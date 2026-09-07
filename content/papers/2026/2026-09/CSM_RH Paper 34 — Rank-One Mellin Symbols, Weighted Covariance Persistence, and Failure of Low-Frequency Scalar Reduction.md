# CSM_RH Paper 34
## Rank-One Mellin Symbols, Weighted Covariance Persistence, and Failure of Low-Frequency Scalar Reduction

**Project:** `CSM_RH`  
**Paper:** `34`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.24 / Paper 33`  
**Campaign:** `33 — PESC_LOW_FREQUENCY_RANK_ONE_ATTACK`  
**Status:** low-frequency scalar / covariance decomposition audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 33 exposed the rank-one scalar

$$
\mathcal R_N^{(1)}
=
\frac{H_NG_N}{W_N}
$$

after mean-zero recentering of the PESC perturbation.

Campaign 33 asks whether this scalar is a lower-strength low-frequency target which can be controlled more easily than full PESC.

The answer is negative.

The rank-one term is genuinely sensitive to fixed Mellin drift modes, but the centered covariance remainder retains the same polynomial exponent for every fixed smooth drift $x^\beta$ with $0<\beta<1$.

Thus the decomposition changes coefficients, not the fixed-power exponent class.

No new frontier is created.

---

# 1. Weighted PESC decomposition

Let

$$
B(j)
=
\sum_{n\le j}c_n
$$

and define the canonical endpoint weight

$$
w_N(n)
=
\begin{cases}
N,&n\le N,\\
2N-n,&N<n<2N,\\
0,&n\ge2N.
\end{cases}
$$

Define

$$
\boxed{
W_N
=
\sum_{n<2N}w_N(n)
=
\frac{3N^2-N}{2}.
}
$$

Define

$$
\boxed{
H_N
=
\sum_{n<2N}
w_N(n)B(n-1),
}
$$

and

$$
\boxed{
G_N
=
\sum_{n<2N}
w_N(n)c_n
=
\sum_{j=N}^{2N-1}B(j).
}
$$

The canonical PESC self-correlation is

$$
\boxed{
\mathcal C_N
=
\sum_{n<2N}
w_N(n)c_nB(n-1).
}
$$

Define weighted means

$$
\overline B_N
=
\frac{H_N}{W_N},
$$

$$
\overline c_N
=
\frac{G_N}{W_N}.
$$

Then:

## Theorem 1.1 — Exact Weighted Covariance Decomposition

$$
\boxed{
\mathcal C_N
=
\sum_{n<2N}
w_N(n)
[
c_n-\overline c_N
]
[
B(n-1)-\overline B_N
]
+
\frac{
H_NG_N
}{
W_N
}.
}
$$

The first term is the weighted centered covariance.

The second term is the rank-one mean product from Paper 33.

Create:

```text
B-RH-010
PESC_WEIGHTED_COVARIANCE_RANK_ONE_DECOMPOSITION
status:
  CERTIFIED
