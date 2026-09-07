# CSM_RH Paper 39
## Growing Accuracy, Polynomial $W$, and the Möbius Pointwise Fixed-Strip Lock

**Project:** `CSM_RH`  
**Paper:** `39`  
**Version:** `v0.1`  
**Date:** `2026-09-07`  
**Parent state:** `CSM_RH v1.29 / Paper 38`  
**Campaign:** `38 — GROWING_ACCURACY_LAMBDA_RESIDUAL_ATTACK`  
**Status:** growing-accuracy proof-dependence audit; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Campaign 38 asks whether the 2026 higher-uniformity theorem

$$
\Lambda-\Lambda^\sharp
:
\qquad
H\log^{-A}X
$$

for every fixed $A>0$ can be uniformized by allowing

$$
A=A(X)
$$

to grow strongly enough that the logarithmic saving becomes a fixed power.

The answer for the published pointwise-major-arc architecture is negative.

The surprising feature is that the Type-II amplifier itself would convert a polynomial parameter $W$ into a genuine fixed power.

The obstruction occurs earlier:

> the Dirichlet-polynomial input used to authorize that $W$ is proved only for fixed logarithmic accuracy, and a growing-accuracy version of its Möbius component already implies a fixed-power Mertens bound and hence a fixed zero-free strip.

Thus the current proof cannot be bootstrapped from arbitrary fixed log powers to a fixed $X$ -power without upgrading one of its foundational arithmetic inputs to target-level strength.

No live GLM-5.3-Flash run is claimed.

---

# 1. Current higher-uniformity theorem

For

$$
X^{1/3+\varepsilon}
\le
H
\le
X^{1-\varepsilon},
$$

the 2026 theorem gives, for every fixed

$$
A>0,
$$

$$
\boxed{
\left|
\sum_{x<n\le x+H}
(
\Lambda(n)-\Lambda^\sharp(n)
)
F(g(n)\Gamma)
\right|^\ast
\le
H\log^{-A}X
}
$$

outside an exceptional set of measure

$$
\boxed{
O_A
\left(
\delta^{-O(1)}
X\log^{-A}X
\right).
}
$$

For the constant nilsequence needed by the present campaign, the nilmanifold-complexity issue can be discarded.

The remaining dependence on $A$ is still essential.

---

# 2. Fixed power requires growing accuracy

Suppose we want

$$
\boxed{
\log^{-A(X)}X
=
X^{-\eta+o(1)}
}
$$

for one fixed

$$
\eta>0.
$$

Taking logarithms gives

$$
A(X)\log\log X
=
\eta\log X+o(\log X).
$$

Therefore:

## Theorem 2.1 — Growing-Accuracy Scale

$$
\boxed{
A(X)
=
\eta
\frac{
\log X
}{
\log\log X
}
+
o
\left(
\frac{\log X}{\log\log X}
\right).
}
$$

Create:

```text
O-RH-091
FIXED_POWER_ACCURACY_REQUIRES_GROWING_A
status:
  CERTIFIED
```

---

# 3. The major-arc $W$ parameter

In the proof of Theorem 3.1(i), after the type-I/type-II decomposition, the prime and Möbius type-II terms are treated using Lemma 3.5 with

$$
\boxed{
W=\log^{100A}X.
}
$$

At the growing-accuracy scale of Section 2:

## Theorem 3.1 — Polynomial- $W$ Transition

$$
\boxed{
W
=
X^{100\eta+o(1)}.
}
$$

Thus a fixed $X$ -power target forces the proof's major-arc parameter to become polynomial.

This is not merely a hidden constant issue.

It changes the exponent class of the proof.

---

# 4. Type-II lemma is formally a fixed-power amplifier

Lemma 3.5 assumes

$$
1\le W\le X^{\varepsilon/1000}
$$

and suitable pointwise Dirichlet-polynomial hypotheses.

Its output has the form

$$
\boxed{
\text{Type-II short sum}
\ll
\frac{H}{W^{1/10}}
}
$$

outside an exceptional set of measure

$$
\boxed{
O
\left(
X
\frac{
\log^{O(1)}X
}{
W^{1/10}
}
\right).
}
$$

Therefore:

## Theorem 4.1 — Polynomial- $W$ Type-II Amplifier

