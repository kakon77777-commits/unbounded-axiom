# CSM_RH Paper 43
## Liouville Sign Collapse, Determinant Fibres, and Polynomial Erosion of the Low-Variation Shift Shell

**Project:** CSM_RH  
**Paper:** 43  
**Version:** 0.1  
**Date:** 2026-09-07  
**Campaign:** 42 — `OSCILLATORY_MOBIUS_CONVOLUTION_SHIFT_ATTACK`  
**Canonical state transition:** v1.33 to v1.34

---

# 0. Trust boundary

This paper continues directly from CSM_RH Paper 42.

The inherited pure-core coefficient is

$$
c_X(n)
=
\sum_{\substack{m_1\cdots m_L=n\\m_i\sim U_i}}
\mu(m_1)\cdots\mu(m_L),
$$

with

$$
\prod_{i=1}^{L}U_i\asymp X,
$$

and the remaining translated-window obstruction is

$$
\mathfrak R_{\mathrm{osc}}(Q,Y)
=
Y
\sum_{X/Q<h\lesssim X^{o(1)}X/Y}
\sum_m
\frac{c_X(m)c_X(m+h)}{m(m+h)}
 e^{iQ\log(1+h/m)}
\widehat\Phi\!\left(Y\log(1+h/m)\right).
$$

The large-major-arc geometry inherited from Paper 42 gives

$$
\frac{Y}{Q}
\ll
X^{3w/10-\varepsilon/2},
$$

where

$$
W=X^w,
\qquad
0<w\le\frac{\varepsilon}{1000}.
$$

The polynomial- $W$ admission target remains

$$
\boxed{
|\mathfrak R_{\mathrm{osc}}(Q,Y)|
\ll
X^{-3w/10+o(1)}.
}
$$

No claim of RH, no fixed zero-free strip, and no pointwise fixed-power Mertens estimate is made.

This paper performs three tasks:

1. close Campaign 42 track OM1 algebraically;
2. sharpen OM2 by removing a much larger low-variation shift shell;
3. identify the exact remaining arithmetic object as a structured weighted Liouville correlation on determinant fibres.

---

# 1. Exact Liouville sign collapse

Let

$$
\lambda(n)=(-1)^{\Omega(n)}
$$

be the Liouville function.

For every integer $m\ge1$,

$$
\boxed{
\mu(m)=\lambda(m)\mu^2(m).
}
$$

Indeed, if $m$ is not squarefree then both sides vanish, while if $m$ is squarefree then

$$
\mu(m)=(-1)^{\Omega(m)}=\lambda(m).
$$

Define the nonnegative restricted squarefree-factorisation weight

$$
\boxed{
r_X(n)
=
\sum_{\substack{m_1\cdots m_L=n\\m_i\sim U_i}}
\mu^2(m_1)\cdots\mu^2(m_L).
}
$$

Since $\lambda$ is completely multiplicative,

$$
\lambda(m_1)\cdots\lambda(m_L)
=
\lambda(m_1\cdots m_L)
=
\lambda(n).
$$

Therefore every nonzero summand in $c_X(n)$ has the same sign.

## Theorem 1.1 — Pure-core Liouville factorisation

For every $n$,

$$
\boxed{
c_X(n)=\lambda(n)r_X(n),
\qquad
r_X(n)\ge0.
}
$$

### Proof

Using $\mu(m)=\lambda(m)\mu^2(m)$,

$$
\begin{aligned}
c_X(n)
&=
\sum_{m_1\cdots m_L=n}
\prod_{i=1}^{L}\lambda(m_i)\mu^2(m_i)\\
&=
\lambda(n)
\sum_{m_1\cdots m_L=n}
\prod_{i=1}^{L}\mu^2(m_i)\\
&=
\lambda(n)r_X(n).
\end{aligned}
$$

The dyadic restrictions are unchanged throughout.  
 $\square$

Create:

