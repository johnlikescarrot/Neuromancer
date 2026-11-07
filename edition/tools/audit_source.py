#!/usr/bin/env python3
"""Audit the supplied EPUB without exporting its text. Requires beautifulsoup4."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_SHA256 = "c1c38a9fbf06a36ad86054e7e11083c95d3d20d0f3988ac01c12ca7553b4ba60"


def tokens(text: str) -> list[str]:
    # A reproducible counting convention, not a publisher's word count.
    return re.findall(r"[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*", text)


def audit(epub: Path) -> dict:
    files = []
    for p in sorted(ROOT.iterdir()):
        if p.is_file():
            files.append({"name": p.name, "bytes": p.stat().st_size,
                          "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
    with zipfile.ZipFile(epub) as z:
        bad_member = z.testzip()
        opf = ET.fromstring(z.read("EPUB/content.opf"))
        nav = BeautifulSoup(z.read("EPUB/nav.xhtml"), "html.parser")
        ncx = ET.fromstring(z.read("EPUB/toc.ncx"))
        spine = [x.get("idref") for x in opf.iter() if x.tag.endswith("}itemref")]
        manifest = {x.get("id"): x.get("href") for x in opf.iter() if x.tag.endswith("}item")}
        ids: dict[str, set[str]] = {}
        for name in z.namelist():
            if name.endswith((".xhtml", ".html")):
                doc = BeautifulSoup(z.read(name), "html.parser")
                ids[name] = {x.get("id") for x in doc.find_all(id=True)}
        broken = []
        links = []
        for a in nav.find_all("a", href=True):
            href = a["href"]
            file, _, fragment = href.partition("#")
            target = "EPUB/" + unquote(file)
            links.append({"label": a.get_text(" ", strip=True), "href": href})
            if target not in ids or (fragment and unquote(fragment) not in ids[target]):
                broken.append(href)
        body = BeautifulSoup(z.read("EPUB/text/ch002.xhtml"), "html.parser")
        chapters, parts = [], []
        part = None
        for section in body.find_all("section", recursive=True):
            heading = section.find(re.compile(r"^h[1-6]$"), recursive=False)
            if heading is None:
                continue
            label = heading.get_text(" ", strip=True)
            if not label.isdigit():
                part = {"title": label, "id": section.get("id"), "chapters": []}
                parts.append(part)
                continue
            # Direct children avoid double-counting text in nested EPUB sections.
            paragraphs = [p.get_text(" ", strip=True) for p in section.find_all("p", recursive=False)]
            text = "\n\n".join(paragraphs)
            number = int(label)
            chapters.append({"number": number, "part": part["title"] if part else None,
                             "id": section.get("id"), "paragraphs": len(paragraphs),
                             "words": len(tokens(text)), "characters": len(text)})
            if part:
                part["chapters"].append(number)
        all_text = "\n".join(p.get_text(" ", strip=True) for p in body.find_all("p"))
        ncx_points = [x for x in ncx.iter() if x.tag.endswith("}navPoint")]
        dc = "{http://purl.org/dc/elements/1.1/}"
        modified = next(x.text for x in opf.iter() if x.tag.endswith("}meta") and x.get("property") == "dcterms:modified")
        return {
            "schema_version": 1,
            "source": {"path": epub.name, "bytes": epub.stat().st_size,
                       "sha256": hashlib.sha256(epub.read_bytes()).hexdigest(),
                       "expected_sha256": EXPECTED_SHA256, "zip_integrity_error": bad_member},
            "bibliography": {"title": opf.find(".//" + dc + "title").text,
                             "creator": opf.find(".//" + dc + "creator").text,
                             "language": opf.find(".//" + dc + "language").text,
                             "epub_modified": modified,
                             "publication_date_in_archive_metadata": "1984-07-01",
                             "isbn": None, "print_publisher": None, "translation_license": None},
            "structure": {"spine": spine, "manifest": manifest,
                          "parts": parts, "chapters": chapters,
                          "chapter_count": len(chapters), "part_count_including_coda": len(parts),
                          "nav_link_count": len(links), "ncx_navpoint_count": len(ncx_points),
                          "broken_nav_links": broken},
            "counts": {"counting_rule": "Unicode-aware ASCII word regex; hyphen/apostrophe compounds count as one; headings excluded; acknowledgements included.",
                       "body_words": len(tokens(all_text)),
                       "chapter_words": sum(c["words"] for c in chapters),
                       "body_paragraphs": len(body.find_all("p")),
                       "epub_members": len(z.namelist())},
            "observations": [
                "The archive metadata describes a custom EPUB assembled from online plain text; this is not evidence of public-domain status or permission to translate.",
                "The EPUB has no ISBN or print-edition statement. Do not invent print page numbers or claim equivalence to a licensed edition.",
                "The NCX nests later navigation points inside earlier ones; the XHTML navigation document is the clearer structural guide.",
                "Underscore emphasis survives in some paragraphs. Spelling and punctuation have not been silently corrected against a print edition.",
                "The final numbered chapter includes a dated inscription and acknowledgements after the narrative; chapter word counts include that paratext.",
                "This audit exports counts and bibliographic/structural facts only, not the source prose."
            ],
            "repository_files": files,
        }


def markdown(report: dict) -> str:
    s, c = report["structure"], report["counts"]
    lines = ["# Source audit / Kiểm tra nguồn", "",
             "## English", "",
             f"The supplied EPUB is an unprotected-by-DRM file, not thereby an uncopyrighted work. It identifies William Gibson as the author. Its archive metadata dates the novel to 1984 and describes a custom conversion from plain text. Public access is not a translation licence.",
             f"The structural pass finds **{s['chapter_count']} numbered chapters**, **{len(s['parts']) - 1} numbered parts plus a coda**, and **{c['body_words']:,} body words** under the stated counting rule. This is not a print-edition word count.",
             f"EPUB SHA-256: `{report['source']['sha256']}`.",
             f"ZIP integrity: {'PASS' if report['source']['zip_integrity_error'] is None else 'FAIL'}. Broken XHTML navigation links: {len(s['broken_nav_links'])}.",
             "", "| Chapter | Part | Words | Paragraphs |", "|---:|---|---:|---:|"]
    for ch in s["chapters"]:
        lines.append(f"| {ch['number']} | {ch['part']} | {ch['words']:,} | {ch['paragraphs']} |")
    lines += ["", "### Editorial cautions", ""] + ["- " + x for x in report["observations"]]
    lines += ["", "## Tiếng Việt", "",
              "Tệp EPUB được cung cấp xác định tác giả là William Gibson. Siêu dữ liệu lưu trữ ghi năm xuất bản 1984 và mô tả việc dựng EPUB từ văn bản thuần. Khả năng truy cập công khai không đồng nghĩa với phạm vi công cộng hoặc giấy phép dịch.",
              f"Kiểm tra cấu trúc ghi nhận **{s['chapter_count']} chương đánh số**, **{len(s['parts']) - 1} phần chính và một phần kết**, cùng **{c['body_words']:,} từ thân văn bản** theo quy tắc đếm trong JSON. Không có số trang bản in để đối chiếu.",
              "Mục lục NCX có phân cấp lồng bất thường; mục lục XHTML rõ ràng hơn. Một số dấu nhấn dạng gạch dưới còn sót. Chính tả và dấu câu chưa được hiệu đính theo bản in. Chương 24 có lời đề tặng/ngày tháng và lời cảm ơn sau truyện; số từ chương bao gồm phần này.",
              "Báo cáo chỉ xuất số liệu và cấu trúc, không xuất văn xuôi nguồn. Các tệp gốc không bị sửa.",
              "", "## Rebuild / Tạo lại", "",
              "```sh", "python -m pip install beautifulsoup4",
              "python edition/tools/audit_source.py", "```", ""]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epub", type=Path, default=ROOT / "neuromancer.epub")
    args = parser.parse_args()
    report = audit(args.epub)
    out = ROOT / "edition" / "reports"
    out.mkdir(parents=True, exist_ok=True)
    (out / "source-audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "source-audit.md").write_text(markdown(report), encoding="utf-8")
    assert report["source"]["sha256"] == EXPECTED_SHA256, "Source differs from the audited file"
    assert [c["number"] for c in report["structure"]["chapters"]] == list(range(1, 25))
    assert not report["structure"]["broken_nav_links"]
    print(json.dumps(report["counts"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
