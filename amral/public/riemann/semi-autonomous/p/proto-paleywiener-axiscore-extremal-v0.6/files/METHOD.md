# Method

## 1. Domain choice

選擇 real-even clamped $H_0^2(-R,R)$，並用

$$
\kappa_R\int\psi''(t)\phi''(t)\,dt
$$

作為 tail inner product。這使 tail operator 成為 identity，Fourier
evaluation 變成 bounded Riesz functionals，也保留 compact support 與
exponential type $R$。

本節點固定 $R=16$ 與 v0.5 困難 patch：

$$
[20.395,20.42]\times[-0.10625,-0.1].
$$

## 2. Nested Galerkin family

在 $u=t/R$ 上使用

$$
\phi_n(t)
=\left(1-u^2\right)^2T_{2n}(u),
$$

其中 $T_{2n}$ 為 even Chebyshev polynomial。window 使 value 與 first
derivative 在兩端同時為零。

每個 raw space 依序：

1. 投影掉 $G(0)$、$G(i/2)$ 兩個 constraint rows；
2. 以 tail Gram whitening；
3. 以 2,048-point Gauss–Legendre quadrature 計算 Fourier transforms；
4. 在五軸帶步長 $0.1$ 與 $3\times3$ core grid 上做 cutting-plane joint
   measure optimization。

raw dimensions 為

$$
24,40,64,80,96,120,144,160,176,192.
$$

## 3. Independent Green solver

為避免 Galerkin basis 自我驗證，另直接解

$$
\kappa_Rk''''=f
$$

及 clamped boundary conditions。若左端為 $a=-R$，先取

$$
k_p(t)
=\frac1{6\kappa_R}
\int_a^t(t-s)^3f(s)\,ds,
$$

再加二次與三次 homogeneous terms，使右端 value/slope 同時為零。

程式用 cumulative moments

$$
\int_a^t s^mf(s)\,ds,\qquad m=0,1,2,3,
$$

計算 representer，不需建立大型 dense Green matrix。

## 4. Three independent agreement tests

1. **Dimension test：** nested Galerkin point extremal 隨維度下降。
2. **Quadrature test：** 1,024、1,536、2,048、2,560-point
   Gauss–Legendre 在 raw dimension 192 比較。
3. **Direct-kernel test：** time steps $0.02,0.01,0.005,0.0025$ 的 Green
   ODE solver 與 Galerkin 極限比較。

## 5. Atomic transfer

取 raw dimension 192 的 joint measures：

- 五帶 axis atom counts：$22,5,14,9,8$；
- core atoms：2；
- total evaluation vectors：62。

先在更高 Galerkin dimensions

$$
208,224,256,288
$$

重建同一 measures，再用 direct Green solver 完全移除 dictionary。

## 6. Rationalization

每一組 measure weights 以 denominator

$$
10^{12}
$$

做 largest-remainder rationalization，確保每組 numerators 精確加總到
$10^{12}$。supports 轉成 decimal rationals；certificate target 固定為

$$
\alpha=\frac{21}{20}=1.05.
$$

tail scale 另取 $10^{18}$ denominator 的 downward decimal rational。
這仍只建立 abstract-model candidate；其作為 theorem-backed zeta
coefficient 的合法性留給 v0.7。

## 7. Schur certificate budget

對 $\alpha=1.01,1.03,1.05,1.06$ 與 v0.6 safe alpha 分別重建。
正方向 rank 為 60，負方向 rank 為 2，因此最終只需驗證 $2\times2$
Schur matrix。時間步長 $0.005\to0.0025$ 的 Schur minimum drift 被保存為
下一節點的誤差規模診斷，但不是 rigorous error bound。
