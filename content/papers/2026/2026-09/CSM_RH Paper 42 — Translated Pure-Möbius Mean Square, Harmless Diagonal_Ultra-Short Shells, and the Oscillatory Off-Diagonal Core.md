# CSM_RH Paper 42
## Translated Pure-Möbius Mean Square, Harmless Diagonal/Ultra-Short Shells, and the Oscillatory Off-Diagonal Core

**Project:** `CSM_RH`  
**Paper:** `42`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.32 / Paper 41`  
**Campaign:** `41 — PURE_MOBIUS_CORE_HIGH_FREQUENCY_ATTACK`  
**Status:** translated-window arithmetic localization; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 41 isolated a legal Type-II pure-Möbius core in the Heath–Brown decomposition.

Campaign 41 asks whether translated high-frequency mean squares of that core can produce the polynomial- $W$ saving required by the Type-II amplifier without importing pointwise fixed-power Mertens.

The campaign does not prove such a saving.

It does, however, localize the difficulty sharply:

1. the diagonal of the translated mean square is already polynomially harmless;
2. the ultra-short shift shell is harmless by the separation between the high-frequency center and the local Parseval window;
3. the remaining obstruction is an oscillatory off-diagonal shifted-correlation problem for the balanced Möbius-convolution coefficients;
4. current Chowla-type technology does not provide the required fixed $X$ -power for this object;
5. no standard zero-detection theorem forces one individual dyadic short Möbius block to be large at every off-line zero ordinate.

Thus the high-frequency route is neither solved nor reduced to the pointwise Mertens lock.

No live GLM-5.3-Flash run is claimed.

---

# 1. Pure-Möbius core coefficient

Let

$$
M_i(s)
=
\sum_{m\sim U_i}
\frac{\mu(m)}{m^s},
\qquad
1\le i\le L,
$$

where

$$
\prod_{i=1}^{L}U_i\asymp X.
$$

Define

$$
\boxed{
F_X(s)
=
\prod_{i=1}^{L}M_i(s)
=
\sum_{\ell\asymp X}
\frac{c_X(\ell)}{\ell^s}.
}
$$

The coefficient is the restricted balanced Möbius convolution

$$
\boxed{
c_X(\ell)
=
\sum_{\substack{
m_1\cdots m_L=\ell\\
m_i\sim U_i
}}
\mu(m_1)\cdots\mu(m_L).
}
$$

For fixed $L$,

$$
\boxed{
|c_X(\ell)|
\le
d_L(\ell).
}
$$

Hence

$$
\boxed{
\sum_{\ell\asymp X}
|c_X(\ell)|^2
\ll_L
X(\log X)^{O_L(1)}.
}
$$

---

# 2. The actual translated window

In the large-major-arc application, the Heath–Brown factors are twisted by a major-arc frequency.

Let the absolute center frequency be

$$
Q>0.
$$

Let the local Parseval half-width be

$$
Y.
$$

The large- $T$ branch supplies

$$
\boxed{
Q
\gtrsim
\frac{X}{H}
X^{\varepsilon/2}.
}
$$

Inside the proof of Lemma 3.5, after the reduction corresponding to equation (3.11), it is enough to consider

$$
\boxed{
Y
\lesssim
\frac{X}{H}
W^{3/10}.
}
$$

For polynomial

$$
W=X^w,
$$

with

$$
0<w\le\frac{\varepsilon}{1000},
$$

we therefore have

$$
\boxed{
\frac{Y}{Q}
\ll
X^{3w/10-\varepsilon/2}.
}
$$

The translated window is strongly separated from frequency zero.

---

# 3. Gaussian majorant

Define

$$
\boxed{
\Phi(u)
=
\exp
\left(
\frac{1-u^2}{2}
\right).
}
$$

Then

$$
\Phi(u)\ge1
$$

for

$$
|u|\le1.
$$

Its Fourier transform, with convention

$$
\widehat\Phi(\xi)
=
\int_{\mathbb R}
\Phi(u)e^{-iu\xi}
\,du,
$$

is

$$
\boxed{
\widehat\Phi(\xi)
=
e^{1/2}
\sqrt{2\pi}
e^{-\xi^2/2}.
}
$$

Thus the sharp-window mean square is bounded by the smooth mean square

$$
\boxed{
\int_{Q-Y}^{Q+Y}
|F_X(1+it)|^2dt
\le
\mathcal I_\Phi(Q,Y),
}
$$

where

$$
\boxed{
\mathcal I_\Phi(Q,Y)
=
\int_{\mathbb R}
\Phi
\left(
\frac{t-Q}{Y}
\right)
|F_X(1+it)|^2
\,dt.
}
$$

---

# 4. Exact translated-window kernel identity

Expanding the square and evaluating the Fourier integral gives:

## Theorem 4.1 — Gaussian Translated Mean-Square Identity

$$
\boxed{
\mathcal I_\Phi(Q,Y)
=
Y
\sum_{m,n}
\frac{
c_X(m)\overline{c_X(n)}
}{
mn
}
e^{-iQ\log(m/n)}
\widehat\Phi
\left(
Y\log(m/n)
\right).
}
$$

The diagonal is

$$
\boxed{
\mathcal D_\Phi(Y)
=
Y\widehat\Phi(0)
\sum_n
\frac{
|c_X(n)|^2
}{
n^2
}.
}
$$

The off-diagonal is

$$
\boxed{
\mathcal O_\Phi(Q,Y)
=
Y
\sum_{m\ne n}
\frac{
c_X(m)\overline{c_X(n)}
}{
mn
}
e^{-iQ\log(m/n)}
\widehat\Phi
\left(
Y\log(m/n)
\right).
}
$$

Create:

```text
B-RH-016
TRANSLATED_PURE_CORE_MEAN_SQUARE_IDENTITY
status:
  CERTIFIED
