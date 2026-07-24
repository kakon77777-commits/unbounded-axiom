#!/usr/bin/env bash
# Build + deploy + verify logic.evemisslab.com in one gated step.
#   1. bash build-site.sh   -> fresh dist/, including this run's build_id
#   2. npx wrangler deploy  -> pushes dist/ live
#   3. python scripts/verify_deploy.py -> confirms homepage/timeline/AI Layer/
#      corpus.json/corpus.jsonl/papers-index/AI-autonomous-count/last-id all
#      agree with each other AND carry the SAME build_id as this build wrote.
# Step 3 failing means the deploy is not actually consistent yet (stale CDN
# edge cache, or a real bug) — this script's own exit code reflects that;
# do not treat `wrangler deploy` succeeding, on its own, as "done."
set -euo pipefail

bash build-site.sh
npx wrangler deploy
python scripts/verify_deploy.py
