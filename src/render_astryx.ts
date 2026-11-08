import * as fs from 'fs';
import * as path from 'path';
import { AstryxCyberpunkTheme } from './astryx_design_system.js';

interface GrammarRule {
  rule: string;
  explanation: string;
  example: string;
}

interface ChapterStudyGuide {
  title?: string;
  summary_vi?: string;
  grammar_focus?: GrammarRule[];
  key_vocabulary?: string[];
}

interface ParagraphData {
  id: string;
  en: string;
  vi: string;
  vocab_highlights?: string[];
}

interface ChapterData {
  chapter_index: number;
  chapter_title_en: string;
  chapter_title_vi: string;
  study_guide?: ChapterStudyGuide;
  paragraphs: ParagraphData[];
}

interface PartData {
  part_index: number;
  part_title_en: string;
  part_title_vi: string;
  chapters: ChapterData[];
}

interface GlossaryEntry {
  term: string;
  ipa: string;
  pos: string;
  level: string;
  definition_en: string;
  definition_vi: string;
  literary_note: string;
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
  glossary: Record<string, GlossaryEntry>;
  parts: PartData[];
}

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function generateAstryxHtml(): string {
  const dataPath = path.resolve(process.cwd(), 'data/bilingual_novel.json');
  const rawData = fs.readFileSync(dataPath, 'utf-8');
  const novel: BilingualNovelData = JSON.parse(rawData);

  // Read Astryx CSS assets
  let astryxCss = '';
  let themeCss = '';
  try {
    const astryxCssPath = path.resolve(process.cwd(), 'node_modules/@astryxdesign/core/dist/astryx.css');
    if (fs.existsSync(astryxCssPath)) {
      astryxCss = fs.readFileSync(astryxCssPath, 'utf-8');
    }
    const themeCssPath = path.resolve(process.cwd(), 'node_modules/@astryxdesign/theme-neutral/dist/theme.css');
    if (fs.existsSync(themeCssPath)) {
      themeCss = fs.readFileSync(themeCssPath, 'utf-8');
    }
  } catch (e) {
    console.warn('Could not read Astryx CSS directly:', e);
  }

  const t = AstryxCyberpunkTheme;
  const bm = novel.target_benchmarks;

  const html: string[] = [];
  html.push(`<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neuromancer - Ấn Bản Song Ngữ Anh - Việt & Cẩm Nang Học Thuật C1/C2 (Meta Astryx Edition)</title>
<style>
/* Astryx Base & Theme Styles */
${themeCss}
${astryxCss}

@page {
  size: A4;
  margin: 1.8cm 1.5cm 2cm 1.5cm;
}

:root {
  --color-primary: ${t.colors.primary};
  --color-primary-muted: ${t.colors.primaryMuted};
  --color-accent: ${t.colors.accent};
  --color-accent-glow: ${t.colors.accentGlow};
  --color-bg-dark: ${t.colors.bgDark};
  --color-bg-card: ${t.colors.bgCard};
  --color-bg-hover: ${t.colors.bgHover};
  --color-border-muted: ${t.colors.borderMuted};
  --color-border-strong: ${t.colors.borderStrong};
  --color-text-primary: ${t.colors.textPrimary};
  --color-text-secondary: ${t.colors.textSecondary};
  --color-text-muted: ${t.colors.textMuted};
  --font-sans: ${t.typography.fontSans};
  --font-serif: ${t.typography.fontSerif};
  --font-mono: ${t.typography.fontMono};
}

* {
  box-sizing: border-box;
}

body {
  font-family: var(--font-sans);
  color: var(--color-text-primary);
  line-height: ${t.typography.lineHeightBody};
  background: #ffffff;
  margin: 0;
  padding: 0;
  font-size: ${t.typography.fontSizeBody};
  -webkit-font-smoothing: antialiased;
}

/* Cover Section */
.cover-page {
  page-break-after: always;
  height: 94vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 35px 25px;
  border: 3px double #0d1b2a;
  background: radial-gradient(circle at 50% 20%, #f0fdf4 0%, #f8fafc 40%, #e2e8f0 100%);
  position: relative;
}

.astryx-badge-system {
  display: inline-block;
  font-size: 8pt;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 700;
  color: #0284c7;
  border: 1px solid #38bdf8;
  background: #f0f9ff;
  padding: 4px 10px;
  border-radius: 9999px;
  margin-bottom: 20px;
}

.cover-title {
  font-size: 38pt;
  font-weight: 900;
  letter-spacing: 5px;
  text-transform: uppercase;
  color: #0b132b;
  margin: 0 0 8px 0;
  font-family: var(--font-serif);
}

.cover-sub {
  font-size: 16.5pt;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 20px;
  letter-spacing: 0.8px;
}

.cover-author {
  font-size: 15pt;
  font-style: italic;
  color: #334155;
  margin-bottom: 30px;
}

.cover-desc {
  max-width: 680px;
  font-size: 10pt;
  line-height: 1.6;
  color: #1e293b;
  background: rgba(255, 255, 255, 0.95);
  padding: 22px 28px;
  border-radius: 8px;
  border: 1px solid #cbd5e1;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
  margin-bottom: 25px;
}

.badge-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin-top: 15px;
}

.badge-item {
  background: #0f172a;
  color: #38bdf8;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: 4px;
  font-size: 8.8pt;
  border: 1px solid #1e293b;
  font-family: var(--font-mono);
}

/* Page Break Containers */
.section-page {
  page-break-before: always;
  page-break-after: always;
}

.astryx-card {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border-muted);
  border-left: 5px solid var(--color-primary);
  padding: 16px 20px;
  margin-bottom: 25px;
  border-radius: 0 6px 6px 0;
}

.astryx-card-title {
  font-size: 15pt;
  font-weight: 800;
  color: var(--color-text-primary);
  margin-top: 0;
  margin-bottom: 10px;
  letter-spacing: 0.5px;
}

/* Table of Contents */
.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 24px;
  margin-top: 20px;
}

.toc-item {
  font-size: 9.3pt;
  line-height: 1.45;
  break-inside: avoid;
}

.toc-link {
  text-decoration: none;
  color: #0369a1;
  font-weight: 600;
}

/* Part Header */
.part-banner {
  page-break-before: always;
  background: linear-gradient(135deg, #0b132b 0%, #1e293b 100%);
  color: #ffffff;
  padding: 32px 24px;
  text-align: center;
  border-radius: 8px;
  margin-bottom: 28px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.part-title-en {
  font-size: 18pt;
  letter-spacing: 2.5px;
  font-weight: 800;
  color: #38bdf8;
  margin: 0 0 8px 0;
  text-transform: uppercase;
}

.part-title-vi {
  font-size: 13.5pt;
  font-weight: 500;
  color: #f1f5f9;
  margin: 0;
}

/* Chapter Container */
.chapter-container {
  margin-bottom: 35px;
  page-break-inside: auto;
}

.chapter-heading-bar {
  background: #f8fafc;
  border-bottom: 2px solid #cbd5e1;
  padding: 14px 18px;
  margin-top: 30px;
  margin-bottom: 18px;
  border-left: 6px solid #0284c7;
  page-break-after: avoid;
  border-radius: 0 4px 4px 0;
}

.chap-title-en {
  font-size: 15.5pt;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 4px 0;
  letter-spacing: 0.5px;
}

.chap-title-vi {
  font-size: 11.5pt;
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
  border-radius: 4px;
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
  font-size: 9.3pt;
  color: #334155;
  margin-bottom: 12px;
  line-height: 1.5;
}

.grammar-item {
  background: #ffffff;
  border: 1px solid #fcd34d;
  padding: 8px 12px;
  margin-bottom: 8px;
  border-radius: 4px;
  font-size: 9pt;
}

.grammar-name {
  font-weight: 700;
  color: #1d4ed8;
}

.grammar-eg {
  font-style: italic;
  color: #047857;
  margin-top: 3px;
  font-size: 8.8pt;
}

/* Parallel Bilingual Grid */
.bilingual-pair {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 12px;
  page-break-inside: avoid;
  align-items: stretch;
}

.col-en {
  flex: 1;
  background: #ffffff;
  padding: 8px 12px;
  border-left: 2px solid #94a3b8;
  font-size: 9.5pt;
  text-align: justify;
  line-height: 1.55;
  color: #0f172a;
}

.col-vi {
  flex: 1;
  background: #f8fafc;
  padding: 8px 12px;
  border-left: 2px solid #0284c7;
  font-size: 9.5pt;
  text-align: justify;
  line-height: 1.55;
  color: #1e293b;
}

/* Glossary Table */
.glossary-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 15px;
  font-size: 8.8pt;
}

.glossary-table th {
  background: #0f172a;
  color: #f8fafc;
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

.vocab-pill {
  background: #e0f2fe;
  color: #0369a1;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 8pt;
  font-weight: 700;
  display: inline-block;
  font-family: var(--font-mono);
}
</style>
</head>
<body>
`);

  // Cover Page
  html.push(`
<div class="cover-page">
  <div class="astryx-badge-system">AST परिजनों DESIGN SYSTEM • DUAL-LANGUAGE SCHOLARLY EDITION</div>
  <div class="cover-title">NEUROMANCER</div>
  <div class="cover-sub">ẤN BẢN SONG NGỮ ANH - VIỆT TOÀN DIỆN &amp; HỌC THUẬT CAO CẤP</div>
  <div class="cover-author">Tác giả: William Gibson • Chuyển ngữ song song &amp; Khảo cứu học thuật</div>
  <div class="cover-desc">
    Kiệt tác khai sinh văn hóa Cyberpunk, đoạt trọn vẹn cả 3 vương miện danh giá nhất của làng văn học khoa học viễn tưởng (Hugo, Nebula, Philip K. Dick).
    <br><br>
    Ấn bản được thiết kế chuyên biệt phục vụ người học nâng cấp năng lực ngôn ngữ đạt và vượt qua các mốc chuẩn học thuật quốc tế đỉnh cao:
    <div class="badge-container">
      <div class="badge-item">IELTS: ${escapeHtml(bm.IELTS)}</div>
      <div class="badge-item">TOEFL iBT: ${escapeHtml(bm.TOEFL_iBT)}</div>
      <div class="badge-item">Cambridge C1/C2: ${escapeHtml(bm.Cambridge)}</div>
      <div class="badge-item">PTE Academic: ${escapeHtml(bm.PTE_Academic)}</div>
      <div class="badge-item">DET: ${escapeHtml(bm.DET)}</div>
    </div>
  </div>
  <div style="font-size: 8.5pt; color: #64748b; margin-top: 15px;">
    Toàn văn 24 chương nguyên tác &amp; bản dịch đối sánh câu-đoạn • Thiết kế giao diện Astryx • Cẩm nang ngữ pháp và thuật ngữ C1/C2
  </div>
</div>
`);

  // Table of Contents & Guidance
  html.push(`
<div class="section-page">
  <div class="astryx-card">
    <div class="astryx-card-title">MỤC LỤC &amp; ĐỊNH HƯỚNG PHƯƠNG PHÁP HỌC SONG NGỮ HỌC THUẬT</div>
    <p>
      Ấn bản áp dụng kỹ thuật <strong>Dual-Language Synoptic Layout (Đối chiếu song ngữ trực quan)</strong>, hỗ trợ tối đa cho học viên ôn luyện các kỳ thi chứng chỉ học thuật tiếng Anh bậc cao (IELTS 7.0+, TOEFL 90/5.0, Cambridge C1/C2, PTE 65, DET 120).
    </p>
    <p>
      Người học được khuyến nghị đọc cột nguyên tác tiếng Anh (bên trái) để cảm thụ cấu trúc cú pháp phức hợp và phong cách Cyberpunk kinh điển của William Gibson, sau đó đối chiếu cột tiếng Việt (bên phải) để củng cố khả năng thấu hiểu ngữ nghĩa, nghệ thuật diễn ngôn và từ vựng trừu tượng.
    </p>
  </div>

  <h3 style="color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 6px; margin-top: 20px;">DANH MỤC CÁC PHẦN VÀ CHƯƠNG</h3>
  <div class="toc-grid">
`);

  for (const part of novel.parts) {
    for (const chap of part.chapters) {
      html.push(`
    <div class="toc-item">
      <a class="toc-link" href="#chap-${chap.chapter_index}">Chương ${chap.chapter_index}: ${escapeHtml(chap.chapter_title_vi)}</a>
      <br><span style="font-size: 8.2pt; color: #64748b;">${escapeHtml(part.part_title_en)}</span>
    </div>
`);
    }
  }

  html.push(`
  </div>
</div>
`);

  // Academic Glossary
  html.push(`
<div class="section-page">
  <div class="astryx-card">
    <div class="astryx-card-title">BẢNG TRA CỨU THUẬT NGỮ CYBERPUNK &amp; TỪ VỰNG HỌC THUẬT C1/C2</div>
    <p>Hệ thống thuật ngữ được William Gibson khai sinh đã trở thành nền tảng của văn hóa kỹ thuật số đương đại và là nguồn ngữ liệu học thuật vô giá phục vụ các kỳ thi Cambridge C1/C2, IELTS 7.0 - 8.5+, TOEFL và GRE.</p>
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

  for (const [key, v] of Object.entries(novel.glossary)) {
    html.push(`
      <tr>
        <td><strong>${escapeHtml(v.term)}</strong><br><span style="color:#64748b; font-family: monospace;">${escapeHtml(v.ipa)}</span> (${escapeHtml(v.pos)})</td>
        <td><span class="vocab-pill">${escapeHtml(v.level)}</span></td>
        <td>${escapeHtml(v.definition_en)}</td>
        <td><strong>${escapeHtml(v.definition_vi)}</strong><br><span style="font-size: 8.2pt; color: #475569;">${escapeHtml(v.literary_note)}</span></td>
      </tr>
`);
  }

  html.push(`
    </tbody>
  </table>
</div>
`);

  // Chapters and Parts
  for (const part of novel.parts) {
    html.push(`
<div class="part-banner">
  <div class="part-title-en">${escapeHtml(part.part_title_en)}</div>
  <div class="part-title-vi">${escapeHtml(part.part_title_vi)}</div>
</div>
`);

    for (const chap of part.chapters) {
      const guide = chap.study_guide;
      html.push(`
<div class="chapter-container" id="chap-${chap.chapter_index}">
  <div class="chapter-heading-bar">
    <div class="chap-title-en">CHAPTER ${chap.chapter_index}: ${escapeHtml(chap.chapter_title_en)}</div>
    <div class="chap-title-vi">${escapeHtml(chap.chapter_title_vi)}</div>
  </div>
`);

      if (guide && guide.summary_vi) {
        html.push(`
  <div class="study-guide-card">
    <div class="study-title">TỔNG QUAN NỘI DUNG &amp; PHÂN TÍCH HỌC THUẬT (C1/C2 ACADEMIC GUIDE)</div>
    <div class="study-summary">${escapeHtml(guide.summary_vi)}</div>
`);
        if (guide.grammar_focus && guide.grammar_focus.length > 0) {
          html.push(`<div style="font-weight: 700; color: #1e3a8a; font-size: 9pt; margin-bottom: 6px;">CẤU TRÚC NGỮ PHÁP TIÊU BIỂU:</div>`);
          for (const gf of guide.grammar_focus) {
            html.push(`
    <div class="grammar-item">
      <div class="grammar-name">• ${escapeHtml(gf.rule)}: <span style="font-weight: normal; color: #334155;">${escapeHtml(gf.explanation)}</span></div>
      <div class="grammar-eg">Ví dụ nguyên tác: "${escapeHtml(gf.example)}"</div>
    </div>
`);
          }
        }
        html.push(`</div>`);
      }

      for (const p of chap.paragraphs) {
        const pEnEscaped = escapeHtml(p.en);
        const pViEscaped = escapeHtml(p.vi);

        html.push(`
  <div class="bilingual-pair">
    <div class="col-en">${pEnEscaped}</div>
    <div class="col-vi">${pViEscaped}</div>
  </div>
`);
      }

      html.push(`</div>`);
    }
  }

  html.push(`
</body>
</html>
`);

  const fullHtml = html.join('\n');
  const outHtmlPath = path.resolve(process.cwd(), 'data/novel_bilingual.html');
  fs.writeFileSync(outHtmlPath, fullHtml, 'utf-8');
  console.log(`Generated Astryx HTML at: ${outHtmlPath}`);
  return outHtmlPath;
}

if (process.argv[1] && process.argv[1].endsWith('render_astryx.ts')) {
  generateAstryxHtml();
}
