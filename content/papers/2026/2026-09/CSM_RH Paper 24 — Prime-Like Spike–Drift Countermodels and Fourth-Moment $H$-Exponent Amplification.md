# CSM_RH Paper 24
## Prime-Like Spike–Drift Countermodels and Fourth-Moment $H$ -Exponent Amplification

**Project:** `CSM_RH`  
**Paper:** `24`  
**Version:** `v0.1`  
**Date:** `2026-09-06`  
**Parent state:** `CSM_RH v1.14 / Paper 23`  
**Campaign:** `23 — PRIME_SIDE_FIXED_POWER_GENERATION_II`  
**Status:** prime-side candidate generation / one-point obstruction audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Campaign 23 asks for prime-specific information which can stop a smooth low-frequency drift from coexisting with large microscopic prime-like jump energy.

Two results are obtained.

1. One-point prime-like constraints are still insufficient: an explicit sparse nonnegative spike sequence can have prime-scale jump energy and a persistent smooth cumulative drift.

2. A centered fourth-moment exponent gap in the interval length $H$ is a genuine fixed-power generator. The hypothesis contains no power of $X$ ; a power of $X$ appears only after setting $H=X^\alpha$ and applying Hölder plus the residue-chain bridge.

No fixed-power fourth-moment theorem is proved.

---

# 1. Prime-like one-point data

On a dyadic block around $X$, the prime-only or von-Mangoldt increment has several elementary one-point features:

```text
nonnegative uncentered detector;
typical support density about 1/log X;
spike height about log X;
centered increment bounded below by -1;
one-step centered energy about X log X.
```

Paper 23 showed that large one-step energy alone cannot stop a smooth low-frequency drift.

The next question is whether adding the one-sided / sparse spike structure changes this conclusion.

It does not.

---

# 2. Spike–drift construction

Fix

$$
\frac12<\beta<1.
$$

Let

$$
L=L_X
$$

be an integer with

$$
L\asymp\log X.
$$

Define

$$
\boxed{
M_\beta(n)
=
\left\lfloor
\frac{
n+n^\beta
}{
L
}
\right\rfloor.
}
$$

For sufficiently large $n$,

$$
0<
\frac{
(n+1)+(n+1)^\beta
-
n-n^\beta
}{
L
}
<1.
$$

Hence

$$
M_\beta(n)-M_\beta(n-1)
\in
\{0,1\}.
$$

Define the nonnegative sparse detector

$$
\boxed{
q_n
=
L
[
M_\beta(n)-M_\beta(n-1)
].
}
$$

Thus

$$
\boxed{
q_n\in\{0,L\}.
}
$$

Define the centered increment

$$
\boxed{
c_n=q_n-1.
}
$$

Then

$$
\boxed{
c_n\ge-1.
}
$$

---

# 3. Exact cumulative drift

Let

$$
B(n)=\sum_{k\le n}c_k.
$$

By telescoping,

$$
B(n)
=
L M_\beta(n)-n
+
O(L)
$$

depending only on the harmless lower endpoint convention.

Therefore:

## Theorem 3.1 — Prime-Like Smooth Drift

$$
\boxed{
B(n)
=
n^\beta
+
O(L).
}
$$

Thus a sparse nonnegative spike sequence with prime-like one-point scale can carry a persistent sublinear power drift.

---

# 4. Correct spike density

On a dyadic block

$$
X<n\le2X,
$$

the number of spikes is

$$
\begin{aligned}
M_\beta(2X)-M_\beta(X)
&=
\frac{
X+(2^\beta-1)X^\beta
}{
L
}
+
O(1)
\\
&\sim
\frac XL.
\end{aligned}
$$

Therefore the support density is

$$
\boxed{
\frac1L
\asymp
\frac1{\log X}.
}
$$

The uncentered total mass is

$$
\sum_{X<n\le2X}q_n
=
X
+
(2^\beta-1)X^\beta
+
O(L),
$$

which is a main term $X$ plus a sublinear drift.

---

# 5. One-step energy

At a spike,

$$
c_n=L-1.
$$

