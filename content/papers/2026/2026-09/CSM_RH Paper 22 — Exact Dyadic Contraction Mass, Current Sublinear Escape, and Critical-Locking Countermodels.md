# CSM_RH Paper 22
## Exact Dyadic Contraction Mass, Current Sublinear Escape, and Critical-Locking Countermodels

**Project:** `CSM_RH`  
**Paper:** `22`  
**Version:** `v0.1`  
**Date:** `2026-09-06`  
**Parent state:** `CSM_RH v1.12 / Paper 21`  
**Campaign:** `21 — DYADIC_PRIME_ERROR_DECORRELATION_ATTACK`  
**Status:** multiscale contraction audit / range correction; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 21 introduced PDSD as a sufficient prime-side mechanism:

> a constant decorrelation gap on a positive density of dyadic lag scales generates a fixed power.

The present campaign asks whether current prime technology or deterministic multiscale geometry can prove that mechanism.

The result is:

```text
exact cumulative contraction mass:
  certified

current unconditional contraction mass:
  sublinear in log X

pure finite-support geometry:
  only vanishing relative gaps

smooth low-frequency drift:
  explicit critical-locking countermodel

current average prime-pair technology:
  no fixed relative adjacent-scale gap

PDSD:
  open
```

The paper also corrects an earlier range restriction: the residue-chain bridge permits every fixed $0<\alpha<1$, not only $\alpha<2/3$.

---

# 1. Dyadic lag energy

Let

$$
a_n=\Lambda(n)-1
$$

on a finite dyadic prime block and extend by zero outside the chosen block.

Define

$$
U_H(x)
=
\sum_{r=1}^{H}a_{x+r},
$$

$$
\mathcal S_X(H)
=
\sum_x|U_H(x)|^2,
$$

and

$$
R_X(H)
=
\frac{\mathcal S_X(H)}{XH^2}.
$$

The exact two-scale relation from Paper 21 is

$$
\mathcal S_X(2H)
=
2\mathcal S_X(H)
+
2\mathcal C_X(H),
$$

where

$$
\mathcal C_X(H)
=
\Re\sum_xU_H(x)\overline{U_H(x+H)}.
$$

---

# 2. Exact dyadic defect

Define

$$
\boxed{
\mathcal D_X(H)
=
4\mathcal S_X(H)
-
\mathcal S_X(2H).
}
$$

Then:

## Theorem 2.1 — Exact Adjacent-Block Defect Identity

$$
\boxed{
\mathcal D_X(H)
=
\sum_x
|U_H(x)-U_H(x+H)|^2
\ge0.
}
$$

### Proof

Expand:

$$
\begin{aligned}
\sum_x|U_H(x)-U_H(x+H)|^2
&=
2\mathcal S_X(H)
-
2\mathcal C_X(H)
\\
&=
4\mathcal S_X(H)
-
[
2\mathcal S_X(H)
+
2\mathcal C_X(H)
]
\\
&=
4\mathcal S_X(H)-\mathcal S_X(2H).
\end{aligned}
$$

 $\square$

Thus critical locking means that adjacent length- $H$ prime-error blocks are nearly identical in $L^2$.

---

# 3. Exact local contraction coefficient

For scales with $\mathcal S_X(H)>0$, define

$$
\boxed{
q_X(H)
=
\frac{\mathcal S_X(2H)}
{
4\mathcal S_X(H)
}.
}
$$

Then

$$
0\le q_X(H)\le1
$$

and

$$
\boxed{
q_X(H)
=
1-
\frac{
\mathcal D_X(H)
}{
4\mathcal S_X(H)
}.
}
$$

Moreover,

$$
\boxed{
R_X(2H)
=
q_X(H)R_X(H).
}
$$

This is exact.

---

# 4. Exact cumulative contraction mass

Let

$$
H_j=2^jH_0.
$$

Define

$$
\boxed{
G_X(J)
=
\sum_{j=0}^{J-1}
-\log q_X(H_j),
}
$$

with the convention that $G_X(J)=+\infty$ if one of the ratios vanishes.

Then:

## Theorem 4.1 — Exact Contraction-Mass Telescoping Law

$$
\boxed{
G_X(J)
=
\log
\frac{
R_X(H_0)
}{
R_X(H_J)
}.
}
$$

Equivalently,

$$
\boxed{
R_X(H_J)
=
R_X(H_0)e^{-G_X(J)}.
}
$$

