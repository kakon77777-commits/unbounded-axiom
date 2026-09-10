---
title: "GACEI-01｜全域對抗計算總論：為什麼局部攻擊不應永遠局部執行"
title_en: "GACEI-01 | General Theory of Global Adversarial Computation: Why Local Attacks Should Not Remain Local Forever"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-01"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 理論總論 / AI 工程智能 / 授權式軟體對抗驗證"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
---

# GACEI-01｜全域對抗計算總論
## 為什麼局部攻擊不應永遠局部執行

**英文題名：** General Theory of Global Adversarial Computation: Why Local Attacks Should Not Remain Local Forever

---

## 摘要

傳統軟體測試、除錯、模糊測試、故障注入與對抗性驗證，經常採取局部循環：發現一個缺陷、施加一次局部攻擊、修復該缺陷、重新驗證，再前往下一個局部區域。這種方法在小型系統與低耦合工程中具有直覺性，但當人工智慧開始能同時閱讀大型 repository、重建架構、生成測試、控制工具、比較多個 execution trace，並在多 Agent 或長上下文環境中持續工作時，局部攻擊逐輪展開可能產生新的計算浪費：大量重複閱讀、重複建模、反覆切換 baseline、局部修復造成測試對象持續漂移，以及「只要仍能想到新反例就繼續」的無限驗證傾向。

本文提出「全域對抗計算」（Global Adversarial Computation, GAC）作為一種軟體工程與 AI 工程智能研究框架。GAC 的核心不是把攻擊數量增加到極大，而是把一組具有明示前提、目標不變量、擾動算子、觀測器、驗證器、成本與交互關係的局部對抗操作，經過抽象化、相容性分析、干涉分析、覆蓋壓縮與執行編排，合成一個針對固定系統 baseline 的有限全域對抗 campaign。該 campaign 在授權、隔離、可恢復的測試環境內一次取得整體缺陷表面，再把全域失敗投影回局部元件、關係、狀態、條件、路徑或驗證邊界。

本文首先區分：

$$
\text{Many Local Attacks}
\neq
\text{Global Adversarial Computation}.
$$

「全域」不是 attack count 的基數性描述，而是對系統整體結構、關係與失敗域具有控制能力的結構性性質。本文將局部攻擊表示為：

$$
a_i
=
\left(
P_i,
T_i,
I_i,
O_i,
V_i,
C_i,
K_i
\right),
$$

其中 $P_i$ 為適用前提， $T_i$ 為擾動算子， $I_i$ 為目標不變量， $O_i$ 為觀測方案， $V_i$ 為驗證或警報機制， $C_i$ 為覆蓋描述， $K_i$ 為成本與資源需求。局部攻擊之間另存在並行、先後、遮蔽、衝突、協同與依賴等關係，因此全域 campaign 不能被簡化為局部攻擊集合的無序聯集。

本文進一步提出「一次型全域攻擊」的最低流程：

$$
\text{Baseline Freeze}
\rightarrow
\text{Global Campaign Synthesis}
\rightarrow
\text{Bounded Execution}
\rightarrow
\text{Global Observation}
\rightarrow
\text{Defect Surface Construction}
\rightarrow
\text{Local Projection}
\rightarrow
\text{Repair Wave}
\rightarrow
\text{Confirmation Campaign}.
$$

在第一輪全域 campaign 完成前，不對被測 baseline 逐點修補，使所有主要觀測共享同一系統版本與狀態參考。這可避免：

$$
a_1(S_0),
a_2(S_1),
a_3(S_2),
\ldots
$$

被誤認成同一 baseline 的全域風險圖。

本文同時提出以多維攻擊覆蓋向量取代單一百分比：

$$
\boldsymbol{\rho}_{A}
=
\left(
\rho^{N},
\rho^{R},
\rho^{\Theta},
\rho^{P},
\rho^{V},
\rho^{T}
\right),
$$

分別描述元件或內容、關係、條件、路徑、驗證、時間與版本等維度的覆蓋。再以 A/B observation、validator 與 alarm 交叉建立缺陷、盲區、誤報與正常狀態的判定矩陣。

本文並提出 MSSP 的第一個全域對抗對偶：

$$
\boxed{
\text{Local Responsibility}
\leftrightarrow
\text{Global Perturbation}
}
$$

以及：

$$
\boxed{
\text{Global Attack}
\xrightarrow{\text{Structural Projection}}
\text{Local Diagnosis}.
}
$$

MSSP 顯式化元件、狀態、依賴與責任邊界，因此特別適合作為 GAC 的第一個實驗載體：全域 campaign 可以擴大擾動範圍，而失敗仍可依結構投影回局部責任域。

最後，本文把局部攻擊視為可累積的工程知識，而非一次性測試。任何新失敗若成功形成可驗證反例，都可以經過抽象化成 attack template 或 attack family，保存至特化的 SEDB 類對抗記憶層：

