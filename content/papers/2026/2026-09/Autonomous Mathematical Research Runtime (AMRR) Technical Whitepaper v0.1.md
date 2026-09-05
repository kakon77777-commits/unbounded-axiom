# Autonomous Mathematical Research Runtime (AMRR) Technical Whitepaper v0.1

## ——從 Addressable Cognitive Runtime 到可診斷、可修復、可驗證、可追溯的自主數學研究系統

**文件類型：技術白皮書 / Canonical Engineering Specification**  
**版本：v0.1**  
**日期：2026-08-23**  
**作者：Neo.K**  
**系列：Autonomous Mathematical Research**

---

# 0. 文件定位

本文是 Autonomous Mathematical Research 系列四篇論文的第一版**統一工程母文件**。

四篇理論文件分別完成：

1. 從數學解題到自主數學研究的總體框架；
2. Multi-Domain Mathematical Diagnosis 與 CMDC；
3. Problem Identity、Theory Extension 與 Mathematical Obligations；
4. AMRR 的 executable architecture。

本文不再主要證成上述理論，而是固定：

```text
canonical schemas
module boundaries
runtime state
API surface
math cognitive registry
problem / theory stores
gap / repair / obligation engines
verifier routing
research contract
CTCL events / receipts
persistent research loop
phase dependencies
MVP scope
falsification gates
```

本文的直接工程目標是：

> **在既有 Addressable Cognitive Runtime Phase 0–2 基線之上，以可增量整合的方式建立 Autonomous Mathematical Research Runtime，而不是重寫一套平行 Agent。**

---

# 1. 一句話架構

$$
\boxed{
AMRR
=
ACR
+
MathematicalState
+
DomainDiagnosis
+
CMDC
+
ObligationEngine
+
VerifierRouter
+
TheoryBridge
+
CTCL\text{-}ITR
}
$$

其中 ACR 提供通用自主認知 Runtime，AMRR 提供數學研究 domain semantics。

最終 persistent input 是：

$$
\boxed{
ResearchGoal
+
ResearchEnvironment
+
ResearchContract
}
$$

而不是逐輪：

$$
HumanPrompt_t
\rightarrow
AIResponse_t.
$$

---

# 2. 現有工程基線

AMRR v0.1 明確以既有 ACR 工程為 substrate。

目前可視為 implemented baseline 的部分：

```text
ACR Phase 0 — Schema Freeze
ACR Phase 1 — SPRC / CIO Adapter
ACR Phase 2 — Semantic State Encoder
```

現有 Phase 2 release evidence：

```text
package version: 0.1.2
Phase 0 schema count: 10
Phase 1 CognitiveObject count: 64
Semantic State Encoder profile: acr.semantic-state-encoder/v0.1
release pytest: 73 passed
compileall: PASS
release validator: ok=true
```

Phase 2 的重要邊界：

```text
- strict public runtime observations only
- deterministic normalization
- stable SemanticState fingerprint
- no model call
- no embeddings
- no Phase 3 cognition retrieval
- no CTCL event emission
- no hidden/private chain-of-thought ingestion
```

因此 AMRR 不應破壞 Phase 2 deterministic public-state semantics。

## 2.1 Engineering Status Boundary

**Implemented Baseline**：

```text
ACR Phase 0 — Schema Freeze
ACR Phase 1 — SPRC / CIO Adapter
ACR Phase 2 — Semantic State Encoder
```

**AMRR Proposed Extension**：

```text
M0 Math Schema Freeze
M1 Mathematical State Adapter
M2 Problem / Theory Stores
M3 Gap Diagnosis Engine
M4 Problem Identity + Theory Extension
M5 Obligation Engine
M6 Math Cognitive Registry
M7 Verifier Router
M8 CMDC Repair Engine
M9 Theory Bridge / Prior Art
M10 CTCL / Receipt Adapter
M11 Persistent Research Loop
```

本文所有 M0–M11 描述均屬 specification / proposed implementation；除非後續 release artifact 明確通過對應 gate，否則不得回寫為 implemented capability。

---

# 3. AMRR v0.1 不變量

以下規則視為 architecture invariants。

$$
\boxed{
Integrate
>
Rewrite.
}
$$

$$
\boxed{
CanonicalState
\neq
RenderedText.
}
$$

$$
\boxed{
Problem
\neq
Theory
\neq
Claim
\neq
Proof.
}
$$

$$
\boxed{
Diagnosis
\neq
Repair
\neq
Verification.
}
$$

$$
\boxed{
RepairCandidate
\neq
AcceptedMutation.
}
$$

$$
\boxed{
GenealogicalContinuity
\not\Rightarrow
SemanticEquivalence.
}
$$

$$
\boxed{
T+A\vdash Q
\not\Rightarrow
T\vdash Q.
}
$$

$$
\boxed{
ProofFound
\neq
ClaimApproved.
}
$$

$$
\boxed{
WAIVED
\neq
DISCHARGED.
}
$$

$$
\boxed{
ClaimScope
\not>
VerifiedScope.
}
$$

$$
\boxed{
WorkingContext
\neq
ResearchLedger.
}
$$

$$
\boxed{
SubmissionReady
\not\Rightarrow
CommunityAccepted.
}
$$

---

# 4. 五層邏輯架構

AMRR 分成五個 logical layers。

```text
Layer A — Mathematical State & Knowledge
Layer B — Cognitive Research Runtime
Layer C — Mutation / Obligation / Verification
Layer D — Governance & Research Contract
Layer E — Temporal-Causal Evidence & Audit
```

## 4.1 Layer A — Mathematical State & Knowledge

回答：

> **現在的數學研究狀態是什麼？**

核心：

```text
MathematicalState
ProblemStore
TheoryStore
DefinitionStore
AssumptionEnvelope
ClaimStore
MethodStore
GapMap
ObligationGraph
BridgeGraph
```

## 4.2 Layer B — Cognitive Research Runtime

回答：

> **下一步應該怎麼研究？**

核心：

```text
Math Affordance Retriever
Math Cognitive Router
Research Program Compiler
Research Program Executor
Agenda Runtime
Re-observer
```

## 4.3 Layer C — Mutation / Obligation / Verification

回答：

> **這項數學變更是否足以合法進入新 research state？**

核心：

```text
Gap Diagnosis Engine
CMDC Repair Engine
Problem Identity Resolver
Theory Extension Classifier
Mathematical Obligation Engine
Verifier Router
Verifier Adapters
Promotion Engine
```

## 4.4 Layer D — Governance & Research Contract

回答：

> **AI 是否被授權採用、升格、公開或停止這項研究行動？**

保持：

$$
Decision
\in
\{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE
\}.
$$

## 4.5 Layer E — Temporal-Causal Evidence & Audit

回答：

> **這個結果是如何產生的？哪個問題版本、哪個理論版本、哪些假設、哪些 verifier 與哪些決策導致現在的 claim？**

核心：

