# WDC Runtime Phase 6–8 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Extend the verified WDC Phase 0–5 runtime with rule-based computation portfolio routing, an explicit commit/authority boundary, and versioned TCD evidence assimilation plus real-transition sedimentation.

**Architecture:** Add three focused modules—`portfolio.py`, `commit.py`, and `tcd.py`—without changing Phase 0–5 semantics. Persist their consequential records in SQLite and use the existing event/provenance patterns. A final integration demo must close the controlled sandbox loop while preserving the History Firewall.

**Tech Stack:** Python 3.11+, stdlib dataclasses/enums/sqlite3/json, existing WDC SQLite layer, pytest 8+.

## Global Constraints

- Keep `WorldSpec` immutable and separate from `WorldRun`.
- Preserve lineage DAG semantics and Phase 0–5 tests.
- No neural learner, Ray, Kubernetes, gVisor, Firecracker, or uncontrolled real API execution.
- `World-Local Event != Parent-Real Historical Fact`.
- `Worth Computing != Worth Believing != Worth Deploying`.
- Use TDD: failing test first, verify RED, minimal GREEN, then full suite.
- Every consequential commit/TCD transition is persisted and versioned.

---

### Task 1: Computation Portfolio Kernel

**Files:**
- Create: `src/wdc/portfolio.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_portfolio.py`

**Interfaces:**
- Consumes: `EvidenceAggregate`, world-family metadata, existing `new_id()` helper.
- Produces: `ComputationOperation`, `EpistemicDeficit`, `ComputationAction`, `DeficitRouter.route(deficit, *, target_id, purpose) -> tuple[ComputationAction, ...]`, persistence helpers.

- [x] **Step 1: Write failing deficit-routing tests**

```python
def test_independence_deficit_routes_cross_backend(tmp_path):
    router = DeficitRouter(...)
    actions = router.route(EpistemicDeficit(independence=0.9), target_id="claim_1", purpose="EVIDENCE")
    assert actions[0].operation is ComputationOperation.CROSS_BACKEND


def test_transport_deficit_routes_calibrate(tmp_path):
    actions = router.route(EpistemicDeficit(transport=0.9), target_id="claim_1", purpose="TRANSPORT")
    assert actions[0].operation is ComputationOperation.CALIBRATE
```

- [x] **Step 2: Run targeted tests and verify RED**

Run: `python -m pytest tests/test_portfolio.py -q`
Expected: import/attribute failure because `wdc.portfolio` does not exist.

- [x] **Step 3: Implement minimal portfolio types and deterministic router**

Routing precedence for v0.1:

```text
transport >= 0.7      -> CALIBRATE
counterexample >= 0.7 -> FORK_COUNTER
independence >= 0.7   -> CROSS_BACKEND
run_uncertainty >= .7 -> REPLICATE
tail >= 0.7           -> STRESS_TAIL
unknown_world >= 0.7  -> EXPLORE_UNKNOWN
fidelity >= 0.7       -> REFINE_FIDELITY
otherwise             -> RUN_MORE
```

Persist proposed actions in `computation_actions` with serialized deficit and expected-value vectors.

- [x] **Step 4: Add redundancy-aware proposal test**

```python
def test_same_family_saturation_prefers_cross_backend(tmp_path):
    deficit = EpistemicDeficit(independence=0.85, run_uncertainty=0.1)
    action = router.route(deficit, target_id=claim.claim_id, purpose="EVIDENCE")[0]
    assert action.operation is ComputationOperation.CROSS_BACKEND
```

- [x] **Step 5: Run targeted and full suites**

Run: `python -m pytest tests/test_portfolio.py -q && python -m pytest -q`
Expected: all pass.

- [x] **Step 6: Commit**

```bash
git add src/wdc/portfolio.py src/wdc/db.py tests/test_portfolio.py
git commit -m "feat: add computation portfolio kernel"
```

---

