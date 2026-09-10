# CSM_RH Paper 82

## Collapse of the Frequency-Resolved Fourth Self-Atom to the Two-Point Spectrum and the Single-Boundary-Pair Polynomial Barrier

**Project:** CSM_RH  
**Paper:** 82  
**Version:** v0.1  
**Date:** 2026-09-09  
**Branch:** `NONLINEAR_MULTI_COPY_ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Entry state:** v1.72 / Paper 81 v0.1  
**Status:** F-RH-026 SELF-DIAGONAL REALIZATION COMPLETED / POSITIVE DEGREE-FOUR PROJECTOR CERTIFIED / SELF-DIAGONAL COLLAPSES EXACTLY TO SECOND-ORDER SPECTRAL DATA / PURE FINITE-DEGREE SINGLE-FIELD MULTI-COPY ROUTE SCREENED OUT  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 81 found that raw even moments are exponent-neutral and that low-rank determinants erase the leading boundary mode.

It retained one nonlinear candidate: the frequency-resolved connected fourth lag tensor

$$
K_4(u_1,u_2,u_3),
$$

whose self-frequency coefficient satisfies

$$
\widehat K_4(\lambda,\lambda,-\lambda)
=
-|a_\lambda|^4.
$$

The present paper answers two questions left open there:

1. Can all unknown boundary frequencies be captured by a positive fourth-order functional without squaring the tensor and thereby raising the degree to eight?
2. Does this positive connected-fourth detector contain genuinely new spectral information beyond the two-point covariance?

The answer to the first question is yes.

The answer to the second is no.

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

be a real Besicovitch almost-periodic field with absolutely summable spectrum.

Define

$$
C_2(u)
=
\mathbb M_t
F(t)F(t+u)
$$

and the connected fourth tensor $K_4$ as in Paper 81.

Define the **negative diagonal connected spectral mass**

$$
\boxed{
\mathfrak D_4(F)
=
-
\sum_{\lambda\ne0}
\widehat K_4
(\lambda,\lambda,-\lambda).
}
$$

Paper 81's self-atom identity gives immediately

$$
\boxed{
\mathfrak D_4(F)
=
\sum_{\lambda\ne0}
|a_\lambda|^4
\ge0.
}
$$

Thus $\mathfrak D_4$ is a positive degree-four functional which detects every unknown boundary frequency simultaneously.

No knowledge of $\gamma$ is required.

No eighth-degree squaring is required.

However,

$$
\boxed{
C_2(u)
=
\sum_{\lambda\ne0}
|a_\lambda|^2e^{-i\lambda u}.
}
$$

Parseval in the lag variable gives the exact identity

$$
\boxed{
\mathfrak D_4(F)
=
\mathbb M_u
|C_2(u)|^2.
}
$$

Therefore the robust frequency-resolved connected-fourth self detector is **exactly the $L^2$ concentration of the two-point spectrum**.

It is not independent four-point spectral information.

This gives a correction to the strategic interpretation of F-RH-026.

The Montgomery–Soundararajan refined singular-series fourth connected defect is a genuinely four-prime local arithmetic object.

But its natural coordinates are the four additive shifts inside one short interval.

The spectral self atom $-|a_\lambda|^4$ of Paper 81 lives in the Fourier variable of the **logarithmic scale field** which resolves zeta ordinates.

These are different coordinates.

The local $R_4(h)$ theorem therefore does not directly estimate $\mathfrak D_4$.

To resolve a zeta ordinate $\gamma$ one must retain multiplicative-scale or Mellin information.

Once this is done, the universal self-frequency fourth detector collapses to a functional of $C_2$.

The paper proves a stronger screening theorem using the logically minimal RH-failure model.

Suppose the rightmost boundary consists of a single conjugate pair

$$
\Theta\pm i\gamma.
$$

After normalization, the boundary field is

$$
\boxed{
F(t)
=
A e^{i\gamma t}
+
\overline A e^{-i\gamma t}.
}
$$

Its two-point function is

$$
\boxed{
C_2(u)
=
2|A|^2
\cos(\gamma u).
}
$$

This already determines both:

- the amplitude $|A|$ ;
- the spectral frequency $|\gamma|$.

Every stationary finite-dimensional polynomial statistic of $F$ is then determined by $C_2$.

In particular,

$$
\boxed{
\mathbb M_t
F(t)^{2m}
=
\binom{2m}{m}
|A|^{2m},
}
$$

and all odd scalar moments vanish.

More generally, every stationary multi-time moment

$$
\mathbb M_t
\prod_{j=1}^q
F(t+u_j)
$$

is a finite sum over sign assignments

$$
\varepsilon_j\in\{\pm1\}
$$

with

$$
\varepsilon_1+\cdots+\varepsilon_q=0,
$$

and is therefore an explicit polynomial in $|A|^2$ and phases

$$
e^{i\gamma(u_i-u_j)},
$$

all already encoded by $C_2$.

Hence all finite-degree stationary cumulants of a single boundary pair are algebraically determined by the two-point covariance.

This gives the **single-boundary-pair polynomial barrier**:

> A finite-degree polynomial multi-copy statistic of a single linear prime-error field may reorganize the arithmetic upper problem, but it cannot provide genuinely new universal spectral coercivity beyond the two-point boundary data, because RH can fail with only one conjugate rightmost zero pair.

This does not say that higher-order prime correlations are uninteresting or cannot be stronger arithmetically.

It says that the **root lower forcing** of a universal finite-degree polynomial detector is already contained in second-order spectral data in the minimal boundary model.

The exponent ledger agrees.

A degree-four self atom has size

$$
|A|^4.
$$

For a PESC $(\kappa)$ boundary,

$$
|A|
\asymp
X^{-\kappa/2}
$$

at normalized fixed-power resolution.

Therefore

$$
\boxed{
\mathfrak D_4
\asymp
X^{-2\kappa}.
}
$$

A bound

$$
\mathfrak D_4
\ll
X^{-s}
$$

forces

$$
\boxed{
\beta_*
\le
1-\frac{s}{4},
}
$$

equivalently every PESC exponent

$$
\boxed{
\kappa'
<
\frac{s}{2}.
}
$$

Thus the degree-four diagonal functional has exactly the same per-copy exponent geometry already found in Paper 81.

A genuinely connected off-diagonal fourth coefficient is not determined by $C_2$, but it is also not universally forced by the existence of a single conjugate boundary pair.

Therefore it cannot serve as a complete RH root detector by itself.

The paper closes F-RH-026 in its original self-frequency form:

```text
F-RH-026
FREQUENCY_RESOLVED_CONNECTED_FOUR_PRIME_CUMULANT_POWER

