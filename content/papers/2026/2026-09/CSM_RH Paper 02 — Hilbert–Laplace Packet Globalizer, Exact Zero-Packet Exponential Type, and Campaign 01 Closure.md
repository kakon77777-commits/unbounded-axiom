# CSM_RH Paper 02
## Hilbert–Laplace Packet Globalizer, Exact Zero-Packet Exponential Type, and Campaign 01 Closure

**Project:** `CSM_RH`  
**Paper:** `02`  
**Version:** `v0.1`  
**Date:** `2026-09-04`  
**Parent:** `CSM_RH Paper 01`  
**Status:** structural theorem / frontier audit; not a proof or disproof of RH  
**中文標題：** CSM_RH 論文 02：Hilbert–Laplace 封包全域化算子、精確零點封包指數型與 Campaign 01 閉合  
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
ROOT_STATUS = OPEN
```

This paper proves a narrower structural result:

> For the smooth $q=1$ major-arc zeta-zero packet used in the v3.18 architecture, zero-zero interference cannot lower the packet's exponential growth type below the supremal real part of the zeta zeros.

Consequently, the pointwise packet-isolation lower bound proposed in Paper 01 is not needed for the fixed-exponent strength audit of EMAE.

The arithmetic EMAE upper bound itself remains open.

No live GLM-5.3-Flash provider run is claimed in this package.

---

# 1. Canonical correction: GLM is a worker/provider, not the protocol

Paper 01 introduced the names:

```text
GLM_Backward Search
Goal-Led Meta-Research
```

as if `GLM` were the name of the mathematical research protocol.

That naming was not canonical and is withdrawn.

The canonical architecture is:

```text
CSM_RH
  = closure-space mathematics protocol / state space

GLM-5.3-Flash
  = replaceable high-volume worker/provider implementation

roles
  = Designer / Builder / Verifier

frontier model
  = residual-risk judge / final promotion authority
```

Therefore:

$$
\boxed{
\mathrm{GLM}
\neq
\mathrm{Protocol}.
}
$$

`Campaign 01` is henceforth a `CSM_RH worker campaign`.

GLM-5.3-Flash is a preferred current worker model for that campaign, not the semantic identity of the campaign itself.

---

# 2. Campaign 01 target

Paper 01 created:

```text
S-RH-007
LOSSLESS_WITNESS_GLOBALIZER
```

with the goal of converting an off-critical zero witness into a global invariant which cannot be erased by aggregation.

The principal open instances were:

```text
O-RH-005-W
WEIL_AGGREGATION_ISOLATION

O-RH-005-M
MAJOR_ARC_AGGREGATION_ISOLATION
```

Campaign 01 generated and audited several candidate families.

The principal survivor is:

```text
C-RH-GLB-01
HILBERT_LAPLACE_PACKET_GLOBALIZER
abbrev: HLPG
```

It applies directly to the smooth $q=1$ major-arc zero packet.

---

# 3. Candidate batch

The campaign-level candidates are:

```text
C-RH-GLB-01
HILBERT_LAPLACE_PACKET_GLOBALIZER
status: SURVIVES / PROVED_AT_PACKET_TYPE_LEVEL

C-RH-GLB-02
FEJER_BOHR_LOGTIME_AVERAGING
status: DEPRIORITIZED
reason: amplitude-drift normalization debt; HLPG is stronger and cleaner

C-RH-GLB-03
POSITIVE_RESOLVENT_REWEIGHTING
status: REJECTED_AS_REPRESENTATION_ONLY
reason: earlier positive-kernel audits already show no fixed-exponent discount

C-RH-GLB-04
FINITE_INTERVAL_SUZUKI_SPECTRAL_LIMIT
status: DEFERRED
reason: relevant modern operator framework exists, but its infinite-interval spectral limit is conjectural

C-RH-GLB-05
DENSITY_WEIGHTED_EXTREME_ZERO_SUPPRESSION
status: REJECTED_BY_O-RH-003
reason: density alone does not exclude a single extreme zero

