# CSM_RH Paper 20
## Mellin Pole Recovery and Exact Single-Zero Sensitivity of Fixed-Power Prime Mean Square

**Project:** `CSM_RH`  
**Paper:** `20`  
**Version:** `v0.1`  
**Date:** `2026-09-06`  
**Parent state:** `CSM_RH v1.10 / Paper 19`  
**Campaign:** `19 — SINGLE_ZERO_SENSITIVE_THEOREM_GENERATION`  
**Status:** single-zero sensitivity bridge certified; not a proof or disproof of RH

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

Paper 19 showed that zero-density information is blind to a finite number of persistent off-axis zeros and required every new mechanism to be sensitive to a single such zero.

The present paper closes that bridge problem.

The key point is:

> a fixed-power dyadic $L^2$ bound for $\psi(x)-x$ analytically continues the Mellin transform of the prime error into a fixed half-plane; every zeta zero in that half-plane would be a pole of $\zeta'/\zeta$, so even one isolated zero is excluded.

No explicit zero-packet cancellation argument is needed.

No zero Gram is needed.

No live GLM-5.3-Flash run is claimed.

---

# 1. Chebyshev error

Define

$$
\psi(x)
=
\sum_{n\le x}\Lambda(n).
$$

Define

$$
\boxed{
E(x)
=
\psi(x)-x.
}
$$

For

$$
\Re s>1,
$$

the Mellin transform of $\psi$ satisfies

