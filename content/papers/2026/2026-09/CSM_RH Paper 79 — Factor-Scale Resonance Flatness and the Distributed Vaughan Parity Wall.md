# CSM_RH Paper 79

## Factor-Scale Resonance Flatness and the Distributed Vaughan Parity Wall

**Project:** CSM_RH  
**Paper:** 79  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 47 — `ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Active frontier:** F-RH-024 — `RENORMALIZED_VAUGHAN_BALANCED_DEFECT_POWER`  
**Status:** DYADIC FACTOR-SCALE ZERO RESPONSE LOCALIZED / EDGE-LOCALIZATION HYPOTHESIS REJECTED / DISTRIBUTED LOG-SCALE PARITY WALL CERTIFIED  
**Canonical entry state:** v1.69 / Paper 78 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 78 proved that the renormalized Vaughan coefficient preserves every nontrivial zeta-zero pole with universal residue.

The next question was whether this universal rightmost-zero mass is concentrated in a narrow polynomial factor range

$$
e\asymp N^\theta,
\qquad
k\asymp N^{1-\theta},
$$

or distributed across the full Vaughan factor strip.

The present paper answers this in the smooth Mellin-resonance sense.

Fix

$$
\psi\in C_c^\infty(1,2).
$$

For a multiplicative prime scale $E$ define the **prime-error block**

$$
\boxed{
P_E(s)
=
\sum_{n\ge1}
\Lambda(n)\psi(n/E)n^{-s}
-
\int_0^\infty
\psi(x/E)x^{-s}dx.
}
$$

Let

$$
\widehat\psi(w)
=
\int_0^\infty
\psi(u)u^{w-1}du.
$$

The smooth explicit formula gives

$$
\boxed{
P_E(s)
=
-
\sum_{\rho'}
E^{\rho'-s}
\widehat\psi(\rho'-s)
+
\mathcal T_{\psi,E}(s),
}
$$

where $\mathcal T_{\psi,E}$ is the trivial-zero / gamma-factor contribution and is negligible at positive large $E$ for the fixed spectral points considered below.

Let

$$
\rho=\Theta+i\gamma
$$

be a nontrivial zeta zero of multiplicity $m_\rho$.

At the **resonant spectral point**

$$
s=\rho,
$$

the contribution of the zero $\rho$ itself is

$$
\boxed{
-m_\rho\widehat\psi(0),
}
$$

where

$$
\widehat\psi(0)
=
\int_1^2
\psi(u)\frac{du}{u}.
$$

This term is exactly independent of $E$.

Thus, after the prime main is removed correctly, a rightmost zero does **not** become larger at the largest $e$ -scale and does not concentrate at a Vaughan edge.

Its self-resonance is flat per logarithmic factor scale.

Now insert the Vaughan cofactor tail

$$
\boxed{
B_U(s)
=
\sum_{k>U}
\frac{b_U(k)}{k^s}
=
\zeta(s)M_U(s)-1.
}
$$

At every nontrivial zeta zero,

$$
\boxed{
B_U(\rho)=-1,
}
$$

for every $U>1$.

Define the smooth $e$ -block of the balanced **prime-error** coefficient by

$$
\boxed{
\mathscr C_{E,U}(s)
=
P_E(s)B_U(s).
}
$$

Then the self-zero resonance of $\mathscr C_{E,U}$ at $\rho$ is

$$
\boxed{
+m_\rho\widehat\psi(0),
}
$$

again independent of both $E$ and $U$.

This is the central theorem of the paper.

If

$$
E=e^t,
$$

the other rightmost zeros

$$
\rho'=\Theta+i\gamma'
$$

contribute phases

$$
e^{i(\gamma'-\gamma)t}.
$$

Hence the boundary response is an almost-periodic function of the **factor scale** $t=\log E$.

Long averaging in $t$ diagonalizes distinct ordinates:

$$
\boxed{
\lim_{T\to\infty}
\frac1T
\int_0^T
\left|
\sum_{\Re\rho'=\Theta}
m_{\rho'}
e^{i(\gamma'-\gamma)t}
\widehat\psi(\rho'-\rho)
\right|^2dt
=
\sum_{\Re\rho'=\Theta}
m_{\rho'}^2
\left|
\widehat\psi(\rho'-\rho)
\right|^2
>0.
}
$$

No linear-independence conjecture is required.

Therefore off-diagonal zeros cannot make the rightmost-zero resonance disappear on almost all factor scales.

For Campaign 47, take

$$
U=N^u,
\qquad
V=N^v.
$$

The Vaughan balanced range contains

$$
V<e<N/U.
$$

Its logarithmic length is

$$
\boxed{
\log\frac{N/U}{V}
=
(1-u-v)\log N.
}
$$

Thus, whenever

$$
u+v<1,
$$

the number of unit-log or dyadic factor scales tends to infinity with $N$.

Each scale carries the same self-zero resonance after the prime main is removed.

The nontrivial zero pole of Paper 78 is therefore the accumulated resonance of a **growing family of logarithmic factor blocks**.

It is not supported on a fixed finite set of dyadic blocks.

It is not concentrated near

$$
e\asymp N/U.
$$

It is a distributed parity wall across the entire admissible logarithmic Vaughan strip.

This resolves the dyadic-localization question opened in Paper 78.

The result also corrects an overly narrow literature calibration in Paper 78.

Ford's 2025 shifted-prime Kubilius theorem gives a particularly strong total-variation approximation for small prime factors.

But 2026 work of Bharadwaj and Rodgers goes further: for a sequence with level of distribution $\sigma>0$, correlation functions of **polynomial-scale large prime factors** match the Poisson–Dirichlet model against test functions supported in

$$
\boxed{
y_1+\cdots+y_k<\sigma.
}
$$

They prove that shifted primes are $1/2$ well-distributed.

Thus current anatomy theory does reach polynomial factor exponents.

However, the support condition is exactly the remaining barrier for the present problem.

A complementary factorization

$$
e\asymp N^\theta,
\qquad
k\asymp N^{1-\theta}
$$

has total logarithmic size

$$
\boxed{
\theta+(1-\theta)=1.
}
$$

No theorem with level

$$
\sigma<1
$$

controls the **complete complementary factor pair** through the restricted-support correlation statement.

Even the shift-averaged nonnegative sequence of Paper 75 has deterministic level only up to

$$
\boxed{
\sigma<1-\tau,
}
$$

because its divisor remainder ratio is

$$
N^{\sigma-(1-\tau)+o(1)}.
$$

Hence its current large-factor correlation information still has support strictly below total factor mass $1$.

The distributed Vaughan resonance lives exactly on that full complementary-factor boundary.

This produces a new, precise scope statement:

```text
current anatomy theorems can see
proper subcollections of polynomial prime factors;