C-RH-GLB-06
RANDOM_PHASE_PACKET_ORTHOGONALIZATION
status: DEFERRED
reason: creates observable-transfer and arithmetic-realizability debt
```

Only `C-RH-GLB-01` is promoted to a theorem route in this paper.

---

# 4. Smooth major-arc kernel

Let

$$
w\in C_c^\infty((0,\infty))
$$

be nonzero, and fix

$$
U>0.
$$

For

$$
s\in\mathbb C
$$

and

$$
u\in[-U,U],
$$

define

$$
\mathcal W_s(u)
=
\int_0^\infty
w(v)e(uv)v^{s-1}\,dv.
$$

For

$$
x=e^T
$$

and

$$
\epsilon=\frac{u}{x},
$$

the exact scaling is

$$
W_{x,u/x}(s)
=
e^{sT}\mathcal W_s(u).
$$

---

# 5. Hilbert packet space

Define the Hilbert space

$$
\mathcal H_{w,U}
=
L^2
\left(
[-U,U],
|\mathcal W_1(u)|^2du
\right).
$$

For each nontrivial zeta zero $\rho$, define the coefficient vector

$$
v_\rho(u)
=
\mathcal W_\rho(u).
$$

Its squared Hilbert norm is

$$
\|v_\rho\|_{\mathcal H_{w,U}}^2
=
\int_{-U}^{U}
|\mathcal W_1(u)|^2
|\mathcal W_\rho(u)|^2du.
$$

This is exactly the zero cross-kernel coefficient

$$
C_{w,U}(\rho).
$$

The v3.18 kernel theorem gives

$$
\boxed{
\|v_\rho\|_{\mathcal H_{w,U}}^2
=
C_{w,U}(\rho)
>
0.
}
$$

Thus every nontrivial zero has a nonzero Hilbert coefficient.

---

# 6. Rapid vertical decay

Write

$$
s=\sigma+i\gamma,
\qquad
0\le\sigma\le1.
$$

Set

$$
v=e^y.
$$

Then

$$
\mathcal W_{\sigma+i\gamma}(u)
=
\int_{\mathbb R}
w(e^y)e^{\sigma y}e(ue^y)e^{i\gamma y}\,dy.
$$

Because $w$ has compact support inside $(0,\infty)$, the function

$$
y
\mapsto
w(e^y)e^{\sigma y}e(ue^y)
$$

is smooth and compactly supported in a fixed interval, uniformly for

$$
0\le\sigma\le1,
\qquad
|u|\le U.
$$

Repeated integration by parts therefore gives:

## Lemma 6.1 — Uniform rapid vertical decay

For every integer

$$
N\ge0,
$$

there exists

$$
C_N=C_N(w,U)
$$

such that

$$
\boxed{
\sup_{\substack{
0\le\sigma\le1\\
|u|\le U
}}
|
\mathcal W_{\sigma+i\gamma}(u)
|
\le
C_N
(1+|\gamma|)^{-N}.
}
$$

The same estimate holds for

$$
\|v_{\sigma+i\gamma}\|_{\mathcal H_{w,U}}.
$$

---

# 7. Absolute summability over zeta zeros

Let

$$
N_\zeta(Y)
$$

count nontrivial zeta zeros up to height $Y$, with multiplicity.

The classical zero-counting estimate gives

$$
N_\zeta(Y)
=
O(Y\log Y).
$$

Combining this with Lemma 6.1, choose $N$ sufficiently large to obtain

$$
\boxed{
\sum_{\rho}
\|v_\rho\|_{\mathcal H_{w,U}}
<
\infty.
}
$$

Therefore the zero packet below is absolutely convergent in $\mathcal H_{w,U}$ on every compact $T$ -interval.

---

# 8. Hilbert-valued zero packet

Define

$$
F(T)
=
\sum_{\rho}
e^{\rho T}v_\rho,
\qquad
T\ge0.
$$

Define the rightmost-zero abscissa

$$
\Theta_\zeta
=
\sup_\rho
\Re\rho.
$$

By symmetry,

$$
\Theta_\zeta
=
\frac12+\Delta_\zeta.
$$

The easy upper estimate is

$$
\|F(T)\|
\le
\sum_\rho
e^{(\Re\rho)T}
\|v_\rho\|
\le
e^{\Theta_\zeta T}
\sum_\rho
\|v_\rho\|.
$$

Hence

$$
\boxed{
\|F(T)\|
=
O(e^{\Theta_\zeta T}).
}
$$

The issue is whether zero-zero interference can improve this exponent.

The next theorem says no.

---

# 9. Hilbert–Laplace coefficient recovery

Define the packet type

$$
\tau_F
=
\inf
\left\{
a\in\mathbb R:
\|F(T)\|
=
O(e^{aT})
\right\}.
$$

## Theorem 9.1 — Exact Hilbert packet type

$$
\boxed{
\tau_F
=
\Theta_\zeta.
}
$$

### Proof

The upper bound

$$
\tau_F\le\Theta_\zeta
$$

was established in Section 8.

Assume for contradiction that

$$
\tau_F<\Theta_\zeta.
$$

Choose

$$
a
$$

such that

$$
\tau_F<a<\Theta_\zeta.
$$

Then

$$
\|F(T)\|
=
O(e^{aT}).
$$

Therefore the Bochner-valued Laplace transform

$$
\widehat F(s)
=
\int_0^\infty
e^{-sT}F(T)\,dT
$$

is holomorphic in the half-plane

$$
\Re s>a.
$$

For

$$
\Re s>\Theta_\zeta,
$$

absolute convergence permits termwise integration:

$$
\widehat F(s)
=
\sum_\rho
\frac{v_\rho}{s-\rho}.
$$

By the rapid decay from Lemma 6.1, the series

$$
\sum_\rho
\frac{v_\rho}{s-\rho}
$$

converges locally normally on compact subsets avoiding the zeta zeros.

Hence it defines an $\mathcal H_{w,U}$ -valued meromorphic function whose residue at a zero $\rho_0$ of multiplicity $m(\rho_0)$ is

$$
m(\rho_0)v_{\rho_0}.
$$

Because

$$
a<\Theta_\zeta,
$$

there exists a zero $\rho_0$ with

$$
\Re\rho_0>a.
$$

The coefficient non-annihilation theorem gives

$$
v_{\rho_0}\neq0.
$$

Choose a continuous linear functional

$$
\ell
\in
\mathcal H_{w,U}^\ast
$$

such that

$$
\ell(v_{\rho_0})\neq0.
$$

Then

$$
\ell(\widehat F(s))
$$

is holomorphic for

$$
\Re s>a,
$$

but on

$$
\Re s>\Theta_\zeta
$$

it equals

$$
\sum_\rho
\frac{
\ell(v_\rho)
}{
s-\rho
}.
$$

The latter has a nonremovable pole at $\rho_0$ with nonzero residue

$$
m(\rho_0)\ell(v_{\rho_0}).
$$

By uniqueness of analytic continuation this is impossible, because $\rho_0$ lies inside the holomorphy half-plane

$$
\Re s>a.
$$

Therefore

$$
\tau_F\ge\Theta_\zeta.
$$

Combining both inequalities gives

$$
\boxed{
\tau_F=\Theta_\zeta.
}
$$

 $\square$

---

# 10. Interpretation

Theorem 9.1 is the major-arc analogue of the successful fixed-aperture singularity-separation mechanism.

The key fact is:

> Cross terms may cancel at individual scales, but they cannot erase a nonzero exponential coefficient from the analytic Laplace resolvent.

Thus:

```text
POINTWISE PACKET INTERFERENCE
does not imply
EXPONENTIAL-TYPE INTERFERENCE.
```

No literal rightmost zero is required.

If the supremum is not attained, the proof chooses a zero with

$$
\Re\rho>a
$$

for every

$$
a<\Theta_\zeta.
$$

---

# 11. Positive packet energy

The $q=1$ pole-zero packet energy on the core arc is

$$
\mathcal E_1(e^T;U)
=
e^T
\|F(T)\|_{\mathcal H_{w,U}}^2.
$$

Define

$$
\tau_E
=
\inf
\left\{
b:
\mathcal E_1(e^T;U)
=
O(e^{bT})
\right\}.
$$

## Theorem 11.1 — Exact $q=1$ packet-energy type

$$
\boxed{
\tau_E
=
1+2\Theta_\zeta.
}
$$

### Proof

Theorem 9.1 gives the upper estimate immediately.

Conversely, if

$$
\mathcal E_1(e^T;U)
=
O(e^{bT}),
$$

then

$$
\|F(T)\|
=
O
\left(
e^{(b-1)T/2}
\right).
$$

Theorem 9.1 therefore forces

$$
\Theta_\zeta
\le
\frac{b-1}{2}.
$$

Hence

$$
b
\ge
1+2\Theta_\zeta.
$$

 $\square$

Using

$$
\Theta_\zeta
=
\frac12+\Delta_\zeta,
$$

we also have

$$
\boxed{
\tau_E
=
2+2\Delta_\zeta.
}
$$

---

# 12. Closure of the growth-type MZI debt

Paper 01 introduced

```text
F-RH-004
MAJOR_ZERO_PACKET_ISOLATION
```

because the isolated pole-zero channel

$$
x^{1+2\Re\rho}
$$

was not known to give a pointwise lower bound for the full packet.

Paper 02 splits that frontier.

## F-RH-004A

```text
POINTWISE_MAJOR_ZERO_PACKET_LOWER_ENVELOPE
status: OPEN
priority: DEPRIORITIZED
```

This is the old pointwise MZI form.

## F-RH-004B

```text
MAJOR_ZERO_PACKET_EXPONENTIAL_TYPE
status: CLOSED
certificate: Theorem 11.1
```

The fixed-exponent strength audit needs `F-RH-004B`, not `F-RH-004A`.

Therefore the major-arc aggregation-isolation barrier is closed at exponential-type level.

Canonical transition:

```text
O-RH-005-M
MAJOR_ARC_AGGREGATION_ISOLATION
OPEN
->
CLOSED_AT_EXPONENTIAL_TYPE
```

---

# 13. EMAE strength is now certified

Recall the positive character major-arc energy gate

$$
\operatorname{EMAE}(\eta):
\qquad
\mathfrak Z_2(x;Q,U)
+
\mathfrak Z_4(x;Q,U)
\ll
x^{3-\eta+o(1)}.
$$

The $q=1$ contribution is a nonnegative term of

$$
\mathfrak Z_2.
$$

Therefore EMAE implies

$$
\mathcal E_1(x;U)
\ll
x^{3-\eta+o(1)}.
$$

Theorem 11.1 gives

$$
1+2\Theta_\zeta
\le
3-\eta.
$$

Hence:

## Corollary 13.1 — Fixed-strip consequence of EMAE

If

$$
\operatorname{EMAE}(\eta)
$$

holds for a fixed

$$
\eta>0,
$$

then

$$
\boxed{
\Theta_\zeta
\le
1-\frac{\eta}{2}.
}
$$

Equivalently,

$$
\boxed{
\Delta_\zeta
\le
\frac12-\frac{\eta}{2}.
}
$$

Thus every fixed positive $\eta$ yields a fixed zero-strip breakthrough.

If

$$
\eta=1,
$$

then

$$
\Theta_\zeta\le\frac12.
$$

By functional-equation symmetry,

$$
\Theta_\zeta\ge\frac12,
$$

so

$$
\Theta_\zeta=\frac12,
$$

which is RH.

Therefore:

```text
EMAE(eta>0)
  = at least S2 fixed-zero-strip strength

