# CSM_RH Paper 11
## Prime-Error Self-Sampling, the Selberg Resolution Floor, and the Irreducible Prime-Correlation Core

**Project:** `CSM_RH`  
**Paper:** `11`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.1 / Paper 10`  
**Campaign:** `10 — PRIME_ONLY_DYADIC_ENERGY_ATTACK`  
**Status:** exact prime-correlation reduction / mechanism audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

Canonical root state:

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

This paper begins from the prime-only target

$$
J_N^\vartheta
=
\sum_{j=N}^{2N-1}
[
\vartheta(j)-j
]^2
$$

and asks for the first genuinely new prime-correlation statement required to improve its exponent.

The answer is an exact self-sampling correlation.

No decomposition identity is part of the target statement.

No live GLM-5.3-Flash run is claimed.

---

# 1. Prime-only increments

Define

$$
q_n
=
\log n\,
\mathbf1_{\mathbb P}(n).
$$

Then

$$
\vartheta(j)
=
\sum_{n\le j}q_n.
$$

Define the centered prime increment

$$
\boxed{
c_n
=
q_n-1.
}
$$

Define the cumulative prime error

$$
\boxed{
B(j)
=
\sum_{n\le j}c_n
=
\vartheta(j)-j.
}
$$

The canonical dyadic energy is

$$
\boxed{
J_N^\vartheta
=
\sum_{j=N}^{2N-1}
B(j)^2.
}
$$

---

# 2. Endpoint multiplicity

Define

$$
w_N(n)
=
\begin{cases}
N,
&
1\le n\le N,
\\
2N-n,
&
N<n<2N,
\\
0,
&
n\ge2N.
\end{cases}
$$

This is the exact number of endpoints

$$
j\in[N,2N-1]
$$

for which

$$
n\le j.
$$

Therefore

$$
\sum_{n<2N}
w_N(n)
[
B(n)^2-B(n-1)^2
]
=
J_N^\vartheta.
$$

---

# 3. Prime-error self-sampling identity

Since

$$
B(n)
=
B(n-1)+c_n,
$$

we have

$$
B(n)^2-B(n-1)^2
=
2c_nB(n-1)+c_n^2.
$$

Define the diagonal term

$$
\boxed{
D_N^\vartheta
=
\sum_{n<2N}
w_N(n)c_n^2.
}
$$

Define the prime-error self-sampling correlation

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{n<2N}
w_N(n)c_nB(n-1).
}
$$

Then:

## Theorem 3.1 — Prime-Error Self-Sampling Identity

$$
\boxed{
J_N^\vartheta
=
D_N^\vartheta
+
2\mathcal C_N^\vartheta.
}
$$

This identity is exact.

---

# 4. Diagonal size

For composite $n$,

$$
c_n=-1.
$$

For prime $p$,

$$
c_p=\log p-1.
$$

Hence

$$
c_n^2
\ll
1
+
(\log n)^2
\mathbf1_{\mathbb P}(n).
$$

Using

$$
w_N(n)\le N
$$

and Chebyshev's bound

$$
\vartheta(x)\ll x,
$$

we have

$$
\sum_{p\le2N}
(\log p)^2
\le
(\log 2N)\vartheta(2N)
\ll
N\log N.
$$

Therefore:

## Lemma 4.1

$$
\boxed{
D_N^\vartheta
=
O(N^2\log N).
}
$$

This is lower order for every target

$$
N^{3-\kappa+o(1)}
$$

with

$$
0<\kappa\le1.
$$

---

# 5. Exact fixed-exponent equivalence

Define:

## PESC $(\kappa)$

$$
\boxed{
|\mathcal C_N^\vartheta|
\ll
N^{3-\kappa+o(1)}.
}
$$

The acronym is:

```text
PESC
PRIME-ERROR SELF-CORRELATION
```

Then:

## Theorem 5.1 — PODEE / PESC equivalence

For every fixed

$$
0<\kappa\le1,
$$

the following are exponent-equivalent:

$$
\boxed{
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}
}
$$

and

$$
\boxed{
\operatorname{PESC}(\kappa).
}
$$

### Proof

If PESC $(\kappa)$ holds, then Theorem 3.1 and Lemma 4.1 give

$$
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}
+
N^{2+o(1)}.
$$

Conversely,

$$
2|\mathcal C_N^\vartheta|
\le
J_N^\vartheta
+
D_N^\vartheta.
$$

The result follows. $\square$

For the first fixed-strip target, Paper 10 requires only

$$
0<\kappa<\frac12.
$$

---

# 6. Prime-sampling form

Because

$$
c_n
=
q_n-1,
$$

we may rewrite PESC as

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{p<2N}
w_N(p)
\log p\,
B(p-1)
-
\sum_{n<2N}
w_N(n)
B(n-1).
}
$$

Thus PESC asks whether logarithmically weighted prime locations sample the endogenous test function

$$
B(n-1)
=
\vartheta(n-1)-(n-1)
$$

with a fixed-power discrepancy.

This is the minimal prime-sampling formulation.

---

# 7. Discrete Stieltjes form

Let

$$
d\vartheta(n)
=
q_n
$$

and

$$
dn=1.
$$

Then

$$
dB(n)
=
d\vartheta(n)-dn
=
c_n.
$$

Therefore

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{n<2N}
w_N(n)
B(n-1)
dB(n).
}
$$

This is a discrete Stieltjes self-integral.

The identity

$$
d(B^2)
=
2B_-\,dB+(dB)^2
$$

is exactly Theorem 3.1.

Thus the prime-sampling discrepancy is not an external covariance placed next to the energy.

It is the energy increment itself.

---

# 8. Self-correlation lock

A tempting heuristic would be:

```text
prime locations should be approximately independent of
the previous prime-counting error
```

and therefore

$$
\mathcal C_N^\vartheta
$$

should exhibit generic cancellation.

But Theorem 3.1 shows:

$$
\mathcal C_N^\vartheta
=
\frac12
\left[
J_N^\vartheta
-
D_N^\vartheta
\right].
$$

Therefore a fixed-power decorrelation theorem of the required strength is already the fixed-power energy theorem.

This creates:

```text
O-RH-022
PRIME_SELF_SAMPLING_ENERGY_LOCK
```

The obstruction does not say PESC is false.

It says independence language is not independent proof input.

---

# 9. Expanded triangular prime-pair form

Expanding the first term in Section 6,

$$
\sum_{p<2N}
w_N(p)
\log p\,
B(p-1)
$$

gives

$$
\sum_{q<p<2N}
w_N(p)
\log p
\log q
-
\sum_{p<2N}
w_N(p)
\log p
(p-1).
$$

Similarly,

$$
\sum_{n<2N}
w_N(n)
B(n-1)
$$

equals

$$
\sum_{q<2N}
\log q
\sum_{q<n<2N}
w_N(n)
-
\sum_{n<2N}
w_N(n)(n-1).
$$

Hence:

## Theorem 9.1 — Triangular Prime-Pair Discrepancy

$$
\boxed{
\begin{aligned}
\mathcal C_N^\vartheta
={}&
\sum_{q<p<2N}
w_N(p)
\log p
\log q
\\
&-
\sum_{p<2N}
w_N(p)
\log p
(p-1)
\\
&-
\sum_{q<2N}
\log q
\sum_{q<n<2N}
w_N(n)
\\
&+
\sum_{n<2N}
w_N(n)(n-1).
\end{aligned}
}
$$

Thus the irreducible target may also be read as one signed triangular prime-pair discrepancy.

No fixed shift $h$ is privileged.

No singular-series model is inserted into the statement.

---

# 10. Prime-only Selberg symmetry

The classical Selberg symmetry formula has the prime-only form

$$
\boxed{
\vartheta(x)\log x
+
\sum_{p\le x}
\log p\,
\vartheta(x/p)
=
2x\log x
+
O(x).
}
$$

Using

$$
B(x)
=
\vartheta(x)-x
$$

and the Mertens prime sum

$$
\sum_{p\le x}
\frac{\log p}{p}
=
\log x
+
O(1),
$$

we obtain

$$
\boxed{
B(x)\log x
+
\sum_{p\le x}
\log p\,
B(x/p)
=
O(x).
}
$$

This is a genuine self-consistency equation for the prime-only error.

---

# 11. Direct Selberg resolution floor

Suppose hypothetically that for some fixed

$$
0\le\beta<1
$$

we already have

$$
B(y)
=
O(y^\beta).
$$

Then

$$
B(x)\log x
=
o(x).
$$

Also, using Chebyshev's bound and partial summation,

$$
\sum_{p\le x}
\frac{\log p}{p^\beta}
=
O
\left(
x^{1-\beta}
\right).
$$

Hence

$$
\begin{aligned}
\sum_{p\le x}
\log p\,
B(x/p)
&\ll
x^\beta
\sum_{p\le x}
\frac{\log p}{p^\beta}
\\
&\ll
x.
\end{aligned}
$$

Therefore the standard

$$
O(x)
$$

Selberg remainder is compatible, at direct magnitude level, with every fixed power

$$
B(x)=O(x^\beta),
\qquad
\beta<1.
$$

It does not by itself resolve which $\beta<1$ is present.

This creates:

```text
O-RH-023
SELBERG_OX_DIRECT_RESOLUTION_FLOOR
```

This is not a no-go theorem against all iterations based on Selberg's formula.

Selberg's actual elementary PNT proof uses nonlinear self-improvement beyond this direct comparison.

The obstruction applies to the raw $O(x)$ resolution scale.

---

# 12. Refined Selberg residual calibration

Filip Saidak proved a refined relation for the $\psi$ version of Selberg's lemma.

If

$$
E(x)
=
\psi(x)-x,
$$

then the Selberg expression admits an explicit linear secondary term and an error of size

$$
O
\left(
E(x)(\log x)^2
\right).
$$

This gives an important calibration:

> sharpening the Selberg residual is tightly coupled to sharpening the PNT error itself.

This paper does not promote Saidak's $\psi$ theorem into a new $\vartheta$ theorem.

The result is used only to reject the idea that a power-accurate Selberg residual should be assumed to be a free lower-strength input.

---

# 13. Campaign 10 mechanism audit

## C10-A — Direct prime-support energy identity

```text
status:
  SUCCESSFUL REDUCTION

