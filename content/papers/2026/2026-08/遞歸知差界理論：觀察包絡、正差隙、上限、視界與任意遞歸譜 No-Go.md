# 遞歸知差界理論：觀察包絡、正差隙、上限、視界與任意遞歸譜 No-Go

**English title:** Recursive Epistemic Bound Theory: Observed Envelopes, Positive Gaps, Ceilings, Horizons, and the Arbitrary-Profile No-Go

**Series:** Recursive Knowing-Difference Algebra / 遞歸知差代數系列  
**Paper ID:** EML-RKD-05  
**Version:** v0.1  
**Date:** 2026-08-16  
**Author:** Neo.K（許筌崴）  
**Affiliation:** EveMissLab / 一言諾科技有限公司  
**Document status:** FORMAL EXTENSION / BOUND THEORY  
**Upstream:** EML-RKD-01, EML-RKD-02, EML-RKD-03, EML-RKD-04  
**Claim strength:** 本文研究在固定量化契約與觀察域下可建立的遞歸知差上下界。本文證明若干條件性 bound 與結構性 No-Go，但不宣稱存在跨所有認知存在、所有任務與所有觀察者的單一普遍知差界。

---

## 摘要

EML-RKD-04 將遞歸知差拆成 structural rank、functional amplitude、fidelity、information gain 與 direction/calibration。本文進一步研究：這些量在觀察存在集合擴張、遞歸階數增加與資源條件改變時，究竟有哪些上下界可以合法推出？

本文首先定義固定量化契約 $Q$ 下的觀察值域：

$$
\mathcal V_{n,Q}(t)
=
\left\{
\Delta_{X,n}^{Q}(p):
X\in\mathfrak X_{\mathrm{obs}}^Q(t),
\;
p\in\mathcal P_X^Q
\right\},
$$

以及觀察下包絡、上包絡：

$$
L_{n,Q}(t)
=
\inf\mathcal V_{n,Q}(t),
$$

$$
U_{n,Q}(t)
=
\sup\mathcal V_{n,Q}(t).
$$

若 observed corpus 在固定 protocol 下只增不減，則：

$$
L_{n,Q}(t)
$$

單調不增，

$$
U_{n,Q}(t)
$$

單調不減；在 normalized bounded codomain 中兩者皆有極限。這是一個**觀察時間方向**的單調結果，而不是遞歸深度方向的衰減律。

本文最重要的結構性結果是**任意遞歸譜可實現性（Arbitrary Recursive Profile Realizability）**：對任意指定序列

$$
(a_n)_{n\ge0},
\qquad
a_n\in[0,1],
$$

可構造一個 exact-coherent graded tower，使每一階 functional meta-amplitude 恰為：

$$
\nu_n=a_n.
$$

因此在不加入額外 contraction、resource、noise、information 或 architectural hypotheses 時，不存在由遞歸深度本身推出的普遍：

$$
\Delta_{n+1}\le\Delta_n,
$$

也不存在普遍：

$$
\Delta_n\to0,
$$

或有限最大遞歸視界定理。遞減、遞增、振盪、週期、平台、稀疏與任意 bounded profile 在純代數上都可實現。

本文隨後定義 positive recursive gap、recursive ceiling、structural/functional/observable horizons，以及 fixed-protocol asymptotic envelope。本文證明：若額外假設 uniform multiplicative contraction：

$$
\Delta_{n+1}\le\lambda\Delta_n,
\qquad
0\le\lambda<1,
$$

則得到幾何衰減與 logarithmic horizon bound；若每階至少產生 additive loss $\delta>0$，則得到 linear horizon bound。若每階有效遞歸有成本 $c_n$ 且總預算有限，則是否能有無限階不由「預算有限」單獨決定，而由：

$$
\sum_n c_n
$$

是否發散決定。

本文亦定義 recursive mass、meta-amplification factor 與 recursive efficiency，指出每階知差趨零不代表整體累積遞歸知差有限。文末把所有 bound 分成：無條件代數界、protocol-fixed observation bounds、以及需額外結構假設才成立的 conditional depth bounds。

**關鍵詞：** 遞歸知差；上下界；observed envelope；positive gap；recursive ceiling；recursion horizon；arbitrary profile；contraction；resource bound；metareasoning；data processing

---

## Abstract

This paper develops a bound theory for Recursive Knowing Difference. Under a fixed quantification contract, it defines observed lower and upper envelopes, positive recursive gaps, ceilings, and structural/functional/observable horizons.

The central structural result is an arbitrary-profile realizability theorem: every bounded sequence $(a_n)\subseteq[0,1]$ can be realized as the functional recursive-difference profile of an exactly coherent graded tower. Hence recursion depth alone does not imply monotone decay, convergence to zero, or a finite maximal horizon.

Meaningful decay theorems require additional assumptions. Uniform multiplicative contraction yields geometric decay and logarithmic horizon bounds; fixed additive loss yields linear horizon bounds. Finite total resource alone does not imply finite recursion depth: the decisive condition is whether cumulative per-level cost diverges.

