# CSM_RH Paper 87

## One-Sided Polynomial Prime Tails: Growing-Order Resolution for Excess and the Additional Parity Barrier for Deficiency

**Project:** CSM_RH  
**Paper:** 87  
**Version:** v0.1  
**Date:** 2026-09-09  
**Canonical root frontier:** F-RH-017-v3  
**Entry state:** v1.77 / Paper 86 v0.1  
**Status:** ONE-SIDED EXCEPTIONAL SET DECOMPOSED / UPPER TAIL SHOWN TO REQUIRE POLYNOMIALLY GROWING NEAR-POISSON RESOLUTION / LOWER TAIL CARRIES THE SAME RESOLUTION COST PLUS THE SIEVE PARITY BARRIER  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 86 proved that every fixed even-moment / Markov argument undergoes a phase transition exactly at the threshold exponent

$$
\nu=d,
\qquad
d=\frac{\kappa}{2}.
$$

Since F-RH-017-v3 requires

$$
\nu>d,
$$

the root problem is threshold-native.

The present paper splits the exceptional set into its two one-sided components:

$$
\boxed{
\mathcal E_\nu^+
=
\left\{
x:
\Delta_H(x)>HX^{-\nu}
\right\},
}
$$

and

$$
\boxed{
\mathcal E_\nu^-
=
\left\{
x:
\Delta_H(x)<-HX^{-\nu}
\right\}.
}
$$

The two tails have different arithmetic obstructions.

Let

$$
H=X^{1-\tau},
$$

and let

$$
N_H(x)
=
\pi(x+H)-\pi(x).
$$

The natural prime-count mean is

$$
\boxed{
\lambda
=
\frac{H}{\log X}.
}
$$

For

$$
\nu<
\min
\left(
\frac12,
1-\tau
\right),
$$

prime powers and the variation of $\log p$ across the interval are smaller than the target

$$
HX^{-\nu}.
$$

Thus, at fixed-power resolution,

$$
\Delta_H(x)>HX^{-\nu}
$$

corresponds to

$$
\boxed{
N_H(x)
>
(1+\delta+o(\delta))\lambda,
}
$$

where

$$
\boxed{
\delta=X^{-\nu}.
}
$$

Likewise the deficiency tail corresponds to

$$
N_H(x)
<
(1-\delta+o(\delta))\lambda.
$$

The first main theorem concerns the **best possible factorial-moment upper-tail method**.

Suppose that for some order $r$ one has the near-Poisson falling-factorial estimate

$$
\boxed{
\mathbb E_X
(N_H)_r
\le
\lambda^r
e^{\varepsilon_r r},
}
$$

where

$$
(N)_r
=
N(N-1)\cdots(N-r+1).
$$

If

$$
r\le\frac{\delta\lambda}{2},
$$

then on the event

$$
N_H\ge(1+\delta)\lambda
$$

one has

$$
(N_H)_r
\ge
\left(
(1+\delta)\lambda-r
\right)^r.
$$

Hence:

## Factorial upper-tail transfer

$$
\boxed{
\Pr_X
\left(
N_H\ge(1+\delta)\lambda
\right)
\le
\exp
\left[
\varepsilon_r r
-
c_0\delta r
\right]
}
$$

for an absolute constant $c_0>0$.

Therefore, even in an ideal factorial-moment framework, a polynomial exceptional saving

$$
\boxed{
\Pr_X
\left(
N_H\ge(1+\delta)\lambda
\right)
\ll
X^{-c}
}
$$

requires both:

$$
\boxed{
r
\gg
\delta^{-1}\log X
=
X^\nu\log X,
}
$$

and

$$
\boxed{
\varepsilon_r
\ll
\delta
=
X^{-\nu}.
}
$$

This is the **upper-tail resolution complexity law**.

It is stronger than the fixed-moment obstruction of Paper 86.

Not only must the moment order grow with $X$ ; it must grow polynomially.

Moreover the tuple/moment theorem must be nearly asymptotically exact at relative precision $X^{-\nu}$ per copy.

The order condition is compatible with the Poisson large-deviation range exactly when

$$
\boxed{
r
\ll
\delta\lambda.
}
$$

For

$$
r\asymp
\delta^{-1}\log X,
$$

this is

$$
\boxed{
2\nu<1-\tau.
}
$$

Thus there is an admissible threshold window

$$
\boxed{
d<\nu<\frac{1-\tau}{2}
}
$$

