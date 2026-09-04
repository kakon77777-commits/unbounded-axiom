---
title: "TCFT-04｜高階推理不等於高階策略：認知成本、注意力分配與停止治理"
title_en: "High-Order Reasoning Is Not High-Order Strategy: Cognitive Cost, Attention Allocation, and Stopping Governance"
series: "Temporal Cognitive Frontier Theory (TCFT) / 時代認知前沿理論"
paper_no: "04"
version: "v0.1"
date: "2026-08-31"
author: "Neo.K"
affiliation: "EveMissLab / 一言諾科技有限公司"
document_type: "理論論文 / Reasoning Allocation Governance 篇"
language: "zh-Hant"
status: "正式系列初稿"
previous_paper: "TCFT-03｜反身性推理：當推理本身進入被推理世界"
next_paper: "TCFT-05｜時間正規化新穎度：Frozen-Time Prior Art 與同期認知基準"
---

# TCFT-04｜高階推理不等於高階策略：認知成本、注意力分配與停止治理

## High-Order Reasoning Is Not High-Order Strategy: Cognitive Cost, Attention Allocation, and Stopping Governance

**系列：** Temporal Cognitive Frontier Theory, TCFT / 時代認知前沿理論  
**篇次：** 04  
**版本：** v0.1  
**日期：** 2026-08-31  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  

---

## 摘要

TCFT-01 至 TCFT-03 依序擴張了一個認知主體可處理的未來結構：未來底空間使更多候選世界進入可思考範圍；反事實視界使未發生世界成為可生成、比較與翻轉決策的候選；反身性推理則把推理者、模型、預測、公開、行動與他者反應重新納入下一輪世界與認知狀態。若只沿能力軸前進，一個自然但錯誤的結論是：**想得越多、越深、越高階，策略就越好。**

本文拒絕此命題。

$$
\boxed{
\text{High-Order Reasoning}
\neq
\text{High-Order Strategy}.
}
$$

原因並不只在於人類有疲勞、時間有限或 AI 有 token budget。更一般地，任何有限智慧體都面對一個 **Reasoning Allocation Problem（推理資源配置問題）**：在多個對象、多個域、多個時間尺度、多種推理操作與多條候選分支之間，應把有限計算、注意力、搜尋、驗證與反身性深度配置在哪裡？

本文提出 **Reasoning Allocation Governance（RAG，推理配置治理）** 作為 TCFT 的策略層候選。對時間 $t$ 的認知預算：

$$
\boxed{
B_t^{cog}
=
B_t^{att}
+
B_t^{search}
+
B_t^{sim}
+
B_t^{cf}
+
B_t^{rr}
+
B_t^{verify}
+
B_t^{switch}
+
B_t^{meta}.
}
$$

其中各項分別表示注意力、搜尋、模擬、反事實、反身推理、驗證、切換與元推理成本。此分解不是神經或計算架構的唯一真實分區，而是一個治理帳本。

本文將 Russell 與 Wefald 的 **utility of computation / value of computation**、bounded rationality、anytime algorithm stopping、resource-rationality、rational inattention 與 expected value of control 視為重要前置文獻。它們共同指出：計算、注意與控制本身具有成本，元層決策必須回答「下一個計算步驟值不值得做」。TCFT-04 在此基礎上加入三個專門面向：第一，未來底空間、反事實與反身性會使搜索空間快速擴張；第二，推理資源配置本身具有 **domain / target opportunity cost**；第三，局部模型解析度提高可能同時降低整體世界與其他主體的覆蓋。

本文提出：

$$
\boxed{
\operatorname{NVOC}_t(r)
=
\mathbb E[
\Delta U_t(r)
]
-
C_t^{direct}(r)
-
C_t^{opp}(r)
-
C_t^{risk}(r)
-
C_t^{delay}(r)
}
$$

其中 $\operatorname{NVOC}$ 為 **Net Value of Computation**， $r$ 表示下一個 reasoning action。若：

$$
\boxed{
\operatorname{NVOC}_t(r)\le 0,
}
$$

則在目前 task、budget、time horizon 與 uncertainty 下，繼續該 reasoning action 不再有正邊際價值。這提供一個比「想累了才停」更一般的停止條件。

本文進一步區分：

$$
\boxed{
\text{Capability}
\neq
\text{Activation}
\neq
\text{Allocation}
\neq
\text{Termination}.
}
$$

一個 agent 可以具有很強的反身性推理能力，但在某一 task 選擇不用；也可以只進行低解析度人物模型，因為該模型已足以支撐行動。這不是能力不足，而可能是更高階的策略配置。

本文提出 **Target Saturation、Domain Neglect、Local-Model Overinvestment、Reasoning Lock-In、Meta-Reasoning Regress、Switching Cost、Strategic Coarsening** 與 **Sufficient Resolution** 等概念。特別地：

$$
\boxed{
\text{High-Resolution Local Model}
\not\Rightarrow
\text{High-Quality Global Strategy}.
}
$$

若把大量資源投入單一他者：

$$
B_{target}\uparrow,
$$

則：

$$
B_{self}
+
B_{others}
+
B_{world}
+
B_{future}
\downarrow
$$

可能同時成立。此時即使對該他者的 inference accuracy 提升，global utility 仍可能下降。

本文最後把 RAG 接回 Cognitive Operator-Domain Theory（CODT）與既有「內外總作用量原理」。CODT 已把高階 method 寫成：

$$
Method
=
Program(
Operators,
Topology,
Context,
Policy,
Budget
),
$$

而既有總作用量理論已提出：

$$
\mathbb E[
\Delta U_{next}
]
\le
\Delta \mathcal S_{next}
$$

作為外部展開停止候選。TCFT-04 將其泛化到內部推理：**推理、反事實、反身性與驗證也都是有成本的作用，策略優劣不在於是否把可用能力全部啟動，而在於是否把正確能力配置到正確地方、正確深度與正確時間。**

