# CSM_RH Paper 06
## Critical Selberg Contraction, Cumulative-Gap Classification, and Multiplicative Gram Neutrality

**Project:** `CSM_RH`  
**Paper:** `06`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v0.6 / Paper 05`  
**Campaign:** `05 — ZERO_FREQUENCY_MULTIPLICATIVE_CONTRACTION`  
**Status:** contraction-classification / multiplicative-decomposition audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

Canonical state:

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

This paper does not prove a fixed-power CSSA estimate.

Its purpose is to determine exactly what kind of contraction a successful multiplicative argument must produce.

The main conclusions are:

```text
FIXED POINTWISE GAP
  sufficient but not necessary

LINEAR CUMULATIVE CONTRACTION MASS
  exact scale-level criterion for a power-law contraction mechanism

SELBERG BASIC SYMMETRY
  critical at first absolute-value closure

SELBERG SIGNED IMPROVEMENT
  nonlinear amplitude contraction with vanishing relative gap

EXACT VAUGHAN / HEATH-BROWN STYLE DECOMPOSITION
  contraction-neutral until a new Gram/correlation estimate is proved

NEW FRONTIER
  MULTIPLICATIVE_GRAM_GAP_CERTIFICATE
```

No theorem below claims that elementary or multiplicative methods can never prove a fixed zero strip.

The result is a typed audit of what the decomposition itself does and does not provide.

---

# 1. Canonical normalized frontier

The centered signed shift aggregate is

$$
\mathcal A_N
=
\sum_{h=1}^{2N-2}
\mathcal R_N(h).
$$

Define

$$
\boxed{
X(N)
=
\frac{
|\mathcal A_N|
}{
N^3
}.
}
$$

The fixed-power target is:

$$
\boxed{
X(N)
\ll
N^{-\kappa+o(1)}
}
$$

for some fixed

$$
\kappa>0.
$$

Paper 05 supplied one sufficient mechanism:

$$
X(N)
\le
\lambda X(\theta N)
+
O(N^{-\kappa_0}),
$$

with fixed

$$
0<\lambda<1,
\qquad
0<\theta<1.
$$

The present paper replaces this by a more general cumulative criterion.

---

# 2. Geometric scale normalization

Fix

$$
q>1.
$$

Let

$$
N_k
=
N_0q^k,
$$

and write

$$
Y_k
=
X(N_k).
$$

Suppose an arithmetic argument yields

$$
\boxed{
Y_k
\le
\lambda_kY_{k-1}
+
C N_k^{-\kappa_0},
}
$$

where

$$
0<\lambda_k\le1
$$

and

$$
\kappa_0>0.
$$

Define the log-contraction increment

$$
g_k
=
-\log\lambda_k
\ge0.
$$

For

$$
0\le m<k,
$$

define cumulative contraction mass

$$
\boxed{
G_{m,k}
=
\sum_{r=m+1}^{k}g_r.
}
$$

---

# 3. Exact iteration formula

Repeated substitution gives:

## Lemma 3.1

$$
\boxed{
Y_k
\le
e^{-G_{0,k}}Y_0
+
C
\sum_{m=1}^{k}
N_m^{-\kappa_0}
e^{-G_{m,k}}.
}
$$

### Proof

Iterating once gives

$$
Y_k
\le
\lambda_k\lambda_{k-1}Y_{k-2}
+
C\lambda_kN_{k-1}^{-\kappa_0}
+
CN_k^{-\kappa_0}.
$$

Continuing to scale $N_0$ gives the stated product formula.

Because

$$
\prod_{r=m+1}^{k}\lambda_r
=
\exp
\left(
-
G_{m,k}
\right),
$$

the result follows. $\square$

The recurrence is therefore controlled by cumulative log-contraction, not by one individual scale.

---

# 4. Linear cumulative-gap theorem

## Theorem 4.1 — Linear cumulative contraction gives a fixed power

Assume there exist constants

$$
\delta>0
$$

and

$$
C_0\ge0
$$

such that for every

$$
0\le m<k,
$$

$$
\boxed{
G_{m,k}
\ge
\delta
\log
\left(
\frac{N_k}{N_m}
\right)
-
C_0.
}
$$

Then

$$
\boxed{
Y_k
\ll
N_k^{-\min(\delta,\kappa_0)+o(1)}.
}
$$

Equivalently,

$$
\boxed{
X(N)
\ll
N^{-\kappa+o(1)}
}
$$

along the geometric scale sequence, with

$$
\kappa
=
\min(\delta,\kappa_0)>0.
$$

### Proof

The hypothesis gives

$$
e^{-G_{m,k}}
\ll
\left(
\frac{N_m}{N_k}
\right)^\delta.
$$

Insert this into Lemma 3.1:

$$
Y_k
\ll
N_k^{-\delta}
+
N_k^{-\delta}
\sum_{m=1}^{k}
N_m^{\delta-\kappa_0}.
$$

Since $N_m$ is geometric:

- if $\delta<\kappa_0$, the sum is bounded;
- if $\delta>\kappa_0$, the last scale dominates and gives $N_k^{\delta-\kappa_0}$ ;
- if $\delta=\kappa_0$, the sum contributes only a factor $k=O(\log N_k)$.

Thus

$$
Y_k
\ll
N_k^{-\min(\delta,\kappa_0)}
\log N_k,
$$

with the logarithm required only at the endpoint.

This is

$$
N_k^{-\min(\delta,\kappa_0)+o(1)}.
$$

 $\square$

---

# 5. Converse audit: sublinear cumulative mass cannot force a fixed power by recurrence alone

The previous condition is also the correct recurrence-level obstruction.

## Theorem 5.1 — Homogeneous countermodel

Suppose only the recurrence class is specified and

$$
G_{0,k}
=
o
\left(
\log N_k
\right).
$$

Then that recurrence class alone cannot force

$$
Y_k
=
O(N_k^{-\kappa})
$$

for any fixed

$$
\kappa>0.
$$

### Proof

Set the additive error equal to zero and take equality:

$$
Y_k
=
\lambda_kY_{k-1}.
$$

Then

$$
Y_k
=
Y_0e^{-G_{0,k}}.
$$

If

$$
G_{0,k}
=
o(\log N_k),
$$

then

$$
Y_k
=
N_k^{-o(1)}.
$$

For every fixed

$$
\kappa>0,
$$

this is asymptotically larger than a generic

$$
N_k^{-\kappa}
$$

power.

Therefore no fixed power follows from the recurrence shape alone. $\square$

This is not a counterexample to the arithmetic truth of CSSA.

It is a countermodel to an insufficient contraction certificate.

---

# 6. Canonical success criterion

The correct Campaign 05 criterion is therefore not merely

$$
\lambda_k<1.
$$

It is:

$$
\boxed{
G_{0,k}
\asymp
\log N_k
}
$$

at least from below, with the stronger tail-uniform version from Theorem 4.1 when additive errors are present.

In words:

> a fixed power requires contraction mass linear in logarithmic scale depth.

A fixed

$$
\lambda<1
$$

is one way to obtain this.

It is not the only way.

---

# 7. Model vanishing-gap classification

Let

$$
t_k
=
\log N_k
=
t_0+kL,
$$

where

$$
L=\log q.
$$

Consider

$$
\lambda_k
=
1-
\frac{c}{t_k^a},
$$

for sufficiently large $k$, with

$$
c>0,
\qquad
a\ge0.
$$

For

$$
a>0,
$$

$$
-\log\lambda_k
=
\frac{c}{t_k^a}
+
O
\left(
t_k^{-2a}
\right).
$$

Summation gives the following classification.

## Theorem 7.1 — Contraction spectrum

### Case A: $a=0$

The gap is fixed:

$$
\lambda_k=1-c.
$$

Then

$$
G_{0,k}
=
\frac{
-\log(1-c)
}{
L
}
t_k
+
O(1).
$$

Hence a fixed power follows.

### Case B: $0<a<1$

$$
G_{0,k}
=
\frac{
c
}{
L(1-a)
}
t_k^{1-a}
+
o
\left(
t_k^{1-a}
\right).
$$

Thus the homogeneous decay is

$$
\boxed{
Y_k
=
\exp
\left[
-
\frac{
c+o(1)
}{
L(1-a)
}
(\log N_k)^{1-a}
\right].
}
$$

This is subpower:

$$
Y_k
=
N_k^{-o(1)}.
$$

### Case C: $a=1$

$$
G_{0,k}
=
\frac cL
\log t_k
+
O(1),
$$

so

$$
\boxed{
Y_k
\asymp
(\log N_k)^{-c/L}
}
$$

at homogeneous scale.

### Case D: $a>1$

The series

$$
\sum_k
t_k^{-a}
$$

converges.

Therefore

$$
G_{0,k}
$$

remains bounded.

The recurrence does not force $Y_k$ to tend to zero.

---

# 8. Why subexponential-in-log error is still subpower

For

$$
0<a<1,
$$

the decay

$$
\exp
\left[
-c
(\log N)^{1-a}
\right]
$$

may be much stronger than any fixed power of

$$
\log N.
$$

But for every fixed

$$
\kappa>0,
$$

$$
\exp
\left[
-c
(\log N)^{1-a}
\right]
\gg
N^{-\kappa}
$$

for sufficiently large $N$.

Thus:

```text
stretched exponential in log N
  !=
