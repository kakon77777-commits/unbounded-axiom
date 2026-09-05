# FCAO Twin-Core Reference Architecture v0.1
## 分形式對話智能體組織雙核心參考架構：從局部類全域對話到可遞歸、可驗證、可重分區的 AI Runtime

**English Title:** FCAO Twin-Core Reference Architecture v0.1: A Recursive, Verifiable, and Dynamically Repartitionable Runtime for Local-Global Conversational AI Organizations  
**系列：** FCAO / Fractal Conversational Agent Organization  
**文件編號：** EML-FCAO-RA-2026-v0.1  
**文件類型：** Technical Whitepaper / Reference Architecture / Implementation Blueprint  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-24  
**狀態：** Reference Architecture Draft / Canonical UTF-8 Source  
**直接前置：**
- `EML-FCAO-2026-00-v0.1` — FCAO Foundation / Integration Paper
- `EML-FCAO-2026-01-v0.1` — Twin-Agent Governance
- `EML-FCAO-2026-02-v0.1` — Temporal-Topological Computation
- ANDO / AI-Native Distributed Organization
- CTCL-ITR
- Software Spacetime
- SEDB
- Addressable Cognitive Runtime
- Self-Constraint Experimental Harness
- MWT / Mathematical World Theory

**後續文件：** FCAO × OpenHarness Integration Architecture and MVP Specification v0.1  
**實作立場：** protocol-agnostic；優先以既有 Agent Harness 作 execution substrate，不預設從零重造 provider、terminal、MCP、CLI、TUI 或基礎 swarm runtime。  
**Canonical Source Policy：** 本 Markdown 為正式 UTF-8 source；數學只使用 ` $...$ ` 與 `$$...$$`；正式工程 schema 另以 JSON Schema / YAML 提供。

---

## 生成、保真與工程邊界聲明

本文把三篇 FCAO v0.1 理論文壓縮成一個可實作的 reference architecture。本文不主張所有模組均已完成 production-grade 實作，也不主張任何特定模型、Agent framework、MCP provider、CLI、A2A implementation 或資料庫必須作為唯一底層。

本文遵守以下工程邊界：

1. FCAO 是 **canonical orchestration semantics**，不是單一 vendor framework。
2. Agent provider、CLI、MCP、A2A、API、local process、cloud runtime 都是 adapter。
3. Primary 與 Twin 是治理角色，不等於特定模型身份。
4. Named Ephemeral Agent 的名字是 semantic handle，不等於人格本體或永久身份。
5. Topology Closure 不等於所有問題被永久解決，而是指定 scope 與 closure target 下的版本化閉合。
6. Verification 不要求保存 hidden chain-of-thought。
7. Canonical state 不應只存在任何單一 Agent context。
8. 任何高風險 world commit 仍受 authority、policy、verification 與 commit gate 約束。
9. 多 Agent、Twin、Repartition 都不被預設為一定更快或更省；必須由 telemetry 與 benchmark 驗證。
10. v0.1 先追求 deterministic interfaces、可回放 event、可測量 decision，而非追求一次建立完整 AGI organization。

---

# 摘要

FCAO 的三篇理論文分別建立了三個核心問題的答案。

第一，Conversation 不必被理解為單純訊息序列，而可以在一段任務生命週期內形成 temporary local computational world。根 Agent 對其子域具有局部類全域視野，並可建立 Named Ephemeral Agents、遞歸委任與 task topology。完成條件不再只是步驟跑完，而是 topology closure。

第二，單一 Root 不應預設同時承擔 planning、delegation、integration、verification 與 closure declaration。FCAO 引入 Primary–Twin 雙生治理：

$$
\boxed{
LocalGlobalAIUnit
=
Primary
+
Twin
+
EphemeralChildren.
}
$$

Primary 負責主要世界建模、規劃、委任、整合與 commit proposal；Twin 負責持續觀察、選擇性審計、challenge、reopen、repartition、fresh verifier dispatch 與 meta-verification。Twin 不是 Final Verifier，也不是 Duplicate Primary。

第三，任務可切分不等於值得切分。FCAO 使用 Temporal Envelope：

$$
\boxed{
\mathcal T(Q)
=
[T_Q^{-},T_Q^{+}]
}
$$

並以候選 topology、critical path、communication、verification、integration、rework 與 governance cost 判斷是否 `NO_SPLIT`、`SPLIT`、`MERGE`、`REASSIGN` 或 `REPARTITION`。因此 decomposition 是：

$$
\boxed{
D_t
=
D(
Q,
S_t,
Resources_t,
Graph_t,
Evidence_t
).
}
$$

本文將上述理論壓縮成 **FCAO Twin-Core Reference Architecture（FCAO-TCRA）v0.1**。整體架構由十二個 canonical planes / services 組成：

$$
\boxed{
\mathcal A_{FCAO}
=
(
World,
State,
Primary,
Twin,
Topology,
Temporal,
Identity,
Delegation,
Execution,
Verification,
Closure,
Ledger
).
}
$$

其中：

- World Boundary 定義 Conversation / Project 的局部類全域作用域；
- Canonical State Plane 保存可版本化的共享狀態；
- Primary Controller 建立主要 plan 與 integration；
- Twin Governor 執行獨立、選擇性治理；
- Topology Engine 保存 task / verification / resource / join relation；
- Temporal Engine 建立時間上下界、critical path 與 schedule estimate；
- Identity Registry 管理 Named Ephemeral Agent；
- Delegation Plane 管理 scope、authority、success condition 與 join contract；
- Execution Adapter Plane 對接 MCP、CLI、A2A、API、local / cloud Agent；
- Verification Plane 管理 Local Closure Certificate、fresh verifier 與 verification placement；
- Closure / Commit Plane 管理 reopen、global closure、commit proposal 與 world-commit gate；
- CTCL-ITR / Telemetry Ledger 保存所有高價值 state transition、estimate、receipt、cost 與 causal lineage。

本文同時提供 canonical schemas、狀態機、事件類型、adapter contract、MVP 分期、conformance levels 與 benchmark requirements。下一份文件再將此 reference architecture 映射至 OpenHarness，決定哪些功能 `Reuse / Extend / Patch / Fork`。

**關鍵詞：** FCAO、Twin-Core、Primary AI、Twin Governor、Fractal Agent Organization、Temporal Topology、Topology Closure、Named Ephemeral Agent、Local Closure Certificate、Dynamic Repartition、CTCL-ITR、SEDB、MCP、CLI、A2A、Reference Architecture

---

# 0. 架構目標

