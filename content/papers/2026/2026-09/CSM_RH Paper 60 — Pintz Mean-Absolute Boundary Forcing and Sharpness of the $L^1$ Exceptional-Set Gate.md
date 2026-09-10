# CSM_RH Paper 60

## Pintz Mean-Absolute Boundary Forcing and Sharpness of the $L^1$ Exceptional-Set Gate

**Project:** CSM_RH  
**Paper:** 60  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Frontier:** F-RH-017-v2  
**Status:** BOUNDARY-ZERO SHARPNESS CERTIFIED / SUPERCRITICAL PRIME-SIDE UPPER THEOREM STILL OPEN  
**Canonical entry state:** v1.50 / Paper 59 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 59 proved that a seeded near-macroscopic exceptional-set theorem

$$
\#\left\{
n\in[N,2N]:
|\psi(n+H)-\psi(n)-H|
>
HN^{-\nu}
\right\}
\ll
N^{1-c},
$$

with

$$
H=N^{1-\tau},
$$

strictly amplifies PESC $(\kappa)$ whenever

$$
\nu>\frac{\kappa}{2},
\qquad
c>\tau.
$$

The present paper proves that these two inequalities are not artifacts of the deterministic residue-chain conversion. They are the exact critical scales selected by a hypothetical zeta zero on the seed boundary.

The main input is Pintz's mean-value theorem for arithmetic error terms. A pole of the Mellin transform at

$$
\rho=\beta+i\gamma
$$

forces a mean absolute error of order

$$
Y^\beta
$$

up to a nonzero constant depending on the pole.

To adapt this cancellation-robust theorem to short intervals, define

$$
A(x)=\psi(x)-x
$$

and, for

$$
0<h\le h_0,
$$

the normalized multiplicative difference

$$
\boxed{
B_h(x)
=
\frac{
A((1+h)x)-A(x)
}{h}.
}
$$

If

$$
\mathcal M(s)
=
\int_1^\infty
A(x)x^{-s-1}\,dx,
$$

then

$$
\boxed{
\mathcal M_h(s)
=
\int_1^\infty
B_h(x)x^{-s-1}\,dx
=
Q_h(s)\mathcal M(s)
+
E_h(s),
}
$$

where

$$
\boxed{
Q_h(s)
=
\frac{(1+h)^s-1}{h}
=
s
\int_0^1
(1+uh)^{s-1}\,du
}
$$

and $E_h$ is entire.

For every fixed nontrivial zeta zero $\rho$,

$$
Q_h(\rho)\to\rho
$$

as $h\to0$. Hence, after choosing $h_0>0$ small enough,

$$
\boxed{
|Q_h(\rho)|
\asymp_\rho1
}
$$

uniformly for

$$
0<h\le h_0.
$$

The growth conditions in Pintz's contour theorem are also uniform in this normalized family: $Q_h$ has only polynomial vertical growth and the entire correction comes from a compact interval of length $h$ divided by $h$.

Repeating Pintz's proof with these uniform bounds gives the multiplicative short-interval mean-value theorem

$$
\boxed{
\frac1Y
\int_1^Y
\left|
A((1+h)x)-A(x)
\right|
\,dx
\gg_\rho
hY^\beta
}
$$

uniformly for

$$
0<h\le h_0
$$

and all sufficiently large $Y$.

Thus a single zeta zero forces short-interval mean absolute oscillation at exactly the differentiated explicit-formula scale.

Now assume the seed PESC $(\kappa)$ and put

$$
d=\frac{\kappa}{2}.
$$

Then

$$
|A(x)|
\ll
x^{1-d+o(1)}.
$$

If a boundary zero exists with

$$
\beta=1-d,
$$

take

$$
h=Y^{-\tau}.
$$

The Pintz lower bound becomes

$$
\int_1^Y
|A((1+h)x)-A(x)|\,dx
\gg_\rho
hY^{2-d}.
$$

Consider a supercritical threshold

$$
hY^{1-\nu},
\qquad
\nu>d.
$$

The contribution from points below threshold is only

$$
hY^{2-\nu}
=
o(hY^{2-d}).
$$

At every exceptional point, the seed pointwise envelope bounds the error by

$$
Y^{1-d+o(1)}.
$$

Therefore the number or measure of exceptional points must satisfy

$$
\boxed{
|\mathcal E|
\gg_\rho
hY^{1-o(1)}
=
Y^{1-\tau-o(1)}.
}
$$

A boundary zero thus saturates the exceptional exponent

$$
\boxed{
c=\tau.
}
$$

This matches Paper 59 exactly.

More generally, a zero at

$$
\beta
=
1-d-\delta
$$

