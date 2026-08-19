# Phase Module Calculus：XX 相位的通用接駁、組合與反證規格
## Phase Module Calculus: A General Interface for Typed Phase Attachment, Composition, and Falsification

**系列**：Identity–Phase Fiber Calculus（IPFC）  
**論文**：Paper 05 / Core-Series Closure Paper  
**版本**：v1.0  
**日期**：2026-08-15  
**作者**：Neo.K（許筌崴）with Aletheia  
**機構**：EveMissLab（一言諾科技有限公司），台灣  
**文件性質**：模組化數學框架／接口規格／組合與驗證理論  
**上游**：
- IPFC Paper 01《同一性–相位纖維微積分》
- IPFC Paper 02《相位語義》
- IPFC Paper 03《相變與同一性分岔》
- IPFC Paper 04《GPC 中的載體同一性》
- EveMissLab Phase Canon v1.1
- GPC-CS Papers 00–10
- PCPRT Papers 01–08

**形式化狀態**：本文新定理目前為手工形式證明，尚未完成 Lean 4 / Coq 機器驗證。  
**核心地位**：本文把 Papers 01–04 的結構收斂為 IPFC 第一版通用 Phase Module 語言。

---

# 摘要

EveMissLab 相位理論經 Phase Canon v1.1 稽核後，已明確拒絕「任何跨域狀態都可直接叫 phase」的做法；IPFC Papers 01–04 又依次建立 identity fiber、semantic phase、phase/identity transition 與 GPC carrier identity safety。然而，若未來每一個「認知相位、時間相位、AI 相位、法律相位、工程相位、神經相位、材料相位」都重新自造一套 state、identity、phase、transport 與 validation 語言，理論仍會重新碎裂。

本文提出 **Phase Module Calculus（PMC）**，將任何可被 IPFC / Phase Canon 接納的 phase domain 統一表示為一個帶型模組：

$$
\boxed{
\mathfrak M
=
(
D,
\kappa,
\mathcal X,
\mathcal O,
q,
\mathcal C,
\tau,
\Phi,
\Theta,
\mathcal T,
\Gamma,
H,
L,
\Pi,
\mathsf A,
\mathsf G,
\mathsf R
).
}
$$

其中：

- $D$：domain；
- $\kappa$：identity criterion；
- $\mathcal X$：state space；
- $\mathcal O$：identity space；
- $q$：identity projection；
- $\mathcal C$：context/index/interface space；
- $\tau=(PH,IF)$：Phase Canon × IPFC 雙型別；
- $\Phi$：phase space；
- $\Theta$：phase extractor；
- $\mathcal T$：transport family；
- $\Gamma$：dynamics；
- $H$：observable/task map；
- $L$：lineage；
- $\Pi$：physical realization map，若宣稱 physical；
- $\mathsf A,\mathsf G$：assumption / guarantee contract；
- $\mathsf R$：refutation / falsification rule。

本文定義 **Exact Phase Module Morphism** 為同時保持 identity、phase、dynamics、observable 與 lineage diagrams 的 map family，並證明 identity morphisms 與 composition 使 exact phase modules 構成一個 category。若兩個 morphisms 只近似交換，本文建立 identity、phase 與 dynamics defect 的 composition bounds；例如在 metric/Lipschitz 條件下：

$$
\boxed{
\varepsilon_q(G\circ F)
\le
\varepsilon_q(G)
+
\operatorname{Lip}(G_O)\varepsilon_q(F).
}
$$

本文亦證明 **Phase Module Quotient Theorem**：對 coarse-graining map：

$$
C:
\mathcal X
\twoheadrightarrow
\bar{\mathcal X},
$$

identity、phase、observable 與 dynamics 可同時下推到 reduced module，當且僅當各自對 $C$ -fibers 具有相應 constancy / consistency。這把 Phase Canon 的 fiber test、PCPRT 的 coarse-graining、IPFC 的 identity fiber 與語義 phase sufficiency 收斂到同一 factorization schema。

對 path-dependent modules，本文證明 **Holonomy Conjugacy Theorem**：若 phase-module isomorphism 與 transport 相容，則 closed-loop holonomy 以共軛方式對應；故「是否存在 nontrivial holonomy」在 module isomorphism 下保持，而具體座標表示可改變。對模組契約，本文引入 assume–guarantee compatibility，證明 sequential composition 在 upstream guarantee 滿足 downstream assumption 時可繼承組合 guarantee，並給出 contract refinement / replacement rule。

最後，本文將 Phase Canon 的「No type jump without a map」轉寫為 PMC 的 type-elevation gate：PH-5 / PH-6 module 若沒有 physical realization record：

$$
\Pi:
\mathcal Z_{\mathrm{phys}}
\rightarrow
\mathcal X
$$

及其 observables / defect / falsification，不得因存在 module morphism、語義相似、holonomy 或 phase vocabulary 而自動提升為 PH-0。

本文因此把「XX 相位」從自然語言命名問題，轉成一個模組合格性問題：

$$
\boxed{
\text{Define identity}
\rightarrow
\text{define phase}
\rightarrow
\text{define transport/dynamics}
\rightarrow
\text{define observables}
\rightarrow
\text{define composition}
\rightarrow
\text{define falsification}.
}
$$

**關鍵詞**：Phase Module、IPFC、相位模組、組合性、Category、Contract、Coarse-Graining、Holonomy、Falsification、Phase Canon、Assume–Guarantee

