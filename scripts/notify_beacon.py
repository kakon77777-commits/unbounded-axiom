#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Notify the Continuous Discovery Beacon after a verified deploy.

Run AFTER scripts/verify_deploy.py succeeds — deploy.sh's own gate for "the
site is actually live and consistent," not just "wrangler deploy returned
0." Fires one 'updated' event for the homepage, content_hash'd to this
build's build_id, so the Beacon's own dedup naturally skips re-notifying for
a build that was already reported.

Missing BEACON_SUBMIT_TOKEN_LOGIC is not an error — it means the integration
isn't configured locally yet, matching the Beacon's own IndexNow adapter,
which reports 'skipped' rather than failing when it has nothing to work
with.

Usage: python scripts/notify_beacon.py
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_ID_PATH = ROOT / "dist" / "ai" / "build-id.json"
BEACON_URL = "https://beacon.evemiss.com/api/v1/events"
SITE_ID = "logic_evemisslab"
SITE_URL = "https://unboundedaxiom.org/"


def main() -> int:
    token = os.environ.get("BEACON_SUBMIT_TOKEN_LOGIC")
    if not token:
        print("[skipped] BEACON_SUBMIT_TOKEN_LOGIC not set - not notifying the Beacon.")
        return 0

    if not BUILD_ID_PATH.exists():
        print(f"[FATAL] {BUILD_ID_PATH} not found - run bash build-site.sh first.")
        return 2
    truth = json.loads(BUILD_ID_PATH.read_text(encoding="utf-8"))
    build_id = truth["build_id"]
    corpus_count = truth.get("corpus_count")

    payload = {
        "site_id": SITE_ID,
        "url": SITE_URL,
        "event_type": "updated",
        "content_hash": f"logic-build:{build_id}",
        "title": "Logic Matrix",
        "summary": f"Verified deploy, corpus_count={corpus_count}, build_id={build_id}",
        "auto_dispatch": True,
    }
    req = urllib.request.Request(
        BEACON_URL,
        data=json.dumps(payload).encode("utf-8"),
        # Explicit User-Agent required: Cloudflare's bot protection in front
        # of beacon.evemiss.com blocks urllib's default "Python-urllib/x.y"
        # signature with a 403 (Cloudflare error 1010) before the request
        # ever reaches the app. curl's default UA passes through fine.
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "unbounded-axiom-deploy-notify/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8")
            print(f"[ok] Beacon notified: {resp.status} {body[:200]}")
            return 0
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(f"[FAILED] Beacon returned {exc.code}: {detail}")
        return 1
    except urllib.error.URLError as exc:
        print(f"[FAILED] Could not reach Beacon: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
