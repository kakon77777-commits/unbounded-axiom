# CSM_RH Paper 04
## Signed-Gate Strength Conservation, the Canonical Centered Aggregate, and Campaign 03 Closure

**Project:** `CSM_RH`  
**Paper:** `04`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v0.4 / Paper 03`  
**Status:** structural reduction / gate-minimality audit; not a proof or disproof of RH  
**中文標題：** CSM_RH 論文 04：符號閘門強度守恆、正則中心化聚合與 Campaign 03 閉合  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** English

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

This paper answers the Campaign 03 question:

> Can a signed, target-faithful principal gate evade the positive $q=1$ bottleneck and also reduce the mathematical strength below fixed-zero-strip level?

The answer is split:

```text
METHOD BYPASS = YES
STRENGTH BYPASS = NO
```

A signed gate already exists in the earlier v3.5 / v3.16 arithmetic architecture.

However, once it is target-faithful at fixed-power level, it is exponent-equivalent to the prime-number-theorem mean square and therefore still carries fixed-zero-strip strength.

No live GLM-5.3-Flash run is claimed.

---

# 1. Campaign 03 starting question

Paper 03 proved the positive-gate obstruction:

```text
O-RH-006
POSITIVE_GATE_PRINCIPAL_NO_BYPASS
```

A positive sufficient gate retaining the $q=1$ principal zeta-packet energy with only subpolynomial loss cannot yield a fixed-power saving without already proving a fixed zeta zero strip.

This left the survivor:

```text
S-RH-008
SIGNED_TARGET_FAITHFUL_PRINCIPAL_GATE
```

The natural hope was that a signed gate might be strictly weaker because it can preserve cancellation which a positive energy destroys.

That hope is correct at the level of proof mechanism.

It is not correct at the level of theorem strength.

---

# 2. Recovery of the pre-existing signed gate

The v3.5 arithmetic decomposition already constructed the required signed interface.

Let

$$
a_n=\Lambda(n)-1.
$$

Define

$$
A(j)
=
\sum_{n\le j}a_n
=
\psi(j)-j.
$$

For

$$
N\le j\le2N-1,
$$

define the discrete PNT mean square

$$
\boxed{
J_N
=
\sum_{j=N}^{2N-1}
A(j)^2.
}
$$

Let $\mathcal R_N(h)$ be the singular-series-centered endpoint-Cesàro shift residual from v3.5.

The exact v3.5 identity is

$$
\boxed{
J_N
=
D_N
+
2\mathcal M_N
+
2
\sum_{h=1}^{2N-2}
\mathcal R_N(h).
}
$$

The deterministic diagonal plus averaged singular-series contribution satisfies

$$
\boxed{
D_N+\mathcal M_N
=
O(N^2\log N).
}
$$

Therefore

$$
\boxed{
J_N
=
2
\sum_{h=1}^{2N-2}
\mathcal R_N(h)
+
O(N^2\log N).
}
$$

This identity is the canonical signed-principal interface.

---

# 3. Canonical Centered Signed Aggregate

Define

$$
\boxed{
\mathcal A_N
=
\sum_{h=1}^{2N-2}
\mathcal R_N(h).
}
$$

For

$$
0\le\kappa\le1,
$$

define the gate:

## CSSA $(\kappa)$

$$
\boxed{
|\mathcal A_N|
\ll
N^{3-\kappa+o(1)}.
}
$$

The name is:

```text
CSSA
CENTERED SIGNED SHIFT AGGREGATE
```

This is not a new representation.

It is a CSM_RH promotion of the already-derived v3.5 minimal signed arithmetic gate.

---

# 4. The signed aggregate is not freely oscillatory

From Section 2,

$$
\boxed{
\mathcal A_N
=
\frac12J_N
+
O(N^2\log N).
}
$$

Because

$$
J_N\ge0,
$$

the global signed aggregate is constrained by a positive mean square.

Thus the phrase `signed cancellation` must be interpreted carefully.

The individual shift residuals

$$
\mathcal R_N(h)
$$

may have either sign, and their cancellation is essential.

But after the full canonical endpoint and shift aggregation, the surviving signed quantity reconstructs the PNT mean square up to a lower-order deterministic term.

Therefore:

```text
SIGNED
does not mean
UNCONSTRAINED RANDOM-SIGN SAVING.
```

Any fixed-power saving for $\mathcal A_N$ is a fixed-power saving for the PNT mean square.

---

# 5. Discrete-continuous mean-square interface

Define

$$
\boxed{
I(N)
=
\int_N^{2N}
|\psi(x)-x|^2dx.
}
$$

The exact v3.5 discrete-continuous relation is

$$
I(N)
=
J_N
-
\sum_{j=N}^{2N-1}A(j)
+
\frac N3.
$$

Cauchy-Schwarz gives

$$
\left|
\sum_{j=N}^{2N-1}A(j)
\right|
\le
N^{1/2}J_N^{1/2}.
$$

Consequently,

$$
I(N)
=
J_N
+
O
\left(
N^{1/2}J_N^{1/2}
+
N
\right),
$$

and conversely

$$
J_N
\ll
I(N)+N.
$$

At every exponent

$$
\delta>1,
$$

 $I(N)$ and $J_N$ therefore have the same upper-bound exponent.

---

# 6. Exact fixed-exponent equivalence of the signed gate

## Theorem 6.1 — CSSA / PNT mean-square exponent equivalence

For every fixed

$$
0\le\kappa\le1,
$$

the following are equivalent at $N^{o(1)}$ exponent resolution:

$$
\boxed{
\operatorname{CSSA}(\kappa)
}
$$

$$
\boxed{
J_N
\ll
N^{3-\kappa+o(1)}
}
$$

and

$$
\boxed{
I(N)
\ll
N^{3-\kappa+o(1)}.
}
$$

### Proof

The identity

$$
J_N
=
2\mathcal A_N
+
O(N^2\log N)
$$

shows that CSSA $(\kappa)$ implies the $J_N$ bound because

$$
N^2\log N
=
N^{2+o(1)}
\le
N^{3-\kappa+o(1)}
$$

for

$$
0\le\kappa\le1.
$$

Conversely,

$$
\mathcal A_N
=
\frac12J_N
+
O(N^2\log N)
$$

shows that the $J_N$ bound implies CSSA $(\kappa)$.

Section 5 gives exponent-equivalence between $J_N$ and $I(N)$.

 $\square$

---

# 7. Fixed zero-strip consequence

Let

$$
\Theta_\zeta
=
\sup_\rho\Re\rho.
$$

The classical PNT mean-square / zero relation used in the earlier AMRAL audit gives:

if

$$
I(N)
\ll
N^{3-\kappa+o(1)},
$$

then

$$
\boxed{
\Theta_\zeta
\le
1-\frac{\kappa}{2}.
}
$$

Combining with Theorem 6.1:

## Corollary 7.1 — CSSA fixed-strip strength

For every fixed

$$
\kappa>0,
$$

$$
\boxed{
\operatorname{CSSA}(\kappa)
\Longrightarrow
\Theta_\zeta
\le
1-\frac{\kappa}{2}.
}
$$

Therefore every positive fixed-power CSSA gain is genuine zero-strip mathematics.

---

# 8. RH endpoint

At

$$
\kappa=1,
$$

CSSA becomes

$$
|\mathcal A_N|
\ll
N^{2+o(1)}.
$$

Theorem 6.1 gives

$$
I(N)
\ll
N^{2+o(1)}.
$$

The mean-square zero relation then forces

$$
\Theta_\zeta\le\frac12.
$$

Functional-equation symmetry gives

$$
\Theta_\zeta\ge\frac12.
$$

Hence CSSA $(1)$ implies RH.

Conversely, on RH the classical PNT mean square satisfies

$$
I(N)
=
O(N^2),
$$

so Theorem 6.1 gives CSSA $(1)$.

Therefore:

$$
\boxed{
\operatorname{CSSA}(1)
\Longleftrightarrow
RH
}
$$

at exponent level.

This endpoint equivalence is not advertised as an easier RH criterion.

It is a strength calibration.

---

# 9. The v3.16 FPD gate is also breakthrough-strength

v3.16 defined the signed four-point prime deviation gate:

$$
\boxed{
|\mathfrak E_{4,N}|
\ll
N^{5-\eta+o(1)}.
}
$$

Together with the closed deterministic four-point model,

$$
\mathfrak M_{4,N}
\ll
N^{9/2+o(1)},
$$

v3.16 derived

$$
I(N)
\ll
N^{
3-\kappa_{\rm FPD}+o(1)
},
$$

where

$$
\boxed{
\kappa_{\rm FPD}
=
\frac12
\min
\left(
\eta,
\frac12
\right).
}
$$

Therefore:

## Corollary 9.1

For every fixed

$$
\eta>0,
$$

FPD $(\eta)$ implies

$$
\boxed{
\Theta_\zeta
\le
1
-
\frac14
\min
\left(
\eta,
\frac12
\right).
}
$$

Thus the earlier signed three-parameter cancellation gate already bypassed positive domination structurally, but never bypassed fixed-zero-strip strength.

---

# 10. Target-Strength Conservation

The previous examples motivate a CSM_RH closure law.

## Definition 10.1

Let $T(\kappa)$ be a target family with the certified implication

$$
T(\kappa)
\Longrightarrow
\Theta_\zeta
\le
1-c\kappa
$$

for some

$$
c>0.
$$

Let $G(\lambda)$ be a sufficient gate satisfying

$$
G(\lambda)
\Longrightarrow
T(\kappa(\lambda)).
$$

Then theorem strength propagates backward through the sufficient-gate edge.

## Theorem 10.2 — Target-Strength Conservation

If

$$
\kappa(\lambda)>0,
$$

then

$$
\boxed{
G(\lambda)
\Longrightarrow
\text{a fixed zeta zero strip}.
}
$$

A gate may improve:

- locality;
- sign structure;
- averaging;
- proof accessibility;
- compatibility with analytic tools;
- compatibility with sieve or bilinear methods.

But it cannot be classified as sub-breakthrough merely because its formula is signed or more local.

The new obstruction is:

```text
O-RH-007
TARGET_STRENGTH_CONSERVATION
status:
  CERTIFIED
