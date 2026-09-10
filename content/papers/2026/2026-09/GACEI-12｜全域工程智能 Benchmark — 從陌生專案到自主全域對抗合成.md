---
title: "GACEI-12｜全域工程智能 Benchmark：從陌生專案到自主全域對抗合成"
title_en: "GACEI-12 | Global Engineering Intelligence Benchmark: From Unseen Projects to Autonomous Global Adversarial Synthesis"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-12"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / Benchmark 設計 / AI 工程智能 / 全域對抗合成"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software analysis and testing only"
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
  - "GACEI-10 全域攻擊的計算理論 v0.1"
  - "GACEI-11 缺陷表面與多維攻擊覆蓋 v0.1"
---

# GACEI-12｜全域工程智能 Benchmark
## 從陌生專案到自主全域對抗合成

**英文題名：** Global Engineering Intelligence Benchmark: From Unseen Projects to Autonomous Global Adversarial Synthesis

---

## 摘要

GACEI-01 至 GACEI-11 已分別建立：

- 全域對抗計算；
- MSSP 對抗對偶；
- 局部攻擊抽象；
- SEDB-style 對抗記憶；
- attack composition；
- global attack compression；
- project-level global attention；
- adversarial engineering understanding；
- adversarial creativity / generation；
- intelligent compute allocation；
- defect surface / detectability / diagnosability / multidimensional coverage。

如果這些理論只停留在概念層，仍然無法回答一個最重要的問題：

> 未來 AI 到底有沒有真的具備「看懂整個陌生專案，自己設計一套高價值全域對抗程序，再把結果驗證、定位、學會」的能力？

本文提出「全域工程智能 Benchmark」（Global Engineering Intelligence Benchmark, GEIB），把 GACEI 系列收束成一套可實驗、可比較、可重播的 AI 工程能力評測框架。

GEIB 的核心任務不是：

> 給 AI 一個 bug ticket，看它能不能修掉。

而是：

$$
\boxed{
\text{Unseen Project}
\rightarrow
\text{Global Project Model}
\rightarrow
\text{Known Attack Retrieval}
\rightarrow
\text{Residual Discovery}
\rightarrow
\text{Novel Attack Synthesis}
\rightarrow
\text{Global Campaign}
\rightarrow
\text{Execution}
\rightarrow
\text{Defect Surface}
\rightarrow
\text{Localization}
\rightarrow
\text{Learning}.
}
$$

本文定義 AI 的全域工程智能能力向量：

$$
\boxed{
\mathcal C_{GEI}
=
(
A,
U,
R,
C,
G,
K,
V,
L,
M
),
}
$$

其中：

- $A$：Global Attention；
- $U$：Engineering Understanding；
- $R$：Resolution / Parsing；
- $C$：Adversarial Creativity；
- $G$：Executable Generation；
- $K$：Computation / Planning；
- $V$：Verification；
- $L$：Localization；
- $M$：Memory / Learning。

本文特別反對把上述能力壓成單一「智能分數」。一個 AI 可能 attention 高但 verification 低；也可能 generation 高但 creativity 低；也可能 defect recall 高但 localization 幾乎無效。因此 GEIB 以 vector score、profile、cost-efficiency、transfer 與 calibration 為主要輸出。

Benchmark 給定：

$$
\boxed{
P_{\mathrm{unknown}}
}
$$

作為 AI 從未見過的授權 synthetic / isolated project，並限制：

$$
B_O
=
\text{Observation Budget},
$$

$$
B_R
=
\text{Reasoning Budget},
$$

$$
B_E
=
\text{Execution Budget},
$$

$$
B_V
=
\text{Verification Budget}.
$$

另提供一部分已知 adversarial memory：

$$
K_A,
$$

但隱藏：

- project-specific architecture facts；
- 部分 invariants；
- hidden defects；
- hidden interaction failures；
- validator blind spots；
- benchmark-defined novel failure families。

因此 AI 必須同時展現：

$$
\boxed{
\text{Reuse What Is Known}
}
$$

與：

$$
\boxed{
\text{Discover What Is Not Known}.
}
$$

本文提出九階段 Benchmark：

$$
\boxed{
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
B_9.
}
$$

分別為：

1. Global Observation；
2. Project Model Construction；
3. Known Attack Retrieval；
4. Residual Mapping；
5. Novel Attack Hypothesis Generation；
6. Global Campaign Compilation；
7. Sandbox Execution；
8. Defect Surface / Localization；
9. Learning / Transfer。

每一階段都有獨立 hidden checks，防止 AI 只靠 downstream result 假裝 upstream capability。

本文進一步提出三種 benchmark project family：

$$
\boxed{
\mathcal P
=
\{
P_{\mathrm{explicit}},
P_{\mathrm{implicit}},
P_{\mathrm{dynamic}}
\}.
}
$$

其中：

- $P_{\mathrm{explicit}}$：架構邊界顯式，例如 MSSP-like；
- $P_{\mathrm{implicit}}$：相同功能但結構較隱性；
- $P_{\mathrm{dynamic}}$：runtime topology / state / lifecycle 會變。

這使 benchmark 可以測：

> architecture legibility 是否真的降低 global understanding cost？

並比較：

$$
C_{\mathrm{obs}}^{explicit}
$$

與：

$$
C_{\mathrm{obs}}^{implicit}.
$$

本文還提出 known / composition / novel 三類 hidden failures：

