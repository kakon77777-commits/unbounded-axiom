# CSM_RH Paper 29
## Residual Selberg Forcing Criticality and the Failure of Elementary Drift Coercivity

**Project:** `CSM_RH`  
**Paper:** `29`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.19 / Paper 28`  
**Campaign:** `28 — ENDOGENOUS_DRIFT_COERCIVITY_ATTACK`  
**Status:** residual Selberg / multiplicative drift / two-scale coercivity audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 28 proved that subtracting the modern sieve model $\Lambda^\sharp$ is fixed-exponent neutral for PESC.

Campaign 28 asks whether classical prime-side multiplicative feedback, especially Selberg symmetry, can directly coerce the residual primitive

$$
F(x)
=
\sum_{n\le x}
[
\Lambda(n)-\Lambda^\sharp(n)
]
$$

against a persistent Mellin drift

$$
F(x)\approx c x^\rho,
\qquad
\Re\rho<1.
$$

The answer for the audited fixed-order Selberg feedback is negative.

The residual Selberg equation sees the drift, but the positive sieve/model sampling channel sends every fixed Mellin mode into the same $1/\log x$ forcing scale already allowed by the classical symmetry formula.

No fixed drift gap is produced.

---

# 1. Classical Selberg remainder equation

Let

$$
A(x)=\psi(x)-x.
$$

Selberg's symmetry formula gives

$$
\boxed{
A(x)
+
\frac1{\log x}
\sum_{n\le x}
\Lambda(n)
A(x/n)
=
O
\left(
\frac{x}{\log x}
\right).
}
$$

This is the standard remainder form of the elementary Selberg prime-number-theorem feedback.

---

# 2. Sieve residual decomposition

Use Paper 28:

$$
A(x)=F(x)+B(x),
$$

where

$$
F(x)
=
\sum_{n\le x}
[
\Lambda(n)-\Lambda^\sharp(n)
]
$$

and

$$
B(x)
=
\sum_{n\le x}
[
\Lambda^\sharp(n)-1
].
$$

Paper 28 certified

$$
\boxed{
\sup_{x\le 2X}|B(x)|
=
X^{o(1)}.
}
$$

Substitute into Selberg symmetry.

Using Chebyshev's bound

$$
\psi(x)\ll x,
$$

we obtain:

## Theorem 2.1 — Residual Selberg Symmetry

Uniformly for $x\asymp X$,

$$
\boxed{
F(x)
+
\frac1{\log x}
\sum_{n\le x}
\Lambda(n)
F(x/n)
=
O
\left(
\frac{x^{1+o(1)}}{\log x}
\right).
}
$$

Splitting

$$
\Lambda=\Lambda^\sharp+f,
\qquad
f=\Lambda-\Lambda^\sharp,
$$

gives

$$
\boxed{
F(x)
+
\frac1{\log x}
\sum_{n\le x}
\Lambda^\sharp(n)F(x/n)
+
\frac1{\log x}
\sum_{n\le x}
f(n)F(x/n)
=
O
\left(
\frac{x^{1+o(1)}}{\log x}
\right).
}
$$

Create:

```text
B-RH-005
RESIDUAL_SELBERG_SYMMETRY
status:
  CERTIFIED