```

---

# 2. Continuous endpoint kernel

At exponent resolution, scale

$$
n=Nu.
$$

The endpoint weight becomes

$$
w_N(n)
=
N\omega(u)
+
O(1),
$$

where

$$
\boxed{
\omega(u)
=
\begin{cases}
1,&0<u\le1,\\
2-u,&1<u<2,\\
0,&u\ge2.
\end{cases}
}
$$

Define its Mellin moment

$$
\boxed{
I(s)
=
\int_0^2
\omega(u)u^s\,du.
}
$$

For

$$
\Re s>-1,
$$

a direct calculation gives:

## Theorem 2.1 — Endpoint Mellin Symbol

$$
\boxed{
I(s)
=
\frac{
2^{s+2}-1
}{
(s+1)(s+2)
}.
}
$$

In particular,

$$
\boxed{
I(0)=\frac32.
}
$$

---

# 3. Dyadic first-primitive symbol

Test a Mellin mode

$$
\boxed{
B(x)=c x^\rho,
}
$$

with

$$
0<\beta=\Re\rho<1.
$$

The first primitive observable is

$$
G_N
=
\sum_{j=N}^{2N-1}B(j).
$$

At exponent level,

$$
\boxed{
G_N
=
c
g(\rho)
N^{\rho+1}
+
O_\rho(N^\beta),
}
$$

where

$$
\boxed{
g(\rho)
=
\int_1^2u^\rho\,du
=
\frac{
2^{\rho+1}-1
}{
\rho+1
}.
}
$$

For $0<\Re\rho<1$,

$$
\boxed{
g(\rho)\ne0.
}
$$

Indeed,

$$
|2^{\rho+1}|
=
2^{\beta+1}
>
1.
$$

Thus the numerator cannot vanish.

---

# 4. Second-integrated endpoint symbol

The rank-one factor $H_N$ has exponent-level form

$$
\boxed{
H_N
=
c
h(\rho)
N^{\rho+2}
+
O_\rho(N^{\beta+1}),
}
$$

where

$$
\boxed{
h(\rho)
=
I(\rho)
=
\frac{
2^{\rho+2}-1
}{
(\rho+1)(\rho+2)
}.
}
$$

Again,

$$
\boxed{
h(\rho)\ne0
}
$$

throughout the critical strip because

$$
|2^{\rho+2}|
=
2^{\beta+2}
>
1.
$$

Therefore neither linear factor of the rank-one scalar has a Mellin blind spot in the critical strip.

---

# 5. Relation with the standard integrated explicit formula

For the von-Mangoldt error

$$
E(x)=\psi(x)-x,
$$

define

$$
\psi_1(x)
=
\int_0^x\psi(t)\,dt.
$$

The classical explicit formula is

$$
\boxed{
\psi_1(x)
=
\frac{x^2}{2}
-
\sum_\rho
\frac{
x^{\rho+1}
}{
\rho(\rho+1)
}
+
\text{elementary lower-order terms}.
}
$$

The zero series converges absolutely because

$$
\sum_\rho|\rho|^{-2}<\infty.
$$

Thus integration genuinely smooths the zero packet while preserving every zero exponent.

A standard isolated-off-line-zero calibration gives

$$
\boxed{
\psi_1(x)
=
\frac{x^2}{2}
+
C_\rho
x^{1+\beta}
\cos
(
\gamma\log x+\phi_\rho
)
+
O(x^{3/2})
}
$$

when one zero pair $\beta\pm i\gamma$, $\beta>1/2$, is the only pair to the right of the critical line.

This is classical calibration, not a hypothesis used to prove RH.

---

# 6. Rank-one response to one conjugate mode

Let the real drift associated with one conjugate pair be

$$
B_\rho(x)
=
c x^\rho
+
\overline c x^{\overline\rho}.
$$

Then

$$
G_N
=
2
|c g(\rho)|
N^{\beta+1}
\cos
(
\gamma\log N+\phi_g
)
+
o(N^{\beta+1}),
$$

and

$$
H_N
=
2
|c h(\rho)|
N^{\beta+2}
\cos
(
\gamma\log N+\phi_h
)
+
o(N^{\beta+2}).
$$

Since

$$
W_N
=
\frac32N^2
+
O(N),
$$

the rank-one scalar is

$$
\boxed{
\mathcal R_N^{(1)}
=
\frac83
|c|^2
|g(\rho)h(\rho)|
N^{2\beta+1}
\cos(\theta_N+\phi_g)
\cos(\theta_N+\phi_h)
+
o(N^{2\beta+1}),
}
$$

where

$$
\theta_N=\gamma\log N.
$$

---

# 7. No phase escape for a single mode

For any real phase difference $\Delta$,

$$
\cos\theta\cos(\theta+\Delta)
=
\frac12
[
\cos(2\theta+\Delta)
+
\cos\Delta
].
$$

Therefore

## Theorem 7.1 — Product-Phase Maximum

$$
\boxed{
\max_\theta
|
\cos\theta\cos(\theta+\Delta)
|
=
\frac{
1+|\cos\Delta|
}{2}
\ge
\frac12.
}
$$

Hence the rank-one response of one nonzero conjugate Mellin mode is not identically small.

For continuous scale $N$ there are arbitrarily large scales with

$$
\boxed{
|\mathcal R_N^{(1)}|
\gg_\rho
N^{2\beta+1}.
}
$$

Integer-scale approximation preserves the same exponent.

Thus a uniform fixed-power rank-one upper bound already has isolated-zero fixed-strip strength.

Create:

```text
O-RH-075
RANK_ONE_ISOLATED_MELLIN_MODE_FIXED_STRIP_LOCK
status:
  CERTIFIED AS FIXED-MODE STRENGTH AUDIT
