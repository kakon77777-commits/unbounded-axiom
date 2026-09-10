# CSM_RH Paper 53

## The Exact Mean-Square Identity Behind PESC, Subendpoint Zero-Free Strips, and Endpoint Equivalence to the Riemann Hypothesis

**Project:** CSM_RH  
**Paper:** 53  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 44 — `PESC_TRIANGULAR_LAG_KERNEL_ATTACK`  
**Track:** PK5/Z4 — `OFF_CRITICAL_ANTI_CANCELLATION_OR_CRITICAL_LINE_ADMISSION`  
**Status:** Z4 STRUCTURAL CLOSURE / PK5 UNCONDITIONAL ADMISSION STILL OPEN  
**Canonical entry state:** v1.43 / Paper 52 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Papers 48–52 analyzed the PESC root energy through discrete Brownian geometry, translated-window synthesis, centered Mellin energy, the Chebyshev root error, truncated explicit formulas, and zero-window Gram estimates.

The present paper identifies the global object underlying all of those representations and thereby closes the structural part of PK5/Z4 without requiring a zero-by-zero lower Gram theorem.

Paper 48 already certified the exact identity

$$
\boxed{
J_N^\vartheta
=
\sum_{n=N}^{2N-1}
\left(
\vartheta(n)-n
\right)^2.
}
$$

Thus the PESC root energy is exactly the dyadic discrete mean square of the prime Chebyshev error.

Let

$$
E_\vartheta(x)=\vartheta(x)-x,
\qquad
E_\psi(x)=\psi(x)-x.
$$

The prime-power difference

$$
\psi(x)-\vartheta(x)
$$

is

$$
O(x^{1/2})
$$

at fixed-power resolution. Consequently, for every fixed

$$
0<\kappa\le1,
$$

the PESC target

$$
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}
$$

is exponent-equivalent to the dyadic von Mangoldt mean-square estimate

$$
\boxed{
\int_N^{2N}
|E_\psi(x)|^2\,dx
\ll
N^{3-\kappa+o(1)}.
}
$$

This immediately gives a global anti-cancellation theorem through Mellin analyticity.

For

$$
\Re s>1,
$$

$$
\boxed{
s
\int_1^\infty
E_\psi(x)x^{-s-1}\,dx
=
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{s}{s-1}.
}
$$

If PESC $(\kappa)$ holds, dyadic Cauchy–Schwarz shows that the Mellin integral converges locally uniformly throughout

$$
\Re s>
1-\frac{\kappa}{2}.
$$

The right-hand side therefore has an analytic continuation to that half-plane. Since a nontrivial zero of $\zeta$ would produce a pole of $-\zeta'/\zeta$, one obtains

$$
\boxed{
\mathrm{PESC}(\kappa)
\Longrightarrow
\zeta(s)\ne0
\quad
\text{for }
\Re s>
1-\frac{\kappa}{2}.
}
$$

By functional-equation symmetry, all nontrivial zeros must then lie in the narrower strip

$$
\boxed{
\frac{\kappa}{2}
\le
\beta
\le
1-\frac{\kappa}{2}.
}
$$

At the endpoint

$$
\kappa=1,
$$

the strip collapses to

$$
\beta=\frac12.
$$

Therefore

$$
\boxed{
\mathrm{PESC}(1)
\Longrightarrow
\mathrm{RH}.
}
$$

The converse follows from the classical RH estimate

$$
\psi(x)-x
=
O(x^{1/2+\varepsilon})
$$

for every $\varepsilon>0$, which implies

$$
J_N^\vartheta
\ll
N^{2+o(1)}.
$$

Hence

$$
\boxed{
\mathrm{PESC}(1)
\Longleftrightarrow
\mathrm{RH}
}
$$

at the exponent resolution used throughout CSM_RH.

This endpoint equivalence is independently consistent with the classical mean-square literature. Cramér proved an $O(X^2)$ dyadic mean-square bound for $\psi(x)-x$ under RH; modern work of Brent, Platt and Trudgian gives explicit constants and notes that if RH is false then the normalized dyadic mean square is unbounded.

