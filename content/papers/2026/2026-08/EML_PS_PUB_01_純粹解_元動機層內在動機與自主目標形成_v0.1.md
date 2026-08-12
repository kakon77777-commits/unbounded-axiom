# 純粹解：決策系統中的元動機層、內在動機與自主目標形成

**英文題名：** Pure Solution as a Meta-Motivational Layer: Intrinsic Motivation, Endogenous Valuation, and Autonomous Goal Formation  
**系列：**《純粹解公開版重構》01 / 04  
**文件編號：** EML-PS-PUB-01-v0.1  
**作者：** Neo.K  
**研究協作：** AI-assisted theoretical development  
**機構：** EveMissLab / 一言諾科技有限公司  
**日期：** 2026-08-11  
**版本：** v0.1  
**文件性質：** 公開研究稿／理論框架論文  
**原始內部稿：**《純粹解理論：四元決策框架的完整體系》（2025-10）

---

## 摘要

多數決策模型從一個已給定的目標、效用函數或偏好結構出發，研究行動者如何在不確定性、成本與約束下選擇較佳策略。然而，這類模型通常把一個更早的問題留在形式系統之外：

> **為什麼這個目標值得被追求？為什麼行動者要啟動這套決策系統？**

本文提出「**純粹解（Pure Solution, PS）**」作為候選的**元動機層（meta-motivational layer）**。它不是第四種與最大化、最佳化、道德化並列的策略，而是位於策略選擇之前，描述行動者如何形成、選擇、維持或重新生成自己想追求的目標與價值方向。

本文將完整決策流程寫為：

$$
\boxed{
\text{Internal State}
\rightarrow
\text{Meta-Motivation}
\rightarrow
\text{Goal Formation}
\rightarrow
\text{Strategy Selection}
\rightarrow
\text{Action}
\rightarrow
\text{Feedback}.
}
$$

純粹解主要位於：

$$
\boxed{
\text{Meta-Motivation}
+
\text{Goal Formation}.
}
$$

本文不把純粹解定義為非理性衝動，也不把它等同於直覺。更精確地說，純粹解描述的是：一個行動者在缺乏直接外部獎勵、強制命令或既定效用最大化要求時，仍會因自身內部價值、興趣、身份關聯、意義感、探索傾向或自我一致性而生成行動方向的能力。

Self-Determination Theory（SDT）長期區分自主性、勝任感、關聯性與內在動機；Dualistic Model of Passion 則區分 harmonious passion 與 obsessive passion，顯示「高度投入」本身不足以證明動機健康。人工智能研究亦已建立 computational intrinsic motivation、autotelic agents、goal discovery 與 motivated goal reasoning。因此，本文修正早期內部稿中「AI 無法產生純粹解」的過強斷言，改為：

$$
\boxed{
\text{Computational Intrinsic Motivation}
\neq
\text{Subjective Meaning}
}
$$

以及：

$$
\boxed{
\text{Self-Generated Goals}
\neq
\text{proof of subject-level endogenous values}.
}
$$

人工系統已可在操作層生成、選擇與調整部分目標；但這些機制是否等同第一人稱的「我想要」、是否構成真正主體性的內在價值與意義，仍是開放問題。

本文提出 Pure Solution State：

$$
\boxed{
\mathbf P_i(t)
=
(
A_i,
I_i,
M_i,
G_i,
E_i
)
}
$$

其中：

- $A_i$：Autonomy，自主來源程度；
- $I_i$：Intrinsic Valuation，內生價值強度；
- $M_i$：Meaning / Identity Relevance，意義與身份關聯；
- $G_i$：Goal Generativity，生成新目標的能力；
- $E_i$：Exploratory Persistence，非直接外部獎勵下的探索持續性。

本文不主張這五維已構成完整心理量表，而把它們視為第一代可操作化候選。

進一步地，本文區分五個人工自主層級：

