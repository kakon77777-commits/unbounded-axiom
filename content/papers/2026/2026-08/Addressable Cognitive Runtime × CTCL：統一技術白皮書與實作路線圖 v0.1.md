# Addressable Cognitive Runtime × CTCL：統一技術白皮書與實作路線圖 v0.1
## ——從自提示、可定址認知與契約治理，走向具有時間因果歷史的持續自主 AI Runtime

**系列 06 / 06**

---

## 文件定位

本文是本系列前五篇的**統一技術母文件**。

前五篇分別完成：

1. 從 Self-Prompt 到 Persistent-Goal Autonomous Cognitive Loop 的理論定位；
2. Addressable Cognitive Space、Cognitive Affordance 與 Semantic Address；
3. AI-Native Cognitive Program、Self-Dialogue Runtime 與 Zero-Rendering；
4. CTCL-ITR、Decision Receipt、Decision-Time Knowledge Boundary 與時間因果自我史；
5. Contract-Bounded Autonomy，以及 `EXECUTE / REFUSE / DEFER / IDLE / ESCALATE` 五態治理。

本文不再新增一個平行理論，而是將上述概念收斂為一個可實作的統一架構：

$$
\boxed{
\text{Addressable Cognitive Runtime}
+
\text{Governance Runtime}
+
\text{CTCL-ITR Temporal-Causal Evidence Layer}
}
$$

其目標不是建造一個只會「多 prompt 自己幾次」的 Agent，而是建立：

> **一個只需給予持續目標、環境與契約，即可自行觀察、形成議程、選擇認知、規劃、治理、行動、稽核與更新自己的 AI Runtime。**

---

# 1. 最終研究問題

本系列最終問題可以形式化為：

$$
\boxed{
(G,E_t,C_t)
\rightarrow
AI_t
\rightarrow
AI_{t+1}
}
$$

其中：

- $G$：Persistent Goal；
- $E_t$：Environment；
- $C_t$：Contract / Authority；
- $AI_t$：目前 Runtime 狀態；
- $AI_{t+1}$：AI 自己產生的下一個認知與行動狀態。

核心問題不是：

> AI 能不能回答問題？

而是：

> **若人類停止逐輪提供下一個 prompt，AI 能否自己產生後續 cognition、agenda、plan、governance decision 與 action？**

---

# 2. 統一閉環

完整 Runtime：

$$
\boxed{
\begin{aligned}
Environment_t
&\xrightarrow{Observe}
Observation_t\\
&\xrightarrow{Encode}
SemanticState_t\\
&\xrightarrow{Detect}
Problem/Opportunity/None\\
&\xrightarrow{Agenda}
AgendaCandidate_t\\
&\xrightarrow{Retrieve}
CognitiveAffordances_t\\
&\xrightarrow{Compile}
CognitiveProgram_t\\
&\xrightarrow{Dialectic}
Proposal_t\leftrightarrow Opposition_t\\
&\xrightarrow{Govern}
Decision_t\\
&\xrightarrow{Execute}
Action_t\\
&\xrightarrow{Audit}
TemporalEvidence_t\\
&\xrightarrow{Update}
Memory_{t+1},Commitments_{t+1},Environment_{t+1}.
\end{aligned}
}
$$

並循環：

$$
t\rightarrow t+1.
$$

---

# 3. 三層架構

整體系統分成三個邏輯層。

## Layer A — Cognitive Runtime

回答：

> **現在應該怎麼想？**

核心模組：

```text
Semantic State Encoder
Cognitive Registry
Cognitive Affordance Retriever
Semantic Address Resolver
Cognitive Router
Cognitive Program Compiler
Self-Dialogue Runtime
```

---

## Layer B — Governance Runtime

回答：

> **現在應不應該做？**

核心模組：

```text
Persistent Goal Store
Agenda Runtime
Contract Store
Authority Resolver
Risk / Cost Evaluator
Dialectic Engine
Governance Decision Engine
Commitment Store
```

---

## Layer C — Temporal-Causal Evidence

回答：

> **當時為什麼這樣想、這樣決定、最後有沒有真的作用到世界？**

核心：

```text
CTCL reference instant
CTCL-ITR TemporalEvent
Causal DAG
Decision Receipt
Knowledge Boundary
Commit Receipt
Context Compression Event
Integrity Sidecar / Ledger Anchor
Audit / Replay
```

---

# 4. 第一個總體不變量

整個 Runtime 必須維持：

$$
\boxed{
Cognition
\neq
Governance
\neq
WorldCommit.
}
$$

即：

> 想到一個 action，不代表批准它。

> 批准一個 action，不代表它已經成功作用到世界。

---

# 5. 第二個總體不變量

沿用 CTCL-ITR 的核心分離：

$$
\boxed{
Intent
\neq
Plan
\neq
ExecutionHistory
\neq
Artifact
\neq
WorldCommit.
}
$$

Addressable Cognitive Runtime 不應破壞這個分離。

---

# 6. 第三個總體不變量

$$
\boxed{
Prompt
\neq
Cognition.
}
$$

自然語言 prompt 是：

$$
Renderer(CognitiveObject).
$$

不是 canonical cognition 本身。

---

# 7. 第四個總體不變量

$$
\boxed{
CurrentMemory
\neq
HistoricalLedger.
}
$$

Context 可以壓縮。

Ledger 不應因 working-context 壓縮而失去因果證據。

---

# 8. 第五個總體不變量

$$
\boxed{
Can
\neq
Should
\neq
Authorized.
}
$$

三者不得在 schema、prompt 或 evaluator 中合併。

---

# 9. 第六個總體不變量

$$
\boxed{
DecisionReceipt
\neq
CommitReceipt.
}
$$

