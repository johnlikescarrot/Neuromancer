import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import fontkit from '@pdf-lib/fontkit';
import { PDFDocument, PDFFont, PDFPage, rgb, StandardFonts } from 'pdf-lib';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const OUTPUT = path.join(ROOT, 'output/neuromancer_english_study_companion.pdf');
const PAGE = { width: 595.28, height: 841.89 };
const MARGIN = 54;
const CONTENT_WIDTH = PAGE.width - MARGIN * 2;

// Values and hierarchy follow the light Astryx neutral theme and its documented
// semantic color/spacing tokens. Astryx is a UI design system; pdf-lib performs
// the actual print-PDF composition.
const C = {
  ink: rgb(10 / 255, 19 / 255, 23 / 255),        // --color-text-primary
  secondary: rgb(78 / 255, 96 / 255, 111 / 255),// --color-text-secondary
  accent: rgb(0, 100 / 255, 224 / 255),         // --color-accent
  paper: rgb(1, 1, 1),                           // --color-background-surface
  body: rgb(241 / 255, 244 / 255, 247 / 255),   // --color-background-body
  border: rgb(204 / 255, 211 / 255, 219 / 255), // --color-border-emphasized
  paleBlue: rgb(232 / 255, 241 / 255, 252 / 255),
  paleGold: rgb(252 / 255, 247 / 255, 231 / 255),
  gold: rgb(151 / 255, 102 / 255, 6 / 255),
  white: rgb(1, 1, 1),
};

function fontPath(): string {
  const candidates = [
    process.env.NEUROMANCER_FONT,
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
  ].filter((value): value is string => Boolean(value));
  const found = candidates.find(existsSync);
  if (!found) {
    throw new Error('No Unicode TTF font found. Set NEUROMANCER_FONT to a DejaVu Sans or Liberation Sans TTF file.');
  }
  return found;
}

function wrap(text: string, font: PDFFont, size: number, maxWidth: number): string[] {
  const lines: string[] = [];
  for (const para of text.split('\n')) {
    if (para.length === 0) { lines.push(''); continue; }
    let line = '';
    for (const word of para.split(/\s+/)) {
      const candidate = line ? `${line} ${word}` : word;
      if (line && font.widthOfTextAtSize(candidate, size) > maxWidth) {
        lines.push(line);
        line = word;
      } else {
        line = candidate;
      }
    }
    if (line) lines.push(line);
  }
  return lines;
}

class GuideWriter {
  readonly pages: PDFPage[] = [];
  private page!: PDFPage;
  private y = 0;

  constructor(
    private readonly doc: PDFDocument,
    private readonly regular: PDFFont,
    private readonly bold: PDFFont,
  ) { this.newPage(); }

  private newPage(): void {
    this.page = this.doc.addPage([PAGE.width, PAGE.height]);
    this.page.drawRectangle({ x: 0, y: 0, width: PAGE.width, height: PAGE.height, color: C.paper });
    this.pages.push(this.page);
    this.y = PAGE.height - MARGIN;
  }

  private ensure(height: number): void {
    if (this.y - height < MARGIN + 26) this.newPage();
  }

  private line(text: string, options: { size?: number; font?: PDFFont; color?: typeof C.ink; x?: number; gap?: number } = {}): void {
    const size = options.size ?? 11;
    const font = options.font ?? this.regular;
    const gap = options.gap ?? 1.42;
    this.ensure(size * gap);
    this.page.drawText(text, {
      x: options.x ?? MARGIN,
      y: this.y - size,
      size,
      font,
      color: options.color ?? C.ink,
    });
    this.y -= size * gap;
  }

  paragraph(text: string, size = 10.5, color = C.ink, indent = 0): void {
    const lines = wrap(text, this.regular, size, CONTENT_WIDTH - indent);
    const lineHeight = size * 1.48;
    for (const textLine of lines) {
      this.ensure(lineHeight);
      this.page.drawText(textLine, { x: MARGIN + indent, y: this.y - size, size, font: this.regular, color });
      this.y -= lineHeight;
    }
    this.y -= 5;
  }