### Task 2: Reality Commit Gate and Controlled External Proxy

**Files:**
- Create: `src/wdc/commit.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_commit_gate.py`

**Interfaces:**
- Consumes: evidence aggregate IDs, transport/unknown/counterexample summary, requested authority permission.
- Produces: `CommitDecision`, `CommitProposal`, `CommitRecord`, `CommitGate.assess()`, `ExternalActionRequest`, `ExternalToolProxy.execute_sandbox()`.

- [x] **Step 1: Write failing authority and consensus-bypass tests**

```python
def test_commit_denied_without_required_authority(tmp_path):
    proposal = CommitProposal(... required_permission="sandbox.write")
    record = gate.assess(proposal, granted_permissions=frozenset())
    assert record.decision is CommitDecision.DENY


def test_consensus_does_not_bypass_commit_gate(tmp_path):
    proposal = CommitProposal(... evidence_aggregate_ids=(agg.aggregate_id,))
    with pytest.raises(CommitDenied):
        proxy.execute_sandbox(proposal.proposed_action, commit_id=None)
```

- [x] **Step 2: Run targeted tests and verify RED**

Run: `python -m pytest tests/test_commit_gate.py -q`
Expected: import failure for `wdc.commit`.

- [x] **Step 3: Implement commit records and gate**

Reference v0.1 decisions:

```text
APPROVE
DENY
DEFER
REQUEST_MORE_EVIDENCE
REQUEST_EXTERNAL_TEST
SAFE_FALLBACK
```

Rules:

```text
missing required authority -> DENY
no evidence aggregate for evidence-required action -> REQUEST_MORE_EVIDENCE
transport debt >= 0.7 for EMPIRICAL_OPEN-like proposal -> REQUEST_EXTERNAL_TEST
unresolved critical counterexample -> REQUEST_MORE_EVIDENCE
otherwise controlled sandbox proposal -> APPROVE
```

Persist every assessment in `commit_records`.

- [x] **Step 4: Implement proxy authorization test**

```python
def test_approved_commit_required_for_sandbox_action(tmp_path):
    record = gate.assess(proposal, granted_permissions={"sandbox.write"})
    result = proxy.execute_sandbox(proposal.proposed_action, commit_id=record.commit_id)
    assert result.commit_id == record.commit_id
```

`ExternalToolProxy` in v0.1 writes only to an in-memory/SQLite sandbox action ledger; it does not call uncontrolled external APIs.

- [x] **Step 5: Run targeted and full suites**

Run: `python -m pytest tests/test_commit_gate.py -q && python -m pytest -q`
Expected: all pass.

- [x] **Step 6: Commit**

```bash
git add src/wdc/commit.py src/wdc/db.py tests/test_commit_gate.py
git commit -m "feat: add reality commit gate"
```

---

### Task 3: TCD Versioning, Evidence Assimilation, and History Firewall

**Files:**
- Create: `src/wdc/tcd.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_tcd_integration.py`

**Interfaces:**
- Consumes: `EvidenceAggregate`, world evidence summary, approved commit/real outcome.
- Produces: `TCDStateVersion`, `FutureCandidate`, `TCDDelta`, `SedimentationRecord`, `TCDStateManager.assimilate_world_evidence()`, `TCDStateManager.sediment_real_transition()`.

- [x] **Step 1: Write failing History Firewall tests**

```python
def test_world_evidence_updates_relevance_not_past_facts(tmp_path):
    before = manager.current()
    after, delta = manager.assimilate_world_evidence(...)
    assert after.parent_time == before.parent_time
    assert after.past_facts == before.past_facts
    assert after.past_relevance != before.past_relevance


def test_sedimentation_advances_parent_time_once(tmp_path):
    next_state = manager.sediment_real_transition(...)
    assert next_state.parent_time == current.parent_time + 1
```

- [x] **Step 2: Run targeted tests and verify RED**

