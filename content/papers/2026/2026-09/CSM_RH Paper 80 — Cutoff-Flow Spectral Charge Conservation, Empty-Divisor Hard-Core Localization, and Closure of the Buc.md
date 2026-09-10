# CSM_RH Paper 80

## Cutoff-Flow Spectral Charge Conservation, Empty-Divisor Hard-Core Localization, and Closure of the Buchstab-Telescoping Route

**Project:** CSM_RH  
**Paper:** 80  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 47 — `ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Entry state:** v1.70 / Paper 79 v0.1  
**Status:** BUCHSTAB CUTOFF-FLOW AUDITED / EMPTY-DIVISOR HARD CORE CERTIFIED / F-RH-024 AND F-RH-025 REDUCED TO ROOT COVARIANCE PLUS POWER-SMALL ENTIRE CORRECTION  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 79 showed that the rightmost-zero resonance of the renormalized Vaughan coefficient is distributed across the logarithmic prime-factor scale

$$
e\asymp N^\theta.
$$

It then proposed decomposing the truncated Möbius coefficient

$$
b_U(k)
=
\sum_{\substack{d\mid k\\d\le U}}
\mu(d)
$$

by Buchstab / divisor-size increments and testing whether cross-scale arithmetic telescoping could generate an additional fixed-power cancellation.

The present paper shows that this route cannot create a new spectral amplifier.

Define

$$
M_U(s)
=
\sum_{d\le U}
\frac{\mu(d)}{d^s}
$$

and

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

For any

$$
U_1<U_2,
$$

one has the exact cutoff-flow identity

$$
\boxed{
B_{U_2}(s)-B_{U_1}(s)
=
\zeta(s)
\sum_{U_1<d\le U_2}
\frac{\mu(d)}{d^s}.
}
$$

Therefore, at every nontrivial zeta zero $\rho$,

$$
\boxed{
B_{U_2}(\rho)-B_{U_1}(\rho)=0.
}
$$

Since

$$
B_U(\rho)=-1
$$

for one, hence every, finite $U>1$,

$$
\boxed{
B_U(\rho)\equiv-1
}
$$

along the entire truncated Möbius cutoff flow.

This is a spectral charge-conservation law.

It has a sharper depth decomposition.

Write

$$
M_U(s)
=
1+R_U(s),
$$

where

$$
R_U(s)
=
\sum_{2\le d\le U}
\frac{\mu(d)}{d^s}.
$$

Then

$$
\boxed{
B_U(s)
=
\left(
\zeta(s)-1
\right)
+
\zeta(s)R_U(s).
}
$$

At a zeta zero $\rho$,

$$
\zeta(\rho)-1=-1,
$$

while

$$
\zeta(\rho)R_U(\rho)=0.
$$

Thus the universal value

$$
B_U(\rho)=-1
$$

is carried entirely by the **empty-divisor branch**

$$
d=1.
$$

Every nonempty Möbius-divisor correction vanishes at the zero.

Now let

$$
A_V(s)
=
-\frac{\zeta'(s)}{\zeta(s)}
-
L_V(s),
$$

where

$$
L_V(s)
=
\sum_{e\le V}
\frac{\Lambda(e)}{e^s}.
$$

The Vaughan balanced coefficient has Dirichlet series

$$
C_{U,V}(s)
=
A_V(s)B_U(s).
$$

The empty-divisor decomposition gives

$$
\boxed{
C_{U,V}(s)
=
A_V(s)
\left(
\zeta(s)-1
\right)
+
\left(
-\zeta'(s)-L_V(s)\zeta(s)
\right)
R_U(s).
}
$$

The second term is analytic at every nontrivial zeta zero.

Hence:

$$
\boxed{
\text{all nontrivial zero poles of the Vaughan balanced coefficient
are already present in the }d=1\text{ branch.}
}
$$

Changing $U$, splitting $U$ into Buchstab shells, or recursively decomposing nonempty divisors can only modify the zero-pole-free regular sector.

This is the divisor-depth analogue of Paper 79's factor-scale resonance theorem:

```text
prime-factor scale:
rightmost resonance is distributed across log e;

