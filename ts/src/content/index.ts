import type { Book, PartUnit } from "../model.js";
import { benchmarks, concordance, howToUse, legal } from "./benchmarks.js";
import {
  characters,
  closeReading,
  concepts,
  context,
  locations,
  translationNotebook,
} from "./context.js";
import { part1 } from "./chapters-part1.js";
import { part2 } from "./chapters-part2.js";
import { part3 } from "./chapters-part3.js";
import { chapters4a } from "./chapters-part4a.js";
import { chapters4b } from "./chapters-part4b.js";
import { part4 as part4Shell, part5 } from "./chapters-part5.js";
import { grammar } from "./grammar.js";
import { glossaryWorld } from "./glossary-a.js";
import { glossaryLiterary } from "./glossary-a.js";
import { glossaryAcademic } from "./glossary-b.js";
import { bibliography, exams, plans, rubric } from "./exams.js";

const part4: PartUnit = { ...part4Shell, chapters: [...chapters4a, ...chapters4b] };

export const book: Book = {
  meta: {
    title: {
      en: "Neuromancer — Bilingual Academic Companion (C1-C2)",
      vi: "Neuromancer — Cẩm nang Học thuật Song ngữ (C1-C2)",
    },
    subtitle: {
      en: "Exam-grade study apparatus for TOEFL · IELTS · PTE · Cambridge · Duolingo",
      vi: "Hệ thống học liệu chuẩn thi cho TOEFL · IELTS · PTE · Cambridge · Duolingo",
    },
    edition: "FINAL",
    date: "2026-11-10",
    toolkit: "TypeScript + Astryx (meta/astryx, theme-gothic tokens) + Puppeteer/Chromium + Fontsource",
  },
  legal,
  benchmarks,
  concordance,
  howToUse,
  context,
  characters,
  locations,
  concepts,
  closeReading,
  translationNotebook,
  parts: [part1, part2, part3, part4, part5],
  grammar,
  glossary: [...glossaryWorld, ...glossaryLiterary, ...glossaryAcademic],
  exams,
  plans,
  rubric,
  bibliography,
};

export const stats = {
  parts: book.parts.length,
  chapters: book.parts.reduce((n, p) => n + p.chapters.length, 0),
  grammarUnits: book.grammar.length,
  glossary: book.glossary.length,
  exams: book.exams.length,
  practiceItems:
    book.parts.reduce((n, p) => n + p.chapters.length, 0) + book.grammar.length + book.exams.reduce((n, e) => n + e.practice.length, 0),
};
