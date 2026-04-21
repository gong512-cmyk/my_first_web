#!/usr/bin/env bash
set -euo pipefail

SITE_URL="${1:-https://your-domain.com}"

check() {
  local path="$1"
  local url="${SITE_URL}${path}"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" "${url}")

  if [[ "${code}" != "200" ]]; then
    echo "Health check failed: ${url} => ${code}"
    return 1
  fi

  echo "OK: ${url}"
}

check "/"
check "/index.html"
check "/timeline.html"
check "/notes.html"
check "/about.html"
check "/sitemap.xml"
check "/rss.xml"

echo "All checks passed."
