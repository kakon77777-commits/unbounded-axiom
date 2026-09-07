# CSM_RH Paper 41
## Heath–Brown Carrier Audit and the Pure-Möbius Type-II Core

**Project:** `CSM_RH`  
**Paper:** `41`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.31 / Paper 40`  
**Campaign:** `40 — HEATH_BROWN_ARITHMETIC_RESONANCE_EXCLUSION`  
**Status:** arithmetic-factor carrier audit / pure-Möbius-core localization; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 40 proved that generic divisor-bounded large-value technology cannot supply the polynomial- $W$ Type-II mean-square saving.

Campaign 40 asks whether the actual Heath–Brown factors of the von Mangoldt function contain enough arithmetic structure to exclude the generic resonance.

The campaign reaches a structural localization rather than a fixed-power theorem.

Two opposite legal Type-II families occur inside the same Heath–Brown identity:

1. carrier-free smooth Type-II components;
2. pure-Möbius-core Type-II components with no polynomial-scale smooth complementary factor.

Thus there is no universal proof rule of the form

```text
every Lambda Type-II component
  ->
one nontrivial Mobius carrier
plus one smooth complementary anti-resonant factor.
```

The remaining hard arithmetic family is the high-frequency simultaneous resonance of several short Möbius Dirichlet polynomials.

No live GLM-5.3-Flash run is claimed.

---

# 1. Heath–Brown identity

Fix an integer

$$
L\ge1
$$

and set

$$
z=(2X)^{1/L}.
$$

The Heath–Brown identity used in the higher-uniformity papers has the form

$$
\boxed{
\Lambda(n)
=
\sum_{1\le j\le L}
(-1)^{j-1}
\binom Lj
\sum_{m_1,\ldots,m_j\le z}
\mu(m_1)\cdots\mu(m_j)
\sum_{\substack{
m_1\cdots m_j
n_1\cdots n_j=n
}}
\log n_1.
}
$$

After dyadic subdivision, every component is a convolution

$$
\boxed{
f
=
a^{(1)}*\cdots*a^{(\ell)},
\qquad
\ell\le2L,
}
$$

where each factor is a dyadic restriction of one of

$$
1,
\qquad
\log,
\qquad
\mu.
$$

Every Möbius factor has dyadic length

$$
\boxed{
N_{\mu}
\ll
X^{1/L}.
}
$$

In the 2026 decomposition one takes

$$
L=\left\lceil\frac{10}{\varepsilon}\right\rceil,
$$

so

$$
\boxed{
N_\mu
\le
X^{\varepsilon/10}
}
$$

at exponent resolution.

---

# 2. Type-II grouping in the 2026 proof

Order the dyadic lengths by

$$
N_1\ge N_2\ge\cdots\ge N_\ell.
$$

After excluding the Type-I and Type- $I_2$ cases, the proof has

$$
N_1N_2
\le
X^{1-\varepsilon/2}.
$$

It then chooses an index $j_\ast\ge3$ such that

$$
\boxed{
X^{\varepsilon/10}
\le
N_3\cdots N_{j_\ast}
\ll
X^{1/3},
}
$$

and defines

$$
\boxed{
\alpha
=
a^{(3)}*\cdots*a^{(j_\ast)},
}
$$

with all remaining factors placed in the complementary Type-II coefficient $\beta$.

The grouping rule is based on support lengths.

It does not preserve an arithmetic label saying that $\alpha$ or $\beta$ must contain a nontrivial Möbius block.

---

# 3. Carrier-free smooth Type-II component

Take the $j=3$ term in Heath–Brown's identity.

Restrict all Möbius variables to

$$
m_1=m_2=m_3=1.
$$

Then

$$
\mu(m_1)\mu(m_2)\mu(m_3)=1.
$$

Choose the three smooth variables on dyadic scales

$$
n_1,n_2,n_3
\asymp
X^{1/3},
$$

with $n_1$ carrying the logarithm.

The resulting nonzero component is, up to dyadic endpoint restrictions,

$$
\boxed{
(\log 1_{X^{1/3}})
*
1_{X^{1/3}}
*
1_{X^{1/3}}.
}
$$

All Möbius factors are convolution identities supported at $1$.

For small fixed $\varepsilon$:

$$
N_1
\asymp
N_2
\asymp
N_3
\asymp
X^{1/3},
$$

so

$$
N_1
<
X^{2/3-\varepsilon/2},
$$

and

$$
N_1N_2
\asymp
X^{2/3}
<
X^{1-\varepsilon/2}.
$$

Thus this lies in the Type-II branch of the 2026 grouping.

Create:

```text
O-RH-099
HEATH_BROWN_TYPEII_NOT_UNIFORMLY_MOBIUS_CARRYING
status:
  CERTIFIED
