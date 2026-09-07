# CSM_RH Paper 38
## Polynomial Shrinking Thresholds, Explicit-Formula Height Tax, and the Right-Edge Subpower Barrier

**Project:** `CSM_RH`  
**Paper:** `38`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.28 / Paper 37`  
**Campaign:** `37 — SHRINKING_THRESHOLD_TAIL_ATTACK`  
**Status:** explicit dependence audit of the Gafni–Tao exceptional-set architecture; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Paper 37 certified that a polynomial shrinking-threshold exceptional-set theorem would imply MLEPG and hence a fixed zero-free strip.

Campaign 37 asks whether the current Gafni–Tao exceptional-set proof can already be pushed to such a threshold by exposing all parameter dependence.

The answer is negative for the audited architecture.

There are three independent reasons:

1. the theorem is proved with $\delta$ and $J$ fixed before $X\to\infty$ ;
2. a polynomial threshold forces the explicit-formula height to increase by a fixed power of $X$ ;
3. the right-edge zero packet is controlled only at stretched-log / subpower strength.

The third obstruction is decisive.

No new fixed-power theorem is admitted.

---

# 1. Shrinking-threshold admission target

Let

$$
H=X^\theta
$$

with fixed

$$
0<\theta<1.
$$

Define

$$
U_H(x)
=
\psi(x+H)-\psi(x)-H.
$$

The Paper-37 admission target is:

$$
\boxed{
\left|
\left\{
x\in[X,2X]:
|U_H(x)|>HX^{-\eta}
\right\}
\right|
\ll
X^{1-c}
}
$$

for some fixed

$$
\eta>0,
\qquad
c>0.
$$

By Paper 37 this implies

$$
\mathcal S_\Lambda(X,H)
\ll
XH^2X^{-\min(2\eta,c)+o(1)},
$$

and therefore MLEPG.

---

# 2. Fixed-parameter structure of Gafni–Tao

The Gafni–Tao proof begins by fixing

$$
0<\delta<1.
$$

It then chooses a natural number $J$ sufficiently large depending on

$$
\delta,\theta,\varepsilon,
$$

and proves its exceptional-set estimate as

$$
X\to\infty
$$

with

$$
J,\delta,\theta,\varepsilon
$$

held fixed.

Therefore the published theorem does not by itself authorize the substitution

$$
\boxed{
\delta=X^{-\eta}.
}
$$

Create:

```text
O-RH-088
GAFNI_TAO_FIXED_PARAMETER_NONUNIFORMITY
status:
  CERTIFIED AS THEOREM-SCOPE AUDIT
```

This is a theorem-scope statement, not a claim that the proof cannot be uniformized by new work.

---

# 3. Spatial localization cost

To replace the varying interval length $x^\theta$ by the multiplicatively normalized length $x/\tau$, the proof localizes $x$ to intervals of the form

$$
[X,(1+\delta/J)X],
$$

where

$$
\tau=X^{1-\theta}.
$$

Covering $[X,2X]$ requires

$$
\boxed{
O(J/\delta)
}
$$

such intervals.

For fixed $\delta,J$ this is a harmless constant.

If

$$
\delta=X^{-\eta}
$$

and $J$ grows polynomially, this becomes an exponent-level cost.

---

# 4. Explicit-formula height tax

The truncated explicit formula used in the proof has error

$$
\boxed{
O
\left(
\frac{
X(\log X)^2
}{
T
}
\right).
}
$$

To resolve the shrinking threshold

$$
\delta X^\theta,
$$

it is necessary that

$$
\frac{
X(\log X)^2
}{
T
}
\ll
\delta X^\theta.
$$

Therefore:

## Theorem 4.1 — Polynomial Threshold Truncation Law

$$
\boxed{
T
\gtrsim
\delta^{-1}
X^{1-\theta}
(\log X)^2.
}
$$

In particular, if

$$
\delta=X^{-\eta},
$$

then

$$
\boxed{
T
\ge
X^{1-\theta+\eta+o(1)}.
}
$$

Create:

```text
B-RH-013
SHRINKING_THRESHOLD_EXPLICIT_FORMULA_HEIGHT_LAW
status:
  CERTIFIED