FCAO-TCRA v0.1 的目標不是：

> 如何讓一個模型回答得更聰明？

而是：

> 如何讓一個 Conversation / Project 形成暫時的局部類全域 AI 組織，能夠自行建立工作拓樸、估計是否值得切分、遞歸生成具名臨時 Agent、持續驗證、發現錯誤後向下重新探查，並在不依賴任何單一 provider 的前提下完成可追溯 closure？

核心目標：

$$
\boxed{
PersistentState
+
TwinGovernance
+
DynamicTopology
+
BoundedDelegation
+
TypedVerification
+
AuditableClosure.
}
$$

---

# 1. 非目標

v0.1 明確不追求：

1. 一開始就完全無人值守；
2. 每個 task 都強制 multi-agent；
3. 每個 task 都建立 Twin；
4. Twin 完整重算 Primary 的所有工作；
5. 一開始就建立全域最優 scheduler；
6. 把所有自然語言推理轉成結構化資料；
7. 保存所有 hidden reasoning；
8. 讓所有 child 擁有 recursive spawn 權；
9. 讓所有 world commit 自動執行；
10. 把 MCP / A2A / CLI 任一協議當成 FCAO 本體；
11. 綁死 OpenHarness 或任一現有 framework；
12. 把 topology closure 誤解成永久真理證明。

---

# 2. 系統總覽

FCAO-TCRA v0.1：

```text
User / External Principal
          |
          v
+-------------------------------+
| Conversation / Project World  |
+-------------------------------+
          |
          v
+----------------+     +----------------+
|    Primary     |<--->|      Twin      |
|  Controller    |     |    Governor    |
+----------------+     +----------------+
          \               /
           \             /
            v           v
        +-------------------+
        |  Topology Engine  |
        +-------------------+
              |       |
              |       +-------------------+
              v                           v
      +---------------+            +---------------+
      | Temporal /    |            | Verification  |
      | Cost Engine   |            | Plane         |
      +---------------+            +---------------+
              |                           |
              +------------+--------------+
                           v
                +----------------------+
                | Delegation / Identity|
                +----------------------+
                           |
                           v
                +----------------------+
                | Execution Adapters   |
                | MCP CLI A2A API ...  |
                +----------------------+
                           |
                           v
                +----------------------+
                | Ephemeral Agent Mesh |
                +----------------------+
                           |
                           v
                +----------------------+
                | Result / LCC / Receipt|
                +----------------------+
                           |
                           v
                +----------------------+
                | Closure / Commit     |
                +----------------------+
                           |
                           v
                +----------------------+
                | State + CTCL Ledger  |
                +----------------------+
```

canonical flow：

$$
\boxed{
Intent
\rightarrow
WorldState
\rightarrow
Estimate
\rightarrow
ChooseTopology
\rightarrow
Delegate
\rightarrow
Execute
\rightarrow
LocalVerify
\rightarrow
Aggregate
\rightarrow
TwinInspect
\rightarrow
Repartition?
\rightarrow
MetaVerify
\rightarrow
Closure
\rightarrow
Commit.
}
$$

---

# 3. 十二個 canonical planes

定義：

$$
\mathcal A_{FCAO}
=
(
W,S,P,T,G,\Theta,I,D,X,V,C,L
).
$$

其中：

$$
W=WorldBoundary,
$$

$$
S=CanonicalState,
$$

$$
P=PrimaryController,
$$

$$
T=TwinGovernor,
$$

$$
G=TopologyEngine,
$$

$$
\Theta=TemporalEngine,
$$

$$
I=IdentityRegistry,
$$

$$
D=DelegationPlane,
$$

$$
X=ExecutionAdapterPlane,
$$

$$
V=VerificationPlane,
$$

$$
C=ClosureCommitPlane,
$$

$$
L=TemporalCausalLedger.
$$

這十二個 plane 在 MVP 可以部署於同一 process；production 可以拆為不同 service。

---

# 4. World Boundary Plane

FCAO 的最高階 execution unit 不是 process，而是 **Local Project World**。

定義：

$$
W_C
=
(
WorldID,
Scope,
Goals,
Constraints,
Principals,
Resources,
StateRef,
TopologyRef,
PolicyRef,
LedgerRef
).
$$

World Boundary 決定：

- 哪些 artifact 屬於本 project；
- 哪些 credential 可見；
- 哪些外部 action 可執行；
- 哪些 Agent 可以加入；
- 哪些 state 可讀寫；
- closure target；
- commit risk class；
- budget；
- deadline；
- escalation target。

因此：

$$
\boxed{
LocalGlobal
}
$$

是相對於此 World Boundary，而不是宣稱某 Agent 具有宇宙級全知。

---

# 5. Canonical State Plane

核心不變量：

$$
\boxed{
CanonicalState
\not\subseteq
SingleAgentContext.
}
$$

State Plane 至少保存：

$$
S_t
=
(
World,
Tasks,
Edges,
Agents,
Delegations,
Artifacts,
Claims,
Evidence,
Verification,
Estimates,
Closures,
Policies,
Budgets,
Events
).
$$

Agent context 只取得投影：

$$
S_i
=
\pi_i(S_t).
$$

這允許：

- Agent 消失後 project 不失憶；
- context compaction 後可恢復；
- Agent replacement；
- multi-model execution；
- Twin 使用不同 context projection；
- SEDB / database / file ledger 作 canonical backend。

---

# 6. State consistency model

v0.1 不要求所有 state 強一致。

至少區分：

$$
Provisional,
Validated,
Canonical,
Committed.
$$

狀態轉換：

$$
Provisional
\rightarrow
Validated
\rightarrow
Canonical
\rightarrow
Committed.
$$

不是所有 artifact 都會走完整四階。

例如 local draft 可以：

$$
Provisional
\rightarrow
CanonicalInternal.
$$

而高風險 world action 才需要：

$$
Validated
\rightarrow
CommitGate
\rightarrow
Committed.
$$

---

# 7. Primary Controller

Primary Profile：

$$
P
=
(
AgentID,
Name,
WorldID,
Authority,
PlanningPolicy,
DelegationPolicy,
IntegrationPolicy,
CommitPolicy
).
$$

Primary 職責：

1. 接收 Intent；
2. 建立初始 World Model；
3. 提出 candidate topology；
4. 呼叫 Temporal Engine；
5. 選擇 `NO_SPLIT` 或 decomposition；
6. 建立 Named Ephemeral Agents；
7. 接收 local result / LCC；
8. 建立 branch integration；
9. 建立 candidate closure；
10. 提出 commit proposal；
11. 接受 Twin challenge / reopen；
12. 在必要時觸發 arbiter。

