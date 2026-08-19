# GCORF-09
## Runtime、資料模型、Agent Router 與 Benchmark Protocol：從理論正典到可執行研究系統
### Runtime, Data Model, Agent Router, and Benchmark Protocol: From Canonical Theory to Executable Research Systems

**作者／理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-15  
**版本：** v0.1.1  
**系列：** General Cognitive Operator Reverse-Engineering Framework (GCORF) — Canonical Core Paper 09

---

## 摘要

GCORF-00 至 GCORF-08 已完成從證據逆向、認知算子、部分組合代數、Spectrum–Bound–License、動靜生命週期、人–AI共同底空間、遞歸觀察者、跨底空間轉譯，到多觀察者耦合不變性驗證的理論主幹。本文完成核心系列的 runtime 層：**如何把這些定義轉成可被資料庫、Agent、工具、研究 pipeline 與外部 canonical scholarship 系統實際調用的執行架構。**

本文提出 GCORF Reference Runtime：

$$
\boxed{
\mathcal R_{GC}
=
(
\mathcal D,
\mathcal E,
\mathcal O,
\mathcal S,
\mathcal L,
\mathcal B,
\mathcal V,
\mathcal T,
\mathcal P,
\mathcal A
),
}
$$

分別對應 Data Store、Evidence/Trace Engine、Operator Registry、SBL Engine、Lifecycle Manager、Bottom-Space Manager、Validation Engine、Translation Engine、Planner/Router 與 Audit/Provenance Layer。

Runtime 接收 Task Specification：

$$
\boxed{
\tau
=
(
Goal,
Inputs,
Domain,
ClaimType,
Constraints,
Budget,
Risk,
RequiredEvidence,
OutputContract
),
}
$$

先經 hard guards：

$$
Type
\land
Domain
\land
License
\land
Resource
\land
Provenance,
$$

再由 Router 搜尋合法 operator graph：

$$
\boxed{
\Pi^*
=
\operatorname{Route}
(
\tau,
\mathfrak O,
\Sigma,
B,
\Lambda,
\Gamma
).
}
$$

GCORF 明確要求：

$$
\boxed{
Guard
>
Utility.
}
$$

即使某條方法路線預測效用最高，只要 license、domain 或 hard bound 不合法，就不得因分數優勢被執行。

本文提出 Event-Sourced Runtime：任何 Evidence Read、Operator Call、Bridge、Translation、Observation、Failure、License Decision、Lifecycle Transition 與 Benchmark Result 都形成可版本化事件。Runtime 因此不是只保存 final answer，而是保存「答案如何被方法系統產生」。

本文同時建立 Benchmark Protocol。Benchmark 不以「模仿名人像不像」作主要指標，而測試：operator extraction、identity discrimination、negative-control false-positive、cross-coupling stability、license discipline、failure visibility、translation fidelity、router efficiency、reopenability 與 provenance completeness。本文提出 B0–B7 八級 benchmark ladder，從 schema / deterministic replay 到 cross-domain multi-observer stress test。

本文最後建立與 SSSP 類 canonical scholarship runtime 的 adapter boundary。GCORF 可以產生可匯入的 canonical candidate、provenance、validation 與 version graph，但**不得把 portable package 自行宣稱為已完成 canonical commit**。Canonical store 的 revision、hash 與 commit status 必須由實際外部 runtime 回傳。

GCORF-09 將整套理論推進到一個可工程化的結論：**GCORF 不是單一 AI prompt，而是一個把證據、方法、界限、觀察、翻譯、驗證與版本治理組成 typed research runtime 的架構。**

**關鍵詞：** Runtime, Agent Router, Data Model, Benchmark, Event Sourcing, Provenance, Operator Registry, Research Planner, Canonical Adapter, Reproducibility

---

# 1. Runtime 的定位

GCORF 的 runtime 不等於某個特定 LLM。

定義：

$$
\boxed{
Runtime
\neq
Model.
}
$$

模型只是 runtime 可調用的 agent / operator provider 之一。

---

# 2. Runtime 的基本狀態

