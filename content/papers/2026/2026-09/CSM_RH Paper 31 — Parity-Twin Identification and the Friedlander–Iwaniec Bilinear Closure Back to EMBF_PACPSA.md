# CSM_RH Paper 31
## Parity-Twin Identification and the Friedlander–Iwaniec Bilinear Closure Back to EMBF/PACPSA

**Project:** `CSM_RH`  
**Paper:** `31`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.21 / Paper 30`  
**Campaign:** `30 — PARITY_SENSITIVE_PESC_ATTACK`  
**Status:** parity-sensitive identification / direct PESC closure audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Campaign 30 asks whether the classical parity problem of sieve theory hides a new scalar or bilinear theorem which is lower-strength than PESC and has not already appeared in CSM_RH.

The result is a closure:

> the Friedlander–Iwaniec parity-breaking bilinear axiom, when specialized to the PESC positivity lifts, produces exactly the endogenous Möbius bilinear geometry already named EMBF in Paper 13. To convert that bilinear parity information into a fixed-power PESC theorem still requires the power-accurate coupled assembly already named PACPSA in Paper 15.

Thus parity sensitivity is essential, but it is not a new missing coordinate.

The PESC-specific parity difficulty has two simultaneous components:

```text
Möbius / Liouville parity cancellation;
endogenous fidelity to the cumulative prime error.
```

Standard asymptotic sieve solves the first component for suitable external sequences. It does not solve the second component for the self-generated PESC weight.

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical prime-only PESC

Recall

$$
q_n
=
\log n\,
1_{\mathbb P}(n),
$$

$$
c_n=q_n-1,
$$

and

$$
B(j)
=
\sum_{n\le j}c_n
=
\vartheta(j)-j.
$$

The endpoint weight is

$$
w_N(n)
=
\#\{
j\in[N,2N-1]:
n\le j
\}.
$$

The canonical root self-correlation is

$$
\boxed{
\mathcal C_N^\vartheta
=
\sum_{n<2N}
w_N(n)c_nB(n-1).
}
$$

PESC $(\kappa)$ asks for

$$
\boxed{
|\mathcal C_N^\vartheta|
\ll
N^{3-\kappa+o(1)}
}
$$

for one fixed

$$
0<\kappa<\frac12.
$$

---

# 2. Positivity lifts

Let

$$
M_N
\ge
\max_{j<2N}|B(j)|.
$$

Define two nonnegative lifted sequences

$$
\boxed{
a_n^\pm
=
w_N(n)
[
M_N\pm B(n-1)
].
}
$$

Define the prime-detection discrepancy functional

$$
\boxed{
\mathfrak E_\vartheta(a)
=
\sum_{p<2N}
(\log p)a_p
-
\sum_{n<2N}a_n.
}
$$

Equivalently,

$$
\mathfrak E_\vartheta(a)
=
\sum_{n<2N}c_na_n.
$$

Therefore:

## Theorem 2.1 — Exact PESC Positivity-Lift Difference

$$
\boxed{
\mathfrak E_\vartheta(a^+)
-
\mathfrak E_\vartheta(a^-)
=
2\mathcal C_N^\vartheta.
}
$$

This is the exact bridge first introduced in Paper 13.

---

# 3. Von Mangoldt detection and prime powers

For compatibility with asymptotic-sieve theorems, define

$$
\boxed{
\mathfrak E_\Lambda(a)
=
\sum_{n<2N}
[
\Lambda(n)-1
]a_n.
}
$$

Then

$$
\mathfrak E_\Lambda(a^+)
-
\mathfrak E_\Lambda(a^-)
=
2
\sum_{n<2N}
w_N(n)
[
\Lambda(n)-1
]
B(n-1).
$$

The difference from the prime-only PESC comes only from prime powers.

Using

$$
w_N(n)\ll N,
$$

$$
|B(n)|\ll N,
$$

and

$$
\sum_{\substack{p^k\le2N\\k\ge2}}
\log p
=
N^{1/2+o(1)},
$$

we obtain:

## Theorem 3.1 — Prime-Power Detection Difference

$$
\boxed{
\mathfrak E_\Lambda(a^+)
-
\mathfrak E_\Lambda(a^-)
=
2\mathcal C_N^\vartheta
+
O
\left(
N^{5/2+o(1)}
\right).
}
$$

Hence the Lambda-detection positivity lift is fixed-exponent equivalent to prime-only PESC throughout the first-strip range

$$
0<\kappa<\frac12.
$$

---

# 4. Liouville parity twins

Let

$$
\lambda(n)=(-1)^{\Omega(n)}
$$

be the Liouville function.

Primes satisfy

$$
\boxed{
\lambda(p)=-1.
}
$$

A classical sieve ambiguity is obtained from the parity twins

$$
\boxed{
u_n^\pm
=
\frac12
[
1\pm\lambda(n)
].
}
$$

The plus sequence selects even prime-factor parity and therefore vanishes on primes.

The minus sequence selects odd prime-factor parity and contains the primes.

Classical divisor-sum sieve information cannot by itself distinguish these two parity worlds.

---

# 5. Squarefree exact parity model

For an exact finite algebraic version compatible with Möbius signs, define

$$
\boxed{
v_n^\pm
=
\frac12
\mu^2(n)
[
1\pm\mu(n)
].
}
$$

On squarefree integers,

$$
\mu(n)=\lambda(n).
$$

Therefore:

## even-parity class

$$
\boxed{
\mu(n)v_n^+
=
v_n^+.
}
$$

## odd-parity class

$$
\boxed{
\mu(n)v_n^-
=
-
v_n^-.
}
$$

Thus a Möbius-weighted bilinear form has no cancellation at all on either pure parity class.

The sign changes of $\mu$ become useful only when the sequence genuinely mixes the two parity classes.

---

# 6. Friedlander–Iwaniec parity-breaking bilinear axiom

For a nonnegative sequence $(a_n)$, Friedlander and Iwaniec introduce a bilinear hypothesis of the form

$$
\boxed{
\mathfrak B_{\mathrm{FI}}(a;L,C)
=
\sum_m
\left|
\sum_{\substack{
L<n\le2L\\
mn\le x
}}
\gamma(n,C)
\mu(mn)
a_{mn}
\right|.
}
$$

Here

$$
\boxed{
\gamma(n,C)
=
\sum_{\substack{d\mid n\\d\le C}}
\mu(d).
}
$$

Their asymptotic sieve for primes adds this bilinear hypothesis to ordinary sieve distribution axioms.

The source of parity-breaking cancellation is explicitly the changing sign of

$$
\mu(mn)
$$

inside the inner sum.

The classical Selberg parity-twin example satisfies the ordinary high-level sieve remainder axiom but fails this bilinear axiom.

---

# 7. The PESC lift inside the FI bilinear form

Insert

$$
a_{mn}^\pm
=
w_N(mn)
[
M_N\pm B(mn-1)
].
$$

For each fixed outer variable $m$, define

$$
I_m^\pm
=
\sum_n
\gamma(n,C)
\mu(mn)
a_{mn}^\pm
$$

in the appropriate dyadic range.

Then:

$$
\boxed{
I_m^+
-
I_m^-
=
2
\sum_n
\gamma(n,C)
\mu(mn)
w_N(mn)
B(mn-1).
}
$$

Define the difference seminorm

$$
\boxed{
\mathfrak B_\Delta
=
\frac12
\sum_m
|I_m^+-I_m^-|.
}
$$

Therefore:

## Theorem 7.1 — FI/PESC Bilinear Identification

$$
\boxed{
\mathfrak B_\Delta
=
\sum_m
\left|
\sum_n
\gamma(n,C)
\mu(mn)
w_N(mn)
B(mn-1)
\right|.
}
$$

This is exactly the EMBF geometry introduced in Paper 13, up to the same dyadic/range conventions.

Create:

```text
B-RH-006
FI_PARITY_BILINEAR_TO_EMBF_IDENTIFICATION
status:
  CERTIFIED
