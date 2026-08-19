# AI_HANDOFF — GCORF-00 v0.1

## Mandatory handling rules

1. Treat `paper.md` as the primary readable artifact.
2. This package is **pre-canonical**. Do not invent an SSSP revision, immutable snapshot URI, canonical hash, or canonical validation result.
3. Before editing, verify `CHECKSUMS.sha256` or run `python tools/verify_package.py`.
4. Preserve formal mathematics exactly as source text using `$...$` and `$$...$$`.
5. Never convert LaTeX to Unicode mathematical glyphs and then treat the Unicode rendering as the new formal source.
6. Never perform `unicode_escape` round trips on scholarly source.
7. Never silently rewrite LaTeX backslashes, delimiters, spacing, or line structure inside formulas.
8. Do not rebuild formal source from rendered chat, screenshots, HTML, or a visual Markdown preview when this package is available.
9. `provenance/normalization.diff` is mechanical evidence. If `paper.md` or its upstream source changes, regenerate it rather than describing changes only in prose.
10. `provenance/math_inventory.json` must be mechanically regenerated after any math edit.
11. Do not overwrite provenance files merely to make an edited artifact appear canonical.
12. After modification, create a new version/package and preserve the prior package as immutable input evidence.
13. Keep validation scopes explicit: artifact validation is not canonical SSSP validation.
14. Do not infer semantic equivalence, proof correctness, or scholarly truth from matching hashes or delimiter checks.

## Recommended @SSSP ingestion path

```text
verify portable package
    -> ingest staged source
    -> validate canonical typed source
    -> commit immutable SSSP revision
    -> export canonical Markdown
    -> replace staged upstream export with true SSSP export
    -> regenerate normalization diff + math inventory + validation + checksums
    -> emit canonical release package
```
