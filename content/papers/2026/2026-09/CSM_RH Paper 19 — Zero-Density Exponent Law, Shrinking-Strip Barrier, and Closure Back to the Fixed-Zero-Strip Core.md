# CSM_RH Paper 19
## Zero-Density Exponent Law, Shrinking-Strip Barrier, and Closure Back to the Fixed-Zero-Strip Core

**Project:** `CSM_RH`  
**Paper:** `19`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.9 / Paper 18`  
**Campaign:** `18 — PRINCIPAL_FEJER_ARC_POWER_ATTACK`  
**Status:** current large-value / zero-density closure audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

Canonical root state:

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Campaign 18 asks whether current large-value, zero-density, exceptional-set, and explicit-formula techniques can upgrade the principal Fejer arc from subpower precision to a fixed power.

The answer for the currently audited absolute zero-density schema is negative.

The main result is an exponent law which separates:

```text
range threshold
from
precision threshold
```

and shows why improving zero density alone does not create a fixed power while the zero-free gap still shrinks with height.

No live GLM-5.3-Flash run is claimed.

---

# 1. Direct theorem candidate

Paper 17 introduced MLEPG.

Let

$$
A(x)=\psi(x)-x.
$$

Let

$$
H=X^\alpha,
\qquad
0<\alpha<1.
$$

Define

$$
\mathcal S_\Lambda(X,H)
=
\sum_x
|A(x+H)-A(x)|^2
$$

with an appropriate finite or smoothed range around $X$.

MLEPG asks for

$$
\boxed{
\mathcal S_\Lambda(X,H)
\ll
XH(\log X)^{O(1)}
+
XH^2X^{-\delta+o(1)}
}
$$

for one fixed

$$
\delta>0.
$$

Paper 18 proved that the principal Fejer arc is a necessary subproblem.

---

# 2. Guth–Maynard already prove the subpower $L^2$ analogue

In the proof of their almost-all short-interval prime theorem, Guth and Maynard use the explicit formula and reduce the problem to an $L^2$ estimate for a zero packet.

Their equation (13.4) has the form

$$
\boxed{
\int_X^{3X}
\left|
\sum_{|\rho|<T}
x^\rho
\frac{
(1+\Delta)^\rho-1
}{
\rho
}
\right|^2
dx
\ll
\Delta^2X^3
\exp
\left(
-c(\log X)^{1/4}
\right),
}
$$

at the scale used in their proof.

Since

$$
H\asymp \Delta X,
$$

the natural normalization is

$$
\Delta^2X^3
=
XH^2.
$$

Thus the current large-value method already proves the structural analogue

$$
\boxed{
XH^2
\times
X^{-o(1)}.
}
$$

The missing MLEPG input is exactly the replacement

$$
X^{-o(1)}
\longrightarrow
X^{-\delta}.
$$

---

# 3. Abstract zero-density input

Assume an upper bound

$$
\boxed{
N(\sigma,T)
\ll
T^{A_0(1-\sigma)+o(1)}
}
$$

uniformly at the exponent level, where

$$
A_0>0
$$

is fixed.

For Guth–Maynard,

$$
\boxed{
A_0=\frac{30}{13}.
}
$$

Take

$$
H=X^\alpha
$$

and the explicit-formula truncation height

$$
\boxed{
T=X^{1-\alpha+o(1)}.
}
$$

This is the natural short-interval scale

$$
T\asymp X/H
$$

up to subpower factors.

---

# 4. Zero-density exponent law

A zero with real part $\sigma$ contributes at squared $L^2$ exponent scale

$$
H^2X^{2\sigma-1}
$$

relative to an $X$ -length integration range.

Equivalently, relative to the baseline

$$
XH^2,
$$

the single-zero exponent factor is

$$
X^{-2(1-\sigma)}.
$$

The density bound permits approximately

$$
T^{A_0(1-\sigma)+o(1)}
=
X^{A_0(1-\alpha)(1-\sigma)+o(1)}
$$

zeros at that real-part scale.

Therefore the absolute zero-density contribution has exponent ratio

$$
\boxed{
X^{-c_{A_0}(\alpha)(1-\sigma)+o(1)},
}
$$

where

$$
\boxed{
c_{A_0}(\alpha)
=
2
-
A_0(1-\alpha).
}
$$

This is the canonical density-to- $L^2$ exponent law for the present audit.

---

# 5. Range threshold

The density schema yields decay in the real-part variable only if

$$
c_{A_0}(\alpha)>0.
$$

Thus:

## Theorem 5.1 — Zero-Density Range Threshold

$$
\boxed{
\alpha
>
1-\frac2{A_0}.
}
$$

For

$$
A_0=\frac{30}{13},
$$

we obtain

$$
\begin{aligned}
1-\frac2{A_0}
&=
1-\frac{26}{30}
\\
&=
\boxed{
\frac2{15}.
}
\end{aligned}
$$

This recovers the Guth–Maynard almost-all short-interval threshold at exponent level.

The threshold is therefore a density-balance phenomenon.

---

# 6. Shrinking zero-free boundary

Let the available zero-free region have the form

$$
\boxed{
\Re\rho
\le
1-\eta(T),
}
$$

where

$$
\eta(T)>0
$$

and

$$
\eta(T)\to0
$$

as

$$
T\to\infty.
$$

The Vinogradov–Korobov region is of this type.

The worst permitted real part in the density exponent law is then

$$
\sigma
=
1-\eta(T).
$$

Substituting into Section 4 gives the best exponent ratio available from the absolute density schema:

$$
\boxed{
X^{-c_{A_0}(\alpha)\eta(T)+o(1)}.
}
$$

Because

$$
\eta(T)\to0,
$$

this is

$$
\boxed{
X^{-o(1)}.
}
$$

It is not a fixed power.

---

# 7. Shrinking-Strip Barrier Theorem

## Theorem 7.1

Fix

$$
A_0<\infty
$$

and

$$
\alpha
>
1-\frac2{A_0}.
$$

Consider an explicit-formula $L^2$ proof schema which:

1. bounds zero contributions by absolute values or positive moments at each real-part scale;
2. uses only the density estimate
   $$
   N(\sigma,T)
   \ll
   T^{A_0(1-\sigma)+o(1)};
   $$
3. uses a zero-free boundary
   $$
   \Re\rho
   \le
   1-\eta(T)
   $$
   with
   $$
   \eta(T)\to0.
   $$

Then the zero-density exponent law supplies at best a subpower factor

$$
\boxed{
X^{-o(1)}
}
$$

over the baseline $XH^2$.

It cannot by itself produce

$$
X^{-\delta}
$$

for fixed

$$
\delta>0.
$$

This theorem is about the specified proof schema.

It is not a universal impossibility theorem for all uses of zeros.

---

# 8. Improving zero density alone does not solve the precision problem

Suppose the density hypothesis were available in the ideal form

$$
A_0=2.
$$

Then the range threshold becomes

$$
\alpha>0.
$$

Thus almost-all short-interval coverage could, at the density-balance level, extend to every fixed positive power scale.

But the precision factor would still be

$$
X^{-2\alpha\eta(T)+o(1)}
=
X^{-o(1)}
$$

whenever

$$
\eta(T)\to0.
$$

Therefore:

## Corollary 8.1

Even an optimal density exponent does not, by itself, give MLEPG fixed-power precision unless one also obtains:

```text
a fixed zero-free gap,
or
new cancellation / coefficient isolation beyond the absolute density schema.
```

This cleanly separates the density problem from the fixed-strip problem.

---

# 9. Guth–Maynard proof location

Guth and Maynard prove

$$
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}
$$

and use the Vinogradov–Korobov zero-free region in their prime-distribution corollaries.

In their almost-all short-interval proof they choose a truncation scale corresponding to the interval length and reduce the problem to the zero-packet $L^2$ estimate described in Section 2.

The final saving is subpower.

The exponent law in this paper explains structurally why the new density exponent changes the admissible short-interval range to $2/15$ but does not generate a fixed $X$ -power.

---

# 10. Gafni–Tao exceptional-set framework

Gafni and Tao define, for fixed relative-error tolerance

$$
\delta>0,
$$

an exceptional set of intervals where the short-interval PNT fails at that tolerance.

They then define exceptional-set exponents and derive explicit bounds from zero-density information.

This is strong quantitative information about the number of bad intervals.

However the parameter $\delta$ in the theorem framework is fixed while $X$ tends to infinity.

By diagonalizing over fixed values

$$
\delta=1,\frac12,\frac13,\ldots,
$$

one obtains an $o(H)$ error outside a density-zero set.

One does not obtain a polynomially shrinking threshold

$$
HX^{-\eta}.
$$

---

# 11. Fixed-threshold versus shrinking-threshold mismatch

Suppose for each fixed

$$
\varepsilon>0
$$

one proves

$$
|\Delta_HA(x)|
\le
\varepsilon H
$$

outside an exceptional set of power-saving size.

Then the good-set contribution to the lag energy is still

$$
\boxed{
\varepsilon^2XH^2.
}
$$

For fixed $\varepsilon$, this has no fixed $X$ -power saving.

Taking $\varepsilon$ arbitrarily small after the theorem is proved does not create a bound

$$
X^{-\delta}.
$$

To obtain MLEPG through a good/bad decomposition, one needs a threshold which shrinks quantitatively with $X$, for example

$$
\boxed{
|\Delta_HA(x)|
\le
HX^{-\eta_1}
}
$$

on the good set.

Create:

```text
O-RH-043
FIXED_THRESHOLD_EXCEPTIONAL_SET_MISMATCH
status:
  CERTIFIED