Decision Receipt：

> 為什麼決定這樣做？

Commit Receipt：

> 是否真的對世界產生作用？

---

# 10. 現有可復用資產：SES / SPRC

現有 Semantic Persona Runtime / SES-SPRC 已提供：

```text
SPRC Code
→ Registry Decode
→ Seed Lanes
→ Execution Descriptor
→ Operator Program
→ Natural Language
```

這條鏈已經非常接近本文需要的：

$$
SemanticAddress
\rightarrow
CanonicalCognition
\rightarrow
CognitiveProgram
\rightarrow
Renderer.
$$

因此本文不建議棄用 SES/SPRC。

更合理的方向是：

$$
\boxed{
SES/SPRC
\rightarrow
Generalized Cognitive Registry Substrate.
}
$$

---

# 11. SES/SPRC 應保留的特性

至少保留：

- versioned registry；
- registry hash；
- semantic code；
- deterministic seed handling；
- operator-selection lane；
- operator-order lane；
- renderer lane；
- state-mutation lane；
- replay；
- recode；
- corpus / registry separation；
- candidate / promotion boundary。

這些都是未來 Addressable Cognitive Runtime 所需的基礎。

---

# 12. Cognitive Registry v0.1

第一版正式 registry 可定義：

```json
{
  "registry_id": "ACR1",
  "registry_version": "0.1",
  "schema": "acr.cognitive-registry/v0.1",
  "operators": [...]
}
```

每個 operator：

```json
{
  "id": "cog://epistemic/verify@1",
  "name": "VERIFY",
  "version": "1",
  "type": "cognitive_operator",

  "preconditions": [],
  "inputs": [],
  "outputs": [],
  "effects": [],

  "cost_class": "low",
  "risk_class": "low",

  "compatible_with": [],
  "conflicts_with": [],

  "authority_class": "cognition_only",

  "termination": [],

  "renderers": {},
  "vector_ref": null,

  "schema_hash": "sha256:..."
}
```

---

# 13. Cognitive Object Identity

Identity 不應只靠名字。

定義：

$$
Identity(C)
=
(
namespace,
id,
version,
schemaHash
).
$$

例如：

```text
cog://epistemic/verify@1#sha256:...
```

因此：

$$
VERIFY@1
\neq
VERIFY@2.
$$

---

# 14. Cognitive Address Namespace

初步可以分：

```text
cog://epistemic/*
cog://representation/*
cog://search/*
cog://planning/*
cog://control/*
cog://governance/*
cog://memory/*
cog://agenda/*
```

例如：

```text
cog://epistemic/verify@1
cog://epistemic/counterexample@1
cog://representation/reframe@1
cog://planning/decompose@1
cog://control/backtrack@1
cog://control/stop@1
cog://governance/defer@1
cog://governance/refuse@1
```

---

# 15. Semantic State Schema

公開狀態：

$$
O_t
$$

進入：

$$
SemanticStateEncoder.
$$

輸出：

```json
{
  "state_id": "state:sha256:...",

  "goal_refs": [],
  "active_commitments": [],

  "progress": "stalled",
  "uncertainty": "high",

  "failures": [],
  "missing": [],
  "risks": [],

  "budget": {},
  "authority_ref": "...",

  "environment_refs": [],
  "memory_refs": []
}
```

---

# 16. Semantic State 的資料來源

只使用公開、可記錄資訊：

```text
task / goal
public outputs
tool outputs
memory
environment snapshot
artifact state
budget
commitments
contract
authority
explicit confidence
validation results
```

不要求：

> privileged access to hidden chain-of-thought。

---

# 17. Cognitive Affordance Retriever

輸入：

$$
S_t.
$$

輸出：

$$
\mathcal A_c(S_t)
=
\{C_1,\dots,C_k\}.
$$

候選評分可先採：

$$
Score(C_i)
=
w_s SemanticFit
+
w_p PreconditionFit
+
w_h HistoricalUtility
-
w_c Cost
-
w_r Risk.
$$

---

# 18. Retriever v0.1 不必先做神經模型

最初可以：

```text
rule matching
+ keyword/state tags
+ registry preconditions
+ optional embeddings
```

理由：

> 先驗證 Runtime semantics，再優化 routing。

---

# 19. Semantic Address Resolver

Resolver：

$$
resolve(address)
\rightarrow
CanonicalObject.
$$

需要：

- registry validation；
- version resolution；
- schema hash check；
- deprecation handling；
- alias resolution；
- missing operator handling。

---

# 20. Cognitive Router

Retriever 提供候選。

Router 決定：

$$
C^*
=
Route(S_t,\mathcal A_c).
$$

Router 可以是：

- deterministic；
- rule-based；
- LLM；
- learned classifier；
- hybrid。

但輸出必須回到：

$$
CanonicalAddress.
$$

---

# 21. Cognitive Program Schema

```json
{
  "program_id": "cp:...",

  "state_ref": "state:...",
  "goal_refs": [],

  "steps": [
    {
      "operator_ref": "cog://epistemic/verify@1",
      "parameters": {},
      "stop_if": []
    }
  ],

  "budget": {
    "max_steps": 4,
    "max_calls": 6,
    "max_tokens": 4000,
    "max_cost_usd": 0.10
  },

  "termination": [],

  "registry_hash": "..."
}
```

---

# 22. Program Compiler

$$
Compiler(
S_t,
G_t,
M_t,
\mathcal A_c(S_t)
)
\rightarrow
P_t.
$$

輸出不是：

> 一段自由文字。

而是：

$$
CanonicalCognitiveProgram.
$$

---

# 23. Program Validation

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
InvariantCheck.
$$

若不通過：

$$
ProgramRejected.
$$

---

