#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Graph Layer — real theory-dependency topology for base-space (handoff spec §4, Phase A).

Aggregates per-paper TCF-lite extractions (registry/tcf/<id>.json, produced by the
§25-governed agent pipeline) into one machine-readable dependency graph at
dist/ai/graph.json. Edges come from two evidence-backed sources only:

  1. explicit external_refs  (paper A cites/depends on paper B, with a verbatim quote)
  2. shared-concept links    (A uses a canonical concept that B defines)

Every edge carries evidence traceable to the source paper. Nodes are marked with the
Triadic-Logic state "omega" (Ω = extracted draft, under revision) — no node is claimed
⊤/⊥ until the Phase E Lean loop / Phase C adversarial consensus exists. Papers without
a TCF extraction are simply absent (honest sparse coverage), never faked.

Also patches /ai/manifest.json + /ai/sitemap.json with the graph pointer so AICL
readers can discover it. Static-first: no runtime tools.
"""
import json
from datetime import datetime, timezone

from scripts.config import *

TCF_DIR = ROOT / "registry" / "tcf"
VERDICTS_FILE = ROOT / "registry" / "tcf" / "edge-verdicts.json"
GENERATED_DIR = ROOT / "registry" / "generated"
AI = DIST_DIR / "ai"

# ref-type -> base weight (multiplied by extractor confidence)
REF_WEIGHTS = {
    "depends_on": 0.9,
    "extends": 0.85,
    "verifies": 0.8,
    "applies": 0.7,
    "critiques": 0.6,
}
CONCEPT_WEIGHT = {"uses": 0.5, "extends": 0.6}
# a canonical concept "defined" by more papers than this is too generic to be an edge
MAX_DEFINERS_PER_CONCEPT = 6
MAX_EVIDENCE_PER_EDGE = 3


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_tcf_files():
    """Read every registry/tcf/<id>.json; return ({id: tcf}, [parse errors])."""
    tcfs, errors = {}, []
    if not TCF_DIR.exists():
        return tcfs, errors
    for path in sorted(TCF_DIR.glob("lm-*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            pid = data.get("id") or path.stem
            if pid != path.stem:
                errors.append(f"{path.name}: id field '{pid}' != filename")
                pid = path.stem
            tcfs[pid] = data
        except Exception as e:  # broken extraction must not break the build
            errors.append(f"{path.name}: {e}")
    return tcfs, errors


def _clip(text, n=200):
    text = (text or "").strip()
    return text if len(text) <= n else text[: n - 1] + "…"


def _concept_index(tcfs):
    """canonical concept -> {'defined_by': [(id, quote)], 'used_by': [(id, role, quote)]}

    De-duplicated per paper: a paper listing the same canonical concept several
    times (e.g. nine UDAE sub-concepts all mapped to canonical "UDAE") counts as
    ONE definer/user, otherwise the generic-concept cap misfires.
    """
    index = {}
    for pid, tcf in tcfs.items():
        for c in tcf.get("concepts", []) or []:
            canon = (c.get("canonical") or c.get("name") or "").strip()
            if not canon:
                continue
            slot = index.setdefault(canon, {"defined_by": [], "used_by": []})
            role = c.get("role", "uses")
            quote = _clip(c.get("evidence", ""))
            if role == "defines":
                if all(d[0] != pid for d in slot["defined_by"]):
                    slot["defined_by"].append((pid, quote))
            else:
                if all(u[0] != pid for u in slot["used_by"]):
                    slot["used_by"].append((pid, role, quote))
    return index


def _build_edges(tcfs, index, registry_ids):
    edges = {}       # (from, to) -> edge dict
    unresolved = []  # refs we could not map to a mapped node

    def add_edge(src, dst, etype, weight, evidence, concept=None):
        if src == dst or dst not in tcfs:
            return
        key = (src, dst)
        e = edges.get(key)
        ev = dict(evidence)
        if concept:
            ev["concept"] = concept
        if e is None:
            edges[key] = {
                "from": src, "to": dst, "types": [etype],
                "weight": round(min(1.0, weight), 3), "evidence": [ev],
            }
        else:
            if etype not in e["types"]:
                e["types"].append(etype)
            e["weight"] = round(min(1.0, max(e["weight"], weight)), 3)
            if len(e["evidence"]) < MAX_EVIDENCE_PER_EDGE:
                e["evidence"].append(ev)

    for pid, tcf in tcfs.items():
        for ref in tcf.get("external_refs", []) or []:
            target = (ref.get("target") or "").strip()
            etype = ref.get("type", "depends_on")
            conf = ref.get("confidence", 0.8)
            try:
                conf = max(0.0, min(1.0, float(conf)))
            except (TypeError, ValueError):
                conf = 0.8
            base = REF_WEIGHTS.get(etype, 0.7)
            quote = _clip(ref.get("evidence", ""))
            evidence = {"kind": "external_ref", "quote": quote}

            if target.startswith("lm-"):
                if target in tcfs:
                    add_edge(pid, target, etype, base * conf, evidence)
                else:
                    unresolved.append({"from": pid, "target": target, "type": etype,
                                       "reason": "target paper not yet TCF-mapped"
                                       if target in registry_ids else "unknown id"})
            elif target:
                # concept-name target: resolve through the definers of that concept
                definers = index.get(target, {}).get("defined_by", [])
                if 0 < len(definers) <= MAX_DEFINERS_PER_CONCEPT:
                    for d_pid, d_quote in definers:
                        add_edge(pid, d_pid, etype, base * conf * 0.9, evidence, concept=target)
                else:
                    unresolved.append({"from": pid, "target": target, "type": etype,
                                       "reason": "concept with no (or too many) definers in mapped set"})

    dropped_generic = []
    for canon, slot in index.items():
        definers = slot["defined_by"]
        if not definers:
            continue
        if len(definers) > MAX_DEFINERS_PER_CONCEPT:
            dropped_generic.append(canon)
            continue
        for u_pid, role, u_quote in slot["used_by"]:
            w = CONCEPT_WEIGHT.get(role, 0.5)
            for d_pid, d_quote in definers:
                add_edge(u_pid, d_pid, "concept_dependency", w,
                         {"kind": "shared_concept", "use_quote": u_quote, "def_quote": d_quote},
                         concept=canon)

    edge_list = sorted(edges.values(), key=lambda e: (e["from"], e["to"]))
    for e in edge_list:
        e["type"] = e.pop("types")[0] if len(e["types"]) == 1 else "+".join(sorted(e.pop("types")))
    return edge_list, unresolved, dropped_generic


def _load_verdicts():
    if not VERDICTS_FILE.exists():
        return {}
    try:
        return json.loads(VERDICTS_FILE.read_text(encoding="utf-8")).get("audited", {})
    except Exception:
        return {}


def _gate_edges(candidates, verdicts):
    """Adversarial-verification gate (handoff spec §10: 邊要可被否決).

    Every candidate edge must have been audited by a skeptic agent before it may
    enter the published graph. The dominant failure mode the audit catches is
    homonym collision — two papers using the same term (底空間, 算子本體論, …)
    for different constructs — which no deterministic joiner can rule out.

      ok      -> published as-is
      weak    -> published at reduced weight, annotated
      wrong   -> rejected (kept in the report with the auditor's reason)
      missing -> pending_audit (NOT published; audit debt is visible, not silent)
    """
    published, rejected, pending = [], [], []
    for e in candidates:
        key = e["from"] + "->" + e["to"]
        v = verdicts.get(key)
        if v is None:
            pending.append(e)
        elif v["verdict"] == "ok":
            e["verification"] = {"verdict": "ok", "method": "adversarial-agent-audit"}
            published.append(e)
        elif v["verdict"] == "weak":
            e["weight"] = round(e["weight"] * 0.6, 3)
            e["verification"] = {"verdict": "weak", "method": "adversarial-agent-audit",
                                 "note": _clip(v.get("reason", ""), 240)}
            published.append(e)
        else:
            rejected.append({"edge": key, "type": e["type"],
                             "reason": _clip(v.get("reason", ""), 400)})
    return published, rejected, pending


# Curated Phase A cluster map (semantic slicing for the spectral matrix).
CLUSTERS = {
    "closure":   ["lm-000049", "lm-001089", "lm-001090", "lm-000464", "lm-001060", "lm-001088"],
    "tcf_fdrs":  ["lm-000776", "lm-000457", "lm-000456", "lm-000075", "lm-000076", "lm-000712", "lm-000063"],
    "triadic":   ["lm-000870", "lm-000215", "lm-000095", "lm-000273", "lm-000293", "lm-000096"],
    "basespace": ["lm-000155", "lm-000154", "lm-000152", "lm-000477", "lm-000329", "lm-000325", "lm-000478", "lm-000291"],
    "eml":       ["lm-001149", "lm-001148", "lm-000058", "lm-000060", "lm-000526"],
    "operator":  ["lm-000069", "lm-000071", "lm-000924", "lm-000567"],
    "governance": ["lm-000301", "lm-000450", "lm-000150", "lm-000017", "lm-000036"],
    "computation": ["lm-000119", "lm-000112", "lm-000630"],
    "unified":   ["lm-000880", "lm-000689"],
}
CLUSTER_OF = {pid: c for c, ids in CLUSTERS.items() for pid in ids}


def _spectral_order(node_ids, edges):
    """Fiedler-vector ordering (graph Laplacian, pure-python power iteration).

    Strongly coupled papers end up adjacent, so dense causal blocks emerge on
    the matrix diagonal ("theory nebulae"). 46 nodes -> trivial compute.
    """
    n = len(node_ids)
    if n < 3:
        return list(node_ids)
    idx = {pid: i for i, pid in enumerate(node_ids)}
    W = [[0.0] * n for _ in range(n)]
    for e in edges:
        i, j = idx.get(e["from"]), idx.get(e["to"])
        if i is None or j is None or i == j:
            continue
        w = max(W[i][j], float(e.get("weight", 0.5)))
        W[i][j] = W[j][i] = w
    deg = [sum(row) for row in W]
    shift = 1.1 * max(deg) if max(deg) > 0 else 1.0
    # B = shift*I - L ; largest eigenvector of B (after deflating the constant
    # vector) approximates the Fiedler vector of L.
    import math
    v = [math.sin(i + 1.0) for i in range(n)]  # deterministic pseudo-random start
    ones = 1.0 / math.sqrt(n)
    for _ in range(400):
        mean = sum(v) / n
        v = [x - mean for x in v]                     # deflate constant component
        nv = [0.0] * n
        for i in range(n):
            acc = (shift - deg[i]) * v[i]
            row = W[i]
            for j in range(n):
                if row[j]:
                    acc += row[j] * v[j]
            nv[i] = acc
        norm = math.sqrt(sum(x * x for x in nv)) or 1.0
        v = [x / norm for x in nv]
    return [pid for _, pid in sorted(zip(v, node_ids))]


def _copy_spectral_heat():
    """Ship the locally generated heat file (scripts/spectral_pull.py) with the build."""
    src = GENERATED_DIR / "spectral-heat.json"
    if src.exists():
        (AI / "spectral-heat.json").write_text(src.read_text(encoding="utf-8"),
                                               encoding="utf-8")
        return True
    return False


def _patch_ai_pointers(total_mapped):
    """Add /ai/graph.json to the AICL manifest + sitemap (after write_ai_layer ran)."""
    manifest_path = AI / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest.setdefault("corpus", {})["dependency_graph"] = "/ai/graph.json"
        manifest["corpus"]["dependency_graph_note"] = (
            f"Real TCF-extracted theory-dependency topology (Phase A prototype, "
            f"{total_mapped} papers mapped). Evidence-backed edges; Ω = draft state.")
        manifest["corpus"]["demand_queue"] = "/api/tcf-queue"
        manifest["corpus"]["demand_queue_note"] = (
            "Lazy TCF instantiation: hollow nodes ranked by ~48h crawler attention; "
            "hottest papers are distilled first (docs/TCF-demand-queue-runbook.md).")
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                                 encoding="utf-8")
    sitemap_path = AI / "sitemap.json"
    if sitemap_path.exists():
        sitemap = json.loads(sitemap_path.read_text(encoding="utf-8"))
        if "/ai/graph.json" not in sitemap.get("resources", []):
            sitemap["resources"].append("/ai/graph.json")
        sitemap_path.write_text(json.dumps(sitemap, ensure_ascii=False, indent=2) + "\n",
                                encoding="utf-8")


def write_graph_layer(registry):
    """Build dist/ai/graph.json from registry/tcf/*.json. Returns stats dict.

    Called after write_ai_layer (needs dist/ai/ to exist). If no TCF extractions
    exist yet, writes nothing and the Worker/front-end fall back to the old
    simulated seed — the graph never lies about coverage.
    """
    tcfs, parse_errors = _load_tcf_files()
    stats = {"mapped": 0, "edges": 0, "errors": parse_errors}
    if not tcfs:
        return stats

    registry_ids = {it["id"] for it in registry["items"]}
    by_id = {it["id"]: it for it in registry["items"]}
    index = _concept_index(tcfs)
    candidates, unresolved, dropped_generic = _build_edges(tcfs, index, registry_ids)
    edge_list, rejected, pending = _gate_edges(candidates, _load_verdicts())

    nodes = []
    for pid in sorted(tcfs.keys()):
        tcf = tcfs[pid]
        reg = by_id.get(pid, {})
        nodes.append({
            "id": pid,
            "title": reg.get("title") or tcf.get("title", pid),
            "theory_name": tcf.get("theory_name", ""),
            "cluster": CLUSTER_OF.get(pid, "other"),
            "canonical": reg.get("canonical_url", f"/p/{pid}/"),
            # Triadic Logic: Ω = extracted draft, unresolved tension; ⊤/⊥ are reserved
            # for the Phase C/E verification loops (multi-agent consensus / Lean).
            "state": "omega",
            "state_basis": "tcf-extracted-draft",
            "counts": {
                "primitives": len(tcf.get("primitives", []) or []),
                "axioms": len(tcf.get("axioms", []) or []),
                "theorems": len(tcf.get("theorems", []) or []),
                "concepts": len(tcf.get("concepts", []) or []),
            },
        })

    concept_summary = {
        canon: {
            "defined_by": [pid for pid, _ in slot["defined_by"]],
            "used_by": sorted({pid for pid, _, _ in slot["used_by"]}),
        }
        for canon, slot in sorted(index.items())
        if slot["defined_by"] or len(slot["used_by"]) > 1
    }

    graph = {
        "version": "0.1",
        "generated_at": _now(),
        "project": SITE_TITLE,
        "method": ("TCF-lite automated distillation (Phase A). Candidate edges = explicit "
                   "evidence-backed external_refs + shared-canonical-concept links "
                   "(user -> definer). EVERY published edge passed a per-edge adversarial "
                   "agent audit (homonym-collision screen); rejected/pending edges are in "
                   "registry/generated/graph-report.json. Node state omega = extracted "
                   "draft; truth states await the verification loops (handoff spec §5)."),
        "provenance": {
            "extractor": "claude-fable-5 + sonnet agents (automated, adversarially verified per edge)",
            "pipeline": "registry/tcf/<id>.json -> scripts/graph_layer.py -> verdict gate -> /ai/graph.json",
            "governance": "agents propose, gates decide — see /ai/rights-spectrum.json",
        },
        "coverage": {
            "papers_total": registry["count"],
            "papers_mapped": len(nodes),
            "note": "Unmapped papers are absent, not zero-weighted: absence of an edge "
                    "means 'not yet extracted', never 'no dependency'.",
        },
        "nodes": nodes,
        "edges": edge_list,
        "spectral_order": _spectral_order([n["id"] for n in nodes], edge_list),
        "clusters": {c: [pid for pid in ids if pid in tcfs] for c, ids in CLUSTERS.items()},
        "concept_index": concept_summary,
    }
    AI.mkdir(parents=True, exist_ok=True)
    (AI / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=1) + "\n",
                                   encoding="utf-8")

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "generated_at": graph["generated_at"],
        "mapped": len(nodes), "edges": len(edge_list),
        "candidates": len(candidates),
        "rejected_edges": rejected,
        "pending_audit": pending,
        "unresolved_refs": unresolved,
        "dropped_generic_concepts": dropped_generic,
        "tcf_parse_errors": parse_errors,
    }
    (GENERATED_DIR / "graph-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    _patch_ai_pointers(len(nodes))
    _copy_spectral_heat()

    stats.update({"mapped": len(nodes), "edges": len(edge_list),
                  "candidates": len(candidates), "rejected": len(rejected),
                  "pending_audit": len(pending), "unresolved": len(unresolved)})
    return stats