```

The original proof chooses

$$
T
=
J(\log X)^2X^{1-\theta}.
$$

Thus, within that parameterization, polynomial shrinking forces at least

$$
\boxed{
J\gtrsim X^\eta.
}
$$

---

# 5. Zero-density exponent tax

Suppose generously that one has the uniform zero-density bound

$$
N(\sigma,T)
\le
T^{A_0(1-\sigma)+o(1)}
$$

with

$$
A_0=\frac{30}{13}.
$$

Under the polynomial truncation height

$$
T=X^{1-\theta+\eta+o(1)},
$$

the density contribution becomes

$$
\boxed{
X^{
A_0(1-\theta+\eta)(1-\sigma)
+o(1)
}.
}
$$

Thus the zero-density part itself pays a fixed exponent tax

$$
\boxed{
A_0\eta(1-\sigma).
}
$$

This is not yet the decisive obstruction, because for $\sigma$ bounded away from $1$ and $\theta$ above the almost-all threshold by a fixed margin, sufficiently small $\eta$ can still leave exponent room.

The fatal region is $\sigma\to1$.

---

# 6. Right-edge lemma

Gafni–Tao isolate a fixed strip

$$
I\subset[1-\eta_0,1].
$$

Using the Vinogradov–Korobov zero-free region and a near-one zero-density estimate, they prove

$$
\boxed{
\sup_{X\le x\le2X}
|S_I(x)|
\ll_\theta
\exp
\left[
-c_\theta
\frac{
(\log X)^{1/3}
}{
(\log\log X)^{1/3}
}
\right]
\frac{X}{\tau}.
}
$$

Since

$$
\frac{X}{\tau}=X^\theta,
$$

the available relative suppression is

$$
\boxed{
\Delta_{\mathrm{edge}}(X)
=
\exp
\left[
-c_\theta
\frac{
(\log X)^{1/3}
}{
(\log\log X)^{1/3}
}
\right].
}
$$

This is

$$
X^{-o(1)}.
$$

---

# 7. Polynomial threshold comparison

For any fixed

$$
\eta>0,
$$

the desired relative threshold is

$$
\delta_X=X^{-\eta}.
$$

But

$$
\boxed{
\Delta_{\mathrm{edge}}(X)
\gg
X^{-\eta}
}
$$

as $X\to\infty$.

Indeed,

$$
\eta\log X
\gg
\frac{
(\log X)^{1/3}
}{
(\log\log X)^{1/3}
}.
$$

Therefore the right-edge estimate is asymptotically much larger than the desired polynomial threshold.

Create:

```text
O-RH-089
GAFNI_TAO_RIGHT_EDGE_SUBPOWER_FLOOR
status:
  CERTIFIED AS CURRENT-PROOF BARRIER
```

The existing Lemma 2.1 cannot dispose of the right-edge zero packet at threshold $X^{-\eta}$.

---

# 8. This failure occurs before Markov

The right-edge treatment is an $L^\infty$ disposal step.

It occurs before the proof invokes the $L^2$ and $L^4$ Markov bounds for the remaining zero strips.

Therefore improving bookkeeping in the later Markov step does not repair this failure.

The proof already lacks sufficient amplitude suppression on the near-one zero packet.

---

# 9. Why the second moment cannot repair the edge

Away from the right edge, the second-moment exponent has the form

$$
(1-\theta)
(1-\sigma)
A(\sigma)
+
2\theta
+
2\sigma
-
2.
$$

After the shrinking-threshold height tax, the natural generous replacement is

$$
\boxed{
(1-\theta+\eta)
(1-\sigma)
A(\sigma)
+
2\theta
+
2\sigma
-
2.
}
$$

Markov at threshold $X^{\theta-\eta}$ introduces an additional cost

$$
X^{2\eta}.
$$

Even ignoring localization and binning costs, the exceptional-set exponent tends to

$$
\boxed{
1+2\eta
}
$$

as

$$
\sigma\to1.
$$

The zero-density term is nonnegative and vanishes with $1-\sigma$.

Hence no uniform power saving can emerge from the second moment arbitrarily close to $\sigma=1$.

---

# 10. Fourth and higher moments have the same edge geometry

The fourth-moment exponent has the form

$$
(1-\theta)
(1-\sigma)
A^\ast(\sigma)
+
4\theta
+
4\sigma
-
4.
$$

At polynomial threshold $X^{\theta-\eta}$, Markov contributes $X^{4\eta}$.

As

$$
\sigma\to1,
$$

the resulting exceptional-set exponent tends to

$$
\boxed{
1+4\eta.
}
$$

The same phenomenon persists for a hypothetical $2k$ -th moment of the standard zero packet.

The baseline exponent is

$$
2k\sigma-2k
=
-2k(1-\sigma),
$$

while the shrinking threshold costs

$$
X^{2k\eta}.
$$

If

$$
1-\sigma<\eta,
$$

then even the best possible contribution obtained by discarding the nonnegative zero-density term cannot compensate the threshold cost.

Create:

```text
O-RH-090
MOMENT_ORDER_CANNOT_CURE_POLYNOMIAL_THRESHOLD_AT_SHRINKING_EDGE
status:
  CERTIFIED AS STANDARD_MARKOV-PACKET STRENGTH AUDIT
