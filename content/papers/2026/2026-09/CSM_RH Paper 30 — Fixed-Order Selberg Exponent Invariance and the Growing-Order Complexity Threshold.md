# CSM_RH Paper 30
## Fixed-Order Selberg Exponent Invariance and the Growing-Order Complexity Threshold

**Project:** `CSM_RH`  
**Paper:** `30`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.20 / Paper 29`  
**Campaign:** `29 — HIGHER_ORDER_SELBERG_AMPLIFIER_ATTACK`  
**Status:** generalized-von-Mangoldt amplifier audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 29 showed that the classical fixed-order Selberg feedback is forcing-critical for every fixed Mellin mode $x^\rho$ with $\Re\rho<1$.

Campaign 29 tests whether generalized von Mangoldt functions

$$
\Lambda_k
=
\mu*\log^k
$$

can amplify this feedback into a fixed polynomial drift gap.

The result is:

```text
fixed k:
  exponent-neutral

finite fixed-order combinations:
  no certified remainder cancellation

slowly growing k:
  can amplify logarithmic/subpower precision

fixed-power critical order:
  k ~ log X / log log X

at that order:
  pointwise/combinatorial complexity becomes polynomial in X

current fixed-k theorems:
  not uniform enough to cross the critical order
```

Higher-order Selberg methods are genuine amplifiers, but the audited theory supplies a subpower amplifier rather than a certified fixed-power amplifier.

---

# 1. Generalized von Mangoldt functions

For an integer

$$
k\ge1,
$$

define

$$
\boxed{
\Lambda_k(n)
=
\sum_{d\mid n}
\mu(d)
\left(
\log\frac nd
\right)^k.
}
$$

Equivalently,

$$
\boxed{
\Lambda_k
=
\mu*\log^k.
}
$$

The Dirichlet series is

$$
\boxed{
\sum_{n\ge1}
\frac{\Lambda_k(n)}{n^s}
=
(-1)^k
\frac{\zeta^{(k)}(s)}{\zeta(s)},
\qquad
\Re s>1.
}
$$

Also,

$$
\boxed{
\Lambda_{k+1}
=
\Lambda_k\log
+
\Lambda*\Lambda_k.
}
$$

The function is nonnegative and supported on integers with at most $k$ distinct prime factors.

At a prime,

$$
\boxed{
\Lambda_k(p)
=
(\log p)^k.
}
$$

---

# 2. Fixed-k summatory polynomial

For each fixed

$$
k\ge1,
$$

there exists a polynomial $R_k$ of degree $k-1$ with leading term

$$
k t^{k-1}
$$

such that

## Theorem 2.1 — Fixed-Order Generalized Selberg Summatory Formula

$$
\boxed{
\sum_{n\le x}\Lambda_k(n)
=
xR_k(\log x)
+
O_k(x).
}
$$

Equivalently, retaining only the leading term,

$$
\boxed{
\sum_{n\le x}\Lambda_k(n)
=
kx(\log x)^{k-1}
+
O_k
\left(
x(\log x)^{k-2}
\right).
}
$$

For $k=2$, this contains the classical Selberg symmetry formula.

For $k\ge2$, the almost-prime observable is much smoother than the prime observable itself.

---

# 3. Complete polynomial subtraction

Define

$$
\boxed{
E_k(x)
=
\sum_{n\le x}\Lambda_k(n)
-
xR_k(\log x).
}
$$

Theorem 2.1 gives

$$
\boxed{
E_k(x)
=
O_k(x).
}
$$

Normalize by the natural leading scale:

$$
\widetilde E_k(x)
=
\frac{
E_k(x)
}{
x(\log x)^{k-1}
}.
$$

Then for fixed $k$,

$$
\boxed{
\widetilde E_k(x)
=
O_k
\left(
(\log x)^{-(k-1)}
\right).
}
$$

Thus increasing a fixed order can manufacture arbitrarily high fixed logarithmic precision.

It does not yet manufacture a power of $x$.

---

# 4. Fixed-zero response of Lambda-k

Let $\rho$ be a simple nontrivial zero of $\zeta$.

Near

$$
s=\rho,
$$

write

$$
\zeta(s)
=
\zeta'(\rho)(s-\rho)
+
O
\left(
(s-\rho)^2
\right).
$$

Then

$$
(-1)^k
\frac{\zeta^{(k)}(s)}{\zeta(s)}
$$

either:

1. has a simple pole at $\rho$, with residue
   $$
   \boxed{
   (-1)^k
   \frac{
   \zeta^{(k)}(\rho)
   }{
   \zeta'(\rho)
   },
   }
   $$
   if $\zeta^{(k)}(\rho)\ne0$ ;

or

2. has the pole cancelled because the numerator also vanishes there.

Therefore:

## Theorem 4.1 — Fixed-Order Zero-Exponent Invariance

Whenever the generalized detector sees the zero $\rho$, its explicit-formula contribution has exponent

$$
\boxed{
x^\rho.
}
$$

Changing fixed $k$ changes the coefficient, not the real exponent.

If the numerator cancels the pole, the detector becomes less sensitive to that particular zero rather than more coercive.

Create:

```text
O-RH-064
FIXED_ORDER_GENERALIZED_SELBERG_ZERO_EXPONENT_INVARIANCE
status:
  CERTIFIED AS STRENGTH AUDIT
