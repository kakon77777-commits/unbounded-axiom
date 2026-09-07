# CSM_RH Paper 23
## Exact Dyadic Haar Resolution, Microscopic Jump-Energy Localization, and Failure of the Diagonal-Injection Shortcut

**Project:** `CSM_RH`  
**Paper:** `23`  
**Version:** `v0.1`  
**Date:** `2026-09-06`  
**Parent state:** `CSM_RH v1.13 / Paper 22`  
**Campaign:** `22 — ARITHMETIC_OCTAVE_DEFECT_ATTACK`  
**Status:** exact multiscale identity / mechanism closure; not a proof or disproof of RH

---

# 0. Trust boundary

This paper does not prove or disprove the Riemann Hypothesis.

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Campaign 22 asks whether the large jump energy of the centered von Mangoldt sequence can force enough arithmetic octave defect at polynomial scales to prove PDSD.

The campaign obtains an exact dyadic Haar resolution of the jump energy.

It also proves that this identity alone cannot force polynomial-scale relative decorrelation.

A two-component countermodel separates:

```text
microscopic high-frequency jump energy
from
macroscopic smooth low-frequency locking.
```

This closes the diagonal-injection / generic Littlewood–Paley shortcut.

No live GLM-5.3-Flash run is claimed.

---

# 1. Finite sequence setup

Let

$$
a=(a_n)
$$

be any finitely supported complex sequence on the integers.

For

$$
H\ge1,
$$

define

$$
U_H(x)
=
\sum_{r=1}^{H}a_{x+r},
$$

$$
\mathcal S(H)
=
\sum_x|U_H(x)|^2,
$$

and the adjacent-block defect

$$
\boxed{
\mathcal D(H)
=
\sum_x
|U_H(x)-U_H(x+H)|^2.
}
$$

Paper 22 gives

$$
\boxed{
\mathcal D(H)
=
4\mathcal S(H)-\mathcal S(2H).
}
$$

---

# 2. Normalized additive octave drop

Divide the defect identity by $4H^2$:

$$
\boxed{
\frac{\mathcal S(H)}{H^2}
-
\frac{\mathcal S(2H)}{(2H)^2}
=
\frac{\mathcal D(H)}{4H^2}.
}
$$

This is an additive telescoping law.

It is distinct from the multiplicative contraction law for $R_X(H)$.

---

# 3. Large-scale limit

Because $a$ has finite support,

$$
\boxed{
\frac{\mathcal S(H)}{H^2}
\longrightarrow
0
}
$$

as

$$
H\to\infty.
$$

For example, if

$$
A_1
=
\sum_n|a_n|,
$$

then for large $H$,

$$
|U_H(x)|
\le
A_1
$$

and only $O(H)$ translates contribute, so

$$
\mathcal S(H)
=
O(H A_1^2).
$$

Hence $\mathcal S(H)/H^2=O(A_1^2/H)$.

---

# 4. Exact dyadic Haar–Calderón resolution

Take

$$
H_j=2^j.
$$

Sum Section 2 from

$$
j=0
$$

to infinity.

Since

$$
\mathcal S(1)
=
\sum_n|a_n|^2,
$$

we obtain:

## Theorem 4.1 — Exact Dyadic Haar Resolution

$$
\boxed{
\sum_{j=0}^{\infty}
\frac{
\mathcal D(2^j)
}{
4^{j+1}
}
=
\sum_n|a_n|^2.
}
$$

This is exact for every finitely supported sequence.

The full microscopic jump energy is partitioned into nonnegative dyadic octave defects.

---

# 5. Fourier proof and dyadic partition of unity

Define

$$
S(\xi)
=
\sum_na_ne(n\xi).
$$

Let

$$
D_H(\xi)
=
\sum_{r=1}^{H}e(r\xi).
$$

Then

$$
\mathcal S(H)
=
\int_0^1
|S(\xi)|^2
|D_H(\xi)|^2
d\xi.
$$

The defect multiplier is

$$
\boxed{
\mathcal D(H)
=
\int_0^1
|S(\xi)|^2
\frac{
|1-e(H\xi)|^4
}{
|1-e(\xi)|^2
}
d\xi.
}
$$

Also,

$$
\frac{|D_H(\xi)|^2}{H^2}
-
\frac{|D_{2H}(\xi)|^2}{(2H)^2}
=
\frac1{4H^2}
\frac{
|1-e(H\xi)|^4
}{
|1-e(\xi)|^2
}.
$$

Thus Theorem 4.1 is a dyadic partition of unity for the Haar-type octave multipliers.

The identity is a special discrete Calderón resolution.

---

# 6. Prime specialization

Now take

$$
a_n
=
\Lambda(n)-1
$$

on a dyadic prime block.

The prime number theorem and the standard second moment of the von Mangoldt function give