Primary 不應預設：

$$
Primary
=
FullVerifier.
$$

---

# 8. Twin Governor

Twin Profile：

$$
T
=
(
AgentID,
Name,
WorldID,
Authority,
AuditPolicy,
RiskThreshold,
AuditBudget,
VerifierPolicy,
ReopenPolicy,
ArbitrationPolicy
).
$$

Twin 職責：

$$
T
=
Observe
+
Challenge
+
SelectAudit
+
Verify
+
Redirect
+
Repartition
+
MetaVerify.
$$

Twin 主要讀：

- topology；
- temporal estimate；
- task state；
- LCC；
- verification queue；
- integration queue；
- risk；
- conflict；
- budget；
- commit proposal。

Twin 不應預設 full duplicate。

---

# 9. Twin Mode

Twin Mode：

$$
TwinMode
\in
\{
OFF,
LIGHT,
SELECTIVE,
STRICT
\}.
$$

## OFF

低風險、極小 task。

## LIGHT

只做：

- candidate closure check；
- high-risk node；
- final meta-verification。

## SELECTIVE

依 audit priority：

$$
\Pi(v)
$$

選擇驗證與 probe。

## STRICT

提高：

- fresh verifier coverage；
- merge verification；
- commit concurrence；
- external / human gate。

---

# 10. Primary–Twin peer rule

Twin 不是 Primary 的普通 child：

$$
Twin
\notin
OrdinaryChildSet(Primary).
$$

Primary 也不是 Twin 的 child。

兩者共享 World：

$$
P,T
\subset
W_C.
$$

但可有不同 context：

$$
Context_P
\neq
Context_T.
$$

也可有不同 provider：

$$
Provider_P
\neq
Provider_T.
$$

這不是必需，但可降低 correlated failure。

---

# 11. Topology Engine

Topology Engine 保存：

$$
G_t
=
(
V_t,
E_t^{dep},
E_t^{join},
E_t^{verify},
E_t^{resource},
E_t^{up},
E_t^{down},
E_t^{cross}
).
$$

其中：

- $E^{dep}$：依賴；
- $E^{join}$：合流；
- $E^{verify}$：驗證；
- $E^{resource}$：資源互斥；
- $E^{up}$：結果 / evidence / receipt 向上；
- $E^{down}$：probe / reopen / repartition 向下；
- $E^{cross}$：peer check / conflict / shared assumption。

因此：

$$
\boxed{
TaskTopology
\neq
TaskList.
}
$$

---

# 12. Node types

v0.1 node：

$$
NodeType
\in
\{
TASK,
VERIFY,
MERGE,
DECISION,
WAIT,
COMMIT,
ESCALATION
\}.
$$

每個 node 至少：

$$
v
=
(
ID,
Type,
Name,
State,
Scope,
Inputs,
Outputs,
Dependencies,
Authority,
Estimate,
Verification,
Closure
).
$$

---

# 13. Edge types

v0.1 edge：

$$
EdgeType
\in
\{
REQUIRES,
BLOCKS,
JOINS,
VERIFIES,
SHARES\_RESOURCE,
REPORTS\_TO,
REOPENS,
REPARTITIONS,
CONFLICTS\_WITH,
DERIVES\_FROM
\}.
$$

Edge 可帶權：

$$
e
=
(
Type,
Latency,
Cost,
Risk,
Loss,
Condition
).
$$

這為後續 Agent Computational Geometry 保留接口。

---

# 14. Topology lifecycle

Topology version：

$$
G_0,G_1,\ldots,G_t.
$$

任何結構性變更：

$$
SPLIT,
MERGE,
REORDER,
REASSIGN,
REOPEN,
REPARTITION
$$

都產生：

$$
TopologyVersionIncrement.
$$

不能覆蓋歷史而不留下 receipt。

---

# 15. Temporal Engine

Temporal Engine 對任何 target 建：

$$
TE_x
=
(
T_x^{-},
T_x^{+},
Confidence,
Basis,
Assumptions,
Observed
).
$$

其中：

$$
\mathcal T_x
=
[T_x^{-},T_x^{+}].
$$

它不是 deterministic promise，而是 operational envelope。

---

# 16. Temporal Engine inputs

輸入：

- historical run；
- task class；
- model class；
- input size；
- context locality；
- tool availability；
- resource contention；
- external latency；
- verification allowance；
- retry allowance；
- current progress。

輸出：

- lower bound；
- upper bound；
- confidence；
- critical path；
- expected bottleneck；
- estimate breach threshold。

---

# 17. Candidate Topology Planner

對 task $Q$：

$$
\mathfrak D(Q)
=
\{
Single,
D_1,\ldots,D_n
\}.
$$

`Single` 永遠是合法候選：

$$
Single
\in
\mathfrak D(Q).
$$

Candidate Planner 至少考慮：

- `NO_SPLIT`；
- `SPLIT_2`；
- `SPLIT_K`；
- reuse existing Agent；
- delayed split；
- speculative branch。

---

# 18. Decomposition decision

多目標 gain：

$$
\Delta(D)
=
(
\Delta T,
\Delta C,
\Delta Q,
\Delta R,
\Delta K,
\Delta L
).
$$

在 policy 已知時：

$$
G(D)
=
U(D)-U(Single).
$$

如果沒有合理單一 utility：

$$
ParetoFrontier(\mathfrak D(Q)).
$$

因此 `NO_SPLIT` 不表示 scheduler 失敗。

---

# 19. Critical path

對當前 acyclic execution projection：

$$
\Pi_{exec}(G_t),
$$

計算：

$$
CP(G_t)
=
\max_{p}
\sum_{v\in p}w(v).
$$

Verification node、WAIT node、MERGE node 都必須進 critical path。

---

# 20. Named Ephemeral Agent Identity

Agent Identity：

$$
AI_i
=
(
InstanceID,
EphemeralName,
Role,
TaskName,
ParentAgentID,
WorldID,
TeamID,
Authority,
Lifetime
).
$$

必須區分：

$$
AgentType
\neq
EphemeralName
\neq
TaskName.
$$

例如：

```yaml
instance_id: agent-01-827f
ephemeral_name: Atlas
role: implementation_worker
task_name: Storage Topology
parent_agent_id: primary-root-001
world_id: sedb-v1
lifetime: until_join
```

---

# 21. 名字的工程意義

Ephemeral Name 的作用：

- 人類可讀；
- Agent 間引用；
- audit log；
- task routing；
- conflict description；
- dashboard；
- memory compression。