```

---

# 5. Fixed-k forcing versus fixed Mellin mode

For a fixed zero or hypothetical Mellin drift with

$$
\Re\rho=\beta<1,
$$

the generalized detector has mode scale

$$
O_{k,\rho}(x^\beta)
$$

whenever the pole survives.

The unconditional complete-model remainder is

$$
O_k(x).
$$

Hence

$$
\boxed{
x^\beta
=
o(x).
}
$$

After normalization by $x(\log x)^{k-1}$:

## forcing

$$
\boxed{
O_k
\left(
(\log x)^{-(k-1)}
\right)
}
$$

## zero/drift mode

$$
\boxed{
O_{k,\rho}
\left(
x^{\beta-1}
(\log x)^{-(k-1)}
\right).
}
$$

Their ratio is

$$
\boxed{
x^{\beta-1}.
}
$$

It is independent of $k$ at exponent level.

Thus fixed-order amplification sharpens the logarithmic normalization while leaving the fixed Mellin mode buried inside the $O_k(x)$ forcing.

---

# 6. Finite fixed-order linear combinations

Let $K$ be fixed and consider

$$
\boxed{
\mathcal L_K(s)
=
\frac{
\sum_{k=1}^{K}
c_k(-1)^k\zeta^{(k)}(s)
}{
\zeta(s)
}.
}
$$

At a simple zero $\rho$, if

$$
\sum_{k=1}^{K}
c_k(-1)^k
\zeta^{(k)}(\rho)
\ne0,
$$

then $\mathcal L_K$ still has a simple pole at $\rho$.

Hence the associated zero contribution still has exponent $x^\rho$.

If the numerator vanishes, the filter misses that zero.

Therefore a fixed-order differential filter cannot move a surviving zero mode to a better exponent.

It can only alter or remove its residue.

---

# 7. Main-term cancellation does not cancel unknown remainders

For fixed $K$, known polynomial main terms

$$
xR_k(\log x)
$$

can be combined exactly.

But the current unconditional statements provide separate errors

$$
E_k(x)=O_k(x).
$$

A finite linear combination gives only

$$
\boxed{
\sum_{k\le K}c_kE_k(x)
=
O_K
\left(
x\sum_{k\le K}|c_k|
\right)
}
$$

without additional joint information.

One cannot use cancellation among independent big- $O$ errors as theorem authority.

Create:

```text
O-RH-065
FIXED_ORDER_REMAINDER_NONCOHERENCE
status:
  CERTIFIED AS CURRENT-THEOREM AUDIT
