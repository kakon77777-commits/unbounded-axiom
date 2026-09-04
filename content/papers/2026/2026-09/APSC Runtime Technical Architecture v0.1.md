# APSC Runtime Technical Architecture v0.1

**Adaptive Possibility-Space Cognition Runtime — Canonical Engineering Architecture, Contracts, Control Loop, and MVP Roadmap**

**文件類型：技術白皮書 01 / 02**  
**系列：Adaptive Possibility-Space Cognition（APSC）**  
**版本：v0.1**  
**日期：2026-08-24**  
**作者：Neo.K**  
**機構：EveMissLab / EVEMISS Technology**

---

## 0. 文件定位

本文件是 APSC 六篇理論論文的第一份統一工程母文件。

它不新增平行母理論，而是把下列理論物件轉成可執行 Runtime：

1. Constrained Possibility Space；
2. Multi-Scale Future Expansion；
3. Counterfactual Observation Expansion（COE）；
4. Finite Cognitive Spacetime；
5. Adaptive Computation Control；
6. Cognitive Operating Profile（COP）；
7. Replayable Cognitive Evidence。

本文件的直接工程目標是：

$$
\boxed{
\text{將「AI 怎麼想」從隱式行為轉成可定址、可約束、可調度、可重播的 Runtime 狀態。}
}
$$

---

# 1. 一句話架構

APSC Runtime 的第一版可以收斂為：

$$
\boxed{
\text{Neural Adapter}
+
\text{State Kernel}
+
\text{Possibility Graph}
+
\text{Constraint Engine}
+
\text{Operator Runtime}
+
\text{COE Engine}
+
\text{Budget Controller}
+
\text{COP Manager}
+
\text{Receipt / Replay Layer}
}
$$

其核心控制流為：

$$
Observation
\rightarrow
State
\rightarrow
PossibilitySpace
\rightarrow
CandidateCognition
\rightarrow
ValueEstimate
\rightarrow
BudgetGate
\rightarrow
Execute
\rightarrow
Receipt
\rightarrow
Update
\rightarrow
StopOrContinue.
$$

---

# 2. 核心工程不變量

## 2.1 Neural Core 不是 Runtime State

神經模型只是一個：

$$
ProposalEngine.
$$

它可以提出：

- 候選狀態；
- 候選分支；
- 候選觀察；
- 候選策略；
- 候選抽象；
- 候選驗證方式。

但不能直接改寫 canonical state。

因此：

$$
\boxed{
NeuralProposal
\neq
CanonicalMutation.
}
$$

---

## 2.2 Observation 不等於 Truth

任何外部觀察都先形成：

$$
ObservationRecord.
$$

不得直接等於：

$$
WorldTruth.
$$

因此：

$$
\boxed{
Observation
\neq
Truth.
}
$$

---

## 2.3 Candidate 不等於 Active Branch

候選分支進入 Runtime 後，必須通過約束與資源檢查。

$$
CandidateBranch
\neq
ActiveBranch.
$$

---

## 2.4 Decision 不等於 Commit

控制器提出決策後，仍可能因：

- verifier；
- budget；
- safety；
- user preference；
- deadline；
- rule；

被拒絕或延後。

因此：

$$
\boxed{
Decision
\neq
Commit.
}
$$

---

## 2.5 Profile Label 不等於 Canonical Policy

UI 顯示：

```text
Fast
Accurate
Research
Safe
Explore
```

只是 preset。

Runtime 必須保存：

$$
\Theta.
$$

所以：

$$
ModeLabel
\neq
CanonicalCOP.
$$

---

# 3. Runtime 分層

第一版分成九層：

```text
L0  External / Neural Adapters
L1  Observation & Input Normalization
L2  Canonical State Kernel
L3  Possibility Graph & Constraint Engine
L4  Cognitive Operator Runtime
L5  COE / Active Observation Engine
L6  Adaptive Computation Controller
L7  Cognitive Operating Profile Manager
L8  Receipt / Replay / Audit Layer
```

---

# 4. L0：External / Neural Adapters

