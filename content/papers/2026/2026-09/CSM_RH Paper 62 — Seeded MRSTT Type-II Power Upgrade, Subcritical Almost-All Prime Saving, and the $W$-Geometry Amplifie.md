# CSM_RH Paper 62

## Seeded MRSTT Type-II Power Upgrade, Subcritical Almost-All Prime Saving, and the $W$ -Geometry Amplifier Ceiling

**Project:** CSM_RH  
**Paper:** 62  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Frontier:** F-RH-017-v3  
**Status:** FIRST SEEDED FIXED-POWER INSERTION INTO 2026 MRSTT MACHINERY CERTIFIED / AMPLIFIER CEILING CERTIFIED / SUPERCRITICAL FRONTIER OPEN  
**Canonical entry state:** v1.52 / Paper 61 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 61 corrected the direct exceptional-set amplifier to the sharp local-envelope gate

$$
\nu>\frac{\kappa}{2},
\qquad
c>
\min\left\{
\tau,\frac{\kappa}{2}
\right\},
\qquad
H=X^{1-\tau}.
$$

The present paper asks whether the strongest current almost-all short-interval technology can cross this gate once the PESC seed is fed back into its analytic inputs.

The answer has two parts.

First, the seed genuinely upgrades the current machinery from logarithmic to fixed-power saving in a nonempty parameter range.

Write

$$
d=\frac{\kappa}{2}.
$$

PESC $(\kappa)$ is equivalent to the fixed zero-free half-plane

$$
\beta_*\le1-d.
$$

Besides the prime-number-theorem bound

$$
\psi(x)-x
\ll
x^{1-d+o(1)},
$$

the same zero-free half-plane gives the Mertens bound

$$
\boxed{
M(x)
=
\sum_{n\le x}\mu(n)
\ll
x^{1-d+o(1)}.
}
$$

Consequently, for a dyadic block of length scale $L$,

$$
\boxed{
\sup_{I\subset[L,2L]}
\left|
\sum_{n\in I}
\frac{\mu(n)}{n^{1+it}}
\right|
\ll
(1+|t|)
L^{-d+o(1)}.
}
$$

This is a fixed-power replacement for the Vinogradov-Korobov input at the unprogressed zeta level.

Matomäki, Radziwiłł, Shao, Tao and Teräväinen decompose every Type-II component of $\Lambda$ into two coefficient sequences, each of which is a convolution of at most five dyadically restricted copies of $1$, $\log$, and $\mu$, with each side supported on a scale at least $X^{\varepsilon_0}$.

Hence each side contains a constituent of length at least

$$
X^{\varepsilon_0/5}.
$$

For

$$
H=X^{1-\tau}
$$

and a polynomial Type-II parameter

$$
W=X^w,
$$

the seeded Dirichlet-polynomial bounds verify the hypotheses of MRSTT Lemma 3.5 provided

$$
\boxed{
\tau+\frac{4w}{3}
<
\frac{d\varepsilon_0}{5}.
}
$$

Thus the $\Lambda$ Type-II cells, which unconditionally use only

$$
W=\log^{O(1)}X,
$$

can under a PESC seed use a genuine polynomial $W=X^w$.

Applying MRSTT Lemma 3.5 to the Heath-Brown decomposition gives a fixed-power scale-coherence theorem. If additionally

$$
4w<\tau,
$$

and

$$
H_2=X^{1-4w},
$$

then, outside a set of measure

$$
O
\left(
X^{1-w/10+o(1)}
\right),
$$

one has

$$
\boxed{
\left|
\sum_{x<n\le x+H}\Lambda(n)
-
\frac{H}{H_2}
\sum_{x<n\le x+H_2}\Lambda(n)
\right|
\ll
H X^{-w/10+o(1)}.
}
$$

The seed pointwise PNT estimate controls the long anchor, giving

$$
\boxed{
|\psi(x+H)-\psi(x)-H|
\ll
H X^{-\eta+o(1)}
}
$$

outside the same exceptional set, where

$$
\boxed{
\eta
=
\min
\left\{
\frac{w}{10},
d-4w,
1-\tau-\varepsilon_0
\right\}.
}
$$

