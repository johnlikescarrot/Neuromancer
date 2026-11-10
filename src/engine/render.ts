/**
 * Block renderers. Every visual decision for the edition lives here, expressed
 * against the print tokens derived from the Astryx theme.
 */
import { Book, PAGE, METRICS } from "./page.js";
import { parseInline, type Line } from "./text.js";
import type { Block, GlossaryEntry, ChapterGuide } from "../types.js";
import { STATS } from "../content/stats.js";

const GUTTER = 17;
const PAIR_GAP = 6.5;

interface BlockOpts {
  /** Filled in by pass 1: block id -> folio string. */
  tocPages: Map<string, string>;
  onTocPage?: (id: string, folio: string) => void;
}

// --------------------------------------------------------------------- basics

function flow(
  book: Book,
  text: string,
  style: Parameters<Book["drawLines"]>[4],
  opts: { x?: number; width?: number; spaceAfter?: number; spaceBefore?: number; minLines?: number } = {},
): void {
  if (!text) return;
  const x = opts.x ?? book.contentLeft;
  const w = opts.width ?? book.contentWidth;
  const lines = book.lines(parseInline(text), style, w);
  const minLines = opts.minLines ?? 2;
  if (opts.spaceBefore) book.y += opts.spaceBefore;
  if (lines.length && book.y + style.leading * minLines > book.contentBottom) book.newPage();
  let y = book.y;
  for (const line of lines) {
    if (y + style.leading > book.contentBottom) {
      book.newPage();
      y = book.y;
    }
    book.drawLine(line, x, y, w, style);
    y += style.leading;
  }
  book.y = y + (opts.spaceAfter ?? 0);
}

function heading(book: Book, block: Extract<Block, { t: "h1" }>, opts: BlockOpts): void {
  const t = book.tokens;
  book.setRunningHead(block.text);
  if (book.pageIndex > 1) book.newPage();
  if (block.id) {
    opts.onTocPage?.(block.id, book.folio());
    book.bookmark(block.text, 1, true);
  }
  if (block.kicker) {
    book.y = book.label(block.kicker, book.contentLeft, book.y + 6);
  }
  book.y += 8;
  const style = { family: "serif" as const, size: t.type.h1, leading: t.type.h1 * 1.24, color: t.ink };
  flow(book, block.text, style);
  book.rule(book.contentLeft, book.y + 3, book.contentWidth, t.accent, 1.1);
  book.y += 16;
}

function subheading(book: Book, block: Extract<Block, { t: "h2" }>): void {
  const t = book.tokens;
  book.ensure(58);
  book.y += 14;
  const style = { family: "serif" as const, size: t.type.h2, leading: t.type.h2 * 1.3, color: t.ink };
  flow(book, block.text, style);
  if (block.vi) {
    flow(book, block.vi, { family: "sans", size: t.type.small - 0.4, leading: (t.type.small - 0.4) * 1.45, color: t.inkMuted }, { spaceBefore: 2 });
  }
  book.y += 4;
}

function subsubheading(book: Book, block: Extract<Block, { t: "h3" }>): void {
  const t = book.tokens;
  book.ensure(42);
  book.y += 9;
  book.y = book.label(block.text, book.contentLeft, book.y);
  book.y += 2;
}

// ------------------------------------------------------- paired bilingual text