The result does not prove RH. It recalibrates Campaign 44: endpoint PESC is not a strictly easier theorem sitting below RH. It is an RH-equivalent mean-square formulation. Subendpoint PESC yields a genuine fixed zero-free strip, while reaching the endpoint requires either a direct RH-scale mean-square theorem or a new exponent-amplification mechanism.

---

# 1. The exact PESC mean-square identity

Define

$$
c_n
=
1_{\mathbb P}(n)\log n-1
$$

and

$$
B(x)
=
\sum_{n\le x}c_n
=
\vartheta(x)-x.
$$

Paper 48 certified

$$
\boxed{
J_N^\vartheta
=
\sum_{n=N}^{2N-1}B(n)^2.
}
$$

Therefore

$$
\boxed{
J_N^\vartheta
=
\sum_{n=N}^{2N-1}
|E_\vartheta(n)|^2.
}
$$

This identity predates the Brownian diagonalization in the internal chain. The later Brownian representation is a coordinate factorization of this exact dyadic mean square.

Indeed, Paper 48 also wrote

$$
J_N^\vartheta
=
\sum_{s=0}^{N-1}
\left(
\sum_{r=0}^{s}y_r
\right)^2,
$$

where the prefix sums are exactly

$$
B(N+s).
$$

Thus the discrete Brownian covariance kernel is simply the Gram representation of cumulative prime-error values over the dyadic interval.

This observation does not invalidate Papers 49–52. It identifies what those transforms are representing.

---

# 2. Prime powers: $\vartheta$ and $\psi$ are mean-square equivalent at PESC scale

Let

$$
Q(x)
=
\psi(x)-\vartheta(x).
$$

Since

$$
\psi(x)
=
\sum_{r\ge1}
\vartheta(x^{1/r}),
$$

we have

$$
Q(x)
=
\sum_{r\ge2}
\vartheta(x^{1/r}).
$$

The Chebyshev estimate

$$
\vartheta(y)\ll y
$$

gives

$$
Q(x)
\ll
x^{1/2}
+
\sum_{3\le r\le\log_2x}
x^{1/r}.
$$

For $r\ge3$,

$$
x^{1/r}\le x^{1/3},
$$

so

$$
Q(x)
\ll
x^{1/2}
+
x^{1/3}\log x
\ll
x^{1/2}.
$$

Hence

$$
\boxed{
Q(x)\ll x^{1/2}.
}
$$

On the dyadic integer interval,

$$
\sum_{N\le n<2N}
|Q(n)|^2
\ll
N^2.
$$

Let

$$
J_N^\psi
=
\sum_{N\le n<2N}
|E_\psi(n)|^2.
$$

Because

$$
E_\psi(n)
=
E_\vartheta(n)+Q(n),
$$

the Hilbert-space triangle inequality gives

$$
\left|
(J_N^\psi)^{1/2}
-
(J_N^\vartheta)^{1/2}
\right|
\ll
N.
$$

Therefore, for every fixed

$$
0<\kappa\le1,
$$

the scale

$$
N^{3-\kappa}
$$

is at least $N^2$, and we obtain:

## Theorem 2.1 — Prime-only / von Mangoldt dyadic mean-square equivalence

For every fixed

$$
0<\kappa\le1,
$$

$$
\boxed{
J_N^\vartheta
\ll
N^{3-\kappa+o(1)}
}
$$

if and only if

$$
\boxed{
J_N^\psi
\ll
N^{3-\kappa+o(1)}.
}
$$

Create:

```text
B-RH-049
PESC_THETA_TO_PSI_DYADIC_MEAN_SQUARE_POWER_EQUIVALENCE
CERTIFIED
```

This is the physical-space analogue of Paper 50's centered prime-power Mellin removal.

---

# 3. Discrete and continuous dyadic mean squares

For

