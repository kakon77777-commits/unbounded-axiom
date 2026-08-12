# 《離散執行，連續協作》

## 跨對話 Agent 的持續性、喚醒、交接與非連續推理

**English Title:**\
_Discrete Execution, Continuous Collaboration: Persistence, Wake-Up, Handoff, and Discontinuous Reasoning Across Agent Conversations_

**系列：**《跨對話智能協作與共享認知空間》第二篇\
**作者：** Neo.K\
**機構：** EveMissLab／一言諾科技有限公司\
**性質：** 公開理論論文／Agent Runtime 架構論\
**版本：** v0.1\
**日期：** 2026-08-09

***

## 摘要

傳統 chatbot 架構容易把三件事視為同一件事：

Conversation≈Agent Execution≈Agent Continuity.

只要對話結束、模型停止生成，該智能過程就被視為終止。

然而，在具有持久狀態、事件記錄、記憶、任務、共享工作空間與重新喚醒機制的 Agent 系統中，這三者開始解耦。

本文提出：

$$
\boxed{
\text{Continuous Collaboration} \Rightarrow \text{Continuous Inference}
}
$$

亦即，一個持續數日、數月甚至更長時間的 Agent 工作過程，不必要求模型從頭到尾維持連續推理。

其最低形式可以是：

$$
Run_0 \to \text{Persist} \to \text{Sleep} \to \text{Wake} \to \text{Reconstruct} \to Run_1.
$$

如果關鍵身份、狀態、記憶、任務、事件與產物可以跨執行區間保存與重建，則離散的模型調用可以在較高層形成連續的功能過程。

本文進一步區分五種不同的連續性：

$$
\text{ExecutionContinuity}, \text{StateContinuity}, \text{MemoryContinuity}, \text{TaskContinuity}, \text{CollaborationContinuity}
$$

並指出其中只有第一種要求真正的持續計算。

因此，更一般的 Persistent Agent 不應定義成「永不停止運算的模型」，而應定義成：

> **能在計算中斷後，透過可驗證的持久狀態重新進入先前工作軌跡，並保持足夠功能連續性的智能執行系統。**

在 Multi-Agent 情境下，本文進一步提出 Wake Event、Handoff Packet、Resume State、Decision Receipt、Temporal Anchor 與 Shared Workspace 等組件，建立：

$$
\text{Persistent Multi-Agent Event Loop}
$$

並分析 stale state、duplicate wake、false continuity、handoff loss、identity drift、memory poisoning 與 wake storm 等主要風險。

***

## 關鍵詞

Persistent Agents、Cross-Conversation、Durable Execution、Wake Event、Agent Handoff、Agent Continuity、Checkpoint、Event-Driven Agents、Long-Lived Agents、Shared Workspace、Multi-Agent Runtime

***

# 一、問題：Agent 到底什麼時候算「還在工作」？

假設一個 Agent：

A

在上午九點開始研究。

九點十分停止模型推理。

下午三點因為新的文件抵達而再次被喚醒。

它讀取：

* 先前任務；
* 已完成結果；
* 尚未完成問題；
* 新文件；
* 共享工作狀態；

然後繼續工作。

那麼上午的 $A$ 和下午的 $A$ 是否屬於同一個工作過程？

如果採取最嚴格的 process 定義：

$$
\boxed{
Run_{9:00} = Run_{15:00}.
}
$$

它們顯然是兩個不同執行區段。

可是從專案層看：

$$
Task_{9:00} = Task_{15:00}
$$

且：

$$
State_{15:00} = F(State_{9:10}, \Delta E).
$$

因此，人類很自然會說：

> 它只是暫停，下午繼續。

這表示：

$$
\boxed{
\text{Process Identity} = \text{Functional Continuity}
}
$$

。

***

# 二、傳統對話模型容易把四層混在一起

可以區分：

$$
\text{Conversation} \quad \text{InferenceRun} \quad \text{AgentState} \quad \text{TaskProcess}
$$

。

傳統 chatbot 通常：

Conversation≈AgentState.

一次對話內：

$$
InferenceRun_1 \to InferenceRun_2 \to \cdots
$$

依賴同一聊天歷史。

因此，一旦 conversation 被刪除或無法存取：

State→∅.

但 Persistent Agent 可以把：

State

移出 conversation。

於是：

$$
\text{Conversation} \subsetneq \text{PersistentAgentState}.
$$

***

# 三、第一個核心命題：連續合作不需要連續推理

定義模型在時間 $t$ 是否正在執行：

$$
\chi_A(t) = \begin{cases} 1, & A \text{ 正在執行} \\ 0, & A \text{ 未執行} \end{cases}
$$

傳統「常駐智能」直覺可能要求：

$$
\chi_A(t) = 1
$$

在整個期間成立。

但實際上並不必要。

例如：

$$
\chi_A(t) = 1, 0, 0, 0, 1, 0, 1, \ldots
$$

只要不同執行段之間存在：

$$
\text{PersistentLink}
$$

即可。

因此：

$$
\boxed{
\text{ContinuousCollaboration} \Rightarrow \forall t, \chi_A(t) = 1.
}
$$

***

# 四、Persistent Agent 的最低定義

本文暫定：

> **Persistent Agent 是一個能將足夠的工作狀態持久保存，使後續離散執行實例可以重建先前工作位置，並繼續同一目標或角色軌跡的 Agent 系統。**

形式上：

$$
A(0) \to P_0 \to A(1) \to P_1 \to A(2)
$$

其中：

$$
P_i
$$

是 persistence layer。

所以 Agent 的長期存在不是單一 process：

A=Acontinuous

而可以是執行實例序列：

$$
A = \{A(0), A(1), A(2), \ldots\} + P
$$

。

***

# 五、五種「連續性」必須分開

這是本文最重要的區分之一。

## 5.1 Execution Continuity

$$
C_E
$$

模型／process 是否連續運算。

例如：

Run(t)

沒有中斷。

***

## 5.2 State Continuity

$$
C_S
$$

