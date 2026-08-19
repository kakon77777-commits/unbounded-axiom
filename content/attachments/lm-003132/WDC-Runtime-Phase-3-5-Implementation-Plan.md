# WDC Runtime Phase 3–5 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the executable local WDC kernel with role/authority isolation, a bounded lifecycle Governor, and dependence-aware cross-world evidence without weakening Phase 0–2 lineage/checkpoint invariants.

**Architecture:** Keep production code stdlib-only. Add role and authority records as explicit control-plane objects; add an authoritative mutable governance-state table rather than mutating immutable `WorldSpec`; add claim/evidence/family tables and aggregate reports that preserve packets and expose dependence instead of fabricating a universal effective evidence count.

**Tech Stack:** Python 3.11+, stdlib (`dataclasses`, `enum`, `sqlite3`, `json`, `typing`), pytest.

## Global Constraints

- Preserve all Phase 0–2 tests and public interfaces unless a new invariant requires a narrow compatible extension.
- `WorldSpec != WorldRun`; `WorldSpec` remains immutable.
- Fork child authority may not exceed parent authority without an explicit grant.
- Local roles do not see sibling post-fork worlds without an enabled cross-world channel.
- Governor manages compute/lifecycle, not truth or moral worth.
- Active allocation never exceeds the global numeric resource budget.
- `INVALID` evidence is never counted as counterevidence.
- Aggregation preserves source packets and exposes family dependence.
- No fake universal `N_eff`; Phase 5 reports `UNRESOLVED` unless a calibrated estimator is supplied.
- Tests are written and observed failing before production code.

---

### Task 1: Role cards, authority profiles, channels, and sibling blindness

**Files:**
- Create: `src/wdc/roles.py`
- Modify: `src/wdc/db.py`
- Modify: `src/wdc/branches.py`
- Test: `tests/test_roles_authority.py`

**Interfaces:**
- Produces: `RoleType`, `RoleCard`, `AuthorityProfile`, `ChannelRule`.
- Produces: `RoleManager.create_authority_profile/get_authority_profile/create_role/get_role/open_channel/assert_can_observe_world`.
- Extends: `BranchManager(..., authority_manager: RoleManager | None = None)`; changed child authority refs are denied unless validated as a subset.

- [x] **Step 1: Write failing tests**

```python
def test_local_role_cannot_observe_sibling_without_channel(...):
    with pytest.raises(ObservationDenied):
        roles.assert_can_observe_world(local_a.role_id, child_b.world_id)


def test_fork_rejects_authority_escalation(...):
    with pytest.raises(AuthorityEscalationError):
        branches.fork(..., child_spec_fields={"authority_profile_ref": elevated.profile_id})
```

- [x] **Step 2: Run tests to verify RED**

Run: `python -m pytest tests/test_roles_authority.py -q`
Expected: collection/import failure because `wdc.roles` does not exist.

- [x] **Step 3: Implement minimal role/authority/channel persistence and checks**

Authority subset rule:

```python
child.external_permissions <= parent.external_permissions
```

Observation rule: exact world scope is allowed; otherwise an enabled channel with the target world is required.

- [x] **Step 4: Run targeted and full tests GREEN**

Run:

```bash
python -m pytest tests/test_roles_authority.py -q
python -m pytest -q
```

- [x] **Step 5: Commit**

```bash
git add src/wdc/db.py src/wdc/roles.py src/wdc/branches.py tests/test_roles_authority.py
git commit -m "feat: add role and authority isolation"
```

### Task 2: Mutable governance state and global budget conservation

**Files:**
- Create: `src/wdc/governor.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_governor.py`

**Interfaces:**
- Produces: `WorldLifecycleStatus`, `GovernorDecision`, `WorldGovernor`.
- Produces: `ensure_world`, `allocate`, `release`, `pause`, `resume`, `kill`, `promote`, `get_state`, `decisions`.

- [x] **Step 1: Write failing tests**

