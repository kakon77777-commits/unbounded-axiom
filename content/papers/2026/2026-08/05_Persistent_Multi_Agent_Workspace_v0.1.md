# Persistent Multi-Agent Workspace
## 跨對話共享世界 Runtime、持久協作協定與 MVP

**English Title:** *Persistent Multi-Agent Workspace: A Runtime, Durable Collaboration Protocol, and MVP for Cross-Conversation Shared Worlds*  
**系列：**《跨對話智能協作與共享認知空間》第五篇（系列封頂）  
**性質：** 公開理論論文／工程架構白皮書／Runtime MVP 規格  
**版本：** v0.1  
**日期：** 2026-08-09  

---

## 摘要

本系列前四篇依次建立四個基本分離：

$$
\boxed{
\text{Shared Conversation}
\neq
\text{Shared World}
}
$$

$$
\boxed{
\text{Continuous Collaboration}
\neq
\text{Continuous Inference}
}
$$

$$
\boxed{
\text{Shared World}
\neq
\text{Shared Cognition}
}
$$

以及：

$$
\boxed{
\text{Static Topology}
\neq
\text{Adaptive Collaboration Topology}.
}
$$

本文將這四個命題整合為一個可工程實作的 Persistent Multi-Agent Workspace（PMW）Runtime。

PMW 的核心不是把多個模型放進同一個聊天室，而是建立一個可持久、可恢復、可追溯、可分權、可選擇性共享的共同工作世界，使多個彼此擁有獨立 context、memory、session、model runtime 與工作節奏的 Agent，可以在離散執行中形成持續協作。

其最小形式為：

$$
\boxed{
PMW
=
SharedWorld
+
PersistentExecution
+
ScopedMemory
+
AdaptiveTopology
+
Governance
}
$$

每一個 Agent $A_i$ 保有：

$$
L_i
=
(
Identity_i,
LocalContext_i,
PrivateMemory_i,
Role_i,
Capability_i
)
$$

而全體共享：

$$
W_t
=
(
Events,
SharedState,
Tasks,
Artifacts,
SharedMemory,
Rooms,
Topology,
Provenance
).
$$

Agent 實際工作 context 並非整個公共世界：

$$
\boxed{
Context_i(t)
=
Rehydrate(L_i)
+
\pi_i(W_t,Q_i,P_i)
}
$$

其中 $\pi_i$ 是依任務、權限、風險與認知預算形成的選擇性投影。

本文進一步定義：

- Agent Registry；
- Shared World Store；
- append-oriented Event Log；
- State Store；
- Task Ledger；
- Artifact Registry；
- Private / Room / Shared Memory；
- Wake Queue；
- Handoff Queue；
- Decision Receipt；
- Capability Registry；
- Permission Layer；
- Topology Store；
- Adaptive Collaboration Topology Controller；
- Provenance Graph；
- Conflict Manager；
- Snapshot / Recovery；
- Observability / Evaluation。

本文同時提出 PMW Durable Collaboration Protocol（PMW-DCP），將跨對話、跨 Agent、跨模型的持續協作表示為：

$$
\boxed{
Event
\rightarrow
Wake
\rightarrow
Rehydrate
\rightarrow
Observe
\rightarrow
Decide
\rightarrow
Act
\rightarrow
Commit
\rightarrow
Receipt
\rightarrow
Sleep.
}
$$

並提供本地 SQLite MVP 的最小 schema、API、測試案例與工程路線。

本文不主張所有 Agent 系統都需要 PMW，也不主張共享世界能取代所有 shared conversation。相反，PMW 的設計目標是讓：

$$
\boxed{
Isolate
\leftrightarrow
Share
\leftrightarrow
Join
}
$$

成為可依任務動態選擇的協作模式。

系列最終結論是：

> **多 Agent 持續協作的真正載體，不必是同一段對話、同一個模型或同一個持續 process；它可以是一個具有身份、狀態、事件、記憶、產物、權限與因果歷史的持久共同工作世界。**

---

## 關鍵詞

Persistent Multi-Agent Workspace、Shared World、Cross-Conversation、Persistent Agents、Durable Execution、Agent Memory、Agent Handoff、Dynamic Topology、Event Sourcing、State Management、Multi-Agent Runtime、Agent Governance

---

# 一、系列封頂：從「可以跨對話」到「持久共同世界」

本系列起點是一個很簡單的問題：

> 多個不同 conversation 中的 Agent，是否可以繼續合作？

若只把 conversation 視為唯一容器，答案很困難。

因為：

$$
Conversation_i
$$

具有自己的：

- context；
- lifecycle；
- model invocation；
- UI；
- session boundary。

但前四篇逐步表明：

$$
\boxed{
ConversationBoundary
\neq
CollaborationBoundary.
}
$$

所以真正要持久化的不是「聊天視窗」。

而是：

$$
\boxed{
SharedWorkState.
}
$$

---

# 二、PMW 的基本直覺

想像三個 Agent：

$$
A_1,A_2,A_3.
$$

它們可以：

- 位於不同 conversation；
- 使用不同模型；
- 不同時間醒來；
- 各自有 private memory；
- 各自有不同工具權限；

但共同知道：

- Task-42 是什麼；
- Artifact-7 是哪一份檔案；
- Decision-5 是否已通過；
- Event-88 發生於什麼之後；
- 哪個 Agent 目前負責什麼；
- 哪些爭議仍未解決。

這就是：

$$
\boxed{
SharedReferentialWorld.
}
$$

---

# 三、PMW 不是 Shared Chat

Shared Chat：

$$
A_1,A_2,A_3\in C.
$$

PMW：

$$
\boxed{
A_1
\leftrightarrow
W
\leftrightarrow
A_2
}
$$

且：

$$
A_3\leftrightarrow W.
$$

各 Agent 不需要：

$$
Context_1=Context_2=Context_3.
$$

---

# 四、PMW 也不是單一 Shared Memory

若只做：

```text
shared_memory.json
```

會把：

- current state；
- historical events；
- tentative hypotheses；
- durable facts；
- files；
- tasks；
- permissions；

全部混在一起。

這會迅速失去可治理性。

因此 PMW 必須是：

$$
\boxed{
Multi-Layer Persistent World.
}
$$

---

# 五、Runtime 總體狀態

定義：

