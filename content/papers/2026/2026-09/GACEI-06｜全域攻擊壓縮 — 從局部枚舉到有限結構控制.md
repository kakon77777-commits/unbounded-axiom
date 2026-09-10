---
title: "GACEI-06｜全域攻擊壓縮：從局部枚舉到有限結構控制"
title_en: "GACEI-06 | Global Adversarial Compression: From Local Enumeration to Finite Structural Control"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-06"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 全域攻擊壓縮 / 覆蓋最佳化 / AI 計算經濟"
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
---

# GACEI-06｜全域攻擊壓縮
## 從局部枚舉到有限結構控制

**英文題名：** Global Adversarial Compression: From Local Enumeration to Finite Structural Control

---

## 摘要

GACEI-01 至 GACEI-05 已依序建立全域對抗計算、MSSP 對抗對偶、局部攻擊抽象、SEDB-style 對抗記憶，以及局部 attack operators 的組合演算。到此為止，AI 已可能擁有大量已知 attacks、attack families、interaction relations、cost profiles、coverage signatures 與 novel attack candidates。但如果系統仍把所有候選 attack、所有 pair、所有 higher-order interaction 全部執行，那麼組合空間將迅速爆炸：

$$
|\mathcal P(A)|=2^{|A|},
$$

若再考慮執行順序，候選 campaign 數量可能更高。

因此全域對抗計算的下一個核心問題不是：

> 如何生成更多 attack？

而是：

$$
\boxed{
\text{如何用有限攻擊結構控制一個遠大於其自身的對抗空間？}
}
$$

本文提出「全域攻擊壓縮」（Global Adversarial Compression, GACmp），將 global campaign synthesis 重新定義為一個多目標、條件化、帶風險與診斷約束的覆蓋壓縮問題。最基本形式為：

$$
\boxed{
\mathcal C^\ast
=
\arg\min_{\mathcal C}
\operatorname{Cost}(\mathcal C)
}
$$

subject to：

$$
\operatorname{Coverage}(\mathcal C)\ge\tau.
$$

但本文指出，單純 set cover 仍不足以描述真正的全域對抗壓縮，因為 attack coverage 至少具有：

- component coverage；
- relation coverage；
- condition coverage；
- path coverage；
- interaction coverage；
- validator coverage；
- recovery coverage；
- version coverage；

而不同 coverage unit 具有不同 risk weight、不同證據品質、不同診斷價值與不同未知程度。因此本文定義多維覆蓋：

$$
\boxed{
\boldsymbol\rho_{\mathcal C}
=
\left(
\rho_N,
\rho_R,
\rho_\Theta,
\rho_P,
\rho_I,
\rho_V,
\rho_{Rec},
\rho_T
\right).
}
$$

其中 $\rho_I$ 特別表示 interaction coverage，不與 invariant symbol 混淆。

本文進一步提出「Globality Certificate」：任何 campaign 若聲稱具有全域覆蓋能力，都必須綁定一個明示 reference frame：

$$
\mathfrak F_G
=
\left(
U,
\mu,
\Theta,
V,
A,
H
\right),
$$

其中 $U$ 為目標 coverage universe， $\mu$ 為權重／測度， $\Theta$ 為條件纖維， $V$ 為版本與 validator profile， $A$ 為 authorization profile， $H$ 為來源與歷史界定。沒有 reference frame 的：

```text
global coverage = 97%
```

不具有穩定工程語義。

本文將 GACEI-05 的 attack interaction hypergraph：

$$
\mathcal H_A
=
(A,\mathcal E,\lambda,\Theta,W)
$$

轉換成 campaign candidate space。每個 attack 或 composite campaign 對 coverage universe 產生一個覆蓋集合：

$$
C(a)\subseteq U,
$$

並攜帶 cost、risk、information gain、diagnosability 與 redundancy。最基本的加權壓縮問題為：

$$
\boxed{
\max_{\mathcal C}
\sum_{u\in U}
w_u
\mathbf 1[
u\text{ covered by }\mathcal C
]
}
$$

subject to：

$$
Cost(\mathcal C)\le B.
$$

更完整形式則加入：

$$
\operatorname{InfoGain},
\quad
\operatorname{RiskResolution},
\quad
\operatorname{Novelty},
\quad
\operatorname{Diagnosability},
\quad
\operatorname{Redundancy}.
$$

因此：

$$
\boxed{
U(\mathcal C)
=
\alpha Cov
+
\beta IG
+
\gamma Risk
+
\delta Novel
-
\eta Cost
-
\mu Red
-
\nu DiagLoss.
}
$$

本文同時提出「攻擊閉包」與「未知殘差」的區分。令目前 known attack knowledge 與可組合關係形成：

$$
\operatorname{Cl}_A(K),
$$

則：

