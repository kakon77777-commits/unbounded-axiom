# Dynamic Semantic Revealing — search layer

Implements Phase 0 + Phase 1 of `lm-001785` (`02_動態語義顯影_本地端實作技術白皮書_v0.1`).
Live on `/timeline/` as an additive layer over the existing paper list — same URLs,
same DOM, same page when JS is off or the flag below is `false`.

## What's shipped (Phase 0 + 1)

- **Index**: `scripts/semantic_layer.py` extracts title/date/url/headings/summary/keywords
  from every paper (YAML frontmatter keywords when present, deterministic heuristics
  otherwise — every derived field is source-tagged `author_declared` vs `system_inferred`,
  §5). Real relations (`related_ids`) come only from `registry/programs/*.json` membership —
  never guessed. Runs on every `python build.py`, writes:
  - `registry/generated/semantic-documents.raw.jsonl` — full record (§4.1), one per paper
  - `dist/ai/semantic-index.min.json` — compressed record (§4.2), fetched by the browser
- **Retrieval**: `semantic-core.js` — exact + lexical (CJK bigram / trigram / token-overlap)
  channels, tiered A/B/C/D scoring (§10), non-zero result guarantee with honest
  relaxed/low-confidence disclosure (§11). Runs in a Web Worker (`lexical-search-worker.js`)
  so 1862 documents score off the main thread.
- **UI**: `semantic-filter.js` / `.css` — search box, 300ms debounce, reveal vs
  focus-only modes, per-row hit-reason label, tier-stat line, non-zero banners.
  Tags each `.paper-row` with `data-semantic-score` / `-tier` / `-visible` (§14.2).

## Not shipped (Phase 2–5 — see §26 of the spec)

- Dictionary/alias expansion (Phase 2) — `channels.semantic`/dictionary in
  `search.config.json` stay off; a query only matches text that's actually in the index.
- Vector/embedding semantic search (Phase 3) — natural-language paraphrase queries with
  little lexical overlap correctly degrade to a disclosed low-confidence fallback instead
  of faking understanding they don't have (see `tests/semantic_queries.jsonl`,
  `natural_language` category).
- Full relation graph + diversity rerank (Phase 4) — relations exist only for papers that
  belong to a `registry/programs/*.json` Program (~70 of 1862 papers today).
- Full-text chunking + quality dashboard (Phase 5).

## Deploy

Part of the normal site build — no separate step:
```
bash build-site.sh   # engine writes dist/ai/semantic-index.min.json; astro copies public/semantic/* -> dist/semantic/*
bash deploy.sh        # build + wrangler deploy + scripts/verify_deploy.py (checks semantic-index.min.json's build_id too)
```

## Rollback

Single flag, per spec §28.1 — no code change needed:
```json
// shell/public/semantic/search.config.json
{ "semantic_search_enabled": false }
```
With it `false`, `semantic-filter.js` hides the search box and never starts the Worker.
The timeline is the plain original page — no URLs changed, nothing else touched (§28.2).

## Known limitations

- ~8 of 1862 papers (0.4%) get a very short/low-signal auto-extracted summary due to
  unusual source formatting (see `registry/generated/semantic-documents.raw.jsonl`,
  `metadata.summary_source: "unavailable"` or a <16-char summary) — title/headings/keywords
  still work fine for search on these, only the displayed summary snippet is thin.
- Typo tolerance is a side effect of CJK bigram/trigram overlap, not a real edit-distance
  matcher — a single wrong character usually still surfaces the right document at a lower
  tier, but this isn't guaranteed for very short queries.
- `related_ids` (Tier D "same series") only exist for the ~70 papers already registered in
  a Research Program — most of the corpus has no relation signal yet, which is honest
  (§9.4 "近似必須被標示"), not a bug.

## Tests

`tests/semantic_queries.jsonl` (33 cases: exact/alias/natural-language/typo/zero-data/
edge-case/cross-domain) run against the real built index through the exact same
`semantic-core.js` the browser imports:
```
node tests/test_semantic_search.mjs   # writes tests/quality-report.json
```
Latest run: 33/33 passed.
