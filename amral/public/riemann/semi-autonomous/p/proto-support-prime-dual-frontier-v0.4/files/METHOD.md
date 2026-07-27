# Method

## 1. 有限座標

在 $[-R,R]$ 上建立實偶 compact polynomial bumps，施加

$$
G(0)=G(i/2)=0,
$$

再用 $C_0$ Gram matrix whitening。對受限 transform row $g(z)$ 定義

$$
C(z)=2\operatorname{Re}\!\left(g(z)g(z)^{\mathsf T}\right),
\qquad
P(x)=g(x)g(x)^{\mathsf T}\succeq0.
$$

未知多測試函數族由任意 $A\succeq0$ 表示。

## 2. Primal proxy

對五個軸帶 $A_j$，離散變數 $u_j$ majorize

$$
H_A(x)=\langle P(x),A\rangle.
$$

有限目標為

$$
J(A)=\langle T,A\rangle+\sum_j\underline N_j u_j.
$$

patch 的必要負向條件在 $3\times3$ 核心點上寫成

$$
\langle C(z_q),A\rangle\le-1.
$$

## 3. Measure dual

對每帶取機率測度 $\mu_j$，對核心點取機率測度 $\nu$：

$$
B_\mu=T+\sum_j\underline N_j\int P(x)\,d\mu_j(x),
\qquad
C_\nu=\int C(z)\,d\nu(z).
$$

若

$$
B_\mu+\alpha C_\nu\succeq0,
$$

則任一 primal-feasible $A$ 滿足

$$
J(A)\ge\alpha.
$$

所以 $\alpha>1$ 是該有限 patch 的阻擋證書。

## 4. 最佳化

固定測度時，

$$
\alpha_*=-\frac{1}{\lambda_{\min}(C_\nu,B_\mu)}.
$$

程式以 SLSQP 在 simplex 上更新權重，並用 cutting-plane 將每個軸帶
上對當前 generalized eigenvector 最敏感的節點加入 active set。

任何已匯出的非負測度與 PSD witness 自身就是有效有限模型 lower
bound；不需要證明測度全域最佳。相反地，$\alpha<1$ 只表示目前搜尋未
找到阻擋。

## 5. Rank-two 快速篩選

單點核心矩陣滿足

$$
C(z)=2\left(rr^{\mathsf T}-ii^{\mathsf T}\right),
$$

其中 $g(z)=r+ii$。whitening 後只需解一個至多二維的特徵值問題，
`rank_two_point_thresholds` 用此結構加速 126 組 uniform frontier。

## 6. Cover

目標矩形

$$
[20,20.5]\times[-0.2,-0.1]
$$

先由 18 個 anisotropic overlapping patches 覆蓋，再各切為
$4\times4$，形成 288 個子矩形。`run_cover_audit.py` 同時做 rational
atomic-cell probe 與 $501\times301$ dense grid audit。

## 7. Prime cutoff

Fourier convention 為

$$
G(w)=\int\psi(t)e^{iwt}\,dt.
$$

由自相關支撐，

$$
m\log p<2R
\iff
p^m<e^{2R}.
$$

`segmented_prime_log_histogram` 逐段枚舉質數與 prime powers，將係數

$$
-2\log(p)p^{-m/2}
$$

線性沉積到 log bins。此壓縮尚無 interval interpolation error。

## 8. 證據層級

- E0：有限 PSD 自對偶推論與 support cutoff 代數。
- E1：程式結構、JSON 關聯、cover 與檔案集合驗證。
- E2：floating quadrature、eigensolve、最佳化與 witness 重建。
- E3：連到解析顯式公式的 interval/theorem certificate；本節點沒有。