The paper separates unconditional algebraic bounds, fixed-protocol observational bounds, and architecture-dependent conditional bounds, preparing the final bound branch for a subsequent paper on strong infinite recursive knowers.

---

# 1. 問題轉換：從「量多少」到「能界多少」

Paper 04 建立：

$$
\mathbf Q_{X,n}^{RKD,Q}
=
(r,\nu,\phi,g,c).
$$

本文允許選取其中某一 axis：

$$
\mu\in
\{
r,\nu,\phi,g,\ldots
\}
$$

或某個明確 scalarizer：

$$
S_Q.
$$

統一記為：

$$
\boxed{
\Delta_{X,n}^{Q}(p)
}
$$

並假設在本文主要 normalized realization 中：

$$
\boxed{
0\le
\Delta_{X,n}^{Q}(p)
\le1.
}
$$

現在問：

$$
\boxed{
\Delta
\text{ 的 lower bound、upper bound、gap、ceiling 與 depth horizon 是什麼？}
}
$$

---

# 2. Bound 不應脫離 contract

定義 bound contract：

$$
\boxed{
B
=
\left(
Q,
\mathfrak X_{\mathrm{obs}},
\mathcal P,
\mu,
\theta,
t
\right).
}
$$

其中：

- $Q$：observation / alignment contract；
- $\mathfrak X_{\mathrm{obs}}$：被納入的存在類別；
- $\mathcal P$：task / content family；
- $\mu$：量化 axis 或 scalarizer；
- $\theta$：功能／觀察 threshold；
- $t$：目前資料歷史位置。

因此本文不寫：

$$
\boxed{
\text{the bound of knowing}.
}
$$

而寫：

$$
\boxed{
\text{bound under }B.
}
$$

---

# 3. Observed Value Set

對固定 recursion level：

$$
n,
$$

定義：

$$
\boxed{
\mathcal V_{n,B}(t)
=
\left\{
\Delta_{X,n}^{Q}(p):
X\in
\mathfrak X_{\mathrm{obs}}^Q(t),
\;
p\in\mathcal P_X^Q
\right\}.
}
$$

如果某些 $X,p$ 在該階不可定義，應標記：

$$
\mathrm{NA},
$$

而不是強迫填：

$$
0.
$$

---

# 4. Hard Lower / Upper Envelope

定義：

$$
\boxed{
L_{n,B}(t)
=
\inf
\mathcal V_{n,B}(t)
}
$$

與：

$$
\boxed{
U_{n,B}(t)
=
\sup
\mathcal V_{n,B}(t).
}
$$

因此：

$$
\boxed{
I_{n,B}(t)
=
[
L_{n,B}(t),
U_{n,B}(t)
].
}
$$

稱為：

$$
\boxed{
\textbf{Observed Recursive Epistemic Envelope}.
}
$$

---

# 5. Theorem T5.1 — Fixed-Protocol Envelope Monotonicity

假設：

1. $B$ 中除 $t$ 外的 protocol 全部固定；
2. observed corpus nested：
   $$
   \mathfrak X_{\mathrm{obs}}(t)
   \subseteq
   \mathfrak X_{\mathrm{obs}}(t+1);
   $$
3. 舊資料的 quantification 不被 retroactive revision 改寫。

則：

$$
\boxed{
L_{n,B}(t+1)
\le
L_{n,B}(t)
}
$$

以及：

$$
\boxed{
U_{n,B}(t+1)
\ge
U_{n,B}(t).
}
$$

**證明。**

新 value set 包含舊 value set：

$$
\mathcal V_{n,B}(t)
\subseteq
\mathcal V_{n,B}(t+1).
$$

集合擴張不能提高 infimum，也不能降低 supremum。∎

---

# 6. Corollary C5.1 — Envelope Limits

若：

$$
\mathcal V_{n,B}(t)
\subseteq
[0,1],
$$

則：

$$
L_{n,B}(t)
$$

為有下界的單調不增序列，

$$
U_{n,B}(t)
$$

為有上界的單調不減序列。

故：

$$
\boxed{
L_{n,B}^{\ast}
=
\lim_{t\to\infty}
L_{n,B}(t)
}
$$

與：

$$
\boxed{
U_{n,B}^{\ast}
=
\lim_{t\to\infty}
U_{n,B}(t)
}
$$

皆存在。

---

# 7. 這不是 depth monotonicity

T5.1 說的是：

$$
\boxed{
t\rightarrow t+1
}
$$

資料集合擴張。

它完全不推出：

$$
\boxed{
n\rightarrow n+1
}
$$

時：

$$
\Delta_{X,n+1}
\le
\Delta_{X,n}.
$$

因此：

$$
\boxed{
\text{corpus monotonicity}
\neq
\text{recursive-depth monotonicity}.
}
$$

---

# 8. Positive Recursive Gap

若：

$$
\mathcal V_{n,B}(t)
\cap
(0,1]
\neq\varnothing,
$$

定義：

$$
\boxed{
\gamma_{n,B}(t)
=
\inf
\left(
\mathcal V_{n,B}(t)
\cap
(0,1]
\right).
}
$$

稱為：

$$
\boxed{
\textbf{Positive Recursive Gap}.
}
$$

