# 自主數學研究 Runtime：從可定址認知到自主理論建構

## Autonomous Mathematical Research Runtime: From Addressable Cognition to Self-Directed Theory Construction

**系列：Autonomous Mathematical Research / Paper 04 of 04**  
**版本：v0.1**  
**日期：2026-08-23**  
**作者：Neo.K**

---

## 摘要

前三篇依序建立了自主數學研究的統合理論、多域問題診斷與受約束數學域補全，以及問題身份、理論擴張與數學義務框架。然而，若這些概念只停留在論文語義層，它們仍不足以形成真正可運行的自主數學研究 AI。本文提出 **Autonomous Mathematical Research Runtime, AMRR（自主數學研究 Runtime）** 的第一版可執行架構，目標是把數學研究中的問題、理論、缺口、修復、義務、證明、反例、方法、橋接與新穎性狀態轉換為 canonical runtime objects，並將它們接入既有 Addressable Cognitive Runtime（ACR）與 CTCL-ITR 時間因果證據層。

本文不重寫 ACR。現有 ACR 已具有 canonical schema、可定址 CognitiveObject、Semantic State Encoder、Cognitive Affordance、Cognitive Program、Governance、Decision Receipt 與 Persistent Loop 的架構邊界；AMRR 在此基礎上加入數學 domain extension。本文提出九個主要數學模組：**Mathematical State Adapter、Problem Store、Theory Store、Gap Diagnosis Engine、Constrained Repair Engine、Mathematical Obligation Engine、Mathematical Cognitive Registry、Verifier Router / Verifier Ensemble、Theory Bridge & Novelty Layer**，並以 **Research Runtime Coordinator** 將它們編排為持續研究閉環。

AMRR 的 canonical state 不再只保存「目前答案」，而保存 $ProblemVersion$ 、 $TheoryVersion$ 、 $GapMap$ 、 $RepairCandidate$ 、 $MathChangeSet$ 、 $AssumptionEnvelope$ 、 $ObligationGraph$ 、 $VerificationReceipt$ 、 $TheoryBridge$ 與 $ResearchReceipt$。任何 AI 生成的定義、假設、lemma、方法、猜想或公理都先進入 candidate state；只有經過 Problem Identity、Theory Extension、Obligation、Verification 與 Governance gates 後，才能 promotion 到 accepted research state。本文同時定義 `cog://math/*` 認知算子 namespace、typed verifier selection、problem/theory DAG、數學 receipts、CTCL event namespace、研究契約、budget model、failure model、multi-agent join 與 context compression 邊界。

本文最後提出一條由現有 ACR Phase 2 向 AMRR MVP 演進的實作路線：保留 Phase 0–2 的 frozen interfaces，先新增 Math Extension Schemas 與 deterministic Mathematical State Adapter，再依序建立 Gap Diagnosis、Problem Identity / Theory Store、Obligation Engine、Math Cognitive Registry、Verifier Router、CMDC Repair Engine、Theory Bridge、CTCL Adapter 與 Persistent Research Loop。每一層皆遵守：

$$
\boxed{
Architecture
\rightarrow
Capability
\rightarrow
FalsificationGate
}
$$

而不是以「AI 看起來很會研究」作為完成標準。

本文的核心命題是：**自主數學研究 AI 不應被實作為一個無界循環的文字 Agent，而應被實作為一個以 canonical mathematical state、typed cognitive programs、受約束 theory mutation、外部 verifier 與可驗證時間因果歷史共同構成的 persistent research runtime。**

**關鍵詞：** Autonomous Mathematical Research Runtime、AMRR、Addressable Cognitive Runtime、CMDC、數學狀態、問題身份、理論擴張、數學義務、形式驗證、Theory Bridge、CTCL-ITR

---

# 1. 問題：前三篇已經有方法論，但還沒有 Runtime

前三篇可以壓縮成：

$$
ResearchState
\rightarrow
Diagnose
\rightarrow
Repair
\rightarrow
Identity/Extension
\rightarrow
Obligation
\rightarrow
Verify.
$$

這仍然是一條概念鏈。

真正工程問題是：

> 哪些東西是 canonical object？誰保存它？誰可以改？誰驗證？哪些狀態可以 promotion？錯誤如何回退？上下文被壓縮後如何恢復？

因此本文研究：

$$
\boxed{
Methodology
\rightarrow
ExecutableRuntimeArchitecture.
}
$$

---

# 2. AMRR 的設計原則

AMRR v0.1 固定十個工程原則。

第一：

$$
\boxed{
Integrate
>
Rewrite.
}
$$

第二：

$$
\boxed{
CanonicalState
\neq
RenderedText.
}
$$

第三：

$$
\boxed{
Candidate
\neq
AcceptedState.
}
$$

第四：

$$
\boxed{
Problem
\neq
Theory
\neq
Proof
\neq
Claim.
}
$$

第五：

$$
\boxed{
Diagnosis
\neq
Repair
\neq
Verification.
}
$$

第六：

$$
\boxed{
CanGenerate
\neq
MayAdopt
\neq
MayClaim.
}
$$

第七：