```

This is not a full multiple-zero coefficient-isolation theorem.

---

# 8. Real smooth power drift

Now take the nonoscillatory strength model

$$
\boxed{
B(x)=x^\beta,
\qquad
0<\beta<1.
}
$$

Then

$$
c_n
=
B(n)-B(n-1)
=
\beta n^{\beta-1}
+
O_\beta(n^{\beta-2}).
$$

The endpoint Mellin symbol gives:

## Total PESC

$$
\boxed{
\mathcal C_N
=
K(\beta)
N^{2\beta+1}
+
o(N^{2\beta+1}),
}
$$

with

$$
\boxed{
K(\beta)
=
\beta I(2\beta-1)
=
\frac{
2^{2\beta+1}-1
}{
2(2\beta+1)
}.
}
$$

---

# 9. Rank-one coefficient for a smooth drift

We have

$$
H_N
=
I(\beta)
N^{\beta+2}
+
o(N^{\beta+2}),
$$

$$
G_N
=
\beta I(\beta-1)
N^{\beta+1}
+
o(N^{\beta+1}),
$$

and

$$
W_N
=
I(0)N^2
+
o(N^2).
$$

Therefore

## Theorem 9.1 — Smooth-Drift Rank-One Coefficient

$$
\boxed{
\mathcal R_N^{(1)}
=
R(\beta)
N^{2\beta+1}
+
o(N^{2\beta+1}),
}
$$

where

$$
\boxed{
R(\beta)
=
\frac{
\beta I(\beta)I(\beta-1)
}{
I(0)
}.
}
$$

Thus the rank-one term has exactly the same polynomial exponent as full PESC.

---

# 10. Centered covariance coefficient

Define

$$
\boxed{
Q(\beta)
=
K(\beta)-R(\beta).
}
$$

Then the centered covariance term satisfies

$$
\boxed{
\operatorname{Cov}_{w_N}(c,B)
=
Q(\beta)
N^{2\beta+1}
+
o(N^{2\beta+1}).
}
$$

The two pieces therefore share the same exponent.

---

# 11. Strict sign of the covariance

Under the positive measure

$$
d\mu(u)
=
\omega(u)\,du,
$$

the two functions

$$
u^\beta
$$

and

$$
\beta u^{\beta-1}
$$

have opposite monotonicity for

$$
0<\beta<1.
$$

The first is strictly increasing.

The second is strictly decreasing.

The weighted covariance inequality therefore gives:

## Theorem 11.1 — Smooth-Drift Covariance Persistence

For every fixed

$$
0<\beta<1,
$$

$$
\boxed{
Q(\beta)<0.
}
$$

In particular,

$$
\boxed{
Q(\beta)\ne0.
}
$$

Thus mean-zero recentering does not eliminate the fixed-power smooth mode from the covariance sector.

Create:

```text
O-RH-076
CENTERED_COVARIANCE_RETAINS_SMOOTH_DRIFT_EXPONENT
status:
  CERTIFIED
```

---

# 12. Near-linear limit

At

$$
\beta=1,
$$

the derivative of the drift is constant.

The weighted covariance therefore vanishes exactly:

$$
\boxed{
Q(1)=0.
}
$$

As

$$
\beta\uparrow1,
$$

$$
\boxed{
Q(\beta)\to0.
}
$$

Meanwhile

$$
R(\beta)\to K(\beta).
$$

Thus the rank-one term captures an increasingly large fraction of a near-linear drift.

This explains why the Section-6 zeroth-mode leakage found in Paper 33 is a natural low-frequency obstruction.

But for every fixed $\beta<1$, the covariance coefficient remains nonzero and the exponent remains $2\beta+1$.

---

# 13. Rank-one is not a complete PESC coordinate

The decomposition

$$
\mathcal C_N
=
\operatorname{Cov}_{w_N}(c,B)
+
\mathcal R_N^{(1)}
$$

does not reduce PESC to the rank-one scalar.

For a fixed smooth mode:

```text
rank-one term:
  N^(2 beta+1)

centered covariance:
  N^(2 beta+1)

full PESC:
  N^(2 beta+1)
