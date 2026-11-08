import assert from 'node:assert/strict';
import { readFile, stat } from 'node:fs/promises';
import { test } from 'node:test';
import { PDFDocument } from 'pdf-lib';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const pdf = path.join(root, 'output/neuromancer_english_study_companion.pdf');

test('study companion is a non-empty, multi-page PDF with clear metadata', async () => {
  const bytes = await readFile(pdf);
  assert.equal(bytes.subarray(0, 4).toString(), '%PDF');
  assert.ok((await stat(pdf)).size > 8_000);
  const document = await PDFDocument.load(bytes);
  assert.ok(document.getPageCount() >= 5, 'expected a substantial guide, not an empty stub');
  assert.match(document.getTitle() ?? '', /English Reading Companion/);
  assert.match(document.getSubject() ?? '', /not the novel or a translation/i);
});