```

This does not say that the true remainders never cancel.

It says that current fixed-order summatory formulae do not certify such cancellation.

---

# 8. Historical calibration: higher weight really does amplify

Higher-weight Selberg/Bombieri/Wirsing methods are not useless.

Historically, elementary methods were strengthened from the original PNT to error terms of the form

$$
\boxed{
\psi(x)-x
=
O_A
\left(
x(\log x)^{-A}
\right)
}
$$

for every fixed $A>0$.

Later Diamond–Steinig-type methods obtained stretched-exponential subpower remainders of the form

$$
\boxed{
x
\exp
\left(
-c(\log x)^\theta
\right)
}
$$

for fixed $\theta>0$ in the known elementary range.

Thus higher weighting and recursion can increase cumulative amplification beyond every fixed logarithmic power.

But these estimates remain

$$
\boxed{
x^{1-o(1)},
}
$$

not $x^{1-\delta}$.

This is consistent with the CSM_RH subpower / fixed-power distinction.

---

# 9. Critical growing order

Suppose one tries to turn a formal logarithmic factor

$$
(\log X)^{-k}
$$

into a fixed power

$$
X^{-\delta}.
$$

The balance equation is

$$
k\log\log X
\sim
\delta\log X.
$$

Therefore the critical order is

## Theorem 9.1 — Fixed-Power Order Scale

$$
\boxed{
k_{\mathrm{crit}}
\asymp
\delta
\frac{
\log X
}{
\log\log X
}.
}
$$

Any order satisfying

$$
k
=
o
\left(
\frac{\log X}{\log\log X}
\right)
$$

can generate at most a subpower factor from powers of $\log X$.

---

# 10. Pointwise weight complexity at the critical order

At a prime,

$$
\Lambda_k(p)
=
(\log p)^k.
$$

At

$$
k
=
c
\frac{\log X}{\log\log X},
$$

we have

$$
\boxed{
(\log X)^k
=
X^{c+o(1)}.
}
$$

Thus the generalized detector itself acquires polynomial-size spikes exactly when the formal logarithmic amplifier enters fixed-power territory.

The pointwise bound

$$
0\le\Lambda_k(n)\le(\log n)^k
$$

therefore ceases to be exponent-neutral.

---

# 11. Factorial proof-complexity scale

The elementary fixed- $k$ summatory argument expands powers of logarithms and integrates expressions of the form

$$
\log^k y.
$$

The natural coefficient scale includes factorial-size quantities.

Stirling gives

$$
\boxed{
\log(k!)
=
k\log k-k+O(\log k).
}
$$

At the critical order

$$
k
=
c
\frac{\log X}{\log\log X},
$$

one gets

$$
\boxed{
k!
=
X^{c+o(1)}.
}
$$

Therefore any factorial-type dependence hidden inside the fixed- $k$ constant $O_k(1)$ becomes polynomial in $X$ at exactly the order required for fixed-power amplification.

The existing theorem

$$
E_k(x)=O_k(x)
$$

is stated for fixed $k$ and provides no uniform control capable of excluding this exponent cost.

Create:

```text
O-RH-066
GROWING_ORDER_FACTORIAL_COMPLEXITY_THRESHOLD
status:
  CERTIFIED AS CURRENT-METHOD UNIFORMITY BARRIER
```

The statement is not that every possible proof must lose $k!$.

It is that the current fixed- $k$ theorem contains no uniformity strong enough to cross the critical order, and factorial-scale dependence is already exponent-critical there.

---

# 12. Support complexity at large order

The generalized function $\Lambda_k$ is supported on integers with at most $k$ distinct prime factors.

For fixed $k$, this is a strong smoothing from primes to bounded-order almost primes.

At

$$
k
\asymp
\frac{\log X}{\log\log X},
$$

the allowed number of distinct prime factors is far larger than the typical order $\log\log X$.

Thus the support restriction becomes weak for typical integers.

This is a qualitative warning:

```text
small fixed k:
  strong almost-prime smoothing

