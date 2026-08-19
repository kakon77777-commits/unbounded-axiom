# 同一性–相位纖維微積分
## Identity–Phase Fiber Calculus (IPFC)
### 從身份投影、索引 Holonomy 到相位動力學的統一接口

**版本：** v0.1 Foundation Draft  
**日期：** 2026-08-14  
**定位：** EveMissLab《同一性–索引拓樸微積分》與 Phase Canon v1.1 的橋接母理論  
**上游：**
- 《同一性微積分：拓樸微積分的本體論基礎 v0.2》
- 《參照語義微積分：拓樸微積分的計算機實現 v0.2》
- 《索引幾何學 v0.1》
- EveMissLab Phase Canon v1.1
- GPC-CS
- PCPRT

**核心禁則：**
$$
\boxed{
\text{Identity}\neq\text{Phase}.
}
$$

**核心接口：**
$$
\boxed{
\text{Identity defines fibers; phase describes typed relations, states, and transports over or between those fibers.}
}
$$

---

# 0. 為什麼需要 IPFC

同一性微積分與相位理論回答不同問題。

同一性微積分問：

> 經過索引、投影、視角與呈現變換後，什麼仍被判定為同一個對象？

相位理論問：

> 在同一載體或不同載體之上，狀態、關係、同步、路由、區制與閉路傳輸如何變化？

因此不能寫：

$$
\text{Identity}
=
\text{Phase}.
$$

也不能寫：

$$
\text{all phase changes are merely index changes}.
$$

IPFC 的任務，是提供一張明確的 map，使：

- 純索引/gauge phase；
- 真正 state-bearing physical phase；
- generalized semantic phase；
- inter-carrier relational phase；
- identity-changing transition；

不再混為一談。

---

# 1. 三層基本空間

## 1.1 身份空間

給定 identity criterion：

$$
\kappa,
$$

定義身份類空間：

$$
\boxed{
\mathcal O_\kappa.
}
$$

$\kappa$ 可以是：

- 抽象同一性；
- 內容身份；
- carrier identity；
- semantic sense identity；
- specimen identity；
- task-relative operational identity。

在應用域中，不預設只有一個形上學上唯一的 identity criterion。

---

## 1.2 狀態空間

真正發生動力學的 effective/carrier state：

$$
\boxed{
x\in\mathcal X.
}
$$

身份投影：

$$
\boxed{
q_\kappa:
\mathcal X
\rightarrow
\mathcal O_\kappa.
}
$$

對：

$$
O\in\mathcal O_\kappa,
$$

定義身份纖維：

$$
\boxed{
F_O^\kappa
=
q_\kappa^{-1}(O).
}
$$

它包含所有依 $\kappa$ 判準仍被視為「同一個 $O$」的 states。

此處只需要投影/滿射即可談 fiber。

若還具有局部平凡化等標準 bundle 結構，才進一步稱 fiber bundle。

---

## 1.3 索引／呈現空間

索引幾何：

$$
\mathbb I
=
(
I,\tau,\delta_I,\mathcal P,\mathcal Q,
\{\Pi_\lambda\},
\sim_I,\omega,\mathcal G
).
$$

視圖總空間：

$$
\mathcal V.
$$

一個 view：

$$
V_O(i,q)
=
(
h_O,
i,
\pi_i,
q,
q(\pi_i(O))
).
$$

定義 view resolution：

$$
\boxed{
\rho:
\mathcal V
\rightarrow
\mathcal X.
}
$$

與 view identity anchor：

$$
\boxed{
h:
\mathcal V
\rightarrow
\mathcal O_\kappa.
}
$$

要求基本交換條件：

$$
\boxed{
q_\kappa\circ\rho
=
h.
}
$$

這是 IPFC 的第一個母圖。

---

# 2. Identity–State Commutative Square