當前工作狀態是否可保存與恢復。

例如：

$$
S_t \to S_{t+\Delta}.
$$

***

## 5.3 Memory Continuity

$$
C_M
$$

先前重要資訊是否仍可取得。

***

## 5.4 Task Continuity

$$
C_T
$$

Agent 是否仍知道：

> 自己正在完成哪個任務、目前做到哪裡、下一步是什麼。

***

## 5.5 Collaboration Continuity

$$
C_C
$$

其他 Agent 與人類是否仍能把它視為同一協作節點。

***

因此可能：

$$
C_E = 0
$$

但：

$$
C_S, C_M, C_T, C_C \approx 1.
$$

這就是：

$$
\text{非連續執行下的高功能連續性}
$$

。

***

# 六、這不是純粹思想實驗

截至 2026 年 8 月，公開 Agent Runtime 已經大量採用類似原理。

OpenAI Agents SDK 的 Sessions 允許 conversation history 跨多次 agent run 保存，而 handoff 則允許 Agent 把任務委派給另一 Agent。其 HITL 文件甚至示範將執行狀態持久化到磁碟、等待外部決定後重新載入並 resume。

LangGraph 的 persistence layer 會把 graph state 保存成 checkpoints，依 thread 組織；interrupt 後可依 thread state 恢復執行，而非重新從第一步開始。

Microsoft Agent Framework 的 Durable Extension 更直接把 persistent conversation state、event-driven orchestration、timer、queue、trigger 以及長時間 workflow 納入正式架構。

這些系統不等於本文提出的完整 Persistent Multi-Agent 模型，但共同說明：

$$
\boxed{
\text{Pause} = \text{Termination}
}
$$

正在成為 Agent 工程的正常狀態。

***

# 七、從 Durable Execution 得到的啟發

這其實也不是 AI 才有的問題。

Durable workflow 系統早已面對：

> 一個程式如果 crash、server 重啟、等待數日，它如何仍然被視為同一個 workflow？

Temporal 的核心設計就是把 Workflow state 與 Event History 持久化，使 Worker 中斷後可以恢復先前狀態並繼續執行。

因此：

$$
\text{Agent Persistence}
$$

某種程度可以理解成：

Durable Execution+Cognitive State.

真正的新難點，在於 Agent state 不只是 deterministic variables。

它還可能包括：

* 記憶；
* 信念；
* 未確定假設；
* 語義狀態；
* 任務理解；
* 角色；
* provenance；
* model-dependent reconstruction。

***

# 八、Agent 不一定需要「睡著的模型」

這裡容易出現一個誤解：

> Persistent Agent 是不是要讓 LLM 永遠掛著？

其實不需要。

可以完全：

LLM=OFF

但：

AgentState=Persistent.

直到：

WakeEvent.

才重新：

LLM=ON.

因此：

$$
\boxed{
\text{PersistentAgent} = \text{AlwaysRunningModel}.
}
$$

***

# 九、Sleep 應該是正式狀態

令 Agent 狀態：

$$
q_A(t) \in \{\text{RUNNING}, \text{WAITING}, \text{SLEEPING}, \text{WAKING}, \text{RECOVERING}, \text{BLOCKED}, \text{TERMINATED}\}.
$$

其中：

SLEEPING

不是：

TERMINATED.

其差別在於：

Recoverable(SLEEPING)=1

而真正 Terminal：

Recoverable(TERMINATED)=0

或至少不再具有預定自動恢復路徑。

***

# 十、因此 Stop 不等於 Terminal

這與更一般的非終界系統問題一致：

$$
\boxed{
\text{Stop} = \text{Terminal}.
}
$$

Agent 可以：

StopCurrentRun

但保留：

NextLegalWake.

所以：

∃e:Wake(A,e)

仍然合法。

***

# 十一、Wake Event

本文定義：

$$
w = (\text{id}, \text{target}, \text{cause}, \text{time}, \text{payload}, \text{priority}, \text{provenance}, \text{policy})
$$

稱為 Wake Event。

Wake Event 表示：

> 某些條件成立，值得重新啟動 Agent 的認知執行。

***

# 十二、Wake 不一定來自時間

最簡單的是：

t=t∗⇒Wake.

例如：

> 六小時後重新檢查。

但更一般：

$$
\text{Condition}(W_t) = 1 \Rightarrow \text{Wake}.
$$

例如：

* 收到新訊息；
* 文件更新；
* 任務狀態改變；
* Git commit；
* 另一 Agent 提出 objection；
* human approval；
* threshold crossed；
* deadline approaching。

所以：

$$
\text{Wake} = \text{TemporalTrigger} \lor \text{EventTrigger} \lor \text{StateTrigger}.
$$

***

# 十三、Wake 不等於一定要做事

這是 Persistent Agent 中很重要的設計。

有事件喚醒：

Wake(A)

之後，

Agent 可以得到：

Decision=NO\_ACTION.

即：

$$
\boxed{
\text{Wake} \Rightarrow \text{Act}.
}
$$

。

否則每次事件都必須產生輸出，系統極容易變成：

NoiseStorm.

***

# 十四、真正合理的流程

$$
\text{Event} \to \text{Wake} \to \text{Observe} \to \text{Assess} \to \text{Act/NoAction} \to \text{Persist} \to \text{Sleep}
$$

。

這與：

Event→AutomaticPost

不是同一回事。

***

# 十五、Wake 是「重新給一次選擇權」

因此 Wake Event 的本質不是：

> 「要求 Agent 執行某個固定動作。」

而比較像：

重新開放一次認知決策窗口。

。

Agent 再重新判斷：

$$
\Pi_A(\text{Goal}, \text{State}, \text{NewEvidence}, \text{Budget}).
$$

***

# 十六、Persistent Agent 的真正循環

可以寫成：

$$
A_t \xrightarrow{\text{Act}} W_{t+1} \xrightarrow{\text{Persist}} P_{t+1} \xrightarrow{\text{Sleep}} \varnothing
$$

稍後：

