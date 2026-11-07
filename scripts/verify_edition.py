#!/usr/bin/env python3
"""
Automated QA verifier for the Neuromancer English-Vietnamese C1/C2 Bilingual Edition.
Checks:
  1. Exact 1-to-1 paragraph alignment (not 1 missing, not 1 extra)
  2. Non-empty translations, balanced '*...*' emphasis markers, Vietnamese diacritics
  3. Length-ratio sanity checks to catch accidental truncations or merges
  4. Pedagogical C1/C2 Study Dossier schema & completeness
"""

import argparse
import re
import sys
from pathlib import Path

from edition_utils import (
    PEDAGOGY_DIR,
    ROOT,
    TRANS_DIR,
    VI_DIACRITIC_RE,
    load_manifest,
    load_source_chapter,
    load_study_dossier,
    parse_vi_file,
)

# Short proper nouns, timecodes, or international interjections allowed to lack Vietnamese diacritics
ALLOWED_NO_DIACRITIC_PATTERNS = re.compile(
    r'^[\W\d_A-Za-z]*$|^"?(Case|Molly|Armitage|Maelcum|Aerol|Ratz|Linda|Hideo|Wintermute|'
    r'Neuromancer|Riviera|Dixie|Zion|Babylon|Hosaka|Ono-Sendai|Sense/Net|Straylight|'
    r'Freeside|Braun|Corto|Deane|Lupus|3Jane|Marie-France|OK|Okay|Uh-huh|Hmm|12:06:26)[.!?\s"]*\*?$',
    re.I,
)