critical growing k:
  broad support, large weights
```

The very mechanism that smooths the prime problem at fixed order becomes less selective when the order approaches fixed-power scale.

---

# 13. Growing-order verdict

There are three regimes.

## Regime I — fixed k

$$
k=O(1).
$$

Result:

```text
arbitrary fixed log powers possible;
fixed zero exponent unchanged;
fixed-power coercivity absent.
```

## Regime II — subcritical growing k

$$
k
=
o
\left(
\frac{\log X}{\log\log X}
\right).
$$

Formal log amplification remains

$$
X^{-o(1)}.
$$

This is compatible with stretched-exponential/subpower error improvements.

## Regime III — critical order

$$
k
\asymp
\frac{\log X}{\log\log X}.
$$

Formal amplification can become a fixed power.

But:

```text
pointwise weights:
  polynomial in X

factorial-type constants:
  polynomial in X

fixed-k summatory theorem:
  no authorized uniformity

almost-prime support:
  substantially less selective
```

No certified net fixed power is obtained.

---

# 14. Campaign 29 track audit

## H1 — fixed-k generalized Selberg response

```text
status:
  CLOSED

zero exponent:
  invariant

forcing:
  O_k(x)
```

## H2 — finite linear-combination forcing cancellation

```text
status:
  NO CERTIFIED CANCELLATION OF O_k(x) REMAINDERS

fixed-zero exponent:
  unchanged if pole survives
```

## H3 — growing-k amplification

```text
status:
  SUBCRITICAL -> SUBPOWER

critical order:
  complexity/uniformity barrier
```

## H4 — generalized almost-prime to PESC transfer

```text
status:
  NO LOWER-STRENGTH FIXED-POWER TRANSFER FOUND
```

## H5 — spectral polynomial in Selberg operator

```text
status:
  FIXED ORDER CHANGES RESIDUES, NOT ZERO EXPONENTS

no coercive filter found
```

---

# 15. Campaign 29 verdict

No fixed-power theorem is proved.

The higher-order Selberg route is classified as:

```text
real amplifier:
  YES

arbitrary fixed log-power:
  YES

subpower / stretched-log potential:
  YES

certified fixed-power:
  NO

fixed-order route:
  CLOSED AS EXPONENT-NEUTRAL

growing-order route:
  OPEN IN PRINCIPLE BUT CURRENTLY UNAUTHORIZED AT CRITICAL ORDER
```

The root target remains PESC.

---

# 16. New certified obstruction package

Create:

```text
O-RH-064
FIXED_ORDER_GENERALIZED_SELBERG_ZERO_EXPONENT_INVARIANCE
CERTIFIED

O-RH-065
FIXED_ORDER_REMAINDER_NONCOHERENCE
CERTIFIED AS CURRENT-THEOREM AUDIT

