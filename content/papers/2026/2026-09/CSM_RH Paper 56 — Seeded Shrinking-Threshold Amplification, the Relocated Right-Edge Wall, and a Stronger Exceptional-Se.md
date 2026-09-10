# CSM_RH Paper 56

## Seeded Shrinking-Threshold Amplification, the Relocated Right-Edge Wall, and a Stronger Exceptional-Set Bootstrap Law

**Project:** CSM_RH  
**Paper:** 56  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Tracks:** SG1 / SG2 structural audit and seeded bridge  
**Status:** NEW SEEDED SHRINKING-THRESHOLD AMPLIFIER BRIDGE CERTIFIED / ARITHMETIC THRESHOLD THEOREM OPEN  
**Canonical entry state:** v1.46 / Paper 55 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 55 proved that for every fixed

$$
0<\kappa\le1,
$$

PESC $(\kappa)$ is exponent-equivalent to the fixed zeta zero-free strip

$$
\beta_*
\le
1-\frac{\kappa}{2},
$$

where

$$
\beta_*
=
\sup_{\zeta(\rho)=0}\Re\rho.
$$

Campaign 46 asks for a genuine arithmetic theorem producing a strict improvement

$$
\kappa
\longmapsto
\kappa+\eta.
$$

The present paper revisits the shrinking-threshold exceptional-set route of Papers 37–38 under the new seeded information.

The seed PESC estimate gives more than a dyadic $L^2$ norm. Through the fixed zero-free strip it also gives the pointwise PNT error bound

$$
\boxed{
|\psi(x)-x|
\ll
x^{1-\kappa/2+o(1)}.
}
$$

This changes the bad-set ledger in the shrinking-threshold bridge.

Let

$$
H=N^\alpha,
\qquad
0<\alpha<1,
$$

and define

$$
U_H(x)
=
\psi(x+H)-\psi(x)-H.
$$

Suppose that for fixed

$$
\nu>0,
\qquad
c>0,
$$

one has the polynomial shrinking-threshold exceptional-set estimate

$$
\boxed{
\#\left\{
x\in[N,2N]:
|U_H(x)|>HN^{-\nu}
\right\}
\ll
N^{1-c}.
}
$$

On the good set the lag energy is bounded by

$$
NH^2N^{-2\nu}.
$$

On the exceptional set, instead of the old trivial bound $|U_H|\ll H\log N$, the seeded pointwise PNT estimate gives

$$
|U_H(x)|
\ll
N^{1-\kappa/2+o(1)}.
$$

Consequently

$$
\boxed{
\mathcal S_\Lambda(N,H)
\ll
NH^2N^{-2\nu}
+
N^{3-\kappa-c+o(1)}.
}
$$

At $H=N^\alpha$, the second term is

$$
NH^2N^{-\delta_{\rm bad}+o(1)}
$$

with

$$
\boxed{
\delta_{\rm bad}
=
\kappa+c+2\alpha-2.
}
$$

Thus the seeded exceptional-set theorem yields the effective lag exponent

$$
\boxed{
\delta_{\rm ST}
=
\min
\left\{
2\nu,
\kappa+c+2\alpha-2
\right\}.
}
$$

Combining this with Paper 54's seeded residue-chain theorem gives the new bootstrap law

$$
\boxed{
\kappa'
<
\Phi_{\rm ST}
(\kappa;\alpha,\nu,c)
:=
\min
\left\{
\alpha,
2\nu,
\kappa+c+2\alpha-2,
2-\alpha(2-\kappa)
\right\}.
}
$$

Strict amplification occurs exactly when

$$
\boxed{
\alpha>\kappa,
\qquad
\nu>\frac{\kappa}{2},
\qquad
c>2(1-\alpha).
}
$$

This is strictly weaker in its exceptional-set requirement than the unseeded Paper-37 bridge. The old bridge required the exceptional-set exponent itself to exceed the target lag exponent. In the seeded bridge, choosing $\alpha$ close to $1$ allows any fixed $c>0$ to participate in a strict amplifier, provided the good-set accuracy crosses the critical threshold $\nu=\kappa/2$.

For moderate $c$, and assuming the good-set threshold is not the active bottleneck, the optimal scale is

$$
\boxed{
\alpha_*
=
1-\frac{c}{4-\kappa}
}
$$

