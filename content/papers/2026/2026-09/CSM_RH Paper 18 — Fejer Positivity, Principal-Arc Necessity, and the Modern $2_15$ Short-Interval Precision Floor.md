# CSM_RH Paper 18
## Fejer Positivity, Principal-Arc Necessity, and the Modern $2/15$ Short-Interval Precision Floor

**Project:** `CSM_RH`  
**Paper:** `18`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v1.8 / Paper 17`  
**Campaign:** `17 — TRIANGULAR_SIGNED_ERROR_POWER_ATTACK`  
**Status:** mechanism correction / spectral bottleneck audit; not a proof or disproof of RH

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

Paper 17 introduced the direct theorem candidate MLEPG and suggested that a fixed power might arise from signed cancellation across the triangular shift kernel.

The present paper corrects that mechanism interpretation.

The exact triangular aggregate is a positive Fejer-weighted spectral energy.

Therefore the missing fixed power cannot be obtained merely by "preserving the signs of the shifts".

It requires genuine spectral deconcentration, including on the principal $q=1$ frequency arc.

No live GLM-5.3-Flash run is claimed.

---

# 1. Centered von Mangoldt sequence

Let

$$
a_n
=
\Lambda(n)-1.
$$

For a finite interval

$$
1\le n\le X,
$$

extend $a_n$ by zero outside this interval.

Define the exponential sum

$$
\boxed{
S_X(\alpha)
=
\sum_{1\le n\le X}
a_n e(n\alpha).
}
$$

For an integer lag

$$
1\le H<X,
$$

define the full zero-extended lag energy

$$
\boxed{
\widetilde{\mathcal S}_\Lambda(X,H)
=
\sum_{x\in\mathbb Z}
\left|
\sum_{x<n\le x+H}
a_n
\right|^2.
}
$$

Only finitely many $x$ contribute.

---

# 2. Exact Fejer identity

Define

$$
D_H(\alpha)
=
\sum_{r=1}^{H}
e(r\alpha).
$$

Then:

## Theorem 2.1 — Exact Fejer Lag-Energy Identity

$$
\boxed{
\widetilde{\mathcal S}_\Lambda(X,H)
=
\int_0^1
|S_X(\alpha)|^2
|D_H(\alpha)|^2
\,d\alpha.
}
$$

### Proof

Write

$$
\sum_{x<n\le x+H}a_n
=
\sum_{r=1}^{H}
a_{x+r}.
$$

The left side is the $\ell^2$ norm of the convolution of the finite sequence $a$ with the length- $H$ interval indicator.

Discrete Fourier Plancherel gives exactly the stated identity.

 $\square$

Thus the triangular correlation kernel is positive definite.

---

# 3. Triangular shift expansion

Expanding the square gives the equivalent form

$$
\boxed{
\widetilde{\mathcal S}_\Lambda(X,H)
=
\sum_{|h|<H}
(H-|h|)
\sum_n
a_n a_{n+h},
}
$$

with zero-extension understood.

The individual off-diagonal correlations may have either sign.

But their triangular signed sum is not an arbitrary signed quantity.

By Theorem 2.1 it is exactly a positive spectral energy.

This corrects the interpretation of the survivor introduced in Paper 17.

---

# 4. Fejer positivity obstruction

Create:

```text
O-RH-039
FEJER_POSITIVITY_NO_SHIFT_SIGN_BYPASS
status:
  CERTIFIED
