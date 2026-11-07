#!/usr/bin/env python3
"""Validate translation coverage and, optionally, the rendered PDF artifact."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

import pymupdf as fitz

PROPER_NAMES = [
    "Case",
    "Molly",
    "Armitage",
    "Wintermute",
    "Neuromancer",
    "Ratz",
    "Finn",
    "Riviera",
    "Hideo",
    "3Jane",
    "Freeside",
    "Straylight",
    "Tessier-Ashpool",
    "Sense/Net",
    "Ono-Sendai",
    "Hosaka",
    "Zion",
    "Chiba",
    "Chatsubo",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text)).strip()


def issue(collection: list, code: str, pid: str, detail: str) -> None:
    if len(collection) < 200:
        collection.append({"code": code, "paragraph_id": pid, "detail": detail})


def validate_translation(source: dict, translation: dict, editorial: dict) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    source_paragraphs = {
        paragraph["id"]: paragraph
        for chapter in source["chapters"]
        for paragraph in chapter["paragraphs"]
    }
    translated = translation.get("paragraphs", {})
    source_ids = set(source_paragraphs)
    translated_ids = set(translated)
    for pid in sorted(source_ids - translated_ids)[:200]:
        issue(errors, "missing-paragraph", pid, "No Vietnamese record")
    for pid in sorted(translated_ids - source_ids)[:200]:
        issue(errors, "extra-paragraph", pid, "ID does not exist in source")
    if translation.get("source_sha256") != source.get("source_sha256"):
        errors.append(
            {
                "code": "source-hash-mismatch",
                "detail": "Translation was not generated from the supplied EPUB",
            }
        )
    if translation.get("completed_paragraphs") != len(translated_ids & source_ids):
        errors.append(
            {
                "code": "completion-count-mismatch",
                "detail": "completed_paragraphs does not match valid source IDs",
            }
        )
    if source.get("chapter_count") != 24 or source.get("paragraph_count") != 2597:
        errors.append({"code": "source-shape", "detail": "Expected 24 chapters and 2597 paragraphs"})
    if set(editorial["parts"]) != set(source["parts"]):
        errors.append({"code": "part-titles", "detail": "Editorial part-title keys differ from source"})
    if source.get("frontmatter", {}).get("dedication_en") != [
        "for Deb",
        "who made it possible with love",
    ]:
        errors.append({"code": "dedication-source", "detail": "EPUB dedication is missing or changed"})
    if len(editorial.get("dedication_vi", [])) != 2:
        errors.append({"code": "dedication-translation", "detail": "Expected two Vietnamese dedication lines"})

    length_ratios: list[float] = []
    machine_count = 0
    reviewed_count = 0
    for pid, source_paragraph in source_paragraphs.items():
        if pid not in translated:
            continue
        english = source_paragraph["en"]
        record = translated[pid]
        vietnamese = record.get("vi", "")
        if record.get("en_sha256") != hashlib.sha256(english.encode()).hexdigest():
            issue(errors, "paragraph-hash-mismatch", pid, "English text changed after translation")
        if not vietnamese.strip():
            issue(errors, "empty-translation", pid, "Vietnamese text is empty")
            continue
        if record.get("status") == "human-reviewed":
            reviewed_count += 1
        elif record.get("status") == "machine-draft":
            machine_count += 1
        else:
            issue(errors, "invalid-status", pid, repr(record.get("status")))
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]", vietnamese):
            issue(errors, "invalid-character", pid, "Control or replacement character")
        if re.search(r"<unk>|▁|\[/?PAD\]|<s>|</s>", vietnamese):
            issue(errors, "tokenizer-artifact", pid, "Untokenized model artifact")
        ratio = len(vietnamese) / max(len(english), 1)
        length_ratios.append(ratio)
        if len(english) >= 60 and (ratio < 0.25 or ratio > 3.0):
            issue(warnings, "length-ratio", pid, f"Vietnamese/English character ratio {ratio:.2f}")
        en_normalized = normalized(english)
        vi_normalized = normalized(vietnamese)
        if len(english.split()) >= 8:
            similarity = SequenceMatcher(None, en_normalized.lower(), vi_normalized.lower()).ratio()
            if similarity > 0.90:
                issue(warnings, "possibly-untranslated", pid, f"Text similarity {similarity:.2f}")
            if not re.search(r"[ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]", vietnamese.lower()):
                issue(warnings, "no-vietnamese-diacritics", pid, "Review possible untranslated output")
        words = re.findall(r"\w+", vietnamese.lower(), flags=re.UNICODE)
        if len(words) >= 20:
            ngrams = Counter(tuple(words[index : index + 6]) for index in range(len(words) - 5))
            if ngrams and ngrams.most_common(1)[0][1] >= 4:
                issue(errors, "repetition-loop", pid, "A six-word sequence occurs at least four times")
        if re.search(r"\b(\w+)(?:\s+\1){4,}\b", vietnamese.lower(), flags=re.UNICODE):
            issue(errors, "consecutive-repetition", pid, "One word repeats at least five times")
        missing_names = [name for name in PROPER_NAMES if name in english and name not in vietnamese]
        if missing_names:
            issue(warnings, "proper-name-review", pid, ", ".join(missing_names))

    chapters = []
    for chapter in source["chapters"]:
        ids = [paragraph["id"] for paragraph in chapter["paragraphs"]]
        chapters.append(
            {
                "chapter": chapter["number"],
                "source_paragraphs": len(ids),
                "translated_paragraphs": sum(pid in translated for pid in ids),
                "human_reviewed": sum(
                    translated.get(pid, {}).get("status") == "human-reviewed" for pid in ids
                ),
            }
        )
    glossary_terms = [entry["term"] for entry in editorial["glossary"]]
    if len(glossary_terms) != len(set(glossary_terms)):
        errors.append({"code": "glossary-duplicates", "detail": "Duplicate glossary terms"})

    return {
        "chapters": chapters,
        "translated_paragraphs": len(translated_ids & source_ids),
        "machine_draft_paragraphs": machine_count,
        "human_reviewed_paragraphs": reviewed_count,
        "length_ratio_min": min(length_ratios, default=0),
        "length_ratio_mean": sum(length_ratios) / max(len(length_ratios), 1),
        "length_ratio_max": max(length_ratios, default=0),
        "errors": errors,
        "warnings": warnings,
        "warning_count_note": "At most 200 warning details are retained; aggregate checks remain strict.",
    }


def validate_pdf(pdf_path: Path, source: dict, translation: dict) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    document = fitz.open(pdf_path)
    page_texts = [page.get_text("text") for page in document]
    full_text = normalized(" ".join(page_texts))
    expected_ids = {
        paragraph["id"]
        for chapter in source["chapters"]
        for paragraph in chapter["paragraphs"]
    }
    missing_ids = sorted(pid for pid in expected_ids if pid not in full_text)
    if missing_ids:
        errors.append(
            {
                "code": "pdf-missing-paragraph-ids",
                "detail": f"{len(missing_ids)} missing; first IDs: {missing_ids[:10]}",
            }
        )
    if "Neuromancer" not in document.metadata.get("title", ""):
        errors.append({"code": "pdf-metadata", "detail": "Title metadata is missing"})
    if document.page_count < 50:
        errors.append({"code": "pdf-page-count", "detail": f"Only {document.page_count} pages"})
    if "who made it possible with love" not in full_text or "Dành cho Deb" not in full_text:
        errors.append({"code": "pdf-dedication", "detail": "Bilingual dedication is not searchable"})
    opening = "The sky above the port was the color of television"
    if opening not in full_text:
        errors.append({"code": "pdf-opening", "detail": "Opening English text is not searchable"})
    final_paragraph = source["chapters"][-1]["paragraphs"][-1]["en"]
    final_probe = normalized(final_paragraph)[:55]
    if final_probe not in full_text:
        errors.append({"code": "pdf-ending", "detail": "Final paragraph probe is not searchable"})

    empty_pages = [index + 1 for index, text in enumerate(page_texts) if not text.strip()]
    if empty_pages:
        warnings.append({"code": "pdf-empty-pages", "detail": empty_pages[:30]})
    outside_blocks: list[dict] = []
    font_xrefs: dict[int, str] = {}
    link_count = 0
    for page_number, page in enumerate(document, start=1):
        rect = page.rect
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            if x0 < -2 or y0 < -2 or x1 > rect.width + 2 or y1 > rect.height + 2:
                if len(outside_blocks) < 30:
                    outside_blocks.append(
                        {"page": page_number, "bbox": [x0, y0, x1, y1]}
                    )
        for font in page.get_fonts(full=True):
            font_xrefs[font[0]] = font[3]
        link_count += len(page.get_links())
    if outside_blocks:
        errors.append({"code": "pdf-outside-page", "detail": outside_blocks})
    fonts = []
    for xref, name in sorted(font_xrefs.items()):
        extracted = document.extract_font(xref)
        embedded = bool(extracted and extracted[3])
        fonts.append({"xref": xref, "name": name, "embedded": embedded})
        if not embedded:
            warnings.append({"code": "pdf-font-not-embedded", "detail": name})
    outline = document.get_toc(simple=True)
    if len(outline) < 30:
        errors.append({"code": "pdf-outline", "detail": f"Only {len(outline)} outline entries"})
    if link_count < 20:
        warnings.append({"code": "pdf-links", "detail": f"Only {link_count} links"})
    report = {
        "file": pdf_path.name,
        "file_size_bytes": pdf_path.stat().st_size,
        "sha256": sha256_file(pdf_path),
        "page_count": document.page_count,
        "page_size_points": [document[0].rect.width, document[0].rect.height],
        "text_characters": len(full_text),
        "expected_paragraph_ids": len(expected_ids),
        "missing_paragraph_ids": len(missing_ids),
        "outline_entries": len(outline),
        "link_count": link_count,
        "empty_pages": empty_pages,
        "fonts": fonts,
        "errors": errors,
        "warnings": warnings,
    }
    document.close()
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("build/source.json"))
    parser.add_argument("--translation", type=Path, default=Path("translation/vi.json"))
    parser.add_argument("--editorial", type=Path, default=Path("edition/editorial.json"))
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--output", type=Path, default=Path("build/qa-report.json"))
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8"))
    translation = json.loads(args.translation.read_text(encoding="utf-8"))
    editorial = json.loads(args.editorial.read_text(encoding="utf-8"))
    translation_report = validate_translation(source, translation, editorial)
    report = {
        "schema": "neuromancer-qa/v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "epub_sha256": source["source_sha256"],
            "chapters": source["chapter_count"],
            "paragraphs": source["paragraph_count"],
            "body_words": source["body_word_count"],
        },
        "translation": translation_report,
        "scope_note": (
            "Automated QA establishes structural coverage and artifact integrity, "
            "not literary translation quality."
        ),
    }
    error_count = len(translation_report["errors"])
    warning_count = len(translation_report["warnings"])
    if args.pdf:
        pdf_report = validate_pdf(args.pdf, source, translation)
        report["pdf"] = pdf_report
        error_count += len(pdf_report["errors"])
        warning_count += len(pdf_report["warnings"])
    report["result"] = "pass" if error_count == 0 else "fail"
    report["error_count"] = error_count
    report["retained_warning_count"] = warning_count
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"QA {report['result'].upper()}: {error_count} errors, "
        f"{warning_count} retained warnings; wrote {args.output}"
    )
    if args.pdf and "pdf" in report:
        print(
            f"PDF: {report['pdf']['page_count']} pages, "
            f"{report['pdf']['file_size_bytes']:,} bytes, "
            f"{report['pdf']['outline_entries']} outline entries"
        )
    if error_count:
        for error in translation_report["errors"][:20]:
            print(f"ERROR {error}", file=sys.stderr)
        if args.pdf:
            for error in report["pdf"]["errors"][:20]:
                print(f"ERROR {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
