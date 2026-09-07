# CSM_RH Paper 17
## Mesoscopic Lag-Energy Power Gain and the First Direct PESC Theorem Candidate

**Project:** `CSM_RH`  
**Paper:** `17`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.7 / Paper 16`  
**Campaign:** `16 — DIRECT_PESC_THEOREM_GENERATION`  
**Status:** direct theorem-candidate generation / deterministic bridge certification; not a proof or disproof of RH

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

Campaign 16 changes research mode.

The canonical target no longer moves:

```text
F-RH-010
PESC
```

The goal is to generate one concrete lemma which:

1. is not PESC merely renamed;
2. does not assume a fixed zero strip;
3. contains a genuine fixed-power source;
4. has a certified deterministic bridge back to PESC / PODEE.

The first candidate surviving those filters is a mesoscopic lag-energy estimate.

No live GLM-5.3-Flash run is claimed.

---

# 1. Work first with the von Mangoldt error

Define

$$
a_n
=
\Lambda(n)-1.
$$

Define

$$
A(x)
=
\sum_{n\le x}a_n
=
\psi(x)-x
$$

up to the harmless integer convention.

Paper 10 already established that for every fixed

$$
0<\kappa<\frac12,
$$

prime-power stripping transfers a dyadic fixed-power mean-square estimate between $\psi$ and $\vartheta$ at exponent level.

Therefore a first fixed-strip theorem may be proved on the $\Lambda$ / $\psi$ side.

---

# 2. Mesoscopic lag energy

For an integer lag

$$
1\le H<N,
$$

define

$$
\boxed{
\mathcal S_\Lambda(N,H)
=
\sum_{0\le x<2N-H}
\left|
A(x+H)-A(x)
\right|^2.
}
$$

Since

$$
A(x+H)-A(x)
=
\sum_{x<n\le x+H}
[
\Lambda(n)-1
],
$$

this is a global discrete Selberg-type increment energy at one fixed additive scale.

---

# 3. Deterministic residue-chain inequality

The key bridge does not use any arithmetic.

Let

$$
X\ge H\ge1
$$

be integers.

Let

$$
u_0,u_1,\ldots,u_X
$$

be any complex sequence.

For

$$
0\le n\le X-H,
$$

define

$$
d_H(n)
=
u_{n+H}-u_n.
$$

Let

$$
M
=
\left\lceil
\frac XH
\right\rceil.
$$

Then:

## Theorem 3.1 — Residue-Chain Energy Inequality

$$
\boxed{
\sum_{n=0}^{X}|u_n|^2
\le
2(M+1)
\sum_{r=0}^{H-1}|u_r|^2
+
2M(M+1)
\sum_{n=0}^{X-H}|d_H(n)|^2.
}
$$

### Proof

Fix one residue

$$
0\le r<H.
$$

Write every index in that residue class as

$$
r+kH.
$$

For each admissible $k$,

$$
u_{r+kH}
=
u_r
+
\sum_{j=0}^{k-1}
d_H(r+jH).
$$

Hence

$$
|u_{r+kH}|^2
\le
2|u_r|^2
+
2k
\sum_{j=0}^{k-1}
|d_H(r+jH)|^2.
$$

There are at most

$$
M+1
$$

indices in each residue class, and

$$
k\le M.
$$

Summing first in $k$ and then in $r$ gives the stated inequality.

 $\square$

---

# 4. Arithmetic specialization

Apply Theorem 3.1 with

$$
u_n=A(n)
$$

and

$$
X=2N.
$$

Chebyshev bounds give

$$
A(r)=O(r),
$$

hence

$$
\sum_{r<H}|A(r)|^2
\ll
H^3.
$$

Therefore:

## Corollary 4.1 — Lag-to-Global Energy Bridge

$$
\boxed{
\sum_{n\le2N}|A(n)|^2
\ll
\left(
\frac NH
\right)^2
\mathcal S_\Lambda(N,H)
+
NH^2.
}
$$

All logarithmic refinements of the initial term are irrelevant at fixed exponent level.

This is the certified bridge for Campaign 16.

---

# 5. Candidate theorem: Mesoscopic Lag-Energy Power Gain

Fix constants

$$
0<\alpha<\frac23
$$

and

$$
\delta>0.
$$

Set

$$
H=N^{\alpha+o(1)}.
$$

Define:

## MLEPG $(\alpha,\delta)$

$$
\boxed{
\mathcal S_\Lambda(N,H)
\ll
NH(\log N)^{O(1)}
+
NH^2N^{-\delta+o(1)}.
}
$$

The first term is the expected diagonal / prime-variance scale.

The second term permits a much larger remainder than the conjectural main scale when

$$
\delta<\alpha.
$$

Thus MLEPG does not require a full asymptotic formula for the Selberg integral.

It asks only for a fixed-power improvement over the completely unresolved scale

$$
NH^2.
$$

---

# 6. Fixed-power consequence

Insert MLEPG into Corollary 4.1.

We obtain

$$
\begin{aligned}
\sum_{n\le2N}|A(n)|^2
&\ll
\frac{N^2}{H^2}
\left[
NH(\log N)^{O(1)}
+
NH^2N^{-\delta+o(1)}
\right]
+
NH^2
\\
&\ll
N^{3-\alpha+o(1)}
+
N^{3-\delta+o(1)}
+
N^{1+2\alpha+o(1)}.
\end{aligned}
$$

For

$$
0<\alpha<\frac23,
$$

and sufficiently small fixed

$$
\kappa
<
\min
\{
\alpha,
\delta
\},
$$

the initial residue term is harmless.

Therefore:

## Theorem 6.1 — MLEPG Implies a Fixed PNT Mean-Square Power

If MLEPG $(\alpha,\delta)$ holds for fixed

$$
0<\alpha<\frac23,
\qquad
\delta>0,
$$

then

$$
\boxed{
\sum_{n\le2N}
|
\psi(n)-n
|^2
\ll
N^{3-\kappa+o(1)}
}
$$

for some fixed

$$
\kappa>0.
$$

One may take any sufficiently small

$$
\kappa
<
\min
\{
\alpha,
\delta,
2-2\alpha
\}.
$$

For

$$
\alpha<\frac23,
$$

the third quantity is not the active restriction when $\kappa$ is chosen small.

By the established CSM_RH bridges, this gives PODEE / PESC at a fixed exponent below the prime-power barrier, and hence a fixed zeta zero strip.

No such MLEPG theorem is proved here.

---

# 7. Why MLEPG is not PESC merely renamed

PESC controls the absolute cumulative error through

$$
\sum_n
w_N(n)
[
\Lambda(n)-1
]
[
\psi(n-1)-(n-1)
].
$$

MLEPG controls only one additive difference scale:

$$
A(x+H)-A(x).
$$

A sequence may have a large slowly varying low-frequency component while having much smaller increments at one scale.

Thus the two statements are not identical by definition.

The residue-chain theorem supplies the nontrivial deterministic bridge.

This is exactly the type of candidate Campaign 16 permits.

---

# 8. Correlation expansion of the lag energy

Let

$$
a_n=\Lambda(n)-1.
$$

Ignoring only endpoint truncation notation, the standard expansion is

$$
\boxed{
\mathcal S_\Lambda(N,H)
=
\sum_{|h|<H}
(H-|h|)
\sum_n
a_n
a_{n+h}
+
\text{boundary terms}.
}
$$

The kernel

$$
H-|h|
$$

is the discrete Fejér / triangular kernel.

Thus MLEPG is equivalent to obtaining a fixed-power saving in one signed triangular average of centered prime-pair correlations, together with standard diagonal and boundary estimates.

---

# 9. Hardy–Littlewood decomposition

For nonzero shifts define schematically

$$
\sum_{X<n\le2X}
\Lambda(n)\Lambda(n+h)
=
\mathfrak S(h)X
+
E_X(h).
$$

The triangular sum splits into:

1. the diagonal;
2. the singular-series deterministic average;
3. the weighted correlation-error aggregate.

The first two are not the new Campaign 16 obstruction.

The prime-pair singular series has the precise Cesàro expansion

$$
\sum_{h\le H}
(H-h)
\mathfrak S(h)
=
\frac12H^2
-
\frac12H\log H
+
O(H)
+
E_{\mathfrak S}(H),
$$

with a much sharper known unconditional estimate for the error than the $H^2$ scale.

Thus the fixed-power question localizes to the actual prime-pair correlation errors.

---

# 10. Current averaged Hardy–Littlewood input

Matomäki, Radziwiłł, and Tao prove that for

$$
H
\ge
X^{8/33+\varepsilon},
$$

the Hardy–Littlewood prime-pair asymptotic holds for all but a logarithmically small proportion of shifts, with individual good-shift error

$$
O
\left(
X\log^{-A}X
\right)
$$

for every fixed $A>0$.

The exceptional set also has arbitrary logarithmic density saving.

After crude control of exceptional shifts, this yields an $L^1$ error budget

$$
\boxed{
\sum_{|h|\le H}
|E_X(h)|
\ll
XH\log^{-A}X
}
$$

after changing $A$.

---

# 11. The triangular-kernel precision loss

MLEPG does not sum $E_X(h)$ with unit weights.

It carries the triangular weight

$$
H-|h|.
$$

Direct absolute transfer from the current averaged Hardy–Littlewood theorem gives only

$$
\boxed{
\sum_{|h|<H}
(H-|h|)
|E_X(h)|
\ll
XH^2
\log^{-A}X.
}
$$

This is the exact current precision floor.

After the residue-chain bridge,

$$
\left(
\frac NH
\right)^2
\cdot
NH^2
\log^{-A}N
=
N^3
\log^{-A}N.
$$

Hence current average-Hardy–Littlewood technology produces only subpower global energy through this route.

This matches the Campaign 15 classification.

---

# 12. The new fixed-power request is weaker than shiftwise power saving

A much stronger theorem would be:

$$
E_X(h)
\ll
X^{1-\delta}
$$

for every or almost every shift.

Campaign 16 does not ask for that.

It asks only for cancellation in the one aggregate

$$
\boxed{
\mathcal T(X,H)
=
\sum_{|h|<H}
(H-|h|)
E_X(h).
}
$$

A sufficient new estimate is

$$
\boxed{
|\mathcal T(X,H)|
\ll
XH^2X^{-\delta+o(1)}.
}
$$

Individual shifts may remain much larger.

Therefore the candidate theorem is genuinely a signed-average power theorem, not a uniform Hardy–Littlewood power theorem.

---

# 13. Candidate interface: Triangular Signed Hardy–Littlewood Power Gain

Create the proof-interface name:

```text
TSHLPG
TRIANGULAR_SIGNED_HARDY_LITTLEWOOD_POWER_GAIN
```

For

$$
H=X^{\alpha+o(1)},
$$

TSHLPG $(\alpha,\delta)$ is the assertion that the endpoint-compatible triangular aggregate of prime-pair errors satisfies

$$
\boxed{
\left|
\sum_{|h|<H}
(H-|h|)
E_X(h)
\right|
\ll
XH^2X^{-\delta+o(1)}.
}
$$

After standard diagonal, singular-series, and dyadic assembly, TSHLPG implies MLEPG.

TSHLPG is a proof interface.

MLEPG is the cleaner theorem candidate because it avoids dependence on a particular Hardy–Littlewood centering convention.

---

# 14. Natural first scale

The strongest classical long-shift theorem for $\Lambda\Lambda$ begins at

$$
\alpha
=
\frac8{33}
+
\varepsilon.
$$

Therefore the first natural candidate scale is

$$
\boxed{
H=N^{8/33+\varepsilon}.
}
$$

At this scale, any fixed

$$
\delta>0
$$

in MLEPG or TSHLPG would produce a fixed global power.

If

$$
\delta<\frac8{33},
$$

the resulting exponent gain is essentially

$$
\kappa<\delta.
$$

If

$$
\delta\ge\frac8{33},
$$

the lag length itself becomes the bottleneck and one obtains essentially

$$
\kappa<\frac8{33}.
$$

---

# 15. Candidate strength classification

MLEPG is breakthrough-strength.

It is not a low-strength theorem.

But it passes the Campaign 16 design filters:

```text
NOT merely a definition of PESC
  PASS