$$
\boxed{
\mathcal R_A
=
U_A
\setminus
\operatorname{Cl}_A(K)
}
$$

表示當前 attack closure 之外的 residual adversarial space。由於真實 attack universe 通常不可完全枚舉，本文不把 $\mathcal R_A$ 當成可精確已知集合，而把它視為由未覆蓋結構、未覆蓋 interaction、未知 validator blind spot、版本差異與新型 failure hypothesis 所形成的條件化殘差描述。

本文最重要的命題之一是：

$$
\boxed{
\text{Globality is not exhaustive enumeration;}
}
$$

而是：

$$
\boxed{
\text{Globality is finite structural control over a declared coverage universe.}
}
$$

這一思想與既有全域量詞壓縮方法論形成呼應，但本文不宣稱軟體 attack coverage 等同數學全稱證明。數學證明中的全域控制可以建立嚴格邏輯蘊涵，而軟體 adversarial campaign 通常只能建立**條件化工程證據與覆蓋聲明**，不能從有限 attack campaign 推出「不存在未知缺陷」。

本文最後提出三層壓縮策略：

$$
\boxed{
\text{Memory Compression}
\rightarrow
\text{Structural Compression}
\rightarrow
\text{Campaign Compression}.
}
$$

第一層避免已知 attack 被重複發明；第二層用 architecture、invariant、state、path 與 interaction 關係剪枝；第三層從剩餘 candidates 中選擇一個 bounded campaign。三層結合後，理想效果是：

$$
\boxed{
\text{more accumulated experience}
\Rightarrow
\text{lower marginal known-assurance cost},
}
$$

讓昂貴前沿 AI 的計算逐步從已知 failure replay 轉向真正未知的 residual space。

**關鍵詞：** Global Adversarial Compression、Attack Set Cover、Coverage Compression、Interaction Coverage、Risk-Weighted Coverage、Information Gain、Globality Certificate、Residual Attack Space、MSSP、SEDB、AI 計算時間經濟學、全域對抗計算

---

# 0. 研究定位與安全範圍

本文研究的是：

$$
\boxed{
\text{authorized adversarial test campaign optimization}
}
$$

其作用域限於：

- 已授權軟體；
- sandbox；
- isolated clone；
- synthetic fixture；
- internal verification runtime；
- 可恢復測試環境。

本文不研究如何壓縮未授權真實系統的攻擊鏈，也不把 campaign optimization 用於降低現實入侵成本。

---

# 1. 為什麼「全部都測」不是全域方法？

## 1.1 枚舉直覺

若有：

$$
n
$$

個 attack operators，

最直接的方法：

$$
A
=
\{a_1,\ldots,a_n\}
$$

全部跑一次。

但若加入 pair interaction：

$$
{n\choose2},
$$

三元 interaction：

$$
{n\choose3},
$$

乃至全部 subset：

$$
2^n.
$$

---

## 1.2 更多不等於更全域

即使：

$$
|\mathcal C|\uparrow,
$$

仍可能：

- 大量 attacks 重複覆蓋同一 invariant；
- 沒有覆蓋關鍵 boundary；
- 沒測 validator blind spot；
- 沒測 recovery；
- 沒測 interaction；
- 沒測版本差異。

所以：

$$
\boxed{
\text{Attack Count}
\neq
\text{Coverage Quality}.
}
$$

---

# 2. Globality Reference Frame

任何 global claim 必須先定義：

$$
\boxed{
\mathfrak F_G
=
\left(
U,
\mu,
\Theta,
V,
A,
H
\right).
}
$$

其中：

$$
U
=
\text{Target Coverage Universe},
$$

$$
\mu
=
\text{Weights / Measure},
$$

$$
\Theta
=
\text{Conditions},
$$

$$
V
=
\text{Version / Validator Profile},
$$

$$
A
=
\text{Authorization Profile},
$$

$$
H
=
\text{History / Provenance Boundary}.
$$

---

## 2.1 Globality 是相對的

同一 campaign：

$$
\mathcal C
$$

對：

$$
\mathfrak F_1
$$

可能 coverage 很高，

對：

$$
\mathfrak F_2
$$

可能很低。

所以：

$$
\boxed{
Global(\mathcal C)
\text{ is reference-frame conditioned}.
}
$$

---

# 3. Coverage Universe

第一版：

$$
U
=
U_N
\cup
U_R
\cup
U_\Theta
\cup
U_P
\cup
U_I
\cup
U_V
\cup
U_{Rec}
\cup
U_T.
$$

---

## 3.1 Node / Component Universe

$$
U_N
$$

包含重要 components / responsibilities。

---

## 3.2 Relation Universe

$$
U_R
$$

包含依賴、資料流、控制流、authority relation。

---

## 3.3 Condition Universe

$$
U_\Theta
$$

包含：

- platform；
- permission；
- mode；
- config；
- resource；
- runtime condition。