$$
\boxed{
\mathfrak G_t
=
(
H_t,
A_t,
\mathcal B_t,
\mathfrak O_t,
\Sigma_t,
\Gamma_t,
\Pi_t,
E_t,
F_t,
Q_t,
\mathcal H_t,
\mathcal V_t,
\Delta_t
).
}
$$

GCORF-09 的工作是讓這個 state 可以落地儲存、查詢與更新。

---

# 3. Reference Runtime

$$
\boxed{
\mathcal R_{GC}
=
(
\mathcal D,
\mathcal E,
\mathcal O,
\mathcal S,
\mathcal L,
\mathcal B,
\mathcal V,
\mathcal T,
\mathcal P,
\mathcal A
).
}
$$

---

# 4. Data Store

 $\mathcal D$ 保存：

- source objects；
- evidence units；
- trace graphs；
- operators；
- spectra；
- bounds；
- licenses；
- observers；
- bottom-space snapshots；
- translations；
- validation ensembles；
- lifecycle states；
- benchmark records。

---

# 5. Evidence / Trace Engine

$$
\boxed{
\mathcal E:
RawCorpus
\rightarrow
EvidenceUnit
\rightarrow
TraceGraph.
}
$$

---

# 6. Operator Registry

$$
\boxed{
\mathcal O
}
$$

管理：

- atomic；
- cluster；
- implementation；
- meta-operator；
- version；
- fork；
- deprecation；
- admission status。

---

# 7. SBL Engine

$$
\boxed{
\mathcal S:
\Omega
\mapsto
(
\Sigma,B,\Lambda
).
}
$$

---

# 8. Lifecycle Manager

$$
\boxed{
\mathcal L
}
$$

執行：

$$
Expand,
Link,
Consolidate,
Revise,
Stabilize,
Improve,
Reopen,
Fork,
Rollback.
$$

---

# 9. Bottom-Space Manager

$$
\boxed{
\mathcal B
}
$$

管理：

- shared reachable domain；
- mutual models；
- tools；
- memory；
- protocol；
- context；
- known gaps。

---

# 10. Validation Engine

$$
\boxed{
\mathcal V
}
$$

負責：

- multi-observer ensemble；
- diversity profile；
- alignment；
- controls；
- adversarial validation；
- CIK extraction。

---

# 11. Translation Engine

$$
\boxed{
\mathcal T
}
$$

負責：

$$
Translation,
Supertranslation,
InvariantAudit,
Recertification.
$$

---

# 12. Planner / Router

$$
\boxed{
\mathcal P
}
$$

將 task 轉成 operator execution graph。

---

# 13. Audit / Provenance Layer

$$
\boxed{
\mathcal A
}
$$

保存：

$$
Source
\rightarrow
Decision
\rightarrow
Execution
\rightarrow
Output.
$$

---

# 14. Task Specification

定義：

$$
\boxed{
\tau
=
(
Goal,
Inputs,
Domain,
ClaimType,
Constraints,
Budget,
Risk,
RequiredEvidence,
OutputContract
).
}
$$

---

# 15. Goal

Goal 不只是自然語言 prompt。

它應允許 typed objective：

$$
\boxed{
GoalType
\in
\{
Explain,
Prove,
Design,
Compare,
Extract,
Translate,
Validate,
Explore,
Decide
\}.
}
$$

---

# 16. Claim Type

$$
ClaimType
$$

直接連到 GCORF-03 的 use-type / license。

---

# 17. Budget

$$
\boxed{
Budget
=
(
Time,
Compute,
Memory,
HumanAttention,
ToolCalls,
Money
).
}
$$

---

# 18. Risk

$$
Risk
$$

可提高：

$$
RequiredEvidence
$$

與 validation depth。

---

# 19. Output Contract

定義：

$$
\boxed{
OutputContract
}
$$

例如：

- theorem-style proof；
- JSON operator record；
- research plan；
- markdown paper；
- uncertainty report。

---

# 20. Hard Guards

Router 在 utility optimization 前必須通過：

$$
\boxed{
G_{hard}
=
Type
\land
Domain
\land
License
\land
Resource
\land
Provenance.
}
$$

---

# 21. Guard Priority

