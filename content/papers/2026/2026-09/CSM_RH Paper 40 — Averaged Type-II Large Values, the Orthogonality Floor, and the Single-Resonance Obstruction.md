# CSM_RH Paper 40
## Averaged Type-II Large Values, the Orthogonality Floor, and the Single-Resonance Obstruction

**Project:** `CSM_RH`  
**Paper:** `40`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.30 / Paper 39`  
**Campaign:** `39 — AVERAGED_TYPEII_POLYNOMIAL_W_ATTACK`  
**Status:** averaged large-value replacement audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 39 proved that the current pointwise route to polynomial $W$ is fixed-strip locked.

Campaign 39 asks whether modern Dirichlet-polynomial large-value estimates can replace the pointwise hypothesis in the Type-II amplifier.

The result is negative at the generic bounded-coefficient level.

The Guth–Maynard theorem improves the nontrivial large-value terms, but retains the classical orthogonality term

$$
N^2V^{-2}.
$$

After normalization to the 1-line, this becomes a $P^{-2}$ level-set floor.

That floor yields at best logarithmic control after layer-cake integration and cannot generate a vanishing fixed power.

More decisively, the divisor-bounded coefficient class of Lemma 3.5 contains explicit phase-aligned examples with a single constant-size resonant frequency. Such one-frequency resonance already forces an $O(1)$ contribution to the product mean square, whereas polynomial $W$ requires that mean square to tend to zero like a fixed power.

Therefore generic large-value technology cannot replace the arithmetic pointwise/nonresonance input.

A genuinely arithmetic simultaneous-resonance exclusion for the actual Heath–Brown factors remains open.

No live GLM-5.3-Flash run is claimed.

---

# 1. Type-II integrated target

Recall

$$
A(s)
=
\sum_{m\sim M}
a(m)m^{-s},
$$

and

$$
B(s)
=
\sum_{N/3<n\le3N}
b(n)n^{-s},
$$

where

$$
MN\asymp X.
$$

The Type-II proof reduces to estimates such as

$$
\boxed{
\int_{W\le|t|\le T}
|A(1+it)B(1+it)|^2
\,dt
\ll
\frac{TH}{X}
\frac{\log^{O(1)}X}{W^{3/10}}
}
$$

or the stronger sufficient estimate

$$
\boxed{
\int_{W\le|t|\le X^{2/3}}
|A(1+it)B(1+it)|^2
\,dt
\ll
\frac{\log^{O(1)}X}{W^{3/10}}.
}
$$

When

$$
W=X^w,
\qquad
w>0,
$$

the right side is

$$
X^{-3w/10+o(1)}.
$$

Thus the desired integrated product must itself vanish at a fixed polynomial rate.

---

# 2. Product polynomial normalization

Write

$$
F(s)=A(s)B(s).
$$

After partitioning its support into $O(1)$ dyadic blocks, one obtains a length- $\asymp X$ polynomial

$$
F(1+it)
=
\frac1X
D_F(t)
\cdot
X^{o(1)},
$$

where

$$
D_F(t)
=
\sum_{\ell\asymp X}
c_\ell
\ell^{-it}
$$

and

$$
|c_\ell|
\le
d_2(\ell)^{O(1)}
=
X^{o(1)}.
$$

After division by an $X^{o(1)}$ factor, Guth–Maynard's bounded-coefficient large-value theorem applies at exponent resolution.

---

# 3. Guth–Maynard large-value theorem

For a length- $L$ Dirichlet polynomial

$$
D(t)
=
\sum_{L<n\le2L}
b_n n^{it},
\qquad
|b_n|\le1,
$$

suppose that at $R$ one-separated points

$$
|D(t_r)|\ge V.
$$

Guth–Maynard prove

$$
\boxed{
R
\le
T^{o(1)}
\left(
L^2V^{-2}
+
L^{18/5}V^{-4}
+
TL^{12/5}V^{-4}
\right).
}
$$

The first term is the classical orthogonality term.

The new theorem improves the large-value geometry in the critical intermediate-amplitude region through the remaining terms.

---

# 4. Normalized product level sets

For the product polynomial, set

$$
L=X.
$$

A normalized threshold

$$
|F(1+it)|\ge P
$$

corresponds, up to $X^{o(1)}$, to

$$
V=XP.
$$

Therefore the Guth–Maynard estimate becomes

## Theorem 4.1 — Product Large-Value Ledger

$$
\boxed{
R_F(P)
\ll
X^{o(1)}
\left(
P^{-2}
+
X^{-2/5}P^{-4}
+
TX^{-8/5}P^{-4}
\right).
}
$$

For the Type-II range

$$
T\le X^{2/3},
$$

the last term is at most

$$
X^{-14/15}P^{-4}.
$$

Hence the persistent first term is

$$
\boxed{
R_F(P)
\ll
X^{o(1)}P^{-2}
+\text{smaller large-value terms}.
}
$$

Create:

```text
B-RH-015
GUTH_MAYNARD_PRODUCT_LEVEL_SET_NORMALIZATION
status:
  CERTIFIED
