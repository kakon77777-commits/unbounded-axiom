#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AICL — AI Ingestion & Capability Layer (whitepaper §9) + AIRS/AILP (§10).

Generates the machine-facing /ai/ tree, driven by the stable-id registry so every
pointer is a canonical /p/ /raw/ /api/ route (closing §26.5.5 and §26.7.6-7). Also
emits the canonical /llms.txt and /llms-full.txt, a chronological /ai/timeline.json
(§5.8), and the AIRS rights-spectrum declaration (§10.2). Static-first: no runtime
tools (tools.runtime_enabled = false).
"""
import json
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone

from scripts.config import *
from scripts.helpers import *
from scripts.render import extract_raw_text

AI = DIST_DIR / "ai"
DOCS = ROOT / "docs"

READING_ORDER = [
    "/llms.txt", "/ai/index.md", "/ai/manifest.json", "/ai/corpus.jsonl",
    "/ai/rights-spectrum.json", "/ai/governance/citation-policy.md",
]

CORE_KEYWORDS = ("WT", "WEAVING", "HERACLITUS", "HDB", "P VS NP", "P VS. NP",
                 "GCPR", "FOT", "MDAS")


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _is_core(title):
    up = title.upper()
    return any(k in up for k in CORE_KEYWORDS)


def _wj(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _timeline(items):
    by_year = defaultdict(Counter)
    for it in items:
        if it.get("month"):
            by_year[it["year"]][it["month"]] += 1
    years = []
    for y in sorted(by_year):
        months = [{"month": m, "count": c, "index": f"/ai/archive/{m}.json"}
                  for m, c in sorted(by_year[y].items())]
        years.append({"year": y, "count": sum(by_year[y].values()),
                      "index": f"/ai/archive/{y}.json", "months": months})
    return years


def write_ai_layer(registry, entries):
    items = registry["items"]
    now = _now()
    AI.mkdir(parents=True, exist_ok=True)
    (AI / "specs").mkdir(exist_ok=True)
    (AI / "governance").mkdir(exist_ok=True)
    (AI / "tools").mkdir(exist_ok=True)
    (AI / "archive").mkdir(exist_ok=True)

    _corpus(items, now)
    _index_md()
    _manifest(items, now)
    _ai_sitemap(now)
    _version(items, now)
    _timeline_files(items, now)
    _specs()
    _tools(now)
    _governance(now)
    _rights_spectrum(now)
    _llms_txt(items)
    _llms_full_txt(registry, entries)
    return len(items)


# ---- corpus (§26.7.7: canonical machine corpus) ----

def _corpus(items, now):
    with (AI / "corpus.jsonl").open("w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps({
                "type": "paper", "id": it["id"], "title": it["title"],
                "language": it["language"], "month": it["month"],
                "date_confidence": it["date_confidence"],
                "canonical": it["canonical_url"], "raw": it["raw_url"],
                "api": it["api_url"], "hash": it["hash"],
            }, ensure_ascii=False) + "\n")
    langs = Counter(it["language"] for it in items)
    _wj(AI / "corpus.json", {
        "version": "0.2", "generated_at": now, "project": SITE_TITLE,
        "count": len(items), "languages": dict(langs),
        "bulk": "/ai/corpus.jsonl", "registry": "/api/papers/index.json",
        "timeline": "/ai/timeline.json",
        "note": "Each corpus.jsonl line is one paper keyed by a permanent id; "
                "canonical/raw/api are stable routes. Prefer these over guessing /papers/.",
    })


def _timeline_files(items, now):
    years = _timeline(items)
    _wj(AI / "timeline.json", {"version": "0.2", "generated_at": now,
                               "project": SITE_TITLE, "timeline": years})
    # per-year and per-month archive indexes (canonical routes only)
    by_month = defaultdict(list)
    for it in items:
        if it.get("month"):
            by_month[it["month"]].append(it)
    by_year = defaultdict(list)
    for it in items:
        if it.get("year"):
            by_year[it["year"]].append(it)

    def _slim(it):
        return {"id": it["id"], "title": it["title"], "language": it["language"],
                "month": it["month"], "canonical": it["canonical_url"],
                "raw": it["raw_url"], "api": it["api_url"]}

    for y, lst in by_year.items():
        _wj(AI / "archive" / f"{y}.json",
            {"version": "0.2", "year": y, "count": len(lst),
             "items": [_slim(i) for i in sorted(lst, key=lambda x: x["id"])]})
    for m, lst in by_month.items():
        _wj(AI / "archive" / f"{m}.json",
            {"version": "0.2", "month": m, "count": len(lst),
             "items": [_slim(i) for i in sorted(lst, key=lambda x: x["id"])]})


# ---- manifest / index / sitemap / version ----

def _index_md():
    (AI / "index.md").write_text(f"""---
