# 第 2 輪術語修正

第 1 輪使用了「接觸飽和平滑螺旋」一詞，但當時實際校準的是：

\[
\max_s\kappa(s)=\rho^{-1}.
\]

這只表示局部曲率半徑達到厚度半徑：

\[
\min_s\frac{1}{\kappa(s)}=\rho.
\]

它不等價於全局：

\[
\operatorname{reach}(\gamma)=\rho.
\]

全局 reach 還受到不同曲線位置之間的最近點、法向交會與自接觸控制。

因此第 2 輪起正式改稱：

\[
\boxed{\text{曲率飽和平滑螺旋}}
\]

而將「接觸飽和」保留給真正驗證：

\[
\operatorname{reach}(\gamma)=\rho
\]

且只發生邊界首次接觸的候選。
