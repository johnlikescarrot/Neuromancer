/** Terse builders so content modules read like a book and not like JSON. */
import type { Block, ChapterGuide, GlossaryEntry } from "../types.js";

export const h1 = (text: string, id?: string, kicker?: string): Block => ({
  t: "h1",
  text,
  id,
  kicker,
});

export const h2 = (text: string, vi?: string): Block => ({ t: "h2", text, vi });
export const h3 = (text: string): Block => ({ t: "h3", text });

/** Bilingual paragraph pair, English in the left column, Vietnamese at right. */
export const pair = (en: string | string[], vi: string | string[], lead = false): Block => ({
  t: "pair",
  en: Array.isArray(en) ? en : [en],
  vi: Array.isArray(vi) ? vi : [vi],
  lead,
});

export const only = (text: string): Block => ({ t: "pair", en: [text], vi: [] });
export const onlyVi = (text: string): Block => ({ t: "pair", en: [], vi: [text] });

export const bullets = (en: string[], vi: string[]): Block => ({ t: "bullets", en, vi });

export const table = (
  head: string[],
  widths: number[],
  rows: string[][],
  caption?: string,
  zebra = true,
): Block => ({ t: "table", head, widths, rows, caption, zebra });

export const divider = (
  id: string,
  kicker: string,
  title: string,
  subtitle?: string,
  en?: string,
  vi?: string,
): Block => ({ t: "divider", id, kicker, title, subtitle, en, vi });

export const callout = (label: string, en: string[], vi: string[]): Block => ({
  t: "callout",
  label,
  en,
  vi,
});

export const quote = (text: string, cite?: string): Block => ({ t: "quote", text, cite });
export const rule = (): Block => ({ t: "rule" });
export const pagebreak = (): Block => ({ t: "pagebreak" });

export const chapter = (guide: ChapterGuide): Block => ({ t: "chapter", guide });

export const glossaryList = (entries: GlossaryEntry[], showGroup = false): Block => ({
  t: "glossary",
  entries,
  showGroup,
});
