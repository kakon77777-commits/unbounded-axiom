# CSM_RH Paper 68

## Dimension-Two Shifted-Prime Möbius Local Factors, Seeded Signed Power Cancellation, and the Absoluteization Energy Frontier

**Project:** CSM_RH  
**Paper:** 68  
**Version:** v0.1  
**Date:** 2026-09-09  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Track:** PT6G — `LOW-CONDUCTOR LOCAL-FACTOR RENORMALIZED DISPERSION`  
**Status:** LOCAL FACTOR RENORMALIZATION CERTIFIED / SIGNED FIXED-POWER CANCELLATION CERTIFIED / ABSOLUTEIZATION-PARITY ENERGY OPEN  
**Canonical entry state:** v1.58 / Paper 67 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 67 showed that fixed low-conductor character harmonics survive absolute shift norms. The present paper computes the exact local arithmetic profile of

$$
C_X(h)
=
\sum_{p\le X}\mu(p+h),
$$

and shows that the low-conductor character modes do admit a natural multiplicative renormalization.

For a prime $\ell$, define

$$
\mu_\ell(n)
=
\begin{cases}
1,&v_\ell(n)=0,\\
-1,&v_\ell(n)=1,\\
0,&v_\ell(n)\ge2.
\end{cases}
$$

If $\ell\nmid h$, averaging over reduced residue classes modulo $\ell^2$ gives

$$
\boxed{
\kappa_\ell(h)
=
\frac{\ell^2-3\ell+1}{\ell(\ell-1)}.
}
$$

If $\ell\mid h$, then

$$
\boxed{
\kappa_\ell(h)=1.
}
$$

For a finite set of primes $S$, with

$$
Q_S=\prod_{\ell\in S}\ell^2,
$$

and

$$
\mu_S(n)=\prod_{\ell\in S}\mu_\ell(n),
$$

CRT gives the exact identity

$$
\boxed{
\frac1{\phi(Q_S)}
\sum_{\substack{a\bmod Q_S\\(a,Q_S)=1}}
\mu_S(a+h)
=
\prod_{\ell\in S}\kappa_\ell(h).
}
$$

For $\ell\nmid h$,

$$
\kappa_\ell(h)
=
\left(1-\frac1\ell\right)^2
\left(1+O(\ell^{-2})\right),
$$

so for fixed nonzero $h$,

$$
\boxed{
\prod_{\substack{\ell\le z\\\ell\nmid h}}
\kappa_\ell(h)
=
\frac{C(h)+o_h(1)}{(\log z)^2},
}
$$

with $C(h)\ne0$.

Even more cleanly,

$$
\boxed{
\frac1\ell
\sum_{h\bmod\ell}\kappa_\ell(h)
=
\left(1-\frac1\ell\right)^2,
}
$$

and therefore a complete shift average satisfies

$$
\boxed{
\mathbb E_h
\prod_{\ell\le z}\kappa_\ell(h)
\sim
\frac{e^{-2\gamma}}{(\log z)^2}.
}
$$

Thus the exact low-conductor local profile is a dimension-two sieve factor. This renormalizes the deterministic local characters, but it only gives logarithmic decay. Even a polynomial cutoff $z=X^\theta$ produces only $(\log X)^{-2}$, never a fixed power $X^{-\eta}$.

The PESC seed already does better in the signed shift mean. Put

$$
d=\frac{\kappa}{2},
$$

so

$$
M(y)=\sum_{n\le y}\mu(n)\ll y^{1-d+o(1)}.
$$

For

$$
H=X^{1-\tau},
$$

$$
\sum_{h\le H}C_X(h)
=
\sum_{p\le X}
\left(
M(p+H)-M(p)
\right),
$$

and hence, when $\tau<d$,

$$
\boxed{
\left|
\sum_{h\le H}C_X(h)
\right|
\ll
H\pi(X)X^{-(d-\tau)+o(1)}.
}
$$

So the seed has already crossed the log-to-power barrier before absolute values.

The unresolved gap is exactly

$$
\boxed{
\left|\sum_hC_X(h)\right|
\quad\longrightarrow\quad
\sum_h|C_X(h)|.
}
$$

