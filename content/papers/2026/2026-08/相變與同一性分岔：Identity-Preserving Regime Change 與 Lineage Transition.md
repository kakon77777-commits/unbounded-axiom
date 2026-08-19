# 相變與同一性分岔：Identity-Preserving Regime Change 與 Lineage Transition
## Phase Transition and Identity Bifurcation: Identity-Preserving Regime Change and Lineage Transition

**系列**：Identity–Phase Fiber Calculus（IPFC）  
**論文**：Paper 03  
**版本**：v1.0  
**日期**：2026-08-15  
**作者**：Neo.K（許筌崴）with Aletheia  
**機構**：EveMissLab（一言諾科技有限公司），台灣  
**文件性質**：數學框架／相變—同一性橋接理論／跨域判準論文  
**上游**：
- IPFC Paper 01《同一性–相位纖維微積分》
- IPFC Paper 02《相位語義》
- EveMissLab Phase Canon v1.1
- PCPRT Papers 01–08
- GPC-CS Papers 00–10

**形式化狀態**：本文新定理為手工形式證明，尚未完成 Lean 4 / Coq 機器驗證。  
**核心警語**：

$$
\boxed{
\text{Phase transition}
\neq
\text{Identity transition}
}
$$

以及：

$$
\boxed{
\text{Identity transition is criterion-relative.}
}
$$

---

# 摘要

相位理論描述系統如何跨越 oscillator phase、regime、material phase、functional phase、semantic phase 或 generalized relational phase；同一性微積分則描述在索引、呈現與狀態變換中，何者仍被判定為「同一個對象」。兩者在最困難的邊界問題上相遇：**當 phase 或 regime 發生劇烈轉變時，改變後的系統仍是同一個嗎？**

本文建立 IPFC 中「相變與同一性分岔」的正式框架。給定 state space：

$$
\mathcal X,
$$

identity projection：

$$
q_\kappa:
\mathcal X
\twoheadrightarrow
\mathcal O_\kappa,
$$

與 phase/regime classifier：

$$
p:
\mathcal X
\rightarrow
\mathcal P,
$$

本文定義 identity fiber：

$$
F_O^\kappa
=
q_\kappa^{-1}(O),
$$

phase region：

$$
P_\alpha
=
p^{-1}(\alpha),
$$

以及 **Phase–Identity Cell**：

$$
\boxed{
C_{O,\alpha}
=
F_O^\kappa
\cap
P_\alpha.
}
$$

這個雙重分割使任一 transition：

$$
x\rightarrow x'
$$

可依：