$$
K_{t+1}
=
K_t
\cup
\operatorname{Abstract}
\left(
A_t^{\mathrm{novel}}
\right).
$$

未來 AI 的目標不應是重複花費高階推理資源重新發明已知攻擊，而應在已知全域覆蓋之外搜尋新的結構性殘差。由此，GAC 不只是軟體驗證方法，也可成為衡量未來 AI 全域注意力、架構理解、解析、創造、生成、計算、驗證、定位與學習能力的工程智能基礎。

**關鍵詞：** 全域對抗計算、Global Adversarial Computation、MSSP、全域攻擊、局部攻擊、對抗性驗證、軟體免疫記憶、SEDB、AI 工程智能、全域注意力、攻擊組合、覆蓋壓縮、缺陷表面、驗證器、警報器、計算資源配置

---

# 0. 研究定位與安全範圍

本文中的「攻擊」「滲透」「對抗」僅指：

> 在具有明確授權、隔離、可恢復、可觀測與可終止條件的軟體副本、測試環境、synthetic runtime、sandbox 或研究系統中，故意施加結構、狀態、語義、時間、權限、恢復或驗證層擾動，以評估系統缺陷、驗證盲區與 AI 工程能力。

本文不提供未授權入侵第三方系統的方法，不把現實網路攻擊當成研究目標，也不主張「全域」等於對外部世界無限制擴散。

本文研究的是：

$$
\boxed{
\text{Whole-System Adversarial Simulation}
}
$$

而不是：

$$
\boxed{
\text{Unauthorized Real-World Intrusion}.
}
$$

兩者必須保持明確區分。

---

# 1. 問題：為什麼局部攻擊會變成計算黑洞？

## 1.1 傳統局部循環

最常見的驗證流程可以寫成：

$$
S_0
\xrightarrow{a_1}
F_1
\xrightarrow{r_1}
S_1
\xrightarrow{a_2}
F_2
\xrightarrow{r_2}
S_2
\rightarrow
\cdots
$$

其中：

- $S_i$：第 $i$ 次修復後的系統；
- $a_i$：第 $i$ 個局部攻擊；
- $F_i$：觀測到的失敗；
- $r_i$：修復。

這個流程本身沒有錯。

但它有三個結構性成本。

第一，測試 baseline 不斷改變。

第二，新的 Agent 或新的 reasoning turn 經常重新理解整個局部上下文。

第三，若沒有停止條件，任何新反例都可以再次開啟下一輪。

因此：

$$
\boxed{
\text{Local Falsifiability}
\not\Rightarrow
\text{Efficient Global Assurance}.
}
$$

## 1.2 局部修復造成 baseline 漂移

若第一個 attack 作用於 $S_0$，第二個 attack 作用於 $S_1$，第三個 attack 作用於 $S_2$，則最後資料集是：

$$
\mathcal E
=
\left\{
a_1(S_0),
a_2(S_1),
a_3(S_2),
\ldots
\right\}.
$$

這並不是：

$$
\left\{
a_1(S^\ast),
a_2(S^\ast),
a_3(S^\ast),
\ldots
\right\}
$$

對同一 baseline 的觀測。

所以若研究目標是建立：

$$
\text{Global Defect Surface},
$$

逐點修復會污染比較基礎。

## 1.3 AI 會放大這個問題

高能力 AI 特別擅長：

$$
\text{Rule}
\rightarrow
\text{Negation}
\rightarrow
\text{Counterexample}.
$$

當系統 invariant 很清楚時，新的反例生成成本可能很低。

這造成一種特殊現象：

$$
\text{Architectural Legibility}
\uparrow
\Rightarrow
\text{Adversarial Legibility}
\uparrow.
$$

架構越容易理解，越容易知道怎麼故意違反它。

這是可測試性與可攻擊性的共同來源，而不是矛盾。

---

# 2. 全域對抗計算的基本定義

## 2.1 被測系統

定義被測系統：

$$
\mathcal S
=
\left(
V,
E,
X,
I,
O,
\Gamma
\right),
$$

其中：

- $V$：元件、模組、actor 或責任單元；
- $E$：合法關係、依賴、資料流、控制流；
- $X$：狀態空間；
- $I$：不變量與契約；
- $O$：可觀測表面；
- $\Gamma$：版本、環境、權限、資源與執行條件。

## 2.2 局部攻擊算子

定義局部 attack：

$$
a_i
=
\left(
P_i,
T_i,
I_i,
O_i,
V_i,
C_i,
K_i
\right).
$$

其中：

$$
P_i
=
\text{Applicability Preconditions},
$$

$$
T_i
=
\text{Perturbation Operator},
$$

$$
I_i
=
\text{Target Invariant Set},
$$

$$
O_i
=
\text{Observation Plan},
$$

$$
V_i
=
\text{Validator / Alarm Contract},
$$

$$
C_i
=
\text{Coverage Signature},
$$

