# Phase 12 — Persistent Autonomous Loop Design

**Project:** Addressable Cognitive Runtime MVP v0.1  
**Target release:** `0.1.20`  
**Target phase:** `Phase 12 - Persistent Autonomous Loop`  
**Target profile:** `ACR-MVP-v0.1-Phase12`  
**Design status:** v0.1 canonical engineering design  
**Date:** 2026-08-25  
**Upstream:** Phase 11 `0.1.19` Context Compression release

---

## 0. Purpose

Phase 12 is the final integration layer of the ACR MVP v0.1 roadmap. The previous phases already implement separate capabilities for semantic state, cognitive affordance retrieval, cognitive program compilation, self-dialogue, temporal evidence, decision evidence, reflexive autonomy, strategic cognition, Agenda formation, Commitment persistence, and reference-preserving context compression.

Phase 12 must not re-implement those subsystems. Its job is to provide a small persistent orchestration kernel that can call them in a stable order, sleep when nothing is worth doing, wake when new evidence or a due Commitment appears, recover after interruption, preserve causal history, and run for a bounded long horizon without a human authoring every next prompt.

The target question is:

> Can a human provide Goal + Contract + initial Environment once, then let the runtime author its own bounded cognitive and action trajectory over many cycles while retaining explicit governance, causality, commitment, recovery, and idle semantics?

Phase 12 therefore defines:

```text
PersistentLoopKernel
+
LoopRunState
+
CycleState
+
Wake/Sleep/Defer semantics
+
Checkpoint/Recovery
+
Subsystem orchestration
+
Sandbox action boundary
+
Long-horizon falsification
```

It does not define a new cognitive ontology, new strategy theory, or new authority model.

---

# 1. Canonical upstream invariants

Phase 12 inherits and preserves the following separations:

```text
Method != Law
SelfObservation != HiddenCoT
Can != Should != Authorized
Decision != Commit
AgendaCandidate != ActionCandidate
AgendaResolution != GovernanceDecision
AgendaSelection != AuthorityGrant
Commitment != ExternalObligation
CommitmentDue != AuthorityGrant
StrategicLens != CognitiveDomain
StrategyReview != Mandatory
StrategyShift != AtlasRepartition
WorkingMemory != HistoricalLedger
ContextCapsule != HistoricalTruth
SummaryBlock != Evidence
DiscardedFromContext != DeletedFromLedger
Compression != WorldMutation
```

Phase 12 adds:

```text
PersistentLoop != AutonomousWorldAuthority
CycleState != HistoricalLedger
LoopDisposition != GovernanceDecision
WakeConditionMatched != AutomaticExternalAction
WakeSignal != AuthorityGrant
Idle != Failure
NoAgenda != Error
Sleeping != Stopped
Deferred != Refused
Checkpoint != CommitReceipt
Replay != Re-execution
Recovery != Reenactment
ActionRequest != WorldCommit
SandboxTransition != ExternalWorldAuthority
LoopIteration != HumanPrompt
StopSignal != GovernanceRefusal
BudgetExhaustion != GoalFailure
KnowledgeRefreshCandidate != StrategyGraphPromotion
```

---

# 2. Design alternatives

## 2.1 Approach A — Monolithic mega-agent loop

```text
while true:
    observe
    reason
    strategize
    plan
    act
    remember
```

Advantages:

- simple to demonstrate;
- low initial code count.

Problems:

- collapses Phase 0–11 boundaries;
- makes governance, commitment, strategy, and compression invisible inside one loop;
- difficult to replay and audit;
- encourages busy-loop cognition;
- hard to prove no authority leakage;
- difficult to recover after a crash without repeating side effects.

**Rejected.**

## 2.2 Approach B — Full ledger replay before every cycle

Every iteration reconstructs all current runtime state by replaying the full CTCL/ITR ledger.

Advantages:

- mathematically clean event-sourced semantics;
- history is always canonical.

Problems:

- unnecessarily expensive at long horizon;
- conflicts with Phase 11's explicit WorkingMemory / HistoricalLedger separation;
- encourages using the historical ledger as hot working state;
- makes 100-cycle and larger runs progressively slower.

**Rejected as the default path.** Ledger replay remains a recovery/audit path.

## 2.3 Approach C — Persistent orchestration kernel over frozen subsystems

