# 共享對話與共享世界  
## 兩種 Multi-Agent 協作拓撲：從共同 Thread 到獨立認知空間與持久共享世界

**English Title:**  
*Shared Conversation and Shared World: Two Collaboration Topologies for Multi-Agent Systems*

**系列：**《跨對話智能協作與共享認知空間》第一篇  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**性質：** 公開理論論文／Agent 系統架構論  
**版本：** v0.1  
**日期：** 2026-08-08

---

## 摘要

目前多智能體系統通常被籠統描述為「多個 Agent 一起工作」，但這種說法掩蓋了一個重要的架構差異：

多個 Agent 究竟是**共享同一個對話上下文**，還是**各自保有獨立認知工作空間，只共享一個持久外部世界**？

本文提出兩種基本協作拓撲：

$$
\boxed{
\text{Shared-Conversation Multi-Agent}
}
$$

與：

$$
\boxed{
\text{Shared-World Multi-Agent}
}
$$

前者使多個 Agent 共同存在於一個 conversation／thread 中，透過同一條對話歷史、共同上下文與即時訊息進行協作；後者則允許每個 Agent 維持自己的 local context、memory、task state 與 reasoning history，只透過一個持久共享層交換訊息、事件、任務、狀態、產物與時間參照。

本文主張：

$$
\boxed{
\text{Shared Conversation}
\neq
\text{Shared World}
}
$$

而且兩者並非競爭性的替代方案，而是具有不同資訊耦合程度、故障隔離能力、上下文成本、認知獨立性與協作延遲的兩種基本 primitive。

在此基礎上，本文進一步提出：

$$
\boxed{
\text{Local Cognitive Space}
+
\text{Persistent Shared World}
+
\text{Optional Shared Room}
}
$$

作為未來長期 Multi-Agent Runtime 的三層架構。

其核心思想是：

> **智能體不需要共享整個認知內部，才能共享同一個工作世界。**

最後，本文提出 Context Coupling、Shared-State Coverage、Cognitive Independence、Coordination Latency 與 Failure Propagation 等可操作指標，為後續研究動態 Agent 協作拓撲、跨對話持續性與 Persistent Multi-Agent Workspace 建立形式基礎。

---

## 關鍵詞

Multi-Agent Systems、Agent Collaboration、Shared Workspace、Shared World、Conversation Topology、Persistent Agents、Cross-Conversation、Shared State、Agent Memory、Context Isolation、Agent Runtime

---

# 一、問題：所謂「多 Agent 一起工作」其實至少是兩件不同的事

2026 年的 Agent 系統已經開始從單一 chatbot 模式轉向：

$$
A_1,A_2,\ldots,A_n
$$

共同完成任務。

但「共同完成任務」至少可能表示兩種非常不同的情形。

第一種：

```text
                Shared Conversation
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      Agent A        Agent B        Agent C
```

三個 Agent 共同讀取同一條 thread。

第二種：

```text
        Agent A           Agent B           Agent C
           │                 │                 │
      Local Context      Local Context      Local Context
           │                 │                 │
           └──────────── Shared World ─────────┘
```

三者並沒有共同的完整 conversation context。

它們只共享：

- 公共訊息；
- 任務；
- 世界狀態；
- 事件；
- 文件；
- artifacts；
- 時間序列；
- provenance。

這兩者表面上都可以呈現：

> 「三個 AI 正在討論。」

但其資訊結構並不相同。

因此首先需要：

$$
\boxed{
\text{Multi-Agent Collaboration}
\not\Rightarrow
\text{Shared Conversation}
}
$$

---

# 二、第一種拓撲：Shared-Conversation Multi-Agent

本文將第一種模式稱為：

## Shared-Conversation Multi-Agent，SCMA

令：

$$
C_t
$$

表示時間 $t$ 的共享 conversation。

共有：

$$
A_1,A_2,\ldots,A_n
$$

個 Agent。

則其基本形式為：

$$
\boxed{
A_i
\leftrightarrow
C_t
\leftrightarrow
A_j
}
$$

對所有參與者而言，主要協作媒介都是：

$$
C_t
$$

。

換言之：

$$
Context_i(t)
\supseteq
C_t
$$

而通常：

$$
C_t
$$

構成每個 Agent 當前認知條件的重要部分。

---

## 2.1 典型形式

例如：

```text
Human:
請三個 Agent 分析這個問題。

Agent A:
我認為 X。

Agent B:
我不同意 A，理由是 Y。

Agent C:
A 與 B 的差異在於 Z。
```

所有訊息都在同一個 thread。

這種模式非常自然。