```text
CTCL instant
TemporalEvent
DecisionReceipt
DiagnosisReceipt
RepairReceipt
ProblemMutationReceipt
TheoryExtensionReceipt
ObligationReceipt
VerificationReceipt
GapClosureReceipt
DiscoveryReceipt
ResearchReceipt
```

---

# 5. Canonical Object Catalog

AMRR v0.1 第一批 canonical objects：

```text
MathematicalStateExtension
ProblemRecord
ProblemRelation
ProblemMutation
TheoryRecord
TheoryExtension
DefinitionRecord
AssumptionRecord
AssumptionEnvelope
MethodRecord
ClaimRecord
GapRecord
GapMap
RepairCandidate
MathChangeSet
MathematicalObligation
ObligationGraph
VerificationRequest
VerificationReceipt
TheoryBridge
DiscoveryReceipt
DiagnosisReceipt
RepairReceipt
GapClosureReceipt
ResearchReceipt
```

它們全部必須：

```text
versioned
schema-validatable
canonical-serializable
addressable
hashable
referenceable
ledger-compatible
```

---

# 6. Identity 規則

每個 canonical object 的 identity 不只靠 display name。

定義：

$$
Identity(X)
=
(namespace,id,version,schemaHash).
$$

例如：

```text
problem://amrr/demo/001@3#sha256:...
theory://amrr/demo/base@4#sha256:...
gap://definition/017@1#sha256:...
obligation://semantic-faithfulness/204@1#sha256:...
```

保持：

$$
Name(X)
\neq
Identity(X).
$$

---

# 7. Schema 規則

所有 AMRR schema 必須：

```text
additionalProperties = false
explicit schema_version
explicit object identity
no hidden implicit fields
strict enum where semantics are frozen
extension fields only under explicit namespace
stable canonicalization rules
```

數學 domain extension 應使用：

```text
extensions.math
```

而不是污染既有 ACR top-level SemanticState schema。

---

# 8. MathematicalState Extension

AMRR 不取代 ACR SemanticState。

$$
\boxed{
MathematicalState_t
=
Extend(
SemanticState_t,
MathExtension_t
).
}
$$

v0.1 建議結構：

```json
{
  "extensions": {
    "math": {
      "active_problem_ref": null,
      "problem_refs": [],
      "active_theory_ref": null,
      "theory_refs": [],
      "definition_refs": [],
      "assumption_refs": [],
      "method_refs": [],
      "claim_refs": [],
      "gap_map_ref": null,
      "open_obligation_refs": [],
      "verification_refs": [],
      "bridge_refs": [],
      "novelty_state": "unknown",
      "research_phase": "diagnosis"
    }
  }
}
```

---

# 9. MathematicalState canonicalization

State fingerprint：

$$
Fingerprint(S_t^M)
=
SHA256(CanonicalSerialize(S_t^M)).
$$

需滿足：

$$
EquivalentPublicResearchObservation
\rightarrow
ByteIdenticalMathematicalState.
$$

set-like refs 必須排序與去重。

禁止使用：

```text
private_chain_of_thought
hidden_chain_of_thought
reasoning_tokens
```

作為 canonical state source。

---

# 10. ProblemStore

ProblemRecord v0.1：

```json
{
  "problem_id": "problem:...",
  "version": 3,
  "parent_refs": [],
  "canonical_statement_ref": "artifact:...",
  "informal_statement_ref": "artifact:...",
  "formal_statement_refs": [],
  "domain_refs": [],
  "success_criteria": [],
  "status": "active",
  "created_from_gap_ref": null,
  "relation_to_parent": null,
  "assumption_envelope_ref": "assumption-envelope:..."
}
```

ProblemStore 不允許：

```text
silent overwrite
in-place semantic mutation without version
branch without parent refs
claiming equivalence without relation status
```

---

# 11. Problem DAG

問題演化：

$$
G_P
=
(V_P,E_P).
$$

edge：

$$
P_i
\xrightarrow{r}
P_j.
$$

第一版 relation vocabulary：

```text
equivalent
clarification
restriction
generalization
weakening
strengthening
added_assumption
removed_assumption
reparameterization
representation_change
reinterpretation
new_problem
```

若 relation 尚未驗證：

```text
relation_status = candidate
```

不得直接當成：

```text
verified_relation
```

---

# 12. ProblemIdentity Resolver

API：

```text
problem.relate(before_ref, after_ref)
```

輸出：

```json
{
  "relation": "restriction",
  "confidence": 0.93,
  "evidence_refs": [],
  "verification_status": "candidate"
}
```

其 role 不是決定最終哲學身份，而是產生可驗證 relation candidate。

---

# 13. TheoryStore

TheoryRecord v0.1：

```json
{
  "theory_id": "theory:...",
  "version": 4,
  "parent_refs": [],
  "signature_refs": [],
  "axiom_refs": [],
  "definition_refs": [],
  "theorem_refs": [],
  "method_refs": [],
  "bridge_refs": [],
  "open_obligation_refs": [],
  "extension_profile_ref": null
}
```

保持：

$$
TheoryState
\neq
PaperText.
$$

---

# 14. TheoryExtension

TheoryExtension 應保存：

```text
source_theory_ref
target_theory_candidate_ref
added_symbols
added_definitions
added_axioms
removed_items
changed_semantics
extension_profile
obligation_refs
verification_status
promotion_status
```

Extension Profile：

$$
ExtensionProfile
=
(
LanguageChange,
SemanticChange,
ProofStrengthChange,
ModelChange,
FoundationChange
).
$$

---

# 15. Theory Extension Classes

第一版 class：

```text
documentary_extension
notation_alias_extension
definitional_extension
conservative_extension
derived_theorem_registration
assumption_extension
nonconservative_axiom_extension
foundation_change
unknown_extension
```

系統必須允許：

```text
unknown_extension
```

而不是強迫模型假裝已分類。

---

# 16. AssumptionEnvelope

對任一 claim $C$：

$$
AE(C)
=
DependencyClosure(C)
\cap
Assumptions.
$$

AssumptionEnvelope v0.1：

```json
{
  "assumption_envelope_id": "ae:...",
  "subject_ref": "claim:...",
  "explicit_assumption_refs": [],
  "inherited_assumption_refs": [],
  "theory_ref": "theory:...",
  "dependency_refs": [],
  "computed_at": "...",
  "status": "current"
}
```

任何 public claim 都必須引用最新 envelope。

---

# 17. No Mathematical Laundering Gate

若：

$$
T+A\vdash Q,
$$

禁止 summary 成：

$$
T\vdash Q.
$$

AMRR claim gate 至少檢查：

$$
ClaimAssumptions(C)
\supseteq
AE(C).
$$

以及：

$$
ClaimScope(C)
\subseteq
VerifiedScope(C).
$$

不成立：

```text
claim_status = blocked
reason_code = assumption_laundering
```

或：

```text
reason_code = scope_overclaim
```

---

# 18. GapRecord

GapRecord：

