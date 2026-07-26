# Method

## Shared basis

The program uses normalized real-even paired bump functions supported in `[-R,R]`. The same basis is used for the Fourier evaluation and for the arithmetic correlation matrices.

## Shared constraints

The full coefficient space is projected to the nullspace of

\[
G(i/2)=0
\]

and, in the default experiment,

\[
G(0)=0.
\]

The second condition is an experimental restriction, not a necessary endpoint condition of the explicit formula.

## Shared normalization

Let `C0` be the zero-lag correlation Gram matrix. The constrained space is whitened so that

\[
c^TC_0c=1.
\]

## Joint minimax problem

On a finite fitting grid `w_k`, the solver minimizes an epigraph variable `t` subject to

\[
2\operatorname{Re}(G_c(w_k)^2)\le t,
\]

\[
c^TM_{\mathrm{arith}}c\ge\delta,
\]

and the normalization constraint. The result is checked on a denser grid.

## Arithmetic matrix

\[
M_{\mathrm{arith}}=M_\infty+M_{\mathrm{fin}}.
\]

The finite-place matrix activates only prime powers satisfying

\[
m\log p<2R.
\]

The archimedean matrix uses the compact-support time-domain kernel from the preceding prototype.

## Audit

For the selected coefficient vector, the arithmetic quadratic value is recomputed from the combined test function rather than only by matrix multiplication. The two calculations are compared in `normalization_audit.json`.
