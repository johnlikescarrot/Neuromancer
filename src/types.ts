export interface GrammarFocus {
  rule: string;
  explanation: string;
  example: string;
}

export interface StudyGuide {
  title: string;
  summary_vi: string;
  grammar_focus: GrammarFocus[];
  key_vocabulary: string[];
}

export interface Paragraph {
  id: string;
  en: string;
  vi: string;
  vocab_highlights: string[];
}

export interface Chapter {
  chapter_index: number;
  chapter_title_en: string;
  chapter_title_vi: string;
  study_guide: StudyGuide;
  paragraphs: Paragraph[];
}

export interface BookPart {
  part_index: number;
  part_title_en: string;
  part_title_vi: string;
  chapters: Chapter[];
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

export interface Edition {
  title: string;
  author: string;
  target_benchmarks: Record<string, string>;
  glossary: Record<string, GlossaryEntry>;
  parts: BookPart[];
}

export interface BookStats {
  parts: number;
  chapters: number;
  paragraphs: number;
  untranslatedCandidates: number;
  glossaryTerms: number;
}

export function getBookStats(book: Edition): BookStats {
  const chapters = book.parts.flatMap((part) => part.chapters);
  const paragraphs = chapters.flatMap((chapter) => chapter.paragraphs);
  return {
    parts: book.parts.length,
    chapters: chapters.length,
    paragraphs: paragraphs.length,
    untranslatedCandidates: paragraphs.filter(({ en, vi }) => en.trim() === vi.trim()).length,
    glossaryTerms: Object.keys(book.glossary).length,
  };
}
