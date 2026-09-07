# CSM_RH Paper 25
## Collision Elimination, Raw-Sieve Centering Debt, and the Fully Distinct Four-Point Core

**Project:** `CSM_RH`  
**Paper:** `25`  
**Version:** `v0.1`  
**Date:** `2026-09-06`  
**Parent state:** `CSM_RH v1.15 / Paper 24`  
**Campaign:** `24 — CENTERED_FOURTH_MOMENT_ATTACK`  
**Status:** exact fourth-moment reduction / current-technology audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 24 introduced C4HEG:

$$
\mathcal M_{4,X}(H)
\ll
XH^{4-\eta}
(\log X)^{O(1)}
$$

for some fixed $\eta>0$ at a polynomial lag $H=X^\alpha$.

Campaign 24 asks whether this is already contained in known sieve/higher-uniformity technology and, if not, which part of the fourth moment is genuinely new.

The answer is:

```text
collision patterns:
  harmless at H^3 scale

fully distinct four-point sector:
  only H^4-sized combinatorial sector

raw Gallagher/Klimov moment bounds:
  uncentered; no legal centered cancellation

2026 higher uniformity:
  powerful but log/subpower for Lambda

fixed H-exponent gain:
  still open
```

No live GLM-5.3-Flash run is claimed.

---

# 1. Centered fourth short-interval moment

Let

$$
a_n
=
\Lambda(n)-1
$$

on a finite prime block and extend by zero outside.

Define

$$
U_H(x)
=
\sum_{r=1}^{H}a_{x+r}.
$$

Define

$$
\boxed{
\mathcal M_{4,X}(H)
=
\sum_x
U_H(x)^4.
}
$$

Since $a_n$ is real, no complex-conjugation convention is needed here.

Expand:

$$
\boxed{
\mathcal M_{4,X}(H)
=
\sum_{1\le r_1,r_2,r_3,r_4\le H}
\sum_x
a_{x+r_1}
a_{x+r_2}
a_{x+r_3}
a_{x+r_4}.
}
$$

---

# 2. Partition by offset collisions

The ordered quadruple of offsets has one of the five multiplicity partitions:

```text
[4]
[3,1]
[2,2]
[2,1,1]
[1,1,1,1]
```

Write

$$
\mathcal M_4
=
\mathcal Q_{4}
+
\mathcal Q_{31}
+
\mathcal Q_{22}
+
\mathcal Q_{211}
+
\mathcal Q_{1111}.
$$

The exact pieces are:

## All four equal

$$
\boxed{
\mathcal Q_4
=
\sum_{r}
\sum_x
a_{x+r}^4.
}
$$

## Three plus one

$$
\boxed{
\mathcal Q_{31}
=
4
\sum_{r\ne s}
\sum_x
a_{x+r}^3a_{x+s}.
}
$$

## Two plus two

$$
\boxed{
\mathcal Q_{22}
=
6
\sum_{r<s}
\sum_x
a_{x+r}^2a_{x+s}^2.
}
$$

## Two plus one plus one

$$
\boxed{
\mathcal Q_{211}
=
12
\sum_r
\sum_{\substack{s<t\\s,t\ne r}}
\sum_x
a_{x+r}^2a_{x+s}a_{x+t}.
}
$$

## Fully distinct

$$
\boxed{
\mathcal Q_{1111}
=
24
\sum_{r_1<r_2<r_3<r_4}
\sum_x
a_{x+r_1}
a_{x+r_2}
a_{x+r_3}
a_{x+r_4}.
}
$$

Define

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
=
\mathcal Q_{1111}.
}
$$

---

# 3. Collision bound

On the relevant range,

$$
|a_n|
\ll
\log X.
$$

Every collision partition has at most three free offset parameters.

There are $O(X)$ contributing translations $x$.

Therefore:

## Theorem 3.1 — Collision Sector Bound

$$
\boxed{
|
\mathcal Q_{4}
|
+
|
\mathcal Q_{31}
|
+
|
\mathcal Q_{22}
|
+
|
\mathcal Q_{211}
|
\ll
XH^3
(\log X)^4.
}
$$

No prime-correlation theorem is needed.

The estimate is purely combinatorial.

---

# 4. Fully distinct reduction

Let

$$
0<\eta\le1.
$$

Suppose

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
\ll
XH^{4-\eta}
(\log X)^C
}
$$

for some fixed $C$.

Then Theorem 3.1 gives

$$
\boxed{
\mathcal M_{4,X}(H)
\ll
XH^{4-\eta}
(\log X)^{O_C(1)}.
}
$$

Therefore:

## Theorem 4.1 — Distinct Four-Point Gain Implies C4HEG

For any fixed $0<\eta\le1$,

$$
\boxed{
\operatorname{D4HEG}(\alpha,\eta)
\Longrightarrow
\operatorname{C4HEG}(\alpha,\eta),
}
$$

where D4HEG is the one-sided upper bound on the fully distinct centered aggregate.

A separate power theorem for each four-point shift tuple is not required.

Only the complete signed three-dimensional shift aggregate needs the $H$ -exponent gain.

---

# 5. Automatic lower bound on the distinct aggregate

Because

$$
\mathcal M_{4,X}(H)\ge0,
$$

Theorem 3.1 also gives

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
\ge
-
O
\left(
XH^3(\log X)^4
\right).
}
$$

Thus for $0<\eta\le1$, a one-sided upper bound

$$
\mathcal A_{4,\mathrm{dist}}
\ll
XH^{4-\eta}\operatorname{polylog}X
$$

already controls the distinct sector at the required scale.

Large negative cancellation is not a separate danger.

---

# 6. Centered four-point correlation

For four distinct offsets

$$
r_1,r_2,r_3,r_4,
$$

define

$$
\boxed{
C_a(r_1,r_2,r_3,r_4)
=
\sum_x
\prod_{i=1}^{4}
[
\Lambda(x+r_i)-1
].
}
$$

Then

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}
=
24
\sum_{r_1<r_2<r_3<r_4}
C_a(r_1,r_2,r_3,r_4).
}
$$

Expansion by subsets gives the exact inclusion-exclusion identity

$$
\boxed{
C_a(\mathbf r)
=
\sum_{S\subseteq\{1,2,3,4\}}
(-1)^{4-|S|}
\sum_x
\prod_{i\in S}
\Lambda(x+r_i).
}
$$

The empty product is interpreted as $1$.

Thus centering couples the one-, two-, three-, and four-point prime correlations with exact signed coefficients.

---

# 7. Why raw sieve moments do not prove the centered result

Classical Gallagher/Klimov sieve moment bounds control the uncentered discrete moment

$$
\widetilde J_k(X,H)
=
\sum_{m\le X}
[
\psi(m+H)-\psi(m)
]^k
$$

at the schematic scale

$$
\boxed{
\widetilde J_k(X,H)
\le
\left[
P_k
\left(
\frac{H}{\log X}
\right)
+
\varepsilon
\right]
X\log^kX.
}
$$

For

$$
P_k(y)
=
\sum_{r=1}^{k}
\left\{
\begin{matrix}
k\\r
\end{matrix}
\right\}
2^r r!y^r,
$$

the fourth-order polynomial is

$$
\boxed{
P_4(y)
=
2y
+
56y^2
+
288y^3
+
384y^4.
}
$$

Hence at polynomial $H$ the raw upper-bound scale contains an $XH^4$ leading term.

---

# 8. Centering requires coherent signed main terms

The centered moment is

$$
\sum_m
[
Y_m-H
]^4,
$$

where

$$
Y_m
=
\psi(m+H)-\psi(m).
$$

Exactly,

$$
\boxed{
\sum_m(Y_m-H)^4
=
J_4
-
4HJ_3
+
6H^2J_2
-
4H^3J_1
+
XH^4
}
$$

up to harmless endpoint conventions.

To cancel the $H^4$ and $H^3$ scales, one needs compatible asymptotic main terms for the separate moments $J_r$.

Independent one-sided upper bounds do not permit this cancellation.

The Gallagher/Klimov constants in $P_r$ are sieve-majorant constants, not a coherent signed probability law.

Create:

```text
O-RH-053
UNCENTERED_SIEVE_MOMENT_CENTERING_DEBT
status:
  CERTIFIED
```

Statement:

> An upper bound for each uncentered moment cannot be inserted into the alternating binomial formula for the centered moment as though the upper-bound main coefficients cancelled.

---

# 9. Conditional higher-moment calibration

Montgomery and Soundararajan predict an approximately Gaussian centered short-interval prime count with variance

$$
H\log(X/H)
$$

at polynomial scales.

Their higher-moment formulas, under strong Hardy–Littlewood input, predict for the fourth centered moment a scale

$$
\boxed{
X
[
H\log(X/H)
]^2.
}
$$

Chan's higher-moment work studies equivalences between higher even short-interval moments under RH and related strong information.

These results show that the expected centered scale is much smaller than $XH^4$.

They do not provide an unconditional C4HEG theorem.

---

# 10. 2026 higher-uniformity calibration

Current higher-uniformity theory gives for the von Mangoldt function:

$$
\Lambda-\Lambda^\sharp
$$

