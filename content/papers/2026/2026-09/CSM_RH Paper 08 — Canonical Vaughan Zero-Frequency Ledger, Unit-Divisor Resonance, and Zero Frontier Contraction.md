# CSM_RH Paper 08
## Canonical Vaughan Zero-Frequency Ledger, Unit-Divisor Resonance, and Zero Frontier Contraction

**Project:** `CSM_RH`  
**Paper:** `08`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v0.8 / Paper 07`  
**Campaign:** `07 — CANONICAL_VAUGHAN_ZERO_FREQUENCY_LEDGER`  
**Status:** exact decomposition ledger / obstruction audit; not a proof or disproof of RH

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

This paper pins one exact Vaughan identity, fixes one cutoff convention, substitutes it into the zero-frequency CSSA paraproduct, and builds a stable exponent ledger.

The result is:

```text
SHORT VAUGHAN BLOCK
  harmless

LONG TYPE-I BLOCK 1
  critical

LONG TYPE-I BLOCK 2
  critical

LONG TYPE-II BLOCK
  critical

LONG CENTERING BLOCK
  critical

SIGNED RECOMBINATION
  exactly returns the long CSSA target

STANDARD BLOCKWISE TRIANGLE
  no frontier contraction

TYPE-I d=1 ATOM
  unattenuated zero-frequency self-coupled channel
