# CSM_RH Paper 54

## Seeded MLEPG Amplification, the Optimal Exponent Map, and the Critical-Locking No-Free-Bootstrap Barrier

**Project:** CSM_RH  
**Paper:** 54  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 45 — `PESC_EXPONENT_AMPLIFICATION_OR_MLEPG_BOOTSTRAP`  
**Track:** EA1–EA4  
**Status:** SEEDED AMPLIFICATION LAW CERTIFIED / ARITHMETIC SEED AND AMPLIFIER THEOREMS OPEN  
**Canonical entry state:** v1.44 / Paper 53 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 53 proved that the PESC exponent has an exact zero-strip meaning:

$$
\operatorname{PESC}(\kappa)
\Longrightarrow
\frac{\kappa}{2}
\le
\Re\rho
\le
1-\frac{\kappa}{2},
$$

and that

$$
\operatorname{PESC}(1)
\Longleftrightarrow
\mathrm{RH}
$$

at the exponent resolution used in CSM_RH.

This paper reopens the secondary frontier F-RH-016, Mesoscopic Lag-Energy Power Gain (MLEPG), and asks whether it can strictly amplify a known PESC exponent.

The answer is precise.

Let

$$
A(n)=\psi(n)-n
$$

and

$$
\mathcal S_\Lambda(N,H)
=
\sum_{0\le x<2N-H}
|A(x+H)-A(x)|^2.
$$

Assume PESC $(\kappa)$:

$$
\sum_{n\le X}|A(n)|^2
\ll
X^{3-\kappa+o(1)}.
$$

At the mesoscopic scale

$$
H=N^\alpha,
\qquad
0<\alpha<1,
$$

assume MLEPG $(\alpha,\delta)$:

$$
\mathcal S_\Lambda(N,H)
\ll
NH(\log N)^{O(1)}
+
NH^2N^{-\delta+o(1)}.
$$

Reusing the seed PESC estimate in the initial residue class of the residue-chain theorem improves the old anchor term. One obtains

$$
\boxed{
\sum_{n\le2N}|A(n)|^2
\ll
N^{3-\alpha+o(1)}
+
N^{3-\delta+o(1)}
+
N^{1+\alpha(2-\kappa)+o(1)}.
}
$$

Therefore the new PESC exponent may be any

$$
\boxed{
\kappa'
<
\Phi(\kappa;\alpha,\delta)
:=
\min
\left\{
\alpha,
\delta,
2-\alpha(2-\kappa)
\right\}.
}
$$

This is the seeded MLEPG amplification law.

Since

$$
2-\alpha(2-\kappa)>\kappa
$$

for every $\alpha<1$, strict amplification occurs exactly when

$$
\boxed{
\alpha>\kappa
\qquad\text{and}\qquad
\delta>\kappa.
}
$$

Thus MLEPG is capable of being an exponent amplifier, but only if it supplies a lag exponent strictly stronger than the already known global exponent.

If the MLEPG exponent is not the bottleneck, the optimal scale solves

$$
\alpha
=
2-\alpha(2-\kappa),
$$

giving

$$
\boxed{
\Phi_*(\kappa)
=
\frac{2}{3-\kappa}.
}
$$

For every $0<\kappa<1$,

$$
\Phi_*(\kappa)>\kappa.
$$

The natural Selberg-variance scale corresponds to MLEPG with

$$
\delta=\alpha.
$$

Thus a natural-order lag-energy theorem at

$$
\alpha=\frac{2}{3-\kappa}
$$

would realize the optimal one-step amplification.

Iterating

$$
\kappa_{j+1}
=
\frac{2}{3-\kappa_j}
$$

gives

$$
1-\kappa_j
=
\frac{1}{
2^j
\left(
1+\dfrac{1}{1-\kappa_0}
\right)
-1
},
$$

so $\kappa_j\to1$ geometrically. If one had a theorem that supplied the required natural MLEPG estimate at every seeded stage, then any positive fixed-power seed would bootstrap to the critical line and hence RH.

No such arithmetic theorem is proved.

Indeed, PESC itself cannot generate the required inequality deterministically. The model sequence

$$
u_n=n^{1-\kappa/2}
$$

satisfies

$$
\sum_{n\le N}|u_n|^2
\asymp
N^{3-\kappa}
$$