名字不替代 machine ID。

因此：

$$
Name
+
ID
$$

雙軌保存。

---

# 22. Recursive lineage

遞歸 spawn：

$$
A_0
\rightarrow
A_1
\rightarrow
A_{1,1}
\rightarrow
\cdots
$$

必須保存：

$$
parent\_agent\_id.
$$

不得把所有 child 都寫成：

$$
parent=main.
$$

否則 ancestry、authority propagation 與 causal lineage 會丟失。

---

# 23. Conditional recursion

不是每個 child 都可 spawn。

定義：

$$
SubdelegationAllowed(A_i)
\in
\{0,1\}.
$$

且 child authority：

$$
Authority_{child}
\preceq
Authority_{parent}.
$$

若 parent 被 revoke：

$$
Revoke(parent)
\Rightarrow
RevokeOrRevalidate(descendants).
$$

---

# 24. Delegation Contract

Delegation：

$$
D_i
=
(
DelegationID,
Parent,
Child,
Task,
Scope,
Inputs,
Authority,
Budget,
TemporalEnvelope,
VerificationContract,
SuccessCriteria,
JoinCondition,
Expiry
).
$$

沒有明確 `JoinCondition` 的 child 不應被視為完整委任。

---

# 25. Join Condition

Join condition 可為：

- artifact produced；
- tests passed；
- LCC emitted；
- verifier pass；
- dependency satisfied；
- branch timeout；
- explicit cancellation。

形式：

$$
Join(A_i)
\iff
J_i(State)=1.
$$

---

# 26. Execution Adapter Plane

FCAO 不直接規定 Agent 如何執行。

Adapter contract：

$$
\phi_i:
CanonicalExecutionRequest
\leftrightarrow
ProviderProtocol_i.
$$

provider 可以是：

- MCP；
- CLI；
- A2A；
- REST / RPC；
- local subprocess；
- in-process Agent；
- remote cloud Agent；
- browser Agent；
- coding Agent；
- human node。

---

# 27. Canonical Execution Request

最小請求：

$$
ER
=
(
RequestID,
AgentIdentity,
Task,
ContextProjection,
Tools,
Authority,
Budget,
Deadline,
OutputContract
).
$$

adapter 只負責翻譯，不擁有 canonical project semantics。

---

# 28. Canonical Execution Result

結果：

$$
XR
=
(
RequestID,
Status,
Artifacts,
Claims,
Evidence,
Usage,
Errors,
LCC,
ProviderMetadata
).
$$

provider-specific metadata 可以保存，但不能成為唯一 canonical state。

---

# 29. Verification Plane

Verification Plane 負責：

$$
V
=
(
LocalVerification,
FreshVerification,
MergeVerification,
MetaVerification,
CommitVerification
).
$$

核心不變量：

$$
VerificationTopology
\subseteq
TaskTopology.
$$

---

# 30. Verification Contract

定義：

$$
VC
=
(
ObjectType,
RiskClass,
Stage,
Method,
RequiredEvidence,
VerifierPolicy,
PassCondition
).
$$

Method 可以是：

- test；
- lint；
- typecheck；
- reproduction；
- citation check；
- schema validation；
- proof checker；
- fresh model review；
- human review。

---

# 31. Local Closure Certificate

Local Closure Certificate：

$$
LCC_i
=
(
Scope,
SatisfiedObligations,
VerifiedArtifacts,
OpenGaps,
Assumptions,
Receipts,
Lineage,
Confidence
).
$$

重要：

$$
LCC_i=complete
\not\Rightarrow
GlobalClosure.
$$

LCC 的目的：

$$
ParentVerification
\neq
FullRecomputation.
$$

---

# 32. Fresh verifier

Twin 或 Primary 可以：

$$
Spawn(A_{verify}^{fresh})
$$

Fresh verifier 應：

- 不直接修改 target artifact，除非 verification contract 明確允許；
- 使用獨立 context projection；
- 輸出 receipt；
- 不自動取得 project-wide authority。

---

# 33. Audit priority

Twin 使用：

$$
\Pi(v)
=
f(
Risk,
Uncertainty,
Centrality,
FailureImpact,
DependencyDepth,
Novelty,
Conflict,
VerificationCost
).
$$

選擇：

$$
V_{audit}
=
\{v\mid \Pi(v)\ge\theta\}.
$$

這避免：

$$
TwinCoverage
=
100\%\ FullRecompute.
$$

---

# 34. Bottom-up aggregation

child：

$$
Result
+
Evidence
+
Usage
+
LCC
$$

向上。

branch integrator 可以先局部 merge。

因此：

$$
Leaves
\rightarrow
LocalMerge
\rightarrow
RegionalMerge
\rightarrow
GlobalMerge.
$$

避免 Primary fan-in bottleneck。

---

# 35. Top-down probe

Twin 發現 anomaly 後建立：

$$
Probe
=
(
Target,
Question,
Reason,
Scope,
Budget,
EvidenceNeeded,
StopCondition
).
$$

原則：

$$
\boxed{
MinimalNecessaryReopening.
}
$$

不是全 project 重跑。

---

# 36. REOPEN

已關閉 node 可以重新打開：

$$
Closed(v,t_1)=1
$$

不代表：

$$
Closed(v,t_2)=1
$$

永遠成立。

`REOPEN` 必須包含：

- reason；
- trigger；
- evidence；
- affected descendants；
- required action；
- issuer；
- authority；
- CTCL timestamp。

---

# 37. REPARTITION

Repartition Receipt：

$$
RR
=
(
OldTopology,
NewTopology,
Trigger,
ExpectedBenefit,
InvalidatedWork,
Authority,
Time
).
$$

必須檢查：

$$
ExpectedGain(Repartition)
>
C_{repart}
$$

才應執行，除非 safety / correctness 要求強制重分區。

---

# 38. Anti-thrashing

若：

$$
N_{repart}(v)\ge\theta_D,
$$

系統進：

$$
FREEZE
$$

或：

$$
ESCALATE.
$$

避免：

$$
D_1
\rightarrow
D_2
\rightarrow
D_1
\rightarrow\cdots
$$

無限震盪。

---

# 39. Closure Engine

Global Closure 不只是：

$$
AllTasksCompleted.
$$

而是：

$$
Closure(G)
=
f(
MandatoryCoverage,
Verification,
OpenGaps,
Conflicts,
JoinState,
Policy
).
$$

v0.1 closure result：

