# 第 2 輪方法

## 二次指數極限族

第 1 輪徑向導數族為：

\[
f'_{a,c,\varepsilon}(\theta)
=
\exp\left[
-a\exp\left(
-\frac{(\theta-c)^2}{\varepsilon^2}
\right)
\right].
\]

當 \(a,\varepsilon\) 同時增大，且

\[
q=\frac{a}{\varepsilon^2}
\]

保持有限時，去除會被長度正規化吸收的常數因子後：

\[
f'_{a,c,\varepsilon}(\theta)
\sim
\exp\left[q(\theta-c)^2\right].
\]

因此定義穩定極限族：

\[
r'(\theta)\propto\exp\left[q(\theta-c)^2\right].
\]

令：

\[
f(\theta)=\int_0^\theta \exp\left[q(u-c)^2\right]du,
\qquad
r(\theta)=bf(\theta).
\]

終點由：

\[
\Theta+\arctan\frac{f(\Theta)}{f'(\Theta)}=\pi
\]

決定，尺度 \(b\) 由 \(L=1\) 決定。

## 活動曲率邊界

沿：

\[
\max\kappa=24.95<\rho^{-1}=25
\]

搜尋。

## 完整合同張力

\[
E_{\mathrm{cong}}=\min(E_+,E_-).
\]

其中 \(E_+\) 為原向分支，\(E_-\) 為鏡像分支。

## 共同凸厚化容器

\[
H=\operatorname{conv}\left(\bigcup_i g_i\gamma_i\right),
\qquad
C_\rho=H\oplus\rho B.
\]

\[
\mu_2(C_\rho)
=
\mu_2(H)+\rho\operatorname{Per}(H)+\pi\rho^2.
\]
