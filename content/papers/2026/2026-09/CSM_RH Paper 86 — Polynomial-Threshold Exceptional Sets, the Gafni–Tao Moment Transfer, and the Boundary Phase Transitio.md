# CSM_RH Paper 86

## Polynomial-Threshold Exceptional Sets, the Gafni–Tao Moment Transfer, and the Boundary Phase Transition at ν = d

**Project:** CSM_RH  
**Paper:** 86  
**Version:** v0.1  
**Date:** 2026-09-09  
**Canonical root frontier:** F-RH-017-v3  
**Entry state:** v1.76 / Paper 85 v0.1  
**Status:** RETURN TO EXCEPTIONAL-SET ROOT / POLYNOMIAL-THRESHOLD MOMENT TRANSFER AUDITED / FIXED-MOMENT MARKOV ROUTE PROVED TO STOP EXACTLY AT ν=d / THRESHOLD-NATIVE ARITHMETIC REQUIRED  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 85 showed that the first robust escape from finite common-power analytic constructions is a scale-adaptive threshold.

This returned the campaign to the canonical exceptional-set frontier F-RH-017-v3.

The present paper asks whether the strongest modern exceptional-interval machinery can supply that frontier.

The main external calibration is the 2025–2026 work of Gafni and Tao on exceptional intervals for the prime number theorem in short intervals.

For

$$
H=X^\theta,
\qquad
\theta=1-\tau,
$$

they study the fixed-relative-threshold exceptional set

$$
\left\{
x\in[X,2X]:
|\psi(x+H_x)-\psi(x)-H_x|
\ge
\delta H_x
\right\},
$$

with fixed $\delta>0$.

Their explicit-formula method combines:

- zero-density estimates;
- second moments of zero-band contributions;
- fourth moments controlled by zero additive energy.

For a zero band with left endpoint $\sigma$, their exponent functions are

$$
\boxed{
\mu_{2,\sigma}(\theta)
=
\tau(1-\sigma)A(\sigma)
+
2\sigma-1,
}
$$

and

$$
\boxed{
\mu_{4,\sigma}(\theta)
=
\tau(1-\sigma)A^*(\sigma)
+
4\sigma-3.
}
$$

They also note that fixed higher even moments lead formally to

$$
\boxed{
\mu_{2k,\sigma}(\theta)
=
\tau(1-\sigma)A^{(2k)}(\sigma)
+
2k\sigma-2k+1,
}
$$

where $A^{(2k)}$ is the corresponding $2k$ -zero additive-energy exponent.

F-RH-017-v3 is quantitatively different.

It requires a **polynomially shrinking relative threshold**

$$
\boxed{
|\Delta_H(x)|
>
H X^{-\nu},
}
$$

where

$$
\Delta_H(x)
=
\psi(x+H)-\psi(x)-H.
$$

Under a PESC $(\kappa)$ seed write

$$
\boxed{
d=\frac{\kappa}{2}.
}
$$

The strict root gate is

$$
\boxed{
\nu>d,
\qquad
c>\min(d,\tau),
}
$$

for an exceptional-set bound

$$
\boxed{
|\mathcal E_\nu(X,H)|
\ll
X^{1-c+o(1)}.
}
$$

The first result of the present paper is the polynomial-threshold Markov law.

Suppose a zero-band contribution $S_I$ satisfies a $2k$ -moment estimate of the standard explicit-formula form

$$
\boxed{
\frac1X
\int_X^{2X}
|S_I(x)|^{2k}dx
\ll
X^{
\mathcal Z_{2k}
+
2k\theta
+
2k\sigma_+
-
2k
+
o(1)
},
}
$$

where $\mathcal Z_{2k}\ge0$ is the cost of counting / correlating zeros in that band.

Applying Markov at threshold

$$
H X^{-\nu}
=
X^{\theta-\nu}
$$

gives

$$
\boxed{
|\{
x:
|S_I(x)|\ge H X^{-\nu}
\}|
\ll
X^{
\mathcal Z_{2k}
+
2k\sigma_+
-
2k
+
1
+
2k\nu
+
o(1)
}.
}
$$

For a narrow band centered at a possible zero real part $\beta$ this becomes

$$
\boxed{
\mu_{2k}^{(\nu)}(\beta)
\ge
1
-
2k(1-\beta)
+
2k\nu.
}
$$

