# CSM_RH Paper 72

## Seeded MRT Pair-Correlation Audit, Fejér Frequency Localization, and the Critical $q=1$ Principal-Arc Floor

**Project:** CSM_RH  
**Paper:** 72  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Canonical root frontier:** F-RH-017-v3  
**Preferred arithmetic subfrontier:** F-RH-022 — `AVERAGED_HARDY_LITTLEWOOD_PAIR_RESIDUAL_EXCESS`  
**Status:** EXISTING AVERAGED PRIME-PAIR PROOF AUDITED / NONCENTRAL FREQUENCIES LOCALIZED / $q=1$ CENTRAL ARC REMAINS CRITICAL  
**Canonical entry state:** v1.62 / Paper 71 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 71 reduced the direct short-interval second moment to a solved local singular-series variance plus one global quantity:

$$
\mathcal R_{\rm HL}^{(2)}(N,H),
$$

the fully aggregated error of actual prime-pair correlations around the Hardy–Littlewood local prediction.

The present paper asks whether the existing averaged Hardy–Littlewood proof of Matomäki–Radziwiłł–Tao can be upgraded from arbitrary logarithmic saving to a fixed power by inserting a PESC $(\kappa)$ seed.

The answer is structurally negative.

The Matomäki–Radziwiłł–Tao argument uses:

1. the circle method;
2. major arcs with
   $$
   q\le\log^B N;
   $$
3. short additive-frequency $L^2$ estimates on the minor arcs;
4. a reduction to twisted Dirichlet-polynomial mean values;
5. Heath–Brown decomposition into Type II and Type $d_1,d_2,d_3,d_4$ components.

The difficult Type $d_3$ and Type $d_4$ estimates contain genuine polynomial margins at several internal stages. For example, a hard Type $d_3$ contribution is reduced to an error carrying an explicit factor

$$
N^{-\varepsilon/4+O(\varepsilon^2)}.
$$

Thus the final $\log^{-A}N$ formulation should not be interpreted as saying that every noncentral analytic component is intrinsically logarithmic.

However, none of those improvements resolves the root obstruction.

Let

$$
a_n=\Lambda(n)-1
$$

on a dyadic block and define

$$
\boxed{
S_0(\alpha)
=
\sum_{N<n\le2N}
a_ne(n\alpha).
}
$$

Let

$$
D_H(\alpha)
=
\sum_{h=1}^{H}e(h\alpha).
$$

The Fejér-type weight

$$
|D_H(\alpha)|^2
$$

is the natural frequency weight associated with averaging prime-pair correlations over two shifts or with the corresponding full convolution energy.

It obeys

$$
\boxed{
|D_H(\alpha)|
\le
\min
\left\{
H,\,
\frac{1}{2\|\alpha\|}
\right\}.
}
$$

This weight radically changes the importance of the rational arcs.

For a nonzero reduced rational

$$
a/q,
\qquad
2\le q\le\log^B N,
$$

and

