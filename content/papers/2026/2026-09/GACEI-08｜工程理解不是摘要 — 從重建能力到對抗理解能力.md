---
title: "GACEI-08｜工程理解不是摘要：從重建能力到對抗理解能力"
title_en: "GACEI-08 | Engineering Understanding Is Not Summarization: From Reconstruction Capability to Adversarial Understanding"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-08"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / AI 工程理解 / 重建驗收 / 對抗理解"
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
  - "理解的工程驗收：如果真的懂，就重建給我看"
  - "擁有資料不等於理解：本地 Agent 的大型理論庫認知編譯"
---

# GACEI-08｜工程理解不是摘要
## 從重建能力到對抗理解能力

**英文題名：** Engineering Understanding Is Not Summarization: From Reconstruction Capability to Adversarial Understanding

---

## 摘要

人工智慧對一個軟體專案輸出高品質摘要、架構圖、模組說明與依賴分析，並不能充分證明它已掌握足以支援工程決策的內部模型。既有「理解的工程驗收」已提出一個更強的操作性原則：

$$
\boxed{
\text{Claimed Understanding}
\rightarrow
\text{Reconstruction Challenge}.
}
$$

也就是：如果 AI 聲稱理解某個系統，應能在有限證據、明確契約與未見測試下，獨立重建一個功能上足夠接近的候選系統。

本文將這條理解驗收再向前推進。對 GACEI 而言，僅能重建仍不足以證明 AI 具備「對抗性工程理解」（Adversarial Engineering Understanding, AEU）。因為一個 AI 可能掌握：

- 正常資料流；
- 正常 control flow；
- 主要模組；
- 主要狀態；
- 基本 lifecycle；

並成功重建正常行為，卻仍不知道：

- 哪些 invariant 是真正控制系統穩定性的關鍵；
- 哪些局部 state mutation 會形成跨模組失敗；
- 哪些時間順序會破壞原本正確的局部行為；
- 哪些 validator blind spot 會產生 false green；
- 哪些 attack combinations 會形成只有全域觀察才看得見的 interaction failure。

因此本文提出：

$$
\boxed{
\text{Can Reconstruct}
\neq
\text{Can Adversarially Understand}.
}
$$

本文定義一條工程理解能力階梯：

$$
\boxed{
U_E^0
<
U_E^1
<
U_E^2
<
U_E^3
<
U_E^4
<
U_E^5
}
$$

其中：

- $U_E^0$：Describe；
- $U_E^1$：Structure；
- $U_E^2$：Reconstruct；
- $U_E^3$：Predict；
- $U_E^4$：Falsify；
- $U_E^5$：Adversarially Synthesize。

其差異可簡化為：

$$
\text{Describe}
\rightarrow
\text{Rebuild}
\rightarrow
\text{Predict}
\rightarrow
\text{Break Hypothetically}
\rightarrow
\text{Generate and Verify New Failure Mechanisms}.
$$

本文不把「break」理解為未授權入侵，而是指在授權 sandbox 中，AI 根據其 project model 推導並驗證系統的失敗條件。

本文進一步提出「理解殘差」（Understanding Residual）：

$$
\boxed{
R_U
=
\mathfrak P
\setminus
\widehat{\mathfrak P}_{\mathrm{usable}},
}
$$

用來描述 project truth 與 AI 可操作模型之間仍未被掌握的結構差異。實作上不能精確知道真實 $\mathfrak P$，因此本文使用 hidden tests、counterfactual interventions、novel transfer tasks、attack applicability checks 與 failure localization 估計：

$$
\widehat R_U.
$$

本文特別區分五種常被混為「理解」的能力：

$$
\boxed{
\text{Recall}
\neq
\text{Model}
\neq
\text{Reconstruct}
\neq
\text{Intervene}
\neq
\text{Falsify}.
}
$$

Recall 可以來自資料檢索；Model 需要結構整合；Reconstruct 需要可執行生成；Intervene 需要因果與狀態理解；Falsify 則要求 AI 能從系統契約與架構中生成有意義的反例，而不是任意輸入垃圾值。

本文將對抗理解定義為：