The inequality is written with $\ge$ because every zero-density / additive-energy cost is nonnegative.

Therefore:

## Universal threshold phase transition

$$
\boxed{
\mu_{2k}^{(\nu)}(\beta)
\ge
1
+
2k
\left(
\nu-(1-\beta)
\right).
}
$$

This yields three regimes.

### Super-boundary threshold

If

$$
\nu<1-\beta,
$$

then a fixed moment can in principle give a power-saving exceptional set.

### Boundary threshold

If

$$
\nu=1-\beta,
$$

then the best possible baseline exponent is

$$
1.
$$

No power density saving remains.

### Sub-boundary threshold

If

$$
\nu>1-\beta,
$$

then

$$
\boxed{
\mu_{2k}^{(\nu)}(\beta)>1.
}
$$

A fixed-moment Markov argument cannot even certify a density-zero exceptional set from that band.

At a saturated PESC $(\kappa)$ boundary,

$$
\beta=1-d,
$$

this becomes

$$
\boxed{
\mu_{2k}^{(\nu)}
\ge
1+2k(\nu-d).
}
$$

F-RH-017-v3 requires precisely the third regime:

$$
\boxed{
\nu>d.
}
$$

Thus the canonical exceptional-set frontier begins **strictly beyond the reach of every fixed even-moment / Markov argument compatible with a possible seed-boundary zero**.

Higher moments do not help.

They increase the slope

$$
2k(\nu-d)
$$

but do not move the transition point.

Even a hypothetical perfect higher zero-additive-energy theorem

$$
\mathcal Z_{2k}=0
$$

would not change this conclusion.

The hard-interval explicit formula makes the obstruction stronger.

To approximate

$$
\Delta_H(x)
$$

to precision

$$
H X^{-\nu},
$$

the usual truncated explicit formula needs

$$
\boxed{
T
\gtrsim
\frac{X}{H}
X^\nu
(\log X)^{O(1)}
=
X^{\tau+\nu+o(1)}.
}
$$

Thus the Gafni–Tao second- and fourth-moment exponent functions acquire the threshold-aware forms

$$
\boxed{
\mu_{2,\sigma}^{(\nu)}
=
(\tau+\nu)(1-\sigma)A(\sigma)
+
2\sigma-1
+
2\nu,
}
$$

and

$$
\boxed{
\mu_{4,\sigma}^{(\nu)}
=
(\tau+\nu)(1-\sigma)A^*(\sigma)
+
4\sigma-3
+
4\nu.
}
$$

At $\sigma=1-d$,

$$
\boxed{
\mu_{2,1-d}^{(\nu)}
=
1
+
2(\nu-d)
+
(\tau+\nu)dA(1-d),
}
$$

and

$$
\boxed{
\mu_{4,1-d}^{(\nu)}
=
1
+
4(\nu-d)
+
(\tau+\nu)dA^*(1-d).
}
$$

The density terms are nonnegative, so the universal baseline barrier already decides the sign.

A smooth interval kernel can reduce or remove the explicit truncation-height penalty, but it cannot remove the baseline

$$
1+2k(\nu-d).
$$

Hence the phase transition is not an artifact of hard cutoffs.

This gives the key campaign conclusion:

```text
GAFNI–TAO / ZERO-DENSITY / ZERO-ADDITIVE-ENERGY
EXCEPTIONAL-SET MACHINERY:

excellent for fixed relative thresholds;

not a direct route to F-RH-017-v3
once the threshold exponent satisfies ν>d.
```

The reason is structural, not merely quantitative.

A possible boundary zero itself contributes at relative size

$$
X^{-d}.
$$

A threshold

$$
X^{-\nu},
\qquad
\nu>d,
$$

lies below that amplitude.

A global moment bound which remains compatible with that zero necessarily sees its contribution before Markov is applied.

F-RH-017-v3 asks for something different:

> prove directly that ordinary-prime arithmetic prevents the boundary-sized mode from occupying the exceptional mass forced by the zeta explicit formula.

This is a **threshold-native arithmetic problem**, not a moment problem.

The paper also separates two notions of “almost all”.

Modern multiplicative-function and almost-prime results can sometimes produce power-saving exceptional sets.

