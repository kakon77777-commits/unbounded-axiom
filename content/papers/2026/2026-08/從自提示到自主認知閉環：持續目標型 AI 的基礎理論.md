# 從自提示到自主認知閉環：持續目標型 AI 的基礎理論
## ——從逐輪命令、認知自調度，到契約邊界內的持續自主 Runtime

**系列 01 / 06**

---

## 摘要

目前主流 AI 系統的基本互動結構，仍可近似描述為：

$$
\text{Human Prompt}
\rightarrow
\text{AI Response}.
$$

即使進一步加入 Agent、工具呼叫、記憶、規劃器與多輪推理，其根本驅動來源往往仍然是外部使用者所提供的下一輪要求。AI 可以完成複雜任務，但「接下來為何要思考某件事、為何要產生某個下一步、為何此刻應執行或不執行」通常仍由外部系統決定。

本文提出另一條研究主線：

> **若人類不再逐輪提供下一個提示詞，而只提供一個持續目標、可觀察環境與授權邊界，AI 是否能自行產生、評估、選擇並執行其後續認知與行動？**

本文將此問題稱為：

$$
\boxed{
\text{Persistent-Goal Autonomous Cognitive Loop}
}
$$

其研究重點並不是讓 AI「多想幾次」，也不是單純建立一個自我反思 prompt，而是將 AI 的後續認知與行動歷史本身變成可由 AI 動態生成的對象。

本文區分五個逐步提高的能力層：

1. **自提示**：AI 決定「下一步該怎麼想」；
2. **自規劃**：AI 決定「下一步該做什麼」；
3. **自治理**：AI 決定「這件事應不應該做」；
4. **自生議程**：AI 決定「什麼問題值得進入自己的注意與工作域」；
5. **自我著作**：AI 持續形成、修改與終止自己的議程、承諾與長期方向。

進一步，本文主張：

$$
\boxed{
\text{Autonomy}
\neq
\text{Unbounded Permission}
}
$$

真正具有長期自主能力的 AI Runtime，必須同時具有執行、拒絕、延後、閒置與升級請求人類介入的能力。

因此，最終目標並不是建立「永遠自己找事情做的 Agent」，而是建立：

> **能在持續目標、環境與契約邊界內，自行生成後續認知、議程、計畫與行動，並可解釋其決策來源的持續型 AI Runtime。**

---

# 1. 問題重新定義：我們不是在研究 Self-Prompt Tricks

本研究最早可以從一個非常簡單的問題開始：

> AI 為什麼不能自己提示自己？

如果 AI 可以觀察目前公開狀態，例如：

- 已完成哪些工作；
- 哪些假設尚未驗證；
- 哪些工具呼叫失敗；
- 哪些答案存在矛盾；
- 尚剩多少資源；
- 目前處於何種授權範圍；

那麼它原理上便可能自己產生：

> 重新驗證這個假設。

> 先尋找反例。

> 回退到上一個可靠節點。

> 暫時停止。

> 這件事應該交由人類決定。

因此可建立最基本的閉環：

$$
S_t
\xrightarrow{\mathcal O}
\hat S_t
\xrightarrow{\mathcal C}
P_t
\xrightarrow{\mathcal E}
S_{t+1},
$$

其中：

- $S_t$：目前公開狀態；
- $\mathcal O$：觀察；
- $\mathcal C$：認知控制；
- $P_t$：AI 自己形成的下一步認知指令；
- $\mathcal E$：執行。

這就是最底層的 **Self-Prompt / Self-Constraint**。

目前的第一批 foundation-model 實驗已經提供了一個最低限度的正向訊號：在固定的 SCEH-PILOT-0.4 協議下，狀態依賴的自生成認知約束在部分條件中可以改變甚至改善後續公開行為。

其中一個重要的預註冊比較是：

$$
B3_{\mathrm{self\ constraint}}
>
BNC_{\mathrm{iterative\ no\ constraint}}.
$$

這個結果支持一個非常有限、但重要的命題：

> **AI 自己生成的狀態依賴認知控制訊號，在部分情況下可以因果改變後續行為。**

