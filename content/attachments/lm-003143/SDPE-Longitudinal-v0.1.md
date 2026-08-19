# SDPE Observer-Network Longitudinal Experiment v0.1

This package overlays the existing SDPE Runtime with a zero-authority observer-network experiment ledger.

## Quick run

```bash
python tools/onx_observatory.py \
  --proof-ledger baseline_structural_run/proof_ledger.jsonl \
  --observer-ledger baseline_structural_run/observer_ledger.jsonl \
  --json-out baseline_structural_run/observatory_snapshot.json \
  --csv-out baseline_structural_run/timeline.csv

python tools/validate_onx_package.py .
```

## Authority boundary

- `reference_runtime/sdpe_runtime.py` reconstructs authoritative proof state.
- `baseline_structural_run/observer_ledger.jsonl` is observational only.
- Hidden oracle access is forbidden during runtime.

## Next real experiment

Replace synthetic-control role holders with real model families, keep the SDPE proof commit gate unchanged, and use crossed role/model assignments. Do not compare model families if each model is permanently bound to a different harness or role.