```

---

# 12. Guth–Maynard and Gafni–Tao combined

The two technologies address different axes.

## Guth–Maynard

Improves:

```text
zero-density exponent;
large-value estimates;
range of short intervals;
subpower quantitative error.
```

## Gafni–Tao

Improves:

```text
quantification of exceptional-set size;
translation from zero-density / zero additive energy to bad-interval counts.
```

Neither currently supplies:

$$
\boxed{
\text{fixed-power shrinking error threshold in }L^2.
}
$$

Thus their combination does not currently prove MLEPG.

---

# 13. Density blindness to a fixed off-axis zero

For every fixed

$$
\beta<1,
$$

a density bound of the form

$$
N(\sigma,T)
\ll
T^{A_0(1-\sigma)+o(1)}
$$

permits finitely many zeros with real part $\beta$.

A single such zero is negligible for the asymptotic count $N(\sigma,T)$.

Therefore density information alone cannot exclude a fixed off-axis zero.

But a fixed zero with real part

$$
\beta
$$

has short-interval explicit-formula amplitude at the natural scale

$$
H X^{\beta-1}
$$

and squared integrated scale

$$
H^2X^{2\beta-1}.
$$

Thus fixed-power principal-arc / lag-energy control must ultimately be sensitive to individual persistent off-axis zero modes.

Create:

```text
O-RH-044
ZERO_DENSITY_SINGLE_ZERO_BLINDNESS
status:
  CERTIFIED AS STRENGTH AUDIT