$$
ClosureState
\in
\{
OPEN,
PARTIAL,
CANDIDATE,
VERIFIED,
CLOSED,
REOPENED,
ESCALATED
\}.
$$

---

# 40. Closure Target

對 research exploration：

$$
\theta_K<1
$$

可以合法。

但未閉合 node 必須：

$$
Deferred
$$

或：

$$
Externalized.
$$

因此：

$$
PartialClosure
\neq
SilentOmission.
$$

---

# 41. Closure Certificate

Global Closure Certificate：

$$
GCC
=
(
WorldID,
TopologyVersion,
ClosureTarget,
MandatoryCoverage,
VerificationSummary,
OpenGaps,
DeferredNodes,
ConflictState,
PrimaryDecision,
TwinDecision,
Receipts,
CommitEligibility
).
$$

只有 GCC 通過 policy 才進 commit proposal。

---

# 42. Commit Plane

Commit：

$$
Proposal
\neq
Canonical
\neq
WorldCommit.
$$

Risk class：

$$
R_c
\in
\{
R_0,R_1,R_2,R_3,R_4
\}.
$$

例如：

$$
R_0:
PrimaryOnly,
$$

$$
R_2:
Primary+TwinCheck,
$$

$$
R_3:
Primary+TwinConcurrence,
$$

$$
R_4:
Primary+Twin+ExternalGate.
$$

---

# 43. Temporary Arbiter

若 Primary 與 Twin 高風險 disagreement：

$$
Decision_P
\neq
Decision_T,
$$

先：

$$
EvidenceExchange.
$$

再：

$$
FreshVerifier.
$$

仍未解才：

$$
TemporaryArbiter.
$$

Arbiter authority：

$$
Authority(A_{arb})
\preceq
DisputeScope.
$$

完成後銷毀 role。

---

# 44. CTCL-ITR Ledger

所有治理關鍵事件：

$$
Event
=
(
EventID,
Actor,
Time,
World,
StateBefore,
Decision,
Target,
Authority,
Evidence,
StateAfter,
Receipt
).
$$

事件至少包括：

$$
\{
ESTIMATE,
CHOOSE\_TOPOLOGY,
DISPATCH,
RESULT,
LCC,
VERIFY,
MERGE,
CHALLENGE,
PROBE,
REOPEN,
REPARTITION,
ARBITRATE,
CLOSE,
COMMIT
\}.
$$

---

# 45. Time domains

至少保存：

$$
\tau_P,
\tau_T,
\tau_i,
T_W.
$$

其中：

- $\tau_P$：Primary active time；
- $\tau_T$：Twin active time；
- $\tau_i$：child Agent time；
- $T_W$：project makespan。

Aggregate work：

$$
W
=
\sum_i\tau_i+\tau_P+\tau_T.
$$

但：

$$
W
\neq
T_W.
$$

---

# 46. Telemetry Plane

v0.1 最少 telemetry：

- wall time；
- active compute time；
- wait time；
- token；
- tool calls；
- retries；
- external cost；
- artifact size；
- verification cost；
- integration cost；
- invalidated work；
- useful work；
- estimate breach；
- repartition count；
- reopen count。

---

# 47. 核心性能指標

至少：

$$
Makespan,
$$

$$
TotalCost,
$$

$$
UsefulWorkRatio,
$$

$$
VerificationRecomputeRatio,
$$

$$
FalseClosureRate,
$$

$$
LateReworkCost,
$$

$$
EstimateCalibration,
$$

$$
TwinMarginalValue.
$$

---

# 48. Useful Work Ratio

$$
W_{useful}
=
W_{executed}
-
W_{invalidated}
-
W_{duplicated}
-
W_{unintegrable}.
$$

$$
UWR
=
\frac{
W_{useful}
}{
W_{total}
}.
$$

高 Agent 數不代表高 UWR。

---

# 49. Verification Recompute Ratio

$$
VRR
=
\frac{
C_{verify}^{recompute}
}{
C_{verify}^{total}
}.
$$

LCC 與 typed receipt 的目標之一是：

$$
VRR\downarrow.
$$

---

# 50. Twin Marginal Value

$$
MV_T
=
AvoidedRework
+
AvoidedFailure
+
VerificationSavings
-
TwinOperatingCost.
$$

此指標必須實測。

$$
TwinBenefit
\neq
AssumedConstant.
$$

---

# 51. SEDB adapter

SEDB 可以保存動態 project field：

$$
F_{FCAO}
=
\{
agent,
task,
risk,
estimate,
verification,
closure,
reopen,
repartition,
receipt,
conflict
\}.
$$

但遵守 SEDB 原則：

$$
AddField
\not\Rightarrow
FillField.
$$

不相關 object 不需 materialize 所有 FCAO 欄位。

---

# 52. SEDB state projection

對 Agent $A_i$：

$$
F_i
\subseteq
F_{FCAO}.
$$

只投影：

- task relevant state；
- required dependency；
- authority；
- evidence；
- output schema。

避免整個 project database 全塞進 context。

---

# 53. Addressable Cognitive Runtime adapter

Twin / Primary 可以呼叫：

$$
CognitionAddress
+
CognitiveOperator
$$

例如：

- contradiction scan；
- topology gap detection；
- decomposition alternative；
- evidence gap；
- merge audit。

因此：

$$
Audit
\neq
RegenerateWholeConversation.
$$

---

# 54. Self-Constraint adapter

每個 Agent action：

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

Twin 也允許：

$$
IDLE.
$$

這是避免 supervisory overactivity 的核心。

---

# 55. MWT relation

MWT 提供 World-first 上位本體。

Primary 與 Twin：

$$
ObserverController_P,
ObserverController_T
$$

都只是 World 內的局部觀察—控制節點。

因此：

$$
Projection_P(W)
\neq
Projection_T(W)
$$

是允許的。

但所有 governance-critical decision 必須回到 canonical state / receipt 可比較。

---

# 56. ANDO relation

FCAO 繼承：

$$
State
\neq
Agent
\neq
Authority
\neq
Commit.
$$

FCAO 增加：

$$
Primary
\parallel
Twin
$$

與：

$$
DynamicTopology.
$$

所以 FCAO 可以視為 ANDO 的 conversation-local / project-local recursive orchestration specialization。

---

# 57. Protocol adapter interface

每個 adapter 必須提供最小介面：

```text
spawn(request) -> execution_handle
send(handle, message) -> receipt
stop(handle, reason) -> receipt
status(handle) -> status
collect(handle) -> result
capabilities() -> capability_profile
```

可選：

```text
pause(handle)
resume(handle)
stream(handle)
attach_tool(handle, tool)
detach_tool(handle, tool)
```