forces multiplicative exceptional mass at least

$$
Y^{1-\tau-\delta-o(1)}
$$

whenever

$$
\nu>d+\delta.
$$

Thus a supercritical exceptional-set theorem can only exclude such a zero when

$$
c>\tau+\delta.
$$

The two inequalities

$$
\nu>d+\delta,
\qquad
c>\tau+\delta
$$

are exactly the threshold and exceptional-mass margins predicted by the $L^1$ amplifier.

Finally, the paper proves a purely deterministic fixed-lag sharpness model. With

$$
H=N^{1-\tau},
$$

one can construct a sequence satisfying the seed pointwise and $L^2$ scales, with exactly one critical bad $H$ -increment on each residue chain. It has

$$
N^{1-\tau}
$$

bad increments and no global exponent improvement. Hence no deterministic converter using only:

- the seed pointwise envelope;
- the number of bad increments; and
- a single $H$ -lag

can replace

$$
c>\tau
$$

by a weaker universal condition.

Together with the smooth boundary power mode from Papers 54–55, which saturates

$$
\nu=\frac{\kappa}{2},
$$

the F-RH-017-v2 gate is sharp in both parameters.

The conclusion is methodological but decisive:

```text
threshold gate nu > kappa/2:
sharp because of the boundary smooth mode.

exception-count gate c > tau:
sharp because of both residue-chain contamination
and cancellation-robust Pintz mean-absolute boundary forcing.
```

There is no remaining deterministic optimization of the F-RH-017-v2 bridge. Future progress must prove the supercritical prime-side exceptional-set estimate itself.

No RH theorem is claimed.

---

# 1. Pintz's mean-value input

Let

$$
C(x)
$$

be an arithmetic error term whose Mellin transform

$$
\int_1^\infty
C(x)x^{-s-1}\,dx
$$

has a pole at

$$
\rho_0=\beta_0+i\gamma_0.
$$

Pintz's 2022 mean-value theorem gives, under standard analytic continuation and growth assumptions,

$$
\boxed{
\frac1Y
\int_1^Y
|C(x)|\,dx
\gg_{\rho_0}
Y^{\beta_0}
}
$$

up to logarithmic factors when the pole has higher order.

For the prime-number-theorem error

$$
A(x)=\psi(x)-x,
$$

the conditions are satisfied and every nontrivial zeta zero gives such a pole.

In particular, if

$$
\rho=\beta+i\gamma
$$

is a fixed nontrivial zero,

$$
\boxed{
\frac1Y
\int_1^Y
|A(x)|\,dx
\gg_\rho
Y^\beta.
}
$$

This theorem is cancellation-robust: it does not require one zero term to dominate the explicit formula pointwise.

External source:

J. Pintz, *On the Mean Value of Arithmetic Error Terms*, Mathematica Pannonica 28 (2022), 58–64.

---

# 2. Normalized multiplicative differences

Fix

$$
0<h\le h_0<1.
$$

Define

$$
\boxed{
B_h(x)
=
\frac{
A((1+h)x)-A(x)
}{h}.
}
$$

Let

$$
\mathcal M(s)
=
\int_1^\infty
A(x)x^{-s-1}\,dx.
$$

For $\Re s$ sufficiently large,

$$
\begin{aligned}
\int_1^\infty
A((1+h)x)x^{-s-1}\,dx
&=
(1+h)^s
\int_{1+h}^\infty
A(u)u^{-s-1}\,du
\\
&=
(1+h)^s
\mathcal M(s)
-
(1+h)^s
\int_1^{1+h}
A(u)u^{-s-1}\,du.
\end{aligned}
$$

Therefore

$$
\boxed{
\mathcal M_h(s)
=
Q_h(s)\mathcal M(s)
+
E_h(s),
}
$$

where

$$
\boxed{
Q_h(s)
=
\frac{
(1+h)^s-1
}{h}
}
$$

and

$$
\boxed{
E_h(s)
=
-
\frac{
(1+h)^s
}{h}
\int_1^{1+h}
A(u)u^{-s-1}\,du.
}
$$

Since the final integral is over a compact interval, $E_h$ is entire.

---

# 3. Uniformity of the multiplier family

The identity

$$
(1+h)^s-1
=
s
\int_0^h
(1+v)^{s-1}\,dv
$$

gives

$$
\boxed{
Q_h(s)
=
s
\int_0^1
(1+uh)^{s-1}\,du.
}
$$

On every fixed vertical strip

$$
\sigma_1\le\Re s\le\sigma_2,
$$

$$
\boxed{
|Q_h(s)|
\ll_{\sigma_1,\sigma_2,h_0}
1+|s|
}
$$

