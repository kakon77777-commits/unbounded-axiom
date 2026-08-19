# WDC Runtime Phase 9 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Add the minimal auditable World Ensemble Learning layer on top of the verified Phase 0–8 runtime.

**Architecture:** A new `wdc.learning` module owns generic versioned component states, learning events, source/scope gating, holdout validation, rollback, Governor misses, and learning-health warnings. Existing Evidence/TCD/Governor semantics remain unchanged.

**Tech Stack:** Python 3.11+, stdlib dataclasses/enums/sqlite3/json, existing WDC SQLite layer, pytest 8+.

## Global Constraints

- Use `python -m pytest`, not bare `pytest`, because the project pytest config intentionally sets `pythonpath = ["src"]` and integration tests also import the repository-root `examples` package.
- No production code before a failing test.
- No neural fine-tuning in Phase 9.
- No uncontrolled external action or EXTERNAL_REAL ingestion.
- `REALITY_FACING` learning requires at least one `REAL` or `EXTERNAL` evidence packet.
- Every update is versioned and rollback-capable.

---

### Task 1: Versioned learning events and source-scope gate

**Files:**
- Create: `src/wdc/learning.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_learning_events.py`

**Interfaces:**
- Consumes: `EvidenceEngine.get_packet(evidence_id)` and `EvidencePacket.source_class/synthetic_depth`.
- Produces: `LearningCoordinator.register_component()`, `propose_update()`, `get_active_version()`, `get_event()`.

- [x] Step 1: write failing tests for source preservation, candidate version creation, and world-only reality-facing rejection.
- [x] Step 2: run `python -m pytest tests/test_learning_events.py -q` and verify feature-missing failure.
- [x] Step 3: add SQLite tables and minimal `wdc.learning` implementation.
- [x] Step 4: run targeted test and full suite.
- [x] Step 5: commit `feat: add versioned learning events`.

### Task 2: Holdout validation and rollback

**Files:**
- Modify: `src/wdc/learning.py`
- Test: `tests/test_learning_validation.py`

**Interfaces:**
- Consumes: candidate learning event from Task 1.
- Produces: `validate_update()` and `rollback()`.

- [x] Step 1: write failing tests showing passing holdout activates candidate, regression leaves prior active, and manual rollback restores prior active version.
- [x] Step 2: run targeted tests and verify RED.
- [x] Step 3: implement minimal validation/activation/rollback.
- [x] Step 4: run targeted and full suite.
- [x] Step 5: commit `feat: add learning validation and rollback`.

### Task 3: Governance miss and Governor calibration version

**Files:**
- Modify: `src/wdc/learning.py`
- Test: `tests/test_governor_learning.py`

**Interfaces:**
- Consumes: generic versioned `GOVERNOR` component.
- Produces: `record_governance_miss()` and `propose_governor_calibration()`.

- [x] Step 1: write failing test where an audit-detected miss becomes a provenance-bearing learning event with a new candidate Governor version.
- [x] Step 2: run targeted test and verify RED.
- [x] Step 3: implement miss persistence and calibration proposal.
- [x] Step 4: validate candidate and run full suite.
- [x] Step 5: commit `feat: add governor meta-calibration`.

### Task 4: Learning health and self-sealing warning

**Files:**
- Modify: `src/wdc/learning.py`
- Test: `tests/test_learning_health.py`

**Interfaces:**
- Produces: `record_health_snapshot()` and `assess_self_sealing()`.

- [x] Step 1: write failing tests for rising self-agreement + falling diversity/accuracy and low-anchor warning.
- [x] Step 2: run targeted tests and verify RED.
- [x] Step 3: implement persisted snapshots/warnings with reference-policy version.
- [x] Step 4: run targeted/full suite.
- [x] Step 5: commit `feat: add learning self-sealing monitor`.

### Task 5: Phase 9 integration demo

**Files:**
- Create: `examples/world_ensemble_learning.py`
- Create: `tests/test_phase9_integration.py`
- Modify: `README.md`
- Create: `PHASE9_IMPLEMENTATION_REPORT.md`

**Interfaces:**
- Consumes: Phase 0–8 demo and Tasks 1–4.
- Produces: one end-to-end learning demo result dictionary.

- [x] Step 1: write failing integration test.
- [x] Step 2: run targeted test and verify RED.
- [x] Step 3: implement demo showing ensemble-relative update, reality-facing gate, rollback, Governor miss calibration, and self-sealing warning.
- [x] Step 4: run `python -m pytest -q`, `python -m compileall -q src tests examples`, and `PYTHONPATH=src:. python -m examples.world_ensemble_learning /tmp/wdc-phase9-demo`.
- [x] Step 5: write report/README and commit.

### Task 6: Completion gate

- [x] `git diff --check` passes.
- [x] `python -m pytest -q` passes.
- [x] `python -m compileall -q src tests examples` passes.
- [x] Phase 9 demo passes.
- [x] package only Git-tracked files.
- [x] extract package into a fresh directory.
- [x] fresh archive `python -m pytest -q` passes.
- [x] fresh archive Phase 9 demo passes.
- [x] working tree is clean.
