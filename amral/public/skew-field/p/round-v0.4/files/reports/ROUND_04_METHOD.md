# 第 4 輪方法

## 曲率函數空間

\[
g_M(s)
=
\sum_{m=1}^M
\left[
a_m\cos(2\pi ms)
+
b_m\sin(2\pi ms)
\right],
\]

\[
\kappa_M(s)
=
\frac{
\pi e^{g_M(s)}
}{
\int_0^1e^{g_M(u)}du
}.
\]

比較：

\[
M=6,\;8,\;10.
\]

## 搜尋分層

第一層使用方向寬度代理：

\[
w_\gamma(\theta)
=
h_\gamma(\theta)+h_\gamma(\theta+\pi).
\]

第二層對固定旋轉相位解平移線性規劃：

\[
h_\gamma(\theta-\phi)
+
t\cdot u_\theta
-
h_C(\theta)
\le z.
\]

第三層同時計算原向與鏡像：

\[
E_{\mathrm{cong}}
=
\min(E_+,E_-).
\]

## 凸容器

\[
\mu_2
\left(
\operatorname{conv}
\bigcup_i g_i\gamma_i
\oplus\rho B
\right).
\]

## 非凸容器

\[
\mu_2
\left(
\bigcup_i
g_iT_\rho(\gamma_i)
\right).
\]

先貪婪加入，再逐族作座標下降。單連通版本以聯集外邊界填孔後的面積作目標。

## 驗證層

- 曲率：向外風格浮點盒；
- 直接法向帶：第 3 輪半轉向正曲率法向單射定理；
- 管狀面積：高解析 buffer；
- 伴隨梯度：中央有限差分；
- 容器：高解析 convex hull／union 重播。