uniformly in

$$
0<h\le h_0.
$$

There is no exponential vertical growth because

$$
|(1+uh)^{it}|=1.
$$

For fixed $\rho$,

$$
\boxed{
Q_h(\rho)\to\rho
}
$$

as

$$
h\to0.
$$

Since a nontrivial zero has $\rho\ne0$, choose $h_0$ small enough that

$$
\boxed{
|Q_h(\rho)|
\ge
\frac{|\rho|}{2}
}
$$

for

$$
0<h\le h_0.
$$

The entire correction also has uniform vertical growth. Indeed, on the compact interval $1\le u\le1+h_0$, $A(u)$ is bounded, and the factor $h^{-1}$ is cancelled by the integration interval length.

Thus the analytic and growth constants entering Pintz's contour proof may be chosen uniformly for the normalized family $B_h$.

---

# 4. Uniformized Pintz short-interval theorem

The Mellin transform $\mathcal M$ has at $\rho$ the pole induced by

$$
-\frac{\zeta'(s)}{\zeta(s)}.
$$

Multiplication by $Q_h(s)$ preserves its order and multiplies its leading coefficient by the nonzero factor $Q_h(\rho)$.

The entire correction $E_h$ creates no pole.

Applying Pintz's theorem with the uniform bounds of Section 3 gives:

## Theorem 4.1 — Uniform multiplicative short-interval mean forcing

Let

$$
\rho=\beta+i\gamma
$$

be a fixed nontrivial zeta zero.

There exist constants

$$
h_0>0,
\qquad
c_\rho>0,
\qquad
Y_\rho\ge2
$$

such that, uniformly for

$$
0<h\le h_0
$$

and

$$
Y\ge Y_\rho,
$$

$$
\boxed{
\frac1Y
\int_1^Y
|B_h(x)|\,dx
\ge
c_\rho
Y^\beta
}
$$

at exponent resolution.

Equivalently,

$$
\boxed{
\int_1^Y
|A((1+h)x)-A(x)|\,dx
\gg_\rho
hY^{\beta+1}.
}
$$

If the zero has multiplicity greater than one, an additional nonnegative logarithmic factor may appear and only strengthens the result.

Create:

```text
B-RH-067
UNIFORM_PINTZ_MULTIPLICATIVE_SHORT_INTERVAL_MEAN_ABSOLUTE_ZERO_FORCING
CERTIFIED
```

This theorem is an adaptation of Pintz's general pole-to-mean-value result, not a claim that the broad mean-value philosophy is new.

---

# 5. Boundary-zero exceptional mass

Assume PESC $(\kappa)$ and set

$$
d=\frac{\kappa}{2}.
$$

The seed gives

$$
\boxed{
|A(x)|
\ll
x^{1-d+o(1)}.
}
$$

Suppose a zero exists on the seed boundary:

$$
\boxed{
\beta=1-d.
}
$$

Choose

$$
h=Y^{-\tau},
\qquad
\tau>0.
$$

Theorem 4.1 gives

$$
\boxed{
\int_1^Y
|A((1+h)x)-A(x)|\,dx
\gg_\rho
hY^{2-d}.
}
$$

Fix a threshold exponent

$$
\nu>d.
$$

Define

$$
\mathcal E(Y)
=
\left\{
x\in[1,Y]:
|A((1+h)x)-A(x)|
>
hY^{1-\nu}
\right\}.
$$

On the good set,

$$
\int_{\mathcal E^c}
|A((1+h)x)-A(x)|\,dx
\le
hY^{2-\nu}
=
o(hY^{2-d}).
$$

On the exceptional set, the seed pointwise envelope gives

$$
|A((1+h)x)-A(x)|
\ll
Y^{1-d+o(1)}.
$$

Therefore:

## Theorem 5.1 — Boundary-zero exceptional-mass lower bound

If a zero lies on

$$
\beta=1-\frac{\kappa}{2},
$$

then for every fixed

$$
\nu>\frac{\kappa}{2}
$$

and

$$
h=Y^{-\tau},
$$

$$
\boxed{
|\mathcal E(Y)|
\gg_\rho
Y^{1-\tau-o(1)}.
}
$$

Create:

```text
B-RH-068
BOUNDARY_ZERO_FORCES_CRITICAL_MULTIPLICATIVE_EXCEPTIONAL_MASS
CERTIFIED
```

Thus the boundary zero itself saturates

$$
\boxed{
c=\tau.
}
$$

---

# 6. Near-boundary zero version

Let

$$
\boxed{
\beta
=
1-d-\delta,
\qquad
\delta\ge0.
}
$$

Theorem 4.1 gives

$$
\boxed{
\int_1^Y
|A((1+h)x)-A(x)|\,dx
\gg_\rho
hY^{2-d-\delta}.
}
$$

If

$$
\nu>d+\delta,
$$

the good-set contribution at threshold

$$
hY^{1-\nu}
$$

is lower order.

Using the seed pointwise envelope on the bad set gives:

## Theorem 6.1 — Near-boundary exceptional-mass lower bound

For

$$
h=Y^{-\tau}
$$

and

$$
\nu>d+\delta,
$$

a zero at

$$
\beta=1-d-\delta
$$

forces

$$
\boxed{
|\mathcal E(Y)|
\gg_\rho
Y^{1-\tau-\delta-o(1)}.
}
$$

Therefore any multiplicative exceptional upper bound

$$
|\mathcal E(Y)|
\ll
Y^{1-c}
$$

excludes such a zero whenever

$$
\boxed{
c>\tau+\delta.
}
$$

The two zero-detection margins are exactly

$$
\boxed{
\delta<\nu-d
}
$$

and

$$
\boxed{
\delta<c-\tau.
}
$$

They are the same threshold and exceptional-count margins appearing in the $L^1$ amplifier.

---

# 7. Why the result is genuinely cancellation-robust

A single explicit-formula zero mode suggests the same scales heuristically, but that does not control cancellation with all other zeros.

The role of Pintz's theorem is precisely to remove this ambiguity.

Its conclusion is a lower bound for

$$
\int|A(x)|\,dx
$$

derived from the Mellin pole itself.

The uniformized multiplier argument transfers that pole to the multiplicative difference.

Thus Theorems 5.1 and 6.1 do not assume:

- dominance of one zero term;
- zero spacing;
- simple zeros;
- pair correlation;
- absence of nearby zeros.

This is the main new calibration supplied by the present paper.

---

# 8. Deterministic fixed-lag sharpness model

The multiplicative Pintz theorem proves arithmetic sharpness of the exception-count scale.

We now give an independent deterministic sharpness model for the fixed-lag residue-chain bridge of Paper 59.

Let

$$
H=N^{1-\tau}
$$

and, for simplicity, assume $H$ divides $N$ at the model level.

There are $H$ residue classes modulo $H$.

For every

$$
1\le r\le H,
$$

define along the chain

$$
r,\ r+H,\ r+2H,\ldots
$$

the sequence

$$
A(r)=0
$$

and

$$
\boxed{
A(r+kH)=N^{1-d}
\qquad
(k\ge1).
}
$$

Then exactly one $H$ -increment on each residue chain is nonzero:

$$
\boxed{
U_H(r)=N^{1-d},
}
$$

and all later increments vanish.

Hence the number of bad increments is exactly

$$
\boxed{
H=N^{1-\tau}.
}
$$

The pointwise seed scale is saturated:

$$
|A(n)|\le N^{1-d}.
$$

The global $L^2$ seed scale is also saturated:

$$
\boxed{
\sum_{n\asymp N}|A(n)|^2
\asymp
N^{3-2d}
=
N^{3-\kappa}.
}
$$

But there is no improved exponent.

Thus:

## Theorem 8.1 — Residue-chain exception-count sharpness

No deterministic theorem using only:

1. the seed pointwise bound;
2. the seed global $L^2$ scale;
3. one lag $H=N^{1-\tau}$ ; and
4. the total number of exceptional $H$ -increments

can guarantee strict amplification under the weaker universal condition

$$
c\le\tau.
$$

Create:

```text
O-RH-143
L1_EXCEPTION_COUNT_GATE_C_GREATER_THAN_TAU_IS_DETERMINISTICALLY_SHARP
CERTIFIED
```

---

# 9. Threshold sharpness

Paper 55's smooth boundary model already gives

$$
\boxed{
U_H(x)
\asymp
HN^{-d}
}
$$

when

$$
d=\frac{\kappa}{2}.
$$

Thus a threshold

$$
HN^{-\nu}
$$

with

$$
\nu\le d
$$

does not lie strictly below the boundary-mode amplitude.

No exceptional theorem at such a threshold is forced to remove the boundary mode.

Therefore:

```text
threshold sharpness:
nu > kappa/2 is necessary.

exception-count sharpness:
c > tau is necessary.
```

Paper 59 proved these conditions are sufficient for the $L^1$ converter.

The present paper proves that both are sharp at the level of the currently available seed data and boundary-zero geometry.

---

# 10. Sharpness of F-RH-017-v2

The preferred frontier is

$$
H=N^{1-\tau}
$$

with

$$
\#\left\{
n\in[N,2N]:
|U_H(n)|
>
HN^{-\nu}
\right\}
\ll
N^{1-c}.
$$