```

A proof strategy which requires every Type-II component to retain a nontrivial Möbius carrier is therefore invalid.

---

# 4. Carrier-free does not mean hard by itself

The component in Section 3 is divisor-like.

Its difficulty is qualitatively different from the Möbius-bearing prime residual.

The 2026 major-arc theory obtains genuine polynomial $W$ for divisor-function Type-II problems.

Thus carrier-free smooth components are not evidence that the fixed-power route fails.

They show only that the arithmetic proof must branch according to the actual factor content.

No universal Möbius-carrier argument can cover every component.

---

# 5. Pure-Möbius Type-II core

The opposite extreme also occurs.

Take the $j=L$ term in Heath–Brown's identity.

Choose:

$$
n_1=2,
$$

so the logarithmic factor contributes the nonzero constant

$$
\log2,
$$

and choose

$$
n_2=\cdots=n_L=1.
$$

The product constraint is then carried almost entirely by the Möbius variables:

$$
m_1\cdots m_L
\asymp
X/2.
$$

Choose all $m_i$ on comparable dyadic scales

$$
\boxed{
m_i
\asymp
(X/2)^{1/L}.
}
$$

These scales are legal because

$$
(X/2)^{1/L}
\le
(2X)^{1/L}=z.
$$

After removing the constant smooth factors, the component is essentially

$$
\boxed{
(\mu_{M_1}*\cdots*\mu_{M_L})
\times\log2.
}
$$

---

# 6. It is genuinely Type II

Set

$$
\lambda=\frac1L.
$$

The largest nontrivial factors have scale

$$
X^\lambda.
$$

Since

$$
L=\left\lceil\frac{10}{\varepsilon}\right\rceil,
$$

we have

$$
\lambda
\le
\frac{\varepsilon}{10}.
$$

Therefore:

$$
X^\lambda
\ll
X^{2/3-\varepsilon/2},
$$

and

$$
X^{2\lambda}
\ll
X^{1-\varepsilon/2}.
$$

Hence the component is not forced into the Type-I or Type- $I_2$ branches.

To form the Type-II factor $\alpha$, the length-grouping algorithm combines enough of the short Möbius blocks that their product first reaches

$$
X^{\varepsilon/10}.
$$

The remaining Type-II factor $\beta$ still contains the other short Möbius blocks.

For $L$ sufficiently large, both sides contain nontrivial Möbius blocks.

Create:

```text
O-RH-100
PURE_MOBIUS_CORE_TYPEII_COMPONENT_EXISTS
status:
  CERTIFIED
```

---

# 7. Failure of the complementary-smooth-factor escape

Paper 40 left open the possibility that a Möbius-bearing factor could be large only when a complementary smooth factor is small.

The pure-Möbius core of Sections 5–6 shows that this cannot be the universal mechanism.

There are legal Type-II components for which the polynomial-scale factors on both sides of the Type-II split are built from Möbius blocks, while the only smooth factors are constants.

Therefore no proof may assume:

```text
Mobius resonance
  ->
independent smooth factor supplies polynomial anti-resonance.
```

Create:

```text
O-RH-101
COMPLEMENTARY_SMOOTH_ANTI_RESONANCE_NOT_UNIVERSAL
status:
  CERTIFIED