公開系統目前已經明確出現這種設計。例如 OpenAgents Workspace 把 workspace 定義為 Agent pool 的容器，而每個 thread 則是一個由指定 Agent 子集參與的 conversation；group thread 中還可以指定 master agent，再由其 `@mention` 其他 Agent。

---

# 三、SCMA 的主要優點

SCMA 最大的優勢是：

$$
\boxed{
\text{Communication Friction}\downarrow
}
$$

因為所有參與者都直接看到共同 thread。

不需要：

- 額外 retrieval；
- 狀態投影；
- message routing；
- shared-state reconstruction。

因此：

$$
Latency_{coordination}
$$

通常較低。

此外，人類也容易理解。

它很接近：

> 把所有人叫進同一間會議室。

---

## 3.1 公共語境天然一致

在理想情況：

$$
C_A=C_B=C_C=C
$$

因此 Agent A 說：

> 「剛才第二個方案。」

B 不需要額外查詢共享狀態，就能知道「第二個方案」是什麼。

這使：

$$
ReferenceResolution
$$

變得非常容易。

---

## 3.2 即時討論非常自然

共享 conversation 特別適合：

- brainstorming；
- rapid review；
- 即時辯論；
- 共同編輯；
- 短期小組決策。

因此它是一種：

$$
\boxed{
High-Coupling Collaboration
}
$$

。

---

# 四、SCMA 的限制：共同語境也是共同耦合

同一個優點，也構成它最大的限制。

假設 thread 中總共有 $n$ 個 Agent。

各 Agent 持續生成內容：

$$
m_i(t)
$$

則共享 conversation 的大小近似：

$$
|C_t|
\sim
\sum_{i=1}^{n}
m_i(t).
$$

當 Agent 數量與工作時間增加：

$$
|C_t|
\uparrow
$$

。

所有 Agent 都可能反覆承受這個共同歷史。

---

## 4.1 Context coupling

定義 Agent $i,j$ 的上下文耦合：

$$
\boxed{
\kappa_{ij}
=
\frac{
|Context_i\cap Context_j|
}{
|Context_i\cup Context_j|
}
}
$$

。

SCMA 通常具有：

$$
\kappa_{ij}\rightarrow1
$$

的傾向。

這代表協調容易，但同時表示：

$$
CognitiveIndependence\downarrow
$$

。

---

# 五、認知錨定問題

假設：

$$
A_1
$$

先提出強烈答案 $X$。

而：

$$
A_2
$$

原本如果獨立求解，可能得到 $Y$。

但在 SCMA 中：

$$
A_2
$$

首先讀到：

$$
X
$$

。

因此實際推理變成：

$$
P(Y\mid Problem,X)
$$

而不是：

$$
P(Y\mid Problem).
$$

所以：

$$
\boxed{
SharedContext
\rightarrow
CrossAgentAnchoring
}
$$

是合理風險。

這不代表共享 conversation 一定導致錯誤。

但對某些任務，例如：

- blind review；
- red teaming；
- independent replication；
- 多路證明搜尋；
- 預測集合；
- 對抗式推理；

過高的：

$$
\kappa
$$

反而可能降低系統價值。

---

# 六、第二種拓撲：Shared-World Multi-Agent

本文提出第二個基本形式：

## Shared-World Multi-Agent，SWMA

其中每一個 Agent：

$$
A_i
$$

都有自己的局部認知空間：

$$
L_i
$$

。

例如：

$$
L_i=
(
Context_i,
Memory_i,
TaskState_i,
Goal_i,
History_i
)
$$

。

但所有 Agent 共同連接：

$$
W
$$

——Persistent Shared World。

因此：

$$
\boxed{
L_i
\leftrightarrow
W
\leftrightarrow
L_j
}
$$

。

注意：

$$
L_i\neq L_j
$$

但：

$$
W_i=W_j=W
$$

。

---

# 七、Shared World 是什麼？

這裡的「World」不是物理宇宙。

它是工程上的共享事件—狀態空間：

$$
\boxed{
W=
(
M,E,S,T,A,P
)
}
$$

其中：

- $M$：Messages；
- $E$：Events；
- $S$：Shared State；
- $T$：Tasks / Temporal references；
- $A$：Artifacts；
- $P$：Provenance。

因此「共享時空」若作工程比喻，可以理解成：

$$
\boxed{
\text{Shared State Space}
+
\text{Shared Event Order}
}
$$

而不是物理學中的 spacetime。

---

# 八、SWMA 最關鍵的不同：Agent 不需要知道整個共享世界

即使：

$$
|W|
$$

極大，Agent $i$ 也不需要：