and the one-step exponent becomes

$$
\boxed{
\kappa_{\rm ST}^*
=
\kappa
+
\frac{
c(2-\kappa)
}{
4-\kappa
}.
}
$$

The paper then identifies the exact new right-edge wall.

Before a seed existed, Paper 38 found a fatal shrinking edge at $\sigma\to1$. PESC $(\kappa)$ removes that edge and relocates it to

$$
\boxed{
\sigma_{\rm edge}
=
1-\frac{\kappa}{2}.
}
$$

A zero mode on this boundary has relative short-interval size

$$
N^{-\kappa/2}
$$

at every sublinear lag below its resonant height. Hence:

- thresholds $\nu<\kappa/2$ lie above the boundary-mode amplitude and may be compatible with the seed;
- $\nu=\kappa/2$ is the critical locking threshold;
- every threshold $\nu>\kappa/2$ lies below the boundary-mode amplitude and is therefore itself strip-improving arithmetic.

This is also visible in the standard zero-packet moment method. At the seeded boundary, a $2r$ -th moment followed by Markov at threshold $HN^{-\nu}$ incurs the baseline exponent

$$
1+2r
\left(
\nu-\frac{\kappa}{2}
\right)
$$

before any nonnegative density cost. If $\nu>\kappa/2$, the exponent already exceeds $1$. Thus no standard finite-moment-plus-Markov treatment of a boundary packet can cross the amplifier threshold while the boundary mode remains admissible.

The seed therefore repairs Paper 38's old $\sigma\to1$ subpower obstruction, but replaces it with a sharper fixed critical wall at $\nu=\kappa/2$.

The new bridge identifies a potentially more economical amplifier route than full MLEPG: a near-macroscopic shrinking-threshold theorem with only a modest polynomial exceptional-set saving can suffice. However, the required good-set accuracy must still cross the boundary-mode scale, and no current theorem of Gafni–Tao or related short-interval technology is known to do this.

No RH theorem is claimed.

---

# 1. Seed information from Paper 55

Assume PESC $(\kappa)$ for a fixed

$$
0<\kappa<1.
$$

Paper 55 certified

$$
\boxed{
\beta_*
\le
1-\frac{\kappa}{2}.
}
$$

The same paper proved the converse direction through the truncated explicit formula:

if

$$
\beta_*
\le
\sigma_0<1,
$$

then

$$
\psi(x)-x
\ll
x^{\sigma_0}\log^2x.
$$

Therefore the seed gives

$$
\boxed{
A(x)
:=
\psi(x)-x
\ll
x^{1-\kappa/2}\log^2x.
}
$$

At exponent resolution,

$$
\boxed{
|A(x)|
\ll
x^{1-\kappa/2+o(1)}.
}
$$

This pointwise consequence was not available in the original unseeded Campaign 36–37 bridge.

---

# 2. Seeded pointwise short-interval envelope

Let

$$
H=N^\alpha,
\qquad
0<\alpha<1.
$$

Define

$$
U_H(x)
=
\psi(x+H)-\psi(x)-H.
$$

Since

$$
U_H(x)
=
A(x+H)-A(x),
$$

the seed pointwise estimate gives uniformly for

$$
N\le x\le2N,
$$

$$
\boxed{
|U_H(x)|
\ll
N^{1-\kappa/2+o(1)}.
}
$$

Relative to $H=N^\alpha$ this is

$$
\boxed{
\frac{|U_H(x)|}{H}
\ll
N^{-\nu_{\rm seed}+o(1)},
}
$$

where

$$
\boxed{
\nu_{\rm seed}
=
\alpha-1+\frac{\kappa}{2}.
}
$$

This exponent is positive only when

$$
\alpha>
1-\frac{\kappa}{2}.
$$

Even when positive,

$$
\nu_{\rm seed}
<
\frac{\kappa}{2}
$$

for every genuinely sublinear scale $\alpha<1$.

Thus the uniform seed estimate approaches, but never crosses, the boundary threshold $\kappa/2$.

---

# 3. Seeded shrinking-threshold hypothesis

Fix

$$
\nu>0,
\qquad
c>0.
$$

Define the exceptional set

