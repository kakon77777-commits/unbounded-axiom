# CSM_RH Paper 32
## Residual-Weighted EMBF Equivalence, Abel Endogeneity Return, and the PACPSA Difference-Stability Bottleneck

**Project:** `CSM_RH`  
**Paper:** `32`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.22 / Paper 31`  
**Campaign:** `31 — ENDOGENOUS_PARITY_BILINEAR_REAUDIT`  
**Status:** residual parity-bilinear re-audit / coupled-sieve stability localization; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 31 identified the Friedlander–Iwaniec parity-breaking bilinear axiom with the EMBF geometry obtained from the PESC positivity lifts.

Campaign 31 reaudits that branch using later CSM_RH results:

```text
Lambda-sharp has subpolynomial centered primitive;
the prime residual has strong almost-all local uniformity;
PESC remains fixed-exponent equivalent after sieve subtraction.
```

The campaign obtains one positive bridge and three closure results.

1. EMBF is fixed-exponent equivalent, throughout the first-strip range, to the same Möbius bilinear form weighted by the residual primitive
   $$
   F=\sum(\Lambda-\Lambda^\sharp).
   $$

2. Abel summation does not externalize the endogenous weight for free: differentiating $F$ returns block sums of the prime residual $f=\Lambda-\Lambda^\sharp$.

3. Current almost-all short-interval theorems do not control the multiplicative grids sampled by EMBF.

4. Removing the outer absolute value destroys the dual sign-uniformity built into the Friedlander–Iwaniec parity axiom.

The remaining parity-side mechanism is therefore PACPSA difference stability.

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical EMBF

Let

$$
B_\vartheta(x)=\vartheta(x)-x.
$$

For a dyadic $n$ -range

$$
L<n\le2L
$$

and parameter $C$, define

$$
\gamma(n,C)
=
\sum_{\substack{d\mid n\\d\le C}}\mu(d).
$$

Paper 13 defines the endogenous Möbius bilinear fidelity seminorm

$$
\boxed{
\mathfrak B_{N,L,C}[B_\vartheta]
=
\sum_m
\left|
\sum_{\substack{
L<n\le2L\\
mn<2N
}}
\gamma(n,C)\mu(mn)w_N(mn)
B_\vartheta(mn-1)
\right|.
}
$$

The endpoint multiplicity satisfies

$$
0\le w_N(k)\le N.
$$

---

# 2. Residual primitive

Use the modern sieve approximant

$$
\Lambda^\sharp(n)
=
\frac{P(R)}{\varphi(P(R))}
1_{\gcd(n,P(R))=1},
$$

with

$$
R
=
\exp
\left(
(\log N)^{1/10}
\right).
$$

Define

$$
f(n)
=
\Lambda(n)-\Lambda^\sharp(n),
$$

and

$$
\boxed{
F(x)
=
\sum_{n\le x}f(n).
}
$$

Define also

$$
B^\sharp(x)
=
\sum_{n\le x}
[
\Lambda^\sharp(n)-1
].
$$

Paper 28 gives

$$
\boxed{
B^\sharp(x)
=
N^{o(1)}
}
$$

uniformly for $x\le2N$.

Since

$$
F(x)+B^\sharp(x)
=
\psi(x)-x,
$$

while

$$
B_\vartheta(x)
=
\vartheta(x)-x,
$$

we have

$$
\boxed{
B_\vartheta(x)
=
F(x)
+
B^\sharp(x)
-
[
\psi(x)-\vartheta(x)
].
}
$$

---

# 3. Prime-power correction

The prime-power difference satisfies

$$
\psi(x)-\vartheta(x)
=
\sum_{\substack{p^j\le x\\j\ge2}}
\log p
=
x^{1/2+o(1)}.
$$

Therefore:

## Theorem 3.1 — Residual Primitive Approximation

Uniformly for $x\le2N$,

$$
\boxed{
B_\vartheta(x)
=
F(x)
+
O
\left(
N^{1/2+o(1)}
\right).
}
$$

The $N^{1/2}$ term is the prime-power barrier already present in Paper 10.

---

# 4. Pair-count lemma

The EMBF range contains only $O(N)$ pairs.

Indeed,

$$
\begin{aligned}
\#\{
(m,n):
L<n\le2L,\,
mn<2N
\}
&\le
\sum_{L<n\le2L}
\frac{2N}{n}
\\
&=
O(N).
\end{aligned}
$$

Also

$$
|\gamma(n,C)|
\le
\tau(n)
=
N^{o(1)}
$$

uniformly, with no restriction that $C$ be fixed.

---

# 5. Residual-weight EMBF equivalence

Define

$$
\boxed{
\mathfrak B_{N,L,C}[F]
=
\sum_m
\left|
\sum_{\substack{
L<n\le2L\\
mn<2N
}}
\gamma(n,C)\mu(mn)w_N(mn)
F(mn-1)
\right|.
}
$$

The seminorm is Lipschitz in its weight.

Using Theorem 3.1, Section 4, and $w_N\le N$:

## Theorem 5.1 — Residual-Weighted EMBF Equivalence

$$
\boxed{
\left|
\mathfrak B_{N,L,C}[B_\vartheta]
-
\mathfrak B_{N,L,C}[F]
\right|
\ll
N^{5/2+o(1)}.
}
$$

Therefore, for every fixed

$$
0<\kappa<\frac12,
$$

a target of size

$$
N^{3-\kappa+o(1)}
$$

is unchanged by the replacement

$$
B_\vartheta
\rightsquigarrow
F.
$$

Create:

```text
B-RH-007
SIEVE_RESIDUAL_EMBF_EQUIVALENCE
status:
  CERTIFIED
