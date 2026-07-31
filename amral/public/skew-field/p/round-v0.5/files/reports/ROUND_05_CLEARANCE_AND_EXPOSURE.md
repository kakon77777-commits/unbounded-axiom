# 清距場、形態腐蝕與面積外露張力

## 1. 厚化曲線的包含條件

令：

\[
T_\rho(\gamma)
=
\gamma\oplus B_\rho
\]

為中心線的完整管狀鄰域，\(C\subset\mathbb R^2\) 為閉容器。

定義形態腐蝕：

\[
C\ominus B_\rho
=
\left\{
x:
x+B_\rho\subseteq C
\right\}.
\]

則：

\[
\boxed{
T_\rho(\gamma)\subseteq C
\iff
\gamma\subseteq C\ominus B_\rho.
}
\]

等價地，若：

\[
d_C(x)
=
\operatorname{dist}(x,C^c),
\qquad x\in C,
\]

則：

\[
T_\rho(\gamma)\subseteq C
\iff
\inf_{s}d_C(\gamma(s))\ge\rho.
\]

## 2. 為何不直接使用多邊形負 buffer

對離散化邊界直接計算：

\[
C.\operatorname{buffer}(-\rho)
\]

時，圓弧近似、凹角與細通道可能造成額外收縮。

第 4 輪七條已知合法中心線，在原始容器中的點態最小清距均約為：

\[
0.04,
\]

但多邊形負 buffer 會把其中多條中心線錯誤判為外露。

因此第 5 輪的快速搜尋採用清距場：

\[
d_C(x)-\rho,
\]

最終判定則直接計算完整管狀鄰域的外露面積。

## 3. 面積外露張力

定義：

\[
\boxed{
\mathcal A_C(\gamma)
=
\inf_{g\in E(2)}
\mu_2
\left[
(gT_\rho(\gamma))\setminus C
\right].
}
\]

在最小值可達時：

\[
\mathcal A_C(\gamma)=0
\iff
\exists g\in E(2):
gT_\rho(\gamma)\subseteq C.
\]

它與凸支撐缺口不同：

- 支撐缺口只觀測凸包方向；
- 面積外露張力直接觀測非凸凹槽、通道與局部缺口；
- 同一曲線可能在凸支撐意義下冗餘，卻在非凸外露意義下仍有貢獻。

## 4. 快速代理與最終重算

搜尋層使用清距違反：

\[
v_C(x)
=
\max\{0,\rho-d_C(x)\},
\]

並以最大值與高階 \(L^p\) 混合排序。

最終候選必須重新計算：

\[
\mu_2
\left[
(gT_\rho(\gamma))\setminus C
\right].
\]

第 5 輪數據顯示，清距代理能找到候選，但不能可靠排序所有候選；因此它只能作搜尋層，不能作證書層。
