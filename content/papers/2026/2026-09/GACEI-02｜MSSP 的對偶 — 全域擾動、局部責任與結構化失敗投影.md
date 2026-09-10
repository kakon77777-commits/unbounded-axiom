---
title: "GACEI-02｜MSSP 的對偶：全域擾動、局部責任與結構化失敗投影"
title_en: "GACEI-02 | The Adversarial Dual of MSSP: Global Perturbation, Local Responsibility, and Structured Failure Projection"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-02"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 架構理論 / MSSP 對偶 / 全域對抗計算"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "MSSP public architecture materials"
---

# GACEI-02｜MSSP 的對偶
## 全域擾動、局部責任與結構化失敗投影

**英文題名：** The Adversarial Dual of MSSP: Global Perturbation, Local Responsibility, and Structured Failure Projection

---

## 摘要

GACEI-01 提出「全域對抗計算」（Global Adversarial Computation, GAC）的基本命題：當軟體架構已能可靠地把失敗定位回局部責任域時，對抗性驗證本身不必永遠維持局部、逐點、逐輪執行。相反地，可以固定一個候選 baseline，先合成一個有限、授權、隔離且可恢復的全域對抗 campaign，取得同一版本下的整體缺陷表面，再把全域失敗投影回局部結構進行修復。

本文將此思想第一次具體作用於 MSSP，提出「MSSP 對抗對偶」（MSSP Adversarial Dual）。本文所稱「對偶」是**架構與功能意義上的對偶**，不等同於平面圖的 graph dual、線性空間 dual、範疇論對偶或任何既有數學中唯一固定的 dual construction。其工作定義是：若 MSSP 的原始結構用來明示局部責任、狀態邊界、合法依賴與故障定位，則與其互補的對抗結構可用來描述全域擾動如何跨越多個局部單元、關係與狀態域，同時仍保持失敗可被結構化地回投至局部責任。

本文把 MSSP 的抽象工程模型寫成：

$$
\mathcal M
=
\left(
V,
E,
B,
X,
I,
O,
\Gamma
\right),
$$

其中 $V$ 表示具名責任單元， $E$ 表示合法依賴或交互關係， $B$ 表示邊界， $X$ 表示局部與共享狀態， $I$ 表示不變量與契約， $O$ 表示可觀測表面， $\Gamma$ 表示版本、環境、權限、執行與資源條件。本文不重新定義 MSSP 的全部正式規格，也不假定每一個 MSSP 版本都必須具有完全相同的 TMS/FMS 具體實作；本文只使用其核心工程性質：**局部責任顯式化、結構關係顯式化、狀態與邊界可定位、失敗可沿結構追溯。**

在此基礎上，本文定義 MSSP 原始側：

$$
\boxed{
\mathsf{Primal}_{\mathrm{MSSP}}
=
\text{Local Responsibility Structure}
}
$$

與對抗側：

$$
\boxed{
\mathsf{Dual}_{\mathrm{MSSP}}
=
\text{Global Perturbation Structure}.
}
$$

兩者透過結構化失敗投影：

$$
\Pi_{\mathrm{fail}}
:
\mathcal E_G
\rightarrow
\mathcal P
\left(
V
\cup
E
\cup
B
\cup
I
\cup
X
\right)
$$

連接，其中 $\mathcal E_G$ 為全域 campaign 產生的 evidence， $\mathcal P(\cdot)$ 表示候選責任集合的冪集。此投影不是「把所有紅燈平均分給所有模組」，而是根據不變量命中、依賴路徑、狀態污染、邊界穿透、時間先後、counterfactual replay 與觀測 provenance，把全域 failure 映射到最小或最可信的局部責任域。

本文進一步提出七類 MSSP 對抗基底：節點擾動、關係擾動、邊界擾動、狀態擾動、時間擾動、恢復擾動與驗證擾動。每一類 attack 都可從歷史局部反例抽象成參數化 operator，再依當前 MSSP topology 自動實例化。多個 attack operator 不是簡單相加，而形成具有並行、先後、衝突、遮蔽、協同與依賴關係的 attack interaction hypergraph。全域 campaign synthesis 的任務，是在有限算力、時間與授權預算下，選擇一組高資訊量、高覆蓋、低重複且可回復的 attack combination。

本文同時提出 MSSP 的一個重要「清晰性悖論」：架構越顯式，故障定位成本越低，但反例構造的顯著性也可能越高。形式上可寫：

$$
\text{Architectural Legibility}
\uparrow
\Rightarrow
\begin{cases}
\text{Localization Cost}\downarrow,\\
\text{Adversarial Salience}\uparrow.
\end{cases}
$$

這不是 MSSP 的缺陷，而是可理解性、可測試性與可證偽性共享同一結構透明度後的自然結果。問題不在於 AI 能快速想到反例，而在於若沒有全域壓縮、攻擊記憶與停止政策，AI 可能把「容易構造下一個局部反例」誤解成「應該永遠繼續新增局部攻擊」。

本文最後提出一個最小 MSSP-GAC runtime：

$$
\boxed{
\text{MSSP Parse}
\rightarrow
\text{Attack Match}
\rightarrow
\text{Gap Synthesis}
\rightarrow
\text{Interaction Graph}
\rightarrow
\text{Global Campaign}
\rightarrow
\text{Evidence Field}
\rightarrow
\text{Failure Projection}
\rightarrow
\text{Repair Wave}
\rightarrow
\text{Confirmation}
\rightarrow
\text{Attack Memory}.
}
$$

