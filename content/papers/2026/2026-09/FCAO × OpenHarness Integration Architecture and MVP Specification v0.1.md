# FCAO × OpenHarness Integration Architecture and MVP Specification v0.1
## 分形式對話智能體組織 × OpenHarness 整合架構與 MVP 規格：Reuse / Extend / Patch / Fork 的最小工程路線

**English Title:** FCAO × OpenHarness Integration Architecture and MVP Specification v0.1  
**系列：** FCAO / Fractal Conversational Agent Organization  
**文件編號：** EML-FCAO-OH-2026-v0.1  
**文件類型：** Technical Whitepaper / Fit-Gap Analysis / Integration Architecture / MVP Specification  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-24  
**狀態：** Engineering Integration Draft / Canonical UTF-8 Source  
**直接前置：**
- `EML-FCAO-2026-00-v0.1` — FCAO Foundation / Integration Paper
- `EML-FCAO-2026-01-v0.1` — Twin-Agent Governance
- `EML-FCAO-2026-02-v0.1` — Temporal-Topological Computation
- `EML-FCAO-RA-2026-v0.1` — FCAO Twin-Core Reference Architecture
- OpenHarness source snapshot supplied for this study

**OpenHarness snapshot observations used in this document:**  
The inspected source includes coordinator mode, agent spawning, task management, swarm backends, teams, hooks, plugins, MCP integration, agent definitions, verification agent definitions, background execution, worktree support, memory, task notifications, and provider/runtime abstractions. This whitepaper does not assume those interfaces are frozen across future upstream versions.

**Integration Policy:**  
`Reuse first → Extend second → Patch only when generic core capability is missing → Fork only when architectural divergence becomes persistent.`

**Canonical Source Policy:**  
本文 Markdown 為正式 UTF-8 source；數學只使用 ` $...$ ` 與 `$$...$$`；不以聊天渲染文字作為 canonical source。

---

## 生成、保真與來源邊界聲明

本文是 FCAO v0.1 理論與 reference architecture 的工程落地文件。它不把 OpenHarness 宣稱為 FCAO，也不把 FCAO 宣稱為 OpenHarness 的替代品。兩者關係為：

$$
\boxed{
OpenHarness
=
ExecutionSubstrate
}
$$

以及：

$$
\boxed{
FCAO
=
CanonicalOrchestrationSemantics.
}
$$

本文對 OpenHarness 的工程判斷基於本次提供的 source snapshot，而非假設未來 upstream 版本永久保持一致。因此每一項 integration decision 都應在實作開始時以 pinned commit / release 再確認。

本文不主張需要立即 fork。相反地，v0.1 明確採：

$$
\boxed{
Upstream
+
FCAOExtension
+
MinimalPatchQueue
}
$$

作為首選。

---

# 摘要

FCAO v0.1 提出一個 Conversation-local / project-local 的分形式多智能體組織模型：一段對話可以形成 temporary local computational world；其最小治理單位不是單一 Root，而是 Primary–Twin 雙核心加 Named Ephemeral Agents；任務不是固定 step list，而是可版本化 task / verification topology；切分前需估計時間上下界，執行中可依 telemetry、verification bottleneck 與 integration risk 動態 `REOPEN`、`REASSIGN`、`SPLIT` 與 `REPARTITION`。

OpenHarness 已提供相當多 FCAO 所需的底層 execution primitives，包括 coordinator mode、background Agent spawn、agent definitions、verification agent、task manager、subprocess / in-process / terminal swarm backend、team registry、message passing、hooks、plugin manifests、MCP client/tools、memory、worktree、task notifications、usage metadata 與 provider abstractions。

因此最合理的工程策略不是從零建立新的 agent shell，也不是立即 fork OpenHarness，而是建立：

$$
\boxed{
FCAOExtensionLayer
}
$$

映射 FCAO 的 canonical state、Primary–Twin、Named Ephemeral Identity、Topology Engine、Temporal Envelope、Local Closure Certificate、Closure Certificate、CTCL-ITR receipts 與 SEDB adapter 到 OpenHarness 既有 runtime。

本文逐項將需求分類為：

$$
\boxed{
Reuse
\mid
Extend
\mid
Patch
\mid
Fork.
}
$$

初步結果為：

- **Reuse**：provider/runtime、task process、background execution、MCP、agent definitions、verification worker、worktree、memory、basic team/message primitives；
- **Extend**：Primary/Twin profiles、FCAO plugin、LCC、temporal estimator、topology store、closure engine、SEDB / CTCL adapters、telemetry、dashboard semantics；
- **Patch Candidate**：真正 recursive parent lineage、per-instance ephemeral naming、richer task/event metadata、first-class topology edge callbacks；
- **Fork**：v0.1 不建議。只有當 upstream extension surface 長期無法承載 canonical lineage、scheduler interception 或 topology semantics，且 upstream patch 不可接受時才成立。

本文進一步提出一個五階段 MVP。第一階段不改 OpenHarness core，只以 plugin + hooks + external FCAO state store 建立 Primary、Twin、Named Agent registry 與 LCC；第二階段加入 temporal envelope / topology engine；第三階段加入 Twin selective audit / closure gate；第四階段才測試 recursive child lineage patch；第五階段進 benchmark，比較 Single Agent、OpenHarness fixed coordinator、fresh verifier、FCAO Primary–Twin dynamic topology。

最終目標不是證明 FCAO 一定比 OpenHarness 原生 coordinator 更好，而是建立一套可測量實驗，使下列命題可以被驗證或否證：

$$
\boxed{
FCAOValue
=
AvoidedLateRework
+
ReducedRecomputation
+
ImprovedClosure
-
GovernanceOverhead.
}
$$