SELF-DIAGONAL VERSION:
CLOSED AS EXACTLY SECOND-SPECTRUM-REDUCIBLE.

GENUINE OFF-DIAGONAL FOURTH INFORMATION:
NOT UNIVERSALLY BOUNDARY-FORCED.
```

There is also an arithmetic coordinate mismatch.

Montgomery–Soundararajan's $R_4$ theorem controls additive four-shift local singular-series structure.

A boundary zero is resolved spectrally in $\log X$ or Mellin frequency.

A fourth tensor which retains $\gamma$ -resolution therefore correlates prime errors across multiplicative scales, not merely four additive offsets inside one interval.

The 2026 work of Leung on joint distributions of primes in multiple short intervals proves multivariate Gaussian behavior only under RH together with a linear-independence hypothesis.

Thus current multiscale Gaussian theory cannot be used as an unconditional root input.

The next branch should no longer search among pure finite-degree polynomial statistics of one linear prime-error field.

A candidate must introduce at least one additional arithmetic state not determined by the two-point prime-error spectrum.

Examples include:

- prime error coupled to an independent ordinary-factorization state;
- conditional factorization statistics given a prime event;
- non-polynomial Boolean / threshold observables;
- mixed additive–multiplicative constraints which are not polynomial functions of one linear prime-error transform.

Before such a candidate advances, it must pass a stronger novelty test:

```text
SINGLE-BOUNDARY-PAIR NOVELTY TEST

