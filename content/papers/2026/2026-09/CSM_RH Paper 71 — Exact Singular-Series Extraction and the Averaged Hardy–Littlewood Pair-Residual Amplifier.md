# CSM_RH Paper 71

## Exact Singular-Series Extraction and the Averaged Hardy–Littlewood Pair-Residual Amplifier

**Project:** CSM_RH  
**Paper:** 71  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Canonical root frontier:** F-RH-017-v3  
**New arithmetic root subfrontier:** F-RH-022 — `AVERAGED_HARDY_LITTLEWOOD_PAIR_RESIDUAL_EXCESS`  
**Status:** LOCAL PAIR FACTOR EXACTLY EXTRACTED / ROOT AMPLIFIER MAP CERTIFIED / FIXED-POWER PAIR RESIDUAL OPEN  
**Canonical entry state:** v1.61 / Paper 70 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Papers 63–70 progressively removed scale-comparison, character-family, local-factor, and shifted-Möbius auxiliary routes from the shortest CSM_RH root path. The present paper returns to the original short-interval prime error

$$
U_H(n)
=
\psi(n+H)-\psi(n)-H
$$

and expands its second moment directly into ordinary prime-pair correlations.

Set

$$
\Lambda_0(n)=\Lambda(n)-1
$$

and

$$
M_2(N,H)
=
\sum_{n\le N}
\left(
\sum_{h=1}^{H}
\Lambda_0(n+h)
\right)^2.
$$

For distinct shifts define

$$
\boxed{
E_0(N;h_1,h_2)
=
\sum_{n\le N}
\Lambda_0(n+h_1)\Lambda_0(n+h_2)
-
N\mathfrak S_0(\{h_1,h_2\}),
}
$$

where $\mathfrak S_0$ is the modified Hardy–Littlewood singular series of Montgomery–Soundararajan.

Define the complete pair residual

$$
\boxed{
\mathcal R_{\rm HL}^{(2)}(N,H)
=
\sum_{\substack{1\le h_1,h_2\le H\\h_1\ne h_2}}
E_0(N;h_1,h_2).
}
$$

Montgomery and Soundararajan proved the exact singular-series average

$$
\boxed{
R_2(H)
=
\sum_{\substack{1\le h_1,h_2\le H\\h_1\ne h_2}}
\mathfrak S_0(\{h_1,h_2\})
=
-H\log H
+
AH
+
O_\varepsilon(H^{1/2+\varepsilon}),
}
$$

with an explicit constant $A$.

The diagonal prime-square term satisfies

$$
\boxed{
\sum_{h\le H}
\sum_{n\le N}
\Lambda_0(n+h)^2
=
NH\log N
+
O(NH+H^2\log^2N).
}
$$

Therefore the entire short-interval second moment decomposes as

$$
\boxed{
M_2(N,H)
=
NH\log\frac NH
+
B\,NH
+
\mathcal R_{\rm HL}^{(2)}(N,H)
+
O_\varepsilon
\left(
NH^{1/2+\varepsilon}
+
H^2\log^2N
\right),
}
$$

for a constant $B$.

This is the key structural reduction of the paper.

The ordinary local arithmetic has already been solved:

- the diagonal contributes $NH\log N$ ;
- the averaged local singular series contributes $-NH\log H$ ;
- together they produce the expected variance
  $$
  NH\log(N/H).
  $$

The only missing root quantity is the **aggregate Hardy–Littlewood pair error**
 $\mathcal R_{\rm HL}^{(2)}$.

Let

$$
H=N^{1-\tau}.
$$

Suppose that for some fixed exponent $\xi>0$,

$$
\boxed{
|\mathcal R_{\rm HL}^{(2)}(N,H)|
\ll
NH^2N^{-\xi+o(1)}.
}
$$

The solved local main term satisfies

$$
NH\log(N/H)
=
NH^2
N^{-(1-\tau)+o(1)}.
$$

Hence the short-interval lag energy has MLEPG exponent

$$
\boxed{
\delta
=
\min\{1-\tau,\xi\}.
}
$$

Paper 54's seeded residue-chain theorem then gives

$$
\boxed{
\kappa'
<
\Phi_{\rm pair}
(\kappa;\tau,\xi)
:=
\min
\left\{
1-\tau,\,
\xi,\,
\kappa+\tau(2-\kappa)
\right\}.
}
$$

Therefore:

## Pair-residual strict amplifier gate

$$
\boxed{
\tau<1-\kappa,
\qquad
\xi>\kappa.
}
$$