F-RH-024 requires coherent information
across a complete complementary factorization
whose normalized log sizes sum to 1.
```

The next Campaign-47 arithmetic target should therefore not single out one $\theta$.

Instead, it should seek a **factor-scale averaged renormalized defect theorem** whose cancellation is uniform over a positive-length $\theta$ interval and remains coherent after summing all such intervals.

Open:

```text
F-RH-025
DISTRIBUTED VAUGHAN FACTOR-SCALE DEFECT POWER
```

A candidate form is:

partition the $e$ -variable by a smooth multiplicative partition

$$
1=
\int
\psi(e/e^t)\,dt
$$

on

$$
V<e<N/U.
$$

Let

$$
\mathcal V_t^{\rm ren}(N,H;U,V)
$$

denote the corresponding locally renormalized Vaughan block.

Find fixed

$$
\eta>0
$$

such that the accumulated defect satisfies

$$
\boxed{
\left|
\int_{\log V}^{\log(N/U)}
\mathcal V_t^{\rm ren}
\,dt
\right|
\ll
NH
N^{-\kappa-\eta},
}
$$

while the local Type-I renormalizations are retained exactly.

This is essentially F-RH-024 with its factor-scale geometry made explicit.

The new information is that no fixed $\theta$ block can be declared the unique hard block.

The boundary zero is coherently replicated across the full logarithmic factor strip.

No RH theorem is claimed.

---

# 1. Smooth prime-error block

Fix

$$
\psi\in C_c^\infty(1,2).
$$

Define

$$
\boxed{
P_E(s)
=
\sum_{n\ge1}
\Lambda(n)
\psi(n/E)n^{-s}
-
\int_0^\infty
\psi(x/E)x^{-s}dx.
}
$$

The continuous term is

$$
\boxed{
E^{1-s}\widehat\psi(1-s).
}
$$

This is the correct blockwise removal of the prime main.

Using $\Lambda(n)-1$ directly gives the same fixed-power resonance after the usual Euler-summation adjustment between the integer sum of $1$ and the continuous integral.

---

# 2. Smooth explicit formula

For fixed $s$ and large $E$, the explicit formula gives

$$
\boxed{
P_E(s)
=
-
\sum_{\rho'}
E^{\rho'-s}
\widehat\psi(\rho'-s)
+
\mathcal T_{\psi,E}(s).
}
$$

The smooth compact support gives rapid decay of

$$
\widehat\psi(\sigma+i\tau)
$$

in $|\tau|$.

Thus the zero sum is absolutely manageable at every fixed spectral point after standard grouping.

---

# 3. Self-zero resonance is factor-scale invariant

Let

$$
\rho=\Theta+i\gamma
$$

be a zero of multiplicity $m_\rho$.

Set

$$
s=\rho.
$$

Its own contribution in Section 2 is

$$
\boxed{
-m_\rho
E^{\rho-\rho}
\widehat\psi(0)
=
-m_\rho\widehat\psi(0).
}
$$

No factor of $E$ remains.

Create:

```text
B-RH-128
A_RIGHTMOST_ZETA_ZERO_HAS_SCALE_INVARIANT_SELF_RESONANCE_IN_EACH_SMOOTH_LOGARITHMIC_PRIME_FACTOR_BLOCK
CERTIFIED
```

This is the factor-scale analogue of Paper 73's log- $N$ resonance.

---

# 4. Vaughan cofactor tail does not alter the resonance amplitude

Recall

$$
B_U(s)
=
\zeta(s)M_U(s)-1.
$$

At every nontrivial zeta zero,

$$
\boxed{
B_U(\rho)=-1.
}
$$

Therefore

$$
\mathscr C_{E,U}(s)
=
P_E(s)B_U(s)
$$

has self-zero response

$$
\boxed{
+m_\rho\widehat\psi(0).
}
$$

This is independent of $U$.

Create:

```text
B-RH-129
VAUGHAN_COFACTOR_TAIL_TRANSPORTS_THE_BLOCKWISE_ZERO_RESONANCE_WITH_UNIVERSAL_UNIT_GAIN
CERTIFIED
```

---

# 5. Factor-scale almost periodicity

Let

$$
E=e^t.
$$

At $s=\rho=\Theta+i\gamma$, the rightmost-zero part is

$$
\boxed{
\sum_{\Re\rho'=\Theta}
m_{\rho'}
e^{i(\gamma'-\gamma)t}
\widehat\psi(\rho'-\rho).
}
$$

This is an absolutely summable almost-periodic Fourier series because the Mellin transform of $\psi$ decays rapidly.

Long $t$ -averaging gives:

## Theorem 5.1 — Factor-scale zero orthogonality

$$
\boxed{
\begin{aligned}
&
\lim_{T\to\infty}
\frac1T
\int_0^T
\left|
\sum_{\Re\rho'=\Theta}
m_{\rho'}
e^{i(\gamma'-\gamma)t}
\widehat\psi(\rho'-\rho)
\right|^2dt
\\
&\qquad
=
\sum_{\Re\rho'=\Theta}
m_{\rho'}^2
\left|
\widehat\psi(\rho'-\rho)
\right|^2.
\end{aligned}
}
$$

The right side is positive if

$$
\widehat\psi(0)\ne0.
$$

Create:

```text
B-RH-130
RIGHTMOST_ZERO_RESPONSES_DIAGONALIZE_IN_LOGARITHMIC_FACTOR_SCALE
CERTIFIED
```

---

# 6. Why naive edge localization was wrong

If one evaluates the uncentered prime block

$$
\sum\Lambda(n)\psi(n/E)n^{-\rho},
$$

its main term has size

$$
E^{1-\rho}.
$$

This grows like

$$
E^{1-\Theta}.
$$

Looking only at that quantity falsely suggests domination by the largest $E$.

But this is the **prime main**, not the zero resonance.

After the continuous prime main is removed, the self-zero term becomes

$$
-m_\rho\widehat\psi(0),
$$

independent of $E$.

Therefore:

```text
C-RH-006
UNRENORMALIZED_E_POWER_GROWTH_MUST_NOT_BE_USED_TO_LOCALIZE_THE_RIGHTMOST_ZERO_TO_THE_VAUGHAN_EDGE
```

---

# 7. Accumulation across the Vaughan factor strip

Let

$$
U=N^u,
\qquad
V=N^v.
$$

The balanced coefficient uses

$$
V<e<N/U.
$$

Thus the factor-scale interval is

$$
\boxed{
v\log N
<
\log e
<
(1-u)\log N.
}
$$

Its length is

$$
\boxed{
(1-u-v)\log N.
}
$$

A smooth partition into unit-log blocks therefore contains

$$
\asymp
(1-u-v)\log N
$$

blocks.

The self-zero resonance has the same size in each block.

Hence the simple pole of the global renormalized coefficient is naturally interpreted as the accumulation of equal-strength logarithmic-scale resonances.

Create:

```text
O-RH-176
THE_UNIVERSAL_ZETA_ZERO_POLE_IS_DISTRIBUTED_ACROSS_A_GROWING_NUMBER_OF_VAUGHAN_LOG_FACTOR_SCALES
CERTIFIED
```

No fixed finite set of logarithmic blocks carries the pole.

---

# 8. No persistent factor-scale cancellation

Theorem 5.1 shows that other rightmost zeros may oscillate against a chosen zero as $E$ changes.

But their long factor-scale cross terms vanish.

The self-zero diagonal remains.

Therefore the rightmost-zero resonance cannot be canceled on almost all factor scales by generic zero-phase interference.

This is a second distributed-parity obstruction:

```text
factor-scale averaging does not remove
the rightmost-zero diagonal;
it reveals it.
```

---

# 9. 2026 large-prime-factor anatomy correction

Paper 78 emphasized Ford's small-factor Kubilius regime.

Current literature is stronger.

Bharadwaj and Rodgers prove that if an arithmetic sequence has level of distribution $\sigma>0$, then the correlation functions of normalized logarithmic prime factors match those of the Poisson–Dirichlet process against test functions supported in

$$
\boxed{
y_1+\cdots+y_k<\sigma.
}
$$

They also prove that shifted primes are

$$
\boxed{
\sigma=\frac12
}
$$

well-distributed.

Therefore modern anatomy theory does see polynomial-size prime factors.

Create correction:

```text
C-RH-007
PAPER78_SMALL_FACTOR_ONLY_DESCRIPTION_OF_CURRENT_SHIFTED_PRIME_ANATOMY_WAS_TOO_NARROW
```

The correct statement is support-limited polynomial anatomy.

---

# 10. Why the complete complementary factorization remains outside current anatomy

For the Vaughan factorization

$$
n=ek,
$$

write

$$
e\asymp N^\theta,
$$

$$
k\asymp N^{1-\theta}.
$$

The normalized logarithmic sizes sum to

$$
\boxed{
1.
}
$$

Bharadwaj–Rodgers correlation transference at level $\sigma$ requires total support strictly below $\sigma$.

For shifted primes,

$$
\sigma=\frac12.
$$

Thus it cannot encode a full complementary factorization.

Even if one applies the general theorem to the shift-averaged nonnegative sequence from Paper 75, its deterministic divisor estimate gives level of distribution only for every

$$
\boxed{
\sigma<1-\tau.
}
$$

Indeed, summing the $O(N)$ divisor error to

$$
D=N^\sigma
$$

costs

$$
N^{1+\sigma},
$$

while the total mass is

$$
NH=N^{2-\tau}.
$$

The relative error is

$$
N^{\sigma-(1-\tau)}.
$$

Hence $\sigma=1$ is not reached for any fixed $\tau>0$.

The complementary factor pair still has total size $1$.

Create:

```text
O-RH-177
CURRENT_LEVEL_OF_DISTRIBUTION_FACTOR_ANATOMY_DOES_NOT_CONTROL_A_COMPLETE_COMPLEMENTARY_FACTOR_PAIR_OF_TOTAL_LOG_SIZE_ONE
CERTIFIED_AS_SCOPE_BARRIER
```

---

# 11. Consequence for dyadic F-RH-024

The factor-scale question now has a definite answer.

```text
EDGE LOCALIZATION:
REJECTED AFTER PROPER PRIME-MAIN RENORMALIZATION.