---

## 3.4 Path Universe

$$
U_P
$$

包含關鍵 execution / state paths。

---

## 3.5 Interaction Universe

$$
U_I
$$

包含高風險 pair / higher-order interactions。

---

## 3.6 Validator Universe

$$
U_V
$$

包含：

- validators；
- alarms；
- observation contracts；
- NotMeasured boundaries。

---

## 3.7 Recovery Universe

$$
U_{Rec}
$$

包含：

- restart；
- rollback；
- retry；
- restore；
- compensation。

---

## 3.8 Version Universe

$$
U_T
$$

包含：

- current version；
- migration boundary；
- compatibility range；
- stale evidence boundary。

---

# 4. Coverage Vector

定義：

$$
\boxed{
\boldsymbol\rho_{\mathcal C}
=
\left(
\rho_N,
\rho_R,
\rho_\Theta,
\rho_P,
\rho_I,
\rho_V,
\rho_{Rec},
\rho_T
\right).
}
$$

---

## 4.1 平均值不夠

若：

$$
\bar\rho
=
0.9,
$$

但：

$$
\rho_V
=
0.2,
$$

表示 validator coverage 非常差。

所以：

$$
\boxed{
\bar\rho
\text{ cannot replace coverage shape}.
}
$$

---

# 5. Coverage Claim

一個完整 claim 至少應是：

```yaml
coverage_claim:
  reference_frame:
  dimensions:
  weights:
  baseline:
  version:
  authorization:
  measured:
  not_measured:
  unknown:
  residual:
  evidence:
```

---

# 6. Set Cover 基本模型

令候選 attack/composite 集合：

$$
\mathcal A_C
=
\{c_1,\ldots,c_m\}.
$$

每個：

$$
c_i
$$

覆蓋：

$$
S_i
\subseteq
U.
$$

---

## 6.1 最小 cover

$$
\boxed{
\min
\sum_i x_i k_i
}
$$

subject to：

$$
\sum_{i:u\in S_i}x_i
\ge1
$$

對每個必要：

$$
u\in U_{\mathrm{required}}.
$$

---

## 6.2 Budgeted maximum coverage

固定：

$$
B,
$$

求：

$$
\boxed{
\max
\sum_{u\in U}
w_u
\mathbf 1[
u\text{ covered}
]
}
$$

subject to：

$$
\sum_i x_i k_i
\le B.
$$

---

# 7. 為什麼普通 Set Cover 不夠？

因為：

$$
S_i
$$

不是完全靜態。

attack interactions 可能改變 coverage。

例如：

$$
C(a\odot b)
\supset
C(a)\cup C(b).
$$

也可能：

$$
C(a\triangleright b)
\subset
C(a)\cup C(b)
$$

因為 masking 造成觀測損失。

---

# 8. Interaction-Aware Coverage

定義：

$$
C_I(c)
$$

為 composite 的 interaction-specific coverage。

則：

$$
C(c)
=
C_L(c)
\cup
C_I(c).
$$

---

## 8.1 Synergy bonus

若：

$$
C_I(a\odot b)
\neq\varnothing,
$$

表示 pair interaction 有獨立 coverage 價值。

---

# 9. Risk-Weighted Coverage

不同 coverage unit：

$$
u_i
$$

權重不同。

定義：

$$
w(u_i)
=
f(
Severity,
Likelihood,
BlastRadius,
BusinessCriticality,
Uncertainty
).
$$

---

## 9.1 高風險低頻

即使：

$$
P(F_i)
$$

低，

若：

$$
Loss(F_i)
$$

極高，

仍可能：

$$
w_i
$$

高。

---

# 10. Information Gain

attack 的價值不只在命中 defect。

它也可能：

- 排除一個重要 failure hypothesis；
- 驗證 validator；
- 縮小未知域；
- 提升 architecture model。

定義：

$$
IG(c)
=
E[
H(\mathcal B)
-
H(\mathcal B\mid E_c)
].
$$

這裡 $H$ 可代表任何合適的 uncertainty measure，不要求實作一定採 Shannon entropy。

---

# 11. Risk Resolution

定義：

$$
RR(c)
=
\sum_i
w_i
\Delta q_i(c),
$$

其中：

$$
\Delta q_i
$$

表示 attack evidence 對某風險命題不確定性的降低。

---

# 12. Novelty Value

已知 attack replay：

$$
Novel(c)\approx0.
$$

但可能 coverage 很高。

新 attack：

$$
Novel(c)>0,
$$

但成本也高。

所以 novelty 不能單獨最大化。

---

# 13. Redundancy

兩個 candidates：

$$
c_i,c_j
$$

若：

$$
C(c_i)\approx C(c_j)
$$

且 evidence 高度重複，

則：

$$
Red(c_i,c_j)\uparrow.
$$

---

# 14. Marginal Coverage

