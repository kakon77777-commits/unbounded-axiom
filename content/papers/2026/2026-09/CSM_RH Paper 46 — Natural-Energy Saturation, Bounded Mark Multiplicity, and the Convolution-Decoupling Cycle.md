# CSM_RH Paper 46
## Natural-Energy Saturation, Bounded Mark Multiplicity, and the Convolution-Decoupling Cycle

**Project:** CSM_RH  
**Paper:** 46  
**Version:** 0.1  
**Date:** 2026-09-07  
**Campaign:** 43 — `WEIGHTED_LIOUVILLE_POLYNOMIAL_PHASE_ATTACK`  
**Track:** WL3 — `STRUCTURED_WEIGHT_DECOUPLING`  
**Canonical state transition:** v1.36 to v1.37

---

# 0. Trust boundary

This paper continues directly from CSM_RH Paper 45.

The inherited residual core is

$$
\boxed{
\begin{aligned}
\mathfrak R_{\lambda}(Q,Y)
=
Y
\sum_{h_\star<h\lesssim X^{o(1)}X/Y}
\sum_m
&\frac{r_X(m)r_X(m+h)}{m(m+h)}\\
&\times
\overline{f_Q(m)}f_Q(m+h)
\widehat\Phi\!\left(Y\log(1+h/m)\right),
\end{aligned}
}
$$

where

$$
f_Q(n)=\lambda(n)n^{iQ},
$$

$$
W=X^w,
\qquad
0<w\le\frac{\varepsilon}{1000},
$$

$$
h_\star
=
\frac{X}{Q}
X^{\varepsilon/2-61w/100},
$$

and the admission target remains

$$
\boxed{
|\mathfrak R_{\lambda}(Q,Y)|
\ll
X^{-3w/10+o(1)}.
}
$$

Paper 45 proved an exact factorisation-space Ramaré marking identity and removed the large common-prime and repeated-large-prime branches at the stronger scale

$$
X^{-31w/100+o(1)}.
$$

It also isolated two hard coefficient families:

1. a rough marked affine prime-Liouville branch;
2. a no-large-prime smooth-carrier branch.

WL3 asks whether the exact convolution structure of

$$
r_X
=
(\mu^2 1_{U_1})*\cdots*(\mu^2 1_{U_L})
$$

contains an $L^2$, dispersion, or factor-decoupling reserve large enough to supply a fixed power of $X$.

No claim of RH, no fixed zero-free strip, and no pointwise fixed-power Mertens or Liouville estimate is made.

---

# 1. Factorisation-space notation

As before,

$$
L=\left\lceil\frac{10}{\varepsilon}\right\rceil,
$$

$$
m_i\sim U_i,
\qquad
U_i=X^{1/L+o(1)},
$$

and

$$
\prod_{i=1}^{L}U_i\asymp X.
$$

Define

$$
g_i(n)
=
\mu^2(n)1_{n\sim U_i}.
$$

Then

$$
\boxed{
r_X
=
g_1*\cdots*g_L.
}
$$

The corresponding signed coefficient is

$$
c_X(n)
=
\lambda(n)r_X(n),
$$

and, by Paper 43,

$$
\boxed{
c_X
=
(\mu 1_{U_1})*\cdots*(\mu 1_{U_L}).
}
$$

Define the polynomial prime threshold

$$
\rho_\star
=
\frac{31w}{100},
$$

$$
P_\star
=
X^{\rho_\star}.
$$

Split the structured weight into

$$
\boxed{
r_X^{\mathrm{sm}}(n)
=
r_X(n)1_{P^+(n)<P_\star},
}
$$

and

$$
\boxed{
r_X^{\mathrm{rough}}(n)
=
r_X(n)1_{P^+(n)\ge P_\star}.
}
$$

At exponent resolution the distinction between strict and non-strict endpoint conventions is harmless.

---

# 2. Total mass of the structured weight

For every fixed dyadic interval,

$$
\sum_{m\sim U_i}\mu^2(m)
\asymp
U_i.
$$

Therefore

$$
\boxed{
\sum_n r_X(n)
=
\prod_{i=1}^{L}
\sum_{m_i\sim U_i}\mu^2(m_i)
\asymp
X.
}
$$

The support of $r_X$ lies in a fixed multiplicative enlargement of the dyadic block $n\asymp X$.
Hence the number of possible support integers is

$$
O_L(X).
$$

Cauchy-Schwarz gives

$$
\left(\sum_n r_X(n)\right)^2
\le
O_L(X)
\sum_n r_X(n)^2.
$$

