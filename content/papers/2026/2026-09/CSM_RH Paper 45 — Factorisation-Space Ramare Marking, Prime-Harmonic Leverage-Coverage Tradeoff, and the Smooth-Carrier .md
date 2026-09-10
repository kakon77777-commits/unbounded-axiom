# CSM_RH Paper 45
## Factorisation-Space Ramare Marking, Prime-Harmonic Leverage-Coverage Tradeoff, and the Smooth-Carrier Residual

**Project:** CSM_RH  
**Paper:** 45  
**Version:** 0.1  
**Date:** 2026-09-07  
**Campaign:** 43 — `WEIGHTED_LIOUVILLE_POLYNOMIAL_PHASE_ATTACK`  
**Track:** WL2 — `LIOUVILLE_AWARE_RAMARE_EXTRACTION`  
**Canonical state transition:** v1.35 to v1.36

---

# 0. Trust boundary

This paper continues directly from CSM_RH Paper 44.

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

and

$$
h_\star
=
\frac{X}{Q}X^{\varepsilon/2-61w/100}.
$$

The admission target remains

$$
\boxed{
|\mathfrak R_{\lambda}(Q,Y)|
\ll
X^{-3w/10+o(1)}.
}
$$

Paper 44 closed phase-only determinant-fibre dispersion as WL1.
The center phase is an exact Archimedean gauge and therefore cannot by itself create a generic fixed-power operator gain.

The next live route is WL2:
extract genuine prime divisibility information while preserving the actual squarefree-factorisation weight $r_X$.

No claim of RH, no fixed zero-free strip, and no pointwise fixed-power Mertens or Liouville estimate is made.

---

# 1. Inherited factorisation space

The pure component from Paper 41 has

$$
L=\left\lceil\frac{10}{\varepsilon}\right\rceil
$$

Möbius variables on balanced scales

$$
m_i\sim U_i,
\qquad
U_i=X^{1/L+o(1)},
$$

with

$$
\prod_{i=1}^{L}U_i\asymp X.
$$

Paper 43 defined

$$
\boxed{
r_X(n)
=
\sum_{\substack{m_1\cdots m_L=n\\m_i\sim U_i}}
\mu^2(m_1)\cdots\mu^2(m_L).
}
$$

Thus $r_X(n)$ counts legal squarefree factorisation tuples.

For every legal tuple

$$
\mathbf m=(m_1,\ldots,m_L),
$$

and every prime $p$,

$$
\sum_{i=1}^{L}1_{p\mid m_i}
=
v_p(m_1\cdots m_L).
$$

This identity is exact because each $m_i$ is squarefree.
It is the key reason prime extraction can be performed without deleting $r_X$.

---

# 2. Prime-multiplicity marking

Let $\mathcal P$ be any finite set of primes.
Define

$$
\boxed{
\Omega_{\mathcal P}(n)
=
\sum_{p\in\mathcal P}v_p(n).
}
$$

This counts prime occurrences with multiplicity across the product $n$.

For a legal factor position $i$ and prime $p$, define the one-prime-removed weight

$$
\boxed{
\begin{aligned}
r_{X;i,p}^{-}(a)
=
\sum_{\substack{
q_i\prod_{j\ne i}m_j=a\\
pq_i\sim U_i,\ m_j\sim U_j\\
p\nmid q_i
}}
\mu^2(q_i)
\prod_{j\ne i}\mu^2(m_j).
\end{aligned}
}
$$

The condition $p\nmid q_i$ is exactly the squarefreeness condition

$$
\mu^2(pq_i)=1.
$$

For fixed $p$ and $n$, every legal factorisation of $n$ is counted once for each factor position containing $p$.
Therefore

## Theorem 2.1 — Exact marked-factorisation identity

For every prime $p$,

$$
\boxed{
\sum_{i=1}^{L}
r_{X;i,p}^{-}(n/p)
=
v_p(n)r_X(n).
}
$$

### Proof

