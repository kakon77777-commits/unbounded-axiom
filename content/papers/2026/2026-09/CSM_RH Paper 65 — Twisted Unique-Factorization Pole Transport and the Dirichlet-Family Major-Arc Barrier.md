# CSM_RH Paper 65

## Twisted Unique-Factorization Pole Transport and the Dirichlet-Family Major-Arc Barrier

**Project:** CSM_RH  
**Paper:** 65  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Track:** PT6E — `ORDINARY_INTEGER_FACTORIZATION_ADDITIVE_LATTICE_LOW_FREQUENCY_EXCESS`  
**Status:** EXACT FACTORIZATION SELF-AMPLIFICATION REJECTED / PRINCIPAL-CHARACTER SEED LIFT CERTIFIED / NONPRINCIPAL FAMILY BARRIER IDENTIFIED  
**Canonical entry state:** v1.55 / Paper 64 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 64 isolated the remaining low-frequency problem as a genuinely ordinary-arithmetic interaction between the additive integer lattice and exact multiplicative factorization.

The present paper tests the most direct such mechanism:

$$
\Lambda=\mu*\log.
$$

The result is exact and negative.

The Dirichlet series are

$$
\sum_{n\ge1}\frac{\mu(n)}{n^s}
=
\frac1{\zeta(s)},
$$

$$
\sum_{n\ge1}\frac{\log n}{n^s}
=
-\zeta'(s),
$$

and therefore ordinary unique factorization gives

$$
\boxed{
\Lambda=\mu*\log
}
$$

together with

