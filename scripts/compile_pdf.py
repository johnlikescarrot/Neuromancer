import argparse
import asyncio
import os
import json
from playwright.async_api import async_playwright

def generate_sample_html():
    with open('templates/book_template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    sample_content = """
    <div class="chapter-header">
      <div class="chapter-title">SAMPLE CHAPTER / CHƯƠNG MẪU</div>
      <div class="chapter-sub">Demonstration of Bilingual Parallel Layout & Exam Notes</div>
    </div>

    <div class="parallel-row">
      <div class="col-en">
        The sky above the port was the color of television, tuned to a dead channel.
      </div>
      <div class="col-vi">
        Bầu trời phía trên bến cảng mang màu của một màn hình tivi bắt trúng kênh tín hiệu chết.
      </div>
    </div>

    <div class="vocab-box">
      <div class="vocab-title">📚 ACADEMIC & EXAM VOCABULARY FOCUS (C1/C2 - IELTS 7.0+ - TOEFL 90/5)</div>
      <div class="vocab-item">
        <span class="vocab-exam-tag">C1 ADVANCED</span>
        <span class="vocab-word">tuned to</span> <span class="vocab-phonetic">/tjuːnd tuː/</span>:
        <span class="vocab-def">adjusted to receive a particular frequency or channel.</span>
        — <span class="vocab-trans">điều chỉnh vào kênh/tần số.</span>
      </div>
      <div class="vocab-item">
        <span class="vocab-exam-tag">C2 PROFICIENCY</span>
        <span class="vocab-word">dead channel</span> <span class="vocab-phonetic">/dɛd ˈtʃænəl/</span>:
        <span class="vocab-def">a broadcast channel with only static noise (white noise/snow).</span>
        — <span class="vocab-trans">kênh tín hiệu nhiễu trắng tĩnh điện.</span>
      </div>
    </div>
    """

    html = template.replace('{{ title }}', 'Neuromancer - Sample Bilingual Edition')
    html = html.replace('{{ content }}', sample_content)
    return html

async def render_pdf(html_path, output_pdf_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Convert path to absolute file url
        abs_html_path = os.path.abspath(html_path)
        await page.goto(f"file://{abs_html_path}", wait_until="networkidle")
        await page.pdf(
            path=output_pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"}
        )
        await browser.close()
        print(f"PDF successfully rendered to {output_pdf_path}")

def build_full_html():
    with open('templates/book_template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    content_parts = []

    # Load available chapter translations from content/
    chapter_files = sorted([f for f in os.listdir('content') if f.endswith('.json')])
    for cf in chapter_files:
        with open(os.path.join('content', cf), 'r', encoding='utf-8') as f:
            ch_data = json.load(f)

        part_title = ch_data.get('part', '')
        part_vi = ch_data.get('part_vi', '')
        if part_title and ch_data.get('is_first_of_part', False):
            content_parts.append(f"""
            <div class="section-part-header">
              <div class="section-part-title">{part_title}</div>
              <div class="section-part-vi">{part_vi}</div>
            </div>
            """)

        ch_title = ch_data.get('chapter', '')
        ch_title_vi = ch_data.get('chapter_vi', '')
        content_parts.append(f"""
        <div class="chapter-header">
          <div class="chapter-title">{ch_title}</div>
          <div class="chapter-sub">{ch_title_vi}</div>
        </div>
        """)

        # Paragraphs and study notes
        for section in ch_data.get('sections', []):
            if section.get('type') == 'parallel':
                content_parts.append(f"""
                <div class="parallel-row">
                  <div class="col-en">{section.get('en', '')}</div>
                  <div class="col-vi">{section.get('vi', '')}</div>
                </div>
                """)
            elif section.get('type') == 'vocab':
                items_html = ""
                for v in section.get('items', []):
                    items_html += f"""
                    <div class="vocab-item">
                      <span class="vocab-exam-tag">{v.get('level', 'C1/IELTS 7.0')}</span>
                      <span class="vocab-word">{v.get('word', '')}</span>
                      <span class="vocab-phonetic">{v.get('ipa', '')}</span>:
                      <span class="vocab-def">{v.get('en_def', '')}</span>
                      — <span class="vocab-trans">{v.get('vi_def', '')}</span>
                    </div>
                    """
                content_parts.append(f"""
                <div class="vocab-box">
                  <div class="vocab-title">📚 {section.get('title', 'KEY VOCABULARY & GRAMMAR NOTE')}</div>
                  {items_html}
                </div>
                """)
            elif section.get('type') == 'note':
                content_parts.append(f"""
                <div class="cultural-note">
                  <div class="cultural-note-title">💡 {section.get('title', 'BỐI CẢNH & THUẬT NGỮ CYBERPUNK')}</div>
                  <div>{section.get('content', '')}</div>
                </div>
                """)

    full_content = "\n".join(content_parts)
    html = template.replace('{{ title }}', 'William Gibson - Neuromancer (Bilingual Edition)')
    html = html.replace('{{ content }}', full_content)
    return html

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample', action='store_true', help='Render sample PDF')
    parser.add_argument('--output', default='Neuromancer_Bilingual_Edition.pdf', help='Output PDF filename')
    args = parser.parse_args()

    os.makedirs('build', exist_ok=True)

    if args.sample:
        html = generate_sample_html()
        html_file = 'build/sample.html'
        pdf_file = 'build/sample.pdf'
    else:
        html = build_full_html()
        html_file = 'build/full_book.html'
        pdf_file = args.output

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    # Copy book_style.css into build
    import shutil
    shutil.copy('templates/book_style.css', 'build/book_style.css')

    asyncio.run(render_pdf(html_file, pdf_file))

if __name__ == '__main__':
    main()