```

This is not a claim that one zero automatically gives a rigorous lower bound without a coefficient-recovery argument.

It records the information deficit of density estimates.

---

# 14. Closure back to the fixed-zero-strip core

Paper 17 gives the deterministic chain

$$
\operatorname{MLEPG}(\alpha,\delta)
\Longrightarrow
\sum_{n\le2N}
|\psi(n)-n|^2
\ll
N^{3-\kappa+o(1)}
$$

for some

$$
\kappa>0.
$$

At exponent level, a fixed zero

$$
\rho
=
\beta+i\gamma
$$

contributes the scale

$$
N^{2\beta+1}
$$

to the PNT mean-square explicit formula.

Thus the bound

$$
N^{3-\kappa+o(1)}
$$

has the fixed-strip strength

$$
\boxed{
\beta
\le
1-\frac{\kappa}{2}.
}
$$

This is the same exponent law already encountered in the earlier ZPPF / principal zeta-packet campaigns.

Therefore the direct PESC branch has closed a loop:

```text
PESC
  ->
MLEPG candidate
  ->
principal Fejer arc
  ->
explicit formula / zero density
  ->
fixed-zero-strip strength
```

The loop is not circular as a proof.

It is a closure-space strength identification.

---

# 15. New obstruction: density / strip decoupling

Create:

```text
O-RH-042
ZERO_DENSITY_SHRINKING_STRIP_EXPONENT_BARRIER
status:
  CERTIFIED FOR ABSOLUTE EXPLICIT-FORMULA SCHEMA
