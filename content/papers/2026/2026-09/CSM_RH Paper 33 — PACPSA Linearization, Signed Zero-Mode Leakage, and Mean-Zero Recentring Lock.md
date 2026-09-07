# CSM_RH Paper 33
## PACPSA Linearization, Signed Zero-Mode Leakage, and Mean-Zero Recentring Lock

**Project:** `CSM_RH`  
**Paper:** `33`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.23 / Paper 32`  
**Campaign:** `32 — PACPSA_DIFFERENCE_STABILITY_ATTACK`  
**Status:** coupled-sieve linearization audit / zero-mode obstruction localization; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 32 identified PACPSA difference stability as the only parity-side mechanism not yet closed.

Campaign 32 asks whether the Friedlander–Iwaniec asymptotic sieve can be linearized around the common positive background of the two PESC positivity lifts so that the sieve error depends on the signed perturbation rather than on the full positive mass.

The result is:

1. common-background cancellation is algebraically real;
2. modern Type-I/II sieve theory already demonstrates difference-level prime detection at arbitrary logarithmic precision;
3. the classical Friedlander–Iwaniec proof contains a separate signed zeroth-mode leakage proportional to the perturbation total;
4. forcing the perturbation total to vanish exports the same smooth drift into an exact rank-one PESC term;
5. therefore PACPSA difference stability by itself is not a lower-strength fixed-power mechanism.

No live GLM-5.3-Flash run is claimed.

---

# 1. The two PESC positivity lifts

Let

$$
c_n
=
\Lambda(n)-1
$$

or, after prime-power stripping, the prime-only centered detector.

Let

$$
B(j)
=
\sum_{n\le j}c_n.
$$

Define

$$
h_n
=
w_N(n)B(n-1).
$$

Choose

$$
M_N
\ge
\max_{j<2N}|B(j)|.
$$

The positive lifts are

$$
\boxed{
a_n^\pm
=
a_{0,n}
\pm
h_n,
}
$$

where

$$
\boxed{
a_{0,n}
=
M_Nw_N(n).
}
$$

Their prime-detection difference is exactly twice the signed PESC observable, up to the already certified prime-power correction.

Thus the common background is

$$
a_0
$$

and the perturbation is

$$
h.
$$

---

# 2. Exact linear cancellation before estimates

Every exact arithmetic identity linear in the input sequence satisfies

$$
\mathcal L(a^+)-\mathcal L(a^-)
=
2\mathcal L(h).
$$

Therefore, if a sieve proof could be carried out as a joint linear calculation before nonlinear estimates are applied, the common background cancels algebraically.

This is not merely hypothetical.

Modern Type-I/Type-II prime-detecting sieve theory explicitly works with a signed difference

$$
w_n=a_n-b_n
$$

between nonnegative sequences and derives prime-sum control from Type I and Type II information on $w$.

Thus:

```text
common-background cancellation:
  feasible in principle

fixed-power output:
  separate question
