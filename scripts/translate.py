#!/usr/bin/env python3
"""Translate every source paragraph with resumable, context-aware MT units."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import ctranslate2
import pysbd
import sentencepiece as spm

MODEL_NAME = "quickmt/quickmt-en-vi"
MODEL_REVISION = "thiennq/quickmt-en-vi-ct2-int8:v1"
MODEL_LICENSE = "CC-BY-4.0"
MAX_UNIT_TOKENS = 320


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_vietnamese(text: str, english: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("▁", " ").replace("<unk>", "")
    text = re.sub(r"\s+", " ", text).strip()
    # Prevent two well-known domain errors without imposing a global style.
    if re.search(r"\b(?:ICE|ice)\b", english):
        text = re.sub(r"\bnước đá\b|\bbăng\b", "ICE", text, flags=re.IGNORECASE)
    if re.search(r"\bdeck\b", english, flags=re.IGNORECASE):
        text = re.sub(
            r"\bboong\b|\bbộ bài\b|\bcỗ bài\b", "deck", text, flags=re.IGNORECASE
        )
    if re.search(r"\bCase\b", english) and "Case" not in text:
        text = re.sub(r"\btrường hợp\b", "Case", text, flags=re.IGNORECASE)
    return text


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def split_oversize(text: str, source_sp: spm.SentencePieceProcessor) -> list[str]:
    if len(source_sp.encode(text, out_type=str)) <= MAX_UNIT_TOKENS:
        return [text]
    words = text.split()
    if len(words) < 2:
        return [text]
    midpoint = len(words) // 2
    # Prefer a clause boundary near the middle, while preserving all words.
    boundary_candidates = [
        index + 1
        for index, word in enumerate(words[:-1])
        if re.search(r"[,;:!?]$|[.][\"’']?$", word)
    ]
    if boundary_candidates:
        midpoint = min(boundary_candidates, key=lambda index: abs(index - midpoint))
    left = " ".join(words[:midpoint])
    right = " ".join(words[midpoint:])
    return split_oversize(left, source_sp) + split_oversize(right, source_sp)


def paragraph_units(
    paragraph: dict, segmenter: pysbd.Segmenter, source_sp: spm.SentencePieceProcessor
) -> list[dict]:
    english = paragraph["en"]
    sentences = [item.strip() for item in segmenter.segment(english) if item.strip()]
    reconstructed = re.sub(r"\s+", " ", " ".join(sentences)).strip()
    if reconstructed != english.strip():
        sentences = [english.strip()]
    pieces: list[str] = []
    for sentence in sentences:
        pieces.extend(split_oversize(sentence, source_sp))
    packed: list[str] = []
    current = ""
    for piece in pieces:
        candidate = f"{current} {piece}".strip()
        if current and len(source_sp.encode(candidate, out_type=str)) > MAX_UNIT_TOKENS:
            packed.append(current)
            current = piece
        else:
            current = candidate
    if current:
        packed.append(current)
    if re.sub(r"\s+", " ", " ".join(packed)).strip() != english.strip():
        raise ValueError(f"Unit segmentation lost source text in {paragraph['id']}")
    return [
        {
            "id": f"{paragraph['id']}-u{index:03d}",
            "paragraph_id": paragraph["id"],
            "en": unit,
            "en_sha256": text_hash(unit),
        }
        for index, unit in enumerate(packed, start=1)
    ]


def load_checkpoint(path: Path) -> dict:
    records: dict[str, dict] = {}
    if not path.exists():
        return records
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
                records[record["id"]] = record
            except (json.JSONDecodeError, KeyError) as error:
                raise ValueError(f"Invalid checkpoint line {line_number}: {error}") from error
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("build/source.json"))
    parser.add_argument(
        "--model", type=Path, default=Path(".cache/quickmt-en-vi-ct2-int8")
    )
    parser.add_argument("--output", type=Path, default=Path("translation/vi.json"))
    parser.add_argument(
        "--checkpoint", type=Path, default=Path("build/translation-units.jsonl")
    )
    parser.add_argument(
        "--overrides", type=Path, default=Path("translation/overrides.json")
    )
    parser.add_argument("--chapters", type=int, nargs="*")
    parser.add_argument("--limit-paragraphs", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=12)
    parser.add_argument("--beam-size", type=int, default=4)
    args = parser.parse_args()

    started = time.monotonic()
    source = json.loads(args.source.read_text(encoding="utf-8"))
    overrides = json.loads(args.overrides.read_text(encoding="utf-8"))["paragraphs"]
    known_ids = {
        paragraph["id"]
        for chapter in source["chapters"]
        for paragraph in chapter["paragraphs"]
    }
    unknown_overrides = set(overrides) - known_ids
    if unknown_overrides:
        raise ValueError(f"Unknown override IDs: {sorted(unknown_overrides)}")

    existing_paragraphs: dict[str, dict] = {}
    if args.output.exists():
        existing = json.loads(args.output.read_text(encoding="utf-8"))
        if existing.get("source_sha256") != source["source_sha256"]:
            raise ValueError("Existing translation belongs to a different EPUB")
        existing_paragraphs = existing.get("paragraphs", {})
    checkpoint = load_checkpoint(args.checkpoint)
    checkpoint.parent.mkdir(parents=True, exist_ok=True)

    print(f"Loading {MODEL_REVISION} from {args.model}", flush=True)
    source_sp = spm.SentencePieceProcessor(model_file=str(args.model / "src.spm.model"))
    target_sp = spm.SentencePieceProcessor(model_file=str(args.model / "tgt.spm.model"))
    translator = ctranslate2.Translator(
        str(args.model),
        device="cpu",
        compute_type="int8",
        inter_threads=int(os.environ.get("CT2_INTER_THREADS", "1")),
        intra_threads=int(os.environ.get("CT2_INTRA_THREADS", "2")),
    )
    segmenter = pysbd.Segmenter(language="en", clean=False)
    paragraphs_done = 0
    translated_units = 0

    def valid_existing(paragraph: dict) -> bool:
        record = existing_paragraphs.get(paragraph["id"], {})
        if paragraph["id"] in overrides:
            return (
                record.get("en_sha256") == text_hash(paragraph["en"])
                and record.get("status") == "human-reviewed"
                and record.get("vi") == overrides[paragraph["id"]].strip()
            )
        return (
            record.get("en_sha256") == text_hash(paragraph["en"])
            and bool(record.get("vi", "").strip())
        )

    def write_output() -> None:
        completed = sum(
            1
            for chapter in source["chapters"]
            for paragraph in chapter["paragraphs"]
            if valid_existing(paragraph)
        )
        data = {
            "schema": "neuromancer-translation/v1",
            "language": "vi-VN",
            "source_sha256": source["source_sha256"],
            "model": MODEL_NAME,
            "model_revision": MODEL_REVISION,
            "model_license": MODEL_LICENSE,
            "decoding": {
                "beam_size": args.beam_size,
                "max_unit_sentencepiece_tokens": MAX_UNIT_TOKENS,
                "compute_type": "int8",
            },
            "status": "machine-assisted draft with explicitly marked human overrides",
            "generated_utc": datetime.now(timezone.utc).isoformat(),
            "completed_paragraphs": completed,
            "total_paragraphs": source["paragraph_count"],
            "paragraphs": dict(sorted(existing_paragraphs.items())),
        }
        atomic_json(args.output, data)

    with args.checkpoint.open("a", encoding="utf-8") as checkpoint_handle:
        for chapter in source["chapters"]:
            if args.chapters and chapter["number"] not in args.chapters:
                continue
            chapter_paragraphs = chapter["paragraphs"]
            if args.limit_paragraphs:
                remaining = args.limit_paragraphs - paragraphs_done
                if remaining <= 0:
                    break
                chapter_paragraphs = chapter_paragraphs[:remaining]
            pending_paragraphs = [
                paragraph for paragraph in chapter_paragraphs if not valid_existing(paragraph)
            ]
            print(
                f"Chapter {chapter['number']:02d}: {len(chapter_paragraphs)} paragraphs; "
                f"{len(pending_paragraphs)} pending",
                flush=True,
            )
            if not pending_paragraphs:
                paragraphs_done += len(chapter_paragraphs)
                continue

            chapter_units: dict[str, list[dict]] = {}
            pending_units: list[dict] = []
            unit_to_paragraph: dict[str, str] = {}
            for paragraph in pending_paragraphs:
                units = paragraph_units(paragraph, segmenter, source_sp)
                chapter_units[paragraph["id"]] = units
                for unit in units:
                    unit_to_paragraph[unit["id"]] = paragraph["id"]
                    cached = checkpoint.get(unit["id"], {})
                    if cached.get("en_sha256") != unit["en_sha256"] or not cached.get("vi"):
                        pending_units.append(unit)

            for offset in range(0, len(pending_units), args.batch_size):
                batch = pending_units[offset : offset + args.batch_size]
                encoded = [source_sp.encode(unit["en"], out_type=str) for unit in batch]
                results = translator.translate_batch(
                    encoded,
                    beam_size=args.beam_size,
                    max_decoding_length=512,
                    max_batch_size=args.batch_size,
                )
                for unit, result in zip(batch, results, strict=True):
                    vietnamese = clean_vietnamese(
                        target_sp.decode(result.hypotheses[0]), unit["en"]
                    )
                    if not vietnamese:
                        raise ValueError(f"Empty model output for {unit['id']}")
                    record = {
                        "id": unit["id"],
                        "paragraph_id": unit["paragraph_id"],
                        "en_sha256": unit["en_sha256"],
                        "vi": vietnamese,
                    }
                    checkpoint[unit["id"]] = record
                    checkpoint_handle.write(
                        json.dumps(record, ensure_ascii=False) + "\n"
                    )
                checkpoint_handle.flush()
                translated_units += len(batch)
                if translated_units % 120 < args.batch_size:
                    elapsed = max(time.monotonic() - started, 0.001)
                    print(
                        f"  {translated_units} new units; {translated_units / elapsed:.2f} units/s",
                        flush=True,
                    )

            for paragraph in pending_paragraphs:
                if paragraph["id"] in overrides:
                    existing_paragraphs[paragraph["id"]] = {
                        "vi": overrides[paragraph["id"]].strip(),
                        "en_sha256": text_hash(paragraph["en"]),
                        "status": "human-reviewed",
                        "unit_count": 0,
                    }
                    continue
                units = chapter_units[paragraph["id"]]
                translations = []
                for unit in units:
                    record = checkpoint.get(unit["id"], {})
                    if record.get("en_sha256") != unit["en_sha256"] or not record.get("vi"):
                        raise ValueError(f"Missing checkpoint translation for {unit['id']}")
                    translations.append(record["vi"])
                existing_paragraphs[paragraph["id"]] = {
                    "vi": " ".join(translations),
                    "en_sha256": text_hash(paragraph["en"]),
                    "status": "machine-draft",
                    "unit_count": len(units),
                }
            paragraphs_done += len(chapter_paragraphs)
            write_output()
            print(f"  checkpoint saved: {args.output}", flush=True)

    write_output()
    elapsed = time.monotonic() - started
    print(
        f"Translation pass complete: {len(existing_paragraphs)} paragraphs, "
        f"{translated_units} new units, {elapsed:.1f} seconds.",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
