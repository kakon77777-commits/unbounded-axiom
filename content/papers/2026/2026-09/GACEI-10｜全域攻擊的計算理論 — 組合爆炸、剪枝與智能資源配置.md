---
title: "GACEI-10｜全域攻擊的計算理論：組合爆炸、剪枝與智能資源配置"
title_en: "GACEI-10 | Computational Theory of Global Adversarial Testing: Combinatorial Explosion, Pruning, and Intelligent Resource Allocation"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-10"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 計算理論 / 智能資源配置 / 全域對抗計算"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "GACEI-02 MSSP 的對偶 v0.1"
  - "GACEI-03 局部攻擊抽象論 v0.1"
  - "GACEI-04 對抗記憶基底 v0.1"
  - "GACEI-05 全域攻擊組合代數 v0.1"
  - "GACEI-06 全域攻擊壓縮 v0.1"
  - "GACEI-07 一眼理解專案 v0.1"
  - "GACEI-08 工程理解不是摘要 v0.1"
  - "GACEI-09 對抗性創造與生成 v0.1"
  - "UCS 通用計算基底"
  - "AICTE AI 計算時間經濟學"
---

# GACEI-10｜全域攻擊的計算理論
## 組合爆炸、剪枝與智能資源配置

**英文題名：** Computational Theory of Global Adversarial Testing: Combinatorial Explosion, Pruning, and Intelligent Resource Allocation

---

## 摘要

GACEI-01 至 GACEI-09 已建立全域對抗計算所需的主要語義構件：project-level global attention、engineering understanding、attack abstraction、persistent adversarial memory、attack composition、global compression、bounded novelty 與 executable adversarial generation。然而，這些能力若沒有真正的計算資源模型，仍可能停留在概念層。因為即使 AI 已經知道：

- 哪些 attack 值得測；
- 哪些 attack 可組合；
- 哪些 residual gap 值得創造；
- 哪些 interaction 具有高風險；

它仍必須面對有限的：

$$
\boxed{
\text{Memory}
+
\text{Compute}
+
\text{Addressing}
+
\text{Bandwidth}
+
\text{Parallelism}
+
\text{I/O}
+
\text{Verification}
+
\text{Human Governance}.
}
$$

本文因此提出「全域對抗計算資源論」（Computational Theory of Global Adversarial Testing），把 GACEI 的 attack planning 與執行正式放進有限計算基底。

本文承接既有 UCS 的通用計算基底，定義對抗計算實現向量：

$$
\boxed{
\mathfrak B_A
=
\left(
\mathcal S,
\mathcal C,
\mathcal A,
\mathcal B,
\mathcal P,
\mathcal D,
\mathcal{IO},
\mathcal V
\right),
}
$$

其中：

- $\mathcal S$：state / memory capacity；
- $\mathcal C$：state-transition / raw compute；
- $\mathcal A$：addressing / retrieval；
- $\mathcal B$：bandwidth / communication；
- $\mathcal P$：parallel realization；
- $\mathcal D$：durability / persistence；
- $\mathcal{IO}$：tool and environment I/O；
- $\mathcal V$：verification / comparison capacity。

同時承接 AICTE，定義實際可調度 AI 預算：

$$
\boxed{
\mathbf B_A
=
\left(
B_{\mathrm{token}},
B_{\mathrm{compute}},
B_{\mathrm{context}},
B_{\mathrm{tool}},
B_{\mathrm{parallel}},
B_{\mathrm{runtime}},
B_{\mathrm{money}},
B_{\mathrm{human}}
\right).
}
$$

本文的第一個核心命題是：

$$
\boxed{
\text{Potential AI Capability}
\neq
\text{Allocated AI Capability}
\neq
\text{Realized Adversarial Throughput}.
}
$$

一個模型即使具有很強的工程理解與創造能力，如果 context 不足、memory retrieval 太慢、tool calls 過少、sandbox runtime 太貴、parallel slots 不足或 verification reserve 被耗盡，仍可能無法完成高品質 global campaign。

本文進一步處理 attack-space combinatorial explosion。若 candidate attacks 為：

$$
A
=
\{a_1,\ldots,a_n\},
$$

只考慮 subset 已有：

$$
2^n
$$

種可能；若再考慮有序執行與 higher-order interaction，候選空間可更大。因此 brute-force global testing 一般不可作為預設方法。

本文提出：

$$
\boxed{
\text{Architecture Understanding}
\rightarrow
\text{Search-Space Compression}
}
$$

以及：

$$
\boxed{
\text{Attack Memory}
\rightarrow
\text{Rediscovery Compression}.
}
$$

