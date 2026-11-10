/**
 * PDF-level tests: the book must build, be A4, carry metadata and resolve its
 * contents page. These assertions run on the artefact itself, using pdf-lib.
 */
import { test, before } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { PDFDocument } from "pdf-lib";
import { build } from "../src/cli/build.js";

const out = path.join(os.tmpdir(), "neuromancer-edition-test.pdf");
let result: Awaited<ReturnType<typeof build>>;
let pdf: PDFDocument;

before(async () => {
  result = await build(out);
  pdf = await PDFDocument.load(fs.readFileSync(out));
});

test("the build produces a substantial A4 book", () => {
  assert.ok(result.pages >= 60, `only ${result.pages} pages`);
  assert.ok(result.bytes > 300_000, `only ${result.bytes} bytes`);
  assert.ok(result.tocFilled >= 38, `only ${result.tocFilled} TOC entries resolved`);
});

test("every page is A4 and single-orientation", () => {
  const pages = pdf.getPages();
  assert.equal(pages.length, result.pages);
  for (const page of pages) {
    const { width, height } = page.getSize();
    assert.ok(Math.abs(width - 595.28) < 1, `page width ${width}`);
    assert.ok(Math.abs(height - 841.89) < 1, `page height ${height}`);
  }
});

test("metadata identifies the work and its toolchain", () => {
  assert.match(pdf.getTitle() ?? "", /Neuromancer/);
  assert.match(pdf.getAuthor() ?? "", /Neuromancer/);
  assert.match(pdf.getCreator() ?? "", /TypeScript/i);
  assert.match(pdf.getSubject() ?? "", /companion/i);
});

test("fonts are embedded rather than referenced", () => {
  const raw = fs.readFileSync(out, "latin1");
  // Subset-embedded TrueType fonts appear as FontFile2 objects.
  assert.ok(raw.includes("/FontFile2"), "no embedded font programmes found");
  assert.ok(!raw.includes("/BaseFont /Helvetica"), "a standard, non-embedded font leaked in");
});