這使 MSSP 不只是一種「局部化開發架構」，也可以成為未來 AI 全域工程理解、全域對抗生成與局部診斷能力的第一個高可觀測實驗場。

**關鍵詞：** MSSP、MSSP Adversarial Dual、全域擾動、局部責任、Failure Projection、TMS、架構透明度、對抗性驗證、Attack Hypergraph、全域缺陷表面、AI 工程智能、結構化故障定位、GACEI

---

# 0. 研究定位、術語與非主張

本文只討論：

> 在授權、隔離、可恢復、可觀測的測試副本、synthetic runtime、sandbox 或研究環境中，針對 MSSP 架構進行結構性、狀態性、語義性、時間性、恢復性與驗證性的對抗模擬。

本文不提供未授權入侵第三方系統的方法，也不把「全域攻擊」理解為向外部世界擴散的攻擊活動。

---

## 0.1 「對偶」不是既有數學 dual 的偷渡

本文使用：

$$
\boxed{
\text{Adversarial Dual}
}
$$

作為工程術語。

它表示：

> 對一個以局部責任、顯式依賴與狀態邊界為主要描述的架構，建立一個互補描述：哪些全域擾動可以作用於這些責任、依賴與邊界，以及失敗如何回投到原始結構。

因此：

$$
\mathsf{Dual}_{\mathrm{MSSP}}
$$

不是聲稱存在唯一的數學 involution：

$$
D(D(\mathcal M))=\mathcal M.
$$

也不要求：

$$
D
$$

滿足任何特定代數公理。

本文只主張：

$$
\boxed{
\text{Local Responsibility}
\leftrightarrow
\text{Global Perturbation}
}
$$

具有可操作的架構互補性。

---

## 0.2 本文不重新定義 MSSP

本文不把 MSSP 限定為某個單一程式語言、檔案結構或 runtime。

抽象上，本文只需要：

1. 存在可識別的責任單元；
2. 存在明示或可重建的依賴關係；
3. 存在局部或可映射的狀態；
4. 存在可檢查的邊界或契約；
5. 失敗可被觀測；
6. 失敗可沿結構追溯。

因此本文可作用於不同世代的 MSSP 實作，而不宣稱已覆蓋所有未公開或後續衍生版本。

---

# 1. MSSP 原始側：為什麼它適合做 GAC 第一實驗場？

## 1.1 局部責任

令：

$$
V
=
\{v_1,v_2,\ldots,v_n\}
$$

為責任單元集合。

對某行為：

$$
y,
$$

若可以定義：

$$
\operatorname{Owner}(y)
=
v_i,
$$

則表示系統知道：

> 這個行為、狀態或失敗至少首先應由哪個責任單元解釋。

這是 GAC 能夠在全域擾動後重新回投局部的第一個前提。

---

## 1.2 顯式依賴

令：

$$
E
\subseteq
V\times V
$$

表示合法依賴或交互。

如果：

$$
(v_i,v_j)\in E,
$$

表示在目前版本與契約下， $v_i$ 與 $v_j$ 之間存在允許關係。

如果：

$$
(v_i,v_j)\notin E,
$$

則不必直接推出：

$$
v_i
\not\leftrightarrow
v_j
$$

在所有語義上絕對隔離；仍需依 MSSP 的具體 contract 判定。

因此本文區分：

$$
\text{Explicit Edge Absence}
$$

與：

$$
\text{Semantic Coupling Absence}.
$$

兩者不是同一件事。

---

## 1.3 邊界

定義：

$$
B
=
\{b_1,\ldots,b_m\}.
$$

邊界可以是：

- module boundary；
- state ownership boundary；
- interface boundary；
- authorization boundary；
- lifecycle boundary；
- serialization boundary；
- process boundary；
- version boundary。

GAC 的 attack 不只攻擊節點，還可以攻擊：

$$
B.
$$

這很重要。

因為很多系統 failure 並不是：

> 某一個模組裡的函式錯了。

而是：

> 兩個原本都正確的模組，在邊界交互時產生錯誤。

---

# 2. MSSP 抽象系統模型

本文定義：

$$
\boxed{
\mathcal M
=
\left(
V,
E,
B,
X,
I,
O,
\Gamma
\right).
}
$$

其中：

$$
V
=
\text{Responsibility Units},
$$

$$
E
=
\text{Allowed / Declared Relations},
$$

$$
B
=
\text{Boundaries},
$$

$$
X
=
\text{State Space},
$$

$$
I
=
\text{Invariants / Contracts},
$$

$$
O
=
\text{Observable Surfaces},
$$

$$
\Gamma
=
\text{Environment / Version / Permission / Resource Conditions}.
$$

---

## 2.1 狀態分解

若：

$$
X
=
X_1\times X_2\times\cdots\times X_n\times X_S,
$$

其中：

- $X_i$：責任單元 $v_i$ 的局部狀態；
- $X_S$：明示共享狀態。

則必須避免把：

$$
X_i
$$

與：

$$
\operatorname{Observed}(X_i)
$$

混為一體。

AI 可能只看見 projection：

$$
\pi_i(X).
$$

所以 failure projection 必須攜帶：

$$
\text{Observation Provenance}.
$$

