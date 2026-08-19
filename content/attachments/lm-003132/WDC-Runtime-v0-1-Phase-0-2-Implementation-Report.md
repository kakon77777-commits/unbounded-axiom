# WDC Runtime v0.1 — Phase 0–2 Implementation Report

Date: 2026-08-17
Branch: `feature/phase0-2`

## Implemented

- typed opaque IDs
- content-addressed filesystem blob store with SHA-256 integrity verification
- SQLite event ledger with three explicit clocks
- immutable `WorldSpec` and separate repeatable `WorldRun`
- deterministic `PythonStateWorld` reference backend
- role-relative observation callback
- exact checkpoint serialization restoring state, local time, and RNG state
- blob-backed checkpoint repository
- fork lineage records with parent run/checkpoint/delta/seed provenance
- ancestry/descendant queries and lineage-cycle rejection
- executable Branching Grid integration demo

## Hard invariants covered by tests

- `WorldSpec != WorldRun`
- unique world/run IDs
- event payload snapshot persistence
- exact checkpoint round-trip
- fork creates new world identity
- child records parent/checkpoint provenance
- lineage is acyclic
- two children can restore the same prefix and diverge afterward

## Verification command

```bash
python -m pytest -q
python -m compileall -q src examples
PYTHONPATH=src:. python examples/branching_grid.py /tmp/wdc-final-demo
```

At implementation completion the test suite contains 17 tests.

## Deferred to the next phase

- RoleCard / branch-blind information-flow enforcement
- Governor resource ledger and lifecycle policy
- EvidencePacket / dependence-aware aggregation
- Commit Gate / external proxy
- TCDStateManager integration
- learning / rollback
- distributed scheduling and hardened sandboxes