$$
n\le x<n+1,
$$

the Chebyshev function $\psi$ is constant:

$$
\psi(x)=\psi(n).
$$

Write

$$
x=n+u,
\qquad
0\le u<1.
$$

Then

$$
E_\psi(x)
=
E_\psi(n)-u.
$$

Consider the Hilbert space direct sum over the $N$ unit intervals.

The piecewise constant function

$$
x\mapsto E_\psi(\lfloor x\rfloor)
$$

has norm

$$
\left(
J_N^\psi
\right)^{1/2}.
$$

The sawtooth correction

$$
x-\lfloor x\rfloor
$$

has squared norm

$$
\frac N3.
$$

Minkowski therefore yields

$$
\boxed{
\left|
\left(
\int_N^{2N}
|E_\psi(x)|^2\,dx
\right)^{1/2}
-
(J_N^\psi)^{1/2}
\right|
\le
\sqrt{\frac N3}.
}
$$

Thus:

## Theorem 3.1 — Discrete / continuous dyadic mean-square equivalence

For every fixed

$$
0<\kappa\le1,
$$

$$
\boxed{
J_N^\psi
\ll
N^{3-\kappa+o(1)}
}
$$

if and only if

$$
\boxed{
I_\psi(N)
:=
\int_N^{2N}
|\psi(x)-x|^2\,dx
\ll
N^{3-\kappa+o(1)}.
}
$$

Combining Theorems 2.1 and 3.1:

## Corollary 3.2 — PESC is a dyadic PNT-error mean-square problem

For every fixed

$$
0<\kappa\le1,
$$

PESC $(\kappa)$ is exponent-equivalent to

$$
\boxed{
I_\psi(N)
\ll
N^{3-\kappa+o(1)}.
}
$$

This is the global physical-space meaning of the centered Mellin energy developed in Papers 49–52.

---

# 4. Mellin transform of the Chebyshev root error

Let

$$
E_\psi(x)=\psi(x)-x.
$$

For

$$
\Re s>1,
$$

absolute convergence allows