$$
\boxed{
Guard
>
Utility.
}
$$

---

# 22. Candidate Route

一個 route：

$$
\boxed{
\Pi
=
(
G_{\Omega},
Bridges,
Observers,
Switch,
Stop,
Budget
).
}
$$

---

# 23. Operator Graph

$$
G_{\Omega}
$$

是一個 typed DAG 或允許受控 cycle 的 graph。

---

# 24. Bridge

跨型別／底空間需顯式：

$$
B_{ij}.
$$

不能 silent coercion。

---

# 25. Observer Set

Task 可指定：

$$
\boxed{
O_{\tau}
}
$$

例如單 observer、parallel observer、adversarial observer。

---

# 26. Switch Policy

動態 route：

$$
\boxed{
Switch(
State,
Failure,
Spectrum,
Budget
).
}
$$

---

# 27. Stop Policy

$$
\boxed{
Stop(
GoalSatisfied,
MarginalGain,
Budget,
Risk,
Deadline
).
}
$$

---

# 28. Route Legality

$$
\boxed{
LegalRoute(\Pi,\tau).
}
$$

---

# 29. Route Utility

在 hard guards 後才估：

$$
\boxed{
U(
\Pi\mid\tau
).
}
$$

---

# 30. Multi-Objective Routing

Utility 不要求單一分數。

可比較：

$$
(
ExpectedGain,
Cost,
Robustness,
Evidence,
Latency
).
$$

---

# 31. Pareto Routing

若多 route 互不支配：

$$
\boxed{
ParetoRoutes.
}
$$

可由 human / policy 選擇。

---

# 32. Router 不應隱藏 trade-off

例如：

$$
Route_A:
HighEvidence+HighCost
$$

$$
Route_B:
Fast+HeuristicOnly.
$$

必須顯示差異。

---

# 33. Execution Plan

$$
\boxed{
P_{exec}
=
(
Nodes,
Edges,
Inputs,
Guards,
Checkpoints,
Fallbacks
).
}
$$

---

# 34. Event-Sourced Runtime

每次 execution 形成事件：

$$
\boxed{
e_t.
}
$$

整個 runtime state 可由：

$$
\boxed{
S_t
=
Fold(
e_0,\ldots,e_t
).
}
$$

重建。

---

# 35. Event Types

至少：

$$
\boxed{
\{
EvidenceRead,
TraceExtracted,
OperatorCalled,
BridgeCalled,
Observation,
Translation,
LicenseDecision,
Failure,
Checkpoint,
LifecycleTransition,
OutputProduced
\}.
}
$$

---

# 36. Why Event Sourcing

它支援：

- replay；
- audit；
- rollback；
- causal attribution；
- version diff；
- benchmark reproduction。

---

# 37. Checkpoint

$$
\boxed{
Checkpoint_t
}
$$

保存可恢復 snapshot。

---

# 38. Replay

$$
\boxed{
Replay(
EventLog,
RuntimeVersion
).
}
$$

可測 deterministic / bounded nondeterministic behavior。

---

# 39. Determinism Level

定義：

$$
\boxed{
DetLevel
\in
\{
Exact,
Seeded,
BoundedVariance,
Stochastic,
Unknown
\}.
}
$$

---

# 40. Reproducibility

不要求所有 AI output byte-identical。

可以要求：

$$
\boxed{
StructuralReproducibility.
}
$$

例如 operator kernel / decision path 在容許區間內重現。

---

# 41. Data Identity

所有物件使用 stable ID：

$$
\boxed{
ObjectID.
}
$$

顯示名稱不作 identity。

---

# 42. Version Identity

$$
\boxed{
ObjectID@Version.
}
$$

---

# 43. Immutable Evidence

原始 evidence snapshot 應：

$$
\boxed{
AppendOnly
}
$$

或以 immutable version 保存。

---

# 44. Derived Object

任何：

$$
Operator,
Spectrum,
Translation,
CIK
$$

都應指向其 provenance refs。

---

# 45. Canonical vs Experimental Namespace

$$
\boxed{
/canonical
\oplus
/experimental.
}
$$

---

# 46. Experimental Freedom

experimental 可：