This is the exact prime-side realization of the abstract cumulative contraction mass introduced in Paper 06.

---

# 5. Minimal multiscale fixed-power condition

Suppose

$$
R_X(H_0)=X^{o(1)}.
$$

Then a fixed-power bound

$$
R_X(H_J)
\le
X^{-\delta+o(1)}
$$

is obtained whenever

$$
\boxed{
G_X(J)
\ge
\delta\log X
+
o(\log X).
}
$$

Conversely, if

$$
G_X(J)=o(\log X),
$$

then the scale chain by itself yields only

$$
R_X(H_J)
=
X^{-o(1)}
$$

up to the initial subpolynomial factor.

Thus the exact threshold remains:

$$
\boxed{
\text{linear contraction mass in }\log X.
}
$$

PDSD is one sufficient mechanism for producing this linear mass.

---

# 6. PDSD is sufficient but not necessary

Paper 21 requires that on a positive density $d$ of scales,

$$
q_X(H_j)
\le
1-\frac{\varepsilon}{2}.
$$

Then

$$
G_X(J)
\ge
dJ
\log
\frac1{
1-\varepsilon/2
},
$$

which is linear in $\log X$.

However linear cumulative contraction can also arise from nonuniform gaps.

Therefore:

```text
PDSD
  sufficient

linear cumulative contraction mass
  exact minimal scale-dynamical condition
```

The latter is a diagnostic identity, not a new canonical frontier.

---

# 7. Initial-scale normalization

At unit lag,

$$
\mathcal S_X(1)
=
\sum
[\Lambda(n)-1]^2
$$

on the chosen dyadic prime block.

The prime number theorem gives

$$
\boxed{
\mathcal S_X(1)
\sim
X\log X.
}
$$

Hence

$$
\boxed{
R_X(1)
\asymp
\log X.
}
$$

Thus unit scale supplies only a logarithmic initial cost.

---

# 8. Current unconditional contraction mass

Current Guth–Maynard large-value technology gives, after the standard explicit-formula $L^2$ argument, a subpower saving for almost-all short intervals at every fixed scale

$$
H=X^\alpha,
\qquad
\alpha>\frac2{15}+\varepsilon.
$$

At exponent-resolution level this has the form

$$
\boxed{
R_X(H)
\ll
\exp
\left(
-c(\log X)^{1/4}
\right)
}
$$

after localization and absorption of standard boundary/logarithmic factors.

Combining with

$$
R_X(1)\asymp\log X
$$

and Theorem 4.1 yields:

## Proposition 8.1 — Current Sublinear Escape

For such a target scale,

$$
\boxed{
G_X(J)
\ge
c'(\log X)^{1/4}
+
O(\log\log X).
}
$$

Thus current technology proves genuine escape from complete dyadic locking.

But

$$
(\log X)^{1/4}
=
o(\log X).
$$

Therefore it does not reach fixed-power contraction mass.

The precise root-log exponent is not the structural issue.

The structural gap is:

$$
\boxed{
o(\log X)
\quad\text{versus}\quad
\Omega(\log X).
}
$$

---

# 9. Endpoint control does not imply positive-density good scales

A lower bound on the total mass

$$
G_X(J)
$$

does not determine how that contraction is distributed among the scales.

The entire sublinear mass could, in principle, be concentrated in a sparse collection of scales.

Therefore the current endpoint short-interval theorem does not imply PDSD.

In particular,

$$
G_X(J)
\gg
(\log X)^{1/4}
$$

does not imply that a fixed positive proportion of the

$$
J\asymp\log X
$$

scales have a fixed contraction gap.

---

# 10. Deterministic finite-support Poincare gap

The critical-locking condition also has a purely functional-analytic lower bound.

Let $f$ be any nonzero sequence supported on an interval of length $O(X)$.

For shift $H$, decompose the sequence into residue classes modulo $H$.

Each residue class is a finite path of length

$$
M
=
O(X/H).
$$

The discrete Dirichlet Poincare inequality gives

$$
\boxed{
\sum_x|f(x)-f(x+H)|^2
\gg
\left(
\frac HX
\right)^2
\sum_x|f(x)|^2.
}
$$

Apply this to

$$
f(x)=U_H(x).
$$

Then:

## Theorem 10.1 — Universal Finite-Support Defect

$$
\boxed{
\frac{
\mathcal D_X(H)
}{
\mathcal S_X(H)
}
\gg
\left(
\frac HX
\right)^2.
}
$$

