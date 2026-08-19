# WDC Runtime Phase 9 Implementation Report

**Date:** 2026-08-17  
**Branch:** `feature/phase9`  
**Base:** Phase 0–8 commit `0295f6b36350e0c5b66a3291614134d5dd035569`

## Scope completed

Phase 9 adds the first auditable World Ensemble Learning layer on top of the verified Phase 0–8 TCD/WDC runtime.

### Versioned learning components

Implemented `src/wdc/learning.py` with four target component types:

```text
GENERATOR
WORLD_MODEL
GOVERNOR
FUTURE_SPACE
```

Each target stores immutable JSON-serializable versions. A learning proposal creates an inactive candidate version first. The active version changes only after holdout validation passes.

### Learning event provenance

Every proposed update records:

```text
source evidence IDs
source classes
synthetic depth
learning scope
prior version
candidate version
update type
validation result
rollback reference
```

Learning scopes:

```text
WORLD_LOCAL
ENSEMBLE_RELATIVE
REALITY_FACING
```

### Reality-facing source gate

WORLD/SYNTHETIC/DERIVED evidence cannot self-promote into a reality-facing update.

A reality-facing update requires at least one `REAL` or `EXTERNAL` evidence packet whose `provenance_ref` is backed by a registered `source_registry` external anchor.

This extra registry check was added during self-review so a caller cannot gain reality-facing authority merely by writing `source_class=EXTERNAL` into an arbitrary packet.

The Phase 9 integration demo uses an explicitly registered **external calibration fixture**. It is a test anchor, not a claim of actual external empirical validation.

### Holdout validation and rollback

Implemented:

```text
validate_update()
rollback()
```

Behavior:

- passing holdout -> candidate becomes active;
- holdout regression -> candidate remains inactive and prior version stays active;
- manual rollback -> prior version is restored;
- an old event cannot rollback over a later active version.

### Governor meta-calibration

Implemented `GovernanceMiss` persistence and a reference calibration path:

```text
GovernanceMiss
-> LearningEvent
-> candidate Governor version
-> holdout validation
-> active Governor version
```

This does not mutate the existing runtime `WorldGovernor` scheduler in place. It versions a logical Governor meta-policy state for later runtime integration.

### Learning health / self-sealing monitor

Persisted health snapshots track:

```text
self_agreement
family_diversity
external_accuracy
unknown_world_mass
reality_anchor_ratio
counterexample_recall
```

Reference warnings:

```text
SELF_SEALING_TREND
LOW_REALITY_ANCHOR
```

The warnings are diagnostics only. They do not automatically rewrite evidence, TCD state, or Governor policy.

## Phase 9 integration demo

New demo:

```text
examples/world_ensemble_learning.py
```

It extends the Phase 0–8 demo with:

```text
world evidence
-> Generator ensemble-relative update APPLIED
-> FutureSpace ensemble-relative update APPLIED
-> WORLD-only WorldModel reality-facing update DENIED
-> registered EXTERNAL anchor + WORLD evidence
-> WorldModel candidate admitted to validation
-> external holdout regression
-> WorldModel candidate ROLLED_BACK
-> GovernanceMiss
-> Governor calibration APPLIED
-> learning-health deterioration
-> SELF_SEALING_TREND + LOW_REALITY_ANCHOR warnings
```

Learning does not sediment a new parent-real event, so parent historical time remains at the Phase 8 value.

## Database additions

Added:

```text
source_registry
learning_component_versions
learning_events
governance_misses
learning_health_snapshots
learning_warnings
```

## New tests

Added:

```text
tests/test_learning_events.py
tests/test_learning_validation.py
tests/test_governor_learning.py
tests/test_learning_health.py
tests/test_phase9_integration.py
```

Coverage includes:

- source class / synthetic depth preservation;
- world-only reality-facing rejection;
- spoofed unregistered EXTERNAL rejection;
- registered external-anchor acceptance;
- candidate versions remain inactive before validation;
- holdout activation;
- holdout regression rollback;
- manual rollback;
- GovernanceMiss calibration;
- self-sealing warnings;
- complete Phase 0–9 integration.

## Permanent invariants added

```text
World-generated evidence != reality-facing training truth
EXTERNAL label != registered external anchor
Learning proposal != active component version
Holdout regression -> prior version remains active
Every consequential update -> LearningEvent
Learning != Historical Sedimentation
Self-sealing warning != automatic evidence rewrite
```

## Deferred after Phase 9

Not implemented here:

- neural fine-tuning;
- real external evidence adapter;
- automatic world-generator training;
- learned WorldModel parameter training;
- live wiring from learned Governor component state into `WorldGovernor` scheduling;
- Phase 10 CLI/package commands;
- Ray/Kubernetes distributed runtime;
- gVisor/Firecracker adapters.
