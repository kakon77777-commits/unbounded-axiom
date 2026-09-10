# CSM_RH Paper 57

## Turan-Gallagher Detector Saturation, Seed-Shifted Mellin Criticality, and the No-Free Single-Zero Coercivity Barrier

**Project:** CSM_RH  
**Paper:** 57  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Track:** SG3 — `SEEDED_ZERO_DETECTOR_WITH_PRIME_SIDE_COERCIVITY`  
**Status:** CLASSICAL SG3A/SG3B DETECTOR ROUTE CLOSED AS NON-AMPLIFYING / NEW ARITHMETIC EXCESS TARGET OPEN  
**Canonical entry state:** v1.47 / Paper 56 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Campaign 46 seeks a theorem which, from a seed PESC exponent

$$
\kappa>0,
$$

creates a strict improvement

$$
\kappa\mapsto\kappa+\eta.
$$

Paper 56 showed that the shrinking-threshold route becomes a true amplifier after seeding, but that its good-set threshold must cross the boundary scale

$$
\nu>\frac{\kappa}{2}.
$$

The present paper audits a different route: use a Turan power-sum zero detector to force a large prime-side observable when a boundary zero exists, then contradict that lower bound by a seed-derived upper bound.

The classical inverse short-interval method of Bombieri and Zaccagnini provides precisely such a cancellation-robust detector. For

$$
w=1+it,
$$

define

$$
\mathcal D_w(x)
=
\int_x^{x^{A_0}}
\left|
\sum_{x<n\le y}
\frac{\Lambda(n)-1}{n^w}
\right|^2
\frac{dy}{y}.
$$

A classical Turan detector theorem states that, if the zeta function has a zero in the circle

$$
|s-w|\le r,
$$

then for suitable absolute constants and every sufficiently large $x$,

$$
\boxed{
\mathcal D_w(x)
\gg_C
(\log x)^3x^{-Cr}.
}
$$

On the other hand, seed PESC $(\kappa)$ implies the pointwise estimate

$$
A(u):=\psi(u)-u
\ll
u^{1-\kappa/2+o(1)}.
$$

Partial summation then gives, for $|t|\le T$ and $x\ge T^B$,

$$
\boxed{
\mathcal D_w(x)
\ll
x^{-\kappa+2/B+o(1)}.
}
$$

Comparing the two bounds shows that the classical detector can contradict a zero only when

$$
\boxed{
Cr
<
\kappa-\frac{2}{B}.
}
$$

Letting $B$ grow, the best radius reachable by this architecture is approximately

$$
r<\frac{\kappa}{C}.
$$

But the seed itself already excludes zeros with

$$
1-\beta<\frac{\kappa}{2}.
$$

Therefore a Turan-Gallagher detector with

$$
C\ge2
$$

cannot strictly amplify the seed. The classical quantitative constants are much larger than $2$, so the published detector is decisively on the non-amplifying side.

The paper then analyzes a seed-shifted detector which uses the Mellin transform directly at the seeded boundary

$$
\sigma_0
=
1-\frac{\kappa}{2}.
$$

Define

$$
\mathcal M(s)
=
\int_1^\infty
A(x)x^{-s-1}\,dx.
$$

PESC $(\kappa)$ gives analyticity for

$$
\Re s>\sigma_0.
$$

For fixed $r>0$ and every integer $m\ge0$, dyadic Cauchy-Schwarz gives the derivative growth

$$
\boxed{
\left|
\mathcal M^{(m)}
(\sigma_0+r+it)
\right|
\ll_r
m!
\left(
\frac{C}{r}
\right)^{m+1}.
}
$$

This has exactly the same critical order as a pole on the seed boundary. Indeed, the model

$$
E_{\rho}(x)=x^{\rho},
\qquad
\rho=\sigma_0+i\gamma,
$$

satisfies the seed dyadic mean-square exponent

$$
\int_X^{2X}|E_\rho(x)|^2dx
\asymp
X^{3-\kappa},
$$

while its Mellin transform is exactly

$$
\frac{1}{s-\rho},
$$