fixed exponent enters explicitly
  PASS

does not assume a fixed zero strip
  PASS

has a certified bridge to PESC
  PASS

current theorem comparison available
  PASS

current best gives only log-power analogue
  PASS
```

Status:

```text
SURVIVOR
```

---

# 16. Rejected candidate: shiftwise Hardy–Littlewood power saving

Candidate:

$$
E_X(h)
\ll
X^{1-\delta}
$$

for almost all shifts.

Status:

```text
REJECTED AS UNNECESSARILY STRONG
```

Reason:

TSHLPG needs only one signed triangular aggregate to save a power.

Demanding a power for individual shifts adds proof obligations not required by PESC.

---

# 17. Rejected candidate: Fejér-frequency power theorem as a new target

By Fourier expansion, the lag energy can be written with a Fejér kernel against a prime exponential-sum energy.

This is useful analytically.

But defining the Fourier form as another canonical frontier would only re-represent MLEPG.

Status:

```text
REJECTED AS REPRESENTATION ONLY
```

It may be used inside the proof.

---

# 18. Rejected candidate: another positive prime-pair variance

Replacing the signed triangular correlation error by

$$
\sum_h
|E_X(h)|^2
$$

creates a stronger positive gate.

Campaign 15 already classified such variance gates as stronger than the minimal signed target.

Status:

```text
REJECTED AS STRONGER POSITIVE SURROGATE
```

---

# 19. New canonical theorem candidate

Create:

```text
F-RH-016
MESOSCOPIC_LAG_ENERGY_POWER_GAIN
abbrev:
  MLEPG