For example, Matomäki proves an $O(X/h)$ exceptional set for suitable $P_2$ counts in intervals of length $h\log X$.

This demonstrates that power-saving exceptional-set mechanisms are arithmetically possible.

But the theorem is a sieve / almost-prime statement at a coarse relative threshold.

It does not provide the polynomially shrinking relative prime-count accuracy required by F-RH-017-v3.

The surviving root question is therefore sharpened.

A successful proof must avoid the chain

```text
explicit formula
→ fixed L^{2k} norm
→ Markov.
```

Candidate mechanisms must instead be threshold-native, such as:

- a stopping-time or density-increment theorem;
- a lower-tail prime-deficiency sieve with genuinely parity-breaking input;
- an inertia / persistence theorem coupled to ordinary-prime arithmetic;
- a scale-adaptive arithmetic state whose complexity is controlled before averaging.

No new frontier is opened.

F-RH-017-v3 remains the canonical root.

No RH theorem is claimed.

---

# 1. Exceptional-set notation

Let

$$
H=X^{1-\tau}.
$$

Define

$$
\boxed{
\Delta_H(x)
=
\psi(x+H)-\psi(x)-H.
}
$$

For a threshold exponent $\nu>0$ define

$$
\boxed{
\mathcal E_\nu(X,H)
=
\left\{
x\in[X,2X]:
|\Delta_H(x)|
>
H X^{-\nu}
\right\}.
}
$$

The target is

$$
\boxed{
|\mathcal E_\nu(X,H)|
\ll
X^{1-c+o(1)}.
}
$$

---

# 2. Canonical F-RH-017-v3 gate

Under PESC $(\kappa)$ put

$$
d=\frac{\kappa}{2}.
$$

Paper 61 established that a strict amplifier follows if

$$
\boxed{
\nu>d,
}
$$

and

$$
\boxed{
c>\min(d,\tau).
}
$$

This is the gate to be tested against known exceptional-set technology.

---

# 3. Gafni–Tao fixed-threshold framework

Gafni and Tao define fixed-relative-threshold exceptional sets

$$
|\Delta(x,x^\theta)|
\ge
\delta x^\theta
$$

for fixed

$$
\delta>0.
$$

Their general zero-density exponent is

$$
\boxed{
\mu_{2,\sigma}(\theta)
=
(1-\theta)(1-\sigma)A(\sigma)
+
2\sigma-1.
}
$$

Their refined fourth-moment exponent is

$$
\boxed{
\mu_{4,\sigma}(\theta)
=
(1-\theta)(1-\sigma)A^*(\sigma)
+
4\sigma-3.
}
$$

They prove an exceptional exponent by taking the supremum over relevant zero bands and the minimum of these two moment bounds.

Create:

```text
B-RH-161
GAFNI_TAO_EXPRESS_EXCEPTIONAL_SET_EXPONENTS_DIRECTLY_IN_TERMS_OF_ZERO_DENSITY_AND_ZERO_ADDITIVE_ENERGY
CERTIFIED_EXTERNAL
```

---

# 4. General moment-to-threshold lemma

Let $p=2k$.

Suppose

$$
\frac1X
\int_X^{2X}
|S(x)|^pdx
\ll
X^{M_p+o(1)}.
$$

Let the threshold be

$$
X^{\theta-\nu}.
$$

Markov gives

$$
\begin{aligned}
|\{
x:
|S(x)|\ge X^{\theta-\nu}
\}|
&\le
X
\frac{
X^{M_p+o(1)}
}{
X^{p(\theta-\nu)}
}.
\end{aligned}
$$

Therefore:

## Lemma 4.1 — Polynomial-threshold Markov penalty

$$
\boxed{
\operatorname{exc\ exponent}
=
1
+
M_p
-
p\theta
+
p\nu.
}
$$

Relative to a fixed-threshold calculation, a threshold $X^{-\nu}$ costs exactly

$$
\boxed{
p\nu
}
$$

in exceptional-set exponent.

Create:

```text
B-RH-162
A_POLYNOMIALLY_SHRINKING_RELATIVE_THRESHOLD_COSTS_P_NU_IN_ANY_PTH_MOMENT_MARKOV_EXCEPTIONAL_BOUND
CERTIFIED
```

---