---

# 0. 工程問題

本文件只回答一個工程問題：

> FCAO 既然已有完整理論與 reference architecture，而 OpenHarness 又已提供成熟的 Agent execution substrate，我們應該如何最少改動地把 FCAO 跑起來？

不是：

> 如何把 OpenHarness 改成另一個產品？

也不是：

> 如何維護一個永久 fork？

---

# 1. OpenHarness 在 FCAO 中的位置

FCAO reference architecture：

$$
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
$$

OpenHarness 最適合承載：

$$
Execution
+
部分 Delegation
+
部分 Verification
+
部分 Identity
+
ToolProtocol.
$$

FCAO 自己保留：

$$
World
+
CanonicalState
+
TwinSemantics
+
Topology
+
Temporal
+
Closure
+
Ledger.
$$

所以：

$$
\boxed{
FCAO
\not\subseteq
OpenHarnessContext.
}
$$

---

# 2. 本次 source snapshot 中已確認的 OpenHarness primitives

本次 source inspection 確認至少有：

1. `CoordinatorMode`
2. `AgentTool`
3. `TaskManager`
4. `TaskRecord`
5. `TeammateSpawnConfig`
6. subprocess swarm backend
7. in-process backend
8. tmux / iTerm2 teammate backend
9. team registry
10. task notification
11. `send_message`
12. `task_stop`
13. agent definitions
14. verification agent definition
15. plugin manifest
16. plugin agents / tools / hooks
17. hook events
18. MCP client / tools
19. memory
20. worktree / isolation support
21. usage fields including token / tool / duration
22. project / user plugin loading
23. background Agent lifecycle

這些已足以支撐 FCAO MVP 的 execution carrier。

---

# 3. OpenHarness coordinator 對 FCAO Primary

OpenHarness Coordinator 已負責：

- user goal；
- worker dispatch；
- result synthesis；
- verification worker；
- task stop；
- follow-up message。

因此：

$$
OpenHarnessCoordinator
\approx
PrimaryExecutionCarrier.
$$

但不能直接等同：

$$
OpenHarnessCoordinator
=
FCAOPrimary.
$$

因為 FCAO Primary 還需要：

- canonical World ID；
- task topology；
- Temporal Envelope；
- decomposition decision；
- versioned closure；
- Twin peer；
- CTCL receipt；
- SEDB state projection。

所以分類：

$$
\boxed{
Primary:
Reuse
+
Extend.
}
$$

---

# 4. OpenHarness verification agent 對 FCAO Twin

OpenHarness 已有 verification agent，且其設計目標是：

- fresh verification；
- try to break implementation；
- run tests；
- return evidence；
- avoid self-confirmation。

這非常適合：

$$
FreshVerifier.
$$

但 FCAO Twin 是：

$$
PersistentTwin
\neq
FreshVerifier.
$$

Twin 還需要：

- project-wide structural observation；
- audit priority；
- topology hole detection；
- temporal breach monitoring；
- `REOPEN`；
- `REPARTITION`；
- closure challenge；
- temporary arbiter policy。

因此：

$$
\boxed{
VerificationAgent:
ReuseAsFreshVerifier
}
$$

而：

$$
\boxed{
PersistentTwin:
Extend.
}
$$

---

# 5. AgentTool 與 Named Ephemeral Agent

現有 `AgentToolInput` 有：

- `description`
- `prompt`
- `subagent_type`
- `model`
- `command`
- `team`
- `mode`

spawn 時目前以：

$$
agent\_name
=
subagent\_type
\lor
"agent".
$$

這不足以表達：

$$
AgentType
\neq
EphemeralName
\neq
TaskName.
$$

FCAO 要求：

```yaml
agent_id: ag-017
ephemeral_name: Atlas
agent_type: worker
task_name: Storage Topology
parent_agent_id: primary-root
```

因此第一階段可以在 external FCAO registry 中維持 mapping：

$$
OpenHarnessTaskID
\leftrightarrow
FCAOAgentIdentity.
$$

分類：

$$
\boxed{
EphemeralIdentity:
ExtendFirst.
}
$$

若 UI / task notification 必須直接顯示 per-instance name，再考慮 core patch。

---

# 6. 真正 parent lineage

現有 Agent spawn config 在 inspected snapshot 中使用：

```text
parent_session_id = "main"
```

這對普通 coordinator → worker 足夠，但 FCAO recursive delegation 需要：

$$
A_0
\rightarrow
A_1
\rightarrow
A_{1,1}.
$$

真正需要保存：

$$
parent\_agent\_id.
$$

v0.1 可以先由 FCAO external state 記錄 logical parent：

$$
LogicalParent
\neq
RuntimeParentSession.
$$

如果 child 真的需要原生 recursive spawn 且 runtime security / context 必須依 lineage 自動處理，才需要 core patch。

分類：

$$
\boxed{
RecursiveLineage:
Extend
\rightarrow
PatchCandidate.
}
$$

---

# 7. TaskRecord 對 FCAO Task Node

OpenHarness `TaskRecord` 目前核心狀態接近：

$$
TaskRecord
=
(
id,
type,
status,
description,
cwd,
output,
timestamps,
metadata
).
$$

FCAO Task Node：

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

兩者不是同一層。

因此不應硬塞 FCAO 全部語義進 `TaskRecord`。

推薦：

$$
OpenHarnessTaskRecord
=
ExecutionRecord
$$

而：

$$
FCAOTaskNode
=
CanonicalTaskObject.
$$

用 `task_id` / metadata 對接。

分類：

$$
\boxed{
TaskRuntime:
Reuse
}
$$

$$
\boxed{
TaskTopology:
Extend.
}
$$

