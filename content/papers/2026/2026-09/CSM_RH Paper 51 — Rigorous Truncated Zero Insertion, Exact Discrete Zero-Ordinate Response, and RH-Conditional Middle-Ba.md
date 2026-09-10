# CSM_RH Paper 51

## Rigorous Truncated Zero Insertion, Exact Discrete Zero-Ordinate Response, and RH-Conditional Middle-Band Admission

**Project:** CSM_RH  
**Paper:** 51  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 44 — `PESC_TRIANGULAR_LAG_KERNEL_ATTACK`  
**Track:** PK5 — `FIXED_POWER_PESC_ADMISSION`  
**Subtracks:** Z1 / Z2, with Z3–Z4 frontier audit  
**Status:** Z1 CLOSED / Z2 CLOSED / PK5 STILL OPEN UNCONDITIONALLY  
**Canonical entry state:** v1.41 / Paper 50 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 50 converted the centered prime PESC statistic into the exact centered Abel transform

$$
\mathfrak L_N(t)
=
\sum_{m=N}^{2N-1}
(\psi(m)-m)
\Delta g_{N,t}(m),
$$

where

$$
g_{N,t}(x)
=
\frac{(2N/x)^{it}-1}{x},
\qquad
\Delta g_{N,t}(m)
=
g_{N,t}(m)-g_{N,t}(m+1).
$$

The fixed-power target is

$$
\mathcal E_\Lambda(N,\kappa)
=
\int_{N^{-\kappa}\le |t|\le N^\kappa}
\frac{|\mathfrak L_N(t)|^2}{t^2}\,dt
\ll
N^{-\kappa+o(1)}
$$

for fixed

$$
0<\kappa\le1.
$$

The present paper first inserts a standard truncated von Mangoldt explicit formula at the exact integer arguments occurring in the Abel sum. Taking the zero height

$$
T=N^\kappa,
$$

the explicit-formula remainder is shown to contribute only

$$
O\!\left(
N^{-\kappa}\log^4 N
\right)
$$

to the centered middle-band energy. Thus the truncation ledger itself is fixed-power admissible.

Second, for each nontrivial zero

$$
\rho=\beta+i\gamma,
$$

an exact discrete response kernel is extracted:

$$
\mathcal K_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^\rho
\Delta g_{N,t}(m).
$$

It has the exact centered frequency representation

$$
\boxed{
\mathcal K_{\rho,N}(t)
=
(2N)^{it}A_{\rho,N}(t)-A_{\rho,N}(0),
}
$$

where

$$
\boxed{
A_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^{\rho-1-it}
\left[
1-
\left(
\frac{m}{m+1}
\right)^{1+it}
\right].
}
$$

The oscillatory phase is therefore exactly

$$
m^{i(\gamma-t)}.
$$

The alignment of the translated Mellin frequency $t$ with the zero ordinate $\gamma$ is not a continuous approximation; it is already present in the finite discrete kernel.

Using the Kusmin–Landau first derivative estimate and partial summation, the paper proves the uniform localization bound

$$
|\mathcal K_{\rho,N}(t)|
\ll
N^{\beta-1}
\left[
\frac{1+|t|}
{|\rho|(1+|\gamma-t|)}
+
\frac1{|\rho|(1+|\gamma|)}
\right]
$$

throughout

$$
|t|\le N,
\qquad
|\gamma|\le N.
$$

For $|t|\le1$, exact centering improves this to

$$
|\mathcal K_{\rho,N}(t)|
\ll
|t|
\frac{N^{\beta-1}}{|\rho|}.
$$

As a calibration theorem, RH implies the full PK5 middle-band target. Indeed, under RH every $\beta=1/2$ ; Riemann–von Mangoldt zero counting and the response localization give a finite-zero contribution

$$
O(N^{-1}\log^4 N)
$$

in energy, while the explicit-formula truncation contributes

$$
O(N^{-\kappa}\log^4 N).
$$

Thus RH implies

$$
\mathcal E_\Lambda(N,\kappa)
\ll
N^{-\kappa+o(1)}
$$