status:
  OPEN
type:
  DIRECT THEOREM CANDIDATE
```

This is the first new frontier created after the representation-generation stop rule.

It is permitted because it is a concrete sufficient lemma with a proved deterministic bridge, not an equivalent restatement declared canonical for its own sake.

PESC remains the root target.

---

# 20. New obstruction: triangular kernel amplification

Create:

```text
O-RH-038
TRIANGULAR_KERNEL_LOG_TO_POWER_GAP
status:
  CERTIFIED
```

Statement:

> Almost-all per-shift Hardy–Littlewood errors of size $X\log^{-A}X$ become $XH^2\log^{-A}X$ after direct triangular weighting. The residue-chain bridge then returns only $N^3\log^{-A}N$. A fixed power must therefore arise from signed cancellation across shifts or from a stronger local theorem.

---

# 21. New survivor

Create:

```text
S-RH-025
TRIANGULAR_SIGNED_PRIME_PAIR_ERROR_CANCELLATION
status:
  OPEN
```

This is the principal proof mechanism for MLEPG.

It asks for power cancellation across shifts before absolute values are taken.

---

# 22. Campaign 16 verdict

Campaign 16 generated several candidates.

The result is:

```text
SHIFTWISE POWER HL
  too strong

FOURIER / FEJER REFORMULATION
  representation only

