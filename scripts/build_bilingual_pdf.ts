import fs from 'fs';
import path from 'path';
import { chromium } from 'playwright';

interface GlossaryItem {
  term: string;
  ipa: string;
  pos: string;
  level: string;
  definition_en: string;
  definition_vi: string;
  literary_note: string;
}

interface GrammarFocusItem {
  rule: string;
  explanation: string;
  example: string;
}

interface StudyGuide {
  title?: string;
  summary_vi?: string;
  grammar_focus?: GrammarFocusItem[];
  key_vocabulary?: string[];
}

interface Paragraph {
  id: string;
  en: string;
  vi: string;
  vocab_highlights?: string[];
}

interface Chapter {
  chapter_index: number;
  chapter_title_en: string;
  chapter_title_vi: string;
  study_guide: StudyGuide;
  paragraphs: Paragraph[];
}

interface Part {
  part_index: number;
  part_title_en: string;
  part_title_vi: string;
  chapters: Chapter[];
}

interface BilingualNovelData {
  title: string;
  author: string;
  target_benchmarks: {
    IELTS: string;
    TOEFL_iBT: string;
    Cambridge: string;
    PTE_Academic: string;
    DET: string;
  };
  glossary: Record<string, GlossaryItem>;
  parts: Part[];
}

function escapeHtml(unsafe: string): string {
  return unsafe
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

export function generateBilingualHtml(data: BilingualNovelData): string {
  const benchmarks = data.target_benchmarks;
  const glossary = data.glossary;
  const parts = data.parts;

  // Read Astryx Gothic Theme CSS directly from node_modules
  const astryxThemeCssPath = path.resolve('node_modules/@astryxdesign/theme-gothic/dist/theme.css');
  let astryxCss = '';
  if (fs.existsSync(astryxThemeCssPath)) {
    astryxCss = fs.readFileSync(astryxThemeCssPath, 'utf-8');
  }

  const htmlParts: string[] = [];

  htmlParts.push(`<!DOCTYPE html>
<html lang="vi" data-astryx-theme="gothic">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neuromancer - Ấn Bản Song Ngữ Anh - Việt &amp; Cẩm Nang Học Thuật C1/C2 (Astryx Edition)</title>
<style>
/* Astryx Design System Theme Injection */
${astryxCss}

/* Print Layout & Typography optimized for A4 Publication */
@page {
  size: A4;
  margin: 1.8cm 1.5cm 2cm 1.5cm;
  @bottom-center {
    content: counter(page);
    font-size: 8.5pt;
    color: #4b5563;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: #111827;
  line-height: 1.55;
  background-color: #ffffff;
  margin: 0;
  padding: 0;
  font-size: 10pt;
  -webkit-font-smoothing: antialiased;
}

/* Cover Page */
.cover-page {
  page-break-after: always;
  height: 94vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 40px 20px;
  border: 3px double #1f2937;
  background: radial-gradient(circle at 50% 30%, #f9fafb 0%, #e5e7eb 100%);
}

.cover-badge-top {
  display: inline-block;
  background-color: #111827;
  color: #38bdf8;
  font-size: 9pt;
  font-weight: 700;
  letter-spacing: 2px;
  padding: 6px 14px;
  border-radius: 9999px;
  text-transform: uppercase;
  margin-bottom: 25px;
}

.cover-title {
  font-size: 42pt;
  font-weight: 900;
  letter-spacing: 6px;
  text-transform: uppercase;
  color: #0f172a;
  margin-bottom: 10px;
  font-family: "Times New Roman", Times, Georgia, serif;
}

.cover-sub {
  font-size: 17pt;
  font-weight: 700;
  color: #1e3a8a;
  margin-bottom: 20px;
  letter-spacing: 1px;
}

.cover-author {
  font-size: 14pt;
  font-style: italic;
  color: #4b5563;
  margin-bottom: 35px;
}

.cover-desc {
  max-width: 660px;
  font-size: 10.5pt;
  line-height: 1.6;
  color: #374151;
  background: rgba(255, 255, 255, 0.95);
  padding: 22px 28px;
  border-radius: 8px;
  border: 1px solid #d1d5db;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  margin-bottom: 25px;
}

.badge-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-top: 15px;
}

.badge {
  background: #0f172a;
  color: #38bdf8;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 9pt;
  border: 1px solid #1e293b;
}

/* Academic Section Page */
.section-page {
  page-break-before: always;
  page-break-after: always;
}

.intro-box {
  background: #f0fdf4;
  border-left: 5px solid #16a34a;
  padding: 16px 20px;
  margin-bottom: 25px;
  border-radius: 0 6px 6px 0;
}

.intro-title {
  font-size: 17pt;
  font-weight: 800;
  color: #14532d;
  margin-top: 0;
  margin-bottom: 12px;
}

/* TOC */
.toc-list {
  list-style: none;
  padding: 0;
  columns: 2;
  column-gap: 32px;
}

.toc-item {
  margin-bottom: 12px;
  font-size: 9.5pt;
  break-inside: avoid;
}

.toc-link {
  text-decoration: none;
  color: #0369a1;
  font-weight: 600;
}

/* Part Header */
.part-header {
  page-break-before: always;
  background: linear-gradient(135deg, #090d16 0%, #1e293b 100%);
  color: #ffffff;
  padding: 32px 24px;
  text-align: center;
  border-radius: 8px;
  margin-bottom: 28px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.part-title-en {
  font-size: 19pt;
  letter-spacing: 2px;
  font-weight: 800;
  color: #38bdf8;
  margin: 0 0 10px 0;
}

.part-title-vi {
  font-size: 14pt;
  font-weight: 500;
  color: #f1f5f9;
  margin: 0;
}

/* Chapter Container */
.chapter-container {
  margin-bottom: 35px;
  page-break-inside: auto;
}

.chapter-header {
  background: #f8fafc;
  border-bottom: 2px solid #cbd5e1;
  padding: 14px 18px;
  margin-top: 32px;
  margin-bottom: 20px;
  border-left: 6px solid #2563eb;
  page-break-after: avoid;
}

.chap-title-en {
  font-size: 15pt;
  font-weight: 800;
  color: #1e3a8a;
  margin: 0 0 4px 0;
}

.chap-title-vi {
  font-size: 12pt;
  color: #475569;
  font-weight: 600;
  margin: 0;
}

/* Study Guide Box */
.study-guide-card {
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-left: 5px solid #d97706;
  padding: 14px 18px;
  margin-bottom: 22px;
  border-radius: 6px;
  page-break-inside: avoid;
}

.study-title {
  font-size: 10.5pt;
  font-weight: 800;
  color: #92400e;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 0;
  margin-bottom: 8px;
}

.study-summary {
  font-size: 9.6pt;
  color: #374151;
  margin-bottom: 12px;
  line-height: 1.5;
}

.grammar-item {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  padding: 9px 12px;
  margin-bottom: 8px;
  border-radius: 4px;
  font-size: 9.2pt;
}

.grammar-name {
  font-weight: 700;
  color: #1d4ed8;
}

.grammar-eg {
  font-style: italic;
  color: #047857;
  margin-top: 3px;
}

/* Parallel Bilingual Grid */
.bilingual-pair {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 14px;
  page-break-inside: avoid;
  align-items: stretch;
}

.col-en {
  flex: 1;
  background: #ffffff;
  padding: 9px 13px;
  border-left: 2px solid #94a3b8;
  font-size: 9.6pt;
  text-align: justify;
  line-height: 1.55;
  color: #0f172a;
}

.col-vi {
  flex: 1;
  background: #f8fafc;
  padding: 9px 13px;
  border-left: 2px solid #3b82f6;
  font-size: 9.6pt;
  text-align: justify;
  line-height: 1.55;
  color: #1e293b;
}

.vocab-pill {
  background: #dbeafe;
  color: #1d4ed8;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 8.5pt;
  font-weight: 700;
  margin-right: 4px;
  display: inline-block;
}

/* Glossary Table */
.glossary-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 15px;
  font-size: 9pt;
}

.glossary-table th {
  background: #0f172a;
  color: #ffffff;
  padding: 8px 10px;
  text-align: left;
  border: 1px solid #334155;
}

.glossary-table td {
  padding: 8px 10px;
  border: 1px solid #cbd5e1;
  vertical-align: top;
}

.glossary-table tr:nth-child(even) {
  background: #f8fafc;
}
</style>
</head>
<body>
`);

  // Cover Page
  htmlParts.push(`
<div class="cover-page">
  <div class="cover-badge-top">Astryx Design System • Definitive Publication</div>
  <div class="cover-title">NEUROMANCER</div>
  <div class="cover-sub">ẤN BẢN SONG NGỮ ANH - VIỆT TOÀN DIỆN &amp; HỌC THUẬT CAO CẤP</div>
  <div class="cover-author">Tác giả: William Gibson • Phiên bản Khảo cứu &amp; Thiết kế Học thuật Toàn bích</div>
  <div class="cover-desc">
    Tác phẩm kinh điển khai sinh thể loại Cyberpunk, đạt cú đúp ba giải thưởng danh giá bậc nhất thế giới khoa học viễn tưởng (Hugo, Nebula, Philip K. Dick).
    <br><br>
    Được thiết kế và biên soạn đặc thù nhằm nâng tầm năng lực đọc hiểu văn chương học thuật đỉnh cao, phục vụ người học chinh phục các mốc điểm chuẩn quốc tế danh giá nhất:
    <div class="badge-container">
      <div class="badge">IELTS ${escapeHtml(benchmarks.IELTS)}</div>
      <div class="badge">TOEFL iBT ${escapeHtml(benchmarks.TOEFL_iBT)}</div>
      <div class="badge">Cambridge C1/C2 ${escapeHtml(benchmarks.Cambridge)}</div>
      <div class="badge">PTE Academic ${escapeHtml(benchmarks.PTE_Academic)}</div>
      <div class="badge">DET ${escapeHtml(benchmarks.DET)}</div>
    </div>
  </div>
  <div style="font-size: 9pt; color: #64748b; margin-top: 15px;">
    Toàn văn 24 chương nguyên tác &amp; bản dịch đối sánh câu-đoạn • Thiết kế giao diện tài liệu tiêu chuẩn Astryx Design System
  </div>
</div>
`);

  // Table of Contents & Study Orientation Page
  htmlParts.push(`
<div class="section-page">
  <div class="intro-box">
    <div class="intro-title">MỤC LỤC &amp; HƯỚNG DẪN PHƯƠNG PHÁP HỌC SONG NGỮ HỌC THUẬT</div>
    <p>
      Cuốn sách này áp dụng phương pháp <strong>Dual-Language Synoptic Reading (Đọc đối sánh song song)</strong>, một trong những kỹ thuật học ngôn ngữ đỉnh cao nhất dành cho trình độ Advanced (C1) và Mastery (C2). Người học nên đọc đoạn văn bản gốc tiếng Anh ở cột trái trước, cảm nhận nghệ thuật miêu tả, cấu trúc ngữ pháp và sắc thái từ vựng; sau đó đối chiếu với cột tiếng Việt ở bên phải để thấu suốt ngữ nghĩa và nghệ thuật chuyển ngữ.
    </p>
    <p>
      Mỗi chương đều được trang bị phần <strong>Chapter Academic Masterclass</strong>, tổng hợp các kiến thức ngữ pháp tinh hoa (đảo ngữ, câu tuyệt đối, cú pháp tích lũy) thường xuất hiện trong các đề thi IELTS Reading/Writing Band 8.0+, TOEFL 90+ (hoặc 5.0), Cambridge C2 Proficiency (CPE), PTE Academic 65+ và DET 120+.
    </p>
  </div>

  <h3 style="color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 6px; margin-top: 20px;">DANH MỤC CÁC PHẦN VÀ CHƯƠNG</h3>
  <ul class="toc-list">
`);

  for (const part of parts) {
    for (const chap of part.chapters) {
      htmlParts.push(`
    <li class="toc-item">
      <a class="toc-link" href="#chap-${chap.chapter_index}">Chương ${chap.chapter_index}: ${escapeHtml(chap.chapter_title_vi)}</a>
      <br><span style="font-size: 8.5pt; color: #64748b;">Part: ${escapeHtml(part.part_title_en)}</span>
    </li>
`);
    }
  }

  htmlParts.push(`
  </ul>
</div>
`);

  // Glossary Section
  htmlParts.push(`
<div class="section-page">
  <div class="intro-box">
    <div class="intro-title">BẢNG TRA CỨU THUẬT NGỮ CYBERPUNK &amp; TỪ VỰNG HỌC THUẬT C1/C2</div>
    <p>Hệ thống thuật ngữ được William Gibson định hình trong Neuromancer đã trở thành nền tảng của văn hóa kỹ thuật số đương đại và là nguồn từ vựng trừu tượng đắt giá cho các kỳ thi học thuật.</p>
  </div>
  <table class="glossary-table">
    <thead>
      <tr>
        <th style="width: 22%;">Thuật ngữ / Phát âm</th>
        <th style="width: 14%;">Cấp độ</th>
        <th style="width: 32%;">Định nghĩa Tiếng Anh</th>
        <th style="width: 32%;">Ý nghĩa &amp; Chú giải Chuyên sâu</th>
      </tr>
    </thead>
    <tbody>
`);

  for (const [, v] of Object.entries(glossary)) {
    htmlParts.push(`
      <tr>
        <td><strong>${escapeHtml(v.term)}</strong><br><span style="color:#64748b; font-family: monospace;">${escapeHtml(v.ipa)}</span> (${escapeHtml(v.pos)})</td>
        <td><span class="vocab-pill">${escapeHtml(v.level)}</span></td>
        <td>${escapeHtml(v.definition_en)}</td>
        <td><strong>${escapeHtml(v.definition_vi)}</strong><br><span style="font-size: 8.5pt; color: #475569;">${escapeHtml(v.literary_note)}</span></td>
      </tr>
`);
  }

  htmlParts.push(`
    </tbody>
  </table>
</div>
`);

  // Parts and Chapters Content
  for (const part of parts) {
    htmlParts.push(`
<div class="part-header">
  <div class="part-title-en">${escapeHtml(part.part_title_en)}</div>
  <div class="part-title-vi">${escapeHtml(part.part_title_vi)}</div>
</div>
`);

    for (const chap of part.chapters) {
      const guide = chap.study_guide;
      htmlParts.push(`
<div class="chapter-container" id="chap-${chap.chapter_index}">
  <div class="chapter-header">
    <div class="chap-title-en">CHAPTER ${chap.chapter_index}: ${escapeHtml(chap.chapter_title_en)}</div>
    <div class="chap-title-vi">${escapeHtml(chap.chapter_title_vi)}</div>
  </div>
`);

      if (guide && guide.summary_vi) {
        htmlParts.push(`
  <div class="study-guide-card">
    <div class="study-title">TỔNG QUAN NỘI DUNG &amp; PHÂN TÍCH HỌC THUẬT (C1/C2 ACADEMIC GUIDE)</div>
    <div class="study-summary">${escapeHtml(guide.summary_vi)}</div>
`);
        if (guide.grammar_focus && guide.grammar_focus.length > 0) {
          htmlParts.push(`<div style="font-weight: bold; color: #1e3a8a; font-size: 9.3pt; margin-bottom: 6px;">CẤU TRÚC NGỮ PHÁP TIÊU BIỂU:</div>`);
          for (const gf of guide.grammar_focus) {
            htmlParts.push(`
    <div class="grammar-item">
      <div class="grammar-name">• ${escapeHtml(gf.rule)}: <span style="font-weight: normal; color: #334155;">${escapeHtml(gf.explanation)}</span></div>
      <div class="grammar-eg">Ví dụ nguyên tác: "${escapeHtml(gf.example)}"</div>
    </div>
`);
          }
        }
        htmlParts.push(`</div>`);
      }

      // Render bilingual paragraphs
      for (const p of chap.paragraphs) {
        const pEnEscaped = escapeHtml(p.en);
        const pViEscaped = escapeHtml(p.vi);

        htmlParts.push(`
  <div class="bilingual-pair">
    <div class="col-en">${pEnEscaped}</div>
    <div class="col-vi">${pViEscaped}</div>
  </div>
`);
      }

      htmlParts.push(`</div>`);
    }
  }

  htmlParts.push(`
</body>
</html>
`);

  return htmlParts.join('\n');
}

export async function buildPdf(): Promise<void> {
  const jsonPath = path.resolve('data/bilingual_novel.json');
  const htmlOutputPath = path.resolve('data/novel_bilingual.html');
  const pdfOutputPath = path.resolve('output/neuromancer_bilingual_edition.pdf');

  console.log('Reading novel dataset from:', jsonPath);
  const rawData = fs.readFileSync(jsonPath, 'utf-8');
  const novelData: BilingualNovelData = JSON.parse(rawData);

  console.log('Generating Astryx Design-powered bilingual HTML layout...');
  const htmlContent = generateBilingualHtml(novelData);
  fs.writeFileSync(htmlOutputPath, htmlContent, 'utf-8');
  console.log(`HTML generated successfully at ${htmlOutputPath} (${(fs.statSync(htmlOutputPath).size / (1024 * 1024)).toFixed(2)} MB)`);

  console.log('Launching headless Chromium browser with Playwright...');
  const browser = await chromium.launch({
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu'
    ]
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1200, height: 1600 });

  console.log('Navigating to generated HTML file...');
  await page.goto(`file://${htmlOutputPath}`, { waitUntil: 'load' });
  await page.waitForTimeout(3000);

  fs.mkdirSync(path.dirname(pdfOutputPath), { recursive: true });

  console.log('Compiling PDF with A4 publication specifications...');
  await page.pdf({
    path: pdfOutputPath,
    format: 'A4',
    printBackground: true,
    margin: {
      top: '20mm',
      bottom: '20mm',
      left: '15mm',
      right: '15mm'
    },
    displayHeaderFooter: true,
    headerTemplate: '<div style="font-size: 8pt; width: 100%; text-align: right; color: #888; padding-right: 15mm; font-family: sans-serif;">Neuromancer (Bilingual C1/C2 Astryx Edition)</div>',
    footerTemplate: '<div style="font-size: 8pt; width: 100%; text-align: center; color: #888; font-family: sans-serif;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>'
  });

  await browser.close();

  const pdfStats = fs.statSync(pdfOutputPath);
  console.log(`PDF successfully generated: ${pdfOutputPath} (${(pdfStats.size / (1024 * 1024)).toFixed(2)} MB)`);
}

if (process.argv[1]?.includes('build_bilingual_pdf.ts')) {
  buildPdf().catch((err) => {
    console.error('Fatal error during PDF generation:', err);
    process.exit(1);
  });
}
