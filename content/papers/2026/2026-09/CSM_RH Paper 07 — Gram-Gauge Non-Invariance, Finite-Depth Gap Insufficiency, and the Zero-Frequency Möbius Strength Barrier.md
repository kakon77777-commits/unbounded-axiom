# CSM_RH Paper 07
## Gram-Gauge Non-Invariance, Finite-Depth Gap Insufficiency, and the Zero-Frequency Möbius Strength Barrier

**Project:** `CSM_RH`  
**Paper:** `07`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v0.7 / Paper 06`  
**Campaign:** `06 — MULTIPLICATIVE_GRAM_GAP`  
**Status:** representation audit / exponent-strength audit; not a proof or disproof of RH

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

The purpose of this paper is to determine whether a multiplicative Gram-gap certificate is a canonical arithmetic object and what strength a useful certificate would actually require.

The principal conclusions are:

```text
RAW GRAM GAP
  not decomposition-invariant

CONSTANT ONE-SHOT GRAM ANGLE
  exponent-insufficient

FIXED-ORDER EXACT DECOMPOSITION
  finite/polylog interface, not a power-saving mechanism

DIRECT FIXED-POWER MÖBIUS CANCELLATION
  already fixed-zero-strip strength

SURVIVING ROUTES
  recombined zero-frequency multilinear power saving
  or recursive multiplicative contraction with linear cumulative mass
