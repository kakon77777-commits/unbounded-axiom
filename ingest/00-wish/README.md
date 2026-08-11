# ingest/00-wish/

Cross-session handoff staging area — a place for Neo to drop papers that
another Claude Code conversation has already pre-formatted (author /
institution / date bylines added, per the corpus's standard header
convention) before handing them to *this* pipeline for full content
review and publish.

## Convention

- One subfolder per series/collection, named however makes sense (matches
  `attachments-pending/`'s convention — no fixed naming rule).
- Files inside are expected to already carry a proper byline block. This
  session still does its normal Stage 1 dedup + content review (math
  corruption, duplicate check, structural sanity) — pre-formatting only
  covers the header metadata, not content correctness.
- Same `--source` flow as any other source: `python scripts/ingest.py
  --source 00-wish [--ctcl-instant-file f.json]`, then the usual
  review → publish → build → deploy cycle.

## Lifecycle

**This folder itself is a standing fixture — do not delete it after a
batch clears.** Only delete the individual files/subfolders once their
content is confirmed published in `content/papers/` (matching how
`attachments-pending/` is cleaned per-item, not as a whole directory).
This distinction exists because a prior session deleted the whole folder
after clearing it once, which briefly worried Neo before he confirmed the
underlying content was safe (it was — everything was already committed to
`content/papers/`) and asked for it back.

This README is git-tracked (see `.gitignore`); everything else placed
here is not — the canonical home for published content is always
`content/papers/`.
