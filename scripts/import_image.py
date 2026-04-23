#!/usr/bin/env python3
import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
from pathlib import Path


def slugify(name: str) -> str:
    value = name.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "image"


def compress_with_sips(path: Path, max_width: int) -> None:
    # sips is available by default on macOS; if not found, keep original size.
    try:
        subprocess.run([
            "sips",
            "-Z",
            str(max_width),
            str(path),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass


def find_post_block(lines, post_slug: str):
    slug_re = re.compile(rf'slug:\s*"{re.escape(post_slug)}"')
    slug_idx = next((i for i, line in enumerate(lines) if slug_re.search(line)), None)
    if slug_idx is None:
        raise ValueError(f"Post slug not found: {post_slug}")

    start = slug_idx
    while start >= 0 and "{" not in lines[start]:
        start -= 1
    if start < 0:
        raise ValueError("Failed to locate start of post block.")

    brace = 0
    end = None
    for i in range(start, len(lines)):
        brace += lines[i].count("{")
        brace -= lines[i].count("}")
        if i > start and brace == 0:
            end = i
            break

    if end is None:
        raise ValueError("Failed to locate end of post block.")

    return start, end


def update_cover_field(lines, start: int, end: int, image_web_path: str) -> str:
    cover_idx = None
    image_idx = None
    indent = "    "

    for i in range(start, end + 1):
        cover_match = re.match(r'^(\s*)cover:\s*"[^"]*",\s*$', lines[i])
        if cover_match:
            cover_idx = i
            indent = cover_match.group(1)
        image_match = re.match(r'^(\s*)image:\s*"[^"]*",\s*$', lines[i])
        if image_match:
            image_idx = i
            indent = image_match.group(1)

    new_line = f'{indent}image: "{image_web_path}",\n'

    if image_idx is not None:
        lines[image_idx] = new_line
    elif cover_idx is not None:
        lines.insert(cover_idx + 1, new_line)
    else:
        lines.insert(start + 1, new_line)

    return "image"


def update_gallery_field(lines, start: int, end: int, image_web_path: str) -> str:
    indent = "    "
    images_start = None
    images_end = None
    insert_anchor = None

    for i in range(start, end + 1):
        cover_match = re.match(r'^(\s*)cover:\s*"[^"]*",\s*$', lines[i])
        if cover_match:
            indent = cover_match.group(1)
            insert_anchor = i
        image_match = re.match(r'^(\s*)image:\s*"[^"]*",\s*$', lines[i])
        if image_match:
            indent = image_match.group(1)
            insert_anchor = i

        images_match = re.match(r'^(\s*)images:\s*\[\s*$', lines[i])
        if images_match:
            indent = images_match.group(1)
            images_start = i
            break

    if images_start is not None:
        for j in range(images_start + 1, end + 1):
            if re.match(r'^\s*\],\s*$', lines[j]):
                images_end = j
                break

        if images_end is None:
            raise ValueError("images array found but closing bracket not found.")

        existing = "".join(lines[images_start:images_end + 1])
        if image_web_path in existing:
            return "images"

        lines.insert(images_end, f'{indent}  "{image_web_path}",\n')
        return "images"

    block = [
        f"{indent}images: [\n",
        f'{indent}  "{image_web_path}",\n',
        f"{indent}],\n",
    ]

    if insert_anchor is not None:
        lines[insert_anchor + 1:insert_anchor + 1] = block
    else:
        lines[start + 1:start + 1] = block

    return "images"


def update_posts_file(posts_file: Path, post_slug: str, image_web_path: str, mode: str) -> str:
    text = posts_file.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    start, end = find_post_block(lines, post_slug)

    if mode == "gallery":
        updated_field = update_gallery_field(lines, start, end, image_web_path)
    else:
        updated_field = update_cover_field(lines, start, end, image_web_path)

    posts_file.write_text("".join(lines), encoding="utf-8")
    return updated_field


def main():
    print(
        "DEPRECATED: scripts/import_image.py is based on the old assets/js/posts.js data model and is not compatible with the current Hugo content structure.\n"
        "Please add images under static/assets/images/... and update front matter (images) in content/posts/<slug>/index.zh.md and index.en.md manually.",
        file=sys.stderr,
    )
    sys.exit(2)

    parser = argparse.ArgumentParser(description="Import image into assets/images and optionally bind it to a post.")
    parser.add_argument("source", help="Source image path")
    parser.add_argument("--name", help="Target base name, default uses source file name")
    parser.add_argument("--post", help="Post slug in assets/js/posts.js to bind image")
    parser.add_argument("--mode", choices=["cover", "gallery"], default="cover", help="cover writes image field, gallery appends to images array")
    parser.add_argument("--max-width", type=int, default=1600, help="Max image width for local compression")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    source = Path(args.source).expanduser().resolve()

    if not source.exists() or not source.is_file():
        print(f"Source file not found: {source}", file=sys.stderr)
        sys.exit(1)

    ext = source.suffix.lower()
    if ext not in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
        print("Unsupported image extension. Use jpg/jpeg/png/webp/gif.", file=sys.stderr)
        sys.exit(1)

    now = dt.datetime.now()
    output_dir = project_root / "assets" / "images" / now.strftime("%Y") / now.strftime("%m")
    output_dir.mkdir(parents=True, exist_ok=True)

    base_name = slugify(args.name if args.name else source.stem)
    filename = f"{base_name}-{now.strftime('%Y%m%d%H%M%S')}{ext}"
    target = output_dir / filename
    shutil.copy2(source, target)

    compress_with_sips(target, args.max_width)

    rel_path = target.relative_to(project_root).as_posix()
    web_path = f"/{rel_path}"

    print(f"Image imported: {rel_path}")

    if args.post:
        posts_file = project_root / "assets" / "js" / "posts.js"
        updated_field = update_posts_file(posts_file, args.post, web_path, args.mode)
        print(f"Post updated: {args.post}")
        if updated_field == "images":
            print(f"Field updated: images[] += \"{web_path}\"")
        else:
            print(f"Field updated: image = \"{web_path}\"")
    else:
        print(f"Image web path: {web_path}")
        print("Tip: Add this path to post.image or post.images[].")


if __name__ == "__main__":
    main()