```

No live GLM-5.3-Flash run is claimed.

---

# 1. Starting frontier

Paper 06 introduced

```text
F-RH-007
MULTIPLICATIVE_GRAM_GAP_CERTIFICATE
MGGC
```

from an exact decomposition

$$
a_n
=
\sum_{r=1}^{R}
b_n^{(r)}.
$$

Let

$$
B_r(j)
=
\sum_{n\le j}
b_n^{(r)}
$$

and

$$
A(j)
=
\sum_{r=1}^{R}
B_r(j).
$$

On the dyadic endpoint interval define

$$
\langle U,V\rangle_N
=
\sum_{j=N}^{2N-1}
U(j)\overline{V(j)}.
$$

The component Gram matrix is

$$
G_{rs}
=
\langle B_r,B_s\rangle_N.
$$

Then

$$
J_N
=
\left\|
A
\right\|_N^2
=
\mathbf 1^\ast
G
\mathbf 1.
$$

This identity is correct.

The new question is whether properties of the individual entries of $G$ are canonical.

---

# 2. Component gauge transformations

Write the component vector as

$$
B
=
(B_1,\ldots,B_R)^T.
$$

Let

$$
T\in\mathbb C^{R\times R}
$$

satisfy

$$
\boxed{
\mathbf 1^\ast T
=
\mathbf 1^\ast.
}
$$

Define new components

$$
C
=
TB.
$$

Then

$$
\sum_{r=1}^{R}
C_r
=
\mathbf 1^\ast C
=
\mathbf 1^\ast TB
=
\mathbf 1^\ast B
=
A.
$$

Thus the target cumulative error is unchanged.

The Gram matrix transforms as

$$
\boxed{
G_C
=
T G_B T^\ast.
}
$$

But

$$
\boxed{
\mathbf 1^\ast
G_C
\mathbf 1
=
J_N
}
$$

remains unchanged.

This is the component-gauge freedom.

---

# 3. Gram-Gauge Non-Invariance Theorem

## Theorem 3.1

The following quantities are not invariants of the recombined target $A$ under exact component regrouping:

- $\operatorname{tr}G$ ;
- the sum of off-diagonal Gram entries;
- the sign pattern of individual cross-Gram entries;
- the ratio between diagonal mass and cross mass;
- a constant-angle statement between arbitrarily chosen components.

The quantity

$$
\boxed{
\mathbf 1^\ast G\mathbf 1
=
J_N
}
$$

is invariant.

### Proof

The target depends only on the sum of the components.

The transformation in Section 2 preserves this sum while changing the Gram matrix by congruence.

The explicit two-component example in Section 4 shows that diagonal and cross masses may be varied arbitrarily while $J_N$ is fixed. $\square$

---

# 4. Explicit two-component gauge example

Let $A$ be any nonzero vector in the endpoint Hilbert space.

For any real parameter $M$, define

$$
C_1
=
MA,
$$

$$
C_2
=
(1-M)A.
$$

Then

$$
C_1+C_2=A.
$$

The target energy is always

$$
J
=
\|A\|^2.
$$

But the diagonal Gram mass is

$$
\boxed{
D_M
=
[
M^2+(1-M)^2
]
J,
}
$$

and the total off-diagonal contribution is

$$
\boxed{
O_M
=
2M(1-M)J.
}
$$

Their sum is

$$
D_M+O_M=J.
$$

For

$$
M>1,
$$

the cross term is negative.

As

$$
M\to\infty,
$$

both

$$
D_M
$$

and

$$
|O_M|
$$

become arbitrarily large relative to $J$, while their cancellation leaves the same target.

Therefore a large negative cross-Gram term is not, by itself, mathematical progress.

---

# 5. Consequence for MGGC

The generic frontier

```text
MULTIPLICATIVE_GRAM_GAP_CERTIFICATE
```

is too representation-dependent unless the component semantics are fixed.

A valid certificate must specify at least:

```text
exact identity
exact cutoffs
exact smooth/dyadic partition
allowed regroupings
canonical component labels
canonical main-profile subtraction
recombination map
```

Even after this gauge fixing, a constant Gram improvement may still be exponent-insufficient.

That issue is addressed next.

---

# 6. Constant Gram gaps do not change exponents

Let

$$
E_N
$$

be any canonical component envelope satisfying

$$
E_N
\le
N^{3+o(1)}.
$$

Suppose a fixed decomposition proves only

$$
J_N
\le
c E_N
$$

for some constant

$$
0<c<1.
$$

Then

$$
J_N
\le
N^{3+o(1)}.
$$

There is no fixed power gain.

To obtain

$$
J_N
\le
N^{3-\kappa+o(1)},
$$

one needs either:

$$
\boxed{
E_N
\le
N^{3-\kappa+o(1)}
}
$$

or an angular / recombination factor

$$
\boxed{
\gamma_N
\le
N^{-\kappa+o(1)}.
}
$$

Thus:

## Theorem 6.1 — Power-Accurate Gram Requirement

A one-shot constant factor reduction in a quantity of trivial exponent $3$ does not alter the exponent.

A one-shot Gram certificate is fixed-power relevant only if the certificate itself contains a fixed power of $N$ or feeds a recurrence whose cumulative contraction mass is linear in $\log N$.

---

# 7. Finite-depth constant-gap theorem

Suppose a recursive factorization applies a fixed contraction

$$
0<\lambda<1
$$

at each of

$$
d(N)
$$

levels.

Ignoring lower-order errors, the total factor is

$$
\lambda^{d(N)}.
$$

Write

$$
c_\lambda
=
-\log\lambda>0.
$$

Then

$$
\lambda^{d(N)}
=
\exp
[
-c_\lambda d(N)
].
$$

## Theorem 7.1

If

$$
d(N)
=
o(\log N),
$$

then

$$
\boxed{
\lambda^{d(N)}
=
N^{-o(1)}.
}
$$

Hence finite depth, $O(\log\log N)$ depth, or any sublogarithmic recursion depth cannot produce a fixed $N^{-\kappa}$ power from a constant contraction factor alone.

To obtain

$$
\lambda^{d(N)}
\le
N^{-\kappa},
$$

one needs

$$
\boxed{
d(N)
\ge
\frac{\kappa}{-\log\lambda}
\log N
+
O(1).
}
$$

This is the depth form of the cumulative-gap theorem from Paper 06.

---

# 8. Calibration with fixed-order Heath-Brown identities

The standard Heath-Brown identity is parameterized by a fixed positive integer $K$ and writes $\Lambda$ on a dyadic interval as a finite alternating sum of Dirichlet convolutions involving truncated Möbius factors, copies of the constant function, and a logarithm factor.

For fixed $K$, the identity itself therefore has fixed combinatorial depth.

Ordinary dyadic or smooth subdivision creates only bookkeeping growth, not an intrinsic $\Omega(\log N)$ recursive contraction depth.

Consequently:

```text
HEATH-BROWN IDENTITY ITSELF
  !=