for every fixed $0<\kappa\le1$.

This is only a one-way conditional calibration. No converse and no RH proof is obtained. Unconditionally, classical zero-free regions combined with absolute zero-response summation do not supply a fixed power near the top of the polynomial zero window. The remaining PK5 problem is therefore the cross-zero / near-ordinate structure and the exclusion or detection of off-critical mass.

---

# 1. Canonical entry object

Paper 50 certified

$$
\boxed{
\mathfrak L_N(t)
=
\sum_{m=N}^{2N-1}
E_\psi(m)
\Delta g_{N,t}(m),
}
$$

where

$$
E_\psi(m)=\psi(m)-m
$$

and

$$
g_{N,t}(x)
=
\frac{(2N/x)^{it}-1}{x}.
$$

The target is

$$
\boxed{
\mathcal E_\Lambda(N,\kappa)
=
\int_{\mathcal B_{N,\kappa}}
\frac{|\mathfrak L_N(t)|^2}{t^2}\,dt
\ll
N^{-\kappa+o(1)},
}
$$

with

$$
\mathcal B_{N,\kappa}
=
\left\{
t\in\mathbb R:
N^{-\kappa}\le |t|\le N^\kappa
\right\}.
$$

Paper 50 left the following sequence:

```text
Z1 RIGOROUS_TRUNCATED_EXPLICIT_FORMULA_INSERTION
Z2 CENTERED_ZERO_RESPONSE_KERNEL_EXTRACTION
Z3 ZERO_WINDOW_CROSS_TERM_AND_NEAR_ORDINATE_AUDIT
Z4 OFF_CRITICAL_ANTI_CANCELLATION_OR_CRITICAL_LINE_ADMISSION
```

The present paper closes Z1 and Z2.

---

# 2. Truncated explicit formula

We use the standard truncated von Mangoldt explicit formula in the form

$$
\boxed{
\psi(x)
=
x
-
\sum_{|\gamma|\le T}
\frac{x^\rho}{\rho}
+
R_\psi(x,T),
}
$$

where the sum runs over nontrivial zeros

$$
\rho=\beta+i\gamma
$$

with multiplicity and

$$
\boxed{
R_\psi(x,T)
\ll
\frac{x\log^2(xT)}{T}
+
\log x
}
$$

for

$$
x,T\ge2.
$$

The constant and trivial-zero terms are absorbed into the displayed error at the resolution needed here.

For

$$
N\le m\le2N,
$$

this becomes

$$
E_\psi(m)
=
-
\sum_{|\gamma|\le T}
\frac{m^\rho}{\rho}
+
R_\psi(m,T),
$$

with

$$
|R_\psi(m,T)|
\ll
\frac{N\log^2(NT)}{T}
+
\log N.
$$

Since the zero sum is finite, it can be interchanged with the finite Abel sum without any convergence issue.

---

# 3. Total variation of the centered Abel kernel

Differentiate

$$
g_{N,t}(x)
=
(2N)^{it}x^{-1-it}-x^{-1}.
$$

Then

$$
g_{N,t}'(x)
=
x^{-2}
\left[
1-
(1+it)
\left(
\frac{2N}{x}
\right)^{it}
\right].
$$

For

$$
N\le x\le2N,
$$

write

$$
\theta
=
t\log\frac{2N}{x}.
$$

If $|t|\le1$,

$$
\left|
1-(1+it)e^{i\theta}
\right|
\le
|1-e^{i\theta}|+|t|
\ll
|t|.
$$

If $|t|\ge1$,

$$
\left|
1-(1+it)e^{i\theta}
\right|
\le
1+|1+it|
\ll
|t|.
$$

Therefore, for all real $t$,

$$
\boxed{
|g_{N,t}'(x)|
\ll
\frac{|t|}{N^2}
}
$$

on the complete dyadic interval.

By the fundamental theorem of calculus,

$$
|\Delta g_{N,t}(m)|
\le
\int_m^{m+1}|g_{N,t}'(x)|\,dx,
$$

