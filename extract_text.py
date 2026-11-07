import zipfile
import re
import json

def extract_neuromancer_text(epub_path="neuromancer.epub", output_path="chapters.json"):
    with zipfile.ZipFile(epub_path, 'r') as z:
        raw = z.read('EPUB/text/ch002.xhtml').decode('utf-8')

    items = re.split(r'(<h[1-6][^>]*>.*?</h[1-6]>)', raw)

    chapters = []
    current_part = ""
    current_ch_num = ""

    for item in items:
        h_match = re.match(r'<h([1-6])[^>]*>(.*?)</h[1-6]>', item, re.DOTALL)
        if h_match:
            t = re.sub(r'<[^>]+>', '', h_match.group(2)).strip()
            if 'PART' in t or 'CODA' in t:
                current_part = t
            else:
                current_ch_num = t
                chapters.append({
                    'part': current_part,
                    'chapter': current_ch_num,
                    'paragraphs': []
                })
        else:
            paras = [re.sub(r'<[^>]+>', '', p).strip() for p in re.findall(r'<p[^>]*>(.*?)</p>', item, re.DOTALL)]
            paras = [p for p in paras if p]
            if paras and chapters:
                chapters[-1]['paragraphs'].extend(paras)

    data = {
        'title': 'Neuromancer',
        'author': 'William Gibson',
        'total_chapters': len(chapters),
        'total_paragraphs': sum(len(c['paragraphs']) for c in chapters),
        'chapters': chapters
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Extraction complete! Chapters: {len(chapters)}, Paragraphs: {data['total_paragraphs']}")

if __name__ == "__main__":
    extract_neuromancer_text()