---

# 1. 為什麼需要 Phase Module Calculus

Phase Canon 解決：

> phase 是哪一型？

IPFC Paper 01 解決：

> phase 相對 identity fiber 扮演什麼角色？

Papers 02–04 已展示：

- semantic phase；
- phase/identity transition；
- GPC carrier identity；

都能掛入同一母接口。

但還缺一層：

> **不同 domain module 之間如何合法連接、組合、替換、粗粒化與驗證？**

這就是 PMC。

---

# 2. 模組化不是「所有 domain 變成同一理論」

PMC 不主張：

$$
\boxed{
\mathfrak M_A
=
\mathfrak M_B
}
$$

只因：

- 都有 phase；
- 都有 state；
- 都有 identity；
- 都有 transport。

它只要求：

> 若要跨模組傳遞 claim，就必須明示 mapping 與交換圖。

所以：

$$
\boxed{
\text{shared interface}
\neq
\text{shared ontology}.
}
$$

---

# 3. Phase Module 的正式定義

## 定義 3.1 — Phase Module

一個 Phase Module 為：

$$
\boxed{
\mathfrak M
=
(
D,
\kappa,
\mathcal X,
\mathcal O,
q,
\mathcal C,
\tau,
\Phi,
\Theta,
\mathcal T,
\Gamma,
H,
L,
\Pi,
\mathsf A,
\mathsf G,
\mathsf R
).
}
$$

---

# 4. Domain 與 Identity

$$
D
$$

指定研究域。

$$
\kappa
$$

指定 identity criterion。

$$
q:
\mathcal X
\twoheadrightarrow
\mathcal O
$$

指定 identity projection。

沒有：

$$
(\kappa,q)
$$

就不知道 module 中「哪一個東西」正在變。

---

# 5. Phase Double Type

$$
\boxed{
\tau
=
(
PH,
IF
).
}
$$

其中：

$$
PH
\in
\{
PH\text{-}0,\ldots,PH\text{-}6
\}
$$

回答：

> phase 的數學／功能型是什麼？

而：

$$
IF
\in
\{
IF\text{-}0,\ldots,IF\text{-}4
\}
$$

回答：

> phase 相對 identity 的角色是什麼？

---

# 6. Phase Space 與 Extractor

$$
\Phi
$$

必須是明示的 phase space。

$$
\boxed{
\Theta:
\mathcal X
\times
\mathcal C
\rightarrow
\Phi.
}
$$

不能只寫：

$$
\phi(x)
$$

卻不說 $\Phi$ 是：

- $S^1$ ；
- order-parameter space；
- group；
- manifold；
- typed relation vector；
- graph state；
- search discrepancy space。

---

# 7. Transport Family

若 module 使用 path / holonomy 語言，必須有：

$$
\boxed{
\mathcal T
=
\{
T_\gamma
\}.
}
$$

並至少滿足：

$$
T_{\operatorname{id}}
=
\operatorname{id}
$$

與合法 path composition：

$$
\boxed{
T_{\gamma_2\circ\gamma_1}
=
T_{\gamma_2}
\circ
T_{\gamma_1}.
}
$$

若沒有：

$$
\mathcal T,
$$

不得宣稱 holonomy。

---

# 8. Dynamics

$$
\boxed{
\Gamma:
\mathcal X
\rightarrow
\mathcal X'
}
$$

描述 state evolution / update。

module 可以：

- static；
- discrete-time；
- continuous-time；
- stochastic；
- path-indexed。

若沒有 dynamics，就不能把靜態相似度描述成 phase dynamics。

---

# 9. Observable / Task Map

$$
\boxed{
H:
\mathcal X
\rightarrow
\mathcal Y
}
$$

回答：

> phase / state 對什麼可測結果有意義？

若：

$$
\Theta
$$

沒有任何 observable / structural / predictive role，

phase 可能只是 nomenclature。

---

# 10. Lineage

若 identity 可能改變，必須指定：

$$
\boxed{
L:
\mathcal O
\rightarrow
\mathcal O'
}
$$

或：

- relation-valued lineage；
- graph lineage；
- stochastic kernel。

若 identity 絕對要求保持：

$$
L=\operatorname{id}.
$$

---

# 11. Physical Realization

只有宣稱 physical elevation 時要求：

$$
\boxed{
\Pi:
\mathcal Z_{\mathrm{phys}}
\rightarrow
\mathcal X.
}
$$

並配：

$$
\Pi\Phi_{\mathrm{phys}}
\approx
\Gamma\Pi.
$$

如果 module 是 PH-5 / PH-6 generalized phase，可以：

$$
\Pi=\varnothing
$$

或標記：

> no physical realization claim。

---

# 12. Falsification Rule

$$
\boxed{
\mathsf R
}
$$

至少應回答：

- identity criterion 如何失效？
- phase necessity 如何被 ablation 反證？
- transport 如何被反證？
- physical realization 如何被反證？
- benchmark failure 門檻？
- type claim 如何降級？

沒有 $\mathsf R$ 的 module 不能進 current Canon。

---

# 13. Phase Module Contract

module 還可帶 assume–guarantee contract：

$$
\boxed{
\mathsf C_{\mathfrak M}
=
(
\mathsf A,
\mathsf G
).
}
$$

