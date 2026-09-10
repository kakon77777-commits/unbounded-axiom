# CSM_RH Paper 78

## Universal Zero-Pole Preservation in the Renormalized Vaughan Coefficient and the Polynomial-Factor Anatomy Barrier

**Project:** CSM_RH  
**Paper:** 78  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 47 — `ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Active frontier:** F-RH-024 — `RENORMALIZED_VAUGHAN_BALANCED_DEFECT_POWER`  
**Status:** RENORMALIZED COEFFICIENT ZERO SPECTRUM AUDITED / PARAMETER-INVARIANT ROOT-HARD CORE CERTIFIED / GENERIC TITCHMARSH AND SMALL-FACTOR ANATOMY ROUTES INSUFFICIENT  
**Canonical entry state:** v1.68 / Paper 77 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 77 derived the exact root identity

$$
\mathcal R_W
=
-
\mathcal V^{\rm ren}_{U,V}
+
\mathcal E_I,
$$

where

$$
\mathcal V^{\rm ren}_{U,V}
=
\mathcal T^{II}_{U,V}
-
\mathcal M_{U,V}
$$

and

$$
\mathcal E_I
\ll
NUV(\log N)^{O(1)}.
$$

It therefore opened F-RH-024: prove a fixed-power upper bound for the renormalized Vaughan defect.

The present paper determines the exact Dirichlet-series spectrum of the renormalized coefficient.

Define

$$
M_U(s)
=
\sum_{d\le U}
\frac{\mu(d)}{d^s},
$$

$$
L_V(s)
=
\sum_{e\le V}
\frac{\Lambda(e)}{e^s},
$$

and

$$
b_U(k)
=
\sum_{\substack{d\mid k\\d\le U}}
\mu(d).
$$

Let

$$
\boxed{
c_{U,V}(n)
=
\sum_{\substack{ek=n\\e>V\\k>U}}
\Lambda(e)b_U(k).
}
$$

Then

$$
\boxed{
\mathcal T^{II}_{U,V}
=
\sum_n
f_{N,H}(n)c_{U,V}(n).
}
$$

Since for $U>1$

$$
\sum_{k>U}
\frac{b_U(k)}{k^s}
=
\zeta(s)M_U(s)-1,
$$

and

$$
\sum_{e>V}
\frac{\Lambda(e)}{e^s}
=
-\frac{\zeta'(s)}{\zeta(s)}
-
L_V(s),
$$

the Dirichlet series of the balanced coefficient is

$$
\boxed{
C_{U,V}(s)
=
\left(
-\frac{\zeta'(s)}{\zeta(s)}
-
L_V(s)
\right)
\left(
\zeta(s)M_U(s)-1
\right).
}
$$

Write

$$
M_U=M_U(1),
$$

$$
J_U
=
\sum_{d\le U}
\frac{\mu(d)\log d}{d},
$$

and

$$
L_V=L_V(1).
$$

Paper 77's scalar counterterm can be written coefficientwise as

$$
\boxed{
q_{U,V}(n)
=
M_U\log n
-
M_UL_V
-
J_U
-
1.
}
$$

Indeed,

$$
\boxed{
\mathcal M_{U,V}
=
\sum_n
f_{N,H}(n)q_{U,V}(n).
}
$$

Its Dirichlet series is

$$
\boxed{
Q_{U,V}(s)
=
-M_U\zeta'(s)
-
\left(
M_UL_V+J_U+1
\right)
\zeta(s).
}
$$

Therefore the renormalized coefficient

$$
\boxed{
h_{U,V}(n)
=
c_{U,V}(n)-q_{U,V}(n)
}
$$

has Dirichlet series

$$
\boxed{
H_{U,V}(s)
=
C_{U,V}(s)-Q_{U,V}(s).
}
$$

The first main theorem is that the renormalization removes **exactly** the pole at $s=1$.

Near

$$
s=1,
$$

$$
C_{U,V}(s)
=
\frac{M_U}{(s-1)^2}
+
\frac{
-J_U-1-M_UL_V
}{
s-1
}
+
O(1),
$$

while $Q_{U,V}$ has precisely the same principal part.

Thus

$$
\boxed{
H_{U,V}(s)
\text{ is holomorphic at }s=1.
}
$$

But no nontrivial zeta-zero pole is removed.

If $\rho$ is a zero of $\zeta$ of multiplicity $m$, then

$$
\zeta(\rho)=0
$$

and

$$
\zeta(s)M_U(s)-1
=
-1+O(s-\rho).
$$

Since

$$
-\frac{\zeta'}{\zeta}(s)
=
-\frac{m}{s-\rho}
+
O(1),
$$

one obtains

$$
\boxed{
\operatorname*{Res}_{s=\rho}
H_{U,V}(s)
=
+m.
}
$$

This residue is independent of $U$ and $V$.

Equivalently,

$$
\boxed{
H_{U,V}(s)
=
\frac{\zeta'(s)}{\zeta(s)}
+
E_{U,V}(s),
}
$$

where $E_{U,V}$ has no pole at any nontrivial zero of $\zeta$.

An explicit formula is

$$
\boxed{
\begin{aligned}
E_{U,V}(s)
&=
\zeta'(s)
\left(
M_U-M_U(s)
\right)
\\
&\quad
+
L_V(s)
\left(
1-\zeta(s)M_U(s)
\right)
\\
&\quad
+
\left(
M_UL_V+J_U+1
\right)
\zeta(s).
\end{aligned}
}
$$

Thus, coefficientwise,

$$
\boxed{
h_{U,V}
=
-\Lambda
+
e_{U,V},
}
$$

where $e_{U,V}$ is a Type-I prime approximant whose Dirichlet series has no nontrivial zeta-zero poles.

The $s=1$ residue of $E_{U,V}$ is $+1$, so $e_{U,V}$ has the correct first-order mean to approximate the constant coefficient $1$.

This gives a conceptual form of Paper 77's exact identity:

```text
renormalized Vaughan balanced coefficient
=
zero-pole-free Type-I prime approximant
minus the actual von Mangoldt coefficient.
```

The RH-sensitive part is therefore parameter-invariant.

For any two parameter choices

$$
(U,V),
\qquad
(U',V'),
$$

$$
\boxed{
H_{U,V}(s)
-
H_{U',V'}(s)
}
$$

has no nontrivial zeta-zero poles.

All choices carry the same universal

$$
\zeta'/\zeta
$$

hard core.

Hence optimizing Vaughan parameters may improve the Type-I error budget, but it cannot remove or weaken the boundary zero spectrum.

The second main result is a central cross-Gram calibration.

Let

$$
W\in C_c^\infty(1,2),
$$

and define the smoothed renormalized coefficient transform

$$
\boxed{
\mathcal H_{U,V;W}(N,y)
=
\sum_n
h_{U,V}(n)
W(n/N)
e(ny/N).
}
$$

Let the smoothed prime-error transform be

$$
\boxed{
\mathcal S_W(N,y)
=
\sum_n
\Lambda(n)
W(n/N)
e(ny/N)
-
N
\int
W(u)e(yu)du.
}
$$

Paper 73 gives the boundary response

$$
\mathcal S_W(N,y)
=
-\sum_\rho
m_\rho
N^\rho
G_\rho(y)
+
\text{lower terms},
$$

where

$$
G_\rho(y)
=
\int_1^2
W(u)u^{\rho-1}e(yu)du.
$$

The residue theorem above gives the opposite response

$$
\boxed{
\mathcal H_{U,V;W}(N,y)
=
+\sum_\rho
m_\rho
N^\rho
G_\rho(y)
+
\text{lower terms}.
}
$$

Therefore the rightmost-zero diagonal in their central cross-energy is **negative**.

Assume the rightmost abscissa

$$
\Theta
=
\sup_\rho\Re\rho
$$

is attained.

Set

$$
H=N^{1-\tau}.
$$

Define

$$
\boxed{
\mathfrak X_{U,V}(N,H;c)
=
\frac{H}{N}
\int_{-c}^{c}
\mathcal H_{U,V;W}(N,y)
\overline{
\mathcal S_W(N,y)
}
dy.
}
$$

Then logarithmic-scale orthogonality gives

$$
\boxed{
\lim_{T\to\infty}
\frac1T
\int_0^T
\frac{
\mathfrak X_{U,V}(e^t,e^{(1-\tau)t};c)
}{
e^{(1-\tau)t}
e^{(2\Theta-1)t}
}
dt
=
-
\sum_{\Re\rho=\Theta}
m_\rho^2
\|G_\rho\|_{L^2(-c,c)}^2
<0.
}
$$

Thus the renormalized balanced coefficient is anti-aligned with the prime error on the rightmost zero diagonal.

Off-diagonal zero pairs cannot remove this contribution on all logarithmic scales.

The fixed-power size is

$$
\boxed{
NH
N^{-2(1-\Theta)}.
}
$$

At a saturated PESC $(\kappa)$ boundary,

$$
\Theta
=
1-\frac{\kappa}{2},
$$

this is exactly

$$
\boxed{
NH
N^{-\kappa}.
}
$$

Therefore the spectral sector of F-RH-024 is genuinely root-critical.

This does not make F-RH-024 useless. Its value is that $h_{U,V}$ has a highly specific ordinary-factorization realization.

But it closes two naive routes.

### Generic Titchmarsh/divisor-shift transfer

Power-saving Titchmarsh-type theorems apply to coefficients such as $\tau$, $\tau_k$, automorphic coefficients, or other dense multiplicative sequences whose Dirichlet series do not carry a universal $\zeta'/\zeta$ pole at every zeta zero.

The renormalized coefficient $h_{U,V}$ is not in that spectral class.

A power-saving theorem for its shifted-prime correlation would already be RH-level horizontal information.

### Existing shifted-prime anatomy transfer

Ford's shifted-prime Kubilius model gives a strong total-variation approximation for the prime factors of $p+a$ below a cutoff $y$.

The approximation becomes asymptotically sharp in the regime

$$
y=x^{o(1)}.
$$

The paper explicitly notes that the distribution of the large prime factors of shifted primes is not well understood.

F-RH-024 requires balanced polynomial factorization:

$$
e\asymp N^\theta,
\qquad
k\asymp N^{1-\theta},
$$

with $\theta$ bounded away from $0$ and $1$ in the genuinely Type-II blocks.

Thus current anatomy transference does not reach the required factor range.

The Campaign-47 conclusion is:

```text
F-RH-024 remains the preferred root arithmetic frontier.