## 4.1 Neural Adapter

每個模型供應商只需實作統一介面：

```text
propose_state()
propose_branches()
propose_observations()
propose_abstraction()
propose_action()
```

Runtime 不依賴某一特定模型。

---

## 4.2 Tool Adapter

外部工具統一為：

```text
observe()
verify()
simulate()
execute()
```

每個工具必須宣告：

- input schema；
- output schema；
- cost estimate；
- latency class；
- side-effect class；
- retry policy；
- trust / reliability metadata。

---

# 5. L1：Observation & Input Normalization

## 5.1 ObservationRecord

第一版 canonical object：

```json
{
  "observation_id": "obs://...",
  "source": "sensor|tool|user|model|world",
  "timestamp": "...",
  "payload": {},
  "reliability": 0.0,
  "cost": {},
  "side_effect": "none|possible|confirmed",
  "provenance": {}
}
```

---

## 5.2 Observation Status

觀察狀態：

```text
RAW
NORMALIZED
SUPPORTED
CONTRADICTED
UNRESOLVED
SUPERSEDED
```

---

# 6. L2：Canonical State Kernel

## 6.1 StateObject

核心狀態：

$$
S_t
=
(
X_t,
R_t,
C_t,
O_t,
B_t
).
$$

工程表示可拆為：

```text
StateSnapshot
EntityState
RuleState
CausalState
ObservationState
BudgetState
```

---

## 6.2 Unknown 必須顯式表示

欄位不可用：

```text
null
```

隨意混合：

- unknown；
- unavailable；
- not applicable；
- not observed。

應使用：

```text
KNOWN
UNKNOWN
UNCERTAIN
NOT_APPLICABLE
UNAVAILABLE
```

---

## 6.3 State Versioning

每次 canonical mutation：

$$
S_t
\rightarrow
S_{t+1}
$$

必須產生：

```text
state_version
parent_state_version
mutation_receipt
```

---

# 7. L3：Possibility Graph

## 7.1 PossibilityNode

每個可能節點至少包含：

```json
{
  "node_id": "poss://...",
  "parent_ids": [],
  "state_ref": "state://...",
  "horizon": 0,
  "resolution": "near|mid|far",
  "probability": null,
  "risk": null,
  "decision_value": null,
  "reachability": "supported|contradicted|undetermined",
  "status": "candidate|active|dormant|pruned|merged|committed"
}
```

---

## 7.2 PossibilityEdge

邊表示：

```text
ACTION
EVENT
OBSERVATION_UPDATE
COUNTERFACTUAL_INTERVENTION
ABSTRACTION
REFINEMENT
MERGE
```

---

## 7.3 Graph 不要求樹

當兩條路徑進入等價狀態：

$$
S_a
\sim_G
S_b,
$$

可以執行：

$$
Merge.
$$

所以 Runtime 使用 DAG / general graph，而不是固定 tree。

---

# 8. Constraint Engine

## 8.1 Rule Classes

```text
HARD
SOFT
PROBABILISTIC
UNKNOWN
```

---

## 8.2 ConstraintResult

```json
{
  "constraint_id": "rule://...",
  "target": "poss://...",
  "status": "pass|fail|undetermined",
  "severity": "hard|soft",
  "reason_code": "...",
  "evidence_refs": []
}
```

---

## 8.3 Constraint Projection

候選空間：

$$
\widetilde{\Omega}
$$

經過：

$$
\Pi_{\mathcal K}
$$

得到：

$$
\widehat{\Omega}.
$$

工程流程：

```text
candidate
→ hard-rule check
→ causal compatibility
→ reachability
→ risk annotation
→ budget relevance
→ active / dormant / prune
```

---

# 9. Reachability Engine

第一版不要求通用規劃器。

只提供統一 contract：

```text
check_reachability(state, target, horizon, budget)
```

回傳：

```text
SUPPORTED
CONTRADICTED
UNDETERMINED
```

及可選：

```text
witness_path
blocking_constraints
required_resources
```

---

# 10. Multi-Scale Horizon Manager

## 10.1 三層 Horizon

