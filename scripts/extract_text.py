import zipfile
import re
import json
import html

def extract_chapters_from_epub(epub_path):
    z = zipfile.ZipFile(epub_path)
    ch2_html = z.read('EPUB/text/ch002.xhtml').decode('utf-8')

    # Pattern to match sections and headers
    # The epub structure has h1 for Parts and h3 for Chapter numbers
    # e.g.:
    # <h1 data-number="1">PART ONE - CHIBA CITY BLUES</h1>
    # <h3 data-number="1.0.1">1</h3>

    tokens = re.split(r'(<h[1-6][^>]*>.*?</h[1-6]>)', ch2_html)

    structure = []
    current_part = "PROLOGUE"
    current_chapter = None

    for token in tokens:
        header_match = re.match(r'<h([1-6])[^>]*>(.*?)</h\1>', token, re.DOTALL)
        if header_match:
            level = header_match.group(1)
            title = header_match.group(2).strip()
            if "PART" in title or "CODA" in title:
                current_part = title
            else:
                current_chapter = {
                    "part": current_part,
                    "chapter_title": title,
                    "paragraphs": []
                }
                structure.append(current_chapter)
        else:
            if current_chapter is not None:
                # Extract all <p>...</p> tags
                raw_paras = re.findall(r'<p[^>]*>(.*?)</p>', token, re.DOTALL)
                for p in raw_paras:
                    # Clean tags inside paragraph
                    clean_p = re.sub(r'<[^>]+>', '', p)
                    clean_p = html.unescape(clean_p).strip()
                    if clean_p and not re.match(r'^\s*<span[^>]*>\s*</span>\s*$', clean_p):
                        # Filter out empty spans or solitary page/anchor marks
                        if clean_p:
                            current_chapter["paragraphs"].append(clean_p)

    return structure

if __name__ == '__main__':
    chapters = extract_chapters_from_epub('neuromancer.epub')
    print(f"Extracted {len(chapters)} chapters.")
    total_p = sum(len(c['paragraphs']) for c in chapters)
    print(f"Total paragraphs: {total_p}")
    with open('data/chapters.json', 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    print("Saved to data/chapters.json successfully.")