```python
def test_governor_never_overallocates_global_budget(...):
    governor.allocate(w1, {"cpu": 2})
    with pytest.raises(BudgetExceeded):
        governor.allocate(w2, {"cpu": 1})


def test_kill_releases_budget_and_preserves_tombstone(...):
    governor.kill(world_id, reason="redundant")
    state = governor.get_state(world_id)
    assert state.status == WorldLifecycleStatus.KILLED
    assert state.tombstone_reason == "redundant"
```

- [x] **Step 2: Run tests to verify RED**

Run: `python -m pytest tests/test_governor.py -q`
Expected: import failure because `wdc.governor` does not exist.

- [x] **Step 3: Implement minimal Governor**

Use a separate `world_governance_state` table so mutable lifecycle does not mutate `WorldSpec`. Resource budgets are numeric mappings; missing resource keys are zero.

- [x] **Step 4: Run targeted and full tests GREEN**

```bash
python -m pytest tests/test_governor.py -q
python -m pytest -q
```

- [x] **Step 5: Commit**

```bash
git add src/wdc/db.py src/wdc/governor.py tests/test_governor.py
git commit -m "feat: add bounded world governor"
```

### Task 3: Claim registry and provenance-bearing evidence packets

**Files:**
- Create: `src/wdc/evidence.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_evidence_packets.py`

**Interfaces:**
- Produces: `ClaimType`, `EvidenceOutcome`, `SourceClass`, `Claim`, `EvidencePacket`, `EvidenceEngine`.
- Produces: `register_claim`, `get_claim`, `add_packet`, `packets`.

- [x] **Step 1: Write failing tests**

```python
def test_invalid_packet_is_not_counterexample(...):
    packet = engine.add_packet(..., outcome=EvidenceOutcome.INVALID, ...)
    assert engine.counterexamples(claim.claim_id) == []


def test_packet_preserves_world_run_and_provenance(...):
    loaded = engine.packets(claim.claim_id)[0]
    assert loaded.world_id == world_id
    assert loaded.run_id == run_id
    assert loaded.provenance_ref == "prov:test"
```

- [x] **Step 2: Verify RED**

Run: `python -m pytest tests/test_evidence_packets.py -q`
Expected: import failure because `wdc.evidence` does not exist.

- [x] **Step 3: Implement claim/packet persistence**

Internal validity and evaluator independence are stored as numeric values in `[0,1]` for the reference implementation; uncertainty/transport remain JSON metadata.

- [x] **Step 4: Run targeted/full GREEN**

```bash
python -m pytest tests/test_evidence_packets.py -q
python -m pytest -q
```

- [x] **Step 5: Commit**

```bash
git add src/wdc/db.py src/wdc/evidence.py tests/test_evidence_packets.py
git commit -m "feat: add claim and evidence packets"
```

### Task 4: World families, dependence vectors, and non-voting aggregate

**Files:**
- Modify: `src/wdc/evidence.py`
- Modify: `src/wdc/db.py`
- Test: `tests/test_evidence_aggregation.py`

**Interfaces:**
- Produces: `FamilyType`, `WorldFamily`, `DependenceVector`, `EvidenceAggregate`.
- Produces: `create_family`, `attach_world_family`, `estimate_pair_dependence`, `aggregate`, `family_ablation`.

- [x] **Step 1: Write failing tests**

```python
def test_same_backend_family_is_exposed_as_dependence(...):
    dep = engine.estimate_pair_dependence(e1.evidence_id, e2.evidence_id)
    assert dep.backend == 1.0


def test_aggregate_reports_families_and_unresolved_effective_count(...):
    agg = engine.aggregate(claim_id)
    assert agg.total_worlds == 3
    assert agg.major_family_count == 2
    assert agg.effective_count_status == "UNRESOLVED"
```

- [x] **Step 2: Verify RED**

Run: `python -m pytest tests/test_evidence_aggregation.py -q`
Expected: missing family/aggregate APIs.

- [x] **Step 3: Implement metadata-based dependence and aggregate**

Dependence dimensions are `1.0` when the two evidence packets' worlds share a registered family of that type, otherwise `0.0` in v0.1. This is a transparent reference estimator, not a scientific universal estimator.

