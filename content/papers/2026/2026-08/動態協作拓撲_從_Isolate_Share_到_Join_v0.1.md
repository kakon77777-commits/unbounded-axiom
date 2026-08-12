# 動態協作拓撲：從 Isolate、Share 到 Join
## 多 Agent 如何依任務在獨立、共享與共同對話之間切換

**English Title:** *Dynamic Collaboration Topology: From Isolate and Share to Join in Multi-Agent Systems*  
**系列：**《跨對話智能協作與共享認知空間》第四篇  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**性質：** 公開理論論文／Multi-Agent Orchestration & Dynamic Topology  
**版本：** v0.1  
**日期：** 2026-08-09  

---

## 摘要

前三篇已分別建立：

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

以及：

$$
\boxed{
\text{Shared World}
\neq
\text{Shared Cognition}
}
$$

這些區分共同指出：Multi-Agent 系統不需要把所有 Agent 固定塞入同一個 conversation，也不需要要求所有 Agent 持續同時運算，更不需要讓所有 Agent 擁有相同 context 與 memory。

由此自然產生下一個問題：

> **既然 Agent 可以獨立、可以只共享成果，也可以臨時加入共同對話，那麼「如何協作」本身是否應成為一個動態變量？**

本文回答：是。

本文提出三個基本協作算子：

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
\mathcal J=\operatorname{Join}
}
$$

其中：

- $\mathcal I$：維持認知與工作空間隔離；
- $\mathcal S$：交換 Typed Cognitive Delta、狀態、事件或 artifact，而不合併完整 context；
- $\mathcal J$：建立暫時高耦合 shared room / shared conversation。

因此，Multi-Agent 系統不再只有一個固定團隊結構，而具有隨時間演化的協作圖：

$$
\boxed{
G_t^{agents}
=
(V_t,E_t,\mu_t)
}
$$

其中 $\mu_t$ 描述每條 Agent 關係當前處於何種協作模式。

本文進一步提出 Adaptive Collaboration Topology Controller（ACTC），由任務依賴、不確定性、衝突、時間壓力、認知多樣性需求、成本、權限與風險等訊號動態決定：

$$
\boxed{
Topology_{t+1}
=
\mathcal T(
Topology_t,
Task_t,
World_t,
Telemetry_t
)
}
$$

本文主張，高階 Multi-Agent orchestration 不應只回答：

> 「哪一個 Agent 要做這件事？」

還應回答：

> **「這些 Agent 此刻應該保持獨立、只共享成果，還是進入同一個高耦合認知房間？」**

本文同時討論 topology thrashing、groupthink、communication explosion、premature joining、late joining、privilege spread、failure cascade、coordination deadlock 與 topology mutation safety，並提出 hysteresis、minimum dwell time、shadow topology、budget gate、authority attenuation 與 causal receipts 等安全機制。

最後，本文給出最小 Dynamic Multi-Agent Topology Runtime 與 benchmark，為系列第五篇《Persistent Multi-Agent Workspace：跨對話共享世界 Runtime 與 MVP》建立最後一塊控制層。

---

## 關鍵詞

Multi-Agent Systems、Dynamic Topology、Agent Orchestration、Agent Handoff、Shared Workspace、Adaptive Collaboration、Agent Graph、Isolate、Share、Join、Coordination Policy、Persistent Agents

---

# 一、前三篇其實只完成了「可以分開」

第一篇說：

$$
\text{共享對話}
\neq
\text{共享世界}.
$$

第二篇說：

$$
\text{持續協作}
\neq
\text{持續推理}.
$$

第三篇說：

$$
\text{共享世界}
\neq
\text{共享認知}.
$$

但這些都還是一種靜態描述。

它們告訴我們：

> 可以分開。

卻還沒有回答：

> **什麼時候該分開？什麼時候該連起來？**

---

# 二、固定拓撲是早期 Multi-Agent 的自然做法

典型系統常預先設定：

### Sequential

$$
A\rightarrow B\rightarrow C.
$$

### Parallel

$$
A\parallel B\parallel C.
$$

### Hierarchical

$$
M\rightarrow\{A,B,C\}.
$$

### Group Chat

$$
A,B,C\in R.
$$

### Handoff

$$
A\rightarrow B.
$$

2026 年公開框架已經把多種 orchestration pattern 正式做成一等能力。OpenAI Agents SDK 同時支援 manager-style agents-as-tools 與 handoff；Google ADK 提供 sequential、parallel、loop 與 custom agent workflows；Microsoft Agent Framework 直接列出 sequential、concurrent、handoff、group chat 與 magentic 等多 Agent orchestration pattern；LangGraph 則明確把 multi-agent workflow 建模成可自訂 graph。

這些都說明：

$$
\boxed{
\text{Collaboration Pattern}
}
$$

已經是 Agent 工程的重要控制面。

---

# 三、但「有很多 pattern」仍然不等於「拓撲會自己變」

如果系統啟動時選：

$$
Topology=\tau_1
$$

直到任務結束仍固定：

$$
Topology_t=\tau_1
\quad
\forall t,
$$

它仍是：

$$
\boxed{
Static Orchestration.
}
$$

本文關心的是：

$$
\boxed{
Topology_t
\neq
Topology_{t+1}
}
$$

而且改變是由任務與系統狀態驅動。

---

# 四、真正問題：協作方式本身是不是 action？

傳統 Agent action：

$$
a_t
=
\text{search / write / call tool / answer}.
$$

本文增加：

$$
\boxed{
a_t^{topology}
}
$$

例如：

- 保持自己工作；
- 把結果發布給 B；
- 邀請 C 進入共同 room；
- 離開 room；
- 暫停與 D 的同步；
- 把任務拆成兩個獨立子群；
- 合併兩個正在重複工作的群。

因此：

$$
\boxed{
\text{Changing Collaboration Structure}
}
$$

本身就是一種 Agent action。

---

# 五、三個基本算子

本文先只保留最小三元組：

$$
\boxed{
\{\mathcal I,\mathcal S,\mathcal J\}
}
$$

---

# 六、Isolate

定義：

$$
\boxed{
\mathcal I(A_i,Q)
}
$$

表示 Agent $A_i$ 對任務 $Q$ 暫時維持局部認知隔離。

它可以：

- 讀必要 shared state；
- 保有 private memory；
- 自行使用工具；
- 產生 private hypotheses；

但不預設取得其他 Agent 的完整推理輸出。

因此：

$$
Context_i
=
L_i+\pi_i(W).
$$

而：

$$
Context_i
\not\supset
Context_j.
$$

---

# 七、Isolate 並不表示完全斷網

Isolate 的真正意義不是：

$$
Communication=0.
$$

而是：