if and only if

$$
\boxed{
\kappa<1-\tau.
}
$$

This is exactly the scale gate already present in the F-RH amplification problem.

In the ideal Poisson model, the tail exponent is much stronger:

$$
\boxed{
\Pr
\left(
|N_H-\lambda|>\delta\lambda
\right)
\approx
\exp
\left[
-c\delta^2\lambda
\right],
}
$$

and

$$
\boxed{
\delta^2\lambda
=
\frac{
X^{1-\tau-2\nu}
}{
\log X
}.
}
$$

Hence in the above window the conjectural one-sided exceptional sets are smaller than every fixed power of $X$.

The obstacle is therefore not probabilistic margin.

It is arithmetic resolution.

Current sieve/factorial-moment technology is far below the required order.

Kuperberg proves an unconditional Selberg-sieve moment bound for prime counts in intervals

$$
h=\lambda\log X=o(X)
$$

for

$$
\boxed{
r=o((\log X)^{1/4}),
}
$$

of the shape

$$
\boxed{
m_r(X,h)
\ll
(\lambda+1)^r
r^{2r}
e^{O(r\log\log r)}.
}
$$

The range is subpolynomial in $X$, whereas F-RH resolution requires

$$
r\asymp X^\nu\log X.
$$

The multiplicative sieve overhead is also much larger than the allowed per-copy precision

$$
1+O(X^{-\nu}).
$$

Thus the existing unconditional upper-tail sieve does not resolve the tiny relative excess in F-RH-017-v3.

Gallagher's classical Selberg-sieve argument gives unconditional exponential upper tails for prime counts in logarithmic intervals.

Kuperberg extends the analysis to growing moments and large tails.

These are genuine upper-tail tools, but they operate at coarse or extreme deviations.

They do not yield near-mean concentration at relative resolution $X^{-\nu}$.

The 2026 work of Jha proves conditional Poisson-tail asymptotics for slowly growing

$$
\lambda
$$

under a strong Hardy–Littlewood hypothesis and studies a phase transition as $\lambda$ grows slower than every fixed power of $\log X$.

The polynomial interval regime here has

$$
\lambda
=
\frac{X^{1-\tau}}{\log X},
$$

well outside that slowly-growing setting.

Therefore the prime-excess tail is not solved by current near-Poisson theory either.

The deficiency tail is strictly more obstructed.

An upper factorial-moment or upper-bound-sieve theorem controls large values of $N_H$.

It gives no lower bound for $N_H$.

To prove

$$
N_H
\ge
(1-\delta)\lambda
$$

outside a power-small exceptional set requires a lower-tail mechanism.

A local-divisibility sieve alone cannot provide such a prime lower bound because of the classical parity phenomenon.

The Selberg parity model used in Papers 64 and 75 can satisfy strong local sieve distribution while containing no primes in the relevant parity class.

Thus:

```text
UPPER TAIL:
resolution-hard, but not intrinsically parity-hard.

LOWER TAIL:
resolution-hard + parity-hard.
```

Matomäki's theorem on $P_2$ numbers in almost all very short intervals provides a useful contrast.

Weighted lower/upper sieve arguments combined with Kloosterman-sum information can prove strong almost-all lower bounds for products of at most two primes.

The same framework does not automatically produce primes, precisely because the prime lower-bound problem sits beyond the corresponding sieve parity barrier.

The present paper therefore does **not** conclude that only the deficiency tail is root-hard.

The excess tail remains unresolved at the required polynomial precision.

Instead it separates two auxiliary frontiers.

Open:

```text
F-RH-027+
POLYNOMIAL PRIME-EXCESS RESOLUTION
```

Target:

$$
\boxed{
|\mathcal E_\nu^+|
\ll
X^{1-c_++o(1)}
}
$$

for some

$$
\nu>d,
\qquad
c_+>\min(d,\tau).
$$

The required mechanism must achieve polynomially growing effective complexity and near-Poisson precision without assuming the desired prime-tuple asymptotics.

Open:

```text
F-RH-027-
POLYNOMIAL PRIME-DEFICIENCY PARITY TAIL
```

Target:

$$
\boxed{
|\mathcal E_\nu^-|
\ll
X^{1-c_-+o(1)}
}
$$

for some

$$
\nu>d,
\qquad
c_->\min(d,\tau).
$$

This requires, in addition, a parity-breaking lower-tail input.

