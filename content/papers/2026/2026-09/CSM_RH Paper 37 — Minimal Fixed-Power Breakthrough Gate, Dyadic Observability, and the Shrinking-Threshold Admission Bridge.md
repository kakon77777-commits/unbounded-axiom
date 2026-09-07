# CSM_RH Paper 37
## Minimal Fixed-Power Breakthrough Gate, Dyadic Observability, and the Shrinking-Threshold Admission Bridge

**Project:** `CSM_RH`  
**Paper:** `37`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.27 / Paper 36`  
**Campaign:** `36 — MINIMAL_FIXED_POWER_BREAKTHROUGH_GATE`  
**Status:** breakthrough-gate audit / no arithmetic candidate admitted; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Papers 17–36 generated and then audited a large family of possible surrogates:

```text
lag energies;
fourth moments;
fully distinct correlations;
sieve-model residuals;
Selberg amplifiers;
parity bilinears;
coupled sieves;
rank-one low-frequency coordinates;
finite-rank projections;
rational/Stieltjes filters;
Müntz filters.
```

Campaign 36 imposes a stricter rule:

> no object counts as progress merely because it has a fixed-power theorem somewhere. The theorem must observe the RH-hard prime-error mode and possess a proved deterministic bridge back to PESC or the fixed-power PNT mean square.

Under this gate, no current candidate is admitted.

The campaign nevertheless produces:

1. a precise dyadic-observability rejection test;
2. an exact counterexample showing why a known fixed-power transformed prime theorem does not qualify;
3. a deterministic shrinking-threshold exceptional-set bridge to MLEPG;
4. a single narrow next campaign.

No live GLM-5.3-Flash run is claimed.

---

# 1. Breakthrough-gate rules

A candidate theorem is admitted only if all of the following are present.

## G1 — genuinely arithmetic estimate

There must be a proved estimate for the prime / von-Mangoldt sequence, not merely an approximation-theory or representation theorem.

## G2 — fixed exponent

The conclusion must contain a fixed positive power of the main scale.

Allowed:

$$
X^{-\delta},
\qquad
\delta>0
\text{ fixed}.
$$

Not sufficient:

$$
(\log X)^{-A},
$$

$$
\exp[-(\log X)^c],
\qquad
0<c<1,
$$

or any

$$
X^{-o(1)}.
$$

## G3 — no fixed-strip input

The fixed exponent may not be imported from an assumed fixed zero-free half-plane.

## G4 — root observability

The observable must actually see the dyadic cumulative prime-error / principal low-frequency mode.

## G5 — proved deterministic bridge

There must be a rigorous route from the estimate to one of:

```text
F-RH-010 PESC;
F-RH-016 MLEPG;
fixed-power PNT mean-square.
```

---

# 2. Why fixed power alone is not enough

There exist genuine fixed-power theorems involving the von Mangoldt function which do not control the ordinary prime number theorem.

A useful test case is the quotient transform

$$
\boxed{
(Tf)(x)
=
\sum_{1\le n\le x}
f
\left(
\left\lfloor
\frac{x}{n}
\right\rfloor
\right).
}
$$

Wei Zhang proved a fixed-power asymptotic for $f=\Lambda$:

$$
\boxed{
(T\Lambda)(x)
=
C_\Lambda x
+
O_\varepsilon
\left(
x^{7/15+1/195+\varepsilon}
\right).
}
$$

The exponent is approximately

$$
0.47179.
$$

This is a real arithmetic fixed-power theorem.

It nevertheless fails the CSM_RH breakthrough gate.

---

# 3. Exact quotient-transform weight identity

Define

$$
\boxed{
\Delta_m(x)
=
\left\lfloor
\frac{x}{m}
\right\rfloor
-
\left\lfloor
\frac{x}{m+1}
\right\rfloor.
}
$$

Grouping by the value

$$
m=
\left\lfloor
\frac{x}{n}
\right\rfloor
$$

gives:

## Theorem 3.1 — Quotient Weight Identity

$$
\boxed{
(Tf)(x)
=
\sum_{m\le x}
f(m)\Delta_m(x).
}
$$

The transform is therefore a sparse weighted sampler of $f$.

---

# 4. Sparse support of the quotient weights

The number of indices with

$$
\Delta_m(x)\ne0
$$

is at most

$$
\boxed{
2\lfloor\sqrt x\rfloor+1.
}
$$

Indeed:

1. there are at most $\sqrt x$ possible indices $m\le\sqrt x$ ;
2. if $m>\sqrt x$ and $\Delta_m(x)>0$, then $m=\lfloor x/n\rfloor$ for some $n<\sqrt x$, giving at most another $\sqrt x$ values.

Thus a length- $x$ arithmetic sequence is sampled at only

$$
O(\sqrt x)
$$

positions by one quotient transform.

---

# 5. Exact dyadic blindness countermodel

Fix a scale $X$ and define

$$
\boxed{
g_X(m)
=
1_{X<m\le2X}.
}
$$

For every integer

$$
X<x\le2X,
$$

the $n=1$ term gives

$$
g_X(x)=1.
$$

For every

$$
n\ge2,
$$

we have

$$
\left\lfloor
\frac{x}{n}
\right\rfloor
\le X,
$$

and hence the corresponding term vanishes.

Therefore:

## Theorem 5.1 — Exact Dyadic Blindness

$$
\boxed{
(Tg_X)(x)=1
\qquad
(X<x\le2X).
}
$$

But the dyadic cumulative mass is

$$
\boxed{
\sum_{X<m\le2X}g_X(m)
=
X.
}
$$

A transform error as strong as

$$
O(1)
$$

is therefore compatible with maximal linear dyadic mass.

---

# 6. Dyadic observability obstruction

Create:

```text
O-RH-086
QUOTIENT_TRANSFORM_DYADIC_OBSERVABILITY_FAILURE
status:
  CERTIFIED