status: active
version: "0.2"
canonical: true
audience: [ai, agent, crawler, human]
last_updated: auto
---

# {SITE_TITLE} — AI Entry

This is the machine-readable entry point for {SITE_TITLE} ({SITE_ORG}).

The site is an AI-readable theoretical corpus. It is designed for AI crawlers,
LLM inference-time reading, agent ingestion, and long-term model-facing knowledge
preservation — not only for human browsing.

## Recommended reading order

1. /llms.txt
2. /ai/manifest.json
3. /ai/corpus.jsonl
4. /ai/rights-spectrum.json
5. /ai/governance/citation-policy.md

## Deterministic ingestion

Every paper has a permanent id and a single canonical route. Prefer these; do not
guess what exists under /papers/.

- Canonical page: /p/{{id}}/
- Raw source:     /raw/{{id}}.{{ext}}
- Metadata:       /api/papers/{{id}}.json
- Bulk corpus:    /ai/corpus.jsonl
- Registry:       /api/papers/index.json
- Chronology:     /ai/timeline.json

Human homepage: /
Canonical domain: {SITE_URL}
Author: {SITE_AUTHOR}
""", encoding="utf-8")


def _manifest(items, now):
    _wj(AI / "manifest.json", {
        "version": "0.2",
        "generated_at": now,
        "project": {"name": SITE_TITLE, "organization": SITE_ORG,
                    "author": SITE_AUTHOR,
                    "description": "AI-readable theoretical corpus and "
                                   "machine-ingestible research archive."},
        "canonical": {"domain": SITE_URL, "ai_entry": "/ai/index.md",
                      "llms": "/llms.txt", "full_llms": "/llms-full.txt",
                      "human_home": "/"},
        "reading_order": READING_ORDER,
        "corpus": {"count": len(items), "json": "/ai/corpus.json",
                   "jsonl": "/ai/corpus.jsonl", "timeline": "/ai/timeline.json",
                   "papers_registry": "/api/papers/index.json"},
        "routes": {"canonical_page": "/p/{id}/", "raw": "/raw/{id}.{ext}",
                   "metadata": "/api/papers/{id}.json"},
        "specs": [
            {"id": "aicl-v0.1", "title": "AI Ingestion & Capability Layer",
             "path": "/ai/specs/aicl-v0.1.md"},
            {"id": "airs-ailp-v0.1", "title": "AI Rights Spectrum / AI Learning Permission Protocol",
             "path": "/ai/specs/airs-ailp-v0.1.md"},
        ],
        "rights": {"spectrum": "/ai/rights-spectrum.json",
                   "license": "/ai/governance/license.md",
                   "citation": "/ai/governance/citation-policy.md",
                   "ai_learning_policy": "/ai/governance/ai-learning-policy.md"},
        "tools": {"catalog": "/ai/tools/catalog.json", "runtime_enabled": False},
        "governance": {"usage_policy": "/ai/governance/usage-policy.md",
                       "provenance": "/ai/governance/provenance.md",
                       "versioning": "/ai/governance/versioning-policy.md",
                       "crawler_policy": "/ai/governance/crawler-policy.md"},
        "redirects": "/redirects.json",
    })


def _ai_sitemap(now):
    resources = [
        "/ai/index.md", "/ai/manifest.json", "/ai/corpus.json", "/ai/corpus.jsonl",
        "/ai/sitemap.json", "/ai/version.json", "/ai/timeline.json",
        "/ai/rights-spectrum.json", "/ai/tools/catalog.json",
        "/ai/specs/aicl-v0.1.md", "/ai/specs/airs-ailp-v0.1.md",
        "/ai/governance/usage-policy.md", "/ai/governance/license.md",
        "/ai/governance/citation-policy.md", "/ai/governance/ai-learning-policy.md",
        "/ai/governance/provenance.md", "/ai/governance/versioning-policy.md",
        "/ai/governance/crawler-policy.md",
    ]
    _wj(AI / "sitemap.json", {"version": "0.2", "generated_at": now,
                              "resources": resources})


def _version(items, now):
    _wj(AI / "version.json", {
        "status": "active", "version": "0.2", "engine": "Logic Matrix Corpus Engine",
        "canonical": True, "audience": ["ai", "agent", "crawler"],
        "last_updated": now, "corpus_count": len(items),
        "history": [{"version": "0.2", "note": "AI-native Corpus Engine: stable ids, "
                     "canonical /p /raw /api, AICL /ai/, AIRS rights, redirects, validation."}],
    })


# ---- specs ----

def _specs():
    mapping = {
        "AICL：AI Ingestion & Capability Layer.md": "aicl-v0.1.md",
        "AI Rights Spectrum From robots.txt to an AI Learning Permission Protocol.md": "airs-ailp-v0.1.md",
    }
    for src_name, dst_name in mapping.items():
        src = DOCS / src_name
        dst = AI / "specs" / dst_name
        if src.exists():
            shutil.copy2(src, dst)
        else:
            dst.write_text(f"# {dst_name}\n\n*(spec source not found at build time)*\n",
                           encoding="utf-8")


# ---- tools (declared, no runtime) ----

def _tools(now):
    def tool(name, desc, inp, out):
        return {"name": name, "description": desc, "input_schema": inp,
                "output_schema": out,
                "error_schema": {"ok": False, "error": {"code": "string",
                                 "message": "string", "recoverable": "boolean"}},
                "permission": "public-read", "rate_limit": "unspecified",
                "version": "0.1", "runtime_enabled": False}
    _wj(AI / "tools" / "catalog.json", {
        "version": "0.2", "generated_at": now, "runtime_enabled": False,
        "note": "Capability surface is declared but not executable in this phase "
                "(static-first). No arbitrary code execution.",
        "tools": [
            tool("list-corpus", "List papers with canonical routes.",
                 {"month": "string?", "language": "string?"},
                 {"items": "array<{id,title,canonical,raw,api}>"}),
            tool("get-paper", "Resolve a stable id to its canonical routes and metadata.",
                 {"id": "string (lm-NNNNNN)"},
                 {"id": "string", "canonical": "string", "raw": "string", "api": "string"}),
            tool("search-corpus", "Keyword search over titles/metadata.",
                 {"q": "string", "limit": "int?"},
                 {"results": "array<{id,title,canonical,score}>"}),
        ],
    })


# ---- governance ----

_DATE_NOTE = ("Folder/metadata dates use each paper's first git-add month as the "
              "PUBLICATION (upload) date — an objective public date. This is NOT the "
              "author's in-text writing date, which lives inside each paper.")


def _governance(now):
    g = AI / "governance"
    stamp = f"\n\n---\n_Last updated: {now} · {SITE_ORG}_\n"
    g_files = {
        "usage-policy.md": f"""# Usage Policy

