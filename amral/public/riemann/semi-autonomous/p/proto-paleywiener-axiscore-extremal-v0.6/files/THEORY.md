# Theory

## 1. Continuous tail Hilbert space

固定 $R>0$ 與 $\kappa_R>0$。令

$$
\mathcal H_R
=\left\{
\psi\in H_0^2(-R,R;\mathbb R):
\psi(t)=\psi(-t)
\right\},
$$

其中 $H_0^2$ 取 clamped trace：

$$
\psi(\pm R)=\psi'(\pm R)=0.
$$

定義

$$
\langle\psi,\phi\rangle_T
=\kappa_R\int_{-R}^{R}\psi''(t)\phi''(t)\,dt.
$$

由 clamped Poincaré inequality，這是 Hilbert norm。令

$$
G_\psi(z)
=\int_{-R}^{R}\psi(t)e^{izt}\,dt.
$$

$G_\psi$ 是 exponential type 至多 $R$ 的 entire function。每個 fixed
$z$ 的 evaluation 在 $\mathcal H_R$ 上連續。

結構子空間為

$$
\mathcal H_R^0
=\left\{
\psi\in\mathcal H_R:
G_\psi(0)=G_\psi(i/2)=0
\right\}.
$$

因 $\psi$ 為 even，

$$
G_\psi(i/2)
=\int_{-R}^{R}\psi(t)\cosh(t/2)\,dt.
$$

## 2. Evaluation representers

對 real $x$，令 $p_x\in\mathcal H_R^0$ 為

$$
\langle\psi,p_x\rangle_T=G_\psi(x).
$$

對 $z=x+iy$，令 $u_z,v_z\in\mathcal H_R^0$ 分別 represent
$\operatorname{Re}G_\psi(z)$ 與 $\operatorname{Im}G_\psi(z)$。其 densities
為

$$
f_z^{\rm re}(t)=\cos(xt)\cosh(yt),
$$

$$
f_z^{\rm im}(t)=-\sin(xt)\sinh(yt).
$$

定義 rank-one／rank-two operators

$$
P_x=p_x\otimes p_x,
$$

$$
C_z
=2\left(u_z\otimes u_z-v_z\otimes v_z\right).
$$

則

$$
\langle\psi,P_x\psi\rangle_T=G_\psi(x)^2,
$$

$$
\langle\psi,C_z\psi\rangle_T
=2\operatorname{Re}G_\psi(z)^2.
$$

## 3. Trace-class primal

令 $\mathcal A_j$ 為五個實軸帶，$\mathcal P$ 為 target core patch，
$N_j>0$ 為指定 count coefficients。考慮

$$
\begin{aligned}
\Lambda_R=\inf\quad&
\operatorname{Tr}(A)+\sum_{j=0}^{4}N_js_j\\
\text{subject to}\quad&
A\succeq0,\qquad A\in\mathcal S_1(\mathcal H_R^0),\\
&\operatorname{Tr}(P_xA)\le s_j
\quad(x\in\mathcal A_j),\\
&\operatorname{Tr}(C_zA)\le-1
\quad(z\in\mathcal P).
\end{aligned}
$$

有限 multi-test Gram matrices 是這個問題的 finite-rank instances。

## 4. Measure dual and weak duality

令每個 $\mu_j$ 是 $\mathcal A_j$ 上的 probability measure，$\nu$ 是
$\mathcal P$ 上的 probability measure。若

$$
W
=I+\sum_{j=0}^{4}N_j\int_{\mathcal A_j}P_x\,d\mu_j(x)
+\alpha\int_{\mathcal P}C_z\,d\nu(z)
\succeq0,
$$

則對每個 primal-feasible $A$，

$$
\operatorname{Tr}(WA)\ge0.
$$

另一方面，

$$
\begin{aligned}
\operatorname{Tr}(WA)
&=\operatorname{Tr}(A)
+\sum_jN_j\int\operatorname{Tr}(P_xA)\,d\mu_j(x)\\
&\quad+\alpha\int\operatorname{Tr}(C_zA)\,d\nu(z)\\
&\le\operatorname{Tr}(A)+\sum_jN_js_j-\alpha.
\end{aligned}
$$

因此

$$
\Lambda_R\ge\alpha.
$$