POSITIVE PRIME-PAIR VARIANCE
  stronger surrogate

MESOSCOPIC LAG-ENERGY POWER GAIN
  survives

TRIANGULAR SIGNED ERROR CANCELLATION
  first concrete attack mechanism
```

No fixed-power theorem is proved.

---

# 23. Campaign 17

The next campaign is:

```text
CSM_RH Campaign 17
TRIANGULAR_SIGNED_ERROR_POWER_ATTACK
```

The canonical root target remains PESC.

The working theorem candidate is MLEPG.

The proof interface is TSHLPG.

---

# 24. Campaign 17 attack directions

## T1 — Circle-method cancellation across shifts

Do not estimate each shift independently.

Insert the triangular kernel before major/minor arc separation and test whether the Fejér localization creates a fixed-power minor-arc gain unavailable shiftwise.

## T2 — Correlated exceptional-set cancellation

Current MRT exceptional shifts are controlled absolutely.

Test whether their signed triangular contribution has stronger cancellation than their cardinality bound.

## T3 — Major-arc residual cancellation

The singular-series main term is already understood.

Audit whether the residual major-arc errors possess cancellation across $h$ after the triangular kernel is inserted.

## T4 — Multiplicative-frequency averaging

MRT convert additive-frequency local energy into Dirichlet-polynomial mean values.

Test whether keeping the complete triangular shift average before Cauchy–Schwarz exposes an additional mean-value gain.

## T5 — Hybrid short-interval theorem

Seek MLEPG directly as a Selberg-increment energy theorem without resolving individual pair correlations.

---

# 25. Campaign 17 rejection filters

Reject a candidate if:

## R1. It takes absolute values in $h$ before the proposed new cancellation.

## R2. It simply assumes power-saving Hardy–Littlewood for almost every shift.

## R3. It uses PODEE/PESC as an input to estimate the lag energy.

## R4. It replaces $N^{-\delta}$ by $\log^{-A}N$.

## R5. It counts the singular-series Cesàro expansion as the missing theorem.

## R6. It hides a fixed zero-free half-plane inside an exponential-sum input.

---

# 26. External calibration

Current literature gives the correct location of the new gap.

1. Matomäki–Radziwiłł–Tao prove averaged Hardy–Littlewood for $\Lambda(n)\Lambda(n+h)$ in shift windows of length at least $X^{8/33+\varepsilon}$, with arbitrary logarithmic savings over the trivial error for almost all shifts.

2. Their proof obtains only logarithmic savings in the relevant prime-correlation minor-arc estimates; power savings are available or expected in some divisor-function cases but not supplied for the von Mangoldt pair correlation.

3. The prime-pair singular-series Cesàro mean has the expansion

$$
\frac12H^2
-
\frac12H\log H
+
O(H)
+
E(H),
$$

and Vaughan's unconditional estimate places $E(H)$ far below the $H^2$ scale.

4. Selberg-integral theory identifies the same triangular correlation kernel as the natural variance of primes in short intervals.

Thus the missing fixed power is localized to the actual prime-correlation residual, not to deterministic singular-series averaging.

---

# 27. State transition

The canonical transition is:

```text
CSM_RH v1.7
  ->
