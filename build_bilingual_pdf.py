import json
import os
import sys
from playwright.sync_api import sync_playwright

def generate_bilingual_html(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        chapters = json.load(f)

    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>Neuromancer - Ấn bản Song ngữ Anh - Việt Toàn diện</title>
<style>
  @page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {
      content: counter(page);
      font-size: 9pt;
      font-family: 'Times New Roman', serif;
      color: #666;
    }
  }

  body {
    font-family: 'Times New Roman', 'Liberation Serif', serif;
    line-height: 1.5;
    color: #1a1a1a;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }

  .cover-page {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 90vh;
    border: 3px double #0d3b66;
    padding: 40px;
    box-sizing: border-box;
  }

  .cover-title-en {
    font-size: 38pt;
    font-weight: 800;
    letter-spacing: 4px;
    color: #0d3b66;
    margin-bottom: 5px;
    text-transform: uppercase;
  }

  .cover-title-vi {
    font-size: 24pt;
    font-weight: 600;
    color: #b84a39;
    margin-bottom: 25px;
    letter-spacing: 1px;
  }

  .cover-author {
    font-size: 18pt;
    font-style: italic;
    color: #333333;
    margin-bottom: 35px;
  }

  .cover-edition {
    font-size: 13pt;
    font-weight: bold;
    color: #1e3d59;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    border-top: 2px solid #0d3b66;
    border-bottom: 2px solid #0d3b66;
    padding: 10px 25px;
    margin-bottom: 30px;
  }

  .cover-targets {
    background-color: #f7f9fa;
    border-left: 4px solid #0d3b66;
    padding: 15px 25px;
    text-align: left;
    max-width: 550px;
    font-size: 10pt;
    color: #2b2d42;
    line-height: 1.6;
    margin-bottom: 30px;
  }

  .cover-targets h4 {
    margin: 0 0 8px 0;
    font-size: 11pt;
    color: #0d3b66;
    text-transform: uppercase;
  }

  .cover-targets ul {
    margin: 0;
    padding-left: 20px;
  }

  .preface-page {
    page-break-after: always;
    padding: 20px 10px;
  }

  .preface-page h2 {
    font-size: 20pt;
    color: #0d3b66;
    text-align: center;
    border-bottom: 1.5px solid #0d3b66;
    padding-bottom: 8px;
    margin-bottom: 20px;
  }

  .preface-page p {
    font-size: 11pt;
    text-align: justify;
    line-height: 1.6;
    margin-bottom: 14px;
  }

  .toc-page {
    page-break-after: always;
    padding: 20px 10px;
  }

  .toc-page h2 {
    font-size: 20pt;
    color: #0d3b66;
    text-align: center;
    border-bottom: 1.5px solid #0d3b66;
    padding-bottom: 8px;
    margin-bottom: 25px;
  }

  .toc-part-title {
    font-size: 12pt;
    font-weight: bold;
    color: #b84a39;
    margin-top: 15px;
    margin-bottom: 6px;
    border-bottom: 1px dashed #bbb;
    padding-bottom: 3px;
  }

  .toc-chapter-item {
    font-size: 10.5pt;
    margin-left: 15px;
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
  }

  .part-divider {
    page-break-before: always;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 80vh;
  }

  .part-divider h1 {
    font-size: 26pt;
    color: #0d3b66;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
  }

  .part-divider h2 {
    font-size: 18pt;
    color: #b84a39;
    font-weight: 500;
  }

  .chapter-block {
    page-break-before: always;
    margin-top: 15px;
  }

  .chapter-header {
    text-align: center;
    margin-bottom: 25px;
    border-bottom: 2px solid #eaeaea;
    padding-bottom: 15px;
  }

  .chapter-header h2 {
    font-size: 20pt;
    color: #0d3b66;
    margin: 0;
  }

  .chapter-header h3 {
    font-size: 14pt;
    color: #666;
    margin: 5px 0 0 0;
    font-weight: normal;
  }

  .pedagogy-box {
    background-color: #f4f6f8;
    border: 1px solid #d3d9de;
    border-left: 5px solid #0d3b66;
    border-radius: 4px;
    padding: 14px 18px;
    margin-bottom: 25px;
    font-size: 9.5pt;
  }

  .pedagogy-title {
    font-weight: bold;
    color: #0d3b66;
    font-size: 11pt;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .vocab-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 12px;
  }

  .vocab-item {
    background-color: #ffffff;
    border: 1px solid #e1e4e8;
    border-radius: 3px;
    padding: 8px 10px;
    line-height: 1.4;
  }

  .vocab-word {
    font-weight: bold;
    color: #0d3b66;
    font-size: 10pt;
  }

  .vocab-ipa {
    font-family: monospace;
    color: #555;
    font-size: 8.5pt;
  }

  .vocab-badge {
    background-color: #e2f0d9;
    color: #276738;
    padding: 1px 4px;
    border-radius: 2px;
    font-size: 7.5pt;
    font-weight: bold;
    margin-left: 4px;
  }

  .grammar-box {
    background-color: #fffaf0;
    border: 1px solid #f2e2c4;
    border-left: 3px solid #d48b0c;
    padding: 8px 12px;
    border-radius: 3px;
    margin-top: 8px;
  }

  .grammar-title {
    font-weight: bold;
    color: #b45309;
    font-size: 9.5pt;
  }

  .parallel-row {
    display: flex;
    flex-direction: row;
    gap: 18px;
    margin-bottom: 16px;
    page-break-inside: avoid;
  }

  .parallel-col-en {
    flex: 1;
    text-align: justify;
    font-size: 10pt;
    line-height: 1.55;
    color: #111111;
  }

  .parallel-col-vi {
    flex: 1;
    text-align: justify;
    font-size: 10pt;
    line-height: 1.55;
    color: #2b3a42;
    background-color: #fafbfc;
    padding: 0 8px;
    border-left: 1.5px solid #e0e5ea;
  }
</style>
</head>
<body>
""")

    # Cover Page
    html_parts.append("""
<div class="cover-page">
  <div class="cover-title-en">NEUROMANCER</div>
  <div class="cover-title-vi">CÔI CHÂU THẦN KINH</div>
  <div class="cover-author">William Gibson</div>
  <div class="cover-edition">Ấn bản Song ngữ Anh - Việt Toàn Diện & Chuẩn Mực Học Thuật Cao Cấp</div>
  <div class="cover-targets">
    <h4>Được biên soạn đáp ứng các chuẩn năng lực khảo thí quốc tế:</h4>
    <ul>
      <li><strong>IELTS:</strong> Chuẩn Band 7.0 - 8.5 (Academic & General Training)</li>
      <li><strong>TOEFL iBT:</strong> Chuẩn 90 - 110 điểm (hoặc 5+ điểm thang đo từ 21/01/2026)</li>
      <li><strong>PTE Academic:</strong> Chuẩn 65 - 85 điểm</li>
      <li><strong>Cambridge English:</strong> C1 Advanced & C2 Proficiency (185 - 210 điểm)</li>
      <li><strong>Duolingo English Test (DET):</strong> Chuẩn 120 - 145 điểm</li>
    </ul>
  </div>
  <div style="font-size: 9.5pt; color: #777;">
    Toàn bộ 24 chương tác phẩm kinh điển Cyberpunk | Phân tích từ vựng C1/C2, cụm từ học thuật, ngữ pháp nâng cao và đối chiếu song song
  </div>
</div>
""")

    # Preface Page
    html_parts.append("""
<div class="preface-page">
  <h2>LỜI NÓI ĐẦU CHO ẤN BẢN SONG NGỮ HỌC THUẬT</h2>
  <p>
    <em>Neuromancer</em> (1984) của William Gibson không chỉ là kiệt tác đặt nền móng cho thể loại văn học viễn tưởng không gian mạng (Cyberpunk) mà còn là một kho tàng ngôn ngữ Anh ngữ đỉnh cao với hệ thống thuật ngữ tân tiến, phong cách văn xuôi sắc bén, cấu trúc câu phức tạp và tính biểu cảm giác quan mạnh mẽ.
  </p>
  <p>
    Nhằm tạo nên một ấn bản song ngữ Anh - Việt chuẩn mực và toàn diện nhất từ trước tới nay, công trình này được thiết kế theo phương pháp đối chiếu song song hai cột (Parallel Dual-Column Layout) kết hợp hệ thống chú giải học thuật chuyên sâu (Pedagogical Framework). Mỗi chương mở đầu với bảng phân tích từ vựng cao cấp bậc C1/C2, ngữ âm quốc tế IPA, kết hợp từ (collocations), ngữ cảnh văn chương và các cấu trúc ngữ pháp trọng điểm thường xuất hiện trong các bài thi chuẩn hóa quốc tế như IELTS (7.0+), TOEFL iBT (90+ / 5+), Pearson PTE Academic (65+), Cambridge C1/C2 (185+) và Duolingo English Test (120+).
  </p>
  <p>
    Bản dịch tiếng Việt được hiệu đính công phu, đảm bảo độ chuẩn xác về ngữ nghĩa kỹ thuật số và bảo toàn trọn vẹn văn phong u tối, sắc lạnh, đầy tính thơ nhưng giàu chất hiện thực của nguyên tác. Đây là tài liệu vừa đáp ứng nhu cầu thưởng thức văn chương đỉnh cao, vừa là công cụ trau dồi năng lực ngôn ngữ thực chiến cho người học trình độ cao cấp.
  </p>
</div>
""")

    # Table of Contents
    html_parts.append("""
<div class="toc-page">
  <h2>MỤC LỤC / TABLE OF CONTENTS</h2>
""")
    current_part = None
    for ch in chapters:
        if ch["part_en"] != current_part:
            current_part = ch["part_en"]
            html_parts.append(f"""
  <div class="toc-part-title">{ch['part_en']} / {ch['part_vi']}</div>
""")
        html_parts.append(f"""
  <div class="toc-chapter-item">
    <span><strong>{ch['title_en']}</strong>: {ch['title_vi']}</span>
    <span>{ch['paragraph_count']} đoạn</span>
  </div>
""")
    html_parts.append("""
</div>
""")

    # Chapters Content
    current_part = None
    for ch in chapters:
        if ch["part_en"] != current_part:
            current_part = ch["part_en"]
            html_parts.append(f"""
<div class="part-divider">
  <h1>{ch['part_en']}</h1>
  <h2>{ch['part_vi']}</h2>
</div>
""")

        html_parts.append(f"""
<div class="chapter-block">
  <div class="chapter-header">
    <h2>{ch['title_en']}</h2>
    <h3>{ch['title_vi']}</h3>
  </div>
""")

        # Pedagogical section
        ped = ch.get("pedagogical_notes", {})
        vocab_list = ped.get("vocabulary", [])
        grammar_focus = ped.get("grammar_focus", None)

        if vocab_list or grammar_focus:
            html_parts.append("""
  <div class="pedagogy-box">
    <div class="pedagogy-title">Khảo cứu Ngôn ngữ Học thuật (C1/C2 Academic Enrichment)</div>
""")
            if vocab_list:
                html_parts.append("""
    <div class="vocab-grid">
""")
                for v in vocab_list:
                    html_parts.append(f"""
      <div class="vocab-item">
        <span class="vocab-word">{v['word']}</span> <span class="vocab-ipa">{v['ipa']}</span> <span class="vocab-badge">{v['level']}</span><br/>
        <strong>Định nghĩa:</strong> {v['meaning_vi']}<br/>
        <strong>Collocation:</strong> <em>{v['collocation']}</em><br/>
        <strong>Ví dụ:</strong> {v['sample']}
      </div>
""")
                html_parts.append("""
    </div>
""")

            if grammar_focus:
                html_parts.append(f"""
    <div class="grammar-box">
      <div class="grammar-title">Tiêu điểm Ngữ pháp Nâng cao: {grammar_focus['pattern']}</div>
      <div><strong>Phân tích:</strong> {grammar_focus['explanation']}</div>
      <div><strong>Minh họa tác phẩm:</strong> <em>{grammar_focus['example']}</em></div>
      <div><strong>Chiến lược phòng thi:</strong> {grammar_focus['exam_tip']}</div>
    </div>
""")

            html_parts.append("""
  </div>
""")

        # Paragraphs side by side
        for p in ch["paragraphs"]:
            p_en = p["en"].replace("\n", " ")
            p_vi = p["vi"].replace("\n", " ")
            html_parts.append(f"""
  <div class="parallel-row">
    <div class="parallel-col-en">{p_en}</div>
    <div class="parallel-col-vi">{p_vi}</div>
  </div>
""")

        html_parts.append("""
</div>
""")

    html_parts.append("""
</body>
</html>
""")

    full_html = "\n".join(html_parts)
    return full_html

def compile_pdf(input_json, output_pdf):
    print("Generating HTML bilingual markup...")
    html_content = generate_bilingual_html(input_json)
    temp_html_path = 'data/temp_bilingual.html'
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"HTML generated ({len(html_content)} chars). Compiling PDF with Playwright Chromium...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath(temp_html_path)}", wait_until='networkidle')
        page.pdf(
            path=output_pdf,
            format='A4',
            print_background=True,
            margin={
                'top': '20mm',
                'bottom': '20mm',
                'left': '15mm',
                'right': '15mm'
            }
        )
        browser.close()

    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
    print(f"Compilation finished successfully: {output_pdf}")

def main():
    json_path = os.path.join('data', 'bilingual_neuromancer.json')
    output_pdf = 'neuromancer_bilingual_en_vi.pdf'
    compile_pdf(json_path, output_pdf)

if __name__ == '__main__':
    main()