  heading(text: string, level: 1 | 2 = 1): void {
    this.y -= level === 1 ? 8 : 4;
    const size = level === 1 ? 18 : 13;
    const height = size * 1.55 + (level === 1 ? 8 : 3);
    this.ensure(height);
    this.line(text, { size, font: this.bold, color: level === 1 ? C.accent : C.ink, gap: 1.3 });
    if (level === 1) {
      this.page.drawLine({ start: { x: MARGIN, y: this.y }, end: { x: PAGE.width - MARGIN, y: this.y }, thickness: 0.7, color: C.border });
      this.y -= 10;
    }
  }

  bullet(text: string): void {
    const lines = wrap(text, this.regular, 10.25, CONTENT_WIDTH - 24);
    const lineHeight = 15;
    this.ensure(lines.length * lineHeight + 2);
    this.page.drawCircle({ x: MARGIN + 4, y: this.y - 7, size: 2, color: C.accent });
    for (let i = 0; i < lines.length; i++) {
      this.page.drawText(lines[i], { x: MARGIN + 16, y: this.y - 10.25, size: 10.25, font: this.regular, color: C.ink });
      this.y -= lineHeight;
    }
    this.y -= 2;
  }

  callout(title: string, text: string, tone: 'blue' | 'gold' = 'blue'): void {
    const inner = CONTENT_WIDTH - 30;
    const lines = wrap(text, this.regular, 10, inner);
    const height = 22 + lines.length * 14.5 + 14;
    this.ensure(height + 8);
    const bottom = this.y - height;
    this.page.drawRectangle({
      x: MARGIN, y: bottom, width: CONTENT_WIDTH, height,
      color: tone === 'gold' ? C.paleGold : C.paleBlue,
      borderColor: tone === 'gold' ? C.gold : C.border,
      borderWidth: 0.65,
    });
    this.page.drawRectangle({ x: MARGIN, y: bottom, width: 4, height, color: tone === 'gold' ? C.gold : C.accent });
    this.page.drawText(title, { x: MARGIN + 14, y: this.y - 17, size: 10, font: this.bold, color: tone === 'gold' ? C.gold : C.accent });
    let textY = this.y - 35;
    for (const line of lines) {
      this.page.drawText(line, { x: MARGIN + 14, y: textY, size: 10, font: this.regular, color: C.ink });
      textY -= 14.5;
    }
    this.y = bottom - 13;
  }

  table(headers: string[], rows: string[][], widths: number[]): void {
    const headerH = 25;
    const padX = 7;
    const fontSize = 8.5;
    const rowLineH = 11.5;
    this.ensure(headerH + rows.length * 40 + 10);
    let top = this.y;
    this.page.drawRectangle({ x: MARGIN, y: top - headerH, width: CONTENT_WIDTH, height: headerH, color: C.ink });
    let x = MARGIN;
    headers.forEach((header, i) => {
      this.page.drawText(header, { x: x + padX, y: top - 16, size: 8.5, font: this.bold, color: C.white });
      x += widths[i];
    });
    top -= headerH;
    rows.forEach((row, index) => {
      const cells = row.map((cell, i) => wrap(cell, this.regular, fontSize, widths[i] - padX * 2));
      const maxLines = Math.max(...cells.map(c => c.length));
      const rowH = Math.max(26, maxLines * rowLineH + 12);
      this.ensure(rowH + 5);
      if (this.y - rowH < MARGIN + 26) { this.newPage(); top = this.y; }
      this.page.drawRectangle({ x: MARGIN, y: top - rowH, width: CONTENT_WIDTH, height: rowH, color: index % 2 === 0 ? C.body : C.paper, borderColor: C.border, borderWidth: 0.35 });
      x = MARGIN;
      cells.forEach((cellLines, i) => {
        cellLines.forEach((txt, j) => this.page.drawText(txt, { x: x + padX, y: top - 13 - j * rowLineH, size: fontSize, font: this.regular, color: C.ink }));
        x += widths[i];
      });
      top -= rowH;
      this.y = top;
    });
    this.y -= 10;
  }