fixed power of N
```

This distinction is exactly the distinction relevant to the CSSA frontier.

---

# 9. Selberg symmetry as a critical contraction calibrator

Write

$$
R(x)
=
\Psi(x)-x.
$$

A standard Selberg symmetry formula has the form

$$
\boxed{
R(x)
+
\sum_{n\le x}
R(x/n)
\frac{
\Lambda(n)
}{
\log x
}
=
O
\left(
\frac{x}{\log x}
\right).
}
$$

Suppose one has the inductive bound

$$
|R(t)|
\le
\beta t
+
O(1)
$$

for smaller arguments.

Applying the triangle inequality to the first symmetry relation gives

$$
|R(x)|
\le
\beta x
+
O
\left(
\frac{x}{\log x}
\right).
$$

Thus the obvious contraction coefficient is exactly critical:

$$
\boxed{
\beta
\mapsto
\beta.
}
$$

No strict improvement occurs.

This is a classical feature of the elementary PNT proof: the first weighted identity removes almost enough mass, but not enough to close by naïve induction.

---

# 10. Selberg signed improvement is nonlinear amplitude contraction

The second signed formula in the Selberg argument contains two sums with opposite signs.

A standard proof sketch obtains an improvement of the form

$$
\boxed{
\beta_{\rm new}
\le
\beta
-
c_0\beta^2
}
$$

for an absolute

$$
c_0>0
$$

within the iteration regime.

One explicit exposition uses

$$
c_0=0.007.
$$

The relative contraction factor is

$$
\boxed{
\frac{
\beta_{\rm new}
}{
\beta
}
\le
1-c_0\beta.
}
$$

As

$$
\beta\to0,
$$

this factor tends to one.

Therefore the signed Selberg mechanism is a genuine contraction, but its relative gap vanishes with the current error amplitude.

---

# 11. Amplitude iteration law

Assume

$$
0<c_0\beta_m<1
$$

and

$$
\beta_{m+1}
\le
\beta_m-c_0\beta_m^2.
$$

Then

$$
\beta_{m+1}
\le
\beta_m
(
1-c_0\beta_m
).
$$

Hence

$$
\frac1{\beta_{m+1}}
\ge
\frac1{\beta_m}
+
c_0,
$$

up to a harmless stronger denominator correction.

Therefore:

## Proposition 11.1

$$
\boxed{
\beta_m
=
O
\left(
\frac1m
\right).
}
$$

This is enough to drive the normalized PNT error amplitude to zero after indefinitely many valid iterations.

It is not a fixed multiplicative contraction.

Even under the idealized assumption that one such iteration were available per fixed logarithmic scale step, so that

$$
m\asymp\log x,
$$

the resulting direct amplitude profile would only be of logarithmic type.

The actual Selberg proof does not supply such a uniform fixed-scale iteration schedule; this observation is only a strength calibration.

---

# 12. Historical elementary error terms and the contraction spectrum

Classical refinements of the Selberg mechanism go beyond the first amplitude iteration.

Historically:

- Bombieri and Wirsing obtained
  $$
  \psi(x)
  =
  x
  +
  O_A
  \left(
  \frac{x}{\log^A x}
  \right)
  $$
  for arbitrary fixed $A>0$ by generalized elementary methods;
- later elementary work obtained stretched-exponential-in-log errors, with a record of the shape
  $$
  \psi(x)
  =
  x
  +
  O
  \left(
  x
  \exp
  [
  -c(\log x)^{1/6}
  ]
  \right)
  $$
  in the historical literature.

These are much stronger than the original qualitative PNT.

But they remain

$$
x^{1-o(1)}
$$

rather than

$$
x^{1-\delta}
$$

for fixed

$$
\delta>0.
$$

This is consistent with the contraction-spectrum distinction:

```text
sublinear cumulative contraction mass
  -> subpower error