這是 continuous weak duality。它只需要一個 dual-feasible measure
witness，不需要 strong duality。

## 5. One-axis/one-core closed form

固定 $x,z$ 與 $N>0$，令

$$
B=I+N\,p_x\otimes p_x.
$$

考慮

$$
\inf_{A\succeq0}
\left\{
\operatorname{Tr}(BA):
\operatorname{Tr}(C_zA)\le-1
\right\}.
$$

設

$$
\widehat u=B^{-1/2}u_z,\qquad
\widehat v=B^{-1/2}v_z,
$$

以及

$$
a=\|\widehat u\|^2,\qquad
b=\|\widehat v\|^2,\qquad
c=\langle\widehat u,\widehat v\rangle.
$$

$B^{-1/2}C_zB^{-1/2}$ 的唯一可能非零特徵值為

$$
\lambda_\pm
=(a-b)\pm\sqrt{(a+b)^2-4c^2}.
$$

若 $\lambda_-<0$，最優值為

$$
\Lambda(x,z;N)
=-\frac1{\lambda_-}
=\frac1{
\sqrt{(a+b)^2-4c^2}-(a-b)
}.
$$

由 Sherman–Morrison，

$$
a
=\|u_z\|^2
-\frac{N\langle p_x,u_z\rangle^2}
{1+N\|p_x\|^2},
$$

$$
b
=\|v_z\|^2
-\frac{N\langle p_x,v_z\rangle^2}
{1+N\|p_x\|^2},
$$

$$
c
=\langle u_z,v_z\rangle
-\frac{N\langle p_x,u_z\rangle
\langle p_x,v_z\rangle}
{1+N\|p_x\|^2}.
$$

所以整個 simplified extremal 只依賴六個 kernel inner products。

## 6. Explicit clamped Green kernel

先不投影結構零點。令

$$
L=2R,\qquad
\xi=s+R,\qquad
\eta=t+R,
$$

$$
a=\min(\xi,\eta),\qquad
b=\max(\xi,\eta).
$$

clamped bi-Laplacian kernel 為

$$
K_{\rm cl}(s,t)
=\frac{
a^2(L-b)^2\left[3bL-(L+2b)a\right]
}{
6L^3\kappa_R
}.
$$

它滿足

$$
\kappa_R\partial_s^4K_{\rm cl}(s,t)=\delta_t(s)
$$

及兩端 clamped boundary conditions。

對 density $f$，令

$$
k_f(t)=\int_{-R}^{R}K_{\rm cl}(t,s)f(s)\,ds.
$$

結構 densities 為

$$
c_0(t)=1,\qquad c_1(t)=\cosh(t/2).
$$

令

$$
M_{ij}
=\iint c_i(s)K_{\rm cl}(s,t)c_j(t)\,ds\,dt,
$$

$$
b_f
=\begin{pmatrix}
\langle k_{c_0},k_f\rangle_T\\
\langle k_{c_1},k_f\rangle_T
\end{pmatrix}.
$$

則投影到 $\mathcal H_R^0$ 後的 kernel pairing 為

$$
\Gamma(f,g)
=\iint f(s)K_{\rm cl}(s,t)g(t)\,ds\,dt
-b_f^\mathsf TM^{-1}b_g.
$$

## 7. Finite atomic Schur reduction

對 finite atomic measures，將所有 axis vectors 與 positive core-real
vectors 吸收到

$$
B_\alpha=I+UU^\ast,
$$

並將 core-imaginary negative vectors寫成 columns of $V$。則

$$
W_\alpha=B_\alpha-VV^\ast.
$$

因 $B_\alpha\succ0$，

$$
W_\alpha\succeq0
$$

等價於

$$
S_\alpha
=I-V^\ast B_\alpha^{-1}V
\succeq0.
$$

Woodbury identity 給出

$$
S_\alpha
=I-\left[
V^\ast V
-V^\ast U
\left(I+U^\ast U\right)^{-1}
U^\ast V
\right].
$$

本節點的 witness 只有兩個 core atoms，因此 $V$ 只有兩個 columns，
$S_\alpha$ 是 $2\times2$。所有 entries 只由顯式
$\Gamma(f,g)$、有理 weights 與有理 coefficients 組成。

這是 v0.7 interval certificate 的完整有限化介面。