Paper 59 proved:

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>\tau
}
$$

is sufficient for a strict exponent gain.

The present paper gives the matching critical obstructions:

$$
\boxed{
\nu=\frac{\kappa}{2}
}
$$

is saturated by the smooth boundary mode, and

$$
\boxed{
c=\tau
}
$$

is saturated by the residue-chain contamination model.

The multiplicative Pintz theorem further shows that a genuine boundary zeta zero forces exceptional mass at exactly this $c=\tau$ scale in a cancellation-robust short-interval observable.

Therefore F-RH-017-v2 is parameter-sharp for the present architecture.

No further deterministic improvement of its $(\nu,c,\tau)$ gate should count as a plausible source of the missing RH exponent.

---

# 11. What remains open

Sharpness does not prove the desired upper theorem.

The direct arithmetic target remains:

$$
\boxed{
\#\left\{
n\in[N,2N]:
|\psi(n+N^{1-\tau})-\psi(n)-N^{1-\tau}|
>
N^{1-\tau-\kappa/2-\varepsilon}
\right\}
\ll
N^{1-c}
}
$$

with fixed

$$
\boxed{
\varepsilon>0,
\qquad
c>\tau.
}
$$

The current finite positive-moment architecture cannot cross the threshold.

The current linear Turan-Gallagher and Euler-product positivity architectures cannot supply the fixed boundary gap.