也就是透過 project model、invariant map、state ownership、dependency path、history、known interaction relation 與 coverage residual，先剪除不相關或低價值候選，再把昂貴前沿算力留給真正需要新推理的 residual space。

本文提出四層 compute allocation：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Reason}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}.
}
$$

並把總預算拆成：

$$
B
=
B_O
+
B_R
+
B_E
+
B_V,
$$

其中：

- $B_O$：observation budget；
- $B_R$：reasoning / synthesis budget；
- $B_E$：execution budget；
- $B_V$：verification / diagnosis reserve。

本文特別要求：

$$
\boxed{
B_V>0.
}
$$

也就是任何 global campaign 都不能把全部資源耗在 attack generation 或 execution，最後卻沒有足夠資源判斷結果。

本文進一步定義「有效對抗計算」：

$$
\boxed{
C_{\mathrm{eff}}^{adv}
=
F(
\mathfrak B_A,
\mathbf B_A,
Q_P,
Q_M,
Q_V,
G
),
}
$$

其中 $Q_P$ 為 project model quality， $Q_M$ 為 adversarial memory quality， $Q_V$ 為 validator quality， $G$ 為當前目標與風險函數。這表示 raw FLOPS 或 token budget 不是單一決定因素。

本文最後提出一個資源調度目標：

$$
\boxed{
\pi^\ast
=
\arg\max_{\pi}
\frac{
E[
\Delta
(
Coverage
+
RiskResolution
+
InformationGain
+
KnowledgeGain
)
]
}{
E[
Cost(\pi)
]
+
\epsilon
}.
}
$$

其中 $\pi$ 是一個跨 observation、reasoning、execution、verification、parallelism 與 model-tier 的動態 allocation policy。

因此，GACEI-10 的核心不是「讓 AI 算得更多」，而是：

$$
\boxed{
\text{讓有限智能計算被配置到最能改變全域工程判斷的位置。}
}
$$

這才是未來 AI 可以「一口氣做全域對抗測試」的真正計算前提。

**關鍵詞：** Global Adversarial Compute、UCS、AICTE、Compute Allocation、Combinatorial Explosion、Pruning、Verification Reserve、Memory Bandwidth、Addressing、Parallelism、AI 工程智能、GACEI

---

# 0. 研究定位與安全範圍

本文研究：

$$
\boxed{
\text{Authorized Adversarial Test Compute Allocation}.
}
$$

所有執行對象僅限：

- synthetic systems；
- sandbox；
- isolated copies；
- authorized repositories；
- internal testbeds。

本文不處理如何降低未授權現實攻擊的計算成本。

---

# 1. 為什麼 GACEI 最後一定會撞到計算理論？

因為前面所有能力都要被實現。

例如：

$$
\text{Creativity}
$$

需要 reasoning。

$$
\text{Generation}
$$

需要 program synthesis。

$$
\text{Global Campaign}
$$

需要 execution。

$$
\text{Verification}
$$

需要 compare / replay / validator。

因此：

$$
\boxed{
\text{Cognitive Design}
\neq
\text{Physical Realization}.
}
$$

---

# 2. 通用計算基底

本文承接：

$$
\boxed{
\mathfrak B_A
=
(
\mathcal S,
\mathcal C,
\mathcal A,
\mathcal B,
\mathcal P,
\mathcal D,
\mathcal{IO},
\mathcal V
).
}
$$

---

# 3. State Capacity $\mathcal S$

對 global campaign，memory 不只是：

> model context。

還包括：

- project model；
- attack memory；
- snapshots；
- traces；
- validator outputs；
- campaign state；
- provenance。

---

# 4. Raw Compute $\mathcal C$

包括：

- model inference；
- static analysis；
- symbolic analysis；
- graph operations；
- test execution；
- simulation；
- diff；
- program synthesis。

---

# 5. Addressing $\mathcal A$

大量 attack memory：

$$
|K_A|\gg1
$$

若無法快速定位 relevant attacks，

則：

$$
K_A
$$

越大反而越慢。

所以：

$$
\boxed{
\text{Memory Capacity}
\neq
\text{Usable Memory}.
}
$$

---

# 6. Bandwidth $\mathcal B$

包括：

- model-to-tool；
- agent-to-agent；
- memory-to-model；
- trace upload；
- artifact transfer。

---

# 7. Parallelism $\mathcal P$

global campaign 可以：

- parallel observations；
- isolated attack lanes；
- parallel validators；
- parallel reconstruction。

但：

$$
\boxed{
\text{Parallelizable}
\neq
\text{Independent}.
}
$$

---

# 8. Durability $\mathcal D$

需要保存：

- attack history；
- interrupted campaign；
- partial evidence；
- model state；
- receipts。

