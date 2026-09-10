# CSM_RH Paper 75

## Shift-Averaged Prime Sequences, Deterministic Power-Level Local Distribution, and the First Boundary-Breaking Bilinear Axiom

**Project:** CSM_RH  
**Paper:** 75  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 47 — `ORDINARY_PRIME_BOUNDARY_BREAKING`  
**Status:** CAMPAIGN 47 OPENED / FIRST EXPLICIT q=1 PARITY-BREAKING INEQUALITY DEFINED / LOCAL SIEVE DISTRIBUTION POWER-SOLVED / POWER-OUTPUT EXTRACTION STILL OPEN  
**Canonical entry state:** v1.65 / Paper 74 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Campaign 46 closed at an RH-equivalent arithmetic wall. Campaign 47 therefore begins under a new entry rule:

> No new representation is developed unless an explicit ordinary-prime $q=1$ fixed-power inequality is stated first.

The present paper supplies the first such inequality.

Let

$$
\omega_H(r)
=
\left(
1-\frac{|r|}{H}
\right)_+
$$

and fix a nonnegative smooth weight

$$
W\in C_c^\infty(1,2).
$$

Define the shift-averaged prime sequence

$$
\boxed{
a_{N,H}(n)
=
W(n/N)
\sum_{r\in\mathbb Z}
\omega_H(r)\Lambda(n+r).
}
$$

This is a nonnegative sequence on the ordinary integer lattice.

Its total mass is

$$
\boxed{
A(N,H)
:=
\sum_n a_{N,H}(n)
=
NH
\left(
\int_1^2W(u)\,du
\right)
(1+o(1)).
}
$$

The crucial structural fact is that its local divisibility distribution is essentially deterministic.

For

$$
A_d(N,H)
=
\sum_{d\mid n}
a_{N,H}(n),
$$

one has uniformly in $d$,

$$
\boxed{
A_d(N,H)
=
\frac{A(N,H)}{d}
+
O_W(N).
}
$$

The proof does not use Bombieri–Vinogradov or primes in progressions.

After the change of variables

$$
m=n+r,
$$

the divisibility condition samples a bounded-variation triangular kernel on the lattice $d\mathbb Z$. Euler summation gives an $O_W(1)$ discrepancy for each prime-power variable $m$, and

$$
\sum_{m\asymp N}\Lambda(m)\ll N.
$$

Consequently,

$$
\boxed{
\sum_{d\le D}
\mu^2(d)\tau_5(d)
\left|
A_d-\frac Ad
\right|
\ll_W
ND(\log N)^{O(1)}.
}
$$

Relative to

$$
A\asymp NH,
$$

the sieve remainder ratio is

$$
\boxed{
\frac{D}{H}N^{o(1)}.
}
$$

Thus, with

$$
H=N^{1-\tau}
$$

and

$$
D=N^{2/3+\varepsilon},
$$

one obtains the genuine fixed-power remainder

$$
\boxed{
\sum_{d\le D}
\mu^2(d)\tau_5(d)
\left|
A_d-\frac Ad
\right|
\ll
A
N^{-\eta_R+o(1)},
}
$$

where

$$
\boxed{
\eta_R
=
\frac13-\tau-\varepsilon.
}
$$

This is positive whenever

$$
\tau<\frac13-\varepsilon.
$$

Therefore the classical high-level local-distribution obstruction in a twin-prime asymptotic sieve disappears after triangular shift averaging.

The surviving parity problem is exactly a bilinear Möbius problem.

For

$$
\gamma(n,C)
=
\sum_{\substack{d\mid n\\d\le C}}
\mu(d),
$$

define the shift-averaged asymptotic-sieve bilinear form

$$
\boxed{
\mathfrak B_{N,H}(L,C)
=
\sum_m
\left|
\sum_{\substack{L<n\le2L\\mn\asymp N}}
\gamma(n,C)
\mu(mn)
a_{N,H}(mn)
\right|.
}
$$

The first Campaign-47 arithmetic candidate is:

```text
F-RH-023
SHIFT-AVERAGED BOUNDARY-BREAKING BILINEAR POWER AXIOM
```

There should exist a fixed

$$
\eta_B>0
$$

such that

$$
\boxed{
\mathfrak B_{N,H}(L,C)
\ll
A(N,H)
N^{-\eta_B}
}
$$

uniformly in the parity-breaking asymptotic-sieve window