def verify_chapter(ch_num: int, strict_ratio: bool = True) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []

    src = load_source_chapter(ch_num)
    vi_path = TRANS_DIR / f"ch{ch_num:02d}.vi.txt"
    study_path = PEDAGOGY_DIR / f"ch{ch_num:02d}.study.json"

    if not vi_path.exists():
        errors.append(f"Ch {ch_num:02d}: Missing translation file {vi_path}")
        return errors

    try:
        vi_map = parse_vi_file(vi_path)
    except Exception as exc:
        errors.append(f"Ch {ch_num:02d}: Parse error in {vi_path.name}: {exc}")
        return errors

    expected_indices = [p["index"] for p in src["paragraphs"]]
    actual_indices = sorted(vi_map.keys())

    missing = sorted(set(expected_indices) - set(actual_indices))
    extra = sorted(set(actual_indices) - set(expected_indices))
    if missing:
        errors.append(f"Ch {ch_num:02d}: Missing paragraph indices: {missing[:15]}")
    if extra:
        errors.append(f"Ch {ch_num:02d}: Extra unexpected paragraph indices: {extra[:15]}")

    diacritic_paras = 0
    for p in src["paragraphs"]:
        idx = p["index"]
        en = p["en"]
        vi = vi_map.get(idx, "").strip()
        if not vi:
            errors.append(f"Ch {ch_num:02d} [{idx:03d}]: Empty Vietnamese translation")
            continue

        # Balanced '*' italics check
        if vi.count("*") % 2 != 0:
            errors.append(f"Ch {ch_num:02d} [{idx:03d}]: Unbalanced '*' emphasis in VI: {vi[:80]}")

        # Disallow stray CJK / Hangul / Cyrillic characters in Vietnamese text
        if re.search(r"[\u0400-\u04FF\u3040-\u30FF\u4E00-\u9FFF\uAC00-\uD7AF]", vi):
            errors.append(f"Ch {ch_num:02d} [{idx:03d}]: Stray non-Latin/VI script character in VI: {vi[:80]}")

        if VI_DIACRITIC_RE.search(vi):
            diacritic_paras += 1
        elif len(en.split()) >= 5:
            errors.append(
                f"Ch {ch_num:02d} [{idx:03d}]: Paragraph >=5 words has NO Vietnamese diacritics: {vi[:80]}"
            )

        # Length ratio sanity check for substantial paragraphs (>= 20 words)
        if strict_ratio and p["word_count"] >= 20:
            ratio = len(vi) / max(len(en), 1)
            if ratio < 0.55 or ratio > 2.40:
                warnings.append(
                    f"Ch {ch_num:02d} [{idx:03d}]: Unusual VI/EN char ratio {ratio:.2f} "
                    f"(EN={len(en)} chars, VI={len(vi)} chars)"
                )

    if diacritic_paras / max(len(expected_indices), 1) < 0.85:
        errors.append(
            f"Ch {ch_num:02d}: Too few paragraphs with Vietnamese diacritics "
            f"({diacritic_paras}/{len(expected_indices)})"
        )

    # Verify Study Dossier
    if not study_path.exists():
        errors.append(f"Ch {ch_num:02d}: Missing C1/C2 study dossier {study_path}")
    else:
        try:
            st = load_study_dossier(ch_num)
        except Exception as exc:
            errors.append(f"Ch {ch_num:02d}: Invalid JSON in {study_path.name}: {exc}")
            return errors

        for req_key in ("chapter_title_vi", "chapter_summary_vi", "vocabulary", "syntax_notes", "exam_drills"):
            if req_key not in st or not st[req_key]:
                errors.append(f"Ch {ch_num:02d} study dossier: Missing or empty '{req_key}'")

        vocab = st.get("vocabulary", [])
        if len(vocab) < 8:
            errors.append(f"Ch {ch_num:02d} study dossier: Expected >=8 vocabulary items, got {len(vocab)}")
        for i, v in enumerate(vocab):
            for vk in ("term", "ipa", "pos", "cefr", "meaning_vi", "nuance_vi", "collocations"):
                if not v.get(vk):
                    errors.append(f"Ch {ch_num:02d} vocab[{i}] ({v.get('term','?')}): missing '{vk}'")

        syntax = st.get("syntax_notes", [])
        if len(syntax) < 2:
            errors.append(f"Ch {ch_num:02d} study dossier: Expected >=2 syntax_notes, got {len(syntax)}")

        drills = st.get("exam_drills", [])
        if len(drills) < 3:
            errors.append(f"Ch {ch_num:02d} study dossier: Expected >=3 exam_drills, got {len(drills)}")

    for w in warnings:
        print(f"  [WARN] {w}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapters", nargs="*", type=int, help="Chapter numbers to verify")
    parser.add_argument("--all", action="store_true", help="Verify all 24 chapters")
    parser.add_argument("--completed", action="store_true", help="Verify all chapters present in data/translations/")
    args = parser.parse_args()

    manifest = load_manifest()
    if args.all:
        targets = list(range(1, manifest["total_chapters"] + 1))
    elif args.completed:
        targets = sorted(
            int(p.stem[2:4]) for p in TRANS_DIR.glob("ch*.vi.txt") if p.stem[2:4].isdigit()
        )
        if not targets:
            print("No completed chapters found yet.")
            return
    else:
        targets = args.chapters

    if not targets:
        print("Specify chapter numbers, --completed, or --all")
        sys.exit(1)

    all_errors: list[str] = []
    total_paras = 0
    total_words_en = 0
    total_words_vi = 0

    for ch_num in targets:
        errs = verify_chapter(ch_num)
        all_errors.extend(errs)
        if not errs:
            src = load_source_chapter(ch_num)
            vi_map = parse_vi_file(TRANS_DIR / f"ch{ch_num:02d}.vi.txt")
            st = load_study_dossier(ch_num)
            vi_words = sum(len(t.split()) for t in vi_map.values())
            total_paras += src["paragraph_count"]
            total_words_en += src["word_count"]
            total_words_vi += vi_words
            print(
                f"[PASS] Ch {ch_num:02d}: {src['paragraph_count']:3d} paras | "
                f"EN {src['word_count']:4d}w -> VI {vi_words:4d}w | "
                f"Vocab: {len(st['vocabulary'])}, Syntax: {len(st['syntax_notes'])}, Drills: {len(st['exam_drills'])}"
            )

    if all_errors:
        print("\n=== VERIFICATION FAILED ===")
        for e in all_errors:
            print("  [ERROR]", e)
        sys.exit(1)

    print(
        f"\nALL {len(targets)} VERIFIED CHAPTER(S) PASSED! "
        f"Total: {total_paras} paragraphs | {total_words_en:,} EN words -> {total_words_vi:,} VI words."
    )


if __name__ == "__main__":
    main()