Consequently,

$$
\boxed{
\sum_n r_X(n)^2
\gg_L
X.
}
$$

On the other hand,

$$
r_X(n)
\le
d_L(n),
$$

and the fixed- $L$ divisor second moment gives

$$
\sum_{n\asymp X}d_L(n)^2
\ll_L
X(\log X)^{O_L(1)}.
$$

Thus:

## Theorem 2.1 — Natural $L^2$ scale of the pure-core structured weight

$$
\boxed{
\sum_n r_X(n)^2
=
X^{1+o(1)}.
}
$$

Equivalently,

$$
\boxed{
\|r_X\|_2
=
X^{1/2+o(1)}.
}
$$

For the normalized Dirichlet coefficient

$$
a_X(n)
=
\frac{r_X(n)}{n},
$$

this becomes

$$
\boxed{
\sum_n|a_X(n)|^2
=
X^{-1+o(1)}.
}
$$

Create:

```text
B-RH-025
PURE_CORE_STRUCTURED_WEIGHT_NATURAL_L2_SCALE
CERTIFIED
```

The structured weight is not an $L^2$ -small perturbation.

---

# 3. Smooth carrier has full exponent energy

Paper 45 constructed a fixed integer $K=K(\varepsilon,w)$ and a legal smooth factorisation subfamily for which

$$
P^+(n)<P_\star
$$

and

$$
\sum_n r_X^{\mathrm{sm}}(n)
\gg_{\varepsilon,w}
\frac{X}{(\log X)^{C_{\varepsilon,w}}}.
$$

Since the support still has $O_L(X)$ possible integers,

$$
\left(
\sum_n r_X^{\mathrm{sm}}(n)
\right)^2
\le
O_L(X)
\sum_n
\left(r_X^{\mathrm{sm}}(n)\right)^2.
$$

Hence

## Theorem 3.1 — Smooth-carrier full exponent energy

$$
\boxed{
\sum_n
\left(r_X^{\mathrm{sm}}(n)\right)^2
\gg_{\varepsilon,w}
\frac{X}{(\log X)^{2C_{\varepsilon,w}}}
=
X^{1-o(1)}.
}
$$

The upper bound from Theorem 2.1 gives

$$
\boxed{
\sum_n
\left(r_X^{\mathrm{sm}}(n)\right)^2
=
X^{1+o(1)}
}
$$

at exponent resolution.

Thus the no-large-prime branch cannot be discarded through coefficient sparsity or coefficient energy.

---

# 4. A sign-coherent smooth subweight also has full exponent energy

Let

$$
s_X(n)
$$

count only the legal tuples in the explicit Paper 45 construction in which each factor $m_i$ is a product of exactly $K$ primes from its prescribed small-prime interval.

Every such tuple has

$$
\Omega(m_1\cdots m_L)
=
KL
$$

counted with multiplicity.
Therefore on the support of $s_X$,

$$
\boxed{
\lambda(n)
=
(-1)^{KL}.
}
$$

Also,

$$
0\le s_X(n)\le r_X^{\mathrm{sm}}(n),
$$

and Paper 45 gives

$$
\sum_n s_X(n)
\gg_{\varepsilon,w}
\frac{X}{(\log X)^{C_{\varepsilon,w}}}.
$$

The same Cauchy-Schwarz argument yields

## Theorem 4.1 — Sign-coherent smooth subweight has full exponent energy

$$
\boxed{
\sum_n s_X(n)^2
\gg_{\varepsilon,w}
\frac{X}{(\log X)^{2C_{\varepsilon,w}}}.
}
$$

Therefore any WL3 mechanism that first replaces the Liouville sign by an absolute value, or expects the nonnegative factorisation weight itself to create a fixed-power cancellation, has no coefficient-side power reserve on this explicit subfamily.

This theorem does not assert a nonzero shifted two-point correlation for $s_X$.
It is a method-scope statement about positivity and one-variable coefficient decoupling.

---

# 5. Rough carrier is also not power-sparse

The rough branch admits an elementary full-exponent construction independent of the smooth construction.

Fix one factor position $i$.

Choose a small fixed $\eta>0$.
Take primes

$$
P_\star<p\le(1+\eta)P_\star.
$$

Since

$$
\rho_\star<\frac1L,
$$

we have

$$
\frac{U_i}{p}
=
X^{1/L-\rho_\star+o(1)}
\to\infty.
$$

For each such prime choose a squarefree integer $q_i$ from a fixed relative interval of scale

