# CSM_RH Paper 64

## Selberg-Symmetry Boundary Saturation, Sparse Integer Pseudo-Primes, and the Ordinary-Arithmetic Residual

**Project:** CSM_RH  
**Paper:** 64  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Track:** PT6 — `DIRECT_LOW_MELLIN_FREQUENCY_BOUNDARY_PACKET_SUPPRESSION`  
**Status:** STANDARD LOW-FREQUENCY STRUCTURAL ROUTES FURTHER NARROWED / ORDINARY-ARITHMETIC EXCESS REMAINS OPEN  
**Canonical entry state:** v1.54 / Paper 63 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 63 showed that the remaining PESC amplifier obstruction is not the high-frequency Type-II residual but the critical low-Mellin-frequency boundary packet. The present paper tests whether three additional pieces of structure can remove that packet:

1. Selberg's nonlinear symmetry formula;
2. the fact that the von Mangoldt measure lives on a sparse positive subset of the integer lattice with logarithmic jump sizes;
3. replication through arithmetic progressions.

The first two are shown to be boundary-compatible.

Let

$$
R(x)=\psi(x)-x.
$$

Selberg's symmetry formula may be written

$$
\boxed{
R(x)\log x
+
\sum_{n\le x}
\Lambda(n)R(x/n)
=
O(x).
}
$$

Insert a boundary power mode

$$
R_\rho(y)=y^\rho,
\qquad
\rho=\beta+i\gamma,
\qquad
\beta<1.
$$

Under the seed PNT estimate, partial summation gives

$$
\sum_{n\le x}
\Lambda(n)n^{-\rho}
=
\frac{x^{1-\rho}}{1-\rho}
+
O_\rho(x^{o(1)}).
$$

Hence the Selberg convolution of the boundary mode is

$$
\boxed{
\sum_{n\le x}
\Lambda(n)R_\rho(x/n)
=
\frac{x}{1-\rho}
+
O_\rho(x^{\beta+o(1)}).
}
$$

The boundary mode is therefore lifted to the natural $x$ -scale which the symmetry formula already permits in its $O(x)$ remainder. Selberg's identity can contract the order-one normalized PNT error, but this formula alone does not contract a fixed power exponent.

The paper then constructs an explicit integer-lattice pseudo-prime model.

Fix

$$
0<d<\frac12,
\qquad
\gamma\ne0,
$$

and sufficiently small fixed $\varepsilon>0$. Let

$$
\boxed{
F(x)
=
x
+
\varepsilon
x^{1-d}
\cos(\gamma\log x).
}
$$

For all sufficiently large $x$,

$$
F'(x)>0.
$$

There exists a subset

$$
\boxed{
\mathcal P^\star\subset\mathbb N
}
$$

such that its logarithmically weighted counting function

$$
\Theta^\star(x)
=
\sum_{\substack{n\le x\\n\in\mathcal P^\star}}
\log n
$$

satisfies

$$
\boxed{
\Theta^\star(x)
=
F(x)
+
O(\log x).
}
$$

The construction is a one-bit greedy quantizer with varying quantum $\log n$. Consequently,

$$
\boxed{
\pi^\star(x)
\sim
\frac{x}{\log x},
}
$$

yet

$$
\boxed{
\Theta^\star(x)-x
=
\varepsilon
x^{1-d}
\cos(\gamma\log x)
+
O(\log x).
}
$$

For every sublinear

$$
H=o(x),
$$

the short-interval error has the boundary scale

$$
\boxed{
\Theta^\star(x+H)-\Theta^\star(x)-H
=
\varepsilon Hx^{-d}
\left[
(1-d)\cos(\gamma\log x)
-
\gamma\sin(\gamma\log x)
\right]
+
o(Hx^{-d})
+
O(\log x).
}
$$

Thus all of the following properties are compatible with a persistent seed-boundary packet:

- exact support on the ordinary integer lattice;
- nonnegative coefficients;
- logarithmic jump size;
- prime-like density $x/\log x$ ;
- monotone weighted counting function;
- local jump bound $O(\log x)$.

