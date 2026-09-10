# CSM_RH Paper 59

## Seeded $L^p$ Residue-Chain Amplification, $L^1$ Optimality, and the Minimal Exceptional-Set Strip-Gap Gate

**Project:** CSM_RH  
**Paper:** 59  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Direct frontier:** F-RH-017  
**Status:** STRONGER DETERMINISTIC EXCEPTIONAL-SET AMPLIFIER CERTIFIED / SUPERCRITICAL ARITHMETIC THRESHOLD STILL OPEN  
**Canonical entry state:** v1.49 / Paper 58 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 56 converted a seeded shrinking-threshold exceptional-set theorem into a lag $L^2$ estimate and then into a PESC exponent improvement. That route required

$$
c>2(1-\alpha)
$$

when

$$
H=N^\alpha
$$

and

$$
|\{x:|U_H(x)|>HN^{-\nu}\}|
\ll
N^{1-c}.
$$

The present paper proves that this is not the optimal deterministic use of the exceptional set.

Let

$$
A(n)=\psi(n)-n,
\qquad
U_H(n)=A(n+H)-A(n).
$$

Assume PESC $(\kappa)$ and write

$$
d=\frac{\kappa}{2}.
$$

Paper 55 gives the pointwise seed envelope

$$
|A(n)|
\ll
n^{1-d+o(1)}.
$$

For every fixed $p\ge1$, a residue-chain inequality gives

$$
\sum_{n\le2N}|A(n)|^p
\ll_p
\frac{N}{H}
\sum_{r\le H}|A(r)|^p
+
\left(
\frac{N}{H}
\right)^p
\sum_{n\le2N-H}|U_H(n)|^p.
$$

If

$$
H=N^\alpha
$$

and

$$
\boxed{
\#\left\{
n\in[N,2N]:
|U_H(n)|>HN^{-\nu}
\right\}
\ll
N^{1-c},
}
$$

then the seed pointwise envelope on the exceptional set yields

$$
\sum_{n\le2N}|A(n)|^p
\ll
N^{1+p(1-d_p')+o(1)}
$$

for every

$$
\boxed{
d_p'
<
\Psi_p(d;\alpha,\nu,c)
:=
\min
\left\{
\nu,\,
d+\alpha-1+\frac{c}{p},\,
1-\alpha(1-d)
\right\}.
}
$$

A dyadic $L^p$ Mellin argument then excludes all zeta zeros with

$$
\Re\rho>1-d_p'.
$$

Using Paper 55's fixed-exponent PESC/zero-strip equivalence, this gives PESC $(\kappa')$ for every

$$
\boxed{
\kappa'
<
2\Psi_p
\left(
\frac{\kappa}{2};
\alpha,\nu,c
\right).
}
$$

Among all $p\ge1$, the only $p$ -dependent term is $c/p$. Therefore:

$$
\boxed{
p=1
}
$$

is the optimal member of the entire $L^p$ residue-chain family.

The resulting $L^1$ amplification law is

$$
\boxed{
\kappa'
<
\Phi_1(\kappa;\alpha,\nu,c)
:=
\min
\left\{
2\nu,\,
\kappa+2c+2\alpha-2,\,
2-2\alpha+\alpha\kappa
\right\}.
}
$$

Strict amplification occurs exactly when

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>1-\alpha,
\qquad
\alpha<1.
}
$$

Thus the exceptional-set requirement from Paper 56 is cut in half.

For the near-macroscopic parametrization

$$
H=N^{1-\tau},
$$

the strict gate is simply

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>\tau.
}
$$

The output gain is

$$
\boxed{
\eta
<
\min
\left\{
2\nu-\kappa,\,
2(c-\tau),\,
(2-\kappa)\tau
\right\}.
}
$$

If the threshold is not the bottleneck and $c$ is fixed, the optimal scale is

$$
\boxed{
\tau_*
=
\frac{2c}{4-\kappa},
\qquad
\alpha_*
=
1-\frac{2c}{4-\kappa},
}
$$