```

---

# 8. Triangle relation to the positive lifts

The ordinary FI bilinear seminorms of the two nonnegative lifts satisfy

$$
|I_m^+-I_m^-|
\le
|I_m^+|+|I_m^-|.
$$

Hence

$$
\boxed{
2\mathfrak B_\Delta
\le
\mathfrak B_{\mathrm{FI}}(a^+;L,C)
+
\mathfrak B_{\mathrm{FI}}(a^-;L,C).
}
$$

Thus sufficiently strong FI-type parity-breaking bounds for both positive lifts imply an EMBF bound.

The converse does not follow, because the common $M_N$ component is removed by the difference but remains inside the two positive seminorms.

This is one reason a direct difference-stability theorem would be stronger than merely applying the asymptotic sieve twice.

---

# 9. C=1 is the raw parity probe

When

$$
C=1,
$$

$$
\gamma(n,1)=1.
$$

The bilinear difference becomes

$$
\boxed{
\sum_m
\left|
\sum_n
\mu(mn)
w_N(mn)
B(mn-1)
\right|.
}
$$

On squarefree products,

$$
\mu(mn)=\lambda(mn).
$$

Thus the lowest-complexity EMBF is literally a Liouville/Möbius parity probe weighted by the endogenous cumulative prime error.

This identifies the PESC parity defect without introducing a new object.

---

# 10. Two independent debts inside the PESC parity problem

The FI bilinear form solves a parity problem for an externally supplied sequence when its special bilinear structure can be estimated.

PESC is more difficult because its weight is endogenous:

$$
\boxed{
B(mn-1)
=
\vartheta(mn-1)-(mn-1).
}
$$

Thus there are two logically distinct requirements.

## Debt A — parity breaking

Obtain cancellation from

$$
\mu(mn)
$$

or an equivalent Liouville-sensitive sign.

## Debt B — endogenous fidelity

Preserve that cancellation when the coefficient is weighted by the cumulative error generated by the same prime process.

Paper 14 and Paper 15 already identified this second issue through the endogenous Möbius bilinear and weighted-Chowla transfer debts.

Create:

```text
O-RH-067
PARITY_BREAKING_DOES_NOT_SUPPLY_ENDOGENOUS_FIDELITY
status:
  CERTIFIED AS STRUCTURAL IDENTIFICATION