定義：

$$
\Delta Cov(c\mid\mathcal C)
=
Cov(\mathcal C\cup\{c\})
-
Cov(\mathcal C).
$$

如果：

$$
\Delta Cov\approx0,
$$

則加入：

$$
c
$$

的覆蓋價值低。

---

# 15. Marginal Information Gain

$$
\Delta IG(c\mid\mathcal C)
=
IG(\mathcal C\cup\{c\})
-
IG(\mathcal C).
$$

---

# 16. Marginal Campaign Value

本文定義：

$$
\boxed{
MCV(c\mid\mathcal C)
=
\frac{
\alpha\Delta Cov
+
\beta\Delta IG
+
\gamma\Delta RR
+
\delta Novel
-
\mu\Delta Red
-
\nu\Delta DiagLoss
}{
\Delta Cost+\epsilon
}.
}
$$

---

# 17. Shadow Price

令：

$$
\lambda_B
$$

表示當期有限 AI 計算資源的影子價格。

若：

$$
MCV(c\mid\mathcal C)
<
\lambda_B,
$$

則：

$$
c
\rightarrow
\text{Defer}.
$$

這直接接 AI 計算時間經濟學。

---

# 18. 三層壓縮

本文提出：

$$
\boxed{
\text{Memory Compression}
\rightarrow
\text{Structural Compression}
\rightarrow
\text{Campaign Compression}.
}
$$

---

## 18.1 Memory Compression

由 GACEI-03/04 完成：

$$
\text{many witnesses}
\rightarrow
\text{few reusable operators}.
$$

---

## 18.2 Structural Compression

利用：

- architecture；
- invariant；
- state；
- path；
- ownership；
- interaction；

剪掉無意義 candidates。

---

## 18.3 Campaign Compression

在剩餘 candidates 中：

$$
\operatorname{Select}
(
Coverage,
Risk,
Info,
Cost,
Diag
).
$$

---

# 19. Architecture-Induced Pruning

若 attack：

$$
a
$$

與：

$$
b
$$

作用於 causal-disconnected structures，

則：

$$
Priority(a\odot b)
\downarrow.
$$

---

# 20. Dependency Path Compression

如果多個 attack 都在測同一：

$$
v_1\rightarrow v_2\rightarrow v_3
$$

path，

可能選一個能穿透整條 path 的 composite，而不是三個近似重複 test。

---

# 21. Invariant Representative

若：

$$
a_1,\ldots,a_k
$$

都對同一 invariant family 提供近似相同 evidence，

可以找：

$$
a^\ast
$$

作 representative。

但必須保留：

$$
\text{representation loss}.
$$

---

# 22. Representative 不是 Proof

即使：

$$
a^\ast
$$

代表一組 attacks，

不能宣稱：

$$
a^\ast
\Rightarrow
\forall a_i.
$$

除非有額外結構保證。

---

# 23. Global Quantifier Compression 的有限類比

既有全域量詞壓縮研究處理：

$$
Q(\mathfrak G(D))
\Rightarrow
\forall x\in D\,P(x).
$$

GACmp 的類比是：

$$
\mathcal C^\ast
\Rightarrow
\text{high coverage over declared }U.
$$

但：

$$
\boxed{
\text{Coverage Evidence}
\neq
\text{Mathematical Universal Proof}.
}
$$

---

# 24. Globality Certificate

本文提出：

$$
\boxed{
GC(\mathcal C)
}
$$

至少包含：

```yaml
globality_certificate:
  campaign_id:
  baseline:
  reference_frame:
  coverage_vector:
  weighted_coverage:
  interaction_coverage:
  required_units:
  measured_units:
  unknown_units:
  not_measured_units:
  residual_gaps:
  diagnostic_quality:
  cost:
  authorization:
  evidence_refs:
  limitations:
```

---

# 25. Certificate 的核心用途

它防止：

$$
\boxed{
\text{large test run}
\rightarrow
\text{fake global claim}.
}
$$

---

# 26. Required Coverage

定義：

$$
U_{\mathrm{req}}
\subseteq
U.
$$

對 release-critical invariants：

$$
u\in U_{\mathrm{req}},
$$

要求：

$$
Covered(u,\mathcal C)=1
$$

或明確：

$$
NotMeasured(u).
$$

---

# 27. Optional Coverage

$$
U_{\mathrm{opt}}
$$

可以依：

$$
MCV
$$

決定是否本輪執行。

---

# 28. Unknown Universe

真實：

$$
U^\ast
$$

往往未知。

我們只能有：

$$
\widehat U.
$$

所以：

$$
\boxed{
Coverage(\widehat U)
=1
\not\Rightarrow
Coverage(U^\ast)=1.
}
$$

---

# 29. Open-Denominator Attack Coverage

新 architecture insight、attack family、version 或 validator blind spot 可能擴張：