```

---

# 11. Positive-gate obstruction versus strength conservation

Two different CSM_RH obstructions must now be separated.

## O-RH-006

```text
POSITIVE_GATE_PRINCIPAL_NO_BYPASS
```

This says a positive gate retaining the principal zeta packet inherits fixed-strip strength through the $q=1$ packet.

## O-RH-007

```text
TARGET_STRENGTH_CONSERVATION
```

This says even a signed gate inherits fixed-strip strength if it is sufficient for a fixed-power target already known to imply a fixed strip.

Therefore:

$$
\boxed{
\text{signed architecture}
}
$$

can escape

$$
O\text{-}RH\text{-}006,
$$

but not

$$
O\text{-}RH\text{-}007.
$$

This is the main closure result of Campaign 03.

---

# 12. Campaign 03 candidate audit

## C03-A — Signed principal mismatch

Status:

```text
FOUND ALREADY
PROMOTED AS CSSA
```

The v3.5 centered signed aggregate is the canonical instance.

It is target-faithful but fixed-strip strength.

---

## C03-B — Linearized pole-residual observable

Status:

```text
VALID PROOF-MECHANISM CANDIDATE
NO STRENGTH REDUCTION
```

If a lossless bridge from this observable to CSSA $(\kappa)$ is proved, `O-RH-007` immediately applies.

---

## C03-C — Polarized cross-correlation

Status:

```text
VALID PROOF-MECHANISM CANDIDATE
NO STRENGTH REDUCTION
```

Polarization may preserve cancellation discarded by positive squaring.

But any fixed-power implication to CSSA or FPD remains breakthrough-strength.

---

## C03-D — Scale-frequency signed transform

Status:

```text
DEFERRED AS TRANSFORM CANDIDATE
```

A transform may make cancellation more visible.

A lossless inverse or target-fidelity bridge is mandatory.

If it is target-faithful at fixed power, theorem strength remains unchanged.

---

## C03-E — Direct pair-spectrum signed difference

Status:

```text
ALREADY REPRESENTED BY FPD / CENTERED PRIME DEVIATION
```

This route is structurally legitimate but fixed-strip strength for every positive fixed-power gain.

---

## C03-F — Certified principal-subterm cancellation

Status:

```text
SURVIVOR AS PROOF MECHANISM
```

This is the most important remaining signed possibility.

The aim is no longer to weaken theorem strength.

The aim is to prove the required breakthrough through arithmetic cancellation without first dominating a positive RH-complete energy.

---

# 13. Campaign 03 verdict

Campaign 03 asked whether a signed target-faithful gate could be genuinely weaker than the positive principal packet gate.

The result is:

```text
SIGNED GATE EXISTS
  YES