function pairColumns(book: Book, block: Extract<Block, { t: "pair" }>): void {
  const f = book.frame();
  const t = book.tokens;
  const colW = (book.contentWidth - GUTTER) / 2;
  const enStyle = {
    family: "serif" as const,
    size: block.lead ? t.type.body + 0.5 : t.type.body,
    leading: (block.lead ? t.type.body + 0.5 : t.type.body) * 1.36,
    color: t.ink,
    align: "left" as const,
  };
  const viStyle = {
    family: "sans" as const,
    size: t.type.body - 0.9,
    leading: (t.type.body - 0.9) * 1.45,
    color: t.ink,
    align: "left" as const,
  };
  const en = block.en ?? [];
  const vi = block.vi ?? [];
  const count = Math.max(en.length, vi.length);

  for (let p = 0; p < count; p++) {
    let enLines: Line[] = p < en.length ? book.lines(parseInline(en[p]), enStyle, colW) : [];
    let viLines: Line[] = p < vi.length ? book.lines(parseInline(vi[p]), viStyle, colW) : [];
    if (!enLines.length && !viLines.length) continue;

    let ei = 0;
    let viStart = 0;
    for (;;) {
      const need = Math.max((enLines.length - ei) * enStyle.leading, (viLines.length - viStart) * viStyle.leading);
      const room = book.contentBottom - book.y;
      if (need <= room) {
        let ey = book.y;
        for (; ei < enLines.length; ei++) {
          book.drawLine(enLines[ei], f.left, ey, colW, enStyle);
          ey += enStyle.leading;
        }
        let vy = book.y;
        for (; viStart < viLines.length; viStart++) {
          book.drawLine(viLines[viStart], f.left + colW + GUTTER, vy, colW, viStyle);
          vy += viStyle.leading;
        }
        book.y = Math.max(ey, vy) + PAIR_GAP;
        break;
      }
      // Not enough room: fill this page, then continue on the next one.
      const pageRoom = book.contentBottom - book.y;
      if (pageRoom > enStyle.leading * 1.6) {
        let ey = book.y;
        while (ei < enLines.length && ey + enStyle.leading <= book.contentBottom) {
          book.drawLine(enLines[ei], f.left, ey, colW, enStyle);
          ey += enStyle.leading;
          ei++;
        }
        let vy = book.y;
        while (viStart < viLines.length && vy + viStyle.leading <= book.contentBottom) {
          book.drawLine(viLines[viStart], f.left + colW + GUTTER, vy, colW, viStyle);
          vy += viStyle.leading;
          viStart++;
        }
        book.y = Math.max(ey, vy);
      }
      book.newPage();
    }
    void viLines;
    void f;
  }
}

function bullets(book: Book, block: Extract<Block, { t: "bullets" }>): void {
  const t = book.tokens;
  const colW = (book.contentWidth - GUTTER) / 2;
  const enStyle = { family: "serif" as const, size: t.type.body - 0.6, leading: (t.type.body - 0.6) * 1.36, color: t.ink };
  const viStyle = { family: "sans" as const, size: t.type.body - 1.3, leading: (t.type.body - 1.3) * 1.46, color: t.ink };
  const en = block.en ?? [];
  const vi = block.vi ?? [];
  const count = Math.max(en.length, vi.length);
  for (let i = 0; i < count; i++) {
    const enLines = i < en.length ? book.lines(parseInline(en[i]), enStyle, colW - 11) : [];
    const viLines = i < vi.length ? book.lines(parseInline(vi[i]), viStyle, colW - 11) : [];
    const height = Math.max(enLines.length * enStyle.leading, viLines.length * viStyle.leading);
    book.ensure(height + 3);
    const top = book.y;
    book.bar(book.contentLeft + 1.6, top + 3.2, 2.2, 2.2, t.accent);
    book.bar(book.contentLeft + colW + GUTTER + 1.6, top + 3.2, 2.2, 2.2, t.accentSoft);
    let ey = top;
    for (const line of enLines) {
      book.drawLine(line, book.contentLeft + 11, ey, colW - 11, enStyle);
      ey += enStyle.leading;
    }
    let vy = top;
    for (const line of viLines) {
      book.drawLine(line, book.contentLeft + colW + GUTTER + 11, vy, colW - 11, viStyle);
      vy += viStyle.leading;
    }
    book.y = Math.max(ey, vy) + 4.5;
  }
  book.y += 2;
}

// ------------------------------------------------------------------- tables

