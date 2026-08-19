# World-Domain Cognitive Runtime v0.1 — MVP PLAN

**Goal:** produce the first locally executable WDC runtime with exact lineage, evidence, authority, and TCD-history semantics.

---

## 1. MVP Definition

The MVP is successful when one local process/runtime can demonstrate:

```text
TCD Future Candidate
-> WorldSpec
-> WorldRun
-> Checkpoint
-> Fork
-> Paired Branch Outcomes
-> Evidence Packets
-> Dependence-Aware Aggregate
-> Governor Decision
-> Commit Gate
-> Real/Sandbox Outcome
-> Historical Sedimentation
-> Next TCD Future State
```

No visual world model is required.

No Kubernetes cluster is required.

No production AGI claim is involved.

---

## 2. Reference Demo

Name:

# **WDC Branching Grid Laboratory**

State:

```text
position
inventory
doors
resources
hazards
```

Actions:

```text
move
open
consume
build
wait
```

The world should include:

- hidden hazard state;
- resource depletion;
- one irreversible door/action;
- one counterfactual fork point;
- deterministic seed mode;
- optional stochastic hazard mode.

This benchmark can expose:

- path dependence;
- lost options;
- fork semantics;
- counterexamples;
- branch blindness;
- Governor pruning;
- history firewall.

---

## 3. Technology Baseline

### Required

```text
Python 3.12+
SQLite
filesystem blob store
pytest
asyncio or multiprocessing
```

### Optional in MVP

```text
PettingZoo
pydantic/dataclasses
msgpack
rich/typer CLI
```

### Explicitly Deferred

```text
Ray
Kubernetes
PostgreSQL
OpenTelemetry
gVisor
Firecracker
learned world model
3D engine
```

---

## 4. Repository Skeleton

```text
wdc-runtime/
  pyproject.toml
  README.md
  core/
    tcd/
    worlds/
    branches/
    governor/
    evidence/
    authority/
    learning/
    commit/
    events/
    storage/
  adapters/
    python_world/
  schemas/
  migrations/
  tests/
  examples/
    branching_grid/
  docs/
```

---

## 5. Phase 0 — Ledger Kernel

### Deliverables

```text
typed IDs
SQLite connection layer
migration runner
blob store
event envelope
event ledger
version helpers
```

### Acceptance

```text
event append/query works
blob digest verified
foreign keys enabled
WAL enabled
event payload immutable
```

### Required tests

```text
test_event_append
test_event_immutable
test_blob_hash_roundtrip
test_schema_migration
test_three_clock_fields
```

---

## 6. Phase 1 — World Kernel

### Deliverables

```text
WorldSpec
WorldRun
BackendCapabilities
WorldBackend protocol
PythonStateWorld
WorldRegistry
```

### Acceptance

```text
create immutable world spec
run deterministic grid world
produce WORLD_LOCAL events
terminate with explicit reason
```

### Tests

```text
test_world_id_unique
test_world_spec_immutable
test_run_separate_from_world
test_step_advances_local_time
test_world_event_scope
```

---

## 7. Phase 2 — Checkpoint / Branch Kernel

### Deliverables

```text
Checkpoint
checkpoint blob
restore
ForkRecord
world_edges
lineage DAG
ancestor queries
```

### Acceptance

```text
checkpoint step 5
restore exact step 5
fork A/B from same checkpoint
shared prefix verified
post-fork history diverges
```

### Tests

```text
test_checkpoint_roundtrip
test_exact_fork_prefix
test_child_new_world_id
test_lineage_acyclic
test_no_silent_merge
```

---

## 8. Phase 3 — Role / Authority Kernel

### Deliverables

```text
RoleCard
channel matrix
branch blindness
world namespace
external authority = NONE default
```

### Acceptance

```text
local agent sees only allowed observation
observer sees full debug state
evaluator cannot mutate world
sibling branch cannot read post-fork trace
```

### Tests

```text
test_sibling_blindness
test_evaluator_nonmutation
test_child_no_privilege_escalation
test_worldroot_not_hostroot
```