```

Statement:

> Fixed-power control of a sparse quotient transform does not deterministically control the cumulative error on the current dyadic block.

This is sufficient to reject the quotient-PNT fixed-power theorem from the PESC breakthrough gate.

The rejection does not diminish the theorem itself.

It only distinguishes:

```text
fixed power in a smoothed/sparse transformed observable

from

fixed power in an RH-observing prime-error observable.
```

---

# 7. Root-observability requirement

The quotient example motivates a general gate rule.

A candidate linear observable

$$
\mathcal L_X(a)
$$

must be tested against adversarial dyadic perturbations.

If there exists a family $g_X$ with

$$
\left|
\mathcal L_x(g_X)
\right|
=
X^{o(1)}
$$

throughout the current dyadic scale while

$$
\left|
\sum_{X<n\le2X}g_X(n)
\right|
=
X^{1-o(1)},
$$

then the observable has no deterministic fixed-power bridge to the ordinary cumulative prime error without additional arithmetic information.

Create:

```text
O-RH-087
FIXED_POWER_WITHOUT_ROOT_OBSERVABILITY_NOT_ADMISSIBLE
status:
  CERTIFIED AS CAMPAIGN-GATE PRINCIPLE
```

---

# 8. Current direct PESC calibration

Let

$$
B(x)=\vartheta(x)-x.
$$

The best unconditional PNT remainder remains subpower relative to $x$.

Current zero-free-region / zero-density refinements yield errors of the form

$$
\boxed{
B(x)
\ll
x
\exp
[
-\omega(x)
],
}
$$

where

$$
\omega(x)
=
o(\log x)
$$

and in the Vinogradov–Korobov class is of order

$$
(\log x)^{3/5}
(\log\log x)^{-1/5}.
$$

Hence

$$
B(x)
=
x^{1-o(1)}.
$$

Inserted into the direct PESC absolute-value bound, this remains only

$$
\boxed{
\mathcal C_N
\ll
N^{3-o(1)}.
}
$$

No fixed PESC exponent is currently obtained.

---

# 9. Direct MLEPG calibration

Recall

$$
U_H(x)
=
\sum_{x<n\le x+H}
[
\Lambda(n)-1
].
$$

The lag energy is

$$
\boxed{
\mathcal S_\Lambda(X,H)
=
\int_X^{2X}
|U_H(x)|^2
\,dx
}
$$

up to discrete/endpoint conventions.

Current 2026 higher-uniformity technology gives, for suitable polynomial $H$, residual estimates with arbitrary fixed logarithmic precision on almost all intervals.

For the prime residual this remains:

$$
\boxed{
H(\log X)^{-A}
}
$$

rather than

$$
HX^{-\eta}.
$$

Thus the available input produces subpower rather than fixed-power MLEPG.

No candidate is admitted.

---

# 10. Guth–Maynard range improvement is not a precision exponent

The 2026 Guth–Maynard large-value theorem gives the zero-density estimate

$$
\boxed{
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}
}
$$

and asymptotics for primes in all short intervals at the scale

$$
x^{17/30+o(1)}.
$$

Combined with the exceptional-set framework, one obtains almost-all short-interval PNT down to

$$
\theta>\frac{2}{15}.
$$

This is a major range improvement.

But:

```text
shorter admissible H:
  range gain