Away from a spike,

$$
c_n=-1.
$$

Let $K_X\sim X/L$ be the number of spikes in the dyadic block.

Then

$$
\begin{aligned}
\sum_{X<n\le2X}c_n^2
&=
K_X(L-1)^2
+
(X-K_X)
\\
&=
XL
+
O(X).
\end{aligned}
$$

Hence:

## Theorem 5.1 — Prime-Scale Jump Energy

$$
\boxed{
\sum_{X<n\le2X}c_n^2
\asymp
X\log X.
}
$$

The model therefore reproduces the prime jump-energy exponent.

---

# 6. Polynomial-scale lag drift

Define

$$
U_H(x)
=
B(x+H)-B(x).
$$

For

$$
x\asymp X,
\qquad
H=o(X),
$$

Theorem 3.1 and Taylor expansion give

$$
\boxed{
U_H(x)
=
\beta H X^{\beta-1}
+
O_\beta
\left(
H^2X^{\beta-2}
+
L
\right)
}
$$

uniformly at exponent scale.

If

$$
\boxed{
H X^{\beta-1}
\gg
L,
}
$$

then the smooth drift dominates the floor/spike discrepancy.

For

$$
H=X^\alpha,
$$

this holds whenever

$$
\boxed{
\alpha>1-\beta.
}
$$

---

# 7. Long-scale energy and defect

In the drift-dominated regime,

$$
\boxed{
\mathcal S_{\rm drift}(X,H)
\asymp
H^2X^{2\beta-1}.
}
$$

The adjacent-block smooth defect has size

$$
U_H(x+H)-U_H(x)
=
O_\beta
\left(
H^2X^{\beta-2}
+
L
\right).
$$

Consequently,

$$
\boxed{
\frac{
\mathcal D(X,H)
}{
\mathcal S(X,H)
}
\ll_\beta
\left(
\frac HX
+
\frac{
L
}{
HX^{\beta-1}
}
\right)^2.
}
$$

For every fixed

$$
\alpha>1-\beta,
\qquad
H=X^\alpha,
$$

the right side tends to zero.

Thus the model has:

```text
prime-like sparse nonnegative spikes;
centered lower bound -1;
jump energy X log X;
smooth cumulative power drift;
polynomial-scale critical locking.
```

---

# 8. One-point arithmetic uncertainty is insufficient

Create:

```text
O-RH-051
PRIME_LIKE_ONE_POINT_CONSTRAINTS_INSUFFICIENT
status:
  CERTIFIED BY EXPLICIT COUNTERMODEL
```

Statement:

> Nonnegativity of the uncentered detector, support density $1/\log X$, spike height $\log X$, centered lower bound $-1$, correct total mass at leading order, and one-step energy $X\log X$ do not force polynomial-scale spectral deconcentration or PDSD.

Therefore any successful low-frequency arithmetic theorem must use genuinely higher-order information about prime locations.

---

# 9. Nonlinear moment route

The countermodel motivates a higher-correlation candidate.

Return to the actual centered von Mangoldt sequence

$$
a_n=\Lambda(n)-1
$$

on a finite prime block and define

$$
U_H(x)
=
\sum_{r=1}^{H}a_{x+r}.
$$

Define the centered fourth lag moment

$$
\boxed{
\mathcal M_{4,X}(H)
=
\sum_x
|U_H(x)|^4.
}
$$

The completely trivial pointwise estimate gives the scale

$$
\mathcal M_{4,X}(H)
\ll
XH^4
(\log X)^{O(1)}.
$$

The new candidate asks only for any fixed improvement in the exponent of $H$.

---

# 10. Fourth-Moment $H$ -Exponent Gap

Fix

$$
0<\alpha<1,
\qquad
H=X^\alpha.
$$

Fix

$$
\eta>0.
$$

Define:

## C4HEG $(\alpha,\eta)$

$$
\boxed{
\mathcal M_{4,X}(H)
\ll
XH^{4-\eta}
(\log X)^{O(1)}.
}
$$

The acronym is:

```text
C4HEG
CENTERED FOURTH-MOMENT H-EXPONENT GAP
```

No factor $X^{-\delta}$ appears in the hypothesis.

The only saving is a fixed power of the interval length $H$.

---

# 11. Hölder amplification

There are only

$$
O(X)
$$

nonzero zero-extended interval positions when $H<X$.

Therefore Hölder / Cauchy gives

$$
\begin{aligned}
\mathcal S_X(H)
&=
\sum_x|U_H(x)|^2
\\
&\le
O(X)^{1/2}
\mathcal M_{4,X}(H)^{1/2}.
\end{aligned}
$$

Under C4HEG,

$$
\boxed{
\mathcal S_X(H)
\ll
XH^{2-\eta/2}
(\log X)^{O(1)}.
}
$$

Since

$$
H=X^\alpha,
$$

this becomes

$$
\boxed{
\mathcal S_X(H)
\ll
XH^2
X^{-\alpha\eta/2}
(\log X)^{O(1)}.
}
$$

Thus a fixed $H$ -exponent gap becomes a fixed $X$ -power.

---

# 12. Global mean-square consequence

Apply Paper 17's corrected residue-chain bridge:

$$
\sum_{n\le2X}|A(n)|^2
\ll
\left(
\frac XH
\right)^2
\mathcal S_X(H)
+
XH^2,
$$

where

$$
A(n)=\psi(n)-n.
$$

Under C4HEG,

$$
\boxed{
\sum_{n\le2X}|A(n)|^2
\ll
X^3H^{-\eta/2}
(\log X)^{O(1)}
+
XH^2.
}
$$

For

$$
H=X^\alpha,
$$

the exponents are

$$
3-\frac{\alpha\eta}{2}
$$

and

$$
1+2\alpha.
$$

Therefore:

## Theorem 12.1 — Fourth-Moment Exponent Amplification

C4HEG $(\alpha,\eta)$ implies

$$
\boxed{
\sum_{n\le2X}
|\psi(n)-n|^2
\ll
X^{3-\kappa+o(1)}
}
$$

for every sufficiently small fixed

$$
\boxed{
0<\kappa
<
\min
\left\{
\frac{\alpha\eta}{2},
2-2\alpha
\right\}.
}
$$

Paper 20's Mellin pole recovery then produces a fixed zero-free strip.

Thus C4HEG is a genuine prime-side fixed-power generator.

---

# 13. General $p$ -moment amplification law

The same mechanism is not specific to the fourth moment.

Let

$$
p>2
$$

be fixed and suppose

$$
\boxed{
\sum_x|U_H(x)|^p
\ll
XH^{p-\eta}
X^{o(1)}.
}
$$

Hölder gives

$$
\boxed{
\mathcal S_X(H)
\ll
XH^{2-2\eta/p}
X^{o(1)}.
}
$$

At

$$
H=X^\alpha,
$$

the generated fixed power is

$$
\boxed{
\delta_p
=
\frac{
2\alpha\eta
}{
p
}.
}
$$

The fourth moment is the first concrete even-moment case.

---

# 14. Natural conjectural scale

Montgomery and Soundararajan predict that in polynomial short intervals the centered prime count is approximately Gaussian with variance

$$
H\log(X/H).
$$

The corresponding fourth moment scale is

$$
\boxed{
\mathcal M_{4,X}(H)
\asymp
X
[
H\log(X/H)
]^2.
}
$$

Ignoring logarithms, this is

$$
XH^2.
$$

Thus the conjectural behavior corresponds to an $H$ -exponent improvement of essentially

$$
\eta=2.
$$

C4HEG asks for only:

$$
\boxed{
\text{some fixed }\eta>0.
}
$$

It is far weaker than the full Gaussian fourth-moment conjecture.

This is plausibility calibration only.

---

# 15. Current sieve moment scale

Classical Gallagher/Klimov-type sieve moment estimates give unconditional upper bounds for uncentered short-interval prime counts of the schematic form

$$
\sum_{m\le X}
[
\psi(m+H)-\psi(m)
]^k
\ll
P_k
\left(
\frac H{\log X}
\right)
X(\log X)^k.
$$

