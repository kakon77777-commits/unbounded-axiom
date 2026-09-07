# CSM_RH Paper 14
## One-Sided Möbius Parity, Inverse-Zeta Coefficient Strength, and Endogenous Dilate Quasi-Orthogonality

**Project:** `CSM_RH`  
**Paper:** `14`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.4 / Paper 13`  
**Campaign:** `13 — ENDOGENOUS_MOBIUS_BILINEAR_STRENGTH_AUDIT`  
**Status:** Möbius-strength / second-moment mechanism audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

The main conclusions are:

```text
mu(mn) under the outer absolute value
  becomes one-sided Möbius cancellation in n

the inner parity coefficient
  carries an explicit inverse-zeta Dirichlet-series factor

coefficient-only fixed-power cancellation
  is zero-sensitive and may import zero-strip strength

generic Cauchy closure
  makes EMBF downstream of prime-error energy

a genuinely new route remains:
  diagonal-scale second-moment quasi-orthogonality across multiplicative dilates
```

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical EMBF object

Let

$$
B(x)=\vartheta(x)-x.
$$

Let

$$
\gamma(n,C)=\sum_{\substack{d\mid n\\ d\le C}}\mu(d).
$$

For

$$
L<n\le2L,
\qquad
mn<2N,
$$

define

$$
\boxed{
\mathfrak B_{N,L,C}
=
\sum_m
\left|
\sum_{\substack{L<n\le2L\\ mn<2N}}
\gamma(n,C)\mu(mn)w_N(mn)B(mn-1)
\right|.
}
$$

---

# 2. Exact Möbius factorization

For all positive integers $m,n$,

$$
\boxed{
\mu(mn)=\mu(m)\mu(n)\mathbf1_{(m,n)=1}.
}
$$

Hence:

## Theorem 2.1 — One-Sided Parity Factorization

$$
\boxed{
\mathfrak B_{N,L,C}
=
\sum_{\substack{m\\ \mu(m)\neq0}}
\left|
\sum_{\substack{L<n\le2L\\ mn<2N\\ (n,m)=1}}
\gamma(n,C)\mu(n)w_N(mn)B(mn-1)
\right|.
}
$$

The sign of $\mu(m)$ disappears because of the outer absolute value. The parity source is therefore one-sided in the inner $n$ variable.

```text
O-RH-030
OUTER_ABSOLUTE_ONE_SIDED_PARITY
status: CERTIFIED
```

---

# 3. The parity coefficient

Define

$$
\boxed{a_C(n)=\mu(n)\gamma(n,C).}
$$

For $d\mid n$,

$$
\mu(n)\mu(d)
=
\mu^2(d)\mu(n/d)\mathbf1_{(d,n/d)=1}.
$$

Therefore:

## Lemma 3.1

$$
\boxed{
a_C(n)
=
\sum_{\substack{dr=n\\ d\le C\\ (d,r)=1}}
\mu^2(d)\mu(r).
}
$$

---

# 4. Dirichlet series of the parity coefficient

For $\Re s>1$,

$$
A_C(s)=\sum_{n\ge1}\frac{a_C(n)}{n^s}.
$$

Then

$$
\boxed{
A_C(s)=\frac{P_C(s)}{\zeta(s)},
}
$$

where

$$
\boxed{
P_C(s)
=
\sum_{d\le C}
\frac{\mu^2(d)}{d^s}
\prod_{p\mid d}(1-p^{-s})^{-1}.
}
$$

For $C=1$,

$$
P_1(s)=1,
\qquad
A_1(s)=\frac1{\zeta(s)}.
$$

Thus the parity coefficient has an explicit inverse-zeta backbone.

---

# 5. Coprime-restricted coefficient

For squarefree $m$, define

$$
a_{C,m}(n)=a_C(n)\mathbf1_{(n,m)=1}.
$$

For $\Re s>1$,

$$
\boxed{
\sum_{n\ge1}\frac{a_{C,m}(n)}{n^s}
=
\frac{P_{C,m}(s)}{\zeta(s)},
}
$$

with

$$
\boxed{
P_{C,m}(s)
=
\sum_{\substack{d\le C\\ (d,m)=1}}
\frac{\mu^2(d)}{d^s}
\prod_{p\mid dm}(1-p^{-s})^{-1}.
}
$$

The finite Euler modifier changes. The inverse-zeta factor remains.

---

# 6. Coefficient partial sums and zero strength

Let

$$
A_C(x)=\sum_{n\le x}a_C(n).
$$

Suppose for fixed $C$ and fixed $\theta<1$, for every $\varepsilon>0$,

$$
A_C(x)=O_\varepsilon(x^{\theta+\varepsilon}).
$$

Then the Dirichlet series is holomorphic in $\Re s>\theta$. Hence every zeta zero $\rho$ in this half-plane must satisfy

$$
\boxed{P_C(\rho)=0.}
$$

For $C=1$, this becomes

$$
\boxed{\zeta(s)\neq0\qquad\Re s>\theta.}
$$

```text
O-RH-031
PARITY_COEFFICIENT_INVERSE_ZETA_STRENGTH
status: CERTIFIED AS STRENGTH AUDIT
```

This is a strength warning for coefficient-only proof routes; it is not an equivalence theorem for EMBF itself.

---

# 7. Inner one-variable transform

Define

$$
F_m(n)=w_N(mn)B(mn-1),
$$

and

$$
S_m
=
\sum_{\substack{L<n\le2L\\mn<2N}}
a_{C,m}(n)F_m(n).
$$

Then

$$
\boxed{\mathfrak B_{N,L,C}=\sum_{\mu(m)\neq0}|S_m|.}
$$

---

# 8. Variation of the endogenous dilate profile

Assume $mL\ll N$. Chebyshev gives $B(x)=O(x)$ and $w_N\le N$.

As $n$ runs over $[L,2L]$, the intervals $[mn,m(n+1))$ are disjoint. Using

$$
|B(y)-B(x)|\le \vartheta(y)-\vartheta(x)+(y-x)
$$

and Chebyshev, the total variation of $B(mn-1)$ is $O(N)$. The total variation of $w_N(mn)$ is also $O(N)$.

Hence:

## Lemma 8.1

$$
\boxed{\operatorname{Var}_{L<n\le2L}F_m(n)=O(N^2).}
$$

Endpoint sizes are also $O(N^2)$.

---

# 9. Coefficient-only Abel route

Let

$$
M_{C,m}(t;L)
=
\sum_{\substack{L<n\le t\\ (n,m)=1}}a_C(n).
$$

Discrete partial summation gives:

## Proposition 9.1

$$
\boxed{
|S_m|
\ll
N^2
\max_{L<t\le2L}|M_{C,m}(t;L)|.
}
$$

Consequently, if uniformly in relevant $m$,

$$
\max_{L<t\le2L}|M_{C,m}(t;L)|
\ll
L^{1-\delta+o(1)},
$$

then

$$
\boxed{
\mathfrak B_{N,L,C}
\ll
N^3L^{-\delta+o(1)}.
}
$$

If $L=N^\alpha$,

$$
\boxed{\mathfrak B_{N,L,C}\ll N^{3-\alpha\delta+o(1)}.}
$$

At $\alpha=1/2$, the gain is $\delta/2$.

A uniform coefficient theorem strong enough to include $C=1,m=1$ is a fixed-power Mertens theorem and hence fixed-zero-strip strength.

---

# 10. Generic second-moment closure

Define

$$
\boxed{
\mathcal Q_{N,L,C}
=
\sum_{\mu(m)\neq0}|S_m|^2.
}
$$

Let $M\asymp N/L$ be the number of outer $m$ values. Then

$$
\boxed{
\mathfrak B_{N,L,C}
\le
M^{1/2}\mathcal Q_{N,L,C}^{1/2}.
}
$$

Since $|a_{C,m}(n)|\le\tau(n)=N^{o(1)}$, Cauchy in $n$, divisor multiplicity, and $w_N^2\le N^2$ yield:

## Theorem 10.1 — Generic Energy Fallback

Let

$$
\mathcal E_B(2N)=\sum_{k<2N}|B(k-1)|^2.
$$

Then

$$
\boxed{
\mathfrak B_{N,L,C}
\ll
N^{3/2+o(1)}\mathcal E_B(2N)^{1/2}.
}
$$

If PODEE $(\kappa)$ holds uniformly on dyadic scales up to $N$, then

$$
\boxed{
\mathfrak B_{N,L,C}
\ll
N^{3-\kappa/2+o(1)}.
}
$$

Thus generic second-moment closure is downstream of the target energy.

```text
O-RH-032
EMBF_GENERIC_ENERGY_FALLBACK
status: CERTIFIED
```

---

# 11. Second-moment expansion

Expand

$$
\mathcal Q_{N,L,C}
=
\sum_m\sum_{n_1,n_2}
a_{C,m}(n_1)a_{C,m}(n_2)
F_m(n_1)F_m(n_2).
$$

The diagonal part $n_1=n_2$ has scale

$$
\boxed{\mathcal Q_{\rm diag}\ll N^{5+o(1)}.}
$$

The completely uncontrolled full second moment may be as large as $N^{11/2+o(1)}$ in a balanced window. Therefore proving diagonal-scale behavior is a genuine fixed-power gain.

---

# 12. Endogenous Möbius-Dilate Quasi-Orthogonality

Assume the balanced window

$$
\boxed{L=N^{1/2+o(1)}.}
$$

Define the target:

## EMDQO

$$
\boxed{\mathcal Q_{N,L,C}\ll N^{5+o(1)}.}
$$

Then $M=N^{1/2+o(1)}$, so

$$
\begin{aligned}
\mathfrak B_{N,L,C}
&\le M^{1/2}\mathcal Q_{N,L,C}^{1/2}\\
&\ll N^{1/4+o(1)}N^{5/2+o(1)}\\
&=N^{11/4+o(1)}.
\end{aligned}
$$

Hence:

## Theorem 12.1 — Diagonal Scale Gives a Fixed Power

$$
\boxed{
\operatorname{EMDQO}
\Longrightarrow
\mathfrak B_{N,L,C}
\ll
N^{3-1/4+o(1)}.
}
$$

No fixed-power Mertens estimate appears in the statement.

---

# 13. General window law

If $L=N^{\alpha+o(1)}$ and the same diagonal-scale estimate $\mathcal Q\ll N^{5+o(1)}$ holds, then

$$
\boxed{
\mathfrak B_{N,L,C}
\ll
N^{3-\alpha/2+o(1)}.
}
$$

Thus the generated fixed power is

$$
\boxed{\kappa=\alpha/2.}
$$

---

# 14. What EMDQO asks

The off-diagonal piece is

$$
\sum_m\sum_{n_1\neq n_2}
a_{C,m}(n_1)a_{C,m}(n_2)
w_N(mn_1)w_N(mn_2)
B(mn_1-1)B(mn_2-1).
$$

EMDQO therefore asks whether distinct multiplicative dilates of the prime-error profile are quasi-orthogonal on average over $m$ after parity weighting.

This is not ordinary Möbius randomness against an external bounded test function. The profile is generated by the same prime sequence.

---

# 15. Known Möbius uniformity calibration

Davenport-type Möbius exponential-sum estimates give savings stronger than every fixed power of $\log N$ against additive phases.

Modern Gowers-uniformity and ergodic results likewise provide strong logarithmic decay for Möbius against structured external systems.

These are substantial results, but they do not supply a fixed $N$ -power for the endogenous multiplicative profile $B(mn-1)$.

Recent 2026 work on multiple Möbius sums obtains nontrivial bounds in several multivariable settings while emphasizing that binary analogues remain substantially harder in that setting.

No cited result proves EMDQO.

---

# 16. EMBF status correction

Paper 13 promoted EMBF as a mechanism frontier. The present audit refines it:

```text
F-RH-012 EMBF
  DEMOTED TO AUXILIARY PARITY-SENSITIVE CONDITION