本文中心命題為：

$$
\boxed{
\text{Strategic intelligence is not merely the ability to reason deeply,
but the ability to allocate, switch, coarse-grain, and stop reasoning well.}
}
$$

**關鍵詞：** 高階推理、高階策略、推理資源配置、Value of Computation、元推理、注意力成本、停止條件、bounded rationality、resource rationality、rational inattention、CODT、TCFT

---

# Abstract

TCFT-01 through TCFT-03 progressively expanded the cognitive space available to an agent: future base-spaces introduced candidate futures; counterfactual horizons introduced unrealized alternatives; reflexive reasoning reintroduced the reasoner, its models, predictions, disclosures, actions, and induced reactions into subsequent world and reasoning states. A tempting but incorrect conclusion is that greater reasoning depth, breadth, or reflexivity automatically yields better strategy.

This paper rejects that conclusion:

$$
\boxed{
\text{High-Order Reasoning}
\neq
\text{High-Order Strategy}.
}
$$

The reason is more general than human fatigue or AI token limits. Any finite cognitive system faces a **Reasoning Allocation Problem**: how should limited attention, computation, search, simulation, counterfactual expansion, reflexive depth, verification, switching, and metareasoning be allocated across targets, domains, timescales, and possible reasoning actions?

We propose **Reasoning Allocation Governance (RAG)** as a strategy-layer candidate within TCFT. A cognitive budget is decomposed as a governance ledger rather than a claim about literal neural modules:

$$
\boxed{
B_t^{cog}
=
B_t^{att}
+
B_t^{search}
+
B_t^{sim}
+
B_t^{cf}
+
B_t^{rr}
+
B_t^{verify}
+
B_t^{switch}
+
B_t^{meta}.
}
$$

Building on utility-of-computation metareasoning, bounded rationality, anytime-algorithm stopping, resource-rational analysis, rational inattention, and expected-value-of-control frameworks, we define a candidate Net Value of Computation:

$$
\boxed{
\operatorname{NVOC}_t(r)
=
\mathbb E[
\Delta U_t(r)
]
-
C_t^{direct}(r)
-
C_t^{opp}(r)
-
C_t^{risk}(r)
-
C_t^{delay}(r).
}
$$

When $\operatorname{NVOC}_t(r)\le 0$, continuing that reasoning action no longer has positive marginal value under the current task, budget, uncertainty, and horizon.

The paper distinguishes capability, activation, allocation, and termination. It introduces Target Saturation, Domain Neglect, Local-Model Overinvestment, Reasoning Lock-In, Meta-Reasoning Regress, Switching Cost, Strategic Coarsening, and Sufficient Resolution. A particularly important claim is that increasing the resolution of a local model can reduce global strategic quality by consuming resources that could have been allocated to self-modeling, third parties, environment, future contingencies, or validation.

Finally, the framework is connected to Cognitive Operator-Domain Theory (CODT) and prior work on total internal-external action costs. The central proposition is:

$$
\boxed{
\text{Strategic intelligence is not merely the ability to reason deeply,
but the ability to allocate, switch, coarse-grain, and stop reasoning well.}
}
$$

**Keywords:** high-order reasoning; strategy; value of computation; metareasoning; attention allocation; stopping; bounded rationality; resource rationality; rational inattention; TCFT

---

# 1. 導論：能力擴張之後，為什麼需要治理？

前面三篇逐步回答：

$$
\boxed{
\text{我能想到哪些未來？}
}
$$

$$
\boxed{
\text{我能生成哪些未發生世界？}
}
$$

$$
\boxed{
\text{我能否把自己與他人的反應放回推理？}
}
$$

但一個真正有限的智慧體還必須回答：

$$
\boxed{
\text{我現在應該把計算資源花在哪裡？}
}
$$

以及：

$$
\boxed{
\text{我什麼時候應該停止？}
}
$$

---

# 2. 高階推理不等於高階策略

假設 agent A 可以做：

$$
RR_{10},
$$

agent B 只做：

$$
RR_2.
$$

不能推出：

$$
Strategy(A)>Strategy(B).
$$

因為：

$$
RR_{10}
$$

可能提供幾乎零新增決策價值，

卻消耗大量：

- time；
- attention；
- compute；
- opportunity；
- verification；
- delay budget。

因此：

$$
\boxed{
\text{Depth}
\not\Rightarrow
\text{Value}.
}
$$

---

# 3. Strategy 是 Reasoning over Reasoning Allocation

普通 reasoning：

$$
R:
State
\rightarrow
Conclusion.
$$

strategy-level metareasoning 則問：

$$
\boxed{
M_R:
State
\rightarrow
\text{Which reasoning action should be executed next?}
}
$$

所以 reasoning action 本身成為 decision variable。

---

# 4. Computational Action

令：

$$
r_t
$$

表示一個 reasoning action。

它可以是：

- 搜尋一個來源；
- 展開一個 counterfactual；
- 增加一階 recursive ToM；
- 驗證一個 assumption；
- 模擬一個 scenario；
- 改變 representation；
- 切換 domain；
- 查證一個 prior；
- 停止。

因此：

$$
\boxed{
r_t
\in
\mathcal R_t^{meta}.
}
$$

---

# 5. Value of Computation

Russell 與 Wefald 的 metareasoning 傳統核心問題之一正是：

> 一個計算步驟因為可能改變外部行動，其價值是多少？

TCFT 沿用此精神。

令：

$$
U_t^*
$$

為目前最佳可行決策的 expected utility。

執行 reasoning action：

$$
r
$$

之後，可能更新為：

$$
U_{t+1}^*.
$$

則粗略 expected improvement：

$$
\boxed{
\operatorname{VOC}(r)
=
\mathbb E[
U_{t+1}^*-U_t^*
].
}
$$

---

# 6. Net Value of Computation

