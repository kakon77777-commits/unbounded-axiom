# CSM_RH Paper 88

## Polynomial-Threshold Inertia, Extremal-Family Sieve-Level Conservation, and a Threshold-Type-II Gate for the Prime-Excess Tail

**Project:** CSM_RH  
**Paper:** 88  
**Version:** v0.1  
**Date:** 2026-09-09  
**Canonical root frontier:** F-RH-017-v3  
**One-sided frontier:** F-RH-027+  
**Entry state:** v1.78 / Paper 87 v0.1  
**Status:** POLYNOMIAL-THRESHOLD INERTIA CERTIFIED / EXTREMAL-FAMILY LOCAL SIEVE LEVEL SHOWN NOT TO IMPROVE WITH FAMILY SIZE / INERTIA ENTROPY DOES NOT REMOVE X^ν RESOLUTION CLASS / THRESHOLD-SENSITIVE TYPE-II FRONTIER IDENTIFIED  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 87 showed that controlling the prime-excess tail

$$
\mathcal E_\nu^+
=
\left\{
x:
\Delta_H(x)>HX^{-\nu}
\right\}
$$

by global factorial moments requires polynomial order

$$
X^\nu\log X.
$$

It proposed a threshold-native alternative:

> use inertia to compress the exceptional set into a maximal separated family and sieve only that family.

The present paper audits this strategy.

Let

$$
H=X^{1-\tau}
$$

and

$$
\boxed{
T=HX^{-\nu}.
}
$$

The first result is a polynomial-threshold inertia theorem.

For fixed $H$ and $x,y\asymp X$,

$$
\Delta_H(x)=\psi(x+H)-\psi(x)-H.
$$

Since

$$
\Lambda(n)\le\log(4X)
$$

on the relevant range,

$$
\boxed{
|\Delta_H(y)-\Delta_H(x)|
\le
2(|y-x|+1)\log(4X).
}
$$

Therefore, if

$$
\Delta_H(x)>T,
$$

then

$$
\boxed{
\Delta_H(y)>\frac{T}{2}
}
$$

whenever

$$
\boxed{
|y-x|
\le
L
:=
\frac{T}{8\log(4X)}
}
$$

for sufficiently large $X$.

Thus

$$
\boxed{
L=X^{1-\tau-\nu+o(1)}.
}
$$

The same statement holds for the deficiency tail.

This extends the power-scale content of the classical inertia property to the polynomially shrinking threshold relevant to F-RH-017-v3.

Bazzanella and Perelli's published fixed-threshold inertia theorem requires

$$
\delta-\delta'
\ge
\exp(-\sqrt{\log X}),
$$

which does not include

$$
\delta=X^{-\nu}.
$$

The elementary bounded-jump argument above loses only logarithms and is sufficient for the exponent ledger.

Now select a maximal $L$ -separated family of excess centers

$$
\boxed{
\mathcal C=\{x_1,\ldots,x_J\}.
}
$$

A maximal-net covering gives

$$
\boxed{
|\mathcal E_\nu^+|
\ll
JL
}
$$

at fixed-power resolution.

Therefore failure of an exceptional bound

$$
|\mathcal E_\nu^+|
\ll
X^{1-c}
$$

forces

$$
\boxed{
J\gg X^{\tau+\nu-c-o(1)}.
}
$$

A greedy extraction of an $H$ -separated subfamily gives at least

$$
\boxed{
K\gg J\frac{L}{H}
=
JX^{-\nu-o(1)}.
}
$$

Hence

$$
\boxed{
K\gg X^{\tau-c-o(1)}.
}
$$

This produces an important regime split.

### Strip-dominated exceptional mass

If

$$
d<\tau,
$$

then F-RH-017-v3 only requires

$$
c>d.
$$

One may test a violation at some

$$
d<c<\tau.
$$

Such a violation forces polynomially many $H$ -separated prime-rich intervals.

### Lag-dominated exceptional mass

If

$$
\tau\le d,
$$

