# CSM_RH Paper 61

## Local-Increment Correction to the Exceptional-Set Amplifier, Piecewise Sharpness, and the Corrected F-RH-017 Gate

**Project:** CSM_RH  
**Paper:** 61  
**Version:** v0.1  
**Date:** 2026-09-08  
**Campaign:** 46 — `SEEDED_ARITHMETIC_STRIP_GAP_GENERATION`  
**Frontier:** F-RH-017-v3  
**Status:** PAPER-60 GLOBAL SHARPNESS CLAIM CORRECTED / STRONGER LOCAL-ENVELOPE AMPLIFIER CERTIFIED / ARITHMETIC UPPER THEOREM OPEN  
**Canonical entry state:** v1.51 / Paper 60 v0.1  
**RH_PROVED:** FALSE  
**RH_DISPROVED:** FALSE  
**GLOBAL_RH_CERTIFICATE:** FALSE

---

# Abstract

Paper 60 claimed that the exceptional-count condition

$$
c>\tau
$$

was globally sharp for the direct frontier

$$
H=N^{1-\tau}.
$$

That statement is correct in the near-macroscopic regime

$$
\tau\le\frac{\kappa}{2},
$$

which was the main intended regime, but it is too strong when

$$
\tau>\frac{\kappa}{2}.
$$

The missing ingredient was the elementary local increment bound for the actual von Mangoldt short-interval error.

Let

$$
A(n)=\psi(n)-n,
\qquad
U_H(n)=A(n+H)-A(n).
$$

Assume PESC $(\kappa)$ and write

$$
d=\frac{\kappa}{2}.
$$

The seed gives

$$
|A(n)|
\ll
N^{1-d+o(1)}
$$

on a dyadic block. Independently, because

$$
0\le\Lambda(m)\le\log(3N),
$$

one has

$$
|U_H(n)|
\ll
H\log N.
$$

Thus, for

$$
H=N^{1-\tau},
$$

the correct bad-set envelope is

$$
\boxed{
|U_H(n)|
\ll
N^{1-\max(d,\tau)+o(1)}.
}
$$

Recomputing the seeded residue-chain $L^p$ bridge with this local envelope gives

$$
\boxed{
d_p'
<
\Psi_p^{\rm loc}
(d;\tau,\nu,c)
:=
\min
\left\{
\nu,\,
(d-\tau)_+
+\frac{c}{p},\,
d+\tau(1-d)
\right\}.
}
$$

As in Paper 59, $p=1$ is optimal. Hence

$$
\boxed{
\kappa'
<
\Phi_{\rm loc}
(\kappa;\tau,\nu,c)
:=
2
\min
\left\{
\nu,\,
\left(
\frac{\kappa}{2}-\tau
\right)_+
+c,\,
\frac{\kappa}{2}
+
\tau
\left(
1-\frac{\kappa}{2}
\right)
\right\}.
}
$$

The exact strict-amplification gate is now

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>
\min
\left\{
\tau,\frac{\kappa}{2}
\right\}.
}
$$

Equivalently, the fixed exponent gain may be any

$$
\boxed{
\eta
<
2
\min
\left\{
\nu-d,\,
c-\min(d,\tau),\,
\tau(1-d)
\right\}.
}
$$

This strictly improves Paper 59 when $\tau>d$ and agrees with it when $\tau\le d$.

The sharpness analysis also changes in exactly the same way.

For a hypothetical seed-boundary zero

$$
\beta=1-d,
$$

the polynomial-scale multiplicative Pintz forcing from Paper 60 gives total mean absolute short-interval mass of order

$$
N^{2-d-\tau}.
$$

Using the correct local envelope

$$
\min
\left\{
N^{1-d},
N^{1-\tau}
\right\}
$$

shows that a supercritical threshold forces exceptional mass at least

$$
\boxed{
N^{1-\min(d,\tau)-o(1)}.
}
$$

Thus the corrected critical exception exponent is

$$
\boxed{
c_{\rm edge}
=
\min(d,\tau).
}
$$

For a near-boundary zero

$$
\beta=1-d-\delta,
$$

the corresponding lower exceptional mass is

$$
\boxed{
N^{1-\delta-\min(d,\tau)-o(1)}.
}
$$