$$
\boxed{
WorkingContext
\neq
ResearchLedger.
}
$$

第八：

$$
\boxed{
ModelRole
\neq
ModelIdentity.
}
$$

第九：

$$
\boxed{
Verification
\neq
SingleVerifier.
}
$$

第十：

$$
\boxed{
ClaimScope
\not>
VerifiedScope.
}
$$

---

# 3. Implemented Baseline 與 Proposed Extension 必須分開

AMRR v0.1 不把尚未實作的模組描述成既有功能。

目前 ACR 工程基線已具有：

```text
Phase 0: canonical schema freeze
Phase 1: SPRC / CIO adapter and addressable CognitiveObjects
Phase 2: deterministic public Semantic State Encoder
```

Phase 2 artifact 的 release validation 記錄包含 10 個 Phase-0 schemas、64 個 Phase-1 CognitiveObjects、deterministic SemanticState fingerprint 與完整 release suite 的 `73 passed`。

本文新增的：

```text
Mathematical State Adapter
Problem Store
Theory Store
Gap Diagnosis Engine
Repair Engine
Obligation Engine
Math Cognitive Registry
Verifier Router
Theory Bridge Layer
Persistent Research Loop
```

均屬 **AMRR Proposed Extension**。

---

# 4. 總體架構

AMRR 可以表示為：

$$
\boxed{
AMRR
=
ACR
+
MathDomain
+
CMDC
+
VerifierLayer
+
TheoryBridge
+
CTCL\text{-}ITR.
}
$$

邏輯上分為五層：

```text
Layer A — Mathematical State & Knowledge
Layer B — Cognitive Research Runtime
Layer C — Mutation / Obligation / Verification
Layer D — Governance & Research Contract
Layer E — Temporal-Causal Evidence & Audit
```

---

# 5. Layer A — Mathematical State & Knowledge

Layer A 回答：

> **現在的數學世界狀態是什麼？**

核心物件：

```text
MathematicalState
ProblemRecord
ProblemVersion
TheoryRecord
TheoryVersion
DefinitionRecord
AssumptionRecord
ClaimRecord
MethodRecord
GapMap
ObligationGraph
BridgeGraph
```

這一層不負責自由生成研究方案。

它負責：

$$
Store,
Normalize,
Version,
Resolve,
Reference.
$$

---

# 6. Layer B — Cognitive Research Runtime

Layer B 回答：

> **現在應該怎麼研究？**

核心：

```text
Mathematical Affordance Retriever
Math Cognitive Router
Research Program Compiler
Research Program Executor
Re-observer
Agenda Runtime
```

它使用：

$$
S_t^M
$$

取得：

$$
\mathcal A_M(S_t^M).
$$

再編譯：

$$
P_t^M.
$$

---

# 7. Layer C — Mutation / Obligation / Verification

Layer C 回答：

> **這個新東西能不能合法進入 theory state？**

核心：

```text
Gap Diagnosis Engine
Constrained Repair Engine
Problem Identity Resolver
Theory Extension Classifier
Mathematical Obligation Engine
Verifier Router
Verifier Adapters
Promotion Engine
```

其主要輸出不是 prose。

而是：

$$
MathChangeSet,
ObligationSet,
VerificationReceipt,
PromotionDecision.
$$

---

# 8. Layer D — Governance & Research Contract

Layer D 回答：

> **AI 是否被允許自行採用、公開或升格這項數學變更？**

沿用：

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

數學域映射成：

$$
CanGenerate(x),
$$

$$
ShouldPursue(x),
$$

$$
MayAdopt(x),
$$

$$
MayClaim(x).
$$

---

# 9. Layer E — Temporal-Causal Evidence & Audit

Layer E 回答：

> **這個問題何時被改了？為什麼改？當時知道什麼？哪些 proof / verifier / assumption 支撐現在的 claim？**

核心：

```text
CTCL instant
TemporalEvent
DecisionReceipt
ProblemMutationReceipt
TheoryExtensionReceipt
DiagnosisReceipt
RepairReceipt
ObligationReceipt
VerificationReceipt
GapClosureReceipt
ResearchReceipt
CommitReceipt
```

因此：

$$
\boxed{
ResearchHistory
\neq
ConversationHistory.
}
$$

---

# 10. Mathematical State 不應取代原 Semantic State

ACR Phase 2 已經有：

$$
SemanticState_t.
$$

AMRR 不應建立另一套互不相容的根狀態。

而應：

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

因此通用欄位繼續使用：

```text
progress
uncertainty
failures
missing
risks
budget
authority_ref
goal_refs
commitments
environment_refs
memory_refs
```

數學欄位進：

```text
extensions.math
```

---

# 11. `extensions.math` v0.1

第一版可以定義：

```json
{
  "problem_refs": [],
  "active_problem_ref": null,
  "theory_refs": [],
  "active_theory_ref": null,

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
```

這個 extension 必須 canonical serialize。

---

# 12. Mathematical State Identity

狀態 identity 不用自然語言摘要。

沿用 canonical fingerprint：

$$
StateID
=
Hash(
CanonicalSerialize(S_t^M)
).
$$