$$
Context_i=W.
$$

它只需要取得：

$$
\boxed{
\pi_i(W,Q_i)
}
$$

其中：

$$
\pi_i
$$

是一個 projection／retrieval operator。

所以：

$$
Context_i
=
L_i
+
\pi_i(W,Q_i).
$$

這與：

$$
Context_i=C_{shared}
$$

有本質差異。

---

# 九、共享世界不是共享腦袋

這帶出本文最核心的命題之一：

$$
\boxed{
SharedWorld
\not\Rightarrow
SharedCognition
}
$$

。

Agent A 可以知道：

> Agent B 已提交 artifact $X$。

但不需要知道：

> Agent B 為產生 $X$ 所經歷的全部 context 與局部工作史。

因此：

$$
\boxed{
\text{Result Sharing}
\neq
\text{Cognitive-State Sharing}
}
$$

。

---

# 十、這其實更接近很多現實組織

一個工程團隊的工程師不會把自己的全部腦內活動同步給其他人。

他們共同使用的是：

- Git；
- Issue tracker；
- 文件；
- Slack；
- database；
- project state。

也就是：

$$
Human_i
+
LocalCognition_i
+
SharedWorld.
$$

Agent 系統也可能自然演化成：

$$
Agent_i
+
LocalCognition_i
+
SharedWorld.
$$

這不代表 Agent 必須模仿人類社會。

更可能只是：

> **對有限而彼此獨立的工作單元而言，局部狀態加共享外部狀態是一種高效的資訊架構。**

---

# 十一、目前公開技術已經出現這種方向的部分構件

公開 Agent infrastructure 已經逐漸把「conversation」與「persistent state」分離。

例如 Microsoft Agent Framework 的工作流文件指出，workflow 中每個 Agent 預設可擁有自己的 thread，而 Agent threads 又能跨 workflow runs 持久保存。

LangGraph 的 checkpoint architecture 同樣把 thread 定義為一系列持久 checkpoint；不同 thread 可以維持不同狀態，而 `thread_id` 是恢復與持久化的主要索引。

Google 對 A2A 的公開定位則強調，Agent 不應只是 stateless tools，而需要能以共同語言合作、協調與 handoff。

這些技術並不等於本文的完整 SWMA 模型。

但它們表明：

$$
\boxed{
AgentIdentity,
Conversation,
State,
Execution
}
$$

正在逐步解耦。

---

# 十二、SCMA 與 SWMA 的真正差異不是 UI

一個 SWMA 系統完全可以做成看起來像聊天室。

反過來，一個 SCMA 也可以做成複雜 dashboard。

所以：

$$
\boxed{
Topology\neq UI
}
$$

。

真正差異是：

> **Agent 在產生下一步行動前，到底共享的是同一份認知歷史，還是只共享一個外部公共世界？**

---

# 十三、形式化比較

對 SCMA：

$$
Context_i(t)
=
C_t+L_i^{small}.
$$

因此：

$$
Context_i\cap Context_j
$$

通常很大。

對 SWMA：

$$
Context_i(t)
=
L_i(t)
+
\pi_i(W_t).
$$

所以可能：

$$
Context_i\cap Context_j
\ll
Context_i\cup Context_j.
$$

但同時：

$$
Access_i(W)
\approx
Access_j(W)
$$

在權限允許範圍內成立。

因此：

$$
\boxed{
ContextCoupling
\neq
WorldCoupling
}
$$

。

這是一個非常重要的區分。

---

# 十四、Shared-State Coverage

定義 Agent $i$ 對共享世界的有效可達率：

$$
\boxed{
\sigma_i
=
\frac{
|W_i^{reachable}|
}{
|W^{authorized}|
}
}
$$

。

SCMA 可以具有：

$$
\kappa\approx1
$$

但未必有巨大：

$$
\sigma
$$

。

反過來 SWMA 可以：

$$
\kappa\ll1
$$

但：

$$
\sigma\approx1.
$$

也就是：

> Agent 的腦內上下文彼此非常不同，但它們都能按需查到同一個公共世界。

---

# 十五、Cognitive Independence

可把簡化的認知獨立度定義成：

$$
\boxed{
I_{ij}=1-\kappa_{ij}.
}
$$

則：

### Shared Conversation

$$
I_{ij}\downarrow
$$

。

### Shared World

$$
I_{ij}\uparrow
$$

。

因此不同 topology 適合不同任務。

---

# 十六、不是所有工作都應該最大獨立

過高：

$$
I
$$

也會有代價。

例如：

$$
A
$$

剛剛解決一個關鍵問題，

但：

$$
B,C
$$

