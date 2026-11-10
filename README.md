# Neuromancer — Bilingual Study Edition

> **A reader's companion, glossary and exam workbook for William Gibson's *Neuromancer***
> Built with a TypeScript typesetting pipeline · PDF output at `output/neuromancer_bilingual_edition.pdf`

---

## 1. What this repository produces

A single, print-ready A4 PDF (79 pages) containing an independent study apparatus for
*Neuromancer*:

| Part | Contents |
| :--- | :--- |
| **Front matter** | Preface, the exam map (TOEFL / IELTS / PTE / Cambridge / DET), and a structural orientation to the novel |
| **I · The Novel** | 24 chapter guides, each with a synopsis, "what to watch", a language-focus note and key terms — English left, Vietnamese right, aligned |
| **II · The Apparatus** | Twelve rhetoric and grammar features; a 102-headword CEFR-levelled lexicon with IPA, glosses in both languages and study notes; a six-section exam workbook with answer keys and model answers |
| **III · Reference** | Character map, chronology, Gibson's coinages, further reading, Vietnamese–English index |

### Scope, stated plainly

This edition is **a companion to the novel, not a copy of it**. No chapter, scene or passage of
*Neuromancer* is reproduced; where the analysis has to point at Gibson's wording it quotes a few
words at most, in the manner of a critical study. You need your own copy of the novel.

The repository previously contained a build that rendered the novel's full text alongside a
machine translation. That build has been **replaced**: `output/neuromancer_bilingual_edition.pdf`
is now the study edition, and the earlier output remains available in git history only. The
reasons are legal and editorial — a complete unauthorized translation and reprint of a novel
still in copyright is not something this project will produce or host — and they are recorded on
the book's own colophon page as well as in `tests/content.test.ts`, which fails the build if a
verbatim ten-word sequence from the source text ever appears in the edition.

---

## 2. Language targets

The apparatus is calibrated to the level described by the following bands. These are the floors
the content is written for, not claims about a reader's score:

| Examination | Target | What the edition trains |
| :--- | :--- | :--- |
| **TOEFL iBT** | 90+ (pre-21 Jan 2026 scale) / **5.0** (new scale) | Inference, rhetorical purpose, vocabulary in context |
| **IELTS Academic** | **7.0** | Lexical precision, paraphrase, matching and reference items |
| **PTE Academic** | **65** | Processing speed, collocation, one-sentence summarising |
| **Cambridge English** | **185** (C1 Advanced; C2 Proficiency as stretch) | Use of English: word formation, inversion, absolute constructions, register transfer |
| **Duolingo English Test** | **120** | Read-and-select discrimination, c-test style gap filling |

Every headword carries a CEFR band, and the distribution is deliberately honest — most entries
are B2/C1, a minority are C2.

---

## 3. Architecture

The old pipeline was five Python scripts (extract → translate → render HTML → print with
Playwright). It is replaced by a typed TypeScript toolchain with no browser dependency:

```
src/
├── types.ts               # typed document model (blocks, glossary entries, chapter guides)
├── design/tokens.ts       # print design tokens, projected from the Astryx design system
├── engine/
│   ├── text.ts            # inline markup, measurement, line breaking
│   ├── page.ts            # A4 architecture, mirrored margins, running heads, folios, outline
│   └── render.ts          # block renderers: paired columns, tables, glossary, cover, TOC
├── content/               # the book itself, as data
│   ├── front.ts           # preface, exam map, structural orientation
│   ├── chapters.ts        # 24 chapter guides (English + Vietnamese)
│   ├── parts.ts           # five part essays, assembled with the guides
│   ├── rhetoric.ts        # twelve rhetoric/grammar features
│   ├── lexicon-a.ts       # cyberspace, corporate, street (headwords)
│   ├── lexicon-b.ts       # body, AI, place, craft, academic (headwords)
│   ├── workbook.ts        # six exam sections with keys
│   ├── appendices.ts      # maps, chronology, coinages, further reading, index
│   └── index.ts           # assembly + table of contents
└── cli/build.ts           # two-pass build: measure pagination, then write the PDF
```

**Why two passes.** The table of contents needs page numbers that only exist after pagination.
Pass one lays the book out into a discarded buffer and records where every division and chapter
lands; pass two writes the real file with a filled contents page. Page geometry is identical
between passes because the contents page reads its numbers from a fixed-width gutter.

**Text engine.** PDFKit can flow text, but a bilingual book needs explicit control: paired
columns of unequal length, per-line justification, baseline placement across four font styles,
widow control at column breaks. `engine/text.ts` measures words and breaks lines itself;
`engine/page.ts` places each line.

**Astryx.** `facebook/astryx` (`@astryxdesign/*`) is a React 19 + StyleX design system for web
UIs — it contains no PDF renderer, and there is no browser in the build environment to print
from. The integration is therefore at the level it can honestly be: `src/design/tokens.ts` reads
the neutral theme's `theme.css` at build time, harvests its colour ramp, type scale and spacing
ramp, and projects them onto print values (points, millimetres, printable inks). The book's
palette and scale are the design system's, not an invented parallel.

**Typography.** DejaVu Serif for English prose, DejaVu Sans for Vietnamese companion text and all
metadata, both chosen for complete Vietnamese diacritic coverage. Fonts are embedded
(`tests/pdf.test.ts` fails if a non-embedded standard font leaks in).

---

## 4. Build and test

```bash
npm install

npm run build      # tsc + build the PDF into output/
npm run check      # type-check only
npm test           # 11 tests: content integrity + PDF artefact
```

Requirements: Node 20+ (developed on Node 22). No browser, no network, no external services.

The build prints a one-line report (`pages, MB, TOC entries resolved, seconds`) and exits
non-zero on failure.

### Tests

| Test | Guards |
| :--- | :--- |
| chapters 1–24, in order | structural completeness |
| chapter guides bilingual and complete | both languages, minimum lengths, paired lists |
| lexicon well formed | IPA delimiters, CEFR bands, unique headwords, no empty fields |
| glossary groups match layout labels | no unlabelled section can appear |
| contents resolves | every division and chapter has a page |
| exam map covers five exams and bands | the language claims stay honest |
| **no verbatim 10-word sequence from the novel** | the editorial policy, mechanically enforced |
| A4 geometry, metadata, embedded fonts | the artefact itself |

---

## 5. Editorial notes

- **Vietnamese text** is an original companion translation of the apparatus, written for
  Vietnamese learners reading the novel in English, and set in the sans face so the two
  languages never blur at a glance.
- **Quotations** are limited to short critical phrases; all exercises, model answers, glosses and
  synopses are original to this project.
- **Synopses** summarise rather than retell, and assume the reader has just finished the chapter.
- **Rights.** *Neuromancer* remains in copyright. This is an unofficial study aid, not authorised
  by the author or his publishers, distributed for study and research.

---

## 6. Repository history

| Stage | What changed |
| :--- | :--- |
| v1 | Python pipeline; full novel text with machine translation, rendered to PDF via Playwright |
| **v2 (this)** | TypeScript typesetting engine; the edition becomes an original companion — 24 chapter guides, levelled lexicon, rhetoric compendium, exam workbook, appendices — with no reproduction of the novel's text |

---

*Ấn bản này là sách đồng hành học thuật cho tiểu thuyết, không phải bản in lại hay bản dịch của
tác phẩm. Toàn bộ phần tóm lược, phân tích, từ điển, bài tập và đáp án là nội dung nguyên bản của
dự án; bạn cần một bản *Neuromancer* của riêng mình để đọc cùng.*