$$
q_\kappa(x)\stackrel{?}{=}q_\kappa(x')
$$

與：

$$
p(x)\stackrel{?}{=}p(x')
$$

分成四型：intra-cell change、identity-preserving phase transition、identity transition without phase-class change、coupled phase–identity transition。

本文進一步證明 **Identity Boundary Crossing Theorem**：若 $\mathcal O_\kappa$ 為離散 identity space，且 $q_\kappa$ 在 identity singular set $B_{\mathrm{id}}$ 外連續，則任何連續 trajectory 若不穿越 $B_{\mathrm{id}}$，identity 必保持不變。相同結構對 phase classifier 給出 Phase Boundary Crossing Theorem。故 phase boundary：

$$
B_{\mathrm{ph}}
$$

與 identity boundary：

$$
B_{\mathrm{id}}
$$

是兩個不同的臨界集合；相變完全可能穿越前者而不穿越後者。

本文亦建立 **Identity-Criterion Refinement Theorem**。若細 criterion $\kappa_f$ 與粗 criterion $\kappa_c$ 滿足：

$$
q_{\kappa_c}
=
r\circ
q_{\kappa_f},
$$

則任何在細 criterion 下 identity-preserving 的 dynamics，在粗 criterion 下也必 identity-preserving；反向不成立。這正式解釋為何「水變冰」可在 specimen identity 下是同一個 specimen，卻在 phase-defined identity 下被分類為不同 phase identities；也說明 semantic sense、AI agent、software version 與 carrier identity 的結論必須明示 criterion。

本文再把 IPFC Paper 01 的 Lineage Factorization 用於 phase transition family，定義 deterministic lineage、branching lineage 與 stochastic lineage kernel；並建立 parameter-loop hysteresis 與 identity-preserving holonomy 的接口。最後，本文提出 phase boundary / identity boundary / realization boundary 三重分離，將 material phase、semantic phase、AI fork、GPC carrier update 與工程 regime transition 納入同一個 typed transition calculus。

**關鍵詞**：相變、同一性、分岔、Lineage、Phase–Identity Cell、Identity Boundary、Regime Change、Holonomy、Hysteresis、IPFC、Phase Canon

---

# 1. 問題：相變後「還是不是同一個」不是純物理問題

## 1.1 兩種分類器

對 state：

$$
x\in\mathcal X,
$$

我們同時可能問：

### Phase / regime 問題

$$
p(x)
=
\alpha.
$$

這個 state 屬於哪個 phase / regime？

### Identity 問題

$$
q_\kappa(x)
=
O.
$$

這個 state 被判成哪一個 identity？

兩個分類器的 codomain 不同：

$$
\boxed{
p:
\mathcal X
\rightarrow
\mathcal P,
}
$$

$$
\boxed{
q_\kappa:
\mathcal X
\rightarrow
\mathcal O_\kappa.
}
$$

所以一般：

$$
\boxed{
p\neq q_\kappa.
}
$$

---

# 2. Phase Classifier 不必是單一 Order Parameter

傳統相變理論常用 order parameter：

$$
m:
\mathcal X
\rightarrow
\mathcal M
$$

再由：

$$
p
=
g\circ m
$$

決定 phase。

但 IPFC 不要求所有 phase 都可由單一局部 order parameter 表示。

原因包括：

- topological transitions；
- hidden order；
- generalized order；
- multi-order-parameter systems。

因此本文把：

$$
p
$$

本身視為 primitive phase/regime classifier。

若存在 order parameter：

$$
m,
$$

則把它視為 phase classification 的一種 realization。

---

# 3. Phase Region 與 Identity Fiber

## 定義 3.1 — Phase Region

對：

$$
\alpha\in\mathcal P,
$$

定義：

$$
\boxed{
P_\alpha
=
p^{-1}(\alpha).
}
$$

---

## 定義 3.2 — Identity Fiber

對：

$$
O\in\mathcal O_\kappa,
$$

定義：

$$
\boxed{
F_O^\kappa
=
q_\kappa^{-1}(O).
}
$$

---

# 4. Phase–Identity Cell

## 定義 4.1

對：

$$
(O,\alpha)
\in
\mathcal O_\kappa
\times
\mathcal P,
$$

定義：

$$
\boxed{
C_{O,\alpha}
=
F_O^\kappa
\cap
P_\alpha.
}
$$

稱為 **Phase–Identity Cell**。

它回答：

> 哪些 states 同時被視為 identity $O$ 且處於 phase $\alpha$？

---

# 5. 四型 Transition Classification

對 transition：

$$
x
\rightarrow
x',
$$

比較：

$$
q_\kappa(x),
\qquad
q_\kappa(x'),
$$

與：

$$
p(x),
\qquad
p(x').
$$

---

## Type T00 — Intra-Cell Change

$$
q_\kappa(x')
=
q_\kappa(x),
$$

且：

$$
p(x')
=
p(x).
$$

只是同一 identity、同一 phase 內的 state change。

---

## Type T01 — Identity-Preserving Phase Transition

$$
\boxed{
q_\kappa(x')
=
q_\kappa(x),
}
$$

但：

$$
\boxed{
p(x')
\neq
p(x).
}
$$

分類：

$$
\boxed{
PH\text{-}2
\times
IF\text{-}1
}
$$

在 material/regime case。

---

## Type T10 — Identity Transition without Phase-Class Change

$$
q_\kappa(x')
\neq
q_\kappa(x),
$$

但：

$$
p(x')
=
p(x).
$$

例如：

- copy/fork identity change；
- ownership/version identity transition；
- semantic referent change；

可以在同一 phase class 內發生。

---

## Type T11 — Coupled Phase–Identity Transition

$$
\boxed{
q_\kappa(x')
\neq
q_\kappa(x),
}
$$

且：

$$
\boxed{
p(x')
\neq
p(x).
}
$$

這才是：

> phase transition 與 identity transition 同時發生。

---

# 6. Transition Classification Theorem

## 定理 6.1

對任何 transition：

$$
x\rightarrow x',
$$

若：

$$
q_\kappa
$$

與：

$$
p
$$

均為單值映射，則上述 T00、T01、T10、T11 四型恰好一型成立。

### 證明

兩個二元命題：

$$
A:
q_\kappa(x')=q_\kappa(x),
$$

$$
B:
p(x')=p(x)
$$

各有真／假兩值。

因此：

$$
(A,B)
$$

共有四種且互斥完備。 $\square$

---

# 7. 第一個重要結論

所以：

$$
\boxed{
\text{phase transition}
\not\Rightarrow
\text{identity transition}.
}
$$

同樣：

$$
\boxed{
\text{identity transition}
\not\Rightarrow
\text{phase transition}.
}
$$

兩者只有在 T11 才同時成立。

---

# 8. Identity Criterion 決定「同一個」的解析度

同一 state pair：

$$
x,x'
$$

可以在不同 identity criteria 下得到不同結論。

例如：

### Specimen criterion

$$
\kappa_{\mathrm{spec}}.
$$

追蹤的是「同一份 specimen 的持續譜系」。

### Material-phase criterion

$$
\kappa_{\mathrm{mat}}.
$$

把 phase class 納入 identity。

則 liquid / solid transition 可能：

$$
q_{\kappa_{\mathrm{spec}}}(x_{\mathrm{liq}})
=
q_{\kappa_{\mathrm{spec}}}(x_{\mathrm{sol}})
$$

但：

$$
q_{\kappa_{\mathrm{mat}}}(x_{\mathrm{liq}})
\neq
q_{\kappa_{\mathrm{mat}}}(x_{\mathrm{sol}}).
$$

這不是矛盾。

兩個 criteria 問的是不同 identity 問題。

---

# 9. Criterion Refinement

## 定義 9.1

若存在滿射或一般映射：

$$
r:
\mathcal O_{\kappa_f}
\rightarrow
\mathcal O_{\kappa_c}
$$

使：

$$
\boxed{
q_{\kappa_c}
=
r\circ
q_{\kappa_f},
}
$$

稱：

$$
\kappa_f
$$

比：

$$
\kappa_c
$$

更細。

即細 identity classes 可被合併成粗 identity classes。

---

# 10. Identity-Criterion Refinement Theorem

## 定理 10.1

若：

$$
q_{\kappa_c}
=
r q_{\kappa_f},
$$

且 dynamics：

$$
\Gamma
$$

在細 criterion 下 identity-preserving：

$$
q_{\kappa_f}\Gamma
=
q_{\kappa_f},
$$

則：

$$
\boxed{
q_{\kappa_c}\Gamma
=
q_{\kappa_c}.
}
$$

### 證明

$$
q_{\kappa_c}\Gamma
=
rq_{\kappa_f}\Gamma
=
rq_{\kappa_f}
=
q_{\kappa_c}.
\qquad\square
$$

---

# 11. 反向不成立

粗 criterion 下 identity-preserving 不推出細 criterion 下 preservation。

因為兩個不同 fine identities：

$$
O_1^{(f)},
O_2^{(f)}
$$

可能被：

$$
r
$$

合併成同一 coarse identity：

$$
O^{(c)}.
$$

所以 dynamics 可以在 fine identities 間移動，但 coarse identity 看起來沒變。

---

# 12. Finite Branch Count Corollary

假設 branch set：

$$
S
\subseteq
\mathcal X
$$

有限。

定義 identity image：

$$
I_f
=
q_{\kappa_f}(S),
$$

$$
I_c
=
q_{\kappa_c}(S).
$$

若：

$$
q_{\kappa_c}
=
rq_{\kappa_f},
$$

則：

$$
\boxed{
|I_c|
\le
|I_f|.
}
$$

### 證明

$$
I_c
=
r(I_f).
$$

任意有限集合在映射下像的基數不超過原集合。 $\square$

這說明：

> identity bifurcation count 本身也是 criterion-resolution dependent。

---

# 13. Topological Identity Boundary

現在給：

$$
\mathcal X
$$

一個拓撲。

假設 identity space：

$$
\mathcal O_\kappa
$$

為離散拓撲。

---

## 定義 13.1 — Identity Regular Domain

令：

$$
B_{\mathrm{id}}
\subseteq
\mathcal X
$$

為 identity singular / ambiguity set。

在：

$$
\mathcal X
\setminus
B_{\mathrm{id}}
$$

上要求：

$$
q_\kappa
$$

連續。

---

# 14. Identity Boundary Crossing Theorem

## 定理 14.1

令：

$$
x:
[0,1]
\rightarrow
\mathcal X
$$

為連續 trajectory。

若：

$$
x([0,1])
\cap
B_{\mathrm{id}}
=
\varnothing,
$$

則：

$$
\boxed{
q_\kappa(x(t))
}
$$

在：

$$
[0,1]
$$

上為常數。

### 證明

因：

$$
x([0,1])
\subseteq
\mathcal X\setminus B_{\mathrm{id}},
$$

且：

$$
q_\kappa
$$

在該域連續。

故：

$$
q_\kappa\circ x:
[0,1]
\rightarrow
\mathcal O_\kappa
$$

連續。

 $[0,1]$ 連通，而連續映射的像仍連通。

但離散空間中的連通子集只有單點。

所以：

$$
q_\kappa(x(t))
$$

必為常數。 $\square$

---

# 15. 推論：Continuous Identity Change Requires a Singular Set

若連續 trajectory 前後：

$$
q_\kappa(x(0))
\neq
q_\kappa(x(1)),
$$

則：

$$
\boxed{
x([0,1])
\cap
B_{\mathrm{id}}
\neq
\varnothing.
}
$$

也就是：

> 在離散 identity classification 下，identity 改變必須穿過 identity classifier 的 singular / ambiguity / boundary region。

---

# 16. Phase Boundary

同樣假設 phase class space：

$$
\mathcal P
$$

離散。

令：

$$
B_{\mathrm{ph}}
\subseteq
\mathcal X
$$

為 phase critical / classification singular set。

在：

$$
\mathcal X
\setminus
B_{\mathrm{ph}}
$$

上：

$$
p
$$

連續。

---

# 17. Phase Boundary Crossing Theorem

## 定理 17.1

若連續 trajectory：

$$
x:[0,1]\rightarrow\mathcal X
$$

滿足：

$$
p(x(0))
\neq
p(x(1)),
$$

則：

$$
\boxed{
x([0,1])
\cap
B_{\mathrm{ph}}
\neq
\varnothing.
}
$$

證明同定理 14.1。 $\square$

---

# 18. Phase Boundary 與 Identity Boundary 是不同集合

所以 state space 有至少兩種臨界集合：

$$
\boxed{
B_{\mathrm{ph}}
}
$$

與：

$$
\boxed{
B_{\mathrm{id}}.
}
$$

它們可以：

1. 不相交；
2. 部分重疊；
3. 一個包含另一個；
4. 完全重合。

不能先驗假定：

$$
B_{\mathrm{ph}}
=
B_{\mathrm{id}}.
$$

---

# 19. 四種 Boundary Crossing

連續 trajectory 可有：

### B00

不穿越任何 boundary。

### B01

穿越：

$$
B_{\mathrm{ph}}
$$

但不穿越：

$$
B_{\mathrm{id}}.
$$

即 identity-preserving phase transition。

### B10

穿越：

$$
B_{\mathrm{id}}
$$

但不穿越：

$$
B_{\mathrm{ph}}.
$$

即 identity transition without phase transition。

### B11

同時穿越兩種 boundary。

即 coupled transition。

---

# 20. Critical Point 不自動是 Identity Singularity

在 standard physical phase transition 中：

- correlation length；
- susceptibility；
- order parameter；
- free-energy derivatives；

可以在 critical point 出現特殊行為。

但這只定位：

$$
B_{\mathrm{ph}}.
$$

是否同時屬於：

$$
B_{\mathrm{id}}
$$

仍取決於：

$$
\kappa.
$$

因此：

$$
\boxed{
\text{criticality}
\neq
\text{identity breakdown automatically}.
}
$$

---

# 21. Landau-Type Order Parameter Interface

若存在 scalar/vector order parameter：

$$
m:
\mathcal X
\rightarrow
\mathcal M,
$$

phase classifier：

$$
p
=
g\circ m.
$$

則 phase transition 可由：

$$
m
$$

的：

- symmetry change；
- discontinuity；
- nonanalyticity；
- bifurcation；

偵測。

IPFC 不改寫 Landau theory。

IPFC 只增加另一條：

$$
q_\kappa:
\mathcal X
\rightarrow
\mathcal O_\kappa
$$

用來問 identity 是否也改變。

---

# 22. Beyond-Landau Guard

Phase Canon 不應要求：

> 每個 phase 一定有單一 conventional symmetry-breaking order parameter。

Kosterlitz–Thouless 型 transition 與後續 topological/quantum-order work 已提供標準反例／擴張路線。

因此 IPFC 只要求：

$$
p:
\mathcal X
\rightarrow
\mathcal P
$$

可被操作化。

 $p$ 可以依：

- order parameter；
- topological invariant；
- response property；
- spectrum；
- defect structure；
- learned classifier；

建立。

但若使用 learned classifier，phase identity 仍需外部 validation。

---

# 23. RG 不是 Identity Projection

Renormalization / coarse-graining map：

$$
C:
\mathcal X
\rightarrow
\mathcal X_{\mathrm{eff}}
$$

一般不是：

$$
q_\kappa.
$$

它回答：

> 哪些 microscopic differences 在指定 scale 下被忽略？

identity projection 則回答：

> 哪些 states 仍算同一 identity？

所以：

$$
\boxed{
C
\neq
q_\kappa
}
$$

一般成立。

---

# 24. Scale–Identity Compatibility

若 coarse identity：

$$
q_{\kappa_{\mathrm{eff}}}
:
\mathcal X_{\mathrm{eff}}
\rightarrow
\mathcal O_{\mathrm{eff}}
$$

與 microscopic identity：

$$
q_{\kappa_{\mathrm{micro}}}
$$

存在：

$$
L_C
:
\mathcal O_{\mathrm{micro}}
\rightarrow
\mathcal O_{\mathrm{eff}}
$$

使：

$$
\boxed{
q_{\kappa_{\mathrm{eff}}}C
=
L_Cq_{\kappa_{\mathrm{micro}}},
}
$$

才可說 identity 在 coarse-graining 下具有明確 lineage。

這直接沿用 IPFC Paper 01 的 Lineage Factorization。

---

# 25. RG Universality 與 Identity 不等價

兩個 microscopic systems 可以 flow 到同一 universality class：

$$
C_\infty(x_A)
\sim
C_\infty(x_B),
$$

但：

$$
q_\kappa(x_A)
\neq
q_\kappa(x_B).
$$

因此：

$$
\boxed{
\text{same universality class}
\not\Rightarrow
\text{same identity}.
}
$$

反之，同一 specimen identity 也可跨不同 physical phases。

---

# 26. Parameterized Dynamics

令 control parameter：

$$
\lambda
\in
\Lambda.
$$

dynamics family：

$$
\boxed{
\Gamma_\lambda:
\mathcal X
\rightarrow
\mathcal X.
}
$$

stable/observable state family：

$$
S_\lambda
\subseteq
\mathcal X.
$$

---

# 27. Phase Bifurcation

定義 phase image：

$$
\boxed{
\mathcal P_\lambda
=
p(S_\lambda).
}
$$

若：

$$
\lambda
$$

穿越：

$$
\lambda_c
$$

時：

- phase branch count；
- connectivity；
- stability；
- invariant structure；

發生定性改變，稱為 phase bifurcation。

---

# 28. Identity Bifurcation

定義：

$$
\boxed{
\mathcal I_{\kappa,\lambda}
=
q_\kappa(S_\lambda).
}
$$

若：

$$
\lambda
$$

穿越：

$$
\lambda_*
$$

時 $\mathcal I_{\kappa,\lambda}$ 的 branch structure 發生定性改變，稱：

$$
\boxed{
\kappa\text{-Identity Bifurcation}.
}
$$

注意：

$$
\lambda_*
$$

不必等於：

$$
\lambda_c.
$$

---

# 29. Phase Bifurcation 與 Identity Bifurcation 可分離

可能：

$$
\lambda_c
\neq
\lambda_*.
$$

甚至：

$$
\lambda_c
$$

存在而：

$$
\lambda_*
$$

不存在。

例如 phase 改變但 specimen lineage 未中斷。

反之也可有 identity fork 而 phase class 不變。

---

# 30. Criterion-Relative Bifurcation Theorem

## 命題 30.1

若：

$$
q_{\kappa_c}
=
rq_{\kappa_f},
$$

則對任一有限 branch family：

$$
S_\lambda,
$$

有：

$$
\boxed{
|
q_{\kappa_c}(S_\lambda)
|
\le
|
q_{\kappa_f}(S_\lambda)
|.
}
$$

因此細 identity criterion 可觀察到比粗 criterion 更多 identity branches。

這是第 12 節推論的 parameterized 版本。

---

# 31. Lineage Across a Transition

transition dynamics：

$$
\Gamma:
\mathcal X_-
\rightarrow
\mathcal X_+.
$$

old identity：

$$
q_-:
\mathcal X_-
\rightarrow
\mathcal O_-.
$$

new identity：

$$
q_+:
\mathcal X_+
\rightarrow
\mathcal O_+.
$$

若：

$$
q_+\Gamma
$$

在每個 old identity fiber 上為常數，則存在唯一：

$$
\boxed{
L:
\mathcal O_-
\rightarrow
\mathcal O_+
}
$$

使：

$$
q_+\Gamma
=
Lq_-.
$$

這就是 deterministic transition lineage。

---

# 32. Branching Transition

如果同一 old identity fiber：

$$
F_O
$$

中不同 states 經 transition 後進入不同 new identities，則 deterministic：

$$
L(O)
$$

不存在。

可改用 relation：

$$
\boxed{
\mathcal L
\subseteq
\mathcal O_-
\times
\mathcal O_+.
}
$$

其中：

$$
(O,O')
\in
\mathcal L
$$

表示存在：

$$
x\in F_O
$$

使：

$$
q_+(\Gamma x)=O'.
$$

---

# 33. Stochastic Lineage

若 transition 具有 noise / stochasticity：

$$
X'
\sim
K_X(\cdot\mid x),
$$

可建立 identity transition kernel：

$$
\boxed{
K_O
(
O'
\mid
O
).
}
$$

若 old identity fiber 內不同 representatives 給出不同 identity kernels，則：

$$
O
$$

本身不是充分 Markov state。

這再次是 fiber sufficiency 問題。

---

# 34. Hysteresis as IPFC Path Dependence

令控制參數沿 loop：

$$
\gamma:
\lambda_0
\rightarrow
\lambda_1
\rightarrow
\cdots
\rightarrow
\lambda_0.
$$

由 dynamics 產生 state transport：

$$
T^\mathcal X_\gamma.
$$

若：

$$
T^\mathcal X_\gamma(x_0)
\neq
x_0,
$$

即有 path residual。

---

# 35. Identity-Preserving Hysteretic Holonomy

若：

$$
\boxed{
q_\kappa
T^\mathcal X_\gamma(x_0)
=
q_\kappa(x_0),
}
$$

但：

$$
T^\mathcal X_\gamma(x_0)
\neq
x_0,
$$

則可在 IPFC transport 意義下稱：

$$
\boxed{
\text{identity-preserving hysteretic holonomy}.
}
$$

注意：

這不是自動等同於 Berry/geometric gauge holonomy。

它是 generalized path-dependent state transport。

---

# 36. Hysteresis Can Cross Phase Boundaries Yet Preserve Identity

一個 parameter loop 可能：

$$
P_{\alpha}
\rightarrow
P_{\beta}
\rightarrow
P_{\alpha}
$$

但最終：

$$
x_{\mathrm{final}}
\neq
x_{\mathrm{initial}}.
$$

若 identity 未變：

$$
q_\kappa(x_{\mathrm{final}})
=
q_\kappa(x_{\mathrm{initial}}),
$$

則是：

$$
IF\text{-}2
$$

的自然候選。

---

# 37. Identity Hysteresis

更進一步，若同一 parameter：

$$
\lambda_0
$$

下 identity classification 依歷史路徑不同：

$$
q_\kappa(x_{\lambda_0}^{\gamma_1})
\neq
q_\kappa(x_{\lambda_0}^{\gamma_2}),
$$

則 identity 本身具有 path-dependent realization。

此時需檢查：

1. $\kappa$ 是否依賴 history；
2. state space 是否漏掉 memory variable；
3. identity 是否其實應提升到 extended state：
   $$
   (x,h).
   $$

因此「identity hysteresis」通常提示 identity state specification 不充分。

---

# 38. The Extended-State Repair

若 dynamics 有 memory：

$$
x_{t+1}
$$

不能只由：

$$
x_t
$$

決定。

加入 history state：

$$
h_t.
$$

擴成：

$$
\boxed{
\tilde x_t
=
(
x_t,h_t
).
}
$$

identity projection：

$$
\tilde q_\kappa
:
\tilde{\mathcal X}
\rightarrow
\mathcal O_\kappa.
$$

phase classifier：

$$
\tilde p
:
\tilde{\mathcal X}
\rightarrow
\mathcal P.
$$

很多看似 identity inconsistency 的問題可能在 extended state 上恢復 determinism。

---

# 39. Metastability

phase transition 常伴隨 metastable states。

IPFC 中：

$$
M_\alpha
\subset
P_\alpha
$$

可表示 metastable region。

只要：

$$
M_\alpha
\subseteq
F_O^\kappa,
$$

metastability 並不威脅 identity。

所以：

$$
\boxed{
\text{metastability}
\neq
\text{identity ambiguity automatically}.
}
$$

---

# 40. Phase–Identity Compatibility Matrix

對每個 identity：

$$
O
$$

與 phase：

$$
\alpha,
$$

定義 occupancy：

$$
\boxed{
A_{O,\alpha}
=
\mathbf 1[
C_{O,\alpha}\neq\varnothing
].
}
$$

矩陣：

$$
A
=
(
A_{O,\alpha}
)
$$

回答：

> 哪些 identities 可以存在於哪些 phases？

---

# 41. Phase-Rigid Identity

若某 identity：

$$
O
$$

只對一個 phase：

$$
\alpha
$$

有：

$$
A_{O,\alpha}=1,
$$

稱：

$$
\boxed{
\text{phase-rigid identity}.
}
$$

此 criterion 下 phase change 必伴 identity change。

---

# 42. Phase-Flexible Identity

若同一：

$$
O
$$

對多個 phases：

$$
\alpha_1,\alpha_2,\ldots
$$

皆有：

$$
A_{O,\alpha_j}=1,
$$

稱：

$$
\boxed{
\text{phase-flexible identity}.
}
$$

此 criterion 允許 identity-preserving phase transition。

---

# 43. Identity-Phase Coupling Index

有限 case 下可定義：

$$
\boxed{
\chi_\kappa(O)
=
|
\{
\alpha:
C_{O,\alpha}
\neq
\varnothing
\}
|.
}
$$

若：

$$
\chi_\kappa(O)=1,
$$

phase-rigid。

若：

$$
\chi_\kappa(O)>1,
$$

phase-flexible。

這不是物理 susceptibility。

只是 identity criterion 下 phase multiplicity 的結構指標。

---

# 44. Semantic Phase Transition Example

一個 word sense：

$$
O_{\mathrm{sense}}
$$

可在不同歷史 contexts 中有 phase drift：

$$
\phi_{t_0}
\rightarrow
\phi_{t_1}
$$

但：

$$
q_{\kappa_S}(x_{t_0})
=
q_{\kappa_S}(x_{t_1}).
$$

這是 semantic IF-1。

若形成新 sense：

$$
q_{\kappa_S}(x_{t_2})
\neq
q_{\kappa_S}(x_{t_0}),
$$

進 IF-4 lineage。

所以 semantic drift vs sense split 正是本篇 transition calculus 的一個 domain instance。

---

# 45. AI Agent Update Example

AI agent：

$$
A_t
$$

經：

- model update；
- memory rewrite；
- tool change；
- policy change；

到：

$$
A_{t+1}.
$$

若 chosen agent identity criterion：

$$
\kappa_A
$$

仍判：

$$
q_{\kappa_A}(A_{t+1})
=
q_{\kappa_A}(A_t),
$$

只是 intra-identity regime change。

若 fork：

$$
A_t
\rightarrow
A_{t+1}^{(1)},
A_{t+1}^{(2)},
$$

則 deterministic single lineage 不足，應用 branching lineage relation。

---

# 46. GPC Carrier Update Example

GPC：

$$
x_B
\rightarrow
x_B'.
$$

如果：

$$
q_B(x_B')
=
q_B(x_B),
$$

是 identity-preserving carrier update。

若：

$$
q_B(x_B')
\neq
q_B(x_B),
$$

則 communication-induced identity transition。

因此安全條件可以擴成：

$$
\boxed{
\Gamma_G(\mathcal S_G)
\subseteq
\mathcal S_G
}
$$

之外，再指定：

$$
\boxed{
q_B\Gamma_G
=
q_B
}
$$

是否為某應用的必要安全 invariant。

---

# 47. Engineering Regime Example

power converter：

$$
x
$$

可以：

- phase shedding；
- mode transition；
- resonant-frequency tracking。

system identity：

$$
O_{\mathrm{converter}}
$$

通常保持。

所以：

$$
\boxed{
PH\text{-}0/1
\times
IF\text{-}1
}
$$

或 path-dependent 時：

$$
IF\text{-}2.
$$

不需要 identity transition。

---

# 48. Physical Carrier Replacement

若某 physical carrier 被完全替換：

$$
z_A
\rightarrow
z_B,
$$

effective state：

$$
x_A
\rightarrow
x_B.
$$

identity 是否保留不能只看 phase。

需要：

$$
q_\kappa(x_A)
\stackrel{?}{=}
q_\kappa(x_B).
$$

這正是忒修斯、upload、hardware migration 等問題。

---

# 49. Physical Realization Boundary

PCPRT 還有另一個 boundary：

$$
B_{\mathrm{real}}
$$

表示：

> 原 effective model / coarse-graining / realization map 不再有效的區域。

所以實際跨尺度系統可能同時有：

$$
\boxed{
B_{\mathrm{ph}},
\quad
B_{\mathrm{id}},
\quad
B_{\mathrm{real}}.
}
$$

三者不可混同。

---

# 50. 三重 Boundary 的意義

### Phase boundary

phase/regime classifier 改變。

### Identity boundary

identity classifier 無法持續或 class 改變。

### Realization boundary

原 effective-to-physical map：

$$
\Pi
$$

失效或需要更換。

所以：

$$
\boxed{
\text{phase model breakdown}
\neq
\text{identity breakdown}
\neq
\text{physical existence breakdown}.
}
$$

---

# 51. Phase Canon 的角色

Phase Canon 決定：

$$
p
$$

所對應的 phase 是：

- PH-0；
- PH-1；
- PH-2；
- PH-3；
- PH-4；
- PH-5；
- PH-6。

IPFC Paper 03 再問：

> phase-class transition 是否跨 identity fiber？

所以：

$$
\boxed{
PH\text{-}k
\times
IF\text{-}1
}
$$

與：

$$
\boxed{
PH\text{-}k
\times
IF\text{-}4
}
$$

是兩個不同 claims。

---

# 52. 相變沒有普遍的 Identity Consequence

本文因此拒絕：

$$
\boxed{
\text{所有 phase transition 都是 identity death/rebirth}.
}
$$

也拒絕：

$$
\boxed{
\text{所有 phase transition 都只是 presentation change}.
}
$$

正確形式是：

$$
\boxed{
\text{identity consequence}
=
\text{function of }
(
\kappa,
q_\kappa,
\Gamma,
p
).
}
$$

---

# 53. Formal Failure Conditions

## F1 — Criterion Omitted

若討論「還是不是同一個」卻沒有 $\kappa$：

結論不完整。

## F2 — Phase Classifier Omitted

若聲稱相變卻沒有：

$$
p
$$

或合法 phase observable：

結論不完整。

## F3 — Boundary Conflation

把：

$$
B_{\mathrm{ph}}
$$

直接當：

$$
B_{\mathrm{id}}
$$

拒絕。

## F4 — Order Parameter Universalization

沒有 order parameter 的 phase 不能因此被排除。

## F5 — Lineage Forced Deterministic

若 old identity fiber 對 downstream identity 非常數：

不得建立單值 $L$。

## F6 — Coarse Criterion Conceals Split

粗 identity preservation 不能被當作細 identity preservation 的證明。

## F7 — Hysteresis Called Holonomy without Transport

沒有 composable path transport：

不得使用 IPFC holonomy 名稱。

---

# 54. Theorem-Level Summary

本文的主要形式結果：

1. Transition Classification Theorem；
2. Identity-Criterion Refinement Theorem；
3. finite branch count monotonicity；
4. Identity Boundary Crossing Theorem；
5. Phase Boundary Crossing Theorem；
6. criterion-relative bifurcation monotonicity；
7. deterministic lineage factorization specialization；
8. hysteretic identity-preserving holonomy interface。

---

# 55. 與標準 phase-transition theory 的關係

## 55.1 Wilson / Fisher

Renormalization-group theory 提供 critical phenomena 與 universality 的成熟框架。

IPFC 不改寫 RG。

IPFC 只增加：

> universality-class relation 不等於 identity relation。

## 55.2 Hohenberg–Halperin

dynamic critical phenomena 顯示 phase transition 的 dynamics、conservation laws 與 slow modes 需要專門分類。

IPFC 不用 identity criterion 取代 dynamic universality class。

兩者分工不同。

## 55.3 Kosterlitz–Thouless

KT transition 是不應把「phase transition」限制成 ordinary local symmetry-breaking order parameter 的經典提醒。

## 55.4 Wen / Quantum Order

quantum order / spin-liquid work 進一步強化：

> phase classification 可以超出 Landau symmetry-breaking order parameter。

因此本文把：

$$
p
$$

保留為一般 typed phase classifier。

---

# 56. 可實驗／可工程 Benchmark

## B1 — Material specimen

同 specimen 多次熱循環：

$$
\alpha
\rightarrow
\beta
\rightarrow
\alpha.
$$

測：

- phase class；
- specimen identity；
- hysteresis residual；
- realization map stability。

## B2 — Semantic sense

測 semantic drift vs identity split。

## B3 — AI fork

測 model/memory update 與 branch lineage。

## B4 — GPC carrier

測 communication-induced state change 是否保持 carrier identity。

## B5 — Software / content-addressed identity

比較：

- process identity；
- version identity；
- content-hash identity；

在同一 update 下的不同 transition classification。

---

# 57. Transition Record

每個實驗 transition 建議記錄：

```json
{
  "identity_criterion": "...",
  "phase_type": "PH-k",
  "ipfc_role_before": "IF-j",
  "state_before": "...",
  "state_after": "...",
  "identity_before": "...",
  "identity_after": "...",
  "phase_before": "...",
  "phase_after": "...",
  "crossed_phase_boundary": true,
  "crossed_identity_boundary": false,
  "crossed_realization_boundary": false,
  "lineage_type": "identity-preserving",
  "path_id": "..."
}
```

實際 numeric / identity values 必須來自 experiment or benchmark，不得人工杜撰。

---

# 58. 與下一批「XX 相位」的通用接點

任何 future module：

$$
\mathfrak M_X
$$

現在除 PAC 外，還要提供 transition specification：

$$
\boxed{
(
p_X,
q_{\kappa_X},
B_{\mathrm{ph},X},
B_{\mathrm{id},X},
L_X
).
}
$$

這使：

- 認知相位；
- 經濟 regime phase；
- 法律 phase；
- AI phase；
- biological phase；

都可以問同一個問題：

> phase boundary 和 identity boundary 到底是否同一條？

---

# 59. 最重要的新視角

以前相變常被敘述成：

> 系統變成另一個相。

IPFC 再補一句：

> **但「另一個相」不自動等於「另一個它」。**

反過來：

> **「另一個它」也不需要另一個相。**

因此 state transition 必須同時經過兩個判定器：

$$
\boxed{
p
}
$$

與：

$$
\boxed{
q_\kappa.
}
$$

---

# 60. 結論

本文建立 IPFC 中 phase transition 與 identity transition 的正式分離。

核心 state space 被雙重分割：

$$
\boxed{
C_{O,\alpha}
=
q_\kappa^{-1}(O)
\cap
p^{-1}(\alpha).
}
$$

phase transition 問：

$$
p(x)\neq p(x').
$$

identity transition 問：

$$
q_\kappa(x)\neq q_\kappa(x').
$$

兩者是正交判定。

對連續 trajectory，identity change 必須穿越：

$$
B_{\mathrm{id}},
$$

phase-class change 必須穿越：

$$
B_{\mathrm{ph}},
$$

但：

$$
\boxed{
B_{\mathrm{id}}
\neq
B_{\mathrm{ph}}
}
$$

一般成立。

不同 identity criterion 又形成 refinement lattice：

$$
q_{\kappa_c}
=
rq_{\kappa_f},
$$

使 identity preservation 具有單向 monotonicity：

$$
\boxed{
\text{fine preservation}
\Rightarrow
\text{coarse preservation},
}
$$

但反向不成立。

最後，當 transition 真正跨 identity fiber 時，IPFC 不再用「phase change」遮蔽它，而要求：

$$
\boxed{
\text{Lineage}.
}
$$

因此本文的最短版本是：

> **相位回答「系統處在哪個 regime」；同一性回答「這還是不是同一個它」；分岔回答「有多少可能的它」；譜系回答「這些它從哪裡來」。**

這使 Phase Canon、IPFC、PCPRT、GPC-CS 與 Semantic Phase 第一次具有共同 transition grammar。

---

# 61. 後續

## IPFC Paper 04
**《GPC 中的載體同一性：跨載體交流、Receiver Update 與 Identity Safety》**

## IPFC Paper 05
**《Phase Module Calculus：XX 相位的通用接駁、組合與反證規格》**

## IPFC Paper 06
**《AI Fork、忒修斯與語義分裂：Identity Lineage 的計算模型》**

---

# 參考文獻

1. Neo.K & Aletheia. *同一性–相位纖維微積分：從身份投影、索引 Holonomy 到相位動力學的統一接口*. IPFC Paper 01, EveMissLab, 2026.
2. Neo.K & Aletheia. *相位語義：語義身份、關係座標、Context Transport 與 Semantic Holonomy*. IPFC Paper 02, EveMissLab, 2026.
3. Wilson, K. G. & Fisher, M. E. “Critical Exponents in 3.99 Dimensions.” *Physical Review Letters* 28, 240 (1972). DOI: 10.1103/PhysRevLett.28.240.
4. Wilson, K. G. “Renormalization Group and Critical Phenomena. II. Phase-Space Cell Analysis of Critical Behavior.” *Physical Review B* 4, 3184 (1971). DOI: 10.1103/PhysRevB.4.3184.
5. Hohenberg, P. C. & Halperin, B. I. “Theory of Dynamic Critical Phenomena.” *Reviews of Modern Physics* 49, 435 (1977). DOI: 10.1103/RevModPhys.49.435.
6. Kosterlitz, J. M. & Thouless, D. J. “Ordering, Metastability and Phase Transitions in Two-Dimensional Systems.” *Journal of Physics C: Solid State Physics* 6, 1181 (1973). DOI: 10.1088/0022-3719/6/7/010.
7. Wen, X.-G. “Quantum Orders and Symmetric Spin Liquids.” *Physical Review B* 65, 165113 (2002). DOI: 10.1103/PhysRevB.65.165113.
8. EveMissLab. *Phase Canon v1.1*. 2026.
9. EveMissLab. *PCPRT Papers 01–08*. 2026.
10. EveMissLab. *GPC-CS Papers 00–10*. 2026.

---

**IPFC Paper 03 v1.0 — COMPLETE.**