$$
\boxed{
\int_1^\infty
\psi(x)x^{-s-1}\,dx
=
-\frac1s
\frac{\zeta'(s)}{\zeta(s)}.
}
$$

Also,

$$
\int_1^\infty
x\,x^{-s-1}\,dx
=
\frac1{s-1}.
$$

Therefore:

## Theorem 1.1 — Prime-Error Mellin Identity

For

$$
\Re s>1,
$$

$$
\boxed{
\int_1^\infty
E(x)x^{-s-1}\,dx
=
-\frac1s
\frac{\zeta'(s)}{\zeta(s)}
-
\frac1{s-1}.
}
$$

Equivalently,

$$
\boxed{
s
\int_1^\infty
E(x)x^{-s-1}\,dx
=
-\frac{\zeta'(s)}{\zeta(s)}
-
\frac{s}{s-1}.
}
$$

The apparent pole at $s=1$ cancels in the prime-error combination.

---

# 2. Dyadic mean-square hypothesis

Fix

$$
0<\kappa<1.
$$

Assume that for every

$$
\varepsilon>0,
$$

one has uniformly for large $X$,

$$
\boxed{
\int_X^{2X}
|E(x)|^2\,dx
\ll_\varepsilon
X^{3-\kappa+\varepsilon}.
}
$$

Call this:

```text
DMS(kappa)
DYADIC_MEAN_SQUARE(kappa)
```

---

# 3. Dyadic Mellin convergence

Let

$$
s=\sigma+it.
$$

On one dyadic block,

$$
I_X(s)
=
\int_X^{2X}
E(x)x^{-s-1}\,dx.
$$

By Cauchy–Schwarz,

$$
\begin{aligned}
|I_X(s)|
&\le
\left(
\int_X^{2X}|E(x)|^2\,dx
\right)^{1/2}
\left(
\int_X^{2X}x^{-2\sigma-2}\,dx
\right)^{1/2}
\\
&\ll_\varepsilon
X^{(3-\kappa+\varepsilon)/2}
X^{-\sigma-1/2}
\\
&=
X^{1-\kappa/2-\sigma+\varepsilon/2}.
\end{aligned}
$$

Thus the dyadic series

$$
\sum_{j\ge0}
\int_{2^j}^{2^{j+1}}
E(x)x^{-s-1}\,dx
$$

converges absolutely and locally uniformly whenever

$$
\boxed{
\sigma
>
1-\frac{\kappa}{2}.
}
$$

Indeed, on any compact subset of that half-plane one chooses $\varepsilon>0$ smaller than twice the distance to the boundary.

Therefore:

## Theorem 3.1 — Mellin Holomorphy from Fixed-Power Mean Square

Under DMS $(\kappa)$, the function

$$
\boxed{
\mathcal M_E(s)
=
\int_1^\infty
E(x)x^{-s-1}\,dx
}
$$

extends holomorphically to

$$
\boxed{
\Re s
>
1-\frac{\kappa}{2}.
}
$$

---

# 4. Pole recovery

On

$$
\Re s>1,
$$

Theorem 1.1 gives

$$
\boxed{
-\frac{\zeta'(s)}{\zeta(s)}
=
s\mathcal M_E(s)
+
\frac{s}{s-1}.
}
$$

Let

$$
\rho
$$

be a nontrivial zero of $\zeta$ of multiplicity $m_\rho$.

Then

$$
\frac{\zeta'(s)}{\zeta(s)}
$$

has a pole at $s=\rho$ with residue $m_\rho$.

Hence:

## Theorem 4.1 — Mellin Pole Recovery

DMS $(\kappa)$ implies

$$
\boxed{
\zeta(s)\neq0
\qquad
\text{for }
\Re s
>
1-\frac{\kappa}{2}.
}
$$

No density argument is used.

No averaging over zeros is used.

One zero in the half-plane would already contradict Mellin holomorphy.

---

# 5. Exact single-zero sensitivity

Suppose hypothetically there were exactly one off-axis zero

$$
\rho_0
=
\beta_0+i\gamma_0
$$

with

$$
\beta_0
>
1-\frac{\kappa}{2}.
$$

Then

$$
-\frac{\zeta'}{\zeta}
$$

would have a pole at $\rho_0$.

No cancellation with any other zero can remove that meromorphic pole.

Therefore the dyadic fixed-power mean-square theorem is sensitive to one persistent zero even when zero-density information is not.

Create:

```text
B-RH-001
MELLIN_POLE_RECOVERY
status:
  CERTIFIED
```

---

# 6. No explicit-formula cancellation authority is needed

Earlier branches repeatedly asked whether one zero mode could be cancelled by the rest of the zero packet.

For this bridge that question is unnecessary.

The Mellin transform analytically recovers the logarithmic derivative itself.

Distinct zeros are distinct poles.

Thus:

```text
ZERO-PACKET POINTWISE CANCELLATION
  irrelevant to Mellin pole recovery

GRAM DECOMPOSITION
  unnecessary

ZERO-DENSITY COUNT
  unnecessary

SINGLE-ZERO ISOLATION
  exact through meromorphic structure
```

---

# 7. MLEPG to the fixed strip

Paper 17 proved the deterministic residue-chain implication.

Assume MLEPG $(\alpha,\delta)$:

$$
\mathcal S_\Lambda(N,N^\alpha)
\ll
N^{1+\alpha+o(1)}
+
N^{1+2\alpha-\delta+o(1)}
$$

for fixed

$$
0<\alpha<\frac23,
\qquad
\delta>0.
$$

Then for every sufficiently small fixed

$$
\kappa
<
\min
\{
\alpha,
\delta,
2-2\alpha
\},
$$

one obtains

$$
\boxed{
\int_X^{2X}
|\psi(x)-x|^2\,dx
\ll
X^{3-\kappa+o(1)}.
}
$$

Combining with Theorem 4.1:

## Theorem 7.1 — MLEPG Single-Zero Exclusion Law

MLEPG $(\alpha,\delta)$ implies

$$
\boxed{
\zeta(s)\neq0
\qquad
\Re s
>
1-\frac{\kappa}{2}
}
$$

for every fixed

$$
0<\kappa
<
\min
\{
\alpha,
\delta,
2-2\alpha
\}.
$$

Thus the MLEPG fixed power has exact fixed-zero-strip authority.

---

# 8. Natural scale calibration

At the current almost-all short-interval range

$$
\alpha>\frac2{15},
$$

suppose one could prove MLEPG with fixed

$$
\delta>0.
$$

Then one could choose

$$
\kappa
<
\min
\left\{
\frac2{15},
\delta
\right\}
$$

up to an arbitrarily small scale margin and obtain a fixed zero-free strip of width approximately

$$
\boxed{
\frac12
\min
\left\{
\frac2{15},
\delta
\right\}.
}
$$

This is a strength ledger, not a proof of MLEPG.

---

# 9. PODEE / PESC single-zero sensitivity

Paper 10 strips prime powers for every first target exponent

$$
0<\kappa<\frac12.
$$

Paper 11 proves PODEE and PESC exponent-equivalent.

Therefore:

## Corollary 9.1

For every fixed

$$
0<\kappa<\frac12,
$$

a PESC / PODEE bound

$$
N^{3-\kappa+o(1)}
$$

implies, after the certified prime-power bridge,

$$
\boxed{
\zeta(s)\neq0
\qquad
\Re s
>
1-\frac{\kappa}{2}.
}
$$

Thus the root arithmetic frontier has exact single-zero authority.

---

# 10. Campaign 19 track audit

## Z1 — multiscale Fejer coefficient recovery

```text
status:
  NOT NEEDED FOR SINGLE-ZERO AUTHORITY

reason:
  Mellin pole recovery is simpler and representation-independent
```

## Z2 — smooth Mellin zero packet

Standard smoothed explicit formulae produce absolutely convergent zero packets and remain a valid optional representation.

Status:

```text
VALID OPTIONAL REPRESENTATION
NOT A MISSING BRIDGE
```

## Z3 — zero-pair Gram coercivity

```text
status:
  REJECTED AS UNNECESSARY

reason:
  pole recovery supplies gauge-independent single-zero authority
```

## Z4 — prime-side multiscale contraction

```text
status:
  OPEN AS A PROOF MECHANISM FOR MLEPG / PESC
```

This is now purely a prime-side theorem-generation question.

---

# 11. Closure of S-RH-027

Paper 19 created:

```text
S-RH-027
SINGLE_ZERO_SENSITIVE_PRINCIPAL_ARC_MECHANISM
```

The present result changes its state to:

```text
S-RH-027
CLOSED_AS_BRIDGE_REQUIREMENT

certificate:
  B-RH-001 MELLIN_POLE_RECOVERY
```

Important:

```text
single-zero sensitivity
  CLOSED

fixed-power prime theorem
  OPEN
```

---

# 12. New obstruction: no cancellation escape after fixed-power mean square

Create:

```text
O-RH-045
MELLIN_POLE_NO_ZERO_CANCELLATION_ESCAPE
status:
  CERTIFIED
```

Statement:

> Once a fixed-power dyadic mean-square bound for $\psi(x)-x$ is proved, an off-axis zero cannot be hidden by cancellation among explicit-formula modes. The Mellin transform recovers the logarithmic derivative, and every zero is a pole.

---

# 13. What remains open

The remaining unknown is not:

```text
how to isolate one zero;
how to prevent zero-packet cancellation;
how to convert a fixed-power mean square into a fixed strip.
```

Those bridges are now certified.

The unknown is:

$$
\boxed{
\text{how to prove the fixed-power prime-side estimate itself}.
}
$$

Concretely:

```text
PESC fixed power
or
MLEPG fixed power
```

remains open.

---

# 14. Research-mode correction

Future workers must not count any of the following as progress:

```text
a new zero-density exponent;
a new exceptional-set theorem with fixed relative tolerance;
a new explicit-formula representation;
a new zero Gram;
another coefficient-isolation proposal.
```

Unless such a result actually creates the prime-side fixed power, the single-zero bridge problem has already been solved by B-RH-001.

---

# 15. Campaign 20

The next campaign is:

```text
CSM_RH Campaign 20
PRIME_SIDE_FIXED_POWER_LEMMA_GENERATION
```

Root target:

```text
F-RH-010
PESC
```

Working candidate:

```text
F-RH-016
MLEPG
```

The campaign is forbidden from introducing another zero-side surrogate.

---

# 16. Campaign 20 allowed tracks

## A1 — principal-arc arithmetic estimate

Prove the principal Fejer local $L^2$ power directly from prime exponential sums without using a fixed zero-free strip.

## A2 — shrinking-threshold short-interval theorem

Prove

$$
|\psi(x+H)-\psi(x)-H|
\le
HX^{-\eta}
$$

for all but a power-saving exceptional set, with fixed $\eta>0$.

## A3 — direct lag-energy theorem

Prove MLEPG in $L^2$ without passing through pointwise good/bad intervals.

## A4 — prime-side scale contraction

Find a recurrence for PESC / lag energy whose cumulative contraction mass is linear in $\log X$.

## A5 — new signed arithmetic cancellation

Produce a fixed-power theorem directly for the centered prime self-correlation.

---

# 17. Campaign 20 rejection filters

Reject a candidate if:

## R1. It is only a zero-density improvement.

## R2. It supplies only a new zero-free region with width tending to zero.

## R3. It re-solves single-zero isolation.

## R4. It obtains only $\log^{-A}X$ or stretched-log savings.

## R5. It assumes PESC / MLEPG.

## R6. It assumes a fixed zero-free strip.

## R7. It creates another equivalent criterion with no new estimate.

---

# 18. External calibration

The bridge uses standard analytic-number-theory identities.

1. The Mellin transform of the Chebyshev $\psi$ function is
   $$
   \int_1^\infty
   \psi(x)x^{-s-1}\,dx
   =
   -\frac{\zeta'(s)}{s\zeta(s)}
   $$
   for $\Re s>1$.

2. Standard smoothed explicit formulae express smooth prime sums as absolutely convergent sums over zeta zeros and provide an alternative coefficient-recovery viewpoint.

3. The logarithmic derivative $\zeta'/\zeta$ has a pole at every zero of $\zeta$, with residue equal to the zero multiplicity.

The CSM_RH contribution here is their placement as the exact bridge authority for the already constructed PESC / MLEPG closure graph.

---

# 19. State transition

The canonical transition is:

```text
CSM_RH v1.10
  ->
CSM_RH v1.11
```

with:

```text
Campaign 19
  CLOSED_AS_SINGLE_ZERO_SENSITIVITY_BRIDGE_CERTIFICATION

B-RH-001
  MELLIN_POLE_RECOVERY
  CREATED / CERTIFIED

O-RH-045
  MELLIN_POLE_NO_ZERO_CANCELLATION_ESCAPE
  CREATED / CERTIFIED

S-RH-027
  SINGLE_ZERO_SENSITIVE_PRINCIPAL_ARC_MECHANISM
  CLOSED_AS_BRIDGE_REQUIREMENT

F-RH-016
  MLEPG
  REMAINS OPEN

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 20
  PRIME_SIDE_FIXED_POWER_LEMMA_GENERATION
  READY
```

---

# 20. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

SINGLE-ZERO SENSITIVITY = CERTIFIED

ZERO-PACKET CANCELLATION ESCAPE = CLOSED

FIXED-POWER MEAN SQUARE -> FIXED ZERO STRIP = CERTIFIED

ZERO-SIDE SURROGATE GENERATION = STOPPED

NEXT MODE = PRIME-SIDE FIXED-POWER LEMMA GENERATION
```

The decisive bridge is:

$$
\boxed{
\int_X^{2X}
|\psi(x)-x|^2\,dx
\ll
X^{3-\kappa+o(1)}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\int_1^\infty
[\psi(x)-x]x^{-s-1}\,dx
\text{ is holomorphic for }
\Re s>1-\frac{\kappa}{2}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\zeta(s)\neq0
\qquad
\Re s>1-\frac{\kappa}{2}.
}
$$

From this point onward, a successful CSM_RH candidate must create the fixed power on the prime side.