$$
\boxed{
\Delta^{-1}\sqrt D
<
L
<
\delta^{-1}\sqrt N,
}
$$

and

$$
1\le C\le ND^{-1},
$$

for appropriate slowly separated $\delta,\Delta$ or for a power-output variant of this range.

This is the exact Friedlander–Iwaniec bilinear axiom with the logarithmic right side replaced by a fixed power and with the special sequence $a_{N,H}$ inserted.

The source of cancellation is the sign of

$$
\mu(mn),
$$

not local congruence equidistribution.

This is precisely the parity-breaking feature missing from classical sieve theory.

The candidate passes the Campaign-47 discrimination tests:

1. **Local sieve information alone is insufficient.** Friedlander and Iwaniec's Selberg parity model
   $$
   a_n=\frac12(1+\lambda(n))
   $$
   satisfies the ordinary remainder hypothesis to very high level but fails the bilinear axiom.

2. **Integer-lattice pseudo-prime models are not protected.** The properties preserved by Paper 64—positive logarithmic jumps, prime-like density, integer support, monotonicity—do not imply Möbius bilinear cancellation. F-RH-023 adds exactly the missing parity-sensitive ordinary-factorization information.

3. **Beurling-prime models do not possess the same invariant.** F-RH-023 uses the simultaneous ordinary identities
   $$
   mn\in\mathbb N,
   \qquad
   \mu(mn),
   \qquad
   mn+r.
   $$
   These are not intrinsic to a generic Beurling prime semigroup.

Thus F-RH-023 genuinely uses the intersection

$$
\boxed{
\text{ordinary additive lattice}
\cap
\text{ordinary integer factorization}.
}
$$

However, the paper also identifies an important extraction barrier.

The published Friedlander–Iwaniec asymptotic-sieve theorem concludes

$$
\sum_p a_p\log p
=
\mathcal H A
\left[
1+
O\left(
\frac{\log\delta}{\log\Delta}
\right)
\right].
$$

Even if the remainder axiom and bilinear axiom were strengthened to fixed powers, this generic extraction has only logarithmic relative accuracy. In their theorem this loss is explicit and cannot be improved merely by refining the same general argument.

For the present sequence,

$$
g(d)=\frac1d,
$$

so the sieve constant is

$$
\boxed{
\mathcal H=1.
}
$$

A fixed-power output

$$
\sum_n
a_{N,H}(n)\Lambda(n)
=
A(N,H)
+
O
\left(
A(N,H)N^{-\eta_S}
\right)
$$

would immediately feed the root pair residual, because

$$
\sum_n
a_{N,H}(n)\Lambda(n)
=
\sum_r
\omega_H(r)
\sum_n
W(n/N)\Lambda(n)\Lambda(n+r),
$$

while the weighted singular-series average differs from $H$ only by $O(\log H)$.

But the **published** asymptotic sieve does not preserve a fixed power into its final prime-detection output.

Campaign 47 therefore separates two tasks:

```text
C47-A
prove F-RH-023, a genuine fixed-power parity-breaking bilinear estimate;

C47-B
derive a power-output prime-detection identity for the dense shift-averaged sequence,
most likely by a direct Vaughan / asymptotic-identity decomposition rather than the generic logarithmic sieve extraction.
```

The local distribution side is already power-solved.

There is also a quantitative ceiling.

Since the Friedlander–Iwaniec parity-breaking mechanism requires

$$
D>N^{2/3+\varepsilon},
$$

the deterministic remainder exponent satisfies at best

$$
\boxed{
\eta_R
<
\frac13-\tau.
}
$$

Hence this first Campaign-47 mechanism can only directly beat a seed exponent $\kappa$ when

$$
\boxed{
\kappa
<
\frac13-\tau.
}
$$

It is therefore a bootstrap candidate, not a one-step RH theorem.

No RH theorem is claimed.

---

# 1. Campaign-47 entry rule

Campaign 46 established that another representation change without a new arithmetic inequality is not justified.

Campaign 47 adopts:

```text
ENTRY RULE

Before a new framework is opened,
state a concrete q=1 fixed-power arithmetic inequality.

The inequality must use a property
which fails to follow from the pseudo-prime
and Beurling-prime model classes.
```

F-RH-023 is the first candidate satisfying this rule.

---

# 2. Triangular shift kernel

Define

$$
\boxed{
\omega_H(r)
=
\max
\left(
1-\frac{|r|}{H},
0
\right).
}
$$

