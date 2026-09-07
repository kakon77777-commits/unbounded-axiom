# CSM_RH Paper 36
## Rational/Stieltjes Filter Closure, Resolvent Drift Persistence, and the Representation–Arithmetic Separation Principle

**Project:** `CSM_RH`  
**Paper:** `36`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.26 / Paper 35`  
**Campaign:** `35 — RATIONAL_MUNTZ_LOW_FREQUENCY_FILTER_AUDIT`  
**Status:** rational/Müntz approximation audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 35 closed ordinary finite-rank polynomial projection as a lower-strength route.

Campaign 35 asks whether rational or Müntz filters change that conclusion because they approximate endpoint branch singularities much more efficiently.

The answer is:

```text
rational approximation complexity:
  dramatically better

prime-side arithmetic strength:
  not automatically better

fixed finite resolvent rank:
  exponent-neutral

root-exponential rank:
  polylogarithmic rank can represent N^(-delta) function error

derivative/correlation control:
  not implied by uniform function approximation

clustered rational poles:
  enter polynomial conditioning scale at fixed-power accuracy

Müntz coordinates:
  are Mellin coordinates and retain hard arithmetic moments
```

Thus approximation efficiency and arithmetic proof strength separate.

No new frontier is created.

---

# 1. Stieltjes representation of a fractional power

For

$$
0<\beta<1,
$$

the power function is a complete Bernstein function and has the Stieltjes representation

$$
\boxed{
u^\beta
=
\frac{\sin(\pi\beta)}{\pi}
\int_0^\infty
t^{\beta-1}
\frac{u}{u+t}
\,dt,
\qquad
u>0.
}
$$

Define the resolvent kernel

$$
\boxed{
r_t(u)
=
\frac{u}{u+t},
\qquad
t>0.
}
$$

The fractional Mellin drift is therefore a positive continuum superposition of rational resolvent coordinates.

---

# 2. Rational approximation complexity

Let

$$
E_{r,r}(u^\beta;[0,1])
$$

be the best uniform type- $(r,r)$ rational approximation error.

Stahl's theorem gives

$$
\boxed{
E_{r,r}(u^\beta;[0,1])
=
C_\beta
\exp
\left(
-2\pi\sqrt{\beta r}
\right)
[
1+o(1)
],
}
$$

where

$$
C_\beta
=
4^{1+\beta}
|\sin(\pi\beta)|.
$$

Therefore:

## Theorem 2.1 — Rational Fixed-Power Rank Scale

To reach a purely approximation-theoretic target

$$
E_{r,r}
\le
N^{-\delta},
$$

it is sufficient at leading order to take

$$
\boxed{
r
\asymp
\frac{
\delta^2
}{
4\pi^2\beta
}
(\log N)^2.
}
$$

This is exponentially cheaper in rank than the ordinary polynomial route of Paper 35.

---

# 3. Pole geometry

For

$$
0<\beta<1,
$$

the poles and zeros of the best rational approximants lie on the negative real axis.

Near-best rational and lightning constructions achieve root-exponential convergence by exponential or tapered-exponential clustering of poles toward the branch point $u=0$.

A representative clustering law is

$$
\boxed{
t_{\min}
=
\exp
[
-\Theta_\beta(\sqrt r)
].
}
$$

At the fixed-power approximation scale

$$
r=\Theta((\log N)^2),
$$

this becomes

$$
\boxed{
t_{\min}
=
N^{-\Theta_\beta(1)}.
}
$$

This is used only as route calibration for clustered-pole rational schemes.

---

# 4. Resolvent arithmetic observables

Return to the PESC endpoint Hilbert space.

For fixed $t>0$, define the scale-local rational coordinate

$$
\boxed{
v_t(n)
=
r_t(n/N)
=
\frac{n/N}{n/N+t}.
}
$$

Define the cumulative-error moment

$$
\boxed{
M_B(t;N)
=
\sum_{n<2N}
w_N(n)
B(n-1)
v_t(n).
}
$$

Define the detector moment

$$
\boxed{
M_c(t;N)
=
\sum_{n<2N}
w_N(n)
c_n
v_t(n).
}
$$

These are the natural correction coordinates in a rational low-frequency projection.

---

# 5. Fixed resolvent response to a smooth drift

Take

$$
B(x)=x^\beta,
\qquad
0<\beta<1.
$$

Then

$$
c_n
=
\beta n^{\beta-1}
+
O_\beta(n^{\beta-2}).
$$

At scale $n=Nu$,

$$
M_B(t;N)
=
N^{\beta+2}
J_B(\beta,t)
+
o(N^{\beta+2}),
$$

where

$$
\boxed{
J_B(\beta,t)
=
\int_0^2
\omega(u)
u^\beta
\frac{u}{u+t}
\,du.
}
$$

Likewise,

$$
M_c(t;N)
=
N^{\beta+1}
J_c(\beta,t)
+
o(N^{\beta+1}),
$$

where

$$
\boxed{
J_c(\beta,t)
=
\beta
\int_0^2
\omega(u)
u^{\beta-1}
\frac{u}{u+t}
\,du.
}
$$

For real

$$
0<\beta<1,
\qquad
t>0,
$$

both integrands are positive.

Therefore:

## Theorem 5.1 — Fixed Resolvent Drift Persistence

$$
\boxed{
J_B(\beta,t)>0,
\qquad
J_c(\beta,t)>0.
}
$$

Every fixed positive resolvent coordinate retains the full smooth-drift exponent.

---

# 6. Finite rational projection remains exponent-neutral

Let

$$
V_r
=
\operatorname{span}
\{
r_{t_1},\ldots,r_{t_r}
\}
$$

for fixed positive nodes $t_j$ independent of $N$ and of the unknown zero set.

Paper 35's finite-rank projection theorem applies verbatim.

For

$$
B(x)=x^\beta,
$$

the low-rank correction has scale

$$
\boxed{
N^{2\beta+1}
}
$$

and the residual covariance has the same outer exponent whenever its coefficient is nonzero.

Thus:

## Theorem 6.1 — Fixed Rational Rank Exponent Invariance

A fixed finite family of resolvent coordinates can change the Mellin transfer coefficient but not the PESC smooth-drift exponent.

Create:

```text
O-RH-081
FIXED_RATIONAL_RESOLVENT_PROJECTION_EXPONENT_INVARIANCE
status:
  CERTIFIED