then F-RH-017-v3 requires

$$
c>\tau.
$$

A failure of the desired bound need not produce polynomially many $H$ -separated intervals.

It may be supported in only one or a bounded number of $H$ -scale clusters.

Thus an extremal-family method is structurally better suited to the regime

$$
d<\tau.
$$

Combining this with the Poisson-resolution window

$$
d<\nu<\frac{1-\tau}{2}
$$

gives:

## Early-bootstrap family window

There exist parameters satisfying

$$
\boxed{
d<\tau
}
$$

and

$$
\boxed{
d<\nu<\frac{1-\tau}{2}
}
$$

if and only if

$$
\boxed{
d<\frac13.
}
$$

Equivalently,

$$
\boxed{
\kappa<\frac23.
}
$$

So a separated-family excess strategy can only live in the clean Poisson large-deviation window as an early-to-middle bootstrap mechanism.

The second main result is the family-size cancellation law for local sieve information.

Associate to the centers the multiset sequence

$$
\boxed{
a_{\mathcal C}(n)
=
\sum_{j=1}^J
\mathbf1_{(x_j,x_j+H]}(n).
}
$$

Its total mass is

$$
\boxed{
A_{\mathcal C}
=
JH+O(J).
}
$$

For every modulus $q$,

$$
\boxed{
A_{\mathcal C,q}
:=
\sum_{q\mid n}
a_{\mathcal C}(n)
=
\frac{JH}{q}
+
O(J).
}
$$

Therefore, for every fixed divisor weight exponent $B$,

$$
\boxed{
\sum_{q\le D}
\tau(q)^B
\left|
A_{\mathcal C,q}
-
\frac{A_{\mathcal C}}{q}
\right|
\ll_B
JD(\log D)^{O_B(1)}.
}
$$

Relative to the total mass,

$$
\boxed{
\frac{\text{sieve remainder to level }D}{A_{\mathcal C}}
\ll
\frac{D}{H}X^{o(1)}.
}
$$

The number of exceptional intervals $J$ cancels completely.

Consequently, collecting a large family does not by itself increase the deterministic local-divisibility level beyond the length of one interval.

At prime-detection scale, classical upper-sieve bounds retain a fixed multiplicative gap.

For a single polynomial interval

$$
H=X^\theta,
\qquad
\theta=1-\tau,
$$

Brun–Titchmarsh gives

$$
\boxed{
\pi(x+H)-\pi(x)
\le
\left(
\frac{2}{\theta}+o(1)
\right)
\frac{H}{\log X}.
}
$$

Summing over the multiset family gives exactly the same constant:

$$
\boxed{
\sum_j
\left(
\pi(x_j+H)-\pi(x_j)
\right)
\le
\left(
\frac{2}{1-\tau}+o(1)
\right)
\frac{JH}{\log X}.
}
$$

Since

$$
X^{-\nu}\to0,
$$

this cannot contradict the near-mean excess

$$
\boxed{
\sum_j
\left(
\pi(x_j+H)-\pi(x_j)
\right)
\ge
\left(
1+cX^{-\nu}
\right)
\frac{JH}{\log X}.
}
$$

The standard dimension-one linear sieve gives the same structural diagnosis.

If one uses only the deterministic divisor remainder above, the available level is

$$
D\lesssim H.
$$

When the upper linear sieve is in the range

$$
1\le s\le3,
$$

its function is

$$
\boxed{
F(s)=\frac{2e^\gamma}{s}.
}
$$

At a prime-scale sifting point

$$
z\asymp X^{1/2},
$$

the parameter is

$$
s=\frac{\log D}{\log z}
\lesssim
2(1-\tau).
$$

Thus the classical sieve constant remains bounded away from $1$.

The family size does not change $s$.

The third result concerns entropy.

The inertia scale compresses the continuum of possible starts to a grid of size

$$
\boxed{
B_{\rm grid}
\asymp
\frac{X}{L}
=
X^{\tau+\nu+o(1)}.
}
$$