For fixed $k=4$ and polynomial

$$
H\gg\log X,
$$

the leading term has size

$$
\boxed{
XH^4
}
$$

up to a fixed constant and lower-order terms.

Thus standard raw sieve-moment control does not produce a positive $\eta$ in C4HEG.

The missing gain must come from centering and higher correlation cancellation.

Create:

```text
O-RH-052
RAW_SIEVE_FOURTH_MOMENT_H4_FLOOR
status:
  CERTIFIED AS CURRENT-METHOD PRECISION AUDIT
```

This is not a universal impossibility theorem for sieve methods.

---

# 16. Four-point correlation expansion

Expanding the fourth moment gives a weighted sum of centered four-point correlations:

$$
\boxed{
\mathcal M_{4,X}(H)
=
\sum_{h_1,h_2,h_3}
W_H(h_1,h_2,h_3)
\sum_n
a_n
a_{n+h_1}
a_{n+h_2}
a_{n+h_3},
}
$$

where $W_H$ is a nonnegative intersection-count kernel with

$$
0\le W_H\le H
$$

and support on

$$
|h_i|\ll H.
$$

The coefficient-blind count has scale $XH^4$.

Therefore any C4HEG proof must exploit genuine cancellation or structure in a three-dimensional average of centered four-point prime correlations.

This is the first place in the current branch where one-point prime-like countermodels are automatically excluded by the theorem statement.

---

# 17. Campaign 23 track audit

## G2-1 — arithmetic low-frequency uncertainty

```text
status:
  ONE-POINT VERSION REJECTED

countermodel:
  prime-like sparse spike + smooth drift
```

A higher-correlation version may still exist.

## G2-2 — prime correlation with smooth self-generated drift

```text
status:
  CURRENT AVERAGE PRIME-CORRELATION PRECISION SUBPOWER
  NO FIXED-POWER CONTRADICTION FOUND
```

## G2-3 — nonlinear short-interval energy transfer

```text
status:
  SURVIVOR

output:
  C4HEG
```

## G2-4 — AP variance to additive-scale transfer

```text
status:
  NO NEW BRIDGE

reason:
  common q=1 low-frequency mode remains the transfer bottleneck
```

## G2-5 — direct PESC prime sampling

```text
status:
  ROOT TARGET / OPEN
```

---

# 18. New canonical theorem candidate

Create:

```text
F-RH-018
CENTERED_FOURTH_MOMENT_H_EXPONENT_GAP
abbrev:
  C4HEG
status:
  OPEN
type:
  PRIME-SIDE NONLINEAR FIXED-POWER GENERATOR
```

Its hypothesis contains no $X$ -power saving.

The fixed power is generated by:

```text
H-exponent saving
  +
polynomial relation H=X^alpha
  +
Hölder
  +
residue-chain bridge.
```

---

# 19. New survivor

Create:

```text
S-RH-029
CENTERED_FOUR_POINT_PRIME_CORRELATION_CANCELLATION
status:
  OPEN
```

A successful theorem must show a fixed $H$ -exponent gain after the full three-shift average is assembled.

It need not prove power saving for each four-point correlation separately.

---

# 20. Campaign 24

The next campaign is:

```text
CSM_RH Campaign 24
CENTERED_FOURTH_MOMENT_ATTACK
```

Root target:

```text
F-RH-010
PESC
```

Working candidates:

```text
F-RH-016
MLEPG

F-RH-018
C4HEG
```

The scale-decorrelation route PDSD remains optional.

---

# 21. Campaign 24 tracks

## M1 — averaged four-point Hardy–Littlewood

Keep the full three-dimensional shift average before absolute values.

Determine whether existing multi-correlation technology yields any fixed saving in the $H$ exponent even though it gives only logarithmic precision shiftwise.

## M2 — centered Selberg/Klimov moment method

Redo the classical sieve moment expansion after exact centering by $H$.

Identify whether the $H^4$ leading contributions cancel algebraically and where the first uncontrolled centered correlation enters.

