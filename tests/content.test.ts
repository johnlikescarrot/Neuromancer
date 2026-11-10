/**
 * Content integrity tests.
 *
 * These run against the typed document model, not the PDF, so failures point at
 * the text rather than at the layout.
 */
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { buildDocument, collectToc, lexicon } from "../src/content/index.js";
import { STATS } from "../src/content/stats.js";
import { chapters } from "../src/content/chapters.js";
import type { Block, GlossaryEntry } from "../src/types.js";

const blocks: Block[] = buildDocument();

const LEVELS = new Set(["B2", "C1", "C2", "specialist"]);

test("every chapter 1–24 appears exactly once, in order", () => {
  const nums = blocks.flatMap((b) => (b.t === "chapter" ? [b.guide.num] : []));
  assert.deepEqual(nums, Array.from({ length: 24 }, (_, i) => i + 1));
  assert.equal(STATS.chapters, 24);
});

test("each chapter guide is bilingual and complete", () => {
  for (const c of chapters) {
    assert.ok(c.title.length > 2, `chapter ${c.num} has no title`);
    assert.ok(c.titleVi.length > 2, `chapter ${c.num} has no Vietnamese title`);
    assert.ok(c.synopsisEn.split(/\s+/).length >= 40, `chapter ${c.num} synopsis too short (en)`);
    assert.ok(c.synopsisVi.split(/\s+/).length >= 40, `chapter ${c.num} synopsis too short (vi)`);
    assert.ok(c.watchEn.length >= 2 && c.watchVi.length >= 2, `chapter ${c.num} watch list thin`);
    assert.equal(c.watchEn.length, c.watchVi.length, `chapter ${c.num} watch lists unpaired`);
    assert.ok(c.focus.length >= 1, `chapter ${c.num} has no language focus`);
    for (const f of c.focus) {
      assert.ok(f.en.length > 30 && f.vi.length > 30, `chapter ${c.num} focus not bilingual`);
    }
    assert.ok(c.terms.length >= 3, `chapter ${c.num} has too few lexicon terms`);
  }
});

test("lexicon entries are well formed", () => {
  assert.ok(lexicon.length >= 100, `expected 100+ headwords, found ${lexicon.length}`);
  assert.equal(STATS.headwords, lexicon.length);
  const seen = new Set<string>();
  for (const e of lexicon as GlossaryEntry[]) {
    const where = `headword "${e.term}"`;
    for (const [field, value] of Object.entries({ term: e.term, ipa: e.ipa, pos: e.pos, en: e.en, vi: e.vi })) {
      assert.ok(typeof value === "string" && value.trim().length > 2, `${where}: empty ${field}`);
    }
    assert.match(e.ipa, /^\/.+\/$/, `${where}: IPA must be slash-delimited`);
    assert.ok(LEVELS.has(e.level), `${where}: unexpected CEFR band "${e.level}"`);
    assert.ok(!seen.has(e.term), `${where}: duplicate headword`);
    seen.add(e.term);
  }
});

test("glossary covers the groups the layout labels", () => {
  const groups = new Set(lexicon.map((e) => e.group));
  for (const g of ["cyberspace", "corporate", "street", "body", "ai", "place", "craft", "academic"]) {
    assert.ok(groups.has(g as never), `no headwords in group "${g}"`);
  }
});

test("table of contents resolves every division and chapter", () => {
  const toc = collectToc(blocks);
  const divisions = toc.filter((t) => t.level === 1).length;
  const chapterEntries = toc.filter((t) => t.id.startsWith("chapter-")).length;
  assert.equal(chapterEntries, 24);
  assert.ok(divisions >= 10, `expected 10+ divisions, found ${divisions}`);
  assert.equal(new Set(toc.map((t) => t.id)).size, toc.length, "duplicate TOC ids");
});

test("the exam map covers all five target examinations", () => {
  const tables = blocks.filter((b): b is Extract<Block, { t: "table" }> => b.t === "table");
  const flat = tables.flatMap((t) => t.rows.flat()).join(" ");
  for (const exam of ["IELTS", "TOEFL", "PTE", "Cambridge", "Duolingo"]) {
    assert.ok(flat.includes(exam), `exam map missing ${exam}`);
  }
  for (const band of ["7.0", "90", "65", "185", "120"]) {
    assert.ok(flat.includes(band), `exam map missing band ${band}`);
  }
});

test("no long passage of the novel is reproduced in this edition", () => {
  // Integrity guard for the editorial policy in the colophon: the companion must
  // not contain a verbatim run of the source text. We tokenise the novel and the
  // book, then look for any shared 10-word sequence.
  const sourcePath = path.join(process.cwd(), "data", "extracted_novel.json");
  let novelText = "";
  try {
    const data = JSON.parse(fs.readFileSync(sourcePath, "utf8")) as {
      parts: { chapters: { paragraphs: string[] }[] }[];
    };
    novelText = data.parts.flatMap((p) => p.chapters.flatMap((c) => c.paragraphs)).join(" ");
  } catch {
    return; // source text absent (e.g. a clean checkout without data/) — skip
  }
  assert.ok(novelText.length > 100_000, "source text loaded but suspiciously small");

  const norm = (s: string) => s.toLowerCase().replace(/[^a-z0-9' ]+/g, " ").replace(/\s+/g, " ").trim();
  const grams = (s: string, n: number) => {
    const w = norm(s).split(" ");
    const out = new Set<string>();
    for (let i = 0; i + n <= w.length; i++) out.add(w.slice(i, i + n).join(" "));
    return out;
  };

  const novelGrams = grams(novelText, 10);
  const collect = (value: unknown, into: string[]): void => {
    if (typeof value === "string") into.push(value);
    else if (Array.isArray(value)) value.forEach((v) => collect(v, into));
    else if (value && typeof value === "object") Object.values(value).forEach((v) => collect(v, into));
  };
  const bookStrings: string[] = [];
  collect(blocks, bookStrings);

  for (const s of bookStrings) {
    if (s.split(/\s+/).length < 10) continue;
    const wordCount = norm(s).split(" ").length;
    for (let i = 0; i + 10 <= wordCount; i++) {
      const g = norm(s).split(" ").slice(i, i + 10).join(" ");
      assert.ok(!novelGrams.has(g), `verbatim 10-word sequence found: "${g}"`);
    }
  }
});