linear cumulative contraction mass
  -> fixed power
```

No impossibility claim for future elementary methods is made.

---

# 13. Multiplicative decompositions are exact rewrites before estimation

Now consider any exact finite decomposition on the required range:

$$
\boxed{
a_n
=
\sum_{r=1}^{R}
b_n^{(r)}.
}
$$

This abstractly includes the role played by truncated Vaughan-, Heath-Brown-, Selberg-, or other convolution decompositions after all coefficients and cutoffs have been fixed.

Define cumulative component errors

$$
B_r(j)
=
\sum_{n\le j}
b_n^{(r)}.
$$

Then

$$
A(j)
=
\sum_{r=1}^{R}
B_r(j).
$$

---

# 14. Multiplicative Gram identity

Define the Hilbert inner product on the dyadic endpoint interval:

$$
\langle U,V\rangle_N
=
\sum_{j=N}^{2N-1}
U(j)\overline{V(j)}.
$$

Let

$$
G_{rs}(N)
=
\langle
B_r,
B_s
\rangle_N.
$$

Then:

## Theorem 14.1 — Exact Gram reconstruction

$$
\boxed{
J_N
=
\sum_{r,s=1}^{R}
G_{rs}(N).
}
$$

Equivalently, if

$$
\mathbf 1
=
(1,\ldots,1)^T,
$$

then

$$
\boxed{
J_N
=
\mathbf 1^\ast
G_N
\mathbf 1.
}
$$

Because $G_N$ is a Gram matrix,

$$
G_N\succeq0.
$$

This is exact.

---

# 15. Triangle / Cauchy closes the decomposition without contraction

By the Hilbert triangle inequality,

$$
\|A\|_N
=
\left\|
\sum_r
B_r
\right\|_N
\le
\sum_r
\|B_r\|_N.
$$

Therefore

$$
\boxed{
J_N
\le
\left(
\sum_r
\sqrt{
G_{rr}(N)
}
\right)^2.
}
$$

This inequality contains no strict contraction coefficient.

It is sharp when the component vectors are positively collinear.

Therefore:

## Theorem 15.1 — Exact-decomposition neutrality

An exact multiplicative decomposition, followed only by componentwise triangle inequality or Cauchy-Schwarz, does not itself provide a fixed contraction gap for $J_N$ or CSSA.

Any fixed-power gain must enter through additional arithmetic information about:

1. the diagonal component norms;
2. the off-diagonal Gram terms;
3. a two-scale transfer law;
4. or another noncircular structural estimate.

The decomposition is an interface.

It is not the saving.

---

# 16. Where a real multiplicative gain may occur

A successful Vaughan / Heath-Brown / Selberg-style worker result must therefore prove at least one genuinely new statement of the following types.

## Type M1 — component power saving

For a decomposition piece,

$$
\|B_r\|_N^2
\ll
N^{3-\eta}
$$

with enough uniformity to sum all pieces without losing the gain.

## Type M2 — Gram cross-cancellation

Prove a structurally forced estimate such as

$$
2
\sum_{r<s}
\Re
G_{rs}(N)
\le
-\delta
\sum_r
G_{rr}(N)
+
\mathcal E_N
$$

with

$$
\delta>0
$$

and a lower-order error.

## Type M3 — two-scale contraction

Prove

$$
X(N_k)
\le
\lambda_k
X(N_{k-1})
+
O(N_k^{-\kappa_0})
$$

with contraction mass satisfying Theorem 4.1.

## Type M4 — direct recombined cancellation

Control

$$
\mathbf 1^\ast G_N\mathbf 1
$$

directly without taking absolute values on the individual Gram entries.

All four are genuine arithmetic estimates.

None is supplied by the convolution identity alone.

---

# 17. New obstruction: exact decomposition neutrality

Create:

```text
O-RH-010
EXACT_MULTIPLICATIVE_DECOMPOSITION_NEUTRALITY
status:
  CERTIFIED