```

Reasons:

```text
coefficient-only route
  zero-sensitive

generic second moment
  downstream of PODEE

standalone EMBF
  not known to imply PESC at required precision
```

---

# 17. New canonical mechanism frontier

Create:

```text
F-RH-013
ENDOGENOUS_MOBIUS_DILATE_QUASI_ORTHOGONALITY
abbrev: EMDQO
status: OPEN
```

Canonical balanced target:

$$
\boxed{
\sum_m
\left|
\sum_{\substack{L<n\le2L\\mn<2N}}
a_{C,m}(n)w_N(mn)B(mn-1)
\right|^2
\ll
N^{5+o(1)},
\qquad
L=N^{1/2+o(1)}.
}
$$

---

# 18. Campaign 13 verdict

```text
TWO-SIDED MOBIUS CANCELLATION
  NO

INNER N-MOBIUS CANCELLATION
  YES / ONLY PARITY SIGN SOURCE

COEFFICIENT-ONLY FIXED POWER
  ZERO-SENSITIVE / STRENGTH-LOADED

GENERIC CAUCHY SECOND MOMENT
  DOWNSTREAM OF PODEE

DIAGONAL-SCALE SECOND MOMENT
  GENUINE FIXED-POWER SUFFICIENT MECHANISM

EMBF
  AUXILIARY

