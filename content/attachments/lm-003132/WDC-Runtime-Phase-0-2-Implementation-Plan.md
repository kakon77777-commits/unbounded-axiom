# WDC Runtime Phase 0–2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build the first executable local WDC kernel covering typed IDs, SQLite/blob/event ledger, immutable WorldSpec/WorldRun separation, PythonStateWorld, exact checkpoints, and an acyclic fork lineage graph.

**Architecture:** Use a small Python `src/` package with stdlib-only production dependencies. Persist metadata/events in SQLite and large bytes in a content-addressed filesystem blob store. Implement a deterministic JSON-state reference world backend first so checkpoint/fork semantics are exact and auditable.

**Tech Stack:** Python 3.11+, stdlib (`dataclasses`, `enum`, `sqlite3`, `hashlib`, `json`, `pathlib`, `uuid`), pytest for tests.

## Global Constraints

- `WorldSpec != WorldRun` is a hard invariant.
- Clock fields remain distinct: `parent_time`, `deliberation_index`, `world_local_time`.
- World-local events cannot become external-real facts.
- Every fork creates a new world ID and records parent/checkpoint/delta/seed policy.
- World ancestry must remain acyclic.
- Production code is stdlib-only for Phase 0–2.
- Tests are written and observed failing before production implementation.

---

### Task 1: Package, typed IDs, blob store, and event ledger

**Files:**
- Create: `pyproject.toml`
- Create: `src/wdc/__init__.py`
- Create: `src/wdc/ids.py`
- Create: `src/wdc/storage.py`
- Create: `src/wdc/events.py`
- Create: `tests/test_ids_storage_events.py`

**Interfaces:**
- Produces: `new_id(prefix: str) -> str`
- Produces: `BlobStore.put(data: bytes, mime_type: str = "application/octet-stream") -> BlobRef`
- Produces: `BlobStore.get(ref: BlobRef) -> bytes`
- Produces: `EventEnvelope` and `EventLedger.append/get/query`

- [x] Write failing tests for typed IDs, blob hash round-trip, three clocks, immutable event payload persistence, and event query.
- [x] Run tests and confirm failures are due to missing package/interfaces.
- [x] Implement minimal package, ID helper, blob store, event dataclass, and SQLite event ledger.
- [x] Re-run tests until green.
- [x] Commit `feat: add WDC ledger kernel`.

### Task 2: SQLite schema and immutable WorldSpec/WorldRun registry

**Files:**
- Create: `src/wdc/db.py`
- Create: `src/wdc/models.py`
- Create: `src/wdc/worlds.py`
- Create: `tests/test_world_registry.py`

**Interfaces:**
- Produces: `WDCDB(path)` with migration/bootstrap.
- Produces: `WorldSpec`, `WorldRun`, `WorldStatus`, `DomainType`.
- Produces: `WorldRegistry.create_spec/get_spec/create_run/get_run`.

- [x] Write failing tests proving world IDs are unique, WorldSpec is immutable after persistence, and multiple runs may reference one spec.
- [x] Run and observe expected failures.
- [x] Implement minimal schema/models/registry.
- [x] Re-run all tests green.
- [x] Commit `feat: add world registry and run separation`.

### Task 3: WorldBackend protocol and deterministic PythonStateWorld

**Files:**
- Create: `src/wdc/backend.py`
- Create: `src/wdc/python_world.py`
- Create: `tests/test_python_world.py`

**Interfaces:**
- Produces: `BackendCapabilities`.
- Produces: `WorldBackend` protocol.
- Produces: `PythonStateWorld(initial_state, transition, seed)` with `initialize`, `step`, `observe`, `checkpoint_bytes`, `restore_bytes`, `terminate`.

- [x] Write failing tests for local-time advancement, deterministic transition, role-relative observation hook, and deterministic seed replay.
- [x] Run and observe expected failures.
- [x] Implement minimal backend/protocol/reference world.
- [x] Run all tests green.
- [x] Commit `feat: add deterministic PythonStateWorld backend`.

### Task 4: Exact checkpoints and blob-backed checkpoint repository

**Files:**
- Create: `src/wdc/checkpoints.py`
- Create: `tests/test_checkpoints.py`

**Interfaces:**
- Produces: `CheckpointRecord`.
- Produces: `CheckpointRepository.create_exact(world_id, run_id, world_local_time, checkpoint_bytes, ...)`.
- Produces: `CheckpointRepository.load(checkpoint_id) -> tuple[CheckpointRecord, bytes]`.

- [x] Write failing checkpoint round-trip and digest tests.
- [x] Run and confirm expected failures.
- [x] Implement minimal checkpoint repository using BlobStore + SQLite metadata.
- [x] Re-run all tests green.
- [x] Commit `feat: add exact checkpoint repository`.

### Task 5: Fork lineage DAG and shared-prefix fork operation

**Files:**
- Create: `src/wdc/branches.py`
- Create: `tests/test_branches.py`

**Interfaces:**
- Produces: `ForkRecord`.
- Produces: `BranchManager.fork(parent_world_id, parent_run_id, checkpoint_id, divergence_type, divergence_delta, seed_policy, child_spec_fields) -> WorldSpec`.
- Produces: `BranchManager.ancestors(world_id)`, `descendants(world_id)`, `assert_acyclic()`.

- [x] Write failing tests for new child identity, parent/checkpoint provenance, exact shared-prefix checkpoint, and cycle rejection.
- [x] Run and confirm expected failures.
- [x] Implement minimal fork/DAG logic.
- [x] Re-run all tests green.
- [x] Commit `feat: add exact fork lineage DAG`.

### Task 6: Branching Grid example and Phase 0–2 integration test

**Files:**
- Create: `examples/branching_grid.py`
- Create: `tests/test_branching_grid_integration.py`
- Create: `README.md`

**Interfaces:**
- Demonstrates one parent run, checkpoint, two children, shared prefix, divergent post-fork states, and persisted lineage/events.

- [x] Write failing integration test first.
- [x] Run and confirm the integration path is incomplete.
- [x] Implement the minimal example wiring only.
- [x] Run the complete test suite green.
- [x] Add README commands for running tests and demo.
- [x] Commit `feat: complete WDC phase 0-2 branching grid demo`.

## Verification

Run:

```bash
python -m pytest -q
python examples/branching_grid.py
```

Expected: all tests pass; demo prints parent/child IDs, shared checkpoint ID, and divergent child terminal states.