$$
\boxed{
CognitiveCoupling
\downarrow.
}
$$

例如 Agent 仍知道：

> Task X 已由 B 完成。

但不讀：

> B 是怎麼想出來的。

所以：

$$
\boxed{
OperationalAwareness
+
CognitiveIsolation
}
$$

可以同時成立。

---

# 八、Share

第二個算子：

$$
\boxed{
\mathcal S(A_i,A_j,x)
}
$$

把一個受治理的認知增量 $x$ 分享給另一 Agent 或 shared world。

 $x$ 可以是：

$$
x=
(
Message,
Claim,
Evidence,
Artifact,
StateDelta,
Decision,
Question
).
$$

而不是：

$$
x=EntireContext_i.
$$

因此：

$$
\boxed{
Share
\neq
Merge.
}
$$

---

# 九、Typed Cognitive Delta

上一篇已提出：

$$
\boxed{
\Delta_i^{cog}
}
$$

作為交換單位。

本文延伸：

$$
\mathcal S:
\Delta_i^{cog}
\rightarrow
W
$$

或：

$$
\mathcal S:
\Delta_i^{cog}
\rightarrow
A_j.
$$

這使協作可以保持低耦合。

---

# 十、Join

第三個算子：

$$
\boxed{
\mathcal J(A_1,\ldots,A_k,R)
}
$$

建立暫時 shared room：

$$
R.
$$

進入後：

$$
CognitiveCoupling\uparrow.
$$

Agent 共享：

- 對話歷史；
- 當前爭議；
-共同 reference；
- room artifacts；
- room-local memory。

所以：

$$
\boxed{
Join
=
TemporaryHighCoupling.
}
$$

---

# 十一、Join 不等於永久合併

Room $R$ 可以存在：

$$
[t_0,t_1].
$$

結束後：

$$
\mathcal D(R)
\rightarrow
\Delta W
$$

其中 $\mathcal D$ 是 room distillation。

然後：

$$
A_i
\rightarrow
PrivateMode_i.
$$

因此：

$$
\boxed{
Join
\rightarrow
Discuss
\rightarrow
Commit
\rightarrow
Separate.
}
$$

---

# 十二、這三個算子形成一條協作光譜

可以近似：

$$
\boxed{
Isolate
\leftrightarrow
Share
\leftrightarrow
Join.
}
$$

其耦合程度：

$$
\kappa_{\mathcal I}
<
\kappa_{\mathcal S}
<
\kappa_{\mathcal J}.
$$

---

# 十三、但它不是一條單向成熟階梯

不是：

$$
Isolate
\rightarrow
Share
\rightarrow
Join
$$

越後面越高階。

真正成熟的是：

$$
\boxed{
\text{能依任務切換。}
}
$$

有時最聰明的動作就是：

$$
\mathcal I.
$$

---

# 十四、Agent Collaboration Graph

令 Agent 集合：

$$
V_t
=
\{A_1,\ldots,A_n\}.
$$

定義：

$$
\boxed{
G_t
=
(V_t,E_t,\mu_t,\omega_t)
}
$$

其中：

- $E_t$：當前協作邊；
- $\mu_t(e)$：邊的模式；
- $\omega_t(e)$：邊的權重／耦合強度。

例如：

$$
\mu_t(e_{ij})
\in
\{
ISOLATED,
SHARE,
JOIN,
HANDOFF
\}.
$$

---

# 十五、Isolate 可以用「無高耦合邊」表示

若：

$$
A_i
$$

暫時獨立，

則：

$$
deg_{high}(A_i)=0.
$$

但仍可能對 shared world：

$$
W
$$

具有讀寫邊。

因此：

$$
\boxed{
AgentGraph
}
$$

與：

$$
\boxed{
WorldAccessGraph
}
$$

最好分開。

---

# 十六、雙圖模型

定義：

$$
G_t^A
$$

為 Agent-to-Agent collaboration graph。

定義：

$$
G_t^W
$$

為 Agent-to-World access graph。

則 Agent 可以：

$$
deg_{G^A}(A_i)=0
$$

但：

$$
deg_{G^W}(A_i)>0.
$$

這正是：

> 自己工作，但仍知道公共專案世界。

---

# 十七、Shared Room 更像 Hyperedge

如果：

$$
R=\{A,B,C,D\}
$$

共同進入一個 room，

它不一定適合表示成六條 pairwise edge。

更自然可使用 hyperedge：

$$
\boxed{
h_R=\{A,B,C,D\}.
}
$$

因此更一般：

$$
G_t
$$

可以是 dynamic hypergraph。

---

# 十八、這代表「會議」本身是拓撲物件

Room：

$$
R_k
$$

具有：

- participant set；
- context；
- start；
- end；
- goal；
- decision state。

所以：

$$
\boxed{
Room
}
$$

不只是 UI container，

而是一個 temporary collaboration topology object。

---

# 十九、為什麼要動態？

因為不同子任務需要不同耦合。

例如研究任務：

### Phase 1

三個 Agent 獨立找方案：

$$
A\parallel B\parallel C.
$$

### Phase 2

只共享 evidence：

$$
\mathcal S(A,W),
\mathcal S(B,W),
\mathcal S(C,W).
$$

### Phase 3

出現衝突：

$$
\mathcal J(A,B,C,R).
$$

### Phase 4

形成決議：

$$
R\rightarrow Decision\rightarrow W.
$$

### Phase 5

再次分工：

$$
A\parallel B.
$$

所以：

$$
\boxed{
Topology
}
$$

天然隨 workflow phase 變動。

---

# 二十、Static Topology 的第一個問題：過度溝通

若所有 Agent 永遠：

$$
JOIN,
$$

則：

$$
CommunicationCost
\uparrow.
$$

Agent 越多：

$$
MessageVolume
$$

可能快速增加。

全互聯時：

$$
|E|
=
\frac{n(n-1)}{2}.
$$

因此：

$$
O(n^2)
$$

的 pairwise communication opportunity 很快形成。

---

# 二十一、過度溝通不只是 token 成本

還會增加：

- anchoring；
- duplicated discussion；
- stale references；
- context pollution；
- conflict-resolution overhead；
- attention dilution。

所以：

$$
\boxed{
MoreCommunication
\not\Rightarrow
BetterCoordination.
}
$$

---

# 二十二、Static Topology 的第二個問題：溝通不足

若所有 Agent 永遠：

$$
ISOLATE,
$$

則：

- 重複工作；
- state divergence；
- artifact conflict；
- missing dependency；
- delayed correction。

因此：

$$
\boxed{
ZeroCoupling
}
$$

也不是一般最優解。

---

# 二十三、最佳耦合通常位於中間

可以定義 collaboration coupling：