```

Statement:

> The complete triangular shift aggregate in MLEPG is a positive Fejer-weighted Fourier energy. A proof cannot obtain the required fixed power merely by avoiding absolute values over shifts; it must prove genuine deconcentration of the centered prime exponential sum in the spectral regions emphasized by the Fejer kernel.

This does not prohibit using signed correlation identities inside a proof.

It prohibits treating "signed $h$ -cancellation" by itself as independent theorem authority.

---

# 5. Principal Fejer arc

The Dirichlet kernel satisfies

$$
|D_H(\alpha)|
=
\left|
\frac{
\sin(\pi H\alpha)
}{
\sin(\pi\alpha)
}
\right|.
$$

Fix any sufficiently small absolute constant

$$
0<c_0<\frac14.
$$

For

$$
\|\alpha\|
\le
\frac{c_0}{H},
$$

we have

$$
\boxed{
|D_H(\alpha)|^2
\gg
H^2.
}
$$

Therefore:

## Theorem 5.1 — Principal-Arc Necessary Bound

$$
\boxed{
H^2
\int_{\|\alpha\|\le c_0/H}
|S_X(\alpha)|^2
\,d\alpha
\ll
\widetilde{\mathcal S}_\Lambda(X,H).
}
$$

Consequently, any MLEPG bound

$$
\widetilde{\mathcal S}_\Lambda(X,H)
\ll
XH(\log X)^{O(1)}
+
XH^2X^{-\delta+o(1)}
$$

forces

$$
\boxed{
\int_{\|\alpha\|\le c_0/H}
|S_X(\alpha)|^2
\,d\alpha
\ll
\frac{X}{H}
(\log X)^{O(1)}
+
X^{1-\delta+o(1)}.
}
$$

The principal frequency arc is therefore an unavoidable fixed-power subproblem.

---

# 6. Principal $q=1$ spectral bottleneck

The interval

$$
\|\alpha\|
\le
c_0/H
$$

is the central additive frequency arc.

It is the $q=1$ major-arc component.

Create:

```text
O-RH-040
PRINCIPAL_FEJER_ARC_FIXED_POWER_NECESSITY
status:
  CERTIFIED
```

Statement:

> Any fixed-power MLEPG theorem at scale $H$ must improve the centered prime exponential-sum $L^2$ mass on the principal $q=1$ arc at the corresponding fixed-power scale.

Therefore a power saving on strongly minor arcs alone cannot close MLEPG.

This reproduces, in the direct lag-energy branch, the principal-component bottleneck seen repeatedly in earlier CSM_RH campaigns.

---

# 7. Why the MRT averaging step does not lose the shift signs

Matomäki–Radziwiłł–Tao use the Hardy–Littlewood circle method for

$$
\sum_n
\Lambda(n)\Lambda(n+h).
$$

After averaging in $h$ and applying Plancherel, their analysis is reduced to positive local Fourier-energy estimates of the schematic form

$$
\boxed{
\int_{\beta-1/H}^{\beta+1/H}
|S(\alpha)|^2
\,d\alpha
\ll_A
X\log^{-A}X
}
$$

for minor-arc centers $\beta$.

Thus the average-over-shifts stage already converts the correlation problem to a positive local $L^2$ problem.

There is no unused global sign cancellation in $h$ left at that stage.

The loss to logarithmic precision occurs in the strength of the available local spectral / Dirichlet-polynomial estimates, not because one first took absolute values of every shift correlation.

---

# 8. MRT strongly minor arcs

For strongly minor arcs, the MRT route converts the exponential-sum local energy into Dirichlet-polynomial mean values.

Their most delicate pieces are the Type $d_3$ and Type $d_4$ components arising after Heath-Brown decomposition.

The Type $d_3$ component uses:

```text
Jutila short-interval mean values;
Hölder-type decomposition;
return to physical space;
oscillatory sums;
Robert-Sargos estimates;
van der Corput processing.
```

This machinery is responsible for reaching the shift threshold

$$
H
\ge
X^{8/33+\varepsilon}.
$$

It supplies arbitrary logarithmic savings, not a fixed $X$ -power for the von Mangoldt pair correlation.

Improving this machinery could improve nonprincipal spectral control.

But Theorem 5.1 shows that it cannot by itself bypass the principal arc.

---

# 9. Updated short-interval scale: $2/15$

The natural first scale in Paper 17 was chosen from the 2019 average prime-pair threshold

$$
\frac8{33}.
$$

Current 2026 short-interval technology provides a smaller exponent for the prime number theorem in almost all short intervals.

The Guth–Maynard zero-density estimate implies the almost-all short-interval PNT for every fixed

$$
\boxed{
\alpha>\frac2{15}.
}
$$

The 2026 Matomäki–Radziwiłł–Shao–Tao–Teräväinen paper records the quantitative form:

for every fixed

$$
A>0
$$

and suitable $H$ in this regime, outside an exceptional set of measure

$$
O
\left(
X\log^{-A}X
\right),
$$

one has

$$
\boxed{
\left|
\sum_{x<n\le x+H}
[
\Lambda(n)-1
]
\right|
\le
H\log^{-A}X.
}
$$

Thus the current range obstruction is below the Paper 17 scale.

The precision obstruction remains.

---

# 10. Current short-interval mean-square consequence

Use the quantitative almost-all statement in Section 9.

On the good set,

$$
\left|
\sum_{x<n\le x+H}a_n
\right|^2
\le
H^2
\log^{-2A}X.
$$

On the exceptional set, Brun–Titchmarsh / trivial Chebyshev-type bounds give

$$
\left|
\sum_{x<n\le x+H}a_n
\right|
\ll
H(\log X)^{O(1)}
$$

in the polynomial short-interval regime.

Since $A$ is arbitrary, after increasing $A$ we obtain:

## Proposition 10.1 — Current Log-Power Lag-Energy Bound

For every fixed

$$
\alpha>\frac2{15}
$$

and every fixed

$$
B>0,
$$

with

$$
H=X^\alpha,
$$

current technology yields schematically

$$
\boxed{
\widetilde{\mathcal S}_\Lambda(X,H)
\ll_B
XH^2
\log^{-B}X
+
\text{standard boundary terms}.
}
$$

This is

$$
XH^2X^{-o(1)}.
$$

It is not a fixed-power improvement.

---

# 11. Modern precision floor

MLEPG needs, for some fixed

$$
\delta>0,
$$

a bound of the form

$$
\boxed{
\widetilde{\mathcal S}_\Lambda(X,H)
\ll
XH(\log X)^{O(1)}
+
XH^2X^{-\delta+o(1)}.
}
$$

Current short-interval technology supplies

$$
XH^2\log^{-B}X
$$

for arbitrary fixed $B$, but no fixed

$$
X^{-\delta}.
$$

Create:

```text
O-RH-041
MODERN_SHORT_INTERVAL_LOG_TO_POWER_PRECISION_FLOOR
status:
  CERTIFIED AS CURRENT-TECHNOLOGY AUDIT