$$
\boxed{
\sum_{n\asymp X}
|\Lambda(n)-1|^2
\sim
X\log X.
}
$$

Therefore Theorem 4.1 gives:

## Corollary 6.1 — Exact Prime Jump-Energy Injection

$$
\boxed{
\sum_{j\ge0}
\frac{
\mathcal D_X(2^j)
}{
4^{j+1}
}
\asymp
X\log X.
}
$$

Thus primes unconditionally inject a large total amount of octave energy.

This is a genuine theorem.

It is not yet a PDSD theorem.

---

# 7. Why total octave energy does not imply PDSD

PDSD needs a relative lower bound:

$$
\frac{
\mathcal D_X(H)
}{
\mathcal S_X(H)
}
\ge
c
$$

on enough polynomial scales.

Theorem 4.1 controls instead the absolute weighted sum

$$
\sum_j
\frac{
\mathcal D_X(2^j)
}{
4^{j+1}
}.
$$

The entire $X\log X$ total may be concentrated at microscopic scales.

Therefore:

```text
large total octave mass
  does not imply

large relative polynomial-scale octave defect.
```

This is the octave-localization debt.

---

# 8. Exact additive octave budget

For the normalized prime-side quantity

$$
R_X(H)
=
\frac{
\mathcal S_X(H)
}{
XH^2
},
$$

Paper 22's defect identity gives

$$
\boxed{
R_X(H)-R_X(2H)
=
\frac{
\mathcal D_X(H)
}{
4XH^2
}.
}
$$

Hence

$$
\boxed{
\sum_{j=0}^{J-1}
\frac{
\mathcal D_X(H_j)
}{
4XH_j^2
}
=
R_X(H_0)-R_X(H_J).
}
$$

This is the additive octave budget.

By contrast, fixed power is governed by the multiplicative budget

$$
\boxed{
G_X(J)
=
\log
\frac{
R_X(H_0)
}{
R_X(H_J)
}.
}
$$

A large additive budget can be spent in a few early scales.

A fixed power requires a logarithmically large multiplicative budget.

---

# 9. Two-component countermodel

The failure of diagonal injection can be made explicit.

Let

$$
M_X
=
\sqrt{\log X}.
$$

Define a high-frequency component

$$
\boxed{
b_n
=
M_X(-1)^n
}
$$

on a long block.

Define a smooth cumulative drift

$$
A_\beta(x)
=
x^\beta,
\qquad
\frac12<\beta<1,
$$

and let its increment sequence be

$$
\boxed{
d_n
=
A_\beta(n)-A_\beta(n-1).
}
$$

Set

$$
\boxed{
a_n=b_n+d_n.
}
$$

---

# 10. Jump energy of the countermodel

The high-frequency component satisfies

$$
\sum_{n\asymp X}|b_n|^2
\asymp
X\log X.
$$

The drift derivative has

$$
d_n
\asymp
X^{\beta-1}
$$

on a dyadic physical block, so

$$
\sum_{n\asymp X}|d_n|^2
\asymp
X^{2\beta-1}
=
o(X\log X).
$$

Thus the microscopic jump energy is overwhelmingly carried by the oscillatory component:

$$
\boxed{
\sum|a_n|^2
\asymp
X\log X.
}
$$

---

# 11. Dyadic cancellation of the high-frequency component

For every even dyadic lag

$$
H=2^j,
\qquad
j\ge1,
$$

the interior block sum of $b_n$ vanishes exactly:

$$
\boxed{
\sum_{r=1}^{H}b_{x+r}=0
}
$$

whenever the complete interval lies in the support.

Only boundary translates contribute.

Thus at polynomial dyadic scales the oscillatory component may carry almost no bulk lag energy even though it carries essentially all microscopic jump energy.

---

# 12. Smooth drift dominates long-scale lag energy

For

$$
H=o(X),
$$

the drift block sum is

$$
\sum_{r=1}^{H}d_{x+r}
=
A_\beta(x+H)-A_\beta(x)
\asymp
H X^{\beta-1}
$$

for

$$
x\asymp X.
$$

Therefore

$$
\boxed{
\mathcal S_d(H)
\asymp
H^2X^{2\beta-1}.
}
$$

Its relative adjacent-block defect satisfies

$$
\boxed{
\frac{
\mathcal D_d(H)
}{
\mathcal S_d(H)
}
=
O_\beta
\left(
\frac{H^2}{X^2}
\right).
}
$$

Hence the smooth component is nearly critically locked.

For polynomial $H$ in a range where

$$
H X^{2\beta-1}
\gg
\log X,
$$

the smooth component can dominate the bulk lag energy while the high-frequency component still dominates $\sum|a_n|^2$.

---

# 13. Countermodel conclusion

The two-component construction simultaneously has:

```text
microscopic jump energy:
  X log X

polynomial-scale lag energy:
  dominated by smooth drift

polynomial-scale relative octave defect:
  tends to zero
```

Therefore:

## Theorem 13.1 — Jump-Energy / Long-Scale-Defect Separation

No deterministic theorem using only:

```text
large one-step jump energy;
finite support;
centering;
dyadic Haar resolution;
generic Littlewood–Paley theory
```

can force a fixed relative polynomial-scale octave defect.

Arithmetic information beyond the diagonal is necessary.

Create:

```text
O-RH-049
OCTAVE_ENERGY_LOCALIZATION_DEBT
status:
  CERTIFIED
```

Create:

```text
O-RH-050
HIGH_FREQUENCY_NOISE_PLUS_SMOOTH_DRIFT_COUNTERMODEL
status:
  CERTIFIED AS MECHANISM COUNTERMODEL
```

---

# 14. Interpretation for the RH branch

The two countermodel components mirror the two structural pieces already found in CSM_RH:

## High-frequency component

Models the large local jump energy of the prime sequence.

## Smooth drift

Models a persistent low-frequency explicit-formula mode such as

$$
x^\rho.
$$

Thus the diagonal identity cannot rule out a hypothetical off-axis zero mode.

The arithmetic octave route therefore loops back to the same low-frequency obstruction as the principal Fejer arc.

---

# 15. Track O1 — centered-prime diagonal injection

Result:

```text
EXACT ALL-SCALE INJECTION
  YES

POLYNOMIAL-SCALE RELATIVE GAP
  NO
```

The diagonal is fully accounted for by Theorem 4.1.

It does not prove PDSD.

---

# 16. Track O2 — sieve lower bound for octave defect

Sieve and rough-number methods can prove strong variance information for sifted sets, and asymptotic variance results are known for integers without small prime factors.

But for the prime sequence itself, unconditional short-interval variance asymptotics remain largely unknown.

Moreover, an absolute lower bound for $\mathcal D_X(H)$ is insufficient unless it is comparable to $\mathcal S_X(H)$.

No current sieve theorem identified in this audit provides the required fixed relative octave floor for primes.

Status:

```text
OPEN / NO PDSD BRIDGE FOUND
```

---

# 17. Track O3 — all-scale Hardy–Littlewood assembly

There are only

$$
O(\log X)
$$

dyadic scales.

Summing currently available arbitrary logarithmic prime-pair error bounds over all scales still produces arbitrary logarithmic or subpower precision.

The scale sum does not convert

$$
\log^{-A}X
$$

into a fixed

$$
X^{-\delta}.
$$

No additional all-scale cancellation theorem is currently available.

Status:

```text
SUBPOWER ONLY
```

---

# 18. Track O4 — spectral Littlewood–Paley prime energy

The exact Littlewood–Paley/Haar resolution is now certified by Theorem 4.1.

But the countermodel shows that total band energy can be concentrated in microscopic octaves while a smooth low-frequency component dominates polynomial lag energies.

Thus generic harmonic analysis cannot prove PDSD.

Status:

```text
EXACT IDENTITY CERTIFIED
RELATIVE POLYNOMIAL OCTAVE FLOOR OPEN
```

---

# 19. Track O5 — locking rigidity plus prime jumps

The exact jump identity

$$
A(n)-A(n-1)
=
\Lambda(n)-1
$$

provides

$$
X\log X
$$

one-step energy.

But the two-component countermodel shows that large jump energy can coexist with long-scale critical locking.

Therefore prime jumps alone do not contradict locking.

One needs arithmetic information coupling microscopic prime jumps to low-frequency polynomial scales.

Status:

```text
DETERMINISTIC VERSION CLOSED
ARITHMETIC COUPLING VERSION OPEN
```

---

# 20. Comparison with known variance technology

The status is consistent with current literature.

The short-interval prime variance is strongly tied to RH, zero pair correlation, and Hardy–Littlewood prime correlations.

Unconditional asymptotics for this variance remain poorly understood.

Unconditional lower bounds for related arithmetic-progression variance can be obtained by circle-method minor-arc methods, but that geometry does not by itself supply the required relative low-frequency octave floor for the present short-interval target.

Thus current variance lower-bound technology does not close PDSD.

---

# 21. New certified identity

Create:

```text
B-RH-002
DYADIC_HAAR_JUMP_ENERGY_RESOLUTION
status:
  CERTIFIED
```

Statement:

$$
\boxed{
\sum_{j=0}^{\infty}
\frac{
\mathcal D(2^j)
}{
4^{j+1}
}
=
\sum_n|a_n|^2.
}
$$

This is a useful structural bridge.

It is not a fixed-power theorem.

---

# 22. PDSD status correction

PDSD remains mathematically valid as a sufficient fixed-power generator.

