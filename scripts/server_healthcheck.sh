#!/usr/bin/env bash
set -euo pipefail

SITE_URL="${1:-https://www.your-domain.com}"
STRICT_WWW="${2:-}"

base_url="${SITE_URL%/}"

extract_host() {
  local url="$1"
  local host="${url#https://}"
  host="${host#http://}"
  host="${host%%/*}"
  echo "${host}"
}

check() {
  local path="$1"
  local url="${base_url}${path}"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" "${url}")

  if [[ "${code}" != "200" ]]; then
    echo "Health check failed: ${url} => ${code}"
    return 1
  fi

  echo "OK: ${url}"
}

check_redirect() {
  local from_url="$1"
  local to_url="$2"
  local output code redirect
  output=$(curl -s -o /dev/null -w "%{http_code} %{redirect_url}" "${from_url}")
  code="${output%% *}"
  redirect="${output#* }"

  if [[ "${code}" != "301" ]]; then
    echo "Redirect check failed: ${from_url} => HTTP ${code}"
    return 1
  fi

  if [[ "${redirect}" != "${to_url}" ]]; then
    echo "Redirect target mismatch: ${from_url} => ${redirect} (expected ${to_url})"
    return 1
  fi

  echo "OK redirect: ${from_url} -> ${to_url}"
}

check "/"
check "/posts/"
check "/timeline/"
check "/about/"
check "/en/"
check "/en/posts/"
check "/en/timeline/"
check "/en/about/"
check "/sitemap.xml"
check "/rss.xml"

if [[ "${STRICT_WWW}" == "--strict-www" ]]; then
  site_host="$(extract_host "${base_url}")"
  if [[ "${site_host}" != www.* ]]; then
    echo "Strict mode requires SITE_URL to use www host. Current: ${base_url}"
    exit 1
  fi

  apex_host="${site_host#www.}"
  check_redirect "http://${apex_host}/" "${base_url}/"
  check_redirect "https://${apex_host}/" "${base_url}/"
fi

echo "All checks passed."
