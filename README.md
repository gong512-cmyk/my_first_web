# Life Log

这是一个双语个人生活记录网站，支持桌面端和移动端响应式访问。

## 环境约定（先看这个）

- 本地开发机：macOS
- 线上服务器：Alibaba Cloud Linux 3（VPS）

文档里命令会明确标注在“本地 Mac”还是“VPS”执行，避免混淆。

## 本地预览

方式 1（推荐）：

```bash
cd <本地项目目录>
python3 -m http.server 8080
```

然后打开 http://localhost:8080

方式 2：

使用你喜欢的任意 static file server。

## 当前页面

- index.html：首页与最近更新
- timeline.html：按月份分组的时间轴
- notes.html：搜索与阅读记录
- about.html：关于与联系方式

## SEO 与订阅文件

- sitemap.xml
- robots.txt
- rss.xml

## 内容来源

文章数据目前维护在 assets/js/posts.js。

## 用真实内容替换示例内容（新手实操）

下面是一套最稳妥的替换流程，按顺序做即可。

### 第 1 步：先备份示例数据

```bash
cd <本地项目目录>
cp assets/js/posts.js assets/js/posts.backup.js
```

### 第 2 步：理解一篇文章的数据结构

在 assets/js/posts.js 里，每一篇记录是一个对象，核心字段如下：

- slug：文章唯一标识（英文短横线）
- date：日期，格式 YYYY-MM-DD
- tags：标签数组
- title.zh / title.en：中英文标题
- summary.zh / summary.en：中英文摘要
- content.zh / content.en：中英文正文
- image：单图封面（可选）
- images：多图相册（可选）

建议先替换一篇，确认成功后再批量替换。

### 第 3 步：新增你的第一篇真实文章

操作方式：

1. 打开 assets/js/posts.js
2. 复制一个现有对象，改成你的内容
3. 确保每个对象之间有英文逗号分隔
4. 保存后本地预览

### 第 4 步：导入图片并绑定文章

单图封面：

```bash
python3 scripts/import_image.py ~/Desktop/my-photo.jpg --post 你的-slug
```

多图相册：

```bash
python3 scripts/import_image.py ~/Desktop/my-photo-1.jpg --post 你的-slug --mode gallery
python3 scripts/import_image.py ~/Desktop/my-photo-2.jpg --post 你的-slug --mode gallery
```

### 第 5 步：本地验收

```bash
cd <本地项目目录>
python3 -m http.server 8080
```

验收点：

1. 首页能看到新文章
2. notes 页面能搜索到新文章
3. 图片和相册显示正常
4. 手机端排版正常

### 第 6 步：替换完后可删除示例文章

当你的真实内容足够后，再删除示例对象，避免一次性大改带来风险。

## Git 版本控制（新手推荐流程）

目标：每次发布可追溯、可回滚。

### 日常发布流程（推荐）

1. 在本地修改内容
2. 本地预览通过
3. 提交 Git commit
4. push 到 main
5. 查看 GitHub Actions 部署结果

### 常用命令模板

```bash
cd <本地项目目录>
git status
git add assets/js/posts.js assets/images
git commit -m "content: publish 2026-04-21 life notes"
git push origin main
```

### Commit 建议写法

- content: 发布或修改文章
- fix: 修复页面显示问题
- docs: 修改文档
- chore: 维护性调整

示例：

- content: add spring trip note
- fix: correct timeline date typo
- docs: update image import guide

### 回滚（两种）

方式 1：Git 回滚提交（推荐）

```bash
git log --oneline -n 10
git revert <commit_id>
git push origin main
```

方式 2：服务器回滚 release（紧急）

```bash
cd /var/www/lifelog/releases
ls -1dt */
ln -sfn /var/www/lifelog/releases/<old_release_id> /var/www/lifelog/current
```

### 强烈建议

1. 不要在 VPS 上直接改线上文件
2. 所有内容改动都从本地走 Git 发布
3. 每次只做一类改动（内容或样式），便于排错

## 图片上传（方案一：本地导入，无后端接口）

当前项目是 static site，没有后端上传 API。推荐使用本地导入脚本来完成图片管理：

1. 把图片导入到项目目录 assets/images/年/月/
2. 自动压缩图片（在 macOS 上会调用 sips）
3. 自动把图片路径写入指定文章的 image 字段

说明：

- image 字段用于单图封面
- images 数组用于多图相册

### 一次性准备

```bash
cd <本地项目目录>
chmod +x scripts/import_image.py
```

### 常用命令

把本地图片导入并绑定到指定文章（推荐）：

```bash
python3 scripts/import_image.py ~/Desktop/test-photo.jpg --post city-morning-walk
```

导入并追加到多图相册（关键）：

```bash
python3 scripts/import_image.py ~/Desktop/test-photo-2.jpg --post city-morning-walk --mode gallery
python3 scripts/import_image.py ~/Desktop/test-photo-3.jpg --post city-morning-walk --mode gallery
```

导入图片但不自动绑定文章：

```bash
python3 scripts/import_image.py ~/Desktop/test-photo.jpg
```

自定义压缩宽度（默认 1600）：

```bash
python3 scripts/import_image.py ~/Desktop/test-photo.jpg --post city-morning-walk --max-width 1400
```

### 文章数据结构说明

脚本会在 assets/js/posts.js 的目标文章里新增或更新：

```js
image: "/assets/images/2026/04/your-file-20260421143000.jpg",
```

如果使用 --mode gallery，会自动写入或追加：

```js
images: [
	"/assets/images/2026/04/your-file-20260421143100.jpg",
	"/assets/images/2026/04/your-file-20260421143200.jpg",
],
```

页面会自动显示：

- 首页卡片显示封面图
- notes 详情页显示文章图或多图相册