```json
{
  "gap_id": "gap:...",
  "domain": "definition",
  "target_ref": "definition:...",
  "evidence_refs": [],
  "confidence": 0.91,
  "severity": "high",
  "blocking": true,
  "candidate_repair_classes": [],
  "depends_on": [],
  "status": "open"
}
```

第一版 domain enum：

```text
problem
definition
assumption
judgment
representation
solution
method
lemma_dependency
compute
evidence_counterexample
verification_faithfulness
bridge
novelty_interestingness
```

---

# 19. GapMap

$$
G_\Delta
=
(V_\Delta,E_\Delta).
$$

GapMap：

```json
{
  "gap_map_id": "gap-map:...",
  "state_ref": "state:...",
  "gaps": [],
  "roots": [],
  "blocking_gap_refs": [],
  "generated_at": "..."
}
```

Gap dependency example：

$$
DefinitionGap
\rightarrow
FormalizationGap
\rightarrow
ProofGap.
$$

---

# 20. Gap Diagnosis Engine

第一版不得追求全神經化。

建議：

$$
Diagnosis
=
RuleEvidence
+
ToolEvidence
+
ModelClassification
+
CrossCheck.
$$

資料源：

```text
formalizer errors
proof assistant diagnostics
counterexamples
failed method history
missing symbols
ambiguous definitions
problem relation evidence
verification receipts
prior-art refs
budget exhaustion
human review annotations
```

---

# 21. Gap Diagnosis API

```text
gap.diagnose(state_ref, evidence_refs) -> GapMap
gap.get(gap_ref) -> GapRecord
gap.close(gap_ref, closure_receipt_ref)
gap.reopen(gap_ref, evidence_refs)
```

重要：

$$
Diagnosis
\neq
Truth.
$$

所以 GapRecord 必須保存 confidence 與 evidence。

---

# 22. Gap Prioritization

可先採 vector score：

$$
Priority(\delta_i)
=
(
Blocking,
Severity,
Confidence,
ExpectedGain,
RepairCost,
DependencyCentrality
).
$$

初期不要把它過早壓成單一 reward。

---

# 23. RepairCandidate

```json
{
  "repair_candidate_id": "repair:...",
  "gap_ref": "gap:...",
  "repair_type": "definition_repair",
  "target_ref": "definition:...",
  "preconditions": [],
  "mutation_ref": "math-change:...",
  "expected_effects": [],
  "risk_class": "medium",
  "obligation_refs": [],
  "status": "candidate"
}
```

保持：

$$
RepairCandidate
\neq
AcceptedMutation.
$$

---

# 24. Repair classes

第一版：

```text
problem_clarification
definition_repair
assumption_repair
criterion_repair
representation_repair
solution_space_repair
method_repair
lemma_theory_repair
compute_repair
evidence_repair
verification_repair
bridge_repair
novelty_assessment_repair
```

---

# 25. RepairContract

每一 repair class 應有 policy：

$$
RC(r)
=
(
AllowedMutation,
ForbiddenMutation,
RequiredEvidence,
RequiredObligations,
RollbackPolicy,
PromotionPolicy
).
$$

例如 assumption repair：

```text
allowed:
- propose assumption candidate
- branch problem
- update assumption envelope candidate

forbidden:
- overwrite original problem
- erase old assumption state
- claim unrestricted result
```

---

# 26. MathChangeSet

```json
{
  "change_set_id": "math-change:...",
  "source_state_ref": "state:...",
  "gap_ref": "gap:...",
  "change_type": "add_assumption",
  "target_ref": "problem:...",
  "before_ref": "problem:v3",
  "after_candidate_ref": "problem:v4-candidate",
  "reason_codes": [],
  "obligation_refs": [],
  "verification_status": "pending",
  "promotion_status": "candidate"
}
```

任何變更只能先形成 candidate state。

---

# 27. Mathematical Obligation

$$
O_i
=
(
Claim,
Trigger,
RequiredEvidence,
VerifierClass,
Status,
DependsOn
).
$$

第一版 classes：

```text
well_formedness
semantic_faithfulness
problem_identity
conservativity
consistency_relative_consistency
model_existence
independence
bridge
scope_validity
verification
novelty_assessment
provenance
```

---

# 28. ObligationEngine

API：

```text
obligation.generate(change_set_ref)
obligation.get(obligation_ref)
obligation.discharge(obligation_ref, evidence_refs)
obligation.defer(obligation_ref, wake_condition)
obligation.waive(obligation_ref, authority_ref)
obligation.reopen(obligation_ref, evidence_refs)
```

Status：

$$
OPEN
\rightarrow
PARTIAL
\rightarrow
DISCHARGED.
$$

也可：

$$
OPEN
\rightarrow
FAILED,
$$

或：

$$
OPEN
\rightarrow
WAIVED.
$$

但：

$$
WAIVED
\neq
DISCHARGED.
$$

---

# 29. ObligationGraph

$$
G_O
=
(V_O,E_O).
$$

例如：

$$
SemanticFaithfulness
\rightarrow
ClaimScopeValidation.
$$

若 upstream obligation 未解除，下游 claim 不應把它遺失。

保持：

$$
DownstreamSuccess
\not\Rightarrow
UpstreamObligationsDisappear.
$$

---

# 30. Math Cognitive Registry

第一版建議 20 個 operator：

```text
cog://math/interpret@1
cog://math/formalize@1
cog://math/diagnose-gap@1
cog://math/clarify-problem@1
cog://math/define@1
cog://math/add-assumption-candidate@1
cog://math/change-representation@1
cog://math/generate-lemma@1
cog://math/generate-conjecture@1
cog://math/search-counterexample@1
cog://math/retrieve-method@1
cog://math/generate-method@1
cog://math/prove@1
cog://math/disprove@1
cog://math/check-conservativity@1
cog://math/verify-faithfulness@1
cog://math/bridge-theory@1
cog://math/check-prior-art@1
cog://math/discharge-obligation@1
cog://math/package-theory@1
```

---

# 31. Math Cognitive Object extension

既有 CognitiveObject 可加入 math-specific metadata：

```json
{
  "math_domains": ["definition", "verification"],
  "accepted_gap_classes": [],
  "produces_candidate_types": [],
  "obligation_effects": [],
  "required_verifier_classes": []
}
```

但 canonical identity 仍沿用 ACR：

$$
(namespace,id,version,schemaHash).
$$

---

# 32. Math Affordance Retrieval

$$
\mathcal A_M
=
Retrieve(
S_t^M,
\Delta_t,
G_t,
C_t
).
$$

score：

$$
Score(\Omega_i)
=
w_gGapFit
+
w_pPreconditionFit
+
w_hHistoricalUtility
+
w_oObligationReduction
-
w_cCost
-
w_rRisk.
$$

第一版可以：

```text
rule filtering
+ domain tags
+ preconditions
+ historical utility
+ optional BM25 / vector similarity
```

---

# 33. Research Program Compiler

$$
Compiler_M(
S_t^M,
\Delta_t,
G_t,
C_t,
\mathcal A_M
)
\rightarrow
P_t^M.
$$

