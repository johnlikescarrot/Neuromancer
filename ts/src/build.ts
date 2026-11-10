/**
 * Build entry: content -> HTML -> PDF (two-pass, so the contents page carries
 * real page numbers). Writes:
 *   ts/build/book.html   (the rendered intermediate)
 *   ts/build/pass1.pdf   (first pass, used only to locate headings)
 *   output/neuromancer_bilingual_academic_companion.pdf
 */
import { mkdirSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { book, stats } from "./content/index.js";
import { embeddedFontsCss } from "./design/fonts.js";
import { renderHtml } from "./html/render.js";
import { FOOTER_TEMPLATE, HEADER_TEMPLATE, launchChromium } from "./pdf/chromium.js";

const here = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(here, "..", "..");
const buildDir = join(here, "build");
const outputDir = join(repoRoot, "output");

/** Headings we place on the contents page, in order, with their visible mark text. */
const TOC_MARKS = [
  "How this companion works",
  "Target Credentials",
  "The book and its coronation",
  "Character guide",
  "Close reading: one sentence, four moves",
  "PART ONE",
  "UNIT 01",
  "UNIT 02",
  "PART TWO",
  "UNIT 03",
  "UNIT 04",
  "UNIT 05",
  "UNIT 06",
  "UNIT 07",
  "PART THREE",
  "UNIT 08",
  "UNIT 09",
  "UNIT 10",
  "UNIT 11",
  "UNIT 12",
  "PART FOUR",
  "UNIT 13",
  "UNIT 14",
  "UNIT 15",
  "UNIT 16",
  "UNIT 17",
  "UNIT 18",
  "UNIT 19",
  "UNIT 20",
  "UNIT 21",
  "UNIT 22",
  "UNIT 23",
  "CODA",
  "UNIT 24",
  "GRAMMAR",
  "GLOSSARY",
  "Exam Playbooks",
  "Study Plans",
  "Answer Key",
  "Gibson, William. Neuromancer",
];

async function locateMarks(pdfPath: string): Promise<Map<string, number>> {
  const pageMap = new Map<string, number>();
  try {
    const { getDocument } = await import("pdfjs-dist/legacy/build/pdf.mjs");
    const data = new Uint8Array(await (await import("node:fs/promises")).readFile(pdfPath));
    const doc = await getDocument({ data, useSystemFonts: true }).promise;
    const pages: string[] = [];
    for (let i = 1; i <= doc.numPages; i++) {
      const page = await doc.getPage(i);
      const content = await page.getTextContent();
      pages.push(
        content.items
          .map((it) => ("str" in it ? it.str : ""))
          .join(" ")
          .replace(/\s+/g, " "),
      );
    }
    // Skip cover, legal and contents pages: they echo the marks in their own text.
    let start = 0;
    for (let i = 0; i < pages.length; i++) {
      if (pages[i].includes("Book Map") && pages[i].includes("Contents")) start = i + 1;
    }
    for (const mark of TOC_MARKS) {
      for (let i = start; i < pages.length; i++) {
        if (pages[i].includes(mark)) {
          pageMap.set(mark, i + 1);
          break;
        }
      }
    }
  } catch (err) {
    console.warn("page-number pass skipped:", (err as Error).message);
  }
  return pageMap;
}

async function printPdf(browser: Awaited<ReturnType<typeof launchChromium>>, html: string, path: string): Promise<void> {
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: "load", timeout: 120_000 });
  await page.evaluate(() => (globalThis as Record<string, unknown>) && Promise.resolve());
  await page.pdf({
    path,
    format: "A4",
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: HEADER_TEMPLATE,
    footerTemplate: FOOTER_TEMPLATE,
    margin: { top: "17mm", bottom: "19mm", left: "15mm", right: "15mm" },
  });
  await page.close();
}

async function main(): Promise<void> {
  mkdirSync(buildDir, { recursive: true });
  mkdirSync(outputDir, { recursive: true });

  console.log("embedding fonts...");
  const fontCss = embeddedFontsCss();

  const outPath = join(outputDir, "neuromancer_bilingual_academic_companion.pdf");
  const pass1Path = join(buildDir, "pass1.pdf");

  console.log("rendering HTML (pass 1)...");
  writeFileSync(join(buildDir, "book.html"), renderHtml(book, fontCss), "utf8");

  const browser = await launchChromium();
  try {
    console.log("printing PDF (pass 1)...");
    await printPdf(browser, renderHtml(book, fontCss), pass1Path);

    console.log("locating headings for the contents page...");
    const pageMap = await locateMarks(pass1Path);
    console.log(`page numbers found for ${pageMap.size}/${TOC_MARKS.length} headings`);

    console.log("printing final PDF (pass 2)...");
    writeFileSync(join(buildDir, "book.html"), renderHtml(book, fontCss, pageMap), "utf8");
    await printPdf(browser, renderHtml(book, fontCss, pageMap), outPath);
  } finally {
    await browser.close();
  }

  console.log("\nBuild complete.");
  console.log(`  chapters:     ${stats.chapters} units in ${stats.parts} parts`);
  console.log(`  grammar:      ${stats.grammarUnits} units`);
  console.log(`  glossary:     ${stats.glossary} entries`);
  console.log(`  practice:     ${stats.practiceItems} items with answer key`);
  console.log(`  exams:        ${stats.exams} playbooks`);
  console.log(`  output:       ${outPath}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