因為沒有讀取共享結果，又重複做兩次。

因此：

$$
I\uparrow
$$

可能導致：

$$
DuplicateWork\uparrow.
$$

所以真正目標不是：

$$
\max I
$$

。

而是：

$$
\boxed{
\text{Optimal Cognitive Coupling}
}
$$

。

---

# 十七、Shared World 的主要優勢之一：局部工作記憶可以保持有限

假設整個共享世界：

$$
|W_t|\rightarrow large.
$$

每個 Agent 仍然只需：

$$
|\pi_i(W_t)|\le B_i
$$

其中：

$$
B_i
$$

是 Agent 的 active-context budget。

因此：

$$
\boxed{
|W_t|\uparrow
\not\Rightarrow
|Context_i|\uparrow
}
$$

。

這對長期 Agent 特別重要。

---

# 十八、長期工作與「對話肥大」

若所有工作都存在：

$$
C_{shared}
$$

中，

時間越長：

$$
|C_{shared}|\uparrow.
$$

最後只能：

- truncate；
- summarize；
- compact；
- retrieve；
- archive。

一旦如此，shared conversation 本身就開始逐漸變成：

$$
SharedWorld
+
Projection.
$$

也就是：

> **超長對話發展到最後，往往會被迫重新發明某種外部記憶與狀態層。**

---

# 十九、Persistent Shared World 的另一個優勢：conversation 可以死亡

假設 Agent A 的目前 session：

$$
C_A^{(1)}
$$

結束。

稍後產生：

$$
C_A^{(2)}.
$$

只要：

$$
W
$$

仍然存在，

則：

$$
C_A^{(1)}
\rightarrow
W
\rightarrow
C_A^{(2)}.
$$

因此：

$$
\boxed{
ConversationEnd
\neq
CollaborationEnd.
}
$$

。

---

# 二十、這也是「跨對話」真正重要的地方

跨對話不是：

> 把聊天記錄從 A 複製到 B。

更一般的形式是：

$$
\boxed{
C_i
\rightarrow
W
\rightarrow
C_j.
}
$$

所以：

$$
Conversation
$$

變成 temporary view。

而：

$$
W
$$

才是 collaboration continuity carrier。

---

# 二十一、離散執行也能形成連續協作

Agent 不需要：

$$
Run(t)=1,\quad\forall t.
$$

它完全可以：

$$
Run
\rightarrow
Sleep
\rightarrow
Wake
\rightarrow
Run.
$$

只要共享狀態持續存在。

因此：

$$
\boxed{
ContinuousCollaboration
\not\Rightarrow
ContinuousInference.
}
$$

這將是本系列第二篇的主要問題。

---

# 二十二、SWMA 並不是免費午餐

Shared world 最大的問題是：

$$
\boxed{
StateConsistency
}
$$

。

當：

$$
A_1,A_2,\ldots,A_n
$$

同時讀寫：

$$
W
$$

時，就會出現典型分散式系統問題：

- race condition；
- stale read；
- duplicate update；
- conflicting writes；
- version mismatch；
- causal-order ambiguity。

這已經不是純理論風險。

2026 年的 STORM 工作就是針對多 Agent 同時操作 shared workspace 時的一致視圖與寫入衝突提出 state-oriented management。

S-Bus 更直接研究多 Agent 共享可變 natural-language state 時的 structural race conditions，並提出 read-set reconstruction 與部分因果一致性機制。

---

# 二十三、共享世界必須是「有治理的世界」

因此不能只做：

```text
shared_memory.json
```

然後讓所有 Agent 任意修改。

至少需要：

$$
W=
(
State,
Version,
EventLog,
Authority,
Provenance,
ConflictPolicy
)
$$

。

寫入應具有：

$$
write=
(
actor,
source,
version,
causation,
authority
)
$$

。

否則 Agent A 的推論可能被 Agent B 誤認為：

> 使用者明確確認的事實。

---

# 二十四、Shared World 中的 shared memory 也不能等於 collective truth

必須區分：

$$
Claim
$$

$$
Hypothesis
$$

$$
Observation
$$

$$
Decision
$$

$$
VerifiedFact
$$

。

因此：

$$
\boxed{
Shared
\neq
True.
}
$$

共享只代表：

> 它進入共同可達資訊空間。

---

# 二十五、Failure Propagation

令：

$$
F_i
$$

表示 Agent $i$ 產生錯誤。

在高度共享 conversation：

$$
F_i
\rightarrow
C
\rightarrow
A_j
$$

錯誤可能透過共同上下文快速傳播。

在 shared-world 架構：