EMDQO
  NEW CANONICAL MECHANISM FRONTIER
```

No fixed-power EMDQO theorem is proved.

---

# 19. Campaign 14

The next campaign is:

```text
CSM_RH Campaign 14
EMDQO_OFF_DIAGONAL_CORRELATION_AUDIT
```

Write

$$
\mathcal Q
=
\mathcal Q_{\rm diag}
+
\mathcal Q_{\rm off}.
$$

The diagonal already satisfies

$$
\mathcal Q_{\rm diag}\ll N^{5+o(1)}.
$$

Therefore the next task is to determine whether one can prove

$$
\boxed{\mathcal Q_{\rm off}\ll N^{5+o(1)}}
$$

in signed total, or another estimate sufficient for the full second moment.

---

# 20. Campaign 14 required questions

```text
Q1
Can the m-sum be interpreted as a multiplicative correlation kernel in n1/n2?

Q2
Does dispersion reintroduce PODEE without gaining a power?

Q3
Can gamma(n,C) and Möbius signs force off-diagonal cancellation?

Q4
What happens near n1=n2?

Q5
Can known large-sieve technology see the endogenous B(mn) profile?

Q6
Do current Möbius uniformity estimates give only log-power decay?

Q7
What exact new off-diagonal theorem is required if known tools fail?
```

---

# 21. State transition

```text
CSM_RH v1.4
  ->
