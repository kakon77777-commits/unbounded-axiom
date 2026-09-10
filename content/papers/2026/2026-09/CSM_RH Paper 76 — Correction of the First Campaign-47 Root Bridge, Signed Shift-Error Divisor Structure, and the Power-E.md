# CSM_RH Paper 76

## Correction of the First Campaign-47 Root Bridge, Signed Shift-Error Divisor Structure, and the Power-Extraction Fork

**Project:** CSM_RH  
**Paper:** 76  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 47 — `ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Status:** PAPER-75 ROOT-BRIDGE CLAIM CORRECTED / SIGNED ROOT SEQUENCE IDENTIFIED / VAUGHAN POWER-TRANSFER AUDITED / F-RH-023 NOT YET ROOT-SUFFICIENT  
**Canonical entry state:** v1.66 / Paper 75 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 75 opened Campaign 47 by introducing the nonnegative shift-averaged sequence

$$
a_{N,H}(n)
=
W(n/N)
\sum_r
\omega_H(r)\Lambda(n+r)
$$

and the Friedlander–Iwaniec-type fixed-power bilinear candidate F-RH-023.

It also suggested that a fixed-power prime-detection asymptotic

$$
\sum_n
a_{N,H}(n)\Lambda(n)
=
A(N,H)
+
O
\left(
A(N,H)N^{-\eta}
\right)
$$

would directly yield a fixed-power root pair residual.

That implication is false at fixed-power resolution.

The present paper corrects it and identifies the correct signed root sequence.

Let

$$
\boxed{
Q_H(n)
=
\sum_r
\omega_H(r)
\left(
\Lambda(n+r)-1
\right)
}
$$

and

$$
\boxed{
f_{N,H}(n)
=
W(n/N)Q_H(n).
}
$$

Define

$$
F(N,H)
=
\sum_n f_{N,H}(n).
$$

Then the weighted root pair covariance is exactly

$$
\boxed{
\mathcal R_W(N,H)
=
\sum_n
W(n/N)
\left(
\Lambda(n)-1
\right)
Q_H(n)
=
\sum_n
\Lambda(n)f_{N,H}(n)
-
F(N,H).
}
$$

Thus the root problem is a **signed prime-detection discrepancy** for $f_{N,H}$.

The nonnegative Paper-75 sequence is merely

$$
\boxed{
a_{N,H}(n)
=
H\,W(n/N)
+
f_{N,H}(n)
}
$$

because

$$
\sum_r\omega_H(r)=H.
$$

Let

$$
\mathcal P(N,H)
=
\sum_n
\Lambda(n)a_{N,H}(n),
$$

$$
A(N,H)
=
\sum_n
a_{N,H}(n),
$$

$$
L_W(N)
=
\sum_n
W(n/N)\Lambda(n),
$$

and

$$
M_W(N)
=
\sum_n
W(n/N).
$$

Then one has the exact identity

$$
\boxed{
\mathcal P(N,H)-A(N,H)
=
H
\left(
L_W(N)-M_W(N)
\right)
+
\mathcal R_W(N,H).
}
$$

Therefore an asymptotic

$$
\mathcal P=A+O(AN^{-\eta})
$$

implies only

$$
\boxed{
\mathcal R_W
=
-H(L_W-M_W)
+
O(AN^{-\eta}).
}
$$

Under PESC $(\kappa)$ with

$$
d=\frac{\kappa}{2},
$$

the one-point prime error satisfies only

$$
L_W-M_W
\ll
N^{1-d+o(1)}.
$$

Hence the leftover term has scale

$$
\boxed{
H(L_W-M_W)
\ll
NH
N^{-d+o(1)}.
}
$$

This is much larger than the F-RH-022 target

$$
NHN^{-\kappa-\eta}
=
NHN^{-2d-\eta}.
$$

A smooth rightmost-zero mode saturates the $N^{-d}$ one-point scale.

Thus the Paper-75 first-order prime-detection bridge is corrected.

The signed sequence $f_{N,H}$ nevertheless retains the strongest useful feature of Paper 75.

For

$$
F_d(N,H)
=
\sum_{d\mid n}
f_{N,H}(n),
$$

one has

$$
\boxed{
F_d(N,H)
=
\frac{F(N,H)}{d}
+
O_W(N)
}
$$

uniformly in $d$.

Indeed,

$$
f_{N,H}
=
a_{N,H}
-
H W_N,
$$

Paper 75 gives

$$
A_d=\frac Ad+O_W(N),
$$

and smooth lattice sampling gives

$$
\sum_{d\mid n}W(n/N)
=
\frac1d
\sum_nW(n/N)
+
O_W(1).
$$

Subtracting yields the claim.

Thus even though $f_{N,H}$ is signed and may have seed-sized total mass, its **divisor discrepancy around its own mean remains deterministic and power-good**.

The paper next audits direct Vaughan extraction.

Ford and Maynard record the standard fact that if a comparison sequence difference $w_n$ has Type I range parameter $\gamma$ and Type II width $\nu$ with

$$
\boxed{
\gamma+\nu>1,
}
$$

then Vaughan's identity gives an asymptotic for

$$
\sum\Lambda(n)w_n.
$$

More generally their 2024 theory classifies precisely when Type I/II ranges force an asymptotic, and shows that this agrees with the Heath–Brown identity criterion.

Thus exact combinatorial identities do not intrinsically have the logarithmic extraction floor of the 1998 generic asymptotic sieve.

However two barriers remain.

First, the F-RH-023 bilinear form of Paper 75 is **not the Vaughan balanced term**.

Vaughan's identity produces the Type-II coefficient

$$
\boxed{
b_V(k)
=
\sum_{\substack{d\mid k\\d\le V}}
\mu(d)
}
$$

paired with an outer von Mangoldt coefficient:

$$
\boxed{
\sum_{m>U}
\Lambda(m)
\sum_k
b_V(k)
f_{N,H}(mk).
}
$$

F-RH-023 instead uses the Friedlander–Iwaniec form

$$
\gamma(n,C)\mu(mn)a_{N,H}(mn)
$$

inside an absolute sum over $m$.

There is no formal implication between these two bilinear estimates.

Second, the two standard power-extraction routes use different information.

### Route A — aggregate asymptotic sieve

The Paper-75 divisor law

$$
A_d=A/d+O(N)
$$

and its signed counterpart

$$
F_d=F/d+O(N)
$$

give strong full-divisor information.

The Friedlander–Iwaniec asymptotic sieve is built for this information and for the special Möbius parity axiom F-RH-023.

But its published generic prime-detection output has only logarithmic relative accuracy.

### Route B — Vaughan / Heath–Brown exact identities

These identities can preserve fixed-power Type I/II errors into the final prime sum.

But their Type-II forms are more general or structurally different from F-RH-023.

If one uses the Ford–Maynard comparison setup, the required interval-uniform Type-I information includes the $m=1$ prime-error mode. A PESC seed supplies only exponent

$$
d=\kappa/2,
$$

and a boundary mode saturates it.

Therefore the generic comparison-sequence route cannot by itself produce the required root exponent $>\kappa$.

This creates the **Campaign-47 extraction fork**:

```text
strong aggregate divisor information
+ F-RH-023
    -> generic asymptotic sieve
    -> logarithmic extraction floor;