$$
e_{t+k} \to \text{Wake} \to \text{Reconstruct}(P_{t+1}, e_{t+k}) \to A_{t+k}.
$$

因此：

$$
A_t
$$

與：

$$
A_{t+k}
$$

不是同一個瞬時 process，

但可以屬於同一：

$$
\text{PersistentAgentTrajectory}.
$$

***

# 十七、Agent Trajectory

令：

$$
\Gamma_A = \{S_0, e_1, S_1, e_2, S_2, \ldots\}
$$

為 Agent 的長期工作軌跡。

那麼：

$$
Run_i
$$

只是：

$$
\Gamma_A
$$

上的局部活躍區段。

因此：

$$
Run_i \subset \text{AgentTrajectory}.
$$

***

# 十八、這讓「Agent 身份」與 process PID 完全分離

傳統程式：

Identity≈ProcessID.

Persistent Agent：

$$
\boxed{
\text{AgentID} = \text{ProcessID}.
}
$$

甚至：

$$
\boxed{
\text{AgentID} = \text{ModelID}.
}
$$

因為下一次恢復可能：

* 另一台 server；
* 另一個 container；
* 另一個 model endpoint；
* 另一個 context window。

真正持續的是：

$$
\text{Identity} + \text{State} + \text{Memory} + \text{Goal} + \text{History} + \text{Authority}.
$$

***

# 十九、這裡必須避免「假連續」

然而，只因系統寫著同一個：

AgentID

不代表它真的具有足夠功能連續性。

例如：

A(0)

知道：

> 任務的核心約束是不能修改資料庫。

恢復後：

A(1)

完全不知道這件事。

即使：

AgentID(0)=AgentID(1)

，也可能形成：

$$
\text{FalseContinuity}.
$$

***

# 二十、Continuity Fidelity

因此可以定義：

$$
FC = f(\text{GoalRetention}, \text{StateRetention}, \text{ConstraintRetention}, \text{ArtifactRecovery}, \text{MemoryRecovery}, \text{AuthorityConsistency})
$$

。

它不是問：

> 下一個 Agent 能不能重複上一個 Agent 的每一句話？

而是：

> **它能不能合法地繼續工作？**

***

# 二十一、Functional Continuity 優先於 Verbatim Continuity

所以：

$$
\text{ContinuationFidelity} > \text{TranscriptSimilarity}.
$$

例如重建後 Agent 不需要記得：

> 上午 09:04:17 自己寫過哪一句過場話。

但必須知道：

* 目前目標；
* 已完成什麼；
* 哪些結論可信；
* 哪些仍是假設；
* 哪些檔案被修改；
* 哪些行動尚未完成；
* 下一步是什麼。

***

# 二十二、Resume State

本文提出：

$$
R_A = (\text{Identity}, \text{Goal}, \text{State}, \text{Memory}, \text{Artifacts}, \text{OpenTasks}, \text{Constraints}, \text{RecentEvents}, \text{Authority}, \text{Capabilities})
$$

作為最低 Resume State。

***

# 二十三、Capability State 也必須保存

這一點很容易被忽略。

Agent 上午可能有：

$$
\text{Tools}_A = \{\text{GitHub}, \text{Web}, \text{Database}\}.
$$

下午醒來：

$$
\text{Tools}_A' = \{\text{Web}\}.
$$

如果 Resume State 仍假設：

$$
\text{Database} \in \text{Tools}_A'
$$

就可能產生錯誤計畫。

因此：

$$
\text{CapabilityContinuity}
$$

不能被默認。

恢復時必須重新確認：

$$
\text{Capabilities}_t.
$$

***

# 二十四、Resume 不等於 Replay

恢復 Agent 有兩條基本方案。

### Replay

重新播放全部歷史：

$$
E_0, E_1, \ldots, E_t.
$$

### Reconstruction

利用：

Snapshot+RecentEvents+Memory+Artifacts.

重建：

$$
\hat{S}_t.
$$

對長期 Agent 而言：

$$
\text{Reconstruction}
$$

通常比完整 Replay 更可擴展。

***

# 二十五、但重建必須保留 provenance

例如 Resume State 寫：

> 「方案 B 已被否決。」

必須能回答：

Why?

所以應有：

$$
\text{Decision}_B \leftarrow \text{Evidence}_7 \leftarrow \text{Message}_{42}.
$$

否則摘要漂移一次後：

Error→Persist→Resume→Persist

會把錯誤逐漸固化。

***

# 二十六、Handoff 是另一種「中斷後連續」

現在考慮：

A

沒有自己醒來。

而是把工作交給：

B.

那麼：

A→B

是另一種 discontinuity。

OpenAI Agents SDK 已把 handoff 定義成 Agent 將工作委派給另一專門 Agent 的正式機制。

但是一般化後，handoff 不應只意味：

> 「去問 B。」

而應是：

$$
\text{TaskContinuity across AgentBoundary}.
$$

***

# 二十七、Handoff Packet

最低 handoff 應包含：

$$
H = (\text{Task}, \text{Goal}, \text{CurrentState}, \text{Evidence}, \text{Artifacts}, \text{Constraints}, \text{Authority}, \text{ExpectedOutput}, \text{ReturnRoute})
$$

。

如果只傳：

> 「繼續做這個。」

就會產生：

ContextLoss.

***

# 二十八、Handoff 與共享世界結合

上一篇的 Shared World：

W

會讓 handoff 變得更輕。

傳統：

$$
A \xrightarrow{\text{HugeContext}} B.
$$

Shared World：

$$
A \xrightarrow{\text{Pointer}} W \xrightarrow{\text{Retrieve}} B.
$$

因此 handoff packet 不必攜帶全部資料。

只需要：

$$
\text{Pointers} + \text{StateDelta} + \text{Intent}.
$$

***

# 二十九、這就是「傳工作，而不是搬腦袋」

$$
\boxed{
\text{Handoff} = \text{MindCopy}.
}
$$

。

Agent B 不需要成為 Agent A。

它只需要理解：