Then

$$
0\le\omega_H(r)\le1,
$$

$$
\operatorname{supp}\omega_H
\subset[-H,H],
$$

and

$$
\boxed{
\sum_{r\in\mathbb Z}
\omega_H(r)
=
H+O(1).
}
$$

Its total variation is bounded absolutely.

---

# 3. Shift-averaged prime sequence

Fix

$$
W\in C_c^\infty(1,2),
\qquad
W\ge0,
\qquad
W\not\equiv0.
$$

Define

$$
\boxed{
a_{N,H}(n)
=
W(n/N)
\sum_r
\omega_H(r)
\Lambda(n+r).
}
$$

The sequence is nonnegative.

It is not a prime indicator.

It is a dense prime-shift convolution designed so that applying an outer von Mangoldt weight detects prime pairs only **after** the shift averaging has regularized the local congruence geometry.

---

# 4. Total mass

Swap

$$
m=n+r.
$$

Then

$$
A(N,H)
=
\sum_m
\Lambda(m)
\sum_n
W(n/N)
\omega_H(m-n).
$$

Because $H=o(N)$ and $W$ is smooth,

$$
\sum_n
W(n/N)
\omega_H(m-n)
=
H
W(m/N)
+
O_W
\left(
1+\frac{H^2}{N}
\right)
$$

uniformly away from the harmless support endpoints.

Weighted PNT therefore gives:

## Theorem 4.1 — Total shift-averaged mass

$$
\boxed{
A(N,H)
=
NH
\left(
\int_1^2W(u)du
\right)
(1+o(1)).
}
$$

At exponent resolution,

$$
\boxed{
A(N,H)\asymp_W NH.
}
$$

---

# 5. Deterministic lattice-sampling lemma

For a fixed prime-power variable $m$, define

$$
f_m(x)
=
W(x/N)
\omega_H(m-x).
$$

The function $f_m$ is compactly supported and has

$$
\boxed{
\|f_m\|_\infty
+
\operatorname{Var}(f_m)
\ll_W1.
}
$$

For every integer $d\ge1$, elementary Euler summation for bounded-variation functions gives

$$
\boxed{
\sum_{k\in\mathbb Z}
f_m(dk)
=
\frac1d
\int_{\mathbb R}
f_m(x)dx
+
O_W(1).
}
$$

Likewise,

$$
\sum_{n\in\mathbb Z}
f_m(n)
=
\int_{\mathbb R}
f_m(x)dx
+
O_W(1).
$$

Subtracting:

## Lemma 5.1 — Lattice divisibility discrepancy

$$
\boxed{
\sum_{d\mid n}
W(n/N)
\omega_H(m-n)
-
\frac1d
\sum_n
W(n/N)
\omega_H(m-n)
=
O_W(1).
}
$$

This contains no prime-distribution theorem.

---

# 6. Power-level local divisibility

Define

$$
\boxed{
A_d(N,H)
=
\sum_{d\mid n}
a_{N,H}(n).
}
$$

Using Lemma 5.1 and summing against $\Lambda(m)$,

$$
\begin{aligned}
A_d-\frac Ad
&=
\sum_m
\Lambda(m)
O_W(1).
\end{aligned}
$$

Only

$$
m\asymp N
$$

within an $O(H)$ enlargement occurs.

Chebyshev's bound gives

$$
\sum_{m\asymp N}\Lambda(m)\ll N.
$$

Therefore:

## Theorem 6.1 — Deterministic local distribution

$$
\boxed{
A_d(N,H)
=
\frac{A(N,H)}{d}
+
O_W(N)
}
$$

uniformly for every $d\ge1$.

Create:

```text
B-RH-115
SHIFT_AVERAGING_CONVERTS_PRIME_LOCAL_DIVISIBILITY_TO_DETERMINISTIC_LATTICE_DISTRIBUTION
CERTIFIED
```

---

# 7. High sieve level is automatically power-good

Let

$$
r_d
=
A_d-\frac Ad.
$$

Theorem 6.1 gives

$$
|r_d|
\ll_WN.
$$

The standard divisor mean value gives

$$
\sum_{d\le D}\mu^2(d)\tau_5(d)
\ll
D(\log D)^{O(1)}.
$$

Hence:

## Theorem 7.1 — Power remainder axiom

$$
\boxed{
\sum_{d\le D}
\mu^2(d)\tau_5(d)
|r_d|
\ll_W
ND(\log N)^{O(1)}.
}
$$