A sufficient second-moment theorem is

$$
\boxed{
E_2(X,H)
=
\sum_{h\le H}
|C_X(h)|^2
\ll
H\pi(X)^2X^{-2\eta}.
}
$$

By Cauchy this implies

$$
\sum_{h\le H}|C_X(h)|
\ll
H\pi(X)X^{-\eta}.
$$

Expanding the energy gives

$$
\boxed{
E_2(X,H)
=
\sum_{p_1,p_2\le X}
\sum_{h\le H}
\mu(p_1+h)\mu(p_2+h).
}
$$

The diagonal is only $O(H\pi(X))$, harmless for every fixed $\eta<1/2$. The hard term is the off-diagonal prime-pair averaged two-point Chowla energy.

This motivates the auxiliary frontier

```text
F-RH-020
PRIME_PAIR_AVERAGED_CHOWLA_ABSOLUTEIZATION_ENERGY
```

with an explicit warning: no certified bridge from F-RH-020 to the root frontier F-RH-017-v3 has yet been established.

No RH theorem is claimed.

---

# 1. Exact one-prime local factor

Fix a prime $\ell$.

If $\ell\mid h$, then every reduced residue $a\bmod\ell^2$ has

$$
a+h\not\equiv0\pmod\ell,
$$

so

$$
\kappa_\ell(h)=1.
$$

Assume now $\ell\nmid h$.

There are

$$
\phi(\ell^2)=\ell(\ell-1)
$$

reduced residues modulo $\ell^2$.

Exactly $\ell(\ell-2)$ have $v_\ell(a+h)=0$.

Exactly $\ell-1$ have $v_\ell(a+h)=1$.

Exactly one has $v_\ell(a+h)\ge2$.

Therefore

$$
\boxed{
\kappa_\ell(h)
=
\frac{\ell(\ell-2)-(\ell-1)}{\ell(\ell-1)}
=
\frac{\ell^2-3\ell+1}{\ell(\ell-1)}.
}
$$

Record:

```text
B-RH-087
EXACT_SHIFTED_PRIME_MOBIUS_ONE_PRIME_LOCAL_FACTOR
CERTIFIED
```

---

# 2. Finite CRT recombination

Let $S$ be finite and define

$$
Q_S=\prod_{\ell\in S}\ell^2.
$$

Since reduced residues modulo $Q_S$ are the CRT product of reduced residues modulo each $\ell^2$, and $\mu_S$ factors prime by prime,

$$
\boxed{
\frac1{\phi(Q_S)}
\sum_{\substack{a\bmod Q_S\\(a,Q_S)=1}}
\mu_S(a+h)
=
\prod_{\ell\in S}\kappa_\ell(h).
}
$$

Record:

```text
B-RH-088
FINITE_LOW_CONDUCTOR_CHARACTER_PROFILES_RECOMBINE_TO_A_LOCAL_EULER_PRODUCT
CERTIFIED
```

For fixed $S$, the prime number theorem in arithmetic progressions transfers this local residue profile to the prime average as $X\to\infty$.

---

# 3. Sieve dimension two

For $\ell\nmid h$, set

$$
f_\ell
=
\frac{\ell^2-3\ell+1}{\ell(\ell-1)}.
$$

Then

$$
\frac{f_\ell}{(1-1/\ell)^2}
=
\frac{\ell(\ell^2-3\ell+1)}{(\ell-1)^3}
=
1-\frac2{\ell^2}+O(\ell^{-3}).
$$

The ratio product therefore converges absolutely.

Mertens' product theorem gives

$$
\prod_{\ell\le z}\left(1-\frac1\ell\right)
\sim
\frac{e^{-\gamma}}{\log z}.
$$

Hence for fixed nonzero $h$,

$$
\boxed{
\prod_{\substack{\ell\le z\\\ell\nmid h}}
\kappa_\ell(h)
=
\frac{C(h)+o_h(1)}{(\log z)^2}.
}
$$

Record:

```text
B-RH-089
SHIFTED_PRIME_MOBIUS_LOCAL_PROFILE_HAS_SIEVE_DIMENSION_TWO
CERTIFIED
```