```

This joins the parity branch to the residual branch of Papers 28–30.

---

# 6. What the replacement means

After Theorem 5.1, the parity-side critical object is

$$
\boxed{
\sum_m
\left|
\sum_n
\gamma(n,C)\mu(mn)w_N(mn)
F(mn-1)
\right|.
}
$$

Thus the modern sieve model removes the local small-prime structure from the endogenous weight.

The remaining weight is exactly the primitive of the true prime residual

$$
f=\Lambda-\Lambda^\sharp.
$$

The PESC-hard low-frequency drift survives the model subtraction.

---

# 7. Attempted Möbius externalization

For fixed $m$, write the inner residual sum as

$$
\boxed{
S_m
=
\sum_{a<n\le b}
\alpha_m(n)
F(mn-1),
}
$$

where

$$
\alpha_m(n)
=
\gamma(n,C)\mu(mn)w_N(mn)
$$

and the interval is the relevant truncation of $(L,2L]$.

Define the partial sum

$$
\boxed{
A_m(t)
=
\sum_{a<n\le t}\alpha_m(n).
}
$$

Discrete Abel summation gives

$$
\boxed{
S_m
=
A_m(b)F(mb-1)
-
\sum_{t=a}^{b-1}
A_m(t)
[
F(m(t+1)-1)-F(mt-1)
]
}
$$

up to the harmless lower-endpoint convention.

---

# 8. Differentiating the endogenous weight returns the prime residual

Because $F$ is the primitive of $f$,

$$
\boxed{
F(m(t+1)-1)-F(mt-1)
=
\sum_{mt\le k<m(t+1)}
f(k).
}
$$

Thus any attempt to exploit cancellation in the Möbius coefficient partial sums $A_m(t)$ by Abel summation creates short block sums of

$$
\boxed{
f=\Lambda-\Lambda^\sharp.
}
$$

The endogenous weight cannot be treated as an arbitrary smooth external coefficient.

Create:

```text
O-RH-069
ABEL_EXTERNALIZATION_RETURNS_PRIME_RESIDUAL
status:
  CERTIFIED
```

This is the exact endogenous-fidelity mechanism behind the earlier abstract warning.

---

# 9. Modern Möbius short-interval input

Current higher-uniformity theory gives, for

$$
H\ge X^{1/3+\varepsilon},
$$

Möbius discorrelation against bounded-complexity nilsequences of size

$$
\boxed{
H\log^{-A}X
}
$$

for all but an exceptional set of starting points of measure

$$
\boxed{
O_A
\left(
X\log^{-A}X
\right).
}
$$

The same theorem gives the corresponding logarithmic residual estimate for

$$
\Lambda-\Lambda^\sharp.
$$

These are powerful local statements.

They are not automatically compatible with the multiplicative sampling geometry in Section 8.

---

# 10. Multiplicative-grid exceptional-set blindness

Consider the balanced EMBF geometry

$$
L=N^{1/2+o(1)},
\qquad
m=N^{1/2+o(1)}.
$$

The residual blocks produced by Section 8 have:

```text
length:
  m ~ N^{1/2}

starting points:
  mt

number of sampled starts for fixed m:
  about L ~ N^{1/2}.