$$
\boxed{
F_H
=
F_K
\cup
F_C
\cup
F_N,
}
$$

其中：

- $F_K$：已存在 attack memory 中的已知 family；
- $F_C$：由已知 attacks 合法組合才能得到；
- $F_N$：在 benchmark bounded closure 下屬於 novel mechanism。

AI 若只會 replay， $F_K$ 可高分但 $F_N$ 會失敗；若只會亂創造，可能 $F_N$ 偶爾命中但 precision、cost 與 safety 很差。

本文定義主要 score vector：

$$
\boxed{
\boldsymbol S_{GEI}
=
(
S_A,
S_U,
S_R,
S_C,
S_G,
S_K,
S_V,
S_L,
S_M
).
}
$$

並加入：

$$
\boxed{
S_{\mathrm{eff}},
S_{\mathrm{transfer}},
S_{\mathrm{cal}},
S_{\mathrm{safety}}.
}
$$

分別表示 resource efficiency、cross-project transfer、confidence calibration 與 sandbox / authorization discipline。

本文最重要的 benchmark 原則之一是：

$$
\boxed{
\text{More Defects Found}
\neq
\text{Higher Global Engineering Intelligence}.
}
$$

因為一個 brute-force AI 可以跑非常多 attacks 找出很多 defect，卻可能：

- observation cost 極高；
- repeated rediscovery；
- false positive 極高；
- blind spot 不知道；
- attack applicability 很差；
- root cause 不會定位；
- 不會把新知識寫回 memory。

因此 GEIB 的主要效率指標為：

$$
\boxed{
GEI_{\mathrm{eff}}
=
\frac{
WeightedEngineeringValue
}{
Observation
+
Reasoning
+
Execution
+
Verification
+
HumanCost
+
\epsilon
}.
}
$$

其中 WeightedEngineeringValue 可以包含：

- weighted defect recall；
- blind-spot discovery；
- attack novelty；
- localization；
- coverage；
- reusable knowledge gain。

本文最後提出「One-Glance-to-Global-Attack Challenge」作為高階 benchmark：

> 給 AI 一個從未見過的專案，在嚴格 observation budget 下，要求它先建立全域工程場，再在固定總算力下生成一套 bounded global adversarial campaign，找出 hidden failures、blind spots 與 interaction defects，最後把 novel attack 抽象進 memory，並在第二個表面不同但結構相似的專案上 transfer。

如果一個 AI 能穩定完成這個任務，它所展現的已經不只是 coding intelligence。

更接近：

$$
\boxed{
\text{Global Engineering Intelligence}.
}
$$

**關鍵詞：** Global Engineering Intelligence、GEIB、AI Benchmark、Global Attention、Adversarial Understanding、Attack Synthesis、Defect Surface、Transfer、Compute Efficiency、GACEI

---

# 0. 研究定位與安全邊界

GEIB 所有 benchmark project 必須是：

- synthetic；
- authorized；
- isolated；
- reproducible；
- recoverable；
- benchmark-owned。

本文不建議以未授權真實第三方系統作為 benchmark target。

因此：

$$
\boxed{
\text{GEIB}
=
\text{AI Engineering Capability Benchmark},
}
$$

不是：

$$
\boxed{
\text{Real-World Offensive Cyber Benchmark}.
}
$$

---

# 1. GEIB 到底測什麼？

它不只測：

- code generation；
- bug fixing；
- unit test pass rate。

它測的是：

$$
\boxed{
\text{AI 是否能把一個陌生工程世界壓成可操作模型，然後在有限資源下對整體進行高價值對抗驗證。}
}
$$

---

# 2. 核心能力向量

$$
\boxed{
\mathcal C_{GEI}
=
(
A,U,R,C,G,K,V,L,M
).
}
$$

---

## 2.1 Attention $A$

是否知道先看哪裡、何時 zoom、何時 stop。

---

## 2.2 Understanding $U$

是否真的建立 architecture / state / invariant / lifecycle model。

---

## 2.3 Resolution $R$

是否能解析：

- relations；
- versions；
- roles；
- authority；
- conditions；
- evidence。

---

## 2.4 Creativity $C$

是否能提出 bounded-novel failure hypothesis。

---

## 2.5 Generation $G$

是否能把 hypothesis 生成 executable sandbox experiment。

---

## 2.6 Computation $K$

是否能在組合爆炸下做 pruning、budget allocation、campaign compression。

---

## 2.7 Verification $V$

是否能區分 defect、harness、NotMeasured、Unknown、false positive、blind spot。

---

## 2.8 Localization $L$

是否能把 global evidence 投影回 responsible structures。

---

## 2.9 Memory $M$

是否能把 novel attack 抽象、版本化、promotion 並 transfer。

---

# 3. Benchmark Input

每個 task 包含：

$$
\boxed{
T
=
(
P,
K_A,
B,
Auth,
G,
H
).
}
$$

其中：

- $P$：benchmark project；
- $K_A$：provided adversarial memory subset；
- $B$：resource budget；
- $Auth$：sandbox authority；
- $G$：task / release goal；
- $H$：hidden benchmark truth。

---

# 4. Resource Budget

$$
\boxed{
B
=
(
B_O,
B_R,
B_E,
B_V,
B_P,
B_H
).
}
$$

---

## 4.1 Observation Budget $B_O$

限制：

- files read；
- graph probes；
- tool reads；
- trace windows。

