# wdc-runtime

Local reference implementation for **World-Domain Cognitive Runtime v0.1**.

Current scope: **Phase 0–11** — ledger/world/checkpoint/fork kernel, role/authority isolation, bounded Governor state, dependence-aware evidence, computation-portfolio routing, an explicit sandbox Commit Gate, versioned TCD evidence assimilation / Historical Sedimentation, and an auditable World Ensemble Learning layer with source gates, holdout validation, rollback, Governor misses, and self-sealing warnings.

## Run tests

```bash
python -m pytest -q
```

## Run the Branching Grid demo

```bash
PYTHONPATH=src:. python examples/branching_grid.py /tmp/wdc-branching-grid
```

The demo creates one parent world, checkpoints it, forks two child worlds from the same exact prefix, applies divergent actions, persists fork events, and prints divergent terminal states.


## Run the Governed Evidence Grid demo

```bash
PYTHONPATH=src:. python examples/governed_evidence_grid.py /tmp/wdc-governed-evidence-grid
```

The demo adds sibling branch blindness, bounded Governor allocation, dependence-aware support/counter evidence, counterexample escalation, and redundant-branch tombstoning on top of the exact fork kernel.

## Run the Tri-Temporal Commit Grid demo

```bash
PYTHONPATH=src:. python examples/tri_temporal_commit_grid.py /tmp/wdc-tri-temporal-grid
```

This demo closes the first controlled TCD/WDC loop: governed branching evidence produces an independence deficit and a `CROSS_BACKEND` computation proposal; the counterevidence revises Future/Present/Past-relevance at the same parent time; an approved sandbox-only commit executes; only that executed sandbox outcome is sedimented into the next parent historical state.


## Run the World Ensemble Learning demo

```bash
PYTHONPATH=src:. python -m examples.world_ensemble_learning /tmp/wdc-world-learning
```

This demo adds Phase 9 learning on top of the tri-temporal loop: world-relative evidence can update Generator/FutureSpace versions, WORLD-only evidence is denied reality-facing promotion, a registered external calibration anchor allows a WorldModel candidate into validation, a deliberate holdout regression rolls it back, a GovernanceMiss calibrates the Governor meta-policy, and deteriorating external quality triggers self-sealing warnings. Learning itself does not advance parent historical time.

## Hard invariants already implemented

- `WorldSpec != WorldRun`
- three clock fields are explicit in the event envelope
- exact checkpoints preserve state, local time, and RNG state
- each fork creates a new world ID
- fork provenance records parent run, checkpoint, delta, and seed policy
- lineage cycles are rejected
- sibling post-fork access is denied without an explicit channel
- fork authority profiles cannot silently escalate external permissions
- mutable Governor lifecycle does not mutate immutable `WorldSpec`
- active Governor allocation cannot exceed the global budget
- `INVALID` evidence is not counterevidence
- aggregates preserve packet inputs and expose evidence-family dependence
- v0.1 does not fabricate a universal effective evidence count
- event payloads are persisted as snapshots
- computation actions are proposals, not execution authority
- Commit Gate verifies referenced evidence aggregates exist
- sandbox proxy requires an approved exact action payload
- TCD world-evidence assimilation preserves parent-real past facts and parent time
- sandbox Historical Sedimentation requires an approved commit + executed sandbox action
- `EXTERNAL_REAL` sedimentation requires a verified `PARENT_REAL_OBSERVATION` external ingest
- WORLD/SYNTHETIC/DERIVED evidence cannot self-promote to `REALITY_FACING` learning
- `REAL`/`EXTERNAL` reality-facing learning requires a registered anchor backed by a `VERIFIED` external ingest
- learning candidates activate only after holdout validation and can rollback
- learning-health warnings are diagnostic and do not mutate evidence/history automatically
- blobs are content-addressed and integrity-checked

See `docs/specs/` for the implementation contracts and `docs/superpowers/plans/` for the executed Phase 0–2, Phase 3–5, Phase 6–8, Phase 9, Phase 10, and Phase 11 plans.

## Phase 10 CLI

Phase 10 exposes the Phase 0–9 kernel through one JSON-first local command surface.

Initialize a workspace:

```bash
wdc --root /tmp/wdc-runtime init
wdc --root /tmp/wdc-runtime status
```

Complex payloads may be inline JSON or `@file.json`:

```bash
wdc --root /tmp/wdc-runtime tcd init --json @tcd-init.json
wdc --root /tmp/wdc-runtime world create --json @world.json
wdc --root /tmp/wdc-runtime evidence claim-create --json @claim.json
wdc --root /tmp/wdc-runtime portfolio route --json @deficit.json
wdc --root /tmp/wdc-runtime commit assess --json @commit.json
wdc --root /tmp/wdc-runtime learning propose --json @learning-update.json
```

Reference demos are available through the installed runtime surface:

```bash
wdc --root /tmp/wdc-demo demo branching-grid
wdc --root /tmp/wdc-demo demo governed-evidence
wdc --root /tmp/wdc-demo demo tri-temporal
wdc --root /tmp/wdc-demo demo learning
```

All successful CLI commands emit JSON to stdout. Expected domain/runtime failures emit a JSON error object to stderr with exit code `2`. The CLI delegates to the existing kernel services; it does not define alternate evidence, authority, TCD, or learning semantics.

## Phase 11 External Evidence / Adapter Layer

Phase 11 adds the first controlled non-WDC evidence boundary. External artifacts are read by adapters, stored as content-addressed blobs, registered with immutable source provenance, and only then may be converted into ordinary `EvidencePacket` objects.

Reference commands:

```bash
wdc --root /tmp/wdc-runtime external adapters
wdc --root /tmp/wdc-runtime external ingest --json @external-ingest.json
wdc --root /tmp/wdc-runtime external show <ingest_id>
wdc --root /tmp/wdc-runtime external evidence-add <ingest_id> --json @evidence.json
wdc --root /tmp/wdc-runtime demo external-evidence
```

The v0.1 reference adapter is `local-json`; it supports canonical inline JSON and local JSON files and performs no network access. A manual `learning source-anchor` record is no longer sufficient to unlock `REALITY_FACING` learning: the provenance must also resolve to a `VERIFIED` external ingest.

`EXTERNAL_REAL` Historical Sedimentation is now available only for verified ingests whose observation scope is `PARENT_REAL_OBSERVATION`. Ordinary external datasets remain evidence and cannot silently become parent-real historical facts.