$$
\frac{U_i}{p}
$$

such that

$$
pq_i\sim U_i
$$

and

$$
p\nmid q_i.
$$

For all $j\ne i$, choose arbitrary squarefree

$$
m_j\sim U_j,
$$

and impose

$$
p\nmid m_j.
$$

The latter condition removes only a negligible proportion because $p\to\infty$.

The prime number theorem on the fixed relative prime interval gives

$$
\#\{p:\ P_\star<p\le(1+\eta)P_\star\}
\asymp
\frac{P_\star}{\log X}.
$$

For each such prime there are

$$
\gg
\frac{U_i}{p}
$$

legal choices of $q_i$ and

$$
\gg
\prod_{j\ne i}U_j
$$

choices for the remaining factors.

Therefore the number of legal tuples in this one-large-prime family is

$$
\gg
\frac{P_\star}{\log X}
\frac{U_i}{P_\star}
\prod_{j\ne i}U_j
=
\frac{X}{\log X}.
$$

Every tuple has

$$
P^+(n)>P_\star
$$

and the selected prime occurs exactly once.

Thus

## Theorem 5.1 — Rough non-repeated carrier has full exponent mass

$$
\boxed{
\sum_n r_X^{\mathrm{rough}}(n)
\gg_{\varepsilon,w}
\frac{X}{\log X}.
}
$$

Consequently,

## Corollary 5.2 — Rough carrier has full exponent energy

$$
\boxed{
\sum_n
\left(r_X^{\mathrm{rough}}(n)\right)^2
\gg_{\varepsilon,w}
\frac{X}{(\log X)^2}
=
X^{1-o(1)}.
}
$$

The rough and smooth branches therefore both survive at full $X$ -exponent in coefficient energy.

Create:

```text
B-RH-026
SMOOTH_AND_ROUGH_CARRIERS_BOTH_HAVE_FULL_EXPONENT_WEIGHT_ENERGY
CERTIFIED
```

---

# 6. Polynomial-prime marking has bounded fibre multiplicity

Let

$$
\mathcal P_\star
=
\{p:\ p>P_\star\}.
$$

For every

$$
n\asymp X,
$$

we have

$$
P_\star^{\Omega_{\mathcal P_\star}(n)}
\le
n
\ll
X.
$$

Hence

$$
\boxed{
\Omega_{\mathcal P_\star}(n)
\le
\frac{\log(CX)}{\log P_\star}
=
\frac1{\rho_\star}
+
o(1).
}
$$

Thus a coefficient at scale $X$ carries only

$$
O_w(1)
$$

prime occurrences above the fixed polynomial threshold.

The exact Paper 45 marking decomposition is

$$
r_X(n)
=
\sum_{p\in\mathcal P_\star}
\sum_{i=1}^{L}
w_{i,p}(n)
$$

on the rough branch, where

$$
w_{i,p}(n)
=
\frac{
r_{X;i,p}^{-}(n/p)
}{
\Omega_{\mathcal P_\star}(n)
}
$$

when the denominator is nonzero.

For fixed $n$, the number of nonzero pairs $(i,p)$ is at most

$$
\boxed{
N_\star
=
L
\left(
\frac1{\rho_\star}+2
\right)
=
O_{\varepsilon,w}(1).
}
$$

Pointwise Cauchy-Schwarz gives

$$
r_X(n)^2
\le
N_\star
\sum_{i,p}
w_{i,p}(n)^2.
$$

Since the $w_{i,p}$ are nonnegative,

$$
\sum_{i,p}
w_{i,p}(n)^2
\le
r_X(n)^2.
$$

Therefore:

## Theorem 6.1 — Marked $L^2$ energy stability

On the rough branch,

$$
\boxed{
\frac1{N_\star}
\sum_n
\left(r_X^{\mathrm{rough}}(n)\right)^2
\le
\sum_{i,p}\sum_n
w_{i,p}(n)^2
\le
\sum_n
\left(r_X^{\mathrm{rough}}(n)\right)^2.
}
$$

The exact polynomial-prime marking decomposition changes the total coefficient energy by at most a constant depending on $\varepsilon$ and $w$.

Create:

```text
B-RH-027
POLYNOMIAL_PRIME_MARKING_BOUNDED_MULTIPLICITY_ENERGY_STABILITY
CERTIFIED
```

This is the $L^2$ counterpart of the prime-harmonic leverage barrier from Paper 45.

---

# 7. Fixed exponent prime bands carry full marked energy