function table(book: Book, block: Extract<Block, { t: "table" }>): void {
  const t = book.tokens;
  const x0 = book.contentLeft;
  const total = book.contentWidth;
  const sum = block.widths.reduce((a, b) => a + b, 0);
  const cols = block.widths.map((w) => (w / sum) * total);
  const pad = 4.5;
  const cellStyle = { family: "sans" as const, size: t.type.micro + 0.6, leading: (t.type.micro + 0.6) * 1.42, color: t.ink };
  const headStyle = { family: "sans" as const, size: t.type.micro + 0.4, leading: (t.type.micro + 0.4) * 1.4, color: t.ink };

  type Row = Line[][];
  const rowLines = (cells: string[], style: typeof cellStyle): Row =>
    cells.map((c, i) => book.lines(parseInline(c), style, cols[i] - pad * 2));
  const rowHeight = (lines: Row, style: typeof cellStyle): number =>
    Math.max(...lines.map((l) => Math.max(1, l.length) * style.leading)) + pad * 2;

  const drawRow = (cells: Row, style: typeof cellStyle, y: number, fill?: string): number => {
    const h = rowHeight(cells, style);
    if (fill) book.panel(x0, y, total, h, fill);
    let x = x0;
    for (let c = 0; c < cols.length; c++) {
      let cy = y + pad;
      for (const line of cells[c]) {
        book.drawLine(line, x + pad, cy, cols[c] - pad * 2, style);
        cy += style.leading;
      }
      x += cols[c];
    }
    book.rule(x0, y + h, total, t.rule, 0.4);
    return y + h;
  };

  book.ensure(70);
  book.y += 8;
  if (block.caption) {
    flow(book, block.caption, { family: "sans", size: t.type.micro, leading: t.type.micro * 1.5, color: t.inkMuted }, { spaceAfter: 5 });
  }
  const headCells = rowLines(block.head, headStyle);
  let y = book.y;
  const headH = rowHeight(headCells, headStyle);
  book.panel(x0, y, total, headH, t.accentSoft);
  let hx = x0;
  for (let c = 0; c < cols.length; c++) {
    let cy = y + pad;
    for (const line of headCells[c]) {
      book.drawLine(line, hx + pad, cy, cols[c] - pad * 2, headStyle);
      cy += headStyle.leading;
    }
    hx += cols[c];
  }
  y += headH;
  book.rule(x0, y, total, t.accent, 0.8);

  for (let r = 0; r < block.rows.length; r++) {
    const cells = rowLines(block.rows[r], cellStyle);
    const h = rowHeight(cells, cellStyle);
    if (y + h > book.contentBottom) {
      book.y = y;
      book.newPage();
      y = book.y;
      // Repeat the header on continuation pages.
      const hc = rowLines(block.head, headStyle);
      const hh = rowHeight(hc, headStyle);
      book.panel(x0, y, total, hh, t.accentSoft);
      let ax = x0;
      for (let c = 0; c < cols.length; c++) {
        let cy = y + pad;
        for (const line of hc[c]) {
          book.drawLine(line, ax + pad, cy, cols[c] - pad * 2, headStyle);
          cy += headStyle.leading;
        }
        ax += cols[c];
      }
      y += hh;
      book.rule(x0, y, total, t.accent, 0.8);
    }
    y = drawRow(cells, cellStyle, y, block.zebra && r % 2 === 1 ? t.panel : undefined);
  }
  book.y = y + 14;
}

// ------------------------------------------------------------------ glossary

function glossary(book: Book, block: Extract<Block, { t: "glossary" }>): void {
  const t = book.tokens;
  let group = "";
  for (const entry of block.entries) {
    if (block.showGroup && entry.group !== group) {
      group = entry.group;
      book.ensure(90);
      book.y += 16;
      book.y = book.label(GROUP_LABELS[entry.group] ?? group, book.contentLeft, book.y + 2, { size: 8, color: t.accent });
      book.rule(book.contentLeft, book.y + 2, book.contentWidth, t.accent, 0.8);
      book.y += 12;
    }
    renderGlossaryEntry(book, entry);
  }
}

const GROUP_LABELS: Record<string, string> = {
  cyberspace: "Cyberspace & hardware",
  corporate: "Corporate power & tradecraft",
  street: "Street, body & subculture",
  body: "Body, medicine & death",
  ai: "Artificial intelligence & constructs",
  place: "Places, geography & architecture",
  craft: "Gibson's craft — style & coinages",
  academic: "Academic register — writing about the novel",
};

