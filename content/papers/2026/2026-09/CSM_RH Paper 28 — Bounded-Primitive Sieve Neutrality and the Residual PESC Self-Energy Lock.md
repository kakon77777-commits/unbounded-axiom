# CSM_RH Paper 28
## Bounded-Primitive Sieve Neutrality and the Residual PESC Self-Energy Lock

**Project:** `CSM_RH`  
**Paper:** `28`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.18 / Paper 27`  
**Campaign:** `27 — DIRECT_PESC_ATTACK_II`  
**Status:** direct bilinear sieve-model audit / fixed-exponent equivalence theorem; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Campaign 27 returns from positive fourth-moment surrogates to the signed bilinear PESC root.

The first direct attack is to subtract the modern sieve approximant $\Lambda^\sharp$ inside the bilinear energy.

The result is a closure theorem:

> because the centered sieve model has a subpolynomially bounded primitive, subtracting it is fixed-exponent neutral. The residual self-correlation is PESC-equivalent at every first-strip exponent.

Thus the modern local sieve model captures congruence structure but does not absorb a polynomial smooth prime-error drift.

No live GLM-5.3-Flash run is claimed.

---

# 1. Lambda-side PESC analogue

Work first with the centered von Mangoldt sequence

$$
\boxed{
a_n=\Lambda(n)-1.
}
$$

Define its primitive

$$
\boxed{
A(j)=\sum_{n\le j}a_n
=
\psi(j)-j.
}
$$

For the dyadic endpoint interval

$$
N\le j\le2N-1,
$$

define the endpoint multiplicity

$$
\boxed{
w_N(n)
=
\#\{
j\in[N,2N-1]:
n\le j
\}.
}
$$

Thus

$$
w_N(n)
=
\begin{cases}
N,&n\le N,\\
2N-n,&N<n<2N,\\
0,&n\ge2N.
\end{cases}
$$

Define

$$
J_a(N)
=
\sum_{j=N}^{2N-1}A(j)^2,
$$

$$
D_a(N)
=
\sum_{n<2N}w_N(n)a_n^2,
$$

and

$$
\boxed{
\mathcal C_a(N)
=
\sum_{n<2N}
w_N(n)a_nA(n-1).
}
$$

The exact energy identity is

$$
\boxed{
J_a
=
D_a
+
2\mathcal C_a.
}
$$

For first fixed-strip exponents $0<\kappa<1/2$, Paper 10's prime-power stripping transfers this Lambda-side mean-square / self-correlation branch back to the canonical prime-only PESC branch.

---

# 2. Modern sieve approximant

The 2026 higher-uniformity framework uses

$$
\boxed{
\Lambda^\sharp(n)
=
\frac{Q}{\varphi(Q)}
1_{(n,Q)=1},
}
$$

where

$$
Q=P(R)
=
\prod_{p<R}p
$$

and

$$
\boxed{
R
=
\exp
\left(
(\log X)^{1/10}
\right).
}
$$

Define the centered model

$$
\boxed{
b_n
=
\Lambda^\sharp(n)-1.
}
$$

Define the true residual

$$
\boxed{
f_n
=
\Lambda(n)-\Lambda^\sharp(n).
}
$$

Then

$$
\boxed{
a_n=b_n+f_n.
}
$$

Let

$$
B(j)=\sum_{n\le j}b_n,
$$

and

$$
F(j)=\sum_{n\le j}f_n.
$$

Then

$$
\boxed{
A(j)=B(j)+F(j).
}
$$

---

# 3. Exact zero mean of the model over one period

The function $\Lambda^\sharp$ is periodic modulo $Q$.

Over a complete residue period,

$$
\sum_{n=1}^{Q}
\Lambda^\sharp(n)
=
\frac{Q}{\varphi(Q)}
\varphi(Q)
=
Q.
$$

Therefore:

## Theorem 3.1 — Exact Period Mean

$$
\boxed{
\sum_{n=1}^{Q}b_n
=
0.
}
$$

Thus the centered model has zero primitive drift over every complete period.

---

# 4. Subpolynomial primitive bound

Because $b_n$ is $Q$ -periodic with zero period mean,

$$
\boxed{
\sup_j|B(j)|
\ll
Q
\left(
1+
\frac{Q}{\varphi(Q)}
\right).
}
$$

Mertens' product estimate gives

$$
\frac{Q}{\varphi(Q)}
\ll
\log R.
$$

Chebyshev's estimate for the first Chebyshev function gives

$$
\log Q
=
\sum_{p<R}\log p
=
O(R).
$$

But

$$
R
=
\exp
\left(
(\log X)^{1/10}
\right)
=
o(\log X).
$$

Hence

$$
\boxed{
Q
=
X^{o(1)}
}
$$

and therefore

## Theorem 4.1 — Bounded Primitive of the Sieve Model

$$
\boxed{
\sup_j|B(j)|
=
X^{o(1)}.
}
$$

This is the decisive low-frequency property of $\Lambda^\sharp$.

---

# 5. Mean-square equivalence after sieve subtraction

Define the residual mean-square

$$
\boxed{
J_f(N)
=
\sum_{j=N}^{2N-1}F(j)^2.
}
$$

Since

$$
A=F+B,
$$

we have

$$
J_a-J_f
=
2\sum_{j=N}^{2N-1}F(j)B(j)
+
\sum_{j=N}^{2N-1}B(j)^2.
$$

Chebyshev's bound gives

$$
\psi(x)\ll x.
$$

The periodic model has total summatory function

$$
\sum_{n\le x}\Lambda^\sharp(n)
=
x+X^{o(1)}.
$$

Hence

$$
F(j)=O(N)
$$

uniformly for $j\le2N$.

Combining with Theorem 4.1:

## Theorem 5.1 — Fixed-Exponent Mean-Square Neutrality

$$
\boxed{
J_a(N)
=
J_f(N)
+
O
\left(
N^2X^{o(1)}
\right).
}
$$

Therefore, for every fixed

$$
0<\kappa<1,
$$

$$
\boxed{
J_a(N)
\ll
N^{3-\kappa+o(1)}
\iff
J_f(N)
\ll
N^{3-\kappa+o(1)}.
}
$$

For the canonical first-strip branch we later restrict to $\kappa<1/2$ because of prime-power stripping.

---

# 6. Diagonal equivalence

Define

$$
D_f(N)
=
\sum_{n<2N}
w_N(n)f_n^2.
$$

Since

$$
a_n=f_n+b_n,
$$

$$
D_a-D_f
=
\sum_{n<2N}
w_N(n)
[
2f_nb_n+b_n^2
].
$$

On the relevant range,

$$
|f_n|+|b_n|
=
X^{o(1)}.
$$

Also,

$$
0\le w_N(n)\le N
$$

and there are $O(N)$ contributing $n$.

Therefore:

## Theorem 6.1 — Diagonal Neutrality

$$
\boxed{
D_a(N)
=
D_f(N)
+
O
\left(
N^2X^{o(1)}
\right).
}
$$

---

# 7. Residual PESC equivalence

Define

$$
\boxed{
\mathcal C_f(N)
=
\sum_{n<2N}
w_N(n)f_nF(n-1).
}
$$

The residual energy identity is

$$
J_f
=
D_f
+
2\mathcal C_f.
$$

Subtracting from the original energy identity and using Theorems 5.1 and 6.1 gives:

## Theorem 7.1 — Sieve-Residual PESC Equivalence

$$
\boxed{
\mathcal C_a(N)
=
\mathcal C_f(N)
+
O
\left(
N^2X^{o(1)}
\right).
}
$$

Hence for every fixed

$$
0<\kappa<1,
$$

$$
\boxed{
\mathcal C_a(N)
\ll
N^{3-\kappa+o(1)}
\iff
\mathcal C_f(N)
\ll
N^{3-\kappa+o(1)}.
}
$$

Combining with the already certified prime-power bridge:

## Corollary 7.2 — Canonical First-Strip Residual Equivalence

For every fixed

$$
0<\kappa<\frac12,
$$

the canonical prime-only PESC fixed-power bound is exponent-equivalent to the Lambda-sharp residual self-correlation bound

$$
\boxed{
\mathcal C_f(N)
\ll
N^{3-\kappa+o(1)}.
}
$$

Create:

```text
B-RH-004
SIEVE_RESIDUAL_PESC_EQUIVALENCE
status:
  CERTIFIED