The bounded-multiplicity statement can be strengthened on any genuine polynomial sub-band.

Choose fixed exponents

$$
\rho_\star<\rho_2<\frac1L.
$$

Let

$$
\mathcal P^\dagger
=
\{p:\ X^{\rho_\star}<p\le X^{\rho_2}\}.
$$

Fix a factor position $i$.

For every

$$
p\in\mathcal P^\dagger,
$$

the one-prime-removed weight $r_{X;i,p}^{-}(a)$ has total mass

$$
\sum_a r_{X;i,p}^{-}(a)
\asymp_{\varepsilon,w}
\frac{X}{p}.
$$

Its support has

$$
O_L(X/p)
$$

possible integers.

Hence

$$
\sum_a
\left(r_{X;i,p}^{-}(a)\right)^2
\gg_{\varepsilon,w}
\frac{X}{p}.
$$

Summing over the fixed exponent band and using Mertens' theorem,

$$
\sum_{X^{\rho_\star}<p\le X^{\rho_2}}\frac1p
=
\log\frac{\rho_2}{\rho_\star}+o(1).
$$

Therefore:

## Theorem 7.1 — Polynomial marked band has natural total energy

$$
\boxed{
\sum_{p\in\mathcal P^\dagger}
\sum_a
\left(r_{X;i,p}^{-}(a)\right)^2
\gg_{\varepsilon,w,\rho_2}
X.
}
$$

The corresponding divisor-moment upper bound is

$$
X^{1+o(1)}.
$$

Thus the raw marked family itself carries natural $X$ -scale energy.
There is no hidden $P_\star^{-c}$ coefficient-energy gain after summing over polynomially many prime locations.

---

# 8. The multiplicity-leverage closure

Paper 45 proved the prime-harmonic tradeoff:

$$
\text{fixed polynomial prime threshold}
\Longrightarrow
\text{bounded prime-harmonic mass},
$$

whereas

$$
\text{diverging harmonic mass}
\Longrightarrow
P=X^{o(1)}.
$$

Theorem 6.1 now adds:

$$
\text{fixed polynomial prime threshold}
\Longrightarrow
\text{bounded mark multiplicity}.
$$

Therefore the two natural decoupling resources cannot both grow.

If one keeps

$$
P=X^{\rho}
$$

with fixed

$$
\rho>0,
$$

then:

1. prime-size leverage is polynomial;
2. prime-harmonic mass is $O(1)$ ;
3. mark multiplicity per coefficient is $O(1)$ ;
4. marked $L^2$ energy remains at the natural exponent.

If one lowers the threshold until the number of usable marks or the harmonic mass grows, then

$$
P=X^{o(1)},
$$

and any gain based only on a fixed power of $P$ is

$$
X^{-o(1)}.
$$

Create:

```text
O-RH-117
POLYNOMIAL_PRIME_MARKING_HAS_NO_GROWING_ORTHOGONAL_MULTIPLICITY
CERTIFIED AS MECHANISM-SCOPE BARRIER
```

This closes the possibility that WL2 merely needed an $L^2$ reinterpretation of the same polynomial prime marking.

---

# 9. What a pure coefficient-energy proof would need

Let $B$ denote either the smooth or rough coefficient branch and define

$$
E_B
=
\sum_n r_B(n)^2.
$$

The normalized coefficient is

$$
a_B(n)
=
\frac{r_B(n)}{n}.
$$

Since

$$
n\asymp X,
$$

$$
\sum_n|a_B(n)|^2
\asymp
\frac{E_B}{X^2}.
$$

A generic Dirichlet-polynomial mean-value or large-sieve inequality at length $X$ has coefficient-energy scale

$$
(Y+X)
\sum_n|a_B(n)|^2.
$$

Because

$$
Y\le X^{1+o(1)}
$$

in the present application, this is

$$
\ll
X^{o(1)}
\frac{E_B}{X}.
$$

To obtain the admission target purely from coefficient energy would require

$$
E_B
\ll
X^{1-3w/10+o(1)}.
$$

But Theorems 3.1 and 5.2 give

$$
E_{\mathrm{sm}}
\ge
X^{1-o(1)},
$$

and

$$
E_{\mathrm{rough}}
\ge
X^{1-o(1)}.
$$

Thus no argument whose only quantitative reserve is small coefficient $L^2$ energy can provide the required fixed power.

Create:

```text
O-RH-118
STRUCTURED_WEIGHT_L2_ENERGY_HAS_NO_FIXED_POWER_RESERVE
CERTIFIED AS COEFFICIENT-ENERGY METHOD BARRIER
```