```

Statement:

> A finite zero-density exponent determines the short-interval range threshold through $2-A_0(1-\alpha)$, but a shrinking zero-free boundary forces the resulting power gain to shrink to zero. Density improvement alone therefore cannot supply MLEPG fixed-power precision within the audited absolute explicit-formula schema.

---

# 16. Status of Campaign 18 tracks

## P1 — Guth–Maynard large-value upgrade

```text
status:
  CURRENT METHOD ALREADY PRODUCES L2 SUBPOWER

fixed power:
  NO

barrier:
  shrinking zero-free boundary in absolute density summation
```

## P2 — Gafni–Tao exceptional-set optimization

```text
status:
  STRONG EXCEPTIONAL-SET COUNTING

shrinking polynomial good-error threshold:
  NOT PROVIDED BY CURRENT FRAMEWORK

fixed-power L2:
  NO
```

## P3 — principal Dirichlet-polynomial mean square

```text
status:
  CURRENT LARGE-VALUE INPUT IMPROVES DENSITY/RANGE

single-zero-sensitive fixed power:
  NOT IDENTIFIED
```

## P4 — smooth explicit-formula zero packet

```text
status:
  STRENGTH AUDIT CONFIRMS FIXED-STRIP SCALE

new coefficient-isolation theorem:
  NOT PROVED
```

---

# 17. What a genuinely new input must do

Any successful next mechanism must be sensitive to a single persistent near- $1$ zero.

Density-only information is insufficient.

The new input must do at least one of:

## S1 — fixed zero-free gap

Directly prove

$$
\Re\rho
\le
1-\eta_0
$$

for some fixed

$$
\eta_0>0.
$$

## S2 — coefficient recovery / isolation

Show that a persistent off-axis zero contributes a noncancellable amount to the principal Fejer / lag-energy observable.

Then MLEPG would exclude it.

## S3 — phase-sensitive zero-packet coercivity

Use the structure of the zero packet beyond absolute counting to obtain a fixed-power lower/upper incompatibility.

## S4 — new prime-side theorem independent of zero density

Prove MLEPG directly by arithmetic methods whose fixed power is not obtained by summing a density estimate.

---

# 18. New survivor

Create:

```text
S-RH-027
SINGLE_ZERO_SENSITIVE_PRINCIPAL_ARC_MECHANISM
status:
  OPEN
```

Definition:

> a theorem mechanism which can detect or exclude the contribution of one persistent off-axis zero in the principal Fejer / short-interval $L^2$ observable, rather than merely bound how many such zeros may exist.

This is a mechanism requirement.

It is not a new target.

---

# 19. Campaign 18 verdict

```text
GUTH-MAYNARD ZERO DENSITY
  RANGE BREAKTHROUGH

GUTH-MAYNARD PRINCIPAL L2
  SUBPOWER

GAFNI-TAO EXCEPTIONAL SET
  POWER-SIZED BAD-SET INFORMATION POSSIBLE

GAFNI-TAO GOOD ERROR THRESHOLD
  FIXED / o(1), NOT POLYNOMIALLY SHRINKING

ABSOLUTE ZERO-DENSITY SCHEMA
  CANNOT CREATE FIXED POWER WITH SHRINKING ZERO-FREE GAP

DENSITY HYPOTHESIS ALONE
  STILL NOT ENOUGH FOR FIXED POWER

MLEPG
  OPEN

PESC
  OPEN