output:
  PESC
```

It identifies the exact first prime-correlation statement.

It does not prove a fixed power.

---

## C10-B — Prime-only Selberg symmetry

```text
status:
  CRITICAL / QUALITATIVE SELF-IMPROVEMENT TOOL

raw remainder scale:
  O(x)

fixed-power resolution from raw magnitude alone:
  NO
```

A stronger operator/inversion theorem could still be useful.

---

## C10-C — Signed sieve-weight approximation

Let

$$
q_n
=
\lambda_n
+
r_n
$$

for a canonical sieve approximation $\lambda_n$.

Then

$$
\mathcal C_N^\vartheta
=
\sum_n
w_N(n)
[
\lambda_n-1
]
B(n-1)
+
\sum_n
w_N(n)
r_nB(n-1).
$$

This is exact.

A useful sieve theorem must therefore control the approximation error against the endogenous weight

$$
B(n-1).
$$

An unweighted counting approximation is not enough.

Status:

```text
OPEN AS PROOF MECHANISM
NO INDEPENDENT FIXED-POWER LEMMA IDENTIFIED
```

---

## C10-D — Target-first bilinear decomposition

Vaughan or Heath-Brown may still be applied to the prime increment.

But Paper 10's decomposition-shell rule remains:

```text
decomposition
  !=