and the one-step gain is

$$
\boxed{
\eta_*
=
\frac{
2c(2-\kappa)
}{
4-\kappa
}.
}
$$

This is twice the exceptional-set gain produced by the $L^2$ bridge of Paper 56 for the same $c$.

The paper also audits the current Gafni–Tao exceptional-set architecture against a polynomially shrinking threshold. Their published theorem fixes the relative threshold $\delta>0$ and a sufficiently large integer $J=J(\delta,\theta,\varepsilon)$ before taking $X\to\infty$. In their explicit-formula reduction the truncation error is $O(X^\theta/J)$, so replacing

$$
\delta
$$

by

$$
X^{-\nu}
$$

requires at least

$$
J\gg X^\nu.
$$

Thus the published theorem cannot be invoked by direct substitution.

More importantly, even after rebuilding the proof with a polynomial truncation height, the standard $L^2$ and $L^4$ zero-packet Markov exponents are supercritical at the seeded boundary whenever

$$
\nu>\frac{\kappa}{2}.
$$

Hence the fixed-threshold parameter issue is not the sole obstruction. The boundary mode remains the genuine wall.

The direct Campaign-46 frontier is therefore strengthened:

```text
F-RH-017-v2
SEEDED_SUPERCRITICAL_SHRINKING_THRESHOLD_EXCEPTIONAL_SET
```

with the minimal deterministic requirements

$$
\boxed{
H=N^{1-\tau},
\qquad
\nu>\frac{\kappa}{2},
\qquad
c>\tau.
}
$$

No RH theorem is claimed.

---

# 1. Seed notation

Assume PESC $(\kappa)$ for fixed

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
\beta_*\le1-d
}
$$

and the pointwise PNT error estimate

$$
\boxed{
|A(x)|
=
|\psi(x)-x|
\ll
x^{1-d+o(1)}.
}
$$

Let

$$
H=N^\alpha,
\qquad
0<\alpha<1.
$$

For integers $n$ define

$$
\boxed{
U_H(n)
=
A(n+H)-A(n).
}
$$

---

# 2. A general residue-chain $L^p$ inequality

Fix

$$
1\le p<\infty.
$$

Write every integer $n\le2N$ as

$$
n=r+kH,
$$

with

$$
1\le r\le H
$$

and

$$
0\le k\le M,
\qquad
M\ll\frac{N}{H}.
$$

Along each residue chain,

$$
A(r+kH)
=
A(r)
+
\sum_{j=0}^{k-1}
U_H(r+jH).
$$

Using

$$
|x+y|^p
\le
2^{p-1}
\left(
|x|^p+|y|^p
\right)
$$

and

$$
\left|
\sum_{j<k}u_j
\right|^p
\le
k^{p-1}
\sum_{j<k}|u_j|^p,
$$

we get

$$
|A(r+kH)|^p
\ll_p
|A(r)|^p
+
k^{p-1}
\sum_{j<k}
|U_H(r+jH)|^p.
$$

Summing $k\le M$ gives

$$
\sum_{k\le M}
|A(r+kH)|^p
\ll_p
M|A(r)|^p
+
M^p
\sum_{j<M}
|U_H(r+jH)|^p.
$$

Summing over $r$ proves:

## Theorem 2.1 — Residue-chain $L^p$ inequality

$$
\boxed{
\sum_{n\le2N}|A(n)|^p
\ll_p
\frac{N}{H}
\sum_{r\le H}|A(r)|^p
+
\left(
\frac{N}{H}
\right)^p
\sum_{n\le2N-H}|U_H(n)|^p.
}
$$

Create:

```text
B-RH-062
SEEDED_RESIDUE_CHAIN_LP_INEQUALITY
CERTIFIED
```

---

# 3. Seeded anchor in $L^p$

The seed pointwise bound gives

$$
\sum_{r\le H}|A(r)|^p
\ll
H^{1+p(1-d)+o(1)}.
$$