```

---

# 5. Diagonal scale

Since

$$
n\asymp X
$$

on the support and

$$
\sum|c_X(n)|^2
\ll
X(\log X)^{O_L(1)},
$$

we obtain

## Theorem 5.1 — Pure-Core Diagonal Bound

$$
\boxed{
\mathcal D_\Phi(Y)
\ll
\frac{Y}{X}
(\log X)^{O_L(1)}.
}
$$

Using

$$
Y
\lesssim
\frac{X}{H}
W^{3/10},
$$

this becomes

$$
\boxed{
\mathcal D_\Phi(Y)
\ll
\frac{
W^{3/10}
}{
H
}
X^{o(1)}.
}
$$

For

$$
H\ge X^{1/3+\varepsilon}
$$

and

$$
W=X^w,
\qquad
w\le\frac{\varepsilon}{1000},
$$

the diagonal is far below the required Type-II scale

$$
W^{-3/10}.
$$

Create:

```text
O-RH-102
PURE_MOBIUS_CORE_DIAGONAL_HARMLESS
status:
  CERTIFIED
```

The diagonal is not the fixed-power obstruction.

---

# 6. Shift form of the off-diagonal

Write

$$
n=m+h.
$$

Then

$$
\boxed{
\mathcal O_\Phi(Q,Y)
=
2Y
\Re
\sum_{h\ge1}
\sum_m
\frac{
c_X(m)\overline{c_X(m+h)}
}{
m(m+h)
}
e^{iQ\log(1+h/m)}
\widehat\Phi
\left(
Y\log(1+h/m)
\right),
}
$$

with the support restrictions implicit.

Thus the hard object is an additively shifted correlation of the restricted Möbius-convolution coefficient, twisted by a multiplicative high-frequency phase.

---

# 7. Gaussian localization in shift

For

$$
m\asymp X
$$

and

$$
h=o(X),
$$

$$
\log(1+h/m)
\asymp
h/X.
$$

Because

$$
\widehat\Phi(\xi)
=
O_A((1+|\xi|)^{-A})
$$

for every fixed $A>0$,

the contribution from

$$
h
\ge
X^{o(1)}
\frac{X}{Y}
$$

is negligible after taking the $X^{o(1)}$ divisor-bound loss into account.

Thus the smooth-window off-diagonal is effectively localized to

$$
\boxed{
1\le h
\lesssim
X^{o(1)}
\frac{X}{Y}.
}
$$

At the Type-II scale,

$$
\frac{X}{Y}
\gtrsim
\frac{H}{W^{3/10}}.
$$

---

# 8. Ultra-short shifts are harmless without Möbius cancellation

Consider

$$
1\le h\le\frac{X}{Q}.
$$

Using only

$$
|c_X(n)|
\le
d_L(n),
$$

Cauchy–Schwarz and divisor moments give, uniformly in $h$,

$$
\boxed{
\sum_m
\frac{
|c_X(m)c_X(m+h)|
}{
m(m+h)
}
\ll
X^{-1+o(1)}.
}
$$

Also

$$
|\widehat\Phi|\ll1.
$$

Therefore the entire ultra-short shell contributes

## Theorem 8.1 — High-Frequency Ultra-Short Shell Bound

$$
\boxed{
|\mathcal O_{\mathrm{ultra}}|
\ll
\frac{Y}{Q}
X^{o(1)}.
}
$$

By Section 2,

$$
\boxed{
|\mathcal O_{\mathrm{ultra}}|
\ll
X^{3w/10-\varepsilon/2+o(1)}.
}
$$

Since

$$
w\le\frac{\varepsilon}{1000},
$$

this is much smaller than

$$
W^{-3/10}
=
X^{-3w/10}.
$$

Create:

```text
O-RH-103
HIGH_FREQUENCY_ULTRASHORT_SHIFT_SHELL_HARMLESS
status:
  CERTIFIED
