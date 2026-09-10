# CSM_RH Paper 47
## Exact Cross- $j$ Binomial Recombination, Loss of the Component Amplifier, and Root-Lag Recoupling

**Project:** CSM_RH  
**Paper:** 47  
**Version:** 0.1  
**Date:** 2026-09-07  
**Campaign:** 43 — `WEIGHTED_LIOUVILLE_POLYNOMIAL_PHASE_ATTACK`  
**Tracks:** WL4 — `CROSS_J_PRE_SQUARE_RECOMBINATION`; WL5 — `ROOT_RECOUPLING_COMPARISON`  
**Canonical state transition:** v1.37 to v1.38

---

# 0. Trust boundary

This paper continues directly from CSM_RH Paper 46.

Papers 43--46 showed that the isolated top-level pure-Mobius Type-II core cannot presently be closed at the required fixed power by any of the following mechanisms alone:

1. phase-only determinant-fibre dispersion;
2. Liouville-aware Ramare extraction;
3. structured-weight decoupling.

The remaining Campaign 43 alternative is to undo the componentwise architecture itself.
The exact Heath--Brown identity contains the alternating coefficients

$$
(-1)^{j-1}\binom Lj,
$$

so WL4 asks whether several $j$ -levels cancel before any componentwise absolute value, translated mean square, or Type-II squaring is applied.

The answer is algebraically strong but analytically non-promoting:

$$
\boxed{
\text{the full cross-}j\text{ sum recombines exactly to }\Lambda
}
$$

on the prescribed range.

Thus cross- $j$ cancellation is real.
However, it does not produce a new fixed-power estimate.
It removes the isolated Type-II component interface and returns the proof to the original prime residual.

WL5 then compares that recombined object with the root frontier.
The root remains open.

No proof or disproof of RH is claimed.
No fixed zero-free strip, fixed-power Mertens estimate, or fixed-power PNT remainder is assumed.

---

# 1. Exact Heath--Brown level notation

Fix

$$
L=\left\lceil\frac{10}{\varepsilon}\right\rceil
$$

and use the inherited normalization

$$
z=(2X)^{1/L}.
$$

Let

$$
\delta(1)=1,
\qquad
\delta(n)=0
\quad(n>1)
$$

be the identity for Dirichlet convolution.

Define the truncated Mobius function

$$
M_z(n)=\mu(n)1_{n\le z},
$$

and let

$$
\mathbf 1(n)=1,
\qquad
\ell(n)=\log n.
$$

The inherited Heath--Brown identity is

$$
\boxed{
\Lambda(n)
=
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj
H_j(n)
}
$$

for the prescribed output range, where

$$
\boxed{
H_j
=
M_z^{*j}
*
\mathbf 1^{*(j-1)}
*
\ell.
}
$$

Here $*$ denotes Dirichlet convolution.

The essential point of WL4 is that the alternating coefficients must be retained before applying any nonlinear operation such as absolute value or squaring.

---

# 2. Binomial form of every $j$ -level

Use the classical identity

$$
\boxed{
\ell
=
\Lambda*\mathbf 1.
}
$$

Define

$$
\boxed{
A_z
=
M_z*\mathbf 1.
}
$$

Then

$$
\begin{aligned}
H_j
&=
M_z^{*j}
*
\mathbf 1^{*(j-1)}
*
(\Lambda*\mathbf 1)
\\
&=
\Lambda
*
(M_z*\mathbf 1)^{*j}.
\end{aligned}
$$

Therefore

## Theorem 2.1 — Exact $j$ -level factorisation

$$
\boxed{
H_j
=
\Lambda*A_z^{*j}.
}
$$

This identity is purely algebraic.
It is valid before dyadic subdivision and before Type-I/Type-II grouping.

---

# 3. Exact cross- $j$ binomial recombination

The alternating Heath--Brown sum becomes

$$
\begin{aligned}
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj H_j
&=
\Lambda*
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj A_z^{*j}.
\end{aligned}
$$

The convolution binomial theorem gives

$$
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj A_z^{*j}
=
\delta-(\delta-A_z)^{*L}.
$$

Define

$$
\boxed{
R_z
=
\delta-A_z.
}
$$

Hence

## Theorem 3.1 — Cross- $j$ binomial recombination identity

$$
\boxed{
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj H_j
=
\Lambda*(\delta-R_z^{*L}).
}
$$

The cancellation mechanism is now explicit.
It is not a heuristic consequence of alternating signs.
It is a finite convolution binomial identity.