```

The modern bottleneck is therefore not primarily the available exponent $\alpha$.

It is the distinction

$$
\boxed{
\log^{-B}X
\quad\text{versus}\quad
X^{-\delta}.
}
$$

---

# 12. Two-scale comparison

There are now two natural scales relevant to the direct theorem candidate.

## Prime-pair/circle-method scale

$$
\alpha
>
\frac8{33}.
$$

At this scale, averaged Hardy–Littlewood pair correlations are known for almost all shifts with arbitrary logarithmic savings.

## Almost-all short-interval PNT scale

$$
\alpha
>
\frac2{15}.
$$

At this smaller scale, the short-interval PNT is known for almost all intervals, again with subpower/logarithmic quantitative precision.

Neither route supplies a fixed lag-energy power.

The smaller scale improves the possible exponent cap in a future residue-chain theorem only if the fixed-power precision problem is also solved.

---

# 13. Exceptional-set power alone is insufficient

Suppose one proves that only

$$
X^{1-\eta}
$$

intervals are exceptional for a fixed relative-error threshold.

This does not by itself imply MLEPG.

The error on the nonexceptional intervals must also shrink with $X$ at fixed-power scale, or a direct $L^2$ argument must replace the pointwise good/bad decomposition.

Indeed, if on the good set one knows only

$$
|\Delta_HA(x)|
\le
\varepsilon H
$$

for fixed $\varepsilon>0$, then the good-set contribution remains

$$
\asymp
\varepsilon^2 XH^2,
$$

which has no fixed $X$ -power gain.

Thus modern exceptional-set improvements do not automatically solve the MLEPG precision problem.

---

# 14. Two-axis fixed-power criterion

A sufficient pointwise/exceptions formulation is the following.

Suppose for fixed

$$
\eta_1,\eta_2>0
$$

one has:

## Good intervals

Outside an exceptional set $\mathcal E$,

$$
\boxed{
|\Delta_HA(x)|
\ll
H X^{-\eta_1+o(1)}.
}
$$

## Exceptional set

$$
\boxed{
|\mathcal E|
\ll
X^{1-\eta_2+o(1)}.
}
$$

Then, using the trivial polynomial bound on exceptional intervals,

$$
\boxed{
\widetilde{\mathcal S}_\Lambda(X,H)
\ll
XH^2
X^{-\min(2\eta_1,\eta_2)+o(1)}.
}
$$

Thus a fixed-power lag-energy theorem needs fixed-power accuracy in an $L^2$ sense.

A power-saving exceptional-set exponent with only fixed relative accuracy is insufficient.

---

# 15. Strength calibration by a single off-axis zero

Let

$$
\rho
=
\beta+i\gamma
$$

be a fixed nontrivial zero.

For

$$
H=o(X)
$$

and eventually

$$
|\gamma|H/X\ll1,
$$

the explicit-formula contribution of this zero to the short-interval error has local amplitude of order

$$
H X^{\beta-1}
$$

up to oscillation and smoothing issues.

Its squared contribution over an $X$ -sized range is therefore of natural scale

$$
\boxed{
H^2X^{2\beta-1}.
}
$$

The MLEPG error budget

$$
XH^2X^{-\delta}
=
H^2X^{1-\delta}
$$

is incompatible at exponential scale with

$$
\beta
>
1-\frac{\delta}{2},
$$

once a coefficient-recovery / cancellation-isolation argument is supplied.

This agrees with the earlier fixed-strip strength audits.

This subsection is a strength calibration, not a new proof of zero isolation for the lag energy.

---

# 16. Status of triangular signed cancellation

Paper 17 created:

```text
S-RH-025
TRIANGULAR_SIGNED_PRIME_PAIR_ERROR_CANCELLATION
```

The current correction is:

```text
status:
  DEMOTED AS INDEPENDENT MECHANISM