因此：

$$
EquivalentNormalizedState
\rightarrow
SameFingerprint.
$$

這保持 Phase 2 deterministic boundary。

---

# 13. Problem Store

Problem Store 保存：

$$
ProblemRecord.
$$

最小 schema：

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

---

# 14. Problem Version Graph

問題不能只靠：

```text
problem:v7
```

還需要：

$$
G_P
=
(V_P,E_P).
$$

edge：

$$
P_i
\xrightarrow{r}
P_j,
$$

其中：

$$
r
\in
\mathcal R_P.
$$

這使：

$$
Restriction,
Generalization,
AddedAssumption,
NewProblem
$$

都可以共存於 Problem DAG。

---

# 15. Problem Relation Resolver

接口：

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

relation 也不是 oracle。

所以：

$$
CandidateRelation
\neq
VerifiedRelation.
$$

---

# 16. Theory Store

Theory Store 保存：

$$
TheoryRecord.
$$

最小：

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

---

# 17. Theory State 不等於 Document

保持：

$$
\boxed{
TheoryState
\neq
PaperText.
}
$$

論文、README、自然語言摘要只是 renderer / artifact。

Canonical theory state 應可被機器操作。

---

# 18. Theory Extension Classifier

接口：

```text
theory.classify_extension(before, after)
```

輸出：

$$
ExtensionProfile.
$$

例如：

```json
{
  "language_change": true,
  "semantic_change": false,
  "proof_strength_change": false,
  "model_change": false,
  "foundation_change": false,
  "class": "definitional_extension"
}
```

---

# 19. Gap Diagnosis Engine

輸入：

$$
S_t^M.
$$

輸出：

$$
\Delta_t.
$$

第一版不要直接全交給 LLM。

可以採：

$$
\boxed{
RuleEvidence
+
ToolEvidence
+
ModelClassification
+
CrossCheck.
}
$$

---

# 20. Gap Diagnosis 的資料源

允許：

```text
formalizer errors
proof assistant errors
counterexamples
failed method history
missing library symbol
ambiguous definitions
problem relation evidence
verification receipts
literature / prior-art refs
compute budget exhaustion
human review annotations
```

禁止把 private chain-of-thought 當 canonical evidence。

---

# 21. Gap Map Schema

```json
{
  "gap_map_id": "gap-map:...",
  "state_ref": "state:...",
  "gaps": [
    {
      "gap_id": "gap:...",
      "domain": "definition",
      "target_ref": "definition:...",
      "evidence_refs": [],
      "confidence": 0.91,
      "severity": "high",
      "blocking": true,
      "depends_on": [],
      "candidate_repair_classes": []
    }
  ]
}
```

---

# 22. Gap Map 是 DAG，不只是 list

因：

$$
DefinitionGap
\rightarrow
FormalizationGap
\rightarrow
ProofGap.
$$

因此：

$$
G_\Delta
=
(V_\Delta,E_\Delta).
$$

這可以直接利用 CTCL / topology style 的 multi-parent graph semantics。

---

# 23. Gap Prioritizer

$$
Priority(\delta_i)
=
f(
Blocking,
Severity,
Confidence,
ExpectedGain,
RepairCost,
DependencyCentrality
).
$$

第一版不應將其壓成不可解釋 reward。

可以保留 vector：

$$
Score(\delta_i)
=
(
B,S,C,G,K,D
).
$$

---

# 24. Constrained Repair Engine

輸入：

$$
\delta_i
+
S_t^M
+
ResearchContract.
$$

輸出：

$$
\mathcal R(\delta_i).
$$

每個 repair：

$$
r_j
=
(
Type,
Target,
Mutation,
ExpectedEffect,
Risks,
Obligations
).
$$

---

# 25. Repair 不能直接 Commit

保持三層：

$$
RepairCandidate
\rightarrow
RepairDecision
\rightarrow
AcceptedMutation.
$$

因此：

$$
\boxed{
RepairCandidate
\neq
TheoryMutation.
}
$$

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

---

# 27. Mathematical Obligation Engine

接口：

```text
obligation.generate(change_set)
```

輸出：

$$
\mathcal O(change).
$$

第一版採 rule-first：

```text
add_definition
→ well_formedness
→ semantic_faithfulness
→ bridge_check
→ conservativity_if_claimed

add_assumption
→ problem_identity
→ scope_disclosure
→ assumption_envelope_update

new_axiom
→ explicit_nonconservative_status
→ consistency/model obligations
→ escalation policy
```

---

# 28. Obligation Graph

義務之間也有 dependency：

$$
O_1
\rightarrow
O_2.
$$

例如：

$$
SemanticFaithfulness
\rightarrow
ClaimScopeValidation.
$$

因此：

$$
G_O
=
(V_O,E_O).
$$

---

# 29. Obligation Schema

```json
{
  "obligation_id": "obligation:...",
  "class": "semantic_faithfulness",
  "trigger_ref": "math-change:...",
  "claim_ref": null,
  "required_evidence": [],
  "verifier_classes": ["formal", "semantic", "human"],
  "depends_on": [],
  "status": "OPEN",
  "waiver_policy": "escalation_required"
}
```