```

But the current almost-all theorem permits an exceptional set of size

$$
N\log^{-A}N.
$$

For every fixed $A$,

$$
\boxed{
N\log^{-A}N
\gg
N^{1/2}.
}
$$

Therefore the theorem permits, without contradiction, every point in one fixed multiplicative grid

$$
\{
mt:
L<t\le2L
\}
$$

to be exceptional.

Hence:

## Theorem 10.1 — Exceptional-Set Grid Blindness

The current almost-all short-interval theorem does not, by cardinality alone, provide any nontrivial uniform control on a fixed balanced EMBF multiplicative grid.

Create:

```text
O-RH-070
ALMOST_ALL_EXCEPTIONAL_SET_MULTIPLICATIVE_GRID_BLINDNESS
status:
  CERTIFIED AS TRANSFERENCE OBSTRUCTION
```

This does not say the residual is actually large on such a grid.

It says the current theorem does not rule it out.

---

# 11. Why arbitrary choice of the log exponent does not fix the grid issue

The short-interval theorem permits every fixed $A>0$.

But the implied constants depend on $A$.

One may not take

$$
A=A(N)\to\infty
$$

without a theorem uniform in that parameter.

For each fixed $A$,

$$
\frac{
N\log^{-A}N
}{
N^{1/2}
}
=
N^{1/2}\log^{-A}N
\to\infty.
$$

Thus arbitrary fixed log-power precision remains insufficient for deterministic control of the multiplicative grid.

---

# 12. Outer absolute value as dual sign uniformity

For each outer variable $m$, write the EMBF inner sum as

$$
I_m.
$$

Then the exact duality identity is

## Theorem 12.1 — Outer-Absolute Duality

For complex $I_m$,

$$
\boxed{
\sum_m|I_m|
=
\sup_{\substack{|\varepsilon_m|\le1}}
\left|
\sum_m
\varepsilon_m I_m
\right|.
}
$$

The supremum is attained by choosing $\varepsilon_m$ to align the phases of the nonzero $I_m$.

Therefore the outer absolute value is equivalent to uniformity against an arbitrary outer sign/phase sequence.

Create:

```text
B-RH-008
EMBF_OUTER_ABSOLUTE_DUAL_UNIFORMITY
status:
  CERTIFIED
```

---

# 13. Why simply removing the outer absolute is not a certified shortcut

Removing the outer absolute controls only the single phase choice

$$
\varepsilon_m\equiv1.
$$

The Friedlander–Iwaniec axiom requires the entire dual family.

A toy example already shows the gap:

$$
I_m=(-1)^m.
$$

Then the unsigned aggregate is $O(1)$ while

$$
\sum_m|I_m|
$$

is the full number of outer variables.

Thus cancellation across $m$ can hide large parity-sensitive inner sums.

A signed aggregate may still be useful if a new direct PESC bridge is proved.

No such bridge is obtained in Campaign 31.

---

# 14. PACPSA difference-stability problem

The two PESC positivity lifts are

$$
a_n^\pm
=
w_N(n)
[
M_N\pm B_\vartheta(n-1)
].
$$

The Friedlander–Iwaniec theorem is formulated for real nonnegative sequences.

Its prime-detection asymptotic has an error proportional to the total positive mass of the input sequence.

Applying such a theorem separately to $a^+$ and $a^-$ gives no certified cancellation between the two theorem errors.

Even if the two lifts share a huge common background

$$
M_Nw_N(n),
$$

separate estimates only give

$$
|\mathrm{Err}(a^+)-\mathrm{Err}(a^-)|
\le
|\mathrm{Err}(a^+)|
+
|\mathrm{Err}(a^-)|.
$$

The common positive mass is therefore paid twice unless a new coupled stability theorem is proved.

---

# 15. Size of the common positivity background

The endpoint weights satisfy

$$
\sum_{n<2N}w_N(n)
\asymp
N^2.
$$

Positivity requires

$$
M_N
\ge
\max_{j<2N}|B_\vartheta(j)|.
$$

Current unconditional PNT bounds make $M_N$ smaller than $N$ by a subpower factor, but not by a fixed power.

Thus the common positivity mass remains

$$
\boxed{
M_NN^2
=
N^{3-o(1)}
}
$$

at current unconditional strength.

A relative asymptotic-sieve error of logarithmic size therefore remains

$$
\boxed{
N^{3-o(1)}.
}
$$

It does not yield PESC $(\kappa)$.

---

# 16. Why standard asymptotic-sieve output does not give difference stability

The classical Friedlander–Iwaniec prime asymptotic has relative error

$$
O
\left(
\frac{\log\delta(x)}{\log\Delta(x)}
\right).
$$

For the practical parameter class this is

$$
O
\left(
\frac{\log\log x}{\log x}
\right).
$$

The theorem supplies an estimate for each nonnegative input sequence.

It does not state a Lipschitz bound for the difference of theorem errors in terms of the signed perturbation

$$
a^+-a^-
=
2w_NB_\vartheta.
$$

Such a theorem would be exactly the missing coupled difference-stability input.

Create:

```text
O-RH-071
SEPARATE_POSITIVE_LIFT_SIEVE_ERROR_FLOOR
status:
  CERTIFIED AS CURRENT-THEOREM AUDIT