This proves that perfect locking is impossible for a nonzero finite sequence.

But the gap vanishes as $H/X\to0$.

---

# 11. Deterministic gap is exponent-insufficient

Let

$$
H_j\le X^\alpha
$$

for fixed

$$
0<\alpha<1.
$$

The universal Poincare gaps contribute at most the scale order

$$
\sum_{H_j\le X^\alpha}
\left(
\frac{H_j}{X}
\right)^2
\asymp
X^{-2(1-\alpha)}.
$$

This tends to zero.

Therefore finite support alone supplies no linear cumulative contraction mass.

Create:

```text
O-RH-047
FINITE_SUPPORT_POINCARE_GAP_INSUFFICIENCY
status:
  CERTIFIED
```

---

# 12. Smooth-drift critical-locking model

The preceding phenomenon is not merely an artifact of a weak Poincare inequality.

Consider a smooth power mode on a dyadic physical interval:

$$
\boxed{
A_\rho(x)=x^\rho,
}
$$

where $\rho$ is fixed.

Let

$$
U_{\rho,H}(x)
=
A_\rho(x+H)-A_\rho(x).
$$

For

$$
x\asymp X,
\qquad
H=o(X),
$$

Taylor expansion gives

$$
U_{\rho,H}(x)
=
\rho Hx^{\rho-1}
\left[
1+
O_\rho(H/X)
\right].
$$

Hence

$$
U_{\rho,H}(x+H)
=
U_{\rho,H}(x)
\left[
1+
O_\rho(H/X)
\right].
$$

Therefore:

## Proposition 12.1 — Smooth Drift Locks Adjacent Scales

For fixed $\rho$,

$$
\boxed{
\frac{
\sum_{x\asymp X}
|
U_{\rho,H}(x+H)-U_{\rho,H}(x)
|^2
}{
\sum_{x\asymp X}
|
U_{\rho,H}(x)
|^2
}
=
O_\rho
\left(
\frac{H^2}{X^2}
\right).
}
$$

Thus a smooth power mode is asymptotically maximally correlated across adjacent short intervals.

---

# 13. Interpretation for a fixed zeta-zero mode

A fixed explicit-formula zero mode has the form

$$
x^\rho
$$

up to its coefficient.

Therefore, at every sublinear scale

$$
H=X^\alpha,
\qquad
\alpha<1,
$$

one fixed zero mode is a scale-locked low-frequency drift in the sense of Proposition 12.1.

This explains structurally why no universal deterministic theorem can prove a fixed PDSD gap:

```text
arbitrary smooth low-frequency modes
  are legal functional-analytic inputs

PDSD
  must use arithmetic information which excludes their dominance
```

Paper 20 has already certified that a sufficiently strong prime-side theorem would exclude the corresponding zeta pole.

---

# 14. Strength calibration against conjectural prime noise

The Montgomery–Soundararajan variance prediction gives the prime-noise scale

$$
\mathcal S_{\rm noise}(H)
\asymp
XH\log(X/H).
$$

A fixed zero with real part $\beta$ contributes the lag-energy scale

$$
\mathcal S_\rho(H)
\asymp
H^2X^{2\beta-1}
$$

at exponent level.

For

$$
H=X^\alpha,
$$

the zero mode dominates the conjectural noise when

$$
\alpha+2\beta-2>0,
$$

that is,

$$
\boxed{
\beta
>
1-\frac{\alpha}{2}.
}
$$

This reproduces the fixed-strip scale naturally associated with short-interval mean square.

This subsection is plausibility/strength calibration only.

It is not used as a proof.

---

# 15. Average Hardy–Littlewood covariance audit

The adjacent covariance has the exact prime-correlation expansion

$$
\mathcal C_X(H)
=
\sum_{1\le h<2H}
K_H(h)
\sum_n
a_na_{n+h}
+
\text{boundary terms},
$$

where $K_H$ is a triangular kernel centered at $h=H$.

Current averaged Hardy–Littlewood theorems give wide shift coverage with arbitrary logarithmic accuracy.

After the triangular weight is inserted, their direct error scale remains too large to compare $\mathcal C_X(H)$ to $\mathcal S_X(H)$ by a fixed relative constant in polynomial ranges.

In addition, unconditional asymptotics for the prime short-interval variance itself remain largely unknown.

Therefore Track D1 does not currently prove PDSD.

---

# 16. Spectral octave audit

Paper 21 gives

