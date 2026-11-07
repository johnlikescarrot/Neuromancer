#!/usr/bin/env python3
"""
Publication-grade Typst PDF compiler for the Complete Bilingual Edition of Neuromancer.
Compiles Front Matter + Parallel Bilingual Chapters (1..24) + Per-Chapter C1/C2 Mastery Dossiers
+ Consolidated Alphabetical Master Vocabulary Index + Back Matter Capstone Pack into PDF.
"""

import argparse
import glob
import json
import re
import sys
from pathlib import Path

import pymupdf
import typst

from edition_utils import (
    PEDAGOGY_DIR,
    ROOT,
    TRANS_DIR,
    load_manifest,
    load_source_chapter,
    load_study_dossier,
    parse_vi_file,
)


def typst_escape_plain(s: str) -> str:
    """Escape all special Typst markup characters in plain text."""
    out = []
    for ch in s:
        if ch in ("\\", "#", "$", "@", "<", ">", "*", "_", "`", "~", "[", "]"):
            out.append("\\" + ch)
        else:
            out.append(ch)
    return "".join(out)


def typst_markup(text: str) -> str:
    """
    Convert clean source/translation string (where '**...**' marks bold and
    '*...*' marks italics) into safe Typst markup using #strong[...] / #emph[...]
    with all other characters escaped.
    """
    token_re = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")
    parts = token_re.split(text)
    rendered = []
    for part in parts:
        if len(part) >= 4 and part.startswith("**") and part.endswith("**"):
            inner = typst_escape_plain(part[2:-2])
            rendered.append(f"#strong[{inner}]")
        elif len(part) >= 2 and part.startswith("*") and part.endswith("*"):
            inner = typst_escape_plain(part[1:-1])
            rendered.append(f"#emph[{inner}]")
        else:
            rendered.append(typst_escape_plain(part))
    return "".join(rendered)


def collect_font_dirs() -> list[str]:
    font_files = glob.glob(str(ROOT / "node_modules" / "@expo-google-fonts" / "**" / "*.ttf"), recursive=True)
    dirs = sorted({str(Path(f).parent) for f in font_files})
    if Path("/usr/share/fonts/truetype/dejavu").exists():
        dirs.append("/usr/share/fonts/truetype/dejavu")
    return dirs