  cover(): void {
    this.page.drawRectangle({ x: 0, y: 0, width: PAGE.width, height: PAGE.height, color: C.body });
    this.page.drawRectangle({ x: MARGIN, y: 90, width: CONTENT_WIDTH, height: PAGE.height - 180, color: C.paper, borderColor: C.border, borderWidth: 1 });
    this.page.drawRectangle({ x: MARGIN, y: PAGE.height - 270, width: CONTENT_WIDTH, height: 5, color: C.accent });
    const title = 'NEUROMANCER';
    const titleSize = 30;
    const titleWidth = this.bold.widthOfTextAtSize(title, titleSize);
    this.page.drawText(title, { x: (PAGE.width - titleWidth) / 2, y: PAGE.height - 345, size: titleSize, font: this.bold, color: C.ink });
    const sub = 'ENGLISH READING COMPANION';
    const subSize = 13;
    this.page.drawText(sub, { x: (PAGE.width - this.bold.widthOfTextAtSize(sub, subSize)) / 2, y: PAGE.height - 380, size: subSize, font: this.bold, color: C.accent });
    const desc = [
      'An original C1/C2 skills workbook for close reading,',
      'literary analysis, vocabulary, and exam-aware practice.',
    ];
    desc.forEach((line, i) => {
      const size = 11;
      this.page.drawText(line, { x: (PAGE.width - this.regular.widthOfTextAtSize(line, size)) / 2, y: PAGE.height - 430 - i * 18, size, font: this.regular, color: C.secondary });
    });
    const note = 'STUDY COMPANION — NOT THE NOVEL OR A TRANSLATION';
    this.page.drawText(note, { x: (PAGE.width - this.bold.widthOfTextAtSize(note, 8.5)) / 2, y: 150, size: 8.5, font: this.bold, color: C.gold });
    this.y = 0;
  }

  finalize(): void {
    this.pages.forEach((page, index) => {
      if (index === 0) return;
      page.drawLine({ start: { x: MARGIN, y: PAGE.height - 33 }, end: { x: PAGE.width - MARGIN, y: PAGE.height - 33 }, thickness: 0.5, color: C.border });
      page.drawText('NEUROMANCER · ENGLISH READING COMPANION', { x: MARGIN, y: PAGE.height - 25, size: 7.5, font: this.regular, color: C.secondary });
      page.drawLine({ start: { x: MARGIN, y: 35 }, end: { x: PAGE.width - MARGIN, y: 35 }, thickness: 0.5, color: C.border });
      const pageLabel = `${index + 1} / ${this.pages.length}`;
      page.drawText(pageLabel, { x: PAGE.width - MARGIN - this.regular.widthOfTextAtSize(pageLabel, 8), y: 22, size: 8, font: this.regular, color: C.secondary });
    });
  }
}

