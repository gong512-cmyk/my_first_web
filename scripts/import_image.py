#!/usr/bin/env python3
"""Copy an image into static/assets/images/<date>-pic/ for a Hugo post.

Prints the public path to paste into the post's `images:` front matter.

Usage:
    python3 scripts/import_image.py path/to/photo.jpg \
        --post diary-20260422 --date 2026-04-22

Optional --max-width N triggers macOS `sips -Z N` resize in place.
"""
import argparse
import datetime as dt
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATIC_IMAGES = REPO_ROOT / "static" / "assets" / "images"
CONTENT_POSTS = REPO_ROOT / "content" / "posts"


def resize_with_sips(path: Path, max_width: int) -> None:
    try:
        subprocess.run(
            ["sips", "-Z", str(max_width), str(path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("warn: sips not available or failed, keeping original size", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="path to source image")
    parser.add_argument("--post", required=True, help="post slug, e.g. diary-20260422")
    parser.add_argument(
        "--date",
        help="YYYY-MM-DD used as folder prefix; defaults to today",
    )
    parser.add_argument("--name", help="override destination filename (keeps extension)")
    parser.add_argument("--max-width", type=int, help="resize to max width via sips")
    args = parser.parse_args()

    src = Path(args.source).expanduser()
    if not src.is_file():
        parser.error(f"source not found: {src}")

    date_str = args.date or dt.date.today().isoformat()
    try:
        dt.date.fromisoformat(date_str)
    except ValueError:
        parser.error(f"invalid --date, expected YYYY-MM-DD: {date_str}")

    folder_name = f"{date_str.replace('-', '')}-pic"
    dest_dir = STATIC_IMAGES / folder_name
    dest_dir.mkdir(parents=True, exist_ok=True)

    filename = args.name or src.name
    if args.name and not Path(args.name).suffix:
        filename = args.name + src.suffix
    dest = dest_dir / filename
    shutil.copy2(src, dest)

    if args.max_width:
        resize_with_sips(dest, args.max_width)

    post_dir = CONTENT_POSTS / args.post
    if not post_dir.is_dir():
        print(
            f"warn: post bundle not found at {post_dir.relative_to(REPO_ROOT)}",
            file=sys.stderr,
        )

    public_path = f"/assets/images/{folder_name}/{filename}"
    print(f"copied: {dest.relative_to(REPO_ROOT)}")
    print(f"front matter path:\n  - {public_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