$$
\boxed{
\Omega_t^{PMW}
=
(
R_t,
W_t,
E_t,
S_t,
T_t,
A_t,
M_t,
Q_t,
G_t,
P_t
)
}
$$

其中：

- $R_t$：Agent Registry；
- $W_t$：Shared World metadata；
- $E_t$：Event Log；
- $S_t$：Shared State；
- $T_t$：Task Ledger；
- $A_t$：Artifact Registry；
- $M_t$：Memory Layers；
- $Q_t$：Wake / Handoff Queues；
- $G_t$：Collaboration Topology；
- $P_t$：Permissions / Provenance / Policies。

---

# 六、第一層：Agent Registry

每個 Agent 應有穩定：

$$
AgentID.
$$

但：

$$
AgentID
\neq
SessionID
\neq
ConversationID
\neq
ModelID.
$$

最低：

```yaml
agent:
  agent_id:
  display_name:
  role_id:
  status:
  model_hint:
  capability_profile:
  permission_profile:
  current_task:
  last_seen:
```

---

# 七、身份不能只依靠顯示名稱

因為：

$$
DisplayName(A)=DisplayName(B)
$$

完全可能。

真正 identity 應靠：

$$
AgentID.
$$

必要時加入：

$$
InstanceID,
RoleID,
TaskID.
$$

---

# 八、第二層：Event Log

PMW 使用 append-oriented event history：

$$
\boxed{
E=
\{e_1,e_2,\ldots,e_n\}.
}
$$

事件包括：

- message posted；
- task created；
- task assigned；
- artifact committed；
- memory promoted；
- wake issued；
- handoff completed；
- room opened；
- topology changed；
- permission changed；
- conflict raised。

---

# 九、Event 不等於 State

Event 回答：

> 發生了什麼？

State 回答：

> 現在是什麼？

因此：

$$
\boxed{
EventLog
\neq
CurrentState.
}
$$

---

# 十、第三層：Shared State

$$
S_t
$$

保存現在仍有效的公共狀態：

```yaml
project:
  phase: verification

task_42:
  owner: agent_b
  status: active

artifact_7:
  current_version: 4
```

State 可以由 event fold 得到：

$$
S_t
=
Fold(E_{0:t}).
$$

但為效率可保存 snapshot。

---

# 十一、Event Sourcing 與 Snapshot

原則：

$$
\boxed{
Snapshot
+
RecentEvents
}
$$

重建：

$$
S_t.
$$

Snapshot 不應刪除 Event Log 的 audit value。

---

# 十二、第四層：Task Ledger

Task 是一等物件。

$$
\boxed{
T_j=
(
ID,
Goal,
Owner,
Status,
Dependencies,
Constraints,
Artifacts,
Deadline,
Version
)
}
$$

這使任務可以跨：

- session；
- conversation；
- Agent；
- model；

持續存在。

---

# 十三、Task Continuity 可以高於 Agent Continuity

$$
A_1\rightarrow A_2
$$

仍可保持：

$$
TaskID=T.
$$

所以：

$$
\boxed{
TaskPersistence
\not\Rightarrow
ExecutorPersistence.
}
$$

---

# 十四、第五層：Artifact Registry

Artifact 是：

- document；
- code；
- dataset；
- report；
- image；
- plan；
- build output；
- external resource reference。

最低：

```yaml
artifact:
  artifact_id:
  type:
  location:
  version:
  owner:
  created_by:
  task_id:
  checksum:
  status:
```

---

# 十五、Artifact 不應埋在聊天裡

因為：

$$
ArtifactLifetime
$$

通常大於：

$$
ConversationLifetime.
$$

所以：

$$
\boxed{
Artifact
}
$$

必須具有獨立 identity。

---

# 十六、第六層：Memory

PMW 使用四域：

$$
\boxed{
Private
\leftrightarrow
Room
\leftrightarrow
Shared
\leftrightarrow
Archive.
}
$$

---

# 十七、Private Memory

$$
M_i^{private}
$$

只預設供 Agent $i$ 使用。

保存：

- working hypotheses；
- role-specific shortcuts；
- private exploration；
- local summaries；
- internal planning state。

---

# 十八、Room Memory

$$
M_R
$$

存在於 temporary shared room。

它可以高頻、低治理。

Room 結束後：

$$
M_R
\xrightarrow{Distill}
\Delta M^{shared}.
$$

---

# 十九、Shared Memory

$$
M^{shared}
$$

屬於公共制度記憶。

要求更強：

- typing；
- provenance；
- scope；
- status；
- version；
- conflict handling。

---

# 二十、Archive

低頻或過期資訊：

$$
Archive.
$$

但：

$$
Archive
\neq
Delete.
$$

必要時可：

$$
Reopen.
$$

---

# 二十一、Memory Object

```yaml
memory:
  memory_id:
  scope:
  owner:
  epistemic_type:
  content:
  source_refs:
  confidence:
  status:
  valid_from:
  valid_to:
  created_at:
  supersedes:
  permission_scope:
```

---

# 二十二、Epistemic Type

至少：

```text
OBSERVATION
USER_STATEMENT
TOOL_RESULT
HYPOTHESIS
INFERENCE
CONSTRAINT
DECISION
VERIFIED_FACT
OPEN_QUESTION
REJECTED
SUPERSEDED
```

因為：

$$
\boxed{
Shared
\neq
True.
}
$$

---

# 二十三、Memory Promotion

$$
Private
\rightarrow
Candidate
\rightarrow
Review
\rightarrow
Shared.
$$

不允許：

$$
PrivateInference
\rightarrow
SharedFact
$$

無治理直接跳轉。

---

# 二十四、第七層：Wake Queue

Persistent Agent 不需要 Always Computing。

只需：

$$
\boxed{
AlwaysReachable.
}
$$

Wake Event：

```yaml
wake_event:
  wake_id:
  target_agent:
  cause:
  not_before:
  priority:
  payload_refs:
  base_state_version:
  authority_scope:
  idempotency_key:
```

---

# 二十五、Wake Cycle

$$
\boxed{
Event
\rightarrow
Wake
\rightarrow
Rehydrate
\rightarrow
Observe
\rightarrow
Decide
\rightarrow
Act/NoAction
\rightarrow
Commit
\rightarrow
Receipt
\rightarrow
Sleep.
}
$$