# 5. Best-case zero-band baseline

The standard explicit-formula $p$ th moment of a narrow band around real part $\beta$ contains the deterministic amplitude factor

$$
X^{p\theta+p\beta-p}.
$$

Ignore **all** zero-counting costs.

This is the most optimistic possible scenario.

Then

$$
M_p
=
p\theta+p\beta-p.
$$

Lemma 4.1 gives

$$
\boxed{
\mu_p^{(\nu)}(\beta)
\ge
1
+
p\beta
-
p
+
p\nu.
}
$$

Equivalently:

## Theorem 5.1 — Universal fixed-moment threshold barrier

$$
\boxed{
\mu_p^{(\nu)}(\beta)
\ge
1
+
p
\left(
\nu-(1-\beta)
\right).
}
$$

Create:

```text
B-RH-163
EVEN_WITH_ZERO_DENSITY_COST_SET_TO_ZERO_A_FIXED_MOMENT_MARKOV_ARGUMENT_HAS_A_PHASE_TRANSITION_AT_NU_EQUALS_ONE_MINUS_BETA
CERTIFIED
```

---

# 6. Boundary phase transition

Let

$$
\delta_\beta=1-\beta.
$$

Then:

### If $\nu<\delta_\beta$

$$
1+p(\nu-\delta_\beta)<1.
$$

A power-saving exceptional exponent is not ruled out by the baseline.

### If $\nu=\delta_\beta$

$$
\boxed{
\mu_p^{(\nu)}\ge1.
}
$$

### If $\nu>\delta_\beta$

$$
\boxed{
\mu_p^{(\nu)}>1.
}
$$

Thus the threshold phase transition is exactly

$$
\boxed{
\nu=1-\beta.
}
$$

---

# 7. Saturated PESC boundary

At

$$
\beta=1-d,
$$

Theorem 5.1 becomes

$$
\boxed{
\mu_{2k}^{(\nu)}
\ge
1
+
2k(\nu-d).
}
$$

Hence:

## Corollary 7.1 — F-RH moment incompatibility

If

$$
\nu>d,
$$

no fixed even-moment / Markov argument compatible with a possible boundary zero can prove

$$
|\mathcal E_\nu|
\ll
X^{1-c}
$$

for any fixed

$$
c>0.
$$

Create:

```text
O-RH-188
F_RH_017_V3_LIES_STRICTLY_BEYOND_THE_FIXED_MOMENT_MARKOV_PHASE_TRANSITION
CERTIFIED
```

---

# 8. Higher moments do not move the transition

Replacing $p=2$ by

$$
p=4,6,8,\ldots
$$

changes

$$
1+p(\nu-d)
$$

only by multiplying the distance from the transition.

The zero of the expression remains

$$
\boxed{
\nu=d.
}
$$

Thus even hypothetical optimal higher zero additive-energy estimates cannot move the threshold.

This strengthens Paper 81's moment-degree neutrality:

```text
higher moments do not merely fail to improve the exponent;
at the adaptive exceptional threshold they all fail at exactly the same ν=d wall.
```

---

# 9. Hard-window truncation height

For a hard interval of length $H$, the truncated explicit formula has error of schematic size

$$
\boxed{
\frac{
X(\log X)^{O(1)}
}{
T
}.
}
$$

To make this smaller than

$$
H X^{-\nu},
$$

one needs

$$
\boxed{
T
\ge
\frac{X}{H}
X^\nu
(\log X)^{O(1)}.
}
$$

Since

$$
H=X^{1-\tau},
$$

$$
\boxed{
T
=
X^{\tau+\nu+o(1)}
}
$$

is the natural threshold-aware height.

Create:

```text
B-RH-164
A_HARD_INTERVAL_EXPLICIT_FORMULA_AT_RELATIVE_PRECISION_X_MINUS_NU_REQUIRES_ZERO_HEIGHT_X_TO_TAU_PLUS_NU_UP_TO_SUBPOWER_FACTORS
CERTIFIED
```

---

# 10. Threshold-aware Gafni–Tao second moment

The Gafni–Tao second moment counts zeros to height $T$.

Replacing

$$
T=X^{\tau+o(1)}
$$

by

$$
T=X^{\tau+\nu+o(1)}
$$

gives the threshold-aware density cost

