#!/usr/bin/env bash
set -euo pipefail

# Bootstrap for Alibaba Cloud Linux 3 (RHEL/CentOS family)
# Usage:
#   sudo bash scripts/bootstrap_alinux3.sh <deploy_user>
# Example:
#   sudo bash scripts/bootstrap_alinux3.sh ec2-user

DEPLOY_USER="${1:-}"
if [[ -z "${DEPLOY_USER}" ]]; then
  echo "Usage: sudo bash $0 <deploy_user>"
  exit 1
fi

# Install required packages
if command -v dnf >/dev/null 2>&1; then
  dnf install -y nginx curl tar openssh-clients firewalld
else
  yum install -y nginx curl tar openssh-clients firewalld
fi

# Create website directories
mkdir -p /var/www/lifelog/releases
mkdir -p /var/www/lifelog/shared
mkdir -p /var/backups/lifelog
chown -R "${DEPLOY_USER}:${DEPLOY_USER}" /var/www/lifelog /var/backups/lifelog

# Nginx site config (HTTP, IP-based)
cat >/etc/nginx/conf.d/lifelog.conf <<'EOF'
server {
  listen 80;
  server_name _;

  root /var/www/lifelog/current;
  index index.html;

  location / {
    try_files $uri $uri/ =404;
  }

  location ~* \.(css|js|svg|jpg|jpeg|png|webp|woff2)$ {
    expires 30d;
    add_header Cache-Control "public, max-age=2592000, immutable";
  }
}
EOF

# Start services
systemctl enable --now nginx
systemctl enable --now firewalld

# Open ports
firewall-cmd --permanent --add-service=ssh
firewall-cmd --permanent --add-service=http
firewall-cmd --reload

# Validate nginx config and reload
nginx -t
systemctl reload nginx

echo "Bootstrap completed."
echo "Next: verify Tencent/Alibaba security group allows TCP 22 and 80."
echo "Then trigger GitHub Actions deploy again."