Therefore the residue-chain anchor is

$$
\boxed{
\frac{N}{H}
\sum_{r\le H}|A(r)|^p
\ll
N
H^{p(1-d)+o(1)}.
}
$$

At

$$
H=N^\alpha,
$$

this is

$$
\boxed{
N^{1+\alpha p(1-d)+o(1)}.
}
$$

---

# 4. Exceptional-set $L^p$ lag bound

Assume

$$
\boxed{
|\mathcal E|
\ll
N^{1-c},
}
$$

where

$$
\mathcal E
=
\left\{
n\in[N,2N]:
|U_H(n)|>HN^{-\nu}
\right\}.
$$

## Good set

On the complement,

$$
|U_H(n)|^p
\le
H^pN^{-p\nu}.
$$

Hence

$$
\boxed{
\sum_{n\notin\mathcal E}|U_H(n)|^p
\ll
N
H^p
N^{-p\nu}.
}
$$

## Bad set

The seed pointwise envelope gives

$$
|U_H(n)|
\le
|A(n+H)|+|A(n)|
\ll
N^{1-d+o(1)}.
$$

Therefore

$$
\boxed{
\sum_{n\in\mathcal E}|U_H(n)|^p
\ll
N^{1-c+p(1-d)+o(1)}.
}
$$

Thus

$$
\boxed{
\sum_{n\le2N-H}|U_H(n)|^p
\ll
NH^pN^{-p\nu}
+
N^{1-c+p(1-d)+o(1)}.
}
$$

---

# 5. Global seeded $L^p$ error exponent

Multiply the lag terms by

$$
(N/H)^p.
$$

The good-set term becomes

$$
\boxed{
N^{p+1-p\nu}.
}
$$

The bad-set term becomes

$$
\boxed{
N^{1-c+p(2-d-\alpha)+o(1)}.
}
$$

The anchor term is

$$
\boxed{
N^{1+\alpha p(1-d)+o(1)}.
}
$$

We compare these with the target form