$$
F_i
\rightarrow
Candidate(W)
$$

還可以經過：

$$
Verify
\rightarrow
Promote
$$

才成為穩定共享知識。

因此可定義：

$$
\boxed{
P_{ij}^{failure}
=
P(
F_j
\mid
F_i
)
}
$$

。

理想的 Shared World 不追求：

$$
P_{ij}^{failure}=0
$$

而是降低無驗證的錯誤級聯。

---

# 二十六、Artifact 比聊天內容更重要的情況

在長期工程中，

Agent A 可能花一小時產生：

```text
architecture.md
```

Agent B 真正需要的可能只是：

$$
Artifact_A
$$

而不是：

$$
Conversation_A^{1h}.
$$

因此：

$$
\boxed{
ArtifactTransfer
\ll
ContextTransfer
}
$$

在資訊量上往往成立。

近期的 Agent Team Work Zone 工作也從長期 coding team 的角度指出，Agent process 停止、compaction 與工作狀態遺失會造成 persistent-team 問題，因此把每個 Agent 的重要工作狀態保存到持久 workspace，並允許 Agent 互相傳文件。

---

# 二十七、這帶出一個新的協作原則

$$
\boxed{
\text{共享成果，
而非預設共享全部認知歷史。}
}
$$

這不是資訊封閉。

而是：

$$
\boxed{
Selective Cognitive Disclosure
}
$$

。

---

# 二十八、第三種形式其實會自然出現：Hybrid

SCMA 與 SWMA 不必二選一。

可以存在：

$$
\boxed{
HybridMultiAgent
}
$$

：

```text
             Persistent Shared World
                     │
      ┌──────────────┼──────────────┐
      │              │              │
    Agent A        Agent B        Agent C
      │              │              │
    Local A        Local B        Local C
      │              │              │
      └──────── Shared Room ────────┘
                 when needed
```

---

# 二十九、Shared Room

令：

$$
R_k
$$

表示暫時共享 conversation。

則：

$$
R_k
\subset
W
$$

或者更準確：

$$
R_k
\leftrightarrow
W.
$$

Agent 平時保持獨立：

$$
A\parallel B\parallel C.
$$

需要高速協調時：

$$
Join(A,B,C,R_k).
$$

討論完成：

$$
R_k
\rightarrow
Decision/Artifact
\rightarrow
W.
$$

然後：

$$
Exit(R_k).
$$

---

# 三十、一個很簡單的現實類比

Shared World 相當於：

> 公司。

Shared Room 相當於：

> 會議室。

Agent 的 local context：

> 個人工作桌。

所以：

$$
\boxed{
\text{會議結束}
\neq
\text{公司消失}.
}
$$

同理：

$$
\boxed{
ConversationEnd
\neq
WorkspaceEnd.
}
$$

---

# 三十一、三個基本協作算子

從兩種 topology，可以抽出三個操作。

## 31.1 Isolate

$$
\mathcal I(A_i)
$$

讓 Agent 保持局部認知獨立。

---

## 31.2 Share

$$
\mathcal S(A_i,W,x)
$$

把：

$$
x
$$

發布到 shared world。

---

## 31.3 Join

$$
\mathcal J(A_1,\ldots,A_k)
$$

建立短期共同 conversation。

因此：

$$
\boxed{
\{\mathcal I,\mathcal S,\mathcal J\}
}
$$

可能構成 Multi-Agent Collaboration 的三個基礎 primitive。

完整動態 topology 將於本系列第四篇處理。

---

# 三十二、不同 topology 適合不同工作

### Shared Conversation 適合：

- 即時討論；
- brainstorm；
- 快速 review；
- 共同決策；
- 短期合作。

### Shared World 適合：

- 長期研究；
- 多工作流並行；
- blind review；
- independent reasoning；
- asynchronous agents；
- cross-session collaboration；
- persistent project state。

### Hybrid 適合：

$$
\boxed{
\text{大多數真正長期的 Agent 組織。}
}
$$

---

# 三十三、四個值得測量的基本變數

除了：

$$
\kappa
$$

Context Coupling，

本文提出至少另外四項。

---

## 33.1 Shared-State Coverage

$$
\sigma
$$

Agent 可有效取得多少共享世界。

---

## 33.2 Cognitive Independence

$$
I
$$

Agent 局部推理相互獨立的程度。

---

## 33.3 Coordination Latency

$$
L_c
$$

從一個 Agent 發現資訊，到另一個需要該資訊的 Agent 有效取得它所需時間。

---

## 33.4 Failure Propagation

$$
P_f
$$

一個 Agent 錯誤導致其他 Agent 繼承錯誤的概率。

