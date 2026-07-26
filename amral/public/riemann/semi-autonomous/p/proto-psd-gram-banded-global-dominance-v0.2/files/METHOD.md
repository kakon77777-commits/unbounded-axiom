# Method

## Constrained transform space

The floating model uses $24$ real even compactly supported polynomial bumps on
$[-3,3]$, sampled at step $0.01$. Two structural linear constraints,
$G(0)=0$ and $G(i/2)=0$, leave a $22$-dimensional $C_0$-whitened coordinate
space. No zeta-zero ordinate is used in this construction.

For the transform row $g(z)\in\mathbb C^{22}$ and $A\succeq0$, define

$$
B_A(z)=2\operatorname{Re}\!\left(g(z)^{\mathsf T}A g(z)\right).
$$

Writing $A=LL^{\mathsf T}$ with columns $\ell_r$ and
$\Phi_r(z)=g(z)^{\mathsf T}\ell_r$ gives

$$
B_A(z)=2\sum_r\operatorname{Re}\!\left(\Phi_r(z)^2\right),
\qquad
H_A(x)=\sum_r|\Phi_r(x)|^2\ge0
$$

for real $x$. Thus PSD is constructive, even though the factorized numerical
search is nonconvex.

## Two comparison cones

The diagonal baseline is

$$
A=\sum_{k=1}^{72}\lambda_k v_kv_k^{\mathsf T},
\qquad \lambda_k\ge0,
$$

using the inherited candidate rays. Its banded program is a linear program.

The Gram search allows $A=LL^{\mathsf T}$ directly in the full constrained
space. Ranks $1,2,4,8$ are tested on four representative patches; the
all-patch run uses rank one after the observed rank collapse.

## Banded zero-position-free objective

The real-axis prefix is partitioned as

$$
[14,18],\ [18,23],\ [23,35],\ [35,70],\ [70,145].
$$

For band $I_j$, floating count profile $\widehat N_j$, and grid
$\mathcal G_j$, the sampled objective is

$$
\mathcal M_{\mathrm{samp}}(A)
=\langle T,A\rangle
+\sum_{j=0}^4\widehat N_j
\max_{x\in\mathcal G_j}H_A(x).
$$

Here $\langle T,A\rangle$ is a prototype tail majorant based on
$2R\int|\psi''|^2$ and a $t^{-4}$ density profile beyond $145$. The first 50
known ordinates are evaluated only after optimization as a holdout.

Each patch imposes

$$
B_A(z)\le-1
$$

on its active core grid, together with an arithmetic floor
$\langle Q_{\mathrm{arith}},A\rangle\ge10^{-3}$.

Stage one minimizes $\mathcal M_{\mathrm{samp}}$. Stage two minimizes the
nonnegative guard bound subject to at most $5\%$ overhead in the stage-one
majorant. A cutting-plane exchange adds the worst dense core point and the
worst violating point from every axis band until the dense-grid violation
tolerance is met.

## Sampling and continuity audit

- Initial core grid: $9\times7$ per patch.
- Dense core grid: $161\times121$.
- Initial axis spacing: $0.5$.
- Dense axis spacing: $0.05$.
- Guard ring: based on a $49\times37$ surrounding grid.

The refined core audit samples the actual first derivatives and adds a global
second-derivative envelope. If a cell has widths $\Delta x,\Delta y$, the
reported upper enclosure is

$$
\max_{\mathrm{grid}}B_A
+\frac{\Delta x}{2}\widehat L_x
+\frac{\Delta y}{2}\widehat L_y,
$$

where $\widehat L_x,\widehat L_y$ are sampled derivative maxima enlarged by
the Hessian envelope over the cell.

Likewise, the axis-band correction uses

$$
u_j^{\mathrm{corr}}
=u_j^{\mathrm{samp}}
+\frac{h_j}{2}
\left(
\max_{\mathcal G_j}|H_A'|
+\frac{h_j}{2}\widehat M_{2,A}
\right).
$$

These are floating envelopes for this discretized transform model, not
interval-arithmetic proofs about exact integrals.

## Partial gap

The package reports

$$
\Delta_{\mathrm{partial}}
=1-\mathcal M(A)
-\max\!\left(0,\sup_{\mathrm{guard}}B_A\right).
$$

The word “partial” is essential: unknown off-axis zero bands, zero presence in
the target patch, and the full explicit-formula sign accounting are not
included.
