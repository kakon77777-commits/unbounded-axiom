# CSM_RH Paper 55

## Fixed-Exponent PESC–Zero-Strip Equivalence, Boundary-Zero Principal-Arc Locking, and the No-Free-Delocking Theorem

**Project:** CSM_RH  
**Paper:** 55  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 45 — `PESC_EXPONENT_AMPLIFICATION_OR_MLEPG_BOOTSTRAP`  
**Tracks:** EA3 / EA4 structural closure  
**Status:** AMPLIFIER STRUCTURE COMPLETE / PRIME-SIDE ARITHMETIC GAP THEOREM OPEN  
**Canonical entry state:** v1.45 / Paper 54 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 54 proved the seeded MLEPG amplification law

$$
\kappa'
<
\min
\left\{
\alpha,
\delta,
2-\alpha(2-\kappa)
\right\}
$$

and showed that strict amplification requires

$$
\alpha>\kappa,
\qquad
\delta>\kappa.
$$

The present paper identifies exactly what such an amplification means in the zeta zero geometry and proves that principal-arc delocking cannot be obtained for free by projection or multiscale bookkeeping.

For every fixed

$$
0<\kappa\le1,
$$

PESC $(\kappa)$ is shown to be exponent-equivalent to the fixed zero-free half-plane

$$
\boxed{
\sup_{\zeta(\rho)=0}
\Re\rho
\le
1-\frac{\kappa}{2}.
}
$$

The implication from PESC to the zero-free half-plane was obtained in Paper 53 by Mellin analyticity. The converse follows from the truncated explicit formula: if every nontrivial zero satisfies

$$
\beta\le1-\frac{\kappa}{2},
$$

then

$$
\psi(x)-x
\ll
x^{1-\kappa/2}\log^2x,
$$

and hence

$$
J_N^\vartheta
\ll
N^{3-\kappa}\log^4N.
$$

Define

$$
\beta_*
=
\sup_{\zeta(\rho)=0}\Re\rho
$$

and

$$
\kappa_*
=
\sup
\left\{
\kappa\in[0,1]:
\operatorname{PESC}(\kappa)
\text{ holds}
\right\}.
$$

Then

$$
\boxed{
\kappa_*
=
2(1-\beta_*).
}
$$

Thus the maximal PESC exponent is exactly twice the global zero-free gap from $\Re s=1$.

The paper then analyzes the explicit-formula power mode

$$
F_\rho(x)
=
-\frac{x^\rho}{\rho}.
$$

For a fixed zero ordinate and any sublinear lag

$$
H=N^\alpha,
\qquad
0<\alpha<1,
$$

the lag energy satisfies

$$
\mathcal S_\rho(N,H)
\asymp_\rho
H^2N^{2\beta-1}.
$$

If

$$
\beta
=
1-\frac{\kappa}{2},
$$

this becomes

$$
\boxed{
\mathcal S_\rho(N,H)
\asymp_\rho
NH^2N^{-\kappa}.
}
$$

Thus a zero on the seed strip boundary is exactly a critical-locking mode with lag exponent $\delta=\kappa$.

Moreover, the discrete derivative of this mode is spectrally concentrated on the principal Fejer arc. If

$$
b_{\rho,n}
=
F_\rho(n)-F_\rho(n-1)
$$

on $N<n\le2N$, then for fixed $c>0$,

$$
\int_{\|\xi\|>c/H}
\left|
\sum_{N<n\le2N}
b_{\rho,n}e(n\xi)
\right|^2d\xi
\ll_{\rho,c}
\frac{H}{N}
\sum_{N<n\le2N}|b_{\rho,n}|^2.
$$

Hence $1-O(H/N)$ of the derivative energy lies inside the principal arc, and the Fejer-weighted principal component has order

$$
H^2N^{2\beta-1}.
$$

The adjacent-block defect of the same zero mode is only

$$
O_\rho((H/N)^2)
$$

relative to its lag energy. Therefore its cumulative dyadic contraction mass up to any terminal scale $N^\alpha$, $\alpha<1$, is $o(1)$.

These facts yield two no-bypass results.

