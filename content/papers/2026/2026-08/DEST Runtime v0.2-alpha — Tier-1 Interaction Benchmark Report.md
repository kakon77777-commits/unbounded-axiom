# DEST Runtime v0.2-alpha — Tier-1 Interaction Benchmark Report

**Date:** 2026-08-13  
**Benchmark:** DEST Tier-1 Interaction Benchmark v0.1  
**Cases:** 60  
**Oracle separation:** policy reads `observation`; oracle reads `hidden_state`

## Results

- DEST interaction policy: **58/60 = 96.7%**
- Flat interaction baseline: **16/60 = 26.7%**
- Oracle semantic-mutation sensitivity: **100.0%**
- Oracle neutral-mutation specificity: **100.0%**
- Regression tests: **7/7 PASS**

## Category scores

- `boundary_evolution` — DEST 100.0%; baseline 30.0%
- `cert_version` — DEST 100.0%; baseline 30.0%
- `core_view` — DEST 100.0%; baseline 20.0%
- `coverage_view` — DEST 90.0%; baseline 30.0%
- `gap_representation` — DEST 90.0%; baseline 20.0%
- `glue_branch` — DEST 100.0%; baseline 30.0%

## Known Runtime misses retained as regression targets

- `IX-CV-10` (coverage_view): expected `RETRIEVE_MORE`, predicted `USE_OK`.
- `IX-GR-09` (gap_representation): expected `REJECT_ESCAPE`, predicted `DEFER_ESCAPE`.

## Why the misses were not patched away

The benchmark is intentionally allowed to expose partial-observability failures.  
The two current misses involve hidden state not fully recoverable from the visible observation:

1. retrieval appears adequate by observable recall, while the hidden state still contains a missing relevant item;
2. UNKNOWN translation certificates do not reveal whether the latent escape is actually invalid or merely unverified.

Tuning thresholds directly to these two cases would make the reference policy more benchmark-specific without adding new evidence. They are therefore retained.

## Oracle mutation discipline

Each case has:

- one **semantic mutation**: one or more hidden-state changes that must alter the oracle answer;
- one **neutral mutation**: a hidden bookkeeping/noise change that must not alter the oracle answer.

The mutation harness now obtains 100% sensitivity and 100% specificity on the bundled suite.

This does not prove the oracle is globally correct. It only proves the selected mutants exercise its decision surface as intended.

## Interpretation

This benchmark is stronger than the v0.1 conformance suite because expected answers are not stored in the policy-visible observation and because cross-module interactions are tested.

It remains a synthetic benchmark authored alongside the Runtime. Therefore the result **must not** be presented as evidence that DEST is superior on open-world research.

The next defensible tier is an independently authored End-to-End / hidden-oracle pack, ideally with:
- delayed evidence,
- real artifacts,
- tool failures,
- independently written mutations,
- frozen hidden cases,
- budget-matched stateful-RAG baseline.