```

---

# 8. Direct cross-term identity

The equivalence can also be seen directly.

Since

$$
a=f+b
$$

and

$$
A=F+B,
$$

the two mixed PESC terms are

$$
\sum_nw_N(n)b_nF(n-1)
+
\sum_nw_N(n)f_nB(n-1).
$$

Using

$$
\Delta(BF)_n
=
b_nF(n-1)
+
f_nB(n-1)
+
b_nf_n,
$$

the mixed sum becomes

$$
\boxed{
\sum_nw_N(n)\Delta(BF)_n
-
\sum_nw_N(n)b_nf_n.
}
$$

By the definition of $w_N$,

$$
\sum_nw_N(n)\Delta(BF)_n
=
\sum_{j=N}^{2N-1}B(j)F(j).
$$

Both terms are

$$
O(N^2X^{o(1)}).
$$

Thus the model-residual cross terms are exponent-neutral.

The critical term is the residual self-correlation $\mathcal C_f$.

---

# 9. Bounded-primitive approximant neutrality

The argument above does not fundamentally depend on the exact sieve formula.

It reveals a general principle:

> an approximant whose centered primitive is subpolynomial cannot absorb a polynomial-scale cumulative drift, and subtracting it cannot lower the first fixed-power mean-square/PESC strength.

Create:

```text
O-RH-060
BOUNDED_PRIMITIVE_APPROXIMANT_NEUTRALITY
status:
  CERTIFIED FOR THE LAMBDA-SHARP MODEL