If

$$
W=X^{w+o(1)}
$$

with

$$
0<w\le\frac{\varepsilon}{1000},
$$

and the hypotheses of Lemma 3.5 hold uniformly at that $W$, then

$$
\boxed{
\text{Type-II short sum}
\ll
HX^{-w/10+o(1)}
}
$$

outside a set of measure

$$
\boxed{
X^{1-w/10+o(1)}.
}
$$

Create:

```text
B-RH-014
POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
status:
  CERTIFIED
```

This is a component bridge, not a complete theorem for $\Lambda-\Lambda^\sharp$.

---

# 5. Formal admissible $\eta$ window

For

$$
W=X^{100\eta+o(1)},
$$

the structural restriction

$$
W\le X^{\varepsilon/1000}
$$

requires

$$
100\eta
\le
\frac{\varepsilon}{1000}.
$$

Hence:

$$
\boxed{
\eta
\le
\frac{\varepsilon}{100000}.
}
$$

This interval is extremely small but positive.

Therefore the abstract Type-II parameter range does not by itself rule out a fixed exponent.

The problem is the input used to verify the Type-II hypotheses.

---

# 6. Pointwise Dirichlet-polynomial input

Lemma 3.2 of the 2026 paper defines

$$
W_\mu=0,
$$

$$
\boxed{
W_\Lambda=\log^A X,
}
$$

and obtains pointwise maximal Dirichlet-polynomial bounds with constants depending on the fixed parameter $A$.

The proof explicitly reduces the $\mu$ and $\Lambda$ cases to Lemma 3.9(ii)–(iii) of the prequel, which is an application of the Vinogradov–Korobov zero-free region.

The theorem is therefore not stated uniformly for

$$
A=A(X)\to\infty.
$$

---

# 7. The foundational Möbius estimate

The prequel's Lemma 3.9(ii) states, for fixed

$$
A>0,
$$

that for

$$
0<\alpha\le1,
$$

characters of modulus

$$
q\le\log^A X,
$$

and all subintervals

$$
I\subset[X^\alpha,2X^\alpha],
$$

one has a bound of the schematic form

$$
\boxed{
\left|
\sum_{\ell\in I}
\frac{
\mu(r\ell)\chi(\ell)
}{
\ell^{1/2+it}
}
\right|
\ll_{\alpha,A}
\frac{
X^{\alpha/2}
}{
\log^A X
}.
}
$$

This is uniform in

$$
|t|\le X
$$

but not in a growing $A$.

The case

$$
r=1,
\qquad
q=1,
\qquad
t=0,
\qquad
\alpha=1
$$

already contains the obstruction.

---

# 8. Growing $A$ would give a weighted fixed-power Möbius theorem

Assume hypothetically that the estimate of Section 7 were valid for

$$
A(X)
=
\eta
\frac{\log X}{\log\log X}
$$

with an implied constant of size

$$
X^{o(1)}.
$$

Then for every

$$
I\subset[X,2X],
$$

$$
\boxed{
\left|
\sum_{n\in I}
\frac{\mu(n)}{\sqrt n}
\right|
\ll
X^{1/2-\eta+o(1)}.
}
$$

This is already a fixed-power arithmetic estimate.

---

# 9. Partial summation converts it to fixed-power Mertens

Let

$$
S(y)
=
\sum_{X<n\le y}
\frac{\mu(n)}{\sqrt n},
\qquad
X\le y\le2X.
$$

The hypothetical growing-accuracy estimate gives

$$
\sup_{X\le y\le2X}|S(y)|
\ll
X^{1/2-\eta+o(1)}.
$$

Discrete partial summation yields

$$
\sum_{X<n\le2X}\mu(n)
=
\sqrt{2X}\,S(2X)
-
\sum_{X<n<2X}
S(n)
[
\sqrt{n+1}-\sqrt n
].
$$

Hence

$$
\boxed{
\left|
\sum_{X<n\le2X}\mu(n)
\right|
\ll
X^{1-\eta+o(1)}.
}
$$

Summing dyadic blocks gives

## Theorem 9.1 — Growing-Accuracy Möbius Lock

The uniform growing- $A$ extension of Lemma 3.9(ii) would imply