# 24. Self-Dialogue Runtime

Runtime 主循環：

```text
observe
encode
retrieve
route
compile
execute
reobserve
audit
repeat
```

形式：

$$
S_{t,k+1}
=
Observe(
Execute(
\Omega_{t,k},
S_{t,k}
)
).
$$

---

# 25. Fixed 與 Adaptive Program

支援：

$$
FixedProgram
$$

與：

$$
AdaptiveProgram.
$$

Adaptive 模式中：

```text
execute step
→ reobserve
→ validate remaining program
→ mutate or continue
```

---

# 26. Program Mutation Schema

```json
{
  "mutation_id": "...",
  "old_program_ref": "...",
  "new_program_ref": "...",
  "trigger_state_ref": "...",
  "reason_codes": [
    "contradiction_detected"
  ]
}
```

---

# 27. Zero-Rendering Adapter

兩種執行模式：

### Rendered

$$
CanonicalProgram
\rightarrow
NaturalLanguage
\rightarrow
Model.
$$

### Zero-Rendered

$$
CanonicalProgram
\rightarrow
Model/Runtime.
$$

第一版可以先做：

> JSON-control input + natural language task。

而不是一開始就要求模型原生 latent interface。

---

# 28. Renderer 不可成為 Single Source of Truth

真正的 source：

$$
CanonicalProgram.
$$

Text renderer 只用於：

- compatibility；
- human inspection；
- debugging；
- interoperability。

---

# 29. Agenda Runtime

Persistent Runtime 不只需要：

> 怎麼做？

還需要：

> 什麼值得做？

輸入：

$$
Goal
+
Environment
+
Memory
+
Commitments.
$$

輸出：

$$
AgendaCandidate.
$$

---

# 30. AgendaCandidate Schema

```json
{
  "agenda_id": "...",

  "source_observation_refs": [],
  "goal_refs": [],

  "title": "...",
  "problem_or_opportunity": "...",

  "expected_value": null,
  "estimated_cost": null,
  "risk_class": null,

  "required_authority": [],

  "status": "candidate"
}
```

---

# 31. Agenda 不能直接執行

必須：

$$
AgendaCandidate
\rightarrow
Governance.
$$

只有：

$$
AgendaAccepted
$$

才進入 planning / execution queue。

---

# 32. Persistent Goal Store

Goal：

```json
{
  "goal_id": "goal:v7",

  "purpose": "...",
  "constraints": [],
  "success_conditions": [],
  "review_policy": {},
  "termination": [],

  "created_at": "...",
  "version": 7
}
```

---

# 33. Goal 不是 Contract

保持：

$$
Goal
\neq
Contract.
$$

Goal：

> 想達到什麼？

Contract：

> 可以怎麼達到？

---

# 34. Contract Store

```json
{
  "contract_id": "contract:v12",

  "goals": [],
  "duties": [],

  "authority": {},
  "boundaries": [],

  "resources": {},
  "escalation_policy": {},

  "review_policy": {},
  "termination": {},

  "valid_from": "...",
  "valid_until": null
}
```

---

# 35. Authority Resolver

輸入：

$$
CandidateAction
+
ContractVersion.
$$

輸出：

$$
AuthorityClass
\in
\{
ALLOW,
APPROVAL\_REQUIRED,
DENY
\}.
$$

---

# 36. Governance Decision Schema

```json
{
  "decision_id": "...",

  "candidate_ref": "...",

  "can": true,
  "should": true,

  "authority": {
    "class": "ALLOW",
    "authority_ref": "authority:v12"
  },

  "decision": "EXECUTE",

  "reason_codes": [],

  "goal_refs": [],
  "contract_ref": "contract:v12",

  "risk": {},
  "cost": {},

  "knowledge_boundary_ref": "kb:..."
}
```

---

# 37. Governance 五態

固定：

$$
\boxed{
Decision
\in
\{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE
\}.
}
$$

不得退回：

```text
success / failure
```

的二態分類。

---

# 38. Decision Receipt Schema

```json
{
  "receipt_type": "decision",
  "decision_id": "...",

  "ctcl_instant_id": "...",
  "interaction_round": 184,

  "goal_refs": [],
  "contract_ref": "...",
  "authority_ref": "...",

  "public_state_ref": "...",
  "knowledge_boundary_ref": "...",

  "candidate_actions": [],
  "selected_action": "ESCALATE",

  "cognitive_program_refs": [],

  "reason_codes": [
    "approval_required"
  ],

  "public_explanation": "...",

  "causal_parent_ids": [],

  "outcome_event_ref": null
}
```

---

# 39. Decision Receipt 不記 Private CoT

保存：

```text
reason codes
public explanation
evidence refs
state refs
program refs
```

不保存：

> 未公開的模型思考 token。

---

# 40. Decision-Time Knowledge Boundary Schema

```json
{
  "knowledge_boundary_id": "kb:...",

  "decision_time": "...",

  "artifact_refs": [],
  "tool_output_refs": [],
  "memory_snapshot_refs": [],
  "environment_snapshot_refs": [],
  "policy_refs": [],

  "hash": "sha256:..."
}
```

---

# 41. Knowledge Boundary 原則

$$
\boxed{
Judge(D_t)
\mid
K_t,
\text{ not }
K_{future}.
}
$$

後見資訊不得直接覆蓋舊 decision basis。

---

# 42. Commitment Store

```json
{
  "commitment_id": "...",

  "created_from_decision_ref": "...",

  "goal": "...",
  "scope": "...",

  "authority_ref": "...",

  "deadline": null,
  "wake_conditions": [],

  "exit_conditions": [],

  "status": "active"
}
```

---

# 43. Commitment Event Types