```

---

# 5. Orthogonality floor

The term

$$
P^{-2}
$$

is scale invariant for the $L^2$ layer cake.

Indeed, schematically,

$$
\int
|F(1+it)|^2dt
=
2
\int_0^\infty
P
\operatorname{meas}
\{
|F|>P
\}
\,dP.
$$

If the available general level-set estimate has the form

$$
\operatorname{meas}
\{
|F|>P
\}
\ll
X^{o(1)}P^{-2},
$$

then its contribution to the layer cake is

$$
\boxed{
X^{o(1)}
\int
\frac{dP}{P}.
}
$$

This is logarithmic / subpower.

It is not

$$
X^{-cw}
$$

for any fixed $c,w>0$.

Create:

```text
O-RH-096
GENERIC_LARGE_VALUE_ORTHOGONALITY_FLOOR
status:
  CERTIFIED
```

Statement:

> A generic Dirichlet-polynomial large-value theorem whose leading normalized term is $P^{-2}$ cannot by itself imply the polynomially vanishing Type-II product mean square required for polynomial $W$.

---

# 6. Sharpness of the first large-value term

Guth–Maynard discuss general bounded-coefficient constructions with

$$
\gg
L^{2-2\sigma}
$$

one-separated points at amplitude

$$
L^\sigma.
$$

This is precisely the scale represented by

$$
L^2V^{-2}.
$$

Thus the orthogonality term is not merely an artifact of their proof.

It reflects a real generic bounded-coefficient phenomenon.

Therefore replacing the first term by a fixed-power improvement is impossible without exploiting additional arithmetic structure.

---

# 7. Explicit one-frequency resonance

There is an even simpler obstruction tailored directly to Lemma 3.5.

Fix

$$
t_0
$$

in the relevant integration interval and choose

$$
\boxed{
a(m)=m^{it_0},
\qquad
b(n)=n^{it_0}.
}
$$

These coefficients satisfy

$$
|a(m)|=|b(n)|=1.
$$

Then

$$
A(1+it)
=
\sum_{m\sim M}
\frac{
m^{-i(t-t_0)}
}{m},
$$

and

$$
B(1+it)
=
\sum_{N/3<n\le3N}
\frac{
n^{-i(t-t_0)}
}{n}.
$$

At

$$
t=t_0,
$$

both are positive harmonic sums of constant size.

---

# 8. Fixed-width resonance interval

Let

$$
s=t-t_0.
$$

For $m\in[M,2M]$,

$$
m^{-is}
=
M^{-is}
\left(
\frac mM
\right)^{-is}.
$$

If

$$
|s|
\le
\frac{\pi}{6\log2},
$$

then

$$
\cos
\left(
s\log\frac mM
\right)
\ge
\frac{\sqrt3}{2}.
$$

Hence

$$
\boxed{
|A(1+i(t_0+s))|
\gg1.
}
$$

For $n\in[N/3,3N]$, write

$$
n^{-is}
=
N^{-is}
(n/N)^{-is}.
$$

If

$$
|s|
\le
\frac{\pi}{6\log3},
$$

then

$$
\boxed{
|B(1+i(t_0+s))|
\gg1.
}
$$

Thus on one fixed-width interval around $t_0$,

$$
\boxed{
|A(1+it)B(1+it)|
\gg1.
}
$$

---

# 9. Resonance contradicts a generic polynomial- $W$ integrated theorem

Choose

$$
t_0
$$

so that the fixed-width interval of Section 8 lies inside

$$
W\le|t|\le X^{2/3}.
$$

This is possible whenever

$$
1\ll W\ll X^{2/3}.
$$

Then

## Theorem 9.1 — Single-Resonance Lower Bound

For the legal coefficients of Section 7,

$$
\boxed{
\int_{W\le|t|\le X^{2/3}}
|A(1+it)B(1+it)|^2dt
\gg1.
}
$$

But a polynomial- $W$ Type-II theorem would require

$$
\boxed{
\int
|AB|^2
\ll
W^{-3/10}\log^{O(1)}X
=
X^{-3w/10+o(1)}
\to0.
}
$$

Contradiction.

Create:

```text
O-RH-097
SINGLE_RESONANT_FREQUENCY_OBSTRUCTS_GENERIC_POLYNOMIAL_W_MEAN_SQUARE
status:
  CERTIFIED