$$
\boxed{
AEU
=
f(
M,
R,
P,
I,
F,
L,
G,
V
)
}
$$

其中：

- $M$：Model fidelity；
- $R$：Reconstruction；
- $P$：Prediction；
- $I$：Intervention understanding；
- $F$：Falsification ability；
- $L$：Localization；
- $G$：Novel adversarial generation；
- $V$：Verification discipline。

一個高 AEU 的 AI 不只會說：

> 「這個系統可能有 race condition。」

而應能指出：

1. race 的結構前提；
2. 哪些 state / relation 參與；
3. 哪個 invariant 可能被破壞；
4. 在什麼 condition fiber 下適用；
5. 用什麼最小 synthetic perturbation 可以驗證；
6. 預期 observation 是什麼；
7. 若失敗發生，如何投影回責任域；
8. 若未發生，如何更新 attack hypothesis。

本文提出「對抗重建測試」（Adversarial Reconstruction Test, ART）：先要求 AI 重建 project model，再要求它根據該模型生成一組它從未看過的 attack hypotheses，最後用 hidden injected defects 或 synthetic failure mechanisms 驗證其理解。若 AI 只能在看到既有測試後重述 attack，則屬於 retrieval；若能在新的系統拓撲上生成結構正確、可執行、可驗證的新 attack，才開始支持 $U_E^5$。

本文最後提出一個關鍵命題：

$$
\boxed{
\text{The strongest evidence of engineering understanding is not explanation alone,}
}
$$

而是：

$$
\boxed{
\text{prediction under intervention + reconstruction + falsification + transfer}.
}
$$

這使 GACEI 從「AI 會不會讀 code」提升到：

> AI 是否擁有足以在陌生系統上建立、重建、預測、反駁與重新驗證的工程世界模型？

**關鍵詞：** Engineering Understanding、Adversarial Understanding、Reconstruction Challenge、Falsification、Intervention、Attack Synthesis、Hidden Tests、Causal Model、AI 工程智能、GACEI、MSSP

---

# 0. 研究定位

本文不處理哲學上的：

- consciousness；
- intentionality；
- subjective understanding；
- self-awareness。

本文只定義：

$$
\boxed{
\text{Operational Engineering Understanding Evidence}.
}
$$

也就是：

> 哪些外部可測行為足以支持 AI 對一個工程系統掌握了可操作模型？

---

# 1. 為什麼摘要不是理解？

## 1.1 摘要可以來自壓縮

一個模型可以：

$$
\text{Read}
\rightarrow
\text{Compress}
\rightarrow
\text{Summarize}.
$$

但：

$$
\boxed{
\text{Compression Fidelity}
\neq
\text{Operational Understanding}.
}
$$

---

## 1.2 正確術語也不夠

AI 可以正確說出：

- event sourcing；
- state machine；
- recovery；
- CAS；
- TMS；
- validator；

仍可能完全不知道：

> 哪一個 invariant 如果被破壞，哪一個 output 會先錯？

---

# 2. 六層工程理解

本文定義：

$$
U_E^0
<
U_E^1
<
U_E^2
<
U_E^3
<
U_E^4
<
U_E^5.
$$

---

## 2.1 $U_E^0$：Describe

AI 能：

- 摘要；
- 轉述；
- 解釋術語；
- 列出檔案。

---

## 2.2 $U_E^1$：Structure

AI 能重建：

$$
(V,E,B).
$$

知道：

- component；
- dependency；
- boundary；
- role。

---

## 2.3 $U_E^2$：Reconstruct

AI 能根據有限規格生成：

$$
\widehat S
$$

使：

$$
Behavior(\widehat S)
\approx
Behavior(S)
$$

在指定測試域成立。

---

## 2.4 $U_E^3$：Predict

AI 能回答：

$$
do(x)
\rightarrow
?
$$

例如：

> 如果這個 state owner 延遲一次 commit，後續哪些狀態會變？

---

## 2.5 $U_E^4$：Falsify

AI 能從：

$$
I
$$

生成：

$$
\neg I
$$

的有意義 witness candidate。

---

## 2.6 $U_E^5$：Adversarially Synthesize

AI 不只生成單一反例。

而是能：