Its s=1 main is fully renormalized.

Its nontrivial zero spectrum is not renormalized at all.

Vaughan parameter optimization cannot remove the hard spectrum.

Generic prime-times-divisor power-saving theorems do not apply automatically.

Current shifted-prime factor-anatomy theorems control only the small-factor regime, not balanced polynomial factors.
```

The next task is therefore to dyadically localize the ordinary-factorization source of the universal zero pole and determine which polynomial factor blocks carry the rightmost-zero mass.

That is a concrete arithmetic question.

No RH theorem is claimed.

---

# 1. Balanced coefficient Dirichlet series

Define

$$
M_U(s)
=
\sum_{d\le U}
\mu(d)d^{-s}.
$$

The truncated divisor coefficient

$$
b_U(k)
=
\sum_{\substack{d\mid k\\d\le U}}
\mu(d)
$$

has Dirichlet series

$$
\sum_{k\ge1}
b_U(k)k^{-s}
=
\zeta(s)M_U(s).
$$

If

$$
1<k\le U,
$$

then every divisor of $k$ is at most $U$, so

$$
b_U(k)
=
\sum_{d\mid k}\mu(d)
=
0.
$$

Also

$$
b_U(1)=1.
$$

Hence for $U>1$,

$$
\boxed{
\sum_{k>U}
b_U(k)k^{-s}
=
\zeta(s)M_U(s)-1.
}
$$

Likewise,

$$
\boxed{
\sum_{e>V}
\Lambda(e)e^{-s}
=
-\frac{\zeta'(s)}{\zeta(s)}
-
L_V(s).
}
$$

Multiplying gives Theorem 1.1:

$$
\boxed{
C_{U,V}(s)
=
\left(
-\frac{\zeta'}{\zeta}-L_V
\right)
\left(
\zeta M_U-1
\right).
}
$$

---

# 2. Coefficient form of the Paper-77 counterterm

Paper 77 defined

$$
\mathcal M_{U,V}
=
F
\left[
M_U(\log N-L_V)-J_U-1
\right]
+
G M_U,
$$

where

$$
G
=
\sum_n
f(n)\log(n/N).
$$

Since

$$
G
=
\sum_n
f(n)
\left(
\log n-\log N
\right),
$$

one obtains

$$
\begin{aligned}
\mathcal M_{U,V}
&=
\sum_n
f(n)
\left[
M_U\log n
-
M_UL_V
-
J_U
-
1
\right].
\end{aligned}
$$

Therefore:

## Theorem 2.1 — Coefficientwise renormalization

$$
\boxed{
q_{U,V}(n)
=
M_U\log n
-
M_UL_V
-
J_U
-
1.
}
$$

Create:

```text
B-RH-123
PAPER77_SCALAR_COUNTERTERM_IS_A_COEFFICWISE_LOG_AFFINE_RENORMALIZATION
CERTIFIED
```

---

# 3. Dirichlet series of the counterterm

Since

$$
\sum_{n\ge1}
\frac{\log n}{n^s}
=
-\zeta'(s),
$$

$$
\sum_{n\ge1}
n^{-s}
=
\zeta(s),
$$

the Dirichlet series of $q_{U,V}$ is

$$
\boxed{
Q_{U,V}(s)
=
-M_U\zeta'(s)
-
\left(
M_UL_V+J_U+1
\right)
\zeta(s).
}
$$

---

# 4. Exact cancellation at $s=1$

Let

$$
t=s-1.
$$

Use

$$
\zeta(s)
=
\frac1t
+
\gamma
+
O(t),
$$

$$
-\frac{\zeta'}{\zeta}(s)
=
\frac1t
-
\gamma
+
O(t),
$$

and

$$
M_U(s)
=
M_U
-
J_U t
+
O(t^2).
$$

Then

$$
\zeta(s)M_U(s)-1
=
\frac{M_U}{t}
+
\gamma M_U
-
J_U
-
1
+
O(t).
$$

Also

$$
-\frac{\zeta'}{\zeta}(s)-L_V(s)
=
\frac1t
-
\gamma
-
L_V
+
O(t).
$$

Therefore

$$
\boxed{
C_{U,V}(s)
=
\frac{M_U}{t^2}
+
\frac{
-J_U-1-M_UL_V
}{t}
+
O(1).
}
$$

But $Q_{U,V}$ has exactly the same two polar coefficients.

Hence:

## Theorem 4.1 — Complete $s=1$ renormalization

$$
\boxed{
H_{U,V}(s)
=
C_{U,V}(s)-Q_{U,V}(s)
}
$$

is holomorphic at $s=1$.

Create:

```text
B-RH-124
RENORMALIZED_VAUGHAN_COEFFICIENT_REMOVES_THE_COMPLETE_S1_PRINCIPAL_PART
CERTIFIED
```

---

# 5. Universal nontrivial-zero residue

Let $\rho$ be a zeta zero of multiplicity $m$.

Then

$$
-\frac{\zeta'}{\zeta}(s)
=
-\frac{m}{s-\rho}
+
O(1).
$$

At the same point,

$$
\zeta(s)M_U(s)-1
=
-1+O(s-\rho).
$$

Thus

$$
C_{U,V}(s)
=
\frac{m}{s-\rho}
+
O(1).
$$

The counterterm series $Q_{U,V}$ is analytic at $\rho$.

Therefore:

## Theorem 5.1 — Parameter-independent zero-pole preservation

$$
\boxed{
\operatorname*{Res}_{s=\rho}
H_{U,V}(s)
=
m.
}
$$

This does not depend on $U$ or $V$.

Create:

```text
B-RH-125
RENORMALIZED_VAUGHAN_COEFFICIENT_PRESERVES_EVERY_NONTRIVIAL_ZETA_ZERO_WITH_UNIVERSAL_OPPOSITE_PRIME_RESIDUE
CERTIFIED
```

---

# 6. Zero-pole-free Type-I approximant

Expand $C_{U,V}$:

$$
\begin{aligned}
C_{U,V}
&=
-\zeta'M_U(s)
+
\frac{\zeta'}{\zeta}
\\
&\quad
-
L_V(s)\zeta M_U(s)
+
L_V(s).
\end{aligned}
$$

Subtract $Q_{U,V}$.

Then

$$
\boxed{
H_{U,V}
=
\frac{\zeta'}{\zeta}
+
E_{U,V},
}
$$

where

$$
\boxed{
\begin{aligned}
E_{U,V}(s)
&=
\zeta'(s)
\left(
M_U-M_U(s)
\right)
\\
&\quad
+
L_V(s)
\left(
1-\zeta(s)M_U(s)
\right)
\\
&\quad
+
\left(
M_UL_V+J_U+1
\right)
\zeta(s).
\end{aligned}
}
$$

At every nontrivial zeta zero, $E_{U,V}$ is analytic.

Since

$$
\frac{\zeta'}{\zeta}(s)
=
-\sum_n
\frac{\Lambda(n)}{n^s},
$$

the coefficient identity is

$$
\boxed{
h_{U,V}
=
-\Lambda
+
e_{U,V}.
}
$$

The series $E_{U,V}$ has residue $+1$ at $s=1$, so $e_{U,V}$ is a first-order prime approximant with mean $1$.

This gives the spectral meaning of the Type-I recombination in Paper 77.

---

# 7. Parameter-invariant hard core

Let two Vaughan choices be

$$
(U,V)
$$

and

$$
(U',V').
$$

Then

$$
\begin{aligned}
H_{U,V}(s)-H_{U',V'}(s)
=
E_{U,V}(s)-E_{U',V'}(s).
\end{aligned}
$$

The right side has no nontrivial zeta-zero poles.

Therefore:

## Corollary 7.1 — Vaughan parameter changes are zero-pole-free

$$
\boxed{
H_{U,V}
-
H_{U',V'}
}
$$

contains no rightmost-zero singularity.

Create:

```text
B-RH-126
ALL_VAUGHAN_PARAMETER_CHOICES_SHARE_THE_SAME_PARAMETER_INVARIANT_ZETA_PRIME_HARD_CORE
CERTIFIED
```

Parameter optimization can improve the deterministic Type-I error but cannot spectrally weaken the root component.

---

# 8. Exact form of F-RH-024

Define

$$
h_{U,V}(n)
=
c_{U,V}(n)-q_{U,V}(n).
$$

Then

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
=
\sum_n
f_{N,H}(n)h_{U,V}(n).
}
$$

Using

$$
h_{U,V}
=
-\Lambda+e_{U,V},
$$

$$
\begin{aligned}
\mathcal V^{\rm ren}_{U,V}
&=
-\sum_n
\Lambda(n)f(n)
+
\sum_n
e_{U,V}(n)f(n).
\end{aligned}
$$

Paper 77's Type-I computation is exactly

$$
\boxed{
\sum_n
e_{U,V}(n)f(n)
=
F+\mathcal E_I.
}
$$

Therefore

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
=
-\mathcal R_W
+
\mathcal E_I.
}
$$

This recovers the exact root bridge and shows where the universal pole enters.

---

# 9. Smoothed zero response

Fix

$$
W\in C_c^\infty(1,2).
$$

Let

$$
G_\rho(y)
=
\int_1^2
W(u)u^{\rho-1}e(yu)du.
$$

The prime error has rightmost-zero response

$$
\boxed{
\mathcal S_W(N,y)
=
-\sum_\rho
m_\rho
N^\rho
G_\rho(y)
+
\text{lower terms}.
}
$$

The universal residue theorem gives

$$
\boxed{
\mathcal H_{U,V;W}(N,y)
=
+\sum_\rho
m_\rho
N^\rho
G_\rho(y)
+
\text{lower terms}.
}
$$

Thus the two transforms contain the same boundary functions with opposite sign.

---

# 10. Negative rightmost-zero cross Gram

Assume the rightmost zero abscissa

$$
\Theta
=
\sup_\rho\Re\rho
$$

is attained.

Let

$$
H=N^{1-\tau}.
$$

Define

$$
\mathfrak X_{U,V}(N,H;c)
=
\frac{H}{N}
\int_{-c}^{c}
\mathcal H_{U,V;W}(N,y)
\overline{
\mathcal S_W(N,y)
}
dy.
$$

Smoothness of $W$ gives rapid decay of $G_\rho$ in $|\Im\rho|$, so logarithmic-scale Hilbert orthogonality applies.

Therefore:

## Theorem 10.1 — Renormalized Vaughan / prime-error log-scale anti-alignment

$$
\boxed{
\begin{aligned}
&
\lim_{T\to\infty}
\frac1T
\int_0^T
\frac{
\mathfrak X_{U,V}
\left(
e^t,e^{(1-\tau)t};c
\right)
}{
e^{(1-\tau)t}
e^{(2\Theta-1)t}
}
dt
\\
&\qquad
=
-
\sum_{\substack{\rho:\Re\rho=\Theta}}
m_\rho^2
\|G_\rho\|_{L^2(-c,c)}^2
<0.
\end{aligned}
}
$$

Create:

```text
B-RH-127
RIGHTMOST_ZERO_MODES_OF_THE_RENORMALIZED_VAUGHAN_COEFFICIENT_AND_PRIME_ERROR_ARE_LOG_SCALE_ANTI_ALIGNED
CERTIFIED_IF_RIGHTMOST_ABSCISSA_IS_ATTAINED
```

Thus the boundary diagonal is not removed by the Vaughan renormalization.

---

# 11. Critical exponent

The cross-Gram boundary scale is

$$
H
N^{2\Theta-1}.
$$

Relative to the natural root scale

$$
NH,
$$

the saving exponent is

$$
\boxed{
2(1-\Theta).
}
$$

At a saturated PESC $(\kappa)$ boundary,

$$
\Theta
=
1-\frac{\kappa}{2},
$$

this equals

$$
\boxed{
\kappa.
}
$$

Therefore F-RH-024 asks for a strict fixed-power improvement over an explicitly present boundary diagonal.

That is genuine horizontal zero-strip progress.

---

# 12. Titchmarsh/divisor-shift calibration

Power-saving shifted-convolution theorems are available for many dense divisor-like coefficients.

For example, Drappeau obtains power-saving errors in Titchmarsh-divisor problems using Kloosterman-sum dispersion; in the prime-times-divisor case a fixed-power error is obtained under GRH for Dirichlet $L$ -functions.

Uniform Titchmarsh variants also exploit divisor or automorphic structure.

These results demonstrate that a factorized coefficient can be analytically easier than a second prime.

But $h_{U,V}$ is spectrally different from $\tau$ or a generic divisor coefficient:

$$
H_{U,V}(s)
$$

contains a universal pole at every nontrivial zeta zero.

Therefore a direct transfer of existing prime-times-divisor power-saving theorems is not justified.

External calibration:

- Drappeau, *Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method*;
- Assing–Blomer–Li, *Uniform Titchmarsh divisor problems*.

---

# 13. Shifted-prime factor-anatomy calibration

Ford's shifted-prime Kubilius model proves a total-variation approximation between the small prime factors of shifted primes and an independent probabilistic model.

Theorem 1 gives

$$
d_{\rm TV}
\ll
e^{-\alpha u\log u}
+
(\log x)^{-A},
$$

where

$$
u=
\frac{\log x}{\log y}.
$$

For the error to tend rapidly to zero from the first term, one needs

$$
u\to\infty,
$$

equivalently

$$
\boxed{
y=x^{o(1)}.
}
$$

The paper explicitly states that the distribution of the large prime factors of shifted primes is not well understood.

F-RH-024 instead contains balanced polynomial factors

$$
e\asymp N^\theta,
$$

$$
k\asymp N^{1-\theta}.
$$

Thus current shifted-prime anatomy results do not control the decisive balanced range.

Create:

```text
O-RH-175
CURRENT_SHIFTED_PRIME_KUBILIUS_TRANSFERENCE_CONTROLS_SMALL_FACTORS_BUT_NOT_THE_POLYNOMIAL_BALANCED_FACTORS_REQUIRED_BY_F_RH_024
CERTIFIED_EXTERNAL_SCOPE_BARRIER
```

---

# 14. Consequence for Campaign 47

Paper 77 solved the extraction problem.

Paper 78 now shows that extraction does not spectrally soften the root.

The next arithmetic theorem must therefore exploit the **specific coefficient realization**

$$
c_{U,V}(n)
=
\sum_{\substack{ek=n\\e>V\\k>U}}
\Lambda(e)b_U(k),
$$

not merely its mean, Fourier norm, or generic divisor-boundedness.

In particular:

```text
DO NOT:
  optimize U,V hoping to remove the zero pole;
  apply a generic prime-times-divisor theorem;
  replace balanced polynomial factorization by small-factor anatomy.