Thus the missing result is now purely arithmetic.

---

# 12. A useful converse interpretation

Suppose a theorem of F-RH-017-v2 type is eventually proved.

Paper 59 converts it into a strict zero-strip improvement.

Theorems 5.1–6.1 explain the converse mechanism:

a zero remaining in the forbidden strip would force too much short-interval mean absolute mass and therefore too many supercritical exceptional intervals.

Thus the exceptional-set theorem is not merely a sufficient technical device.

At the sharp scale, it is a quantitative manifestation of zero exclusion.

This is consistent with classical inverse short-interval theory, but here the threshold and exception-count exponents are matched explicitly to the seeded PESC boundary.

---

# 13. External calibration

## 13.1. Pintz mean-value theorem

János Pintz,
*On the Mean Value of Arithmetic Error Terms*,
Mathematica Pannonica, New Series 28 (2022), 58–64.

Pintz proves a general Mellin-pole-to-mean-absolute-value theorem and obtains for the PNT error

$$
\frac1Y
\int_1^Y
|\psi(x)-x|\,dx
\gg_{\rho}
Y^\beta
$$

from any fixed nontrivial zero

$$
\rho=\beta+i\gamma.
$$

DOI:

https://doi.org/10.1556/314.2022.00007

## 13.2. Recent inverse-theory calibration

Johnston and Trudgian,
*A round of Pintz to celebrate oscillations in sums*,
Analysis Mathematica, 2026.

They make explicit a modern Pintz/Landau framework for deducing zero information from arithmetic sum bounds.

The present short-interval multiplier calculation is a CSM_RH-specific adaptation of this broad Mellin-pole philosophy.

---

# 14. State transition

Advance the candidate state from

$$
v1.50
$$

to

$$
v1.51.
$$

Add:

```text
B-RH-067
UNIFORM_PINTZ_MULTIPLICATIVE_SHORT_INTERVAL_MEAN_ABSOLUTE_ZERO_FORCING
CERTIFIED
```

Add:

```text
B-RH-068
BOUNDARY_ZERO_FORCES_CRITICAL_MULTIPLICATIVE_EXCEPTIONAL_MASS
CERTIFIED
```

Add:

```text
O-RH-143
L1_EXCEPTION_COUNT_GATE_C_GREATER_THAN_TAU_IS_DETERMINISTICALLY_SHARP
CERTIFIED
```

Frontier:

```text
F-RH-017-v2
UNCHANGED / NOW PARAMETER-SHARPNESS CERTIFIED
```

No RH certificate is created.

---

# 15. Conclusion

The remaining F-RH-017-v2 gate is not loose.

Its two strict inequalities

$$
\boxed{
\nu>\frac{\kappa}{2}
}
$$

and

$$
\boxed{
c>\tau
}
$$

are both critical.

The first is saturated by the smooth explicit-formula boundary mode.

The second is saturated by residue-chain contamination and, in a cancellation-robust arithmetic sense, by Pintz mean-absolute forcing from a boundary zeta zero.

Therefore the route cannot be made easier by another deterministic norm conversion.

The next advance must prove the supercritical exceptional-set upper theorem itself.
