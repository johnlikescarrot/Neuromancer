import fs from "fs";
import path from "path";
import { renderEditionHtml } from "./render_astryx.js";
import { chromium } from "playwright";

async function buildPdf() {
  console.log("1. Rendering TypeScript + Astryx HTML template...");
  const html = renderEditionHtml();
  const htmlPath = path.resolve(process.cwd(), "data/novel_bilingual.html");
  fs.writeFileSync(htmlPath, html, "utf-8");
  console.log(`Saved HTML to ${htmlPath} (${(html.length / 1024 / 1024).toFixed(2)} MB)`);

  const pdfOutput = path.resolve(process.cwd(), "output/neuromancer_bilingual_edition.pdf");
  fs.mkdirSync(path.dirname(pdfOutput), { recursive: true });

  console.log("2. Launching browser for PDF generation...");
  const executablePath = fs.existsSync("/opt/google/chrome/chrome")
    ? "/opt/google/chrome/chrome"
    : "/home/jules/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome";

  const browser = await chromium.launch({
    executablePath,
    args: [
      "--no-sandbox",
      "--disable-setuid-sandbox",
      "--disable-dev-shm-usage",
      "--disable-gpu"
    ]
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1240, height: 1754 });

  console.log("3. Navigating to document...");
  await page.goto(`file://${htmlPath}`, { waitUntil: "load", timeout: 60000 });
  await page.waitForTimeout(2000);

  console.log("4. Rendering PDF with precise A4 dimensions and academic headers...");
  await page.pdf({
    path: pdfOutput,
    format: "A4",
    printBackground: true,
    margin: {
      top: "20mm",
      bottom: "20mm",
      left: "15mm",
      right: "15mm"
    },
    displayHeaderFooter: true,
    headerTemplate: `
      <div style="font-size: 8pt; width: 100%; text-align: right; color: #64748b; padding-right: 15mm; font-family: -apple-system, sans-serif;">
        Neuromancer (William Gibson) — Astryx Bilingual Academic Edition
      </div>
    `,
    footerTemplate: `
      <div style="font-size: 8pt; width: 100%; text-align: center; color: #64748b; font-family: -apple-system, sans-serif;">
        Trang <span class="pageNumber"></span> / <span class="totalPages"></span>
      </div>
    `
  });

  await browser.close();

  const stats = fs.statSync(pdfOutput);
  console.log(`Successfully generated PDF: ${pdfOutput}`);
  console.log(`PDF Size: ${(stats.size / 1024 / 1024).toFixed(2)} MB`);
}

buildPdf().catch((err) => {
  console.error("Error generating PDF:", err);
  process.exit(1);
});