TCFT 進一步扣除多種成本：

$$
\boxed{
\operatorname{NVOC}_t(r)
=
\mathbb E[
\Delta U_t(r)
]
-
C_t^{direct}(r)
-
C_t^{opp}(r)
-
C_t^{risk}(r)
-
C_t^{delay}(r).
}
$$

其中：

$$
C^{direct}
$$

為直接計算／注意／工具成本。

$$
C^{opp}
$$

為因執行 $r$ 而不能做其他事的機會成本。

$$
C^{risk}
$$

為錯誤展開、過度自信、資訊污染或不可逆行動相關風險。

$$
C^{delay}
$$

為延遲決策造成的價值損失。

---

# 7. 停止條件

若：

$$
\boxed{
\operatorname{NVOC}_t(r)\le 0,
}
$$

則繼續這個 reasoning action 沒有正邊際價值。

因此：

$$
\boxed{
\text{Stop}
\not\Rightarrow
\text{No More Reasoning Is Possible}.
}
$$

而是：

$$
\boxed{
\text{No Currently Available Reasoning Action Has Positive Net Value}.
}
$$

---

# 8. Global Stopping

若：

$$
\max_{r\in\mathcal R_t^{meta}}
\operatorname{NVOC}_t(r)
\le0,
$$

可候選性地停止整個 deliberation：

$$
\boxed{
\text{Act / Commit / Defer / Idle}.
}
$$

實際 outcome 仍依任務與權限而定。

---

# 9. Bounded Rationality

bounded rationality 的核心不是：

> 有限智慧體比較笨。

而是：

$$
\boxed{
\text{optimization itself has costs and limits}.
}
$$

即使存在理論上的最佳答案：

$$
a^*,
$$

找到：

$$
a^*
$$

可能比使用一個足夠好的：

$$
\tilde a
$$

成本高得多。

---

# 10. Bounded Optimality 與 TCFT

因此真正策略目標可以從：

$$
\arg\max_a U(a)
$$

轉向：

$$
\boxed{
\arg\max_{\pi}
\mathbb E[
U(
Outcome(\pi)
)
-
C(\pi)
].
}
$$

其中：

$$
\pi
$$

包含整個 reasoning policy，

而不是單一外部 action。

---

# 11. Resource Rationality

resource-rational analysis 把認知策略視為在有限 computational resources 下的適應性／近似最適配置。

TCFT 接受這個重要方向。

但 TCFT-04 特別強調：

$$
\boxed{
\text{the resource budget is distributed across domains,
targets, reasoning modes, and reflexive depths}.
}
$$

不是只有同一問題內的計算深度。

---

# 12. Rational Inattention

rational inattention 提醒：

$$
\boxed{
\text{information processing itself is costly}.
}
$$

因此不是所有可取得資訊都值得處理。

---

# 13. Expected Value of Control

Expected Value of Control 模型把 expected payoff、control intensity 與 effort cost 放進同一控制配置問題。

TCFT 將此精神泛化為：

$$
\boxed{
\text{How much cognitive control should be allocated,
to what, and for how long?}
}
$$

---

# 14. Cognitive Budget Ledger

定義：

$$
\boxed{
B_t^{cog}
=
B_t^{att}
+
B_t^{search}
+
B_t^{sim}
+
B_t^{cf}
+
B_t^{rr}
+
B_t^{verify}
+
B_t^{switch}
+
B_t^{meta}.
}
$$

它不是聲稱認知真的必須物理切成八個池，而是一個治理帳本。

---

# 15. Capability、Activation、Allocation、Termination

TCFT-04 的核心 separation：

$$
\boxed{
\text{Capability}
\neq
\text{Activation}
\neq
\text{Allocation}
\neq
\text{Termination}.
}
$$

一個 agent 有能力：

$$
RR_{10}
$$

不代表每次都該啟動：

$$
RR_{10}.
$$

---

# 16. Strategic Restraint

若 task 只需：

$$
RR_2,
$$

但：

$$
Cap(RR_{10})=1,
$$

合理策略仍可：

$$
\boxed{
Act(RR_{10})=0.
}
$$

這不是能力不足，而可能是：

$$
\boxed{
\text{Strategic Restraint}.
}
$$

---

# 17. Sufficient Resolution

對 target $X$，令模型解析度為：

$$
\rho_X.
$$

若：

$$
\boxed{
Decision(
M_X^{\rho}
)
=
Decision(
M_X^{\rho+\Delta}
)
}
$$

在合理 uncertainty 與 perturbation 下持續穩定，則可候選地稱為：

$$
\boxed{
\text{Sufficient Resolution}.
}
$$

---

# 18. Strategic Coarsening

如果：

$$
M_X^{coarse}
$$

已足以支持 action，

則：

$$
\boxed{
\text{Strategic Coarsening}
}
$$

可能比最大解析度更好。

粗略不必等於錯誤。

---

# 19. Local-Model Overinvestment

定義：

$$
\boxed{
\text{Local-Model Overinvestment}
}
$$

當：

$$
\Delta Accuracy_{target}>0
$$

但：

$$
\Delta U_{global}<0.
$$

也就是：

> 局部模型變準，整體策略反而變差。

---

# 20. 為什麼局部變準仍可能全域變差？

因為：

$$
\boxed{
B_{total}
=
B_{target}
+
B_{self}
+
B_{others}
+
B_{world}
+
B_{future}
+
B_{verify}.
}
$$

若：

$$
B_{target}\uparrow,
$$

其他項可能下降。

---

# 21. Target Saturation

若對 target $j$ 的邊際增益：

$$
\Delta U_j(b)
$$

隨 budget 下降，

且：

$$
\boxed{
\frac{\partial \mathbb E[U]}{\partial b_j}
\le0,
}
$$

則可候選稱為：

$$
\boxed{
\text{Target Saturation}.
}
$$

---

# 22. Domain Neglect