```

---

# 10. Consequence for generic averaged replacement

Theorems 4.1 and 9.1 show that no statement of the form

```text
divisor-bounded coefficients
+
generic Dirichlet-polynomial large-value theorem
->
polynomial-W integrated Type-II saving
```

can hold.

The pointwise smallness in Lemma 3.5 is not merely a convenient sufficient condition.

It excludes resonances which are legal in the ambient coefficient class.

---

# 11. Weak pointwise logarithmic control is still insufficient

Suppose one supplements large-value theory by an arbitrary fixed logarithmic pointwise estimate

$$
\boxed{
|A(1+it)|,\,
|B(1+it)|
\le
\log^{-K}X
}
$$

for fixed $K$.

A single peak at the maximal allowed scale contributes only a negative power of $\log X$ to the product mean square.

But

$$
\log^{-C}X
=
X^{-o(1)}
\gg
X^{-cw}.
$$

Thus a finite or subpower number of subpower-sized resonant peaks is still incompatible with the required fixed-power integrated bound.

A fixed-power conclusion requires polynomial control of the total resonance mass, not merely arbitrary fixed log-power peak suppression.

---

# 12. Large-value count quantization

Large-value theorems count one-separated points.

Such a count is an integer.

A bound which says

$$
R\le X^{o(1)}
$$

does not distinguish between:

```text
no resonance;
one resonance;
a subpower number of resonances.
```

But the polynomially vanishing Type-II target is sensitive even to one sufficiently broad subpower-amplitude resonance.

Create:

```text
O-RH-098
LARGE_VALUE_COUNT_QUANTIZATION_BARRIER
status:
  CERTIFIED AS FIXED-POWER TRANSFERENCE AUDIT
```

This is another formulation of why improving the number of large values is not enough when the target integral itself must tend to zero polynomially.

---

# 13. Applying Guth–Maynard separately to the two factors

One might attempt to control simultaneous large values through

$$
\min
\{
R_A(U),R_B(V)
\}.
$$

For the normalized factor $A$, the first Guth–Maynard term gives

$$
\boxed{
R_A(U)
\ll
X^{o(1)}U^{-2}
+\cdots
}
$$

and likewise

$$
\boxed{
R_B(V)
\ll
X^{o(1)}V^{-2}
+\cdots.
}
$$

The same orthogonality floor remains.

Moreover the phase-aligned example makes the two resonances occur at the same $t_0$.

Thus independent large-value estimates do not solve simultaneous resonance.

---

# 14. Applying the theorem to the product

Treating

$$
F=AB
$$

as one Dirichlet polynomial improves bookkeeping but not the exponent class.

The first term becomes

$$
P^{-2}
$$

and the one-frequency example still survives.

Therefore neither:

```text
factorwise large-value control
```

nor

```text
product large-value control
```

gives the required polynomial mean-square saving generically.

---

# 15. Why Guth–Maynard still matters

This negative conclusion does not diminish the Guth–Maynard theorem.

Their improvement in the critical regime near amplitude

$$
V=L^{3/4}
$$

is strong enough to improve zero-density estimates and prime short-interval ranges.

It is simply a different quantitative task.

The current CSM_RH Type-II target asks for an integrated quantity which tends to zero by a fixed power.

That requires arithmetic cancellation beyond the generic bounded-coefficient orthogonality floor.

---

# 16. Actual Heath–Brown factors are not generic

The obstruction above applies to the ambient divisor-bounded coefficient class.

The Type-II factors arising from the actual decomposition of $\Lambda$ and $\mu$ have additional structure.

Heath–Brown's identity writes the relevant components as convolutions of factors which are:

```text
1 on a dyadic block;
log n on a dyadic block;
mu(n) on a short dyadic block.
```

In particular, Möbius-bearing factors occur on scales at most a small fixed power of $X$ in the chosen identity.

Therefore the generic resonance example does not prove that the actual arithmetic factors possess such resonances.

It only proves that general large-value theory cannot rule them out.

---

# 17. New surviving arithmetic question

The remaining route is:

> prove that the actual Möbius-bearing Heath–Brown factors and their complementary factors cannot be simultaneously resonant on a set with enough spectral mass to defeat polynomial $W$.

This is stronger than generic large-value theory and weaker in form than demanding pointwise fixed-power Mertens for the full Möbius polynomial.

Whether it is genuinely lower-strength is open.

No theorem is claimed here.

---

# 18. Campaign 39 track audit

## AV1 — large-value replacement of pointwise input

```text
status:
  FAILS GENERICALLY

