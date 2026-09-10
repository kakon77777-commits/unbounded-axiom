# CSM_RH Paper 66

## Large-Sieve Power Suppression of High-Conductor Major Arcs and the Low-Conductor Character Core

**Project:** CSM_RH  
**Paper:** 66  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Frontier:** F-RH-019 — `AVERAGED_CHARACTER_MAJOR_ARC_POWER_WITHOUT_INDIVIDUAL_FAMILY_STRIPS`  
**Status:** HIGH-CONDUCTOR AVERAGING CERTIFIED / LOW-CONDUCTOR CORE REMAINS OPEN  
**Canonical entry state:** v1.56 / Paper 65 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 65 showed that additive rational frequencies introduce all Dirichlet-character channels and that a PESC seed for the Riemann zeta function controls only the principal channels at fixed-power resolution.

The present paper proves that individual fixed strips are nevertheless unnecessary for polynomially large conductors.

Let

$$
A(\alpha)
=
\sum_{M<n\le M+H}
a_n e(n\alpha)
$$

and let

$$
\mathfrak M_R(K)
$$

be the union of arcs

$$
\left|
\alpha-\frac aq
\right|
\le
\frac{c_0}{RK},
\qquad
R<q\le2R,
\qquad
(a,q)=1.
$$

For each fixed offset $\beta$, the rational points $a/q+\beta$ with $q\sim R$ are $\gg R^{-2}$ separated. The additive large sieve therefore gives

$$
\sum_{R<q\le2R}
\sum_{(a,q)=1}
\left|
A\left(
\frac aq+\beta
\right)
\right|^2
\ll
(H+R^2)
\sum|a_n|^2.
$$

Integrating over the common arc offset yields the dyadic major-arc theorem

$$
\boxed{
\int_{\mathfrak M_R(K)}
|A(\alpha)|^2\,d\alpha
\ll
\frac{H+R^2}{RK}
\sum|a_n|^2.
}
$$

If

$$
K\asymp H
$$

and

$$
R^2\le H,
$$

then

$$
\boxed{
\int_{\mathfrak M_R(K)}
|A(\alpha)|^2\,d\alpha
\ll
\frac1R
\sum|a_n|^2.
}
$$

Thus every denominator block

$$
R=X^u,
\qquad
u>0
$$

carries a genuine fixed-power factor

$$
X^{-u}.
$$

This conclusion is completely independent of zero-free regions for the individual nonprincipal Dirichlet $L$ -functions.

In character language, the saving is the combined effect of:

- Gauss-sum normalization in the additive-to-multiplicative transform;
- rational-arc width;
- family orthogonality / large-sieve dispersion.

Hence F-RH-019 succeeds on all polynomial-conductor major arcs.

The same calculation also identifies its limit.

If

$$
R=X^{o(1)},
$$

the factor

$$
R^{-1}
$$

is only subpower. In particular, for a fixed modulus $q$, a nonprincipal character channel retains fixed positive weight in the major-arc norm.

The PESC seed controls the principal character because

$$
L(s,\chi_0)
=
\zeta(s)
\times
\text{finite Euler factors},
$$

but supplies no fixed zero-free half-plane for a fixed nonprincipal

$$
L(s,\chi).
$$

The classical zero-free region for such a channel still shrinks like a reciprocal logarithm of conductor-height, so its twisted Möbius / prime sums are not known to have a common fixed-power bound.

Therefore family averaging does not eliminate the character barrier. It localizes it:

$$
\boxed{
\text{all polynomial conductors}
\quad\longrightarrow\quad
\text{fixed-power averaged control},
}
$$

while

$$
\boxed{
\text{subpolynomial and fixed conductors}
\quad\longrightarrow\quad
\text{unresolved low-conductor spectral core}.
}
$$

A complementary log-free zero-density calculation confirms this geometry. Jutila's near-one estimate

$$
\sum_{q\le Q}
\sum_{\chi\bmod q}^{*}
N(\sigma,T,\chi)
\ll
(Q^2T)^{(2+o(1))(1-\sigma)}
$$

implies that, in a dyadic conductor block

$$
R=X^u
$$

and height

$$
T=X^v,
$$

the conductor-weighted count of channels with a zero to the right of

$$
\sigma=1-\delta
$$

has schematic exponent

$$
\boxed{
-u+2\delta(2u+v).
}
$$

For

$$
\delta<\frac14
$$

this becomes power-small once

$$
u>
\frac{2\delta v}{1-4\delta}.
$$

Again, zero-density averaging becomes effective only after a positive conductor exponent is present. It does not resolve the $u=0$ core.

The paper therefore partially closes F-RH-019:

```text
HIGH-CONDUCTOR MAJOR-ARC AVERAGING:
CERTIFIED AT FIXED POWER.

LOW-CONDUCTOR NONPRINCIPAL CORE:
OPEN.
```

