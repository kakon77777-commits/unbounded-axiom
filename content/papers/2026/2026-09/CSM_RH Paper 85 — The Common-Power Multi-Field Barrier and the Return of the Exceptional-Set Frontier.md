# CSM_RH Paper 85

## The Common-Power Multi-Field Barrier and the Return of the Exceptional-Set Frontier

**Project:** CSM_RH  
**Paper:** 85  
**Version:** v0.1  
**Date:** 2026-09-09  
**Branch:** `MIXED_ARITHMETIC_STATE_SCREENING`  
**Entry state:** v1.75 / Paper 84 v0.1  
**Status:** FINITE ZETA-DERIVED MULTI-FIELD HOMOGENEITY CLASSIFIED / FIXED ANALYTIC OBSERVABLES HORIZONTALLY DEGREE-NEUTRAL / FIRST GENUINE ESCAPE IS SCALE-ADAPTIVE NONANALYTIC THRESHOLDING / CANONICAL RETURN TO F-RH-017-v3  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Papers 82–84 progressively ruled out:

- finite-degree polynomial statistics of one linear prime-error field;
- periodic / finite-sieve mixed factor states;
- the prime-error / Mertens cross spectrum as a standalone horizontal amplifier.

The repeated mechanism was the same.

At a zeta zero

$$
\rho=\beta+i\gamma,
$$

every linear field under consideration carried a response equal to a zero-dependent coefficient times a common horizontal power.

The present paper formalizes this phenomenon.

A normalized arithmetic field

$$
Y_j(X)
$$

belongs to the **common-defect class** if, for every fixed hypothetical rightmost zero $\rho$, its boundary response has the form

$$
\boxed{
Y_j(X)
=
c_j(\rho)
X^{-(1-\beta)}
(\log X)^{m_j}
e^{i\gamma\log X}
+
\text{conjugate / lower terms}.
}
$$

More generally, if the field is sampled at the deterministic scale

$$
X^{\theta_j},
$$

its response is

$$
\boxed{
Y_j(X^{\theta_j})
=
c_j(\rho)
X^{-\theta_j(1-\beta)}
(\log X)^{m_j}
e^{i\theta_j\gamma\log X}
+
\cdots.
}
$$

This class includes, after their natural normalization:

- the prime-number-theorem error;
- the Mertens field;
- fixed derivatives in $\log X$ ;
- fixed antiderivatives;
- compact Mellin smoothings;
- finite scale differences;
- finite collections of zeta-derived linear error fields.

The coefficient $c_j(\rho)$ may contain:

- powers of $\rho$ ;
- $1/\zeta'(\rho)$ ;
- higher zero derivatives;
- finite Euler factors;
- test-transform values.

These alter the vertical spectral data but not the horizontal defect slope.

Let a monomial use the fields with multiplicities

$$
n_j\ge0.
$$

Its weighted copy degree is

$$
\boxed{
W
=
\sum_j
n_j\theta_j.
}
$$

At a boundary zero its horizontal size is

$$
\boxed{
X^{-W(1-\beta)}
(\log X)^{O(1)}.
}
$$

Therefore a fixed-power upper

$$
\boxed{
|\mathcal O(X)|
\ll
X^{-s+o(1)}
}
$$

for a nonzero weighted-homogeneous mixed observable of weight $W$ forces

$$
\boxed{
\beta_*
\le
1-\frac{s}{W}.
}
$$

Equivalently, it yields PESC exponent

$$
\boxed{
\kappa'
<
\frac{2s}{W}.
}
$$

The copy weight multiplies the available arithmetic exponent and the boundary threshold by the same factor.

There is no free horizontal amplification from finite multi-field homogeneity.

The result extends from homogeneous polynomials to arbitrary fixed polynomials.

For a polynomial observable, let

$$
W_*
$$

be the smallest weighted degree whose boundary polynomial does not vanish identically on the rightmost-zero response.

Then

$$
\boxed{
\mathcal O(X)
=
X^{-W_*(1-\beta)}
(\log X)^{O(1)}
\mathcal A(\log X)
+
\text{smaller powers},
}
$$

where $\mathcal A$ is an almost-periodic boundary coefficient.