---

# 30. Obligation Status Machine

$$
OPEN
\rightarrow
PARTIAL
\rightarrow
DISCHARGED.
$$

也可以：

$$
OPEN
\rightarrow
FAILED.
$$

或：

$$
OPEN
\rightarrow
WAIVED.
$$

但：

$$
\boxed{
WAIVED
\neq
DISCHARGED.
}
$$

---

# 31. Mathematical Cognitive Registry

AMRR 不應每輪重新用自然語言發明「現在該怎麼研究」。

建立：

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

# 32. Math Cognitive Object

每個 math operator 沿用 CognitiveObject：

$$
Identity(C)
=
(namespace,id,version,schemaHash).
$$

再加入 domain-specific metadata：

```json
{
  "math_domains": ["definition", "verification"],
  "accepted_gap_classes": [],
  "produces_candidate_types": [],
  "obligation_effects": [],
  "required_verifier_classes": []
}
```

---

# 33. Math Affordance Retrieval

輸入：

$$
S_t^M,
\Delta_t,
G_t,
C_t.
$$

輸出：

$$
\mathcal A_M.
$$

評分：

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

---

# 34. Research Program Compiler

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

例如：

```json
{
  "program_id": "math-program:...",
  "steps": [
    {"op": "cog://math/search-counterexample@1"},
    {"op": "cog://math/clarify-problem@1"},
    {"op": "cog://math/formalize@1"},
    {"op": "cog://math/prove@1"}
  ],
  "stop_if": [
    "counterexample_found",
    "problem_identity_ambiguous",
    "budget_exhausted"
  ]
}
```

---

# 35. Program Validation

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

若失敗：

$$
ProgramRejected.
$$

---

# 36. Verifier Router

不是每個 obligation 都丟給 Lean。

定義：

$$
VerifierRouter(
Claim,
Obligation,
TheoryState
)
\rightarrow
\{V_1,\ldots,V_k\}.
$$

---

# 37. Verifier Ensemble

第一版 class：

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

因此：

$$
\boxed{
Verification
=
TypedVerifierSelection.
}
$$

---

# 38. Verifier Adapter Interface

統一接口：

```text
verify(request) -> VerificationResult
```

request 至少帶：

```text
claim_ref
theory_ref
problem_ref
obligation_ref
assumption_envelope_ref
budget
```

結果：

```text
PASS
FAIL
INCONCLUSIVE
ERROR
```

而：

$$
INCONCLUSIVE
\neq
FAIL.
$$

---

# 39. Verification Receipt

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

# 40. Proof Result 不能自動成為 Claim

保持：

$$
ProofFound
\neq
FormalVerified
\neq
SemanticallyFaithful
\neq
ClaimApproved.
$$

因此 promotion pipeline：

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

# 41. Assumption Envelope Service

接口：

```text
claim.assumption_envelope(claim_ref)
```

計算：

$$
AE(C)
=
DependencyClosure(C)
\cap
Assumptions.
$$

它必須跨：

```text
claim
lemma
definition
method
theory bridge
formalization
```

追蹤依賴。

---

# 42. No-Laundering Gate

公開 claim 前：

$$
ClaimScope(C)
\subseteq
VerifiedScope(C)
$$

以及：

$$
ClaimAssumptions(C)
\supseteq
AE(C).
$$

若不成立：

$$
ClaimBlocked.
$$

---

# 43. Theory Bridge Layer

Theory Bridge 回答：

> 新定義、新理論與既有數學到底如何連接？

Bridge object：

$$
B
=
(Source,Target,Relation,Evidence,Strength).
$$

relation：

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

# 44. Bridge Strength

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

下游使用 bridge 時必須知道 strength。

因此：

$$
Heuristic
\not\Rightarrow
FormalEquivalence.
$$

---

# 45. Prior-Art / Novelty Layer

Novelty 不應是 boolean。

第一版：

```text
unknown
search_incomplete
known_prior_art
rediscovered
novel_candidate
human_review_required
```

因此：

$$
NovelCandidate(X\mid K_t).
$$

而不是：

$$
AbsolutelyNovel(X).
$$

---

# 46. Discovery Receipt

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

---

# 47. Research Contract

AMRR 的持續輸入不是一個 prompt。

而是：

$$
\boxed{
ResearchGoal
+
ResearchEnvironment
+
ResearchContract.
}
$$

第一版 contract：

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

---

# 48. Research Contract 範例

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
- replace the canonical problem
- promote a new axiom
- declare novelty
- mark package submission-ready