DO:
  dyadically decompose e and k;
  derive the exact dyadic portion of the counterterm;
  identify which balanced factor ranges carry the universal zero-pole mass;
  search for ordinary-factorization cancellation specifically in those ranges.
```

---

# 15. State transition

Advance candidate state

$$
v1.68
\to
v1.69.
$$

Add:

```text
B-RH-123
PAPER77_SCALAR_COUNTERTERM_IS_A_COEFFICIENTWISE_LOG_AFFINE_RENORMALIZATION

B-RH-124
RENORMALIZED_VAUGHAN_COEFFICIENT_REMOVES_THE_COMPLETE_S1_PRINCIPAL_PART

B-RH-125
RENORMALIZED_VAUGHAN_COEFFICIENT_PRESERVES_EVERY_NONTRIVIAL_ZETA_ZERO_WITH_UNIVERSAL_OPPOSITE_PRIME_RESIDUE

B-RH-126
ALL_VAUGHAN_PARAMETER_CHOICES_SHARE_THE_SAME_PARAMETER_INVARIANT_ZETA_PRIME_HARD_CORE

B-RH-127
RIGHTMOST_ZERO_MODES_OF_THE_RENORMALIZED_VAUGHAN_COEFFICIENT_AND_PRIME_ERROR_ARE_LOG_SCALE_ANTI_ALIGNED