But the target exceptional estimate

$$
|\mathcal E_\nu^+|
\ll
X^{1-c}
$$

corresponds to an exceptional fraction

$$
\boxed{
\frac{J}{B_{\rm grid}}
\ll
X^{-c+o(1)}.
}
$$

Thus inertia reduces the number of candidate positions, but not the power of $X$ required in the tail probability.

A representative-wise Chernoff or factorial-moment argument still needs logarithmic cost

$$
c\log X.
$$

At relative deviation

$$
\delta=X^{-\nu},
$$

the order remains

$$
\boxed{
r
\asymp
\delta^{-1}\log B_{\rm grid}
=
X^\nu(\tau+\nu+o(1))\log X.
}
$$

Hence the polynomial complexity class $X^\nu$ survives inertia compression.

The analysis identifies the only place where a separated family can still help:

> Type-II or other genuinely prime-specific cancellation across the selected family.

To make this precise, define the comparison density

$$
\boxed{
\rho_{\mathcal C}
=
\frac{JH}{X}.
}
$$

On the dyadic ambient interval define

$$
\boxed{
w_{\mathcal C}(n)
=
a_{\mathcal C}(n)
-
\rho_{\mathcal C}
\mathbf1_{[X,2X]}(n).
}
$$

At threshold precision

$$
\delta A_{\mathcal C}
=
JHX^{-\nu},
$$

the aggregate Type-I error condition

$$
JD\ll\delta JH
$$

only reaches

$$
\boxed{
D\ll HX^{-\nu}.
}
$$

Thus the threshold-accurate Type-I exponent is

$$
\boxed{
\gamma_{\rm th}
=
1-\tau-\nu.
}
$$

A power-preserving Vaughan / prime-producing-sieve extraction would therefore require a complementary Type-II range strong enough to bridge the missing width

$$
\boxed{
1-\gamma_{\rm th}
=
\tau+\nu.
}
$$

Open:

```text
F-RH-028+
EXCEPTIONAL_FAMILY_THRESHOLD_TYPE_II
```

Given a maximal separated excess family $\mathcal C$, prove a Type-II estimate for $w_{\mathcal C}$ at relative precision $X^{-\nu}$ over a complementary log-range sufficient to combine with

$$
\gamma_{\rm th}=1-\tau-\nu
$$

in a Vaughan / Heath–Brown / Ford–Maynard prime-producing identity.

A schematic dyadic form is

$$
\boxed{
\left|
\sum_{\substack{m\sim M\\n\sim N\\mn\asymp X}}
\alpha_m\beta_n
w_{\mathcal C}(mn)
\right|
\ll
JH X^{-\nu-\eta}
}
$$

for bounded coefficients in the required balanced ranges.

If such a theorem held with the necessary range geometry, then one could obtain