$$
\boxed{
M(X)
=
\sum_{n\le X}\mu(n)
\ll
X^{1-\eta+o(1)}.
}
$$

Create:

```text
O-RH-092
GROWING_ACCURACY_MOBIUS_INPUT_IMPLIES_FIXED_POWER_MERTENS
status:
  CERTIFIED
```

---

# 10. Fixed-power Mertens has fixed-strip strength

By partial summation,

$$
\sum_{n=1}^\infty
\frac{\mu(n)}{n^s}
$$

converges and defines a holomorphic function for

$$
\Re s>1-\eta.
$$

For

$$
\Re s>1,
$$

this function equals

$$
\frac1{\zeta(s)}.
$$

Analytic continuation therefore forces

$$
\boxed{
\zeta(s)\ne0
\qquad
\text{for }
\Re s>1-\eta.
}
$$

Thus the growing-accuracy Möbius input required by the present pointwise route is already a fixed-zero-strip theorem.

Create:

```text
O-RH-093
POINTWISE_GROWING_ACCURACY_ROUTE_FIXED_STRIP_LOCK
status:
  CERTIFIED
```

This is the central closure of Campaign 38.

---

# 11. Why arbitrary fixed $A$ does not evade the lock

For every fixed $A$,

$$
\log^{-A}X
=
X^{-o(1)}.
$$

This is compatible with all currently known zero-free regions.

But the transition

$$
A
\asymp
\frac{\log X}{\log\log X}
$$

changes

$$
\log^{-A}X
$$

into a fixed power.

The fixed- $A$ theorem cannot be diagonalized across $A$ without controlling the dependence of all implied constants and, more importantly, without proving the stronger arithmetic statement in Sections 8–10.

Arbitrary fixed logarithmic accuracy is therefore not a hidden fixed-power theorem.

---

# 12. Exceptional-set constants also become unauthorised

The 2026 theorem gives

$$
O_A
\left(
X\log^{-A}X
\right)
$$

exceptional measure.

At growing

$$
A=A(X),
$$

the unspecified constant

$$
C(A)
$$

must also be controlled.

To conclude

$$
X^{1-c}
$$

one needs at least

$$
C(A(X))
=
X^{o(1)}
$$

relative to the intended exponent budget.

No such growing- $A$ uniformity is supplied by the theorem.

Create:

```text
O-RH-094
FIXED_A_EXCEPTIONAL_CONSTANT_NONUNIFORMITY
status:
  CERTIFIED AS THEOREM-SCOPE AUDIT
```

This is secondary to the Möbius fixed-strip lock.

---

# 13. The prime Dirichlet-polynomial input has the same qualitative issue

The prequel's Lemma 3.9(iii) gives, for fixed $A$, a prime Dirichlet-polynomial estimate for characters of modulus

$$
q\le\log^A X
$$

and derives it by contour integration using the classical zero-free region for Dirichlet $L$ -functions.

At growing

$$
A\asymp
\eta
\frac{\log X}{\log\log X},
$$

the formal modulus range becomes polynomial:

$$
q\le X^{\eta+o(1)}.
$$

A fixed-power version would therefore require a qualitatively stronger prime/Dirichlet- $L$ input.

The present campaign does not need this second lock, because the Möbius input alone already reaches fixed-strip strength.

---

# 14. Current proof architecture is circular at fixed-power precision

The logical chain of the published pointwise major-arc route is:

```text
fixed-A zero-free-region Dirichlet input
  ->
W = log^(100 A) X
  ->
Type-II log-power amplifier
  ->
H log^(-A) X
```

Attempting

```text
A ~ eta log X / log log X
```

changes it to

```text
fixed-power Möbius / prime Dirichlet input
  ->
W = X^(100 eta)
  ->
Type-II fixed-power amplifier
  ->
H X^(-eta')
```

The amplifier works.

The input is already breakthrough-strength.

Create:

```text
O-RH-095
CURRENT_POINTWISE_HIGHER_UNIFORMITY_FIXED_POWER_CIRCULARITY
status:
  CERTIFIED AS CURRENT-METHOD CLOSURE
```

---

# 15. A possible non-circular escape

Lemma 3.5 ultimately proves an integrated estimate of the form

$$
\int
|A(1+it)B(1+it)|^2
\,dt
\ll
\frac{
\log^{O(1)}X
}{
W^{3/10}
}.
$$

