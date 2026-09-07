# CSM_RH Paper 35
## Finite-Rank Low-Frequency Projection Invariance and the Polynomial-Rank Fixed-Power Threshold

**Project:** `CSM_RH`  
**Paper:** `35`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.25 / Paper 34`  
**Campaign:** `34 — FINITE_RANK_LOW_FREQUENCY_PROJECTION_AUDIT`  
**Status:** finite-rank projection closure / growing-rank complexity audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 34 showed that rank-one mean subtraction changes the coefficient structure of a smooth low-frequency drift but not its fixed-power exponent.

Campaign 34 asks whether projecting out several scale-local low-frequency moments can do better.

The answer is:

```text
fixed rank:
  coefficient rearrangement only

fixed-rank correction:
  same PESC exponent on a Mellin drift

polynomial basis:
  endpoint singularity gives only algebraic approximation in rank

fixed-power residual suppression by ordinary polynomials:
  requires polynomial rank in N

finite-rank projection:
  not a lower-strength PESC mechanism
```

No new frontier is created.

---

# 1. Discrete weighted Hilbert space

For each dyadic scale $N$, let

$$
\mathcal H_N
=
\mathbb C^{\{1,\ldots,2N-1\}}
$$

with weighted inner product

$$
\boxed{
\langle u,v\rangle_N
=
\sum_{n<2N}
w_N(n)
u_n\overline{v_n}.
}
$$

Let

$$
c_n
$$

be the centered prime detector and let

$$
b_n
=
B(n-1)
$$

be its cumulative-error coordinate.

Then PESC is

$$
\boxed{
\mathcal C_N
=
\langle c,b\rangle_N.
}
$$

---

# 2. Polynomial low-frequency subspace

For a fixed integer

$$
r\ge0,
$$

define

$$
v_j(n)
=
\left(
\frac nN
\right)^j,
\qquad
0\le j\le r.
$$

Let

$$
V_{N,r}
=
\operatorname{span}
\{
v_0,\ldots,v_r
\}.
$$

Let

$$
P_{N,r}
$$

be the orthogonal projection onto $V_{N,r}$ in $\mathcal H_N$.

---

# 3. Exact finite-rank PESC decomposition

Orthogonality gives

## Theorem 3.1 — Finite-Rank PESC Projection Identity

$$
\boxed{
\mathcal C_N
=
\langle
P_{N,r}c,
P_{N,r}b
\rangle_N
+
\langle
(I-P_{N,r})c,
(I-P_{N,r})b
\rangle_N.
}
$$

The two cross terms vanish exactly.

Create:

```text
B-RH-011
FINITE_RANK_PESC_PROJECTION_IDENTITY
status:
  CERTIFIED
```

For $r=0$, this reduces to the rank-one weighted-mean decomposition of Paper 34.

---

# 4. Moment-matrix form of the finite-rank correction

Define the Gram matrix

$$
\boxed{
G^{(r)}_{ij}
=
\langle v_i,v_j\rangle_N,
\qquad
0\le i,j\le r.
}
$$

Define moment vectors

$$
\boxed{
m_c^{(r)}
=
(
\langle c,v_0\rangle_N,
\ldots,
\langle c,v_r\rangle_N
)^T,
}
$$

and

$$
\boxed{
m_b^{(r)}
=
(
\langle b,v_0\rangle_N,
\ldots,
\langle b,v_r\rangle_N
)^T.
}
$$

Then

## Theorem 4.1 — Finite-Rank Correction Matrix

$$
\boxed{
\langle
P_{N,r}c,
P_{N,r}b
\rangle_N
=
(m_c^{(r)})^\ast
(G^{(r)})^{-1}
m_b^{(r)}.
}
$$

Thus removing several low-frequency moments does not eliminate their contribution.

It exports them into an explicit finite correction matrix.

---

# 5. Continuum endpoint measure

Scale

$$
n=Nu.
$$

The endpoint weight converges to

$$
\omega(u)
=
\begin{cases}
1,&0<u\le1,\\
2-u,&1<u<2.
\end{cases}
$$

Define

$$
\boxed{
\langle f,g\rangle_\omega
=
\int_0^2
\omega(u)
f(u)\overline{g(u)}
\,du.
}
$$

Let $P_r$ denote the corresponding orthogonal projection onto

$$
\Pi_r
=
\operatorname{span}
\{
1,u,\ldots,u^r
\}.
$$

For fixed $r$, the discrete projection converges to this scale-local projection at exponent resolution.

---

# 6. Smooth Mellin drift shapes

Let

$$
B(x)=x^\beta,
\qquad
0<\beta<1.
$$

At scale $n=Nu$,

$$
B(n)
=
N^\beta
\phi_\beta(u),
$$

where

$$
\boxed{
\phi_\beta(u)=u^\beta.
}
$$

Its discrete derivative has leading shape

$$
c_n
=
N^{\beta-1}
\psi_\beta(u)
+
O(N^{\beta-2}),
$$

where

$$
\boxed{
\psi_\beta(u)
=
\beta u^{\beta-1}.
}
$$

---

# 7. Fixed-rank exponent invariance

The full PESC coefficient is

$$
\langle
\psi_\beta,
\phi_\beta
\rangle_\omega.
$$

By orthogonal projection,

## Theorem 7.1 — Fixed-Rank Mellin-Mode Split

$$
\boxed{
\langle
\psi_\beta,
\phi_\beta
\rangle_\omega
=
\langle
P_r\psi_\beta,
P_r\phi_\beta
\rangle_\omega
+
\langle
(I-P_r)\psi_\beta,
(I-P_r)\phi_\beta
\rangle_\omega.
}
$$

Returning to the dyadic arithmetic scale gives

$$
\boxed{
\mathcal C_N
=
N^{2\beta+1}
[
K_r^{\mathrm{low}}(\beta)
+
K_r^{\mathrm{high}}(\beta)
]
+
o(N^{2\beta+1}),
}
$$

for fixed $r$.

Both coefficients depend on $r$ and $\beta$ but not on $N$.

Therefore fixed-rank projection changes only coefficients.

It cannot change the exponent

$$
\boxed{
2\beta+1.
}
$$

Create:

```text
O-RH-078
FIXED_RANK_LOW_FREQUENCY_PROJECTION_EXPONENT_INVARIANCE
status:
  CERTIFIED