POSITIVE q=1 DOMINATION CAN BE AVOIDED
  YES

FIXED-STRIP THEOREM STRENGTH CAN BE AVOIDED
  NO

CAN SIGNED STRUCTURE STILL BE A BETTER PROOF INTERFACE
  YES
```

Thus `S-RH-008` changes status.

Old:

```text
SIGNED_TARGET_FAITHFUL_PRINCIPAL_GATE
OPEN / SURVIVOR
```

New:

```text
SIGNED_TARGET_FAITHFUL_PRINCIPAL_GATE
INTERFACE_EXISTENCE = CLOSED
FIXED_POWER_ESTIMATE = OPEN
```

---

# 14. New canonical arithmetic frontier

Create:

```text
F-RH-006
CENTERED_SIGNED_SHIFT_AGGREGATE
abbrev:
  CSSA
status:
  OPEN
type:
  MINIMAL_SIGNED_ARITHMETIC_FRONTIER
source:
  AMRAL RH v3.5
```

Its gate is

$$
\boxed{
|\mathcal A_N|
\ll
N^{3-\kappa+o(1)}.
}
$$

For

$$
\kappa>0,
$$

this is a fixed-zero-strip breakthrough.

For

$$
\kappa=1,
$$

it is RH-level.

The term `minimal` is relative to the v3.5 centered-shift decomposition: no Cauchy-Schwarz or positive norm is inserted after the exact endpoint and shift summation.

No universal minimality claim over all possible RH formulations is made.

---

# 15. Reclassification of the major-arc detour

The v3.17-v3.18 positive pair-spectrum / character-major-arc program was not wasted.

It proved several useful facts:

- genuine minor arcs admit fixed-power saving;
- character major arcs expose explicit zero packets;
- zero density alone is insufficient;
- packet interference can be globalized analytically;
- positive EMAE necessarily contains a fixed zeta strip;
- the $q=1$ bottleneck is exact.

However, Campaign 03 shows that the positive energy route is a stronger analytic interface than the earlier signed v3.5 target.

Therefore the canonical frontier hierarchy becomes:

```text
ROOT ARITHMETIC TARGET