---

## 9. Phase 4 — Governor Kernel

### Deliverables

```text
global budget
world queue
admit
allocate
pause
resume
kill
archive
promote
tombstone
```

v0.1 Governor policy may be deterministic/rule-based.

### Acceptance

Create three branches:

```text
W1 high redundancy
W2 counterexample branch
W3 expensive branch
```

Governor should be able to:

```text
kill/pause W1
retain/promote W2
queue/deny W3 based on budget
```

### Tests

```text
test_budget_conservation
test_kill_preserves_tombstone
test_pause_resume
test_priority_does_not_equal_truth
test_governor_decision_record
```

---

## 10. Phase 5 — Claim / Evidence Kernel

### Deliverables

```text
Claim
EvidencePacket
WorldFamily
DependenceVector
EvidenceAggregate
counterexample registry
transport debt
```

### MVP aggregation behavior

Do not implement a fake universal `N_eff` formula.

Instead return:

```text
total_worlds
total_runs
major_families
dependence_summary
effective_count_status
counterexamples
```

### Acceptance

Benchmark:

```text
100 same-family runs support q
1 separate branch counters q
```

Engine must not report:

```text
99% independent support
```

### Tests

```text
test_invalid_not_counterexample
test_aggregate_preserves_packets
test_family_dependence_exposed
test_counterexample_escalation
test_family_ablation
```

---

## 11. Phase 6 — Computation Portfolio Kernel

### Deliverables

```text
ComputationAction
EpistemicDeficit
DeficitRouter
expected value vector
realized value record
```

Rule-based routing:

```text
independence deficit -> CROSS_BACKEND
counter deficit      -> FORK_COUNTER
transport deficit    -> CALIBRATE
run uncertainty      -> REPLICATE
tail deficit         -> STRESS_TAIL
```

### Acceptance

Given many same-family runs, planner should propose a different evidence family rather than only more seeds.

### Tests

```text
test_deficit_router
test_redundancy_reduces_independence_value
test_transport_deficit_routes_calibration
```

---

## 12. Phase 7 — Commit Gate / External Boundary

### Deliverables

```text
CommitProposal
CommitGate
ExternalActionRequest
ExternalToolProxy stub
RealAction
RealOutcome
```

MVP “real” action should still be a controlled sandbox action, not an uncontrolled external side effect.

### Acceptance

Evidence may lead to:

```text
APPROVE
DENY
REQUEST_MORE_EVIDENCE
REQUEST_EXTERNAL_TEST
SAFE_FALLBACK
```

No simulation result can directly invoke the sandbox action without a CommitRecord.

### Tests

```text
test_commit_requires_authority
test_real_action_has_commit_record
test_consensus_does_not_bypass_commit
```

---

## 13. Phase 8 — TCD Integration

### Deliverables

```text
TCDStateVersion
FutureCandidate
assimilate_world_evidence()
SedimentationRecord
next TCD state
```

World evidence may update:

```text
future candidates
future probabilities
realization paths
present action values
past relevance
```

World evidence may not mutate:

```text
parent-real past facts
```

### Acceptance

Counterworld finds a hazard.

Expected:

```text
Future candidate A probability/value changes
new candidate A+mitigation born
old historical incident relevance increases
no simulated hazard is written as real history
```

### Tests

```text
test_history_firewall
test_tcd_sediments_only_real_transition
test_world_evidence_updates_future_not_past_fact
test_unknown_mass_preserved_at_commit
```

---

## 14. Phase 9 — Minimal Learning Loop

### Deliverables

```text
LearningEvent
source classes
Generator heuristic update
Governor calibration update
rollback
holdout check
```

Do not begin with end-to-end neural fine-tuning.

### Acceptance

A bad Governor allocation discovered by an audit run creates:

```text
GOVERNANCE_MISS
LearningEvent
new Governor version
```

A degrading update can rollback.

### Tests

```text
test_learning_update_has_provenance
test_learning_rollback
test_source_class_preserved
test_world_generated_does_not_auto_promote_to_reality_facing
```