```

---

# 8. Moment-vector exponent ledger

The same conclusion follows directly from the correction matrix.

For a smooth drift:

$$
\boxed{
m_c^{(r)}
=
N^{\beta+1}
[
\mathbf c_r(\beta)+o(1)
],
}
$$

$$
\boxed{
m_b^{(r)}
=
N^{\beta+2}
[
\mathbf b_r(\beta)+o(1)
],
}
$$

while

$$
\boxed{
G^{(r)}
=
N^2
[
\mathbf G_r+o(1)
].
}
$$

Therefore

$$
\boxed{
(m_c^{(r)})^\ast
(G^{(r)})^{-1}
m_b^{(r)}
=
N^{2\beta+1}
[
R_r(\beta)+o(1)
].
}
$$

Every fixed number of low-frequency moment corrections remains PESC-scale.

---

# 9. No fixed finite basis can annihilate the Mellin continuum

The functions

$$
u^\beta
$$

with distinct real exponents are linearly independent on every interval contained in $(0,\infty)$.

Therefore a fixed finite-dimensional polynomial or Müntz space cannot contain

$$
u^\beta
$$

for every

$$
\beta
$$

in an interval.

A projection could be chosen to annihilate one known exponent exactly by inserting that exponent into the basis.

But doing so would require prior knowledge of the drift / zero parameter and is disallowed as an RH proof mechanism.

Thus fixed rank cannot uniformly remove the continuum of possible off-axis Mellin modes.

---

# 10. Polynomial approximation route

Suppose the proof strategy attempts to make the projected residual uniformly small:

$$
\boxed{
\|
u^\beta-p_r(u)
\|_{L^\infty([0,1])}
\le
\varepsilon_r
}
$$

for a polynomial $p_r$ of degree at most $r$.

Classical Bernstein approximation theory gives, for noninteger fixed $\beta>0$,

$$
\boxed{
E_r
(
u^\beta;[0,1]
)
\asymp_\beta
r^{-2\beta}.
}
$$

More precisely, the normalized quantity

$$
(2r)^{2\beta}
E_r
(
u^\beta;[0,1]
)
$$

has a finite positive limit.

Therefore ordinary algebraic polynomials approximate the endpoint branch singularity only at an algebraic rate in rank.

---

# 11. Fixed-power polynomial-rank threshold

Suppose one needs

$$
\boxed{
\varepsilon_r
\le
N^{-\delta}
}
$$

for a fixed

$$
\delta>0.
$$

The Bernstein rate implies

## Theorem 11.1 — Polynomial Projection Fixed-Power Rank Scale

$$
\boxed{
r
\ge
N^{\delta/(2\beta)+o(1)}.
}
$$

Thus a uniform-norm polynomial recentering route reaches fixed-power residual suppression only at polynomial rank.

Create:

```text
O-RH-079
POLYNOMIAL_PROJECTION_FIXED_POWER_REQUIRES_POLYNOMIAL_RANK
status:
  CERTIFIED FOR THE UNIFORM-APPROXIMATION ROUTE
