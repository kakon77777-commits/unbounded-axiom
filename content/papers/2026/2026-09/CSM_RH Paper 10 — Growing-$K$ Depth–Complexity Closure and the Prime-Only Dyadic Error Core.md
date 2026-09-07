# CSM_RH Paper 10
## Growing- $K$ Depth–Complexity Closure and the Prime-Only Dyadic Error Core

**Project:** `CSM_RH`  
**Paper:** `10`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.0 / Paper 09`  
**Campaign:** `09 — GROWING_K_HEATH_BROWN_DEPTH_COMPLEXITY`  
**Status:** depth–complexity audit / prime-power stripping theorem; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

Canonical state:

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

This paper closes the obvious growing-depth Heath-Brown identity search as an identity-level route and then removes the remaining decomposition shell.

The main conclusions are:

```text
GROWING K
  does not algebraically suppress the prime channel

ALL-UNIT PRIME SUPPORT
  expands as K grows

STANDARD BLOCKWISE GROWING-K IMPLEMENTATION
  has no fixed-power sweet spot under constant per-depth gain

PRIME POWERS
  are lower-order for the first fixed-strip target

NEW MINIMAL CORE
  prime-only dyadic theta-error energy
```

No live GLM-5.3-Flash run is claimed.

---

# 1. Growing- $K$ Heath-Brown identity

Let

$$
X=2N.
$$

For an integer

$$
K=K(X)\ge1,
$$

define

$$
U
=
X^{1/K}
$$

up to harmless integer rounding.

The Heath-Brown identity is

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

on the required range, provided the truncated Möbius convention is fixed so that

$$
U^K\ge X.
$$

The algebraic proof works for every positive integer $K$.

However, standard analytic applications normally fix $K$, because the number of convolution variables and the constants in the later decomposition depend on $K$.

---

# 2. All-unit sector for growing $K$

Write

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

Paper 09 proved:

$$
\boxed{
Q_{K,0}(n)
=
\Lambda(n)
}
$$

for every $U$ -rough integer $n$ in the validity range.

In particular, for every prime

$$
p>U,
$$

$$
\boxed{
Q_{K,0}(p)
=
\log p.
}
$$

This remains true when $K$ depends on $X$.

---

# 3. Growing depth expands the all-unit prime region

Since

$$
U=X^{1/K},
$$

 $U$ is decreasing as $K$ increases.

Therefore the set of primes satisfying

$$
p>U
$$

is increasing with $K$.

At those primes, every sector containing at least one non-unit truncated Möbius factor is exactly zero.

Thus:

## Theorem 3.1 — Growing- $K$ Prime-Support Monotonicity

Increasing $K$ cannot create coefficientwise cross-sector cancellation on the newly exposed prime range.

Instead it moves more prime coefficients into the sector where

$$
Q_{K,0}(p)=\log p
$$

and all non-unit sectors vanish.

This is an identity-level statement.

It does not exclude cancellation after summing over different integers.

---

# 4. All-unit prime-mass saturation

Let

$$
\vartheta(x)
=
\sum_{p\le x}
\log p.
$$

For every

$$
K\ge2,
$$

we have

$$
U
\le
X^{1/2}.
$$

The prime number theorem gives

$$
\vartheta(X)
\sim
X.
$$

Hence

$$
\begin{aligned}
\sum_{U<p<X}
\log p
&=
\vartheta(X)-\vartheta(U)
\\
&=
X+o(X).
\end{aligned}
$$

Therefore:

## Theorem 4.1 — All-Unit Prime-Mass Saturation

For every $K\ge2$, the all-unit sector contains asymptotically the full logarithmic mass of the primes below $X$:

$$
\boxed{
\sum_{\substack{
p<X\\
p>U
}}
Q_{K,0}(p)
=
X+o(X).
}
$$

Thus the persistent prime sector is not an $L^1$ -negligible residue.

---

# 5. Log-depth limit

If

$$
K
=
c\log X,
$$

then

$$
U
=
X^{1/(c\log X)}
=
e^{1/c}.
$$

Thus $U$ is asymptotically constant.

Apart from finitely many small primes, the complete prime support then lies in the all-unit sector.

Therefore growing depth does not drive the all-unit prime channel to zero.

At coefficient level it drives it toward saturation.

---

# 6. Exact alternating coefficient mass

The absolute binomial coefficient mass over the $j$ -layers is

$$
\boxed{
\sum_{j=1}^{K}
\binom Kj
=
2^K-1.
}
$$

If all alternating $j$ -layers are separated by triangle inequality, this mass must be included in a uniform layerwise ledger.

Its scale is:

## Sublogarithmic depth

If

$$
K=o(\log X),
$$

then

$$
2^K
=
X^{o(1)}.
$$

## Logarithmic depth

If

$$
K=c\log X,
$$

then

$$
\boxed{
2^K
=
X^{c\log2}.
}
$$

Thus blockwise absolute treatment of log-depth alternating layers incurs a fixed-power coefficient tax.

---

# 7. Standard dyadic block-complexity tax

The $j$ th Heath-Brown term contains

$$
2j
$$

multiplicative variables:

- $j$ truncated Möbius variables;
- $j-1$ constant-function variables;
- one logarithmic variable.

A standard dyadic implementation partitions each variable into

$$
O(\log X)
$$

ranges.

Thus the number of dyadic boxes in the $j$ th layer is bounded by

$$
(\log X)^{O(j)}.
$$

A convenient uniform model is

$$
B_j(X)
\le
C^{2j}
(\log X)^{2j}
$$

for some absolute bookkeeping constant $C>1$.

After including binomial coefficients,

$$
\sum_{j=1}^{K}
\binom Kj
B_j(X)
\le
\left[
1+C^2(\log X)^2
\right]^K-1.
$$

Therefore

$$
\boxed{
\log B_{\rm total}
=
O
\left(
K\log\log X
\right).
}
$$

The standard blockwise decomposition remains exponent-neutral only when

$$
\boxed{
K
=
o
\left(
\frac{
\log X
}{
\log\log X
}
\right).
}
$$

This is a bookkeeping statement for the standard dyadic implementation.

It is not a lower bound on every conceivable implementation.

---

# 8. No sweet spot in the standard constant-per-depth model

Assume, optimistically, that each additional identity depth gives a fixed constant analytic contraction

$$
e^{-g},
\qquad
g>0.
$$

After depth $K$, the benefit would be

$$
e^{-gK}.
$$

To make this a fixed power

$$
X^{-\kappa},
$$

one needs

$$
K
\asymp
\log X.
$$

But the standard blockwise regime is exponent-neutral only for

$$
K
=
o
\left(
\frac{
\log X
}{
\log\log X
}
\right).
$$

Inside the exponent-neutral complexity region,

$$
e^{-gK}
=
X^{-o(1)}.
$$

Thus:

## Theorem 8.1 — Standard Growing-Depth No-Sweet-Spot

Under both assumptions

```text
A
fixed constant gain per additional Heath-Brown depth