$$
|\beta|
\le
N^{-1}\log^{B'}N,
$$

one has, for large $N$,

$$
\left\|
\frac aq+\beta
\right\|
\gg
q^{-1}.
$$

Hence

$$
\boxed{
|D_H(a/q+\beta)|
\ll q.
}
$$

The nonprincipal polylogarithmic major arcs therefore carry only polylogarithmic Fejér weight rather than the full $H$ weight.

After the Hardy–Littlewood local main terms are extracted, the standard Siegel–Walfisz major-arc approximation error

$$
O(N\log^{-A}N)
$$

contributes only

$$
N\log^{-A'}N
$$

to the weighted quadratic energy, for arbitrarily large fixed $A'$.

Relative to

$$
NH^2,
\qquad
H=N^{1-\tau},
$$

this is a fixed-power saving

$$
\boxed{
N^{-2(1-\tau)+o(1)}.
}
$$

Thus the low-conductor nonprincipal major-arc approximation errors which were a serious issue for the shifted-Möbius auxiliary route are not the root obstruction in the Fejér-weighted prime-pair aggregate.

The $q=1$ central arc is completely different.

Assume PESC $(\kappa)$ and set

$$
d=\frac{\kappa}{2}.
$$

Then

$$
A(x)
=
\psi(x)-x
\ll
x^{1-d+o(1)}.
$$

Partial summation gives, uniformly for

$$
|\beta|
\le
N^{-1}\log^B N,
$$

$$
\boxed{
|S_0(\beta)|
\ll
N^{1-d+o(1)}.
}
$$

For

$$
|\beta|\le c/N
$$

and

$$
H=o(N),
$$

$$
|D_H(\beta)|
\asymp H.
$$

Therefore the PESC seed yields only

$$
\boxed{
\int_{|\beta|\le c/N}
|S_0(\beta)|^2
|D_H(\beta)|^2
\,d\beta
\ll
NH^2N^{-2d+o(1)}
=
NH^2N^{-\kappa+o(1)}.
}
$$

This is exactly the critical F-RH-022 scale.

A smooth boundary mode

$$
a_n^{(\rho)}
\asymp
n^{-d+i\gamma}
$$

has

$$
|S_\rho(\beta)|
\asymp_\rho
N^{1-d}
$$

through a fixed positive fraction of the central interval

$$
|\beta|\le c_\rho/N.
$$

Thus the critical central-arc scale is saturated by the canonical boundary model.

Consequently:

```text
PESC fixed strip
+
existing averaged-prime-pair minor-arc machinery
```

cannot yield

$$
\xi>\kappa
$$

unless it proves new cancellation on the $q=1$ central principal arc itself.

This conclusion is stronger than saying that the Matomäki–Radziwiłł–Tao theorem currently has only logarithmic error terms. The hard Type $d_3/d_4$ minor-arc technology may be improved substantially without touching the root boundary mode.

A second elementary frequency localization reinforces this point.

By Parseval,

$$
\int_0^1|S_0(\alpha)|^2d\alpha
\ll
N\log N.
$$

On the region

$$
\|\alpha\|\ge N^{-v},
$$

$$
|D_H(\alpha)|^2
\ll
N^{2v}.
$$

Therefore

$$
\boxed{
\int_{\|\alpha\|\ge N^{-v}}
|S_0(\alpha)|^2
|D_H(\alpha)|^2d\alpha
\ll
N^{1+2v+o(1)}.
}
$$

Relative to $NH^2=N^{3-2\tau}$, this has saving exponent

$$
\boxed{
s_{\rm far}
=
2(1-\tau-v).
}
$$

Hence every frequency satisfying

$$
v<
1-\tau-\frac{\kappa}{2}
$$

is automatically supercritical:

$$
s_{\rm far}>\kappa.
$$

The possible PESC boundary obstruction is confined to the low additive-frequency band

$$
\boxed{
\|\alpha\|
\lesssim
N^{-\left(
1-\tau-\kappa/2
\right)+o(1)}.
}
$$

The central $1/N$ arc lies inside this band and already saturates the seed exponent.

Finally, a classical Selberg-integral estimate gives a useful conditional calibration. If

$$
\Theta
=
\sup_\rho\Re\rho
=
1-d
$$

and one supplements the fixed zero-free strip by the Density Hypothesis, then the standard estimate is

$$
\boxed{
J(N,\theta)
\ll
N(\theta N)^{2\Theta}
(\log N)^B.
}
$$

For

$$
H=\theta N=N^{1-\tau},
$$

this becomes

$$
\boxed{
J
\ll
NH^2
N^{-\kappa(1-\tau)+o(1)}.
}
$$

The corresponding saving exponent

$$
\boxed{
\kappa(1-\tau)
}
$$

is strictly smaller than the seed exponent $\kappa$ whenever $\tau>0$.

Thus even a fixed strip plus the classical density-level zero input does not self-amplify the seed through the Selberg integral.

The missing ingredient is a genuine pair-cancellation theorem, arithmetically represented by F-RH-022 and spectrally represented by cancellation among the low-frequency zero ensemble.

The canonical next track is therefore:

```text
PAIR5
PRINCIPAL-ARC / LOW-FREQUENCY PAIR-CANCELLATION EXCESS
```

not another improvement to the noncentral Type $d_3/d_4$ machinery.

No RH theorem is claimed.

---

# 1. Entry state

Assume

$$
\operatorname{PESC}(\kappa),
\qquad
0<\kappa<1.
$$

Set

$$
\boxed{
d=\frac{\kappa}{2}.
}
$$

Paper 71 opened F-RH-022:

$$
|\mathcal R_{\rm HL}^{(2)}(N,H)|
\ll
NH^2N^{-\xi+o(1)}
$$

with the strict amplifier requirement

$$
\boxed{
\xi>\kappa.
}
$$

The question of this paper is whether this can be obtained by inserting the seed into the existing averaged Hardy–Littlewood proof.

---

# 2. MRT proof architecture

Matomäki, Radziwiłł and Tao prove an averaged Hardy–Littlewood theorem for

$$
H\ge N^{8/33+\varepsilon}.
$$

Their circle-method decomposition uses major arcs

$$
\left|
\alpha-\frac aq
\right|
\le
\frac{\log^{B'}N}{N},
\qquad
q\le\log^B N,
$$

and minor arcs elsewhere.

The major arcs are evaluated by classical prime exponential-sum asymptotics.

The minor arcs are reduced to local additive-frequency $L^2$ estimates of the form

$$
\int_{\beta-1/H}^{\beta+1/H}
|S_f(\alpha)|^2d\alpha.
$$

A Fourier/logarithmic change of variables reduces those estimates to mean values of twisted Dirichlet polynomials.

For $\Lambda$, Heath–Brown decomposition produces:

- Type II;
- Type $d_1$ ;
- Type $d_2$ ;
- Type $d_3$ ;
- Type $d_4$.

The Type $d_3$ and $d_4$ pieces are the principal innovations responsible for lowering the shift exponent below $1/3$.

---

# 3. The logarithmic statement does not mean every inner estimate is logarithmic

The published minor-arc proposition is

$$
\int_{\text{short minor interval}}
|S_f(\alpha)|^2d\alpha
\ll
N\log^{-A}N.
$$

However, inside the Type $d_3$ proof, after Jutila's medium-interval fourth moment estimate and the averaged exponential-sum estimate, a hard contribution is bounded by a term containing

$$
\boxed{
N^{-\varepsilon/4+O(\varepsilon^2)}.
}
$$

Likewise, the Type $d_4$ treatment uses a classical exponent pair and has a genuine polynomial margin in the admissible shift range.

Therefore it is incorrect to identify the final arbitrary-log theorem with an intrinsic absence of power in every noncentral component.

Record:

```text
B-RH-104
MRT_HARD_TYPE_D3_D4_ANALYSIS_CONTAINS_INTERNAL_FIXED_POWER_MARGIN
CERTIFIED_AS_PROOF_AUDIT
```

This fact does **not** imply that the complete prime-pair theorem has a power-saving error.

---

# 4. Fejér weight associated with the pair aggregate

Let

$$
a_n=\Lambda(n)-1
$$

and

$$
S_0(\alpha)
=
\sum_{N<n\le2N}
a_ne(n\alpha).
$$

Let

$$
D_H(\alpha)
=
\sum_{h=1}^{H}e(h\alpha).
$$

The standard identity is

$$
\boxed{
|D_H(\alpha)|
=
\left|
\frac{
\sin(\pi H\alpha)
}{
\sin(\pi\alpha)
}
\right|
\le
\min
\left\{
H,\,
\frac{1}{2\|\alpha\|}
\right\}.
}
$$

The quadratic form

$$
\int_0^1
|S_0(\alpha)|^2
|D_H(\alpha)|^2d\alpha
$$

is the exact Fourier energy of the corresponding full convolution and is the natural frequency model for the triangularly aggregated pair correlations.

Only this frequency weighting is used in the barrier calculations below.

Sharp endpoint versions of the root energy require standard boundary bookkeeping; no new RH implication in this paper depends on discarding those endpoints.

---

# 5. Polylogarithmic nonprincipal major arcs are Fejér-small

Let

$$
2\le q\le\log^B N,
$$

$$
(a,q)=1,
$$

and

$$
|\beta|
\le
N^{-1}\log^{B'}N.
$$

For sufficiently large $N$,

$$
\left\|
\frac aq+\beta
\right\|
\gg
\frac1q.
$$

Therefore

$$
\boxed{
|D_H(a/q+\beta)|
\ll q.
}
$$

Suppose the major-arc prime approximation has residual

$$
E_{q,a}(\beta)
\ll
N\log^{-A}N.
$$

Then summing the residual square over all polylogarithmic nonprincipal major arcs gives

$$
\begin{aligned}
&
\sum_{2\le q\le\log^B N}
\sum_{(a,q)=1}
\int_{|\beta|\le N^{-1}\log^{B'}N}
|E_{q,a}(\beta)|^2
|D_H(a/q+\beta)|^2d\beta
\\
&\ll
\boxed{
N\log^{-A'}N
}
\end{aligned}
$$

for every prescribed fixed $A'>0$, after choosing $A$ sufficiently large.

The cross term between the local main term and $E_{q,a}$ obeys the same conclusion after enlarging $A$.

Since

$$
NH^2
=
N^{3-2\tau},
$$

the relative exponent of this error is

$$
\boxed{
2(1-\tau)+o(1).
}
$$

For the F-RH-022 amplifier range

$$
\tau<1-\kappa,
$$

this is strictly larger than $\kappa$.

Record:

```text
B-RH-105
FEJER_WEIGHT_MAKES_POLYLOG_NONPRINCIPAL_MAJOR_ARC_APPROXIMATION_ERRORS_SUPERCRITICAL
CERTIFIED
```

The local main terms themselves are not discarded; they are precisely what reconstruct the singular-series contribution already extracted in Paper 71.

---

# 6. Seeded $q=1$ principal exponential sum

Let

$$
A(x)=\psi(x)-x.
$$

PESC $(\kappa)$ gives

$$
\boxed{
A(x)
\ll
x^{1-d+o(1)}.
}
$$

By partial summation,

$$
S_0(\beta)
=
A(2N)e(2N\beta)
-
A(N)e(N\beta)
-
2\pi i\beta
\int_N^{2N}
A(t)e(t\beta)dt
+
O(\log N).
$$

Hence, uniformly for

$$
|\beta|
\le
N^{-1}\log^B N,
$$

$$
\boxed{
|S_0(\beta)|
\ll
N^{1-d+o(1)}.
}
$$

Record:

```text
B-RH-106
PESC_SEED_CONTROLS_THE_Q1_ULTRAMAJOR_PRIME_ERROR_AT_N_TO_ONE_MINUS_D
CERTIFIED
```

---

# 7. The central principal-arc critical floor

Fix a sufficiently small constant

$$
c>0.
$$

If

$$
|\beta|\le\frac cN
$$

and

$$
H=N^{1-\tau},
\qquad
\tau>0,
$$

then

$$
H|\beta|
\le
cN^{-\tau}
=o(1).
$$

Therefore

$$
\boxed{
|D_H(\beta)|
=
H(1+o(1)).
}
$$

Combining with Section 6 gives the seed-level central energy bound

$$
\boxed{
\int_{|\beta|\le c/N}
|S_0(\beta)|^2
|D_H(\beta)|^2d\beta
\ll
NH^2
N^{-2d+o(1)}.
}
$$

Since

$$
2d=\kappa,
$$

this is

$$
\boxed{
NH^2N^{-\kappa+o(1)}.
}
$$

There is no fixed excess beyond the seed exponent.

Create:

```text
O-RH-163
Q1_CENTRAL_PRINCIPAL_ARC_HAS_A_SEED_CRITICAL_ENERGY_FLOOR_AT_EXPONENT_KAPPA
CERTIFIED_AS_METHOD_BARRIER
```

The word "floor" refers to the method scale: PESC alone gives no stronger upper exponent.

---

# 8. Smooth boundary mode saturates the central scale

Let

$$
\rho=1-d+i\gamma
$$

and model the boundary coefficient density by

$$
a_n^{(\rho)}
=
n^{-d+i\gamma}
$$

up to a harmless nonzero constant.

Then

$$
S_\rho(\beta)
=
\sum_{N<n\le2N}
n^{-d+i\gamma}
e(n\beta).
$$

Rescale

$$
n=Nu,
\qquad
\beta=\frac yN.
$$

Riemann-sum approximation gives

$$
\boxed{
N^{d-1-i\gamma}
S_\rho(y/N)
\to
\int_1^2
u^{-d+i\gamma}
e(yu)\,du
}
$$

locally uniformly in $y$.

The limiting integral is nonzero at $y=0$ and hence on a sufficiently small interval

$$
|y|\le c_\rho.
$$

Therefore

$$
\boxed{
|S_\rho(\beta)|
\asymp_\rho
N^{1-d}
}
$$

on a fixed positive fraction of

$$
|\beta|\le c_\rho/N.
$$

Consequently its central weighted energy is

$$
\boxed{
\asymp_\rho
NH^2N^{-2d}
=
NH^2N^{-\kappa}.
}
$$

Thus O-RH-163 is sharp in the canonical boundary model.

---

# 9. Parseval localizes all possible supercritical difficulty to low frequency

Parseval gives

$$
\int_0^1
|S_0(\alpha)|^2d\alpha
=
\sum_{N<n\le2N}
|\Lambda(n)-1|^2
\ll
N\log N.
$$

Fix

$$
v>0.
$$

On

$$
\|\alpha\|\ge N^{-v},
$$

$$
|D_H(\alpha)|^2
\ll
N^{2v}.
$$

Therefore:

## Theorem 9.1 — Far-frequency automatic power saving

$$
\boxed{
\int_{\|\alpha\|\ge N^{-v}}
|S_0(\alpha)|^2
|D_H(\alpha)|^2d\alpha
\ll
N^{1+2v+o(1)}.
}
$$

Relative to

$$
NH^2
=
N^{3-2\tau},
$$

the saving exponent is

$$
\boxed{
s_{\rm far}
=
2(1-\tau-v).
}
$$

Thus the far-frequency sector is already stronger than the PESC seed whenever

$$
\boxed{
v<
1-\tau-d.
}
$$

Equivalently, any possible seed-critical obstruction is confined to

$$
\boxed{
\|\alpha\|
\lesssim
N^{-(1-\tau-d)+o(1)}.
}
$$

Record:

```text
B-RH-107
PARSEVAL_CONFINES_ALL_SEED_CRITICAL_PAIR_ENERGY_TO_AN_ULTRALOW_ADDITIVE_FREQUENCY_BAND
CERTIFIED
```

---

# 10. Consequence for the MRT minor-arc attack

The Matomäki–Radziwiłł–Tao proof invests its deepest work in noncentral minor arcs:

- Type $d_3$ ;
- Type $d_4$ ;
- twisted Dirichlet-polynomial mean values;
- medium-interval fourth moments;
- exponential-sum estimates.

These tools are essential for obtaining the almost-all Hardy–Littlewood theorem in the range

$$
H\ge N^{8/33+\varepsilon}.
$$

But for the seeded F-RH-022 amplifier they are not, by themselves, the decisive missing input.

Even a hypothetical theorem that made every noncentral minor-arc contribution negligible would leave the $q=1$ central arc at

$$
NH^2N^{-\kappa}.
$$

Hence:

```text
O-RH-164
PERFECT_NONCENTRAL_MRT_MINOR_ARC_CONTROL_CANNOT_AMPLIFY_WHILE_Q1_CENTRAL_ARC_REMAINS_AT_SEED_SCALE
CERTIFIED
```

This is the pair-correlation analogue of Paper 63's long-anchor barrier.

---

# 11. Conditional fixed-strip Selberg calibration

Let

$$
\Theta
=
\sup_\rho\Re\rho.
$$

Zaccagnini records the classical estimate, assuming the Density Hypothesis for simplicity,

$$
\boxed{
J(x,\theta)
\ll
x(\theta x)^{2\Theta}
(\log x)^B.
}
$$

Set

$$
\Theta=1-d
$$

and

$$
H=\theta x=x^{1-\tau}.
$$

Then

$$
\begin{aligned}
J
&\ll
xH^{2-2d}
(\log x)^B
\\
&=
\boxed{
xH^2
x^{-2d(1-\tau)+o(1)}.
}
\end{aligned}
$$

Since

$$
2d=\kappa,
$$

the fixed-strip Selberg saving exponent is

$$
\boxed{
s_{\rm strip}
=
\kappa(1-\tau).
}
$$

For every fixed

$$
\tau>0,
$$

$$
\boxed{
s_{\rm strip}<\kappa.
}
$$

Thus a fixed strip, even combined with the classical density-level input, is not a self-amplifier.

Record as conditional calibration:

```text
O-RH-165
FIXED_STRIP_PLUS_DENSITY_HYPOTHESIS_SELBerg_BOUND_HAS_SUBCRITICAL_SAVING_KAPPA_TIMES_ONE_MINUS_TAU
CONDITIONAL_METHOD_CALIBRATION
```

No Density Hypothesis is assumed anywhere else in the campaign.

---

# 12. What the existing averaged pair theorem can and cannot contribute

The existing theorem proves

$$
\sum_{N<n\le2N}
\Lambda(n)\Lambda(n+h)
=
\mathfrak S(h)N
+
O_A(N\log^{-A}N)
$$

for all but

$$
O_A(H\log^{-A}N)
$$

shifts in the established range.

This is strong enough to show that most individual pair errors are logarithmically small.

It does not improve the $q=1$ central PNT boundary mode supplied by PESC.

The seed, conversely, improves the $q=1$ global error to a fixed power but only at exactly the critical exponent.

Therefore the two inputs meet at the boundary without producing an excess.

---

# 13. Revised status of F-RH-022

F-RH-022 remains mathematically correct as a sufficient root subfrontier:

$$
|\mathcal R_{\rm HL}^{(2)}|
\ll
NH^2N^{-\xi},
\qquad
\xi>\kappa
$$

activates the Paper-54 amplifier.

But the naive strategy

```text
take the existing MRT averaged prime-pair proof
and replace its zeta zero-free input by PESC
```

is closed.

The seed only controls the principal central arc at the critical scale.

Any successful proof of F-RH-022 must add information which creates cancellation **inside the low-frequency principal sector**, not merely on the existing minor arcs.

---

# 14. New active subtrack

Open:

```text
PAIR5
PRINCIPAL_ARC_LOW_FREQUENCY_PAIR_CANCELLATION_EXCESS
```

Target form:

prove a fixed excess beyond

$$
NH^2N^{-\kappa}
$$

for the low-frequency contribution of the actual prime error after the Hardy–Littlewood local main term is extracted.

Equivalent arithmetic language:

prove fixed-power aggregate cancellation in

$$
\mathcal R_{\rm HL}^{(2)}.
$$

Equivalent spectral language:

prove pair decorrelation of the low-frequency zero ensemble beyond what follows from the location of the rightmost zero alone.

This is exactly the new information absent from the seed strip.

---

# 15. External proof audit

Matomäki–Radziwiłł–Tao's paper records:

- major arcs with denominators $q\le\log^B N$ ;
- a Siegel–Walfisz prime major-arc approximation;
- minor-arc local $L^2$ savings of arbitrary log power;
- reduction to twisted Dirichlet polynomials;
- Type II and Type $d_1,d_2,d_3,d_4$ decomposition;
- Type $d_3$ analysis using Jutila's fourth moment and Robert–Sargos exponential-sum estimates;
- Type $d_4$ analysis using an $L^2$ mean value theorem and a van der Corput exponent pair.

Their proof explicitly contains polynomial margins in hard Type $d_3$ subcases while the final proposition is stated with logarithmic saving.

The proof therefore supports the distinction made here between:

```text
noncentral analytic savings
and
central principal-boundary cancellation.
```

---

# 16. State transition

Advance candidate state

$$
v1.62
\to
v1.63.
$$

Add:

```text
B-RH-104
MRT_HARD_TYPE_D3_D4_ANALYSIS_CONTAINS_INTERNAL_FIXED_POWER_MARGIN
CERTIFIED_AS_PROOF_AUDIT

B-RH-105
FEJER_WEIGHT_MAKES_POLYLOG_NONPRINCIPAL_MAJOR_ARC_APPROXIMATION_ERRORS_SUPERCRITICAL
CERTIFIED

B-RH-106
PESC_SEED_CONTROLS_THE_Q1_ULTRAMAJOR_PRIME_ERROR_AT_N_TO_ONE_MINUS_D
CERTIFIED

B-RH-107
PARSEVAL_CONFINES_ALL_SEED_CRITICAL_PAIR_ENERGY_TO_AN_ULTRALOW_ADDITIVE_FREQUENCY_BAND
CERTIFIED

O-RH-163
Q1_CENTRAL_PRINCIPAL_ARC_HAS_A_SEED_CRITICAL_ENERGY_FLOOR_AT_EXPONENT_KAPPA
CERTIFIED_AS_METHOD_BARRIER

O-RH-164
PERFECT_NONCENTRAL_MRT_MINOR_ARC_CONTROL_CANNOT_AMPLIFY_WHILE_Q1_CENTRAL_ARC_REMAINS_AT_SEED_SCALE
CERTIFIED

O-RH-165
FIXED_STRIP_PLUS_DENSITY_HYPOTHESIS_SELBerg_BOUND_HAS_SUBCRITICAL_SAVING_KAPPA_TIMES_ONE_MINUS_TAU
CONDITIONAL_METHOD_CALIBRATION
```

Open:

```text
PAIR5
PRINCIPAL_ARC_LOW_FREQUENCY_PAIR_CANCELLATION_EXCESS
ACTIVE
```

No RH certificate is created.

---

# 17. Conclusion

The averaged Hardy–Littlewood proof does not fail because every part of its minor-arc machinery is only logarithmic.

Some of its hardest components already possess fixed-power internal slack.

The PESC amplifier fails for a more fundamental reason.

The $q=1$ central principal arc contains the seed boundary mode itself.

PESC controls that arc at exactly

$$
NH^2N^{-\kappa},
$$

and the canonical smooth boundary mode saturates the scale.

All improvements outside that central sector can leave the boundary untouched.

Therefore F-RH-022 cannot be obtained by a naive seed insertion into the existing averaged-prime-pair proof.

The next new information must be pair cancellation at the principal low frequency itself.

That is PAIR5.