If $\mathcal A$ is not identically zero, its logarithmic-scale mean square is positive.

Thus the same zero-strip conversion holds with $W_*$.

The theorem extends again to any **fixed analytic observable** near the origin.

Because every normalized field tends to zero when $\beta<1$, the Taylor series of the analytic observable has a first nonvanishing weighted homogeneous term.

That term determines the horizontal exponent.

Hence:

```text
FINITE ZETA-DERIVED LINEAR FIELDS
+ FIXED ANALYTIC COMBINATION
=
COMMON-POWER DEGREE NEUTRALITY.
```

Several apparently more flexible operations remain inside this class.

### Log-scale differentiation

If

$$
D=X\frac{d}{dX},
$$

then

$$
D
\left(
X^{-\delta}
e^{i\gamma\log X}
\right)
=
(-\delta+i\gamma)
X^{-\delta}
e^{i\gamma\log X}.
$$

The power is unchanged.

### Fixed scale differences

For fixed $c>0$,

$$
Y(cX)-Y(X)
$$

multiplies a boundary mode by

$$
c^{-\delta+i\gamma}-1.
$$

The power is unchanged unless the transfer coefficient vanishes, in which case the mode is deleted rather than improved.

### Antiderivatives and natural rescaling

Integrating a field shifts both its natural scale and its zero response by the same power of $X$.

After normalization, the defect remains

$$
X^{-(1-\beta)}.
$$

### Compact Mellin smoothing

A fixed Mellin kernel multiplies the zero response by its transform evaluated at $\rho$.

Again only the coefficient changes.

### Ratios

A ratio may cancel the common power

$$
X^{-(1-\beta)}.
$$

But then it also cancels the horizontal location information.

The result can retain residue ratios such as

$$
1/\zeta'(\rho),
$$

but it does not by itself force $\beta$ to move.

Thus ratios are useful for vertical geometry, not for a standalone horizontal exponent amplifier.

The paper then identifies the first real escape from the analytic common-power class.

Take a normalized field with boundary amplitude

$$
|Y(X)|
\asymp
X^{-\delta},
\qquad
\delta=1-\beta.
$$

A fixed threshold

$$
\mathbf1_{\{|Y|>c\}}
$$

eventually becomes blind because $Y(X)\to0$.

But a **scale-adaptive threshold**

$$
\boxed{
\mathbf1_{\{
|Y(X)|
>
X^{-d}
\}}
}
$$

behaves differently.

If

$$
\delta<d,
$$

then the hypothetical boundary mode exceeds the threshold on a positive proportion of logarithmic scales, modulo its phase zeros.

Therefore an exceptional-set theorem which proves that the exceedance set is too small can exclude the zero.

This is exactly the geometry of the canonical short-interval exceptional-set frontier.

In the CSM_RH notation, the surviving root route is again:

```text
F-RH-017-v3
```

with the strict gate

$$
\boxed{
\nu>d,
\qquad
c>\min(d,\tau),
}
$$

where

$$
d=\frac{\kappa}{2}.
$$

Thus a long sequence of linear, polynomial, nonlinear and mixed-state screens returns to the same point:

> the first operation which genuinely escapes common-power homogeneity is a nonanalytic, scale-adaptive threshold, and its quantitative form is the exceptional-set problem already isolated in Papers 60–61.

The result is a structural consolidation rather than a proof of RH.

It says that a broad finite-dimensional class of zeta-derived constructions can now be rejected before detailed arithmetic development.

A future route must do at least one of the following:

1. prove the F-RH-017-v3 exceptional-set excess directly;
2. use a genuinely dynamic / adaptive arithmetic state whose threshold is not a fixed analytic function of finitely many zeta-derived linear fields;
3. introduce an ordinary-prime invariant whose boundary response has a different horizontal slope, not merely a different residue.

No RH theorem is claimed.

---

# 1. Common-defect linear fields

Let

$$
\delta=1-\beta.
$$

A normalized field $Y_j$ is called $\rho$ -common-defect if