When these hold,

$$
\operatorname{PESC}(\kappa)
\Longrightarrow
\operatorname{PESC}(\kappa+\eta)
$$

for every fixed

$$
\boxed{
0<\eta
<
\min
\left\{
1-\tau-\kappa,\,
\xi-\kappa,\,
\tau(2-\kappa)
\right\}.
}
$$

This gives the new arithmetic root subfrontier

```text
F-RH-022
AVERAGED_HARDY_LITTLEWOOD_PAIR_RESIDUAL_EXCESS
```

with target

$$
\boxed{
|\mathcal R_{\rm HL}^{(2)}(N,H)|
\ll
NH^2N^{-\kappa-\eta}
}
$$

for some fixed $\eta>0$ and some

$$
H=N^{1-\tau},
\qquad
0<\tau<1-\kappa.
$$

F-RH-022 is substantially weaker than a uniform Hardy–Littlewood twin-prime theorem for every shift. Only the fully aggregated pair-error sum is required.

The local singular-series cancellation is already rigorous. What remains is global cancellation of the **errors around the singular series**.

Current averaged prime-pair technology reaches precisely the same object, but only at logarithmic resolution.

Known results of Mikawa and Matomäki–Radziwiłł–Tao imply that the Hardy–Littlewood prime-pair asymptotic holds for all but logarithmically few shifts in long polynomial shift ranges. A standard $L^2$ formulation gives arbitrary fixed powers of $\log X$ of averaged saving, but no fixed factor $X^{-\eta}$.

Thus in exponent language the current averaged pair theory supplies

$$
\xi=o(1),
$$

while F-RH-022 requires

$$
\xi>\kappa.
$$

This is not a local-factor problem: Montgomery–Soundararajan's theorem has already evaluated the local singular-series average to lower order.

Nor is it an individual twin-prime problem: cancellation among the pair errors is explicitly allowed.

A smooth seed-boundary mode has short-interval second-moment scale

$$
NH^2N^{-\kappa},
$$

so the critical aggregate residual exponent is naturally $\xi=\kappa$. Any fixed excess beyond $\kappa$ would remove that boundary contribution and activate the seeded amplifier.

The pair-residual route is therefore closer to the root observable than the shifted-Möbius auxiliary route and does not require an unproved additive pole-transport bridge.

F-RH-017-v3 remains the canonical general root frontier, but F-RH-022 is now the preferred **ordinary-prime arithmetic subfrontier**.

No RH theorem is claimed.

---

# 1. Short-interval second moment

Define

$$
\boxed{
\Lambda_0(n)=\Lambda(n)-1.
}
$$

Then

$$
\boxed{
U_H(n)
=
\sum_{h=1}^{H}
\Lambda_0(n+h).
}
$$

Set

$$
\boxed{
M_2(N,H)
=
\sum_{n\le N}
U_H(n)^2.
}
$$

Expanding the square,

$$
\boxed{
M_2(N,H)
=
\sum_{1\le h_1,h_2\le H}
\sum_{n\le N}
\Lambda_0(n+h_1)
\Lambda_0(n+h_2).
}
$$

Split into diagonal and distinct-shift contributions.

---

# 2. Diagonal term

Let

$$
D_2(N,H)
=
\sum_{h\le H}
\sum_{n\le N}
\Lambda_0(n+h)^2.
$$

The prime number theorem and partial summation give

$$
\sum_{m\le X}\Lambda(m)^2
=
X\log X
+
O(X),
$$

at the precision needed here.

Since

$$
\Lambda_0^2
=
\Lambda^2-2\Lambda+1,
$$

we also have

$$
\boxed{
\sum_{m\le X}
\Lambda_0(m)^2
=
X\log X
+
O(X).
}
$$

Shifting the $N$ -length interval by at most $H$ changes the sum by

$$
O(H\log^2N).
$$

Summing over $h$ gives:

## Theorem 2.1 — Diagonal prime-square term

$$
\boxed{
D_2(N,H)
=
NH\log N
+
O
\left(
NH
+
H^2\log^2N
\right).
}
$$

Record:

```text
B-RH-099
SHORT_INTERVAL_LAMBDA0_DIAGONAL_EQUALS_NH_LOG_N_AT_EXPONENT_RESOLUTION
CERTIFIED
```

---

# 3. Modified singular series

For a finite set $\mathcal D$ of distinct shifts, Montgomery and Soundararajan define the modified singular series

