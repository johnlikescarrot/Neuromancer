import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { renderBook, escapeHtml } from '../src/render.js';
import { getBookStats, type Edition } from '../src/types.js';

const book = JSON.parse(await readFile('data/bilingual_novel.json', 'utf8')) as Edition;

test('source inventory and stable counts', () => {
  const stats = getBookStats(book);
  assert.deepEqual([stats.parts, stats.chapters, stats.paragraphs, stats.glossaryTerms], [5, 24, 2598, 25]);
  const ids = book.parts.flatMap((part) => part.chapters).flatMap((chapter) => chapter.paragraphs.map((paragraph) => paragraph.id));
  assert.equal(new Set(ids).size, ids.length);
});

test('HTML escaping prevents markup injection', () => {
  assert.equal(escapeHtml('<script a="b">Tom & \'An\'</script>'), '&lt;script a=&quot;b&quot;&gt;Tom &amp; &#39;An&#39;&lt;/script&gt;');
});

test('renderer creates linked navigation and original study modules', () => {
  const html = renderBook(book, ':root{}', '@page{}');
  assert.equal((html.match(/class="chapter"/g) ?? []).length, 24);
  assert.equal((html.match(/class="sheet module"/g) ?? []).length, 6);
  assert.ok(html.includes('href="#chapter-24"'));
  assert.ok(html.includes('@page{}'));
  assert.ok(!html.includes('Ví dụ nguyên tác:'));
  assert.ok(html.includes('ví dụ học thuật minh họa'));
});

test('renderer does not disguise untranslated English as Vietnamese', () => {
  const stats = getBookStats(book);
  const html = renderBook(book, '', '');
  assert.equal((html.match(/class="pair missing"/g) ?? []).length, stats.untranslatedCandidates);
  assert.ok(html.includes('Phụ lục kiểm tra dữ liệu'));
});