but for every fixed $0<\alpha<1$,

$$
\sum_{n\asymp N}
|u_{n+N^\alpha}-u_n|^2
\asymp
N^{1+2\alpha-\kappa}.
$$

Thus its mesoscopic lag exponent is exactly $\delta=\kappa$. It fails every MLEPG $(\alpha,\delta)$ with

$$
\alpha>\kappa,
\qquad
\delta>\kappa.
$$

This critical power-law model proves that no purely deterministic implication from PESC $(\kappa)$ can create the strict lag gain required by the amplifier.

The same phenomenon appears in the dyadic contraction language of Papers 21–22. A PESC-saturating power-law mode has asymptotically scale-invariant normalized lag energy and therefore locks the dyadic contraction ratio near $1$. To amplify, the prime sequence must exhibit genuine arithmetic decorrelation beyond this critical-locking model.

Campaign 45 is therefore reduced to a sharp new frontier:

$$
\boxed{
\text{produce lag decorrelation strong enough to make }
\delta_{\rm lag}>\kappa.
}
$$

The current Guth–Maynard short-interval advances improve range and zero-density exponents but retain subpower error precision, so they do not presently supply the required fixed-power seed or amplifier.

No RH theorem is claimed.

---

# 1. Entry state from Paper 53

Paper 53 established the exponent-level equivalence

$$
\operatorname{PESC}(\kappa)
\Longleftrightarrow
\int_N^{2N}
|\psi(x)-x|^2\,dx
\ll
N^{3-\kappa+o(1)}
$$

for fixed

$$
0<\kappa\le1.
$$

It also proved

$$
\operatorname{PESC}(\kappa)
\Longrightarrow
\zeta(s)\ne0
\quad
\text{for }
\Re s>
1-\frac{\kappa}{2}.
$$

At $\kappa=1$ this becomes RH-equivalent.

Thus a future proof strategy based on a subendpoint fixed power must contain an amplification mechanism.

The candidate secondary frontier is F-RH-016:

```text
MESOSCOPIC_LAG_ENERGY_POWER_GAIN
MLEPG
```

Papers 17 and 22 certified its original deterministic bridge.

The present paper audits that bridge again with the existing PESC exponent reused as a seed.

---

# 2. MLEPG and the residue-chain bridge

Let

$$
A(n)=\psi(n)-n.
$$

For an integer lag $H$ define

$$
\boxed{
\mathcal S_\Lambda(N,H)
=
\sum_{0\le x<2N-H}
|A(x+H)-A(x)|^2.
}
$$

Paper 17's residue-chain theorem gives, up to absolute constants,

$$
\boxed{
\sum_{n\le2N}|A(n)|^2
\ll
\frac{N}{H}
\sum_{r<H}|A(r)|^2
+
\left(
\frac{N}{H}
\right)^2
\mathcal S_\Lambda(N,H).
}
$$

The old bridge estimated the first term only by Chebyshev:

$$
\sum_{r<H}|A(r)|^2\ll H^3.
$$

This produced the old anchor loss

$$
NH^2.
$$

Once PESC $(\kappa)$ is already known, this is no longer the correct anchor estimate.

---

# 3. Seeded anchor improvement

Assume PESC $(\kappa)$ globally at all sufficiently large dyadic scales.

Then for every $\varepsilon>0$,

$$
\sum_{X\le n<2X}|A(n)|^2
\ll_\varepsilon
X^{3-\kappa+\varepsilon}.
$$

Cover

$$
1\le n<H
$$

by dyadic intervals.

The resulting geometric sum gives

$$
\boxed{
\sum_{r<H}|A(r)|^2
\ll
H^{3-\kappa+o(1)}.
}
$$

Therefore the residue-chain anchor becomes

$$
\boxed{
\frac{N}{H}
\sum_{r<H}|A(r)|^2
\ll
N H^{2-\kappa+o(1)}.
}
$$

At

$$
H=N^\alpha,
$$

this is

$$
\boxed{
N^{1+\alpha(2-\kappa)+o(1)}.
}
$$

Relative to the global $N^3$ scale, its exponent gain is

$$
\boxed{
\kappa_{\rm anchor}
=
2-\alpha(2-\kappa).
}
$$

For every

$$
0<\kappa<1,
\qquad
0<\alpha<1,
$$