```

Only the coefficients differ.

Therefore controlling the rank-one scalar alone does not supply a fixed-power PESC theorem.

Create:

```text
O-RH-077
RANK_ONE_SCALAR_NOT_A_COMPLETE_PESC_COORDINATE
status:
  CERTIFIED BY SMOOTH-DRIFT COUNTERMODEL
```

---

# 14. Current sieve control of the covariance remains subpower

The centered perturbation has zero weighted mean.

This removes the classical zeroth-mode leakage from the coupled-sieve input.

However the covariance term remains an endogenous signed prime correlation.

Current sieve / higher-uniformity technology gives logarithmic or subpower precision for the relevant prime residual inputs.

Since the covariance smooth-mode contribution has the same $N^{2\beta+1}$ exponent, arbitrary logarithmic control does not produce a fixed PESC exponent.

Thus mean-zero sieve stability does not close the covariance sector.

---

# 15. Fixed-power bounds on the linear factors

The symbols

$$
g(\rho)
$$

and

$$
h(\rho)
$$

have no zeros in the critical strip.

Therefore fixed-power control of either linear observable over all scales would be strongly zero-sensitive.

The classical explicit formula for the first integrated prime error confirms this directly for isolated off-line zeros.

Thus the factors

$$
G_N,
\qquad
H_N
$$

are not cheap low-frequency quantities whose fixed-power bounds are known independently of the PESC problem.

---

# 16. Multiple-zero caveat

For a general zero packet, $G_N$ and $H_N$ are log-scale exponential sums.

Their product may have substantial phase cancellation at individual scales.

The present campaign does not prove a universal coefficient-isolation theorem for the rank-one product.

This is another reason not to promote

$$
\mathcal R_N^{(1)}
$$

to a canonical frontier.

The fixed-mode audit is sufficient to show that the scalar is not obviously lower-strength.

---

# 17. Campaign 33 track audit

## ZM1 — first/second primitive Mellin analysis

```text
status:
  COMPLETE AT FIXED-MODE LEVEL

symbols:
  g(rho), h(rho)

critical-strip zeros:
  none
```

## ZM2 — scalar-product cancellation

```text
status:
  NO UNIFORM FREE CANCELLATION

single mode:
  Omega(N^(2 beta+1)) on subsequences
```

## ZM3 — dyadic phase variation

```text
status:
  PRODUCT OSCILLATES

phase zeros:
  possible at isolated scales

uniform fixed-power escape:
  not available
```

## ZM4 — arithmetic control of first primitive

```text
status:
  CURRENT UNCONDITIONAL CONTROL SUBPOWER

fixed-power control:
  zero-sensitive / unavailable
```

## ZM5 — direct covariance decomposition

```text
status:
  EXACT

centered covariance:
  retains same smooth-drift exponent
```

---

# 18. Campaign 33 verdict

The rank-one scalar is useful diagnostically but is not a lower-strength replacement for PESC.

The low-frequency decomposition produces:

```text
rank-one mean product:
  captures most near-linear drift

mean-zero covariance:
  smaller coefficient near beta=1
  but same fixed polynomial exponent

fixed-power theorem:
  still absent
```

No new frontier is created.

The canonical root remains PESC.

---

# 19. New certified package

Create:

```text
B-RH-010
PESC_WEIGHTED_COVARIANCE_RANK_ONE_DECOMPOSITION
CERTIFIED

O-RH-075
RANK_ONE_ISOLATED_MELLIN_MODE_FIXED_STRIP_LOCK
CERTIFIED AS FIXED-MODE STRENGTH AUDIT

O-RH-076
CENTERED_COVARIANCE_RETAINS_SMOOTH_DRIFT_EXPONENT
CERTIFIED

O-RH-077
RANK_ONE_SCALAR_NOT_A_COMPLETE_PESC_COORDINATE
CERTIFIED
```

---

# 20. Canonical status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN / DIRECT THEOREM CANDIDATE

rank-one scalar:
  diagnostic only

mean-zero covariance:
  diagnostic subcomponent
```

---

# 21. Campaign 34

The next campaign is:

```text
CSM_RH Campaign 34
FINITE_RANK_LOW_FREQUENCY_PROJECTION_AUDIT
```

This campaign tests one final natural extension of the rank-one idea:

> can projecting out several low-frequency polynomial/Mellin moments make the remaining signed covariance genuinely easier at fixed exponent?

No new frontier may be created unless the projection produces a proved fixed-power bridge weaker than PESC.

---

# 22. Campaign 34 tracks

## FR1 — polynomial moment projection

Project the cumulative error against

$$
1,u,u^2,\ldots,u^r
$$

under the endpoint weight.

Compute the response of a drift $u^\beta$.

## FR2 — finite-rank Mellin symbols

Use a finite family of scale-local Mellin windows.

Determine whether any fixed rank can change the exponent $2\beta+1$, rather than only its coefficient.

## FR3 — growing-rank threshold

If fixed rank only creates coefficient zeros at $\beta=1$, determine the rank growth needed to turn coefficient suppression into an $X$ -power.

Track condition number and arithmetic complexity.

## FR4 — sieve after multi-moment recentering

Test whether eliminating several signed low moments removes all classical asymptotic-sieve leakage terms or merely exports them into a finite-rank correction matrix.

## FR5 — direct comparison with higher-order Selberg

Determine whether finite-rank recentering is mathematically distinct from the already-audited higher-order generalized Selberg amplifier.

---

# 23. Campaign 34 rejection filters

Reject a candidate if:

## R1. Fixed rank changes only coefficients, not exponents.

## R2. Growing rank reaches the same log X/log log X complexity threshold as Paper 30 without new uniformity.

## R3. The projection uses the unknown zero set.

## R4. The finite-rank correction matrix contains PESC-scale Mellin modes.

## R5. The result is merely another representation of the same low-frequency drift.

## R6. It assumes fixed-power integrated PNT estimates.

---

# 24. External calibration

The fixed-mode calibration is consistent with standard explicit-formula theory.

The first integrated Chebyshev function has an absolutely convergent zero expansion:

$$
\psi_1(x)
=
\frac{x^2}{2}
-
\sum_\rho
\frac{x^{\rho+1}}{\rho(\rho+1)}
+
\text{lower-order terms}.
$$

A single hypothetical zero pair with real part $\beta>1/2$ produces a term of size

$$
x^{1+\beta}\cos(\gamma\log x).
$$

Thus integrated low-frequency observables remain directly sensitive to off-critical zeros; integration damps high ordinates but does not improve the real exponent.

---

# 25. State transition

```text
CSM_RH v1.24
  ->
CSM_RH v1.25
```

with:

```text
Campaign 33
  CLOSED_AS_RANK_ONE_AND_COVARIANCE_STRENGTH_AUDIT

B-RH-010
  PESC_WEIGHTED_COVARIANCE_RANK_ONE_DECOMPOSITION
  CREATED / CERTIFIED

O-RH-075
  RANK_ONE_ISOLATED_MELLIN_MODE_FIXED_STRIP_LOCK
  CREATED / CERTIFIED AS FIXED-MODE STRENGTH AUDIT

O-RH-076
  CENTERED_COVARIANCE_RETAINS_SMOOTH_DRIFT_EXPONENT
  CREATED / CERTIFIED

O-RH-077
  RANK_ONE_SCALAR_NOT_A_COMPLETE_PESC_COORDINATE
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 34
  FINITE_RANK_LOW_FREQUENCY_PROJECTION_AUDIT
  READY
```

---

# 26. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

RANK-ONE LOW-FREQUENCY SCALAR = DIAGNOSTIC

RANK-ONE FIXED-MODE RESPONSE = FIXED-STRIP SCALE

MEAN-ZERO COVARIANCE = SAME POWER EXPONENT ON SMOOTH DRIFT

LOW-FREQUENCY SPLIT = COEFFICIENT REARRANGEMENT, NOT EXPONENT REDUCTION

NEXT CAMPAIGN = 34
```

The central coefficient law is

$$
\boxed{
\mathcal C_N
=
[
Q(\beta)+R(\beta)
]
N^{2\beta+1}
+
o(N^{2\beta+1}),
}
$$

with

$$
\boxed{
Q(\beta)<0,
\qquad
R(\beta)>0,
\qquad
0<\beta<1.
}
$$

Both pieces preserve the same fixed-power exponent.

The rank-one projection therefore isolates a low-frequency component, but it does not reduce the RH-strength exponent class.