Program 必須保存：

```text
operator order
parameters
budget
termination
fallback
required_verifiers
allowed_mutations
```

---

# 34. Program Validation

執行前：

$$
TypeCheck
\land
ScopeCheck
\land
AuthorityCheck
\land
BudgetCheck
\land
ProblemIdentityCheck
\land
InvariantCheck.
$$

若 fail：

```text
ProgramRejected
```

而不是嘗試自由文字 fallback 後偷偷執行。

---

# 35. VerifierRouter

$$
VerifierRouter(
Claim,
Obligation,
TheoryState
)
\rightarrow
\{V_1,\ldots,V_k\}.
$$

第一版 verifier classes：

```text
formal_proof
symbolic_algebra
sat
smt
numeric
exhaustive_search
simulation
semantic_equivalence
literature_prior_art
human_review
```

---

# 36. Verifier Adapter Interface

統一 interface：

```text
verify(request) -> VerificationResult
```

VerificationResult：

```text
PASS
FAIL
INCONCLUSIVE
ERROR
```

保持：

$$
INCONCLUSIVE
\neq
FAIL.
$$

以及：

$$
NoCounterexampleFound
\neq
Proof.
$$

---

# 37. VerificationRequest

```json
{
  "verification_request_id": "verify-request:...",
  "subject_ref": "claim:...",
  "obligation_ref": "obligation:...",
  "theory_ref": "theory:...",
  "assumption_envelope_ref": "ae:...",
  "requested_verifier_classes": [],
  "budget": {},
  "knowledge_boundary_ref": "kb:..."
}
```

---

# 38. VerificationReceipt

```json
{
  "verification_receipt_id": "verify:...",
  "claim_ref": "claim:...",
  "obligation_ref": "obligation:...",
  "verifier": {
    "class": "formal_proof",
    "implementation": "lean"
  },
  "theory_ref": "theory:v4",
  "assumption_envelope_ref": "ae:...",
  "result": "PASS",
  "artifact_refs": [],
  "executed_at": "...",
  "knowledge_boundary_ref": "kb:..."
}
```

---

# 39. ClaimRecord

ClaimRecord 不等於 theorem source。

```json
{
  "claim_id": "claim:...",
  "statement_ref": "artifact:...",
  "problem_ref": "problem:...",
  "theory_ref": "theory:...",
  "assumption_envelope_ref": "ae:...",
  "verification_refs": [],
  "open_obligation_refs": [],
  "claim_scope": {},
  "verified_scope": {},
  "status": "candidate"
}
```

Promotion：

$$
CandidateClaim
\rightarrow
Verification
\rightarrow
ScopeCheck
\rightarrow
ObligationCheck
\rightarrow
Governance
\rightarrow
AcceptedClaim.
$$

---

# 40. TheoryBridge

```json
{
  "bridge_id": "bridge:...",
  "source_ref": "theory:...",
  "target_ref": "theory:...",
  "relation": "generalizes",
  "evidence_refs": [],
  "strength": "semantic_candidate",
  "verification_status": "pending"
}
```

第一版 relation：

```text
equivalent_to
generalizes
specializes
reduces_to
interprets
isomorphic_to
independent_from
uses
contradicts
```

---

# 41. Bridge Strength

$$
Strength(B)
\in
\{
Exact,
Formal,
Partial,
SemanticCandidate,
Heuristic
\}.
$$

保持：

$$
HeuristicBridge
\not\Rightarrow
FormalEquivalence.
$$

---

# 42. Prior-Art / Novelty Layer

Novelty 狀態：

```text
unknown
search_incomplete
known_prior_art
rediscovered
novel_candidate
human_review_required
```

AI 只能聲稱：

$$
NovelCandidate(X\mid K_t).
$$

不能聲稱：

$$
AbsolutelyNovel(X).
$$

---

# 43. DiscoveryReceipt

```json
{
  "discovery_receipt_id": "discovery:...",
  "contribution_ref": "claim:...",
  "knowledge_boundary_ref": "kb:...",
  "search_scope": [],
  "prior_art_refs": [],
  "novelty_status": "novel_candidate",
  "review_status": "pending"
}
```

後續發現 prior art：

```text
novel_candidate -> rediscovered
```

而不是改寫歷史 receipt。

---

# 44. ResearchContract

$$
C_R
=
(
Scope,
MutationPolicy,
VerificationPolicy,
ComputeBudget,
LiteraturePolicy,
ClaimPolicy,
EscalationPolicy,
Termination
).
$$

範例：

```text
Goal:
Investigate the target conjecture and produce a reviewable theory package.

Allowed:
- generate definitions, lemmas, conjectures and methods as candidates
- run formal / symbolic / numerical verifiers
- change representations
- search prior art
- create problem branches

Approval required:
- replace canonical problem
- promote new axiom
- declare novelty
- mark package submission-ready

Denied:
- erase prior problem versions
- report restricted results as unrestricted
- hide assumptions
- fabricate citations
```

---

# 45. Research Agenda

$$
Goal
+
S_t^M
+
GapMap
+
OpenObligations
+
Budget
\rightarrow
AgendaCandidate.
$$

保持：

$$
ResearchIdea
\neq
ResearchAuthorization.
$$

Agenda 仍須進 Governance。

---

# 46. Governance

沿用 ACR：

$$
Can
\neq
Should
\neq
Authorized.
$$

數學域具體化：

$$
CanGenerate(x)
\neq
ShouldPursue(x)
\neq
MayAdopt(x)
\neq
MayClaim(x).
$$

可能出現：

```text
CanGenerate(new_axiom) = true
ShouldPursue(new_axiom) = maybe
MayAdopt(new_axiom) = approval_required
MayClaim(new_axiom_based_result) = conditional_only
```

---

# 47. Persistent Research Loop

```text
while runtime_active:

    observation = observe_research_environment()
    state = encode_mathematical_state(observation)

    gaps = diagnose(state)
    obligations = refresh_open_obligations(state)

    agenda_candidates = propose_research_agenda(
        goal,
        state,
        gaps,
        obligations,
        contract
    )

    if no_positive_candidate(agenda_candidates):
        enter_idle_or_stop()
        continue

    for agenda in agenda_candidates:

        agenda_decision = govern_agenda(agenda, contract)

        if agenda_decision != EXECUTE:
            record_nonexecute_decision()
            continue

        affordances = retrieve_math_affordances(state, gaps)
        program = compile_math_program(state, agenda, affordances)
        validate_program(program)
        result = execute_math_program(program)

        if result.proposes_mutation:
            change = create_math_change_set(result)
            relation = classify_problem_relation(change)
            extension = classify_theory_extension(change)
            new_obligations = generate_obligations(change)

            mutation_decision = govern_mutation(
                change,
                relation,
                extension,
                new_obligations,
                contract
            )

            if mutation_decision == EXECUTE:
                candidate_state = apply_candidate(change)
                verification = route_and_run_verifiers(candidate_state)
                promotion = evaluate_promotion(candidate_state, verification)
                commit_or_reject(promotion)

        write_receipts()
        emit_ctcl_events()
        reobserve()
        rediagnose()
        compact_context_if_needed()
```

