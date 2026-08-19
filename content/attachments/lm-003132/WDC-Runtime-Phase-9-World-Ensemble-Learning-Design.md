# WDC Runtime Phase 9 — World Ensemble Learning Design

**Status:** approved continuation of the existing MVP Phase 9 specification.

## Goal

Add a minimal, auditable World Ensemble Learning layer without neural fine-tuning. The layer must preserve evidence source provenance, separate learning scope, version all target components, validate updates on holdout metrics, rollback regressions, record Governor misses, and detect a reference self-sealing signature.

## Non-goals

Phase 9 does not implement gradient training, a learned world model backend, external-real ingestion, automatic ontology generation, or distributed learning.

## Components

### 1. LearningCoordinator

New module `src/wdc/learning.py` owns learning-event orchestration and four target component types:

- `GENERATOR`
- `WORLD_MODEL`
- `GOVERNOR`
- `FUTURE_SPACE`

Each component has versioned JSON-serializable state stored in SQLite. Updates create candidate versions first; activation only occurs after validation.

### 2. Source and Scope Gate

Source provenance comes from existing `EvidencePacket.source_class` and `synthetic_depth`.

Learning scopes:

- `WORLD_LOCAL`
- `ENSEMBLE_RELATIVE`
- `REALITY_FACING`

A `REALITY_FACING` update is rejected if every source packet is `WORLD`, `SYNTHETIC`, `DERIVED`, or `UNKNOWN`. At least one `REAL` or `EXTERNAL` evidence packet is required. Generated evidence may participate alongside an anchor, but cannot self-promote alone.

### 3. Holdout Validation and Rollback

A proposed update stores:

- prior version;
- candidate version;
- source evidence IDs/classes;
- synthetic depth;
- update type;
- learning scope.

Validation compares an explicit holdout metric before/after. If the candidate fails the declared threshold/direction, the prior version remains active and the event becomes `ROLLED_BACK`. If it passes, the candidate becomes active and the event becomes `APPLIED`.

Manual rollback is supported for an already-applied event and reactivates the prior version.

### 4. Governor Miss / Calibration

A `GovernanceMiss` records a computation/world that was undervalued or prematurely pruned. The first reference calibration path converts a miss into a new Governor component version. The state is deliberately heuristic JSON, not a trained policy.

### 5. Learning Health Monitor

Persist snapshots of:

- self agreement;
- world-family diversity;
- external accuracy;
- unknown-world mass;
- reality-anchor ratio;
- counterexample recall.

Reference self-sealing warning condition:

- self agreement rises;
- family diversity falls;
- external accuracy falls.

A second warning condition is high self agreement with very low reality-anchor ratio. These are diagnostic heuristics, not universal scientific thresholds.

## Persistence

Add tables:

- `learning_component_versions`
- `learning_events`
- `governance_misses`
- `learning_health_snapshots`
- `learning_warnings`

All updates are append/version oriented. No active version is silently overwritten.

## Integration Demo

`examples/world_ensemble_learning.py` extends the Phase 0–8 tri-temporal demo:

1. reuse existing world evidence;
2. register Generator, WorldModel, Governor, FutureSpace component v0 states;
3. demonstrate that world-only evidence can produce an ensemble-relative Generator update;
4. demonstrate that the same world-only evidence is rejected for a reality-facing WorldModel update;
5. create a real/external anchored packet and allow a reality-facing candidate update;
6. force a holdout regression and verify rollback;
7. record a GovernanceMiss and apply a validated Governor calibration version;
8. create two health snapshots that trigger a self-sealing warning.

## Hard Invariants

- world-generated evidence never silently becomes reality-facing training truth;
- every consequential update has a `LearningEvent`;
- active versions change only after validation;
- rollback restores the prior version;
- source classes and synthetic depth are preserved in the learning event;
- warnings diagnose self-sealing risk but do not rewrite evidence or TCD history.