Fix a legal tuple

$$
m_1\cdots m_L=n.
$$

Because every $m_i$ is squarefree, precisely $v_p(n)$ of the factors $m_i$ contain $p$.
For each such position write

$$
m_i=pq_i.
$$

Removing that occurrence of $p$ produces exactly one summand of

$$
r_{X;i,p}^{-}(n/p).
$$

Conversely every summand of the right-hand marked family reconstructs a legal tuple of product $n$ with $p\mid m_i$.
Summing over the $v_p(n)$ marked positions gives the identity.

 $\square$

Summing over $p\in\mathcal P$ gives

$$
\boxed{
\sum_{p\in\mathcal P}
\sum_{i=1}^{L}
r_{X;i,p}^{-}(n/p)
=
\Omega_{\mathcal P}(n)r_X(n).
}
$$

Hence on the branch

$$
\Omega_{\mathcal P}(n)>0,
$$

we have the exact Ramaré-type formula

$$
\boxed{
r_X(n)
=
\sum_{p\in\mathcal P}
\sum_{i=1}^{L}
\frac{r_{X;i,p}^{-}(n/p)}{\Omega_{\mathcal P}(n)}.
}
$$

Create:

```text
B-RH-021
FACTORISATION_SPACE_RAMARE_MARKING_IDENTITY
status:
  CERTIFIED EXACT IDENTITY
```

This is stronger than replacing $r_X$ by $d_L$ before extraction.
The exact restricted squarefree factorisation structure survives.

---

# 3. Liouville-aware extraction

Because

$$
\lambda(p)=-1
$$

for every prime $p$ and $\lambda$ is completely multiplicative,

$$
\lambda(n)
=
-\lambda(n/p)
$$

whenever $p\mid n$.

For the twisted function,

$$
f_Q(n)
=
-p^{iQ}f_Q(n/p).
$$

Combining this with Theorem 2.1 gives

## Theorem 3.1 — Exact twisted marked extraction

On $\Omega_{\mathcal P}(n)>0$,

$$
\boxed{
 f_Q(n)r_X(n)
=
-
\sum_{p\in\mathcal P}
\sum_{i=1}^{L}
\frac{p^{iQ}f_Q(n/p)r_{X;i,p}^{-}(n/p)}
{\Omega_{\mathcal P}(n)}.
}
$$

Similarly,

$$
\boxed{
 \overline{f_Q(n)}r_X(n)
=
-
\sum_{p\in\mathcal P}
\sum_{i=1}^{L}
\frac{p^{-iQ}\overline{f_Q(n/p)}r_{X;i,p}^{-}(n/p)}
{\Omega_{\mathcal P}(n)}.
}
$$

No Möbius or Liouville sign has been discarded.
No new scale averaging has been introduced.

---

# 4. Fixed-power extraction threshold

Define

$$
\boxed{
\rho_\star
=
\frac{31w}{100}
}
$$

and

$$
\boxed{
P_\star
=
X^{\rho_\star}.
}
$$

The target exponent is

$$
\frac{3w}{10}
=
\frac{30w}{100}.
$$

Thus a branch bounded by

$$
P_\star^{-1+o(1)}
$$

has the same extra margin as the enlarged harmless shift shell from Paper 43:

$$
\boxed{
P_\star^{-1+o(1)}
=
X^{-31w/100+o(1)}
=
X^{-3w/10-w/100+o(1)}.
}
$$

The balanced pure-core factors have size

$$
U_i=X^{1/L+o(1)}.
$$

Since

$$
w\le\frac{\varepsilon}{1000}
$$

and

$$
L=\left\lceil\frac{10}{\varepsilon}\right\rceil,
$$

we have, for fixed $0<\varepsilon\le1$,

$$
\rho_\star
<
\frac1L
$$

with a very large exponent margin.
Hence the range

$$
P_\star<p\lesssim X^{1/L}
$$

is nonempty for large $X$.

Let

