#!/usr/bin/env python3
"""Extract the supplied EPUB into stable chapter/paragraph identifiers."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup

EXPECTED_CHAPTERS = 24
EXPECTED_PARAGRAPHS = 2597


def clean_text(value: str) -> str:
    value = unicodedata.normalize("NFC", value)
    return re.sub(r"\s+", " ", value).strip()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def extract(epub_path: Path) -> dict:
    with zipfile.ZipFile(epub_path) as archive:
        root = archive.read("META-INF/container.xml").decode("utf-8")
        match = re.search(r'full-path="([^"]+)"', root)
        if not match:
            raise ValueError("EPUB container has no rootfile")
        opf_path = match.group(1)
        opf = ET.fromstring(archive.read(opf_path))
        spine_ids = [
            item.attrib["idref"] for item in opf.iter() if item.tag.endswith("itemref")
        ]
        items = {
            item.attrib["id"]: item.attrib["href"]
            for item in opf.iter()
            if item.tag.endswith("item") and "id" in item.attrib and "href" in item.attrib
        }
        base = str(Path(opf_path).parent)
        body = None
        for spine_id in spine_ids:
            href = items.get(spine_id)
            if not href:
                continue
            candidate = str(Path(base) / href)
            soup = BeautifulSoup(archive.read(candidate), "html.parser")
            if soup.find("h3") and soup.find("p"):
                body = soup
                source_document = candidate
                break
        if body is None:
            raise ValueError("Could not locate the EPUB body document")
        dedication: list[str] = []
        for spine_id in spine_ids:
            href = items.get(spine_id)
            if not href:
                continue
            candidate = str(Path(base) / href)
            if candidate == source_document:
                continue
            soup = BeautifulSoup(archive.read(candidate), "html.parser")
            for emphasis in soup.find_all("em"):
                lines = [
                    clean_text(line)
                    for line in emphasis.get_text("\n", strip=True).splitlines()
                    if clean_text(line)
                ]
                if any("Deb" in line for line in lines):
                    dedication = lines
                    break
            if dedication:
                break
        if dedication != ["for Deb", "who made it possible with love"]:
            raise ValueError(f"Unexpected or missing dedication: {dedication!r}")

    chapters: list[dict] = []
    current_part = ""
    current_chapter: dict | None = None
    for element in body.find_all(["h1", "h2", "h3", "p"]):
        text = clean_text(element.get_text(" ", strip=True))
        if not text:
            continue
        if element.name in {"h1", "h2"}:
            current_part = text
            current_chapter = None
        elif element.name == "h3":
            if not text.isdigit():
                raise ValueError(f"Unexpected chapter heading: {text!r}")
            number = int(text)
            current_chapter = {
                "id": f"ch{number:02d}",
                "number": number,
                "part": current_part,
                "paragraphs": [],
            }
            chapters.append(current_chapter)
        elif element.name == "p" and current_chapter is not None:
            # The EPUB's only other paragraph is an empty pagination anchor.
            number = len(current_chapter["paragraphs"]) + 1
            current_chapter["paragraphs"].append(
                {"id": f"{current_chapter['id']}-p{number:04d}", "en": text}
            )

    if len(chapters) != EXPECTED_CHAPTERS:
        raise ValueError(f"Expected {EXPECTED_CHAPTERS} chapters, found {len(chapters)}")
    if [chapter["number"] for chapter in chapters] != list(range(1, 25)):
        raise ValueError("Chapter numbering is not contiguous from 1 to 24")
    paragraph_count = sum(len(chapter["paragraphs"]) for chapter in chapters)
    if paragraph_count != EXPECTED_PARAGRAPHS:
        raise ValueError(
            f"Expected {EXPECTED_PARAGRAPHS} paragraphs, found {paragraph_count}"
        )
    identifiers = [p["id"] for c in chapters for p in c["paragraphs"]]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("Duplicate paragraph identifiers")

    parts: list[str] = []
    for chapter in chapters:
        if chapter["part"] not in parts:
            parts.append(chapter["part"])
    word_count = sum(
        len(paragraph["en"].split())
        for chapter in chapters
        for paragraph in chapter["paragraphs"]
    )
    return {
        "schema": "neuromancer-source/v1",
        "title": "Neuromancer",
        "author": "William Gibson",
        "language": "en-US",
        "source_file": epub_path.name,
        "source_sha256": sha256_file(epub_path),
        "source_document": source_document,
        "chapter_count": len(chapters),
        "paragraph_count": paragraph_count,
        "body_word_count": word_count,
        "frontmatter": {"dedication_en": dedication},
        "parts": parts,
        "chapters": chapters,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epub", type=Path, default=Path("neuromancer.epub"))
    parser.add_argument("--output", type=Path, default=Path("build/source.json"))
    args = parser.parse_args()
    source = extract(args.epub)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Extracted {source['chapter_count']} chapters, "
        f"{source['paragraph_count']} paragraphs, {source['body_word_count']} words."
    )
    print(f"Source SHA-256: {source['source_sha256']}")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
