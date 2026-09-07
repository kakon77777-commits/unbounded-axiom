# CSM_RH Paper 09
## Heath-Brown $K=3$ Unit-Sector Ledger and Fixed- $K$ Rough-Prime Persistence

**Project:** `CSM_RH`  
**Paper:** `09`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v0.9 / Paper 08`  
**Campaign:** `08 — CANONICAL_HEATH_BROWN_K3_ZERO_FREQUENCY_LEDGER`  
**Status:** exact combinatorial ledger / fixed- $K$ obstruction theorem; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

Canonical root state:

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

The paper pins the Heath-Brown identity at $K=3$, performs the alternating cancellation before any absolute values are taken, and groups the result by the number of non-unit truncated Möbius factors.

The main result is stronger than the initial $K=3$ audit:

> the all-unit sector survives for every fixed $K$, and on every $U$ -rough integer in the validity range it is exactly equal to $\Lambda$.

Therefore increasing a fixed Heath-Brown depth cannot algebraically remove the rough prime / prime-power channel.

No live GLM-5.3-Flash run is claimed.

---

# 1. Pinned Heath-Brown identity

Let

$$
L(n)=\log n.
$$

Let

$$
\delta(1)=1,
\qquad
\delta(n)=0
\quad
(n>1).
$$

Let $*$ denote Dirichlet convolution.

Set

$$
X=2N
$$

and

$$
\boxed{
U
=
\left\lceil
X^{1/3}
\right\rceil.
}
$$

Define

$$
\mu_{\le U}(n)
=
\mu(n)
\mathbf 1_{n\le U}.
$$

For $K=3$, the Heath-Brown identity is

$$
\boxed{
\Lambda
=
3\mu_{\le U}*L
-
3\mu_{\le U}^{*2}*\mathbf1*L
+
\mu_{\le U}^{*3}*\mathbf1^{*2}*L
}
$$

throughout

$$
1\le n<X.
$$

The full-range validity follows directly from the standard proof: if

$$
\mu_{>U}
=
\mu-\mu_{\le U},
$$

then every factor in

$$
\mu_{>U}^{*3}*\mathbf1^{*2}*L
$$

contains three integers strictly larger than $U$, so their product is larger than

$$
U^3
\ge
X.
$$

Hence this convolution vanishes on $n<X$.

Expanding

$$
\mu_{>U}
=
\mu-\mu_{\le U}
$$

and using

$$
\mu*\mathbf1=\delta,
\qquad
\mu*L=\Lambda
$$

gives the identity.

---

# 2. Unit / non-unit Möbius split

Write

$$
\boxed{
\mu_{\le U}
=
\delta+\nu,
}
$$

where

$$
\nu(1)=0
$$

and

$$
\nu(n)
=
\mu(n)
\mathbf1_{2\le n\le U}.
$$

Substitute this into the pinned $K=3$ identity.

After expanding the alternating $j=1,2,3$ terms before taking any absolute values, one obtains

$$
\boxed{
\Lambda
=
Q_0+Q_1+Q_2+Q_3,
}
$$

where $Q_r$ collects exactly $r$ non-unit truncated Möbius factors.

---

# 3. Exact $K=3$ sectors

## Sector $Q_0$ — all Möbius factors are units

$$
\boxed{
Q_0
=
3L
-
3\mathbf1*L
+
\mathbf1^{*2}*L.
}
$$

## Sector $Q_1$ — one non-unit Möbius factor

$$
\boxed{
Q_1
=
3\nu*L
-
6\nu*\mathbf1*L
+
3\nu*\mathbf1^{*2}*L.
}
$$

Equivalently,

$$
Q_1
=
3\nu*
[
\delta
-
2\mathbf1
+
\mathbf1^{*2}
]
*L.
$$

## Sector $Q_2$ — two non-unit Möbius factors

$$
\boxed{
Q_2
=
-3\nu^{*2}*\mathbf1*L
+
3\nu^{*2}*\mathbf1^{*2}*L.
}
$$

Equivalently,

$$
Q_2
=
3\nu^{*2}*
[
\mathbf1^{*2}
-
\mathbf1
]
*L.
$$

## Sector $Q_3$ — three non-unit Möbius factors

$$
\boxed{
Q_3
=
\nu^{*3}*\mathbf1^{*2}*L.
}
$$

No unit configuration has been dropped.

---

# 4. Divisor-polynomial form of the all-unit sector

Let

$$
d_j
=
\mathbf1^{*j}
$$

be the ordered $j$ -fold divisor function.

By symmetry over the $j$ ordered factors,

$$
\boxed{
[
\mathbf1^{*(j-1)}*L
](n)
=
\frac{d_j(n)}{j}
\log n.
}
$$

Therefore for $K=3$,

$$
\boxed{
Q_0(n)
=
\log n
\left[
3
-
\frac32d_2(n)
+
\frac13d_3(n)
\right].
}
$$

This is an exact arithmetic function.

---

# 5. What the alternating unit algebra actually cancels

For a prime $p$,

$$
d_2(p)=2,
\qquad
d_3(p)=3.
$$

Hence

$$
Q_0(p)
=
\log p.
$$

For distinct primes $p,q$,

$$
d_2(pq)=4,
\qquad
d_3(pq)=9,
$$

so

$$
Q_0(pq)=0.
$$

For a prime square,

$$
d_2(p^2)=3,
\qquad
d_3(p^2)=6,
$$

and therefore

$$
Q_0(p^2)
=
\log p.
$$

Thus the alternating unit sector does perform nontrivial algebraic cancellation:

```text
prime
  survives