For example, with

$$
\tau=\frac{d\varepsilon_0}{100},
\qquad
w=\frac{\tau}{8},
$$

all conditions hold and

$$
\boxed{
\eta
=
\frac{d\varepsilon_0}{8000}
}
$$

for sufficiently small fixed $\varepsilon_0$.

Thus a fixed PESC seed plus existing 2026 MRSTT technology already implies a genuine fixed-power almost-all short-interval prime-number theorem at a sufficiently near-macroscopic scale.

Second, the same calculation proves that this architecture cannot become a PESC amplifier.

MRSTT Lemma 3.5 requires

$$
H_2\le \frac{X}{W^4}.
$$

For a comparison from

$$
H=X^{1-\tau}
$$

to a longer scale $H_2\ge H$, this forces

$$
\boxed{
w\le\frac{\tau}{4}.
}
$$

The lemma then returns an amplitude saving and exceptional-measure saving of only

$$
W^{-1/10}.
$$

Hence even before the seed-frequency restriction is used,

$$
\boxed{
\nu_{\rm MRSTT}
\le
\frac{\tau}{40},
\qquad
c_{\rm MRSTT}
\le
\frac{\tau}{40}.
}
$$

In the actual seeded Dirichlet-polynomial insertion one must moreover have

$$
\tau
<
\frac{6d\varepsilon_0}{35},
$$

so necessarily

$$
\tau\ll d.
$$

The corrected F-RH-017-v3 amplifier gate in this regime is

$$
\nu>d,
\qquad
c>\tau.
$$

Therefore the standard MRSTT Type-II scale-comparison architecture misses both amplifier inequalities by a fixed factor:

$$
\nu_{\rm MRSTT}\ll\tau\ll d,
\qquad
c_{\rm MRSTT}\le\tau/40<\tau.
$$

This is not a logarithmic-versus-polynomial issue anymore. The seed has already repaired that issue. The remaining failure comes from the internal $W$ -geometry and the $W^{-1/10}$ conversion of the Type-II variance lemma.

The paper also separates the structured sieve component from the hard residual. For a polylogarithmic roughness cutoff $R=(\log X)^B$, $0<B<1$, define

$$
q=P(R)=\prod_{p<R}p
$$

and

$$
\Lambda_R^\sharp(n)
=
\frac{q}{\phi(q)}
1_{(n,q)=1}.
$$

Since $q=X^{o(1)}$, this structured component is uniformly flat on every polynomial interval:

$$
\boxed{
\sum_{x<n\le x+H}
\Lambda_R^\sharp(n)
=
H+X^{o(1)}.
}
$$

Its complement has Dirichlet series

$$
\boxed{
D_R(s)
=
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{q}{\phi(q)}
\zeta(s)
\prod_{p<R}
(1-p^{-s}).
}
$$

The pole at $s=1$ cancels exactly, while every nontrivial zero pole of $-\zeta'/\zeta$ survives unchanged because the sieve term vanishes at a nontrivial zero of $\zeta$.

Thus the polynomially flat rough-number approximant is not the missing boundary suppression. The hard zero geometry lives entirely in the parity-sensitive residual.

Paper 62 therefore produces the first genuine fixed-power arithmetic upper estimate after seeding, but also proves that the current Type-II machinery cannot cross the sharp F-RH-017-v3 gate.

No RH theorem is claimed.

---

# 1. Entry state

Assume PESC $(\kappa)$ for a fixed

$$
0<\kappa<1.
$$

Set

$$
\boxed{
d=\frac{\kappa}{2}.
}
$$

Paper 55 gives

$$
\boxed{
\zeta(s)\ne0
\qquad
\Re s>1-d
}
$$

and

$$
\boxed{
\psi(x)-x
\ll
x^{1-d+o(1)}.
}
$$

Paper 61 gives the current direct amplifier gate, for

$$
H=X^{1-\tau},
$$

as

$$
\boxed{
\nu>d,
\qquad
c>\min(d,\tau).
}
$$

The purpose of this paper is to insert the seed into the 2026 almost-all Type-II technology and compare its output to this gate.