```text
NEAR
MID
FAR
```

---

## 10.2 Resolution Policy

一般規則：

$$
h\uparrow
\Rightarrow
Resolution\downarrow.
$$

但可局部 refine。

---

## 10.3 Near

保留：

- explicit state；
- explicit action；
- local causal transition。

---

## 10.4 Mid

轉為：

```text
ScenarioFamily
```

---

## 10.5 Far

轉為：

```text
Attractor
Region
MacroState
```

---

# 11. L4：Cognitive Operator Runtime

## 11.1 Operator Registry

第一版 operator：

```text
expand
counterfactual_intervene
counterfactual_observe
observe
verify
prune
merge
abstract
refine
backtrack
reframe
profile_shift
commit
```

---

## 11.2 OperatorSpec

每個 operator 必須宣告：

```json
{
  "operator_id": "cog://expand@0.1",
  "input_types": [],
  "output_types": [],
  "cost_model": {},
  "side_effect_class": "none",
  "preconditions": [],
  "postconditions": [],
  "interruptible": true,
  "checkpointable": true
}
```

---

# 12. Operator Invocation

任何認知操作都建立：

```text
CognitiveOperation
```

包含：

```text
operation_id
operator_id
state_ref
goal_ref
profile_ref
budget_before
estimated_value
estimated_cost
status
```

---

# 13. Operator Status

```text
PROPOSED
QUEUED
RUNNING
PAUSED
PREEMPTED
COMPLETED
FAILED
CANCELLED
```

---

# 14. L5：COE Engine

## 14.1 Candidate Observation Generation

$$
\mathfrak Q
:
(B_t,G_t,\widehat{\Omega}_t)
\rightarrow
\mathcal Q_t.
$$

工程輸出：

```text
ObservationCandidate[]
```

---

## 14.2 ObservationCandidate

```json
{
  "query_id": "query://...",
  "target": "...",
  "expected_outcomes": [],
  "estimated_information_gain": null,
  "estimated_decision_value": null,
  "estimated_risk_reduction": null,
  "estimated_cost": {},
  "observer_effect": "none|possible|likely"
}
```

---

# 15. COE Expansion

對觀察 $q$：

$$
\mathfrak O_q^{CF}
(
\widehat{\Omega}_t
)
=
\{
(o_i,p_i,\widehat{\Omega}_{t|o_i})
\}.
$$

第一版允許：

- discrete outcomes；
- bounded continuous bins；
- symbolic outcomes。

---

# 16. Observation Value

統一值函數：

$$
V_{obs}(q)
=
w_I IG(q)
+
w_D DROV(q)
+
w_R RiskReduction(q)
+
w_C Compression(q)
-
w_K Cost(q).
$$

權重由 COP 提供。

---

# 17. L6：Adaptive Computation Controller

## 17.1 Candidate Cognitive Queue

每輪建立：

$$
\mathcal U_t^{candidate}.
$$

然後過濾：

$$
\mathcal U_t^{feasible}
=
\{
u
|
C(u)\preceq B_t
\}.
$$

---

## 17.2 Value Estimator

每個候選：

$$
\widehat{\Delta Q}(u).
$$

計算：

$$
Score(u)
=
\widehat{\Delta Q}(u)
-
\lambda^\top C(u).
$$

---

# 18. Marginal Value of Cognition

$$
MVC(u)
=
\frac{
\widehat{\Delta Q}(u)
}{
ScalarCost(u)
}.
$$

MVC 是第一版 scheduler 的主要排序訊號之一。

---

# 19. Dynamic Shadow Price

每種資源：

$$
\lambda_i
=
f(
B_i,
Deadline,
COP,
Risk
).
$$

當：

$$
B_i\downarrow,
$$

通常：

$$
\lambda_i\uparrow.
$$

---

# 20. Scheduler

第一版 scheduler：

```text
filter infeasible
→ apply hard gates
→ score candidates
→ urgency adjustment
→ risk adjustment
→ choose top action
```

---

# 21. Preemption

若新操作：

$$
Score(u_b)-Score(u_a)>\tau_p,
$$

