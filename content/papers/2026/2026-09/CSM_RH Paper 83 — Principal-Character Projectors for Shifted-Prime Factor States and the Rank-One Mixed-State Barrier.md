# CSM_RH Paper 83

## Principal-Character Projectors for Shifted-Prime Factor States and the Rank-One Mixed-State Barrier

**Project:** CSM_RH  
**Paper:** 83  
**Version:** v0.1  
**Date:** 2026-09-09  
**Branch:** `MIXED_ARITHMETIC_STATE_SCREENING`  
**Entry state:** v1.73 / Paper 82 v0.1  
**Status:** PERIODIC / SIEVE FACTOR STATES CLASSIFIED / PRINCIPAL ZETA HARD CORE IS RANK ONE / CENTERED FACTOR-ANATOMY FLUCTUATIONS ARE PRINCIPAL-ZETA-BLIND  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 82 closed pure finite-degree polynomial statistics of one linear prime-error field as a source of new universal boundary coercivity.

The next proposed class was a mixed observable coupling primality to an ordinary-factorization state.

The present paper classifies the largest tractable subclass: factor states determined by congruence information, finite divisor conditions, roughness conditions over finitely many primes, or any periodic state of a shifted integer.

The conclusion is exact.

Fix:

- an integer shift $a$ ;
- a modulus $Q\ge1$ ;
- a bounded function
  $$
  g:\mathbb Z/Q\mathbb Z\to\mathbb C.
  $$

For prime variables $n$ coprime to $Q$, define

$$
\boxed{
w_{g,a}(n)
=
g(n+a\bmod Q).
}
$$

Let

$$
\boxed{
\mathcal P_{g,a;Q}(s)
=
\sum_{n\ge1}
\frac{\Lambda(n)w_{g,a}(n)}{n^s}.
}
$$

The finitely many prime powers supported on primes dividing $Q$ may be separated into an entire Dirichlet polynomial and will be ignored in the spectral projector statements.

On the reduced residue group

$$
G_Q
=
(\mathbb Z/Q\mathbb Z)^\times,
$$

expand

$$
w_{g,a}(r)
=
\sum_{\chi\bmod Q}
\widehat g_a(\chi)\chi(r),
$$

where

$$
\boxed{
\widehat g_a(\chi)
=
\frac1{\phi(Q)}
\sum_{r\in G_Q}
g(r+a)
\overline{\chi(r)}.
}
$$

Then

