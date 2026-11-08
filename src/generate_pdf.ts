import * as path from 'path';
import * as fs from 'fs';
import { chromium } from 'playwright';
import { generateAstryxHtml } from './render_astryx.js';

export async function buildPdf(): Promise<void> {
  console.log('Rendering HTML with Astryx Design System...');
  const htmlPath = generateAstryxHtml();
  const pdfOut = path.resolve(process.cwd(), 'output/neuromancer_bilingual_edition.pdf');
  const outDir = path.dirname(pdfOut);
  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  console.log(`Launching Playwright to render PDF at: ${pdfOut}...`);
  const startTime = Date.now();

  const browser = await chromium.launch({
    executablePath: fs.existsSync('/home/jules/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome')
      ? '/home/jules/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome'
      : (fs.existsSync('/usr/bin/google-chrome') ? '/usr/bin/google-chrome' : undefined),
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
    ],
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1200, height: 1600 });

  const fileUrl = `file://${htmlPath}`;
  console.log(`Navigating to ${fileUrl}...`);
  await page.goto(fileUrl, { waitUntil: 'load' });
  await page.waitForTimeout(3000);

  console.log('Generating A4 PDF with academic headers & pagination...');
  await page.pdf({
    path: pdfOut,
    format: 'A4',
    printBackground: true,
    margin: {
      top: '20mm',
      bottom: '20mm',
      left: '15mm',
      right: '15mm',
    },
    displayHeaderFooter: true,
    headerTemplate: `
      <div style="font-size: 8pt; width: 100%; text-align: right; color: #64748b; padding-right: 15mm; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        Neuromancer (William Gibson) • Meta Astryx Bilingual Scholarly Edition
      </div>
    `,
    footerTemplate: `
      <div style="font-size: 8pt; width: 100%; text-align: center; color: #64748b; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        Page <span class="pageNumber"></span> of <span class="totalPages"></span>
      </div>
    `,
  });

  await browser.close();

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  const sizeMb = (fs.statSync(pdfOut).size / (1024 * 1024)).toFixed(2);
  console.log(`Successfully generated PDF in ${elapsed}s!`);
  console.log(`Output: ${pdfOut} (${sizeMb} MB)`);
}

if (process.argv[1] && process.argv[1].endsWith('generate_pdf.ts')) {
  buildPdf().catch((err) => {
    console.error('Failed to build PDF:', err);
    process.exit(1);
  });
}