$$
\mathcal D_X(H)
=
4
\int_0^1
|S_X(\xi)|^2
|D_H(\xi)|^2
\sin^2(\pi H\xi)
d\xi.
$$

Thus a PDSD good scale is a lower bound on a positive octave-defect energy relative to the low-pass energy.

This is the cleanest spectral formulation of the local problem.

But current principal-arc estimates give only subpower global escape.

No fixed relative octave lower bound is known on a positive density of polynomial dyadic scales.

Track D2 therefore remains open.

---

# 17. Variance-lower-bound audit

To prove

$$
\mathcal D_X(H)
\ge
c\mathcal S_X(H),
$$

one needs simultaneous information on:

```text
the signed two-block defect;
the one-block variance scale.
```

Existing lower-bound methods and conditional variance results do not currently provide the required unconditional fixed relative comparison throughout a positive density of polynomial scales.

Recent literature continues to emphasize that very little is known unconditionally about asymptotics for the variance of primes in short intervals.

Track D3 therefore does not close PDSD.

---

# 18. Long critical locking audit

Assume

$$
q_X(H_j)
=
1-o(1)
$$

for many consecutive dyadic scales.

Then

$$
U_{H_j}(x+H_j)
\approx
U_{H_j}(x)
$$

in $L^2$.

This says the cumulative prime error behaves approximately like a low-curvature drift on those scales.

Proposition 12.1 shows that smooth power modes realize exactly this behavior.

Therefore a contradiction cannot come from multiscale geometry alone.

It must use arithmetic information showing that the centered von Mangoldt sequence has enough irreducible octave energy.

Track D5 is therefore reduced to a new arithmetic spectral lower-bound problem.

---

# 19. Correction to the MLEPG lag range

Paper 17 and Paper 21 imposed the convenient restriction

$$
\alpha<\frac23.
$$

The residue-chain exponent ledger actually gives the three global terms

$$
N^{3-\alpha+o(1)},
\qquad
N^{3-\delta+o(1)},
\qquad
N^{1+2\alpha+o(1)}.
$$

A positive global exponent gain exists provided

$$
\boxed{
0<\alpha<1,
}
$$

because the third term allows

$$
\kappa<2-2\alpha.
$$

Therefore the correct admissible range for the abstract deterministic bridge is:

$$
\boxed{
0<\alpha<1.
}
$$

Create:

```text
COR-RH-001
MLEPG_ALPHA_RANGE_CORRECTION

old:
  alpha < 2/3

correct:
  alpha < 1

global exponent cap:
  kappa < min(alpha, delta, 2-2alpha)
```

The earlier restriction was sufficient but unnecessarily strong.

---

# 20. Campaign 21 verdict

```text
D1 average Hardy-Littlewood covariance
  current precision insufficient

D2 spectral octave escape
  exact formulation / fixed relative lower bound open

D3 variance lower bound
  insufficient for fixed relative gap

D4 positive-density scales
  not implied by current endpoint subpower theorem

D5 long critical locking contradiction
  fails deterministically because smooth drift is a locking countermodel

PDSD
  OPEN

linear cumulative contraction mass
  exact minimal scale criterion

current contraction mass
  provably sublinear
```

No fixed power is proved.

---

# 21. New obstruction: smooth-drift locking

Create:

```text
O-RH-048
SMOOTH_LOW_FREQUENCY_CRITICAL_LOCKING
status:
  CERTIFIED AS COUNTERMODEL TO PURELY DETERMINISTIC GAP PROOFS
```

Statement:

> Smooth power-law cumulative-error modes have adjacent-block defect only of order $(H/X)^2$ relative to their lag energy for $H=o(X)$. A fixed dyadic decorrelation gap therefore cannot follow from finite support, centering, or multiscale geometry alone.

---

# 22. PDSD status

PDSD remains a legitimate fixed-power generator because:

```text
its hypothesis contains no X-power;
its fixed power is generated by iteration;
its bridge to MLEPG and Mellin pole recovery is certified.
```

But Campaign 21 finds no current unconditional theorem proving it.

It remains:

```text
F-RH-017
PDSD
OPEN
```

---

# 23. Campaign 22

The next campaign is:

```text
CSM_RH Campaign 22
ARITHMETIC_OCTAVE_DEFECT_ATTACK
```

It does not create another target.

It attacks the exact positive defect

$$
\boxed{
\mathcal D_X(H)
=
\sum_x
|U_H(x)-U_H(x+H)|^2.
}
$$