$$
\boxed{
\mathfrak S_0(\mathcal D)
=
\sum_{\mathcal I\subseteq\mathcal D}
(-1)^{|\mathcal I|}
\mathfrak S(\mathcal I).
}
$$

The Hardy–Littlewood prime-tuple conjecture is equivalently written, for distinct shifts, as

$$
\sum_{n\le N}
\prod_{d\in\mathcal D}
\Lambda_0(n+d)
=
N\mathfrak S_0(\mathcal D)
+
\text{error}.
$$

For $|\mathcal D|=2$, define

$$
\boxed{
E_0(N;h_1,h_2)
=
\sum_{n\le N}
\Lambda_0(n+h_1)\Lambda_0(n+h_2)
-
N\mathfrak S_0(\{h_1,h_2\}).
}
$$

No Hardy–Littlewood assumption is made in this definition.

---

# 4. Exact local singular-series average

Define

$$
R_2(H)
=
\sum_{\substack{1\le h_1,h_2\le H\\h_1\ne h_2}}
\mathfrak S_0(\{h_1,h_2\}).
$$

Montgomery and Soundararajan prove:

## Theorem 4.1 — Montgomery–Soundararajan local pair average

For every fixed $\varepsilon>0$,

$$
\boxed{
R_2(H)
=
-H\log H
+
AH
+
O_\varepsilon
\left(
H^{1/2+\varepsilon}
\right),
}
$$

where

$$
A
=
2-\gamma-\log(2\pi)
$$

in their normalization.

This theorem is unconditional.

It is a theorem about the singular series itself, not about the actual prime-pair correlations.

Record:

```text
B-RH-100
MODIFIED_SINGULAR_SERIES_PAIR_AVERAGE_PRODUCES_MINUS_H_LOG_H
CERTIFIED_EXTERNAL_THEOREM
```

---

# 5. Exact pair-error aggregate

Define

$$
\boxed{
\mathcal R_{\rm HL}^{(2)}(N,H)
=
\sum_{\substack{1\le h_1,h_2\le H\\h_1\ne h_2}}
E_0(N;h_1,h_2).
}
$$

Then the distinct-shift contribution to $M_2$ is exactly

$$
\boxed{
N R_2(H)
+
\mathcal R_{\rm HL}^{(2)}(N,H).
}
$$

Combining Sections 2 and 4:

## Theorem 5.1 — Exact local-factor / global-residual decomposition

$$
\boxed{
\begin{aligned}
M_2(N,H)
&=
NH\log\frac NH
+
B\,NH
+
\mathcal R_{\rm HL}^{(2)}(N,H)
\\
&\quad
+
O_\varepsilon
\left(
NH^{1/2+\varepsilon}
+
H^2\log^2N
\right),
\end{aligned}
}
$$

for an absolute constant $B$ depending only on the normalization of the diagonal and singular-series constants.

Record:

```text
B-RH-101
ROOT_SHORT_INTERVAL_SECOND_MOMENT_EQUALS_SOLVED_LOCAL_VARIANCE_PLUS_AGGREGATE_HL_PAIR_ERROR
CERTIFIED
```

The numerical value of $B$ is irrelevant to every fixed-power conclusion below.

---

# 6. Solved local variance scale

Take

$$
H=N^{1-\tau},
\qquad
0<\tau<1.
$$

Then

$$
NH\log\frac NH
=
\tau
NH\log N.
$$

Relative to the trivial MLEPG scale

$$
NH^2,
$$

$$
\boxed{
NH\log\frac NH
=
NH^2
N^{-(1-\tau)+o(1)}.
}
$$

Thus the solved local arithmetic has lag exponent

$$
\boxed{
\delta_{\rm local}
=
1-\tau.
}
$$

This is exactly the variance scale predicted by Montgomery–Soundararajan and by the pair-correlation philosophy.

---

# 7. Pair-residual power hypothesis

Assume

$$
\boxed{
|\mathcal R_{\rm HL}^{(2)}(N,H)|
\ll
NH^2
N^{-\xi+o(1)}
}
$$

for some fixed $\xi>0$.

The lower-order terms in Theorem 5.1 have lag exponents at least $1-\tau$ or larger at every fixed-power resolution relevant before the endpoint.

Therefore:

## Theorem 7.1 — Pair-residual to MLEPG exponent

$$
\boxed{
M_2(N,H)
\ll
NH^2
N^{-\delta+o(1)},
}
$$

with

$$
\boxed{
\delta
=
\min
\{1-\tau,\xi\}.
}
$$