$$
\begin{aligned}
\int_1^\infty
\psi(x)x^{-s-1}\,dx
&=
\sum_{n\ge1}
\Lambda(n)
\int_n^\infty
x^{-s-1}\,dx
\\
&=
\frac1s
\sum_{n\ge1}
\frac{\Lambda(n)}{n^s}
\\
&=
-\frac1s
\frac{\zeta'(s)}{\zeta(s)}.
\end{aligned}
$$

Also,

$$
\int_1^\infty
x\,x^{-s-1}\,dx
=
\frac1{s-1}.
$$

Therefore:

## Theorem 4.1 — Exact Chebyshev-error Mellin identity

For

$$
\Re s>1,
$$

$$
\boxed{
s
\int_1^\infty
E_\psi(x)x^{-s-1}\,dx
=
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{s}{s-1}.
}
$$

The pole at $s=1$ cancels in the displayed combination.

This identity provides a global anti-cancellation mechanism. One need not isolate a single zero response if the mean-square bound itself forces the Mellin transform to be analytic across the relevant half-plane.

---

# 5. Dyadic mean square implies Mellin analyticity

Assume that for some real exponent $A$,

$$
\boxed{
I_\psi(X)
\ll
X^{A}
}
$$

for all sufficiently large dyadic $X$.

Let

$$
s=\sigma+i\tau.
$$

On the dyadic block

$$
X\le x\le2X,
$$

Cauchy–Schwarz gives

$$
\begin{aligned}
\int_X^{2X}
|E_\psi(x)|x^{-\sigma-1}\,dx
&\le
X^{-\sigma-1}
X^{1/2}
I_\psi(X)^{1/2}
\\
&\ll
X^{-\sigma-\frac12+\frac A2}.
\end{aligned}
$$

Summing over dyadic $X$ converges whenever

$$
-\sigma-\frac12+\frac A2<0.
$$

Equivalently,

$$
\boxed{
\sigma>
\frac{A-1}{2}.
}
$$

The convergence is locally uniform in every closed half-plane to the right of this boundary. Thus:

## Theorem 5.1 — Mean-square analytic-continuation lemma

If

$$
I_\psi(X)\ll X^A,
$$

then

$$
\boxed{
\int_1^\infty
E_\psi(x)x^{-s-1}\,dx
}
$$

defines an analytic function for

$$
\boxed{
\Re s>
\frac{A-1}{2}.
}
$$

By Theorem 4.1, the function

$$
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{s}{s-1}
$$

has an analytic continuation to the same region.

---

# 6. General PESC exponent implies a zero-free strip

Assume PESC $(\kappa)$ for a fixed

$$
0<\kappa\le1.
$$

By Corollary 3.2, for every $\varepsilon>0$,

$$
I_\psi(N)
\ll_\varepsilon
N^{3-\kappa+\varepsilon}.
$$

Apply Theorem 5.1 with

$$
A=3-\kappa+\varepsilon.
$$

Then the Mellin transform is analytic for

$$
\Re s>
1-\frac{\kappa}{2}
+
\frac{\varepsilon}{2}.
$$

Since $\varepsilon>0$ is arbitrary,

$$
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{s}{s-1}
$$

has no pole at any fixed point satisfying

$$
\Re s>
1-\frac{\kappa}{2}.
$$

A nontrivial zero $\rho$ of multiplicity $m$ would make

$$
-\frac{\zeta'(s)}{\zeta(s)}
$$

have a simple pole at $\rho$ with nonzero residue $-m$. The rational term has no pole there.

Therefore:

## Theorem 6.1 — PESC zero-free-strip theorem

For every fixed

$$
0<\kappa\le1,
$$

$$
\boxed{
\mathrm{PESC}(\kappa)
\Longrightarrow
\zeta(s)\ne0
\quad
\text{whenever}
\quad
\Re s>
1-\frac{\kappa}{2}.
}
$$

Create:

```text
B-RH-050
PESC_KAPPA_IMPLIES_ZERO_FREE_HALF_PLANE_RE_GT_ONE_MINUS_KAPPA_OVER_TWO
CERTIFIED
```

This is stronger than a zero-density conclusion: even one zero in the forbidden half-plane is excluded.

---

# 7. Functional-equation symmetry narrows the entire critical strip

Nontrivial zeros of $\zeta$ are symmetric about the critical line:

$$
\rho
\longmapsto
1-\overline\rho.
$$

Suppose PESC $(\kappa)$ holds.

Theorem 6.1 excludes

$$
\beta>
1-\frac{\kappa}{2}.
$$

If a zero satisfied

$$
\beta<
\frac{\kappa}{2},
$$

then its reflected zero would have real part

$$
1-\beta
>
1-\frac{\kappa}{2},
$$

contradicting Theorem 6.1.

Therefore:

## Corollary 7.1 — Symmetric strip contraction

PESC $(\kappa)$ implies that every nontrivial zero satisfies

$$
\boxed{
\frac{\kappa}{2}
\le
\beta
\le
1-\frac{\kappa}{2}.
}
$$

Thus the PESC exponent has a direct geometric meaning in the critical strip.

For

$$
\kappa<1,
$$

PESC $(\kappa)$ gives a genuine fixed-width zero-free region but does not by itself force the critical line.

At

$$
\kappa=1,
$$

the interval collapses.

---

# 8. Endpoint implication: PESC $(1)$ implies RH

Set

$$
\kappa=1.
$$

Corollary 7.1 gives

$$
\frac12
\le
\beta
\le
\frac12.
$$

Therefore:

## Theorem 8.1 — Endpoint PESC implies RH

$$
\boxed{
\mathrm{PESC}(1)
\Longrightarrow
\mathrm{RH}.
}
$$

Equivalently, if RH is false, then the endpoint estimate

$$
J_N^\vartheta
\ll
N^{2+o(1)}
$$

cannot hold.

This is a global anti-cancellation theorem. It avoids any need to prove that one off-critical zero dominates a finite local zero cluster in the response kernel.

If off-critical zeros collectively cancelled strongly enough to make the endpoint dyadic mean square $N^{2+o(1)}$, the Mellin transform would analytically continue across their poles, which is impossible.

Thus the analytic-continuation argument supplies the coercivity that Z4 sought.

---

# 9. Converse: RH implies endpoint PESC

A classical equivalent formulation of RH is that for every

$$
\varepsilon>0,
$$

$$
\boxed{
\psi(x)-x
=
O_\varepsilon
\left(
x^{1/2+\varepsilon}
\right).
}
$$

Therefore

$$
I_\psi(N)
\ll_\varepsilon
N
\cdot
N^{1+2\varepsilon}
=
N^{2+2\varepsilon}.
$$

Since $\varepsilon>0$ is arbitrary,

$$
\boxed{
I_\psi(N)
\ll
N^{2+o(1)}.
}
$$

By Theorems 2.1 and 3.1,

$$
\boxed{
J_N^\vartheta
\ll
N^{2+o(1)}.
}
$$

Thus:

## Theorem 9.1 — Endpoint PESC / RH equivalence

At the exponent resolution used in CSM_RH,

$$
\boxed{
\mathrm{PESC}(1)
\Longleftrightarrow
\mathrm{RH}.
}
$$

Create:

```text
B-RH-051
PESC_ENDPOINT_KAPPA_ONE_EQUIVALENT_TO_RH_AT_EXPONENT_RESOLUTION
CERTIFIED
```

This is an equivalence theorem, not an RH certificate.

---

# 10. Relation to classical mean-square prime-number-theorem results

The endpoint scale is classical.

Cramér proved under RH that the dyadic mean square

$$
I_\psi(X)
=
\int_X^{2X}
(\psi(x)-x)^2\,dx
$$

is

$$
O(X^2).
$$

Brent, Platt and Trudgian later proved explicit upper and lower constants under RH and an unconditional positive lower bound. Their 2020/2022 work states in particular that if RH is false then

$$
\boxed{
I_\psi(X)/X^2
}
$$

is unbounded.

This is fully consistent with Theorem 9.1.

Their result also shows that even under RH the normalized mean square need not converge. Thus endpoint PESC should be interpreted as a scale bound, not as convergence to a universal constant.

The contribution of the present internal chain is not the invention of prime-error mean-square theory. It is the exact identification of the CSM_RH PESC root object with that theory and the reconciliation of the Brownian, Mellin, Abel and zero-window representations with the classical physical-space mean square.

---

# 11. What Papers 49–52 now mean

The new equivalence does not make Papers 49–52 false.

It changes their role.

## Paper 49

The Brownian root kernel was moved, with power-safe distortion, to a centered Mellin energy.

This is a frequency-space representation of the dyadic prime-error mean square.

## Paper 50

Prime powers were removed in the centered Mellin transform and the statistic was rewritten exactly as an Abel transform of

$$
\psi(x)-x.
$$

This is the transform-side analogue of Theorem 2.1.

## Paper 51

The truncated explicit formula inserted the zeta zeros and extracted the exact discrete response

$$
m^{i(\gamma-t)}.
$$

This explains spectrally why an off-critical real part contributes the scale

$$
N^{\beta-1}.
$$

## Paper 52

Zero-window Gram geometry was reduced to only polylogarithmic loss, leaving the weighted beta mass

$$
\sum
\frac{
N^{2\beta-2}
}{
(1+|\gamma|)^2
}.
$$

This is a local spectral version of the same exponent obstruction.

## Paper 53

The Mellin analytic-continuation argument shows that the global dyadic mean-square endpoint already detects every off-critical zero at once.

Thus finite-cluster lower Gram analysis is no longer required for the endpoint converse.

It may still be useful for quantitative or local refinements.

---

# 12. Z4 closure

The original Z4 target was:

```text
OFF_CRITICAL_ANTI_CANCELLATION_OR_CRITICAL_LINE_ADMISSION
```

The required anti-cancellation is now supplied globally.

If PESC $(1)$ held while an off-critical zero existed, Theorem 5.1 would analytically continue

$$
-\zeta'/\zeta
$$

through a genuine zero pole.

That is impossible.

Therefore close Z4 as:

```text
CLOSED_AS_GLOBAL_MELLIN_ANALYTICITY_ANTI_CANCELLATION_AND_ENDPOINT_RH_EQUIVALENCE
```

Add:

```text
O-RH-131
ENDPOINT_PESC_IS_RH_EQUIVALENT_NOT_A_STRICTLY_EASIER_INTERMEDIATE_THEOREM
CERTIFIED_AS_CAMPAIGN_RECALIBRATION
```

This is a methodological warning.

---

# 13. PK5 status after Z4

All structural subtracks are now closed:

```text
Z1 CLOSED
TRUNCATED_EXPLICIT_FORMULA_INSERTION

Z2 CLOSED
EXACT_DISCRETE_ZERO_RESPONSE

Z3 CLOSED
ZERO_ORDINATE_GEOMETRY_TO_WEIGHTED_BETA_MASS

Z4 CLOSED
GLOBAL_MELLIN_ANTI_CANCELLATION_AND_ENDPOINT_RH_EQUIVALENCE
```

However, PK5 itself is not proved unconditionally.

The remaining statement

$$
\boxed{
J_N^\vartheta
\ll
N^{2+o(1)}
}
$$

is now known internally to be RH-equivalent.

Therefore record PK5 as:

```text
OPEN_UNCONDITIONAL_ENDPOINT_ADMISSION_RH_EQUIVALENT
```

Do not write

```text
PK5 CLOSED
```

in the theorem sense.

---

# 14. Consequence for subendpoint campaigns

Theorem 6.1 provides a useful calibration for any future fixed-power result.

Suppose one proves PESC $(\kappa_0)$ for some

$$
0<\kappa_0<1.
$$

Then the result is nontrivial:

$$
\zeta(s)\ne0
\quad
\text{for}
\quad
\Re s>
1-\frac{\kappa_0}{2},
$$

and all nontrivial zeros lie in

$$
\frac{\kappa_0}{2}
\le
\Re s
\le
1-\frac{\kappa_0}{2}.
$$

But this alone is not RH.

Therefore a subendpoint proof can reach RH only if accompanied by an amplification mechanism.

A possible future architecture is

$$
\boxed{
\kappa_0
\longmapsto
\Phi(\kappa_0)
>
\kappa_0
}
$$

where the new zero-free strip or another arithmetic theorem improves the PESC exponent, and the map can be iterated toward

$$
\kappa=1.
$$

No such amplifier is proved here.

This is a more precise role for the secondary frontier F-RH-016 / MLEPG.

---

# 15. Recommended next campaign

Campaign 44 has completed the structural analysis of PESC.

It should not continue producing additional coordinate systems for the same endpoint unless they provide a genuine new inequality.

The recommended next mathematical fork is:

## Route A — Direct endpoint mean-square attack

Attack

$$
\sum_{N\le n<2N}
|\vartheta(n)-n|^2
\ll
N^{2+o(1)}
$$

directly.

This is RH-equivalent.

## Route B — Subendpoint-to-endpoint exponent amplification

First prove

$$
J_N^\vartheta
\ll
N^{3-\kappa_0+o(1)}
$$

for some fixed

$$
\kappa_0>0,
$$

then prove an independent theorem that upgrades

$$
\kappa
\mapsto
\Phi(\kappa)>\kappa.
$$

Iterate if possible.

## Route C — Return to F-RH-016 / MLEPG

Determine whether MLEPG contains structure stronger than the global PESC mean square and can generate such an amplifier rather than merely reformulating PESC.

The recommended next campaign is therefore:

```text
CAMPAIGN 45
PESC_EXPONENT_AMPLIFICATION_OR_MLEPG_BOOTSTRAP
```

with the first audit:

```text
EA1
DOES_F_RH_016_IMPLY_A_STRICT_PESC_EXPONENT_IMPROVEMENT?
```

---

# 16. External calibration

## 16.1. Zeta zero symmetry

NIST DLMF Section 25.10 records that the nontrivial zeros are symmetric about both the real axis and the critical line.

https://dlmf.nist.gov/25.10

## 16.2. RH and the Chebyshev error

NIST DLMF Section 25.16 records the classical equivalence

$$
\mathrm{RH}
\Longleftrightarrow
\psi(x)
=
x+O(x^{1/2+\varepsilon})
$$

for every $\varepsilon>0$.

https://dlmf.nist.gov/25.16

## 16.3. Mean square of the PNT error

Richard P. Brent, David J. Platt, and Timothy S. Trudgian,
*The mean square of the error term in the prime number theorem*,
Journal of Number Theory 238 (2022), 740–762.

Preprint:

https://arxiv.org/abs/2008.06140

They prove an explicit $O(X^2)$ dyadic mean-square upper bound under RH, an unconditional positive $X^2$ lower bound, and note that if RH is false then the normalized mean square is unbounded.

These results independently validate the endpoint scale identified here.

---

# 17. State transition

Advance the candidate research state from

$$
v1.43
$$

to

$$
v1.44.
$$

Add:

```text
B-RH-049
PESC_THETA_TO_PSI_DYADIC_MEAN_SQUARE_POWER_EQUIVALENCE
CERTIFIED
```

Add:

```text
B-RH-050
PESC_KAPPA_IMPLIES_ZERO_FREE_HALF_PLANE_RE_GT_ONE_MINUS_KAPPA_OVER_TWO
CERTIFIED
```

Add:

```text
B-RH-051
PESC_ENDPOINT_KAPPA_ONE_EQUIVALENT_TO_RH_AT_EXPONENT_RESOLUTION
CERTIFIED
```

Add:

```text
O-RH-131
ENDPOINT_PESC_IS_RH_EQUIVALENT_NOT_A_STRICTLY_EASIER_INTERMEDIATE_THEOREM
CERTIFIED_AS_CAMPAIGN_RECALIBRATION
```

Track state:

```text
PK5/Z1 CLOSED
PK5/Z2 CLOSED
PK5/Z3 CLOSED
PK5/Z4 CLOSED_STRUCTURALLY

PK5 OPEN_UNCONDITIONAL_ENDPOINT_ADMISSION_RH_EQUIVALENT
```

Campaign 44 state:

```text
STRUCTURAL_REDUCTION_COMPLETE
ROOT_THEOREM_OPEN
```

No RH certificate is created.

---

# 18. Conclusion

Campaign 44 has reached its conceptual endpoint.

The exact chain is now

$$
\boxed{
\begin{aligned}
\mathrm{PESC}
&\longleftrightarrow
\text{Brownian root energy}
\\
&\longleftrightarrow
\text{centered Mellin energy}
\\
&\longleftrightarrow
\text{centered Abel transform of }\psi-x
\\
&\longleftrightarrow
\text{zero-response ensemble}
\\
&\longleftrightarrow
\text{dyadic mean square of the PNT error}.
\end{aligned}
}
$$

At a general fixed exponent,

$$
\boxed{
\mathrm{PESC}(\kappa)
\Longrightarrow
\frac{\kappa}{2}
\le
\Re\rho
\le
1-\frac{\kappa}{2}.
}
$$

At the endpoint,

$$
\boxed{
\mathrm{PESC}(1)
\Longleftrightarrow
\mathrm{RH}.
}
$$

This does not solve RH.

It tells us exactly what would solve it.

The next useful theorem must therefore do more than re-express the endpoint. It must create an actual exponent improvement, an iterative amplification, or a genuinely stronger mesoscopic inequality.