The absolute frontier F-RH-017-v3 follows if both one-sided estimates hold, with

$$
c
=
\min(c_+,c_-).
$$

No RH theorem is claimed.

---

# 1. One-sided exceptional sets

Recall

$$
\Delta_H(x)
=
\psi(x+H)-\psi(x)-H.
$$

Define

$$
\boxed{
\mathcal E_\nu^+
=
\{
x\in[X,2X]:
\Delta_H(x)>HX^{-\nu}
\},
}
$$

and

$$
\boxed{
\mathcal E_\nu^-
=
\{
x\in[X,2X]:
\Delta_H(x)<-HX^{-\nu}
\}.
}
$$

Then

$$
\boxed{
\mathcal E_\nu
=
\mathcal E_\nu^+
\cup
\mathcal E_\nu^-.
}
$$

Therefore separate bounds

$$
|\mathcal E_\nu^\pm|
\ll
X^{1-c_\pm+o(1)}
$$

give

$$
|\mathcal E_\nu|
\ll
X^{1-\min(c_+,c_-)+o(1)}.
$$

---

# 2. Translation to unweighted prime counts

For

$$
x\asymp X,
$$

and primes

$$
p\in(x,x+H],
$$

$$
\log p
=
\log X
+
O(1).
$$

Prime powers with exponent at least $2$ contribute

$$
O
\left(
H X^{-1/2}
(\log X)^{O(1)}
+
(\log X)^{O(1)}
\right).
$$

Thus if

$$
\nu<
\min
\left(
\frac12,
1-\tau
\right),
$$

this error is

$$
o
\left(
HX^{-\nu}
\right).
$$

Hence the weighted tail and the unweighted prime-count tail have the same fixed-power threshold.

---

# 3. Falling factorial moments

Let $x$ be uniform in the discrete interval

$$
[X,2X]\cap\mathbb Z.
$$

Define

$$
N=N_H(x).
$$

For integer $r\ge1$ let

$$
(N)_r
=
N(N-1)\cdots(N-r+1).
$$

Assume

$$
\boxed{
\mathbb E_X(N)_r
\le
\lambda^r
e^{\varepsilon_r r}.
}
$$

This notation separates:

- the Poisson main $\lambda^r$ ;
- the logarithmic per-copy loss $\varepsilon_r$.

---

# 4. Upper-tail factorial transfer

Let

$$
K=(1+\delta)\lambda.
$$

If

$$
N\ge K
$$

and

$$
r\le\frac{\delta\lambda}{2},
$$

then

$$
\begin{aligned}
(N)_r
&\ge
(K-r)^r
\\
&\ge
\lambda^r
\left(
1+\frac{\delta}{2}
\right)^r.
\end{aligned}
$$

Therefore:

## Theorem 4.1 — Near-Poisson factorial upper-tail transfer

$$
\boxed{
\Pr_X(N\ge(1+\delta)\lambda)
\le
\exp
\left[
\varepsilon_r r
-
r\log
\left(
1+\frac{\delta}{2}
\right)
\right].
}
$$

For $0<\delta\le1$,

$$
\log
\left(
1+\frac{\delta}{2}
\right)
\ge
\frac{\delta}{3}.
$$

Hence

$$
\boxed{
\Pr_X(N\ge(1+\delta)\lambda)
\le
\exp
\left[
-\left(
\frac{\delta}{3}
-
\varepsilon_r
\right)r
\right].
}
$$

Create:

```text
B-RH-166
NEAR_POISSON_FACTORIAL_MOMENTS_TRANSFER_TO_A_TINY_RELATIVE_PRIME_EXCESS_TAIL_WITH_EXPONENT_DELTA_TIMES_R
CERTIFIED
```

---

# 5. Required order for a polynomial exceptional saving

Suppose

$$
\varepsilon_r
\le
\frac{\delta}{6}.
$$

Then

$$
\Pr_X(N\ge(1+\delta)\lambda)
\le
e^{-\delta r/6}.
$$

To obtain

$$
\boxed{
\Pr_X(N\ge(1+\delta)\lambda)
\le
X^{-c},
}
$$

it suffices, and within this transfer is necessary up to constants, to take

$$
\boxed{
r
\ge
6c
\frac{\log X}{\delta}.
}
$$

For

$$
\delta=X^{-\nu},
$$

## Theorem 5.1 — Polynomial resolution order