Run: `python -m pytest tests/test_tcd_integration.py -q`
Expected: import failure for `wdc.tcd`.

- [x] **Step 3: Implement versioned TCD records**

`TCDStateVersion` must contain separate serialized refs/data for:

```text
past_facts
past_relevance
present_action_values
future_candidates
unknown_world_mass
parent_time
version_id
```

`assimilate_world_evidence()` may modify all except `past_facts` and `parent_time`.

- [x] **Step 4: Implement sedimentation**

`sediment_real_transition()` requires an approved `commit_id` or an explicitly typed independent external observation, records action/outcome provenance, increments `parent_time` by one, and creates a `SedimentationRecord`.

- [x] **Step 5: Add explicit laundering rejection**

```python
def test_world_local_event_cannot_be_sedimented_as_real_fact(tmp_path):
    with pytest.raises(HistoryFirewallViolation):
        manager.sediment_world_local_fact(...)
```

- [x] **Step 6: Run targeted and full suites**

Run: `python -m pytest tests/test_tcd_integration.py -q && python -m pytest -q`
Expected: all pass.

- [x] **Step 7: Commit**

```bash
git add src/wdc/tcd.py src/wdc/db.py tests/test_tcd_integration.py
git commit -m "feat: integrate TCD assimilation and sedimentation"
```

---

### Task 4: Phase 6–8 Closed-Loop Demo

**Files:**
- Create: `examples/tri_temporal_commit_grid.py`
- Create: `tests/test_phase6_8_integration.py`
- Create: `PHASE6_8_IMPLEMENTATION_REPORT.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: Phase 0–5 Branching Grid helpers plus new Portfolio, Commit, and TCD modules.
- Produces: `run_demo(base_dir) -> dict[str, object]` proving the controlled loop.

- [x] **Step 1: Write failing integration test**

```python
def test_phase6_8_demo_closes_controlled_tcd_loop(tmp_path):
    result = run_demo(tmp_path)
    assert result["portfolio_operation"] == "CROSS_BACKEND"
    assert result["commit_decision"] == "APPROVE"
    assert result["sandbox_action_executed"] is True
    assert result["history_firewall_preserved"] is True
    assert result["parent_time_before"] == 0
    assert result["parent_time_after"] == 1
```

- [x] **Step 2: Run integration test and verify RED**

Run: `python -m pytest tests/test_phase6_8_integration.py -q`
Expected: missing demo module.

- [x] **Step 3: Implement demo**

Flow:

```text
create TCD state at t=0
use Phase 0–5 evidence with high independence deficit
route CROSS_BACKEND computation proposal
create controlled sandbox commit proposal
approve only with sandbox.write authority
execute sandbox proxy action
assimilate evidence without changing past facts
sediment sandbox action/outcome
produce TCD state at t=1
```

- [x] **Step 4: Run full verification**

Run:

```bash
python -m pytest -q
python -m compileall -q src examples
python -m examples.tri_temporal_commit_grid
```

Expected: all tests pass, compile succeeds, demo prints a result with `history_firewall_preserved=true`.

- [x] **Step 5: Write implementation report and README update**

Document exact test count, implemented APIs, invariants, and deferred Phase 9 work.

- [x] **Step 6: Commit**

```bash
git add examples tests PHASE6_8_IMPLEMENTATION_REPORT.md README.md
git commit -m "feat: close phase6-8 tri-temporal runtime loop"
```

---

## Completion Gate

- [x] `git diff --check`
- [x] no incomplete task checkbox lines remain in this plan
- [x] `python -m pytest -q`
- [x] `python -m compileall -q src examples`
- [x] `PYTHONPATH=src:. python -m examples.tri_temporal_commit_grid`
- [x] working tree clean after report commit
- [x] source ZIP created from Git-tracked files only
- [x] source ZIP extracted to a fresh directory
- [x] fresh archive `python -m pytest -q` passes
- [x] fresh archive demo passes