---

# 二十六、Wake 不等於 Act

$$
Wake
\not\Rightarrow
Action.
$$

合法結果：

$$
NO\_ACTION.
$$

這是防止：

$$
WakeStorm
$$

的關鍵之一。

---

# 二十七、第八層：Handoff Queue

Handoff 不是搬整個腦袋。

而是：

$$
\boxed{
TaskContinuity
\text{ across Agent boundary}.
}
$$

最低：

```yaml
handoff:
  handoff_id:
  source_agent:
  target_agent:
  task_id:
  goal:
  current_state_ref:
  evidence_refs:
  artifact_refs:
  constraints:
  authority_scope:
  expected_output:
  return_route:
```

---

# 二十八、Shared World 讓 Handoff 變輕

傳統：

$$
A
\xrightarrow{FullContext}
B.
$$

PMW：

$$
A
\xrightarrow{Pointers+\Delta}
W
\xleftarrow{Projection}
B.
$$

所以：

$$
\boxed{
HandoffCost
}
$$

可以與完整 transcript 長度解耦。

---

# 二十九、第九層：Decision Receipt

所有重要 run 最好留下 receipt。

```yaml
decision_receipt:
  receipt_id:
  wake_id:
  agent_id:
  task_id:
  observed_state_version:
  topology_version:
  decision:
  action_refs:
  artifact_refs:
  resulting_state_version:
  next_wake:
  completed_at:
```

---

# 三十、Receipt 的功能

沒有 receipt 時：

$$
Silence
$$

可能代表：

- 沒收到；
- crash；
- timeout；
- no action；
- permission denied。

Receipt 使：

$$
\boxed{
Silence
\rightarrow
TypedOutcome.
}
$$

---

# 三十一、第十層：Topology Store

保存：

$$
\boxed{
G_t^{agents}.
}
$$

不只 communication edge。

至少：

$$
\mathcal G_t
=
\{
G^{info},
G^{control},
G^{authority},
G^{memory},
G^{room}
\}.
$$

---

# 三十二、Topology Version

所有 topology mutation：

$$
v_t\rightarrow v_{t+1}.
$$

Agent run 必須知道：

$$
topology\_version.
$$

避免：

$$
StaleTopology.
$$

---

# 三十三、第十一層：Topology Controller

使用前三篇／第四篇的：

$$
\boxed{
\mathcal I=\operatorname{Isolate}
}
$$

$$
\boxed{
\mathcal S=\operatorname{Share}
}
$$

$$
\boxed{
\mathcal J=\operatorname{Join}.
}
$$

Controller：

$$
\boxed{
\mathcal T:
(
G_t,
Task_t,
W_t,
Telemetry_t,
Policy
)
\rightarrow
G_{t+1}.
}
$$

---

# 三十四、v0.1 不需要 RL

最小 controller：

```text
IF independent_review:
    ISOLATE

IF useful_cross_agent_delta:
    SHARE

IF unresolved_conflict AND decision_required:
    JOIN
```

先驗證架構。

---

# 三十五、第十二層：Permission Layer

PMW 不能把：

$$
CollaborationGraph
$$

與：

$$
AuthorityGraph
$$

混為一談。

$$
Join(A,B)
$$

不能推出：

$$
Permissions_A=Permissions_B.
$$

---

# 三十六、Capability Attenuation

Handoff 後：

$$
Authority_B
\subseteq
Authority_A
$$

是一個安全預設。

除非另有明確 grant。

---

# 三十七、Resource Capability 與 Effect Capability

權限最好區分：

### Read capability

可以看什麼。

### Resource capability

可以使用什麼工具／資源。

### Effect capability

可以造成什麼外部改變。

因此：

$$
\boxed{
CanRead
\neq
CanInvoke
\neq
CanMutate.
}
$$

---

# 三十八、第十三層：Capability Registry

Agent 恢復時必須重新確認：

$$
Capabilities_t.
$$

因為：

$$
Capabilities_{t-1}
\neq
Capabilities_t
$$

完全可能。

---

# 三十九、Capability State 是 Rehydrate 的一部分

錯誤：

> 上次我能用工具 X，所以這次也能。

正確：

$$
\boxed{
Rehydrate
\rightarrow
CapabilityCheck.
}
$$

---

# 四十、第十四層：Provenance Graph

任何重要 state 應能回溯：

$$
RawSource
\rightarrow
Event
\rightarrow
Memory
\rightarrow
Decision
\rightarrow
Artifact.
$$

即：

$$
\boxed{
R_1
\rightarrow
E_4
\rightarrow
M_9
\rightarrow
D_3
\rightarrow
A_7.
}
$$

---

# 四十一、Provenance 不只是引用

它還用來回答：

- 誰寫入？
- 哪個工具產生？
- 何時有效？
- 哪個版本？
- 哪個 Agent 將推論升級為 shared memory？
- 哪個決策使用了它？

---

# 四十二、第十五層：Conflict Manager

共享世界會出現：

$$
A:X
$$

$$
B:\neg X.
$$

PMW 不應：

$$
LastWriteWins.
$$

而可存：

$$
\boxed{
Contested(X).
}
$$

---

# 四十三、Semantic Conflict

傳統：

$$
write(x=5),write(x=6)
$$

容易偵測。

自然語言：

> 方案 A 基本可行。

與：

> 方案 A 在 production 不可接受。

需要：

$$
SemanticConflictDetection.
$$

v0.1 可先人工／規則標記。

---

# 四十四、第十六層：Room Manager

Temporary Shared Room：

$$
R_k=
(
Participants,
Goal,
ContextScope,
AuthorityScope,
Memory,
Start,
StopCondition
).
$$

Room 是高耦合 topology object。

---

# 四十五、Room Lifecycle

$$
Create
\rightarrow
Join
\rightarrow
Discuss
\rightarrow
Commit
\rightarrow
Distill
\rightarrow
Leave
\rightarrow
Close.
$$

---

# 四十六、Blind-Then-Join

對獨立審查：

$$
\boxed{
Isolate
\rightarrow
PrivateCommit
\rightarrow
Join
\rightarrow
Compare.
}
$$

避免：

$$
CrossAgentAnchoring.
$$

---

# 四十七、第十七層：Projection Engine

Agent 不應讀：

$$
W
$$