- [x] **Step 4: Run targeted/full GREEN**

```bash
python -m pytest tests/test_evidence_aggregation.py -q
python -m pytest -q
```

- [x] **Step 5: Commit**

```bash
git add src/wdc/db.py src/wdc/evidence.py tests/test_evidence_aggregation.py
git commit -m "feat: add dependence-aware evidence aggregation"
```

### Task 5: Counterexample escalation and Governor handoff

**Files:**
- Modify: `src/wdc/evidence.py`
- Modify: `src/wdc/governor.py`
- Test: `tests/test_counterexample_escalation.py`

**Interfaces:**
- Produces: `CounterexampleAssessment` and `EvidenceEngine.assess_counterexample`.
- Produces: `WorldGovernor.propose_counterexample_escalation(...)` returning computation-operation recommendations.

- [x] **Step 1: Write failing tests**

```python
def test_strong_counterexample_requests_replication_and_cross_backend(...):
    assessment = engine.assess_counterexample(packet.evidence_id)
    assert assessment.escalate is True
    ops = governor.propose_counterexample_escalation(assessment)
    assert "REPLICATE" in ops
    assert "CROSS_BACKEND" in ops
```

- [x] **Step 2: Verify RED**

Run: `python -m pytest tests/test_counterexample_escalation.py -q`
Expected: missing escalation APIs.

- [x] **Step 3: Implement explicit threshold-based reference policy**

Reference threshold:

```text
internal_validity >= 0.8
evaluator_independence >= 0.5
outcome == COUNTER
```

The threshold is versioned policy, not a truth criterion.

- [x] **Step 4: Run targeted/full GREEN**

```bash
python -m pytest tests/test_counterexample_escalation.py -q
python -m pytest -q
```

- [x] **Step 5: Commit**

```bash
git add src/wdc/evidence.py src/wdc/governor.py tests/test_counterexample_escalation.py
git commit -m "feat: escalate strong counterexamples"
```

### Task 6: Governed Evidence Grid integration demo

**Files:**
- Create: `examples/governed_evidence_grid.py`
- Create: `tests/test_governed_evidence_grid_integration.py`
- Modify: `README.md`
- Create: `PHASE3_5_IMPLEMENTATION_REPORT.md`

**Interfaces:**
- Demonstrates exact sibling forks, isolated local roles, bounded Governor allocation, a valid counterexample packet, same-family dependence exposure, counterexample escalation, and redundant-branch kill/tombstone.

- [x] **Step 1: Write failing integration test**

```python
def test_governed_evidence_demo(...):
    result = run_demo(tmp_path)
    assert result["sibling_access_denied"] is True
    assert result["budget_conserved"] is True
    assert result["counterexample_escalated"] is True
    assert result["effective_count_status"] == "UNRESOLVED"
    assert result["redundant_world_status"] == "KILLED"
```

- [x] **Step 2: Verify RED**

Run: `python -m pytest tests/test_governed_evidence_grid_integration.py -q`
Expected: demo module missing.

- [x] **Step 3: Implement minimal integration wiring**

Reuse existing Branching Grid transitions; do not invent new core semantics for the demo.

- [x] **Step 4: Run full verification**

```bash
python -m pytest -q
python -m compileall -q src examples
PYTHONPATH=src:. python examples/governed_evidence_grid.py /tmp/wdc-governed-evidence-grid
```

- [x] **Step 5: Write report and commit**

```bash
git add README.md examples/governed_evidence_grid.py tests/test_governed_evidence_grid_integration.py PHASE3_5_IMPLEMENTATION_REPORT.md
git commit -m "feat: complete WDC phase 3-5 governed evidence demo"
```

## Final Verification

Run from a fresh extracted source archive:

```bash
python -m pytest -q
python -m compileall -q src examples
PYTHONPATH=src:. python examples/governed_evidence_grid.py /tmp/wdc-governed-evidence-grid-archive
```

Expected: all tests pass, demo reports sibling access denied, budget conserved, counterexample escalated, dependence exposed, and redundant world tombstoned.