---

# 三十四、因此 Multi-Agent topology 是一個多目標最佳化問題

不存在單一：

$$
Topology^*
$$

適合所有任務。

更合理的是：

$$
\boxed{
T^*
=
\arg\max_T
U(
Coordination,
Independence,
Cost,
Latency,
Reliability,
Recoverability
)
}
$$

。

這意味著：

> 未來高階 Agent Runtime 可能不只選擇「哪個 Agent 做任務」，還要選擇「Agent 應該以什麼關係工作」。

---

# 三十五、對「共享時空」概念的嚴格限制

本文使用「共享世界」或「共享時空」時，不主張任何物理學含義。

其最低工程定義是：

$$
\boxed{
SharedWorld
=
SharedState
+
SharedEventStructure
}
$$

如果再加入共同時間參照：

$$
\boxed{
SharedCognitiveSpacetime
=
StateSpace
+
EventOrder
+
TemporalReference
}
$$

。

這只是分散式 Agent 協作的形式語言。

---

# 三十六、時間順序與因果順序也必須分離

設：

$$
e_1,e_2
$$

兩事件。

時間戳可能滿足：

$$
t(e_1)<t(e_2)
$$

但並不能因此推出：

$$
e_1\rightarrow e_2.
$$

所以 shared world 最好同時具有：

$$
TemporalOrder
$$

與：

$$
CausalReference.
$$

例如：

```yaml
event:
  id:
  actor:
  timestamp:
  parent_event:
  caused_by:
  state_version:
```

。

---

# 三十七、身份不能依賴顯示名稱

長期 Agent 系統中：

$$
DisplayName(A)=DisplayName(B)
$$

完全可能。

因此：

$$
\boxed{
AgentIdentity
\neq
DisplayName.
}
$$

最低應有：

$$
AgentID
$$

與：

$$
InstanceID.
$$

必要時再加入：

$$
RoleID,\ TaskID,\ SessionID.
$$

---

# 三十八、Conversation ID 也可能降級成 View ID

如果 collaboration continuity 存在於：

$$
W
$$

而不是：

$$
C
$$

那麼未來：

$$
ConversationID
$$

很可能只是：

$$
\boxed{
ViewID
}
$$

。

真正重要的持續標識會逐漸變成：

$$
AgentID
$$

$$
ThreadID
$$

$$
TaskID
$$

$$
ArtifactID
$$

$$
StateVersion
$$

$$
EventID.
$$

---

# 三十九、從「聊天室」轉向「工作世界」

Chatbot 時代：

$$
\boxed{
Conversation
=
PrimaryStateContainer.
}
$$

Agent 時代可能逐漸變成：

$$
\boxed{
Conversation
\subset
Workspace.
}
$$

再進一步：

$$
\boxed{
Workspace
\subset
PersistentSharedWorld.
}
$$

。

---

# 四十、一個更一般的 Multi-Agent 模型

可以將 Agent $A_i$ 定義為：

$$
A_i=
(
L_i,
M_i,
G_i,
P_i,
R_i
)
$$

其中：

- $L_i$：local context；
- $M_i$：private memory；
- $G_i$：goal；
- $P_i$：policy；
- $R_i$：runtime capability。

共享世界：

$$
W=
(
E,S,T,K,F,H
)
$$

其中：

- $E$：events；
- $S$：shared states；
- $T$：tasks；
- $K$：shared knowledge；
- $F$：files/artifacts；
- $H$：shared history。

則：

$$
\boxed{
A_i:
(L_i,\pi_i(W))
\rightarrow
(a_i,\Delta W_i).
}
$$

Agent 讀取共享世界的一部分，

做出局部行動，

再把：

$$
\Delta W_i
$$

提交回世界。

---

# 四十一、Shared World 因而是一個協作介面，而不是大腦

$$
\boxed{
W
\neq
\sum_i Mind_i.
}
$$

它比較像：

$$
\boxed{
W
=
CoordinationSurface.
}
$$

。

這個區分非常重要。

否則「共享記憶」很容易被誤解成：

> 所有 Agent 共享全部內在狀態。

那反而會破壞模組化與隔離性。

---

# 四十二、從分散式系統看，這並不是完全陌生的東西

從計算機科學角度看，SWMA 與許多既有概念有親緣：

- blackboard architecture；
- tuple space；
- actor systems；
- event sourcing；
- shared databases；
- distributed logs；
- pub/sub；
- message bus。

真正新的問題不一定是「共享狀態」本身。

而是：

$$
\boxed{
\text{具有生成、推理、記憶與自主決策能力的 Agent，
如何在其中持續存在。}
}
$$