CSSA
  minimal signed centered aggregate

FPD
  signed four-point sufficient gate

EPV / PPEU
  positive variance gates

EMAE / ZPPF
  positive major-arc zero-energy gates
```

Moving downward in this list may improve analytic tractability.

It does not automatically reduce theorem strength.

---

# 16. Why the research should return to CSSA

The current CSM_RH state has already answered the representation questions required to justify a direct arithmetic attack.

Continuing to design stronger positive energies risks repeatedly encountering `O-RH-006`.

Continuing to design weaker-looking but target-faithful gates risks `O-RH-007`.

The shortest remaining arithmetic statement is now explicit:

$$
\boxed{
\sum_{h=1}^{2N-2}
\mathcal R_N(h)
=
O(N^{3-\kappa+o(1)})
}
$$

for some fixed

$$
\kappa>0.
$$

This is genuine number theory.

There is no remaining reason to call it a routine tail estimate.

---

# 17. Signed cancellation is constrained cancellation

A future worker must not reason:

```text
there are many positive and negative shift residuals
therefore square-root cancellation is plausible
```

without proving an arithmetic mechanism.

The identity

$$
\mathcal A_N
=
\frac12J_N
+
O(N^2\log N)
$$

shows that the full cancellation pattern is constrained by the square of the PNT error.

A valid proof must explain why the centered prime correlations collectively reproduce a smaller PNT mean square.

Possible mechanisms must be structural, not probabilistic rhetoric.

---

# 18. Campaign 04

The next worker campaign is:

```text
CSM_RH Campaign 04
CENTERED_SIGNED_ARITHMETIC_CANCELLATION
```

Target:

```text
F-RH-006
CSSA(kappa)
for any fixed kappa > 0
```

The campaign is no longer a gate-design campaign.

It is a direct arithmetic proof campaign.

---

# 19. Campaign 04 admissible mechanism families

## A. Signed dispersion after exact centering

Apply dispersion only after subtracting the singular-series backbone.

Do not square the uncentered correlation.

## B. Vaughan / Heath-Brown bilinear decomposition

Decompose $\Lambda$ inside the centered signed aggregate while preserving the outer endpoint and shift signs until the last possible stage.

## C. Endpoint-kernel bilinear cancellation

Exploit the exact Cesàro endpoint weight

$$
W_N(h)
$$

rather than replacing it by a uniform box.

## D. Dyadic scale telescoping

Search for cancellation between neighboring endpoint scales before absolute values are taken.

## E. Fourier coefficient at zero after centering

Use the identity

$$
\sum_h
\mathcal R_N(h)e(h\alpha)
=
P_+
[
G_N\overline F_N
]
-
M_N^+(\alpha)
$$

and evaluate the signed aggregate through the centered Fourier object without taking its full $L^2$ norm.

## F. Certified principal-subterm cancellation

Identify exact pairs or families of arithmetic subterms whose cancellation follows from algebra, reciprocity, functional identities, or a proved oscillatory estimate.

These are search families, not established theorems.

---

# 20. Campaign 04 hard rejection filters

Reject a candidate if it:

## R1. Squares before centering

This returns to a stronger positive gate.

## R2. Applies triangle inequality before the decisive signed sum

This may destroy the only structural advantage of CSSA.

## R3. Assumes random-sign cancellation

A statistical metaphor is not a proof.

## R4. Deletes the singular-series model without an exact identity

The deterministic backbone must be subtracted canonically.

## R5. Uses only log-power saving

The target requires a fixed

$$
N^{-\kappa}.
$$

## R6. Hides a fixed zero strip as an input

Any such candidate is circular at the current target.

## R7. Uses finite numerical cancellation as a global theorem

Finite checks are diagnostics only.

---

# 21. Worker role split

`CSM_RH` remains the protocol.

GLM-5.3-Flash may be used as a replaceable high-volume worker provider.

## Designer

Must produce:

```text
arithmetic mechanism
exact signed object
where cancellation occurs
why model subtraction is preserved
predicted exponent gain
failure modes
```

## Builder

Must produce:

```text
complete expansion
Type I / II / bilinear ranges if used
endpoint and shift weights
quantifier order
uniformity
explicit exponent ledger
unproved lemmas
```

## Verifier

Must test:

```text
triangle-inequality leakage
hidden positive gate
hidden zero-strip input
model-subtraction correctness
exceptional-zero sensitivity
fixed-power versus log-power
finite-to-global leakage
```

The frontier model remains final promotion authority.

---

# 22. External strength calibration

The external literature remains consistent with this classification.

Chou, Haag, Huryn, and Ledoan relate the Hardy-Littlewood prime-pair error variance to prime exponential sums and prove a lower bound of the form

$$
E(N)
=
\Omega
\left(
N^{1+2\Theta_\zeta-\varepsilon}
\right).
$$

Thus a fixed-power upper bound for the standard positive pair variance already has zero-strip consequences.

Brent, Platt, and Trudgian prove on RH that the PNT mean square is

$$
O(N^2)
$$

on dyadic intervals, consistent with the CSSA endpoint calibration.

Zaccagnini's mean-square / zero-distribution framework supplies the converse zero-strip strength implication used in the AMRAL chain.

The present paper's new contribution is not those external theorems.

It is the CSM_RH identification that the signed gate already existed and that its exact arithmetic identity makes the distinction:

```text
proof-mechanism weakening
versus
theorem-strength weakening
```

unavoidable.

---

# 23. State transition

The canonical transition is:

```text
CSM_RH v0.4
  ->