Möbius-divisor depth:
rightmost spectral charge is localized at the empty divisor d=1.
```

The paper then strengthens the conclusion using Paper 78's exact spectral split.

Recall

$$
H_{U,V}(s)
=
\frac{\zeta'(s)}{\zeta(s)}
+
E_{U,V}(s),
$$

where $E_{U,V}$ is analytic at every zeta zero and has residue $+1$ at $s=1$.

Define

$$
\boxed{
R_{U,V}(s)
=
E_{U,V}(s)-\zeta(s).
}
$$

Because the $+1$ residue at $s=1$ is cancelled by $\zeta(s)$ and $E_{U,V}$ has no zero poles,

$$
\boxed{
R_{U,V}(s)
\text{ has an entire analytic continuation.}
}
$$

Coefficientwise,

$$
\boxed{
h_{U,V}(n)
=
-\left(
\Lambda(n)-1
\right)
+
r_{U,V}(n),
}
$$

where the Dirichlet series of $r_{U,V}$ has entire continuation.

The explicit entire correction is

$$
\boxed{
\begin{aligned}
R_{U,V}(s)
&=
\zeta'(s)
\left(
M_U-M_U(s)
\right)
\\
&\quad
+
L_V(s)
\left(
1-\zeta(s)M_U(s)
\right)
\\
&\quad
+
\left(
M_UL_V+J_U
\right)
\zeta(s).
\end{aligned}
}
$$

Paper 77's exact extraction identity becomes

$$
\boxed{
\sum_n
f_{N,H}(n)
r_{U,V}(n)
=
\mathcal E_I,
}
$$

with

$$
\boxed{
\mathcal E_I
\ll
NUV(\log N)^{O(1)}.
}
$$

Therefore

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
=
-\mathcal R_W
+
\mathcal E_I.
}
$$

This is not merely a formal bookkeeping identity.

It is a hard-core decomposition:

- the entire correction is already Type-I power-controlled;
- the only non-entire zero-pole sector is exactly the negative original prime-error coefficient.

Consequently F-RH-024 is not an independent new root inequality.

Once the Type-I parameter gate makes $\mathcal E_I$ supercritical, a fixed-power estimate for

$$
\mathcal V^{\rm ren}_{U,V}
$$

is equivalent at exponent resolution to the same fixed-power estimate for the original root covariance

$$
\mathcal R_W.
$$

Likewise, F-RH-025 cannot obtain a new gain by Buchstab telescoping of $b_U$.

The nonempty divisor shells live in the entire / zero-pole-free correction sector and their accumulated correlation is exactly part of the already-controlled Type-I error.

The remaining hard term is the empty-divisor prime-error branch.

There is also an exact squarefree complementary-divisor identity.

If $k>1$ is squarefree, then

$$
\sum_{d\mid k}\mu(d)=0.
$$

Thus

$$
\boxed{
b_U(k)
=
-
\mu(k)
\sum_{\substack{q\mid k\\q<k/U}}
\mu(q).
}
$$

Moving the cutoff from small divisors to complementary divisors therefore does not eliminate parity.

It transports it and multiplies by the global sign $\mu(k)$.

This is the combinatorial analogue of cutoff-flow spectral conservation.

The campaign consequence is a structural closure of the first Campaign-47 route:

```text
F-RH-023:
auxiliary parity statement only;

F-RH-024:
root covariance plus known entire correction;