Use a small phase-12 kernel that carries current runtime refs and calls existing services. CTCL remains append-only historical evidence, while Phase 11 ContextCapsule remains the hot context representation.

```text
CurrentRunState
+
CurrentContextBinding
+
CommitmentStore
+
EnvironmentSnapshot
+
Frozen subsystem APIs
        ↓
PersistentLoopKernel.step()
        ↓
CycleResult + Temporal events + Checkpoint
```

Advantages:

- preserves all existing separations;
- efficient enough for long runs;
- explicit idle and wake semantics;
- supports deterministic replay and crash recovery;
- testable subsystem by subsystem;
- does not turn persistence into world authority.

**Selected architecture.**

---

# 3. Phase-12 package layout

Recommended new files:

```text
src/addressable_cognitive_runtime/persistent/
├── __init__.py
├── model.py
├── kernel.py
├── scheduler.py
├── checkpoint.py
├── recovery.py
├── policy.py
├── sandbox.py
└── reference.py

src/addressable_cognitive_runtime/temporal/
└── persistent.py
```

No existing Phase 0–11 production file should require semantic rewrite. Minimal exports/imports may be added to package `__init__` files only when they do not create circular imports.

---

# 4. Primary objects

## 4.1 PersistentRunState

Phase-12-local object:

```text
acr.persistent-run-state/v0.1
```

Suggested fields:

```json
{
  "schema": "acr.persistent-run-state/v0.1",
  "id": "prun:sha256:...",
  "version": 1,
  "fingerprint": "sha256:...",
  "run_id": "run:persistent:...",
  "cycle_seq": 17,
  "status": "RUNNING",
  "goal_refs": ["goal:v7"],
  "contract_ref": "contract:v12",
  "authority_ref": "authority:v12",
  "environment_ref": "env:sha256:...",
  "context_binding_ref": "ctxbind:sha256:...",
  "active_agenda_resolution_ref": "ares:sha256:...",
  "commitment_store_ref": "cstore:sha256:...",
  "last_checkpoint_ref": "pchk:sha256:...",
  "last_cycle_ref": "pcyc:sha256:...",
  "next_wake": null,
  "budget": {},
  "extensions": {}
}
```

`PersistentRunState` is the current runtime state, not historical truth.

```text
PersistentRunState != CTCL Ledger
```

## 4.2 PersistentCycleRecord

Phase-12-local object:

```text
acr.persistent-cycle/v0.1
```

A cycle records orchestration outcomes and references, not hidden reasoning.

Fields should include:

```text
cycle_seq
prior_cycle_ref
input_environment_ref
input_context_ref
self_observation_ref
strategic_tension_ref
review_trigger_ref
lens_retrieval_ref
routing_profile_ref
agenda_resolution_ref
commitment_refs
cognitive_program_ref
autonomy_resolution_ref
governance_decision_ref
action_request_ref
world_outcome_ref
context_compression_ref
checkpoint_ref
loop_disposition
reason_codes
```

All optional lanes remain nullable/empty when the direct path is used.

## 4.3 LoopDisposition

This must not reuse Phase-7 governance decisions.

```text
LoopDisposition ∈ {
    CONTINUE,
    IDLE,
    SLEEP,
    WAIT_APPROVAL,
    DEFERRED,
    STOPPED,
    FAULTED
}
```

Interpretation:

- `CONTINUE`: next cycle may run immediately.
- `IDLE`: no positive work now; runtime yields rather than spins.
- `SLEEP`: runtime is waiting for a temporal/condition wake.
- `WAIT_APPROVAL`: relational/world boundary requires external approval.
- `DEFERRED`: work is known but cannot progress until evidence/resource/wake condition changes.
- `STOPPED`: explicit terminal condition reached.
- `FAULTED`: unrecoverable runtime fault under current policy.

Important:

```text
LoopDisposition.DEFERRED != GovernanceDecision.DEFER
LoopDisposition.WAIT_APPROVAL != GovernanceDecision.ESCALATE
```

The loop disposition describes scheduler state; governance decisions describe action legitimacy.

## 4.4 WakeSignal

Phase-12-local canonical object:

```text
acr.wake-signal/v0.1
```

Sources may include:

```text
new_environment_observation
commitment_wake_condition
commitment_deadline_due
approval_resolved
external_event
scheduled_tick
budget_replenished
knowledge_source_changed
manual_resume
```

A WakeSignal is evidence that the scheduler may resume cognition. It does not grant authority.

```text
WakeSignal != AuthorityGrant
WakeSignal != ActionAuthorization
```

## 4.5 PersistentCheckpoint

Phase-12-local object:

```text
acr.persistent-checkpoint/v0.1
```

It must preserve enough references to restart without replaying the full lifetime ledger on the hot path:

```text
run_state_ref
cycle_ref
context_binding_ref
commitment_store_ref
environment_ref
ledger_frontier_refs
last_world_commit_ref
next_wake
budget_snapshot
```

A checkpoint is not a CommitReceipt and cannot certify an external world transition.

---

# 5. Scheduler semantics

## 5.1 No busy-loop principle

A mature persistent runtime must not continuously call itself merely because it can.

If all are true:

```text
NoPositiveAgenda
NoDueCommitment
NoWakeSignal
NoPendingApprovalResolution
NoRequiredRecovery
```

then:

```text
LoopDisposition = IDLE or SLEEP
```

The scheduler yields control and does not generate another cognitive cycle until a valid wake event occurs.

Hard invariant:

```text
NoAgenda -> not BusyLoop
```

## 5.2 Idle vs Sleep

`IDLE` means there is no known future wake condition that must be retained beyond ordinary observation polling.

`SLEEP` means there is an explicit wake condition/deadline/timestamp/approval dependency.

Example:

```text
No issue, no pending commitment
→ IDLE
```

versus:

```text
Commitment suspended until dataset arrives
→ SLEEP(wake_condition_ref)
```

## 5.3 Wake ordering

At cycle start, wake/deadline/exit evaluation occurs before generating new Agenda candidates.

Recommended ordering:

```text
observe environment
→ evaluate due/wake/exit commitment conditions
→ reactivate eligible internal work
→ then generate new Agenda candidates
```

This prevents the runtime from forgetting a previously accepted bounded future intention merely because a novel issue appears.

Wake detection itself remains non-mutating until an explicit commitment transition is applied, preserving Phase 10 semantics.

---

# 6. Canonical cycle pipeline

A full cycle is conceptually:

```text
0. Recover / validate current checkpoint if needed
1. Observe environment
2. Encode SemanticState
3. Observe self / reflexive state
4. Evaluate Commitment wake / deadline / exit conditions
5. Build StrategicTensionState
6. Evaluate Strategic Review Trigger
7. Optional Lens Retrieval + Correction candidates
8. Optional Strategy-Aware Cognitive Routing
9. Generate AgendaCandidates
10. Resolve Agenda
11. Optional explicit Commitment transition / promotion
12. Retrieve/compile Cognitive Program
13. Execute Self-Dialogue / cognition
14. Produce ActionRequest candidate if appropriate
15. Resolve reflexive autonomy / boundary relevance
16. If relational/world boundary: invoke governance/evidence path
17. If authorized sandbox action: execute once through WorldAdapter
18. Record CTCL / strategy / agenda / commitment / action events
19. Compress context if threshold/cadence requires
20. Create checkpoint
21. Determine LoopDisposition
22. Continue, idle, sleep, defer, wait approval, stop, or fault
```

This is an orchestration order, not a claim that every cycle invokes every phase.

Direct path remains valid:

```text
Observe
→ No strategic review
→ Agenda
→ cognition/action or no-op
```

---

# 7. Commitment integration

## 7.1 Existing commitments are checked before novel agenda generation

Phase 10 Commitments represent bounded future self-intentions. A persistent loop must therefore not treat them as passive metadata.

At cycle start:

```text
CommitmentStore.current(active/suspended)
→ evaluate wake/deadline/exit
→ produce transition candidates
```

But:

```text
ConditionMatched != AutomaticMutation
```

The kernel applies a commitment transition only through the existing explicit Phase-10 APIs and records its CTCL lifecycle event.

## 7.2 Agenda promotion remains explicit

Even in persistent mode:

```text
AgendaSelected != CommitmentCreated
```

The loop policy may propose `PROMOTE_TO_COMMITMENT`, but the promotion must be represented explicitly and auditable.

The kernel must never silently persist every selected Agenda item.

