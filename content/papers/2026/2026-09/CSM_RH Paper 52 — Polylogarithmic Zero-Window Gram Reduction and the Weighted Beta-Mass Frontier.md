# CSM_RH Paper 52

## Polylogarithmic Zero-Window Gram Reduction and the Weighted Beta-Mass Frontier

**Project:** CSM_RH  
**Paper:** 52  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 44 — `PESC_TRIANGULAR_LAG_KERNEL_ATTACK`  
**Track:** PK5 — `FIXED_POWER_PESC_ADMISSION`  
**Subtrack:** Z3 — `ZERO_WINDOW_GRAM_AND_ZERO_DENSITY_CROSS_TERM_AUDIT`  
**Status:** Z3 CLOSURE CANDIDATE / Z4 NEXT  
**Canonical entry state:** v1.42 / Paper 51 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 51 inserted the truncated zeta explicit formula into the exact centered Abel representation of the PESC root statistic and extracted the discrete zero response

$$
\mathcal K_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^\rho
\Delta g_{N,t}(m),
$$

with exact ordinate phase

$$
m^{i(\gamma-t)}
$$

for

$$
\rho=\beta+i\gamma.
$$

It also proved that, for

$$
|t|\le N,
\qquad
|\gamma|\le N,
$$

$$
|\mathcal K_{\rho,N}(t)|
\ll
N^{\beta-1}
\left[
\frac{1+|t|}
{|\rho|(1+|\gamma-t|)}
+
\frac1{|\rho|(1+|\gamma|)}
\right].
$$

The unresolved question was whether zero-zero cross terms could themselves create a power-sized loss when the responses are summed over all zeros up to height

$$
T=N^\kappa.
$$

This paper proves that they do not.

After dividing by the PESC energy weight $|t|$, each zero response on $|t|\ge1$ is dominated by a Cauchy-type ordinate window centered at $\gamma$ with coefficient

$$
\frac{N^{\beta-1}}{1+|\gamma|}.
$$

The Gram kernel of two such windows satisfies