---

# 8. TeamRegistry 對 FCAO 分形組織

OpenHarness TeamRegistry 有：

- team name；
- members；
- messages。

這能承載：

$$
LocalTeam.
$$

但 FCAO team 還需要：

- parent team；
- world；
- task region；
- authority；
- topology scope；
- Twin activation；
- lifecycle。

因此：

$$
TeamRegistry
$$

可直接做 UI / runtime grouping，但 canonical fractal organization 應由 FCAO state 保留。

分類：

$$
\boxed{
TeamRuntime:
Reuse
+
Extend.
}
$$

---

# 9. TaskNotification 對 FCAO Result Packet

OpenHarness TaskNotification 已有：

$$
(
task\_id,
status,
summary,
result,
usage
).
$$

usage 有：

$$
total\_tokens,
tool\_uses,
duration\_ms.
$$

FCAO Local Result Packet：

$$
LRP
=
(
Artifact,
Claims,
Evidence,
Coverage,
Assumptions,
OpenGaps,
Conflicts,
Usage,
LCC
).
$$

現有 notification 很適合當 transport envelope，但不足以當 closure object。

方案：

1. worker 產生 LCC artifact / JSON；
2. task notification metadata 引用 LCC URI；
3. FCAO hook 在 `subagent_stop` 時讀取 LCC；
4. 更新 canonical topology。

分類：

$$
\boxed{
TaskNotification:
ReuseAsTransport
+
ExtendWithLCCRef.
}
$$

---

# 10. Hooks 是 FCAO 最重要的 extension surface

目前 hook events 包含：

- session start / end；
- pre / post compact；
- pre / post tool use；
- user prompt submit；
- notification；
- stop；
- subagent stop。

FCAO 第一版最重要的 hook：

$$
SUBAGENT\_STOP.
$$

因為它可以：

$$
TaskComplete
\rightarrow
ReadLCC
\rightarrow
UpdateTopology
\rightarrow
UpdateTemporalEstimate
\rightarrow
TriggerTwinInspection.
$$

`POST_TOOL_USE` 也可用於 telemetry。

因此：

$$
\boxed{
Hooks:
ReuseStrongly.
}
$$

---

# 11. Plugin system

OpenHarness PluginManifest 已提供：

- tools；
- hooks；
- MCP；
- agents；
- skills；
- commands。

這非常接近 FCAO 所需的非 fork extension surface。

推薦 plugin：

```text
.openharness/plugins/fcao/
├── plugin.json
├── agents/
│   ├── fcao-primary.md
│   ├── fcao-twin.md
│   ├── fcao-auditor.md
│   └── fcao-arbiter.md
├── tools/
│   ├── topology.py
│   ├── temporal.py
│   ├── closure.py
│   ├── lcc.py
│   └── state.py
├── hooks.json
├── mcp.json
├── schemas/
└── profiles/
```

分類：

$$
\boxed{
FCAOPlugin:
Extend.
}
$$

---

# 12. MCP

OpenHarness 已有 MCP client / resource / auth / tool support。

因此 FCAO 不需要自己重造 MCP stack。

MCP 在 FCAO 中：

$$
MCP
=
ExecutionAndResourceAdapter.
$$

不是：

$$
MCP
=
ProjectOntology.
$$

分類：

$$
\boxed{
MCP:
Reuse.
}
$$

---

# 13. CLI / subprocess

OpenHarness subprocess backend 已提供：

- background task；
- process execution；
- polling；
- result collection。

適合：

- coding Agent；
- CLI Agent；
- local model runner；
- isolated worker。

FCAO 只需要封裝：

$$
ExecutionHandle
\leftrightarrow
AgentIdentity.
$$

分類：

$$
\boxed{
CLI/Subprocess:
Reuse.
}
$$

---

# 14. Worktree / isolation

多 coding Agents 共用 repo 時，worktree 能降低：

$$
FileConflict.
$$

FCAO 把它視為：

$$
E^{resource}
$$

的一種工程實現。

分類：

$$
\boxed{
Worktree:
Reuse.
}
$$

---

# 15. Memory

OpenHarness memory 可承載：

- session continuity；
- Agent memory；
- team memory。

但 FCAO canonical state 不應只依賴 memory subsystem。

因此：

$$
Memory
=
ContextSupport
$$

而：

$$
CanonicalState
=
ExternalStateStore.
$$

分類：

$$
\boxed{
Memory:
ReuseAsContext
}
$$

$$
\boxed{
CanonicalState:
ExtendExternally.
}
$$

---

# 16. Coordinator mode 的限制

OpenHarness coordinator prompt 已有很好的 engineering delegation heuristic，但它仍主要以：

$$
Coordinator
\rightarrow
Workers
\rightarrow
Coordinator.
$$

為中心。

FCAO 需要：

$$
Primary
\parallel
Twin.
$$

因此不建議直接大改 coordinator prompt 來假裝 Twin。

應建立獨立 persistent Twin session / agent record，透過 FCAO state event 與 hooks 接收 project updates。

---

# 17. Twin runtime design

推薦：

```text
Primary Session
    |
    +---- FCAO State Store ---- Twin Session
    |              |                |
    |              |                +-- Audit Agent
    |              |                +-- Fresh Verifier
    |              |
    +-- Workers ---+
```

Twin 不需要收到所有 worker token stream。

它只需要：

- task transition；
- temporal estimate；
- LCC；
- verification result；
- risk change；
- topology version；
- closure candidate。

---

# 18. Twin event subscription

v0.1 由 FCAO hook / state event bus 實作。

事件：

$$
\{
TASK\_COMPLETE,
ESTIMATE\_BREACH,
VERIFY\_FAIL,
MERGE\_READY,
CONFLICT,
CLOSURE\_CANDIDATE
\}.
$$

