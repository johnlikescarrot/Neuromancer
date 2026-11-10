/**
 * Page architecture and typographic primitives.
 *
 * A4, mirrored margins, running heads, folios in two numbering systems (roman
 * front matter, arabic main matter), PDF outline bookmarks, and a line-level
 * drawing layer that the block renderers compose.
 */
import PDFDocument from "pdfkit";
import { Typesetter, fontName, type Family, type Line } from "./text.js";
import type { Style } from "../types.js";
import type { PrintTokens } from "../design/tokens.js";

const MM = 72 / 25.4;
export const PAGE = { w: 210 * MM, h: 297 * MM };

export const METRICS = {
  top: 22 * MM,
  bottom: 24 * MM,
  outer: 21 * MM,
  inner: 28 * MM,
  headGap: 9 * MM,
  folioGap: 11 * MM,
};

export interface Frame {
  left: number;
  width: number;
  top: number;
  bottom: number;
  right: number;
}

export interface TextStyle {
  family: Family;
  size: number;
  leading: number;
  color?: string;
  align?: "left" | "justify" | "right" | "center";
  tracking?: number;
}

const ROMAN: [number, string][] = [
  [1000, "m"],
  [900, "cm"],
  [500, "d"],
  [400, "cd"],
  [100, "c"],
  [90, "xc"],
  [50, "l"],
  [40, "xl"],
  [10, "x"],
  [9, "ix"],
  [5, "v"],
  [4, "iv"],
  [1, "i"],
];

export function roman(n: number): string {
  let out = "";
  let v = n;
  for (const [value, glyph] of ROMAN) {
    while (v >= value) {
      out += glyph;
      v -= value;
    }
  }
  return out;
}

export interface PageDeps {
  tokens: PrintTokens;
  measure: boolean;
  tocPages: Map<string, string>;
  onTocPage?: (id: string, folio: string) => void;
}

export class Book {
  readonly doc: PDFKit.PDFDocument;
  readonly ts: Typesetter;
  readonly tokens: PrintTokens;
  private deps: PageDeps;

  /** 0-based physical page index. */
  pageIndex = 0;
  /** First physical page of the arabic-numbered main matter. */
  private mainStart: number | null = null;
  private pendingMain = false;
  private runningHead = "";
  private runningHeadLeft = "NEUROMANCER · STUDY EDITION";
  private hideFolio = new Set<number>();
  y = 0;

  constructor(deps: PageDeps, sink: NodeJS.WritableStream) {
    this.deps = deps;
    this.tokens = deps.tokens;
    this.doc = new PDFDocument({
      size: [PAGE.w, PAGE.h],
      margins: { top: 0, bottom: 0, left: 0, right: 0 },
      bufferPages: true,
      autoFirstPage: false,
      pdfVersion: "1.7",
      info: {
        Title:
          "Neuromancer — Bilingual Study Edition: Reader's Companion, Glossary & Exam Workbook",
        Author: "Independent editorial project (johnlikescarrot/Neuromancer)",
        Subject:
          "Critical companion and English-language study apparatus for William Gibson's Neuromancer",
        Keywords:
          "Neuromancer, William Gibson, cyberpunk, bilingual edition, CEFR C1/C2, IELTS, TOEFL, PTE, Cambridge English, DET",
        Creator: "neuromancer-edition (TypeScript / PDFKit)",
      },
      lang: "en",
    });
    this.doc.pipe(sink);
    this.ts = new Typesetter(this.doc);
  }

  registerFonts(dir: string): void {
    const d = this.doc;
    d.registerFont("Serif", `${dir}/DejaVuSerif.ttf`);
    d.registerFont("SerifBold", `${dir}/DejaVuSerif-Bold.ttf`);
    d.registerFont("SerifItalic", `${dir}/DejaVuSerif-Italic.ttf`);
    d.registerFont("SerifBoldItalic", `${dir}/DejaVuSerif-BoldItalic.ttf`);
    d.registerFont("Sans", `${dir}/DejaVuSans.ttf`);
    d.registerFont("SansBold", `${dir}/DejaVuSans-Bold.ttf`);
    d.registerFont("SansOblique", `${dir}/DejaVuSans-Oblique.ttf`);
    d.registerFont("SansBoldOblique", `${dir}/DejaVuSans-BoldOblique.ttf`);
    d.registerFont("Mono", `${dir}/DejaVuSansMono.ttf`);
    d.registerFont("MonoBold", `${dir}/DejaVuSansMono-Bold.ttf`);
  }

