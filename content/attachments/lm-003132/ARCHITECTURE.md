# World-Domain Cognitive Runtime v0.1 — ARCHITECTURE

**Status:** implementation contract v0.1  
**Derived from:** `World_Domain_Cognitive_Runtime_v0.1_Technical_Whitepaper_2026-08-17.md`  
**Primary goal:** implement the smallest auditable runtime before distributed scale or photorealistic backends.

---

## 1. Architectural Thesis

WDC Runtime is a **typed execution and evidence runtime** around TCD prospective cognition.

The parent loop is:

$$
\boxed{
TCDState_t
\rightarrow
FutureCandidates_t
\rightarrow
WorldComputations_t
\rightarrow
CrossWorldEvidence_t
\rightarrow
UpdatedPolicy_t
\rightarrow
CommitGate
\rightarrow
RealAction_t
\rightarrow
RealOutcome_{t+1}
\rightarrow
TCDState_{t+1}.
}
$$

Permanent boundaries:

$$
\boxed{
\text{Future Candidate}
\neq
\text{Runnable World}
\neq
\text{Actual Future}.
}
$$

$$
\boxed{
\text{World-Local Event}
\neq
\text{Parent-Real Historical Fact}.
}
$$

$$
\boxed{
\text{World Priority}
\neq
\text{World Truth}
\neq
\text{World Moral Worth}.
}
$$

$$
\boxed{
\text{Worth Computing}
\neq
\text{Worth Believing}
\neq
\text{Worth Deploying}.
}
$$

---

## 2. v0.1 Hard Invariants

These are implementation invariants, not aspirations.

### I1 — Three Clocks Stay Separate

Every relevant record must distinguish:

```text
parent_time
deliberation_index
world_local_time
```

Never flatten these into one generic `time`.

### I2 — WorldSpec Is Not WorldRun

```text
WorldSpec != WorldRun
```

A specification may be executed many times. Replay must create a new `run_id`, not silently overwrite an existing run.

### I3 — Historical Lineage Is Acyclic

World ancestry must be a DAG.

```text
child cannot become its own ancestor
```

### I4 — Fork Creates New Identity

```text
child_world_id != parent_world_id
```

A fork must record parent, checkpoint, divergence delta, seed policy, and child contract.

### I5 — History Firewall

A `WORLD_LOCAL` event may become a `PARENT_INTERNAL` evidence record, but cannot silently become an `EXTERNAL_REAL` fact.

### I6 — Authority Does Not Increase by Nesting

Without an explicit higher-level grant:

```text
child_external_permissions ⊆ parent_external_permissions
```

### I7 — Cross-World Aggregation Preserves Inputs

An evidence aggregate never destroys or replaces the evidence packets that produced it.

### I8 — Commit Is Separate From Simulation

`PromoteWorld`, `EvidenceAggregateUpdated`, or “many worlds agree” never grants real-world authority.

### I9 — Every Consequential Learning Update Is Versioned

Every generator/model/Governor/TCD update has:

```text
before_version
after_version
source_evidence
reason
validation
rollback_ref
```

### I10 — Global Resource Conservation

Active allocations must remain inside the declared global budget.

---

## 3. Four-Plane Architecture

### 3.1 Control Plane

Owns cognitive/runtime control semantics:

```text
TCDStateManager
FutureGenerator
WorldRegistry
WorldInstantiator
BranchManager
WorldGovernor
ComputationPortfolioPlanner
RoleAndAuthorityManager
RealityCommitGate
```

The Control Plane decides **what should be computed** and **what may be committed**.

It does not implement domain physics itself.

### 3.2 World Execution Plane

Owns executable world dynamics through adapters:

```text
PythonStateWorld
PettingZooAdapter
ExternalProcessAdapter
LearnedWorldAdapter
future simulator adapters
```

Every backend implements the same minimum `WorldBackend` contract.

### 3.3 Evidence / History Plane

Owns durable provenance:

```text
EventLedger
CheckpointStore
WorldLineageGraph
ClaimRegistry
EvidenceEngine
EvidenceAggregateStore
LearningEventStore
HistoricalSedimentationStore
```

This plane is append-oriented and versioned.

### 3.4 External Boundary Plane

Owns contact with reality:

```text
ExternalEvidenceAdapter
ExternalToolProxy
ExternalAuthorizer
RealActionExecutor
RealObservationIngest
```

World-local actors never directly inherit this authority.

---

## 4. Module Boundaries

### TCDStateManager

Owns:

```text
Past Base Space
Present Base Space
Future Base Space
parent temporal versions
```

May accept world evidence through an explicit assimilation interface.

Must reject direct mutation of historical facts by simulated events.