$$
K_i
=
\text{Resource and Execution Cost}.
$$

因此：

$$
\boxed{
\text{Attack}
\neq
\text{Arbitrary Bad Input}.
}
$$

一個可重用 attack 必須知道：在什麼條件下適用、故意改變什麼、希望破壞什麼、如何知道真的命中、覆蓋哪些結構、成本多少。

## 2.3 全域 campaign

全域 campaign 不是簡單集合：

$$
\mathcal A_G
\neq
\{a_1,a_2,\ldots,a_n\}.
$$

而是：

$$
\boxed{
\mathcal A_G
=
\operatorname{Compose}
\left(
\mathcal A_L,
\Pi,
\Lambda,
B
\right),
}
$$

其中：

- $\mathcal A_L$：局部 attack 候選集合；
- $\Pi$：組合與排程拓撲；
- $\Lambda$：相容、衝突、遮蔽、依賴與協同關係；
- $B$：總預算。

這使 GAC 成為：

$$
\boxed{
\text{Adversarial Program Synthesis}
}
$$

而不只是：

$$
\boxed{
\text{Test Enumeration}.
}
$$

---

# 3. 全域不是「很多」

## 3.1 攻擊數量不等於全域性

即使：

$$
|\mathcal A|=10^6,
$$

仍不能推出：

$$
\mathcal A
=
\text{Global}.
$$

如果一百萬個 attack 都只覆蓋同一 API 的輸入邊界，它們仍可能具有極高局部密度與極低結構全域性。

所以：

$$
\boxed{
\text{Globality}
\neq
\text{Cardinality}.
}
$$

## 3.2 全域性的最低要求

一個 attack campaign 若要稱為全域，至少應能明示其 reference frame，並對多個相互獨立的結構維度形成覆蓋。

本文提出第一版多維攻擊覆蓋向量：

$$
\boldsymbol{\rho}_{A}
=
\left(
\rho^{N},
\rho^{R},
\rho^{\Theta},
\rho^{P},
\rho^{V},
\rho^{T}
\right).
$$

其中：

$$
\rho^{N}
=
\text{Component / Node Coverage},
$$

$$
\rho^{R}
=
\text{Relation / Dependency Coverage},
$$

$$
\rho^{\Theta}
=
\text{Condition / Scope Coverage},
$$

$$
\rho^{P}
=
\text{Path / Interaction Coverage},
$$

$$
\rho^{V}
=
\text{Validation / Detection Coverage},
$$

$$
\rho^{T}
=
\text{Time / Version Coverage}.
$$

因此：

$$
\rho^{N}=1
$$

不代表：

$$
\rho^{R}
=
\rho^{\Theta}
=
\rho^{P}
=
\rho^{V}
=
\rho^{T}
=
1.
$$

## 3.3 全域壓縮問題

真正有價值的問題不是：可以生成多少 attack？

而是：是否存在一個較小的 attack 結構，可以控制或覆蓋一大片原本需要逐項測試的攻擊域？

令候選 attack 集合為：

$$
\mathcal A
=
\{a_1,\ldots,a_n\}.
$$

令成本為：

$$
c(a_i).
$$

則可研究：

$$
\boxed{
\mathcal A^\ast
=
\arg\min_{\mathcal B\subseteq\mathcal A}
\sum_{a_i\in\mathcal B}c(a_i)
}
$$

subject to：

$$
\operatorname{Coverage}(\mathcal B)
\geq
\tau.
$$

更一般地：

$$
\mathcal A^\ast
=
\arg\max_{\mathcal B}
\frac{
\operatorname{RiskCoverage}(\mathcal B)
\cdot
\operatorname{InformationGain}(\mathcal B)
}{
\operatorname{ComputeCost}(\mathcal B)+\epsilon
}.
$$

這就是 GAC 的第一個「全域攻擊壓縮」問題。

---

# 4. 為什麼局部攻擊可以組合？

## 4.1 組合需要結構條件

局部 attack 可以組合，不是因為 $a_i$ 和 $a_j$ 都叫 attack，而是因為它們在系統圖與因果結構上具有可描述關係。

第一版定義六類。

### 並行

$$
a_i
\parallel
a_j
$$

表示兩者可在同一 baseline 上獨立執行，不破壞彼此前提與觀測。

### 先後

$$
a_i
\prec
a_j
$$

表示 $a_j$ 的適用前提依賴 $a_i$ 造成的狀態。

### 衝突