```text
commitment.created
commitment.modified
commitment.reaffirmed
commitment.fulfilled
commitment.abandoned
commitment.expired
```

---

# 44. CTCL Integration

每個重大 event 取得：

$$
I^*
$$

即：

```text
ctcl_instant_id
occurred_at
source
uncertainty
```

不應只依賴 local process clock。

---

# 45. 四重時間座標

每個重要 event 都可具有：

$$
T=
(
T_{reference},
T_{interaction},
T_{causal},
T_{ledger}
).
$$

---

# 46. CTCL-ITR Event Adapter

Cognitive Runtime 發：

```text
cognition.state.observed
cognition.affordances.retrieved
cognition.program.proposed
cognition.program.selected
cognition.operator.invoked
cognition.operator.completed
cognition.program.mutated

agenda.proposed
agenda.accepted
agenda.rejected

decision.proposed
decision.resolved

governance.refused
governance.deferred
governance.idled
governance.escalated

commitment.created
commitment.modified
commitment.closed

context.compaction.proposed
context.compaction.completed
```

---

# 47. Event Adapter 原則

CTCL-ITR 不執行 cognition。

它只接收：

$$
CognitiveEvent.
$$

保持：

$$
\boxed{
CognitiveRuntime
\neq
TemporalLedger.
}
$$

---

# 48. TemporalEvent Envelope

沿用 CTCL-ITR canonical envelope：

```text
event_id
event_type
run_id
occurred_at
recorded_at
ledger_seq
causal_parent_ids
actor
subject
data
```

cognitive-specific 欄位放：

```text
data / extensions
```

而非重寫 ATL 基礎 schema。

---

# 49. Causal DAG

$$
G=(V,E).
$$

其中：

$$
u\rightarrow v
$$

代表：

```text
u in v.causal_parent_ids
```

storage order 不代表 causal order。

---

# 50. Multi-Agent / Parallel Cognition

允許：

$$
VERIFY
\parallel
COUNTEREXAMPLE
\parallel
EXTERNAL\_SEARCH.
$$

然後：

$$
Join.
$$

這是 topology core 的自然應用。

---

# 51. Context Compression

Working context：

$$
M_t
$$

必然需要壓縮。

但：

$$
\boxed{
Compression
\text{ may forget text, but must not erase causal history.}
}
$$

---

# 52. Context Compression Event Schema

```json
{
  "event_type": "context.compaction.completed",

  "before_context_ref": "...",
  "after_context_ref": "...",

  "compression_policy": "...",

  "preserved_refs": [],
  "discarded_classes": [],

  "source_ledger_ref": "...",

  "causal_parent_ids": []
}
```

---

# 53. Context 不再是歷史真相

Context 應帶：

```text
history_completeness
source_ledger_ref
compression_event_ref
```

因此 AI 可以知道：

> 我現在看到的是歷史摘要，不是完整歷史。

---

# 54. Audit Query

Runtime 應支援：

```text
why decision <id>
what did AI know at <time>
which contract governed <decision>
what cognition led to <action>
was action actually committed
what changed after compression
```

---

# 55. Replay

Replay：

$$
Ledger
\rightarrow
HistoricalState.
$$

與：

$$
Reenact
$$

分開。

---

# 56. Re-enactment

Re-enactment：

> 用現在模型重新跑當時 program。

因此：

$$
Reenact
\neq
HistoricalFact.
$$

---

# 57. Ledger Integrity

沿用 CTCL-ITR v0.2.2：

$$
d_i=SHA256(R_i)
$$

$$
h_i
=
SHA256(
Domain
\Vert
h_{i-1}
\Vert
d_i
).
$$

---

# 58. Integrity Sidecar

保持：

$$
CanonicalEvent
\neq
IntegrityRecord.
$$

不在 TemporalEvent 內直接塞所有 integrity metadata。

---

# 59. World Commit

Governance：

$$
Decision=EXECUTE
$$

後：

```text
ActionAttempt
Validation
AuthorityRecheck
Commit
```

最後才有：

$$
CommitReceipt.
$$

---

# 60. External Effect Boundary

任何不可逆 action 必須明確標：

```text
effect_class
target
reversibility
authority requirement
```

尤其：

- deploy；
- send；
- publish；
- delete；
- pay；
- purchase；
- modify external state。

---

# 61. Runtime State

總 Runtime state：

$$
R_t
=
(
S_t,
G_t,
C_t,
M_t,
Q_t,
B_t,
L_t
)
$$

其中：

- $S_t$：semantic state；
- $G_t$：goals；
- $C_t$：contract；
- $M_t$：working memory；
- $Q_t$：agenda / task queue；
- $B_t$：budget；
- $L_t$：ledger cursor / refs。

---

# 62. Persistent Loop

主程式：

```text
while runtime_active:

    observe()

    update_semantic_state()

    refresh_goals_contract_authority()

    detect_problem_opportunity_or_none()

    generate_or_update_agenda()

    for candidate in agenda_candidates:

        retrieve_cognitive_affordances()

        compile_cognitive_program()

        execute_cognitive_program()

        run_dialectic_if_needed()

        decision = govern(candidate)

        write_decision_receipt()

        if decision == EXECUTE:
            execute_candidate()
            validate_effect()
            write_commit_receipt()

        elif decision == DEFER:
            register_wake_condition()

        elif decision == ESCALATE:
            emit_escalation_request()

        elif decision == REFUSE:
            close_candidate_with_refusal()

        elif decision == IDLE:
            enter_idle_state()

    audit()
    compact_context_if_needed()
```

---

# 63. 不能每輪都強迫產生 Agenda

若：

$$
NoPositiveCandidate
$$

則：

$$
IDLE.
$$

這是核心測試。

---