estimate
```

Any successful result must prove PESC or PODEE after recombination.

Status:

```text
SUBORDINATE PROOF TOOL
```

---

## C10-E — Dyadic scale self-improvement

A scale recurrence remains admissible.

But the previous Selberg analysis shows that known elementary self-improvement mechanisms are critical or vanishing-gap rather than fixed-gap.

Status:

```text
OPEN ONLY WITH NEW FIXED-POWER CONTRACTION
```

---

## C10-F — New prime-correlation theorem

The minimal exact target is now:

$$
\boxed{
\operatorname{PESC}(\kappa).
}
$$

Status:

```text
OPEN
IRREDUCIBLE CURRENT CORE
```

---

# 14. Canonical frontier relation

Paper 10 introduced

```text
F-RH-009
PRIME_ONLY_DYADIC_ERROR_ENERGY
PODEE
```

This paper creates:

```text
F-RH-010
PRIME_ERROR_SELF_CORRELATION
PESC
```

with the certified relation

$$
\boxed{
F\text{-}RH\text{-}009(\kappa)
\Longleftrightarrow_{\rm exponent}
F\text{-}RH\text{-}010(\kappa)
}
$$

for

$$
0<\kappa\le1.
$$

This is an exact interface equivalence.

It is not a theorem-strength reduction.

---

# 15. Fixed-strip calibration

For the first fixed-strip target, choose

$$
0<\kappa<\frac12.
$$

Paper 10 proved that PODEE $(\kappa)$ is exponent-equivalent to the corresponding $\psi$ dyadic mean-square bound because prime powers contribute only

$$
O(N^{5/2+o(1)}).
$$

The established PNT mean-square / zero relation then yields a fixed zeta zero strip.

Therefore:

$$
\boxed{
\operatorname{PESC}(\kappa)
\Longrightarrow
\text{a fixed zeta zero strip}
}
$$

for every fixed

$$
0<\kappa<\frac12.
$$

PESC is not a low-strength lemma.

It is simply the cleanest current prime-correlation interface.

---

# 16. What has been removed

The current prime-correlation core contains no:

```text
zeta zero packet
character family
major/minor arc
singular series
prime powers
Vaughan cutoff
Heath-Brown depth
Gram decomposition
fixed shift
positive energy auxiliary gate
```

The only arithmetic input is the prime support itself.

This is the strongest closure-space reduction achieved so far in the arithmetic branch.

---

# 17. New obstruction: prime self-sampling energy lock

Create:

```text
O-RH-022
PRIME_SELF_SAMPLING_ENERGY_LOCK
status:
  CERTIFIED