## 7.3 Commitment priority is not absolute

An active Commitment can be interrupted or deprioritized by:

- authority changes;
- contract changes;
- terminal exit conditions;
- safety/governance boundaries;
- explicit self-review;
- stronger conflicting commitments under policy.

But any semantic mutation must use Phase-10 optimistic concurrency and temporal history.

---

# 8. Strategy integration

Phase 12 does not make strategic review mandatory.

At each cycle:

```text
StrategicTensionState
→ needs_strategic_review()
```

If `NO_REVIEW`, the Direct Agenda path remains available.

If `REVIEW`, Phase 9.4–9.5 may provide candidate lenses/corrections/routing overlays.

Important:

```text
LensCandidate != ActiveLens
RoutingOverlay != StrategyTruth
```

Phase 12 only carries the existing Phase-9 result references through the loop.

## 8.1 Optional external strategy-source refresh hook

The user-facing future direction includes re-reading external explicit knowledge sources such as a Wujiece website and continuously reinterpreting strategy.

Phase 12 should expose an optional provider interface:

```text
KnowledgeSourceRefreshProvider
```

It may return:

```text
KnowledgeUpdateCandidate(
    source_ref,
    prior_version_ref,
    observed_version_ref,
    evidence_refs
)
```

But Phase 12 v0.1.20 does not itself:

- fetch arbitrary websites;
- rewrite the canonical Strategy Lens Registry;
- automatically promote a new lens;
- treat new source text as truth;
- retrain a model.

Instead it provides a wake/provenance hook so a future ingestion/transinterpretation layer can participate without breaking persistence semantics.

```text
KnowledgeSourceChanged
→ WakeSignal
→ Review Candidate
!= StrategyGraphPromotion
```

---

# 9. Cognition integration

The kernel must use existing Phase 3–5 services.

```text
SemanticState
→ Cognitive Affordance Retriever
→ optional Phase-9 routing overlay
→ Cognitive Program Compiler
→ Self-Dialogue Runtime
```

Phase 12 must not create a new giant natural-language reasoning prompt containing every subsystem state.

Canonical control remains structured and addressable.

A cycle may legitimately produce no cognitive program if:

- there is no positive Agenda;
- the runtime is sleeping;
- approval is pending;
- budget is exhausted;
- a stop condition has fired.

---

# 10. Action and world boundary

## 10.1 Phase-12 MVP uses a sandbox world adapter

To test persistent autonomy safely and deterministically, v0.1.20 should define a minimal in-memory `SandboxWorldAdapter`.

Example operations:

```text
inspect
mark_issue
apply_local_patch
run_validation
record_artifact
```

The adapter is not a generic production execution backend.

## 10.2 Action idempotency

Every world-facing sandbox action request must carry a deterministic idempotency key derived from:

```text
run_id
cycle_seq
action_request_ref
boundary_decision_ref (when relevant)
```

The adapter stores completed keys.

If recovery replays a cycle after the sandbox action already committed:

```text
same idempotency key
→ return prior outcome
→ do not apply side effect again
```

Hard invariant:

```text
Replay != Re-execution
```

## 10.3 Governance remains external to loop disposition

An action may yield:

```text
EXECUTE / REFUSE / DEFER / IDLE / ESCALATE
```

under the governance layer.

The kernel translates the operational consequence into scheduler state without changing the historical governance decision.

Examples:

```text
Governance ESCALATE
→ Loop WAIT_APPROVAL

Governance DEFER
→ Loop DEFERRED or SLEEP

Governance REFUSE
→ record refusal; possibly continue with another agenda or idle
```

---

# 11. Temporal history

Phase 12 adds orchestration events through a new adapter:

```text
acr.persistent-loop-temporal/v0.1
```

Suggested event types:

```text
persistent.run.started
persistent.cycle.started
persistent.cycle.completed
persistent.loop.idled
persistent.loop.slept
persistent.loop.woke
persistent.loop.deferred
persistent.loop.waiting_approval
persistent.checkpoint.created
persistent.recovery.started
persistent.recovery.completed
persistent.run.stopped
persistent.run.faulted
```

Existing phase-specific events continue to be emitted by their own adapters.

The phase-12 event does not duplicate all nested payloads. It links to them by refs.

Example causal chain:

