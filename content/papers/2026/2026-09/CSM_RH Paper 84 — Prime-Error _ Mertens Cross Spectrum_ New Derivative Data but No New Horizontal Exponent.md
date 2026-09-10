# CSM_RH Paper 84

## Prime-Error / Mertens Cross Spectrum: New Derivative Data but No New Horizontal Exponent

**Project:** CSM_RH  
**Paper:** 84  
**Version:** v0.1  
**Date:** 2026-09-09  
**Branch:** `MIXED_ARITHMETIC_STATE_SCREENING`  
**Entry state:** v1.74 / Paper 83 v0.1  
**Status:** PRIME/MERTENS MIXED STATE SCREENED / SAME-ZERO CROSS SPECTRUM CONTAINS ZETA-DERIVATIVE DATA / HORIZONTAL EXPONENT REMAINS PESC-EQUIVALENT / NATURAL MELLIN COUPLING IS A MERTENS-ENERGY GRADIENT  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 83 showed that periodic / finite-sieve factor states do not create a new principal zeta direction.

The first surviving mixed-state candidate was the joint spectrum of:

- the prime-number-theorem error;
- the Mertens / Möbius summatory state.

This candidate genuinely contains information absent from the prime-error two-point spectrum.

For exponential smoothing define

$$
\boxed{
P(X)
=
\sum_{n\ge1}
\Lambda(n)e^{-n/X}
-
X
}
$$

and

$$
\boxed{
M_\mu(X)
=
\sum_{n\ge1}
\mu(n)e^{-n/X}.
}
$$

Mellin inversion gives

$$
\boxed{
P(X)
=
\frac1{2\pi i}
\int_{(c)}
\Gamma(s)X^s
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
ds
-
X
}
$$

and

$$
\boxed{
M_\mu(X)
=
\frac1{2\pi i}
\int_{(c)}
\Gamma(s)X^s
\frac1{\zeta(s)}
ds.
}
$$

Let

$$
\rho=\beta+i\gamma
$$

be a simple nontrivial zeta zero.

Its prime-error coefficient is

$$
\boxed{
A_\rho
=
-\Gamma(\rho),
}
$$

so that

$$
P(X)
\supset
-\Gamma(\rho)X^\rho.
$$

Its Mertens coefficient is