B
standard dyadic/blockwise recombination cost
```

there is no $K(X)$ regime giving a net fixed power while keeping the representation tax subpolynomial.

This theorem applies only to that implementation model.

A proof preserving large-scale alternating cancellation may escape assumption B.

---

# 9. Why avoiding the complexity tax is still not enough

Suppose a future method avoids all blockwise $2^K$ and dyadic taxes by preserving the complete alternating algebra.

The identity-level prime persistence remains:

$$
Q_{K,0}(p)=\log p
\qquad
(p>U).
$$

Therefore depth alone still does not contract prime coefficients.

Any gain must come from cancellation after summing the zero-frequency arithmetic target over different integers.

That is a new arithmetic theorem, not a consequence of increasing $K$.

---

# 10. Campaign 09 verdict

The growing- $K$ audit gives:

```text
IDENTITY VALIDITY
  PASS

PRIME-CHANNEL SUPPRESSION BY DEPTH
  NO

ROUGH-PRIME SECTOR
  EXPANDS WITH K

ALL-UNIT PRIME LOG MASS
  X + o(X)

STANDARD SUBPOLYNOMIAL COMPLEXITY REGION
  K = o(log X / log log X)

CONSTANT-PER-DEPTH GAIN IN THAT REGION
  SUBPOWER ONLY

LOG-DEPTH STANDARD BLOCKWISE COST
  FIXED-POWER OR WORSE

IDENTITY-LEVEL FRONTIER CONTRACTION
  ZERO
```

Therefore growing- $K$ Heath-Brown depth is closed as an identity-level search direction.

---

# 11. New obstruction: growing-depth prime saturation

Create:

```text
O-RH-019
GROWING_K_ALL_UNIT_PRIME_SATURATION
status:
  CERTIFIED
```

Statement:

> As Heath-Brown depth grows, the truncation threshold decreases, so more prime coefficients lie entirely in the all-unit sector. For every $K\ge2$, that sector already carries $X+o(X)$ logarithmic prime mass below $X$.

---

# 12. New obstruction: standard depth–complexity incompatibility

Create:

```text
O-RH-020
STANDARD_GROWING_K_DEPTH_COMPLEXITY_INCOMPATIBILITY
status:
  CERTIFIED_UNDER_BLOCKWISE_MODEL
