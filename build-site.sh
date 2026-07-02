#!/usr/bin/env bash
# Unified build for logic.evemisslab.com.
#   1. Python engine  -> data + AI layer + raw/api + 3 viz pages + sitemap/llms/robots
#   2. Astro human shell (reads the engine JSON) -> / , /p/{id}/ readers, /timeline/
#   3. Overlay the Astro output onto dist/ (its /index.html and /p/{id}/ pages replace
#      the engine's plain versions; the machine metadata is preserved in the Astro pages).
# Set the Cloudflare Pages/Workers build command to:  bash build-site.sh
set -euo pipefail

echo "[1/3] engine build — python3 build.py"
python3 build.py

echo "[2/3] astro human shell — astro build"
cd shell
if [ ! -d node_modules ]; then npm ci || npm install; fi
npm run build
cd ..

echo "[3/3] overlay astro output onto dist/"
cp -r shell/dist/. dist/

echo "[ok] unified site built -> dist/"