prime square
  survives with von Mangoldt weight

rough semiprime with distinct primes
  cancels exactly
```

This is not elimination of the prime channel.

It is a finite combinatorial prime-power detector.

---

# 6. $U$ -rough numbers

Call $n>1$ $U$ -rough if it has no divisor

$$
d
$$

satisfying

$$
2\le d\le U.
$$

Equivalently, every prime divisor of $n$ is larger than $U$.

For such an $n$, every convolution term containing $\nu$ vanishes.

Hence:

## Theorem 6.1 — $K=3$ Rough-Prime Persistence

For every $U$ -rough integer

$$
1<n<X,
$$

$$
\boxed{
Q_0(n)
=
\Lambda(n).
}
$$

### Proof

Because $\nu$ is supported on

$$
2\le d\le U,
$$

any nonzero term from $Q_1,Q_2,Q_3$ would force a divisor of $n$ in this range.

No such divisor exists.

Therefore

$$
Q_1(n)=Q_2(n)=Q_3(n)=0.
$$

Since

$$
\Lambda
=
Q_0+Q_1+Q_2+Q_3,
$$

the result follows. $\square$

---

# 7. Consequence at $K=3$

Because

$$
U^3\ge X,
$$

an $U$ -rough integer below $X$ cannot contain three prime factors counted with multiplicity.

Thus its possible von Mangoldt support is limited to:

```text
large prime
large prime square
```

and the unit sector already assigns exactly the correct von Mangoldt weight.

The hoped-for cancellation of the Vaughan unit-divisor channel has therefore not occurred.

It has been reorganized into an exact rough-prime-power channel.

---

# 8. General fixed- $K$ all-unit sector

Now let

$$
K\ge1
$$

be fixed.

Take

$$
U
\ge
X^{1/K}.
$$

The fixed- $K$ Heath-Brown identity is

$$
\boxed{
\Lambda
=
\sum_{j=1}^{K}
(-1)^{j-1}
\binom Kj
\mu_{\le U}^{*j}
*
\mathbf1^{*(j-1)}
*
L
}
$$

on $n<X$.

Write again

$$
\mu_{\le U}
=
\delta+\nu.
$$

The all-unit sector is

$$
\boxed{
Q_{K,0}
=
\sum_{j=1}^{K}
(-1)^{j-1}
\binom Kj
\mathbf1^{*(j-1)}
*
L.
}
$$

Using the divisor-function identity,

$$
\boxed{
Q_{K,0}(n)
=
\log n
\sum_{j=1}^{K}
(-1)^{j-1}
\binom Kj
\frac{d_j(n)}{j}.
}
$$

---

# 9. Fixed- $K$ Rough-Prime Persistence Theorem

## Theorem 9.1

For every fixed

$$
K\ge1,
$$

every admissible $U\ge X^{1/K}$, and every $U$ -rough integer

$$
1<n<X,
$$

$$
\boxed{
Q_{K,0}(n)
=
\Lambda(n).
}
$$

### Proof

Exactly as in Theorem 6.1, every sector containing at least one non-unit truncated Möbius factor vanishes on a $U$ -rough integer.

Only $Q_{K,0}$ remains.

The full Heath-Brown identity equals $\Lambda$.

 $\square$

---

# 10. Prime persistence for every fixed $K$

Let

$$
p
$$

be prime with

$$
U<p<X.
$$

Then $p$ is $U$ -rough, so Theorem 9.1 gives

$$
Q_{K,0}(p)
=
\log p.
$$

This can also be checked directly.

For a prime,

$$
d_j(p)=j.
$$

Therefore

$$
\begin{aligned}
Q_{K,0}(p)
&=
\log p
\sum_{j=1}^{K}
(-1)^{j-1}
\binom Kj
\\
&=
\log p.
\end{aligned}
$$

Hence:

$$
\boxed{
\text{no fixed Heath-Brown depth }K
\text{ can algebraically remove the all-unit prime channel.}
}
$$

---

# 11. Zero-frequency CSSA sector ledger

Define

$$
\mathcal T_r(N)
=
\sum_{2\le n<X}
w_N(n)
A(n-1)
Q_r(n)
$$

for

$$
r=0,1,2,3,
$$

and retain the centering block

$$
\mathcal T_{\rm C}(N)
=
-
\sum_{2\le n<X}
w_N(n)A(n-1).
$$

Then

$$
\boxed{
\mathcal A_N
=
\mathcal T_0
+
\mathcal T_1
+
\mathcal T_2
+
\mathcal T_3
+
\mathcal T_{\rm C}
-
\mathcal M_N.
}
$$

The exact alternating cancellation internal to $j=1,2,3$ has already been performed in the $Q_r$.

No later block is allowed to claim that same cancellation a second time.

---

# 12. Generic exponent ledger

For fixed $K=3$, every $Q_r(n)$ is bounded by a fixed divisor-function power times

$$
\log n.
$$

Hence

$$
Q_r(n)
=
N^{o(1)}
$$

for

$$
n<X.
$$

Using only

$$
w_N(n)\ll N,
$$

$$
A(n)\ll n,
$$

one obtains

$$
\boxed{
\mathcal T_r(N)
=
O(N^{3+o(1)})
}
$$

for every

$$
r=0,1,2,3.
$$

The centering block is also

$$
O(N^3).
$$

Thus the $K=3$ exponent ledger is:

| Sector | Meaning | Generic exponent | Status |
|---|---|---:|---|
| $Q_0$ | all-unit / rough-prime sector | $3+o(1)$ | CRITICAL |
| $Q_1$ | one non-unit Möbius factor | $3+o(1)$ | CRITICAL |
| $Q_2$ | two non-unit Möbius factors | $3+o(1)$ | CRITICAL |
| $Q_3$ | three non-unit Möbius factors | $3+o(1)$ | CRITICAL |
| $C$ | centering | $3$ | CRITICAL |
| full recombination | $\Lambda-1$ | $3+o(1)$ | ORIGINAL FRONTIER |

No fixed-power saving is created by the $K=3$ identity alone.

---

# 13. Why the $Q_0$ block is qualitatively different

The sectors $Q_1,Q_2,Q_3$ contain actual truncated Möbius variables.

The sector $Q_0$ does not.

On $U$ -rough numbers it is exactly $\Lambda$.

Therefore any blockwise method which treats

$$
\mathcal T_0
$$

separately must control a zero-frequency prime / prime-power channel with no Möbius averaging.

This is the Heath-Brown analogue of the Vaughan unit-divisor resonance.

But the structure is sharper:

> the troublesome unit contribution has been algebraically cleaned into an exact rough von Mangoldt sector.

---

# 14. Cross-sector recombination

The exact identity

$$
Q_0+Q_1+Q_2+Q_3
=
\Lambda
$$

shows that complete signed recombination of the Heath-Brown sectors returns the original prime coefficient.

Adding the centering block returns

$$
\Lambda-1.
$$

Thus:

```text
blockwise absolute values
  lose possible cross-sector cancellation

