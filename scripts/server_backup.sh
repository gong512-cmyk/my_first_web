#!/usr/bin/env bash
set -euo pipefail

# Backup /var/www/lifelog/current into /var/backups/lifelog.
# Keep latest 14 backups.

SOURCE_DIR="/var/www/lifelog/current"
BACKUP_DIR="/var/backups/lifelog"
STAMP="$(date +%Y%m%d_%H%M%S)"
TARGET="${BACKUP_DIR}/lifelog_${STAMP}.tar.gz"

mkdir -p "${BACKUP_DIR}"

tar -czf "${TARGET}" -C "${SOURCE_DIR}" .

cd "${BACKUP_DIR}"
ls -1t lifelog_*.tar.gz | tail -n +15 | xargs -r rm -f

echo "Backup created: ${TARGET}"