fixed-power contraction
```

A fixed-power result must come from estimates on the resulting multilinear pieces, from their recombination, or from a separate iterative mechanism.

The same semantic rule applies to a fixed Vaughan decomposition.

---

# 9. Polylogarithmic piece count is exponent-neutral

Suppose a fixed exact decomposition and its partitions yield

$$
R_N
=
N^{o(1)}
$$

pieces:

$$
\mathcal A_N
=
\sum_{r=1}^{R_N}
T_r(N).
$$

If every piece satisfies the uniform fixed-power bound

$$
|T_r(N)|
\le
N^{3-\kappa+o(1)},
$$

then

$$
\boxed{
|\mathcal A_N|
\le
N^{3-\kappa+o(1)}.
}
$$

Thus a polylogarithmic or subpolynomial number of pieces is harmless once every piece has a power saving.

Conversely, if one only has

$$
|T_r(N)|
\le
N^{3+o(1)},
$$

componentwise triangle inequality cannot generate a fixed saving.

The exponent must appear in the component estimate or in certified recombination.

---

# 10. Möbius partial sums

Define the Mertens function

$$
\boxed{
M(x)
=
\sum_{n\le x}
\mu(n).
}
$$

For

$$
\Re s>1,
$$

partial summation gives

$$
\boxed{
\frac1{\zeta(s)}
=
s
\int_1^\infty
M(x)x^{-s-1}\,dx.
}
$$

This identity supplies an immediate strength audit for zero-frequency multiplicative cancellation.

---

# 11. Fixed-power Möbius cancellation implies a fixed zero-free half-plane

## Theorem 11.1

Assume that for some

$$
\theta<1
$$

and every

$$
\varepsilon>0,
$$

$$
M(x)
=
O_\varepsilon
\left(
x^{\theta+\varepsilon}
\right).
$$

Then

$$
\boxed{
\zeta(s)\neq0
\qquad
\text{for }
\Re s>\theta.
}
$$

### Proof

Fix

$$
s
$$

with

$$
\Re s>\theta.
$$

Choose

$$
\varepsilon>0
$$

such that

$$
\theta+\varepsilon<\Re s.
$$

Then

$$
M(x)x^{-s-1}
=
O
\left(
x^{-1-(\Re s-\theta-\varepsilon)}
\right),
$$

so the integral

$$
s
\int_1^\infty
M(x)x^{-s-1}\,dx
$$

converges locally uniformly in the half-plane

$$
\Re s>\theta.
$$

It therefore defines a holomorphic continuation of

$$
1/\zeta(s)
$$

from

$$
\Re s>1
$$

to

$$
\Re s>\theta.
$$

A zero of $\zeta$ in this half-plane would be a pole of $1/\zeta$, contradicting holomorphy.

 $\square$

---

# 12. Fixed-strip calibration

If a proposed zero-frequency Type-I argument needs

$$
M(x)
\ll
x^{1-\delta}
$$

for some fixed

$$
\delta>0,
$$

then Theorem 11.1 already yields

$$
\boxed{
\zeta(s)\neq0
\qquad
\text{for }
\Re s>1-\delta.
}
$$

Thus the input is already fixed-zero-strip mathematics.

At the critical endpoint, the classical criterion

$$
M(x)
=
O_\varepsilon
\left(
x^{1/2+\varepsilon}
\right)
$$

for every $\varepsilon>0$ is equivalent to RH.

Therefore:

```text
DIRECT MERTENS FIXED-POWER SAVING
  can be a proof mechanism

but

DIRECT MERTENS FIXED-POWER SAVING
  is not a lower-strength shortcut