```text
B-RH-017
PURE_MOBIUS_CORE_LIOUVILLE_SIGN_FACTORISATION
status:
  CERTIFIED EXACT IDENTITY
```

This materially changes the interpretation of the pure core.

It is not an internally cancelling high-order Möbius convolution.
Its complete sign is carried by one Liouville value, while the convolution multiplicity is nonnegative.

---

# 2. Grouped Type-II coefficients inherit the same sign rigidity

Let $I\sqcup J=\{1,\ldots,L\}$ be a Type-II partition.

Define

$$
\alpha_I(u)
=
\sum_{\substack{\prod_{i\in I}m_i=u\\m_i\sim U_i}}
\prod_{i\in I}\mu(m_i),
$$

and

$$
\beta_J(v)
=
\sum_{\substack{\prod_{j\in J}m_j=v\\m_j\sim U_j}}
\prod_{j\in J}\mu(m_j).
$$

Then

$$
c_X=\alpha_I*\beta_J.
$$

Define the nonnegative weights

$$
r_I(u)
=
\sum_{\substack{\prod_{i\in I}m_i=u\\m_i\sim U_i}}
\prod_{i\in I}\mu^2(m_i),
$$

$$
r_J(v)
=
\sum_{\substack{\prod_{j\in J}m_j=v\\m_j\sim U_j}}
\prod_{j\in J}\mu^2(m_j).
$$

Exactly as above,

$$
\boxed{
\alpha_I(u)=\lambda(u)r_I(u),
\qquad
\beta_J(v)=\lambda(v)r_J(v).
}
$$

Hence

$$
\lambda(u)\lambda(v)=\lambda(uv),
$$

so the Type-II grouping does not create new independent sign carriers.

The entire pure component remains a single Liouville sign multiplied by a structured nonnegative factorisation multiplicity.

---

# 3. Exact weighted-Liouville form of the hard shell

The correlation coefficient becomes

$$
\boxed{
c_X(m)c_X(m+h)
=
\lambda(m)\lambda(m+h)
r_X(m)r_X(m+h).
}
$$

Thus

$$
\boxed{
\begin{aligned}
\mathfrak R_{\mathrm{osc}}(Q,Y)
=
Y
\sum_h\sum_m
&\frac{\lambda(m)\lambda(m+h)
r_X(m)r_X(m+h)}{m(m+h)}\\
&\times e^{iQ\log(1+h/m)}
\widehat\Phi\!\left(Y\log(1+h/m)\right),
\end{aligned}
}
$$

with the inherited shift restrictions.

This is a weighted, locally Cesaro-scale, oscillatory two-point Liouville correlation.

Three distinctions are essential:

1. $r_X$ is not identically $1$ ;
2. the $m$ -average is localized to one dyadic scale, rather than logarithmically averaging over many scales;
3. the phase depends on both $m$ and the growing shift $h$.

Therefore known logarithmically averaged Chowla results do not directly prove the required bound.

---

# 4. Type-II determinant expansion

Choose a Type-II split with

$$
u\sim M,
\qquad
v\sim N,
\qquad
MN\asymp X,
\qquad
M\le N.
$$

Write

$$
c_X(n)
=
\sum_{uv=n}\alpha(u)\beta(v).
$$

For a fixed shift $h$,

$$
\sum_m c_X(m)c_X(m+h)\mathcal K(m,h)
$$

expands into quadruples

$$
(u,v,u',v')
$$

satisfying

$$
\boxed{
u'v'-uv=h,
}
$$

where $u,u'\sim M$, $v,v'\sim N$, and $\mathcal K$ contains the denominator, translated phase, and Gaussian cutoff.

The additive shift of products is therefore a determinant-type incidence equation.

---

# 5. GCD fibre parametrisation

Fix $u,u'$ and set