---

# 2. Seeded Mertens bound

The reciprocal zeta function has Dirichlet series

$$
\boxed{
\frac1{\zeta(s)}
=
\sum_{n=1}^{\infty}
\frac{\mu(n)}{n^s}
}
$$

for $\Re s>1$.

Since the seed excludes every zeta zero from

$$
\Re s>1-d,
$$

standard Perron / contour shifting in any fixed smaller half-plane gives, for every fixed $\epsilon_1>0$,

$$
\boxed{
M(x)
=
\sum_{n\le x}\mu(n)
\ll_{\epsilon_1}
x^{1-d+\epsilon_1}.
}
$$

At exponent resolution,

$$
\boxed{
M(x)
\ll
x^{1-d+o(1)}.
}
$$

This is the Möbius analogue of the seeded PNT pointwise bound.

---

# 3. Seeded dyadic Möbius Dirichlet polynomial

Let

$$
I\subset[L,2L]
$$

be any interval.

By partial summation,

$$
\sum_{n\in I}
\frac{\mu(n)}{n^{1+it}}
$$

is a linear combination of endpoint terms of size

$$
L^{-1}|M(u)|
$$

and an integral bounded by

$$
(1+|t|)
\int_L^{2L}
|M(u)|u^{-2}du.
$$

Thus:

## Theorem 3.1 — Seeded Möbius Dirichlet-polynomial power bound

Uniformly for real $t$,

$$
\boxed{
\sup_{I\subset[L,2L]}
\left|
\sum_{n\in I}
\frac{\mu(n)}{n^{1+it}}
\right|
\ll
(1+|t|)
L^{-d+o(1)}.
}
$$

The same argument applied to $\Lambda(n)-1$ gives

$$
\boxed{
\sup_{I\subset[L,2L]}
\left|
\sum_{n\in I}
\frac{\Lambda(n)-1}{n^{1+it}}
\right|
\ll
(1+|t|)
L^{-d+o(1)}.
}
$$

Create:

```text
B-RH-072
SEEDED_MOBIUS_AND_VON_MANGOLDT_DIRICHLET_POLYNOMIAL_POWER_WINDOW
CERTIFIED
```

---

# 4. Elementary $1$ and $\log$ blocks

Let

$$
f(n)=1
$$

or

$$
f(n)=\log n
$$

on a dyadic interval $[L,2L]$.

For

$$
1\le|t|\le L/2,
$$

partial summation against the integral of $x^{-1-it}$ gives

$$
\boxed{
\sup_{I\subset[L,2L]}
\left|
\sum_{n\in I}
\frac{1}{n^{1+it}}
\right|
\ll
\frac1{|t|}
+
\frac{|t|}{L}
+
\frac1L
}
$$

and

$$
\boxed{
\sup_{I\subset[L,2L]}
\left|
\sum_{n\in I}
\frac{\log n}{n^{1+it}}
\right|
\ll
(\log X)
\left(
\frac1{|t|}
+
\frac{|t|}{L}
+
\frac1L
\right).
}
$$

Thus any sufficiently long $1$ - or $\log$ -block also supplies polynomial high-frequency decay once

$$
|t|\ge X^w.
$$

---

# 5. Seeded composite Type-II Dirichlet polynomial

The MRSTT Heath-Brown decomposition used for the Type-II part of $\Lambda$ has the following form.

Each Type-II coefficient sequence $a$ or $b$:

1. is a convolution of at most five factors;
2. every factor is a dyadic restriction of one of
   $$
   1,\quad \log,\quad \mu;
   $$
3. each complete side is supported on a scale at least
   $$
   X^{\varepsilon_0}.
   $$

Therefore, on each side, at least one constituent has scale

$$
\boxed{
L\ge X^{\varepsilon_0/5}.
}
$$

To estimate a maximal dyadic Dirichlet polynomial for the convolution, pull out all other variables. Their absolute $1/n$ weighted sums cost only $\log^{O(1)}X$. The output dyadic restriction leaves the distinguished constituent summed over an interval inside its dyadic support.

Hence Theorems 3.1 and Section 4 apply to the distinguished block.

Let

