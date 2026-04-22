#!/usr/bin/env python3
"""
translate_post.py — 将 .zh.md 文章自动翻译为 .en.md

用法:
    python3 scripts/translate_post.py content/posts/my-post/index.zh.md

需要先设置环境变量：
    export OPENAI_API_KEY="sk-..."

依赖：
    pip3 install openai
"""

import argparse
import os
import re
import sys
from pathlib import Path


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """分离 YAML front matter 和正文"""
    if not text.startswith("---"):
        return {}, text
    end = text.index("---", 3)
    fm_raw = text[3:end].strip()
    body = text[end + 3:].strip()

    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
        else:
            fm[line.strip()] = ""
    return fm, body


def build_prompt(zh_path: Path) -> tuple[str, str]:
    """读取 zh.md，构造翻译 prompt，返回 (prompt, raw_zh_text)"""
    text = zh_path.read_text(encoding="utf-8")
    prompt = f"""You are a professional translator. Translate the following Hugo blog post from Chinese to English.

Rules:
1. Keep ALL YAML front matter keys exactly as-is (title, date, tags, cover, summary, images, etc.)
2. Translate ONLY the VALUES of: title, summary, and the body content below the front matter
3. Keep tags in English (they are usually already English; if Chinese, translate them)
4. Keep dates, numbers, file paths, and code blocks unchanged
5. Output the complete file starting with --- (the YAML front matter delimiter)
6. Write naturally — not word-for-word, but preserve meaning and tone

Input file:
---
{text}
---

Output the translated English .md file content only, no explanation:"""
    return prompt, text


def translate_with_openai(prompt: str) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        print("错误: 请先安装 openai 库: pip3 install openai")
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("错误: 请设置环境变量 OPENAI_API_KEY")
        print('  export OPENAI_API_KEY="sk-..."')
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


def main():
    parser = argparse.ArgumentParser(description="将 .zh.md 自动翻译为 .en.md")
    parser.add_argument("zh_file", help="源文件路径，例如 content/posts/my-post/index.zh.md")
    parser.add_argument("--dry-run", action="store_true", help="只打印输出，不写文件")
    args = parser.parse_args()

    zh_path = Path(args.zh_file)
    if not zh_path.exists():
        print(f"错误: 文件不存在: {zh_path}")
        sys.exit(1)
    if ".zh." not in zh_path.name:
        print(f"错误: 文件名必须包含 .zh.（例如 index.zh.md）")
        sys.exit(1)

    en_path = Path(str(zh_path).replace(".zh.", ".en."))
    if en_path.exists():
        print(f"英文版已存在: {en_path}")
        overwrite = input("是否覆盖？(y/N) ").strip().lower()
        if overwrite != "y":
            print("已取消。")
            sys.exit(0)

    print(f"正在翻译: {zh_path}")
    print("调用 OpenAI API...")

    prompt, _ = build_prompt(zh_path)
    result = translate_with_openai(prompt)

    # 清理模型可能输出的代码围栏
    result = re.sub(r"^```(?:markdown|yaml)?\n?", "", result)
    result = re.sub(r"\n?```$", "", result)

    if args.dry_run:
        print("\n===== 翻译结果预览 =====")
        print(result)
        return

    en_path.write_text(result + "\n", encoding="utf-8")
    print(f"已生成: {en_path}")


if __name__ == "__main__":
    main()