$$
\boxed{
B_\rho
=
\frac{\Gamma(\rho)}{\zeta'(\rho)},
}
$$

so that

$$
M_\mu(X)
\supset
\frac{\Gamma(\rho)}{\zeta'(\rho)}
X^\rho.
$$

Thus the same-zero mixed spectral coefficient is

$$
\boxed{
A_\rho\overline{B_\rho}
=
-
\frac{
|\Gamma(\rho)|^2
}{
\overline{\zeta'(\rho)}
}.
}
$$

This depends on

$$
\zeta'(\rho),
$$

which is not determined by the prime-error two-point spectrum.

Therefore the prime/Mertens pair passes the **spectral novelty** test of Paper 82.

However, it fails the stronger **horizontal exponent novelty** test.

Both components scale as

$$
X^\beta.
$$

Hence every degree-two same-zero mixed amplitude scales as

$$
\boxed{
X^{2\beta}.
}
$$

After normalization by the two natural first-order scales $X^2$, its fixed-power saving exponent is

$$
\boxed{
2(1-\beta).
}
$$

Consequently the rightmost-zero mixed cross exponent is

$$
\boxed{
s_{PM}^*
=
2(1-\beta_*).
}
$$

By Papers 48–55,

$$
\boxed{
s_{PM}^*
=
\kappa_*.
}
$$

Squaring a positive cross amplitude into an energy changes the exponent to

$$
4(1-\beta_*),
$$

but the PESC conversion divides by the copy degree and returns the same

$$
2(1-\beta_*).
$$

Thus the derivative information changes spectral weights but not horizontal power geometry.

This conclusion does not require a uniform bound on

$$
|\zeta'(\rho)|.
$$

For a fixed hypothetical simple boundary zero,

$$
1/\zeta'(\rho)
$$

is a fixed nonzero constant.

Any strict power improvement eventually dominates such a constant.

If the rightmost zero has multiplicity

$$
m\ge2,
$$

then

$$
1/\zeta(s)
$$

has a pole of order $m$.

The corresponding Mertens contribution has the form

$$
\boxed{
\frac{
m\Gamma(\rho)
}{
\zeta^{(m)}(\rho)
}
X^\rho
(\log X)^{m-1}
+
O_\rho
\left(
X^\rho
(\log X)^{m-2}
\right).
}
$$

Thus multiplicity strengthens the logarithmic forcing without changing the fixed-power exponent.

The mixed state therefore contains vertical / local-zero information:

- zero simplicity;
- values of $\zeta'(\rho)$ ;
- negative derivative moments;
- spacing-sensitive data.

But this does not move the rightmost zero horizontally by itself.

The paper next identifies two exact collapse mechanisms.

First, the linear multiplicative coupling is not new.

Since

$$
\boxed{
\left(
-\frac{\zeta'}{\zeta}
\right)
\frac1\zeta
=
-\frac{\zeta'}{\zeta^2}
=
\left(
\frac1\zeta
\right)',
}
$$

one has coefficientwise

$$
\boxed{
(\Lambda*\mu)(n)
=
-\mu(n)\log n.
}
$$

Thus Dirichlet convolution of the prime and Möbius states is merely a logarithmically weighted Mertens state.

Second, the natural Mellin same-line coupling is the gradient of Mertens spectral energy.

Let

$$
\boxed{
F(s)=\frac1{\zeta(s)}.
}
$$

Then

$$
\boxed{
-\frac{\zeta'}{\zeta}(s)
=
\frac{F'(s)}{F(s)}.
}
$$

Therefore

$$
\boxed{
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
|F(s)|^2
=
F'(s)\overline{F(s)}.
}
$$

For

$$
s=\sigma+it,
$$

taking real and imaginary parts gives

$$
\boxed{
\Re
\left[
\left(
-\frac{\zeta'}{\zeta}
\right)
\frac1{|\zeta|^2}
\right]
=
\frac12
\partial_\sigma
\left|
\frac1{\zeta(s)}
\right|^2,
}
$$

and

$$
\boxed{
\Im
\left[
\left(
-\frac{\zeta'}{\zeta}
\right)
\frac1{|\zeta|^2}
\right]
=
-\frac12
\partial_t
\left|
\frac1{\zeta(s)}
\right|^2.
}
$$

Thus the natural prime/Mertens Mellin cross state is a gradient observable of the reciprocal-zeta energy.

This explains why the mixed state exposes $\zeta'(\rho)$ without generating a new horizontal pole location.

The Mertens state is itself root-level.

A fixed-power bound

$$
M(x)
\ll
x^{1-d+o(1)}
$$

forces

$$
\beta_*
\le
1-d,
$$

while a zero-free strip of that width gives the corresponding Mertens estimate at exponent resolution.

The Weak Mertens Conjecture is even stronger: classical work shows it implies RH, simplicity of the zeta zeros, and convergence of

$$
\boxed{
\sum_\rho
\frac1{
|\rho\zeta'(\rho)|^2
}.
}
$$

Modern work on negative moments of $\zeta'(\rho)$ confirms that this derivative sector remains difficult.

Bui obtains conditional upper bounds for negative discrete moments on large subfamilies of zeros.

Gao and Zhao obtain lower bounds for negative moments under RH and simple-zero hypotheses.

Ng's work on the distribution of the Mertens function uses RH together with the Gonek–Hejhal negative-moment conjecture.

Thus the derivative-sensitive information supplied by the mixed state is real, but it belongs to an already hard Mertens / zero-derivative sector.

The Campaign conclusion is:

```text
PRIME / MERTENS CROSS SPECTRUM

SPECTRAL NOVELTY:
YES — it contains 1/zeta'(rho).

UNIVERSAL BOUNDARY FORCING:
YES — a simple boundary zero gives a nonzero same-zero cross atom;
multiple zeros give stronger logarithmic forcing.

HORIZONTAL EXPONENT NOVELTY:
NO — the critical mixed exponent is exactly kappa_*.

LINEAR DIRICHLET COUPLING:
COLLAPSES TO WEIGHTED MERTENS.

NATURAL MELLIN COUPLING:
IS A GRADIENT OF RECIPROCAL-ZETA ENERGY.
```

Therefore the global prime/Mertens cross spectrum is closed as a **standalone horizontal PESC amplifier**.

It remains useful as a possible auxiliary route for zero simplicity and derivative-moment information.

The next screening should move beyond finite collections of zeta-derived linear fields whose singularities all occur at the same zero locations.

No RH theorem is claimed.

---

# 1. Exponential smoothing

Use

$$
e^{-y}
=
\frac1{2\pi i}
\int_{(c)}
\Gamma(s)y^{-s}ds.
$$

Therefore

$$
\sum_n
\Lambda(n)e^{-n/X}
=
\frac1{2\pi i}
\int_{(c)}
\Gamma(s)X^s
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
ds.
$$

The pole at $s=1$ contributes $X$.

Subtracting gives $P(X)$.

Similarly,

$$
\sum_n
\mu(n)e^{-n/X}
=
\frac1{2\pi i}
\int_{(c)}
\Gamma(s)X^s
\frac1{\zeta(s)}
ds.
$$

---

# 2. Simple-zero responses

Let $\rho$ be simple.

Since

$$
-\frac{\zeta'}{\zeta}(s)
=
-\frac1{s-\rho}
+
O(1),
$$

the prime residue is

$$
\boxed{
-\Gamma(\rho)X^\rho.
}
$$

Since

$$
\frac1{\zeta(s)}
=
\frac1{
\zeta'(\rho)(s-\rho)
}
+
O(1),
$$

the Mertens residue is

$$
\boxed{
\frac{
\Gamma(\rho)
}{
\zeta'(\rho)
}
X^\rho.
}
$$

Create:

```text
B-RH-150
A_SIMPLE_ZETA_ZERO_HAS_PRIME_AND_MERTENS_SMOOTHED_RESPONSES_WITH_COMMON_POWER_X_TO_RHO_AND_RELATIVE_WEIGHT_ONE_OVER_ZETA_PRIME_RHO
CERTIFIED
```

---

# 3. Same-zero cross coefficient

For a simple zero,

$$
A_\rho
=
-\Gamma(\rho),
$$

$$
B_\rho
=
\frac{
\Gamma(\rho)
}{
\zeta'(\rho)
}.
$$

Thus

$$
\boxed{
A_\rho
\overline{B_\rho}
=
-
\frac{
|\Gamma(\rho)|^2
}{
\overline{\zeta'(\rho)}
}.
}
$$

This is nonzero.

Create:

```text
B-RH-151
THE_PRIME_MERTENS_SAME_ZERO_CROSS_ATOM_CONTAINS_DERIVATIVE_DATA_NOT_PRESENT_IN_THE_PRIME_ERROR_TWO_POINT_SPECTRUM
CERTIFIED
```

---

# 4. No need for a uniform derivative lower bound

Suppose a fixed zero $\rho$ exists.

Then

$$
0<
|\zeta'(\rho)|
<
\infty
$$

if $\rho$ is simple.

Hence the cross coefficient is a fixed nonzero constant depending on $\rho$.

If an arithmetic theorem improves the cross exponent by fixed $\eta>0$, the ratio between the hypothetical boundary lower and the upper contains

$$
X^\eta.
$$

Therefore the power contradiction eventually dominates any fixed value of

$$
|\zeta'(\rho)|.
$$

Thus lack of a uniform derivative estimate does not destroy fixed-power zero exclusion.

---

# 5. Multiple zeros

Suppose

$$
\zeta(s)
=
\frac{
\zeta^{(m)}(\rho)
}{
m!
}
(s-\rho)^m
+
O
\left(
(s-\rho)^{m+1}
\right).
$$

Then

$$
\frac1{\zeta(s)}
=
\frac{
m!
}{
\zeta^{(m)}(\rho)
}
(s-\rho)^{-m}
+
O
\left(
(s-\rho)^{-m+1}
\right).
$$

Taking the residue against

$$
\Gamma(s)X^s
$$

gives the leading term

$$
\boxed{
\frac{
m\Gamma(\rho)
}{
\zeta^{(m)}(\rho)
}
X^\rho
(\log X)^{m-1}.
}
$$

The prime logarithmic derivative always has residue $-m$.

Therefore multiplicity adds polynomial logarithmic growth to the mixed state.

Create:

```text
B-RH-152
A_MULTIPLE_ZETA_ZERO_STRENGTHENS_THE_MERTENS_MIXED_FORCING_BY_A_LOG_X_POLYNOMIAL_WITHOUT_CHANGING_THE_HORIZONTAL_POWER
CERTIFIED
```

---

# 6. Horizontal exponent of the mixed cross atom

Let

$$
\rho=\beta+i\gamma.
$$

Both linear fields have amplitude

$$
X^\beta
$$

at the zero.

Therefore a degree-two same-zero cross amplitude has size

$$
\boxed{
X^{2\beta}.
}
$$

Normalize by $X^2$.

The fixed-power saving is

$$
\boxed{
2(1-\beta).
}
$$

At the rightmost abscissa,

$$
\boxed{
s_{PM}^*
=
2(1-\beta_*).
}
$$

By the PESC equivalence,

$$
\boxed{
s_{PM}^*
=
\kappa_*.
}
$$

Create:

```text
B-RH-153
THE_PRIME_MERTENS_SAME_ZERO_CROSS_SPECTRUM_HAS_THE_SAME_MAXIMAL_HORIZONTAL_POWER_EXPONENT_AS_PESC
CERTIFIED_AT_EXPONENT_RESOLUTION
```

---

# 7. Positive cross energy does not change the result

A positive frequency-unresolved detector can square the same-zero cross amplitudes.

Its boundary contribution has size

$$
X^{4\beta}.
$$

Relative to $X^4$, its saving exponent is

$$
4(1-\beta).
$$

But the observable has four linear copies.

The corresponding PESC conversion is

$$
\frac{2}{4}
\cdot
4(1-\beta)
=
2(1-\beta).
$$

Hence positivity by squaring does not improve the per-copy horizontal exponent.

This is the mixed-state analogue of Papers 81–82.

---

# 8. Dirichlet convolution collapse

The Dirichlet series are

$$
\sum_n
\frac{\Lambda(n)}{n^s}
=
-\frac{\zeta'}{\zeta}(s),
$$

and

$$
\sum_n
\frac{\mu(n)}{n^s}
=
\frac1{\zeta(s)}.
$$

Their product is

$$
\boxed{
-\frac{\zeta'}{\zeta^2}(s)
=
\left(
\frac1{\zeta(s)}
\right)'.
}
$$

But

$$
\left(
\sum_n
\frac{\mu(n)}{n^s}
\right)'
=
-\sum_n
\frac{
\mu(n)\log n
}{
n^s
}.
$$

Therefore:

## Theorem 8.1 — Prime/Möbius convolution identity

$$
\boxed{
(\Lambda*\mu)(n)
=
-\mu(n)\log n.
}
$$

Create:

```text
B-RH-154
LINEAR_MULTIPLICATIVE_PRIME_MOBIUS_COUPLING_COLLAPSES_EXACTLY_TO_A_LOG_WEIGHTED_MERTENS_STATE
CERTIFIED
```

---

# 9. Mellin gradient identity

Let

$$
F(s)=\frac1{\zeta(s)}.
$$

Then

$$
F'(s)
=
-\frac{\zeta'(s)}{\zeta(s)^2}.
$$

Therefore

$$
\boxed{
F'(s)\overline{F(s)}
=
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
\frac1{|\zeta(s)|^2}.
}
$$

For

$$
s=\sigma+it,
$$

$$
\partial_\sigma|F|^2
=
2\Re(F'\overline F),
$$

and

$$
\partial_t|F|^2
=
-2\Im(F'\overline F).
$$

Thus:

## Theorem 9.1 — Prime/Mertens spectral-gradient identity

$$
\boxed{
\Re
\left[
\left(
-\frac{\zeta'}{\zeta}
\right)
\frac1{|\zeta|^2}
\right]
=
\frac12
\partial_\sigma
\left|
\frac1\zeta
\right|^2,
}
$$

$$
\boxed{
\Im
\left[
\left(
-\frac{\zeta'}{\zeta}
\right)
\frac1{|\zeta|^2}
\right]
=
-\frac12
\partial_t
\left|
\frac1\zeta
\right|^2.
}
$$

Create:

```text
B-RH-155
THE_NATURAL_PRIME_MERTENS_MELLIN_CROSS_STATE_IS_THE_GRADIENT_OF_RECIPROCAL_ZETA_ENERGY
CERTIFIED
```

---

# 10. Mertens fixed-power exponent is itself root-level

The identity

$$
\frac1{\zeta(s)}
=
s
\int_1^\infty
M(x)x^{-s-1}dx
$$

in the initial half-plane shows that a bound

$$
M(x)
\ll
x^\theta
$$

analytically continues $1/\zeta$ to

$$
\Re s>\theta.
$$

Hence no zeta zero can lie there.

Conversely, a fixed zero-free strip gives the corresponding Mertens bound at exponent resolution by standard Perron / smoothing.

Thus the Mertens state itself carries the same rightmost-zero horizontal location.

The prime/Mertens cross does not create a new real-part exponent.

---

# 11. Weak Mertens and derivative moments

The Weak Mertens Conjecture states

$$
\boxed{
\int_1^X
\left(
\frac{M(x)}x
\right)^2dx
\ll
\log X.
}
$$

Classical results imply that WMC forces:

- RH;
- simplicity of all nontrivial zeros;
- convergence of
  $$
  \boxed{
  \sum_\rho
  \frac1{
  |\rho\zeta'(\rho)|^2
  }.
  }
  $$

Thus derivative-sensitive Mertens information is at least as hard as root-level spectral information.

---

# 12. Current negative-moment calibration

Negative moments

$$
J_{-k}(T)
=
\sum_{0<\gamma\le T}
|\zeta'(\rho)|^{-2k}
$$

are closely tied to Mertens bounds.

Current results remain strongly conditional or partial:

- Ng studies the limiting distribution of normalized Mertens under RH together with a Gonek–Hejhal negative-moment conjecture;
- Gao and Zhao prove lower bounds for negative moments under RH and simple-zero hypotheses;
- Bui proves conditional upper bounds over large subfamilies of zeros.

This confirms that the additional derivative coordinate is mathematically meaningful but not presently an easier route to horizontal zero exclusion.

---

# 13. Mixed-state verdict

The screen gives:

```text
GLOBAL PRIME / MERTENS MIXED STATE

NEW INFORMATION BEYOND PRIME C2:
YES.

SINGLE-BOUNDARY-PAIR FORCING:
YES.

MULTIPLE-ZERO FORCING:
YES, STRONGER BY LOG POWERS.

HORIZONTAL POWER GAIN:
NO.

LINEAR CONVOLUTION NOVELTY:
NO.

MELLIN CROSS NOVELTY:
DERIVATIVE-SENSITIVE, BUT A GRADIENT OF MERTENS ENERGY.
```

Therefore:

```text
PRIME_MERTENS_CROSS_SPECTRUM
CLOSED AS A STANDALONE HORIZONTAL PESC AMPLIFIER.
```

It may remain useful for:

- zero simplicity;
- negative moments;
- derivative-size restrictions;
- auxiliary vertical zero geometry.

---

# 14. Stronger mixed-field screening principle

Papers 82–84 suggest a broader rule.

Suppose a finite collection of linear arithmetic fields has rightmost-zero responses

$$
X^\rho
c_j(\rho),
$$

where the coefficients $c_j(\rho)$ may contain:

- $\rho$ ;
- $\zeta'(\rho)$ ;
- finite Euler factors;
- test transforms.

Any homogeneous degree- $q$ same-zero statistic then has horizontal size

$$
X^{q\beta}.
$$

Its normalized fixed-power threshold is

$$
q(1-\beta).
$$

Dividing by copy degree returns the same one-zero horizontal exponent

$$
1-\beta.
$$

Thus adding finitely many zeta-derived linear fields can add **vertical spectral coordinates** without automatically adding horizontal exponent leverage.

The next route must exploit a structural inequality whose arithmetic strength is not merely homogeneity in common $X^\rho$ modes.

---

# 15. External calibration

## 15.1. Nathan Ng

N. Ng,
*The distribution of the summatory function of the Möbius function*,
Proceedings of the London Mathematical Society 89 (2004), 361–389.

Assuming RH and a Gonek–Hejhal negative-moment conjecture, Ng proves limiting-distribution and strong weak-Mertens results.

URL:

https://doi.org/10.1112/S0024611504014741

## 15.2. Bui, 2024

H. M. Bui,
*Negative discrete moments of the derivative of the Riemann zeta-function*,
Bulletin of the London Mathematical Society 56 (2024), 2680–2705.

The paper obtains conditional upper bounds for negative moments on large subfamilies of zeros and records the classical consequences of the Weak Mertens Conjecture.

URL:

https://doi.org/10.1112/blms.13092

## 15.3. Gao–Zhao, 2023

P. Gao and L. Zhao,
*Lower bounds for negative moments of $\zeta'(\rho)$*,
Mathematika 69 (2023).

They establish lower bounds for negative derivative moments under RH and simple-zero assumptions.

URL:

https://doi.org/10.1112/mtk.12219

---

# 16. State transition

Advance candidate state

$$
v1.74
\to
v1.75.
$$

Add:

```text
B-RH-150
A_SIMPLE_ZETA_ZERO_HAS_PRIME_AND_MERTENS_SMOOTHED_RESPONSES_WITH_COMMON_POWER_X_TO_RHO_AND_RELATIVE_WEIGHT_ONE_OVER_ZETA_PRIME_RHO

B-RH-151
THE_PRIME_MERTENS_SAME_ZERO_CROSS_ATOM_CONTAINS_DERIVATIVE_DATA_NOT_PRESENT_IN_THE_PRIME_ERROR_TWO_POINT_SPECTRUM

B-RH-152
A_MULTIPLE_ZETA_ZERO_STRENGTHENS_THE_MERTENS_MIXED_FORCING_BY_A_LOG_X_POLYNOMIAL_WITHOUT_CHANGING_THE_HORIZONTAL_POWER

B-RH-153
THE_PRIME_MERTENS_SAME_ZERO_CROSS_SPECTRUM_HAS_THE_SAME_MAXIMAL_HORIZONTAL_POWER_EXPONENT_AS_PESC

B-RH-154
LINEAR_MULTIPLICATIVE_PRIME_MOBIUS_COUPLING_COLLAPSES_EXACTLY_TO_A_LOG_WEIGHTED_MERTENS_STATE

B-RH-155
THE_NATURAL_PRIME_MERTENS_MELLIN_CROSS_STATE_IS_THE_GRADIENT_OF_RECIPROCAL_ZETA_ENERGY
```

Update:

```text
GLOBAL_PRIME_ERROR_MERTENS_CROSS_SPECTRUM
CLOSED_AS_STANDALONE_HORIZONTAL_AMPLIFIER
```

No RH certificate is created.

---

# 17. Recommended next action

The next round should formalize the broader **common-power multi-field barrier** hinted in Section 14.

The goal is to determine exactly which mixed constructions are ruled out before another arithmetic candidate is developed.

If every finite family of meromorphic zeta-derived linear fields with common zero exponent $X^\rho$ is horizontally degree-neutral, then the next route must introduce either:

- a nonhomogeneous scale operation;
- a dynamic / adaptive constraint;
- an inequality connecting two arithmetic fields at different natural exponents;
- or genuinely non-zeta-derived ordinary-prime information.

That classification should be completed before opening another root frontier.

---

# 18. Conclusion

The prime/Mertens mixed state is genuinely richer than the prime error alone.

It knows $\zeta'(\rho)$.

It sees multiple-zero multiplicity.

But all fields still ride on the same horizontal mode $X^\rho$.

The extra information is vertical, not horizontal.

The natural linear coupling collapses to weighted Mertens, and the natural Mellin coupling is a gradient of reciprocal-zeta energy.

Thus the route does not supply a new fixed-power PESC amplifier.