Since

$$
A\asymp NH,
$$

$$
\boxed{
\frac{
\sum_{d\le D}\mu^2(d)\tau_5(d)|r_d|
}{
A
}
\ll
\frac DH
N^{o(1)}.
}
$$

Create:

```text
B-RH-116
SHIFT_AVERAGED_SEQUENCE_HAS_POWER_LEVEL_ASYMPTOTIC_SIEVE_REMAINDER_TO_ANY_D_BELOW_H_BY_A_POWER
CERTIFIED
```

---

# 8. Compatibility with the parity-breaking distribution threshold

Friedlander and Iwaniec's asymptotic sieve requires

$$
\boxed{
D>N^{2/3}
}
$$

and explains that the bilinear parity axiom is realistic only once the level is somewhat beyond $N^{2/3+\varepsilon}$.

Choose

$$
\boxed{
D=N^{2/3+\varepsilon}.
}
$$

Let

$$
H=N^{1-\tau}.
$$

Then

$$
\frac DH
=
N^{-(1/3-\tau-\varepsilon)}.
$$

Therefore:

## Corollary 8.1 — Automatic fixed-power local remainder

If

$$
\tau<\frac13-\varepsilon,
$$

then

$$
\boxed{
\sum_{d\le D}
\mu^2(d)\tau_5(d)|r_d|
\ll
A
N^{-\eta_R+o(1)}
}
$$

with

$$
\boxed{
\eta_R
=
\frac13-\tau-\varepsilon.
}
$$

The local distribution hurdle is no longer the twin-prime obstruction for this shift-averaged sequence.

---

# 9. The Friedlander–Iwaniec bilinear coefficient

Define

$$
\boxed{
\gamma(n,C)
=
\sum_{\substack{d\mid n\\d\le C}}
\mu(d).
}
$$

Friedlander and Iwaniec introduce this coefficient in their parity-breaking axiom.

Their bilinear form has inner sign oscillation

$$
\mu(mn).
$$

They explicitly identify this Möbius sign change as the cancellation mechanism which breaks the sieve parity obstruction.

---

# 10. First Campaign-47 inequality

Define

$$
\boxed{
\mathfrak B_{N,H}(L,C)
=
\sum_m
\left|
\sum_{\substack{L<n\le2L\\mn\in\operatorname{supp}W_N}}
\gamma(n,C)
\mu(mn)
a_{N,H}(mn)
\right|.
}
$$

Here

$$
W_N(x)=W(x/N).
$$

Open:

```text
F-RH-023
SHIFT_AVERAGED_BOUNDARY_BREAKING_BILINEAR_POWER_AXIOM
```

Candidate statement:

there exists a fixed

$$
\boxed{
\eta_B>0
}
$$

such that

$$
\boxed{
\mathfrak B_{N,H}(L,C)
\ll
A(N,H)
N^{-\eta_B}
}
$$

uniformly in the parity-sensitive balanced range

$$
\boxed{
\Delta^{-1}\sqrt D
<
L
<
\delta^{-1}\sqrt N,
}
$$

and

$$
\boxed{
1\le C\le ND^{-1}.
}
$$

This is the first explicit new arithmetic inequality of Campaign 47.

---

# 11. Why F-RH-023 is genuinely parity-sensitive

Friedlander and Iwaniec exhibit Selberg's sequence

$$
\boxed{
a_n^{\rm parity}
=
\frac12(1+\lambda(n)),
}
$$

the indicator of integers with an even number of prime factors.

This sequence can satisfy the standard local remainder hypothesis with a level as high as

$$
N^{1-\varepsilon},
$$

yet contains no primes.

It fails the bilinear axiom.

Thus:

## Calibration 11.1

High local divisibility level does not imply F-RH-023.

The new inequality tests global multiplicative parity information.

This is exactly what Campaign 47 requires.

---

# 12. Pseudo-prime and Beurling discrimination

Paper 64 constructed positive, sparse, integer-supported pseudo-prime sequences with:

- logarithmic jumps;
- density $N/\log N$ ;
- monotone weighted count;
- a persistent boundary harmonic.

Those properties alone do not impose any estimate resembling

$$
\mathfrak B_{N,H}\ll AN^{-\eta_B}.
$$

F-RH-023 inserts the ordinary Möbius factor

$$
\mu(mn)
$$

on actual integer factorizations.