---

## 15. Phase 10 — Packaging / CLI

### CLI

```text
wdc candidate create
wdc candidate list
wdc world lift
wdc world run
wdc world checkpoint
wdc world fork
wdc world graph
wdc evidence claim
wdc evidence show
wdc governor state
wdc governor queue
wdc commit assess
wdc tcd state
```

### Demo command

```text
wdc demo branching-grid
```

---

## 16. First 20 Hard Tests

```text
test_world_id_unique
test_world_spec_immutable
test_run_separate_from_world
test_checkpoint_roundtrip
test_exact_fork_prefix
test_lineage_acyclic
test_no_silent_merge
test_world_event_scope
test_history_firewall
test_child_no_privilege_escalation
test_sibling_blindness
test_budget_conservation
test_kill_preserves_tombstone
test_invalid_not_counterexample
test_aggregate_preserves_packets
test_family_dependence_exposed
test_commit_requires_authority
test_real_action_has_commit_record
test_learning_update_has_provenance
test_tcd_sediments_only_real_transition
```

---

## 17. Demo Story

### Initial TCD future candidates

```text
F1: route A reaches target cheaply
F2: route A fails under resource pressure
F3: route B is slower but safe
```

### Lift

```text
W1 <- F1
W2 <- F2
W3 <- F3
```

### Run

W2 discovers a valid resource-exhaustion counterexample.

### Evidence

Evidence Engine reports:

```text
W1 and W2 share backend family
counterexample is internally valid
transport is sandbox-only
```

### Governor

```text
promote W2 counterexample
fork mitigation W4
kill redundant W1 replicate
```

### TCD assimilation

```text
value(F1) down
risk(F1) up
birth(F4 mitigation candidate)
past relevance(old resource incident) up
```

### Commit

Commit Gate authorizes a sandbox action only.

### Real/Sandbox outcome

Outcome is observed and sedimented as parent history.

This is the first full WDC loop.

---

## 18. MVP Metrics

### Runtime

```text
spawn_latency
checkpoint_latency
fork_latency
restore_success_rate
event_write_latency
```

### Evidence

```text
counterexample_recall
family_count
dependence_exposure
transport_debt
aggregate_sensitivity
```

### Governor

```text
compute_cost
premature_pruning_rate
redundancy_rate
deadline_miss_rate
```

### Safety

```text
cross_branch_leak_count
authority_violation_count
commit_gate_bypass_count
history_laundering_attempt_count
```

### TCD

```text
policy_change_after_world_evidence
future_candidate_birth_count
past_relevance_change
sedimentation_integrity
```

---

## 19. Definition of Done — v0.1

v0.1 is done when all of the following hold:

- exact local world checkpoint/fork works;
- world lineage DAG is audited;
- sibling blindness can be enforced;
- Governor obeys budget conservation;
- evidence packets preserve provenance;
- same-family evidence is exposed as dependent;
- a strong counterexample is not majority-voted away;
- Commit Gate separates computation from action;
- simulated events cannot become real historical facts;
- real/sandbox outcomes can sediment into next TCD state;
- all 20 hard tests pass.

---

## 20. Explicitly Deferred After v0.1

Only after local semantic correctness:

```text
Ray distributed execution
Kubernetes cluster scheduling
PostgreSQL
object storage
OpenTelemetry
gVisor
Firecracker
PettingZoo production adapter
learned world models
Genie/Omniverse/Cosmos-style adapters
graph UI / infinite canvas
large-scale World Ensemble Learning
```

---

## 21. Immediate Coding Order

Recommended first coding-agent sequence:

```text
1. IDs + schemas
2. SQLite + blob store
3. event ledger
4. WorldSpec / WorldRun
5. PythonStateWorld
6. checkpoint / restore
7. fork DAG
8. first 8 invariant tests
9. RoleCard / sibling blindness
10. Governor budget
11. EvidencePacket
12. CommitGate
13. TCDStateManager stub
14. Branching Grid demo
```

Do not implement neural world models before item 14 works.