$$
\kappa_{\rm anchor}-\kappa
=
(1-\alpha)(2-\kappa)
>
0.
$$

Thus the seeded anchor is automatically stronger than the seed exponent at every genuinely mesoscopic scale.

This removes the old artificial $2/3$ ceiling from the bootstrap problem.

---

# 4. Seeded MLEPG amplification theorem

Recall MLEPG $(\alpha,\delta)$:

$$
\boxed{
\mathcal S_\Lambda(N,N^\alpha)
\ll
N^{1+\alpha+o(1)}
+
N^{1+2\alpha-\delta+o(1)}.
}
$$

Insert this and the seeded anchor into the residue-chain inequality.

The diagonal term gives

$$
\left(
\frac{N}{H}
\right)^2
NH
=
\frac{N^3}{H}
=
N^{3-\alpha}.
$$

The lag-gain term gives

$$
\left(
\frac{N}{H}
\right)^2
NH^2N^{-\delta}
=
N^{3-\delta}.
$$

The seeded anchor gives

$$
N^{1+\alpha(2-\kappa)}.
$$

Hence:

## Theorem 4.1 — Seeded MLEPG amplification law

Assume PESC $(\kappa)$ and MLEPG $(\alpha,\delta)$ with

$$
0<\kappa<1,
\qquad
0<\alpha<1,
\qquad
\delta>0.
$$

Then for every fixed

$$
\kappa'
<
\boxed{
\Phi(\kappa;\alpha,\delta)
=
\min
\left\{
\alpha,
\delta,
2-\alpha(2-\kappa)
\right\},
}
$$