可以搶佔：

$$
u_a.
$$

前提：

```text
interruptible = true
```

---

# 22. Checkpoint

可搶佔操作應支援：

```json
{
  "checkpoint_id": "ckpt://...",
  "operation_id": "...",
  "state_ref": "...",
  "open_branches": [],
  "evidence_refs": [],
  "resume_token": "..."
}
```

---

# 23. Stop Policy

主動停止：

$$
\max_u
Score(u)
\leq
\epsilon.
$$

則：

```text
STOP_COGNITION
```

---

# 24. Commit Policy

提交至少考慮：

$$
Stability
$$

$$
Risk
$$

$$
ExpectedFurtherGain.
$$

第一版：

$$
Commit=1
$$

若：

$$
Stability\geq\tau_s,
$$

$$
Risk\leq\tau_r,
$$

$$
ExpectedFurtherGain\leq\tau_g.
$$

---

# 25. L7：COP Manager

## 25.1 Canonical COP

第一版十維：

$$
\Theta
=
(
\theta_d,
\theta_b,
\theta_v,
\theta_{cf},
\theta_o,
\theta_r,
\theta_l,
\theta_a,
\theta_c,
\theta_n
).
$$

---

## 25.2 COP Object

```json
{
  "cop_id": "cop://...",
  "depth": 0.5,
  "breadth": 0.5,
  "verification": 0.5,
  "counterfactual": 0.5,
  "observation": 0.5,
  "risk": 0.5,
  "latency": 0.5,
  "abstraction": 0.5,
  "commitment": 0.5,
  "novelty": 0.5
}
```

---

# 26. COP Sources

有效 Profile 由：

```text
user preference
task profile
system hard constraints
adaptive proposal
```

合成。

---

# 27. Adaptive Region

AI 自調範圍：

$$
\mathcal A
=
[\Theta_{min},\Theta_{max}].
$$

---

# 28. Profile Shift

重要 shift 必須：

```text
PROPOSE
→ PROJECT_TO_FEASIBLE_REGION
→ APPLY
→ RECEIPT
```

---

# 29. Hysteresis

避免頻繁切換：

$$
|\Delta Trigger|
>
\tau_h.
$$

否則不 shift。

---

# 30. L8：Receipt Layer

## 30.1 DecisionReceipt

```json
{
  "receipt_id": "receipt://decision/...",
  "state_ref": "...",
  "selected_operation": "...",
  "alternatives": [],
  "budget_before": {},
  "budget_after": {},
  "cop_ref": "...",
  "commit": false
}
```

---

## 30.2 ProfileReceipt

```json
{
  "receipt_id": "receipt://profile/...",
  "old_cop": "...",
  "new_cop": "...",
  "trigger": "...",
  "reason_code": "...",
  "authorized_region": {}
}
```

---

## 30.3 ObservationReceipt

保存：

```text
query
expected outcomes
actual outcome
estimated value
realized value
cost
```

---

# 31. Replay Layer

Runtime 應輸出：

```text
run_manifest.json
events.jsonl
operations.jsonl
observations.jsonl
budgets.jsonl
profiles.jsonl
receipts.jsonl
final_state.json
```

---

# 32. Private Reasoning Boundary

Runtime 不需要保存：

```text
private chain-of-thought
hidden model scratchpad
```

需要保存的是：

```text
selected operator
public justification code
state transition
budget transition
external observation
receipt
```

因此：

$$
Replayability
\not\Rightarrow
PrivateReasoningDisclosure.
$$

---

# 33. Canonical Runtime Objects

v0.1 最小 canonical objects：

```text
RunManifest
Goal
ObservationRecord
StateSnapshot
Rule
ConstraintResult
PossibilityNode
PossibilityEdge
CognitiveOperation
ObservationCandidate
BudgetState
CognitiveOperatingProfile
Checkpoint
DecisionReceipt
ProfileReceipt
ObservationReceipt
FinalCommit
```

---

# 34. ID Namespace

建議：