First, subtracting or projecting away a principal low-frequency component cannot prove MLEPG for the original prime sequence unless the removed component is independently bounded with exponent strictly larger than $\kappa$. For a boundary zero mode, the removed component already has the critical size $NH^2N^{-\kappa}$.

Second, any valid seeded MLEPG theorem with $\alpha>\kappa$ and $\delta>\kappa$ necessarily proves a strictly narrower zero-free strip. It is therefore not a weaker deterministic consequence of PESC $(\kappa)$ ; it is itself new strip-gap arithmetic.

Campaign 45 is consequently structurally complete. The remaining task is theorem generation: produce a genuinely arithmetic prime-side estimate that creates a fixed gap beyond the seed strip boundary.

No RH theorem is claimed.

---

# 1. PESC and the rightmost zeta zero

Let

$$
E_\psi(x)
=
\psi(x)-x.
$$

Paper 53 proved that for every fixed

$$
0<\kappa\le1,
$$

PESC $(\kappa)$ implies

$$
\boxed{
\zeta(s)\ne0
\qquad
\Re s>
1-\frac{\kappa}{2}.
}
$$

Equivalently,

$$
\boxed{
\operatorname{PESC}(\kappa)
\Longrightarrow
\beta_*
\le
1-\frac{\kappa}{2}.
}
$$

We now prove the converse at the same exponent resolution.

---

# 2. Fixed zero-free half-plane implies the corresponding PNT power

Assume

$$
\boxed{
\beta_*
\le
\sigma_0
<
1.
}
$$

Use the standard truncated explicit formula for the symmetrized Chebyshev function:

$$
\psi_0(x)
=
x
-
\sum_{|\gamma|\le T}
\frac{x^\rho}{\rho}
+
O
\left(
\frac{x\log^2(xT)}{T}
+
\log x
\right).
$$

At a prime-power discontinuity,

$$
\psi(x)-\psi_0(x)
=
O(\log x),
$$

which is negligible below.

Take

$$
T=x^2.
$$

The Riemann-von Mangoldt zero count implies

$$
\sum_{0<|\gamma|\le T}
\frac1{|\rho|}
\ll
\log^2(T+2).
$$

Since

$$
|x^\rho|
\le
x^{\sigma_0},
$$

we obtain

$$
\boxed{
\psi(x)-x
\ll
x^{\sigma_0}\log^2x.
}
$$

Therefore

$$
\int_N^{2N}
|\psi(x)-x|^2dx
\ll
N^{2\sigma_0+1}\log^4N.
$$

If

$$
\sigma_0
=
1-\frac{\kappa}{2},
$$

then

$$
2\sigma_0+1
=
3-\kappa.
$$

Using Paper 53's prime-power and discrete-continuous transfer:

## Theorem 2.1 — Fixed-exponent PESC / zero-strip equivalence

For every fixed

$$
0<\kappa\le1,
$$

$$
\boxed{
\operatorname{PESC}(\kappa)
\Longleftrightarrow
\beta_*
\le
1-\frac{\kappa}{2}.
}
$$

Equivalently,

$$
\operatorname{PESC}(\kappa)
$$

holds if and only if all nontrivial zeta zeros lie in

$$
\frac{\kappa}{2}
\le
\Re\rho
\le
1-\frac{\kappa}{2},
$$

using functional-equation symmetry.

Create:

```text
B-RH-055
FIXED_EXPONENT_PESC_ZERO_FREE_STRIP_EQUIVALENCE
CERTIFIED
```

This extends the endpoint equivalence in Paper 53 to every fixed exponent.

---

# 3. Exact maximal-exponent law

Define

$$
\boxed{
\beta_*
=
\sup_{\zeta(\rho)=0}
\Re\rho.
}
$$

By critical-line symmetry,

$$
\frac12
\le
\beta_*
\le
1.
$$

Define

$$
\boxed{
\kappa_*
=
\sup
\left\{
\kappa\in[0,1]:
\operatorname{PESC}(\kappa)
\text{ holds}
\right\}.
}
$$

Theorem 2.1 immediately gives:

## Theorem 3.1 — PESC spectral exponent law