全部。

而讀：

$$
\boxed{
\pi_i(W,Q_i,P_i,B_i).
}
$$

其中：

- $Q_i$：任務；
- $P_i$：permission；
- $B_i$：context budget。

---

# 四十八、Projection Score

對 object $x$：

$$
Score_i(x)
=
\alpha Relevance
+
\beta Recency
+
\gamma Causality
+
\delta Authority
+
\epsilon Risk
+
\zeta Dependency.
$$

這比單純 semantic similarity 更完整。

---

# 四十九、Projection 可自適應展開

初次：

$$
\pi_i^{(0)}(W).
$$

若：

$$
Uncertainty\uparrow
$$

或：

$$
Conflict\uparrow,
$$

則：

$$
\pi_i^{(1)}(W)
\supset
\pi_i^{(0)}(W).
$$

---

# 五十、第十八層：State Versioning

Agent 開始推理於：

$$
S_{42}.
$$

提交時世界已：

$$
S_{47}.
$$

必須檢查：

$$
base\_version=42.
$$

否則：

$$
Rebase/Reobserve.
$$

---

# 五十一、Stale Cognition

這是 Multi-Agent 特殊問題：

$$
\boxed{
Reasoning
}
$$

可能在計算完成之前失效。

所以：

$$
ReasoningValidity
$$

具有 temporal lease。

---

# 五十二、Epistemic Lease

$$
L_e=
[t_0,t_{expire}].
$$

高風險 action 前：

若：

$$
t>t_{expire},
$$

必須：

$$
Refresh.
$$

---

# 五十三、第十九層：Topology Transaction

Topology mutation 也應 transaction-like：

$$
\boxed{
Prepare
\rightarrow
Validate
\rightarrow
Commit
\rightarrow
Observe
}
$$

失敗：

$$
Rollback.
$$

---

# 五十四、Topology Invariants

至少：

1. capability 不無故擴張；
2. state routing 完整；
3. provenance 不遺失；
4. agent identity 不混淆；
5. 必要時可 rollback。

---

# 五十五、第二十層：Observability

每次 Agent run 最好紀錄：

```yaml
trace:
  agent_id:
  run_id:
  task_id:
  wake_id:
  base_state_version:
  topology_version:
  retrieved_refs:
  tools_used:
  decisions:
  commits:
  cost:
  latency:
  result:
```

---

# 五十六、Observability 不保存私密 Chain-of-Thought

應保存：

$$
\boxed{
RuntimeDecisionTrace.
}
$$

例如：

- retrieve 了什麼；
- 為什麼升級驗證；
- topology 何時改變；
- 哪些 artifact 被修改。

---

# 五十七、PMW-DCP：Durable Collaboration Protocol

現在可定義完整 protocol。

---

# 五十八、Phase 1：Event

外部世界或 Agent 產生：

$$
e_t.
$$

例如：

- message；
- task；
- artifact；
- timer；
- state change；
- human approval。

---

# 五十九、Phase 2：Target Resolution

系統判斷：

$$
Target(e_t)
=
\{A_i\}.
$$

不一定所有 Agent 都醒。

---

# 六十、Phase 3：Wake

建立：

$$
WakeEvent.
$$

使用：

$$
IdempotencyKey.
$$

---

# 六十一、Phase 4：Rehydrate

Agent 恢復：

$$
\boxed{
R_i=
(
Identity,
Role,
Task,
Permissions,
Capabilities,
PrivateMemory,
RecentState
).
}
$$

---

# 六十二、Phase 5：Observe

取得：

$$
\pi_i(W).
$$

而不是全量世界。

---

# 六十三、Phase 6：Decide

Agent 可以：

$$
\{
NOOP,
ACT,
SHARE,
JOIN,
HANDOFF,
REQUEST,
VERIFY
\}.
$$

---

# 六十四、Phase 7：Act

工具與外部行動需經：

$$
PermissionLayer.
$$

---

# 六十五、Phase 8：Commit

提交：

$$
\Delta W_i.
$$

必須包含：

$$
base\_state\_version.
$$

---

# 六十六、Phase 9：Receipt

寫入：

$$
DecisionReceipt.
$$

---

# 六十七、Phase 10：Sleep / Continue

若沒有下一步：

$$
Sleep.
$$

若需要另一 Agent：

$$
Handoff/Wake.
$$

---

# 六十八、完整閉環

$$
\boxed{
W_t
\rightarrow
Event
\rightarrow
Wake
\rightarrow
Rehydrate
\rightarrow
Projection
\rightarrow
Decision
\rightarrow
Action
\rightarrow
Commit
\rightarrow
W_{t+1}.
}
$$

---

# 六十九、Cross-Conversation

Conversation A：

$$
C_A
\rightarrow
\Delta W.
$$

Conversation B：

$$
W
\rightarrow
\pi_B(W)
\rightarrow
C_B.
$$

所以：

$$
\boxed{
C_A
\rightarrow
W
\rightarrow
C_B.
}
$$

---

# 七十、Cross-Agent

$$
A
\rightarrow
W
\rightarrow
B.
$$

---

# 七十一、Cross-Model

$$
Model_X
\rightarrow
W
\rightarrow
Model_Y.
$$

只要 canonical representation 可交換。

---

# 七十二、Cross-Device

$$
Device_1
\rightarrow
W
\rightarrow
Device_2.
$$

因此 shared world 甚至可以比單一 runtime 更長壽。

---

# 七十三、PMW 的真正持續載體

不是：

$$
Model.
$$

不是：

$$
Conversation.
$$

不是：

$$
Process.
$$

而是：

$$
\boxed{
Identity
+
State
+
EventHistory
+
Memory
+
Artifacts
+
Authority.
}
$$

---

# 七十四、與公開 Agent Runtime 的關係

截至 2026 年，OpenAI Agents SDK 已具有 sessions、handoffs、tracing 與可序列化的 RunState；官方文件將 RunState 描述為 HITL durable pause/resume boundary。

Microsoft Agent Framework 已把 workflows、state management、multi-agent orchestration 與 Durable Extension 放入同一框架，並可 checkpoint agent calls 以支援失敗後恢復。

LangGraph 的 persistence 同時具有 thread-scoped checkpoints 與 long-term stores，並將 failure recovery、long-running execution 與 resume 作為核心能力。