The obstruction is therefore not caused by a lack of positivity, sparsity, jump discreteness, or integer spacing.

This conclusion complements recent Beurling-prime constructions. Broucke constructs positive generalized-prime systems whose zeta functions have zeros on prescribed contours and whose PNT errors nearly attain the corresponding zero-free-region scale. Earlier normalization results show that generalized-prime systems can be made arbitrarily close to the ordinary integer lattice and can agree with the rational primes up to any prescribed finite height while exhibiting different global zeta-zero geometry.

The two model classes isolate the remaining structure:

```text
integer-lattice pseudo-primes:
retain additive lattice + positivity + prime-like sparsity,
but not exact multiplicative primality.

Beurling primes:
retain Euler-product / prime multiplicativity + positivity,
but not the exact ordinary-integer additive lattice.

ordinary primes:
possess both simultaneously.
```

Hence a successful PT6 theorem must exploit their intersection, not either family of properties separately.

Finally, the arithmetic-progression replication route is audited. The Barban–Davenport–Halberstam variance satisfies the classical upper form

$$
V(x,Q)
\ll
xQ\log x
+
\frac{x^2}{\log^A x}.
$$

A global zeta error of size $x^{1-d}$ appears coherently in every principal character, giving only a lower contribution of order

$$
x^{2-2d}\log Q.
$$

For every fixed $d>0$,

$$
\frac{x^2}{\log^A x}
\gg
x^{2-2d}\log Q.
$$

Thus the standard BDH upper bound cannot use principal-character replication to improve the seed. Removing this obstruction would require fixed-power distribution information for nonprincipal Dirichlet characters, which is not supplied by a seed concerning the Riemann zeta function alone.

The remaining PT6 problem is therefore narrowed to a genuinely ordinary-prime interaction between additive lattice and multiplicative factorization at the critical low Mellin frequency.

No RH theorem is claimed.

---

# 1. Seed notation

Assume PESC $(\kappa)$ and set

$$
\boxed{
d=\frac{\kappa}{2}.
}
$$

The active zero boundary is

$$
\Re\rho\le1-d.
$$

The remaining direct frontier is the supercritical short-interval estimate

$$
|\psi(x+H)-\psi(x)-H|
\le
H x^{-d-\eta}
$$

outside a sufficiently small exceptional set.

Paper 63 showed that no longer-scale comparison controlled only by the seed can reach the exponent $d+\eta$.

We now test additional low-frequency structures.

---

# 2. Selberg symmetry formula in error form

The Selberg symmetry formula is

$$
\psi(x)\log x
+
\sum_{n\le x}
\Lambda(n)\psi(x/n)
=
2x\log x
+
O(x).
$$

Write

$$
\psi(x)=x+R(x).
$$

The main terms cancel to give

$$
\boxed{
R(x)\log x
+
\sum_{n\le x}
\Lambda(n)R(x/n)
=
O(x).
}
$$

This identity is exact up to the classical $O(x)$ symmetry remainder.

---

# 3. Boundary power mode under the Selberg operator

Fix

$$
\rho=\beta+i\gamma,
\qquad
0<\beta<1.
$$

Consider

$$
R_\rho(y)=y^\rho.
$$

Then

$$
\sum_{n\le x}
\Lambda(n)R_\rho(x/n)
=
x^\rho
\sum_{n\le x}
\frac{\Lambda(n)}{n^\rho}.
$$

Under any fixed PNT power bound stronger than $o(x)$, partial summation gives the main term

$$
\boxed{
\sum_{n\le x}
\frac{\Lambda(n)}{n^\rho}
=
\frac{x^{1-\rho}}{1-\rho}
+
O_\rho(x^{o(1)}).
}
$$

At the exponent-resolution level used here, the only relevant fact is that the main term is $x^{1-\rho}$.

Thus:

## Theorem 3.1 — Selberg boundary-mode lifting