```

---

# 13. What Vaughan / Heath-Brown may still contribute

The Möbius audit does not invalidate Vaughan or Heath-Brown decompositions.

They may expose cancellation that is not reducible to a standalone bound on $M(x)$.

The surviving possibilities are:

## V1. Type-I/II component saving

A multilinear block may have a fixed-power saving because of cancellation among several multiplicative variables.

## V2. Recombined multilinear cancellation

Several canonical blocks may cancel after their main profiles are subtracted, without requiring a fixed-power Mertens estimate for any one factor.

## V3. Recursive arithmetic contraction

A canonical decomposition may be embedded in a genuine multiscale recurrence with linear cumulative contraction mass.

These remain open.

---

# 14. Main-profile saturation example

The simplest exact decomposition already shows why raw Gram geometry can be misleading.

Write

$$
a_n
=
\Lambda(n)-1.
$$

At cumulative level,

$$
A(j)
=
\psi(j)-j.
$$

Treat this as two components:

$$
B_1(j)
=
\psi(j),
$$

$$
B_2(j)
=
-j.
$$

Each component separately has a leading size of order $j$.

Their Gram diagonals are therefore of cubic dyadic scale.

Their cross term cancels the common deterministic main profile, leaving

$$
J_N
=
\sum_{j=N}^{2N-1}
(\psi(j)-j)^2.
$$

Thus enormous cross-Gram cancellation is already present before any RH-scale improvement.

The hard problem is the exponent of the residual after deterministic main-profile cancellation.

This motivates gauge fixing and canonical centering before any Gram certificate is interpreted.

---

# 15. Correction to F-RH-007

The raw frontier

```text
F-RH-007
MULTIPLICATIVE_GRAM_GAP_CERTIFICATE
```

is reclassified:

```text
status:
  RETIRED_AS_UNFIXED_GENERIC_FRONTIER

reason:
  raw Gram diagnostics are decomposition-gauge dependent
```

A named, fixed decomposition may still use Gram analysis internally.

But CSM_RH theorem promotion requires a representation-stable output.

---

# 16. New canonical frontier

Create:

```text
F-RH-008
GAUGE_FIXED_ZERO_FREQUENCY_MULTILINEAR_POWER_SAVING
abbrev:
  GZMPS
status:
  OPEN
```

A valid GZMPS certificate must include:

```text
1. one exact published or independently verified coefficient identity
2. exact cutoff parameters
3. exact partition convention
4. canonical block grouping
5. canonical main-profile subtraction
6. zero-frequency target preservation
7. a fixed-power block estimate or recombined fixed-power estimate
8. no triangle leakage that destroys the claimed sign cancellation
9. no hidden fixed-zero-strip input
10. exact derived kappa
```

The output must be invariant under merely cosmetic rewriting of the same fixed decomposition.

---

# 17. Two accepted GZMPS success modes

## Mode A — power-accurate pieces

Let

$$
\mathcal A_N
=
\sum_{r\le R_N}
T_r(N),
$$

with

$$
R_N=N^{o(1)}.
$$

If every canonical piece satisfies

$$
\boxed{
T_r(N)
=
O
\left(
N^{3-\kappa+o(1)}
\right)
}
$$

uniformly, then GZMPS closes.

## Mode B — recombined cancellation

If some individual pieces are larger, the proof may keep a canonical block sum signed and prove directly

$$
\boxed{
\left|
\sum_{r\in\mathcal B}
T_r(N)
\right|
\ll
N^{3-\kappa+o(1)}
}
$$

for every required block.

The cancellation must be theorem-forced.

It may not be inferred from a representation-dependent Gram picture alone.

---

# 18. Recursive success mode

A third route is allowed when the fixed decomposition is part of a genuine recurrence.

Suppose

$$
X(N_k)
\le
\lambda_k
X(N_{k-1})
+
O(N_k^{-\kappa_0}).
$$

Then Paper 06 applies.

The worker must prove

$$
\boxed{
\sum_{r=m+1}^{k}
-\log\lambda_r
\ge
\delta
\log
\left(
\frac{N_k}{N_m}
\right)
-
O(1)
}
$$

for some fixed

$$
\delta>0.
$$

A fixed-order identity used once does not satisfy this condition merely by existing.

---

# 19. Campaign 06 candidate audit

## C06-A — raw negative cross-Gram

```text
status:
  REJECTED AS NONCANONICAL