```

---

# 7. Representation error is not arithmetic error

Suppose a rational function satisfies

$$
\boxed{
\|u^\beta-r_r(u)\|_\infty
\le
N^{-\delta}.
}
$$

This is a statement about representing the cumulative drift profile.

PESC, however, couples the cumulative profile to its arithmetic derivative.

Uniform approximation of a function does not imply comparable approximation of its derivative.

Indeed, in general one may have functions $e_N$ with

$$
\|e_N\|_\infty
\le
N^{-\delta}
$$

but

$$
\|e_N'\|_\infty
\asymp1
$$

or larger.

Therefore a fixed-power rational approximation coefficient cannot be inserted directly into the PESC derivative/correlation ledger.

Create:

```text
O-RH-082
UNIFORM_FUNCTION_APPROXIMATION_DOES_NOT_CONTROL_PESC_DERIVATIVE
status:
  CERTIFIED
```

---

# 8. Resolvent derivative conditioning

The resolvent derivative is

$$
\boxed{
r_t'(u)
=
\frac{t}{(u+t)^2}.
}
$$

Hence

$$
\boxed{
\|r_t'\|_{L^\infty([0,2])}
=
\frac1t.
}
$$

For clustered-pole schemes with

$$
t_{\min}
=
\exp[-\Theta(\sqrt r)],
$$

the most singular basis derivative has size

$$
\boxed{
\exp[\Theta(\sqrt r)].
}
$$

At

$$
r=\Theta((\log N)^2),
$$

this becomes

$$
\boxed{
N^{\Theta(1)}.
}
$$

Thus the same pole clustering which gives fixed-power function approximation introduces polynomial derivative conditioning at the PESC fixed-power rank scale.

Create:

```text
O-RH-083
CLUSTERED_RESOLVENT_DERIVATIVE_CONDITIONING_ENTERS_FIXED_POWER_SCALE
status:
  CERTIFIED FOR EXPONENTIALLY CLUSTERED RESOLVENT ROUTES
