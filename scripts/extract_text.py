import zipfile
import json
import xml.etree.ElementTree as ET
import re

def clean_text(text):
    if not text:
        return ""
    # normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_content(epub_path):
    with zipfile.ZipFile(epub_path, 'r') as z:
        # Title and dedication
        ch1_xml = z.read('EPUB/text/ch001.xhtml').decode('utf-8')
        ch2_xml = z.read('EPUB/text/ch002.xhtml').decode('utf-8')

    root = ET.fromstring(ch2_xml)

    parts = []
    current_part = {
        'title': 'PART ONE - CHIBA CITY BLUES',
        'chapters': []
    }

    current_chapter = None

    for elem in root.iter():
        tag = elem.tag.split('}')[-1]
        text = clean_text(''.join(elem.itertext()))

        if tag in ['h1', 'h2']:
            if 'PART' in text or 'CODA' in text:
                if current_chapter is not None and current_part is not None:
                    if current_chapter not in current_part['chapters']:
                        current_part['chapters'].append(current_chapter)
                    current_chapter = None
                if current_part and current_part['chapters']:
                    parts.append(current_part)
                current_part = {
                    'title': text,
                    'chapters': []
                }
        elif tag == 'h3':
            if current_chapter is not None:
                current_part['chapters'].append(current_chapter)
            current_chapter = {
                'part_title': current_part['title'],
                'chapter_num': text,
                'paragraphs': []
            }
        elif tag == 'p':
            if text:
                if current_chapter is not None:
                    current_chapter['paragraphs'].append({
                        'id': len(current_chapter['paragraphs']) + 1,
                        'english': text
                    })

    if current_chapter is not None:
        current_part['chapters'].append(current_chapter)
    if current_part and current_part not in parts:
        parts.append(current_part)

    # Flatten chapters list
    all_chapters = []
    for p in parts:
        for c in p['chapters']:
            all_chapters.append(c)

    novel_data = {
        'title': 'Neuromancer',
        'author': 'William Gibson',
        'parts': parts,
        'chapters': all_chapters
    }
    return novel_data

if __name__ == '__main__':
    data = extract_content('neuromancer.epub')
    with open('data/neuromancer_structured.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(data['parts'])} parts, {len(data['chapters'])} chapters.")
    total_p = sum(len(c['paragraphs']) for c in data['chapters'])
    print(f"Total paragraphs extracted: {total_p}")