```

---

# 11. Rough Liouville parity scalar

A natural scalar parity observable is the rough Liouville sum.

For fixed squarefree $Q$, define

$$
\boxed{
L_Q(x)
=
\sum_{\substack{n\le x\\ \gcd(n,Q)=1}}
\lambda(n).
}
$$

Its Dirichlet series is

$$
\boxed{
\sum_{\substack{n\ge1\\ \gcd(n,Q)=1}}
\frac{\lambda(n)}{n^s}
=
\frac{\zeta(2s)}{\zeta(s)}
\prod_{p\mid Q}
(1+p^{-s}),
\qquad
\Re s>1.
}
$$

The finite Euler factor is nonzero.

For any zeta zero $\rho$ with

$$
\Re\rho>\frac12,
$$

the numerator

$$
\zeta(2\rho)
$$

is finite and nonzero because

$$
\Re(2\rho)>1.
$$

Hence the rough Liouville Dirichlet series has a pole at every such zero.

---

# 12. Fixed-power parity scalar is already fixed-strip strength

Suppose for some fixed

$$
\theta>\frac12
$$

one could prove

$$
\boxed{
L_Q(x)
=
O_\varepsilon
\left(
x^{\theta+\varepsilon}
\right)
}
$$

for every $\varepsilon>0$.

Partial summation would analytically continue its Dirichlet series to

$$
\Re s>\theta.
$$

But Section 11 shows that every zeta zero in that half-plane would create a pole.

Therefore:

## Theorem 12.1 — Rough-Parity Fixed-Power Lock

$$
\boxed{
L_Q(x)
=
O_\varepsilon
(x^{\theta+\varepsilon})
\quad
\Longrightarrow
\quad
\zeta(s)\ne0
\text{ for }
\Re s>\theta.
}
$$

Thus a direct fixed-power Liouville-parity scalar is not a lower-strength free input.

Create:

```text
O-RH-068
ROUGH_LIOUVILLE_PARITY_SCALAR_INVERSE_ZETA_LOCK
status:
  CERTIFIED