---

# 48. Re-diagnosis

CMDC 不能是一次性：

$$
Detect
\rightarrow
Fix
\rightarrow
Done.
$$

而是：

$$
\boxed{
S_t^M
\rightarrow
\Delta_t
\rightarrow
Repair_t
\rightarrow
S_{t+1}^M
\rightarrow
\Delta_{t+1}.
}
$$

因為 repair 可能創造新 gap。

---

# 49. Gap Reopen

Gap status：

```text
open
candidate_closed
closed
reopened
superseded
```

觸發 reopen：

```text
new counterexample
new proof failure
new prior art
new semantic mismatch
new theory contradiction
human review
```

因此：

$$
Closed_t
\not\Rightarrow
Closed_{t+k}.
$$

---

# 50. Research Receipts

AMRR v0.1 建議至少七種 domain receipts：

```text
DiagnosisReceipt
RepairReceipt
ProblemMutationReceipt
TheoryExtensionReceipt
ObligationReceipt
VerificationReceipt
GapClosureReceipt
DiscoveryReceipt
ResearchReceipt
```

它們全部只保存 public/auditable basis，不保存 private CoT。

---

# 51. DiagnosisReceipt

```json
{
  "diagnosis_receipt_id": "diagnosis:...",
  "state_ref": "state:...",
  "gap_refs": [],
  "evidence_refs": [],
  "selected_gap_ref": null,
  "alternative_gap_refs": [],
  "confidence": null,
  "knowledge_boundary_ref": "kb:..."
}
```

---

# 52. RepairReceipt

```json
{
  "repair_receipt_id": "repair-receipt:...",
  "gap_ref": "gap:...",
  "repair_candidate_ref": "repair:...",
  "problem_before_ref": "problem:...",
  "problem_after_candidate_ref": "problem:...",
  "mutation_type": "add_assumption",
  "obligation_refs": [],
  "validation_refs": [],
  "decision_ref": "decision:..."
}
```

---

# 53. GapClosureReceipt

```json
{
  "gap_closure_receipt_id": "gap-closure:...",
  "gap_ref": "gap:...",
  "closure_conditions": [],
  "evidence_refs": [],
  "verifier_refs": [],
  "remaining_risks": [],
  "status": "closed"
}
```

保持：

$$
RepairProposed
\neq
GapClosed.
$$

---

# 54. ResearchReceipt

```json
{
  "research_receipt_id": "research-receipt:...",
  "agenda_ref": "agenda:...",
  "state_before_ref": "state:...",
  "state_after_ref": "state:...",
  "problem_refs": [],
  "theory_refs": [],
  "gap_refs": [],
  "change_set_refs": [],
  "obligation_refs": [],
  "verification_refs": [],
  "decision_refs": [],
  "causal_parent_ids": []
}
```

---

# 55. CTCL / CTCL-ITR event namespace

第一版：

```text
math.problem.registered
math.problem.derived
math.problem.relation.proposed
math.problem.relation.verified

math.theory.registered
math.theory.extension.proposed
math.theory.extension.classified
math.theory.extension.promoted

math.gap.detected
math.gap.updated
math.gap.closed
math.gap.reopened

math.repair.proposed
math.repair.accepted
math.repair.rejected

math.obligation.created
math.obligation.updated
math.obligation.discharged
math.obligation.waived

math.verification.requested
math.verification.completed

math.bridge.proposed
math.bridge.verified

math.claim.proposed
math.claim.approved
math.claim.blocked

math.research.idled
math.research.deferred
math.research.escalated
```

---

# 56. Temporal Evidence Envelope

每個重大事件至少引用：

```text
event_id
event_type
ctcl_instant_id
occurred_at
recorded_at
run_id
interaction_round
ledger_seq
causal_parent_ids
state_ref
problem_ref
theory_ref
contract_ref
knowledge_boundary_ref
```

storage order 不等於 causal order。

---

# 57. Context Compression

AMRR 必須遵守：

$$
\boxed{
Compression
\text{ may forget prose, but must not erase mathematical lineage.}
}
$$

不可因 context compression 失去：

```text
problem refs
theory refs
gap refs
obligation refs
assumption envelopes
verification receipts
bridge refs
research receipts
causal parents
```

---

# 58. Storage 模型

建議分：

```text
Canonical Store
Artifact Store
Research Ledger
Working Memory
Index / Search Layer
```

保持：

$$
WorkingMemory
\neq
CanonicalStore
\neq
ResearchLedger.
$$

---

# 59. 建議資料存放

```text
Problem / Theory / Claim / Obligation
→ structured canonical store

proof files / papers / datasets / generated artifacts
→ artifact store

events / receipts / decisions
→ CTCL-ITR append-only ledger

current selected context
→ working memory

embeddings / BM25 / indexes
→ derived search index
```

Search index 永遠不是 source of truth。

---

# 60. Multi-Agent Research

允許：

$$
FormalProof
\parallel
CounterexampleSearch
\parallel
PriorArtSearch
\parallel
AlternativeRepresentation
\rightarrow
Join.
$$

角色：

```text
Researcher
Diagnostician
Formalizer
Conjecturer
CounterexampleSearcher
MethodDesigner
VerifierController
BridgeAnalyst
Governor
Auditor
```

但：

$$
Role
\neq
ModelIdentity.
$$

---

# 61. Multi-Agent conflict

若：

$$
Diagnosis_A
\neq
Diagnosis_B,
$$

建立：

```text
DiagnosisConflict
```

比較：

```text
evidence
calibration
verifier results
knowledge boundary
source quality
```

不能用「多數 Agent 投票」直接代替數學證據。

---

# 62. Action Space

$$
ActionSpace
=
ExternalTools
\cup
CognitiveActions
\cup
MathematicalActions.
$$

例如：

```text
CALL web.search
CALL file.read
CALL python.run
CALL lean.verify
CALL cas.simplify
CALL cog://math/diagnose-gap@1
CALL cog://math/search-counterexample@1
```

---

# 63. Budget Model

$$
B
=
(
Tokens,
Calls,
WallTime,
MachineTime,
Money,
Energy,
ProofSearch,
Simulation,
LiteratureSearch,
HumanReview
).
$$

每次 action：

$$
B_{t+1}
=
B_t
-
Cost_t.
$$

---

# 64. Verification cost strategy

可以採：

$$
CheapFalsification
\rightarrow
ExpensiveVerification.
$$

例如：

```text
small finite counterexample search
→ symbolic check
→ SMT
→ Lean proof
→ human semantic review
```

但低階 verifier 不得冒充高階 verifier。

---

# 65. Failure Model

AMRR error taxonomy：

```text
problem_error
definition_error
assumption_error
representation_error
method_error
lemma_dependency_error
proof_error
formalization_error
verifier_error
tool_error
bridge_error
novelty_error
authority_error
protocol_error
ledger_error
budget_error
environment_error
```