$$
\boxed{
r_{\rm res}
\asymp
X^\nu\log X.
}
$$

Create:

```text
B-RH-167
A_POWER_SAVING_EXCEPTIONAL_BOUND_AT_RELATIVE_RESOLUTION_X_MINUS_NU_REQUIRES_FACTORIAL_MOMENT_ORDER_OF_POLYNOMIAL_SIZE_X_TO_NU_UP_TO_LOGS
CERTIFIED_WITHIN_FACTORIAL_TRANSFER
```

---

# 6. Per-copy precision requirement

The same theorem requires

$$
\varepsilon_r
<
c_0\delta.
$$

Thus the factorial moment theorem must have multiplicative error

$$
\boxed{
e^{o(\delta r)}
}
$$

across $r$ copies.

Equivalently, its logarithmic loss **per copy** must satisfy

$$
\boxed{
\varepsilon_r
=
O(X^{-\nu}).
}
$$

Any uniform sieve overhead

$$
C^r,
\qquad
C>1,
$$

has

$$
\varepsilon_r=\log C,
$$

which is eventually much larger than

$$
X^{-\nu}.
$$

Therefore:

## Corollary 6.1 — Constant-factor sieve barrier

A fixed per-copy multiplicative sieve gap cannot resolve a relative excess which tends to zero polynomially.

Create:

```text
O-RH-189
ANY_FIXED_PER_COPY_UPPER_SIEVE_CONSTANT_GAP_IS_FATAL_FOR_THE_ONE_PLUS_X_MINUS_NU_PRIME_EXCESS_TAIL
CERTIFIED
```

---

# 7. Compatibility with the Poisson deviation window

The factorial argument needs

$$
r_{\rm res}
\ll
\delta\lambda.
$$

Now

$$
r_{\rm res}
\asymp
X^\nu\log X,
$$

while

$$
\delta\lambda
=
\frac{
X^{1-\tau-\nu}
}{
\log X
}.
$$

Thus

$$
r_{\rm res}
\ll
\delta\lambda
$$

if and only if

$$
\boxed{
2\nu<1-\tau
}
$$

at fixed-power resolution.

Therefore there exists $\nu$ satisfying both

$$
d<\nu
$$

and

$$
2\nu<1-\tau
$$

if and only if

$$
\boxed{
2d=\kappa<1-\tau.
}
$$

Create:

```text
B-RH-168
THE_GROWING_ORDER_UPPER_TAIL_RESOLUTION_WINDOW_EXISTS_EXACTLY_UNDER_THE_SAME_KAPPA_LESS_THAN_ONE_MINUS_TAU_SCALE_GATE_AS_THE_ROOT_AMPLIFIER
CERTIFIED
```

---

# 8. Ideal Poisson margin

For a Poisson variable of mean $\lambda$ and $0<\delta<1$,

$$
\Pr
\left(
|N-\lambda|\ge\delta\lambda
\right)
\le
2
\exp
\left(
-c\delta^2\lambda
\right).
$$

Here

$$
\boxed{
\delta^2\lambda
=
\frac{
X^{1-\tau-2\nu}
}{
\log X
}.
}
$$

If

$$
2\nu<1-\tau,
$$

this tends to infinity polynomially in $X$.

Hence the model predicts an exceptional set much smaller than

$$
X^{1-c}
$$

for every fixed $c$.

There is large conjectural margin.

---

# 9. Kuperberg's unconditional large-moment calibration

Kuperberg proves for

$$
h=\lambda\log X=o(X)
$$

and

$$
r=o((\log X)^{1/4})
$$

an unconditional Selberg-sieve moment bound

$$
\boxed{
m_r(X,h)
\ll
(\lambda+1)^r
r^{2r}
e^{O(r\log\log r)}.
}
$$

This theorem is valuable for extreme prime-count tails.

For the current problem, however:

$$
r_{\rm available}
=
X^{o(1)},
$$

while

$$
r_{\rm required}
=
X^\nu\log X.
$$

Furthermore the factor

$$
r^{2r}
e^{O(r\log\log r)}
$$

is far larger than the required near-Poisson per-copy precision.

Create:

```text
O-RH-190
CURRENT_UNCONDITIONAL_SELBerg_SIEVE_LARGE_MOMENTS_ARE_BOTH_TOO_LOW_ORDER_AND_TOO_COARSE_PER_COPY_FOR_POLYNOMIAL_RELATIVE_PRIME_EXCESS
CERTIFIED_EXTERNAL_SCOPE_BARRIER
```