$$
H=X^{1-\tau},
\qquad
W=X^w.
$$

MRSTT Lemma 3.5 requires Dirichlet-polynomial control for

$$
W\le|t|\le\frac{XW}{H}
=
X^{\tau+w}.
$$

For a distinguished Möbius block of minimal length $X^{\varepsilon_0/5}$, Theorem 3.1 gives

$$
\boxed{
|D_\mu(1+it)|
\ll
X^{
\tau+w-d\varepsilon_0/5+o(1)
}.
}
$$

To make this at most

$$
W^{-1/3}
=
X^{-w/3},
$$

it suffices that

$$
\boxed{
\tau+\frac{4w}{3}
<
\frac{d\varepsilon_0}{5}.
}
$$

For a $1$ - or $\log$ -block the analogous condition is weaker once the same inequality holds.

Thus:

## Theorem 5.1 — Polynomial MRSTT Type-II input from a PESC seed

Assume

$$
\boxed{
\tau+\frac{4w}{3}
<
\frac{d\varepsilon_0}{5}.
}
$$

Then every unprogressed Type-II coefficient pair in the MRSTT/Heath-Brown decomposition of $\Lambda$ satisfies the Dirichlet-polynomial hypotheses of MRSTT Lemma 3.5 with

$$
\boxed{
W=X^w.
}
$$

Create:

```text
B-RH-073
SEEDED_MRSTT_TYPEII_POLYNOMIAL_W_INPUT
CERTIFIED
```

This is exactly the point where the seed turns the $\Lambda$ input from logarithmic to polynomial.

---

# 6. External comparison with the 2026 MRSTT theorem

Unconditionally, MRSTT Lemma 3.2 takes

$$
\boxed{
W_\Lambda=\log^A X,
}
$$

while for the divisor functions

$$
\boxed{
W_{d_k}=X^{c_k}.
}
$$

In their proof of the major-arc theorem, this produces:

```text
Lambda, mu:
arbitrary log-power saving.

d_k:
fixed power saving.
```

Theorem 5.1 shows that a PESC seed changes the unprogressed $\Lambda$ Type-II input to the divisor-function side of this qualitative divide: polynomial $W$ becomes legal on a fixed parameter window.

This does not claim the full MRSTT theorem with all maximal progression uniformity at polynomial precision. The present insertion is deliberately restricted to the direct unprogressed short-interval problem F-RH-017.

---

# 7. Type-II fixed-power scale coherence

Take

$$
H_1=H=X^{1-\tau}
$$

and choose

$$
\boxed{
H_2=X^{1-4w}.
}
$$

If

$$
4w<\tau,
$$

then

$$
H_2>H_1.
$$

Moreover,

$$
\boxed{
H_2=\frac{X}{W^4},
}
$$

so the geometric condition in MRSTT Lemma 3.5 is saturated.

Assume also

$$
H_1\ge X^{1/3+\varepsilon_0}.
$$

By Theorem 5.1, every Type-II cell satisfies the Dirichlet-polynomial hypotheses of MRSTT Lemma 3.5(i).

Therefore each Type-II cell obeys

$$
\boxed{
\left|
S_{H_1}(x)
-
\frac{H_1}{H_2}
S_{H_2}(x)
\right|
\ll
H_1X^{-w/10}
}
$$

outside a set of measure

$$
\boxed{
O
\left(
X^{1-w/10+o(1)}
\right).
}
$$

There are only $\log^{O(1)}X$ Heath-Brown cells, so the same power exponent survives their union.

---

# 8. Type-I cells are cheaper

The Type-I cells have form

$$
a*\psi,
$$

where $a$ is supported on

$$
M\le X^{\varepsilon_0}
$$

and $\psi$ is $1$ or a fixed power of $\log$.

Counting the inner variable in the two intervals gives deterministically

$$
\boxed{
\left|
S_{H_1}^{I}(x)
-
\frac{H_1}{H_2}
S_{H_2}^{I}(x)
\right|
\ll
X^{\varepsilon_0+o(1)}.
}
$$

Relative to

$$
H_1=X^{1-\tau},
$$

this is