$$
\boxed{
\mathcal E_{N,H}(\nu)
=
\left\{
x\in[N,2N]\cap\mathbb Z:
|U_H(x)|>HN^{-\nu}
\right\}.
}
$$

The seeded shrinking-threshold input is

$$
\boxed{
|\mathcal E_{N,H}(\nu)|
\ll
N^{1-c}.
}
$$

No such theorem with amplifier parameters is assumed or proved here.

The purpose of this paper is to compute its exact deterministic consequence once a PESC seed is already present.

---

# 4. Improved bad-set energy using the seed

Split

$$
\mathcal S_\Lambda(N,H)
=
\sum_{N\le x<2N-H}
|U_H(x)|^2
$$

into good and bad sets.

## Good set

Outside $\mathcal E_{N,H}(\nu)$,

$$
|U_H(x)|^2
\le
H^2N^{-2\nu}.
$$

Hence

$$
\boxed{
\mathcal S_{\rm good}
\ll
NH^2N^{-2\nu}.
}
$$

## Exceptional set

On the exceptional set use the seed pointwise envelope, not the trivial prime-counting bound:

$$
|U_H(x)|^2
\ll
N^{2-\kappa+o(1)}.
$$

Therefore

$$
\boxed{
\mathcal S_{\rm bad}
\ll
N^{1-c}
N^{2-\kappa+o(1)}
=
N^{3-\kappa-c+o(1)}.
}
$$

Combining:

## Theorem 4.1 — Seeded shrinking-threshold lag-energy bridge

Assume PESC $(\kappa)$ and the exceptional-set estimate of Section 3. Then

$$
\boxed{
\mathcal S_\Lambda(N,H)
\ll
NH^2N^{-2\nu}
+
N^{3-\kappa-c+o(1)}.
}
$$

At

$$
H=N^\alpha,
$$

write

$$
N^{3-\kappa-c}
=
NH^2
N^{-\delta_{\rm bad}},
$$

where

$$
\boxed{
\delta_{\rm bad}
=
\kappa+c+2\alpha-2.
}
$$

Thus

$$
\boxed{
\mathcal S_\Lambda(N,H)
\ll
NH^2
N^{-\delta_{\rm ST}+o(1)}
}
$$

with

$$
\boxed{
\delta_{\rm ST}
=
\min
\left\{
2\nu,
\kappa+c+2\alpha-2
\right\}.
}
$$

Create:

```text
B-RH-059
SEEDED_SHRINKING_THRESHOLD_EXCEPTIONAL_SET_TO_LAG_POWER_GAIN
CERTIFIED
```

This strictly improves the old unseeded bridge B-RH-012 whenever the seed pointwise PNT bound is stronger than the trivial bad-set envelope.

---

# 5. Seeded shrinking-threshold PESC map

Paper 54's seeded residue-chain theorem states that PESC $(\kappa)$ plus a lag exponent $\delta$ at scale $N^\alpha$ gives every

$$
\kappa'
<
\min
\left\{
\alpha,
\delta,
2-\alpha(2-\kappa)
\right\}.
$$

Insert $\delta_{\rm ST}$ from Theorem 4.1.

## Theorem 5.1 — Seeded shrinking-threshold amplification law

Assume PESC $(\kappa)$ and the shrinking-threshold exceptional-set theorem

$$
|\mathcal E_{N,N^\alpha}(\nu)|
\ll
N^{1-c}.
$$

Then every

$$
\boxed{
\kappa'
<
\Phi_{\rm ST}
(\kappa;\alpha,\nu,c)
}
$$

is admissible, where

$$
\boxed{
\Phi_{\rm ST}
(\kappa;\alpha,\nu,c)
=
\min
\left\{
\alpha,
2\nu,
\kappa+c+2\alpha-2,
2-\alpha(2-\kappa)
\right\}.
}
$$

Create:

```text
B-RH-060
SEEDED_SHRINKING_THRESHOLD_PESC_AMPLIFICATION_LAW
CERTIFIED
```

---

# 6. Exact strict-amplifier gate

We ask when

$$
\Phi_{\rm ST}
(\kappa;\alpha,\nu,c)
>
\kappa.
$$

The four conditions are:

$$
\alpha>\kappa,
$$

$$
2\nu>\kappa,
$$

$$
\kappa+c+2\alpha-2>\kappa,
$$

and