Its published proof obtains this by imposing pointwise bounds on one or both Dirichlet-polynomial factors.

Pointwise control at

$$
t=0
$$

is what exposes the fixed-power Mertens lock.

But an integrated product estimate need not logically require a pointwise fixed-power bound at every $t$.

A small set of bad frequencies could, in principle, be tolerated if a sufficiently strong large-value theorem controls their measure and contribution.

This is a genuinely different arithmetic possibility.

It is not solved in Campaign 38.

---

# 16. Campaign 38 track audit

## GA1 — accuracy parameter scaling

```text
status:
  EXACT

A ~ eta log X / log log X
```

## GA2 — W-parameter transition

```text
status:
  POLYNOMIAL

W = log^(100 A) X
  -> X^(100 eta+o(1))
```

## GA3 — Vinogradov–Korobov dependency

```text
status:
  FATAL FOR CURRENT POINTWISE ROUTE

growing-A Möbius input:
  fixed-power Mertens
  -> fixed zero strip
```

## GA4 — exceptional-set parameter uniformity

```text
status:
  NOT PROVIDED FOR GROWING A

secondary obstruction:
  O_A constants
```

## GA5 — direct bridge to shrinking-threshold target

```text
status:
  NOT REACHED

reason:
  foundational pointwise input already target-strength
```

---

# 17. Campaign 38 verdict

No fixed-power residual theorem is proved.

The important positive result is the localization:

```text
polynomial W:
  would be useful

Type-II amplifier:
  already capable of fixed power

published pointwise input:
  only fixed-A

growing pointwise input:
  already fixed-strip strength
```

Thus current higher-uniformity technology does not hide a fixed-power theorem behind the phrase "for every fixed $A$."

---

# 18. New certified package

Create:

```text
B-RH-014
POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
CERTIFIED

O-RH-091
FIXED_POWER_ACCURACY_REQUIRES_GROWING_A
CERTIFIED

O-RH-092
GROWING_ACCURACY_MOBIUS_INPUT_IMPLIES_FIXED_POWER_MERTENS
CERTIFIED

O-RH-093
POINTWISE_GROWING_ACCURACY_ROUTE_FIXED_STRIP_LOCK
CERTIFIED

O-RH-094
FIXED_A_EXCEPTIONAL_CONSTANT_NONUNIFORMITY
CERTIFIED AS THEOREM-SCOPE AUDIT

O-RH-095
CURRENT_POINTWISE_HIGHER_UNIFORMITY_FIXED_POWER_CIRCULARITY
CERTIFIED AS CURRENT-METHOD CLOSURE
```

No new canonical frontier is created.

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
CERTIFIED