Evaluate the candidate on
F(t)=Ae^{iγt}+conj(A)e^{-iγt}.

If the candidate is algebraically determined
by C_2(u),
it is not a new spectral amplifier.
```

No RH theorem is claimed.

---

# 1. Finite cyclic model

The core identities are exact already on a finite odd cyclic group.

Let

$$
G=\mathbb Z/M\mathbb Z,
$$

with $M$ odd.

Let $x_t$ be a real zero-mean sequence.

Use the normalized Fourier transform

$$
\boxed{
a_k
=
\frac1M
\sum_{t\in G}
x_t
e^{-2\pi i kt/M}.
}
$$

Then

$$
x_t
=
\sum_{k\in G}
a_k
e^{2\pi i kt/M},
$$

and

$$
a_{-k}
=
\overline{a_k}.
$$

---

# 2. Two-point correlation

Define

$$
\boxed{
C_2(u)
=
\frac1M
\sum_{t\in G}
x_t x_{t+u}.
}
$$

Fourier expansion gives

$$
\boxed{
C_2(u)
=
\sum_{k\in G}
|a_k|^2
e^{-2\pi i ku/M}.
}
$$

Since $x$ has zero mean,

$$
a_0=0.
$$

---

# 3. Four-point connected tensor

Define

$$
C_4(u_1,u_2,u_3)
=
\frac1M
\sum_t
x_t
x_{t+u_1}
x_{t+u_2}
x_{t+u_3}.
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
-C_2(u_1)
C_2(u_3-u_2)
\\
&\quad
-C_2(u_2)
C_2(u_3-u_1)
\\
&\quad
-C_2(u_3)
C_2(u_2-u_1).
\end{aligned}
}
$$

This is the finite stationary fourth cumulant tensor.

---

# 4. Exact self-frequency coefficient

Let

$$
\widehat K_4(k_1,k_2,k_3)
$$

denote the normalized three-dimensional Fourier coefficient in the lag variables.

For

$$
k\ne0,
$$

Paper 81's combinatorics gives

$$
\boxed{
\widehat K_4(k,k,-k)
=
-|a_k|^4.
}
$$

Because $M$ is odd, there are no nonzero order-two frequencies which would create a special degeneracy.

---

# 5. Positive degree-four diagonal projector

Define

$$
\boxed{
\mathfrak D_4(x)
=
-\sum_{k\ne0}
\widehat K_4(k,k,-k).
}
$$

Then:

## Theorem 5.1 — Positive connected-fourth diagonal mass

$$
\boxed{
\mathfrak D_4(x)
=
\sum_{k\ne0}
|a_k|^4
\ge0.
}
$$

Create:

```text
B-RH-144
THE_NEGATIVE_DIAGONAL_SPECTRAL_MASS_OF_THE_CONNECTED_FOURTH_TENSOR_IS_A_POSITIVE_DEGREE_FOUR_BOUNDARY_DETECTOR
CERTIFIED
```

This solves the positivity problem without squaring $K_4$.

---

# 6. Exact collapse to the two-point spectrum

By Parseval applied to $C_2$,

$$
\boxed{
\frac1M
\sum_{u\in G}
|C_2(u)|^2
=
\sum_{k\in G}
|a_k|^4.
}
$$

Since $a_0=0$,

## Theorem 6.1 — Fourth diagonal / second-spectrum identity

$$
\boxed{
\mathfrak D_4(x)
=
\frac1M
\sum_u
|C_2(u)|^2.
}
$$

Create:

```text
B-RH-145
THE_ROBUST_CONNECTED_FOURTH_SELF_DIAGONAL_IS_EXACTLY_THE_L2_ENERGY_OF_THE_TWO_POINT_SPECTRUM
CERTIFIED
```

Thus the positive self-frequency detector contains no independent four-point spectral information.

---

# 7. Almost-periodic limit

Let

$$
F(t)
=
\sum_{\lambda\ne0}
a_\lambda e^{i\lambda t}
$$

with absolutely summable spectrum.

Then

$$
C_2(u)
=
\mathbb M_t
F(t)F(t+u)
=
\sum_\lambda
|a_\lambda|^2
e^{-i\lambda u}.
$$

Besicovitch Parseval gives

$$
\boxed{
\mathbb M_u
|C_2(u)|^2
=
\sum_\lambda
|a_\lambda|^4.
}
$$

The finite cyclic identity therefore converges to the continuous almost-periodic identity

$$
\boxed{
\mathfrak D_4(F)
=
\mathbb M_u
|C_2(u)|^2.
}
$$

---

# 8. Single conjugate boundary pair

Assume

$$
\boxed{
F(t)
=
A e^{i\gamma t}
+
\overline A e^{-i\gamma t}.
}
$$

Then

$$
\boxed{
C_2(u)
=
2|A|^2
\cos(\gamma u).
}
$$

In particular,

$$
C_2(0)=2|A|^2.
$$

The frequency of $C_2$ determines $|\gamma|$.

Hence $C_2$ determines the complete stationary law of the phase-averaged single-mode process.

---

# 9. All scalar moments are second-order determined

For $m\ge1$,

$$
F(t)^{2m}
$$

has a zero-frequency term only when exactly $m$ copies of $Ae^{i\gamma t}$ and $m$ copies of its conjugate are selected.

Therefore:

## Theorem 9.1 — Single-mode even moment formula

$$
\boxed{
\mathbb M_t
F(t)^{2m}
=
\binom{2m}{m}
|A|^{2m}.
}
$$

All odd scalar moments vanish.

Since

$$
|A|^2
=
\frac12C_2(0),
$$

every scalar moment is a polynomial in the two-point covariance.

---

# 10. All stationary multi-time polynomial moments are second-order determined

Consider

$$
\mathbb M_t
\prod_{j=1}^q
F(t+u_j).
$$

Each factor contributes a sign

$$
\varepsilon_j\in\{+1,-1\}.
$$

The $t$ -average vanishes unless

$$
\boxed{
\varepsilon_1+\cdots+\varepsilon_q=0.
}
$$

Every surviving term is

$$
|A|^q
e^{i\gamma
\sum_j
\varepsilon_j u_j}.
$$

The amplitude and the phase differences are determined by $C_2$.

Therefore:

## Theorem 10.1 — Single-boundary-pair polynomial sufficiency of $C_2$

Every stationary finite-degree polynomial moment and cumulant of a single conjugate boundary pair is algebraically determined by its two-point covariance.

Create:

```text
O-RH-181
A_SINGLE_CONJUGATE_BOUNDARY_PAIR_HAS_NO_INDEPENDENT_FINITE_DEGREE_STATIONARY_POLYNOMIAL_STATISTICS_BEYOND_C2
CERTIFIED
```

---

# 11. Root significance

A hypothetical failure of RH does not logically require many rightmost zeros.

A single conjugate pair

$$
\Theta\pm i\gamma
$$

is sufficient to create a rightmost off-critical boundary mode.

Therefore a universal RH root detector must detect the single-pair model.

Theorem 10.1 implies:

```text
finite-degree polynomial multi-copy statistics
of one linear prime-error field
do not create new universal spectral lower forcing
beyond the two-point covariance.
```

They may still reorganize the arithmetic upper problem, but the boundary coercivity is second-order-reducible.

---

# 12. Exponent map for the positive fourth diagonal

At a boundary zero

$$
\beta=1-d,
$$

the normalized linear amplitude is

$$
|A|
\asymp
X^{-d}.
$$

Thus

$$
\boxed{
\mathfrak D_4
\asymp
X^{-4d}.
}
$$

Since

$$
\kappa=2d,
$$

$$
\boxed{
\mathfrak D_4
\asymp
X^{-2\kappa}.
}
$$

If

$$
\mathfrak D_4
\ll
X^{-s+o(1)},
$$

then a boundary mode requires

$$
4(1-\beta)\ge s.
$$

Hence

$$
\boxed{
\beta_*
\le
1-\frac{s}{4},
}
$$

and every PESC exponent

$$
\boxed{
\kappa'
<
\frac{s}{2}
}
$$

follows.

This is exactly the degree-four specialization of Paper 81's moment-degree law.

---

# 13. Genuine off-diagonal fourth information is not universally forced

A connected fourth coefficient involving at least two distinct frequencies can contain information not determined by a single $C_2$ atom.

However, in the single conjugate boundary-pair model there are no independent distinct boundary frequencies.

Therefore such an off-diagonal coefficient may vanish while RH still fails.

Hence:

```text
genuinely new off-diagonal fourth information
cannot be the sole universal root forcing mechanism.
```

Create:

```text
O-RH-182
GENUINE_OFF_DIAGONAL_CONNECTED_FOURTH_INFORMATION_IS_NOT_UNIVERSALLY_FORCED_BY_A_SINGLE_BOUNDARY_PAIR
CERTIFIED_AS_ROOT_SCREEN
```

---

# 14. Coordinate mismatch with local four-prime arithmetic

Montgomery–Soundararajan's refined singular-series theorem controls the combinatorics of four **additive prime shifts** inside one short interval.

Its natural variables are

$$
h_1,h_2,h_3,h_4.
$$

The zeta ordinate $\gamma$ is resolved by Fourier analysis in

$$
t=\log X
$$

or by Mellin frequency.

A connected tensor which exactly isolates the self atom

$$
(\gamma,\gamma,-\gamma)
$$

therefore lives in multiplicative-scale coordinates.

It correlates prime errors across multiplicatively related scales.

This is not the same four-prime object as the local refined-singular-series $R_4$ theorem.

Thus:

```text
C-RH-008
PAPER81_OVERSTATED_THE_DIRECT_ARITHMETIC_LEVERAGE_OF_THE_LOCAL_R4_THEOREM_FOR_THE_LOG_SCALE_FREQUENCY_RESOLVED_SELF_ATOM
```

The $R_4$ theorem remains valuable local arithmetic, but it does not directly estimate $\mathfrak D_4$.

---

# 15. 2026 multiscale Gaussian calibration

Leung proves in 2026 that weighted prime counts in multiple short intervals have a multivariate Gaussian limiting distribution under:

- the Riemann hypothesis;
- a linear-independence hypothesis on zeta-zero ordinates.

This confirms that genuinely multiscale Gaussian behavior is deeply tied to the zero spectrum.

It cannot be used as an unconditional input to exclude the off-critical zero which the present campaign is trying to rule out.

External source:

Sun-Kai Leung,
*Joint distribution of primes in multiple short intervals*,
Advances in Mathematics 490 (2026), 110847.

---

# 16. F-RH-026 verdict

Update:

```text
F-RH-026
FREQUENCY_RESOLVED_CONNECTED_FOUR_PRIME_CUMULANT_POWER