```

Statement:

> In the standard dyadic/blockwise implementation, the exponent-neutral complexity range is $K=o(\log X/\log\log X)$. A fixed gain per depth is then subpower. Logarithmic depth is required for a power, but standard blockwise complexity is already power-sized or larger there.

This is an implementation-model obstruction, not a universal theorem.

---

# 13. Prime-power stripping

The closure analysis now permits a simpler target which does not use Heath-Brown decomposition at all.

Define

$$
\boxed{
\vartheta(x)
=
\sum_{p\le x}
\log p.
}
$$

Define the prime-only error

$$
\boxed{
B(j)
=
\vartheta(j)-j.
}
$$

Recall

$$
A(j)
=
\psi(j)-j.
$$

The difference is

$$
\Delta(j)
=
A(j)-B(j)
=
\psi(j)-\vartheta(j).
$$

Since

$$
\psi(x)-\vartheta(x)
=
\sum_{m\ge2}
\vartheta(x^{1/m}),
$$

Chebyshev bounds give

$$
\boxed{
\Delta(x)
=
O
\left(
x^{1/2}\log x
\right).
}
$$

---

# 14. Prime-only dyadic energies

Define

$$
J_N^\psi
=
\sum_{j=N}^{2N-1}
[
\psi(j)-j
]^2
$$

and

$$
\boxed{
J_N^\vartheta
=
\sum_{j=N}^{2N-1}
[
\vartheta(j)-j
]^2.
}
$$

Then

$$
A(j)
=
B(j)+\Delta(j).
$$

Therefore

$$
A(j)^2-B(j)^2
=
2B(j)\Delta(j)
+
\Delta(j)^2.
$$

Using Chebyshev bounds

$$
B(j)\ll j
$$

and Section 13,

$$
|A(j)^2-B(j)^2|
\ll
N^{3/2+o(1)}
$$

on the dyadic interval.

Summing $N$ terms gives:

## Theorem 14.1 — Prime-Power Stripping

$$
\boxed{
J_N^\psi
=
J_N^\vartheta
+
O
\left(
N^{5/2+o(1)}
\right).
}
$$

---

# 15. Fixed-strip exponent equivalence below the half-power barrier

Let

$$
0<\kappa<\frac12.
$$

Then

$$
5/2
<
3-\kappa.
$$

Therefore:

## Corollary 15.1

For every fixed

$$
0<\kappa<\frac12,
$$

$$
\boxed{
J_N^\psi
\ll
N^{3-\kappa+o(1)}
}
$$

if and only if

$$
\boxed{
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}.
}
$$

Thus the first fixed-zero-strip breakthrough does not require control of prime powers.

A sufficiently small positive $\kappa$ can be attacked entirely at the prime-only level.

---

# 16. Prime-only energy increment identity

Define

$$
c_n
=
\begin{cases}
\log n-1,
&
n\text{ prime},
\\
-1,
&
n\text{ composite}.
\end{cases}
$$

Then

$$
B(j)
=
\sum_{n\le j}c_n.
$$

Define

$$
D_N^\vartheta
=
\sum_{n<2N}
w_N(n)c_n^2.
$$

The same discrete energy increment used earlier gives:

## Theorem 16.1

$$
\boxed{
J_N^\vartheta
=
D_N^\vartheta
+
2
\sum_{n<2N}
w_N(n)c_nB(n-1).
}
$$

Moreover,

$$
D_N^\vartheta
=
O(N^2\log N).
$$

Therefore, for every

$$
0<\kappa<1,
$$

a fixed-power bound on the prime-only paraproduct is exponent-equivalent to the corresponding bound on $J_N^\vartheta$.

---

# 17. New canonical minimal frontier

Create:

```text
F-RH-009
PRIME_ONLY_DYADIC_ERROR_ENERGY
abbrev:
  PODEE
status:
  OPEN
```

The target is:

$$
\boxed{
J_N^\vartheta
=
\sum_{j=N}^{2N-1}
[
\vartheta(j)-j
]^2
\ll
N^{3-\kappa+o(1)}
}
$$

for any fixed

$$
0<\kappa<\frac12.
$$

By Paper 04 and Theorem 14.1, such a result is enough to produce a fixed zeta zero strip.

The strength is not reduced.

The representation overhead is.

---

# 18. Why PODEE is more canonical than another decomposition search

PODEE contains:

```text
no singular series
no prime powers
no Vaughan cutoff
no Heath-Brown depth
no Gram gauge
no character family
no major/minor arc split
no convolution-block naming
```

It is simply a dyadic mean square of the prime-only PNT error.

All previous decompositions may still be used as proof tools.

But they are no longer part of the theorem statement.

This sharply separates:

```text
canonical target
from
candidate proof mechanism.
```

---

# 19. New obstruction: decomposition-shell exhaustion

Create:

```text
O-RH-021
DECOMPOSITION_SHELL_EXHAUSTION
status:
  CERTIFIED_FOR_CURRENT_CAMPAIGNS