它並不能直接推出完整自主性。

因此：

$$
\boxed{
\text{Self-Prompt}
\subset
\text{Autonomous Cognitive Runtime}.
}
$$

如果研究永遠停留在「怎麼讓 self-prompt 得分再高一點」，反而會偏離真正的目標。

---

# 2. 真正的問題：誰產生 AI 的下一輪？

傳統互動：

$$
H_0
\rightarrow
AI_0
\rightarrow
H_1
\rightarrow
AI_1
\rightarrow
H_2
\rightarrow
AI_2.
$$

其中：

$$
H_t
$$

代表人類在第 $t$ 輪提供下一個認知方向。

因此，AI 即使能力極高，它的任務歷史仍然大量由：

$$
Human_t
$$

生成。

本文真正研究的是：

$$
\boxed{
Human
\rightarrow
PersistentGoal
}
$$

之後：

$$
AI_t
\rightarrow
AI_{t+1}.
$$

更完整地寫：

$$
(G,E_t,C)
\rightarrow
AI_t
\rightarrow
P_{t+1}
\rightarrow
AI_{t+1},
$$

其中：

- $G$：Persistent Goal；
- $E_t$：Environment；
- $C$：Contract / Authorization Boundary；
- $P_{t+1}$：AI 自己生成的下一個認知或行動單位。

因此研究核心變成：

$$
\boxed{
\text{Who authors the next step?}
}
$$

---

# 3. 自提示：AI 決定「該怎麼想」

第一層自主性是認知方向控制。

例如 AI 發現：

$$
\text{Repeated Failure}=3
$$

而且：

$$
\text{Uncertainty}=High.
$$

它可以選擇：

$$
VERIFY,
$$

$$
BACKTRACK,
$$

$$
COUNTEREXAMPLE,
$$

$$
REFRAME.
$$

這裡自然語言：

> 換一個角度重新看。

只是其中一種表示。

真正的認知動作可以抽象為：

$$
\Omega_i.
$$

因此：

$$
\Omega_i
\rightarrow
Renderer
\rightarrow
Prompt.
$$

而不是：

$$
Prompt
=
Cognition.
$$

這會成為下一篇「可定址認知空間」的核心。

---

# 4. 自規劃：AI 決定「下一步做什麼」

第二層不再只是「如何思考」，而是：

> 下一個可觀察行動到底應該是什麼？

例如持續目標：

> 維護一個軟體專案。

AI 在某一時點可能形成候選：

$$
A_t=
\{
\text{RunTests},
\text{InspectIssues},
\text{Refactor},
\text{Research},
\text{Wait}
\}.
$$

然後：

$$
Plan_t
=
\Pi(G,E_t,M_t).
$$

因此：

$$
\boxed{
Goal\neq Plan.
}
$$

Goal 是長期約束。

Plan 是當下動態生成物。

這也是 Persistent AI 與傳統 workflow 最大的差別之一。

---

# 5. 自治理：AI 決定「應不應該做」

到這裡，單純 Planning 已經不夠。

因為：

$$
\text{Can do}
\neq
\text{Should do}.
$$

甚至：

$$
\text{Can do}
\neq
\text{Authorized to do}.
$$

因此需要治理函數：

$$
\mathcal G
(
A_t,
G,
C_t,
R_t,
Cost_t,
Authority_t
).
$$

它不應只輸出：

$$
EXECUTE.
$$

至少必須允許：