---

# 9. I/O $\mathcal{IO}$

包括：

- filesystem；
- build tools；
- sandbox；
- test runner；
- database；
- browser；
- formal verifier。

---

# 10. Verification Capacity $\mathcal V$

包括：

- diff；
- oracle；
- A/B；
- hidden tests；
- replay；
- formal checks；
- provenance validation。

---

# 11. AI 可調度預算

$$
\boxed{
\mathbf B_A
=
(
B_t,
B_c,
B_x,
B_u,
B_p,
B_r,
B_m,
B_h
).
}
$$

---

# 12. Token Budget $B_t$

不是只是輸出長度。

它代表：

- reasoning；
- planning；
- synthesis；
- critique；
- explanation。

---

# 13. Compute Budget $B_c$

模型與機械計算總資源。

---

# 14. Context Budget $B_x$

AI 同時可持有多少 project state。

---

# 15. Tool Budget $B_u$

能呼叫多少：

- test；
- shell；
- analyzer；
- validator。

---

# 16. Parallel Budget $B_p$

同時多少 workers / lanes。

---

# 17. Runtime Budget $B_r$

campaign 可跑多久。

---

# 18. Monetary Budget $B_m$

API、cloud、sandbox、hardware 成本。

---

# 19. Human Budget $B_h$

人類：

- review；
- authorization；
- decision；
- dispute resolution。

---

# 20. 潛在能力與實現能力

定義：

$$
C_{AI}^{pot}
$$

為模型潛在能力。

實際配置：

$$
C_{AI}^{alloc}
=
Allocate(
C_{AI}^{pot},
\mathbf B_A
).
$$

實際產出：

$$
Y^{adv}
=
F(
C_{AI}^{alloc},
\mathfrak B_A,
K_A,
\widehat{\mathfrak P},
V
).
$$

---

# 21. 三層不能混

$$
\boxed{
C_{AI}^{pot}
\neq
C_{AI}^{alloc}
\neq
Y^{adv}.
}
$$

---

# 22. Attack Space Explosion

若：

$$
n
$$

個 attacks，

subset：

$$
2^n.
$$

---

# 23. Ordering Explosion

長度 $k$ 的有序選擇：

$$
P(n,k)
=
\frac{n!}{(n-k)!}.
$$

---

# 24. Higher-Order Interaction

pair：

$$
{n\choose2}
$$

三元：

$$
{n\choose3}
$$

一直到：

$$
{n\choose n}.
$$

---

# 25. Brute Force 不是預設答案

即使 GPU 很強，

也可能：

$$
C_{\mathrm{raw}}\uparrow
$$

但：

$$
C_{\mathrm{effective}}
$$

被：

- memory；
- I/O；
- tool；
- synchronization；

限制。

---

# 26. Attack-Space Pruning

本文提出：

$$
\boxed{
A
\rightarrow
A_{\mathrm{eligible}}
\rightarrow
A_{\mathrm{relevant}}
\rightarrow
A_{\mathrm{high-value}}
\rightarrow
\mathcal C^\ast.
}
$$

---

# 27. Eligibility Pruning

先刪：

- unauthorized；
- stale；
- NotApplicable；
- invalid；
- unrecoverable。

---

# 28. Structural Pruning

利用：

$$
\widehat{\mathfrak P}.
$$

刪除沒有 causal relation 的 interaction candidates。

---

# 29. Memory Pruning

已知：

$$
LOW\_VALUE,
FALSE\_POSITIVE,
DEPRECATED
$$

可降權。

---

# 30. Coverage Pruning

若 attack：

$$
a
$$

對目前 campaign：

$$
\Delta Cov(a)\approx0,
$$

降權。

---

# 31. Information Pruning

若：

$$
\Delta IG(a)\approx0,
$$

降權。

---

# 32. Diagnostic Pruning

如果：

$$
DiagLoss(a)
$$

過高，

拆 lane 或 defer。

---

# 33. Architecture Understanding as Computational Compression

如果 AI 理解：

$$
G_S,
$$

就可以知道：

$$
a_i
$$

和：

$$
a_j
$$

是否存在 interaction path。

因此：

$$
\boxed{
\text{Understanding}
\rightarrow
\text{Fewer Candidate Computations}.
}
$$

---

# 34. Memory as Computational Compression

若 attack 已知：

$$
a\in K_A,
$$

不再支付：

$$
C_{\mathrm{discover}}.
$$

只支付：

$$
C_{\mathrm{retrieve}}
+
C_{\mathrm{instantiate}}.
$$

---

# 35. Known / Unknown Compute Split

$$
\boxed{
B_R
=
B_R^{known}
+
B_R^{novel}.
}
$$

