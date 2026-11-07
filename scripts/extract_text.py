import zipfile
import re
import html
import json
import os

def clean_html(raw_html):
    clean = re.sub(r'<[^<]+?>', '', raw_html)
    return html.unescape(clean).strip()

def extract_epub(epub_path):
    z = zipfile.ZipFile(epub_path)
    text = z.read('EPUB/text/ch002.xhtml').decode('utf-8')

    parts_and_chapters = []

    # Matches h1, h2, h3
    header_regex = re.compile(r'<h([1-3])\s+[^>]*data-number="([^"]+)"[^>]*>(.*?)</h\1>', re.DOTALL)
    headers = list(header_regex.finditer(text))

    current_part = "UNKNOWN"

    for i, match in enumerate(headers):
        level = int(match.group(1))
        data_num = match.group(2)
        title = clean_html(match.group(3))

        start_pos = match.end()
        end_pos = headers[i+1].start() if i + 1 < len(headers) else len(text)

        content_slice = text[start_pos:end_pos]
        paras = re.findall(r'<p[^>]*>(.*?)</p>', content_slice, re.DOTALL)
        clean_paras = [clean_html(p) for p in paras if clean_html(p)]

        if level in (1, 2) and ("PART" in title.upper() or "CODA" in title.upper()):
            current_part = title
            if clean_paras:
                parts_and_chapters.append({
                    "type": "part_intro",
                    "part": current_part,
                    "title": title,
                    "data_number": data_num,
                    "paragraphs": clean_paras
                })
        elif level == 3:
            parts_and_chapters.append({
                "type": "chapter",
                "part": current_part,
                "chapter": title,
                "data_number": data_num,
                "paragraphs": clean_paras
            })

    return parts_and_chapters

def main():
    epub_path = 'neuromancer.epub'
    chapters = extract_epub(epub_path)

    os.makedirs('data', exist_ok=True)
    with open('data/chapters.json', 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(chapters)} entries into data/chapters.json")

    # Initialize glossary framework with target benchmarks
    glossary_meta = {
        "benchmarks": {
            "TOEFL": "90 (prior to Jan 21, 2026) / 5 (from Jan 21, 2026 onwards)",
            "IELTS": "7.0 (Good user / operational command)",
            "PTE_Academic": "65",
            "Cambridge": "185 (C1 Advanced / C2 Proficiency)",
            "Duolingo_DET": "120"
        },
        "target_audience": "Advanced English Learners & Cyberpunk Connoisseurs",
        "entries": {}
    }
    with open('data/glossary.json', 'w', encoding='utf-8') as f:
        json.dump(glossary_meta, f, ensure_ascii=False, indent=2)
    print("Initialized data/glossary.json")

if __name__ == '__main__':
    main()