is highly discorrelated from nilsequences on almost all short intervals, with arbitrary logarithmic accuracy in the stated ranges.

It also gives asymptotically small short-interval Gowers norms and, as an application, $\ell$ -point Hardy–Littlewood correlations with one averaging shift variable.

For the prime case the quantitative gain remains logarithmic/subpower rather than a fixed power in $X$ or $H$.

Therefore using the generalized von Neumann theorem on the fully distinct sector can at current strength yield at best a subpower relative error unless a new power-saving uniformity estimate is supplied.

---

# 11. One-shift versus three-shift geometry

The explicit 2026 Hardy–Littlewood application has one averaging parameter:

$$
\sum_{n\le X}
\Lambda(n)
\Lambda(n+h)
\cdots
\Lambda(n+(\ell-1)h).
$$

The fully distinct fourth-moment aggregate has three independent relative shift degrees of freedom:

$$
r_2-r_1,
\qquad
r_3-r_1,
\qquad
r_4-r_1.
$$

The underlying Gowers-uniformity machinery can address richer finite-complexity systems, but its current quantitative prime saving remains subpower.

Thus increasing shift dimension does not manufacture an $H^{-\eta}$ gain from the existing log-power estimates.

---

# 12. Contrast with divisor functions

The 2026 higher-uniformity paper proves, for $d_2$ against a fixed linear phase in a suitable short-interval range, a genuine power-saving estimate of the form

$$
X^{-c\varepsilon}.
$$

The corresponding general $\Lambda$ discorrelation results in that work remain at arbitrary logarithmic saving.

This contrast is useful calibration:

```text
power-saving short-interval discorrelation:
  reachable for some divisor problems

same type of fixed power for Lambda:
  not presently supplied
```

The prime-specific obstruction is therefore visible inside the current technology itself.

---

# 13. Current four-point core

After collision elimination, the first genuinely unresolved nonlinear arithmetic object is

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
=
24
\sum_{r_1<r_2<r_3<r_4\le H}
\sum_x
\prod_{i=1}^{4}
[
\Lambda(x+r_i)-1
].
}
$$

A sufficient theorem is:

## D4HEG $(\alpha,\eta)$

For

$$
H=X^\alpha
$$

and some fixed

$$
0<\eta\le1,
$$

$$
\boxed{
\mathcal A_{4,\mathrm{dist}}(X,H)
\ll
XH^{4-\eta}
(\log X)^{O(1)}.
}
$$

This contains no fixed $X$ -power in its statement.

At polynomial $H$ it generates one.

---

# 14. Strength chain

D4HEG gives:

$$
\boxed{
\operatorname{D4HEG}
\Longrightarrow
\operatorname{C4HEG}
}
$$

by Theorem 4.1.

Paper 24 gives:

$$
\boxed{
\operatorname{C4HEG}
\Longrightarrow
\operatorname{MLEPG}
}
$$

through Hölder at one polynomial scale.

Paper 17 gives:

$$
\boxed{
\operatorname{MLEPG}
\Longrightarrow
\text{fixed-power PNT mean square}.
}
$$

Paper 20 gives:

$$
\boxed{
\text{fixed-power PNT mean square}
\Longrightarrow
\text{fixed zeta zero strip}.
}
$$

No arrow in this chain is claimed to prove the input D4HEG.

---

# 15. Campaign 24 track audit

## M1 — averaged four-point Hardy–Littlewood

```text
status:
  CURRENT ONE-SHIFT THEOREMS / GOWERS INPUT GIVE SUBPOWER PRECISION

fixed H-exponent gain:
  NOT IDENTIFIED
```

## M2 — centered Selberg/Klimov moment method

```text
status:
  RAW MOMENTS CONTROLLED
  CENTERING CANCELLATION NOT CERTIFIED FROM UPPER BOUNDS
```

## M3 — short-interval higher uniformity

```text
status:
  STRONG STRUCTURAL CONTROL
  PRIME QUANTITATIVE SAVING LOG/SUBPOWER
```

## M4 — sieve approximant plus residual

```text
status:
  MODEL COMPUTABLE
  RESIDUAL FOURTH-MOMENT POWER FIDELITY OPEN
```

## M5 — fourth cumulant

```text
status:
  USEFUL ORGANIZATION
  CONNECTED FULLY DISTINCT SECTOR REMAINS OPEN
```

---

# 16. New obstruction: collision shell is not the barrier

Create:

```text
O-RH-054
FOURTH_MOMENT_COLLISION_SHELL_HARMLESS
status:
  CERTIFIED
```

Statement:

> All fourth-moment offset configurations containing a collision contribute at most $XH^3(\log X)^4$. For any target gain $0<\eta\le1$, the fixed $H$ -exponent obstruction lies entirely in the fully distinct sector.

---

# 17. New mechanism subfrontier

Create:

```text
F-RH-019
FULLY_DISTINCT_CENTERED_FOUR_POINT_H_EXPONENT_GAP
abbrev:
  D4HEG
status:
  OPEN
type:
  MECHANISM SUBFRONTIER
```

Root target remains:

```text
F-RH-010
PESC
```

Direct theorem candidate remains:

```text
F-RH-016
MLEPG
```

Nonlinear theorem candidate remains:

```text
F-RH-018
C4HEG
```

D4HEG is the first irreducible four-point sublemma for C4HEG.

---

# 18. Campaign 25

The next campaign is:

```text
CSM_RH Campaign 25
FULLY_DISTINCT_FOUR_POINT_ATTACK
```

The target does not move beyond D4HEG as a sublemma.

---

# 19. Campaign 25 tracks

## F1 — exact $\Lambda^\sharp$ / residual decomposition

Write

$$
\Lambda-1
=
(\Lambda^\sharp-1)
+
(\Lambda-\Lambda^\sharp)
$$

inside the fully distinct aggregate.

Compute the pure model term exactly enough to identify its $H$ exponent.

Audit every mixed residual term without early absolute-value leakage.

## F2 — three-dimensional generalized von Neumann

Use short-interval $U^s$ uniformity to control the fully distinct three-shift average.

Determine the exact quantitative dependence needed to turn log-power uniformity into an $H^{-\eta}$ saving.

## F3 — singular-series centered average

Average the four-point singular series over all distinct triples of relative shifts and determine which lower-order one-, two-, and three-point model terms cancel after exact centering.

## F4 — connected fourth cumulant

Define the connected prime four-point function after subtracting all pairings and lower-order singular-series contributions.

Test whether C4HEG reduces to an $H$ -exponent bound on that connected component.

## F5 — divisor/primes technology transfer

Use the power-saving $d_2$ short-interval discorrelation theorem as a model proof.

Locate the exact input which fails when $d_2$ is replaced by $\Lambda$.

---

# 20. Campaign 25 rejection filters

Reject a candidate if:

## R1. It applies uncentered moment upper bounds inside a signed centered identity.

## R2. It assumes the prime $4$ -tuple conjecture.

## R3. It gets only $\log^{-A}X$ or $H^{-o(1)}$.

## R4. It proves a fixed power only for collision configurations.

## R5. It takes absolute values of all distinct four-point correlations before using the three-dimensional average.

## R6. It treats one-shift Hardy–Littlewood as though it directly controlled all three independent shift variables.

---

# 21. State transition

```text
CSM_RH v1.15
  ->
CSM_RH v1.16
```

with:

```text
Campaign 24
  CLOSED_AS_COLLISION_REDUCTION_AND_CURRENT_TECHNOLOGY_AUDIT

O-RH-053
  UNCENTERED_SIEVE_MOMENT_CENTERING_DEBT
  CREATED / CERTIFIED

O-RH-054
  FOURTH_MOMENT_COLLISION_SHELL_HARMLESS
  CREATED / CERTIFIED

F-RH-018
  C4HEG
  REMAINS OPEN

F-RH-019
  D4HEG
  CREATED / OPEN / MECHANISM SUBFRONTIER

Campaign 25
  FULLY_DISTINCT_FOUR_POINT_ATTACK
  READY
```

---

# 22. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

C4HEG = OPEN

D4HEG = OPEN

COLLISION FOURTH-MOMENT SECTOR = CLOSED / HARMLESS

RAW SIEVE MOMENT -> CENTERED MOMENT = INVALID WITHOUT COHERENT MAIN TERMS

2026 PRIME HIGHER UNIFORMITY = SUBPOWER QUANTITATIVE STRENGTH

FULLY DISTINCT THREE-SHIFT AVERAGE = CURRENT FOUR-POINT CORE

NEXT CAMPAIGN = 25
```

The concrete open sublemma is:

$$
\boxed{
\sum_{1\le r_1<r_2<r_3<r_4\le X^\alpha}
\sum_x
\prod_{i=1}^{4}
[
\Lambda(x+r_i)-1
]
\ll
X
\left(
X^\alpha
\right)^{4-\eta}
(\log X)^{O(1)}
}
$$

for some fixed $\alpha\in(0,1)$ and some fixed $\eta\in(0,1]$.

A fixed $H$ -exponent gain in this fully distinct aggregate is enough to generate a fixed prime-side power through the already certified chain.
