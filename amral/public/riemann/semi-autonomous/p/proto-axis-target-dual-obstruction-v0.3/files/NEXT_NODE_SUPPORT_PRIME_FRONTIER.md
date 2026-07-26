# Next Node: RH Support–Prime Dual Frontier v0.4

## Decision

Do not spend another node increasing rank at $R=3$. The current PSD cone is
already blocked by explicit dual witnesses. Move the variable that the
obstruction diagnostic actually responds to: support radius and basis
geometry.

## Main question

For each support radius $R$, estimate a defensible lower-bound frontier

$$
L_P(R,\mathcal D,\mathcal T)
$$

for every patch $P$, basis dictionary $\mathcal D$, and theorem-object set
$\mathcal T$, while tracking the prime-side cost proxy

$$
C_{\mathrm{prime}}(R)\asymp e^{2R}.
$$

The goal is not merely to find $L_P<1$. It is to locate configurations where
dual escape, primal feasibility, prime-side computability, and theorem
certification can coexist.

## Work packages

### F1 — Parametric dual frontier

- Sweep $R\in[4.5,9]$ densely near observed transitions.
- Compare at least three basis densities and two bump-width schedules.
- Search single-band, three-band, and five-band nonnegative measures.
- Record both center and multi-point patch constraints.

### F2 — Dual-gated primal search

Only run expensive primal optimization when the strongest stable dual lower
bound is below $1$. Recheck each candidate against an independently refined
dual mesh.

### F3 — Prime-side cost engine

- Derive the precise support-to-prime cutoff relation for the chosen Fourier
  convention.
- Implement a segmented prime-power accumulator.
- Report wall time, memory, cutoff, and interval-error budget as functions of
  $R$.

### F4 — Theorem-ready count and tail

- Replace the $[18,23]$ floating count profile by a cited explicit bound.
- Replace the prototype tail matrix by a theorem-backed interval enclosure.
- Preserve downward rounding for lower-bound coefficients.

### F5 — Stop rules

- If a stable dual lower bound exceeds $1$ for every tested dictionary at a
  radius, do not run its primal search.
- If all-patch escape requires an intractable prime cutoff, redesign the
  dictionary or arithmetic decomposition before increasing $R$.
- Do not infer full-patch feasibility from center-only escape.
- Do not introduce known zero ordinates into optimization.

## First experiment

Use $R\in\{4.5,5.0,5.1,5.5,6.0,7.0,8.0,8.5\}$, basis densities
$6,8,10$ per unit, and tail fractions from $0$ through $10^{-3}$. Compute
tail-only and $A_1$-hybrid generalized-eigenvalue thresholds before any
nonconvex primal run.

## Success condition

A v0.4 positive result requires at least one configuration with:

1. stable all-patch dual lower bounds below $1$;
2. a primal candidate below the same finite budget;
3. a quantified prime-side execution plan;
4. no dependence on fitted known-zero ordinates.

Formal analytic claims still require interval transfer and theorem-backed
count/tail objects.