The objective is to find arithmetic information which forces enough defect mass across logarithmically many scales.

---

# 24. Campaign 22 tracks

## O1 — centered-prime diagonal injection

Separate the prime diagonal contribution to the two-block defect and determine exactly what signed off-diagonal theorem is required to cancel it.

## O2 — sieve lower bound for octave defect

Adapt lower-bound divisor-sum methods directly to $\mathcal D_X(H)$ rather than to the ordinary short-interval variance.

## O3 — all-scale Hardy–Littlewood assembly

Sum the defect over many dyadic scales before applying absolute values to correlation errors.

Test whether the multiscale kernel has cancellations unavailable at one scale.

## O4 — spectral Littlewood–Paley prime energy

Construct a rigorous band-energy lower bound for the centered von Mangoldt exponential sum across dyadic frequency octaves.

The bound must be arithmetic, not a generic uncertainty principle.

## O5 — locking rigidity plus prime jumps

Assume small defect on many scales and combine the resulting low-curvature structure with the exact jump sequence

$$
A(n)-A(n-1)=\Lambda(n)-1.
$$

Test whether the large diagonal energy

$$
\sum_{n\asymp X}
[\Lambda(n)-1]^2
\asymp
X\log X
$$

forces octave escape.

---

# 25. Campaign 22 rejection filters

Reject a candidate if:

## R1. It uses only finite-support Poincare.

## R2. It treats the conjectural prime variance as proved.

## R3. It inserts a fixed zero-free strip.

## R4. It obtains only the already known sublinear contraction mass.

## R5. It proves octave defect only at finitely many scales independent of $X$.

## R6. It replaces a relative defect bound by an absolute bound too small to compare with $\mathcal S_X(H)$.

---

# 26. External calibration

Relevant current context:

1. Guth–Maynard's 2026 large-value theorem gives the zero-density exponent $30/13$ and almost-all short-interval prime asymptotics down to exponent $2/15+\varepsilon$, with subpower exponential accuracy rather than fixed-power accuracy.

2. Montgomery–Soundararajan predict prime short-interval variance of order $H\log(X/H)$ in polynomial ranges, which predicts strong adjacent-block decorrelation.

3. Gorodetsky's 2024 work emphasizes that unconditional asymptotics for the variance of primes in short intervals remain largely unknown.

4. Leung's 2026 theorem obtains weak negative correlations for prime counts in multiple short intervals under RH and linear-independence hypotheses, providing conditional plausibility for adjacent-block decorrelation.

None proves the arithmetic octave defect required here.

---

# 27. State transition

```text
CSM_RH v1.12
  ->
CSM_RH v1.13
```

with:

```text
Campaign 21
  CLOSED_AS_CONTRACTION_MASS_AND_LOCKING_AUDIT

F-RH-017
  PDSD
  REMAINS OPEN

O-RH-047
  FINITE_SUPPORT_POINCARE_GAP_INSUFFICIENCY
  CREATED / CERTIFIED

O-RH-048
  SMOOTH_LOW_FREQUENCY_CRITICAL_LOCKING
  CREATED / CERTIFIED AS DETERMINISTIC COUNTERMODEL

COR-RH-001
  MLEPG_ALPHA_RANGE_CORRECTION
  CREATED / CERTIFIED

Campaign 22
  ARITHMETIC_OCTAVE_DEFECT_ATTACK
  READY
```

---

# 28. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

PDSD = OPEN

EXACT DYADIC CONTRACTION MASS = CERTIFIED

CURRENT CONTRACTION MASS = SUBLINEAR IN log X

PURE DETERMINISTIC FIXED GAP = IMPOSSIBLE AS A GENERAL PRINCIPLE

ARITHMETIC OCTAVE DEFECT = NEXT OPEN MECHANISM

CORRECT MLEPG RANGE = 0 < alpha < 1

NEXT CAMPAIGN = 22
```

The exact remaining scale-dynamical gap is:

$$
\boxed{
G_X(J)
=
\sum_{j<J}
-\log
\left(
1-
\frac{
\mathcal D_X(H_j)
}{
4\mathcal S_X(H_j)
}
\right)
}
$$

and fixed power requires

$$
\boxed{
G_X(J)
\gg
\log X.
}
$$

Current unconditional technology supplies genuine but sublinear escape. The missing input must force arithmetic octave energy, not merely finite-support curvature.