$$
\boxed{
\kappa_*
=
2(1-\beta_*).
}
$$

Create:

```text
B-RH-056
PESC_MAXIMAL_EXPONENT_EQUALS_TWICE_GLOBAL_ZETA_ZERO_FREE_GAP
CERTIFIED
```

Interpretation:

```text
beta_* = 1
  <-> no fixed positive PESC exponent

1/2 < beta_* < 1
  <-> a maximal subendpoint PESC exponent exists

beta_* = 1/2
  <-> kappa_* = 1
  <-> RH
```

Thus exponent amplification and zero-strip narrowing are the same global resource measured in different coordinates.

---

# 4. Explicit-formula zero mode

Fix

$$
\rho=\beta+i\gamma
$$

with

$$
0<\beta<1.
$$

Define the natural explicit-formula mode

$$
\boxed{
F_\rho(x)
=
-\frac{x^\rho}{\rho}.
}
$$

Then

$$
F_\rho'(x)
=
-x^{\rho-1}.
$$

For a lag

$$
1\le H=o(N),
$$

define

$$
U_{\rho,H}(x)
=
F_\rho(x+H)-F_\rho(x).
$$

Taylor expansion, uniformly for

$$
N\le x\le2N,
$$

gives

$$
\boxed{
U_{\rho,H}(x)
=
-Hx^{\rho-1}
\left[
1+O_\rho(H/N)
\right].
}
$$

Hence:

## Theorem 4.1 — Zero-mode lag-energy law

For fixed $\rho$ and $H=o(N)$,

$$
\boxed{
\int_N^{2N}
|U_{\rho,H}(x)|^2dx
\asymp_\rho
H^2N^{2\beta-1}.
}
$$

If

$$
\beta
=
1-\frac{\kappa}{2},
$$

then

$$
\boxed{
\int_N^{2N}
|U_{\rho,H}(x)|^2dx
\asymp_\rho
NH^2N^{-\kappa}.
}
$$

Thus a zero on the PESC $(\kappa)$ boundary has exactly the critical lag exponent

$$
\boxed{
\delta_{\rm zero}=\kappa.
}
$$

This is the zeta-zero version of Paper 54's abstract power-law locking countermodel.

---

# 5. Discrete derivative of a zero mode

On the dyadic integer interval define

$$
\boxed{
b_{\rho,n}
=
F_\rho(n)-F_\rho(n-1),
\qquad
N<n\le2N.
}
$$

For fixed $\rho$,

$$
b_{\rho,n}
=
-n^{\rho-1}
\left[
1+O_\rho(1/N)
\right].
$$

Therefore, for

$$
\beta>\frac12,
$$

$$
\boxed{
\sum_{N<n\le2N}
|b_{\rho,n}|^2
\asymp_\rho
N^{2\beta-1}.
}
$$

At $\beta=1/2$ the same sum is $\asymp_\rho1$, which is the limiting logarithmic case.

Define the additive Fourier transform

$$
\boxed{
B_{\rho,N}(\xi)
=
\sum_{N<n\le2N}
b_{\rho,n}e(n\xi).
}
$$

Parseval gives

$$
\int_0^1
|B_{\rho,N}(\xi)|^2d\xi
=
\sum_{N<n\le2N}|b_{\rho,n}|^2.
$$

---

# 6. Principal-arc concentration of a fixed zero mode

For

$$
\|\xi\|>0,
$$

summation by parts and the geometric-sum estimate give

$$
\left|
B_{\rho,N}(\xi)
\right|
\ll_\rho
\frac{
N^{\beta-1}
}{
\|\xi\|
}.
$$

Indeed:

- the endpoint size of $b_{\rho,n}$ is $O_\rho(N^{\beta-1})$ ;
- the total variation of $b_{\rho,n}$ over the dyadic block is $O_\rho(N^{\beta-1})$ ;
- partial sums of $e(n\xi)$ are $O(\|\xi\|^{-1})$.

Let

$$
H=N^\alpha,
\qquad
0<\alpha<1,
$$

and fix an absolute $c>0$.

Then