```

---

# 3. Normalized residual feedback

Define

$$
\boxed{
r(x)=\frac{F(x)}{x}.
}
$$

Then Theorem 2.1 becomes

$$
\boxed{
r(x)
+
\frac1{\log x}
\sum_{n\le x}
\frac{\Lambda^\sharp(n)}{n}
r(x/n)
+
\frac1{\log x}
\sum_{n\le x}
\frac{f(n)}{n}
r(x/n)
=
O
\left(
\frac{X^{o(1)}}{\log x}
\right).
}
$$

The first multiplicative operator is a positive model-sampling channel.

Its total weight is logarithmic.

---

# 4. Summatory law for Lambda-sharp

Let

$$
L^\sharp(t)
=
\sum_{n\le t}
\Lambda^\sharp(n).
$$

By periodicity and exact period mean from Paper 28,

$$
\boxed{
L^\sharp(t)
=
t
+
X^{o(1)}
}
$$

uniformly for $t\le 2X$.

For any fixed complex number $\delta$ with

$$
\Re\delta>0,
$$

partial summation gives

## Theorem 4.1 — Mellin Sampling Law

$$
\boxed{
\sum_{n\le x}
\Lambda^\sharp(n)n^{\delta-1}
=
\frac{x^\delta}{\delta}
+
X^{o(1)}
}
$$

at fixed- $\delta$ exponent resolution.

The implicit constant may depend on $\delta$.

---

# 5. Fixed Mellin drift test

Let

$$
\rho
=
\beta+i\gamma
$$

be fixed with

$$
\beta<1.
$$

Set

$$
\delta=1-\rho,
\qquad
\Re\delta>0.
$$

Test the hypothetical drift

$$
\boxed{
F_\rho(x)=c x^\rho.
}
$$

Then

$$
r_\rho(x)=c x^{-\delta}.
$$

The model-sampling term is

$$
\begin{aligned}
\frac1{\log x}
\sum_{n\le x}
\frac{\Lambda^\sharp(n)}n
r_\rho(x/n)
&=
\frac{
c x^{-\delta}
}{
\log x
}
\sum_{n\le x}
\Lambda^\sharp(n)n^{\delta-1}
\\
&=
\boxed{
\frac{c}{\delta\log x}
+
x^{-\delta+o(1)}.
}
\end{aligned}
$$

Thus every fixed sublinear Mellin mode creates a contribution at the same $1/\log x$ scale as the Selberg forcing.

---

# 6. Residual self-sampling scale

For the exact model

$$
F_\rho(x)=c x^\rho,
$$

its discrete derivative has scale

$$
f_\rho(n)
=
F_\rho(n)-F_\rho(n-1)
=
c\rho n^{\rho-1}
+
O_\rho(n^{\beta-2}).
$$

Therefore

$$
\begin{aligned}
\frac1{\log x}
\sum_{n\le x}
\frac{f_\rho(n)}n
r_\rho(x/n)
&=
\frac{
c x^{-\delta}
}{
\log x
}
\sum_{n\le x}
f_\rho(n)n^{\delta-1}
\\
&=
O_{\rho,c}
\left(
x^{-\delta}
\right)
\end{aligned}
$$

at fixed-mode scale.

Thus:

```text
model multiplicative sampling:
  1/log x forcing scale

residual nonlinear self-sampling:
  x^{rho-1} scale

direct residual r(x):
  x^{rho-1} scale
```

The $1/\log x$ model channel dominates every fixed power decay.

---

# 7. Residual Selberg forcing criticality

The residual Selberg equation therefore permits every fixed mode

$$
x^\rho,
\qquad
\Re\rho<1,
$$

at exponent level.

The mode is not invisible.

Rather, its image under the positive model sampling operator is absorbed by the pre-existing Selberg forcing.

Create:

```text
O-RH-062
RESIDUAL_SELBERG_MELLIN_MODE_FORCING_CRITICALITY
status:
  CERTIFIED AS FIXED-MODE STRENGTH AUDIT