```

This concerns the standard moment-plus-Markov zero-packet architecture.

It is not a universal impossibility theorem for every high-moment method.

---

# 11. The zero-free-region scale

The Vinogradov–Korobov region only removes zeros in a shrinking neighborhood

$$
1-\sigma
\asymp
(\log X)^{-2/3}
(\log\log X)^{-1/3}
$$

at the present height scale, up to constants and the harmless effect of subpower height changes.

This width tends to zero.

For every fixed

$$
\eta>0,
$$

eventually

$$
1-\sigma<\eta
$$

throughout part of the remaining admissible edge layer.

Thus the moment-order audit in Section 10 is consistent with the explicit $L^\infty$ barrier of Section 7.

---

# 12. Maximum natural shrinking class of the current edge input

The right-edge bound is compatible with thresholds no smaller than a stretched-log class such as

$$
\boxed{
\delta_X
\gtrsim
\exp
\left[
-C
\frac{
(\log X)^{1/3}
}{
(\log\log X)^{1/3}
}
\right].
}
$$

For such a subpower threshold,

$$
\delta_X^{-1}=X^{o(1)},
$$

so the necessary truncation height can remain

$$
T=X^{1-\theta+o(1)}.
$$

This explains structurally why the existing architecture naturally lives in a subpower-precision class.

This section is an architecture calibration, not a new uniform theorem, because the published proof keeps $\delta$ fixed.

---

# 13. Interior zero-density region is not the primary failure

To localize the obstruction, suppose hypothetically that all zeros with

$$
\sigma>1-\eta_0
$$

were absent for one fixed

$$
\eta_0>0.
$$

Then the remaining $\sigma$ -range is bounded away from $1$.

With Guth–Maynard

$$
A_0=\frac{30}{13},
$$

and

$$
\theta>\frac{2}{15}
$$

by a fixed margin, sufficiently small shrinking exponent $\eta$ leaves room in the second-moment exponent ledger.

For example, at the most basic $\sigma=1/2$ density point, ignoring localization losses, the condition is

$$
\boxed{
\frac{A_0}{2}
(1-\theta+\eta)
+
2\eta
<
1.
}
$$

This has a positive solution $\eta$ whenever

$$
\theta>\frac{2}{15}.
$$

Thus the critical issue is not merely the $30/13$ density coefficient.

It is the absence of a fixed right-edge gap.

---

# 14. Current-proof J coupling adds further costs

In the published proof the same $J$ controls:

1. spatial localization;
2. zero-strip subdivision;
3. explicit-formula truncation height.

If one formally sets

$$
J=X^j,
\qquad
\delta=X^{-\eta},
$$

then:

## truncation requirement

$$
j\ge\eta;
$$

## number of spatial intervals

$$
J/\delta
=
X^{j+\eta};
$$

## number of zero strips

$$
J
=
X^j;
$$

## pigeonhole threshold per zero strip

$$
\frac{\delta}{J}
=
X^{-(\eta+j)}.
$$

These costs were constants in the fixed-parameter proof.

They become exponent-level losses when $J$ and $\delta^{-1}$ grow polynomially.

Even without the right-edge failure, the proof would require a new uniform re-optimization.

---

# 15. Generous current-architecture L2 ledger

If one keeps the original $J$ coupling and chooses the minimal polynomial scale

$$
j=\eta,
$$

then a generous global $A_0$ second-moment calculation produces the schematic exceptional exponent

$$
\boxed{
\Xi_2(\sigma)
=
2\sigma-1
+
A_0
(1-\theta+\eta)
(1-\sigma)
+
7\eta
}
$$

after accounting for:

1. the threshold $\delta/J$ ;
2. the $J$ zero strips;
3. the $J/\delta$ spatial blocks.

For $\sigma=1/2$,

$$
\boxed{
\Xi_2(1/2)
=
\frac{A_0}{2}
(1-\theta+\eta)
+
7\eta.
}
$$

This can remain below $1$ for very small $\eta$ when $\theta$ is above $2/15$ by a fixed margin.

But

$$
\boxed{
\lim_{\sigma\to1}
\Xi_2(\sigma)
=
1+7\eta>1.
}
$$

Again the right edge is fatal.

The precise coefficient $7$ is architecture-specific and is not claimed to be optimal.

---

# 16. Campaign 37 track audit

## ST1 — fixed-delta dependence

```text
status:
  NONUNIFORM IN PUBLISHED THEOREM

