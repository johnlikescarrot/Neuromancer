/**
 * Document model for the Neuromancer bilingual study edition.
 *
 * The model is deliberately small and print-oriented: a book is an ordered list
 * of typed blocks, and the layout engine in `src/engine` knows how to place each
 * one on an A4 page. Content modules never touch PDFKit directly.
 */

export type Lang = "en" | "vi";

/** Font style axis: regular, italic, bold, bold-italic. */
export type Style = "r" | "i" | "b" | "bi";

export interface Run {
  text: string;
  style: Style;
}

export type LexicalGroup =
  | "cyberspace"
  | "corporate"
  | "street"
  | "body"
  | "ai"
  | "place"
  | "craft"
  | "academic";

/**
 * One glossary headword. `level` is the CEFR / exam band the word is useful for
 * (C1, C2, or a specialist label), so the glossary doubles as a study list.
 */
export interface GlossaryEntry {
  term: string;
  ipa: string;
  pos: string;
  level: string;
  en: string;
  vi: string;
  note?: string;
  group: LexicalGroup;
}

export interface ChapterGuide {
  part: string;
  num: number;
  title: string;
  titleVi: string;
  /** Original editorial synopsis — no quotations from the novel. */
  synopsisEn: string;
  synopsisVi: string;
  watchEn: string[];
  watchVi: string[];
  focus: { label: string; en: string; vi: string; example?: string }[];
  terms: string[];
}

export type Block =
  | { t: "cover" }
  | { t: "titlepage" }
  | { t: "colophon" }
  | { t: "toc" }
  | {
      t: "divider";
      id: string;
      kicker: string;
      title: string;
      subtitle?: string;
      en?: string;
      vi?: string;
    }
  | { t: "h1"; text: string; id?: string; kicker?: string; toc?: boolean }
  | { t: "h2"; text: string; vi?: string }
  | { t: "h3"; text: string }
  | { t: "pair"; en?: string[]; vi?: string[]; lead?: boolean }
  | { t: "bullets"; en?: string[]; vi?: string[] }
  | {
      t: "table";
      head: string[];
      rows: string[][];
      widths: number[];
      caption?: string;
      zebra?: boolean;
    }
  | { t: "glossary"; entries: GlossaryEntry[]; showGroup: boolean }
  | { t: "callout"; label: string; en?: string[]; vi?: string[] }
  | { t: "quote"; text: string; cite?: string }
  | { t: "rule" }
  | { t: "pagebreak" }
  | { t: "chapter"; guide: ChapterGuide };