polynomially shrinking relative error:
  not supplied

fixed MLEPG exponent:
  not supplied
```

Range and precision remain distinct coordinates.

---

# 11. Gafni–Tao exceptional-set theorem remains fixed-threshold

Let

$$
\mathcal E_\delta(X,\theta)
$$

denote the set on which the short-interval PNT fails by a fixed relative threshold $\delta$.

The Gafni–Tao exceptional-set exponents are defined with

$$
\boxed{
\delta>0
\text{ fixed}.
}
$$

In the proof they explicitly:

```text
fix delta;
choose J sufficiently large depending on delta, theta, epsilon;
let X tend to infinity with J, delta, theta, epsilon fixed.
```

The resulting bounds contain constants depending on

$$
\delta,\theta,J,\varepsilon.
$$

Therefore the theorem as stated does not authorize the substitution

$$
\boxed{
\delta=X^{-\eta}.
}
$$

This confirms the fixed-threshold mismatch identified in Paper 19.

---

# 12. The shrinking-threshold condition that would pass the gate

The exact missing shape can now be stated.

Let

$$
H=X^\alpha,
\qquad
0<\alpha<1.
$$

Assume there exist fixed

$$
\eta>0,
\qquad
c>0
$$

such that

$$
\boxed{
\left|
\left\{
x\in[X,2X]:
|U_H(x)|
>
HX^{-\eta}
\right\}
\right|
\ll
X^{1-c}.
}
$$

Call this a shrinking-threshold exceptional-set estimate.

This is not currently claimed as a theorem.

---

# 13. Shrinking-threshold to MLEPG bridge

On the good set,

$$
|U_H(x)|^2
\le
H^2X^{-2\eta}.
$$

On every interval, the elementary bound gives

$$
|U_H(x)|
\ll
H\log X.
$$

Hence the bad-set contribution is

$$
\ll
X^{1-c}
H^2
(\log X)^2.
$$

Therefore:

## Theorem 13.1 — Shrinking-Threshold Exceptional Set to Lag Energy

If Section 12 holds, then

$$
\boxed{
\mathcal S_\Lambda(X,H)
\ll
XH^2X^{-2\eta}
+
X^{1-c}H^2(\log X)^2.
}
$$

Equivalently,

$$
\boxed{
\mathcal S_\Lambda(X,H)
\ll
XH^2
X^{-\delta+o(1)},
}
$$

where

$$
\boxed{
\delta
=
\min
\{
2\eta,c
\}.
}
$$

This is stronger than the second term required by MLEPG.

Create:

```text
B-RH-012
SHRINKING_THRESHOLD_EXCEPTIONAL_SET_TO_MLEPG
status:
  CERTIFIED
```

---

# 14. Consequence for the global fixed strip

By Paper 17's corrected residue-chain inequality,

$$
\sum_{n\le2N}|A(n)|^2
\ll
\left(
\frac NH
\right)^2
\mathcal S_\Lambda(N,H)
+
NH^2,
$$

where

$$
A(x)=\psi(x)-x.
$$

With

$$
H=N^\alpha
$$

and Theorem 13.1, one gets a fixed global mean-square exponent whenever

$$
0<\alpha<1
$$

and

$$
\eta,c>0
$$

are fixed.

For sufficiently small fixed $\kappa$,

$$
\boxed{
\kappa
<
\min
\{
\alpha,
2\eta,
c,
2-2\alpha
\}.
}
$$

The Mellin-pole bridge then excludes zeros in

$$
\Re s>1-\kappa/2.
$$

Thus the shrinking-threshold arithmetic estimate would genuinely pass Campaign 36.

---

# 15. Why current logarithmic thresholds fail the bridge

If instead

$$
|U_H(x)|
\le
H(\log X)^{-A}
$$

outside an exceptional set of size

$$
X(\log X)^{-A},
$$

then the same good/bad decomposition gives only inverse powers of $\log X$.

At polynomial $H$ these are

$$
X^{-o(1)}.
$$

No fixed $\delta$ in Theorem 13.1 is generated.

Thus the gate cleanly separates:

```text
arbitrary fixed logarithmic accuracy

