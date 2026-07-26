# Results

## Explicit test function

- support: \([-3,3]\);
- spline spacing: \(h=0.01\);
- nodes: 601;
- endpoint correction:
  \[
  a\in[-0.001409632218803803,-0.001409632218803802];
  \]
- endpoint residual:
  \[
  G(i/2)\in[-6.52,6.52]\times10^{-36}.
  \]

## Continuous regional sign

Target:

\[
K=[8,8.5]+i[-0.2,-0.1].
\]

Validated cover:

- certified cells: 480;
- unresolved cells: 0;
- maximum depth used: 3;
- second-derivative bound:
  \[
  M_2\le11.4820525926;
  \]
- global block upper bound:
  \[
  \boxed{
  \sup_{w\in K}2\operatorname{Re}(G(w)^2)
  \le-2.2416560599\times10^{-6}
  }.
  \]

## Arithmetic sign

Activated prime powers:

\[
\#\{p^m:m\log p<6\}=98.
\]

Finite interval:

\[
Q_{\mathrm{fin}}
\in[-0.099762166120387,-0.099762166120386].
\]

Archimedean interval:

\[
Q_\infty
\in[0.133524840678940,0.161109862461679].
\]

Total:

\[
\boxed{
Q_{\mathrm{arith}}(\psi)
\in[0.033762674558557,0.061347696341296]
}.
\]

Therefore the same explicit function satisfies both strict inequalities.

## Interpretation

This is the first package in the series that replaces:

- dense-grid negativity by a continuous rectangular cover;
- one floating arithmetic value by a positive interval;
- inherited sampled arrays by an explicit piecewise-linear mathematical object.

It establishes a nonempty validated intersection in the finite-dimensional model. It does not yet bound all non-target zero contributions.
