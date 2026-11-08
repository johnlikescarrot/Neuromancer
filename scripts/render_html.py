import json
import html
from pathlib import Path

def generate_html():
    with open("data/bilingual_novel.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    benchmarks = data["target_benchmarks"]
    glossary = data["glossary"]
    parts = data["parts"]

    html_out = []
    html_out.append("""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Neuromancer - Ấn Bản Song Ngữ Anh - Việt & Cẩm Nang Học Thuật C1/C2</title>
<style>
  @page {
    size: A4;
    margin: 1.8cm 1.5cm 2cm 1.5cm;
    @bottom-center {
      content: counter(page);
      font-size: 9pt;
      color: #666;
      font-family: 'Liberation Sans', sans-serif;
    }
  }

  body {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    color: #1a1a1a;
    line-height: 1.55;
    background: #fff;
    margin: 0;
    padding: 0;
    font-size: 10.5pt;
  }

  /* Cover Page */
  .cover-page {
    page-break-after: always;
    height: 95vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 40px 20px;
    border: 3px double #0d1b2a;
    background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
  }

  .cover-title {
    font-size: 38pt;
    font-weight: 900;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #0b132b;
    margin-bottom: 5px;
    font-family: 'Liberation Serif', serif;
  }

  .cover-sub {
    font-size: 18pt;
    font-weight: 700;
    color: #1c2541;
    margin-bottom: 25px;
    letter-spacing: 1px;
  }

  .cover-author {
    font-size: 16pt;
    font-style: italic;
    color: #3a506b;
    margin-bottom: 40px;
  }

  .cover-desc {
    max-width: 650px;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
    background: #ffffffdd;
    padding: 20px 25px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    margin-bottom: 30px;
  }

  .badge-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 15px;
  }

  .badge {
    background: #0b132b;
    color: #48cae4;
    font-weight: bold;
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 9.5pt;
    border: 1px solid #1c2541;
  }

  /* Academic Intro Page */
  .section-page {
    page-break-before: always;
    page-break-after: always;
  }

  .intro-box {
    background: #f1f5f9;
    border-left: 5px solid #0284c7;
    padding: 16px 20px;
    margin-bottom: 25px;
    border-radius: 0 6px 6px 0;
  }

  .intro-title {
    font-size: 18pt;
    font-weight: bold;
    color: #0f172a;
    margin-top: 0;
    margin-bottom: 12px;
  }

  /* TOC */
  .toc-list {
    list-style: none;
    padding: 0;
    columns: 2;
    column-gap: 30px;
  }

  .toc-item {
    margin-bottom: 10px;
    font-size: 10pt;
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
    background: #0f172a;
    color: #fff;
    padding: 30px 20px;
    text-align: center;
    border-radius: 6px;
    margin-bottom: 25px;
  }

  .part-title-en {
    font-size: 18pt;
    letter-spacing: 2px;
    font-weight: 800;
    color: #38bdf8;
    margin: 0 0 8px 0;
  }

  .part-title-vi {
    font-size: 14pt;
    font-weight: 500;
    color: #e2e8f0;
    margin: 0;
  }

  /* Chapter Header */
  .chapter-container {
    margin-bottom: 35px;
    page-break-inside: auto;
  }

  .chapter-header {
    background: #f8fafc;
    border-bottom: 2px solid #cbd5e1;
    padding: 14px 18px;
    margin-top: 30px;
    margin-bottom: 20px;
    border-left: 6px solid #2563eb;
    page-break-after: avoid;
  }

  .chap-title-en {
    font-size: 16pt;
    font-weight: bold;
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
    background: #fdfbf7;
    border: 1px solid #fed7aa;
    border-left: 5px solid #f97316;
    padding: 14px 18px;
    margin-bottom: 22px;
    border-radius: 4px;
    page-break-inside: avoid;
  }

  .study-title {
    font-size: 11pt;
    font-weight: bold;
    color: #9a3412;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 0;
    margin-bottom: 8px;
  }

  .study-summary {
    font-size: 9.8pt;
    color: #334155;
    margin-bottom: 12px;
    line-height: 1.5;
  }

  .grammar-item {
    background: #fff;
    border: 1px solid #e2e8f0;
    padding: 8px 12px;
    margin-bottom: 8px;
    border-radius: 4px;
    font-size: 9.3pt;
  }

  .grammar-name {
    font-weight: bold;
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
    padding: 8px 12px;
    border-left: 2px solid #94a3b8;
    font-size: 9.8pt;
    text-align: justify;
    line-height: 1.55;
    color: #0f172a;
  }

  .col-vi {
    flex: 1;
    background: #f8fafc;
    padding: 8px 12px;
    border-left: 2px solid #3b82f6;
    font-size: 9.8pt;
    text-align: justify;
    line-height: 1.55;
    color: #1e293b;
  }

  .vocab-pill {
    background: #dbeafe;
    color: #1d4ed8;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 8.5pt;
    font-weight: bold;
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
    color: #fff;
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
""")

    # Cover Page
    html_out.append(f"""
<div class="cover-page">
  <div class="cover-title">NEUROMANCER</div>
  <div class="cover-sub">ẤN BẢN SONG NGỮ ANH - VIỆT TOÀN DIỆN &amp; HỌC THUẬT CAO CẤP</div>
  <div class="cover-author">Tác giả: William Gibson • Bản dịch song song &amp; Khảo cứu học thuật</div>
  <div class="cover-desc">
    Tác phẩm kinh điển khai sinh thể loại Cyberpunk, đạt cú đúp ba giải thưởng danh giá bậc nhất thế giới khoa học viễn tưởng (Hugo, Nebula, Philip K. Dick).
    <br><br>
    Được thiết kế và biên soạn đặc thù nhằm nâng tầm năng lực đọc hiểu văn chương học thuật đỉnh cao, phục vụ người học chinh phục các mốc điểm chuẩn quốc tế danh giá nhất:
    <div class="badge-container">
      <div class="badge">IELTS {benchmarks['IELTS']}</div>
      <div class="badge">TOEFL iBT {benchmarks['TOEFL_iBT']}</div>
      <div class="badge">Cambridge C1/C2 {benchmarks['Cambridge']}</div>
      <div class="badge">PTE Academic {benchmarks['PTE_Academic']}</div>
      <div class="badge">DET {benchmarks['DET']}</div>
    </div>
  </div>
  <div style="font-size: 9pt; color: #64748b; margin-top: 15px;">
    Toàn văn 24 chương nguyên tác &amp; bản dịch đối sánh câu-đoạn • Tuyển tập chú giải ngữ pháp &amp; từ điển chuyên ngành
  </div>
</div>
""")

    # Table of Contents & Study Orientation Page
    html_out.append("""
<div class="section-page">
  <div class="intro-box">
    <div class="intro-title">MỤC LỤC &amp; HƯỚNG DẪN PHƯƠNG PHÁP HỌC SONG NGỮ HỌC THUẬT</div>
    <p>
      Cuốn sách này áp dụng phương pháp <strong>Dual-Language Synoptic Reading (Đọc đối sánh song song)</strong>, một trong những kỹ thuật học ngôn ngữ đỉnh cao nhất dành cho trình độ Advanced (C1) và Mastery (C2). Người học nên đọc đoạn văn bản gốc tiếng Anh ở cột trái trước, cảm nhận nghệ thuật miêu tả, cấu trúc ngữ pháp và sắc thái từ vựng; sau đó đối chiếu với cột tiếng Việt ở bên phải để thấu suốt ngữ nghĩa và nghệ thuật chuyển ngữ.
    </p>
    <p>
      Mỗi chương đều được trang bị phần <strong>Chapter Academic Masterclass</strong>, tổng hợp các kiến thức ngữ pháp tinh hoa (đảo ngữ, câu tuyệt đối, cú pháp tích lũy) thường xuất hiện trong các đề thi IELTS Reading/Writing Band 8.0+, TOEFL 100+ và Cambridge C2 Proficiency (CPE).
    </p>
  </div>

  <h3 style="color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 6px; margin-top: 20px;">DANH MỤC CÁC PHẦN VÀ CHƯƠNG</h3>
  <ul class="toc-list">
""")

    for part in parts:
        for chap in part["chapters"]:
            html_out.append(f"""
    <li class="toc-item">
      <a class="toc-link" href="#chap-{chap['chapter_index']}">Chương {chap['chapter_index']}: {chap['chapter_title_vi']}</a>
      <br><span style="font-size: 8.5pt; color: #64748b;">Part: {part['part_title_en']}</span>
    </li>
""")

    html_out.append("""
  </ul>
</div>
""")

    # Cyberpunk & C1/C2 Vocabulary Glossary Section
    html_out.append("""
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
""")

    for key, v in glossary.items():
        html_out.append(f"""
      <tr>
        <td><strong>{html.escape(v['term'])}</strong><br><span style="color:#64748b; font-family: monospace;">{html.escape(v['ipa'])}</span> ({v['pos']})</td>
        <td><span class="vocab-pill">{v['level']}</span></td>
        <td>{html.escape(v['definition_en'])}</td>
        <td><strong>{html.escape(v['definition_vi'])}</strong><br><span style="font-size: 8.5pt; color: #475569;">{html.escape(v['literary_note'])}</span></td>
      </tr>
""")

    html_out.append("""
    </tbody>
  </table>
</div>
""")

    # Parts and Chapters Content
    for part in parts:
        html_out.append(f"""
<div class="part-header">
  <div class="part-title-en">{html.escape(part['part_title_en'])}</div>
  <div class="part-title-vi">{html.escape(part['part_title_vi'])}</div>
</div>
""")

        for chap in part["chapters"]:
            guide = chap.get("study_guide", {})
            html_out.append(f"""
<div class="chapter-container" id="chap-{chap['chapter_index']}">
  <div class="chapter-header">
    <div class="chap-title-en">CHAPTER {chap['chapter_index']}: {html.escape(chap['chapter_title_en'])}</div>
    <div class="chap-title-vi">{html.escape(chap['chapter_title_vi'])}</div>
  </div>
""")

            if guide and "summary_vi" in guide:
                html_out.append(f"""
  <div class="study-guide-card">
    <div class="study-title">TỔNG QUAN NỘI DUNG &amp; PHÂN TÍCH HỌC THUẬT (C1/C2 ACADEMIC GUIDE)</div>
    <div class="study-summary">{html.escape(guide['summary_vi'])}</div>
""")
                if "grammar_focus" in guide and guide["grammar_focus"]:
                    html_out.append("""<div style="font-weight: bold; color: #1e3a8a; font-size: 9.3pt; margin-bottom: 6px;">CẤU TRÚC NGỮ PHÁP TIÊU BIỂU:</div>""")
                    for gf in guide["grammar_focus"]:
                        html_out.append(f"""
    <div class="grammar-item">
      <div class="grammar-name">• {html.escape(gf['rule'])}: <span style="font-weight: normal; color: #334155;">{html.escape(gf['explanation'])}</span></div>
      <div class="grammar-eg">Ví dụ nguyên tác: "{html.escape(gf['example'])}"</div>
    </div>
""")
                html_out.append("""</div>""")

            # Render bilingual paragraphs
            for p in chap["paragraphs"]:
                p_en_escaped = html.escape(p["en"])
                p_vi_escaped = html.escape(p["vi"])

                html_out.append(f"""
  <div class="bilingual-pair">
    <div class="col-en">{p_en_escaped}</div>
    <div class="col-vi">{p_vi_escaped}</div>
  </div>
""")

            html_out.append("""</div>""")

    html_out.append("""
</body>
</html>
""")

    output_html_path = Path("data/novel_bilingual.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html_out))

    print(f"Generated HTML successfully: {output_html_path} (size: {output_html_path.stat().st_size / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    generate_html()