若 agent 長期大量投入：

$$
D_1
$$

而忽略：

$$
D_2,\ldots,D_n,
$$

即使：

$$
Performance(D_1)
$$

非常高，

仍可能形成：

$$
\boxed{
\text{Domain Neglect}.
}
$$

---

# 23. Domain Allocation Problem

令：

$$
\mathcal D
=
\{D_1,\ldots,D_n\}.
$$

分配：

$$
b_1,\ldots,b_n
$$

subject to：

$$
\sum_{k=1}^{n}b_k\le B.
$$

策略問題：

$$
\boxed{
\max_{\mathbf b}
\mathbb E[
U(
b_1,\ldots,b_n
)
].
}
$$

---

# 24. 平均分配不等於合理

最佳配置一般不要求：

$$
b_1=b_2=\cdots=b_n.
$$

因為不同 domain 具有不同：

- urgency；
- uncertainty；
- expected impact；
- risk；
- decision sensitivity。

---

# 25. Attention Opportunity Cost

把注意力放在 $X$，意味此刻無法完整放在 $Y$。

因此：

$$
\boxed{
C^{opp}(X)
}
$$

是推理配置的實質成本，而不只是心理疲勞。

---

# 26. 自己也是被配置的 target

分析：

$$
M_A(B)
$$

時，還要問：

$$
\boxed{
M_A(
A\mid M_A(B)
).
}
$$

也就是：

> 我正在因為研究 B 而做什麼？

---

# 27. Self-Game

現在的自己：

$$
A_t
$$

可以選擇繼續深挖。

未來的自己：

$$
A_{t+1}
$$

承擔延遲、時間與 lost alternatives。

所以：

$$
\boxed{
A_t
\leftrightarrow
A_{t+1}
}
$$

形成一種 intertemporal self-game。

---

# 28. Value of Information 不等於 Value of Computation

某資訊如果拿到可能極有價值：

$$
VOI(I)\gg0.
$$

但取得它可能極昂貴。

因此：

$$
\boxed{
VOI
\neq
VOC.
}
$$

---

# 29. Value of Search

搜尋 $s$ 的預期價值可候選寫成：

$$
\boxed{
VOS(s)
=
\mathbb E[
VOI(
Result(s)
)
]
-
C(s).
}
$$

---

# 30. Value of Verification

驗證 $v$：

$$
\boxed{
VOV(v)
=
ExpectedLossAvoided(v)
-
C(v).
}
$$

因此不需要所有 claim 都用相同驗證強度。

---

# 31. Verification Allocation

高風險、不可逆、高外部性的 claim：

$$
B_{verify}\uparrow.
$$

探索性、低風險假說：

$$
B_{verify}
$$

可以較低。

---

# 32. Delay Cost

若 deadline：

$$
T_d,
$$

reasoning 耗時：

$$
\tau_r,
$$

則可能產生：

$$
\boxed{
C^{delay}(r).
}
$$

因此：

$$
\text{better answer later}
$$

可能輸給：

$$
\text{good-enough answer now}.
$$

---

# 33. Anytime Reasoning

anytime algorithm 的精神是：

> 多算通常可以改善答案，但任何時點都可返回目前解。

TCFT 將其抽象到 reasoning。

真正需要決定：

$$
\boxed{
t_{stop}.
}
$$

---

# 34. Stop 是一個 Meta-Action

停止不是沒有 action。

$$
\boxed{
Stop
\in
\mathcal R^{meta}.
}
$$

與：

- Search；
- Expand；
- Verify；
- Simulate；

同樣是策略選項。

---

# 35. Optimal Stopping Candidate

如果：

$$
\max_r
\operatorname{NVOC}(r)
\le0,
$$

則：

$$
\boxed{
Stop
}
$$

可能是最合理選擇。

所以：

$$
\boxed{
\text{Knowing when not to think further
is part of strategic intelligence}.
}
$$

---

# 36. Premature Stopping

若存在：

$$
r^*
$$

使：

$$
\operatorname{NVOC}(r^*)\gg0
$$

但 agent 已停止，

則：

$$
\boxed{
\text{Premature Stopping}.
}
$$

---

# 37. Overthinking

若持續執行：

$$
r_1,r_2,\ldots
$$

而：

$$
\operatorname{NVOC}(r_k)<0
$$

持續成立，

可候選性地稱：

$$
\boxed{
\text{Overthinking}.
}
$$

這是一個功能定義，不是心理診斷。

---

# 38. Reasoning Lock-In

若 agent 因已投入大量：

$$
C_{past}
$$

而繼續同一路徑，即使未來邊際價值低，

形成：

$$
\boxed{
\text{Reasoning Lock-In}.
}
$$

已付出的 reasoning cost 不應自動增加未來 reasoning value。

---

# 39. Switching Cost

從：

$$
D_i
$$

切換到：

$$
D_j
$$

具有：

$$
C_{switch}(i,j).
$$

可能包括：

- context rebuild；
- memory load；
- representation shift；
- tool shift；
- synchronization。

---

# 40. Contextual Inertia

如果：

$$
C_{switch}
$$

很高，

agent 可能即使知道別的 domain 更重要，也不切。

形成：

$$
\boxed{
\text{Contextual Inertia}.
}
$$

---

# 41. Thrashing

反過來，頻繁切換會使：

$$
C_{switch}\uparrow
$$

形成：

$$
\boxed{
\text{Thrashing}.
}
$$

策略必須在 Lock-In 與 Thrashing 之間取得平衡。

---

# 42. Domain Switching Policy

候選：

$$
\boxed{
\pi_{switch}(S_t)
\rightarrow
\{
Stay,
Switch(D_j),
Pause,
Merge,
Delegate
\}.
}
$$

---

# 43. Delegation

如果 reasoning action：

$$
r
$$

可交給另一 agent 或 tool，

策略集合就不是：

