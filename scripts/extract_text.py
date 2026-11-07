import zipfile
import re
import json
import os

def clean_html(text):
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&mdash;', '—')
    text = text.replace('&quot;', '"')
    text = text.replace('&ldquo;', '“')
    text = text.replace('&rdquo;', '”')
    text = text.replace('&lsquo;', '‘')
    text = text.replace('&rsquo;', '’')
    text = text.replace('&hellip;', '…')
    text = text.replace('&amp;', '&')
    lines = [l.strip() for l in text.split('\n')]
    return [l for l in lines if l]

def extract():
    epub_path = 'neuromancer.epub'
    if not os.path.exists(epub_path):
        raise FileNotFoundError(f"{epub_path} not found")

    with zipfile.ZipFile(epub_path) as z:
        raw_html = z.read('EPUB/text/ch002.xhtml').decode('utf-8')

    sections = re.split(r'(<h[1-6][^>]*>.*?</h[1-6]>)', raw_html)

    parts_meta = {
        'PART ONE - CHIBA CITY BLUES': {'part': 1, 'title_en': 'PART ONE - CHIBA CITY BLUES', 'title_vi': 'PHẦN MỘT - CHIBA CITY BLUES'},
        'PART TWO - THE SHOPPING EXPEDITION': {'part': 2, 'title_en': 'PART TWO - THE SHOPPING EXPEDITION', 'title_vi': 'PHẦN HAI - CUỘC SẮM SỬA VŨ TRANG'},
        'PART THREE - MIDNIGHT IN THE RUE JULES VERNE': {'part': 3, 'title_en': 'PART THREE - MIDNIGHT IN THE RUE JULES VERNE', 'title_vi': 'PHẦN BA - NỬA ĐÊM Ở PHỐ JULES VERNE'},
        'PART FOUR - THE STRAYLIGHT RUN': {'part': 4, 'title_en': 'PART FOUR - THE STRAYLIGHT RUN', 'title_vi': 'PHẦN BỐN - ĐỘT NHẬP STRAYLIGHT'},
        'CODA - DEPARTURE AND ARRIVAL': {'part': 5, 'title_en': 'CODA - DEPARTURE AND ARRIVAL', 'title_vi': 'VĨ THANH - RA ĐI VÀ HỒI HƯỚNG'}
    }

    current_part = parts_meta['PART ONE - CHIBA CITY BLUES']
    chapters = []
    current_ch = None

    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        h_match = re.search(r'<h([1-6])[^>]*>(.*?)</h\1>', sec)
        if h_match:
            heading_text = h_match.group(2).strip()
            if heading_text in parts_meta:
                current_part = parts_meta[heading_text]
            elif heading_text.isdigit():
                ch_num = int(heading_text)
                if current_ch:
                    chapters.append(current_ch)
                current_ch = {
                    'chapter_num': ch_num,
                    'part_num': current_part['part'],
                    'part_title_en': current_part['title_en'],
                    'part_title_vi': current_part['title_vi'],
                    'paragraphs': []
                }
        else:
            if current_ch is not None:
                paras = clean_html(sec)
                current_ch['paragraphs'].extend(paras)

    if current_ch:
        chapters.append(current_ch)

    out_dir = 'data/chapters'
    os.makedirs(out_dir, exist_ok=True)
    summary = []
    for ch in chapters:
        ch_file = os.path.join(out_dir, f"chapter_{ch['chapter_num']:02d}.json")
        with open(ch_file, 'w', encoding='utf-8') as f:
            json.dump(ch, f, ensure_ascii=False, indent=2)
        summary.append({
            'chapter': ch['chapter_num'],
            'part': ch['part_num'],
            'paragraphs_count': len(ch['paragraphs']),
            'word_count': sum(len(p.split()) for p in ch['paragraphs'])
        })

    with open('data/chapters_manifest.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(chapters)} chapters successfully.")

if __name__ == '__main__':
    extract()
