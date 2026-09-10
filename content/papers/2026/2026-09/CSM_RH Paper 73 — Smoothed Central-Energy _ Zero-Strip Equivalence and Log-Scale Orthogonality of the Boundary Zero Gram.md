# CSM_RH Paper 73

## Smoothed Central-Energy / Zero-Strip Equivalence and Log-Scale Orthogonality of the Boundary Zero Gram

**Project:** CSM_RH  
**Paper:** 73  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Track:** PAIR5 — `PRINCIPAL_ARC_LOW_FREQUENCY_PAIR_CANCELLATION_EXCESS`  
**Canonical root frontier:** F-RH-017-v3  
**Preferred arithmetic subfrontier:** F-RH-022  
**Status:** CENTRAL PRINCIPAL-ARC EXPONENT IDENTIFIED EXACTLY WITH ZERO-STRIP EXPONENT / PERSISTENT OFF-DIAGONAL CANCELLATION RULED OUT IN LOG-SCALE MEAN / ARITHMETIC ROOT STILL OPEN  
**Canonical entry state:** v1.63 / Paper 72 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 72 localized the entire seed-critical obstruction for the averaged Hardy–Littlewood pair residual to the $q=1$ ultra-low additive-frequency sector.

The present paper determines the exact exponent content of that sector.

Fix a nonzero smooth weight

$$
W\in C_c^\infty(1,2)
$$

and a constant $c>0$.

Define the smoothed principal prime error

$$
\boxed{
\mathcal S_W(N,y)
=
\sum_{n\ge1}
\Lambda(n)
W(n/N)
e(ny/N)
-
N
\int_0^\infty
W(u)e(yu)\,du
}
$$

for

$$
|y|\le c.
$$

For any auxiliary short-interval scale $H=o(N)$ define the central energy

$$
\boxed{
\mathcal C_W(N,H;c)
=
\frac{H^2}{N}
\int_{-c}^{c}
|\mathcal S_W(N,y)|^2dy.
}
$$

The factor $H^2/N$ is exactly the scale obtained from a $1/N$ central additive-frequency window with Fejér weight $|D_H|^2\asymp H^2$.

The first main theorem is an inverse theorem.

Suppose for some fixed $s>0$,

$$
\boxed{
\mathcal C_W(N,H;c)
\ll
NH^2
N^{-s+o(1)}.
}
$$

Then

$$
\boxed{
\zeta(\rho)=0
\quad\Longrightarrow\quad
\Re\rho
\le
1-\frac{s}{2}.
}
$$

The proof is direct and does not assume RH.

Indeed, for any smooth test

$$
\phi\in C_c^\infty(-c,c),
$$

let

$$
\Phi(u)
=
\int_{-c}^{c}
\phi(y)e(yu)\,dy
$$

and

$$
K(u)=W(u)\Phi(u).
$$

The scalar projection

$$
F_{W,\phi}(N)
=
\int_{-c}^{c}
\phi(y)\mathcal S_W(N,y)\,dy
$$

satisfies

$$
F_{W,\phi}(N)
\ll
N^{1-s/2+o(1)}
$$

by Cauchy–Schwarz.

Its Mellin transform is exactly