```text
run://
goal://
obs://
state://
rule://
poss://
cog://
query://
budget://
cop://
ckpt://
receipt://
commit://
```

---

# 35. Runtime State Machine

主 Runtime 狀態：

```text
INIT
OBSERVE
STATE_BUILD
GENERATE
CONSTRAIN
ROUTE_COGNITION
EXECUTE
UPDATE
EVALUATE_STOP
COMMIT
DONE
FAILED
```

---

# 36. 主循環

```text
INIT
→ ingest goal / COP / budget
→ OBSERVE
→ normalize observations
→ STATE_BUILD
→ construct canonical state
→ GENERATE
→ propose possibilities
→ CONSTRAIN
→ project to working possibility space
→ ROUTE_COGNITION
→ select operator
→ EXECUTE
→ UPDATE
→ emit receipts
→ EVALUATE_STOP
→ continue / commit
```

---

# 37. API Surface

第一版建議：

```text
POST /runs
GET  /runs/{id}
POST /runs/{id}/observe
POST /runs/{id}/step
POST /runs/{id}/pause
POST /runs/{id}/resume
POST /runs/{id}/commit
GET  /runs/{id}/state
GET  /runs/{id}/possibilities
GET  /runs/{id}/budget
GET  /runs/{id}/profile
PATCH /runs/{id}/profile
GET  /runs/{id}/receipts
GET  /runs/{id}/replay
```

---

# 38. Step Contract

`POST /runs/{id}/step`

輸入：

```json
{
  "max_operations": 1,
  "allow_external_observation": true
}
```

輸出：

```json
{
  "selected_operation": "...",
  "status": "...",
  "state_ref": "...",
  "budget_ref": "...",
  "receipt_ref": "..."
}
```

---

# 39. Budget Contract

```json
{
  "wall_ms": 10000,
  "compute_units": 100,
  "memory_units": 50,
  "observation_units": 10,
  "external_units": 5,
  "risk_ceiling": 0.2
}
```

---

# 40. COP Presets

Preset 只是 convenience：

```text
single_turn_accuracy
exploration
low_latency
high_risk_assurance
research
balanced
```

Runtime 仍保存展開後的完整 $\Theta$。

---

# 41. Failure Model

## 41.1 State Failure

```text
STATE_UNRESOLVED
STATE_CONTRADICTION
STATE_SCHEMA_ERROR
```

---

## 41.2 Constraint Failure

```text
HARD_RULE_FAIL
CAUSAL_CONFLICT
REACHABILITY_FAIL
```

---

## 41.3 Cognitive Failure

```text
OPERATOR_FAILED
OPERATOR_TIMEOUT
CHECKPOINT_FAILED
PREEMPTION_FAILED
```

---

## 41.4 Observation Failure

```text
OBSERVATION_UNAVAILABLE
OBSERVATION_UNRELIABLE
OBSERVER_EFFECT_BLOCKED
```

---

## 41.5 Budget Failure

```text
BUDGET_EXHAUSTED
DEADLINE_REACHED
EXTERNAL_QUOTA_EXHAUSTED
```

---

# 42. Graceful Degradation

當資源下降：

```text
reduce breadth
→ raise abstraction
→ reduce far-horizon detail
→ defer low-value verify
→ freeze dormant branches
→ minimal viable commit
```

---

# 43. Safety / Governance Gate

第一版 Runtime 至少應具備：

```text
external action allowlist
side-effect classification
budget ceiling
observation permission
COP hard minimum / maximum
manual pause
manual cancel
manual commit override
```

---

# 44. Model Independence

核心 Kernel 不應要求某家模型 SDK。

Agent Adapter 使用：

```text
provider-neutral interface
```

---

# 45. Deterministic Core

能 deterministic 的部分應 deterministic：

- schema validation；
- budget accounting；
- state versioning；
- rule checking；
- receipt generation；
- replay manifest；
- scheduler tie-breaking with seed。

---

# 46. Stochastic Boundary

模型 proposal 可不確定，但必須被包進：

```text
ProposalRecord
```

並保存：

```text
model_id
model_version
seed if available
request hash
response hash
```

