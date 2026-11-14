#!/usr/bin/env python3
"""food-picture-01 entry: copy the packaged food image to /output/entry.png (deterministic)."""
from __future__ import annotations

import os
import shutil
from pathlib import Path

OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SRC = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT / "entry.png")


if __name__ == "__main__":
    main()
