# 實驗方法

## 固定參數

\[
(L,\rho,\tau)=(1,0.04,\pi).
\]

\(\tau=\pi\) 表示法向針完成全部無向方向。

每一條合法中心線的無端帽法向帶面積為：

\[
2\rho L=0.08.
\]

完整開曲線管狀鄰域面積為：

\[
2\rho L+\pi\rho^2.
\]

## 曲線族

### 常曲率半圓

\[
\gamma(s)
=
\left(
\frac{\sin(\pi s)}{\pi},
\frac{1-\cos(\pi s)}{\pi}
\right).
\]

### 一般平滑徑向調制螺旋

令

\[
f'(\theta)
=
\exp\left[
-a\exp\left(
-\left(\frac{\theta-c}{\varepsilon}\right)^2
\right)
\right],
\]

\[
f(\theta)
=
\int_0^\theta f'(u)\,du,
\]

\[
r(\theta)=bf(\theta).
\]

終點 \(\Theta\) 由切向總轉角條件決定：

\[
\Theta+
\arctan\frac{f(\Theta)}{f'(\Theta)}
=
\pi.
\]

尺度 \(b\) 由曲線長度等於一決定。

- \(a=0\)：阿基米德螺旋；
- 接觸飽和族：調整 \(a\) 使最大曲率等於 \(1/\rho\)；
- 有限寬度曲率層：以有限預算 max-min 支撐張力搜尋取得。

## 共同凸容器代理

對各曲線選擇剛體配置 \(g_i\in SE(2)\)，定義中心凸包：

\[
H
=
\operatorname{conv}
\left(
\bigcup_i g_i\gamma_i
\right).
\]

厚化共同容器為：

\[
C_\rho
=
H\oplus \rho B.
\]

由 Steiner 公式：

\[
\mu_2(C_\rho)
=
\mu_2(H)
+
\rho\operatorname{Per}(H)
+
\pi\rho^2.
\]

使用 differential evolution 加 Powell 局部修正，搜尋各曲線的旋轉和平移。

## Leave-one-out 支撐張力

對未包含目標曲線的中心容器 \(H_{-i}\)，定義：

\[
E_\infty(\gamma_i\mid H_{-i})
=
\inf_{\phi,t}
\max_\theta
\left[
h_{\gamma_i}(\theta-\phi)
+
t\cdot u_\theta
-
h_{H_{-i}}(\theta)
\right].
\]

因目標與容器均厚化同一個 \(\rho\)，支撐函數中的 \(+\rho\) 相消。

因此：

- \(E_\infty\le0\)：目標厚化曲線可放入既有厚化容器；
- \(E_\infty>0\)：至少需要相應的各向同性支撐擴張。

## 誠實邊界

這是有限曲線族、凸容器、離散方向與有限搜尋預算下的第一輪實驗。沒有全域最優證書，也沒有對 reach 作完整區間驗證。