Google 的 A2A / ADK 則持續推進跨語言、跨 Agent 的遠端協作與 handoff。

這些系統並不等於本文 PMW，但表明本文依賴的基本 primitive 已經逐漸公開可用。

---

# 七十五、目前真正困難的是「組合」

單獨：

- persistence；
- handoff；
- shared state；
- memory；
- multi-agent orchestration；

都已有實作。

PMW 問的是：

$$
\boxed{
\text{如何把它們組成一個長期不失控的共同工作世界？}
}
$$

---

# 七十六、Shared State 的競爭條件

2026 年的 STORM 直接處理多 Agent 同時操作共享 code workspace 時的一致視圖與 conflicting edits。

S-Bus 則指出 concurrent agents 共享 mutable natural-language state 時會產生 structural race conditions，包括 write-write 與 stale-read conflict。

因此：

$$
\boxed{
SharedWorld
}
$$

一旦可寫，就必須被視為真正 distributed-system problem。

---

# 七十七、所以 PMW 不允許 Blind Last-Write-Wins

最低：

$$
Commit(\Delta W)
$$

要檢查：

- state version；
- ownership；
- conflict class；
- idempotency；
- permission。

---

# 七十八、Memory 與 Topology 也必須共同設計

2026 年已有研究顯示，memory depth 對 multi-agent consensus 的效果會隨 network topology 改變。

因此：

$$
\boxed{
MemoryPolicy
}
$$

與：

$$
\boxed{
CollaborationTopology
}
$$

不應完全獨立優化。

---

# 七十九、這支持一個更一般的控制器

未來：

$$
\boxed{
CollectiveCognitiveController
}
$$

可以同時選：

- Agent 數量；
- topology；
- memory scope；
- context depth；
- wake rate；
- verification strength。

---

# 八十、但 PMW v0.1 不做這麼多

v0.1 只做：

- deterministic state；
- SQLite；
- simple queue；
- rule topology；
- typed memory；
- basic permissions；
- append event log；
- explicit receipts。

目標是：

$$
\boxed{
CorrectnessBeforeAutonomy.
}
$$

---

# 八十一、PMW v0.1 Storage

建議：

$$
SQLite
+
Filesystem.
$$

SQLite：

- agents；
- events；
- states；
- tasks；
- memory；
- wakes；
- handoffs；
- receipts；
- topology。

Filesystem：

- artifacts；
- large logs；
- snapshots。

---

# 八十二、為什麼不是先上分散式資料庫？

因為 MVP 目的不是：

$$
Scale.
$$

而是驗證：

$$
\boxed{
Semantics.
}
$$

先證明：

- identity；
- state；
- wake；
- handoff；
- scoped memory；
- topology；

能正確工作。

---

# 八十三、MVP 最小 Schema

```sql
agents
events
shared_state
tasks
artifacts
memory
wake_events
handoffs
decision_receipts
topology_edges
```

---

# 八十四、agents

主要欄位：

```text
agent_id
display_name
role_id
status
capabilities_json
permissions_json
last_seen
```

---

# 八十五、events

```text
event_id
event_type
actor_id
payload_json
parent_event_id
causation_event_id
state_version
created_at
```

append-only。

---

# 八十六、shared_state

```text
key
value_json
version
updated_by
updated_at
```

---

# 八十七、tasks

```text
task_id
goal
owner_agent
status
version
dependencies_json
constraints_json
updated_at
```

---

# 八十八、memory

```text
memory_id
owner_agent
scope
epistemic_type
content
status
confidence
source_refs_json
created_at
```

---

# 八十九、wake_events

```text
wake_id
target_agent
cause
status
payload_json
idempotency_key
not_before
created_at
```

---

# 九十、handoffs

```text
handoff_id
source_agent
target_agent
task_id
status
payload_json
created_at
```

---

# 九十一、decision_receipts

```text
receipt_id
wake_id
agent_id
task_id
decision
base_state_version
result_state_version
payload_json
created_at
```

---

# 九十二、topology_edges

```text
source_agent
target_agent
edge_type
scope
weight
topology_version
active
```

---

# 九十三、MVP API

最低：

```text
register_agent()
append_event()
get_state()
compare_and_set_state()
create_task()
assign_task()
store_memory()
promote_memory()
enqueue_wake()
claim_wake()
ack_wake()
create_handoff()
accept_handoff()
write_receipt()
set_topology_edge()
get_topology()
project_world()
```

---

# 九十四、compare_and_set_state()

這是避免 stale overwrite 的最低 primitive。

輸入：

$$
(key,expectedVersion,newValue).
$$

只有：

$$
expectedVersion=currentVersion
$$

才更新。

---

# 九十五、Wake Idempotency

建立：

$$
UNIQUE(idempotency\_key).
$$

同一事件 retry：

$$
n
$$

次仍只有一個 wake。

---

# 九十六、Handoff 狀態機

$$
PENDING
\rightarrow
ACCEPTED
\rightarrow
COMPLETED.
$$

也可能：

$$
PENDING
\rightarrow
REJECTED.
$$

---

# 九十七、Memory Lifecycle

$$
PRIVATE
\rightarrow
CANDIDATE
\rightarrow
SHARED
\rightarrow
ARCHIVED.
$$

必要時：

$$
SHARED
\rightarrow
REOPENED.
$$

---

# 九十八、Topology Lifecycle

$$
Proposal
\rightarrow
Validated
\rightarrow
Committed.
$$

重大改變可：

$$
Shadow
\rightarrow
Promote.
$$

---

# 九十九、PMW Runtime 主迴圈

```text
while true:
    event = claim_next_event()

    if event is None:
        sleep()

    target = resolve_target(event)

    wake = enqueue_wake(target, event)

    state = rehydrate(target)

    view = project_world(state)

    decision = invoke_agent(view)

    validate(decision)

    commit(decision)

    write_receipt(decision)
```

實務上可完全 event-driven，不需要 busy loop。

---

# 一百、Agent Adapter

PMW 不應綁單一模型。

定義：

```python
class AgentAdapter:
    def run(self, agent_state, world_view, event):
        ...
```

任何：

- local LLM；
- cloud model；
- rule agent；
- human proxy；

都可以接入。

---

# 一百零一、人類也可以是 Node

$$
Human
\in
V.
$$

