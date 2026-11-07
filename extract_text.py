import zipfile
import re
import json
import os

def clean_html_text(raw_html):
    text = re.sub(r'<[^>]+>', '', raw_html)
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;', "'")
    text = text.replace('\xa0', ' ').strip()
    return text

def extract_chapters(epub_path):
    with zipfile.ZipFile(epub_path, 'r') as z:
        ch2_content = z.read('EPUB/text/ch002.xhtml').decode('utf-8')

    tokens = re.split(r'(<h[123][^>]*>.*?</h[123]>)', ch2_content)

    current_part = "PART ONE - CHIBA CITY BLUES"
    current_chapter = None
    chapters = []

    for token in tokens:
        h_match = re.match(r'<h([123])[^>]*>(.*?)</h\1>', token)
        if h_match:
            tag_level, text = h_match.group(1), h_match.group(2)
            cleaned = clean_html_text(text)
            if tag_level in ('1', '2'):
                current_part = cleaned
            elif tag_level == '3':
                chapter_num = int(cleaned.strip())
                current_chapter = {
                    "part": current_part,
                    "chapter_number": chapter_num,
                    "title": f"Chapter {chapter_num}",
                    "paragraphs": []
                }
                chapters.append(current_chapter)
        else:
            if current_chapter is not None:
                paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', token, re.DOTALL)
                for p in paragraphs:
                    cleaned_p = clean_html_text(p)
                    if cleaned_p:
                        current_chapter["paragraphs"].append(cleaned_p)

    return chapters

def main():
    os.makedirs('data', exist_ok=True)
    epub_path = 'neuromancer.epub'
    chapters = extract_chapters(epub_path)
    output_path = os.path.join('data', 'chapters_en.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(chapters)} chapters into {output_path}")

if __name__ == '__main__':
    main()
