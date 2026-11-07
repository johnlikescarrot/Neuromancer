import zipfile
import re
import json
import html
from pathlib import Path

def clean_html(text):
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'</p>', '\n\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    # Normalize multiple whitespace
    lines = [re.sub(r'\s+', ' ', line).strip() for line in text.split('\n')]
    paragraphs = [p for p in lines if p]
    return paragraphs

def extract_novel():
    epub_path = Path("neuromancer.epub")
    with zipfile.ZipFile(epub_path, 'r') as z:
        content_ch001 = z.read("EPUB/text/ch001.xhtml").decode("utf-8")
        content_ch002 = z.read("EPUB/text/ch002.xhtml").decode("utf-8")

    novel = {
        "title": "Neuromancer",
        "author": "William Gibson",
        "dedication": "for Deb\nwho made it possible with love",
        "parts": []
    }

    # Regex to split on headings
    heading_pattern = re.compile(r'(<h[1-6][^>]*>.*?</h[1-6]>)', re.IGNORECASE | re.DOTALL)
    tokens = heading_pattern.split(content_ch002)

    current_part = None
    current_chapter = None
    part_number = 0

    for i in range(1, len(tokens), 2):
        h_tag = tokens[i]
        body = tokens[i + 1] if i + 1 < len(tokens) else ""

        # Clean heading title
        h_clean = re.sub(r'<[^>]+>', '', h_tag).strip()

        if "PART " in h_clean.upper() or "CODA" in h_clean.upper():
            part_number += 1
            current_part = {
                "part_index": part_number,
                "part_title": h_clean,
                "chapters": []
            }
            novel["parts"].append(current_part)
        else:
            # Chapter heading
            paragraphs = clean_html(body)
            # Remove empty paragraphs
            paragraphs = [p for p in paragraphs if len(p.strip()) > 0]

            chapter_obj = {
                "chapter_title": h_clean,
                "paragraphs": paragraphs,
                "paragraph_count": len(paragraphs),
                "word_count": sum(len(p.split()) for p in paragraphs)
            }
            if current_part is not None:
                current_part["chapters"].append(chapter_obj)

    # Save to json
    output_path = Path("data/extracted_novel.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(novel, f, ensure_ascii=False, indent=2)

    total_chapters = sum(len(p["chapters"]) for p in novel["parts"])
    total_paragraphs = sum(sum(c["paragraph_count"] for c in p["chapters"]) for p in novel["parts"])
    total_words = sum(sum(c["word_count"] for c in p["chapters"]) for p in novel["parts"])

    print(f"Extraction complete:")
    print(f"- Parts: {len(novel['parts'])}")
    print(f"- Chapters: {total_chapters}")
    print(f"- Paragraphs: {total_paragraphs}")
    print(f"- Words: {total_words}")
    print(f"- Output saved to: {output_path}")

if __name__ == "__main__":
    extract_novel()