```

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical source identity

For arithmetic functions, let $*$ denote Dirichlet convolution.

Define

$$
L(n)=\log n.
$$

For cutoffs $U,V>1$, define

$$
\mu_{\le U}(n)
=
\mu(n)\mathbf 1_{n\le U},
$$

$$
\mu_{>U}(n)
=
\mu(n)\mathbf 1_{n>U},
$$

$$
\Lambda_{\le V}(n)
=
\Lambda(n)\mathbf 1_{n\le V},
$$

and

$$
\Lambda_{>V}(n)
=
\Lambda(n)\mathbf 1_{n>V}.
$$

The pinned Vaughan identity is

$$
\boxed{
\Lambda
=
\Lambda_{\le V}
+
\mu_{\le U}*L
-
\mu_{\le U}*\Lambda_{\le V}*1
+
\mu_{>U}*\Lambda_{>V}*1.
}
$$

Equivalently,

$$
\boxed{
\Lambda_{>V}
=
\mu_{\le U}*L
-
\mu_{\le U}*\Lambda_{\le V}*1
+
\mu_{>U}*\Lambda_{>V}*1.
}
$$

The identity is exact for every $U,V>1$.

Canonical expository source for this campaign:

```text
Terence Tao,
254A Notes 3: The large sieve and the Bombieri-Vinogradov theorem,
Lemma 18, equation (32).
```

No other Vaughan variant is mixed into this paper.

---

# 2. Fixed cutoff convention

Set

$$
X=2N.
$$

For sufficiently large integer $N$, fix

$$
\boxed{
U=V=\lfloor X^{1/3}\rfloor.
}
$$

The exact floor is part of the campaign convention.

At exponent level,

$$
U,V
=
N^{1/3+o(1)},
$$

and

$$
UV
=
N^{2/3+o(1)}.
$$

---

# 3. CSSA paraproduct

Recall

$$
a_n
=
\Lambda(n)-1,
$$

$$
A(j)
=
\sum_{m\le j}a_m
=
\psi(j)-j,
$$

and the endpoint weight

$$
w_N(n)
=
\begin{cases}
N,
&
1\le n\le N,
\\
2N-n,
&
N<n<2N,
\\
0,
&
n\ge2N.
\end{cases}
$$

Paper 05 gave

$$
\boxed{
\mathcal A_N
=
\sum_{2\le n<2N}
w_N(n)a_nA(n-1)
-
\mathcal M_N.
}
$$

The deterministic singular-series term satisfies

$$
\mathcal M_N
=
O(N^2\log N).
$$

---

# 4. Short / long split

Define

$$
\mathcal P_{\rm short}
=
\sum_{2\le n\le V}
w_N(n)
[
\Lambda(n)-1
]
A(n-1),
$$

and

$$
\mathcal P_{\rm long}
=
\sum_{V<n<2N}
w_N(n)
[
\Lambda(n)-1
]
A(n-1).
$$

Then

$$
\boxed{
\mathcal A_N
=
\mathcal P_{\rm short}
+
\mathcal P_{\rm long}
-
\mathcal M_N.
}
$$

---

# 5. Short block is harmless

Chebyshev bounds give

$$
\psi(x)\ll x,
$$

hence

$$
A(x)\ll x.
$$

Also

$$
w_N(n)\le N.
$$

Therefore

$$
\begin{aligned}
|\mathcal P_{\rm short}|
&\ll
N
\sum_{n\le V}
[
\Lambda(n)+1
]
n
\\
&\ll
NV^2.
\end{aligned}
$$

Since

$$
V=N^{1/3+o(1)},
$$

we obtain

$$
\boxed{
\mathcal P_{\rm short}
=
O
\left(
N^{5/3+o(1)}
\right).
}
$$

Thus the short block is below every CSSA target

$$
N^{3-\kappa+o(1)}
$$

with

$$
0<\kappa\le1.
$$

The deterministic term

$$
\mathcal M_N
=
N^{2+o(1)}
$$

is also harmless at this strength scale.

Therefore the entire fixed-power frontier lies in $\mathcal P_{\rm long}$.

---

# 6. Canonical long Vaughan blocks

On the range

$$
n>V,
$$

use the exact identity

$$
\Lambda_{>V}
=
\mu_{\le U}*L
-
\mu_{\le U}*\Lambda_{\le V}*1
+
\mu_{>U}*\Lambda_{>V}*1.
$$

Define:

## Block V-I1

$$
\boxed{
T_{\rm I1}
=
\sum_{V<n<X}
w_N(n)A(n-1)
[
\mu_{\le U}*L
](n).
}
$$

Expanding the convolution:

$$
\boxed{
T_{\rm I1}
=
\sum_{d\le U}
\mu(d)
\sum_{\substack{
m\ge1\\
V<dm<X
}}
(\log m)
w_N(dm)
A(dm-1).
}
$$

---

## Block V-I2

$$
\boxed{
T_{\rm I2}
=
-
\sum_{V<n<X}
w_N(n)A(n-1)
[
\mu_{\le U}*\Lambda_{\le V}*1
](n).
}
$$

Define

$$
\alpha_{U,V}(r)
=
\sum_{\substack{
d\ell=r\\
d\le U,\ \ell\le V
}}
\mu(d)\Lambda(\ell).
$$

Then

$$
\boxed{
T_{\rm I2}
=
-
\sum_{r\le UV}
\alpha_{U,V}(r)
\sum_{\substack{
m\ge1\\
V<rm<X
}}
w_N(rm)A(rm-1).
}
$$

This is the second canonical Type-I block.

---

## Block V-II

$$
\boxed{
T_{\rm II}
=
\sum_{V<n<X}
w_N(n)A(n-1)
[
\mu_{>U}*\Lambda_{>V}*1
](n).
}
$$

Define

$$
b_U(r)
=
\sum_{\substack{
d\mid r\\
d>U
}}
\mu(d).
$$

Then

$$
\boxed{
T_{\rm II}
=
\sum_{r>U}
b_U(r)
\sum_{\substack{
\ell>V\\
r\ell<X
}}
\Lambda(\ell)
w_N(r\ell)
A(r\ell-1).
}
$$

Because

$$
r>U,
\qquad
\ell>V,
\qquad
r\ell<X,
$$

both long multiplicative variables lie in the standard intermediate regime

$$
N^{1/3+o(1)}
<
r,\ell
<
N^{2/3+o(1)}.
$$

---

## Block V-C

The centering block is

$$
\boxed{
T_{\rm C}
=
-
\sum_{V<n<X}
w_N(n)A(n-1).
}
$$

---

# 7. Exact long recombination

By construction:

## Theorem 7.1 — Vaughan long-block identity

$$
\boxed{
\mathcal P_{\rm long}
=
T_{\rm I1}
+
T_{\rm I2}
+
T_{\rm II}
+
T_{\rm C}.
}
$$

### Proof

The coefficient of $w_N(n)A(n-1)$ in the right-hand side is

$$
[
\mu_{\le U}*L
](n)
-
[
\mu_{\le U}*\Lambda_{\le V}*1
](n)
+
[
\mu_{>U}*\Lambda_{>V}*1
](n)
-
1.
$$

For

$$
n>V,
$$

Vaughan's identity says the first three terms equal

$$
\Lambda(n).
$$

Hence the coefficient is

$$
\Lambda(n)-1.
$$

 $\square$

Thus the signed recombination is exactly the original long CSSA paraproduct.

---

# 8. Coefficient size audit

Standard divisor bounds give

$$
|\alpha_{U,V}(r)|
\le
\tau(r)\log V
=
N^{o(1)}
$$

uniformly on

$$
r\le UV.
$$

Likewise

$$
|b_U(r)|
\le
\tau(r)
=
N^{o(1)}.
$$

Using only

$$
A(x)\ll x,
$$

$$
w_N(x)\ll N,
$$

and divisor-sum estimates, one obtains:

$$
\boxed{
T_{\rm I1}
=
O(N^{3+o(1)})
}
$$

by absolute values,

$$
\boxed{
T_{\rm I2}
=
O(N^{3+o(1)})
}
$$

by absolute values,

$$
\boxed{
T_{\rm II}
=
O(N^{3+o(1)})
}
$$

by absolute values,

and

$$
\boxed{
T_{\rm C}
=
O(N^3).
}
$$

Thus every long block is critical at coefficient-blind strength.

Known zero-free-region PNT error estimates can improve these to strong subpower forms, but not to a fixed $N^{-\kappa}$ factor.

---

# 9. Canonical exponent ledger

The Campaign 07 ledger is:

| Block | Role | Trivial exponent | Fixed-power status |
|---|---|---:|---|
| `V-SHORT` | short $\Lambda-1$ block | $5/3+o(1)$ | CLOSED |
| `V-I1` | first Type-I | $3+o(1)$ | CRITICAL |
| `V-I2` | second Type-I | $3+o(1)$ | CRITICAL |
| `V-II` | Type-II | $3+o(1)$ | CRITICAL |
| `V-C` | long centering | $3$ | CRITICAL |
| `V-LONG` | signed recombination | $3+o(1)$ | EXACTLY ORIGINAL FRONTIER |

No long block receives a fixed exponent saving from the identity alone.

---

# 10. Type-I unit-divisor atom

The first Type-I block contains the exact $d=1$ contribution

$$
\boxed{
T_{\rm I1}^{(1)}
=
\sum_{V<m<X}
(\log m)
w_N(m)
A(m-1).
}
$$

There is:

```text
no Möbius averaging,
no divisor averaging,
no additive phase,
no minor-arc denominator,
no large-sieve separation
```

in this atom.

It is an unattenuated zero-frequency coupling between a prime-detecting weight and the cumulative PNT error.

The remaining part is

$$
T_{\rm I1}^{(\ge2)}
=
\sum_{2\le d\le U}
\mu(d)
\sum_{\substack{
m\\
V<dm<X
}}
(\log m)
w_N(dm)
A(dm-1).
$$

Thus any Type-I proof that first applies triangle inequality in $d$ must separately control $T_{\rm I1}^{(1)}$.

This is the canonical unit-divisor resonance.

---

# 11. Why ordinary Type-I oscillation is absent

In standard exponential-sum applications, Vaughan's Type-I blocks are useful because after fixing the small divisor $d$, the long variable carries an oscillatory test function such as

$$
e(\alpha dm).
$$

At the present CSSA frontier, the target is at zero external frequency.

The long factor is instead

$$
w_N(dm)A(dm-1).
$$

Therefore the ordinary additive oscillation source is absent.

This does not rule out arithmetic cancellation.

It rules out counting the standard nonzero-frequency Type-I mechanism as already available.

---

# 12. Triangle leakage theorem for the pinned ledger

Suppose the long Vaughan blocks are recombined only after estimating

$$
|T_{\rm I1}|,
\qquad
|T_{\rm I2}|,
\qquad
|T_{\rm II}|,
\qquad
|T_{\rm C}|
$$

separately.

Then the campaign has discarded all possible cancellation between the blocks.

Since each separate absolute-value estimate is critical at

$$
N^{3+o(1)},
$$

the resulting bound remains

$$
N^{3+o(1)}.
$$

Therefore:

## Theorem 12.1

For the pinned Vaughan ledger, coefficient-blind blockwise triangle estimation produces no fixed-power frontier contraction.

A successful Vaughan proof must preserve a signed recombination across at least part of the critical long block family or prove a fixed-power estimate for one or more critical blocks by genuinely new arithmetic input.

---

# 13. Algebraic recombination of the three $\Lambda$ blocks

The first three long blocks satisfy

$$
T_{\rm I1}
+
T_{\rm I2}
+
T_{\rm II}
=
\sum_{V<n<X}
w_N(n)\Lambda(n)A(n-1).
$$

Thus their largest mutual cancellation is already exactly encoded by the coefficient identity

$$
\Lambda_{>V}
=
\mu_{\le U}*L
-
\mu_{\le U}*\Lambda_{\le V}*1
+
\mu_{>U}*\Lambda_{>V}*1.
$$

After adding $T_{\rm C}$, the coefficient becomes $\Lambda-1$.

Hence full algebraic recombination returns the original target.

This is why the decomposition has zero closure gain until an estimate is inserted before complete recombination.

---

# 14. Canonicality of the present ledger

This campaign avoids the Gram-gauge problem from Paper 07 by fixing:

```text
one Vaughan identity
one U,V convention
one support split
one block naming convention
one centering block
one recombination map
```

No block is promoted because it has a visually favorable Gram sign.

Progress is measured only by a proved exponent.

---

# 15. Campaign 07 verdict

The fixed Vaughan identity achieves:

```text
EXACT DECOMPOSITION
  PASS