$$
\boxed{
N^{1+p(1-d')+o(1)}.
}
$$

The three constraints are:

$$
d'<\nu,
$$

$$
d'
<
d+\alpha-1+\frac{c}{p},
$$

and

$$
d'
<
1-\alpha(1-d).
$$

Therefore:

## Theorem 5.1 — Seeded exceptional-set $L^p$ exponent

For every

$$
d_p'
<
\boxed{
\Psi_p(d;\alpha,\nu,c)
=
\min
\left\{
\nu,\,
d+\alpha-1+\frac{c}{p},\,
1-\alpha(1-d)
\right\},
}
$$

one has

$$
\boxed{
\sum_{n\le2N}|A(n)|^p
\ll
N^{1+p(1-d_p')+o(1)}.
}
$$

Create:

```text
B-RH-063
SEEDED_EXCEPTIONAL_SET_TO_GLOBAL_LP_PNT_ERROR_GAIN
CERTIFIED
```

---

# 6. Global $L^p$ error implies a zero-free strip

The discrete / continuous difference between

$$
A(n)
$$

and

$$
\psi(x)-x
$$

inside a unit interval is bounded by $1$, so the same exponent holds for

$$
\int_N^{2N}
|\psi(x)-x|^pdx.
$$

Suppose

$$
\int_X^{2X}
|\psi(x)-x|^pdx
\ll
X^{1+p(1-d')+\varepsilon}.
$$

Let

$$
s=\sigma+it.
$$

For $p>1$, Hölder gives

$$
\begin{aligned}
\int_X^{2X}
|\psi(x)-x|
x^{-\sigma-1}dx
&\le
\left(
\int_X^{2X}
|\psi(x)-x|^pdx
\right)^{1/p}
\\
&\quad\times
\left(
\int_X^{2X}
x^{-q(\sigma+1)}dx
\right)^{1/q}
\\
&\ll
X^{1-d'-\sigma+\varepsilon/p},
\end{aligned}
$$

where

$$
1/p+1/q=1.
$$

For $p=1$ the same bound follows directly.

Thus the dyadic Mellin sum converges locally uniformly for

$$
\boxed{
\Re s>1-d'.
}
$$

By Paper 53's Mellin identity,

$$
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{s}{s-1}
$$

is analytic there.

Therefore:

## Theorem 6.1 — $L^p$ Mellin strip theorem

If the dyadic $L^p$ exponent $d'$ holds, then

$$
\boxed{
\zeta(s)\ne0
\quad
\text{for}
\quad
\Re s>1-d'.
}
$$

By Paper 55, this is equivalent at exponent scale to PESC $(\kappa')$ for every

$$
\boxed{
\kappa'<2d'.
}
$$

Combining with Theorem 5.1:

## Theorem 6.2 — Seeded $L^p$ exceptional-set PESC amplifier

$$
\boxed{
\kappa'
<
2
\Psi_p
\left(
\frac{\kappa}{2};
\alpha,\nu,c
\right).
}
$$

Create:

```text
B-RH-064
SEEDED_LP_EXCEPTIONAL_SET_TO_ZERO_STRIP_AND_PESC_AMPLIFICATION
CERTIFIED
```

---

# 7. $L^1$ is optimal in the entire $L^p$ family

The function

$$
\Psi_p
=
\min
\left\{
\nu,\,
d+\alpha-1+\frac{c}{p},\,
1-\alpha(1-d)
\right\}
$$

depends on $p$ only through

$$
c/p.
$$

For

$$
p\ge1,
$$

$$
\frac{c}{p}
\le c.
$$

Hence:

## Theorem 7.1 — $L^1$ optimality

Among all fixed

$$
p\ge1,
$$

the strongest deterministic zero-strip output from the seeded residue-chain / exceptional-set architecture is attained at

$$
\boxed{
p=1.
}
$$

Create:

```text
B-RH-065
L1_IS_OPTIMAL_SEEDED_EXCEPTIONAL_SET_RESIDUE_CHAIN_EXPONENT_CONVERTER
CERTIFIED
```

This is the key improvement over Paper 56.

---

# 8. The optimal $L^1$ amplification law

Set

$$
p=1.
$$

Then

$$
d_1'
<
\min
\left\{
\nu,\,
d+\alpha-1+c,\,
1-\alpha(1-d)
\right\}.
$$

Returning to

$$
\kappa=2d,
$$

we obtain:

## Theorem 8.1 — Seeded $L^1$ shrinking-threshold amplification law

Every

$$
\boxed{
\kappa'
<
\Phi_1(\kappa;\alpha,\nu,c)
}
$$

is admissible, where

$$
\boxed{
\Phi_1
=
\min
\left\{
2\nu,\,
\kappa+2c+2\alpha-2,\,
2-2\alpha+\alpha\kappa
\right\}.
}
$$

Create:

```text
B-RH-066
SEEDED_L1_SHRINKING_THRESHOLD_PESC_AMPLIFICATION_LAW
CERTIFIED
```

---

# 9. Exact strict-amplifier gate

We ask when

$$
\Phi_1>\kappa.
$$

The three inequalities are

$$
2\nu>\kappa,
$$

$$
\kappa+2c+2\alpha-2>\kappa,
$$

and

$$
2-2\alpha+\alpha\kappa>\kappa.
$$

For

$$
\alpha<1,
$$

the last is automatic:

$$
2-2\alpha+\alpha\kappa-\kappa
=
(1-\alpha)(2-\kappa)
>0.
$$

Thus:

## Corollary 9.1 — Minimal deterministic exceptional-set gate

Strict amplification occurs exactly when

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>1-\alpha,
\qquad
\alpha<1.
}
$$

Compared with Paper 56,

$$
c>2(1-\alpha)
$$

has been improved to

$$
\boxed{
c>1-\alpha.
}
$$

The boundary threshold

$$
\nu>\kappa/2
$$

cannot be weakened.

---

# 10. Near-macroscopic formulation

Write

$$
\boxed{
\alpha=1-\tau,
\qquad
\tau>0.
}
$$

Then

$$
\Phi_1
=
\min
\left\{
2\nu,\,
\kappa+2(c-\tau),\,
\kappa+(2-\kappa)\tau
\right\}.
$$

Thus the exponent gain

$$
\eta=\kappa'-\kappa
$$

may be any fixed number satisfying

$$
\boxed{
\eta
<
\min
\left\{
2\nu-\kappa,\,
2(c-\tau),\,
(2-\kappa)\tau
\right\}.
}
$$

The minimal gate becomes

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>\tau.
}
$$

This is the strengthened direct frontier.

---

# 11. Optimal use of an exceptional exponent

Assume

$$
2\nu
$$

is not the active bottleneck.

For fixed $c$, maximize

$$
\min
\left\{
\kappa+2c+2\alpha-2,\,
2-2\alpha+\alpha\kappa
\right\}.
$$

Balance the two terms:

$$
\kappa+2c+2\alpha-2
=
2-2\alpha+\alpha\kappa.
$$

This gives

$$
\boxed{
\alpha_*
=
1-
\frac{2c}{4-\kappa}.
}
$$

Equivalently,

$$
\boxed{
\tau_*
=
\frac{2c}{4-\kappa}.
}
$$

The optimized output exponent is

$$
\boxed{
\kappa_*
'
=
\kappa
+
\frac{
2c(2-\kappa)
}{
4-\kappa
}.
}
$$

Thus the optimized one-step gain is

$$
\boxed{
\eta_*
=
\frac{
2c(2-\kappa)
}{
4-\kappa
}.
}
$$

This is exactly twice the modest- $c$ exceptional-set gain produced by the $L^2$ conversion in Paper 56.

To keep the threshold term non-bottlenecking, it suffices that

$$
\boxed{
\nu
\ge
\frac{\kappa}{2}
+
\frac{
c(2-\kappa)
}{
4-\kappa
}.
}
$$

If the formula attempts to produce $\kappa'>1$, the assumptions are themselves incompatible with the known critical-line zeros; in applications one stops at any fixed $\kappa'<1$.

---

# 12. General $L^p$ optimization

For completeness, if $p\ge1$ is fixed and the threshold is not active, balance

$$
d+\alpha-1+\frac{c}{p}
$$

with

$$
1-\alpha(1-d).
$$

This gives

$$
\boxed{
\alpha_{p,*}
=
1-
\frac{
2c
}{
p(4-\kappa)
}.
}
$$

The PESC exponent gain is

$$
\boxed{
\eta_{p,*}
=
\frac{
2c(2-\kappa)
}{
p(4-\kappa)
}.
}
$$

This decreases exactly like $1/p$.

Thus the optimality of $p=1$ is quantitative, not merely qualitative.

---

# 13. Comparison with Paper 56

Paper 56 used:

```text
exceptional set
-> lag L2 energy
-> MLEPG
-> seeded residue-chain L2
-> PESC
```

The present paper uses:

```text
exceptional set
-> lag Lp moment
-> residue-chain Lp directly
-> global PNT-error Lp
-> Mellin analyticity
-> zero strip
-> PESC
```

The direct Mellin route avoids the extra $L^2$ cost of squaring the exceptional-set pointwise envelope.

Therefore Paper 56 remains correct but is not optimal as an exceptional-set exponent converter.

The improved canonical direct target should use the $L^1$ bridge.

---

# 14. F-RH-017 v2

Replace the old preferred direct target by the stronger version:

```text
F-RH-017-v2
SEEDED_SUPERCRITICAL_SHRINKING_THRESHOLD_EXCEPTIONAL_SET
```

At scale

$$
\boxed{
H=N^{1-\tau},
}
$$

prove

$$
\boxed{
\#\left\{
n\in[N,2N]:
|\psi(n+H)-\psi(n)-H|
>
HN^{-\nu}
\right\}
\ll
N^{1-c}
}
$$

with

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>\tau.
}
$$

Then a strict fixed PESC exponent improvement follows.

This is the cheapest currently certified exceptional-set amplifier.

---

# 15. Audit of the Gafni-Tao fixed-threshold proof

Gafni and Tao define their exceptional set using a fixed relative threshold

$$
\delta>0.
$$

In the proof they explicitly:

1. fix $\delta$ ;
2. choose a natural number $J$ sufficiently large depending on $\delta,\theta,\varepsilon$ ;
3. hold $\delta,J,\theta,\varepsilon$ fixed as $X\to\infty$.

Their explicit-formula truncation height is

$$
T
=
J(\log^2X)X^{1-\theta},
$$

and the truncation error is

$$
O\left(
\frac{X^\theta}{J}
\right).
$$

To compare this with a polynomial threshold

$$
\delta_X
=
X^{-\nu},
$$

one would need

$$
\boxed{
J
\gg
X^\nu
}
$$

already at the truncation step.

Thus the published theorem cannot be used by the formal substitution

$$
\delta=X^{-\nu}.
$$

Its asymptotic notation permits constants depending on fixed $\delta$ and $J$.

This is a theorem-scope statement, not a criticism of the result.

---

# 16. Fixed- $H$ removes one technical polynomial cost, but not the wall

The Gafni-Tao proof also subdivides

$$
[X,2X]
$$

into

$$
O_\delta(1)
$$

multiplicative intervals in order to replace the varying length

$$
x^\theta
$$

by a nearly fixed multiplicative increment.

For the CSM_RH frontier we may instead formulate the interval length as a fixed dyadic

$$
H=N^\alpha.
$$

This removes the need for that subdivision and therefore avoids a polynomial covering factor when $\delta$ shrinks.

This is a useful technical simplification.

However it does not resolve the seeded boundary threshold.

The explicit formula still requires a polynomial height

$$
T
\gtrsim
N^{1-\alpha+\nu}.
$$

More importantly, a zero on

$$
\beta=1-\kappa/2
$$

contributes relative size

$$
N^{-\kappa/2}.
$$

No finite positive moment argument can prove a density-small exceptional set below that amplitude while the boundary zero remains admissible.

---

# 17. Polynomial-threshold $L^2$ packet exponent

For comparison with the current exceptional-set technology, take a narrow zero packet around real part

$$
\sigma
$$

and let

$$
q
=
1-\alpha+\nu
$$

be the minimal explicit-formula height exponent.

The standard $L^2$ zero-packet estimate has average-square exponent

$$
2\alpha+2\sigma-2
+
qA(\sigma)(1-\sigma).
$$

Markov at threshold

$$
N^{\alpha-\nu}
$$

gives exceptional-measure exponent

$$
\boxed{
\mu_{2,\sigma}^{\rm poly}
=
1
+
2
\left(
\nu-(1-\sigma)
\right)
+
qA(\sigma)(1-\sigma).
}
$$

At the seed boundary

$$
1-\sigma
=
\frac{\kappa}{2},
$$

if

$$
\nu>\frac{\kappa}{2},
$$

then

$$
\boxed{
\mu_{2,\sigma}^{\rm poly}>1
}
$$

even before any positive zero-density cost is used.

Thus $L^2$ Markov cannot cross the boundary.

---

# 18. Polynomial-threshold $L^4$ packet exponent

Similarly the standard fourth-moment estimate gives

$$
\boxed{
\mu_{4,\sigma}^{\rm poly}
=
1
+
4
\left(
\nu-(1-\sigma)
\right)
+
qA^*(\sigma)(1-\sigma).
}
$$

At the seed boundary and supercritical threshold,

$$
\boxed{
\mu_{4,\sigma}^{\rm poly}>1.
}
$$

The same baseline obstruction occurs at every finite even moment:

$$
\boxed{
1
+
2r
\left(
\nu-\frac{\kappa}{2}
\right)
}
$$

before nonnegative density / additive-energy costs.

Therefore the failure of direct polynomial-threshold uniformization is structural, not merely caused by the fixed- $\delta$ quantifiers in the published theorem.

This refines Paper 56's moment barrier using the current Gafni-Tao parameter ledger.

---

# 19. Current technology verdict

Current zero-density and additive-zero-energy technology is highly effective for:

$$
\boxed{
\nu<\frac{\kappa}{2}
}
$$

after a seed strip is present, because the boundary packet then lies below the threshold.

It cannot, through a standard finite positive moment + Markov argument, enter

$$
\boxed{
\nu>\frac{\kappa}{2}.
}
$$

But the new $L^1$ deterministic bridge substantially lowers the amount of exceptional-set rarity required once a supercritical arithmetic theorem is found.

This is the exact division of labor:

```text
analytic seed:
moves the right edge to 1-kappa/2

current density/moment technology:
controls subcritical thresholds

new arithmetic theorem:
must cross nu=kappa/2

L1 residue-chain bridge:
converts even modest c>tau into a fixed strip gain
```

---

# 20. New minimal arithmetic target

Choose a small fixed

$$
\tau>0
$$

and put

$$
H=N^{1-\tau}.
$$

The minimal direct target is now:

$$
\boxed{
\#\left\{
n\in[N,2N]:
|U_H(n)|
>
HN^{-\kappa/2-\varepsilon}
\right\}
\ll
N^{1-c}
}
$$

for some fixed

$$
\varepsilon>0,
\qquad
c>\tau.
$$

Then Theorem 10.1 gives the explicit exponent gain

$$
\boxed{
\eta
<
\min
\left\{
2\varepsilon,\,
2(c-\tau),\,
(2-\kappa)\tau
\right\}.
}
$$

This is the sharpest currently certified direct Campaign-46 target.

---

# 21. State transition

Advance the candidate state from

$$
v1.49
$$

to

$$
v1.50.
$$

Add:

```text
B-RH-062
SEEDED_RESIDUE_CHAIN_LP_INEQUALITY
CERTIFIED
```

Add:

```text
B-RH-063
SEEDED_EXCEPTIONAL_SET_TO_GLOBAL_LP_PNT_ERROR_GAIN
CERTIFIED
```

Add:

```text
B-RH-064
SEEDED_LP_EXCEPTIONAL_SET_TO_ZERO_STRIP_AND_PESC_AMPLIFICATION
CERTIFIED
```

Add:

```text
B-RH-065
L1_IS_OPTIMAL_SEEDED_EXCEPTIONAL_SET_RESIDUE_CHAIN_EXPONENT_CONVERTER
CERTIFIED
```

Add:

```text
B-RH-066
SEEDED_L1_SHRINKING_THRESHOLD_PESC_AMPLIFICATION_LAW
CERTIFIED
```

Update preferred frontier:

```text
F-RH-017-v2
nu > kappa/2
c > 1-alpha
```

No RH certificate is created.

---

# 22. Conclusion

The exceptional-set route has become cheaper.

The earlier $L^2$ conversion paid the square of the exceptional-set envelope.

The $L^1$ residue-chain / Mellin route pays it only once.

For

$$
H=N^{1-\tau},
$$

the strict exceptional-set gate is now

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>\tau.
}
$$

The threshold wall did not move.

The exception-count wall did.

This matters because any future arithmetic theorem only needs a modest polynomial rarity of supercritical failures, not the stronger rarity previously required.

The current Gafni-Tao machinery cannot simply be parameter-substituted into this regime, and its finite-moment architecture remains critically blocked at the boundary.

Thus the next breakthrough target is as small and explicit as the present chain can make it:

$$
\boxed{
\text{beat the boundary amplitude on almost all }
N^{1-\tau}\text{-intervals, with only }N^{1-c}
\text{ exceptions and }c>\tau.
}
$$
