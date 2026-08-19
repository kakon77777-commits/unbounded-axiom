# GCORF-00 v0.1 — SSSP-Compatible Pre-Canonical Handoff

This archive is a portable scholarly handoff package for:

**GCORF-00 — 通用認知算子逆向框架：總綱、範圍與非主張**

## Important status

This archive is **NOT** claiming that a live SSSP canonical revision has already been created.

The current package freezes a UTF-8 Markdown staging source and provides reproducible artifact-level validation so that `@SSSP` or a downstream maintainer can ingest it without reconstructing formal source from chat.

- Primary readable artifact: `paper.md`
- Staged upstream source slot: `provenance/sssp_export_raw.md`
- Live SSSP canonical revision: **not assigned**
- Canonical SSSP validation: **not run in this environment**
- Portable artifact validation: mechanically generated and reproducible

## Package layout

```text
GCORF-00_v0.1_SSSP_Handoff/
├── paper.md
├── README.md
├── AI_HANDOFF.md
├── SSSP_IMPORT_NOTE.md
├── manifest.json
├── validation.json
├── CHECKSUMS.sha256
├── provenance/
│   ├── sssp_export_raw.md
│   ├── normalization.diff
│   ├── normalization_manifest.json
│   ├── math_inventory.json
│   └── source_map.md
└── tools/
    └── verify_package.py
```

## Verification

From the extracted package root:

```bash
python tools/verify_package.py
```

A successful run verifies byte-level checksums, UTF-8 decoding, math delimiter structure, mechanically regenerated math inventory, and mechanically regenerated normalization diff.

It does **not** prove the truth of the paper's theoretical claims or the correctness of every mathematical statement.
