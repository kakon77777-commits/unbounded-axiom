# Research Log

## 2026-07-25

### 問題重述

v0.8 已否定 scalar count lower 對 arbitrary dual measure 的 operator
transfer。主線改成：

$$
\text{cell occupancy}
\to
\text{uncertain locations}
\to
\text{universal operator family}.
$$

### Exact prototype

選用真正的 $H_0^1(0,1)$ Dirichlet Green kernel，讓全部位置依賴都是
piecewise rational。先找到 count-only configuration

$$
x_1=x_2=\frac15
$$

的 exact negative determinant，再選擇分離 occupancy cells 測試位置資訊
是否足以修復。

根盒 interval determinant lower 為負；自適應 cover 最終以 $8$ 個葉盒、
最大深度 $7$ 完成 universal proof。

### Parent clamped transfer

觀察到直接從 v0.7 Schur matrix 抽取 full-operator eigenvalue margin 並非
必要。把 $\alpha$ 從 $21/20$ 降到 $1$ 可由 convex combination 自動得到
$1/21$ identity margin。

以兩次 Poincaré 與 rank-one difference bound，把 $58$ 個固定 atoms
擴成獨立 cell。uniform half-width $2\times10^{-15}$ 通過；
$2.5\times10^{-15}$ 超出當前 proof budget，但沒有被誤標成實際失敗。

### Floating local diagnostic

建立 deterministic adversarial corner search。threshold 在 $0.016$ 仍略
高於 $1$，在 $0.017$ 低於 $1$；三層 time-step refinement 穩定。

這揭示約 $8\times10^{12}$ 的 exact-versus-local scale gap。下一輪改做
local interval Green derivative 與 adaptive Schur cover，而不是再細化
scalar counts。

### Status

- exact synthetic family：完成；
- conditional abstract clamped family：完成；
- actual zeta occupancy source：未完成；
- global RH certificate：false。

