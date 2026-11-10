import assert from 'node:assert/strict';
import { readFile, stat } from 'node:fs';
import { promisify } from 'node:util';
import path from 'node:path';
import { PDFDocument, PDFName } from 'pdf-lib';
import { getBookStats, type Edition } from './types.js';

const read = promisify(readFile);
const fileStat = promisify(stat);
const root = process.cwd();

export async function validateEdition(): Promise<void> {
  const source = JSON.parse(await read(path.join(root, 'data/bilingual_novel.json'), 'utf8')) as Edition;
  const extracted = JSON.parse(await read(path.join(root, 'data/extracted_novel.json'), 'utf8')) as Edition;
  const stats = getBookStats(source);
  assert.equal(stats.parts, 5, 'Five parts including the coda');
  assert.equal(stats.chapters, 24, 'Twenty-four chapters');
  assert.equal(stats.paragraphs, 2598, 'All existing paragraph pairs retained');
  assert.equal(stats.glossaryTerms, 25, 'Existing glossary retained');
  assert.ok(stats.untranslatedCandidates > 0, 'Audit should identify incomplete source translations');

  source.parts.forEach((part, partIndex) => part.chapters.forEach((chapter, chapterIndex) => {
    const original = extracted.parts[partIndex]?.chapters[chapterIndex];
    assert.ok(original, 'Chapter should exist in extracted source');
    assert.equal(chapter.paragraphs.length, original.paragraphs.length, 'Paragraph count must match source');
    chapter.paragraphs.forEach((paragraph, paragraphIndex) => {
      assert.ok(paragraph.en.trim() && paragraph.vi.trim(), 'Both language columns must be nonempty');
      assert.equal(paragraph.en, original.paragraphs[paragraphIndex], 'English source must be unchanged');
      assert.match(paragraph.id, /^\d+_\d+_\d+$/, 'Stable paragraph ID required');
    });
  }));

  const html = await read(path.join(root, 'data/novel_bilingual.html'), 'utf8');
  assert.ok(html.includes('data-astryx-theme="gothic"'), 'Astryx theme must be embedded');
  assert.ok(html.includes('@page'), 'Paged print stylesheet required');
  assert.equal((html.match(/class="pair(?: missing)?"/g) ?? []).length, 2598, 'HTML must contain every pair');
  assert.equal((html.match(/TRÙNG VĂN BẢN NGUỒN ·/g) ?? []).length, stats.untranslatedCandidates, 'Every identical pair must be flagged for contextual review');
  assert.ok(html.includes('target-counter'), 'TOC must contain generated page references');

  const bytes = await read(path.join(root, 'output/neuromancer_bilingual_edition.pdf'));
  assert.equal(bytes.subarray(0, 4).toString(), '%PDF');
  const document = await PDFDocument.load(bytes);
  assert.ok(document.getPageCount() >= 300, 'Full book must be present in PDF');
  assert.ok(document.catalog.has(PDFName.of('Outlines')), 'PDF must include navigation bookmarks');
  assert.ok((await fileStat(path.join(root, 'output/neuromancer_bilingual_edition.pdf'))).size > 1_000_000);
  const report = JSON.parse(await read(path.join(root, 'output/build-report.json'), 'utf8')) as Record<string, unknown>;
  assert.equal(report.pages, document.getPageCount());
  assert.equal(report.paragraphs, 2598);
  console.log(`Validated: ${stats.chapters} chapters, ${stats.paragraphs} pairs, ${document.getPageCount()} PDF pages, ${stats.untranslatedCandidates} transparently flagged source gaps.`);
}

await validateEdition();