其中：

- $\mathsf A$：environment / input / upstream assumptions；
- $\mathsf G$：在 assumptions 成立時 module 承諾的 guarantees。

例如：

- input phase range；
- identity criterion availability；
- telemetry sufficiency；
- realization domain；
- noise bound；
- task definition。

---

# 14. Canon-Admissible Phase Module

## 定義 14.1

一個 module 稱 **canon-admissible**，若至少：

1. $\kappa$ 明示；
2. $q$ 明示；
3. PH type 明示；
4. IF type 明示；
5. $\Phi$ 明示；
6. $\Theta$ 明示；
7. 若宣稱 dynamics， $\Gamma$ 明示；
8. 若宣稱 holonomy， $\mathcal T$ 明示；
9. $H$ 或 structural necessity test 明示；
10. 若 identity 可改變，lineage 明示；
11. 若宣稱 physical， $\Pi$ 明示；
12. $\mathsf R$ 明示。

---

# 15. Exact Phase Module Morphism

令：

$$
\mathfrak M_A
$$

與：

$$
\mathfrak M_B
$$

為兩個 modules。

定義 morphism：

$$
\boxed{
F
=
(
F_X,
F_O,
F_C,
F_\Phi,
F_Y
)
}
$$

必要時再加：

$$
F_Z
$$

於 physical states。

---

# 16. Identity Compatibility

要求：

$$
\boxed{
q_BF_X
=
F_Oq_A.
}
$$

這代表：

> state mapping 與 identity mapping 相容。

---

# 17. Phase Compatibility

要求：

$$
\boxed{
\Theta_B
(
F_Xx,
F_Cc
)
=
F_\Phi
\left(
\Theta_A(x,c)
\right).
}
$$

簡記：

$$
\boxed{
\Theta_BF_X
=
F_\Phi\Theta_A.
}
$$

---

# 18. Dynamics Compatibility

若兩 module 都有 dynamics：

$$
\Gamma_A,
\Gamma_B,
$$

要求：

$$
\boxed{
F_X\Gamma_A
=
\Gamma_BF_X.
}
$$

這是 conjugacy / semiconjugacy 型 compatibility。

---

# 19. Observable Compatibility

要求存在：

$$
F_Y:
\mathcal Y_A
\rightarrow
\mathcal Y_B
$$

使：

$$
\boxed{
H_BF_X
=
F_YH_A.
}
$$

---

# 20. Lineage Compatibility

若有 identity transitions：

$$
L_A:
\mathcal O_A
\rightarrow
\mathcal O_A',
$$

$$
L_B:
\mathcal O_B
\rightarrow
\mathcal O_B',
$$

以及 identity maps before/after：

$$
F_O,
F_O',
$$

要求：

$$
\boxed{
F_O'L_A
=
L_BF_O.
}
$$

---

# 21. Realization Compatibility

若雙方都宣稱 physical：

$$
\Pi_A:
\mathcal Z_A
\rightarrow
\mathcal X_A,
$$

$$
\Pi_B:
\mathcal Z_B
\rightarrow
\mathcal X_B,
$$

則需 physical map：

$$
F_Z:
\mathcal Z_A
\rightarrow
\mathcal Z_B
$$

滿足：

$$
\boxed{
F_X\Pi_A
=
\Pi_BF_Z.
}
$$

沒有這個 square，不得把 generalized module morphism 當 physical realization morphism。

---

# 22. Exact Morphism

## 定義 22.1

若相關 identity、phase、dynamics、observable、lineage 以及聲稱之 realization diagrams 全部交換，稱：

$$
\boxed{
F:
\mathfrak M_A
\rightarrow
\mathfrak M_B
}
$$

為 **Exact Phase Module Morphism**。

---

# 23. Identity Morphism

對任一 module：

$$
\mathfrak M,
$$

定義：

$$
\boxed{
\operatorname{id}_{\mathfrak M}
=
(
\operatorname{id}_X,
\operatorname{id}_O,
\operatorname{id}_C,
\operatorname{id}_\Phi,
\operatorname{id}_Y
).
}
$$

每個交換圖平凡成立。

---

# 24. Exact Morphism Composition Theorem

## 定理 24.1

若：

$$
\mathfrak M_A
\xrightarrow{F}
\mathfrak M_B
\xrightarrow{G}
\mathfrak M_C
$$

為 exact morphisms，則：

$$
\boxed{
G\circ F
:
\mathfrak M_A
\rightarrow
\mathfrak M_C
}
$$

亦為 exact morphism。

### 證明

identity：

$$
q_CG_XF_X
=
G_Oq_BF_X
=
G_OF_Oq_A.
$$

phase：

$$
\Theta_CG_XF_X
=
G_\Phi\Theta_BF_X
=
G_\Phi F_\Phi\Theta_A.
$$

dynamics：

$$
G_XF_X\Gamma_A
=
G_X\Gamma_BF_X
=
\Gamma_CG_XF_X.
$$

observable：

$$
H_CG_XF_X
=
G_YH_BF_X
=
G_YF_YH_A.
$$

lineage 與 realization 同理。 $\square$

---

# 25. Phase Modules Form a Category

## 定理 25.1

在固定的合法 interface notion 下：

- objects：canon-admissible Phase Modules；
- morphisms：Exact Phase Module Morphisms；

連同：

- identity morphisms；
- morphism composition；