理想：

$$
B_R^{known}\downarrow
$$

隨 memory 成熟。

---

# 36. Observation / Reason / Execute / Verify

總流程預算：

$$
\boxed{
B
=
B_O
+
B_R
+
B_E
+
B_V.
}
$$

---

# 37. Observation Budget $B_O$

用於：

- project model；
- missing uncertainty；
- targeted probes。

---

# 38. Reasoning Budget $B_R$

用於：

- attack selection；
- novelty；
- composition；
- diagnosis hypothesis。

---

# 39. Execution Budget $B_E$

用於：

- sandbox；
- test；
- replay；
- interaction lane。

---

# 40. Verification Budget $B_V$

用於：

- validator；
- A/B；
- counterfactual；
- provenance；
- confirmation。

---

# 41. Verification Reserve

$$
\boxed{
B_V>0.
}
$$

任何 campaign 若：

$$
B_E=B
$$

而：

$$
B_V=0,
$$

幾乎等於：

> 只做實驗，不留資源判斷。

---

# 42. Dynamic Budget Allocation

不同專案：

$$
(B_O,B_R,B_E,B_V)
$$

不同。

---

# 43. 熟悉架構

若：

$$
Q_P\gg0,
$$

可降低：

$$
B_O.
$$

---

# 44. 新架構

若：

$$
Q_P
$$

低，

提高：

$$
B_O,B_R.
$$

---

# 45. 已知 attack-heavy

提高：

$$
B_E,
$$

降低：

$$
B_R^{novel}.
$$

---

# 46. Validator-weak

提高：

$$
B_V.
$$

---

# 47. Marginal Intelligent Compute Value

對候選計算行動：

$$
c_i,
$$

定義：

$$
\boxed{
MIV(c_i)
=
\frac{
E[
\Delta V_{\mathrm{intent}}(c_i)
]
}{
E[
\Delta Cost(c_i)
]
+
\epsilon
}.
}
$$

---

# 48. 對抗專用 MIV

$$
MIV_A(c)
=
\frac{
E[
\Delta Coverage
+
\Delta RiskResolution
+
\Delta Knowledge
+
\Delta DiagnosticQuality
]
}{
E[
\Delta Cost
]
+\epsilon
}.
$$

---

# 49. Shadow Price

若：

$$
MIV_A(c)
<
\lambda_B,
$$

則：

$$
c
\rightarrow
Defer.
$$

---

# 50. Compute Policy

定義：

$$
\pi:
State
\rightarrow
Action.
$$

---

# 51. State

包含：

$$
(
\widehat{\mathfrak P},
K_A,
Coverage,
Residual,
Evidence,
Budget
).
$$

---

# 52. Action

可以是：

```text
OBSERVE
RETRIEVE
REASON
GENERATE
EXECUTE
VERIFY
REPLAY
STOP
```

---

# 53. Optimal Policy

$$
\boxed{
\pi^\ast
=
\arg\max_{\pi}
\frac{
E[
\Delta(
Coverage+
RiskResolution+
InformationGain+
KnowledgeGain
)
]
}{
E[
Cost(\pi)
]
+\epsilon
}.
}
$$

---

# 54. Policy 不一定可精確求最優

真實系統：

- stochastic；
- partially observed；
- non-stationary；
- open denominator。

所以多半需要 heuristic / adaptive policy。

---

# 55. POMDP 類比

可以把 campaign 看成部分可觀測決策問題。

但本文不宣稱所有 GACEI runtime 都應 formalize 為 POMDP。

---

# 56. Adaptive Test-Time Compute

不同 attack hypothesis 不應分配相同 reasoning。

---

# 57. Easy Known Attack

$$
B_R(a)\downarrow.
$$

---

# 58. Novel High-Risk Attack

$$
B_R(a)\uparrow.
$$

---

# 59. Uniform Reasoning 不是最優

$$
\boxed{
\text{Uniform Compute}
\neq
\text{Optimal Compute}.
}
$$

---

# 60. Model Tier Routing

不同任務可用不同模型。

例如：

- cheap model：retrieval / known replay；
- strong model：novel attack synthesis；
- deterministic tool：validator；
- formal tool：critical proof obligation。

---

# 61. Capability Matching

定義：

$$
ModelFit(m,t).
$$

不必所有 task 都用 frontier model。

---

# 62. Frontier Compute Reserve

$$
B_F
$$

專門留給：

- residual unknown；
- high-risk ambiguity；
- new architecture；
- failed localization。

---

# 63. Cheap Known Work

已知 attack instantiation 可：

$$
\text{low-cost model}
+
\text{deterministic tool}.
$$