complete recombination
  returns the original CSSA frontier
```

A successful fixed- $K$ Heath-Brown proof would require a nontrivial partial recombination theorem between these two extremes.

No such theorem is established here.

---

# 15. Fixed- $K$ frontier neutrality

Theorem 9.1 gives a general obstruction.

## Theorem 15.1 — Fixed- $K$ Heath-Brown Rough-Channel Neutrality

For every fixed $K$, the canonical all-unit sector retains the full von Mangoldt coefficient on the $U$ -rough subset of the validity range.

Therefore fixed- $K$ alternating convolution depth alone does not create a lower-strength zero-frequency prime frontier.

Any fixed-power gain must come from:

1. a proved estimate on the all-unit rough sector;
2. a theorem-forced cancellation between the all-unit sector and non-unit sectors;
3. a recursive use of the identity across enough scales;
4. or another new arithmetic mechanism.

Increasing $K$ while keeping it fixed does not eliminate this requirement.

---

# 16. New obstruction: fixed- $K$ rough-prime persistence

Create:

```text
O-RH-017
FIXED_K_ROUGH_PRIME_PERSISTENCE
status:
  CERTIFIED
```

Statement:

> In every fixed- $K$ Heath-Brown identity with admissible truncation, the all-unit Möbius sector agrees exactly with $\Lambda$ on $U$ -rough integers. In particular every prime larger than $U$ survives with coefficient $\log p$.

This obstruction generalizes the pinned $K=3$ result.

---

# 17. New obstruction: Heath-Brown fixed-depth frontier neutrality

Create:

```text
O-RH-018
HEATH_BROWN_FIXED_DEPTH_FRONTIER_NEUTRALITY
status:
  CERTIFIED_AT_IDENTITY_LEVEL
