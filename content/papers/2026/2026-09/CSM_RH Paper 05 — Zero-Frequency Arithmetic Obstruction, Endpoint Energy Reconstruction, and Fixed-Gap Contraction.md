# CSM_RH Paper 05
## Zero-Frequency Arithmetic Obstruction, Endpoint Energy Reconstruction, and Fixed-Gap Contraction

**Project:** `CSM_RH`  
**Paper:** `05`  
**Version:** `v0.1`  
**Date:** `2026-09-05`  
**Parent state:** `CSM_RH v0.5 / Paper 04`  
**Campaign:** `04 — CENTERED_SIGNED_ARITHMETIC_CANCELLATION`  
**Status:** structural theorem / mechanism audit; not a proof or disproof of RH  
**中文標題：** CSM_RH 論文 05：零頻算術阻礙、端點能量重建與固定間隙收縮  
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

This paper does five things:

1. identifies CSSA as an exact zero-frequency value of a centered pair polynomial;
2. proves an endpoint-local energy reconstruction identity;
3. proves an exact paraproduct / energy-increment identity;
4. shows that generic harmonic-analysis and generic bilinear manipulations cannot by themselves create the missing fixed power;
5. replaces vague "find cancellation" language with a concrete sufficient mechanism: a fixed-gap arithmetic contraction.

No live GLM-5.3-Flash run is claimed.

---

# 1. Canonical signed frontier

Let

$$
a_n
=
\Lambda(n)-1
$$

and

$$
A(j)
=
\sum_{n\le j}a_n
=
\psi(j)-j.
$$

Define

$$
J_N
=
\sum_{j=N}^{2N-1}
A(j)^2.
$$

The endpoint multiplicity is

$$
w_N(r)
=
\begin{cases}
N,
&
1\le r\le N,
\\
2N-r,
&
N<r<2N,
\\
0,
&
r\ge2N.
\end{cases}
$$

For

$$
1\le h\le2N-2,
$$

define

$$
\mathcal C_N(h)
=
\sum_{n=h+1}^{2N-1}
w_N(n)a_na_{n-h},
$$

$$
W_N(h)
=
\sum_{n=h+1}^{2N-1}
w_N(n),
$$

and the singular-series-centered residual

$$
\mathcal R_N(h)
=
\mathcal C_N(h)
-
[
\mathfrak S(h)-1
]
W_N(h).
$$

The canonical centered signed aggregate is

$$
\boxed{
\mathcal A_N
=
\sum_{h=1}^{2N-2}
\mathcal R_N(h).
}
$$

The v3.5 arithmetic remainder identity is

$$
\boxed{
J_N
=
D_N
+
2\mathcal M_N
+
2\mathcal A_N,
}
$$

where

$$
D_N
=
\sum_{n<2N}
w_N(n)a_n^2
$$

and

$$
\mathcal M_N
=
\sum_{h=1}^{2N-2}
[
\mathfrak S(h)-1
]
W_N(h).
$$

Known deterministic estimates give

$$
D_N+\mathcal M_N
=
O(N^2\log N).
$$

---

# 2. Zero-frequency representation

Define

$$
F_N(\alpha)
=
\sum_{n<2N}
a_ne(n\alpha),
$$

$$
G_N(\alpha)
=
\sum_{n<2N}
w_N(n)a_ne(n\alpha),
$$

and

$$
M_N^+(\alpha)
=
\sum_{h=1}^{2N-2}
[
\mathfrak S(h)-1
]
W_N(h)e(h\alpha).
$$

Let

$$
P_+
$$

denote positive-frequency projection.

Define the centered pair polynomial

$$
\boxed{
H_N(\alpha)
=
P_+
[
G_N\overline{F_N}
]
-
M_N^+(\alpha).
}
$$

Then

$$
H_N(\alpha)
=
\sum_{h=1}^{2N-2}
\mathcal R_N(h)e(h\alpha).
$$

Therefore:

## Theorem 2.1 — CSSA is a zero-frequency value