$$
\boxed{
\sum_{n\le x}
\Lambda(n)R_\rho(x/n)
=
\frac{x}{1-\rho}
+
O_\rho(x^{\beta+o(1)}).
}
$$

The first term of the symmetry formula is only

$$
R_\rho(x)\log x
=
x^\rho\log x.
$$

Therefore the boundary mode is not forced to shrink. The convolution maps it to the $x$ scale already admitted by the symmetry remainder.

Create:

```text
O-RH-148
SELBERG_SYMMETRY_LIFTS_FIXED_POWER_BOUNDARY_MODE_TO_ALLOWED_X_SCALE
CERTIFIED_AS_METHOD_BARRIER
```

---

# 4. Interpretation of the Selberg elementary contraction

Selberg's elementary PNT argument can improve a bound of the form

$$
|R(x)|\le ax
$$

to a smaller normalized constant at sufficiently large scales, and iteration drives

$$
R(x)/x\to0.
$$

This does not imply a power-exponent contraction.

The boundary-mode calculation explains why.

A fixed exponent

$$
R(x)\asymp x^\beta
$$

with $\beta<1$ feeds the symmetry convolution at order $x$, where the formula has no power margin.

Thus the classical Selberg contraction acts on the coefficient of the $x$ scale, not on the rightmost Mellin singularity.

A fixed-power improvement would require a refined symmetry theorem whose residual is itself below the boundary-mode lift or another cancellation mechanism not present in the standard formula.

No such theorem is certified.

---

# 5. Positive sparse integer-lattice boundary model

We now show that several remaining "prime-like" local properties are insufficient.

Fix

$$
0<d<\frac12,
\qquad
\gamma\ne0.
$$

Choose sufficiently small

$$
0<\varepsilon<1.
$$

Define

$$
\boxed{
F(x)
=
x
+
\varepsilon
x^{1-d}
\cos(\gamma\log x).
}
$$

Differentiate:

$$
F'(x)
=
1
+
\varepsilon x^{-d}
\left[
(1-d)\cos(\gamma\log x)
-
\gamma\sin(\gamma\log x)
\right].
$$

Since the perturbation tends to zero,

$$
\boxed{
F'(x)>0
}
$$

for all sufficiently large $x$.

Also,

$$
F(n)-F(n-1)=1+O(n^{-d}).
$$

Hence for all sufficiently large $n$,

$$
\boxed{
\frac12
\le
F(n)-F(n-1)
\le
\frac32.
}
$$

---

# 6. Greedy logarithmic quantization lemma

Let

$$
q_n=\log n.
$$

We construct

$$
b_n\in\{0,q_n\}
$$

so that

$$
S_N=\sum_{n_0\le n\le N}b_n
$$

tracks

$$
F(N)-F(n_0-1).
$$

Let

$$
e_N
=
S_N
-
\left(
F(N)-F(n_0-1)
\right).
$$

Inductively choose

$$
b_n=
\begin{cases}
0,
&
e_{n-1}-\Delta F_n
\ge
-q_n/2,
\\
q_n,
&
e_{n-1}-\Delta F_n
<
-q_n/2,
\end{cases}
$$

where

$$
\Delta F_n=F(n)-F(n-1).
$$

For sufficiently large $n_0$, the slow variation of $q_n$ and the bound

$$
1/2\le\Delta F_n\le3/2
$$

give

$$
\boxed{
|e_N|
\le
\frac12\log N
+
O(1).
}
$$

Thus:

## Theorem 6.1 — Sparse logarithmic-jump tracking

There exists a set

$$
\mathcal P^\star
=
\{n:b_n=\log n\}
$$

such that

$$
\boxed{
\Theta^\star(N)
:=
\sum_{\substack{n\le N\\n\in\mathcal P^\star}}
\log n
=
F(N)
+
O(\log N).
}
$$

Create:

```text
B-RH-081
POSITIVE_INTEGER_LATTICE_LOG_JUMP_SEQUENCE_CAN_TRACK_A_BOUNDARY_HARMONIC
CERTIFIED_MODEL
```