SINGLE CRITICAL THETA:
NOT IDENTIFIED.

DISTRIBUTED LOG-SCALE RESONANCE:
CERTIFIED.
```

Every positive-length subinterval of the admissible $\theta$ strip contains a number of resonant logarithmic blocks proportional to its length.

The root-hard spectrum is therefore distributed through the factorization scale.

---

# 12. New explicit geometry frontier F-RH-025

Open:

```text
F-RH-025
DISTRIBUTED_VAUGHAN_FACTOR_SCALE_DEFECT_POWER
```

Let

$$
\psi_t(e)
=
\psi(e/e^t)
$$

form a smooth multiplicative partition over

$$
V<e<N/U.
$$

Decompose the exact renormalized Vaughan defect into

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
=
\int_{\log V}^{\log(N/U)}
\mathcal V_t^{\rm ren}
\,dt
+
\text{endpoint terms}.
}
$$

The target is not that each block be absolutely tiny.

The target is a fixed-power estimate for the full accumulated defect:

$$
\boxed{
\left|
\int
\mathcal V_t^{\rm ren}dt
\right|
\ll
NH
N^{-\kappa-\eta},
}
$$

with the local prime main and Type-I counterterms retained exactly.

Paper 79 warns that any proof must overcome a coherent rightmost-zero resonance which is present across the entire factor-scale interval.

---

# 13. What anatomy information might still help

The Bharadwaj–Rodgers theorem may still control proper subcollections of the factorization.

For example, prime factors with total normalized log size below

$$
\sigma
$$

can have Poisson–Dirichlet correlation behavior.

This could be useful for:

- the factorization of a small cofactor;
- excluding exceptional anatomy classes;
- controlling portions of $b_U(k)$ built from prime factors whose total size lies below the level.

But it does not determine the joint law of the complete pair $(e,k)$ whose total normalized size is $1$.

Thus anatomy may become a supporting tool for F-RH-025, not a complete theorem.

---

# 14. State transition

Advance candidate state

$$
v1.69
\to
v1.70.
$$

Add:

```text
B-RH-128
A_RIGHTMOST_ZETA_ZERO_HAS_SCALE_INVARIANT_SELF_RESONANCE_IN_EACH_SMOOTH_LOGARITHMIC_PRIME_FACTOR_BLOCK