```

This is a genuine benefit of the translated high-frequency geometry.

---

# 9. Remaining hard shell

After Sections 7–8, the unresolved shifts satisfy

$$
\boxed{
\frac{X}{Q}
<
h
\lesssim
X^{o(1)}
\frac{X}{Y}.
}
$$

For these shifts, the phase

$$
\boxed{
\phi_{Q,h}(m)
=
Q\log(1+h/m)
}
$$

has order-one or larger total variation across a dyadic $m$ -block.

Indeed,

$$
\phi'_{Q,h}(m)
=
-\frac{
Qh
}{
m(m+h)
},
$$

so over a block of length $\asymp X$ the total phase variation is

$$
\asymp
\frac{Qh}{X}.
$$

At the lower edge

$$
h=X/Q,
$$

this is already order one.

Thus the unresolved shell is genuinely oscillatory.

---

# 10. Oscillatory shifted-correlation core

Define

$$
\boxed{
\mathfrak R_{\mathrm{osc}}(Q,Y)
=
Y
\sum_{\frac{X}{Q}<h\lesssim X^{o(1)}X/Y}
\sum_m
\frac{
c_X(m)\overline{c_X(m+h)}
}{
m(m+h)
}
e^{iQ\log(1+h/m)}
\widehat\Phi
\left(
Y\log(1+h/m)
\right).
}
$$

Modulo the harmless diagonal, ultra-short shell, and Gaussian tail:

$$
\boxed{
\mathcal I_\Phi(Q,Y)
=
2\Re
\mathfrak R_{\mathrm{osc}}(Q,Y)
+
\text{harmless terms}.
}
$$

Create:

```text
O-RH-104
PURE_CORE_HIGH_FREQUENCY_HARDNESS_IS_OSCILLATORY_SHIFTED_CORRELATION
status:
  CERTIFIED AS EXACT LOCALIZATION
```

No new canonical frontier is created.

---

# 11. Polynomial- $W$ admission shape

To invoke B-RH-014 for the pure core, it is sufficient to prove

$$
\boxed{
|
\mathfrak R_{\mathrm{osc}}(Q,Y)
|
\ll
W^{-3/10}
X^{o(1)}
}
$$

uniformly over the Type-II parameter range.

For

$$
W=X^w,
$$

this is a genuine fixed-power correlation theorem.

The phase oscillation is available.

The arithmetic cancellation is not presently known.

---

# 12. Relation to ordinary Möbius correlations

The coefficient $c_X$ is not the Möbius function itself.

It is a balanced restricted convolution of several short Möbius factors.

Thus even a theorem for

$$
\sum_n
\mu(n)\mu(n+h)
$$

does not transfer automatically.

Nevertheless the standard two-point Chowla problem provides a lower-complexity calibration.

Ordinary unweighted two-point Chowla remains open.

Known averaged results produce qualitative or logarithmic savings over shifts, not a fixed $X$ -power uniformly of the form required in Section 11.

Recent 2026 progress on full-range logarithmically weighted Liouville correlations also remains power-logarithmic rather than polynomial in $X$.

Therefore current correlation technology does not supply the required core estimate.

Create:

```text
O-RH-105
CURRENT_CHOWLA_PRECISION_INSUFFICIENT_FOR_PURE_CORE_FIXED_POWER
status:
  CERTIFIED AS CURRENT-LITERATURE CALIBRATION
```

---

# 13. Average-Chowla comparison

A representative averaged-Chowla estimate has the shape

$$
\sum_{h\le H}
\left|
\sum_{n\le X}
\mu(n)\mu(n+h)
\right|
=
o(XH)
$$

or obtains powers of $\log X$ in quantitatively strengthened settings.

Such an estimate does not imply

$$
X^{-\delta}
$$

suppression for the weighted oscillatory aggregate in Section 10.

The gap is quantitative, not merely notational.

---

# 14. Zero-ordinate resonance test

One might hope that a zero

$$
\rho=\beta+i\gamma
$$

with

$$
\beta>\frac12
$$

would force one short dyadic Möbius polynomial

$$
\sum_{m\sim U}
\frac{\mu(m)}{m^{1+i\gamma}}
$$

to be large.

No such standard deterministic statement is available.

Classical zero-detection methods instead construct a composite polynomial by multiplying a short Möbius truncation by a smoothed approximation to $\zeta(s)$.

The resulting zero-detecting polynomial has different coefficients and a wider length range.

Thus:

```text
single short Mobius block:
  not a certified zero detector