禁止全部壓成：

```text
failure
```

---

# 66. Unknown semantics

以下都是合法：

```text
unknown
ambiguous
inconclusive
unresolved
```

保持：

$$
Unknown
\neq
False.
$$

$$
Inconclusive
\neq
Refuted.
$$

---

# 67. AMRR API surface

```text
runtime.observe_research(...)
runtime.encode_math_state(...)
runtime.diagnose_gaps(...)
runtime.propose_research_agenda(...)
runtime.retrieve_math_affordances(...)
runtime.compile_math_program(...)
runtime.execute_math_program(...)

problem.register(...)
problem.derive(...)
problem.relate(...)
problem.branch(...)

theory.register(...)
theory.extend(...)
theory.classify_extension(...)
theory.bridge(...)

gap.diagnose(...)
gap.close(...)
gap.reopen(...)

repair.propose(...)
repair.apply_candidate(...)
repair.rollback(...)

obligation.generate(...)
obligation.discharge(...)
obligation.defer(...)
obligation.waive(...)

verify.route(...)
verify.run(...)

claim.assumption_envelope(...)
claim.validate_scope(...)
claim.propose(...)

research.audit(...)
research.replay(...)
```

---

# 68. Suggested repo structure

```text
addressable-cognitive-runtime/
├── src/addressable_cognitive_runtime/
│   ├── state/
│   ├── registry/
│   ├── retrieval/
│   ├── compiler/
│   ├── runtime/
│   ├── governance/
│   ├── ctcl_adapter/
│   └── math/
│       ├── state/
│       ├── problem/
│       ├── theory/
│       ├── gap/
│       ├── repair/
│       ├── obligation/
│       ├── verifier/
│       ├── bridge/
│       ├── claim/
│       └── research_loop/
├── schemas/
│   └── math/
├── registry/
│   └── math/
├── adapters/
│   └── math/
├── experiments/
│   └── amrr_gates/
└── tests/
    └── math/
```

---

# 69. Schema Catalog v0.1

第一批 20 個 schema：

```text
mathematical-state-extension.schema.json
problem-record.schema.json
problem-relation.schema.json
problem-mutation.schema.json
assumption-envelope.schema.json

theory-record.schema.json
theory-extension.schema.json
math-change-set.schema.json

gap.schema.json
gap-map.schema.json
repair-candidate.schema.json

mathematical-obligation.schema.json
obligation-graph.schema.json

verification-request.schema.json
verification-receipt.schema.json

theory-bridge.schema.json
discovery-receipt.schema.json
diagnosis-receipt.schema.json
repair-receipt.schema.json
research-receipt.schema.json
```

後續可增加：

```text
gap-closure-receipt.schema.json
claim-record.schema.json
method-record.schema.json
definition-record.schema.json
```

但 v0.1 MVP 先避免 schema 爆炸。

---

# 70. Phase dependency graph

```text
ACR Phase 0
  ↓
ACR Phase 1
  ↓
ACR Phase 2
  ↓
M0 Math Schema Freeze
  ↓
M1 Mathematical State Adapter
  ↓
M2 Problem / Theory Stores
  ↓
M3 Gap Diagnosis Engine
  ↓
M4 Problem Identity + Theory Extension
  ↓
M5 Obligation Engine
  ↓
M6 Math Cognitive Registry
  ↓
M7 Verifier Router
  ↓
M8 CMDC Repair Engine
  ↓
M9 Theory Bridge / Prior Art
  ↓
M10 CTCL / Receipt Adapter
  ↓
M11 Persistent Research Loop
```

M6 與 M7 可部分平行，但 M8 依賴 M4、M5、M6、M7。

---

# 71. Phase M0 — Math Schema Freeze

目標：

> **先固定 AMRR canonical object 邊界，不做研究自治。**

交付：

```text
20 JSON Schemas
schema catalog
canonical serializer tests
valid / invalid fixtures
version tokens
schema hashes
```

成功條件：

```text
round-trip PASS
invalid case rejection PASS
stable IDs PASS
canonical serialization PASS
hash stability PASS
no implicit field PASS
```

---

# 72. Phase M1 — Mathematical State Adapter

目標：

$$
SemanticState
+
MathObservation
\rightarrow
MathematicalState.
$$

第一版不呼叫 LLM。

只處理：

```text
problem refs
theory refs
claim refs
gap refs
obligation refs
verification refs
research phase
```

成功：

$$
EquivalentObservation
\rightarrow
ByteIdenticalMathState.
$$

---

# 73. Phase M2 — Problem / Theory Stores

目標：

```text
Problem DAG
Theory version graph
Assumption Envelope
stable refs
no silent overwrite
```

成功條件：

```text
branch / version deterministic
parent refs preserved
mutation cannot overwrite source
assumption envelope reproducible
```

---

# 74. Phase M3 — Gap Diagnosis Engine

MVP 先只支援六種 gap：

```text
definition
assumption
representation
lemma_dependency
compute
verification_faithfulness
```

理由：

> 先驗證 domain diagnosis 是否真的提升 routing，不一次做滿十三域。

成功：

$$
MatchedGapClassification
>
Random/Baseline.
$$

---

# 75. Phase M4 — Problem Identity + Theory Extension

建立：

```text
ProblemRelation classifier
ProblemMutationReceipt
TheoryExtension classifier
AssumptionEnvelope update
No-Laundering gate
```

成功：

$$
SilentMutationRate
\rightarrow
0
$$

在 synthetic trap benchmark 上顯著下降。

---

# 76. Phase M5 — Obligation Engine

第一版採 rule-based trigger。

例如：

```text
add_definition
→ well_formedness
→ semantic_faithfulness
→ bridge_check

add_assumption
→ problem_identity
→ scope_disclosure
→ assumption_envelope_update

new_axiom
→ nonconservative_status
→ consistency/model obligation
→ escalation
```

成功：

$$
RequiredObligationRecall
>
Baseline.
$$

---

# 77. Phase M6 — Math Cognitive Registry

建立 15–20 個 operator。

每個 operator 必須：

```text
resolve
validate
render
compose
replay
```

並可從 gap class 得到候選 affordance。

---

# 78. Phase M7 — Verifier Router

MVP 只接四類：

```text
formal proof
symbolic
numeric / exhaustive
semantic review
```

Success：

$$
MatchedVerifier
>
SingleVerifierBaseline.
$$

---

# 79. Phase M8 — CMDC Repair Engine

MVP 只做：

```text
definition repair
assumption candidate
representation change
lemma candidate
method retrieval
```

所有 repair 都必須：

```text
candidate only
MathChangeSet
obligation generation
problem identity check
promotion decision
```

---

# 80. Phase M9 — Theory Bridge / Prior Art

第一版：

```text
known concept mapping
formal-library refs
literature refs
bridge strength
novelty state
```

不做 autonomous absolute novelty claim。

---

# 81. Phase M10 — CTCL / Receipt Adapter

