# Life Log

基于 Hugo 的中英文双语个人生活记录网站。

## 技术栈

- Hugo（无 npm、无 bundler）
- 内容驱动：`content/posts/<slug>/index.zh.md` 与 `index.en.md`
- 样式主入口：`assets/css/styles.css`（模板通过 Hugo resources 管线加载）

## 本地开发

```bash
hugo server
```

打开 `http://localhost:1313` 预览。

## 内容结构

每篇文章是一个 page bundle：

```text
content/posts/<slug>/
	index.zh.md
	index.en.md
```

建议 front matter 字段：

```yaml
title: "标题"
date: 2026-04-22
tags: [life, coding]
cover: gradient-1
images:
	- /assets/images/20260422-pic/photo.jpg
summary: "一句话摘要"
```

## 图片管理（当前策略）

当前请手动管理图片：

1. 将图片放到 `static/assets/images/<date>-pic/`
2. 在文章 front matter 的 `images` 字段引用 `/assets/images/...`

`scripts/import_image.py` 仍基于旧版 `assets/js/posts.js` 数据模型，当前 Hugo 架构下已不适用。

## 发布与部署（推荐主流程）

主流程：`push -> GitHub Actions -> VPS`

1. 提交并推送到 `main`
2. GitHub Actions 执行 `hugo --minify`
3. 上传 `public/` 到 VPS 新 release 目录
4. 切换 `/var/www/lifelog/current` 软链接
5. 健康检查 `/`、`/sitemap.xml`、`/rss.xml`

工作流文件：`.github/workflows/deploy.yml`

## 手动部署（兜底）

`deploy/deploy.sh` 已对齐 Hugo 流程：

```bash
./deploy/deploy.sh <user@host> <remote_release_dir>
```

脚本会：

1. 本地执行 `hugo --minify`
2. 仅上传 `public/` 到远端 release 目录
3. 切换 `current` 软链接

## 服务器初始化（Alibaba Cloud Linux 3）

```bash
chmod +x scripts/bootstrap_alinux3.sh
scp scripts/bootstrap_alinux3.sh <VPS_USER>@<VPS_IP>:/tmp/bootstrap_alinux3.sh
ssh <VPS_USER>@<VPS_IP> "sudo bash /tmp/bootstrap_alinux3.sh <VPS_USER>"
```

## GitHub Secrets

在仓库 `Settings -> Secrets and variables -> Actions` 配置：

- `SITE_URL`：站点完整地址（例如 `https://example.com`）
- `VPS_HOST`：VPS 地址
- `VPS_USER`：VPS 登录用户
- `VPS_SSH_PRIVATE_KEY`：部署私钥

## 健康检查与运维

- 健康检查脚本：`scripts/server_healthcheck.sh`
- 备份脚本：`scripts/server_backup.sh`
- 定时任务样例：`scripts/cron.sample`

健康检查脚本支持可选的 `--strict-www` 模式，用于校验 apex 到 www 的 301 跳转：

```bash
bash scripts/server_healthcheck.sh https://www.your-domain.com --strict-www
```

## 回滚

```bash
cd /var/www/lifelog/releases
ls -1dt */
ln -sfn /var/www/lifelog/releases/<old_release_id> /var/www/lifelog/current
```

## 提交约定

- `content:` 发布或修改文章
- `fix:` 修复显示或功能问题
- `docs:` 文档更新
- `chore:` 维护性调整