```

No fixed-power theorem is proved.

---

# 20. Campaign 19

The next campaign is:

```text
CSM_RH Campaign 19
SINGLE_ZERO_SENSITIVE_THEOREM_GENERATION
```

The root target remains PESC.

The working theorem candidate remains MLEPG.

The new design constraint is:

```text
every candidate mechanism must be capable of distinguishing
"no near-1 zero"
from
"one persistent near-1 zero".
```

Density-only candidates are rejected automatically.

---

# 21. Campaign 19 tracks

## Z1 — multiscale coefficient recovery

Use principal Fejer energies over a family of scales $H$ to recover a fixed zero mode.

A valid proof must quantify the inverse map and control all other zeros.

## Z2 — smooth Mellin packet coercivity

Replace the hard interval kernel by a smooth positive packet and test whether Mellin coefficients of individual zeros can be isolated with a fixed exponent.

## Z3 — zero-pair Gram positivity with gauge control

Build a canonical zero-mode Gram form whose diagonal from one off-axis orbit cannot be removed by representation changes or uncontrolled cross terms.

Paper 07's Gram-gauge obstruction must be respected.

## Z4 — prime-side multiscale contraction

Avoid zeros entirely and prove a fixed-power recurrence for lag energies across scales.

The recurrence must have linear cumulative contraction mass.

---

# 22. Campaign 19 rejection filters

Reject a candidate if:

## R1. It uses only a zero-density count.

## R2. It uses a shrinking zero-free region and calls the resulting subpower a fixed power.

## R3. It controls exceptional-set size without a polynomially shrinking good-error threshold.

## R4. It assumes a fixed zero-free strip.

## R5. It ignores cancellation among zero modes in a coefficient-recovery claim.

## R6. It creates a gauge-dependent Gram gap.

## R7. It merely restates PESC / MLEPG.

---

# 23. External calibration

The present audit uses the following current results.

1. Guth–Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026), prove
$$
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}
$$
and obtain almost-all prime asymptotics for short intervals beginning at exponent $2/15+\varepsilon$. Their proof reduces the almost-all result to an explicit-formula $L^2$ zero-packet estimate and obtains subpower exponential decay.

2. Gafni–Tao, *On the number of exceptional intervals to the prime number theorem in short intervals*, Essential Number Theory 5 (2026), develop explicit bounds on exceptional-set exponents from zero-density and zero-additive-energy estimates. Their exceptional-set definitions use fixed relative-error tolerances.

3. Matomäki–Radziwiłł–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae 244 (2026), record the current almost-all short-interval PNT range and arbitrary logarithmic quantitative accuracy.

None supplies a fixed $X$ -power principal-arc estimate.

---

# 24. State transition

The canonical transition is:

```text
CSM_RH v1.9
  ->
CSM_RH v1.10
```

with:

```text
Campaign 18
  CLOSED_AS_ZERO_DENSITY_AND_EXCEPTIONAL_SET_PRECISION_AUDIT

O-RH-042
  ZERO_DENSITY_SHRINKING_STRIP_EXPONENT_BARRIER
  CREATED / CERTIFIED FOR ABSOLUTE EXPLICIT-FORMULA SCHEMA

O-RH-043
  FIXED_THRESHOLD_EXCEPTIONAL_SET_MISMATCH
  CREATED / CERTIFIED

O-RH-044
  ZERO_DENSITY_SINGLE_ZERO_BLINDNESS
  CREATED / CERTIFIED AS STRENGTH AUDIT

S-RH-027
  SINGLE_ZERO_SENSITIVE_PRINCIPAL_ARC_MECHANISM
  CREATED / OPEN

F-RH-016
  MLEPG
  REMAINS OPEN

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 19
  SINGLE_ZERO_SENSITIVE_THEOREM_GENERATION
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

CURRENT ZERO-DENSITY RANGE = STRONG

CURRENT ZERO-DENSITY PRECISION = SUBPOWER

2/15 = RANGE THRESHOLD, NOT FIXED-POWER THRESHOLD

GAFNI-TAO = EXCEPTIONAL-SET TOOL, NOT SHRINKING-THRESHOLD POWER L2

DENSITY-ONLY SCHEMA = SINGLE-ZERO BLIND

NEXT REQUIREMENT = SINGLE-ZERO-SENSITIVE MECHANISM

NEXT CAMPAIGN = 19
```

The key exponent identity is

$$
\boxed{
c_{A_0}(\alpha)
=
2
-
A_0(1-\alpha).
}
$$

It controls whether zero-density information can gain anything at a short-interval scale.

But the actual fixed-power exponent available from a shrinking zero-free boundary is only

$$
\boxed{
c_{A_0}(\alpha)\eta(T),
}
$$

which tends to zero.

The next theorem-generation round must therefore add information which is qualitatively stronger than density.