```

---

# 3. Friedlander–Iwaniec technical inputs

After their technical reduction, the Friedlander–Iwaniec proof uses:

## Type-I remainder input

$$
\boxed{
\sum_{d\le D}
\mu^2(d)\tau_5(d)
|r_d(t)|
\ll
A(x)(\log x)^{-3}.
}
$$

## Type-II / parity input

$$
\boxed{
\sum_m
\tau_5(m)
\left|
\sum_{\substack{
N<n\le2N\\
mn\le x
}}
\gamma(n)\mu(mn)a_{mn}
\right|
\ll
A(x)(\log x)^{-3}.
}
$$

For the PESC perturbation $h$, the derivative of the Type-II input is exactly the EMBF-type geometry already audited in Papers 13–15 and 31–32.

The Type-I derivative is a signed congruence-distribution problem for $h$.

Thus even ideal linearization does not make the analytic inputs disappear.

---

# 4. Section-6 main leakage in the classical proof

The Friedlander–Iwaniec proof contains a term $S_1$ whose congruence sums are replaced by their main density plus remainders.

At the main-term level they obtain

$$
\boxed{
|S_1|
\le
A(x)L(x)M(x)
+
O
\left(
A(x)(\log x)^{-2}
\right),
}
$$

with

$$
\boxed{
L(x)\ll\log\delta,
}
$$

and

$$
\boxed{
M(x)\ll\frac1{\log\Delta}.
}
$$

Therefore

$$
\boxed{
S_1
\ll
A(x)
\frac{\log\delta}{\log\Delta}.
}
$$

This term is produced by the main-density component of the proof, not merely by independent remainder errors.

The authors explicitly describe this estimate as tight within their method.

---

# 5. Difference-level Section-6 leakage

Suppose the same proof architecture is jointly linearized for

$$
a^\pm=a_0\pm h.
$$

The common $a_0$ contribution cancels.

But the Section-6 main-density contribution is linear in the total input mass.

Hence the difference retains

$$
\boxed{
H_h
\frac{\log\delta}{\log\Delta},
}
$$

where

$$
\boxed{
H_h
=
\sum_{n<2N}h_n
=
\sum_{n<2N}
w_N(n)B(n-1).
}
$$

Create:

```text
O-RH-072
FI_SECTION6_SIGNED_ZERO_MODE_LEAKAGE
status:
  CERTIFIED AS CURRENT-PROOF-ARCHITECTURE AUDIT
```

Statement:

> Perfect cancellation of the common positive background does not remove the classical asymptotic-sieve zeroth-mode leakage. In the difference problem, that leakage is proportional to the total signed perturbation itself.

This is a statement about the audited Friedlander–Iwaniec architecture.

It is not a universal impossibility theorem for every future coupled sieve.

---

# 6. Exact integrated form of the perturbation total

By the definition of $w_N$,

$$
\boxed{
H_h
=
\sum_{j=N}^{2N-1}
\sum_{n\le j}
B(n-1).
}
$$

Thus $H_h$ is a second integrated moment of the cumulative prime error.

For a smooth drift

$$
B(x)\asymp x^\beta,
$$

with fixed

$$
0<\beta<1,
$$

we have

$$
\boxed{
H_h
\asymp
N^{\beta+2}.
}
$$

If

$$
\beta\uparrow1,
$$

this is

$$
N^{3-o(1)}.
$$

Therefore multiplying by any fixed inverse logarithmic relative factor remains

$$
N^{3-o(1)}.
$$

It does not yield a fixed PESC exponent.

---

# 7. Endpoint weight total

Define

$$
\boxed{
W_N
=
\sum_{n<2N}w_N(n).
}
$$

For the canonical endpoint weight,

$$
\boxed{
W_N
=
\frac{
3N^2-N
}{2}.
}
$$

Define the weighted mean of the cumulative error

$$
\boxed{
\overline B_N
=
\frac{H_h}{W_N}.
}
$$

---

# 8. Mean-zero recentering

Define the mean-zero perturbation

$$
\boxed{
\widetilde h_n
=
w_N(n)
[
B(n-1)-\overline B_N
].
}
$$

Then

$$
\boxed{
\sum_n\widetilde h_n=0.
}
$$

This kills the Section-6 zeroth-mode term at the formal signed-input level.

However PESC decomposes exactly as follows.

Let

$$
\boxed{
G_N
=
\sum_{n<2N}
w_N(n)c_n.
}
$$

Then

## Theorem 8.1 — Mean-Zero PESC Recentring Identity

$$
\boxed{
\mathcal C_N
=
\sum_{n<2N}
c_n\widetilde h_n
+
\overline B_NG_N.
}
$$

Moreover,

$$
\boxed{
G_N
=
\sum_{j=N}^{2N-1}B(j).
}
$$

Create:

```text
B-RH-009
MEAN_ZERO_PESC_RECENTERING_IDENTITY
status:
  CERTIFIED