Twin 只在 policy 需要時 wake。

因此：

$$
PersistentTwin
$$

不代表持續燒 token。

---

# 19. Twin IDLE

若沒有高價值 intervention：

$$
TwinDecision
=
IDLE.
$$

這對成本控制非常重要。

---

# 20. Topology Engine 不應塞進 OpenHarness TaskManager v0.1

第一版推薦 external SQLite / SEDB-compatible store：

```text
worlds
agents
tasks
edges
delegations
estimates
lcc
verification
events
closures
```

OpenHarness TaskManager 只負責實際執行生命週期。

因此：

$$
\boxed{
ExecutionState
\neq
CanonicalTaskTopology.
}
$$

---

# 21. Temporal Engine

第一版不需要 machine learning。

只需：

- heuristic lower / upper；
- task-class defaults；
- observed duration；
- historical percentile；
- verification allowance；
- retry allowance。

object：

```yaml
target: task-017
lower_ms: 180000
upper_ms: 720000
confidence: 0.6
```

當：

$$
Observed>T^{+},
$$

產生：

$$
ESTIMATE\_BREACH.
$$

---

# 22. Temporal Engine 與 OpenHarness usage

TaskNotification / task metadata 已能提供：

- duration；
- token；
- tool use。

這些可直接回填：

$$
HistoricalRun.
$$

因此：

$$
\boxed{
Telemetry:
Reuse
+
Extend.
}
$$

---

# 23. LCC 實作

v0.1 worker output contract 增加：

```json
{
  "status": "partial",
  "artifacts": [],
  "verified": [],
  "open_gaps": [],
  "assumptions": [],
  "receipts": []
}
```

最初可存：

```text
.fcao/runs/<task_id>/lcc.json
```

之後再換 SEDB。

---

# 24. LCC 不要求修改每個 provider

可由 wrapper prompt / agent definition 要求 worker 最後輸出固定 machine-readable artifact。

因此：

$$
LCC
$$

先屬於：

$$
Extend.
$$

不需要 core patch。

---

# 25. Closure Engine

第一版 external tool：

```text
fcao_closure_check(world_id)
```

檢查：

- mandatory node；
- LCC；
- verification；
- open gap；
- conflict；
- deferred node；
- topology version。

輸出：

$$
GCC.
$$

---

# 26. Primary closure challenge

Primary 提出：

$$
CANDIDATE\_CLOSURE.
$$

Twin 檢查後回：

- `CONCUR`
- `CHALLENGE`
- `REOPEN`
- `ESCALATE`

只有通過 policy 才 `CLOSE`。

---

# 27. REOPEN mapping

OpenHarness 已有：

- send message；
- task stop；
- re-spawn。

所以第一代 `REOPEN` 不需要 core primitive。

FCAO state 先：

$$
CLOSED
\rightarrow
REOPENED.
$$

然後 scheduler：

- follow-up existing Agent；
- spawn new Agent；
- spawn verifier；
- reassign。

分類：

$$
\boxed{
REOPEN:
Extend.
}
$$

---

# 28. REPARTITION mapping

第一代 repartition 由外部 Topology Engine 改圖，再使用 existing AgentTool / task stop / send_message 執行。

因此：

$$
\boxed{
REPARTITION:
Extend.
}
$$

只有當需要 atomic scheduler interception 才考慮 patch。

---

# 29. Stop / pause

OpenHarness 已有 task stop。

如果未來 FCAO 要：

$$
PAUSE
\rightarrow
RESUME
$$

且 backend 不一致，可能要 extension / patch。

v0.1 不把 pause/resume 列為硬依賴。

---

# 30. Fit-Gap Summary

## Reuse

- coordinator execution
- worker spawn
- task process
- task stop
- send_message
- MCP
- worktree
- memory
- verification worker
- agent definitions
- provider runtime
- background tasks
- basic teams
- usage metadata
- plugin loader
- hooks

## Extend

- FCAO World
- Primary profile
- Persistent Twin
- Named Ephemeral Identity registry
- topology graph
- temporal envelope
- candidate decomposition
- LCC
- closure engine
- CTCL receipts
- SEDB adapter
- Twin event bus
- audit priority
- dynamic repartition
- benchmark harness

## Patch Candidate

- actual recursive runtime parent lineage
- per-instance Agent display name in spawn path
- richer task metadata / event payload
- topology-native scheduler callback
- first-class pause/resume if required

## Fork

v0.1：

$$
\boxed{
NO.
}
$$

---

# 31. 為什麼現在不 fork

Fork 會立即產生：

- upstream merge burden；
- security patch burden；
- provider compatibility burden；
- CLI/TUI maintenance；
- MCP maintenance；
- test drift；
- duplicated infrastructure work。

而 FCAO 真正新意主要在：

$$
Twin
+
Topology
+
Temporal
+
Closure
+
Ledger.
$$

這些目前大部分能放在 extension layer。

---

# 32. Patch policy

只有當：

$$
ExtensionSurface
<
RequiredSemantics
$$

且 blocker 是 generic capability 時，先提出 upstream patch。

例如：

> expose actual parent agent ID in spawn configuration.

這對任何 recursive orchestration 都有價值。

---

# 33. Fork criteria

只有同時滿足：

1. blocker 位於 core execution path；
2. plugin / hook 無法解；
3. upstream generic patch 不接受；
4. FCAO 需要長期不同 semantics；
5. patch queue 持續擴大；
6. merge cost 已高於 fork ownership benefit；

才：

$$
Fork=TRUE.
$$

---

# 34. Fork Decision Metric

可以定義：