---

# 7. Prime-like density of the pseudo-prime support

Theorem 6.1 gives

$$
\Theta^\star(x)
=
x+o(x).
$$

Since every selected integer carries weight $\log n$, standard partial summation gives

$$
\boxed{
\pi^\star(x)
:=
\#\{n\le x:n\in\mathcal P^\star\}
\sim
\frac{x}{\log x}.
}
$$

Thus the support has the same first-order density as the primes.

It is not asserted to consist of actual primes.

That distinction is precisely the point of the model.

---

# 8. Boundary short-interval oscillation of the pseudo-primes

Let

$$
H=o(x).
$$

Taylor expansion gives

$$
F(x+H)-F(x)-H
=
H(F'(x)-1)
+
O
\left(
H^2x^{-1-d}
\right).
$$

Therefore

$$
\boxed{
F(x+H)-F(x)-H
=
\varepsilon
Hx^{-d}
\left[
(1-d)\cos(\gamma\log x)
-
\gamma\sin(\gamma\log x)
\right]
+
O
\left(
H^2x^{-1-d}
\right).
}
$$

Using

$$
\Theta^\star(y)=F(y)+O(\log y),
$$

we obtain

$$
\boxed{
\Theta^\star(x+H)-\Theta^\star(x)-H
=
\varepsilon
Hx^{-d}
\left[
(1-d)\cos(\gamma\log x)
-
\gamma\sin(\gamma\log x)
\right]
+
O
\left(
H^2x^{-1-d}
+
\log x
\right).
}
$$

For every fixed polynomial interval exponent with

$$
H=x^\alpha
$$

and

$$
\alpha>d,
$$

the $O(\log x)$ quantization error is negligible relative to the boundary scale.

Hence the pseudo-prime system exhibits exactly the PT6 critical short-interval amplitude.

---

# 9. What the pseudo-prime model preserves

The construction has:

```text
support:
a subset of the ordinary positive integers.

weights:
0 or log n.

positivity:
all weights nonnegative.

weighted monotonicity:
Theta*(x) is nondecreasing.

jump cap:
each jump is O(log x).

density:
pi*(x) ~ x/log x.

global PNT:
Theta*(x) ~ x.

boundary harmonic:
Theta*(x)-x has x^(1-d) log-periodic oscillation.

short intervals:
relative boundary amplitude x^-d.
```

Thus none of these properties individually or jointly excludes the critical packet.

The model deliberately does not impose exact primality or the Euler-product factorization law of the rational primes.

---

# 10. Beurling-prime complementary model

Recent work of Broucke constructs Beurling zeta functions with:

- positive generalized primes;
- zeta functions with infinitely many zeros on a prescribed contour;
- no zeros to the right of that contour;
- PNT error oscillations close to the scale predicted by the contour.

This shows that generalized Euler-product positivity and prime multiplicativity also do not create a self-improving fixed zero-free strip.

Earlier normalization work goes further in a different direction: generalized prime systems may be chosen to agree with the rational primes up to any prescribed finite height and may be placed arbitrarily close to the ordinary integer lattice while exhibiting globally different zero geometry.

These results are external model calibration.

They do not constitute counterexamples for the ordinary primes.

---

# 11. Two-model separation principle

The pseudo-prime model and the Beurling model preserve complementary structures.

## Integer-lattice pseudo-prime model

Preserves:

- ordinary integer lattice;
- positivity;
- sparse logarithmic jumps;
- prime-like density.

Does not preserve:

- exact ordinary-prime multiplicative factorization.

## Beurling-prime model

Preserves:

- positive prime objects;
- generalized Euler product;
- multiplicative prime-generated semigroup;
- prescribed global zero geometry.

Does not preserve:

- exact ordinary-integer additive lattice / unique ordinary factorization.

Therefore:

## Principle 11.1 — Ordinary-arithmetic residual

Any PT6 mechanism based only on one of the following packages is insufficiently specific:

```text
integer lattice + positivity + prime-like sparsity,

or

Euler product + positive generalized prime multiplicativity.
```

A successful theorem must use a property of the ordinary primes arising from the simultaneous compatibility of the ordinary additive lattice with exact integer factorization.

Create:

```text
O-RH-149
LOW_FREQUENCY_BOUNDARY_PACKET_COMPATIBLE_WITH_COMPLEMENTARY_INTEGER_AND_BEURLING_PRIME_MODELS
CERTIFIED_AS_METHOD_CALIBRATION
```

---

# 12. Arithmetic-progression replication idea

A zeta zero also appears in the principal Dirichlet character modulo every $q$.

This suggests amplifying a boundary zero by summing prime-distribution variance over moduli.

Let

$$
V(x,Q)
=
\sum_{q\le Q}
\sum_{(a,q)=1}
\left|
\psi(x;q,a)
-
\frac{x}{\phi(q)}
\right|^2.
$$

For each $q$, Cauchy over reduced residue classes gives a principal-component lower bound of order

$$
\frac{|A(x)|^2}{\phi(q)}
$$

up to the finitely many primes dividing $q$.

Thus a boundary-sized global error would contribute heuristically and, after standard local corrections, at scale

$$
\boxed{
|A(x)|^2
\sum_{q\le Q}
\frac1{\phi(q)}
\asymp
x^{2-2d}\log Q.
}
$$

This is a genuine replication of the principal zeta error across moduli.

---

# 13. Classical BDH upper bound is too coarse at fixed-power scale

The Barban–Davenport–Halberstam upper bound has the classical form

$$
\boxed{
V(x,Q)
\ll_A
xQ\log x
+
\frac{x^2}{\log^A x}.
}
$$

The second term arises from the available small-modulus distribution / Siegel-Walfisz input in the standard theorem.

For every fixed

$$
d>0
$$

and fixed $A$,

$$
\boxed{
\frac{x^2}{\log^A x}
\gg
x^{2-2d}\log Q.
}
$$

Therefore the classical BDH theorem cannot contradict a seed-boundary principal contribution.

Create:

```text
O-RH-150
CLASSICAL_BDH_LOGARITHMIC_SMALL_MODULUS_ERROR_MASKS_FIXED_POWER_PRINCIPAL_ZETA_REPLICATION
CERTIFIED_AS_METHOD_BARRIER
```

---

# 14. Why the zeta seed does not automatically improve the BDH remainder

The zeta seed controls only the principal $L$ -function:

$$
\zeta(s).
$$

The BDH variance contains all Dirichlet characters modulo $q$.

Improving the small-modulus remainder from

$$
x^2\log^{-A}x
$$

to a fixed-power error would require correspondingly stronger information on nonprincipal Dirichlet $L$ -functions or an alternative arithmetic argument which avoids them.

PESC $(\kappa)$ for the Riemann zeta function alone gives no such family-wide zero-free strip.

Thus the arithmetic-progression replication idea does use ordinary congruence structure, but it immediately opens a new family of $L$ -function boundary problems rather than closing the original one.

This route is retained only as a high-cost possibility.

---

# 15. Selberg symmetry and generalized-prime calibration together

The low-frequency audit now has three levels.

```text
Selberg symmetry:
uses exact ordinary divisor convolution,
but boundary mode is lifted into the allowed O(x) scale.

integer pseudo-prime model:
uses exact additive lattice and prime-like positive jumps,
but boundary harmonic survives.

Beurling model:
uses positive Euler-product multiplicativity,
but prescribed boundary zeros survive.
```

No one of these structures supplies the missing fixed exponent.

Thus PT6 cannot be solved merely by adding one more standard structural identity.

---

# 16. Updated PT6 target

The remaining problem should be stated as a genuinely joint ordinary-arithmetic theorem.

A useful but deliberately non-equivalent research target is:

```text
PT6E
ORDINARY-INTEGER FACTORIZATION / ADDITIVE-LATTICE LOW-FREQUENCY EXCESS
```

Desired output:

a fixed-power suppression of the actual von Mangoldt low-frequency boundary packet which fails for:

- arbitrary sparse positive integer-supported pseudo-prime sequences; and
- generic positive Beurling prime systems.

Candidate sources of such an excess include:

- quantitative interaction of unique factorization with additive short intervals;
- sign-sensitive Möbius–prime correlations beyond the current Type-II variance theory;
- congruence replication with fixed-power family control;
- a genuinely new nonlinear parity-breaking estimate.

No theorem is claimed.

---

# 17. External calibration

## 17.1. Selberg symmetry formula

The classical formula is

$$
\psi(x)\log x
+
\sum_{n\le x}
\Lambda(n)\psi(x/n)
=
2x\log x+O(x).
$$

Modern lecture notes and formalized proofs record the equivalent error form used here.

## 17.2. Beurling prescribed contours

F. Broucke,
*On the connection between zero-free regions and the error term in the prime number theorem*,
Analysis Mathematica, published August 2026.

Broucke constructs Beurling zeta functions with infinitely many zeros on prescribed contours and proves associated PNT-error oscillation results showing near-sharpness.

URL:

https://link.springer.com/article/10.1007/s10476-026-00176-y

## 17.3. Near-integer generalized-prime normalization

W.-B. Zhang,
*Normalization of Beurling generalized primes with Riemann Hypothesis*,
Annales Univ. Sci. Budapest. Sect. Comput. 39 (2013), 459–469.

The constructions can agree with the ordinary primes up to an arbitrarily prescribed finite height while realizing different global zeta behavior.

## 17.4. Barban–Davenport–Halberstam

The classical Gallagher form is

$$
V(x,Q)
\ll
xQ\log x
+
x^2\log^{-A}x.
$$

Modern surveys emphasize that the logarithmic second error term prevents a genuine asymptotic for power-smaller $Q$ without stronger small-modulus information.

---

# 18. State transition

Advance the candidate state from

$$
v1.54
$$

to

$$
v1.55.
$$

Add:

```text
O-RH-148
SELBERG_SYMMETRY_LIFTS_FIXED_POWER_BOUNDARY_MODE_TO_ALLOWED_X_SCALE
CERTIFIED_AS_METHOD_BARRIER
```

Add:

```text
B-RH-081
POSITIVE_INTEGER_LATTICE_LOG_JUMP_SEQUENCE_CAN_TRACK_A_BOUNDARY_HARMONIC
CERTIFIED_MODEL
```

Add:

```text
O-RH-149
LOW_FREQUENCY_BOUNDARY_PACKET_COMPATIBLE_WITH_COMPLEMENTARY_INTEGER_AND_BEURLING_PRIME_MODELS
CERTIFIED_AS_METHOD_CALIBRATION
```

Add:

```text
O-RH-150
CLASSICAL_BDH_LOGARITHMIC_SMALL_MODULUS_ERROR_MASKS_FIXED_POWER_PRINCIPAL_ZETA_REPLICATION
CERTIFIED_AS_METHOD_BARRIER
```

Open:

```text
PT6E
ORDINARY_INTEGER_FACTORIZATION_ADDITIVE_LATTICE_LOW_FREQUENCY_EXCESS
```

No RH certificate is created.

---

# 19. Conclusion

The critical low-frequency packet survives every standard structural property tested so far.

Selberg symmetry does not contract its exponent.

Positive sparse logarithmic jumps on the exact integer lattice do not contract it.

Positive generalized Euler-product primes do not contract it.

Classical congruence averaging cannot see it at fixed-power precision because the small-modulus BDH remainder is only logarithmically small.

Therefore the remaining CSM_RH gap is more specific than "use prime arithmetic."

It is:

$$
\boxed{
\text{exploit a quantitative property unique to ordinary integer factorization}
\ \cap\
\text{ordinary additive lattice}
}
$$

strong enough to suppress the boundary packet by a fixed new power.

That is PT6E.