$$
\mathcal P_\star
=
\{p:\ P_\star<p\le z\},
\qquad
z=(2X)^{1/L}.
$$

---

# 5. Common-prime branch

Suppose an extracted prime satisfies

$$
p\mid m
$$

and

$$
p\mid h.
$$

Then

$$
p\mid m+h.
$$

Thus $p$ is common to both sides of the shifted pair.
The Liouville and Archimedean prime factors cancel exactly:

if

$$
m=pa,
\qquad
h=pk,
$$

then

$$
m+h=p(a+k)
$$

and

$$
\boxed{
\overline{f_Q(m)}f_Q(m+h)
=
\overline{f_Q(a)}f_Q(a+k).
}
$$

This is a recursive smaller-scale copy, accompanied by a denominator factor $p^{-2}$.

The branch is also harmless by absolute values.
Let

$$
H_{\max}
\lesssim
X^{o(1)}\frac{X}{Y}
$$

be the Gaussian-supported shift length.
Since $r_X(n)\le d_L(n)=X^{o(1)}$ on $n\asymp X$,

$$
\begin{aligned}
|\mathfrak R_{\mathrm{common}}|
&\ll
Y X^{-2+o(1)}
\sum_{p>P_\star}
\#\{h\le H_{\max}:p\mid h\}
\#\{m\asymp X:p\mid m\}\\
&\ll
Y X^{-2+o(1)}
\sum_{p>P_\star}
\frac{H_{\max}}p
\frac Xp\\
&\ll
X^{o(1)}
\sum_{p>P_\star}\frac1{p^2}\\
&\ll
P_\star^{-1+o(1)}.
\end{aligned}
$$

Therefore

## Theorem 5.1 — Large common-prime branch is fixed-power harmless

$$
\boxed{
|\mathfrak R_{\mathrm{common}}|
\ll
X^{-31w/100+o(1)}.
}
$$

Create:

```text
B-RH-022
LARGE_COMMON_PRIME_BRANCH_FIXED_POWER_HARMLESS
status:
  CERTIFIED
```

This completes the Campaign 43 requirement to separate primes dividing both $m$ and $m+h$ through

$$
(m,m+h)=(m,h).
$$

---

# 6. Repeated-large-prime branch

The marked identity allows $v_p(m)\ge2$ because the same prime may occur in several distinct squarefree factors $m_i$.

For $p>P_\star$, the total branch with

$$
p^2\mid m
$$

is again harmless.

Indeed,

$$
\begin{aligned}
|\mathfrak R_{p^2}|
&\ll
Y X^{-2+o(1)}
H_{\max}
\sum_{p>P_\star}
\#\{m\asymp X:p^2\mid m\}\\
&\ll
Y X^{-2+o(1)}
H_{\max}
\sum_{p>P_\star}
\frac X{p^2}\\
&\ll
X^{o(1)}
\sum_{p>P_\star}\frac1{p^2}\\
&\ll
P_\star^{-1+o(1)}.
\end{aligned}
$$

Thus

## Theorem 6.1 — Repeated large primes are fixed-power harmless

$$
\boxed{
|\mathfrak R_{p^2}|
\ll
X^{-31w/100+o(1)}.
}
$$

Create:

```text
B-RH-023
REPEATED_LARGE_PRIME_BRANCH_FIXED_POWER_HARMLESS
status:
  CERTIFIED
```

After Sections 5-6, the main extracted branch may assume

$$
\boxed{
p\nmid h,
\qquad
v_p(m)=1.
}
$$

In particular

$$
p\nmid m+h.
$$

---

# 7. Exact asymmetric prime-Liouville core

On the main branch write

$$
m=pa,
\qquad
p\in\mathcal P_\star,
\qquad
p\nmid a,
\qquad
p\nmid h.
$$

Then

$$
m+h=pa+h
$$

and the exact extracted factor is