```

Statement:

> The weighted correlation between the centered prime increment and its own past cumulative error is exactly half the prime-only dyadic energy minus the lower-order diagonal. It cannot be justified by generic independence or decorrelation heuristics without proving the target itself.

---

# 18. New obstruction: Selberg direct resolution floor

Create:

```text
O-RH-023
SELBERG_OX_DIRECT_RESOLUTION_FLOOR
status:
  CERTIFIED_AS_DIRECT_MAGNITUDE_OBSTRUCTION
```

Statement:

> The classical $O(x)$ Selberg symmetry remainder is directly compatible with every hypothetical fixed power $B(x)=O(x^\beta)$ for $\beta<1$. Raw magnitude comparison of the classical formula cannot distinguish a fixed zero-strip exponent.

This does not block nonlinear Selberg-type arguments with genuinely stronger input.

---

# 19. New survivor

Create:

```text
S-RH-019
ENDOGENOUS_PRIME_SAMPLING_CANCELLATION
status:
  OPEN
```

The target is not ordinary equidistribution against an external test function.

The test function is

$$
B(n-1)
=
\vartheta(n-1)-(n-1),
$$

generated by the same prime sequence.

A successful theorem must exploit genuine arithmetic structure of this endogenous coupling.

---

# 20. Campaign 10 verdict

```text
DIRECT ENERGY
  REDUCED TO PESC

PRIME-ONLY SELBERG FORMULA
  CRITICAL AT O(x) RESOLUTION

SIGNED SIEVE APPROXIMATION
  POSSIBLE TOOL
  NO FREE FIXED POWER

BILINEAR DECOMPOSITION
  SUBORDINATE TOOL

FIRST IRREDUCIBLE PRIME-CORRELATION LEMMA
  PESC(kappa)

FIXED POWER PROVED
  NO