PESC $(\kappa')$ follows.

Create:

```text
B-RH-052
SEEDED_PESC_MLEPG_EXPONENT_AMPLIFICATION_LAW
CERTIFIED
```

This is the central deterministic theorem of Campaign 45.

---

# 5. Exact strict-amplification criterion

We ask when

$$
\Phi(\kappa;\alpha,\delta)>\kappa.
$$

The anchor condition is automatic:

$$
2-\alpha(2-\kappa)>\kappa
$$

if and only if

$$
\alpha<1.
$$

Therefore:

## Corollary 5.1 — MLEPG strict-amplification gate

For

$$
0<\kappa<1
$$

and

$$
0<\alpha<1,
$$

the seeded MLEPG bridge strictly improves the PESC exponent if and only if

$$
\boxed{
\alpha>\kappa
\qquad\text{and}\qquad
\delta>\kappa.
}
$$

This is the exact Campaign 45 amplifier gate.

The scale must lie beyond the current exponent, and the arithmetic lag saving must itself beat the current exponent.

The condition

$$
\delta>\kappa
$$

cannot be supplied by bookkeeping. It is the new arithmetic content.

---

# 6. Optimal one-step exponent map

Suppose the MLEPG exponent $\delta$ is large enough not to be the active restriction.

Then maximize

$$
\min
\left\{
\alpha,
2-\alpha(2-\kappa)
\right\}
$$

over

$$
0<\alpha<1.
$$

The first function increases in $\alpha$.

The second decreases in $\alpha$.

The optimum occurs at their intersection:

$$
\alpha
=
2-\alpha(2-\kappa).
$$

Hence

$$
\alpha(3-\kappa)=2,
$$

so

$$
\boxed{
\alpha_*(\kappa)
=
\frac{2}{3-\kappa}.
}
$$

At this point,

$$
\boxed{
\Phi_*(\kappa)
=
\frac{2}{3-\kappa}.
}
$$

For

$$
0<\kappa<1,
$$

$$
\Phi_*(\kappa)-\kappa
=
\frac{
(1-\kappa)(2-\kappa)
}{
3-\kappa
}
>
0.
$$

Thus:

## Theorem 6.1 — Optimal seeded residue-chain amplification map

If MLEPG is available at

$$
\alpha
=
\frac{2}{3-\kappa}
$$

with

$$
\delta
\ge
\frac{2}{3-\kappa},
$$

then every

$$
\kappa'
<
\boxed{
\frac{2}{3-\kappa}
}
$$

is admissible.

Create:

```text
B-RH-053
OPTIMAL_SEEDED_MLEPG_BOOTSTRAP_MAP_KAPPA_TO_TWO_OVER_THREE_MINUS_KAPPA
CERTIFIED
```

---

# 7. Natural Selberg scale realizes the optimal map

The natural short-interval variance scale is

$$
\mathcal S_\Lambda(N,H)
\asymp
NH
\times
\text{logarithmic factor}.
$$

In MLEPG notation,

$$
NH^2N^{-\delta}
$$

reaches the same power scale as $NH$ when

$$
\boxed{
\delta=\alpha.
}
$$

Thus the natural-order MLEPG theorem is precisely MLEPG $(\alpha,\alpha)$ at exponent resolution.

Choose

$$
\alpha
=
\alpha_*(\kappa)
=
\frac{2}{3-\kappa}.
$$

Then

$$
\delta=\alpha=\Phi_*(\kappa),
$$

and the optimal amplification is attained.

Therefore the ideal Campaign 45 arithmetic theorem is not an exotic super-natural variance estimate.

It is:

> prove natural-order lag energy at the dynamically selected scale  
> $$H=N^{2/(3-\kappa)}$$  
> under hypotheses no stronger than the currently available seed PESC $(\kappa)$.

No such theorem is currently certified.

---

# 8. Exact iteration to the critical line

Define

$$
\boxed{
\kappa_{j+1}
=
\frac{2}{3-\kappa_j}.
}
$$

Let

$$
e_j=1-\kappa_j.
$$

Then

$$
\begin{aligned}
e_{j+1}
&=
1-
\frac{2}{2+e_j}
\\
&=
\frac{e_j}{2+e_j}.
\end{aligned}
$$

Therefore

$$
\boxed{
\frac1{e_{j+1}}
=
2\frac1{e_j}+1.
}
$$

Solving the recurrence gives

$$
\boxed{
\frac1{e_j}
=
2^j
\left(
\frac1{e_0}+1
\right)
-1.
}
$$

Hence

$$
\boxed{
1-\kappa_j
=
\frac1{
2^j
\left(
1+\dfrac1{1-\kappa_0}
\right)
-1
}.
}
$$

Thus

$$
\kappa_j\to1
$$

geometrically.

---

# 9. Bootstrap meta-theorem

The iteration does not itself provide the arithmetic theorem required at each stage.

We therefore separate the deterministic engine from the missing input.

Define the following hypothetical statement.

## Natural MLEPG Bootstrap Hypothesis, NMBH

For every fixed

$$
0<\kappa<1,
$$

PESC $(\kappa)$ implies MLEPG $(\alpha,\delta)$ at

$$
\boxed{
\alpha=\delta=\frac{2}{3-\kappa}.
}
$$

This is not assumed elsewhere and is not proved here.

Then:

## Theorem 9.1 — Conditional iterative bootstrap meta-theorem

If:

1. PESC $(\kappa_0)$ is proved for one fixed $\kappa_0>0$ ; and
2. NMBH holds for every seeded exponent generated by the recurrence;

then PESC $(\kappa_j)$ holds for all $j$, where

$$
\kappa_j\to1.
$$

Paper 53 then implies RH.

### Proof

Apply Theorem 6.1 inductively.

For any nontrivial zero with

$$
\beta>\frac12,
$$

choose $j$ sufficiently large that

$$
1-\frac{\kappa_j}{2}<\beta.
$$

Paper 53 excludes that zero.

Functional-equation symmetry excludes zeros to the left of the critical line.

Therefore every nontrivial zero lies on

$$
\Re s=\frac12.
$$

$$
\Box
$$

This is a bootstrap architecture, not a proof of its arithmetic hypothesis.

---

# 10. PESC alone cannot create the required lag exponent

The seeded amplification law requires

$$
\delta>\kappa.
$$

Can PESC $(\kappa)$ itself imply this merely by deterministic inequalities?

No.

First, the generic translation estimate gives

$$
\begin{aligned}
\mathcal S_\Lambda(N,H)
&=
\sum_x
|A(x+H)-A(x)|^2
\\
&\le
2\sum_x|A(x+H)|^2
+
2\sum_x|A(x)|^2.
\end{aligned}
$$

Thus PESC $(\kappa)$ gives only

$$
\boxed{
\mathcal S_\Lambda(N,H)
\ll
N^{3-\kappa+o(1)}.
}
$$

At

$$
H=N^\alpha,
$$

rewriting this in the MLEPG remainder scale

$$
NH^2N^{-\delta}
$$

gives at best

$$
\boxed{
\delta_{\rm det}
=
\kappa+2\alpha-2.
}
$$

This is positive only when

$$
\alpha>1-\frac{\kappa}{2}.
$$

But for every $\alpha<1$,

$$
\delta_{\rm det}<\kappa.
$$

Therefore deterministic translation never crosses the amplifier gate.

It can preserve the seed exponent arbitrarily closely as $\alpha\to1$, but cannot improve it.

---

# 11. A sharp critical-locking countermodel

The preceding failure is not merely weakness of the triangle inequality.

Fix

$$
0<\kappa<1
$$

and define the model sequence

$$
\boxed{
u_n=n^{1-\kappa/2}.
}
$$

Then

$$
|u_n|^2
=
n^{2-\kappa},
$$

so

$$
\boxed{
\sum_{n\le N}|u_n|^2
\asymp
N^{3-\kappa}.
}
$$

Thus the sequence exactly saturates the PESC $(\kappa)$ global energy scale.

Let

$$
H=N^\alpha,
\qquad
0<\alpha<1.
$$

For

$$
N\le n\le2N
$$

and large $N$, the mean value theorem gives

$$
u_{n+H}-u_n
=
\left(
1-\frac{\kappa}{2}
\right)
H
\xi_{n,H}^{-\kappa/2}
$$

for some

$$
n<\xi_{n,H}<n+H.
$$

Since

$$
\xi_{n,H}\asymp N,
$$

$$
|u_{n+H}-u_n|^2
\asymp
H^2N^{-\kappa}.
$$

Summing over $\asymp N$ values of $n$ gives

$$
\boxed{
\sum_{N\le n<2N}
|u_{n+H}-u_n|^2
\asymp
NH^2N^{-\kappa}.
}
$$

Therefore its lag exponent is exactly

$$
\boxed{
\delta_{\rm model}=\kappa.
}
$$

If

$$
\alpha>\kappa
$$

and

$$
\delta>\kappa,
$$

the MLEPG diagonal term

$$
NH=N^{1+\alpha}
$$

is smaller than the model lag energy by

$$
N^{\alpha-\kappa},
$$

while the MLEPG remainder

$$
NH^2N^{-\delta}
$$

is smaller by

$$
N^{\delta-\kappa}.
$$

Hence this PESC-saturating model violates every strict-amplifier MLEPG estimate.

## Theorem 11.1 — Critical-locking no-free-bootstrap barrier

There is no universal deterministic implication

$$
\operatorname{PESC}(\kappa)
\Longrightarrow
\operatorname{MLEPG}(\alpha,\delta)
$$

in the strict-amplifier regime

$$
\alpha>\kappa,
\qquad
\delta>\kappa.
$$

Create:

```text
O-RH-132
PESC_SATURATING_POWER_LAW_CRITICAL_LOCKING_BLOCKS_DETERMINISTIC_MLEPG_AMPLIFICATION
CERTIFIED
```

This proves that the missing amplifier must use arithmetic structure specific to the primes.

---

# 12. Connection to dyadic contraction mass

Papers 21–22 defined

$$
R_N(H)
=
\frac{
\mathcal S_\Lambda(N,H)
}{
NH^2
}
$$

and the exact dyadic ratio

$$
q_N(H)
=
\frac{
R_N(2H)
}{
R_N(H)
}.
$$

The cumulative contraction mass is

$$
G_N(J)
=
\sum_{j<J}
-\log q_N(H_j).
$$

The power-law countermodel of Section 11 has

$$
R_N(H)
\asymp
N^{-\kappa}
$$

uniformly over every polynomial lag scale

$$
H=o(N).
$$

Therefore

$$
q_N(H)\to1
$$

at exponent resolution.

This is exactly critical locking.

A genuine arithmetic amplifier must force the prime sequence away from this model by generating additional contraction mass.

If at a terminal scale

$$
H=N^\alpha
$$

one proves

$$
R_N(H)
\ll
N^{-\delta_{\rm sc}+o(1)},
$$

then

$$
\mathcal S_\Lambda(N,H)
\ll
NH^2N^{-\delta_{\rm sc}+o(1)}.
$$

The seeded residue-chain argument gives

$$
\boxed{
\kappa'
<
\min
\left\{
\delta_{\rm sc},
2-\alpha(2-\kappa)
\right\}.
}
$$

Thus a sufficient contraction-mass amplifier criterion is

$$
\boxed{
\delta_{\rm sc}>\kappa.
}
$$

Equivalently, after initial-scale normalization,

$$
\boxed{
G_N(J)
>
\kappa\log N
+
o(\log N).
}
$$

Create:

```text
B-RH-054
SEEDED_DYADIC_CONTRACTION_MASS_AMPLIFIER_GATE
CERTIFIED
```

This is the contraction-language version of the MLEPG condition $\delta>\kappa$.

---

# 13. Natural contraction calibration

The conjectural short-interval variance scale is approximately

$$
\mathcal S_\Lambda(N,H)
\asymp
NH\log(N/H).
$$

Therefore

$$
R_N(H)
\asymp
\frac{\log(N/H)}{H}.
$$

At adjacent dyadic scales,

$$
\frac{R_N(2H)}{R_N(H)}
\sim
\frac12
\frac{
\log(N/2H)
}{
\log(N/H)
}.
$$

Away from the terminal scale this is close to

$$
\frac12.
$$

If such a contraction persisted across essentially all dyadic scales from subpolynomial size to

$$
H=N^\alpha,
$$

the cumulative contraction mass would be approximately

$$
\alpha\log N,
$$

and therefore

$$
\delta_{\rm sc}\approx\alpha.
$$

This is exactly the natural MLEPG exponent

$$
\delta=\alpha.
$$

Thus the optimal bootstrap map is not asking for a contraction stronger than the expected prime variance.

It is asking for enough of that natural decorrelation to be proved at fixed-power precision.

---

# 14. Seed gate and amplifier gate are distinct

Campaign 45 now has two logically independent arithmetic obligations.

## Gate S — fixed-power seed

Produce any theorem implying

$$
\operatorname{PESC}(\kappa_0)
$$

for some fixed

$$
\kappa_0>0.
$$

A single fixed-power MLEPG theorem, shrinking-threshold exceptional-set theorem, or sufficient contraction-mass theorem would do this through the already certified unseeded bridges.

No such theorem is currently certified.

## Gate A — exponent amplifier

Given PESC $(\kappa)$, prove an arithmetic lag theorem with

$$
\boxed{
\delta_{\rm lag}>\kappa.
}
$$

At natural strength, use the moving scale

$$
\alpha_*(\kappa)
=
\frac{2}{3-\kappa}.
$$

The two gates should not be conflated.

A theorem that creates only one small fixed exponent but cannot be repeated is a seed, not an amplifier.

---

# 15. Current external technology calibration

The 2026 Annals paper of Guth and Maynard proves the zero-density estimate

$$
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}
$$

