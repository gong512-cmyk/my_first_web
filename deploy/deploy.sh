#!/usr/bin/env bash
set -euo pipefail

# Usage:
# ./deploy/deploy.sh user@your-vps-ip /var/www/lifelog/releases/$(date +%Y%m%d%H%M%S)

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <user@host> <remote_release_dir>"
  exit 1
fi

HOST="$1"
REMOTE_RELEASE="$2"
REMOTE_CURRENT="/var/www/lifelog/current"

rsync -av --delete \
  --exclude ".git" \
  --exclude "deploy" \
  ./ "$HOST:$REMOTE_RELEASE"

ssh "$HOST" "ln -sfn '$REMOTE_RELEASE' '$REMOTE_CURRENT'"
echo "Deploy complete: $REMOTE_RELEASE"