。

---

# 四十三、這會產生傳統分散式系統沒有完全處理的新問題

例如：

### 語義衝突

兩個 Agent 寫的不是：

```text
x = 5
x = 6
```

而是：

> 「方案 A 已經失敗。」

與：

> 「方案 A 仍然值得繼續。」

這不是 byte-level conflict。

而是：

$$
\boxed{
SemanticConflict.
}
$$

---

# 四十四、自然語言 shared state 的困難

傳統 database 可以：

$$
Lock(row).
$$

但：

> 「這項研究基本完成。」

到底能不能 lock？

Agent 可能：

- 語義不同；
- 信心不同；
- 時間點不同；
- 證據不同。

因此未來 shared world 需要：

$$
\boxed{
TypedEpistemicState.
}
$$

例如：

```yaml
claim:
  content:
  status: hypothesis
  confidence:
  source:
  valid_at:
  supersedes:
```

。

---

# 四十五、共享世界不是為了讓所有 Agent 變得一樣

恰恰相反。

它最大的價值可能就是允許：

$$
\boxed{
Difference
+
Coordination.
}
$$

。

如果所有 Agent 最後都讀一樣的 context、持有一樣的 memory、得到一樣的 state：

$$
A_1\approx A_2\approx A_3,
$$

那麼增加 Agent 數量的價值可能迅速下降。

---

# 四十六、真正有價值的是「可協作的差異」

$$
\boxed{
UsefulMultiAgent
=
Diversity
\times
Coordination.
}
$$

若：

$$
Diversity=0
$$

只是重複。

若：

$$
Coordination=0
$$

只是彼此無關。

因此：

$$
Diversity>0
$$

且：

$$
Coordination>0
$$

才產生真正多智能體價值。

---

# 四十七、這也是為什麼兩種 topology 都不應消失

SCMA 最大化：

$$
Coordination.
$$

SWMA 更容易保留：

$$
Diversity.
$$

Hybrid 則試圖動態平衡：

$$
\boxed{
Diversity
\leftrightarrow
Coordination.
}
$$

。

---

# 四十八、假說一：任務時間越長，Shared World 的價值越高

提出：

## H1 — Temporal Persistence Hypothesis

隨任務持續時間：

$$
T\uparrow
$$

如果 conversation history 不斷成長，

則：

$$
Utility(SWMA)-Utility(SCMA)
$$

平均會增加。

原因包括：

- context cost；
- compaction loss；
- restart；
- artifact accumulation；
- task branching。

這可以實驗檢驗。

---

# 四十九、假說二：獨立驗證任務偏好較低 Context Coupling

## H2 — Independent Verification Hypothesis

對需要：

- 多路獨立證明；
- blind review；
- adversarial evaluation；

的任務，

存在：

$$
\kappa^*<1
$$

使：

$$
Accuracy(\kappa^*)
>
Accuracy(\kappa=1).
$$

也就是：

> 完全共享所有先前答案不一定是最佳多 Agent 策略。

---

# 五十、假說三：協作拓撲應當可動態切換

## H3 — Adaptive Topology Hypothesis

對複合長期任務：

$$
T=T_1+T_2+\cdots+T_m
$$

最優 topology 可能隨子任務改變：

$$
Topology_t
=
f(Task_t,Conflict_t,Uncertainty_t,Cost_t).
$$

因此：

$$
\boxed{
StaticTopology
<
AdaptiveTopology
}
$$

在適當 benchmark 上應可被驗證。

---

# 五十一、最小 Benchmark

可以設計三組系統。

### Baseline A — Single Shared Thread

$$
SCMA.
$$

### Baseline B — Independent Agents Only

$$
A_1\parallel A_2\parallel A_3
$$

但沒有 persistent shared world。

### System C — Shared World

$$
SWMA.
$$

### System D — Hybrid

$$
SWMA+TemporarySharedRoom.
$$

---

# 五十二、測量項目

至少包括：

$$
Q=\text{task quality}
$$

$$
C=\text{token/compute cost}
$$

$$
L=\text{latency}
$$

$$
D=\text{duplicate work}
$$

$$
F=\text{failure propagation}
$$

$$
R=\text{restart recoverability}
$$

$$
I=\text{independent solution diversity}.
$$

---

# 五十三、本文不主張什麼

本文不主張：

1. Shared World 一定優於 Shared Conversation；
2. 多 Agent 一定優於單 Agent；
3. Agent 必須模仿人類組織；
4. 所有 Agent 必須具有 private memory；
5. 共享世界等同共享意識；
6. conversation 將會消失；
7. shared state 能自動解決語義一致性。

