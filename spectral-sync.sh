#!/usr/bin/env bash
# Project Spectral-Matrix — one-shot loop: pull -> decay -> patch -> deploy.
# Daily driver for 衍. Does NOT rebuild the whole site; it refreshes the heat
# JSON in dist/ and redeploys assets (hash-deduped, ~seconds).
# Full rebuild path (after new TCF extractions): bash build-site.sh && npx wrangler deploy
set -e
cd "$(dirname "$0")"

echo "== [1/3] pull ingestion data + decay =="
python scripts/spectral_pull.py

echo "== [2/3] deploy logic worker (refreshed dist/ai/spectral-heat.json) =="
npx wrangler deploy

echo "== [3/3] commit heat history =="
git add registry/generated/spectral-history.json registry/generated/spectral-heat.json
git diff --cached --quiet || git commit -m "spectral: daily heat sync ($(date -u +%Y-%m-%d))" && git push || true

echo "== done. spectral.evemisslab.com reads the fresh heat live. =="
