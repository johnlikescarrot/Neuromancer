/** Counts surfaced on the cover and in copy, so the numbers cannot drift. */
import { lexiconA } from "./lexicon-a.js";
import { lexiconB } from "./lexicon-b.js";
import { chapters } from "./chapters.js";

export const STATS = {
  headwords: lexiconA.length + lexiconB.length,
  chapters: chapters.length,
  c2: [...lexiconA, ...lexiconB].filter((e) => e.level === "C2").length,
  c1: [...lexiconA, ...lexiconB].filter((e) => e.level === "C1").length,
};