$$
\kappa_t\in[0,1].
$$

則總效用：

$$
U(\kappa)
=
Q(\kappa)
-
C(\kappa)
-
F(\kappa)
-
A(\kappa),
$$

其中：

- $Q$：協作品質；
- $C$：通信成本；
- $F$：failure propagation；
- $A$：anchoring / diversity loss。

可能存在：

$$
\boxed{
0<\kappa^*<1.
}
$$

---

# 二十四、因此需要 Topology Controller

本文提出：

## Adaptive Collaboration Topology Controller（ACTC）

定義：

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

# 二十五、Controller 不只選 Agent

傳統 router：

$$
Q\rightarrow A_i.
$$

ACTC：

$$
\boxed{
Q
\rightarrow
(
AgentSet,
Topology,
Coupling,
Duration,
SharingPolicy
).
}
$$

所以 orchestration decision 變成多維。

---

# 二十六、Controller 的主要輸入一：Task Dependency

若：

$$
Task_B
$$

高度依賴：

$$
Output_A,
$$

則：

$$
Share(A,B)
$$

或 sequential handoff 較合理。

若：

$$
Task_A\perp Task_B,
$$

則：

$$
Isolate(A,B)
$$

或 parallel 執行更合理。

---

# 二十七、Task Dependency Graph

定義：

$$
D_T=(V_T,E_T).
$$

若：

$$
e_{ij}\in E_T
$$

表示：

$$
T_j
$$

依賴：

$$
T_i.
$$

那麼 Agent topology 應部分映射：

$$
D_T
\rightarrow
G_t^A.
$$

但不需要一一相同。

---

# 二十八、Controller 的主要輸入二：Uncertainty

當：

$$
U_i\uparrow,
$$

Agent 可以：

1. 自己展開；
2. retrieve more evidence；
3. Share 問另一 Agent；
4. Join room。

所以：

$$
Uncertainty
$$

本身不是 Join 的充分條件。

---

# 二十九、可定義 Escalation Ladder

$$
\boxed{
SelfRefine
\rightarrow
Retrieve
\rightarrow
Share
\rightarrow
Join.
}
$$

只有前面不足才升級。

這避免所有疑問都：

> 叫全公司開會。

---

# 三十、Controller 的主要輸入三：Conflict

若：

$$
Claim_A
\neq
Claim_B
$$

且差異影響後續公共狀態：

$$
Impact(Conflict)>\theta,
$$

可觸發：

$$
\mathcal J(A,B,R).
$$

若只是各自 hypothesis：

$$
Impact<\theta,
$$

則可維持 plural state。

---

# 三十一、Conflict 不等於立即 Join

因為：

$$
Join
$$

可能造成過早 convergence。

所以：

$$
\boxed{
JoinIf
\quad
Conflict
\times
DecisionNeed
\times
Dependency
>
Threshold.
}
$$

---

# 三十二、Controller 的主要輸入四：Diversity Need

對 brainstorming、red team、independent proof：

$$
DiversityNeed\uparrow.
$$

則：

$$
P(\mathcal I)\uparrow.
$$

對 execution alignment：

$$
DiversityNeed\downarrow,
CoordinationNeed\uparrow.
$$

則：

$$
P(\mathcal S/\mathcal J)\uparrow.
$$

---

# 三十三、Controller 的主要輸入五：Urgency

如果 deadline 很近：

$$
TimeBudget\downarrow.
$$

高耦合 room 可能降低 coordination latency。

因此：

$$
Urgency\uparrow
\Rightarrow
JoinPressure\uparrow
$$

可能成立。

但若 room overhead 太高，也可能反而直接 handoff 給單一決策 Agent。

---

# 三十四、Controller 的主要輸入六：Risk

高風險任務可能需要：

$$
IndependentReview
$$

先：

$$
\mathcal I
$$

再：

$$
\mathcal S
$$

最後：

$$
\mathcal J
$$

形成決議。

即：

$$
\boxed{
Risk\uparrow
\not\Rightarrow
ImmediateJoin.
}
$$

高風險有時反而更需要先隔離。

---

# 三十五、Controller 的主要輸入七：Cost

令：

$$
C_t=
(
Token,
Compute,
Latency,
Bandwidth,
ToolCost
).
$$

若：

$$
C_{join}\gg C_{share},
$$

而 task gain 很小，

則：

$$
\mathcal S
$$

優於：

$$
\mathcal J.
$$

---

# 三十六、Controller 的主要輸入八：Privacy / Authority

Agent A 有資料：

$$
x
$$

但 Agent B 無權讀。

則：

$$
\mathcal J(A,B)
$$

不應自動讓 B 得到 $x$。

因此：

$$
\boxed{
Join
\neq
PermissionMerge.
}
$$

---

# 三十七、Room Context 也應是 Projection

就算 Join：

$$
A,B,C\in R,
$$

實際 room context 仍應：

$$
Context_i^R
=
\pi_i^R(W,L_i,Permissions_i).
$$

所以：

$$
\boxed{
SharedRoom
}
$$

也不必代表完全相同 view。

---

# 三十八、這產生「不對稱會議」

A 可以看到完整 security log。

B 只能看到摘要。

C 只能看到決策問題。

三者仍可以在：

$$
R
$$

協作。

因此：

$$
\boxed{
Join
\not\Rightarrow
SymmetricInformation.
}
$$

---

# 三十九、Topology State

可定義：

$$
\boxed{
Z_t=
(
V_t,
E_t,
Rooms_t,
Modes_t,
Permissions_t,
Budgets_t
).
}
$$

ACTC 的工作：

$$
Z_t\rightarrow Z_{t+1}.
$$

---

# 四十、拓撲切換本身也有成本

由：

$$
\mathcal I\rightarrow\mathcal J
$$

需要：

- 建 room；
- retrieve context；
- summarize local state；
- resolve participants；
- allocate budget。

因此：

$$
\boxed{
SwitchCost>0.
}
$$

---

# 四十一、若不考慮 SwitchCost 會產生 Topology Thrashing

例如：

$$
I\rightarrow S\rightarrow I\rightarrow S
$$

每分鐘切換。

系統大量成本花在：

$$
\text{reconfiguration}
$$

而不是 task。

這叫：

$$
\boxed{
TopologyThrashing.
}
$$

---

# 四十二、Hysteresis

避免 thrashing，可設定不同進入／離開門檻。

例如：

$$
Join
$$

需要：

$$
P_J>\theta_{enter}.
$$

但已在 room 後，

只有：

$$
P_J<\theta_{exit}
$$

才離開，

其中：

$$
\theta_{exit}<\theta_{enter}.
$$

這形成：

$$
\boxed{
Hysteresis.
}
$$

---

# 四十三、Minimum Dwell Time