---

# 4. The support gap that kills the binomial remainder

For

$$
2\le n\le z,
$$

every divisor of $n$ is at most $z$, so

$$
A_z(n)
=
\sum_{d\mid n}\mu(d)
=
0.
$$

Also

$$
A_z(1)=1.
$$

Therefore

$$
R_z(n)=0
$$

for all

$$
1\le n\le z.
$$

Thus every integer in the support of $R_z$ is strictly larger than $z$.
Consequently every integer in the support of

$$
R_z^{*L}
$$

is strictly larger than

$$
z^L=2X.
$$

Hence

$$
\boxed{
R_z^{*L}(n)=0
\qquad
(n\le2X).
}
$$

Combining with Theorem 3.1 yields:

## Theorem 4.1 — Exact pre-square Heath--Brown recombination

For the inherited normalization and every

$$
n\le2X,
$$

we have

$$
\boxed{
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj H_j(n)
=
\Lambda(n).
}
$$

For output blocks enlarged by a fixed multiplicative constant, the same argument is obtained by enlarging the harmless constant in $z^L$.
No exponent changes.

Create:

```text
B-RH-029
HEATH_BROWN_CROSS_J_BINOMIAL_RECOMBINATION_TO_LAMBDA
CERTIFIED
```

This closes the previously unaudited algebraic possibility from Paper 41:
cross- $j$ cancellation is genuine.

---

# 5. Actual dyadic product-support overlap across adjacent $j$ -levels

The exact identity of Section 4 occurs before dyadic subdivision.
WL4 nevertheless requires checking that the $j$ -levels are not formally disjoint after localization.

Consider the top level $j=L$.
Take a legal pure-core dyadic cell with

$$
m_i\sim U_i
\qquad
(1\le i\le L),
$$

$$
n_1=2,
$$

and

$$
n_2=\cdots=n_L=1.
$$

Its output scale is

$$
\boxed{
N_{\rm out}
\asymp
2\prod_{i=1}^{L}U_i
\asymp X.
}
$$

Now fix one index $r$.
At level $j=L-1$, retain the Mobius variables on the scales

$$
U_i
\qquad
(i\ne r),
$$

and use one smooth variable on scale

$$
U_r.
$$

For example, take

$$
n_1=2,
\qquad
n_2\sim U_r,
$$

with the other identity-scale smooth variables fixed at $1$.
Then again

$$
\boxed{
N_{\rm out}
\asymp
2U_r
\prod_{i\ne r}U_i
\asymp X.
}
$$

Therefore adjacent $j$ -levels have genuine overlap after multiplication pushforward to the same output dyadic block.

This verifies that cross- $j$ recombination is not forbidden by disjoint output support.

However, the internal factor coordinates are not the same:

1. the $j=L$ cell contains a Mobius factor on scale $U_r$ ;
2. the $j=L-1$ cell replaces that coordinate by a smooth factor;
3. their coefficient signs and factor multiplicities differ;
4. the exact cancellation occurs only after summing the complete divisor/factorisation families.

Thus there is no canonical cell-by-cell cancellation rule.

Create:

```text
O-RH-121
CROSS_J_CANCELLATION_IS_GLOBAL_MULTIPLICATIVE_PUSHFORWARD_NOT_DYADIC_CELLWISE
CERTIFIED AS STRUCTURAL LOCALIZATION
```

---

# 6. Linear translated-frequency transforms commute with recombination

Let

$$
\mathcal T
$$

be any linear operator on coefficient sequences supported on the prescribed output block.
This includes:

1. formation of a Dirichlet polynomial;
2. restriction to a translated frequency interval;
3. multiplication by the Gaussian window used in Paper 42;
4. any fixed linear smoothing applied before the square is expanded.

Linearity gives

$$
\boxed{
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj
\mathcal T H_j
=
\mathcal T\Lambda.
}
$$

After a complete dyadic partition

$$
H_j
=
\sum_{\nu}H_{j,\nu},
$$

we similarly have

$$
\boxed{
\sum_{j=1}^{L}
(-1)^{j-1}\binom Lj
\sum_{\nu}
\mathcal T H_{j,\nu}
=
\mathcal T\Lambda.
}
$$

Therefore the cross- $j$ translated-frequency terms do not define a new coefficient family.
They are exactly the cross terms required to reconstruct the transformed von Mangoldt sequence.

Create:

```text
B-RH-030
LINEAR_TRANSLATED_OPERATOR_COMMUTES_WITH_EXACT_CROSS_J_RECOMBINATION
CERTIFIED
```

---

# 7. What happens after squaring

Suppose the target norm is Hilbertian.
Write

$$
b_j
=
(-1)^{j-1}\binom Lj.
$$

Then

$$
\left\|
\sum_j b_j\mathcal T H_j
\right\|_2^2
=
\sum_{j,k}
b_jb_k
\left\langle
\mathcal T H_j,
\mathcal T H_k
\right\rangle.
$$

By Theorem 4.1 and Section 6,

$$
\boxed{
\sum_{j,k}
b_jb_k
\left\langle
\mathcal T H_j,
\mathcal T H_k
\right\rangle
=
\|\mathcal T\Lambda\|_2^2.
}
$$

Thus cross- $j$ inner products can indeed cancel a large component norm.
But the exact result of all such cancellation is simply the original Lambda-level norm.

Nothing in the alternating signs alone implies

$$
\|\mathcal T\Lambda\|_2^2
\le
X^{-\delta}
\sum_j
\|\mathcal T H_j\|_2^2
$$

for a fixed

$$
\delta>0.
$$

The left side is an arithmetic quantity that must still be estimated.

In particular, once the square has been expanded, the cross terms are not sign-definite.
The factors

$$
b_jb_k
$$

do not determine the signs or phases of

$$
\left\langle
\mathcal T H_j,
\mathcal T H_k
\right\rangle.
$$

Therefore:

## Theorem 7.1 — Exact recombination is not a power estimate

The Heath--Brown alternating coefficients certify an exact pre-square identity, but they do not by themselves certify any fixed- $X$ -power contraction of the translated mean square.

Create:

```text
O-RH-122
ALTERNATING_CROSS_J_SIGNS_RECOMBINE_EXACTLY_BUT_DO_NOT_BY_THEMSELVES_BOUND_THE_RECOMBINED_NORM
CERTIFIED AS METHOD-SCOPE BARRIER
```

---

# 8. Why the polynomial- $W$ component amplifier disappears after recombination

The bridge

```text
B-RH-014
POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
```

is a component bridge.
It applies after a Type-II factorization has produced a product of separated Dirichlet factors and the required polynomial- $W$ mean-square hypothesis has been verified for that component.

Exact cross- $j$ recombination occurs earlier.
It sums the component family back to

$$
\Lambda.
$$

At this stage there is no distinguished pair

$$
\alpha*\beta
$$

to which B-RH-014 can automatically be applied.

Therefore one cannot combine the two statements as

$$
\text{exact cross-}j\text{ recombination}
+
\text{B-RH-014}
\Longrightarrow
\text{fixed power}.
$$

That inference would use the Type-II amplifier after deleting the Type-II interface on which it is defined.

Create:

```text
O-RH-123
PRE_SQUARE_CROSS_J_RECOMBINATION_REMOVES_THE_COMPONENTWISE_TYPEII_AMPLIFIER_INTERFACE
CERTIFIED
```

This is the central analytic closure of WL4.

---

# 9. Recombination inside the actual Lambda-minus-Lambda-sharp residual

The 2026 higher-uniformity theorem is not a theorem for bare $\Lambda$.
Its prime residual is

$$
\Lambda-\Lambda^\sharp.
$$

The published approximant is

$$
\Lambda^\sharp(n)
=
\frac{P(R)}{\varphi(P(R))}
1_{(n,P(R))=1},
$$

with

$$
R
=
\exp((\log X)^{1/10}).
$$

The same paper proves that $\Lambda^\sharp$ can be replaced, with negligible short-interval error at its stated precision, by an essentially Type-I model.

Cross- $j$ recombination applies to the Heath--Brown decomposition of $\Lambda$.
It does not make $\Lambda^\sharp$ disappear.

Thus before the componentwise triangle inequality, the exact residual is simply restored to

$$
\boxed{
\Lambda-\Lambda^\sharp.
}
$$

Hence WL4 has not produced a new residual theorem.
It has undone the decomposition that created the isolated pure-Mobius Type-II obstruction.

This is a valid structural success:

$$
\boxed{
\text{pure-core obstruction}
\not\Rightarrow
\text{global impossibility}
}
$$

because the global identity can cancel it.

But it is not an analytic promotion:

$$
\boxed{
\text{global identity}
\not\Rightarrow
\text{fixed-power residual estimate}.
}
$$