and obtains pointwise prime asymptotics in intervals of length

$$
x^{17/30+o(1)}
$$

and almost-all asymptotics down to

$$
X^{2/15+o(1)}.
$$

The published error terms in the short-interval corollaries are of subpower exponential type, such as

$$
\exp(-c\sqrt{\log X}),
$$

rather than a relative error

$$
X^{-\eta}
$$

with fixed $\eta>0$.

Thus these major range improvements do not presently cross Gate S or Gate A.

This is consistent with Papers 37–38.

The classical Goldston–Montgomery and later short-interval variance literature connects natural-order prime variance to pair-correlation information about zeta zeros. This calibrates the strength of MLEPG $(\alpha,\alpha)$: it is a genuinely deep arithmetic statement, not a deterministic consequence of a global PNT mean square.

---

# 16. EA1 verdict

The Campaign 45 question was:

```text
EA1
DOES_F_RH_016_IMPLY_A_STRICT_PESC_EXPONENT_IMPROVEMENT?
```

Answer:

```text
YES, CONDITIONALLY ON ITS PARAMETERS.

Given seed PESC(kappa):

MLEPG(alpha,delta)
strictly amplifies iff

  alpha > kappa
  delta > kappa
  alpha < 1.

The seeded output exponent is

  min(alpha, delta, 2-alpha(2-kappa)).
```