$$
\sum_n\Lambda(n)a_{\mathcal C}(n)
=
JH
+
O\left(
JHX^{-\nu-\eta'}
\right),
$$

contradicting the defining prime excess of every interval in the family.

No such theorem is currently certified.

The key point is that it is now the only family-specific place where $J$ could provide new cancellation.

Current extremal interval-sieve work provides useful calibration.

Banks, Ford and Tao study extremal interval sieves and show that sieve survivor geometry can be highly nontrivial.

Jha's 2026 Poisson-tail work successfully combines extremal interval sieve estimates with concentration inequalities, but under a strong Hardy–Littlewood hypothesis and in a regime where the interval mean grows slower than every fixed power of $\log X$.

The F-RH regime has

$$
\lambda=X^{1-\tau}/\log X,
$$

and seeks unconditional polynomial relative precision.

Thus those results validate the architecture but do not supply F-RH-028+.

No RH theorem is claimed.

---

# 1. Elementary polynomial-threshold inertia

Let

$$
T=HX^{-\nu}.
$$

For integers $x,y\in[X,2X]$ and fixed $H$,

$$
\begin{aligned}
\Delta_H(y)-\Delta_H(x)
&=
\psi(y+H)-\psi(x+H)
\\
&\quad
-\left(\psi(y)-\psi(x)\right).
\end{aligned}
$$

Each $\psi$ increment over an interval containing at most $|y-x|+1$ integers is bounded by

$$
(|y-x|+1)\log(4X).
$$

Hence:

## Theorem 1.1 — Polynomial-threshold inertia

$$
\boxed{
|\Delta_H(y)-\Delta_H(x)|
\le
2(|y-x|+1)\log(4X).
}
$$

If

$$
\Delta_H(x)>T
$$

and

$$
|y-x|
\le
\frac{T}{8\log(4X)}-1,
$$

then

$$
\boxed{
\Delta_H(y)>\frac{T}{2}.
}
$$

The same holds with both signs reversed.

Create:

```text
B-RH-169
POLYNOMIAL_THRESHOLD_PRIME_INTERVAL_EXCEPTIONS_HAVE_INERTIA_LENGTH_H_X_MINUS_NU_UP_TO_LOGARITHMS
CERTIFIED
```

---

# 2. Relation to classical inertia

Bazzanella and Perelli prove that for fixed relative thresholds

$$
0<\delta'<\delta
$$

with

$$
\delta-\delta'
\ge
e^{-\sqrt{\log X}},
$$

an exceptional point generates an interval of exceptions of length comparable to

$$
(\delta-\delta')H.
$$

For

$$
\delta=X^{-\nu},
$$

the published hypothesis eventually fails.

Theorem 1.1 replaces that input in the present polynomial regime, with only a logarithmic loss.

---

# 3. Maximal separated family

Let

$$
L=HX^{-\nu}(\log X)^{-1}.
$$

Choose a maximal $L$ -separated subset

$$
\mathcal C
=
\{x_1,\ldots,x_J\}
\subset
\mathcal E_\nu^+.
$$

Maximality implies a covering by $O(L)$ neighborhoods.

Therefore:

## Theorem 3.1 — Exceptional mass to center count

$$
\boxed{
|\mathcal E_\nu^+|
\ll
JL.
}
$$

If

$$
|\mathcal E_\nu^+|
\ge
X^{1-c},
$$

then

$$
\boxed{
J\gg
X^{\tau+\nu-c-o(1)}.
}
$$

Create:

```text
B-RH-170
A_FAILURE_OF_THE_ONE_SIDED_EXCEPTIONAL_EXPONENT_FORCES_X_TO_TAU_PLUS_NU_MINUS_C_SEPARATED_EXCESS_CENTERS
CERTIFIED
```

---

# 4. Extraction of disjoint H-scale intervals

Because the centers are $L$ -separated, any interval of length $O(H)$ contains at most

$$
O(H/L)
=
X^{\nu+o(1)}
$$

centers.

A greedy algorithm therefore selects an $H$ -separated subfamily of size

$$
\boxed{
K\gg J\frac{L}{H}.
}
$$

Hence if the exceptional measure is at least $X^{1-c}$,

$$
\boxed{
K\gg X^{\tau-c-o(1)}.
}
$$

Create:

```text
B-RH-171
EXCEPTIONAL_MASS_X_TO_ONE_MINUS_C_FORCES_X_TO_TAU_MINUS_C_DISJOINT_H_SCALE_EXCESS_INTERVALS_WHEN_C_IS_BELOW_TAU
CERTIFIED
```

---

# 5. Strip-dominated versus lag-dominated family geometry

Recall the root forcing exponent

$$
\min(d,\tau).
$$

If $d<\tau$, choose $d<c<\tau$. A failure at exponent $c$ forces polynomially many disjoint intervals.

If $\tau\le d$, every admissible root exponent satisfies $c>\tau$ and the disjoint-family lower bound becomes subconstant.

Create:

```text
O-RH-192
THE_EXTREMAL_DISJOINT_INTERVAL_FAMILY_MECHANISM_IS_INTRINSICALLY_A_STRIP_DOMINATED_D_LESS_THAN_TAU_TOOL
CERTIFIED
```

---

# 6. Compatibility with the Poisson window

The upper-tail concentration window is

$$
d<\nu<\frac{1-\tau}{2}.
$$

Together with $d<\tau$, such parameters exist if and only if

$$
d<\frac13.
$$

Equivalently,

$$
\kappa<\frac23.
$$

---

# 7. The interval-family multiset

Define

$$
a_{\mathcal C}(n)
=
\sum_{j=1}^J
\mathbf1_{(x_j,x_j+H]}(n).
$$

Then

$$
A_{\mathcal C}
=
JH+O(J).
$$

For every modulus $q$,

$$
A_{\mathcal C,q}
=
\sum_j
\left(
\frac{H}{q}+O(1)
\right).
$$

Thus:

## Theorem 7.1 — Family divisor law

$$
\boxed{
A_{\mathcal C,q}
=
\frac{JH}{q}+O(J).
}
$$

Create:

```text
B-RH-172
A_MULTISET_OF_J_LENGTH_H_INTERVALS_HAS_DIVISOR_REMAINDER_O_J_PER_MODULUS_INDEPENDENT_OF_THE_FAMILY_SIZE
CERTIFIED
```

---

# 8. Aggregate Type-I level

For fixed $B$,

$$
\sum_{q\le D}
\tau(q)^B
\left|
A_{\mathcal C,q}
-
\frac{A_{\mathcal C}}q
\right|
\ll
JD(\log D)^{O_B(1)}.
$$

Since

$$
A_{\mathcal C}\asymp JH,
$$

the relative error is

$$
\boxed{
\frac{D}{H}X^{o(1)}.
}
$$

Create:

```text
B-RH-173
THE_DETERMINISTIC_TYPE_I_LEVEL_OF_AN_EXTREMAL_INTERVAL_MULTISET_IS_CONTROLLED_BY_H_NOT_BY_JH
CERTIFIED
```

---

# 9. Brun–Titchmarsh family bound

For

$$
H=X^{1-\tau},
$$

Brun–Titchmarsh gives

$$
\pi(x_j+H)-\pi(x_j)
\le
\frac{2H}{\log H}(1+o(1)).
$$

Therefore

$$
\boxed{
\sum_j
\left(
\pi(x_j+H)-\pi(x_j)
\right)
\le
\left(
\frac{2}{1-\tau}+o(1)
\right)
\frac{JH}{\log X}.
}
$$

The defining excess is only $1+X^{-\nu}$, so the classical family upper sieve leaves a constant gap much larger than the target deviation.

Create:

```text
O-RH-193
SUMMING_BRUN_TITCHMARSH_OVER_AN_EXTREMAL_EXCESS_FAMILY_DOES_NOT_APPROACH_THE_ONE_PLUS_X_MINUS_NU_RESOLUTION
CERTIFIED
```

---

# 10. Linear-sieve interpretation

The dimension-one upper linear sieve has

$$
F(s)=\frac{2e^\gamma}{s}
$$

in the initial range.

With deterministic level $D\lesssim H$ and prime sifting scale $z\asymp X^{1/2}$,

$$
s\lesssim2(1-\tau).
$$

The family size $J$ does not appear.

This is a method-scope result, not an impossibility theorem for added Type-II information.

---

# 11. Inertia grid entropy

The inertia scale is

$$
L=X^{1-\tau-\nu+o(1)}.
$$

Hence

$$
\boxed{
B_{\rm grid}
=
X/L
=
X^{\tau+\nu+o(1)}.
}
$$

The target center count is

$$
J\ll X^{\tau+\nu-c+o(1)}.
$$

Thus the desired exceptional fraction remains

$$
X^{-c+o(1)}.
$$

---

# 12. Resolution order after inertia compression

A near-Poisson representative event with relative deviation $\delta=X^{-\nu}$ still requires order

$$
\delta^{-1}
\log(B_{\rm grid}/J).
$$

At the target fraction,

$$
\log(B_{\rm grid}/J)=c\log X+o(\log X).
$$

Therefore:

## Theorem 12.1 — Inertia does not change the resolution complexity class

$$
\boxed{
r_{\rm grid}\asymp X^\nu\log X.
}
$$

Create:

```text
O-RH-194
INERTIA_COMPRESSES_THE_NUMBER_OF_CANDIDATE_INTERVALS_BUT_DOES_NOT_REMOVE_THE_POLYNOMIAL_X_TO_NU_CONCENTRATION_COMPLEXITY
CERTIFIED
```

---

# 13. Threshold-accurate Type-I level

Prime detection must be accurate to

$$
\delta A_{\mathcal C}
=
JHX^{-\nu}.
$$

The aggregate Type-I error to level $D$ is

$$
JDX^{o(1)}.
$$

Therefore threshold-small Type I only reaches

$$
\boxed{
D\ll HX^{-\nu-o(1)}.
}
$$

Thus

$$
\boxed{
\gamma_{\rm th}=1-\tau-\nu.
}
$$

Create:

```text
B-RH-174
AT_RELATIVE_PRECISION_X_MINUS_NU_THE_EXTREMAL_INTERVAL_SEQUENCE_HAS_DETERMINISTIC_TYPE_I_EXPONENT_ONE_MINUS_TAU_MINUS_NU
CERTIFIED
```

---

# 14. Why a Type-II theorem is the only surviving family-specific leverage

A Vaughan / Heath–Brown identity can preserve fixed-power Type-I / Type-II errors.

But threshold-accurate Type I now reaches only

$$
X^{1-\tau-\nu}.
$$

The complementary logarithmic gap is

$$
\boxed{
\tau+\nu.
}
$$

Thus any threshold-native prime asymptotic for the selected family must obtain genuinely prime-specific balanced information across a substantial complementary product range.

---

# 15. F-RH-028+ — exceptional-family threshold Type II

Let

$$
\rho_{\mathcal C}
=
\frac{JH}{X}
$$

and

$$
w_{\mathcal C}(n)
=
a_{\mathcal C}(n)
-
\rho_{\mathcal C}\mathbf1_{[X,2X]}(n).
$$

Open:

```text
F-RH-028+
EXCEPTIONAL_FAMILY_THRESHOLD_TYPE_II
```

A schematic target is:

for a sufficiently broad balanced range with $MN\asymp X$,

$$
\boxed{
\left|
\sum_{m\sim M}
\sum_{n\sim N}
\alpha_m\beta_n
w_{\mathcal C}(mn)
\right|
\ll
JHX^{-\nu-\eta}
}
$$

for bounded coefficients, uniformly over every maximal separated excess family $\mathcal C$.

If this can be combined with the Type-I exponent $1-\tau-\nu$ in a quantitative prime-producing identity, then

$$
\sum_n\Lambda(n)a_{\mathcal C}(n)
=
JH+O(JHX^{-\nu-\eta'}),
$$

contradicting the defining excess.

No proof is given.

---

# 16. Current extremal-interval literature calibration

Bazzanella and Perelli introduced the inertia and decrease properties of the short-interval PNT exceptional set.

Banks, Ford and Tao show that extremal interval-sieve survivor geometry is nontrivial and cannot be replaced by naive independent Bernoulli heuristics.

Jha's 2026 Poisson-tail work combines extremal interval sieve estimates with concentration inequalities under a strong Hardy–Littlewood hypothesis; its interval mean grows subpolynomially in $\log X$, far below the polynomial mean here.

These works validate the architecture but do not supply F-RH-028+.

---

# 17. Strategic verdict for F-RH-027+

The inertia / maximal-family attack does achieve two things:

1. it turns exceptional measure into the size of a separated structured family;
2. in the strip-dominated regime it produces polynomially many disjoint prime-rich intervals.

But by itself it does not solve the resolution problem.

The two naive routes retain the old complexity:

```text
LOCAL SIEVE:
family size J cancels from the divisor level.

REPRESENTATIVE-WISE CONCENTRATION:
inertia grid still needs X^nu-order resolution.
```

Thus F-RH-027+ survives only through a genuinely new balanced / Type-II theorem for the exceptional family.

---

# 18. State transition

Advance candidate state

$$
v1.78\to v1.79.
$$

Add:

```text
B-RH-169
POLYNOMIAL_THRESHOLD_PRIME_INTERVAL_EXCEPTIONS_HAVE_INERTIA_LENGTH_H_X_MINUS_NU_UP_TO_LOGARITHMS

B-RH-170
A_FAILURE_OF_THE_ONE_SIDED_EXCEPTIONAL_EXPONENT_FORCES_X_TO_TAU_PLUS_NU_MINUS_C_SEPARATED_EXCESS_CENTERS

B-RH-171
EXCEPTIONAL_MASS_X_TO_ONE_MINUS_C_FORCES_X_TO_TAU_MINUS_C_DISJOINT_H_SCALE_EXCESS_INTERVALS_WHEN_C_IS_BELOW_TAU

B-RH-172
A_MULTISET_OF_J_LENGTH_H_INTERVALS_HAS_DIVISOR_REMAINDER_O_J_PER_MODULUS_INDEPENDENT_OF_THE_FAMILY_SIZE

B-RH-173
THE_DETERMINISTIC_TYPE_I_LEVEL_OF_AN_EXTREMAL_INTERVAL_MULTISET_IS_CONTROLLED_BY_H_NOT_BY_JH

B-RH-174
AT_RELATIVE_PRECISION_X_MINUS_NU_THE_EXTREMAL_INTERVAL_SEQUENCE_HAS_DETERMINISTIC_TYPE_I_EXPONENT_ONE_MINUS_TAU_MINUS_NU

O-RH-192
THE_EXTREMAL_DISJOINT_INTERVAL_FAMILY_MECHANISM_IS_INTRINSICALLY_A_STRIP_DOMINATED_D_LESS_THAN_TAU_TOOL

O-RH-193
SUMMING_BRUN_TITCHMARSH_OVER_AN_EXTREMAL_EXCESS_FAMILY_DOES_NOT_APPROACH_THE_ONE_PLUS_X_MINUS_NU_RESOLUTION

O-RH-194
INERTIA_COMPRESSES_THE_NUMBER_OF_CANDIDATE_INTERVALS_BUT_DOES_NOT_REMOVE_THE_POLYNOMIAL_X_TO_NU_CONCENTRATION_COMPLEXITY
```

Open:

```text
F-RH-028+
EXCEPTIONAL_FAMILY_THRESHOLD_TYPE_II
OPEN
```

F-RH-027+ remains open.

No RH certificate is created.

---

# 19. Recommended next action

Attack F-RH-028+.

The next paper should derive an unconditional baseline Type-II estimate for arbitrary separated interval families:

$$
a_{\mathcal C}(n)
=
\sum_j
\mathbf1_{x_j<n\le x_j+H}.
$$

The exact question is:

```text
How small can
sum_{m~M,n~N} alpha_m beta_n
(a_C(mn)-JH/X)
be proved using only:

- separation of x_j;
- interval geometry;
- large-sieve / dispersion methods?

Does any saving improve with J?
```

If the best general bound has no useful $J$ gain, the upper-tail family route reaches a balanced-complexity wall.

If a fixed power of $J$ is gained, there may finally be a genuinely threshold-native upper-tail mechanism.

---

# 20. Conclusion

Polynomial-threshold inertia is available.

It creates clusters of the expected power length.

But cluster multiplicity does not improve the deterministic sieve level.

The family-size factor cancels from local divisor distribution, and the inertia grid does not change the $X^\nu$ concentration complexity class.

The only remaining possible gain from a large exceptional family is balanced multiplicative cancellation.

That is now isolated as F-RH-028+.