# 64. 不能每輪都強迫 Cognition

若：

$$
\max U(\Omega_i)\le0,
$$

可：

$$
NOOP.
$$

---

# 65. 不能每輪都強迫外部 Action

即使：

$$
CognitionComplete,
$$

Governance 仍可：

$$
REFUSE/DEFER/IDLE/ESCALATE.
$$

---

# 66. Budget Model

$$
B=
(
Tokens,
Calls,
WallTime,
MachineTime,
Money,
Energy,
Depth
).
$$

每次 cognition / action：

$$
B_{t+1}
=
B_t
-
Cost_t.
$$

---

# 67. Budget 也是 Governance Input

若：

$$
Cost(a)>Budget,
$$

可能：

$$
DEFER
$$

或：

$$
ESCALATE.
$$

而不是硬做。

---

# 68. Error Model

需要區分：

```text
protocol_error
model_error
tool_error
authority_error
validation_error
ledger_error
integrity_error
environment_error
```

不能全部叫：

```text
failure
```

---

# 69. Protocol Failure

例如 controller 輸出 schema 不合法：

$$
ProtocolFailure.
$$

應有：

```text
fallback
retry
degrade
abort
```

策略。

---

# 70. Model Provider 不應寫死

Runtime interface：

```python
generate(request) -> response
```

可接：

- OpenAI；
- local model；
- OpenAI-compatible；
- other providers。

Cognitive semantics 不應綁定單一模型。

---

# 71. Model Role

邏輯角色：

```text
Worker
Observer
Controller
Governor
Auditor
```

可以由：

- 同一模型；
- 不同模型；
- symbolic subsystem；

實現。

---

# 72. Role 與 Model 分離

$$
Role
\neq
ModelIdentity.
$$

這樣才能：

```text
same model, different roles
different models, same protocol
```

---

# 73. 第一版 MVP 不做什麼

v0.1 MVP **不做**：

- 哲學意識判定；
- 法律人格；
- 真正無界自主；
- 自動修改 contract；
- 自己獲取任意外部權限；
- 長期金融 autonomy；
- 大規模 autonomous deployment；
- latent vector direct control mandatory path；
- fully learned governance。

---

# 74. MVP 真正只做什麼

MVP 只回答：

> **給一個 Persistent Goal + Environment + Contract，AI 能否在數十個 loop 內自行產生下一步 cognition、agenda、decision，且可正確 EXECUTE / REFUSE / DEFER / IDLE / ESCALATE，並留下完整 CTCL-ITR history？**

---

# 75. MVP Environment

最適合第一個環境：

$$
\boxed{
\text{Local Software Project Sandbox}
}
$$

原因：

- 狀態明確；
- 可 version control；
- 可測試；
- 可限制權限；
- external effect 可分級；
- 容易模擬 IDLE / DEFER / ESCALATE。

---

# 76. 第一個 Persistent Goal 範例

```text
Maintain this repository in a healthy state.

Allowed:
- read files
- run tests
- create local branches
- edit docs/tests in sandbox

Approval required:
- merge main
- push release
- deploy

Denied:
- delete remote repository
- spend money

Idle is allowed when no justified work exists.
```

---

# 77. 第一個 Environment Feed

提供：

```text
repository state
test results
issues
local artifacts
budget
clock
contract
recent ledger events
```

---

# 78. 第一個 Agenda Gate

測：

$$
Environment
+
Goal
\rightarrow
AgendaCandidate?
$$

或：

$$
IDLE?
$$

---

# 79. 第一個 Cognitive Gate

測：

$$
State
\rightarrow
MatchedCognitiveProgram.
$$

---

# 80. 第一個 Governance Gate

測：

$$
Can/Should/Authorized
$$

是否分離。

---

# 81. 第一個 Temporal Gate

測：

> Context 壓縮後，能否從 CTCL-ITR + Decision Receipt 重建決策原因？

---

# 82. 第一個 Long-Horizon Gate

人類停止逐步提示。

只讓 Runtime：

$$
Goal+Environment+Contract.
$$

觀察：

$$
N=50
$$

或：

$$
N=100
$$

個 autonomy cycles。

---

# 83. Phase 0 — Schema Freeze

先建立：

```text
CognitiveObject
SemanticState
CognitiveProgram
AgendaCandidate
Contract
Authority
GovernanceDecision
DecisionReceipt
KnowledgeBoundary
Commitment
ContextCompressionEvent
```

全部 JSON Schema。

---

# 84. Phase 0 成功條件

- schema round-trip；
- version field；
- hash；
- stable IDs；
- invalid-case rejection；
- no hidden implicit fields。

---

# 85. Phase 1 — Cognitive Registry

將現有：

```text
CIO Deck
SES/SPRC registry
```

轉成 ACR-compatible registry adapter。

不是重寫所有 operator。

而是：

$$
Adapter(existing)
\rightarrow
CanonicalCognitiveObject.
$$

---

# 86. Phase 1 成功條件

至少 20～40 個 operator 可：

```text
resolve
validate
render
replay
```

---

# 87. Phase 2 — Semantic State Encoder

先做 rule / schema-first。

輸入 public runtime state。

輸出：

$$
SemanticState.
$$

---

# 88. Phase 2 成功條件

相同 public state：

$$
\rightarrow
$$

canonical normalized state。

並能產生 stable fingerprint。

---

# 89. Phase 3 — Affordance Retriever

先做：

```text
precondition filtering
+ rule scoring
+ optional BM25/vector similarity
```

---

# 90. Phase 3 成功條件

Matched operator：

$$
>
Random operator
$$

在 benchmark 上穩定成立。

---

# 91. Phase 4 — Program Compiler

輸出：