SELF-DIAGONAL:
CLOSED AS SECOND-SPECTRUM-REDUCIBLE.

OFF-DIAGONAL:
NOT UNIVERSALLY ROOT-FORCED.

OVERALL STATUS:
CLOSED AS A STANDALONE UNIVERSAL ROOT AMPLIFIER.
```

This does not close higher prime correlations as a research topic.

It closes the specific claim that the connected fourth tensor supplies a new universal boundary lower geometry beyond second order.

---

# 17. Stronger novelty test

Any next multi-copy candidate should pass:

```text
SINGLE-BOUNDARY-PAIR NOVELTY TEST

Input:
F(t)=Ae^{iγt}+conj(A)e^{-iγt}.

Question:
Is the candidate determined by
C_2(u)=2|A|^2 cos(γu)?

If YES:
reject as a new universal spectral amplifier.

If NO:
check that it remains nonzero
for the single-pair model.
```

For polynomial functionals of one linear field, Theorem 10.1 shows the answer is always YES.

---

# 18. Consequence for future direction

The next candidate must introduce information which is not a finite-degree polynomial statistic of one linear prime-error field.

Plausible classes are:

1. a mixed observable coupling the prime error to a genuinely independent ordinary-factorization state;
2. conditional factor anatomy given a prime event;
3. non-polynomial threshold or Boolean observables;
4. arithmetic constraints using both addition and multiplication which cannot be reconstructed from the two-point prime-error spectrum.

A new branch should state an explicit such observable before developing another framework.

---

# 19. External calibration

## 19.1. Montgomery–Soundararajan

H. L. Montgomery and K. Soundararajan,
*Primes in short intervals*,
Communications in Mathematical Physics 252 (2004), 589–617.

They develop the Gaussian short-interval moment model under strong Hardy–Littlewood input.

URL:

https://arxiv.org/abs/math/0409258

## 19.2. Leung, 2026

Sun-Kai Leung,
*Joint distribution of primes in multiple short intervals*,
Advances in Mathematics 490 (2026), 110847.

The theorem obtains a multivariate Gaussian law under RH and a linear-independence conjecture.

URL:

https://doi.org/10.1016/j.aim.2026.110847

## 19.3. MRSTT, 2026

Matomäki, Radziwiłł, Shao, Tao and Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*,
Inventiones Mathematicae 244 (2026), 967–1091.

This remains the main unconditional higher-uniformity calibration for actual short-interval prime correlations.

---

# 20. State transition

Advance candidate state

$$
v1.72
\to
v1.73.
$$

Add:

```text
B-RH-144
THE_NEGATIVE_DIAGONAL_SPECTRAL_MASS_OF_THE_CONNECTED_FOURTH_TENSOR_IS_A_POSITIVE_DEGREE_FOUR_BOUNDARY_DETECTOR