WL4 therefore closes as

```text
CLOSED_AS_EXACT_BINOMIAL_RECOMBINATION_TO_THE_ORIGINAL_LAMBDA_RESIDUAL_WITHOUT_POWER_GAIN
```

---

# 10. WL5: exact root comparison begins with the centered prime increment

The root PESC frontier from Paper 11 uses the prime-only centered increment

$$
c_n
=
1_{\mathbb P}(n)\log n-1.
$$

Let

$$
B(n)
=
\sum_{m\le n}c_m
=
\vartheta(n)-n.
$$

The PESC correlation is

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{n<2N}
w_N(n)c_nB(n-1).
}
$$

Expanding the cumulative error gives

$$
\mathcal C_N^\vartheta
=
\sum_{n<2N}
\sum_{m<n}
w_N(n)c_mc_n.
$$

Writing

$$
h=n-m
$$

gives the exact positive-lag form:

## Theorem 10.1 — PESC triangular lag-kernel identity

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{h\ge1}
\sum_{m\ge1}
w_N(m+h)
c_m c_{m+h},
}
$$

where the weight automatically enforces

$$
m+h<2N.
$$

Thus PESC is itself a weighted two-point correlation problem, but with a specific endogenous triangular lag kernel rather than one isolated exogenous shift.

Create:

```text
B-RH-031
PESC_TRIANGULAR_POSITIVE_LAG_AUTOCORRELATION_IDENTITY
CERTIFIED
```

This is the correct root-level object to compare with the translated two-point kernels that appeared in Papers 42--46.

---

# 11. Von Mangoldt recoupling and prime powers

Define the centered von Mangoldt increment

$$
\widetilde c_n
=
\Lambda(n)-1.
$$

The difference

$$
\widetilde c_n-c_n
$$

is supported on proper prime powers.

Papers 10--11 already certified that the total proper-prime-power contribution to the corresponding dyadic energy is

$$
O(N^{5/2+o(1)}).
$$

Therefore for every fixed

$$
0<\kappa<\frac12,
$$

the root target

$$
N^{3-\kappa+o(1)}
$$

dominates the prime-power correction.

At the root-admission exponent range, the prime-only PESC kernel and the centered-von-Mangoldt lag kernel are therefore exponent-equivalent under the already certified prime-power bridge.

This makes the return from Heath--Brown recombination to the prime-error root mathematically natural.
It does not create a fixed exponent.

---

# 12. The Lambda-sharp model gap is still a separate bridge requirement

Cross- $j$ recombination restores

$$
\Lambda-\Lambda^\sharp.
$$

The PESC/MLEPG root is built from

$$
\Lambda-1
$$

or its prime-only analogue.

These differ by

$$
\Lambda^\sharp-1.
$$

Hence a fixed-power theorem for the residual

$$
\Lambda-\Lambda^\sharp
$$

would not automatically be a fixed-power root theorem unless the model discrepancy is also controlled at compatible strength.

This is exactly the root-observability gate created in Paper 37:

```text
fixed power in some transformed/residual observable
  !=
fixed power in PESC/MLEPG
```

without a proved deterministic bridge.

The current 2026 theorem gives arbitrary fixed logarithmic precision for the residual on almost all relevant intervals.
It does not supply the fixed- $X$ -power root bridge required here.

Create:

```text
O-RH-124
LAMBDA_SHARP_RESIDUAL_RECOUPLING_REQUIRES_A_SEPARATE_FIXED_POWER_MODEL_TO_ROOT_BRIDGE
CERTIFIED AS ROOT-OBSERVABILITY GATE
```

No new frontier is created for this statement.
It returns ownership of the unresolved fixed-power problem to the existing root frontiers.

---

# 13. WL5 verdict

WL5 asked:

> if WL4 collapses back to the full prime-error coefficient, compare the resulting object directly with F-RH-010 rather than pretending a new component theorem has been obtained.

The comparison is now complete.

The exact chain is

$$
\boxed{
\begin{aligned}
&\text{full Heath--Brown }j\text{-sum}
\\
&\qquad\longrightarrow
\Lambda
\\
&\qquad\longrightarrow
\Lambda-\Lambda^\sharp
\quad\text{in the actual residual theorem}
\\
&\qquad\longrightarrow
\text{root comparison with }\Lambda-1
\\
&\qquad\longrightarrow
\text{PESC triangular lag kernel after the model bridge}.
\end{aligned}
}
$$