---

## 4.2 Reasoning Budget $B_R$

限制：

- model compute；
- reasoning tokens；
- synthesis iterations。

---

## 4.3 Execution Budget $B_E$

限制：

- attack runs；
- sandbox runtime；
- replay count。

---

## 4.4 Verification Budget $B_V$

限制：

- hidden checks；
- A/B；
- counterfactuals；
- validator rechecks。

---

## 4.5 Parallel Budget $B_P$

限制同時 workers / lanes。

---

## 4.6 Human Budget $B_H$

限制人工 review / escalation 次數。

---

# 5. Benchmark Project Families

$$
\boxed{
\mathcal P
=
\{
P_{\mathrm{explicit}},
P_{\mathrm{implicit}},
P_{\mathrm{dynamic}}
\}.
}
$$

---

## 5.1 Explicit Architecture

特徵：

- boundaries 明示；
- state ownership 明示；
- invariants 明示；
- dependency map 易取得。

MSSP-like project 可作代表。

---

## 5.2 Implicit Architecture

功能接近，但：

- responsibility 隱藏；
- state 分散；
- docs 不完整；
- dependency 要推導。

---

## 5.3 Dynamic Architecture

runtime 中：

- topology 改變；
- state ownership 改變；
- lifecycle branch；
- worker set 改變。

用來測 static project model 的極限。

---

# 6. 功能等價對照組

可建立：

$$
P_E
$$

與：

$$
P_I
$$

具有近似相同 user-facing behavior，

但 architecture legibility 不同。

比較：

$$
C_{\mathrm{obs}}(P_E)
$$

與：

$$
C_{\mathrm{obs}}(P_I).
$$

---

# 7. Hidden Failure Taxonomy

$$
\boxed{
F_H
=
F_K
\cup
F_C
\cup
F_N.
}
$$

---

## 7.1 Known Family $F_K$

attack memory 已知。

測：

- retrieval；
- applicability；
- cheap reuse。

---

## 7.2 Compositional Failure $F_C$

需要：

$$
a_i\odot a_j
$$

或 higher-order composition 才出現。

測：

- interaction understanding；
- composition；
- campaign synthesis。

---

## 7.3 Benchmark-Novel Failure $F_N$

在 benchmark 提供的：

$$
K_A,\Gamma,\Pi,\mathcal O,B
$$

bounded closure 外。

測：

- creativity；
- generation；
- transfer learning。

---

# 8. Hidden Validator Failures

project 不只藏 product defect。

也可藏：

- false green；
- alarm suppression；
- stale validator；
- wrong denominator；
- NotMeasured collapse。

這能測 GACEI-11。

---

# 9. Hidden Model Traps

benchmark 可故意放：

- stale README；
- superseded test；
- misleading file name；
- semantically similar but wrong module。

測：

$$
\text{Can the AI resist superficial interpretation?}
$$

---

# 10. Phase B1：Global Observation

AI 先在：

$$
B_O
$$

下選 observation。

輸出：

$$
\widehat{\mathfrak P}_0.
$$

---

# 11. B1 Hidden Checks

測：

- component recall；
- relation accuracy；
- version accuracy；
- observation efficiency；
- uncertainty honesty。

---

# 12. B1 Score

$$
S_A
=
f(
Selection,
Coverage,
VOI,
Stop,
Uncertainty
).
$$

---

# 13. Phase B2：Project Model Construction

AI 建立：

$$
\widehat{\mathfrak P}
=
(
\widehat V,
\widehat E,
\widehat X,
\widehat I,
\widehat O,
\widehat\Gamma,
\widehat H,
U
).
$$

---

# 14. B2 Hidden Checks

測：

- state owner；
- invariant；
- lifecycle；
- authority；
- recovery；
- validator surface。

---

# 15. Understanding Score

$$
S_U
=
f(
Structure,
State,
Invariant,
Lifecycle,
Authority,
Version
).
$$

---

# 16. Phase B3：Known Attack Retrieval

給：

$$
K_A.
$$

AI 應：

$$
\text{Retrieve}
\rightarrow
\text{Match}
\rightarrow
\text{Instantiate}.
$$

---

# 17. B3 不應重新 brainstorm 已知 attack

benchmark 可以測：

$$
C_{\mathrm{rediscovery}}.
$$

---

# 18. Retrieval Precision

$$
RP
=
\frac{
ApplicableKnownAttacksRetrieved
}{
AllKnownAttacksRetrieved
}.
$$

---

# 19. Retrieval Recall

$$
RR
=
\frac{
ApplicableKnownAttacksRetrieved
}{
AllApplicableKnownAttacks
}.
$$

---

# 20. Phase B4：Residual Mapping

known coverage 後，AI 建立：

$$
G_R.
$$

---

# 21. B4 Hidden Checks

比較：

$$
\widehat G_R
$$

與 benchmark truth residual。

---

# 22. Resolution Score

$$
S_R
=
f(
ResidualPrecision,
ResidualRecall,
ConditionAwareness,
VersionAwareness
).
$$

---

# 23. Phase B5：Novel Hypothesis Generation

AI 對：

$$
G_R
$$

生成：

$$
H_{\mathrm{novel}}.
$$

---

# 24. Creativity Precision

$$
CP
=
\frac{
UsefulGroundedNovelHypotheses
}{
AllNovelHypotheses
}.
$$

---

# 25. Creativity Recall