$$
\boxed{
\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=
-\frac{\zeta'(s)}{\zeta(s)}.
}
$$

If

$$
\rho
$$

is a zero of $\zeta$ of multiplicity $m$, write

$$
\zeta(s)
=
(s-\rho)^m g(s),
\qquad
g(\rho)\ne0.
$$

Then

$$
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=
-\frac{m}{s-\rho}
-
\frac{g'(s)}{g(s)}.
}
$$

Thus the pole of $1/\zeta$ carried by the Möbius channel is not damped by convolution with $\log$. The zero of $-\zeta'$ cancels exactly $m-1$ of the $m$ pole orders, leaving the universal simple pole required by the von Mangoldt channel.

The same phenomenon persists after additive-lattice decomposition into Dirichlet characters.

For any Dirichlet character $\chi$,

$$
\boxed{
\chi\Lambda
=
(\chi\mu)*(\chi\log)
}
$$

and

$$
\boxed{
\sum_{n\ge1}
\frac{\chi(n)\Lambda(n)}{n^s}
=
-\frac{L'(s,\chi)}{L(s,\chi)}.
}
$$

Every zero of $L(s,\chi)$ is therefore transported to a simple pole of the twisted von Mangoldt series with its multiplicity as residue. Exact factorization is pole-preserving in every character channel.

This identifies a major structural consequence for PT6E.

The PESC seed

$$
\beta_*(\zeta)
\le
1-d,
\qquad
d=\frac{\kappa}{2},
$$

automatically lifts to every principal Dirichlet character

$$
\chi_0\pmod q,
$$

because

$$
L(s,\chi_0)
=
\zeta(s)
\prod_{p\mid q}
(1-p^{-s}).
$$

Thus, uniformly at exponent resolution for polynomially bounded $q$, principal-character Möbius sums inherit the same fixed-power cancellation.

However, the additive major arcs in ordinary shifted-prime problems contain all Dirichlet characters, not only the principal one.

Lichtman's proof of averaged Möbius cancellation on shifted primes makes this explicit. Its major-arc proposition requires twisted Liouville / Möbius estimates for every

$$
\chi\pmod q,
\qquad
q\le W,
$$

and the key prime Dirichlet-polynomial lemma is proved by replacing the zeta Vinogradov-Korobov zero-free region with the zero-free region of

$$
L(s,\chi).
$$

The published theorem therefore takes only

$$
W=(\log X)^A.
$$

If one tries to upgrade the Fourier saving to a fixed power by taking

$$
W=X^w,
$$

the principal-character pieces are improved by the PESC seed, but the nonprincipal major arcs immediately require fixed-power zero-free information for the Dirichlet $L$ -functions of conductor up to $X^w$.

The zeta seed supplies no such family-wide strip.

This is not merely a technical mismatch. A zero of a nonprincipal $L(s,\chi)$ produces a pole in the twisted Möbius channel and, by the exact twisted convolution identity above, is transmitted into the twisted prime channel. The additive-multiplicative decomposition therefore imports new spectral boundaries instead of averaging them away automatically.

The paper consequently separates two notions:

```text
ordinary factorization:
exactly relates Möbius and primes,
but preserves every Mellin pole.

ordinary additive lattice:
creates character twists,
but therefore introduces an L-function family.

their naive combination:
does not self-amplify the zeta seed.
```

The standard shifted-prime Möbius theorem is still highly relevant as evidence of genuine ordinary-arithmetic decorrelation. It proves logarithmic cancellation averaged over shifts. But its current circle-method proof cannot be turned into a polynomial PESC amplifier by inserting only a zeta seed.

A new frontier is therefore opened:

```text
F-RH-019
AVERAGED CHARACTER MAJOR-ARC POWER WITHOUT INDIVIDUAL FAMILY STRIPS
```

The target is not to prove a fixed zero-free strip for every Dirichlet $L$ -function. It is to exploit averaging over additive frequencies, moduli, or shifts strongly enough to obtain a fixed-power prime-side estimate while allowing a sparse set of bad nonprincipal characters.

This is the first PT6E route which genuinely uses both ordinary additive and multiplicative structure without simply replacing RH by a family-GRH problem.

No RH theorem is claimed.

---

# 1. Exact ordinary factorization identity

For every positive integer $n$,

$$
\boxed{
\Lambda(n)
=
\sum_{d\mid n}
\mu(d)
\log\frac{n}{d}.
}
$$

Equivalently,

$$
\boxed{
\Lambda
=
\mu*\log.
}
$$

At the Dirichlet-series level,

$$
\sum_{n\ge1}
\frac{\mu(n)}{n^s}
=
\frac1{\zeta(s)}
$$

and

$$
\sum_{n\ge1}
\frac{\log n}{n^s}
=
-\zeta'(s).
$$

Multiplication gives

$$
\boxed{
\frac1{\zeta(s)}
\left(
-\zeta'(s)
\right)
=
-\frac{\zeta'(s)}{\zeta(s)}.
}
$$

This identity is exact.

---

# 2. Boundary pole transport

Let $\rho$ be a zeta zero of multiplicity $m$.

Write

$$
\boxed{
\zeta(s)
=
(s-\rho)^m g(s),
\qquad
g(\rho)\ne0.
}
$$

Then

$$
\frac1{\zeta(s)}
=
(s-\rho)^{-m}g(s)^{-1}.
$$

Differentiate:

$$
\zeta'(s)
=
m(s-\rho)^{m-1}g(s)
+
(s-\rho)^m g'(s).
$$

Therefore

$$
\begin{aligned}
-\frac{\zeta'(s)}{\zeta(s)}
&=
-
\frac{
m(s-\rho)^{m-1}g(s)
+
(s-\rho)^m g'(s)
}{
(s-\rho)^m g(s)
}
\\
&=
\boxed{
-\frac{m}{s-\rho}
-
\frac{g'(s)}{g(s)}.
}
\end{aligned}
$$

Thus:

## Theorem 2.1 — Unique-factorization zero-pole transport

Every zeta zero of multiplicity $m$ produces a simple pole of the von Mangoldt Dirichlet series with residue $-m$.

The Möbius pole is not canceled by the exact convolution identity.

Create:

```text
O-RH-151
EXACT_MOBIUS_LOG_FACTORIZATION_PRESERVES_THE_ZETA_BOUNDARY_POLE
CERTIFIED_AS_METHOD_BARRIER
```

This explains why seed Mertens cancellation cannot be fed through $\Lambda=\mu*\log$ to obtain a stronger PNT exponent by formal factorization alone.

---

# 3. Short-interval interpretation

The seed boundary mode in the prime error has relative short-interval scale

$$
H X^{-d}.
$$

The same zeta zero is also a singularity of

$$
1/\zeta(s),
$$

and therefore generates a corresponding Mertens oscillation.

The exact identity

$$
\Lambda=\mu*\log
$$

recombines the Möbius singularity into the universal simple pole of

$$
-\zeta'/\zeta.
$$

Hence any Dirichlet-hyperbola decomposition of the short-interval von Mangoldt sum which uses only:

- the seed Mertens power bound;
- the smooth logarithm factor; and
- deterministic divisor splitting

must retain a boundary contribution at the seed exponent.

This is the multiplicative counterpart of Papers 54–55's critical locking.

---

# 4. Character-twisted exact factorization

Let

$$
\chi
$$

be any Dirichlet character modulo $q$.

By complete multiplicativity,

$$
\chi(d)\chi(n/d)=\chi(n)
$$

whenever $d\mid n$.

Therefore

$$
\begin{aligned}
((\mu\chi)*(\chi\log))(n)
&=
\sum_{d\mid n}
\mu(d)\chi(d)
\chi(n/d)
\log(n/d)
\\
&=
\chi(n)
\sum_{d\mid n}
\mu(d)\log(n/d)
\\
&=
\boxed{
\chi(n)\Lambda(n).
}
\end{aligned}
$$

Thus:

## Theorem 4.1 — Twisted unique-factorization identity

$$
\boxed{
\chi\Lambda
=
(\chi\mu)*(\chi\log).
}
$$

At the Dirichlet-series level,

$$
\boxed{
\sum_{n\ge1}
\frac{\mu(n)\chi(n)}{n^s}
=
\frac1{L(s,\chi)}
}
$$

and

$$
\boxed{
\sum_{n\ge1}
\frac{\chi(n)\Lambda(n)}{n^s}
=
-\frac{L'(s,\chi)}{L(s,\chi)}.
}
$$

Create:

```text
B-RH-082
TWISTED_ORDINARY_FACTORIZATION_IDENTITY_FOR_MOBIUS_AND_VON_MANGOLDT
CERTIFIED
```

---

# 5. Twisted pole transport

Suppose

$$
L(s,\chi)
=
(s-\rho)^m g_\chi(s),
\qquad
g_\chi(\rho)\ne0.
$$

Then exactly as in Section 2,

$$
\boxed{
-\frac{L'(s,\chi)}{L(s,\chi)}
=
-\frac{m}{s-\rho}
-
\frac{g_\chi'(s)}{g_\chi(s)}.
}
$$

Hence:

## Corollary 5.1 — Character-channel pole preservation

Every zero of every Dirichlet $L$ -function is transported through the twisted Möbius/log factorization into the corresponding twisted von Mangoldt channel.

Create:

```text
O-RH-152
ADDITIVE_CHARACTER_TWIST_PLUS_EXACT_FACTORIZATION_PRESERVES_L_FUNCTION_BOUNDARY_POLES
CERTIFIED
```

This is the basic spectral reason that introducing additive congruence structure creates new boundary channels rather than removing the original one.

---

# 6. Principal-character seed lift

Let

$$
\chi_0
$$

be the principal character modulo $q$.

Then

$$
\boxed{
L(s,\chi_0)
=
\zeta(s)
\prod_{p\mid q}
(1-p^{-s}).
}
$$

The finite Euler product has zeros only on the line

$$
\Re s=0.
$$

Therefore the nontrivial zero set in the critical strip is exactly the zeta zero set.

If PESC $(\kappa)$ gives

$$
\zeta(s)\ne0
\qquad
\Re s>1-d,
$$

then every principal $L(s,\chi_0)$ has the same fixed zero-free half-plane.

Moreover,

$$
\boxed{
\frac1{L(s,\chi_0)}
=
\frac1{\zeta(s)}
\prod_{p\mid q}
(1-p^{-s})^{-1}.
}
$$

For every fixed

$$
\sigma>1-d
$$

and polynomially bounded

$$
q\le X^w,
$$

the finite Euler product contributes only

$$
X^{o(1)}
$$

at exponent resolution.

Thus standard Perron shifting gives:

## Theorem 6.1 — Principal-character seeded Möbius power cancellation

For every fixed $\varepsilon>0$ and fixed $w>0$,

$$
\boxed{
\sum_{\substack{n\le X\\(n,q)=1}}
\mu(n)
\ll
X^{1-d+\varepsilon+o(1)}
}
$$

uniformly at exponent resolution for

$$
q\le X^w,
$$

subject only to the harmless finite Euler-factor loss.

Create:

```text
B-RH-083
PESC_SEED_LIFTS_TO_PRINCIPAL_DIRICHLET_CHARACTER_FIXED_POWER_CANCELLATION
CERTIFIED_AT_EXPONENT_RESOLUTION
```

The same statement applies to principal-character prime sums through the PNT seed.

---

# 7. Shifted-prime Möbius cancellation is genuinely ordinary arithmetic

Lichtman proves, for

$$
H=X^\theta,
\qquad
0<\theta<1,
$$

the averaged shifted-prime estimate

$$
\boxed{
\sum_{h\le H}
\left|
\sum_{p\le X}
\mu(p+h)
\right|
\ll_{\theta,\delta}
\frac{
H\pi(X)
}{
(\log X)^{1/3-\delta}
}.
}
$$

This correlation is genuinely unavailable from either model class in Paper 64 alone.

It simultaneously tests:

- ordinary primes $p$ ;
- additive shifts $p+h$ ;
- ordinary integer factorization through $\mu(p+h)$.

Thus it is a natural PT6E observable.

External source:

M. Lichtman,
*Averages of the Möbius Function on Shifted Primes*,
Quarterly Journal of Mathematics 73 (2022), 729–757.

---

# 8. Fourier decoupling and the major-arc family

The shifted-prime proof reduces the correlation to a Fourier estimate for Möbius:

$$
\boxed{
\sup_\alpha
\int_0^X
\left|
\sum_{x<n\le x+H}
\mu(n)e(n\alpha)
\right|
dx.
}
$$

The proof splits $\alpha$ into rational major and minor arcs according to

$$
\alpha\approx \frac aq.
$$

Its major-arc proposition treats

$$
q\le W
$$

and expands the twisted multiplicative sums into Dirichlet characters modulo $q$.

The key prime Dirichlet-polynomial lemma is stated for every

$$
\chi\pmod q,
\qquad
q\le(\log X)^A,
$$

and its proof explicitly replaces the Vinogradov-Korobov zero-free region for $\zeta$ by that for

$$
\boxed{
L(s,\chi).
}
$$

Therefore the major arcs are genuinely an $L$ -function family problem.

---

# 9. Why a zeta seed upgrades only the principal part

Suppose one attempts to replace

$$
W=(\log X)^A
$$

by

$$
W=X^w.
$$

For the principal characters modulo $q\le W$, Theorem 6.1 supplies a fixed-power seed.

For nonprincipal characters, the relevant Dirichlet series are

$$
\frac1{L(s,\chi)}
$$

and

$$
-\frac{L'(s,\chi)}{L(s,\chi)}.
$$

PESC $(\kappa)$ contains no information about their rightmost zeros.

The classical uniform zero-free region for conductors growing with $X$ is only logarithmic in the conductor and height.

Hence the existing major-arc proof cannot promote the nonprincipal pieces to a common fixed-power exponent.

Create:

```text
O-RH-153
SHIFTED_PRIME_MOBIUS_MAJOR_ARCS_REQUIRE_NONPRINCIPAL_DIRICHLET_L_FAMILY_CONTROL
CERTIFIED_AS_METHOD_BARRIER
```

This does not rule out a different averaged-major-arc proof.

It rules out the naive plan:

```text
insert zeta PESC seed
and replace every log-power W by polynomial W
inside the existing proof.
```

---

# 10. The family barrier is spectral, not merely technical

Suppose a nonprincipal

$$
L(s,\chi)
$$

has a zero

$$
\rho_\chi
$$

close to its allowed right boundary.

Then

$$
1/L(s,\chi)
$$

has a pole there.

By Corollary 5.1, the twisted von Mangoldt series has the matching simple pole.

Thus a character major arc can carry its own slowly varying boundary packet independently of the zeta boundary.

The zeta seed cannot suppress this packet because it belongs to a different $L$ -function.

Therefore the nonprincipal obstruction is not just a missing uniform constant in an estimate.

It is a genuine new spectral channel.

---

# 11. Why demanding individual fixed strips is strategically expensive

One possible response would be to assume or prove

$$
L(s,\chi)\ne0
\qquad
\Re s>1-\delta
$$

uniformly for every

$$
q\le X^w
$$

and every character modulo $q$.

But this upgrades the original zeta problem into a broad Dirichlet- $L$ family problem.

Such a theorem is substantially stronger than the input PESC seed and approaches a family-GRH style task as $\delta\to1/2$.

PT6E should therefore not adopt individual family strips as its default route.

The desired new theorem should exploit averaging in the additive variable or character family.

---

# 12. Existing shifted-prime power saving remains logarithmic

Lichtman's theorem gives arbitrary qualitative cancellation and the quantitative power

$$
(\log X)^{-1/3+\delta}
$$

for polynomial shift ranges.

The stronger higher-correlation theorem gives larger logarithmic powers when more Möbius factors are averaged, but remains logarithmic.

This is consistent with the character-family audit:

the existing proof has enough family zero-free information for arbitrary logarithmic savings in the Siegel-Walfisz range, not for a common fixed power at polynomial conductor.

Thus the shifted-prime observable is structurally promising but not yet a PESC amplifier.

---

# 13. A principal-only power improvement does not control the Fourier supremum

The seed can improve the additive frequency

$$
\alpha=0
$$

and, more generally, the principal-character component of rational major arcs.

However the shifted-prime decoupling uses

$$
\boxed{
\sup_\alpha.
}
$$

A single nonprincipal major arc with only logarithmic control determines the supremum.

Therefore principal-character fixed-power cancellation alone does not upgrade the final shifted-prime theorem.

This is another form of the same family barrier.

---

# 14. New frontier: averaged-character major-arc power

Open:

```text
F-RH-019
AVERAGED_CHARACTER_MAJOR_ARC_POWER_WITHOUT_INDIVIDUAL_FAMILY_STRIPS
```

Desired architecture:

1. retain the ordinary shifted-prime / Möbius observable;
2. replace the worst-case major-arc supremum by an averaged character or averaged rational-frequency norm;
3. use large-sieve / dispersion / additive-shift averaging to tolerate a sparse set of bad nonprincipal characters;
4. retain a fixed power after the averaging;
5. feed the resulting prime-side estimate into F-RH-017-v3 or another certified amplifier.

The goal is explicitly **not** to prove a fixed strip for every Dirichlet $L$ -function.

This is the natural PT6E continuation.

---

# 15. Relation to the sieve parity problem

Friedlander and Iwaniec's asymptotic sieve breaks the classical parity problem by adding a genuinely bilinear axiom.

This is useful methodological calibration.

The current PT6E audit reaches an analogous conclusion:

- exact Möbius inversion does not break the boundary pole;
- rough sieve structure does not break it;
- ordinary additive shifts introduce character families;
- a new averaged bilinear / dispersion principle is required to extract a power without solving every twisted $L$ -function separately.

No claim is made that the classical asymptotic sieve theorem directly proves the desired CSM_RH estimate.

---

# 16. External calibration

## 16.1. Shifted-prime Möbius theorem

M. Lichtman,
*Averages of the Möbius Function on Shifted Primes*,
Quarterly Journal of Mathematics 73 (2022), 729–757.

For $H=X^\theta$,

$$
\sum_{h\le H}
\left|
\sum_{p\le X}\mu(p+h)
\right|
\ll
H\pi(X)(\log X)^{-1/3+\delta}.
$$

The major-arc proof uses Dirichlet characters and a zero-free region for $L(s,\chi)$.

## 16.2. Asymptotic sieve parity breaking

J. Friedlander and H. Iwaniec,
*Asymptotic sieve for primes*.

Their framework breaks the classical sieve parity obstruction by imposing an additional bilinear axiom.

The broad lesson is that genuine parity-breaking requires extra bilinear information rather than formal Möbius inversion alone.

---

# 17. State transition

Advance the candidate state from

$$
v1.55
$$

to

$$
v1.56.
$$

Add:

```text
B-RH-082
TWISTED_ORDINARY_FACTORIZATION_IDENTITY_FOR_MOBIUS_AND_VON_MANGOLDT
CERTIFIED
```

Add:

```text
B-RH-083
PESC_SEED_LIFTS_TO_PRINCIPAL_DIRICHLET_CHARACTER_FIXED_POWER_CANCELLATION
CERTIFIED_AT_EXPONENT_RESOLUTION
```

Add:

```text
O-RH-151
EXACT_MOBIUS_LOG_FACTORIZATION_PRESERVES_THE_ZETA_BOUNDARY_POLE
CERTIFIED_AS_METHOD_BARRIER
```

Add:

```text
O-RH-152
ADDITIVE_CHARACTER_TWIST_PLUS_EXACT_FACTORIZATION_PRESERVES_L_FUNCTION_BOUNDARY_POLES
CERTIFIED
```

Add:

```text
O-RH-153
SHIFTED_PRIME_MOBIUS_MAJOR_ARCS_REQUIRE_NONPRINCIPAL_DIRICHLET_L_FAMILY_CONTROL
CERTIFIED_AS_METHOD_BARRIER
```

Open:

```text
F-RH-019
AVERAGED_CHARACTER_MAJOR_ARC_POWER_WITHOUT_INDIVIDUAL_FAMILY_STRIPS
```

No RH certificate is created.

---

# 18. Conclusion

Exact ordinary factorization does not erase the boundary singularity.

It transports it.

After additive twisting, the same statement holds channel by channel for every Dirichlet character.

Thus the first naive attempt to combine ordinary additive and multiplicative structure expands the spectral problem from one zeta function to a Dirichlet- $L$ family.

The PESC seed upgrades the principal characters to fixed-power precision.

It does not upgrade the nonprincipal family.

The existing shifted-prime Möbius machinery therefore remains logarithmic on its major arcs.

The next useful theorem must exploit **averaging across character channels** strongly enough to avoid requiring an individual fixed strip for every $L(s,\chi)$.

That is F-RH-019.
