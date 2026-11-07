#!/usr/bin/env python3
"""Shared utilities for parsing source chapters, Vietnamese translations, and C1 study dossiers."""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "data" / "source"
TRANS_DIR = ROOT / "data" / "translations"
PEDAGOGY_DIR = ROOT / "data" / "pedagogy"

VI_DIACRITIC_RE = re.compile(
    r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ"
    r"ÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]"
)


def load_manifest() -> dict:
    return json.loads((SOURCE_DIR / "manifest.json").read_text(encoding="utf-8"))


def load_source_chapter(ch_num: int) -> dict:
    return json.loads((SOURCE_DIR / f"ch{ch_num:02d}.json").read_text(encoding="utf-8"))


def parse_vi_file(path: Path) -> Dict[int, str]:
    """
    Parse a tagged Vietnamese translation file (`data/translations/chXX.vi.txt`).
    Format:
      [001] Vietnamese paragraph one...
      [002] Vietnamese paragraph two...
    Returns dict mapping 1-based paragraph index -> Vietnamese text.
    """
    entries: Dict[int, List[str]] = {}
    current_idx = None
    line_re = re.compile(r"^\[(\d{3,4})\]\s*(.*)$")

    for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        m = line_re.match(stripped)
        if m:
            idx = int(m.group(1))
            if idx in entries:
                raise ValueError(f"{path.name}:{line_no}: Duplicate paragraph index [{idx:03d}]")
            current_idx = idx
            entries[current_idx] = [m.group(2).strip()]
        else:
            if current_idx is None:
                raise ValueError(f"{path.name}:{line_no}: Unexpected line before first [NNN]: {stripped[:60]}")
            entries[current_idx].append(stripped)

    return {k: " ".join(v).strip() for k, v in entries.items()}


def load_study_dossier(ch_num: int) -> dict:
    p = PEDAGOGY_DIR / f"ch{ch_num:02d}.study.json"
    return json.loads(p.read_text(encoding="utf-8"))