```

This is not a universal theorem about every rational basis.

---

# 9. Stieltjes quadrature interpretation

The Stieltjes formula expresses the drift as a positive continuum of resolvents:

$$
u^\beta
=
C_\beta
\int_0^\infty
t^{\beta-1}
r_t(u)
\,dt.
$$

A rational quadrature discretizes this continuum into a finite family

$$
\boxed{
\sum_{j=1}^{r}
\alpha_jr_{t_j}(u).
}
$$

The approximation-theoretic gain is obtained by selecting nodes and coefficients so that the continuum profile is reconstructed efficiently.

But the corresponding arithmetic projection requires the moments

$$
M_B(t_j;N),
\qquad
M_c(t_j;N),
$$

or equivalent linear combinations.

Theorem 5.1 shows that these moments themselves retain the full smooth-drift exponent.

Thus the approximation does not supply their arithmetic smallness.

---

# 10. Rational correction matrix

For a finite rational basis, define the Gram matrix

$$
G_{ij}
=
\langle
r_{t_i},
r_{t_j}
\rangle_N.
$$

Define moment vectors

$$
m_B
=
(
M_B(t_1;N),\ldots,M_B(t_r;N)
)^T,
$$

$$
m_c
=
(
M_c(t_1;N),\ldots,M_c(t_r;N)
)^T.
$$

The exact low-rank PESC correction is

$$
\boxed{
m_c^\ast
G^{-1}
m_B.
}
$$

For fixed rank, this has the same smooth-drift exponent as PESC.

For growing rank, proving that this correction is fixed-power small requires arithmetic control of a growing family of resolvent moments and of the conditioning of $G^{-1}$.

Approximation theory alone supplies neither.

---

# 11. Representation–arithmetic separation principle

Create:

```text
O-RH-084
REPRESENTATION_EFFICIENCY_DOES_NOT_IMPLY_ARITHMETIC_FIXED_POWER
status:
  CERTIFIED AS CSM_RH MECHANISM PRINCIPLE