reason:
  Gram sign and magnitude depend on component gauge
```

## C06-B — fixed constant Gram angle

```text
status:
  REJECTED AS EXPONENT-INSUFFICIENT

reason:
  one constant factor does not change N^3 exponent
```

## C06-C — fixed-order Vaughan / Heath-Brown plus triangle inequality

```text
status:
  DECOMPOSITION-NEUTRAL

reason:
  exact finite convolution expansion is an interface;
  triangle recombination supplies no power
```

## C06-D — Type-I saving from fixed-power Mertens bound

```text
status:
  VALID BUT STRENGTH-NONREDUCING

reason:
  direct fixed-power Mertens cancellation already gives a fixed zero-free half-plane
```

## C06-E — recombined zero-frequency Type-I/II power saving

```text
status:
  SURVIVOR
```

## C06-F — recursive multiplicative contraction

```text
status:
  SURVIVOR

gate:
  linear cumulative log-contraction mass
```

---

# 20. New obstruction: Gram gauge non-invariance

Create:

```text
O-RH-012
GRAM_GAUGE_NONINVARIANCE
status:
  CERTIFIED
```

Statement:

> Cross-Gram signs, diagonal mass, and constant-angle gaps are not invariants of an exact recombined arithmetic target under component regrouping. They cannot be promoted as theorem progress without a fixed decomposition semantics and a representation-stable output.

---

# 21. New obstruction: finite-depth constant-gap insufficiency

Create:

```text
O-RH-013
FINITE_DEPTH_CONSTANT_GAP_INSUFFICIENCY
status:
  CERTIFIED
```

Statement:

> A constant contraction repeated only $o(\log N)$ times produces at most $N^{-o(1)}$ decay. A fixed-order decomposition therefore cannot obtain a fixed power from constant-factor improvement alone.

---

# 22. New obstruction: Möbius strength conservation

Create:

```text
O-RH-014
MOBIUS_FIXED_STRIP_STRENGTH
status:
  CERTIFIED
```

Statement:

> Any zero-frequency proof input of the form $M(x)=O(x^{\theta+\varepsilon})$ for every $\varepsilon>0$ already excludes zeta zeros in $\Re s>\theta$. Such an input may prove the desired result, but it is not a theorem-strength bypass.

---

# 23. New survivors

Create:

```text
S-RH-014
POWER_ACCURATE_TYPE_I_II_COMPONENT_ESTIMATE
status:
  OPEN
```

Create:

```text
S-RH-015
RECOMBINED_ZERO_FREQUENCY_MULTILINEAR_CANCELLATION
status:
  OPEN
```

Create:

```text
S-RH-016
RECURSIVE_MULTIPLICATIVE_LOG_DEPTH_CONTRACTION
status:
  OPEN