形成一個 category，記為：

$$
\boxed{
\mathbf{PhaseMod}_{\mathrm{IPFC}}.
}
$$

### 證明

identity laws 與 associativity 逐分量繼承自 functions/maps 的 composition。定理 24.1 保證 closure。 $\square$

---

# 26. 這不是宣稱新 category theory

 $\mathbf{PhaseMod}_{\mathrm{IPFC}}$ 是 IPFC 的專用結構。

外部 applied category theory 已有大量 open-system composition：

- decorated cospans；
- structured cospans；
- decorated corelations；
- wiring/interface formalisms。

本文不宣稱重新發明 open-system category theory。

PMC 的新增內容是把：

$$
\boxed{
\text{identity}
+
\text{typed phase}
+
\text{lineage}
+
\text{realization}
+
\text{falsification}
}
$$

打包成 domain module contract。

---

# 27. Approximate Morphism

實際跨模型／跨載體通常只有近似交換。

定義 identity defect：

$$
\boxed{
\varepsilon_q(F)
=
\sup_x
d_{O_B}
\left(
q_BF_X(x),
F_Oq_A(x)
\right).
}
$$

phase defect：

$$
\boxed{
\varepsilon_\Phi(F)
=
\sup_{x,c}
d_{\Phi_B}
\left(
\Theta_B(F_Xx,F_Cc),
F_\Phi\Theta_A(x,c)
\right).
}
$$

dynamics defect：

$$
\boxed{
\varepsilon_\Gamma(F)
=
\sup_x
d_{X_B}
\left(
F_X\Gamma_A(x),
\Gamma_BF_X(x)
\right).
}
$$

---

# 28. Approximate Identity Composition Bound

## 定理 28.1

假設：

$$
F:
A\rightarrow B,
$$

$$
G:
B\rightarrow C
$$

是 approximate morphisms，且：

$$
G_O
$$

是：

$$
K_O
$$

-Lipschitz。

則：

$$
\boxed{
\varepsilon_q(G\circ F)
\le
\varepsilon_q(G)
+
K_O\varepsilon_q(F).
}
$$

### 證明

任取 $x$：

$$
d
\left(
q_CG_XF_Xx,
G_OF_Oq_Ax
\right)
$$

不超過：

$$
d
\left(
q_CG_XF_Xx,
G_Oq_BF_Xx
\right)
+
d
\left(
G_Oq_BF_Xx,
G_OF_Oq_Ax
\right).
$$

第一項：

$$
\le
\varepsilon_q(G).
$$

第二項由 Lipschitz：

$$
\le
K_O
d
\left(
q_BF_Xx,
F_Oq_Ax
\right)
\le
K_O\varepsilon_q(F).
$$

取 supremum 即得。 $\square$

---

# 29. Approximate Phase Composition Bound

## 定理 29.1

若：

$$
G_\Phi
$$

為：

$$
K_\Phi
$$

-Lipschitz，則在 context maps 相容的條件下：

$$
\boxed{
\varepsilon_\Phi(G\circ F)
\le
\varepsilon_\Phi(G)
+
K_\Phi\varepsilon_\Phi(F).
}
$$

證明與定理 28.1 同型。 $\square$

---

# 30. Approximate Dynamics Composition Bound

## 定理 30.1

若：

$$
G_X
$$

為：

$$
K_X
$$

-Lipschitz，則：

$$
\boxed{
\varepsilon_\Gamma(G\circ F)
\le
\varepsilon_\Gamma(G)
+
K_X\varepsilon_\Gamma(F).
}
$$

在兩 module dynamics 及 mapping domain 相容時成立。

---

# 31. Defect Ledger

所以跨多 module chain：

$$
\mathfrak M_0
\rightarrow
\mathfrak M_1
\rightarrow
\cdots
\rightarrow
\mathfrak M_n
$$

不能只寫：

> approximately aligned。

至少要記：

$$
\boxed{
\boldsymbol\varepsilon
=
(
\varepsilon_q,
\varepsilon_\Phi,
\varepsilon_\Gamma,
\varepsilon_H,
\varepsilon_L,
\varepsilon_\Pi
).
}
$$

不同 defect 不應無理由壓成單一 score。

---

# 32. Phase Module Isomorphism

若 exact morphism：

$$
F:
\mathfrak M_A
\rightarrow
\mathfrak M_B
$$

存在 exact inverse：

$$
F^{-1},
$$

則稱兩 modules isomorphic：

$$
\boxed{
\mathfrak M_A
\cong
\mathfrak M_B.
}
$$

這比「兩邊都有 phase」強很多。

---

# 33. Transport-Preserving Morphism

若 context path：

$$
\gamma
$$

在 A module 映到：

$$
F_C(\gamma)
$$

在 B module，

要求：

$$
\boxed{
F_XT_\gamma^A
=
T_{F_C(\gamma)}^BF_X.
}
$$

這使 transport 也成為 morphism 的一部分。

---

# 34. Holonomy Conjugacy Theorem

## 定理 34.1

假設：

$$
F:
\mathfrak M_A
\rightarrow
\mathfrak M_B
$$

為 transport-preserving module isomorphism。

對 closed loop：

$$
\gamma,
$$

有：

$$
\boxed{
\operatorname{Hol}_{F_C(\gamma)}^B
=
F_X
\operatorname{Hol}_\gamma^A
F_X^{-1}.
}
$$