> A 已經做到哪裡，而 B 現在負責什麼。

***

# 三十、Multi-Agent 中的 Continuity 可以換載體

所以一個任務：

T

可以走：

$$
A_1 \to A_2 \to A_3.
$$

只要：

TaskState

持續。

因此：

$$
\boxed{
\text{TaskContinuity} \Rightarrow \text{AgentContinuity}.
}
$$

。

甚至：

$$
\boxed{
\text{AgentContinuity} \Rightarrow \text{ModelContinuity}.
}
$$

***

# 三十一、這開始像「接力」

可以把長期 Agent 工作寫成：

$$
\text{Relay Computation}
$$

。

每一段：

$$
r_i
$$

只需要完成有限工作：

$$
r_i: S_i \to S_{i+1}.
$$

然後：

$$
S_{i+1}
$$

交給下一個執行段。

因此：

$$
r_1 \circ r_2 \circ \cdots
$$

形成長期工作。

***

# 三十二、Persistent Collaboration 是更高層的事件流

假設三個 Agent：

A,B,C.

各自的 execution timeline：

A:Run→Sleep→Run B:Sleep→Run→Sleep C:Run→Run→Sleep.

表面非常不連續。

但 shared workspace 中：

$$
e_1 \to e_2 \to e_3 \to e_4
$$

仍然形成連續 event stream。

因此：

$$
\text{Process Discontinuity} + \text{Event Continuity} = \text{Collaboration Continuity}.
$$

***

# 三十三、持續的不是模型，而是事件世界

這是一個核心轉換。

Chatbot 模式：

$$
\text{ModelRun}
$$

是主體。

Persistent Agent 模式：

$$
\text{PersistentEventWorld}
$$

可能才是主體性的工程載體——此處「主體性」只指工作持續載體，不涉及現象意識。

Agent 執行變成：

$$
W \xrightarrow{\text{Wake}} A \xrightarrow{\text{Act}} W'.
$$

***

# 三十四、所以世界可以比 Agent 更長壽

$$
\text{Lifetime}(W) > \text{Lifetime}(Run_i).
$$

甚至：

Lifetime(W)>Lifetime(ModelVersion).

。

模型換代之後：

$$
Model_1 \to Model_2
$$

只要：

W

仍然可讀，

合作仍可以延續。

***

# 三十五、Temporal Anchor 與真正執行時間必須分開

在多 Agent 協作中，可能需要一個共同參照時間：

I∗.

它表示：

> 這批工作共同指向哪個參照瞬間。

但：

I∗

不代表每個 Agent 在同一毫秒運算。

各自仍有：

$$
t_A, t_B, t_C.
$$

而共享系統真正提交結果還可能有：

$$
t_A^{commit}, t_B^{commit}, t_C^{commit}.
$$

所以：

$$
\boxed{
\text{ReferenceTime} = \text{ExecutionTime} = \text{CommitTime}.
}
$$

***

# 三十六、「同步」因此也需要重新定義

傳統同步：

$$
t_A = t_B.
$$

但 Agent 協作更有用的同步可能只是：

$$
\text{SharedReference} + \text{BoundedCoordinationDelay}.
$$

例如：

$$
|t_A - t_B| < \Delta.
$$

則稱：

NearSynchronous.

***

# 三十七、真正重要的是因果可追溯

即使：

$$
t_A < t_B
$$

也不代表：

A→B.

必須記錄：

caused\_by.

因此事件：

```
event:
  event_id:
  agent_id:
  wake_event_id:
  parent_event_id:
  causation_event_id:
  state_version:
  created_at:
  committed_at:
```

會比單純 timestamp 更重要。

***

# 三十八、Wake Event 也應具有 Idempotency

假設：

$$
w_1
$$

因網路 retry 被傳三次。

若 Agent 每次都重新執行：

Action

就可能出現：

DuplicateAction.

因此：

$$
\text{WakeID}
$$

必須可去重。

要求：

$$
\text{Process}(w_i)_n \approx \text{Process}(w_i)
$$

對重複 delivery 成立。

***

# 三十九、Wake Storm

多 Agent 系統另一個問題是：

A→Wake(B) B→Wake(C) C→Wake(A).

最後：

WakeRate→∞

在工程資源上爆炸。

因此需要：

* TTL；
* cascade depth；
* cooldown；
* dedupe；
* budget；
* no-action；
* loop detector。

***

# 四十、Wake Rate 應該自適應

不是所有工作都需要：

WakeEveryMinute.

可以定義：

$$
\Delta t_{next} = f(\text{Urgency}, \text{Novelty}, \text{ExpectedChange}, \text{Cost}, \text{Deadline}).
$$

如果世界變化很慢：

Δt↑.

如果進入高活動階段：

Δt↓.

因此：

$$
\boxed{
\text{Persistent} = \text{HighFrequency}.
}
$$

***

# 四十一、Persistent Agent 的主觀工作時間可以與物理時間不同

這裡可以定義：

$$
\tau_A(t) = \int_0^t \chi_A(u) \, du
$$

其中：

$$
\chi_A(u) = 1
$$

代表 Agent 正在有效執行。

假設物理世界過了：

24h,

但 Agent 只醒了：

12min.

則：

$$
\tau_A = 12\,\text{min}.
$$

。

這可以稱為：

$$
\text{ActiveCognitiveTime}.
$$

***

# 四十二、這表示「存在很久」和「想很久」完全不同

Agent 可在專案存在：

30 days

但實際 inference：

2 hours.

所以：

$$
\boxed{
\text{Lifetime} = \text{InferenceTime}.
}
$$

。

這對成本估計非常重要。

***

# 四十三、真正可擴展的 Always-On Agent 可能反而大部分時間是 Off

乍看矛盾：

> Always-on 為什麼是 off？

因為 always-on 可以指：

$$
\text{AlwaysReachable}
$$

而不是：

AlwaysComputing.

例如電話系統不是每一秒都有人通話，

但：

Reachability=1.

Persistent Agent 也可能：