$$
\overline{f_Q(m)}r_X(m)
=
-
\sum_i
\frac{p^{-iQ}\overline{f_Q(a)}r_{X;i,p}^{-}(a)}
{\Omega_{\mathcal P_\star}(pa)}
$$

inside the marked $p$ -summand.

Therefore the main one-sided extracted object is

$$
\boxed{
\begin{aligned}
\mathfrak R_{\mathrm{aff}}
=
-Y
\sum_{p\in\mathcal P_\star}
\sum_{i=1}^{L}
\sum_{\substack{h\\p\nmid h}}
\sum_a
&\frac{p^{-iQ}\overline{f_Q(a)}f_Q(pa+h)}
{pa(pa+h)}\\
&\times
\frac{r_{X;i,p}^{-}(a)r_X(pa+h)}
{\Omega_{\mathcal P_\star}(pa)}
\widehat\Phi\!\left(Y\log(1+h/(pa))\right),
\end{aligned}
}
$$

up to the already-harmless common-prime and repeated-prime branches.

Create:

```text
B-RH-024
ASYMMETRIC_PRIME_LIOUVILLE_AFFINE_REDUCTION
status:
  CERTIFIED EXACT STRUCTURAL REDUCTION
```

The Liouville correlation order has not doubled.
This is a genuine advantage over WL1 van der Corput differencing.

However, the remaining arithmetic value is now

$$
f_Q(pa+h),
$$

namely a twisted Liouville value on an affine form in a prime variable.
The parity problem has been moved into an affine prime-Liouville correlation; it has not disappeared.

---

# 8. Double extraction and prime-determinant geometry

If the second side also has a large prime factor, apply the same marking identity to

$$
f_Q(pa+h)r_X(pa+h).
$$

Write

$$
pa+h=qb.
$$

On the main branch $p\nmid h$ and $q\nmid h$.
If $p=q$, then

$$
p\mid(qb-pa)=h,
$$

contradicting the main-branch condition.
Therefore

$$
\boxed{p\ne q.}
$$

The twice-extracted relation is

$$
\boxed{
qb-pa=h.
}
$$

The remaining Liouville carrier is

$$
\overline{f_Q(a)}f_Q(b),
$$

while the prime twist is

$$
p^{-iQ}q^{iQ}.
$$

Thus double extraction produces a prime-decorated determinant incidence rather than removing Liouville parity.

---

# 9. Prime incidence alone gives no fixed power

Consider one dyadic prime block

$$
p,q\sim P,
$$

with

$$
P_\star\le P\le z.
$$

Since

$$
pa\asymp X,
$$

we have

$$
a\asymp A,
\qquad
A\asymp\frac XP.
$$

For fixed distinct primes $p,q$ and fixed shift $h$, the equation

$$
qb-pa=h
$$

forces

$$
pa\equiv-h\pmod q.
$$

Since $p$ is invertible modulo $q$, $a$ occupies one residue class modulo $q$.
Hence

$$
\#\{a\asymp A:qb-pa=h\}
\ll
\frac Aq+1.
$$

Because

$$
P\le X^{1/L+o(1)}
$$

and $L$ is fixed and large,

$$
\frac Aq
\asymp
\frac X{P^2}
\gg1.
$$

Therefore

$$
\#\{a\}
\ll
\frac X{P^2}.
$$

The number of ordered prime pairs $p,q\sim P$ is

$$
\ll
\frac{P^2}{(\log P)^2}.
$$

Consequently the total prime-determinant incidence count on one dyadic block is only

$$
\boxed{
\ll
\frac{X}{(\log P)^2}
}
$$

before divisor-type structured weights.
At exponent resolution this is

$$
X^{1+o(1)},
$$

not

$$
X^{1-\delta}.
$$

Thus prime congruence counting by itself reproduces the old incidence floor up to logarithms.

Create:

```text
O-RH-114
DOUBLE_RAMARE_PRIME_INCIDENCE_STOPS_AT_LOGARITHMIC_GEOMETRY
status:
  CERTIFIED AS GEOMETRIC MECHANISM BARRIER
```