$$
\boxed{
H_1
X^{-(1-\tau-\varepsilon_0)+o(1)}.
}
$$

Thus the Type-I cells are not the limiting term in the near-macroscopic seeded regime.

---

# 9. Root scale-coherence theorem

Sum all Type-I and Type-II Heath-Brown cells.

## Theorem 9.1 — Seeded fixed-power scale coherence for $\Lambda$

Assume

$$
4w<\tau,
$$

$$
\tau+\frac{4w}{3}
<
\frac{d\varepsilon_0}{5},
$$

and

$$
1-\tau>\frac13+\varepsilon_0.
$$

Then, outside a set of measure

$$
O
\left(
X^{1-w/10+o(1)}
\right),
$$

$$
\boxed{
\left|
\sum_{x<n\le x+H}\Lambda(n)
-
\frac{H}{H_2}
\sum_{x<n\le x+H_2}\Lambda(n)
\right|
\ll
H
X^{-\eta_{\rm coh}+o(1)},
}
$$

where

$$
\boxed{
\eta_{\rm coh}
=
\min
\left\{
\frac{w}{10},
1-\tau-\varepsilon_0
\right\}.
}
$$

Create:

```text
B-RH-074
SEEDED_MRSTT_FIXED_POWER_LAMBDA_SCALE_COHERENCE
CERTIFIED
```

---

# 10. Anchor insertion

Write

$$
A(x)=\psi(x)-x.
$$

Then

$$
\sum_{x<n\le x+H_2}\Lambda(n)
=
H_2
+
A(x+H_2)-A(x).
$$

The seed pointwise bound gives

$$
\boxed{
|A(x+H_2)-A(x)|
\ll
X^{1-d+o(1)}.
}
$$

Multiplying by $H/H_2$ gives

$$
\boxed{
\frac{H}{H_2}
|A(x+H_2)-A(x)|
\ll
H
X^{-d+4w+o(1)}.
}
$$

Combining with Theorem 9.1:

## Theorem 10.1 — Seeded subcritical almost-all short-interval power theorem

Outside a set of measure

$$
O
\left(
X^{1-w/10+o(1)}
\right),
$$

$$
\boxed{
|\psi(x+H)-\psi(x)-H|
\ll
H
X^{-\eta+o(1)},
}
$$

where

$$
\boxed{
\eta
=
\min
\left\{
\frac{w}{10},
d-4w,
1-\tau-\varepsilon_0
\right\}.
}
$$

Create:

```text
B-RH-075
SEEDED_SUBCRITICAL_ALMOST_ALL_SHORT_INTERVAL_FIXED_POWER_THEOREM
CERTIFIED
```

This is a genuine fixed-power arithmetic upper estimate obtained from the seed plus existing Type-II technology.

---

# 11. Explicit safe parameter choice

Fix a sufficiently small

$$
0<\varepsilon_0<\frac{1}{10}.
$$

Choose

$$
\boxed{
\tau
=
\frac{d\varepsilon_0}{100}
}
$$

and

$$
\boxed{
w
=
\frac{\tau}{8}
=
\frac{d\varepsilon_0}{800}.
}
$$

Then

$$
4w=\frac{\tau}{2}<\tau.
$$

Also

$$
\tau+\frac{4w}{3}
=
\frac{7\tau}{6}
=
\frac{7d\varepsilon_0}{600}
<
\frac{d\varepsilon_0}{5}.
$$

The MRSTT restriction

$$
W\le X^{\varepsilon_0/1000}
$$

also holds because

$$
w
=
\frac{d\varepsilon_0}{800}
\le
\frac{\varepsilon_0}{1600}.
$$

Finally,

$$
\frac{w}{10}
=
\boxed{
\frac{d\varepsilon_0}{8000}
}
$$

is far smaller than both $d-4w$ and $1-\tau-\varepsilon_0$.

Thus:

## Corollary 11.1

For

$$
H
=
X^{1-d\varepsilon_0/100},
$$

one has

$$
\boxed{
|\psi(x+H)-\psi(x)-H|
\ll
H
X^{-d\varepsilon_0/8000+o(1)}
}
$$