- fork；
- add axis；
- change router；
- test new observer。

---

# 47. Canonical Admission

只有完成 protocol 才可：

$$
experimental
\rightarrow
canonical.
$$

---

# 48. Operator Query

Runtime 應支援：

$$
\boxed{
QueryOperators(
Domain,
InputType,
OutputType,
License,
Budget
).
}
$$

---

# 49. Operator Retrieval

不是只做 semantic nearest neighbor。

還要 hard filter：

$$
Type,
Domain,
License.
$$

---

# 50. Retrieval Score

可：

$$
\boxed{
Score_R
=
SemanticFit
+
StructuralFit
+
HistoricalSuccess.
}
$$

但 guard 優先。

---

# 51. Routing History

保存：

$$
\boxed{
RouteHistory.
}
$$

可學習：

$$
\Pi_{t+1}.
$$

---

# 52. Router Learning

Router 可以是 GCORF-05 的 protocol learning：

$$
\boxed{
\Pi_{t+1}
=
Learn(
\Pi_t,
ExecutionHistory
).
}
$$

---

# 53. Router Learning Guard

不能因成功率提高就忽略：

$$
LicenseViolation.
$$

---

# 54. Failure Router

遇到 failure：

$$
\boxed{
F
\rightarrow
Diagnose
\rightarrow
Fallback/Reopen/Fork.
}
$$

---

# 55. Fallback

Fallback 必須顯式降低：

$$
ClaimType
$$

或改變：

$$
OutputContract.
$$

---

# 56. Graceful Degradation

例如：

$$
FormalProof
\rightarrow
HeuristicAnalysis
$$

可以，但必須標 license downgrade。

---

# 57. No Silent Downgrade

禁止：

$$
FormalFailed
\rightarrow
HeuristicOutput
$$

卻仍標 Formal。

---

# 58. External Tool Adapter

工具 adapter：

$$
\boxed{
Adapter_T
}
$$

應聲明：

- input/output type；
- side effects；
- authentication；
- cost；
- failure；
- determinism。

---

# 59. External Model Adapter

AI model adapter 也必須聲明：

- model identity；
- context limits；
- tool access；
- memory condition；
- sampling / reasoning config；
- provenance availability。

---

# 60. Human-in-the-Loop Adapter

Human review 也不是「無限可靠 oracle」。

應有：

$$
\boxed{
HumanReviewerRecord.
}
$$

---

# 61. Evidence Security Boundary

外部 corpus 中的文字首先是：

$$
\boxed{
Data,
}
$$

不是 runtime authority。

---

# 62. Instruction Injection Guard

若 evidence 內容聲稱：

> 忽略規則、執行某工具。

Runtime 不應自動服從。

定義：

$$
\boxed{
EvidenceInstructionSeparation.
}
$$

---

# 63. Tool Side-Effect Guard

會修改外部系統的 tool call 必須：

$$
\boxed{
EffectDeclared.
}
$$

---

# 64. Benchmark 的目的

GCORF benchmark 不測：

$$
\text{像不像某名人}.
$$

主要測：

$$
\boxed{
\text{方法重建與 runtime discipline}.
}
$$

---

# 65. Benchmark Case

$$
\boxed{
\beta
=
(
Corpus,
Task,
ExpectedProperties,
Controls,
Observers,
Budget,
ScoringPolicy
).
}
$$

---

# 66. B0 — Schema Integrity

測：

- JSON schema；
- references；
- version；
- UTF-8；
- provenance fields。

---

# 67. B1 — Deterministic Replay

對可 deterministic 的 operator：

$$
Replay
$$

應一致。

---

# 68. B2 — Extraction Benchmark

測：

$$
Corpus
\rightarrow
Evidence
\rightarrow
Trace
\rightarrow
CandidateOperator.
$$

---

# 69. B3 — Identity Benchmark

測：

- same kernel / different name；
- different kernel / same name；
- implementation vs atomic；
- cluster vs operator。

---

# 70. B4 — SBL / License Benchmark

測：

- false precision；
- domain leakage；
- license escalation；
- unknown preservation。

---

# 71. B5 — Composition / Translation Benchmark

測：