function renderGlossaryEntry(book: Book, entry: GlossaryEntry): void {
  const t = book.tokens;
  const x = book.contentLeft;
  const width = book.contentWidth;
  const termStyle = { family: "serif" as const, size: t.type.body + 0.6, leading: (t.type.body + 0.6) * 1.24, color: t.ink };
  const metaStyle = { family: "sans" as const, size: t.type.micro + 0.1, leading: (t.type.micro + 0.1) * 1.45, color: t.accent };
  const enStyle = { family: "serif" as const, size: t.type.small - 0.3, leading: (t.type.small - 0.3) * 1.42, color: t.ink };
  const viStyle = { family: "sans" as const, size: t.type.small - 0.9, leading: (t.type.small - 0.9) * 1.5, color: t.ink };
  const noteStyle = { family: "serif" as const, size: t.type.small - 1.1, leading: (t.type.small - 1.1) * 1.4, color: t.inkMuted };

  const meta = [entry.pos, entry.level].filter(Boolean).join(" · ");
  const headLine = `**${entry.term}**  *${entry.ipa}*`;
  const metaW = book.measureText(meta.toUpperCase(), "sans", metaStyle.size) + 6;
  const headLines = book.lines(parseInline(headLine), termStyle, width - metaW - 8);

  // Provisional height for the whole entry, so a headword never orphans.
  const enLines = book.lines(parseInline(entry.en), enStyle, width - 10);
  const viLines = book.lines(parseInline(entry.vi), viStyle, width - 10);
  const noteLines = entry.note ? book.lines(parseInline(entry.note), noteStyle, width - 10) : [];
  const height =
    headLines.length * termStyle.leading +
    enLines.length * enStyle.leading +
    viLines.length * viStyle.leading +
    noteLines.length * noteStyle.leading +
    10;
  if (height < (book.contentBottom - book.frame().top) * 0.55) book.ensure(height);
  if (book.y < book.frame().top + 3) book.y = book.frame().top + 3;

  book.bar(x, book.y + 2, 1.6, height - 6, t.accentSoft);

  let y = book.y;
  for (const line of headLines) {
    book.drawLine(line, x + 9, y, width - metaW - 8, termStyle);
    y += termStyle.leading;
  }
  book.doc
    .save()
    .font("SansBold")
    .fontSize(metaStyle.size)
    .fillColor(t.accent)
    .text(meta.toUpperCase(), x, y - termStyle.leading + 3.2, {
      width: width - 6,
      align: "right",
      characterSpacing: 0.9,
      lineBreak: false,
    })
    .restore();
  y += 1.5;
  for (const line of enLines) {
    book.drawLine(line, x + 9, y, width - 10, enStyle);
    y += enStyle.leading;
  }
  for (const line of viLines) {
    book.drawLine(line, x + 9, y, width - 10, viStyle);
    y += viStyle.leading;
  }
  if (noteLines.length) {
    y += 1.5;
    for (const line of noteLines) {
      book.drawLine(line, x + 9, y, width - 10, noteStyle);
      y += noteStyle.leading;
    }
  }
  book.y = y + 9;
}

// ------------------------------------------------------- composite furniture

function cover(book: Book): void {
  const t = book.tokens;
  const d = book.doc;
  book.newPage({ blankDecor: true });
  book.suppressFolio(book.pageIndex);
  d.save();
  d.rect(0, 0, PAGE.w, PAGE.h).fill(t.coverBase);
  // A quiet grid: the matrix as graph paper.
  d.strokeColor("#1b2a30").lineWidth(0.35);
  for (let y = 60; y < PAGE.h; y += 26) {
    d.moveTo(0, y).lineTo(PAGE.w, y).stroke();
  }
  for (let x = 0; x < PAGE.w; x += 26) {
    d.moveTo(x, 0).lineTo(x, PAGE.h).stroke();
  }
  d.rect(0, 0, PAGE.w, PAGE.h).fillOpacity(0).fill("#000");
  d.restore();

  d.save().rect(0, 0, PAGE.w, 96).fill("#0b1013").restore();
  d.save().rect(0, PAGE.h - 150, PAGE.w, 150).fill("#0b1013").restore();

  const left = 34;
  book.label("Bilingual study edition · Anh – Việt", left, 118, { size: 8, color: "#63c8d8", width: PAGE.w - 68 });
  d.save()
    .font("SansBold")
    .fontSize(52)
    .fillColor("#f2f7f8")
    .text("NEUROMANCER", left, 150, { width: PAGE.w - 68, characterSpacing: 1.6, lineBreak: false })
    .restore();
  d.save().moveTo(left, 214).lineTo(left + 120, 214).lineWidth(2.4).strokeColor("#0c6f82").stroke().restore();
  d.save()
    .font("Sans")
    .fontSize(13)
    .fillColor("#a9bcc2")
    .text("William Gibson", left, 228, { width: PAGE.w - 68, characterSpacing: 2.2, lineBreak: false })
    .restore();

  d.save()
    .font("Serif")
    .fontSize(19)
    .fillColor("#e8eff1")
    .text("Reader's Companion, Glossary\n& Exam Workbook", left, PAGE.h - 250, { width: PAGE.w - 68, lineGap: 4 })
    .restore();
  d.save()
    .font("Sans")
    .fontSize(9.6)
    .fillColor("#8fa6ad")
    .text(
      `${STATS.chapters} chapter guides · ${STATS.headwords} CEFR-levelled headwords · twelve rhetoric features · six exam sections with keys`,
      left,
      PAGE.h - 190,
      { width: PAGE.w - 140, lineGap: 3.4 },
    )
    .restore();

  d.save()
    .font("SerifItalic")
    .fontSize(13)
    .fillColor("#7f979e")
    .text(
      "What happens in each chapter,\nwhat the language is doing,\nand what it trains you to do.",
      left,
      300,
      { width: 260, lineGap: 7 },
    )
    .restore();

  // Scope band across the middle of the cover: the void above the imprint is
  // the design's largest empty area, so it carries the book's inventory.
  const bandY = 470;
  d.save().moveTo(left, bandY).lineTo(PAGE.w - left, bandY).lineWidth(0.6).strokeColor("#24424a").stroke().restore();
  const items: [string, string][] = [
    ["PART I", "The Novel\nChapter guides 1–24"],
    ["PART II", "The Apparatus\nRhetoric · lexicon · workbook"],
    ["PART III", "Reference\nMaps, chronology, indexes"],
  ];
  items.forEach(([num, label], i) => {
    const x = left + i * ((PAGE.w - left * 2) / 3);
    d.save().font("SansBold").fontSize(7.2).fillColor("#63c8d8").text(num, x, bandY + 18, { lineBreak: false, characterSpacing: 1.3 }).restore();
    d.save().font("Sans").fontSize(8.4).fillColor("#b9cbd0").text(label, x, bandY + 34, { width: (PAGE.w - left * 2) / 3 - 18, lineGap: 3 }).restore();
  });
  d.save().moveTo(left, bandY + 96).lineTo(PAGE.w - left, bandY + 96).lineWidth(0.6).strokeColor("#24424a").stroke().restore();
  d.save()
    .font("Sans")
    .fontSize(7.6)
    .fillColor("#6f8a92")
    .text("TOEFL 90+ · IELTS 7.0 · PTE 65 · Cambridge 185 · DET 120", left, PAGE.h - 96, {
      width: PAGE.w - 68,
      characterSpacing: 0.9,
      lineBreak: false,
    })
    .restore();
}