```

Statement:

> Efficient approximation of the shape of a hypothetical low-frequency prime-error drift does not imply a fixed-power estimate for the arithmetic coordinates required to subtract that drift from PESC.

The rational route dramatically improves the first problem.

It does not solve the second.

---

# 12. Müntz coordinates

A Müntz family has the form

$$
\boxed{
1,
u^{\lambda_1},
u^{\lambda_2},
\ldots
}
$$

with positive exponents.

Müntz's theorem states that, under the standard hypotheses, the span is dense in $C[0,1]$ precisely when

$$
\boxed{
\sum_j
\frac1{\lambda_j}
=
\infty.
}
$$

Thus a zero-independent infinite exponent family can be representationally complete.

But every basis vector is itself a Mellin coordinate.

---

# 13. Müntz moment scaling

For a basis exponent $\lambda$, define the cumulative-error moment

$$
M_B(\lambda;N)
=
\sum_{n<2N}
w_N(n)
B(n-1)
\left(
\frac nN
\right)^\lambda.
$$

For

$$
B(x)=x^\beta,
$$

$$
\boxed{
M_B(\lambda;N)
=
N^{\beta+2}
I(\beta+\lambda)
+
o(N^{\beta+2}),
}
$$

where

$$
I(s)
=
\frac{
2^{s+2}-1
}{
(s+1)(s+2)
}.
$$

Likewise,

$$
\boxed{
M_c(\lambda;N)
=
\beta
N^{\beta+1}
I(\beta-1+\lambda)
+
o(N^{\beta+1}).
}
$$

For real nonnegative $\lambda$, these coefficients are nonzero.

Thus a fixed Müntz basis is exponent-neutral.

---

# 14. Unknown-exponent issue

If one inserts the exact unknown exponent

$$
\lambda=\beta
$$

into a basis, representation of the drift becomes trivial.

But such a choice uses the unknown drift / zero parameter as a proof input.

This is disallowed.

A predetermined dense exponent family avoids that circularity.

However the arithmetic correction moments remain Mellin-weighted integrated prime-error observables.

No current fixed-power estimates for those growing families are supplied by the approximation theorem.

---

# 15. Müntz density is not a quantitative arithmetic theorem

The divergence condition

$$
\sum1/\lambda_j=\infty
$$

is a completeness statement.

It does not give:

```text
a fixed-power approximation rate for the entire critical-strip drift family;
uniform conditioning of the resulting arithmetic correction matrix;
fixed-power estimates for the Mellin prime-error moments.
```

Therefore Müntz completeness does not create a lower-strength PESC route.

Create:

```text
O-RH-085
MUNTZ_COMPLETENESS_WITHOUT_ARITHMETIC_MOMENT_CONTROL
status:
  CERTIFIED AS MECHANISM AUDIT
```

---

# 16. Campaign 35 track audit

## RA1 — rational approximation complexity

```text
status:
  ROOT-EXPONENTIAL

formal N^(-delta) representation rank:
  O((log N)^2)
```

## RA2 — Stieltjes/resolvent representation

```text
status:
  EXACT

basis:
  u/(u+t)
```

## RA3 — arithmetic control of rational moments

```text
status:
  FIXED RESOLVENTS RETAIN FULL DRIFT EXPONENT

fixed-power moment theorem:
  not available
```

## RA4 — Müntz basis without zero knowledge

```text
status:
  REPRESENTATIONALLY COMPLETE IN PRINCIPLE

arithmetic moments:
  Mellin-hard
```

## RA5 — complexity versus zero sensitivity

```text
status:
  APPROXIMATION COMPLEXITY IMPROVED

arithmetic fixed-power complexity:
  not improved by current theorem set

derivative conditioning:
  exponent-critical in clustered-pole route
```

---

# 17. Campaign 35 verdict

The rational route is the first audited low-frequency filter whose approximation rank is genuinely attractive:

$$
r
=
O((\log N)^2)
$$

can represent a fixed-power branch-profile error.

But this does not produce a prime theorem.

The correction coordinates retain the same Mellin drift exponent, and derivative-sensitive PESC control is not inherited from uniform approximation.

Müntz completeness has the same representation/arithmetic separation.

Therefore:

```text
rational/Müntz filtering:
  valuable representation technology

lower-strength RH route:
  not obtained
```

No new frontier is created.

---

# 18. New certified package

Create:

```text
O-RH-081
FIXED_RATIONAL_RESOLVENT_PROJECTION_EXPONENT_INVARIANCE
CERTIFIED

O-RH-082
UNIFORM_FUNCTION_APPROXIMATION_DOES_NOT_CONTROL_PESC_DERIVATIVE
CERTIFIED

O-RH-083
CLUSTERED_RESOLVENT_DERIVATIVE_CONDITIONING_ENTERS_FIXED_POWER_SCALE
CERTIFIED FOR CLUSTERED-POLE ROUTES

O-RH-084
REPRESENTATION_EFFICIENCY_DOES_NOT_IMPLY_ARITHMETIC_FIXED_POWER
CERTIFIED