如果沒有任何 reliable positive observation，則：

$$
\gamma_{n,B}(t)
=
\mathrm{NA}.
$$

---

# 9. Finite-Sample Gap Trap

若目前只觀察：

$$
\{0.1,0.4,0.8\},
$$

則：

$$
\gamma=0.1.
$$

這只表示：

> 當前 finite corpus 中最小 positive observed value 是 0.1。

完全不表示：

$$
\boxed{
\text{ontology has a minimum recursive quantum of }0.1.
}
$$

---

# 10. Resolution-Tracked Gap

令：

$$
\epsilon_B(t)
$$

為 observation / estimation floor。

定義 reliable positive set：

$$
\boxed{
\mathcal V_{n,B}^{+,\mathrm{rel}}(t)
=
\left\{
v\in\mathcal V_{n,B}(t):
v>\epsilon_B(t)
\right\}.
}
$$

再定義：

$$
\boxed{
\gamma_{n,B}^{rel}(t)
=
\inf
\mathcal V_{n,B}^{+,\mathrm{rel}}(t).
}
$$

只有同時追蹤：

$$
t\to\infty
$$

與：

$$
\epsilon_B(t)
$$

變化，才能討論 asymptotic positive gap。

---

# 11. Gap Trichotomy

對固定：

$$
n,B,
$$

可以有：

### G0 — No reliable positive evidence

$$
\gamma_{n,B}^{rel}
=
\mathrm{NA}.
$$

### G1 — Gapless candidate

$$
\boxed{
\liminf_{t\to\infty}
\gamma_{n,B}^{rel}(t)
=
0.
}
$$

### G2 — Positive-gap candidate

$$
\boxed{
\liminf_{t\to\infty}
\gamma_{n,B}^{rel}(t)
>
0.
}
$$

本文不把 G2 自動叫成 universal quantization。

---

# 12. Recursive Ceiling

定義：

$$
\boxed{
\beta_{n,B}(t)
=
U_{n,B}(t).
}
$$

asymptotic：

$$
\boxed{
\beta_{n,B}^{\ast}
=
U_{n,B}^{\ast}.
}
$$

稱為：

$$
\boxed{
\textbf{Recursive Epistemic Ceiling}.
}
$$

如果：

$$
\beta_{n,B}^{\ast}=1,
$$

只表示在該 normalized contract 下 observed values 可接近上端。

不表示：

$$
\boxed{
\text{absolute omniscience}.
}
$$

---

# 13. Individual Floor

對固定：

$$
X,
$$

定義：

$$
\boxed{
\delta_{X,n}^{B}
=
\inf_{p\in\mathcal P_X^Q}
\left\{
\Delta_{X,n}^{Q}(p)>0
\right\}.
}
$$

在 recursion-depth direction 也可定義：

$$
\boxed{
\delta_X^{B}
=
\liminf_{n\to\infty}
\Delta_{X,n}^{Q}.
}
$$

兩者不要混。

---

# 14. Class Floor

對存在 class：

$$
\mathfrak X,
$$

定義：

$$
\boxed{
\delta_{\mathfrak X}^{B}
=
\inf_{X\in\mathfrak X}
\delta_X^{B}.
}
$$

即使：

$$
\delta_X^{B}>0
$$

對每個 $X$ individually 成立，仍可能：

$$
\boxed{
\delta_{\mathfrak X}^{B}=0.
}
$$

例如：

$$
\delta_{X_m}^{B}
=
\frac1m.
$$

---

# 15. No-Go N5.1 — Individual positivity 不推出 class gap

$$
\boxed{
\forall X\in\mathfrak X,
\quad
\delta_X>0
}
$$

不推出：

$$
\boxed{
\inf_X\delta_X>0.
}
$$

這是最簡單但非常重要的 non-uniformity。

---

# 16. 任意遞歸譜的代數構造

現在進入本文核心。

給任意 bounded sequence：

$$
\boxed{
(a_n)_{n\ge0},
\qquad
a_n\in[0,1].
}
$$

定義：

$$
\boxed{
\mathcal E^{(n)}
=
\mathbb R^{n+1}.
}
$$

bonding map：

$$
\boxed{
F_n
(
x_0,\ldots,x_n,x_{n+1}
)
=
(
x_0,\ldots,x_n
).
}
$$

zero-meta embedding：

$$
\boxed{
\iota_n
(
x_0,\ldots,x_n
)
=
(
x_0,\ldots,x_n,0
).
}
$$

recursive lift：

$$
\boxed{
K_n
(
x_0,\ldots,x_n
)
=
(
x_0,\ldots,x_n,a_n
).
}
$$

---

# 17. Exact Coherence of the Construction

立刻有：

$$
F_nK_n
(
x_0,\ldots,x_n
)
=
(
x_0,\ldots,x_n
).
$$

因此：

$$
\boxed{
F_nK_n=id.
}
$$

所以每一階 target coherence 都 exact。

meta-residual：

$$
\boxed{
m_{n+1}
=
K_n(x)-\iota_n(x)
=
a_n e_{n+1},
}
$$

其中：

$$
e_{n+1}
$$