This does not rule out an operator estimate that uses genuine Liouville arithmetic.
It rules out obtaining the target by treating $r_X$ or its marked descendants as unusually low-energy weights.

---

# 10. Exact factor bipartitions

The convolution can be split across any nonempty proper subset of factor positions.

Let

$$
I\sqcup J
=
\{1,\ldots,L\}.
$$

Define

$$
R_I
=
\mathop{*}_{i\in I}g_i,
$$

$$
R_J
=
\mathop{*}_{j\in J}g_j.
$$

Then

$$
r_X
=
R_I*R_J.
$$

For the signed coefficient define

$$
C_I
=
\mathop{*}_{i\in I}
(\mu1_{U_i}),
$$

$$
C_J
=
\mathop{*}_{j\in J}
(\mu1_{U_j}),
$$

so

$$
c_X
=
C_I*C_J.
$$

Let the two product scales be

$$
R
=
\prod_{i\in I}U_i,
$$

$$
S
=
\prod_{j\in J}U_j,
$$

with

$$
RS\asymp X.
$$

Without loss of generality orient the split so that

$$
R\le S.
$$

Then

$$
R\le X^{1/2+o(1)}.
$$

---

# 11. A factor split returns a determinant fibre

Expand a fixed shifted product.

Ignoring the harmless smooth kernel and the $m^{-1}(m+h)^{-1}$ normalization for the moment, the signed correlation contains

