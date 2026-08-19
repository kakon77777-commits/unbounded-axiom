# GPC 中的載體同一性：跨載體交流、Receiver Update 與 Identity Safety
## Carrier Identity in Generalized Phase Communication: Cross-Carrier Interaction, Receiver Update, and Identity Safety

**系列**：Identity–Phase Fiber Calculus（IPFC）  
**論文**：Paper 04  
**版本**：v1.0  
**日期**：2026-08-15  
**作者**：Neo.K（許筌崴）with Aletheia  
**機構**：EveMissLab（一言諾科技有限公司），台灣  
**文件性質**：形式安全理論／GPC-CS identity extension／非操作性橋接論文  
**上游**：
- IPFC Paper 01《同一性–相位纖維微積分》
- IPFC Paper 02《相位語義》
- IPFC Paper 03《相變與同一性分岔》
- GPC-CS Papers 00–10
- PCPRT Papers 01–08
- EveMissLab Phase Canon v1.1

**形式化狀態**：本文新 IPFC–GPC 定理目前為手工形式證明，尚未完成 Lean 4 / Coq 機器驗證。  
**安全邊界**：本文不提供人格改寫、主體複製、身份遷移、神經刺激、模型覆寫或任何高風險 carrier manipulation 的操作程序。所有「identity」均需明示 criterion；本文不宣稱 first-person continuity 已可由外部觀測判定。

---

# 摘要

GPC-CS 將交流從「訊息是否被正確解碼」擴張為「交流是否改變 receiver carrier state」，其基本 receiver update 可寫為：

$$
x_B'
=
F_B
\left(
x_B,
D_B
\left(
T_{AB}
\left(
E_A(x_A)
\right),
x_B
\right)
\right).
$$

GPC-CS Paper 07 進一步區分 observable-state、informational、functional、causal-lineage 與 substrate continuity，並明確拒絕把 identity-related observable profile：

$$
\Psi(x)
$$

直接等同 personal identity 或 first-person continuity。然而，Paper 07 刻意沒有建立一個 operational identity projection，因此仍缺少下列形式問題的統一答案：**交流之後 receiver state 改變多少仍屬同一 identity fiber？跨載體 transduction 在何種條件下可下推為 identity lineage？語義保持與 carrier identity 保持之間是否存在邏輯蘊含？恢復到「同一身份」與恢復到「同一完整狀態」是否等價？有限 telemetry 何時足以判定 identity-related safety？**

本文將 IPFC 引入 GPC-CS。對 receiver state space：

$$
\mathcal X_B
$$

與明示 identity criterion：

$$
\kappa_B,
$$

定義：

$$
q_B:
\mathcal X_B
\twoheadrightarrow
\mathcal O_B.
$$

receiver identity fiber：

$$
F_{O_B}
=
q_B^{-1}(O_B).
$$

本文首先定義 **Carrier-Identity-Preserving Interaction**：對 admissible sender states 與 receiver states，GPC update 必須保持：

