# Method

## 1. Coordinate model

在 $[-3,3]$ 上建立 24 個實偶 bumps，以步長 $0.01$ 做 floating
quadrature。施加 $G(0)=G(i/2)=0$ 後，模型維度為 $22$。令
$g(z)\in\mathbb C^{22}$，並定義

$$
C(z)=2\operatorname{Re}(g(z)g(z)^{\mathsf T}),\qquad
P(x)=g(x)g(x)^{\mathsf T}.
$$

對 $A\succeq0$，核心與實軸值分別為

$$
B_A(z)=\langle C(z),A\rangle,\qquad
H_A(x)=\langle P(x),A\rangle\ge0.
$$

## 2. Primal lower-bound target

有限分帶目標是

$$
J(A)=\langle T,A\rangle+\sum_j\widehat N_j u_j,
$$

其中 $u_j\ge H_A(x)$ 對第 $j$ 帶的每個網格點成立。只保留
$A_1=[18,23]$ 的下界資訊，取 26 點均勻網格及向下截斷 count

$$
\underline N_1=7.113998598824.
$$

令

$$
M_1=\frac{\underline N_1}{26}
\sum_{x\in\mathcal G_1}P(x).
$$

由非負性可得

$$
J(A)\ge\langle\rho T+M_1,A\rangle
$$

對任意 $0<\rho\le1$ 成立。

## 3. Dual witness

對 patch 中心 $z_P$，若

$$
W_P=\rho T+M_1+\alpha C(z_P)\succeq0,
$$

則 $A\succeq0$ 與 $\langle C(z_P),A\rangle\le-1$ 蘊含

$$
J(A)\ge\alpha.
$$

Primary family 使用

$$
\rho=10^{-3},\qquad\alpha=2.
$$

它在全部 18 個 patch 中心通過。

## 4. Verification layers

1. 以 `numpy.linalg.eigvalsh` 檢查原 floating matrices。
2. 對 quadrature step、axis step 與 $\rho$ 做 sensitivity sweep。
3. 將矩陣和 transform vectors 匯出為十進有理數。
4. 從有理 vectors 重建 $P$ 與 $C$，以 `Fraction` 執行 exact
   $LDL^{\mathsf T}$。
5. 把 v0.2 的 saved Gram matrices 代回
   $\langle W_P,A_P\rangle$ 檢查對偶恆等式。

Exact rational 層證明的是所匯出 surrogate 的 positivity，不是 analytic
Fourier integrals 的 interval enclosure。

## 5. Support diagnostic

在每單位約 8 個 bumps 的規則下改變 $R$，用 generalized eigenvalues
求 tail-only 單點 threshold。報告

$$
e^{2R}
$$

作為質數側截斷成本代理。這是一項研究診斷，不是可行性定理，也不把
$R=8.5$ 宣稱為臨界半徑。