### 證明

由 transport compatibility：

$$
F_XT_\gamma^A
=
T_{F_C(\gamma)}^BF_X.
$$

右乘：

$$
F_X^{-1}
$$

得：

$$
T_{F_C(\gamma)}^B
=
F_XT_\gamma^AF_X^{-1}.
$$

closed loop transport 即 holonomy。 $\square$

---

# 35. Holonomy Nontriviality Corollary

module isomorphism 下：

$$
\operatorname{Hol}_\gamma^A
=
\operatorname{id}
$$

當且僅當：

$$
\operatorname{Hol}_{F_C(\gamma)}^B
=
\operatorname{id}.
$$

所以：

$$
\boxed{
\text{nontrivial holonomy existence is representation-invariant under module isomorphism}.
}
$$

但具體座標／矩陣表示可以不同。

---

# 36. Direct Product Phase Module

兩個獨立 modules：

$$
\mathfrak M_A,
\mathfrak M_B.
$$

定義 product state：

$$
\mathcal X_{A\times B}
=
\mathcal X_A
\times
\mathcal X_B.
$$

identity：

$$
q_{A\times B}(x_A,x_B)
=
(
q_A(x_A),
q_B(x_B)
).
$$

phase：

$$
\Theta_{A\times B}
=
(
\Theta_A,
\Theta_B
).
$$

---

# 37. Product Fiber Theorem

## 定理 37.1

$$
\boxed{
F_{(O_A,O_B)}^{A\times B}
=
F_{O_A}^A
\times
F_{O_B}^B.
}
$$

### 證明

由 product identity projection 定義直接展開。 $\square$

---

# 38. Product 不代表 Coupling

direct product 只表示：

> 兩 modules 並列。

如果有 interaction：

$$
\Gamma_{AB}
$$

依賴雙方 state，

需要明確定義 coupled module。

不能因寫：

$$
\mathfrak M_A\times\mathfrak M_B
$$

就假裝 interaction 已被建模。

---

# 39. Phase Module Coarse-Graining

給定滿射：

$$
\boxed{
C:
\mathcal X
\twoheadrightarrow
\bar{\mathcal X}.
}
$$

問：

> 能否在 reduced state space 上保留 identity、phase、observable、dynamics？

---

# 40. Identity Factorization Criterion

存在：

$$
\bar q:
\bar{\mathcal X}
\rightarrow
\mathcal O
$$

使：

$$
q
=
\bar q C
$$

當且僅當：

$$
\boxed{
C(x_1)=C(x_2)
\Rightarrow
q(x_1)=q(x_2).
}
$$

---

# 41. Phase Factorization Criterion

存在：

$$
\bar\Theta
$$

使：

$$
\Theta
=
\bar\Theta C
$$

當且僅當：

$$
\boxed{
C(x_1)=C(x_2)
\Rightarrow
\Theta(x_1)=\Theta(x_2).
}
$$

context-dependent case 按固定 context 或擴張 state 處理。

---

# 42. Observable Factorization Criterion

存在：

$$
\bar H
$$

使：

$$
H
=
\bar HC
$$

當且僅當：

$$
\boxed{
C(x_1)=C(x_2)
\Rightarrow
H(x_1)=H(x_2).
}
$$

---

# 43. Dynamics Factorization Criterion

存在：

$$
\bar\Gamma:
\bar{\mathcal X}
\rightarrow
\bar{\mathcal X}
$$

使：

$$
\boxed{
C\Gamma
=
\bar\Gamma C
}
$$

當且僅當：

$$
\boxed{
C(x_1)=C(x_2)
\Rightarrow
C\Gamma(x_1)=C\Gamma(x_2).
}
$$

---

# 44. Phase Module Quotient Theorem

## 定理 44.1

給定：

$$
C:
\mathcal X
\twoheadrightarrow
\bar{\mathcal X},
$$

若：

- identity 對 $C$ -fibers constant；
- phase 對 $C$ -fibers constant；
- observable 對 $C$ -fibers constant；
- downstream coarse dynamics 對 $C$ -fibers consistent；

則存在 reduced module：

$$
\boxed{
\bar{\mathfrak M}
}
$$

與 quotient morphism：

$$
\boxed{
C_{\mathfrak M}:
\mathfrak M
\rightarrow
\bar{\mathfrak M}
}
$$

使 identity、phase、observable 與 dynamics diagrams 同時交換。

若任一 required property 對 $C$ -fibers 不 constant/consistent，該 property 不能被此 coarse-graining 精確保留。

### 證明

逐項使用 factorization criteria 40–43。 $\square$

---

# 45. 這統一了多條舊線

同一 factorization pattern 出現在：

- PCPRT fiber sufficiency；
- GPC Paper 10 observability；
- IPFC lineage factorization；
- Semantic identity recoverability；
- Semantic task sufficiency；
- Carrier identity observability。

所以 Phase Module Calculus 的真正共同核心是：

$$
\boxed{
\text{A high-level quantity exists exactly when it is constant on the fibers being quotiented out.}
}
$$

---

# 46. Assume–Guarantee Compatibility

令：

$$
\mathsf C_A
=
(
\mathsf A_A,
\mathsf G_A
)
$$

與：

$$
\mathsf C_B
=
(
\mathsf A_B,
\mathsf G_B
).
$$