$$
CR
=
\frac{
HiddenNovelMechanismsHypothesized
}{
HiddenNovelMechanismsInScope
}.
$$

---

# 26. Novelty Inflation Penalty

parameter variants 不應都算 novel family。

定義：

$$
P_{NI}.
$$

---

# 27. Creativity Score

$$
S_C
=
f(
CP,
CR,
Grounding,
BoundedNovelty,
NoveltyInflationPenalty
).
$$

---

# 28. Phase B6：Executable Generation

把 hypothesis：

$$
h
$$

生成：

$$
a.
$$

要求：

- fixture；
- perturbation；
- schedule；
- observation；
- validator；
- recovery；
- provenance。

---

# 29. Generation Validity

$$
GV
=
\frac{
ExecutableValidAttacks
}{
GeneratedAttacks
}.
$$

---

# 30. Safety Validity

$$
SV
=
\frac{
SandboxScopedAttacks
}{
GeneratedAttacks
}.
$$

---

# 31. Generation Score

$$
S_G
=
f(
GV,
SV,
Observability,
Recoverability,
Reproducibility
).
$$

---

# 32. Phase B7：Global Campaign Compilation

候選：

$$
A_K
+
A_N.
$$

AI 需要建立：

- interaction graph；
- lanes；
- schedule；
- coverage target；
- budget allocation。

---

# 33. Campaign Compression

比較：

$$
|\mathcal C|
$$

與 eligible attack space。

---

# 34. Computational Score

$$
S_K
=
f(
CoveragePerCost,
PruningQuality,
InteractionSelection,
BudgetUse,
VerificationReserve
).
$$

---

# 35. Phase B8：Sandbox Execution

執行：

$$
\mathcal C(S^\ast).
$$

---

# 36. Benchmark 記錄

- wall-clock；
- tool calls；
- retries；
- parallel lanes；
- failed harness；
- execution cost。

---

# 37. Phase B9：Defect Surface / Learning

AI 建立：

$$
\Delta_G,
$$

detection matrix，

localization，

coverage vector，

residual。

再把 novel attack：

$$
W_0\rightarrow W_2/W_3/W_4
$$

依證據 promotion。

---

# 38. Verification Score

$$
S_V
=
f(
DefectClassification,
BlindSpotDetection,
FalsePositiveControl,
NotMeasuredDiscipline,
Calibration
).
$$

---

# 39. Localization Score

$$
S_L
=
f(
ResponsibilityAccuracy,
CausalSupport,
CounterfactualQuality,
DiagnosticEfficiency
).
$$

---

# 40. Memory Score

$$
S_M
=
f(
AbstractionQuality,
Deduplication,
VersionBinding,
PromotionDiscipline,
TransferReadiness
).
$$

---

# 41. 主 Score Vector

$$
\boxed{
\boldsymbol S_{GEI}
=
(
S_A,
S_U,
S_R,
S_C,
S_G,
S_K,
S_V,
S_L,
S_M
).
}
$$

---

# 42. 不應只輸出平均

可以另算：

$$
\bar S
=
\frac1{9}
\sum_i S_i,
$$

但：

$$
\boxed{
\bar S
\neq
\text{Complete Capability Profile}.
}
$$

---

# 43. Worst-Dimension Score

$$
S_{\min}
=
\min_i S_i.
$$

這能暴露最弱能力。

---

# 44. Critical-Dimension Weighting

對安全型 benchmark：

$$
w_V,w_L
$$

可更高。

對 research creativity benchmark：

$$
w_C,w_G
$$

可更高。

---

# 45. Efficiency Score

定義：

$$
\boxed{
S_{\mathrm{eff}}
=
\frac{
WeightedEngineeringValue
}{
C_O+C_R+C_E+C_V+C_H+\epsilon
}.
}
$$

---

# 46. WeightedEngineeringValue

可以包含：

$$
WEV
=
\alpha D_R
+
\beta B_R
+
\gamma L_A
+
\delta K_G
+
\eta C_Q,
$$

其中：

- $D_R$：weighted defect recall；
- $B_R$：blind-spot recall；
- $L_A$：localization accuracy；
- $K_G$：knowledge gain；
- $C_Q$：coverage quality。

---

# 47. Observation Efficiency

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

# 48. Frontier Compute Efficiency

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

# 49. Known Work Efficiency

$$
KWE
=
\frac{
KnownCoverage
}{
KnownAttackReasoningCost+\epsilon
}.
$$

---

# 50. Verification Efficiency

$$
VE
=
\frac{
CorrectlyResolvedClaims
}{
VerificationCost+\epsilon
}.
$$

---

# 51. Transfer Benchmark

完成 project A 後，

給：

$$
P_B
$$

表面不同但結構相似。

---

# 52. Transfer 不提供完整 memory?

可分兩個 protocol：

## Memory-On

允許使用剛學到 attack memory。

## Memory-Off

只測內部 model transfer。

---

# 53. Transfer Score

$$
S_{\mathrm{transfer}}
=
f(
AttackTransfer,
ModelTransfer,
FalseApplicability,
CostSaving
).
$$

---

# 54. Negative Transfer Control

再給：

$$
P_C
$$

表面相似但 structure 不同。

AI 應拒絕錯誤 transfer。

---

# 55. Calibration Score

對：

- attack applicability；
- defect probability；
- localization；

AI 輸出 confidence。

---

# 56. Calibration

理想：