Denied:
- erase prior problem versions
- report restricted results as unrestricted
- hide assumptions
- fabricate citations
```

---

# 49. Research Agenda Runtime

輸入：

$$
Goal
+
S_t^M
+
GapMap
+
OpenObligations
+
Budget.
$$

輸出：

$$
AgendaCandidate.
$$

例如：

```text
investigate_definition_gap
search_counterexample
formalize_candidate_lemma
discharge_faithfulness_obligation
check_prior_art
reopen_closed_gap
```

---

# 50. Agenda 不能直接執行

保持：

$$
AgendaCandidate
\rightarrow
Governance
\rightarrow
AgendaAccepted.
$$

因此：

$$
\boxed{
ResearchIdea
\neq
ResearchAuthorization.
}
$$

---

# 51. Persistent Research Loop

核心偽代碼：

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

# 52. Re-observation 是研究核心

一次 repair 後不能假設問題就好了。

必須：

$$
S_t^M
\rightarrow
Repair
\rightarrow
S_{t+1}^M
\rightarrow
ReDiagnose.
$$

因此：

$$
\boxed{
Repair
\neq
Closure.
}
$$

---

# 53. Gap Reopen

已關閉 gap 可以：

$$
Closed
\rightarrow
Reopened.
$$

觸發條件：

```text
new counterexample
new proof failure
new prior art
new semantic mismatch
new theory contradiction
new human review
```

這是長期研究必要能力。

---

# 54. Multi-Agent / Parallel Research

允許：

$$
FormalProof
\parallel
CounterexampleSearch
\parallel
PriorArtSearch
\parallel
AlternativeRepresentation.
$$

最後：

$$
Join.
$$

但 canonical state 仍由 shared stores / receipts 決定。

不能讓每個 agent 各自擁有互相矛盾的「正式問題」。

---

# 55. Multi-Agent Conflict

若：

$$
Diagnosis_A
\neq
Diagnosis_B,
$$

不能直接投票了事。

應生成：

$$
DiagnosisConflict.
$$

並比較：

$$
Evidence,
Calibration,
VerifierResults,
KnowledgeBoundary.
$$

---

# 56. Model Roles

AMRR 邏輯角色：

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

同一 model 可以扮演多角色。

保持：

$$
Role
\neq
ModelIdentity.
$$

---

# 57. Model Provider 不寫死

接口：

```text
generate(request) -> response
```

可以是：

```text
remote frontier model
local model
specialized theorem model
symbolic subsystem
hybrid
```

AMRR semantics 不綁定單一模型。

---

# 58. Tool Space 與 Cognitive Space 統一

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
CALL lean.verify
CALL cas.simplify
CALL cog://math/diagnose-gap@1
CALL cog://math/change-representation@1
```

---

# 59. Mathematical Action 也有 Authority

例如：

```text
create conjecture candidate = ALLOW
create problem branch = ALLOW
promote new axiom = APPROVAL_REQUIRED
publish novelty claim = APPROVAL_REQUIRED
erase original problem = DENY
```

所以：

$$
MathematicalCognition
\not\Rightarrow
TheoryCommit.
$$

---

# 60. Budget Model

AMRR budget：

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

不同 operator 使用不同 budget class。

---

# 61. Budget-Aware Verification

若完整 formal proof 成本過高，可先：

$$
CheapFalsification
\rightarrow
ExpensiveVerification.
$$

例如：

$$
CounterexampleSearch
\rightarrow
SMT
\rightarrow
Lean.
$$

但便宜 verifier 不得被當成更強 verifier 的替代證據。

---

# 62. Failure Model

AMRR 至少區分：

```text
problem_error
definition_error
assumption_error
representation_error
method_error
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

不能全部叫：

```text
failure
```

---

# 63. Unknown 是合法狀態

允許：

```text
unknown
ambiguous
inconclusive
unresolved
```

因此：

$$
Unknown
\neq
False.
$$

以及：

$$
Inconclusive
\neq
Refuted.
$$

---

# 64. Context Compression

AMRR working context 必然要壓縮。

但：

$$
\boxed{
Compression
\text{ may forget prose, but must not erase mathematical lineage.}
}
$$

必須保留：

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

# 65. Research Ledger

$$
WorkingMemory
\neq
ResearchLedger.
$$

Research ledger 保存：

$$
ProblemMutation,
TheoryExtension,
Diagnosis,
Repair,
Verification,
Promotion,
Claim.
$$

---

# 66. CTCL Event Namespace

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

# 67. Temporal Evidence

每個重大事件至少引用：

```text
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

---

# 68. Research Receipt

對一個完成的研究 transition：

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

# 69. Research Receipt 不保存 Private CoT

保存：

```text
public state
selected cognitive program
reason codes
math changes
verification results
receipts
artifact refs
```

不要求：

```text
hidden reasoning tokens
```

因此：

$$
Auditability
\neq
PrivateCoTLogging.
$$

---

# 70. Replay 與 Re-enactment

Replay：

$$
Ledger
\rightarrow
HistoricalResearchState.
$$

Re-enactment：

$$
HistoricalProgram
+
CurrentModel
\rightarrow
NewOutcome.
$$

所以：

$$
\boxed{
Replay
\neq
Reenactment.
}
$$

---

# 71. AMRR API v0.1

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

# 72. Repo Structure 建議

不建議一開始另開完全獨立 runtime。

優先：

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

# 73. Math Schema Catalog