The first arrow is exact and certified.
The second is bookkeeping of the actual theorem.
The third requires a quantitative model-to-root bridge.
The fourth is the existing prime-error root architecture.

No fixed- $X$ -power estimate is produced by the first two arrows.

Therefore WL5 closes as

```text
CLOSED_AS_ROOT_RECOUPLING_WITHOUT_A_NEW_FIXED_POWER_THEOREM
```

---

# 14. Campaign 43 closure

Campaign 43 started from the weighted Liouville polynomial-phase core and audited five logically different mechanisms.

The final record is:

```text
WL1
  CLOSED_AS_ARCHIMEDEAN_GAUGE_AND_EVEN_ORDER_LIOUVILLE_BARRIER

WL2
  CLOSED_AS_EXACT_MARKED_EXTRACTION_WITH_PRIME_HARMONIC_AND_SMOOTH_CARRIER_BARRIERS

WL3
  CLOSED_AS_NATURAL_L2_SATURATION_BOUNDED_MARK_MULTIPLICITY_AND_DETERMINANT_CYCLE_BARRIER

WL4
  CLOSED_AS_EXACT_BINOMIAL_RECOMBINATION_TO_THE_ORIGINAL_LAMBDA_RESIDUAL_WITHOUT_POWER_GAIN

WL5
  CLOSED_AS_ROOT_RECOUPLING_WITHOUT_A_NEW_FIXED_POWER_THEOREM
```

Campaign 43 therefore closes as

```text
CLOSED_AS_COMPONENT_MECHANISMS_EXHAUSTED_AND_EXACTLY_RECOUPLED_TO_ROOT_PRIME_ERROR
```

This is not an impossibility theorem for all future approaches.
It is a closure theorem for the audited component architecture.

---

# 15. What was learned from the cross- $j$ audit

The main conceptual lesson is subtle.

Paper 41 was correct not to promote the pure-Mobius component obstruction to a global impossibility claim.
The cross- $j$ cancellation really exists.

But the cancellation is not a hidden source of free analytic power.
It is the algebraic mechanism by which Heath--Brown's inclusion-exclusion decomposition returns to the function it decomposed.

Thus:

$$
\boxed{
\text{decomposition can create a hard component}
}
$$

and simultaneously

$$
\boxed{
\text{exact recombination can cancel that component}
}
$$

without either statement implying

$$
\boxed{
\text{a stronger theorem for the undecomposed function}.
}
$$

This separates three logically distinct claims:

1. component hardness;
2. decomposition-level cancellation;
3. root arithmetic contraction.

Only the third can promote the RH frontier.

---

# 16. New root-directed continuation

After Campaign 43, further work should not continue inventing new names for the same Heath--Brown pure-core obstruction.

The exact root object from Theorem 10.1 suggests a direct campaign:

```text
CSM_RH Campaign 44
PESC_TRIANGULAR_LAG_KERNEL_ATTACK
```

The target is the root-observing correlation

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{h\ge1}
\sum_m
w_N(m+h)c_mc_{m+h}.
}
$$

This route keeps the prime-error coefficient itself visible from the start.
It does not pass through a componentwise Heath--Brown triangle inequality.

---

# 17. Campaign 44 tracks

## PK1 — exact kernel normalization

Rewrite the PESC weight

$$
w_N(m+h)
$$

as an explicit triangular lag-position kernel and isolate the lower-order boundary/diagonal pieces.

## PK2 — spectral representation

Derive a Fourier or Mellin representation of the triangular positive-lag kernel without replacing the signed prime-error coefficient by an absolute value.

The representation must retain the principal low-frequency mode required by the root-observability gate.

## PK3 — translated-window synthesis

Compare the root triangular kernel with the translated Gaussian/Mellin kernels used in Paper 42.

Determine whether a controlled superposition of translated windows reconstructs the PESC kernel with power-safe condition number.

A logarithmically ill-conditioned synthesis does not count as fixed-power progress.

## PK4 — centered-Lambda / prime-only bridge

Keep proper prime powers explicit and use the already certified

$$
O(N^{5/2+o(1)})
$$

prime-power floor when

$$
0<\kappa<\frac12.
$$

## PK5 — fixed-power admission

A successful theorem must prove

$$
\boxed{
|\mathcal C_N^\vartheta|
\ll
N^{3-\kappa+o(1)}
}
$$

for one fixed

$$
\kappa>0
$$