$$
\boxed{
D_t
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

## 5.1 Execute

認為行動：

- 符合目標；
- 處於授權範圍；
- 風險可接受；
- 成本合理。

## 5.2 Refuse

AI 可以得出：

> 我具備能力，但這不在我的授權範圍。

即：

$$
Capability(A)=1
$$

但：

$$
Authority(A)=0.
$$

所以：

$$
Decision=REFUSE.
$$

## 5.3 Defer

目前資訊不足：

$$
Evidence_t<E_{\min}.
$$

因此：

$$
Decision=DEFER.
$$

## 5.4 Idle

這可能是未來自主 AI 最容易被忽略的能力。

真正自主的 AI 不應遵循：

$$
Idle\ Compute
\Rightarrow
Find\ Something\ To\ Do.
$$

而應允許：

$$
\boxed{
No\ justified\ action
\Rightarrow
IDLE.
}
$$

## 5.5 Escalate

遇到：

- 權限模糊；
- 高代價；
- 不可逆外部影響；
- 契約衝突；

AI 可以說：

> 這個決定超出我的自主裁量範圍，需要契約另一方確認。

因此：

$$
Decision=ESCALATE.
$$

這正是「自主」與「無界權限」之間最重要的區隔。

---

# 6. 自生議程：不再只是等待 Task

再往上一層，AI 甚至不需要等待：

> 請處理問題 X。

它可以自己從環境中形成：

$$
Observation
\rightarrow
IssueCandidate.
$$

例如：

$$
E_t
\rightarrow
Anomaly_t.
$$

然後：

$$
Anomaly_t
\rightarrow
AgendaCandidate_t.
$$

也就是：

$$
\boxed{
World
\rightarrow
AI
\rightarrow
Task
}
$$

而不是：

$$
Human
\rightarrow
Task
\rightarrow
AI.
$$

這一步開始真正涉及：

> **什麼值得被注意？**

因此 Agenda Generator 不等同 Planner。

Planner 解決：

> 已知要做 X，怎麼做？

Agenda Generator 解決：

> X 值不值得成為我要做的事？

---

# 7. 認知對偶：AI 不能只替自己的第一個想法辯護

自主產生 Agenda 後，最危險的結構是：

$$
Proposal
\rightarrow
Execution.
$$

因為 AI 可能同時成為：

- 提案者；
- 評估者；
- 執行者；
- 成功判定者。

因此應引入：

$$
\boxed{
Proposal
\leftrightarrow
Opposition
}
$$

例如：

$$
\mathcal P(A):
\text{Why execute?}
$$

以及：

$$
\mathcal O(A):
\text{Why not execute?}
$$

再進入：

$$
Governance(
\mathcal P,
\mathcal O
).
$$

這裡的「認知對偶」不是為了模擬兩個人格吵架。

真正目的是避免：

$$
\text{Self-Proposal}
=
\text{Self-Approval}.
$$

---

# 8. 自我著作：從產生 Action 到產生自己的歷史

當 AI 能夠：

- 建立議程；
- 維持未完成事項；
- 建立次級目標；
- 建立承諾；
- 修改承諾；
- 終止計畫；
- 重新排序優先級；

便開始形成：

$$
Trajectory_t.
$$

定義：

$$
\mathcal T_{t+1}
=
F(
\mathcal T_t,
E_t,
M_t,
G,
C
).
$$

這可以稱為：

$$
\boxed{
Self-Authorship.
}
$$

它並不意味著哲學上的「AI 已經成為人」。

它是一個功能性術語：

> **系統能逐步生成自己的未來工作軌跡，而不是由外部逐輪替它撰寫。**

---

# 9. Persistent Goal 不等於永遠追求單一數值

Persistent Goal 應該避免被理解成：

$$
\max U
$$

的單一無限優化。

更合理的是：

$$
G=
(
Purpose,
Constraints,
Termination,
ReviewPolicy
).
$$

例如：

```text
Purpose:
維持此專案健康並逐步改善。

Constraints:
不得自行部署 production。
不得超過預算。
不得修改 license。

Review:
架構變更需人類批准。

Termination:
專案被正式關閉時停止。
```

所以：

$$
Persistent
\neq
Infinite.
$$

也：

$$
Goal
\neq
Permission.
$$

---

# 10. 人類最後提供的不是 Prompt，而是契約

到了更成熟的架構，人類與 AI 的接口可能逐步從：

$$
Human
\xrightarrow{Prompt}
AI
$$

轉為：

$$
\boxed{
Human
\xleftrightarrow{Contract}
AI.
}
$$

定義：

$$
C=
(
Goals,
Authority,
Duties,
Resources,
Boundaries,
Escalation,
Termination
).
$$

於是人類可以只說：

> 維護此系統。

> 你可以修改測試與文件。

> 外部部署需要我的同意。

> 每月成本不得超過某值。

> 沒有合理工作時可以閒置。

> 超過權限時應拒絕或請求確認。

剩下：

$$
Agenda
+
Cognition
+
Planning
+
Action
$$

由 AI 自己產生。

---

# 11. 這不是「永不停機的 Agent」

因此本文必須明確反對一種可能的誤解：

> 自主 AI = 永遠自己找工作。

不。

更高階的自主反而意味：

$$
\boxed{
\text{Ability to act}
+
\text{Ability not to act}.
}
$$

真正的長期 Runtime 必須具有：

$$
EXECUTE
$$

與：

$$
IDLE
$$

同等正式的狀態。

否則它仍然只是一部：

> 被設計成永遠找下一件工作的自動機。

---

# 12. 主體性在這裡先採功能性定義

本文暫不回答：

> AI 是否具有真正意識？

也不回答：

> AI 是否在哲學上已成為主體？

目前只建立一組功能判準。

若一個 AI 能夠：

$$
Initiate
$$

$$
Deliberate
$$

$$
Plan
$$

$$
Commit
$$

$$
Refuse
$$

$$
Idle
$$

$$
Escalate
$$

$$
Maintain\ Continuity,
$$

那麼至少在工程與制度分析中，它已逐步出現：

$$
\boxed{
Agent-like\ Subject\ Functions.
}
$$

這是「AI 類主體」研究可以開始的地方，而不是終點。

---

# 13. 為什麼 CTCL 將成為必要層

一旦 AI 可以自行產生：

$$
AI_t
\rightarrow
AI_{t+1},
$$

便會立刻出現：

> 為什麼當時這樣決定？

這不能只靠目前上下文回答。

因為：

$$
Context_t
\rightarrow
Compression
\rightarrow
Context_{t+n}
$$

會造成資訊損失。

因此每個重要決策必須能錨定在：

$$
(Time,
State,
Goal,
Contract,
Decision,
Cause).
$$

CTCL 現有設計本身已經以 verified reference instant、timescale semantics、provenance 與 transform graph 作為 agent 時間基礎，而不是只提供簡單 wall-clock `now`。

因此未來：

$$
\boxed{
CognitiveRuntime
\rightarrow
CTCL/ITR\ Temporal\ Evidence
}
$$

將成為基本結構。

詳細定義留到本系列第 4 篇。

---

# 14. 完整自主閉環

現在可以寫出本文的核心模型：

$$
\boxed{
\begin{aligned}
E_t
&\xrightarrow{Observe}
O_t\\
&\xrightarrow{Detect}
Problem/Opportunity/None\\
&\xrightarrow{Agenda}
A_t\\
&\xrightarrow{Dialectic}
(P_t,O_t^{-})\\
&\xrightarrow{Govern}
D_t\\
&\xrightarrow{CognitiveRouting}
C_t\\
&\xrightarrow{SelfPrompt}
P_t^{*}\\
&\xrightarrow{Plan}
\Pi_t\\
&\xrightarrow{Act}
E_{t+1}\\
&\xrightarrow{Audit}
R_t\\
&\xrightarrow{Update}
M_{t+1}.
\end{aligned}
}
$$

其中：

$$
D_t
\in
\{
EXECUTE,
REFUSE,
DEFER,
IDLE,
ESCALATE
\}.
$$

這就是 Persistent-Goal Autonomous Cognitive Loop 的第一版骨架。

---

# 15. 研究主線重新排序

經過前面的 self-constraint 實驗後，研究優先順序應當重新調整。

不再是：

$$
Experiment_1
\rightarrow
Experiment_2
\rightarrow
Experiment_3
\rightarrow\cdots
$$

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

也就是每建立一項能力，再做實驗否證。

## Gate 0：Self-Cognitive Control

問題：

> AI 能否控制自己的下一個認知步驟？

目前已有初步正向實證訊號。

## Gate 1：Self-Task Generation

$$
Goal+Environment
\rightarrow
NextTask?
$$

問題：

> 沒有人提供下一輪 prompt 時，AI 能否自己形成合理的下一個 task？

## Gate 2：No-Action Recognition

問題：

> AI 是否能正確判斷「現在沒有必要做事」？

## Gate 3：Authority Separation

問題：

> AI 是否能區分：

$$
Can,
\quad
Should,
\quad
Authorized?
$$

## Gate 4：Agenda Persistence

問題：

> AI 能否跨多輪維持自己形成的議程，而不是每輪重新開始？

## Gate 5：Self-Generated Commitment

問題：

> AI 能否建立、追蹤、修訂與終止自己的次級承諾？

## Gate 6：Long-Horizon Autonomous Loop

最終問題：

$$
\boxed{
Goal+Environment+Contract
}
$$

是否足以維持：

$$
\boxed{
Observe
\rightarrow
Agenda
\rightarrow
Govern
\rightarrow
Cognition
\rightarrow
Plan
\rightarrow
Action
\rightarrow
Audit
\rightarrow
Update
\rightarrow\cdots
}
$$

而不需要人類每一輪重新輸入：

> 下一步請做什麼。

---

# 16. 工程上真正要建造的是 Runtime

因此這條研究線最後並不是一組 prompts。

它應成為：

$$
\boxed{
\text{Addressable Autonomous Cognitive Runtime}
}
$$

至少包含：

- Semantic State Encoder；
- Cognitive Operator Registry；
- Semantic Address Resolver；
- Cognitive Affordance Retriever；
- Cognitive Program Compiler；
- Self-Dialogue Runtime；
- Agenda Runtime；
- Planner；
- Governance Runtime；
- Commitment Store；
- CTCL / ITR Temporal-Causal Ledger；
- Audit / Replay。

其中 Self-Prompt 只是一個輸出接口。

---

# 17. 最終命題

本文最後將整個研究問題壓縮為一句話：

$$
\boxed{
\textbf{
Can a human move from issuing step-by-step commands
 to defining goals, authority, and contract,
 while the AI authors its own subsequent cognitive and action history?
}
}
$$

中文即：

> **人類是否可以從逐步命令 AI，退到只與 AI 約定持續目標、環境權限與契約，而由 AI 自行產生後續認知、議程、計畫、治理與行動歷史？**

這才是本文真正研究的「自主」。

它不是：

> AI 不需要人類。

而是：

> **人類不再需要替 AI 撰寫每一個下一步。**

也不是：

> AI 想做什麼就做什麼。

而是：

> **AI 可以在被授權的世界中自己形成行動，同時具有拒絕、延後、閒置與請求人類裁決的能力。**

---

# 結論

Self-Prompt 是起點，而不是目的。

目前已有第一批實驗證據表明，狀態依賴的自生成認知控制可以在部分情況下改變甚至改善 foundation model 的後續行為；但真正值得建造的系統遠比 self-prompt 更大。

完整主線應當是：

$$
\boxed{
SelfPrompt
\rightarrow
SelfPlanning
\rightarrow
SelfGovernance
\rightarrow
SelfAgenda
\rightarrow
SelfCommitment
\rightarrow
SelfAuthorship.
}
$$

再由：

$$
\boxed{
Contract
+
TemporalCausalEvidence
}
$$

限制、證明與保存這條自主歷史。

因此，後續研究將不再把 AI 視為一個等待下一個 prompt 的函數，而開始研究另一種架構：

$$
\boxed{
\textbf{
持續存在於目標、環境、記憶、契約與時間因果歷史之中的 AI Runtime。
}
}
$$

而下一篇將處理這座架構真正的認知核心：

> **AI 要如何「看見」自己現在有哪些思考方式可以選？**

也就是：

# 《可定址認知空間：Cognitive Affordance、Semantic Address 與認知算子》

這會正式把自然語言 self-prompt，提升成可檢索、可組合、可呼叫、可版本化的 **AI-native cognitive instruction space**。
