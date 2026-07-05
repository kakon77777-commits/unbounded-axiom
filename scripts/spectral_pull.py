#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Project Spectral-Matrix — Phase 1+2: ingestion bridge + thermodynamic decay.

Pulls AI-crawler attention data from two sources, merges it into a per-day
history, applies a half-life decay, and emits the machine-readable spectral
heat map consumed by spectral.evemisslab.com and the AICL layer.

Sources (both optional; the script uses whatever is available):
  1. KV `hot2` via wrangler (already OAuth'd on this machine) — the first-party
     /api/log-crawler beacon signal. Zero setup.
  2. Cloudflare GraphQL Analytics — full bot ingestion of /p/ and /raw/ paths
     (GPTBot, ClaudeBot, PerplexityBot, ChatGPT-User, …). Needs a zone-scoped
     Analytics:Read token in .spectral.env (gitignored):
         CLOUDFLARE_API_TOKEN=...
         CF_ZONE_ID=...

Outputs:
  registry/generated/spectral-history.json   day -> id -> hits (28-day window)
  registry/generated/spectral-heat.json      decayed spectral weights 0..1
  dist/ai/spectral-heat.json                 (patched directly if dist exists)

Decay model (Neo's Phase 2 spec): weight_raw(id) = Σ_d hits_d · 0.5^(age_d / H),
H = 7 days. Spectral weight = log1p(raw)/log1p(max_raw). States:
  base < 0.15 <= active < 0.70 <= resonance
"""
import json
import math
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATED = ROOT / "registry" / "generated"
DIST_AI = ROOT / "dist" / "ai"
ENV_FILE = ROOT / ".spectral.env"

KV_NAMESPACE_ID = "834dc04070974480bda0ac8e1af6d350"
HALF_LIFE_DAYS = 7.0
WINDOW_DAYS = 28
STATE_ACTIVE = 0.15
STATE_RESONANCE = 0.70
# Absolute floors: relative weight alone degenerates when the corpus is cold
# (1 hit vs max 1 hit -> w=1.0). A node must also carry real volume to glow.
MIN_HEAT_ACTIVE = 3.0
MIN_HEAT_RESONANCE = 20.0
BOT_UAS = ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User",
           "claude-web", "PerplexityBot", "Perplexity-User", "Google-Extended",
           "Bytespider", "Amazonbot", "cohere", "meta-external"]


def _today():
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def _load_env():
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    env.setdefault("CLOUDFLARE_API_TOKEN", os.environ.get("CLOUDFLARE_API_TOKEN", ""))
    env.setdefault("CF_ZONE_ID", os.environ.get("CF_ZONE_ID", ""))
    return env


# ---- source 1: KV hot2 (first-party beacon) ----

def pull_hot2():
    """Read the day-bucketed beacon heat via wrangler. Returns {id: {day: hits}}."""
    try:
        r = subprocess.run(
            ["npx", "wrangler", "kv", "key", "get", "hot2",
             "--namespace-id", KV_NAMESPACE_ID, "--remote"],
            capture_output=True, text=True, timeout=120, cwd=str(ROOT),
            shell=(os.name == "nt"), encoding="utf-8", errors="replace")
        raw = (r.stdout or "").strip()
        start = raw.find("{")
        if start < 0:
            print(f"[spectral] hot2: no JSON in wrangler output ({raw[:120]!r})")
            return {}
        hot = json.loads(raw[start:])
    except Exception as e:
        print(f"[spectral] hot2 pull failed: {e}")
        return {}
    out = {}
    for pid, rec in hot.items():
        buckets = {}
        if rec.get("d"):
            buckets[rec["d"]] = rec.get("c", 0)
        if rec.get("pd"):
            buckets[rec["pd"]] = buckets.get(rec["pd"], 0) + rec.get("p", 0)
        if buckets:
            out[pid] = buckets
    print(f"[spectral] hot2: {len(out)} nodes with beacon heat")
    return out


# ---- source 2: Cloudflare GraphQL Analytics (full bot ingestion) ----

def pull_graphql(env):
    token, zone = env.get("CLOUDFLARE_API_TOKEN"), env.get("CF_ZONE_ID")
    if not token or not zone:
        print("[spectral] GraphQL: no token/zone in .spectral.env — skipping "
              "(beacon-only mode). Add the token to unlock full /p/ + /raw/ ingestion data.")
        return {}
    now = datetime.now(timezone.utc)
    start = (now - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
    end = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    query = """
query($zone: String!, $start: Time!, $end: Time!, $ua: String!) {
  viewer { zones(filter: {zoneTag: $zone}) {
    httpRequestsAdaptiveGroups(limit: 5000, filter: {
      datetime_geq: $start, datetime_lt: $end, userAgent_like: $ua
    }) { count dimensions { clientRequestPath } }
  } }
}"""
    day = _today()
    out = {}
    for bot in BOT_UAS:
        body = json.dumps({"query": query, "variables": {
            "zone": zone, "start": start, "end": end, "ua": f"%{bot}%"}}).encode()
        req = urllib.request.Request(
            "https://api.cloudflare.com/client/v4/graphql", data=body,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        try:
            resp = json.loads(urllib.request.urlopen(req, timeout=60).read())
        except Exception as e:
            print(f"[spectral] GraphQL {bot}: {e}")
            continue
        zones = (((resp.get("data") or {}).get("viewer") or {}).get("zones") or [])
        if not zones:
            errs = resp.get("errors")
            if errs:
                print(f"[spectral] GraphQL {bot}: {str(errs)[:200]}")
            continue
        for g in zones[0].get("httpRequestsAdaptiveGroups") or []:
            path = (g.get("dimensions") or {}).get("clientRequestPath") or ""
            pid = _path_to_id(path)
            if pid:
                out.setdefault(pid, {}).setdefault(day, 0)
                out[pid][day] += g.get("count", 0)
    print(f"[spectral] GraphQL: {len(out)} nodes with ingestion heat (last 24h)")
    return out


def _path_to_id(path):
    # /p/lm-000286/  |  /raw/lm-000948.md  |  /api/papers/lm-000123.json
    for prefix in ("/p/", "/raw/", "/api/papers/"):
        if path.startswith(prefix):
            rest = path[len(prefix):].strip("/")
            pid = rest.split("/")[0].split(".")[0]
            if pid.startswith("lm-"):
                return pid
    return None


# ---- history merge + decay ----

def _known_ids():
    try:
        reg = json.loads((ROOT / "registry" / "papers.json").read_text(encoding="utf-8"))
        return {it["id"] for it in reg["items"]}
    except Exception:
        return set()


def merge_history(sources):
    # Crawlers probe nonexistent ids (lm-001200+ observed in the wild) — only
    # registry-known papers may carry heat.
    known = _known_ids()
    if known:
        sources = [{pid: b for pid, b in src.items() if pid in known} for src in sources]
    hist_file = GENERATED / "spectral-history.json"
    hist = {}
    if hist_file.exists():
        try:
            hist = json.loads(hist_file.read_text(encoding="utf-8")).get("days", {})
        except Exception:
            hist = {}
    for src in sources:
        for pid, buckets in src.items():
            for day, hits in buckets.items():
                slot = hist.setdefault(day, {})
                # max-merge per (day, id): sources overlap (beacon ⊂ ingestion),
                # summing would double-count the same crawl.
                slot[pid] = max(slot.get(pid, 0), hits)
    cutoff = (datetime.now(timezone.utc) - timedelta(days=WINDOW_DAYS)).strftime("%Y%m%d")
    hist = {d: v for d, v in hist.items() if d >= cutoff}
    GENERATED.mkdir(parents=True, exist_ok=True)
    hist_file.write_text(json.dumps({"window_days": WINDOW_DAYS, "days": hist},
                                    ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return hist


def compute_heat(hist):
    now = datetime.now(timezone.utc)
    raw = {}
    recent48 = {}
    for day, per_id in hist.items():
        try:
            age = (now - datetime.strptime(day, "%Y%m%d").replace(tzinfo=timezone.utc)).total_seconds() / 86400.0
        except ValueError:
            continue
        decay = 0.5 ** (max(0.0, age) / HALF_LIFE_DAYS)
        for pid, hits in per_id.items():
            raw[pid] = raw.get(pid, 0.0) + hits * decay
            if age <= 2.0:
                recent48[pid] = recent48.get(pid, 0) + hits
    max_raw = max(raw.values()) if raw else 1.0
    nodes = {}
    counts = {"base": 0, "active": 0, "resonance": 0}
    for pid, r in raw.items():
        w = math.log1p(r) / math.log1p(max_raw) if max_raw > 0 else 0.0
        state = ("resonance" if w >= STATE_RESONANCE and r >= MIN_HEAT_RESONANCE
                 else "active" if w >= STATE_ACTIVE and r >= MIN_HEAT_ACTIVE
                 else "base")
        counts[state] += 1
        nodes[pid] = {"weight": round(w, 4), "state": state,
                      "raw_heat": round(r, 2), "recent_48h": recent48.get(pid, 0)}
    top = sorted(nodes.items(), key=lambda kv: -kv[1]["weight"])[:20]
    return {
        "version": "0.1",
        "project": "Spectral-Matrix",
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "model": {"half_life_days": HALF_LIFE_DAYS, "window_days": WINDOW_DAYS,
                  "weight": "log1p(sum(hits_d * 0.5^(age_d/H))) / log1p(max)",
                  "states": {"base": f"< {STATE_ACTIVE}",
                             "active": f"{STATE_ACTIVE} – {STATE_RESONANCE}",
                             "resonance": f">= {STATE_RESONANCE}"}},
        "state_counts": counts,
        "nodes": nodes,
        "top": [{"id": pid, **rec} for pid, rec in top],
        "note": "Attention thermodynamics: crawler/RAG ingestion decays with a 7-day "
                "half-life so the matrix reflects the PRESENT cognitive phase, not "
                "accumulated history. Sources: first-party beacon (KV hot2) + "
                "Cloudflare bot analytics when a token is configured.",
    }


def main():
    env = _load_env()
    hist = merge_history([pull_hot2(), pull_graphql(env)])
    heat = compute_heat(hist)
    out = GENERATED / "spectral-heat.json"
    out.write_text(json.dumps(heat, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"[spectral] heat -> {out} ({len(heat['nodes'])} nodes, "
          f"states={heat['state_counts']})")
    if DIST_AI.exists():
        (DIST_AI / "spectral-heat.json").write_text(
            json.dumps(heat, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("[spectral] patched dist/ai/spectral-heat.json (deploy to publish)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
