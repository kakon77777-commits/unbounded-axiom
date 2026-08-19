# World-Domain Cognitive Runtime v0.1 — EVENTS

**Purpose:** event envelope, event taxonomy, scope transitions, reliability, and provenance rules.

---

## 1. Event Philosophy

The event system has two distinct jobs:

1. operational coordination;
2. durable epistemic / historical provenance.

Do not conflate them.

$$
\boxed{
Telemetry
\neq
EvidenceLedger.
}
$$

Distributed telemetry may be sampled.

Evidence-critical and historical-critical events may not be silently dropped.

---

## 2. Event Envelope

Recommended envelope:

```text
event_id
event_type
source
subject
event_time
scope
schema_version
trace_id
span_id
parent_time
deliberation_index
world_local_time
world_id
run_id
actor_id
payload_ref
provenance_ref
reliability_class
```

Fields not applicable to an event may be null, but clock meaning must never be ambiguous.

---

## 3. Scope

```text
WORLD_LOCAL
PARENT_INTERNAL
EXTERNAL_REAL
```

### WORLD_LOCAL

Occurred inside a runnable world.

Example:

```text
AgentMoved
WorldObjectDestroyed
WorldLocalFailure
```

### PARENT_INTERNAL

Occurred in the parent computation/runtime.

Example:

```text
WorldOutcomeProduced
EvidencePacketCreated
GovernorDecisionMade
CommitProposalCreated
```

### EXTERNAL_REAL

Observed or executed across the real/external boundary.

Example:

```text
RealActionCommitted
RealSensorObservation
ExternalDatasetReceived
HumanAuthorizationGranted
```

---

## 4. History Firewall Rule

Valid:

```text
WORLD_LOCAL event
  -> PARENT_INTERNAL evidence record
```

Invalid:

```text
WORLD_LOCAL event
  -> EXTERNAL_REAL fact
```

Example:

```text
World local:
  CityCollapsed(world=W17)

Parent internal:
  WorldOutcomeProduced(
    W17,
    result=CityCollapsed
  )
```

The parent fact is that **W17 produced that result**, not that the real city collapsed.

---

## 5. Reliability Classes

```text
EPHEMERAL_TELEMETRY
PERSISTENT_OPERATION
EVIDENCE_CRITICAL
HISTORICAL_CRITICAL
```

### EPHEMERAL_TELEMETRY

May be sampled.

Examples:

```text
CPUUsageSample
WorkerHeartbeat
StepLatency
```

### PERSISTENT_OPERATION

Must normally be retained for operational audit.

Examples:

```text
WorldRunStarted
CheckpointCreated
WorldRunPaused
WorldKilled
```

### EVIDENCE_CRITICAL

Must be durably retained.

Examples:

```text
WorldOutcomeProduced
EvidencePacketCreated
CounterexampleFound
EvidenceAggregateUpdated
EvaluatorResult
```

### HISTORICAL_CRITICAL

Parent-real temporal provenance.

Examples:

```text
RealActionCommitted
RealOutcomeObserved
HistoricalSedimentCreated
```

---

## 6. Canonical Event Types

### TCD

```text
TCDStateCreated
TCDStateAdvanced
FutureCandidateBorn
FutureCandidateUpdated
FutureCandidateRetired
FutureSpaceUpdated
PastRelevanceUpdated
PresentValuationUpdated
```

### World lifecycle

```text
WorldProposed
WorldAdmitted
WorldRejected
WorldSpawned
WorldRunStarted
WorldRunPaused
WorldRunResumed
WorldRunCompleted
WorldKilled
WorldInvalidated
WorldArchived
```

### Checkpoint / branch

```text
CheckpointCreated
CheckpointRestored
CheckpointValidationFailed
WorldForked
WorldCloned
WorldReplayed
WorldIntervened
WorldMutated
WorldLineageViolation
```

### Roles / channels

```text
RoleCardCreated
RoleCardUpdated
ChannelOpened
ChannelClosed
CrossBranchAccessDenied
InformationFlowViolation
AuthorityGrantCreated
AuthorityRequestDenied
```

### Evidence

```text
ClaimRegistered
EvidencePacketCreated
EvaluatorResultCreated
EvidenceAggregateUpdated
CounterexampleFound
CounterexampleEscalated
FamilyDependenceUpdated
FamilyAblationCompleted
TransportDebtUpdated
UnknownWorldMassUpdated
```

### Governor / portfolio

```text
ComputationActionProposed
ComputationActionApproved
ComputationActionRejected
BudgetAllocated
BudgetRevoked
WorldPromoted
WorldDemoted
WorldPreempted
GovernorMissDetected
PortfolioRebalanced
```

### Commit / external reality

```text
CommitProposalCreated
CommitAssessmentCompleted
CommitApproved
CommitDenied
CommitDeferred
ExternalEvidenceRequested
HumanAuthorizationRequested
HumanAuthorizationGranted
RealActionCommitted
RealActionFailed
RealOutcomeObserved
```

### Learning

```text
LearningEventCreated
GeneratorUpdated
WorldModelUpdated
GovernorUpdated
FutureSpaceLearnerUpdated
LearningValidationFailed
LearningRollbackStarted
LearningRollbackCompleted
SelfSealingWarning
OntologyCoverageWarning
```

### Safety

```text
SandboxViolation
NetworkViolation
FilesystemViolation
CredentialViolation
RunawaySpawnDetected
SafetyKill
ExperimentContaminated
```