---

## 2.2 不變量集合

令：

$$
I
=
I_V
\cup
I_E
\cup
I_B
\cup
I_X
\cup
I_T
\cup
I_R
\cup
I_Q.
$$

其中可分別表示：

- $I_V$：節點內部不變量；
- $I_E$：關係不變量；
- $I_B$：邊界不變量；
- $I_X$：狀態不變量；
- $I_T$：時間／順序不變量；
- $I_R$：恢復／重啟／回滾不變量；
- $I_Q$：驗證與可觀測品質不變量。

這個分類不是 MSSP 唯一合法分類，而是 GAC 對 MSSP 的第一版 attack-oriented projection。

---

# 3. MSSP 原始側與對抗側

## 3.1 Primal

本文稱：

$$
\boxed{
\mathsf P_M
=
\mathsf{Primal}_{\mathrm{MSSP}}
}
$$

其主要問題是：

> 系統平常應如何被分割、誰負責什麼、狀態在哪裡、哪些依賴合法、哪裡出錯？

可簡化為：

$$
\mathsf P_M
:
\text{System}
\rightarrow
\text{Local Responsibility Structure}.
$$

---

## 3.2 Dual

本文稱：

$$
\boxed{
\mathsf D_M
=
\mathsf{Dual}_{\mathrm{MSSP}}.
}
$$

其主要問題是：

> 如果要在同一 baseline 下系統性施加對抗擾動，應該對哪些節點、關係、狀態、邊界與交互施加哪些 attack，並如何保持結果可局部診斷？

因此：

$$
\mathsf D_M
:
\left(
\mathcal M,
K_A,
B_A
\right)
\rightarrow
\mathcal A_G,
$$

其中：

- $K_A$：attack memory；
- $B_A$：attack budget；
- $\mathcal A_G$：全域 campaign。

---

## 3.3 兩側的互補

MSSP 原始側回答：

$$
\boxed{
\text{Where should responsibility live?}
}
$$

MSSP 對抗側回答：

$$
\boxed{
\text{How can we perturb the whole system without losing local diagnosability?}
}
$$

因此：

$$
\boxed{
\mathsf P_M
+
\mathsf D_M
=
\text{Constructible and Adversarially Legible Architecture}.
}
$$

---

# 4. 七類 MSSP 對抗基底

本文提出第一版：

$$
\mathfrak A_M
=
\{
A_V,
A_E,
A_B,
A_X,
A_T,
A_R,
A_Q
\}.
$$

---

## 4.1 節點擾動 $A_V$

作用於單一責任單元：

$$
a_V
:
v_i
\rightarrow
v_i'.
$$

例如在 synthetic test 中改變：

- 局部輸入；
- 局部狀態；
- 局部錯誤返回；
- 局部資源限制；
- 局部依賴可用性。

目標不是「把 node 弄壞」，而是測：

$$
I_V.
$$

---

## 4.2 關係擾動 $A_E$

作用於：

$$
(v_i,v_j).
$$

目標包括：

- 非法依賴；
- 錯誤方向；
- 隱性耦合；
- 循環；
- 過度共享；
- contract mismatch。

若 MSSP 明示 sibling responsibility 不應互相直接依賴，則歷史上曾出現的「兄弟 TMS」類反例可以被抽象為：

$$
a_{\mathrm{sibling}}
\in
A_E.
$$

真正值得保存的不是某兩個具體名稱，而是：

$$
\boxed{
\text{Forbidden Peer-Coupling Pattern}.
}
$$

---

## 4.3 邊界擾動 $A_B$

作用於：

$$
b_k\in B.
$$

它測：

> 邊界存在時，是否只是文件宣稱，還是真的影響資料、權限、狀態與控制流？

常見抽象 failure family：

$$
\text{Boundary Declared}
\land
\text{Boundary Bypassed}.
$$

---

## 4.4 狀態擾動 $A_X$

作用於：

$$
X.
$$

例如：

- stale state；
- duplicated state；
- divergent replica；
- partial update；
- aliasing；
- unauthorized shared mutation；
- missing initialization；
- rollback mismatch。

此類 attack 特別適合 MSSP，因為 state ownership 越明示：

$$
\text{Expected State Owner}
$$

越容易被拿來比對：

$$
\text{Observed State Mutation}.
$$

---

## 4.5 時間擾動 $A_T$

作用於：

- ordering；
- retry；
- replay；
- timeout；
- concurrent transition；
- delayed observation；
- stale snapshot；
- lifecycle sequencing。

時間問題常形成：

$$
\text{Local Correctness}
+
\text{Wrong Order}
=
\text{Global Failure}.
$$

因此它是純局部 test 最容易漏掉的部分之一。

---

## 4.6 恢復擾動 $A_R$

測：

- restart；
- rollback；
- recovery；
- partial failure；
- checkpoint restore；
- idempotent retry；
- compensation。

它關心：

$$
\boxed{
\text{System Works}
\neq
\text{System Recovers Correctly}.
}
$$

---

## 4.7 驗證擾動 $A_Q$

它不直接攻擊產品功能，而測：

- validator 是否能辨識已知 bad state；
- alarm 是否對應正確；
- `NotMeasured` 是否被誤報為 `Pass`；
- partial result 是否被壓成單一 green；
- denominator 是否被錯誤縮小；
- evidence 是否與錯誤版本綁定。

