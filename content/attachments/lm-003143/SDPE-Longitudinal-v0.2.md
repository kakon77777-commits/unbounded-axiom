# SDPE × Observer-Network Longitudinal Experiment v0.2

**Status:** executable REAL RUN 001 factorial package.
**Purpose:** test whether persistent failure memory and observer-role separation alter rollback-to-repair dynamics in an SDPE proof enclosure runtime.

## Frozen first-batch design

$$
\boxed{
\text{Memory}\in\{M^+,M^-\}
\times
\text{Architecture}\in\{ON,SA\}
}
$$

Where:
- `ON` = role-separated Observer Network;
- `SA` = Single Agent proposal/self-verification control;
- `M+` = rejected-route / invalidation memory preserved;
- `M-` = failure memory ablated after canonical invalidation.

The deterministic SDPE runtime remains the only proof authority. The observer sidecar can never commit proof state.

## Primary endpoints

1. $PER_t$ — proof enclosure ratio;
2. $EER_t$ — epistemic enclosure ratio;
3. $L_{repair}$ — rollback-to-reclosure lag;
4. $IRR$ — invalid-route reintroduction rate;
5. $IPR$ — invalidated-pass rate;
6. $\sigma_t$ — verification share from canonical DVI telemetry.

`FCR` (false certification rate) is **post-freeze only** and requires a hidden-oracle label. Before oracle release, the package reports `IPR`, not `FCR`.

## Contents

- `REAL_RUN_001_FACTORIAL_PROTOCOL_v0.2.md` — frozen experiment protocol;
- `ONX_Event_Schema_v0.2.json` — sidecar event schema;
- `ONX_Run_Schema_v0.2.json` — arm/run manifest schema;
- `tools/onx_observatory_v02.py` — arm-level metrics;
- `tools/onx_factorial_scorer.py` — 2x2 comparison / interaction metrics;
- `preflight_2x2/` — deterministic synthetic preflight proving the instrumentation works;
- `real_run_001_2x2/` — clean templates for real model traces;
- `operator_only/` — hidden-oracle policy files; do not mount into Agent workspaces.

## Critical interpretation rule

The preflight is **not evidence** that memory or observer networks improve real AI research. It is engineered only to exercise all measurement pathways, including memory reset, route reintroduction, invalidation, repair, and reclosure.

## Identifiability correction

Phase A uses homogeneous role-separated Agent instances of each model family versus the same-family single-agent control. Heterogeneous four-model observer networks are deferred to Phase B, preventing architecture effects from being confounded with model diversity. See `real_run_001_2x2/REAL_RUN_001_RUN_MATRIX_v0.2.md`.