and hence

$$
\boxed{
\sum_{m=N}^{2N-1}
|\Delta g_{N,t}(m)|
\ll
\frac{|t|}{N}.
}
$$

This is the key reason the ordinary pointwise explicit-formula remainder becomes power-admissible after insertion into the centered Abel kernel.

---

# 4. Z1 theorem: polynomial-height truncation is admissible

Insert the truncated explicit formula into Paper 50:

$$
\mathfrak L_N(t)
=
-
\sum_{|\gamma|\le T}
\mathcal K_{\rho,N}(t)
+
\mathfrak R_{N,T}^{\mathrm{EF}}(t),
$$

where

$$
\boxed{
\mathcal K_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^\rho
\Delta g_{N,t}(m)
}
$$

and

$$
\mathfrak R_{N,T}^{\mathrm{EF}}(t)
=
\sum_{m=N}^{2N-1}
R_\psi(m,T)
\Delta g_{N,t}(m).
$$

Using Section 3,

$$
|\mathfrak R_{N,T}^{\mathrm{EF}}(t)|
\ll
|t|
\left[
\frac{\log^2(NT)}{T}
+
\frac{\log N}{N}
\right].
$$

Define the remainder energy

$$
\mathcal E_{\mathrm{EF}}(N,\kappa,T)
=
\int_{\mathcal B_{N,\kappa}}
\frac{
|\mathfrak R_{N,T}^{\mathrm{EF}}(t)|^2
}{t^2}\,dt.
$$

Since the length of the two-sided band is

$$
O(N^\kappa),
$$

we obtain

$$
\mathcal E_{\mathrm{EF}}(N,\kappa,T)
\ll
N^\kappa
\left[
\frac{\log^4(NT)}{T^2}
+
\frac{\log^2N}{N^2}
\right].
$$

Take

$$
\boxed{
T=N^\kappa.
}
$$

For fixed

$$
0<\kappa\le1,
$$

the first term becomes

$$
N^{-\kappa}\log^4N,
$$

while

$$
N^{\kappa-2}\log^2N
\le
N^{-\kappa}\log^2N.
$$

Therefore:

## Theorem 4.1 — Middle-band admissible explicit-formula truncation

For every fixed $0<\kappa\le1$, taking $T=N^\kappa$ gives

$$
\boxed{
\mathcal E_{\mathrm{EF}}
\left(
N,\kappa,N^\kappa
\right)
\ll
N^{-\kappa}\log^4N
=
N^{-\kappa+o(1)}.
}
$$

Thus Z1 is closed.

Create:

```text
B-RH-044
PESC_CENTERED_ABEL_POLYNOMIAL_HEIGHT_EXPLICIT_FORMULA_WITH_ADMISSIBLE_REMAINDER
CERTIFIED
```

Close:

```text
Z1
CLOSED_AS_POLYNOMIAL_HEIGHT_EXPLICIT_FORMULA_WITH_MIDDLE_BAND_ADMISSIBLE_REMAINDER
```

No hypothesis on the zero real parts has been used.

---

# 5. Exact discrete response of one zero

The zero response is

$$
\mathcal K_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^\rho
\Delta g_{N,t}(m).
$$

Expand

$$
g_{N,t}(m)
=
(2N)^{it}m^{-1-it}-m^{-1}.
$$

Then

$$
\Delta g_{N,t}(m)
=
(2N)^{it}
\left[
m^{-1-it}-(m+1)^{-1-it}
\right]
-
\left[
m^{-1}-(m+1)^{-1}
\right].
$$

Define

$$
\boxed{
A_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^\rho
\left[
m^{-1-it}-(m+1)^{-1-it}
\right].
}
$$

Then:

## Theorem 5.1 — Exact centered zero response

For every nontrivial zero $\rho$ and every real $t$,

$$
\boxed{
\mathcal K_{\rho,N}(t)
=
(2N)^{it}A_{\rho,N}(t)-A_{\rho,N}(0).
}
$$

Moreover,

