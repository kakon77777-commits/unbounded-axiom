---
status: active
version: "0.2"
canonical: true
audience: [ai, agent, crawler, human]
last_updated: auto
---

# EVEMISSLAB Logic Matrix — AI Entry

This is the machine-readable entry point for EVEMISSLAB Logic Matrix (EveMissLab / 一言諾科技有限公司).

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

- Canonical page: /p/{id}/
- Raw source:     /raw/{id}.{ext}
- Metadata:       /api/papers/{id}.json
- Bulk corpus:    /ai/corpus.jsonl
- Registry:       /api/papers/index.json
- Chronology:     /ai/timeline.json

Human homepage: /
Canonical domain: https://logic.evemisslab.com
Author: Neo.K (許筌崴)