Campaign 22 shows:

```text
PDSD
  cannot be obtained from diagonal jump energy alone

PDSD
  requires true low-frequency arithmetic decorrelation
```

Therefore PDSD remains:

```text
F-RH-017
OPEN / STRONG SUFFICIENT PRIME-SIDE MECHANISM
```

but is no longer treated as likely to follow from generic multiscale energy injection.

---

# 23. Return to the shortest target path

The audited scale route now requires a new theorem controlling the competition between:

```text
high-frequency prime noise
and
smooth low-frequency prime drift.
```

That is the same low-frequency obstruction already visible in MLEPG / principal Fejer analysis.

Therefore no shorter fixed-power route has been obtained.

The canonical root remains:

```text
F-RH-010
PESC
```

and the direct theorem candidate remains:

```text
F-RH-016
MLEPG
```

---

# 24. Campaign 23

The next campaign changes candidate family again.

```text
CSM_RH Campaign 23
PRIME_SIDE_FIXED_POWER_GENERATION_II
```

The scale-decorrelation shell is retained as optional, not primary.

New candidates must create arithmetic control that couples prime jumps to low frequencies.

---

# 25. Campaign 23 allowed tracks

## G2-1 — arithmetic low-frequency uncertainty

Prove a theorem specific to $\Lambda-1$ which prevents too much low-frequency concentration relative to its known jump energy.

Generic uncertainty principles do not count.

## G2-2 — prime correlation with a smooth self-generated drift

Assume a slowly varying component dominates the prime error and derive a contradiction using prime-pair or sieve information without passing through zero density.

## G2-3 — nonlinear short-interval energy transfer

Use higher moments or nonlinear identities to transfer microscopic prime variance into polynomial lag energy.

The transfer must have a fixed exponent.

## G2-4 — arithmetic progression variance to additive-scale transfer

Test whether unconditional lower bounds for von Mangoldt variance in arithmetic progressions can be combined with a new transference theorem to force polynomial octave energy.

The transfer theorem itself must be proved.

## G2-5 — direct PESC prime-sampling theorem

Return to the root endogenous self-sampling correlation and generate a new arithmetic estimate without another surrogate gate.

---

# 26. Campaign 23 rejection filters

Reject a candidate if:

## R1. It uses only the jump-energy identity B-RH-002.

## R2. It uses generic Littlewood–Paley or uncertainty theory without prime-specific arithmetic.

## R3. It assumes a short-interval variance asymptotic.

## R4. It assumes a fixed zero strip.

## R5. It produces only subpower precision.

## R6. It creates another equivalent target without a new estimate.

---

# 27. State transition

```text
CSM_RH v1.13
  ->
CSM_RH v1.14
```

with:

```text
Campaign 22
  CLOSED_AS_HAAR_RESOLUTION_AND_DIAGONAL_INJECTION_AUDIT

B-RH-002
  DYADIC_HAAR_JUMP_ENERGY_RESOLUTION
  CREATED / CERTIFIED

O-RH-049
  OCTAVE_ENERGY_LOCALIZATION_DEBT
  CREATED / CERTIFIED

O-RH-050
  HIGH_FREQUENCY_NOISE_PLUS_SMOOTH_DRIFT_COUNTERMODEL
  CREATED / CERTIFIED AS MECHANISM COUNTERMODEL

F-RH-017
  PDSD
  REMAINS OPEN / OPTIONAL STRONG SUFFICIENT MECHANISM

F-RH-016
  MLEPG
  REMAINS OPEN / DIRECT THEOREM CANDIDATE

F-RH-010
  PESC
  REMAINS OPEN / ROOT TARGET

Campaign 23
  PRIME_SIDE_FIXED_POWER_GENERATION_II
  READY
```

---

# 28. Final status

```text
RH = OPEN

PESC = OPEN

MLEPG = OPEN

PDSD = OPEN / OPTIONAL

DYADIC HAAR JUMP-ENERGY RESOLUTION = CERTIFIED

TOTAL PRIME OCTAVE ENERGY = LARGE

POLYNOMIAL-SCALE RELATIVE OCTAVE FLOOR = OPEN

DIAGONAL-INJECTION SHORTCUT = CLOSED

GENERIC LITTLEWOOD-PALEY SHORTCUT = CLOSED

NEXT CAMPAIGN = 23
```

The exact identity

$$
\boxed{
\sum_{j=0}^{\infty}
\frac{
\mathcal D_X(2^j)
}{
4^{j+1}
}
=
\sum_n|\Lambda(n)-1|^2
}
$$

shows that the prime sequence already contains abundant octave energy.

The unresolved issue is where that energy lives.

A fixed-power RH route needs prime-specific arithmetic which prevents the long-scale observable from being dominated by a smooth low-frequency drift.
