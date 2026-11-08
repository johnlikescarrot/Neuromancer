export interface TargetBenchmarks {
  IELTS: string;
  TOEFL_iBT: string;
  Cambridge: string;
  PTE_Academic: string;
  DET: string;
}

export interface GlossaryEntry {
  term: string;
  ipa: string;
  pos: string;
  level: string;
  definition_en: string;
  definition_vi: string;
  literary_note: string;
}

export interface GrammarFocus {
  rule: string;
  explanation: string;
  example: string;
}

export interface StudyGuide {
  title?: string;
  summary_vi?: string;
  grammar_focus?: GrammarFocus[];
  key_vocabulary?: string[];
}

export interface Paragraph {
  id: string;
  en: string;
  vi: string;
  vocab_highlights?: string[];
}

export interface Chapter {
  chapter_index: number;
  chapter_title_en: string;
  chapter_title_vi: string;
  study_guide?: StudyGuide;
  paragraphs: Paragraph[];
}

export interface Part {
  part_index: number;
  part_title_en: string;
  part_title_vi: string;
  chapters: Chapter[];
}

export interface BilingualNovel {
  title: string;
  author: string;
  target_benchmarks: TargetBenchmarks;
  glossary: Record<string, GlossaryEntry>;
  parts: Part[];
}