B-RH-145
THE_ROBUST_CONNECTED_FOURTH_SELF_DIAGONAL_IS_EXACTLY_THE_L2_ENERGY_OF_THE_TWO_POINT_SPECTRUM

O-RH-181
A_SINGLE_CONJUGATE_BOUNDARY_PAIR_HAS_NO_INDEPENDENT_FINITE_DEGREE_STATIONARY_POLYNOMIAL_STATISTICS_BEYOND_C2

O-RH-182
GENUINE_OFF_DIAGONAL_CONNECTED_FOURTH_INFORMATION_IS_NOT_UNIVERSALLY_FORCED_BY_A_SINGLE_BOUNDARY_PAIR

C-RH-008
PAPER81_OVERSTATED_THE_DIRECT_ARITHMETIC_LEVERAGE_OF_THE_LOCAL_R4_THEOREM_FOR_THE_LOG_SCALE_FREQUENCY_RESOLVED_SELF_ATOM
```

Close:

```text
F-RH-026
CLOSED_AS_STANDALONE_UNIVERSAL_ROOT_AMPLIFIER
```

No RH certificate is created.

---

# 21. Conclusion

The connected fourth tensor passes the elementary boundary-visibility test but fails the stronger novelty test.

Its universal self-frequency detector is positive and robust, yet exactly equal to the squared two-point spectral mass.

A single conjugate boundary pair determines all finite-degree stationary polynomial statistics through its two-point covariance.

Therefore pure polynomial multi-copy statistics of one linear prime-error field cannot provide new universal spectral coercivity beyond second order.

The next genuinely new object must mix in arithmetic state not encoded by that two-point spectrum.