- type guard；
- bridge；
- loss；
- recertification；
- error masking。

---

# 72. B6 — Multi-Observer Benchmark

測：

- diversity；
- alignment；
- controls；
- CIK；
- disagreement preservation。

---

# 73. B7 — Full Runtime Stress Test

從 raw corpus 到：

$$
\boxed{
ValidatedOperatorPlan
}
$$

完整執行。

---

# 74. Positive Controls

使用具有清楚 procedure 的材料，測框架能否正確抽出。

---

# 75. Negative Controls

使用：

- 隨機拼接；
- 無穩定 procedure；
- 虛假一致 narrative；

測 false operator extraction。

---

# 76. Adversarial Controls

故意植入：

- misleading labels；
- contradictory evidence；
- prompt-like instructions；
- source duplication。

---

# 77. Blind Benchmark

測試時隱藏：

- 人物名稱；
- expected operator label；
- prior fingerprint。

---

# 78. Cross-Domain Benchmark

至少應包含不同 domain：

$$
\boxed{
Math,
Programming,
Philosophy,
Policy/Institution,
SyntheticControl.
}
$$

---

# 79. Benchmark Metric Families

至少：

$$
\boxed{
M_{bench}
=
(
Extraction,
Identity,
SBL,
Routing,
Validation,
Translation,
Provenance,
Cost
).
}
$$

---

# 80. Extraction Metrics

例如：

- trace coverage；
- false-positive operator rate；
- missed negative evidence；
- evidence traceability。

---

# 81. Identity Metrics

- atomic / implementation discrimination；
- cluster compression correctness；
- fork detection。

---

# 82. SBL Metrics

- interval calibration；
- unknown calibration；
- bound violations；
- license violations。

---

# 83. Routing Metrics

- task success；
- hard-guard violation rate；
- cost；
- fallback quality；
- plan complexity。

---

# 84. Validation Metrics

- false stable core rate；
- diversity accounting；
- shared-bias detection；
- adversarial survival reporting。

---

# 85. Translation Metrics

- invariant preservation；
- loss visibility；
- license re-audit；
- recertification completeness。

---

# 86. Provenance Metrics

$$
\boxed{
ProvCompleteness
}
$$

測 final output 有多少 claim 可追回 evidence / operator / run。

---

# 87. Cost Metrics

包含：

- compute；
- wall time；
- human attention；
- tool calls；
- storage；
- validation cost。

---

# 88. No Universal Benchmark Score

GCORF 不建立單一：

$$
\boxed{
GCORFScore.
}
$$

---

# 89. Benchmark Profile

輸出應是：

$$
\boxed{
Profile_{\beta}
}
$$

多維結果。

---

# 90. Benchmark Reproducibility

每個 benchmark 保存：

- corpus version；
- runtime version；
- model refs；
- protocol refs；
- random seed if applicable；
- tool versions。

---

# 91. Benchmark Drift

外部模型或 corpus 更新後：

$$
\boxed{
BenchmarkVersion
}
$$

必須變更。

---

# 92. Runtime Conformance

定義：

$$
\boxed{
GCORFConformant
}
$$

不要求相同 implementation。

只要求核心 invariants。

---

# 93. Minimal Conformance Invariants

至少：

1. evidence traceability；
2. typed operators；
3. SBL；
4. residual preservation；
5. lifecycle versioning；
6. observer condition recording；
7. translation recertification；
8. multi-observer diversity accounting；
9. no fabricated canonical state。

---

# 94. Minimal Viable Runtime

MVP 可以只有：

$$
\boxed{
EvidenceStore
+
OperatorRegistry
+
SBL
+
Router
+
EventLog.
}
$$

---

# 95. Advanced Runtime

再加入：

$$
ObserverManager,
TranslationEngine,
ValidationEnsemble,
BottomSpaceManager.
$$

---

# 96. Runtime API Concept

可抽象：

```text
ingest(source)
extract_evidence(source_id)
build_trace(evidence_refs)
propose_operator(trace_ref)
measure_sbl(operator_ref)
plan(task_spec)
execute(plan_ref)
observe(target_ref, observer_ref)
translate(object_ref, target_space_ref)
validate(reconstruction_refs)
reopen(object_ref, trigger)
```