為新 coordinate 的 unit vector。

若 amplitude：

$$
\nu_n
=
\|m_{n+1}\|_2,
$$

則：

$$
\boxed{
\nu_n=a_n.
}
$$

---

# 18. Theorem T5.2 — Arbitrary Recursive Profile Realizability

對任意 sequence：

$$
(a_n)_{n\ge0}
\subseteq[0,1],
$$

存在一個 exact target-coherent graded recursive system，使其 Euclidean functional meta-amplitude 滿足：

$$
\boxed{
\nu_n=a_n
\quad
\forall n.
}
$$

∎

---

# 19. Corollary C5.2 — No Universal Decay

不存在僅由「recursive level increases」推出的普遍：

$$
\boxed{
\nu_{n+1}\le\nu_n.
}
$$

因為可取：

$$
a_n
=
1-2^{-n-1},
$$

得到遞增 profile。

---

# 20. Corollary C5.3 — No Universal Amplification

同理不存在普遍：

$$
\nu_{n+1}\ge\nu_n.
$$

取：

$$
a_n=2^{-n}
$$

即可。

---

# 21. Corollary C5.4 — No Universal Convergence to Zero

取：

$$
a_n=1.
$$

則：

$$
\nu_n=1
$$

對所有 $n$。

因此：

$$
\boxed{
\text{recursive depth}
\not\Rightarrow
\nu_n\to0.
}
$$

---

# 22. Corollary C5.5 — No Universal Limit

取：

$$
a_n
=
\frac{1+(-1)^n}{2}.
$$

則：

$$
a_n
=
1,0,1,0,\ldots
$$

沒有 limit。

因此：

$$
\boxed{
\text{recursive depth}
\not\Rightarrow
\Delta_n
\text{ converges}.
}
$$

---

# 23. 可合法出現的 profile regime

純代數上可以有：

### Decay

$$
a_n=2^{-n}.
$$

### Persistent

$$
a_n=c>0.
$$

### Amplifying

$$
a_n=1-2^{-n-1}.
$$

### Periodic

$$
a_{n+p}=a_n.
$$

### Sparse

只有：

$$
n=2^k
$$

時：

$$
a_n>0.
$$

### Oscillatory / irregular

任意 bounded sequence。

因此：

$$
\boxed{
\text{profile shape requires extra law, not recursion alone}.
}
$$

---

# 24. No-Go N5.2 — Depth is not a contraction operator

$$
n\mapsto n+1
$$

只是階層索引增加。

它本身沒有數學理由必須是：

- contraction；
- smoothing；
- noise accumulation；
- information loss；
- cost growth。

所有這些都必須額外建模。

---

# 25. Conditional Contraction Assumption

現在加入：

$$
\boxed{
\Delta_{n+1}
\le
\lambda
\Delta_n,
\qquad
0\le\lambda<1.
}
$$

這不是 RKD 母公理。

它是一個 additional realization hypothesis。

---

# 26. Theorem T5.3 — Geometric Recursive Bound

由 induction：

$$
\boxed{
\Delta_n
\le
\lambda^n
\Delta_0.
}
$$

因此：

$$
\boxed{
\Delta_n\to0.
}
$$

---

# 27. Functional Horizon

給：

$$
\theta>0,
$$

定義：

$$
\boxed{
H_X^{fun}(\theta)
=
\sup
\left\{
n:
\Delta_{X,n}\ge\theta
\right\}.
}
$$

若：

$$
\Delta_0<\theta,
$$

則：

$$
H_X^{fun}(\theta)
$$

可視為空或：

$$
-1
$$

依 implementation convention。

---

# 28. Theorem T5.4 — Logarithmic Horizon under Contraction

若：

$$
0<\theta\le\Delta_0,
$$

且：

$$
\Delta_n
\le
\lambda^n\Delta_0,
\qquad
0<\lambda<1,
$$

則任何滿足：

$$
\Delta_n\ge\theta
$$

的 $n$ 必須：

$$
\lambda^n\Delta_0
\ge
\theta.
$$

因此：

$$
\boxed{
n
\le
\frac{
\log(\theta/\Delta_0)
}{
\log\lambda
}.
}
$$

所以：

$$
\boxed{
H_X^{fun}(\theta)
\le
\left\lfloor
\frac{
\log(\theta/\Delta_0)
}{
\log\lambda
}
\right\rfloor.
}
$$

---

# 29. Additive Loss Assumption

若：

$$
\boxed{
\Delta_{n+1}
\le
\max
\{
0,
\Delta_n-\delta
\},
\qquad
\delta>0,
}
$$

則：

$$
\boxed{
\Delta_n
\le
\max
\{
0,
\Delta_0-n\delta
\}.
}
$$

---

# 30. Theorem T5.5 — Linear Horizon under Additive Loss

對：

$$
0<\theta\le\Delta_0,
$$

若：

$$
\Delta_n\ge\theta,
$$

必須：

$$
\Delta_0-n\delta
\ge
\theta.
$$

所以：

$$
\boxed{
H_X^{fun}(\theta)
\le
\left\lfloor
\frac{
\Delta_0-\theta
}{
\delta
}
\right\rfloor.
}
$$

