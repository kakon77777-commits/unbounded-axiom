# v0.1 Numerical Results

Target spectral rectangle:

\[
8.0\le \operatorname{Re}w\le 8.5,
\qquad
-0.2\le \operatorname{Im}w\le -0.1.
\]

Shared configuration:

- 24 real-even paired bump functions;
- endpoint constraint `G(i/2)=0`;
- experimental central constraint `G(0)=0`;
- `C0` normalization `c^T C0 c = 1`;
- 60 fitting points and 1,891 dense checking points;
- arithmetic safety requirement equal to 20% of the minimum eigenvalue on the constrained normalized space.

| R | Prime powers | min eig(A) | required margin | candidate q_A | dense max block | dense min block | grid intersection |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1.5 | 12 | 4.8907e-4 | 9.7815e-5 | 1.00548 | -1.0809e-8 | -1.6009e-6 | yes |
| 2.0 | 24 | 1.0136e-3 | 2.0271e-4 | 0.22150 | -6.8324e-7 | -1.1733e-4 | yes |
| 2.5 | 47 | 7.8769e-4 | 1.5754e-4 | 0.29242 | -7.6498e-6 | -1.1209e-3 | yes |
| 3.0 | 98 | 1.5722e-3 | 3.1445e-4 | 0.04917 | -2.3078e-5 | -3.9722e-3 | yes |
| 3.5 | 209 | 1.0563e-3 | 2.1127e-4 | 0.17381 | -4.0988e-5 | -8.5057e-3 | yes* |
| 4.0 | 465 | 1.2528e-3 | 2.5057e-4 | 0.28110 | -5.9203e-5 | -2.0932e-2 | yes |

`*` The SLSQP termination flag at `R=3.5` was not success, but the returned candidate passed the independent feasibility checks. Optimizer status and candidate feasibility are intentionally reported separately.

## Selected normalization audit: R=3.0

Matrix evaluation:

\[
Q_\infty=0.14945347602365677,
\]

\[
Q_{\mathrm{fin}}=-0.10027857308007093,
\]

\[
Q_{\mathrm{total}}=0.049174902943585994.
\]

Direct recomputation from the combined test function:

\[
Q_\infty=0.14945347602365650,
\]

\[
Q_{\mathrm{fin}}=-0.10027857308007099,
\]

\[
Q_{\mathrm{total}}=0.04917490294358551.
\]

The total absolute discrepancy was approximately

\[
4.86\times10^{-16}.
\]

Constraint and normalization residuals:

\[
|G(i/2)|\approx5.55\times10^{-17},
\]

\[
|G(0)|\approx4.16\times10^{-17},
\]

\[
|c^TC_0c-1|\approx3.33\times10^{-16}.
\]

## Legal interpretation

The experiment establishes only:

\[
\boxed{
\text{a common floating-point coefficient vector satisfies both finite-grid tests}
}
\]

for the synthetic target rectangle and the listed support radii.

It does not establish continuous regional negativity, interval PSD, control of the remaining zero contribution, or the Riemann hypothesis.

## Quadrature sensitivity at R=3.0

| Time-grid points | min eig(A) | candidate q_A | dense max block | grid intersection |
|---:|---:|---:|---:|:---:|
| 1601 | 0.00155327 | 0.04944579 | -2.30781897e-5 | yes |
| 2401 | 0.00157225 | 0.04917490 | -2.30781713e-5 | yes |
| 3201 | 0.00152806 | 0.04951111 | -2.30781897e-5 | yes |

The regional maximum remained stable to approximately `2e-11` across these grids. The arithmetic value varied by about `3.4e-4`, without approaching the required margin or changing sign. This is numerical convergence evidence only.