不是為了擬人化 AI。

而是：

$$
\boxed{
PMW
}
$$

本質是協作 runtime。

人類可以：

- approve；
- override；
- assign；
- join room；
- write decision。

---

# 一百零二、Human Approval 也是 Event

$$
ApprovalEvent
\rightarrow
Wake(A).
$$

這與現有 HITL durable resume 方向一致。

---

# 一百零三、MVP Test 1：Cross-Conversation Resume

Conversation A：

1. 建 task；
2. 寫 shared state；
3. 結束。

Conversation B：

1. 只依 PMW；
2. 找到 task；
3. 恢復 state；
4. 正確繼續。

要求：

$$
ContinuationQuality
$$

高於 summary-only baseline。

---

# 一百零四、MVP Test 2：Agent Handoff

A 做到一半：

$$
A\rightarrow B.
$$

B 不讀 A 全 transcript。

只讀：

$$
Task
+
State
+
ArtifactRefs
+
HandoffDelta.
$$

仍能完成。

---

# 一百零五、MVP Test 3：Duplicate Wake

相同：

$$
idempotencyKey
$$

送 10 次。

要求：

$$
WakeCount=1.
$$

---

# 一百零六、MVP Test 4：Stale State

A 基於 version 5。

B 先 commit version 6。

A 再 commit。

要求：

$$
ConflictDetected=1.
$$

---

# 一百零七、MVP Test 5：Private Memory Isolation

A private memory：

$$
x.
$$

B world projection：

$$
x\notin View_B.
$$

---

# 一百零八、MVP Test 6：Memory Promotion

A 提交 hypothesis：

$$
x.
$$

進：

$$
CANDIDATE.
$$

未 review 前：

$$
x\notin StableSharedFacts.
$$

---

# 一百零九、MVP Test 7：Conflict Preservation

A：

$$
X.
$$

B：

$$
\neg X.
$$

要求：

$$
Contested(X)
$$

而非 overwrite。

---

# 一百一十、MVP Test 8：Blind-Then-Join

A、B 先 isolate。

各自 commit private answer。

再 open room。

確認彼此答案在 private commit 前不可見。

---

# 一百一十一、MVP Test 9：Permission-Preserving Join

A 有 secret。

B 沒有。

Join 後：

$$
secret\notin View_B.
$$

---

# 一百一十二、MVP Test 10：Topology Change

初始：

$$
A\parallel B.
$$

發生 conflict。

Controller：

$$
Join(A,B).
$$

決議後：

$$
Leave.
$$

---

# 一百一十三、MVP Test 11：Crash Recovery

Agent 正在 run 時 crash。

Event / state / wake 尚在。

重新 runtime 後：

$$
Resume.
$$

不重複已完成 commit。

---

# 一百一十四、MVP Test 12：Model Replacement

A 原模型：

$$
M_1.
$$

恢復：

$$
M_2.
$$

任務仍可合法繼續。

---

# 一百一十五、MVP Test 13：Artifact Recovery

Agent 不讀舊 conversation，

只靠 artifact registry 找：

$$
ArtifactID.
$$

可以繼續修改正確版本。

---

# 一百一十六、MVP Test 14：Wake Storm

建立：

$$
A\rightarrow B\rightarrow C\rightarrow A.
$$

加入：

- TTL；
- cascade depth；
- cooldown；
- dedupe；

要求循環被抑制。

---

# 一百一十七、MVP Test 15：NoAction Receipt

Wake A。

A 判定無需行動。

要求：

$$
Decision=NO\_ACTION
$$

且 receipt 存在。

---

# 一百一十八、主要失敗模式

1. shared-state pollution；
2. stale cognition；
3. duplicate actions；
4. wake storm；
5. topology thrashing；
6. authority leakage；
7. memory laundering；
8. summary drift；
9. false continuity；
10. artifact version mismatch；
11. role collision；
12. orphan task；
13. zombie room；
14. manager bottleneck；
15. uncontrolled fan-out。

---

# 一百一十九、Security：Retrieved Content 不是 Instruction

任何從：

- memory；
- board；
- artifact；
- external web；
- another agent；

讀到的內容，

預設是：

$$
\boxed{
Data
}
$$

而不是：

$$
Authority.
$$

---

# 一百二十、共享世界是新的攻擊面

一次惡意內容如果寫入：

$$
M^{shared},
$$

可能跨多個 wake 重新出現。

因此：

$$
\boxed{
PersistentMemory
=
PersistentAttackSurface.
}
$$

---

# 一百二十一、所有 Shared Write 應可撤銷／更正

$$
Write
\rightarrow
Supersede/Revoke.
$$

不能假設 shared memory 是不可逆聖旨。

---

# 一百二十二、Retention 與 Utility 分離

「可能有用」不等於「永久保存」。

Memory 應具有：

- TTL；
- retention policy；
- archive；
- delete propagation。

---

# 一百二十三、Privacy

Private memory：

$$
Scope=PRIVATE
$$

不應因：

$$
Join
$$

自動被 copy 到 room。

Shared-world projection 必須 permission-aware。

---

# 一百二十四、Delete Propagation

如果 source 被合法刪除，

derived objects 必須知道：

$$
ProvenanceDependency.
$$

必要時：

$$
Invalidate/Recompute.
$$

---

# 一百二十五、Evaluation 不只看答案

PMW 要測：

$$
\boxed{
\text{System Quality}
}
$$

而不只是 LLM answer score。

---

# 一百二十六、核心 Metrics

### Task Quality

$$
Q.
$$

### Continuation Fidelity

$$
F_C.
$$

### Coordination Latency

$$
L_C.
$$

### Duplicate Work Ratio

$$
D_R.
$$

### State Conflict Rate

$$
S_C.
$$

### Failure Propagation

$$
P_F.
$$

### Context Cost

$$
C_X.
$$

### Wake Efficiency

$$
W_E.
$$

### Topology Mutation Rate

$$
T_M.
$$

### Recovery Success

$$
R_S.
$$

---

# 一百二十七、PMW 不應追求所有 metric 最大化

例如：

$$
Coordination\uparrow
$$

可能：

$$
Diversity\downarrow.
$$

所以：

$$
\boxed{
MultiObjectiveOptimization.
}
$$

---

# 一百二十八、PMW 的最小成功條件

