# Next Node: Paley–Wiener Axis/Core Extremal v0.6

## Node

`RH-PaleyWiener-AxisCoreExtremal-20260724-v0.6`

## 為何轉向

v0.5 已分離三件事：

- 子空間 notch 被 exact monotonicity 排除；
- 外部 slope lift 的 joint improvement 只有 $1.12\%$；
- polynomial-bump 幾何改善到 $3.87\%$，但以小 tail eigenvalue 與 peak
  migration 為代價，仍有 $\alpha_{\rm safe}>1$。

反覆出現的 $A_1$/core tradeoff 更像 compact-support entire functions 的
連續極值限制，而非再加一批局部 atoms 就能解決的 dictionary 問題。

## 第一個連續問題

固定 $R$ 與結構零點，考慮 real-even
$\psi\in H^2_0([-R,R])$，令

$$
G(z)=\int_{-R}^{R}\psi(t)e^{izt}\,dt.
$$

以目標核心 $\mathcal P\subset\mathcal R$ 與五個實軸帶 $A_j$ 定義

$$
\mathcal J_R(G)
=\mathcal T_R(G)
+\sum_{j=0}^{4}\underline N_j
  \sup_{x\in A_j}G(x)^2.
$$

研究帶有核心正規化的 extremal value

$$
\Lambda_R
=\inf_G\left\{
\mathcal J_R(G):
\sup_{z\in\mathcal P}2\operatorname{Re}G(z)^2\le-1,\ 
G(0)=G(i/2)=0
\right\}.
$$

第一個目標不是宣稱 $\Lambda_R\ge1$，而是建立：

1. 函數空間、domain 與 evaluation functionals 的嚴格定義；
2. 存在性或 compactness 條件；
3. primal–dual formulation 與 strong-duality 所需假設；
4. 可由 reproducing kernels 表示的有限 measure dual；
5. 能與 v0.5 discrete witnesses 對照的 Galerkin convergence statement。

## 工作包

1. 選擇 Paley–Wiener 或 de Branges 型 Hilbert space normalization。
2. 導出 real-axis value、complex-core value、derivative 與 tail 的 kernel。
3. 把五帶 sup 改寫成 probability-measure dual。
4. 檢查 v0.5 support measures 是否近似連續 Euler–Lagrange/KKT support。
5. 先在簡化的一帶一點核心模型求 closed-form 或 rigorous lower bound。
6. 只有在連續模型顯示 $\Lambda_R<1$ 的可信可能性時，才回到新 dictionary
   與 primal construction。

## Success gate

至少完成下列之一：

- 一個帶明確假設的解析 lower bound，能解釋 v0.5 的 persistent dual block；
- 一個具 convergence/error control 的 Galerkin upper bound，顯示某個 $R\le16$
  可能穿越 $1$；
- 一個 rigorous separating inequality，證明特定 continuous subproblem
  不可行。

## Stop rules

- 不把更多局部 bump density 當作新研究方向。
- 不接受只在離散 axis grid 上成立的 $\alpha<1$。
- 不把 finite-basis saturation 說成 continuous impossibility。
- 未有 kernel/error theorem 前，不擴建大型 prime matrices。