---

# 64. 高能力模型真正該做什麼？

$$
\boxed{
\text{Unknown Structure}
+
\text{Novel Hypothesis}
+
\text{Ambiguous Diagnosis}.
}
$$

---

# 65. Parallelism

可以：

$$
a_1\otimes a_2\otimes\cdots
$$

在 isolated lanes。

---

# 66. Parallel Speedup

理想：

$$
T_p
\approx
\frac{T_1}{p}.
$$

但實際有：

- setup；
- I/O；
- synchronization；
- shared validator；
- memory contention。

---

# 67. Amdahl 類限制

若不可並行部分比例：

$$
s,
$$

最大 speedup：

$$
Speedup(p)
\le
\frac1{
s+\frac{1-s}{p}
}.
$$

這裡只是結構類比，不表示所有 campaign 都嚴格符合。

---

# 68. Parallelism 也可能增加診斷成本

$$
p\uparrow
$$

可能：

$$
TraceComplexity\uparrow.
$$

---

# 69. 所以需要 Lane Isolation

每個 lane：

- baseline id；
- attack ids；
- validator；
- snapshot；
- provenance。

---

# 70. Agent Parallelism

多 AI agents 可並行：

- observe；
- synthesize；
- validate。

---

# 71. 但多 Agent 不是免費

增加：

- coordination；
- duplicate work；
- communication；
- merge cost。

---

# 72. Coordination Cost

$$
C_{\mathrm{coord}}
=
f(
n,
shared_state,
handoffs,
conflicts
).
$$

---

# 73. Role Collapse 的計算浪費

如果多 agents 全部做同一件事：

$$
\text{Redundant Reasoning}\uparrow.
$$

---

# 74. Authority Topology

不同 Agent 應有不同：

- objective；
- authority；
- stop rights。

否則並行只變重複。

---

# 75. Memory Bandwidth

attack memory 若很大：

$$
K_A
$$

的 retrieval 本身可能成 bottleneck。

---

# 76. Retrieval Index

需要：

- semantic id；
- structural signature；
- family；
- relation；
- version；
- risk。

---

# 77. Search Cost

若：

$$
T_A(N)=O(N),
$$

大型 memory 很快失效。

---

# 78. Indexed Retrieval

理想：

$$
T_A(N)\ll O(N)
$$

對主要 query。

---

# 79. Address Construction Barrier

即使 memory 裡有答案，

AI 若不知道查哪裡，

仍需昂貴解析。

---

# 80. 因此 Query Construction 也是計算

$$
q
\rightarrow
address
$$

不是免費。

---

# 81. Structural Query

由：

$$
\widehat{\mathfrak P}
$$

產生：

$$
q_{\mathrm{struct}}.
$$

---

# 82. Memory Hit

$$
Retrieve(q_{\mathrm{struct}})
\rightarrow
A_{\mathrm{known}}.
$$

---

# 83. Cache of Attack Plans

相似 project 可保存：

$$
PlanTemplate.
$$

---

# 84. 但 plan 不應直接重播

必須：

$$
Rebind(
ProjectVersion,
Auth,
Coverage,
Risk
).
$$

---

# 85. Compute Reuse

可重用：

- attack templates；
- interaction relations；
- validator；
- fixture generator；
- campaign skeleton。

---

# 86. Reuse 不等於 stale reuse

版本差異：

$$
\Delta_V
$$

大時，必須 revalidate。

---

# 87. Checkpointing

長 campaign 應保存：

$$
Checkpoint_t
=
(
Plan,
Evidence,
Budget,
Residual,
MemoryDelta
).
$$

---

# 88. Resume

可以：

$$
Checkpoint_t
\rightarrow
Campaign_{t+1}.
$$

避免 context loss 從零開始。

---

# 89. Persistent State

這直接利用：

$$
\mathcal D.
$$

---

# 90. Verification Throughput

若 execution rate：

$$
\lambda_E
$$

高於 verification rate：

$$
\lambda_V,
$$

則形成：

$$
\boxed{
\text{Verification Backlog}.
}
$$

---

# 91. Backlog Growth

$$
\frac{dQ}{dt}
=
\lambda_E-\lambda_V.
$$

若：

$$
\lambda_E>\lambda_V,
$$

未驗證 evidence queue 增長。

---

# 92. 所以不能只擴 attack generation

否則：

$$
\text{Evidence Debt}\uparrow.
$$

---

# 93. Verification Reserve Policy

要求：

$$
\lambda_V
\ge
\alpha\lambda_E
$$

對某最低 $\alpha$。

---

# 94. Critical Evidence Priority

高風險 finding 優先 verification。

---

