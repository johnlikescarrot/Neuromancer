#!/usr/bin/env python3
"""Validate the companion PDF: structure, coverage, glyphs and source-overlap guard."""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ED = ROOT / "edition"
sys.path.insert(0, str(ED / "content"))
import chapters_01_07, chapters_08_12, chapters_13_18, chapters_19_24
import frontmatter as fm
import practice as pr

import pymupdf
from bs4 import BeautifulSoup
from fontTools.ttLib import TTFont

CHAPTERS = chapters_01_07.CHAPTERS + chapters_08_12.CHAPTERS + chapters_13_18.CHAPTERS + chapters_19_24.CHAPTERS
PDF = ED / "Neuromancer-Bilingual-Learning-Companion.pdf"


def norm_tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def ngrams(tokens, n):
    return {tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)}


def main() -> None:
    report = {"checks": [], "warnings": []}
    def check(name, ok, detail=""):
        report["checks"].append({"name": name, "pass": bool(ok), "detail": detail})
        if not ok:
            print("FAIL", name, detail)

    check("pdf_exists", PDF.exists() and PDF.stat().st_size > 100_000, str(PDF.stat().st_size if PDF.exists() else 0))
    doc = pymupdf.open(PDF)
    text = "\n".join(page.get_text() for page in doc)
    check("page_count", len(doc) >= 60, f"{len(doc)} pages")
    check("vietnamese_diacritics", all(ch in text for ch in "ăâđêôơư"), "required lowercase Vietnamese letters present")
    check("no_cjk_contamination", not re.search(r"[\u4e00-\u9fff]", text), "no Chinese characters in extracted text")
    check("not_a_translation_notice", "NOT A TRANSLATION" in text and "KHÔNG PHẢI BẢN DỊCH" in text)
    # Chapter coverage
    missing = [c["n"] for c in CHAPTERS if f"Chapter {c['n']:02d}" not in text]
    check("all_24_chapters", not missing, f"missing={missing}")
    # Vocabulary coverage
    vocab = [v[0] for c in CHAPTERS for v in c["vocab"]]
    check("vocab_count", len(vocab) == 192, str(len(vocab)))
    missing_vocab = [w for w in vocab if w.lower() not in text.lower()]
    check("vocab_in_pdf", not missing_vocab, f"missing={missing_vocab[:10]}")
    # Practice coverage
    for rid in ["R1","R2","R3","L1","L2","W1","W2","W3","W4","I1","I2","I3"]:
        check(f"practice_{rid}", rid in text)
    # Outline / bookmarks
    toc = doc.get_toc()
    check("pdf_outline", len(toc) >= 30, f"{len(toc)} outline entries")
    # Font glyph coverage for extracted text
    fonts = [TTFont(ED / "fonts" / f) for f in ["BeVietnamPro-Regular.ttf","BeVietnamPro-Bold.ttf","BeVietnamPro-Italic.ttf"]]
    cmap = set()
    for f in fonts:
        for table in f["cmap"].tables:
            cmap.update(table.cmap.keys())
    used = {ord(ch) for ch in text if not ch.isspace() and ord(ch) > 31}
    missing_glyphs = sorted(used - cmap)
    check("font_glyph_coverage", not missing_glyphs, "missing=" + "".join(chr(x) for x in missing_glyphs[:20]))
    # Source-overlap guard: no 12-token run from the novel appears in the PDF.
    with zipfile.ZipFile(ROOT / "neuromancer.epub") as z:
        soup = BeautifulSoup(z.read("EPUB/text/ch002.xhtml"), "html.parser")
        source = " ".join(p.get_text(" ", strip=True) for p in soup.find_all("p"))
    src_12 = ngrams(norm_tokens(source), 12)
    pdf_12 = ngrams(norm_tokens(text), 12)
    overlap = src_12 & pdf_12
    check("no_12_token_source_overlap", not overlap, f"overlap_count={len(overlap)}")
    # Content sanity: no obvious placeholder or blank pages
    check("no_placeholder", "TODO" not in text and "Lorem ipsum" not in text)
    blank_pages = []
    for i, page in enumerate(doc):
        lines = [l.strip() for l in page.get_text().splitlines() if l.strip()]
        body = [l for l in lines if not l.startswith("Neuromancer —") and not l.startswith("Original study") and not l.startswith("English–Vietnamese") and l != str(i+1)]
        if len(" ".join(body)) < 20:
            blank_pages.append(i+1)
    check("no_blank_pages", not blank_pages, f"blank={blank_pages}")
    check("bilingual_chapter_units", all(c.get("summary_en") and c.get("summary_vi") and c.get("task_en") and c.get("task_vi") for c in CHAPTERS))
    # Render representative pages for visual inspection (not committed)
    tmp = ED / "tmp"
    tmp.mkdir(exist_ok=True)
    sample_pages = sorted({0, 1, 2, 5, 10, min(20, len(doc)-1), min(40, len(doc)-1), len(doc)-1})
    for i in sample_pages:
        pix = doc[i].get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2))
        pix.save(tmp / f"page-{i+1:03}.png")
    report["page_count"] = len(doc)
    report["outline_entries"] = len(toc)
    report["sample_pages"] = [i+1 for i in sample_pages]
    report["pdf_bytes"] = PDF.stat().st_size
    out = ED / "reports" / "validation.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    failed = [c for c in report["checks"] if not c["pass"]]
    print(json.dumps({"pages": len(doc), "outline": len(toc), "checks": len(report["checks"]), "failed": len(failed), "bytes": PDF.stat().st_size}, indent=2))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