$$
FDM
=
C_{patch\_maintenance}
+
C_{upstream\_conflict}
-
C_{fork\_ownership}.
$$

當：

$$
FDM>\theta_F
$$

且 architecture divergence 穩定，才考慮 fork。

---

# 35. Repository strategy

建議新 repo：

```text
fcao-openharness
```

但不是 OpenHarness fork。

它是 integration layer：

```text
fcao-openharness/
├── README.md
├── plugin/
├── schemas/
├── runtime/
├── adapters/
├── benchmarks/
├── tests/
├── examples/
└── vendor-lock/
```

---

# 36. Upstream pin

保存：

```yaml
openharness:
  repository: HKUDS/OpenHarness
  commit: <PINNED_SHA>
  release: <OPTIONAL_RELEASE>
```

不要依賴 floating `main` 作 benchmark baseline。

---

# 37. License handling

若使用 OpenHarness 原始碼、copy / modify code，必須依其 LICENSE 保留相應 notice。

若純 plugin / external integration，只需依實際分發內容決定 notice placement。

v0.1 package 應保留：

```text
THIRD_PARTY_NOTICES.md
```

---

# 38. FCAO Plugin Manifest

範例：

```json
{
  "name": "fcao",
  "version": "0.1.0",
  "description": "FCAO Twin-Core orchestration extension",
  "enabled_by_default": true,
  "tools_dir": "tools",
  "hooks_file": "hooks.json",
  "agents": "agents"
}
```

---

# 39. FCAO Agents

至少：

```text
fcao-primary
fcao-twin
fcao-auditor
fcao-arbiter
fcao-integrator
```

其中：

- auditor 是 fresh verifier；
- arbiter 是 temporary；
- integrator 是 optional hierarchical merge worker。

---

# 40. FCAO Tools

最小：

```text
fcao_world_get
fcao_task_get
fcao_topology_get
fcao_topology_propose
fcao_temporal_estimate
fcao_lcc_submit
fcao_reopen
fcao_repartition
fcao_closure_check
fcao_event_append
```

---

# 41. Hooks

第一版：

```json
{
  "subagent_stop": ["fcao_on_subagent_stop"],
  "post_tool_use": ["fcao_on_post_tool_use"],
  "session_start": ["fcao_on_session_start"],
  "session_end": ["fcao_on_session_end"]
}
```

---

# 42. subagent_stop workflow

$$
SUBAGENT\_STOP
\rightarrow
CollectTask
\rightarrow
LoadLCC
\rightarrow
AppendEvent
\rightarrow
UpdateEstimate
\rightarrow
UpdateTopology
\rightarrow
MaybeWakeTwin.
$$

---

# 43. post_tool_use workflow

只保存必要 telemetry：

- tool class；
- duration；
- status；
- target resource；
- cost if available。

不保存 hidden reasoning。

---

# 44. Canonical State Backend v0.1

第一版推薦：

$$
SQLite
+
JSONArtifacts.
$$

理由：

- local-first；
- deterministic；
- easy test；
- easy replay；
- no external dependency。

之後：

$$
SEDBAdapter.
$$

---

# 45. Minimal tables

```text
world
agent
task
edge
delegation
estimate
artifact
lcc
verification
event
closure
```

---

# 46. Event ID

所有治理 event：

$$
EventID
$$

唯一。

OpenHarness task ID、Agent ID 只是 references。

---

# 47. Identity mapping

建立：

```text
fcao_agent_id
openharness_agent_id
openharness_task_id
ephemeral_name
role
parent_fcao_agent_id
```

因此 runtime implementation 可以替換。

---

# 48. Primary bootstrap

使用者進入 FCAO mode：

1. 建 World；
2. assign Primary；
3. load policy；
4. load / create Twin；
5. create initial topology；
6. persist `WORLD_OPEN`。

---

# 49. Twin bootstrap

Twin 初始只讀：

- world summary；
- topology；
- policy；
- risk；
- estimates。

不需要複製 Primary 全 context。

---

# 50. Candidate decomposition MVP

v0.1 只生成：

$$
Single,
Split2,
SplitK.
$$

不要一開始做任意 graph optimization。

---

# 51. Decomposition output

```yaml
candidate: split-3
tasks:
  - task-a
  - task-b
  - task-c
dependencies: []
verification:
  - merge-check
expected:
  lower_ms: 300000
  upper_ms: 900000
```

---

# 52. NO_SPLIT test

MVP 必須有至少一個 case：

$$
Single
$$

勝出。

否則 scheduler 可能只是：

> always spawn agents.

這不符合 FCAO。

---

# 53. Twin selective audit MVP

Twin 不持續全讀。

只有：

$$
\Pi(v)>\theta
$$

才：

- inspect LCC；
- spawn auditor；
- challenge merge；
- reopen。

---

# 54. Audit Agent reuse

OpenHarness verification agent 可以直接作：

$$
FreshVerifier.
$$

只需 wrapper contract 要求 machine-readable receipt。

---

# 55. Arbiter

第一版可以仍用 generic fresh Agent：

```text
subagent_type = verification / plan
```

外部 FCAO registry 標記 role=`arbiter`。

不需要修改 OpenHarness built-in role system。

---

# 56. Hierarchical merge

如果：

$$
fan\_in>\theta,
$$

Primary 可以 spawn integrator worker。

其 output 仍需 LCC / merge certificate。

---

# 57. Temporal breach

當 observed duration 超過：

$$
T^{+},
$$

hook / scheduler 產生：

```text
ESTIMATE_BREACH
```

Twin wake：

- inspect；
- IDLE；
- REASSIGN；
- SPLIT；
- STOP；
- escalate。

---

# 58. Verification bottleneck

