# CSM_RH Paper 81

## Nonlinear Screening: Moment-Degree Invariance, Gaussian Scale Neutrality, and a Frequency-Resolved Fourth-Cumulant Candidate

**Project:** CSM_RH  
**Paper:** 81  
**Version:** v0.1  
**Date:** 2026-09-09  
**New branch:** `NONLINEAR_MULTI_COPY_ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Entry state:** v1.71 / Paper 80 v0.1  
**Status:** GENERIC EVEN-MOMENT AMPLIFICATION REJECTED / MULTISCALE LOW-RANK DETERMINANT REJECTED AS BOUNDARY-BLIND / FREQUENCY-RESOLVED CONNECTED FOURTH TENSOR PASSES BOUNDARY SCREEN  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 80 closed the linear Vaughan/Buchstab branch and imposed a new screening rule:

> a new transform should be rejected if its hard coefficient is merely a nonzero copy of the prime-error pole projector plus a zero-pole-free correction.

The present paper begins the nonlinear / multi-copy search.

It first proves a general **moment-degree law** showing that ordinary even moments do not improve the PESC exponent geometry.

Let

$$
U_H(x)
=
\psi(x+H)-\psi(x)-H
$$

with

$$
H=X^{1-\tau}.
$$

For even

$$
q\ge2,
$$

define

$$
\boxed{
M_q(X,H)
=
\int_X^{2X}
|U_H(x)|^qdx.
}
$$

Suppose

$$
\boxed{
M_q(X,H)
\ll
XH^q
X^{-s+o(1)}.
}
$$

The short-difference mean-value forcing used in Papers 60–61 implies that a zeta zero

$$
\rho=\beta+i\gamma
$$

forces, along an unbounded sequence of $X$,

$$
\boxed{
\int_X^{2X}
|U_H(x)|dx
\gg_\rho
H X^\beta
X^{-o(1)}.
}
$$

Hölder gives

$$
\left(
\int|U_H|
\right)^q
\le
X^{q-1}
M_q.
$$

Hence

$$
XH^q
X^{-q(1-\beta)-o(1)}
\ll
M_q.
$$

Comparing with the upper bound yields

$$
\boxed{
\beta
\le
1-\frac{s}{q}.
}
$$

Therefore an even-moment saving exponent $s$ implies every PESC exponent

$$
\boxed{
\kappa'
<
\frac{2s}{q}.
}
$$

If PESC $(\kappa)$ is saturated at

$$
\beta=1-\frac{\kappa}{2},
$$

the moment-critical exponent is

$$
\boxed{
s_{\rm crit}(q)
=
\frac q2\kappa.
}
$$

Thus taking more copies simply multiplies the boundary exponent by the number of copies.

There is no exponent amplification from the degree itself.

The same conclusion appears from the conjectural Gaussian prime model.

Montgomery and Soundararajan's singular-series analysis predicts, under the corresponding Hardy–Littlewood input,

$$
\boxed{
M_q(X,H)
\asymp
X
\left(
H\log(X/H)
\right)^{q/2}
}
$$

for even $q$ in polynomial short-interval ranges.

Relative to $XH^q$, the Gaussian saving exponent is

$$
\boxed{
s_{\rm Gauss}(q)
=
\frac q2
(1-\tau).
}
$$

Therefore

$$
s_{\rm Gauss}(q)>s_{\rm crit}(q)
$$

is equivalent for **every even $q$** to

$$
\boxed{
1-\tau>\kappa.
}
$$

The ideal Gaussian geometry of every raw even moment therefore has exactly the same PESC scale gate as the second moment.

This rejects generic higher even moments as a new Campaign-level amplifier.

The local higher-correlation arithmetic is nevertheless highly developed.

Montgomery and Soundararajan proved for the refined singular-series sums

$$
R_k(h)
$$

that

$$
\boxed{
R_k(h)
=
\mu_k
\left(
-h\log h+Ah
\right)^{k/2}
+
O_{k,\varepsilon}
\left(
h^{k/2-1/(7k)+\varepsilon}
\right)
}
$$

for even $k$.

In particular,

$$
\boxed{
R_4(h)
=
3
\left(
-h\log h+Ah
\right)^2
+
O_\varepsilon
\left(
h^{2-1/28+\varepsilon}
\right).
}
$$

Thus the **local singular-series fourth connected defect** is already power-smaller than the Gaussian Wick main term.

Bloom and Kuperberg's 2025 work additionally gives near-optimal upper bounds for odd refined-singular-series moments, confirming that local higher-moment arithmetic is substantially better understood than the actual prime-tuple error terms.

This suggests that the only nonlinear quantity worth keeping is not a raw higher moment but a **connected cumulant**, where Gaussian pairings are removed.

However, the scalar fourth cumulant is not sufficiently robust as a root detector.

For a single conjugate boundary pair,

$$
Z(t)
=
A e^{i\gamma t}
+
\overline A e^{-i\gamma t},
$$

one has

$$
\boxed{
\operatorname{Cum}_4(Z)
=
\mathbb E Z^4
-
3
\left(
\mathbb E Z^2
\right)^2
=
-6|A|^4.
}
$$

So a single boundary mode is visible.

But with several rightmost zero ordinates, additive relations among ordinates can produce extra scalar fourth-moment resonances.

A scalar cumulant may therefore suffer accidental cancellation.

The paper resolves this by passing to a **frequency-resolved connected fourth tensor**.

Let

$$
F(t)
=
\sum_{\lambda\ne0}
a_\lambda e^{i\lambda t},
\qquad
a_{-\lambda}
=
\overline{a_\lambda},
$$

be an absolutely summable almost-periodic boundary signal.

Define the stationary two-point function

$$
C_2(u)
=
\mathbb M_t
F(t)F(t+u)
$$

and the four-point function

$$
C_4(u_1,u_2,u_3)
=
\mathbb M_t
F(t)
F(t+u_1)
F(t+u_2)
F(t+u_3).
$$

Define the connected tensor

$$
\boxed{
\begin{aligned}
K_4(u_1,u_2,u_3)
&=
C_4(u_1,u_2,u_3)
\\
&\quad
-
C_2(u_1)
C_2(u_3-u_2)
\\
&\quad
-
C_2(u_2)
C_2(u_3-u_1)
\\
&\quad
-
C_2(u_3)
C_2(u_2-u_1).
\end{aligned}
}
$$

Consider its Fourier coefficient in the lag variables at

$$
\boxed{
(\lambda,\lambda,-\lambda).
}
$$

There is exactly one fourth-order frequency assignment:

$$
(-\lambda,\lambda,\lambda,-\lambda).
$$

The raw four-point coefficient is

$$
|a_\lambda|^4.
$$

Exactly two Wick pairings contribute at the same lag-frequency triple, each with coefficient

$$
|a_\lambda|^4.
$$

The third pairing contributes at a different lag-frequency triple.

Therefore:

## Self-frequency fourth-cumulant identity

$$
\boxed{
\widehat K_4
(\lambda,\lambda,-\lambda)
=
-|a_\lambda|^4.
}
$$

This coefficient is independent of all additive relations involving other frequencies.

Thus every nonzero rightmost-zero mode has a universal negative self-frequency fourth-cumulant atom.

The connected tensor is therefore a robust nonlinear boundary detector.

This is the first nonlinear candidate to pass the Paper-80 screening rule.

By contrast, a multi-scale wedge or determinant built from two linear responses is **boundary-blind at leading order**.

A single rightmost zero gives a rank-one complex response vector across linear test weights or scales.

Its exterior square vanishes.

Thus smallness of such a determinant cannot exclude the zero; the determinant has deleted the very boundary mode that must be forced.

The paper rejects this route before developing it further.

The arithmetic challenge for the connected fourth tensor is now explicit.

A local short-interval expansion requires genuine four-copy prime correlations.

The local singular-series Wick part is power-controlled by the Montgomery–Soundararajan $R_4$ theorem.

What remains is the actual connected four-prime residual beyond the refined singular series.

Current higher-uniformity theorems, including the 2026 Matomäki–Radziwiłł–Shao–Tao–Teräväinen work, provide very strong logarithmic control for Hardy–Littlewood systems with one averaged variable, but do not supply the fixed-power connected four-prime residual required to beat a saturated PESC boundary.

Open:

```text
F-RH-026
FREQUENCY_RESOLVED_CONNECTED_FOUR_PRIME_CUMULANT_POWER
```

The desired theorem must:

1. construct an arithmetic incarnation of the connected lag tensor whose rightmost-zero self-frequency coefficient is $-|a_\gamma|^4$ ;
2. subtract all pair/Wick terms exactly;
3. retain the Montgomery–Soundararajan singular-series connected main separately;
4. prove a fixed-power bound for the actual four-prime connected residual;
5. beat the degree-four boundary threshold

$$
\boxed{
2\kappa.
}
$$

Unlike a raw fourth moment, F-RH-026 is not automatically neutralized by Gaussian pairings.

Unlike a scalar cumulant, it is not vulnerable to additive relations among zero ordinates.

Whether ordinary prime arithmetic can control this frequency-resolved connected tensor more efficiently than the pair residual is open.

No RH theorem is claimed.

---

# 1. General even-moment forcing

Let

$$
q\ge2
$$

be even.

Suppose a zero

$$
\rho=\beta+i\gamma
$$

exists.

The short-difference lower forcing inherited from the Pintz mean-value mechanism gives

$$
\boxed{
\|U_H\|_{L^1(X,2X)}
\gg_\rho
H X^\beta
X^{-o(1)}.
}
$$

By Hölder,

$$
\|U_H\|_1
\le
X^{1-1/q}
\|U_H\|_q.
$$

Therefore:

## Theorem 1.1 — $L^q$ boundary lower scale

$$
\boxed{
M_q(X,H)
\gg_\rho
XH^q
X^{-q(1-\beta)-o(1)}.
}
$$

Create:

```text
B-RH-139
A_ZETA_ZERO_FORCES_THE_QTH_SHORT_INTERVAL_MOMENT_AT_EXPONENT_Q_TIMES_ONE_MINUS_BETA
CERTIFIED_FROM_PINTZ_PLUS_HOLDER
```

---

# 2. Moment upper exponent to zero strip

Assume

$$
M_q(X,H)
\ll
XH^q
X^{-s+o(1)}.
$$

Theorem 1.1 gives

$$
q(1-\beta)\ge s.
$$

Hence:

## Theorem 2.1 — Moment-degree zero-strip map

$$
\boxed{
\beta_*
\le
1-\frac{s}{q}.
}
$$

Equivalently,

$$
\boxed{
\operatorname{PESC}(\kappa')
}
$$

holds for every

$$
\boxed{
\kappa'
<
\frac{2s}{q}.
}
$$

Create:

```text
B-RH-140
QTH_MOMENT_POWER_SAVING_MAPS_TO_PESC_EXPONENT_TWO_S_OVER_Q
CERTIFIED
```

---

# 3. Seed-critical moment exponent

If PESC $(\kappa)$ is saturated,

$$
\beta_*
=
1-\frac{\kappa}{2}.
$$

Theorem 1.1 then gives the critical saving exponent

$$
\boxed{
s_{\rm crit}(q)
=
q
\left(
1-\beta_*
\right)
=
\frac q2\kappa.
}
$$

Thus strict amplification from a raw $q$ th moment requires

$$
\boxed{
s>\frac q2\kappa.
}
$$

Create:

```text
O-RH-179
RAW_HIGHER_MOMENTS_MULTIPLY_THE_SEED_THRESHOLD_BY_THE_COPY_DEGREE_AND_DO_NOT_CREATE_A_FREE_EXPONENT_GAIN
CERTIFIED
```

---

# 4. Gaussian moment scale

For a centered Gaussian variable of variance

$$
\sigma_H^2
\asymp
H\log(X/H),
$$

the even $q$ th moment is

$$
\mu_q
\sigma_H^q.
$$

Hence the conjectural short-interval prime moment is

$$
\boxed{
M_q^{\rm Gauss}
\asymp
X
\left(
H\log(X/H)
\right)^{q/2}.
}
$$

Relative to

$$
XH^q,
$$

$$
\boxed{
s_{\rm Gauss}(q)
=
\frac q2
(1-\tau)
}
$$

at fixed-power resolution.

Thus:

## Corollary 4.1 — Moment-degree scale neutrality

$$
\boxed{
s_{\rm Gauss}(q)
>
s_{\rm crit}(q)
}
$$

if and only if

$$
\boxed{
1-\tau>\kappa.
}
$$

The condition is independent of $q$.

Create:

```text
B-RH-141
ALL_GAUSSIAN_EVEN_MOMENTS_HAVE_THE_SAME_PESC_SCALE_GATE_AS_THE_SECOND_MOMENT
CERTIFIED
```

---

# 5. Montgomery–Soundararajan local fourth structure

Let

$$
\mathfrak S_0(\mathcal D)
$$

be the refined singular series and

$$
R_k(h)
=
\sum_{\substack{1\le d_1,\ldots,d_k\le h\\d_i\ {\rm distinct}}}
\mathfrak S_0(\{d_1,\ldots,d_k\}).
$$

Montgomery and Soundararajan prove for even $k$

$$
\boxed{
R_k(h)
=
\mu_k
\left(
-h\log h+Ah
\right)^{k/2}
+
O_{k,\varepsilon}
\left(
h^{k/2-1/(7k)+\varepsilon}
\right).
}
$$

For $k=4$:

$$
\boxed{
R_4(h)
=
3
\left(
-h\log h+Ah
\right)^2
+
O_\varepsilon
\left(
h^{2-1/28+\varepsilon}
\right).
}
$$

Create:

```text
B-RH-142
THE_LOCAL_REFINED_SINGULAR_SERIES_FOURTH_MOMENT_HAS_A_POWER_SMALL_CONNECTED_DEFECT_AFTER_WICK_SUBTRACTION
CERTIFIED_EXTERNAL_THEOREM
```

This is a theorem about the local Hardy–Littlewood model, not the actual four-prime error.

---

# 6. Recent odd-moment calibration

Bloom and Kuperberg prove for every odd

$$
k\ge3
$$

the near-optimal bound

$$
\boxed{
R_k(h)
\ll
h^{(k-1)/2}
(\log h)^{O(1)}.
}
$$

This improves the older exponent

$$
k/2-1/(7k)
$$

for odd $k$ and confirms the conjectured power of $h$.

Thus both even Wick structure and odd lower-order local structure are sharply understood at the singular-series level.

The remaining difficulty is the actual prime-tuple residual.

---

# 7. Scalar fourth cumulant boundary test

Let

$$
Z(t)
=
A e^{i\gamma t}
+
\overline A e^{-i\gamma t}.
$$

Long averaging gives

$$
\mathbb E Z^2
=
2|A|^2,
$$

and

$$
\mathbb E Z^4
=
6|A|^4.
$$

Hence

$$
\boxed{
\operatorname{Cum}_4(Z)
=
-6|A|^4.
}
$$

So a single conjugate boundary pair is non-Gaussian at fourth order.

But a scalar fourth cumulant is not adopted as the canonical root observable because multiple rightmost zero frequencies may satisfy additive relations which contribute extra zero-frequency quartets.

---

# 8. Connected fourth lag tensor

Let

$$
F(t)
=
\sum_{\lambda\ne0}
a_\lambda e^{i\lambda t}
$$

with

$$
a_{-\lambda}
=
\overline{a_\lambda}.
$$

Define the Besicovitch mean

$$
\mathbb M_t.
$$

Set

$$
C_2(u)
=
\mathbb M_t
F(t)F(t+u),
$$

and

$$
C_4(u_1,u_2,u_3)
=
\mathbb M_t
F(t)
F(t+u_1)
F(t+u_2)
F(t+u_3).
$$

Define

$$
\boxed{
\begin{aligned}
K_4(u_1,u_2,u_3)
&=
C_4(u_1,u_2,u_3)
\\
&\quad
-C_2(u_1)C_2(u_3-u_2)
\\
&\quad
-C_2(u_2)C_2(u_3-u_1)
\\
&\quad
-C_2(u_3)C_2(u_2-u_1).
\end{aligned}
}
$$

This is the stationary connected fourth correlation.

---

# 9. Universal self-frequency cumulant atom

Fix

$$
\lambda\ne0.
$$

Consider the lag-frequency triple

$$
(\lambda,\lambda,-\lambda).
$$

In $C_4$, the corresponding frequency assignment is uniquely

$$
(-\lambda,\lambda,\lambda,-\lambda),
$$

and contributes

$$
|a_\lambda|^4.
$$

The pairing

$$
(0,1)(2,3)
$$

contributes

$$
|a_\lambda|^4.
$$

The pairing

$$
(0,2)(1,3)
$$

also contributes

$$
|a_\lambda|^4.
$$

The pairing

$$
(0,3)(1,2)
$$

does not contribute at this lag-frequency triple.

Therefore:

## Theorem 9.1 — Universal fourth-cumulant self atom

$$
\boxed{
\widehat K_4
(\lambda,\lambda,-\lambda)
=
-|a_\lambda|^4.
}
$$

Create:

```text
B-RH-143
EVERY_BOUNDARY_FREQUENCY_HAS_A_UNIVERSAL_NONZERO_SELF_ATOM_IN_THE_CONNECTED_FOURTH_LAG_TENSOR
CERTIFIED
```

No assumption about additive relations among distinct frequencies is required.

---

# 10. Rejection of multi-scale wedge determinants

Suppose a linear family of test transforms has a single boundary-mode response

$$
v\,e^{i\gamma t}.
$$

Its complex covariance contribution is rank one:

$$
vv^*.
$$

Any exterior-square / determinant statistic designed to vanish on rank-one components therefore removes the leading boundary mode.

Such a statistic may measure additional noise, but smallness of the determinant cannot exclude the boundary zero.

Create:

```text
O-RH-180
LOW_RANK_MULTISCALE_DETERMINANTS_ARE_BOUNDARY_BLIND_AT_LEADING_ORDER
CERTIFIED_AS_SCREENING_BARRIER
```

---

# 11. Arithmetic fourth connected residual

For the short-interval prime field

$$
\Lambda_0(n)=\Lambda(n)-1,
$$

define the distinct-shift four-prime residual

$$
\boxed{
\begin{aligned}
\mathcal E_4(N,H)
&=
\sum_{\substack{1\le h_1,\ldots,h_4\le H\\h_i\ {\rm distinct}}}
\Bigg[
\sum_{n\le N}
\prod_{j=1}^4
\Lambda_0(n+h_j)
\\
&\qquad\qquad
-
N
\mathfrak S_0
(\{h_1,h_2,h_3,h_4\})
\Bigg].
\end{aligned}
}
$$

This is the actual four-prime error after the local refined singular series is removed.

The local sum of the singular series has Gaussian/Wick main plus the power-small error in Section 5.

No fixed-power theorem of the size required below is known for $\mathcal E_4$.

---

# 12. Degree-four root threshold

A saturated PESC $(\kappa)$ boundary has short-interval amplitude

$$
H X^{-\kappa/2}
$$

per copy.

Four copies therefore have critical scale

$$
\boxed{
XH^4X^{-2\kappa}.
}
$$

Hence a robust connected fourth-order arithmetic theorem would need a saving strictly beyond

$$
\boxed{
2\kappa.
}
$$

This is the nonlinear analogue of the pair-residual threshold $\kappa$.

Taking four copies has not lowered the horizontal cost.

---

# 13. New frontier F-RH-026

Open:

```text
F-RH-026
FREQUENCY_RESOLVED_CONNECTED_FOUR_PRIME_CUMULANT_POWER
```

The target is not merely

$$
\mathcal E_4
\ll
NH^4N^{-2\kappa-\eta}.
$$

The root-safe form must retain the connected lag-frequency information which isolates the universal self atom

$$
-|a_\gamma|^4.
$$

A future precise arithmetic formulation should:

1. use four copies of the short-interval prime error;
2. subtract all three Wick pairings;
3. introduce enough scale/lag modulation to resolve the self-frequency atom;
4. separate the local singular-series connected term;
5. prove a fixed-power upper smaller than the boundary self atom.

The exact local arithmetic theorem is not yet known.

---

# 14. Current technology calibration

Matomäki, Radziwiłł, Shao, Tao and Teräväinen prove 2026 higher-uniformity and Hardy–Littlewood results with one short averaged variable for the von Mangoldt function, Möbius function and divisor functions.

Their quantitative prime/Möbius conclusions in the relevant difficult components are of arbitrary logarithmic-saving type rather than the fixed-power connected four-prime residual demanded by F-RH-026.

Thus current higher-uniformity technology does not immediately cross the degree-four boundary threshold.

---

# 15. Nonlinear screening verdict

The first nonlinear screening gives:

```text
RAW EVEN MOMENTS:
REJECTED AS EXPONENT-NEUTRAL.