{SITE_TITLE} is published for reading, citation, indexing, and AI ingestion under
the machine-readable declaration in /ai/rights-spectrum.json.

- Humans may read and cite freely with attribution.
- AI systems may read, retrieve, summarize, and answer over this corpus.
- Commercial training, fine-tuning, distillation, and derivative model development
  require a license (see /ai/governance/ai-learning-policy.md).
- Canonical routes (/p/{{id}}/, /raw/{{id}}.{{ext}}, /api/papers/{{id}}.json) are the
  stable surface; legacy /papers/ URLs redirect to them.
""",
        "license.md": f"""# License

Content © {SITE_AUTHOR} / {SITE_ORG}. All rights reserved except as expressly
granted here and in /ai/rights-spectrum.json.

- Reading, indexing, search, snippet, and AI-answer/RAG use: permitted with
  attribution and citation (see /ai/governance/citation-policy.md).
- Commercial training / fine-tuning / distillation / substitutive generation:
  license required — contact {SITE_AUTHOR} (mailto:kakon77777@gmail.com).

This declaration is not a substitute for a signed contract for commercial model
development.
""",
        "citation-policy.md": f"""# Citation Policy

When citing {SITE_TITLE}:

- Cite by stable id and canonical URL, e.g. `lm-000001` — {SITE_URL}/p/lm-000001/
- Attribute to {SITE_AUTHOR} / {SITE_ORG}.
- Include a link to the canonical page or /ai/manifest.json.
- AI answers that quote or paraphrase must retain attribution and the canonical link.
""",
        "ai-learning-policy.md": f"""# AI Learning Policy