```

The statement is certified here for the specific modern $\Lambda^\sharp$ approximant.

A general abstract version would require explicit hypotheses on pointwise size and primitive growth.

---

# 10. What Lambda-sharp captures

The model $\Lambda^\sharp$ captures the deterministic obstruction from small prime divisibility.

Its periodic primitive is tiny at polynomial scale.

Therefore it can encode:

```text
small-prime congruence structure;
local sieve density;
structured local model terms.
```

But it cannot encode:

```text
a cumulative component x^beta with fixed beta>0;
a persistent polynomial smooth drift;
the long low-frequency mode responsible for fixed-strip strength.
```

The latter remains almost completely inside

$$
F=A-B.
$$

---

# 11. Current local residual theorem is compatible with a fixed drift

The 2026 theorem gives for almost all polynomial short intervals

$$
\boxed{
F(x+H)-F(x)
\ll
H\log^{-A}X
}
$$

for every fixed $A>0$ in the stated range.

Now consider a hypothetical smooth component

$$
F_{\beta}(x)=x^\beta,
\qquad
0<\beta<1.
$$

For

$$
H=o(X),
$$

$$
F_\beta(x+H)-F_\beta(x)
=
\beta H X^{\beta-1}
+
O
\left(
H^2X^{\beta-2}
\right).
$$

But for every fixed $A$,

$$
\boxed{
X^{\beta-1}
\ll
\log^{-A}X.
}
$$

Therefore the current log-accurate short-interval residual theorem is fully compatible with every fixed power drift $x^\beta$ with $\beta<1$.

Create:

```text
O-RH-061
LOG_LOCAL_RESIDUAL_BLIND_TO_FIXED_POWER_DRIFT
status:
  CERTIFIED AS STRENGTH AUDIT
```

---

# 12. Why the bilinear route is drift-sensitive

Although a local residual increment theorem does not detect $x^\beta$, the residual PESC does.

For a smooth cumulative mode

$$
F(x)\asymp x^\beta,
$$

its increment is

$$
f_n
\asymp
\beta n^{\beta-1},
$$

and the bilinear product has scale

$$
f_nF(n)
\asymp
n^{2\beta-1}.
$$

After the endpoint weight contributes one factor $N$ and the $n$ -sum another scale factor, the residual self-correlation has natural exponent

$$
\boxed{
N^{2\beta+1}.
}
$$

Thus a PESC bound

$$
N^{3-\kappa}
$$

is incompatible at exponent scale with

$$
\beta
>
1-\frac{\kappa}{2}.
$$

This matches the certified Mellin-pole strip law.

The bilinear root target is therefore genuinely sensitive to the smooth drift that current local residual uniformity ignores.

---

# 13. Campaign 27 track audit

## P2-1 — signed prime sampling with drift subtraction

```text
status:
  LAMBDA-SHARP DRIFT SUBTRACTION TOO SMALL

reason:
  model primitive X^{o(1)}
```

## P2-2 — PESC after sieve-model subtraction

```text
status:
  EXACT FIXED-EXPONENT EQUIVALENCE

result:
  B-RH-004
```

## P2-3 — bilinear residual/model cross term

```text
status:
  HARMLESS O(N^2 X^{o(1)})

critical term:
  residual self-correlation
```

## P2-4 — scale-coupled signed recurrence

```text
status:
  NO NEW FIXED-GAP RECURRENCE FOUND

existing cumulative-contraction criterion remains
```

## P2-5 — direct arithmetic drift exclusion

```text
status:
  CURRENT LOCAL RESIDUAL THEOREMS BLIND TO FIXED DRIFT

new bilinear arithmetic theorem:
  still needed
```

---

# 14. Direct PESC branch verdict

The sieve-model subtraction does not create a weaker target.

Instead it clarifies the root obstruction:

$$
\boxed{
\text{PESC}
\quad\text{is essentially the self-energy of}
\quad
f=\Lambda-\Lambda^\sharp
}
$$

because the structured model has negligible primitive at polynomial scale.

Therefore:

```text
model terms:
  harmless