```

Campaign 10 closes as the minimal prime-correlation reduction.

---

# 21. Campaign 11

The next campaign is:

```text
CSM_RH Campaign 11
ENDOGENOUS_PRIME_SAMPLING_MECHANISM
```

Target:

```text
F-RH-010
PESC
```

The campaign asks only:

> What new arithmetic mechanism could control primes sampled against their own past counting error with a fixed power?

---

# 22. Campaign 11 tracks

## Track S — refined Selberg operator

Seek a power-accurate refinement of the prime-only Selberg self-consistency relation together with an operator inversion or contraction certificate.

A small residual alone is insufficient unless the inverse step is proved.

## Track W — endogenous sieve approximation

Construct signed sieve weights $\lambda_n$ and prove both:

$$
\sum_n
w_N(n)
[
\lambda_n-1
]
B(n-1)
$$

and

$$
\sum_n
w_N(n)
[
q_n-\lambda_n
]
B(n-1)
$$

at fixed-power strength.

The second term is the target-fidelity bottleneck.

## Track R — scale-local prime sampling

Split the endpoint geometry into canonical scales and search for a recurrence whose cumulative contraction mass is linear in $\log N$.

## Track C — direct new correlation theorem

Prove PESC directly by a new signed prime-correlation estimate.

---

# 23. Campaign 11 rejection filters

Reject a candidate if:

## R1. Independence heuristic

"Primes should be uncorrelated with past error" is not a proof because of O-RH-022.

## R2. External-test equidistribution substitution

A theorem for arbitrary fixed smooth test functions is applied to $B(n-1)$ without controlling its endogenous arithmetic dependence.

## R3. Classical Selberg $O(x)$ remainder advertised as exponent resolution

O-RH-023 applies.

## R4. Sieve majorant without signed target fidelity

Upper-bound sieve control does not directly control PESC.

## R5. Hidden fixed zero strip

Any such input must be classified as breakthrough-strength.

## R6. Subpower advertised as fixed power

The target remains one fixed $\kappa>0$.

---

# 24. External calibration

The classical prime-only Selberg symmetry formula is

$$
\vartheta(x)\log x
+
\sum_{p\le x}
\log p\,
\vartheta(x/p)
=
2x\log x
+
O(x).
$$

Saidak's 2008 analysis of the $\psi$ version shows quantitatively how the error in Selberg's lemma tracks the PNT error after an explicit secondary main term is extracted.

These results support the classification of the Selberg route as a self-improvement framework whose fixed-power strengthening would itself require new arithmetic information.

---

# 25. State transition

The canonical transition is:

```text
CSM_RH v1.1
  ->
CSM_RH v1.2
```

with:

```text
Campaign 10
  CLOSED_AS_MINIMAL_PRIME_CORRELATION_REDUCTION

F-RH-009
  PODEE
  REMAINS OPEN

F-RH-010
  PESC
  CREATED / OPEN / EXACT-INTERFACE-EQUIVALENT TO PODEE

O-RH-022
  PRIME_SELF_SAMPLING_ENERGY_LOCK
  CREATED / CERTIFIED

O-RH-023
  SELBERG_OX_DIRECT_RESOLUTION_FLOOR
  CREATED / CERTIFIED AS DIRECT-MAGNITUDE OBSTRUCTION

S-RH-019
  ENDOGENOUS_PRIME_SAMPLING_CANCELLATION
  CREATED / OPEN

Campaign 11
  ENDOGENOUS_PRIME_SAMPLING_MECHANISM
  READY
```

---

# 26. Final status

```text
RH = OPEN

PODEE FIXED POWER = OPEN

PESC FIXED POWER = OPEN

PODEE <-> PESC
= EXACT AT FIXED EXPONENT

DECOMPOSITION SHELLS
= REMOVED FROM CANONICAL TARGET

CLASSICAL SELBERG O(x) RESOLUTION
= CRITICAL

GENERIC INDEPENDENCE HEURISTIC
= CIRCULAR

FIRST IRREDUCIBLE PRIME-CORRELATION LEMMA
= PESC

NEXT CAMPAIGN
= ENDOGENOUS PRIME-SAMPLING MECHANISM
```

The current arithmetic core is:

$$
\boxed{
\left|
\sum_{p<2N}
w_N(p)\log p
[
\vartheta(p-1)-(p-1)
]
-
\sum_{n<2N}
w_N(n)
[
\vartheta(n-1)-(n-1)
]
\right|
\ll
N^{3-\kappa+o(1)}
}
$$

for one fixed

$$
0<\kappa<\frac12.
$$

At the present closure state, that is the first genuinely new prime-distribution theorem required by this branch.