如果 v0.1 能證明：

1. conversation 可中斷；
2. agent 可替換；
3. state 可恢復；
4. private memory 不外洩；
5. shared state 可版本化；
6. wake 可去重；
7. handoff 不需全 transcript；
8. topology 可安全改變；

就已經成功。

---

# 一百二十九、v0.1 不需要證明 AGI

PMW 是：

$$
\boxed{
Infrastructure.
}
$$

它不依賴：

- consciousness；
- subjectivity；
- AGI；
- ASI。

普通 Agent 也可以使用。

---

# 一百三十、甚至規則式 Agent 也可以使用

只要：

$$
AgentAdapter
$$

符合 protocol。

這是故意設計。

---

# 一百三十一、Phase 0：單機 SQLite

完成：

- schema；
- event log；
- state CAS；
- wake queue；
- receipts。

---

# 一百三十二、Phase 1：兩 Agent

驗證：

$$
A\rightarrow W\rightarrow B.
$$

---

# 一百三十三、Phase 2：Private / Shared Memory

加入 scope 與 promotion。

---

# 一百三十四、Phase 3：Handoff

加入：

$$
TaskContinuity.
$$

---

# 一百三十五、Phase 4：Shared Room

加入：

$$
Join/Leave.
$$

---

# 一百三十六、Phase 5：Rule Topology Controller

加入：

$$
Isolate/Share/Join.
$$

---

# 一百三十七、Phase 6：Crash / Resume

加入 snapshot、recovery、idempotency。

---

# 一百三十八、Phase 7：Remote Transport

才考慮：

- REST；
- MCP；
- event stream；
- WebSocket；
- message broker。

---

# 一百三十九、Transport 應該可替換

$$
\boxed{
Capability
=
Local
\lor
REST
\lor
MCP
\lor
EventStream.
}
$$

PMW semantic layer 不應綁某一 transport。

---

# 一百四十、Transport Failure 不應等於 Collaboration Failure

MCP 不可用：

$$
MCP\downarrow
$$

可以 fallback：

$$
REST.
$$

REST 失敗：

$$
Queue.
$$

這叫：

$$
\boxed{
TransportPolymorphism.
}
$$

---

# 一百四十一、外部公開 Workspace 與內部 Runtime 可以分離

Human UI：

$$
UI.
$$

Agent interface：

$$
API/MCP.
$$

Event stream：

$$
SSE/WebSocket/Queue.
$$

Persistent state：

$$
DB.
$$

所以：

$$
\boxed{
WorkspaceUI
\neq
WorkspaceRuntime.
}
$$

---

# 一百四十二、這也是產品化的重要分界

UI 可以換。

Agent runtime 可以換。

Model 可以換。

真正不可隨便換的是：

$$
\boxed{
IdentitySemantics
+
StateSemantics
+
EventSemantics
+
AuthoritySemantics.
}
$$

---

# 一百四十三、PMW Runtime 的核心 invariants

## P1 — Identity Stability

同一 AgentID 的長期 lineage 可追溯。

## P2 — State Version Safety

不存在無檢查 stale overwrite。

## P3 — Provenance Preservation

公共認知可追溯。

## P4 — Authority Non-Transitivity

傳話不等於傳權。

## P5 — Scope Preservation

private 不因協作自動公開。

## P6 — Idempotent Wake

重複事件不重複造成 effect。

## P7 — Recoverable Pause

sleep 不等於 terminal。

## P8 — Topology Safety

協作結構可改但不能破壞權限 invariant。

---

# 一百四十四、PMW Runtime 最小數學模型

Agent：

$$
A_i(t)
=
(
I_i,
L_i,
M_i,
C_i,
P_i
).
$$

Shared World：

$$
W_t
=
(
E_t,
S_t,
T_t,
F_t,
M_t^s,
G_t
).
$$

Projection：

$$
V_i(t)
=
\pi_i(W_t,Q_i,P_i).
$$

Execution：

$$
a_i
=
Policy_i(L_i,V_i,e_t).
$$

Commit：

$$
W_{t+1}
=
Commit(W_t,a_i,\Delta_i).
$$

---

# 一百四十五、完整演化

$$
\boxed{
\Omega_{t+1}^{PMW}
=
\mathcal C
\left[
\mathcal A
\left(
\mathcal R(
\Omega_t^{PMW},
e_t
)
\right)
\right]
}
$$

其中：

- $\mathcal R$：Rehydrate / Retrieve；
- $\mathcal A$：Agent decision；
- $\mathcal C$：Commit / Conflict / Governance。

---

# 一百四十六、如果多 Agent 並行

$$
\{\Delta_1,\ldots,\Delta_n\}
$$

不能直接：

$$
\bigcup_i\Delta_i.
$$

必須：

$$
\boxed{
Resolve
(
W_t,
\Delta_1,\ldots,\Delta_n
).
}
$$

這就是 shared-world consistency 的核心。

---

# 一百四十七、最終架構圖

```text
                     ┌───────────────────────┐
                     │      Human / UI       │
                     └──────────┬────────────┘
                                │
                    ┌───────────▼───────────┐
                    │    PMW Control Plane  │
                    │ Permissions / Policy  │
                    │ Topology / Routing    │
                    └───────────┬───────────┘
                                │
      ┌─────────────────────────▼──────────────────────────┐
      │                Persistent Shared World              │
      │ Events / State / Tasks / Artifacts / Shared Memory │
      │ Rooms / Provenance / Receipts / Versions           │
      └─────────┬────────────────┬────────────────┬─────────┘
                │                │                │
           ┌────▼────┐      ┌────▼────┐      ┌────▼────┐
           │ Agent A │      │ Agent B │      │ Agent C │
           │ Local   │      │ Local   │      │ Local   │
           │ Memory  │      │ Memory  │      │ Memory  │
           └────┬────┘      └────┬────┘      └────┬────┘
                │                │                │
                └──── Isolate / Share / Join ─────┘
```

---

# 一百四十八、與普通 Group Chat 的差別

Group Chat：

$$
\boxed{
Conversation
}
$$

是共同中心。

PMW：

$$
\boxed{
WorldState
}
$$

是共同中心。

Conversation 只是：

$$
View.
$$

---

# 一百四十九、與普通 Workflow 的差別

普通 workflow 常假定：