function titlepage(book: Book): void {
  const t = book.tokens;
  book.newPage({ blankDecor: true });
  book.suppressFolio(book.pageIndex);
  const d = book.doc;
  const left = book.contentLeft;
  let y = 150;
  book.label("An independent study edition", left, y, { size: 8 });
  y += 26;
  flow(book, "**Neuromancer**", { family: "serif", size: 40, leading: 46, color: t.ink }, { spaceAfter: 6 });
  flow(book, "Reader's Companion, Glossary & Exam Workbook", {
    family: "serif",
    size: 15,
    leading: 21,
    color: t.ink,
  }, { spaceAfter: 18 });
  book.rule(left, book.y, 90, t.accent, 1.6);
  book.y += 18;
  flow(book, "A bilingual (English – Vietnamese) critical apparatus for the novel by **William Gibson**", {
    family: "sans",
    size: 10,
    leading: 16,
    color: t.inkMuted,
  }, { spaceAfter: 40 });
  flow(book, "Phiên bản nghiên cứu song ngữ Anh – Việt: cẩm nang đọc hiểu, từ điển thuật ngữ và sách bài tập nâng cấp năng lực tiếng Anh học thuật.", {
    family: "sans",
    size: 9,
    leading: 15,
    color: t.inkMuted,
  });
  const baseY = PAGE.h - METRICS.bottom - 70;
  book.rule(left, baseY, book.contentWidth, t.rule, 0.4);
  book.y = baseY + 10;
  flow(book, "Typeset with a TypeScript build pipeline · design tokens projected from the Astryx design system", {
    family: "sans",
    size: 7.6,
    leading: 12,
    color: t.inkMuted,
  });
}

