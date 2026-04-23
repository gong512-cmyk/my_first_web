# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Bilingual (zh/en) personal life-log static website. Built with **Hugo** static site generator. No npm, no bundler.

## Local Development

```bash
hugo server
```

Then open http://localhost:1313. Hugo watches files and live-reloads automatically.

## Architecture

**Content is Markdown-driven.** All posts live in `content/posts/{slug}/` as page bundles. Each bundle has:
- `index.zh.md` — Chinese version (front matter + body)
- `index.en.md` — English version (same front matter keys, translated values)

**Front matter fields per post:**
```yaml
title: "标题"
date: 2026-04-22
tags: [life, coding]
cover: gradient-1      # CSS class for card background
images:                # optional; list of image paths
  - /assets/images/20260422-pic/photo.jpg
summary: "一句话摘要"
```

**Hugo multilingual:** `defaultContentLanguage = "zh"`, `defaultContentLanguageInSubdir = false`.
- Chinese site at `/` — `public/posts/slug/`
- English site at `/en/` — `public/en/posts/slug/`
- Language switcher uses `.AllTranslations` in baseof template.

**Layouts (Go HTML templates):**
- `layouts/_default/baseof.html` — shared HTML shell (nav, header, footer)
- `layouts/index.html` — homepage (latest 3 posts)
- `layouts/posts/list.html` — posts grid (生活记录 nav)
- `layouts/posts/single.html` — single post detail
- `layouts/timeline/single.html` — timeline grouped by month
- `layouts/about/single.html` — about page (content + features list)
- `layouts/_default/taxonomy.html` — tag index
- `layouts/_default/term.html` — posts filtered by tag

**i18n strings:** `i18n/zh.yaml` and `i18n/en.yaml`. All UI text (nav labels, hero text, footer) goes here.

**Static assets:** primary stylesheet source is `assets/css/styles.css` (loaded via Hugo resources pipeline in base template), while `static/assets/css/styles.css` is kept as compatibility fallback; images live in `static/assets/images/`. Served at `/assets/...`.

**Standalone pages** (timeline, about): `content/timeline.zh.md` / `content/timeline.en.md` etc., with `type:` field in front matter to route to the correct layout.

## Adding a New Post

1. Create a new page bundle directory:
   ```bash
   mkdir content/posts/my-new-post
   ```
2. Create `index.zh.md` and `index.en.md` with the required front matter.
3. Run `hugo server` to preview locally.
4. Commit and push — GitHub Actions builds and deploys automatically.

### From Obsidian

Write your note with YAML front matter matching the fields above. Use `## 中文` / `## English` sections if drafting both languages in one file, then split into separate `index.zh.md` / `index.en.md` before committing.

## Image Import

Images should go in `static/assets/images/{date}-pic/`. Reference them in front matter as `/assets/images/{date}-pic/filename.jpg`.

```bash
# The import_image.py script needs updating for Hugo (see scripts/import_image.py)
# For now, manually copy images to static/assets/images/ and add paths to front matter
```

## Build Output

Hugo generates the site into `public/`. This directory is git-ignored; GitHub Actions builds it fresh on every push.

## Cover Classes

The `cover` field (e.g., `gradient-1`, `gradient-2`) is applied as a CSS class to post cards. Defined in `assets/css/styles.css` (synced to static fallback when needed). Available: `gradient-1` through `gradient-4`.

## Deployment

Push to `main` triggers GitHub Actions (`.github/workflows/deploy.yml`):
1. Install Hugo, run `hugo --minify` (reads `HUGO_BASEURL` from `secrets.SITE_URL`)
2. Tar `public/` and upload to VPS via SSH
3. Switch `/var/www/lifelog/current` symlink to new release
4. Run health checks against `SITE_URL`; fallback to VPS localhost check
5. Keep only the last 7 releases

Manual deploy: build locally with `hugo --minify`, then use `./deploy/deploy.sh`.

VPS is Alibaba Cloud Linux 3 (RHEL/CentOS family). Bootstrap script: `scripts/bootstrap_alinux3.sh`.

## Commit Conventions

- `content:` — publish or modify posts
- `fix:` — fix display or functionality issues
- `docs:` — documentation changes
- `chore:` — maintenance tasks