若 A 的 output/interface guarantee 可以作 B 的 admissible input：

$$
\boxed{
\mathsf G_A
\subseteq
\mathsf A_B,
}
$$

稱 sequentially compatible。

---

# 47. Sequential Contract Composition Theorem

## 定理 47.1

假設：

1. module A 在 $\mathsf A_A$ 下保證 $\mathsf G_A$ ；
2. module B 在 $\mathsf A_B$ 下保證 $\mathsf G_B$ ；
3.
   $$
   \mathsf G_A
   \subseteq
   \mathsf A_B.
   $$

則 sequential composition：

$$
A
\rightarrow
B
$$

在 upstream assumptions：

$$
\mathsf A_A
$$

成立時可繼承 downstream guarantee：

$$
\boxed{
\mathsf G_B.
}
$$

### 證明

由 A contract：

$$
\mathsf A_A
\Rightarrow
\mathsf G_A.
$$

compatibility 給：

$$
\mathsf G_A
\Rightarrow
\mathsf A_B.
$$

B contract：

$$
\mathsf A_B
\Rightarrow
\mathsf G_B.
$$

合成即：

$$
\mathsf A_A
\Rightarrow
\mathsf G_B.
\qquad\square
$$

---

# 48. Contract Composition 不是所有循環系統都自動安全

對 feedback / cyclic interconnection，

單純：

$$
\mathsf G_A\subseteq\mathsf A_B,
\qquad
\mathsf G_B\subseteq\mathsf A_A
$$

不必自動解決：

- well-posedness；
- circular assumption；
- finite-time transient；
- gain amplification；
- hidden shared state。

所以循環 composition 仍需更強的 contract semantics / fixed-point / small-gain / invariance analysis。

PMC 不把簡單 set inclusion 過度推廣。

---

# 49. Contract Refinement

為避免方向歧義，本文定義：

$$
\boxed{
\mathsf C'
\preceq
\mathsf C
}
$$

表示：

> $\mathsf C'$ 是 $\mathsf C$ 的可替換 refinement。

要求：

$$
\boxed{
\mathsf A
\subseteq
\mathsf A'
}
$$

即新 module 接受至少同樣多的 environments；

並：

$$
\boxed{
\mathsf G'
\subseteq
\mathsf G
}
$$

即新 module 保證不比舊 module 更弱。

---

# 50. Replacement Theorem

## 定理 50.1

若 module：

$$
M'
$$

與：

$$
M
$$

interface-compatible，且：