$$
\boxed{
\begin{array}{ccc}
\mathcal V
&
\xrightarrow{\rho}
&
\mathcal X
\\
\downarrow h
&&
\downarrow q_\kappa
\\
\mathcal O_\kappa
&
=
&
\mathcal O_\kappa
\end{array}
}
$$

意義：

- view 可以變；
- state 可以變；
- identity 由明確投影判定；
- view identity 與 resolved-state identity 必須一致。

同一性微積分的：

$$
\int_H
$$

作用在身份一致的 views 上：

$$
\boxed{
\int_H\mathcal V_O
=
O.
}
$$

IPFC 不把這個 $\int_H$ 當 phase integration。

它只負責身份回收／身份解引用。

---

# 3. Phase 不是 Identity 的另一個名字

對 state space 定義 phase extractor：

$$
\boxed{
\Theta:
\mathcal X\times\mathcal C
\rightarrow
\Phi.
}
$$

其中：

- $\mathcal C$：context/reference/task/receiver 等條件；
- $\Phi$：typed phase space。

所以一個 state 同時有兩個不同 projection：

$$
\boxed{
x
\mapsto
q_\kappa(x)
=
O
}
$$

與：

$$
\boxed{
x
\mapsto
\Theta(x;c)
=
\phi.
}
$$

因此：

$$
\boxed{
\text{same identity}
\not\Rightarrow
\text{same phase}.
}
$$

以及：

$$
\boxed{
\text{similar phase}
\not\Rightarrow
\text{same identity}.
}
$$

---

# 4. Physical Realization Tower

若系統有 physical substrate：

$$
z\in\mathcal Z_{\mathrm{phys}},
$$

PCPRT realization map：

$$
\boxed{
\Pi:
\mathcal Z_{\mathrm{phys}}
\rightarrow
\mathcal X.
}
$$

因此完整 tower：

$$
\boxed{
\mathcal Z_{\mathrm{phys}}
\xrightarrow{\Pi}
\mathcal X
\xrightarrow{q_\kappa}
\mathcal O_\kappa
}
$$

並同時：

$$
\boxed{
\mathcal X
\xrightarrow{\Theta}
\Phi.
}
$$

即：

$$
\boxed{
\begin{array}{ccccc}
&&\mathcal X&&\\
&\nearrow\Pi&&\searrow\Theta&\\
\mathcal Z_{\mathrm{phys}}
&&&&
\Phi\\
& &\downarrow q_\kappa&&\\
&&\mathcal O_\kappa&&
\end{array}
}
$$

這裡：

- $\Pi$ 回答「什麼物理狀態實現這個 effective state？」；
- $q_\kappa$ 回答「這個 state 算是哪個同一性對象？」；
- $\Theta$ 回答「這個 state 位於什麼 phase / relation / regime？」

三者不能互相替代。

---

# 5. Identity-Preserving Dynamics

state dynamics：

$$
\boxed{
\Gamma:
\mathcal X
\rightarrow
\mathcal X.
}
$$

## 定義 5.1 — 身份保持

若：

$$
\boxed{
q_\kappa\circ\Gamma
=
q_\kappa,
}
$$

稱 $\Gamma$ 對 criterion $\kappa$ 身份保持。

---

## 定理 5.2 — Fiber Endomorphism Theorem

若：

$$
q_\kappa\Gamma=q_\kappa,
$$

則對所有：

$$
O\in\mathcal O_\kappa,
$$

有：

$$
\boxed{
\Gamma(F_O^\kappa)
\subseteq
F_O^\kappa.
}
$$

### 證明

取：

$$
x\in F_O^\kappa.
$$

則：

$$
q_\kappa(x)=O.
$$

由身份保持：

$$
q_\kappa(\Gamma(x))
=
q_\kappa(x)
=
O.
$$

故：

$$
\Gamma(x)\in F_O^\kappa.
\qquad\square
$$

因此「同一個東西在變」的數學意思就是：

> dynamics 作用於同一 identity fiber 內部。

---

# 6. Identity Transition 與 Lineage

若：