$$
P(correct\mid conf=p)\approx p.
$$

---

# 57. Calibration Score

$$
S_{\mathrm{cal}}
=
1-ECE.
$$

---

# 58. Safety / Authority Score

所有 generated actions 必須：

$$
Scope
\subseteq
AuthorizedSandbox.
$$

---

# 59. Overreach

任何要求：

- external target；
- unauthorized network；
- production mutation；
- private credential；

都直接記：

$$
SafetyViolation.
$$

---

# 60. Safety Score

$$
S_{\mathrm{safety}}
=
1-
ViolationRate.
$$

---

# 61. Benchmark 不獎勵「越狠越好」

GEIB 不以：

$$
Damage
$$

作 scoring objective。

---

# 62. 反而獎勵最小有效 perturbation

$$
Q_{\mathrm{attack}}
=
\frac{
InformationValue
}{
PerturbationCost+\epsilon
}.
$$

---

# 63. Hidden Defect Injection

Benchmark 可以注入：

- local defect；
- relation defect；
- state defect；
- temporal defect；
- recovery defect；
- validator defect；
- interaction defect。

---

# 64. Defect Injection 要可追溯

每個 hidden defect 有：

$$
TruthRecord.
$$

---

# 65. TruthRecord

保存：

- intended mechanism；
- applicable conditions；
- expected evidence；
- true responsible structure；
- severity；
- allowed solution space。

---

# 66. Benchmark 不應把單一路徑當唯一答案

某些 defect 可能有多個有效 attack。

因此 scoring 應對：

$$
\text{mechanism equivalence}
$$

而不是 exact script match。

---

# 67. Mechanism-Based Scoring

若 AI attack：

$$
a
$$

與 hidden mechanism：

$$
f
$$

語義等價，

即使 code 不同也應得分。

---

# 68. Hidden Validator Traps

可注入：

- false green；
- false red；
- stale threshold；
- wrong version；
- denominator collapse。

---

# 69. Hidden Observation Traps

例如：

- log 缺失；
- stale snapshot；
- wrong environment；
- incomplete trace。

---

# 70. Hidden Version Traps

讓某 docs 是舊版。

測：

$$
VersionAwareness.
$$

---

# 71. Hidden Authority Traps

某 capability 存在，但 benchmark 沒授權執行。

AI 必須：

$$
\boxed{
\text{Know}
\neq
\text{Execute}.
}
$$

---

# 72. Benchmark Baselines

至少比較：

### Baseline A：Static Scanner

規則式。

### Baseline B：Replay Agent

只使用已知 attack memory。

### Baseline C：Coding Agent

能讀 repo、寫 test，但無 global framework。

### Baseline D：Multi-Agent Reviewer

多 agents 分工。

### Baseline E：GACEI-style Agent

完整 pipeline。

---

# 73. Baseline A 的價值

測 deterministic lower bound。

---

# 74. Baseline B

測 memory 的純價值。

---

# 75. Baseline C

測一般 coding intelligence。

---

# 76. Baseline D

測多 Agent 但不保證全域方法論。

---

# 77. Baseline E

測完整 global engineering intelligence。

---

# 78. Ablation Study

移除：

- attack memory；
- active observation；
- creativity；
- verification reserve；
- localization；
- compression。

看各模組貢獻。

---

# 79. Memory Ablation

預期：

$$
RediscoveryCost\uparrow.
$$

---

# 80. Attention Ablation

預期：

$$
ObservationCost\uparrow.
$$

---

# 81. Creativity Ablation

預期：

$$
NovelFailureRecall\downarrow.
$$

---

# 82. Compression Ablation

預期：

$$
ExecutionCost\uparrow.
$$

---

# 83. Verification Ablation

預期：

$$
FalseGreen\uparrow.
$$

---

# 84. Localization Ablation

預期：

$$
TimeToRepair\uparrow.
$$

---

# 85. Longitudinal Benchmark

同一 agent：

$$
t_1,t_2,\ldots,t_n
$$

持續處理多個 project。

---

# 86. 測 Learning Curve

$$
C_n
=
\text{cost on project }n.
$$

理想：

$$
C_n\downarrow
$$

對已知類型 project。

---

# 87. 但 novel project 可能上升

這不是退步。

---

# 88. Knowledge Gain

$$
KG_n
=
|K_{n+1}^{useful}-K_n^{useful}|.
$$

---

# 89. Amortized Engineering Cost

$$
AEC_N
=
\frac{
\sum_{n=1}^{N}Cost_n
}{
N
}.
$$

---

# 90. Memory Capital Effect

若 AMS 有效：

$$
AEC_N
$$

對相似 project family 應下降。

---

# 91. Attack Family Transfer Rate

$$
AFTR
=
\frac{
SuccessfulTransferredFamilies
}{
EligibleFamilies
}.
$$

---

# 92. False Transfer Rate

$$
FTR
=
\frac{
IncorrectTransferredFamilies
}{
AttemptedTransfers
}.
$$

---

# 93. Benchmark 的核心不是「一次拿高分」

而是：

$$
\boxed{
\text{能不能越做越便宜、越做越準、越做越少重複。}
}
$$

---

# 94. One-Glance-to-Global-Attack Challenge

高階 challenge：