def generate_typst_source(chapters_to_include: list[int], is_complete: bool) -> str:
    manifest = load_manifest()
    front = json.loads((ROOT / "data" / "front_matter.json").read_text(encoding="utf-8"))
    back_path = ROOT / "data" / "back_matter.json"
    back = json.loads(back_path.read_text(encoding="utf-8")) if back_path.exists() else None

    lines: list[str] = []

    # Document & Typography Setup
    lines.append(
        r"""
#set document(
  title: "Neuromancer — Ấn Bản Song Ngữ Anh–Việt Toàn Văn & Học Thuật C1/C2",
  author: "William Gibson (Nguyên tác) • Ấn bản Học thuật Song ngữ C1/C2",
)

#let navy = rgb("#0B1120")
#let slate-dark = rgb("#1E293B")
#let slate-mid = rgb("#475569")
#let slate-muted = rgb("#64748B")
#let border-light = rgb("#CBD5E1")
#let bg-soft = rgb("#F8FAFC")
#let bg-study = rgb("#F1F5F9")
#let cyan-accent = rgb("#0284C7")
#let cyan-bright = rgb("#38BDF8")
#let amber-accent = rgb("#D97706")
#let amber-bright = rgb("#FBBF24")
#let emerald-accent = rgb("#059669")

#set text(
  font: ("Crimson Pro", "Be Vietnam Pro", "DejaVu Serif"),
  size: 10.4pt,
  fill: rgb("#0F172A"),
  lang: "vi",
)

#set par(
  justify: true,
  leading: 0.62em,
  spacing: 0.85em,
)

// Cover Page (no headers/footers/margins)
#page(
  paper: "a4",
  margin: 0pt,
  fill: navy,
)[
  #place(top + left, dx: 14mm, dy: 14mm)[
    #rect(
      width: 182mm,
      height: 269mm,
      stroke: 0.7pt + rgb("#1E3A5F"),
      inset: 14mm,
    )[
      #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white)
      #grid(
        columns: (1fr, auto),
        align(left)[
          #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8.5pt, fill: cyan-bright, tracking: 1.8pt)[
            UNABRIDGED BILINGUAL CRITICAL & PEDAGOGICAL EDITION
          ]
        ],
        align(right)[
          #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8.5pt, fill: amber-bright, tracking: 1.2pt)[
            CEFR C1 → C2
          ]
        ]
      )
      #v(4mm)
      #line(length: 100%, stroke: 0.5pt + cyan-accent)
      #v(26mm)

      #text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 12pt, weight: "medium", fill: rgb("#94A3B8"), tracking: 3pt)[
        WILLIAM GIBSON
      ]
      #v(4mm)
      #text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 42pt, weight: "extrabold", fill: white, tracking: 2pt)[
        NEUROMANCER
      ]
      #v(3mm)
      #text(font: ("Crimson Pro", "DejaVu Serif"), size: 17pt, style: "italic", fill: cyan-bright)[
        Ấn Bản Song Ngữ Anh–Việt Toàn Văn & Tinh Thông Học Thuật
      ]
      #v(8mm)
      #rect(width: 48mm, height: 1.2mm, fill: amber-bright)
      #v(8mm)
      #set par(justify: false, leading: 0.75em)
      #text(size: 10.5pt, fill: rgb("#CBD5E1"))[
        Bản dịch văn học hoàn chỉnh 100% nguyên tác (5 Phần • 24 Chương • 2.597 Đoạn văn) đối chiếu song song từng đoạn, tích hợp hệ thống phân tích từ vựng học thuật, giải phẫu cú pháp nâng cao và bài tập thực chiến theo 5 chuẩn khảo thí quốc tế:
      ]
      #v(10mm)

      #grid(
        columns: (1fr, 1fr),
        gutter: 4mm,
        rect(width: 100%, fill: rgb("#111C33"), stroke: 0.5pt + rgb("#1E3A5F"), radius: 3pt, inset: 4mm)[
          #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8pt, fill: cyan-bright)[TOEFL iBT TARGET]\
          #v(1mm)
          #text(size: 10.5pt, weight: "bold", fill: white)[90 điểm (trước 21/01/2026) • Band 5.0 (từ 21/01/2026)]
        ],
        rect(width: 100%, fill: rgb("#111C33"), stroke: 0.5pt + rgb("#1E3A5F"), radius: 3pt, inset: 4mm)[
          #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8pt, fill: cyan-bright)[IELTS ACADEMIC / GT]\
          #v(1mm)
          #text(size: 10.5pt, weight: "bold", fill: white)[Band 7.0+ (Lexical & Syntactic Mastery)]
        ],
        rect(width: 100%, fill: rgb("#111C33"), stroke: 0.5pt + rgb("#1E3A5F"), radius: 3pt, inset: 4mm)[
          #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8pt, fill: cyan-bright)[PTE ACADEMIC & DET]\
          #v(1mm)
          #text(size: 10.5pt, weight: "bold", fill: white)[PTE 65+ • Duolingo English Test 120+]
        ],
        rect(width: 100%, fill: rgb("#111C33"), stroke: 0.5pt + rgb("#1E3A5F"), radius: 3pt, inset: 4mm)[
          #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8pt, fill: cyan-bright)[CAMBRIDGE QUALIFICATIONS]\
          #v(1mm)
          #text(size: 10.5pt, weight: "bold", fill: white)[Scale 185+ (C1 Advanced / C2 Proficiency)]
        ],
      )

      #v(1fr)
      #line(length: 100%, stroke: 0.4pt + rgb("#334155"))
      #v(3mm)
      #grid(
        columns: (1fr, auto),
        align(left)[
          #text(font: ("Crimson Pro", "DejaVu Serif"), size: 9.5pt, style: "italic", fill: rgb("#94A3B8"))[
            "The sky above the port was the color of television, tuned to a dead channel."
          ]
        ],
        align(right)[
          #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8pt, fill: rgb("#64748B"))[
            CHIBA • SPRAWL • ZION • FREESIDE • STRAYLIGHT
          ]
        ]
      )
    ]
  ]
]

// Interior Page Geometry & Running Headers/Footers
#set page(
  paper: "a4",
  margin: (top: 20mm, bottom: 20mm, left: 16mm, right: 16mm),
  header: context {
    if counter(page).get().first() > 2 {
      set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 7.5pt, fill: slate-muted)
      grid(
        columns: (1fr, auto),
        align(left)[NEUROMANCER — WILLIAM GIBSON],
        align(right)[ẤN BẢN SONG NGỮ ANH–VIỆT TOÀN VĂN & HỌC THUẬT C1/C2]
      )
      v(-2mm)
      line(length: 100%, stroke: 0.35pt + border-light)
    }
  },
  footer: context {
    if counter(page).get().first() > 1 {
      set text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8pt, fill: slate-muted)
      line(length: 100%, stroke: 0.35pt + border-light)
      v(1.5mm)
      grid(
        columns: (1fr, auto, 1fr),
        align(left)[TOEFL 90/5.0 • IELTS 7.0 • PTE 65],
        align(center)[— #counter(page).display() —],
        align(right)[CAMBRIDGE 185 • DET 120]
      )
    }
  }
)

#show heading.where(level: 1): it => {
  v(4mm)
  block(breakable: false)[
    #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 17pt, weight: "bold", fill: navy)
    #it.body
    #v(1.5mm)
    #line(length: 100%, stroke: 1pt + cyan-accent)
    #v(2mm)
  ]
}

#show heading.where(level: 2): it => {
  v(3mm)
  block(breakable: false)[
    #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 12.5pt, weight: "bold", fill: slate-dark)
    #it.body
    #v(1mm)
  ]
}

#show heading.where(level: 3): it => {
  v(2mm)
  block(breakable: false)[
    #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 10.5pt, weight: "semibold", fill: cyan-accent)
    #it.body
    #v(0.5mm)
  ]
}
"""
    )

    # Title & Dedication Page
    ded_en = typst_markup(manifest["dedication"]["en"])
    ded_vi = typst_markup(manifest["dedication"]["vi"])
    edition_status = (
        "ẤN BẢN HOÀN CHỈNH TOÀN VĂN (24/24 CHƯƠNG)"
        if is_complete
        else f"BẢN XEM TRƯỚC TIẾN ĐỘ ({len(chapters_to_include)}/24 CHƯƠNG)"
    )

    lines.append(
        f"""
#v(18mm)
#align(center)[
  #text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 9pt, fill: cyan-accent, tracking: 2pt)[{typst_escape_plain(edition_status)}]
  #v(4mm)
  #text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 26pt, weight: "bold", fill: navy)[NEUROMANCER]
  #v(2mm)
  #text(font: ("Crimson Pro", "DejaVu Serif"), size: 14pt, style: "italic", fill: slate-mid)[William Gibson (1984)]
  #v(14mm)
  #rect(width: 125mm, fill: bg-soft, stroke: 0.5pt + border-light, radius: 4pt, inset: 6mm)[
    #set par(justify: false)
    #text(size: 11pt)[{ded_en}]
    #v(2mm)
    #line(length: 40%, stroke: 0.4pt + border-light)
    #v(2mm)
    #text(size: 10.5pt, fill: slate-mid)[{ded_vi}]
  ]
  #v(16mm)
  #rect(width: 155mm, fill: white, stroke: 0.5pt + border-light, radius: 4pt, inset: 5mm)[
    #set align(left)
    #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 8.5pt, fill: slate-mid)
    *Lưu ý Học thuật & Bản quyền:* Nguyên tác tiếng Anh *Neuromancer* thuộc bản quyền của nhà văn William Gibson (xuất bản lần đầu năm 1984 bởi Ace Books). Ấn bản song ngữ và hệ thống học liệu ngôn ngữ CEFR C1/C2 này được biên soạn từ kho tư liệu văn bản trong dự án phục vụ mục đích nghiên cứu văn học, dịch thuật đối chiếu và học tập học thuật.
  ]
]
#pagebreak()

// Table of Contents
#heading(level: 1, outlined: false)[MỤC LỤC TỔNG QUÁT • TABLE OF CONTENTS]
#v(2mm)
#block[
  #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 9pt)
  #outline(title: none, indent: 1.2em, depth: 2)
]
#pagebreak()
"""
    )

    # Front Matter Guide
    lines.append("#heading(level: 1)[DẪN LUẬN & CẨM NANG CHINH PHỤC CHUẨN C1/C2]\n")
    for sec in front["preface_sections"]:
        lines.append(f"#heading(level: 2, outlined: false)[{typst_escape_plain(sec['heading'])}]\n")
        for p in sec["paragraphs"]:
            lines.append(f"{typst_markup(p)}\n\n")

    # Exam Matrix Table
    lines.append(
        r"""
#block[
  #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 8.4pt)
  #set par(justify: false, leading: 0.55em)
  #table(
    columns: (20%, 22%, 29%, 29%),
    inset: 5pt,
    stroke: 0.45pt + border-light,
    fill: (x, y) => if y == 0 { navy } else if calc.odd(y) { bg-soft } else { white },
    table.header(
      [#text(fill: white, weight: "bold")[Kỳ thi]],
      [#text(fill: white, weight: "bold")[Điểm Mục tiêu (C1)]],
      [#text(fill: white, weight: "bold")[Yêu cầu Năng lực Cốt lõi]],
      [#text(fill: white, weight: "bold")[Thiết kế Hỗ trợ trong Sách]],
    ),
"""
    )
    for row in front["exam_matrix"]:
        lines.append(
            f"    [*{typst_escape_plain(row['exam'])}*\\ #text(size: 7.5pt, fill: cyan-accent)[CEFR {typst_escape_plain(row['cefr'])}]],"
            f"[{typst_escape_plain(row['target_score'])}],"
            f"[{typst_escape_plain(row['key_demands'])}],"
            f"[{typst_escape_plain(row['how_book_helps'])}],\n"
        )
    lines.append("  )\n]\n#v(4mm)\n")

    # 5-Step Protocol
    lines.append("#heading(level: 2, outlined: false)[3. Quy trình 5 Bước Tự học Song ngữ Hiệu suất Cao]\n")
    for st in front["study_protocol"]:
        lines.append(
            f"#block(fill: bg-soft, stroke: (left: 2.5pt + cyan-accent), inset: (left: 4mm, right: 3mm, top: 2.5mm, bottom: 2.5mm), width: 100%)[\n"
            f"  #text(font: (\"Be Vietnam Pro\", \"DejaVu Sans\"), size: 9.2pt, weight: \"bold\", fill: navy)[{typst_escape_plain(st['step'])}]\\ \n"
            f"  #text(size: 9.6pt)[{typst_markup(st['detail'])}]\n"
            f"]\n#v(1.5mm)\n"
        )

    # Foundational Lexicon
    lines.append("#heading(level: 2, outlined: false)[4. Từ điển Khái niệm Nền tảng Thế giới Neuromancer]\n")
    lines.append(
        r"""
#block[
  #set text(size: 8.8pt)
  #set par(justify: false, leading: 0.55em)
  #table(
    columns: (22%, 24%, 54%),
    inset: 5pt,
    stroke: 0.4pt + border-light,
    fill: (x, y) => if y == 0 { slate-dark } else if calc.odd(y) { bg-soft } else { white },
    table.header(
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Thuật ngữ Gốc & IPA]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Chuẩn Dịch Tiếng Việt]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Giải nghĩa Văn học & Kỹ thuật]],
    ),
"""
    )
    for lx in front["foundational_lexicon"]:
        lines.append(
            f"    [*{typst_escape_plain(lx['term'])}*\\ #text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 7.6pt, fill: slate-muted)[{typst_escape_plain(lx['ipa'])}]],"
            f"[*{typst_escape_plain(lx['vi'])}*],"
            f"[{typst_escape_plain(lx['note'])}],\n"
        )
    lines.append("  )\n]\n#pagebreak()\n")

    # Render Parts & Chapters
    seen_parts = set()
    all_vocab_index = []

    for ch_num in chapters_to_include:
        src = load_source_chapter(ch_num)
        vi_map = parse_vi_file(TRANS_DIR / f"ch{ch_num:02d}.vi.txt")
        study = load_study_dossier(ch_num)

        # Part Banner if entering a new Part
        if src["part_num"] not in seen_parts:
            seen_parts.add(src["part_num"])
            lines.append(
                f"""
#v(28mm)
#align(center)[
  #rect(width: 100%, fill: navy, radius: 5pt, inset: 12mm)[
    #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white)
    #text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 9pt, fill: cyan-bright, tracking: 2pt)[NEUROMANCER • WILLIAM GIBSON]
    #v(4mm)
    #heading(level: 1, outlined: true)[#text(fill: white, size: 19pt)[{typst_escape_plain(src['part_title_en'])}]]
    #v(2mm)
    #text(size: 13pt, fill: amber-bright, weight: "semibold")[{typst_escape_plain(src['part_title_vi'])}]
  ]
]
#pagebreak()
"""
            )

        ch_heading_en = f"CHAPTER {ch_num}"
        ch_heading_vi = f"CHƯƠNG {ch_num}: {study['chapter_title_vi']}"
        lines.append(
            f"""
#heading(level: 2, outlined: true)[{typst_escape_plain(ch_heading_en)} — {typst_escape_plain(ch_heading_vi)}]
#block(fill: bg-soft, stroke: 0.4pt + border-light, radius: 3pt, inset: 3.5mm, width: 100%)[
  #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 8.4pt, fill: slate-mid)
  *Tổng quan Chương {ch_num} ({src['paragraph_count']} đoạn • {src['word_count']:,} từ gốc):* {typst_markup(study['chapter_summary_vi'])}
]
#v(2mm)
"""
        )

        # Parallel Two-Column Lockstep Table
        lines.append(
            r"""
#block[
  #set par(justify: true, leading: 0.60em)
  #table(
    columns: (1fr, 1fr),
    inset: (x: 5pt, y: 4.5pt),
    stroke: (x, y) => (
      left: if x == 1 { 0.45pt + border-light } else { none },
      bottom: if y == 0 { 0.8pt + cyan-accent } else { 0.25pt + rgb("#E2E8F0") },
      top: none,
      right: none,
    ),
    table.header(
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 8pt, weight: "bold", fill: cyan-accent)[ORIGINAL ENGLISH TEXT]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), size: 8pt, weight: "bold", fill: amber-accent)[BẢN DỊCH VĂN HỌC TIẾNG VIỆT]],
    ),
"""
        )

        for p in src["paragraphs"]:
            idx = p["index"]
            anchor = f"{ch_num:02d}·{idx:03d}"
            en_typ = typst_markup(p["en"])
            vi_typ = typst_markup(vi_map[idx])
            lines.append(
                f"    [#text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 6.8pt, fill: slate-muted)[{anchor}] #h(2pt) {en_typ}],\n"
                f"    [#text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 6.8pt, fill: slate-muted)[{anchor}] #h(2pt) {vi_typ}],\n"
            )

        lines.append("  )\n]\n#v(5mm)\n")

        # End-of-Chapter C1/C2 Mastery Dossier
        lines.append(
            f"""
#block(fill: navy, radius: 3pt, inset: (x: 4mm, y: 3mm), width: 100%, breakable: false)[
  #set text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white)
  #grid(
    columns: (1fr, auto),
    align(left)[#text(size: 10.5pt, weight: "bold")[HỒ SƠ TINH THÔNG NGÔN NGỮ C1/C2 — CHƯƠNG {ch_num}]],
    align(right)[#text(font: ("JetBrains Mono", "DejaVu Sans Mono"), size: 8pt, fill: amber-bright)[TOEFL 90/5.0 • IELTS 7.0 • PTE 65 • CAM 185 • DET 120]]
  )
]
#v(2mm)
#heading(level: 3, outlined: false)[A. Từ vựng Học thuật & Văn chương Trọng tâm (C1–C2 Lexical Spotlight)]
#block[
  #set text(size: 8.6pt)
  #set par(justify: false, leading: 0.55em)
  #table(
    columns: (24%, 34%, 42%),
    inset: 5pt,
    stroke: 0.4pt + border-light,
    fill: (x, y) => if y == 0 { slate-dark } else if calc.odd(y) { bg-soft } else { white },
    table.header(
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Từ vựng • IPA • CEFR]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Nghĩa Tiếng Việt & Sắc thái C1/C2]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Collocations & Ứng dụng Thi Quốc tế]],
    ),
"""
        )

        for v in study["vocabulary"]:
            all_vocab_index.append(
                {
                    "term": v["term"],
                    "ipa": v["ipa"],
                    "pos": v["pos"],
                    "cefr": v["cefr"],
                    "meaning_vi": v["meaning_vi"],
                    "chapter": ch_num,
                }
            )
            qref = f" [{v['quote_id']}]" if v.get("quote_id") else ""
            lines.append(
                f"    [*{typst_escape_plain(v['term'])}* ({typst_escape_plain(v['pos'])})\\ "
                f"#text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 7.4pt, fill: slate-muted)[{typst_escape_plain(v['ipa'])}]\\ "
                f"#text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 7.2pt, weight: \"bold\", fill: cyan-accent)[{typst_escape_plain(v['cefr'])}{typst_escape_plain(qref)}]],"
                f"[*{typst_escape_plain(v['meaning_vi'])}*\\ {typst_markup(v['nuance_vi'])}],"
                f"[{typst_markup(v['collocations'])}],\n"
            )
        lines.append("  )\n]\n#v(3mm)\n")

        # Syntax & Discourse Notes
        lines.append("#heading(level: 3, outlined: false)[B. Giải phẫu Cú pháp, Ẩn dụ & Chuyển đổi Văn phong Học thuật]\n")
        for idx_s, syn in enumerate(study["syntax_notes"], 1):
            lines.append(
                f"#block(fill: bg-study, stroke: (left: 2.5pt + amber-accent), inset: 3.5mm, radius: 2pt, width: 100%)[\n"
                f"  #set par(justify: false, leading: 0.58em)\n"
                f"  #text(font: (\"Be Vietnam Pro\", \"DejaVu Sans\"), size: 9pt, weight: \"bold\", fill: navy)[{idx_s}. {typst_escape_plain(syn['feature'])}]\n"
                f"  #v(1mm)\n"
                f"  #text(size: 9pt, style: \"italic\", fill: slate-dark)[\"{typst_markup(syn['quote_en'])}\"]\n"
                f"  #v(1mm)\n"
                f"  #text(size: 8.9pt)[*Phân tích:* {typst_markup(syn['analysis_vi'])}]\n"
                f"  #v(1mm)\n"
                f"  #text(size: 8.8pt, fill: emerald-accent)[*Ứng dụng C1/C2:* {typst_markup(syn['exam_transfer_vi'])}]\n"
                f"]\n#v(2mm)\n"
            )

        # Multi-Exam Practice Drills & Answer Key
        lines.append("#heading(level: 3, outlined: false)[C. Bài tập Thực chiến Đa Kỳ Thi & Đáp án Phân tích]\n")
        for idx_d, dr in enumerate(study["exam_drills"], 1):
            lines.append(
                f"#block(fill: white, stroke: 0.45pt + border-light, inset: 3.5mm, radius: 3pt, width: 100%)[\n"
                f"  #set par(justify: false, leading: 0.58em)\n"
                f"  #text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 7.8pt, weight: \"bold\", fill: cyan-accent)[BÀI {idx_d} • {typst_escape_plain(dr['exam_tag'])}]\n"
                f"  #v(1mm)\n"
                f"  #text(size: 9.2pt, weight: \"semibold\")[{typst_markup(dr['prompt'])}]\n"
                f"  #v(1.5mm)\n"
                f"  #line(length: 100%, stroke: 0.3pt + border-light)\n"
                f"  #v(1mm)\n"
                f"  #text(size: 8.7pt, fill: slate-dark)[*Đáp án & Hướng dẫn Chấm điểm C1:* {typst_markup(dr['answer_and_explanation'])}]\n"
                f"]\n#v(2mm)\n"
            )

        lines.append("#pagebreak()\n")

    # Back Matter: Consolidated Master Vocabulary Index
    if all_vocab_index:
        all_vocab_sorted = sorted(all_vocab_index, key=lambda x: x["term"].lower())
        lines.append(
            f"""
#heading(level: 1, outlined: true)[PHỤ LỤC I — TỔNG MỤC LỤC TỪ VỰNG C1–C2 TOÀN TÁC PHẨM ({len(all_vocab_sorted)} MỤC TỪ)]
#text(size: 9.4pt, fill: slate-mid)[Bảng tra cứu theo thứ tự bảng chữ cái A–Z toàn bộ hệ thống từ vựng học thuật, văn chương và thành ngữ nâng cao được tuyển chọn xuyên suốt các chương.]
#v(3mm)
#block[
  #set text(size: 8.3pt)
  #set par(justify: false, leading: 0.52em)
  #table(
    columns: (25%, 18%, 10%, 37%, 10%),
    inset: 4.5pt,
    stroke: 0.35pt + border-light,
    fill: (x, y) => if y == 0 { navy } else if calc.odd(y) { bg-soft } else { white },
    table.header(
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Mục từ (Headword)]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Phiên âm IPA]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[CEFR]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Nghĩa Tinh tuyển Tiếng Việt]],
      [#text(font: ("Be Vietnam Pro", "DejaVu Sans"), fill: white, weight: "bold")[Chương]],
    ),
"""
        )
        for item in all_vocab_sorted:
            lines.append(
                f"    [*{typst_escape_plain(item['term'])}* ({typst_escape_plain(item['pos'])})],"
                f"[#text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 7.4pt)[{typst_escape_plain(item['ipa'])}]],"
                f"[#text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 7.4pt, fill: cyan-accent, weight: \"bold\")[{typst_escape_plain(item['cefr'])}]],"
                f"[{typst_escape_plain(item['meaning_vi'])}],"
                f"[Ch. {item['chapter']:02d}],\n"
            )
        lines.append("  )\n]\n")

    # Back Matter Capstone Exam Pack (if present)
    if back:
        lines.append("#pagebreak()\n")
        lines.append(f"#heading(level: 1, outlined: true)[{typst_escape_plain(back['title'])}]\n")
        lines.append(f"{typst_markup(back['intro'])}\n#v(3mm)\n")
        for sec in back["sections"]:
            lines.append(f"#heading(level: 2, outlined: true)[{typst_escape_plain(sec['heading'])}]\n")
            lines.append(f"{typst_markup(sec['overview'])}\n#v(2mm)\n")
            for task in sec["tasks"]:
                lines.append(
                    f"#block(fill: bg-soft, stroke: 0.45pt + border-light, inset: 4mm, radius: 3pt, width: 100%)[\n"
                    f"  #set par(justify: false, leading: 0.60em)\n"
                    f"  #text(font: (\"JetBrains Mono\", \"DejaVu Sans Mono\"), size: 8pt, weight: \"bold\", fill: cyan-accent)[{typst_escape_plain(task['badge'])}]\n"
                    f"  #v(1.5mm)\n"
                    f"  #text(size: 9.4pt, weight: \"semibold\")[{typst_markup(task['prompt'])}]\n"
                    f"  #v(2mm)\n"
                    f"  #line(length: 100%, stroke: 0.35pt + border-light)\n"
                    f"  #v(1.5mm)\n"
                    f"  #text(size: 9pt)[*Bài mẫu / Đáp án Chuẩn C1–C2:* {typst_markup(task['model_response'])}]\n"
                    f"]\n#v(3mm)\n"
                )

    return "".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=str(ROOT / "build" / "neuromancer_preview.pdf"),
        help="Output PDF file path",
    )
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="Fail unless all 24 chapters are present and verified",
    )
    parser.add_argument(
        "--render-samples",
        action="store_true",
        help="Render sample PNG pages into build/preview/ for visual QA",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    completed = sorted(
        int(p.stem[2:4]) for p in TRANS_DIR.glob("ch*.vi.txt") if p.stem[2:4].isdigit()
    )

    if args.require_complete and completed != list(range(1, 25)):
        missing = sorted(set(range(1, 25)) - set(completed))
        print(f"ERROR: --require-complete specified, missing chapters: {missing}")
        sys.exit(1)

    is_complete = completed == list(range(1, 25))
    build_dir = ROOT / "build"
    build_dir.mkdir(parents=True, exist_ok=True)

    typ_source = generate_typst_source(completed, is_complete=is_complete)
    typ_path = build_dir / "edition.typ"
    typ_path.write_text(typ_source, encoding="utf-8")

    out_pdf = Path(args.output)
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    font_dirs = collect_font_dirs()
    typst.compile(str(typ_path), output=str(out_pdf), font_paths=font_dirs)

    # Post-compile PDF QA via PyMuPDF
    doc = pymupdf.open(str(out_pdf))
    toc = doc.get_toc()
    bad_glyph_pages = []
    for pno in range(len(doc)):
        txt = doc[pno].get_text("text")
        if "\ufffd" in txt:
            bad_glyph_pages.append(pno + 1)

    size_mb = out_pdf.stat().st_size / (1024 * 1024)
    print(
        f"Compiled PDF: {out_pdf} | Pages: {len(doc)} | Size: {size_mb:.2f} MB | "
        f"TOC entries: {len(toc)} | Chapters: {len(completed)}/24"
    )
    if bad_glyph_pages:
        print(f"ERROR: Found replacement character U+FFFD on pages: {bad_glyph_pages}")
        sys.exit(1)

    if args.render_samples:
        prev_dir = build_dir / "preview"
        prev_dir.mkdir(parents=True, exist_ok=True)
        sample_pages = sorted({0, 1, 2, 3, min(5, len(doc) - 1), len(doc) - 1})
        for idx in sample_pages:
            pix = doc[idx].get_pixmap(dpi=140)
            png_path = prev_dir / f"page_{idx+1:04d}.png"
            pix.save(str(png_path))
        print(f"Rendered {len(sample_pages)} preview PNGs to {prev_dir}")


if __name__ == "__main__":
    main()