delta, J:
  fixed before X -> infinity
```

## ST2 — explicit-formula truncation

```text
status:
  POLYNOMIAL HEIGHT TAX

delta = X^(-eta)
  forces T >= X^(1-theta+eta+o(1))
```

## ST3 — Guth–Maynard density insertion

```text
status:
  INTERIOR REGION CAN RETAIN EXPONENT ROOM FOR SMALL eta

global A0:
  30/13

decisive failure:
  not interior density
```

## ST4 — right-edge zero packet

```text
status:
  FATAL FOR CURRENT PROOF

available suppression:
  X^(-o(1))

required suppression:
  X^(-eta)
```

## ST5 — higher moments

```text
status:
  STANDARD MARKOV MOMENTS DO NOT CURE SHRINKING EDGE

reason:
  threshold penalty survives as sigma -> 1
```

---

# 17. Campaign 37 verdict

No polynomial shrinking-threshold theorem is obtained.

The Paper-37 admission target remains valid and open.

The current Gafni–Tao architecture is classified as:

```text
fixed threshold:
  valid

power exceptional sets:
  valid

subpower shrinking threshold:
  structurally compatible with edge scale, but not a published uniform theorem

polynomial shrinking threshold:
  not supported

first decisive obstruction:
  right-edge X^(-o(1)) amplitude floor
```

No theorem passes the Campaign-36 breakthrough gate.

---

# 18. New certified package

Create:

```text
B-RH-013
SHRINKING_THRESHOLD_EXPLICIT_FORMULA_HEIGHT_LAW
CERTIFIED

O-RH-088
GAFNI_TAO_FIXED_PARAMETER_NONUNIFORMITY
CERTIFIED AS THEOREM-SCOPE AUDIT

O-RH-089
GAFNI_TAO_RIGHT_EDGE_SUBPOWER_FLOOR
CERTIFIED AS CURRENT-PROOF BARRIER

O-RH-090
MOMENT_ORDER_CANNOT_CURE_POLYNOMIAL_THRESHOLD_AT_SHRINKING_EDGE
CERTIFIED AS STANDARD MARKOV-PACKET STRENGTH AUDIT
```

No new frontier is created.

---

# 19. Canonical root status

```text
F-RH-010
PESC
OPEN / ROOT TARGET

F-RH-016
MLEPG
OPEN / DIRECT THEOREM CANDIDATE

B-RH-012
SHRINKING_THRESHOLD_EXCEPTIONAL_SET_TO_MLEPG
CERTIFIED BRIDGE

polynomial shrinking-threshold theorem:
  OPEN / NOT PROVED