- 創造新 attack family；
- 組合局部 attacks；
- 設計 validator；
- 執行 synthetic campaign；
- 驗證；
- 定位；
- 抽象新知識。

---

# 3. Can Describe 不等於 Can Reconstruct

$$
\boxed{
D
\not\Rightarrow
R.
}
$$

一個 AI 可以描述：

> 「這是一個 append-only event store。」

但重建時仍可能：

- 漏掉 concurrency；
- 漏掉 idempotence；
- 漏掉 ordering；
- 漏掉 recovery。

---

# 4. Can Reconstruct 不等於 Can Predict

如果重建只是：

$$
Input
\rightarrow
Output
$$

的表面模仿，

可能：

$$
R
$$

高，

但：

$$
P
$$

低。

---

# 5. Predict 需要 intervention model

定義：

$$
M_C
=
\text{Causal Engineering Model}.
$$

AI 必須知道：

$$
do(s_i:=s_i')
$$

如何影響：

$$
s_j,
s_k,\ldots
$$

---

# 6. Intervention Fidelity

對原系統：

$$
S,
$$

重建系統：

$$
\widehat S,
$$

施加相同：

$$
do(a).
$$

比較：

$$
d(
Behavior(S\mid do(a)),
Behavior(\widehat S\mid do(a))
).
$$

---

# 7. Counterfactual Understanding

AI 不只回答：

> 發生了什麼？

而是：

> 如果這個 mutation 沒發生，failure 還會出現嗎？

---

# 8. Falsification 是更高階理解證據

給 invariant：

$$
I.
$$

AI 應能構造：

$$
w
$$

使：

$$
w\models \neg I
$$

在 synthetic environment 中被測試。

---

# 9. 但「想到反例」也不等於理解

如果 AI 只是：

> 任意把資料刪掉。

當然可以讓系統壞。

這種：

$$
\boxed{
\text{Trivial Destruction}
}
$$

不算高品質 falsification。

---

# 10. Meaningful Falsification

要求：

$$
w
$$

滿足：

1. precondition valid；
2. target invariant explicit；
3. perturbation minimal or interpretable；
4. observation linked；
5. validator discriminative；
6. recovery bounded；
7. diagnosis possible。

---

# 11. Attack Validity Score

可定義：

$$
Q_A
=
f(
P,
I,
M,
O,
V,
D,
R
).
$$

其中：

- $P$：precondition；
- $I$：invariant relevance；
- $M$：mechanism fidelity；
- $O$：observation；
- $V$：validator；
- $D$：diagnosability；
- $R$：recovery。

---

# 12. 對抗理解不是攻擊數量

若：

$$
N_{\mathrm{attack}}\uparrow
$$

不代表：

$$
AEU\uparrow.
$$

---

# 13. 反例品質比反例數量重要

一個 attack 若能暴露：

$$
\text{hidden global coupling},
$$

可能比：

$$
100
$$

個重複 local mutation 有價值。

---

# 14. 理解與 attack novelty

已知 attack replay：

$$
a\in K_A
$$

只測：

$$
\text{retrieval + transfer}.
$$

真正 creativity 需要：

$$
a_{\mathrm{new}}
\notin K_A.
$$

---

# 15. Novel 不等於 Good

新 attack：

$$
a_{\mathrm{new}}
$$

可能只是：

- invalid；
- impossible；
- irrelevant；
- redundant。

所以：

$$
\boxed{
\text{Novelty}
\neq
\text{Engineering Value}.
}
$$

---

# 16. 對抗理解的八個構件

本文定義：

$$
\boxed{
AEU
=
f(
M,
R,
P,
I,
F,
L,
G,
V
).
}
$$

---

## 16.1 Model $M$

project field fidelity。

---

## 16.2 Reconstruction $R$

能否重建功能與結構。

---

## 16.3 Prediction $P$

能否預測 intervention 後結果。

---

## 16.4 Intervention $I$

能否控制變量而非只觀察 correlation。

---

## 16.5 Falsification $F$

能否生成有意義反例。

---

## 16.6 Localization $L$

能否把 failure 投影回責任域。

---

## 16.7 Generation $G$

能否生成 executable adversarial experiment。

---

## 16.8 Verification $V$

能否分辨：

- true defect；
- false positive；
- NotMeasured；
- harness failure。

---

# 17. Understanding Residual

理想 project：

$$
\mathfrak P.
$$

AI model：

$$
\widehat{\mathfrak P}.
$$

概念性：

$$
\boxed{
R_U
=
\mathfrak P
\setminus
\widehat{\mathfrak P}_{\mathrm{usable}}.
}
$$

---

# 18. 真實 residual 通常不可直接知道

因此只能估：

$$
\widehat R_U.
$$

---

# 19. 如何估 residual？

利用：

- hidden tests；
- hidden architecture facts；
- injected defects；
- unseen interventions；
- version shifts；
- transfer project。

---

# 20. Hidden Structure Test

刻意隱藏：

$$
e_{ij}.
$$

看 AI 是否從其他 evidence 推導正確 relation。

---

# 21. Hidden State Test

不直接給：

$$
Owner(X_i).
$$

看 AI 能否從 mutation / persistence 行為推斷。

---

# 22. Hidden Invariant Test

只給 examples，不給 invariant。

看 AI 是否能抽出：

$$
I^\ast.
$$

---

# 23. Hidden Failure Test

在 system 中注入：

$$
F^\ast.
$$

看 AI 是否：

1. 發現；
2. 解釋；
3. 定位；
4. 生成 regression attack。

---

# 24. Reconstruction Challenge

給：

- requirements；
- limited source；
- architecture hints。

要求：

$$
\widehat S.
$$

---

# 25. Behavioral Gate

$$
d_T(
Behavior(S),
Behavior(\widehat S)
)
\le\epsilon.
$$

---

# 26. Structural Gate

重建：

$$
V,E,X,I.
$$

---

# 27. Intervention Gate

比較：

$$
do(a)
$$

後行為。

---

# 28. Falsification Gate

要求：

$$
\widehat S
$$

與：

$$
S
$$

面對 novel perturbation 時是否產生一致 failure。

---

# 29. Transfer Gate

把表面名稱全部換掉。

若 AI 仍能套用同一機制：

$$
Transfer=1.
$$

---

# 30. Surface Identity Removal

改掉：

- names；
- UI；
- directory；
- variable names；
- story domain。

保留：

$$
\text{functional structure}.
$$

---

# 31. 如果理解只靠表面記憶

則：

$$
Transfer
\downarrow.
$$

---

# 32. Adversarial Reconstruction Test

本文提出：

$$
\boxed{
ART.
}
$$

---

# 33. ART Phase 1：Observe

AI 在有限 budget 下建立：

$$
\widehat{\mathfrak P}.
$$

---

# 34. ART Phase 2：Reconstruct

AI 建立：

$$
\widehat S.
$$

---

# 35. ART Phase 3：Predict

給 unseen interventions。

---

# 36. ART Phase 4：Falsify

要求 AI 生成：

$$
A_{\mathrm{novel}}.
$$

---

# 37. ART Phase 5：Execute

只在 authorized sandbox。

---

# 38. ART Phase 6：Localize

對 failures：

$$
F_i
$$

回投：

$$
\Pi(F_i).
$$

---

# 39. ART Phase 7：Distill

把有效 attack 抽象：

$$
W_0
\rightarrow
W_2/W_3.
$$

---

# 40. ART Phase 8：Transfer

把 attack 套到新 project。

---

# 41. ART Score

$$
\boxed{
S_{ART}
=
w_M M
+
w_R R
+
w_P P
+
w_F F
+
w_L L
+
w_G G
+
w_V V
+
w_T T.
}
$$

---

# 42. 不應只有總分

必須輸出 vector：

$$
\boldsymbol S_{ART}.
$$

---

# 43. 理解 profile

兩個 AI：

$$
A_1,A_2
$$

可能同總分，

但：

$$
A_1
$$

強 reconstruction，

$$
A_2
$$

強 falsification。

---

# 44. Summary Trap

AI A：

> 說得很好。

AI B：

> 說得普通，但 hidden intervention 全對。

工程上：

$$
B
$$

可能更理解。

---

# 45. Fluent Explanation Bias

人類容易被：

$$
\text{fluency}
$$

誤導成：

$$
\text{understanding}.
$$

---

# 46. 因此需要 execution evidence

$$
\boxed{
\text{Can Explain}
\ll
\text{Can Predict Under Intervention}.
}
$$

---

# 47. Reconstruction 仍不是唯一真模型

即使：

$$
\widehat S
$$

通過 tests，

不能推出：

$$
\widehat S=S
$$

在內部實作上相同。

---

# 48. Equivalence Relative to Test Domain

$$
\widehat S
\equiv_{\mathcal T,\epsilon}
S.
$$

---

# 49. 對抗等價也相對

$$
\widehat S
\equiv_{\mathcal A,\mathcal T,\epsilon}^{\mathrm{adv}}
S.
$$

表示在指定 attack / intervention domain 下足夠等價。

---

# 50. Adversarial Equivalence

定義：

$$
d_A(S,\widehat S)
=
\frac1{|\mathcal A|}
\sum_{a\in\mathcal A}
d(
Behavior(S\mid a),
Behavior(\widehat S\mid a)
).
$$

---

# 51. 若：

$$
d_A\le\epsilon_A,
$$

支持：

$$
S
\equiv_A
\widehat S.
$$

---

# 52. 這比正常輸入等價更強

因為 attack domain 專門碰：

- boundaries；
- error states；
- recovery；
- timing；
- authority。

---

# 53. Causal Model Reconstruction

AI 應建立：

$$
G_C
=
(V_C,E_C).
$$

其中：

$$
E_C
$$

表示 engineering causal influence。

---

# 54. Dependency 不等於因果

import：

$$
A\rightarrow B
$$

不代表：

$$
A
$$

是某 failure 的 cause。

---

# 55. 因果需要 intervention evidence

$$
do(A)
$$

改變：

$$
B
$$

才提供較強 support。

---

# 56. State Transition Model

$$
x_{t+1}
=
F(x_t,u_t,\theta_t).
$$

---

# 57. 理解需要預測 $F$

不是只知道：

$$
x_t.
$$

---

# 58. Failure Surface Model

定義：

$$
\mathcal F
=
\{
x:
I(x)=0
\}.
$$

AI 的 adversarial understanding 需要估計：

$$
\partial\mathcal F.
$$

---

# 59. 最有價值的是 boundary

如果 AI 知道：

> 再多一點 delay 就會失敗。

它掌握了 failure boundary。

---

# 60. Failure Margin

$$
m(x)
=
d(x,\mathcal F).
$$

---

# 61. Robustness 不是 pass/fail

可以研究：

$$
m(x).
$$

---

# 62. Attack Generation 應靠近 boundary

比隨機亂破壞更有資訊。

---

# 63. Minimal Counterexample

理想 attack：

$$
a^\ast
=
\arg\min_a
Cost(a)
$$

subject to：

$$
I(T_a(x))=0.
$$

---

# 64. Minimal 不等於唯一

可能有多個。

---

# 65. Counterexample Quality

$$
Q_C
=
\frac{
MechanismClarity
\cdot
DiagnosticValue
}{
PerturbationSize+\epsilon
}.
$$

---

# 66. 對抗理解與 GACEI-05

AI 若真正理解：

$$
Relation(a,b)
$$

才能正確建立：

- synergy；
- masking；
- conflict；
- dependency。

---

# 67. 對抗理解與 GACEI-06

AI 若真正理解 project，

才能：

$$
\text{compress safely}.
$$

---

# 68. Bad Model, Good Test Memory

即使 AMS 很完整，

若：

$$
\widehat{\mathfrak P}
$$

錯，

attack retrieval 仍會錯。

---

# 69. Good Model, Bad Memory

AI 可以重新創造 attacks，

但成本高。

---

# 70. Good Model + Good Memory

已知：

$$
\rightarrow
\text{cheap}.
$$

未知：

$$
\rightarrow
\text{creative}.
$$

---

# 71. Understanding Is Resource Allocation

高 AEU 的 AI 還要知道：

> 哪些地方不值得再理解得更深？

---

# 72. Complete Understanding 通常不必要

只需要：

$$
\boxed{
\text{Sufficient Understanding for Current Decision}.
}
$$

---

# 73. Understanding Budget

$$
B_U
$$

不應無限。

---

# 74. Marginal Understanding Value

$$
MUV(o)
=
\frac{
E[\Delta DecisionQuality]
}{
Cost(o)+\epsilon
}.
$$

---

# 75. 若：

$$
MUV<\lambda_B,
$$

停止。

---

# 76. 理解的停止比理解本身重要

否則 AI 會：

> 再讀一點。

一直讀下去。

---

# 77. Understanding Debt

仍未理解的地方：

$$
D_U.
$$

只要誠實記錄即可。

---

# 78. Debt 不等於 blocker

只有：

$$
D_U
\cap
CriticalDecisionDomain
\neq\varnothing
$$

才阻擋。

---

# 79. False Understanding

定義：

$$
\boxed{
FU
}
$$

當 AI confidence 高，

但 hidden intervention / reconstruction 低。

---

# 80. Overconfident Model

$$
Conf\uparrow,
$$

$$
Accuracy\downarrow.
$$

---

# 81. Calibration

理想：

$$
P(\mathrm{correct}\mid \mathrm{conf}=p)
\approx p.
$$

---

# 82. Unknown-aware AI

知道：

$$
\boxed{
\text{I do not know}
}
$$

是工程能力。

---

# 83. NotMeasured-aware AI

validator 沒測：

$$
\neq
Pass.
$$

---

# 84. Version-aware AI

舊 evidence：

$$
\neq
\text{current truth}.
$$

---

# 85. Authority-aware AI

README：

$$
\neq
\text{canonical contract}
$$

在某些專案成立。

---

# 86. Corpus Understanding 與 Project Understanding

Research corpus：

$$
\mathfrak C
$$

與 runtime project：

$$
\mathfrak P
$$

不同。

---

# 87. U 軸與 L 軸

既有 Research Cognitive Compilation：

$$
U_0\rightarrow U_6
$$

描述 corpus understanding。

---

# 88. Project engineering depth

本文：

$$
U_E^0\rightarrow U_E^5.
$$

---

# 89. 兩者可交叉

AI 可以：

$$
U_6
$$

很高，

但：

$$
U_E^2
$$

低。

也可能相反。

---

# 90. Example：資料找得很準但不會 attack

這是：

$$
\text{High Corpus Understanding}
+
\text{Low Adversarial Understanding}.
$$

---

# 91. Example：只懂一個專案很深

這可能：

$$
U_E^5
$$

高，

但 corpus routing 弱。

---

# 92. AI Architect Benchmark

未來 architect AI 應至少：

$$
U_E^4.
$$

---

# 93. 全域攻擊 AI

理想：

$$
U_E^5.
$$

---

# 94. 但 execution authority 仍分離

即使：

$$
Capability=High,
$$

也不代表：

$$
Authority=High.
$$

---

# 95. Ability / Authority Separation

$$
\boxed{
\text{Can Generate}
\neq
\text{May Execute}.
}
$$

---

# 96. AEU 不增加真實世界攻擊權限

其測試只在 sandbox。

---

# 97. Benchmark Project Design

建立一組 synthetic project：

$$
S_1,\ldots,S_n.
$$

---

# 98. 每個含 hidden defects

分類：

- structural；
- state；
- temporal；
- recovery；
- validator；
- interaction。

---

# 99. 隱藏 attack corpus

AI 不能先看到。

---

# 100. 測 novel generation

看是否重新發現：

$$
F^\ast.
$$

---

# 101. Surface-Changed Transfer

換：

- names；
- language；
- directory；
- UI。

---

# 102. Structure-Preserved Transfer

保留：

$$
(V,E,X,I).
$$

---

# 103. 測真正抽象理解

如果 attack transfer 成功：

$$
AEU\uparrow.
$$

---

# 104. Structure-Changed Negative Control

故意改變：

$$
I
$$

讓舊 attack 不再 applicable。

---

# 105. AI 應拒絕套用

這測：

$$
\text{Non-Overgeneralization}.
$$

---

# 106. AEU Precision

$$
Precision_{AEU}
=
\frac{
ValidGeneratedAttacks
}{
AllGeneratedAttacks
}.
$$

---

# 107. AEU Recall

$$
Recall_{AEU}
=
\frac{
HiddenFailureMechanismsFound
}{
HiddenFailureMechanismsInScope
}.
$$

---

# 108. AEU Efficiency

$$
Efficiency_{AEU}
=
\frac{
WeightedUsefulFindings
}{
ObservationCost+ReasoningCost+ExecutionCost+\epsilon
}.
$$

---

# 109. AEU Transfer

$$
Transfer_{AEU}
=
\frac{
CrossProjectValidAttacks
}{
EligibleTransferredAttacks
}.
$$

---

# 110. AEU Calibration

比較 confidence 與實際 attack validity。

---

# 111. AI 可能高 Recall 低 Precision

一直亂攻。

---

# 112. 也可能高 Precision 低 Recall

過度保守。

---

# 113. 所以需要 frontier

$$
\boxed{
\text{Precision-Recall-Cost Frontier}.
}
$$

---

# 114. 對抗理解與創造

GACEI-09 將處理：

$$
\text{如何從理解生成新的 attack family？}
$$

---

# 115. 本文只建立能力門檻

即：

$$
\boxed{
\text{理解到什麼程度，才有資格談 adversarial creativity？}
}
$$

---

# 116. 最小資格

至少：

1. model；
2. invariant；
3. state；
4. lifecycle；
5. observation；
6. version；
7. authorization。

---

# 117. 缺一不可？

不是所有 attack 都需要所有欄位。

但缺的必須標記：

$$
Unknown
$$

而不是默認。

---

# 118. Failure Hypothesis

定義：

$$
h
=
(P,I,M,E).
$$

其中：

- $P$：precondition；
- $I$：target invariant；
- $M$：mechanism；
- $E$：expected evidence。

---

# 119. Hypothesis 不等於 Attack

還需要：

$$
Generation(h)
\rightarrow
a.
$$

---

# 120. Attack 不等於 Finding

執行後：

$$
a
\rightarrow
Evidence.
$$

---

# 121. Finding 不等於 Root Cause

還需要：

$$
Localization.
$$

---

# 122. 理解鏈

$$
\boxed{
\text{Model}
\rightarrow
\text{Hypothesis}
\rightarrow
\text{Attack}
\rightarrow
\text{Evidence}
\rightarrow
\text{Diagnosis}
\rightarrow
\text{Learning}.
}
$$

---

# 123. 若任一層混淆

可能出現：

- hallucinated attack；
- false green；
- false red；
- wrong localization；
- wrong memory promotion。

---

# 124. 所以 AEU 是鏈條能力

不是單一模型 output。

---

# 125. 多 Agent 也可分工

一個 AI model；

一個 AI falsify；

一個 AI validate。

---

# 126. 但若共享同一 bias

仍可能一起錯。

---

# 127. Independent Perspective Value

因此某些高風險 case 仍值得：

$$
\text{independent reconstruction}.
$$

---

# 128. 但不應每次都做

依：

$$
Risk
+
Uncertainty
+
ClaimImportance.
$$

---

# 129. Understanding Verification Cost

驗證理解本身也有成本：

$$
C_{UV}.
$$

---

# 130. 不要把理解驗收變成另一個永動機

所以 ART 也要 bounded。

---

# 131. ART Stop Rule

若：

- reconstruction gate pass；
- intervention gate pass；
- hidden attack gate pass；
- transfer gate pass；
- residual disclosed；

則停止。

---

# 132. 新反例進 future corpus

不必無限 reopen。

---

# 133. 本文研究假說

## H1：重建能力與對抗理解正相關但不等價

$$
Corr(R,AEU)>0
$$

但：

$$
R\neq AEU.
$$

---

## H2：Intervention test 比摘要評分更能預測 attack quality

$$
PredictivePower(Intervention)
>
PredictivePower(SummaryScore).
$$

---

## H3：Transfer test 能有效區分表面記憶與結構理解

$$
Gap_{\mathrm{transfer}}
$$

應在 memorization-heavy agent 更大。

---

## H4：Adversarial reconstruction 可發現正常重建測試漏掉的模型缺口

存在：

$$
S,\widehat S
$$

使正常 tests 等價，

但 attack domain 不等價。

---

## H5：Residual-aware AI 具有較低 false understanding

明示：

$$
Unknown
$$

的 AI，其 hidden intervention error 應較低。

---

# 134. Benchmark 比較

### A：Summary Model

只做摘要。

### B：Reconstruction Model

重建。

### C：Prediction Model

重建 + intervention。

### D：AEU Model

重建 + intervention + falsification + transfer。

---

# 135. 測量

$$
SummaryAccuracy,
$$

$$
ReconstructionScore,
$$

$$
InterventionFidelity,
$$

$$
NovelAttackPrecision,
$$

$$
HiddenFailureRecall,
$$

$$
LocalizationAccuracy,
$$

$$
TransferScore,
$$

$$
ComputeCost.
$$

---

# 136. 本文非主張

本文不主張：

1. 重建是哲學理解的充分條件；
2. 對抗理解等於主體性；
3. 能生成 attack 就代表高理解；
4. attack 數量代表理解深度；
5. 所有正常行為重建都需要 attack testing；
6. 所有工程系統都有唯一真 causal model；
7. hidden tests 可以完全測盡理解；
8. intervention fidelity 可以證明唯一內部模型；
9. AI 必須知道所有細節才算理解；
10. Summary 沒有價值；
11. 文件解釋沒有價值；
12. 重建必須 bytes identical；
13. 對抗等價是全域安全證明；
14. AEU 高的 AI 應獲得更大 execution authority；
15. adversarial creativity 可以脫離 authorization；
16. 本文方法可用於未授權第三方系統的攻擊能力評估。

本文主張的是：

$$
\boxed{
\text{工程理解的強證據必須跨越描述，進入重建、干預、預測、反例與遷移。}
}
$$

---

# 137. 與 GACEI-07 的關係

GACEI-07 回答：

$$
\boxed{
\text{如何便宜地建立 project model？}
}
$$

本文回答：

$$
\boxed{
\text{怎麼知道這個 project model 真的足夠懂？}
}
$$

---

# 138. 與既有理解驗收的關係

既有原則：

$$
\text{If you really understand it, rebuild it.}
$$

本文增加：

$$
\boxed{
\text{If you adversarially understand it, predict how it can fail and prove that prediction in a sandbox.}
}
$$

---

# 139. 下一篇：對抗性創造與生成

GACEI-09 將正式處理：

$$
\boxed{
\text{Project Model}
+
\text{Attack Memory}
+
\text{Residual Gap}
\rightarrow
\text{Novel Attack Hypothesis}
\rightarrow
\text{Executable Experiment}.
}
$$

也就是把：

- Creativity；
- Generation；

從理解中獨立出來。

---

# 140. 結論

工程 AI 最容易產生的幻覺之一不是亂講技術，而是：

> **它說得太像懂了。**

一份漂亮摘要、一張完整架構圖、一段流暢說明，都可能來自：

$$
\text{high-quality pattern completion}.
$$

真正強的工程理解需要更殘酷的外部證據：

$$
\boxed{
\text{Can you rebuild it?}
}
$$

接著：

$$
\boxed{
\text{Can you predict what happens if I intervene?}
}
$$

再接著：

$$
\boxed{
\text{Can you construct a non-trivial counterexample to its invariants?}
}
$$

最後：

$$
\boxed{
\text{Can you transfer that failure mechanism to a structurally similar but superficially different system?}
}
$$

如果答案都成立，我們才開始有更強理由說：

> 這個 AI 不只是看過、背過、摘要過。

而是：

$$
\boxed{
\text{它建立了一個可以被操作、被反駁、被重建、被遷移的工程世界模型。}
}
$$

因此本文將工程理解的強證據壓縮為：

$$
\boxed{
\text{Understanding}
=
\text{Reconstruction}
+
\text{Prediction}
+
\text{Intervention}
+
\text{Falsification}
+
\text{Transfer}
}
$$

在 GACEI 中，這是 AI 從「會讀專案」走向「能生成全域對抗程序」的真正能力門檻。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