model/residual cross terms:
  harmless

residual self-energy:
  PESC-equivalent
```

This is the shortest bilinear closure obtained so far.

---

# 15. No new frontier

Campaign 27 does not create another canonical frontier.

The canonical target remains:

```text
F-RH-010
PESC
```

The direct theorem candidate remains:

```text
F-RH-016
MLEPG
```

The residual formulation is a certified equivalent first-strip representation, not a new target.

---

# 16. Campaign 28

The next campaign is:

```text
CSM_RH Campaign 28
ENDOGENOUS_DRIFT_COERCIVITY_ATTACK
```

The problem is now intentionally narrow:

> find a genuinely prime-arithmetic bilinear theorem which prevents the residual primitive $F=\sum(\Lambda-\Lambda^\sharp)$ from carrying a persistent polynomial smooth drift.

---

# 17. Campaign 28 tracks

## E1 — residual prime-sampling coercivity

Use the fact that $f=\Lambda-\Lambda^\sharp$ is not an arbitrary derivative.

Test whether

$$
\sum_n
w_N(n)f_nF(n-1)
$$

has a sign/coercivity property after subtracting explicit sieve-model terms.

## E2 — Selberg symmetry on the residual primitive

Insert

$$
\Lambda=\Lambda^\sharp+f
$$

into the prime-only Selberg symmetry formula.

Keep the periodic model exact and isolate a bilinear identity involving $F$.

Reject the route if the resulting forcing remains only $O(X)$ and is compatible with every fixed power drift.

## E3 — multiplicative sampling of a smooth residual drift

Assume

$$
F(x)\approx cx^\beta
$$

on one dyadic scale and compute how the prime/multiplicative sampling identities respond.

Seek a contradiction requiring less than a full fixed-power PNT theorem.

## E4 — two-scale signed residual energy

Relate residual PESC at $N$ and $2N$ directly.

A valid candidate must generate fixed contraction mass without passing through a positive variance frontier.

## E5 — canonical drift projection with arithmetic remainder

Define a canonical low-frequency projection of $F$ and prove that the residual prime arithmetic contracts the projected coefficient.

The projection may depend on scale but must not use the unknown zero set or assume the desired PNT bound.

---

# 18. Campaign 28 rejection filters

Reject a candidate if:

## R1. The model primitive is subpolynomial and the argument merely subtracts it again.

## R2. The new statement is residual PESC under another name.

## R3. It uses only the current local bound $H\log^{-A}X$.

## R4. It assumes a fixed zero-free strip.

## R5. It uses a generic smoothness principle valid for arbitrary sequences.

## R6. It creates a positive higher-moment surrogate.

---

# 19. External calibration

The modern approximant used here is

$$
\Lambda^\sharp(n)
=
\frac{P(R)}{\varphi(P(R))}
1_{(n,P(R))=1},
\qquad
R=\exp((\log X)^{1/10}),
$$

and current almost-all short-interval residual bounds are of arbitrary logarithmic accuracy in the prime case.

These are the correct contemporary inputs for the present sieve-subtraction audit.

---

# 20. State transition

```text
CSM_RH v1.18
  ->
CSM_RH v1.19
```

with:

```text
Campaign 27
  CLOSED_AS_DIRECT_SIEVE_MODEL_PESC_AUDIT

B-RH-004
  SIEVE_RESIDUAL_PESC_EQUIVALENCE
  CREATED / CERTIFIED

O-RH-060
  BOUNDED_PRIMITIVE_APPROXIMANT_NEUTRALITY
  CREATED / CERTIFIED FOR LAMBDA-SHARP

O-RH-061
  LOG_LOCAL_RESIDUAL_BLIND_TO_FIXED_POWER_DRIFT
  CREATED / CERTIFIED AS STRENGTH AUDIT

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 28
  ENDOGENOUS_DRIFT_COERCIVITY_ATTACK
  READY
```

---

# 21. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

LAMBDA-SHARP SUBTRACTION = FIXED-EXPONENT NEUTRAL

MODEL PRIMITIVE = X^{o(1)}

RESIDUAL PRIMITIVE = CARRIES THE PESC-HARD DRIFT

CURRENT LOCAL RESIDUAL THEOREM = LOG-ACCURATE BUT DRIFT-BLIND

RESIDUAL SELF-CORRELATION = PESC-EQUIVALENT

NEXT CAMPAIGN = 28
```

The decisive identity is

$$
\boxed{
\mathcal C_a(N)
=
\mathcal C_f(N)
+
O(N^2X^{o(1)}).
}
$$

For first-strip exponents, the modern sieve model changes the local structure but not the global fixed-power difficulty.