---

# 10. Gallagher and Jha calibration

Gallagher used a sieve upper bound for prime tuples to obtain unconditional exponential upper bounds for the tail of prime counts in intervals of logarithmic length.

This proves that prime-excess tails are amenable to upper-sieve methods at coarse deviations.

Kuperberg extends this to growing moments and large sets.

Jha's 2026 work obtains Poisson-tail asymptotics under a strong Hardy–Littlewood hypothesis when the Poisson mean $\lambda$ grows slowly and studies a phase transition for $\lambda$ below every fixed power of $\log X$.

The F-RH polynomial interval has

$$
\lambda
=
X^{1-\tau}/\log X.
$$

Thus it lies far beyond that regime.

---

# 11. Upper-tail conclusion

The prime-excess tail is **not** classified as a parity problem.

Its present obstruction is:

```text
POLYNOMIAL RESOLUTION COMPLEXITY
+
NEAR-EXACT PRIME-TUPLE PRECISION.
```

A successful theorem could conceivably use:

- growing-order factorial moments;
- extremal interval sieve plus concentration;
- a threshold-native counting argument not reducible to fixed moments.

But current results do not achieve the required resolution.

Open:

```text
F-RH-027+
POLYNOMIAL_PRIME_EXCESS_RESOLUTION
```

---

# 12. Why upper factorial moments do not control deficiency

The quantity

$$
(N)_r
$$

is increasing in $N$.

Upper bounds for

$$
\mathbb E(N)_r
$$

therefore penalize unusually **large** prime counts.

They do not imply lower bounds for $N$.

In particular, the transfer in Section 4 has no lower-tail analogue using only upper factorial moments.

To control

$$
N\le(1-\delta)\lambda
$$

one needs additional information such as:

- lower factorial asymptotics;
- a negative exponential moment;
- inclusion-exclusion with sufficiently accurate alternating terms;
- a direct lower-bound sieve / prime-detection theorem.

---

# 13. Parity obstruction for the deficiency tail

A pure local-divisibility sieve cannot guarantee prime mass.

The classical parity phenomenon permits sequences with excellent local sieve distribution but the wrong multiplicative parity and no primes in the target class.

In the notation used earlier in the campaign, Selberg's parity sequence

$$
a_n
=
\frac12
(1+\lambda(n))
$$

is the canonical calibration.

It can satisfy strong local remainder information while evading prime detection.

Therefore a lower-tail theorem of the form

$$
\boxed{
N_H(x)
\ge
(1-\delta)\lambda
}
$$

for almost all $x$ cannot follow from local sieve distribution alone.

Create:

```text
O-RH-191
THE_POLYNOMIAL_PRIME_DEFICIENCY_TAIL_REQUIRES_PARITY_BREAKING_INFORMATION_IN_ADDITION_TO_THRESHOLD_RESOLUTION
CERTIFIED_AS_SIEVE_SCOPE_BARRIER
```

---

# 14. Almost-prime contrast

Matomäki proves that almost all intervals

$$
(x-h\log X,x]
$$

contain a product of at most two primes as soon as

$$
h\to\infty.
$$

Her proof uses Richert's weighted sieve, lower and upper sieve estimates, and Kloosterman-sum input.

This demonstrates that strong almost-all **lower-tail** statements are possible for almost primes.

But the passage from $P_2$ to primes reintroduces the parity problem.

Thus the theorem is a clean control experiment:

```text
DEFICIENCY LOWER TAIL:
arithmetic tools exist for almost primes;
prime detection remains the additional hard step.
```

---

# 15. One-sided frontiers

Open two auxiliary frontiers.

## F-RH-027+

Find

$$
\nu>d
$$

and

$$
c_+>\min(d,\tau)
$$

such that

$$
\boxed{
|\mathcal E_\nu^+|
\ll
X^{1-c_++o(1)}.
}
$$

## F-RH-027-

Find

$$
\nu>d
$$

and

$$
c_->\min(d,\tau)
$$

such that

$$
\boxed{
|\mathcal E_\nu^-|
\ll
X^{1-c_-+o(1)}.
}
$$

If both hold, then F-RH-017-v3 holds with

$$
\boxed{
c
=
\min(c_+,c_-).
}
$$

Neither one-sided theorem is certified here.

---