$$
g=(u,u'),
\qquad
u=ga,
\qquad
u'=gb,
\qquad
(a,b)=1.
$$

The equation

$$
u'v'-uv=h
$$

becomes

$$
\boxed{
bv'-av=k,
\qquad
k=\frac{h}{g}.
}
$$

Hence a necessary condition is

$$
\boxed{g\mid h.}
$$

If one solution $(v_0,v_0')$ exists, all integral solutions are

$$
\boxed{
v=v_0+bt,
\qquad
v'=v_0'+at,
\qquad
t\in\mathbb Z.
}
$$

Since

$$
a,b\asymp\frac{M}{g},
$$

the number of points of this affine lattice fibre inside $v,v'\asymp N$ is

$$
\boxed{
O\!\left(1+\frac{Ng}{M}\right).
}
$$

Create:

```text
B-RH-018
TYPEII_SHIFTED_PRODUCT_DETERMINANT_FIBRE_PARAMETRISATION
status:
  CERTIFIED EXACT REDUCTION
```

---

# 6. Algebraic incidence reaches only the orthogonality floor

The number of pairs $u,u'\sim M$ with $(u,u')=g$ is at most

$$
\ll
\left(\frac{M}{g}\right)^2
$$

up to harmless divisor losses.

Therefore the number of quadruples at a fixed $h$ is bounded by

$$
\begin{aligned}
\mathcal N_h
&\ll
X^{o(1)}
\sum_{g\mid h}
\left(\frac{M}{g}\right)^2
\left(1+\frac{Ng}{M}\right)\\
&\ll
X^{o(1)}
\left(
M^2\sum_{g\mid h}\frac1{g^2}
+
MN\sum_{g\mid h}\frac1g
\right).
\end{aligned}
$$

Since

$$
M^2\le MN\asymp X,
$$

and

$$
\sum_{g\mid h}\frac1g
\le h^{o(1)},
$$

we obtain

## Theorem 6.1 — Determinant incidence floor

$$
\boxed{
\mathcal N_h
\ll
X^{1+o(1)}.
}
$$

After inserting divisor-bounded grouped coefficients and the factor

$$
\frac1{m(m+h)}\asymp X^{-2},
$$

this reproduces the fixed-shift absolute scale

$$
\boxed{X^{-1+o(1)}.}
$$

This is the same orthogonality floor already visible in Paper 42.

Thus product-equality plus additive-shift algebra does not, by itself, provide the fixed $X$ -power needed by B-RH-014.

Create:

```text
O-RH-107
DETERMINANT_INCIDENCE_ALGEBRA_STOPS_AT_ORTHOGONALITY_FLOOR
status:
  CERTIFIED
```

This closes Campaign 42 track OM1 as a structural reduction rather than a successful fixed-power estimate.

---

# 7. Phase geometry on one determinant fibre

Along a fibre

$$
v=v_0+bt,
\qquad
v'=v_0'+at,
$$

the translated phase is

$$
\psi(t)
=
Q\log\frac{u'v'}{uv}
=
Q\log\frac{b}{a}
+
Q\log\frac{v'}{v}.
$$

Differentiate with respect to the real interpolation variable $t$.

Since

$$
bv'-av=k=\frac hg,
$$

we have

$$
\begin{aligned}
\psi'(t)
&=
Q\left(\frac{a}{v'}-\frac{b}{v}\right)\\
&=
-Q\frac{k}{vv'}.
\end{aligned}
$$

Hence

## Theorem 7.1 — Exact first derivative on determinant fibres

$$
\boxed{
\psi'(t)
=
-\frac{Qh}{g\,v(t)v'(t)}.
}
$$

On $v,v'\asymp N$,

$$
\boxed{
|\psi'(t)|
\asymp
\frac{Qh}{gN^2}.
}
$$

A long fibre has length

$$
\asymp
\frac{Ng}{M}.
$$

Therefore its total phase variation is

$$
\boxed{
\operatorname{Var}_{\mathrm{fibre}}\psi
\asymp
\frac{Qh}{gN^2}
\frac{Ng}{M}
\asymp
\frac{Qh}{MN}
\asymp
\frac{Qh}{X}.
}
$$

The GCD parameter cancels from the total variation.

This is an important geometric rigidity: every genuinely long determinant fibre sees essentially the same normalized oscillation parameter

$$
\boxed{V(h)=\frac{Qh}{X}.}
$$

---

# 8. The original $X/Q$ cutoff was not maximal

Paper 42 declared

$$
h\le\frac{X}{Q}
$$

harmless by absolute values.

The same argument works much farther.

For any $H_0$ in the Gaussian-localized range,

$$
\begin{aligned}
\left|
Y\sum_{1\le h\le H_0}
\sum_m
\frac{c_X(m)c_X(m+h)}{m(m+h)}
 e^{iQ\log(1+h/m)}
\widehat\Phi(\cdots)
\right|
&\ll
YH_0X^{-1+o(1)}.
\end{aligned}
$$

Equivalently, if

$$
H_0=\frac{X}{Q}V_0,
$$

then

$$
\boxed{
|\mathfrak R_{V\le V_0}|
\ll
\frac{Y}{Q}V_0X^{o(1)}.
}
$$

This gives a direct conversion between phase-variation threshold and trivial total mass.

---

# 9. Polynomial erosion of the low-variation shell

Set

$$
\boxed{
V_\star
=
X^{\varepsilon/2-61w/100}.
}
$$

Because

$$
w\le\frac{\varepsilon}{1000},
$$

we have

$$
\frac{\varepsilon}{2}-\frac{61w}{100}
\ge
\left(\frac12-\frac{61}{100000}\right)\varepsilon
>0.
$$

Define

$$
\boxed{
h_\star
=
\frac{X}{Q}V_\star.
}
$$

Then, using the inherited bound

$$
\frac{Y}{Q}
\ll
X^{3w/10-\varepsilon/2},
$$

we obtain

$$
\begin{aligned}
|\mathfrak R_{h\le h_\star}|
&\ll
\frac{Y}{Q}
X^{\varepsilon/2-61w/100+o(1)}\\
&\ll
X^{3w/10-61w/100+o(1)}\\
&=
X^{-31w/100+o(1)}.
\end{aligned}
$$

The target is

$$
X^{-3w/10+o(1)}
=
X^{-30w/100+o(1)}.
$$

Hence the enlarged shell has an extra margin

$$
\boxed{X^{-w/100+o(1)}.}
$$

## Theorem 9.1 — Polynomial low-variation shell erosion

The entire range

$$
\boxed{
1\le h\le
\frac{X}{Q}
X^{\varepsilon/2-61w/100}
}
$$

is harmless for polynomial- $W$ admission.

Create:

```text
O-RH-108
POLYNOMIAL_LOW_VARIATION_SHIFT_SHELL_HARMLESS
status:
  CERTIFIED
```

This strictly strengthens O-RH-103.

---

# 10. The new residual shell has polynomial phase variation

The residual range now begins at

$$
h>h_\star.
$$

Therefore

$$
\boxed{
\frac{Qh}{X}
>
X^{\varepsilon/2-61w/100}.
}
$$

Since the Gaussian cutoff still allows shifts up to

$$
h\lesssim X^{o(1)}\frac{X}{Y},
$$

and

$$
\frac{Q}{Y}
\gtrsim
X^{\varepsilon/2-3w/10},
$$

the residual shell has room of at least

$$
\boxed{
X^{31w/100-o(1)}
}
$$

in multiplicative shift scale at the extremal inherited geometry.

Thus the new unresolved object is not a barely oscillatory shell.

It is a polynomially oscillatory shell.

Create:

```text
O-RH-109
RESIDUAL_SHIFT_SHELL_HAS_POLYNOMIAL_PHASE_VARIATION
status:
  CERTIFIED
```

---

# 11. Why polynomial phase variation does not yet solve the problem

If the arithmetic weights on a determinant fibre were smooth or absent, the derivative identity from Section 7 would make classical oscillatory-sum methods immediately relevant.

But the exact fibre weight inherits Liouville signs and structured squarefree-factorisation weights.

At the atomic level, fixing all variables except one factor on each side produces affine forms

$$
A_0+B_0t,
\qquad
A_1+B_1t,
$$

and a weight of the schematic form

$$
\boxed{
\lambda(A_0+B_0t)
\lambda(A_1+B_1t)
\times
\text{structured nonnegative multiplicity}.
}
$$

Therefore a derivative test cannot simply discard the arithmetic amplitude.

The remaining problem is a hybrid of:

1. two-linear-form Liouville decorrelation;
2. polynomially varying phase;
3. determinant-fibre arithmetic;
4. restricted squarefree-factorisation weights.

The phase is now strong enough to matter, but a theorem coupling it to the Liouville carrier is still required.

---

# 12. Calibration against two-point Chowla technology

The exact sign collapse makes ordinary Liouville correlation a direct calibration rather than merely an analogy.

Tao's two-point logarithmically averaged Chowla theorem proves cancellation after logarithmic averaging for two affine-linear Liouville forms, but it does not prove the ordinary Cesaro two-point Chowla conjecture.

Pilatte obtained a fixed power of the logarithm for the logarithmically weighted shift-one correlation.

Guo's August 2026 result gives quantitative logarithmic cancellation uniformly for shifts up to a small power of $\log x$ and explicitly states that it does not prove ordinary Cesaro two-point Chowla.

Our residual object is stronger in several ways:

$$
\boxed{
\text{one dyadic scale}
+
\text{structured weights}
+
\text{polynomial shift range}
+
\text{oscillatory phase}.
}
$$

The phase is additional information, but current logarithmic Chowla estimates cannot be inserted as a black box to produce

$$
X^{-3w/10}.
$$

Create:

```text
O-RH-110
CURRENT_LOG_CHOWLA_THEOREMS_DO_NOT_CLOSE_WEIGHTED_OSCILLATORY_LIOUVILLE_CORE
status:
  CERTIFIED AS CURRENT-LITERATURE CALIBRATION
```

This is a scope statement, not a universal impossibility theorem.

---

# 13. Campaign 42 track audit

## OM1 — balanced Möbius-convolution correlation algebra

**Status:** `CLOSED_AS_LIOUVILLE_WEIGHTED_DETERMINANT_REDUCTION`

Outputs:

$$
c_X(n)=\lambda(n)r_X(n),
$$

and

$$
u'v'-uv=h
$$

with exact GCD fibre parametrisation.

Pure incidence counting stops at the orthogonality floor.

## OM2 — high-frequency phase geometry

**Status:** `ADVANCED_TO_POLYNOMIAL_VARIATION_RESIDUAL`

The harmless shell extends to

$$
h\le
\frac{X}{Q}
X^{\varepsilon/2-61w/100},
$$

so every residual long fibre has

$$
\operatorname{Var}\psi
\gtrsim
X^{\varepsilon/2-61w/100}.
$$

## OM3 — averaged shift cancellation

**Status:** `NOT_CLOSED_BY_CURRENT_CHOWLA_INPUT`

Known logarithmic/average technology does not yield the required uniform fixed $X$ -power for the weighted dyadic object.

## OM4 — Ramaré extraction

**Status:** `STILL_OPEN`

The Liouville sign collapse makes small-prime extraction more natural, but extraction must be performed without converting the problem back into an uncontrolled two-linear-form parity problem.

## OM5 — cross- $j$ coupling

**Status:** `STILL_OPEN`

The exact Heath-Brown identity contains pointwise inclusion-exclusion across $j$ -levels. Any successful use must preserve those cross terms before absolute values and before componentwise mean-square bounds.

---

# 14. New canonical core

After removing the enlarged harmless shell, define

$$
\boxed{
\begin{aligned}
\mathfrak R_{\lambda}(Q,Y)
=
Y
\sum_{h_\star<h\lesssim X^{o(1)}X/Y}
\sum_m
&\frac{\lambda(m)\lambda(m+h)
r_X(m)r_X(m+h)}{m(m+h)}\\
&\times e^{iQ\log(1+h/m)}
\widehat\Phi\!\left(Y\log(1+h/m)\right).
\end{aligned}
}
$$

Then

$$
\boxed{
\mathfrak R_{\mathrm{osc}}(Q,Y)
=
\mathfrak R_{\lambda}(Q,Y)
+
O\!\left(X^{-31w/100+o(1)}\right).
}
$$

Hence polynomial- $W$ admission reduces to proving

$$
\boxed{
|\mathfrak R_{\lambda}(Q,Y)|
\ll
X^{-3w/10+o(1)}.
}
$$

This is not declared a new root frontier.

It is the sharpened internal form of the existing F-RH-010 / B-RH-014 route.

---

# 15. Campaign 42 verdict

Campaign 42 does not prove the required fixed-power estimate.

It does, however, achieve two irreversible reductions:

1. the high-order Möbius sign structure collapses exactly to Liouville;
2. all low and moderately varying phase shells can be removed by absolute values until the remaining phase variation is polynomial in $X$.

Thus the obstruction is now more specific than in Paper 42:

$$
\boxed{
\text{weighted Liouville two-point decorrelation}
+
\text{polynomial determinant-fibre oscillation}.
}
$$

Campaign 42 is therefore closed as

```text
CLOSED_AS_WEIGHTED_LIOUVILLE_POLYNOMIAL_PHASE_LOCALIZATION
```

with no RH promotion.

---

# 16. Campaign 43

The next campaign is

```text
CSM_RH Campaign 43
WEIGHTED_LIOUVILLE_POLYNOMIAL_PHASE_ATTACK
```

The target remains B-RH-014 through the sharpened core $\mathfrak R_\lambda(Q,Y)$.

No new observable is introduced.

---

# 17. Campaign 43 tracks

## WL1 — phase-first determinant-fibre dispersion

Apply Cauchy or van der Corput only after preserving the determinant-fibre phase.

The goal is to turn the polynomial lower bound

$$
\frac{Qh}{X}
\ge
X^{\varepsilon/2-61w/100}
$$

into a fixed-power gain without replacing Liouville coefficients by generic bounded coefficients.

## WL2 — Liouville-aware Ramaré extraction

Exploit complete multiplicativity of $\lambda$ and extract a prime from exactly one side when it does not divide $h$.

Track the common divisor

$$
(m,m+h)=(m,h)
$$

separately so that common-prime signs cancel before extraction.

## WL3 — structured-weight decoupling

Use

$$
r_X
=
(\mu^2 1_{U_1})*\cdots*(\mu^2 1_{U_L})
$$

to determine whether the nonnegative multiplicity weight can be separated from the Liouville sign at acceptable exponent cost.

## WL4 — cross- $j$ pre-square recombination

Audit whether the alternating Heath-Brown $j$ -sum can be recombined before translated mean-square expansion so that the pure Liouville carrier cancels against adjacent $j$ -levels.

## WL5 — root-recoupling comparison

If WL4 collapses back to the full prime-error coefficient, compare the resulting object directly with F-RH-010 rather than pretending a new component theorem has been obtained.

---

# 18. Rejection filters for Campaign 43

Reject a candidate proof if any of the following occurs.

## R1. Generic-coefficient phase cancellation

The argument applies an oscillatory derivative bound after replacing Liouville-weighted coefficients by arbitrary bounded coefficients.

## R2. Logarithmic-to-power promotion

A bound of size $\log^{-A}X$, $o(1)$, or $\exp(-c\log^\alpha X)$ is treated as $X^{-\delta}$ for fixed $\delta>0$.

## R3. Scale averaging mismatch

A logarithmically averaged Chowla theorem over many scales is used as a uniform theorem on one prescribed dyadic scale without an explicit transfer argument.

## R4. Weight deletion

The factor $r_X(m)r_X(m+h)$ is discarded without a positive majorant whose exponent ledger is verified.

## R5. Hidden fixed-strip input

A pointwise estimate equivalent to a fixed zero-free strip is inserted through a Möbius or Liouville Dirichlet polynomial estimate.

## R6. Cross- $j$ cancellation after big- $O$

Separate component bounds are estimated absolutely and then claimed to cancel.

---

# 19. External calibration

The following sources calibrate the scope of the claims in this paper.

1. K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae 244 (2026), 967–1091, DOI `10.1007/s00222-026-01408-6`. The relevant Type-II target is Lemma 3.5, especially equations (3.9)–(3.13).

2. T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Forum of Mathematics, Pi 4 (2016), arXiv:`1509.05422`. This proves logarithmically averaged two-point cancellation, not ordinary Cesaro two-point Chowla.

3. C. Pilatte, *Improved bounds for the two-point logarithmic Chowla conjecture*, arXiv:`2310.19357`. This obtains a fixed power of the logarithm for the logarithmically weighted shift-one problem.

4. J. Guo, *Quantitative Logarithmic Chowla Correlations Uniformly over Growing Shifts*, arXiv:`2608.23500` (2026). The result remains logarithmically weighted and its stated shift range is polylogarithmic.

No cited theorem is claimed to prove the weighted dyadic fixed- $X$ -power estimate required here.

---

# 20. State transition

The canonical state advances from v1.33 to v1.34.

New bridge identities:

```text
B-RH-017
PURE_MOBIUS_CORE_LIOUVILLE_SIGN_FACTORISATION
CERTIFIED

B-RH-018
TYPEII_SHIFTED_PRODUCT_DETERMINANT_FIBRE_PARAMETRISATION
CERTIFIED
```

New obstructions/refinements:

```text
O-RH-107
DETERMINANT_INCIDENCE_ALGEBRA_STOPS_AT_ORTHOGONALITY_FLOOR
CERTIFIED

O-RH-108
POLYNOMIAL_LOW_VARIATION_SHIFT_SHELL_HARMLESS
CERTIFIED

O-RH-109
RESIDUAL_SHIFT_SHELL_HAS_POLYNOMIAL_PHASE_VARIATION
CERTIFIED

O-RH-110
CURRENT_LOG_CHOWLA_THEOREMS_DO_NOT_CLOSE_WEIGHTED_OSCILLATORY_LIOUVILLE_CORE
CERTIFIED AS CURRENT-LITERATURE CALIBRATION
```

Root status remains

```text
F-RH-010  PRIME_ERROR_SELF_CORRELATION  OPEN
F-RH-016  MESOSCOPIC_LAG_ENERGY_POWER_GAIN  OPEN
RH_PROVED  FALSE
RH_DISPROVED  FALSE
GLOBAL_RH_CERTIFICATE  FALSE
```

---

# 21. Final status

The campaign has not solved RH and has not proved polynomial- $W$ Type-II admission.

The accepted advance is

$$
\boxed{
\text{pure Möbius convolution}
\longrightarrow
\lambda(n)\times\text{nonnegative structured weight}
}
$$

combined with

$$
\boxed{
\text{residual shifts}
\Longrightarrow
\frac{Qh}{X}
\ge
X^{\varepsilon/2-61w/100}.
}
$$

Thus the next valid attack is no longer generic Möbius correlation algebra.

It is a Liouville-aware polynomial-phase dispersion problem, with Ramaré extraction and cross- $j$ recombination retained as live alternatives.