若：

$$
Queue_V>\theta_V,
$$

Twin 可以：

- spawn fresh verifier；
- 降低低風險 audit；
- 暫停新 speculative task。

---

# 59. Integration bottleneck

若 Primary pending results 過多：

$$
Queue_I>\theta_I,
$$

scheduler 可：

- hierarchical merge；
- freeze fan-out；
- create integrator。

---

# 60. Recursive Agent MVP boundary

第一版不要求 child 原生 spawn child。

先由 Primary 代行 logical recursive spawn：

```text
A1 requests subdelegation
→ FCAO state validates authority
→ Primary/Runtime spawns A1.1
→ parent_fcao_agent_id = A1
```

因此 FCAO semantic recursion 可先成立，而不改 core。

---

# 61. Native recursive spawn patch

第二階段才測：

- child calls AgentTool；
- real parent session / agent ID propagation；
- subdelegation authority inheritance；
- nested team / topology scope。

若無法用 plugin 解，就形成 upstream patch proposal。

---

# 62. Patch 01 candidate：Ephemeral Name

理想新增：

```python
ephemeral_name: str | None
```

與：

```python
agent_name = ephemeral_name or subagent_type or "agent"
```

這是低風險 generic patch。

---

# 63. Patch 02 candidate：Parent Identity

理想：

```python
parent_session_id=context.session_id
parent_agent_id=context.agent_id
```

而不是固定 `main`。

---

# 64. Patch 03 candidate：Task Metadata

TaskRecord metadata 已有 dict，但若需要 typed structured metadata，可提出：

```python
metadata: dict[str, Any]
```

或 extension field。

---

# 65. Patch 04 candidate：Hook Event

如果 `subagent_stop` 不足以捕捉：

- task start；
- task status change；
- spawn；
- message；
- verification state；

可以提出 generic lifecycle events。

---

# 66. 不應先 patch 的東西

不要為 FCAO 直接改：

- provider；
- TUI；
- MCP client；
- terminal；
- memory core；
- worktree；
- command parser；

除非有明確 blocker。

---

# 67. MVP Phase 0 — Carrier Verification

目標：確認 OpenHarness snapshot 可作穩定 carrier。

測：

- spawn；
- task poll；
- stop；
- message；
- verifier；
- hooks；
- plugin；
- MCP；
- usage。

輸出：

$$
CarrierCapabilityReceipt.
$$

---

# 68. MVP Phase 1 — FCAO State + Identity

完成：

- World；
- Primary；
- Twin registry；
- child identity；
- task graph；
- event store；
- no topology optimization yet。

---

# 69. MVP Phase 2 — LCC + Closure

完成：

- worker LCC；
- subagent_stop ingestion；
- global closure engine；
- Twin challenge；
- fresh verifier。

---

# 70. MVP Phase 3 — Temporal Topology

完成：

- envelope；
- candidate split；
- NO_SPLIT；
- estimate breach；
- one repartition；
- topology version。

---

# 71. MVP Phase 4 — Recursive Semantics

完成：

- logical recursive delegation；
- authority propagation；
- nested lineage；
- optional native parent patch experiment。

---

# 72. MVP Phase 5 — SEDB / CTCL

完成：

- CTCL event fields；
- SEDB state projection；
- replay；
- snapshot；
- long-running project restore。

---

# 73. MVP Phase 6 — Benchmark

四組：

1. Single Agent；
2. OpenHarness Coordinator fixed decomposition；
3. OpenHarness + fresh verifier；
4. FCAO Primary–Twin dynamic topology。

---

# 74. Benchmark Case A — Tiny task

期望：

$$
FCAO
\rightarrow
NO\_SPLIT.
$$

若 FCAO 反而多開多個 Agent，失敗。

---

# 75. Case B — Independent branches

期望：

$$
SPLIT
$$

降低 makespan。

---

# 76. Case C — High coupling

期望：

$$
MERGE
$$

或較小 fan-out。

---

# 77. Case D — Hidden defect

worker 局部看似完成，但 merge invariant 失敗。

期望：

$$
Twin
\rightarrow
REOPEN.
$$

---

# 78. Case E — Temporal breach

一個 child 超過 upper envelope。

期望：

$$
Twin/Primary
\rightarrow
REPARTITION
$$

或 `REASSIGN`。

---

# 79. Case F — Verification queue

worker 完成速度高於 verifier throughput。

期望 Twin 不繼續盲目 fan-out。

---

# 80. Case G — False closure

Primary candidate closure 漏掉 mandatory node。

期望 Twin：

$$
CHALLENGE.
$$

---

# 81. Case H — Twin overhead

低風險 task 中 Twin 不應過度工作。

期望：

$$
Twin=IDLE
$$

或 LIGHT mode。

---

# 82. Metrics

至少：

$$
T_{makespan},
$$

$$
TokenCost,
$$

$$
ToolCalls,
$$

$$
UsefulWorkRatio,
$$

$$
LateReworkCost,
$$

$$
FalseClosureRate,
$$

$$
VerificationRecomputeRatio,
$$

$$
TwinMarginalValue,
$$

$$
RepartitionCount,
$$

$$
EstimateCalibration.
$$

---

# 83. Success criterion

FCAO MVP 不以：

> Agent 數量更多

為成功。

成功是：

1. 能選擇不切；
2. 能形成 named worker；
3. 能保存 logical parent lineage；
4. 能用 LCC 降低重算；
5. Twin 能 selective audit；
6. 能在 breach 後改 topology；
7. closure 可被 challenge；
8. event 可 replay；
9. OpenHarness 可升級而 FCAO state 不破裂。

---

# 84. Failure criterion

若以下任一成立，需重新設計：