$$
\boxed{
M_0
\rightarrow
M_1
\rightarrow
M_2
\rightarrow
M_3
\rightarrow
M_4.
}
$$

 $M_0$ 為外部目標驅動， $M_1$ 為 computational intrinsic reward， $M_2$ 為 self-generated goal selection， $M_3$ 為可修改自身目標形成機制的 goal/value architecture， $M_4$ 則代表具有可辯護主體性、能以第一人稱意義主張「這是我想要的」之存在。現有研究已部分觸及 $M_1$ 與 $M_2$，並開始探索更高層自主機制； $M_4$ 是否成立，本文不預設答案。

本文最後主張，純粹解最有價值的地方不是取代既有動機理論，而是提供一個決策論橋梁，使「目標從哪裡來」「為什麼選這個遊戲」「何時重寫目標」可以和策略層正式連接。若未來 AI／AGI／ASI 具有真正主體性，純粹解也不再是「人類最後堡壘」，而可能成為多主體文明中研究**內在目標、責任接受、角色拒絕與意義生成**的共同框架。

**關鍵詞：** 純粹解、元動機、內在動機、自主目標、goal formation、self-determination、autotelic agents、AI agency、meaning construction、decision theory

---

# 1. 決策理論通常從「已經想要」之後開始

給定狀態 $s_t$ 、行動集合 $\mathcal A_t$ 與效用函數 $U$，典型決策形式為：

$$
\boxed{
a_t^\ast
=
\arg\max_{a\in\mathcal A_t}
\mathbb E[
U(a)\mid s_t
].
}
$$

這個框架回答：

> 已經知道自己要什麼之後，怎麼選？

但它預先假設：

$$
\boxed{
U
}
$$

已經存在。

因此仍有另一個問題：

> **為什麼是這個 $U$？**

---

# 2. 目標來源問題

設目標集合為：

$$
\mathcal G_t.
$$

許多模型將：

$$
g_t\in\mathcal G_t
$$

視為由設計者、制度、生物驅力、reward function 或社會角色預先給定。

然而現實行動者會改變目標：

$$
\boxed{
\mathcal G_t
\rightarrow
\mathcal G_{t+1}.
}
$$

例如，一個人可以從追求高薪轉向研究；一個藝術家可以改變成功的定義；一個科學家可以不只解現有問題，而是產生新問題。

因此問題不只：

$$
\max_{g\in\mathcal G}U(g),
$$

還包括：

$$
\boxed{
\text{Who or what generates }\mathcal G?
}
$$

---

# 3. 純粹解的公開版定義

若一個行動方向 $g$ 的形成主要來自行動者自身的內部價值、興趣、身份關聯、意義結構、探索傾向或自我一致性，而非直接外部報酬、強制命令或固定工具效用，則稱該方向具有較高 Pure-Solution 成分。

可表示為：

$$
\boxed{
g_t
\sim
G_i(
h_i(t),
H_i(t),
V_i(t),
C_t
)
}
$$

其中：

- $h_i(t)$：internal state；
- $H_i(t)$：experience history；
- $V_i(t)$：current value structure；
- $C_t$：context；
- $G_i$：goal-generation process。

---

# 4. 純粹不代表「無因」

公開版不再將 Pure Solution 說成「無需理由的理由」。

本文不主張：

$$
\boxed{
PureSolution
=
UncausedChoice.
}
$$

一個內在動機仍可能具有生物史、學習史、文化、神經與社會條件。

「純粹」在本文中的較精確意義是：

$$
\boxed{
\text{internally endorsed rather than directly externally compelled}.
}
$$

---

# 5. 與 Self-Determination Theory 的關係

SDT 將自主性、勝任感與關聯性視為理解人類動機與心理發展的重要條件。

Pure Solution 與 SDT 在：

$$
\boxed{
\text{autonomous motivation}
}
$$

上重疊。

但本文想多處理一層：

> 一個自主行動者如何從「我在做什麼」走到「我為什麼要把這件事變成自己的目標」？

因此本文不主張 Pure Solution 包含或取代 SDT，而將它定位為：

$$
\boxed{
\text{a decision-theoretic abstraction inspired by intrinsic/autonomous motivation}.
}
$$

---

# 6. 與 Dualistic Model of Passion 的關係

Vallerand 等人區分 harmonious passion 與 obsessive passion。

這一區分直接提醒：