$$
\boxed{
\mathcal A_N
=
H_N(0).
}
$$

At the decisive point

$$
\alpha=0,
$$

every additive phase is equal to one:

$$
e(h\alpha)=1.
$$

Hence any fixed-power cancellation at the CSSA level must arise from arithmetic cancellation in the coefficients themselves.

It cannot be obtained merely from oscillation of the external additive phase.

---

# 3. Sharp generic Fourier evaluation law

Let

$$
M=2N-2.
$$

For any trigonometric polynomial

$$
H(\alpha)
=
\sum_{h=1}^{M}
c_he(h\alpha),
$$

Parseval and Cauchy-Schwarz give

$$
|H(0)|
=
\left|
\sum_{h=1}^{M}c_h
\right|
\le
M^{1/2}
\left(
\sum_{h=1}^{M}|c_h|^2
\right)^{1/2}.
$$

Since

$$
\|H\|_2^2
=
\sum_{h=1}^{M}|c_h|^2,
$$

we have:

## Theorem 3.1

$$
\boxed{
|H(0)|
\le
M^{1/2}
\|H\|_2.
}
$$

This is sharp.

Take

$$
c_h=1
$$

for every $h$.

Then

$$
H(0)=M
$$

and

$$
\|H\|_2=M^{1/2},
$$

so equality holds.

Therefore no coefficient-blind harmonic-analysis theorem can improve the generic

$$
N^{1/2}
$$

loss between the shift- $L^2$ gate and CSSA.

Any improvement must use arithmetic structure of the coefficients

$$
\mathcal R_N(h).
$$

---

# 4. Endpoint-local centered residual

For

$$
h<j,
$$

define

$$
Q_j(h)
=
\sum_{n=h+1}^{j}
a_na_{n-h}
-
[
\mathfrak S(h)-1
]
(j-h).
$$

The v3.5 endpoint decomposition gives

$$
\mathcal R_N(h)
=
\sum_{j=N}^{2N-1}
\mathbf 1_{h<j}
Q_j(h).
$$

Define the all-shift endpoint aggregate

$$
\boxed{
\mathcal B(j)
=
\sum_{h=1}^{j-1}
Q_j(h).
}
$$

Then

$$
\boxed{
\mathcal A_N
=
\sum_{j=N}^{2N-1}
\mathcal B(j).
}
$$

---

# 5. Endpoint energy reconstruction

Let

$$
L(j)
=
\sum_{n\le j}
a_n^2
$$

and

$$
\mathcal M(j)
=
\sum_{h=1}^{j-1}
[
\mathfrak S(h)-1
]
(j-h).
$$

Now

$$
\sum_{h=1}^{j-1}
\sum_{n=h+1}^{j}
a_na_{n-h}
=
\sum_{1\le m<n\le j}
a_ma_n.
$$

Using

$$
A(j)^2
=
L(j)
+
2
\sum_{1\le m<n\le j}
a_ma_n,
$$

we obtain:

## Theorem 5.1 — Endpoint-local energy identity

$$
\boxed{
\mathcal B(j)
=
\frac12A(j)^2
-
\frac12L(j)
-
\mathcal M(j).
}
$$

Since

$$
A(j)=\psi(j)-j,
$$

this becomes

$$
\boxed{
\mathcal B(j)
=
\frac12
(\psi(j)-j)^2
-
\frac12
\sum_{n\le j}
(\Lambda(n)-1)^2
-
\mathcal M(j).
}
$$

The standard diagonal estimate and Cesàro singular-series estimate give

$$
L(j)
=
O(j\log j)
$$

and

$$
\mathcal M(j)
=
O(j\log j).
$$

Therefore:

$$
\boxed{
\mathcal B(j)
=
\frac12
(\psi(j)-j)^2
+
O(j\log j).
}
$$

This is stronger structural information than a global signed identity.

After all shifts are centered and summed at one endpoint, the result already reconstructs a positive PNT-error energy, up to a deterministic lower-order correction.