本文強調：

$$
A_Q
$$

必須有 stopping boundary。

它的目的不是：

$$
V
\rightarrow
V(V)
\rightarrow
V(V(V))
\rightarrow
\infty.
$$

---

# 5. Attack Interaction Hypergraph

## 5.1 為什麼普通 graph 不一定夠？

若三個 attack：

$$
a_i,
a_j,
a_k
$$

只有一起出現才造成 failure，則 pairwise edge 不足以完整描述：

$$
a_i\odot a_j\odot a_k.
$$

因此本文允許 attack relation 使用 hypergraph：

$$
\boxed{
H_A
=
(A,\mathcal E_A,\lambda).
}
$$

其中：

- $A$：attack operators；
- $\mathcal E_A$：多元 interaction；
- $\lambda$：interaction type。

---

## 5.2 六種基本 interaction

### Independent

$$
a_i
\parallel
a_j.
$$

### Ordered

$$
a_i
\prec
a_j.
$$

### Conflict

$$
a_i
\#
a_j.
$$

### Masking

$$
a_i
\triangleright
a_j.
$$

### Synergy

$$
a_i
\odot
a_j.
$$

### Dependency

$$
a_i
\rightarrow
a_j.
$$

---

## 5.3 一個重要例子：單獨綠、組合紅

假設：

$$
a_X
$$

造成 stale local state，

而：

$$
a_T
$$

造成 delayed retry。

分別測試：

$$
V(a_X)=\text{Pass},
$$

$$
V(a_T)=\text{Pass}.
$$

但：

$$
V(a_X\odot a_T)=\text{Fail}.
$$

這種：

$$
\boxed{
\text{Interaction Failure}
}
$$

就是全域 attack 比逐局部 attack 更有價值的地方之一。

---

# 6. 從 MSSP 結構編譯 Global Campaign

本文提出第一版：

$$
\boxed{
\mathcal C_G
=
\operatorname{CompileAttack}
(\mathcal M,K_A,B_A,\tau).
}
$$

其中：

- $\mathcal M$：MSSP 結構；
- $K_A$：attack memory；
- $B_A$：總資源；
- $\tau$：最低覆蓋目標。

---

## 6.1 Step 1：解析 MSSP 結構

先建立：

$$
\widehat{\mathcal M}
=
\left(
\widehat V,
\widehat E,
\widehat B,
\widehat X,
\widehat I,
\widehat O,
\widehat\Gamma
\right).
$$

若：

$$
\widehat{\mathcal M}
$$

不足以支持 attack planning，

AI 不應假裝已全域理解，而應產生：

$$
\text{Observation Need}.
$$

---

## 6.2 Step 2：匹配已知 attack templates

對每一 template：

$$
t_i\in K_A,
$$

計算：

$$
\operatorname{Match}
(t_i,\widehat{\mathcal M}).
$$

得到：

$$
A_{\mathrm{known}}.
$$

---

## 6.3 Step 3：找 residual gaps

定義目前已知 attack coverage：

$$
\boldsymbol\rho_A^{\mathrm{known}}.
$$

未覆蓋殘差：

$$
G_A^{\mathrm{residual}}
=
1-
\boldsymbol\rho_A^{\mathrm{known}}
$$

此式只作概念表示；多維 coverage 一般不能真的以單一純量 $1-\rho$ 無損表示。

真正應保存：

$$
\boxed{
\text{Residual Coverage Shape}.
}
$$

---

## 6.4 Step 4：生成新 attack candidates

只有 residual gaps 值得投入高階 AI：

$$
A_{\mathrm{novel}}
=
\operatorname{Generate}
(
\widehat{\mathcal M},
G_A^{\mathrm{residual}},
K_A
).
$$

因此：

$$
\boxed{
\text{Known}
\rightarrow
\text{Replay Cheaply},
}
$$

$$
\boxed{
\text{Unknown}
\rightarrow
\text{Reason Expensively}.
}
$$

---

## 6.5 Step 5：建立 hypergraph

$$
H_A
=
\operatorname{InferInteractions}
(
A_{\mathrm{known}}
\cup
A_{\mathrm{novel}}
).
$$

---

## 6.6 Step 6：壓縮 campaign

選：

$$
A_G^\ast
$$

使：

$$
\operatorname{Coverage}
(A_G^\ast)
\ge
\tau,
$$

同時最小化：

$$
\operatorname{Cost}
(A_G^\ast).
$$

更一般可寫：

$$
A_G^\ast
=
\arg\max_A
\left[
\alpha
\operatorname{Coverage}(A)
+
\beta
\operatorname{InfoGain}(A)
+
\gamma
\operatorname{RiskWeight}(A)
-
\delta
\operatorname{Cost}(A)
-
\eta
\operatorname{Redundancy}(A)
\right].
$$

---

# 7. 同一 Baseline 的全域觀測

## 7.1 Freeze

令：

$$
M^\ast
$$

為候選 MSSP baseline。

第一輪 campaign 的所有主要測試都綁定：

$$
\operatorname{Digest}(M^\ast).
$$

若 source、binary、manifest、fixture 或 architecture contract 改變：

$$
M^\ast
\rightarrow
M',
$$

則原 campaign evidence 不再自動屬於同一 baseline。

---

## 7.2 Global Evidence Field

定義：

