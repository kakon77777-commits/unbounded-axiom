# CSM_RH Paper 58

## Euler-Product Positivity Walls, Higher-Derivative Sign Loss, and the Heath-Brown Joint-Covariance Requirement

**Project:** CSM_RH  
**Paper:** 58  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Track:** SG4 — `NEW_ARITHMETIC_CONTRACTION_THEOREM`  
**Status:** STANDARD POSITIVITY / LINEAR-FACTORIZATION ROUTES CLOSED AS NON-AMPLIFYING; DIRECT ARITHMETIC FRONTIERS REMAIN OPEN  
**Canonical entry state:** v1.48 / Paper 57 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Campaign 46 seeks a genuine arithmetic theorem which upgrades a seed exponent

$$
\operatorname{PESC}(\kappa)
$$

to

$$
\operatorname{PESC}(\kappa+\eta)
$$

for some fixed

$$
\eta>0.
$$

Papers 55–57 showed that this is exactly a fixed zero-strip improvement problem and that principal-arc projection, standard moment-Markov methods, and classical Turan-Gallagher single-zero detectors do not generate the missing exponent.

The present paper audits the remaining standard candidates based on Euler-product positivity, higher logarithmic derivatives, prime support positivity, and Heath-Brown factorization.

First, positivity in the absolute-convergence half-plane has an intrinsic logarithmic-distance wall. Let

$$
F(s)
=
-\frac{\zeta'(s)}{\zeta(s)}.
$$

For

$$
\sigma>1,
$$

the Dirichlet coefficients of $F$ are nonnegative:

$$
F(s)
=
\sum_{n\ge1}
\frac{\Lambda(n)}{n^s}.
$$

A nonnegative trigonometric polynomial with nonnegative cosine coefficients therefore produces the classical positivity inequality

$$
\sum_{j=0}^{J}
a_j
\Re
F(\sigma+ijt)
\ge0.
$$

If

$$
\rho=\beta+i\gamma
$$

is the target zero and $t=\gamma$, the $j=1$ term contains the negative zero pole

$$
-\frac{a_1}{\sigma-\beta}.
$$

However, the same explicit formula contains an archimedean contribution of order

$$
\frac12
\left(
\sum_{j\ge1}a_j
\right)
\log|\gamma|.
$$

In the standard one-target zero-dropping positivity architecture, a contradiction is therefore possible only if

$$
\boxed{
1-\beta
\ll
\frac1{\log|\gamma|}.
}
$$

A zero at a fixed seeded distance

$$
1-\beta
=
\frac{\kappa}{2}
$$

is asymptotically invisible to this scale comparison.

This explains why modern positivity-based improvements continue to sharpen constants in logarithmic zero-free regions rather than create fixed strips. In 2026, Bellotti, Trudgian and Yang improved the classical-shaped region to

$$
\sigma
\ge
1-\frac1{4.896\log t},
$$

but the shape remains logarithmic.

Second, one cannot remove the logarithmic wall simply by taking higher derivatives of the logarithmic derivative. Define

$$
F_m(s)
=
(-1)^m
\frac{d^m}{ds^m}
F(s)
=
\sum_{n\ge1}
\frac{
\Lambda(n)(\log n)^m
}{
n^s
},
$$

which again has nonnegative Dirichlet coefficients for $\Re s>1$.

A target zero pole is amplified to order

$$
m!
(s-\rho)^{-m-1}.
$$

But for every

$$
m\ge1,
$$

the zero-side kernel

$$
\Re
(s-\rho)^{-m-1}
$$

changes sign as the ordinate separation varies. Thus the crucial one-sign Poisson-kernel property of $m=0$ is lost. Other zeros can no longer be discarded in a positivity upper bound. Higher derivatives amplify the target pole and simultaneously destroy the zero-side positivity that made the classical argument possible.

Third, raw positivity of the prime measure is far below the seeded boundary scale. A boundary zero mode contributes a short-interval error of relative size

$$
N^{-\kappa/2}.
$$

Since

$$
\psi(x+H)-\psi(x)
=
H+U_H(x)
$$

and

$$
N^{-\kappa/2}=o(1),
$$

the positivity condition

$$
\psi(x+H)-\psi(x)\ge0
$$

is automatically compatible with such a mode. Prime support positivity therefore supplies no fixed-power boundary suppression.

Fourth, the exact Heath-Brown factorization route is already algebraically calibrated by Paper 47. The complete alternating cross- $j$ recombination returns the original von Mangoldt root object. If the lag vectors of the finitely many factorization components are each controlled only at seed scale

$$
NH^2N^{-\kappa+o(1)},
$$

componentwise triangle or Cauchy estimates can recover at best the same seed scale. A strict amplifier requires a genuinely joint covariance deficit of fixed-power size, for example

$$
\boxed{
\left\|
\sum_j c_jX_j
\right\|_2^2
\le
N^{-\eta}
\sum_j|c_j|^2\|X_j\|_2^2.
}
$$

Such a theorem is not supplied by the identity itself. Paper 47's exact recoupling and Papers 43–46's component barriers show that alternating signs, Ramaré extraction, structured-weight smallness, and componentwise Type-II estimates do not create this fixed-power joint deficit for free.

Finally, the paper calibrates positivity inside the critical strip. Recent work on the real part of the logarithmic derivative of the Riemann xi-function shows that positivity near the critical line may remain compatible with hypothetical off-critical zeros outside local neighborhoods of those zeros. Thus positivity of the xi log-derivative is not, by itself, a global off-critical exclusion principle.

The conclusion is a closure theorem for the standard SG4 candidates:

```text
Euler-product coefficient positivity:
non-amplifying at fixed-strip scale.

Higher log-derivative positivity:
zero-side sign structure fails.

Raw prime-measure positivity:
boundary error is too small relative to the positive main term.

Existing Heath-Brown factorization:
requires a new fixed-power joint cross-j covariance theorem.
```

No new equivalent criterion is needed. The preferred direct arithmetic frontier remains Paper 56's F-RH-017:

$$
\boxed{
\#\left\{
x:
|U_H(x)|>HN^{-\nu}
\right\}
\ll
N^{1-c},
\qquad
\nu>\frac{\kappa}{2},
\qquad
c>2(1-\alpha).
}
$$