B-RH-014
POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
CERTIFIED COMPONENT BRIDGE
```

---

# 20. Campaign 39

The pointwise growing-accuracy route is closed.

The next campaign is:

```text
CSM_RH Campaign 39
AVERAGED_TYPEII_POLYNOMIAL_W_ATTACK
```

The target is to remove the pointwise Dirichlet-polynomial hypothesis from the fixed-power amplifier.

This is a genuinely arithmetic theorem-generation campaign.

---

# 21. Campaign 39 tracks

## AV1 — large-value replacement of pointwise input

Replace

$$
\sup_t|A(1+it)|
\ll
W^{-1/3}
$$

by a distribution estimate for the set

$$
\{
t:
|A(1+it)|>V
\}.
$$

Insert the distribution directly into the $|AB|^2$ integral.

## AV2 — Guth–Maynard large-value technology

Audit whether modern large-value estimates for Dirichlet polynomials can support

$$
W=X^w
$$

at some fixed

$$
w>0
$$

without a pointwise Mertens theorem.

## AV3 — low-frequency excision

The point $t=0$ is measure zero in the Parseval integral.

Quantify the contribution of a neighborhood of zero instead of controlling it pointwise.

A valid theorem must prevent a polynomially wide bad-frequency block.

## AV4 — product large-value geometry

Use the Heath–Brown type-II factorization.

It may be enough that at each frequency at least one factor is small, or that simultaneous large values are rare.

This must be proved quantitatively.

## AV5 — polynomial- $W$ integrated bridge

The admission target is an estimate of the form

$$
\boxed{
\int_{|t|\le T}
|A(1+it)B(1+it)|^2dt
\ll
T
X^{-cw+o(1)}
}
$$

or the exact scale required by Lemma 3.5, with

$$
W=X^w.
$$

If obtained, invoke B-RH-014.

---

# 22. Campaign 39 rejection filters

Reject a candidate if:

## R1. It assumes pointwise fixed-power Mertens.

## R2. It assumes a fixed zero-free strip.

## R3. It merely takes $A=A(X)$ inside a fixed- $A$ theorem.

## R4. It controls only one Dirichlet factor while simultaneous large values remain unbounded.

## R5. The large-value exceptional set is only logarithmically small when a polynomial $W$ is required.

## R6. The final integrated saving is $X^{-o(1)}$.

---

# 23. External calibration

The audit uses two parts of the Matomäki–Radziwiłł–Shao–Tao–Teräväinen architecture.

1. In the 2026 paper, Theorem 1.1 gives $H\log^{-A}X$ discorrelation for every fixed $A$, and the proof of Theorem 3.1 uses
   $$
   W=\log^{100A}X
   $$
   for the $\mu,\Lambda$ type-II terms.

2. Lemma 3.5 converts $W$ into the output factor $W^{-1/10}$.

3. Lemma 3.2 is reduced to the prequel's Lemma 3.9(ii)–(iii), which is proved using the classical zero-free region. The Möbius estimate in Lemma 3.9(ii), if extended uniformly to growing $A$, would already imply a fixed-power Mertens bound.

The next campaign asks whether modern large-value technology can replace this pointwise step by an averaged one.

---

# 24. State transition

```text
CSM_RH v1.29
  ->
CSM_RH v1.30
```

with:

```text
Campaign 38
  CLOSED_AS_GROWING_ACCURACY_POINTWISE_INPUT_AUDIT

B-RH-014
  POLYNOMIAL_W_TYPEII_FIXED_POWER_AMPLIFIER
  CREATED / CERTIFIED

O-RH-091
  FIXED_POWER_ACCURACY_REQUIRES_GROWING_A
  CREATED / CERTIFIED

O-RH-092
  GROWING_ACCURACY_MOBIUS_INPUT_IMPLIES_FIXED_POWER_MERTENS
  CREATED / CERTIFIED

O-RH-093
  POINTWISE_GROWING_ACCURACY_ROUTE_FIXED_STRIP_LOCK
  CREATED / CERTIFIED

O-RH-094
  FIXED_A_EXCEPTIONAL_CONSTANT_NONUNIFORMITY
  CREATED / CERTIFIED

O-RH-095
  CURRENT_POINTWISE_HIGHER_UNIFORMITY_FIXED_POWER_CIRCULARITY
  CREATED / CERTIFIED

F-RH-010
  PESC
  REMAINS OPEN

F-RH-016
  MLEPG
  REMAINS OPEN

Campaign 39
  AVERAGED_TYPEII_POLYNOMIAL_W_ATTACK
  READY
```

---

# 25. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

ARBITRARY FIXED LOG ACCURACY = REAL

GROWING A = REQUIRED FOR FIXED POWER

GROWING A -> POLYNOMIAL W

POLYNOMIAL W TYPE-II AMPLIFIER = VALID

POINTWISE DIRICHLET INPUT AT GROWING A = FIXED-STRIP STRENGTH

FIXED-A THEOREM CANNOT BE DIAGONALIZED TO FIXED POWER

AVERAGED LARGE-VALUE REPLACEMENT = OPEN

NEXT CAMPAIGN = 39
```

The decisive scale conversion is

$$
\boxed{
A
\sim
\eta
\frac{\log X}{\log\log X}
\quad\Longrightarrow\quad
W=\log^{100A}X
=
X^{100\eta+o(1)}.
}
$$

The decisive obstruction is:

$$
\boxed{
\text{uniform growing-}A\text{ Möbius input}
\Longrightarrow
M(X)\ll X^{1-\eta+o(1)}
\Longrightarrow
\zeta(s)\ne0
\text{ for }
\Re s>1-\eta.
}
$$

The current pointwise route therefore reaches the desired fixed power only after importing fixed-strip-strength arithmetic.