$$
\{Do,NotDo\}
$$

而是：

$$
\boxed{
\{Do,Delegate,Defer,Stop\}.
}
$$

---

# 44. Delegation Value

$$
\boxed{
VOD(r,j)
=
ExpectedGain(r,j)
-
CoordinationCost
-
VerificationCost
-
TrustRisk.
}
$$

---

# 45. Multi-Agent Allocation

對 agents：

$$
A_1,\ldots,A_n,
$$

目標不是讓所有 agent 重複相同 computation，

而是：

$$
\boxed{
\text{maximize complementary coverage per total cost}.
}
$$

---

# 46. Redundancy 不是永遠浪費

如果獨立 replication 能顯著降低 model error，

則：

$$
\boxed{
\text{Redundancy}
\neq
\text{Waste}.
}
$$

---

# 47. Correlated Redundancy

若所有 agents 共用：

- same model；
- same data；
- same prompt；
- same blindspot；

重複十次可能只產生：

$$
\boxed{
\text{correlated confidence}.
}
$$

---

# 48. Attention to Other Others

在 social reasoning 中，如果只模型：

$$
B,
$$

容易忽略：

$$
C,D,E,\ldots
$$

但 relationship outcome 可能主要受到第三方支配。

所以：

$$
\boxed{
\text{Target-Centric Reasoning}
\not\Rightarrow
\text{System-Centric Strategy}.
}
$$

---

# 49. World Outside the Social Graph

甚至不能把所有注意力都留給 agents。

還有：

- environment；
- technology；
- institution；
- deadline；
- random shock；
- resource state。

因此：

$$
\boxed{
B_{social}
\neq
B_{global}.
}
$$

---

# 50. Strategic Scope

令：

$$
\mathcal S_t
$$

為目前納入策略的 scope。

若：

$$
\mathcal S_t
$$

過窄，

則高深度 reasoning 可能是：

$$
\boxed{
\text{locally sophisticated, globally blind}.
}
$$

---

# 51. Scope-Depth Tradeoff

固定 budget 下常出現：

$$
\boxed{
Depth\uparrow
\Rightarrow
Breadth\downarrow
}
$$

的資源 tradeoff。

這不是邏輯必然，而是有限資源條件。

---

# 52. Strategic Intelligence Vector

TCFT-04 可保存：

$$
\boxed{
\vec S_i
=
(
Allocation,
Switching,
Stopping,
Coarsening,
Verification,
Delegation,
ScopeControl,
MetaEfficiency
).
}
$$

而不是壓成一個「策略 IQ」。

---

# 53. Reasoning Efficiency

定義候選：

$$
\boxed{
\eta_R
=
\frac{
\Delta U_{decision}
}{
C_{cog}
}.
}
$$

但：

$$
\boxed{
Efficiency
\neq
ObjectiveValidity.
}
$$

更有效率地完成錯誤目標仍然是錯。

---

# 54. Goal Review

因此治理中要保留：

$$
\boxed{
B_{goal-review}.
}
$$

在：

- anomaly；
- repeated failure；
- regime shift；

時提升。

---

# 55. Adaptive Governance

若：

$$
Regime_t
\neq
Regime_{t+1},
$$

原配置策略可以：

$$
\boxed{
\pi_R^*(t)
\neq
\pi_R^*(t+1).
}
$$

RAG 必須可版本化與情境化。

---

# 56. Cognitive Cost 不只有時間

至少可以拆：

$$
\boxed{
C_{cog}
=
C_{time}
+
C_{compute}
+
C_{attention}
+
C_{memory}
+
C_{switch}
+
C_{verify}
+
C_{delay}
+
C_{risk}.
}
$$

---

# 57. Token Cost 只是 AI 的一部分

對 LLM：

$$
C_{token}
$$

只是：

$$
\boxed{
C_{token}
\subset
C_{cog-total}.
}
$$

工具、搜尋、驗證、狀態同步與 human review 可能更昂貴。

---

# 58. Low Subjective Effort 不等於 Low Strategic Cost

即使人類主觀上「不累」，

推理仍消耗：

- time；
- opportunity；
- attention channel；
- delayed action。

所以：

$$
\boxed{
\text{Low Subjective Effort}
\not\Rightarrow
\text{Low Strategic Cost}.
}
$$

---

# 59. More Capability Can Increase Allocation Complexity

如果：

$$
Cap\uparrow,
$$

可選 reasoning actions：

$$
|\mathcal R^{meta}|\uparrow.
$$

因此：

$$
\boxed{
\text{More Capability}
\not\Rightarrow
\text{Simpler Strategy}.
}
$$

---

# 60. Reasoning Inflation

AI 讓單次 reasoning 變便宜：

$$
C(r)\downarrow.
$$

但如果使用量：

$$
N(r)\uparrow\uparrow,
$$

總成本：

$$
N(r)C(r)
$$

不一定下降。

本文暫稱：

$$
\boxed{
\text{Reasoning Inflation}.
}
$$

---

# 61. Verification Bottleneck

AI 可以快速生成：

$$
10^4
$$

候選，

但 human / verifier 只能檢查：

$$
20.
$$

則真正 bottleneck 是：

$$
\boxed{
B_{verify}.
}
$$

這時再增加 generation 可能沒有正邊際價值。

---

# 62. TCFT-01 的停止問題

未來底空間：

$$
\Omega_t
$$

何時不再擴張？

當：

$$
\boxed{
\mathbb E[
\Delta U_{new-future}
]
\le
C_{expand}
+
C_{evaluate}
+
C_{delay}.
}
$$

---

# 63. TCFT-02 的停止問題

反事實視界：

$$
\mathcal C_t
$$

何時停止？

當：

$$
\boxed{
\max_{c_{new}}
ExpectedReversalValue(c_{new})
\le
Cost(c_{new}).
}
$$

---

# 64. TCFT-03 的停止問題

反身深度：

