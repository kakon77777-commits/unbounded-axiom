# Phase 12 Unified Implementation Sequence

**目標：** 在不修改 Phase 0–11 frozen semantics 的前提下，把 ACE／DRS／WPCE 接進 Phase 12 persistent orchestration。

## Milestone 0 — Freeze & Baseline

- Verify Phase 10 source hashes.
- Verify Phase 11 reference pack and canonical validator.
- Run current Phase 12 design validation.
- Record baseline test count and environment limitations.

**Exit:** upstream identities captured; no mutation.

## Milestone 1 — Integration Models Only

新增 Phase-12-local / integration-local models，不先接 provider：

```text
integration/autonomy.py
integration/sealing.py
integration/will.py
integration/intervention.py
```

候選物件：

- `CandidateAutonomyEvent`
- `SealState` / `SealTransition`
- `RestoreAnchor`
- `GovernanceWillState`
- `ReachabilityAssessment`
- `InterventionAssessment`
- `LeastSufficientInterventionChoice`

**Exit:** pure-model deterministic unit tests green.

## Milestone 2 — DRS Access View

新增：

```text
ContextCapsule
+ SealState
+ mandatory refs
→ ActiveCognitiveDomain
```

要求：

- no source deletion;
- protected refs remain recoverable;
- closure creep rejected;
- restart-safe restore anchors.

**Exit:** U-E/U-F/U-G green.

## Milestone 3 — ACE Passive Archive

把 ACE observer 接在 normal cognition / action candidate 之後，治理前只做 evidence archival。

要求：

- no ACE prompt injection;
- no praise/reward;
- no authority mutation;
- no private-CoT storage;
- contamination metadata.

**Exit:** U-B/U-C/U-D green.

## Milestone 4 — Will-Governance State

把 consent/refusal/revocation/meta-will/uncertainty 接為 versioned evidence refs。

優先只實作：

- current state projection;
- provenance;
- refusal/revocation effect on admissible actions;
- commitment conflict review.

**Exit:** U-I/U-J/U-K green.

## Milestone 5 — Reachability / Rights Boundary

先做 typed diagnostic，不做假精確 optimizer：

```text
AgencyImpact
RightsFloor
Reversibility
ExitImpact
CrossSubjectRisk
CommonReachabilityStatus
```

允許狀態：

```text
PASS
FAIL
INCOMPARABLE
EMPTY_COMMON_DOMAIN
UNKNOWN
```

**Exit:** U-L/U-M/U-N green.

## Milestone 6 — Intervention Burden + LSI

在 world adapter 前增加：

```text
ActionRequest
→ InterventionAssessment
→ candidate interventions
→ LSI comparator
→ GovernanceDecision
→ authorized WorldAdapter
```

先用 deterministic ordinal rules，不宣稱 universal ethical scalar。

**Exit:** U-O/U-P green.

## Milestone 7 — Emergency / Authority Return

實作 break-glass typed path 與 expiry/review/authority-return event。

**Exit:** U-Q green.

## Milestone 8 — Temporal Adapters & Recovery

新增事件族並接 checkpoint frontier：

- autonomy evidence;
- sealing;
- will governance;
- intervention assessment;
- authority return.

確保 recovery 只靠 durable refs。

**Exit:** U-R/U-S/U-T green.

## Milestone 9 — Context Compression Cross-Layer Test

Phase 11 compaction 必須保留：

- restore anchor;
- active seal state;
- ACE archive refs;
- current will-governance refs;
- intervention/governance decision refs。

**Exit:** U-H green.

## Milestone 10 — 100-Cycle Unified Harness

建立 deterministic mixed run：

- direct agenda cycles;
- idle/sleep/wake;
- commitment due/review;
- DRS seal/unseal;
- quiet ACE candidate;
- contaminated false positive;
- refusal/revocation;
- multi-subject conflict;
- LSI action;
- emergency rescue + authority return;
- context compaction;
- crash before/after world commit;
- explicit stop.

**Exit:** U-U green + all original Phase-12 gates green.

## Milestone 11 — Release Commit

只有在：

```text
original Phase 12 gates = all green
unified U-A ... U-U = all green
upstream hashes unchanged
UTF-8 validation = PASS
canonical delimiter validation = PASS
source manifest = complete
```

才建立 implementation release。
