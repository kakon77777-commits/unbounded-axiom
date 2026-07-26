# Next Node Specification: Axis–Target Dual Obstruction v0.3

## Objective

Determine whether unit off-axis negativity on each target patch forces a
real-axis band budget greater than $1$, with first priority on $[18,23]$.
This is a lower-bound problem, not another candidate search.

## Finite-grid primal

For core matrices $C_q$, axis matrices $P_{jm}$, tail matrix $T$, arithmetic
matrix $Q$, band count coefficients $n_j$, and arithmetic floor $a=10^{-3}$,
the convex unfactorized stage-one problem is

$$
\begin{aligned}
\text{minimize}\quad&
\langle T,A\rangle+\sum_j n_ju_j\\
\text{subject to}\quad&
\langle C_q,A\rangle\le-1 &&\text{for every core point }q,\\
&
\langle P_{jm},A\rangle\le u_j
&&\text{for every axis point }(j,m),\\
&
\langle Q,A\rangle\ge a,\\
&
A\succeq0,\qquad u_j\ge0.
\end{aligned}
$$

The saved Burer–Monteiro solutions give primal upper bounds for this problem.
The next node must produce lower bounds.

## Exact conic dual

Introduce multipliers

$$
\alpha_q\ge0,
\qquad
\beta_{jm}\ge0,
\qquad
\tau\ge0.
$$

A dual form is

$$
\begin{aligned}
\text{maximize}\quad&
\sum_q\alpha_q+a\tau\\
\text{subject to}\quad&
T+\sum_q\alpha_qC_q
+\sum_{j,m}\beta_{jm}P_{jm}
-\tau Q\succeq0,\\
&
\sum_m\beta_{jm}\le n_j
&&\text{for each band }j.
\end{aligned}
$$

Every feasible dual point is a directly checkable lower-bound witness. The
axis weights can be written as

$$
\beta_{jm}=n_j\mu_{jm},
\qquad
\mu_{jm}\ge0,
\qquad
\sum_m\mu_{jm}\le1.
$$

This makes the “supremum dominates an average” interpretation explicit.

## First experiment

1. Use one representative core point and only $A_1=[18,23]$ axis weights.
2. Add multiple core points on the patch only if the single-point lower bound
   is weak.
3. Add the tail matrix, then $A_0$ and $A_2$; defer distant bands unless dual
   slack shows they matter.
4. Optimize an approximate witness, then verify the saved matrix eigenvalues
   independently.
5. Refine both core and axis meshes and track the lower-bound drift.

## Verification route

For a proposed witness, recompute

$$
W
=T+\sum_q\alpha_qC_q
+\sum_{j,m}\beta_{jm}P_{jm}
-\tau Q.
$$

The floating research check is

$$
\lambda_{\min}(W)>0
$$

with a safety margin substantially larger than reconstruction error.
Promotion requires rational or interval enclosures for all entries and a
certified positive lower bound for $\lambda_{\min}(W)$.

## Decision thresholds

- If all $18$ patches have a certified dual value greater than $1$, retire the
  present $R=3$, $22$-dimensional function class under this budget model.
- If stable dual values remain below $1$, inspect dual slack to identify
  missing primal directions before changing the basis.
- If only $[18,23]$ weights are active, formulate the resulting local
  axis-target transfer inequality analytically.
- Do not treat an approximate dual search failure as evidence that the primal
  optimum is below $1$.