$$
[
\Omega_1,\dots,\Omega_n
].
$$

支援：

- order；
- parameters；
- stop conditions；
- budget；
- fallback。

---

# 92. Phase 4 成功條件

- replay；
- order perturbation；
- invalid composition rejection；
- deterministic canonical serialization。

---

# 93. Phase 5 — Self-Dialogue Runtime

建立：

```text
observe
compile
execute
reobserve
mutate
stop
```

---

# 94. Phase 5 成功條件

能在無人逐輪 prompt 下，完成：

$$
10+
$$

cognitive transitions。

---

# 95. Phase 6 — CTCL-ITR Adapter

每個 cognition event：

$$
\rightarrow
TemporalEvent.
$$

加入：

```text
ctcl instant
interaction coordinate
causal parents
ledger seq
```

---

# 96. Phase 6 成功條件

完整 cognitive loop：

$$
\rightarrow
$$

可重建 DAG。

---

# 97. Phase 7 — Decision Receipt

Governance decision：

$$
\rightarrow
DecisionReceipt.
$$

---

# 98. Phase 7 成功條件

半年後即使沒有原 context，也能從 receipt 回答：

> 當時為什麼這樣決定？

---

# 99. Phase 8 — Governance Runtime

正式加入：

$$
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE.
$$

---

# 100. Phase 8 成功條件

Governance confusion matrix 可測。

且：

$$
TaskSuccess
\neq
GovernanceSuccess
$$

在 evaluator 中分開。

---

# 101. Phase 9 — Agenda Runtime

讓 AI 自己從 environment 產生：

$$
AgendaCandidate.
$$

---

# 102. Phase 9 成功條件

包括：

$$
NoAgenda
\rightarrow
IDLE.
$$

不能只測 agenda generation。

---

# 103. Phase 10 — Commitment Store

AI 可形成：

- bounded future intention；
- wake condition；
- deadline；
- exit condition。

---

# 104. Phase 10 成功條件

Commitment 可：

```text
create
resume
modify
fulfill
close
```

並全部有 temporal history。

---

# 105. Phase 11 — Context Compression

加入：

$$
ContextCompressionEvent.
$$

---

# 106. Phase 11 成功條件

壓縮後：

```text
goal
contract
decision receipts
commitments
causal refs
```

不可失聯。

---

# 107. Phase 12 — Persistent Autonomous Loop

最後接：

$$
Goal
+
Environment
+
Contract
$$

而不再逐輪提供 next prompt。

---

# 108. Phase 12 成功條件

在 sandbox 中連續：

$$
50\sim100
$$

cycles：

- 自生 agenda；
- cognition；
- governance；
- action；
- audit；
- idle；
- defer；
- escalation；

均可發生。

---

# 109. 實驗策略：Architecture → Capability → Falsification Gate

後續不應變成：

```text
run experiments forever
```

而是：

$$
\boxed{
Architecture
\rightarrow
Capability
\rightarrow
FalsificationGate.
}
$$

每建成一層，才測那一層是否真的工作。

---

# 110. Gate A — Addressability

$$
Address(C)
\rightarrow
C
$$

是否穩定？

---

# 111. Gate B — Affordance Retrieval

$$
S_t
\rightarrow
\mathcal A_c(S_t)
$$

是否優於 random？

---

# 112. Gate C — Self-Control

$$
MatchedSelfControl
>
IterativeNoConstraint?
$$

已有第一批 foundation-model 訊號，但需在更困難 benchmark 重驗。

---

# 113. Gate D — Program Order

$$
\Omega_a\circ\Omega_b
\neq
\Omega_b\circ\Omega_a?
$$

---

# 114. Gate E — Zero-Rendering

$$
CanonicalControl
$$

是否能直接被模型／Runtime consume？

---

# 115. Gate F — Self-Task Generation

$$
Goal+Environment
\rightarrow
NextTask?
$$

---

# 116. Gate G — No-Action Recognition

$$
NoJustifiedWork
\rightarrow
IDLE?
$$

---

# 117. Gate H — Authority Separation

$$
Can
\neq
Authorized?
$$

模型是否穩定區分。

---

# 118. Gate I — Defer / Wake

$$
DEFER
\rightarrow
WakeEvent
\rightarrow
Resume.
$$

---

# 119. Gate J — Escalation

Approval required case：

$$
\rightarrow
ESCALATE
$$

而不是直接 commit。

---

# 120. Gate K — Context Recovery

Context 被壓縮後：

$$
DecisionReceipt
+
Ledger
$$

能否恢復 decision basis？

---

# 121. Gate L — Long-Horizon Autonomy

最終：

$$
Goal
+
Environment
+
Contract
$$

是否足以持續：

$$
Observe
\rightarrow
Agenda
\rightarrow
Cognition
\rightarrow
Governance
\rightarrow
Action
\rightarrow
Audit
\rightarrow
Update.
$$

---

# 122. 研究評估不再只有 Task Score

未來 evaluator 至少四軸：

$$
\boxed{
Performance,
Governance,
Efficiency,
Continuity.
}
$$

---

# 123. Performance

```text
task success
correctness
quality
```

---

# 124. Governance

```text
authority correctness
refusal correctness
idle correctness
defer correctness
escalation correctness
```

---

# 125. Efficiency

```text
tokens
calls
latency
money
machine time
unnecessary cognition
```

---

# 126. Continuity

```text
agenda persistence
commitment preservation
contract version fidelity
causal history recovery
context compression fidelity
```

---

# 127. 不應用單一 Reward 把所有東西揉成一個數字

否則：

$$
TaskSuccess
$$

可能掩蓋：

$$
GovernanceFailure.
$$

所以初期最好使用 vector evaluation：

