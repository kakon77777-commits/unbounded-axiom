# CSM_RH Paper 77

## Exact Renormalized Vaughan Extraction for the Signed Shift-Prime Root Sequence

**Project:** CSM_RH  
**Paper:** 77  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 47 — `ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Track:** C47-B-v2 — `EXACT_VAUGHAN_SIGNED_ROOT_DECOMPOSITION`  
**Status:** EXACT POWER-OUTPUT DECOMPOSITION CERTIFIED / PAPER-75 BILINEAR AXIOM SUPERSEDED AS ROOT INPUT / RENORMALIZED TYPE-II DEFECT OPEN  
**Canonical entry state:** v1.67 / Paper 76 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 76 corrected the first Campaign-47 root bridge and identified the signed root sequence

$$
f_{N,H}(n)
=
W(n/N)
\sum_r
\omega_H(r)
\left(
\Lambda(n+r)-1
\right).
$$

It proved

$$
\mathcal R_W(N,H)
=
\sum_n
\Lambda(n)f_{N,H}(n)
-
F(N,H),
$$

where

$$
F(N,H)
=
\sum_n f_{N,H}(n),
$$

and also proved the deterministic divisor law

$$
F_d
=
\frac Fd
+
O_W(N).
$$

The present paper applies Vaughan's identity **directly to this signed root sequence**, retains every Type-I main term exactly, and identifies the unique renormalized Type-II quantity which remains.

Let

$$
U,V>1
$$

with

$$
V<N,
$$

and define

$$
\boxed{
b_U(k)
=
\sum_{\substack{d\mid k\\d\le U}}
\mu(d),
}
$$

$$
\boxed{
a_{U,V}(k)
=
\sum_{\substack{de=k\\d\le U\\e\le V}}
\mu(d)\Lambda(e).
}
$$

For every $n>V$, Vaughan's identity is

$$
\boxed{
\Lambda(n)
=
\sum_{\substack{dr=n\\d\le U}}
\mu(d)\log r
-
\sum_{\substack{kr=n\\k\le UV}}
a_{U,V}(k)
-
\sum_{\substack{ek=n\\e>V\\k>U}}
\Lambda(e)b_U(k).
}
$$

Applying this to $f=f_{N,H}$ gives

$$
\sum_n\Lambda(n)f(n)
=
T_1-T_2-T_3.
$$

Define

$$
F_d=\sum_{d\mid n}f(n),
$$

and introduce the logarithmically weighted companion

$$
G
=
\sum_n
f(n)\log(n/N),
$$

$$
G_d
=
\sum_{d\mid n}
f(n)\log(n/N).
$$

The same bounded-variation lattice argument as in Papers 75–76 gives

$$
\boxed{
F_d
=
\frac Fd+r_d,
\qquad
G_d
=
\frac Gd+s_d,
}
$$

with

$$
r_d,s_d
=
O_W(N)
$$

uniformly, and the aggregate power bounds

$$
\boxed{
\sum_{d\le D}
\tau_5(d)
\left(
|r_d|+|s_d|
\right)
\ll_W
ND(\log N)^{O(1)}.
}
$$

Now define the truncated scalar coefficients

$$
\boxed{
M_U
=
\sum_{d\le U}\frac{\mu(d)}d,
}
$$

$$
\boxed{
J_U
=
\sum_{d\le U}
\frac{\mu(d)\log d}{d},
}
$$

$$
\boxed{
L_V
=
\sum_{e\le V}
\frac{\Lambda(e)}e.
}
$$

The two Type-I terms then have an exact main-term recombination.

The first Type-I piece is

$$
T_1
=
\sum_{d\le U}
\mu(d)
\left[
(\log N-\log d)F_d+G_d
\right].
$$

The second is

$$
T_2
=
\sum_{k\le UV}
a_{U,V}(k)F_k.
$$

Since

$$
\boxed{
\sum_{k\le UV}\frac{a_{U,V}(k)}k
=
M_U L_V,
}
$$

one obtains

$$
\boxed{
T_1-T_2-F
=
\mathcal M_{U,V}(F,G;N)
+
\mathcal E_I,
}
$$

where

$$
\boxed{
\mathcal M_{U,V}
=
F
\left[
M_U(\log N-L_V)-J_U-1
\right]
+
G M_U
}
$$

and

$$
\boxed{
\begin{aligned}
\mathcal E_I
&=
\sum_{d\le U}
\mu(d)
\left[
(\log N-\log d)r_d+s_d
\right]
\\
&\quad
-
\sum_{k\le UV}
a_{U,V}(k)r_k.
\end{aligned}
}
$$

The Type-II term is

$$
\boxed{
\mathcal T^{II}_{U,V}(f)
=
\sum_{\substack{e>V,\ k>U\\ek\in\operatorname{supp}f}}
\Lambda(e)b_U(k)f(ek).
}
$$

Therefore the root covariance has the exact decomposition

$$
\boxed{
\mathcal R_W
=
\mathcal M_{U,V}
-
\mathcal T^{II}_{U,V}
+
\mathcal E_I.
}
$$

Equivalently, define the **renormalized Vaughan defect**

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
=
\mathcal T^{II}_{U,V}
-
\mathcal M_{U,V}.
}
$$

Then

$$
\boxed{
\mathcal R_W
=
-
\mathcal V^{\rm ren}_{U,V}
+
\mathcal E_I.
}
$$

This is the principal result of the paper.

The Type-I error is power-controlled.

Using

$$
|a_{U,V}(k)|
\le
\sum_{e\mid k}\Lambda(e)
=
\log k,
$$

and the aggregate divisor discrepancy,

$$
\boxed{
\mathcal E_I
\ll_W
NUV
(\log N)^{O(1)}.
}
$$

Take

$$
H=N^{1-\tau},
\qquad
U=N^u,
\qquad
V=N^v.
$$

Relative to the natural root covariance scale

$$
NH,
$$

the Type-I error has saving exponent

$$
\boxed{
\eta_I
=
1-\tau-u-v.
}
$$

Therefore, for a PESC $(\kappa)$ seed, if

$$
\boxed{
u+v
<
1-\tau-\kappa-\eta
}
$$

for some fixed $\eta>0$, then

$$
\boxed{
\mathcal E_I
\ll
NH
N^{-\kappa-\eta+o(1)}.
}
$$

This proves that **exact Vaughan extraction itself preserves fixed power**. The generic logarithmic extraction floor of the 1998 asymptotic sieve is absent.

But the paper also identifies why an unrenormalized Type-II estimate is the wrong target.

Under PESC $(\kappa)$, put

$$
d=\frac{\kappa}{2}.
$$

The seed gives

$$
M_U
\ll
U^{-d+o(1)},
$$

$$
J_U+1
\ll
U^{-d+o(1)}
\log U,
$$

and

$$
L_V
=
\log V
-
\gamma
+
O
\left(
V^{-d+o(1)}
\right).
$$

Moreover,

$$
F,G
\ll
HN^{1-d+o(1)}.
$$

Hence

$$
\boxed{
\mathcal M_{U,V}
\ll
NH
N^{-d}
U^{-d}
N^{o(1)}.
}
$$

If

$$
U=N^u,
$$

then the scalar Type-I main has effective exponent

$$
\boxed{
d(1+u).
}
$$

For every fixed

$$
u<1,
$$

$$
d(1+u)<2d=\kappa.
$$

Thus $\mathcal M_{U,V}$ can be parametrically larger than the root-critical covariance scale.

The exact identity then forces $\mathcal T^{II}_{U,V}$ to carry a matching one-point truncation component.

Therefore:

```text
DO NOT PROVE
T^{II}_{U,V} IS SMALL.