F-RH-025:
Buchstab / factor-scale reformulation of the same root hard core.
```

Campaign 47 produced valuable exact structure:

- deterministic divisor laws after shift averaging;
- a power-preserving Vaughan extraction;
- the exact counterterm;
- the parameter-invariant zero-pole hard core.

But it did not generate a strict exponent amplifier.

Any next campaign should therefore adopt a stronger entry test:

> Before developing a new linear arithmetic transform, compute its zeta-zero pole projector.
>
> Reject the candidate as a new amplifier if its hard coefficient is
> $$
> c(\Lambda-1)+\text{zero-pole-free correction},
> $$
> with $c\ne0$.

A genuinely new route must be nonlinear, multi-copy, or otherwise use ordinary-prime information which is not spectrally equivalent to a single prime-error coefficient plus an entire correction.

No RH theorem is claimed.

---

# 1. Truncated Möbius cutoff flow

Define

$$
\boxed{
b_U(k)
=
\sum_{\substack{d\mid k\\d\le U}}
\mu(d).
}
$$

For $1<k\le U$,

$$
b_U(k)
=
\sum_{d\mid k}\mu(d)
=
0.
$$

Also

$$
b_U(1)=1.
$$

Therefore

$$
\begin{aligned}
\sum_{k>U}
\frac{b_U(k)}{k^s}
&=
\sum_{k\ge1}
\frac{b_U(k)}{k^s}
-
1
\\
&=
\boxed{
\zeta(s)M_U(s)-1.
}
\end{aligned}
$$

This is valid initially for $\Re s>1$ and then by meromorphic continuation.

---

# 2. Cutoff increment identity

Let

$$
U_1<U_2.
$$

Then

$$
M_{U_2}(s)-M_{U_1}(s)
=
\sum_{U_1<d\le U_2}
\frac{\mu(d)}{d^s}.
$$

Hence:

## Theorem 2.1 — Möbius cutoff-flow identity

$$
\boxed{
B_{U_2}(s)-B_{U_1}(s)
=
\zeta(s)
\sum_{U_1<d\le U_2}
\frac{\mu(d)}{d^s}.
}
$$

Create:

```text
B-RH-131
TRUNCATED_MOBIUS_CUTOFF_INCREMENTS_CARRY_AN_EXPLICIT_ZETA_FACTOR
CERTIFIED
```

---

# 3. Spectral charge conservation

Let $\rho$ be any nontrivial zero of $\zeta$.

Theorem 2.1 gives

$$
\boxed{
B_{U_2}(\rho)-B_{U_1}(\rho)=0.
}
$$

Since

$$
B_U(\rho)
=
\zeta(\rho)M_U(\rho)-1
=
-1,
$$

for every finite $U$,

## Theorem 3.1 — Cutoff-flow zero-charge conservation

$$
\boxed{
B_U(\rho)\equiv-1.
}
$$

Create:

```text
B-RH-132
THE_VAUGHAN_COFACTOR_ZERO_VALUE_IS_A_CONSERVED_QUANTITY_ALONG_THE_MOBIUS_CUTOFF_FLOW
CERTIFIED
```

The value does not drift, diffuse, or telescope with $U$.

---

# 4. Empty-divisor localization

Write

$$
M_U(s)
=
1+R_U(s),
$$

$$
R_U(s)
=
\sum_{2\le d\le U}
\mu(d)d^{-s}.
$$

Then

$$
\boxed{
B_U(s)
=
\zeta(s)-1
+
\zeta(s)R_U(s).
}
$$

At a zeta zero,

$$
\boxed{
\left(
\zeta(\rho)-1
\right)
=-1,
}
$$

$$
\boxed{
\zeta(\rho)R_U(\rho)=0.
}
$$

Thus:

## Theorem 4.1 — Empty-divisor hard-core localization

The entire zero value $B_U(\rho)=-1$ is carried by the divisor $d=1$ branch.

Every nonempty Möbius-divisor branch has zero spectral charge at $\rho$.

Create:

```text
B-RH-133
THE_UNIVERSAL_VAUGHAN_ZERO_CHARGE_IS_LOCALIZED_AT_THE_EMPTY_DIVISOR_BRANCH
CERTIFIED
```

---

# 5. Balanced coefficient depth decomposition

Define

$$
A_V(s)
=
-\frac{\zeta'(s)}{\zeta(s)}
-
L_V(s).
$$

Then

$$
C_{U,V}(s)
=
A_V(s)B_U(s).
$$

Use Theorem 4.1:

$$
\boxed{
\begin{aligned}
C_{U,V}(s)
&=
A_V(s)
\left(
\zeta(s)-1
\right)
\\
&\quad
+
A_V(s)\zeta(s)R_U(s).
\end{aligned}
}
$$

But

$$
A_V(s)\zeta(s)
=
-\zeta'(s)
-
L_V(s)\zeta(s),
$$

which is analytic at every nontrivial zero.

Hence:

## Theorem 5.1 — All zero poles occur at divisor depth zero

$$
\boxed{
C_{U,V}(s)
=
A_V(s)(\zeta(s)-1)
+
\text{zero-pole-free divisor-depth correction}.
}
$$

Create:

```text
B-RH-134
ALL_NONTRIVIAL_ZERO_POLES_OF_THE_VAUGHAN_BALANCED_COEFFICIENT_ALREADY_OCCUR_IN_THE_D_EQUALS_ONE_BRANCH
CERTIFIED
```

---

# 6. Buchstab-shell increments cannot alter the zero residue

A shell increment

$$
\Delta_{U_1,U_2}M(s)
=
\sum_{U_1<d\le U_2}
\frac{\mu(d)}{d^s}
$$

changes the balanced coefficient by

$$
\boxed{
\Delta C(s)
=
\left(
-\zeta'(s)-L_V(s)\zeta(s)
\right)
\Delta_{U_1,U_2}M(s).
}
$$

This is analytic at every zeta zero.

Therefore every divisor-size shell, and every finite recursive grouping of such shells, has zero nontrivial-zero pole residue.

Create:

```text
O-RH-178
BUCHSTAB_OR_DIVISOR_SIZE_SHELLS_CANNOT_CHANGE_THE_UNIVERSAL_RIGHTMOST_ZERO_RESIDUE
CERTIFIED
```

This is the precise obstruction to F-RH-025's proposed cross-scale telescoping mechanism.

---

# 7. Squarefree complementary-divisor duality

Assume $k>1$ is squarefree.

Then

$$
\sum_{d\mid k}\mu(d)=0.
$$

Therefore

$$
b_U(k)
=
-
\sum_{\substack{d\mid k\\d>U}}
\mu(d).
$$

Set

$$
q=k/d.
$$

Because $k$ is squarefree,

$$
\mu(d)
=
\mu(k)\mu(q).
$$

The condition $d>U$ is

$$
q<k/U.
$$

Hence:

## Theorem 7.1 — Squarefree complementary parity transport

$$
\boxed{
b_U(k)
=
-
\mu(k)
\sum_{\substack{q\mid k\\q<k/U}}
\mu(q).
}
$$

Create:

```text
B-RH-135
TRUNCATED_MOBIUS_PARITY_DEFECT_IS_TRANSPORTED_TO_THE_COMPLEMENTARY_DIVISOR_SCALE_ON_SQUAREFREE_INTEGERS
CERTIFIED
```

Moving the cutoff does not destroy parity; it relocates it.

---

# 8. Entire correction theorem

Paper 78 gave

$$
H_{U,V}(s)
=
\frac{\zeta'(s)}{\zeta(s)}
+
E_{U,V}(s),
$$

with

$$
\boxed{
\begin{aligned}
E_{U,V}(s)
&=
\zeta'(s)
\left(
M_U-M_U(s)
\right)
\\
&\quad
+
L_V(s)
\left(
1-\zeta(s)M_U(s)
\right)
\\
&\quad
+
\left(
M_UL_V+J_U+1
\right)
\zeta(s).
\end{aligned}
}
$$

Define

$$
\boxed{
R_{U,V}(s)
=
E_{U,V}(s)-\zeta(s).
}
$$

Then

$$
\boxed{
\begin{aligned}
R_{U,V}(s)
&=
\zeta'(s)
\left(
M_U-M_U(s)
\right)
\\
&\quad
+
L_V(s)
\left(
1-\zeta(s)M_U(s)
\right)
\\
&\quad
+
\left(
M_UL_V+J_U
\right)
\zeta(s).
\end{aligned}
}
$$

At every zeta zero, all terms are regular.

At $s=1$, the simple-pole residues cancel:

- the first term contributes $-J_U$ ;
- the second contributes $-M_UL_V$ ;
- the third contributes $M_UL_V+J_U$.

Thus:

## Theorem 8.1 — Entire Type-I correction

$$
\boxed{
R_{U,V}(s)
}
$$

admits an entire analytic continuation.

Create:

```text
B-RH-136
THE_RENORMALIZED_VAUGHAN_REGULAR_SECTOR_MINUS_ITS_MEAN_HAS_ENTIRE_CONTINUATION
CERTIFIED
```

---

# 9. Coefficient hard-core decomposition

Let

$$
R_{U,V}(s)
=
\sum_{n\ge1}
\frac{r_{U,V}(n)}{n^s}
$$

initially in its half-plane of Dirichlet convergence.

Since

$$
H_{U,V}
=
\frac{\zeta'}{\zeta}
+
\zeta
+
R_{U,V},
$$

and

$$
\frac{\zeta'}{\zeta}
=
-\sum_n
\frac{\Lambda(n)}{n^s},
$$

one has:

## Theorem 9.1 — Prime-error hard-core decomposition

$$
\boxed{
h_{U,V}(n)
=
-\left(
\Lambda(n)-1
\right)
+
r_{U,V}(n).
}
$$

The correction $r_{U,V}$ has entire Dirichlet-series continuation.

Create:

```text
B-RH-137
RENORMALIZED_VAUGHAN_COEFFICIENT_EQUALS_NEGATIVE_PRIME_ERROR_PLUS_AN_ENTIRE_CORRECTION
CERTIFIED
```

---

# 10. Correlation of the entire correction is already power-controlled

Paper 77 gave

$$
\mathcal V^{\rm ren}_{U,V}
=
-\mathcal R_W
+
\mathcal E_I.
$$

On the other hand, Theorem 9.1 gives

$$
\begin{aligned}
\mathcal V^{\rm ren}_{U,V}
&=
\sum_n
f(n)h_{U,V}(n)
\\
&=
-\mathcal R_W
+
\sum_n
f(n)r_{U,V}(n).
\end{aligned}
$$

Therefore:

## Theorem 10.1 — Entire correction correlation identity

$$
\boxed{
\sum_n
f_{N,H}(n)r_{U,V}(n)
=
\mathcal E_I.
}
$$

Since

$$
\boxed{
\mathcal E_I
\ll
NUV(\log N)^{O(1)},
}
$$

the zero-pole-free correction is already controlled at the deterministic Type-I exponent.

Create:

```text
B-RH-138
THE_ENTIRE_VAUGHAN_CORRECTION_PAIRS_WITH_THE_SIGNED_ROOT_SEQUENCE_ONLY_THROUGH_THE_ALREADY_CONTROLLED_TYPE_I_ERROR
CERTIFIED
```

---

# 11. F-RH-024 equivalence at exponent resolution

Assume

$$
H=N^{1-\tau},
$$

$$
U=N^u,
$$

$$
V=N^v,
$$

and choose parameters such that

$$
\boxed{
1-\tau-u-v
>
\kappa+\eta.
}
$$

Then

$$
\mathcal E_I
\ll
NHN^{-\kappa-\eta+o(1)}.
$$

Hence

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
=
-\mathcal R_W
+
o_{\rm power}
\left(
NHN^{-\kappa}
\right).
}
$$

Therefore:

## Corollary 11.1 — F-RH-024 root equivalence

At every parameter choice for which the Type-I correction is supercritical,

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
\ll
NHN^{-\kappa-\eta}
}
$$

is equivalent at fixed-power resolution to

$$
\boxed{
\mathcal R_W
\ll
NHN^{-\kappa-\eta}.
}
$$

F-RH-024 is therefore not an independent amplifier input.

Update:

```text
F-RH-024
CLOSED_AS_ROOT_EQUIVALENT_REPRESENTATION
```

---

# 12. Consequence for F-RH-025

F-RH-025 proposed gaining cancellation from factor-scale / Buchstab decomposition of the Vaughan cofactor.

Theorems 3.1, 5.1 and 6 show:

- the zero charge is invariant under cutoff motion;
- the hard pole is already in the empty-divisor branch;
- every nonempty divisor shell is zero-pole-free.

Theorem 10.1 further shows that the full zero-pole-free correction contributes only the already-controlled Type-I error.

Therefore:

## Corollary 12.1 — Buchstab telescoping route closure

Cross-scale telescoping of the nonempty Möbius-divisor anatomy cannot generate a new fixed-power root gain within this exact Vaughan architecture.

Update:

```text
F-RH-025
CLOSED_AS_NONAMPLIFYING_BUCHSTAB_REORGANIZATION
```

The distributed prime-factor resonance of Paper 79 remains correct, but it is carried by the depth-zero prime-error hard core.

---

# 13. Relation to classical parity theory

Friedlander and Iwaniec's asymptotic sieve breaks the classical parity obstruction by adding a Möbius-sensitive bilinear hypothesis.

Ford and Maynard's later general theory proves that substantial Type-II information is genuinely necessary for arbitrary nonnegative prime-producing sequences.

These results remain important calibrations.

The present conclusion is narrower:

for the **specific Campaign-47 signed root sequence and its exact Vaughan renormalization**, the nonempty truncated-Möbius anatomy contributes only to a zero-pole-free correction whose root pairing has already been estimated by Type-I divisor discrepancy.

Thus classical parity sensitivity does not automatically become a new PESC amplifier in this specialized construction.

External calibration:

- Friedlander–Iwaniec, *Asymptotic sieve for primes*;
- Ford–Maynard, *On the theory of prime producing sieves*.

---

# 14. Campaign-47 structural verdict

Campaign 47 began with a stronger entry rule than Campaign 46:

```text
explicit q=1 fixed-power inequality first;
framework second.
```

It produced:

1. deterministic shift-averaged divisor distribution;
2. the signed root sequence;
3. a power-preserving exact Vaughan extraction;
4. the coefficientwise renormalization;
5. universal zero-pole preservation;
6. distributed prime-factor resonance;
7. cutoff-flow zero-charge conservation;
8. empty-divisor hard-core localization;
9. an entire correction whose root correlation is already Type-I small.

The final exact decomposition is

$$
\boxed{
\text{renormalized Vaughan defect}
=
-\text{original root covariance}
+
\text{power-small entire correction}.
}
$$

Hence the Campaign-47 Vaughan/Buchstab route does not supply an independent fixed-power arithmetic inequality.

Record:

```text
CAMPAIGN_47_VAUGHAN_BUCHSTAB_BRANCH
STRUCTURALLY_CLOSED_AT_EMPTY_DIVISOR_HARD_CORE
```

This does not close the root problem itself.

---

# 15. Entry rule for a future campaign

Any new **linear** arithmetic transform $g(n)$ should first be tested spectrally.

Let

$$
G(s)
=
\sum_n
g(n)n^{-s}.
$$

If one can write

$$
\boxed{
G(s)
=
c\,
\frac{\zeta'(s)}{\zeta(s)}
+
E(s),
}
$$

with

$$
c\ne0
$$

and $E$ free of nontrivial zeta-zero poles, then $g$ carries the same one-point prime-error hard core.

Such a transform should be rejected as a new amplifier representation unless it introduces a genuinely new nonlinear inequality.

A future campaign should therefore prioritize:

```text
nonlinear / multi-copy ordinary-prime boundary breaking
```

rather than another linear convolution or truncated-factorization transform.

---

# 16. External calibration

## 16.1. Friedlander–Iwaniec

J. Friedlander and H. Iwaniec,
*Asymptotic sieve for primes*,
Annals of Mathematics 148 (1998), 1041–1065.

They introduce a Möbius-sensitive bilinear axiom specifically to break the sieve parity problem.

URL:

https://arxiv.org/abs/math/9811186

## 16.2. Ford–Maynard

K. Ford and J. Maynard,
*On the theory of prime producing sieves*,
2024.

They establish a general Type-I / Type-II framework and prove that a substantial Type-II range is always necessary to guarantee a nontrivial lower bound for primes in an arbitrary nonnegative sequence.

URL:

https://arxiv.org/abs/2407.14368

These results justify treating parity-sensitive bilinear information as genuine arithmetic input, while the present paper shows that the specific truncated-Möbius anatomy of Campaign 47 does not escape the root hard core.

---

# 17. State transition

Advance candidate state

$$
v1.70
\to
v1.71.
$$

Add:

```text
B-RH-131
TRUNCATED_MOBIUS_CUTOFF_INCREMENTS_CARRY_AN_EXPLICIT_ZETA_FACTOR

