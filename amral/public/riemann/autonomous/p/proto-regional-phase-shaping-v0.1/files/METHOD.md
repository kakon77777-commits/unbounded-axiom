# 方法與數學邊界

## 1. 原型做了什麼

對一個偏軸矩形 \(K\)，程式在有限維實偶緊支撐基底中求解：

\[
\min_{c\in\ker E}
\sum_{w_j\in K}
\left|\sum_kc_kG_k(w_j)-i\right|^2
+\lambda\|c\|_2^2,
\]

其中端點泛函為：

\[
E(c)=G_c(i/2).
\]

實偶性使：

\[
G_c(-i/2)=G_c(i/2),
\]

所以一個實線性條件同時消去兩個 Mellin 端點。

## 2. 為何區塊是負的

在實偶條件下：

\[
G(\bar w)=\overline{G(w)}.
\]

因此偏軸共軛區塊為：

\[
B(w)=2\operatorname{Re}(G(w)^2).
\]

若 \(G(w)=u+iv\)，則：

\[
B(w)=2(u^2-v^2).
\]

只要整個矩形上：

\[
|v|>|u|,
\]

區塊即為負。逼近 \(i\) 是達成此條件的方便方法，不是唯一方法。

## 3. 連續區域估計

程式以：

\[
|G(w)|\le
\int|\psi(t)|e^{|\operatorname{Im}w||t|}\,dt=M_0
\]

與：

\[
|G'(w)|\le
\int|t\psi(t)|e^{|\operatorname{Im}w||t|}\,dt=M_1
\]

得到：

\[
\|\nabla B\|_2\le4\sqrt2M_0M_1.
\]

若網格最大值為 \(B_{\max}^{\rm grid}\)，每格到最近網格點的最大距離為 \(r\)，則候選上界為：

\[
B_{\max}^{\rm cont}
\le
B_{\max}^{\rm grid}+4\sqrt2M_0M_1r.
\]

目前 \(M_0,M_1\) 仍由浮點求積得到，因此這不是嚴格區間證書。

## 4. 尚未處理

本包不計算：

- ζ 零點；
- 繞數；
- Gamma 分布；
- 質數位置矩陣；
- 其他零點洩漏；
- Weil 二次型的總符號。

它只完成：

\[
\text{偏軸矩形}
\longrightarrow
\text{有限維 Paley–Wiener 候選負方向}.
\]