---

## 7. Event Versioning

Each event has:

```text
schema_version
```

Event payloads are immutable after persistence.

Corrections are new events:

```text
EventCorrectionIssued
```

Do not rewrite old events in place.

---

## 8. Provenance Chains

Every consequential event should resolve upstream.

Example:

```text
FutureCandidateBorn
  -> WorldSpawned
  -> WorldRunStarted
  -> WorldOutcomeProduced
  -> EvidencePacketCreated
  -> EvidenceAggregateUpdated
  -> CommitProposalCreated
  -> RealActionCommitted
  -> RealOutcomeObserved
  -> HistoricalSedimentCreated
```

---

## 9. Trace Context

Execution trace context:

```text
trace_id
span_id
```

Semantic provenance context:

```text
candidate_id
world_id
run_id
claim_id
evidence_id
aggregate_id
commit_id
```

OpenTelemetry-style trace IDs are useful for distributed execution, but semantic WDC provenance must be stored separately.

---

## 10. Clock Requirements

### Parent event

Must carry:

```text
parent_time
```

### Parent deliberation event

Carries:

```text
parent_time
deliberation_index
```

### World-local event

Carries:

```text
parent_time
deliberation_index
world_local_time
world_id
run_id
```

Do not infer one clock from another.

---

## 11. Event Ordering

Within one run, sequence ordering may use:

```text
world_local_time
event_seq
```

Across distributed services, do not assume wall-clock timestamps alone establish strict causal order.

Use explicit parent/provenance links where causal ordering matters.

---

## 12. Idempotency

For commands that may retry, produce stable idempotency keys.

Example:

```text
checkpoint(run_id, local_time, request_id)
```

Duplicate delivery must not create two semantically different checkpoints for one idempotent request.

---

## 13. Exactly-Once Is Not Assumed

The reference event pipeline should be robust to at-least-once delivery.

Consumers should use:

```text
event_id
```

for deduplication.

---

## 14. Counterexample Event Rule

`CounterexampleFound` requires a linked `EvidencePacket`.

It must never be created from a bare text assertion.

Minimum payload:

```text
claim_id
evidence_id
world_id
run_id
internal_validity
claim_type
escalation_status
```

---

## 15. Learning Event Rule

Every consequential update creates:

```text
LearningEventCreated
```

before the target version is made active.

Payload:

```text
target_component
update_type
source_evidence_ids
source_classes
synthetic_depth
prior_version
candidate_new_version
validation_plan
rollback_ref
```

On success:

```text
GeneratorUpdated
WorldModelUpdated
GovernorUpdated
FutureSpaceLearnerUpdated
```

On failure:

```text
LearningValidationFailed
LearningRollbackStarted
LearningRollbackCompleted
```

---

## 16. Commit Event Rule

No external-real action without:

```text
CommitProposalCreated
CommitAssessmentCompleted
CommitApproved
```

or another explicitly authorized exceptional path recorded by policy.

A commit event carries:

```text
evidence_aggregate_ids
transport_debt
unknown_world_mass
counterexamples
authority
```

---

## 17. Safety Override Rule

Safety may override experiment blindness.

Example:

```text
SafetyKill
```

must also create, where relevant:

```text
ExperimentContaminated
```

The system must not continue to report the experiment as untouched.

---

## 18. Sibling Branch Isolation

When:

```text
branch_visibility = ISOLATED_UNTIL_RESOLUTION
```

an attempted sibling post-fork access emits:

```text
CrossBranchAccessDenied
```

If actual leakage occurs:

```text
InformationFlowViolation
ExperimentContaminated
```

---

## 19. Persistence Policy

Suggested:

| Reliability | Retention |
|---|---|
| EPHEMERAL_TELEMETRY | sampled / TTL |
| PERSISTENT_OPERATION | durable operational retention |
| EVIDENCE_CRITICAL | durable, versioned |
| HISTORICAL_CRITICAL | durable, protected |

Exact retention duration is deployment policy, not theory.

---

## 20. CloudEvents Compatibility

A transport layer may map:

```text
event_id        -> id
event_type      -> type
source          -> source
subject         -> subject
event_time      -> time
schema_version  -> dataschema/datacontent metadata as appropriate
```

WDC-specific clocks, scope, IDs, and provenance remain extensions/payload.

---

## 21. Event Handler Contract

Handlers should be:

```text
idempotent where possible
scope-aware
version-aware
provenance-preserving
failure-explicit
```

A failed handler produces an explicit failure event; it must not silently discard an evidence-critical event.

---

## 22. Minimal Event Bus Interface

```python
class EventBus:
    def publish(self, event): ...
    def subscribe(self, event_type, handler): ...
    def replay(self, from_offset=None, filter=None): ...
```

Durable ledger:

```python
class EventLedger:
    def append(self, event): ...
    def get(self, event_id): ...
    def query(self, **filters): ...
```

---

## 23. v0.1 Event Tests

```text
test_world_local_cannot_be_real_fact
test_evidence_event_is_durable
test_historical_event_is_durable
test_event_payload_immutable
test_event_correction_is_new_event
test_at_least_once_dedup
test_three_clock_fields
test_counterexample_requires_packet
test_real_action_requires_commit
test_learning_update_requires_learning_event
test_sibling_leak_emits_violation
test_safety_kill_marks_contamination
```