EMAE(1)
  = S3 RH-level strength
```

This is now a certified structural implication, not a single-zero dominance heuristic.

---

# 14. What has and has not been solved

## Closed

```text
C1
smooth zero coefficients are rapidly summable

C2
every zero has nonzero Hilbert coefficient

C3
full q=1 zero packet has exact exponential type Theta_zeta

C4
packet interference cannot reduce exponential type

C5
q=1 pole-zero energy has exact type 1 + 2 Theta_zeta

C6
EMAE fixed-power strength audit is certified
```

## Still open

```text
G1
prove EMAE(eta) for any fixed eta > 0

G2
derive a genuinely new arithmetic cancellation theorem strong enough for G1

G3
close the Weil constructive isolation frontier if that branch remains active

G4
prove the RH-scale eta = 1 major-arc energy bound

G5
RH
```

The campaign has removed a representation/globalization uncertainty.

It has not supplied the missing arithmetic fixed-power saving.

---

# 15. Why this is not another RH-equivalent representation loop

Theorem 11.1 alone does not assert

$$
\Theta_\zeta=\frac12.
$$

It identifies the exact exponent encoded by a pre-existing positive packet energy.

The new closure gain is:

```text
before:
  full packet interference could invalidate the isolated-channel strength audit

after:
  full packet exponential type is exactly known