additive loss 產生 linear horizon。

---

# 31. Contraction 需要物理／資訊來源

實際：

$$
\lambda<1
$$

可能來自：

- information channel contraction；
- memory loss；
- finite precision；
- repeated lossy compression；
- noise accumulation；
- imperfect re-encoding；
- bounded attention；
- communication bottleneck。

但這些是 realization assumptions。

本文不把任何一個預設為所有存在必有。

---

# 32. Data Processing 作為條件性前例

若某 observable chain 滿足：

$$
C
\rightarrow
M_n
\rightarrow
M_{n+1},
$$

即高一階只是低一階 observable 的 stochastic post-processing，則普通 data-processing inequality 給：

$$
\boxed{
I(C;M_{n+1})
\le
I(C;M_n).
}
$$

若 channel 進一步滿足 strong data-processing coefficient：

$$
\eta_n<1,
$$

則可以有：

$$
\boxed{
I(C;M_{n+1})
\le
\eta_n
I(C;M_n).
}
$$

這提供一種「為什麼某些 recursion realization 會衰減」的外部數學模板。

---

# 33. No-Go N5.3 — DPI 不能無條件套在 open recursion

若：

$$
M_{n+1}
$$

還取得新的 evidence：

$$
Z_{n+1},
$$

使：

$$
M_{n+1}
=
h(M_n,Z_{n+1}),
$$

而：

$$
I(C;Z_{n+1}\mid M_n)>0,
$$

則：

$$
C\rightarrow M_n\rightarrow M_{n+1}
$$

的純 post-processing Markov 結構不再成立。

所以：

$$
\boxed{
I(C;M_{n+1})
>
I(C;M_n)
}
$$

完全可能。

Paper 06 將正式把這種新資訊寫成 epistemic injection。

---

# 34. Structural Horizon

定義：

$$
\boxed{
H_X^{str}
=
\sup
\left\{
n:
r_{X,n}>0
\right\}.
}
$$

如果：

$$
r_{X,n}=0
$$

從某階後永久成立，structural recursion 在該 contract 下停止新增不可約 meta directions。

---

# 35. Observable Horizon

令 observer detection floor：

$$
\epsilon_{Q,n}.
$$

定義：

$$
\boxed{
H_X^{obs}(Q)
=
\sup
\left\{
n:
\Delta_{X,n}^{Q}>
\epsilon_{Q,n}
\right\}.
}
$$

若 functional threshold：

$$
\theta
$$

滿足：

$$
\theta\le
\epsilon_{Q,n}
$$

在考察範圍成立，則通常：

$$
\boxed{
H_X^{obs}(Q)
\le
H_X^{fun}(\theta)
\le
H_X^{str}
}
$$

但此 inequality 依賴 definitions compatible。

---

# 36. No-Go N5.4 — Observable horizon 不是 intrinsic constant

若 measurement technology 改善：

$$
\epsilon_{Q_t,n}\downarrow0,
$$

則同一 $X$ 的：

$$
H_X^{obs}(Q_t)
$$

可以增加。

因此：

$$
\boxed{
H_X^{obs}
}
$$

是：

$$
\boxed{
X
+
Q
+
t
}
$$

的共同性質。

---

# 37. Resource Cost per Recursive Level

令：

$$
\boxed{
c_{X,n}\ge0
}
$$

表示建立／保持第 $n\to n+1$ 階有效 recursion 的 incremental cost。

這個 cost 可以是：

- time；
- compute；
- memory；
- energy；
- communication；
- sample complexity；
- opportunity cost。

不同 cost 不應在沒有 exchange rate 時直接相加。

本文先假設已被 $Q$ 映到一個共同 resource unit。

---

# 38. Cumulative Recursive Cost

定義：

$$
\boxed{
C_X(N)
=
\sum_{n=0}^{N-1}
c_{X,n}.
}
$$

若 available budget：

$$
B_X<\infty,
$$

可執行 depth $N$ 必須：

$$
\boxed{
C_X(N)\le B_X.
}
$$

---

# 39. Theorem T5.6 — Divergent Cost Implies Finite Budget Horizon

若：

$$
\boxed{
\sum_{n=0}^{\infty}
c_{X,n}
=
\infty,
}
$$

則對任何有限：

$$
B_X<\infty,
$$

存在有限 $N_B$ 使：

$$
C_X(N_B)>B_X.
$$

因此有限 budget 無法支付所有無限多階。

---

# 40. No-Go N5.5 — Finite budget alone 不推出 finite algebraic recursion

若：

$$
c_n=2^{-n-1},
$$

則：

$$
\sum_{n=0}^{\infty}c_n
=
1.
$$

所以抽象 cost model 中，有限 budget：

$$
B=1
$$

不排除支付任意多階。

因此：

$$
\boxed{
B<\infty
\not\Rightarrow
H<\infty.
}
$$

真正分界是 cumulative cost 是否 diverge。

---

# 41. Uniform Positive Cost Bound

若：

$$
\boxed{
c_n\ge c_{\min}>0,
}
$$

則：