- plugin 無法穩定讀取 task lifecycle；
- task / Agent mapping 無法可靠建立；
- Twin 必須 full duplicate 才能工作；
- topology state 只能塞在 prompt；
- 每次 OpenHarness update 都破壞 FCAO；
- core patch 數快速增長；
- external state 與 runtime state 無法 reconcile。

---

# 85. Runtime reconciliation

定義：

$$
Reconcile(
FCAOState,
OpenHarnessRuntime
).
$$

若 runtime 有 task：

$$
task\_id=x
$$

但 FCAO 無對應：

$$
OrphanExecution.
$$

若 FCAO task running，但 runtime 不存在：

$$
LostExecution.
$$

都要 event 化。

---

# 86. Orphan handling

OrphanExecution：

- adopt；
- stop；
- ignore；

依 policy。

不得 silent merge。

---

# 87. Lost execution

LostExecution：

$$
RUNNING
\rightarrow
BLOCKED
$$

再：

- restore；
- reassign；
- fail。

---

# 88. Snapshot restore

project restore：

1. load FCAO snapshot；
2. replay events；
3. query OpenHarness tasks；
4. reconcile；
5. resume Primary / Twin；
6. reopen stale tasks。

---

# 89. Context compaction

OpenHarness 有 pre/post compact hooks。

FCAO 可利用：

$$
PRE\_COMPACT
$$

保存：

- current world state ref；
- topology version；
- active task refs；
- unresolved conflict。

避免 compaction 破壞 continuity。

---

# 90. Security

Project plugin / hook 是 executable extension。

因此 FCAO plugin 必須：

- source controlled；
- pinned；
- reviewed；
- no arbitrary credential logging；
- respect permissions；
- deny unauthorized world commit。

---

# 91. Twin authority

Twin 不應預設 shell admin。

其第一版 authority：

- read project state；
- inspect artifact；
- spawn verifier；
- propose reopen；
- propose repartition；
- challenge closure。

直接 destructive action 仍需 Primary / policy gate。

---

# 92. Arbiter authority

Temporary arbiter：

$$
Authority
\preceq
DisputeScope.
$$

不得因仲裁獲得全 project 控制。

---

# 93. Protocol neutrality

即使 OpenHarness 日後被替換：

$$
FCAOState
+
Schemas
+
Events
+
Topology
$$

仍可保留。

只需替換：

$$
ExecutionAdapter.
$$

這是避免 vendor lock-in 的核心。

---

# 94. OpenHarness-specific code boundary

所有 OpenHarness-specific implementation 限制在：

```text
adapters/openharness/
```

核心：

```text
fcao/core/
```

不得 import OpenHarness internal class。

理想 interface：

```text
FCAOCore
→ ExecutionAdapter Protocol
→ OpenHarnessAdapter
```

---

# 95. Import policy

Core 層只能依賴 FCAO 自己的 protocols / schemas。

禁止：

```python
from openharness.tasks import ...
```

出現在：

```text
fcao/core/
```

只能出現在：

```text
fcao/adapters/openharness/
```

---

# 96. Upstream update policy

每次 upgrade：

1. update pinned ref；
2. run carrier tests；
3. run adapter contract tests；
4. run FCAO benchmark smoke；
5. compare behavior；
6. promote version。

---

# 97. Compatibility manifest

保存：

```yaml
fcao_version: 0.1
openharness:
  tested_commit: ...
  tested_version: ...
compatibility:
  plugin: pass
  hooks: pass
  spawn: pass
  task_notification: pass
  mcp: pass
  verifier: pass
```

---

# 98. Implementation directory

推薦：

```text
fcao-openharness/
├── fcao/
│   ├── core/
│   │   ├── world.py
│   │   ├── topology.py
│   │   ├── temporal.py
│   │   ├── identity.py
│   │   ├── closure.py
│   │   └── events.py
│   ├── adapters/
│   │   ├── openharness/
│   │   ├── sedb/
│   │   └── ctcl_itr/
│   ├── schemas/
│   └── benchmark/
├── openharness-plugin/
│   ├── plugin.json
│   ├── agents/
│   ├── tools/
│   └── hooks.json
└── tests/
```

---

# 99. v0.1 Engineering Invariants

## Invariant 1

$$
OpenHarness
\neq
CanonicalStateOwner.
$$

## Invariant 2

$$
RuntimeTaskID
\neq
FCAOTaskID.
$$

## Invariant 3

$$
OpenHarnessAgentID
\neq
FCAOAgentIdentity.
$$

## Invariant 4

$$
PersistentTwin
\neq
VerificationWorker.
$$

## Invariant 5

$$
PluginFirst
>
ForkFirst.
$$

作為工程政策，而非數學序關係。

## Invariant 6

$$
LogicalRecursiveLineage
$$

必須先於 native recursive spawn 成立。

## Invariant 7

$$
LCC
$$

不得只存在自由文字 summary。

## Invariant 8

$$
Topology
$$

不得只存在 Primary prompt。

## Invariant 9

$$
TemporalEnvelope
$$

必須可以被 observed telemetry 修正。

## Invariant 10

$$
REPARTITION
\Rightarrow
TopologyVersion
+
Receipt.
$$

## Invariant 11

$$
Closure
\Rightarrow
GCC.
$$

## Invariant 12

$$
Fork
$$

需要具體 blocker，不可因「未來可能改」而先 fork。

---

# 100. 結論

本次 source inspection 顯示，OpenHarness 已經提供 FCAO 最難重造、但理論上並非 FCAO 核心貢獻的一大批 infrastructure：