$$
\begin{aligned}
\int_{\|\xi\|>c/H}
|B_{\rho,N}(\xi)|^2d\xi
&\ll_{\rho,c}
N^{2\beta-2}
\int_{c/H}^{1/2}
\frac{d\xi}{\xi^2}
\\
&\ll_{\rho,c}
HN^{2\beta-2}.
\end{aligned}
$$

Comparing with total Parseval mass:

## Theorem 6.1 — Fixed-zero principal-arc concentration

For fixed $\rho$ with $\beta>1/2$,

$$
\boxed{
\frac{
\displaystyle
\int_{\|\xi\|>c/H}
|B_{\rho,N}(\xi)|^2d\xi
}{
\displaystyle
\int_0^1
|B_{\rho,N}(\xi)|^2d\xi
}
\ll_{\rho,c}
\frac{H}{N}.
}
$$

Hence, because $H=o(N)$,

$$
\boxed{
\int_{\|\xi\|\le c/H}
|B_{\rho,N}(\xi)|^2d\xi
=
\left[
1-o(1)
\right]
\int_0^1
|B_{\rho,N}(\xi)|^2d\xi.
}
$$

A fixed zero mode is therefore asymptotically a principal-additive-frequency mode at every sublinear lag scale.

Create:

```text
B-RH-057
FIXED_ZETA_ZERO_MODE_CONCENTRATES_ON_PRINCIPAL_FEJER_ARC
CERTIFIED_AS_MODEL_THEOREM
```

---

# 7. Principal Fejer energy of the zero mode

Let

$$
D_H(\xi)
=
\sum_{r=1}^{H}e(r\xi).
$$

For sufficiently small fixed $c_0>0$,

$$
|D_H(\xi)|^2
\gg
H^2
$$

on

$$
\|\xi\|\le c_0/H.
$$

Theorem 6.1 therefore gives

$$
\boxed{
\int_{\|\xi\|\le c_0/H}
|B_{\rho,N}(\xi)|^2
|D_H(\xi)|^2d\xi
\asymp_\rho
H^2N^{2\beta-1}
}
$$

at exponent scale.

If

$$
\beta=1-\frac{\kappa}{2},
$$

then

$$
\boxed{
\text{principal Fejer zero-mode energy}
\asymp
NH^2N^{-\kappa}.
}
$$

Thus the critical-locking mode identified in Paper 54 is not merely a physical-space smooth drift. It is precisely concentrated in the principal $q=1$ Fejer arc isolated in Paper 18.

---

# 8. Adjacent-scale defect of the zero mode

Differentiate again:

$$
F_\rho''(x)
=
-(\rho-1)x^{\rho-2}.
$$

Using Taylor expansion,

$$
U_{\rho,H}(x+H)-U_{\rho,H}(x)
=
-(\rho-1)
H^2x^{\rho-2}
\left[
1+O_\rho(H/N)
\right].
$$

Therefore

$$
\boxed{
\int_N^{2N}
|U_{\rho,H}(x+H)-U_{\rho,H}(x)|^2dx
\asymp_\rho
H^4N^{2\beta-3}.
}
$$

Dividing by the lag energy from Theorem 4.1:

$$
\boxed{
\frac{
\mathcal D_\rho(N,H)
}{
\mathcal S_\rho(N,H)
}
\asymp_\rho
\left(
\frac{H}{N}
\right)^2.
}
$$

Hence the local normalized contraction coefficient satisfies

$$
\boxed{
q_\rho(H)
=
1-
O_\rho
\left(
\frac{H^2}{N^2}
\right).
}
$$

For a dyadic chain

$$
H_j=2^jH_0
$$

with terminal scale

$$
H_J\le N^\alpha,
\qquad
\alpha<1,
$$

the cumulative contraction mass obeys

$$
\begin{aligned}
G_\rho(J)
&=
\sum_{j<J}
-\log q_\rho(H_j)
\\
&\ll_\rho
\sum_{j<J}
\frac{H_j^2}{N^2}
\\
&\ll
\frac{H_J^2}{N^2}
\\
&\ll
N^{2\alpha-2}.
\end{aligned}
$$

Thus:

## Theorem 8.1 — Boundary-zero multiscale locking