# 16. Relative difficulty classification

The current campaign evidence supports:

$$
\boxed{
\text{upper tail}
=
\text{resolution-hard};
}
$$

$$
\boxed{
\text{lower tail}
=
\text{resolution-hard}
+
\text{parity-hard}.
}
$$

This does not prove that the lower tail is mathematically harder in every possible method.

It classifies the barriers visible to current sieve / moment technology.

---

# 17. Relation to Paper 86

Paper 86 showed that fixed moment order fails once

$$
\nu>d.
$$

Paper 87 sharpens this for the upper tail.

Even if moments become almost perfectly Poissonian, the order must grow to

$$
\boxed{
X^\nu\log X.
}
$$

Thus moving from fixed to slowly-growing polylogarithmic order is not enough.

The required complexity class changes from:

```text
fixed / polylog
```

to:

```text
polynomial in X.
```

This explains why modern fixed- $k$ Hardy–Littlewood, zero additive-energy, and sieve moment theorems do not automatically approach F-RH-017-v3.

---

# 18. State transition

Advance candidate state

$$
v1.77
\to
v1.78.
$$

Add:

```text
B-RH-166
NEAR_POISSON_FACTORIAL_MOMENTS_TRANSFER_TO_A_TINY_RELATIVE_PRIME_EXCESS_TAIL_WITH_EXPONENT_DELTA_TIMES_R

B-RH-167
A_POWER_SAVING_EXCEPTIONAL_BOUND_AT_RELATIVE_RESOLUTION_X_MINUS_NU_REQUIRES_FACTORIAL_MOMENT_ORDER_OF_POLYNOMIAL_SIZE_X_TO_NU_UP_TO_LOGS

B-RH-168
THE_GROWING_ORDER_UPPER_TAIL_RESOLUTION_WINDOW_EXISTS_EXACTLY_UNDER_THE_SAME_KAPPA_LESS_THAN_ONE_MINUS_TAU_SCALE_GATE_AS_THE_ROOT_AMPLIFIER

O-RH-189
ANY_FIXED_PER_COPY_UPPER_SIEVE_CONSTANT_GAP_IS_FATAL_FOR_THE_ONE_PLUS_X_MINUS_NU_PRIME_EXCESS_TAIL

O-RH-190
CURRENT_UNCONDITIONAL_SELBerg_SIEVE_LARGE_MOMENTS_ARE_BOTH_TOO_LOW_ORDER_AND_TOO_COARSE_PER_COPY_FOR_POLYNOMIAL_RELATIVE_PRIME_EXCESS

O-RH-191
THE_POLYNOMIAL_PRIME_DEFICIENCY_TAIL_REQUIRES_PARITY_BREAKING_INFORMATION_IN_ADDITION_TO_THRESHOLD_RESOLUTION
```

Open:

```text
F-RH-027+
POLYNOMIAL_PRIME_EXCESS_RESOLUTION

F-RH-027-
POLYNOMIAL_PRIME_DEFICIENCY_PARITY_TAIL
```

Canonical root remains:

```text
F-RH-017-v3
```

No RH certificate is created.

---

# 19. Recommended next action

The next round should attack F-RH-027+ first because it has one fewer known obstruction.

The exact question is:

```text
Can one replace polynomially high factorial moments
by a threshold-native extremal-interval sieve
whose complexity grows only with the number
of actually exceptional intervals rather than X^nu?
```

A promising angle is to combine:

- the inertia property of exceptional intervals;
- a maximal separated subfamily of excess intervals;
- a sieve bound for the union of their prime-rich translates;
- a concentration / entropy argument.

This would be genuinely different from global $r$ th moments.

If that also requires $X^\nu$ independent constraints, then the upper-tail frontier itself has a growing-complexity wall.

After that, the lower-tail parity frontier can be isolated cleanly.

---

# 20. Conclusion

The one-sided split reveals two distinct barriers.

The prime-excess tail is not blocked by parity, but polynomial relative resolution forces polynomially growing statistical complexity and nearly exact tuple information.

The prime-deficiency tail inherits the same resolution problem and adds the classical lower-sieve parity obstruction.

The Poisson model predicts enormous room on both sides whenever

$$
d<\nu<\frac{1-\tau}{2},
$$

and this window exists precisely under the root amplifier gate

$$
\kappa<1-\tau.
$$

The remaining difficulty is therefore arithmetic, not probabilistic.