from

polynomially shrinking threshold accuracy.
```

---

# 16. Principal Fejer route

Paper 18 established that the complete triangular lag aggregate is the positive Fejer energy

$$
\int_0^1
|S_X(\alpha)|^2
|D_H(\alpha)|^2
\,d\alpha.
$$

On the principal arc

$$
\|\alpha\|
\le
c/H,
$$

one has

$$
|D_H(\alpha)|^2
\gg
H^2.
$$

Therefore any fixed-power MLEPG theorem must control the principal $q=1$ low-frequency component at fixed-power strength.

Current minor-arc or non-principal-phase fixed-power exponential-sum theorems do not remove this principal contribution.

No candidate is admitted.

---

# 17. Prime-specific scale recurrence

The exact contraction identities of Papers 21–23 remain valid.

But fixed power requires cumulative contraction mass

$$
\Omega(\log X).
$$

Current unconditional prime information supplies at best sublinear contraction mass in the audited positive-defect routes.

No new prime-specific signed recurrence with linear contraction mass is currently proved.

No candidate is admitted.

---

# 18. Campaign 36 admission table

## Candidate A — direct PESC

```text
fixed-power arithmetic estimate:
  NO

verdict:
  REJECT / OPEN ROOT
```

## Candidate B — direct MLEPG

```text
fixed-power arithmetic estimate:
  NO

current precision:
  log/subpower

verdict:
  REJECT / OPEN
```

## Candidate C — Gafni–Tao exceptional set

```text
power-sized exceptional set:
  YES IN MANY RANGES

relative threshold:
  FIXED DELTA

polynomially shrinking threshold:
  NOT AUTHORIZED

verdict:
  REJECT
```

## Candidate D — Guth–Maynard short intervals

```text
range breakthrough:
  YES

fixed relative power precision:
  NO

verdict:
  REJECT FOR THIS GATE
```

## Candidate E — quotient-transform PNT

```text
fixed-power theorem:
  YES

root observability:
  FAILS

deterministic PESC bridge:
  NO

verdict:
  REJECT
```

## Candidate F — principal Fejer fixed power

```text
would pass gate:
  YES

currently proved:
  NO
```

## Candidate G — shrinking-threshold short interval

```text
would pass gate:
  YES

direct bridge:
  B-RH-012

currently proved:
  NO
```

---

# 19. Campaign 36 verdict

No candidate is admitted.

This is an intentional successful outcome of the gate.

```text
new fixed-power arithmetic theorem admitted:
  NONE

false-positive fixed-power theorem detected:
  quotient transform

new deterministic bridge:
  B-RH-012

root target:
  unchanged
```

The state is not advanced by inventing another equivalent criterion.

It is advanced by making the admission boundary explicit.

---

# 20. New certified package

Create:

```text
O-RH-086
QUOTIENT_TRANSFORM_DYADIC_OBSERVABILITY_FAILURE
CERTIFIED

O-RH-087
FIXED_POWER_WITHOUT_ROOT_OBSERVABILITY_NOT_ADMISSIBLE
CERTIFIED AS CAMPAIGN-GATE PRINCIPLE

B-RH-012
SHRINKING_THRESHOLD_EXCEPTIONAL_SET_TO_MLEPG
CERTIFIED
```

No new frontier is created.

---

# 21. Canonical status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN / DIRECT THEOREM CANDIDATE

Campaign-36 admitted fixed-power theorem:
  NONE
```

---

# 22. Campaign 37

The next campaign is deliberately narrow:

```text
CSM_RH Campaign 37
SHRINKING_THRESHOLD_TAIL_ATTACK
```

It does not create a new canonical frontier.

Its sole objective is to determine whether the Gafni–Tao / Guth–Maynard exceptional-set machinery can be quantified when the relative threshold shrinks as a power of $X$.

---

# 23. Campaign 37 tracks

## ST1 — explicit delta dependence

Re-read the exceptional-set proof and expose every dependence on the fixed threshold $\delta$.

Track:

```text
subdivision count;
choice of J;
explicit-formula truncation;
Markov threshold;
L2/L4 zero-sum estimates;
implied constants.
```