CSM_RH v1.5
```

with:

```text
Campaign 13
  CLOSED_AS_MOBIUS_STRENGTH_AND_SECOND_MOMENT_AUDIT

O-RH-030
  OUTER_ABSOLUTE_ONE_SIDED_PARITY
  CREATED / CERTIFIED

O-RH-031
  PARITY_COEFFICIENT_INVERSE_ZETA_STRENGTH
  CREATED / CERTIFIED AS STRENGTH AUDIT

O-RH-032
  EMBF_GENERIC_ENERGY_FALLBACK
  CREATED / CERTIFIED

F-RH-012
  EMBF
  DEMOTED TO AUXILIARY CONDITION

F-RH-013
  EMDQO
  CREATED / OPEN

Campaign 14
  EMDQO_OFF_DIAGONAL_CORRELATION_AUDIT
  READY
```

---

# 22. Final status

```text
RH = OPEN

PESC = OPEN

EMBF = AUXILIARY

COEFFICIENT-ONLY EMBF FIXED POWER
= ZERO-SENSITIVE

GENERIC EMBF SECOND MOMENT
= DOWNSTREAM OF PODEE

EMDQO DIAGONAL-SCALE SECOND MOMENT
= OPEN / GENUINE FIXED-POWER MECHANISM

BALANCED EMDQO SUCCESS
= kappa 1/4 parity-breaking gain

NEXT CAMPAIGN = 14
```

The new concrete target is

$$
\boxed{
\mathcal Q_{N,L,C}\ll N^{5+o(1)}
\qquad
L=N^{1/2+o(1)}.
}
$$

At the current closure state, this is the first parity-sensitive second-moment theorem which could produce a fixed power without simply assuming a fixed-power Mertens estimate or using PESC itself as input.