  // ---------------------------------------------------------------- geography

  get isRecto(): boolean {
    return this.pageIndex % 2 === 0; // physical page 1 is a recto, so index 0 is too
  }

  frame(): Frame {
    const left = this.isRecto ? METRICS.inner : METRICS.outer;
    const right = this.isRecto ? METRICS.outer : METRICS.inner;
    return {
      left,
      right: PAGE.w - right,
      width: PAGE.w - left - right,
      top: METRICS.top,
      bottom: PAGE.h - METRICS.bottom,
    };
  }

  get contentBottom(): number {
    return this.frame().bottom;
  }

  get contentLeft(): number {
    return this.frame().left;
  }

  get contentWidth(): number {
    return this.frame().width;
  }

  /** Display folio for the current page, or "" when the page carries none. */
  folio(): string {
    if (this.pageIndex === 0 || this.hideFolio.has(this.pageIndex)) return "";
    if (this.mainStart === null) return roman(this.pageIndex + 1);
    return String(this.pageIndex - this.mainStart + 1);
  }

  startMainMatter(): void {
    if (this.mainStart === null) this.pendingMain = true;
  }

  get inMainMatter(): boolean {
    return this.mainStart !== null;
  }

  setRunningHead(text: string): void {
    this.runningHead = text;
  }

  suppressFolio(page = this.pageIndex): void {
    this.hideFolio.add(page);
  }

  // ------------------------------------------------------------------- pages

  newPage(opts: { blankDecor?: boolean } = {}): void {
    this.doc.addPage();
    this.pageIndex = this.doc.bufferedPageRange().count - 1;
    if (this.pendingMain) {
      this.mainStart = this.pageIndex;
      this.pendingMain = false;
    }
    const f = this.frame();
    this.y = f.top;
    this.doc.x = f.left;
    if (!opts.blankDecor) this.decorate();
  }

  /** Draws running head, folio and edge rule for the current page. */
  decorate(): void {
    if (this.pageIndex === 0) return;
    const f = this.frame();
    const d = this.doc;
    const t = this.tokens;

    // Running head: book title on verso, current section on recto.
    const head = this.isRecto ? this.runningHead : this.runningHeadLeft;
    if (head) {
      d.save();
      d.font("Sans")
        .fontSize(6.6)
        .fillColor(t.inkMuted)
        .text(head.toUpperCase(), f.left, METRICS.top - 16, {
          width: f.width,
          align: this.isRecto ? "left" : "right",
          characterSpacing: 1.1,
          lineBreak: false,
        });
      d.restore();
    }

    d.save();
    d.moveTo(f.left, METRICS.top - 6.5)
      .lineTo(f.right, METRICS.top - 6.5)
      .lineWidth(0.4)
      .strokeColor(t.rule)
      .stroke();
    d.restore();

    const folio = this.folio();
    if (folio) {
      d.save();
      d.font("Sans")
        .fontSize(7.4)
        .fillColor(this.inMainMatter ? t.ink : t.inkMuted)
        .text(folio, f.left, PAGE.h - METRICS.bottom + 14, {
          width: f.width,
          align: this.isRecto ? "left" : "right",
          lineBreak: false,
        });
      d.restore();
    }
  }

  bookmark(title: string, level: number, expanded = false): void {
    if (this.deps.measure) return;
    try {
      const outline = this.doc.outline;
      // PDFKit tracks the current page automatically; nesting is by call order.
      void level;
      outline.addItem(title, { expanded });
    } catch {
      /* outline is a nicety — never fail a build over it */
    }
  }

  // ---------------------------------------------------------------- drawing

  ensure(height: number): void {
    if (this.y + height > this.contentBottom) this.newPage();
  }