$$
\sum_{\substack{
a,a'\sim R\\
b,b'\sim S\\
a'b'-ab=h
}}
C_I(a)C_I(a')
C_J(b)C_J(b').
$$

Thus every factor bipartition returns the determinant incidence equation

$$
\boxed{
a'b'-ab=h.
}
$$

Fix

$$
a,a'\sim R
$$

and let

$$
d=(a,a').
$$

Solutions exist only if

$$
d\mid h.
$$

When they exist, the $(b,b')$ solutions form one affine lattice fibre with step sizes

$$
\frac{a}{d}
\qquad\text{and}\qquad
\frac{a'}{d}.
$$

Because

$$
b,b'\sim S,
$$

the number of solutions on that fibre is

$$
\boxed{
O\left(
1+
\frac{Sd}{R}
\right).
}
$$

Summing over the outer variables gives

$$
\sum_{a,a'\sim R}
\left(
1+\frac{S(a,a')}{R}
\right).
$$

The classical gcd average satisfies

$$
\sum_{a,a'\sim R}(a,a')
\ll
R^2\log R.
$$

Therefore

$$
\boxed{
\#\{
a,a',b,b':
a'b'-ab=h
\}
\ll
R^2
+
RS\log R.
}
$$

Since

$$
R^2\le RS\asymp X,
$$

we obtain

## Theorem 11.1 — Factorisation-bipartition fibre-volume conservation

For every factor bipartition,

$$
\boxed{
\#\{
a,a',b,b':
a'b'-ab=h
\}
\ll
X^{1+o(1)}
}
$$

uniformly in the inherited shift range.

The same bound survives the structured convolution multiplicities because fixed-order divisor weights are $X^{o(1)}$ on this support.

Create:

```text
B-RH-028
FACTORISATION_BIPARTITION_DETERMINANT_FIBRE_VOLUME_CONSERVATION
CERTIFIED
```

This generalizes the one-coordinate determinant fibre already visible in Papers 43–45.

---

# 12. Why the apparent long fibre gives no geometric fixed power

For a generic coprime pair

$$
(a,a')=1,
$$

a single fibre has length approximately

$$
\frac{S}{R}
=
\frac{X}{R^2}.
$$

There are approximately

$$
R^2
$$

outer pairs.

Thus the leading geometric volume is

$$
\boxed{
R^2
\cdot
\frac{X}{R^2}
=
X.
}
$$

The gcd average changes this only by a logarithm.

Hence splitting off a short convolution coordinate does create a long affine parameter, but the number of fibres grows by the reciprocal amount.
At exponent resolution the two effects cancel exactly.

After restoring the normalization

$$
\frac1{m(m+h)}
\asymp
X^{-2},
$$

one fixed shift has absolute geometric scale

$$
X^{-1+o(1)}.
$$

The number of relevant shifts is

$$
X^{o(1)}\frac{X}{Y}.
$$

Multiplying by the outer factor $Y$ returns

$$
X^{o(1)}.
$$

The desired bound is instead

$$
X^{-3w/10+o(1)}.
$$

Thus the absolute-value determinant geometry still lands at the old orthogonality floor.

Create:

```text
O-RH-119
ABSOLUTE_FACTOR_DECOUPLING_RETURNS_ORTHOGONALITY_FLOOR
CERTIFIED AS GEOMETRIC METHOD BARRIER
```

---

# 13. Preserving the signs returns genuine Mobius arithmetic

The signed factor split is not identical to the unsigned count.

For example, splitting off one factor position gives

$$
c_X
=
(\mu1_{U_i})*C_{-i}.
$$

The fixed-shift correlation then contains sums of the form

$$
\sum_{\substack{
a,a'\sim U_i\\
b,b'\sim X/U_i\\
a'b'-ab=h
}}
\mu(a)\mu(a')
C_{-i}(b)C_{-i}(b').
$$

Therefore a successful improvement beyond Theorem 11.1 must exploit cancellation in the exposed Mobius variables or in a higher structured coupling.

If one takes absolute values or applies Cauchy-Schwarz until the Mobius signs disappear, Theorems 2.1–12.1 return the natural energy/incidence scale.

If one keeps the signs, the problem has not been decoupled into a purely weight-theoretic estimate.
It has returned to a short-Mobius or affine-Liouville correlation problem.

Create:

```text
O-RH-120
SIGNED_FACTOR_DECOUPLING_RETURNS_MOBIUS_PARITY_NOT_WEIGHT_SMALLNESS
CERTIFIED AS STRUCTURAL REDUCTION
```

This is not a theorem that all future factor-splitting arguments fail.
It identifies the exact point at which WL3 stops being a structured-weight problem and becomes an arithmetic-cancellation problem again.

---

# 14. Current quantitative literature calibration

The present conclusion is compatible with the strongest nearby unconditional results.

Matomaki and Teravainen use Ramaré extraction to obtain cancellation of the Mobius function in all intervals of length $x^\theta$ for $\theta>0.55$.
The normalized conclusion is qualitative $o(1)$, not a fixed power of the ambient variable.

Helfgott and Radziwill obtain strong expansion for a divisibility-by-primes graph.
Its quantitative resource is the harmonic prime mass

$$
\mathscr L
=
\sum_{p\in\mathbf P}\frac1p,
$$

and the resulting Liouville correlation gain is logarithmic.

Recent quantitative Gowers-uniformity and polynomial-pattern results give arbitrary powers of logarithm for broad Mobius and Liouville polynomial averages.
This is a major strengthening of qualitative cancellation, but it is still not a fixed power of $X$.

The 2026 growing-shift logarithmic Chowla results likewise give power-logarithmic cancellation, not the single-dyadic, structured-weight estimate

$$
X^{-3w/10}
$$

required here.

Accordingly, WL3 does not import any external theorem whose precision is weaker than the Campaign 43 admission ledger.

---

# 15. WL3 required-check audit

## Required check 1 — separate smooth and rough carriers

Completed.

The smooth branch has

$$
E_{\mathrm{sm}}
=
X^{1+o(1)}
$$

at exponent resolution.

The rough branch has

$$
E_{\mathrm{rough}}
=
X^{1+o(1)}
$$

at exponent resolution.

Neither branch is power-negligible by coefficient mass or energy.

## Required check 2 — preserve the exact convolution

Completed.

All energy identities are derived from

$$
r_X
=
g_1*\cdots*g_L
$$

without replacing $r_X$ by a generic coefficient until an explicitly labelled divisor-moment upper bound.

## Required check 3 — audit $L^2$ energy of $r_X$ and marked weights

Completed.

$$
\sum r_X^2
=
X^{1+o(1)}.
$$

Polynomial-prime marking preserves rough-branch energy up to $O_{\varepsilon,w}(1)$.

A fixed polynomial prime sub-band carries natural total marked energy

$$
X^{1+o(1)}.
$$

## Required check 4 — sign-coherent smooth subfamily

Completed.

There is an explicit nonnegative subweight $s_X$ with

$$
\lambda(n)=(-1)^{KL}
$$

on its support and

$$
\sum s_X(n)^2
\ge
X^{1-o(1)}.
$$

Thus positivity or absolute-value decoupling cannot extract a fixed power from the smooth coefficient itself.

## Required check 5 — no external $X$ -scale averaging

Satisfied.

Every estimate remains on the inherited single dyadic $X$ -scale.

## Required check 6 — fixed-power ledger

Satisfied.

All coefficient-energy, mark-multiplicity, and determinant-volume gains are at most constants or logarithms at exponent resolution.

No step promotes

$$
X^{-o(1)}
$$

to

$$
X^{-\delta}.
$$

## Required check 7 — create a new long averaging variable

Audited.

A factor split creates affine fibres of length approximately

$$
X/R^2,
$$

but also approximately $R^2$ outer fibres.
The total geometric volume remains

$$
X^{1+o(1)}.
$$

No fixed-power gain is obtained without using genuine Mobius/Liouville cancellation.

---

# 16. WL3 rejection list

The following routes are rejected inside WL3.

## R1. Treat $r_X$ as $L^2$ -small

Rejected by Theorem 2.1.

## R2. Discard the smooth carrier as sparse

Rejected by Theorems 3.1 and 4.1.

## R3. Assume the rough carrier is sparse after removing common and repeated large primes

Rejected at coefficient-energy level by Theorem 5.1 and Corollary 5.2.

## R4. Expect polynomial-prime marking to create polynomially many orthogonal pieces per coefficient

Rejected by Theorem 6.1.

## R5. Sum the marked pieces and claim a $P_\star^{-c}$ energy gain

Rejected by Theorem 7.1.

## R6. Split one or several convolution factors and count determinant fibres absolutely

Rejected by Theorems 11.1 and 12.1.

## R7. Remove the exposed Mobius signs and still claim the signed problem was solved

Rejected by Section 13.

## R8. Use power-logarithmic literature as a fixed- $X$ -power theorem

Rejected by the admission ledger.

---

# 17. WL3 closure

WL3 has produced a complete coefficient-side and factorisation-side audit.

The exact convolution structure is useful for organizing the residual problem, but it does not contain a hidden fixed-power reserve of any of the following forms:

1. low total $L^2$ energy;
2. power-sparse smooth support;
3. power-sparse rough support;
4. growing orthogonal multiplicity from polynomial-prime marks;
5. absolute determinant-fibre volume reduction.

The only remaining possible gain after a legal factor split must use arithmetic cancellation that survives the full structured coupling.

Thus WL3 closes as

```text
WL3
CLOSED_AS_NATURAL_L2_SATURATION_BOUNDED_MARK_MULTIPLICITY_AND_DETERMINANT_CYCLE_BARRIER
```

Campaign 43 remains active.

No fixed-power theorem is proved.

---

# 18. Campaign 43 continuation

The next live track is WL4:

```text
CROSS_J_PRE_SQUARE_RECOMBINATION
```

This route returns to the exact Heath-Brown identity before componentwise triangle inequalities and before componentwise Type-II squaring.

The Heath-Brown levels carry alternating coefficients

$$
(-1)^{j-1}\binom Lj.
$$

Paper 41 explicitly left open the possibility that cross- $j$ recombination suppresses the pure-Mobius core before componentwise estimation.

WL4 must therefore determine whether the Paper 41 pure-core component is an artifact of estimating each $j$ -level separately or whether it survives any legal pre-square recombination.

Required WL4 checks:

1. reconstruct the relevant Heath-Brown $j$ -levels before componentwise absolute values;
2. identify which dyadic pure-Mobius components at different $j$ have overlapping product support;
3. compute cross- $j$ terms at the translated frequency rather than assuming cancellation from alternating signs;
4. preserve the single dyadic $X$ -scale and the major-arc $(Q,Y)$ geometry;
5. quantify any overlap or cancellation with a fixed $X$ -power ledger;
6. reject cancellation that appears only after replacing unequal dyadic components by identical formal symbols;
7. if recombination reconstructs a simpler Lambda-level object, compare it directly with the root frontier $F$ -RH-010 rather than hiding the recoupling.

---

# 19. State transition

The canonical state advances

```text
CSM_RH v1.36
  ->
CSM_RH v1.37
```

Create:

```text
B-RH-025
PURE_CORE_STRUCTURED_WEIGHT_NATURAL_L2_SCALE
CERTIFIED
```

```text
B-RH-026
SMOOTH_AND_ROUGH_CARRIERS_BOTH_HAVE_FULL_EXPONENT_WEIGHT_ENERGY
CERTIFIED
```

```text
B-RH-027
POLYNOMIAL_PRIME_MARKING_BOUNDED_MULTIPLICITY_ENERGY_STABILITY
CERTIFIED
```

```text
B-RH-028
FACTORISATION_BIPARTITION_DETERMINANT_FIBRE_VOLUME_CONSERVATION
CERTIFIED
```

Create:

```text
O-RH-117
POLYNOMIAL_PRIME_MARKING_HAS_NO_GROWING_ORTHOGONAL_MULTIPLICITY
CERTIFIED AS MECHANISM-SCOPE BARRIER
```

```text
O-RH-118
STRUCTURED_WEIGHT_L2_ENERGY_HAS_NO_FIXED_POWER_RESERVE
CERTIFIED AS COEFFICIENT-ENERGY METHOD BARRIER
```

```text
O-RH-119
ABSOLUTE_FACTOR_DECOUPLING_RETURNS_ORTHOGONALITY_FLOOR
CERTIFIED AS GEOMETRIC METHOD BARRIER
```

```text
O-RH-120
SIGNED_FACTOR_DECOUPLING_RETURNS_MOBIUS_PARITY_NOT_WEIGHT_SMALLNESS
CERTIFIED AS STRUCTURAL REDUCTION
```

Campaign 43:

```text
WL1:
  CLOSED_AS_ARCHIMEDEAN_GAUGE_AND_EVEN_ORDER_LIOUVILLE_BARRIER

WL2:
  CLOSED_AS_EXACT_MARKED_EXTRACTION_WITH_PRIME_HARMONIC_AND_SMOOTH_CARRIER_BARRIERS

WL3:
  CLOSED_AS_NATURAL_L2_SATURATION_BOUNDED_MARK_MULTIPLICITY_AND_DETERMINANT_CYCLE_BARRIER

WL4:
  NEXT

WL5:
  OPEN
```

No root promotion occurs.

$$
\boxed{
\mathrm{RH\_PROVED}
=
\mathrm{false}
}
$$

$$
\boxed{
\mathrm{RH\_DISPROVED}
=
\mathrm{false}
}
$$

$$
\boxed{
\mathrm{GLOBAL\_RH\_CERTIFICATE}
=
\mathrm{false}
}
$$

---

# 20. References and external calibration

1. K. Matomaki and J. Teravainen, *On the Mobius function in all short intervals*, J. Eur. Math. Soc. 25 (2023), 1207-1225, arXiv:1911.09076. Ramaré prime extraction produces a strong structural factorisation, while the normalized short-interval conclusion is qualitative rather than a fixed power of the ambient scale.

2. H. A. Helfgott and M. Radziwill, *Expansion, divisibility and parity*, arXiv:2103.06853. The prime-divisibility graph is controlled by the harmonic mass $\mathscr L=\sum 1/p$ and yields logarithmic-scale Liouville correlation improvements.

3. L. Matthiesen, *Quantitative asymptotics for polynomial patterns in the primes*, Mathematika (2026). The Mobius/Liouville polynomial-pattern estimates save arbitrary powers of logarithm; this remains weaker than the fixed- $X$ -power admission target in Campaign 43.

4. J. Guo, *Logarithmic Chowla Correlations Across All Shift Scales*, arXiv:2608.23500, version current in September 2026. The result gives power-logarithmic logarithmically weighted two-point Liouville cancellation across shifts, not the present single-dyadic structured-weight fixed- $X$ -power estimate.

5. O. Gorodetsky, *The variance of integers without small prime factors in short intervals*, Math. Z. 308 (2024), Article 59. Its smooth-number analysis explicitly involves squarefree smooth counts $\Psi_{\mu^2}(x,y)$, consistent with the fact that fixed-power smoothness thresholds need not create power-sparse coefficient families.

---

# 21. Final status block

```text
CSM_RH PAPER 46

WL3 STRUCTURED WEIGHT DECOUPLING = CLOSED

TOTAL r_X L2 ENERGY = X^(1+o(1))

SMOOTH CARRIER ENERGY = X^(1+o(1)) AT EXPONENT RESOLUTION

ROUGH CARRIER ENERGY = X^(1+o(1)) AT EXPONENT RESOLUTION

POLYNOMIAL PRIME MARK MULTIPLICITY = O_{epsilon,w}(1)

MARKED ENERGY = NATURAL SCALE

FACTOR SPLIT = DETERMINANT FIBRE VOLUME X^(1+o(1))

ABSOLUTE / ENERGY-ONLY DECOUPLING = NO FIXED X POWER

SIGNED DECOUPLING = RETURNS TO MOBIUS / LIOUVILLE ARITHMETIC

CAMPAIGN 43 = ACTIVE

NEXT = WL4 CROSS_J_PRE_SQUARE_RECOMBINATION

RH = OPEN
```