$$
\boxed{
Y_j(X)
=
X^{-\delta}
(\log X)^{m_j}
\left(
c_j(\rho)
e^{i\gamma\log X}
+
\overline{c_j(\rho)}
e^{-i\gamma\log X}
\right)
+
o_{\rm pow}
\left(
X^{-\delta}
\right).
}
$$

The exact logarithmic polynomial is irrelevant at fixed-power resolution.

---

# 2. Deterministic scale weights

Sample field $j$ at

$$
X^{\theta_j},
\qquad
\theta_j>0.
$$

Then

$$
\boxed{
Y_j(X^{\theta_j})
=
X^{-\theta_j\delta}
(\log X)^{m_j}
\left(
c_{j,\theta_j}(\rho)
e^{i\theta_j\gamma\log X}
+
\text{conjugate}
\right)
+
\cdots.
}
$$

The scale weight $\theta_j$ therefore multiplies both:

- the horizontal decay;
- the logarithmic frequency.

---

# 3. Weighted monomial law

Consider

$$
\boxed{
\mathcal M(X)
=
\prod_{j=1}^J
Y_j(X^{\theta_j})^{n_j}
}
$$

with nonnegative integer multiplicities $n_j$.

Define

$$
\boxed{
W
=
\sum_j n_j\theta_j.
}
$$

Every term in the boundary expansion of $\mathcal M$ has horizontal magnitude

$$
\boxed{
X^{-W\delta}
(\log X)^{O(1)}.
}
$$

Create:

```text
B-RH-156
A_WEIGHTED_MONOMIAL_OF_COMMON_DEFECT_FIELDS_HAS_HORIZONTAL_BOUNDARY_EXPONENT_W_TIMES_ONE_MINUS_BETA
CERTIFIED
```

---

# 4. Homogeneous mixed-field zero-strip map

Suppose a weighted-homogeneous observable of weight $W$ has a nonzero boundary response and satisfies

$$
|\mathcal O(X)|
\ll
X^{-s+o(1)}.
$$

A hypothetical zero with

$$
\delta<\frac{s}{W}
$$

would force a larger boundary power along an unbounded logarithmic-scale set.

Therefore:

## Theorem 4.1 — Common-power homogeneous map

$$
\boxed{
\beta_*
\le
1-\frac{s}{W}.
}
$$

Equivalently,

$$
\boxed{
\kappa'
<
\frac{2s}{W}.
}
$$

Create:

```text
B-RH-157
FINITE_HOMOGENEOUS_MULTI_FIELD_STATISTICS_DIVIDE_THEIR_POWER_SAVING_BY_TOTAL_COPY_WEIGHT
CERTIFIED
```

---

# 5. General polynomial observables

Let

$$
\Phi
$$

be a fixed polynomial in finitely many fields and conjugates.

Substitute the rightmost-zero boundary expansions.

Group the resulting terms by weighted degree.

Let

$$
W_*
$$

be the smallest weight for which the boundary coefficient does not vanish identically.

Then

$$
\boxed{
\Phi(Y(X))
=
X^{-W_*\delta}
(\log X)^{O(1)}
A(\log X)
+
o_{\rm pow}
\left(
X^{-W_*\delta}
\right),
}
$$

where $A$ is almost periodic.

If $A\not\equiv0$, Besicovitch Parseval gives

$$
\boxed{
\mathbb M_t
|A(t)|^2
>0.
}
$$

Therefore an upper saving $s$ forces

$$
\boxed{
\beta_*
\le
1-\frac{s}{W_*}.
}
$$

Create:

```text
B-RH-158
THE_FIRST_NONVANISHING_WEIGHTED_DEGREE_OF_A_FINITE_POLYNOMIAL_OBSERVABLE_CONTROLS_ITS_ENTIRE_HORIZONTAL_ZERO_FORCING
CERTIFIED
```

---

# 6. Fixed analytic observables

Let $\Phi$ be analytic in a neighborhood of the origin.

Because every normalized common-defect field tends to zero,

$$
Y_j(X)\to0.
$$

Expand

$$
\Phi
=
\Phi(0)
+
P_1
+
P_2
+\cdots,
$$

where $P_m$ are homogeneous Taylor components.

After removing the constant main, let the first nonzero boundary Taylor component have weighted degree $W_*$.