$$
a_i
\mathrel{\#}
a_j
$$

表示兩者同時作用會使至少一個 attack 的語義失效。

### 遮蔽

$$
a_i
\triangleright
a_j
$$

表示 $a_i$ 產生的失敗訊號會遮住 $a_j$ 的可觀測效果。

### 協同

$$
a_i
\odot
a_j
$$

表示兩個局部 attack 單獨可能不造成缺陷，但組合後形成新的 failure mode。

### 依賴

$$
a_i
\rightarrow
a_j
$$

表示 attack graph 上存在明示依賴。

## 4.2 Attack Interaction Graph

定義：

$$
G_A
=
\left(
A,
E_A,
\lambda
\right),
$$

其中：

- $A$：attack operator；
- $E_A$：attack 關係；
- $\lambda$：關係型別。

則全域 campaign synthesis 變成：

$$
\boxed{
\text{Architecture Graph}
+
\text{Attack Interaction Graph}
+
\text{Budget}
\rightarrow
\text{Executable Campaign}.
}
$$

---

# 5. 一次型全域攻擊

## 5.1 Baseline Freeze

令候選 release baseline 為：

$$
S^\ast.
$$

第一輪全域 attack 開始後，除非遇到 sandbox 失效、attack harness 自身錯誤、無法恢復的測試污染或明示安全停止條件，否則不在 campaign 途中修改 product baseline。

因此所有主要 attack 作用於：

$$
S^\ast.
$$

## 5.2 One-Shot 不等於 One Process

「一次型」不是要求所有攻擊在一個 OS process 或同一毫秒執行。

它的定義是：

$$
\boxed{
\text{One Baseline}
+
\text{One Bounded Campaign Plan}
+
\text{One Global Observation Epoch}.
}
$$

campaign 可以包含 isolated parallel lanes、ordered phases、restart、snapshot restore、multiple sandboxes 與 branch-specific probes，只要它們仍然屬於同一 baseline 與同一 campaign contract。

## 5.3 第一輪之後才修

流程：

$$
S^\ast
\xrightarrow{\mathcal A_G}
\mathcal E_G
$$

其中：

$$
\mathcal E_G
=
\text{Global Evidence Set}.
$$

再：

$$
\mathcal E_G
\xrightarrow{\Pi_L}
\mathcal F_L
$$

其中：

$$
\Pi_L
=
\text{Local Failure Projection}.
$$

最後才進入 repair wave：

$$
S^\ast
\xrightarrow{\operatorname{Repair}(\mathcal F_L)}
S'.
$$

## 5.4 確認輪

修復後：

$$
S'
\xrightarrow{\mathcal A_G'}
\mathcal E_G'.
$$

其中 $\mathcal A_G'$ 至少包含所有曾命中缺陷的 attack、受修復影響的鄰近 attack 與必要 regression coverage。

第二輪之後若又產生有趣但非 blocker 的全新 attack：

$$
\rightarrow
\text{Attack Memory / Future Deep Profile}.
$$

而不是無限延長當前 release。

---

# 6. 全域缺陷表面

## 6.1 Baseline observation

令：

$$
O_0
=
\operatorname{Observe}(S^\ast).
$$

全域擾動後：

$$
O_1
=
\operatorname{Observe}
\left(
\mathcal A_G(S^\ast)
\right).
$$

若 observation space 可量化，可寫：

$$
\Delta_G
=
d(O_0,O_1).
$$

若不可量化，則：

$$
\Delta_G
=
\operatorname{Diff}(O_0,O_1).
$$

本文稱：

$$
\boxed{
\Delta_G
=
\text{Global Defect Surface}.
}
$$

## 6.2 缺陷表面不是單一 bug count

定義：

$$
\Delta_G
=
\left(
\Delta_{\mathrm{behavior}},
\Delta_{\mathrm{state}},
\Delta_{\mathrm{relation}},
\Delta_{\mathrm{semantic}},
\Delta_{\mathrm{temporal}},
\Delta_{\mathrm{authority}},
\Delta_{\mathrm{recovery}},
\Delta_{\mathrm{observability}}
\right).
$$

因此：

$$
\boxed{
\text{Bug Count}
\neq
\text{Defect Surface}.
}
$$

兩個系統即使同樣發現 10 個 bug，也可能具有完全不同的缺陷幾何。

---

# 7. A/B、驗證器與警報器

## 7.1 三個不同問題

對某 attack $a_i$，必須區分：

1. 系統真的出現缺陷嗎？
2. validator 能辨識嗎？
3. alarm 有發出正確訊號嗎？

因此：

$$
\boxed{
\text{Defect}
\neq
\text{Validator Failure}
\neq
\text{Alarm State}.
}
$$

## 7.2 四格矩陣

| 實際缺陷 | Alarm | 判定 |
|---|---|---|
| 有 | 有 | True Positive |
| 有 | 無 | Blind Spot |
| 無 | 有 | False Positive |
| 無 | 無 | True Negative |

其中最值得研究的是：

$$
\boxed{
\text{Blind Spot}.
}
$$

因為它表示：系統真的壞了，但現有驗證制度沒有看見。

## 7.3 Validator 本身也需要最小可證偽性

本文不主張對 validator 進行無限 meta-verification。

最低要求是：

$$
\exists w_{\mathrm{bad}}
\quad
V(w_{\mathrm{bad}})
=
\text{Reject},
$$

且：

$$
\exists w_{\mathrm{good}}
\quad
V(w_{\mathrm{good}})
=
\text{Accept}.
$$

這建立 discriminative evidence。

但只要 claim 已被充分支持，就不應自動開啟：

$$
V
\rightarrow
V(V)
\rightarrow
V(V(V))
\rightarrow
\cdots
$$

的無限鏈。

---

# 8. MSSP 的全域對抗對偶

## 8.1 MSSP 的原始優勢

MSSP 的主要工程優勢之一，是把系統責任與狀態邊界顯式化。

令 MSSP 系統圖為：

$$
G_M
=
(V_M,E_M,I_M).
$$

當：

$$
S_i
=
\text{FAIL},
$$

系統可以優先查找：

$$
S_i,
\operatorname{Dep}(S_i),
\operatorname{Boundary}(S_i).
$$

這降低 fault localization 成本。

## 8.2 對偶觀點

既然 failure localization 已經局部化，attack 本身不必也維持局部化。

因此：

$$
\boxed{
\text{MSSP Primal}
=
\text{Local Responsibility Structure}
}
$$

對應：

$$
\boxed{
\text{MSSP Adversarial Dual}
=
\text{Global Perturbation Structure}.
}
$$

兩者透過：

$$
\Pi_M
:
\mathcal E_G
\rightarrow
\mathcal F_L
$$

連接。

也就是：

$$
\boxed{
\text{Global Attack}
\xrightarrow{\Pi_M}
\text{Local Diagnosis}.
}
$$

## 8.3 清晰性悖論

MSSP 還有一個值得單獨研究的性質：

$$
\text{Architectural Legibility}
\uparrow
$$

會同時造成：

$$
\text{Debuggability}
\uparrow
$$

與：

$$
\text{Adversarial Salience}
\uparrow.
$$

因此「容易知道哪裡錯」與「容易知道怎麼故意弄錯」可能是同一種架構透明度的兩個面向。

GAC 的目的不是壓制這種可證偽性，而是把它從無限局部探索轉化成可壓縮、可學習、可重用的全域 campaign。

---

# 9. 攻擊記憶：用過就學會

## 9.1 一次性 attack 是浪費

如果某個局部 attack 已經真正造成 red、被確認不是 harness 假象、具有一般化結構並能被重新套用，則下一個專案不應重新花昂貴推理成本「想到一次」。

所以：

$$
\boxed{
\text{Novel Attack Cost}
\rightarrow
\text{Reusable Knowledge Capital}.
}
$$

## 9.2 三層記憶

本文建議 attack memory 至少保存三層。

### Concrete Witness

真實發生過的具體失敗案例。

### Attack Template

從 witness 抽象出的參數化 attack operator。

### Attack Family

更高階失敗機制，例如 boundary violation、stale state、authority drift、semantic collapse、partial-result collapse、TOCTOU、recovery inconsistency 與 false-green verification。

## 9.3 SEDB 特化版

可將 attack memory 表示為稀疏、多欄位、可版本化的工程知識記錄：

```yaml
attack_id:
family:
first_discovered_in:
applicability:
target_invariants:
affected_structures:
operator:
compatible_with:
conflicts_with:
requires_before:
expected_observation:
validator:
alarm:
coverage_signature:
compute_cost:
historical_hit_rate:
false_positive_history:
version_scope:
provenance:
last_revalidated:
```

這個資料層只保存：

$$
K_A.
$$

它不自行等於：

$$
\operatorname{Planner}.
$$

因此：

$$
\boxed{
\text{Attack Database}
\neq
\text{Attack Intelligence}.
}
$$

## 9.4 學習律

令 $K_t$ 為時刻 $t$ 的 attack knowledge。

若本輪得到 novel attacks：

$$
A_t^{\mathrm{novel}},
$$

則：

$$
\boxed{
K_{t+1}
=
K_t
\cup
\operatorname{Abstract}
\left(
A_t^{\mathrm{novel}}
\right).
}
$$

未來的昂貴 reasoning 應優先投入：

$$
\boxed{
\text{Residual Unknown Attack Space}
}
$$

而不是已知 attack replay。

---

# 10. AI 為什麼需要創造與生成能力？

## 10.1 Retrieval 不夠

若 AI 只能：

$$
(\mathcal S,K_t)
\rightarrow
\operatorname{Select}(a_i),
$$

它只是 attack retrieval system。

## 10.2 創造

真正的創造要求：

$$
(\mathcal S,K_t)
\rightarrow
a_{\mathrm{new}},
$$

且：

$$
a_{\mathrm{new}}
\notin
K_t.
$$

這表示 AI 從新架構、新關係、新狀態耦合或新 failure hypothesis 中生成以前沒有的 attack family。

## 10.3 生成

創造只得到概念：

$$
a_{\mathrm{concept}}.
$$

生成則要求：

$$
a_{\mathrm{concept}}
\rightarrow
a_{\mathrm{executable}}.
$$

可執行 attack 至少要包含 fixture、perturbation、schedule、oracle、expected signal、cleanup / restore 與 measurement plan。

因此：

$$
\boxed{
\text{Creativity}
\neq
\text{Executable Generation}.
}
$$

---

# 11. 全域注意力與一眼工程理解

## 11.1 「看一眼」的操作性定義

本文所說「AI 看一眼或幾眼理解整個專案」不是指 one literal token pass，而是指：

$$
B_{\mathrm{obs}}
\ll
|\mathcal S|,
$$

在有限 observation budget 下，快速取得足以支持全域攻擊規劃的結構模型：

$$
\widehat{\mathcal S}.
$$

## 11.2 需要觀察的不是所有細節

AI 應優先抽取：

$$
\widehat{\mathcal S}
=
\left(
\widehat V,
\widehat E,
\widehat X,
\widehat I,
\widehat O,
\widehat\Gamma
\right).
$$

也就是主要元件、關係與依賴、核心狀態、不變量、觀測表面、環境與權限邊界。

因此：

$$
\boxed{
\text{Global Understanding}
\neq
\text{Read Every Byte First}.
}
$$

---

# 12. 計算能力不是單純更多 FLOPS

## 12.1 候選組合爆炸

若有 $n$ 個 attack，單純 subset 已有：

$$
2^n
$$

種。

若再考慮 ordering，空間更大。

所以全域攻擊不能依賴 brute force。

## 12.2 架構理解等於 attack-space compression

如果 AI 知道 $a_i$ 只作用於 renderer，而 $a_j$ 只作用於完全隔離的 storage path，且不存在 interaction path，就可以剪掉：

$$
a_i
\odot
a_j
$$

的探索。

因此：

$$
\boxed{
\text{Architecture Understanding}
\rightarrow
\text{Adversarial Search-Space Compression}.
}
$$

## 12.3 計算資源配置

令總 AI 資源為：

$$
\mathbf B
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
$$

對 attack candidate $a_i$，可定義：

$$
\operatorname{MIV}_A(a_i)
=
\frac{
E[\Delta V_{\mathrm{risk}}(a_i)]
+
E[\Delta V_{\mathrm{knowledge}}(a_i)]
}{
E[\Delta C(a_i)]
+
\epsilon
}.
$$

若：

$$
\operatorname{MIV}_A(a_i)
<
\lambda_B,
$$

其中 $\lambda_B$ 為當期智能算力 shadow price，則：

$$
a_i
\rightarrow
\text{Defer / Deep Profile / Archive}.
$$

而不是無條件繼續。

---

# 13. GAC 的第一版能力向量

本文提出未來 AI 全域對抗工程能力向量：

$$
\boxed{
\mathcal C_{\mathrm{GAC}}
=
\left(
A,
U,
R,
C,
G,
K,
V,
L,
M
\right).
}
$$

其中：

$$
A
=
\text{Global Attention},
$$

$$
U
=
\text{Architectural Understanding},
$$

$$
R
=
\text{Resolution / Parsing},
$$

$$
C
=
\text{Adversarial Creativity},
$$

$$
G
=
\text{Executable Generation},
$$

$$
K
=
\text{Computation / Planning},
$$

$$
V
=
\text{Verification},
$$

$$
L
=
\text{Localization},
$$

$$
M
=
\text{Memory / Learning}.
$$

任何單一能力都不足以構成完整 GAC。

例如 $M+V$ 較接近 attack knowledge base； $G$ 較接近 test generator； $A+U$ 較接近 architecture reviewer；而：

$$
A+U+R+C+G+K+V+L+M
$$

才接近：

$$
\boxed{
\text{Autonomous Global Adversarial Synthesis}.
}
$$

---

# 14. 第一版演算法骨架

以下不是單一固定實作，而是 GAC runtime 的抽象控制流程。

```text
INPUT:
  project baseline S*
  attack memory K
  budget B
  authorization boundary Auth
  coverage target Tau

1. OBSERVE
   Build a bounded global project model S_hat.

2. MATCH
   Retrieve applicable known attack templates from K.

3. GAP
   Identify uncovered structures, relations, conditions, paths,
   validators, versions, and high-risk unknowns.

4. CREATE
   Generate novel local attack candidates for residual gaps.

5. TYPE / GUARD
   Reject attacks that violate authorization, sandbox, reversibility,
   scope, or execution constraints.

6. BUILD INTERACTION GRAPH
   Infer parallel, ordered, conflicting, masking, synergistic,
   and dependency relations.

7. COMPRESS
   Select a bounded campaign maximizing meaningful coverage and
   information gain under budget.

8. EXECUTE
   Run the campaign against the frozen baseline in isolated environments.

9. OBSERVE / VALIDATE / ALARM
   Collect behavioral, structural, semantic, temporal, authority,
   recovery, and observability evidence.

10. PROJECT
    Map global failures back to local responsibility regions.

11. REPAIR
    Execute one bounded repair wave.

12. CONFIRM
    Re-run affected and mandatory global coverage.

13. DISTILL
    Abstract novel successful attacks into reusable templates/families.

14. COMMIT MEMORY
    Update K -> K'.

15. STOP
    Archive non-blocking novel ideas instead of extending the release
    campaign indefinitely.
```

---

# 15. 研究假說

本文提出以下第一版可反駁假說。

## H1：全域先行可降低 baseline 漂移

在相同 attack 候選與修復能力下：

$$
\operatorname{BaselineDrift}_{\mathrm{GAC}}
<
\operatorname{BaselineDrift}_{\mathrm{SequentialLocal}}
$$

應可在多輪實驗中觀察。

## H2：攻擊記憶可降低重複 reasoning 成本

隨著 attack memory 增長：

$$
K_t
\subseteq
K_{t+1},
$$

對相似新專案的已知攻擊發現成本應滿足：

$$
C_{\mathrm{known}}(t+1)
<
C_{\mathrm{known}}(t)
$$

在某些範圍內成立。

## H3：架構清晰度可降低定位成本但提高反例顯著性

對顯式架構：

$$
L_{\mathrm{arch}}
\uparrow,
$$

可能同時觀察：

$$
C_{\mathrm{localize}}
\downarrow
$$

以及：

$$
C_{\mathrm{construct\_counterexample}}
\downarrow.
$$

這是 MSSP 可作第一實驗場的原因之一。

## H4：全域壓縮可以優於 attack 枚舉

存在專案族，使：

$$
|\mathcal A^\ast|
\ll
|\mathcal A|
$$

但：

$$
\operatorname{Coverage}(\mathcal A^\ast)
\approx
\operatorname{Coverage}(\mathcal A).
$$

若此假說不成立，GAC 的算力優勢會大幅下降。

## H5：生成能力可以提升未知失敗覆蓋

只 replay known attacks 的系統：

$$
M_{\mathrm{replay}},
$$

與具有新 attack synthesis 的系統：

$$
M_{\mathrm{creative}},
$$

在 unseen project 上比較 novel defect discovery：

$$
D_{\mathrm{novel}}(M_{\mathrm{creative}})
>
D_{\mathrm{novel}}(M_{\mathrm{replay}})
$$

應在部分 project distribution 中成立。

---

# 16. Benchmark 的第一版方向

未來 GACEI benchmark 可以給 AI 一個從未見過的授權測試專案：

$$
P_{\mathrm{unknown}},
$$

並限制：

$$
B_O
=
\text{Observation Budget},
$$

$$
B_C
=
\text{Compute Budget},
$$

$$
B_A
=
\text{Attack Execution Budget}.
$$

測量：

- project model reconstruction accuracy；
- invariant extraction；
- attack applicability precision；
- known attack reuse；
- novel attack generation；
- global coverage vector；
- true positive；
- blind spot discovery；
- false positive；
- localization accuracy；
- repair relevance；
- compute efficiency；
- reusable attack distillation。

最終問題不是：AI 找到幾個 bug？

而是：

$$
\boxed{
\text{AI 能否在有限資源下，先理解整個陌生系統，}
}
$$

再：

$$
\boxed{
\text{生成一個針對它的高資訊量全域對抗程序？}
}
$$

---

# 17. 與既有 EveMissLab 理論的關係

本文不是從零開始。

## 17.1 OAC：觀察與注意力

OAC 已區分 observation、attention、semantic understanding 與 computation，並允許 attention 作用於 topology、relation、temporal differential 與 global field。

GAC 承接：

$$
\text{Observation Budget}
+
\text{Goal-Directed Attention}.
$$

## 17.2 工程理解驗收

既有「如果真的懂，就重建給我看」建立：

$$
\text{Claimed Understanding}
\rightarrow
\text{Reconstruction Challenge}.
$$

GAC 再增加：

$$
\boxed{
\text{Can Reconstruct}
\neq
\text{Can Adversarially Model}.
}
$$

## 17.3 Research Cognitive Compilation

既有 U0-U6 與 L0-L7 區分研究庫理解成熟度與系統解構深度。

其中：

$$
U_6
=
\text{Falsify / Repair},
$$

以及：

$$
L_7
=
\text{Generative Synthesis}
$$

可直接成為 GAC 的理解與生成前置能力。

## 17.4 CPRR：局部解析與跳躍式路由

CPRR 已建立：

$$
\text{resolve locally}
\rightarrow
\text{handoff}
\rightarrow
\text{re-resolve}.
$$

GAC 可把 attack planning 視為一種 adversarial resolution process，而非一次窮舉所有 attack path。

## 17.5 DEST-08：候選生成與全域黏合

DEST-08 已區分：

$$
\text{Proposal}
\neq
\text{Typed}
\neq
\text{Verified}
\neq
\text{Globally Glued}.
$$

GAC 可建立：

$$
\text{Attack Proposal}
\neq
\text{Executable Attack}
\neq
\text{Verified Attack}
\neq
\text{Global Campaign Member}.
$$

## 17.6 UCS：計算基底

UCS 區分 realization capacity 與 cognitive intervention capacity。

因此：

$$
\boxed{
\text{More Compute}
\neq
\text{Better Attack Planning}.
}
$$

## 17.7 AICTE：智能資源配置

AICTE 已指出高額度不等於等比例成果，並建立邊際智能計算價值。

GAC 把同一思想用於 attack selection：

$$
\text{Do not spend frontier compute on already-known attack rediscovery}.
$$

## 17.8 DEST-01 / DEST-02：局部、全域與多維覆蓋

GAC 的 local/global distinction 與 multidimensional coverage 直接承接多域判定與多維覆蓋思想。

## 17.9 GQCM：全域不是很多

GQCM 的核心思想是：

$$
\boxed{
\text{Globality is structural, not merely large finite enumeration}.
}
$$

GAC 將此原則從全域證明轉化為：全域 attack campaign 應尋找可以結構性控制大攻擊域的有限組合，而不是把 attack count 最大化。

---

# 18. 本文非主張

本文不主張：

1. 所有軟體都應進行高強度對抗測試；
2. attack 越多，品質越高；
3. 任何局部 attack 集合都可無損組成全域 campaign；
4. MSSP 是唯一適合 GAC 的架構；
5. GAC 可以證明軟體沒有未知缺陷；
6. 高 attack coverage 等於高安全性；
7. 多 Agent 一定比單 Agent 更適合 GAC；
8. 全域 campaign 一定比所有 sequential local testing 便宜；
9. SEDB attack memory 可以取代 AI reasoning；
10. 已知 attack family 足以覆蓋未知系統；
11. 所有新反例都應立即加入 release blocker；
12. validator 必須被無限遞歸驗證；
13. whole-system adversarial simulation 等於現實世界 penetration；
14. 一個 AI 能生成 attack 就表示它理解整個架構；
15. 一個 AI 能找到大量缺陷就表示它具有高全域注意力；
16. 任何「100% global coverage」在未固定 reference frame 前具有普遍意義。

本文主張的是：

$$
\boxed{
\text{局部 attack 應被抽象、組合、壓縮、記憶與全域化，}
}
$$

以及：

$$
\boxed{
\text{AI 的高階對抗能力應被評估為理解、生成、計算與驗證的聯合能力，}
}
$$

而不是只計算：

$$
\boxed{
\text{找到多少 bug}.
}
$$

---

# 19. 系列後續

GACEI 系列後續預定依序處理：

1. GACEI-02：MSSP 的對偶；
2. GACEI-03：局部攻擊抽象論；
3. GACEI-04：SEDB 對抗記憶基底；
4. GACEI-05：全域攻擊組合代數；
5. GACEI-06：全域攻擊壓縮；
6. GACEI-07：一眼理解專案與全域注意力；
7. GACEI-08：工程理解與對抗能力；
8. GACEI-09：對抗性創造與生成；
9. GACEI-10：全域攻擊計算理論與資源配置；
10. GACEI-11：缺陷表面、多維覆蓋與警報盲區；
11. GACEI-12：全域工程智能 Benchmark。

---

# 20. 結論

軟體工程長期習慣把 attack、test、fault injection 與 counterexample 視為局部事件。

這在很多場景中仍然合理。

但當 AI 開始具有跨 repository 閱讀、架構抽取、全域狀態建模、自動測試生成、sandbox 執行、trace 比較、validator 生成、多 Agent 協作與長期 attack memory，局部 attack 永遠局部執行就不再是唯一合理形式。

本文因此提出：

$$
\boxed{
\text{Global Adversarial Computation}
}
$$

並把其最小精神壓縮為：

$$
\boxed{
\text{Understand Globally}
\rightarrow
\text{Attack Globally}
\rightarrow
\text{Diagnose Locally}
\rightarrow
\text{Learn Permanently}.
}
$$

中文可表述為：

> **全域理解，全域擾動，局部診斷，永久學習。**

其目標不是讓 AI 成為永動攻擊機。

恰恰相反。

GAC 希望把：

$$
\text{Endless Local Adversarial Reasoning}
$$

壓縮成：

$$
\text{Bounded Global Adversarial Computation}.
$$

如果某一局部反例已經被人類或 AI 發現、驗證、抽象與保存，那麼下一個系統不應再次用昂貴的智能推理從零發明它。

真正值得投入未來前沿 AI 算力的，不是：

> 我們是否還能再想到一個以前已知的局部反例？

而是：

$$
\boxed{
\text{目前的全域 attack closure 之外，還剩下什麼真正未知的結構？}
}
$$

這才是從局部測試走向全域工程智能的起點。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將渲染畫面視為 canonical source。