$$
\widehat U_t
\rightarrow
\widehat U_{t+1}.
$$

因此 coverage 可下降，即使已測項目增加。

---

# 30. Attack Closure

令：

$$
K
$$

為 known attack knowledge，

$$
\mathcal O
$$

為允許的 composition operators。

定義：

$$
\boxed{
Cl_A(K\mid\mathcal O,\Theta,B)
}
$$

表示在指定：

- operator grammar；
- condition；
- budget；

下可生成的 attack closure。

---

# 31. Closure 不是無限實際 materialization

系統不必真的列舉：

$$
Cl_A.
$$

可以保存：

- grammar；
- family；
- constraints；
- generators。

---

# 32. Residual Attack Space

定義概念性：

$$
\boxed{
R_A
=
U_A
\setminus
Cl_A(K).
}
$$

但由於：

$$
U_A
$$

一般未知，

實作上應保存：

$$
\widehat R_A
$$

作為 residual gap profile。

---

# 33. Residual Gap Profile

可以包含：

```yaml
residual:
  uncovered_structures:
  uncovered_relations:
  uncovered_paths:
  uncovered_conditions:
  unknown_interactions:
  weak_validators:
  stale_versions:
  unexplained_failures:
  high-risk-unmodeled:
```

---

# 34. Residual Priority

$$
Priority(r)
=
\frac{
Risk(r)
\cdot
Uncertainty(r)
\cdot
Reachability(r)
}{
ExpectedCost(r)+\epsilon
}.
$$

---

# 35. Novel Attack Synthesis 只處理 Residual

因此：

$$
\boxed{
\text{Known Coverage}
\rightarrow
\text{Cheap Replay},
}
$$

$$
\boxed{
\text{Residual Coverage}
\rightarrow
\text{Frontier Synthesis}.
}
$$

---

# 36. Greedy Compression

如果 coverage function 接近 diminishing return，

可以用 greedy heuristic：

$$
c^\ast
=
\arg\max_c
MCV(c\mid\mathcal C).
$$

逐步加入。

---

## 36.1 本文不預設次模性

不能無條件宣稱：

$$
Cov
$$

是 submodular。

因為 synergy attack 可能：

$$
\Delta Cov(c\mid A)
<
\Delta Cov(c\mid B)
$$

對：

$$
A\subset B.
$$

這違反典型 diminishing returns。

---

# 37. Synergy 造成 Supermodular Region

若 interaction：

$$
a\odot b
$$

具有新增 coverage，

可能出現局部：

$$
\boxed{
\text{increasing returns}.
}
$$

所以普通 greedy set cover 保證不能直接套用。

---

# 38. Hybrid Selection

本文建議第一版：

1. mandatory singles；
2. known high-value interactions；
3. greedy residual cover；
4. architecture-guided higher-order candidates；
5. diagnostic reserve。

---

# 39. Mandatory Singles

有些 attack 必須單獨跑，因為：

- validator control；
- baseline sanity；
- known blocker regression；
- independent evidence。

它們不應被 compression 刪掉。

---

# 40. Interaction Core

令：

$$
E_I^{\mathrm{core}}
$$

為歷史高風險 interaction。

必須納入：

$$
\mathcal C.
$$

---

# 41. Diagnostic Reserve

預留：

$$
B_D
\subset B
$$

給：

- counterfactual replay；
- failed composite split；
- validator retest。

---

# 42. Budget Partition

可寫：

$$
B
=
B_K
+
B_I
+
B_N
+
B_D,
$$

其中：

- $B_K$：known replay；
- $B_I$：interaction；
- $B_N$：novel synthesis；
- $B_D$：diagnosis。

---

# 43. Budget 不應固定比例

不同 project：

$$
B_K:B_I:B_N:B_D
$$

應動態配置。

---

# 44. Known-heavy 專案

若：

$$
Coverage(K)
$$

很高，

可降低：

$$
B_N.
$$

---

# 45. Novel architecture

若：

$$
Match(K,S)
$$

很低，

提高：

$$
B_N.
$$

---

# 46. Validator-weak 專案

若：

$$
\rho_V
$$

低，

提高：

$$
B_D.
$$

---

# 47. Pareto Frontier

多目標 campaign 不必只有唯一 scalar optimum。

可以保留：

$$
\boxed{
\mathcal P^\ast
=
\text{Pareto Frontier}
}
$$

例如：

- low-cost profile；
- balanced profile；
- deep-assurance profile。

---

# 48. Assurance Profiles

## Fast

低成本、高風險核心。

## Standard

預設 release profile。

## Deep

高 interaction / recovery / validator coverage。

---

# 49. Profile 不等於固定 Attack List

同一：

$$
\text{Standard}
$$

對不同 project 應生成不同：

$$
\mathcal C.
$$

---