$$
m^\rho
\left[
m^{-1-it}-(m+1)^{-1-it}
\right]
=
m^{\rho-1-it}
\left[
1-
\left(
\frac{m}{m+1}
\right)^{1+it}
\right].
$$

Hence

$$
\boxed{
A_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^{\rho-1-it}
q_t(m),
}
$$

where

$$
q_t(m)
=
1-
\left(
\frac{m}{m+1}
\right)^{1+it}.
$$

If

$$
\rho=\beta+i\gamma,
$$

the oscillatory factor is exactly

$$
\boxed{
m^{i(\gamma-t)}.
}
$$

Thus the translated frequency variable $t$ is exactly centered on the zero ordinate $\gamma$ in the finite discrete response.

The centering is also exact:

$$
\boxed{
\mathcal K_{\rho,N}(0)=0.
}
$$

Create:

```text
B-RH-045
PESC_EXACT_DISCRETE_CENTERED_ZERO_ORDINATE_RESPONSE_KERNEL
CERTIFIED
```

---

# 6. Bounds for the local response amplitude

For real $x\ge N$, define

$$
q_t(x)
=
1-
\left(
\frac{x}{x+1}
\right)^{1+it}.
$$

Write

$$
\ell_x
=
\log\left(1+\frac1x\right).
$$

Then

$$
q_t(x)
=
1-
e^{-(1+it)\ell_x}.
$$

If

$$
|t|\le N
$$

and

$$
x\ge N,
$$

then

$$
|(1+it)\ell_x|
\ll1.
$$

Therefore

$$
\boxed{
|q_t(x)|
\ll
\frac{1+|t|}{x}.
}
$$

Differentiating gives

$$
q_t'(x)
=
-
\left(
\frac{x}{x+1}
\right)^{1+it}
\frac{1+it}{x(x+1)}
$$

up to the immaterial sign convention, so

$$
\boxed{
|q_t'(x)|
\ll
\frac{1+|t|}{x^2}.
}
$$

Now define the slowly varying coefficient

$$
b_{\beta,t}(x)
=
x^{\beta-1}q_t(x).
$$

Since

$$
0<\beta<1,
$$

we have uniformly on $[N,2N]$,

$$
|b_{\beta,t}(x)|
\ll
(1+|t|)N^{\beta-2}
$$

and

$$
|b_{\beta,t}'(x)|
\ll
(1+|t|)N^{\beta-3}.
$$

Thus its total variation is

$$
\boxed{
\operatorname{Var}_{[N,2N]}
b_{\beta,t}
\ll
(1+|t|)N^{\beta-2}.
}
$$

---

# 7. Kusmin–Landau localization in $\gamma-t$

Let

$$
u=\gamma-t.
$$

For

$$
1\le |u|\le2N,
$$

consider the phase

$$
f_u(x)
=
\frac{u}{2\pi}\log x.
$$

Then

$$
f_u'(x)
=
\frac{u}{2\pi x}
$$

is monotone and, on

$$
N\le x\le2N,
$$

satisfies

$$
\frac{|u|}{4\pi N}
\le
|f_u'(x)|
\le
\frac1\pi
<
\frac12.
$$

Therefore the distance of $f_u'(x)$ to the nearest integer is at least

$$
\frac{|u|}{4\pi N}.
$$

The Kusmin–Landau first derivative estimate yields

$$
\sup_{N\le M\le2N}
\left|
\sum_{m=N}^{M}
m^{iu}
\right|
\ll
\frac{N}{|u|}.
$$

For $|u|<1$, the trivial estimate is $O(N)$.

Combining the two regimes,

$$
\boxed{
\sup_{N\le M\le2N}
\left|
\sum_{m=N}^{M}
m^{iu}
\right|
\ll
\frac{N}{1+|u|}.
}
$$

Partial summation with Section 6 therefore gives

$$
\left|
\sum_{m=N}^{2N-1}
m^{\rho-1-it}q_t(m)
\right|
\ll
\frac{
(1+|t|)N^{\beta-1}
}{
1+|\gamma-t|
}.
$$

Thus:

## Theorem 7.1 — Exact discrete zero-frequency localization

Whenever

$$
|t|\le N,
\qquad
|\gamma|\le N,
$$

we have

$$
\boxed{
|A_{\rho,N}(t)|
\ll
\frac{
(1+|t|)N^{\beta-1}
}{
|\rho|(1+|\gamma-t|)
}.
}
$$

Consequently,

$$
\boxed{
|\mathcal K_{\rho,N}(t)|
\ll
N^{\beta-1}
\left[
\frac{1+|t|}
{|\rho|(1+|\gamma-t|)}
+
\frac1{|\rho|(1+|\gamma|)}
\right].
}
$$

This is the rigorous discrete analogue of the continuous single-zero response calibration in Paper 50.

---

# 8. Additional low-frequency gain from exact centering

For

$$
|t|\le1,
$$

differentiate

$$
g_{N,t}(x)
$$

with respect to $t$:

$$
\partial_t g_{N,t}(x)
=
i
\log\frac{2N}{x}
\frac{(2N/x)^{it}}{x}.
$$

On

$$
N\le x\le2N
$$

and

$$
|t|\le1,
$$

one has

$$
\left|
\partial_x\partial_t
g_{N,t}(x)
\right|
\ll
N^{-2}.
$$

Therefore

$$
\left|
\partial_t
\Delta g_{N,t}(m)
\right|
\ll
N^{-2}.
$$

It follows that

$$
\left|
\partial_t
\mathcal K_{\rho,N}(t)
\right|
\ll
\frac1{|\rho|}
\sum_{m=N}^{2N-1}
m^\beta N^{-2}
\ll
\frac{N^{\beta-1}}{|\rho|}.
$$

Since

$$
\mathcal K_{\rho,N}(0)=0,
$$

the mean value theorem gives:

## Theorem 8.1 — Centered low-frequency zero response

For

$$
|t|\le1,
$$

$$
\boxed{
|\mathcal K_{\rho,N}(t)|
\ll
|t|
\frac{N^{\beta-1}}{|\rho|}.
}
$$

This removes the apparent $t^{-2}$ singularity in the energy near the bottom of the middle band.

Close:

```text
Z2
CLOSED_AS_EXACT_DISCRETE_CENTERED_ZERO_ORDINATE_RESPONSE_WITH_KUSMIN_LANDAU_LOCALIZATION
```

---

# 9. Zero counting inputs

Let

$$
N_\zeta(T)
$$

denote the number of nontrivial zeta zeros with

$$
0<\gamma\le T
$$

counted with multiplicity.

The Riemann–von Mangoldt formula implies

$$
N_\zeta(T)
=
\frac{T}{2\pi}
\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+
O(\log T).
$$

In particular,

$$
N_\zeta(T)=O(T\log T).
$$

It also gives the unit-interval bound

$$
\boxed{
N_\zeta(U+1)-N_\zeta(U)
\ll
\log(U+2).
}
$$

By partial summation,

$$
\boxed{
\sum_{0<\gamma\le T}
\frac1\gamma
\ll
\log^2(T+2)
}
$$

and

$$
\boxed{
\sum_{\gamma}
\frac1{(1+|\gamma|)^2}
\ll1.
}
$$

Only these coarse zero-counting facts are required for the conditional theorem below.

---

# 10. RH-conditional pointwise control of the finite zero sum

Assume RH in this section only.

Then every nontrivial zero has

$$
\beta=\frac12.
$$

Set

$$
T=N^\kappa,
\qquad
0<\kappa\le1,
$$

and define

$$
\mathfrak Z_{N,T}(t)
=
\sum_{|\gamma|\le T}
\mathcal K_{\rho,N}(t).
$$

## 10.1. The range $|t|\le1$

By Theorem 8.1,

$$
|\mathfrak Z_{N,T}(t)|
\ll
|t|N^{-1/2}
\sum_{|\gamma|\le T}
\frac1{|\rho|}.
$$

The first nontrivial zero has positive ordinate bounded away from zero, so