PROVE
T^{II}_{U,V} - M_{U,V}
IS SMALL.
```

This supersedes the root use of Paper 75's F-RH-023.

The new arithmetic frontier is:

```text
F-RH-024
RENORMALIZED VAUGHAN BALANCED DEFECT POWER
```

Find fixed

$$
\tau,u,v,\eta>0
$$

such that

$$
u+v
<
1-\tau-\kappa-\eta
$$

and

$$
\boxed{
\left|
\mathcal T^{II}_{U,V}(f_{N,H})
-
\mathcal M_{U,V}(F,G;N)
\right|
\ll
NH
N^{-\kappa-\eta}.
}
$$

Then the exact identity gives

$$
\boxed{
\mathcal R_W(N,H)
\ll
NH
N^{-\kappa-\eta+o(1)}.
}
$$

Provided additionally

$$
\kappa+\eta<1-\tau,
$$

the already-solved local Hardy–Littlewood variance is smaller, so the weighted pair energy has a strict fixed-power excess beyond the seed.

Thus F-RH-024 is a direct root bootstrap inequality.

It has no generic sieve extraction loss and no shifted-Möbius coercivity bridge.

Its arithmetic content is very specific:

> the ordinary-factorization Type-II term must reproduce the explicit one-point Möbius truncation main $\mathcal M_{U,V}$, with a covariance defect smaller by a fixed power.

This is a second-order parity-cancellation theorem rather than a first-order prime-producing theorem.

The pseudo-prime and Beurling calibrations remain effective. The term

$$
\Lambda(e)b_U(k)f(ek)
$$

simultaneously uses:

- actual prime powers through $\Lambda(e)$ ;
- ordinary divisor truncation through $b_U(k)$ ;
- ordinary product $ek$ ;
- ordinary additive shifts hidden in $f(ek)$.

The exact renormalization $\mathcal M_{U,V}$ additionally uses the ordinary Möbius and von Mangoldt Dirichlet coefficients.

Thus F-RH-024 is not implied by the positive integer-lattice pseudo-prime properties of Paper 64 and is not intrinsic to a generic Beurling prime system.

Campaign 47 therefore passes C47-B-v2.

The next task is no longer extraction.

It is to attack F-RH-024 itself.

No RH theorem is claimed.

---

# 1. Signed root sequence

Recall

$$
\boxed{
f(n)
=
f_{N,H}(n)
=
W(n/N)
\sum_r
\omega_H(r)
\left(
\Lambda(n+r)-1
\right).
}
$$

Let

$$
\boxed{
F=\sum_n f(n).
}
$$

Paper 76 proved

$$
\boxed{
\mathcal R_W
=
\sum_n\Lambda(n)f(n)-F.
}
$$

All sums below are automatically restricted to the compact dyadic support of $f$.

---

# 2. Vaughan identity

For parameters

$$
U,V>1
$$

define

$$
b_U(k)
=
\sum_{\substack{d\mid k\\d\le U}}
\mu(d)
$$

and

$$
a_{U,V}(k)
=
\sum_{\substack{de=k\\d\le U\\e\le V}}
\mu(d)\Lambda(e).
$$

For $n>V$,

$$
\boxed{
\Lambda(n)
=
\sum_{\substack{dr=n\\d\le U}}
\mu(d)\log r
-
\sum_{\substack{kr=n\\k\le UV}}
a_{U,V}(k)
-
\sum_{\substack{ek=n\\e>V\\k>U}}
\Lambda(e)b_U(k).
}
$$

This is the standard Vaughan identity obtained by comparing the coefficients in the truncated Dirichlet-series decomposition.

External calibration:

Encyclopedia of Mathematics, `Vaughan identity`.

---

# 3. Exact decomposition of the root prime-detection sum

Multiply Vaughan's identity by $f(n)$ and sum.

Define

$$
T_1
=
\sum_{d\le U}
\mu(d)
\sum_{d\mid n}
f(n)\log(n/d),
$$

$$
T_2
=
\sum_{k\le UV}
a_{U,V}(k)
\sum_{k\mid n}
f(n),
$$

and

$$
T_3
=
\sum_{\substack{e>V,\ k>U}}
\Lambda(e)b_U(k)f(ek).
$$

Then

$$
\boxed{
\sum_n
\Lambda(n)f(n)
=
T_1-T_2-T_3.
}
$$

Therefore

$$
\boxed{
\mathcal R_W
=
T_1-T_2-T_3-F.
}
$$

No approximation has yet been made.

---

# 4. Log-weighted divisor law

Define

$$
\boxed{
G
=
\sum_n
f(n)\log(n/N),
}
$$

and

$$
\boxed{
G_d
=
\sum_{d\mid n}
f(n)\log(n/N).
}
$$

Multiplying the smooth weight $W(u)$ by $\log u$ preserves compact support and bounded variation.

The same lattice-sampling argument as Paper 76 therefore gives:

## Theorem 4.1 — Log-weighted signed divisor law

$$
\boxed{
G_d
=
\frac Gd
+
s_d,
}
$$

with

$$
\boxed{
s_d=O_W(N)
}
$$

uniformly.

Moreover, for every $D\ge1$,

$$
\boxed{
\sum_{d\le D}
\tau_5(d)
\left(
|r_d|+|s_d|
\right)
\ll_W
ND(\log N)^{O(1)},
}
$$

where

$$
F_d=\frac Fd+r_d.
$$

Create:

```text
B-RH-119
LOG_WEIGHTED_SIGNED_SHIFT_ERROR_SEQUENCE_RETAINS_DETERMINISTIC_DIVISOR_DISTRIBUTION
CERTIFIED
```

---

# 5. Exact first Type-I main term

Since

$$
\log(n/d)
=
\log N
-
\log d
+
\log(n/N),
$$

$$
\begin{aligned}
T_1
&=
\sum_{d\le U}
\mu(d)
\left[
(\log N-\log d)F_d+G_d
\right].
\end{aligned}
$$

Define

$$
M_U
=
\sum_{d\le U}
\frac{\mu(d)}d,
$$

and

$$
J_U
=
\sum_{d\le U}
\frac{\mu(d)\log d}{d}.
$$

Substitute the divisor laws:

$$
\boxed{
\begin{aligned}
T_1
&=
F
\left(
\log N\,M_U-J_U
\right)
+
G M_U
\\
&\quad
+
\sum_{d\le U}
\mu(d)
\left[
(\log N-\log d)r_d+s_d
\right].
\end{aligned}
}
$$

---

# 6. Exact second Type-I main term

Since

$$
T_2
=
\sum_{k\le UV}
a_{U,V}(k)F_k,
$$

we need the scalar sum

$$
\sum_{k\le UV}
\frac{a_{U,V}(k)}k.
$$

By definition,

$$
\begin{aligned}
\sum_{k\le UV}
\frac{a_{U,V}(k)}k
&=
\sum_{d\le U}
\frac{\mu(d)}d
\sum_{e\le V}
\frac{\Lambda(e)}e
\\
&=
\boxed{
M_U L_V,
}
\end{aligned}
$$

where

$$
L_V
=
\sum_{e\le V}
\frac{\Lambda(e)}e.
$$

Therefore:

$$
\boxed{
T_2
=
F M_U L_V
+
\sum_{k\le UV}
a_{U,V}(k)r_k.
}
$$

---

# 7. Renormalized exact root identity

Combine Sections 5–6 and subtract $F$.

Define

$$
\boxed{
\mathcal M_{U,V}
=
F
\left[
M_U(\log N-L_V)
-
J_U
-
1
\right]
+
G M_U.
}
$$

Define

$$
\boxed{
\begin{aligned}
\mathcal E_I
&=
\sum_{d\le U}
\mu(d)
\left[
(\log N-\log d)r_d+s_d
\right]
\\
&\quad
-
\sum_{k\le UV}
a_{U,V}(k)r_k.
\end{aligned}
}
$$

Then:

## Theorem 7.1 — Exact renormalized Vaughan root decomposition

$$
\boxed{
\mathcal R_W
=
\mathcal M_{U,V}
-
\mathcal T^{II}_{U,V}
+
\mathcal E_I,
}
$$

where

$$
\boxed{
\mathcal T^{II}_{U,V}
=
\sum_{\substack{e>V,\ k>U}}
\Lambda(e)b_U(k)f(ek).
}
$$

Equivalently,

$$
\boxed{
\mathcal R_W
=
-
\mathcal V^{\rm ren}_{U,V}
+
\mathcal E_I,
}
$$

where

$$
\boxed{
\mathcal V^{\rm ren}_{U,V}
=
\mathcal T^{II}_{U,V}
-
\mathcal M_{U,V}.
}
$$

Create:

```text
B-RH-120
EXACT_RENORMALIZED_VAUGHAN_DECOMPOSITION_OF_THE_SIGNED_ROOT_COVARIANCE
CERTIFIED
```

---

# 8. Power bound for the Type-I error

The coefficient $a_{U,V}(k)$ satisfies

$$
\begin{aligned}
|a_{U,V}(k)|
&\le
\sum_{\substack{e\mid k\\e\le V}}
\Lambda(e)
\\
&\le
\sum_{e\mid k}
\Lambda(e)
\\
&=
\boxed{
\log k.
}
\end{aligned}
$$

Therefore, using Theorem 4.1,

$$
\begin{aligned}
|\mathcal E_I|
&\ll
(\log N)
\sum_{d\le U}
\left(
|r_d|+|s_d|
\right)
+
(\log N)
\sum_{k\le UV}
|r_k|
\\
&\ll
\boxed{
NUV
(\log N)^{O(1)}.
}
\end{aligned}
$$

Create:

```text
B-RH-121
EXACT_VAUGHAN_TYPE_I_ERROR_RETAINS_FIXED_POWER_FROM_SHIFT_AVERAGED_DIVISOR_DISTRIBUTION
CERTIFIED
```

---

# 9. Exponent ledger

Set

$$
H=N^{1-\tau},
$$

$$
U=N^u,
$$

$$
V=N^v.
$$

Then

$$
NH
=
N^{2-\tau}.
$$

The Type-I error satisfies

$$
\boxed{
\frac{
|\mathcal E_I|
}{
NH
}
\ll
N^{-(1-\tau-u-v)+o(1)}.
}
$$

Hence the Type-I saving exponent is

$$
\boxed{
\eta_I
=
1-\tau-u-v.
}
$$

For a seed PESC $(\kappa)$ and desired excess $\eta>0$, Type I is supercritical provided

$$
\boxed{
u+v
<
1-\tau-\kappa-\eta.
}
$$

This is compatible with positive $u,v$ whenever

$$
\tau<1-\kappa-\eta.
$$

Thus the exact extraction produces no logarithmic loss.

---

# 10. Seed size of the explicit renormalization

Assume PESC $(\kappa)$ and put

$$
d=\frac{\kappa}{2}.
$$

The seed Mertens bound gives

$$
\boxed{
M_U
\ll
U^{-d+o(1)}.
}
$$

Since

$$
\frac1{\zeta(s)}
\sim
s-1
$$

at $s=1$,

$$
\sum_{n=1}^{\infty}
\frac{\mu(n)\log n}{n}
=
-1.
$$

Partial summation with the seed Mertens bound gives

$$
\boxed{
J_U+1
\ll
U^{-d+o(1)}
\log U.
}
$$

Likewise the seed PNT error gives

$$
\boxed{
L_V
=
\log V-\gamma
+
O
\left(
V^{-d+o(1)}
\right).
}
$$

Finally,

$$
\boxed{
F,G
\ll
HN^{1-d+o(1)}.
}
$$

Therefore:

## Theorem 10.1 — Size of the explicit one-point renormalization

$$
\boxed{
\mathcal M_{U,V}
\ll
NH
N^{-d}
U^{-d}
N^{o(1)}.
}
$$

If

$$
U=N^u,
$$

the effective exponent is

$$
\boxed{
d(1+u).
}
$$

---

# 11. Why unrenormalized Type II is the wrong target

For every fixed

$$
u<1,
$$

$$
d(1+u)
<
2d
=
\kappa.
$$

Hence the explicit Type-I main may be larger than the desired root-critical scale.

The exact identity then implies that the Type-II term must contain a matching component.

Therefore a conjecture such as

$$
\mathcal T^{II}_{U,V}
\ll
NHN^{-\kappa-\eta}
$$

is structurally incompatible with the required cancellation unless the explicit main $\mathcal M_{U,V}$ is independently negligible, which it is not at the seed level.

Create:

```text
O-RH-174
UNRENORMALIZED_VAUGHAN_TYPE_II_SMALLNESS_DISCARDS_A_NECESSARY_ONE_POINT_TRUNCATION_COUNTERTERM
CERTIFIED_AS_METHOD_BARRIER
```

The correct object is

$$
\mathcal T^{II}_{U,V}
-
\mathcal M_{U,V}.
$$

---

# 12. New arithmetic frontier F-RH-024

Open:

```text
F-RH-024
RENORMALIZED_VAUGHAN_BALANCED_DEFECT_POWER
```

Given a PESC $(\kappa)$ seed, find fixed

$$
\tau,u,v,\eta>0
$$

such that

$$
\boxed{
u+v
<
1-\tau-\kappa-\eta
}
$$

and

$$
\boxed{
\left|
\mathcal T^{II}_{U,V}
-
\mathcal M_{U,V}
\right|
\ll
NH
N^{-\kappa-\eta}.
}
$$

Then Theorem 7.1 and Section 9 give

$$
\boxed{
\mathcal R_W
\ll
NH
N^{-\kappa-\eta+o(1)}.
}
$$

This is a direct ordinary-prime root covariance bound.

Create:

```text
B-RH-122
F_RH_024_PLUS_THE_DETERMINISTIC_TYPE_I_POWER_GIVES_A_DIRECT_ROOT_COVARIANCE_EXCESS
CERTIFIED_CONDITIONAL_BRIDGE
```

---

# 13. Connection to F-RH-022

The triangular kernel is the normalized Fejér lag kernel.

The local diagonal and modified-singular-series contribution has scale

$$
N\log(N/H)
=
NH
N^{-(1-\tau)+o(1)}.
$$

Therefore, if

$$
\boxed{
\kappa+\eta
<
1-\tau,
}
$$

the solved local main term is smaller than the F-RH-024 target.

After standard dyadic smooth partitioning, the bound

$$
\mathcal R_W
\ll
NHN^{-\kappa-\eta}
$$

therefore supplies the same fixed-power excess required by the weighted version of F-RH-022.

No shifted-Möbius or central-coercivity bridge is needed.

---

# 14. Status of F-RH-023

Paper 75's F-RH-023 remains a meaningful Friedlander–Iwaniec parity statement.

However, the exact root extraction has now identified a different arithmetic quantity.

Update:

```text
F-RH-023
OPEN_AUXILIARY_PARITY_CANDIDATE
NO_LONGER_PREFERRED_ROOT_INPUT
```

The preferred Campaign-47 arithmetic frontier becomes F-RH-024.

This is not merely a change of notation.

F-RH-024 includes the explicit counterterm required by the exact Vaughan identity.

---

# 15. Pseudo-prime / Beurling discrimination

The balanced term contains

$$
\Lambda(e)b_U(k)f(ek).
$$

This requires ordinary:

- von Mangoldt prime-power weights;
- Möbius divisor truncation;
- multiplication $ek$ ;
- additive shifts inside $f(ek)$.

The counterterm uses

$$
M_U,\quad
J_U,\quad
L_V,
$$

which are ordinary Möbius and von Mangoldt Dirichlet coefficients.

The positive pseudo-prime model of Paper 64 does not determine these quantities from its preserved properties.

A generic Beurling prime system does not identify its generalized multiplicative semigroup with the ordinary additive lattice in the required way.

Thus the new frontier remains inside the intended ordinary-prime intersection.

---

# 16. External calibration

## 16.1. Vaughan identity

The Encyclopedia of Mathematics gives the exact decomposition into:

- a first Type-I term with $\mu(d)\log r$ ;
- a second Type-I term with the truncated convolution coefficient;
- a Type-II term with
  $$
  \Lambda(e)
  \sum_{\substack{d\mid k\\d\le U}}\mu(d).
  $$

URL:

https://encyclopediaofmath.org/wiki/Vaughan_identity

## 16.2. Ford–Maynard prime-producing sieves

Ford and Maynard formulate Type I / Type II comparison estimates and record that Vaughan's identity yields an asymptotic when

$$
\gamma+\nu>1.
$$

Their more general theory shows that sufficiently strong Type-I/II information can be transferred to the prime sum without an intrinsic logarithmic extraction floor.

URL:

https://www.ford126.web.illinois.edu/wwwpapers/prime-producing-sieves.pdf

This is used only as extraction calibration; the present theorem is an exact direct computation on the signed root sequence.

---

# 17. State transition

Advance candidate state

$$
v1.67
\to
v1.68.
$$

Add:

```text
B-RH-119
LOG_WEIGHTED_SIGNED_SHIFT_ERROR_SEQUENCE_RETAINS_DETERMINISTIC_DIVISOR_DISTRIBUTION

