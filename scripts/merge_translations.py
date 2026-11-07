#!/usr/bin/env python3
"""Merge the six independently resumable chapter-group translation artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("build/source.json"))
    parser.add_argument("--groups", type=Path, default=Path("build/groups"))
    parser.add_argument("--output", type=Path, default=Path("translation/vi.json"))
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8"))
    files = sorted(args.groups.glob("**/vi-group-*.json"))
    if len(files) != 6:
        raise ValueError(f"Expected six translation groups, found {len(files)}: {files}")
    paragraphs: dict[str, dict] = {}
    metadata = None
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("source_sha256") != source["source_sha256"]:
            raise ValueError(f"Source hash mismatch in {path}")
        if metadata is None:
            metadata = data
        else:
            for key in ("model", "model_revision", "model_license", "decoding"):
                if data.get(key) != metadata.get(key):
                    raise ValueError(f"Metadata mismatch for {key} in {path}")
        for pid, record in data.get("paragraphs", {}).items():
            if pid in paragraphs:
                raise ValueError(f"Duplicate paragraph {pid} in {path}")
            paragraphs[pid] = record
    source_ids = {
        paragraph["id"]
        for chapter in source["chapters"]
        for paragraph in chapter["paragraphs"]
    }
    if set(paragraphs) != source_ids:
        missing = sorted(source_ids - set(paragraphs))
        extra = sorted(set(paragraphs) - source_ids)
        raise ValueError(f"Merged coverage mismatch; missing={missing[:10]}, extra={extra[:10]}")
    merged = {
        "schema": "neuromancer-translation/v1",
        "language": "vi-VN",
        "source_sha256": source["source_sha256"],
        "model": metadata["model"],
        "model_revision": metadata["model_revision"],
        "model_license": metadata["model_license"],
        "decoding": metadata["decoding"],
        "status": "machine-assisted draft with explicitly marked human overrides",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "completed_paragraphs": len(paragraphs),
        "total_paragraphs": source["paragraph_count"],
        "paragraphs": dict(sorted(paragraphs.items())),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Merged {len(files)} groups into {len(paragraphs)} paragraphs: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