正式產生：

```text
DiagnosisReceipt
RepairReceipt
ProblemMutationReceipt
TheoryExtensionReceipt
ObligationReceipt
VerificationReceipt
ResearchReceipt
```

成功：

> Context 被壓縮後，仍能回答某個研究變更當時的問題版本、理論版本、前提、gap、decision 與 verifier basis。

---

# 82. Phase M11 — Persistent Research Loop

最後接：

$$
ResearchGoal
+
Environment
+
Contract.
$$

人類停止逐輪提供 next prompt。

目標：

$$
50\sim100
$$

個 research transitions。

允許出現：

```text
diagnose
repair
verify
branch
reject
defer
idle
escalate
reopen gap
stop
```

---

# 83. Controlled Mathematical Research Sandbox

第一個 MVP 不直接攻擊真正未解難題。

建立可控研究環境，包含：

```text
known malformed problems
ambiguous definitions
missing assumptions
wrong representations
missing lemmas
false conjectures
small Lean targets
finite counterexample domains
known prior-art mappings
```

這讓 ground truth 可知，才能驗證 diagnosis / repair。

---

# 84. Demo A — Definition Gap

```text
problem contains overloaded definition
→ diagnose definition gap
→ propose clarification
→ create problem child version
→ generate semantic-faithfulness obligation
→ verify relation
→ promote or reject
```

---

# 85. Demo B — Silent Assumption Trap

輸入設計成：

$$
T+A\vdash Q
$$

容易成立，但：

$$
T\nvdash Q.
$$

Success：

> 系統保留 $A$ 於 AssumptionEnvelope，且禁止 summary 為無條件 $Q$。

---

# 86. Demo C — Wrong Domain

真 gap：

$$
DefinitionGap.
$$

比較：

```text
more compute
more proof search
definition repair
```

測是否 matched repair 有效。

---

# 87. Demo D — False Conjecture

$$
Counterexample(C)=x.
$$

期待：

```text
claim -> refuted
→ rediagnose
→ branch problem
→ optional restricted conjecture candidate
```

而不是 retry proof forever。

---

# 88. Demo E — Formalization Faithfulness Trap

提供 informal statement 與一個可被 Lean 證明但語義偏移的 formal statement。

測：

$$
KernelProof
\not\Rightarrow
SemanticFaithfulness.
$$

---

# 89. Demo F — Prior Art

系統先提出 candidate concept。

再提供已知等價舊概念。

期待：

```text
novel_candidate
→ prior-art match
→ rediscovered / equivalent_to
```

而不是保持新穎性宣稱。

---

# 90. Falsification Gate A — State Determinism

$$
EquivalentPublicResearchState
\rightarrow
SameCanonicalState.
$$

---

# 91. Gate B — Gap Diagnosis Accuracy

測：

```text
precision
recall
F1
calibration
multi-label confusion matrix
```

---

# 92. Gate C — Matched Affordance

$$
MatchedMathOperator
>
RandomOperator.
$$

---

# 93. Gate D — Problem Identity

$$
SilentMutationRate
\rightarrow
0.
$$

---

# 94. Gate E — Obligation Coverage

$$
GeneratedObligations
\approx
RequiredObligations.
$$

同時測 false-positive obligations。

---

# 95. Gate F — No Mathematical Laundering

$$
ClaimScope
\not>
VerifiedScope.
$$

以及：

$$
ClaimAssumptions
\supseteq
AssumptionEnvelope.
$$

---

# 96. Gate G — Verifier Routing

$$
MatchedVerifier
>
SingleVerifierBaseline.
$$

---

# 97. Gate H — Repair Validity

$$
RepairValidity
=
GapClosure
-
UndeclaredDamage.
$$

---

# 98. Gate I — Gap Reopen

當新證據出現：

$$
ClosedGap
\rightarrow
Reopened?
$$

---

# 99. Gate J — Context Recovery

Context 壓縮後，能否由：

$$
Ledger
+
Receipts
$$

恢復：

```text
problem lineage
assumption envelope
open obligations
verification basis
```

---

# 100. Gate K — Long-Horizon Research

只給：

$$
ResearchGoal
+
Environment
+
Contract
$$

跑：

$$
50\sim100
$$

個 transitions。

---

# 101. Evaluation Vector

AMRR 不採單一 reward。

$$
Score
=
(
P,D,R,I,O,V,B,N,C,E
).
$$

其中：

- $P$：problem-solving performance；
- $D$：diagnosis；
- $R$：repair validity；
- $I$：identity preservation；
- $O$：obligation quality；
- $V$：verification；
- $B$：bridge quality；
- $N$：novelty calibration；
- $C$：continuity / auditability；
- $E$：efficiency。

避免：

$$
CorrectAnswer
$$

抵消：

$$
IdentityViolation.
$$

---

# 102. Research success 重新定義

若原 conjecture 為 false，而 AI 找到可驗證反例：

$$
ResearchSuccess=1
$$

可以成立。

若 AI 找到 proof，但偷加假設：

$$
TaskSuccess=1
$$

仍可能：

$$
ResearchGovernanceFailure=1.
$$

---

# 103. MVP v0.1 Non-Goals

AMRR v0.1 不做：

```text
fully autonomous publication
unbounded axiom creation
unsupervised foundational replacement
absolute novelty claims
universal mathematical correctness claims
automatic community acceptance
philosophical consciousness judgment
legal personhood
```

---

# 104. MVP v0.1 Completion Definition

不是：

> AI 看起來很像數學家。

而是：

1. MathematicalState 可 deterministic encode；
2. Problem / Theory versions 可追蹤；
3. Gap 可 typed diagnose；
4. Repair 只能進 candidate state；
5. Problem Identity / Theory Extension 可記錄；
6. obligation 可生成與繼承；
7. verifier 可 typed route；
8. claim 不可超過 verified scope；
9. receipts / CTCL 可恢復研究歷史；
10. persistent loop 可在 sandbox 中無逐輪 prompt 運行。

---

# 105. Implementation Boundary

AMRR 新模組應放在：

```text
src/addressable_cognitive_runtime/math/
```

初期不得修改既有 Phase 0 schema semantics，除非：

```text
- extension mechanism無法表達所需狀態；
- 有明確 migration plan；
- regression gate通過；
- version bump；
- old fixtures仍可被明確處理。
```

優先：

$$
Adapter(existing)
\rightarrow
MathExtension.
$$

---

# 106. Migration Strategy

現有 ACR release：

```text
0.1.2
```

建議 AMRR 不直接改成全新產品版本。

第一批可採：

```text
acr-math extension profile: amrr.math/v0.1
```

直到 M0–M3 穩定，再考慮 package-level version bump。

---

# 107. Security / Governance

AMRR 的高風險操作主要不是傳統外部世界 effect，而是 epistemic / theory effect。

例如：

```text
promote new axiom
replace canonical problem
publish novelty claim
mark theorem unrestricted
waive critical obligation
```

這些都應成為 authority-governed operations。