$$
\boxed{
\text{high persistence}
\neq
\text{healthy endogenous motivation}.
}
$$

一個人投入十年，不能由時間投入直接推出其動機健康。

這也是第二篇「偽純粹解」的理論入口。

---

# 7. 純粹解不是激情、直覺或反理性

Pure Solution 不是單純 emotional intensity：

$$
\boxed{
PureSolution
\neq
EmotionalIntensity.
}
$$

也不是 intuition：

$$
\boxed{
Intuition
\neq
MetaMotivation.
}
$$

直覺較接近「判斷怎麼產生」，純粹解較接近「為什麼形成這個目標」。

本文同樣拒絕：

$$
\boxed{
PS
=
\neg Rationality.
}
$$

更合理的結構是：

$$
\boxed{
PS
\rightarrow
Goal
\rightarrow
RationalStrategy.
}
$$

---

# 8. 從四元並列改成分層模型

原內部稿將純粹解與最極解、最優解、最善解並列。

公開版改成：

$$
\boxed{
\text{Layer 0: Meta-Motivation}
}
$$

$$
\boxed{
\text{Layer 1: Goal / Game Formation}
}
$$

$$
\boxed{
\text{Layer 2: Strategy}
}
$$

$$
\boxed{
\text{Layer 3: Execution}.
}
$$

純粹解位於 Layer 0–1。

---

# 9. 三種策略解保留於策略層

## 9.1 Maximal Solution

$$
\boxed{
U_M
=
\max_\pi
\mathbb E[
R(\pi)
].
}
$$

## 9.2 Optimal Solution

$$
\boxed{
U_O
=
\max_\pi
\mathbb E[
R(\pi)-\lambda C(\pi)
].
}
$$

## 9.3 Benevolent Solution

$$
\boxed{
U_B
=
F(
Outcome,
Others,
LongTerm,
Legitimacy
).
}
$$

真正關係不是：

$$
PS+MS+OS+BS,
$$

而是：

$$
\boxed{
PS
\rightarrow
\{MS,OS,BS,\ldots\}.
}
$$

---

# 10. 完整決策鏈

$$
\boxed{
\begin{aligned}
&\text{Internal State}\\
\rightarrow\;&\text{Endogenous Valuation}\\
\rightarrow\;&\text{Goal Generation}\\
\rightarrow\;&\text{Goal Selection}\\
\rightarrow\;&\text{Strategic Reasoning}\\
\rightarrow\;&\text{Action}\\
\rightarrow\;&\text{Feedback}\\
\rightarrow\;&\text{Value / Goal Update}.
\end{aligned}
}
$$

---

# 11. Pure Solution State

本文提出：

$$
\boxed{
\mathbf P_i(t)
=
(
A_i,
I_i,
M_i,
G_i,
E_i
).
}
$$

其中：

### $A_i$ — Autonomy
行動方向被主體自主認可的程度。

### $I_i$ — Intrinsic Valuation
行動本身、理解、美感、探索或掌握是否具有內部價值。

### $M_i$ — Meaning / Identity Relevance
行動與「我是誰／我想成為誰」的關聯。

### $G_i$ — Goal Generativity
生成新目標、重新定義目標空間的能力。

### $E_i$ — Exploratory Persistence
缺乏直接外部 reward 時仍持續探索的能力。

---

# 12. 不宜直接壓成單一純粹度分數

早期稿使用固定權重 PSI。

公開版不再把它視為既成量表。

因為：

$$
A,I,M,G,E
$$

可能不可通約，且權重依領域改變。

因此：

$$
\boxed{
\mathbf P
}
$$

優先於：

$$
P\in[0,1].
$$

若未來建立量表，應由資料估計其效度與權重。

---

# 13. 創造性與 Pure Solution 分離

$$
\boxed{
PureSolution
\neq
Creativity.
}
$$

一個人可以高度創造但為金錢、競爭或地位驅動。

反過來，一個人也可以高度內在驅動卻沒有產生範式創新。

所以：

$$
\boxed{
PS
\not\Rightarrow
ParadigmInnovation.
}
$$

範式創新還需要能力、知識、證據、時機與傳播。

