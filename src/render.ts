import { readFile, writeFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import path from 'node:path';
import { STUDY_MODULES, type StudyModule } from './study-material.js';
import { getBookStats, type BookPart, type Edition } from './types.js';

const require = createRequire(import.meta.url);
const root = process.cwd();

export function escapeHtml(value: string): string {
  return value.replace(/[&<>"']/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
  })[character]!);
}

function text(value: string): string {
  return escapeHtml(value);
}

function renderModule(module: StudyModule, index: number): string {
  return `<section class="sheet module" id="${module.id}" data-bookmark="${text(module.title)}">
    <header class="module-head">
      <div class="module-index">${String(index + 1).padStart(2, '0')}</div>
      <div><p class="eyebrow">${text(module.eyebrow)}</p><h1 class="display">${text(module.title)}</h1><p class="lead">${text(module.intro)}</p></div>
    </header>
    ${module.blocks.map((block) => `<article class="study-block">
      <h2>${text(block.heading)}</h2>
      <div><p>${text(block.body)}</p>
      ${block.bullets ? `<ul>${block.bullets.map((bullet) => `<li>${text(bullet)}</li>`).join('')}</ul>` : ''}
      ${block.example ? `<div class="example"><div class="en">${text(block.example.en)}</div><div class="vi">${text(block.example.vi)}</div><div class="note">${text(block.example.note)}</div></div>` : ''}
      </div>
    </article>`).join('')}
  </section>`;
}

function renderPart(part: BookPart, position: number): string {
  const first = part.chapters[0]!.chapter_index;
  const last = part.chapters.at(-1)!.chapter_index;
  return `<section class="part" id="part-${part.part_index}" data-bookmark="${text(part.part_title_en)}">
    <div class="part-num">${String(position + 1).padStart(2, '0')}</div>
    <div class="part-content"><p class="eyebrow">${first === last ? `Chapter ${first}` : `Chapters ${first}–${last}`}</p>
      <h1>${text(part.part_title_en.replace(/^PART (ONE|TWO|THREE|FOUR) - /, '').replace(/^CODA - /, 'CODA · '))}</h1>
      <div class="vi">${text(part.part_title_vi)}</div></div>
    <div class="part-meta">NEUROMANCER · ẤN BẢN ĐỐI SÁNH ANH–VIỆT</div>
  </section>`;
}