function colophon(book: Book): void {
  const t = book.tokens;
  book.newPage();
  book.setRunningHead("");
  const left = book.contentLeft;
  book.y = book.frame().top + 20;
  book.y = book.label("Colophon & provenance", left, book.y, { size: 8 });
  book.y += 10;

  const blocks: [string, string][] = [
    [
      "What this book is",
      "A reader's companion to *Neuromancer*: twenty-four chapter guides, a levelled glossary of Gibson's vocabulary, a compendium of his rhetoric and grammar, and an exam workbook calibrated to C1 Advanced / C2 Proficiency. It is written for readers who want to understand the novel and to leave it with better English than they arrived with.",
    ],
    [
      "What this book is not",
      "It is not a reprint, and it is not a translation, of the novel. No chapter or scene of *Neuromancer* is reproduced here. Where the apparatus needs to point at Gibson's wording — a turn of phrase, a coinage, a syntactic habit — it quotes a few words at most, in the manner of a critical study, and always in order to analyse them. Readers need a copy of the novel beside them; this volume is designed to sit next to it, not instead of it.",
    ],
    [
      "Editorial method",
      "Chapter guides are original summaries and analysis. Vietnamese text is an original companion translation of the apparatus, written for Vietnamese learners reading the novel in English, and is set in the sans face so the two languages never blur at a glance. Every headword in the glossary carries IPA, a part of speech, a CEFR band and a note on why it earns its place.",
    ],
    [
      "How it is made",
      "The edition is generated by a TypeScript pipeline: content modules define a typed document model, a layout engine breaks lines, paginates, aligns the bilingual columns and writes the PDF with PDFKit. Colour and type scales are read at build time from the Astryx neutral theme, the Meta open-source design system, so the printed page speaks the same visual language as a modern product interface. Fonts: DejaVu Serif and DejaVu Sans — chosen for full Vietnamese diacritic coverage.",
    ],
    [
      "Rights",
      "William Gibson's novel remains in copyright and is quoted here only in short critical phrases. This companion is an unofficial study aid, not authorised by the author or his publishers; all editorial prose, glosses, exercises and answer keys are original to this project. Distributed for study and research in the spirit of fair use and fair dealing.",
    ],
  ];

  for (const [head, body] of blocks) {
    book.y += 8;
    flow(book, head, { family: "serif", size: t.type.h3 + 1.4, leading: (t.type.h3 + 1.4) * 1.3, color: t.ink }, { spaceAfter: 3 });
    flow(book, body, { family: "serif", size: t.type.small - 0.1, leading: (t.type.small - 0.1) * 1.55, color: t.ink }, { spaceAfter: 6 });
  }
}

function divider(book: Book, block: Extract<Block, { t: "divider" }>, opts: BlockOpts): void {
  const t = book.tokens;
  book.setRunningHead(block.title);
  book.newPage();
  book.startMainMatter();
  opts.onTocPage?.(block.id, book.folio());
  book.bookmark(block.title, 1, true);
  const d = book.doc;
  const top = 200;
  d.save().rect(book.contentLeft, top - 60, 3, 210).fill(t.accent).restore();
  book.label(block.kicker, book.contentLeft + 18, top - 54, { size: 9 });
  d.save()
    .font("SerifBold")
    .fontSize(t.type.part + 6)
    .fillColor(t.ink)
    .text(block.title, book.contentLeft + 18, top - 30, { width: book.contentWidth - 40, lineGap: 2 })
    .restore();
  let y = book.doc.y + 14;
  if (block.subtitle) {
    d.save().font("Sans").fontSize(11).fillColor(t.inkMuted).text(block.subtitle, book.contentLeft + 18, y, { width: book.contentWidth - 40 }).restore();
    y = d.y + 12;
  }
  if (block.en) {
    book.y = y;
    flow(book, block.en, { family: "serif", size: 10, leading: 15.4, color: t.ink }, { x: book.contentLeft + 18, width: book.contentWidth - 60, spaceAfter: 8 });
  }
  if (block.vi) {
    flow(book, block.vi, { family: "sans", size: 8.6, leading: 14, color: t.inkMuted }, { x: book.contentLeft + 18, width: book.contentWidth - 60 });
  }
}

// ------------------------------------------------------------------- chapters