```

This explains why the Friedlander–Iwaniec method uses special bilinear structure instead of demanding a global fixed-power Liouville sum.

---

# 13. Output precision of the classical asymptotic sieve

The Friedlander–Iwaniec theorem produces a prime-detection asymptotic with relative error

$$
\boxed{
O
\left(
\frac{\log\delta(x)}{\log\Delta(x)}
\right).
}
$$

For their practical parameter class

$$
\delta(x)
=
(\log x)^\alpha,
$$

$$
\Delta(x)
=
x^\eta,
$$

this becomes

$$
\boxed{
O
\left(
\frac{\log\log x}{\log x}
\right).
}
$$

This is parity-breaking precision.

It is not fixed-power precision.

Applied to PESC positivity lifts of total mass at the natural

$$
N^{3+o(1)}
$$

scale, a direct independent-output error of this class remains

$$
N^{3-o(1)}.
$$

Thus classical asymptotic-sieve output does not by itself prove PESC $(\kappa)$.

---

# 14. Return to PACPSA

Paper 15 introduced:

```text
F-RH-014
PACPSA
POWER_ACCURATE_COUPLED_PARITY_SIEVE_ASSEMBLY
```

The reason for that frontier can now be stated more sharply.

A PESC proof through parity-sensitive positive lifts needs not only:

```text
a parity-breaking bilinear estimate
```

but also:

```text
a power-accurate coupled assembly
whose error is controlled at the difference level,
not merely relative to each N^3-sized positive lift.
```

This is exactly the bridge debt already recorded in Paper 15.

Therefore Campaign 30 does not create a new parity frontier.

It identifies the classical sieve interpretation of an existing one.

---

# 15. Relationship with EMBF / EMDQO history

The sequence is now:

```text
Friedlander-Iwaniec parity axiom
  ->
PESC positivity-lift difference
  ->
EMBF
  ->
EMDQO / weighted Chowla analysis
  ->
PACPSA bridge debt
```

Paper 14 showed that at $C=1$ the coefficient side contains inverse-zeta structure.

Paper 15 showed that second-moment expansion of EMBF exposes an endogenous weighted binary Chowla-type off-diagonal.

Campaign 30 therefore reconnects classical parity theory to those already audited CSM_RH obstructions.

---

# 16. Campaign 30 track audit

## Q1 — PESC parity decomposition

```text
status:
  IDENTIFIED THROUGH POSITIVITY LIFTS

prime parity:
  Liouville odd

direct new theorem:
  NO
```

## Q2 — asymptotic-sieve scalar defect

```text
status:
  NOT A SINGLE CHEAP SCALAR

parity-sensitive authority:
  Möbius bilinear form

direct fixed-power rough-Liouville scalar:
  inverse-zeta locked
```

## Q3 — parity-breaking bilinear input

```text
status:
  EXACTLY MAPS TO EMBF GEOMETRY

fixed-power PESC bridge:
  still requires PACPSA-type coupled assembly
```

## Q4 — prime versus almost-prime drift comparator

```text
status:
  PARITY COMPARATOR EXISTS

fixed-power scalar control:
  already fixed-strip strength
```

## Q5 — direct residual sign structure

```text
status:
  NO NEW PRIME-SPECIFIC SIGN IDENTITY FOUND

Möbius parity sign:
  already present in EMBF
```

---

# 17. Campaign 30 verdict

The parity-sensitive route is essential but not new.

The main closure is:

$$
\boxed{
\text{PESC parity problem}
=
\text{Möbius parity breaking}
+
\text{endogenous cumulative-error fidelity}.
}
$$

The first component is the classical Friedlander–Iwaniec insight.

The second component is the CSM_RH-specific obstruction already exposed by EMBF/EMDQO/PACPSA.

No lower-strength fixed-power theorem is obtained.

---

# 18. New certified bridge and obstructions

Create:

```text
B-RH-006
FI_PARITY_BILINEAR_TO_EMBF_IDENTIFICATION
CERTIFIED

O-RH-067
PARITY_BREAKING_DOES_NOT_SUPPLY_ENDOGENOUS_FIDELITY
CERTIFIED

O-RH-068
ROUGH_LIOUVILLE_PARITY_SCALAR_INVERSE_ZETA_LOCK
CERTIFIED
```

No new frontier is created.

---

# 19. Canonical root status

The root remains:

```text
F-RH-010
PESC
OPEN
```

The direct lag-energy candidate remains:

```text
F-RH-016
MLEPG
OPEN
```

Older auxiliary parity objects remain in their audited roles:

```text
F-RH-012 EMBF
  auxiliary parity bilinear

F-RH-013 EMDQO
  auxiliary second-moment mechanism

F-RH-014 PACPSA
  power-accurate coupled assembly requirement
