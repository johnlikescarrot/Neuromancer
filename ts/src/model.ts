/**
 * Content model for the Neuromancer bilingual academic companion.
 *
 * Every entry in this model is ORIGINAL study-guide prose (English + Vietnamese).
 * Quotations from the novel are brief and carry a `quote` field; a test enforces
 * a hard word budget on them (brief quotation for study and commentary only).
 */

export type Cefr = "B2" | "C1" | "C2";
export type DomainTag = "cyberpunk" | "literary" | "academic" | "colloquial";

export interface Mcq {
  id: string;
  stem: { en: string; vi: string };
  options: string[];
  /** 0-based index of the correct option. */
  answer: number;
  explain: { en: string; vi: string };
}

export interface Quote {
  text: string;
  attribution: string;
  /** Bilingual commentary of our own. */
  note: { en: string; vi: string };
}

export interface BenchmarkRow {
  test: string;
  target: string;
  cefr: string;
  whatItProves: { en: string; vi: string };
  editionUse: { en: string; vi: string };
}

export interface ConcordanceRow {
  cefr: string;
  ielts: string;
  toeflLegacy: string;
  toeflBand: string;
  pte: string;
  det: string;
  cambridge: string;
}

export interface ProseSection {
  id: string;
  title: { en: string; vi: string };
  paragraphs: { en: string; vi: string }[];
  bullets?: { en: string; vi: string }[];
}

export interface GuideEntry {
  id: string;
  name: string;
  kind: string;
  summary: { en: string; vi: string };
  studyValue: { en: string; vi: string };
}

export interface ChapterUnit {
  id: string;
  partId: string;
  number: string;
  title: { en: string; vi: string };
  synopsis: { en: string; vi: string };
  themes: string[];
  craftNote: { en: string; vi: string };
  vocab: string[];
  grammarRefs: string[];
  examLens: string[];
  practice: Mcq;
  writingPrompt: { en: string; vi: string };
}

export interface PartUnit {
  id: string;
  label: string;
  title: { en: string; vi: string };
  argument: { en: string; vi: string };
  chapters: ChapterUnit[];
}

export interface GrammarUnit {
  id: string;
  title: { en: string; vi: string };
  whatItIs: { en: string; vi: string };
  mechanics: { en: string; vi: string }[];
  examples: { good: string; note: { en: string; vi: string } }[];
  practice: Mcq;
  examValue: { en: string; vi: string };
}

export interface GlossaryEntry {
  id: string;
  term: string;
  ipa: string;
  pos: string;
  cefr: Cefr;
  domain: DomainTag;
  defEn: string;
  glossVi: string;
  collocations: string[];
  example: string;
}

export interface ExamPlaybook {
  id: string;
  test: string;
  target: string;
  scaleNote: { en: string; vi: string };
  formatBullets: { en: string; vi: string }[];
  c1Profile: { en: string; vi: string }[];
  trainingMap: { skill: string; use: { en: string; vi: string } }[];
  strategies: { title: { en: string; vi: string }; body: { en: string; vi: string } }[];
  practice: Mcq[];
}

export interface PlanWeek {
  week: string;
  focus: { en: string; vi: string };
  tasks: { en: string; vi: string }[];
  output: { en: string; vi: string };
}

export interface PlanSection {
  id: string;
  title: { en: string; vi: string };
  intro: { en: string; vi: string };
  weeks: PlanWeek[];
}

export interface RubricRow {
  skill: string;
  c1Evidence: { en: string; vi: string };
  selfTest: { en: string; vi: string };
}

export interface BibEntry {
  id: string;
  citation: string;
  note: string;
}

export interface Book {
  meta: {
    title: { en: string; vi: string };
    subtitle: { en: string; vi: string };
    edition: string;
    date: string;
    toolkit: string;
  };
  legal: ProseSection[];
  benchmarks: BenchmarkRow[];
  concordance: ConcordanceRow[];
  howToUse: ProseSection[];
  context: ProseSection[];
  characters: GuideEntry[];
  locations: GuideEntry[];
  concepts: GuideEntry[];
  closeReading: { title: { en: string; vi: string }; quote: Quote; steps: { en: string; vi: string }[] };
  translationNotebook: ProseSection[];
  parts: PartUnit[];
  grammar: GrammarUnit[];
  glossary: GlossaryEntry[];
  exams: ExamPlaybook[];
  plans: PlanSection[];
  rubric: RubricRow[];
  bibliography: BibEntry[];
}