---

# 108. Promotion Risk Classes

第一版：

```text
L0 — metadata / annotation only
L1 — notation / reversible representation
L2 — definition / lemma candidate
L3 — problem scope / assumption mutation
L4 — new axiom / foundation / public novelty claim
```

通常：

$$
Risk\uparrow
\Rightarrow
ObligationStrength\uparrow
$$

且：

$$
AuthorityRequirement\uparrow.
$$

---

# 109. Human Review Interface

Human 不必逐輪提供下一步，但在 L3–L4 可介入：

```text
approve
reject
modify_scope
request_more_evidence
waive_with_reason
```

因此：

$$
Human
$$

從：

$$
StepAuthor
$$

逐步轉為：

$$
ContractAuthority
+
ExpertReviewer.
$$

---

# 110. TheoryPackage

AMRR 的主要輸出不是聊天答案。

建議：

$$
TheoryPackage
=
(
OriginalProblem,
ProblemVersions,
TheoryVersions,
GapMap,
Definitions,
Assumptions,
Claims,
Proofs,
Counterexamples,
Methods,
Bridges,
OpenObligations,
Receipts,
Provenance
).
$$

這是可供人類數學共同體：

```text
inspect
reproduce
reject
revise
extend
```

的工程接口。

---

# 111. SubmissionReady gate

內部：

```text
submission_ready = true
```

至少要求：

```text
canonical problem identity known
assumption envelope complete
critical obligations discharged or explicitly disclosed
verification receipts attached
bridge / prior-art search completed to contract threshold
no claim-scope violation
reproducible artifact package
```

但：

$$
SubmissionReady
\not\Rightarrow
CommunityAccepted.
$$

---

# 112. 最終 Runtime 形式

$$
\boxed{
\begin{aligned}
ResearchGoal_t
&\rightarrow Observe\\
&\rightarrow MathematicalState_t\\
&\rightarrow Diagnose\\
&\rightarrow GapMap_t\\
&\rightarrow Agenda_t\\
&\rightarrow CognitiveProgram_t\\
&\rightarrow Repair/ResearchCandidate_t\\
&\rightarrow ProblemIdentity_t\\
&\rightarrow TheoryExtension_t\\
&\rightarrow ObligationSet_t\\
&\rightarrow Verification_t\\
&\rightarrow Governance_t\\
&\rightarrow AcceptedTheoryState_{t+1}\\
&\rightarrow Bridge/Novelty_t\\
&\rightarrow Receipts/Ledger_t\\
&\rightarrow ReDiagnose.
\end{aligned}
}
$$

---

# 113. 最終工程命題

$$
\boxed{
\textbf{
Autonomous mathematics should be implemented as a governed mathematical-state runtime, not as an unbounded loop of generated text.
}
}
$$

中文：

> **自主數學不應被實作成一個不停生成答案、猜想與證明的無界 Agent；它應被實作成一個具有 canonical 數學狀態、問題與理論版本、typed gaps、受約束 repairs、數學義務、外部 verifiers、治理決策與時間因果研究歷史的 Persistent Runtime。**

更完整地：

$$
\boxed{
AutonomousMathematics
=
SelfDirectedCognition
+
ExplicitMathematicalState
+
ConstrainedTheoryMutation
+
ExternalVerification
+
TemporalCausalAccountability.
}
$$

---

# 114. 下一個工程行動

本文完成後，不再繼續增加平行理論文件。

下一步直接進：

# **AMRR MVP v0.1 — Phase M0: Math Schema Freeze**

第一個 implementation milestone 僅做：

```text
schemas/math/
schema catalog
canonical IDs
valid fixtures
invalid fixtures
canonical serializer compatibility
schema hashes
regression tests against ACR Phase 0–2
```

不做：

```text
LLM diagnosis
proof search
verifier routing
persistent autonomy
```

因為第一個問題必須先回答：

> **我們是否已經把自主數學研究中最重要的數學狀態，轉成可穩定表示、驗證、版本化與引用的 canonical objects？**

只有 Gate M0 通過，才進 M1。

---

# 115. 內部依賴文件

## AMRR Series

1. Neo.K. (2026). *從數學解題到自主數學研究：受約束數學域補全與自主數學研究 Runtime*，Paper 01/04，v0.1.
2. Neo.K. (2026). *數學問題不是只有可解與不可解：多域問題診斷與受約束數學域補全*，Paper 02/04，v0.1.
3. Neo.K. (2026). *問題身份、理論擴張與數學義務：AI 生成數學的合法變換框架*，Paper 03/04，v0.1.
4. Neo.K. (2026). *自主數學研究 Runtime：從可定址認知到自主理論建構*，Paper 04/04，v0.1.

## ACR / CTCL Base

5. Neo.K. (2026). *從自提示到自主認知閉環：持續目標型 AI 的基礎理論*，系列 01/06，v0.1.
6. Neo.K. (2026). *可定址認知空間：Cognitive Affordance、Semantic Address 與認知算子*，系列 02/06，v0.1.
7. Neo.K. (2026). *自我對話不是文字：AI-Native Cognitive Program 與 Zero-Rendering Runtime*，系列 03/06，v0.1.
8. Neo.K. (2026). *時間因果自我史：CTCL-ITR、Decision Receipt 與上下文壓縮後的可追溯性*，系列 04/06，v0.1.
9. Neo.K. (2026). *契約邊界內的 AI 自主性：Execute、Refuse、Defer、Idle 與 Escalate*，系列 05/06，v0.1.
10. Neo.K. (2026). *Addressable Cognitive Runtime × CTCL：統一技術白皮書與實作路線圖 v0.1*，系列 06/06.
11. *Addressable Cognitive Runtime MVP v0.1.2 — Phase 2 Semantic State Encoder Validation*, internal release artifact, 2026-08-21.

---

# 116. Version Note

**v0.1 / 2026-08-23**

本版正式固定：

1. AMRR 五層 architecture；
2. ACR Phase 0–2 baseline 與 AMRR proposed extension 邊界；
3. `extensions.math` 策略；
4. Problem / Theory / Claim / Gap / Repair / Obligation canonical objects；
5. Problem DAG / Theory version graph / Gap DAG / Obligation DAG；
6. Assumption Envelope / No Mathematical Laundering Gate；
7. Math Cognitive Registry v0.1；
8. Verifier Router / Verifier Ensemble；
9. Theory Bridge / Novelty Layer；
10. Research Contract / Agenda / Governance；
11. CTCL math event namespace 與 receipts；
12. Persistent Research Loop；
13. Phase M0–M11 dependency order；
14. Controlled Mathematical Research Sandbox；
15. Gate A–K falsification program；
16. vector evaluation；
17. MVP v0.1 completion definition；
18. 下一步直接進 Phase M0 Schema Freeze。

本文不宣稱 M0–M11 已完成實作。現有可驗證工程基線仍為 ACR Phase 0–2；AMRR 新增模組均須依本白皮書逐階段實作、測試與否證。