CSM_RH v0.5
```

with:

```text
Campaign 03
  CLOSED_AS_GATE_MINIMALITY_AUDIT

S-RH-008
  SIGNED_TARGET_FAITHFUL_PRINCIPAL_GATE
  interface existence:
    CLOSED
  fixed-power estimate:
    OPEN

F-RH-006
  CENTERED_SIGNED_SHIFT_AGGREGATE
  CREATED / OPEN

O-RH-007
  TARGET_STRENGTH_CONSERVATION
  CREATED / CERTIFIED

S-RH-009
  STRUCTURAL_SIGNED_CANCELLATION_MECHANISM
  CREATED / OPEN

Campaign 04
  CENTERED_SIGNED_ARITHMETIC_CANCELLATION
  READY
```

---

# 24. Final status

```text
RH = OPEN

POSITIVE PRINCIPAL BYPASS
= NO

SIGNED PRINCIPAL INTERFACE
= EXISTS

SIGNED FIXED-POWER ESTIMATE
= OPEN

SIGNED METHOD BYPASS
= YES

SIGNED STRENGTH BYPASS
= NO

CANONICAL MINIMAL ARITHMETIC FRONTIER
= CSSA

NEXT CAMPAIGN
= DIRECT CENTERED SIGNED CANCELLATION
```

The central identity is:

$$
\boxed{
\sum_h
\mathcal R_N(h)
=
\frac12
\sum_{j=N}^{2N-1}
(\psi(j)-j)^2
+
O(N^2\log N).
}
$$

Consequently,

$$
\boxed{
\operatorname{CSSA}(\kappa)
\Longleftrightarrow_{\rm exponent}
I(N)
\ll
N^{3-\kappa+o(1)}.
}
$$

Therefore:

$$
\boxed{
\kappa>0
\Longrightarrow
\text{fixed zeta zero strip},
}
$$

and

$$
\boxed{
\kappa=1
\Longleftrightarrow
RH
}
$$

at exponent level.

The next work should no longer search for a weaker gate.

It should search for a real arithmetic cancellation theorem.