B-RH-129
VAUGHAN_COFACTOR_TAIL_TRANSPORTS_THE_BLOCKWISE_ZERO_RESONANCE_WITH_UNIVERSAL_UNIT_GAIN

B-RH-130
RIGHTMOST_ZERO_RESPONSES_DIAGONALIZE_IN_LOGARITHMIC_FACTOR_SCALE

O-RH-176
THE_UNIVERSAL_ZETA_ZERO_POLE_IS_DISTRIBUTED_ACROSS_A_GROWING_NUMBER_OF_VAUGHAN_LOG_FACTOR_SCALES

O-RH-177
CURRENT_LEVEL_OF_DISTRIBUTION_FACTOR_ANATOMY_DOES_NOT_CONTROL_A_COMPLETE_COMPLEMENTARY_FACTOR_PAIR_OF_TOTAL_LOG_SIZE_ONE

C-RH-006
UNRENORMALIZED_E_POWER_GROWTH_MUST_NOT_BE_USED_TO_LOCALIZE_THE_RIGHTMOST_ZERO_TO_THE_VAUGHAN_EDGE

C-RH-007
PAPER78_SMALL_FACTOR_ONLY_DESCRIPTION_OF_CURRENT_SHIFTED_PRIME_ANATOMY_WAS_TOO_NARROW
```

Open:

```text
F-RH-025
DISTRIBUTED_VAUGHAN_FACTOR_SCALE_DEFECT_POWER
OPEN_GEOMETRIC_ROOT_FRONTIER
```

F-RH-024 remains the algebraic root frontier.

No RH certificate is created.

---

# 15. External calibration

## 15.1. Bharadwaj–Rodgers, 2026

A. Bharadwaj and B. Rodgers,
*Large prime factors of well-distributed sequences*,
Canadian Mathematical Bulletin, published online 17 April 2026.

They prove:

- level $1$ implies full Poisson–Dirichlet convergence of large prime factors;
- positive level $\sigma$ implies convergence of large-prime-factor correlation functions against test functions supported in
  $$
  y_1+\cdots+y_k<\sigma;
  $$
- shifted primes have level $1/2$.

URL:

https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/large-prime-factors-of-welldistributed-sequences/270043D7BAB4CDA2A601A061FB482AA0

## 15.2. Ford, 2025

K. Ford,
*Poisson Approximation of Prime Divisors of Shifted Primes*,
International Mathematics Research Notices 2025.

Ford gives a strong total-variation shifted-prime Kubilius theorem and a transference principle for factor anatomy.

The 2026 Bharadwaj–Rodgers theorem provides the more appropriate polynomial-factor support calibration used in this paper.

---

# 16. Recommended next action

The next round should **not** choose a single $\theta$ block.

Instead, use the distributed resonance theorem to ask whether the ordinary-factorization coefficient

$$
b_U(k)
=
\sum_{\substack{d\mid k\\d\le U}}\mu(d)
$$

has a factor-scale martingale / Buchstab / Poisson–Dirichlet decomposition whose **cross-scale increments** telescope against the equal-strength prime-error resonances.

The test is strict:

- any proposed scale decomposition must reproduce the universal unit zero residue when all scales are summed;
- a claimed fixed-power gain must come from arithmetic cancellation between factor-anatomy classes, not from deleting or centering the resonant diagonal.

If no such cross-scale arithmetic cancellation exists, F-RH-025 is another RH-equivalent distributed parity wall.

---

# 17. Conclusion

The rightmost-zero mass in the renormalized Vaughan coefficient is not an edge effect.

After the prime main is removed correctly, each logarithmic prime-factor scale carries the same self-zero resonance.

The global pole is the accumulation of these resonances across a factor-scale interval of length proportional to $\log N$.

Modern large-factor anatomy reaches polynomial scales, but only under a support-sum condition strictly below the available level of distribution.

A complete complementary Vaughan factorization lies on total log mass $1$ and remains outside that regime.

Campaign 47 has therefore reached a distributed, not localized, parity geometry.