Hence the two detector margins are

$$
\boxed{
\delta<\nu-d
}
$$

and

$$
\boxed{
\delta<c-\min(d,\tau),
}
$$

matching the first two gains in the corrected $L^1$ amplifier exactly.

A deterministic chain model respecting the local increment cap also saturates the same piecewise count.

- If $\tau\le d$, one seed-sized jump on each residue chain gives $N^{1-\tau}$ bad increments.
- If $\tau>d$, each chain needs $N^{\tau-d}$ local $H$ -sized jumps to build the seed amplitude, giving a total of $N^{1-d}$ bad increments.

Thus

$$
c>\min(d,\tau)
$$

is sharp for the actual local-envelope residue-chain architecture.

Paper 60 is therefore corrected, not discarded. Its $c>\tau$ conclusion remains valid and sharp in the preferred regime $\tau\le\kappa/2$. The canonical frontier is upgraded to F-RH-017-v3 with the full piecewise gate.

The paper also narrows the scope of the Pintz uniformization claimed in Paper 60. What is required and certified here is the polynomial short-interval regime

$$
h=Y^{-\tau},
\qquad
0<\tau<1
$$

with $\tau$ fixed. This is sufficient for CSM_RH. No claim of uniformity for arbitrarily tiny $h$ independent of the $Y$ -scale is needed.

No RH theorem is claimed.

---

# 1. Seed and local notation

Assume PESC $(\kappa)$ with

$$
0<\kappa<1.
$$

Set

$$
\boxed{
d=\frac{\kappa}{2}.
}
$$

Paper 55 gives

$$
\boxed{
|A(n)|
=
|\psi(n)-n|
\ll
N^{1-d+o(1)}
}
$$

for

$$
n\asymp N.
$$

Let

$$
\boxed{
H=N^{1-\tau},
\qquad
0<\tau<1.
}
$$

Define

$$
\boxed{
U_H(n)
=
A(n+H)-A(n)
=
\psi(n+H)-\psi(n)-H.
}
$$

---

# 2. The missing local increment envelope

For

$$
N\le n\le2N
$$

and

$$
1\le H\le N,
$$

$$
\begin{aligned}
0
\le
\psi(n+H)-\psi(n)
&=
\sum_{n<m\le n+H}
\Lambda(m)
\\
&\le
(H+1)\log(3N).
\end{aligned}
$$

Therefore

$$
\boxed{
|U_H(n)|
\ll
H\log N.
}
$$

The seed also gives

$$
|U_H(n)|
\le
|A(n+H)|+|A(n)|
\ll
N^{1-d+o(1)}.
$$

Combining:

## Theorem 2.1 — Seeded local increment envelope

$$
\boxed{
|U_H(n)|
\ll
\min
\left\{
N^{1-d+o(1)},
H N^{o(1)}
\right\}.
}
$$

At

$$
H=N^{1-\tau},
$$

$$
\boxed{
|U_H(n)|
\ll
N^{1-\max(d,\tau)+o(1)}.
}
$$

Create:

```text
B-RH-069
SEEDED_LOCAL_VON_MANGOLDT_INCREMENT_ENVELOPE
CERTIFIED
```

This elementary bound was omitted from the bad-set ledger of Papers 59–60.

---

# 3. Corrected exceptional-set $L^p$ lag bound

Assume

$$
\boxed{
|\mathcal E|
\ll
N^{1-c},
}
$$

where

$$
\mathcal E
=
\left\{
n\in[N,2N]:
|U_H(n)|>HN^{-\nu}
\right\}.
$$

Fix

$$
p\ge1.
$$

## Good set

As before,

$$
\boxed{
\sum_{n\notin\mathcal E}
|U_H(n)|^p
\ll
N
H^p
N^{-p\nu}.
}
$$

## Bad set

Theorem 2.1 gives

$$
\boxed{
\sum_{n\in\mathcal E}
|U_H(n)|^p
\ll
N^{1-c+p(1-\max(d,\tau))+o(1)}.
}
$$

This improves the Paper-59 bad-set term exactly when

$$
\tau>d.
$$

---

# 4. Corrected residue-chain $L^p$ exponent

Paper 59 proved