$$
C_X(N)\ge Nc_{\min}.
$$

若：

$$
C_X(N)\le B_X,
$$

得到：

$$
\boxed{
N
\le
\left\lfloor
\frac{B_X}{c_{\min}}
\right\rfloor.
}
$$

---

# 42. Geometric Cost Growth

若：

$$
c_n
=
c_0a^n,
\qquad
a>1,
$$

則：

$$
C_X(N)
=
c_0
\frac{a^N-1}{a-1}.
$$

budget condition：

$$
C_X(N)\le B
$$

推出：

$$
\boxed{
N
\le
\log_a
\left(
1+
\frac{(a-1)B}{c_0}
\right).
}
$$

因此 exponentially growing per-level cost 產生 logarithmic budget horizon。

---

# 43. Metareasoning 的資源前例

rational metareasoning 的核心思想之一，就是：

> computation 本身不是免費；是否再多做一步 reasoning，應考慮 expected improvement 與 computation cost。

近年的 LLM metareasoning 工作亦把 reasoning quality 與 inference cost 的 trade-off 直接寫入 reward / policy。

本文只把這些當成：

$$
\boxed{
c_n
\text{ 不應被預設為 }0
}
$$

的工程前例。

但是否：

$$
c_n\ge c_{\min}>0
$$

對任意存在成立，本文不作普遍主張。

---

# 44. Meta-Amplification Factor

若：

$$
\Delta_{X,n}>0,
$$

定義：

$$
\boxed{
\lambda_{X,n}^{meta}
=
\frac{
\Delta_{X,n+1}
}{
\Delta_{X,n}
}.
}
$$

分類：

- $0\le\lambda<1$：attenuation；
- $\lambda=1$：persistence；
- $\lambda>1$：amplification。

如果 denominator 為 0，ratio 標記 NA。

---

# 45. No-Go N5.6 — Meta-amplification 不代表 violation

若：

$$
\lambda_{X,n}^{meta}>1,
$$

只表示高一階在當前 metric 下值更高。

它可能來自：

- better internal processing；
- new external evidence；
- changed measurement scale；
- changed task distribution；
- observer recalibration。

所以要判斷「真正 intrinsic amplification」，Paper 06 必須先控制 injection 與 protocol drift。

---

# 46. Recursive Mass

對 weights：

$$
w_n\ge0,
$$

定義：

$$
\boxed{
M_X^{rec}
=
\sum_{n=0}^{\infty}
w_n\Delta_{X,n}.
}
$$

若：

$$
w_n=1,
$$

得到 unweighted cumulative recursive mass。

---

# 47. No-Go N5.7 — Per-level decay 不推出 finite total mass

令：

$$
\Delta_n
=
\frac1{n+1}.
$$

則：

$$
\Delta_n\to0.
$$

但：

$$
\boxed{
\sum_{n=0}^{\infty}
\Delta_n
=
\infty.
}
$$

所以：

$$
\boxed{
\text{each level becomes weak}
\not\Rightarrow
\text{total recursive contribution is finite}.
}
$$

---

# 48. Power-Law Classification

若：

$$
\Delta_n
\asymp
(n+1)^{-\alpha},
$$

則：

### $\alpha>1$

$$
M^{rec}<\infty
$$

對 $w_n=1$。

### $0<\alpha\le1$

$$
M^{rec}=\infty.
$$

因此 tail rate 本身是重要 bound parameter。

---

# 49. Recursive Efficiency

定義：

$$
\boxed{
\eta_{X,n}^{rec}
=
\frac{
\Delta_{X,n}
}{
c_{X,n}
}
}
$$

若：

$$
c_{X,n}>0.
$$

這不是 information-theoretic $\eta$ ；為避免符號衝突，machine-readable registry 中 canonical alias 採：

$$
\boxed{
\mathrm{Eff}_{X,n}^{rec}.
}
$$

即：

$$
\boxed{
\mathrm{Eff}_{X,n}^{rec}
=
\frac{\Delta_{X,n}}{c_{X,n}}.
}
$$

---

# 50. Cumulative Efficiency

$$
\boxed{
\mathrm{Eff}_{X}^{cum}(N)
=
\frac{
\sum_{n<N}\Delta_{X,n}
}{
\sum_{n<N}c_{X,n}
}
}
$$

若 denominator positive。

這允許比較：

- shallow high-yield system；
- deep low-yield system；
- distributed expensive system；
- compact but noisy system。

但跨資源種類仍需要 cost normalization。

---

# 51. Bound Bundle

本文 canonical bound object：

$$
\boxed{
\mathfrak B_{n,B}^{RKD}
=
\left\langle
L_n,
U_n,
\gamma_n,
\beta_n,
H^{str},
H^{fun},
H^{obs},
M^{rec},
\mathrm{Eff}^{rec}
\right\rangle.
}
$$

它不是一個 scalar。

---

# 52. Bound Type I — Unconditional Algebraic Bounds

例如 Paper 04 ordinary rank：

$$
r>0
\Rightarrow
r\ge1.
$$

以及：

$$
0\le
\Delta
\le1
$$

若 normalization 如此定義。