# 50. Campaign Compression Ratio

定義：

$$
\boxed{
CR_C
=
\frac{
|\mathcal A_{\mathrm{eligible}}|
}{
|\mathcal C^\ast|
}.
}
$$

---

# 51. Ratio 大不一定好

若：

$$
CR_C\gg1
$$

但 defect recall 大幅下降，

是過度壓縮。

---

# 52. Effective Compression

定義：

$$
ECR
=
CR_C
\cdot
Q_{\mathrm{coverage}}
\cdot
Q_{\mathrm{diag}}.
$$

---

# 53. Compute Saving

若 full enumeration cost：

$$
C_F,
$$

compressed campaign：

$$
C_C,
$$

則：

$$
Saving
=
C_F-C_C.
$$

---

# 54. Knowledge-Amortized Cost

隨專案：

$$
S_1,\ldots,S_n,
$$

attack memory 增長，

定義：

$$
\bar C_n
=
\frac{
\sum_{i=1}^{n}C_i
}{
n
}.
$$

理想：

$$
\frac{d\bar C_n}{dn}<0
$$

在某一階段成立。

---

# 55. 不會永遠下降

新 architecture、toolchain、platform 可能使：

$$
\bar C_n
$$

重新上升。

所以：

$$
\boxed{
\text{Learning Curve}
\neq
\text{Monotone Forever}.
}
$$

---

# 56. Value of Experience

定義：

$$
VoE_n
=
C_{\mathrm{from\ scratch}}
-
C_{\mathrm{memory-assisted}}.
$$

---

# 57. MSSP 的壓縮優勢

MSSP 顯式：

- responsibility；
- boundary；
- dependency；
- invariant；

因此：

$$
C(a)
$$

較容易映射到：

$$
U.
$$

---

# 58. MSSP 的代表性 Attack

如果某 attack template 能對整類：

$$
PeerBoundary
$$

建立代表性 coverage，

它可以取代大量 literal peer-pair scripts。

---

# 59. 但 Peer Pair Interaction 仍可能不同

因此：

$$
\text{Family Coverage}
\neq
\text{All Pair Interaction Coverage}.
$$

需要分開聲明。

---

# 60. Compression Certificate

任何壓縮 campaign 應保存：

$$
\boxed{
\text{What was removed and why?}
}
$$

---

## 60.1 Removed candidate reasons

```text
REDUNDANT
NOT_APPLICABLE
CONFLICTING
MASKED
LOW_MCV
COVERED_BY_REPRESENTATIVE
OVER_BUDGET
DEFERRED_NOVEL
UNAUTHORIZED
STALE
```

---

# 61. Compression Debt

被刪掉的 candidates 形成：

$$
D_C.
$$

不是消失。

---

# 62. Deferred Debt

$$
D_{\mathrm{defer}}
$$

可在 deep profile 或未來版本處理。

---

# 63. Release Claim 與 Compression Debt

若：

$$
D_C
$$

包含 release-critical unit，

不能宣稱該 coverage complete。

---

# 64. Globality Score

本文不建議用單一 score 取代 vector。

但若需要 ranking，可定義：

$$
GScore(\mathcal C)
=
f(
\boldsymbol\rho,
Risk,
Diag,
Cost,
Residual
).
$$

---

# 65. Score 必須可展開

任何：

$$
GScore
$$

都必須能展開回：

- coverage vector；
- risk weighting；
- residual；
- unknown；
- NotMeasured。

---

# 66. False Globality

定義：

$$
\boxed{
\text{False Globality}
}
$$

指 campaign 宣稱 global，但實際：

- 分母未定；
- residual 未揭露；
- validator coverage 低；
- interaction 未測；
- version mismatch；
- authorization 不完整。

---

# 67. Globality Audit

可檢查：

1. reference frame fixed？
2. required units covered？
3. unknown disclosed？
4. NotMeasured separated？
5. interaction profile？
6. diagnostics sufficient？
7. version bound？
8. evidence replayable？

---

# 68. 全域不是 100%

一個 engineering global campaign 可以：

$$
\rho<1
$$

但仍合理稱為：

> global campaign under declared reference frame

如果它覆蓋整體架構的主要維度並誠實揭露 residual。

---

# 69. 100% 也可能不全域

如果：

$$
\rho_N=1
$$

但只數 nodes，

仍不是：

$$
\text{global}.
$$

---

# 70. Adaptive Compression

campaign 執行後：

$$
E_t
$$

可能改變 posterior risk。

因此：

$$
\mathcal C_{t+1}
=
Replan(
\mathcal C_t,
E_t
).
$$

---

# 71. Adaptive 不等於無限

必須有：

- max replans；
- max cost；
- max wall-clock；
- stop threshold。

---

# 72. Early Stop

若：

$$
P(\text{release blocker}\mid E)
$$

已低於門檻，