```

Statement:

> For fixed $K$, alternating convolution algebra can cancel composite factorization patterns, but it cannot remove the all-unit rough von Mangoldt sector. Complete recombination returns $\Lambda$. The identity alone therefore supplies no fixed-power zero-frequency frontier contraction.

This is not an impossibility theorem for estimates built on the identity.

---

# 18. Campaign 08 verdict

The original Campaign 08 question was whether the $K=3$ alternating structure could eliminate the low-order unit channel before absolute values were taken.

The precise answer is:

```text
UNIT CONFIGURATION CANCELLATION
  YES, PARTIAL

ROUGH SEMIPRIME CANCELLATION
  YES, EXACT

ROUGH PRIME / PRIME-POWER ELIMINATION
  NO

ALL-UNIT SECTOR
  SURVIVES

K=3 FIXED-POWER BLOCK SAVING
  NONE

FIXED-K GENERALIZATION
  ROUGH-PRIME PERSISTENCE CERTIFIED
```

Therefore increasing to $K=4,5,\ldots$ with each $K$ fixed is not the next useful campaign.

---

# 19. New survivor: cross-sector rough-principal cancellation

Create:

```text
S-RH-018
ROUGH_PRINCIPAL_CROSS_SECTOR_CANCELLATION
status:
  OPEN
```

A valid theorem would need to prove that the critical all-unit sector cancels with a canonical signed combination of the non-unit sectors at fixed-power strength.

It must not simply recombine all sectors back into $\Lambda$.

---

# 20. Why growing $K$ is the next structural question

Paper 07 proved that a fixed constant contraction repeated only

$$
o(\log N)
$$

times cannot yield a fixed $N$ -power.

A fixed Heath-Brown depth has only finitely many alternating layers.

Therefore a new structural possibility is:

$$
\boxed{
K=K(N)\to\infty.
}
$$

But growing $K$ changes three quantities simultaneously:

1. truncation scale
   $$
   U=X^{1/K};
   $$

2. alternating binomial mass
   $$
   \sum_{j=1}^{K}\binom Kj
   =
   2^K-1;
   $$

3. multilinear / dyadic block complexity.

A useful growing-depth route must gain enough contraction to beat these costs.

---

# 21. First depth-complexity calculation

If blockwise absolute values are taken across the $j$ -layers, the binomial coefficient mass is

$$
2^K-1.
$$

If

$$
K=o(\log N),
$$

then

$$
2^K
=
N^{o(1)}.
$$

So the combinatorial coefficient cost is exponent-neutral.

But such a $K$ is still sublogarithmic.

A constant contraction per layer would then yield only

$$
N^{-o(1)}
$$

by Paper 07.

If instead

$$
K
=
c\log N,
$$

then

$$
\boxed{
2^K
=
N^{c\log2}.
}
$$

The identity has acquired a fixed positive power of combinatorial mass before any analytic estimate.

Therefore a log-depth strategy cannot use blockwise absolute values on the alternating layers.

It must preserve substantial alternating cancellation.

---

# 22. Intermediate growth

For

$$
K
=
c\log\log N,
$$

one has

$$
2^K
=
(\log N)^{c\log2}
=
N^{o(1)}.
$$

The truncation is

$$
U
=
\exp
\left(
\frac{\log X}{c\log\log N}
\right)
=
X^{1/(c\log\log N)}.
$$

This gives increasing convolution depth with only polylogarithmic binomial mass.

But

$$
K
=
o(\log N),
$$

so constant per-layer contraction alone remains subpower.

Thus the interesting growing- $K$ regime would require either:

```text
per-layer gap increasing with K,
nonlocal cancellation across many j-layers,
or a contraction mechanism not proportional merely to depth.
```

---

# 23. Campaign 09

The next campaign is:

```text
CSM_RH Campaign 09
GROWING_K_HEATH_BROWN_DEPTH_COMPLEXITY
```

It is not an RH proof campaign.

It is a feasibility audit for the last obvious way of extracting more structural depth from the Heath-Brown identity.

---

# 24. Campaign 09 required questions

Workers must answer:

```text
Q1
For K=K(N), what exact truncation U(N) is used?