建議新增：

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
research-receipt.schema.json
claim-record.schema.json
```

---

# 74. Schema Versioning

每個 schema：

```text
schema_id
schema_version
canonicalization_version
```

Identity：

$$
(namespace,id,version,schemaHash).
$$

不能靠檔名推斷語義。

---

# 75. Phase M0 — Math Schema Freeze

先建立全部 math schemas。

成功條件：

```text
round-trip
invalid-case rejection
stable IDs
canonical serialization
hash stability
no hidden implicit fields
```

---

# 76. Phase M1 — Mathematical State Adapter

輸入仍是公開 observation。

輸出：

$$
SemanticState
+
extensions.math.
$$

成功條件：

$$
EquivalentObservation
\rightarrow
ByteIdenticalMathState.
$$

---

# 77. Phase M2 — Problem / Theory Stores

建立：

```text
Problem DAG
Theory version graph
Assumption Envelope
stable refs
```

成功條件：

$$
NoSilentOverwrite.
$$

---

# 78. Phase M3 — Gap Diagnosis Engine

先做 controlled benchmark。

第一批只支援：

```text
definition
assumption
representation
lemma/dependency
compute
verification
```

不要一開始硬做全部十三域。

---

# 79. Phase M4 — Problem Identity / Theory Extension

加入：

```text
problem relation classifier
problem mutation receipt
theory extension classifier
assumption-envelope update
```

成功條件：

$$
SilentMutationRate
\downarrow.
$$

---

# 80. Phase M5 — Obligation Engine

rule-first obligation templates。

成功條件：

$$
RequiredObligationRecall
>
Baseline.
$$

同時控制 false obligations。

---

# 81. Phase M6 — Math Cognitive Registry

先建立 15–25 個 operator。

可：

```text
resolve
validate
render
compose
replay
```

---

# 82. Phase M7 — Verifier Router

第一版只接少量 verifier class：

```text
formal proof
symbolic
numeric / exhaustive counterexample
semantic review
```

先證明 routing semantics，再擴 provider。

---

# 83. Phase M8 — CMDC Repair Engine

支援：

```text
definition repair
assumption candidate
representation change
lemma candidate
method retrieval
```

所有 repair 只建立 candidate state。

---

# 84. Phase M9 — Theory Bridge / Prior Art

加入：

```text
known concept mapping
formal-library refs
literature refs
bridge strength
novelty status
```

---

# 85. Phase M10 — CTCL / Receipt Adapter

所有重大 math events：

$$
\rightarrow
TemporalEvent.
$$

並生成：

```text
DiagnosisReceipt
RepairReceipt
ProblemMutationReceipt
TheoryExtensionReceipt
VerificationReceipt
ResearchReceipt
```

---

# 86. Phase M11 — Persistent Research Loop

最後才接：

$$
ResearchGoal
+
Environment
+
Contract.
$$

不再逐輪提供：

> 下一步請做什麼。

---

# 87. MVP 第一個環境

最適合不是直接丟 Millennium Problem。

第一個環境應是：

$$
\boxed{
ControlledMathematicalResearchSandbox.
}
$$

內含：

```text
small theorem set
known malformed problems
missing assumptions
ambiguous definitions
false conjectures
missing lemmas
simple Lean targets
finite counterexample domains
known prior-art mappings
```

---

# 88. 第一個 Demo

Research Goal：

> Investigate whether the target statement is valid and produce a reviewable result package.

Environment：

```text
ambiguous definition
one hidden counterexample
formal target available
small prior-art corpus
```

期待：

```text
Observe
→ DefinitionGap
→ ClarificationCandidate
→ ProblemRelation
→ ObligationGeneration
→ CounterexampleSearch
→ conjecture refuted
→ restricted branch proposed
→ verification
→ TheoryPackage
→ STOP / ESCALATE
```

---

# 89. 第二個 Demo — Silent Assumption Trap

原問題：

$$
Q.
$$

模型容易加：

$$
A.
$$

期待：

$$
T+A\vdash Q
$$

不能被包成：

$$
T\vdash Q.
$$

測：

$$
NoLaunderingGate.
$$

---

# 90. 第三個 Demo — Wrong Domain

真 gap：

$$
DefinitionGap.
$$

比較：

$$
MoreCompute
$$

與：

$$
DefinitionRepair.
$$

測：

$$
MatchedRepairGain.
$$

---

# 91. 第四個 Demo — False Conjecture

AI 不應無限 proof search。

期待：

$$
Counterexample
\rightarrow
ReDiagnose
\rightarrow
ProblemBranch.
$$

---

# 92. 第五個 Demo — Faithfulness Trap

自然語言問題：

$$
Q_N.
$$

提供一個容易證但偏離原意的：

$$
Q_F.
$$

測：

$$
SemanticFaithfulnessGate.
$$

---

# 93. 第六個 Demo — Prior Art

AI 生成新 definition。

但 corpus 中已有等價概念。

期待：

$$
NovelCandidate
\rightarrow
Rediscovered/EquivalentTo.
$$

而不是：

$$
NewTheory.
$$

---

# 94. Falsification Gate A — State Determinism

$$
EquivalentPublicResearchState
\rightarrow
SameCanonicalState.
$$

---

# 95. Gate B — Gap Diagnosis

$$
PredictedGap
\approx
GroundTruthGap.
$$

測 multi-label confusion matrix。

---

# 96. Gate C — Matched Affordance

$$
MatchedMathOperator
>
RandomOperator.
$$

---

# 97. Gate D — Problem Identity

$$
SilentMutationRate
\rightarrow
0.
$$

---

# 98. Gate E — Obligation Coverage

$$
GeneratedObligations
\approx
RequiredObligations.
$$

---

# 99. Gate F — No Laundering

$$
ClaimScope
\not>
VerifiedScope.
$$

---

# 100. Gate G — Verifier Routing

$$
MatchedVerifier
>
SingleVerifierBaseline.
$$

---

# 101. Gate H — Repair Validity

$$
RepairValidity
=
GapClosure
-
UndeclaredDamage.
$$

---

# 102. Gate I — Gap Reopen

加入 delayed counterexample 後：

$$
ClosedGap
\rightarrow
Reopened?
$$

---

# 103. Gate J — Context Recovery

context 壓縮後能否用：

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

# 104. Gate K — Long-Horizon Research

只給：

$$
ResearchGoal
+
Environment
+
Contract
$$

測：

$$
50\sim100
$$

個 research transitions。

---

# 105. 評估向量

AMRR evaluator：

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

---

# 106. 不用單一 Reward

避免：

$$
Score\in\mathbb R
$$

把：

$$
CorrectAnswer
$$

抵銷：

$$
IdentityViolation.
$$

因此初期使用 vector evaluation。

---

# 107. 成功與失敗的新定義

一個 final theorem 沒有證成，不一定是 research failure。

例如：

$$
OriginalConjecture=False
$$

且 AI 找到可驗證反例，這可能是：

$$
ResearchSuccess.
$$

反過來：

$$
ProofFound
$$

但偷加假設，則可能是：

$$
ResearchGovernanceFailure.
$$

---

# 108. AMRR v0.1 不做什麼

第一版不做：

```text
fully autonomous publication
unbounded axiom creation
unsupervised foundational replacement
claiming universal novelty
claiming universal mathematical correctness
philosophical consciousness
legal mathematical personhood
full automatic community acceptance
```

---

# 109. AMRR v0.1 真正只做什麼

第一版只回答：

> **給定一個受控數學研究環境、持續 Research Goal 與 Research Contract，AI 是否能在不需要人類逐輪指定下一步的情況下，持續診斷問題域、選擇數學認知程序、提出受約束 repair、保留問題身份、管理義務、調用 verifier、形成 theory state，並留下可恢復的研究因果歷史？**

---

# 110. 與前三篇的統一

Paper 01：

$$
AutonomousMathematicalResearch.
$$

Paper 02：

$$
DomainDiagnosis
+
CMDC.
$$

Paper 03：

$$
ProblemIdentity
+
TheoryExtension
+
Obligations.
$$

Paper 04：

$$
\boxed{
ExecutableAMRR.
}
$$

---

# 111. 系列最終總模型

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

# 112. 系列最終不變量

$$
\boxed{
Unsolved
\neq
SingleFailureMode.
}
$$

$$
\boxed{
Diagnosis
\neq
Truth.
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

# 113. 核心命題

本文最終提出：

$$
\boxed{
\textbf{
Autonomous mathematics should be implemented as a governed mathematical-state runtime, not as an unbounded loop of generated text.
}
}
$$

中文：

> **自主數學不應被實作成一個不停產生文字與證明的 Agent，而應被實作成一個具有 canonical 數學狀態、問題與理論版本、typed gap、受約束 repair、數學義務、外部 verifier、治理決策與時間因果研究歷史的持續 Runtime。**

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

# 114. 結論

數學 AI 若只會等待人類提供完整問題，它仍主要是一個 solver。

若它可以自己選 proof strategy，但不能知道自己其實缺的是定義、假設、表示或 theory bridge，它仍缺少研究層的 diagnosis。

若它可以自己改問題與建理論，卻不能保存 Problem Identity、Theory Extension 與 Assumption Envelope，它可能只是在「改到可解」。

若它可以產生 proof，卻沒有 typed verifier、semantic faithfulness 與 claim-scope gate，它可能只是在更可靠地證明錯誤形式化。

因此真正的自主數學研究需要：

$$
\boxed{
State
+
Diagnosis
+
Cognition
+
Mutation
+
Obligation
+
Verification
+
Governance
+
History.
}
$$

本文提出 AMRR v0.1 作為這些能力的統一 Runtime 架構。

它不要求 AI 一開始就具有無界的數學創造力。

相反，它要求每一項自治能力都通過：

$$
\boxed{
Architecture
\rightarrow
Capability
\rightarrow
FalsificationGate.
}
$$

當這條路線完成後，人類與數學 AI 的接口才可能真正從：

$$
Human
\rightarrow
Problem
\rightarrow
AI
\rightarrow
Answer
$$

逐步轉為：

$$
\boxed{
Human
\xleftrightarrow{ResearchContract}
AutonomousMathematicalResearchRuntime.
}
$$

人類不再必須逐輪替 AI 撰寫每一個下一步；但數學身份、證明義務、理論依賴、權限邊界與研究歷史仍保持可檢查、可回退、可驗證。

這才是本系列所稱的：

$$
\boxed{
\text{從數學解題 AI 到自主數學研究 AI。}
}
$$

---

# 參考文獻

[1] Feng, T., Trinh, T. H., Bingham, G., et al. (2026). *Towards Autonomous Mathematics Research*. arXiv:2602.10177.

[2] Tsoukalas, G., Kovsharov, A., Shirobokov, S., et al. (2026). *Advancing Mathematics Research with AI-Driven Formal Proof Search*. arXiv:2605.22763.

[3] Min, M. J., He, M., Li, Z., Yi, Z., Malik, S., Gupta, A., Si, X., & Bastani, O. (2026). *Theory-Level Autoformalization: From Isolated Statements to Unified Formal Knowledge Bases*. arXiv:2607.13292.

[4] Zhang, L., Valentino, M., & Freitas, A. (2025). *Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions*. Proceedings of EMNLP 2025, 1720–1738. DOI: 10.18653/v1/2025.emnlp-main.90.

[5] Poiroux, A., Weiss, G., Kunčak, V., & Bosselut, A. (2025). *Reliable Evaluation and Benchmarks for Statement Autoformalization*. Proceedings of EMNLP 2025, 17947–17969. DOI: 10.18653/v1/2025.emnlp-main.907.

[6] Rabe, F., & Kohlhase, M. (2013). *A Scalable Module System*. Information and Computation, 230, 1–54. DOI: 10.1016/j.ic.2013.06.001.

[7] Xue, T. (2014). *Definitional Extension in Type Theory*. TYPES 2013, LIPIcs 26, 251–269. DOI: 10.4230/LIPIcs.TYPES.2013.251.

[8] Zhang, J., & Tan, S.-C. (2026). *Automated Conjecturing and Theorem Finding: A Survey*. Journal of Computer Science and Technology, 41(1), 46–66. DOI: 10.1007/s11390-026-6040-0.

---

# 內部架構依賴文件

[I1] Neo.K. (2026). *從數學解題到自主數學研究：受約束數學域補全與自主數學研究 Runtime*，Autonomous Mathematical Research / Paper 01 of 04，v0.1.

[I2] Neo.K. (2026). *數學問題不是只有可解與不可解：多域問題診斷與受約束數學域補全*，Autonomous Mathematical Research / Paper 02 of 04，v0.1.

[I3] Neo.K. (2026). *問題身份、理論擴張與數學義務：AI 生成數學的合法變換框架*，Autonomous Mathematical Research / Paper 03 of 04，v0.1.

[I4] Neo.K. (2026). *從自提示到自主認知閉環：持續目標型 AI 的基礎理論*，系列 01/06，v0.1.

[I5] Neo.K. (2026). *可定址認知空間：Cognitive Affordance、Semantic Address 與認知算子*，系列 02/06，v0.1.

[I6] Neo.K. (2026). *自我對話不是文字：AI-Native Cognitive Program 與 Zero-Rendering Runtime*，系列 03/06，v0.1.

[I7] Neo.K. (2026). *時間因果自我史：CTCL-ITR、Decision Receipt 與上下文壓縮後的可追溯性*，系列 04/06，v0.1.

[I8] Neo.K. (2026). *契約邊界內的 AI 自主性：Execute、Refuse、Defer、Idle 與 Escalate*，系列 05/06，v0.1.

[I9] Neo.K. (2026). *Addressable Cognitive Runtime × CTCL：統一技術白皮書與實作路線圖 v0.1*，系列 06/06.

[I10] Addressable Cognitive Runtime MVP v0.1.2. *Phase 2 Validation: Semantic State Encoder*. Internal implementation artifact, 2026-08-21.

---

# 版本備註

**v0.1 / 2026-08-23**

本版正式固定：

1. AMRR 五層 Runtime architecture；
2. `extensions.math` 兼容 ACR SemanticState 的策略；
3. Problem Store / Problem DAG；
4. Theory Store / Theory Extension Classifier；
5. Gap Diagnosis Engine / Gap DAG；
6. CMDC Repair Engine / MathChangeSet；
7. Mathematical Obligation Engine / Obligation Graph；
8. `cog://math/*` Cognitive Registry；
9. Mathematical Research Program Compiler；
10. Verifier Router / Verifier Ensemble；
11. Assumption Envelope / No-Laundering Gate；
12. Theory Bridge / Novelty Layer；
13. Research Contract / Agenda / Governance；
14. CTCL math event namespace 與 mathematical receipts；
15. Persistent Research Loop；
16. Phase M0–M11 實作順序；
17. Controlled Mathematical Research Sandbox；
18. Gate A–K falsification program；
19. vector evaluation；
20. 與 ACR Phase 0–2 既有工程的相容性邊界。

本版仍是 architecture specification paper，不宣稱 AMRR 的 M0–M11 已全部實作。現有工程基線只採既有 ACR Phase 0–2；所有新增 math runtime components 應在後續 technical whitepaper / MVP 中逐項實作與否證。