$$
\boxed{
\int_1^\infty
F_{W,\phi}(N)
N^{-z-1}dN
=
-\frac{\zeta'(z)}{\zeta(z)}
\widehat K(z)
-
\frac{\widehat K(1)}{z-1},
}
$$

initially for $\Re z>1$, where

$$
\widehat K(z)
=
\int_0^\infty
K(u)u^{z-1}du.
$$

The growth bound analytically continues the left-hand side to

$$
\Re z>1-\frac{s}{2}.
$$

For every hypothetical zeta zero $\rho$ in that region, the function

$$
G_\rho(y)
=
\int_1^2
W(u)u^{\rho-1}e(yu)\,du
$$

is not identically zero. Hence one can choose $\phi$ so that

$$
\widehat K(\rho)
=
\int\phi(y)G_\rho(y)\,dy
\ne0.
$$

The logarithmic derivative would then have an uncancelled pole, contradiction.

The converse holds at fixed-power resolution.

If

$$
\boxed{
\beta_*
:=
\sup_{\zeta(\rho)=0}\Re\rho
\le
1-\frac{s}{2},
}
$$

then standard smoothed contour shifting gives, uniformly for bounded $y$,

$$
\boxed{
\mathcal S_W(N,y)
\ll_{\varepsilon,W,c}
N^{1-s/2+\varepsilon}.
}
$$

Consequently,

$$
\boxed{
\mathcal C_W(N,H;c)
\ll
NH^2
N^{-s+o(1)}.
}
$$

Therefore the maximal central-energy saving exponent is exactly

$$
\boxed{
s_{\rm central}^*
=
2(1-\beta_*).
}
$$

By Paper 55,

$$
\boxed{
s_{\rm central}^*
=
\kappa_*,
}
$$

the maximal PESC exponent.

Thus the smoothed $q=1$ central-energy problem is exponent-equivalent to the root zero-strip problem itself.

The second main result addresses zero-pair cancellation.

The smooth explicit formula gives

$$
\boxed{
\mathcal S_W(N,y)
=
-\sum_\rho
N^\rho
G_\rho(y)
+
\text{trivial-zero / smoothing remainder}.
}
$$

Because $W$ is smooth and compactly supported,

$$
\boxed{
\|G_\rho\|_{L^2(-c,c)}
\ll_{A,W,c}
(1+|\gamma|)^{-A}
}
$$

for every fixed $A>0$.

Hence the zero expansion is an absolutely convergent Hilbert-valued almost-periodic series after normalization at any attained rightmost zero abscissa.

Assume

$$
\Theta=\beta_*
$$

is attained and $\Theta>1/2$.

Put

$$
t=\log N.
$$

Then, in $L^2(-c,c)$,

$$
\boxed{
e^{-\Theta t}
\mathcal S_W(e^t,\cdot)
-
\left(
-\sum_{\Re\rho=\Theta}
e^{i\gamma t}
G_\rho
\right)
\longrightarrow0.
}
$$

Grouping multiplicities at equal ordinates, Hilbert-space Parseval for almost-periodic Fourier series gives

$$
\boxed{
\lim_{T\to\infty}
\frac1T
\int_0^T
\left\|
\sum_{\Re\rho=\Theta}
e^{i\gamma t}
G_\rho
\right\|_2^2dt
=
\sum_{\gamma}
m_\gamma^2
\|G_{\Theta+i\gamma}\|_2^2
>0.
}
$$

Thus different zero ordinates may create negative cross terms at individual scales, but they cannot cancel the rightmost-zero diagonal on all logarithmic scales.

The corresponding normalized central energy has positive logarithmic mean at the critical exponent

$$
\boxed{
2(1-\Theta).
}
$$

This is a direct no-persistent-cancellation theorem for the PAIR5 zero Gram.

It agrees with known mean-square theory for the prime-number-theorem error: if $\Theta>1/2$, one has dyadic lower bounds of order

$$
X^{2\Theta+1-\varepsilon}
$$

for the mean square of $\psi(x)-x$.

The campaign consequence is sharp.

The hope that pair decorrelation of zero ordinates could by itself produce a fixed covariance deficit beyond the seed is rejected.

At $q=1$, a rightmost zero contributes a positive diagonal whose logarithmic-scale mean cannot be canceled by off-diagonal zero pairs.

Therefore any estimate

$$
\mathcal C_W
\ll
NH^2N^{-\kappa-\eta}
$$

already **is** a strict zero-strip improvement.

No vertical zero-spacing theorem can turn the seed into such an estimate without supplying horizontal information strong enough to remove the rightmost zero.

Recent work on pair correlation without assuming RH reinforces the distinction between density information and uniform strip information: pair-correlation hypotheses can force asymptotically $100\%$ of zeros onto the critical line, while the present fixed-power central-energy problem is sensitive to even a sparse or finite off-critical rightmost zero.

PAIR5 therefore reaches a spectral equivalence wall.

F-RH-022 remains a valid arithmetic root subfrontier, but its central $q=1$ core has no independent analytic leverage beyond the root problem. A successful proof must introduce genuinely new ordinary-prime arithmetic which directly produces the central fixed-power upper bound.

No RH theorem is claimed.

---

# 1. Smoothed central principal transform

Fix

$$
W\in C_c^\infty(1,2),
\qquad
W\not\equiv0.
$$

Let

$$
e(x)=e^{2\pi ix}.
$$

For $N\ge1$ and $|y|\le c$, define

$$
\boxed{
\mathcal S_W(N,y)
=
\sum_{n\ge1}
\Lambda(n)
W(n/N)
e(ny/N)
-
N
\int_0^\infty
W(u)e(yu)\,du.
}
$$

Only integers

$$
N<n<2N
$$

contribute to the sum.

The second term removes the pole at $s=1$.

---

# 2. Smoothed central energy

For any

$$
1\le H=o(N)
$$

define

$$
\boxed{
\mathcal C_W(N,H;c)
=
\frac{H^2}{N}
\int_{-c}^{c}
|\mathcal S_W(N,y)|^2dy.
}
$$

If

$$
\alpha=\frac{y}{N},
$$

then

$$
d\alpha=\frac{dy}{N}.
$$

Moreover, for fixed $|y|\le c$ and $H=o(N)$,

$$
D_H(y/N)
=
H(1+o(1)).
$$

Thus $\mathcal C_W$ is exactly the smooth model for the $1/N$ central part of the Fejér-weighted pair energy.

---

# 3. Scalar testing of central energy

Let

$$
\phi\in C_c^\infty(-c,c).
$$

Define

$$
\Phi(u)
=
\int_{-c}^{c}
\phi(y)e(yu)dy
$$

and

$$
\boxed{
K(u)=W(u)\Phi(u).
}
$$

Then

$$
K\in C_c^\infty(1,2).
$$

The scalar projection is

$$
\begin{aligned}
F_{W,\phi}(N)
&=
\int_{-c}^{c}
\phi(y)\mathcal S_W(N,y)dy
\\
&=
\boxed{
\sum_{n\ge1}
\Lambda(n)K(n/N)
-
N\widehat K(1),
}
\end{aligned}
$$

where

$$
\widehat K(z)
=
\int_0^\infty
K(u)u^{z-1}du.
$$

---

# 4. Exact Mellin identity

For $\Re z>1$, termwise integration is justified.

Since $K$ is supported on $(1,2)$,

$$
\begin{aligned}
\int_1^\infty
\sum_n
\Lambda(n)K(n/N)
N^{-z-1}dN
&=
\sum_{n\ge2}
\Lambda(n)n^{-z}
\widehat K(z)
\\
&=
-\frac{\zeta'(z)}{\zeta(z)}
\widehat K(z).
\end{aligned}
$$

Also,

$$
\int_1^\infty
N\widehat K(1)
N^{-z-1}dN
=
\frac{\widehat K(1)}{z-1}.
$$

Hence:

## Theorem 4.1 — Exact central-test Mellin identity

$$
\boxed{
\int_1^\infty
F_{W,\phi}(N)
N^{-z-1}dN
=
-\frac{\zeta'(z)}{\zeta(z)}
\widehat K(z)
-
\frac{\widehat K(1)}{z-1}.
}
$$

Record:

```text
B-RH-108
EXACT_MELLIN_IDENTITY_FOR_SMOOTHED_Q1_CENTRAL_TEST
CERTIFIED
```

---

# 5. Central-energy upper bound implies a zero-free strip

Assume

$$
\boxed{
\mathcal C_W(N,H;c)
\ll
NH^2N^{-s+o(1)}.
}
$$

Then

$$
\int_{-c}^{c}
|\mathcal S_W(N,y)|^2dy
\ll
N^{2-s+o(1)}.
$$

By Cauchy–Schwarz,

$$
\boxed{
F_{W,\phi}(N)
\ll_{\phi}
N^{1-s/2+o(1)}.
}
$$

Therefore the Mellin integral in Theorem 4.1 converges and is analytic in

$$
\boxed{
\Re z>1-\frac{s}{2}.
}
$$

Suppose $\rho$ is a zeta zero in this half-plane.

Define

$$
G_\rho(y)
=
\int_1^2
W(u)u^{\rho-1}e(yu)du.
$$

This is an entire function of $y$.

It cannot vanish identically, because it is the Fourier transform of the nonzero compactly supported function

$$
W(u)u^{\rho-1}.
$$

Hence there exists

$$
\phi\in C_c^\infty(-c,c)
$$

such that

$$
\boxed{
\widehat K(\rho)
=
\int_{-c}^{c}
\phi(y)G_\rho(y)dy
\ne0.
}
$$

Then the right side of Theorem 4.1 has an uncancelled pole at $\rho$, contradiction.

Thus:

## Theorem 5.1 — Central-energy inverse zero-strip theorem

$$
\boxed{
\mathcal C_W
\ll
NH^2N^{-s+o(1)}
\quad\Longrightarrow\quad
\beta_*
\le
1-\frac{s}{2}.
}
$$

Record:

```text
B-RH-109
SMOOTHED_Q1_CENTRAL_ENERGY_POWER_SAVING_IMPLIES_THE_MATCHING_ZERO_FREE_STRIP
CERTIFIED
```

No RH assumption is used.

---

# 6. Zero-free strip implies central-energy upper bound

Assume

$$
\boxed{
\beta_*
\le
1-\frac{s}{2}.
}
$$

Fix $\varepsilon>0$.

For bounded $y$, the Mellin transform

$$
\widehat W_y(z)
=
\int_1^2
W(u)e(yu)u^{z-1}du
$$

decays faster than any power of $|\Im z|$, uniformly in

$$
|y|\le c.
$$

The standard smoothed explicit formula / contour shift to

$$
\Re z
=
1-\frac{s}{2}
+\varepsilon
$$

therefore gives

$$
\boxed{
\mathcal S_W(N,y)
\ll_{\varepsilon,W,c}
N^{1-s/2+\varepsilon}
}
$$

uniformly on $|y|\le c$.

Consequently,

$$
\boxed{
\mathcal C_W(N,H;c)
\ll_{\varepsilon,W,c}
NH^2
N^{-s+2\varepsilon}.
}
$$

At fixed-power resolution:

## Theorem 6.1 — Zero-strip to central-energy theorem

$$
\boxed{
\beta_*
\le
1-\frac{s}{2}
\quad\Longrightarrow\quad
\mathcal C_W
\ll
NH^2N^{-s+o(1)}.
}
$$

Record:

```text
B-RH-110
ZERO_FREE_STRIP_GIVES_MATCHING_SMOOTHED_Q1_CENTRAL_ENERGY_EXPONENT
CERTIFIED
```

---

# 7. Exact central exponent identity

Define

$$
s_{\rm central}^*
=
\sup
\left\{
s:
\mathcal C_W(N,H;c)
\ll
NH^2N^{-s+o(1)}
\right\}.
$$

Theorems 5.1 and 6.1 give:

## Theorem 7.1 — Central-energy / zero-strip exponent identity

$$
\boxed{
s_{\rm central}^*
=
2(1-\beta_*).
}
$$

Paper 55 established

$$
\kappa_*
=
2(1-\beta_*).
$$

Therefore:

$$
\boxed{
s_{\rm central}^*
=
\kappa_*.
}
$$

Create:

```text
B-RH-111
MAXIMAL_Q1_CENTRAL_ENERGY_EXPONENT_EQUALS_MAXIMAL_PESC_EXPONENT
CERTIFIED
```

This is the central spectral equivalence wall.

---

# 8. Smooth explicit formula as a Hilbert-valued zero series

For

$$
G_\rho(y)
=
\int_1^2
W(u)u^{\rho-1}e(yu)du,
$$

smooth explicit formula gives

$$
\boxed{
\mathcal S_W(N,y)
=
-\sum_\rho
N^\rho
G_\rho(y)
+
\mathcal T_W(N,y),
}
$$

where $\mathcal T_W$ contains the trivial-zero and rapidly decaying smoothing contributions.

For every fixed $A>0$,

$$
\boxed{
\|G_\rho\|_{L^2(-c,c)}
\ll_{A,W,c}
(1+|\gamma|)^{-A}.
}
$$

Indeed, repeated integration by parts in $u$ or $\log u$ gives rapid decay for bounded $y$.

Combined with

$$
N(T+1)-N(T)
=
O(\log T),
$$

this implies

$$
\boxed{
\sum_\rho
\|G_\rho\|_{L^2(-c,c)}
<\infty.
}
$$

Hence the zero expansion is absolutely convergent as a Hilbert-valued series after normalization by any rightmost real exponent.

---

# 9. Attained rightmost zero and boundary almost periodicity

Assume

$$
\Theta=\beta_*
$$

is attained and

$$
\Theta>\frac12.
$$

Set

$$
t=\log N.
$$

Normalize:

$$
\boxed{
\mathcal F_t(y)
=
e^{-\Theta t}
\mathcal S_W(e^t,y).
}
$$

Every zero with $\beta<\Theta$ carries the factor

$$
e^{-(\Theta-\beta)t}.
$$

By absolute Hilbert summability and dominated convergence,

$$
\boxed{
\left\|
\mathcal F_t
+
\sum_{\Re\rho=\Theta}
e^{i\gamma t}G_\rho
\right\|_2
\longrightarrow0.
}
$$

Thus the asymptotic boundary signal is a Hilbert-valued almost-periodic Fourier series.

---

# 10. Log-scale orthogonality

Group equal ordinates.

If $\rho=\Theta+i\gamma$ has multiplicity $m_\gamma$, its coefficient is

$$
m_\gamma G_\rho.
$$

For an absolutely convergent Hilbert-valued Fourier series,

$$
F(t)
=
\sum_\gamma
e^{i\gamma t}V_\gamma,
$$

one has

$$
\boxed{
\lim_{T\to\infty}
\frac1T
\int_0^T
\|F(t)\|_2^2dt
=
\sum_\gamma
\|V_\gamma\|_2^2.
}
$$

Therefore:

## Theorem 10.1 — Boundary-zero Gram log-orthogonality

$$
\boxed{
\lim_{T\to\infty}
\frac1T
\int_0^T
\left\|
\sum_{\Re\rho=\Theta}
e^{i\gamma t}
G_\rho
\right\|_2^2dt
=
\sum_{\gamma}
m_\gamma^2
\|G_{\Theta+i\gamma}\|_2^2
>0.
}
$$

Create:

```text
B-RH-112
RIGHTMOST_ZERO_GRAM_DIAGONALIZES_IN_LOG_SCALE_MEAN
CERTIFIED
```

No linear-independence conjecture on the ordinates is required.

Distinct frequencies are orthogonal in the long Cesàro mean.

---

# 11. No persistent off-diagonal cancellation

At a fixed scale $N$, the zero-pair expansion contains cross terms

$$
e^{i(\gamma-\gamma')\log N}
\langle
G_\rho,G_{\rho'}
\rangle.
$$

They may be negative.

Theorem 10.1 shows that for

$$
\gamma\ne\gamma',
$$

their long $\log N$ average vanishes.

The diagonal survives with positive mass.

Therefore:

## Corollary 11.1 — No-persistent-cancellation theorem

If the rightmost zero abscissa is attained, the boundary-zero diagonal cannot be canceled by off-diagonal zero pairs on all logarithmic scales.

Create:

```text
O-RH-166
OFF_DIAGONAL_ZERO_PAIRS_CANNOT_PERSISTENTLY_CANCEL_A_RIGHTMOST_ZERO_DIAGONAL_ACROSS_LOG_SCALES
CERTIFIED
```

This directly answers the central PAIR5 Gram question.

---

# 12. Relation to known PNT-error mean square

Known mean-square theory provides an external analogue.

If

$$
\Theta>\frac12,
$$

then

$$
\boxed{
X^{2\Theta+1-\varepsilon}
\ll
\int_X^{2X}
|\psi(x)-x|^2dx
\ll
X^{2\Theta+1}.
}
$$

The lower bound is ineffective because it depends on hypothetical zero behavior near $\Theta$.

This confirms the same principle:

```text
rightmost zero real part
sets the fixed-power mean-square exponent.
```

The present theorem localizes that principle specifically to the smoothed $q=1$ additive central sector.

External source:

Kühn, Robles, Zeindler et al.,
*On the mean values of the error terms in Mertens' theorems*,
Research in Number Theory, 2025.

---

# 13. Almost-periodic literature calibration

The use of logarithmic-scale Fourier series for prime-number error terms belongs to a well-developed almost-periodic framework.

Akbary, Ng and Shahabi establish limiting distributions for broad classes of classical error terms from explicit formulas.

Nathan Ng's 2025 work on prime-number error terms develops additional $L^2$ bounds for almost-periodic functions in precisely this style.

The current PAIR5 argument is simpler because the smooth weight makes the zero-response coefficients rapidly summable.

No conjectural linear independence of zeta-zero ordinates is used.

---

# 14. Why vertical pair decorrelation is not enough

A theorem about zero-pair spacing controls the differences

$$
\gamma-\gamma'.
$$

It may reduce off-diagonal interactions.

But Theorem 10.1 shows that the rightmost diagonal is already positive after those interactions are averaged out.

Therefore vertical pair decorrelation cannot by itself lower the central energy exponent below

$$
2(1-\Theta).
$$

To obtain a larger saving exponent, one must force

$$
\Theta
$$

to move left.

That is horizontal zero information.

Hence:

```text
PAIR5 CENTRAL COVARIANCE DEFICIT
IS NOT A FREE CONSEQUENCE OF ZERO-PAIR REPULSION.
```

---

# 15. Recent pair-correlation calibration without RH

Recent work of Goldston, Lee, Schettler and Suriajaya shows that Montgomery's Pair Correlation Conjecture, treated without assuming RH, implies that asymptotically $100\%$ of zeta zeros are simple and on the critical line.

This is a striking horizontal consequence of pair-correlation information.

But the theorem is density-level.

The fixed-power central-energy problem is sensitive to even a sparse or finite rightmost off-critical zero, because a single such zero fixes the exponent in Theorems 5.1 and 10.1.

Thus PAIR5 requires stronger all-zero horizontal control than a density-one statement.

External source:

D. A. Goldston, J. Lee, J. Schettler, A. I. Suriajaya,
*Pair Correlation Conjecture for the zeros of the Riemann zeta-function I: simple and critical zeros*,
2025.

---

# 16. Consequence for F-RH-022

F-RH-022 remains a valid arithmetic sufficient theorem:

$$
|\mathcal R_{\rm HL}^{(2)}|
\ll
NH^2N^{-\xi},
\qquad
\xi>\kappa
$$

would amplify PESC $(\kappa)$.

But after Paper 72, every noncentral sector can in principle be made supercritical without touching the root mode.

Paper 73 now proves that the remaining smoothed central sector has maximal exponent exactly

$$
\kappa_*.
$$

Therefore a successful F-RH-022 proof must contain, somewhere in its arithmetic argument, a theorem which is genuinely strong enough to improve the zero strip.

There is no remaining generic zero-Gram cancellation to harvest for free.

---

# 17. PAIR5 verdict

Record:

```text
PAIR5A
RIGHTMOST ZERO GRAM LOG-ORTHOGONALITY
CLOSED / CERTIFIED.

PAIR5B
PERSISTENT OFF-DIAGONAL CANCELLATION
CLOSED AS IMPOSSIBLE AT LOG-SCALE MEAN.

PAIR5C
CENTRAL ENERGY FIXED-POWER EXCESS FROM VERTICAL PAIR STATISTICS ALONE
CLOSED AS NONVIABLE.

PAIR5D
NEW ORDINARY-PRIME ARITHMETIC CENTRAL UPPER
OPEN.
```

The root problem survives only in PAIR5D.

---

# 18. New obstruction and state transition

Advance candidate state

$$
v1.63
\to
v1.64.
$$

Add:

```text
B-RH-108
EXACT_MELLIN_IDENTITY_FOR_SMOOTHED_Q1_CENTRAL_TEST

B-RH-109
SMOOTHED_Q1_CENTRAL_ENERGY_POWER_SAVING_IMPLIES_THE_MATCHING_ZERO_FREE_STRIP

B-RH-110
ZERO_FREE_STRIP_GIVES_MATCHING_SMOOTHED_Q1_CENTRAL_ENERGY_EXPONENT

B-RH-111
MAXIMAL_Q1_CENTRAL_ENERGY_EXPONENT_EQUALS_MAXIMAL_PESC_EXPONENT

B-RH-112
RIGHTMOST_ZERO_GRAM_DIAGONALIZES_IN_LOG_SCALE_MEAN

O-RH-166
OFF_DIAGONAL_ZERO_PAIRS_CANNOT_PERSISTENTLY_CANCEL_A_RIGHTMOST_ZERO_DIAGONAL_ACROSS_LOG_SCALES
```

No RH certificate is created.

---

# 19. Recommended next action

PAIR5 has now exhausted the generic spectral geometry.

The next round should stop asking whether zero-pair phases can cancel the boundary mode.

They cannot do so persistently.

Return to the arithmetic side of F-RH-022 and ask a narrower question:

```text
Is there an ordinary-prime identity or inequality
which gives a fixed-power upper bound
for the smoothed q=1 central prime error
without deriving it from the existing zero strip?
```

Candidate mechanisms must fail for the pseudo-prime and Beurling models of Paper 64 and must use actual integer factorization / prime-pair arithmetic.

If no such arithmetic mechanism emerges, PAIR5 should be regarded as having reached the RH-equivalent wall rather than as an independent amplifier engine.

---

# 20. Conclusion

The $q=1$ central principal arc has now been characterized exactly at fixed-power resolution.

Its maximal saving exponent is

$$
\boxed{
2(1-\beta_*).
}
$$

That is the same exponent as maximal PESC.

If the rightmost zero abscissa is attained, the boundary-zero response is an almost-periodic Hilbert-valued Fourier series in $\log N$, and its diagonal has strictly positive logarithmic mean.

Off-diagonal zero pairs cannot remove it on all scales.

Thus the final central fixed-power gain cannot come from generic pair decorrelation.

It must come from arithmetic strong enough to move the rightmost zero itself.

That is the remaining CSM_RH root problem.