這些來自 algebra / codomain specification。

---

# 53. Bound Type II — Protocol-Fixed Observational Bounds

例如：

$$
L_n(t)\downarrow,
$$

$$
U_n(t)\uparrow
$$

只在：

- protocol fixed；
- corpus nested；
- old scores not rewritten；

時成立。

---

# 54. Bound Type III — Architecture-Dependent Depth Bounds

例如：

$$
\Delta_{n+1}\le\lambda\Delta_n
$$

推出 geometric decay。

這完全依賴 additional architecture / channel assumption。

因此：

$$
\boxed{
\text{conditional theorem}
\neq
\text{universal law}.
}
$$

---

# 55. Population Upper Envelope under Uniform Contraction

令：

$$
\boxed{
\beta_n
=
\sup_{X\in\mathfrak X}
\Delta_{X,n}.
}
$$

若對 class 中所有 $X$：

$$
\Delta_{X,n+1}
\le
\lambda\Delta_{X,n}
$$

使用共同：

$$
0\le\lambda<1,
$$

則：

$$
\Delta_{X,n}
\le
\lambda^n\Delta_{X,0}.
$$

取 supremum：

$$
\boxed{
\beta_n
\le
\lambda^n\beta_0.
}
$$

因此：

$$
\boxed{
\beta_n\to0.
}
$$

這是一個 class-level conditional collapse result。

---

# 56. No-Go N5.8 — 沒有 uniform coefficient 就不能推出 class decay

如果每個 $X$ 有自己的：

$$
\lambda_X<1
$$

但：

$$
\sup_X\lambda_X=1,
$$

則 class upper envelope 未必以共同幾何率衰減。

例如：

$$
\lambda_{X_m}
=
1-\frac1m.
$$

對每個固定 $X_m$ 都 contraction，

但 across class 可以有 arbitrarily slow decay。

---

# 57. Observation-Depth Matrix

實際實驗資料最好記錄：

$$
\boxed{
D_{i,n}
=
\Delta_{X_i,n}^{Q}.
}
$$

rows：

$$
X_i
$$

為不同存在／個體／system instances，

columns：

$$
n
$$

為 recursion depth。

這樣：

- column envelope 對應 fixed $n$ population bounds；
- row profile 對應 fixed $X$ recursion spectrum；
- global inf/sup 是第三種聚合。

不要把三種方向混在一個 summary statistic。

---

# 58. Recursive Spectrum

對固定 $X$：

$$
\boxed{
\mathbf \Delta_X^{Q}
=
\left(
\Delta_{X,0}^{Q},
\Delta_{X,1}^{Q},
\Delta_{X,2}^{Q},
\ldots
\right).
}
$$

稱為：

$$
\boxed{
\textbf{Recursive Epistemic Spectrum}.
}
$$

T5.2 告訴我們：

> 純代數不限制這條 bounded spectrum 的形狀。

因此任何實際規律都是 empirical / architectural information。

---

# 59. Human Evidence 的位置

Recht 等人在人類特定 nested-confidence task 中觀察到第二至第四階 above-chance behavior，並用包含 recursive evidence degradation 與 noise 的模型解釋高階表現下降。

這提供一個：

$$
\boxed{
\text{某類 human realization 可能呈現 attenuation}
}
$$

的實證前例。

但它不能推出：

$$
\boxed{
\forall X,\quad
\Delta_{n+1}\le\Delta_n.
}
$$

本文的 T5.2 正式說明：純代數不會替這個 empirical pattern 提供普遍性。

---

# 60. AI / Tool-Using System 的位置

對人工系統，meta-level 可能：

- 重算；
- 查工具；
- 呼叫 verifier；
- 使用外部 memory；
- 委派另一 agent。

因此：

$$
\Delta_{n+1}>\Delta_n
$$

不只 algebraically possible，也有合理 architecture mechanism。

這也是為什麼 Paper 06 必須加入：

$$
\boxed{
\text{epistemic injection}
}
$$

而不是只研究 closed contraction。

---

# 61. 本文主要定理

- **T5.1** Fixed-Protocol Envelope Monotonicity；
- **C5.1** Bounded Envelope Limits；
- **T5.2** Arbitrary Recursive Profile Realizability；
- **C5.2** No Universal Decay；
- **C5.3** No Universal Amplification；
- **C5.4** No Universal Convergence to Zero；
- **C5.5** No Universal Limit；
- **T5.3** Geometric Recursive Bound under uniform contraction；
- **T5.4** Logarithmic Functional Horizon；
- **T5.5** Linear Horizon under additive loss；
- **T5.6** Divergent Cost Implies Finite Budget Horizon。

---

# 62. 本文主要 No-Go

- **N5.1** Individual positive floors do not imply a class-wide positive floor；
- **N5.2** Recursion depth is not itself a contraction operator；
- **N5.3** Data Processing cannot be applied unchanged to open recursion with new evidence；
- **N5.4** Observable horizon is not an intrinsic constant of $X$ ；
- **N5.5** Finite budget alone does not imply finite algebraic recursion if cumulative costs are summable；
- **N5.6** Meta-amplification factor $>1$ does not by itself identify intrinsic amplification；
- **N5.7** Per-level decay does not imply finite total recursive mass；
- **N5.8** Individual contraction constants do not yield a uniform class decay unless they are uniformly bounded away from 1。