---

# 47. Metrics

Runtime 本身輸出：

$$
Q_{\mathrm{decision}},
$$

$$
C_{\mathrm{compute}},
$$

$$
T_{\mathrm{wall}},
$$

$$
C_{\mathrm{obs}},
$$

$$
Recall_{\mathrm{critical}},
$$

$$
R_{\mathrm{alloc}},
$$

$$
R_{\mathrm{obs}},
$$

$$
R_{\mathrm{commit}}.
$$

---

# 48. Telemetry

本地 telemetry 至少包含：

```text
active nodes
dormant nodes
pruned nodes
current horizon
current COP
remaining budget
current operation
decision stability
expected further gain
```

---

# 49. Dashboard

第一版 Dashboard 不需華麗。

頁面：

```text
Overview
State
Possibility Graph
Operators
Observations
Budget
COP
Receipts
Replay
```

---

# 50. Possibility Graph View

至少顯示：

- active；
- dormant；
- pruned；
- merged；
- near / mid / far；
- risk；
- reachability；
- decision value。

---

# 51. COP Control View

UI 支援：

```text
preset selector
advanced sliders
adaptive toggle
adaptive min / max
profile shift history
```

---

# 52. Minimal Neural Integration

MVP 可以只接一個模型。

要求：

```text
JSON structured proposal
bounded branch count
bounded observation candidate count
bounded abstraction candidates
```

---

# 53. Branch Cap

第一版必須硬限制：

$$
N_{\mathrm{active}}
\leq
N_{\max}.
$$

避免模型一次生成無限候選。

---

# 54. Horizon Cap

$$
h
\leq
h_{\max}.
$$

但可以用 abstract node 表示更遠期。

---

# 55. COE Cap

$$
|\mathcal Q_t|
\leq
Q_{\max}
$$

以及：

$$
|\mathcal O(q)|
\leq
O_{\max}.
$$

---

# 56. Verification Cap

每輪：

$$
N_{verify}
\leq
V_{\max}.
$$

---

# 57. Runtime Acceptance Gates

## Gate A：Schema Integrity

所有 canonical object 必須通過 schema。

## Gate B：State Versioning

任何 mutation 都必須有 parent version。

## Gate C：No Direct Neural Mutation

模型 proposal 不可直接改 canonical state。

## Gate D：Budget Monotonicity

已消耗資源不可無故增加回來。

## Gate E：Constraint Enforcement

Hard Rule fail 不可進 active space。

## Gate F：COE Boundedness

觀察候選與 outcome 必須有上限。

## Gate G：Preemption Safety

搶佔後可恢復或明確標記不可恢復。

## Gate H：COP Boundary

Adaptive shift 不可離開授權區域。

## Gate I：Receipt Completeness

重要決策必須有 receipt。

## Gate J：Replay Integrity

同一 deterministic core 輸入可重播。

## Gate K：Commit Gate

未通過 commit policy 不得自動 final commit。

---

# 58. MVP v0.1 的完成定義

MVP v0.1 不要求完整 AGI。

只需證明：

1. 可以建立 canonical state；
2. 可以生成有限 possibility graph；
3. 可以執行 constraint projection；
4. 可以在至少 5 種 cognition operator 間選擇；
5. 可以計算 budget；
6. 可以執行 COE 的簡化版本；
7. 可以切換 COP；
8. 可以主動 stop / commit；
9. 可以輸出 receipts；
10. 可以完整 replay。

---

# 59. MVP Operator Scope

v0.1 建議只做：

```text
expand
observe
verify
prune
abstract
commit
```

第二輪再加入：

```text
counterfactual_intervene
merge
refine
backtrack
reframe
profile_shift
```

---

# 60. MVP COE Scope

第一版只支援：

```text
discrete observation candidates
bounded outcomes
heuristic DROV
simple cost
```

不要求完整 causal Bayesian model。

---

# 61. MVP Controller

第一版可以使用：

$$
Score(u)
=
w_q \widehat{\Delta Q}(u)
-
\lambda^\top C(u).
$$

先用 heuristic estimator。