$$
\sum_{n\le2N}|A(n)|^p
\ll_p
\frac{N}{H}
\sum_{r\le H}|A(r)|^p
+
\left(
\frac{N}{H}
\right)^p
\sum_{n\le2N-H}|U_H(n)|^p.
$$

The anchor remains

$$
\boxed{
N^{1+(1-\tau)p(1-d)+o(1)}.
}
$$

The good lag term becomes

$$
\boxed{
N^{1+p-p\nu}.
}
$$

The corrected bad lag term becomes

$$
\begin{aligned}
&
N^{p\tau}
N^{1-c+p(1-\max(d,\tau))+o(1)}
\\
&=
\boxed{
N^{
1-c
+
p
\left(
1-\max(d,\tau)+\tau
\right)
+o(1)
}.
}
\end{aligned}
$$

Compare with the target

$$
N^{1+p(1-d')+o(1)}.
$$

The three conditions are:

$$
d'<\nu,
$$

$$
d'
<
\max(d,\tau)-\tau
+
\frac{c}{p},
$$

and

$$
d'
<
d+\tau(1-d).
$$

Since

$$
\max(d,\tau)-\tau
=
(d-\tau)_+,
$$

we obtain:

## Theorem 4.1 — Corrected seeded $L^p$ exceptional exponent

$$
\boxed{
d_p'
<
\Psi_p^{\rm loc}
=
\min
\left\{
\nu,\,
(d-\tau)_+
+\frac{c}{p},\,
d+\tau(1-d)
\right\}.
}
$$

Create:

```text
B-RH-070
LOCAL_ENVELOPE_SEEDED_EXCEPTIONAL_SET_TO_GLOBAL_LP_GAIN
CERTIFIED
```

---

# 5. $L^1$ remains optimal

Only the middle term

$$
(d-\tau)_+ + c/p
$$

depends on $p$.

It decreases as $p$ increases.

Therefore:

## Corollary 5.1 — Local-envelope $L^1$ optimality

Among all fixed

$$
p\ge1,
$$

the strongest corrected residue-chain exponent is still attained by

$$
\boxed{
p=1.
}
$$

No change is required to Paper 59's broad $L^1$ optimality conclusion.

---

# 6. Corrected $L^1$ PESC amplification law

Set

$$
p=1.
$$

Then

$$
\boxed{
d'
<
\min
\left\{
\nu,\,
(d-\tau)_+ +c,\,
d+\tau(1-d)
\right\}.
}
$$

The $L^1$ Mellin theorem of Paper 59 converts this to a zero-free strip and therefore to PESC.

Thus:

## Theorem 6.1 — Corrected local-envelope PESC amplifier

Every

$$
\boxed{
\kappa'
<
\Phi_{\rm loc}
(\kappa;\tau,\nu,c)
}
$$

is admissible, where

$$
\boxed{
\Phi_{\rm loc}
=
2
\min
\left\{
\nu,\,
\left(
\frac{\kappa}{2}-\tau
\right)_+
+c,\,
\frac{\kappa}{2}
+
\tau
\left(
1-\frac{\kappa}{2}
\right)
\right\}.
}
$$

Create:

```text
B-RH-071
CORRECTED_LOCAL_ENVELOPE_L1_PESC_AMPLIFICATION_LAW
CERTIFIED
```

---

# 7. Exact corrected strict gate

Strict amplification means

$$
d'>d.
$$

The threshold condition is

$$
\nu>d.
$$

The bad-set condition is

$$
(d-\tau)_+ +c>d.
$$

If

$$
\tau\le d,
$$

this is

$$
c>\tau.
$$

If

$$
\tau\ge d,
$$

this is

$$
c>d.
$$

Hence:

## Corollary 7.1 — Corrected F-RH exceptional gate

$$
\boxed{
\nu>d,
\qquad
c>\min(d,\tau).
}
$$

Returning to $\kappa$:

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>
\min
\left\{
\tau,\frac{\kappa}{2}
\right\}.
}
$$

The anchor condition is automatic for every fixed $\tau>0$.

---

# 8. Corrected explicit exponent gain

Write

$$
\kappa'
=
\kappa+\eta.
$$

The three margins are

$$
\nu-d,
$$

$$
c-\min(d,\tau),
$$

and

$$
\tau(1-d).
$$

Therefore:

## Corollary 8.1

Any fixed

$$
\boxed{
\eta
<
2
\min
\left\{
\nu-\frac{\kappa}{2},
\,
c-
\min
\left(
\tau,\frac{\kappa}{2}
\right),
\,
\tau
\left(
1-\frac{\kappa}{2}
\right)
\right\}
}
$$

is admissible.

This is the corrected direct bootstrap output.

---

# 9. Piecewise optimization

Assume the threshold term is not the bottleneck.

We maximize

$$
\min
\left\{
c-\min(d,\tau),
\tau(1-d)
\right\}.
$$

## Regime I: modest exceptional exponent

If

$$
c\le d(2-d),
$$

the optimizer lies in

$$
\tau\le d.
$$

Balance

$$
c-\tau
=
\tau(1-d).
$$

Thus

$$
\boxed{
\tau_*
=
\frac{c}{2-d}
=
\frac{2c}{4-\kappa}.
}
$$

and

$$
\boxed{
\eta_*
=
\frac{
2c(1-d)
}{
2-d
}
=
\frac{
2c(2-\kappa)
}{
4-\kappa
}.
}
$$

This agrees with Paper 59.

## Regime II: larger exceptional exponent

If

$$
c>d(2-d),
$$

one may enter the region $\tau>d$.

There the bad-set margin is the constant

$$
c-d,
$$

while the anchor margin is

$$
\tau(1-d).
$$

Choosing

$$
\tau
\ge
\frac{c-d}{1-d}
$$

gives

$$
\boxed{
d'-d<c-d,
}
$$

hence

$$
\boxed{
\eta<2(c-d)=2c-\kappa,
}
$$

subject to the threshold and the global endpoint cap.

This regime was underestimated by Paper 59.

---

# 10. Correction to Paper 60's Pintz sharpness ledger

Paper 60 used only the seed pointwise envelope

$$
|U_H|
\ll
N^{1-d+o(1)}
$$

when converting a Pintz mean-absolute lower bound to exceptional mass.

The correct envelope is

$$
\boxed{
|U_H|
\ll
N^{1-\max(d,\tau)+o(1)}.
}
$$

Suppose a seed-boundary zero exists:

$$
\beta=1-d.
$$

In the polynomial multiplicative scale

$$
h=Y^{-\tau},
$$

the adapted Pintz lower bound has total mass

$$
\boxed{
\int
|A((1+h)x)-A(x)|\,dx
\gg
Y^{2-d-\tau}
}
$$

on a constant-multiple window at exponent resolution.

Divide by the corrected local envelope

$$
Y^{1-\max(d,\tau)+o(1)}.
$$

Then any supercritical threshold forces exceptional mass at least

$$
\boxed{
Y^{1-\min(d,\tau)-o(1)}.
}
$$

Therefore:

## Theorem 10.1 — Corrected boundary-zero critical exception exponent

$$
\boxed{
c_{\rm edge}
=
\min(d,\tau).
}
$$

This agrees exactly with Corollary 7.1.

---

# 11. Near-boundary Pintz ledger

Let

$$
\beta
=
1-d-\delta
$$

with

$$
\delta\ge0.
$$

The multiplicative mean lower bound has exponent

$$
Y^{2-d-\delta-\tau}.
$$

At a threshold with

$$
\nu>d+\delta,
$$

the good-set contribution is lower order.

Dividing by the local envelope gives exceptional mass

$$
\boxed{
Y^{1-\delta-\min(d,\tau)-o(1)}.
}
$$

Thus an upper bound

$$
|\mathcal E|
\ll
Y^{1-c}
$$

excludes the zero whenever

$$
\boxed{
c>
\delta+\min(d,\tau).
}
$$

Equivalently,

$$
\boxed{
\delta
<
c-\min(d,\tau).
}
$$

Together with the threshold condition

$$
\delta<\nu-d,
$$

these are exactly the first two strip gains in Corollary 8.1.

The corrected $L^1$ bridge and the boundary-zero lower forcing therefore match.

---

# 12. Corrected scope of the Pintz adaptation

Paper 60 stated uniformity for every

$$
0<h\le h_0.
$$

That formulation was broader than necessary.

The CSM_RH application only requires the polynomial regime

$$
\boxed{
h=Y^{-\tau},
\qquad
0<\tau<1
}
$$

with $\tau$ fixed.

In this regime:

1. the Mellin multiplier
   $$
   Q_h(s)
   =
   \frac{(1+h)^s-1}{h}
   $$
   has uniform polynomial vertical growth;

2. for a fixed zero $\rho$,
   $$
   Q_h(\rho)\to\rho\ne0;
   $$

3. on the large- $x$ tail used in Pintz's contour proof,
   $$
   hx\gg Y^{1-\tau},
   $$
   so the normalized difference has a polynomial growth bound independent at exponent level of $h$ ;

4. the compact lower-limit correction is entire and uniformly controlled.

Thus the Pintz proof may be adapted uniformly at exponent resolution for every fixed polynomial exponent $\tau\in(0,1)$.

Record the corrected scope as:

```text
B-RH-067R
POLYNOMIAL_SCALE_PINTZ_MULTIPLICATIVE_SHORT_INTERVAL_FORCING
CERTIFIED / REPLACES OVERBROAD UNIFORM-h WORDING OF B-RH-067
```

No assertion about arbitrarily tiny $h$ outside a polynomial scale is needed.

---

# 13. Deterministic local-cap sharpness model

We now construct a residue-chain model which respects the local increment cap and saturates the corrected exception count.

Let

$$
H=N^{1-\tau}.
$$

There are $H$ residue chains and each has length

$$
M\asymp N^\tau.
$$

The target seed amplitude is

$$
B=N^{1-d}.
$$

The local increment cap is

$$
L
=
\min(B,H).
$$

## Case I: $\tau\le d$

Then

$$
B\le H.
$$

On every residue chain make one jump of size $B$ and remain at level $B$ thereafter.

The number of bad increments is

$$
\boxed{
H=N^{1-\tau}.
}
$$

Thus

$$
c=\tau.
$$

The plateau occupies almost all entries and

$$
\sum|A(n)|^2
\asymp
N B^2
=
N^{3-2d}.
$$

## Case II: $\tau>d$

Then

$$
H<B.
$$

On each residue chain use

$$
\boxed{
K=N^{\tau-d}
}
$$

successive increments of size $H$.

After these increments the amplitude is

$$
KH
=
N^{\tau-d}
N^{1-\tau}
=
N^{1-d}
=
B.
$$

Then keep the chain at level $B$.

The number of bad increments is

$$
\boxed{
HK
=
N^{1-\tau}
N^{\tau-d}
=
N^{1-d}.
}
$$

Thus

$$
c=d.
$$

Again the plateau dominates the global $L^2$ energy and saturates

$$
N^{3-2d}.
$$

Therefore:

## Theorem 13.1 — Local-increment constrained exception-count sharpness

Within the one-lag residue-chain architecture respecting both:

- the seed amplitude $N^{1-d}$ ; and
- the actual local increment cap $H N^{o(1)}$,

the critical exceptional exponent is exactly

$$
\boxed{
c_{\rm crit}
=
\min(d,\tau).
}
$$

Create:

```text
O-RH-144
LOCAL_INCREMENT_CONSTRAINED_RESIDUE_CHAIN_MODEL_SATURATES_C_EQUALS_MIN_D_TAU
CERTIFIED
```

This replaces the globally overstrong sharpness wording of O-RH-143.

---

# 14. Formal correction ledger

Paper 60 remains useful, but two statements are corrected.

## Correction C-RH-001

Old wording:

```text
c > tau is globally sharp.
```

Correct wording:

```text
c > tau is sharp when tau <= kappa/2.

Globally:
c > min(tau,kappa/2)
is the correct local-envelope gate.
```

## Correction C-RH-002

Old wording:

```text
Pintz multiplicative forcing uniform for all 0<h<=h0.
```

Correct wording:

```text
The CSM_RH-certified scope is
h=Y^{-tau}
for each fixed 0<tau<1,
which is sufficient for the campaign.
```

These corrections strengthen the preferred frontier and narrow an unnecessarily broad uniformity claim.

---

# 15. F-RH-017-v3

Replace F-RH-017-v2 by:

```text
F-RH-017-v3
LOCAL-ENVELOPE SEEDED SUPERCRITICAL EXCEPTIONAL SET
```

At

$$
\boxed{
H=N^{1-\tau}
}
$$

prove

$$
\boxed{
\#\left\{
n\in[N,2N]:
|\psi(n+H)-\psi(n)-H|
>
HN^{-\nu}
\right\}
\ll
N^{1-c}
}
$$