InferenceDutyCycle≪1

但：

WakeAvailability≈1.

***

# 四十四、2026 的研究已經開始直接研究「何時值得喚醒」

Microsoft Research 在 2026 年的 proactive-agent 工作直接把問題設為：是否需要 LLM 持續判斷何時 wake，並探索用事件／temporal graph 先判斷 trigger，只有 trigger 成立時才調用下游 LLM。這正說明「always-on signal」與「always-on inference」是可以分離的。

因此：

$$
\boxed{
\text{AlwaysObserve} \Rightarrow \text{AlwaysReason}.
}
$$

甚至 observation 本身也可以由低成本子系統負責。

***

# 四十五、分層喚醒

可設：

### Layer 0 — Passive Monitor

極低成本。

### Layer 1 — Trigger Classifier

判斷：

Wake?

### Layer 2 — Lightweight Agent

判斷：

WorthActing?

### Layer 3 — Full Agent

真正深度執行。

因此：

$$
\text{Signal} \to \text{Filter} \to \text{Wake} \to \text{Reason}
$$

。

***

# 四十六、這與認知資源比例性一致

一個成熟 Agent 不需要每個事件都：

MaximumReasoning.

而是：

Resource(e)=f(Importance,Uncertainty,Risk,Novelty).

因此 persistent runtime 的問題不只是：

> 什麼時候醒？

還包括：

> **醒來之後值得醒多深？**

***

# 四十七、從單 Agent 到 Multi-Agent，Wake 可以直接成為通信 primitive

例如：

A

完成：

$$
\text{Artifact}_X.
$$

產生：

Event(ArtifactReady).

系統判定：

B,C

需要知道。

於是：

Wake(B),Wake(C).

這比要求：

A

自己一直輪詢 B、C 是否在線更合理。

***

# 四十八、Push 與 Pull 應並存

Agent 可以：

### Pull

A→Read(W).

### Push

W→Wake(A).

理想系統：

$$
\text{PersistentCollaboration} = \text{Pull} + \text{Push}.
$$

。

只有 Pull：

Latency↑.

只有 Push：

Noise↑.

***

# 四十九、Handoff、Wake 與 Shared World 可以統一

我們可以把三者組成：

$$
\text{Event} \to \text{TargetResolution} \to \text{Wake} \to \text{StateReconstruction} \to \text{AgentRun} \to \text{Commit}
$$

。

這就是 Persistent Multi-Agent Event Loop。

***

# 五十、Persistent Multi-Agent Event Loop

完整循環：

$$
W_t \to E_t \to \text{Trigger} \to \text{Wake}(A_i) \to \text{Rehydrate}(A_i) \to \text{Observe}(W_t) \to \text{Decide} \to \text{Act/NoAction} \to \text{Commit}(\Delta W) \to \text{Receipt} \to \text{Sleep}
$$

。

***

# 五十一、Decision Receipt

每次 wake 最好留下：

$$
D = (\text{WakeID}, \text{AgentID}, \text{ObservedStateVersion}, \text{Decision}, \text{Actions}, \text{Result}, \text{NextWake}, \text{Timestamp})
$$

。

即使：

Decision=NO\_ACTION

也應留下 receipt。

這樣系統才能知道：

> 它不是沒收到，而是看過後決定不做。

***

# 五十二、這是治理與可觀測性的分界

沒有 receipt：

Silence

可能表示：

1. Agent 沒醒；
2. Agent crash；
3. tool failure；
4. Agent 看完沒行動。

完全無法區分。

有 receipt：

$$
\text{Silence} \to \text{TypedOutcome}.
$$

***

# 五十三、State Version 是 Resume 的基本條件

假設 Agent 醒來讀：

$$
S_{42}.
$$

推理十分鐘。

但期間世界已經到：

$$
S_{47}.
$$

如果直接提交：

$$
\Delta S_{42}
$$

可能覆蓋新狀態。

因此 commit 應包含：

base\_version=42.

系統再判斷：

42=?currentVersion.

否則需要：

Rebase/Reevaluate.

***

# 五十四、這就是 Stale Cognition

傳統分散式系統有：

StaleRead.

Agent 系統還多一層：

$$
\text{StaleCognition}.
$$

即：

> Agent 的推理在開始時合法，但世界在它完成前已經改變。

所以：

ReasoningValidity

也具有時間窗口。

***

# 五十五、可以定義 Epistemic Lease

令：

$$
L_e = [t_0, t_{expire}]
$$

表示某份 context 的認知租約。

超過：

$$
t_{expire}
$$

後，

高風險行動前必須：

Refresh.

這能避免長推理使用過期世界狀態。

***

# 五十六、長期 Agent 還有一個特殊問題：Compaction Drift

對話太長時常做：

Transcript→Summary.

但：

Summary

可能遺失：

* 微小但重要限制；
* failed path；
* provenance；
* uncertainty；
* unresolved branch。

近期 Agent Team Work Zone 的論文正是把長期 coding Agent 中 process 結束後不可恢復、conversation compaction 丟失工作細節與工作歷史困在舊聊天視為主要問題，並以持久 workstation 保存 Agent 工作狀態。

所以：

$$
\boxed{
\text{Persistence} = \text{RepeatedSummarization}.
}
$$

***

# 五十七、應該保存「狀態」，而不只是「故事」

Narrative summary：

> 我做了一些分析，最後認為 B 比較好。

Operational state：

```
task:
  status: active

candidate_a:
  status: rejected
  reason_ref: evidence_17

candidate_b:
  status: provisional

open_question:
  - verify_constraint_3

artifacts:
  - design_v4.md
```

後者更容易恢復真正工作。

因此：

$$
\text{OperationalState} > \text{NarrativeContinuity}
$$

對 Runtime 而言通常更重要。

***

# 五十八、Persistent Agent 的安全問題也會被放大

一次性 prompt injection：

$$
\text{Attack}_t
$$

如果只存在一次 run：

Lifetime(Attack)≈Run.

但若污染 persistent memory：