$$
|\rho|\asymp1+|\gamma|.
$$

Using Section 9,

$$
\boxed{
|\mathfrak Z_{N,T}(t)|
\ll
|t|N^{-1/2}\log^2(T+2).
}
$$

## 10.2. The range $1\le |t|\le T$

By Theorem 7.1,

$$
|\mathfrak Z_{N,T}(t)|
\ll
N^{-1/2}
\sum_{|\gamma|\le T}
\left[
\frac{1+|t|}
{(1+|\gamma|)(1+|\gamma-t|)}
+
\frac1{(1+|\gamma|)^2}
\right].
$$

The second sum is $O(1)$.

For the first sum, decompose the ordinates into unit intervals.

- If $|\gamma|\le |t|/2$, then the factor involving $|\gamma-t|$ reduces the summand to $O((1+|\gamma|)^{-1})$.
- If $|t|/2<\gamma<2|t|$, the factor $(1+|t|)/(1+\gamma)$ is $O(1)$, while unit intervals at distance $j$ from $t$ contribute $O(\log(T+2)/(1+j))$.
- If $\gamma\ge2|t|$, the summand is $O(|t|/\gamma^2)$.
- Negative ordinates satisfy the same or a stronger bound because $|\gamma-t|\asymp |t|+|\gamma|$.

Using the unit-interval zero count,

$$
\boxed{
\sum_{|\gamma|\le T}
\frac{1+|t|}
{(1+|\gamma|)(1+|\gamma-t|)}
\ll
\log^2(T+2).
}
$$

Therefore

$$
\boxed{
|\mathfrak Z_{N,T}(t)|
\ll
N^{-1/2}\log^2(T+2)
}
$$

for

$$
1\le|t|\le T.
$$

---

# 11. RH implies the PK5 middle-band target

Still assuming RH, split the finite-zero energy at $|t|=1$.

For

$$
N^{-\kappa}\le|t|\le1,
$$

Section 10 gives

$$
\frac{
|\mathfrak Z_{N,T}(t)|^2
}{t^2}
\ll
N^{-1}\log^4T.
$$

Hence this range contributes

$$
O(N^{-1}\log^4T).
$$

For

$$
1\le|t|\le T,
$$

$$
|\mathfrak Z_{N,T}(t)|^2
\ll
N^{-1}\log^4T,
$$

and

$$
\int_1^T\frac{dt}{t^2}\le1.
$$

Thus the second range also contributes

$$
O(N^{-1}\log^4T).
$$

Therefore

$$
\boxed{
\int_{\mathcal B_{N,\kappa}}
\frac{
|\mathfrak Z_{N,T}(t)|^2
}{t^2}\,dt
\ll
N^{-1}\log^4N.
}
$$

The explicit-formula remainder from Theorem 4.1 contributes

$$
O(N^{-\kappa}\log^4N).
$$

Since

$$
0<\kappa\le1,
$$

we have

$$
N^{-1}\le N^{-\kappa}.
$$

Using

$$
|F+G|^2\le2|F|^2+2|G|^2,
$$

we obtain:

## Theorem 11.1 — RH-conditional PK5 admission

Assume RH. Then for every fixed

$$
0<\kappa\le1,
$$

$$
\boxed{
\mathcal E_\Lambda(N,\kappa)
\ll
N^{-\kappa}\log^4N
=
N^{-\kappa+o(1)}.
}
$$

Thus the exact centered Mellin / Abel PESC middle-band target is compatible with RH at the full fixed-power scale required by Campaign 44.

This is a conditional theorem only.

Record:

```text
RH_CONDITIONAL_CALIBRATION
PK5_MIDDLE_BAND_ADMISSION
PASS
```

Do **not** create an RH certificate.

---

# 12. What Theorem 11.1 does and does not establish

Theorem 11.1 proves the one-way implication

$$
\boxed{
\mathrm{RH}
\Longrightarrow
\mathrm{PK5\ middle\text{-}band\ admission}.
}
$$

It does not prove the converse

$$
\mathrm{PK5\ admission}
\Longrightarrow
\mathrm{RH}.
$$