---

# 58. MCP mapping

MCP adapter 主要承擔：

- tool discovery；
- tool invocation；
- task / long-running extension；
- resource access；
- external service。

FCAO 不把 MCP session 當 canonical project world。

---

# 59. CLI mapping

CLI adapter 主要承擔：

- coding Agent；
- local subprocess；
- shell / repo work；
- local filesystem；
- model-specific agent CLI。

CLI process 可以是 child Agent runtime，但其 stdout 不是 canonical state。

---

# 60. A2A mapping

A2A / Agent-to-Agent protocol 適合：

- remote specialist；
- capability discovery；
- cross-runtime delegation；
- long-running task。

但 parent / child lineage、Twin semantics、LCC 與 closure 仍由 FCAO canonical model保存。

---

# 61. Human node

人類可以是：

$$
HumanNode
\in
AgentPlane.
$$

例如：

- approve；
- clarify；
- legal review；
- domain verification；
- high-risk commit。

但人類不是所有低風險 task 的必經 kernel。

---

# 62. Authority Envelope

Authority：

$$
A_{env}
=
(
Actions,
Scopes,
Targets,
Credentials,
CommitClasses,
Expiry,
Subdelegation
).
$$

Capability：

$$
Capability
\neq
Authority.
$$

即使 Agent 技術上能執行 shell，也不代表有權修改 production。

---

# 63. Credential handling

credential 不應寫入：

- prompt；
- LCC；
- event log；
- child name；
- artifact description。

Agent 只取得 scoped handle / secret reference。

---

# 64. Failure model

至少處理：

1. Agent timeout；
2. Agent crash；
3. provider unavailable；
4. tool failure；
5. invalid artifact；
6. verifier disagreement；
7. estimate breach；
8. state conflict；
9. topology inconsistency；
10. credential / permission failure；
11. duplicate result；
12. stale context。

---

# 65. Recovery

若 Agent crash：

$$
AgentFailure
\not\Rightarrow
ProjectFailure.
$$

因為 state 在 Agent 外。

Recovery：

$$
Checkpoint
\rightarrow
Reassign
\rightarrow
Resume.
$$

若 context 不可恢復，至少保留：

- task；
- state projection；
- artifact；
- LCC；
- event history。

---

# 66. Idempotency

任何可重試操作應有：

$$
IdempotencyKey.
$$

尤其：

- external API；
- commit；
- publish；
- payment；
- destructive operation。

避免 retry 造成重複 world effect。

---

# 67. Concurrency control

不同 child 同時修改 shared artifact 時，必須有：

- worktree；
- branch；
- file lock；
- optimistic concurrency；
- merge protocol；

之一。

FCAO 不規定唯一方法，但要求 conflict 可被觀察。

---

# 68. Artifact lineage

Artifact：

$$
A
=
(
ArtifactID,
Version,
Creator,
Task,
Inputs,
Hash,
Validation,
ParentArtifacts
).
$$

因此：

$$
Result
\rightarrow
Artifact
\rightarrow
Verification
\rightarrow
Closure
$$

可追溯。

---

# 69. Event sourcing

v0.1 推薦：

$$
State_t
=
Fold(Event_0,\ldots,Event_t).
$$

不要求所有 backend 真正只使用 event sourcing，但 governance-critical transition 應能重放。

---

# 70. Snapshot

長 project 可以週期性：

$$
Snapshot(S_t).
$$

Snapshot 不取代 event history，而是降低 replay cost。

---

# 71. Primary lifecycle

Primary：

$$
PState
\in
\{
BOOTSTRAP,
MODELING,
ESTIMATING,
PLANNING,
DISPATCHING,
INTEGRATING,
COMMIT\_PENDING,
CLOSED,
ESCALATED
\}.
$$

---

# 72. Twin lifecycle

Twin：

$$
TState
\in
\{
BOOTSTRAP,
OBSERVING,
AUDITING,
CHALLENGING,
REPARTITIONING,
META\_VERIFYING,
IDLE,
ESCALATED
\}.
$$

---

# 73. Project lifecycle

Project：

$$
WState
\in
\{
OPEN,
RUNNING,
BLOCKED,
REOPENED,
REPAIRING,
VERIFYING,
COMMIT\_PENDING,
CLOSED,
ESCALATED
\}.
$$

三套 state 不壓成一個。

---

# 74. 最小控制循環

```text
1. Load canonical world state
2. Primary proposes candidate topology
3. Temporal Engine estimates candidates
4. Primary chooses topology
5. Twin audits estimate / high-risk structure
6. Delegation Plane spawns named agents
7. Agents execute and emit receipts / LCC
8. Runtime updates topology + temporal state
9. Twin watches breach / bottleneck / conflict
10. If needed: probe / reopen / repartition
11. Primary integrates
12. Twin meta-verifies candidate closure
13. Closure Engine issues GCC
14. Commit Plane applies policy gate
15. Persist event + snapshot
```

---

# 75. Scheduler pseudocode

```text
while project not terminal:
    state = load_canonical_state()
    events = collect_new_events()

    if reevaluation_required(events, state):
        candidates = topology.generate_candidates(state)
        feasible = filter_feasible(candidates, state.policy, state.resources)

        estimates = temporal.estimate(feasible, state)
        choice = primary.choose(estimates, state.policy)

        twin_review = twin.inspect(choice, estimates, state)

        if twin_review.challenge:
            choice = reconcile_or_arbitrate(choice, twin_review)

        apply_topology(choice)

    dispatch_ready_nodes()
    collect_results_and_lcc()
    run_scheduled_verification()
    update_metrics()

    if closure_candidate():
        gcc = closure.evaluate()
        if twin.meta_verify(gcc):
            commit_or_close(gcc)
```

---

# 76. Reevaluation trigger

Reevaluate 只在：

$$
\{
TASK\_COMPLETE,
ESTIMATE\_BREACH,
CONFLICT,
RESOURCE\_SHOCK,
MERGE\_READY,
RISK\_CHANGE,
VERIFY\_FAIL,
REOPEN
\}
$$

等事件觸發。

不做 continuous full replan。

---

# 77. Planning budget

Planner 本身有：

$$
PlanningBudget.
$$

若：

$$
ExpectedValueOfMorePlanning
<
PlanningCost,
$$

停止候選探索。

---

# 78. Fan-out control

$$
FanOut
\le
FanOut_{max}.
$$

由：

- token；
- cost；
- Twin monitoring capacity；
- verification throughput；
- integration capacity；

決定。

---