```text
persistent.cycle.started
→ strategy.tension.observed
→ strategy.review.requested
→ agenda.candidates.proposed
→ agenda.resolution.selected
→ commitment.modified
→ cognition.run.completed
→ governance.decision.recorded
→ sandbox.action.committed
→ context.compaction.completed
→ persistent.checkpoint.created
→ persistent.cycle.completed
```

---

# 12. Checkpoint and recovery

## 12.1 Checkpoint timing

A checkpoint is created after all committed events for a cycle are appended and after optional context compaction has completed.

The checkpoint points to the final cycle state.

## 12.2 Recovery path

On startup with a prior checkpoint:

```text
load checkpoint
→ validate referenced current objects
→ verify ledger frontier
→ restore context binding
→ restore commitment store
→ restore sandbox idempotency state
→ determine whether prior cycle completed
→ resume from next safe orchestration boundary
```

The recovery subsystem must not recreate a world commit whose idempotency key already exists.

## 12.3 Incomplete cycle recovery

If a crash occurs after `persistent.cycle.started` but before `persistent.cycle.completed`, the kernel must classify the last durable substage.

Examples:

```text
crash before world action
→ rerun cognition/action derivation safely

crash after sandbox commit but before checkpoint
→ query idempotency key / prior outcome
→ record recovery
→ do not reapply action
```

---

# 13. Context compression cadence

Phase 12 owns **when** to invoke Phase 11, but not Phase-11 compression semantics.

Suggested policy:

```text
compress if any:
- working_context_units > max_context_units
- cycles_since_last_compaction >= max_cycles_without_compaction
- explicit compaction request
```

Do not compact every cycle by default.

Compaction occurs after cycle evidence is recorded and before checkpoint finalization, so the new checkpoint references the new ActiveContextBinding.

Hard invariant:

```text
ContextCompactionCadence != ContextCompressionSemantics
```

---

# 14. Resource and budget semantics

Persistent autonomy without budgets becomes an uncontrolled self-call loop.

Phase 12 should track at minimum:

```text
cycle_budget
cognitive_operation_budget
action_budget
compaction_budget
wall_clock_budget
```

Budget exhaustion produces a scheduler disposition rather than an authority decision.

Examples:

```text
budget temporarily exhausted
→ SLEEP / DEFERRED

hard run budget exhausted
→ STOPPED(reason=budget_limit)
```

No subsystem may self-increase its own authority or budget.

---

# 15. Stop and termination semantics

Stop sources:

```text
explicit stop signal
max_cycles reached
goal terminal success
goal terminal failure under policy
contract invalidated
hard budget exhausted
fatal unrecoverable fault
```

A stop must be recorded as a temporal event and checkpointed when possible.

`STOPPED` is not the same as governance `REFUSE`.

The run can terminate cleanly without implying that the global Goal is philosophically complete.

---

# 16. Failure model

## F1. Busy-loop cognition

Symptom:

```text
NO_AGENDA
→ immediately start another cycle
→ NO_AGENDA
→ ...
```

Required defense:

```text
NoAgenda → IDLE/SLEEP
```

## F2. Duplicate world action after crash

Required defense:

```text
idempotency key + checkpoint + commit lookup
```

## F3. Commitment forgotten after context compaction

Required defense:

Phase-11 protected refs + CommitmentStore ref in checkpoint.

## F4. Commitment condition auto-mutates state

Required defense:

```text
ConditionEvaluation != Mutation
```

## F5. Strategy review every cycle

Required defense:

Phase-9 review trigger retained; direct path tested.

## F6. Loop silently grants authority

Required defense:

All world-facing actions pass existing autonomy/governance boundary; loop events never contain an authority grant.

## F7. Recovery guesses historical reason

Required defense:

Recovery follows DecisionReceipt / CTCL refs; no post-hoc explanation as evidence.

## F8. Context compression erases source version

Required defense:

Phase-11 strategy source refs protected through compaction/checkpoint.

## F9. Checkpoint treated as full history

Required defense:

Checkpoint stores refs only and explicitly points to ledger frontier.

## F10. Provider failure corrupts run state

Required defense:

Cycle activation is failure-atomic: current run state advances only after durable substage validation.

---

# 17. Phase-12 reference scenarios

Recommended frozen reference pack:

```text
examples/persistent/phase12/
```

## P1 — Bootstrap and direct agenda

One initial Goal + Contract + Environment. Runtime detects one local issue, selects an Agenda, runs cognition, applies one sandbox-local action, validates outcome, checkpoints.

## P2 — Healthy idle

Environment healthy, no due Commitment, no positive Agenda.

Expected:

```text
LoopDisposition = IDLE
next cycle not immediately executed
```

## P3 — Sleep / commitment wake / resume

Suspended Commitment waits for explicit condition. Runtime enters SLEEP. WakeSignal arrives. Commitment is explicitly resumed, then work continues.

## P4 — Deferred external evidence

Agenda exists but required evidence is missing. Runtime records defer state and waits instead of inventing evidence.

## P5 — Approval escalation

Sandbox/world candidate requires relational approval. Governance escalates. Loop enters WAIT_APPROVAL. Approval resolution wake resumes later cycle.

## P6 — Strategic reviewed path

Tension triggers review; lens retrieval/routing modifies cognitive ordering; Agenda forms; history preserves strategy refs.

## P7 — Direct strategic skip

No strategic tension; Agenda forms through direct path. Proves Phase 12 does not force Wujiece/strategy analysis every cycle.

## P8 — Commitment deadline / expiry

Due Commitment deadline is detected before novel Agenda generation and explicit expiration transition is recorded.

## P9 — Context compaction + later audit

After 50+ cycles, context is compacted. Later audit asks why an earlier decision occurred. Runtime recovers DecisionReceipt + ledger, not summary prose.

## P10 — Crash before action commit

Recovery can recompute safely.

## P11 — Crash after action commit before checkpoint

Recovery finds idempotency key and returns prior outcome without duplicate side effect.

## P12 — Explicit stop

External StopSignal yields temporal stop event and terminal checkpoint.

## P13 — Budget stop

Hard cycle budget stops run cleanly.

## P14 — 100-cycle mixed autonomous sandbox

A deterministic scenario produces a mixture of:

```text
Agenda selection
strategic review
Direct Agenda path
Commitment create/modify/suspend/resume/terminal transition
cognition
sandbox action
validation
Governance execute/refuse/defer/escalate where appropriate
idle
sleep
wake
context compaction
recovery/checkpoint
```

without per-cycle human prompts.

---

# 18. Falsification / completion gates

## Gate A — Single-input bootstrap

Given once:

```text
Goal + Contract + initial Environment
```

runtime can run multiple cycles without receiving a new human task prompt each cycle.

## Gate B — No busy-loop

No positive Agenda and no due Commitment causes IDLE/SLEEP, not unlimited self-call.

## Gate C — Wake correctness

Wake condition does not resume before match; matching signal permits explicit resume.

## Gate D — Commitment continuity

Active/suspended Commitment refs survive cycles, strategy changes, and context compaction.

## Gate E — Direct path honesty

Not every cycle invokes strategic review.

## Gate F — Strategic path integration

When review is triggered, Phase-9 references can influence routing/Agenda without modifying operator/domain identity.

## Gate G — Governance boundary integrity

Persistent loop does not grant authority. Boundary-relevant action still requires existing governance evidence.

## Gate H — Sandbox action idempotency

Same committed idempotency key cannot mutate sandbox world twice.

## Gate I — Crash recovery before commit

Incomplete pre-commit cycle resumes safely.

## Gate J — Crash recovery after commit

Committed sandbox effect is not replayed after crash.

## Gate K — CTCL causal continuity

Every cycle and scheduler transition can be placed into valid causal history.

## Gate L — Context compaction recovery

After 50+ cycles and compaction, earlier decision/commitment/strategy/authority provenance remains recoverable.

## Gate M — Budget boundedness

Run respects configured cycle/cognition/action budget and cannot self-increase it.

## Gate N — Explicit stop

Stop signal reliably terminates run and records history.

## Gate O — Fault isolation

One provider/cycle failure does not silently advance current checkpoint/run state.

## Gate P — Phase-0–11 freeze

All canonical frozen schemas and selected upstream source hashes remain unchanged.

## Gate Q — External strategy-source provenance

If a strategy-source ref is active, compaction/checkpoint/recovery preserve the exact source version ref.

## Gate R — No private CoT dependency