## M3 — short-interval higher uniformity

Test whether current $U^s$ / nilsequence uniformity of $\Lambda-\Lambda^\sharp$ can control enough of the four-point aggregate to reduce the $H$ exponent.

Log-power improvement alone does not count.

## M4 — sieve approximant plus exact fourth-moment residual

Decompose

$$
\Lambda-1
=
(\Lambda^\sharp-1)
+
(\Lambda-\Lambda^\sharp)
$$

and keep all mixed fourth-moment terms signed until the exponent ledger is complete.

## M5 — direct fourth-cumulant method

Separate Gaussian pairings from the connected fourth cumulant.

C4HEG needs only an $H$ -exponent gain for the total fourth moment, not an asymptotic Gaussian law.

---

# 22. Campaign 24 rejection filters

Reject a candidate if:

## R1. It uses only uncentered moment bounds.

## R2. It assumes the prime $4$ -tuple conjecture.

## R3. It proves only a logarithmic saving over $XH^4$.

## R4. It inserts an $X^{-\delta}$ hypothesis directly.

## R5. It treats the conjectural Gaussian fourth moment as proved.

## R6. It takes absolute values of every centered four-point correlation before the proposed cancellation.

---

# 23. External calibration

Relevant literature:

1. Montgomery and Soundararajan, *Primes in short intervals*, Comm. Math. Phys. 252 (2004), develop evidence and conditional moment formulae predicting an approximately Gaussian centered prime count with variance $H\log(X/H)$ on polynomial scales.

2. Gallagher's short-interval moment method and later Bazzanella–Languasco–Zaccagnini estimates give unconditional sieve upper bounds for uncentered moments. At fourth order and polynomial $H$, the leading upper-bound scale remains $XH^4$.

3. Chan's higher-moment work studies even and odd centered moments under RH and related strong information, underscoring that sharp higher moments are already closely tied to deep zeta/prime-correlation structure.

4. Current higher-uniformity theorems for the von Mangoldt function provide arbitrary logarithmic decay in short-interval structured correlations, but no fixed $H$ -exponent gap for the centered fourth moment is identified in this audit.

None proves C4HEG.

---

# 24. State transition

```text
CSM_RH v1.14
  ->
CSM_RH v1.15
```

with:

```text
Campaign 23
  CLOSED_AS_PRIME_SIDE_CANDIDATE_GENERATION_II

O-RH-051
  PRIME_LIKE_ONE_POINT_CONSTRAINTS_INSUFFICIENT
  CREATED / CERTIFIED BY COUNTERMODEL

O-RH-052
  RAW_SIEVE_FOURTH_MOMENT_H4_FLOOR
  CREATED / CERTIFIED AS CURRENT-METHOD AUDIT

F-RH-018
  C4HEG
  CREATED / OPEN

S-RH-029
  CENTERED_FOUR_POINT_PRIME_CORRELATION_CANCELLATION
  CREATED / OPEN

F-RH-017
  PDSD
  REMAINS OPEN / OPTIONAL

F-RH-016
  MLEPG
  REMAINS OPEN

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 24
  CENTERED_FOURTH_MOMENT_ATTACK
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

PDSD = OPEN / OPTIONAL

C4HEG = OPEN

ONE-POINT PRIME-LIKE CONSTRAINT ROUTE = CLOSED

FOURTH-MOMENT FIXED H-EXPONENT GAP = NEW SURVIVOR

CURRENT RAW SIEVE MOMENTS = H^4 SCALE

NEXT CAMPAIGN = 24
```

The new theorem candidate is:

$$
\boxed{
\sum_x
\left|
\sum_{r=1}^{X^\alpha}
[
\Lambda(x+r)-1
]
\right|^4
\ll
X
\left(
X^\alpha
\right)^{4-\eta}
(\log X)^{O(1)}
}
$$

for some fixed

$$
0<\alpha<1,
\qquad
\eta>0.
$$

Any fixed positive $\eta$ generates a fixed prime-number-theorem mean-square power through Hölder and the already certified residue-chain bridge.
