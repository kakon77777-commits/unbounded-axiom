# Next node: PSD Gram banded global dominance v0.2

## Fixed input

Retain the 18-patch adaptive anisotropic cover from this package. Do not begin
by increasing the patch count.

Let $\mathbf G(w)$ be the transform vector of a small local basis and let

$$
A_\alpha\succeq0
$$

be the patchwise Gram variable.

Use

$$
B_{A_\alpha}(w)
=
2\operatorname{Re}
\left(
\mathbf G(w)^\mathsf{T}
A_\alpha
\mathbf G(w)
\right).
$$

For real $t$,

$$
B_{A_\alpha}(t)
=
2\mathbf G(t)^\mathsf{T}
A_\alpha
\mathbf G(t)
\ge0.
$$

## Convex program

Minimize a weighted or lexicographic combination of

$$
\operatorname{tr}(A_\alpha E_{\mathrm{axis}}),
$$

guard positive peak, and a Sobolev/tail proxy, subject to:

$$
B_{A_\alpha}(w)\le-1
\quad
(w\in K_\alpha),
$$

$$
\operatorname{tr}(A_\alpha Q_{\mathrm{arith}})
\ge q_{\min},
$$

$$
A_\alpha\succeq0.
$$

Use an exchange loop for dense core and guard points.

## Required ablations

1. diagonal $A$ versus full $A$;
2. rank cap;
3. support radius;
4. axis-energy weight versus roughness weight;
5. shared Gram matrix across patches versus patchwise matrices.

## Required outputs

- floating Pareto frontier;
- eigenvalue and rank diagnostics for $A_\alpha$;
- full zero-side partial budget;
- unknown off-axis band placeholders with explicit nonzero charges;
- diagonal baseline comparison;
- failure frontier if no positive budget is found.

## Promotion gate

Only promote to interval certification when

$$
\Delta_{\mathrm{global}}^{\mathrm{float}}
>
\kappa
\times
\text{estimated total numerical uncertainty}
$$

for a deliberately conservative safety factor $\kappa$. Otherwise continue at
E2 or stop with a negative structural result.