$$
d_R
$$

何時停止？

當：

$$
\boxed{
\Delta DecisionValue(d_R+1)
\le
\Delta Cost(d_R+1).
}
$$

---

# 65. Unified Marginal Stopping Principle

因此可統一成：

$$
\boxed{
\mathbb E[
\Delta U_{next}
]
\le
\Delta C_{next}
+
\Delta C_{opp,next}
+
\Delta C_{risk,next}.
}
$$

則考慮：

$$
\boxed{
Stop / Switch / Delegate / Act.
}
$$

---

# 66. 與內外總作用量原理的接口

既有 DIEEC 已提出：

$$
\boxed{
\mathbb E[
\Delta U_{expand}
]
>
\Delta \mathcal S_{expand}
}
$$

才值得繼續展開，

而：

$$
\boxed{
\mathbb E[
\Delta U_{next}
]
\le
\Delta \mathcal S_{next}
}
$$

作為停止候選。

TCFT-04 把此原則泛化到內部 reasoning action。

---

# 67. Cognitive Action Cost

對 reasoning action：

$$
r_t,
$$

可定義：

$$
\boxed{
\mathcal L_t^{cog}(r_t)
=
C_{att}
+
C_{compute}
+
C_{memory}
+
C_{switch}
+
C_{verify}
+
C_{delay}
+
C_{risk}.
}
$$

---

# 68. Cognitive Action Path

整條 reasoning trajectory：

$$
\Gamma_R
=
\{
S_0,r_0,S_1,r_1,\ldots,S_T
\}.
$$

總成本：

$$
\boxed{
\mathcal S_R[\Gamma_R]
=
\sum_{t=0}^{T-1}
\mathcal L_t^{cog}(r_t)
+
C_{terminal}.
}
$$

---

# 69. Strategic Objective

候選：

$$
\boxed{
\pi_R^*
=
\arg\max_{\pi_R}
\left[
\mathbb E[
U_{task}
]
-
\mathcal S_R[\pi_R]
\right].
}
$$

subject to：

- safety；
- legality；
- epistemic minimum；
- deadline；
- minimum verification。

---

# 70. CODT 接口

CODT 已有：

$$
\boxed{
Method
=
Program(
Operators,
Topology,
Context,
Policy,
Budget
).
}
$$

TCFT-04 的 RAG 主要對應：

$$
\boxed{
Policy
+
Budget
+
Termination
+
Routing.
}
$$

---

# 71. RAG 不是 Domain 宣告

依 CODT：

$$
\boxed{
RAG
\not\Rightarrow
PromotedDomain.
}
$$

目前最保守定位是：

$$
\boxed{
\text{meta-policy / scheduler / governance-layer candidate}.
}
$$

---

# 72. Think-Act Boundary

繼續思考與立即行動本身也是競爭選項。

如果：

$$
V_{think}
=
\max_r NVOC(r)
$$

低於立即行動的淨價值，

就應：

$$
\boxed{
ActNow.
}
$$

實際形式需要 task-specific 定義。

---

# 73. Defer 與 Idle

如果目前資訊不足，但未來自然會有高價值 evidence，

則：

$$
\boxed{
Defer
}
$$

可能優於：

$$
ThinkForever.
$$

若沒有必要行動或繼續推理：

$$
\boxed{
Idle
}
$$

也可以是合法策略。

---

# 74. Reasoning Allocation Governance

RAG 最小輸出候選：

$$
\boxed{
G_R(S_t)
\rightarrow
\{
Reason,
Search,
Verify,
ExpandCF,
ExpandRR,
Switch,
Delegate,
Act,
Defer,
Stop,
Idle
\}.
}
$$

---

# 75. Confidence 不是停止準則

高 confidence 仍可能有：

- support failure；
- blindspot；
- self-confirmation。

低 confidence 也不一定值得繼續，

如果下一步成本過高。

所以：

$$
\boxed{
Confidence
\neq
StoppingCriterion.
}
$$

---

# 76. Decision Sensitivity

真正重要的常常不是 uncertainty 單獨大小，

而是：

$$
\boxed{
\text{Uncertainty}
\times
\text{Decision Sensitivity}.
}
$$

如果 uncertainty 很高但 action 幾乎不變，

繼續推理價值可能很低。

---

# 77. Expected Regret Reduction

可以候選定義：

$$
\boxed{
ERR(r)
=
ExpectedRegret_{before}
-
ExpectedRegret_{after\ r}.
}
$$

如果：

$$
ERR(r)
$$

很小，

則 $r$ 可能沒有策略價值。

---

# 78. Risk-Sensitive Allocation

若有 low-probability high-impact branch：

$$
P(c^*)\ll1,
$$

但：

$$
Loss(c^*)\gg1,
$$

它仍可能：

$$
NVOC(c^*)>0.
$$

所以不能只用 probability pruning。

---

# 79. Myopic 與 Non-Myopic Metareasoning

只看：

$$
NVOC(r_t)
$$

可能漏掉：

> 這一步本身沒直接收益，但會開啟高價值 reasoning region。

因此需要：

$$
\boxed{
\text{non-myopic metareasoning}.
}
$$

---

# 80. Gateway Computation

某 reasoning action：

$$
r_g
$$

直接價值：

$$
\Delta U\approx0,
$$

但會解鎖：

$$
r_{high}.
$$

因此：

$$
\boxed{
V(r_g)
=
V_{direct}
+
V_{option}.
}
$$

---

# 81. Option Value of Computation

定義候選：

$$
\boxed{
OVC(r)
}
$$

表示：

> 這個 reasoning action 是否打開未來高價值計算選項？

---

# 82. Amortized Cognitive Value

某些昂貴結構：

- ontology；
- index；
- reusable model；
- toolchain；

可以跨任務攤銷。

所以：

$$
C_{now}
>
Benefit_{now}
$$

不代表長期不值得。