reason:
  the complete triangular aggregate is a positive Fejer energy
```

Signed prime-pair identities may still be used internally.

But they must produce a positive spectral-energy improvement in the end.

---

# 17. Surviving mechanism: principal spectral deconcentration

Create:

```text
S-RH-026
PRINCIPAL_FEJER_ARC_POWER_DECONCENTRATION
status:
  OPEN
```

Prototype:

for

$$
H=X^\alpha
$$

and some fixed

$$
\delta>0,
$$

prove

$$
\boxed{
\int_{\|\alpha'\|\le c/H}
|S_X(\alpha')|^2
\,d\alpha'
\ll
\frac{X}{H}
(\log X)^{O(1)}
+
X^{1-\delta+o(1)}.
}
$$

This is a proof-mechanism sublemma.

It is not promoted as a new root frontier.

MLEPG remains the direct theorem candidate and PESC remains the root target.

---

# 18. Campaign 17 verdict

```text
SHIFT-SIGN BYPASS
  REJECTED

FEJER POSITIVITY
  CERTIFIED

MRT AVERAGING STEP
  ALREADY POSITIVE-L2

STRONGLY MINOR ARC IMPROVEMENT
  POSSIBLE TOOL / NOT SUFFICIENT ALONE

PRINCIPAL q=1 ARC
  NECESSARY FIXED-POWER SUBPROBLEM

CURRENT ALMOST-ALL SHORT-INTERVAL RANGE
  alpha > 2/15

CURRENT QUANTITATIVE PRECISION
  arbitrary log-power

FIXED X-POWER
  NOT OBTAINED

MLEPG
  REMAINS OPEN