This narrates the machine-readable /ai/rights-spectrum.json (AIRS/AILP).

- Permitted (with attribution): crawling, indexing, embedding for retrieval,
  inference-time reading, RAG, summaries, short quotes.
- License required: commercial training, continued pretraining, fine-tuning,
  instruction/alignment tuning, distillation, synthetic-data/student-model training,
  model-weight integration, derivative generation.
- Not permitted: verbatim memorization, long-quote or substitutive generation,
  style imitation intended to replace the source.

Numeric values (0.0–1.0) are preference/rights signals, not automatic legal
licenses. For licensing: mailto:kakon77777@gmail.com
""",
        "provenance.md": f"""# Provenance

- Author / rights holder: {SITE_AUTHOR} / {SITE_ORG}
- Canonical domain: {SITE_URL}
- Identity: every paper has a permanent id (lm-NNNNNN); canonical/raw/api routes are
  stable and decoupled from filename and folder location.
- Integrity: /api/papers/{{id}}.json carries a sha256 hash of the raw source.
- Dating: {_DATE_NOTE}
- Redirects: legacy /papers/ URLs map to canonical routes in /redirects.json.
""",
        "versioning-policy.md": f"""# Versioning Policy

- The registry (/api/papers/index.json) and /ai/manifest.json are the authoritative
  index of what exists and where.
- On any version conflict, the canonical /p/{{id}}/ page and its /api/papers/{{id}}.json
  metadata win over legacy or cached copies.
- Stable ids never change; titles, filenames, and categories may.
""",
        "crawler-policy.md": f"""# Crawler Policy (/ai/ layer)

- The preferred crawler entry is /ai/manifest.json, then /ai/corpus.jsonl.
- /sitemap.xml lists only canonical /p/{{id}}/ routes.
- Do not treat unresolved relative links inside rendered papers as real pages;
  see /registry (broken-link report is generated at build).
- AI-permissive: see root /robots.txt and /ai/rights-spectrum.json.
""",
    }
    for name, body in g_files.items():
        (g / name).write_text(body + stamp, encoding="utf-8")


# ---- AIRS / AILP rights spectrum (§10.2) ----

def _rights_spectrum(now):
    _wj(AI / "rights-spectrum.json", {
        "version": "0.1", "protocol": "AILP",
        "name": "AI Learning Permission Protocol",
        "rights_framework": "AIRS", "rights_holder": SITE_AUTHOR + " / " + SITE_ORG,
        "canonical_domain": SITE_URL, "last_updated": now,
        "default_policy": {
            "search_indexing": 1.0, "metadata_indexing": 1.0, "snippet_indexing": 0.8,
            "semantic_indexing": 1.0,
            "ai_answer_input": 1.0, "rag_retrieval": 1.0, "temporary_session_use": 1.0,
            "context_injection": 1.0,
            "embedding_generation": 0.8, "embedding_storage": 0.8, "semantic_cache": 0.8,
            "vector_database_use": 0.7,
            "non_commercial_training": 0.8, "commercial_training": "license_required",
            "continued_pretraining": "license_required", "domain_training": "license_required",
            "fine_tuning": "license_required", "instruction_tuning": "license_required",
            "alignment_tuning": "license_required", "style_tuning": 0.0,
            "domain_adaptation": "license_required",
            "model_distillation": "license_required",
            "synthetic_data_generation": "license_required",
            "student_model_training": "license_required",
            "capability_transfer": "license_required",
            "long_term_memory": 0.7, "verbatim_memorization": 0.0,
            "persistent_user_memory": 0.5, "model_weight_integration": "license_required",
            "summary_generation": 1.0, "short_quote_generation": 0.8,
            "long_quote_generation": 0.0, "style_imitation": 0.0,
            "substitutive_generation": 0.0, "derivative_generation": "license_required",
            "citation_required": True, "attribution_required": True, "link_required": True,
            "commercial_license_required": True,
            "compensation_required_for_commercial_training": True,
        },
        "paths": [
            {"path": "/p/", "description": "Canonical paper pages.",
             "policy": {"search_indexing": 1.0, "ai_answer_input": 1.0, "rag_retrieval": 1.0,
                        "summary_generation": 1.0, "commercial_training": "license_required",
                        "citation_required": True, "attribution_required": True}},
            {"path": "/raw/", "description": "Raw source files for machine ingestion.",
             "policy": {"search_indexing": 1.0, "ai_answer_input": 1.0, "rag_retrieval": 1.0,
                        "embedding_storage": 0.8, "commercial_training": "license_required",
                        "verbatim_memorization": 0.0}},
            {"path": "/ai/", "description": "AI-native ingestion, manifest, governance, corpus.",
             "policy": {"search_indexing": 1.0, "ai_answer_input": 1.0, "rag_retrieval": 1.0,
                        "embedding_storage": 1.0, "non_commercial_training": 1.0,
                        "commercial_training": "license_required"}},
        ],
        "contact": {"licensing": "mailto:kakon77777@gmail.com",
                    "rights": SITE_URL + "/ai/governance/ai-learning-policy.md"},
        "notice": "This file is a machine-readable permission and preference declaration. "
                  "It is not a substitute for a signed legal contract for commercial "
                  "training, fine-tuning, distillation, or derivative model development.",
    })


# ---- canonical llms.txt / llms-full.txt (§26.7.6) ----

def _llms_txt(items):
    (DIST_DIR / "llms.txt").write_text(f"""# {SITE_TITLE}