$$
\int_{\mathbb R}
\frac{dt}
{(1+|t-\gamma|)(1+|t-\gamma'|)}
\ll
\frac{\log(2+|\gamma-\gamma'|)}
{1+|\gamma-\gamma'|}.
$$

The Riemann-von Mangoldt local zero count implies that each unit ordinate interval contains only $O(\log T)$ zeros, counted with multiplicity. A Schur row-sum argument then yields only

$$
O(\log^3T)
$$

loss for the complete separated-window Gram operator.

The low-frequency range $|t|\le1$ is treated separately. Differentiating the exact centered zero response and using the same Kusmin-Landau localization gives

$$
\sup_{|s|\le1}
|\partial_s\mathcal K_{\rho,N}(s)|
\ll
\frac{N^{\beta-1}}
{(1+|\gamma|)^2}
$$

up to an absolute finite-low-zero adjustment. Since

$$
\mathcal K_{\rho,N}(0)=0,
$$

the low-frequency channel also has only a bounded Gram cost.

Consequently the entire finite-zero contribution satisfies

$$
\boxed{
\int_{N^{-\kappa}\le|t|\le T}
\frac{
\left|
\sum_{|\gamma|\le T}
\mathcal K_{\rho,N}(t)
\right|^2
}{t^2}\,dt
\ll
(\log T)^3
\mathfrak D_N(T),
}
$$

where

$$
\boxed{
\mathfrak D_N(T)
=
\sum_{|\gamma|\le T}
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}.
}
$$

Thus all power-scale risk in Z3 is concentrated in the real parts $\beta$ ; ordinate clustering and separated-window interference cost only polylogarithms.

The weighted beta mass has an exact layer-cake representation. If

$$
\mathfrak Z_w(\sigma,T)
=
\sum_{\substack{|\gamma|\le T\\\beta\ge\sigma}}
\frac1{(1+|\gamma|)^2},
$$

then

$$
\boxed{
\mathfrak D_N(T)
=
O(N^{-1})
+
2\log N
\int_{1/2}^1
N^{2\sigma-2}
\mathfrak Z_w(\sigma,T)\,d\sigma.
}
$$

The uppermost ordinate shell is automatically admissible:

$$
\sum_{Y\le|\gamma|\le2Y}
\frac{N^{2\beta-2}}{(1+|\gamma|)^2}
\ll
\frac{\log Y}{Y}.
$$

In particular, with $T=N^\kappa$, zeros with

$$
|\gamma|
\ge
\frac{T}{(\log N)^A}
$$

contribute only

$$
N^{-\kappa+o(1)}.
$$

Classical Ingham-Huxley zero-density estimates can refine the weighted ledger, but they do not exclude even one fixed off-critical zero. Therefore zero density by itself cannot certify the endpoint $\kappa=1$ weighted-beta condition. Z3 is closed as an ordinate-geometry reduction, and Z4 becomes the unique remaining PK5 frontier: off-critical anti-cancellation or critical-line admission.

No RH theorem is claimed.

---

# 1. Entry from Paper 51

Paper 51 gave

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
T=N^\kappa
$$

and

$$
\int_{\mathcal B_{N,\kappa}}
\frac{
|\mathfrak R_{N,T}^{\mathrm{EF}}(t)|^2
}{t^2}\,dt
\ll
N^{-\kappa+o(1)}.
$$

Therefore PK5 reduces to the finite-zero sum

$$
\mathfrak Z_{N,T}(t)
=
\sum_{|\gamma|\le T}
\mathcal K_{\rho,N}(t).
$$

The inherited response estimate is

$$
|\mathcal K_{\rho,N}(t)|
\ll
N^{\beta-1}
\left[
\frac{1+|t|}
{|\rho|(1+|\gamma-t|)}
+
\frac1{|\rho|(1+|\gamma|)}
\right].
$$

The exact centering condition is

$$
\mathcal K_{\rho,N}(0)=0.
$$

The task of Z3 is to price all cross-zero interactions without assuming simple zeros, pair correlation, or RH.

---

# 2. Weighted response normalization

Define

$$
F_{\rho,N}(t)
=
\frac{
\mathcal K_{\rho,N}(t)
}{t}
$$

for $t\ne0$.

For nontrivial zeros,

$$
|\rho|
\asymp
1+|\gamma|
$$

uniformly up to an absolute constant, after absorbing the finite low-ordinate set.

For

$$
|t|\ge1,
$$

Paper 51 therefore gives

$$
\boxed{
|F_{\rho,N}(t)|
\ll
\frac{
N^{\beta-1}
}{
1+|\gamma|
}
\frac1{1+|\gamma-t|}
+
\frac{
N^{\beta-1}
}{
(1+|\gamma|)^2
}
\frac1{|t|}.
}
$$

Set

$$
b_\rho
=
\frac{
N^{\beta-1}
}{
1+|\gamma|
}
$$

and

$$
c_\rho
=
\frac{
N^{\beta-1}
}{
(1+|\gamma|)^2
}.
$$

The first term is the localized ordinate window. The second is a rank-one integrable tail.

---

# 3. A convolution lemma for ordinate windows

Let

$$
h(x)
=
\frac1{1+|x|}.
$$

For $d\ge0$, define

$$
\mathcal H(d)
=
\int_{\mathbb R}
h(x)h(x-d)\,dx.
$$

## Lemma 3.1 — Cauchy-window convolution

For all $d\ge0$,

$$
\boxed{
\mathcal H(d)
\ll
\frac{
\log(2+d)
}{
1+d
}.
}
$$

### Proof

For $d\le2$, the integral is $O(1)$.

Assume $d>2$ and split the real line into

$$
(-\infty,0],
\qquad
[0,d],
\qquad
[d,\infty).
$$

On the middle interval,

$$
\frac1{(1+x)(1+d-x)}
=
\frac1{d+2}
\left[
\frac1{1+x}
+
\frac1{1+d-x}
\right].
$$

Hence

$$
\int_0^d
\frac{dx}
{(1+x)(1+d-x)}
=
\frac{
2\log(1+d)
}{
d+2
}.
$$

On each exterior interval, one denominator is at least $1+d$ at the endpoint scale, and direct integration gives the same order

$$
O\left(
\frac{\log(2+d)}{1+d}
\right).
$$

Summing the three pieces proves the lemma.

$$
\Box
$$

Thus the Gram interaction of two separated ordinate windows decays almost like $1/|\gamma-\gamma'|$, with only one logarithm.

---

# 4. Unit-ordinate zero clusters

Let

$$
\Gamma_T
=
\left\{
\gamma:
\zeta(\beta+i\gamma)=0,
\ |\gamma|\le T
\right\},
$$

counted with multiplicity.

For an integer $j$, define the unit cluster

$$
\mathcal C_j
=
\left\{
\rho:
j\le\gamma<j+1
\right\}.
$$

The Riemann-von Mangoldt formula implies

$$
\boxed{
\#\mathcal C_j
\ll
\log(T+2)
}
$$

uniformly for

$$
|j|\le T+1.
$$

This count includes multiplicity.

If two zeros lie in the same unit cluster, Lemma 3.1 gives an $O(1)$ Gram interaction.

Therefore, for an arbitrary set of complex coefficients $u_\rho$ supported on one cluster,

$$
\left\|
\sum_{\rho\in\mathcal C_j}
u_\rho
h(\,\cdot-\gamma_\rho)
\right\|_2^2
\ll
\log(T+2)
\sum_{\rho\in\mathcal C_j}
|u_\rho|^2.
$$

This closes the local multiplicity problem.

Create:

```text
B-RH-046A
PESC_UNIT_ORDINATE_ZERO_CLUSTER_GRAM_BOUND
CERTIFIED
```

Close:

```text
Z3A
CLOSED_AS_UNIT_ORDINATE_CLUSTER_COST_ONLY_LOGARITHMIC
```

---

# 5. Separated-window Schur bound

For two zeros $\rho,\rho'$, define

$$
G_{\rho,\rho'}
=
\mathcal H
\left(
|\gamma-\gamma'|
\right).
$$

By Lemma 3.1,

$$
G_{\rho,\rho'}
\ll
\frac{
\log(2+|\gamma-\gamma'|)
}{
1+|\gamma-\gamma'|
}.
$$

Fix one zero ordinate $\gamma$. Group all other ordinates according to

$$
n
\le
|\gamma-\gamma'|
<
n+1.
$$

Each such shell intersects only $O(1)$ unit ordinate intervals, each containing

$$
O(\log(T+2))
$$

zeros.

Hence the row sum satisfies

$$
\begin{aligned}
\sum_{|\gamma'|\le T}
G_{\rho,\rho'}
&\ll
\log(T+2)
\sum_{0\le n\le2T+2}
\frac{\log(2+n)}{1+n}
\\
&\ll
\boxed{
\log^3(T+2)
}.
\end{aligned}
$$

The same estimate holds for column sums.

By the Schur test:

## Theorem 5.1 — Separated-window almost orthogonality

For arbitrary complex coefficients $u_\rho$,

$$
\boxed{
\int_{\mathbb R}
\left|
\sum_{|\gamma|\le T}
u_\rho
h(t-\gamma)
\right|^2dt
\ll
\log^3(T+2)
\sum_{|\gamma|\le T}
|u_\rho|^2.
}
$$

No pair-correlation hypothesis is used.

No simplicity assumption is used.

Create:

```text
B-RH-046B
PESC_SEPARATED_ZERO_WINDOW_SCHUR_ALMOST_ORTHOGONALITY
CERTIFIED
```

Close:

```text
Z3B
CLOSED_AS_SEPARATED_ORDINATE_WINDOWS_WITH_POLYLOG_GRAM_COST
```

---

# 6. The rank-one high-frequency tail

The second term in Section 2 contributes, on $|t|\ge1$,

$$
\sum_\rho
\frac{c_\rho}{|t|}.
$$

Therefore

$$
\int_{|t|\ge1}
\left|
\sum_\rho
\frac{c_\rho}{|t|}
\right|^2dt
\ll
\left(
\sum_\rho c_\rho
\right)^2.
$$

Now

$$
c_\rho
=
b_\rho
\frac1{1+|\gamma|}.
$$

By Cauchy,

$$
\left(
\sum_\rho c_\rho
\right)^2
\le
\left(
\sum_\rho b_\rho^2
\right)
\left(
\sum_\rho
\frac1{(1+|\gamma|)^2}
\right).
$$

The second zero sum converges because

$$
N_\zeta(U)=O(U\log U).
$$

Thus

$$
\boxed{
\int_{|t|\ge1}
\left|
\sum_\rho
\frac{c_\rho}{|t|}
\right|^2dt
\ll
\sum_\rho b_\rho^2.
}
$$

The nonlocalized tail is therefore harmless at power scale.

---

# 7. Refined derivative localization at low frequency

Paper 51 used the coarse centered estimate

$$
|\mathcal K_{\rho,N}(t)|
\ll
|t|
\frac{N^{\beta-1}}{|\rho|}.
$$

For the zero ensemble, we need one additional ordinate decay.

Differentiate the exact response:

$$
\partial_t
\mathcal K_{\rho,N}(t)
=
\frac1\rho
\sum_{m=N}^{2N-1}
m^\rho
\Delta
\left(
\partial_t g_{N,t}
\right)(m).
$$

Now

$$
\partial_t g_{N,t}(x)
=
i
\log\frac{2N}{x}
\frac{
(2N/x)^{it}
}{x}.
$$

The centered logarithm satisfies

$$
0
\le
\log\frac{2N}{x}
\le
\log2
$$

on

$$
N\le x\le2N.
$$

For $|t|\le1$, write

$$
m^\rho
\Delta
\left(
\partial_t g_{N,t}
\right)(m)
=
i(2N)^{it}
m^{\rho-1-it}
r_t(m),
$$

where

$$
r_t(m)
=
\log\frac{2N}{m}
-
\left(
\frac{m}{m+1}
\right)^{1+it}
\log\frac{2N}{m+1}.
$$

A direct derivative estimate gives

$$
|r_t(x)|
\ll
x^{-1}
$$

and

$$
|r_t'(x)|
\ll
x^{-2}
$$

uniformly for

$$
N\le x\le2N,
\qquad
|t|\le1.
$$

Apply the same Kusmin-Landau plus partial-summation argument as in Paper 51 to the phase

$$
m^{i(\gamma-t)}.
$$

For all but the finite low-ordinate set,

$$
|\gamma-t|
\asymp
1+|\gamma|.
$$

Hence

$$
\boxed{
\sup_{|t|\le1}
\left|
\partial_t
\mathcal K_{\rho,N}(t)
\right|
\ll
\frac{
N^{\beta-1}
}{
(1+|\gamma|)^2
}.
}
$$

The finite exceptional low-ordinate set is absorbed into the absolute constant.

Since

$$
\mathcal K_{\rho,N}(0)=0,
$$

we obtain:

## Theorem 7.1 — Low-frequency ensemble-ready response

For

$$
|t|\le1,
$$

$$
\boxed{
\frac{
|\mathcal K_{\rho,N}(t)|
}{
|t|
}
\ll
\frac{
N^{\beta-1}
}{
(1+|\gamma|)^2
}.
}
$$

This additional ordinate decay is a direct consequence of centering. The logarithm is $\log(2N/x)$, not $\log x$, so no $\log N$ loss appears.

---

# 8. Low-frequency cross terms are bounded

By Theorem 7.1,

$$
\int_{N^{-\kappa}\le|t|\le1}
\frac{
\left|
\sum_\rho
\mathcal K_{\rho,N}(t)
\right|^2
}{t^2}\,dt
\ll
\left(
\sum_\rho c_\rho
\right)^2.
$$

Section 6 already proved

$$
\left(
\sum_\rho c_\rho
\right)^2
\ll
\sum_\rho b_\rho^2.
$$

Therefore

$$
\boxed{
\int_{N^{-\kappa}\le|t|\le1}
\frac{
\left|
\sum_\rho
\mathcal K_{\rho,N}(t)
\right|^2
}{t^2}\,dt
\ll
\sum_\rho
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}.
}
$$

The low-frequency channel is therefore not a hidden coherent rank-one power obstruction.

---

# 9. Main Z3 Gram reduction theorem

Define the weighted beta mass

$$
\boxed{
\mathfrak D_N(T)
=
\sum_{|\gamma|\le T}
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}.
}
$$

Combine Sections 5–8.

## Theorem 9.1 — Polylogarithmic zero-ensemble Gram reduction

For

$$
2\le T\le N,
$$

$$
\boxed{
\int_{T^{-1}\le|t|\le T}
\frac{
\left|
\sum_{|\gamma|\le T}
\mathcal K_{\rho,N}(t)
\right|^2
}{t^2}\,dt
\ll
\log^3(T+2)
\mathfrak D_N(T).
}
$$

More generally, for the Campaign 44 band

$$
N^{-\kappa}
\le
|t|
\le
N^\kappa
$$

with

$$
T=N^\kappa,
$$

$$
\boxed{
\mathcal E_{\mathrm{zeros}}(N,\kappa)
\ll
(\log N)^3
\mathfrak D_N(N^\kappa).
}
$$

Thus zero-zero cross terms cost only $N^{o(1)}$.

Create:

```text
B-RH-046
PESC_ZERO_ENSEMBLE_POLYLOG_GRAM_REDUCTION_TO_WEIGHTED_BETA_MASS
CERTIFIED
```

This is the central Z3 result.

---

# 10. Exact weighted zero-density layer cake

Define

$$
\boxed{
\mathfrak Z_w(\sigma,T)
=
\sum_{\substack{|\gamma|\le T\\\beta\ge\sigma}}
\frac1{(1+|\gamma|)^2}.
}
$$

Zeros with

$$
\beta<\frac12
$$

contribute only

$$
O(N^{-1})
$$

to $\mathfrak D_N(T)$, because

$$
N^{2\beta-2}\le N^{-1}
$$

and

$$
\sum_\rho
(1+|\gamma|)^{-2}
<
\infty.
$$

For

$$
\beta\ge\frac12,
$$

the identity

$$
N^{2\beta-2}
=
N^{-1}
+
2\log N
\int_{1/2}^{\beta}
N^{2\sigma-2}\,d\sigma
$$

holds exactly.

Summing over zeros and applying Tonelli to the nonnegative integrand gives:

## Theorem 10.1 — Weighted beta layer-cake identity

$$
\boxed{
\mathfrak D_N(T)
=
O(N^{-1})
+
2\log N
\int_{1/2}^{1}
N^{2\sigma-2}
\mathfrak Z_w(\sigma,T)\,d\sigma.
}
$$

The implicit $O(N^{-1})$ contains the $\beta<1/2$ contribution and the baseline $\beta\ge1/2$ term.

Create:

```text
B-RH-047
PESC_WEIGHTED_BETA_MASS_EXACT_LAYER_CAKE_LEDGER
CERTIFIED
```

This closes the algebraic part of Z3C.

---

# 11. A sufficient weighted zero-density criterion

Theorem 9.1 immediately gives:

## Corollary 11.1

If

$$
\boxed{
\mathfrak D_N(N^\kappa)
\ll
N^{-\kappa+o(1)},
}
$$

then

$$
\boxed{
\mathcal E_{\mathrm{zeros}}(N,\kappa)
\ll
N^{-\kappa+o(1)}.
}
$$

Together with the explicit-formula remainder from Paper 51, this implies the complete PK5 middle-band target.

A simple stronger sufficient condition is

$$
\beta
\le
1-\frac{\kappa}{2}
$$

for every zero with

$$
|\gamma|\le N^\kappa.
$$

Indeed,

$$
N^{2\beta-2}
\le
N^{-\kappa},
$$

and the ordinate weight is summable.

At

$$
\kappa=1,
$$

this condition becomes

$$
\beta\le\frac12.
$$

By functional-equation symmetry, that is exactly the critical-line condition for the truncated zero set.

This does not prove the condition. It identifies the exponent geometry of PK5.

---

# 12. Upper ordinate shells are automatically admissible

For

$$
Y\ge2,
$$

Riemann-von Mangoldt gives

$$
\#\{
\rho:
Y\le|\gamma|\le2Y
\}
\ll
Y\log Y.
$$

Since

$$
N^{2\beta-2}\le1,
$$

we have:

## Theorem 12.1 — High-ordinate shell bound

$$
\boxed{
\sum_{\substack{
Y\le|\gamma|\le2Y
}}
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}
\ll
\frac{\log Y}{Y}.
}
$$

Consequently,

$$
\boxed{
\sum_{|\gamma|\ge Y}
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}
\ll
\frac{\log(Y+2)}{Y}.
}
$$

Take

$$
T=N^\kappa
$$

and

$$
Y=
\frac{
T
}{
(\log N)^A
}.
$$

Then

$$
\boxed{
\sum_{Y\le|\gamma|\le T}
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}
\ll
N^{-\kappa}
(\log N)^{A+1}.
}
$$

Thus the uppermost polynomial ordinate shell is fixed-power admissible without any information about $\beta$ beyond $\beta<1$.

Create:

```text
B-RH-048
PESC_TOP_ORDINATE_SHELL_FIXED_POWER_ADMISSIBILITY
CERTIFIED
```

Close:

```text
Z3D
CLOSED_AS_TOP_POLYNOMIAL_ORDINATE_SHELL_AUTOMATICALLY_ADMISSIBLE
```

The remaining dangerous mass lies below the top ordinate shell and is controlled by the real parts.

---

# 13. Classical zero-density calibration

Classical zero-density estimates have the form

$$
N_\zeta(\sigma,U)
\ll
U^{A(\sigma)(1-\sigma)}
(\log U)^B.
$$

Two standard examples are:

For

$$
\frac12\le\sigma<\frac34,
$$

Ingham gives the exponent

$$
\frac{
3(1-\sigma)
}{
2-\sigma
}.
$$

For

$$
\frac34\le\sigma<1,
$$

Huxley gives

$$
\frac{
3(1-\sigma)
}{
3\sigma-1
}.
$$

These estimates imply strong rarity of zeros to the right of a fixed vertical line and are more than sufficient to make many weighted height sums converge.

However, zero-density estimates count exceptional zeros. They do not exclude a finite exceptional set.

The weighted beta criterion is sensitive to even one fixed off-critical zero.

Suppose

$$
\rho_0=\beta_0+i\gamma_0
$$

is fixed. Once

$$
T>|\gamma_0|,
$$

its contribution to $\mathfrak D_N(T)$ is

$$
\frac{
N^{2\beta_0-2}
}{
(1+|\gamma_0|)^2
}.
$$

For the endpoint

$$
\kappa=1,
$$

if

$$
\beta_0>\frac12,
$$

then

$$
N^{2\beta_0-2}
\gg
N^{-1}.
$$

Thus no zero-density theorem that still permits even one fixed off-critical zero can by itself certify

$$
\mathfrak D_N(N)
\ll
N^{-1+o(1)}.
$$

More generally, for fixed $\kappa$ a zero with

$$
\beta_0>
1-\frac{\kappa}{2}
$$

violates the simple weighted-beta sufficient condition.

Create:

```text
O-RH-130
CLASSICAL_ZERO_DENSITY_ALONE_CANNOT_CERTIFY_ENDPOINT_WEIGHTED_BETA_MASS
CERTIFIED_AS_Z3C_METHOD_BARRIER
```

This is a method barrier, not a theorem that PK5 fails.

---

# 14. Why the classical zero-free region also remains subpower

A classical zero-free region has the qualitative form

$$
\beta
\le
1-\eta(|\gamma|),
$$

where

$$
\eta(U)\to0
$$

as

$$
U\to\infty.
$$

Even after the ordinate weight

$$
(1+|\gamma|)^{-2}
$$

is included, such a shrinking strip does not produce a uniform fixed power in $N$ for all intermediate subpolynomial heights.

For the elementary de la Vallee Poussin shape

$$
\eta(U)
\asymp
\frac1{\log U},
$$

inverting the zero-free region and balancing the factors

$$
N^{-2(1-\beta)}
$$

and

$$
|\gamma|^{-2}
$$

produces a subpower exponential scale rather than

$$
N^{-\delta}
$$

with fixed $\delta>0$.

Stronger classical zero-free regions improve this subpower scale, but the same structural issue remains: their distance from $\Re s=1$ tends to zero.

This is fully consistent with Paper 51 obstruction O-RH-129.

---

# 15. Z3C closure

The purpose of Z3C was not to prove RH or the PK5 endpoint directly. It was to identify exactly how zero-density information enters after cross terms are priced.

That ledger is now complete:

$$
\boxed{
\mathcal E_{\mathrm{zeros}}
\ll
N^{o(1)}
\mathfrak D_N(T)
}
$$

and

$$
\boxed{
\mathfrak D_N(T)
=
O(N^{-1})
+
2\log N
\int_{1/2}^{1}
N^{2\sigma-2}
\mathfrak Z_w(\sigma,T)\,d\sigma.
}
$$

Classical zero-density estimates can be inserted into $\mathfrak Z_w$, but they do not remove finite exceptional off-critical zeros.

Close:

```text
Z3C
CLOSED_AS_EXACT_WEIGHTED_BETA_DENSITY_LEDGER_WITH_CLASSICAL_DENSITY_METHOD_BARRIER
```

---

# 16. Complete Z3 closure

All four Z3 subtasks have now been resolved.

```text
Z3A CLOSED
UNIT_ORDINATE_CLUSTER_COST_ONLY_LOGARITHMIC

Z3B CLOSED
SEPARATED_ORDINATE_WINDOWS_WITH_POLYLOG_GRAM_COST

Z3C CLOSED
EXACT_WEIGHTED_BETA_DENSITY_LEDGER_WITH_CLASSICAL_DENSITY_METHOD_BARRIER

Z3D CLOSED
TOP_POLYNOMIAL_ORDINATE_SHELL_AUTOMATICALLY_ADMISSIBLE
```

Therefore close Z3 as:

```text
CLOSED_AS_ZERO_ORDINATE_GEOMETRY_REDUCED_WITH_ONLY_POLYLOG_LOSS_TO_WEIGHTED_BETA_MASS
```

PK5 remains open.

---

# 17. The exact Z4 frontier

After Papers 51 and 52, the explicit-formula zero contribution has the power-safe upper reduction

$$
\mathcal E_{\mathrm{zeros}}
\ll
N^{o(1)}
\sum_{|\gamma|\le N^\kappa}
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}.
$$

No remaining $N^\delta$ cost comes from:

- unit zero multiplicity;
- separated ordinate windows;
- high-frequency rank-one tails;
- low-frequency centering;
- explicit-formula truncation;
- the uppermost ordinate shell.

The only remaining power exponent is

$$
\boxed{
2\beta-2.
}
$$

Thus Z4 is now exactly:

```text
OFF_CRITICAL_ANTI_CANCELLATION_OR_CRITICAL_LINE_ADMISSION
```

There are two logically distinct routes.

## Route Z4-A — Upper admission

Prove directly that the actual weighted beta ensemble satisfies enough cancellation or structure to force

$$
\mathcal E_{\mathrm{zeros}}
\ll
N^{-\kappa+o(1)}
$$

without assuming RH.

## Route Z4-B — Converse detection

Prove that an off-critical zero with sufficiently large $\beta$ creates a coercive response that cannot be cancelled by the rest of the zero ensemble.

For $\kappa=1$, a successful global version of Z4-B would connect the PESC middle-band endpoint directly to the critical line.

Neither route is proved here.

---

# 18. Recommended Z4 attack order

The next campaign taskpack should be:

```text
Z4A FUNCTIONAL_EQUATION_SAME_ORDINATE_PAIR_AUDIT
Z4B CONTINUOUS_RESPONSE_LIMIT_WITH_UNIFORM_DISCRETE_ERROR
Z4C FINITE_CLUSTER_LOWER_GRAM_OR_RESPONSE_LINEAR_INDEPENDENCE
Z4D HIGH_ORDINATE_CONTAMINATION_TAIL_IN_FIXED_TEST_WINDOW
Z4E OFF_CRITICAL_DOMINANT_BETA_ANTI_CANCELLATION
```

The first object to exploit is the functional-equation partner:

If

$$
\rho=\beta+i\gamma
$$

is a zero, then

$$
1-\overline\rho
=
1-\beta+i\gamma
$$

is also a zero.

Their $N$ scales are

$$
N^{\beta-1}
$$

and

$$
N^{-\beta}.
$$

If

$$
\beta>\frac12,
$$

the ratio is

$$
N^{2\beta-1}.
$$

Thus the same-ordinate reflected partner is power-smaller than the right-hand zero. This does not yet prove anti-cancellation against all other zeros, but it eliminates one apparent symmetry-based cancellation mechanism.

This is the natural starting point for Paper 53.

---

# 19. External calibration

The external results used as standard inputs are:

1. **Riemann-von Mangoldt zero counting and critical-strip symmetry**  
   NIST Digital Library of Mathematical Functions, Section 25.10.  
   https://dlmf.nist.gov/25.10

2. **Ingham-Huxley zero-density estimates**  
   Classical zero-density theory; see Iwaniec-Kowalski, *Analytic Number Theory*, Chapter 10, and the corresponding lecture reproduction:  
   https://wiki.math.ntnu.no/_media/ma3001/2025h/analyticnumbertheory/ik_chapter_10.pdf

3. **Kusmin-Landau first derivative estimate**  
   Used already in Paper 51 for the discrete zero response and again here for the differentiated centered kernel.  
   https://androma.org/theorems/9055

These are calibration and standard analytic inputs. No density hypothesis, pair-correlation conjecture, Lindelof hypothesis, or RH is assumed.

---

# 20. Campaign state transition

Advance the candidate state from

$$
v1.42
$$

to

$$
v1.43.
$$

Add:

```text
B-RH-046
PESC_ZERO_ENSEMBLE_POLYLOG_GRAM_REDUCTION_TO_WEIGHTED_BETA_MASS
CERTIFIED
```

Add:

```text
B-RH-047
PESC_WEIGHTED_BETA_MASS_EXACT_LAYER_CAKE_LEDGER
CERTIFIED
```

Add:

```text
B-RH-048
PESC_TOP_ORDINATE_SHELL_FIXED_POWER_ADMISSIBILITY
CERTIFIED
```

Add:

```text
O-RH-130
CLASSICAL_ZERO_DENSITY_ALONE_CANNOT_CERTIFY_ENDPOINT_WEIGHTED_BETA_MASS
CERTIFIED_AS_Z3C_METHOD_BARRIER
```

Track state:

```text
PK5 ACTIVE

Z1 CLOSED
Z2 CLOSED
Z3 CLOSED
Z4 ACTIVE
```

No root certificate is created.

---

# 21. Conclusion

The zero ensemble has now been separated into geometry and exponent.

The geometry is benign at fixed-power scale:

$$
\boxed{
\text{ordinate clustering}
+
\text{separated-window cross terms}
=
N^{o(1)}.
}
$$

The exponent is not:

$$
\boxed{
N^{2\beta-2}.
}
$$

The complete Z3 reduction is

$$
\boxed{
\mathcal E_{\mathrm{zeros}}
\ll
(\log N)^3
\sum_{|\gamma|\le N^\kappa}
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}.
}
$$

Thus Campaign 44 has reached a sharply defined frontier.

The remaining question is no longer whether many zero responses overlap.

It is whether off-critical real-part mass can be admitted by a new cancellation mechanism or, conversely, whether an off-critical response can be shown to survive every allowed cancellation.

That is Z4.