B-RH-132
THE_VAUGHAN_COFACTOR_ZERO_VALUE_IS_A_CONSERVED_QUANTITY_ALONG_THE_MOBIUS_CUTOFF_FLOW

B-RH-133
THE_UNIVERSAL_VAUGHAN_ZERO_CHARGE_IS_LOCALIZED_AT_THE_EMPTY_DIVISOR_BRANCH

B-RH-134
ALL_NONTRIVIAL_ZERO_POLES_OF_THE_VAUGHAN_BALANCED_COEFFICIENT_ALREADY_OCCUR_IN_THE_D_EQUALS_ONE_BRANCH

B-RH-135
TRUNCATED_MOBIUS_PARITY_DEFECT_IS_TRANSPORTED_TO_THE_COMPLEMENTARY_DIVISOR_SCALE_ON_SQUAREFREE_INTEGERS

B-RH-136
THE_RENORMALIZED_VAUGHAN_REGULAR_SECTOR_MINUS_ITS_MEAN_HAS_ENTIRE_CONTINUATION

B-RH-137
RENORMALIZED_VAUGHAN_COEFFICIENT_EQUALS_NEGATIVE_PRIME_ERROR_PLUS_AN_ENTIRE_CORRECTION

B-RH-138
THE_ENTIRE_VAUGHAN_CORRECTION_PAIRS_WITH_THE_SIGNED_ROOT_SEQUENCE_ONLY_THROUGH_THE_ALREADY_CONTROLLED_TYPE_I_ERROR

O-RH-178
BUCHSTAB_OR_DIVISOR_SIZE_SHELLS_CANNOT_CHANGE_THE_UNIVERSAL_RIGHTMOST_ZERO_RESIDUE
```

Update:

```text
F-RH-024
CLOSED_AS_ROOT_EQUIVALENT_REPRESENTATION

F-RH-025
CLOSED_AS_NONAMPLIFYING_BUCHSTAB_REORGANIZATION
```

No RH certificate is created.

---

# 18. Conclusion

The truncated Möbius cutoff has a conserved zeta-zero charge.

That charge is not distributed among the nonempty divisor shells.

It sits entirely in the empty-divisor branch.

All Buchstab cutoff increments are zero-pole-free.

After the exact Vaughan renormalization, the remaining coefficient is exactly the negative prime error plus an entire correction whose pairing with the signed root sequence is already power-controlled.

Therefore the Campaign-47 Vaughan/Buchstab route has returned exactly to the original root covariance.

The next genuinely new route must be nonlinear or multi-copy.