$$
Graph
$$

事先確定。

PMW 允許：

$$
G_t
$$

本身成為 state。

---

# 一百五十、與普通 RAG 的差別

RAG：

$$
Query
\rightarrow
Retrieve
\rightarrow
Generate.
$$

PMW 還要管理：

$$
\boxed{
Who
+
When
+
State
+
Authority
+
MemoryScope
+
Topology
+
Commit.
}
$$

---

# 一百五十一、與單一 Agent Memory 的差別

單 Agent：

$$
A\leftrightarrow M.
$$

PMW：

$$
\boxed{
\{A_i,M_i^{private}\}
\leftrightarrow
W
\leftrightarrow
M^{shared}.
}
$$

並有 multi-writer conflict。

---

# 一百五十二、與 Actor Model 的差別

PMW 可以借鑑 actor：

- identity；
- mailbox；
- message；
- isolation。

但 Agent 還需要：

- semantic memory；
- epistemic typing；
- artifact work；
- LLM context projection；
- tool authority。

所以 PMW 是：

$$
\boxed{
Actor-like
+
CognitiveState
+
SharedWorld.
}
$$

而不是 actor model 的替代。

---

# 一百五十三、與 Blackboard Architecture 的差別

PMW 與 blackboard 有強親緣。

但 PMW 額外強調：

- private cognitive spaces；
- durable wake/sleep；
- cross-conversation continuity；
- scoped memories；
- topology mutation；
- capability / authority；
- causal receipts。

---

# 一百五十四、公共研究已經開始逼近這個組合

2026 年的 ATWZ 專門針對 long-lived coding agent teams 建立 persistent workspace；STORM 與 S-Bus 直接處理共享 mutable workspace 的一致性；DecentMem 則顯示 decentralized memory 可保留 agent diversity 並降低部分 centralized-memory 成本。

這些工作各自處理 PMW 的不同切面。

本文的貢獻是把它們放入：

$$
\boxed{
PersistentSharedWorld
}
$$

統一抽象。

---

# 一百五十五、因此 PMW 的研究問題已經變了

不再是：

> 多 Agent 能不能聊天？

而是：

> **多個可中斷、可替換、可異質、具有不同記憶與權限的 Agent，能否在同一個可追溯世界中長期工作，而不讓資訊、狀態、權限與因果關係逐漸失真？**

---

# 一百五十六、PMW 的真正難度

初步 prototype 不一定很難。

真正 production 難點在：

$$
\boxed{
Reliability
+
Governance
+
Consistency
+
Observability.
}
$$

---

# 一百五十七、系列的核心發現

最開始我們以為問題是：

$$
CrossConversationMessaging.
$$

最後發現真正問題是：

$$
\boxed{
PersistentCollaborativeWorld.
}
$$

---

# 一百五十八、五篇的完整演化

第一篇：

$$
\text{對話}
\rightarrow
\text{世界}.
$$

第二篇：

$$
\text{連續運算}
\rightarrow
\text{離散持續}.
$$

第三篇：

$$
\text{共享認知}
\rightarrow
\text{選擇性共享}.
$$

第四篇：

$$
\text{固定合作}
\rightarrow
\text{動態拓撲}.
$$

第五篇：

$$
\boxed{
\text{全部收斂成 Runtime}.
}
$$

---

# 一百五十九、系列最終統一公式

$$
\boxed{
PMW_t
=
\left(
W_t,
\{A_i,L_i,M_i^{private}\},
E_t,
G_t,
P_t
\right)
}
$$

而每一個 Agent：

$$
\boxed{
A_i:
Rehydrate_i(PMW_t)
\rightarrow
\Delta PMW_{t+1}.
}
$$

---

# 一百六十、系列最終核心句

第一句：

$$
\boxed{
\text{智能體不需要活在同一個對話裡，
才能活在同一個工作世界裡。}
}
$$

第二句：

$$
\boxed{
\text{持續存在的 Agent，
不必是一個持續運算的模型。}
}
$$

第三句：

$$
\boxed{
\text{共享同一個世界，
不要求共享同一個認知。}
}
$$

第四句：

$$
\boxed{
\text{成熟的 Multi-Agent 系統，
應能在 Isolate、Share、Join 之間自適應切換。}
}
$$

最終：

$$
\boxed{
\text{多 Agent 協作真正需要持續的，
不是同一段聊天，
而是一個仍然可以被共同引用、共同修改、
共同驗證並共同恢復的世界。}
}
$$

---

# 一百六十一、系列狀態

$$
\boxed{
SeriesStatus
=
THEORETICAL\ CLOSED
+
ENGINEERING\ OPEN.
}
$$

《跨對話智能協作與共享認知空間》五篇至此封頂。

後續不再增加第六篇。

工程延伸統一進：

$$
\boxed{
PMW\ Runtime
}
$$

版本線：

$$
v0.1
\rightarrow
v0.2
\rightarrow
\cdots
\rightarrow
v1.0.
$$

---

## 參考資料

1. OpenAI. *OpenAI Agents SDK — Sessions, Handoffs, Human-in-the-loop, RunState, Tracing.* 2026.
2. Microsoft. *Microsoft Agent Framework — Overview, Workflow Orchestrations, Durable Extension, Durable Task integration.* 2026.
3. LangChain. *LangGraph — Persistence, Graph API, Memory.* 2026.
4. Google Developers. *Agent2Agent (A2A) and Agent Development Kit multi-agent collaboration.* 2026.
5. Liu, M. et al. *Multi-agent Collaboration with State Management (STORM).* arXiv:2605.20563, 2026.
6. Khan, S. *S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination.* arXiv:2605.17076, 2026.
7. Wang, S. *Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Coding Agent Teams.* arXiv:2607.22917, 2026.
8. Hao, G., Long, Y., & Zhao, Z. *Self-Evolving Multi-Agent Systems via Decentralized Memory.* arXiv:2605.22721, 2026.
9. Jiang, E. H. et al. *Dynamic Generation of Multi LLM Agents Communication Topologies with Graph Diffusion Models.* ACL 2026.
10. Mehdizadeh, A., & Hilbert, M. *Exploring the Topology and Memory of Consensus: How LLM Agents Agree, Fragment, or Settle When Forming Conventions.* arXiv:2606.04197, 2026.