```

---

# 20. Campaign 38

The zero-density exceptional-set route is now localized to the same right-edge subpower barrier already seen in other explicit-formula arguments.

The next campaign therefore switches to a genuinely different arithmetic source:

```text
CSM_RH Campaign 38
GROWING_ACCURACY_LAMBDA_RESIDUAL_ATTACK
```

The target is the 2026 higher-uniformity theorem for

$$
f=\Lambda-\Lambda^\sharp.
$$

The question is:

> can its arbitrary fixed log-power accuracy be uniformized to an accuracy parameter growing with $X$ strongly enough to produce $HX^{-\eta}$?

---

# 21. Campaign 38 tracks

## GA1 — accuracy parameter scaling

The current theorem gives

$$
H\log^{-A}X
$$

for every fixed $A$.

Set formally

$$
A
\asymp
\eta
\frac{\log X}{\log\log X}
$$

and audit every proof constant.

## GA2 — W-parameter transition

The 2026 proof uses a prime major-arc parameter of the form

$$
W_\Lambda=\log^{C A}X.
$$

At growing $A$, compute the exact point at which

$$
W_\Lambda
$$

becomes polynomial in $X$.

## GA3 — Vinogradov–Korobov dependency

Track where the prime Dirichlet-polynomial input uses the shrinking zero-free region.

Determine whether that step alone prevents polynomial $W_\Lambda$.

## GA4 — exceptional-set parameter uniformity

The almost-all theorem also gives a logarithmic exceptional set.

Audit whether making $A$ grow causes the exceptional-set constant or auxiliary complexity to become exponent-level.

## GA5 — direct bridge to Paper 37 target

If a uniform theorem of the form

$$
|U_H(x)|
\ll
HX^{-\eta}
$$

outside

$$
O(X^{1-c})
$$

intervals emerges, immediately invoke B-RH-012.

No new observable is allowed.

---

# 22. Campaign 38 rejection filters

Reject a candidate if:

## R1. $A$ is treated as growing while a theorem assumes it fixed.

## R2. A hidden $O_A(1)$ constant is ignored.

## R3. $W_\Lambda$ becomes polynomial without re-proving the prime Dirichlet-polynomial estimate.

## R4. The proof imports a fixed zero-free strip.

## R5. The final exceptional set remains only logarithmically small.

## R6. The output is $X^{-o(1)}$ rather than $X^{-\eta}$.

---

# 23. External calibration

The audited source is Gafni–Tao, *On the number of exceptional intervals to the prime number theorem in short intervals*, published in Essential Number Theory 5 (2026), 221–241.

The proof:

1. fixes $\delta$ and $J$ before letting $X\to\infty$ ;
2. uses the truncation height
   $$
   T=J(\log X)^2X^{1-\theta};
   $$
3. disposes of the right-edge zero packet with a Vinogradov–Korobov stretched-log bound;
4. controls the remaining zero strips by $L^2$ and $L^4$ moments and Markov's inequality.

The Guth–Maynard zero-density theorem gives the global bound

$$
A(\sigma)\le\frac{30}{13},
$$

which yields the all-interval threshold $17/30$ and almost-all threshold $2/15$.

Neither theorem currently provides the polynomial shrinking-threshold statement required by B-RH-012.

---

# 24. State transition

```text
CSM_RH v1.28
  ->
CSM_RH v1.29
```

with:

```text
Campaign 37
  CLOSED_AS_SHRINKING_THRESHOLD_GAFNI_TAO_DEPENDENCE_AUDIT

B-RH-013
  SHRINKING_THRESHOLD_EXPLICIT_FORMULA_HEIGHT_LAW
  CREATED / CERTIFIED

O-RH-088
  GAFNI_TAO_FIXED_PARAMETER_NONUNIFORMITY
  CREATED / CERTIFIED

O-RH-089
  GAFNI_TAO_RIGHT_EDGE_SUBPOWER_FLOOR
  CREATED / CERTIFIED

O-RH-090
  MOMENT_ORDER_CANNOT_CURE_POLYNOMIAL_THRESHOLD_AT_SHRINKING_EDGE
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 38
  GROWING_ACCURACY_LAMBDA_RESIDUAL_ATTACK
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

POLYNOMIAL SHRINKING-THRESHOLD EXCEPTIONAL SET = NOT PROVED

GAFNI-TAO FIXED-DELTA THEOREM = NOT UNIFORM IN delta = X^(-eta)

EXPLICIT-FORMULA HEIGHT = PAYS +eta EXPONENT

RIGHT-EDGE ZERO PACKET = X^(-o(1)) FLOOR

STANDARD L2/L4/HIGHER-MOMENT MARKOV = CANNOT CURE SHRINKING EDGE

INTERIOR GUTH-MAYNARD DENSITY = NOT THE PRIMARY BARRIER

NEXT CAMPAIGN = 38
```

The decisive comparison is

$$
\boxed{
\exp
\left[
-c
\frac{
(\log X)^{1/3}
}{
(\log\log X)^{1/3}
}
\right]
\gg
X^{-\eta}
}
$$

for every fixed $\eta>0$.

The present exceptional-set proof reaches the right edge at subpower precision.

The breakthrough gate requires polynomial precision.