Then exactly the same argument gives:

## Theorem 6.1 — Analytic-observable neutrality

$$
\boxed{
\text{fixed analytic finite-field observable}
\Longrightarrow
\text{horizontal exponent }W_*(1-\beta).
}
$$

Create:

```text
O-RH-185
FIXED_ANALYTIC_NONLINEARIZATION_OF_FINITELY_MANY_COMMON_DEFECT_FIELDS_DOES_NOT_CREATE_A_NEW_HORIZONTAL_SLOPE
CERTIFIED
```

---

# 7. Log derivatives preserve the slope

Let

$$
Y(X)
=
X^{-\delta}
e^{i\gamma\log X}.
$$

Then

$$
\boxed{
X\frac{d}{dX}Y(X)
=
(-\delta+i\gamma)Y(X).
}
$$

Repeated log derivatives multiply by powers of

$$
-\delta+i\gamma
$$

and do not change $X^{-\delta}$.

Thus derivatives add vertical data but no new horizontal exponent.

---

# 8. Fixed scale differences preserve the slope

For fixed $c>0$,

$$
\boxed{
Y(cX)-Y(X)
=
\left(
c^{-\delta+i\gamma}-1
\right)
Y(X).
}
$$

If the coefficient is nonzero, the slope is unchanged.

If it vanishes, that mode is annihilated and ceases to be a universal root detector.

Create:

```text
O-RH-186
FIXED_SCALE_DIFFERENCES_EITHER_PRESERVE_THE_COMMON_HORIZONTAL_SLOPE_OR_DELETE_THE_BOUNDARY_MODE
CERTIFIED
```

---

# 9. Mellin smoothing and antiderivatives

A fixed compact Mellin smoothing has boundary response

$$
\widehat K(\rho)
X^\rho.
$$

The transfer coefficient $\widehat K(\rho)$ changes the amplitude only.

An antiderivative of $X^\rho$ is

$$
\frac{X^{\rho+1}}{\rho+1},
$$

while its natural deterministic scale gains the same factor $X$.

Thus after normalization the defect is still

$$
X^{-(1-\beta)}.
$$

The same holds for any fixed finite number of antiderivatives.

---

# 10. Ratios remove horizontal information

Suppose two normalized fields have the same boundary power:

$$
Y_1
\sim
c_1(\rho)X^{-\delta},
$$

$$
Y_2
\sim
c_2(\rho)X^{-\delta}.
$$

Then formally

$$
\frac{Y_1}{Y_2}
\sim
\frac{c_1(\rho)}{c_2(\rho)}.
$$

The power $X^{-\delta}$ is gone.

The ratio may expose:

- $\zeta'(\rho)$ ;
- finite Euler factors;
- phase relations.

But a bound on the ratio alone does not locate $\beta$.

Moreover an arithmetic proof requires denominator nonvanishing or lower control, which can itself contain root-level information.

Thus ratio normalization is classified as a vertical-data operation, not a standalone horizontal amplifier.

---

# 11. Single-boundary-pair sufficiency for screening

A universal RH root detector must exclude the possibility that the rightmost spectrum consists only of

$$
\Theta\pm i\gamma.
$$

For this model every common-defect field is a finite linear combination of

$$
X^{-\delta}
e^{\pm i\theta_j\gamma\log X}
$$

times constant residues and logarithms.

Theorems 3–6 therefore classify every fixed finite analytic observable on this minimal failure model.

No assumptions about additive relations among many zero ordinates are needed.

---

# 12. Why a fixed threshold is blind

Let

$$
|Y(X)|
\asymp
X^{-\delta},
\qquad
\delta>0.
$$

For any fixed $c>0$,

$$
\boxed{
\mathbf1_{\{|Y(X)|>c\}}
=0
}
$$

for all sufficiently large $X$.

Thus a fixed nonanalytic threshold is not useful.

---

# 13. Scale-adaptive thresholds escape homogeneity

Now take

$$
\boxed{
\mathcal I_d(X)
=
\mathbf1_{\{
|Y(X)|
>
X^{-d}
\}}.
}
$$

If

$$
\delta<d,
$$

then

$$
X^{d-\delta}\to\infty.
$$