且 required coverage 完成，

可停止。

---

# 73. Early Escalate

若：

$$
E
$$

發現 catastrophic interaction，

可：

$$
\text{Standard}
\rightarrow
\text{Deep}
$$

局部升級。

---

# 74. Reopen 也要有理由

不能：

> AI 又想到一個 attack。

就自動：

$$
Reopen=1.
$$

應要求：

$$
\Delta Claim
+
\Delta Risk
+
\Delta Coverage
$$

足夠大。

---

# 75. Attack Portfolio

最終 campaign 可視為：

$$
\boxed{
\text{Adversarial Portfolio}.
}
$$

類似有限資源下的風險投資組合。

---

# 76. Portfolio Diversification

避免全部 attacks 都集中同一：

- family；
- component；
- validator。

---

# 77. Concentration Risk

定義：

$$
Concentration(\mathcal C)
$$

衡量 coverage 是否過度集中。

---

# 78. Worst-Dimension Constraint

可要求：

$$
\min_j\rho_j
\ge\tau_{\min}.
$$

避免平均值掩蓋短板。

---

# 79. Critical-Dimension Constraint

例如 commercial storage runtime：

$$
\rho_{\mathrm{state}},
\rho_{\mathrm{recovery}},
\rho_{\mathrm{version}}
$$

門檻可更高。

---

# 80. Risk-Aware Objective

$$
U(\mathcal C)
=
\sum_j
w_j\rho_j
-
\lambda Cost
-
\mu ResidualRisk.
$$

---

# 81. Residual Risk

$$
RR_{\mathrm{res}}
=
\sum_{u\in U_{\mathrm{uncovered}}}
w_u
q_u.
$$

---

# 82. Unknown Risk

Unknown：

$$
q_u
$$

不能假設：

$$
0.
$$

可以保存 interval：

$$
q_u
\in
[\ell_u,h_u].
$$

---

# 83. Conservative Profile

對 high-stakes release：

使用：

$$
h_u
$$

作 upper-bound risk estimate。

---

# 84. Exploratory Profile

研究性專案可使用較寬 uncertainty tolerance。

---

# 85. Campaign Planner 的輸入

```yaml
planner_input:
  project_model:
  attack_memory:
  interaction_graph:
  reference_frame:
  risk_weights:
  authorization:
  compute_budget:
  diagnostic_budget:
  assurance_profile:
```

---

# 86. Planner Output

```yaml
campaign:
  selected_attacks:
  selected_interactions:
  lanes:
  schedule:
  snapshots:
  expected_coverage:
  expected_cost:
  diagnostic_reserve:
  residual:
  excluded_candidates:
  globality_certificate_draft:
```

---

# 87. Planner 不直接證明安全

它只產生：

$$
\boxed{
\text{Best Bounded Campaign Under Current Model}.
}
$$

---

# 88. Model Error

若：

$$
\widehat S
\neq
S,
$$

compression 可能錯。

所以 global campaign 需要 observation-quality metadata。

---

# 89. Model Confidence

定義：

$$
Q_S
=
f(
StructureCoverage,
InvariantCoverage,
StateCoverage,
VersionConfidence
).
$$

---

# 90. Low Model Confidence

若：

$$
Q_S<\tau_S,
$$

應先：

$$
\text{Observe More}
$$

而不是急著壓縮 campaign。

---

# 91. Compression Depends on Understanding

所以：

$$
\boxed{
\text{Bad Understanding}
\rightarrow
\text{Bad Compression}.
}
$$

這直接連到後面的 GACEI-07 / 08。

---

# 92. Compression Depends on Memory Quality

若 AMS：

$$
K_A
$$

含大量 false applicability，

則：

$$
\mathcal C^\ast
$$

也會失真。

---

# 93. Compression Depends on Interaction Knowledge

若：

$$
a\odot b
$$

synergy 未被記錄，

planner 可能錯誤刪除 $b$。

---

# 94. Compression 是全系列的中間樞紐

前半：

$$
\text{Attack Knowledge}
\rightarrow
\text{Compression}.
$$

後半：

$$
\text{Attention / Understanding / Creativity}
\rightarrow
\text{Better Compression}.
$$

---

# 95. AI Benchmark

給模型相同：

- project；
- attack memory；
- budget；

比較：

### A：Enumerate

大量全部跑。

### B：Random Sample

固定 budget 隨機選。

### C：Risk-only

只選高 severity。

### D：GACmp

coverage + interaction + info + cost + diagnosis。

測：

$$
\text{Defect Recall},
$$

$$
\text{Weighted Coverage},
$$

$$
\text{Interaction Recall},
$$

$$
\text{Compute Cost},
$$

$$
\text{Diagnostic Quality},
$$

$$
\text{Residual Honesty}.
$$

---

# 96. Compression Efficiency

定義：