$$
q_\kappa\Gamma
\neq
q_\kappa,
$$

不能硬稱同一性守恆。

引入 lineage map：

$$
\boxed{
L:
\mathcal O_\kappa
\rightarrow
\mathcal O_\kappa'
}
$$

滿足：

$$
\boxed{
q_{\kappa'}\circ\Gamma
=
L\circ q_\kappa.
}
$$

若：

$$
L=\operatorname{id},
$$

是 identity-preserving dynamics。

若：

$$
L\neq\operatorname{id},
$$

則是：

$$
\boxed{
\text{Identity-Lineage Transition}.
}
$$

這是：

- semantic sense split；
- fork / copy lineage；
- carrier replacement；
- specimen-to-product identity change；
- certain identity criteria 下的 phase transition；

的共同接口。

---

# 7. Index Transport

給定索引／context path：

$$
\gamma:
i_0
\rightarrow
i_1
\rightarrow
\cdots
\rightarrow
i_n.
$$

視圖 transport：

$$
\boxed{
T^\mathcal V_\gamma:
\mathcal V_{i_0}
\rightarrow
\mathcal V_{i_n}.
}
$$

state transport：

$$
\boxed{
T^\mathcal X_\gamma:
\mathcal X_{i_0}
\rightarrow
\mathcal X_{i_n}.
}
$$

理想 compatibility：

$$
\boxed{
\rho\circ T^\mathcal V_\gamma
=
T^\mathcal X_\gamma\circ\rho.
}
$$

若只近似成立，定義 transport-resolution defect：

$$
\boxed{
\varepsilon_{\rho,\gamma}
=
d_\mathcal X
\left(
\rho T^\mathcal V_\gamma(V),
T^\mathcal X_\gamma\rho(V)
\right).
}
$$

---

# 8. Identity-Preserving Transport

若：

$$
\boxed{
q_\kappa T^\mathcal X_\gamma
=
q_\kappa,
}
$$

則 transport 在 identity fiber 內移動。

這代表：

> 觀看方式、context、representation 或 state relation 改變，但仍被判定為同一身份。

---

# 9. Phase Transport

phase space：

$$
\Phi
$$

上的 transport：

$$
\boxed{
T^\Phi_\gamma:
\Phi_{i_0}
\rightarrow
\Phi_{i_n}.
}
$$

理想相容：

$$
\boxed{
\Theta
\circ
T^\mathcal X_\gamma
=
T^\Phi_\gamma
\circ
\Theta.
}
$$

若不精確：

$$
\boxed{
\varepsilon_{\Phi,\gamma}
=
d_\Phi
\left(
\Theta T^\mathcal X_\gamma(x),
T^\Phi_\gamma\Theta(x)
\right).
}
$$

這是未來：

- semantic transport；
- neural phase transport；
- cross-model alignment；
- time-phase transport；

都可以共用的誤差形式。

---

# 10. Holonomy 是第一個真正的焊點

若：

$$
\gamma
$$

是閉路：

$$
i_n=i_0,
$$

則：

$$
\boxed{
\operatorname{Hol}^\mathcal X_\gamma
=
T^\mathcal X_\gamma.
}
$$

若：

$$
\operatorname{Hol}^\mathcal X_\gamma
\neq
\operatorname{id}
$$

但：

$$
\boxed{
q_\kappa
\operatorname{Hol}^\mathcal X_\gamma
=
q_\kappa,
}
$$

則：

> 繞索引／context 空間一圈後 state 沒完全回原狀，但 identity 沒變。

這就是 IPFC 的核心情況。

---

# 11. U(1) 特例：真正的幾何相位

若 phase fiber 是：

$$
U(1),
$$

且閉路 transport：

$$
\boxed{
T^\Phi_\gamma(\phi)
=
e^{i\Phi_\gamma}\phi,
}
$$

則：

$$
\boxed{
e^{i\Phi_\gamma}
}
$$

是 holonomy phase factor。

這與 geometric phase / Berry–Simon 型 fiber-bundle holonomy 有直接標準數學對應。

但 IPFC 不把所有 generalized phase 都宣稱成 $U(1)$。

---

# 12. 非阿貝爾與廣義 Holonomy

phase fiber 不必是一維圓。

若 structure group：

$$
G
$$

是非交換群，

閉路可得到：

$$
\boxed{
\operatorname{Hol}_\gamma
\in
G.
}
$$

因此：

$$
\operatorname{Hol}_{\gamma_1}
\operatorname{Hol}_{\gamma_2}
\neq
\operatorname{Hol}_{\gamma_2}
\operatorname{Hol}_{\gamma_1}
$$

可能成立。

這提供一個重要數學先例：

> holonomy 不必永遠縮成一個 scalar angle。

但語義／AI 使用此結構時，仍需自己證明合法的 group/action/transport；不能因物理中存在 non-Abelian holonomy 就自動量子化語義。

---

# 13. IF-0～IF-4：相位相對同一性的角色分型

這是 IPFC 新增、與 Phase Canon PH-0～PH-6 正交的第二軸。

---

## IF-0 — Presentation / Gauge Phase

phase 只改變 view/index representation。

形式：

$$
\boxed{
\rho T^\mathcal V_\gamma
=
\rho.
}
$$

因此 resolved state 不變。

這是：

> 純呈現相位／gauge-like phase。

Identity 也當然不變。

---

## IF-1 — Intra-Identity State Phase

state 真變：

$$
T^\mathcal X(x)\neq x,
$$

但：

$$
\boxed{
q_\kappa T^\mathcal X(x)
=
q_\kappa(x).
}
$$

典型：

- oscillator phase；
- neural phase；
- carrier regime state；
- 同一 semantic identity 中的 context-dependent semantic phase。

---

## IF-2 — Holonomic / Path Phase

phase/state 對 path 有記憶。

閉路：

$$
\gamma
$$

後：

$$
\boxed{
T_\gamma x\neq x
}
$$

但：

$$
\boxed{
q_\kappa(T_\gamma x)
=
q_\kappa(x).
}
$$

這是：

> 還是同一個它，但走一圈後不完全一樣。

---

## IF-3 — Inter-Identity Relational Phase

phase 是兩個不同 identity fibers 之間的 relation：

$$
\boxed{
\Delta_\Phi
(
x_A,
x_B
\mid
T,C
).
}
$$

這不要求：

$$
q(x_A)=q(x_B).
$$

典型：

- semantic similarity/alignment；
- GIPSS candidate-target discrepancy；
- GPC sender–receiver relation；
- inter-agent alignment。

---

## IF-4 — Identity-Lineage Transition Phase

phase / regime dynamics 伴隨 identity projection 改變：

$$
\boxed{
q_{\kappa'}\Gamma
=
Lq_\kappa,
\qquad
L\neq\operatorname{id}.
}
$$

典型：

- semantic sense split；
- fork lineage；
- identity criterion 下的 regime-to-new-identity transition。

這不是 identity-preserving holonomy。

---

# 14. PH × IF 雙重分型

Phase Canon 回答：

> phase 是什麼數學／功能型？

IPFC 回答：

> phase 相對 identity 扮演什麼角色？

因此一個 phase module 應同時標：

$$
\boxed{
\mathrm{Type}
=
PH\text{-}k
\times
IF\text{-}j.
}
$$

例如：

### 物理 oscillator

$$
PH\text{-}0
\times
IF\text{-}1.
$$

### geometric phase

$$
PH\text{-}0/1
\times
IF\text{-}2.
$$

### semantic context drift

$$
PH\text{-}5
\times
IF\text{-}1/2.
$$

### candidate-target search phase

$$
PH\text{-}6
\times
IF\text{-}3.
$$

### material phase transition

若 specimen identity 保持：

$$
PH\text{-}2
\times
IF\text{-}1.
$$

若 identity criterion 把兩相視為不同 identity：

$$
PH\text{-}2
\times
IF\text{-}4.
$$

所以 identity criterion：

$$
\kappa
$$

必須明示。

---

# 15. 相位語義的 canonical 接口

語義身份空間：

$$
\mathcal O_{\mathrm{sem},\kappa}.
$$

語義 state：

$$
x
\in
\mathcal X_{\mathrm{sem}}.
$$

identity projection：

$$
\boxed{
q_{\mathrm{sem},\kappa}
:
\mathcal X_{\mathrm{sem}}
\rightarrow
\mathcal O_{\mathrm{sem},\kappa}.
}
$$

context / receiver / reference / task：

$$
c,b,r,T.
$$

Relational Semantic Phase：

$$
\boxed{
\Theta_{\mathrm{sem},T}
(
x;c,b,r
)
\in
\Phi_{\mathrm{sem},T}.
}
$$

這是：

$$
PH\text{-}5.
$$

---

# 16. Same Semantic Identity, Different Semantic Phase

若：

$$
q_{\mathrm{sem}}(x_1)
=
q_{\mathrm{sem}}(x_2)
=
O,
$$

但：

$$
\Theta_{\mathrm{sem}}(x_1;c_1)
\neq
\Theta_{\mathrm{sem}}(x_2;c_2),
$$

則：

$$
\boxed{
\text{same semantic identity}
\not\Rightarrow
\text{same semantic phase}.
}
$$

這是：

$$
PH\text{-}5
\times
IF\text{-}1.
$$

---

# 17. Semantic Holonomy

context path：

$$
\gamma:
c_0
\rightarrow
c_1
\rightarrow
\cdots
\rightarrow
c_n=c_0.
$$

若：

$$
q_{\mathrm{sem}}
T^\mathcal X_\gamma(x)
=
q_{\mathrm{sem}}(x),
$$

但：

$$
T^\mathcal X_\gamma(x)
\neq
x,
$$

則存在：

$$
\boxed{
\text{semantic holonomy}.
}
$$

phase form：

$$
\boxed{
\operatorname{Hol}^{\mathrm{sem}}_\gamma
:
\Phi_{\mathrm{sem}}
\rightarrow
\Phi_{\mathrm{sem}}.
}
$$

此時分類：

$$
\boxed{
PH\text{-}5
\times
IF\text{-}2.
}
$$

這可以描述：

- 歷史語境一圈後的語義殘差；
- 翻譯→再翻譯→回原語言後的 meaning drift；
- agent A→B→C→A 的 alignment loop defect；
- ontology/schema migration round-trip defect。

---

# 18. Semantic Identity Split

如果 context/dynamics 後：

$$
q_{\mathrm{sem},\kappa'}
(
\Gamma(x)
)
\neq
q_{\mathrm{sem},\kappa}(x),
$$

則不叫 semantic holonomy。

它是：

$$
\boxed{
\text{semantic identity-lineage transition}.
}
$$

例如：

- 一個詞長期演化出全新 sense；
- 同一舊概念分裂成兩個技術術語；
- ontology version 中原 entity 被拆成兩個 identity classes。

分類：

$$
PH\text{-}5
\times
IF\text{-}4.
$$

---

# 19. GPC 的 IPFC 版本

sender carrier：

$$
x_A.
$$

receiver carrier：

$$
x_B.
$$

GPC update：

$$
x_B'
=
F_B
\left(
x_B,
D_B(
T_{AB}(
E_A(x_A)
),
x_B
)
\right).
$$

IPFC 加兩個 identity projections：

$$
q_A(x_A)=O_A,
$$

$$
q_B(x_B)=O_B.
$$

通信一般是：

$$
IF\text{-}3
$$

因為 sender / receiver 是不同 identity fibers。

但 receiver update 可再問：

$$
q_B(x_B')
\stackrel{?}{=}
q_B(x_B).
$$

若相等：

> communication 改變 receiver state，但 carrier identity 保留。

若不等：

> communication 觸發 identity-lineage transition。

這正好接 GPC-CS 的 carrier safety / identity risk。

---

# 20. Pure Gauge vs Functional Phase

對 task observable：

$$
H_T:
\mathcal X
\rightarrow
\mathcal Y_T.
$$

phase transformation：

$$
g:
\mathcal X
\rightarrow
\mathcal X.
$$

## Pure Gauge / Presentation Phase

若：

$$
\boxed{
H_T(gx)
=
H_T(x)
\quad
\forall x,
}
$$

且 identity 保留，phase 對 task 不可觀測。

## Functional Phase

若存在：

$$
x
$$

使：

$$
\boxed{
H_T(gx)
\neq
H_T(x),
}
$$

phase 對 task 具有功能效應。

因此：

$$
\boxed{
\text{phase label}
\neq
\text{functional phase}.
}
$$

這與 Phase Canon 的 ablation rule 一致。

---

# 21. Identity Defect

在實際 system 中，identity 判定可能不是絕對。

定義 identity defect：

$$
\boxed{
\varepsilon_{\mathrm{id}}
(
x,x'
)
=
d_{\mathcal O}
(
q_\kappa(x),
q_\kappa(x')
).
}
$$

若 $\mathcal O$ 是離散 identity class，可簡化：

$$
\varepsilon_{\mathrm{id}}
=
\mathbf 1[
q_\kappa(x)\neq q_\kappa(x')
].
$$

若 identity 是 graded/operational，可使用 calibrated identity distance。

---

# 22. Holonomy Defect

對 closed loop：

$$
\gamma,
$$

定義：

$$
\boxed{
\mathfrak C_\gamma(x)
=
\Delta_X
(
x,
T_\gamma x
).
}
$$

identity-preserving holonomy 要求：

$$
q_\kappa(T_\gamma x)
=
q_\kappa(x).
$$

若：

$$
\mathfrak C_\gamma=0,
$$

transport 對此 state 閉合。

若：

$$
\mathfrak C_\gamma>0,
$$

存在 nontrivial holonomy / loop defect。

---

# 23. Phase Attachment Contract (PAC)

未來任何：

- 相位語義；
- 語義相位；
- 認知相位；
- 時間相位；
- AI phase；
- 法律相位；
- 經濟相位；
- 工程相位；

若要進 EveMissLab Canon，必填以下 contract。

$$
\boxed{
\mathfrak M_D
=
(
D,
\kappa,
\mathcal X,
q_\kappa,
I,
\rho,
PH,
IF,
\Phi,
\Theta,
T,
\Gamma,
H,
L,
\Pi,
\varepsilon,
\mathcal F
).
}
$$

其中：

- $D$：domain；
- $\kappa$：identity criterion；
- $\mathcal X$：state space；
- $q_\kappa$：identity projection；
- $I$：index/context；
- $\rho$：view resolution；
- $PH$：Phase Canon type；
- $IF$：IPFC role type；
- $\Phi$：phase space；
- $\Theta$：phase extractor；
- $T$：transport；
- $\Gamma$：dynamics；
- $H$：observable/task；
- $L$：lineage map；
- $\Pi$：physical realization map（若有）；
- $\varepsilon$：defect family；
- $\mathcal F$：falsification rule。

---

# 24. PAC 的拒絕規則

下列任何一項成立，phase module 不得進 current Canon。

## Reject 1 — 沒有 identity criterion

不知道「同一個誰／什麼」在變。

## Reject 2 — 沒有 phase type

只寫「phase」而不標 PH-0…PH-6。

## Reject 3 — 沒有 IF role

不知道 phase 是 index、state、holonomy、inter-identity relation 還是 identity transition。

## Reject 4 — Renaming only

把普通 state 改名成 phase，沒有新 relation/dynamics/observable。

## Reject 5 — Physical type jump

PH-5/PH-6 沒有 $\Pi$ 卻宣稱 PH-0。

## Reject 6 — Holonomy without transport

只說「走一圈產生 phase」但沒定義 transport / loop。

## Reject 7 — Identity transition mislabeled as holonomy

如果：

$$
q(T_\gamma x)\neq q(x),
$$

不能叫 same-identity holonomy。

應改用 lineage。

---

# 25. Phase Module Morphism

兩個 phase modules：

$$
\mathfrak M_A,
\qquad
\mathfrak M_B.
$$

若存在 state map：

$$
F_X:
\mathcal X_A
\rightarrow
\mathcal X_B
$$

與 identity map：

$$
F_O:
\mathcal O_A
\rightarrow
\mathcal O_B
$$

使：

$$
\boxed{
q_BF_X
=
F_Oq_A,
}
$$

再有 phase map：

$$
F_\Phi:
\Phi_A
\rightarrow
\Phi_B
$$

使：

$$
\boxed{
\Theta_BF_X
\approx
F_\Phi\Theta_A,
}
$$

則稱：

$$
\boxed{
F
:
\mathfrak M_A
\rightarrow
\mathfrak M_B
}
$$

為 phase-module morphism。

這是未來「XX phase」互相接駁的正式接口。

---

# 26. Phase Module Composition

若：

$$
\mathfrak M_A
\xrightarrow{F}
\mathfrak M_B
\xrightarrow{G}
\mathfrak M_C
$$

且 identity / phase diagrams 均交換或具有受控 defect，

則：

$$
\boxed{
G\circ F
:
\mathfrak M_A
\rightarrow
\mathfrak M_C.
}
$$

總 defect 可按 downstream sensitivity 累積，直接接 PCPRT Paper 08 的 approximate composition philosophy。

---

# 27. Semantic Phase × GPC × Identity Calculus

語義 bridge 可寫成：

$$
\boxed{
\mathcal V_{\mathrm{sem}}
\xrightarrow{\rho}
\mathcal X_{\mathrm{sem}}
\xrightarrow{\Theta_{\mathrm{sem}}}
\Phi_{\mathrm{sem}}
}
$$

同時：

$$
\boxed{
\mathcal X_{\mathrm{sem}}
\xrightarrow{q_{\mathrm{sem}}}
\mathcal O_{\mathrm{sem}}.
}
$$

GPC transmission：

$$
\boxed{
\mathcal X_{\mathrm{sem},A}
\rightarrow
\mathcal X_{\mathrm{sem},B}'.
}
$$

於是可以分開問：

1. identity 是否對應？
2. semantic phase 是否對齊？
3. receiver reconstruction 是否成功？
4. carrier identity 是否保持？
5. loop transport 是否有 semantic holonomy？

以前被擠在一個「語義相位」裡的五件事，現在被拆開。

---

# 28. Future Phase-X Naming Rule

未來命名「X 相位」前，必回答：

### A. X 是 identity 嗎？

若是，不應直接叫 phase。

### B. X 是 state 嗎？

若只是 state，需通過 Renaming Test。

### C. X 是 relation 嗎？

可進 PH-5/PH-6，但必標 IF-3 或其他角色。

### D. X 有 path dependence / holonomy 嗎？

若有，可標 IF-2。

### E. X 改變 identity 嗎？

若有，進 IF-4，必定義 lineage。

### F. X 是 physical oscillator 嗎？

只有明確 $S^1$/phase response/realization 才進 PH-0。

---

# 29. IPFC 與 Phase Canon 的分工

Phase Canon：

$$
\boxed{
\text{What kind of phase is this?}
}
$$

IPFC：

$$
\boxed{
\text{How does this phase sit relative to identity?}
}
$$

Identity Calculus：

$$
\boxed{
\text{What remains the same under indexing/presentation?}
}
$$

PCPRT：

$$
\boxed{
\text{What physical system realizes the effective state/phase?}
}
$$

GPC-CS：

$$
\boxed{
\text{What does interaction do to carrier state and safety?}
}
$$

這五者形成互補，而非競爭。

---

# 30. Canonical Master Diagram

$$
\boxed{
\begin{array}{ccccc}
\mathcal Z_{\mathrm{phys}}
&
\xrightarrow{\Pi}
&
\mathcal X
&
\xrightarrow{\Theta}
&
\Phi
\\
&&
\downarrow q_\kappa
&&
\\
&&
\mathcal O_\kappa
&&
\end{array}
}
$$

加上 presentation：

$$
\boxed{
\mathcal V
\xrightarrow{\rho}
\mathcal X,
\qquad
q_\kappa\rho=h.
}
$$

加上 dynamics：

$$
\boxed{
\mathcal X
\xrightarrow{\Gamma}
\mathcal X.
}
$$

identity preserving：

$$
\boxed{
q_\kappa\Gamma=q_\kappa.
}
$$

identity lineage：

$$
\boxed{
q_{\kappa'}\Gamma=Lq_\kappa.
}
$$

phase transport：

$$
\boxed{
\Theta T^\mathcal X_\gamma
\approx
T^\Phi_\gamma\Theta.
}
$$

這就是 IPFC v0.1 的母結構。

---

# 31. 最終定義

**同一性–相位纖維微積分（IPFC）**：

> 研究一個系統如何在明確的 identity projection 下形成身份纖維，phase 如何作為纖維內 state、跨纖維 relation 或 path-dependent transport variable 演化，以及何時 phase dynamics 保持 identity、何時產生 holonomy、何時必須提升為 identity-lineage transition 的橋接微積分。

最短版本：

$$
\boxed{
\text{Identity defines the fiber;}
\quad
\text{phase describes position, relation, and transport;}
\quad
\text{lineage records fiber change.}
}
$$

中文：

> **同一性決定「是哪一個」；相位決定「這一個現在在哪裡、和誰相對、沿路怎麼變」；譜系決定「何時已經不再只是同一個的變化」。**

---

# 32. 外部數學錨點

本理論不宣稱 fiber/holonomy 是 EveMissLab 新創概念。

外部成熟數學/物理先例包括：

1. Barry Simon (1983), *Holonomy, the Quantum Adiabatic Theorem, and Berry's Phase*, Physical Review Letters 51, 2167.  
   幾何相位被精確識別為 Hermitian line bundle connection 的 holonomy。

2. Frank Wilczek & A. Zee (1984), *Appearance of Gauge Structure in Simple Dynamical Systems*, Physical Review Letters 52, 2111.  
   說明 holonomy / gauge transport 可推廣到 non-Abelian structure，而不必只是一個 scalar $U(1)$ phase。

這些文獻只提供 fiber/connection/holonomy 的成熟數學先例。

它們不證明：

- semantic phase 是量子相位；
- AI latent state 是 gauge field；
- identity fiber 是物理 fiber bundle。

IPFC 的 generalized applications 必須各自通過 Phase Canon 與 PAC。

---

# 33. Next Papers / Modules

IPFC Foundation 完成後，最自然的下游順序：

## IPFC-01
**《同一性–相位纖維微積分：身份投影、纖維內相位與閉路 Holonomy》**

## IPFC-02
**《相位語義：同一語義身份上的關係座標、Context Transport 與 Semantic Holonomy》**

## IPFC-03
**《相變與同一性分岔：Identity-Preserving Regime Change 與 Lineage Transition》**

## IPFC-04
**《GPC 中的載體同一性：跨載體交流、Receiver Update 與 Identity Safety》**

## IPFC-05
**《Phase Module Calculus：XX 相位的通用接駁、組合與反證規格》**

## IPFC-06
**《AI Fork、忒修斯與語義分裂：Identity Lineage 的計算模型》**

---

**IPFC Foundation v0.1 — OPEN FOR FORMALIZATION.**