```

This discharges a bridge debt.

It does not discharge the arithmetic energy upper-bound debt.

Therefore this result is not classified as `REPACKAGING_ONLY`.

---

# 16. Candidate C-RH-GLB-02 — Fejer / Bohr log-time averaging

A natural attempt is to average the packet over long log-time windows so distinct imaginary frequencies become orthogonal.

For finite trigonometric sums this is standard.

However the amplitudes are

$$
e^{(\Re\rho)T},
$$

so a long translation window changes both phase and magnitude.

Without a normalization tied to an unknown extremal real part, the averaging theorem introduces a new scale-selection debt.

Because HLPG already recovers coefficients without this debt, the candidate is:

```text
DEPRIORITIZED
```

not false.

---

# 17. Candidate C-RH-GLB-03 — Positive resolvent reweighting

Earlier positive-kernel work showed that fixed nonzero positive spectral pieces retain the same off-axis exponent, while moving spectral windows pay a sensitivity tax.

Full moving-center energies are elliptically equivalent, at fixed-exponent level, to classical normalized PNT mean-square quantities.

Therefore another positive reweighting without a new arithmetic theorem is classified:

```text
REJECTED_AS_REPRESENTATION_ONLY
```

under the existing representation-closure obstruction.

---

# 18. Candidate C-RH-GLB-04 — finite-interval Suzuki operator limit

Modern Suzuki operator work provides a strong and relevant finite-interval framework for the Weil quadratic form and connects the construction with de Branges / operator theory.

However the proposed limiting self-adjoint operator whose spectrum would recover zeta-zero ordinates is presently formulated as a conjectural limit construction.

Therefore it cannot currently serve as a closed `CSM_RH` globalizer certificate.

Classification:

```text
DEFERRED
external dependency:
  conjectural finite-interval -> infinite-limit spectral bridge
