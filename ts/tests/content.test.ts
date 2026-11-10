import { describe, expect, it } from "vitest";
import { book, stats } from "../src/content/index.js";
import { renderHtml } from "../src/html/render.js";
import { tokens } from "../src/design/tokens.js";

const ALL_VOCAB_IDS = book.parts.flatMap((p) => p.chapters.flatMap((c) => c.vocab));
const ALL_MCQ = [
  ...book.parts.flatMap((p) => p.chapters.map((c) => c.practice)),
  ...book.grammar.map((g) => g.practice),
  ...book.exams.flatMap((e) => e.practice),
];

describe("content integrity", () => {
  it("covers five parts and exactly 24 chapter units", () => {
    expect(book.parts).toHaveLength(5);
    expect(stats.chapters).toBe(24);
    const nums = book.parts.flatMap((p) => p.chapters.map((c) => c.number));
    expect(nums).toEqual([...Array(24)].map((_, i) => String(i + 1)));
  });

  it("has a grammar masterclass of at least 16 units, each with examples and practice", () => {
    expect(book.grammar.length).toBeGreaterThanOrEqual(16);
    for (const g of book.grammar) {
      expect(g.examples.length).toBeGreaterThanOrEqual(1);
      expect(g.mechanics.length).toBeGreaterThanOrEqual(2);
      expect(g.practice.options).toHaveLength(4);
    }
  });

  it("ships a glossary of at least 200 unique entries", () => {
    const ids = new Set(book.glossary.map((v) => v.id));
    expect(ids.size).toBe(book.glossary.length);
    expect(book.glossary.length).toBeGreaterThanOrEqual(200);
  });

  it("resolves every chapter vocabulary reference to a glossary entry", () => {
    const gloss = new Set(book.glossary.map((v) => v.id));
    const missing = ALL_VOCAB_IDS.filter((id) => !gloss.has(id));
    expect(missing).toEqual([]);
  });

  it("gives every chapter at least 8 vocabulary items and 2 grammar pointers that resolve", () => {
    const gids = new Set(book.grammar.map((g) => g.id));
    for (const p of book.parts) {
      for (const c of p.chapters) {
        expect(c.vocab.length).toBeGreaterThanOrEqual(8);
        expect(c.grammarRefs.length).toBeGreaterThanOrEqual(2);
        for (const ref of c.grammarRefs) expect(gids.has(ref)).toBe(true);
      }
    }
  });

  it("keeps every practice item well-formed with a valid answer index", () => {
    for (const q of ALL_MCQ) {
      expect(q.options).toHaveLength(4);
      expect(q.answer).toBeGreaterThanOrEqual(0);
      expect(q.answer).toBeLessThan(4);
      expect(q.stem.en.length).toBeGreaterThan(10);
      expect(q.stem.vi.length).toBeGreaterThan(10);
      expect(q.explain.en.length).toBeGreaterThan(10);
    }
  });

  it("is bilingual end to end: synopses, prompts and playbooks carry Vietnamese", () => {
    for (const p of book.parts) {
      for (const c of p.chapters) {
        expect(c.synopsis.en.length).toBeGreaterThan(200);
        expect(c.synopsis.vi.length).toBeGreaterThan(200);
        expect(c.writingPrompt.vi.length).toBeGreaterThan(20);
      }
    }
    for (const v of book.glossary) {
      expect(v.glossVi.length).toBeGreaterThan(8);
      expect(v.defEn.length).toBeGreaterThan(20);
      expect(v.collocations.length).toBeGreaterThanOrEqual(2);
      expect(v.example.length).toBeGreaterThan(15);
    }
    for (const e of book.exams) {
      expect(e.scaleNote.vi.length).toBeGreaterThan(30);
      expect(e.strategies.length).toBeGreaterThanOrEqual(3);
      expect(e.practice.length).toBeGreaterThanOrEqual(2);
    }
  });

  it("covers all five commissioned credentials with their exact targets", () => {
    const t = book.benchmarks.map((b) => b.test + " " + b.target).join(" | ");
    expect(t).toContain("90 / 120");
    expect(t).toContain("Band 5.0");
    expect(t).toContain("7.0");
    expect(t).toContain("65");
    expect(t).toContain("185");
    expect(t).toContain("120");
    expect(book.benchmarks).toHaveLength(5);
    expect(book.concordance.length).toBeGreaterThanOrEqual(4);
  });

  it("keeps novel quotations brief (<= 30 words each, one quoted passage total)", () => {
    const quotes = [book.closeReading.quote];
    expect(quotes).toHaveLength(1);
    for (const q of quotes) {
      const words = q.text.trim().split(/\s+/).length;
      expect(words).toBeLessThanOrEqual(30);
    }
  });

  it("carries a copyright notice that states the novel and translations are not reproduced", () => {
    const legal = book.legal
      .map((s) => `${s.title.en} ${s.title.vi} ${s.paragraphs.map((p) => p.en + p.vi).join(" ")}`)
      .join(" ");
    expect(legal).toMatch(/copyright/i);
    expect(legal).toMatch(/full text of the novel is not reproduced/i);
    expect(legal).toMatch(/không kèm bản dịch/i);
    expect(legal).toMatch(/William Gibson/);
  });

  it("covers the novel's parts with accurate structural labels", () => {
    const labels = book.parts.map((p) => p.label);
    expect(labels).toEqual(["Part One", "Part Two", "Part Three", "Part Four", "Coda"]);
  });
});

describe("design tokens come from Astryx theme-gothic", () => {
  it("matches the gothic palette values shipped by @astryxdesign/theme-gothic", () => {
    expect(tokens.astryx.backgroundBody.toLowerCase()).toBe("#101314");
    expect(tokens.astryx.textPrimary.toLowerCase()).toBe("#e8f1f6");
    expect(tokens.astryx.syntaxConstant.toLowerCase()).toBe("#e6b85e");
    expect(tokens.print.gold.toLowerCase()).toBe("#e6b85e");
    expect(tokens.print.violet.toLowerCase()).toBe("#c39adb");
    expect(tokens.print.cyan.toLowerCase()).toBe("#7cc5b3");
  });
});

describe("rendered HTML", () => {
  const html = renderHtml(book, "/* fonts */");

  it("includes every unit, the glossary, the answer key and the legal page", () => {
    for (let i = 1; i <= 24; i++) {
      expect(html).toContain(`UNIT ${String(i).padStart(2, "0")}`);
    }
    expect(html).toContain("Academic Glossary");
    expect(html).toContain("Answer Key");
    expect(html).toContain("Copyright and editorial independence");
    expect(html).toContain("NEUROMANCER");
    expect(html).toContain("GRAMMAR G16");
  });

  it("lists contents rows for parts and units", () => {
    expect(html).toContain("Book Map");
    expect(html).toContain("PART FOUR");
    expect(html).toContain("U24");
  });

  it("embeds the five benchmark badges on the cover", () => {
    expect(html).toContain("TOEFL <b>90 / B5.0</b>");
    expect(html).toContain("IELTS <b>7.0</b>");
    expect(html).toContain("PTE <b>65</b>");
    expect(html).toContain("CAMBRIDGE <b>185</b>");
    expect(html).toContain("DET <b>120</b>");
  });
});