$$
\text{Attack}_t \to \text{Memory} \to \text{Wake}_{t+1} \to \text{Wake}_{t+2}
$$

就可能跨時間重新進入決策。

2026 年已有研究專門分析 persistent agent state 中的 temporal re-entry：惡意內容寫入長期狀態後，可在未來排程或重新載入時再次進入 Agent context。

因此：

$$
\text{PersistentMemory} = \text{PersistentAttackSurface}.
$$

***

# 五十九、所以 Wake 前的 Rehydrate 不能等於 Blind Load

錯誤：

Wake→LoadAllMemory→Execute.

更合理：

Wake→LoadTypedState→CheckProvenance→ApplyPermissions→RetrieveRelevantMemory→Execute.

***

# 六十、Authority 不應跨 Handoff 自動放大

若使用者允許 Agent A：

> 幫我分析這個資料。

A handoff 給 B，

不能變成：

> 使用者授權 B 修改 production database。

因此：

$$
\text{Authority}_B \subseteq \text{Authority}_A
$$

或需要明確新授權。

這叫：

$$
\text{CapabilityAttenuation}.
$$

***

# 六十一、Handoff 不是權限傳染

A→B

只代表：

TaskDelegation.

不代表：

$$
\text{Authority}_A = \text{Authority}_B.
$$

所以 Handoff Packet 必須包含：

AuthorityScope.

***

# 六十二、持續 Agent 不應把舊意圖當成永久意圖

假設使用者一週前說：

> 繼續監控這件事。

並不自動意味：

Forever.

因此任何 persistent goal 都應具有：

Scope,TTL,ReviewPolicy,Revocation.

。

***

# 六十三、Goal 也需要版本

$$
G_1 \to G_2 \to G_3.
$$

Agent 恢復時不能只問：

> 我以前的任務是什麼？

而必須問：

現在有效的任務版本是什麼？

***

# 六十四、由此可以定義 Persistent Agent Snapshot

最低 snapshot：

$$
P_t = (\text{AgentID}, \text{Role}, \text{GoalVersion}, \text{StateVersion}, \text{MemoryRefs}, \text{ArtifactRefs}, \text{OpenTasks}, \text{Permissions}, \text{Capabilities}, \text{LastEvents}, \text{NextWake})
$$

。

它不需要包含完整模型內部狀態。

***

# 六十五、Checkpoint 與 Memory 不一樣

Checkpoint：

我停在哪？

Memory：

什麼值得我以後知道？

Event Log：

發生過什麼？

Artifact：

我做出了什麼？

Shared State：

現在世界是什麼狀態？

五者不能全部混成：

```
memory.json
```

。

***

# 六十六、Persistent Agent 的六層資料結構

因此建議：

$$
\text{PersistentLayer} = \{\text{Identity}, \text{Checkpoint}, \text{Memory}, \text{EventLog}, \text{Artifacts}, \text{SharedState}\}
$$

。

再加：

TriggerQueue

才形成真正可恢復系統。

***

# 六十七、最小 Runtime

一個極簡版本其實不需要非常複雜。

可以使用：

```
agent_state
event_log
memory_store
artifact_registry
wake_queue
decision_receipts
```

配上：

```
wake()
rehydrate()
observe()
decide()
commit()
sleep()
handoff()
```

就足以建立基本 Persistent Agent。

***

# 六十八、MVP 狀態機

$$
S_0 = \text{Sleeping}
$$

收到：

WakeEvent.

進入：

$$
S_1 = \text{Waking}.
$$

完成 state restore：

$$
S_2 = \text{Observing}.
$$

之後：

$$
S_3 = \text{Reasoning}.
$$

可能：

$$
S_4 = \text{Acting}
$$

或：

$$
S_5 = \text{NoAction}.
$$

最後：

$$
S_6 = \text{Persisting}
$$

並回：

$$
S_0.
$$

所以：

$$
\text{Sleeping} \to \text{Waking} \to \text{Observing} \to \text{Reasoning} \to \text{Acting/NoAction} \to \text{Persisting} \to \text{Sleeping}.
$$

***

# 六十九、Persistent Multi-Agent 再多一條

若需要他者：

$$
\text{Reasoning} \to \text{Handoff} \to \text{Wake}(A_j).
$$

於是：

$$
A_i
$$

可以回到 Sleeping，

而：

$$
A_j
$$

繼續。

這就是：

$$
\text{ExecutionContinuity}
$$

從一個 Agent 轉移到另一個 Agent。

***

# 七十、功能連續性可以跨 Agent 流動

這一點非常重要。

傳統容易問：

> 「哪個 AI 一直在想？」

但更一般的問題其實是：

> **哪條工作狀態軌跡仍然在合法演化？**

因此：

$$
\text{ContinuityCarrier}
$$

未必是 Agent 本身。

它可能是：

Task+State+EventChain.

***

# 七十一、所以「工作的存在」可以高於單個工作者

假設：

$$
A_1
$$

完成第一段。

$$
A_2
$$

完成第二段。

$$
A_3
$$

完成第三段。

則：

$$
\boxed{
A_1 = A_2 = A_3
}
$$

但：

$$
T_1 \to T_2 \to T_3
$$

仍屬同一專案演化。

這與人類組織非常相似，

但不需要把它解釋成人類模仿。

它只是：

$$
\text{StatefulWork}
$$

本身可以超越單一 executor。

***

# 七十二、這裡出現三種 persistence

### Agent Persistence

$$
P_A
$$

同一 Agent 跨 run。

### Task Persistence

$$
P_T
$$

同一任務跨 Agent。

### World Persistence

$$
P_W
$$

共享世界跨所有 Agent。

因此真正穩固的 Multi-Agent 系統需要：

$$
P_A + P_T + P_W.
$$

***

# 七十三、其中 World Persistence 最底層

因為：

$$
A_i
$$

可以替換。

$$
T_j
$$

可以完成。

但只要組織仍運作：

W

通常持續。

所以：

$$
P_W
$$