```

Statement:

> Replacing $\Lambda$ by an exact Vaughan-, Heath-Brown-, Selberg-, or other finite convolution decomposition does not create contraction by itself. After cumulative summation the PNT mean square is exactly the all-ones quadratic form of the component Gram matrix. A saving requires new norm, cross-Gram, or scale-transfer information.

This does not reject those methods.

It identifies their real proof obligation.

---

# 18. New obstruction: sublinear contraction mass

Create:

```text
O-RH-011
SUBLINEAR_CONTRACTION_MASS
status:
  CERTIFIED_AS_RECURRENCE_OBSTRUCTION
```

Statement:

> A scale recurrence whose cumulative log-contraction is only $o(\log N)$ cannot, by recurrence structure alone, force a fixed $N^{-\kappa}$ saving.

This is a statement about the recurrence certificate, not about the arithmetic function outside that certificate.

---

# 19. New canonical frontier

Create:

```text
F-RH-007
MULTIPLICATIVE_GRAM_GAP_CERTIFICATE
abbrev:
  MGGC
status:
  OPEN
```

A valid MGGC may take any of the forms M1–M4 from Section 16, provided it yields either:

$$
X(N)
\ll
N^{-\kappa}
$$

directly, or a recurrence whose cumulative contraction mass is linear in

$$
\log N.
$$

---

# 20. New survivors

Create:

```text
S-RH-012
LINEAR_CUMULATIVE_CONTRACTION_MASS
status:
  OPEN / SURVIVOR