export function renderBook(book: Edition, themeCss: string, printCss: string): string {
  const stats = getBookStats(book);
  const missing = book.parts.flatMap((part) => part.chapters).flatMap((chapter) =>
    chapter.paragraphs.filter((paragraph) => paragraph.en.trim() === paragraph.vi.trim())
      .map((paragraph) => ({ id: paragraph.id, chapter: chapter.chapter_index })),
  );
  const benchmarkRows: Array<[string, string, string]> = [
    ['IELTS', '7.0', 'Đọc phức hợp · Lexical Resource · Grammatical Range'],
    ['TOEFL iBT', '90 · trước 21/01/2026<br>5 · từ 21/01/2026', 'Inference · Rhetorical Purpose · Reading to Learn'],
    ['Cambridge English', '185 · C1 Advanced', 'Use of English · sắc thái · biến đổi cấu trúc'],
    ['PTE Academic', '65', 'Từ vựng trong ngữ cảnh · tóm tắt · xử lý văn bản'],
    ['Duolingo English Test', '120', 'Ngữ cảnh câu · nhận diện từ · sản xuất ngôn ngữ'],
  ];

  return `<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Neuromancer — Bilingual Study Edition</title>
<meta name="author" content="William Gibson">
<meta name="description" content="Ấn bản đối sánh Anh–Việt và cẩm nang học thuật B2–C1">
<style>${themeCss}</style><style>${printCss}</style></head>
<body data-astryx-theme="gothic"><main class="book">
<section class="cover" data-bookmark="Bìa sách"><div class="cover-grid">
  <div class="cover-brand">A BILINGUAL READING &amp; LANGUAGE LAB</div>
  <h1 class="cover-title">Neuro&shy;mancer</h1>
  <div class="cover-subtitle">Ấn bản đối sánh Anh–Việt<br>Cẩm nang đọc văn chương &amp; tiếng Anh học thuật B2–C1</div>
  <div class="cover-author">WILLIAM GIBSON</div>
  <div class="cover-meta"><span>24 CHƯƠNG · ${stats.paragraphs.toLocaleString('en-US')} CẶP ĐOẠN<br>${stats.glossaryTerms} MỤC THUẬT NGỮ CHÚ GIẢI</span><span>STUDY EDITION<br>ENGLISH / TIẾNG VIỆT</span></div>
</div></section>

<section class="sheet front" id="orientation" data-bookmark="Định hướng ấn bản">
  <p class="eyebrow">Reader orientation · Lời đầu sách</p><h1 class="display">Một cuốn sách.<br>Hai ngôn ngữ. Nhiều cách đọc.</h1>
  <p class="lead">Phiên bản này tái thiết kế trải nghiệm đọc đối sánh, kết nối văn chương Cyberpunk với rèn luyện đọc–viết B2–C1. Toàn bộ dữ liệu song ngữ sẵn có được giữ nguyên; phần học tập và hệ thống dàn trang được biên soạn riêng.</p>
  <div class="stat-row"><div class="stat"><strong>${stats.parts}</strong><span>phần + coda</span></div><div class="stat"><strong>${stats.chapters}</strong><span>chương</span></div><div class="stat"><strong>${stats.paragraphs.toLocaleString('en-US')}</strong><span>cặp đoạn</span></div><div class="stat"><strong>6</strong><span>module học tập</span></div></div>
  <div class="notice"><strong>Minh bạch về dữ liệu dịch.</strong> Bộ dữ liệu nguồn có ${stats.untranslatedCandidates} đoạn tiếng Việt trùng tiếng Anh — chủ yếu tên riêng, mốc giờ và chuỗi ký tự cố ý giữ nguyên. Chúng được đánh dấu <strong>TRÙNG VĂN BẢN NGUỒN</strong> và liệt kê ở phụ lục kiểm tra; không được tự động thay bằng nội dung dịch mới; việc trùng văn bản không đồng nghĩa thiếu bản dịch. Các đoạn còn lại giữ nguyên như dữ liệu cũ, chưa qua rà soát biên tập toàn diện.</div>
  <h2>Cách dùng nhanh</h2><p>Đọc cột trái trước và ghi suy luận; chỉ sau đó đối chiếu cột phải. Mã ở mỗi cặp đoạn giúp truy vết dữ liệu. Mỗi chương mở bằng tóm tắt và một điểm ngữ pháp/tu từ; ví dụ trong khung này là <strong>ví dụ học thuật minh họa</strong>, không mặc định là trích dẫn nguyên tác.</p>
  <div class="colophon"><div><p class="eyebrow">Design system</p><p class="small">TypeScript · Astryx Gothic design tokens<br>Paged.js · Chromium PDF · pdf-lib</p></div><div><p class="eyebrow">Nguyên tắc học tập</p><p class="small">Comprehension trước translation<br>Retrieval trước recognition<br>Accuracy trước complexity</p></div></div>
  <p class="small">Tác phẩm gốc và bản dịch thuộc quyền của các chủ sở hữu tương ứng. Tài liệu này không thay thế hướng dẫn, rubric hay đề luyện chính thức của tổ chức thi.</p>
</section>

<section class="sheet front" id="benchmarks" data-bookmark="Mục tiêu năng lực">
  <p class="eyebrow">Proficiency map · Bản đồ năng lực</p><h1 class="display">Từ B2 vững<br>đến C1 có chủ đích</h1>
  <p class="lead">Các mốc dưới đây là định hướng học tập theo yêu cầu của ấn bản, không phải cam kết điểm số hoặc bảng quy đổi chính thức giữa các kỳ thi.</p>
  <table class="benchmarks"><thead><tr><th>Bài thi</th><th>Mốc mục tiêu</th><th>Trọng tâm chuyển giao</th></tr></thead><tbody>
  ${benchmarkRows.map(([exam, score, skills]) => `<tr><td>${exam}</td><td>${score}</td><td>${skills}</td></tr>`).join('')}
  </tbody></table>
  <div class="notice"><strong>Đọc văn chương ≠ luyện đề.</strong> Hãy kết hợp học liệu này với bài thi mẫu và rubric hiện hành. Định dạng, thang điểm và chiến lược phòng thi có thể thay đổi; luôn kiểm tra nguồn chính thức của kỳ thi bạn dự định tham dự.</div>
  <h2>Ba dấu hiệu của tiến bộ</h2><p><strong>Chính xác hơn:</strong> giải thích được lựa chọn dựa trên bằng chứng. <strong>Độc lập hơn:</strong> giảm phụ thuộc vào bản dịch và từ điển. <strong>Linh hoạt hơn:</strong> tóm tắt, paraphrase và dùng lại cấu trúc trong ngữ cảnh mới.</p>
</section>

<section class="sheet toc" id="contents" data-bookmark="Mục lục"><p class="eyebrow">Navigation · Điều hướng</p><h1 class="display">Mục lục</h1>
  <div class="toc-part">HỌC LIỆU NỀN TẢNG</div>
  ${STUDY_MODULES.map((module, index) => `<div class="toc-item"><span class="num">${String(index + 1).padStart(2, '0')}</span><span class="label">${text(module.title)}<small>${text(module.eyebrow.replace(/^\d+ · /, ''))}</small></span><a href="#${module.id}"></a></div>`).join('')}
  <div class="toc-part">VĂN BẢN ĐỐI SÁNH</div>
  ${book.parts.map((part) => `<div class="toc-part">${text(part.part_title_en)}</div>${part.chapters.map((chapter) => `<div class="toc-item"><span class="num">${String(chapter.chapter_index).padStart(2, '0')}</span><span class="label">${text(chapter.study_guide.title.replace(/^Chương \d+(\s*\(Coda\))?:\s*/, ''))}<small>${text(chapter.chapter_title_en)}</small></span><a href="#chapter-${chapter.chapter_index}"></a></div>`).join('')}`).join('')}
  <div class="toc-part">TRA CỨU &amp; KIỂM CHỨNG</div>
  <div class="toc-item"><span class="num">A</span><span class="label">Thuật ngữ Cyberpunk &amp; từ vựng học thuật</span><a href="#glossary"></a></div>
  <div class="toc-item"><span class="num">B</span><span class="label">Phụ lục kiểm tra dữ liệu</span><a href="#audit"></a></div>
</section>

${STUDY_MODULES.map(renderModule).join('\n')}

${book.parts.map((part) => `${renderPart(part, book.parts.indexOf(part))}${part.chapters.map((chapter) => `<article class="chapter" id="chapter-${chapter.chapter_index}" data-bookmark="Chương ${chapter.chapter_index}: ${text(chapter.study_guide.title.replace(/^Chương \d+(\s*\(Coda\))?:\s*/, ''))}">
  <header class="chapter-head" data-running="CHƯƠNG ${chapter.chapter_index}"><div class="chapter-no">${String(chapter.chapter_index).padStart(2, '0')}</div><div><p class="eyebrow">Chapter ${chapter.chapter_index} · ${text(part.part_title_en)}</p><h1>${text(chapter.study_guide.title.replace(/^Chương \d+(\s*\(Coda\))?:\s*/, ''))}</h1><div class="chapter-sub">${text(chapter.chapter_title_en)}</div></div></header>
  <aside class="guide"><h2>Academic masterclass · Định hướng trước khi đọc</h2><p>${text(chapter.study_guide.summary_vi)}</p>
    ${chapter.study_guide.grammar_focus.map((focus) => `<div class="grammar"><strong>${text(focus.rule)}</strong><p>${text(focus.explanation)}</p><p><span class="example-label">Ví dụ học thuật minh họa</span><br><em>${text(focus.example)}</em></p></div>`).join('')}
  </aside>
  <div class="reading-labels"><span>ENGLISH · VĂN BẢN GỐC</span><span>TIẾNG VIỆT · ĐỐI CHIẾU</span></div>
  ${chapter.paragraphs.map((paragraph) => { const isMissing = paragraph.en.trim() === paragraph.vi.trim(); return `<div class="pair${isMissing ? ' missing' : ''}" id="p-${paragraph.id}">
    <p class="pair-text pair-en"><span class="pair-id">${paragraph.id}</span>${text(paragraph.en)}</p>
    <p class="pair-text pair-vi">${isMissing ? '<span class="missing-label">TRÙNG VĂN BẢN NGUỒN · CẦN RÀ SOÁT</span>' : ''}${text(paragraph.vi)}</p>
  </div>`; }).join('\n')}
  <div class="chapter-end">KẾT THÚC CHƯƠNG ${chapter.chapter_index} · ${chapter.paragraphs.length} CẶP ĐOẠN</div>
</article>`).join('')}`).join('\n')}

<section class="sheet glossary-intro" id="glossary" data-bookmark="Phụ lục A: Thuật ngữ"><p class="eyebrow">Appendix A · Reference lexicon</p><h1 class="display">Ngôn ngữ của<br>không gian mạng</h1><p class="lead">${stats.glossaryTerms} mục thuật ngữ kết nối văn chương, công nghệ và từ vựng học thuật. IPA và nhãn cấp độ giữ từ dữ liệu nguồn; nên đối chiếu từ điển khi dùng trong sản xuất ngôn ngữ.</p><div class="rule"></div>
<div class="glossary-grid">${Object.entries(book.glossary).map(([key, entry]) => `<article class="glossary-entry" id="term-${text(key.replace(/\s+/g, '-'))}"><h3>${text(entry.term)}</h3><div class="ipa">${text(entry.ipa)} · ${text(entry.pos)}</div><div class="level">${text(entry.level)}</div><p>${text(entry.definition_en)}</p><p><strong>${text(entry.definition_vi)}</strong></p><p class="note">${text(entry.literary_note)}</p></article>`).join('')}</div></section>

<section class="sheet front" id="audit" data-bookmark="Phụ lục B: Kiểm tra dữ liệu"><p class="eyebrow">Appendix B · Source integrity</p><h1 class="display">Kiểm chứng<br>dữ liệu đầu vào</h1><p class="lead">Quy trình TypeScript đọc trực tiếp <span class="mono">data/bilingual_novel.json</span>, kiểm tra số phần/chương/đoạn và không ghi đè nội dung. Báo cáo máy đọc nằm tại <span class="mono">output/build-report.json</span>.</p>
<div class="notice"><strong>${stats.untranslatedCandidates} đoạn cần rà soát theo ngữ cảnh.</strong> Danh sách dưới đây giúp xử lý minh bạch trong một phiên bản sau. Mã đoạn tương ứng với mã in ở đầu mỗi cặp văn bản.</div>
<div class="audit-list">${missing.map(({ id, chapter }) => `<div>Ch. ${String(chapter).padStart(2, '0')} · ${id}</div>`).join('')}</div>
<div class="rule"></div><h2>Phạm vi biên tập lần này</h2><p>Thiết kế lại ấn bản và pipeline xuất bản; bổ sung module học tập nguyên bản; cải thiện điều hướng, metadata, bookmarks và kiểm thử. Không khẳng định rằng các bản dịch cũ đã được hiệu đính, và không gắn nhãn ví dụ minh họa là trích dẫn nguyên tác.</p></section>

<section class="back-cover"><div class="cover-brand">READ · INFER · COMPARE · CREATE</div><blockquote>Đọc ngôn ngữ.<br>Đối chiếu ý nghĩa.<br>Tạo ra cách diễn đạt<br>của chính bạn.</blockquote><div class="colophon-bottom">NEUROMANCER · BILINGUAL STUDY EDITION<br>TypeScript × Astryx · B2–C1 LANGUAGE LAB</div></section>
</main></body></html>`;
}

async function main(): Promise<void> {
  const book = JSON.parse(await readFile(path.join(root, 'data/bilingual_novel.json'), 'utf8')) as Edition;
  const themePath = require.resolve('@astryxdesign/theme-gothic/theme.css');
  const [themeCss, printCss] = await Promise.all([
    readFile(themePath, 'utf8'),
    readFile(path.join(root, 'src/styles.css'), 'utf8'),
  ]);
  const html = renderBook(book, themeCss, printCss).replace(/[\t ]+$/gm, '');
  const destination = path.join(root, 'data/novel_bilingual.html');
  await writeFile(destination, html);
  console.log(`Rendered ${getBookStats(book).paragraphs} paragraph pairs to ${destination}`);
}

if (process.argv[1] && import.meta.url === new URL(`file://${path.resolve(process.argv[1])}`).href) {
  await main();
}