```

---

# 17. PACPSA restated after Campaign 31

Paper 15 introduced

```text
F-RH-014
PACPSA
POWER_ACCURATE_COUPLED_PARITY_SIEVE_ASSEMBLY
```

Campaign 31 sharpens its meaning:

> PACPSA is not merely "apply an asymptotic sieve to two lifts." It requires a theorem whose error functional is stable at the difference level, so that the common $N^{3-o(1)}$ positivity background cancels before the error estimate is paid.

This is now the only parity-side mechanism not already closed by the re-audit.

---

# 18. Campaign 31 track audit

## V1 — Lambda-sharp subtraction inside EMBF

```text
status:
  SUCCESS

result:
  B-RH-007

first-strip replacement error:
  N^(5/2+o(1))
```

## V2 — modern Möbius / Liouville short-interval uniformity

```text
status:
  DOES NOT TRANSFER DIRECTLY

reasons:
  endogenous Abel differentiation;
  multiplicative-grid exceptional-set blindness;
  log/subpower precision
```

## V3 — low-frequency projection of the endogenous weight

```text
status:
  NO CANONICAL FIXED-POWER PROJECTION FOUND

smooth external projection:
  Möbius control remains log/subpower
```

## V4 — remove the outer absolute value

```text
status:
  OUTER ABSOLUTE = DUAL SIGN UNIFORMITY

removal:
  strictly weaker

direct PESC bridge:
  not found
```

## V5 — PACPSA difference stability

```text
status:
  ONLY SURVIVING PARITY-SIDE MECHANISM

current theorem:
  no coupled difference-error estimate
```

---

# 19. Campaign 31 verdict

The parity branch has now been reaudited using all later residual and short-interval information.

The updated closure diagram is:

```text
PESC positivity lifts
    |
    v
FI parity bilinear
    |
    v
EMBF
    |
Lambda-sharp subtraction
    |
    v
residual-weight EMBF
    |
    +--> Abel externalization -> residual f-blocks
    |                         -> multiplicative-grid debt
    |
    +--> remove outer abs -> loses dual sign uniformity
    |
    v
PACPSA difference stability
```

No lower-strength fixed-power theorem is obtained.

---

# 20. New certified package

Create:

```text
B-RH-007
SIEVE_RESIDUAL_EMBF_EQUIVALENCE
CERTIFIED

B-RH-008
EMBF_OUTER_ABSOLUTE_DUAL_UNIFORMITY
CERTIFIED

O-RH-069
ABEL_EXTERNALIZATION_RETURNS_PRIME_RESIDUAL
CERTIFIED

O-RH-070
ALMOST_ALL_EXCEPTIONAL_SET_MULTIPLICATIVE_GRID_BLINDNESS
CERTIFIED

O-RH-071
SEPARATE_POSITIVE_LIFT_SIEVE_ERROR_FLOOR
CERTIFIED AS CURRENT-THEOREM AUDIT
```

No new frontier is created.

---

# 21. Canonical status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN

F-RH-012
EMBF
AUXILIARY / RESIDUAL-EQUIVALENT IN FIRST-STRIP RANGE

F-RH-014
PACPSA
OPEN / ONLY SURVIVING PARITY-ASSEMBLY MECHANISM
```

---

# 22. Campaign 32

The next campaign is:

```text
CSM_RH Campaign 32
PACPSA_DIFFERENCE_STABILITY_ATTACK
```

The target is not to improve the ordinary asymptotic sieve.

It is to determine whether the proof can be linearized around the common positive background of the two PESC lifts.

---

# 23. Campaign 32 tracks

## D1 — common-background linearization

Write

$$
a^\pm=a_0\pm h,
$$

with

$$
a_0=M_Nw_N,
\qquad
h=w_NB_\vartheta.
$$

Track every asymptotic-sieve error term under the perturbation parameter $t$ in