```

This remains a valuable future route, especially for the Weil branch.

---

# 19. Candidate C-RH-GLB-05 — density weighted suppression

Any candidate whose decisive step is only a density theorem still permits a sparse or isolated extreme zero.

The packet-type theorem actually makes the obstruction sharper:

a single nonzero zero coefficient already creates an analytic singularity in the Hilbert-Laplace resolvent.

Therefore density-only suppression remains blocked.

Classification:

```text
REJECTED_BY_O-RH-003
```

---

# 20. Candidate C-RH-GLB-06 — random phase orthogonalization

Introducing an auxiliary random phase can diagonalize a finite packet in expectation.

But a new phase variable must be connected back to a canonical arithmetic observable.

Without that transfer theorem the route introduces:

```text
OBSERVABLE_TRANSFER_DEBT
ARITHMETIC_REALIZABILITY_DEBT
```

Because HLPG achieves the required noncancellation without altering the observable, this candidate is deferred.

---

# 21. Updated obstruction topology

The major-arc branch now becomes:

```text
OFF-CRITICAL ZERO
      |
      v
SMOOTH MELLIN COEFFICIENT v_rho != 0
      |
      v
HILBERT ZERO PACKET F(T)
      |
      v
HILBERT-LAPLACE COEFFICIENT RECOVERY
      |
      v
exact packet type = Theta_zeta
      |
      v
exact q=1 energy type = 1 + 2 Theta_zeta
      |
      v
EMAE fixed-power bound
      |
      v
fixed zero strip
```

The globalization bridge is now closed.

The only unresolved major-arc step in this chain is the arithmetic upper bound.

---

# 22. Updated CSM_RH frontier

## Principal frontier

```text
F-RH-003
EXCEPTIONAL_MAJOR_ARC_ENERGY
status: OPEN
strength:
  S2 for every fixed eta > 0
  S3 at eta = 1
```

## Deprioritized auxiliary frontier

```text
F-RH-004A
POINTWISE_MAJOR_ZERO_PACKET_LOWER_ENVELOPE
status: OPEN
priority: LOW
reason:
  no longer required for exponent-level closure
```

## Closed bridge frontier

```text
F-RH-004B
MAJOR_ZERO_PACKET_EXPONENTIAL_TYPE
status: CLOSED
certificate:
  Theorem 9.1
  Theorem 11.1
```

---

# 23. GLM worker architecture for the next campaign

The next worker campaign must preserve the canonical provider/protocol separation.

## CSM_RH produces

```text
Frontier Task Contract
Source Pack
Known Obstruction Pack
Strength Budget
Required Output Schema
```

## Designer worker

Produces:

```text
candidate mechanism
minimal assumptions
target estimate
known theorem mapping
failure modes
```

## Builder worker

Produces:

```text
derivation
lemmas
explicit constants / exponents
proof obligations
computational crosschecks
```

## Verifier worker

Produces:

```text
objections
hidden-RH-premise audit
quantifier audit
uniformity audit
counterexample attempt
strength classification
```

## Frontier model

Receives only the typed artifacts:

```text
Task Contract
Candidate Artifact
Objection
Repair Patch
Verification Report
```

It does not treat worker self-confidence as proof authority.

---

# 24. Campaign 02 target

Because the packet globalizer is closed, the next high-volume worker target is no longer `LOSSLESS_WITNESS_GLOBALIZER` on the major-arc branch.

The new target is:

```text
CSM_RH Campaign 02

target:
  ARITHMETIC_EMAE_FIXED_POWER

