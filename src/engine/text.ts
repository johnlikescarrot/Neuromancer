/**
 * Inline text model: lightweight markup, measurement, and line breaking.
 *
 * PDFKit can flow text by itself, but a book needs explicit control over line
 * breaking: paired bilingual columns, hanging indent, widow control and exact
 * baseline placement. So we measure words ourselves and place each line.
 */
import type { Run, Style } from "../types.js";

export type Family = "serif" | "sans" | "mono";

const STYLE_SUFFIX: Record<Style, string> = { r: "", i: "I", b: "B", bi: "BI" };

export function fontName(family: Family, style: Style): string {
  const base = family === "serif" ? "Serif" : family === "sans" ? "Sans" : "Mono";
  const bold = style === "b" || style === "bi" ? "Bold" : "";
  const italic = style === "i" || style === "bi" ? "Oblique" : "";
  if (family === "mono") return bold ? "MonoBold" : "Mono";
  if (family === "sans") return `Sans${bold}${italic}`;
  // DejaVu Serif ships Italic/BoldItalic under different names.
  if (style === "i") return "SerifItalic";
  if (style === "b") return "SerifBold";
  if (style === "bi") return "SerifBoldItalic";
  return `Serif${STYLE_SUFFIX.r}`;
}

/**
 * Parse a tiny inline markup: `*italic*`, `**bold**`, `***bold italic***`.
 * Anything else is literal, so typographic quotes and dashes survive untouched.
 */
export function parseInline(input: string): Run[] {
  const runs: Run[] = [];
  let buffer = "";
  let i = 0;
  const flush = (style: Style) => {
    if (buffer) runs.push({ text: buffer, style });
    buffer = "";
  };
  while (i < input.length) {
    if (input.startsWith("***", i)) {
      const end = input.indexOf("***", i + 3);
      if (end > i) {
        flush("r");
        runs.push({ text: input.slice(i + 3, end), style: "bi" });
        i = end + 3;
        continue;
      }
    }
    if (input.startsWith("**", i)) {
      const end = input.indexOf("**", i + 2);
      if (end > i) {
        flush("r");
        runs.push({ text: input.slice(i + 2, end), style: "b" });
        i = end + 2;
        continue;
      }
    }
    if (input[i] === "*") {
      const end = input.indexOf("*", i + 1);
      if (end > i) {
        flush("r");
        runs.push({ text: input.slice(i + 1, end), style: "i" });
        i = end + 1;
        continue;
      }
    }
    buffer += input[i];
    i += 1;
  }
  flush("r");
  return runs.length ? runs : [{ text: "", style: "r" }];
}

export interface LineItem {
  text: string;
  style: Style;
  w: number;
  /** True when a word space separates this item from the previous one. */
  spaceBefore: boolean;
}

export interface Line {
  items: LineItem[];
  width: number;
  spaces: number;
  /** True when the line closes a paragraph (never justified). */
  last: boolean;
  /** True when the line ends because of an explicit break, not wrapping. */
  hard: boolean;
}

interface Word {
  text: string;
  style: Style;
  spaceBefore: boolean;
}

export interface BreakOptions {
  family: Family;
  size: number;
  width: number;
  /** Extra tracking in points applied to every glyph when measuring. */
  tracking?: number;
}

export class Typesetter {
  private cache = new Map<string, number>();

  constructor(private doc: PDFKit.PDFDocument) {}

  measure(text: string, family: Family, style: Style, size: number, tracking = 0): number {
    if (!text) return 0;
    const key = `${family}|${style}|${size}|${tracking}|${text}`;
    const hit = this.cache.get(key);
    if (hit !== undefined) return hit;
    this.doc.font(fontName(family, style)).fontSize(size);
    let w: number;
    if (tracking) {
      w = 0;
      for (const ch of text) w += this.doc.widthOfString(ch) + tracking;
    } else {
      w = this.doc.widthOfString(text);
    }
    if (this.cache.size > 60000) this.cache.clear();
    this.cache.set(key, w);
    return w;
  }

  private tokenize(runs: Run[]): Word[] {
    const words: Word[] = [];
    let pendingSpace = false;
    for (const run of runs) {
      const parts = run.text.split(/(\s+)/);
      for (const part of parts) {
        if (!part) continue;
        if (/^\s+$/.test(part)) {
          pendingSpace = true;
          continue;
        }
        words.push({ text: part, style: run.style, spaceBefore: pendingSpace });
        pendingSpace = false;
      }
    }
    return words;
  }

  break(runs: Run[], opts: BreakOptions): Line[] {
    const { family, size, width } = opts;
    const tracking = opts.tracking ?? 0;
    const words = this.tokenize(runs);
    const lines: Line[] = [];
    let items: LineItem[] = [];
    let lineWidth = 0;
    let spaces = 0;

    const push = (last: boolean, hard = false) => {
      lines.push({ items, width: lineWidth, spaces, last, hard });
      items = [];
      lineWidth = 0;
      spaces = 0;
    };

    const spaceW = this.measure("\u00a0", family, "r", size, tracking);

    for (const word of words) {
      const w = this.measure(word.text, family, word.style, size, tracking);
      const gap = word.spaceBefore && items.length ? spaceW : 0;

      if (items.length && lineWidth + gap + w > width + 0.01) {
        push(false);
      }

      if (w > width && !items.length) {
        // A single unbreakable token wider than the column: hard-split it.
        let chunk = "";
        let chunkW = 0;
        for (const ch of word.text) {
          const cw = this.measure(ch, family, word.style, size, tracking);
          if (chunk && chunkW + cw > width) {
            items.push({ text: chunk, style: word.style, w: chunkW, spaceBefore: false });
            lineWidth += chunkW;
            push(false, true);
            chunk = "";
            chunkW = 0;
          }
          chunk += ch;
          chunkW += cw;
        }
        if (chunk) {
          items.push({ text: chunk, style: word.style, w: chunkW, spaceBefore: false });
          lineWidth += chunkW;
        }
        continue;
      }

      if (gap) {
        spaces += 1;
        lineWidth += spaceW;
      } else if (items.length && lineWidth > 0) {
        // consecutive tokens without whitespace (markup boundary) — no gap
      }
      items.push({ text: word.text, style: word.style, w, spaceBefore: gap > 0 });
      lineWidth += w;
    }

    push(true);
    // Trailing empty line when the paragraph ends on a full line
    if (lines.length > 1) {
      const lastLine = lines[lines.length - 1];
      if (!lastLine.items.length) lines.pop();
      else lastLine.last = true;
    }
    return lines;
  }
}