For every fixed zero mode and every sublinear terminal scale,

$$
\boxed{
G_\rho(J)=o(1).
}
$$

A boundary zero mode contributes no linear contraction mass.

Create:

```text
O-RH-133
BOUNDARY_ZERO_MODE_IS_ASYMPTOTICALLY_MAXIMALLY_LOCKED_ACROSS_SUBLINEAR_DYADIC_LAGS
CERTIFIED_AS_MODEL_BARRIER
```

---

# 9. Seed PESC gives no principal-arc margin

Paper 54 showed that PESC $(\kappa)$ alone gives only

$$
\mathcal S_\Lambda(N,H)
\ll
N^{3-\kappa+o(1)}.
$$

At

$$
H=N^\alpha,
$$

this corresponds to the MLEPG remainder exponent

$$
\delta_{\rm det}
=
\kappa+2\alpha-2.
$$

For every

$$
\alpha<1,
$$

$$
\delta_{\rm det}<\kappa.
$$

The boundary-zero model shows a sharper reason why no deterministic principal-arc argument can cross the gap.

A legal PESC $(\kappa)$ spectral mode can sit almost entirely on the principal Fejer arc and have exact lag exponent $\delta=\kappa$.

Therefore the missing inequality is not a Fourier-coordinate artifact.

It is a statement excluding the boundary mode itself.

---

# 10. No-free-projection theorem

Suppose a proof introduces a decomposition

$$
b
=
P_Hb
+
(I-P_H)b,
$$

where $P_H$ is a principal-arc, low-frequency, finite-rank, or smooth-drift projector.

Assume the residual component is shown to satisfy a strict amplifier bound.

This does not control the original lag energy unless the projected component is also bounded.

For the boundary-zero model of Sections 4–7,

$$
P_Hb_\rho
$$

contains

$$
1-o(1)
$$

of the derivative $L^2$ mass for every projector which captures the principal arc at width $\asymp H^{-1}$.

Its Fejer lag energy remains

$$
\asymp
NH^2N^{-\kappa}.
$$

Therefore any projected proof aiming at

$$
NH^2N^{-\delta},
\qquad
\delta>\kappa,
$$

must independently prove an additional suppression

$$
\boxed{
\|P_Hb\|_{\rm Fejer}^2
\ll
NH^2N^{-\kappa-\eta}
}
$$

for some fixed

$$
\eta>0.
$$

That suppression is exactly the missing strip-gap arithmetic.

Create:

```text
O-RH-134
PRINCIPAL_ARC_PROJECTION_CANNOT_BYPASS_BOUNDARY_MODE_WITHOUT_INDEPENDENT_POWER_SUPPRESSION
CERTIFIED
```

This rejects the idea that one may simply subtract the critical power-law mode and prove decorrelation of the residual.

The coefficient of the removed mode is the hard object.

---

# 11. Strict MLEPG amplification is a zero-strip improvement theorem

Assume PESC $(\kappa)$.

Suppose MLEPG $(\alpha,\delta)$ holds with

$$
\alpha>\kappa,
\qquad
\delta>\kappa.
$$