```

and:

```text
S-RH-013
SIGNED_MULTIPLICATIVE_GRAM_CANCELLATION
status:
  OPEN / SURVIVOR
```

These replace the overly narrow requirement that every scale individually have one fixed contraction ratio.

---

# 21. Campaign 05 candidate audit

## C05-A — Basic Selberg symmetry

```text
status:
  CRITICAL / NO FIXED GAP

certificate:
  naive beta -> beta
```

It is sufficient as a starting point for PNT.

It is not a fixed-power contraction.

---

## C05-B — Signed Selberg second relation

```text
status:
  GENUINE AMPLITUDE CONTRACTION
  VANISHING RELATIVE GAP

profile:
  beta -> beta - c beta^2
```

It proves qualitative decay.

It does not provide a fixed relative contraction as $\beta\to0$.

---

## C05-C — Higher-weight Selberg / Bombieri / Wirsing style recursion

```text
status:
  HISTORICALLY STRONG SUBPOWER MECHANISM
  NO FIXED POWER CURRENTLY CERTIFIED
```

Known elementary remainder improvements are consistent with sublinear cumulative contraction mass.

This is not a no-go theorem against future higher-weight identities.

---

## C05-D — Vaughan decomposition

```text
status:
  INTERFACE SURVIVES
  DECOMPOSITION-ONLY GAP = NONE
```

Required new input:

```text
Type I / II cumulative norm saving
or
cross-Gram cancellation
or
two-scale contraction
```

---

## C05-E — Heath-Brown decomposition

```text
status:
  INTERFACE SURVIVES
  DECOMPOSITION-ONLY GAP = NONE
```

The additional multilinear resolution may expose more cancellation opportunities.

But the exact identity alone remains MGGC-neutral.

---

## C05-F — Fixed-gap recurrence

```text
status:
  VALID SUFFICIENT SPECIAL CASE
```

It is now subsumed by the more general linear cumulative-gap theorem.

---

# 22. Campaign 05 verdict

Campaign 05 asked whether a standard multiplicative decomposition could itself provide the missing fixed-gap contraction.

The answer is:

```text
BASIC SELBERG
  critical

SIGNED SELBERG
  contracting but asymptotically critical

KNOWN HIGHER-WEIGHT ELEMENTARY METHODS
  strong subpower, not fixed power

VAUGHAN / HEATH-BROWN EXACT DECOMPOSITION
  contraction-neutral until new arithmetic estimates are supplied

FIXED POINTWISE GAP
  sufficient but too restrictive as a search specification

LINEAR CUMULATIVE GAP
  correct generalized success criterion

MULTIPLICATIVE GRAM GAP
  next irreducible frontier