O-RH-066
GROWING_ORDER_FACTORIAL_COMPLEXITY_THRESHOLD
CERTIFIED AS CURRENT-METHOD UNIFORMITY BARRIER
```

No new frontier is created.

---

# 17. Return to the arithmetic root

The generalized Selberg shell has now been audited at:

```text
order 2;
fixed higher order;
finite fixed-order combinations;
subcritical growing order;
critical growing-order exponent budget.
```

No lower-strength fixed-power bridge is found.

Therefore CSM_RH returns again to:

```text
F-RH-010
PESC
```

with no additional surrogate.

---

# 18. Campaign 30

The next campaign is:

```text
CSM_RH Campaign 30
PARITY_SENSITIVE_PESC_ATTACK
```

The goal is not to introduce another almost-prime smoothing layer.

It is to identify arithmetic information that distinguishes the true prime residual from the family of generalized almost-prime models.

---

# 19. Campaign 30 tracks

## Q1 — PESC parity decomposition

Decompose the residual prime detector according to Liouville/Möbius parity information while preserving the signed endogenous primitive.

The target must remain bilinear.

## Q2 — asymptotic-sieve scalar defect

Use the Bombieri asymptotic-sieve perspective: higher generalized von Mangoldt information leaves a parity-sensitive scalar undetermined.

Identify the analogue of that undetermined scalar inside PESC.

## Q3 — parity-breaking bilinear input

Revisit Friedlander–Iwaniec-type parity-breaking hypotheses, but require a direct bilinear bridge to PESC rather than EMBF/PACPSA surrogate proliferation.

## Q4 — prime-versus-almost-prime drift comparator

Construct an observable whose value on $\Lambda$ differs at fixed exponent from every bounded-order generalized almost-prime model.

## Q5 — direct residual sign structure

Search for a prime-specific signed identity involving $f=\Lambda-\Lambda^\sharp$ that is not shared by $\Lambda_k$ for $k\ge2$.

---

# 20. Campaign 30 rejection filters

Reject a candidate if:

## R1. It only introduces another $\Lambda_k$ or almost-prime average.

## R2. It reproduces EMBF/EMDQO without a direct PESC bridge.

## R3. It uses parity-breaking as a slogan without an exponent ledger.

## R4. It obtains only logarithmic/subpower precision.

## R5. It assumes a fixed zero strip.

## R6. It creates another positive higher-moment target.

---

# 21. External calibration

Current/classical calibration:

1. For fixed $k$,
   $$
   \sum_{n\le x}\Lambda_k(n)
   =
   xR_k(\log x)+O_k(x),
   $$
   with $R_k$ of degree $k-1$ and leading term $k(\log x)^{k-1}$.

2. The generalized von Mangoldt functions satisfy
   $$
   \Lambda_{k+1}
   =
   \Lambda_k\log
   +
   \Lambda*\Lambda_k.
   $$

3. Higher-weight elementary methods historically improve the PNT remainder through arbitrary logarithmic powers and stretched-exponential subpower scales.

4. Bombieri's asymptotic-sieve perspective shows that very rich higher-almost-prime information can still leave the prime/parity component undetermined.

These facts motivate the next parity-sensitive return to PESC.

---

# 22. State transition

```text
CSM_RH v1.20
  ->
CSM_RH v1.21
```

with:

```text
Campaign 29
  CLOSED_AS_HIGHER_ORDER_SELBERG_AMPLIFIER_AUDIT

O-RH-064
  CREATED / CERTIFIED

O-RH-065
  CREATED / CERTIFIED AS CURRENT-THEOREM AUDIT

O-RH-066
  CREATED / CERTIFIED AS CURRENT-METHOD UNIFORMITY BARRIER

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 30
  PARITY_SENSITIVE_PESC_ATTACK
  READY
```

---

# 23. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

FIXED-ORDER HIGHER SELBERG = EXPONENT-NEUTRAL

FINITE FIXED-ORDER FILTER = NO CERTIFIED REMAINDER CANCELLATION

SUBCRITICAL GROWING ORDER = SUBPOWER

FIXED-POWER CRITICAL ORDER = log X / log log X

CURRENT UNIFORMITY AT CRITICAL ORDER = INSUFFICIENT

HIGHER SELBERG = REAL SUBPOWER AMPLIFIER, NOT CERTIFIED FIXED-POWER AMPLIFIER

NEXT CAMPAIGN = 30
```

The central scale law is

$$
\boxed{
(\log X)^{-k}
=
X^{-\delta}
\quad\Longleftrightarrow\quad
k
\sim
\delta
\frac{\log X}{\log\log X}.
}
$$

At precisely this order,

$$
\boxed{
(\log X)^k
=
X^{\delta+o(1)}
}
$$

and factorial-type $k$ -dependence also enters polynomial exponent scale.

The current fixed- $k$ generalized Selberg theory does not provide a certified net fixed power across this threshold.