question:
  find the weakest genuinely arithmetic theorem that yields
  EMAE(eta) for some fixed eta > 0

forbidden shortcuts:
  density-only
  representation-only
  shrinking-aperture false saving
  moving-band sensitivity omission
  isolated-channel dominance assumption
  finite verification -> global theorem
```

Candidate mechanism families should include only mechanisms that can change arithmetic strength.

Examples of admissible search families:

```text
zero repulsion with quantitative energy consequence
character packet bilinear cancellation
large-sieve refinement with extremal-zero sensitivity
new weighted prime-correlation inequality
structural cancellation tied to functional-equation pairing
hybrid conductor-height-energy estimate
```

These are search families, not established theorems.

---

# 25. Finite synthetic crosscheck

The package includes:

```text
hlpg_finite_packet_crosscheck.py
hlpg_finite_packet_crosscheck.csv
```

The script verifies on a synthetic finite Hilbert-valued exponential packet:

1. direct norm-square energy equals its pair expansion;
2. the Laplace rational form equals direct numerical integration;
3. the maximal-real-part diagonal term produces a positive real-axis residue;
4. lower-real-part same-frequency terms do not cancel the maximal diagonal pole;
5. pointwise interference can be substantial while exponential-type recovery remains intact.

This is a formula crosscheck only.

It is not numerical evidence for RH.

---

# 26. External literature boundary

The proof of Theorem 9.1 is self-contained at the level needed here.

Relevant surrounding literature includes:

1. M. Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, Journal of the London Mathematical Society 108 (2023), 1448–1487, DOI `10.1112/jlms.12785`.

2. M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096` (2026). This develops a finite-interval operator framework and formulates a spectral-limit conjecture; the conjectural limit is not used as a theorem here.

3. D. Carando, A. Defant, F. Marceca, I. Schoolmann, *Vector-valued general Dirichlet series*, Studia Mathematica 258 (2021), 269–316.

4. A. Defant, A. Pérez, *Hardy spaces of vector-valued Dirichlet series*, Studia Mathematica 243 (2018), 53–78.

These references provide context for vector-valued Dirichlet-series and operator language but do not replace the explicit proof given above.

---

# 27. State transition

The canonical transition is:

```text
CSM_RH v0.2
  ->
CSM_RH v0.3
```

with:

```text
GLM semantic correction:
  GLM_Backward Search = WITHDRAWN NAME
  GLM-5.3-Flash = WORKER / PROVIDER

O-RH-005-M:
  OPEN
  ->
  CLOSED_AT_EXPONENTIAL_TYPE

F-RH-004:
  SPLIT INTO
    F-RH-004A OPEN / LOW PRIORITY
    F-RH-004B CLOSED

B-RH-005:
  old pointwise lower-envelope bridge remains OPEN

B-RH-007:
  HILBERT_PACKET_TO_EXACT_EXPONENTIAL_TYPE = CERTIFIED

B-RH-008:
  EMAE_TO_FIXED_ZERO_STRIP = CERTIFIED

S-RH-007:
  LOSSLESS_WITNESS_GLOBALIZER
  ->
  PARTIALLY_CLOSED
  major-arc instance = CLOSED
  Weil instance = OPEN
```

---

# 28. Final status

```text
RH = OPEN

WEIL GLOBALIZATION = OPEN

FIXED-APERTURE GLOBALIZATION = CLOSED
FIXED-APERTURE RH-COMPLETE TAIL = OPEN

MAJOR-ARC PACKET GLOBALIZATION = CLOSED_AT_EXPONENTIAL_TYPE
MAJOR-ARC EMAE FIXED POWER = OPEN

EMAE STRENGTH AUDIT = CERTIFIED

GLM = WORKER / PROVIDER
CSM_RH = PROTOCOL / STATE SPACE

NEXT CAMPAIGN:
  ARITHMETIC_EMAE_FIXED_POWER
```

The main mathematical conclusion is:

$$
\boxed{
\inf
\left\{
a:
\left\|
\sum_\rho
e^{\rho T}
\mathcal W_\rho
\right\|_{\mathcal H_{w,U}}
=
O(e^{aT})
\right\}
=
\Theta_\zeta.
}
$$

Therefore:

$$
\boxed{
\operatorname{type}
\left(
\mathcal E_1
\right)
=
1+2\Theta_\zeta
=
2+2\Delta_\zeta.
}
$$

The major-arc zero packet cannot hide an off-axis zero at exponential-type level.

The remaining major-arc obstruction is arithmetic, not representational.