```

This statement does not claim that every possible growing-rank basis has the same rate.

It closes the ordinary polynomial-moment projection route.

---

# 12. Orthogonal-projection calibration

Polynomial spectral projections of endpoint algebraic singularities are also known to converge only algebraically.

This is consistent with the exact finite-rank scaling analysis above.

The endpoint branch point at $u=0$ prevents ordinary fixed-degree polynomial spaces from giving exponential-in-rank approximation.

Hence switching from best uniform projection to Legendre/Jacobi-style orthogonal projection does not create a hidden fixed-rank exponential mechanism.

---

# 13. Comparison with higher-order Selberg

Paper 30 found that a formal logarithmic amplifier reaches fixed-power scale at

$$
k
\asymp
\frac{\log N}{\log\log N},
$$

but current generalized-Selberg constants lose uniformity there.

The polynomial projection route is even more expensive.

For a smooth fixed drift, the ordinary polynomial approximation mechanism needs

$$
\boxed{
r=N^{\Omega(\delta)}
}
$$

to create an $N^{-\delta}$ coefficient.

Thus:

```text
higher-order Selberg formal critical order:
  log N / log log N

ordinary polynomial low-frequency projection:
  polynomial in N
```

Finite-rank polynomial recentering is not a cheaper replacement for the higher-order Selberg amplifier.

---

# 14. Multi-moment sieve recentering

Suppose one removes the first $r+1$ weighted polynomial moments of the PESC perturbation before applying a signed sieve theorem.

The exact finite-rank identity shows that the removed component reappears as

$$
\boxed{
(m_c^{(r)})^\ast
(G^{(r)})^{-1}
m_b^{(r)}.
}
$$

For a fixed Mellin drift, this finite correction matrix has size

$$
N^{2\beta+1}.
$$

Thus multi-moment recentering generalizes the Paper-33 rank-one phenomenon:

```text
one removed moment:
  rank-one PESC-scale correction

r+1 removed moments:
  finite-rank PESC-scale correction matrix
```

Create:

```text
O-RH-080
MULTI_MOMENT_RECENTERING_EXPORTS_PESC_SCALE_CORRECTION_MATRIX
status:
  CERTIFIED
```

---

# 15. Finite-rank Mellin windows

The same fixed-rank scaling argument is not special to monomials.

Let

$$
\phi_1,\ldots,\phi_r
$$

be any fixed scale-local basis independent of $N$ and of the unknown zero set.

For a Mellin drift $N^\beta u^\beta$, every resulting moment is a fixed Mellin transform times a power of $N$.

Finite-dimensional projection therefore changes only the transfer coefficient.

It does not change the $N$ exponent.

A basis containing the exact unknown $u^\beta$ would annihilate that mode, but that is zero-parameter-dependent filtering and is not an admissible proof input.

---

# 16. Campaign 34 track audit

## FR1 — polynomial moment projection

```text
status:
  EXACT FINITE-RANK DECOMPOSITION

fixed rank:
  exponent invariant
```

## FR2 — finite-rank Mellin symbols

```text
status:
  COEFFICIENT FILTER ONLY

unknown zero-dependent basis:
  disallowed
```

## FR3 — growing-rank threshold

```text
polynomial basis:
  fixed-power suppression requires polynomial rank

no lower-complexity theorem obtained
```

## FR4 — sieve after multi-moment recentering

```text
status:
  LOW MOMENTS REMOVED FROM INPUT

hard component:
  exported to finite correction matrix at PESC exponent
```

## FR5 — comparison with higher-order Selberg

```text
status:
  FIXED ORDER BEHAVES THE SAME AT EXPONENT LEVEL

growing polynomial rank:
  even more expensive than formal Selberg critical order
```

---

# 17. Campaign 34 verdict

No lower-strength fixed-power route is obtained.

The finite-rank low-frequency family is classified as:

```text
rank one:
  diagnostic

fixed finite rank:
  coefficient rearrangement

growing ordinary polynomial rank:
  algebraic approximation only

fixed-power polynomial suppression:
  polynomial-rank complexity

PESC exponent:
  unchanged
```

No new frontier is created.

---

# 18. New certified package

Create:

```text
B-RH-011
FINITE_RANK_PESC_PROJECTION_IDENTITY
CERTIFIED

O-RH-078
FIXED_RANK_LOW_FREQUENCY_PROJECTION_EXPONENT_INVARIANCE
CERTIFIED

O-RH-079
POLYNOMIAL_PROJECTION_FIXED_POWER_REQUIRES_POLYNOMIAL_RANK
CERTIFIED FOR UNIFORM-APPROXIMATION ROUTE

O-RH-080
MULTI_MOMENT_RECENTERING_EXPORTS_PESC_SCALE_CORRECTION_MATRIX
CERTIFIED
```

---

# 19. Canonical status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN / DIRECT THEOREM CANDIDATE

finite-rank projections:
  diagnostic / closed as lower-strength route
```