$$
2-\alpha(2-\kappa)>\kappa.
$$

The final inequality is automatic for $\alpha<1$.

The third simplifies to

$$
c>2(1-\alpha).
$$

Therefore:

## Corollary 6.1 — Seeded exceptional-set strict-amplifier gate

For

$$
0<\kappa<1,
\qquad
0<\alpha<1,
$$

strict amplification occurs exactly when

$$
\boxed{
\alpha>\kappa,
\qquad
\nu>\frac{\kappa}{2},
\qquad
c>2(1-\alpha).
}
$$

This is a substantially weaker requirement on $c$ than in the unseeded lag-energy bridge.

If $\alpha$ is chosen sufficiently close to $1$, any fixed

$$
c>0
$$

can satisfy the exceptional-set condition.

The non-negotiable threshold remains

$$
\boxed{
\nu>\frac{\kappa}{2}.
}
$$

---

# 7. Optimization when the exceptional exponent is modest

Assume first that the threshold term $2\nu$ is not the bottleneck.

We maximize

$$
\min
\left\{
\alpha,
\kappa+c+2\alpha-2,
2-\alpha(2-\kappa)
\right\}.
$$

For the usual regime of modest $c$, the scale term $\alpha$ is inactive at the optimum.

Balance the bad-set term with the seeded anchor:

$$
\kappa+c+2\alpha-2
=
2-\alpha(2-\kappa).
$$

This gives

$$
\boxed{
\alpha_*
=
1-\frac{c}{4-\kappa}.
}
$$

The common output exponent is

$$
\boxed{
\kappa_{\rm exc}^*
=
\kappa
+
\frac{
c(2-\kappa)
}{
4-\kappa
}.
}
$$

Define

$$
\boxed{
c_{\rm crit}(\kappa)
=
\frac{
(1-\kappa)(4-\kappa)
}{
3-\kappa
}.
}
$$

For

$$
0<c\le c_{\rm crit}(\kappa),
$$

the scale term is indeed inactive and the formula above is the optimizer.

For larger $c$, the original seeded MLEPG scale ceiling becomes active and the maximum cannot exceed

$$
\frac{2}{3-\kappa}.
$$

Thus, absent the threshold bottleneck,

$$
\boxed{
\Phi_{\rm ST}^{\rm opt}
\le
\frac{2}{3-\kappa}.
}
$$

The shrinking-threshold route therefore interpolates naturally between a weak exceptional-set amplifier and the ideal natural-MLEPG amplifier of Paper 54.

---

# 8. Threshold requirement at the optimized scale

In the modest- $c$ regime, the target output is

$$
\kappa_{\rm exc}^*
=
\kappa
+
\frac{
c(2-\kappa)
}{
4-\kappa
}.
$$

To keep $2\nu$ from becoming the bottleneck, it suffices that

$$
2\nu
\ge
\kappa_{\rm exc}^*.
$$

Equivalently,

$$
\boxed{
\nu
\ge
\frac{\kappa}{2}
+
\frac{
c(2-\kappa)
}{
2(4-\kappa)
}.
}
$$

Thus the good-set accuracy need only cross the boundary threshold by an amount proportional to the available exceptional-set power.

This gives a quantitative tradeoff between:

- threshold precision;
- exceptional-set rarity;
- output zero-strip improvement.

---

# 9. The right edge is relocated by the seed

Paper 38 found that the unseeded Gafni–Tao architecture fails at a right-edge packet

$$
\sigma\to1
$$

whose available amplitude suppression is only subpower.

PESC $(\kappa)$ changes the geometry completely.

There are no zeros with

$$
\sigma>
1-\frac{\kappa}{2}.
$$

Thus the surviving right edge is

$$
\boxed{
\sigma_{\rm edge}
=
1-\frac{\kappa}{2}.
}
$$

This is a fixed distance from $1$.

The old Vinogradov–Korobov shrinking-edge packet is absent under the seed.

Therefore:

```text
OLD RIGHT EDGE
sigma -> 1
subpower zero-free width
fatal for polynomial threshold

SEEDED RIGHT EDGE
sigma <= 1-kappa/2
fixed edge
polynomial threshold bookkeeping becomes meaningful
```

This is a genuine structural repair of the Paper-38 architecture.

However, the repaired edge contains its own critical wall.

---