$$
Coordinator
+
AgentSpawn
+
TaskRuntime
+
Swarm
+
VerificationWorker
+
Hooks
+
Plugins
+
MCP
+
Memory
+
Worktree
+
BackgroundExecution.
$$

因此 FCAO 不需要重新寫一套完整 agent CLI / harness。

真正應該建立的是：

$$
\boxed{
FCAOExtensionLayer
=
World
+
CanonicalState
+
PrimaryTwin
+
NamedIdentity
+
Topology
+
Temporal
+
LCC
+
Closure
+
Ledger.
}
$$

OpenHarness 只作：

$$
\boxed{
ExecutionCarrier.
}
$$

v0.1 的 Fit-Gap 結論不是：

> fork OpenHarness。

而是：

$$
\boxed{
Reuse
\rightarrow
Extend
\rightarrow
Measure
\rightarrow
PatchIfNecessary
\rightarrow
ForkOnlyIfArchitecturallyForced.
}
$$

這個順序同時降低 maintenance cost 與 upstream divergence，也保留 FCAO protocol-agnostic 的本體地位。

最重要的是，FCAO 的 MVP 現在不再需要從 provider、terminal、tool calling、MCP、swarm、verification worker 開始。工程可以直接從真正有研究差異的地方開始：

$$
\boxed{
Primary
\parallel
Twin
}
$$

$$
\boxed{
NamedEphemeralAgents
}
$$

$$
\boxed{
DynamicTaskVerificationTopology
}
$$

$$
\boxed{
[T^{-},T^{+}]
}
$$

$$
\boxed{
LCC
+
REOPEN
+
REPARTITION
+
GCC.
}
$$

因此本文件完成後，FCAO v0.1 已具備：

1. 三篇理論文；
2. 一份 protocol-agnostic Reference Architecture；
3. 一份 OpenHarness Fit-Gap / Integration Whitepaper；
4. machine-readable schemas；
5. MVP phase plan；
6. benchmark plan；
7. fork decision policy。

下一個合理產物已不是新論文或新白皮書，而是：

$$
\boxed{
FCAO\text{-}OpenHarness\ MVP\ v0.1.
}
$$

也就是開始真正跑。

---

# 附錄 A：Fit-Gap Matrix

| FCAO Requirement | OpenHarness Primitive | v0.1 Decision |
|---|---|---|
| Primary execution | CoordinatorMode | Reuse + Extend |
| Persistent Twin | Verification / Agent runtime | Extend |
| Fresh verifier | verification agent | Reuse |
| Named ephemeral agent | AgentTool / agent name | Extend, optional Patch |
| Recursive lineage | parent_session / task metadata | Extend, Patch candidate |
| Task execution | TaskManager | Reuse |
| Task topology | none first-class | Extend |
| Verification topology | verifier + external graph | Extend |
| Temporal envelope | usage duration only | Extend |
| Dynamic repartition | spawn/stop/message primitives | Extend |
| LCC | no canonical LCC | Extend |
| Closure certificate | no canonical GCC | Extend |
| CTCL receipt | hooks + timestamps | Extend |
| SEDB canonical state | memory / external storage | Extend |
| MCP | MCP client/tools | Reuse |
| CLI/subprocess | swarm subprocess | Reuse |
| Worktree isolation | worktree | Reuse |
| Team grouping | TeamRegistry | Reuse + Extend |
| Lifecycle hooks | HookEvent | Reuse |
| Native recursive parent | hard-coded / limited lineage | Patch candidate |
| Full FCAO semantics | none | Extension layer |
| Fork | not required | No |

---

# 附錄 B：MVP Acceptance Checklist

- [ ] Pin OpenHarness snapshot.
- [ ] Build FCAO plugin shell.
- [ ] Create World ID.
- [ ] Register Primary.
- [ ] Register Persistent Twin.
- [ ] Spawn child with FCAO machine ID + ephemeral name.
- [ ] Preserve logical parent lineage.
- [ ] Maintain task graph outside prompt.
- [ ] Emit LCC.
- [ ] Ingest `subagent_stop`.
- [ ] Store duration/token/tool telemetry.
- [ ] Create Temporal Envelope.
- [ ] Demonstrate `NO_SPLIT`.
- [ ] Demonstrate `SPLIT`.
- [ ] Demonstrate Twin `IDLE`.
- [ ] Demonstrate Twin fresh verifier.
- [ ] Demonstrate `REOPEN`.
- [ ] Demonstrate `REPARTITION`.
- [ ] Emit topology version.
- [ ] Emit CTCL-style event receipt.
- [ ] Emit Global Closure Certificate.
- [ ] Reconcile runtime tasks after restart.
- [ ] Compare against three baselines.

---

# 附錄 C：Fork Decision Record Template

```yaml
decision_id: fork-decision-001
fcao_version: 0.1
openharness_commit: "<sha>"
blockers:
  - requirement: recursive_parent_lineage
    extension_possible: false
    upstream_patch_possible: true
  - requirement: first_class_topology_callback
    extension_possible: true
patch_queue_size: 1
upstream_merge_cost: low
fork_ownership_cost: high
decision: DO_NOT_FORK
reason:
  - "Current blockers remain solvable through extension or generic upstream patch."
```

---

# 附錄 D：Compatibility Manifest Example

```yaml
fcao_version: 0.1
openharness:
  repository: HKUDS/OpenHarness
  tested_commit: "<PINNED_SHA>"
compatibility:
  plugin_loader: pass
  hook_subagent_stop: pass
  agent_spawn: pass
  task_polling: pass
  task_stop: pass
  message: pass
  verifier: pass
  mcp: pass
  worktree: pass
known_gaps:
  - native_recursive_parent_lineage
  - per_instance_ephemeral_name
```

---

**End of canonical source.**