Away from the zero set of the oscillatory phase, the boundary mode eventually exceeds the threshold.

For a single sinusoidal boundary pair, the exceedance occupies a positive proportion of logarithmic scales.

Thus an upper theorem saying the exceedance set is too sparse can exclude the zero.

Create:

```text
B-RH-159
SCALE_ADAPTIVE_THRESHOLDING_CONVERTS_A_HORIZONTAL_EXPONENT_GAP_INTO_A_POSITIVE_LOG_SCALE_EXCEEDANCE_MASS
CERTIFIED_ON_THE_SINGLE_BOUNDARY_PAIR_MODEL
```

This is qualitatively different from an analytic observable.

---

# 14. Return to the exceptional-set frontier

For the short-interval prime error

$$
U_H(n)
=
\psi(n+H)-\psi(n)-H,
$$

Papers 60–61 studied exceptional sets

$$
\boxed{
\mathcal E_{\nu}
=
\left\{
n:
|U_H(n)|
>
H N^{-\nu}
\right\}.
}
$$

Under a PESC $(\kappa)$ seed, set

$$
d=\frac{\kappa}{2},
$$

and

$$
H=N^{1-\tau}.
$$

The strict amplification gate was

$$
\boxed{
\nu>d,
\qquad
c>\min(d,\tau),
}
$$

where

$$
|\mathcal E_\nu|
\ll
N^{1-c}.
$$

The scale-adaptive threshold of Section 13 is exactly this structure.

Therefore:

## Theorem 14.1 — Canonical return theorem

Within the finite zeta-derived common-power class, the first robust operation which escapes fixed analytic degree-neutrality is the scale-adaptive exceptional-set threshold already represented by F-RH-017-v3.

Create:

```text
B-RH-160
THE_FIRST_NONANALYTIC_ESCAPE_FROM_COMMON_POWER_HOMOGENEITY_RETURNS_TO_THE_CANONICAL_EXCEPTIONAL_SET_FRONTIER
CERTIFIED_AS_STRUCTURAL_IDENTIFICATION
```

---

# 15. Broader multi-field barrier

Suppose a finite family of normalized fields has, at every fixed zero $\rho$, responses of the form

$$
\boxed{
X^{-\theta_j(1-\beta)}
(\log X)^{m_j}
c_j(\rho)
e^{i\theta_j\gamma\log X}.
}
$$

Then any fixed analytic finite-dimensional construction has a first nonzero weighted degree $W_*$.

Its universal horizontal forcing is linear in

$$
W_*(1-\beta).
$$

The coefficient data may be arbitrarily rich.

It may contain:

- derivatives of $\zeta$ ;
- local Euler data;
- nonprincipal $L$ -data;
- zero multiplicity.

But unless the construction changes the horizontal scaling law itself, it does not create a new PESC exponent mechanism.

Create:

```text
O-RH-187
FINITE_COMMON_POWER_ZETA_DERIVED_MULTI_FIELD_ANALYTIC_CONSTRUCTIONS_ARE_HORIZONTALLY_DEGREE_NEUTRAL
CERTIFIED
```

---

# 16. What can still escape

The theorem does not cover all imaginable arithmetic constructions.

The surviving classes include:

## 16.1. Scale-adaptive / threshold observables

These return to exceptional-set geometry.

## 16.2. Dynamic state switching

An arithmetic state may change its rule depending on previously observed scale information.

This is not a fixed analytic function.

## 16.3. Different horizontal slopes

A genuinely new arithmetic field could have a rightmost-zero response whose normalized exponent is not proportional to

$$
1-\beta.
$$

No such ordinary-prime field has been identified in the campaign.

## 16.4. Infinite-dimensional or growing-complexity transforms

If the number of fields / polynomial degree / scale resolution grows with $X$, a fixed Taylor-order argument no longer applies automatically.

Such a route would need its own complexity-versus-power ledger.

---

# 17. Literature calibration

Akbary, Ng and Shahabi develop a general vector-valued Besicovitch almost-periodic framework for classical prime-number-theory error terms, including prime, Möbius, Liouville and related fields.

This supports treating multiple explicit-formula error fields as a common almost-periodic spectral system.