```

---

# 8. Dirichlet-polynomial form of the core

For dyadic Möbius blocks define

$$
\boxed{
M_i(s)
=
\sum_{m\sim M_i}
\frac{\mu(m)}{m^s}.
}
$$

The pure core has Dirichlet polynomial, up to a fixed nonzero scalar and harmless dyadic bookkeeping,

$$
\boxed{
F_{\mathrm{core}}(s)
=
\prod_{i=1}^{L}
M_i(s).
}
$$

A Type-II grouping partitions the index set into two nonempty groups:

$$
A_{\mathrm{core}}(s)
=
\prod_{i\in I}
M_i(s),
$$

$$
B_{\mathrm{core}}(s)
=
\prod_{i\notin I}
M_i(s).
$$

Thus simultaneous Type-II resonance becomes a high moment / multi-factor resonance problem for short Möbius Dirichlet polynomials.

---

# 9. Translated high-frequency window

In the large- $T$ major-arc application, the Type-II coefficients are twisted by

$$
n^{iT}.
$$

Consequently a Möbius block appears as

$$
\sum_{m\sim M}
\frac{\mu(m)}{m^{1+i(t-T)}}.
$$

The integration variable $t$ is small relative to the major-arc center $T$ in the relevant parameter regime.

Thus the unresolved object is not the pointwise value at frequency zero.

It is a translated high-frequency window centered near

$$
-T.
$$

This distinction matters because the fixed-power Mertens lock of Paper 39 used the $t=0$ specialization of a pointwise theorem.

Campaign 40 does not prove that high-frequency averaged control is equivalent to fixed-power Mertens.

---

# 10. Why generic mean values still do not solve the core

For one dyadic Möbius block of length $M$,

$$
\sum_{m\sim M}
\frac{|\mu(m)|^2}{m^2}
\asymp
\frac1M
$$

up to arithmetic constants.

The standard Dirichlet-polynomial mean-value theorem therefore gives the same diagonal scale as for generic bounded coefficients.

It does not supply an additional fixed-power suppression purely from the sign pattern of $\mu$.

For the product core, generic mean-value technology again reaches an orthogonality-scale bound rather than the polynomially vanishing $W^{-c}$ target.

Thus arithmetic information beyond the diagonal is required.

---

# 11. No universal carrier-preserving decomposition in the current proof

The current 2026 proof applies the triangle inequality after decomposing $\Lambda$ and then treats each Type-II component separately.

Under this componentwise architecture:

1. smooth-only Type-II components exist;
2. mixed Möbius/smooth Type-II components exist;
3. pure-Möbius-core Type-II components exist.

Hence the proof cannot be reduced to one carrier pattern.

A future proof could reorganize or couple different Heath–Brown $j$ -levels before applying absolute values.

Campaign 40 does not provide such a coupled identity.

---

# 12. Cross- $j$ cancellation remains unaudited

The pure core is one dyadic component of one Heath–Brown $j$ -level.

The exact Heath–Brown identity contains alternating coefficients

$$
(-1)^{j-1}\binom Lj.
$$

It is logically possible that a proof preserving cancellation across several $j$ -levels could suppress the core before Type-II estimation.

The published higher-uniformity argument uses triangle inequalities and does not exploit such cancellation at fixed-power scale.

Therefore:

```text
componentwise pure-Mobius obstruction:
  certified

global cross-j impossibility:
  not claimed
```

---

# 13. Campaign 40 track audit

## HB1 — Möbius carrier audit

```text
status:
  NO UNIVERSAL CARRIER PATTERN

smooth-only components:
  exist

pure-Mobius components:
  exist
```

## HB2 — translated-frequency Möbius large values

```text
status:
  LOCALIZED

frequency:
  high / translated

pointwise t=0 Mertens lock:
  not directly applicable
```

## HB3 — simultaneous resonance exclusion

```text
status:
  NOT PROVED

hard core:
  product of short Mobius Dirichlet polynomials
```

## HB4 — short Möbius factor versus complementary factor

```text
status:
  COMPLEMENTARY SMOOTH FACTOR NOT UNIVERSAL

pure-Mobius core:
  defeats this universal strategy
```

## HB5 — integrated polynomial-W admission

```text
status:
  NOT OBTAINED
```

---

# 14. Campaign 40 verdict

No polynomial- $W$ Type-II theorem is proved.

The positive result is a sharper localization than Paper 40:

$$
\boxed{
\text{generic resonance problem}
\rightsquigarrow
\text{actual high-frequency multi-short-Möbius resonance core}.
}
$$

The divisor-like smooth components and mixed components must be treated separately.

The universal remaining arithmetic obstruction is not a generic divisor-bounded polynomial.

It is the possibility of spectral mass in products of genuine short Möbius Dirichlet polynomials.

---

# 15. New certified package

Create:

```text
O-RH-099
HEATH_BROWN_TYPEII_NOT_UNIFORMLY_MOBIUS_CARRYING
CERTIFIED

O-RH-100
PURE_MOBIUS_CORE_TYPEII_COMPONENT_EXISTS
CERTIFIED

O-RH-101
COMPLEMENTARY_SMOOTH_ANTI_RESONANCE_NOT_UNIVERSAL
CERTIFIED
```

No new canonical frontier is created.

---

# 16. Canonical status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN

B-RH-014
POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
CERTIFIED COMPONENT BRIDGE

generic Type-II resonance:
  closed

actual pure-Mobius high-frequency core:
  open
```

---

# 17. Campaign 41

The next campaign is:

```text
CSM_RH Campaign 41
PURE_MOBIUS_CORE_HIGH_FREQUENCY_ATTACK
```

This is a genuinely arithmetic campaign.

No new representation is allowed.

---

# 18. Campaign 41 tracks

## PM1 — translated-window moment formula

For

$$
M_U(s)
=
\sum_{m\sim U}
\frac{\mu(m)}{m^s},
$$

compute the exact mean-square and higher-moment scale on a translated interval

$$
t\in[T-Y,T+Y].
$$

Separate diagonal, near-diagonal, and genuinely arithmetic off-diagonal terms.

## PM2 — zero-ordinate resonance test

Determine whether a zero

$$
\rho=\beta+i\gamma
$$

with $\beta>1/2$ forces a quantitatively large translated short-Möbius polynomial near

$$
t=\gamma.
$$

No coefficient-isolation claim may be made without proof.

## PM3 — multi-factor simultaneous resonance

For the pure core

$$
\prod_{i=1}^{L}M_{U_i}(1+it),
$$

seek a polynomial bound for the spectral measure of the simultaneous-large set.

The bound must improve the generic orthogonality floor.

## PM4 — high-frequency versus zero-frequency separation

Test whether excluding a neighborhood of $t=0$ genuinely weakens the arithmetic statement below fixed-power Mertens strength.

This is the central strength question.

## PM5 — polynomial- $W$ admission

The only accepted output is an integrated bound strong enough to invoke B-RH-014 for the pure-Möbius core and all mixed components.

---

# 19. Campaign 41 rejection filters

Reject a candidate if:

## R1. It replaces the translated window by a theorem uniform down to $t=0$ and thereby imports fixed-power Mertens.

## R2. It uses generic divisor-bounded large values only.

## R3. It controls only one Möbius block while repeated blocks can resonate together.

## R4. It obtains only $X^{-o(1)}$ suppression.

## R5. It assumes zero repulsion or a fixed zero-free strip.

## R6. It ignores cross- $j$ cancellation as a logically possible alternative and claims universal impossibility.

---

# 20. External calibration

The structural facts used in this audit are explicit in the current higher-uniformity papers.

1. The Heath–Brown identity for $\Lambda$ contains $j$ Möbius variables and $j$ smooth variables at level $j$.

2. After dyadic subdivision, every Möbius factor has length at most $X^{1/L}$.

3. The 2026 Type-II grouping in Lemma 4.4 is selected by support lengths and forms
   $$
   \alpha=a^{(3)}*\cdots*a^{(j_\ast)}.
   $$
   No arithmetic carrier condition is imposed.

4. The proof of the major-arc theorem then applies the Type-II estimate componentwise after triangle inequalities.

These facts permit both the smooth-only and pure-Möbius Type-II examples constructed above.

---

# 21. State transition

```text
CSM_RH v1.31
  ->
CSM_RH v1.32
```

with:

```text
Campaign 40
  CLOSED_AS_HEATH_BROWN_CARRIER_AND_PURE_MOBIUS_CORE_AUDIT

O-RH-099
  HEATH_BROWN_TYPEII_NOT_UNIFORMLY_MOBIUS_CARRYING
  CREATED / CERTIFIED

O-RH-100
  PURE_MOBIUS_CORE_TYPEII_COMPONENT_EXISTS
  CREATED / CERTIFIED

O-RH-101
  COMPLEMENTARY_SMOOTH_ANTI_RESONANCE_NOT_UNIVERSAL
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 41
  PURE_MOBIUS_CORE_HIGH_FREQUENCY_ATTACK
  READY
```

---

# 22. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

GENERIC TYPE-II LARGE-VALUE ESCAPE = CLOSED

UNIVERSAL MOBIUS-CARRIER PATTERN = FALSE

UNIVERSAL COMPLEMENTARY SMOOTH ANTI-RESONANCE = FALSE

PURE-MOBIUS TYPE-II CORE = EXISTS

HIGH-FREQUENCY MULTI-SHORT-MOBIUS RESONANCE = OPEN

POLYNOMIAL-W TYPE-II ADMISSION = NOT OBTAINED

NEXT CAMPAIGN = 41
```

The critical structural countercomponent is:

$$
\boxed{
n_1=2,\quad
n_2=\cdots=n_L=1,\quad
m_i\asymp(X/2)^{1/L}.
}
$$

It leaves a legal Type-II component whose nontrivial factors are almost entirely Möbius blocks.

The next fixed-power question is therefore genuinely about the high-frequency spectral behavior of short Möbius Dirichlet polynomials.