for all $x\in[X,2X]$ outside a set of measure

$$
\boxed{
O
\left(
X^{1-d\varepsilon_0/8000+o(1)}
\right).
}
$$

This is deliberately crude. Its significance is the existence of a fixed positive exponent, not the numerical constant.

---

# 12. Why this does not amplify PESC

The current frontier F-RH-017-v3 requires

$$
\boxed{
\nu>d
}
$$

and, in the present regime

$$
\tau\ll d,
$$

$$
\boxed{
c>\tau.
}
$$

The MRSTT Type-II scale-comparison lemma contains an internal ceiling.

Because

$$
H_2\le\frac{X}{W^4}
$$

and $H_2\ge H=X^{1-\tau}$,

$$
\boxed{
w\le\frac{\tau}{4}.
}
$$

Its pointwise conclusion has saving

$$
W^{-1/10},
$$

and its exceptional set has the same power saving.

Therefore the strongest exponents directly available from this lemma satisfy

$$
\boxed{
\nu_{\rm TII}
\le
\frac{w}{10}
\le
\frac{\tau}{40}
}
$$

and

$$
\boxed{
c_{\rm TII}
\le
\frac{w}{10}
\le
\frac{\tau}{40}.
}
$$

But

$$
\tau\ll d.
$$

Hence

$$
\boxed{
\nu_{\rm TII}
\ll d
}
$$

and

$$
\boxed{
c_{\rm TII}<\tau.
}
$$

Both F-RH-017-v3 inequalities fail.

---

# 13. Mean-square form makes the ceiling stronger

The proof of MRSTT Lemma 3.5 first establishes a mean-square estimate of schematic size

$$
\boxed{
\frac1X
\int
|\Delta_{\rm TII}(x)|^2dx
\ll
H^2
W^{-3/10}
\log^{O(1)}X.
}
$$

Suppose one asks for a stronger threshold

$$
H X^{-\nu}.
$$

Chebyshev gives exceptional measure at most

$$
X^{1-c+o(1)}
$$

only with

$$
\boxed{
c
\le
\frac{3w}{10}
-
2\nu.
}
$$

For any supercritical target

$$
\nu>d
$$

in the seeded admissible range $w\ll\tau\ll d$, the right-hand side is negative.

Thus changing the Chebyshev threshold inside the existing mean-square proof cannot repair the amplifier failure.

Create:

```text
O-RH-145
SEEDED_MRSTT_TYPEII_W_GEOMETRY_CANNOT_REACH_F_RH_017_SUPERCRITICAL_GATE
CERTIFIED_AS_METHOD_BARRIER
```

This is a barrier for the existing MRSTT Lemma-3.5 scale-comparison architecture, not for every future Type-II method.

---

# 14. A polynomially flat rough-number approximant

Fix

$$
0<B<1
$$

and define

$$
R=(\log X)^B.
$$

Let

$$
q=P(R)
=
\prod_{p<R}p.
$$

The prime number theorem for the Chebyshev function at this polylogarithmic scale gives

$$
\log q
=
(1+o(1))R,
$$

so

$$
\boxed{
q=X^{o(1)}.
}
$$

Define

$$
\boxed{
\Lambda_R^\sharp(n)
=
\frac{q}{\phi(q)}
1_{(n,q)=1}.
}
$$

This sequence is periodic modulo $q$.

On an interval of length $H=X^\alpha$,

$$
\#\{x<n\le x+H:(n,q)=1\}
=
\frac{H\phi(q)}{q}
+
O(q).
$$

Therefore

$$
\boxed{
\sum_{x<n\le x+H}
\Lambda_R^\sharp(n)
=
H
+
O\left(
\frac{q^2}{\phi(q)}
\right)
=
H+X^{o(1)}.
}
$$

Hence the rough structured component is uniformly flat at every fixed polynomial scale.

---

# 15. The residual carries all nontrivial zero poles

The Dirichlet series of the rough approximant is

$$
\boxed{
\sum_{n\ge1}
\frac{\Lambda_R^\sharp(n)}{n^s}
=
\frac{q}{\phi(q)}
\zeta(s)
\prod_{p<R}
(1-p^{-s}).
}
$$