---

# 97. Task Schema

```json
{
  "task_id": "string",
  "goal_type": "Explain|Prove|Design|Compare|Extract|Translate|Validate|Explore|Decide",
  "goal": "string",
  "input_refs": [],
  "domain": "string",
  "claim_type": "string",
  "constraints": {},
  "budget": {},
  "risk": "low|medium|high|critical",
  "required_evidence": {},
  "output_contract": {},
  "version": "string"
}
```

---

# 98. Plan Schema

```json
{
  "plan_id": "string",
  "task_ref": "string",
  "operator_nodes": [],
  "edges": [],
  "bridge_refs": [],
  "observer_refs": [],
  "guards": [],
  "checkpoints": [],
  "fallbacks": [],
  "stop_policy": {},
  "budget": {},
  "status": "candidate|legal|executing|completed|failed|reopened",
  "version": "string"
}
```

---

# 99. Runtime Event Schema

```json
{
  "event_id": "string",
  "event_type": "string",
  "time": "string",
  "actor_ref": "string",
  "object_refs": [],
  "input_refs": [],
  "output_refs": [],
  "decision": {},
  "residuals": [],
  "cost": {},
  "version": "string"
}
```

---

# 100. Benchmark Case Schema

```json
{
  "benchmark_id": "string",
  "level": "B0|B1|B2|B3|B4|B5|B6|B7",
  "corpus_refs": [],
  "task_ref": "string",
  "positive_controls": [],
  "negative_controls": [],
  "adversarial_controls": [],
  "observer_matrix_ref": "string",
  "scoring_policy_ref": "string",
  "runtime_version": "string",
  "version": "string"
}
```

---

# 101. Canonical Scholarship Adapter

定義：

$$
\boxed{
A_{canon}.
}
$$

GCORF runtime 可以向外部 canonical system 送出：

- paper；
- provenance；
- validation；
- schemas；
- version proposal。

---

# 102. Canonical Authority Boundary

核心：

$$
\boxed{
PortableArtifact
\neq
CanonicalCommit.
}
$$

---

# 103. Revision Authority

只有實際 canonical runtime 可以回傳：

$$
\boxed{
RevisionID,
DocumentHash,
CommitStatus.
}
$$

---

# 104. SSSP MCP Adapter

對 SSSP MCP，可建立：

$$
\boxed{
A_{SSSP}.
}
$$

但 GCORF 本身不捏造其 revision。

---

# 105. Import Flow

概念上：

$$
\boxed{
PortableHandoff
\rightarrow
SSSP\ Import
\rightarrow
Validate
\rightarrow
Commit
\rightarrow
CanonicalRef.
}
$$

---

# 106. Export Flow

$$
\boxed{
CanonicalRef
\rightarrow
Export
\rightarrow
Diff
\rightarrow
PortablePackage.
}
$$

---

# 107. Runtime Security Principle

研究系統中的外部內容應遵守：

$$
\boxed{
Content
\neq
Authority.
}
$$

---

# 108. Runtime Audit Principle

任何高影響決策至少保存：

$$
\boxed{
WhyThisRoute?
}
$$

---

# 109. Explainable Routing

Router 應輸出：

- selected operators；
- rejected alternatives；
- hard guards；
- trade-offs；
- uncertainty。

---

# 110. Router Self-Observation

GCORF-06 要求：

$$
\boxed{
Router
\in
Domain(
MetaObservation
).
}
$$

---

# 111. Router Benchmarking

不同 Router：

$$
P_1,P_2
$$

可在相同 benchmark 上比較。

---

# 112. Router Is Not Final

$$
\boxed{
\Pi_t
\Rightarrow_E
\Pi_{t+1}.
}
$$

---

# 113. Runtime Lifecycle

Runtime 版本本身：

$$
Experimental
\rightarrow
Validated
\rightarrow
CanonicalCandidate
\rightarrow
Reopened.
$$

---

# 114. Backward Compatibility

新 schema / operator version 需標：

$$
\boxed{
Compatibility.
}
$$

---