---

# 4. Exact shift-averaged local product

Among $h\bmod\ell$, one class has $\ell\mid h$ and contributes $1$ ; the other $\ell-1$ classes contribute $f_\ell$.

Thus

$$
\begin{aligned}
\frac1\ell\sum_{h\bmod\ell}\kappa_\ell(h)
&=
\frac1\ell+\frac{\ell-1}{\ell}f_\ell
\\
&=
\boxed{
\left(1-\frac1\ell\right)^2.
}
\end{aligned}
$$

By CRT,

$$
\boxed{
\mathbb E_h
\prod_{\ell\le z}\kappa_\ell(h)
=
\prod_{\ell\le z}
\left(1-\frac1\ell\right)^2
\sim
\frac{e^{-2\gamma}}{(\log z)^2}.
}
$$

This is the exact dimension-two local factor seen by the shift average.

---

# 5. Local-factor logarithmic ceiling

Even if one could impose the complete local profile through

$$
z=X^\theta,
$$

one obtains only

$$
\boxed{
(\log X)^{-2}.
}
$$

No fixed $\eta>0$ satisfies

$$
(\log X)^{-2}\ll X^{-\eta}.
$$

Thus:

```text
O-RH-157
LOW_CONDUCTOR_LOCAL_FACTOR_RENORMALIZATION_HAS_ONLY_LOGARITHMIC_DIMENSION_TWO_DECAY
CERTIFIED
```

This is the local-congruence version of the classical sieve parity limitation.

---

# 6. Seeded signed shifted-prime power

Assume PESC $(\kappa)$ and set

$$
d=\frac{\kappa}{2}.
$$

Then

$$
M(y)\ll y^{1-d+o(1)}.
$$

Let

$$
C_X(h)=\sum_{p\le X}\mu(p+h),
\qquad
H=X^{1-\tau}.
$$

Interchanging sums,

$$
\boxed{
\sum_{h\le H}C_X(h)
=
\sum_{p\le X}
\left(
M(p+H)-M(p)
\right).
}
$$

Since $p+H\le2X$,

$$
|M(p+H)-M(p)|
\ll
X^{1-d+o(1)}.
$$

Therefore, if $\tau<d$,

$$
\boxed{
\left|
\sum_{h\le H}C_X(h)
\right|
\ll
H\pi(X)X^{-(d-\tau)+o(1)}.
}
$$

Record:

```text
B-RH-090
PESC_SEED_GIVES_FIXED_POWER_SIGNED_SHIFTED_PRIME_MOBIUS_CANCELLATION
CERTIFIED
```

---

# 7. The absoluteization gap

Lichtman's theorem controls

$$
\sum_{h\le H}|C_X(h)|.
$$

The seed gives only

$$
\left|\sum_{h\le H}C_X(h)\right|.
$$

Paper 67 proved that no deterministic signed-to-absolute conversion exists even for a fixed character harmonic.

Thus:

```text
O-RH-158
PESC_SEED_CROSSES_SIGNED_LOG_TO_POWER_BUT_NOT_THE_SHIFT_ABSOLUTEIZATION_GAP
CERTIFIED
```

The missing information is global sign energy.

---

# 8. A sufficient second-moment theorem

By Cauchy-Schwarz,

$$
\sum_{h\le H}|C_X(h)|
\le
H^{1/2}
E_2(X,H)^{1/2},
$$

where

$$
\boxed{
E_2(X,H)
=
\sum_{h\le H}|C_X(h)|^2.
}
$$

Therefore

$$
E_2(X,H)
\ll
H\pi(X)^2X^{-2\eta}
$$

implies

$$
\sum_{h\le H}|C_X(h)|
\ll
H\pi(X)X^{-\eta}.
$$

---

# 9. Prime-pair averaged Chowla expansion

Expand:

$$
\boxed{
E_2(X,H)
=
\sum_{p_1,p_2\le X}
\sum_{h\le H}
\mu(p_1+h)\mu(p_2+h).
}
$$

The diagonal satisfies

$$
\boxed{
E_2^{\rm diag}
\le
H\pi(X).
}
$$