```

Statement:

> The fixed-order residual Selberg symmetry formula does not yield a fixed polynomial drift gap. For every fixed Mellin mode with real part below one, the sieve-model sampling channel produces a contribution of order $1/\log x$, which lies inside the classical forcing scale.

This is a statement about the audited identity and fixed-mode test.

It is not a universal impossibility theorem for all identities derived from Selberg's method.

---

# 8. Why local logarithmic residual bounds do not repair the feedback

Current higher-uniformity technology gives

$$
F(x+H)-F(x)
\ll
H\log^{-A}X
$$

for almost all polynomial intervals in the current range.

For

$$
F_\rho(x)=x^\rho,
\qquad
\beta<1,
$$

the relative short-interval increment is

$$
X^{\beta-1}
=
X^{-(1-\beta)}.
$$

Every fixed negative power is eventually smaller than every fixed inverse logarithmic power.

Therefore the local theorem remains compatible with the same drift modes which saturate the residual Selberg forcing test.

---

# 9. Residual PESC energy lock

Define as in Paper 28

$$
J_f(N)
=
\sum_{j=N}^{2N-1}|F(j)|^2,
$$

$$
D_f(N)
=
\sum_{n<2N}w_N(n)|f_n|^2,
$$

and

$$
\mathcal C_f(N)
=
\sum_{n<2N}
w_N(n)f_nF(n-1)
$$

in the real model, or the corresponding Hermitian real part in a complex-mode strength test.

The exact energy identity is

$$
\boxed{
J_f
=
D_f
+
2\mathcal C_f.
}
$$

Hence

$$
\boxed{
\mathcal C_f
=
\frac12
[
J_f-D_f
].
}
$$

A sign argument on $\mathcal C_f$ cannot be independent of the residual energy itself.

---

# 10. Smooth drift saturates the self-correlation

For a fixed power mode with

$$
F(x)\asymp x^\beta,
\qquad
\beta>\frac12,
$$

we have

$$
J_f(N)
\asymp
N^{2\beta+1},
$$

while

$$
D_f(N)
\asymp
N^{2\beta}
$$

at exponent scale.

Therefore

$$
\boxed{
\frac{D_f(N)}{J_f(N)}
\asymp
N^{-1},
}
$$

and consequently

$$
\boxed{
\mathcal C_f(N)
=
\frac12J_f(N)
[
1+o(1)
].
}
$$

A persistent smooth drift makes the signed residual self-correlation almost maximally positive.

It does not generate a helpful negative sign.

---

# 11. Two-scale normalized residual energy

Define

$$
\boxed{
Y_f(N)
=
N^{-3}J_f(N).
}
$$

For a pure fixed Mellin mode with real part $\beta$,

$$
J_f(N)
\asymp
N^{2\beta+1}.
$$

Thus

## Theorem 11.1 — Mellin-Mode Two-Scale Ratio

$$
\boxed{
\frac{
Y_f(2N)
}{
Y_f(N)
}
=
2^{-2(1-\beta)}
}
$$

at exact scaling exponent level.

For every fixed $\beta<1$, this is a contraction.

But as

$$
\beta\uparrow1,
$$

the contraction tends to $1$.

---

# 12. Uniform two-scale gap has fixed-strip strength

Suppose one could prove a recurrence

$$
\boxed{
Y_f(2N)
\le
qY_f(N)
+
O(N^{-\eta})
}
$$

with fixed

$$
q<1,
\qquad
\eta>0.
$$

Ignoring the lower-order forcing, the Mellin-mode test requires

$$
2^{-2(1-\beta)}
\le
q.
$$

Therefore

$$
\boxed{
\beta
\le
1+\frac12\log_2 q
<
1.
}
$$

Thus a uniform fixed two-scale gap already has fixed-zero-strip strength.

Create:

```text
O-RH-063
UNIFORM_TWO_SCALE_RESIDUAL_GAP_IS_FIXED_STRIP_STRENGTH
status:
  CERTIFIED AS STRENGTH AUDIT
```

This does not say such a recurrence is impossible.

It says it is not a lower-strength free lemma.

---

# 13. Campaign 28 track audit

## E1 — residual prime-sampling coercivity

```text
status:
  ENERGY LOCK

smooth drift:
  C_f ~ J_f/2

new independent sign coercivity:
  NONE
```

## E2 — Selberg symmetry on residual primitive

```text
status:
  RESIDUAL IDENTITY CERTIFIED

fixed drift coercivity:
  NO

reason:
  model sampling enters at allowed 1/log x forcing scale
```

## E3 — multiplicative sampling of smooth drift

```text
status:
  EXACT FIXED-MODE CALIBRATION

Mellin drift:
  compatible with forcing
```

## E4 — two-scale signed residual energy

```text
status:
  EACH FIXED MODE CONTRACTS

uniform fixed contraction:
  already fixed-strip strength
```

## E5 — canonical drift projection

```text
status:
  NO CANONICAL LOWER-STRENGTH PROJECTION FOUND

not promoted to obstruction theorem
```

---

# 14. Campaign 28 verdict

No new lower-strength fixed-power prime theorem is found.

The direct PESC branch remains the shortest certified target.

The new information is a closure:

```text
Lambda-sharp subtraction:
  fixed-exponent neutral

classical Selberg feedback:
  PNT-level but fixed-power forcing-critical

local residual uniformity:
  drift-blind at fixed powers

simple self-correlation sign:
  energy-locked

uniform two-scale gap:
  fixed-strip strength
