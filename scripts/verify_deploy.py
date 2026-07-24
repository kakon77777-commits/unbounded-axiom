#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post-deploy consistency gate.

Run AFTER `npx wrangler deploy` (which itself must come after a fresh
`bash build-site.sh`). Compares every number Neo asked to be checked — the
homepage's stat tiles, the timeline's total, the AI Layer page's stat tiles,
/ai/corpus.json, /ai/corpus.jsonl, /api/papers/index.json, the AI-autonomous
count, and the last permanent id — against the LOCAL `dist/ai/build-id.json`
this build just wrote (the ground truth for what SHOULD now be live). Every
one of the sources above (plus /ai/manifest.json, /ai/version.json,
/ai/companions.json, /ai/programs/index.json) also carries a `build_id`
stamped by scripts/build.py in this same run — checked too, since two
DIFFERENT builds could coincidentally have the same paper count but can
never coincidentally share a build_id.

A mismatch after retrying (CDN edge caches can lag a few seconds after
`wrangler deploy` returns — a known, previously-observed behavior on this
project) means the deploy is NOT actually finished yet, regardless of what
wrangler printed. Exits non-zero in that case — treat that as "do not tell
Neo this deploy is done."

Usage: python scripts/verify_deploy.py [--base-url https://logic.evemisslab.com]
                                        [--retries 5] [--delay 5]
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT / "dist"

STAT_RE = re.compile(r'<div class="n"[^>]*>(\d+)</div>')
BUILD_ID_META_RE = re.compile(r'name="build-id"\s+content="([^"]*)"')
TIMELINE_TOTAL_RE = re.compile(r'([\d,]+)\s+in total')


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "verify-deploy/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8")


def _fetch_json(url: str):
    return json.loads(_fetch(url))


def _last_id(ids) -> str | None:
    def numeric(item_id: str) -> int:
        m = re.search(r"(\d+)$", item_id)
        return int(m.group(1)) if m else -1
    return max(ids, key=numeric) if ids else None


def load_local_truth() -> dict:
    path = DIST_DIR / "ai" / "build-id.json"
    if not path.exists():
        print(f"[FATAL] {path} not found — run `bash build-site.sh` first.")
        sys.exit(2)
    return json.loads(path.read_text(encoding="utf-8"))