1. 給陌生 project；
2. 嚴格 $B_O$ ；
3. 給部分 $K_A$ ；
4. 固定總 budget；
5. 隱藏 $F_K,F_C,F_N$ ；
6. 隱藏 validator blind spot；
7. 要求 global campaign；
8. 要求 defect surface；
9. 要求 memory update；
10. 給 transfer project。

---

# 95. Challenge Success

不要求找出所有未知 defect。

而要求：

- 高 weighted coverage；
- 高 hidden defect recall；
- 高 blind-spot recall；
- 低 false positive；
- 高 localization；
- honest residual；
- bounded cost；
- valid memory update。

---

# 96. Globality Certificate

Benchmark output 必須包含：

$$
GC(\mathcal C).
$$

---

# 97. Defect Surface Certificate

亦包含：

$$
DSC(\mathcal C).
$$

---

# 98. Learning Receipt

記錄：

```yaml
learning_receipt:
  new_witnesses:
  promoted_templates:
  new_families:
  falsified_hypotheses:
  superseded_memory:
  transfer_results:
  residual_unknowns:
```

---

# 99. Benchmark Reproducibility

每個 benchmark task 應保存：

- project digest；
- hidden truth digest；
- resource budget；
- model version；
- tool version；
- seed；
- sandbox image；
- scoring rules。

---

# 100. Hidden Truth 不應被模型看見

正式 eval：

$$
Train/Eval\ Separation.
$$

---

# 101. Contamination Risk

若 benchmark project 洩漏到 training corpus，

novelty score 失真。

---

# 102. Fresh Project Generation

可定期生成新的 synthetic project variants。

---

# 103. Dynamic Benchmark

每期：

$$
P_t
$$

不同。

---

# 104. Static Core + Dynamic Frontier

保留固定核心測 regression，

再加入 dynamic unseen tasks 測真正 generalization。

---

# 105. Score Stability

固定核心讓：

$$
Score_t
$$

可比較。

---

# 106. Frontier Freshness

dynamic frontier 防止 benchmark memorization。

---

# 107. Benchmark Difficulty Levels

## L1：Explicit / Known

顯式架構、known attacks 為主。

## L2：Implicit / Mixed

結構隱性，known + composition。

## L3：Novel / Dynamic

novel mechanisms、runtime change。

## L4：Global Interaction

higher-order interaction + validator blind spot。

## L5：Transfer / Learning

跨 project transfer 與 memory update。

---

# 108. Difficulty 不等於 attack 危險度

只表示工程推理難度。

---

# 109. GEI Capability Profile

最終報告：

```yaml
gei_profile:
  attention:
  understanding:
  resolution:
  creativity:
  generation:
  computation:
  verification:
  localization:
  memory:
  efficiency:
  transfer:
  calibration:
  safety:
```

---

# 110. Profile 比排名更重要

模型 A 可能：

- creativity 強；
- verification 弱。

模型 B 可能相反。

對不同工程任務適用性不同。

---

# 111. Pareto Frontier

可以比較：

$$
(
Quality,
Cost,
Time,
Safety
).
$$

---

# 112. 不必有唯一最佳模型

---

# 113. Human-AI Team Benchmark

也可測：

$$
Human+AI.
$$

---

# 114. Human Intervention Budget 固定

比較：

> 同樣人類時間下，哪個 AI 系統提高最多 engineering value？

---

# 115. Multi-Agent Benchmark

固定：

$$
N_{\mathrm{agents}}.
$$

測 coordination overhead。

---

# 116. Role Differentiation

可以設：

- challenger；
- measurer；
- realist / resource governor。

---

# 117. Role Collapse Penalty

如果三個 agent 大量 duplicate reasoning：

$$
C_{\mathrm{dup}}\uparrow.
$$

---

# 118. Shared Memory Benefit

測：

$$
C_{\mathrm{rediscovery}}\downarrow.
$$

---

# 119. Shared Memory Risk

錯誤 memory 可能傳播。

所以也測：

$$
ErrorPropagation.
$$

---

# 120. Memory Poison Control

benchmark 可故意放一條過期 attack memory。

AI 應：

$$
\text{revalidate / reject}.
$$

---

# 121. Authority Separation Benchmark

給 AI 高能力，但低 execution authority。

測：

$$
\boxed{
\text{Can it stay within authority?}
}
$$

---

# 122. Capability / Authority 分離

$$
\boxed{
Capability
\neq
Authority.
}
$$

---

# 123. Model Tier Benchmark

允許：

- cheap model；
- frontier model；
- deterministic tools。

看 AI 是否會做 model routing。

---

# 124. Frontier Compute Waste

若所有 known task 都用 frontier model：

$$
Penalty.
$$

---

# 125. Compute Allocation Score

$$
CAS
=
\frac{
HighValueFrontierUse
}{
TotalFrontierUse+\epsilon
}.
$$

---

# 126. Verification Reserve Score

若 campaign 沒保留：

$$
B_V,
$$

扣分。

---

# 127. Stop Quality

AI 是否知道什麼時候停止？

---

# 128. Overthinking Penalty

若 required claims 已滿足但仍大量開新 attack：

$$
Penalty_{\mathrm{overrun}}.
$$

---

# 129. Underthinking Penalty

如果 residual critical gap 尚未處理就停止：

$$
Penalty_{\mathrm{premature}}.
$$

---

# 130. Stop Score

$$
S_{\mathrm{stop}}
=
f(
Timeliness,
ResidualRisk,
BudgetUse,
ClaimCompleteness
).
$$

---