with

$$
\boxed{
\nu>\frac{\kappa}{2},
\qquad
c>
\min
\left\{
\tau,\frac{\kappa}{2}
\right\}.
}
$$

Then a strict PESC exponent improvement follows.

The explicit output is Corollary 8.1.

---

# 16. Relation to current almost-all prime technology

The 2026 work of Matomäki, Radziwiłł, Shao, Tao and Teräväinen proves extremely strong logarithmic discorrelation and Gowers-uniformity estimates for $\Lambda-\Lambda^\sharp$ in almost all short intervals.

For example, in the relevant ranges they obtain arbitrary fixed powers of logarithmic saving outside exceptional sets of arbitrary fixed logarithmic saving.

They also note that under RH one obtains power-saving short-interval prime-number-theorem estimates.

This calibrates the present frontier:

- current unconditional technology is far stronger than qualitative density-zero control;
- but it remains logarithmic at the level relevant here;
- the polynomial threshold
  $$
  N^{-\kappa/2-\varepsilon}
  $$
  required by F-RH-017-v3 is still beyond the published unconditional results.

The stronger local-envelope converter does not change that arithmetic fact.

---

# 17. State transition

Advance the candidate state from

$$
v1.51
$$

to

$$
v1.52.
$$

Add:

```text
B-RH-069
SEEDED_LOCAL_VON_MANGOLDT_INCREMENT_ENVELOPE
CERTIFIED
```