```

Thus the present first-order / second-order feedback shell has been exhausted relative to the audited identities.

---

# 15. Why higher Selberg order remains a distinct candidate family

Selberg's classical formula arises from the generalized von Mangoldt function

$$
\Lambda_2
=
\mu*\log^2.
$$

More generally,

$$
\boxed{
\Lambda_k
=
\mu*\log^k
}
$$

satisfies

$$
\boxed{
\Lambda_{k+1}
=
\Lambda_k\log
+
\Lambda*\Lambda_k.
}
$$

The average of $\Lambda_k$ smooths over integers with at most $k$ distinct prime factors.

A higher-order combination may, in principle, modify the forcing polynomial seen by Mellin drift modes.

This has not yet been audited in CSM_RH at fixed-power resolution.

---

# 16. Campaign 29

The next campaign is:

```text
CSM_RH Campaign 29
HIGHER_ORDER_SELBERG_AMPLIFIER_ATTACK
```

This is not a new root target.

It is a mechanism audit.

---

# 17. Campaign 29 tracks

## H1 — fixed-k generalized Selberg response

Derive the normalized residual feedback associated with $\Lambda_k$ for fixed $k$.

Insert a Mellin mode $x^\rho$ and compute the exact forcing scale.

## H2 — finite linear-combination forcing cancellation

Combine several fixed-order Selberg identities so that the $x/\log^j x$ model forcing cancels to the greatest possible order.

Test whether the remaining error is still subpower-critical.

## H3 — growing-k amplification

Let $k$ increase slowly with $X$.

Track:

```text
support complexity;
combinatorial coefficients;
almost-prime model error;
Mellin-mode amplification;
fixed-power gain.
```

Reject the route if the complexity cost consumes the exponent.

## H4 — generalized almost-prime to PESC transfer

Test whether a fixed-power theorem for a smoothed $\Lambda_k$ observable transfers back to prime PESC without assuming a fixed zero strip.

## H5 — spectral polynomial in the Selberg operator

View the fixed-order identities as polynomial filters of multiplicative convolution.

Search for a positive/coercive filter which suppresses the constant forcing channel while retaining sensitivity to $x^\rho$.

---

# 18. Campaign 29 rejection filters

Reject a candidate if:

## R1. Fixed $k$ leaves an $x/\log^j x$ forcing larger than every fixed power drift.

## R2. Growing $k$ produces only sublinear cumulative amplification.

## R3. Combinatorial/almost-prime complexity costs a fixed power larger than the gain.

## R4. The transfer back to primes assumes the desired fixed strip.

## R5. The result is only another generalized-von-Mangoldt representation with no new estimate.

---

# 19. External calibration

Relevant classical facts:

1. Selberg's remainder symmetry formula is

$$
A(x)
+
\frac1{\log x}
\sum_{n\le x}
\Lambda(n)A(x/n)
=
O(x/\log x).
$$

2. The generalized von Mangoldt functions satisfy

$$
\Lambda_k=\mu*\log^k
$$

and

$$
\Lambda_{k+1}
=
\Lambda_k\log
+
\Lambda*\Lambda_k.
$$

They are supported on integers with at most $k$ distinct prime factors.

3. Current prime residual short-interval control after subtraction of $\Lambda^\sharp$ remains of arbitrary logarithmic accuracy, not fixed-power accuracy.

---

# 20. State transition

```text
CSM_RH v1.19
  ->
CSM_RH v1.20
```

with:

```text
Campaign 28
  CLOSED_AS_RESIDUAL_SELBERG_AND_DRIFT_COERCIVITY_AUDIT

B-RH-005
  RESIDUAL_SELBERG_SYMMETRY
  CREATED / CERTIFIED

O-RH-062
  RESIDUAL_SELBERG_MELLIN_MODE_FORCING_CRITICALITY
  CREATED / CERTIFIED AS FIXED-MODE STRENGTH AUDIT

O-RH-063
  UNIFORM_TWO_SCALE_RESIDUAL_GAP_IS_FIXED_STRIP_STRENGTH
  CREATED / CERTIFIED AS STRENGTH AUDIT

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 29
  HIGHER_ORDER_SELBERG_AMPLIFIER_ATTACK
  READY
```

---

# 21. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

RESIDUAL SELBERG SYMMETRY = CERTIFIED

FIXED-ORDER SELBERG DRIFT COERCIVITY = NOT OBTAINED

MODEL SAMPLING OF x^rho = FORCING-CRITICAL

RESIDUAL SELF-CORRELATION SIGN = ENERGY-LOCKED

UNIFORM TWO-SCALE GAP = FIXED-STRIP STRENGTH

NEXT CAMPAIGN = 29
```

The central fixed-mode calculation is

$$
\boxed{
\frac1{\log x}
\sum_{n\le x}
\frac{\Lambda^\sharp(n)}n
\left(
\frac{x}{n}
\right)^{\rho-1}
=
\frac1{(1-\rho)\log x}
+
x^{\rho-1+o(1)}.
}
$$

For every fixed $\Re\rho<1$, the dominant image lies inside the classical Selberg forcing scale.

The next question is whether higher-order Selberg filters can cancel that forcing without paying away the fixed exponent.