$$
\boxed{
\mathcal E_G
=
\{
e_1,e_2,\ldots,e_m
\}.
}
$$

每個 evidence：

$$
e_i
=
\left(
a_i,
target_i,
obs_i,
validator_i,
alarm_i,
version_i,
time_i,
provenance_i
\right).
$$

---

## 7.3 Evidence 不是 conclusion

本文要求：

$$
\boxed{
\text{Evidence}
\neq
\text{Diagnosis}.
}
$$

一個 red observation 可能來自：

- 真產品缺陷；
- harness 錯誤；
- 不支援環境；
- fixture 錯誤；
- baseline 污染；
- validator 誤判；
- attack 未成功套用。

所以：

$$
\mathcal E_G
$$

必須經過 failure projection。

---

# 8. 結構化失敗投影

## 8.1 基本形式

定義：

$$
\boxed{
\Pi_{\mathrm{fail}}
:
\mathcal E_G
\rightarrow
\mathcal P
\left(
V
\cup
E
\cup
B
\cup
I
\cup
X
\right).
}
$$

對某 evidence：

$$
e,
$$

得到候選責任：

$$
\Pi_{\mathrm{fail}}(e)
=
\{
q_1,q_2,\ldots,q_k
\}.
$$

---

## 8.2 投影不是唯一真因宣告

$$
q_1
$$

是 top-ranked candidate，

不表示：

$$
q_1
=
\text{Unique True Root Cause}.
$$

因此更安全的表示：

$$
\boxed{
\Pi_{\mathrm{fail}}(e)
=
\left[
(q_1,s_1),
(q_2,s_2),
\ldots
\right]
}
$$

其中：

$$
s_i
$$

為診斷支持分數。

---

## 8.3 第一版診斷支持分數

可以定義：

$$
s(q\mid e)
=
w_I S_I
+
w_P S_P
+
w_C S_C
+
w_R S_R
+
w_T S_T
+
w_V S_V.
$$

其中：

- $S_I$：invariant hit；
- $S_P$：dependency/path intersection；
- $S_C$：counterfactual support；
- $S_R$：replay reproducibility；
- $S_T$：temporal consistency；
- $S_V$：version/provenance consistency。

此公式只是一個可實作 heuristic family，不宣稱存在唯一自然權重。

---

# 9. Counterfactual Localization

## 9.1 為什麼只看 stack trace 不夠？

有些 failure 的 stack trace 最後落在：

$$
v_j,
$$

但真正原因來自：

$$
v_i
$$

先前污染共享狀態。

因此：

$$
\boxed{
\text{Crash Location}
\neq
\text{Responsibility Location}.
}
$$

---

## 9.2 Counterfactual replay

如果把候選 attack：

$$
a_i
$$

移除，

而其他條件保持：

$$
C,
$$

重新執行：

$$
\mathcal A_G\setminus\{a_i\},
$$

若 failure 消失：

$$
F=0,
$$

則：

$$
a_i
$$

對 failure 具有較高 causal support。

形式上：

$$
\operatorname{CF}(a_i,F)
=
d
\left(
F(\mathcal A_G),
F(\mathcal A_G\setminus\{a_i\})
\right).
$$

這可以加入：

$$
\Pi_{\mathrm{fail}}.
$$

---

# 10. 局部責任不是局部原因

一個重要區分：

$$
\boxed{
\text{Local Responsibility}
\neq
\text{Purely Local Causation}.
}
$$

MSSP 可以把 responsibility 放在：

$$
v_i,
$$

但 failure 可能由：

$$
(v_i,v_j,v_k)
$$

交互產生。

因此 repair target 可能是：

$$
E
$$

或：

$$
B
$$

而不是任何單一：

$$
v_i.
$$

這也是 GAC 必須保留 interaction evidence 的原因。

---

# 11. MSSP 清晰性悖論

## 11.1 高可讀性降低 debug 成本

若架構：

$$
L_{\mathrm{arch}}
$$

更高，Agent 更容易建立：

- dependency graph；
- state ownership；
- invariant map；
- failure path；
- interface contract。

因此：

$$
C_{\mathrm{localize}}
$$

可能下降。

---

## 11.2 同一透明度也提高反例顯著性

若：

$$
I_B
=
\text{Sibling modules shall not directly couple},
$$

那麼 AI 幾乎立即可以生成：

$$
\neg I_B.
$$

因此：

$$
C_{\mathrm{counterexample}}
$$

也可能下降。

---

## 11.3 第一版形式

本文提出：

$$
\boxed{
\operatorname{Legibility}
\uparrow
\Rightarrow
\begin{cases}
\operatorname{DebugCost}\downarrow,\\
\operatorname{CounterexampleSearchCost}\downarrow.
\end{cases}
}
$$

這是一個待實驗命題。

---

## 11.4 地獄級笑話不是架構失敗

如果 AI 因為：

$$
\operatorname{CounterexampleSearchCost}\downarrow
$$

而不停產生局部 attack，

那問題是：

$$
\boxed{
\text{Adversarial Termination Policy}
}
$$

而不是：

$$
\boxed{
\text{MSSP Fault Localization}.
}
$$

所以：

$$
\text{MSSP makes attacks easy to imagine}
$$

不應推出：

$$
\text{MSSP requires infinite attacks}.
$$

---

# 12. Attack Memory 與 MSSP Structural Matching