$$
q_B(x_B')=q_B(x_B).
$$

並證明 **Message-Family Fiber Invariance Theorem**：一個 GPC interaction family 對 receiver identity 全域保持，當且僅當每一個 sender-conditioned receiver update 都把每個 receiver identity fiber 映回自身。

第二，本文把跨載體 transfer：

$$
T_{AB}:
\mathcal X_A
\rightarrow
\mathcal X_B
$$

接到 IPFC Lineage Factorization。存在唯一 deterministic carrier-lineage map：

$$
L_{AB}:
\mathcal O_A
\rightarrow
\mathcal O_B
$$

使：

$$
q_BT_{AB}
=
L_{AB}q_A
$$

當且僅當 $q_BT_{AB}$ 在每個 source identity fiber 上為常數。若同一 source identity fiber 的不同 representatives 被 transfer 到不同 target identities，deterministic identity migration 不可由 source identity alone 定義，必須提升為 branching relation 或 stochastic lineage kernel。

第三，本文建立兩個 no-go 結果。**Semantic–Carrier Independence Proposition** 表明 semantic identity preservation 與 carrier identity preservation 一般互不蘊含：同一 semantic proposition 可以被一個 carrier 接收而不改變其身份，也可以伴隨 carrier identity transition；反之 carrier identity 可保持但 semantic reconstruction 失敗。**Identity Recovery Weakness Theorem** 表明 exact state recovery 必推出 identity recovery，但只恢復到同一 identity fiber 不推出 exact state recovery；若 fiber 含多個 states，identity recovery 嚴格弱於 state recovery。

第四，本文把 GPC-CS Paper 10 的 observation-fiber 原理專門化為 **Carrier Identity Observability Theorem**：存在只依 telemetry：

$$
H_B(x)
$$

精確判定 operational identity：

$$
q_B(x)
$$

的 classifier，當且僅當 $q_B$ 在 $H_B$ 的每個 observation fiber 上為常數。若 observation fiber 跨越不同 identity classes，則任何只依該 telemetry 的 exact identity classifier 都不可能存在。此結果不把 personal identity 物理化；它只作用於研究者事先明示的 operational criterion。

最後，本文把 state safety、identity safety、semantic success 與 lineage safety 分成不同規格，定義 Identity-Safe GPC Corridor、Safe Identity Recovery、Network Identity Invariance 與 Communication Identity Safety Matrix。由此，GPC 中的「安全交流」不再只有訊息 fidelity，而可精確區分：

$$
\boxed{
\text{semantic success},
\quad
\text{carrier-state safety},
\quad
\text{carrier-identity preservation},
\quad
\text{lineage correctness}.
}
$$

本文的最高結論是：

> **Communication may transmit meaning, modify state, preserve identity, cross identity boundaries, or create lineage; these are separate claims and must be verified separately.**

**關鍵詞**：GPC、Carrier Identity、Identity Safety、Receiver Update、Lineage、Cross-Carrier Transduction、Semantic Communication、Observability、Recovery、IPFC

---

# 1. GPC 的真正研究對象是 Receiver State Update

傳統通信首先關心：

$$
m_A
\rightarrow
\hat m_B.
$$

GPC 則增加：

$$
\boxed{
x_B
\rightarrow
x_B'.
}
$$

receiver 不是只產生 output 的無狀態 terminal。

它可能具有：

- persistent memory；
- policy；
- learned parameters；
- self-model；
- preference state；
- physical state；
- relational state；
- safety margins。

所以：

$$
\boxed{
\text{message fidelity}
\neq
\text{carrier-state safety}.
}
$$

---

# 2. GPC Receiver Update 的標準分解

sender state：

$$
x_A\in\mathcal X_A.
$$

receiver state：

$$
x_B\in\mathcal X_B.
$$

encoding：

$$
E_A:
\mathcal X_A
\rightarrow
\mathcal M_A.
$$

transduction：

$$
T_{AB}:
\mathcal M_A
\rightarrow
\mathcal U_B.
$$

decoding：

$$
D_B:
\mathcal U_B
\times
\mathcal X_B
\rightarrow
\mathcal R_B.
$$

receiver update：

$$
F_B:
\mathcal X_B
\times
\mathcal R_B
\rightarrow
\mathcal X_B.
$$

因此：

$$
\boxed{
U_{AB}(x_A,x_B)
=
F_B
\left(
x_B,
D_B
\left(
T_{AB}(E_A(x_A)),
x_B
\right)
\right).
}
$$

記：

$$
x_B'
=
U_{AB}(x_A,x_B).
$$

---

# 3. Sender-Conditioned Receiver Update

固定 sender state：

$$
a\in\mathcal X_A.
$$

定義：

$$
\boxed{
U_a:
\mathcal X_B
\rightarrow
\mathcal X_B,
}
$$

$$
U_a(x_B)
=
U_{AB}(a,x_B).
$$

這把 GPC interaction family 寫成：

$$
\boxed{
\mathcal U_A
=
\{
U_a
:
a\in\mathcal X_A
\}.
}
$$

---

# 4. Operational Carrier Identity

GPC-CS Paper 07 已經建立：

$$
\Psi:
\mathcal X_B
\rightarrow
\mathcal Y_I
$$

作為 identity-related observable profile。

本文再增加：

$$
\boxed{
q_B
=
q_{\kappa_B}
:
\mathcal X_B
\twoheadrightarrow
\mathcal O_B,
}
$$

其中：

$$
\kappa_B
$$

是研究者明示的 operational carrier identity criterion。

---

# 5. $\Psi$ 與 $q_B$ 不能混為一談

$$
\Psi
$$

回答：

> 我們量到哪些 identity-related observables？

$$
q_B
$$

回答：

> 在指定 criterion 下，這個 state 被分類成哪個 operational identity？

所以：

$$
\boxed{
\Psi
\neq
q_B.
}
$$

可能：

$$
\Psi(x_1)=\Psi(x_2)
$$

但：

$$
q_B(x_1)\neq q_B(x_2),
$$

若 $\Psi$ 對該 criterion 不充分。

也可能不同：

$$
\Psi
$$

profiles 仍被：

$$
q_B
$$

歸為同一 identity。

---

# 6. First-Person Boundary

本文不定義：

$$
q_B
$$

為「主觀體驗的同一個我」。

除非未來另有可辯護的 theory / operationalization。

所以：

$$
\boxed{
q_B(x_1)=q_B(x_2)
}
$$

只表示：

> 依 $\kappa_B$，兩 states 屬同一 operational carrier identity class。

不推出：

$$
\boxed{
\text{first-person continuity}.
}
$$

---

# 7. Carrier Identity Fiber

對：

$$
O_B\in\mathcal O_B,
$$

定義：

$$
\boxed{
F_{O_B}^B
=
q_B^{-1}(O_B).
}
$$

它包含所有在：

$$
\kappa_B
$$

下仍被視為同一 receiver carrier identity 的 states。

---

# 8. Carrier-Identity-Preserving Interaction

## 定義 8.1

一個 sender-conditioned update：

$$
U_a
$$

對 receiver identity-preserving，若：

$$
\boxed{
q_BU_a
=
q_B.
}
$$

等價：

$$
\boxed{
q_B(U_{AB}(a,x_B))
=
q_B(x_B)
}
$$

對所有 admissible：

$$
x_B.
$$

---

# 9. Message-Family Identity Preservation

## 定義 9.1

對 admissible sender set：

$$
K_A
\subseteq
\mathcal X_A,
$$

若：

$$
\boxed{
q_BU_a
=
q_B
\qquad
\forall a\in K_A,
}
$$

則 GPC interaction family 在 $K_A$ 上 carrier-identity-preserving。

---

# 10. Message-Family Fiber Invariance Theorem

## 定理 10.1

下列兩條等價：

### A

$$
q_BU_a
=
q_B
$$

對所有：

$$
a\in K_A.
$$

### B

對所有：

$$
a\in K_A,
$$

$$
O_B\in\mathcal O_B,
$$

有：

$$
\boxed{
U_a
\left(
F_{O_B}^B
\right)
\subseteq
F_{O_B}^B.
}
$$

### 證明

對每一固定 $a$，直接套用 IPFC Paper 01 的 Fiber Invariance Theorem。

A 對所有 $a$ 成立，當且僅當每個 $U_a$ 保持所有 receiver identity fibers。 $\square$

---

# 11. 身份安全不是「完全不變」

identity-preserving 不要求：

$$
x_B'=x_B.
$$

允許：

$$
\boxed{
x_B'
\neq
x_B,
\qquad
q_B(x_B')
=
q_B(x_B).
}
$$

因此：

- learning；
- memory update；
- adaptation；
- semantic uptake；
- policy refinement；

都可以發生而不自動構成 identity transition。

---

# 12. GPC Phase Role

sender–receiver semantic / relational phase：

$$
PH\text{-}5
\times
IF\text{-}3.
$$

receiver 自身 state phase/update 若仍在同 identity fiber：

$$
IF\text{-}1.
$$

若 path-dependent loop residual：

$$
IF\text{-}2.
$$

若 receiver identity 改變：

$$
IF\text{-}4.
$$

所以單一 GPC event 可同時具有多個 IF roles。

---

# 13. Identity-Safe Carrier Set

令一般 carrier safe set：

$$
\mathcal S_B
\subseteq
\mathcal X_B.
$$

令 admissible identity classes：

$$
\mathcal A_B^{\mathrm{id}}
\subseteq
\mathcal O_B.
$$

定義：

$$
\boxed{
\mathcal S_B^{\mathrm{id}}
=
\mathcal S_B
\cap
q_B^{-1}
\left(
\mathcal A_B^{\mathrm{id}}
\right).
}
$$

這是 **Identity-Safe Carrier Corridor**。

---

# 14. Identity-Safe Update

若：

$$
x_B
\in
\mathcal S_B^{\mathrm{id}}
$$

推出：

$$
U_a(x_B)
\in
\mathcal S_B^{\mathrm{id}}
$$

對所有 admissible $a$，則 interaction family 保持 identity-safe corridor。

注意：

這比：

$$
q_BU_a=q_B
$$

弱或強取決於：

$$
\mathcal A_B^{\mathrm{id}}.
$$

如果 admissible set 允許多個 identities，更新可以換 identity 但仍留在 corridor。

---

# 15. Strict Identity Preservation 與 Identity-Admissible Safety

必須區分：

## Strict Identity Preservation

$$
\boxed{
q_B(x_B')=q_B(x_B).
}
$$

## Identity-Admissible Safety

$$
\boxed{
q_B(x_B')
\in
\mathcal A_B^{\mathrm{id}}.
}
$$

後者允許某些設計上合法的 identity transitions。

---

# 16. Finite Composition Identity Theorem

## 定理 16.1

若有限 update sequence：

$$
U_{a_1},
\ldots,
U_{a_n}
$$

各自滿足：

$$
q_BU_{a_k}
=
q_B,
$$

則：

$$
\boxed{
q_B
U_{a_n}
\cdots
U_{a_1}
=
q_B.
}
$$

### 證明

由反覆合成：

$$
q_BU_{a_n}\cdots U_{a_1}
=
q_BU_{a_{n-1}}\cdots U_{a_1}
=
\cdots
=
q_B.
\qquad\square
$$

所以 finite GPC conversation 可在逐步 identity-preserving 條件下保持同 identity fiber。

---

# 17. Composition Safety 仍不等於 Full-State Recovery

即使每一步 identity-preserving：

$$
q_B(x_t)=O_B
$$

對所有 $t$，

仍可能：

$$
x_T
$$

與：

$$
x_0
$$

差很大。

因此：

$$
\boxed{
\text{identity preservation}
\neq
\text{state invariance}.
}
$$

---

# 18. GPC Path Dependence

對 message/history word：

$$
w
=
(a_1,\ldots,a_n),
$$

定義：

$$
\boxed{
U_w
=
U_{a_n}
\circ
\cdots
\circ
U_{a_1}.
}
$$

兩條 histories：

$$
w,v
$$

可以有：

$$
U_w(x_B)
\neq
U_v(x_B)
$$

即使：

- 最終 external message summary 類似；
- identity 保持；
- functional output 相近。

這就是 Paper 06 的 path dependence 與 IPFC IF-2 接口。

---

# 19. Identity-Preserving Interaction Holonomy

若 message/context loop：

$$
\gamma
$$

回到相同外部 control condition，

但：

$$
U_\gamma(x_B)\neq x_B,
$$

同時：

$$
q_BU_\gamma(x_B)=q_B(x_B),
$$

則稱：

$$
\boxed{
\text{identity-preserving GPC holonomy}.
}
$$

這是 generalized state/path holonomy，不自動是 physical geometric phase。

---

# 20. Cross-Carrier Transfer 與 Communication 不同

GPC communication：

$$
x_B
\rightarrow
x_B'
$$

通常是既有 receiver 被更新。

Cross-carrier transfer：

$$
\boxed{
T_{AB}^{X}:
\mathcal X_A
\rightarrow
\mathcal X_B
}
$$

則問：

> source carrier state 如何在 target carrier 上形成對應 state？

兩者不應共用一個「傳輸」詞而不分型。

---

# 21. Cross-Carrier Identity Projections

source：

$$
q_A:
\mathcal X_A
\twoheadrightarrow
\mathcal O_A.
$$

target：

$$
q_B:
\mathcal X_B
\twoheadrightarrow
\mathcal O_B.
$$

我們問：

> transfer 是否能下推成 identity-level lineage？

---

# 22. Carrier-Lineage Factorization Theorem

## 定理 22.1

假設：

$$
q_A
$$

滿射。

存在唯一 deterministic carrier-lineage map：

$$
\boxed{
L_{AB}:
\mathcal O_A
\rightarrow
\mathcal O_B
}
$$

使：

$$
\boxed{
q_B
T_{AB}^{X}
=
L_{AB}
q_A
}
$$

當且僅當：

$$
\boxed{
q_A(x_1)=q_A(x_2)
\Rightarrow
q_B(T_{AB}^{X}(x_1))
=
q_B(T_{AB}^{X}(x_2)).
}
$$

### 證明

直接套用 IPFC Paper 01 的 Lineage Factorization Theorem。 $\square$

---

# 23. Carrier Identity 不充分時 Transfer 無法下推

若存在：

$$
x_1,x_2
\in
F_O^A
$$

但：

$$
q_B(T_{AB}^{X}(x_1))
\neq
q_B(T_{AB}^{X}(x_2)),
$$

則 deterministic：

$$
L_{AB}(O)
$$

不存在。

所以：

$$
\boxed{
\text{source identity alone is insufficient to determine target identity}.
}
$$

需補：

- source state；
- history；
- side information；
- branch variable；
- stochastic kernel。

---

# 24. Copy、Migration、Fork 的 Lineage Topology

本文不把三者當 personal identity verdict。

只定義工程 lineage topology。

## Copy

source 保留，target 新增：

$$
A
\rightarrow
B,
$$

且 $A$ 仍存在。

## Migration

design specification 宣稱 source role 轉移至 target，source 停止或退出 active lineage。

## Fork

一個 source 產生：

$$
B_1,
B_2,\ldots
$$

多個後繼。

這些是 provenance / causal topology labels。

---

# 25. Branching No-Single-Lineage Proposition

若同一 source identity：

$$
O_A
$$

合法產生兩個 distinct target identities：

$$
O_{B_1}\neq O_{B_2},
$$

則不存在單值 deterministic：

$$
L_{AB}(O_A)
$$

可同時表示兩個 branch outcomes。

因此需 relation：

$$
\boxed{
\mathcal L_{AB}
\subseteq
\mathcal O_A
\times
\mathcal O_B
}
$$

或：

$$
\boxed{
K_B(O_B\mid O_A).
}
$$

---

# 26. Provenance 不等於 Identity

provenance 回答：

> 這個 state / datum 從哪裡來、經什麼 derivation 形成？

identity 回答：

> 在 criterion $\kappa$ 下，它屬於哪個 identity class？

所以：

$$
\boxed{
\text{provenance}
\neq
\text{identity}.
}
$$

但 provenance 是 lineage 的重要證據層。

---

# 27. Functional Equivalence 不等於 Carrier Identity

兩個 states / systems 可以 behaviorally equivalent：

$$
x\sim_{\mathrm{beh}}y
$$

但：

$$
q(x)\neq q(y).
$$

bisimulation 類結構可作 functional equivalence 的成熟數學鄰居。

IPFC 不把 bisimulation relation 當 identity relation。

---

# 28. Semantic Identity 與 Carrier Identity 是兩個投影

對 message meaning state：

$$
x_{\mathrm{sem}},
$$

有：

$$
q_{\mathrm{sem}}.
$$

對 receiver carrier state：

$$
x_B,
$$

有：

$$
q_B.
$$

所以一次 communication 同時可以問：

$$
\boxed{
q_{\mathrm{sem}}(\hat x_B^{\mathrm{sem}})
\stackrel{?}{=}
F_Oq_{\mathrm{sem}}(x_A^{\mathrm{sem}})
}
$$

與：

$$
\boxed{
q_B(x_B')
\stackrel{?}{=}
q_B(x_B).
}
$$

---

# 29. Semantic–Carrier Independence Proposition

## 命題 29.1

在一般 GPC model 中：

$$
\boxed{
\text{semantic identity preservation}
}
$$

與：

$$
\boxed{
\text{carrier identity preservation}
}
$$

互不蘊含。

### 反例 A：Semantic Success, Carrier Identity Change

令 receiver 完整取得 proposition：

$$
O_{\mathrm{sem}}
$$

但 update 被 criterion $\kappa_B$ 分類為新 carrier identity：

$$
q_B(x_B')\neq q_B(x_B).
$$

則 semantic identity preserved，但 carrier identity 不 preserved。

### 反例 B：Carrier Identity Preserved, Semantic Failure

令：

$$
q_B(x_B')=q_B(x_B)
$$

但 receiver reconstructs wrong proposition：

$$
q_{\mathrm{sem}}(\hat x_B^{\mathrm{sem}})
\neq
F_Oq_{\mathrm{sem}}(x_A^{\mathrm{sem}}).
$$

則 carrier identity preserved，但 semantic identity 不 preserved。 $\square$

---

# 30. 重要結論：Meaning Preservation 不能當 Identity Safety Certificate

因此：

$$
\boxed{
\text{message understood correctly}
\not\Rightarrow
\text{receiver identity preserved}.
}
$$

反向也不成立。

這是 IPFC Paper 02 與 Paper 04 的核心分工。

---

# 31. Functional Success 也獨立

GPC 可有：

1. semantic identity success；
2. semantic phase alignment；
3. receiver functional success；
4. carrier identity preservation。

四者應分列。

建議：

$$
\boxed{
\mathbf S_{\mathrm{GPC}}
=
(
S_{\mathrm{sem-id}},
S_{\mathrm{phase}},
S_{\mathrm{func}},
S_{\mathrm{car-id}}
).
}
$$

---

# 32. Identity Recovery

令 update：

$$
U:
\mathcal X_B
\rightarrow
\mathcal X_B.
$$

recovery：

$$
R:
\mathcal X_B
\rightarrow
\mathcal X_B.
$$

---

## 定義 32.1 — Exact State Recovery

$$
\boxed{
R(U(x))
=
x.
}
$$

---

## 定義 32.2 — Identity Recovery

$$
\boxed{
q_B(R(U(x)))
=
q_B(x).
}
$$

identity recovery 只要求回到原 identity fiber。

---

# 33. Identity Recovery Weakness Theorem

## 定理 33.1

Exact state recovery 必推出 identity recovery。

### 證明

若：

$$
R(U(x))
=
x,
$$

兩邊施：

$$
q_B
$$

得：

$$
q_B(R(U(x)))
=
q_B(x).
\qquad\square
$$

---

## 定理 33.2 — Converse Failure

若存在某 identity fiber：

$$
F_O^B
$$

含至少兩個不同 states：

$$
x\neq y,
$$

則存在 identity recovery 而不是 exact state recovery。

### 證明

取 update/recovery composition 使：

$$
R(U(x))
=
y.
$$

因：

$$
x,y\in F_O^B,
$$

有：

$$
q_B(R(U(x)))
=
q_B(y)
=
O
=
q_B(x),
$$

所以 identity recovered。

但：

$$
R(U(x))
=
y
\neq
x.
$$

故 exact state recovery 失敗。 $\square$

---

# 34. Recovery Hierarchy

因此：

$$
\boxed{
\text{exact state recovery}
\Rightarrow
\text{identity recovery}
}
$$

但：

$$
\boxed{
\text{identity recovery}
\not\Rightarrow
\text{exact state recovery}.
}
$$

再加 Paper 06：

$$
\boxed{
\text{endpoint identity recovery}
\neq
\text{safe identity recovery}.
}
$$

---

# 35. Safe Identity Recovery

recovery path：

$$
x_0^{(r)},
x_1^{(r)},
\ldots,
x_m^{(r)}.
$$

要求：

$$
x_k^{(r)}
\in
\mathcal S_B
$$

並且：

$$
q_B(x_k^{(r)})
\in
\mathcal A_B^{\mathrm{id}}
$$

對所有 $k$。

最後：

$$
q_B(x_m^{(r)})
=
q_B(x_{\mathrm{target}}).
$$

這才是 **safe identity recovery**。

---

# 36. 回到 Identity Fiber 不代表恢復歷史

即使：

$$
q_B(x_m^{(r)})
=
q_B(x_0),
$$

也可能：

$$
V_I(0,m)
$$

很大，

或 history state：

$$
h_m
\neq
h_0.
$$

所以 endpoint identity equality 不會消掉 path dependence。

---

# 37. Identity Observability

令 telemetry / observation map：

$$
\boxed{
H_B:
\mathcal X_B
\rightarrow
\mathcal Y_B.
}
$$

我們問：

> 是否存在只看 $H_B(x)$ 就能精確判定 $q_B(x)$ 的 classifier？

---

# 38. Carrier Identity Observability Theorem

## 定理 38.1

存在：

$$
\boxed{
g:
\mathcal Y_B
\rightarrow
\mathcal O_B
}
$$

使：

$$
\boxed{
q_B
=
g\circ H_B
}
$$

當且僅當：

$$
\boxed{
H_B(x_1)=H_B(x_2)
\Rightarrow
q_B(x_1)=q_B(x_2).
}
$$

### 證明

同 IPFC factorization theorem。

必要性：

若：

$$
q_B=gH_B
$$

且 observations 相同，則 identities 相同。

充分性：

在：

$$
\operatorname{im}H_B
$$

上定義：

$$
g(y)=q_B(x)
$$

其中：

$$
H_B(x)=y.
$$

由 observation-fiber constancy，定義與代表元無關。 $\square$

---

# 39. Identity-Unobservable Observation Fiber

若存在：

$$
x_1,x_2
$$

使：

$$
H_B(x_1)=H_B(x_2)
$$

但：

$$
q_B(x_1)\neq q_B(x_2),
$$

則：

$$
\boxed{
\text{exact operational identity is unobservable from }H_B.
}
$$

任何 deterministic exact classifier 都不可能只依該 telemetry 完成。

---

# 40. Identity-Related Profile $\Psi$ 的角色

如果：

$$
H_B=\Psi,
$$

則 Paper 07 的限制變成一個 factorization test：

$$
q_B
\stackrel{?}{=}
g\Psi.
$$

如果不存在：

$$
g,
$$

則：

$$
\Psi
$$

對 criterion $\kappa_B$ 不充分。

這把「identity-related observables 不等於 identity」從警語提升成可證條件。

---

# 41. Safety Observability 與 Identity Observability 不同

identity-safety property：

$$
P_I(x)
=
\mathbf 1
[
q_B(x)
\in
\mathcal A_B^{\mathrm{id}}
].
$$

可能：

$$
P_I
$$

可由 telemetry 判斷，

但完整：

$$
q_B
$$

不可判斷。

所以：

$$
\boxed{
\text{identity-safety observability}
\not\Rightarrow
\text{identity observability}.
}
$$

---

# 42. Identity Safety Classifier Theorem

存在：

$$
g_I:
\mathcal Y_B
\rightarrow
\{0,1\}
$$

使：

$$
P_I
=
g_IH_B
$$

當且僅當：

$$
H_B(x_1)=H_B(x_2)
\Rightarrow
P_I(x_1)=P_I(x_2).
$$

這是 Paper 10 observation-fiber theorem 的 identity-safety specialization。

---

# 43. Monitoring 不等於 Identity Verification

runtime monitor：

$$
M_t
=
\mathcal M(y_{0:t})
$$

可偵測：

- drift；
- anomaly；
- spec violation；
- safety margin。

但若 observation history fiber 仍跨 identity classes：

$$
\boxed{
\text{monitoring}
\neq
\text{exact identity verification}.
}
$$

---

# 44. State-Safe but Identity-Unsafe

可能：

$$
x_B'
\in
\mathcal S_B
$$

但：

$$
q_B(x_B')
\notin
\mathcal A_B^{\mathrm{id}}.
$$

所以：

$$
\boxed{
\text{state safety}
\not\Rightarrow
\text{identity safety}.
}
$$

---

# 45. Identity-Safe but Functionally Failed

也可能：

$$
q_B(x_B')=q_B(x_B)
$$

且：

$$
x_B'\in\mathcal S_B,
$$

但 task：

$$
H_T(x_B')
$$

失敗。

因此 identity preservation 不是一般 functional correctness certificate。

---

# 46. Network Identity Projection

對 $N$ 個 carriers：

$$
\mathbf X
=
(x_1,\ldots,x_N).
$$

各自：

$$
q_i:
\mathcal X_i
\rightarrow
\mathcal O_i.
$$

定義：

$$
\boxed{
Q_G(\mathbf X)
=
(
q_1(x_1),
\ldots,
q_N(x_N)
).
}
$$

---

# 47. Global Identity-Preserving Dynamics

global update：

$$
\Gamma_G:
\mathcal X_G
\rightarrow
\mathcal X_G.
$$

若：

$$
\boxed{
Q_G\Gamma_G
=
Q_G,
}
$$

則整個 network 的 carrier identity tuple 被保持。

---

# 48. Local-to-Global Identity Preservation Theorem

## 定理 48.1

若 global update 可分解成有限個局部 updates：

$$
\Gamma_G
=
U_m\circ\cdots\circ U_1,
$$

且每個 $U_k$ 對 $Q_G$ identity-preserving：

$$
Q_GU_k
=
Q_G,
$$

則：

$$
\boxed{
Q_G\Gamma_G
=
Q_G.
}
$$

### 證明

同有限 composition theorem。 $\square$

---

# 49. Identity Cascade

如果某 update 造成：

$$
q_i(x_i')
\neq
q_i(x_i),
$$

且該 identity transition 進一步改變：

- allowed operators；
- topology；
- trust relation；
- routing；
- access policy；

則後續 network propagation law 可變。

這是：

$$
\boxed{
\text{identity transition}
\rightarrow
\text{operator/topology transition}
\rightarrow
\text{new GPC dynamics}.
}
$$

本文只建立風險結構，不提供任何誘導 identity transition 的操作方法。

---

# 50. Lineage Graph for GPC Networks

定義：

$$
\boxed{
\mathcal G_L
=
(V_L,E_L).
}
$$

一條 edge：

$$
O_i^t
\rightarrow
O_j^{t+1}
$$

表示有經記錄的：

- update；
- migration；
- copy；
- fork；
- merge；

identity-lineage event。

network communication graph：

$$
\mathcal G_C
$$

與 lineage graph：

$$
\mathcal G_L
$$

一般不同。

---

# 51. Message Topology、Dynamical Topology、Lineage Topology 三分

$$
\boxed{
\mathcal G_{\mathrm{msg}}
\neq
\mathcal G_{\mathrm{dyn}}
\neq
\mathcal G_{\mathrm{lin}}.
}
$$

message graph：誰向誰發訊息。

dynamical graph：誰的 state 對誰有有效 gain。

lineage graph：哪個 identity 從哪個 identity 演化／分叉而來。

---

# 52. Physical Realization

PCPRT：

$$
\Pi_B:
\mathcal Z_B
\rightarrow
\mathcal X_B.
$$

physical dynamics：

$$
\Phi_B^{\mathrm{phys}}:
\mathcal Z_B
\rightarrow
\mathcal Z_B.
$$

effective update：

$$
\Gamma_B:
\mathcal X_B
\rightarrow
\mathcal X_B.
$$

要求：

$$
\Pi_B
\Phi_B^{\mathrm{phys}}
\approx
\Gamma_B
\Pi_B.
$$

---

# 53. Physical Carrier Identity Projection

identity 可定義於 effective state：

$$
q_B:
\mathcal X_B
\rightarrow
\mathcal O_B.
$$

組合：

$$
\boxed{
q_B\Pi_B:
\mathcal Z_B
\rightarrow
\mathcal O_B
}
$$

給 physical states 一個 criterion-relative carrier identity classification。

這仍不等同 metaphysical personal identity。

---

# 54. Realization Preservation 不等於 Identity Preservation

可能：

$$
\Pi_B
\Phi^{\mathrm{phys}}
\approx
\Gamma_B\Pi_B
$$

很好，

但：

$$
q_B\Gamma_B
\neq
q_B.
$$

即 physical realization 忠實實現了一個 **identity-changing effective dynamics**。

所以：

$$
\boxed{
\text{realization correctness}
\not\Rightarrow
\text{identity preservation}.
}
$$

---

# 55. Cross-Carrier Semantic Transduction 的四個判定

對：

$$
A\rightarrow B
$$

至少分：

## C0 — Semantic Identity

receiver 是否重構同一 chosen semantic identity？

## C1 — Semantic Phase

relational semantic phase 是否在 tolerance 內？

## C2 — Receiver Carrier Identity

receiver update 是否保持：

$$
q_B?
$$

## C3 — Lineage

若 carrier identity 變，lineage 是否被正確記錄／規格化？

---

# 56. Communication Identity Safety Matrix

因此一次 GPC event 不能只給：

$$
\text{success/fail}.
$$

建議至少輸出：

$$
\boxed{
\mathbf R_{\mathrm{GPC-ID}}
=
(
S_{\mathrm{sem}},
S_{\mathrm{phase}},
S_{\mathrm{func}},
S_{\mathrm{car-id}},
L_{\mathrm{status}},
R_{\mathrm{safe}}
).
}
$$

---

# 57. Conventional Communication as a Boundary Case

Shannon 型 communication theory 的核心 engineering abstraction 聚焦 source、transmitter、channel、receiver、destination 與 information rate/error，並刻意將 semantic aspects 從 engineering transmission problem 中分離。

IPFC–GPC 不否定這個抽象。

它只處理另一個問題：

> 當 receiver 本身是 persistent adaptive carrier 時，communication-induced state dynamics 是否需要額外安全與 identity specification？

---

# 58. Semantic Communication as a Neighbor, Not Identity Theory

DeepSC 類 semantic communication system 把 text semantic encoding / decoding 與 channel transmission聯合優化。

這支持：

$$
\boxed{
\text{communication quality can be task/semantic-relative}.
}
$$

但它不自動提供：

$$
q_B
$$

或 carrier identity theory。

因此：

$$
\boxed{
\text{semantic communication}
\neq
\text{carrier identity communication theory}.
}
$$

---

# 59. Bisimulation as Functional Neighbor

Park 1981 開啟的 bisimulation tradition 提供：

> 不同內部 states / processes 可在指定 transition behavior 下視為等價

的成熟形式語言。

IPFC–GPC 由此只吸收：

$$
\boxed{
\text{behavioral equivalence}
\neq
\text{state equality}.
}
$$

更不能自動升格為：

$$
\boxed{
\text{personal identity}.
}
$$

---

# 60. Provenance as Lineage Neighbor

data provenance 研究正式區分資料從哪裡來、哪些 source data 影響其存在，以及 transformation history。

這與 IPFC lineage 的工程精神相容。

但：

$$
\boxed{
\text{origin/derivation record}
\neq
\text{identity verdict}.
}
$$

provenance 是 lineage evidence，不是 identity 本身。

---

# 61. Operational Identity Claim Record

每一個 carrier identity claim 至少存：

$$
\boxed{
\mathfrak R_{\mathrm{id}}
=
(
\kappa,
q,
K,
H,
\Psi,
\Gamma,
L,
\mathcal A,
E,
R
).
}
$$

其中：

- $\kappa$：identity criterion；
- $q$：identity projection；
- $K$：scope/domain；
- $H$：observation map；
- $\Psi$：identity-related profile；
- $\Gamma$：state dynamics；
- $L$：lineage model；
- $\mathcal A$：admissible identity set；
- $E$：evidence；
- $R$：refutation / countercondition。

---

# 62. Identity Specification Before Verification

若沒有：

$$
\kappa
$$

與：

$$
q_\kappa,
$$

就不能說：

> 系統「已證明保持身份」。

只能說：

> 某些 observables / functions / lineage constraints 被保持。

因此：

$$
\boxed{
\text{identity verification quality}
\le
\text{identity specification quality}.
}
$$

這是邏輯依賴原則。

---

# 63. Falsification Conditions

## F1 — Criterion Missing

若「same receiver」沒有 operational $\kappa_B$：

identity claim 不完整。

## F2 — Fiber Preservation Failure

若存在 admissible：

$$
a,x_B
$$

使：

$$
q_BU_a(x_B)\neq q_B(x_B),
$$

則 strict carrier-identity preservation claim 被反證。

## F3 — Lineage Factorization Failure

若 source identity fiber 內不同 states transfer 到不同 target identities：

deterministic $L_{AB}$ 不存在。

## F4 — Observation-Fiber Ambiguity

若相同 telemetry 對應不同 operational identities：

exact identity classifier from that telemetry 不存在。

## F5 — Semantic/Carrier Conflation

若以 semantic fidelity 當 carrier identity certificate：

claim 類型錯誤。

## F6 — Recovery Conflation

若只回到 same identity fiber 就宣稱 exact state recovery：

claim 過強。

## F7 — First-Person Overclaim

任何從：

$$
q,\Psi,\mathbf C,L
$$

直接推出 first-person persistence 的 claim，超出本文模型。

---

# 64. Benchmark 1 — Persistent Receiver Update

對持續型 receiver：

$$
x_B^0
\rightarrow
x_B^1
\rightarrow
\cdots
\rightarrow
x_B^T
$$

記錄：

- state drift；
- identity class；
- semantic success；
- function；
- safety；
- history variation。

目的：

> 測 interaction sequence 是否保持 chosen identity fiber。

---

# 65. Benchmark 2 — Semantic Success vs Carrier Identity

建立四組：

1. semantic success + identity preserve；
2. semantic success + identity transition；
3. semantic failure + identity preserve；
4. semantic failure + identity transition。

測試二者是否在實際 system 中可分離。

---

# 66. Benchmark 3 — Cross-Carrier Lineage Factorization

對 source identity：

$$
O_A
$$

取多個 representatives：

$$
x_A^{(1)},\ldots,x_A^{(n)}.
$$

執行同一 transfer specification：

$$
T_{AB}^{X}.
$$

檢查：

$$
q_B(T_{AB}^{X}(x_A^{(i)}))
$$

是否全相同。

若否：

$$
\boxed{
L_{AB}(O_A)
}
$$

不能單值化。

---

# 67. Benchmark 4 — Identity Observability

在 telemetry：

$$
H_B
$$

上建立 pairs：

$$
x_1,x_2.
$$

尋找：

$$
H_B(x_1)=H_B(x_2)
$$

但：

$$
q_B(x_1)\neq q_B(x_2)
$$

的 counterexamples。

若找到，exact identity observability 被反證。

---

# 68. Benchmark 5 — Identity Recovery vs State Recovery

對 update/recovery pairs：

$$
R\circ U,
$$

分開測：

$$
d_\mathcal X(RU(x),x)
$$

與：

$$
\mathbf 1[q_B(RU(x))=q_B(x)].
$$

驗證：

> same identity recovery 可以在 full-state error 非零時成立。

---

# 69. Data Record

每次 GPC identity experiment 建議存：

```json
{
  "identity_criterion": "carrier-operational-v1",
  "receiver_identity_before": "...",
  "receiver_identity_after": "...",
  "semantic_identity_success": true,
  "semantic_phase_residual": {},
  "functional_success": true,
  "state_safe": true,
  "carrier_identity_preserved": true,
  "lineage_event": "none",
  "identity_observation_map": "...",
  "recovery_level": "not_tested"
}
```

所有數字與 label 必須來自實際 protocol / annotator / verifier，不得杜撰。

---

# 70. Theorem-Level Summary

本文主要形式結果：

1. Message-Family Fiber Invariance Theorem；
2. Finite Composition Identity Theorem；
3. Carrier-Lineage Factorization Theorem；
4. Branching No-Single-Lineage Proposition；
5. Semantic–Carrier Independence Proposition；
6. Identity Recovery Weakness Theorem；
7. Carrier Identity Observability Theorem；
8. Identity Safety Classifier Theorem；
9. Local-to-Global Identity Preservation Theorem。

---

# 71. 與 GPC-CS Paper 07 的關係

Paper 07 正確地保持保守：

$$
\Psi(x)
$$

只是 identity-related profile。

本文不推翻它。

IPFC Paper 04 新增：

$$
q_\kappa
$$

但要求：

> 只有在一個明示的 operational identity criterion 下，才把 states 商化成 identity classes。

因此 Paper 07 的五維 continuity vector：

$$
\mathbf C
=
(
C_{\mathrm{obs}},
C_{\mathrm{info}},
C_{\mathrm{func}},
C_{\mathrm{lin}},
C_{\mathrm{sub}}
)
$$

可以成為：

- $q_\kappa$ 的 features；
- evidence；
- constraint；

但不是自動等於：

$$
q_\kappa.
$$

---

# 72. 與 GPC-CS Paper 06 的關係

Paper 06 區分：

$$
\text{invertible},
\quad
\text{informationally recoverable},
\quad
\text{operationally recoverable},
\quad
\text{safely recoverable}.
$$

本文再加入：

$$
\boxed{
\text{identity recoverable}.
}
$$

因此 recovery hierarchy 更完整：

$$
\boxed{
\text{exact state recovery}
\Rightarrow
\text{identity recovery}
}
$$

但 identity recovery 還需另問：

- safe？
- history preserved？
- lineage correct？
- function preserved？

---

# 73. 與 GPC-CS Paper 10 的關係

Paper 10 的核心 observation-fiber 原理：

> property 可由 observation 精確判定，當且僅當 property 在 observation fibers 上為常數。

本文把 property 專門化為：

$$
q_\kappa
$$

或：

$$
P_I.
$$

所以 carrier identity observability 不需要另外發明神秘 metric。

它就是一個 factorization / sufficiency 問題。

---

# 74. 與 PCPRT 的關係

PCPRT 回答：

> carrier state 如何由 physical substrate 實現？

IPFC Paper 04 回答：

> effective carrier state 在 interaction 後是否仍位於同 identity fiber？

GPC-CS 回答：

> interaction 是否保持 safety / recoverability / network containment？

三者分工：

$$
\boxed{
\text{Physical realization}
\neq
\text{Identity classification}
\neq
\text{Safety verification}.
}
$$

---

# 75. 最終 Canonical Diagram

$$
\boxed{
\begin{array}{ccccc}
\mathcal Z_B
&
\xrightarrow{\Pi_B}
&
\mathcal X_B
&
\xrightarrow{q_B}
&
\mathcal O_B
\\
&&
\uparrow U_{AB}(x_A,\cdot)
&&
\\
&&
\mathcal X_B
&&
\end{array}
}
$$

interaction safety 問：

$$
U_{AB}(x_A,x_B)
\in
\mathcal S_B?
$$

identity preservation 問：

$$
q_BU_{AB}(x_A,x_B)
=
q_B(x_B)?
$$

semantic success 問：

$$
q_{\mathrm{sem}}(\hat x_B^{\mathrm{sem}})
=
F_Oq_{\mathrm{sem}}(x_A^{\mathrm{sem}})?
$$

lineage 問：

$$
q_BT_{AB}^{X}
=
L_{AB}q_A?
$$

四者不能合併成一個「communication success」布林值。

---

# 76. 結論

GPC-CS 最初最重要的改寫是：

> communication does not end at decoding; it ends at carrier-state transformation.

IPFC Paper 04 再補上：

> carrier-state transformation does not have a single identity consequence.

交流可以：

- 傳對語義；
- 傳錯語義；
- 改變 receiver state；
- 保持 receiver identity；
- 跨越 receiver identity boundary；
- 形成新 lineage；
- 保持 function；
- 改變 function；

這些是不同維度。

因此本文最終把 GPC identity safety 寫成：

$$
\boxed{
\text{GPC Identity Safety}
=
\text{Explicit Identity Criterion}
+
\text{Fiber Preservation / Admissibility}
+
\text{Lineage Correctness}
+
\text{Observation Sufficiency}
+
\text{Safe Recovery}.
}
$$

最核心的四個判定式是：

$$
\boxed{
q_BU_a=q_B
}
$$

—— interaction 是否 strict identity-preserving；

$$
\boxed{
q_BT_{AB}^{X}=L_{AB}q_A
}
$$

—— cross-carrier transfer 是否可下推成 lineage；

$$
\boxed{
q_B=gH_B
}
$$

—— operational identity 是否可由 telemetry 觀測；

$$
\boxed{
q_B(RU(x))=q_B(x)
}
$$

—— recovery 是否至少恢復 identity。

同時本文永久保留 GPC-CS Paper 07 的 epistemic boundary：

$$
\boxed{
\text{operational carrier identity}
\neq
\text{first-person continuity automatically}.
}
$$

所以 GPC 中的同一性問題不再需要在「完全不談身份」與「直接宣稱主體同一」之間二選一。

IPFC 提供第三條路：

> **先明示 criterion，再建立 fiber、lineage、observability 與 falsification；能證多少，就只說多少。**

---

# 77. 後續

## IPFC Paper 05
**《Phase Module Calculus：XX 相位的通用接駁、組合與反證規格》**

## IPFC Paper 06
**《AI Fork、忒修斯與語義分裂：Identity Lineage 的計算模型》**

## GPC Identity Benchmark 01
**Persistent Receiver Identity Preservation**

## GPC Identity Benchmark 02
**Cross-Carrier Lineage Factorization**

---

# 參考文獻

1. Neo.K & Aletheia. *同一性–相位纖維微積分：從身份投影、索引 Holonomy 到相位動力學的統一接口*. IPFC Paper 01, EveMissLab, 2026.
2. Neo.K & Aletheia. *相位語義：語義身份、關係座標、Context Transport 與 Semantic Holonomy*. IPFC Paper 02, EveMissLab, 2026.
3. Neo.K & Aletheia. *相變與同一性分岔：Identity-Preserving Regime Change 與 Lineage Transition*. IPFC Paper 03, EveMissLab, 2026.
4. EveMissLab. *GPC-CS Paper 06: Irreversible Updates and Path-Dependent Safety*. 2026.
5. EveMissLab. *GPC-CS Paper 07: Identity Drift and Cross-Carrier Continuity*. 2026.
6. EveMissLab. *GPC-CS Paper 10: Observability, Verifiability, and Falsification*. 2026.
7. Shannon, C. E. “A Mathematical Theory of Communication.” *Bell System Technical Journal* 27, 379–423, 623–656 (1948). DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x.
8. Xie, H., Qin, Z., Li, G. Y., & Juang, B.-H. “Deep Learning Enabled Semantic Communication Systems.” *IEEE Transactions on Signal Processing* 69, 2663–2675 (2021). DOI: 10.1109/TSP.2021.3071210.
9. Park, D. “Concurrency and Automata on Infinite Sequences.” In *Theoretical Computer Science*, LNCS 104, 167–183 (1981). DOI: 10.1007/BFb0017309.
10. Buneman, P., Khanna, S., & Tan, W.-C. “Why and Where: A Characterization of Data Provenance.” ICDT 2001, LNCS 1973, 316–330. DOI: 10.1007/3-540-44503-X_20.
11. EveMissLab. *PCPRT Papers 01–08*. 2026.
12. EveMissLab. *Phase Canon v1.1*. 2026.

---

**IPFC Paper 04 v1.0 — COMPLETE.**