Define the residual

$$
\boxed{
r_R(n)
=
\Lambda(n)-\Lambda_R^\sharp(n).
}
$$

Its Dirichlet series is

$$
\boxed{
D_R(s)
=
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{q}{\phi(q)}
\zeta(s)
\prod_{p<R}
(1-p^{-s}).
}
$$

At

$$
s=1,
$$

the second term has residue

$$
\frac{q}{\phi(q)}
\prod_{p<R}
\left(
1-\frac1p
\right)
=
1,
$$

so the main pole cancels exactly.

At a nontrivial zero $\rho$ of zeta, the sieve term vanishes:

$$
\zeta(\rho)=0.
$$

Therefore every nontrivial zero pole of

$$
-\frac{\zeta'}{\zeta}
$$

survives in $D_R$ with the same residue.

Thus:

## Theorem 15.1 — Flat structured part / zero-pole residual decomposition

At polynomial interval scales,

$$
\boxed{
\Lambda_R^\sharp
}
$$

is uniformly flat up to $X^{o(1)}$, while

$$
\boxed{
r_R=\Lambda-\Lambda_R^\sharp
}
$$

carries the full nontrivial zeta-zero pole structure.

Create:

```text
B-RH-076
POLYLOG_ROUGH_APPROXIMANT_IS_POLYNOMIALLY_FLAT_AND_ZERO_POLES_REMAIN_IN_RESIDUAL
CERTIFIED
```

This identifies the parity-sensitive residual, not the structured rough-number model, as the exact hard arithmetic object.

---

# 16. Relation to the sieve parity problem

A rough-number approximant captures local divisibility by small primes, but it does not distinguish primes from general integers with no small prime factors at a level sufficient to resolve the parity of the number of prime factors.

This is the classical parity obstruction in sieve theory.

Theorem 15.1 gives a spectral version tailored to CSM_RH:

```text
small-prime structured part:
uniformly flat at polynomial scales.

nontrivial zeta poles:
entirely retained by the residual.
```

Thus further improvement must use information beyond roughness / ordinary sieve positivity.

No claim is made that the classical parity problem alone proves the CSM_RH barrier.

It is used as method calibration.

---

# 17. Comparison with current 2026 results

MRSTT prove for

$$
X^{1/3+\varepsilon}\le H\le X
$$

that

$$
\Lambda-\Lambda^\sharp
$$

has arbitrary log-power discorrelation on almost all intervals.

Their Lemma 3.2 explicitly uses

$$
W_\Lambda=\log^A X
$$

but permits

$$
W_{d_k}=X^{c_k}.
$$

Their Lemma 3.5 itself accepts

$$
1\le W\le X^{\varepsilon/1000}
$$

and outputs a Type-II saving

$$
H/W^{1/10}
$$

outside an exceptional set of measure

$$
X\log^{O(1)}X/W^{1/10}.
$$

Thus the polynomial $W$ used in the present paper is already structurally supported by the 2026 Type-II theorem. The new ingredient is the seeded fixed-strip Dirichlet-polynomial input which verifies its hypotheses for the unprogressed $\Lambda$ cells.

This explains, within one common architecture, why:

- the unseeded $\Lambda$ theorem has log savings;
- the divisor-function theorem can have power savings;
- a seeded $\Lambda$ theorem can also acquire power savings;
- yet the existing Type-II exponent conversion remains far below the supercritical PESC-amplifier scale.

External source:

K. Matomäki, M. Radziwiłł, X. Shao, T. Tao, J. Teräväinen,
*Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*,
Inventiones Mathematicae 244 (2026), 967–1091.

---

# 18. Updated frontier

Paper 62 does not change the sharp direct target.

F-RH-017-v3 remains:

$$
\boxed{
\#\left\{
n\in[X,2X]:
|\psi(n+H)-\psi(n)-H|
>
H X^{-\nu}
\right\}
\ll
X^{1-c}
}
$$

with

$$
H=X^{1-\tau},
$$

$$
\boxed{
\nu>d,
\qquad
c>\min(d,\tau).
}
$$