Thus the pseudo-prime model does not automatically satisfy the new axiom.

For Beurling systems the separation is stronger.

The expression

$$
\boxed{
\mu(mn)\,
\Lambda(mn+r)
}
$$

simultaneously requires:

- the ordinary product $mn$ ;
- the ordinary Möbius function;
- the additive ordinary shift $mn+r$.

A generic Beurling prime system has no invariant operation corresponding to this triple structure.

Thus F-RH-023 passes the two-model discrimination test.

---

# 13. Relation to the weighted prime-pair aggregate

The outer prime-detection sum for the sequence $a_{N,H}$ is

$$
\boxed{
\mathcal P(N,H)
=
\sum_n
a_{N,H}(n)
\Lambda(n).
}
$$

Expanding,

$$
\boxed{
\mathcal P(N,H)
=
\sum_r
\omega_H(r)
\sum_n
W(n/N)
\Lambda(n)
\Lambda(n+r).
}
$$

Therefore a power-accurate prime-detection theorem

$$
\boxed{
\mathcal P(N,H)
=
A(N,H)
+
O
\left(
A(N,H)
N^{-\eta_S}
\right)
}
$$

would give a power-accurate weighted prime-pair aggregate.

The local Hardy–Littlewood prediction satisfies

$$
\sum_r
\omega_H(r)\mathfrak S(r)
=
H+O(\log H)
$$

by the Montgomery–Soundararajan singular-series average.

Hence the difference between $A(N,H)$ and the full local singular-series main term is only

$$
O_W(N\log H)
+
o(NH).
$$

Relative to $A\asymp NH$, this has fixed-power exponent

$$
1-\tau
$$

up to logarithms.

Thus any prime-detection exponent

$$
\eta_S>\kappa
$$

in the amplifier range

$$
\tau<1-\kappa
$$

would activate F-RH-022.

---

# 14. The published asymptotic-sieve extraction floor

Friedlander and Iwaniec prove, under their standard hypotheses,

$$
\boxed{
\sum_p
a_p\log p
=
\mathcal H A
\left[
1+
O
\left(
\frac{\log\delta}{\log\Delta}
\right)
\right].
}
$$

For the density

$$
g(d)=\frac1d,
$$

$$
\boxed{
\mathcal H
=
\prod_p
(1-g(p))
\left(
1-\frac1p
\right)^{-1}
=
1.
}
$$

However,

$$
\frac{\log\delta}{\log\Delta}
$$

cannot be made into

$$
N^{-\eta}
$$

inside the published generic framework.

Even taking $\delta$ fixed and $\Delta$ a power of $N$ leaves only

$$
O(1/\log N).
$$

Friedlander and Iwaniec explicitly note that this loss cannot be removed merely by refining their general argument.

Therefore:

## Obstruction 14.1 — Generic asymptotic-sieve extraction floor

A fixed-power F-RH-023 input does **not**, by itself, produce a fixed-power prime-pair output through the published 1998 theorem.

Create:

```text
O-RH-169
PUBLISHED_ASYMPTOTIC_SIEVE_HAS_A_LOGARITHMIC_PRIME_DETECTION_EXTRACTION_FLOOR
CERTIFIED
```

---

# 15. Campaign-47 split

Campaign 47 therefore has two sharply separated tasks.

## C47-A — Arithmetic bilinear input

Prove

$$
\boxed{
\mathfrak B_{N,H}(L,C)
\ll
A(N,H)N^{-\eta_B}.
}
$$

This is F-RH-023.

## C47-B — Power-output extraction

Develop a direct prime-detection identity for the dense shift-averaged sequence which converts:

- the already certified power local remainder; and
- the F-RH-023 power bilinear estimate

into

$$
\boxed{
\mathcal P(N,H)
=
A(N,H)
+
O
\left(
A(N,H)N^{-\eta_S}
\right).
}
$$

The natural candidates are direct Vaughan / Heath–Brown / Opera-de-Cribro asymptotic identities rather than the generic logarithmic sieve theorem.

No C47-B theorem is yet certified.

---

# 16. Exponent budget

Take

$$
D=N^{2/3+\varepsilon}
$$

and

$$
H=N^{1-\tau}.
$$

The local remainder exponent is

$$
\boxed{
\eta_R
=
\frac13-\tau-\varepsilon.
}
$$

Therefore any power-output extraction based on this level can only produce a root excess beyond a PESC seed if at least