But:

```text
PESC(kappa) alone does not imply delta > kappa.
```

Therefore close EA1 as:

```text
CLOSED_AS_SEEDED_MLEPG_IS_A_TRUE_AMPLIFIER_EXACTLY_BEYOND_THE_CRITICAL_LOCKING_EXPONENT
```

---

# 17. EA2 verdict: optimal map

Close EA2 as:

```text
CLOSED_AS_OPTIMAL_NATURAL_MLEPG_MAP
```

with

$$
\boxed{
\kappa
\mapsto
\frac{2}{3-\kappa}.
}
$$

The map has the endpoint fixed point

$$
\kappa=1
$$

and approaches it geometrically under iteration.

No arithmetic theorem establishing the required MLEPG family is supplied.

---

# 18. EA3 and EA4 next tasks

The campaign should now stop asking whether an exponent map exists.

It does.

The next question is whether prime arithmetic can satisfy the amplifier inequality.

Open:

```text
EA3
SEEDED_PRINCIPAL_ARC_DELOCKING
```

Target:

prove that PESC $(\kappa)$ plus currently available arithmetic information forces enough spectral escape from the Fejer principal arc to yield

$$
\delta_{\rm lag}>\kappa.
$$

Open:

```text
EA4
UNIFORM_CONTRACTION_MASS_BOOTSTRAP
```