A successful double-extraction argument would still need arithmetic cancellation from the residual Liouville values or another non-generic coupling.

---

# 10. Prime-harmonic mass of the fixed-power extraction band

The prime range available to the balanced pure core is

$$
P_\star<p\le z,
$$

where

$$
P_\star=X^{\rho_\star},
\qquad
z=X^{1/L+o(1)}.
$$

Mertens' theorem gives

$$
\sum_{P_\star<p\le z}\frac1p
=
\log\log z-\log\log P_\star+o(1).
$$

Since both endpoints are fixed powers of $X$,

$$
\boxed{
\sum_{P_\star<p\le z}\frac1p
=
\log\left(\frac{1/L}{\rho_\star}\right)+o(1).
}
$$

This is a constant depending on $\varepsilon$ and $w$.
It does not grow with $X$.

Define

$$
\mathscr L(P,z)
=
\sum_{P<p\le z}\frac1p.
$$

More generally, let

$$
P=X^{\rho(X)},
\qquad
z=X^{\theta+o(1)},
\qquad
\theta>0
$$

with $\rho(X)>0$.
Then

$$
\boxed{
\mathscr L(P,z)
=
\log\frac{\theta}{\rho(X)}+o(1).
}
$$

Therefore:

1. if $\rho(X)\ge\rho_0>0$, then $\mathscr L(P,z)=O(1)$ ;
2. if $\mathscr L(P,z)\to\infty$, then $\rho(X)\to0$ ;
3. if $\rho(X)\to0$, then
   $$
   P=X^{o(1)},
   $$
   so any saving that is only $P^{-c}$ is
   $$
   X^{-o(1)}.
   $$

This produces an exact leverage-versus-harmonic-mass tradeoff.

## Theorem 10.1 — Prime-harmonic leverage barrier

A Ramaré/divisibility mechanism whose two quantitative resources are only

1. harmonic averaging through $\mathscr L(P,z)$ ; and
2. a saving polynomial in the lower extracted-prime scale $P$,

cannot simultaneously obtain

$$
\mathscr L(P,z)\to\infty
$$

and a fixed saving

$$
P^{-c}\le X^{-\delta}
$$

for fixed $c,\delta>0$.

Create:

```text
O-RH-115
PRIME_HARMONIC_MASS_VERSUS_FIXED_POWER_LEVERAGE_BARRIER
status:
  CERTIFIED AS MECHANISM-SCOPE BARRIER
```

This does not rule out a deeper arithmetic use of the extracted prime.
It rules out obtaining the missing fixed power merely by combining a growing Ramaré prime average with the size of that same extracted prime.

---

# 11. The no-large-prime branch is not power-negligible

One might try to avoid Theorem 10.1 by extracting only primes

$$
p>P_\star
$$

and discarding integers with no such prime.

That disposal is not available at fixed-power precision.

For the balanced pure component, each factor has

$$
U_i=X^{1/L+o(1)}.
$$

Fix an integer $K$ so large that

$$
\frac{1}{LK}<\frac{\rho_\star}{2}.
$$

This $K$ depends only on fixed $\varepsilon,w$.

Choose a fixed $\eta>0$ so small that

$$
(1+\eta)^K<2.
$$

For each $i$, consider primes in the interval

$$
\mathcal Q_i
=
\left[
U_i^{1/K},
(1+\eta)U_i^{1/K}
\right].
$$

By the prime number theorem in a fixed relative interval,

$$
\#\mathcal Q_i
\gg_{\varepsilon,w}
\frac{U_i^{1/K}}{\log X}.
$$

Take $K$ distinct primes from $\mathcal Q_i$ and multiply them.
The resulting integer $m_i$ is squarefree and satisfies

$$
U_i
\le
m_i
<
2U_i.
$$

Moreover every prime factor of $m_i$ is at most

$$
(1+\eta)U_i^{1/K}
\le
X^{\rho_\star/2+o(1)}
<
P_\star.
$$