---

# 63. 對 Paper 01 猜想的第二次回答

Paper 01 問：

$$
\boxed{
\text{知道之知道的上下界是否存在？}
}
$$

本文回答：

> 在固定 bounded quantification contract 下，observed-domain lower/upper envelopes 可以被嚴格定義，且在 nested corpus、fixed protocol 下具有時間方向的 monotone limits。

但：

$$
\boxed{
\text{這不等於存在 recursion-depth universal law}.
}
$$

---

# 64. 對 Paper 04 Dual-Gap 的接續

Paper 04 得到：

$$
\gamma^{rank}=1
$$

與：

$$
\gamma^{fun}=0
$$

可同時成立。

本文現在補上：

$$
\boxed{
\gamma_{n,B}(t)
}
$$

在 observational corpus 中如何演化，

以及：

$$
\boxed{
\beta_{n,B}^{\ast}
}
$$

如何定義。

因此：

$$
\boxed{
\text{algebraic gap}
}
$$

與：

$$
\boxed{
\text{observed positive gap}
}
$$

再次被分離。

---

# 65. 下一篇正式交接

下一篇文件 ID：

$$
\boxed{
\text{EML-RKD-06 — Strong Infinite Recursive Knowers}
}
$$

將在本文 bound skeleton 上加入：

$$
\boxed{
\Delta_{n+1}
\le
\alpha_n\Delta_n
+
\eta_{n+1}
}
$$

其中：

- $\alpha_n$：internal retention / contraction / amplification；
- $\eta_{n+1}$：new epistemic injection。

並研究：

- Strong Infinite Recursive Knower；
- anchored strong recursion；
- closed vs open recursion；
- persistent information contraction；
- resource no-free-lunch；
- observation margin；
- individual vs uniform class strongness。

---

# 66. 結論

本文最重要的結果是：

$$
\boxed{
\text{recursive depth alone imposes no universal profile law}.
}
$$

因為對任意：

$$
(a_n)\subseteq[0,1],
$$

都有 exact-coherent algebraic realization：

$$
\boxed{
\nu_n=a_n.
}
$$

所以沒有額外條件時，以下全部不能當成普遍定律：

$$
\boxed{
\Delta_{n+1}\le\Delta_n,
}
$$

$$
\boxed{
\Delta_{n+1}\ge\Delta_n,
}
$$

$$
\boxed{
\Delta_n\to0,
}
$$

$$
\boxed{
H_X<\infty.
}
$$

真正的 bound 必須來自額外結構。

若加入 uniform contraction：

$$
\Delta_{n+1}\le\lambda\Delta_n,
$$

得到：

$$
\Delta_n\le\lambda^n\Delta_0.
$$

若加入 additive loss：

$$
\Delta_{n+1}\le\Delta_n-\delta,
$$

得到 linear horizon。

若加入 resource cost：

$$
c_n,
$$

真正分界是：

$$
\boxed{
\sum_n c_n
=
\infty
\quad\text{or}\quad
<\infty.
}
$$

因此本文把遞歸知差界理論整理成三層：

$$
\boxed{
\text{algebraic bounds}
}
$$

$$
\boxed{
\text{protocol-fixed observational bounds}
}
$$

$$
\boxed{
\text{architecture-dependent conditional bounds}.
}
$$

這個三層分離阻止我們把某一種人類實驗中的衰減、某一種 AI 架構中的放大、或某一個 finite corpus 中的 positive gap，直接升格成所有認知存在的普遍定律。

下一篇才開始處理真正最強的問題：

$$
\boxed{
\exists X:
\quad
\liminf_{n\to\infty}
\Delta_{X,n}>0
\ ?
}
$$

以及什麼條件允許或禁止這種存在。

---

# References

1. Recht, S., Jovanovic, L., Mamassian, P., & Balsdon, T. (2022). *Confidence at the limits of human nested cognition*. Neuroscience of Consciousness, 2022(1), niac014. DOI: 10.1093/nc/niac014.
2. Polyanskiy, Y., & Wu, Y. (2015). *Strong data-processing inequalities for channels and Bayesian networks*. arXiv:1508.06025.
3. Raginsky, M. (2014). *Strong data processing inequalities and Phi-Sobolev inequalities for discrete channels*. arXiv:1411.3575.
4. De Sabbata, C. N., Sumers, T. R., & Griffiths, T. L. (2024). *Rational Metareasoning for Large Language Models*. arXiv:2410.05563.
5. Cox, M. T., Mohammad, Z., Kondrakunta, S., Gogineni, V. R., Dannenhauer, D., & Larue, O. (2022). *Computational Metacognition*. arXiv:2201.12885.

---

## Version note

v0.1 deliberately separates universal algebraic possibility from conditional decay models. Any later empirical finding of attenuation, amplification, ceilings, or horizons should be registered as a property of a declared observation/architecture class, not silently promoted into a carrier-independent law of recursive knowing.