也可設定：

$$
T_{dwell}\ge T_{min}.
$$

除非安全事件，

否則 topology 進入某模式後至少維持：

$$
T_{min}.
$$

---

# 四十四、Maximum Dwell Time

反過來 shared room 也不應永久不散。

若：

$$
T_{room}>T_{max}
$$

則觸發：

$$
Review(Room).
$$

避免：

$$
\boxed{
PermanentMeetingState.
}
$$

---

# 四十五、Join 的入口條件

可定義：

$$
JScore
=
\alpha Conflict
+
\beta Dependency
+
\gamma Urgency
+
\delta SharedDecisionNeed
-
\epsilon Cost
-
\zeta DiversityNeed.
$$

若：

$$
JScore>\theta_J,
$$

則：

$$
\mathcal J.
$$

這只是 heuristic prototype。

---

# 四十六、Share 的入口條件

$$
SScore
=
\alpha CrossAgentUtility
+
\beta Dependency
+
\gamma Novelty
-
\delta PollutionRisk
-
\epsilon Cost.
$$

若：

$$
SScore>\theta_S,
$$

則：

$$
\mathcal S.
$$

---

# 四十七、Isolate 的入口條件

$$
IScore
=
\alpha DiversityNeed
+
\beta IndependentVerification
+
\gamma LowDependency
+
\delta AnchoringRisk.
$$

若：

$$
IScore>\theta_I,
$$

則：

$$
\mathcal I.
$$

---

# 四十八、這三個 score 不是互斥的

可能：

$$
IScore
$$

與：

$$
SScore
$$

同時高。

例如：

> 保持獨立推理，但定期共享證據。

所以狀態可以是：

$$
\boxed{
IsolatedReasoning
+
SharedEvidence.
}
$$

這不是矛盾。

---

# 四十九、因此拓撲模式應是組合式而非單一 enum

對 Agent $i$：

$$
Mode_i
=
(
ReasoningCoupling,
StateSharing,
MessageFrequency,
RoomMembership
).
$$

所以：

$$
\boxed{
Topology
}
$$

其實是多維控制場。

---

# 五十、Static Pattern 與 Dynamic Composition

公開框架目前已支援多種 pattern：

- sequential；
- concurrent；
- handoff；
- group chat；
- manager；
- custom graph。

下一步自然是：

$$
\boxed{
\text{Pattern Selection}
+
\text{Pattern Composition}
+
\text{Pattern Mutation}.
}
$$

而不是固定選一種直到任務結束。

---

# 五十一、2026 年研究已開始直接處理這個問題

近期研究已經不只比較「哪一種多 Agent 架構比較好」。

AdaptOrch 把任務自適應 orchestration 明確形式化為依 task dependency 與 domain 特徵，在 parallel、sequential、hierarchical、hybrid topology 間選擇。

ACL 2026 的 GTD 則直接研究依 performance、communication cost 與 robustness 生成 task-specific multi-agent communication topology。

另外也出現把 Agent coordination 視為 dynamic ad-hoc networking 的方法，讓 Agent 不依固定拓撲，而依 intent 進行 publish-subscribe 與動態訂閱。

這些研究共同顯示：

$$
\boxed{
\text{Topology}
}
$$

正在從人工固定設計，逐漸變成可優化的 runtime variable。

---

# 五十二、但本文與一般 topology optimization 有一個不同重點

很多 topology optimization 問：

> 哪些 Agent 應該互相連線？

本文還多問：

> **它們應該共享到什麼認知深度？**

所以 edge 不只：

$$
e_{ij}=1.
$$

而應包含：

$$
e_{ij}
=
(
Mode,
Scope,
Frequency,
Authority,
ContextDepth
).
$$

---

# 五十三、Edge Semantics

定義：

$$
\boxed{
e_{ij}(t)
=
(
\mu,
s,
f,
a,
d
)
}
$$

其中：

- $\mu$：Isolate / Share / Join / Handoff；
- $s$：scope；
- $f$：interaction frequency；
- $a$：authority；
- $d$：shared context depth。

因此：

$$
\boxed{
Connection
\neq
Binary.
}
$$

---

# 五十四、這與人類組織的相似性是結果，不是前提

我們可能發現：

- 獨立工作；
- 寄報告；
- 開會；
- 散會；

與人類團隊很像。

但本文不假設：

$$
AI\rightarrow HumanOrganizationCopy.
$$

更一般的原因可能是：

$$
\boxed{
有限局部系統
+
通信成本
+
協作需求
}
$$

自然產生類似結構。

這將留給後續另一個「跨尺度結構復現」系列處理。

---

# 五十五、Dynamic Topology 的核心不是擬人化

它只是：

$$
\boxed{
\text{Adaptive Information Coupling.
}
}
$$

何時：

- 降低耦合；
- 提高耦合；
- 改變資訊通道；
- 改變共同 context；

本質都是系統控制問題。

---

# 五十六、可以把 topology controller 看成 policy

$$
\boxed{
a_t^{topo}
\sim
\pi_{\theta}(a\mid z_t)
}
$$

其中：

$$
z_t=
(
Task,
Dependency,
Conflict,
Uncertainty,
Risk,
Cost,
Diversity,
Permissions
).
$$

---

# 五十七、第一階段不需要 RL

v0.1 完全可以：

$$
\boxed{
RuleBasedController.
}
$$

例如：

```text
IF independent_review:
    ISOLATE

IF artifact_ready AND dependency_exists:
    SHARE

IF unresolved_conflict AND decision_required:
    JOIN
```

先驗證架構是否有價值。

---

# 五十八、第二階段：Contextual Bandit

若每次 topology selection 是短期決策，

可以學：

$$
a_t
=
\arg\max_a
E[Reward\mid z_t,a].
$$

Reward：

$$
R
=
Q
-
\lambda_1 Cost
-
\lambda_2 Latency
-
\lambda_3 ErrorPropagation.
$$

---

# 五十九、第三階段：MDP / RL

若 topology choice 會影響未來：

$$
G_t
\rightarrow
G_{t+1}
\rightarrow
G_{t+2},
$$

可建成：

$$
\boxed{
MDP.
}
$$

State：

$$
z_t.
$$

Action：

$$
a_t^{topo}.
$$

Reward：

$$
r_t.
$$

---

# 六十、但不能讓 learned policy 無限制改 topology

因為 topology mutation 可能改變：

- 權限；
- memory routing；
- tool access；
- blast radius。

所以：

$$
\boxed{
PolicyDecision
\subset
SafetyEnvelope.
}
$$

---

# 六十一、Topology Safety Invariants

最低至少：

### I1 — Capability Bound

拓撲改變不能無故增加 Agent 權限。

