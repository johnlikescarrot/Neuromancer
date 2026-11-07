#!/usr/bin/env python3
"""Download and verify the CC BY 4.0 QuickMT English–Vietnamese model."""

from __future__ import annotations

import argparse
import hashlib
import sys
import time
import urllib.request
from pathlib import Path

RELEASE = (
    "https://github.com/thiennq/quickmt-en-vi-ct2-int8/"
    "releases/download/v1/"
)
FILES = {
    "model.bin": (
        206686329,
        "81f2be8df576c8c28505a71466f45db172aebbf74b64b05045321dc308d023a0",
    ),
    "config.json": (
        223,
        "66edc5d58ceb812a41b4b784497001f815c35400884f40984b19de29e1bc3d69",
    ),
    "source_vocabulary.json": (
        335066,
        "6742782136af6e207fb86f650f60a556f187ab18e9da405b22dec7b45384a2a5",
    ),
    "target_vocabulary.json": (
        322073,
        "580d7293caa7cb66f4b427b5c929c17aec37396976ba0385c5124b512b65fd7a",
    ),
    "src.spm.model": (
        586058,
        "82efd76a945ec4574b2ab3d2476b0043a9737c8dbe693cd20a7fa036d273c0eb",
    ),
    "tgt.spm.model": (
        553521,
        "03be7f771990d2bee00d7ff09219baad95b53fef1dcd387b3048c156d665e046",
    ),
    # The release does not publish a checksum for NOTICE.txt; its required
    # attribution text is validated below after the exact byte-size check.
    "NOTICE.txt": (598, None),
}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def valid(path: Path, size: int, checksum: str | None) -> bool:
    if not path.exists() or path.stat().st_size != size:
        return False
    return checksum is None or digest(path) == checksum


def download(url: str, destination: Path) -> None:
    temporary = destination.with_suffix(destination.suffix + ".part")
    request = urllib.request.Request(url, headers={"User-Agent": "Neuromancer-Edition/1.0"})
    with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as out:
        while True:
            block = response.read(1024 * 1024)
            if not block:
                break
            out.write(block)
    temporary.replace(destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=Path(".cache/quickmt-en-vi-ct2-int8")
    )
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    for name, (size, checksum) in FILES.items():
        path = args.output / name
        if valid(path, size, checksum):
            print(f"Verified cached {name}", flush=True)
            continue
        expected_checksum = checksum
        for attempt in range(1, 4):
            try:
                print(f"Downloading {name} ({size:,} bytes), attempt {attempt}", flush=True)
                download(RELEASE + name, path)
                if path.stat().st_size != size:
                    raise ValueError(f"Wrong size for {name}: {path.stat().st_size}")
                actual = digest(path)
                if expected_checksum is not None and actual != expected_checksum:
                    raise ValueError(f"Wrong SHA-256 for {name}: {actual}")
                print(f"Verified {name}: {actual}", flush=True)
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(attempt * 3)
    notice = (args.output / "NOTICE.txt").read_text(encoding="utf-8")
    if "quickmt" not in notice.lower() or "CC BY 4.0" not in notice:
        raise ValueError("Unexpected model NOTICE.txt; refusing unattributed use")
    return 0


if __name__ == "__main__":
    sys.exit(main())