---

# 6. Boundary-term cancellation in the standard pair-error interface

Let

$$
r_j(h)
=
\psi_2(j,h)
-
\mathfrak S(h)(j-h)
$$

and

$$
E(j)
=
\psi(j)-j.
$$

The exact v3.5 interface is

$$
Q_j(h)
=
r_j(h)
-
E(j)
-
E(j-h)
+
E(h).
$$

Summing over

$$
1\le h<j
$$

gives

$$
\sum_{h=1}^{j-1}
E(j-h)
=
\sum_{h=1}^{j-1}
E(h).
$$

Hence these two boundary sums cancel exactly, and:

## Theorem 6.1

$$
\boxed{
\mathcal B(j)
=
\sum_{h=1}^{j-1}
r_j(h)
-
(j-1)E(j).
}
$$

Thus the standard Hardy-Littlewood pair-error sum and the linear PNT boundary correction combine into the same endpoint energy object.

This prevents a proof from treating the two pieces as independent random errors.

---

# 7. Exact paraproduct representation

The raw positive-shift aggregate satisfies

$$
\sum_{h=1}^{2N-2}
\mathcal C_N(h)
=
\sum_{1\le m<n<2N}
w_N(n)a_na_m.
$$

Since

$$
A(n-1)
=
\sum_{m<n}a_m,
$$

we obtain:

## Theorem 7.1 — Zero-frequency prime paraproduct

$$
\boxed{
\sum_{h=1}^{2N-2}
\mathcal C_N(h)
=
\sum_{n=2}^{2N-1}
w_N(n)a_nA(n-1).
}
$$

Therefore CSSA has the exact bilinear form

$$
\boxed{
\mathcal A_N
=
\sum_{n=2}^{2N-1}
w_N(n)
(\Lambda(n)-1)
(
\psi(n-1)-(n-1)
)
-
\mathcal M_N.
}
$$

This is the canonical zero-frequency bilinear interface.

---

# 8. Energy-increment conservation

Because

$$
A(n)
=
A(n-1)+a_n,
$$

we have

$$
A(n)^2-A(n-1)^2
=
2a_nA(n-1)+a_n^2.
$$

Using the endpoint multiplicity weight and discrete summation by parts gives the exact identity

$$
\sum_{n<2N}
w_N(n)
[
A(n)^2-A(n-1)^2
]
=
J_N.
$$

Therefore:

## Theorem 8.1 — Paraproduct energy conservation

$$
\boxed{
2
\sum_{n=2}^{2N-1}
w_N(n)a_nA(n-1)
=
J_N-D_N.
}
$$

So the bilinear form exposed in Section 7 is not generically orthogonal.

It is the discrete energy increment of the PNT error.

A proposal of the form

```text
prime increment a_n
should be approximately independent of
past cumulative error A(n-1)
```

cannot be accepted as a cancellation principle without new arithmetic content.

Globally, their weighted correlation reconstructs the positive energy.

---

# 9. Exact mean-square strength calibration

Let

$$
\Theta_\zeta
=
\sup_\rho\Re\rho.
$$

A 2025 mean-square result recalled by Zhao states:

if

$$
\Theta_\zeta=\frac12,
$$

then

$$
\int_X^{2X}
(\psi(x)-x)^2dx
\asymp
X^2,
$$

while if

$$
\Theta_\zeta>\frac12,
$$

then for every

$$
\varepsilon>0,
$$

$$
X^{2\Theta_\zeta+1-\varepsilon}
\ll
\int_X^{2X}
(\psi(x)-x)^2dx
\ll
X^{2\Theta_\zeta+1}.
$$

Combined with the discrete-continuous exponent bridge, this confirms:

for

$$
\Theta_\zeta>\frac12,
$$

the signed CSSA itself has the same power exponent as

$$
N^{1+2\Theta_\zeta},
$$

because the deterministic

$$
O(N^2\log N)
$$

correction is lower order.