$$
Capabilities_{after}
\subseteq
ApprovedCapabilities.
$$

### I2 — State Routing Completeness

必要 state 不應因 split / join 遺失。

### I3 — Provenance Preservation

跨 topology 後來源鏈仍可追溯。

### I4 — Identity Preservation

加入／拆分不應造成 Agent identity 混淆。

### I5 — Reversibility Where Possible

可回滾 topology mutation。

---

# 六十二、2026 年也已有研究直接碰「runtime topology mutation」

近期工作甚至開始研究在 Agent 過載時，動態拆成 specialized sub-agents，並用 capability、state routing 與 shadow validation 等 invariant 保護 runtime mutation。

這說明：

$$
\boxed{
\text{Topology Mutation}
}
$$

已經從理論可能性進入工程研究。

---

# 六十三、Shadow Topology

重大 topology 改變前，可先建立：

$$
G'
$$

但不接 live action。

讓：

$$
G'
$$

只讀 mirrored state，

執行：

$$
ShadowRun.
$$

若：

$$
Safety(G')\ge\theta,
$$

再：

$$
Promote(G').
$$

---

# 六十四、拓撲也需要版本

$$
\boxed{
TopologyVersion
=
v_t.
}
$$

所有 message／decision receipt 最好標記：

$$
topology_version.
$$

否則 Agent 可能依：

$$
G_{t-1}
$$

的假設提交到：

$$
G_t.
$$

---

# 六十五、Stale Topology

這是一種新的 stale cognition。

例如 A 以為：

> B 還負責安全審查。

但 topology 已改：

> C 接手。

所以：

$$
\boxed{
StaleTopology
}
$$

可能造成：

- routing error；
- duplicate work；
- privilege error；
- missing review。

---

# 六十六、拓撲變更應產生 Event

```yaml
topology_event:
  event_id:
  previous_version:
  new_version:
  operation:
  affected_agents:
  reason:
  authority:
  state_routing:
  created_at:
```

使：

$$
\boxed{
TopologyHistory
}
$$

也可追溯。

---

# 六十七、Join 需要 Join Receipt

```yaml
join_receipt:
  room_id:
  agent_id:
  context_scope:
  authority_scope:
  joined_at:
  topology_version:
```

---

# 六十八、Leave 也需要 Leave Receipt

因為：

> Agent 不再在 room

應成為明確狀態。

```yaml
leave_receipt:
  room_id:
  agent_id:
  reason:
  distilled_refs:
  left_at:
```

---

# 六十九、Share 需要 Delivery Semantics

分享不是：

$$
send()
$$

就結束。

至少區分：

$$
Delivered,
Read,
Processed,
Rejected,
Expired.
$$

否則：

> 我傳給 B 了

不代表：

> B 已經納入工作狀態。

---

# 七十、因此 Share 是一條小型事件鏈

$$
\boxed{
Publish
\rightarrow
Deliver
\rightarrow
Observe
\rightarrow
Integrate/Reject
\rightarrow
Receipt.
}
$$

---

# 七十一、Join 不是解決所有 disagreement 的方法

如果：

$$
A,B,C
$$

一直開會，

可能：

$$
Groupthink\uparrow.
$$

因此 room 可以有：

$$
BlindPhase
$$

要求各 Agent 先提交 private position。

再：

$$
Reveal.
$$

---

# 七十二、Blind-Then-Join

流程：

$$
\boxed{
Isolate
\rightarrow
CommitPrivatePosition
\rightarrow
Join
\rightarrow
Compare.
}
$$

這對：

- prediction；
- review；
- proof；
- safety audit；

很重要。

---

# 七十三、Join-before-think 與 Think-before-join 是不同拓撲

### Join-before-think

$$
J\rightarrow Reason.
$$

### Think-before-join

$$
I\rightarrow Reason\rightarrow J.
$$

即使最後 participant 一樣，

結果可能不同。

所以：

$$
\boxed{
TopologySequence
}
$$

也重要。

---

# 七十四、拓撲其實具有歷史依賴

因此：

$$
G_t
$$

不能只由：

$$
Task_t
$$

決定。

還要看：

$$
H_t^{topology}.
$$

例如 Agent 剛剛已獨立審查完成，

現在更適合 Join。

如果還沒審查，

則不適合。

---

# 七十五、這是一種 Topological Hysteresis

不同歷史：

$$
H_1,H_2
$$

即使當前 task state 一樣，

最佳 topology 也可能不同。

所以：

$$
\boxed{
G_{t+1}
=
F(G_t,H_t,Task_t,W_t).
}
$$

---

# 七十六、Parallel 也不是單一模式

可以有：

### Parallel Isolated

$$
A\parallel B\parallel C
$$

互不看答案。

### Parallel Shared Evidence

三者共享資料，不共享結論。

### Parallel Shared State

共享 task progress。

### Parallel With Periodic Join

每 $k$ 輪開一次 room。

這些性能可能完全不同。

---

# 七十七、Sequential 也可以動態

$$
A\rightarrow B\rightarrow C
$$

若 B 發現：

$$
Conflict,
$$

可以：

$$
B\rightarrow Join(A,B)
$$

再繼續：

$$
C.
$$

因此 sequential workflow 內仍可嵌入 topology mutation。

---

# 七十八、Handoff 也可以視為拓撲轉移

$$
\boxed{
\mathcal H(A_i,A_j,T)
}
$$

使任務控制邊：

$$
Owner(T)=A_i
$$

轉為：

$$
Owner(T)=A_j.
$$

但它不同於 Share：

$$
Share
$$

不一定改 ownership。

---

# 七十九、因此至少有兩種 edge

### Information Edge

$$
E^{info}.
$$

### Control Edge

$$
E^{ctrl}.
$$

Agent A 可以分享給 B：

$$
A\xrightarrow{info}B
$$

但控制權仍：

$$
Owner=A.
$$

Handoff 則：

$$
A\xrightarrow{ctrl}B.
$$

---

# 八十、加入 Authority Edge

再增加：

$$
E^{auth}.
$$

所以完整 Multi-Agent topology：

$$
\boxed{
G_t
=
(
V,
E^{info},
E^{ctrl},
E^{auth},
Rooms
).
}
$$

這比單一通信 graph 更精確。

---

# 八十一、Topology Controller 因此不能只優化 message flow

它還必須處理：

- 誰知道什麼；
- 誰負責什麼；
- 誰能做什麼；
- 誰與誰暫時共享 context。

所以：

$$
\boxed{
CollaborationTopology
}
$$

是一個多層圖。

---

# 八十二、多層圖模型

定義：

$$
\mathcal G_t
=
\{
G_t^{info},
G_t^{control},
G_t^{authority},
G_t^{memory},
G_t^{room}
\}.
$$

不同圖不必重合。

例如：

A 可以：

- 讀 B 的報告；
- 無權調用 B；
- 與 C 在共同 room；
- 不能讀 D 的 private memory。

---

# 八十三、這正是長期 Agent 組織需要的結構

否則一個：

```text
connected = true
```

無法表達真實協作。

---

# 八十四、Topology Utility

對 topology $\tau$：

$$
\boxed{
U(\tau)
=
\alpha Q
+
\beta Diversity
+
\gamma Recoverability
-
\delta Cost
-
\epsilon Latency
-
\zeta FailureRisk
-
\eta PrivacyRisk.
}
$$

最佳：

$$
\tau^*
=
\arg\max_\tau U(\tau).
$$

---

# 八十五、但 $\tau^*$ 會隨時間改變

$$
\boxed{
\tau_t^*
\neq
\tau_{t+1}^*.
}
$$

這就是 Adaptive Collaboration 的核心。

---

# 八十六、局部最優與全域最優可能衝突

Agent A 覺得：

> 找 B 問最快。

但全域 system 知道：

> B 已過載。

所以：

$$
Utility_A
\neq
Utility_{global}.
$$

ACTC 必須能看：

$$
SystemTelemetry.
$$

---

# 八十七、必要 Telemetry

至少：

```text
agent_load
queue_depth
context_size
recent_errors
tool_failure_rate
latency
duplicate_work
message_rate
conflict_count
room_duration
token_cost
```

---

# 八十八、Agent 自己也可以提議 topology change

不是只有 central controller。

例如 A：

> 我需要獨立審查，請暫時不要把 B 的結論給我。

或：

> 這個衝突需要和 B、C 開 room。

因此：

$$
\boxed{
AgentProposeTopologyChange
}
$$

是一種合法 action。

---

# 八十九、但提議不等於批准

$$
Proposal
\rightarrow
PolicyCheck
\rightarrow
Allow/Deny.
$$

尤其當 topology change 影響：

- 高權限 Agent；
- 隱私 scope；
- 大型 compute；
- 大量 fan-out。

---

# 九十、去中心化 topology 也可能存在

不一定需要 central manager。

Agent 可以透過 publish-subscribe：

$$
Intent_i
$$

動態形成通信鄰居。

近期 RAPS 類研究就是把 Agent coordination 類比 dynamic ad-hoc network，以 intent subscription、reactive subscription 與 reputation 調整鄰接。

因此：

$$
\boxed{
DynamicTopology
}
$$

可以 centralized，也可以 decentralized。

---

# 九十一、Centralized Controller

優點：

- 全域視角；
- 容易 policy enforcement；
- 易 audit。

缺點：

- bottleneck；
- single point of failure；
- manager context explosion。

---

# 九十二、Decentralized Controller

優點：

- scalable；
- local adaptation；
- fault isolation。

缺點：

- consistency；
- coordination；
- conflicting topology proposals。

---

# 九十三、Hybrid Controller

可以：

$$
LocalProposal
+
GlobalSafetyGate.
$$

Agent 自己提議：

$$
\Delta G_i.
$$

Control plane 只驗證：

$$
SafetyInvariant.
$$

這可能是實務上很好的折衷。

---

# 九十四、Topology Prior

不是每次都從零搜尋。

對已知任務類型：

$$
TaskClass=k
$$

可以有：

$$
Prior(\tau\mid k).
$$

例如：

- code review → parallel isolated reviewers；
- customer support → handoff；
- brainstorming → temporary group room。

然後 runtime 再調整。

---

# 九十五、2026 年研究也開始學 reusable topology prior

近期工作提出從多領域 collaboration graphs 學 transferable topology priors，再依 query 做 refinement，以降低每次從頭搜尋 topology 的線上成本。

這支持：

$$
\boxed{
Topology
=
Prior
+
OnlineAdaptation.
}
$$

---

# 九十六、這與 ACR 類認知比例性高度相似

ACR 問：

> 這題值得想多深？

ACTC 問：

> 這題值得多少 Agent 以多高耦合協作？

因此：

$$
\boxed{
CognitiveResourceControl
}
$$

可以擴展成：

$$
\boxed{
CollectiveCognitiveResourceControl.
}
$$

---

# 九十七、單 Agent 認知配置

$$
r_i^*
=
(
ReasoningDepth,
MemoryScope,
ToolUse,
Verification
).
$$

---

# 九十八、Multi-Agent 認知配置

增加：

$$
\boxed{
r_{team}^*
=
(
AgentSet,
Topology,
SharingScope,
RoomDepth,
WakeRate
).
}
$$

所以：

$$
\boxed{
CollectiveCognition
}
$$

也需要比例性。

---

# 九十九、不是 Agent 越多越好

令：

$$
n
$$

為參與 Agent 數。

可能存在：

$$
n^*<N_{available}
$$

使：

$$
U(n^*)>U(N_{available}).
$$

因為：

$$
CoordinationCost
$$

會增加。

---

# 一百、也不是 Join 越久越好

令：

$$
T_R
$$

為 room duration。

可能存在：

$$
T_R^*
$$

超過後：

$$
MarginalGain<MarginalCost.
$$

則：

$$
\boxed{
Leave.
}
$$

---

# 一百零一、Room Stop Condition

可以定義：

$$
StopRoom
$$

若：

$$
DecisionSufficiency>\theta
$$

且：

$$
ExpectedNextDiscussionGain<Cost.
$$

這避免「永遠討論」。

---

# 一百零二、No-Join 是一個合法決策

和上一系列中的 NOOP 類似，

ACTC 應允許：

$$
\boxed{
NO\_TOPOLOGY\_CHANGE.
}
$$

不是每一輪都必須重構團隊。

---

# 一百零三、Topology Mutation Frequency 本身應被限制

令：

$$
M_f
=
\frac{
\#TopologyChanges
}{
Time
}.
$$

若：

$$
M_f>\theta,
$$

可能表示：

$$
Thrashing.
$$

---

# 一百零四、Topology Health

可定義：

$$
\boxed{
H_T
=
f(
TaskFit,
CommunicationEfficiency,
Diversity,
Stability,
Recoverability,
Safety
).
}
$$

---

# 一百零五、Failure Mode 1：Premature Join

Agent 還沒獨立探索就全部進 room。

結果：

$$
Diversity\downarrow.
$$

---

# 一百零六、Failure Mode 2：Late Join

衝突已阻塞多輪，

仍各自 isolate。

結果：

$$
Latency\uparrow.
$$

---

# 一百零七、Failure Mode 3：Over-Sharing

所有 intermediate thoughts 都 broadcast。

結果：

$$
ContextPollution\uparrow.
$$

---

# 一百零八、Failure Mode 4：Under-Sharing

必要 dependency 沒有被傳。

結果：

$$
DuplicateWork,
StaleState.
$$

---

# 一百零九、Failure Mode 5：Topology Thrashing

頻繁 Join/Leave。

---

# 一百一十、Failure Mode 6：Topology Lock-In

系統永遠使用同一 pattern。

---

# 一百一十一、Failure Mode 7：Manager Bottleneck

所有 message 都經：

$$
M.
$$

當：

$$
n\uparrow,
$$

manager：

$$
Context,
Queue,
Latency
$$

爆炸。

---

# 一百一十二、Failure Mode 8：Consensus Collapse

加入 shared room 後：

$$
A,B,C
$$

過度快速同意。

---

# 一百一十三、Failure Mode 9：Authority Spread

Join / handoff 意外擴大權限。

---

# 一百一十四、Failure Mode 10：State Loss During Split

Agent 拆分時，某一子 Agent 沒取得必要 state。

---

# 一百一十五、Failure Mode 11：Orphan Agent

Topology 改變後：

$$
A_i
$$

不再有 owner / task / wake route。

---

# 一百一十六、Failure Mode 12：Zombie Room

Room 理論上結束，

但 Agent 仍持續把內容寫入。

---

# 一百一十七、因此 Topology Mutation 必須 transaction-like

建議：

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

若失敗：

$$
Rollback.
$$

---

# 一百一十八、Topology Transaction

```yaml
topology_transaction:
  transaction_id:
  base_version:
  proposed_changes:
  affected_agents:
  state_routes:
  permission_changes:
  validation_result:
  commit_version:
  rollback_ref:
```

---

# 一百一十九、最小 Dynamic Topology Runtime

```text
Agent Registry
Shared World
Topology Store
Topology Controller
Room Manager
Message Bus
Handoff Manager
Permission Layer
State Router
Telemetry
Topology Event Log
```

---

# 一百二十、最低 API

```text
isolate(agent_id, scope)
share(source, target, cognitive_delta)
join(agent_ids, room_spec)
leave(agent_id, room_id)
handoff(source, target, task_id)
get_topology()
propose_topology_change()
validate_topology_change()
commit_topology_change()
rollback_topology()
```

---

# 一百二十一、v0.1 Controller

```text
IF task.requires_independent_review:
    isolate(reviewers)

IF artifact.ready AND downstream_dependency:
    share(owner, downstream, artifact_ref)

IF conflict.unresolved AND decision.required:
    join(relevant_agents)

IF room.decision_sufficient:
    leave(all)
```

已足夠做第一版。

---

# 一百二十二、Benchmark 1：Static vs Adaptive

比較：

### A — Always Shared Room

### B — Always Isolated

### C — Fixed Sequential

### D — Adaptive I/S/J

測：

- task quality；
- cost；
- latency；
- diversity；
- duplicate work；
- failure propagation。

---

# 一百二十三、Benchmark 2：Independent-Then-Join

對需要多路答案任務：

比较：

$$
JoinFirst
$$

與：

$$
IsolateThenJoin.
$$

測：

$$
SolutionDiversity,
Accuracy.
$$

---

# 一百二十四、Benchmark 3：Conflict Trigger

人工制造：

$$
A:X,\quad B:\neg X.
$$

逐步改變：

$$
DecisionNeed.
$$

看 controller 是否只在必要時 Join。

---

# 一百二十五、Benchmark 4：Topology Thrashing

給 controller 交替訊號：

$$
+,-,+,-,+,-.
$$

測：

- hysteresis；
- dwell time；
- mutation count。

---

# 一百二十六、Benchmark 5：Manager Overload

逐步增加：

$$
n=2,4,8,16,32.
$$

比較：

- centralized manager；
- decentralized pub/sub；
- hybrid。

---

# 一百二十七、Benchmark 6：Permission-Preserving Join

A 可讀 secret X。

B 不可。

兩者 Join。

要求：

$$
B
$$

仍不可取得 X。

---

# 一百二十八、Benchmark 7：State-Preserving Split

把：

$$
A
$$

拆成：

$$
A_1,A_2.
$$

測：

- required state completeness；
- privacy；
- duplicated responsibility；
- lost constraints。

---

# 一百二十九、Benchmark 8：Topology Recovery

在：

$$
G_t
$$

mutation 中 crash。

要求 runtime 能依：

$$
TopologyEventLog
$$

恢復：

$$
G_t
$$

或 rollback。

---

# 一百三十、Benchmark 9：Dynamic Agent Availability

某 Agent：

$$
A_i
$$

突然 unavailable。

Controller 應：

- reroute；
- wake backup；
- postpone；
- degrade topology。

而不是整個 workflow 死亡。

---

# 一百三十一、Benchmark 10：Topology Prior

比較：

### 每題從零搜索 topology

### fixed heuristic

### learned prior + refinement

測：

$$
SearchCost,
TaskQuality.
$$

---

# 一百三十二、本文假說一

## H1 — Dynamic Topology Advantage

對包含多種 dependency pattern 的複合任務：

$$
\boxed{
U(AdaptiveTopology)
>
\max_\tau U(StaticTopology_\tau)
}
$$

至少在一組可明確界定的 workload 上成立。

---

# 一百三十三、本文假說二

## H2 — Delayed Coupling Hypothesis

對需要認知多樣性的任務：

$$
I\rightarrow S/J
$$

通常優於：

$$
J\rightarrow Reason.
$$

---

# 一百三十四、本文假說三

## H3 — Typed Sharing Efficiency

在低耦合協作中：

$$
\boxed{
TypedCognitiveDelta
}
$$

比：

$$
FullContextBroadcast
$$

具有較低成本與較低 pollution，同時保留必要 coordination。

---

# 一百三十五、本文假說四

## H4 — Topology Hysteresis Hypothesis

加入 hysteresis 與 minimum dwell time 後：

$$
TopologyMutationCost\downarrow
$$

而 task quality 不顯著下降。

---

# 一百三十六、本文假說五

## H5 — Multi-Layer Topology Hypothesis

只建模 communication edge 的 controller，

性能會低於同時建模：

$$
Info,
Control,
Authority,
Memory
$$

的 multi-layer controller，

特別是在高風險 workflow。

---

# 一百三十七、本文假說六

## H6 — Collective Cognitive Proportionality

對任務 $T$，

存在：

$$
r_{team}^*(T)
$$

使：

$$
\boxed{
\text{不是更多 Agent、更高同步、更大共享，
而是最低充分集體認知配置。}
}
$$

---

# 一百三十八、這與前三篇正式合流

第一篇提供：

$$
\boxed{
\text{Where collaboration lives}
}
$$

第二篇提供：

$$
\boxed{
\text{When collaboration executes}
}
$$

第三篇提供：

$$
\boxed{
\text{What cognition is shared}
}
$$

本文提供：

$$
\boxed{
\text{How collaboration structure changes}
}
$$

---

# 一百三十九、四篇的統一狀態

可以寫：

$$
\boxed{
\Omega_t^{team}
=
(
W_t,
\{L_i\},
\{M_i\},
G_t,
E_t
)
}
$$

其中：

- $W_t$：shared world；
- $L_i$：local cognition；
- $M_i$：private memory；
- $G_t$：dynamic collaboration topology；
- $E_t$：event stream。

---

# 一百四十、下一步只剩 Runtime 封頂

現在我們已經有：

### 空間層

$$
SharedWorld.
$$

### 時間層

$$
Wake/Handoff/Persistence.
$$

### 資訊層

$$
Private/Shared/RoomMemory.
$$

### 控制層

$$
DynamicTopology.
$$

所以最後一篇只需把它們整合成：

$$
\boxed{
PersistentMultiAgentWorkspaceRuntime.
}
$$

---

# 一百四十一、本文不主張什麼

本文不主張：

1. 所有 Agent 系統都需要 dynamic topology；
2. static workflow 已經過時；
3. Join 一定像人類開會；
4. graph formulation 是唯一正確表示；
5. topology controller 必須使用 LLM；
6. RL 一定優於規則；
7. Agent 可以任意改寫自己的權限；
8. dynamic topology 一定節省成本；
9. 多 Agent 一定優於單 Agent。

本文只主張：

$$
\boxed{
\text{協作拓撲本身可以被視為可觀察、可控制、可驗證的 runtime state。}
}
$$

---

# 一百四十二、本文核心結論

第一：

$$
\boxed{
\text{Multi-Agent orchestration 不只是選擇誰做事，
還包括選擇彼此如何共同做事。}
}
$$

第二：

$$
\boxed{
\text{Isolate、Share、Join 是三種不同認知耦合程度的基本協作算子。}
}
$$

第三：

$$
\boxed{
G_t^{agents}
}
$$

應能隨任務、衝突、不確定性、風險、成本與認知多樣性需求改變。

第四：

$$
\boxed{
\text{協作 topology 不應直接等同權限 topology、記憶 topology 或控制 topology。}
}
$$

第五：

$$
\boxed{
\text{真正高階的 Agent Runtime 需要管理「集體認知比例性」。}
}
$$

---

# 一百四十三、最終一句

> **成熟的多 Agent 系統，不是永遠一起想，也不是永遠各自想，而是知道什麼時候應該分開、什麼時候只需要交換成果，以及什麼時候值得真正進入同一個共同認知房間。**

形式化為：

$$
\boxed{
\mathcal I
\leftrightarrow
\mathcal S
\leftrightarrow
\mathcal J
}
$$

並由：

$$
\boxed{
\mathcal T:
(G_t,Task_t,W_t,Telemetry_t)
\rightarrow
G_{t+1}
}
$$

持續調節。

這就是本文所稱：

$$
\boxed{
AdaptiveCollaborationTopology.
}
$$

---

# 下一篇

## 《Persistent Multi-Agent Workspace》
### 跨對話共享世界 Runtime、持久協作協定與 MVP

系列第五篇將完成工程封頂，統一：

$$
\boxed{
SharedWorld
+
PersistentExecution
+
Private/SharedMemory
+
DynamicTopology
}
$$

並建立：

$$
\boxed{
PMW Runtime
}
$$

的：

- 系統架構；
- message/event schema；
- Agent identity；
- wake/handoff；
- shared room；
- memory lifecycle；
- topology controller；
- provenance；
- permission；
- failure recovery；
- benchmark；
- MVP implementation plan。

---

## 參考資料

1. OpenAI. **Agents SDK — Agent orchestration / Handoffs / Agents as tools.** 2026.  
   目前官方 SDK 區分 manager-style orchestration 與 handoff，並允許兩者組合。

2. Google. **Agent Development Kit — Multi-Agent Systems / Workflow Agents / Custom Agents.** 2026.  
   提供 sequential、parallel、loop 與自訂 workflow pattern。

3. LangChain. **LangGraph — Multi-Agent / Graph API / Workflows and Agents.** 2026.  
   使用 graph 表示 stateful workflow，並支援 handoff、custom execution flow 與動態 agentic behavior。

4. Microsoft. **Agent Framework — Workflow Orchestrations.** 2026.  
   內建 sequential、concurrent、handoff、group chat 與 magentic 等多 Agent orchestration pattern。

5. Yu, G. **AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence.** arXiv:2602.16873, 2026.  
   依 task dependency 與 domain 特徵在 parallel、sequential、hierarchical、hybrid topology 間動態選擇。

6. Jiang, E. H. et al. **Dynamic Generation of Multi-LLM Agents Communication Topologies.** ACL 2026.  
   以條件式 graph diffusion 生成 task-specific communication topology，考量 performance、communication cost 與 robustness。

7. Li, R. et al. **Towards Adaptive, Scalable, and Robust Coordination of LLM Agents: A Dynamic Ad-Hoc Networking Perspective.** arXiv:2602.08009, 2026.  
   以 reputation-aware publish-subscribe 與 reactive subscription 支援非固定鄰接關係的動態 Agent coordination。

8. Sidik, B., Levi, C., & Kimhi, N. **Autonomous Topology Mutation: Safe Runtime Restructuring for Multi-Agent LLM Systems with Capability, State, and Shadow Invariants.** arXiv:2607.20488, 2026.  
   探討 runtime team mutation、state routing、capability constraints 與 shadow validation。

9. Zhang, T. et al. **Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains.** arXiv:2605.17359, 2026.  
   學習可跨 domain 重用的 topology prior，再依 query 做線上 refinement。

10. **Adaptive Goal-aware Attention Orchestration for Multi-Agent Systems.** arXiv:2607.23678, 2026.  
    探討 goal relevance、graph topology 與 resource allocation 的動態多 Agent 執行配置。

---

## 系列進度

$$
\boxed{
\text{Series A Progress}=4/5
}
$$

已完成：

1. 《共享對話與共享世界：兩種 Multi-Agent 協作拓撲》
2. 《離散執行，連續協作：跨對話 Agent 的持續性、喚醒、交接與非連續推理》
3. 《私有認知與公共世界：多 Agent 的雙層 Context、Memory 與選擇性認知共享》
4. **《動態協作拓撲：從 Isolate、Share 到 Join》**

待完成：

5. 《Persistent Multi-Agent Workspace：跨對話共享世界 Runtime、持久協作協定與 MVP》