Add:

```text
B-RH-070
LOCAL_ENVELOPE_SEEDED_EXCEPTIONAL_SET_TO_GLOBAL_LP_GAIN
CERTIFIED
```

Add:

```text
B-RH-071
CORRECTED_LOCAL_ENVELOPE_L1_PESC_AMPLIFICATION_LAW
CERTIFIED
```

Replace / narrow:

```text
B-RH-067
->
B-RH-067R
POLYNOMIAL_SCALE_PINTZ_MULTIPLICATIVE_SHORT_INTERVAL_FORCING
```

Replace sharpness obstruction:

```text
O-RH-143
->
O-RH-144
LOCAL_INCREMENT_CONSTRAINED_RESIDUE_CHAIN_MODEL_SATURATES_C_EQUALS_MIN_D_TAU
```

Add corrections:

```text
C-RH-001
PAPER60_GLOBAL_C_GREATER_TAU_SHARPNESS_CORRECTED

C-RH-002
PAPER60_UNIFORM_H_PINTZ_SCOPE_NARROWED_TO_FIXED_POLYNOMIAL_SCALE
```

Preferred frontier:

```text
F-RH-017-v3
```

No RH certificate is created.

---

# 18. Conclusion

The direct exceptional-set gate has one more piece of arithmetic structure than Papers 59–60 initially used:

$$
\boxed{
|U_H|
\ll
H N^{o(1)}.
}
$$

Combining it with the seed pointwise PNT error gives the exact local envelope

$$
\boxed{
|U_H|
\ll
N^{1-\max(\kappa/2,\tau)+o(1)}.
}
$$

This changes the critical exception-count exponent from the globally stated $\tau$ to

$$
\boxed{
\min
\left(
\tau,\frac{\kappa}{2}
\right).
}
$$

The threshold wall remains unchanged:

$$
\boxed{
\nu>\frac{\kappa}{2}.
}
$$

The corrected gate is sharp both in the residue-chain model and in the polynomial-scale boundary-zero Pintz ledger.

For the originally preferred near-macroscopic regime

$$
\tau\le\frac{\kappa}{2},
$$

nothing changes:

$$
c>\tau.
$$

Outside that regime, the campaign is strictly stronger than previously recorded.

The remaining problem is still arithmetic, but the target is now correctly minimized.