```

---

# 9. Rank-one drift term

The scalar correction is

$$
\boxed{
\mathcal R_N^{(1)}
=
\overline B_NG_N
=
\frac{
H_hG_N
}{
W_N
}.
}
$$

For a smooth real drift

$$
B(x)\asymp x^\beta,
$$

we have

$$
H_h
\asymp
N^{\beta+2},
$$

$$
G_N
\asymp
N^{\beta+1},
$$

and

$$
W_N
\asymp
N^2.
$$

Hence

## Theorem 9.1 — Rank-One Drift Scale

$$
\boxed{
\mathcal R_N^{(1)}
\asymp
N^{2\beta+1}.
}
$$

This is exactly the same exponent as the PESC smooth-drift self-correlation.

Thus forcing the perturbation total to vanish does not remove the hard low-frequency mode.

It exports it into a rank-one scalar product.

Create:

```text
O-RH-073
MEAN_ZERO_RECENTERING_RANK_ONE_DRIFT_LOCK
status:
  CERTIFIED AS FIXED-MODE STRENGTH AUDIT
```

---

# 10. Why the recentering term is not lower strength

PESC $(\kappa)$ has target scale

$$
N^{3-\kappa}.
$$

The rank-one smooth-drift term has scale

$$
N^{2\beta+1}.
$$

Thus the same exponent comparison appears:

$$
2\beta+1
\le
3-\kappa
$$

only if

$$
\boxed{
\beta
\le
1-\frac{\kappa}{2}.
}
$$

Therefore the mean-zero trick merely moves the fixed-strip-sensitive component out of the signed sieve perturbation and into an explicit scalar.

It does not weaken the fixed-exponent problem.

---

# 11. Modern Ford–Maynard difference-level sieve

Modern prime-detecting sieve theory provides an important calibration.

Let

$$
w_n=a_n-b_n
$$

be the signed difference of two nonnegative sequences.

Under suitable Type I and Type II ranges and growth hypotheses, Ford and Maynard prove, in the asymptotic parameter region, that for every fixed

$$
A>1,
$$

$$
\boxed{
\sum_p w_p
\ll_A
\frac{x}{(\log x)^A}.
}
$$

Thus:

```text
difference-level prime detection:
  already feasible

common-background cancellation:
  already feasible

quantitative class:
  arbitrary log-power
```

This shows that PACPSA's conceptual coupling is not the missing invention.

The missing ingredient is fixed-power signed arithmetic information.

---

# 12. Modern Type-I/II limitations

The same modern theory constructs bounded nonnegative sequences satisfying nontrivial Type I and Type II estimates but containing no primes when the Type II information is below the necessary range.

It also gives necessary-and-sufficient combinatorial criteria for an asymptotic to follow from specified Type I/II ranges.

Thus generic Type I/II information has sharp structural limits.

This supports the following Campaign-32 conclusion:

> a fixed-power PESC theorem cannot be obtained merely by declaring the two lifts coupled. The signed perturbation must carry genuinely stronger Type I/II information than current logarithmic residual/parity technology supplies.

---

# 13. Signed Type-I derivative debt

For the perturbation $h$, define its divisibility sums

$$
H_d(x)
=
\sum_{\substack{n\le x\\d\mid n}}
h_n.
$$

For a chosen density $g(d)$, define

$$
\boxed{
r_d^{(h)}(x)
=
H_d(x)-g(d)H_h(x).
}
$$

A difference-level version of the Friedlander–Iwaniec proof still requires strong aggregate control of these signed remainders.

This is not supplied automatically by:

```text
positivity-lift coupling;
EMBF parity cancellation;
Lambda-sharp subtraction;
almost-all short-interval uniformity.
```

The Type-II derivative is EMBF-like.

The signed Type-I derivative is a separate endogenous distribution debt.

No new frontier is created for it because no fixed-power bridge weaker than PESC is proved.

---

# 14. Bilinear derivative stability

The Friedlander–Iwaniec bilinear axiom contains an outer absolute value.

Paper 32 proved that this is dual uniformity over arbitrary outer phases.

Linearizing

$$
a_t=a_0+th
$$

inside the inner bilinear sum is exact.

But differentiating the seminorm itself produces phase/sign dependence determined by the current inner sums.

Thus a derivative theorem still requires uniform control over the dual outer phases.

The derivative does not eliminate EMBF.

---

# 15. PACPSA status after the linearization audit

Paper 15 originally introduced PACPSA as a power-accurate coupled parity-sieve assembly.

Paper 32 sharpened it into difference-level stability.

Campaign 32 sharpens it again.

Difference stability alone is insufficient because:

1. the signed perturbation has its own zeroth-mode leakage in the classical FI architecture;
2. mean-zero recentering exports the same drift to the rank-one term $\overline B_NG_N$ ;
3. signed Type-I and Type-II derivative estimates are still required;
4. current modern difference-level sieve theory yields arbitrary logarithmic, not fixed-power, accuracy from standard Type-I/II hypotheses.

Therefore PACPSA changes state to:

```text
F-RH-014
PACPSA
status:
  NOT SUFFICIENT AS DIFFERENCE-STABILITY ALONE
