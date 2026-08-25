# Phase 12 Persistent Autonomous Loop — Design Validation

**Design target:** ACR MVP `0.1.20`  
**Phase:** `Phase 12 - Persistent Autonomous Loop`  
**Profile target:** `ACR-MVP-v0.1-Phase12`  
**Date:** 2026-08-25

## 1. Architecture gate

Phase 12 is classified as an architectural subsystem. This pack contains only the design specification and validation evidence. No Phase-12 runtime production code is implemented in this design gate.

Selected architecture:

```text
Persistent orchestration kernel
+ explicit current run/cycle state
+ frozen Phase 0-11 subsystem APIs
+ CTCL append-only history
+ first-class Idle/Sleep/Wake/Defer/Approval states
+ checkpoint/recovery
+ deterministic sandbox world adapter
```

Rejected as defaults:

1. monolithic mega-agent loop;
2. full lifetime-ledger replay on every hot cycle.

## 2. Upstream release basis

Imported baseline:

```text
version = 0.1.19
phase   = Phase 11 - Context Compression
profile = ACR-MVP-v0.1-Phase11
```

Phase-11 baseline evidence retained in the source workspace:

```text
phase11 reference count       = 12
phase11 long-horizon cycles   = 64
phase11 Gate A-P              = all true
```

The design preserves the Phase-11 principle that working context is not the historical ledger and that context compaction may not erase causal provenance.

## 3. Design self-review

```text
lines                     = 1447
characters                = 34498
TBD                       = 0
TODO                      = 0
implement later           = 0
fill in details           = 0
Gate A-T present          = true
P1-P14 present            = true
target version 0.1.20     = true
LoopDisposition names     = internally consistent
Replay/Re-execution split = explicit
Idle/no-busy-loop gate    = explicit
100-cycle protocol        = explicit
```

## 4. Canonical Phase-12 invariants

The design explicitly preserves at least:

```text
PersistentLoop != AutonomousWorldAuthority
CycleState != HistoricalLedger
LoopDisposition != GovernanceDecision
WakeConditionMatched != AutomaticExternalAction
Idle != Failure
NoAgenda != Error
Sleeping != Stopped
Deferred != Refused
Checkpoint != CommitReceipt
Replay != Re-execution
Recovery != Reenactment
ActionRequest != WorldCommit
LoopIteration != HumanPrompt
BudgetExhaustion != GoalFailure
KnowledgeRefreshCandidate != StrategyGraphPromotion
```

## 5. Reference and falsification plan

Frozen implementation targets are defined for:

```text
P1-P14 reference scenarios
Gate A-T
100-cycle mixed deterministic sandbox run
crash before commit
crash after commit before checkpoint
idempotent replay
Idle/Sleep/Wake
Commitment continuity
Strategic direct/review paths
Governance boundary integrity
Phase-11 context compaction/recovery
external strategy-source provenance
no hidden-CoT dependency
```

## 6. External knowledge / Wujiece continuation boundary

The design reserves an optional `KnowledgeSourceRefreshProvider` and source-change WakeSignal so a future Wujiece / explicit-knowledge reinterpretation layer can participate in the persistent loop.

Phase 12 v0.1.20 does **not** automatically fetch websites, promote new lenses, certify new source text as truth, or rewrite the Strategy Lens Registry.

## 7. Git evidence

```text
branch = phase12-persistent-autonomous-loop-design
commit = f345023f0b29d5cac123f20e0efb37361eb81b2d
```

## 8. Artifact integrity

```text
design_sha256 = 5c5575819ef5fa7bf62a22da99a853ba2d5d9cf4702f3348a78c67fecd620479
```

## 9. Gate result

```text
DESIGN_VALIDATION = PASS
IMPLEMENTATION     = NOT_STARTED_BY_DESIGN_GATE
NEXT               = written spec approval -> implementation plan -> TDD
```