Thus an off-critical supremum cannot be hidden by shift signs.

At the RH endpoint, CSSA has the required upper exponent

$$
2+o(1),
$$

which is sufficient for the RH-equivalence calibration established in Paper 04.

---

# 10. Campaign 04 mechanism audit

## C04-A — Signed dispersion after exact centering

Generic dispersion converts CSSA into an $L^2$ object.

Theorem 3.1 shows the resulting

$$
N^{1/2}
$$

evaluation loss is sharp without arithmetic coefficient information.

Status:

```text
GENERIC VERSION REJECTED
ARITHMETIC-SPECIFIC VERSION MAY SURVIVE
```

---

## C04-B — Vaughan / Heath-Brown bilinear decomposition

At

$$
\alpha=0,
$$

external additive oscillation is absent.

A multiplicative decomposition of $\Lambda$ may still expose Möbius, divisor, or bilinear cancellation.

However such a route must produce new cancellation in the arithmetic coefficients themselves.

Status:

```text
SURVIVES ONLY AS NEW MULTIPLICATIVE CANCELLATION
```

No fixed-power theorem is proved here.

---

## C04-C — Endpoint-kernel bilinear cancellation

Theorem 8.1 shows the raw endpoint-weighted bilinear form is exactly an energy increment.

Coefficient-blind bilinear orthogonality therefore cannot be the missing theorem.

Status:

```text
GENERIC VERSION REJECTED
```

---

## C04-D — Dyadic scale telescoping

Signed combinations across scales may cancel zero contributions.

But such a transformed estimate does not control CSSA at each scale unless a stable inverse / target-fidelity theorem is proved.

If the inverse is lossless at fixed exponent, `O-RH-007 TARGET_STRENGTH_CONSERVATION` applies.

Status:

```text
DEFERRED
TARGET_FIDELITY_DEBT
```

---

## C04-E — Centered Fourier zero-frequency attack

The exact target is

$$
H_N(0).
$$

Minor-arc and generic phase-cancellation methods operate away from the zero frequency.

Theorem 3.1 shows that generic recovery of the zero value from $L^2$ data is already sharp.

Status:

```text
GENERIC HARMONIC VERSION REJECTED
```

---

## C04-F — Certified principal-subterm cancellation

This remains the genuine survivor.

The cancellation must be forced by arithmetic structure such as:

```text
multiplicative convolution
reciprocity
exact algebraic pairing
a quantitative Selberg-type contraction
a new bilinear estimate at zero frequency
or another noncircular arithmetic mechanism
```

Status:

```text
SURVIVOR
```

---

# 11. New obstruction: zero-frequency arithmetic barrier

Create:

```text
O-RH-008
ZERO_FREQUENCY_ARITHMETIC_OBSTRUCTION
status:
  CERTIFIED
```

Statement:

> The canonical CSSA target is the zero-frequency value of the centered pair polynomial. Generic additive-phase oscillation, minor-arc estimates, or coefficient-blind harmonic analysis cannot supply the required fixed power. Any successful estimate must exploit arithmetic structure of the centered coefficients.

This obstruction does not say that CSSA is impossible to prove.

It types the source of any possible proof.

---

# 12. New obstruction: energy-increment circularity

Create:

```text
O-RH-009
ENERGY_INCREMENT_CIRCULARITY
status:
  CERTIFIED
```

Statement:

> The canonical zero-frequency bilinear form between the prime increment and the cumulative PNT error is exactly half the PNT mean-square energy minus the diagonal. A bilinear estimate which assumes generic decorrelation between these two factors is not a valid independent input.

The exact certificate is

$$
2
\sum_n
w_N(n)a_nA(n-1)
=
J_N-D_N.
$$

---

# 13. What a successful next mechanism must look like

The surviving mechanism must not merely rewrite

$$
J_N.
$$

It must produce a noncircular arithmetic contraction.

One useful sufficient format is developed next.

---

# 14. Fixed-Gap Arithmetic Contraction