exact power-preserving Vaughan/Heath-Brown extraction
    -> requires a different balanced Type-II input
       and interval-level information whose generic seed component is critical.
```

The correct next task is not to prove F-RH-023 yet.

It is to derive a **special exact Vaughan/Heath–Brown identity for the signed root sequence $f_{N,H}$**, track the full $F_d=F/d+O(N)$ main terms rather than replacing them by a smooth comparison sequence, and identify the exact renormalized balanced form which remains after subtracting the root mean $F$.

Only after that form is written explicitly should Campaign 47 choose its next fixed-power arithmetic axiom.

No RH theorem is claimed.

---

# 1. The triangular kernel identity

For integer $H\ge1$,

$$
\omega_H(r)
=
\left(
1-\frac{|r|}{H}
\right)_+.
$$

One has exactly

$$
\boxed{
\sum_{r\in\mathbb Z}\omega_H(r)=H.
}
$$

Therefore

$$
\begin{aligned}
a_{N,H}(n)
&=
W(n/N)
\sum_r
\omega_H(r)\Lambda(n+r)
\\
&=
\boxed{
H W(n/N)
+
f_{N,H}(n).
}
\end{aligned}
$$

---

# 2. Correct signed root sequence

Define

$$
Q_H(n)
=
\sum_r
\omega_H(r)
\left(
\Lambda(n+r)-1
\right)
$$

and

$$
f_{N,H}(n)
=
W(n/N)Q_H(n).
$$

The weighted pair covariance is

$$
\begin{aligned}
\mathcal R_W
&=
\sum_n
W(n/N)
(\Lambda(n)-1)
\sum_r
\omega_H(r)
(\Lambda(n+r)-1)
\\
&=
\boxed{
\sum_n
(\Lambda(n)-1)f_{N,H}(n).
}
\end{aligned}
$$

Let

$$
F=\sum_n f_{N,H}(n).
$$

Then:

## Theorem 2.1 — Root covariance as signed prime-detection discrepancy

$$
\boxed{
\mathcal R_W
=
\sum_n
\Lambda(n)f_{N,H}(n)
-
F.
}
$$

Create:

```text
B-RH-117
ROOT_PAIR_COVARIANCE_IS_EXACTLY_SIGNED_PRIME_DETECTION_MINUS_SIGNED_TOTAL_MASS
CERTIFIED
```

---

# 3. Correction to the Paper-75 nonnegative bridge

Let

$$
\mathcal P
=
\sum_n
\Lambda(n)a_{N,H}(n),
$$

$$
A
=
\sum_n
a_{N,H}(n),
$$

$$
L_W
=
\sum_n
W(n/N)\Lambda(n),
$$

and

$$
M_W
=
\sum_n
W(n/N).
$$

Using

$$
a_{N,H}=HW_N+f_{N,H},
$$

$$
\mathcal P
=
H L_W
+
\sum_n
\Lambda(n)f_{N,H}(n),
$$

and

$$
A
=
H M_W
+
F.
$$

Subtracting and using Theorem 2.1:

## Theorem 3.1 — Exact nonnegative prime-detection correction

$$
\boxed{
\mathcal P-A
=
H(L_W-M_W)
+
\mathcal R_W.
}
$$

Hence:

$$
\boxed{
\mathcal P=A+E
\quad\Longrightarrow\quad
\mathcal R_W
=
-H(L_W-M_W)
+
E.
}
$$

Create correction:

```text
C-RH-005
PAPER75_FIRST_ORDER_PRIME_DETECTION_DOES_NOT_DIRECTLY_CONTROL_THE_CENTERED_ROOT_PAIR_RESIDUAL
```

---

# 4. Fixed-power size of the omitted one-point term

Assume PESC $(\kappa)$ and put

$$
d=\frac{\kappa}{2}.
$$

The smoothed PNT error satisfies

$$
\boxed{
L_W-M_W
\ll
N^{1-d+o(1)}.
}
$$

Therefore

$$
\boxed{
H(L_W-M_W)
\ll
NH
N^{-d+o(1)}.
}
$$

The root pair-residual amplifier requires an exponent strictly beyond

$$
\kappa=2d.
$$

Thus first-order prime detection relative to $A$ leaves a term with only half the required exponent.

Create:

```text
O-RH-170
FIRST_ORDER_PRIME_DETECTION_LEAVES_A_ONE_POINT_BOUNDARY_TERM_AT_EXPONENT_KAPPA_OVER_TWO
CERTIFIED
```

---

# 5. Smooth boundary-mode sharpness

Take the standard synthetic prime-error density

$$
e_\rho(n)
\asymp
n^{-d+i\gamma},
$$

corresponding to a PNT error mode

$$
x^{1-d+i\gamma}.
$$

Then for smooth $W$,

$$
\sum_n
W(n/N)e_\rho(n)
\asymp_\rho
N^{1-d+i\gamma}.
$$

Hence

$$
H(L_W-M_W)
$$

has the natural boundary scale

$$
\boxed{
HN^{1-d}
=
NHN^{-d}.
}
$$

Thus O-RH-170 is sharp in the canonical boundary model.

---

# 6. Signed divisor distribution survives

Define

$$
F_d
=
\sum_{d\mid n}
f_{N,H}(n).
$$

Paper 75 gives

$$
A_d
=
\frac Ad
+
O_W(N).
$$

Smooth lattice sampling gives

$$
M_{W,d}
:=
\sum_{d\mid n}
W(n/N)
=
\frac{M_W}{d}
+
O_W(1).
$$

Since

$$
f_{N,H}
=
a_{N,H}
-
H W_N,
$$

$$
F=A-HM_W.
$$

Therefore:

## Theorem 6.1 — Signed root-sequence divisor law

$$
\boxed{
F_d
=
\frac Fd
+
O_W(N).
}
$$

Create:

```text
B-RH-118
SIGNED_SHIFT_ERROR_SEQUENCE_RETAINS_DETERMINISTIC_DIVISOR_DISTRIBUTION_AROUND_ITS_OWN_MEAN
CERTIFIED
```

This theorem contains no prime-in-progressions input.

---

# 7. Power remainder for the signed sequence

Let

$$
r_d^\circ
=
F_d-\frac Fd.
$$

Then

$$
|r_d^\circ|
\ll_W N.
$$

Hence

$$
\boxed{
\sum_{d\le D}
\mu^2(d)\tau_5(d)
|r_d^\circ|
\ll_W
ND(\log N)^{O(1)}.
}
$$

Relative to the natural root second-order scale

$$
NH,
$$

this has exponent

$$
\boxed{
1-\tau-\frac{\log D}{\log N}.
}
$$

At

$$
D=N^{2/3+\varepsilon},
$$

the exponent is again

$$
\boxed{
\frac13-\tau-\varepsilon.
}
$$

So the strong aggregate Type-I side survives the correction to the signed root sequence.

---

# 8. Exact Vaughan balanced coefficient

Vaughan's identity may be written, for suitable $U,V$, as

$$
\Lambda
=
a_1+a_2+a_3+a_4,
$$

where the balanced term has the form

$$
\boxed{
a_4(n)
=
-
\sum_{\substack{mk=n\\m>U}}
\Lambda(m)
b_V(k),
}
$$

with

$$
\boxed{
b_V(k)
=
\sum_{\substack{d\mid k\\d\le V}}
\mu(d),
}
$$

up to the standard support restrictions associated with the chosen version of the identity.

Thus, applied to $f_{N,H}$, the balanced contribution is a dyadic sum built from

$$
\boxed{
\Lambda(m)b_V(k)f_{N,H}(mk).
}
$$

External calibration:

the Encyclopedia of Mathematics formulation of Vaughan's identity identifies the first pieces as Type I and the last piece as Type II.

---

# 9. F-RH-023 is not the Vaughan Type-II input

Paper 75 defined

$$
\mathfrak B_{N,H}(L,C)
=
\sum_m
\left|
\sum_{L<n\le2L}
\gamma(n,C)
\mu(mn)
a_{N,H}(mn)
\right|.
$$

Its coefficient structure is

$$
\boxed{
\gamma(n,C)\mu(mn).
}
$$

Vaughan's balanced term instead has

$$
\boxed{
\Lambda(m)b_V(n).
}
$$

These are not the same bilinear form.

No divisor identity makes a fixed-power estimate for one automatically imply a fixed-power estimate for the other.

Create:

```text
O-RH-171
PAPER75_F_RH_023_DOES_NOT_FORMALLY_CONTROL_THE_VAUGHAN_BALANCED_TERM
CERTIFIED
```

Thus F-RH-023 cannot yet be inserted into an exact Vaughan power-output proof.

---

# 10. Ford–Maynard power-transfer calibration

Ford and Maynard formulate general Type I and Type II estimates for a comparison difference $w_n=a_n-b_n$.

They record that Vaughan's identity gives an asymptotic whenever

$$
\boxed{
\gamma+\nu>1,
}
$$

where $\gamma$ is the Type-I parameter and $\nu$ is the width of the Type-II interval.

Their Theorem 2.2 gives the broader exact combinatorial criterion for when Type I/II information guarantees an asymptotic and explains that this criterion agrees with what Heath–Brown's identity can deliver.

Therefore:

## Calibration 10.1

Exact Vaughan / Heath–Brown identities can preserve quantitative Type I/II information into the prime-detection output.

There is no intrinsic generic logarithmic extraction floor in the identity itself.

This is different from the 1998 generic asymptotic-sieve theorem.

---

# 11. Why the generic comparison route is still seed-limited

The Ford–Maynard Type-I hypothesis is interval-uniform and includes the case

$$
m=1.
$$

For a comparison between the normalized shifted-prime density and a smooth model, the $m=1$ component contains a smoothed prime-number-theorem error.

PESC $(\kappa)$ supplies fixed exponent only

$$
\boxed{
d=\frac{\kappa}{2}.
}
$$

A rightmost boundary mode saturates this exponent.

Hence a generic comparison-sequence Vaughan theorem can preserve a fixed power, but the available seed Type-I power is not supercritical for the root pair problem.

Record:

```text
O-RH-172
GENERIC_VAUGHAN_COMPARISON_TYPE_I_INPUT_IS_LIMITED_BY_THE_ONE_POINT_SEED_EXPONENT
CERTIFIED_AS_SEED_METHOD_BARRIER
```

---

# 12. The Campaign-47 power-extraction fork

The two available architectures now have complementary strengths and weaknesses.

## Aggregate asymptotic-sieve route

Input:

$$
F_d=\frac Fd+O(N)
$$

to high level, plus a special Möbius parity bilinear estimate such as F-RH-023.

Strength:

the aggregate divisor input has fixed exponent potentially larger than $\kappa$.

Weakness:

the published generic prime-detection extraction has a logarithmic floor.

## Exact Vaughan / Heath–Brown route

Input:

interval-uniform Type I plus its own balanced Type-II family.

Strength:

fixed-power input can survive to fixed-power prime output.

Weakness:

the generic Type-I comparison sees the one-point seed mode, and F-RH-023 is not its Type-II form.

Thus:

```text
O-RH-173
CAMPAIGN47_POWER_EXTRACTION_FORK
CERTIFIED
```

Neither standard route currently converts F-RH-023 into F-RH-022.

---

# 13. Correct status of F-RH-023

F-RH-023 remains a meaningful ordinary-factorization parity statement.

It passes the pseudo-prime and Beurling discrimination tests.

But after the present correction:

```text
F-RH-023
OPEN_PARITY_INPUT_CANDIDATE