role:
  AUXILIARY COUPLED-SIEVE PROGRAM
```

It is no longer the unique surviving parity-side lower-strength mechanism.

---

# 16. New obstruction: coupled-sieve zero mode

Create:

```text
O-RH-074
COUPLED_SIEVE_ZERO_MODE_SURVIVES_BACKGROUND_CANCELLATION
status:
  CERTIFIED AS CURRENT-METHOD CLOSURE
```

Statement:

> Cancelling the common positive background of the two PESC lifts does not cancel the zeroth mode of the signed perturbation. In the classical asymptotic-sieve proof this mode appears explicitly in the Section-6 relative leakage; forcing it to zero merely exports the same smooth drift into a rank-one PESC-scale scalar.

---

# 17. Campaign 32 track audit

## D1 — common-background linearization

```text
status:
  ALGEBRAICALLY VALID

modern precedent:
  Ford-Maynard signed difference w=a-b

fixed-power consequence:
  NO
```

## D2 — signed remainder axioms

```text
status:
  STILL REQUIRED

Type I:
  signed divisibility remainder debt

Type II:
  EMBF-like parity bilinear
```

## D3 — bilinear derivative stability

```text
status:
  OUTER-PHASE UNIFORMITY REMAINS

no free derivative gain
```

## D4 — Jordan / polarization

```text
status:
  MEAN-ZERO RECENTERING AVAILABLE

hard mode:
  exported to rank-one scalar
```

## D5 — difference-level prime detection

```text
status:
  MODERN LOG-POWER VERSION EXISTS

fixed-power version:
  NOT OBTAINED
```

---

# 18. Campaign 32 verdict

No fixed-power theorem is proved.

The parity branch is now classified as follows:

```text
parity breaking:
  understood structurally

difference-level coupling:
  feasible

common positive background:
  removable

signed perturbation zero mode:
  still hard

signed Type-I/Type-II power information:
  unavailable

current output:
  log/subpower

lower-strength fixed-power parity route:
  not identified
```

The root target remains PESC.

---

# 19. Canonical status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN / DIRECT THEOREM CANDIDATE

F-RH-012
EMBF
AUXILIARY

F-RH-014
PACPSA
AUXILIARY / NOT SUFFICIENT AS DIFFERENCE-STABILITY ALONE
```

No new frontier is created.

---

# 20. Campaign 33

The next campaign is:

```text
CSM_RH Campaign 33
PESC_LOW_FREQUENCY_RANK_ONE_ATTACK
```

The new target is not a new criterion.

It is the exact low-frequency scalar exposed by mean-zero recentering:

$$
\boxed{
\mathcal R_N^{(1)}
=
\frac{
H_hG_N
}{
W_N
}.
}
$$

The campaign asks whether this scalar can be controlled by a theorem weaker than full PESC.

---

# 21. Campaign 33 tracks

## ZM1 — first/second primitive Mellin analysis

Study

$$
G_N
=
\sum_{j=N}^{2N-1}B(j)
$$

and

$$
H_h
=
\sum_{j=N}^{2N-1}
\sum_{r<j}B(r)
$$

as Mellin observables.

Determine their exact zero-mode sensitivity.

## ZM2 — scalar-product cancellation

Test whether

$$
H_hG_N
$$

has cancellation unavailable in either factor separately.

A pure power-mode countermodel must be passed.

## ZM3 — dyadic phase variation