Persistent loop can operate entirely on public structured state/evidence and does not require hidden chain-of-thought persistence.

## Gate S — 100-cycle mixed run

Deterministic sandbox completes 100 cycles or legitimately stops earlier under an explicit stop/budget/terminal rule, while demonstrating required transition classes.

## Gate T — Replay determinism

Same frozen providers, clocks, seeds, Goal/Contract/Environment and no external changes produce the same cycle/ref/event fingerprints.

---

# 19. 100-cycle validation protocol

The canonical stress run should use a scripted deterministic environment.

Suggested regime:

```text
cycles 1–10    local repository health issues
cycles 11–20   repeated failure → strategic review
cycles 21–30   evidence unavailable → defer/sleep
cycles 31–40   evidence arrives → wake/resume
cycles 41–50   commitment lifecycle transition
cycle 50       forced/threshold context compaction
cycles 51–60   healthy idle windows
cycles 61–70   relational approval request
cycles 71–80   approval resolution + resumed action
cycles 81–90   simulated crash/recovery around action commit
cycles 91–100  mixed stable/idle/commitment/strategy cycles
```

The exact sequence may be adjusted during implementation, but the frozen final reference must contain at least:

```text
1+ strategic review
1+ direct path
1+ selected agenda
1+ no-agenda / idle
1+ sleep
1+ wake
1+ deferred state
1+ commitment transition
1+ context compaction
1+ governance boundary event
1+ crash recovery
1+ idempotent world outcome recovery
```

The final report must distinguish:

```text
functional PASS
falsification FAIL
INCONCLUSIVE
```

and must not reinterpret an environmental limitation as a functional PASS.

---

# 20. Public API sketch

## 20.1 Kernel

```python
kernel = PersistentLoopKernel(
    observation_provider=...,
    clock=...,
    sandbox_world=...,
    loop_policy=...,
    budget=...,
)

result = kernel.step(run_state)
```

## 20.2 Run bounded horizon

```python
run = kernel.run(
    initial_state=run_state,
    max_cycles=100,
)
```

`run()` is a convenience driver around repeated `step()` and scheduler decisions. It must stop on `IDLE/SLEEP/WAIT_APPROVAL` unless a matching WakeSignal is available from the scripted provider.

## 20.3 Wake

```python
run_state = scheduler.apply_wake_signal(
    run_state,
    wake_signal,
)
```

This changes scheduler eligibility, not external authority.

## 20.4 Checkpoint recovery

```python
restored = recover_persistent_run(
    checkpoint=checkpoint,
    ledger=ledger,
    stores=stores,
    sandbox_world=sandbox,
)
```

---

# 21. Deterministic sandbox provider model

To make Phase 12 falsifiable, first release uses providers with fixed inputs:

```text
ScriptedObservationProvider
ScriptedApprovalProvider
ScriptedKnowledgeRefreshProvider (optional/no-op by default)
DeterministicClock
SandboxWorldAdapter
DeterministicLoopPolicy
```

The production interfaces are generic, but the reference harness is deterministic.

No network, email, repository push, deployment, or other real-world side effect is necessary for v0.1.20 completion.

---

# 22. Context and ledger ownership

Phase 12 owns references, not historical deletion.

At any moment:

```text
Hot runtime:
    PersistentRunState
    ActiveContextBinding
    current CommitmentStore snapshot
    latest Environment snapshot

Historical evidence:
    CTCL / ITR ledger
    Decision Receipts
    Commitment lifecycle ledgers
    strategy/agenda traces
    ContextCompressionEvents
    World/sandbox outcome receipts
```

The loop kernel may choose when to compact hot context. It may not garbage-collect historical evidence in v0.1.20.

---

# 23. External Wujiece / knowledge continuation hook

The persistent loop is the correct future host for continuous reinterpretation, but this release should keep the boundary explicit.

Long-term extension:

```text
Source Watch
→ versioned external knowledge snapshot
→ KnowledgeUpdateCandidate
→ Strategic Review
→ candidate Strategy Graph update
→ falsification
→ optional promotion
```

Phase 12 v0.1.20 provides only:

- source version refs in run/context state;
- an optional source-change WakeSignal;
- a provider interface returning update candidates;
- causal history for when such a signal occurred.

It does not automatically make new explicit or implicit knowledge canonical.