Recent work of Leong gives simultaneous explicit control of

$$
\zeta'/\zeta
$$

and

$$
1/\zeta
$$

near the classical zero-free region, illustrating that these two basic zeta-derived fields remain naturally coupled in current analytic work.

Bui's negative-moment results show that derivative-sensitive coordinates such as

$$
1/\zeta'(\rho)
$$

are substantial vertical information, but do not by themselves produce a new horizontal zero-location exponent.

---

# 18. State transition

Advance candidate state

$$
v1.75
\to
v1.76.
$$

Add:

```text
B-RH-156
A_WEIGHTED_MONOMIAL_OF_COMMON_DEFECT_FIELDS_HAS_HORIZONTAL_BOUNDARY_EXPONENT_W_TIMES_ONE_MINUS_BETA

B-RH-157
FINITE_HOMOGENEOUS_MULTI_FIELD_STATISTICS_DIVIDE_THEIR_POWER_SAVING_BY_TOTAL_COPY_WEIGHT

B-RH-158
THE_FIRST_NONVANISHING_WEIGHTED_DEGREE_OF_A_FINITE_POLYNOMIAL_OBSERVABLE_CONTROLS_ITS_ENTIRE_HORIZONTAL_ZERO_FORCING

B-RH-159
SCALE_ADAPTIVE_THRESHOLDING_CONVERTS_A_HORIZONTAL_EXPONENT_GAP_INTO_A_POSITIVE_LOG_SCALE_EXCEEDANCE_MASS

B-RH-160
THE_FIRST_NONANALYTIC_ESCAPE_FROM_COMMON_POWER_HOMOGENEITY_RETURNS_TO_THE_CANONICAL_EXCEPTIONAL_SET_FRONTIER

O-RH-185
FIXED_ANALYTIC_NONLINEARIZATION_OF_FINITELY_MANY_COMMON_DEFECT_FIELDS_DOES_NOT_CREATE_A_NEW_HORIZONTAL_SLOPE

O-RH-186
FIXED_SCALE_DIFFERENCES_EITHER_PRESERVE_THE_COMMON_HORIZONTAL_SLOPE_OR_DELETE_THE_BOUNDARY_MODE

O-RH-187
FINITE_COMMON_POWER_ZETA_DERIVED_MULTI_FIELD_ANALYTIC_CONSTRUCTIONS_ARE_HORIZONTALLY_DEGREE_NEUTRAL
```

Update:

```text
FINITE_ZETA_DERIVED_ANALYTIC_MULTI_FIELD_ROUTE
STRUCTURALLY_CLOSED_AS_COMMON_POWER_DEGREE_NEUTRAL.
```

Canonical active root remains:

```text
F-RH-017-v3
```

with F-RH-022 as the preferred ordinary-prime pair-residual formulation.

No RH certificate is created.

---

# 19. Recommended next action

Do not open another finite analytic transform family.

There are now two justified next choices.

## Choice A — Return to F-RH-017-v3

Attack the scale-adaptive exceptional-set theorem directly, now with the benefit of the full campaign's negative results.

The question becomes:

```text
Can ordinary-prime arithmetic force
an exceptional-set exponent
c > min(d,tau)
at a threshold exponent
nu > d?
```

## Choice B — Growing-complexity / dynamic observable

Permit the number of scales or states to grow with $N$.

But require a complexity ledger before any arithmetic work:

- number of states;
- total test entropy;
- scale resolution;
- boundary response;
- union / chaining loss.

Without a provable complexity advantage, the route should be rejected.

The default recommendation is Choice A.

---

# 20. Conclusion

A broad finite-dimensional family of zeta-derived constructions has now been classified.

Different fields can reveal new residues, derivatives, multiplicities and local spectral geometry.

Fixed analytic combinations can be highly nonlinear.

But if every field shares the same normalized horizontal defect slope, the first nonzero weighted degree determines the entire boundary power.

The copy degree multiplies both the hoped-for saving and the zero-forcing threshold.

The first robust escape is not another analytic transform.

It is a dynamic threshold.

That returns the campaign to the exceptional-set frontier already isolated near the beginning.