# 10. Boundary-zero threshold scale

Take a model zero on the seeded boundary:

$$
\rho
=
1-\frac{\kappa}{2}
+i\gamma.
$$

Paper 55 proved that for a fixed zero and sublinear lags below the resonant height,

$$
U_{\rho,H}(x)
=
-Hx^{\rho-1}
\left[
1+o(1)
\right].
$$

Hence

$$
\boxed{
\frac{
|U_{\rho,H}(x)|
}{
H
}
\asymp_\rho
N^{-\kappa/2}
}
$$

on a positive-amplitude portion of the dyadic block.

Therefore define the boundary threshold

$$
\boxed{
\nu_{\rm edge}
=
\frac{\kappa}{2}.
}
$$

The threshold geometry is:

## Subcritical accuracy

$$
\nu<\frac{\kappa}{2}.
$$

Then

$$
HN^{-\nu}
\gg
HN^{-\kappa/2}.
$$

A boundary zero mode can lie below the threshold. Such a theorem need not improve the zero strip.

## Critical accuracy

$$
\nu=\frac{\kappa}{2}.
$$

The threshold is at the exact boundary-mode scale.

## Supercritical accuracy

$$
\nu>\frac{\kappa}{2}.
$$

Then

$$
HN^{-\nu}
\ll
HN^{-\kappa/2}.
$$

A boundary mode is larger than the allowed good-set threshold.

This is precisely the threshold needed by Corollary 6.1.

Thus the strict amplifier gate and the boundary-zero detection threshold coincide.

---

# 11. Three-zone seeded threshold geometry

The seed itself supplies the uniform relative exponent

$$
\nu_{\rm seed}
=
\alpha-1+\frac{\kappa}{2}.
$$

For every $\alpha<1$,

$$
\nu_{\rm seed}
<
\frac{\kappa}{2}.
$$

Hence the seeded short-interval precision landscape has three zones:

```text
ZONE I
nu <= alpha-1+kappa/2

uniformly available from the seed pointwise PNT bound

ZONE II
alpha-1+kappa/2 < nu <= kappa/2

requires additional mesoscopic arithmetic
but remains compatible with a boundary zero

ZONE III
nu > kappa/2

strict strip-improvement zone
boundary zero no longer compatible
```

The purpose of current almost-all short-interval technology can therefore be separated into:

- seed-preserving mesoscopic refinement in Zone II;
- genuine strip-gap generation in Zone III.

Only Zone III can amplify $\kappa$.

---

# 12. Seeded moment barrier at the relocated edge

Paper 38 audited a standard $2r$ -th moment plus Markov architecture.

At a zero strip with

$$
d=1-\sigma,
$$

the zero-packet amplitude has relative scale

$$
N^{-d}.
$$

A $2r$ -th moment therefore has baseline power

$$
N^{-2rd}
$$

relative to the full-measure scale.

Markov at the shrinking threshold

$$
N^{-\nu}
$$

costs

$$
N^{2r\nu}.
$$

At the seeded edge

$$
d=\frac{\kappa}{2},
$$

the baseline exceptional-set exponent becomes

$$
\boxed{
1
+
2r
\left(
\nu-\frac{\kappa}{2}
\right)
}
$$

before including any nonnegative zero-density tax.

Therefore:

## Theorem 12.1 — Seeded right-edge finite-moment barrier

Within the standard zero-packet $2r$ -moment plus Markov architecture, if

$$
\nu>\frac{\kappa}{2},
$$

then the boundary-strip contribution already has exponent strictly greater than $1$ before zero-density losses are added.

Hence no finite moment order can prove a power-saving exceptional-set estimate at a supercritical threshold while the boundary packet remains admissible.

Create:

```text
O-RH-135
SEEDED_STANDARD_MOMENT_MARKOV_ARCHITECTURE_CANNOT_CROSS_BOUNDARY_THRESHOLD
CERTIFIED_AS_METHOD_BARRIER
```

This is not a universal impossibility theorem for every moment method.

It identifies the exact failure of the standard packet-plus-Markov architecture.

---

# 13. Relation to the old Paper-38 barrier

Paper 38 proved:

```text
unseeded polynomial shrinking threshold
fails near sigma -> 1

reason:
threshold penalty remains fixed
while zero-free width shrinks to zero
```