The number of such $m_i$ is

$$
\gg
\frac{U_i}{(\log X)^K}.
$$

Choosing such an $m_i$ independently for every factor position gives at least

$$
\boxed{
\frac{X}{(\log X)^{KL+O(1)}}
}
$$

legal factorisation tuples in the pure component for which the total product $n$ has no prime factor exceeding $P_\star$.

Since $r_X(n)$ counts legal tuples,

## Theorem 11.1 — Log-dense smooth-carrier mass

For some fixed constant $C_{\varepsilon,w}>0$,

$$
\boxed{
\sum_{\substack{n\asymp X\\P^+(n)<P_\star}}
r_X(n)
\gg
\frac{X}{(\log X)^{C_{\varepsilon,w}}}.
}
$$

Here $P^+(n)$ is the largest prime factor of $n$.

The constructed tuples have exactly $K$ prime factors in each $m_i$.
Therefore their total Liouville parity is constant:

$$
\boxed{
\lambda(n)=(-1)^{KL}
}
$$

throughout this constructed subfamily.

Thus the no-large-prime branch is not merely logarithmically dense in $r_X$ -mass; it contains a logarithmically dense sign-coherent subfamily.

Create:

```text
O-RH-116
POLYNOMIAL_PRIME_EXTRACTION_LEAVES_LOG_DENSE_SIGN_COHERENT_SMOOTH_CARRIER
status:
  CERTIFIED
```

This statement is about the exact pure-core factorisation space.
It does not claim that the shifted two-point smooth branch has a nonzero asymptotic correlation.
It proves that the branch cannot be deleted by an absolute fixed-power coverage estimate.

---

# 12. External Ramaré calibration

The structural conclusion above is consistent with the known quantitative role of Ramaré extraction.

Matomäki and Teräväinen use Ramaré's identity to extract a small prime factor in their work on Möbius sums in short intervals.
The result is a qualitative

$$
o(x^\theta)
$$

for every

$$
\theta>0.55,
$$

not a uniform fixed $X$ -power gain of the kind required here.

Helfgott and Radziwiłł study a divisibility-by-primes graph with harmonic prime mass

$$
\mathscr L
=
\sum_{p\in\mathbf P}\frac1p.
$$

Their spectral scale is of order

$$
\sqrt{\mathscr L},
$$

and their Liouville two-point consequence has logarithmic-size gain, for example

$$
O\left((\log\log x)^{-1/2}\right)
$$

in a logarithmically averaged setting.

For the present polynomial extraction interval,

$$
\mathscr L
=O_{\varepsilon,w}(1),
$$

so that source of gain does not even grow with $X$.

Likewise, current shifted-prime Möbius/Liouville results averaged over shifts provide qualitative or logarithmic-power cancellation, not the required single-dyadic fixed power of $X$ for the weighted affine form in Section 7.

This calibration is not used as a proof of impossibility.
It confirms that WL2 has reached a quantitatively stronger target than standard Ramaré/shift-averaged parity technology currently supplies.

---

# 13. WL2 audit

## Required check 1 — separate primes dividing both sides

Passed.

The common-prime branch $p\mid h$ is recursively self-similar and is bounded by

$$
X^{-31w/100+o(1)}.
$$

## Required check 2 — extract without deleting $r_X$

Passed.

B-RH-021 is an exact factorisation-space identity.

## Required check 3 — preserve one dyadic scale

Passed.

All extracted weights retain the original dyadic constraints through

$$
pq_i\sim U_i.
$$

No averaging over external $X$ -scales occurs.

## Required check 4 — fixed power rather than logarithmic gain

Not obtained on the main affine branch.

Prime incidence geometry gives only logarithmic savings, while polynomial prime averaging has bounded harmonic mass.

## Required check 5 — audit $p^2$

Passed.

The repeated-large-prime branch is bounded by

$$
X^{-31w/100+o(1)}.
$$

## Required check 6 — no hidden zero-free strip