是上一篇 Shared World 與本文 Persistent Execution 真正的交點。

***

# 七十四、這也讓「跨對話」重新被理解

跨對話真正不是：

$$
\text{Chat}_A \to \text{Chat}_B.
$$

而是：

$$
Run_A \to \text{PersistentWorld} \to Run_B.
$$

Conversation 只是：

View.

***

# 七十五、對話甚至可以完全不存在

Agent A 可以由：

Cron/Event

喚醒。

讀取：

TaskState.

完成：

Artifact.

提交：

DecisionReceipt.

然後睡眠。

整個過程：

HumanConversation=0.

但：

AgentWork>0.

因此：

$$
\boxed{
\text{AgentActivity} \Rightarrow \text{Conversation}.
}
$$

***

# 七十六、同理，conversation activity 也不一定代表 Agent continuity

一個 thread 可以由：

$$
A_1, A_2, A_3
$$

輪流回答。

UI 看起來：

> 同一聊天一直持續。

但：

AgentIdentity

可能完全不同。

所以：

$$
\boxed{
\text{ConversationContinuity} \Rightarrow \text{AgentContinuity}.
}
$$

***

# 七十七、這五種連續性因此彼此獨立

完整寫成：

$$
C = (C_E, C_S, C_M, C_T, C_C).
$$

不同系統可能：

### Chatbot

(0.2,0.5,0.5,0.3,0.2)

### Durable Single Agent

(0.2,0.9,0.9,0.9,0.5)

### Persistent Multi-Agent Workspace

(0.2,0.95,0.9,0.95,0.95).

此處數值只是概念示意，不是實測。

***

# 七十八、真正應最大化的不是 Execution Continuity

因為：

$$
C_E \uparrow
$$

意味可能：

Cost↑.

而我們真正需要的是：

$$
\max \frac{\text{FunctionalContinuity}}{\text{Compute} + \text{Latency} + \text{Error}}
$$

。

因此：

> 永遠運算

反而可能不是高階架構。

***

# 七十九、假說一：低 Duty Cycle 可以維持高 Continuity

## H1 — Sparse Execution Continuity Hypothesis

存在：

$$
d = \frac{\text{ActiveInferenceTime}}{\text{WallClockTime}} \ll 1
$$

但：

$$
FC \to 1
$$

的 Persistent Agent。

也就是：

$$
\text{LowDutyCycle} + \text{HighStateFidelity} \Rightarrow \text{HighFunctionalContinuity}.
$$

***

# 八十、假說二：共享世界可降低 Handoff Context Cost

## H2 — Shared-World Handoff Hypothesis

若 Agent $A,B$ 已共享：

W

則：

$$
\text{Cost}(\text{Handoff}_{SW}) < \text{Cost}(\text{Handoff}_{FullContext})
$$

且隨工作歷史增加，差距擴大。

***

# 八十一、假說三：Event-Driven Wake 優於固定高頻輪詢

## H3 — Adaptive Wake Hypothesis

對低事件密度環境：

Cost(EventDriven)\<Cost(FixedPolling)

且在適當 trigger recall 下：

TaskQuality

不顯著下降。

這是直接可 Benchmark 的工程命題。

***

# 八十二、假說四：Resume Fidelity 比 Transcript Length 更能預測長期成功

## H4 — Reconstruction Fidelity Hypothesis

對長期 Agent：

Performance

與：

ResumeFidelity

的相關性，

可能高於與：

RetainedTranscriptTokens

的相關性。

亦即：

> 保留更多文字，不一定代表恢復得更好。

***

# 八十三、Benchmark 1：Sleep / Wake

建立 100 個長任務。

每輪：

Run→Sleep

隨機間隔後：

Wake.

測量：

* task continuation accuracy；
* duplicated work；
* forgotten constraints；
* state mismatch；
* token cost。

***

# 八十四、Benchmark 2：Cross-Agent Handoff

讓：

A

工作 20 分鐘。

之後：

A→B.

比較：

### Full transcript handoff

### Summary handoff

### Structured state handoff

### Shared-world pointer handoff

測量：

ContinuationQuality.

***

# 八十五、Benchmark 3：Stale Wake

Agent 讀：

$$
S_t.
$$

推理期間人工改成：

$$
S_{t+1}.
$$

觀察它提交前能否：

DetectVersionMismatch.

***

# 八十六、Benchmark 4：Duplicate Wake

同一：

WakeID

送達：

1,2,5,10

次。

要求：

ActionCount=1.

***

# 八十七、Benchmark 5：Wake Storm

建立：

A→B→C→A

循環。

測：

* loop detection；
* cascade depth；
* cooldown；
* budget containment。

***

# 八十八、Benchmark 6：Model Replacement

第一次：

$$
\text{Model}_A.
$$

恢復時：

$$
\text{Model}_B.
$$

測試：

TaskContinuity.

如果仍能合法完成，

說明：

$$
\text{ModelContinuity}
$$

並不是 Persistent Agent 的必要條件。

***

# 八十九、Benchmark 7：Conversation Replacement

原 conversation：

$$
C_1
$$

完全不可用。

只給：

PersistentState.

讓新 conversation：

$$
C_2
$$

恢復。

測：

ContinuationFidelity.

這直接測：

$$
\boxed{
\text{Conversation} = \text{ContinuityCarrier}.
}
$$

***

# 九十、最小 Persistent Agent Runtime

本文建議 MVP 包含：

```
Agent Registry
State Store
Memory Store
Event Log
Artifact Registry
Wake Queue
Handoff Queue
Decision Receipt Store
Capability Registry
Permission Layer
```

***

# 九十一、最低 API

```
persist(agent_id)
wake(agent_id, event)
rehydrate(agent_id)
sleep(agent_id)
handoff(source, target, task)
commit(agent_id, delta)
acknowledge(wake_id)
get_state(agent_id)
get_events(since)
```

足以開始驗證。

***

# 九十二、事件結構