composite zero-detecting polynomial:
  classical and effective
```

Create:

```text
O-RH-106
NO_CERTIFIED_SINGLE_DYADIC_MOBIUS_ZERO_DETECTOR
status:
  CERTIFIED AS METHOD-SCOPE AUDIT
```

This does not prove that no such theorem can exist.

---

# 15. High frequency is not automatically zero-frequency Mertens

The pure-core hard shell is evaluated in a translated frequency window.

The pointwise Mertens lock of Paper 39 arose by specializing a theorem at

$$
t=0.
$$

The present fixed-power admission target concerns a weighted mean square centered at

$$
Q
\gg
Y.
$$

Campaign 41 does not prove a deterministic implication

$$
\text{translated pure-core mean square}
\Longrightarrow
\text{fixed-power Mertens}.
$$

Therefore the high-frequency route remains logically distinct from the already closed pointwise route.

---

# 16. But frequency translation alone is not arithmetic cancellation

Replacing

$$
t
$$

by

$$
t-Q
$$

is equivalent to twisting the coefficients by

$$
n^{iQ}.
$$

The twist

$$
\mu(n)n^{iQ}
$$

remains a bounded multiplicative function.

Generic mean-value theorems depend mainly on coefficient magnitudes and therefore do not gain a fixed power merely from this translation.

The gain in Section 8 comes from geometric shell size.

The hard shell still needs arithmetic cancellation.

---

# 17. Campaign 41 track audit

## PM1 — translated-window moment formula

```text
status:
  EXACT

result:
  B-RH-016
```

## PM2 — zero-ordinate resonance test

```text
status:
  NO SINGLE-BLOCK ZERO-DETECTOR THEOREM FOUND

standard zero detection:
  uses composite polynomial
```

## PM3 — multi-factor simultaneous resonance

```text
status:
  REDUCED TO OSCILLATORY SHIFTED CORRELATION OF c_X

fixed-power estimate:
  OPEN
```

## PM4 — high-frequency versus zero-frequency separation

```text
status:
  LOGICALLY DISTINCT

ultra-short shifts:
  polynomially harmless from Q >> Y

remaining shell:
  arithmetic
```

## PM5 — polynomial-W admission

```text
status:
  NOT OBTAINED
```

---

# 18. Campaign 41 verdict

No polynomial- $W$ theorem is proved.

The important localization is:

```text
pure-core diagonal:
  harmless

Gaussian far-shift tail:
  harmless

ultra-short h <= X/Q:
  harmless

remaining X/Q < h <= X^(o(1)) X/Y:
  hard oscillatory shifted-correlation shell
```

The hard shell is a genuinely arithmetic object and is not presently controlled at fixed $X$ -power precision.

---

# 19. New certified package

Create:

```text
B-RH-016
TRANSLATED_PURE_CORE_MEAN_SQUARE_IDENTITY
CERTIFIED

O-RH-102
PURE_MOBIUS_CORE_DIAGONAL_HARMLESS
CERTIFIED

O-RH-103
HIGH_FREQUENCY_ULTRASHORT_SHIFT_SHELL_HARMLESS
CERTIFIED

O-RH-104
PURE_CORE_HIGH_FREQUENCY_HARDNESS_IS_OSCILLATORY_SHIFTED_CORRELATION
CERTIFIED

O-RH-105
CURRENT_CHOWLA_PRECISION_INSUFFICIENT_FOR_PURE_CORE_FIXED_POWER
CERTIFIED AS CURRENT-LITERATURE CALIBRATION

O-RH-106
NO_CERTIFIED_SINGLE_DYADIC_MOBIUS_ZERO_DETECTOR
CERTIFIED AS METHOD-SCOPE AUDIT
```

No new root frontier is created.

---

# 20. Canonical status

```text
F-RH-010
PESC
OPEN

F-RH-016
MLEPG
OPEN

B-RH-014
POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
CERTIFIED

pure-Mobius high-frequency hard shell:
  OPEN