Record:

```text
B-RH-102
AVERAGED_HL_PAIR_RESIDUAL_POWER_CONVERTS_DIRECTLY_TO_MLEPG
CERTIFIED
```

---

# 8. Seeded PESC amplifier

Paper 54 proves that if

$$
H=N^\alpha
$$

and the lag exponent is $\delta$, then a PESC $(\kappa)$ seed yields every exponent

$$
\kappa'
<
\min
\left\{
\alpha,\,
\delta,\,
2-\alpha(2-\kappa)
\right\}.
$$

Set

$$
\alpha=1-\tau.
$$

Using Theorem 7.1:

## Theorem 8.1 — Averaged pair-residual amplifier map

$$
\boxed{
\kappa'
<
\Phi_{\rm pair}
(\kappa;\tau,\xi)
=
\min
\left\{
1-\tau,\,
\xi,\,
\kappa+\tau(2-\kappa)
\right\}.
}
$$

Create:

```text
B-RH-103
AVERAGED_HARDY_LITTLEWOOD_PAIR_RESIDUAL_SEEDED_PESC_AMPLIFIER
CERTIFIED
```

---

# 9. Exact strict gate and gain

Strict amplification occurs iff every active term exceeds $\kappa$.

The anchor term satisfies

$$
\kappa+\tau(2-\kappa)>\kappa
$$

for every $\tau>0$.

Thus the only nontrivial conditions are

$$
\boxed{
1-\tau>\kappa
}
$$

and

$$
\boxed{
\xi>\kappa.
}
$$

Equivalently:

## Corollary 9.1 — Pair-residual strict amplifier gate

$$
\boxed{
\tau<1-\kappa,
\qquad
\xi>\kappa.
}
$$

The gain may be any

$$
\boxed{
0<\eta
<
\min
\left\{
1-\tau-\kappa,\,
\xi-\kappa,\,
\tau(2-\kappa)
\right\}.
}
$$

This is one of the simplest arithmetic amplifier gates in Campaign 46.

---

# 10. Optimal scale if the pair residual is not the bottleneck

Suppose

$$
\xi
$$

is large enough not to be active.

Balance

$$
1-\tau-\kappa
$$

with

$$
\tau(2-\kappa).
$$

This gives

$$
\boxed{
\tau_*
=
\frac{1-\kappa}{3-\kappa}.
}
$$

The corresponding gain is

$$
\boxed{
\eta_*
=
\frac{
(1-\kappa)(2-\kappa)
}{
3-\kappa
}.
}
$$

Thus a sufficiently strong pair-residual theorem would produce a substantial one-step bootstrap.

---

# 11. New arithmetic root subfrontier F-RH-022

Open:

```text
F-RH-022
AVERAGED_HARDY_LITTLEWOOD_PAIR_RESIDUAL_EXCESS
```

Target:

for a PESC $(\kappa)$ seed, find fixed

$$
\tau,\eta>0
$$

with

$$
\tau<1-\kappa
$$

such that

$$
\boxed{
|\mathcal R_{\rm HL}^{(2)}(N,N^{1-\tau})|
\ll
N
\left(
N^{1-\tau}
\right)^2
N^{-\kappa-\eta}.
}
$$

This is a direct sufficient root theorem.

It requires no shifted-Möbius sampling bridge and no individual twin-prime asymptotic.

---

# 12. Why F-RH-022 is weaker than uniform twin primes

A uniform quantitative Hardy–Littlewood pair conjecture would require, for every relevant difference,

$$
E_0(N;h_1,h_2)
$$

to be individually small.

F-RH-022 requires only

$$
\boxed{
\sum_{h_1\ne h_2}
E_0(N;h_1,h_2)
}
$$

to be small.

Large positive and negative pair errors are allowed to cancel.

This is precisely the aggregate cancellation which Montgomery and Soundararajan identify as the missing ingredient when extending their moment theorem to large $H$.

Thus F-RH-022 is a genuinely averaged prime-pair problem.

---

# 13. Current averaged Hardy–Littlewood technology

A strong average form of the prime-pair conjecture is known.

For prime indicators, current results imply that in polynomial shift ranges one has, for every fixed $A>0$, an $L^2$ average of the form

$$
\boxed{
\sum_{|r|\le H}
\left|
\frac1N
\sum_{N<n\le2N}
1_{\mathbb P}(n)
1_{\mathbb P}(n+r)
-
\mathfrak S(r)
\left(
\frac{\pi(N)}N
\right)^2
\right|^2
\ll
\frac{
H
}{
\log^{A+2}N
}
}
$$