MULTISCALE WEDGE / DETERMINANT:
REJECTED AS BOUNDARY-BLIND.

SCALAR FOURTH CUMULANT:
BOUNDARY-VISIBLE BUT NOT ROBUST TO ZERO-ORDINATE ADDITIVE RELATIONS.

FREQUENCY-RESOLVED CONNECTED FOURTH TENSOR:
PASSES THE BOUNDARY SCREEN.
```

Only the last candidate advances.

---

# 16. State transition

Advance candidate state

$$
v1.71
\to
v1.72.
$$

Add:

```text
B-RH-139
A_ZETA_ZERO_FORCES_THE_QTH_SHORT_INTERVAL_MOMENT_AT_EXPONENT_Q_TIMES_ONE_MINUS_BETA

B-RH-140
QTH_MOMENT_POWER_SAVING_MAPS_TO_PESC_EXPONENT_TWO_S_OVER_Q

B-RH-141
ALL_GAUSSIAN_EVEN_MOMENTS_HAVE_THE_SAME_PESC_SCALE_GATE_AS_THE_SECOND_MOMENT

B-RH-142
THE_LOCAL_REFINED_SINGULAR_SERIES_FOURTH_MOMENT_HAS_A_POWER_SMALL_CONNECTED_DEFECT_AFTER_WICK_SUBTRACTION