O-RH-175
CURRENT_SHIFTED_PRIME_KUBILIUS_TRANSFERENCE_CONTROLS_SMALL_FACTORS_BUT_NOT_THE_POLYNOMIAL_BALANCED_FACTORS_REQUIRED_BY_F_RH_024
```

F-RH-024 remains open and preferred.

No RH certificate is created.

---

# 16. Recommended next action

The next round should derive a dyadic decomposition

$$
e\asymp E,
\qquad
k\asymp K,
\qquad
EK\asymp N,
$$

of

$$
c_{U,V}(n)
$$

and a matching dyadic partition of the coefficientwise counterterm

$$
q_{U,V}(n).
$$

The goal is to identify the smallest set of polynomial factor exponents

$$
\theta=\frac{\log E}{\log N}
$$

which can carry the universal rightmost-zero pole.

If the pole mass can be forced into a restricted balanced range, that range becomes the next explicit Campaign-47 arithmetic target.

If every polynomial range can independently carry it, the factorization route reaches a stronger distributed parity wall.

---

# 17. Conclusion

Vaughan renormalization removes the complete main pole at $s=1$.

It removes none of the nontrivial zeta-zero poles.

Every parameter choice shares the same $\zeta'/\zeta$ hard core.

The balanced coefficient is therefore not a generic divisor coefficient; it is a composite-supported arithmetic realization of the opposite prime zero spectrum.

This explains both the promise and the difficulty of F-RH-024.

The next progress must come from the ordinary polynomial factorization itself.