O-RH-085
MUNTZ_COMPLETENESS_WITHOUT_ARITHMETIC_MOMENT_CONTROL
CERTIFIED
```

---

# 19. Canonical root status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN / DIRECT THEOREM CANDIDATE

low-frequency projection families:
  exhausted as representation-only mechanisms
```

---

# 20. Campaign 36

After Papers 17–36, surrogate representation generation is stopped again.

The next campaign is:

```text
CSM_RH Campaign 36
MINIMAL_FIXED_POWER_BREAKTHROUGH_GATE
```

Its purpose is to consolidate the audited closure graph and admit only genuinely new prime-side fixed-power lemmas.

---

# 21. Campaign 36 admission rules

A candidate is admitted only if it satisfies all of:

## G1 — new arithmetic estimate

It contains a theorem estimate not already equivalent by deterministic identities to PESC, MLEPG, or one of the closed auxiliary gates.

## G2 — fixed exponent source

The proof contains an explicit mechanism generating a fixed positive exponent.

## G3 — no zero-strip input

No fixed zero-free half-plane is assumed.

## G4 — no representation-only gain

Improved approximation, projection, decomposition, filtering, or basis efficiency does not count unless accompanied by a new prime estimate.

## G5 — direct bridge

A proved chain returns the candidate to PESC / fixed PNT mean-square.

---

# 22. Campaign 36 preferred theorem families

## B1 — direct signed PESC contraction

A genuinely new arithmetic inequality for the endogenous prime self-correlation.

## B2 — direct MLEPG power theorem

A fixed-power lag-energy estimate proved without importing a fixed strip.

## B3 — shrinking-threshold short-interval theorem

A theorem with polynomially shrinking relative error and power-sized exceptional set.

## B4 — fixed-power principal Fejer deconcentration

A prime exponential-sum estimate on the principal arc with an actual fixed exponent.

## B5 — new arithmetic recursion

A scale recurrence whose cumulative contraction mass is provably linear in $\log N$ from prime-specific information.

---

# 23. Campaign 36 hard rejects

Reject:

```text
new equivalent criteria;
new positive p-moment surrogates;
new zero-density-only routes;
new fixed-order Selberg filters;
new finite-rank low-frequency projections;
new rational/Müntz representations without arithmetic estimates;
logarithmic or stretched-log savings labelled as fixed power;
fixed zero-strip assumptions.
```

---

# 24. State transition

```text
CSM_RH v1.26
  ->
CSM_RH v1.27
```

with:

```text
Campaign 35
  CLOSED_AS_RATIONAL_MUNTZ_REPRESENTATION_ARITHMETIC_AUDIT

O-RH-081
  CREATED / CERTIFIED

O-RH-082
  CREATED / CERTIFIED

O-RH-083
  CREATED / CERTIFIED FOR CLUSTERED-POLE ROUTES

O-RH-084
  CREATED / CERTIFIED

O-RH-085
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

F-RH-016
  MLEPG
  REMAINS OPEN / DIRECT THEOREM CANDIDATE

Campaign 36
  MINIMAL_FIXED_POWER_BREAKTHROUGH_GATE
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

POLYNOMIAL PROJECTION = CLOSED

RATIONAL REPRESENTATION = ROOT-EXPONENTIALLY EFFICIENT

RATIONAL ARITHMETIC CONTROL = OPEN / NO POWER GAIN

MUNTZ COMPLETENESS = REPRESENTATIONAL ONLY

FIXED-POWER DERIVATIVE CONTROL = NOT PROVIDED BY FUNCTION APPROXIMATION

LOW-FREQUENCY REPRESENTATION SHELL = CLOSED

NEXT CAMPAIGN = 36
```

The central lesson is:

$$
\boxed{
\text{approximating the shape of a hard drift is not the same as proving that primes cannot contain that drift.}
}
$$

Rational approximation solves the former with impressive efficiency.

CSM_RH still needs the latter.