```

---

# 19. Campaign 18

The next campaign is:

```text
CSM_RH Campaign 18
PRINCIPAL_FEJER_ARC_POWER_ATTACK
```

It remains theorem-generation work.

The root target does not change.

The campaign asks whether any current zero-density, large-value, Dirichlet-polynomial, or explicit-formula technique can prove a fixed-power principal-arc estimate without assuming a fixed zero strip.

---

# 20. Campaign 18 tracks

## P1 — Guth–Maynard large-value upgrade

Insert the 2026 large-value estimates into a quantitative $L^2$ short-interval calculation rather than merely a density-zero exceptional-set statement.

Test the strongest exponent actually obtainable.

## P2 — Gafni–Tao exceptional-set optimization

Use the quantitative zero-density-to-exceptional-set machine with a shrinking error threshold.

Determine whether the optimization remains subpower or could produce a fixed $X$ -power in $L^2$.

## P3 — Principal Dirichlet-polynomial mean square

Work directly with the $q=1$ local Fourier mass and Mellin/Dirichlet-polynomial transforms.

Identify the first large-value estimate which would have to improve by a fixed power.

## P4 — Explicit-formula zero packet

Smooth the lag energy and compute the contribution of one fixed off-axis zero.

Use this only as a strength/countermodel audit unless a genuine coefficient-isolation argument is proved.

---

# 21. Campaign 18 rejection filters

Reject a candidate if:

## R1. It improves only strongly minor arcs.

## R2. It obtains only logarithmic or stretched-logarithmic savings.

## R3. It assumes a fixed zero-free half-plane.

## R4. It invokes exceptional-set density without also controlling the shrinking good-interval error in $L^2$.

## R5. It treats the Fejer-weighted energy as a signed object after Theorem 2.1.

## R6. It claims that lowering the short-interval exponent alone creates a fixed-power gain.

---

# 22. External calibration

Current literature relevant to this campaign includes:

1. Matomäki–Radziwiłł–Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. Lond. Math. Soc. 118 (2019). Their shift averaging plus Plancherel reduces the minor-arc problem to positive local Fourier $L^2$ estimates; the Type $d_3$ and Type $d_4$ Dirichlet-polynomial analysis yields arbitrary logarithmic savings and the $8/33$ threshold.

2. Guth–Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics 203 (2026), 623–675. They prove
$$
N(\sigma,T)
\le
T^{30(1-\sigma)/13+o(1)}
$$
and derive improved prime-distribution consequences.

3. Matomäki–Radziwiłł–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae 244 (2026), 967–1091. They record the quantitative almost-all short-interval PNT with arbitrary logarithmic accuracy; the exponent $1/6$ is improved to $2/15$ using Guth–Maynard.

4. Gafni–Tao, *On the number of exceptional intervals to the prime number theorem in short intervals*, Essential Number Theory 5 (2026), 221–241. They quantify the translation from zero-density estimates to exceptional-set bounds.

None of these results currently supplies the fixed $X$ -power MLEPG requires.

---

# 23. State transition

The canonical transition is:

```text
CSM_RH v1.8
  ->
CSM_RH v1.9
```

with:

```text
Campaign 17
  CLOSED_AS_FEJER_POSITIVITY_AND_PRECISION_AUDIT

O-RH-039
  FEJER_POSITIVITY_NO_SHIFT_SIGN_BYPASS
  CREATED / CERTIFIED

O-RH-040
  PRINCIPAL_FEJER_ARC_FIXED_POWER_NECESSITY
  CREATED / CERTIFIED

O-RH-041
  MODERN_SHORT_INTERVAL_LOG_TO_POWER_PRECISION_FLOOR
  CREATED / CERTIFIED AS CURRENT-TECHNOLOGY AUDIT

S-RH-025
  TRIANGULAR_SIGNED_PRIME_PAIR_ERROR_CANCELLATION
  DEMOTED AS INDEPENDENT MECHANISM

S-RH-026
  PRINCIPAL_FEJER_ARC_POWER_DECONCENTRATION
  CREATED / OPEN

F-RH-016
  MLEPG
  REMAINS OPEN / DIRECT THEOREM CANDIDATE

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 18
  PRINCIPAL_FEJER_ARC_POWER_ATTACK
  READY
```

---

# 24. Final status

```text
RH = OPEN

PESC = OPEN / ROOT TARGET

MLEPG = OPEN / DIRECT THEOREM CANDIDATE

TRIANGULAR SHIFT-SIGN BYPASS = CLOSED

FEJER ENERGY = POSITIVE

PRINCIPAL q=1 ARC = NECESSARY

CURRENT SHORT-INTERVAL RANGE = alpha > 2/15

CURRENT PRECISION = LOG-POWER / SUBPOWER

FIXED X-POWER = OPEN

NEXT CAMPAIGN = 18
```

The central unresolved mechanism has become:

$$
\boxed{
\text{fixed-power deconcentration of centered prime spectral mass on the principal Fejer arc}.
}
$$

Improving shift range or strongly minor-arc technology alone is not enough.