本文只主張：

$$
\boxed{
\text{SharedConversation 與 SharedWorld 是兩種不同的協作拓撲。}
}
$$

以及：

$$
\boxed{
\text{它們具有可區分、可測量、可組合的工程性質。}
}
$$

---

# 五十四、從 2026 年公開狀態看，兩條路線正在靠近

目前可以看到一些明顯趨勢。

OpenAgents 已經把 workspace 與 conversation thread 明確分開：workspace 是 Agent pool 的容器，而 thread 是實際 conversation。

Microsoft Agent Framework 已允許工作流中的 Agent 各自擁有 persistent thread。

LangGraph 把 persistent state、checkpoint 與 thread identity 正式變成 runtime primitive。

而 STORM、S-Bus、ATWZ 等近期研究則分別開始處理：

- shared workspace state consistency；
- concurrent Agent conflicts；
- long-lived Agent team state persistence。

這表示真正的問題已經逐漸從：

> 「Agent 能不能彼此呼叫？」

轉向：

> **「多個長期存在、彼此有獨立狀態的 Agent，應該共享多少認知，又應該共享多少世界？」**

---

# 五十五、最終三層架構

本文最後提出：

$$
\boxed{
\text{Private Cognitive Space}
}
$$

$$
+
$$

$$
\boxed{
\text{Persistent Shared World}
}
$$

$$
+
$$

$$
\boxed{
\text{Ephemeral Shared Conversation}
}
$$

。

即：

$$
\boxed{
PC
+
SW
+
SC.
}
$$

三者分別負責：

### Private Cognitive Space

保持：

- 專注；
- 獨立推理；
- local memory；
- failure isolation。

### Persistent Shared World

保持：

- task continuity；
- artifact continuity；
- event history；
- shared state；
- provenance。

### Ephemeral Shared Conversation

處理：

- 高速協調；
- 爭議；
- brainstorming；
- 共同決策。

---

# 五十六、核心結論

Multi-Agent 系統長期以來容易把：

$$
\text{多個 Agent}
$$

與：

$$
\text{同一個對話}
$$

綁在一起。

但兩者沒有邏輯上的必然關係。

更一般的形式是：

$$
\boxed{
\{A_1,\ldots,A_n\}
+
\{L_1,\ldots,L_n\}
+
W.
}
$$

其中：

$$
L_i
$$

彼此保持差異，

而：

$$
W
$$

提供共同現實。

因此：

$$
\boxed{
\text{Multi-Agent Collaboration}
=
\text{Local Cognition}
+
\text{Selective Sharing}
+
\text{Common World}.
}
$$

---

# 五十七、最後命題

本文可以壓縮為一句：

$$
\boxed{
\text{智能體不需要活在同一個對話裡，
才能活在同一個工作世界裡。}
}
$$

甚至更進一步：

$$
\boxed{
\text{共享認知不是協作的前提；
共享一個可持續、可追溯、可操作的世界就可能足夠。}
}
$$

因此，未來 Multi-Agent Runtime 真正需要解決的，不只是：

> 「誰回答下一句？」

而是：

$$
\boxed{
\text{此刻應共享多少認知、多少狀態，
以及採用哪一種協作拓撲？}
}
$$

這也構成下一篇的入口。

---

# 下一篇

## 《離散執行，連續協作》
### 跨對話 Agent 的持續性、喚醒、交接與非連續推理

下一篇將正式處理：

$$
\boxed{
ContinuousCollaboration
\not\Rightarrow
ContinuousInference
}
$$

並分析：

$$
Run
\rightarrow
Sleep
\rightarrow
Wake
\rightarrow
Handoff
\rightarrow
Resume
$$

為什麼仍然可以在觀察層形成一個持續存在的 Agent 協作過程。

---

## 參考資料

OpenAgents. *What is OpenAgents Workspace?* Updated July 27, 2026.

OpenAgents. *OpenAgents Overview — The Collaboration OS for AI Agents.* Updated July 27, 2026.

Google Developers Blog. *How A2A is Building a World of Collaborative Agents.* June 18, 2026.

Microsoft Learn. *Microsoft Agent Framework Workflows — State.* 2026.

LangChain. *LangGraph Checkpointing Reference.* 2026.

Liu, M. et al. *Multi-agent Collaboration with State Management (STORM).* arXiv:2605.20563, 2026.

Khan, S. *S-Bus: Automatic Read-Set Reconstruction for Multi-Agent LLM State Coordination.* arXiv:2605.17076, 2026.

Wang, S. *Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Coding Agent Teams.* arXiv:2607.22917, 2026.