# WDC Runtime Phase 6–8 Implementation Report

**Date:** 2026-08-17  
**Branch:** `feature/phase6-8`  
**Base:** Phase 0–5 commit `4076d8772425620522cfc4efd67d4dd5082c1d7f`

## Scope completed

Phase 6–8 closes the first controlled TCD/WDC loop on top of the verified Phase 0–5 runtime.

### Phase 6 — Computation Portfolio Kernel

Implemented `src/wdc/portfolio.py`:

- `ComputationOperation`
- `EpistemicDeficit`
- `ComputationAction`
- deterministic `DeficitRouter`
- SQLite persistence for proposed computation actions

Reference routing:

```text
transport deficit      -> CALIBRATE
counterexample deficit -> FORK_COUNTER
independence deficit   -> CROSS_BACKEND
run uncertainty        -> REPLICATE
tail deficit           -> STRESS_TAIL
unknown-world deficit  -> EXPLORE_UNKNOWN
fidelity deficit       -> REFINE_FIDELITY
otherwise              -> RUN_MORE
```

A `ComputationAction` is a proposal only; it does not allocate or execute resources.

### Phase 7 — Reality Commit Gate / Controlled Sandbox Boundary

Implemented `src/wdc/commit.py`:

- `CommitProposal`
- `CommitDecision`
- `CommitRecord`
- `CommitGate`
- `ExternalToolProxy`
- durable sandbox action records

Hard behavior:

- missing required permission -> `DENY`
- missing or unknown evidence aggregate -> `REQUEST_MORE_EVIDENCE`
- high empirical transport debt -> `REQUEST_EXTERNAL_TEST`
- unresolved counterexamples -> `REQUEST_MORE_EVIDENCE`
- failed/unknown safety status -> `SAFE_FALLBACK`
- controlled sandbox action with valid evidence + authority -> `APPROVE`

The proxy executes only the exact action payload authorized by an approved commit record.

No uncontrolled external API is implemented.

### Phase 8 — TCD Integration / History Firewall

Implemented `src/wdc/tcd.py`:

- `FutureCandidate`
- `TCDStateVersion`
- `TCDDelta`
- `SedimentationRecord`
- `TCDStateManager.create_initial()`
- `TCDStateManager.assimilate_world_evidence()`
- `TCDStateManager.sediment_transition()`

Assimilation at the same parent time may update:

```text
Future candidate probability/value
new Future candidates
Present action values
Past relevance
Unknown-world mass
```

It may not update:

```text
Parent-real past facts
Parent historical time
```

Sedimentation requires the controlled sandbox transition to have:

1. an approved commit record;
2. a recorded sandbox action bound to that commit;
3. matching parent time.

Only then does parent time advance exactly once and the observed sandbox-real fact enter the parent historical facts.

`EXTERNAL_REAL` sedimentation is deliberately rejected in v0.1 until a provenance-validating external evidence adapter exists.

## Code-review hardening

Before packaging, the implementation was self-reviewed because this environment exposes no general-purpose code-review subagent tool.

The review found and fixed two provenance gaps:

1. Commit Gate originally checked only that aggregate IDs were non-empty. It now verifies every referenced aggregate exists.
2. TCD assimilation originally accepted arbitrary aggregate IDs and allowed a raw `EXTERNAL_REAL` scope. It now verifies aggregate existence and rejects external-real ingestion until an adapter exists.

These changes prevent fake provenance strings from becoming action or historical authority.

## Integration demo

New demo:

```text
examples/tri_temporal_commit_grid.py
```

It composes the Phase 0–5 governed evidence demo with Phase 6–8:

```text
Branching worlds
-> same-family dependence exposed
-> strong counterexample
-> independence deficit
-> CROSS_BACKEND computation proposal
-> TCD evidence assimilation at t=0
-> mitigation candidate born
-> Commit Gate
-> approved sandbox-only mitigation
-> sandbox outcome
-> Historical Sedimentation
-> TCD state at t=1
```

Observed integration values during verification:

```text
portfolio_operation = CROSS_BACKEND
commit_decision = APPROVE
history_firewall_preserved = true
parent_time_before = 0
parent_time_after_assimilation = 0
parent_time_after = 1
original_candidate_probability = 0.70 -> 0.35
past_relevance = 0.20 -> 0.95
unknown_world_mass_at_commit = 0.35
```

## Database additions

Added tables:

```text
computation_actions
commit_records
sandbox_actions
tcd_state_versions
tcd_deltas
sedimentation_records
```

## New tests

Added:

```text
tests/test_portfolio.py
tests/test_commit_gate.py
tests/test_tcd_integration.py
tests/test_phase6_8_integration.py
```

Coverage includes:

- deficit routing;
- computation persistence;
- authority denial;
- unknown aggregate rejection;
- consensus cannot bypass commit;
- empirical transport-debt gate;
- exact approved action payload enforcement;
- world evidence cannot mutate past facts;
- fake aggregate provenance rejection;
- external-real ingestion rejection until adapter exists;
- sandbox sedimentation requires approved action;
- parent time advances exactly once;
- complete Phase 0–8 integration flow.

## Permanent invariants now executable

```text
WorldSpec != WorldRun
World-Local Event != Parent-Real Historical Fact
World Count != Independent Evidence Count
Worth Computing != Worth Believing != Worth Deploying
ComputationAction != Resource Allocation
Simulation Consensus != External Authority
World Evidence Assimilation != Historical Fact Mutation
Approved Commit + Executed Sandbox Action -> eligible sedimentation
```

## Deferred after Phase 8

Not implemented here:

- external evidence adapter;
- real uncontrolled tool execution;
- Phase 9 learning loop;
- Ray/Kubernetes distributed runtime;
- PostgreSQL/object store;
- gVisor/Firecracker adapters;
- learned world-model backend;
- neural Governor/VOC estimator.