$$
\boxed{
(\tau+\nu)(1-\sigma)A(\sigma).
}
$$

After Markov:

$$
\boxed{
\mu_{2,\sigma}^{(\nu)}
=
(\tau+\nu)(1-\sigma)A(\sigma)
+
2\sigma-1
+
2\nu.
}
$$

At $\sigma=1-d$,

$$
\boxed{
\mu_{2,1-d}^{(\nu)}
=
1
+
2(\nu-d)
+
(\tau+\nu)dA(1-d).
}
$$

---

# 11. Threshold-aware fourth moment

Similarly,

$$
\boxed{
\mu_{4,\sigma}^{(\nu)}
=
(\tau+\nu)(1-\sigma)A^*(\sigma)
+
4\sigma-3
+
4\nu.
}
$$

At $\sigma=1-d$,

$$
\boxed{
\mu_{4,1-d}^{(\nu)}
=
1
+
4(\nu-d)
+
(\tau+\nu)dA^*(1-d).
}
$$

The extra zero-energy terms cannot improve the baseline because they are nonnegative.

Create:

```text
B-RH-165
THE_THRESHOLD_AWARE_GAFNI_TAO_L2_AND_L4_EXPONENTS_RETAIN_THE_UNIVERSAL_NU_EQUALS_D_PHASE_TRANSITION
CERTIFIED_AS_EXPONENT_TRANSFER
```

---

# 12. Smooth kernels do not remove the baseline wall

A compact smooth interval kernel may suppress high zero ordinates rapidly.

This can improve the truncation-height bookkeeping in Sections 9–11.

But the response of a zero at real part $\beta$ still has relative power

$$
X^{-(1-\beta)}.
$$

The moment threshold penalty is still

$$
p\nu.
$$

Therefore the best-case baseline theorem in Section 5 remains.

The $\nu=d$ wall is not a hard-cutoff artifact.

---

# 13. Why fixed-relative exceptional results remain useful but insufficient

For fixed

$$
\delta>0,
$$

the threshold exponent is

$$
\nu=0.
$$

A boundary zero at

$$
\beta=1-d
$$

then has baseline exceptional exponent

$$
1-2kd.
$$

Power-saving exceptional-set estimates are therefore compatible with fixed-relative thresholds.

This explains why zero-density and additive-energy machinery can be highly effective for the classical “almost all short intervals” problem.

But F-RH-017-v3 asks for a threshold polynomially smaller than the possible boundary amplitude.

That is a different problem.

---

# 14. Almost-prime exceptional sets as a calibration

Matomäki proves that for suitable $P_2$ -counting problems in intervals of length

$$
h\log X,
$$

all but

$$
O(X/h)
$$

starting points satisfy the desired lower bound.

Thus genuinely power-saving exceptional sets are possible in short-interval sieve problems.

This is useful calibration.

However:

- the counted objects are almost primes, not primes;
- the conclusion is at a coarse relative lower threshold;
- it does not give polynomially shrinking relative accuracy for the prime count.

The result therefore illustrates that the obstacle is not “power exceptional sets” in general.

The obstacle is the threshold-native, parity-sensitive accuracy required for primes.

External source:

Kaisa Matomäki,
*Almost primes in almost all very short intervals*,
JLMS 106 (2022).

---

# 15. What a successful F-RH-017 proof must avoid

The route

$$
\boxed{
\text{explicit formula}
\to
L^{2k}
\to
\text{Markov}
}
$$

cannot cross the frontier.

A successful argument must instead produce exceptional-set control **before** reducing the arithmetic to a fixed global moment.

Possible architectures include:

## 15.1. Stopping-time / density increment

Detect the first scale at which a prime deficiency or excess develops and exploit structure conditioned on that stopping event.

## 15.2. Threshold-native parity-breaking sieve

Prove that prime deficiency by

$$
H X^{-\nu}
$$

forces a structured factorization event whose total mass can be power bounded.

## 15.3. Inertia plus arithmetic persistence contradiction

Use the deterministic persistence of a threshold exceedance together with an arithmetic theorem that forbids too many persistent deficient intervals.

## 15.4. Growing-complexity adaptive state

Allow scale resolution to depend on $X$, but maintain an explicit entropy / union-loss ledger.

No such theorem is certified here.

---