可候選寫：

$$
\boxed{
ACV(r)
=
\sum_k ExpectedBenefit_k(r)
-
LifecycleCost(r).
}
$$

---

# 83. Meta-Reasoning Regress

如果用：

$$
M_2
$$

決定：

$$
M_1,
$$

再用：

$$
M_3
$$

決定：

$$
M_2,
$$

形成：

$$
M_1
\leftarrow
M_2
\leftarrow
M_3
\leftarrow
\cdots
$$

則產生：

$$
\boxed{
\text{Meta-Reasoning Regress}.
}
$$

meta 層也必須接受：

$$
\boxed{
NVOC^{meta}\le0
}
$$

時停止。

---

# 84. Allocation Audit

對 AI runtime 特別重要的是保留：

$$
\boxed{
ReasoningLedger_t
=
(
Action,
Target,
Domain,
Budget,
ExpectedGain,
ActualGain,
Cost,
StopReason
).
}
$$

如此才能回放：

> 為什麼當時選擇不繼續想？

---

# 85. 可反證命題

## H1：Reasoning Depth 與 Strategic Utility 可分離

若在控制 task difficulty 後，reasoning depth 總是單調提高 cost-adjusted strategic outcome，TCFT-04 的核心 separation 被削弱。

## H2：NVOC-Based Stopping 優於固定深度

若 fixed-depth reasoning 在 heterogeneous tasks 中不劣於 cost-aware stopping，NVOC 的工程必要性降低。

## H3：Strategic Coarsening 可提高 Global Utility

若 coarse local model 永遠無法在 cost-adjusted global performance 上超越 fine model，Strategic Coarsening 應降級。

## H4：Domain Switching 改善 Multi-Domain Tasks

若 explicit switch policy 沒有帶來收益，domain-level routing 可能不必要。

## H5：Verification Allocation 優於 Uniform Verification

若所有 claim 同樣驗證比 risk-sensitive allocation 更好，selective verification 沒有必要。

## H6：Meta-Reasoning Cost 不可忽略

若 meta-control cost 始終 negligible， $B^{meta}$ 不必單獨建模。

---

# 86. 實驗設計

### Experiment A：Fixed Depth vs Cost-Aware Stopping

比較：

$$
Depth=k
$$

與：

$$
NVOC\text{-stop}.
$$

量測：

- utility；
- accuracy；
- latency；
- compute；
- regret。

### Experiment B：Single-Target Overinvestment

建立：

$$
A,B,C,Environment.
$$

agent 可大量分析 $B$，但 outcome 同時由 $C$ 與 environment 影響。

檢查 high-resolution $M(B)$ 是否造成 global performance 下降。

### Experiment C：Strategic Coarsening

提供 coarse、medium、fine models，比較：

$$
\boxed{
Utility-Cost Frontier.
}
$$

### Experiment D：Domain Switching

比較 no-switch、periodic、value-guided、random switching。

### Experiment E：Verification Allocation

比較 uniform、risk-weighted、uncertainty-weighted 與 NVOC-weighted verification。

### Experiment F：Human-AI Attention Allocation

提供大量 AI-generated branches，限制 human review budget，測不同 attention policy。

### Experiment G：Meta-Reasoning Regress

允許 agent 花資源「思考如何思考」，測 meta-overhead 是否爆炸。

### Experiment H：Deadline Shift

縮短 deadline，測合理策略是否自動調低不必要深度與增加 action urgency。

### Experiment I：Risk Shift

提高 tail loss，測是否對 low-probability high-impact branches 增加 counterfactual / verification budget。

### Experiment J：Amortized Reasoning

比較一次性 reasoning 與建立 reusable cognitive infrastructure 的跨任務成本。

---

# 87. Temporal Strategic Advancement

TCFT 的時代前沿不只測：

$$
\text{reasoning capability}.
$$

還可以測：

$$
\boxed{
\text{reasoning governance capability}.
}
$$

某個歷史人物未必比所有人「想得最深」，

但可能更早展現：

- selective attention；
- correct stopping；
- domain switching；
- coarse but sufficient models；
- delegation；
- uncertainty-sensitive verification。

這也可以是 temporal cognitive advancement。

---

# 88. Temporal Baseline for Strategy

因此：

$$
\boxed{
B_t^{strategy}
}
$$

必須包含同期可取得的：

- tools；
- advisers；
- institutions；
- communication；
- computational resources。

不能只比較裸人腦。

---

# 89. AI-Augmented Baseline

進入 AI 時代後：

$$
B_t^{human+AI}
$$

應成為現代 benchmark 的一部分。

如果 AI 已經可以廉價完成某種 reasoning，

那麼一個現代人的「超前」必須扣除這個工具條件。

---

# 90. Strategy Is Task-Relative

策略優劣必須 index by：

$$
\boxed{
Task,
Goal,
Risk,
Time,
Resources,
Constraints.
}
$$

不存在一個無條件固定的：

$$
\text{globally optimal reasoning depth}.
$$

---

# 91. Dynamic Strategic Invariant

高階穩定不一定是：

$$
\pi_R(t+1)=\pi_R(t).
$$

而可能是：

$$
\boxed{
I(RAG_t)
\approx
I(RAG_{t+1})
}
$$

即治理原則穩定，但資源配置動態改變。

例如：

- 高風險需要更多驗證；
- 低邊際價值停止；
- persistent failure 觸發切換。

---

# 92. 與 TCFT-05 的接口

TCFT-04 最後還沒有回答：

> 某個人很早就懂得這種資源治理，是真的超前，還是我們把今天的語言投射回去？

這需要：

$$
\boxed{
Frozen-Time Prior-Art Audit.
}
$$

以及：

$$
\boxed{
Time-Normalized Novelty.
}
$$

這就是 TCFT-05。

---

# 93. 侷限

第一，NVOC 中的效用與成本通常只能估計。