The next useful theorem must either annihilate the low-conductor nonprincipal channels in the ordinary shifted-prime observable or prove a fixed-power averaged estimate for them without requiring individual Dirichlet- $L$ strips.

No RH theorem is claimed.

---

# 1. Dyadic rational major arcs

Let

$$
A(\alpha)
=
\sum_{M<n\le M+H}
a_n e(n\alpha),
$$

where

$$
e(x)=e^{2\pi ix}.
$$

Fix

$$
R\ge1,
\qquad
K\ge1.
$$

Define the dyadic major-arc set

$$
\boxed{
\mathfrak M_R(K)
=
\bigcup_{\substack{R<q\le2R\\(a,q)=1}}
\left\{
\alpha:
\left|
\alpha-\frac aq
\right|
\le
\frac{c_0}{RK}
\right\},
}
$$

where $c_0>0$ is a sufficiently small absolute constant.

The exact value of $c_0$ is immaterial for exponent bookkeeping.

---

# 2. Farey separation

If

$$
\frac aq\ne\frac{a'}{q'}
$$

with

$$
R<q,q'\le2R,
$$

then

$$
\left|
\frac aq-\frac{a'}{q'}
\right|
\ge
\frac1{qq'}
\ge
\boxed{
\frac1{4R^2}.
}
$$

Thus, for every fixed real $\beta$, the translated set

$$
\left\{
\frac aq+\beta:
R<q\le2R,
(a,q)=1
\right\}
$$

has the same separation.

---

# 3. Additive large-sieve input

The additive large sieve gives, for a $\delta$ -separated set of frequencies,

$$
\sum_r
\left|
\sum_{M<n\le M+H}
a_ne(n\alpha_r)
\right|^2
\ll
\left(
H+\delta^{-1}
\right)
\sum|a_n|^2.
$$

With

$$
\delta^{-1}\ll R^2,
$$

we obtain:

## Theorem 3.1 — Dyadic rational-point large sieve

For every real $\beta$,

$$
\boxed{
\sum_{R<q\le2R}
\sum_{(a,q)=1}
\left|
A\left(
\frac aq+\beta
\right)
\right|^2
\ll
(H+R^2)
\sum|a_n|^2.
}
$$

The implicit constant is absolute.

External calibration: this is the standard additive large-sieve theorem applied to Farey fractions.

---

# 4. Integrated dyadic major-arc theorem

Integrate Theorem 3.1 over

$$
|\beta|
\le
\frac{c_0}{RK}.
$$

By nonnegativity,

$$
\begin{aligned}
\int_{\mathfrak M_R(K)}
|A(\alpha)|^2d\alpha
&\le
\int_{|\beta|\le c_0/(RK)}
\sum_{q\sim R}
\sum_{(a,q)=1}
\left|
A\left(
\frac aq+\beta
\right)
\right|^2
d\beta.
\end{aligned}
$$

Therefore:

## Theorem 4.1 — High-conductor major-arc $L^2$ suppression

$$
\boxed{
\int_{\mathfrak M_R(K)}
|A(\alpha)|^2d\alpha
\ll
\frac{
H+R^2
}{
RK
}
\sum|a_n|^2.
}
$$

Create:

```text
B-RH-084
DYADIC_HIGH_CONDUCTOR_ADDITIVE_MAJOR_ARC_L2_SUPPRESSION
CERTIFIED
```

No Dirichlet- $L$ zero-free information enters this theorem.

---

# 5. Polynomial-conductor fixed power

Take

$$
K\asymp H.
$$

If

$$
R^2\le H,
$$

then

$$
H+R^2\ll H.
$$

Hence:

## Corollary 5.1

$$
\boxed{
\int_{\mathfrak M_R(H)}
|A(\alpha)|^2d\alpha
\ll
R^{-1}
\sum|a_n|^2.
}
$$

If

$$
R=X^u,
\qquad
u>0,
$$

then

$$
\boxed{
\int_{\mathfrak M_R(H)}
|A|^2
\ll
X^{-u}
\sum|a_n|^2.
}
$$

This is a genuine fixed-power family average.

Create:

```text
B-RH-085
POLYNOMIAL_CONDUCTOR_MAJOR_ARCS_HAVE_ZERO_FREE_REGION_INDEPENDENT_POWER_SAVING
CERTIFIED
```

---

# 6. Character interpretation

For a rational frequency

$$
\frac aq
$$

with $(a,q)=1$, the additive phase on integers coprime to $q$ admits a Dirichlet-character expansion.

Schematically,

$$
e(an/q)
=
\frac1{\phi(q)}
\sum_{\chi\bmod q}
\tau(\overline\chi)
\chi(a)\chi(n)
$$

with the usual primitive / induced-character bookkeeping.

For primitive characters,

$$
|\tau(\chi)|^2=q.
$$

After summing over reduced residues $a$ and using character orthogonality, the total squared additive mass becomes a weighted character mean square.

The factor $R^{-1}$ in Corollary 5.1 is therefore the additive formulation of:

```text
Gauss normalization
+
character orthogonality
+
arc-width dilution.
```

Thus the result is precisely the kind of averaged-character mechanism sought in F-RH-019.

---

# 7. The low-conductor floor

The gain in Corollary 5.1 is

$$
R^{-1}.
$$

If

$$
R=X^{o(1)},
$$

then

$$
R^{-1}=X^{-o(1)}.
$$

For fixed $R$ it is merely a constant.

Therefore:

## Theorem 7.1 — Large-sieve conductor floor

Large-sieve averaging alone does not provide a fixed power on the union of fixed or subpolynomial denominator major arcs.

Create:

```text
O-RH-154
AVERAGED_CHARACTER_LARGE_SIEVE_HAS_A_LOW_CONDUCTOR_FIXED_POWER_FLOOR
CERTIFIED
```

This is not a defect of the large sieve. It is the correct scaling of the family size.

---

# 8. Principal channels are already seeded

Let

$$
\chi_0\bmod q
$$

be principal.

Paper 65 certified

$$
L(s,\chi_0)
=
\zeta(s)
\prod_{p\mid q}
(1-p^{-s}),
$$

so PESC $(\kappa)$ gives principal-character fixed-power cancellation at exponent resolution.

Hence the low-conductor obstruction is entirely nonprincipal.

We may record:

```text
LOW CONDUCTOR PRINCIPAL:
CONTROLLED BY ZETA SEED.

LOW CONDUCTOR NONPRINCIPAL:
NOT CONTROLLED AT FIXED POWER.
```

---

# 9. Why a fixed nonprincipal channel is not automatically harmless

For a fixed nonprincipal character $\chi$, the best general zero-free region has logarithmically shrinking width as the height grows.

Thus current unconditional theory gives strong subpower cancellation in twisted Mertens / prime sums, but not a uniform fixed exponent which can be inserted into F-RH-017-v3.

If a sequence of zeros of $L(s,\chi)$ approached $\Re s=1$ within the classical allowed region, its twisted low-frequency channel would remain only subpower-suppressed.

The zeta seed says nothing about this possibility.

Thus the low-conductor floor is spectral, not merely combinatorial.

---

# 10. Zero-density calibration

Let

$$
N(\sigma,T,\chi)
$$

count zeros of

$$
L(s,\chi)
$$

with

$$
\Re\rho\ge\sigma,
\qquad
|\Im\rho|\le T.
$$

A classical near-one zero-density theorem of Jutila gives, for

$$
\frac45\le\sigma\le1,
$$

$$
\boxed{
\sum_{q\le Q}
\sum_{\chi\bmod q}^{*}
N(\sigma,T,\chi)
\ll
(Q^2T)^{(2+o(1))(1-\sigma)}.
}
$$

Let

$$
\sigma=1-\delta,
$$

$$
R=X^u,
\qquad
T=X^v.
$$

In a dyadic conductor block $q\sim R$, the number of bad primitive character-zero incidences is bounded at exponent level by

$$
X^{2\delta(2u+v)+o(1)}.
$$

The additive major-arc character weight / arc-width supplies an effective conductor factor of order $R^{-1}$.

Therefore the weighted bad-channel count has schematic exponent

$$
\boxed{
-u+2\delta(2u+v).
}
$$

If

$$
\delta<\frac14
$$

and

$$
\boxed{
u>
\frac{
2\delta v
}{
1-4\delta
},
}
$$

this quantity is power-small.

This is only a spectral-count calibration, not a complete major-arc amplitude theorem.

Its purpose is to show that log-free zero density agrees with the large-sieve geometry: averaging becomes effective after a positive conductor exponent appears.

---

# 11. Why zero density still leaves $u=0$

At

$$
u=0,
$$

the preceding exponent becomes

$$
2\delta v>0.
$$

No conductor-weight saving remains.

Thus zero-density estimates allow many zero incidences over growing heights even for a fixed small conductor family.

They do not prove that a fixed nonprincipal $L$ -function has a fixed zero-free half-plane.

Hence zero-density averaging does not remove the low-conductor core.

---

# 12. Consequence for shifted-prime Möbius major arcs

Lichtman's current major-arc proof takes

$$
q\le W
$$

and controls every character individually.

F-RH-019 proposed replacing this worst-case treatment by an averaged norm.

Theorem 5.1 proves that this replacement is effective for every dyadic range

$$
q\asymp X^u,
\qquad
u>0.
$$

Therefore a redesigned shifted-prime proof need not solve the entire polynomial conductor family.

It only needs a separate treatment of the low-conductor region.

This is a real reduction of the family barrier.

---

# 13. Why summing the dyadic bounds does not finish the problem

Summing

$$
R^{-1}
$$

over dyadic

$$
1\le R\le X^w
$$

gives a series dominated by the first few denominator blocks.

Thus the total major-arc bound is controlled by low conductors.

Choosing a fixed lower cutoff

$$
R\ge X^{u_0}
$$

gives the clean power

$$
X^{-u_0}.
$$

But the omitted range

$$
q<X^{u_0}
$$

still contains nonprincipal character channels with no seed fixed strip.

Letting

$$
u_0\to0
$$

destroys the fixed power.

This is the exact remaining F-RH-019 gap.

---

# 14. Partial closure of F-RH-019

Record:

```text
F-RH-019/HIGH
AVERAGED POLYNOMIAL-CONDUCTOR MAJOR-ARC POWER
CLOSED / CERTIFIED

F-RH-019/LOW
LOW-CONDUCTOR NONPRINCIPAL MAJOR-ARC POWER
OPEN
```

The original frontier is therefore partially closed.

It should no longer be described as a full polynomial Dirichlet- $L$ family problem.

The unresolved part is localized near conductor exponent zero.

---

# 15. Next arithmetic target

The next target is:

```text
PT6F
LOW-CONDUCTOR NONPRINCIPAL CHARACTER ANNIHILATION
```

Desired outcome:

a fixed-power estimate for the contribution of

$$
q\le X^{u_0}
$$

for some small fixed $u_0>0$ which:

- does not assume a fixed zero-free strip for every nonprincipal $L(s,\chi)$ ;
- exploits the shifted-prime / ordinary-integer observable;
- combines with B-RH-085 on $q\ge X^{u_0}$.

Possible mechanisms:

1. algebraic cancellation of nonprincipal low-conductor channels in the prime-shift average;
2. a dispersion identity in which principal terms survive but nonprincipal low- $q$ terms enter quadratically and can be large-sieved;
3. a signed average over shifts or residue classes which kills fixed low-conductor characters before absolute values are taken;
4. a new low-conductor bilinear theorem.

No theorem is claimed.

---

# 16. External calibration

## 16.1. Additive and multiplicative large sieve

The additive large sieve over Farey fractions gives

$$
\sum_{q\le Q}
\sum_{(a,q)=1}
\left|
\sum a_ne(an/q)
\right|^2
\ll
(Q^2+H)
\sum|a_n|^2.
$$

The multiplicative form gives

$$
\sum_{q\le Q}
\frac{q}{\phi(q)}
\sum_{\chi\bmod q}^{*}
\left|
\sum a_n\chi(n)
\right|^2
\ll
(Q^2+H)
\sum|a_n|^2.
$$

These are standard large-sieve inequalities.

## 16.2. Jutila zero density

For

$$
4/5\le\sigma\le1,
$$

Jutila proved

$$
\sum_{q\le Q}
\sum_{\chi\bmod q}^{*}
N(\sigma,T,\chi)
\ll_\varepsilon
(Q^2T)^{(2+\varepsilon)(1-\sigma)}.
$$

This is used only for family-size calibration.

---

# 17. State transition

Advance the candidate state from

$$
v1.56
$$

to

$$
v1.57.
$$

Add:

```text
B-RH-084
DYADIC_HIGH_CONDUCTOR_ADDITIVE_MAJOR_ARC_L2_SUPPRESSION
CERTIFIED
```

Add:

```text
B-RH-085
POLYNOMIAL_CONDUCTOR_MAJOR_ARCS_HAVE_ZERO_FREE_REGION_INDEPENDENT_POWER_SAVING
CERTIFIED
```

Add:

```text
O-RH-154
AVERAGED_CHARACTER_LARGE_SIEVE_HAS_A_LOW_CONDUCTOR_FIXED_POWER_FLOOR
CERTIFIED
```

Update F-RH-019:

```text
HIGH-CONDUCTOR PART CLOSED
LOW-CONDUCTOR CORE OPEN
```

Open:

```text
PT6F
LOW-CONDUCTOR NONPRINCIPAL CHARACTER ANNIHILATION
```

No RH certificate is created.

---

# 18. Conclusion

Averaging over character channels works.

For polynomial conductor blocks it works extremely cleanly:

$$
\boxed{
q\asymp X^u
\quad\Rightarrow\quad
X^{-u}
\text{ major-arc }L^2\text{ saving}.
}
$$

No individual Dirichlet- $L$ zero-free region is required.

Thus the family barrier of Paper 65 was too broad.

The real unresolved set is the low-conductor core.

There, the family is too small for large-sieve dilution to create a fixed power, while the zeta seed controls only the principal characters.

The next problem is therefore finite-/subpolynomial-conductor nonprincipal annihilation, not polynomial-family GRH.