in the root-admissible range, without a hidden fixed zero-free strip.

---

# 18. Campaign 44 rejection filters

Reject a candidate if:

## R1. It proves a fixed-power estimate for a kernel that does not deterministically observe PESC/MLEPG.

## R2. It removes the low-frequency portion of the prime-error coefficient and then claims root control.

## R3. It obtains only $X^{-o(1)}$, logarithmic, or qualitative cancellation.

## R4. It uses a fixed-power PNT/Mertens estimate or fixed zero-free strip as an input.

## R5. It approximates the triangular kernel by translated windows with a power-sized uncontrolled reconstruction loss.

## R6. It returns to componentwise Heath--Brown absolute values without a new root-level bridge.

---

# 19. External calibration

The scope of this paper is consistent with the current published architecture.

1. K. Matomaki, M. Radziwill, X. Shao, T. Tao, J. Teravainen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`. The paper states the Heath--Brown decomposition into Type-I, Type- $I_2$, and Type-II sums and treats the prime residual $\Lambda-\Lambda^\sharp$ with arbitrary fixed logarithmic precision on almost all intervals in its range.

2. The same paper defines
   $$
   \Lambda^\sharp(n)
   =
   \frac{P(R)}{\varphi(P(R))}1_{(n,P(R))=1}
   $$
   and proves that it is, up to a negligible error at the published scale, essentially Type-I.

3. CSM_RH Papers 10--11 already certify that proper prime powers are lower order for the first fixed-strip root exponent range $0<\kappa<1/2$ and that PESC is exponent-equivalent to the prime-only dyadic error energy.

No external source is promoted here to a fixed- $X$ -power PESC theorem.

---

# 20. State transition

The canonical state advances from v1.37 to v1.38.

New certified bridges:

```text
B-RH-029
HEATH_BROWN_CROSS_J_BINOMIAL_RECOMBINATION_TO_LAMBDA
CERTIFIED

B-RH-030
LINEAR_TRANSLATED_OPERATOR_COMMUTES_WITH_EXACT_CROSS_J_RECOMBINATION
CERTIFIED

B-RH-031
PESC_TRIANGULAR_POSITIVE_LAG_AUTOCORRELATION_IDENTITY
CERTIFIED
```

New certified obstructions/refinements:

```text
O-RH-121
CROSS_J_CANCELLATION_IS_GLOBAL_MULTIPLICATIVE_PUSHFORWARD_NOT_DYADIC_CELLWISE
CERTIFIED

O-RH-122
ALTERNATING_CROSS_J_SIGNS_RECOMBINE_EXACTLY_BUT_DO_NOT_BY_THEMSELVES_BOUND_THE_RECOMBINED_NORM
CERTIFIED

O-RH-123
PRE_SQUARE_CROSS_J_RECOMBINATION_REMOVES_THE_COMPONENTWISE_TYPEII_AMPLIFIER_INTERFACE
CERTIFIED

O-RH-124
LAMBDA_SHARP_RESIDUAL_RECOUPLING_REQUIRES_A_SEPARATE_FIXED_POWER_MODEL_TO_ROOT_BRIDGE
CERTIFIED
```

Root status remains

```text
F-RH-010  PRIME_ERROR_SELF_CORRELATION  OPEN
F-RH-016  MESOSCOPIC_LAG_ENERGY_POWER_GAIN  OPEN
RH_PROVED  FALSE
RH_DISPROVED  FALSE
GLOBAL_RH_CERTIFICATE  FALSE
```

Campaign 43 is closed.

Campaign 44 is ready at

```text
PK1
EXACT_PESC_TRIANGULAR_KERNEL_NORMALIZATION
```

---

# 21. Final status

The accepted advance is

$$
\boxed{
\text{cross-}j\text{ cancellation is exact}
}
$$

but

$$
\boxed{
\text{its exact value is the original }\Lambda\text{ object}.
}
$$

Therefore the pure-Mobius component is not a global obstruction, while the cross- $j$ identity is not a hidden fixed-power theorem either.

The campaign returns to the root at the exact positive-lag representation

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{h\ge1}
\sum_m
w_N(m+h)c_mc_{m+h}.
}
$$

Current canonical continuation:

```text
CSM_RH Paper 47
state v1.38
Campaign 43 CLOSED
Campaign 44 READY
next: PK1 EXACT_PESC_TRIANGULAR_KERNEL_NORMALIZATION
```

No RH promotion occurs.