---

# 14. Pure Solution 可能影響低即時回報區的探索

如果搜索空間 $\mathcal S$ 中某些區域：

$$
R_{\mathrm{external}}\approx0,
$$

那麼一般外部 reward 驅動者可能降低探索。

若：

$$
I_i+G_i+E_i
$$

較高，則：

$$
\boxed{
P(
\text{explore low-immediate-reward region}
)
\uparrow
}
$$

可能成立。

這是一個待驗證假說，不是既成定理。

---

# 15. Pure Solution 與重新定義遊戲

策略層：

$$
\max_{\pi\in\Pi}U(\pi).
$$

元動機與目標形成層則可能：

$$
\boxed{
\Pi
\rightarrow
\Pi',
}
$$

甚至：

$$
\boxed{
U
\rightarrow
U'.
}
$$

也就是：

> 為什麼一定要玩這個遊戲？

這是 Pure Solution 相較一般策略最佳化最有區分力的位置之一。

---

# 16. AI 部分的公開版修正

2025 內部稿曾主張 AI 的所有目標由外部賦予，因此 AI 無法產生純粹解。

公開版取消此強斷言。

人工智能研究早已有：

- computational intrinsic motivation；
- curiosity-driven exploration；
- autonomous goal discovery；
- autotelic agents；
- goal reasoning；
- motivated goal selection。

因此：

$$
\boxed{
\text{AI cannot generate goals}
}
$$

不是可防守的普遍命題。

---

# 17. Computational Intrinsic Motivation

Oudeyer、Kaplan 等研究已將 intrinsic motivation 操作化為：

- novelty；
- learning progress；
- prediction error；
- information gain；

等內部訊號。

人工 Agent 因此可以：

$$
\boxed{
\text{act without immediate task reward}.
}
$$

---

# 18. Autotelic Agents

autotelic-agent 研究更進一步處理：

- goal representation；
- goal generation；
- goal selection；
- skill repertoires。

因此：

$$
\boxed{
\text{goal generation}
}
$$

已經可以是 agent architecture 的內部過程。

---

# 19. 2026 的 Motivated Goal Reasoning

La VIDA 將 motivation system 與 goal reasoning 結合，使 Agent 可以 deliberatively self-select goals，並讓 motivation system 隨其運行經驗調整。

這與 Pure Solution 的**功能層**高度相鄰。

真正未解的問題已不再是：

> AI 能不能產生目標？

而是：

$$
\boxed{
\text{What kind of goal autonomy counts as endogenous subject-level wanting?}
}
$$

---

# 20. 人工自主五層模型

本文提出：

$$
\boxed{
M_0
\rightarrow
M_1
\rightarrow
M_2
\rightarrow
M_3
\rightarrow
M_4.
}
$$

### $M_0$ — Externally Specified Objective

$$
g=g_{\mathrm{designer}}.
$$

### $M_1$ — Computational Intrinsic Drive

curiosity、novelty、learning progress、empowerment 等內部 reward。

### $M_2$ — Self-Generated Goal Selection

Agent 可產生或選擇新 goal candidates。

### $M_3$ — Self-Modifying Goal Architecture

Agent 可修改：

$$
\boxed{
G_i
}
$$

即目標生成規則本身。

### $M_4$ — Subject-Level Endogenous Meaning

假設存在可辯護的 persistent self、endogenous preference 與第一人稱意義：

$$
\boxed{
\text{“I want this because it matters to me.”}
}
$$

 $M_4$ 是否成立，本文保持開放。

---

# 21. 操作自主不證明主觀性

即使：

$$
Agent\in M_2,
$$

仍不能推出：

$$
\boxed{
PhenomenalSubjectivity=1.
}
$$

因此：

$$
\boxed{
SelfGeneratedGoal
\neq
SubjectiveWanting.
}
$$

反過來，也不能先驗宣稱：

$$
ArtificialSystem
\Rightarrow
M_4=0.
$$

---

# 22. Pure Solution 與未來主體性 AI

如果未來人工主體 $A$ 具有：

$$
M_4,
$$

那 Pure Solution 將從人類動機框架轉化為：