### FutureGenerator

Produces `FutureCandidate` objects.

Does not spawn worlds directly.

### WorldInstantiator

Transforms an admitted candidate/world request into immutable `WorldSpec`.

Does not decide whether a candidate deserves compute; that belongs to the Governor / Portfolio Planner.

### WorldRegistry

Owns IDs, status, versions, lineage pointers, backend metadata.

Does not own large checkpoint blobs.

### BranchManager

Owns checkpoint validation, fork construction, ancestry queries, DAG integrity.

State merge is denied by default.

### WorldGovernor

Owns:

```text
admission
budget allocation
queueing
pause/resume
preemption
kill/archive
promotion/demotion
```

The Governor answers:

```text
Should compute?
How much compute?
Should continue?
```

A scheduler adapter answers:

```text
Where and when should this workload run?
```

### ComputationPortfolioPlanner

Owns WDC-06 computation actions:

```text
RUN_MORE
REPLICATE
FORK_COUNTER
EXPLORE_UNKNOWN
CROSS_BACKEND
REFINE_FIDELITY
STRESS_TAIL
CALIBRATE
TRANSPORT_TEST
EXTERNAL_TEST_PROPOSAL
```

v0.1 should begin with rule-based deficit routing.

### RoleAndAuthorityManager

Owns role cards and explicit information channels.

Roles include:

```text
MASTER
LOCAL_AGENT
OBSERVER
EVALUATOR
GOVERNOR
SAFETY_OBSERVER
EXTERNAL_AUTHORIZER
```

### EvidenceEngine

Owns claim-aware evidence packets, evidence families, dependence metadata, counterexamples, family ablations, transport debt, and aggregate versions.

It must never default to “one world, one vote”.

### WorldEnsembleLearner

Owns four distinct update channels:

```text
GeneratorUpdate
WorldModelUpdate
GovernorUpdate
FutureSpaceUpdate
```

These channels must remain separate.

### RealityCommitGate

The only normal path from WDC internal evidence to an authorized parent-real action.

### HistoricalSedimentationStore

Stores parent-real action/outcome history plus WDC decision provenance.

It records that a simulation produced an outcome; it does not rewrite the simulated outcome as a real event.

---

## 5. Three Clock Model

WDC has three clocks:

$$
\boxed{
(t,k,\tau_i)
}
$$

- `t`: parent historical time.
- `k`: parent deliberation iteration within the same decision moment.
- `tau_i`: local runtime time of world `W_i`.

A world can run one million local steps while parent historical time remains unchanged.

Only a real parent commit and resulting external transition advance `t`.

---

## 6. Parent Decision Flow

```text
1. Load TCD state.
2. Generate future candidates.
3. Compute epistemic deficits.
4. Propose world-computation actions.
5. Governor admits / rejects / queues.
6. Instantiate and run worlds.
7. Build evidence packets.
8. Aggregate with dependence + counterexamples + transport debt.
9. Assimilate into Future / Present valuation / Past relevance.
10. Repeat bounded deliberation if useful.
11. Submit CommitProposal.
12. Commit Gate approves / denies / requests more evidence.
13. Execute authorized real/sandbox action.
14. Ingest real outcome.
15. Create HistoricalSedimentationRecord.
16. Update TCD state and learning targets.
```

---

## 7. World Execution Flow

```text
WorldSpec
  -> WorldRun
  -> initialize
  -> step*
  -> checkpoint*
  -> observe*
  -> outcome
  -> evaluate
  -> terminate
  -> archive
```

A fork is:

```text
WorldRun(parent)
  -> Checkpoint
  -> ForkRecord
  -> Child WorldSpec
  -> Child WorldRun
```

---

## 8. World Graph Semantics

Allowed lineage edge families:

```text
INSTANTIATE
CLONE
FORK
REPLAY
INTERVENE
MUTATE
MERGE_EVIDENCE
MERGE_LINEAGE
```

`MERGE_STATE` is denied unless a reconciliation adapter is explicitly registered.

Fork types:

```text
CLONE
CONTROLLED_FORK
COUNTERFACTUAL
PARAMETER_MUTATION
POLICY_MUTATION
RULE_MUTATION
BACKEND_MUTATION
```

---

## 9. History Firewall

Event scopes:

```text
WORLD_LOCAL
PARENT_INTERNAL
EXTERNAL_REAL
```

Valid transformation:

```text
WORLD_LOCAL: CityCollapsed
    ->
PARENT_INTERNAL: WorldOutcomeObserved(
    world_id=W17,
    result=CityCollapsed
)
```

Invalid transformation:

```text
WORLD_LOCAL: CityCollapsed
    -X->
EXTERNAL_REAL: CityCollapsed
```

Only external observations/actions or explicitly verified external evidence may create parent-real facts.

---

## 10. Role / Information Architecture

Every role receives a `RoleCard`.

A role card declares:

```text
observation scope
write/action scope
tool scope
external authority
memory scope
cross-world channel allowlist
audit level
```

Branch blindness modes:

```text
ISOLATED_UNTIL_RESOLUTION
EXPLICIT_CHANNELS
OPEN
```

Paired counterfactual benchmarks should default to `ISOLATED_UNTIL_RESOLUTION`.

---

## 11. Security Architecture

Reference isolation classes:

```text
S0_INPROCESS
S1_PROCESS
S2_CONTAINER
S3_GVISOR
S4_MICROVM
```

Default external policy:

```text
network = DENY
host_fs = DENY
external_credentials = NONE
external_tools = PROXY_ONLY
```

External tools must follow:

```text
World
 -> ExternalToolProxy
 -> ExternalAuthorizer
 -> RealTool
```

World-local `root` never means host root.

---

## 12. Storage Architecture

### Local Reference Runtime

```text
SQLite WAL
+
filesystem content-addressed blob store
```

Metadata remains transactional and queryable.

Large objects remain outside metadata rows:

```text
checkpoints
traces
artifacts
large state snapshots
```

Store blob references as:

```text
sha256
size
mime_type
storage_uri
```

Hash proves integrity, not truth.

### Distributed Evolution

Replace infrastructure without changing semantics:

```text
SQLite      -> PostgreSQL
filesystem  -> object storage
processes   -> Ray actors
local queue -> Kubernetes/Ray
local logs  -> OpenTelemetry
```

---

## 13. Event / Provenance Architecture

Use a persisted event ledger for consequential events.

Distributed telemetry may use OpenTelemetry, but:

```text
Telemetry != Evidence Ledger
```

Telemetry may be sampled.

Evidence-critical and historical-critical records must not disappear due to telemetry sampling.

Recommended reliability classes:

```text
EPHEMERAL_TELEMETRY
PERSISTENT_OPERATION
EVIDENCE_CRITICAL
HISTORICAL_CRITICAL
```

---

## 14. Local-First Deployment

### v0.1

```text
Python
SQLite WAL
filesystem blobs
asyncio / multiprocessing
PythonStateWorld
CLI
```

### v0.2+

```text
PostgreSQL
object store
Ray actors
OpenTelemetry
optional Kubernetes
gVisor / Firecracker
```

Do not begin with Kubernetes merely because the eventual architecture is distributed.

---

## 15. Reference Repository Layout

```text
wdc-runtime/
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
    pettingzoo/
    external_process/
    ray/
    kubernetes/
    gvisor/
    firecracker/
  schemas/
  migrations/
  tests/
  examples/
  docs/
```

Suggested package namespaces:

```text
wdc.tcd
wdc.worlds
wdc.branches
wdc.governor
wdc.evidence
wdc.roles
wdc.learning
wdc.commit
wdc.events
wdc.storage
wdc.adapters
```

---

## 16. Architecture Acceptance Criteria

The architecture is considered executable, not “proven”, when a local demo can:

1. create TCD future candidates;
2. lift candidates to worlds;
3. execute and checkpoint a world;
4. fork an exact child;
5. preserve a lineage DAG;
6. isolate sibling branches;
7. create evidence packets;
8. expose shared-family dependence;
9. let Governor kill a redundant branch;
10. route a valid counterexample to escalation;
11. pass a proposal through Commit Gate;
12. preserve the simulated-vs-real history boundary;
13. sediment the actual real/sandbox transition;
14. update the next Future Base Space.

---

## 17. Architectural Anti-Patterns

Do not implement WDC as:

```text
one LLM repeatedly prompting itself
and calling every answer a world
```

Do not:

- conflate `WorldSpec` and `WorldRun`;
- let world-local events mutate real history;
- let branch children inherit unrestricted host secrets;
- aggregate worlds by raw majority;
- attach permanent “worth” scores to worlds;
- let promotion imply deployment authority;
- train reality-facing models on synthetic worlds without provenance/transport gates;
- start distributed scaling before exact local lineage tests pass.

---

## 18. First Engineering Decision

The first implementation target is **Branching Grid Laboratory**, not a visual world model.

The objective is to prove the runtime semantics are executable:

```text
Candidate
-> World
-> Checkpoint
-> Fork
-> Evidence
-> Governor
-> Commit
-> Real/Sandbox Outcome
-> TCD Sedimentation
```

Only after this loop is correct should the project add heavier backends.