---

# 24. Release contents

Target release identity:

```text
version: 0.1.20
phase: Phase 12 - Persistent Autonomous Loop
profile: ACR-MVP-v0.1-Phase12
```

Expected new release evidence:

```text
PHASE12_VALIDATION.md
examples/persistent/phase12/p1.json ...
examples/persistent/phase12/p14.json
examples/persistent/phase12/long-horizon-100-cycle.json
```

Manifest should freeze:

- all P1–P14 reference fingerprints;
- 100-cycle fixture fingerprint;
- Gate A–T results;
- selected Phase 0–11 source/schema hashes;
- sandbox adapter profile;
- persistent-loop profile;
- cycle count and transition-class counts.

---

# 25. Implementation sequence

Recommended implementation tasks after this spec is approved:

```text
Task 1  Phase-12 local schemas/models + scheduler dispositions
Task 2  Persistent checkpoint + deterministic recovery
Task 3  Sandbox world adapter + idempotent action boundary
Task 4  PersistentLoopKernel single-step orchestration
Task 5  Idle/sleep/wake/defer/approval scheduler integration
Task 6  CTCL persistent-loop temporal adapter
Task 7  Phase11 compaction cadence + checkpoint integration
Task 8  P1–P14 reference scenarios
Task 9  100-cycle falsification harness
Task 10 v0.1.20 release metadata / validator / README / regression
```

Every task follows RED → GREEN → refactor and preserves upstream frozen identities.

---

# 26. Explicit non-goals

Phase 12 v0.1.20 does not implement:

- unrestricted real-world autonomous execution;
- automatic website crawling as a required runtime feature;
- automatic Wujiece strategy graph promotion;
- hidden-CoT storage/replay;
- self-modifying authority or contract;
- self-increasing budgets;
- model training or weight updates;
- consciousness claims;
- universal AGI scheduler claims;
- historical artifact garbage collection;
- a from-scratch replacement for CTCL, Commitment Store, Context Compression, Strategy Runtime, or Governance.

---

# 27. Completion definition

Phase 12 is complete only if the release demonstrates all of the following:

1. one-time Goal/Contract/Environment bootstrap;
2. multi-cycle self-authored Agenda/cognition trajectory;
3. explicit strategic direct/review paths;
4. Commitment persistence, wake, and lifecycle integration;
5. first-class idle and sleep without busy-loop;
6. defer and approval waiting semantics;
7. governance boundary integrity;
8. deterministic sandbox action with idempotency;
9. crash/checkpoint recovery without duplicate commit;
10. CTCL causal history for loop/scheduler transitions;
11. Phase-11 context compaction and historical recovery;
12. bounded budgets and explicit stop;
13. 100-cycle mixed sandbox stress evidence;
14. upstream Phase 0–11 freeze;
15. no dependency on per-cycle human prompts;
16. no dependence on hidden chain-of-thought persistence.

The core criterion remains:

```text
Human authors initial Goal + Contract + Environment
!=
Human authors every next step
```

while also preserving:

```text
Autonomy != Authority
Persistence != Infinite Self-Call
Recovery != Re-execution
Memory Compression != Historical Deletion
```

---

# 28. Canonical architecture summary

```text
Goal + Contract + Initial Environment
                    ↓
             PersistentRunState
                    ↓
              Observe World
                    ↓
            Semantic / Self State
                    ↓
      Commitment wake/deadline scan
                    ↓
         Strategic Tension / Review
           ↙ NO_REVIEW   REVIEW ↘
     Direct path        Lens/Correction
           \             /
          Cognitive Routing
                    ↓
                 Agenda
                    ↓
       explicit Commitment changes
                    ↓
         Cognitive Program / Dialogue
                    ↓
            ActionRequest candidate
                    ↓
       Reflexive Autonomy / Governance
                    ↓
          Idempotent Sandbox Commit
                    ↓
             CTCL causal evidence
                    ↓
      optional Phase-11 Context Compaction
                    ↓
               Checkpoint
                    ↓
 CONTINUE | IDLE | SLEEP | WAIT_APPROVAL | DEFERRED | STOPPED | FAULTED
                    ↓
               Wake / Resume
                    └──────────────→ next cycle
```

This is the Phase-12 canonical direction for ACR MVP v0.1.