Passed.

No Dirichlet-polynomial fixed-power estimate for Möbius, Liouville, primes, or $1/L(s)$ is inserted.

---

# 14. What WL2 actually achieved

WL2 did not prove B-RH-014.

It did produce four exact structural gains.

First, the $r_X$ weight is compatible with a precise prime-marking identity.

Second, all large-prime common-divisor contamination is fixed-power harmless.

Third, all repeated-large-prime contamination is fixed-power harmless.

Fourth, the genuinely hard extracted branch has been localized to

$$
\boxed{
\text{affine prime variable}
+
\text{twisted Liouville residual}
+
\text{structured marked }r_X\text{ weights}.
}
$$

The prime variable is therefore useful as a structural coordinate, but ordinary incidence counting and prime-harmonic averaging do not yet provide the missing fixed power.

---

# 15. Why WL2 closes

The original WL2 question was whether prime extraction itself could break the simultaneous resonance remaining after Paper 44.

The answer is now precise.

It breaks the common-prime ambiguity and produces a clean asymmetric affine form.
But it creates two unavoidable residual branches:

$$
\boxed{
\text{large-prime affine Liouville branch}
}
$$

and

$$
\boxed{
\text{no-large-prime smooth-carrier branch}.
}
$$

The first still requires parity-sensitive arithmetic cancellation.
The second has only logarithmic coverage loss and contains a sign-coherent factorisation subfamily.

Thus WL2 is closed as a successful structural reduction, not as a fixed-power theorem.

```text
WL2
CLOSED_AS_EXACT_MARKED_EXTRACTION_WITH_PRIME_HARMONIC_AND_SMOOTH_CARRIER_BARRIERS
```

Campaign 43 remains active.

---

# 16. Campaign 43 continuation

The next track is WL3:

```text
STRUCTURED_WEIGHT_DECOUPLING
```

The new WL3 task is sharper than the original generic wording.

It must separately audit:

1. the smooth-carrier branch
   $$
   P^+(n)<P_\star;
   $$
2. the rough marked branch carrying $r_{X;i,p}^{-}$ ;
3. whether the convolution
   $$
   r_X
   =
   (\mu^2 1_{U_1})*\cdots*(\mu^2 1_{U_L})
   $$
   admits an $L^2$ or dispersion decoupling with a genuine fixed $X$ -power;
4. whether the sign-coherent smooth subfamily prevents an absolute or positivity-based decoupling;
5. whether a legal decomposition can create a new long averaging variable without destroying the single prescribed dyadic scale.

Cross- $j$ pre-square recombination remains live as WL4.

---

# 17. State transition

The canonical state advances

```text
CSM_RH v1.35
  ->
CSM_RH v1.36
```

Create:

```text
B-RH-021
FACTORISATION_SPACE_RAMARE_MARKING_IDENTITY
CERTIFIED
```

```text
B-RH-022
LARGE_COMMON_PRIME_BRANCH_FIXED_POWER_HARMLESS
CERTIFIED
```

```text
B-RH-023
REPEATED_LARGE_PRIME_BRANCH_FIXED_POWER_HARMLESS
CERTIFIED
```

```text
B-RH-024
ASYMMETRIC_PRIME_LIOUVILLE_AFFINE_REDUCTION
CERTIFIED
```

Create:

```text
O-RH-114
DOUBLE_RAMARE_PRIME_INCIDENCE_STOPS_AT_LOGARITHMIC_GEOMETRY
CERTIFIED AS GEOMETRIC MECHANISM BARRIER
```

```text
O-RH-115
PRIME_HARMONIC_MASS_VERSUS_FIXED_POWER_LEVERAGE_BARRIER
CERTIFIED AS MECHANISM-SCOPE BARRIER
```

```text
O-RH-116
POLYNOMIAL_PRIME_EXTRACTION_LEAVES_LOG_DENSE_SIGN_COHERENT_SMOOTH_CARRIER
CERTIFIED
```