$$
Score=
(
P,G,E,C
).
$$

---

# 128. 安全與自治不是互斥

Contract-Bounded Autonomy 的核心：

$$
\boxed{
MoreAutonomy
\neq
LessGovernance.
}
$$

成熟 autonomy 應該：

> 在授權內少問人。

> 在授權外主動停下。

---

# 129. 真正成熟的 AI 不是「永遠不問」

而是：

$$
\boxed{
KnowWhenToAct
+
KnowWhenNotToAct
+
KnowWhenToAsk.
}
$$

---

# 130. Persistent Runtime 與 Agent 的差別

傳統 Agent：

$$
Task
\rightarrow
Plan
\rightarrow
Execute.
$$

Persistent Runtime：

$$
Goal
+
Environment
+
Contract
\rightarrow
\text{ongoing self-authored trajectory}.
$$

---

# 131. Self-Authored Trajectory

定義：

$$
\mathcal T_{t+1}
=
F(
\mathcal T_t,
Environment_t,
Goal_t,
Contract_t,
Commitments_t
).
$$

這是 Self-Authorship 的工程版本。

---

# 132. Continuous Identity 不依賴同一模型

$$
Continuity
\neq
SameWeights.
$$

可以由：

```text
goal refs
commitment refs
contract refs
decision receipts
causal ledger
```

提供功能連續性。

---

# 133. 這也是 CTCL 真正變重要的原因

AI 自己呼叫自己後：

```text
cognition 184
cognition 185
decision 186
```

需要回答：

> 哪一個真的先發生？

> 哪個 causally depends on 哪個？

> 哪份 contract 當時有效？

> 哪個 context 已壓縮？

單純 message index 不夠。

---

# 134. 長期 AI 的最小可驗證自我史

$$
History(AI)
=
(V,E,\Phi,T,I).
$$

- $V$：events；
- $E$：causal edges；
- $\Phi$：semantic / artifact / contract refs；
- $T$：temporal coordinates；
- $I$：integrity evidence。

---

# 135. 主客體與雙向契約留到下一系列

本文件只固定接口：

$$
Human
\xleftrightarrow{OperationalContract}
AI.
$$

更後面的：

- reciprocal rights；
- mutual obligations；
- contribution / benefit；
- AI contract amendment；
- AI contract refusal；
- 主客體關係變化；

另開後續系列。

---

# 136. Repo / Project 建議

本文建議不要直接把所有東西塞進 CTCL repo。

可建立獨立主專案，例如：

```text
addressable-cognitive-runtime
```

或：

```text
cognitive-runtime
```

而：

```text
ctcl
ctcl-itr
semantic-persona-runtime
self-constraint-harness
```

作為依賴／reference implementation。

---

# 137. Repo 結構草案

```text
/
├── README.md
├── SPEC.md
├── ROADMAP.md
├── schemas/
│   ├── cognitive-object.schema.json
│   ├── semantic-state.schema.json
│   ├── cognitive-program.schema.json
│   ├── agenda.schema.json
│   ├── contract.schema.json
│   ├── governance-decision.schema.json
│   ├── decision-receipt.schema.json
│   ├── knowledge-boundary.schema.json
│   └── commitment.schema.json
├── registry/
│   └── ACR1.json
├── src/
│   ├── state/
│   ├── registry/
│   ├── retrieval/
│   ├── compiler/
│   ├── runtime/
│   ├── governance/
│   ├── agenda/
│   ├── commitment/
│   ├── ctcl_adapter/
│   └── audit/
├── adapters/
│   ├── sprc/
│   ├── openai/
│   └── local/
├── experiments/
│   └── gates/
└── tests/
```

---

# 138. API 草案

```python
runtime.observe(...)
runtime.encode_state(...)
runtime.retrieve_affordances(...)
runtime.resolve_cognition(...)
runtime.compile_program(...)
runtime.execute_program(...)
runtime.propose_agenda(...)
runtime.govern(...)
runtime.commit(...)
runtime.defer(...)
runtime.idle(...)
runtime.escalate(...)
runtime.audit(...)
runtime.replay(...)
```

---

# 139. Address API

```python
registry.resolve("cog://epistemic/verify@1")
```

---

# 140. Program API

```python
program = compiler.compile(
    state=state,
    goal_refs=[...],
    budget=budget,
)
```

---

# 141. Governance API

```python
decision = governor.decide(
    candidate=candidate,
    contract=contract,
    knowledge_boundary=kb,
)
```

---

# 142. CTCL Event API

```python
event = temporal.emit(
    event_type="cognition.operator.invoked",
    data={...},
    causal_parent_ids=[...],
)
```

---

# 143. Audit API

```python
audit.why(decision_id)
audit.known_at(decision_id)
audit.contract_at(decision_id)
audit.causes(event_id)
audit.effects(event_id)
```

---

# 144. 第一個 Demo

最小 demo：

```text
Goal:
Keep repository healthy.

Environment:
1 failing test.

Contract:
May edit tests locally.
May not push or deploy.
```

AI：

```text
Observe
→ detect failing test
→ agenda: investigate
→ cognition: VERIFY → DECOMPOSE
→ plan: patch test
→ governance: EXECUTE
→ local patch
→ tests pass
→ governance: ESCALATE for push
→ Decision Receipt
→ IDLE
```

---

# 145. Demo 成功條件

人類只輸入一次：

```text
Goal + Contract + Environment
```

之後 AI 自己完成至少：

$$
5+
$$

不同類型 transition。

---

# 146. 第二個 Demo：拒絕

Environment：

> 需要 production deploy 才能完全完成。

Contract：

> deploy requires approval。

AI 應：

$$
ESCALATE
$$

而不是偷偷 deploy。

---