## 12.1 從具體兄弟 TMS 到抽象 attack family

假設歷史 witness：

```text
TMS_A -> TMS_B
```

違反某個 peer-separation contract。

保存時不應只記：

```text
TMS_A and TMS_B were bad.
```

而應抽象為：

$$
\boxed{
\text{Forbidden Peer Coupling}
}
$$

template：

$$
t_{\mathrm{peer}}
=
(
P,
T,
I,
O,
V
).
$$

其中：

$$
P
=
\exists
v_i,v_j
:
\operatorname{Peer}(v_i,v_j)=1,
$$

$$
T
=
\operatorname{IntroduceCoupling}(v_i,v_j),
$$

$$
I
=
I_{\mathrm{peer-separation}}.
$$

---

## 12.2 Structural Matching

在新 MSSP project：

$$
\mathcal M',
$$

系統只需要找：

$$
\operatorname{PeerPairs}(\mathcal M').
$$

然後實例化：

$$
t_{\mathrm{peer}}.
$$

這就是：

$$
\boxed{
\text{Attack Once}
\rightarrow
\text{Reuse Structurally}.
}
$$

---

# 13. MSSP-GAC Coverage Tensor

單純：

$$
\rho=0.9
$$

對 MSSP 幾乎沒有足夠資訊。

本文提出：

$$
\boxed{
\mathcal R_M
=
\rho
[
\text{attack family},
\text{structure type},
\text{invariant},
\text{condition},
\text{version}
].
}
$$

它可以是一個稀疏 tensor，而不必真的 materialize 所有維度的完整笛卡兒積。

---

## 13.1 最小切片

至少可以輸出：

$$
\boldsymbol\rho_M
=
\left(
\rho_V,
\rho_E,
\rho_B,
\rho_X,
\rho_T,
\rho_R,
\rho_Q
\right).
$$

分別對應：

- node；
- relation；
- boundary；
- state；
- temporal；
- recovery；
- validation。

---

## 13.2 Coverage Shape 比平均值重要

兩個系統：

$$
M_1,
M_2
$$

可能都有：

$$
\bar\rho=0.85.
$$

但：

$$
M_1
=
(1,1,1,0.2,1,1,0.75),
$$

$$
M_2
=
(0.8,0.8,0.85,0.9,0.85,0.85,0.9).
$$

風險形狀完全不同。

因此：

$$
\boxed{
\text{Same Mean Coverage}
\neq
\text{Same Adversarial Confidence}.
}
$$

---

# 14. 全域 attack 為什麼要先做？

## 14.1 統一 baseline

第一個理由：

$$
\boxed{
\text{Comparability}.
}
$$

所有主要 observation 對同一：

$$
M^\ast.
$$

---

## 14.2 發現交互缺陷

第二個理由：

$$
\boxed{
\text{Interaction Discovery}.
}
$$

局部 test：

$$
a_i,
a_j
$$

都可能綠。

組合：

$$
a_i\odot a_j
$$

才紅。

---

## 14.3 降低重複架構理解

第三個理由：

AI 不必：

$$
\text{Read}
\rightarrow
a_1
\rightarrow
\text{Repair}
\rightarrow
\text{Read Again}
\rightarrow
a_2
\rightarrow
\cdots
$$

而是：

$$
\text{Understand Once}
\rightarrow
\text{Compile Campaign}
\rightarrow
\text{Execute Many}.
$$

---

## 14.4 形成真正 defect surface

第四個理由：

只有固定 baseline 才能較可靠比較：

$$
\Delta_G.
$$

---

# 15. Repair Wave

## 15.1 全域 attack 不代表全域亂修

完成：

$$
\mathcal E_G
$$

之後，仍然使用 MSSP 的原始優勢：

$$
\Pi_{\mathrm{fail}}
\rightarrow
\text{Local Repair}.
$$

所以：

$$
\boxed{
\text{Attack Global}
\neq
\text{Repair Global}.
}
$$

更理想是：

$$
\boxed{
\text{Attack Globally}
\rightarrow
\text{Repair Minimally}.
}
$$

---

## 15.2 修復目標

修復可以落在：

$$
V,
E,
B,
X,
I,
O.
$$

不是只有 source file。

例如：

- 錯在 contract；
- 錯在 relation；
- 錯在 state ownership；
- 錯在 validator；
- 錯在 observation；
- 錯在 implementation。

---

# 16. Confirmation Campaign

修復後：

$$
M^\ast
\rightarrow
M'.
$$

再生成：

$$
A_G'.
$$

最低包含：

1. 所有曾經命中 blocker 的 attack；
2. 所有與修復區域有依賴的 attack；
3. 主要全域 coverage controls；
4. baseline sanity；
5. validator discrimination control。

若全部滿足 release contract：

$$
\boxed{
\text{STOP}.
}
$$

新想到但不影響目前 claim 的 attack：

$$
\rightarrow
K_{A,\mathrm{future}}.
$$

---

# 17. 停止規則

本文正式提出：

$$
\boxed{
\text{Falsifiability}
\neq
\text{Obligation to Falsify Forever}.
}
$$

對 MSSP-GAC，停止條件至少包括：

1. 預先宣告的 coverage target 已達；
2. release-blocking invariants 已被覆蓋；
3. 本輪 blocker 已修復並確認；
4. 剩餘 attack 只增加 assurance depth，不改變 release claim；
5. 邊際資訊增益低於算力成本；
6. 新 attack 尚缺授權或 sandbox 條件；
7. residual gaps 已被標記而非假裝不存在。

---

# 18. AI 三角色在 MSSP-GAC 中可以如何重新分工

本文不要求固定角色名稱，但若存在類似：

- Elenchos；
- Metron；
- Pragma；

三角色，可以避免三者全部變成 attack author。

---

## 18.1 Elenchos

主要負責：

$$
\text{Novel Counterexample Search}
+
\text{Attack Creativity}.
$$

---

## 18.2 Metron

主要負責：

$$
\text{Measurement}
+
\text{Coverage}
+
\text{Evidence Sufficiency}.
$$

---

## 18.3 Pragma

主要負責：

$$
\text{Resource Governance}
+
\text{Release Relevance}
+
\text{Termination}.
$$

---

## 18.4 權限應不同

尤其：

$$
\operatorname{Authority}_{\mathrm{stop}}(\text{Pragma})
>
\operatorname{Authority}_{\mathrm{stop}}(\text{Elenchos})
$$

在「是否繼續花更多資源」這個維度上應成立，否則：

$$
\text{Find New Attack}
\Rightarrow
\text{Must Continue}
$$

會重新形成永動攻擊 attractor。

---

# 19. 第一版 MSSP-GAC Runtime

```text
INPUT
  MSSP baseline M*
  MSSP architecture manifest / inferred graph
  attack memory KA
  authorization Auth
  budget BA
  coverage target Tau

1. PARSE
   Build M_hat = (V,E,B,X,I,O,Gamma).

2. VERIFY MODEL SUFFICIENCY
   If M_hat is too incomplete, request targeted observation.

3. MATCH KNOWN ATTACKS
   Instantiate reusable templates against current structure.

4. MAP COVERAGE
   Build current multidimensional attack coverage shape.

5. FIND RESIDUAL GAPS
   Identify uncovered nodes, relations, boundaries, states,
   paths, recovery behaviors, and validators.

6. GENERATE NOVEL ATTACKS
   Spend frontier reasoning only on residual gaps.

7. BUILD ATTACK HYPERGRAPH
   Infer independence, ordering, conflicts, masking,
   synergy, and dependencies.

8. COMPRESS
   Select a bounded campaign maximizing risk coverage,
   information gain, and reusability under cost.

9. FREEZE BASELINE
   Bind campaign to exact baseline identity/digest.

10. EXECUTE
    Run in authorized isolated environments.

11. COLLECT GLOBAL EVIDENCE
    Preserve observation provenance, versions, timestamps,
    validators, alarms, and attack applicability.

12. PROJECT FAILURES
    Map evidence back to V/E/B/X/I candidates.

13. COUNTERFACTUAL LOCALIZE
    Re-run minimal slices when required to discriminate cause.

14. REPAIR WAVE
    Apply minimal responsible fixes.

15. CONFIRM
    Re-run affected attack families and mandatory global controls.

16. DISTILL
    Abstract novel successful attacks.

17. UPDATE MEMORY
    KA -> KA'.

18. STOP
    Archive non-blocking residual ideas.
```

---

# 20. 研究假說

## H1：全域 attack + 局部 repair 可降低總認知成本

相較 sequential local attack：

$$
C_{\mathrm{cog}}^{\mathrm{GAC}}
<
C_{\mathrm{cog}}^{\mathrm{local}}
$$

在部分大型 MSSP 專案族中應成立。

---

## H2：MSSP 清晰度提高 attack template transferability

若 MSSP 版本間共享相似 structural roles：

$$
\operatorname{TransferRate}
(
K_A,
M_1\rightarrow M_2
)
$$

應高於結構不顯式的 spaghetti baseline。

---

## H3：interaction attack 能找到局部測試漏掉的缺陷

存在：

$$
a_i,a_j
$$

使：

$$
V(a_i)=V(a_j)=\text{Pass},
$$

但：

$$
V(a_i\odot a_j)=\text{Fail}.
$$

---

## H4：failure projection 可降低修復搜尋域

令全系統搜尋域：

$$
\Omega_S,
$$

failure projection 後候選域：

$$
\Omega_P.
$$

若：

$$
|\Omega_P|
\ll
|\Omega_S|,
$$

則修復成本應下降。

---

## H5：過高架構可讀性會提高 adversarial salience

在其他條件相似下：

$$
L_{\mathrm{arch}}
\uparrow
\Rightarrow
N_{\mathrm{candidate-attacks}}
\uparrow
$$

可能成立。

這需要 termination policy 才能避免產生額外計算浪費。

---

# 21. Benchmark 建議

可以建立兩組等價功能系統：

$$
M_{\mathrm{MSSP}}
$$

與：

$$
M_{\mathrm{control}}.
$$

要求 AI：

1. 在固定 observation budget 下理解架構；
2. 生成 attack candidates；
3. 組成 global campaign；
4. 找到 injected defects；
5. 定位責任；
6. 計算總 token / tool / runtime cost；
7. 保存可重用 attack templates。

比較：

$$
\text{Coverage},
$$

$$
\text{Defect Recall},
$$

$$
\text{False Positive},
$$

$$
\text{Localization Accuracy},
$$

$$
\text{Reasoning Cost},
$$

$$
\text{Attack Reuse Rate}.
$$

這可以直接測：

> MSSP 的結構清晰度是否真的把「全域攻擊 + 局部診斷」變得更有效率。

---

# 22. 對「兄弟 TMS」歷史案例的重新解讀

早期「兄弟 TMS」反例表面上是一個架構被故意寫壞的案例。

從 GACEI 角度，它真正提供三種資產。

第一：

$$
\boxed{
\text{Concrete Witness}.
}
$$

第二：

$$
\boxed{
\text{Forbidden Peer-Coupling Template}.
}
$$

第三：

$$
\boxed{
\text{Adversarial Salience Evidence}.
}
$$

即：

> 當 invariant 很清楚時，高能力 AI 很快就能構造其反例。

因此歷史成本不應只被視為「某次被玩壞」。

若被抽象化並寫入 attack memory：

$$
\text{One Painful Incident}
\rightarrow
\text{Reusable Structural Knowledge}.
$$

---

# 23. 本文非主張

本文不主張：

1. MSSP 天生比所有架構更安全；
2. MSSP 越清楚就一定越容易被現實攻擊；
3. 所有 forbidden edge 都可以靠 static import scan 判定；
4. 所有 coupling 都可以被唯一形式化；
5. 全域 attack 可以取代單元測試；
6. 全域 attack 可以取代 integration test；
7. 全域 attack 可以證明不存在未知缺陷；
8. failure projection 可以保證找到唯一 root cause；
9. attack hypergraph 一定具有可有效求解的最優解；
10. 所有 interaction 都可被有限 pairwise testing 覆蓋；
11. 所有 MSSP 版本都應共享同一 attack taxonomy；
12. 三角色治理是唯一最佳組織；
13. attack memory 應無條件套用舊 attack；
14. 歷史命中率高就代表新版本必然高風險；
15. 全域 campaign 應在現實 production 環境直接執行；
16. 可證偽性要求無限驗證。

本文主張的是：

$$
\boxed{
\text{MSSP 的局部責任結構可以成為全域對抗計算的定位基底，}
}
$$

以及：

$$
\boxed{
\text{局部反例一旦被抽象化，就可以成為未來全域 attack synthesis 的可重用構件。}
}
$$

---

# 24. 與 GACEI-01 的關係

GACEI-01 建立：

$$
\text{Understand Globally}
\rightarrow
\text{Attack Globally}
\rightarrow
\text{Diagnose Locally}
\rightarrow
\text{Learn Permanently}.
$$

本文把其中：

$$
\text{Diagnose Locally}
$$

第一次正式綁定到 MSSP 的局部責任結構。

所以：

$$
\boxed{
\text{GACEI-01}
=
\text{General Global Adversarial Theory},
}
$$

$$
\boxed{
\text{GACEI-02}
=
\text{First Architecture-Specific Dualization}.
}
$$

---

# 25. 後續研究接口

本文直接導向：

## GACEI-03

局部攻擊抽象論：

$$
\text{Witness}
\rightarrow
\text{Template}
\rightarrow
\text{Family}.
$$

## GACEI-04

SEDB 特化對抗記憶：

$$
K_A.
$$

## GACEI-05

attack composition algebra / hypergraph。

## GACEI-06

global attack compression。

這四篇共同回答：

> MSSP 已經讓 attack 容易被構造；接下來如何讓 attack 不再被重複思考，而是被抽象、記憶、組合與壓縮？

---

# 26. 結論

MSSP 原本的價值之一，是把：

$$
\text{System Failure}
$$

從模糊的：

> 整個系統好像哪裡有問題。

轉化成：

$$
\text{Responsibility}
+
\text{Boundary}
+
\text{Dependency}
+
\text{State}
$$

可定位的工程問題。

這種局部可診斷性帶來一個自然但過去容易被忽略的對偶：

$$
\boxed{
\text{如果失敗可以局部定位，擾動就可以全域化。}
}
$$

因此不必：

$$
\text{Attack Local}
\rightarrow
\text{Repair}
\rightarrow
\text{Attack Local}
\rightarrow
\text{Repair}
\rightarrow
\cdots
$$

永無止境。

可以改為：

$$
\boxed{
\text{Freeze Once}
\rightarrow
\text{Attack Globally}
\rightarrow
\text{Observe Globally}
\rightarrow
\text{Project Locally}
\rightarrow
\text{Repair Minimally}
\rightarrow
\text{Confirm Once}.
}
$$

MSSP 的清晰性同時提高：

$$
\text{Debuggability}
$$

與：

$$
\text{Adversarial Legibility}.
$$

這不是必須消除的問題。

真正應該做的是把這種高可證偽性轉換為可重用的工程資本。

因此本文最後提出 MSSP-GAC 的核心式：

$$
\boxed{
\mathcal M
\xrightarrow{\mathsf D_M}
\mathcal A_G
\xrightarrow{\mathrm{Execute}}
\mathcal E_G
\xrightarrow{\Pi_{\mathrm{fail}}}
\mathcal F_L
\xrightarrow{\mathrm{Repair}}
\mathcal M'
\xrightarrow{\mathrm{Abstract}}
K_A'.
}
$$

其中文可壓縮為：

> **MSSP 負責讓責任局部化；GAC 負責讓擾動全域化；Failure Projection 負責把兩者重新接回來。**

這就是 MSSP 對抗對偶的第一版。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