It also does not prove PK5 unconditionally.

The reason is now explicit. Without RH, each zero response carries the scale

$$
N^{\beta-1}.
$$

The frequency localization controls

$$
\gamma-t,
$$

but it does not create a negative power in $N$ when $\beta$ is close to $1$.

---

# 13. Classical zero-free regions are not a fixed-power substitute

The classical zero-free region has the qualitative shape

$$
\beta
\le
1-\frac{c}{\log(|\gamma|+2)}
$$

at large height.

At the top of the polynomial window

$$
|\gamma|
\asymp
T
=
N^\kappa,
$$

this gives only

$$
N^{\beta-1}
\le
N^{-c/\log T}
=
e^{-c/\kappa},
$$

which is a constant-scale saving rather than

$$
N^{-\delta}
$$

for a fixed $\delta>0$.

Near

$$
t\asymp\gamma,
$$

the factor

$$
(1+|t|)/(1+|\gamma|)
$$

is also of constant size.

Hence absolute summation of the zero responses combined only with the classical zero-free region cannot yield the required fixed power.

Create:

```text
O-RH-129
CLASSICAL_ZERO_FREE_REGION_PLUS_ABSOLUTE_ZERO_RESPONSE_SUMMATION_HAS_NO_FIXED_POWER
CERTIFIED_AS_PK5_METHOD_BARRIER
```

This obstruction does not exclude cancellation, zero-density amplification, orthogonality, or a more global anti-cancellation argument. It excludes only the naive route.

---

# 14. Z3 is now the exact frontier

After Z1 and Z2, the transform is

$$
\boxed{
\mathfrak L_N(t)
=
-
\sum_{|\gamma|\le N^\kappa}
\mathcal K_{\rho,N}(t)
+
\mathfrak R_{N,N^\kappa}^{\mathrm{EF}}(t),
}
$$

with

$$
\int_{\mathcal B_{N,\kappa}}
\frac{
|\mathfrak R_{N,N^\kappa}^{\mathrm{EF}}(t)|^2
}{t^2}\,dt
\ll
N^{-\kappa+o(1)}.
$$

Therefore the only nontrivial fixed-power object remaining is the zero-window sum itself.

Z3 should now ask:

1. how large can clusters with $|\gamma-t|\lesssim1$ be in the weighted response norm?
2. can zero-density estimates reduce the contribution of $\beta>1/2+\delta$ to a power-admissible level?
3. can cross terms between separated ordinate windows be controlled by an almost-orthogonality inequality?
4. does the exact centering create a positive or coercive Gram structure after pairing conjugate zeros?
5. if an off-critical zero exists, can its response be prevented from being cancelled by the remaining zero ensemble?

The first three are primarily upper-bound questions.

The fifth is the anti-cancellation problem required for a converse or RH implication.

---

# 15. Updated PK5 task order

The next taskpack is:

```text
PK5/Z1 CLOSED
POLYNOMIAL_HEIGHT_EXPLICIT_FORMULA_WITH_MIDDLE_BAND_ADMISSIBLE_REMAINDER

PK5/Z2 CLOSED
EXACT_DISCRETE_CENTERED_ZERO_ORDINATE_RESPONSE_WITH_KUSMIN_LANDAU_LOCALIZATION

PK5/Z3 ACTIVE
ZERO_WINDOW_GRAM_AND_ZERO_DENSITY_CROSS_TERM_AUDIT

PK5/Z4 OPEN
OFF_CRITICAL_ANTI_CANCELLATION_OR_CRITICAL_LINE_ADMISSION
```

Recommended Z3 decomposition:

```text
Z3A UNIT_ORDINATE_CLUSTER_GRAM_BOUND
Z3B SEPARATED_WINDOW_ALMOST_ORTHOGONALITY
Z3C ZERO_DENSITY_WEIGHTED_BETA_LEDGER
Z3D HIGH_ORDINATE_TAIL_AT_FIXED_WINDOW
```

Hard rejections:

```text
DROP_ZERO_ZERO_CROSS_TERMS
ASSUME_SIMPLE_ZEROS
ASSUME_PAIR_CORRELATION
ASSUME_RH
PROMOTE_ZERO_DENSITY_LOG_GAIN_TO_FIXED_POWER
IGNORE_MULTIPLICITY
REPLACE_EXACT_DISCRETE_RESPONSE_BY_CONTINUOUS_MODEL_WITHOUT_ERROR_LEDGER
```

---

# 16. External calibration and sources

The following external results are used as standard inputs or calibration.

## 16.1. Truncated von Mangoldt explicit formula

A standard form is

$$
\psi(x)
=
x
-
\sum_{|\gamma|\le T}
\frac{x^\rho}{\rho}
+
O\left(
\frac{x\log^2(xT)}{T}
+
\log x
\right).
$$

See, for example:

- Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, AMS Graduate Studies in Mathematics, chapter on the explicit formula.
- K. Kedlaya, analytic number theory notes, von Mangoldt explicit formula.

## 16.2. Zero distribution

The Riemann–von Mangoldt formula gives

$$
N_\zeta(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+
O(\log T).
$$

See NIST DLMF Section 25.10 and standard zeta-function texts.

## 16.3. RH and the Chebyshev error

NIST DLMF Section 25.16 records the classical equivalence

$$
\mathrm{RH}
\Longleftrightarrow
\psi(x)
=
x+O(x^{1/2+\varepsilon})
$$

for every $\varepsilon>0$.

The present conditional theorem does not use this pointwise equivalence as its proof. Instead it uses the zero-location statement $\beta=1/2$ directly in the exact response kernel.

## 16.4. Kusmin–Landau

The first derivative estimate for exponential sums is classical. In the form used here, if the derivative of a real phase is monotone and stays a distance $\lambda$ from the integers, the exponential sum is $O(\lambda^{-1})$.

---

# 17. Campaign state transition

Advance the candidate research state from

$$
v1.41
$$

to

$$
v1.42.
$$

Campaign 44 remains active.

Add:

```text
B-RH-044
PESC_CENTERED_ABEL_POLYNOMIAL_HEIGHT_EXPLICIT_FORMULA_WITH_ADMISSIBLE_REMAINDER
CERTIFIED
```

Add:

```text
B-RH-045
PESC_EXACT_DISCRETE_CENTERED_ZERO_ORDINATE_RESPONSE_KERNEL
CERTIFIED
```

Add:

```text
O-RH-129
CLASSICAL_ZERO_FREE_REGION_PLUS_ABSOLUTE_ZERO_RESPONSE_SUMMATION_HAS_NO_FIXED_POWER
CERTIFIED_AS_PK5_METHOD_BARRIER
```

Track state:

```text
PK5 ACTIVE

Z1 CLOSED
Z2 CLOSED
Z3 ACTIVE
Z4 OPEN
```

No root certificate is created.

---

# 18. Conclusion

The zero layer has now been entered rigorously.

The chain is

$$
\boxed{
\begin{aligned}
\text{centered PESC root energy}
&\longleftrightarrow
\text{centered Mellin middle band}
\\
&\longleftrightarrow
\text{centered von Mangoldt transform}
\\
&=
\text{centered Abel transform of }\psi-m
\\
&=
-
\sum_{|\gamma|\le N^\kappa}
\mathcal K_{\rho,N}
+
\text{power-admissible remainder}.
\end{aligned}
}
$$

The response of each zero is finite, discrete, centered, and exactly ordinate-aligned:

$$
m^{i(\gamma-t)}.
$$

Under RH the entire zero ensemble satisfies the required middle-band fixed-power estimate using only coarse zero counting and Kusmin–Landau localization.

Unconditionally, the truncation and single-zero geometry are no longer the bottleneck.

The bottleneck is now the ensemble:

$$
\boxed{
\text{zero-window Gram structure}
+
\text{zero-density weighting}
+
\text{off-critical anti-cancellation}.
}
$$

That is the exact mathematical content of PK5/Z3–Z4.
