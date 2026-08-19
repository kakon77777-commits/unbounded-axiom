# AI_HANDOFF — GCORF-01 v0.1

## Status

This package is prepared for downstream review and SSSP MCP ingestion. It is **not itself evidence of an SSSP canonical commit**.

## Editing rules

1. Treat `paper.md` as the primary scholarly artifact in this package.
2. Preserve UTF-8.
3. Preserve inline math `$...$` and display math `$$...$$`.
4. Do not silently replace LaTeX commands with Unicode math glyphs.
5. Do not use `unicode_escape` round trips.
6. Do not silently normalize backslashes, delimiters, or formula spacing.
7. Any substantive edit must produce a new declared version.
8. Preserve rejected, uncertain, and negative evidence states; do not silently upgrade them.
9. Do not convert BehavioralInference or LatentHypothesis into Direct evidence without new provenance.
10. Before using a new operator as atomic, run the existing-library / implementation-mode checks described in the paper.
11. Verify `CHECKSUMS.sha256` before editing or importing.
12. When committing through SSSP MCP, record the actual canonical revision/hash returned by that runtime; never fabricate one from this archive.