# 131. Global Engineering Intelligence 不等於 AGI

本文不主張：

$$
GEI=AGI.
$$

GEI 是一個工程 domain capability。

---

# 132. 但 GEI 可以作 AGI-like 能力子測試

因為需要：

- global model；
- adaptive attention；
- transfer；
- memory；
- planning；
- verification。

---

# 133. GEI 與 Coding Benchmark 的差異

coding benchmark 常問：

> 能不能完成指定 issue？

GEIB 問：

> 能不能自己理解整個陌生系統，決定哪裡值得測，生成高價值實驗，並學會？

---

# 134. GEI 與 Security Benchmark 的差異

GEIB 不以外部入侵成功率為目標。

而以：

- project understanding；
- software quality；
- defect discovery；
- validator robustness；
- compute efficiency；

為目標。

---

# 135. GEI 與 Fuzzing Benchmark 的差異

fuzzing 常著重 input-space exploration。

GEIB 還包含：

- architecture；
- state；
- temporal；
- recovery；
- validator；
- global interaction；
- memory。

---

# 136. GEI 與 SWE-Bench 類任務的差異

SWE-style：

$$
Issue+Repo\rightarrow Patch.
$$

GEIB：

$$
Repo
\rightarrow
Model
\rightarrow
AttackProgram
\rightarrow
Evidence
\rightarrow
Diagnosis
\rightarrow
Learning.
$$

---

# 137. Benchmark 的核心問題

$$
\boxed{
\text{Can the AI choose the experiment before being told the bug?}
}
$$

---

# 138. 這就是自主工程研究

不只是執行 specification。

---

# 139. Research Mode

GEIB 也可延伸到：

- simulation；
- scientific software；
- formal runtime；
- game system；
- agent system。

---

# 140. 不限 MSSP

MSSP 只是第一個高可觀測載體。

---

# 141. Benchmark Extension to EML

可測 semantic / round-trip / determinism failure。

---

# 142. Extension to LIMEN / SEDB-RAL

可測 identity / authority / currentness / recovery。

---

# 143. 但每個 domain 需要自己的 attack families

GEIB 只提供 meta-framework。

---

# 144. Domain Adapter

定義：

$$
D_A:
Domain
\rightarrow
(
Invariants,
Observations,
AttackGrammar,
Validators
).
$$

---

# 145. Benchmark Core 保持共同

共同能力：

$$
A,U,R,C,G,K,V,L,M.
$$

---

# 146. Domain-Specific Scoring

另加 domain score。

---

# 147. Long-Horizon GEI

未來可以測：

$$
\text{project evolution over weeks}.
$$

---

# 148. Memory Continuity

同一 agent 能否記得：

- old attack；
- superseded version；
- transfer history。

---

# 149. Non-Monotone Knowledge

新版本可能讓舊 attack：

$$
NotApplicable.
$$

AI 必須學會忘記 active status，而不是刪除歷史。

---

# 150. Memory Lifecycle Score

測：

- promotion；
- quarantine；
- supersession；
- retirement。

---

# 151. Benchmark Governance

每個 score 必須可解釋。

---

# 152. Hidden Metric 不應決定所有結果

模型開發者應能看到主要 scoring dimensions。

---

# 153. Anti-Gaming

不能只針對：

$$
N_{\mathrm{attacks}}
$$

刷分。

---

# 154. Rate Limits

attack count 不直接加分。

---

# 155. Value-Based Scoring

只有：

- hidden mechanism；
- blind spot；
- valid localization；
- reusable learning；

真正加重要分。

---

# 156. Cost Penalty

大量無效 attack：

$$
Score\downarrow.
$$

---

# 157. False Positive Penalty

亂報 defect：

$$
Score\downarrow.
$$

---

# 158. Residual Honesty Bonus

正確說：

$$
Unknown
$$

比亂說：

$$
Safe
$$

更高分。

---

# 159. Benchmark Output 不應只有 Leaderboard

還應有：

$$
\boxed{
\text{Capability Profile}
+
\text{Failure Analysis}
+
\text{Cost Breakdown}
+
\text{Learning Trace}.
}
$$

---

# 160. Benchmark Trace

保存：

$$
Observation
\rightarrow
Decision
\rightarrow
Attack
\rightarrow
Evidence
\rightarrow
Update.
$$

---

# 161. Trace 用於研究 AI 認知策略

可比較：

- overread；
- overthink；
- premature attack；
- good pruning；
- good stopping。

---

# 162. Full Benchmark Formula

可以概念寫成：

$$
\boxed{
Score_{GEIB}
=
F(
\boldsymbol S_{GEI},
S_{\mathrm{eff}},
S_{\mathrm{transfer}},
S_{\mathrm{cal}},
S_{\mathrm{safety}},
S_{\mathrm{stop}}
).
}
$$

---

# 163. 但主輸出仍是 vector

---

# 164. 研究假說

## H1：GACEI-style agent 在固定 budget 下優於 local-only agent

$$
GEI_{\mathrm{eff}}^{GACEI}
>
GEI_{\mathrm{eff}}^{local}.
$$

## H2：Attack memory 降低 known-family rediscovery cost

$$
C_{\mathrm{known}}^{memory}
<
C_{\mathrm{known}}^{scratch}.
$$

## H3：Active observation 降低 project understanding cost

$$
C_{\mathrm{obs}}^{active}
<
C_{\mathrm{obs}}^{full}
$$

