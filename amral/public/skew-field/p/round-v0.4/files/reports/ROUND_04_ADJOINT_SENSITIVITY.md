# 曲率函數—支撐函數伴隨靈敏度

## 曲率正規化

令：

\[
g_a(s)=\sum_j a_j\phi_j(s),
\]

\[
\kappa_a(s)
=
\frac{
\tau e^{g_a(s)}
}{
\int_0^1e^{g_a(u)}du
}.
\]

則：

\[
\delta\kappa(s)
=
\kappa(s)
\left[
\delta g(s)
-
\frac1{\tau}
\int_0^1\kappa(u)\delta g(u)du
\right].
\]

對單一係數：

\[
\frac{\partial\kappa(s)}{\partial a_j}
=
\kappa(s)
\left[
\phi_j(s)-\bar\phi_j
\right],
\]

其中：

\[
\bar\phi_j
=
\frac1{\tau}
\int_0^1\kappa(u)\phi_j(u)du.
\]

## 中心線變分

\[
\theta(s)=\int_0^s\kappa(v)dv,
\qquad
\delta\theta(s)=\int_0^s\delta\kappa(v)dv.
\]

由：

\[
\gamma'(s)=T(s),
\qquad
\delta T(s)=N(s)\delta\theta(s),
\]

得到：

\[
\delta\gamma(s)
=
\int_0^sN(u)\delta\theta(u)du.
\]

## 支撐函數變分

若方向 \(n\) 的支撐點 \(s_\ast\) 唯一：

\[
h_\gamma(n)=\gamma(s_\ast)\cdot n,
\]

則：

\[
\delta h_\gamma(n)
=
n\cdot\delta\gamma(s_\ast).
\]

因此：

\[
\frac{\partial h_\gamma(n)}{\partial a_j}
=
\int_0^{s_\ast}
\left[
n\cdot
\int_v^{s_\ast}N(u)du
\right]
\kappa(v)
\left[
\phi_j(v)-\bar\phi_j
\right]dv.
\]

方向寬度：

\[
w_\gamma(n)=h_\gamma(n)+h_\gamma(-n)
\]

的梯度為兩個支撐點貢獻之和。

若活動支撐點、方向或相位不唯一，則改用 Clarke 次梯度凸包。

## 數值核對

對第 4 輪 Fourier-10 候選：

\[
\max_j
\left|
D_j^{\rm FD}-D_j^{\rm adj}
\right|
=
7.537290719695e-05,
\]

相對 \(L^2\) 誤差：

\[
1.194240584988e-03.
\]

此結果支持下一輪使用伴隨梯度取代大部分黑箱係數搜尋，但尚不是區間梯度證書。
