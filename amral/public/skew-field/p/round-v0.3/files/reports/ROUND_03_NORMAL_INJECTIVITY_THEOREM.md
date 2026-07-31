# 半轉向正曲率法向單射定理

令平面曲線以切向角 \(\alpha\) 參數化，曲率半徑為

\[
R(\alpha)=\frac{1}{\kappa(\alpha)}.
\]

假設

\[
0<\kappa(\alpha),\qquad R(\alpha)\ge R_0>0,
\qquad \alpha_1-\alpha_0\le\pi.
\]

定義法向映射

\[
F(\alpha,t)=\gamma(\alpha)+tN(\alpha).
\]

則在 \(|t|<R_0\) 的開法向帶內，\(F\) 為單射。

若兩條法線在 \(\alpha<\beta\) 處相交，令 \(\Delta=\beta-\alpha\)、\(m=(\alpha+\beta)/2\)，則

\[
t+u
=
\frac{1}{\sin(\Delta/2)}
\int_\alpha^\beta R(v)\cos(v-m)\,dv
\ge 2R_0.
\]

所以不可能同時有 \(|t|<R_0\) 與 \(|u|<R_0\)。

本定理證明的是直接雙向法向帶的全局單射性，不自動完成圓形端帽的全局 reach 證明。