B-RH-143
EVERY_BOUNDARY_FREQUENCY_HAS_A_UNIVERSAL_NONZERO_SELF_ATOM_IN_THE_CONNECTED_FOURTH_LAG_TENSOR

O-RH-179
RAW_HIGHER_MOMENTS_MULTIPLY_THE_SEED_THRESHOLD_BY_THE_COPY_DEGREE_AND_DO_NOT_CREATE_A_FREE_EXPONENT_GAIN

O-RH-180
LOW_RANK_MULTISCALE_DETERMINANTS_ARE_BOUNDARY_BLIND_AT_LEADING_ORDER
```

Open:

```text
F-RH-026
FREQUENCY_RESOLVED_CONNECTED_FOUR_PRIME_CUMULANT_POWER
OPEN_NONLINEAR_ROOT_CANDIDATE
```

No RH certificate is created.

---

# 17. External calibration

## 17.1. Montgomery–Soundararajan

H. L. Montgomery and K. Soundararajan,
*Primes in short intervals*,
Communications in Mathematical Physics 252 (2004), 589–617.

Their refined singular-series moment theorem gives Gaussian even main terms and the power error

$$
h^{k/2-1/(7k)+\varepsilon}.
$$

URL:

https://arxiv.org/abs/math/0409258

## 17.2. Bloom–Kuperberg, 2025

T. F. Bloom and V. Kuperberg,
*Odd moments and adding fractions*,
Proceedings of the London Mathematical Society 131 (2025).

They prove for odd $k\ge3$

$$
R_k(h)
\ll
h^{(k-1)/2}
(\log h)^{O(1)}.
$$

URL:

https://doi.org/10.1112/plms.70068

## 17.3. MRSTT, 2026

K. Matomäki, M. Radziwiłł, X. Shao, T. Tao and J. Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*,
Inventiones Mathematicae 244 (2026), 967–1091.

The paper proves higher-uniformity and averaged Hardy–Littlewood results in short intervals, providing the current technology calibration for actual higher prime correlations.

URL:

https://doi.org/10.1007/s00222-026-01408-6

---

# 18. Recommended next action

Do not try to prove a raw fourth-moment theorem.

The next round should construct an **arithmetic realization of the connected lag tensor**.

The first goal is an exact identity, analogous to Paper 77:

```text
four-prime connected tensor
=
local refined-singular-series connected tensor
+
actual connected residual.
```

Then introduce a Mellin/log-scale modulation which resolves the spectral coefficient

$$
(\gamma,\gamma,-\gamma)
$$

without knowing $\gamma$ in advance, most likely by taking an $L^2$ norm over lag frequencies.

Only after a positive frequency-resolved boundary lower theorem is certified should a new fixed-power arithmetic axiom be stated.

---

# 19. Conclusion

Nonlinearity alone does not create an exponent amplifier.

Raw higher moments preserve the same per-copy zero-strip geometry as the second moment.

Low-rank determinant constructions erase the leading boundary signal and are therefore unsuitable.

The first genuinely different multi-copy object is the connected fourth-correlation tensor.

Its self-frequency coefficient remembers every boundary mode with universal weight $-|a_\lambda|^4$ and is immune to additive relations among distinct zero ordinates.

The arithmetic realization of that tensor is the next problem.