Target:

prove a seeded lower bound

$$
G_N(J)
\ge
(\kappa+\eta_\kappa)\log N
$$

for some

$$
\eta_\kappa>0
$$

at a scale compatible with the optimal map.

Hard rejections:

```text
USE_PESC_TRANSLATION_BOUND_AS_IF_DELTA_GT_KAPPA
CONFUSE_SEED_WITH_AMPLIFIER
REUSE_OLD_UNSEEDED_ANCHOR_2_MINUS_2ALPHA
CLAIM_NATURAL_MLEPG_FROM_ZERO_FREE_STRIP_ALONE
PROMOTE_SUBPOWER_SHORT_INTERVAL_ERROR_TO_FIXED_POWER
ASSUME_PAIR_CORRELATION
ASSUME_RH
HIDE_DELTA_LE_KAPPA_IN_O_ONE
```

---

# 19. Campaign state transition

Advance the candidate state from

$$
v1.44
$$

to

$$
v1.45.
$$

Add:

```text
B-RH-052
SEEDED_PESC_MLEPG_EXPONENT_AMPLIFICATION_LAW
CERTIFIED
```

Add:

```text
B-RH-053
OPTIMAL_SEEDED_MLEPG_BOOTSTRAP_MAP_KAPPA_TO_TWO_OVER_THREE_MINUS_KAPPA
CERTIFIED
```

Add:

```text
B-RH-054
SEEDED_DYADIC_CONTRACTION_MASS_AMPLIFIER_GATE
CERTIFIED
```

Add:

```text
O-RH-132
PESC_SATURATING_POWER_LAW_CRITICAL_LOCKING_BLOCKS_DETERMINISTIC_MLEPG_AMPLIFICATION
CERTIFIED
```

Campaign 45 state:

```text
EA1 CLOSED
EA2 CLOSED
EA3 OPEN
EA4 OPEN

SEED GATE OPEN
AMPLIFIER ARITHMETIC GATE OPEN
```

No RH certificate is created.

---

# 20. Conclusion

The role of MLEPG is now exact.

It is neither merely another representation of PESC nor an automatic bootstrap theorem.

With a seed exponent $\kappa$, the deterministic bridge is

$$
\boxed{
\kappa'
<
\min
\left\{
\alpha,
\delta,
2-\alpha(2-\kappa)
\right\}.
}
$$

Strict improvement occurs exactly beyond the critical-locking threshold:

$$
\boxed{
\alpha>\kappa,
\qquad
\delta>\kappa.
}
$$

At natural lag-energy strength, the optimal map is

$$
\boxed{
\kappa
\mapsto
\frac{2}{3-\kappa}.
}
$$

Repeated ideal amplification converges geometrically to the RH endpoint.

But the power-law model

$$
u_n=n^{1-\kappa/2}
$$

shows why this amplification cannot be free: a sequence can saturate PESC $(\kappa)$ while remaining perfectly locked at lag exponent $\delta=\kappa$.

Therefore the next theorem must be genuinely arithmetic.

It must prove that the prime-error sequence decorrelates more strongly across mesoscopic scales than the critical power-law mode allowed by the current PESC exponent.

That is the new core of CSM_RH.