async function build(): Promise<void> {
  const doc = await PDFDocument.create();
  doc.registerFontkit(fontkit);
  const fontBytes = await readFile(fontPath());
  const regular = await doc.embedFont(fontBytes, { subset: true });
  const bold = await doc.embedFont(StandardFonts.HelveticaBold);
  doc.setTitle('Neuromancer — English Reading Companion');
  doc.setAuthor('Original study material');
  doc.setSubject('C1/C2 English reading strategies and exam-aware practice; not the novel or a translation.');
  doc.setKeywords(['English reading', 'C1', 'C2', 'literary analysis', 'study companion']);

  const w = new GuideWriter(doc, regular, bold);
  w.cover();

  w.heading('How to use this companion');
  w.paragraph('This is an original skills workbook inspired by the themes and reading challenges associated with science fiction. It does not reproduce, continue, or translate William Gibson’s novel. Use it alongside a lawfully obtained copy of the book, your own notes, and official test-preparation materials.');
  w.callout('A realistic promise', 'Literary reading can build vocabulary, inference, and stylistic awareness. It cannot by itself predict or guarantee any examination score; each test also assesses productive skills, listening, timing, and test-specific task formats.', 'gold');
  w.heading('A repeatable close-reading routine', 2);
  [
    'Before reading: preview the section title and write one question you expect the scene or argument to raise.',
    'During reading: mark unfamiliar words only when they affect meaning; infer first, then verify. Label evidence, inference, and uncertainty separately.',
    'After reading: write a 60-word précis, identify one rhetorical choice, and explain how it changes tone or point of view.',
    'Review after 24 hours: retrieve five terms from memory and revise one claim using precise evidence from your own copy.',
  ].forEach(x => w.bullet(x));
  w.heading('A practical 8-week pathway');
  w.table(['Weeks', 'Main skill', 'Evidence of progress'], [
    ['1–2', 'Contextual vocabulary and inference', 'Explain 10 unfamiliar words from context before checking a dictionary.'],
    ['3–4', 'Syntax, cohesion, and point of view', 'Annotate clause relationships and track a shift in perspective.'],
    ['5–6', 'Rhetorical analysis and concise summary', 'Write a 150-word analysis with a clear claim and support.'],
    ['7–8', 'Timed transfer to exam tasks', 'Complete official practice tasks; log errors and repeat weak skills.'],
  ], [62, 178, 247]);

  w.heading('What the score targets mean — and do not mean');
  w.paragraph('Targets below are planning goals supplied for this project, not a claim that one literary workbook is sufficient preparation. Requirements vary by institution, test version, skill profile, and date; confirm the current official requirement before booking an exam.');
  w.table(['Assessment', 'Requested target', 'Study implication'], [
    ['IELTS Academic', 'Band 7.0', 'Practise all four skills and task-specific criteria; reading alone is not a score predictor.'],
    ['TOEFL iBT', '90 old scale / 5 new scale', 'Important correction: ETS maps an old-scale requirement of 90 to 4.5. Its recommended new-scale target for old 90 is 4.5; 5.0 aligns with 95+ on the historical scale.'],
    ['PTE Academic', '65', 'Use Pearson’s current official score guide and timed speaking/writing practice.'],
    ['Cambridge English', '185', 'C1 Advanced/C2 Proficiency use distinct exam profiles; use the official scale and score report.'],
    ['Duolingo English Test', '120', 'Practise the live task types and review the institution’s accepted test and minimum score.'],
  ], [92, 105, 290]);
  w.callout('TOEFL date note', 'Since 21 January 2026, TOEFL iBT reports a 1–6 scale in half-point increments. ETS’s published guidance maps the former 90 requirement to 4.5, not 5.0. A 5.0 target is associated with 95+ on the former scale. Always follow the exact wording used by your institution.', 'gold');

  w.heading('C1/C2 reading toolkit');
  w.heading('Infer meaning without over-translating', 2);
  w.paragraph('For an unfamiliar item, identify its grammatical role, identify nearby contrasts or cause-and-effect signals, and substitute a tentative meaning. Continue reading to test that hypothesis. Record a translation only if it helps you distinguish meaning or register; a word-for-word gloss can hide ambiguity and tone.');
  w.heading('Read syntax as an argument', 2);
  w.paragraph('In a long sentence, locate the finite verb first. Bracket subordinate clauses, participial phrases, and parenthetical material; then ask which information is foregrounded and what the sentence delays. Do not label a structure “advanced” just because it is long: explain its effect.');
  w.heading('Separate observation from interpretation', 2);
  w.paragraph('A strong analytical note follows a simple chain: observable feature → plausible effect → interpretation → qualification. Use calibrated language (“suggests,” “may imply,” “is consistent with”) when the evidence supports more than one reading.');
  w.table(['Term', 'Working definition', 'Original example'], [
    ['agency', 'Capacity to act and make consequential choices.', 'The witness regained agency by refusing the default setting.'],
    ['opaque', 'Difficult to understand or inspect; not transparent.', 'An opaque ranking system concealed how it weighted each signal.'],
    ['recursive', 'Repeatedly applied to its own output or process.', 'The analyst used a recursive review: each revision generated the next question.'],
    ['contingent', 'Dependent on a condition; not inevitable.', 'The forecast was contingent on the network remaining stable.'],
    ['salient', 'Especially noticeable or relevant to a purpose.', 'For the speaker, the salient detail was the silence after the alarm.'],
  ], [72, 176, 239]);

  w.heading('Original practice passage');
  w.callout('READ THIS ORIGINAL EXAMPLE', 'At 02:13, the city’s maintenance network marked a quiet block as unusually active. No person had entered the square; a row of rain-dark sensors had simply begun reporting the same temperature. Mira checked the raw readings before accepting the dashboard’s confident alert. The anomaly was not proof of intrusion, she noted, but it was enough to justify a second, independent measurement.', 'blue');
  w.heading('Inference and language tasks', 2);
  [
    'Inference: Why does Mira inspect the raw readings before trusting the alert? Give two plausible reasons and distinguish them from facts stated directly.',
    'Vocabulary in context: What does “anomaly” mean here? Which nearby details support your interpretation?',
    'Rhetoric: Explain the effect of the contrast between “confident alert” and “not proof”.',
    'Grammar: Identify the main clause in the final sentence. What does the concessive phrase “but it was enough…” accomplish?',
    'Summary: Restate the event in no more than 25 words without adding a cause the passage does not establish.',
  ].forEach(x => w.bullet(x));
  w.heading('Answer notes');
  w.paragraph('Possible answers: Mira checks primary data because an automated alert may be overconfident or based on duplicated sensor output; the passage does not establish which explanation is correct. “Anomaly” means an irregularity, supported by “unusually active” and identical readings. The contrast distinguishes suspicion from proof while still justifying a proportionate check. Main clause: “it was enough”; the contrastive clause presents a cautious action despite uncertainty. A good summary preserves the uncertainty and avoids claiming that an intruder existed.');

  w.heading('Transfer practice for the five exams');
  w.table(['Skill', 'Short drill', 'Self-check'], [
    ['Reading', 'Write a one-sentence main claim, then one inference and the clue supporting it.', 'Did I separate what is stated from what I infer?'],
    ['Listening', 'Listen once to a short lecture; note claim, contrast, and one example.', 'Can I reconstruct the argument without transcribing?'],
    ['Writing', 'Write a 150-word response to an interpretive question with one counterpoint.', 'Is each paragraph doing one clear job?'],
    ['Speaking', 'Give a 60-second interpretation, then support it with two details.', 'Did I answer directly and manage time?'],
  ], [72, 235, 180]);
  w.paragraph('Use current official practice material for the exact format, scoring rubric, and timing. A novel is a source of rich language, not a substitute for the test itself.');
  w.heading('Weekly review checklist');
  [
    'I can explain why a particular inference is plausible and name the evidence that supports it.',
    'I can distinguish denotation, connotation, register, and a character’s point of view.',
    'I can summarize a passage accurately without importing assumptions.',
    'I can explain how syntax, repetition, contrast, or narrative distance shapes an effect.',
    'I completed at least one timed, official-format task and turned errors into a review plan.',
  ].forEach(x => w.bullet(`□  ${x}`));
  w.callout('Next step', 'Keep a dated error log with three fields: task / why my answer missed / what I will do differently next time. Revisit the same skill after a week and measure the change.', 'blue');

  w.heading('Sources and editorial note');
  w.paragraph('Astryx design reference: Meta Astryx design system, CLI documentation for semantic color and spacing tokens, https://github.com/meta/astryx (queried 8 November 2026). Astryx provides UI components and design tokens; it is not a PDF-generation library. This document uses its neutral-theme token vocabulary for visual decisions and pdf-lib for PDF output.');
  w.paragraph('TOEFL score note: ETS, “TOEFL iBT Score Scale Update: A Guide for Institutions,” https://www.ets.org/toefl/institutions/ibt/score-scale-update.html. ETS’s table maps a legacy 90 requirement to 4.5 on the 1–6 scale; verify current official guidance and institutional requirements.');
  w.paragraph('All explanatory prose, practice questions, example passage, and example sentences in this companion are original. No passages from Neuromancer are reproduced. This companion is unofficial and is not affiliated with or endorsed by the author, publisher, ETS, IELTS, Pearson, Cambridge English, Duolingo, or Meta.');

  w.finalize();
  await mkdir(path.dirname(OUTPUT), { recursive: true });
  await writeFile(OUTPUT, await doc.save());
  console.log(`Created ${path.relative(ROOT, OUTPUT)} (${w.pages.length} pages)`);
}

build().catch(error => { console.error(error); process.exitCode = 1; });