```

---

# 21. Campaign 42

The next campaign is:

```text
CSM_RH Campaign 42
OSCILLATORY_MOBIUS_CONVOLUTION_SHIFT_ATTACK
```

The target is exactly the hard shell from Section 10.

No new observable is allowed.

---

# 22. Campaign 42 tracks

## OM1 — balanced Möbius-convolution correlation algebra

Expand

$$
c_X(m)c_X(m+h)
$$

back into the underlying short Möbius variables.

Determine whether product equality plus additive shift forces a usable bilinear or multilinear Diophantine structure.

## OM2 — phase geometry

Exploit

$$
Q\log(1+h/m)
$$

on the shell

$$
X/Q<h\lesssim X^{o(1)}X/Y.
$$

Quantify curvature and derivative scales.

## OM3 — averaged shift cancellation

Test current averaged Chowla technology after the convolution expansion.

A valid result must produce a fixed $X$ -power, not merely $o(1)$ or log savings.

## OM4 — Ramaré extraction

Audit whether extracting one small prime factor from one Möbius variable breaks the simultaneous resonance in the same spirit as the all-short-interval Möbius theorem.

The exponent ledger must survive the extra variable.

## OM5 — cross-j coupling

If the single pure-core component remains hard, test whether keeping the alternating Heath–Brown $j$ -sum before absolute values cancels the oscillatory core.

No cancellation between separate big- $O$ estimates is allowed.

---

# 23. Campaign 42 rejection filters

Reject a candidate if:

## R1. It replaces the oscillatory shell by ordinary Chowla without tracking the phase.

## R2. It obtains only logarithmic or qualitative cancellation.

## R3. It assumes pointwise fixed-power Mertens.

## R4. It assumes a fixed zero-free strip.

## R5. It uses generic bounded coefficients.

## R6. It discards the alternating cross- $j$ structure and then claims universal impossibility.

---

# 24. External calibration

The current structural calibration is:

1. the 2026 higher-uniformity paper uses Heath–Brown decomposition and componentwise Type-II estimates;
2. the actual Type-II proof requires the product mean square in Lemma 3.5;
3. standard zero-detection does not use a single short dyadic Möbius block as a canonical zero detector;
4. averaged Chowla results give qualitative/logarithmic cancellation over shifts;
5. as of September 2026, recent logarithmically weighted Liouville correlation progress remains in a power-of-logarithm precision class.

These facts leave the oscillatory pure-core shell open without falsely identifying it with a solved or fixed-strip-equivalent theorem.

---

# 25. State transition

```text
CSM_RH v1.32
  ->
CSM_RH v1.33
```

with:

```text
Campaign 41
  CLOSED_AS_TRANSLATED_WINDOW_OFFDIAGONAL_LOCALIZATION

B-RH-016
  TRANSLATED_PURE_CORE_MEAN_SQUARE_IDENTITY
  CREATED / CERTIFIED

O-RH-102
  PURE_MOBIUS_CORE_DIAGONAL_HARMLESS
  CREATED / CERTIFIED

O-RH-103
  HIGH_FREQUENCY_ULTRASHORT_SHIFT_SHELL_HARMLESS
  CREATED / CERTIFIED

O-RH-104
  PURE_CORE_HIGH_FREQUENCY_HARDNESS_IS_OSCILLATORY_SHIFTED_CORRELATION
  CREATED / CERTIFIED

O-RH-105
  CURRENT_CHOWLA_PRECISION_INSUFFICIENT_FOR_PURE_CORE_FIXED_POWER
  CREATED / CERTIFIED

O-RH-106
  NO_CERTIFIED_SINGLE_DYADIC_MOBIUS_ZERO_DETECTOR
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 42
  OSCILLATORY_MOBIUS_CONVOLUTION_SHIFT_ATTACK
  READY
```

---

# 26. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

PURE-MOBIUS DIAGONAL = HARMLESS

ULTRA-SHORT HIGH-FREQUENCY SHIFT SHELL = HARMLESS

SINGLE SHORT MOBIUS ZERO-DETECTOR LOCK = NOT ESTABLISHED

OSCILLATORY MOBIUS-CONVOLUTION OFF-DIAGONAL = OPEN

CURRENT CHOWLA PRECISION = INSUFFICIENT FOR FIXED X POWER

POLYNOMIAL-W TYPE-II ADMISSION = NOT OBTAINED

NEXT CAMPAIGN = 42
```

The decisive reduction is:

$$
\boxed{
\text{pure-Mobius polynomial-W problem}
\rightsquigarrow
\mathfrak R_{\mathrm{osc}}(Q,Y)
}
$$

with

$$
\boxed{
\frac{X}{Q}
<
h
\lesssim
X^{o(1)}
\frac{X}{Y}.
}
$$

Everything outside this oscillatory shifted-correlation shell is already below the required fixed-power scale.