Q2
What is the exact alternating coefficient mass?

Q3
How many canonical dyadic / smooth blocks are created?

Q4
Which cancellations are preserved before absolute values?

Q5
What is the effective contraction per j-layer?

Q6
What is the cumulative contraction mass?

Q7
What is the combinatorial exponent tax?

Q8
Does net contraction remain linear in log N after subtracting all taxes?

Q9
Does the all-unit rough-prime sector remain critical?

Q10
If the answer is no fixed power, what is the strongest subpower profile actually obtained?
```

---

# 25. Campaign 09 hard rejection filters

Reject a candidate if:

## R1. $2^K$ is ignored

Alternating coefficient mass must be included.

## R2. Dyadic block count is ignored

Representation complexity is part of the exponent ledger.

## R3. Constant contraction at $K=o(\log N)$ is called fixed power

Paper 07 forbids this.

## R4. $K\asymp\log N$ is used with blockwise triangle inequality

The resulting $2^K$ factor is already a fixed power.

## R5. The rough-prime sector is claimed to disappear

Theorem 9.1 still applies at each admissible $K$.

## R6. Growing- $K$ Möbius cancellation imports a fixed Mertens power

Paper 07's Möbius strength audit applies.

---

# 26. State transition

The canonical transition is:

```text
CSM_RH v0.9
  ->
CSM_RH v1.0
```

The version number refers to closure-state maturity.

It does not indicate a proof of RH.

Transitions:

```text
Campaign 08
  CLOSED_AS_K3_AND_FIXED_K_UNIT_SECTOR_AUDIT

O-RH-017
  FIXED_K_ROUGH_PRIME_PERSISTENCE
  CREATED / CERTIFIED

O-RH-018
  HEATH_BROWN_FIXED_DEPTH_FRONTIER_NEUTRALITY
  CREATED / CERTIFIED AT IDENTITY LEVEL

S-RH-018
  ROUGH_PRINCIPAL_CROSS_SECTOR_CANCELLATION
  CREATED / OPEN

F-RH-008
  GZMPS
  REMAINS OPEN

Campaign 09
  GROWING_K_HEATH_BROWN_DEPTH_COMPLEXITY
  READY
```

---

# 27. Final status

```text
RH = OPEN

CSSA FIXED POWER = OPEN

VAUGHAN FIXED IDENTITY = NEUTRAL

HEATH-BROWN K=3 = NEUTRAL AT IDENTITY LEVEL

ALL-UNIT ROUGH-PRIME CHANNEL = PERSISTS

EVERY FIXED K = SAME ROUGH-PRIME PERSISTENCE

FIXED-K DECOMPOSITION SEARCH = STRUCTURALLY EXHAUSTED

GROWING-K DEPTH / COMPLEXITY = OPEN

ROUGH-PRINCIPAL CROSS-SECTOR CANCELLATION = OPEN
```

The central theorem is:

$$
\boxed{
Q_{K,0}(n)
=
\Lambda(n)
\qquad
\text{for every }U\text{-rough }n<X.
}
$$

Thus fixed higher convolution depth cleans composite factorization patterns but cannot algebraically remove the prime channel.

The next question is whether growing depth can create enough cumulative arithmetic contraction to offset its own combinatorial complexity.