### 支持格式

- jpg / jpeg / png / webp / gif

## VPS 部署（阿里云）

### Alibaba Cloud Linux 3（RHEL/CentOS 系）快速初始化

你的系统如果是 Alibaba Cloud Linux 3，请不要使用 apt。可以直接运行项目里的初始化脚本：

在本地 Mac 执行（把脚本传到 VPS 并远程执行）：

```bash
cd <本地项目目录>
chmod +x scripts/bootstrap_alinux3.sh
scp scripts/bootstrap_alinux3.sh <VPS登录用户>@<VPS_IP>:/tmp/bootstrap_alinux3.sh
ssh <VPS登录用户>@<VPS_IP> "sudo bash /tmp/bootstrap_alinux3.sh <你的部署用户>"
```

示例：

```bash
scp scripts/bootstrap_alinux3.sh ecs-user@1.2.3.4:/tmp/bootstrap_alinux3.sh
ssh ecs-user@1.2.3.4 "sudo bash /tmp/bootstrap_alinux3.sh ecs-user"
```

脚本会自动完成：

1. 安装 nginx、curl、tar、openssh-clients、firewalld
2. 创建 /var/www/lifelog/releases 与 /var/www/lifelog/current 体系所需目录
3. 写入基于 IP 的 Nginx 配置（先走 HTTP）
4. 启动 nginx 与 firewalld，并放行 22/80

然后请确认云安全组也放行了 TCP 22 和 80。

1. 准备服务器目录：

```bash
sudo mkdir -p /var/www/lifelog/releases
sudo mkdir -p /var/www/lifelog/shared
sudo chown -R $USER:$USER /var/www/lifelog
```

2. 上传新版本并切换 current symlink：

在本地 Mac 执行：

```bash
cd <本地项目目录>
chmod +x deploy/deploy.sh
./deploy/deploy.sh user@your-vps-ip /var/www/lifelog/releases/202604210001
```

3. 将 deploy/nginx.conf.sample 配置到 Nginx 后 reload Nginx。

4. 申请 HTTPS 证书：

```bash
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

## 建议下一步

- 把示例文章数据替换为你的真实内容
- 增加自动化 RSS 与 sitemap 生成
- 接入 GitHub Actions 自动部署

## 自动更新与维护（新手指南）

这一节会告诉你如何用最少手工操作，让网站自动更新并保持稳定。

### 第 1 步：把项目放到 GitHub

1. 新建一个 GitHub repository。
2. 把当前项目推到 main 分支。
3. 后续本地开发完成后，继续 push 到 main。

完成后，每次 push main 都可以触发自动部署。

### 第 2 步：准备 VPS 目录

在 VPS 上运行：

```bash
sudo mkdir -p /var/www/lifelog/releases
sudo mkdir -p /var/www/lifelog/shared
sudo mkdir -p /var/backups/lifelog
sudo chown -R $USER:$USER /var/www/lifelog /var/backups/lifelog
```

### 第 3 步：为 GitHub Actions 创建 SSH Key

在本地机器运行：

```bash
ssh-keygen -t ed25519 -C "lifelog-deploy" -f ~/.ssh/lifelog_deploy
```

然后执行：

1. 把 ~/.ssh/lifelog_deploy.pub 加到 VPS 用户的 ~/.ssh/authorized_keys。
2. 把 ~/.ssh/lifelog_deploy 私钥内容复制到 GitHub Secret：VPS_SSH_PRIVATE_KEY。

### 第 4 步：配置 GitHub repository secrets

进入 GitHub repo 的 Settings -> Secrets and variables -> Actions，添加：

- VPS_HOST：你的 VPS IP 或域名
- VPS_USER：你的 VPS 登录用户
- VPS_SSH_PRIVATE_KEY：第 3 步生成的私钥文本
- SITE_URL：网站完整地址，例如 https://your-domain.com

### 第 5 步：启用自动部署

项目中已包含 workflow 文件：

- .github/workflows/deploy.yml

工作流程如下：

1. push 到 main。
2. GitHub 把文件上传到 VPS 新 release 目录。
3. 自动更新 /var/www/lifelog/current symlink。
4. 自动执行首页、sitemap、rss 的健康检查。

### 第 6 步：配置服务器维护任务

项目中已准备文件：

- scripts/server_backup.sh
- scripts/server_healthcheck.sh
- scripts/cron.sample

建议在 VPS 上执行：

```bash
sudo mkdir -p /opt/lifelog/scripts
sudo cp /var/www/lifelog/current/scripts/server_backup.sh /opt/lifelog/scripts/
sudo cp /var/www/lifelog/current/scripts/server_healthcheck.sh /opt/lifelog/scripts/
sudo chmod +x /opt/lifelog/scripts/server_backup.sh /opt/lifelog/scripts/server_healthcheck.sh
crontab -e
```

然后把 scripts/cron.sample 的内容粘贴进 crontab。

### 第 7 步：日常操作（很简单）

1. 本地修改内容。
2. 本地预览确认。
3. push 到 main。
4. 查看 GitHub Actions 部署结果。

即使部署失败，线上旧版本仍会保留，因为 current symlink 只会在新版本上传完成后切换。

### 第 8 步：安全检查清单

- 保留 7 到 14 个 release 目录用于回滚
- 保留 14 份备份压缩包
- 开启 HTTPS 自动续签
- 使用非 root 部署用户
- 仅开放 22、80、443 端口

### 快速回滚（需要时）

在 VPS 上执行：

```bash
cd /var/www/lifelog/releases
ls -1dt */
ln -sfn /var/www/lifelog/releases/<old_release_id> /var/www/lifelog/current
```

这会在几秒内恢复到旧版本。
