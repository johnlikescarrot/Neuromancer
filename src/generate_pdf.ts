import path from 'path';
import fs from 'fs';
import { chromium } from 'playwright';

export async function generateBilingualPdf(htmlFilePath?: string, outputPdfPath?: string) {
  const htmlFile = path.resolve(htmlFilePath || 'data/novel_bilingual.html');
  const pdfOut = path.resolve(outputPdfPath || 'output/neuromancer_bilingual_edition.pdf');

  if (!fs.existsSync(htmlFile)) {
    throw new Error(`HTML source file does not exist: ${htmlFile}`);
  }

  const outDir = path.dirname(pdfOut);
  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  console.log(`Starting browser for Astryx PDF rendering...`);
  console.log(`Loading HTML from: file://${htmlFile}`);
  const startTime = Date.now();

  // Determine available executable
  const possiblePaths = [
    '/usr/bin/google-chrome',
    '/home/jules/.cache/ms-playwright/chromium_headless_shell-1208/chrome-headless-shell-linux64/chrome-headless-shell',
    '/home/jules/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome',
  ];
  let executablePath: string | undefined = undefined;
  for (const p of possiblePaths) {
    if (fs.existsSync(p)) {
      executablePath = p;
      break;
    }
  }

  const browser = await chromium.launch({
    executablePath,
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
    ]
  });

  try {
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1200, height: 1600 });

    await page.goto(`file://${htmlFile}`, { waitUntil: 'load' });
    console.log('Document loaded. Awaiting typography and layout stabilization...');
    await page.waitForTimeout(3000);

    console.log('Rendering high-fidelity A4 bilingual PDF...');
    await page.pdf({
      path: pdfOut,
      format: 'A4',
      printBackground: true,
      margin: {
        top: '20mm',
        bottom: '20mm',
        left: '15mm',
        right: '15mm'
      },
      displayHeaderFooter: true,
      headerTemplate: '<div style="font-size: 8pt; width: 100%; text-align: right; color: #888; padding-right: 15mm; font-family: -apple-system, BlinkMacSystemFont, sans-serif;">Neuromancer (Astryx Bilingual C1/C2 Edition)</div>',
      footerTemplate: '<div style="font-size: 8pt; width: 100%; text-align: center; color: #888; font-family: -apple-system, BlinkMacSystemFont, sans-serif;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>'
    });

    const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
    const sizeMb = (fs.statSync(pdfOut).size / (1024 * 1024)).toFixed(2);
    console.log(`PDF successfully generated at: ${pdfOut}`);
    console.log(`Time taken: ${elapsed}s, File size: ${sizeMb} MB`);
  } finally {
    await browser.close();
  }
}

async function main() {
  await generateBilingualPdf();
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((err) => {
    console.error('Error generating PDF:', err);
    process.exit(1);
  });
}
