# METHOD

## 1. Real-even spectral block

For a real-even compactly supported test function,

\[
G(w)=\int_{\mathbb R}\psi(t)e^{iwt}\,dt
\]

satisfies

\[
G(-w)=G(w),\qquad G(\overline w)=\overline{G(w)}.
\]

The off-axis conjugate block is

\[
B(w)=2\operatorname{Re}(G(w)^2).
\]

## 2. Finite critical-line annihilation

For stored ordinates \(\gamma_1,\ldots,\gamma_q\), the floating model imposes

\[
G(\gamma_j)=0,\qquad 1\le j\le q.
\]

It also imposes

\[
G(0)=0,\qquad G(i/2)=0.
\]

These equalities are exact only relative to the chosen basis and trapezoidal
quadrature model.

## 3. Paired-bump basis

The basis consists of 24 real-even compact polynomial bumps:

\[
\phi_j(t)
=
b\!\left(\frac{t-a_j}{h}\right)
+
b\!\left(\frac{t+a_j}{h}\right),
\]

where

\[
b(u)=
\begin{cases}
(1-u^2)^3,&|u|<1,\\
0,&|u|\ge1.
\end{cases}
\]

## 4. Arithmetic constraint

The same coefficient vector is used in

\[
Q_{\rm arith}(c)
=
c^\top M_{\rm arith}c.
\]

The model requires

\[
Q_{\rm arith}(c)\ge\delta.
\]

The arithmetic matrix uses the same time-domain archimedean kernel and
finite-prime-power activation rule as the previous arithmetic-matrix
prototype.

## 5. Target minimax

The target rectangle is

\[
20\le\operatorname{Re}w\le20.5,\qquad
-0.2\le\operatorname{Im}w\le-0.1.
\]

The finite problem minimizes the largest sampled value of \(B(w)\) under
normalization, annihilation, and arithmetic positivity.

## 6. Control-window exchange

The finite control window is

\[
10\le\operatorname{Re}w\le60,\qquad
-0.45\le\operatorname{Im}w\le-0.05.
\]

A sparse control set is optimized first. The worst point on a denser grid is
added to the active constraints, and the problem is solved again.

This is a floating exchange-method prototype for a semi-infinite QCQP.

## 7. Why a nonzero control window cannot touch the axis

For real \(x\),

\[
B(x)=2G(x)^2\ge0.
\]

Suppose a nonzero entire \(G\) satisfied \(B(x+iy)\le0\) on a region whose
closure contains an open real interval. Continuity would give \(G(x)=0\) on
that interval. The identity theorem would imply \(G\equiv0\).

Therefore a nontrivial nonpositivity window must retain a gap

\[
|\operatorname{Im}w|\ge\beta_{\min}>0.
\]

A complete program would have to study the cost as
\(\beta_{\min}\downarrow0\), not pretend that one fixed nonzero function can
remain nonpositive all the way to the critical axis.
