import { readFile, writeFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
import path from 'node:path';
import chromium from '@sparticuz/chromium';
import { chromium as playwright, type Browser } from 'playwright';
import { PDFDocument, PDFName, PDFString, PDFArray, PDFDict, PDFRef } from 'pdf-lib';
import { getBookStats, type Edition } from './types.js';

const require = createRequire(import.meta.url);
const root = process.cwd();
const htmlPath = path.join(root, 'data/novel_bilingual.html');
const pdfPath = path.join(root, 'output/neuromancer_bilingual_edition.pdf');

async function launchBrowser(): Promise<Browser> {
  const localBrowser = process.env.CHROMIUM_PATH;
  const compatibilityLib = path.join(tmpdir(), 'al2023/lib');
  if (!localBrowser && !existsSync(path.join(compatibilityLib, 'libnspr4.so'))) {
    const chromiumRoot = path.dirname(require.resolve('@sparticuz/chromium/package.json'));
    const { inflate } = require(path.join(chromiumRoot, 'build/cjs/lambdafs.cjs')) as { inflate: (input: string) => Promise<string> };
    await inflate(path.join(chromiumRoot, 'bin/al2023.tar.br'));
  }
  const executablePath = localBrowser || await chromium.executablePath();
  return playwright.launch({
    executablePath,
    headless: true,
    timeout: 0,
    env: { ...process.env, LD_LIBRARY_PATH: process.env.LD_LIBRARY_PATH || compatibilityLib },
    args: localBrowser ? ['--no-sandbox', '--disable-dev-shm-usage'] : chromium.args,
  });
}

interface Bookmark {
  title: string;
  id: string;
  pageIndex: number;
}

/** pdf-lib has no public outline API; build a simple, spec-compliant outline tree. */
function addOutlines(document: PDFDocument, bookmarks: Bookmark[]): void {
  if (bookmarks.length === 0) return;
  const pages = document.getPages();
  const outline = document.context.obj({ Type: 'Outlines', Count: bookmarks.length });
  const outlineRef = document.context.register(outline);
  const itemRefs = bookmarks.map(() => document.context.nextRef());
  const rootRef = document.catalog.get(PDFName.of('Pages'));
  bookmarks.forEach((bookmark, index) => {
    const page = pages[bookmark.pageIndex];
    if (!page) return;
    const item = document.context.obj({
      Title: PDFString.of(bookmark.title),
      Parent: outlineRef,
      Dest: [page.ref, 'XYZ', null, null, null],
      ...(index > 0 ? { Prev: itemRefs[index - 1]! } : {}),
      ...(index < bookmarks.length - 1 ? { Next: itemRefs[index + 1]! } : {}),
    });
    document.context.assign(itemRefs[index]!, item);
  });
  outline.set(PDFName.of('First'), itemRefs[0]!);
  outline.set(PDFName.of('Last'), itemRefs.at(-1)!);
  document.catalog.set(PDFName.of('Outlines'), outlineRef);
  document.catalog.set(PDFName.of('PageMode'), PDFName.of('UseOutlines'));
  // Keep the page tree reference live: some consumers expect it after a pdf-lib save.
  if (rootRef instanceof PDFRef) document.catalog.set(PDFName.of('Pages'), rootRef);
}

async function main(): Promise<void> {
  const book = JSON.parse(await readFile(path.join(root, 'data/bilingual_novel.json'), 'utf8')) as Edition;
  const browser = await launchBrowser();
  let rawPdf: Uint8Array;
  let bookmarks: Bookmark[];
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 960 } });
    page.setDefaultTimeout(0);
    page.on('console', (message) => {
      if (message.type() === 'error') console.error(`Browser: ${message.text()}`);
    });
    await page.goto(`file://${htmlPath}`, { waitUntil: 'load', timeout: 0 });
    await page.evaluate(() => { (window as unknown as { PagedConfig: object }).PagedConfig = { auto: false }; });
    const pagedPolyfill = path.join(path.dirname(require.resolve('pagedjs')), '../dist/paged.polyfill.js');
    await page.addScriptTag({ path: pagedPolyfill });
    await page.evaluate(async () => {
      const paged = (window as unknown as { PagedPolyfill: { preview: () => Promise<unknown> } }).PagedPolyfill;
      await paged.preview();
    });
    await page.waitForSelector('.pagedjs_page', { timeout: 0 });
    const pages = await page.locator('.pagedjs_page').count();
    console.log(`Paginated ${pages} A4 pages. Exporting PDF…`);
    const bookmarkData = await page.evaluate(() => {
      const pageElements = Array.from(document.querySelectorAll<HTMLElement>('.pagedjs_page'));
      return Array.from(document.querySelectorAll<HTMLElement>('[data-bookmark]')).map((element) => {
        const cloned = document.querySelectorAll<HTMLElement>(`[data-bookmark="${CSS.escape(element.dataset.bookmark ?? '')}"]`);
        const located = Array.from(cloned).find((candidate) => candidate.closest('.pagedjs_page'));
        const parent = located?.closest('.pagedjs_page');
        return {
          title: element.dataset.bookmark ?? '',
          id: element.id,
          pageIndex: parent ? pageElements.indexOf(parent as HTMLElement) : 0,
        };
      });
    });
    bookmarks = bookmarkData.filter((bookmark, index, all) =>
      bookmark.pageIndex >= 0 && all.findIndex((candidate) => candidate.id === bookmark.id && candidate.id !== '') === index,
    );
    rawPdf = await page.pdf({
      printBackground: true,
      preferCSSPageSize: true,
      displayHeaderFooter: false,
    });
  } finally {
    await browser.close();
  }

  const pdfDocument = await PDFDocument.load(rawPdf);
  pdfDocument.setTitle('Neuromancer — Ấn bản đối sánh Anh–Việt & Cẩm nang B2–C1');
  pdfDocument.setAuthor('William Gibson');
  pdfDocument.setSubject('Bilingual English–Vietnamese study edition; academic reading and language development');
  pdfDocument.setKeywords(['Neuromancer', 'bilingual', 'English', 'Vietnamese', 'B2', 'C1', 'Astryx']);
  pdfDocument.setCreator('TypeScript · Astryx Gothic · Paged.js · Chromium');
  pdfDocument.setProducer('Neuromancer TypeScript PDF pipeline');
  addOutlines(pdfDocument, bookmarks);
  const finalPdf = await pdfDocument.save({ useObjectStreams: true });
  await writeFile(pdfPath, finalPdf);

  const stats = getBookStats(book);
  const report = {
    generator: 'TypeScript / Astryx Gothic / Paged.js',
    source: 'data/bilingual_novel.json',
    output: 'output/neuromancer_bilingual_edition.pdf',
    ...stats,
    pages: pdfDocument.getPageCount(),
    bookmarks: bookmarks.length,
    bytes: finalPdf.byteLength,
    sha256: createHash('sha256').update(finalPdf).digest('hex'),
    sourceContentModified: false,
  };
  await writeFile(path.join(root, 'output/build-report.json'), `${JSON.stringify(report, null, 2)}\n`);
  console.log(`Created ${pdfPath} (${report.pages} pages, ${(report.bytes / 1_048_576).toFixed(2)} MiB).`);
}

await main();
