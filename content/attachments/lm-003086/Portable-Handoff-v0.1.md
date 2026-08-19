# GCORF-01 v0.1 Portable Handoff

This archive contains the second canonical-core paper of the GCORF series in UTF-8 Markdown plus machine-readable schemas and integrity metadata.

Primary artifact: `paper.md`.

This package is **SSSP-ready**, but it does not claim that an SSSP MCP canonical revision has already been created. Import/commit status must be established by the actual SSSP MCP runtime.

## Contents

- `paper.md` — canonical-intent scholarly source for GCORF-01 v0.1
- `schemas/evidence_unit.schema.json` — machine-readable minimal evidence unit schema
- `schemas/candidate_operator.schema.json` — machine-readable candidate operator schema
- `AI_HANDOFF.md` — downstream AI editing rules
- `manifest.json` — package metadata
- `validation.json` — portable-artifact validation scope
- `CHECKSUMS.sha256` — SHA-256 manifest
- `provenance/source_map.md` — internal theory/source lineage
- `provenance/math_inventory.json` — mechanically generated math inventory
- `tools/verify_package.py` — independent package verifier

## Important

Do not rebuild formulas from rendered chat. Preserve `$...$` and `$$...$$` exactly unless creating a declared new revision.