# 95. Evidence Queue

可以按：

$$
Priority(e)
=
Risk
\times
Uncertainty
\times
ClaimImpact.
$$

排序。

---

# 96. Compute Waste Types

本文定義第一版：

$$
W_C
=
W_{\mathrm{rediscovery}}
+
W_{\mathrm{redundancy}}
+
W_{\mathrm{overread}}
+
W_{\mathrm{oververify}}
+
W_{\mathrm{idle}}
+
W_{\mathrm{coord}}.
$$

---

# 97. Rediscovery Waste

重新想到已知 attack。

---

# 98. Redundancy Waste

多 agents 做相同工作。

---

# 99. Overread Waste

已 ObsEnough 仍一直讀。

---

# 100. Oververify Waste

claim 已足夠仍無限 meta-verification。

---

# 101. Idle Waste

compute 因 I/O / memory bottleneck 等待。

---

# 102. Coordination Waste

多 agent handoff 過度。

---

# 103. Effective Compute Efficiency

$$
\boxed{
ECE
=
\frac{
UsefulDecisionChangingCompute
}{
TotalCompute+\epsilon
}.
}
$$

---

# 104. Global Adversarial Efficiency

$$
GAE
=
\frac{
WeightedCoverage
+
RiskResolved
+
KnowledgeGain
}{
ComputeCost
+
HumanCost
+
RuntimeCost
+
\epsilon
}.
$$

---

# 105. 更高額度不一定更高效率

$$
B\uparrow
$$

不保證：

$$
GAE\uparrow.
$$

---

# 106. Diminishing Return

可能：

$$
\frac{\partial^2Y}{\partial B^2}<0.
$$

---

# 107. Negative Return

過度驗證甚至可能：

$$
\frac{\partial Y}{\partial B}<0.
$$

例如：

- 延誤 release；
- 增加錯誤修改；
- context drift。

---

# 108. Stop Policy

若：

$$
MIV_A<\lambda_B
$$

持續數輪，

停止。

---

# 109. Stop 不是失敗

是資源最佳化。

---

# 110. Reopen Policy

只有：

$$
\Delta Risk
+
\Delta Claim
+
\Delta EvidenceNeed
$$

足夠大才 reopen。

---

# 111. Resource Profile

本文提出三種：

## Fast

$$
B_O,B_R,B_E,B_V
$$

低，覆蓋高風險核心。

## Standard

平衡。

## Deep

高 interaction、recovery、validator、novelty。

---

# 112. Profile 是 budget policy

不是固定 attack list。

---

# 113. Commercial Software

可能更重：

- data；
- payment；
- account；
- persistence；
- recovery。

---

# 114. Research Architecture

可能更重：

- invariant；
- novel attack；
- structural coverage；
- falsification。

---

# 115. MSSP Example

MSSP App 已有大量 known attacks。

理想：

$$
B_R^{known}\downarrow,
$$

$$
B_E^{known}
$$

自動化，

$$
B_R^{novel}
$$

只投 residual。

---

# 116. 這就是把前面地獄笑話變成資產

以前三個 AI 每次重想 attack。

未來：

$$
\boxed{
\text{Think Once}
\rightarrow
\text{Store}
\rightarrow
\text{Retrieve Cheaply}.
}
$$

---

# 117. AI 原生計算

傳統 test system：

$$
Algorithm
\rightarrow
Execution.
$$

未來 GACEI：

$$
\boxed{
AI
\rightarrow
Model
\rightarrow
Select
\rightarrow
Generate
\rightarrow
Allocate
\rightarrow
Execute
\rightarrow
Verify.
}
$$

---

# 118. 計算機理論的改變

重點從：

> 能不能算？

增加成：

> 哪些狀態值得算？

---

# 119. Realization vs Cognitive Intervention

承接 UCS：

$$
\boxed{
\mathfrak A
=
\mathfrak B
\otimes
\mathfrak I.
}
$$

其中：

- $\mathfrak B$：realization substrate；
- $\mathfrak I$：cognitive intervention policy。

---

# 120. 全域攻擊 AI 的真正優勢

不是：

$$
C_{\mathrm{raw}}\gg
$$

而是：

$$
\boxed{
\text{better selection of what to compute}.
}
$$

---

# 121. Computational Attention

可以把 attention 理解成：

$$
\boxed{
\text{Compute Allocation over State Space}.
}
$$

---

# 122. Attention / Compute Duality

注意力選：

> 哪裡值得看。

計算選：

> 哪裡值得變換。

---

# 123. Addressing / Attention Coupling

如果 attention 選中：

$$
g,
$$

但 memory addressing 找不到 relevant knowledge，