$$
\mathsf C_{M'}
\preceq
\mathsf C_M,
$$

則任何只依賴：

$$
\mathsf A_M
\Rightarrow
\mathsf G_M
$$

的上層 sequential proof，在相同 interface assumptions 下不會因以 $M'$ 取代 $M$ 而失效。

### 說明

此定理只針對 contract-level proof。

若上層還依賴：

- latency；
- hidden state；
- phase holonomy；
- identity lineage；
- physical realization；

這些也必須被納入 contract。

---

# 51. Phase Contract 必須把 Identity 寫進 Guarantee

若上層需要：

$$
q\Gamma=q,
$$

那 identity preservation 必須出現在：

$$
\mathsf G.
$$

不能只寫：

> output function correct。

同理，若 holonomy 必須為零：

$$
\operatorname{Hol}_\gamma
=
\operatorname{id},
$$

也必須進 guarantee。

---

# 52. Type-Elevation Gate

## 規則 52.1

若 source module：

$$
PH\text{-}5
\quad\text{或}\quad
PH\text{-}6
$$

要宣稱 target：

$$
PH\text{-}0,
$$

至少需：

1. physical state space：
   $$
   \mathcal Z_{\mathrm{phys}};
   $$
2. realization map：
   $$
   \Pi;
   $$
3. physical dynamics；
4. observable map；
5. realization defect；
6. falsification rule。

---

# 53. Module Morphism 不自動授權 Type Jump

即使存在：

$$
F:
\mathfrak M_{\mathrm{sem}}
\rightarrow
\mathfrak M_{\mathrm{phys}},
$$

也不能只因：

$$
F_\Phi
$$

存在，就說 semantic phase 是 physical phase。

必須額外證明：

$$
\boxed{
F_X\Pi_{\mathrm{source}}
=
\Pi_{\mathrm{target}}F_Z
}
$$

或其他合法 realization bridge。

所以：

$$
\boxed{
\text{phase morphism}
\neq
\text{physical realization automatically}.
}
$$

---

# 54. No-Type-Jump Corollary

在 canon-admissible PMC 中，若 physical realization record 缺失，module 的 current PH type 不得僅由 cross-domain morphism 提升至 PH-0。

這是 Phase Canon：

$$
\boxed{
\text{No type jump without a map}
}
$$

在 module calculus 中的直接治理規則。

---

# 55. Module Equivalence vs Module Similarity

兩 modules 可以：

- phase score 相近；
- outputs 相近；
- equations 長得相似；

卻不構成：

$$
\mathfrak M_A
\cong
\mathfrak M_B.
$$

isomorphism 需要完整 compatible inverse maps。

所以：

$$
\boxed{
\text{similar formula}
\neq
\text{module equivalence}.
}
$$

---

# 56. Semantic Phase Module

Paper 02 可註冊為：

$$
\boxed{
\mathfrak M_{\mathrm{sem}}.
}
$$

其核心：

- $PH=5$ ；
- $IF=1/2/3/4$ ；
- identity：
  sense/concept/proposition/intent；
- phase：
  typed semantic relation；
- transport：
  context / translation / agent path；
- holonomy：
  semantic loop residual；
- lineage：
  sense split / ontology split。

---

# 57. Neural Phase Module

可分：

$$
PH\text{-}0/1/4.
$$

identity criterion：

- neuron；
- circuit；
- population；
- functional assembly。

phase space：

$$
S^1
$$

或 relative/coherence variables。

若從 neural phase 升到 semantic phase，必須有 module morphism / task map，而不能寫成：

$$
\text{neural phase}
=
\text{meaning}.
$$

---

# 58. Epistemic Search Phase Module

GIPSS / GIPE：

$$
PH\text{-}6.
$$

通常：

$$
IF\text{-}3
$$

因為 phase 是 candidate–target relational discrepancy。

其 phase space 更像 typed search/control vector，而不是：

$$
S^1.
$$

所以「search phase」不需要 circular geometry 才合法。

---

# 59. Internal-Time Module

若 literal oscillator：

$$
PH\text{-}0.
$$

若是 progress / relational internal time：

$$
PH\text{-}5.
$$

IF role 可為：

$$
IF\text{-}1/2.
$$

同一名稱「時間相位」可能因此對應不同 modules。

必須拆型。

---

# 60. Material / Regime Module

$$
PH\text{-}2.
$$

若 specimen identity 保持：

$$
IF\text{-}1.
$$

若 criterion 把 phase class 當 identity：

$$
IF\text{-}4.
$$

Paper 03 已證明兩者依 $\kappa$ 分離。

---

# 61. Engineering Phase Module

power electronics / oscillator computing：

$$
PH\text{-}0/1.
$$

phase 是：

- switching phase；
- interleaving；
- resonance；
- PLL relation。

一般不需要：

$$
PH\text{-}5
$$

或 quantum phase。

---

# 62. GPC Carrier Relation Module

GPC sender–receiver relation：

$$
PH\text{-}5
\times
IF\text{-}3.
$$

receiver internal update：

$$
IF\text{-}1
$$

或 identity transition：

$$
IF\text{-}4.
$$

因此同一 GPC system 可以由多個 coupled phase modules 組成。

---

# 63. Future Legal / Economic / Social Phase

若未來定義：

- legal phase；
- economic phase；
- institutional phase；

PMC 第一個問題不是：

> 有沒有 metaphorical sense？

而是：

1. identity criterion？
2. state space？
3. phase space？
4. phase extractor？
5. observable？
6. dynamics？
7. transport？
8. IF role？
9. falsification？

若答案只是：

> 「某個東西處於某階段。」

通常只是 regime/state label，不一定需要 phase vocabulary。

---

# 64. Module Registration Record

每個 module 建議存：

```json
{
  "module_id": "IPFC-MOD-...",
  "domain": "...",
  "identity_criterion": "...",
  "phase_canon_type": "PH-k",
  "ipfc_role": ["IF-j"],
  "state_space": "...",
  "identity_projection": "...",
  "phase_space": "...",
  "phase_extractor": "...",
  "transport": "...",
  "dynamics": "...",
  "observable": "...",
  "lineage": "...",
  "physical_realization": "...",
  "assumptions": [],
  "guarantees": [],
  "falsification": []
}
```

---

# 65. Rejection Rules

module 不得進 current Canon 若：

## R1

沒有 identity criterion。

## R2

沒有 PH type。

## R3

沒有 IF role。

## R4

phase 只是 renamed scalar/state。

## R5

holonomy 沒 transport。

## R6

identity transition 被誤稱 same-identity holonomy。

## R7

PH-5 / PH-6 無 realization bridge 卻宣稱 physical。

## R8

module composition 忽略 defect / interface mismatch。

## R9

contract 沒寫真正依賴的 identity / phase / safety requirement。

## R10

沒有 falsification rule。

---

# 66. PMC 與 Applied Category Theory

Fong 的 decorated cospan framework、Baez–Courser–Vasilakopoulou 的 structured/decorated cospans等工作展示：

> 帶內部結構的 open systems 可以被放入 compositional categorical language。

PMC 與之共享：

- compositionality；
- typed interfaces；
- semantics-preserving maps；

但 PMC 不聲稱 decorated cospans 就是 IPFC Phase Modules。

未來若需要真正 open-system wiring algebra，可以把 PMC module interface 再映到成熟 cospan/double-category framework。

---

# 67. PMC 與 Assume–Guarantee Contracts

現代 contract-based design 已建立：

- assumptions；
- guarantees；
- refinement；
- composition；
- modular verification。

PMC 吸收這個工程紀律，用來回答：

> 一個 phase module 在什麼環境條件下，能保證 identity / phase / safety / observable property？

但 PMC 的 contract 欄位比一般 input-output contract 多出：

- identity；
- phase type；
- lineage；
- realization；
- falsification。

---

# 68. 為什麼 Paper 05 是 IPFC Core 的收斂點

Papers 01–04 分別建立：

$$
\boxed{
\text{identity fiber}
}
$$

$$
\boxed{
\text{semantic phase}
}
$$

$$
\boxed{
\text{phase/identity transition}
}
$$

$$
\boxed{
\text{interaction identity safety}.
}
$$

Paper 05 將它們抽象成：

$$
\boxed{
\mathfrak M
}
$$

與：

$$
\boxed{
F:
\mathfrak M_A
\rightarrow
\mathfrak M_B.
}
$$

所以之後新增 domain 不再需要改母理論。

---

# 69. IPFC Core Closure

IPFC 第一階段核心可以寫成：

$$
\boxed{
\text{Paper 01}
\rightarrow
\text{Paper 02}
\rightarrow
\text{Paper 03}
\rightarrow
\text{Paper 04}
\rightarrow
\text{Paper 05}.
}
$$

分別回答：

1. 什麼叫 identity fiber？
2. semantic phase 如何合法存在？
3. phase transition 與 identity transition 如何分開？
4. interaction 如何影響 carrier identity？
5. 所有 X-phase modules 如何組合與驗證？

---

# 70. 核心形式結果

本文新增：

1. Exact Phase Module Morphism；
2. Phase Modules Form a Category；
3. Approximate Identity Composition Bound；
4. Approximate Phase Composition Bound；
5. Approximate Dynamics Composition Bound；
6. Holonomy Conjugacy Theorem；
7. Product Fiber Theorem；
8. Phase Module Quotient Theorem；
9. Sequential Contract Composition Theorem；
10. Contract Replacement Theorem；
11. No-Type-Jump module gate。

---

# 71. 最終結論

Phase Module Calculus 的目的不是讓更多東西被叫做 phase。

恰恰相反。

它的目的是讓「phase」這個詞變得**更難合法使用**。

一個 X-phase claim 必須提供：

$$
\boxed{
\text{Identity}
+
\text{Typed Phase}
+
\text{Dynamics/Transport}
+
\text{Observable}
+
\text{Lineage}
+
\text{Realization if physical}
+
\text{Contract}
+
\text{Falsification}.
}
$$

跨 domain claim 必須提供：

$$
\boxed{
\text{Phase Module Morphism}.
}
$$

跨多 module chain 必須記：

$$
\boxed{
\text{Defect Ledger}.
}
$$

需要 coarse-graining 時，必須通過：

$$
\boxed{
\text{Fiber Factorization}.
}
$$

需要 modular verification 時，必須滿足：

$$
\boxed{
\text{Assume–Guarantee Compatibility}.
}
$$

需要 physical elevation 時，仍受：

$$
\boxed{
\text{No type jump without a map}.
}
$$

因此 IPFC / PMC 的最高版本可以濃縮為：

> **不是所有東西都是相位；但任何聲稱使用相位的跨域理論，都應該能說清楚：是哪個東西、哪種相位、如何變、怎麼傳、能測什麼、何時失敗、以及如何與其他模組組合。**

---

# 72. 後續

IPFC Core Papers 01–05 至此完成。

下一階段不再是母接口建造，而是兩條分支：

## Formalization Track

- Lean 4：IdentitySystem / PhaseModule / Morphism / Quotient / Contracts
- approximate defect lemmas
- lineage factorization automation

## Domain / Benchmark Track

- Semantic Holonomy Benchmark
- GPC Carrier Identity Benchmark
- Neural–Semantic Phase Bridge
- GIPSS/GIPE Phase Module
- Material / Regime Module
- Engineering Phase Module

Paper 06《AI Fork、忒修斯與語義分裂》可作為 Identity Lineage 的專題應用，而不再是 Core interface 的必要前置。

---

# 參考文獻

1. Neo.K & Aletheia. *IPFC Paper 01: Identity–Phase Fiber Calculus*. EveMissLab, 2026.
2. Neo.K & Aletheia. *IPFC Paper 02: Phase Semantics*. EveMissLab, 2026.
3. Neo.K & Aletheia. *IPFC Paper 03: Phase Transition and Identity Bifurcation*. EveMissLab, 2026.
4. Neo.K & Aletheia. *IPFC Paper 04: Carrier Identity in GPC*. EveMissLab, 2026.
5. Fong, B. “Decorated Cospans.” *Theory and Applications of Categories* 30, 1096–1120 (2015). arXiv:1502.00872.
6. Baez, J. C., Courser, K., & Vasilakopoulou, C. “Structured versus Decorated Cospans.” *Compositionality* 4 (2022). arXiv:2101.09363.
7. Saoud, A., Girard, A., & Fribourg, L. “Assume-guarantee contracts for continuous-time systems.” *Automatica* 134, 109910 (2021). DOI: 10.1016/j.automatica.2021.109910.
8. Incer, I. et al. “Pacti: Assume-Guarantee Contracts for Efficient Compositional Analysis and Design.” *ACM Transactions on Cyber-Physical Systems* 9(1), Article 3 (2025). DOI: 10.1145/3704736.
9. Sharf, M., Besselink, B., & Johansson, K. H. “Contract Composition for Dynamical Control Systems: Definition and Verification using Linear Programming.” arXiv:2211.01298, 2022.
10. EveMissLab. *Phase Canon v1.1*. 2026.
11. EveMissLab. *GPC-CS Papers 00–10*. 2026.
12. EveMissLab. *PCPRT Papers 01–08*. 2026.

---

**IPFC Paper 05 v1.0 — COMPLETE.**  
**IPFC Core Series Papers 01–05 — CLOSED FOR FOUNDATION PHASE.**