B-RH-120
EXACT_RENORMALIZED_VAUGHAN_DECOMPOSITION_OF_THE_SIGNED_ROOT_COVARIANCE

B-RH-121
EXACT_VAUGHAN_TYPE_I_ERROR_RETAINS_FIXED_POWER_FROM_SHIFT_AVERAGED_DIVISOR_DISTRIBUTION

B-RH-122
F_RH_024_PLUS_THE_DETERMINISTIC_TYPE_I_POWER_GIVES_A_DIRECT_ROOT_COVARIANCE_EXCESS

O-RH-174
UNRENORMALIZED_VAUGHAN_TYPE_II_SMALLNESS_DISCARDS_A_NECESSARY_ONE_POINT_TRUNCATION_COUNTERTERM
```

Open:

```text
F-RH-024
RENORMALIZED_VAUGHAN_BALANCED_DEFECT_POWER
OPEN_ROOT_ARITHMETIC
```

Downgrade:

```text
F-RH-023
AUXILIARY_PARITY_CANDIDATE
```

No RH certificate is created.

---

# 18. Recommended next action

C47-B-v2 is complete.

The next round should attack F-RH-024 itself.

Do not estimate $\mathcal T^{II}_{U,V}$ absolutely.

Instead:

1. dyadically decompose $e$ and $k$ ;
2. insert the definition
   $$
   f(ek)
   =
   W(ek/N)
   \sum_r
   \omega_H(r)
   (\Lambda(ek+r)-1);
   $$
3. isolate the exact contribution corresponding to $\mathcal M_{U,V}$ ;
4. test whether the remaining balanced covariance has a large-sieve, dispersion, or Möbius-parity fixed-power saving.

This is now a concrete arithmetic theorem with an exact root bridge.

---

# 19. Conclusion

The Campaign-47 extraction problem has been solved at the structural level.

Vaughan's identity preserves the fixed-power divisor information generated by shift averaging.

The price is not logarithmic.

The real issue is that the balanced Type-II term contains an explicit one-point truncation component which must be subtracted.

After that renormalization, one single arithmetic quantity remains.

That quantity is F-RH-024.

Campaign 47 now has its first root-sufficient fixed-power inequality.