function chapter(book: Book, guide: ChapterGuide, opts: BlockOpts): void {
  const t = book.tokens;
  book.setRunningHead(`Chapter ${guide.num} — ${guide.title}`);
  book.newPage();
  opts.onTocPage?.(`chapter-${guide.num}`, book.folio());
  book.bookmark(`${guide.num}. ${guide.title}`, 2);

  const left = book.contentLeft;
  const indent = 72;
  book.y = book.frame().top + 2;
  // Numeral, in the margin of the text block.
  book.doc
    .save()
    .font("SansBold")
    .fontSize(30)
    .fillColor(t.accentSoft)
    .text(String(guide.num).padStart(2, "0"), left - 2, book.frame().top - 2, { width: 60, lineBreak: false })
    .restore();
  book.label(guide.part, left + indent, book.frame().top + 1, { size: 6.4, width: book.contentWidth - indent });
  book.y = book.frame().top + 13;
  flow(book, `**${guide.title}**`, { family: "serif", size: t.type.h1 - 1.5, leading: (t.type.h1 - 1.5) * 1.22, color: t.ink }, { x: left + indent, width: book.contentWidth - indent, spaceAfter: 2 });
  flow(book, guide.titleVi, { family: "sans", size: t.type.small - 0.4, leading: (t.type.small - 0.4) * 1.45, color: t.inkMuted }, { x: left + indent, width: book.contentWidth - indent });
  book.y += 8;
  book.rule(left, book.y, book.contentWidth, t.accent, 1.1);
  book.y += 10;

  book.y = book.label("Synopsis · Tóm lược", left, book.y, { size: 6.6 });
  book.y += 4;
  pairColumns(book, { t: "pair", en: [guide.synopsisEn], vi: [guide.synopsisVi] });

  if (guide.watchEn.length || guide.watchVi.length) {
    book.ensure(70);
    book.y = book.label("What to watch · Điểm cần chú ý", left, book.y + 8, { size: 6.6 });
    book.y += 6;
    bullets(book, { t: "bullets", en: guide.watchEn, vi: guide.watchVi });
  }

  if (guide.focus.length) {
    book.ensure(70);
    book.y = book.label("Language focus · Trọng tâm ngôn ngữ", left, book.y + 8, { size: 6.6 });
    book.y += 8;
    for (const f of guide.focus) {
      book.ensure(52);
      flow(book, `**${f.label}**`, { family: "sans", size: t.type.small - 0.6, leading: (t.type.small - 0.6) * 1.4, color: t.accent }, { spaceAfter: 2 });
      flow(book, f.en, { family: "serif", size: t.type.small - 0.2, leading: (t.type.small - 0.2) * 1.5, color: t.ink }, { spaceAfter: 2 });
      flow(book, f.vi, { family: "sans", size: t.type.small - 1.1, leading: (t.type.small - 1.1) * 1.5, color: t.inkMuted }, { spaceAfter: 3 });
      if (f.example) {
        flow(book, `*${f.example}*`, { family: "serif", size: t.type.small - 0.6, leading: (t.type.small - 0.6) * 1.44, color: t.accent }, { spaceAfter: 8 });
      } else {
        book.y += 5;
      }
    }
  }

  if (guide.terms.length) {
    book.ensure(46);
    book.y = book.label("Lexicon", left, book.y + 6, { size: 6.6 });
    book.y += 5;
    flow(book, guide.terms.join("  ·  "), { family: "sans", size: t.type.small - 1.4, leading: (t.type.small - 1.4) * 1.6, color: t.ink });
  }
}

// ------------------------------------------------------------------------ TOC

export interface TocItem {
  level: 1 | 2;
  text: string;
  id: string;
  page?: string;
}

function toc(book: Book, items: TocItem[]): void {
  const t = book.tokens;
  book.newPage();
  book.setRunningHead("Contents");
  const left = book.contentLeft;
  book.y = book.frame().top + 8;
  flow(book, "**Contents**", { family: "serif", size: t.type.h1, leading: t.type.h1 * 1.2, color: t.ink }, { spaceAfter: 2 });
  flow(book, "Mục lục", { family: "sans", size: t.type.small, leading: t.type.small * 1.4, color: t.inkMuted }, { spaceAfter: 12 });
  book.rule(left, book.y, book.contentWidth, t.accent, 1);

  for (const item of items) {
    const isPart = item.level === 1;
    const style = {
      family: (isPart ? "sans" : "serif") as "sans" | "serif",
      size: isPart ? t.type.small - 0.4 : t.type.body - 0.4,
      leading: (isPart ? t.type.small - 0.4 : t.type.body - 0.4) * (isPart ? 1.9 : 1.5),
      color: isPart ? t.accent : t.ink,
    };
    const indent = isPart ? 0 : 18;
    if (isPart && book.y > book.frame().top + 40) book.y += 9;
    book.ensure(style.leading * 2);
    const page = item.page ?? "";
    const pageW = 26;
    const titleW = book.contentWidth - indent - pageW - 8;
    const titleText = isPart ? item.text.toUpperCase() : item.text;
    const tw = book.measureText(titleText, style.family, style.size, isPart ? 0.9 : 0);
    const dotsStart = left + indent + Math.min(tw, titleW) + 5;
    const dotsEnd = left + book.contentWidth - pageW - 4;
    if (book.y < book.contentBottom - style.leading) {
      book.doc
        .save()
        .font(isPart ? "SansBold" : "Serif")
        .fontSize(style.size)
        .fillColor(style.color)
        .text(titleText, left + indent, book.y + 1.5, { lineBreak: false, characterSpacing: isPart ? 0.9 : 0 })
        .restore();
      book.doc
        .save()
        .font("Sans")
        .fontSize(style.size)
        .fillColor(style.color)
        .text(page, left + book.contentWidth - pageW, book.y + 1.5, { width: pageW, align: "right", lineBreak: false })
        .restore();
      if (dotsEnd > dotsStart) {
        const baseline = book.y + style.size * 0.86;
        book.doc
          .save()
          .font("Sans")
          .fontSize(style.size * 0.82)
          .fillColor(t.rule)
          .text(".  ".repeat(Math.max(2, Math.floor((dotsEnd - dotsStart) / 3.1))), dotsStart, baseline, { lineBreak: false, baseline: "alphabetic", characterSpacing: 0.1 })
          .restore();
      }
    } else {
      book.newPage();
      book.doc.save().font(isPart ? "SansBold" : "Serif").fontSize(style.size).fillColor(style.color)
        .text(titleText, left + indent, book.y + 1.5, { lineBreak: false }).restore();
      book.doc.save().font("Sans").fontSize(style.size).fillColor(style.color)
        .text(page, left + book.contentWidth - pageW, book.y + 1.5, { width: pageW, align: "right", lineBreak: false }).restore();
    }
    book.y += style.leading + (isPart ? 3 : 0);
  }
}