SHORT-BLOCK REMOVAL
  PASS

TYPE-I / TYPE-II LEDGER
  PASS

GAUGE FIXING
  PASS

FIXED-POWER BLOCK SAVING
  NONE

FIXED-POWER RECOMBINED SAVING
  NONE

FRONTIER CONTRACTION
  ZERO
```

Therefore Campaign 07 closes as an exact ledger and a no-free-saving audit.

It does not close CSSA.

---

# 16. New obstruction: Type-I Unit-Divisor Resonance

Create:

```text
O-RH-015
TYPE_I_UNIT_DIVISOR_RESONANCE
status:
  CERTIFIED_FOR_PINNED_VAUGHAN_LEDGER
```

Statement:

> At zero external frequency, the first Vaughan Type-I block contains an exact $d=1$ atom with no Möbius averaging or additive oscillation. Any blockwise Type-I method that separates divisor values by triangle inequality must control this unattenuated channel directly.

This obstruction is specific to the pinned Vaughan ledger.

It is not a universal impossibility theorem for all multiplicative decompositions.

---

# 17. New obstruction: Vaughan Zero-Frequency Frontier Neutrality

Create:

```text
O-RH-016
VAUGHAN_ZERO_FREQUENCY_FRONTIER_NEUTRALITY
status:
  CERTIFIED_AT_IDENTITY_PLUS_GENERIC_BOUND_LEVEL