第二，機會成本高度 task-dependent。

第三，人類 cognitive effort 與 AI compute cost 不可直接等量。

第四，reasoning quality 不一定隨 compute 單調增加。

第五，meta-reasoning 本身會消耗資源。

第六，過度成本最小化可能造成 premature stopping。

第七，高風險 task 可能需要非期望值式風險準則。

第八，Strategic Coarsening 若錯用可能遮蔽必要細節。

第九，domain switching 需要維持 state consistency。

第十，本文不宣稱已找到 globally optimal reasoning allocation。

---

# 94. 結論

TCFT-01 至 TCFT-03 主要在問：

$$
\boxed{
\text{How much more can an agent think?}
}
$$

TCFT-04 第一次反過來問：

$$
\boxed{
\text{How much of that capability should actually be used?}
}
$$

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Activation}
\neq
\text{Allocation}
\neq
\text{Termination}.
}
$$

高階推理不是高階策略。

因為策略不只要求：

$$
\text{Think Deeply}.
$$

還要求：

$$
\boxed{
\text{Think at the right depth,
about the right target,
in the right domain,
for the right duration,
at the right cost.
}
}
$$

所以：

$$
\boxed{
\text{High-Resolution Local Model}
\not\Rightarrow
\text{High-Quality Global Strategy}.
}
$$

一個 agent 對單一他者的模型可以越來越精細，

但如果它把：

$$
B_{self},
B_{others},
B_{world},
B_{future}
$$

全部擠出去，

整體策略可能反而惡化。

同樣地，反事實可以繼續生成、反身性可以繼續升階、資訊可以繼續搜尋；但當：

$$
\boxed{
\operatorname{NVOC}\le0,
}
$$

繼續推理不再自動構成智慧。

真正成熟的策略能力包含：

$$
\boxed{
\text{Allocate}
+
\text{Switch}
+
\text{Coarsen}
+
\text{Verify}
+
\text{Delegate}
+
\text{Stop}.
}
$$

因此 TCFT-04 的中心命題是：

$$
\boxed{
\text{Strategic intelligence is not merely the ability to reason deeply,
but the ability to allocate, switch, coarse-grain, and stop reasoning well.}
}
$$

一個存在真正高階的地方，有時不是：

> 他能想到第十層。

而是：

> 他知道第二層已經夠了。

甚至：

> 他知道這次根本不值得把主要注意力放在這個人、這個問題或這個域。

下一篇 TCFT-05 將處理另一個必要問題：

$$
\boxed{
\text{即使某種思維看起來超前，
我們怎麼知道它在當時真的超前？}
}
$$

也就是：

$$
\boxed{
\text{Frozen-Time Prior Art}
+
\text{Temporal Baseline}
+
\text{Time-Normalized Novelty}.
}
$$

---

# References

1. Russell, S. J., & Wefald, E. H. (1991). Principles of metareasoning. *Artificial Intelligence*, 49(1–3), 361–395. DOI: 10.1016/0004-3702(91)90015-C.
2. Russell, S. J., & Wefald, E. H. (1991). *Do the Right Thing: Studies in Limited Rationality*. MIT Press.
3. Hansen, E. A., & Zilberstein, S. (2001). Monitoring and control of anytime algorithms: A dynamic programming approach. *Artificial Intelligence*, 126(1–2), 139–157. DOI: 10.1016/S0004-3702(00)00068-0.
4. Zilberstein, S. (2011). Metareasoning and bounded rationality. In M. T. Cox & A. Raja (Eds.), *Metareasoning: Thinking about Thinking*. MIT Press.
5. Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences*, 43, e1. DOI: 10.1017/S0140525X1900061X.
6. Sims, C. A. (2003). Implications of rational inattention. *Journal of Monetary Economics*, 50(3), 665–690.
7. Sims, C. A. (2006). Rational Inattention: Beyond the Linear-Quadratic Case. *American Economic Review*, 96(2), 158–163. DOI: 10.1257/000282806777212431.
8. Sims, C. A. (2010). Rational inattention and monetary economics. *Handbook of Monetary Economics*, 3, 155–181. DOI: 10.1016/B978-0-444-53238-1.00004-1.
9. Shenhav, A., Botvinick, M. M., & Cohen, J. D. (2013). The Expected Value of Control: An Integrative Theory of Anterior Cingulate Cortex Function. *Neuron*, 79(2), 217–240. DOI: 10.1016/j.neuron.2013.07.007.
10. Botvinick, M., & Braver, T. (2015). Motivation and Cognitive Control: From Behavior to Neural Mechanism. *Annual Review of Psychology*, 66, 83–113. DOI: 10.1146/annurev-psych-010814-015044.
11. Fulton, C. (2022). Choosing what to pay attention to. *Theoretical Economics*.
12. Neo.K. (2026). *內外總作用量原理：從 TOKEN 機率到世界展開成本*. EveMissLab.
13. Neo.K. (2026). *Cognitive Operator-Domain Theory (CODT) Series 01–10*. EveMissLab.
14. Neo.K. (2026). *TCFT-00｜超前認知不是預言：時代認知前沿的問題設定*. EveMissLab.
15. Neo.K. (2026). *TCFT-01｜未來底空間選擇：想像力、候選世界與問題先行*. EveMissLab.
16. Neo.K. (2026). *TCFT-02｜反事實視界：未發生世界、問題生成與認知覆蓋*. EveMissLab.
17. Neo.K. (2026). *TCFT-03｜反身性推理：當推理本身進入被推理世界*. EveMissLab.

---

# Canonical Note

本文件正式原始碼使用 UTF-8。

數學原始碼只使用 canonical delimiters：

- inline math：` $...$ `
- display math：`$$...$$`

不進行 unicode_escape 類 round-trip；不把 LaTeX 轉為 Unicode 數學字元後再作 canonical source；不以聊天 rendering view 作為正式原稿。
