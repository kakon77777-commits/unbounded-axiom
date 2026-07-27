# Method

## 1. Lineage reconstruction

本節點直接追溯 v0.1–v0.7 的目標函數與 dual：

- v0.1 使用連續軸能量作候選生成 proxy；
- v0.2 改為 count upper 乘 band supremum 的 leakage envelope；
- v0.3–v0.6 對該 epigraph envelope 建立 finite 與 continuous dual；
- v0.7 對固定 continuous atomic operator 完成 interval positivity。

審計不改動任何父節點輸出，只重新標記各物件能合法支援的結論。

## 2. Exact semantic countermodels

`bridge/semantics.py` 使用 `Fraction` 建立兩個完全精確的反例：

1. 二點 band 反例，否定 lower count 乘任意 probability measure；
2. $\mathbb Q^2$ 中兩個不共線 rank-one operators，證明共同 PSD floor
   只能是零。

這一層不使用浮點數值。

## 3. Typed band profiles

使用 inherited profile

$$
|S(T)|
\le
0.112\log T
+
0.278\log\log T
+
2.510
$$

及 floating Riemann–Siegel theta，對每個 band 計算

$$
L_{a,b}
=
\max\left(
0,
\frac{\theta(b)-\theta(a)}{\pi}
-B(a)-B(b)
\right),
$$

$$
U_{a,b}
=
\max\left(
0,
\frac{\theta(b)-\theta(a)}{\pi}
+B(a)+B(b)
\right).
$$

程式把 $L$ 與 $U$ 分別標為 `count_lower_candidate` 與
`count_upper_candidate`。本節點沒有 interval-enclose `loggamma`、對數
或 endpoint conventions，因此兩者仍是 E2 theorem objects。

## 4. Lower-profile Galerkin search

固定：

$$
R=16,
$$

結構條件

$$
G(0)=G(i/2)=0,
$$

以及 prototype patch

$$
[20.395,20.42]\times[-0.10625,-0.1].
$$

採用 clamped even Chebyshev family

$$
\left(1-u^2\right)^2T_{2n}(u),
\qquad
u=t/R,
$$

用 tail quadratic form whitening。raw dimensions 為

$$
24,40,64,80,96,120,144,160,176,192.
$$

lower candidate profile 向下截到 $12$ 位：

$$
(0,0,0,5.069962795568,26.742367141539).
$$

只有 $A_3,A_4$ 進入 measure optimization；前三帶的 coefficient 為零，
不建立無效 simplex variables。

## 5. Atomic measure dual

對非零 band measures $\mu_j$ 與 prototype core measure $\nu$，建立

$$
B_\mu
=
I
+
\sum_jL_j\int P_x\,d\mu_j(x),
$$

$$
C_\nu
=
\int C_z\,d\nu(z).
$$

固定 measures 時，

$$
\alpha_\ast
=
-\frac{1}{\lambda_{\min}(C_\nu,B_\mu)}.
$$

SLSQP 在 simplex 上更新 weights；cutting-plane 把當前 generalized
eigenvector 在每個非零 band 的最大軸點加入 active set。

這裡的 $L_j$ 只用來測試 abstract lower-profile epigraph model。依本節點
的 exact semantic theorem，它不是 actual zero-side operator transfer。

## 6. Direct Green transfer

最後一組 atomic measures 直接放入 clamped $D^4$ Green RKHS，使用

$$
\Delta t\in\{0.02,0.01,0.005\}.
$$

先投影掉 $1$ 與 $\cosh(t/2)$ 兩個 structural representers，再以
projected Gram eigenfactorization 求同一 generalized threshold。

這消除 Galerkin dictionary 依賴，但仍是 floating trapezoid transfer，
不是 v0.7 類型的 interval certificate。

## 7. Sampled primal escape

取 effective dimension $190$ 的 minimum generalized vector，在

$$
101\times101
$$

core grid 與 axis step $0.01$ 上重算。縮放使 sampled core maximum 等於
$-1$，再計算

$$
\|q\|^2
+
\sum_jL_j\sup_{\mathrm{grid}}H_q.
$$

這提供與 dual 門檻一致的 sampled primal escape。它沒有證明整個
continuous patch 的負性，因此明確標為 E2 diagnostic。

## 8. Reproducibility

`run_all.py` 依序重建所有 JSON。`verify_outputs.py` 再檢查：

- exact semantic countermodels；
- profile 重算；
- Galerkin 維度序列；
- direct Green convergence；
- sampled primal objective；
- active probability sums；
- 全部 RH global flags 為 false。

`run_tests.py` 使用 Python standard-library `unittest`，不需要額外測試
框架。