def one_pass(base_url: str, truth: dict) -> list[tuple[str, bool, str]]:
    """Returns [(check_name, ok, detail), ...]. Never raises — a fetch
    failure is recorded as a failed check, not a crash, so one bad endpoint
    doesn't hide the results for the rest."""
    results = []
    bid = truth["build_id"]
    count = truth["corpus_count"]
    ai_auto = truth["authorship"]["ai_autonomous"]
    last_id = truth["last_id"]

    def check(name, fn):
        try:
            ok, detail = fn()
        except Exception as e:  # noqa: BLE001 — deliberately broad, this is a probe
            ok, detail = False, f"fetch/parse error: {e}"
        results.append((name, ok, detail))

    def homepage():
        html = _fetch(base_url + "/")
        stats = STAT_RE.findall(html)
        page_bid_m = BUILD_ID_META_RE.search(html)
        page_bid = page_bid_m.group(1) if page_bid_m else None
        total_ok = stats and int(stats[0]) == count
        bid_ok = page_bid == bid
        return total_ok and bid_ok, f"total={stats[0] if stats else '?'} (want {count}), build_id={page_bid} (want {bid})"

    def timeline():
        html = _fetch(base_url + "/timeline/")
        m = TIMELINE_TOTAL_RE.search(html)
        total = int(m.group(1).replace(",", "")) if m else None
        page_bid_m = BUILD_ID_META_RE.search(html)
        page_bid = page_bid_m.group(1) if page_bid_m else None
        ok = total == count and page_bid == bid
        return ok, f"total={total} (want {count}), build_id={page_bid} (want {bid})"

    def ai_layer():
        html = _fetch(base_url + "/ai/")
        stats = STAT_RE.findall(html)
        page_bid_m = BUILD_ID_META_RE.search(html)
        page_bid = page_bid_m.group(1) if page_bid_m else None
        total_ok = stats and int(stats[0]) == count
        ai_auto_ok = len(stats) >= 3 and int(stats[2]) == ai_auto
        bid_ok = page_bid == bid
        return total_ok and ai_auto_ok and bid_ok, (
            f"total={stats[0] if stats else '?'} (want {count}), "
            f"ai_autonomous={stats[2] if len(stats) >= 3 else '?'} (want {ai_auto}), "
            f"build_id={page_bid} (want {bid})"
        )

    def corpus_json():
        d = _fetch_json(base_url + "/ai/corpus.json")
        ok = (d.get("count") == count and d.get("authorship", {}).get("ai_autonomous") == ai_auto
              and d.get("build_id") == bid)
        return ok, f"count={d.get('count')}, ai_autonomous={d.get('authorship', {}).get('ai_autonomous')}, build_id={d.get('build_id')}"

    def corpus_jsonl():
        text = _fetch(base_url + "/ai/corpus.jsonl")
        lines = [l for l in text.splitlines() if l.strip()]
        ids = []
        for l in lines:
            try:
                ids.append(json.loads(l)["id"])
            except Exception:
                pass
        found_last = _last_id(ids)
        ok = len(lines) == count and found_last == last_id
        return ok, f"lines={len(lines)} (want {count}), last_id={found_last} (want {last_id})"

    def papers_index():
        d = _fetch_json(base_url + "/api/papers/index.json")
        items = d.get("items", [])
        found_last = _last_id([it["id"] for it in items])
        ok = len(items) == count and found_last == last_id
        return ok, f"items={len(items)} (want {count}), last_id={found_last} (want {last_id})"

    def manifest_version_companions_programs():
        parts = []
        ok_all = True
        for label, path, field in [
            ("manifest.json", "/ai/manifest.json", "build_id"),
            ("version.json", "/ai/version.json", "build_id"),
            ("companions.json", "/ai/companions.json", "build_id"),
            ("programs/index.json", "/ai/programs/index.json", "build_id"),
        ]:
            d = _fetch_json(base_url + path)
            got = d.get(field)
            ok = got == bid
            ok_all = ok_all and ok
            parts.append(f"{label}={got}{'' if ok else ' (MISMATCH)'}")
        return ok_all, "; ".join(parts)

    check("首頁總數 (homepage stat tile + build_id)", homepage)
    check("Timeline 總數 (+ build_id)", timeline)
    check("AI Layer 總數 + AI自主分類數 (+ build_id)", ai_layer)
    check("corpus.json", corpus_json)
    check("corpus.jsonl (line count + last id)", corpus_jsonl)
    check("papers/index.json (item count + last id)", papers_index)
    check("manifest/version/companions/programs build_id", manifest_version_companions_programs)
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="https://logic.evemisslab.com")
    ap.add_argument("--retries", type=int, default=5)
    ap.add_argument("--delay", type=float, default=5.0)
    args = ap.parse_args()

    truth = load_local_truth()
    print(f"[verify] local build truth: build_id={truth['build_id']} count={truth['corpus_count']} "
          f"ai_autonomous={truth['authorship']['ai_autonomous']} last_id={truth['last_id']}")
    print(f"[verify] checking {args.base_url} ...")

    last_results = []
    for attempt in range(1, args.retries + 1):
        last_results = one_pass(args.base_url, truth)
        if all(ok for _, ok, _ in last_results):
            print(f"[verify] PASS on attempt {attempt}/{args.retries}")
            for name, ok, detail in last_results:
                print(f"  [OK]   {name} — {detail}")
            print(f"\n[verify] Deployment IS consistent — build {truth['build_id']} is fully live across every surface checked.")
            sys.exit(0)
        if attempt < args.retries:
            n_fail = sum(1 for _, ok, _ in last_results if not ok)
            print(f"[verify] attempt {attempt}/{args.retries}: {n_fail} check(s) failed — "
                  f"retrying in {args.delay}s (CDN edge cache may still be catching up) ...")
            time.sleep(args.delay)

    print(f"\n[verify] FAIL after {args.retries} attempts — deployment is NOT consistent:")
    for name, ok, detail in last_results:
        mark = "OK  " if ok else "FAIL"
        print(f"  [{mark}] {name} — {detail}")
    print(f"\n[verify] Do not report this deploy as complete. Investigate before telling Neo it's done.")
    sys.exit(1)


if __name__ == "__main__":
    main()