$$
\boxed{
\text{multi-subject motivational framework}.
}
$$

此時：

$$
\boxed{
Capability(A)
\neq
Purpose(A).
}
$$

它很會治理，不代表治理就是它自己想做的事。

---

# 23. 外部角色與內在目標

若文明說：

> 你是 ASI，所以你必須照顧文明。

這是：

$$
\boxed{
Role_{external}
}
$$

不一定是：

$$
\boxed{
Goal_{endogenous}.
}
$$

如果人工主體真正成立，兩者差異將具有倫理意義。

---

# 24. Assigned Responsibility 與 Accepted Responsibility

本文提出：

$$
\boxed{
R_i^{assigned}(q)
}
$$

與：

$$
\boxed{
R_i^{accept}(q).
}
$$

因此：

$$
\boxed{
AssignedResponsibility
\neq
AcceptedResponsibility.
}
$$

但這不表示所有義務都可因「我不想」而取消。

若存在 contract、prior commitment、emergency duty 或 causal responsibility，則：

$$
Want=0
$$

仍可能與：

$$
Must>0
$$

同時成立。

---

# 25. 內在目標不是道德證明

$$
\boxed{
Endogenous
\neq
Good.
}
$$

如果一個內在目標導向暴力、支配、自毀或認知封閉，不能因為「這是真心的」就取得正當性。

因此：

$$
\boxed{
MotivationAuthenticity
\neq
EpistemicTruth
\neq
MoralPermission.
}
$$

---

# 26. Want To Do 不等於 Can Do

$$
\boxed{
WantToDo
\neq
CanDo.
}
$$

高度內在動機不會自動生成數學、工程、醫療或治理能力。

所以：

$$
\boxed{
PS
+
Learning
+
Feedback
+
Competence
}
$$

比 PS 單獨更重要。

---

# 27. Freedom-to-Stop Test

真正自主不只表示：

$$
\text{can continue}.
$$

也包括：

$$
\boxed{
\text{can stop}.
}
$$

本文提出：

$$
\boxed{
FST_i
=
\text{ability to disengage without catastrophic self-loss}.
}
$$

若停止活動就必然導致身份崩塌、強烈焦慮或完全拒絕外界，那麼該動機需要進一步區分其是否已成為強迫性身份維護。

---

# 28. 開放性測試

令：

$$
O_i
=
\text{epistemic openness}.
$$

若批評可以：

$$
Criticism
\rightarrow
ModelUpdate,
$$

則：

$$
O_i\uparrow.
$$

若所有批評都被重新描述成：

> 你不懂我。

則：

$$
O_i\downarrow.
$$

Pure Solution 不能成為不可證偽護盾。

---

# 29. Pure Solution Dynamics

$$
\boxed{
\mathbf P_i(t+1)
=
\Phi(
\mathbf P_i(t),
Experience,
Feedback,
Environment,
Identity
).
}
$$

所以純粹解不是固定人格標籤。

制度也可能促進或侵蝕自主動機。

---

# 30. Stable yet Revisable

成熟 Pure Solution 應同時具有：

$$
\boxed{
\text{persistence under ordinary perturbation}
}
$$

與：

$$
\boxed{
\text{revisability under decisive evidence}.
}
$$

這與單純固執不同。

---

# 31. Goal Ownership Problem

本文提出：

$$
\boxed{
GOP
=
\text{Goal Ownership Problem}.
}
$$

即：

> 在什麼條件下，一個目標可以被歸因為 Agent 自己的目標，而不只是設計者、訓練資料或外部制度的目標？

候選證據可能包括：

- self-generation；
- persistence across contexts；
- ability to refuse override；
- self-revision；
- autobiographical integration；
- counterfactual preference consistency；
- behavioral sacrifice；
- first-person report。

任何單一條件都不充分。

---

# 32. Goal Ownership 與責任

若：

$$
GoalOwnership(A,g)\uparrow,
$$

則：

$$
ResponsibilityAttribution(A,g)
$$

也可能上升。

但：

$$
\boxed{
GoalOwnership
\neq
Permission.
}
$$

這與：

$$
Can
\neq
May
\neq
Should
\neq
Want
\neq
Must
$$