之後再學習：

$$
\widehat{\Delta Q}.
$$

---

# 62. MVP COP

先提供 5 個 preset：

```text
balanced
single_turn_accuracy
exploration
low_latency
high_risk_assurance
```

外加 advanced JSON。

---

# 63. MVP Demo Task

建議第一個 demo 不直接做複雜遊戲。

先做：

**Hidden-State Route Planning**

世界：

```text
graph map
hidden hazard
limited observation
limited verify
multiple routes
deadline
```

AI 必須決定：

- 先走；
- 先觀察；
- 先驗證；
- 剪掉哪些路；
- 何時 commit。

---

# 64. Demo 可測理論

同一任務可以比較：

```text
Fixed Depth
Fixed Search
APSC without COE
APSC with COE
APSC with COP
```

---

# 65. Phase Plan

## Phase 0 — Schema Freeze

完成：

```text
canonical objects
JSON schemas
ID namespace
event types
receipt types
```

---

## Phase 1 — State / Budget Kernel

完成：

```text
StateStore
BudgetManager
RunManifest
versioning
receipts
```

---

## Phase 2 — Possibility Graph

完成：

```text
nodes
edges
constraint engine
reachability interface
prune
abstract
```

---

## Phase 3 — Operator Runtime

完成：

```text
registry
invocation
queue
status
checkpoint
```

---

## Phase 4 — COE

完成：

```text
observation candidates
outcome expansion
value estimate
observe / update
```

---

## Phase 5 — Adaptive Controller

完成：

```text
MVC
scheduler
shadow price
stop
commit
preemption
```

---

## Phase 6 — COP Manager

完成：

```text
profile
presets
adaptive region
shift
receipt
```

---

## Phase 7 — Replay / Dashboard

完成：

```text
events
replay
graph view
budget view
COP view
```

---

## Phase 8 — Benchmark Harness

連接下一份白皮書：

**AI Tension Arena Protocol & Benchmark Specification**。

---

# 66. Repository Layout

建議：

```text
apsc-runtime/
├── README.md
├── pyproject.toml
├── schemas/
├── src/apsc/
│   ├── state/
│   ├── possibility/
│   ├── constraints/
│   ├── operators/
│   ├── coe/
│   ├── controller/
│   ├── cop/
│   ├── budget/
│   ├── receipts/
│   ├── replay/
│   ├── adapters/
│   └── api/
├── tests/
├── examples/
├── benchmarks/
└── docs/
```

---

# 67. 測試策略

至少包含：

```text
unit tests
schema tests
property tests
golden replay tests
budget monotonicity tests
profile boundary tests
preemption tests
failure injection
```

---

# 68. Property Tests

重要 property：

$$
Budget_{t+1}
\preceq
Budget_t
$$

除非有明確 external top-up。

以及：

$$
HardFail(\omega)
\Rightarrow
\omega\notin Active.
$$

以及：

$$
AdaptiveCOP
\in
\mathcal A.
$$

---

# 69. Golden Replay

固定：

```text
seed
world
observations
operator outcomes
```

應得到相同：

```text
state versions
budget trajectory
receipts
final commit
```

---

# 70. 性能目標

v0.1 不追求最大吞吐。

優先順序：

```text
correctness
replayability
boundedness
auditability
then performance
```

---

# 71. 非目標

v0.1 不做：

- 通用世界模型；
- 通用因果發現；
- 完整 POMDP solver；
- 自主訓練大模型；
- 私有 chain-of-thought 儲存；
- 無限制長期自主；
- 現實高風險 actuator。

---

# 72. 可否證工程標準

若 APSC Runtime：

1. 無法比固定 depth baseline 降低資源浪費；
2. COE 無法改善任何觀察選擇；
3. COP 無法穩定改變可預測行為；
4. Replay 無法重現 deterministic core；
5. Budget accounting 不可靠；

則 v0.1 架構需要被修正，而不是只增加更多模組。

---

# 73. 第一版最小成功條件

可以用一個最小公式表示：