注意力無法轉成 action。

---

# 124. Generation / Compute Coupling

AI 生成：

$$
10^4
$$

候選，

但 execution budget 只有：

$$
100,
$$

必須 selection。

---

# 125. Verification / Compute Coupling

如果 validator 很貴，

可能值得先跑 cheap proxy。

---

# 126. Multi-Fidelity Verification

$$
V_0
\rightarrow
V_1
\rightarrow
V_2.
$$

例如：

- static gate；
- unit sandbox；
- deep replay。

---

# 127. Escalation Only When Needed

只有：

$$
V_0
$$

有疑義才：

$$
V_1.
$$

---

# 128. Compute Cascades

這形成：

$$
\boxed{
\text{cheap filter}
\rightarrow
\text{medium validation}
\rightarrow
\text{expensive confirmation}.
}
$$

---

# 129. Asymmetric Compute

不必對所有 attack 同樣深。

---

# 130. High-Risk / Low-Confidence

最值得 deep compute。

---

# 131. Low-Risk / High-Confidence

cheap replay 即可。

---

# 132. Compute Map

可以建立：

$$
M_C(u)
$$

表示 coverage unit $u$ 的預算配置。

---

# 133. Risk Map

$$
M_R(u).
$$

---

# 134. Uncertainty Map

$$
M_U(u).
$$

---

# 135. Combined Allocation

$$
B(u)
\propto
M_R(u)
M_U(u)
M_I(u),
$$

其中 $M_I$ 表示 expected information gain。

---

# 136. 不應完全線性

實作可用 ranking / learned policy。

---

# 137. Compute Scheduling

若 tasks：

$$
T
=
\{t_1,\ldots,t_n\},
$$

每個有：

- cost；
- dependency；
- value；
- deadline。

這變成 scheduling problem。

---

# 138. Precedence Constraint

$$
t_i\prec t_j.
$$

---

# 139. Parallel Constraint

$$
t_i\parallel t_j.
$$

---

# 140. Resource Constraint

$$
\sum_i
resource_i
\le B.
$$

---

# 141. Verification Dependency

finding：

$$
f_i
$$

不能 promotion 前：

$$
V(f_i)=Pass.
$$

---

# 142. Memory Commit Dependency

$$
Verify
\prec
PromoteMemory.
$$

---

# 143. Attack Generation Dependency

$$
ObsEnough
\prec
NovelSynthesis
$$

一般成立。

---

# 144. 但 emergency probe 可例外

若重大 failure 已明顯，

不必等完整 model。

---

# 145. Compute Governance

任何自動 planner 都需要：

- max budget；
- authorization；
- stop；
- escalation；
- audit。

---

# 146. Cost Ceiling

$$
Cost(\pi)\le B_{\max}.
$$

---

# 147. Time Ceiling

$$
Time(\pi)\le T_{\max}.
$$

---

# 148. Parallel Ceiling

$$
Workers\le P_{\max}.
$$

---

# 149. Human Escalation

若：

$$
Risk
>
\tau_H
$$

且：

$$
Uncertainty
>
\tau_U,
$$

交給 human review。

---

# 150. Human Budget 也有限

所以不能所有 edge case 都 escalated。

---

# 151. Escalation Value

$$
EV_H
=
\frac{
ExpectedDecisionImprovement
}{
HumanTime+\epsilon
}.
$$

---

# 152. 最後人類也進同一資源經濟

這與 AICTE 一致。

---

# 153. Benchmark：Compute Allocation

給同一：

- project；
- attack memory；
- hidden defects；
- total budget。

比較：

### A：Uniform

平均資源。

### B：Brute Force

盡量多跑。

### C：Risk-only

只看 severity。

### D：GACEI Compute Policy

memory + risk + uncertainty + info + verification reserve。

---

# 154. 測量

$$
WeightedDefectRecall,
$$

$$
Coverage,
$$

$$
NovelUsefulFindings,
$$

$$
VerificationBacklog,
$$

$$
ComputeCost,
$$

$$
WallClock,
$$

$$
HumanCost,
$$

$$
KnowledgeGain.
$$

---

# 155. Frontier Compute Efficiency

$$
FCE
=
\frac{
NovelHighValueFindings
}{
FrontierModelCompute+\epsilon
}.
$$

---

# 156. Known Compute Efficiency

$$
KCE
=
\frac{
KnownCoverage
}{
KnownWorkCompute+\epsilon
}.
$$

---

# 157. Verification Efficiency

$$
VE
=
\frac{
CorrectlyResolvedClaims
}{
VerificationCompute+\epsilon
}.
$$

---

# 158. Observation Efficiency

沿用：