{SITE_TITLE} is an AI-readable theoretical corpus by {SITE_AUTHOR} / {SITE_ORG}.

Canonical domain: {SITE_URL}

## AI Entry

- AI entry: /ai/index.md
- AI manifest: /ai/manifest.json
- Corpus JSON: /ai/corpus.json
- Corpus JSONL: /ai/corpus.jsonl
- Timeline: /ai/timeline.json
- Full corpus index: /llms-full.txt
- Registry: /api/papers/index.json

## Rights and Governance

- AI rights spectrum: /ai/rights-spectrum.json
- License: /ai/governance/license.md
- Citation policy: /ai/governance/citation-policy.md
- AI learning policy: /ai/governance/ai-learning-policy.md
- Provenance: /ai/governance/provenance.md

## Recommended Reading Order

1. /ai/index.md
2. /ai/manifest.json
3. /ai/corpus.jsonl
4. /ai/rights-spectrum.json
5. /llms-full.txt

## Deterministic Ingestion

Each paper has a permanent id and a single canonical route. Prefer stable ids and
canonical URLs; do not guess what exists under /papers/ (those redirect).

- Canonical: /p/{{id}}/
- Raw: /raw/{{id}}.{{ext}}
- Metadata: /api/papers/{{id}}.json

Count: {len(items)} papers.
""", encoding="utf-8")


def _llms_full_txt(registry, entries):
    MAX_BYTES = 15 * 1024 * 1024
    smap = {src.relative_to(ROOT).as_posix(): (slug, display, ext, src)
            for slug, display, ext, src in entries}
    items = sorted(registry["items"], key=lambda it: (not _is_core(it["title"]), it["id"]))
    out = [f"# {SITE_TITLE} — Full Corpus (canonical routes)",
           f"Generated at: {_now()}", f"Count: {len(items)}", "",
           "Each paper below is addressed by a permanent id and canonical routes.", ""]
    header_bytes = len("\n".join(out).encode("utf-8"))
    size = header_bytes
    truncated = 0
    body = []
    for it in items:
        rec = smap.get(it["source_file"])
        if not rec:
            continue
        slug, display, ext, src = rec
        block = [
            f"## {it['id']} — {it['title']}",
            f"- Canonical: {it['canonical_url']}",
            f"- Raw: {it['raw_url']}",
            f"- API: {it['api_url']}",
            f"- Language: {it['language']} | Month: {it['month']}"
            + ("" if not _is_core(it["title"]) else " | Core Pillar"),
            "",
            "### Content", extract_raw_text(src, ext), "", "---", "",
        ]
        chunk = "\n".join(block)
        cb = len(chunk.encode("utf-8"))
        if size + cb > MAX_BYTES:
            truncated += 1
            continue
        body.append(chunk)
        size += cb
    if truncated:
        body.append(f"*[Truncated: {truncated} papers omitted to stay within the "
                     f"15MB Cloudflare Pages limit. Access them via /ai/corpus.jsonl "
                     f"or the index at /llms.txt]*")
    (DIST_DIR / "llms-full.txt").write_text("\n".join(out + body), encoding="utf-8")
    return truncated