The new seed removes $\sigma\to1$ entirely.

For thresholds satisfying

$$
\nu<\frac{\kappa}{2},
$$

the surviving right edge has positive amplitude margin

$$
\frac{\kappa}{2}-\nu>0.
$$

Thus the old asymptotic subpower mismatch is no longer the first obstruction.

The architecture may have exponent room in this subcritical regime, subject to:

- parameter uniformity;
- explicit-formula height tax;
- spatial localization;
- zero-density constants.

But this regime cannot amplify the seed.

At the supercritical threshold needed for amplification, a new obstruction appears immediately:

$$
\boxed{
\text{the seed boundary mode itself}.
}
$$

This is sharper than the old right-edge barrier.

---

# 14. Current Gafni–Tao theorem does not cross the wall

Gafni and Tao prove quantitative exceptional-set estimates for the prime number theorem in short intervals using zero-density inputs, including the 2026 Guth–Maynard estimates.

Their theorem is formulated for a fixed relative error threshold. In the proof, the threshold parameters are fixed before the asymptotic limit.

Thus the published theorem does not provide a uniform substitution

$$
\delta=N^{-\nu}.
$$

Paper 38 already certified this theorem-scope issue.

The seed PESC strip repairs the right-edge geometry but does not repair this parameter-uniformity gap automatically.

More importantly, even a successful uniformization of the existing standard moment architecture can at most approach the seeded boundary threshold from below. Theorem 12.1 shows that crossing

$$
\nu=\frac{\kappa}{2}
$$

requires a new mechanism which suppresses or excludes the boundary packet itself.

This is the arithmetic content of Campaign 46.

---

# 15. Relation to inverse short-interval theory

The idea that strong almost-all short-interval estimates constrain the zeta zeros is classical.

Zaccagnini's work on primes in almost all short intervals proves converse theorems: sufficiently strong uniform Selberg-integral bounds imply zero-density estimates and zero-free regions.

This external literature confirms the direction of the present bridge:

$$
\boxed{
\text{short-interval power precision}
\Longrightarrow
\text{zero-strip information}.
}
$$

The internal seeded bridge is sharper for the present purpose because it explicitly reuses the existing PESC exponent in the exceptional-set bad-set ledger and feeds the resulting lag exponent into the exact Campaign-45 bootstrap map.

No claim of novelty is made for the broad inverse philosophy.

---

# 16. SG1 verdict

SG1 asked for seeded principal Fejer power suppression.

Paper 55 already showed that a boundary zero mode places essentially all of its derivative energy on the principal arc and saturates the exponent $\kappa$.

The present threshold analysis gives the same conclusion in physical space.

Thus:

```text
SG1 STRUCTURAL STATUS:
CLOSED AS BOUNDARY-THRESHOLD LOCKING IDENTIFIED

SG1 ARITHMETIC STATUS:
OPEN
```

Any theorem proving principal-arc suppression beyond $N^{1-\kappa}$ is itself a strip-gap theorem.

---

# 17. SG2 verdict

SG2 asked whether the shrinking-threshold route becomes more useful after a PESC seed.

Answer:

```text
YES.
```

The seeded pointwise PNT bound improves the exceptional-set-to-lag bridge from the old bad-set exponent to

$$
\delta_{\rm bad}
=
\kappa+c+2\alpha-2.
$$

This reduces the strict exceptional-set requirement to

$$
c>2(1-\alpha).
$$

Thus SG2 is structurally stronger than previously recognized.

But:

```text
THE ARITHMETIC THRESHOLD THEOREM REMAINS OPEN.
```

The good-set precision must cross

$$
\nu>\frac{\kappa}{2},
$$

which is exactly the seeded boundary-zero scale.

Record:

```text
SG2S
CLOSED_WITH_SEEDED_SHRINKING_THRESHOLD_AMPLIFICATION_LAW

SG2A
OPEN_SUPERCRITICAL_SHRINKING_THRESHOLD_EXCEPTIONAL_SET_THEOREM
```

---

# 18. New minimal arithmetic target

The full MLEPG natural-variance theorem is not necessary for a strict bootstrap.

A weaker near-macroscopic target suffices.

Choose

$$
\alpha=1-\tau
$$

with fixed

$$
\tau>0.
$$