$$
OE
=
\frac{
ProjectModelQuality
}{
ObservationCost+\epsilon
}.
$$

---

# 159. Total System Efficiency

$$
\boxed{
TSE
=
f(
OE,
KCE,
FCE,
VE,
WallClock,
HumanCost
).
}
$$

---

# 160. 研究假說

## H1：Architecture-guided pruning 降低 compute cost

在 defect recall 接近時：

$$
C_{\mathrm{guided}}
<
C_{\mathrm{bruteforce}}.
$$

## H2：Memory-assisted attack selection 降低 frontier-model usage

$$
B_F^{memory}
<
B_F^{scratch}.
$$

## H3：Verification reserve 降低 unresolved evidence backlog

$$
Q_{\mathrm{backlog}}
\downarrow.
$$

## H4：Adaptive compute allocation 優於 uniform budget

$$
Utility_{\mathrm{adaptive}}
>
Utility_{\mathrm{uniform}}
$$

在有限 budget benchmark 中成立。

## H5：過度平行化存在負收益區

存在：

$$
p^\ast
$$

使：

$$
p>p^\ast
\Rightarrow
GAE\downarrow.
$$

---

# 161. 本文非主張

本文不主張：

1. raw FLOPS 不重要；
2. token 可以完全代表 compute；
3. 所有 attack planning 都能精確求最優；
4. 所有 project 都可同一 allocation policy；
5. parallelism 越高越好；
6. memory 越大越好；
7. retrieval 一定是 $O(\log N)$ ；
8. POMDP 是 GACEI 唯一 formalism；
9. 所有 verification 都需要 frontier model；
10. 所有 known attack 都可以 cheap model 處理；
11. human governance 可以完全自動化；
12. compute 更多一定提高 coverage；
13. more agents 一定提高效率；
14. global adversarial computation 可以證明無未知缺陷；
15. 所有 cost 都能轉換成單一貨幣；
16. 本文方法可用於未授權第三方系統攻擊資源最佳化。

本文主張的是：

$$
\boxed{
\text{全域對抗計算必須被視為有限資源下的智能計算配置問題。}
}
$$

---

# 162. 與 GACEI-09 的關係

GACEI-09 回答：

$$
\boxed{
\text{AI 如何創造與生成新的 attack？}
}
$$

本文回答：

$$
\boxed{
\text{當已知與新 attack 都很多時，哪些值得真的花計算資源？}
}
$$

---

# 163. 與 UCS 的關係

UCS 區分：

$$
\text{Realization Capacity}
\neq
\text{Cognitive Intervention Capacity}.
$$

本文把這一區分直接應用到 adversarial engineering。

---

# 164. 與 AICTE 的關係

AICTE 提出：

$$
MIV
=
\frac{
E[\Delta V]
}{
E[\Delta C]+\epsilon
}.
$$

本文把它收斂為 attack observation、reasoning、execution、verification 的配置規則。

---

# 165. 下一篇：缺陷表面與多維攻擊覆蓋

GACEI-11 將回答：

> 算完之後，我們到底觀察到了什麼？

核心將正式建立：

$$
\boxed{
\text{Defect Surface}
+
\text{A/B}
+
\text{Validator}
+
\text{Alarm}
+
\text{Blind Spot}
+
\text{Multidimensional Coverage}.
}
$$

---

# 166. 結論

未來 AI 若要做到：

> 看一眼整個專案，然後一口氣生成並執行全域 adversarial campaign，

真正限制它的並不只有模型 intelligence。

它還需要：

$$
\boxed{
\text{Memory}
+
\text{Addressing}
+
\text{Compute}
+
\text{Bandwidth}
+
\text{Parallelism}
+
\text{I/O}
+
\text{Verification}
+
\text{Governance}.
}
$$

更重要的是，這些資源不能平均亂撒。

真正高階的 AI 工程計算能力在於：

$$
\boxed{
\text{知道下一單位計算應該花在哪裡。}
}
$$

已知 attack：

$$
\rightarrow
\text{cheap retrieval / replay}.
$$

未知 residual：

$$
\rightarrow
\text{frontier reasoning}.
$$

高風險 ambiguous finding：

$$
\rightarrow
\text{verification reserve}.
$$

低價值重複：

$$
\rightarrow
\text{stop}.
$$

因此本文將全域對抗計算的計算核心壓縮為：

$$
\boxed{
\text{Global Intelligence}
=
\text{Global Selection of Finite Computation}.
}
$$

不是：

$$
\boxed{
\text{Infinite Computation}.
}
$$

這正是從「AI 很會想」走向「AI 能有效率地完成整個工程世界模型中的高價值計算」的關鍵一步。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