// ------------------------------------------------------------------ dispatcher

export function renderBlocks(book: Book, blocks: Block[], tocItems: TocItem[], opts: BlockOpts): void {
  for (const block of blocks) {
    switch (block.t) {
      case "cover":
        cover(book);
        break;
      case "titlepage":
        titlepage(book);
        break;
      case "colophon":
        colophon(book);
        break;
      case "toc":
        toc(book, tocItems);
        break;
      case "divider":
        divider(book, block, opts);
        break;
      case "h1":
        heading(book, block, opts);
        break;
      case "h2":
        subheading(book, block);
        break;
      case "h3":
        subsubheading(book, block);
        break;
      case "pair":
        pairColumns(book, block);
        break;
      case "bullets":
        bullets(book, block);
        break;
      case "table":
        table(book, block);
        break;
      case "glossary":
        glossary(book, block);
        break;
      case "callout":
        callout(book, block);
        break;
      case "quote":
        quote(book, block);
        break;
      case "rule":
        book.y += 10;
        book.rule(book.contentLeft, book.y, book.contentWidth, book.tokens.rule, 0.4);
        book.y += 10;
        break;
      case "pagebreak":
        book.newPage();
        break;
      case "chapter":
        chapter(book, block.guide, opts);
        break;
    }
  }
}

function callout(book: Book, block: Extract<Block, { t: "callout" }>): void {
  const t = book.tokens;
  const x = book.contentLeft;
  const w = book.contentWidth;
  const pad = 12;
  const enStyle = { family: "serif" as const, size: t.type.small - 0.2, leading: (t.type.small - 0.2) * 1.5, color: t.ink };
  const viStyle = { family: "sans" as const, size: t.type.small - 1.1, leading: (t.type.small - 1.1) * 1.5, color: t.inkMuted };
  const enLines = (block.en ?? []).flatMap((p) => book.lines(parseInline(p), enStyle, w - pad * 2 - 4));
  const viLines = (block.vi ?? []).flatMap((p) => book.lines(parseInline(p), viStyle, w - pad * 2 - 4));
  const h = enLines.length * enStyle.leading + viLines.length * viStyle.leading + pad * 2 + 16;
  book.ensure(h + 10);
  const top = book.y;
  book.panel(x, top, w, h, t.panel);
  book.bar(x, top, 3, h, t.accent);
  let y = top + pad;
  book.label(block.label, x + pad, y, { size: 6.6 });
  y += 11;
  for (const line of enLines) {
    book.drawLine(line, x + pad, y, w - pad * 2 - 4, enStyle);
    y += enStyle.leading;
  }
  y += 3;
  for (const line of viLines) {
    book.drawLine(line, x + pad, y, w - pad * 2 - 4, viStyle);
    y += viStyle.leading;
  }
  book.y = top + h + 12;
}

function quote(book: Book, block: Extract<Block, { t: "quote" }>): void {
  const t = book.tokens;
  const style = { family: "serif" as const, size: t.type.body + 0.6, leading: (t.type.body + 0.6) * 1.5, color: t.ink };
  const lines = book.lines(parseInline(block.text), style, book.contentWidth - 34);
  book.ensure(lines.length * style.leading + 20);
  const top = book.y + 6;
  book.bar(book.contentLeft + 3, top, 1.4, lines.length * style.leading - 2, t.accent);
  let y = top;
  for (const line of lines) {
    book.drawLine(line, book.contentLeft + 18, y, book.contentWidth - 34, style);
    y += style.leading;
  }
  book.y = y;
  if (block.cite) {
    flow(book, block.cite, { family: "sans", size: t.type.micro + 0.3, leading: 11, color: t.inkMuted }, { x: book.contentLeft + 18, width: book.contentWidth - 40, spaceBefore: 4 });
  }
  book.y = Math.max(book.y, y) + 10;
}