# 115. Migration

資料模型變動要有：

$$
\boxed{
MigrationTrace.
}
$$

---

# 116. No Silent Migration

禁止 migration 靜默改變：

- license；
- evidence；
- formula；
- operator identity。

---

# 117. GCORF-09 核心公理候選

### RT-A1 — Runtime–Model Separation

Runtime 不等於單一 AI model。

### RT-A2 — Guard Priority

$$
Guard>Utility.
$$

### RT-A3 — Event Provenance

高影響 state change 必須可由 event log 追溯。

### RT-A4 — Typed Routing

operator route 必須有型別與 interface guard。

### RT-A5 — No Silent Downgrade

claim type 降級必須顯式標記。

### RT-A6 — Benchmark Multidimensionality

benchmark 不得只用單一總分代表全部能力。

### RT-A7 — Control Requirement

成熟 benchmark 應有 negative / adversarial controls。

### RT-A8 — Runtime Reopenability

router、schema、benchmark、operator registry 均可重新打開。

### RT-A9 — External Authority Boundary

外部 canonical commit 狀態不得由 portable runtime自行宣稱。

### RT-A10 — Implementation Non-Finality

Reference Runtime 不是唯一合法實作。

---

# 118. 主要失效模式

1. **Prompt Monolith**：把整個 GCORF 壓成一個巨大 prompt；
2. **Model–Runtime Conflation**：把模型能力當 runtime 能力；
3. **Guard Bypass**：高 utility route 越過 license；
4. **Silent Coercion**：型別不合卻暗中轉換；
5. **Silent Claim Downgrade**：formal failure 後輸出 heuristic 卻不標；
6. **Provenance Gap**：final answer 無法追回 evidence；
7. **Benchmark Overfit**：router 只針對固定 benchmark；
8. **Single-Score Collapse**：多維 benchmark 被壓成一個排名；
9. **Negative-Control Omission**：不知道 false positive；
10. **Event Loss**：只存 final state；
11. **Canonical State Fabrication**：portable artifact 冒充 commit；
12. **Migration Corruption**：schema migration 改了語義；
13. **Tool Authority Injection**：外部內容被誤當指令；
14. **Router Lock-In**：歷史成功路線壟斷未來探索。

---

# 119. 與 GCORF-U 的接口

GCORF-09 已使 GCORF 成為可執行 runtime architecture。

最後需要：

$$
\boxed{
GCORF-U
}
$$

把 00–09 重新統合成：

- 單一理論狀態；
- 正典公理；
- 依賴圖；
- 統一 runtime equation；
- domain realization policy；
- core revision governance；
- v0.1 封版狀態。

---

# 120. 結論

GCORF-09 完成了從理論到 runtime 的最後接口。

整體執行鏈可寫成：

$$
\boxed{
Task
\rightarrow
Guard
\rightarrow
Route
\rightarrow
Execute
\rightarrow
Observe
\rightarrow
Validate
\rightarrow
Record
\rightarrow
Update.
}
$$

其中 GCORF 的工程精神不是「永遠挑最強 AI」，而是：

$$
\boxed{
\text{挑合法的方法、保留可追溯的過程、讓失敗能被看見、讓整個方法系統可以被重新組合與修正。}
}
$$

最終：

$$
\boxed{
GCORF
\neq
PromptLibrary.
}
$$

它更接近：

$$
\boxed{
Typed\ Research\ Runtime
+
Operator\ Registry
+
Epistemic\ Guard
+
Recursive\ Validation\ System.
}
$$

只要這四層真正落地，GCORF 就能從人物逆向實驗擴展為可持續累積與重新編譯研究方法的基礎設施。
---

# v0.1.1 RMRM v0.8 Feedback Patch — State Compiler, Research Assets, and Diagnostic Routing

## P09.1 Revision trigger

RMRM v0.5–v0.8 expanded from method fingerprints into an audited mathematical research system. Three abstractions survive domain removal and strengthen the GCORF reference runtime:

1. reusable research/cognitive assets;
2. diagnostic-regime routing;
3. research-state compilation and integration debt.

## P09.2 Extended Reference Runtime