$$
\boxed{
\mathcal P_{g,a;Q}(s)
=
\sum_{\chi\bmod Q}
\widehat g_a(\chi)
\left(
-\frac{L'}{L}(s,\chi)
\right)
+
\mathcal E_Q(s),
}
$$

where $\mathcal E_Q$ is entire in the critical strip.

The principal-character coefficient is

$$
\boxed{
\pi_{g,a;Q}
=
\widehat g_a(\chi_0)
=
\frac1{\phi(Q)}
\sum_{r\in G_Q}
g(r+a).
}
$$

Since

$$
L(s,\chi_0)
=
\zeta(s)
\prod_{p\mid Q}
\left(
1-p^{-s}
\right),
$$

one has

$$
\boxed{
-\frac{L'}{L}(s,\chi_0)
=
-\frac{\zeta'}{\zeta}(s)
+
\mathcal A_Q(s),
}
$$

where $\mathcal A_Q$ is analytic at every nontrivial zeta zero.

Therefore:

## Principal-character factor-state projector theorem

$$
\boxed{
\mathcal P_{g,a;Q}(s)
=
\pi_{g,a;Q}
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
+
\mathcal R_{g,a;Q}(s),
}
$$

where $\mathcal R_{g,a;Q}$ contains:

- nonprincipal Dirichlet- $L$ logarithmic derivatives;
- finite Euler corrections;
- no **principal-character** zeta pole.

Thus a zeta zero $\rho$ of multiplicity $m$ contributes to the principal projector with residue

$$
\boxed{
-m\,\pi_{g,a;Q}.
}
$$

The theorem gives an immediate dichotomy.

Define the principal-centered factor state

$$
\boxed{
g^\circ(r+a)
=
g(r+a)-\pi_{g,a;Q}.
}
$$

Then

$$
\boxed{
\widehat {g^\circ}_a(\chi_0)=0.
}
$$

Hence the shifted-prime series weighted by $g^\circ$ has no principal-character $\zeta'/\zeta$ term.

So:

```text
UNCENTERED PERIODIC FACTOR STATE:
retains a scalar copy of the original zeta hard core.

PRINCIPAL-CENTERED PERIODIC FACTOR STATE:
removes the zeta hard core and keeps only nonprincipal L-spectra.
```

This includes every finite divisor-sieve state.

If

$$
g(m)
=
\sum_{d\in\mathcal D}
\lambda_d
\mathbf 1_{d\mid m},
$$

then $g$ is periodic modulo

$$
Q=\operatorname{lcm}_{d\in\mathcal D}d.
$$

Therefore every finite Selberg-sieve weight, truncated small-prime anatomy state, finite roughness gate, and finite combination of divisibility patterns satisfies the projector theorem.

A particularly transparent example is a roughness gate.

Let

$$
P(z)
=
\prod_{p\le z}p
$$

and

$$
g_z(m)
=
\mathbf 1_{(m,P(z))=1}.
$$

For $Q=P(z)$,

$$
\boxed{
\pi_{z,a}
=
\frac1{\phi(P(z))}
\#\left\{
r\bmod P(z):
(r,P(z))=1,\,
(r+a,P(z))=1
\right\}.
}
$$

By the Chinese remainder theorem,

$$
\boxed{
\pi_{z,a}
=
\prod_{\substack{p\le z\\p\nmid a}}
\frac{p-2}{p-1}.
}
$$

For primes $p\mid a$, the local factor is $1$.

The parity obstruction is visible immediately: if $2\nmid a$ and $2\le z$, the density is $0$.

The centered roughness observable

$$
\boxed{
g_z(n+a)-\pi_{z,a}
}
$$

therefore deletes the principal zeta boundary mode exactly.

This structural projector is consistent with current shifted-prime factor-anatomy theorems.

Ford proves a Kubilius-type model for prime factors of shifted primes and Poisson behavior for prime factors in disjoint small-prime sets.

Bharadwaj and Rodgers prove polynomial large-prime-factor correlation laws for well-distributed sequences under restricted support.

These results describe increasingly rich **conditional factor anatomy**.

But the present theorem shows that, for periodic/sieve-visible parts of that anatomy, the principal zeta error remains a one-dimensional scaling direction independent of the orthogonal anatomy fluctuations.

The vector form makes this explicit.

Suppose

$$
g_1,\ldots,g_J
$$

form a partition of unity on shifted reduced residue states:

$$
\boxed{
\sum_{j=1}^J
g_j(r+a)=1
}
$$

for every

$$
r\in G_Q.
$$

Define

$$
\pi_j
=
\pi_{g_j,a;Q}.
$$

Then

$$
\boxed{
\sum_j\pi_j=1.
}
$$

The vector of shifted-prime Dirichlet series satisfies

$$
\boxed{
\mathbf P(s)
=
\boldsymbol\pi
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
+
\mathbf R(s).
}
$$

Thus the principal-zeta hard core lies in the rank-one direction

$$
\boxed{
\operatorname{span}\{\boldsymbol\pi\}.
}
$$

For any vector $c\in\mathbb C^J$:

- if
  $$
  c\cdot\boldsymbol\pi=0,
  $$
  then the linear statistic $c\cdot\mathbf P$ has no principal zeta projector;

- if
  $$
  c\cdot\boldsymbol\pi\ne0,
  $$
  then it contains precisely a scalar copy of the original zeta hard core.

This gives the **rank-one mixed-state barrier**.

A factor-state vector can contain substantial arithmetic information orthogonal to its principal direction.

But the existence of a zeta boundary zero alone only forces the principal direction.

The centered factor-anatomy fluctuations are not a new universal root forcing mechanism.

The same conclusion applies to normalized conditional distributions.

If a factor-state count is centered relative to the total prime count,

$$
N_j(X)
-
\pi_j\psi(X),
$$

then its principal zeta error cancels.

If it is instead centered relative to the deterministic main

$$
\pi_jX,
$$

then

$$
\boxed{
N_j(X)-\pi_jX
=
\pi_j(\psi(X)-X)
+
\Delta_j(X),
}
$$

where

$$
\sum_j\Delta_j(X)=0.
$$

The first term is the rank-one root-hard direction.

The second is conditional anatomy.

Thus adding periodic factor states does not by itself create a relation which bounds the principal amplitude from the orthogonal fluctuations.

A genuinely new mixed-state route must introduce at least one of the following:

1. a nonperiodic complete-factorization state;
2. a second global arithmetic field with its own zeta-zero residue data;
3. a nonlinear constraint which forces the principal prime-error amplitude to interact with an orthogonal factor-state fluctuation.

The paper identifies one candidate class that survives the present projector test:

```text
GLOBAL PRIME-ERROR / MERTENS-STATE CROSS SPECTRUM
```

The smoothed prime error has zero coefficients which do not depend on $\zeta'(\rho)$, while the smoothed Möbius summatory field has coefficients proportional, for a simple zero, to

$$
\frac1{\zeta'(\rho)}.
$$

Thus their joint spectral state is not determined by the prime-error two-point covariance alone.

This class will be screened next.

No root frontier is opened here; the next paper must first prove a universal boundary forcing theorem for the mixed prime/Mertens state.

No RH theorem is claimed.

---

# 1. Periodic shifted factor states

Fix $Q$ and $a$.

For

$$
r\in G_Q,
$$

define

$$
w(r)
=
g(r+a).
$$

Dirichlet characters form an orthonormal basis of functions on $G_Q$.

Therefore

$$
\boxed{
w(r)
=
\sum_{\chi\bmod Q}
\widehat g_a(\chi)\chi(r).
}
$$

---

# 2. Shifted-prime character decomposition

Ignoring the finite set of prime powers whose prime divides $Q$,

$$
\begin{aligned}
\mathcal P_{g,a;Q}(s)
&=
\sum_n
\frac{\Lambda(n)}{n^s}
\sum_\chi
\widehat g_a(\chi)\chi(n)
\\
&=
\boxed{
\sum_\chi
\widehat g_a(\chi)
\left(
-\frac{L'}{L}(s,\chi)
\right).
}
\end{aligned}
$$

Restoring the exceptional prime-power terms changes the expression by a finite Dirichlet series.

Create:

```text
B-RH-146
EVERY_PERIODIC_SHIFTED_PRIME_FACTOR_STATE_DECOMPOSES_EXACTLY_INTO_DIRICHLET_CHARACTER_LOG_DERIVATIVES
CERTIFIED
```

---

# 3. Principal-character projector

The principal coefficient is

$$
\pi_{g,a;Q}
=
\frac1{\phi(Q)}
\sum_{r\in G_Q}
g(r+a).
$$

Since

$$
L(s,\chi_0)
=
\zeta(s)
\prod_{p\mid Q}(1-p^{-s}),
$$

the only globally forced zeta factor in the character decomposition is the principal-character term.

Thus:

## Theorem 3.1 — Periodic factor-state zeta projector

$$
\boxed{
\mathcal P_{g,a;Q}(s)
=
\pi_{g,a;Q}
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
+
\mathcal R_{g,a;Q}(s).
}
$$

Create:

```text
B-RH-147
THE_PRINCIPAL_ZETA_HARD_CORE_OF_A_PERIODIC_SHIFTED_PRIME_STATE_IS_EXACTLY_ITS_REDUCED_RESIDUE_MEAN
CERTIFIED
```

The remainder may contain nonprincipal Dirichlet- $L$ poles; those are separate spectra and are not forced by the existence of a zeta zero alone.

---

# 4. Centering dichotomy

Define

$$
g^\circ(r+a)
=
g(r+a)-\pi_{g,a;Q}.
$$

Then

$$
\widehat {g^\circ}_a(\chi_0)=0.
$$

Therefore:

## Corollary 4.1 — Principal-centering theorem

The shifted-prime observable weighted by $g^\circ$ contains no principal-character $\zeta'/\zeta$ term.

Create:

```text
O-RH-183
CENTERING_A_PERIODIC_FACTOR_STATE_REMOVES_THE_PRINCIPAL_ZETA_BOUNDARY_MODE_RATHER_THAN_AMPLIFYING_IT
CERTIFIED
```

---

# 5. Finite divisor states are periodic

Let

$$
g(m)
=
\sum_{d\in\mathcal D}
\lambda_d
\mathbf1_{d\mid m}
$$

with finite $\mathcal D$.

Then $g$ is periodic modulo

$$
Q=\operatorname{lcm}_{d\in\mathcal D}d.
$$

Hence Theorem 3.1 applies.

This includes:

- finite Selberg-sieve weights;
- finite small-prime factor-pattern indicators;
- finite squarefree / roughness gates;
- finite Boolean combinations of divisibility conditions.

Thus:

```text
SMALL-FACTOR SIEVE ANATOMY
DOES NOT EVADE THE PRINCIPAL PROJECTOR.
```

---

# 6. Roughness gate density

Let

$$
g_z(m)
=
\mathbf1_{(m,P(z))=1}.
$$

For each prime $p\le z$, the variable prime residue $r$ must satisfy

$$
r\not\equiv0\pmod p.
$$

If $p\nmid a$, roughness of $r+a$ imposes the additional exclusion

$$
r\not\equiv-a\pmod p.
$$

Among the $p-1$ reduced residues, $p-2$ remain.

If $p\mid a$, no additional reduced residue is excluded.

Therefore:

## Theorem 6.1 — Shifted-prime roughness principal density

$$
\boxed{
\pi_{z,a}
=
\prod_{\substack{p\le z\\p\nmid a}}
\frac{p-2}{p-1}.
}
$$

Create:

```text
B-RH-148
THE_PRINCIPAL_PROJECTOR_OF_A_FINITE_SHIFTED_PRIME_ROUGHNESS_GATE_IS_ITS_EXACT_LOCAL_SIEVE_DENSITY
CERTIFIED
```

---

# 7. Vector partition theorem

Suppose

$$
\sum_{j=1}^Jg_j(r+a)=1
$$

on $G_Q$.

Set

$$
\boldsymbol\pi
=
(\pi_1,\ldots,\pi_J).
$$

Then

$$
\sum_j\pi_j=1.
$$

The vector prime series is

$$
\boxed{
\mathbf P(s)
=
\boldsymbol\pi
\left(
-\frac{\zeta'}{\zeta}(s)
\right)
+
\mathbf R(s).
}
$$

Thus:

## Theorem 7.1 — Rank-one principal direction

The principal zeta spectrum of any finite periodic factor-state partition has rank one.

Create:

```text
B-RH-149
THE_PRINCIPAL_ZETA_SPECTRUM_OF_A_FINITE_PERIODIC_FACTOR_STATE_VECTOR_IS_RANK_ONE
CERTIFIED
```

---

# 8. Orthogonal anatomy fluctuations are root-blind

Let

$$
c\cdot\boldsymbol\pi=0.
$$

Then

$$
c\cdot\mathbf P(s)
=
c\cdot\mathbf R(s)
$$

contains no principal zeta projector.

Therefore any statistic built purely from the factor-anatomy directions orthogonal to $\boldsymbol\pi$ is not universally forced by a zeta boundary zero.

Create:

```text
O-RH-184
ORTHOGONAL_PERIODIC_FACTOR_ANATOMY_FLUCTUATIONS_ARE_NOT_UNIVERSALLY_FORCED_BY_A_ZETA_BOUNDARY_ZERO
CERTIFIED
```

---

# 9. Absolute versus conditional centering

Let $N_j(X)$ denote a factor-state prime count with main density $\pi_j$.

Write

$$
\boxed{
E_j(X)
=
N_j(X)-\pi_jX.
}
$$

Also define the conditional fluctuation

$$
\boxed{
\Delta_j(X)
=
N_j(X)-\pi_j\psi(X).
}
$$

Then

$$
\boxed{
E_j(X)
=
\pi_j(\psi(X)-X)
+
\Delta_j(X).
}
$$

Summing gives

$$
\sum_j\Delta_j(X)=0.
$$

This is the physical-space form of the rank-one projector.

The principal root amplitude is a common scaling direction.

The conditional factor-state fluctuation is transverse to it.

---

# 10. Why improved anatomy alone does not improve the PNT error

Suppose one proves very strong estimates for

$$
\Delta_j(X).
$$

Then

$$
N_j(X)
=
\pi_j\psi(X)
+
\text{small}.
$$

This sharpens the conditional distribution of factor states among primes.

But summing over $j$ returns the identity

$$
\psi(X)=\psi(X).
$$

No improved bound for

$$
\psi(X)-X
$$

follows.

Conversely, proving

$$
N_j(X)-\pi_jX
$$

smaller than the principal boundary scale for any $j$ with $\pi_j\ne0$ already removes the same zeta hard core.

Thus:

```text
conditional anatomy can be much easier
without controlling the root;

absolute anatomy at fixed-power precision
inherits the root.
```

---

# 11. Current factor-anatomy literature calibration

## Ford, 2025

Ford develops a Kubilius model for shifted primes and proves that prime factors in disjoint small-prime sets behave approximately like independent Poisson variables.

This is strong control of conditional factor anatomy.

It is compatible with the present projector theorem: the Poisson fluctuations live in the state distribution transverse to the total prime mass.

## Bharadwaj–Rodgers, 2026

For well-distributed sequences, Bharadwaj and Rodgers obtain Poisson–Dirichlet large-factor correlations under restricted support; shifted primes are $1/2$ well-distributed.

Again this concerns conditional anatomy.

It does not change the rank-one principal zeta direction in the prime count.

---

# 12. Screening of Möbius / Liouville shifted-prime states

The centered Möbius or Liouville state of $p+a$ is not a finite periodic state.

Thus the exact projector theorem does not directly classify it.

However current theorems such as Lichtman's averaged shifted-prime Möbius cancellation control quantities of the form

$$
\sum_{p\le X}\mu(p+h)
$$

on average over $h$.

Such a centered multiplicative state is not universally forced to be nonzero by a zeta boundary zero.

Therefore it cannot be a standalone root detector merely because it is arithmetically nonperiodic.

A mixed theorem would have to couple it to the principal prime-error direction through an additional exact or coercive relation.

---

# 13. First surviving mixed-state class

The present screen leaves one conceptually different class:

```text
GLOBAL PRIME-ERROR / GLOBAL MERTENS-STATE CROSS SPECTRUM
```

The smoothed prime error has explicit-formula boundary coefficients which depend on the zero location and the test transform.

For a simple zero $\rho$, the smoothed Möbius summatory field has coefficient

$$
\boxed{
\frac{\widehat V(\rho)}{\zeta'(\rho)}.
}
$$

This derivative information is not contained in the two-point spectrum of the prime-error field.

Therefore the pair

$$
(\text{prime error},\text{Mertens state})
$$

passes the Paper-82 single-field novelty test.

It does not yet pass the universal root-forcing or arithmetic-upper tests.

Those are the next tasks.

---

# 14. New mixed-state entry rule

A future mixed state should be rejected if it falls into either class:

```text
A. PERIODIC / FINITE-SIEVE STATE
   -> principal zeta scalar copy + nonprincipal remainder.

B. PRINCIPAL-CENTERED PERIODIC STATE
   -> zeta hard core removed.
```

A candidate advances only if:

1. it contains additional spectral data not determined by the prime-error $C_2$ ;
2. a zeta boundary zero forces a nonzero mixed signal;
3. the signal survives the single-boundary-pair model;
4. there is an explicit arithmetic quantity for which a fixed-power upper is at least conceptually distinct from PESC itself.

---

# 15. External calibration

## 15.1. Ford, 2025

K. Ford,
*Poisson Approximation of Prime Divisors of Shifted Primes*,
International Mathematics Research Notices 2025.

Ford develops a Kubilius model for shifted primes and proves approximate independence / Poisson behavior for prime divisors in disjoint sets.

URL:

https://doi.org/10.1093/imrn/rnaf079

## 15.2. Bharadwaj–Rodgers, 2026

A. Bharadwaj and B. Rodgers,
*Large prime factors of well-distributed sequences*,
Canadian Mathematical Bulletin, online 17 April 2026.

They obtain Poisson–Dirichlet large-factor laws at level $1$ and restricted-support correlation laws at positive level; shifted primes are $1/2$ well-distributed.

URL:

https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/large-prime-factors-of-welldistributed-sequences/270043D7BAB4CDA2A601A061FB482AA0

## 15.3. Lichtman

J. D. Lichtman,
*Averages of the Möbius function on shifted primes*,
Quarterly Journal of Mathematics 73 (2022), 729–750.

He proves averaged cancellation of Möbius on shifted primes with logarithmic quantitative savings.

URL:

https://doi.org/10.1093/qmath/haab054

---

# 16. State transition

Advance candidate state

$$
v1.73
\to
v1.74.
$$

Add:

```text
B-RH-146
EVERY_PERIODIC_SHIFTED_PRIME_FACTOR_STATE_DECOMPOSES_EXACTLY_INTO_DIRICHLET_CHARACTER_LOG_DERIVATIVES

B-RH-147
THE_PRINCIPAL_ZETA_HARD_CORE_OF_A_PERIODIC_SHIFTED_PRIME_STATE_IS_EXACTLY_ITS_REDUCED_RESIDUE_MEAN

B-RH-148
THE_PRINCIPAL_PROJECTOR_OF_A_FINITE_SHIFTED_PRIME_ROUGHNESS_GATE_IS_ITS_EXACT_LOCAL_SIEVE_DENSITY

B-RH-149
THE_PRINCIPAL_ZETA_SPECTRUM_OF_A_FINITE_PERIODIC_FACTOR_STATE_VECTOR_IS_RANK_ONE

O-RH-183
CENTERING_A_PERIODIC_FACTOR_STATE_REMOVES_THE_PRINCIPAL_ZETA_BOUNDARY_MODE_RATHER_THAN_AMPLIFYING_IT

O-RH-184
ORTHOGONAL_PERIODIC_FACTOR_ANATOMY_FLUCTUATIONS_ARE_NOT_UNIVERSALLY_FORCED_BY_A_ZETA_BOUNDARY_ZERO
```

Update:

```text
PERIODIC / SMALL-FACTOR MIXED STATE ROUTE
CLOSED AS PRINCIPAL-RANK-ONE OR ROOT-BLIND.
```

No new root frontier is opened yet.

Next screen:

```text
GLOBAL PRIME-ERROR / MERTENS-STATE CROSS SPECTRUM
```

No RH certificate is created.

---

# 17. Conclusion

Adding a finite factor state to a prime count creates a higher-dimensional arithmetic observable, but its principal zeta spectrum remains one-dimensional.

The reduced-residue mean of the state is the exact projector coefficient.

Centering removes the root mode.

Not centering retains only a scalar copy of it.

Thus small-prime divisibility anatomy, roughness gates, and finite sieve states do not create new universal boundary coercivity.

A genuinely new mixed-state route must leave the periodic/sieve category and carry additional zeta-zero data not already encoded by the prime-error two-point spectrum.