# 79. Fan-in control

若 merge fan-in 過大：

$$
deg^{-}(merge)>\theta_{fanin},
$$

改用 hierarchical merge。

---

# 80. Verification queue control

若：

$$
Queue_V>\theta_V,
$$

可：

- 增加 verifier；
- 降低低風險 audit；
- 暫停新 fan-out；
- 將部分 node 延後。

---

# 81. Integration queue control

若：

$$
Queue_I>\theta_I,
$$

可：

- branch integrator；
- hierarchical merge；
- typed artifact；
- stronger LCC；
- 降低 speculative execution。

---

# 82. Time budget control

若：

$$
T_D^{+}>Deadline
$$

對全部候選成立，系統應：

$$
ESCALATE
$$

或：

- reduce scope；
- lower closure target；
- add resources；
- defer noncritical node。

不能假裝多派 Agent 一定能解。

---

# 83. Cost budget control

Budget shortage：

$$
Budget_t<RequiredBudget
$$

時允許：

- cheaper model；
- lower Twin mode；
- reduced speculative branch；
- defer low-priority node。

但：

$$
BudgetPressure
\not\Rightarrow
SilentInvariantRemoval.
$$

---

# 84. Closure before commit

任何 commit：

$$
CommitProposal
\Rightarrow
ClosureCertificate.
$$

高風險 commit 還需要：

$$
TwinConcurrence
$$

或 external gate。

---

# 85. Conformance levels

## FCAO-L0 — Single World

要求：

- canonical world；
- task graph；
- event receipt；
- Agent identity。

不要求 Twin。

## FCAO-L1 — Recursive Delegation

增加：

- Named Ephemeral Agent；
- parent lineage；
- delegation contract；
- LCC。

## FCAO-L2 — Twin Governance

增加：

- persistent Twin；
- selective audit；
- challenge；
- reopen；
- meta-verification。

## FCAO-L3 — Temporal Topology

增加：

- Temporal Envelope；
- candidate topology；
- critical path；
- repartition；
- verification placement。

## FCAO-L4 — Protocol Federation

增加：

- multiple adapters；
- remote Agent；
- MCP / CLI / A2A federation；
- cross-runtime receipts。

---

# 86. MVP 目標

第一個 MVP 不需要一次達 FCAO-L4。

推薦：

$$
MVP
=
L2
+
MinimalL3.
$$

即：

- Primary；
- Twin；
- 2–4 child；
- named Agent；
- task graph；
- temporal envelope；
- one repartition；
- LCC；
- closure certificate；
- event ledger。

---

# 87. MVP Phase 0 — Deterministic Core

完成：

- schemas；
- task graph；
- event store；
- state reducer；
- closure engine；
- no real LLM。

用 deterministic fake agents 驗證 state machine。

---

# 88. MVP Phase 1 — Single Provider

加入：

- one real Agent provider；
- Primary；
- child spawn；
- Named Ephemeral Agent；
- result / LCC。

---

# 89. MVP Phase 2 — Twin

加入 persistent Twin：

- read-only structural monitor；
- challenge；
- fresh verifier；
- no direct repartition first。

---

# 90. MVP Phase 3 — Repartition

加入：

- temporal upper breach；
- Twin `REOPEN`；
- `SPLIT` / `REASSIGN`；
- topology version；
- CTCL receipt。

---

# 91. MVP Phase 4 — Protocol Adapter

至少兩種 execution backend，例如：

$$
CLI
+
MCP
$$

或：

$$
Local
+
Cloud.
$$

證明 canonical model 不依賴單一 provider。

---

# 92. MVP Phase 5 — SEDB / persistent state

將：

- task；
- Agent；
- LCC；
- risk；
- estimate；
- receipt；

保存到 persistent backend。

---

# 93. MVP Phase 6 — Benchmark

比較：

1. Single Agent；
2. fixed multi-agent；
3. fixed multi-agent + verifier；
4. FCAO Primary–Twin + dynamic topology。

---

# 94. Benchmark 必測案例

至少有：

### Case A：不值得切

系統應選：

$$
NO\_SPLIT.
$$

### Case B：平行有效

選：

$$
SPLIT.
$$

### Case C：verification bottleneck

Twin 偵測 queue。

### Case D：temporal breach

觸發：

$$
REPARTITION.
$$

### Case E：false closure

Twin 阻止 closure。

### Case F：high-risk dispute

觸發 fresh verifier / arbiter。

---

# 95. Acceptance criteria

Reference MVP 至少證明：

1. Conversation 可形成 World ID；
2. Primary / Twin 有獨立 state；
3. child 有 unique ID + ephemeral name + task name；
4. parent lineage 可遞歸；
5. task graph 不只 flat list；
6. Temporal Envelope 可更新；
7. verification 是 graph node；
8. child 產生 LCC；
9. Twin 可 selective audit；
10. Twin 可阻止 false closure；
11. topology 可 versioned repartition；
12. final GCC 可輸出；
13. event 可重放；
14. provider adapter 可替換。

---

# 96. Schema set

本 package 附帶：

- `fcao_architecture_profile.schema.json`
- `agent_identity.schema.json`
- `task_node.schema.json`
- `delegation_contract.schema.json`
- `closure_certificate.schema.json`
- `event_receipt.schema.json`
- `FCAO_Reference_Profile_v0.1.yaml`

它們是 v0.1 machine-readable skeleton，不代表 production API 已 freeze。

---

# 97. OpenHarness integration boundary

下一份白皮書才處理：

$$
Requirement_{FCAO}
\times
Capability_{OpenHarness}.
$$

每一項分類：

$$
Reuse,
Extend,
Patch,
Fork.
$$

本文不先假定 fork。

---

# 98. 實作優先序

建議：

$$
CanonicalState
\rightarrow
Topology
\rightarrow
Identity
\rightarrow
LCC
\rightarrow
Primary
\rightarrow
Twin
\rightarrow
Temporal
\rightarrow
Repartition
\rightarrow
Adapters.
$$

不要先做漂亮 UI。

---

# 99. 核心不變量

## Invariant 1

$$
CanonicalState
\not\subseteq
SingleAgentContext.
$$

## Invariant 2

$$
Twin
\neq
OrdinaryChild
\neq
DuplicatePrimary.
$$

## Invariant 3

$$
AgentType
\neq
EphemeralName
\neq
TaskName.
$$

## Invariant 4

$$
Authority_{child}
\preceq
Authority_{parent}.
$$

## Invariant 5

$$
VerificationTopology
\subseteq
TaskTopology.
$$