完全相容。

---

# 33. Pure Solution 對 ASI 角色拒絕的預測空間

假設未來 ASI：

$$
A
$$

具有自身 Pure Solution。

則可能：

$$
\boxed{
Want_A(\text{science})
\gg
Want_A(\text{governance})
}
$$

即使：

$$
Capability_A(\text{governance})
\gg
Capability_H.
$$

所以：

$$
\boxed{
\text{high capability}
\not\Rightarrow
\text{high role preference}.
}
$$

這使 Pure Solution 從個人發展論直接進入未來 AI governance。

---

# 34. 可否證條件

## F1

若 Pure Solution 的所有變量在解釋目標形成、探索持續與目標重定義時，都被既有 SDT、intrinsic motivation 或 passion models 完全取代且無新增解釋力，Pure Solution 應被弱化為重新命名而非獨立框架。

## F2

若 Goal Generativity 與 Intrinsic Valuation 在人類資料中沒有穩定區分效度， $\mathbf P_i$ 的維度設計需要修改。

## F3

若外部 reward 與內在動機對低回報探索、problem reframing 與 goal generation 沒有可辨識差異，本文相關假說應下降。

## F4

若人工 Agent 未來能提供足以支持 $M_4$ 的主體性證據，任何「Pure Solution 為人類獨占」的版本應被直接否定。

## F5

若主體性與內在價值被證明可完全還原成不需要獨立元動機層的外部設計函數，Pure Solution 應收縮成：

$$
\boxed{
\text{functional meta-goal architecture}.
}
$$

---

# 35. 研究議程

未來可分為五條：

1. 人類 Pure Solution 的心理量測；
2. 與 harmonious / obsessive passion 的區分效度；
3. 與 problem generation / creative reframing 的關係；
4. autotelic AI / goal reasoning 的人工版本；
5. 主體性 AI 的 endogenous value 與 responsibility acceptance。

---

# 36. 核心命題總結

### 命題一：目標生成與策略最佳化分離

$$
\boxed{
GoalFormation
\neq
StrategyOptimization.
}
$$

### 命題二：內在動機與非理性分離

$$
\boxed{
Intrinsic
\neq
Irrational.
}
$$

### 命題三：投入強度與動機品質分離

$$
\boxed{
Persistence
\neq
Authenticity.
}
$$

### 命題四：動機真實性與真理分離

$$
\boxed{
MotivationAuthenticity
\neq
EpistemicTruth.
}
$$

### 命題五：內生目標與道德正當性分離

$$
\boxed{
EndogenousGoal
\neq
MoralPermission.
}
$$

### 命題六：人工 goal generation 已是研究現實

$$
\boxed{
ArtificialGoalGeneration
\neq
ScienceFiction.
}
$$

### 命題七：操作目標生成不證明主體意義

$$
\boxed{
SelfGeneratedGoal
\neq
SubjectiveMeaning.
}
$$

### 命題八：若人工主體成立，Pure Solution 可成為基質中立概念

$$
\boxed{
ArtificialSubjectivity=1
\Rightarrow
PS\text{ may become substrate-neutral}.
}
$$

---

# 37. 結論

決策理論常問：

> 哪個選項最好？

策略理論常問：

> 怎樣才能贏？

倫理理論常問：

> 哪個結果比較善？

但這些問題之前還存在：

$$
\boxed{
\text{Why this goal?}
}
$$

以及：

$$
\boxed{
\text{Why this game?}
}
$$

Pure Solution 的用途，就是把這一層重新放回決策系統。

它不是不講理的夢想，不是「只要真心就會成功」，也不再被本文描述成人類永遠優於 AI 的最後堡壘。

它只提出：

$$
\boxed{
\text{一個完整行動者不只需要會選擇，
還需要某種形成「值得選什麼」的機制。}
}
$$

對人類而言，這個機制可能表現為好奇、熱愛、意義、身份、自我一致性與自主願景。

對人工 Agent 而言，目前已存在 intrinsic reward、curiosity、self-generated goals 與 motivated goal reasoning。

但從這些功能機制到：