  /** Baseline offset inside a line box, so mixed fonts sit on the same line. */
  private baseline(lineTop: number, size: number, leading: number): number {
    const ascent = size * 0.928;
    return lineTop + (leading - size * 1.164) / 2 + ascent;
  }

  setStyle(style: Style, family: Family, size: number, color: string): this {
    this.doc.font(fontName(family, style)).fontSize(size).fillColor(color);
    return this;
  }

  drawLine(
    line: Line,
    x: number,
    lineTop: number,
    targetWidth: number,
    style: TextStyle,
    flow: "ltr" | "rtl" = "ltr",
  ): void {
    const { family, size, leading, color = this.tokens.ink, align = "left", tracking = 0 } = style;
    const y = this.baseline(lineTop, size, leading);
    const justify =
      (align === "justify" && !line.last && line.spaces > 0) || align === "justify" && line.hard === false && !line.last;
    const extra =
      align === "justify"
        ? Math.max(0, targetWidth - line.width) / Math.max(1, line.spaces)
        : 0;
    let cursor = x;
    if (align === "right") cursor = x + targetWidth - line.width;
    if (align === "center") cursor = x + (targetWidth - line.width) / 2;
    const gapExtra = align === "justify" && !line.last ? extra : 0;

    for (let i = 0; i < line.items.length; i++) {
      const item = line.items[i];
      this.doc
        .font(fontName(family, item.style))
        .fontSize(size)
        .fillColor(color)
        .text(item.text, cursor, y, {
          lineBreak: false,
          baseline: "alphabetic",
          characterSpacing: tracking,
        });
      cursor += item.w;
      const next = line.items[i + 1];
      if (next && next.spaceBefore) {
        const spaceW = this.ts.measure("\u00a0", family, "r", size, tracking);
        cursor += spaceW + gapExtra;
      }
    }
    void justify;
    void flow;
  }

  /** Lay out a block of prose lines; returns the y after the last line. */
  drawLines(
    lines: Line[],
    x: number,
    startY: number,
    width: number,
    style: TextStyle,
  ): number {
    let y = startY;
    for (const line of lines) {
      this.drawLine(line, x, y, width, style);
      y += style.leading;
    }
    return y;
  }

  rule(x: number, y: number, width: number, color?: string, weight = 0.5): void {
    this.doc
      .save()
      .moveTo(x, y)
      .lineTo(x + width, y)
      .lineWidth(weight)
      .strokeColor(color ?? this.tokens.rule)
      .stroke()
      .restore();
  }

  panel(x: number, y: number, w: number, h: number, fill: string, radius = 0): void {
    this.doc.save();
    if (radius > 0) {
      this.doc.roundedRect(x, y, w, h, radius).fill(fill);
    } else {
      this.doc.rect(x, y, w, h).fill(fill);
    }
    this.doc.restore();
  }

  bar(x: number, y: number, h: number, w: number, color: string): void {
    this.doc.save().rect(x, y, w, h).fill(color).restore();
  }

  /** Small-caps-ish label: uppercase sans, tracked, in accent ink. */
  label(text: string, x: number, y: number, opts: { size?: number; color?: string; width?: number; align?: "left" | "right" | "center" } = {}): number {
    const size = opts.size ?? 6.9;
    this.doc
      .save()
      .font("SansBold")
      .fontSize(size)
      .fillColor(opts.color ?? this.tokens.accent)
      .text(text.toUpperCase(), x, y, {
        width: opts.width ?? this.contentWidth,
        align: opts.align ?? "left",
        characterSpacing: 1.15,
        lineBreak: false,
      })
      .restore();
    return y + size * 1.5;
  }

  end(): Promise<void> {
    return new Promise((resolve, reject) => {
      const d = this.doc;
      d.on("error", reject);
      d.on("end", () => resolve());
      d.end();
    });
  }

  // --- measurement helpers -------------------------------------------------

  lines(runs: ReturnType<typeof import("./text.js").parseInline>, style: TextStyle, width: number): Line[] {
    return this.ts.break(runs, {
      family: style.family,
      size: style.size,
      width,
      tracking: style.tracking,
    });
  }

  measureText(text: string, family: Family, size: number, tracking = 0): number {
    return this.ts.measure(text, family, "r", size, tracking);
  }
}