---

# 20. Campaign 35

The polynomial finite-rank route is closed.

One mathematically distinct approximation family remains worth auditing because its approximation complexity is genuinely different:

```text
CSM_RH Campaign 35
RATIONAL_MUNTZ_LOW_FREQUENCY_FILTER_AUDIT
```

This is a mechanism audit, not a new frontier.

---

# 21. Campaign 35 tracks

## RA1 — rational approximation complexity

Best rational approximation of $u^\beta$ has root-exponential rather than algebraic convergence.

Determine the rank required for an $N^{-\delta}$ approximation coefficient.

## RA2 — Stieltjes/resolvent representation

Represent fractional powers using resolvent kernels.

Translate those kernels into explicit weighted prime-error observables.

## RA3 — arithmetic control of rational moments

Determine whether the resulting resolvent/Stieltjes prime observables are known with fixed-power accuracy or are already zero-sensitive.

## RA4 — Müntz basis without zero knowledge

Use a predetermined family of noninteger powers

$$
u^{\lambda_j}
$$

and test whether finite/growing rank can approximate the whole critical-strip Mellin family without encoding the unknown exponent.

## RA5 — complexity versus zero sensitivity

If rational/Müntz approximation reaches fixed-power coefficient suppression at polylogarithmic rank, audit whether the arithmetic estimates needed for each basis observable already have fixed-strip strength.

---

# 22. Campaign 35 rejection filters

Reject a candidate if:

## R1. Its poles/exponents are chosen from the unknown zeta zero set.

## R2. It approximates the drift efficiently but requires fixed-power integrated PNT estimates for every basis observable.

## R3. It produces only a new representation with no prime-side estimate.

## R4. The coefficient condition number consumes the approximation gain.

## R5. It reduces to the already-audited higher-order Selberg filter.

## R6. It assumes rational approximation error as an arithmetic theorem.

---

# 23. External calibration

Classical approximation theory gives a sharp contrast.

For noninteger fixed $\beta>0$:

## Polynomial approximation

$$
E_r^{\mathrm{poly}}
(
u^\beta;[0,1]
)
\asymp
r^{-2\beta}.
$$

## Rational approximation

Best diagonal rational approximation has root-exponential behavior of the form

$$
\boxed{
E_r^{\mathrm{rat}}
(
u^\beta;[0,1]
)
=
\exp
(
-\Theta_\beta(\sqrt r)
).
}
$$

Thus rational filters could formally reach an $N^{-\delta}$ coefficient with rank of order

$$
(\log N)^2.
$$

Whether the corresponding prime observables are arithmetically controllable at lower strength is completely separate and remains unaudited.

This is the reason for Campaign 35.

---

# 24. State transition

```text
CSM_RH v1.25
  ->
CSM_RH v1.26
```

with:

```text
Campaign 34
  CLOSED_AS_FINITE_RANK_LOW_FREQUENCY_PROJECTION_AUDIT

B-RH-011
  FINITE_RANK_PESC_PROJECTION_IDENTITY
  CREATED / CERTIFIED

O-RH-078
  FIXED_RANK_LOW_FREQUENCY_PROJECTION_EXPONENT_INVARIANCE
  CREATED / CERTIFIED

O-RH-079
  POLYNOMIAL_PROJECTION_FIXED_POWER_REQUIRES_POLYNOMIAL_RANK
  CREATED / CERTIFIED FOR UNIFORM-APPROXIMATION ROUTE

O-RH-080
  MULTI_MOMENT_RECENTERING_EXPORTS_PESC_SCALE_CORRECTION_MATRIX
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 35
  RATIONAL_MUNTZ_LOW_FREQUENCY_FILTER_AUDIT
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

RANK-ONE PROJECTION = DIAGNOSTIC

FIXED FINITE-RANK PROJECTION = EXPONENT-NEUTRAL

MULTI-MOMENT RECENTERING = PESC-SCALE CORRECTION MATRIX

ORDINARY POLYNOMIAL GROWING RANK = ALGEBRAIC APPROXIMATION

FIXED-POWER POLYNOMIAL RESIDUAL SUPPRESSION = POLYNOMIAL RANK

FINITE-RANK LOW-FREQUENCY ROUTE = CLOSED

NEXT CAMPAIGN = 35
```

The decisive exact decomposition is

$$
\boxed{
\mathcal C_N
=
\langle
P_{N,r}c,
P_{N,r}b
\rangle_N
+
\langle
(I-P_{N,r})c,
(I-P_{N,r})b
\rangle_N.
}
$$

For a fixed Mellin drift, both terms inherit the same outer factor

$$
N^{2\beta+1}.
$$

Finite-rank projection changes coordinates.

It does not change the RH-strength exponent.