reason:
  P^(-2) orthogonality floor
```

## AV2 — Guth–Maynard large-value technology

```text
status:
  IMPROVES CRITICAL LARGE-VALUE TERMS

does not remove:
  orthogonality floor
```

## AV3 — low-frequency excision

```text
status:
  DOES NOT FIX GENERIC RESONANCE

resonance can be placed at any legal t0 > W
```

## AV4 — product large-value geometry

```text
status:
  GENERIC PRODUCT THEOREM STILL HAS P^(-2) FLOOR

single simultaneous resonance:
  legal
```

## AV5 — polynomial-W integrated bridge

```text
status:
  NOT OBTAINED GENERICALLY

requires:
  arithmetic resonance exclusion
```

---

# 19. Campaign 39 verdict

No polynomial- $W$ integrated theorem is proved.

The campaign closes the purely generic averaged escape:

```text
pointwise fixed-power input:
  too strong / fixed-strip locked

generic averaged large values:
  too weak / resonance floor

remaining possibility:
  arithmetic simultaneous-resonance exclusion
```

The component bridge B-RH-014 remains valid.

---

# 20. New certified package

Create:

```text
B-RH-015
GUTH_MAYNARD_PRODUCT_LEVEL_SET_NORMALIZATION
CERTIFIED

O-RH-096
GENERIC_LARGE_VALUE_ORTHOGONALITY_FLOOR
CERTIFIED

O-RH-097
SINGLE_RESONANT_FREQUENCY_OBSTRUCTS_GENERIC_POLYNOMIAL_W_MEAN_SQUARE
CERTIFIED

O-RH-098
LARGE_VALUE_COUNT_QUANTIZATION_BARRIER
CERTIFIED
```

No new canonical frontier is created.

---

# 21. Canonical root status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN / DIRECT THEOREM CANDIDATE

B-RH-014
POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
CERTIFIED COMPONENT BRIDGE

generic large-value replacement:
  CLOSED
```

---

# 22. Campaign 40

The next campaign is:

```text
CSM_RH Campaign 40
HEATH_BROWN_ARITHMETIC_RESONANCE_EXCLUSION
```

This is a genuinely arithmetic campaign.

No generic bounded-coefficient theorem is admissible as the main step.

---

# 23. Campaign 40 tracks

## HB1 — Möbius carrier audit

For every Type-II component arising from the chosen Heath–Brown identity for $\Lambda-\Lambda^\sharp$, identify which grouped factor contains a Möbius-bearing short variable.

Determine whether at least one factor always retains explicit Möbius structure after grouping.

## HB2 — translated-frequency Möbius large values

The large- $T$ major-arc application twists the factors by $n^{iT}$.

Study the actual frequency window seen by each Möbius factor and whether its short length relative to $|T|$ permits fixed-power averaged cancellation without a global Mertens theorem.

