import fs from 'fs';
import path from 'path';
import { BilingualNovel } from './types.js';
import { generateAstryxCSS } from './astryx_theme.js';

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

export function renderBilingualEditionHtml(novelData: BilingualNovel): string {
  const benchmarks = novelData.target_benchmarks;
  const glossary = novelData.glossary;
  const parts = novelData.parts;

  const htmlOut: string[] = [];

  htmlOut.push(`<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neuromancer - Ấn Bản Song Ngữ Anh - Việt & Cẩm Nang Học Thuật C1/C2 Toàn Diện (Astryx Edition)</title>
<style>
${generateAstryxCSS()}
</style>
</head>
<body>
`);

  // Cover Page
  htmlOut.push(`
<div class="cover-page">
  <div class="cover-badge-top">Astryx High-Performance Academic Typesetting</div>
  <div class="cover-title">NEUROMANCER</div>
  <div class="cover-sub">ẤN BẢN SONG NGỮ ANH - VIỆT TOÀN DIỆN &amp; HỌC THUẬT CAO CẤP</div>
  <div class="cover-author">Tác giả: William Gibson • Khảo cứu văn bản &amp; Chú giải học thuật C1/C2</div>
  <div class="cover-desc">
    Kiệt tác khai sinh thể loại Cyberpunk, vinh dự đoạt cả ba giải thưởng khoa học viễn tưởng danh giá bậc nhất: Hugo, Nebula và Philip K. Dick.
    <br><br>
    Được thiết kế và dàn trang tối ưu phục vụ học viên và chuyên gia chinh phục các ngưỡng chuẩn năng lực tiếng Anh quốc tế hàng đầu:
    <div class="badge-container">
      <div class="badge">IELTS ${benchmarks.IELTS}</div>
      <div class="badge">TOEFL iBT ${benchmarks.TOEFL_iBT}</div>
      <div class="badge">Cambridge ${benchmarks.Cambridge}</div>
      <div class="badge">PTE Academic ${benchmarks.PTE_Academic}</div>
      <div class="badge">DET ${benchmarks.DET}</div>
    </div>
  </div>
  <div style="font-size: 8.8pt; color: #64748b; margin-top: 20px;">
    Toàn văn 24 chương nguyên tác &amp; 2.598 đoạn văn song song • Hệ thống phân tích ngữ pháp &amp; Từ điển học thuật quốc tế
  </div>
</div>
`);

  // Section: Introduction & TOC
  htmlOut.push(`
<div class="section-page">
  <div class="intro-box">
    <div class="intro-title">MỤC LỤC &amp; HƯỚNG DẪN ĐỌC ĐỐI SÁNH HỌC THUẬT (SYNOPTIC READING)</div>
    <p>
      Ấn bản này được dàn trang theo nguyên lý <strong>Parallel Dual-Language Layout (Cột đối sánh song song)</strong> kết hợp hệ thống thiết kế hiện đại <strong>Astryx Design System</strong>. Cột bên trái hiển thị văn bản nguyên tác của William Gibson với phong cách miêu tả Neo-noir giàu hình ảnh và cú pháp cô đọng; cột bên phải hiển thị bản dịch tiếng Việt chuẩn mực, hỗ trợ người học đào sâu phân tích từ vựng, ngữ pháp và nghệ thuật hành văn.
    </p>
    <p>
      Phần đầu mỗi chương bao gồm <strong>Chapter Academic Masterclass</strong> tập trung vào các cấu trúc ngữ pháp học thuật tinh hoa (Inversion, Absolute Construction, Participial Phrases, Modality) tương thích với tiêu chí Lexical Resource &amp; Grammatical Range trong IELTS 7.0-8.5+, TOEFL 90+ / 5.0, Cambridge C1/C2 và PTE Academic 65+.
    </p>
  </div>

  <h3 style="color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 8px; margin-top: 24px;">DANH MỤC CÁC PHẦN VÀ CHƯƠNG</h3>
  <ul class="toc-list">
`);

  for (const part of parts) {
    for (const chap of part.chapters) {
      htmlOut.push(`
    <li class="toc-item">
      <a class="toc-link" href="#chap-${chap.chapter_index}">Chương ${chap.chapter_index}: ${escapeHtml(chap.chapter_title_vi)}</a>
      <br><span style="font-size: 8.5pt; color: #64748b;">${escapeHtml(part.part_title_en)}</span>
    </li>
`);
    }
  }

  htmlOut.push(`
  </ul>
</div>
`);

  // Section: Glossary
  htmlOut.push(`
<div class="section-page">
  <div class="intro-box">
    <div class="intro-title">BẢNG TRA CỨU THUẬT NGỮ CYBERPUNK &amp; TỪ VỰNG HỌC THUẬT C1/C2</div>
    <p>Hệ thống thuật ngữ mang tính tiên tri và các từ vựng học thuật đỉnh cao phục vụ người học nâng cấp văn phong luận thuyết và đọc hiểu học thuật nâng cao.</p>
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

  for (const [_, v] of Object.entries(glossary)) {
    htmlOut.push(`
      <tr>
        <td><strong>${escapeHtml(v.term)}</strong><br><span style="color:#64748b; font-family: monospace;">${escapeHtml(v.ipa)}</span> (${escapeHtml(v.pos)})</td>
        <td><span class="vocab-pill">${escapeHtml(v.level)}</span></td>
        <td>${escapeHtml(v.definition_en)}</td>
        <td><strong>${escapeHtml(v.definition_vi)}</strong><br><span style="font-size: 8.5pt; color: #475569;">${escapeHtml(v.literary_note)}</span></td>
      </tr>
`);
  }

  htmlOut.push(`
    </tbody>
  </table>
</div>
`);

  // Parts and Chapters
  for (const part of parts) {
    htmlOut.push(`
<div class="part-header">
  <div class="part-title-en">${escapeHtml(part.part_title_en)}</div>
  <div class="part-title-vi">${escapeHtml(part.part_title_vi)}</div>
</div>
`);

    for (const chap of part.chapters) {
      const guide = chap.study_guide;
      htmlOut.push(`
<div class="chapter-container" id="chap-${chap.chapter_index}">
  <div class="chapter-header">
    <div class="chap-title-en">CHAPTER ${chap.chapter_index}: ${escapeHtml(chap.chapter_title_en)}</div>
    <div class="chap-title-vi">${escapeHtml(chap.chapter_title_vi)}</div>
  </div>
`);

      if (guide && guide.summary_vi) {
        htmlOut.push(`
  <div class="study-guide-card">
    <div class="study-title">TỔNG QUAN NỘI DUNG &amp; PHÂN TÍCH HỌC THUẬT (C1/C2 MASTERCLASS)</div>
    <div class="study-summary">${escapeHtml(guide.summary_vi)}</div>
`);
        if (guide.grammar_focus && guide.grammar_focus.length > 0) {
          htmlOut.push(`<div style="font-weight: 700; color: #1e3a8a; font-size: 9.3pt; margin-bottom: 6px;">CẤU TRÚC NGỮ PHÁP TIÊU BIỂU:</div>`);
          for (const gf of guide.grammar_focus) {
            htmlOut.push(`
    <div class="grammar-item">
      <div class="grammar-name">• ${escapeHtml(gf.rule)}: <span style="font-weight: normal; color: #334155;">${escapeHtml(gf.explanation)}</span></div>
      <div class="grammar-eg">Ví dụ nguyên tác: "${escapeHtml(gf.example)}"</div>
    </div>
`);
          }
        }
        htmlOut.push(`</div>`);
      }

      // Bilingual paragraphs
      for (const p of chap.paragraphs) {
        let pEnText = escapeHtml(p.en);
        const pViText = escapeHtml(p.vi);

        // Highlight vocabulary terms if any
        if (p.vocab_highlights && p.vocab_highlights.length > 0) {
          for (const term of p.vocab_highlights) {
            const regex = new RegExp(`\\b(${term})\\b`, 'gi');
            pEnText = pEnText.replace(regex, '<span class="term-highlight">$1</span>');
          }
        }

        htmlOut.push(`
  <div class="bilingual-pair">
    <div class="col-en">${pEnText}</div>
    <div class="col-vi">${pViText}</div>
  </div>
`);
      }

      htmlOut.push(`</div>`);
    }
  }

  htmlOut.push(`
</body>
</html>
`);

  return htmlOut.join('\n');
}

export function main() {
  const jsonPath = path.resolve('data/bilingual_novel.json');
  const outPath = path.resolve('data/novel_bilingual.html');

  console.log(`Reading novel data from ${jsonPath}...`);
  const raw = fs.readFileSync(jsonPath, 'utf-8');
  const data: BilingualNovel = JSON.parse(raw);

  console.log('Rendering HTML with Astryx styling...');
  const htmlContent = renderBilingualEditionHtml(data);

  fs.writeFileSync(outPath, htmlContent, 'utf-8');
  const sizeMb = (fs.statSync(outPath).size / (1024 * 1024)).toFixed(2);
  console.log(`Generated HTML successfully: ${outPath} (${sizeMb} MB)`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main();
}
