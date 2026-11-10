import { tokens } from "./tokens.js";

const { print: P, astryx: A } = tokens;

/**
 * The A4 print stylesheet. Visual language: Astryx `theme-gothic`
 * (deep blue-grays, ice ink, editor-syntax accents) set for paper:
 * dark full-bleed panels for covers and part dividers, a warm paper
 * reading surface for the study apparatus.
 */
export function printCss(fontCss: string): string {
  return `
${fontCss}

:root {
  --paper: ${P.paper};
  --paper-warm: ${P.paperWarm};
  --ink: ${P.ink};
  --ink-soft: ${P.inkSoft};
  --ink-faint: ${P.inkFaint};
  --rule: ${P.rule};
  --panel-dark: ${P.panelDark};
  --panel-dark-text: ${P.panelDarkText};
  --panel-muted: ${P.panelMuted};
  --gold: ${P.gold};
  --cyan: ${P.cyan};
  --violet: ${P.violet};
  --blue: ${P.blue};
  --red: ${P.red};
  --green: ${P.green};
  --serif: "Source Serif 4", "Noto Serif", Georgia, serif;
  --display: "Playfair Display", "Source Serif 4", Georgia, serif;
  --ui: "Inter", "Fustat", system-ui, sans-serif;
  --vi: "Fustat", "Inter", "Source Serif 4", sans-serif;
  --mono: "JetBrains Mono", ui-monospace, monospace;
  --black-letter: "UnifrakturMaguntia", serif;
  --gothic-display: "Manufacturing Consent", "Playfair Display", serif;
}

@page { size: A4; margin: 17mm 15mm 19mm 15mm; }

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  background: var(--paper);
  color: var(--ink);
  font-family: var(--serif);
  font-size: 10.2pt;
  line-height: 1.52;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
  text-rendering: optimizeLegibility;
  font-variant-ligatures: common-ligatures;
}

p { margin: 0 0 0.55em 0; text-align: justify; hyphens: auto; }
strong { font-weight: 700; }
em { font-style: italic; }
a { color: inherit; text-decoration: none; }

h1, h2, h3, h4 { font-family: var(--display); color: var(--ink); margin: 0; }
h1 { font-size: 19pt; line-height: 1.18; font-weight: 700; }
h2 { font-size: 14.5pt; line-height: 1.22; font-weight: 700; }
h3 { font-size: 11.5pt; line-height: 1.3; font-weight: 700; }
h4 { font-size: 10pt; font-family: var(--ui); font-weight: 700; letter-spacing: 0.02em; }

.kicker {
  font-family: var(--ui);
  font-size: 7.4pt;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink-faint);
}
.kicker .accent { color: var(--blue); }

.page-break { break-before: page; }
.avoid { break-inside: avoid; }

/* ---------- Cover ---------- */
.cover {
  break-after: page;
  height: 264mm;
  margin: -17mm -15mm -19mm -15mm;
  padding: 22mm 18mm 16mm 18mm;
  background:
    radial-gradient(1200mm 400mm at 85% -10%, ${A.syntaxKeyword}22 0%, transparent 55%),
    radial-gradient(900mm 380mm at -10% 110%, ${A.syntaxFunction}22 0%, transparent 50%),
    var(--panel-dark);
  color: var(--panel-dark-text);
  display: flex;
  flex-direction: column;
  position: relative;
}
.cover .monogram {
  font-family: var(--black-letter);
  font-size: 30pt;
  color: var(--gold);
  line-height: 1;
}
.cover .rule-gold {
  height: 2px; width: 46mm;
  background: linear-gradient(90deg, var(--gold), transparent);
  margin: 7mm 0;
}
.cover .display {
  font-family: var(--gothic-display);
  font-size: 41pt;
  line-height: 1.02;
  letter-spacing: 0.01em;
  color: var(--panel-dark-text);
}
.cover .display .ghost { color: ${A.textSecondary}; }
.cover .vi-title {
  font-family: var(--display);
  font-size: 17pt;
  font-weight: 600;
  color: var(--cyan);
  margin-top: 6mm;
  line-height: 1.35;
}
.cover .subtitle {
  font-family: var(--ui);
  font-size: 10.5pt;
  line-height: 1.6;
  color: ${A.textSecondary};
  margin-top: 7mm;
  max-width: 150mm;
}
.cover .spacer { flex: 1; }
.cover .benchmark-strip {
  display: flex;
  gap: 3mm;
  flex-wrap: wrap;
  border-top: 1px solid ${A.border};
  padding-top: 5mm;
}
.cover .badge {
  border: 1px solid ${A.border};
  border-radius: 2mm;
  padding: 2mm 3.2mm;
  font-family: var(--mono);
  font-size: 7.2pt;
  color: var(--panel-dark-text);
  background: #ffffff08;
}
.cover .badge b { color: var(--gold); font-weight: 700; }
.cover .edition-line {
  font-family: var(--ui);
  font-size: 8pt;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-faint);
  margin-top: 6mm;
}
.cover .corner {
  position: absolute; top: 14mm; right: 16mm;
  font-family: var(--mono); font-size: 7.5pt; color: ${A.textSecondary};
  text-align: right; line-height: 1.7;
}

/* ---------- Generic panels & chips ---------- */
.panel {
  background: var(--panel-muted);
  border-left: 2.2mm solid var(--blue);
  padding: 3.2mm 4mm;
  margin: 3mm 0;
  break-inside: avoid;
}
.panel.vi { border-left-color: var(--cyan); }
.panel.warn { border-left-color: var(--gold); background: ${P.gold}14; }
.panel.practice { border-left-color: var(--violet); background: ${P.violet}12; }
.panel.prompt { border-left-color: var(--cyan); background: ${P.cyan}14; }
.panel.dark {
  background: var(--panel-dark);
  color: var(--panel-dark-text);
  border-left-color: var(--gold);
}
.panel h4 { margin-bottom: 1.2mm; }
.panel p:last-child { margin-bottom: 0; }

.chips { display: flex; flex-wrap: wrap; gap: 1.6mm; margin: 2mm 0 3mm 0; }
.chip {
  font-family: var(--ui);
  font-size: 7.3pt;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 0.9mm 2.2mm;
  border-radius: 5mm;
  background: var(--panel-muted);
  color: var(--ink-soft);
  border: 0.3mm solid var(--rule);
}
.chip.theme { background: ${P.blue}18; color: #2c3e66; border-color: ${P.blue}55; }
.chip.cefr-C2 { background: ${P.violet}22; color: #5b3a75; border-color: ${P.violet}66; }
.chip.cefr-C1 { background: ${P.blue}1c; color: #2c3e66; border-color: ${P.blue}55; }
.chip.cefr-B2 { background: ${P.green}22; color: #3d5a2c; border-color: ${P.green}66; }
.chip.exam { background: ${P.gold}26; color: #6d5312; border-color: ${P.gold}77; }
.chip.mono { font-family: var(--mono); text-transform: none; letter-spacing: 0; }

/* ---------- Section openers ---------- */
.opener {
  break-after: page;
  min-height: 246mm;
  margin: -17mm -15mm -19mm -15mm;
  padding: 30mm 18mm 18mm 18mm;
  background:
    radial-gradient(1000mm 320mm at 110% -20%, ${A.syntaxFunction}1f 0%, transparent 55%),
    var(--panel-dark);
  color: var(--panel-dark-text);
  display: flex; flex-direction: column; justify-content: flex-end;
}
.opener .roman {
  font-family: var(--gothic-display);
  font-size: 64pt; line-height: 0.9;
  color: var(--gold);
  margin-bottom: 8mm;
}
.opener h1 { color: var(--panel-dark-text); font-size: 25pt; max-width: 160mm; }
.opener .vi-sub { font-family: var(--display); color: var(--cyan); font-size: 13pt; margin-top: 3mm; }
.opener .argument {
  margin-top: 8mm; max-width: 150mm;
  color: ${A.textSecondary}; font-family: var(--ui); font-size: 9.6pt; line-height: 1.7;
}
.opener .argument .vi { color: ${A.textSecondary}; margin-top: 2.2mm; }

/* ---------- Contents ---------- */
.toc-part { margin: 4mm 0; break-inside: avoid; }
.toc-part h3 { border-bottom: 0.4mm solid var(--rule); padding-bottom: 1.4mm; margin-bottom: 1.8mm; }
.toc-row { display: flex; align-items: baseline; gap: 2mm; font-size: 9.3pt; margin: 0.9mm 0; }
.toc-row .num { font-family: var(--mono); font-size: 7.8pt; color: var(--ink-faint); width: 12mm; }
.toc-row .t { flex: 1; }
.toc-row .t .vi { color: var(--ink-faint); font-family: var(--vi); font-size: 8.4pt; }
.toc-row .dots { flex: 0 0 auto; color: var(--ink-faint); }
.toc-row .pg { font-family: var(--mono); font-size: 8pt; color: var(--ink-soft); min-width: 8mm; text-align: right; }

/* ---------- Chapter unit ---------- */
.unit { break-before: page; }
.unit-head { border-bottom: 0.6mm solid var(--ink); padding-bottom: 2.6mm; margin-bottom: 3.6mm; }
.unit-head .row { display: flex; align-items: baseline; gap: 4mm; }
.unit-head .chipnum {
  font-family: var(--mono); font-size: 8.5pt; font-weight: 700;
  background: var(--ink); color: var(--paper);
  padding: 1mm 2.6mm; border-radius: 1.2mm;
}
.unit-head h2 { margin-top: 1.8mm; }
.unit-head .vi-title { font-family: var(--display); color: var(--ink-soft); font-size: 11pt; margin-top: 1mm; }
.unit-head .exam-lens { margin-top: 2mm; font-family: var(--mono); font-size: 7.6pt; color: var(--ink-faint); }

.synopsis-en { font-size: 10.4pt; }
.synopsis-en p:first-of-type::first-letter {
  font-family: var(--display); font-size: 25pt; float: left; line-height: 0.82;
  padding: 0.8mm 1.6mm 0 0; color: var(--ink);
}
.synopsis-vi {
  font-family: var(--vi);
  border-left: 1.6mm solid var(--cyan);
  background: ${P.cyan}10;
  padding: 2.8mm 3.6mm; margin: 2.8mm 0 3.4mm 0;
}
.synopsis-vi p { text-align: left; hyphens: none; }
.synopsis-vi .lbl { font-family: var(--ui); font-size: 7.2pt; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink-faint); margin-bottom: 1.2mm; }

.craft-note { border-left: 1.6mm solid var(--gold); background: ${P.gold}12; padding: 2.8mm 3.6mm; margin: 3mm 0; break-inside: avoid; }
.craft-note .lbl { font-family: var(--ui); font-size: 7.2pt; letter-spacing: 0.14em; text-transform: uppercase; color: #6d5312; margin-bottom: 1.2mm; }
.craft-note .vi { color: var(--ink-soft); font-family: var(--vi); margin-top: 1.2mm; font-size: 9.2pt; }

table.vocab { width: 100%; border-collapse: collapse; margin: 2.6mm 0 3.2mm 0; font-size: 8.8pt; }
table.vocab th {
  font-family: var(--ui); font-size: 7pt; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--ink-faint); text-align: left; border-bottom: 0.5mm solid var(--ink); padding: 1.2mm 1.6mm;
}
table.vocab td { border-bottom: 0.25mm solid var(--rule); padding: 1.5mm 1.6mm; vertical-align: top; break-inside: avoid; }
table.vocab td.term { font-weight: 700; width: 30mm; }
table.vocab td.term .ipa { display: block; font-family: var(--mono); font-size: 7.4pt; color: var(--ink-faint); font-weight: 400; }
table.vocab td.vi { font-family: var(--vi); width: 52mm; color: var(--ink-soft); }
table.vocab td.def { width: auto; }

.grammar-xref { display: flex; gap: 3mm; margin: 2.6mm 0; }
.grammar-xref .gx {
  flex: 1; border: 0.35mm solid var(--rule); border-radius: 1.6mm; padding: 2.2mm 2.8mm; break-inside: avoid;
}
.grammar-xref .gx .lbl { font-family: var(--ui); font-size: 6.8pt; letter-spacing: 0.13em; text-transform: uppercase; color: var(--violet); }
.grammar-xref .gx .t { font-family: var(--display); font-weight: 600; font-size: 9.6pt; margin-top: 0.8mm; }
.grammar-xref .gx .s { font-size: 8.4pt; color: var(--ink-soft); margin-top: 0.6mm; }

/* ---------- Practice ---------- */
.practice h4 .tag {
  font-family: var(--mono); font-size: 7pt; color: var(--violet);
  border: 0.3mm solid var(--violet); border-radius: 1mm; padding: 0.3mm 1.6mm; margin-right: 2mm;
}
.practice .stem { font-weight: 600; margin-bottom: 1.6mm; }
.practice .stem .vi { display: block; font-family: var(--vi); font-weight: 400; color: var(--ink-soft); font-size: 8.8pt; margin-top: 0.7mm; }
.practice ol { margin: 0 0 0 5mm; padding: 0; }
.practice ol li { margin: 0.7mm 0; }
.practice .answer-note {
  margin-top: 1.8mm; font-size: 8.4pt; color: var(--ink-faint);
  border-top: 0.25mm dashed var(--rule); padding-top: 1.4mm;
}

/* ---------- Glossary ---------- */
.glossary-cols { column-count: 2; column-gap: 7mm; }
.gloss-entry { break-inside: avoid; margin: 0 0 2.6mm 0; }
.gloss-entry .head { display: flex; align-items: baseline; gap: 1.8mm; flex-wrap: wrap; }
.gloss-entry .term { font-family: var(--display); font-weight: 700; font-size: 10.2pt; }
.gloss-entry .ipa { font-family: var(--mono); font-size: 7.6pt; color: var(--ink-faint); }
.gloss-entry .pos { font-style: italic; font-size: 8.2pt; color: var(--ink-soft); }
.gloss-entry .def { font-size: 8.9pt; margin-top: 0.5mm; }
.gloss-entry .vi { font-family: var(--vi); font-size: 8.5pt; color: var(--ink-soft); }
.gloss-entry .coll { font-family: var(--mono); font-size: 7.3pt; color: var(--ink-faint); }
.gloss-entry .ex { font-size: 8.4pt; font-style: italic; color: var(--ink-soft); }

.alpha-head {
  break-before: column; font-family: var(--gothic-display); font-size: 22pt; color: var(--ink);
  border-bottom: 0.5mm solid var(--ink); margin: 2mm 0 2.6mm 0; padding-bottom: 1mm;
}

/* ---------- Grammar masterclass ---------- */
.g-unit { break-before: page; }
.g-unit .what { border-left: 1.6mm solid var(--violet); background: ${P.violet}10; padding: 3mm 4mm; margin: 3mm 0; }
.g-unit .what .vi { font-family: var(--vi); color: var(--ink-soft); margin-top: 1.2mm; }
.example-row { display: flex; gap: 3mm; margin: 2.2mm 0; break-inside: avoid; }
.example-row .good {
  flex: 1.2; background: var(--panel-dark); color: var(--panel-dark-text);
  border-radius: 1.6mm; padding: 2.6mm 3.2mm; font-family: var(--serif); font-size: 9.3pt;
}
.example-row .note { flex: 1; font-size: 8.8pt; color: var(--ink-soft); }
.example-row .note .vi { font-family: var(--vi); display: block; margin-top: 0.8mm; }
ul.mech { margin: 2mm 0 2.6mm 5mm; padding: 0; }
ul.mech li { margin: 1mm 0; }
ul.mech li .vi { font-family: var(--vi); color: var(--ink-soft); font-size: 8.8pt; display: block; }

/* ---------- Exams ---------- */
.exam-hero {
  margin: -17mm -15mm 5mm -15mm;
  padding: 12mm 15mm 7mm 15mm;
  background: var(--panel-dark); color: var(--panel-dark-text);
}
.exam-hero .kicker { color: var(--gold); }
.exam-hero h2 { color: var(--panel-dark-text); margin-top: 1.6mm; }
.exam-hero .target { font-family: var(--mono); color: var(--cyan); font-size: 9.5pt; margin-top: 1.6mm; }
.exam-hero .scale-note { color: ${A.textSecondary}; font-family: var(--ui); font-size: 8.8pt; margin-top: 2mm; max-width: 150mm; }

.strategy-grid { display: flex; gap: 3mm; margin: 3mm 0; }
.strategy-grid .card {
  flex: 1; border: 0.35mm solid var(--rule); border-top: 1.2mm solid var(--gold);
  border-radius: 1.6mm; padding: 2.8mm 3.2mm; break-inside: avoid;
}
.strategy-grid .card .t { font-family: var(--display); font-weight: 700; font-size: 9.6pt; }
.strategy-grid .card .b { font-size: 8.6pt; color: var(--ink-soft); margin-top: 1mm; }
.strategy-grid .card .b .vi { font-family: var(--vi); display: block; margin-top: 0.8mm; }

table.map { width: 100%; border-collapse: collapse; font-size: 8.8pt; margin: 2.6mm 0; }
table.map th { font-family: var(--ui); font-size: 7pt; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-faint); text-align: left; border-bottom: 0.5mm solid var(--ink); padding: 1.2mm 1.6mm; }
table.map td { border-bottom: 0.25mm solid var(--rule); padding: 1.5mm 1.6mm; vertical-align: top; break-inside: avoid; }
table.map td.skill { font-weight: 700; width: 34mm; }
table.map td .vi { font-family: var(--vi); color: var(--ink-soft); display: block; margin-top: 0.6mm; font-size: 8.3pt; }

table.data { width: 100%; border-collapse: collapse; font-size: 8.6pt; margin: 2.6mm 0 3.6mm 0; }
table.data th { font-family: var(--ui); font-size: 7pt; letter-spacing: 0.1em; text-transform: uppercase; color: var(--panel-dark-text); background: var(--panel-dark); text-align: left; padding: 1.6mm 1.8mm; }
table.data td { border-bottom: 0.25mm solid var(--rule); padding: 1.6mm 1.8mm; vertical-align: top; break-inside: avoid; }
table.data tr:nth-child(even) td { background: #ffffff00; }
table.data td .vi { font-family: var(--vi); color: var(--ink-soft); display: block; margin-top: 0.5mm; font-size: 8.1pt; }
table.data td b.mono { font-family: var(--mono); font-weight: 700; }

/* ---------- Plans / rubric ---------- */
.plan-week { break-inside: avoid; border: 0.35mm solid var(--rule); border-radius: 1.8mm; padding: 3mm 3.6mm; margin: 2.4mm 0; }
.plan-week .wk { font-family: var(--mono); font-size: 8pt; color: var(--blue); font-weight: 700; }
.plan-week .focus { font-family: var(--display); font-weight: 700; font-size: 10.2pt; margin: 0.8mm 0; }
.plan-week .focus .vi { display: block; font-family: var(--vi); font-weight: 400; font-size: 8.8pt; color: var(--ink-soft); }
.plan-week ul { margin: 1.2mm 0 1.2mm 5mm; padding: 0; font-size: 9pt; }
.plan-week ul li .vi { font-family: var(--vi); color: var(--ink-soft); font-size: 8.3pt; display: block; }
.plan-week .out { font-size: 8.6pt; color: var(--ink-soft); border-top: 0.25mm dashed var(--rule); padding-top: 1.4mm; }
.plan-week .out .vi { font-family: var(--vi); display: block; }

/* ---------- Answer key & bibliography ---------- */
.answer-key { column-count: 2; column-gap: 7mm; font-size: 8.8pt; }
.answer-key .grp { break-inside: avoid; margin-bottom: 2.6mm; }
.answer-key .grp h4 { border-bottom: 0.3mm solid var(--rule); padding-bottom: 1mm; margin-bottom: 1.2mm; }
.answer-key .row { display: flex; gap: 2mm; }
.answer-key .row .id { font-family: var(--mono); font-size: 7.8pt; color: var(--ink-faint); min-width: 16mm; }
.answer-key .row .ex { color: var(--ink-soft); }

.bib { font-size: 9pt; }
.bib .entry { padding-left: 8mm; text-indent: -8mm; margin: 1.8mm 0; break-inside: avoid; }
.bib .entry .id { font-family: var(--mono); font-size: 8pt; color: var(--ink-faint); }
.bib .entry .note { display: block; color: var(--ink-soft); font-size: 8.3pt; margin-top: 0.5mm; text-indent: 0; }

/* ---------- Quote / close reading ---------- */
.pull-quote {
  break-inside: avoid;
  margin: 5mm 0;
  border-top: 0.5mm solid var(--gold);
  border-bottom: 0.5mm solid var(--gold);
  padding: 4mm 2mm;
  text-align: center;
}
.pull-quote .en { font-family: var(--display); font-size: 13.5pt; line-height: 1.5; font-style: italic; }
.pull-quote .vi { font-family: var(--display); font-size: 11pt; color: var(--ink-soft); margin-top: 2.4mm; }
.pull-quote .attr { font-family: var(--ui); font-size: 7.6pt; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink-faint); margin-top: 2.4mm; }

.steps { counter-reset: step; margin: 3mm 0; }
.steps .step { display: flex; gap: 3.4mm; margin: 2.4mm 0; break-inside: avoid; }
.steps .step .n {
  counter-increment: step; flex: 0 0 8mm; height: 8mm; border-radius: 50%;
  background: var(--ink); color: var(--paper); font-family: var(--mono);
  display: flex; align-items: center; justify-content: center; font-size: 8.6pt;
}
.steps .step .n::before { content: counter(step); }
.steps .step .b { flex: 1; }
.steps .step .b .vi { font-family: var(--vi); color: var(--ink-soft); display: block; margin-top: 0.6mm; font-size: 8.8pt; }

.small { font-size: 8.4pt; color: var(--ink-soft); }
.legal-text { font-size: 8.6pt; }
.legal-text p { text-align: left; }
hr.thin { border: none; border-top: 0.25mm solid var(--rule); margin: 4mm 0; }

.cols-2 { column-count: 2; column-gap: 7mm; }
`;
}
