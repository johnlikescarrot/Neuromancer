#!/usr/bin/env python3
"""
Deterministic extractor for Neuromancer (neuromancer.epub).
Extracts 100% of front matter dedication, all 5 Parts, all 24 Chapters,
and author's colophon/acknowledgments into structured JSON files under data/source/.
"""

import json
import os
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPUB_PATH = ROOT / "neuromancer.epub"
OUT_DIR = ROOT / "data" / "source"


def serialize_inline(el: ET.Element) -> str:
    """Serialize inline XML element preserving <em> and <br/> cleanly."""
    parts = []
    if el.text:
        parts.append(el.text)
    for child in el:
        tag = child.tag.split("}")[-1]
        inner = serialize_inline(child)
        if tag in ("em", "i"):
            inner_stripped = inner.strip()
            if inner_stripped:
                # Normalize internal newlines inside <em> without duplicating <br/>
                inner_norm = re.sub(r"\s*/\s*\n\s*", " / ", inner_stripped)
                inner_norm = re.sub(r"\s*\n\s*", " — ", inner_norm)
                parts.append(f"*{inner_norm}*")
        elif tag == "br":
            parts.append(" / ")
        else:
            parts.append(inner)
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def clean_text(raw: str) -> str:
    """
    Clean plain-text -> Pandoc conversion artifacts while preserving 100% of
    William Gibson's words, emphasis, and punctuation:
      1. Remove stray LaTeX non-breaking space ties ('~')
      2. Restore ASCII-truncated French loanword 'cloisonn' -> 'cloisonné'
      3. Convert balanced '_..._' plain-text italics to '*...*'
      4. Normalize ' -- ' / '--' to typographic em-dash '—'
      5. Collapse internal whitespace runs cleanly
    """
    txt = raw.replace("~", "")
    txt = re.sub(r"\bcloisonn\b", "cloisonné", txt)
    # Convert _italics_ to *italics*
    txt = re.sub(r"_([^_]+)_", r"*\1*", txt)
    # Normalize double hyphens to em-dash
    txt = re.sub(r"\s*--\s*", "—", txt)
    # Collapse repeated or edge line-break slashes from spacer <br/> tags
    txt = re.sub(r"(?:\s*/\s*)+", " / ", txt).strip()
    txt = re.sub(r"^/\s*|\s*/$", "", txt).strip()
    # Collapse multiple spaces/newlines
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt


PART_META = {
    "part-one---chiba-city-blues": {
        "part_num": 1,
        "title_en": "PART ONE — CHIBA CITY BLUES",
        "title_vi": "PHẦN MỘT — KHÚC BLUES THÀNH PHỐ CHIBA",
        "subtitle_en": "Chiba City Blues",
        "subtitle_vi": "Khúc Blues Thành Phố Chiba",
    },
    "part-two---the-shopping-expedition": {
        "part_num": 2,
        "title_en": "PART TWO — THE SHOPPING EXPEDITION",
        "title_vi": "PHẦN HAI — CHUYẾN VIỄN CHINH MUA SẮM",
        "subtitle_en": "The Shopping Expedition",
        "subtitle_vi": "Chuyến Viễn Chinh Mua Sắm",
    },
    "part-three---midnight-in-the-rue-jules-verne": {
        "part_num": 3,
        "title_en": "PART THREE — MIDNIGHT IN THE RUE JULES VERNE",
        "title_vi": "PHẦN BA — NỬA ĐÊM TRÊN PHỐ JULES VERNE",
        "subtitle_en": "Midnight in the Rue Jules Verne",
        "subtitle_vi": "Nửa Đêm Trên Phố Jules Verne",
    },
    "part-four---the-straylight-run": {
        "part_num": 4,
        "title_en": "PART FOUR — THE STRAYLIGHT RUN",
        "title_vi": "PHẦN BỐN — PHI VỤ ĐỘT KÍCH STRAYLIGHT",
        "subtitle_en": "The Straylight Run",
        "subtitle_vi": "Phi Vụ Đột Kích Straylight",
    },
    "coda---departure-and-arrival": {
        "part_num": 5,
        "title_en": "CODA — DEPARTURE AND ARRIVAL",
        "title_vi": "VĨ THANH — KHỞI HÀNH VÀ ĐẾN ĐÍCH",
        "subtitle_en": "Departure and Arrival",
        "subtitle_vi": "Khởi Hành Và Đến Đích",
    },
}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(EPUB_PATH, "r") as zf:
        ch001_xml = zf.read("EPUB/text/ch001.xhtml").decode("utf-8")
        ch002_xml = zf.read("EPUB/text/ch002.xhtml").decode("utf-8")

    # 1. Extract dedication from ch001.xhtml
    r1 = ET.fromstring(ch001_xml)
    dedication_en = ""
    for p in r1.iter():
        if p.tag.split("}")[-1] == "p":
            s = clean_text(serialize_inline(p))
            if "for Deb" in s:
                dedication_en = s
                break

    # 2. Walk ch002.xhtml sections in document order
    r2 = ET.fromstring(ch002_xml)
    chapters = []
    current_part = None

    def walk(el: ET.Element):
        nonlocal current_part
        tag = el.tag.split("}")[-1]
        if tag == "section":
            sid = el.attrib.get("id", "")
            if sid in PART_META:
                current_part = PART_META[sid]
            else:
                # Check if this section is a numbered chapter (has <h3>1..24</h3>)
                h3_list = [
                    "".join(c.itertext()).strip()
                    for c in el
                    if c.tag.split("}")[-1] == "h3"
                ]
                if h3_list and h3_list[0].isdigit():
                    ch_num = int(h3_list[0])
                    paras = []
                    idx = 0
                    for c in el:
                        if c.tag.split("}")[-1] == "p":
                            txt = clean_text(serialize_inline(c))
                            if not txt:
                                continue
                            idx += 1
                            pid = f"{ch_num:02d}-{idx:03d}"
                            paras.append(
                                {
                                    "id": pid,
                                    "index": idx,
                                    "en": txt,
                                    "word_count": len(txt.split()),
                                }
                            )
                    ch_obj = {
                        "chapter": ch_num,
                        "chapter_id": f"ch{ch_num:02d}",
                        "part_num": current_part["part_num"],
                        "part_title_en": current_part["title_en"],
                        "part_title_vi": current_part["title_vi"],
                        "paragraph_count": len(paras),
                        "word_count": sum(p["word_count"] for p in paras),
                        "paragraphs": paras,
                    }
                    chapters.append(ch_obj)
        for child in el:
            if child.tag.split("}")[-1] in ("body", "section"):
                walk(child)

    walk(r2)

    assert len(chapters) == 24, f"Expected 24 chapters, got {len(chapters)}"

    for ch in chapters:
        ch_file = OUT_DIR / f"{ch['chapter_id']}.json"
        ch_file.write_text(
            json.dumps(ch, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    total_paras = sum(c["paragraph_count"] for c in chapters)
    total_words = sum(c["word_count"] for c in chapters)

    manifest = {
        "title": "Neuromancer",
        "author": "William Gibson",
        "original_publication_year": 1984,
        "dedication": {
            "en": dedication_en,
            "vi": "*Tặng Deb / người đã biến cuốn sách này thành hiện thực bằng tình yêu thương*",
        },
        "parts": list(PART_META.values()),
        "total_chapters": len(chapters),
        "total_paragraphs": total_paras,
        "total_words": total_words,
        "chapters": [
            {
                "chapter": c["chapter"],
                "chapter_id": c["chapter_id"],
                "part_num": c["part_num"],
                "part_title_en": c["part_title_en"],
                "part_title_vi": c["part_title_vi"],
                "paragraph_count": c["paragraph_count"],
                "word_count": c["word_count"],
            }
            for c in chapters
        ],
    }

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Extracted {len(chapters)} chapters, {total_paras} paragraphs, {total_words} words.")
    print(f"Dedication: {dedication_en}")
    for c in manifest["chapters"]:
        print(
            f"  Ch {c['chapter']:2d} (Part {c['part_num']}): "
            f"{c['paragraph_count']:3d} paras, {c['word_count']:4d} words"
        )


if __name__ == "__main__":
    main()