```

Statement:

> After the harmless short block is removed, the exact signed recombination of the canonical Vaughan long blocks is the original long CSSA target. The identity alone creates no lower-strength intermediate fixed-power frontier.

A new theorem may still enter inside the decomposition.

The identity itself is neutral.

---

# 18. F-RH-008 remains open

The canonical frontier

```text
F-RH-008
GAUGE_FIXED_ZERO_FREQUENCY_MULTILINEAR_POWER_SAVING
GZMPS
```

remains open.

The pinned Vaughan specialization has not supplied a certificate.

Status:

```text
GZMPS / VAUGHAN INSTANCE
  OPEN
```

---

# 19. Surviving Vaughan route

Create:

```text
S-RH-017
RECOMBINED_VAUGHAN_ZERO_FREQUENCY_CANCELLATION
status:
  OPEN
```

A valid result must prove a fixed power for a canonical signed combination of the long blocks before full recombination returns the original target.

It may not:

```text
triangle every long block,
assume fixed-power Mertens cancellation,
use nonzero additive phase,
or relabel subpower as fixed-power.
```

---

# 20. Why test Heath-Brown next

Vaughan's first Type-I block exposes a singled-out unit-divisor atom.

The Heath-Brown identity has a different architecture: it is an alternating finite sum of higher Dirichlet convolutions.

For fixed $K$, it can be written in the form

$$
\Lambda
=
\sum_{j=1}^{K}
(-1)^{j-1}
\binom Kj
\mu_{\le U}^{*j}
*
1^{*(j-1)}
*
L
$$

on the range where the truncation condition is valid.

The alternating higher-convolution structure may reveal algebraic cancellation among low-order configurations before blockwise absolute values are taken.

This is a structural possibility, not an asserted saving.

---

# 21. Campaign 08

The next campaign is:

```text
CSM_RH Campaign 08
CANONICAL_HEATH_BROWN_K3_ZERO_FREQUENCY_LEDGER
```

Fix

$$
K=3.
$$

Choose $U$ so that the identity is valid on the full interval

$$
n<2N.
$$

A canonical choice is

$$
U
=
\lceil
(2N)^{1/3}
\rceil.
$$

The campaign must not change $K$ after seeing the estimates.

---

# 22. Campaign 08 questions

The worker must answer:

```text
Q1
What are the exact j=1,2,3 zero-frequency blocks?