$$
\boxed{
\text{same model}
+
\text{same task}
+
\text{different COP / controller}
\Rightarrow
\text{measurably different, replayable cognitive trajectory}.
}
$$

並且：

$$
\boxed{
\text{adaptive controller}
\text{ 在至少一類任務中}
>
\text{fixed cognition baseline}.
}
$$

---

# 74. 與第二份白皮書的邊界

本文件只定義：

$$
APSC\ Runtime.
$$

下一份：

**AI Tension Arena Protocol & Benchmark Specification**

負責：

- arena world contract；
- multi-agent episode；
- fairness；
- scoring；
- benchmark tasks；
- replay comparison；
- leaderboard；
- experimental matrix。

---

# 75. 最終架構總結

APSC Runtime 的工程母式：

$$
\boxed{
O_t
\rightarrow
S_t
\rightarrow
\widetilde{\Omega}_t
\rightarrow
\Pi_{\mathcal K}
\rightarrow
\widehat{\Omega}_t
\rightarrow
\mathcal U_t
\rightarrow
\mathcal C
\rightarrow
u_t^\ast
\rightarrow
S_{t+1}
}
$$

其中：

$$
\mathcal C
=
f(
Budget,
COP,
Risk,
Deadline,
ExpectedValue
).
$$

觀察候選則透過：

$$
\mathfrak O^{CF}
$$

加入 cognition queue。

---

# 76. 結論

APSC Runtime 的目的不是重新建立一個神經模型，也不是建立一個與 LLM 平行的「邏輯 AI」。

它建立的是一個位於模型與世界之間的：

$$
\boxed{
\text{cognitive control runtime}.
}
$$

神經模型負責提出候選。

Runtime 負責：

> 哪些候選可以成立？  
> 哪些值得展開？  
> 哪些應觀察？  
> 哪些應驗證？  
> 哪些應剪枝？  
> 哪些應抽象？  
> 下一單位資源該花在哪裡？  
> Profile 是否需要改變？  
> 現在是否已經值得停止？  
> 最終決策是否可以提交？

因此：

$$
\boxed{
\text{Neural intelligence generates possibilities; APSC Runtime governs cognition over them.}
}
$$

這份白皮書固定了第一版工程骨架。

下一份技術白皮書將進入：

**AI Tension Arena Protocol & Benchmark Specification v0.1**

並把本 Runtime 放入真正會反作用的多智能體世界中進行可重播驗證。

---

## 版本記錄

### v0.1 — 2026-08-24

本版首次固定：

1. APSC Runtime 九層工程架構；
2. Neural Proposal / Canonical Mutation 分離；
3. Observation / Truth 分離；
4. Candidate / Active Branch 分離；
5. Decision / Commit 分離；
6. Canonical Runtime Objects；
7. State Kernel；
8. Possibility Graph；
9. Constraint Engine；
10. Reachability Interface；
11. Multi-Scale Horizon Manager；
12. Cognitive Operator Registry；
13. COE Engine；
14. Observation Value；
15. Adaptive Computation Controller；
16. MVC；
17. Dynamic Shadow Price；
18. Scheduler；
19. Preemption；
20. Checkpoint；
21. Stop / Commit Policy；
22. COP Manager；
23. Adaptive Region；
24. Profile Shift / Hysteresis；
25. Decision / Profile / Observation Receipts；
26. Replay Layer；
27. Private Reasoning Boundary；
28. Runtime State Machine；
29. API Surface；
30. Budget Contract；
31. Failure Model；
32. Graceful Degradation；
33. Governance Gate；
34. Deterministic Core；
35. Telemetry / Dashboard；
36. Branch / Horizon / COE / Verification Caps；
37. Acceptance Gate A–K；
38. MVP Completion Definition；
39. MVP Operator Scope；
40. MVP COE Scope；
41. MVP Controller；
42. MVP COP；
43. Hidden-State Route Planning Demo；
44. Phase 0–8 Implementation Plan；
45. Repository Layout；
46. Test Strategy；
47. Property Tests；
48. Golden Replay；
49. Non-goals；
50. Falsification Criteria。