Paper 54 gives PESC $(\kappa')$ for some fixed

$$
\kappa'>\kappa.
$$

Theorem 2.1 then gives

$$
\boxed{
\beta_*
\le
1-\frac{\kappa'}{2}
<
1-\frac{\kappa}{2}.
}
$$

Therefore:

## Theorem 11.1 — Seeded amplifier / strip-gap theorem

Every strict seeded MLEPG amplifier theorem is automatically a theorem creating a fixed new zero-free gap beyond the seed boundary.

Equivalently, if

$$
\beta_*
=
1-\frac{\kappa}{2},
$$

then no MLEPG theorem in the strict-amplifier regime

$$
\alpha>\kappa,
\qquad
\delta>\kappa
$$

can hold.

Create:

```text
B-RH-058
STRICT_SEEDED_MLEPG_AMPLIFICATION_IMPLIES_STRICT_ZERO_STRIP_NARROWING
CERTIFIED
```

This does not make MLEPG circular.

It calibrates its exact arithmetic strength.

---

# 12. Conversely, a strip improvement already gives the amplified PESC exponent

Suppose one proves directly that

$$
\boxed{
\beta_*
\le
1-\frac{\kappa'}{2}
}
$$

for some

$$
\kappa'>\kappa.
$$

Theorem 2.1 immediately gives PESC $(\kappa')$.

Thus, at the root exponent level:

$$
\boxed{
\text{strict PESC amplification}
\Longleftrightarrow
\text{strict fixed zero-strip improvement}.
}
$$

MLEPG is one possible prime-side mechanism for proving such an improvement.

It is not an intermediate theorem of lower zero-strip strength.

---

# 13. EA3 verdict

Campaign 45 / EA3 asked whether a seeded PESC theorem could delock the principal Fejer arc.

The structural answer is now complete.

```text
SEED PESC(kappa)
  permits a boundary mode

boundary mode
  is concentrated on principal Fejer arc

boundary mode
  has lag exponent delta = kappa

boundary mode
  has o(1) dyadic contraction mass

projection removal
  merely transfers the burden to coefficient suppression

strict delocking delta > kappa
  creates a genuinely narrower zero strip
```

Therefore close the structural audit as:

```text
EA3S
CLOSED_AS_PRINCIPAL_ARC_DELOCKING_REQUIRES_NEW_FIXED_STRIP_GAP_ARITHMETIC
```

The arithmetic theorem itself remains open:

```text
EA3A
OPEN_PRIME_SIDE_PRINCIPAL_ARC_POWER_SUPPRESSION_BEYOND_SEED_BOUNDARY
```

---

# 14. EA4 verdict

Paper 54 identified the contraction-mass amplifier condition

$$
G_N(J)
>
\kappa\log N
+
o(\log N).
$$

Theorem 8.1 shows that the boundary zero model has

$$
G_\rho(J)=o(1)
$$

through every sublinear lag chain.

Therefore no deterministic multiscale geometry can create the required mass from PESC $(\kappa)$ alone.

A successful EA4 theorem must again exclude or suppress the boundary mode.

Close the structural audit as:

```text
EA4S
CLOSED_AS_LINEAR_CONTRACTION_MASS_REQUIRES_ARITHMETIC_BOUNDARY_MODE_SUPPRESSION
```

Keep open:

```text
EA4A
OPEN_PRIME_SIDE_LINEAR_CONTRACTION_MASS_BEYOND_CRITICAL_LOCKING
```

---

# 15. Campaign 45 structural closure

Campaign 45 has now certified:

1. the seeded amplification law;
2. the optimal ideal exponent map;
3. the exact PESC / zero-strip exponent equivalence;
4. the principal-arc location of the boundary mode;
5. the multiscale locking of that mode;
6. the impossibility of projection or deterministic scale geometry as a free bypass.

Thus the amplifier architecture is complete.

The remaining problems are no longer architectural.

They are arithmetic.

Record:

```text
CAMPAIGN_45
STRUCTURAL_AMPLIFIER_THEORY_COMPLETE
ARITHMETIC_SEED_AND_STRIP_GAP_GATES_OPEN
```

---

# 16. Current literature calibration

The relation between zero-free regions and PNT error terms is classical and remains an active subject.

Recent 2026 work of Broucke gives upper bounds for PNT error terms from broad classes of zero-free regions and studies near-sharpness by constructing generalized prime systems with zeros on prescribed contours.

Recent work of Johnston and Trudgian makes explicit a Pintz/Landau philosophy in the reverse direction: sufficiently strong arithmetic remainder information forces zero-free information.

These results calibrate the present theorem:

```text
arithmetic error improvement
  <-> stronger zero exclusion
```

is not peculiar to CSM_RH.

The internal contribution is the exact matching of that principle to the PESC exponent, MLEPG amplifier law, and principal-Fejer critical-locking geometry.

Current Guth-Maynard large-value technology gives major zero-density and short-interval range improvements, but does not presently provide a fixed strip gap beyond a seeded boundary.

---

# 17. Next campaign

Further coordinate changes of PESC, MLEPG, or the principal arc should not count as progress unless they produce a new arithmetic inequality.

The recommended next campaign is:

```text
CSM_RH Campaign 46
SEEDED_ARITHMETIC_STRIP_GAP_GENERATION
```

Root goal:

```text
Given PESC(kappa),
prove PESC(kappa+eta)
for some fixed eta>0.
```

Equivalent zero goal:

```text
Given beta_* <= 1-kappa/2,
prove beta_* <= 1-(kappa+eta)/2.
```

Allowed prime-side tracks:

```text
SG1 SEEDED_PRINCIPAL_FEJER_POWER_SUPPRESSION
SG2 SEEDED_SHRINKING_THRESHOLD_SHORT_INTERVAL_L2
SG3 SEEDED_ZERO_DETECTOR_WITH_PRIME_SIDE_COERCIVITY
SG4 NEW_ARITHMETIC_CONTRACTION_THEOREM
```

Required output:

$$
\boxed{
\eta>0
\text{ fixed}.
}
$$

Hard rejections:

```text
ANOTHER_EQUIVALENT_CRITERION_WITHOUT_NEW_ESTIMATE
PROJECT_OUT_PRINCIPAL_MODE_WITHOUT_COEFFICIENT_BOUND
USE_ZERO_DENSITY_TO_IGNORE_FINITE_BOUNDARY_ZEROS
PROMOTE_SUBPOWER_TO_FIXED_POWER
ASSUME_BOUNDARY_LINE_IS_ZERO_FREE
ASSUME_PAIR_CORRELATION
ASSUME_RH
```

---

# 18. State transition

Advance the candidate state from

$$
v1.45
$$

to

$$
v1.46.
$$

Add:

```text
B-RH-055
FIXED_EXPONENT_PESC_ZERO_FREE_STRIP_EQUIVALENCE
CERTIFIED
```

Add:

```text
B-RH-056
PESC_MAXIMAL_EXPONENT_EQUALS_TWICE_GLOBAL_ZETA_ZERO_FREE_GAP
CERTIFIED
```

Add:

```text
B-RH-057
FIXED_ZETA_ZERO_MODE_CONCENTRATES_ON_PRINCIPAL_FEJER_ARC
CERTIFIED_AS_MODEL_THEOREM
```

Add:

```text
B-RH-058
STRICT_SEEDED_MLEPG_AMPLIFICATION_IMPLIES_STRICT_ZERO_STRIP_NARROWING
CERTIFIED
```

Add:

```text
O-RH-133
BOUNDARY_ZERO_MODE_IS_ASYMPTOTICALLY_MAXIMALLY_LOCKED_ACROSS_SUBLINEAR_DYADIC_LAGS
CERTIFIED_AS_MODEL_BARRIER
```

Add:

```text
O-RH-134
PRINCIPAL_ARC_PROJECTION_CANNOT_BYPASS_BOUNDARY_MODE_WITHOUT_INDEPENDENT_POWER_SUPPRESSION
CERTIFIED
```

Campaign 45:

```text
STRUCTURAL_AMPLIFIER_THEORY_COMPLETE
ARITHMETIC_GATES_OPEN
```

No RH certificate is created.

---

# 19. Conclusion

The CSM_RH exponent has acquired an exact spectral meaning.

$$
\boxed{
\kappa_*
=
2(1-\beta_*).
}
$$

A seeded PESC exponent is therefore a measured zero-free gap.

An amplifier must enlarge that gap.

The principal Fejer arc contains precisely the kind of smooth explicit-formula mode which saturates the seed exponent. A boundary zero mode has

$$
\boxed{
\mathcal S_\rho(N,H)
\asymp
NH^2N^{-\kappa}
}
$$

and

$$
\boxed{
G_\rho(J)=o(1).
}
$$

It cannot be removed by a free projection and it cannot be destroyed by deterministic multiscale geometry.

Thus the next advance must be an actual theorem about the primes.

Not a new representation.

Not a new equivalent condition.

Not a new zero-density count which permits a finite boundary exception.

The missing object is now exact:

$$
\boxed{
\text{a prime-side theorem which creates a fixed new strip gap}.
}
$$