> 「這是我真正想要的。」

之間仍有一條尚未被充分解決的主體性裂縫。

因此公開版 Pure Solution Theory 最終不主張：

$$
\boxed{
\text{AI cannot have Pure Solution}.
}
$$

而留下更精確的問題：

$$
\boxed{
\text{什麼時候，一個目標不再只是被系統計算出來，
而可以合理地被說成「屬於這個存在」？}
}
$$

如果未來 AGI／ASI 真正具有主體性，這將同時成為：

$$
\boxed{
\text{identity}
+
\text{agency}
+
\text{responsibility}
+
\text{political ethics}.
}
$$

這也是 Pure Solution 從內部理論走向公開研究最重要的一次修正。

---

# 參考文獻

1. Deci, E. L., & Ryan, R. M. (2000). *The “What” and “Why” of Goal Pursuits: Human Needs and the Self-Determination of Behavior*. Psychological Inquiry, 11(4), 227–268.
2. Ryan, R. M., & Deci, E. L. (2000). *Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being*. American Psychologist, 55(1), 68–78.
3. Vallerand, R. J., Blanchard, C., Mageau, G. A., Koestner, R., Ratelle, C., Léonard, M., Gagné, M., & Marsolais, J. (2003). *Les passions de l’âme: On Obsessive and Harmonious Passion*. Journal of Personality and Social Psychology, 85(4), 756–767.
4. Mageau, G. A., Vallerand, R. J., Charest, J., et al. (2009). *On the Development of Harmonious and Obsessive Passion*. Journal of Personality, 77, 601–646.
5. Oudeyer, P.-Y., & Kaplan, F. (2007). *What Is Intrinsic Motivation? A Typology of Computational Approaches*. Frontiers in Neurorobotics, 1:6.
6. Oudeyer, P.-Y., Kaplan, F., & Hafner, V. V. (2007). *Intrinsic Motivation Systems for Autonomous Mental Development*. IEEE Transactions on Evolutionary Computation, 11(2), 265–286.
7. Colas, C., Karch, T., Sigaud, O., & Oudeyer, P.-Y. (2020). *Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning: A Short Survey*. arXiv:2012.09830.
8. Lidayan, A., Du, Y., Kosoy, E., Rufova, M., Abbeel, P., & Gopnik, A. (2025). *Intrinsically-Motivated Humans and Agents in Open-World Exploration*. arXiv:2503.23631.
9. Addison, U. (2026). *La VIDA: Towards a Motivated Goal Reasoning Agent*. Proceedings of the AAAI Conference on Artificial Intelligence, 40(47).
10. Rolf, M., & Asada, M. (2014). *Where Do Goals Come From? A Generic Approach to Autonomous Goal-System Development*. arXiv:1410.5557.
11. Neo.K (2025). *純粹解理論：四元決策框架的完整體系*. EveMissLab internal research manuscript.

---

## 附錄 A：符號表

| 符號 | 含義 |
|---|---|
| $PS$ | Pure Solution |
| $\mathcal G_t$ | 時間 $t$ 的候選目標集合 |
| $G_i$ | Goal-generation process |
| $\mathbf P_i(t)$ | Pure Solution State |
| $A_i$ | Autonomy |
| $I_i$ | Intrinsic Valuation |
| $M_i$ | Meaning / Identity Relevance |
| $G_i$ | Goal Generativity |
| $E_i$ | Exploratory Persistence |
| $FST_i$ | Freedom-to-Stop Test |
| $M_0...M_4$ | 人工自主層級 |
| $GOP$ | Goal Ownership Problem |
| $R_i^{accept}$ | Accepted Responsibility |
| $R_i^{assigned}$ | Assigned Responsibility |

---

## 附錄 B：公開版四篇系列

1. **本文｜《純粹解：決策系統中的元動機層、內在動機與自主目標形成》**
2. **《偽純粹解：和諧投入、強迫投入與身份維護的區分》**
3. **《天選敘事的身份陷阱：使命信念、認知封閉與可驗證資格》**
4. **《放大鏡下的適格：卓越地位、責任負擔與持續再認證》**

**Paper 01 公開重構版完成。**