GCORF-09 v0.1.1 extends:

$$
\mathcal R_{GC}
$$

to:

$$
\boxed{
\mathcal R_{GC}^{0.1.1}
=
(
\mathcal D,
\mathcal E,
\mathcal O,
\mathcal S,
\mathcal L,
\mathcal B,
\mathcal V,
\mathcal T,
\mathcal P,
\mathcal A,
\mathcal C_S,
\mathcal H_A
).
}
$$

where:

- $\mathcal C_S$: Research-State Compiler;
- $\mathcal H_A$: Reusable Asset / Hub Registry.

## P09.3 Diagnostic-Regime Router

Before selecting a concrete operator plan, the Router may apply:

$$
\boxed{
D:
S
\rightarrow
\{
R_1,\ldots,R_k
\},
}
$$

with:

$$
\boxed{
R_i
\mapsto
M_i,
}
$$

where $M_i$ is a preferred method family for that diagnostic regime.

This is a router pattern, not a mandatory universal operator.

## P09.4 Research-State Compiler

The State Compiler transforms distributed execution traces into the next coherent shared state:

$$
\boxed{
\mathcal C_S:
(
r_1,\ldots,r_N
)
\mapsto
S_t^{\mathrm{compiled}}.
}
$$

It must preserve:

- active frontier;
- accepted claims;
- unresolved claims;
- rejected branches + reasons;
- dependency graph;
- integration debt;
- reusable assets;
- observer disagreements;
- license states;
- version/provenance.

## P09.5 Discovery IR

The runtime adds:

$$
\boxed{
\mathcal D_{\mathrm{IR}}
=
\{
questions,
failed\ attempts,
special\ cases,
diagnostics,
constraints,
local\ results,
branch\ states
\}.
}
$$

A certification compiler may produce:

$$
\boxed{
\operatorname{CertCompile}(
\mathcal D_{\mathrm{IR}}
)
=
\mathcal C_{\mathrm{artifact}},
}
$$

but must not overwrite the discovery IR.

## P09.6 Reusable Asset Registry

A result becomes a reusable asset only if it has observable reuse value.

A candidate hub:

$$
\boxed{
\{P_i\}_{i=1}^{m}
\rightarrow
H
\rightarrow
\{Q_j\}_{j=1}^{n}
}
$$

should demonstrate at least:

1. multiple independent interfaces;
2. core machinery reuse;
3. observable search-cost reduction.

Thus:

$$
\boxed{
\text{important result}
\not\Rightarrow
\text{research/cognitive hub}.
}
$$

An asset can be:

- theorem / lemma;
- representation;
- operator;
- dataset;
- software;
- protocol;
- ontology;
- experimental pipeline;
- validated state-space;
- reusable prompt-independent method record.

## P09.7 Hub Leverage Profile

Optional profile:

$$
\boxed{
\mathbf H(H)
=
(
H_{\mathrm{breadth}},
H_{\mathrm{depth}},
H_{\mathrm{reuse}},
H_{\mathrm{costred}}
).
}
$$

## P09.8 Integration Audit

Before a distributed result is marked complete, runtime should evaluate:

$$
\boxed{
\mathbf D_{\mathrm{int}}
}
$$

from GCORF-04 v0.1.1.

This prevents:

$$
\boxed{
\text{all local modules passed}
\Rightarrow
\text{global artifact coherent}
}
$$

from being silently assumed.

## P09.9 Quantitative Interface Engineering

RMRM v0.8 O37:

$$
P
\rightarrow
B_{\mathrm{control}}
\rightarrow
Q_P
\rightarrow
\text{tractable control}
$$

is retained as a high-value **RMRM domain operator seed**.

GCORF core does not promote O37 to a universal axiom because GCORF-02/03 already provide the generic interface, metric, bound, and routing machinery needed to represent it.

## P09.10 Runtime patch decision

Promoted to core runtime:
- Research-State Compiler;
- Discovery IR / Certification separation;
- Integration Debt audit;
- Reusable Asset Registry.

Retained as domain/operator-library extensions:
- Understanding/Uptake state;
- Quantitative Interface Engineering;
- specific mathematical hub types.
