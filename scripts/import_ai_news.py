#!/usr/bin/env python3
"""Import daily AI news MD files from external source into Hugo content/ai-news/.

Usage:
  python3 scripts/import_ai_news.py            # import all files
  python3 scripts/import_ai_news.py 2026-05-04 # import specific date
  python3 scripts/import_ai_news.py --force     # overwrite existing files

Source: /Volumes/ORICO2/张咋了AI资讯/{date}.md
Dest:   content/ai-news/{date}/index.zh.md
"""

import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

SOURCE_DIR = Path("/Volumes/ORICO2/张咋了AI资讯")
DEST_DIR = Path(__file__).parent.parent / "content" / "ai-news"
SKIP_FILES = {"README.md", "latest.md", "信息源清单.md"}
GRADIENTS = ["gradient-1", "gradient-2", "gradient-3", "gradient-4"]


def extract_summary(content: str) -> str:
    """Extract first item from 今日3点 section as summary."""
    m = re.search(r"## 今日3点\s*\n\n1\.\s+(.+?)(?=\n2\.|\n\n)", content, re.DOTALL)
    if m:
        s = re.sub(r"\s+", " ", m.group(1)).strip()
        if len(s) > 120:
            s = s[:120] + "…"
        return s
    return ""


def import_file(src: Path, force: bool = False) -> Optional[Path]:
    date_str = src.stem  # e.g., 2026-05-04
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

    out_path = DEST_DIR / date_str / "index.zh.md"
    if out_path.exists() and not force:
        print(f"  skip (exists): {out_path.relative_to(DEST_DIR.parent.parent)}")
        return None

    content = src.read_text(encoding="utf-8")

    # Extract title from first H1
    m = re.match(r"^#\s+(.+)", content, re.MULTILINE)
    title = m.group(1).strip() if m else f"AI 资讯 {date_str}"

    summary = extract_summary(content)
    cover = GRADIENTS[dt.day % 4]

    # Remove first H1 (Hugo uses title from front matter)
    body = re.sub(r"^#[^\n]+\n+", "", content, count=1)

    # Escape quotes in summary for YAML inline string
    summary_escaped = summary.replace('"', '\\"')

    front_matter = f"""---
title: "{title}"
date: {date_str}
tags: [AI资讯]
cover: {cover}
summary: "{summary_escaped}"
---

"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(front_matter + body, encoding="utf-8")
    return out_path


def main():
    if not SOURCE_DIR.exists():
        print(f"Error: {SOURCE_DIR} not found. Is the drive mounted?")
        sys.exit(1)

    force = "--force" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if args:
        files = [SOURCE_DIR / f"{args[0]}.md"]
    else:
        files = sorted(SOURCE_DIR.glob("*.md"))

    DEST_DIR.mkdir(parents=True, exist_ok=True)

    count = 0
    for f in files:
        if not f.exists():
            print(f"Not found: {f}")
            continue
        if f.name in SKIP_FILES:
            continue
        result = import_file(f, force=force)
        if result:
            print(f"  ✓ {result.relative_to(DEST_DIR.parent.parent)}")
            count += 1

    print(f"\nDone: imported {count} file(s) → {DEST_DIR.relative_to(DEST_DIR.parent.parent)}/")


if __name__ == "__main__":
    main()