Q2
Which unit-Möbius configurations cancel algebraically across the alternating j-sum?

Q3
After that exact cancellation, which multilinear configurations remain critical?

Q4
Does any remaining block have at least two genuinely long multiplicative variables before triangle inequality?

Q5
Can any known unconditional multilinear theorem yield a fixed N-power there without a fixed-strip input?

Q6
If not, what is the smallest surviving multilinear theorem?
```

---

# 23. Campaign 08 hard rejection filters

Reject a candidate if:

## R1. $K$ is changed after the fact

No parameter shopping over the identity depth.

## R2. Alternating terms are absolutized before low-order cancellation is checked

The entire purpose of the campaign is lost.

## R3. Unit configurations are silently dropped

They must be shown to cancel or be estimated.

## R4. Fixed-power Möbius cancellation is treated as routine

Paper 07's strength audit applies.

## R5. Polylog saving is promoted as fixed power

The target remains $N^{-\kappa}$.

## R6. A large number of blocks is itself called progress

Only exponent improvement counts.

---

# 24. State transition

The canonical transition is:

```text
CSM_RH v0.8
  ->
CSM_RH v0.9
```

with:

```text
Campaign 07
  CLOSED_AS_EXACT_VAUGHAN_LEDGER

O-RH-015
  TYPE_I_UNIT_DIVISOR_RESONANCE
  CREATED / CERTIFIED FOR PINNED VAUGHAN

O-RH-016
  VAUGHAN_ZERO_FREQUENCY_FRONTIER_NEUTRALITY
  CREATED / CERTIFIED AT IDENTITY + GENERIC BOUND LEVEL

S-RH-017
  RECOMBINED_VAUGHAN_ZERO_FREQUENCY_CANCELLATION
  CREATED / OPEN

F-RH-008
  GZMPS
  REMAINS OPEN

Campaign 08
  CANONICAL_HEATH_BROWN_K3_ZERO_FREQUENCY_LEDGER
  READY
```

---

# 25. Final status

```text
RH = OPEN

CSSA FIXED POWER = OPEN

PINNED VAUGHAN IDENTITY = CLOSED

VAUGHAN SHORT BLOCK = CLOSED

VAUGHAN LONG BLOCKS = CRITICAL

STANDARD BLOCKWISE TYPE-I/II ESTIMATION = NO FIXED-POWER GAIN

RECOMBINED VAUGHAN CANCELLATION = OPEN

GZMPS = OPEN

NEXT CAMPAIGN = HEATH-BROWN K=3
```

The main exact formula is:

$$
\boxed{
\mathcal P_{\rm long}
=
T_{\rm I1}
+
T_{\rm I2}
+
T_{\rm II}
+
T_{\rm C}.
}
$$

But the decomposition has not yet produced a new exponent.

The next test is whether a fixed higher-order alternating convolution can remove the unit-divisor resonance before estimation.