```

Statement:

> Vaughan, fixed- $K$ Heath-Brown, and growing- $K$ Heath-Brown identity manipulations have not produced a lower-strength fixed-power target. For the purpose of obtaining any first fixed zero strip, the problem can be stated without those decomposition shells as PODEE.

This does not say those identities are useless as future proof tools.

---

# 20. Campaign 10

The next campaign is:

```text
CSM_RH Campaign 10
PRIME_ONLY_DYADIC_ENERGY_ATTACK
```

Target:

```text
F-RH-009
PODEE
```

The campaign must begin from the prime-only target, not from a preselected decomposition.

---

# 21. Campaign 10 admissible mechanism families

## P1. Direct prime-support energy identity

Exploit exact algebra of

$$
c_n
=
\log n\,\mathbf1_{\mathbb P}(n)-1.
$$

## P2. Prime-only Selberg symmetry

Use an identity whose main object is $\vartheta(x)-x$ rather than reintroducing prime powers.

## P3. Sieve-weight approximation with signed remainder

Approximate the prime indicator by canonical sieve weights while preserving a signed target-fidelity ledger.

## P4. Bilinear / multilinear decomposition

Vaughan or Heath-Brown may be reused only after PODEE is fixed as the target.

## P5. Scale self-improvement

Search for a direct contraction of normalized prime-only energy across dyadic scales.

## P6. New prime-correlation theorem

State the exact correlation estimate required, rather than hiding it behind a stronger positive gate.

---

# 22. Campaign 10 rejection filters

Reject a candidate if:

## R1. It changes the target before proving target fidelity.

## R2. It reintroduces prime powers as if they were essential.

## R3. It counts a decomposition identity as an estimate.

## R4. It uses a fixed zero strip as an input.

## R5. It proves only $N^{3-o(1)}$ and labels it fixed-power.

## R6. It uses finite prime data as asymptotic authority.

## R7. It hides the first genuinely new prime-correlation lemma.

---

# 23. External calibration

The Heath-Brown identity is stated for every positive integer $K$ in standard references, while the analytic decomposition theorems built from it typically fix $K$ and allow later constants to depend on $K$.

This is consistent with the growing-depth complexity audit.

The prime-power stripping step uses only the standard estimate

$$
\psi(x)-\vartheta(x)
=
O
\left(
x^{1/2}\log x
\right)
$$

at the coarse strength required here.

No contemporary theorem is being promoted into a fixed-strip result.

---

# 24. State transition

The canonical transition is:

```text
CSM_RH v1.0
  ->
CSM_RH v1.1
```

with:

```text
Campaign 09
  CLOSED_AS_GROWING_DEPTH_COMPLEXITY_AUDIT

O-RH-019
  GROWING_K_ALL_UNIT_PRIME_SATURATION
  CREATED / CERTIFIED

O-RH-020
  STANDARD_GROWING_K_DEPTH_COMPLEXITY_INCOMPATIBILITY
  CREATED / CERTIFIED UNDER BLOCKWISE MODEL

O-RH-021
  DECOMPOSITION_SHELL_EXHAUSTION
  CREATED / CERTIFIED FOR CURRENT CAMPAIGNS

F-RH-009
  PRIME_ONLY_DYADIC_ERROR_ENERGY
  CREATED / OPEN

Campaign 10
  PRIME_ONLY_DYADIC_ENERGY_ATTACK
  READY
```

---

# 25. Final status

```text
RH = OPEN

CSSA FIXED POWER = OPEN

GROWING-K HEATH-BROWN IDENTITY-LEVEL ROUTE
= CLOSED

STANDARD GROWING-K BLOCKWISE SWEET SPOT
= NONE UNDER CONSTANT-PER-DEPTH MODEL

ALL-UNIT PRIME SECTOR
= SATURATES PRIME LOG MASS

PRIME POWERS
= LOWER ORDER FOR ANY kappa < 1/2

PODEE
= OPEN / NEW CANONICAL MINIMAL FRONTIER

NEXT CAMPAIGN
= PRIME-ONLY DYADIC ENERGY ATTACK
```

The new canonical target is:

$$
\boxed{
\sum_{j=N}^{2N-1}
[
\vartheta(j)-j
]^2
\ll
N^{3-\kappa+o(1)}
\qquad
\text{for some }
0<\kappa<\frac12.
}
$$

At this point the missing object is no longer a decomposition architecture.

It is a genuinely new prime-distribution theorem.