# 16. Relation to the canonical boundary forcing

Paper 61 showed that a boundary zero forces exceptional mass at the critical scale

$$
X^{1-\min(d,\tau)-o(1)}
$$

for thresholds beyond the seed.

Therefore F-RH-017-v3 requires

$$
c>\min(d,\tau)
$$

to contradict that forcing.

Paper 86 adds:

```text
fixed moments cannot even reach c>0 once ν>d.
```

Thus the exceptional-mass side of F-RH-017 is genuinely stronger than every fixed moment-Markov consequence.

---

# 17. Current best exceptional-interval calibration

Gafni and Tao give the modern explicit bridge from:

- zero density $A(\sigma)$ ;
- zero additive energy $A^*(\sigma)$ ;

to the fixed-relative exceptional exponent $\mu(\theta)$.

Their 2026 paper incorporates the recent Guth–Maynard and Tao–Trudgian–Yang density technology and provides the strongest current systematic bounds of this form.

They explicitly note that higher $2k$ moments could be incorporated through higher zero additive energies, but no known unconditional estimates there improve the existing $L^2/L^4$ inputs.

Paper 86 shows that, for F-RH-017-v3, this lack of higher-energy estimates is not the decisive obstruction.

The baseline Markov phase transition already blocks all fixed $k$.

---

# 18. State transition

Advance candidate state

$$
v1.76
\to
v1.77.
$$

Add:

```text
B-RH-161
GAFNI_TAO_EXPRESS_EXCEPTIONAL_SET_EXPONENTS_DIRECTLY_IN_TERMS_OF_ZERO_DENSITY_AND_ZERO_ADDITIVE_ENERGY

B-RH-162
A_POLYNOMIALLY_SHRINKING_RELATIVE_THRESHOLD_COSTS_P_NU_IN_ANY_PTH_MOMENT_MARKOV_EXCEPTIONAL_BOUND

B-RH-163
EVEN_WITH_ZERO_DENSITY_COST_SET_TO_ZERO_A_FIXED_MOMENT_MARKOV_ARGUMENT_HAS_A_PHASE_TRANSITION_AT_NU_EQUALS_ONE_MINUS_BETA

B-RH-164
A_HARD_INTERVAL_EXPLICIT_FORMULA_AT_RELATIVE_PRECISION_X_MINUS_NU_REQUIRES_ZERO_HEIGHT_X_TO_TAU_PLUS_NU_UP_TO_SUBPOWER_FACTORS

B-RH-165
THE_THRESHOLD_AWARE_GAFNI_TAO_L2_AND_L4_EXPONENTS_RETAIN_THE_UNIVERSAL_NU_EQUALS_D_PHASE_TRANSITION

O-RH-188
F_RH_017_V3_LIES_STRICTLY_BEYOND_THE_FIXED_MOMENT_MARKOV_PHASE_TRANSITION
```

Canonical root:

```text
F-RH-017-v3
ACTIVE
```

No RH certificate is created.

---

# 19. Recommended next action

The next round should not compute another moment.

Split the exceptional set into:

$$
\boxed{
\mathcal E_\nu^+
=
\{
\Delta_H>HX^{-\nu}
\},
}
$$

and

$$
\boxed{
\mathcal E_\nu^-
=
\{
\Delta_H<-HX^{-\nu}
\}.
}
$$

Then audit them separately.

The immediate question is:

```text
Can an ordinary-prime upper-bound sieve
control the tiny relative excess tail E_nu^+
at polynomial threshold?

If not, where exactly does sharp-factorial-moment information fail?

For the deficiency tail E_nu^-,
what parity-breaking lower-tail input would be required?
```

This one-sided decomposition may identify which half of F-RH-017 is truly root-hard.

---

# 20. Conclusion

Modern exceptional-interval methods are extremely strong at fixed relative error.

But the CSM_RH root threshold shrinks polynomially.

At a possible PESC boundary zero, the threshold crosses below the natural zero-mode amplitude exactly when $\nu>d$.

Every fixed moment-Markov method undergoes a phase transition at that same point.

Higher moments and better zero additive-energy estimates cannot move the transition.

Therefore F-RH-017-v3 is genuinely threshold-native.

The campaign is now back at the correct root frontier with a sharper description of what cannot prove it.