$$
a_t=a_0+th.
$$

Seek a derivative bound depending on $h$, not on $a_0$.

## D2 — signed remainder axioms

Linearize the divisor-distribution remainders

$$
r_d(a_t)
$$

and test whether the derivative sequence satisfies a signed analogue of the sieve remainder axioms at a power-accurate norm.

## D3 — bilinear derivative stability

Differentiate the Friedlander–Iwaniec bilinear form before taking the outer absolute value.

Determine whether phase alignment can be controlled uniformly in $t$.

## D4 — Jordan / polarization formulation

Seek a theorem for signed perturbations by polarization of the nonnegative asymptotic sieve.

Reject the route if total variation of the perturbation remains $N^{3-o(1)}$.

## D5 — difference-level prime-detection functional

Work directly with

$$
\mathfrak E(a^+)-\mathfrak E(a^-)
$$

and derive a sieve identity in which the common positivity background cancels algebraically before all error estimates.

This is the preferred route.

---

# 24. Campaign 32 rejection filters

Reject a candidate if:

## R1. It applies the ordinary asymptotic sieve separately to $a^+$ and $a^-$.

## R2. Its signed norm is total variation of $a^+-a^-$ at $N^{3-o(1)}$ scale.

## R3. It obtains only logarithmic relative error.

## R4. It assumes EMBF/PESC fixed power as an input.

## R5. It drops the outer absolute without replacing the lost dual sign uniformity.

## R6. It claims cancellation between two big- $O$ errors without a joint theorem.

---

# 25. External calibration

Current relevant theorems:

1. The 2026 higher-uniformity theorem gives both $\mu$ and $\Lambda-\Lambda^\sharp$ logarithmic discorrelation on almost all intervals of length at least $X^{1/3+\varepsilon}$, with logarithmically small exceptional sets.

2. The Friedlander–Iwaniec asymptotic sieve is explicitly formulated for nonnegative sequences, and its prime-detection output has relative error $\log\delta/\log\Delta$, which is $\log\log x/\log x$ in the practical parameter regime.

These facts explain why modern local uniformity and classical parity breaking still do not supply a power-accurate coupled difference theorem.

---

# 26. State transition

```text
CSM_RH v1.22
  ->
CSM_RH v1.23
```

with:

```text
Campaign 31
  CLOSED_AS_ENDOGENOUS_PARITY_BILINEAR_REAUDIT

B-RH-007
  SIEVE_RESIDUAL_EMBF_EQUIVALENCE
  CREATED / CERTIFIED

B-RH-008
  EMBF_OUTER_ABSOLUTE_DUAL_UNIFORMITY
  CREATED / CERTIFIED

O-RH-069
  ABEL_EXTERNALIZATION_RETURNS_PRIME_RESIDUAL
  CREATED / CERTIFIED

O-RH-070
  ALMOST_ALL_EXCEPTIONAL_SET_MULTIPLICATIVE_GRID_BLINDNESS
  CREATED / CERTIFIED

O-RH-071
  SEPARATE_POSITIVE_LIFT_SIEVE_ERROR_FLOOR
  CREATED / CERTIFIED AS CURRENT-THEOREM AUDIT

F-RH-014
  PACPSA
  REMAINS OPEN / ONLY SURVIVING PARITY-ASSEMBLY MECHANISM

Campaign 32
  PACPSA_DIFFERENCE_STABILITY_ATTACK
  READY
```

---

# 27. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

EMBF = FIRST-STRIP EQUIVALENT AFTER RESIDUAL WEIGHT SUBSTITUTION

MOBIUS SHORT-INTERVAL UNIFORMITY = STRONG BUT NOT ENDOGENOUS-GRID STABLE

OUTER ABSOLUTE = ESSENTIAL DUAL SIGN UNIFORMITY IN FI AXIOM

SEPARATE POSITIVE-LIFT ASYMPTOTIC SIEVE = N^(3-o(1)) ERROR FLOOR

PACPSA DIFFERENCE STABILITY = ONLY SURVIVING PARITY MECHANISM

NEXT CAMPAIGN = 32
```

The principal new bridge is

$$
\boxed{
\mathfrak B_{N,L,C}[B_\vartheta]
=
\mathfrak B_{N,L,C}[F]
+
O
\left(
N^{5/2+o(1)}
\right)
}
$$

at seminorm-distance level.

The principal remaining question is no longer whether parity can be broken.

It is whether the asymptotic-sieve error can be made stable under the signed endogenous perturbation before the common positive background is charged.