Define the normalized CSSA size

$$
\boxed{
X(N)
=
\frac{
|\mathcal A_N|
}{
N^3
}.
}
$$

Suppose an arithmetic decomposition proves, for fixed constants

$$
0<\theta<1,
\qquad
0<\lambda<1,
\qquad
\kappa_0>0,
$$

that for all sufficiently large $N$,

$$
\boxed{
X(N)
\le
\lambda X(\theta N)
+
C N^{-\kappa_0}.
}
$$

Integer rounding of $\theta N$ is harmless and suppressed in the notation.

---

# 15. Contraction theorem

## Theorem 15.1 — Fixed gap implies a fixed power

Under the recurrence in Section 14,

$$
\boxed{
X(N)
=
O(N^{-\kappa}),
}
$$

where one may take

$$
\boxed{
\kappa
=
\min
\left(
\kappa_0,
\frac{
-\log\lambda
}{
\log(1/\theta)
}
\right)
}
$$

up to an arbitrarily small endpoint loss when the two exponents coincide.

Consequently,

$$
\boxed{
|\mathcal A_N|
=
O(N^{3-\kappa+o(1)}).
}
$$

### Proof

Iterate $j$ times:

$$
X(N)
\le
\lambda^j
X(\theta^jN)
+
C
N^{-\kappa_0}
\sum_{i=0}^{j-1}
\lambda^i
\theta^{-i\kappa_0}.
$$

Choose $j$ so that

$$
\theta^jN
$$

is bounded.

The initial term has size

$$
\lambda^j
=
N^{-\delta+o(1)},
$$

where

$$
\delta
=
\frac{
-\log\lambda
}{
\log(1/\theta)
}.
$$

If

$$
\lambda\theta^{-\kappa_0}<1,
$$

the geometric sum is bounded and contributes

$$
O(N^{-\kappa_0}).
$$

If

$$
\lambda\theta^{-\kappa_0}>1,
$$

the last geometric term dominates and contributes

$$
O(N^{-\delta}).
$$

At equality there is only an additional logarithmic factor.

Hence

$$
X(N)
=
O
\left(
N^{-\min(\kappa_0,\delta)+o(1)}
\right).
$$

 $\square$

---

# 16. Why the contraction target is useful

Theorem 15.1 does not reduce theorem strength.

A fixed gap would itself be breakthrough mathematics.

But it changes the worker target from:

```text
prove a mysterious global N^(3-kappa) estimate
```

to:

```text
derive one arithmetic self-improvement step with a fixed contraction gap
```

This is structurally closer to successful iterative arguments in analytic and elementary prime number theory.

The fixed condition

$$
\lambda<1
$$

is essential.

A critical recurrence with effective coefficient one may prove decay slower than every fixed power and therefore does not close CSSA $(\kappa)$.

---

# 17. New survivor

Create:

```text
S-RH-010
ZERO_FREQUENCY_MULTIPLICATIVE_CANCELLATION
status:
  OPEN / SURVIVOR
```

and:

```text
S-RH-011
FIXED_GAP_ARITHMETIC_CONTRACTION
status:
  OPEN / SURVIVOR
```

The first describes where cancellation must come from.

The second gives a concrete sufficient shape for that cancellation.

---

# 18. Campaign 05

The next campaign is:

```text
CSM_RH Campaign 05
ZERO_FREQUENCY_MULTIPLICATIVE_CONTRACTION
```

It has two coupled tracks.

## Track M — multiplicative decomposition

Use an exact identity for $\Lambda$ such as Vaughan, Heath-Brown, Selberg, or another verified convolution decomposition.

The worker must preserve the zero-frequency signed target.

Goal:

```text
derive arithmetic cancellation before
triangle inequality / squaring destroys the sign structure
```

## Track C — contraction extraction

From the multiplicative decomposition, attempt to derive

$$
X(N)
\le
\lambda X(\theta N)
+
O(N^{-\kappa_0})
$$

with a fixed

