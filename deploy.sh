#!/usr/bin/env bash
# Build + deploy + verify logic.evemisslab.com in one gated step.
#   1. bash build-site.sh   -> fresh dist/, including this run's build_id
#   2. npx wrangler deploy  -> pushes dist/ live
#   3. python scripts/verify_deploy.py -> confirms homepage/timeline/AI Layer/
#      corpus.json/corpus.jsonl/papers-index/AI-autonomous-count/last-id all
#      agree with each other AND carry the SAME build_id as this build wrote.
#   4. python scripts/notify_beacon.py -> tells the Continuous Discovery
#      Beacon (beacon.evemiss.com) this build is real and live, so it can
#      broadcast IndexNow/Sitemap/RSS signals. Only runs after step 3 passes
#      — never notify about a deploy that isn't actually confirmed live.
#      Non-fatal if it fails or isn't configured (BEACON_SUBMIT_TOKEN_LOGIC
#      unset): the site's own deploy must never depend on the Beacon being
#      reachable.
# Step 3 failing means the deploy is not actually consistent yet (stale CDN
# edge cache, or a real bug) — this script's own exit code reflects that;
# do not treat `wrangler deploy` succeeding, on its own, as "done."
set -euo pipefail

bash build-site.sh
npx wrangler deploy
python scripts/verify_deploy.py
python scripts/notify_beacon.py || echo "[warn] Beacon notification failed - deploy itself succeeded, this is non-fatal"