ROOT_SUFFICIENCY:
NOT CERTIFIED
```

Campaign 47 should not spend the next round proving F-RH-023 before resolving the exact extraction form.

---

# 14. Correct C47-B target

The next task is now narrower.

Apply an exact Vaughan or Heath–Brown identity directly to the signed root sequence

$$
f_{N,H}(n).
$$

For each Type-I piece:

1. keep the main term
   $$
   F_d=\frac Fd
   $$
   exactly;
2. use only the deterministic error
   $$
   O(N);
   $$
3. track logarithmic quotient weights as separate smooth divisor moments.

Then identify the balanced remainder after subtracting the root mean $F$.

The output should be an exact decomposition of the form

$$
\boxed{
\mathcal R_W(N,H)
=
\mathcal M_{\rm 1pt}(N,H;U,V)
+
\mathcal V_{\rm bal}(N,H;U,V)
+
O
\left(
NH
N^{-(1/3-\tau)+o(1)}
\right),
}
$$

where:

- $\mathcal M_{\rm 1pt}$ is an explicit finite combination of one-point prime-error moments;
- $\mathcal V_{\rm bal}$ is a genuinely ordinary-factorization balanced form.

Only after $\mathcal V_{\rm bal}$ and $\mathcal M_{\rm 1pt}$ are explicit should the next arithmetic inequality be chosen.

This is C47-B v2.

---

# 15. Why this correction is useful

Paper 75 had the right idea that shift averaging makes local divisibility easy.

The mistake was identifying first-order prime detection of a nonnegative lift with the centered root covariance.

Paper 76 preserves the useful part:

$$
\boxed{
F_d=F/d+O(N)
}
$$

for the **actual signed root sequence**.

Thus the campaign does not return to Campaign-46 representation loops.

The next unknown is now a concrete exact-identity bookkeeping problem.

---

# 16. External calibration

## 16.1. Ford–Maynard, 2024

K. Ford and J. Maynard,
*On the theory of prime producing sieves*,
arXiv:2407.14368.

They define general Type I and Type II comparison estimates.

They note that Vaughan's identity gives an asymptotic if

$$
\gamma+\nu>1,
$$

and their Theorem 2.2 gives a necessary/sufficient combinatorial criterion for when the Type I/II ranges force an asymptotic.

URL:

https://www.ford126.web.illinois.edu/wwwpapers/prime-producing-sieves.pdf

## 16.2. Vaughan identity

A standard exact form writes the von Mangoldt function as Type-I pieces plus a balanced Type-II piece containing

$$
\Lambda(m)
\sum_{\substack{d\mid k\\d\le V}}\mu(d).
$$

URL:

https://encyclopediaofmath.org/wiki/Vaughan_identity

## 16.3. Opera de Cribro asymptotic identities

Friedlander and Iwaniec explain that Chapter 18 develops prime sums as special linear forms, bilinear forms and small terms, with the bilinear part breaking the parity barrier.

This confirms that exact/asymptotic identity extraction and generic sieve extraction are distinct architectures.

---

# 17. State transition

Advance candidate state

$$
v1.66
\to
v1.67.
$$

Add:

```text
B-RH-117
ROOT_PAIR_COVARIANCE_IS_EXACTLY_SIGNED_PRIME_DETECTION_MINUS_SIGNED_TOTAL_MASS
CERTIFIED