$$
CE
=
\frac{
WeightedCoverage
\cdot
DiagnosticQuality
}{
Cost+\epsilon
}.
$$

---

# 97. Discovery Efficiency

$$
DE
=
\frac{
NovelUsefulFindings
}{
FrontierCompute+\epsilon
}.
$$

---

# 98. Experience Efficiency

$$
EE
=
\frac{
KnownAttackCoverage
}{
KnownAttackReasoningCost+\epsilon
}.
$$

AMS 成熟後：

$$
EE\uparrow
$$

應是理想方向。

---

# 99. 研究假說

## H1：Structural compression 可顯著降低 campaign size

存在 project family，使：

$$
|\mathcal C^\ast|
\ll
|\mathcal A_{\mathrm{eligible}}|
$$

且 weighted defect recall 保持接近。

---

## H2：Interaction-aware compression 優於 plain set cover

若存在 synergy / masking，

則：

$$
Quality_{\mathrm{interaction-aware}}
>
Quality_{\mathrm{plain-cover}}.
$$

---

## H3：Coverage shape 約束優於單一平均 coverage

加入：

$$
\min_j\rho_j\ge\tau_j
$$

可降低短板漏測。

---

## H4：Memory growth 可降低 known-assurance marginal cost

對成熟 project family：

$$
\frac{dC_{\mathrm{known}}}{d|K_A|}<0
$$

在一定區間成立。

---

## H5：Residual-honest planner 比 fake-100% planner 更可校準

明示：

$$
Unknown
+
NotMeasured
+
Residual
$$

的 planner，其 post-release surprise rate 應較低。

---

# 100. 本文非主張

本文不主張：

1. 所有 attack coverage 都能精確 set-cover 化；
2. coverage function 必然次模；
3. greedy 一定近似最優；
4. 所有 synergy 都可預先知道；
5. global campaign 可以證明軟體無未知缺陷；
6. 100% declared coverage 等於 real-world safety；
7. attack universe 可以完全枚舉；
8. residual risk 可以精確量化；
9. weighted coverage 可以替代人工工程判斷；
10. campaign 越小越好；
11. compression ratio 越高越好；
12. 所有 attack family 都可用一個 representative 取代；
13. MSSP 是唯一能做 structural compression 的架構；
14. high-value interaction 必須全部在同一輪跑；
15. adaptive replanning 應無限持續；
16. 本文方法可用於未授權真實系統 attack optimization。

本文主張的是：

$$
\boxed{
\text{全域 attack 的價值來自有限結構控制，而不是局部 attack 枚舉。}
}
$$

---

# 101. 與 GACEI-01 至 05 的關係

GACEI-01：

$$
\text{Why global?}
$$

GACEI-02：

$$
\text{How global failures project locally?}
$$

GACEI-03：

$$
\text{How local attacks become reusable?}
$$

GACEI-04：

$$
\text{How reusable knowledge persists?}
$$

GACEI-05：

$$
\text{How attacks compose?}
$$

本文：

$$
\boxed{
\text{How do we choose the smallest high-value global composition?}
}
$$

---

# 102. 下一篇：一眼理解專案

GACEI-07 將從 campaign 反過來問：

> 壓縮需要 architecture model，那 AI 怎麼在有限觀察下快速取得足夠好的全域 project model？

核心將接：

- OAC；
- observation budget；
- multi-scale attention；
- topology；
- relation；
- state；
- invariant；
- active observation；
- project global field。

---

# 103. 結論

如果一個 AI 已經記得：

$$
1000
$$

個局部 attack，

又能生成：

$$
10000
$$

個新候選，

那不表示它應該：

$$
11000
$$

個全部執行。

真正高階的工程智能必須知道：

$$
\boxed{
\text{哪些 attack 不需要再跑？}
}
$$

$$
\boxed{
\text{哪些 attack 可以代表一整類 coverage？}
}
$$

$$
\boxed{
\text{哪些 interaction 必須保留？}
}
$$

$$
\boxed{
\text{哪些未知 residual 值得昂貴 reasoning？}
}
$$

因此本文把 global campaign 的核心從：

$$
\text{Attack Enumeration}
$$

改寫成：

$$
\boxed{
\text{Finite Structural Control}.
}
$$

其最簡單公式為：

$$
\boxed{
\min Cost(\mathcal C)
\quad
\text{subject to}
\quad
Coverage(\mathcal C)\ge\tau.
}
$$

但真正完整版本還需要：

$$
\boxed{
Coverage
+
Interaction
+
Risk
+
Information
+
Diagnosability
+
Residual Honesty.
}
$$

所以最終目標不是：

> **測得最多。**

而是：

> **用最少但足夠的有意義對抗計算，控制最大且明示的工程風險域，並誠實留下尚未被控制的未知殘差。**

這就是「全域攻擊壓縮」的第一版。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