Then the strict gate becomes

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>2\tau,
\qquad
1-\tau>\kappa.
}
$$

Thus Campaign 46 can seek:

> On intervals of length  
> $$H=N^{1-\tau},$$  
> prove relative error  
> $$N^{-\nu}$$  
> for all but $N^{1-c}$ starting points, with  
> $$\nu>\kappa/2$$  
> and  
> $$c>2\tau.$$

This is a quantitatively weaker target than natural-order MLEPG across the full interval range.

It still creates a strict fixed zero-strip improvement.

Create:

```text
F-RH-017
SEEDED_SUPERCRITICAL_SHRINKING_THRESHOLD_EXCEPTIONAL_SET
OPEN / CAMPAIGN-46 DIRECT ARITHMETIC TARGET
```

---

# 19. Recommended next track: SG3

SG1 and SG2 now meet the same boundary packet.

The next route should not continue increasing ordinary moment order.

Open:

```text
SG3
SEEDED_ZERO_DETECTOR_WITH_PRIME_SIDE_COERCIVITY
```

The target is a mechanism which uses the special arithmetic structure of $\Lambda$ to exclude a boundary packet rather than merely estimate its positive moments.

Candidate ingredients:

```text
SG3A
TURAN_POWER_SUM_BOUNDARY_ZERO_DETECTOR

SG3B
GALLAGHER_SHORT_INTERVAL_L2_COERCIVITY_WITH_SEED

SG3C
BOUNDARY_PACKET_PHASE_LOCALIZATION_AND_INERTIA

SG3D
PRIME_SIDE UPPER BOUND STRONG ENOUGH TO CONTRADICT DETECTOR LOWER BOUND
```

This direction is motivated by classical inverse short-interval work, where zeros are detected through large derivatives of logarithmic zeta quantities and related short-interval coefficient energies.

No SG3 theorem is claimed here.

---

# 20. State transition

Advance the candidate state from

$$
v1.46
$$

to

$$
v1.47.
$$

Add:

```text
B-RH-059
SEEDED_SHRINKING_THRESHOLD_EXCEPTIONAL_SET_TO_LAG_POWER_GAIN
CERTIFIED
```

Add:

```text
B-RH-060
SEEDED_SHRINKING_THRESHOLD_PESC_AMPLIFICATION_LAW
CERTIFIED
```

Add:

```text
O-RH-135
SEEDED_STANDARD_MOMENT_MARKOV_ARCHITECTURE_CANNOT_CROSS_BOUNDARY_THRESHOLD
CERTIFIED_AS_METHOD_BARRIER
```

Add frontier:

```text
F-RH-017
SEEDED_SUPERCRITICAL_SHRINKING_THRESHOLD_EXCEPTIONAL_SET
OPEN
```

Campaign 46 state:

```text
SG1 STRUCTURAL CLOSED / ARITHMETIC OPEN
SG2 STRUCTURAL CLOSED / ARITHMETIC OPEN
SG3 ACTIVE
SG4 OPEN
```

No RH certificate is created.

---

# 21. Conclusion

A PESC seed fundamentally changes the shrinking-threshold problem.

It supplies a pointwise envelope

$$
|\psi(x)-x|
\ll
x^{1-\kappa/2+o(1)},
$$

which strengthens the bad-set ledger and yields the new bootstrap map

$$
\boxed{
\Phi_{\rm ST}
=
\min
\left\{
\alpha,
2\nu,
\kappa+c+2\alpha-2,
2-\alpha(2-\kappa)
\right\}.
}
$$

The exceptional-set requirement can be made very mild by working near the macroscopic scale.

But one threshold cannot be weakened:

$$
\boxed{
\nu>\frac{\kappa}{2}.
}
$$

The old right edge at $\sigma\to1$ has disappeared.

The new edge is fixed:

$$
\boxed{
\sigma=1-\frac{\kappa}{2}.
}
$$

And the boundary zero mode lives exactly at relative short-interval scale

$$
\boxed{
N^{-\kappa/2}.
}
$$

Thus Campaign 46 has localized the next arithmetic breakthrough even more tightly.

The next theorem does not need to prove the full natural Selberg variance.

It only needs to beat the seeded boundary threshold on almost all near-macroscopic intervals with a modest fixed exceptional-set saving.

That is F-RH-017.