B-RH-118
SIGNED_SHIFT_ERROR_SEQUENCE_RETAINS_DETERMINISTIC_DIVISOR_DISTRIBUTION_AROUND_ITS_OWN_MEAN
CERTIFIED

C-RH-005
PAPER75_FIRST_ORDER_PRIME_DETECTION_DOES_NOT_DIRECTLY_CONTROL_THE_CENTERED_ROOT_PAIR_RESIDUAL

O-RH-170
FIRST_ORDER_PRIME_DETECTION_LEAVES_A_ONE_POINT_BOUNDARY_TERM_AT_EXPONENT_KAPPA_OVER_TWO
CERTIFIED

O-RH-171
PAPER75_F_RH_023_DOES_NOT_FORMALLY_CONTROL_THE_VAUGHAN_BALANCED_TERM
CERTIFIED

O-RH-172
GENERIC_VAUGHAN_COMPARISON_TYPE_I_INPUT_IS_LIMITED_BY_THE_ONE_POINT_SEED_EXPONENT
CERTIFIED_AS_SEED_METHOD_BARRIER

O-RH-173
CAMPAIGN47_POWER_EXTRACTION_FORK
CERTIFIED
```

Update:

```text
F-RH-023
OPEN_PARITY_INPUT_CANDIDATE
ROOT_SUFFICIENCY_NOT_CERTIFIED
```

Next:

```text
C47-B-v2
EXACT_VAUGHAN_DECOMPOSITION_OF_THE_SIGNED_ROOT_SEQUENCE
```

No RH certificate is created.

---

# 18. Conclusion

Campaign 47 survives its first correction.

The nonnegative shift-averaged sequence of Paper 75 is useful for local divisibility, but first-order prime detection of that sequence does not control the centered root pair residual at fixed-power resolution.

The correct root object is the signed shift-error sequence

$$
f_{N,H}(n)
=
W(n/N)
\sum_r
\omega_H(r)(\Lambda(n+r)-1).
$$

It retains the deterministic divisor law

$$
F_d=F/d+O(N).
$$

The remaining challenge is to build an exact prime-detection decomposition which uses this strong aggregate law while exposing a balanced ordinary-factorization term at fixed-power accuracy.

That exact decomposition must be completed before Campaign 47 commits to F-RH-023 or any replacement bilinear axiom.