whose derivatives at $s=\rho+r$ are

$$
\boxed{
\frac{m!}{r^{m+1}}.
}
$$

For the actual Chebyshev error, a boundary zero produces the same pole order in the Mellin transform through

$$
-\frac{\zeta'(s)}{\zeta(s)}
=
s\mathcal M(s)
+
\frac{s}{s-1}.
$$

Thus the seed-shifted derivative detector is critically saturated: the seed upper bound and a boundary-pole lower bound have identical $r^{-(m+1)}$ growth.

This yields a no-free-coercivity theorem. Neither the classical Re $(s)=1$ Turan detector nor a seed-shifted Mellin derivative detector can create a strict strip gap using PESC $(\kappa)$ alone. A successful detector theorem must contain a genuinely new prime-side excess saving beyond the critical seed scale.

The paper defines one such explicit frontier. If a prime-side Turan-Gallagher detector upper bound

$$
\mathcal D_w(x)
\ll
x^{-\lambda+o(1)}
$$

were proved with

$$
\boxed{
\lambda>\frac{C\kappa}{2},
}
$$

then the classical detector would exclude the seeded boundary and create a strict fixed strip improvement. The seed gives only $\lambda=\kappa$, so for $C>2$ this target requires a substantial new arithmetic gain and is inefficient compared with the shrinking-threshold frontier F-RH-017.

SG3 therefore closes the standard single-zero detector route as a method barrier and passes the campaign to SG4: search for a genuinely nonlinear or arithmetic contraction mechanism which distinguishes the von Mangoldt sequence from the critically saturated Mellin power mode.

No RH theorem is claimed.

---

# 1. Entry state

Assume PESC $(\kappa)$ for fixed

$$
0<\kappa<1.
$$

Papers 55–56 give

$$
\boxed{
\beta_*
\le
1-\frac{\kappa}{2}
}
$$

and

$$
\boxed{
A(x)
=
\psi(x)-x
\ll
x^{1-\kappa/2+o(1)}.
}
$$

Set

$$
\boxed{
\sigma_0
=
1-\frac{\kappa}{2}.
}
$$

Campaign 46 / SG3 asks whether a single zero at or just to the left of this boundary can be detected by a prime-side observable with enough coercivity to force

$$
\beta_*
<
\sigma_0.
$$

---

# 2. Classical Turan-Gallagher prime detector

For

$$
w=1+it,
\qquad
2\le|t|\le T,
$$

define

$$
\boxed{
P_w(x,y)
=
\sum_{x<n\le y}
\frac{\Lambda(n)-1}{n^w}.
}
$$

Define the multiplicative detector energy

$$
\boxed{
\mathcal D_w(x)
=
\int_x^{x^{A_0}}
|P_w(x,y)|^2
\frac{dy}{y}.
}
$$

A classical result in the Bombieri-Turan-Zaccagnini inverse theory gives the following.

## External detector input

There exist absolute constants

$$
A_0\ge1,
\qquad
B_0\ge1,
\qquad
C_0>2
$$

such that, for an admissible detector radius $r$, if the Riemann zeta function has a zero in

$$
|s-w|\le r,
$$

then for every

$$
B\ge B_0,
\qquad
x\ge T^B,
$$

and every

$$
C>C_0,
$$

one has

$$
\boxed{
\mathcal D_w(x)
\gg_C
(\log x)^3x^{-Cr}.
}
$$

The published quantitative proof is based on Turan's Second Main Theorem and a Gallagher conversion to short-interval prime coefficient energy.

The constants are not claimed to be optimal.

The only feature needed below is that the zero-distance exponent is multiplied by a fixed detector loss $C$.

---

# 3. Seed upper bound for the same detector

By partial summation,

$$
\boxed{
P_w(x,y)
=
A(y)y^{-w}
-
A(x)x^{-w}
+
w
\int_x^y
A(u)u^{-w-1}\,du.
}
$$

Since

$$
\Re w=1
$$

and

$$
A(u)
\ll
u^{1-\kappa/2+\varepsilon},
$$

for every fixed

$$
0<\varepsilon<\frac{\kappa}{2},
$$

we have

$$
|A(y)y^{-w}|
+
|A(x)x^{-w}|
\ll
x^{-\kappa/2+\varepsilon}.
$$

Moreover,

$$
\begin{aligned}
\left|
w
\int_x^y
A(u)u^{-w-1}\,du
\right|
&\ll
(1+|t|)
\int_x^\infty
u^{-1-\kappa/2+\varepsilon}\,du
\\
&\ll_{\kappa,\varepsilon}
(1+|t|)
x^{-\kappa/2+\varepsilon}.
\end{aligned}
$$

Thus

$$
\boxed{
|P_w(x,y)|
\ll
(1+T)
x^{-\kappa/2+o(1)}.
}
$$

If

$$
x\ge T^B,
$$

then

$$
T\le x^{1/B}.
$$

Hence

$$
\boxed{
|P_w(x,y)|^2
\ll
x^{-\kappa+2/B+o(1)}.
}
$$

Since

$$
\int_x^{x^{A_0}}\frac{dy}{y}
=
(A_0-1)\log x,
$$

we obtain:

## Theorem 3.1 — Seed upper bound for the classical detector

For every fixed admissible $B$,

$$
\boxed{
\mathcal D_w(x)
\ll
x^{-\kappa+2/B+o(1)}.
}
$$

Create:

```text
B-RH-061
SEEDED_TURAN_GALLAGHER_DETECTOR_UPPER_BOUND
CERTIFIED
```

---

# 4. Classical detector amplification test

Suppose a zero lies in

$$
|s-w|\le r.
$$

The external lower bound and Theorem 3.1 would give simultaneously

$$
x^{-Cr}
\ll
\mathcal D_w(x)
\ll
x^{-\kappa+2/B+o(1)}.
$$

For large $x$, these are incompatible only if

$$
\boxed{
Cr
<
\kappa-\frac{2}{B}.
}
$$

Thus the detector can exclude at most

$$
\boxed{
r
<
\frac{
\kappa-2/B
}{C}.
}
$$

Letting $B$ be arbitrarily large yields the limiting detector radius

$$
\boxed{
r_{\rm TG}
\le
\frac{\kappa}{C}.
}
$$

The seed zero-free half-plane already excludes a zero at the same ordinate whenever its horizontal distance from $\Re s=1$ is

$$
\boxed{
1-\beta
<
\frac{\kappa}{2}.
}
$$

Therefore:

## Theorem 4.1 — Classical Turan-Gallagher no-amplification criterion

A detector of the form above can strictly improve the seed only if

$$
\boxed{
C<2.
}
$$

If

$$
C=2,
$$

it can at best recover the seed boundary.

If

$$
C>2,
$$

it certifies only a weaker interior part of the zero-free region already known from the seed.

The classical quantitative Zaccagnini-Bombieri constants satisfy

$$
C_0\gg2.
$$

Thus the standard published detector architecture cannot amplify PESC $(\kappa)$.

Create:

```text
O-RH-136
CLASSICAL_TURAN_GALLAGHER_SINGLE_ZERO_DETECTOR_LOSES_TOO_MUCH_TO_AMPLIFY_A_PESC_SEED
CERTIFIED_AS_METHOD_BARRIER
```

This is a barrier for the quantified classical detector, not a theorem that every possible Turan refinement must have $C\ge2$.

---

# 5. Detector excess exponent

The preceding calculation suggests a clean arithmetic target.

Suppose instead that one proves

$$
\boxed{
\mathcal D_w(x)
\ll
x^{-\lambda+o(1)}
}
$$

for a fixed exponent $\lambda>0$.

The same Turan lower bound excludes zeros whenever

$$
Cr<\lambda.
$$

To push the zero-free boundary strictly beyond the seed line

$$
1-\beta=\frac{\kappa}{2},
$$

one needs

$$
\boxed{
\lambda
>
\frac{C\kappa}{2}.
}
$$

Define:

```text
F-RH-018
SEEDED_TURAN_GALLAGHER_DETECTOR_EXCESS_POWER
```

Target:

$$
\boxed{
\lambda
>
\frac{C\kappa}{2}.
}
$$

The seed itself supplies only

$$
\lambda=\kappa
$$

in the limit $B\to\infty$.

Therefore for $C>2$, F-RH-018 requires an arithmetic gain substantially stronger than the seed exponent.

This makes the classical detector less economical than F-RH-017, whose exceptional-set bridge only needs to cross the boundary threshold by an arbitrarily small fixed amount.

---

# 6. Why recentering the detector is natural

The classical detector works on the absolute-convergence line

$$
\Re s=1.
$$

After a seed exists, that line is unnecessarily far from the active zero boundary

$$
\sigma_0
=
1-\frac{\kappa}{2}.
$$

Paper 20 and Paper 53 give the prime-error Mellin transform

$$
\boxed{
\mathcal M(s)
=
\int_1^\infty
A(x)x^{-s-1}\,dx
}
$$

with

$$
-\frac{\zeta'(s)}{\zeta(s)}
=
s\mathcal M(s)
+
\frac{s}{s-1}.
$$

PESC $(\kappa)$ gives holomorphy of $\mathcal M$ in

$$
\boxed{
\Re s>\sigma_0.
}
$$

This suggests a seed-shifted detector at

$$
s=\sigma_0+r+it.
$$

The next sections show that the seed-shifted route removes the large absolute-line distance, but becomes exactly critically saturated.

---

# 7. Derivative bounds from the seed dyadic mean square

PESC $(\kappa)$ gives, for every fixed $\varepsilon>0$,

$$
\int_X^{2X}
|A(x)|^2dx
\ll_\varepsilon
X^{3-\kappa+\varepsilon}.
$$

For an integer

$$
m\ge0,
$$

differentiate the Mellin transform:

$$
\boxed{
\mathcal M^{(m)}(s)
=
(-1)^m
\int_1^\infty
A(x)
(\log x)^m
x^{-s-1}\,dx.
}
$$

Fix

$$
r>0
$$

and take

$$
s=\sigma_0+r+it.
$$

On a dyadic block

$$
X\le x\le2X,
$$

Cauchy-Schwarz gives

$$
\begin{aligned}
\left|
\int_X^{2X}
A(x)
(\log x)^m
x^{-s-1}\,dx
\right|
&\ll_\varepsilon
(\log X)^m
X^{(3-\kappa+\varepsilon)/2}
X^{-\sigma_0-r-1/2}
\\
&=
(\log X)^m
X^{-r+\varepsilon/2}.
\end{aligned}
$$

Choose, for example,

$$
\varepsilon=r.
$$

Then the dyadic block is

$$
\ll_r
(\log X)^m
X^{-r/2}.
$$

Summing over

$$
X=2^j
$$

uses

$$
\sum_{j\ge0}
j^m e^{-aj}
\ll
m!a^{-m-1}.
$$

Therefore:

## Theorem 7.1 — Seed-shifted Mellin derivative growth

For each fixed $r>0$,

$$
\boxed{
\left|
\mathcal M^{(m)}
(\sigma_0+r+it)
\right|
\ll_r
m!
\left(
\frac{C_r}{r}
\right)^{m+1}
}
$$

uniformly in real $t$ and integers $m\ge0$.

At the level of the distance exponent, the seed permits precisely

$$
r^{-(m+1)}.
$$

The constants are not asserted uniform as $r\downarrow0$, because the PESC $o(1)$ exponent does not provide such quantitative boundary uniformity.

---

# 8. Exact critical model

Consider

$$
\boxed{
E_\rho(x)
=
x^\rho,
\qquad
\rho=\sigma_0+i\gamma.
}
$$

Then

$$
\int_X^{2X}
|E_\rho(x)|^2dx
=
\int_X^{2X}
x^{2\sigma_0}dx
\asymp
X^{2\sigma_0+1}.
$$

Since

$$
2\sigma_0+1
=
3-\kappa,
$$

the model exactly saturates the PESC $(\kappa)$ dyadic mean-square exponent:

$$
\boxed{
\int_X^{2X}|E_\rho(x)|^2dx
\asymp
X^{3-\kappa}.
}
$$

Its Mellin transform is explicit:

$$
\boxed{
\int_1^\infty
E_\rho(x)x^{-s-1}dx
=
\frac1{s-\rho}
}
$$

for

$$
\Re s>\sigma_0.
$$

Hence

$$
\boxed{
\left|
\frac{d^m}{ds^m}
\frac1{s-\rho}
\right|_{s=\rho+r}
=
\frac{m!}{r^{m+1}}.
}
$$

Thus the derivative growth permitted by Theorem 7.1 is attained, in its exact distance exponent, by the seed-critical boundary mode.

Create:

```text
O-RH-137
SEED_SHIFTED_MELLIN_DERIVATIVE_BOUND_IS_CRITICALLY_SATURATED_BY_A_BOUNDARY_POLE
CERTIFIED_AS_MODEL_BARRIER
```

---

# 9. Actual zeta boundary pole has the same order

If the actual zeta function had a zero

$$
\rho
=
\sigma_0+i\gamma
$$

of multiplicity $m_\rho$, then

$$
-\frac{\zeta'(s)}{\zeta(s)}
$$

would have a pole

$$
-\frac{m_\rho}{s-\rho}.
$$

Since

$$
-\frac{\zeta'(s)}{\zeta(s)}
=
s\mathcal M(s)
+
\frac{s}{s-1},
$$

the Mellin transform has local form

$$
\boxed{
\mathcal M(s)
=
-\frac{
m_\rho
}{
\rho(s-\rho)
}
+
\text{holomorphic term}.
}
$$

Therefore, at

$$
s=\rho+r,
$$

the pole contribution to the $m$ -th derivative has size

$$
\boxed{
\asymp_\rho
\frac{
m_\rho m!
}{
r^{m+1}
}.
}
$$

The seed upper bound and the boundary-pole lower growth therefore have the same critical power of $r$ and $m$.

A Turan power-sum selection among derivatives cannot create a distance exponent margin from the seed alone.

---

# 10. Critical logarithmic-time normalization

The saturation is especially transparent in logarithmic time.

Set

$$
x=e^y
$$

and define the seed-normalized residual

$$
\boxed{
R_\kappa(y)
=
e^{-\sigma_0 y}
A(e^y).
}
$$

Then

$$
\begin{aligned}
\int_Y^{Y+\log2}
|R_\kappa(y)|^2dy
&=
\int_{e^Y}^{2e^Y}
|A(x)|^2
x^{-2\sigma_0-1}\,dx.
\end{aligned}
$$

PESC $(\kappa)$ gives

$$
\boxed{
\int_Y^{Y+\log2}
|R_\kappa(y)|^2dy
\le
e^{o(Y)}.
}
$$

A boundary zero mode

$$
A_\rho(x)
\sim
x^{\sigma_0+i\gamma}
$$

becomes

$$
\boxed{
R_{\kappa,\rho}(y)
\sim
e^{i\gamma y},
}
$$

a persistent harmonic with constant local energy.

Thus the seed-normalized log-time space explicitly permits the boundary oscillation.

A strict exponent improvement would require genuine exponential damping in $Y$, not merely a change of detector coordinates.

---

# 11. No-free single-zero coercivity theorem

The preceding two detector channels fail for complementary reasons.

## Absolute-line Turan-Gallagher detector

It has robust single-zero sensitivity but loses the zero distance by a factor $C$:

$$
r
\mapsto
Cr.
$$

For $C>2$ it is weaker than the seed strip.

## Seed-shifted Mellin detector

It removes the absolute-line distance loss, but the seed bound itself is exactly saturated by the boundary pole:

$$
\boxed{
m!r^{-m-1}.
}
$$

Therefore:

## Theorem 11.1 — No-free seeded detector amplification

PESC $(\kappa)$ alone supplies no quantitative margin in either:

1. the classical Turan-Gallagher detector energy; or
2. the seed-shifted Mellin derivative growth

that can force a strict zero-strip improvement.

A successful SG3 theorem must add a genuinely new arithmetic upper bound beyond the critical seed scale.

Create:

```text
O-RH-138
NO_FREE_SINGLE_ZERO_COERCIVITY_FROM_SEED_PESC_ALONE
CERTIFIED
```

This is compatible with Paper 55's general no-free-amplification theorem but now applies directly to cancellation-robust zero detector architectures.

---

# 12. Relation to classical inverse short-interval theory

Zaccagnini's inverse theorem proves that sufficiently strong uniform Selberg-integral estimates force zero-density and zero-free information.

The proof explicitly uses:

1. a Turan power-sum lower bound from a zero;
2. a lower bound for a prime Dirichlet-polynomial detector;
3. Gallagher's lemma;
4. a Selberg-integral upper bound.

This is exactly the SG3 philosophy.

The present audit shows why that classical detector is not automatically an amplifier after seeding: its zero-distance exponent has a fixed constant loss.

Richards' quasi-RH short-interval theorem provides a complementary calibration. A fixed strip

$$
\Re\rho
\le
\frac12+\delta
$$

implies normal prime distribution in almost all intervals of exponent exceeding $2\delta$, and the corresponding theorem for general signed measures is sharp at that scale.

For the CSM_RH seed,

$$
\delta
=
\frac{1-\kappa}{2},
$$

so the analytically forced short-interval scale is

$$
\alpha>1-\kappa.
$$

This supplies mesoscopic regularity but not the supercritical power accuracy

$$
\nu>\frac{\kappa}{2}
$$

required by Paper 56.

Thus known inverse and quasi-RH theory is consistent with the critical saturation found here.

---

# 13. SG3 verdict

The SG3 attack order was:

```text
SG3A
TURAN_POWER_SUM_BOUNDARY_ZERO_DETECTOR

SG3B
GALLAGHER_SHORT_INTERVAL_L2_COERCIVITY_WITH_SEED

SG3C
BOUNDARY_PACKET_PHASE_LOCALIZATION_AND_INERTIA

SG3D
PRIME_SIDE UPPER BOUND STRONG ENOUGH TO CONTRADICT DETECTOR LOWER BOUND
```

Verdict:

```text
SG3A
CLOSED_AS_CLASSICAL_DETECTOR_SINGLE_ZERO_SENSITIVE_BUT_CONSTANT_LOSS_NONAMPLIFYING

SG3B
CLOSED_AS_SEED_UPPER_BOUND_SATURATES_BELOW_REQUIRED_CLASSICAL_DETECTOR_EXCESS

SG3C
CLOSED_AS_SEED_SHIFTED_MELLIN_BOUNDARY_POLE_CRITICALITY

SG3D
OPEN_NEW_PRIME_SIDE_EXCESS_BOUND
```

The standard detector route is therefore structurally exhausted.

---

# 14. New frontier F-RH-018

Create:

```text
F-RH-018
SEEDED_TURAN_GALLAGHER_DETECTOR_EXCESS_POWER
```

A sufficient form is:

$$
\boxed{
\mathcal D_w(x)
\ll
x^{-\lambda+o(1)}
}
$$

uniformly in the detector range, with

$$
\boxed{
\lambda
>
\frac{C\kappa}{2}.
}
$$

Then the classical Turan lower bound excludes the seeded boundary and creates a strict zero-free strip improvement.

This target is mathematically valid but probably inefficient because the classical detector constant $C$ is large.

Therefore F-RH-018 is recorded as a secondary, not preferred, frontier.

---

# 15. Recommended SG4 direction

The remaining Campaign 46 track is

```text
SG4
NEW_ARITHMETIC_CONTRACTION_THEOREM
```

The next method should not merely change the zero detector.

It should exploit a property which the critical model

$$
x^{\sigma_0+i\gamma}
$$

does not possess but the von Mangoldt sequence does.

Candidate arithmetic asymmetries include:

```text
SG4A
PRIME_SUPPORT_AND_POSITIVITY_VERSUS_SMOOTH_BOUNDARY_MODE

SG4B
SEEDED_HEATH_BROWN_BILINEAR_MAJOR_ARC_INCOMPATIBILITY

SG4C
NONLINEAR_EULER_PRODUCT_BOUNDARY_MODE_DETECTOR

SG4D
MULTISCALE PRIME_FACTOR_COHERENCE_BREAKING
```

A valid SG4 theorem must output an explicit fixed exponent gain.

Hard rejection:

```text
ANOTHER_LINEAR_MELLIN_OR_TURAN_DETECTOR_WITH_CRITICAL_SEED_GROWTH
```

---

# 16. External calibration

## 16.1. Zaccagnini inverse short-interval theorem

Alessandro Zaccagnini,
*Primes in almost all short intervals and the distribution of the zeros of the Riemann zeta-function*,
Acta Arithmetica 84 (1998), 225–244.

The inverse section uses Turan's Second Main Theorem to turn a zero into a lower bound for a Dirichlet-prime detector, then Gallagher's lemma and a Selberg-integral upper bound to control zeros.

URL:

https://people.dmi.unipr.it/alessandro.zaccagnini/psfiles/papers/Q429.pdf

## 16.2. Richards' quasi-RH short-interval calibration

Ian Richards,
*On the normal density of primes in short intervals*,
Journal of Number Theory 12 (1980), 378–384.

Under a quasi-RH strip of width $\delta$ about the critical line, almost-all short-interval normality follows for interval exponent exceeding $2\delta$. Richards also gives a signed-measure counterexample showing sharpness of the general theorem at the boundary scale.

## 16.3. Pintz oscillation calibration

Classical Turan-Pintz-Revesz work shows that an individual zeta zero forces oscillation of the global prime-number-theorem error at its natural $x^\beta$ scale. This confirms the role of single-zero sensitive detectors, while short intervals require additional control because a single zero contribution is reduced by the differencing factor.

---

# 17. State transition

Advance the candidate state from

$$
v1.47
$$

to

$$
v1.48.
$$

Add:

```text
B-RH-061
SEEDED_TURAN_GALLAGHER_DETECTOR_UPPER_BOUND
CERTIFIED
```

Add:

```text
O-RH-136
CLASSICAL_TURAN_GALLAGHER_SINGLE_ZERO_DETECTOR_LOSES_TOO_MUCH_TO_AMPLIFY_A_PESC_SEED
CERTIFIED_AS_METHOD_BARRIER
```

Add:

```text
O-RH-137
SEED_SHIFTED_MELLIN_DERIVATIVE_BOUND_IS_CRITICALLY_SATURATED_BY_A_BOUNDARY_POLE
CERTIFIED_AS_MODEL_BARRIER
```

Add:

```text
O-RH-138
NO_FREE_SINGLE_ZERO_COERCIVITY_FROM_SEED_PESC_ALONE
CERTIFIED
```

Add frontier:

```text
F-RH-018
SEEDED_TURAN_GALLAGHER_DETECTOR_EXCESS_POWER
OPEN / SECONDARY
```

Campaign 46:

```text
SG1 STRUCTURAL CLOSED / ARITHMETIC OPEN
SG2 STRUCTURAL CLOSED / ARITHMETIC OPEN
SG3 STANDARD DETECTOR ROUTE CLOSED / EXCESS BOUND OPEN
SG4 ACTIVE
```

No RH certificate is created.

---

# 18. Conclusion

The single-zero detection problem is no longer ambiguous.

Classical Turan-Gallagher machinery is cancellation-robust, but its quantitative distance loss is too large to amplify an existing PESC seed.

Moving the detector to the seeded Mellin boundary removes that geometric loss, but exposes a sharper obstruction:

$$
\boxed{
\text{the seed bound itself is pole-scale sharp}.
}
$$

A boundary mode has exactly the Mellin derivative growth allowed by the seed.

Therefore no linear detector can manufacture the missing exponent from existing information alone.

The next advance must distinguish the arithmetic prime sequence from the smooth critical boundary mode.

That is SG4.