For any fixed $\eta<1/2$,

$$
H\pi(X)
=
o\left(
H\pi(X)^2X^{-2\eta}
\right).
$$

Hence the hard object is

$$
\boxed{
E_2^{\rm off}
=
\sum_{\substack{p_1,p_2\le X\\p_1\ne p_2}}
\sum_{h\le H}
\mu(p_1+h)\mu(p_2+h).
}
$$

This is a prime-pair averaged two-point Chowla problem.

---

# 10. Auxiliary frontier

Open:

```text
F-RH-020
PRIME_PAIR_AVERAGED_CHOWLA_ABSOLUTEIZATION_ENERGY
OPEN_AUXILIARY
```

Target:

$$
\boxed{
E_2(X,H)
\ll
H\pi(X)^2X^{-2\eta}
}
$$

for some fixed $\eta>0$.

Important scope:

```text
NO_CERTIFIED_ROOT_BRIDGE_TO_F-RH-017-v3.
```

The canonical RH frontier remains F-RH-017-v3.

F-RH-020 is a parity diagnostic: it identifies a concrete ordinary-arithmetic theorem that would cross the signed-to-absolute gap in the shifted-prime auxiliary model.

---

# 11. Relation to current literature

Lichtman proves

$$
\sum_{h\le H}
\left|
\sum_{p\le X}\mu(p+h)
\right|
\ll
H\pi(X)(\log X)^{-1/3+\delta}
$$

for polynomial shift ranges, and proves higher averaged Hardy-Littlewood-Chowla correlations with logarithmic savings.

His proof uses sieve restriction to typical factorizations, Fourier decoupling, and major/minor arc estimates. The local-factor calculation above explains why purely local congruence data naturally live at logarithmic scale.

Friedlander and Iwaniec's asymptotic sieve gives complementary calibration: the classical parity problem is broken only after adding extra bilinear information.

Thus the remaining fixed-power target is naturally a parity-energy theorem, not another local-factor computation.

---

# 12. PT6G status

```text
PT6G-LOCAL:
CLOSED / EXACT EULER PRODUCT CERTIFIED.

PT6G-LOCAL-DECAY:
CLOSED AS NON-AMPLIFYING / DIMENSION-TWO LOG DECAY.

PT6G-SIGNED:
CLOSED / SEED FIXED POWER CERTIFIED.

PT6G-ABSOLUTE:
OPEN / GLOBAL PARITY ENERGY REQUIRED.
```

---

# 13. State transition

Advance candidate state

$$
v1.58
\to
v1.59.
$$

Add:

```text
B-RH-087
EXACT_SHIFTED_PRIME_MOBIUS_ONE_PRIME_LOCAL_FACTOR

B-RH-088
FINITE_LOW_CONDUCTOR_CHARACTER_PROFILES_RECOMBINE_TO_A_LOCAL_EULER_PRODUCT

B-RH-089
SHIFTED_PRIME_MOBIUS_LOCAL_PROFILE_HAS_SIEVE_DIMENSION_TWO

B-RH-090
PESC_SEED_GIVES_FIXED_POWER_SIGNED_SHIFTED_PRIME_MOBIUS_CANCELLATION

O-RH-157
LOW_CONDUCTOR_LOCAL_FACTOR_RENORMALIZATION_HAS_ONLY_LOGARITHMIC_DIMENSION_TWO_DECAY

O-RH-158
PESC_SEED_CROSSES_SIGNED_LOG_TO_POWER_BUT_NOT_THE_SHIFT_ABSOLUTEIZATION_GAP
```

Open F-RH-020 as auxiliary only.

No RH certificate is created.

---

# 14. Conclusion

The low-conductor local characters can be recombined exactly.

Their total deterministic effect is a dimension-two Euler product with logarithmic decay.

The seed already gives fixed-power cancellation in the signed shifted-prime mean.

Therefore the only unresolved part of this auxiliary route is absoluteization: a global parity/sign-energy theorem.

The simplest sufficient formulation is the prime-pair averaged two-point Chowla energy F-RH-020.

The root CSM_RH frontier remains F-RH-017-v3.