```

---

# 20. Campaign 31

The next campaign is:

```text
CSM_RH Campaign 31
ENDOGENOUS_PARITY_BILINEAR_REAUDIT
```

No new frontier may be created unless the result is strictly weaker than PESC and has a proved fixed-power bridge.

The campaign revisits EMBF only with the new information accumulated after Papers 20–30.

---

# 21. Campaign 31 tracks

## V1 — Lambda-sharp subtraction inside EMBF

Replace

$$
B
=
F+B^\sharp
$$

using Paper 28's bounded-primitive sieve model.

Determine whether EMBF is fixed-exponent equivalent to an endogenous residual-weighted Möbius bilinear.

## V2 — modern Möbius / Liouville short-interval uniformity

Use the 2026 short-interval higher-uniformity framework for $\mu$ together with the residual weight.

Test whether the weight can be externalized without assuming the desired PESC bound.

## V3 — low-frequency projection of the endogenous weight

Project $F$ onto a canonical scale-local smooth component and ask whether Möbius parity cancellation can control that projection at fixed power.

The projection must be defined without zeros.

## V4 — remove the outer absolute value

PESC itself is signed, whereas EMBF uses an outer absolute value over $m$.

Search for an aggregate-first signed bilinear identity that avoids this strengthening without collapsing back to PESC tautologically.

## V5 — PACPSA difference-stability

Study whether the asymptotic sieve can be made stable directly for the difference of the two positivity lifts, so that the common $N^3$ mass cancels before the error estimate.

A valid result must be proved, not assumed.

---

# 22. Campaign 31 rejection filters

Reject a candidate if:

## R1. It reproduces Paper 14's coefficient-only inverse-zeta argument.

## R2. It reproduces Paper 15's EMDQO without a stronger bridge.

## R3. It uses ordinary parity-breaking without endogenous fidelity.

## R4. It obtains only logarithmic/subpower output.

## R5. It assumes fixed-power Liouville/Möbius partial sums.

## R6. It redefines PESC as a new bilinear form.

---

# 23. External calibration

The present audit uses three classical facts.

1. Friedlander–Iwaniec's asymptotic sieve adds a Möbius bilinear axiom specifically to break the classical parity problem; their Selberg parity-twin example satisfies strong ordinary sieve distribution but fails the bilinear axiom.

2. In practical parameter ranges, their prime-detection theorem has relative error of order $\log\log x/\log x$, not a fixed power.

3. The Liouville Dirichlet series is

$$
\zeta(2s)/\zeta(s),
$$

so fixed-power parity cancellation is itself sensitive to the zero set of $\zeta$.

These facts align the classical parity barrier with the previously identified CSM_RH EMBF/PACPSA branch.

---

# 24. State transition

```text
CSM_RH v1.21
  ->
CSM_RH v1.22
```

with:

```text
Campaign 30
  CLOSED_AS_PARITY_IDENTIFICATION_AND_EMBF_RECONNECTION

B-RH-006
  FI_PARITY_BILINEAR_TO_EMBF_IDENTIFICATION
  CREATED / CERTIFIED

O-RH-067
  PARITY_BREAKING_DOES_NOT_SUPPLY_ENDOGENOUS_FIDELITY
  CREATED / CERTIFIED

O-RH-068
  ROUGH_LIOUVILLE_PARITY_SCALAR_INVERSE_ZETA_LOCK
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 31
  ENDOGENOUS_PARITY_BILINEAR_REAUDIT
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

CLASSICAL PARITY DEFECT = IDENTIFIED

FI PARITY BILINEAR = EMBF GEOMETRY AFTER PESC LIFTING

PARITY BREAKING ALONE = INSUFFICIENT

ENDOGENOUS FIDELITY = STILL OPEN

ROUGH LIOUVILLE FIXED POWER = INVERSE-ZETA / FIXED-STRIP STRENGTH

CLASSICAL ASYMPTOTIC SIEVE OUTPUT = LOG-RELATIVE PRECISION

PACPSA DIFFERENCE-STABILITY = STILL THE PARITY-ASSEMBLY DEBT

NEXT CAMPAIGN = 31
```

The decisive identification is

$$
\boxed{
\frac12
\sum_m
\left|
I_m(a^+)-I_m(a^-)
\right|
=
\sum_m
\left|
\sum_n
\gamma(n,C)
\mu(mn)
w_N(mn)
B(mn-1)
\right|.
}
$$

The right-hand side is exactly the endogenous Möbius bilinear geometry already isolated in EMBF.

The classical parity problem and the CSM_RH endogenous-weight problem are therefore now connected in one certified diagram.