What changes is the internal status of the arithmetic upper problem.

We now know:

```text
fixed-power almost-all saving below the seed boundary:
reachable by seeded current technology.

supercritical saving beyond the seed boundary:
not reachable by the present MRSTT Type-II W-geometry.
```

The remaining gap is therefore not simply:

```text
log saving -> power saving.
```

That gap has been crossed.

It is:

```text
subcritical power saving -> boundary-crossing power saving.
```

---

# 19. Recommended next attack

The next theorem must improve one of the two Type-II geometry losses:

1. permit a substantially larger effective $W$ relative to $X/H$ ; or
2. convert a given polynomial $W$ into a much stronger amplitude / exceptional saving than $W^{-1/10}$.

Equivalently, one needs a new Type-II large-deviation theorem rather than a better Vinogradov-Korobov input.

Candidate next track:

```text
Campaign 46 / PT5
SEEDED TYPE-II LARGE-DEVIATION BEYOND W-GEOMETRY
```

Required shape:

$$
\boxed{
\frac1X
\int
|\Delta_{\rm TII}(x)|^2dx
\ll
H^2X^{-2d-\eta}
}
$$

or a sign-sensitive / $L^1$ replacement strong enough to yield the F-RH-017-v3 exceptional gate.

Hard rejections:

```text
CLAIM_SEED_DIRICHLET_POLYNOMIAL_POWER_WINDOW_ALREADY_AMPLIFIES_PESC
IGNORE_H2_LE_X_OVER_W4
TREAT_W_MINUS_ONE_TENTH_AS_IF_IT_COULD_EXCEED_D_WHEN_TAU_LL_D
USE_POLYLOG_ROUGH_APPROXIMANT_AS_IF_IT_REMOVED_NONTRIVIAL_ZERO_POLES
REVERT_TO_LOG_VERSUS_POWER_AS_THE_ONLY BOTTLENECK
ASSUME_RH
```

---

# 20. State transition

Advance the candidate state from

$$
v1.52
$$

to

$$
v1.53.
$$

Add:

```text
B-RH-072
SEEDED_MOBIUS_AND_VON_MANGOLDT_DIRICHLET_POLYNOMIAL_POWER_WINDOW
CERTIFIED
```

Add:

```text
B-RH-073
SEEDED_MRSTT_TYPEII_POLYNOMIAL_W_INPUT
CERTIFIED
```

Add:

```text
B-RH-074
SEEDED_MRSTT_FIXED_POWER_LAMBDA_SCALE_COHERENCE
CERTIFIED
```

Add:

```text
B-RH-075
SEEDED_SUBCRITICAL_ALMOST_ALL_SHORT_INTERVAL_FIXED_POWER_THEOREM
CERTIFIED
```

Add:

```text
B-RH-076
POLYLOG_ROUGH_APPROXIMANT_IS_POLYNOMIALLY_FLAT_AND_ZERO_POLES_REMAIN_IN_RESIDUAL
CERTIFIED
```

Add:

```text
O-RH-145
SEEDED_MRSTT_TYPEII_W_GEOMETRY_CANNOT_REACH_F_RH_017_SUPERCRITICAL_GATE
CERTIFIED_AS_METHOD_BARRIER
```

No RH certificate is created.

---

# 21. Conclusion

A fixed PESC seed changes the state of current short-interval technology in a measurable way.

It gives fixed-power Mertens cancellation.

That cancellation upgrades the MRSTT Type-II Dirichlet-polynomial input from logarithmic $W$ to polynomial $W$.

The existing 2026 Type-II theorem then gives a genuine fixed-power almost-all prime-number-theorem estimate.

So the seed is not inert.

But the same theorem contains a geometric ceiling:

$$
w\le\frac{\tau}{4},
\qquad
\text{output saving}\sim\frac{w}{10}.
$$

In the seed-admissible region

$$
\tau\ll d,
$$

this is parametrically below the boundary exponent $d$ and below the required exceptional exponent $\tau$.

Therefore the campaign has crossed the log-to-power barrier but not the boundary-crossing barrier.

The next missing object is a stronger Type-II large-deviation principle, not another zero-free-region input.