## ST2 — polynomially shrinking substitution

Set

$$
\delta=X^{-\eta}.
$$

Allow

$$
J=J(X)
$$

if necessary.

Track the effect on

$$
T
=
J(\log X)^2X^{1-\alpha}
$$

and therefore on every zero-density exponent.

## ST3 — Guth–Maynard density insertion

Insert

$$
A_0=\frac{30}{13}
$$

and determine whether there exists any open region

$$
(\alpha,\eta,c)
$$

with

$$
\eta>0,
\qquad
c>0
$$

for which the shrinking-threshold exceptional-set estimate survives.

## ST4 — layer-cake / second-moment optimization

If threshold-dependent tail estimates exist, integrate the full tail instead of using one threshold.

Target:

$$
\mathcal S_\Lambda(X,H)
\ll
XH^2X^{-\delta_0}.
$$

## ST5 — no hidden fixed-strip source

Reject any power which ultimately comes from assuming a fixed zero-free strip.

The exponent must emerge from large-value / zero-density / exceptional-set arithmetic alone.

---

# 24. Campaign 37 hard rejects

Reject:

```text
delta fixed while being described as shrinking;
A=A(X) inside an O_A theorem without uniformity;
J growing while T is still treated as X^(1-alpha+o(1)) without checking;
fixed zero-free strip input;
only logarithmic threshold;
power exceptional set with constant relative error;
new transformed prime observable without dyadic observability.
```

---

# 25. External calibration

The Campaign-36 audit uses the following current facts.

1. Guth–Maynard 2026 prove
   $$
   N(\sigma,T)
   \le
   T^{30(1-\sigma)/13+o(1)}
   $$
   and short-interval prime asymptotics at the $17/30$ all-interval scale.

2. Gafni–Tao 2026 quantify exceptional-set exponents and recover almost-all PNT for
   $$
   \theta>\frac{2}{15}.
   $$
   Their exceptional-set definitions and proof fix the relative threshold $\delta$ before taking $X\to\infty$.

3. Matomäki–Radziwiłł–Shao–Tao–Teräväinen 2026 give arbitrary fixed logarithmic precision for $\Lambda-\Lambda^\sharp$ on almost all polynomial short intervals in their range.

4. Current PNT remainder improvements based on Vinogradov–Korobov zero-free regions remain of the class
   $$
   x\exp[-o(\log x)]
   =
   x^{1-o(1)}.
   $$

5. Fixed-power estimates do exist for some transformed von-Mangoldt observables, such as the quotient transform, demonstrating why root observability is a necessary extra gate condition.

---

# 26. State transition

```text
CSM_RH v1.27
  ->
CSM_RH v1.28
```

with:

```text
Campaign 36
  CLOSED_WITH_NO_ADMITTED_FIXED_POWER_THEOREM

O-RH-086
  QUOTIENT_TRANSFORM_DYADIC_OBSERVABILITY_FAILURE
  CREATED / CERTIFIED

O-RH-087
  FIXED_POWER_WITHOUT_ROOT_OBSERVABILITY_NOT_ADMISSIBLE
  CREATED / CERTIFIED

B-RH-012
  SHRINKING_THRESHOLD_EXCEPTIONAL_SET_TO_MLEPG
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 37
  SHRINKING_THRESHOLD_TAIL_ATTACK
  READY
```

---

# 27. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

BREAKTHROUGH GATE = ACTIVE

CURRENT ADMITTED FIXED-POWER PRIME THEOREM = NONE

FIXED-POWER TRANSFORMED PRIME THEOREMS = NOT ENOUGH WITHOUT ROOT OBSERVABILITY

GUTH-MAYNARD = RANGE BREAKTHROUGH, NOT FIXED-PRECISION BREAKTHROUGH

GAFNI-TAO = POWER EXCEPTIONAL-SET TECHNOLOGY AT FIXED RELATIVE THRESHOLD

SHRINKING-THRESHOLD POWER EXCEPTIONAL SET = OPEN

NEXT CAMPAIGN = 37
```

The one theorem shape which now matters is:

$$
\boxed{
\left|
\{
x:
|U_H(x)|>HX^{-\eta}
\}
\right|
\ll
X^{1-c}.
}
$$

If proved for any fixed positive $\eta$ and $c$ at one polynomial scale $H=X^\alpha$, it passes the gate and feeds directly into MLEPG.

Everything else remains calibration.