```

---

# 24. Campaign 07

The next campaign is:

```text
CSM_RH Campaign 07
CANONICAL_VAUGHAN_ZERO_FREQUENCY_LEDGER
```

This campaign fixes one exact Vaughan identity before estimation.

The objective is not to prove RH immediately.

The objective is to produce the first fully gauge-fixed Type-I/II ledger for CSSA.

---

# 25. Campaign 07 canonical workflow

## Step 1 — pin one exact Vaughan identity

Record:

```text
source
equation
range of validity
parameters U,V or equivalent cutoffs
all boundary terms
```

No mixing of incompatible Vaughan variants is allowed.

## Step 2 — apply it to the zero-frequency CSSA paraproduct

Start from

$$
\mathcal A_N
=
\sum_{n<2N}
w_N(n)
a_nA(n-1)
-
\mathcal M_N.
$$

Substitute the fixed identity consistently.

## Step 3 — define canonical blocks

Every Type-I, Type-II, diagonal, correction, and main-profile term receives one stable ID.

## Step 4 — subtract canonical main profiles

No arbitrary component re-centering is allowed.

## Step 5 — build the exponent ledger

For each block state:

```text
trivial exponent
best proved exponent
required exponent
saving source
whether Möbius fixed-power input is used
whether triangle leakage occurs
```

## Step 6 — promote only genuine power-bearing blocks

A block counts as progress only if its exponent improves by a fixed positive amount or if it participates in a rigorously proved recombined cancellation with such a gain.

---

# 26. Campaign 07 rejection filters

Reject a candidate if:

## R1. Gram-only evidence

A negative cross term is shown without a canonical block theorem.

## R2. Fixed constant gain only

A factor such as $0.9$ is called an exponent saving.

## R3. Möbius strength laundering

A fixed-power Mertens estimate is used but classified as routine.

## R4. Variant mixing

Different Vaughan identities or incompatible cutoffs are combined silently.

## R5. Arbitrary re-centering

Main profiles are moved between blocks without an exact conserved identity.

## R6. Triangle leakage

Signed canonical blocks are absolutized before the claimed cancellation.

## R7. Subpower mislabeled fixed-power

Logarithmic or stretched-exponential-in-log savings are promoted as $N^{-\kappa}$.

---

# 27. External calibration

The fixed-order Heath-Brown identity is a standard finite convolution identity for $\Lambda$ involving truncated Möbius functions and a fixed integer parameter $K$.

Modern applications use this identity to turn sums over primes into Type-I / Type-II or multilinear sums after smooth or dyadic subdivision.

This supports the semantic distinction:

```text
identity
  !=
estimate
```

The Mertens criterion provides the corresponding strength calibration for direct Möbius cancellation.

---

# 28. State transition

The canonical transition is:

```text
CSM_RH v0.7
  ->
CSM_RH v0.8
```

with:

```text
Campaign 06
  CLOSED_AS_GRAM_CANONICALITY_AUDIT

F-RH-007
  RAW MULTIPLICATIVE GRAM GAP
  RETIRED / REFINED

F-RH-008
  GZMPS
  CREATED / OPEN

O-RH-012
  GRAM_GAUGE_NONINVARIANCE
  CREATED / CERTIFIED

O-RH-013
  FINITE_DEPTH_CONSTANT_GAP_INSUFFICIENCY
  CREATED / CERTIFIED

O-RH-014
  MOBIUS_FIXED_STRIP_STRENGTH
  CREATED / CERTIFIED

S-RH-014
  POWER_ACCURATE_TYPE_I_II_COMPONENT_ESTIMATE
  CREATED / OPEN

S-RH-015
  RECOMBINED_ZERO_FREQUENCY_MULTILINEAR_CANCELLATION
  CREATED / OPEN

S-RH-016
  RECURSIVE_MULTIPLICATIVE_LOG_DEPTH_CONTRACTION
  CREATED / OPEN

Campaign 07
  CANONICAL_VAUGHAN_ZERO_FREQUENCY_LEDGER
  READY
```

---

# 29. Final status

```text
RH = OPEN

CSSA FIXED POWER = OPEN

RAW MULTIPLICATIVE GRAM GAP
= RETIRED AS NONCANONICAL

ONE-SHOT CONSTANT GRAM GAP
= EXPONENT-INSUFFICIENT

DIRECT FIXED-POWER MERTENS INPUT
= FIXED-ZERO-STRIP STRENGTH

GAUGE-FIXED RECOMBINED TYPE-I/II SAVING
= OPEN

RECURSIVE LOG-DEPTH MULTIPLICATIVE CONTRACTION
= OPEN

NEXT CAMPAIGN
= 07
```

The main correction is:

$$
\boxed{
\text{decomposition geometry is not theorem authority}.
}
$$

The next proof attempt must pin one exact decomposition and demonstrate where an actual fixed power enters the recombined zero-frequency arithmetic estimate.