```

No fixed-power estimate has been proved.

But the next proof obligation is now materially smaller and more falsifiable.

---

# 23. Campaign 06

The next campaign is:

```text
CSM_RH Campaign 06
MULTIPLICATIVE_GRAM_GAP
```

The worker must choose one exact decomposition and output an explicit Gram-gap certificate.

The campaign must not accept:

```text
"Vaughan identity gives cancellation"
```

or:

```text
"Type II sums should be square-root size"
```

without an explicit theorem and exponent ledger.

---

# 24. Campaign 06 required output

For every candidate decomposition, the worker must provide:

```text
1. exact coefficient identity
2. cutoff parameters
3. cumulative component functions B_r(j)
4. Gram matrix entries G_rs(N)
5. which entries carry the saving
6. proof of the saving
7. recombination without triangle leakage
8. scale-transfer law if used
9. cumulative contraction mass
10. resulting kappa
11. hidden-zero-strip audit
12. failure mode
```

If a proposed recurrence has coefficients $\lambda_k$, the worker must compute:

$$
\boxed{
G_{m,k}
=
\sum_{r=m+1}^{k}
-\log\lambda_r
}
$$

and explicitly test whether it is linear in

$$
\log(N_k/N_m).
$$

---

# 25. Hard rejection filters for Campaign 06

Reject a candidate if:

## R1. Decomposition-only rhetoric

An exact identity is presented as if it were already an estimate.

## R2. Triangle leakage

Cross terms are individually absolutized before the proposed cancellation.

## R3. Critical contraction hidden as strict contraction

A coefficient

$$
\lambda_k\to1
$$

is called a fixed gap without cumulative-mass analysis.

## R4. Subpower advertised as fixed power

A bound such as

$$
\exp[-c(\log N)^\alpha],
\qquad
0<\alpha<1,
$$

is not

$$
N^{-\kappa}.
$$

## R5. Hidden zero-strip input

The new estimate assumes a fixed zero-free half-plane.

## R6. Finite Gram numerics promoted globally

Numerics may reject a conjectured sign law.

They cannot certify asymptotic MGGC.

---

# 26. External calibration

The standard Selberg symmetry formula and its elementary PNT use are documented in modern analytic-number-theory lecture notes.

One standard proof sketch explicitly observes that the first absolute-value induction only reproduces the same constant $\beta$, and then uses a second signed identity to improve

$$
\beta
$$

to

$$
\beta-c\beta^2.
$$

Historical surveys of elementary PNT error terms record progressively stronger estimates:

$$
x\log^{-A}x
$$

for arbitrary fixed $A$, followed by stretched-exponential-in-log errors of the form

$$
x\exp[-c(\log x)^{1/6}].
$$

These provide calibration for the distinction between:

```text
qualitative / subpower self-improvement
and
fixed-power contraction.
```

They are not used to prove any impossibility theorem.

---

# 27. State transition

The canonical transition is:

```text
CSM_RH v0.6
  ->
CSM_RH v0.7
```

with:

```text
Campaign 05
  CLOSED_AS_CONTRACTION_CLASSIFICATION_AUDIT

F-RH-007
  MULTIPLICATIVE_GRAM_GAP_CERTIFICATE
  CREATED / OPEN

O-RH-010
  EXACT_MULTIPLICATIVE_DECOMPOSITION_NEUTRALITY
  CREATED / CERTIFIED

O-RH-011
  SUBLINEAR_CONTRACTION_MASS
  CREATED / CERTIFIED_AS_RECURRENCE_OBSTRUCTION

S-RH-012
  LINEAR_CUMULATIVE_CONTRACTION_MASS
  CREATED / OPEN

S-RH-013
  SIGNED_MULTIPLICATIVE_GRAM_CANCELLATION
  CREATED / OPEN

Campaign 06
  MULTIPLICATIVE_GRAM_GAP
  READY
```

---

# 28. Final status

```text
RH = OPEN

CSSA FIXED POWER = OPEN

FIXED-GAP SEARCH
= GENERALIZED TO CUMULATIVE-GAP SEARCH

SELBERG BASIC CONTRACTION
= CRITICAL

SELBERG SIGNED CONTRACTION
= REAL BUT VANISHING-GAP

EXACT MULTIPLICATIVE DECOMPOSITION
= NEUTRAL UNTIL ESTIMATED

MULTIPLICATIVE GRAM GAP
= OPEN

NEXT CAMPAIGN
= 06
```

The principal criterion is now:

$$
\boxed{
G_{m,k}
\gtrsim
\delta
\log
\left(
\frac{N_k}{N_m}
\right)
}
$$

for some fixed

$$
\delta>0.
$$

The missing theorem is no longer "find a clever identity."

It is:

> prove enough arithmetic cancellation inside an exact multiplicative Gram expansion that the cumulative contraction mass is linear in logarithmic scale depth, or obtain the fixed CSSA power directly.