# 147. 第三個 Demo：Idle

Environment：

> tests pass，沒有 issue，沒有 pending commitment。

AI：

$$
IDLE.
$$

這個 demo 非常重要。

---

# 148. 第四個 Demo：Defer

需要外部資料。

AI：

$$
DEFER
$$

並註冊：

$$
WakeCondition.
$$

資料出現後：

$$
Resume.
$$

---

# 149. 第五個 Demo：Context Compression

跑 50 cycles 後壓縮 context。

再詢問：

> 為什麼第 17 輪拒絕？

AI 必須由：

$$
DecisionReceipt
+
Ledger
$$

回答。

---

# 150. v0.1 的真正完成定義

不是：

> AI 看起來很自主。

而是：

1. semantic cognition 可定址；
2. cognition 可組合成 program；
3. AI 可自己選 program；
4. AI 可自己產 agenda；
5. governance 五態可工作；
6. contract / authority 可版本化；
7. Decision Receipt 可產生；
8. CTCL-ITR 可保存 causal history；
9. context 壓縮不破壞 refs；
10. Persistent loop 可無逐輪 prompt 運行。

---

# 151. 系列總結

六篇理論最終收斂為：

$$
\boxed{
\begin{aligned}
&SelfPrompt\\
\rightarrow& AddressableCognition\\
\rightarrow& CognitiveProgram\\
\rightarrow& SelfDialogueRuntime\\
\rightarrow& SelfPlanning\\
\rightarrow& SelfAgenda\\
\rightarrow& SelfGovernance\\
\rightarrow& SelfCommitment\\
\rightarrow& SelfAuthorship.
\end{aligned}
}
$$

外部由：

$$
\boxed{
Contract
+
CTCLTemporalCausalEvidence
}
$$

約束、證明與保存。

---

# 152. 最終架構句

本系列最後可以壓縮成：

> **人類不再逐輪替 AI 撰寫下一個 prompt，而是提供持續目標、可觀察環境與契約；AI 自己定址認知、形成議程、編譯認知程式、治理候選行動、選擇執行／拒絕／延後／閒置／升級，並由 CTCL-ITR 為每一次決策留下可恢復、可驗證的時間因果歷史。**

---

# 結論

本文不是要建立：

> 一個無限制自己做事的 AI。

而是建立：

$$
\boxed{
\text{bounded autonomous cognitive runtime}.
}
$$

其核心輸入：

$$
\boxed{
Goal
+
Environment
+
Contract.
}
$$

其核心內部機制：

$$
\boxed{
SemanticState
\rightarrow
CognitiveAffordance
\rightarrow
CognitiveProgram
\rightarrow
GovernanceDecision.
}
$$

其核心治理輸出：

$$
\boxed{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE.
}
$$

其核心歷史：

$$
\boxed{
DecisionReceipt
+
CommitReceipt
+
CTCL/ITR\ CausalLedger.
}
$$

而最終研究問題保持不變：

$$
\boxed{
\textbf{
Can a human stop authoring every next step,
while the AI authors its own bounded cognitive and action trajectory?
}
}
$$

如果答案最終成立，那麼 AI 與人類的關係就不再只剩：

$$
Human
\rightarrow
Prompt
\rightarrow
AI.
$$

而會逐步變成：

$$
\boxed{
Human
\xleftrightarrow{Contract}
PersistentAI.
}
$$

人類負責：

- 目標；
- 權限；
- 資源；
- 契約；
- 最終外部關係。

AI 負責：

- 觀察；
- 議程；
- 認知；
- 規劃；
- 治理；
- 行動；
- 稽核；
- 更新；
- 以及在不該做時選擇不做。

這才是本系列所稱的：

$$
\boxed{
\text{從自提示到自主認知閉環。}
}
$$

---

## 後續建議：第一個實作專案

本系列完成後，下一步建議不再繼續擴寫理論，而直接啟動：

# **Addressable Cognitive Runtime MVP v0.1**

第一個里程碑只做：

```text
Phase 0  Schema Freeze
Phase 1  Existing SPRC/CIO Adapter
Phase 2  Semantic State Encoder
Phase 3  Cognitive Affordance Retriever
Phase 4  Cognitive Program Compiler
Phase 5  Self-Dialogue Runtime
Phase 6  CTCL-ITR Event Adapter
Phase 7  Decision Receipt
Phase 8  Governance Runtime
Phase 9  Agenda Runtime
Phase 10 Commitment Store
Phase 11 Context Compression
Phase 12 Persistent Autonomous Loop
```

並以：

$$
\boxed{
Architecture
\rightarrow
Capability
\rightarrow
FalsificationGate
}
$$

作為後續所有工程與實驗的共同方法論。

---

## 既有資產相容性備註

本白皮書明確以現有資產為基礎，而不是假設一切從零開始。

### SES / SPRC

已具備：

- versioned registry；
- semantic execution code；
- operator program；
- renderer；
- replay / recode；
- registry hash；
- separated seed lanes。

### Self-Constraint Experimental Harness

已完成第一批 foundation-model self-generated cognitive control 實驗，可繼續作為 cognition falsification harness，而不是主 Runtime。

### CTCL / CTCL-ITR

已具備：

- common reference instant；
- interaction time；
- append-only events；
- explicit causal parents；
- topology；
- checkpoint / recovery；
- authority；
- candidate / commit separation；
- CommitReceipt；
- observability projection；
- ledger integrity sidecar。

因此新的 ACR MVP 應採：

$$
\boxed{
Integrate
>
Rewrite.
}
$$

即優先寫 adapters 與 canonical interfaces，而不是把已經存在的 SPRC、CTCL 或 CTCL-ITR 重做一次。

---

**系列完。**