CSM_RH v1.8
```

with:

```text
Campaign 16
  CLOSED_AS_FIRST_DIRECT_THEOREM_GENERATION_ROUND

F-RH-010
  PESC
  REMAINS ROOT TARGET / OPEN

F-RH-016
  MLEPG
  CREATED / OPEN / DIRECT THEOREM CANDIDATE

O-RH-038
  TRIANGULAR_KERNEL_LOG_TO_POWER_GAP
  CREATED / CERTIFIED

S-RH-025
  TRIANGULAR_SIGNED_PRIME_PAIR_ERROR_CANCELLATION
  CREATED / OPEN

Campaign 17
  TRIANGULAR_SIGNED_ERROR_POWER_ATTACK
  READY
```

---

# 28. Final status

```text
RH = OPEN

PESC = OPEN / ROOT TARGET

REPRESENTATION GENERATION = STOPPED

FIRST DIRECT NEW LEMMA CANDIDATE = MLEPG

CURRENT AVERAGE HL ANALOGUE = LOG-POWER ONLY

FIXED-POWER SOURCE NEEDED = SIGNED TRIANGULAR ERROR CANCELLATION

MLEPG PROVED = NO

NEXT CAMPAIGN = 17
```

The concrete new theorem candidate is:

$$
\boxed{
\mathcal S_\Lambda(N,N^\alpha)
\ll
N^{1+\alpha+o(1)}
+
N^{1+2\alpha-\delta+o(1)}
}
$$

for some fixed

$$
0<\alpha<\frac23,
\qquad
\delta>0.
$$

A natural first scale is

$$
\alpha
=
\frac8{33}
+
\varepsilon.
$$

The deterministic residue-chain theorem then converts any such fixed $\delta$ into a fixed global prime-number-theorem mean-square power and hence back into the canonical PESC branch.
