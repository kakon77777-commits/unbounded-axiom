#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Research Program layer — AI Layer v0.2 MVP.

A Program is a persistent, open-ended AI-native research lineage (as opposed to a
one-shot paper): a sequence of research "iterations" (graph-update events, not
necessarily standalone-readable) that share a permanent Program id and converge on
periodic "checkpoint" states. This is a distinct object from a Paper — a Program's
identity does NOT change as new iterations are added, and it does not presuppose a
fixed endpoint (`open_ended: true`).

Design + first reference implementation (FMO) specified in Neo.K & Aletheia's
"Logic Matrix AI Layer v0.2" white paper (2026-07-19). This module implements the
MVP scope only (Program registry + Artifact mapping + latest-state + integrity
report + human/machine routes) — NOT the full graph-diff / branch / contribution-
ledger machinery from the white paper's later phases, which is deliberately deferred.

Source of truth: registry/programs/*.json (hand-authored program seeds, one file per
program, each a dict with at minimum {id, title, status, iterations: [...]}). This
module resolves each iteration/foundation/applied artifact's `id` against the paper
registry (canonical_url, raw_url, title, authorship, month) and emits the machine +
human-consumable outputs. It does NOT touch content/papers/ or registry/papers.json.

Outputs:
    dist/ai/programs/index.json                 all programs, summary form
    dist/ai/programs/{id}.json                   full enriched program object
    dist/ai/programs/{id}/latest-state.json      current_state + resolved checkpoint artifact
    dist/ai/programs/{id}/artifacts.json         every resolved artifact (foundation+iteration+applied)
    dist/ai/programs/{id}/open-issues.json       current_state.unresolved_gaps + next_actions
    dist/ai/programs/{id}/timeline.json          iterations in sequence order, resolved
    dist/ai/programs/{id}/integrity-report.json  missing/duplicate/hash-conflict record (warn-only, never silently "fixed")
"""
import json
from datetime import datetime, timezone

from scripts.config import *

PROGRAMS_DIR = ROOT / "registry" / "programs"


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_program_seeds() -> list:
    """Every hand-authored registry/programs/*.json seed file."""
    if not PROGRAMS_DIR.exists():
        return []
    seeds = []
    for p in sorted(PROGRAMS_DIR.glob("*.json")):
        try:
            seeds.append(json.loads(p.read_text(encoding="utf-8")))
        except Exception as e:
            print(f"[warn] programs: failed to parse {p} — {e}")
    return seeds


def _resolve(art: dict, by_id: dict) -> dict:
    """Merge a seed artifact stub {id, title, ...} with its live registry entry."""
    rid = art.get("id")
    live = by_id.get(rid)
    resolved = dict(art)
    if live is None:
        resolved["_unresolved"] = True
        return resolved
    resolved.update({
        "canonical_url": live["canonical_url"],
        "raw_url": live["raw_url"],
        "api_url": live["api_url"],
        "authorship": live.get("authorship", "collaborative"),
        "month": live.get("month"),
        "language": live.get("language"),
    })
    return resolved


def write_programs(registry, build_id=None) -> dict:
    """Emit /ai/programs/ for every registry/programs/*.json seed. Returns
    {"programs": int, "iterations": int, "missing": int, "unresolved_refs": [..]}."""
    seeds = load_program_seeds()
    by_id = {it["id"]: it for it in registry["items"]}

    out_dir = DIST_DIR / "ai" / "programs"
    out_dir.mkdir(parents=True, exist_ok=True)

    index_entries = []
    unresolved_refs = []
    total_iterations = 0
    total_missing = 0

    for seed in seeds:
        pid = seed["id"]
        prog_dir = out_dir / pid.replace("rp-", "")

        foundation = [_resolve(a, by_id) for a in seed.get("foundation_artifacts", [])]
        applied = [_resolve(a, by_id) for a in seed.get("applied_artifacts", [])]
        iterations = [_resolve(a, by_id) for a in seed.get("iterations", [])]
        all_artifacts = foundation + applied + iterations

        for a in all_artifacts:
            if a.get("_unresolved"):
                unresolved_refs.append(f"{pid}:{a.get('id')}")

        total_iterations += len(iterations)
        integrity = seed.get("integrity", {})
        total_missing += len(integrity.get("missing_sequences", []))

        current_state = dict(seed.get("current_state", {}))
        ckpt_id = current_state.get("artifact_id")
        current_state["artifact"] = next((a for a in iterations if a.get("id") == ckpt_id), None)

        full = dict(seed)
        full["foundation_artifacts"] = foundation
        full["applied_artifacts"] = applied
        full["iterations"] = iterations
        full["current_state"] = current_state
        full["generated_at"] = _now()

        # {id}.json — full enriched program object
        (out_dir / f"{pid}.json").write_text(
            json.dumps(full, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        prog_dir.mkdir(parents=True, exist_ok=True)

        (prog_dir / "latest-state.json").write_text(
            json.dumps({"program_id": pid, "generated_at": _now(), **current_state},
                       ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        (prog_dir / "artifacts.json").write_text(
            json.dumps({
                "program_id": pid, "generated_at": _now(),
                "foundation": foundation, "applied": applied, "iterations": iterations,
            }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        (prog_dir / "open-issues.json").write_text(
            json.dumps({
                "program_id": pid, "generated_at": _now(),
                "unresolved_gaps": current_state.get("unresolved_gaps", []),
                "next_actions": current_state.get("next_actions", []),
                "handoff_required_tasks": current_state.get("handoff_required_tasks", []),
            }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        (prog_dir / "timeline.json").write_text(
            json.dumps({
                "program_id": pid, "generated_at": _now(),
                "iterations": sorted(iterations, key=lambda a: a.get("sequence", 0)),
            }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        # integrity report — files_seen/imported come from the seed (author-declared at
        # ingest time); missing/duplicate records are NEVER silently dropped or renumbered.
        (prog_dir / "integrity-report.json").write_text(
            json.dumps({
                "program_id": pid, "generated_at": _now(),
                **integrity,
                "unresolved_artifact_refs": [a.get("id") for a in all_artifacts if a.get("_unresolved")],
            }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        index_entries.append({
            "id": pid,
            "title": seed.get("title"),
            "short_title": seed.get("short_title"),
            "type": seed.get("type"),
            "status": seed.get("status"),
            "open_ended": seed.get("open_ended", False),
            "canonical_route": seed.get("canonical_route"),
            "iteration_count": len(iterations),
            "foundation_count": len(foundation),
            "current_sequence": current_state.get("sequence"),
            "missing_sequences": integrity.get("missing_sequences", []),
        })

    (out_dir / "index.json").write_text(
        json.dumps({
            "version": "0.2", "generated_at": _now(), "build_id": build_id,
            "note": "AI-native research programs — persistent, open-ended research lineages, "
                    "distinct from one-shot papers. See /ai/manifest.json capabilities.research_programs.",
            "count": len(index_entries),
            "programs": index_entries,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if unresolved_refs:
        print(f"[warn] programs: {len(unresolved_refs)} artifact ref(s) did not resolve against the paper registry: {unresolved_refs}")

    return {
        "programs": len(index_entries),
        "iterations": total_iterations,
        "missing": total_missing,
        "unresolved_refs": unresolved_refs,
    }