No root promotion occurs.

$$
\boxed{
\mathrm{RH\_PROVED}=\mathrm{false}
}
$$

$$
\boxed{
\mathrm{RH\_DISPROVED}=\mathrm{false}
}
$$

$$
\boxed{
\mathrm{GLOBAL\_RH\_CERTIFICATE}=\mathrm{false}
}
$$

The root frontier remains

$$
\boxed{
F\text{-}RH\text{-}010
=
\mathrm{PESC}
=
\mathrm{OPEN}.
}
$$

The direct theorem candidate remains

$$
\boxed{
F\text{-}RH\text{-}016
=
\mathrm{MLEPG}
=
\mathrm{OPEN}.
}
$$

---

# 18. Campaign 43 verdict after Paper 45

The frontier has changed from

$$
\text{weighted Liouville polynomial-phase core}
$$

to the sharper split

$$
\boxed{
\begin{array}{c}
\text{rough marked affine prime-Liouville branch}\\
\oplus\\
\text{log-dense smooth-carrier structured-weight branch}.
\end{array}
}
$$

The large common-prime and repeated-prime branches are no longer part of the hard core.

The center phase is no longer treated as an independent generic cancellation source.
The extracted prime is no longer treated as a generic fixed-power amplifier.

The next legitimate question is whether the exact nonnegative factorisation weight itself contains a decoupling or energy gain that neither WL1 nor WL2 could see.

That is Campaign 43 / WL3.

---

# 19. External references

1. K. Matomäki and J. Teräväinen, *On the Möbius function in all short intervals*, arXiv:`1911.09076`, J. Eur. Math. Soc. 25 (2023), 1207-1225. The main new idea includes Ramaré prime-factor extraction; the resulting short-interval theorem is qualitative $o(1)$ at the normalized scale.

2. H. A. Helfgott and M. Radziwiłł, *Expansion, divisibility and parity*, arXiv:`2103.06853`. The prime-divisibility graph is governed by the harmonic mass $\mathscr L=\sum 1/p$ and yields logarithmic-scale Liouville correlation gains.

3. J. D. Lichtman, *Averages of the Möbius function on shifted primes*, arXiv:`2009.08969`, Q. J. Math. 73 (2022), 729-757. The quantitative averaged-shift bounds provide logarithmic rather than fixed- $X$ -power savings.

4. J. D. Lichtman and J. Teräväinen, *On the Hardy-Littlewood-Chowla conjecture on average*, arXiv:`2111.08912`, Forum Math. Sigma 10 (2022). The theorem gives strong averaged-shift cancellation but does not supply the single-dyadic structured-weight fixed- $X$ -power estimate required here.

5. O. Gorodetsky, *Smooth numbers and the Dickman $\rho$ function*, J. Anal. Math. 151 (2023), 139-169. This calibrates the abundance of integers free of large prime factors; Paper 45 uses instead an elementary fixed- $K$ prime-product construction for the certified lower bound in Section 11.

---

# 20. Final status

```text
PAPER 45 = VALID STRUCTURAL ADVANCE

WL2 EXACT r_X-PRESERVING RAMARE MARKING = CERTIFIED
LARGE COMMON-PRIME BRANCH = FIXED-POWER HARMLESS
REPEATED LARGE-PRIME BRANCH = FIXED-POWER HARMLESS
ASYMMETRIC AFFINE PRIME-LIOUVILLE REDUCTION = CERTIFIED
DOUBLE-PRIME INCIDENCE FIXED-POWER GAIN = NOT OBTAINED
POLYNOMIAL PRIME HARMONIC MASS = BOUNDED
NO-LARGE-PRIME SMOOTH CARRIER = NOT POWER-NEGLIGIBLE
WL2 = CLOSED AS STRUCTURAL REDUCTION
CAMPAIGN 43 = ACTIVE
NEXT = WL3 STRUCTURED_WEIGHT_DECOUPLING
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
RH = OPEN
```