Campaign 46 has therefore exhausted its standard structural mechanisms. The next progress must be a genuinely new prime-side excess estimate.

No RH theorem is claimed.

---

# 1. Entry state

Assume

$$
\operatorname{PESC}(\kappa)
$$

for fixed

$$
0<\kappa<1.
$$

The inherited facts are:

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
|\psi(x)-x|
\ll
x^{1-\kappa/2+o(1)}.
}
$$

Define

$$
\boxed{
d_{\rm seed}
=
\frac{\kappa}{2}.
}
$$

A hypothetical zero on the seed boundary has

$$
\beta
=
1-d_{\rm seed}.
$$

Campaign 46 asks for an arithmetic mechanism proving a fixed additional distance from $\Re s=1$.

---

# 2. Absolute-convergence positivity

For

$$
\Re s>1,
$$

define

$$
\boxed{
F(s)
=
-\frac{\zeta'(s)}{\zeta(s)}
=
\sum_{n=1}^{\infty}
\frac{\Lambda(n)}{n^s}.
}
$$

The coefficients are nonnegative.

Let

$$
P(\theta)
=
a_0
+
\sum_{j=1}^{J}
a_j\cos(j\theta)
$$

satisfy

$$
P(\theta)\ge0
$$

for all real $\theta$, with

$$
a_j\ge0.
$$

Then for every

$$
\sigma>1
$$

and real $t$,

$$
\boxed{
\sum_{j=0}^{J}
a_j
\Re
F(\sigma+ijt)
=
\sum_{n\ge1}
\frac{
\Lambda(n)
}{
n^\sigma
}
P(t\log n)
\ge0.
}
$$

This is the basic Euler-product positivity mechanism used in the classical zero-free-region method.

---

# 3. One-target positivity ledger

Let

$$
\rho=\beta+i\gamma
$$

be a hypothetical target zero, with

$$
|\gamma|
$$

large.

Set

$$
t=\gamma
$$

and

$$
\sigma=1+\eta,
\qquad
\eta>0.
$$

Write

$$
d=1-\beta.
$$

Then

$$
\sigma-\beta
=
\eta+d.
$$

The completed-zeta explicit formula gives, uniformly in the relevant right half-plane,

$$
\Re F(\sigma+i\tau)
=
\frac12\log(|\tau|+3)
-
\sum_\rho
\frac{
\sigma-\Re\rho
}{
(\sigma-\Re\rho)^2+(\tau-\Im\rho)^2
}
+
O_\sigma(1)
$$

for nonzero $\tau$, with the pole at $1$ treated separately at $\tau=0$.

In the $j=1$ term, the target zero contributes

$$
\boxed{
-\frac1{\eta+d}.
}
$$

Dropping all other negative zero contributions yields the standard one-target upper bound.

At $j=0$,

$$
F(1+\eta)
=
\frac1{\eta}
+
O(1).
$$

For $j\ge1$,

$$
\Re F(1+\eta+ij\gamma)
\le
\frac12
\log(|j\gamma|+3)
+
O_\eta(1),
$$

except that the target negative pole is retained for $j=1$.

Hence

$$
\begin{aligned}
0
&\le
\sum_{j=0}^{J}
a_j
\Re
F(1+\eta+ij\gamma)
\\
&\le
\frac{a_0}{\eta}
+
\frac12
\left(
\sum_{j\ge1}a_j
\right)
\log|\gamma|
-
\frac{a_1}{\eta+d}
+
O_{P,\eta}
\left(
1+\log(J+2)
\right).
\end{aligned}
$$

This is the classical positivity budget in the form relevant to the seed audit.

---

# 4. The logarithmic-distance wall

Set

$$
A_+
=
\sum_{j\ge1}a_j.
$$

Since

$$
a_1\le A_+,
$$

the target zero term satisfies

$$
\frac{a_1}{\eta+d}
\le
\frac{A_+}{d}.
$$

If

$$
d
\gg
\frac1{\log|\gamma|},
$$

then

$$
\frac{A_+}{d}
\ll
A_+\log|\gamma|.
$$

Thus the target pole is no larger than the unavoidable archimedean scale retained in the standard zero-dropping positivity ledger.

Therefore:

## Theorem 4.1 — Positive-coefficient Euler-product logarithmic wall

Within the standard one-target isolation architecture based on:

1. the nonnegative Dirichlet coefficients of $-\zeta'/\zeta$ ;
2. a nonnegative trigonometric polynomial with nonnegative cosine coefficients; and
3. discarding all non-target zero contributions by sign,

the method can exclude zeros only at horizontal distance

$$
\boxed{
1-\beta
=
O\left(
\frac1{\log|\gamma|}
\right).
}
$$

It cannot by itself create a fixed zero-free strip.

Create:

```text
O-RH-139
POSITIVE_COEFFICIENT_EULER_PRODUCT_ZERO_DROPPING_HAS_INTRINSIC_LOGARITHMIC_DISTANCE_WALL
CERTIFIED_AS_METHOD_BARRIER
```

This is a statement about the standard positivity architecture, not about every possible use of the Euler product.

---

# 5. Seeded boundary is far outside the positivity detection scale

Under PESC $(\kappa)$, the active boundary distance is

$$
d_{\rm seed}
=
\frac{\kappa}{2},
$$

which is fixed as

$$
|\gamma|\to\infty.
$$

Therefore

$$
d_{\rm seed}
\log|\gamma|
\to\infty.
$$

The boundary zero contribution in the absolute-line positivity ledger is only

$$
O_\kappa(1),
$$

while the natural archimedean budget is

$$
\asymp
\log|\gamma|.
$$

Hence the classical Euler-product positivity mechanism is asymptotically less sensitive than the seed.

This is consistent with the modern state of the art.

Bellotti, Trudgian and Yang proved in 2026 the explicit region

$$
\boxed{
\zeta(\sigma+it)\ne0
\quad
\text{for}
\quad
\sigma
\ge
1-
\frac1{4.896\log t},
\qquad
t\ge3.
}
$$

The constant is substantially improved, but the asymptotic distance scale remains

$$
1/\log t.
$$

Thus modern refinements of this positivity family improve constants inside the same logarithmic geometry rather than supplying a fixed-strip bootstrap.

---

# 6. Why higher logarithmic derivatives do not repair the wall

Define

$$
\boxed{
F_m(s)
=
(-1)^m
\frac{d^m}{ds^m}
F(s).
}
$$

For

$$
\Re s>1,
$$

$$
\boxed{
F_m(s)
=
\sum_{n\ge1}
\frac{
\Lambda(n)(\log n)^m
}{
n^s
},
}
$$

so the Dirichlet coefficients remain nonnegative.

Near a zero $\rho$,

$$
F_m(s)
$$

contains the amplified pole

$$
\boxed{
-\frac{
m!
}{
(s-\rho)^{m+1}
}.
}
$$

This looks promising because the target zero pole becomes high order.

However, the zero-side sign structure changes.

For

$$
s-\rho
=
a+ib,
\qquad
a>0,
$$

$$
\boxed{
\Re
\frac1{(a+ib)^{m+1}}
=
\frac{
\cos
\left(
(m+1)\arctan(b/a)
\right)
}{
(a^2+b^2)^{(m+1)/2}
}.
}
$$

When

$$
m=0,
$$

the cosine is positive for every real $b$.

When

$$
m\ge1,
$$

the cosine changes sign as $b/a$ varies.

For example, take

$$
\arctan(b/a)
=
\frac{\pi}{m+2}.
$$

Then

$$
\cos
\left(
\frac{(m+1)\pi}{m+2}
\right)
<0.
$$

Thus:

## Theorem 6.1 — Higher-derivative zero-side sign-loss theorem

For every

$$
m\ge1,
$$

the real zero kernel associated with $F_m$ is not one-signed in the half-plane to the right of the zeros.

Therefore the classical step

```text
keep the target zero
drop all other zero contributions by sign
```

is no longer valid.

Create:

```text
O-RH-140
HIGHER_LOG_DERIVATIVE_POLE_AMPLIFICATION_DESTROYS_ZERO_SIDE_ONE_SIGN_STRUCTURE
CERTIFIED
```

Higher derivatives amplify the target pole but simultaneously remove the positivity mechanism needed to isolate it.

---

# 7. Relation to Turan detectors

One can attempt to recover target isolation from higher derivatives using Turan power-sum selection.

That is exactly the architecture audited in Paper 57.

The result was:

```text
target isolation is recovered,
but at a fixed distance-exponent loss C,
and the classical detector cannot amplify the seed when C>2.
```

Thus the two routes fit together:

```text
m = 0:
one-sign zero kernel,
but logarithmic-distance wall.

m >= 1:
strong pole amplification,
but zero-side sign is lost.

Turan recovery:
restores target sensitivity,
but pays a non-amplifying detector constant.
```

There is no missing free derivative trick between Papers 57 and 58.

---

# 8. Raw prime-measure positivity is boundary-blind

Let

$$
H=N^\alpha
$$

and

$$
U_H(x)
=
\psi(x+H)-\psi(x)-H.
$$

Since $\Lambda(n)\ge0$,

$$
\boxed{
\psi(x+H)-\psi(x)
\ge0.
}
$$

Equivalently,

$$
U_H(x)\ge-H.
$$

A boundary zero under PESC $(\kappa)$ contributes at scale

$$
\boxed{
|U_H(x)|
\asymp
H N^{-\kappa/2}
}
$$

in the critical model.

Since

$$
N^{-\kappa/2}
=o(1),
$$

$$
HN^{-\kappa/2}
\ll
H.
$$

Therefore the positivity lower bound

$$
U_H(x)\ge-H
$$

is compatible with the entire boundary-mode oscillation.

Create:

```text
O-RH-141
RAW_PRIME_MEASURE_POSITIVITY_IS_BLIND_TO_SEEDED_BOUNDARY_MODE
CERTIFIED_AS_SCALE_BARRIER
```

Prime positivity controls order-one relative negativity.

The required strip amplifier lives at a vanishing relative scale.

---

# 9. Positivity of the xi logarithmic derivative does not give global exclusion

The completed zeta function satisfies

$$
\boxed{
\frac{\xi'}{\xi}(s)
=
\sum_\rho
\frac1{s-\rho}
}
$$

in the standard paired sense.

If

$$
\Re s>\beta_*,
$$

every individual Poisson kernel has positive real part, so

$$
\Re
\frac{\xi'}{\xi}(s)
>0.
$$

This is simply positivity to the right of the complete zero set.

It contains no mechanism for moving $\beta_*$.

Recent work by Grigutis and Turcinskas studies positivity of

$$
\Re
\xi'/\xi
$$

near the critical line. Their 2026 analysis explicitly considers hypothetical off-critical zeros and finds that positivity may persist away from relatively small neighborhoods of those zeros.

This is external evidence for the internal conclusion:

```text
xi-log-derivative positivity
is compatible with off-critical zeros
and is not itself a global strip-gap theorem.
```

---

# 10. Heath-Brown exact recoupling is unchanged by seeding

Paper 47 certified the exact cross- $j$ recombination of the Heath-Brown identity.

After all $j$ -levels are retained before squaring and the inherited output range is respected,

$$
\boxed{
\sum_j
c_j H_j
=
\Lambda
}
$$

on the relevant root range.

The translated lag operator is linear.

Therefore, if

$$
X_j
$$

denotes the lag vector of component $H_j$,

$$
\boxed{
X_\Lambda
=
\sum_j
c_jX_j.
}
$$

The seed PESC exponent does not change this identity.

It only changes the scale against which the component and joint estimates are judged.

---

# 11. Componentwise estimates cannot create a joint fixed power for free

Assume there are only

$$
N^{o(1)}
$$

effective $j$ -levels / dyadic component cells after the fixed Heath-Brown order and dyadic partition are accounted for.

Suppose every component is controlled only at the seed lag scale:

$$
\boxed{
\|X_j\|_2^2
\ll
NH^2N^{-\kappa+o(1)}.
}
$$

Then triangle inequality gives

$$
\begin{aligned}
\|X_\Lambda\|_2
&\le
\sum_j
|c_j|
\|X_j\|_2
\\
&\ll
N^{o(1)}
\left(
NH^2N^{-\kappa}
\right)^{1/2}.
\end{aligned}
$$

Hence

$$
\boxed{
\|X_\Lambda\|_2^2
\ll
NH^2N^{-\kappa+o(1)}.
}
$$

No fixed improvement occurs.

Therefore:

## Theorem 11.1 — Seed-scale componentwise Heath-Brown no-amplification theorem

A finite or $N^{o(1)}$ Heath-Brown decomposition whose components are controlled only through separate seed-scale norm bounds cannot yield a strict MLEPG exponent

$$
\delta>\kappa.
$$

Create:

```text
O-RH-142
COMPONENTWISE_HEATH_BROWN_SEED_SCALE_BOUNDS_CANNOT_CREATE_FIXED_POWER_AMPLIFICATION
CERTIFIED
```

This is independent of the detailed form of the component bounds.

---

# 12. The exact missing Heath-Brown theorem is joint

Expand

$$
\boxed{
\|X_\Lambda\|_2^2
=
\sum_{j,k}
c_j
\overline{c_k}
\langle
X_j,X_k
\rangle.
}
$$

A strict improvement at the component natural scale would follow from a genuinely joint inequality such as

$$
\boxed{
\left\|
\sum_j
c_jX_j
\right\|_2^2
\le
N^{-\eta}
\sum_j
|c_j|^2
\|X_j\|_2^2
}
$$

for some fixed

$$
\eta>0,
$$

or from another estimate of equivalent fixed-power strength.

This is a covariance theorem.

It is not contained in the Heath-Brown identity.

Paper 47 already proved that the exact alternating signs restore the original $\Lambda$ object rather than automatically creating a power saving.

Papers 43–46 further certified that:

- isolated Liouville components;
- Ramaré extraction;
- prime-harmonic leverage;
- structured-weight $L^2$ smallness; and
- factor-by-factor determinant geometry

do not supply the missing fixed power.

Thus SG4B is not "apply Heath-Brown again."

It is:

```text
prove a new seeded joint cross-j covariance theorem.
```

No such theorem is certified.

---

# 13. Boundary-mode interpretation of the joint covariance problem

Suppose the root error contains a seed-boundary mode at exponent

$$
\beta
=
1-\frac{\kappa}{2}.
$$

Paper 55 showed that its lag energy is

$$
NH^2N^{-\kappa}
$$

and is concentrated on the principal Fejer arc.

Since the complete Heath-Brown sum reconstructs $\Lambda$, the component covariance matrix must reconstruct that boundary mode as well.

Therefore a fixed-power joint covariance deficit would imply that the complete reconstructed boundary mode is smaller than the seed scale.

By Papers 54–55, that is already a zero-strip improvement.

Hence:

## Corollary 13.1 — Joint covariance improvement is genuine strip-gap arithmetic

Any seeded Heath-Brown joint inequality strong enough to yield

$$
\delta>\kappa
$$

is itself a new fixed zero-strip theorem.

It cannot be justified solely by the formal alternating signs of the identity.

This is a calibration, not a circularity objection.

---

# 14. SG4A verdict: prime support and positivity

The original SG4A candidate was:

```text
PRIME_SUPPORT_AND_POSITIVITY_VERSUS_SMOOTH_BOUNDARY_MODE
```

Verdict:

```text
STANDARD POSITIVITY ROUTE CLOSED AS NON-AMPLIFYING.
```

Reasons:

1. raw prime-measure positivity only controls the relative scale $1$ ;
2. the boundary signal has relative scale $N^{-\kappa/2}$ ;
3. Euler-product positivity in $\Re s>1$ has only logarithmic zero-distance resolution;
4. near-critical xi positivity is compatible with hypothetical off-critical zeros away from local neighborhoods.

A new positivity theorem would need quantitative information beyond coefficient nonnegativity.

---

# 15. SG4B verdict: seeded Heath-Brown bilinear route

The original SG4B candidate was:

```text
SEEDED_HEATH_BROWN_BILINEAR_MAJOR_ARC_INCOMPATIBILITY
```

Verdict:

```text
EXISTING COMPONENTWISE ROUTE CLOSED.
```

The missing theorem is explicitly joint:

$$
\boxed{
\text{fixed-power cross-j covariance deficit}.
}
$$

The seed does not manufacture it.

Record:

```text
SG4B-JOINT
OPEN
```

as a possible but high-cost arithmetic subfrontier.

---

# 16. SG4C verdict: nonlinear Euler-product boundary detector

The original SG4C candidate was:

```text
NONLINEAR_EULER_PRODUCT_BOUNDARY_MODE_DETECTOR
```

The standard candidates are exhausted:

```text
first log derivative:
logarithmic-distance wall

higher log derivatives:
zero-side sign loss

Turan derivative selection:
Paper 57 detector saturation

xi log-derivative positivity:
compatible with hypothetical off-line zeros
```

Therefore close the standard SG4C architecture as:

```text
CLOSED_AS_NO_STANDARD_EULER_POSITIVITY_OR_DERIVATIVE_ROUTE_CROSSES_THE_SEEDED_FIXED_BOUNDARY
```

A genuinely nonlinear Euler-product theorem remains logically possible but would require new information not contained in ordinary coefficient positivity.

---

# 17. SG4D status

SG4D was:

```text
MULTISCALE_PRIME_FACTOR_COHERENCE_BREAKING
```

No certified theorem currently separates the von Mangoldt sequence from the critical boundary mode at a fixed-power level.

This remains the only genuinely open structural-arithmetic direction inside SG4.

However, it is not yet as concrete as F-RH-017.

Therefore Campaign 46 should not create a new canonical frontier merely to rename the gap.

The preferred direct target remains:

```text
F-RH-017
SEEDED_SUPERCRITICAL_SHRINKING_THRESHOLD_EXCEPTIONAL_SET
```

because it has explicit parameters and a certified amplification map.

The secondary detector target remains:

```text
F-RH-018
SEEDED_TURAN_GALLAGHER_DETECTOR_EXCESS_POWER
```

but is quantitatively more expensive.

---

# 18. Current external calibration

## 18.1. 2026 Heath-Brown-inspired zero-free region

Chiara Bellotti, Tim Trudgian and Andrew Yang,
*Zero-free regions inspired by work of Heath-Brown*,
arXiv:2603.21490.

They prove

$$
\zeta(\sigma+it)\ne0
$$

for

$$
t\ge3,
\qquad
\sigma
\ge
1-\frac1{4.896\log t}.
$$

The result substantially improves the constant in the classical logarithmic region but does not alter its $1/\log t$ shape.

URL:

https://arxiv.org/abs/2603.21490

## 18.2. Positivity of the xi log derivative

Andrius Grigutis and Lukas Turcinskas,
*Note on the positivity of the real part of the log-derivative of the Riemann xi-function near the critical line*,
Lithuanian Mathematical Journal, 2026.

The paper studies positivity near the critical line and explicitly considers scenarios with hypothetical off-critical zeros. Positivity can persist away from local neighborhoods of such zeros.

URL:

https://arxiv.org/abs/2509.18963

These results are used only as calibration of method scope.

---

# 19. Campaign 46 structural status

After Papers 56–58:

```text
SG1
principal-arc standard structure:
CLOSED
arithmetic suppression:
OPEN

SG2
seeded shrinking-threshold bridge:
CERTIFIED
F-RH-017:
OPEN

SG3
standard Turan-Gallagher / Mellin detector:
CLOSED AS NON-AMPLIFYING
F-RH-018:
OPEN SECONDARY

SG4A
standard positivity:
CLOSED AS NON-AMPLIFYING

SG4B
componentwise Heath-Brown:
CLOSED
joint covariance theorem:
OPEN HIGH-COST

SG4C
standard Euler-product derivative positivity:
CLOSED

SG4D
new nonlinear prime coherence:
OPEN / UNSPECIFIED
```

The campaign has reached the point where further formal architecture is unlikely to reduce the gap.

---

# 20. State transition

Advance the candidate state from

$$
v1.48
$$

to

$$
v1.49.
$$

Add:

```text
O-RH-139
POSITIVE_COEFFICIENT_EULER_PRODUCT_ZERO_DROPPING_HAS_INTRINSIC_LOGARITHMIC_DISTANCE_WALL
CERTIFIED_AS_METHOD_BARRIER
```

Add:

```text
O-RH-140
HIGHER_LOG_DERIVATIVE_POLE_AMPLIFICATION_DESTROYS_ZERO_SIDE_ONE_SIGN_STRUCTURE
CERTIFIED
```

Add:

```text
O-RH-141
RAW_PRIME_MEASURE_POSITIVITY_IS_BLIND_TO_SEEDED_BOUNDARY_MODE
CERTIFIED_AS_SCALE_BARRIER
```

Add:

```text
O-RH-142
COMPONENTWISE_HEATH_BROWN_SEED_SCALE_BOUNDS_CANNOT_CREATE_FIXED_POWER_AMPLIFICATION
CERTIFIED
```

No new root theorem and no RH certificate is created.

---

# 21. Recommended next action

The most economical remaining theorem is still F-RH-017.

Choose

$$
H=N^{1-\tau}
$$

with fixed small $\tau>0$.

Prove

$$
\boxed{
\#\left\{
x\in[N,2N]:
|\psi(x+H)-\psi(x)-H|
>
HN^{-\nu}
\right\}
\ll
N^{1-c}
}
$$

with

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>2\tau.
}
$$

Paper 56 then converts this directly into

$$
\operatorname{PESC}(\kappa+\eta)
$$

for an explicit fixed $\eta>0$.

This target is weaker and more concrete than:

- full natural Selberg variance;
- a large-constant Turan detector excess;
- a new joint Heath-Brown covariance theorem; or
- an unspecified nonlinear Euler-product principle.

The next mathematical campaign should therefore attack F-RH-017 directly rather than generating another representation.

---

# 22. Conclusion

The standard positivity idea has now been separated into its real strengths and its real limits.

Positive von Mangoldt coefficients are powerful enough to prove nonvanishing near $\Re s=1$.

They are not fine enough to see a seeded boundary at fixed distance.

Higher derivatives increase pole sensitivity but lose one-sign zero geometry.

Raw positivity of prime counts is blind to a vanishing relative boundary oscillation.

Heath-Brown factorization exposes arithmetic structure but, after exact cross- $j$ recoupling, does not create a fixed covariance deficit by formal algebra alone.

Thus Campaign 46 has exhausted its standard structural mechanisms.

The missing theorem is no longer hidden.

It is a genuinely new prime-side excess estimate beyond the critical seed scale.

Among the currently certified formulations, F-RH-017 remains the cheapest direct target.