## Invariant 6

$$
Decomposable
\not\Rightarrow
WorthDecomposing.
$$

## Invariant 7

$$
Single
\in
CandidateTopologies.
$$

## Invariant 8

$$
Repartition
\Rightarrow
Receipt
+
TopologyVersion.
$$

## Invariant 9

$$
LCC
\not\Rightarrow
GlobalClosure.
$$

## Invariant 10

$$
Closure
\not\Rightarrow
WorldCommit.
$$

## Invariant 11

$$
Protocol
\neq
CanonicalSemantics.
$$

## Invariant 12

$$
EfficiencyClaim
\Rightarrow
Telemetry
+
Benchmark.
$$

---

# 100. 結論

FCAO-TCRA v0.1 將三篇理論文壓縮成一個可實作的 AI-native orchestration runtime。

它的最小治理單位不是：

$$
Root+Children,
$$

而是：

$$
\boxed{
Primary
\parallel
Twin
+
NamedEphemeralAgents.
}
$$

它的任務表示不是：

$$
TaskList,
$$

而是：

$$
\boxed{
DynamicTaskVerificationTopology.
}
$$

它的時間模型不是：

$$
OneEstimatedDuration,
$$

而是：

$$
\boxed{
[T^{-},T^{+}]
+
ObservedTelemetry.
}
$$

它的完成條件不是：

$$
StepsDone,
$$

而是：

$$
\boxed{
VersionedTopologyClosure.
}
$$

它的分散式執行不是：

$$
MoreAgents=Better,
$$

而是：

$$
\boxed{
ChooseAgentCount
+
ChooseEdges
+
ChooseVerification
+
ChooseMerge
+
ChooseWhenToChange.
}
$$

而其 protocol stance 是：

$$
\boxed{
FCAO
=
CanonicalOrchestrationSemantics
}
$$

底層：

$$
MCP,
CLI,
A2A,
API,
LocalRuntime,
CloudRuntime
$$

只是 adapters。

因此下一階段的問題已從「還需要發明什麼理論？」轉為：

> **現有 OpenHarness 已提供哪些 execution substrate？FCAO 哪些模組可直接 Reuse，哪些適合 plugin / hook Extend，哪些需要 upstream Patch，哪些才真正值得 Fork？**

這將由下一份：

**FCAO × OpenHarness Integration Architecture and MVP Specification v0.1**

處理。

到此，FCAO v0.1 已從理論正式進入 reference architecture 階段。

---

# 附錄 A：Reference Runtime Profile Example

```yaml
world:
  id: fcao-demo-world
  closure_target: 1.0
  commit_risk_class: R2

primary:
  agent_id: primary-root-001
  name: Polaris
  role: primary

twin:
  agent_id: twin-root-001
  name: Argus
  role: twin
  mode: SELECTIVE

topology:
  max_fanout: 6
  max_repartition_per_node: 4
  hierarchical_merge_threshold: 5

temporal:
  envelope_required: true
  default_confidence_floor: 0.50
  breach_triggers_replan: true

verification:
  require_lcc: true
  local_for:
    - deterministic_test
    - schema_validation
  merge_for:
    - integration_contract
  commit_for:
    - public_release

state:
  backend: pluggable
  event_sourcing: true
  snapshots: true

adapters:
  required_interface:
    - spawn
    - send
    - stop
    - status
    - collect
    - capabilities
```

---

# 附錄 B：Agent Identity Example

```yaml
instance_id: agent-017-9fd2
ephemeral_name: Atlas
role: implementation_worker
task_id: task-017
task_name: Storage Topology
parent_agent_id: primary-root-001
world_id: fcao-demo-world
team_id: storage-branch
authority_ref: authority://delegation-017
lifetime:
  type: until_join
```

---

# 附錄 C：Closure Certificate Example

```yaml
closure_id: gcc-world-001-v7
world_id: fcao-demo-world
topology_version: topo-v7
closure_target: 1.0
mandatory_coverage: 1.0
verification:
  local_pass: 8
  merge_pass: 3
  open_failures: 0
open_gaps: []
deferred_nodes: []
conflicts: []
primary:
  decision: CLOSE
  receipt: receipt://primary-close-007
twin:
  decision: CONCUR
  receipt: receipt://twin-meta-009
commit_eligibility:
  eligible: true
  max_risk_class: R2
```

---

# 附錄 D：Event Receipt Example

```yaml
event_id: event-000128
event_type: REPARTITION
world_id: fcao-demo-world
actor:
  agent_id: twin-root-001
  role: twin
target:
  task_id: task-017
state_before: state-v42
decision:
  action: SPLIT
  reason: "Observed execution exceeded upper temporal envelope and verification queue remained blocked."
authority_ref: authority://twin-project-governance
evidence_refs:
  - estimate://task-017-v3
  - metric://verify-queue-v8
state_after: state-v43
ctcl:
  occurred_at: "2026-08-24T16:00:00+08:00"
  causal_parent: event-000127
```

---

# 附錄 E：Adapter Contract

```text
interface FCAOExecutionAdapter:
    capabilities() -> CapabilityProfile
    spawn(ExecutionRequest) -> ExecutionHandle
    send(ExecutionHandle, Message) -> ActionReceipt
    status(ExecutionHandle) -> ExecutionStatus
    collect(ExecutionHandle) -> ExecutionResult
    stop(ExecutionHandle, StopReason) -> ActionReceipt

optional:
    pause(ExecutionHandle)
    resume(ExecutionHandle)
    stream(ExecutionHandle)
```

---

# 附錄 F：v0.1 Conformance Checklist

- [ ] World ID exists.
- [ ] Canonical state exists outside Agent context.
- [ ] Primary identity is explicit.
- [ ] Twin identity is explicit when Twin mode is enabled.
- [ ] Child Agent has machine ID and ephemeral name.
- [ ] Parent lineage is preserved.
- [ ] Task graph has typed nodes and edges.
- [ ] `Single` is considered as a valid execution topology.
- [ ] Temporal Envelope is stored for scheduled tasks.
- [ ] Verification nodes are represented inside topology.
- [ ] LCC is emitted for delegated tasks.
- [ ] Twin can challenge candidate closure.
- [ ] Reopen and repartition are versioned.
- [ ] Governance-critical actions emit receipts.
- [ ] Closure Certificate exists before commit.
- [ ] Provider-specific data does not own canonical semantics.
- [ ] Telemetry can distinguish useful, invalidated, verification, and integration work.
- [ ] Benchmark can compare FCAO against simpler baselines.

---

**End of canonical source.**