For a complex Mellin mode $N^\rho$, study whether dyadic changes in phase can force cancellation of the rank-one scalar over several scales.

Uniform fixed-power conclusions must survive near-resonant ordinates.

## ZM4 — arithmetic control of the first primitive

Seek a prime theorem for $G_N$ weaker than PESC but strong enough, together with current control of $H_h$, to make the rank-one term fixed-power small.

## ZM5 — direct covariance decomposition

Interpret PESC as weighted covariance plus the rank-one mean product.

Test whether the covariance part admits a genuinely lower-strength sieve theorem.

---

# 22. Campaign 33 rejection filters

Reject a candidate if:

## R1. It assumes fixed-power bounds for both $G_N$ and $H_h$.

## R2. It merely restates the PESC smooth-drift exponent test.

## R3. It uses a fixed zero-free strip.

## R4. It uses only arbitrary logarithmic PNT error.

## R5. It relies on cancellation of complex zero modes without a uniform coefficient-recovery argument.

## R6. It creates another positive moment frontier.

---

# 23. External calibration

Two sieve frameworks are relevant to this audit.

1. Friedlander–Iwaniec's asymptotic sieve works with real nonnegative input sequences and proves a relative error
   $$
   O
   \left(
   \frac{\log\delta}{\log\Delta}
   \right).
   $$
   In Section 6 their main-density term is bounded by
   $$
   A(x)
   \frac{\log\delta}{\log\Delta}.
   $$

2. Ford–Maynard's modern theory works explicitly with signed differences
   $$
   w=a-b
   $$
   between nonnegative sequences and proves arbitrary logarithmic prime-sum accuracy when the Type I/II parameter ranges satisfy their asymptotic criterion. The same theory gives counterexamples outside the sufficient region.

Together these show:

```text
coupling is possible;
fixed-power endogenous information remains the missing part.
```

---

# 24. State transition

```text
CSM_RH v1.23
  ->
CSM_RH v1.24
```

with:

```text
Campaign 32
  CLOSED_AS_PACPSA_LINEARIZATION_AND_ZERO_MODE_AUDIT

B-RH-009
  MEAN_ZERO_PESC_RECENTERING_IDENTITY
  CREATED / CERTIFIED

O-RH-072
  FI_SECTION6_SIGNED_ZERO_MODE_LEAKAGE
  CREATED / CERTIFIED AS CURRENT-PROOF-ARCHITECTURE AUDIT

O-RH-073
  MEAN_ZERO_RECENTERING_RANK_ONE_DRIFT_LOCK
  CREATED / CERTIFIED AS FIXED-MODE STRENGTH AUDIT

O-RH-074
  COUPLED_SIEVE_ZERO_MODE_SURVIVES_BACKGROUND_CANCELLATION
  CREATED / CERTIFIED AS CURRENT-METHOD CLOSURE

F-RH-014
  PACPSA
  DEMOTED TO AUXILIARY COUPLED-SIEVE PROGRAM

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 33
  PESC_LOW_FREQUENCY_RANK_ONE_ATTACK
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

COMMON BACKGROUND CANCELLATION = FEASIBLE

MODERN DIFFERENCE-LEVEL PRIME SIEVE = LOG-POWER FEASIBLE

FI DIFFERENCE ZERO MODE = SURVIVES

MEAN-ZERO RECENTERING = EXACT

RECENTERED RANK-ONE DRIFT TERM = PESC-SCALE ON POWER MODES

PACPSA DIFFERENCE STABILITY ALONE = INSUFFICIENT

LOWER-STRENGTH PARITY FIXED-POWER ROUTE = NOT IDENTIFIED

NEXT CAMPAIGN = 33
```

The two decisive identities are

$$
\boxed{
H_h
=
\sum_{n<2N}w_N(n)B(n-1)
}
$$

and

$$
\boxed{
\mathcal C_N
=
\sum_n
c_nw_N(n)
[
B(n-1)-\overline B_N
]
+
\frac{
H_hG_N
}{
W_N
}.
}
$$

The common positive sieve background can be removed.

The low-frequency prime-error mode cannot.