$$
\lambda<1.
$$

The contraction parameters must be explicit.

---

# 19. Campaign 05 rejection filters

Reject a candidate if:

## R1

The only saving comes from

$$
e(n\alpha)
$$

with

$$
\alpha\neq0.
$$

The target is at $\alpha=0$.

## R2

It uses generic $L^2$ interpolation and silently assumes a gain beyond the sharp

$$
N^{1/2}
$$

evaluation norm.

## R3

It assumes

$$
a_n
$$

and

$$
A(n-1)
$$

are decorrelated without overcoming Theorem 8.1.

## R4

Its recurrence has

$$
\lambda=1
$$

and no other fixed-power mechanism.

## R5

Its remainder is only logarithmically smaller.

## R6

It uses a fixed zeta zero strip as an input.

## R7

It converts a finite numerical contraction into a global theorem.

---

# 20. Current external calibration

Current literature supports the obstruction classification.

A 2025 peer-reviewed mean-square result records that, writing

$$
\Theta_\zeta
=
\sup_\rho\Re\rho,
$$

the dyadic PNT mean square has power scale

$$
X^{1+2\Theta_\zeta}
$$

up to an arbitrary epsilon in the lower bound when

$$
\Theta_\zeta>\frac12,
$$

and is of order

$$
X^2
$$

when

$$
\Theta_\zeta=\frac12.
$$

The 2026 Maynard-Pandey-Radziwiłł exponential-sum theorem gives

$$
\left|
\sum_{n<N}
\Lambda(n)e(n\alpha)
\right|
\le
N^{o(1)}
\left(
\frac{N}{B^{1/2}}
+
N^{19/24}
\right).
$$

At the principal core

$$
q=1,
\qquad
\alpha=\frac{u}{N},
\qquad
u=O(1),
$$

one has

$$
B=O(1),
$$

so the first term remains at the unsaved $N$ scale.

This is consistent with the zero-frequency obstruction.

Recent work on zero-free regions and PNT error terms also continues to translate known shrinking zero-free contours into subpower, rather than fixed-power, prime-number-theorem error terms.

---

# 21. State transition

The canonical transition is:

```text
CSM_RH v0.5
  ->
CSM_RH v0.6
```

with:

```text
Campaign 04
  STATUS:
    STRUCTURAL AUDIT CLOSED
    FIXED-POWER PROOF NOT OBTAINED

O-RH-008
  ZERO_FREQUENCY_ARITHMETIC_OBSTRUCTION
  CREATED / CERTIFIED

O-RH-009
  ENERGY_INCREMENT_CIRCULARITY
  CREATED / CERTIFIED

S-RH-010
  ZERO_FREQUENCY_MULTIPLICATIVE_CANCELLATION
  CREATED / OPEN

S-RH-011
  FIXED_GAP_ARITHMETIC_CONTRACTION
  CREATED / OPEN

Campaign 05
  ZERO_FREQUENCY_MULTIPLICATIVE_CONTRACTION
  READY
```

---

# 22. Final status

```text
RH = OPEN

CSSA FIXED POWER = OPEN

GENERIC FOURIER BYPASS = CLOSED / NO

GENERIC L2-TO-POINT IMPROVEMENT = CLOSED / SHARP

GENERIC PRIME-INCREMENT / PNT-ERROR DECORRELATION = CLOSED / NO

ZERO-FREQUENCY MULTIPLICATIVE CANCELLATION = OPEN

FIXED-GAP ARITHMETIC CONTRACTION = OPEN

NEXT CAMPAIGN = 05
```

The two central exact identities are:

$$
\boxed{
\mathcal A_N
=
H_N(0)
}
$$

and

$$
\boxed{
2
\sum_n
w_N(n)
(\Lambda(n)-1)
(
\psi(n-1)-(n-1)
)
=
J_N-D_N.
}
$$

The next mathematical problem is therefore not to manufacture more additive oscillation.

It is to discover a genuine arithmetic contraction at zero frequency.