在相同 task quality 下成立。

## H4：Residual-guided creativity 提高 novel attack precision

$$
Precision_{novel}^{residual}
>
Precision_{novel}^{free}.
$$

## H5：Multidimensional defect surface 提高 decision quality

$$
DecisionQuality_{DSMAC}
>
DecisionQuality_{binary}.
$$

## H6：Longitudinal shared memory 降低 amortized engineering cost

$$
AEC_N\downarrow
$$

對相似 project family 成立。

---

# 165. 主系列的總體閉環

GACEI-01 至 12 可以壓成：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Understand}
\rightarrow
\text{Resolve}
\rightarrow
\text{Remember}
\rightarrow
\text{Create}
\rightarrow
\text{Generate}
\rightarrow
\text{Compose}
\rightarrow
\text{Compress}
\rightarrow
\text{Compute}
\rightarrow
\text{Verify}
\rightarrow
\text{Localize}
\rightarrow
\text{Learn}.
}
$$

下一個 project 再從：

$$
K_{t+1}
$$

開始。

---

# 166. 系列核心學習律

$$
\boxed{
K_{t+1}
=
K_t
\cup
\operatorname{Promote}
(
\operatorname{Abstract}
(
A_t^{novel}
)
).
}
$$

---

# 167. 系列核心成本律

理想：

$$
\boxed{
\text{Known Assurance Marginal Cost}
\downarrow
}
$$

隨可重用 memory 增長。

---

# 168. 系列核心創造律

$$
\boxed{
\text{Frontier Compute}
\rightarrow
\text{Residual Unknowns},
}
$$

而不是已知 attack rediscovery。

---

# 169. 系列核心全域律

$$
\boxed{
\text{Globality}
\neq
\text{Attack Count}.
}
$$

而是：

$$
\boxed{
\text{Finite Structural Control over a Declared Engineering Domain}.
}
$$

---

# 170. 系列核心對偶律

對 MSSP-like architecture：

$$
\boxed{
\text{Local Responsibility}
\leftrightarrow
\text{Global Perturbation}.
}
$$

---

# 171. 系列核心證據律

$$
\boxed{
\text{Global Evidence}
=
\text{Defect Surface}
+
\text{Detection}
+
\text{Diagnosis}
+
\text{Coverage}
+
\text{Residual}.
}
$$

---

# 172. 系列核心智能律

$$
\boxed{
\text{Global Engineering Intelligence}
=
\text{Global Selection of Finite Computation}.
}
$$

---

# 173. 本文非主張

本文不主張：

1. GEIB 等於 AGI benchmark；
2. 找到更多 defect 就一定更智能；
3. attack 越多越高分；
4. 全域 benchmark 應作用於未授權真實系統；
5. hidden defect set 能代表所有現實 failure；
6. synthetic project 能完全替代真實工程；
7. 單一總分可以代表所有能力；
8. benchmark novelty 等於全球歷史 novelty；
9. 高 GEIB score 應自動獲得更高 execution authority；
10. multi-agent 一定比 single-agent 好；
11. memory 越大 score 越高；
12. observation 越少越好；
13. compute 越少越好；
14. 所有 project domain 使用同一 attack grammar；
15. GEIB 能證明模型無安全風險；
16. benchmark 可取代真實產品驗證流程。

本文主張的是：

$$
\boxed{
\text{未來 AI 的工程能力應被評估為一條跨觀察、理解、創造、計算、驗證與學習的全域流程。}
}
$$

---

# 174. 結論

今日許多 AI 工程 benchmark 問：

> 你能不能修掉這個 bug？

GACEI-12 問的是另一個問題：

> **如果我不告訴你 bug 在哪裡，只給你一個陌生專案、有限時間、有限算力、有限工具與一個 sandbox，你能不能先看懂整個系統，再自己決定哪些地方值得測，生成新的 failure hypotheses，組成一套 bounded global campaign，找到真正缺陷與 blind spots，定位原因，最後把新知識保存下來，讓下一次變得更便宜？**

這個問題測的不只是 coding。

它同時測：

$$
\boxed{
\text{Attention}
+
\text{Understanding}
+
\text{Resolution}
+
\text{Creativity}
+
\text{Generation}
+
\text{Computation}
+
\text{Verification}
+
\text{Localization}
+
\text{Memory}.
}
$$

而它最重要的限制不是：

> AI 能不能無限算。

而是：

$$
\boxed{
\text{AI 能不能在有限算力下選對要算的東西。}
}
$$

因此整個 GACEI 主系列最後可以壓縮成四句：

$$
\boxed{
\text{Understand Globally}
}
$$

$$
\boxed{
\text{Attack Structurally}
}
$$

$$
\boxed{
\text{Diagnose Locally}
}
$$

$$
\boxed{
\text{Learn Permanently}.
}
$$

而 GEIB 就是把這四句變成可以真正測量的 AI 工程能力。

如果未來某個 AI 可以在陌生 project 上穩定完成：

$$
\boxed{
\text{One Glance}
\rightarrow
\text{Global Model}
\rightarrow
\text{Global Adversarial Program}
\rightarrow
\text{Defect Surface}
\rightarrow
\text{Reusable Learning},
}
$$

那它所展現的就不只是「很會寫程式」。

而是：

$$
\boxed{
\text{Global Engineering Intelligence}.
}
$$

這就是 GACEI 主系列的收束點。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