## HB3 — simultaneous resonance exclusion

Define the set where both Type-II factors are larger than polynomial thresholds.

Seek a bound on the spectral measure of the simultaneous-large set stronger than the generic $P^{-2}$ floor.

## HB4 — short Möbius factor versus complementary factor

Exploit that Möbius factors in the fixed Heath–Brown identity have length at most a small power of $X$.

Test whether large values of such a factor force a complementary factor into a regime controlled by mean-value or large-value estimates.

## HB5 — integrated polynomial- $W$ admission

The only accepted output is the exact integrated estimate needed by Lemma 3.5 with

$$
W=X^w
$$

for some fixed $w>0$.

If obtained, invoke B-RH-014.

---

# 24. Campaign 40 rejection filters

Reject a candidate if:

## R1. It treats the actual factors as arbitrary divisor-bounded coefficients.

## R2. It assumes pointwise fixed-power Mertens.

## R3. It assumes a fixed zero-free strip.

## R4. It only reduces the number of resonant frequencies to $X^{o(1)}$.

## R5. It obtains only logarithmic total resonance mass.

## R6. It ignores an allowed Heath–Brown component with no certified Möbius carrier.

---

# 25. External calibration

The current audit uses:

1. Matomäki–Radziwiłł–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals II*, Lemmas 3.4 and 3.5. The Type-II product mean square is proved using a Baker–Harman–Pintz parallelogram lemma plus pointwise smallness of one factor.

2. Guth–Maynard, *New large value estimates for Dirichlet polynomials*, Theorem 1.1:
   $$
   R
   \le
   T^{o(1)}
   \left(
   N^2V^{-2}
   +
   N^{18/5}V^{-4}
   +
   TN^{12/5}V^{-4}
   \right).
   $$
   The first term is the generic orthogonality floor.

3. The higher-uniformity paper's Heath–Brown decomposition expresses $\Lambda$ components using dyadic factors of type $1$, $\log$, and short $\mu$.

The next campaign uses the third item as arithmetic structure rather than discarding it into the generic divisor-bounded class.

---

# 26. State transition

```text
CSM_RH v1.30
  ->
CSM_RH v1.31
```

with:

```text
Campaign 39
  CLOSED_AS_GENERIC_AVERAGED_TYPEII_LARGE_VALUE_AUDIT

B-RH-015
  GUTH_MAYNARD_PRODUCT_LEVEL_SET_NORMALIZATION
  CREATED / CERTIFIED

O-RH-096
  GENERIC_LARGE_VALUE_ORTHOGONALITY_FLOOR
  CREATED / CERTIFIED

O-RH-097
  SINGLE_RESONANT_FREQUENCY_OBSTRUCTS_GENERIC_POLYNOMIAL_W_MEAN_SQUARE
  CREATED / CERTIFIED

O-RH-098
  LARGE_VALUE_COUNT_QUANTIZATION_BARRIER
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 40
  HEATH_BROWN_ARITHMETIC_RESONANCE_EXCLUSION
  READY
```

---

# 27. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

POLYNOMIAL-W TYPE-II AMPLIFIER = VALID

POINTWISE POLYNOMIAL-W INPUT = FIXED-STRIP LOCKED

GENERIC AVERAGED LARGE-VALUE REPLACEMENT = CLOSED

GUTH-MAYNARD IMPROVEMENT = REAL BUT RETAINS ORTHOGONALITY FLOOR

SINGLE GENERIC RESONANCE = ENOUGH TO KILL VANISHING PRODUCT MEAN SQUARE

ARITHMETIC HEATH-BROWN RESONANCE EXCLUSION = OPEN

NEXT CAMPAIGN = 40
```

The decisive generic obstruction is

$$
\boxed{
R_F(P)
\ll
X^{o(1)}
\left(
P^{-2}
+\cdots
\right),
}
$$

together with the legal phase-aligned example

$$
\boxed{
a(m)=m^{it_0},
\qquad
b(n)=n^{it_0},
}
$$

for which

$$
\boxed{
\int
|A(1+it)B(1+it)|^2dt
\gg1.
}
$$

The breakthrough route, if it exists, must use the arithmetic identity of the actual prime factors rather than generic large-value geometry.