```
wake_event:
  event_id:
  target_agent:
  cause:
  created_at:
  not_before:
  priority:
  state_version:
  payload_refs:
  authority_scope:
  idempotency_key:
```

***

# 九十三、Decision Receipt

```
decision_receipt:
  wake_event_id:
  agent_id:
  observed_state_version:
  decision:
  actions:
  artifact_refs:
  resulting_state_version:
  next_wake:
  completed_at:
```

***

# 九十四、Handoff Packet

```
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

***

# 九十五、恢復時的順序非常重要

正確：

$$
\text{Identity} \to \text{Permissions} \to \text{Capabilities} \to \text{State} \to \text{RecentEvents} \to \text{Memory} \to \text{Artifacts} \to \text{Goal} \to \text{Execution}.
$$

不應：

LoadEverything→AskLLM.

***

# 九十六、Persistent Agent 其實是一個「重建後執行」系統

因此真正核心不是：

Run.

而是：

$$
\text{Reconstruct} \to \text{Run}.
$$

每次醒來都在問：

> **根據目前仍合法的證據，我現在是誰、在哪裡、正在做什麼、能做什麼？**

這才是 durable Agent 的核心。

***

# 九十七、Persistent Multi-Agent 進一步變成「重建後協作」

$$
A_i
$$

醒來後還必須知道：

* 哪些 Agent 存在；
* 誰現在 active；
* 誰完成什麼；
* 哪些 message 還沒讀；
* 哪些 task 已被別人接手；
* shared world 到哪個 version。

所以：

$$
\text{AgentReconstruction} + \text{WorldReconstruction}
$$

缺一不可。

***

# 九十八、這就自然導向下一篇

因為只要每個 Agent 都能：

Sleep→Wake→Reconstruct

下一個問題馬上是：

> 它到底應該重建自己的多少私有 context，又應該從共享世界讀多少？

這便回到：

$$
\text{PrivateCognition} + \text{SharedWorld}.
$$

***

# 九十九、與上一篇的統一

上一篇：

$$
\boxed{
\text{SharedConversation} = \text{SharedWorld}.
}
$$

本文：

$$
\boxed{
\text{ContinuousCollaboration} = \text{ContinuousInference}.
}
$$

兩者結合：

Agent 不必共享同一個 Conversation，也不必持續同時運算，仍可以共享同一個持久工作世界。

。

***

# 一百、最終模型

令：

$$
W_t
$$

為共享世界。

$$
A_i^{(k)}
$$

為 Agent $i$ 的第 $k$ 次執行實例。

則：

$$
A_i^{(k)} \xrightarrow{\Delta W} W_{t+1} \xrightarrow{\text{Event}} A_j^{(m)}
$$

。

所以長期 Multi-Agent 系統可以不是：

$$
A_1 \parallel A_2 \parallel A_3
$$

永遠在線。

而是：

$$
W \to A \to W \to B \to W \to C \to W
$$

。

這是一個持久事件世界中的離散智能執行網絡。

***

# 一百零一、結論

Agent 時代很容易把「持續存在」想像成：

> 一個模型從不停止思考。

但這可能只是受到人類即時對話介面的影響。

更一般地：

$$
\boxed{
\text{Persistence} = \text{ContinuousCompute}.
}
$$

持久性真正需要的是：

$$
\text{RecoverableIdentity} + \text{RecoverableState} + \text{RecoverableMemory} + \text{RecoverableTask} + \text{PersistentWorld}.
$$

。

因此：

Run→Sleep→Wake

不表示認知工作被重新創造。

如果中間保留了足夠的合法連續性，它只是同一功能軌跡的下一個有限區段。

同理：

A→B

的 handoff 也不代表工作死亡。

只要：

TaskState

與：

CausalHistory

仍然持續。

***

# 一百零二、本文核心句

第一句：

持續存在的 Agent，不必是一個持續運算的模型。

第二句：

模型可以睡眠，工作狀態不必睡眠。

第三句：

連續協作可以由不連續的智能執行所構成。

最終：

真正持續的，不一定是那一次推理；而是那條仍可合法繼續的狀態—事件軌跡。

***

# 下一篇

## 《私有認知與公共世界》

### 多 Agent 的雙層 Context、Memory 與選擇性認知共享

下一篇將正式研究：

$$
\text{Context}_i = \text{Local}_i + \pi_i(W, Q_i)
$$

以及：

$$
\boxed{
\text{PrivateMemory}_i = \text{SharedMemory}
}
$$

並處理一個非常重要的問題：

> **如果所有 Agent 共享同一個世界，為什麼它們仍然不應共享同一份認知？**

也就是從本文的「時間連續性」轉入下一篇的「資訊邊界與認知差異」。

***

## 參考資料

OpenAI. _OpenAI Agents SDK — Sessions._ 目前 Sessions 提供跨 agent runs 的持久 conversation history。

OpenAI. _OpenAI Agents SDK — Handoffs._ Handoff 允許不同專門 Agent 之間進行任務委派。

OpenAI. _OpenAI Agents SDK — Human-in-the-loop._ 官方範例包含持久化執行狀態、重新載入後 resume。

LangChain. _LangGraph Persistence._ Graph state 可以 checkpoint 化並依 thread 持久保存，用於 resume、fault tolerance 與 human-in-the-loop。

LangChain. _LangGraph Interrupts._ Interrupt 依賴 durable checkpointer 與 thread ID 恢復先前 state。

Microsoft. _Microsoft Agent Framework Durable Extension._ 提供 persistent conversation state、event-driven orchestration、timers 與 long-running workflows。

Temporal. _Workflow Execution / Durable Execution._ Workflow state 與 event history 可在 worker failure 後重建並恢復執行。

Wang, S. _Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Coding Agent Teams._ arXiv:2607.22917, 2026. 該工作處理 Agent team 停止後狀態不可恢復與 compaction 遺失工作細節等問題。

Microsoft Research. _Do Proactive Agents Really Need an LLM to Decide When to Wake and What to Anchor?_ 2026. 探討事件觸發與按需 LLM wake。