in the established ranges.

Mikawa proved almost-all prime-pair asymptotics for

$$
H\ge N^{1/3+\varepsilon},
$$

and Matomäki–Radziwiłł–Tao improved the shift-window range to

$$
H\ge N^{8/33+\varepsilon}
$$

for the relevant almost-all statement.

At exponent resolution, standard dyadic partial summation converts the logarithmically weighted von Mangoldt version into the same **arbitrary logarithmic saving class**.

Thus current technology controls the pair errors very strongly on average, but only by powers of $\log N$.

---

# 14. Why arbitrary logarithmic average is still subcritical

Suppose schematically that the weighted pair errors satisfy

$$
\sum_{r\le H}
|E_r(N)|^2
\ll
H N^2
(\log N)^{-A}
$$

for arbitrary fixed $A$.

The triangular aggregate obeys Cauchy:

$$
\begin{aligned}
\left|
\sum_{r<H}
(H-r)E_r(N)
\right|
&\le
\left(
\sum_{r<H}
(H-r)^2
\right)^{1/2}
\left(
\sum_{r<H}
|E_r(N)|^2
\right)^{1/2}
\\
&\ll
\boxed{
NH^2
(\log N)^{-A/2}.
}
\end{aligned}
$$

This is

$$
NH^2N^{-o(1)},
$$

so its fixed-power exponent is

$$
\boxed{
\xi=0
}
$$

in the CSM_RH ledger.

F-RH-022 requires

$$
\boxed{
\xi>\kappa>0.
}
$$

Therefore the current averaged Hardy–Littlewood theorem does not itself activate the seeded amplifier.

Create:

```text
O-RH-162
CURRENT_AVERAGED_PRIME_PAIR_THEOREMS_GIVE_ARBITRARY_LOG_SAVING_BUT_NO_F_RH_022_FIXED_POWER
CERTIFIED_AS_EXTERNAL_TECHNOLOGY_GAP
```

---

# 15. Singular-series cancellation is not the missing power

Theorem 4.1 already gives a power-sized error

$$
O(H^{1/2+\varepsilon})
$$

for the purely local singular-series average.

Thus the local Euler-product geometry is known far more precisely than required for F-RH-022.

The missing term is solely

$$
\boxed{
\mathcal R_{\rm HL}^{(2)}.
}
$$

This is an important distinction.

The root problem is no longer:

```text
understand the average singular series.
```

That part is solved.

It is:

```text
prove fixed-power cancellation of the actual prime-pair errors around that local series.
```

---

# 16. Boundary criticality calibration

A smooth boundary prime-error mode with

$$
\beta=1-\frac{\kappa}{2}
$$

has fixed- $H$ lag energy

$$
\boxed{
NH^2N^{-\kappa}
}
$$

at exponent resolution.

When

$$
\tau<1-\kappa,
$$

the solved local variance

$$
NH\log(N/H)
$$

is smaller:

$$
1-\tau>\kappa.
$$

Therefore a boundary-sized mode must live in the global pair-residual sector rather than in the local singular-series main term.

This calibrates

$$
\boxed{
\xi=\kappa
}
$$

as the critical pair-residual exponent.

F-RH-022 asks for any fixed excess

$$
\boxed{
\xi>\kappa.
}
$$

The statement is a boundary-mode calibration, not a proof that an actual boundary zero gives a pointwise lower bound for $\mathcal R_{\rm HL}^{(2)}$ at every scale.

---

# 17. Relation to pair correlation of zeta zeros

Goldston and Montgomery proved, under RH, that the strong pair-correlation conjecture for zeta zeros is equivalent to the corresponding second-moment asymptotic for primes in short intervals.

Montgomery and Soundararajan predict

$$
\boxed{
M_2(N,H)
\sim
NH\log(N/H)
}
$$

in the polynomial short-interval range.

Thus the conjectural final scale corresponds to

$$
\boxed{
\delta_{\rm expected}
=
1-\tau.
}
$$

For every seed satisfying

$$
\kappa<1-\tau,
$$

this lies strictly beyond the current PESC exponent.

Hence the arithmetic target is compatible with the standard conjectural variance scale.

This is calibration only; RH or pair correlation is not assumed.

---

# 18. Campaign status

After Paper 71:

```text
F-RH-017-v3:
CANONICAL GENERAL ROOT FRONTIER / OPEN.

F-RH-022:
PREFERRED ORDINARY-PRIME ARITHMETIC SUBFRONTIER / OPEN.

F-RH-020:
AUXILIARY PARITY-ENERGY FRONTIER / DE-PRIORITIZED.

F-RH-021R:
HIGH-COST AUXILIARY BRIDGE / DE-PRIORITIZED.
```

The direct arithmetic unknown is now:

$$
\boxed{
\text{fixed-power cancellation of the aggregate pair errors}
}
$$

after the singular-series main term has been exactly removed.

---

# 19. Recommended next action

The next round should inspect the proof of the modern averaged prime-pair theorem itself.

Question:

```text
Can a PESC fixed-strip seed upgrade
the existing arbitrary-log averaged Hardy–Littlewood residual
to a fixed-power aggregate residual?
```

The audit should separate:

1. local singular-series major arcs — already solved;
2. polynomial-conductor frequencies — likely large-sieve suppressible;
3. fixed low-conductor spectral channels;
4. bilinear/minor-arc pair-error terms.

Unlike the shifted-Möbius route, every gain here feeds the root second moment directly.

No extra coercivity bridge is required.

---

# 20. External calibration

## 20.1. Montgomery–Soundararajan singular-series moments

H. L. Montgomery and K. Soundararajan,
*Primes in short intervals*,
Communications in Mathematical Physics 252 (2004), 589–617.

They prove

$$
R_2(H)
=
-H\log H
+
AH
+
O(H^{1/2+\varepsilon})
$$

and conjecture the short-interval second moment

$$
M_2(N,H)
\sim
NH\log(N/H)
$$

in polynomial ranges.

URL:

https://arxiv.org/abs/math/0409258

## 20.2. Averaged prime-pair results

Modern averaged Hardy–Littlewood results imply prime-pair asymptotics for almost all shifts with arbitrary logarithmic exceptional savings.

A convenient summary is in:

N. Evans,
*Correlations of almost primes*,
Mathematical Proceedings of the Cambridge Philosophical Society 173 (2022).

The introduction records the prime-pair $L^2$ averaged estimate and the ranges obtained by Mikawa and by Matomäki–Radziwiłł–Tao.

URL:

https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/correlations-of-almost-primes/08F8E4E4C36F68ED6DDA373CCAF7A221

---

# 21. State transition

Advance candidate state

$$
v1.61
\to
v1.62.
$$

Add:

```text
B-RH-099
SHORT_INTERVAL_LAMBDA0_DIAGONAL_EQUALS_NH_LOG_N_AT_EXPONENT_RESOLUTION

B-RH-100
MODIFIED_SINGULAR_SERIES_PAIR_AVERAGE_PRODUCES_MINUS_H_LOG_H

B-RH-101
ROOT_SHORT_INTERVAL_SECOND_MOMENT_EQUALS_SOLVED_LOCAL_VARIANCE_PLUS_AGGREGATE_HL_PAIR_ERROR

B-RH-102
AVERAGED_HL_PAIR_RESIDUAL_POWER_CONVERTS_DIRECTLY_TO_MLEPG

B-RH-103
AVERAGED_HARDY_LITTLEWOOD_PAIR_RESIDUAL_SEEDED_PESC_AMPLIFIER

O-RH-162
CURRENT_AVERAGED_PRIME_PAIR_THEOREMS_GIVE_ARBITRARY_LOG_SAVING_BUT_NO_F_RH_022_FIXED_POWER
```

Open:

```text
F-RH-022
AVERAGED_HARDY_LITTLEWOOD_PAIR_RESIDUAL_EXCESS
OPEN_ROOT_SUBFRONTIER
```

No RH certificate is created.

---

# 22. Conclusion

The local pair arithmetic is not the unresolved part of the short-interval variance.

Montgomery–Soundararajan already proved that its aggregate contributes

$$
-H\log H
$$

and converts the diagonal

$$
NH\log N
$$

into the correct

$$
NH\log(N/H)
$$

variance scale.

The entire remaining root uncertainty is the aggregate error of the actual prime-pair correlations around the Hardy–Littlewood local prediction.

If that aggregate saves any fixed exponent beyond the current PESC seed,

$$
\xi>\kappa,
$$

at a scale

$$
H=N^{1-\tau},
\qquad
\tau<1-\kappa,
$$

the seeded amplifier fires immediately.

This is F-RH-022.

It is currently the shortest ordinary-prime arithmetic subproblem in the CSM_RH campaign.
