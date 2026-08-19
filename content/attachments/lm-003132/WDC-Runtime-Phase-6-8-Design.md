# WDC Runtime Phase 6–8 Design

## Scope

Implement only the next three approved MVP layers on top of the verified Phase 0–5 base:

1. **Phase 6 — Computation Portfolio Kernel**
2. **Phase 7 — Reality Commit Gate / External Boundary**
3. **Phase 8 — TCD Integration / History Firewall**

Neural learners, distributed schedulers, uncontrolled external tools, and production deployment remain out of scope.

## Architecture

### Portfolio layer

Create `wdc.portfolio` as a pure metareasoning layer over existing evidence state. It defines `ComputationOperation`, `EpistemicDeficit`, `ComputationAction`, and a deterministic `DeficitRouter`. It proposes *next computations* but does not allocate resources or execute worlds; the existing `WorldGovernor` remains the lifecycle/budget authority.

### Commit layer

Create `wdc.commit` as the only normal bridge from parent-internal WDC evidence to controlled external/sandbox action. `CommitGate.assess()` must consider authority, evidence presence, transport debt, unresolved counterexamples, unknown-world mass, and requested action risk. Approval creates an immutable `CommitRecord`; execution through an `ExternalToolProxy` requires that record.

### TCD layer

Create `wdc.tcd` with versioned `TCDStateVersion`, `FutureCandidate`, `TCDDelta`, and `SedimentationRecord`. World evidence may update future candidate value/probability, current action valuation, and past *relevance*; it may not mutate parent-real historical facts. Only explicit parent-real/sandbox action and observed outcome can advance `parent_time` and produce the next sedimented TCD state.

## Data flow

```text
EvidenceAggregate
  -> EpistemicDeficit
  -> DeficitRouter
  -> ComputationAction proposals

EvidenceAggregate + Authority + Action
  -> CommitProposal
  -> CommitGate
  -> CommitRecord
  -> ExternalToolProxy controlled action
  -> RealOutcome

TCDState_t + WorldEvidence
  -> TCDDelta (same parent_time)
  -> Commit + RealOutcome
  -> SedimentationRecord
  -> TCDState_{t+1}
```

## Hard invariants

- `Worth Computing != Worth Believing != Worth Deploying`.
- `ComputationAction` is a proposal; it does not allocate or execute by itself.
- Cross-world consensus never bypasses `CommitGate`.
- `APPROVE` requires sufficient declared authority for the requested sandbox/external operation.
- World-local evidence cannot mutate `past_facts`.
- World evidence may change `past_relevance` only.
- `parent_time` remains unchanged during evidence assimilation and increments only on explicit sedimentation of a parent-real/sandbox transition.
- `RealAction` requires a persisted approved `CommitRecord`.
- Unknown-world mass and transport debt are carried into the commit record, not erased.

## Error handling

Typed domain errors:

- `UnknownComputationTarget`
- `CommitDenied`
- `AuthorityInsufficient`
- `HistoryFirewallViolation`
- `TCDVersionConflict`

No silent fallback may convert a denied commit into an approved external action.

## Testing

Use TDD for each layer. Minimum new behaviors:

- deficit routing maps each dominant deficit to the intended computation operation;
- redundant same-family evidence suppresses independence-oriented run-more proposals and favors `CROSS_BACKEND`;
- high transport debt routes `CALIBRATE`;
- commit approval fails without authority even when all worlds agree;
- approved commit is required for the controlled proxy;
- world evidence changes future/present/past relevance but never historical facts;
- sedimentation advances `parent_time` exactly once and records real/sandbox outcome;
- integration demo closes `Future -> World Evidence -> Computation/Commit -> Sandbox Outcome -> New TCD State`.