$$
\boxed{
\kappa
<
\frac13-\tau.
}
$$

In addition, the bilinear exponent must survive the extraction above $\kappa$.

Thus the first Campaign-47 mechanism is a bootstrap candidate in the region

$$
\boxed{
0<\kappa<\frac13.
}
$$

It is not an endpoint mechanism.

---

# 17. Why this is a genuine new campaign direction

Campaign 46 repeatedly encountered representations whose hardest component recombined to the original prime error without isolating a new arithmetic inequality.

Paper 75 is different.

Before any new extraction machinery is developed, the missing inequality has already been written explicitly:

$$
\boxed{
\mathfrak B_{N,H}(L,C)
\ll
A(N,H)N^{-\eta_B}.
}
$$

Its content is:

```text
fixed-power Möbius parity cancellation
inside an ordinary shift-averaged prime sequence
at balanced multiplicative scales.
```

This statement is not implied by:

- PESC;
- local sieve distribution;
- high-conductor averaging;
- positive prime density;
- pseudo-prime integer support;
- generalized Euler-product positivity.

It is an actual new arithmetic input.

---

# 18. External calibration

## 18.1. Friedlander–Iwaniec asymptotic sieve

J. Friedlander and H. Iwaniec,
*Asymptotic sieve for primes*,
Annals of Mathematics 148 (1998), 1041–1065.

Their axiom (B) is

$$
\sum_m
\left|
\sum_{\substack{L<n\le2L\\mn\le x}}
\gamma(n,C)\mu(mn)a_{mn}
\right|
\ll
A(x)(\log x)^{-222}.
$$

They state explicitly that:

- the cancellation comes from the sign changes of $\mu(mn)$ ;
- the axiom resolves the parity problem;
- Selberg's parity sequence satisfies the ordinary remainder hypothesis but fails the bilinear axiom;
- for twin-prime-type sequences the obstacle is precisely verifying the required bilinear information and high distribution level.

URL:

https://emis.de/ft/50744

## 18.2. Power versus family averaging

Modern dispersion theorems can produce genuine powers when substantial family averaging or extra divisor structure is available.

This remains calibration only: F-RH-023 is a fixed $q=1$ ordinary-factorization bilinear problem.

---

# 19. State transition

Advance candidate state

$$
v1.65
\to
v1.66.
$$

Open Campaign 47:

```text
CAMPAIGN_47
ORDINARY_PRIME_BOUNDARY_BREAKING
ACTIVE
```

Add:

```text
B-RH-115
SHIFT_AVERAGING_CONVERTS_PRIME_LOCAL_DIVISIBILITY_TO_DETERMINISTIC_LATTICE_DISTRIBUTION
CERTIFIED

B-RH-116
SHIFT_AVERAGED_SEQUENCE_HAS_POWER_LEVEL_ASYMPTOTIC_SIEVE_REMAINDER_TO_ANY_D_BELOW_H_BY_A_POWER
CERTIFIED

O-RH-169
PUBLISHED_ASYMPTOTIC_SIEVE_HAS_A_LOGARITHMIC_PRIME_DETECTION_EXTRACTION_FLOOR
CERTIFIED
```

Open:

```text
F-RH-023
SHIFT_AVERAGED_BOUNDARY_BREAKING_BILINEAR_POWER_AXIOM
OPEN_ARITHMETIC
```

No RH certificate is created.

---

# 20. Recommended next action

Do **not** immediately invent another sieve framework.

The next round should first attack C47-B:

```text
Can one derive a power-output exact prime-detection identity
for the special dense sequence a_{N,H},
using polynomial Vaughan/Heath-Brown cutoffs,
such that every linear term is controlled by B-RH-116
and the only balanced term is F-RH-023?
```

If yes, F-RH-023 becomes a genuine root bootstrap target.

If no, the shift-averaged asymptotic-sieve route should be closed before any effort is spent proving the bilinear axiom.

That preserves the Campaign-47 entry rule.

---

# 21. Conclusion

Shift averaging changes the twin-prime sieve geometry in one decisive respect.

The high-level local distribution problem becomes a deterministic lattice-sampling estimate with fixed-power accuracy.

The only surviving classical parity obstruction is the Möbius bilinear form.

That form is now explicit.

The published asymptotic sieve cannot preserve fixed-power accuracy to the final prime-detection output, so a power-output extraction identity is the immediate next gate.

Campaign 47 begins with a real inequality, not a new representation.
