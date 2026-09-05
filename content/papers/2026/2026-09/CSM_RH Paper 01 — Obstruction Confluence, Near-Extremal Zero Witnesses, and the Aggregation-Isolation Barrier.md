# CSM_RH Paper 01
## Obstruction Confluence, Near-Extremal Zero Witnesses, and the Aggregation-Isolation Barrier

**Project:** `CSM_RH`  
**Paper:** `01`  
**Version:** `v0.1`  
**Date:** `2026-09-04`  
**Parent state:** `CSM_RH v0.1 / Paper 00`  
**Research method:** `GLM_Backward Search`, scope: Goal-Led Meta-Research  
**Status:** closure-space research paper; not a proof or disproof of RH  
**中文標題：** CSM_RH 論文 01：阻斷匯流、近極端零點見證與聚合—隔離障壁  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** English

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

This paper performs four narrower tasks:

1. determine whether three current RH frontiers can legitimately be quotiented;
2. prove a common near-extremal-zero witness-preservation structure;
3. separate witness preservation from globalization / isolation;
4. compile the resulting state correction into `CSM_RH v0.2`.

A route obstruction is not a theorem refutation.

A representation analogy is not a bridge certificate.

A shared witness is not sufficient for mathematical quotient.

---

# 1. Source basis

The principal internal source artifacts are:

```text
CSM_RH Paper 00
  Canonical Domain Model and GLM_RH Protocol v0.1

RH_NonlocalDifferenceCone_ConditionalCellDual v1.4
  Scalar Schur dual and conditional off-axis cell analysis

RH_FixedAperture v1.65 Independent Audit
  Exact aperture growth type and local-prime discrepancy criterion

RH_CharacterMajorArcVariance v3.18
  Character zero packets, exact core scaling, CMZE / EMAE,
  isolated pole-zero power, and density-only no-go

CSM Paper 02
  Typed Closure Graphs and Obstruction Propagation

CSM Paper 03
  Frontier Geometry and Relative Exhaustion

CSM Paper 06
  Closure Transfer Laws and Cross-Domain Invariance
```

Inherited results retain the trust boundaries of their source artifacts.

---

# 2. The Paper 00 question

Paper 00 introduced three principal frontiers:

```text
F-RH-001  GLOBAL_WEIL_ISOLATION_DOMINANCE
F-RH-002  GLOBAL_TAIL_INVARIANT
F-RH-003  EXCEPTIONAL_MAJOR_ARC_ENERGY
```

and a provisional quotient candidate:

```text
QO-RH-A
SINGLE_EXTREME_ZERO_GLOBALIZATION_BARRIER
```

The intended question was whether these are three descriptions of one underlying RH obstruction.

This paper gives a stricter answer:

```text
THREE-WAY MATHEMATICAL QUOTIENT = NOT CERTIFIED

THREE-WAY WITNESS CONFLUENCE = CERTIFIED

WEIL / MAJOR-ARC AGGREGATION-ISOLATION HOMOLOGY = CERTIFIED AS A TYPED STRUCTURAL ANALOGY

FIXED-APERTURE LOSSLESS DIAGNOSTIC BRIDGE = ALREADY CLOSED

MAJOR-ARC PACKET ISOLATION = OPEN

WEIL CONSTRUCTIVE CELL-TO-GLOBAL ISOLATION = OPEN
```

Thus Paper 00's quotient candidate must be refined rather than promoted.

---

# 3. Root zero-displacement invariant

Let $Z_{\mathrm{nt}}(\zeta)$ be the multiset of nontrivial zeros of the Riemann zeta function.

Define

$$
\Delta_\zeta
=
\sup_{\rho\in Z_{\mathrm{nt}}(\zeta)}
\left|
\Re\rho-\frac12
\right|.
$$

By the critical strip,

$$
0\le \Delta_\zeta\le \frac12.
$$

RH is equivalent to

$$
\Delta_\zeta=0.
$$

The important technical point is that the supremum need not be assumed to be attained.

Accordingly, the canonical obstruction object should not be based on a literal "rightmost zero" unless such attainment has independently been proved.

---

# 4. Near-extremal zero family

## Definition 4.1

Assume

$$
\Delta_\zeta>0.
$$

For any

$$
0<\varepsilon<\Delta_\zeta,
$$

an $\varepsilon$ -near-extremal zero is a nontrivial zero $\rho_\varepsilon$ such that, after using functional-equation symmetry if necessary,

$$
\Re\rho_\varepsilon
>
\frac12+\Delta_\zeta-\varepsilon.
$$

Write

$$
\rho_\varepsilon
=
\frac12+\delta_\varepsilon+i\tau_\varepsilon,
$$

where

$$
\delta_\varepsilon
>
\Delta_\zeta-\varepsilon
>
0.
$$

## Proposition 4.2

If RH is false, then for every

$$
0<\varepsilon<\Delta_\zeta
$$

there exists an $\varepsilon$ -near-extremal zero.

### Proof

By the definition of supremum, there exists a zero satisfying

$$
\left|
\Re\rho-\frac12
\right|
>
\Delta_\zeta-\varepsilon.
$$

If this zero lies to the left of the critical line, use the functional-equation symmetry of the zero set to obtain a corresponding zero on the right.

Hence there exists

$$
\rho_\varepsilon
=
\frac12+\delta_\varepsilon+i\tau_\varepsilon
$$

with

$$
\delta_\varepsilon>\Delta_\zeta-\varepsilon.
$$

No attainment of the supremum was assumed. $\square$

---

# 5. Why the "single extreme zero" language is dangerous

A phrase such as

```text
the rightmost zero
```

may accidentally import the claim that

$$
\Delta_\zeta
$$

is attained by some zero.

The current program does not need that assumption.

The canonical replacement is:

```text
NEAR_EXTREMAL_ZERO_FAMILY
```

or, when a single member is enough for a local argument:

```text
NEAR_EXTREMAL_ZERO_WITNESS
```

Therefore the provisional Paper 00 name

```text
SINGLE_EXTREME_ZERO_GLOBALIZATION_BARRIER
```

is replaced at the typed level by

```text
OC-RH-A
NEAR_EXTREMAL_ZERO_WITNESS_CONFLUENCE
```

and

```text
O-RH-005
AGGREGATION_ISOLATION_BARRIER
```

The first is a confluence object.

The second is an obstruction schema.

Neither is, by itself, an equivalence quotient of the three frontiers.

---

# 6. Weil-side witness persistence

Take an off-critical zero

$$
\rho
=
\frac12+\delta+i\tau,
\qquad
\delta>0.
$$

The v1.4 $z$ -plane coordinate is

$$
z
=
\frac{\rho-1/2}{i}
=
\tau-i\delta.
$$

For real even test functions $\psi$, write

$$
G_\psi(z)
=
A_z(\psi)-iB_z(\psi),
$$

where

$$
A_z(\psi)
=
\int
\psi(t)\cos(\tau t)\cosh(\delta t)\,dt
$$

up to the harmless sign convention for the imaginary coordinate, and

$$
B_z(\psi)
=
\int
\psi(t)\sin(\tau t)\sinh(-\delta t)\,dt.
$$

The orbit operator is

$$
C_z
=
2A_z\otimes A_z
-
2B_z\otimes B_z.
$$

The key point is not merely that a negative sign occurs syntactically.

For an off-critical nontrivial zeta zero, both

$$
\delta\neq0
$$

and

$$
\tau\neq0.
$$

Hence the even function

$$
g_z(t)
=
\sin(\tau t)\sinh(-\delta t)
$$

is not identically zero.

Choose an even nonnegative smooth compactly supported cutoff $\chi$ supported where $g_z$ is nonzero, and let

$$
\psi(t)=\chi(t)g_z(t).
$$

Then $\psi$ is real and even, and

$$
B_z(\psi)
=
\int
\chi(t)g_z(t)^2\,dt
>
0.
$$

Therefore $B_z$ is a nonzero functional.

## Theorem 6.1 — Weil local witness persistence

Every off-critical nontrivial zeta zero generates a nonzero negative rank-one component

$$
-2B_z\otimes B_z
$$

inside its four-point orbit operator

$$
C_z
=
2A_z\otimes A_z
-
2B_z\otimes B_z.
$$

Thus the off-axis zero is not annihilated by the local orbit representation.

### Important limitation

The full v1.4 object has the form

$$
W_z
=
B
+
2mA_z\otimes A_z
-
2mB_z\otimes B_z,
$$

where $B$ is a separately supplied background.

The existence of the local negative component does not imply

$$
W_z\not\succeq0.
$$

The scalar Schur criterion makes the missing step explicit:

$$
W_z\succeq0
\Longleftrightarrow
\frac1{2m}
-
K_{BB}
+
\frac{K_{AB}^2}{
\frac1{2m}+K_{AA}
}
\ge0.
$$

Therefore the unresolved issue is not local witness existence.

It is constructive witness isolation / dominance against the remaining background.

---

# 7. Fixed-aperture witness persistence

For a fixed

$$
h>0,
$$

define

$$
D_h(t)
=
\frac12
\left[
\Psi(t+h)
+
\Psi(t-h)
-
2\Psi(t)
\right].
$$

The audited zero representation is

$$
D_h(t)
=
\sum_\gamma
c_h(\gamma)e^{i\gamma t},
$$

with

$$
c_h(\gamma)
=
\frac{
1-\cos(\gamma h)
}{
\gamma^2
}.
$$

For a zeta zero

$$
\rho
=
\frac12+\delta+i\tau,
$$

the corresponding zero parameter may be written

$$
\gamma
=
-\tau+i\delta.
$$

If the filter annihilated this mode, then

$$
1-\cos(\gamma h)=0,
$$

so

$$
\cos(\gamma h)=1.
$$

But the complex solutions of

$$
\cos z=1
$$

are

$$
z=2\pi k,
\qquad
k\in\mathbb Z,
$$

which are real.

Because

$$
\Im\gamma=\delta\neq0,
$$

the coefficient cannot vanish.

## Theorem 7.1 — Fixed-aperture non-annihilation

For every fixed

$$
h>0,
$$

no off-critical zeta-zero mode is annihilated by the fixed-aperture filter.

More strongly, the v1.65 audit established the exact growth invariant

$$
\sigma_h
=
\inf
\left\{
\sigma\ge0:
D_h(t)=O(e^{\sigma t})
\right\}
$$

and

$$
\boxed{
\sigma_h=\Delta_\zeta.
}
$$

Hence

$$
RH
\Longleftrightarrow
\sigma_h=0.
$$

The local-prime discrepancy $\mathfrak E_h(x)$ has the same type:

$$
\inf
\left\{
\sigma\ge0:
\mathfrak E_h(x)=O(x^\sigma)
\right\}
=
\Delta_\zeta.
$$

Therefore

$$
RH
\Longleftrightarrow
\mathfrak E_h(x)=x^{o(1)}.
$$

This is not merely a visible local witness.

It is a lossless global diagnostic of horizontal zero displacement.

---

# 8. Major-arc isolated witness persistence

Let $w$ be a nonzero smooth major-arc weight and define

$$
W_{x,\epsilon}(s)
=
\int_0^\infty
w(t/x)e(\epsilon t)t^{s-1}\,dt.
$$

On the core scale

$$
\epsilon=\frac ux,
$$

the exact scaling is

$$
W_{x,u/x}(s)
=
x^s\mathcal W_s(u),
$$

where

$$
\mathcal W_s(u)
=
\int_0^\infty
w(v)e(uv)v^{s-1}\,dv.
$$

For fixed

$$
U>0,
$$

define

$$
C_{w,U}(\rho)
=
\int_{-U}^{U}
|\mathcal W_1(u)|^2
|\mathcal W_\rho(u)|^2
\,du.
$$

The v3.18 kernel theorem gives

$$
C_{w,U}(\rho)>0
$$

for every fixed zero in the relevant strip, and

$$
\int_{|\epsilon|\le U/x}
|
W_{x,\epsilon}(1)
|^2
|
W_{x,\epsilon}(\rho)
|^2
\,d\epsilon
=
x^{1+2\Re\rho}
C_{w,U}(\rho).
$$

For

$$
\rho
=
\frac12+\delta+i\tau,
$$

this becomes

$$
\boxed{
x^{2+2\delta}
C_{w,U}(\rho).
}
$$

## Theorem 8.1 — Major-arc isolated witness persistence

Every fixed off-critical zeta zero has a strictly positive isolated pole-zero cross-energy response on the smooth core major arc.

For an $\varepsilon$ -near-extremal zero,

$$
\delta_\varepsilon
>
\Delta_\zeta-\varepsilon,
$$

so its isolated power exponent satisfies

$$
1+2\Re\rho_\varepsilon
>
2+2\Delta_\zeta-2\varepsilon.
$$

Thus the isolated major-arc response approaches the extremal horizontal-displacement scale as

$$
\varepsilon\to0.
$$

### Important limitation

The actual zero packet is

$$
Z_\chi(x,\epsilon)
=
\sum_{\rho_\chi}
W_{x,\epsilon}(\rho_\chi).
$$

The full positive character-family energy contains

$$
|Z_\chi(x,\epsilon)|^2,
$$

not the sum of the isolated squared zero contributions.

Character orthogonality removes cancellation between different characters in the basic quadratic character energy, but it does not automatically remove zero-zero interference inside one character packet.

Therefore

$$
\text{isolated zero scale}
$$

is not yet a lower bound for

$$
\mathfrak Z_2.
$$

This is the major-arc isolation debt.

---

# 9. Tri-representation witness theorem

We can now state the first new CSM_RH cross-representation theorem.

## Theorem 9.1 — Near-Extremal Witness Preservation

Assume RH is false.

For every

$$
0<\varepsilon<\Delta_\zeta,
$$

there exists a right-side nontrivial zero

$$
\rho_\varepsilon
=
\frac12+\delta_\varepsilon+i\tau_\varepsilon,
\qquad
\delta_\varepsilon
>
\Delta_\zeta-\varepsilon,
$$

such that:

### Weil representation

The associated orbit operator contains a nonzero negative rank-one component

$$
-2B_{z_\varepsilon}\otimes B_{z_\varepsilon}.
$$

### Fixed-aperture representation

For every fixed

$$
h>0,
$$

the corresponding spectral coefficient satisfies

$$
c_h(\gamma_\varepsilon)\neq0,
$$

and globally

$$
\sigma_h=\Delta_\zeta.
$$

### Major-arc representation

For every admissible nonzero smooth $w$ and fixed

$$
U>0,
$$

the isolated pole-zero cross kernel has strictly positive coefficient

$$
C_{w,U}(\rho_\varepsilon)>0
$$

and power

$$
x^{1+2\Re\rho_\varepsilon}
>
x^{2+2\Delta_\zeta-2\varepsilon}
$$

at the exponent level.

Therefore the same near-extremal off-critical witness is visible in all three representations.

### What this theorem does not say

It does not say that the three full proof obligations are equivalent.

It does not say that the Weil negative component dominates the full background.

It does not say that the major-arc isolated channel lower-bounds the full zero packet.

It does not prove a new estimate on $\Delta_\zeta$.

It proves cross-representation witness persistence.

---

# 10. Obstruction confluence is weaker than quotient

CSM distinguishes:

```text
SAME WITNESS
SAME OBSTRUCTION SHAPE
SAME MATHEMATICAL STATEMENT
```

These are different relations.

Theorem 9.1 establishes:

```text
SAME NEAR-EXTREMAL WITNESS FAMILY
```

across the three routes.

Sections 6 and 8 further establish the same obstruction shape for Weil and major-arc routes:

```text
distinguished witness is visible in an isolated component
but the full aggregated object contains uncontrolled background / interference
```

However, the fixed-aperture route already has a lossless global theorem

$$
\sigma_h=\Delta_\zeta.
$$

Hence its unresolved problem is of a different type:

```text
the witness has already been globalized;
the remaining difficulty is proving the required tail estimate.
```

Therefore a three-way quotient would collapse mathematically distinct proof debts.

---

# 11. Aggregation-Isolation Barrier

## Definition 11.1

An `Aggregation-Isolation Barrier` occurs when a representation has the form

$$
\mathcal A
=
\mathcal S_\star+\mathcal R,
$$

where:

- $\mathcal S_\star$ is a distinguished local or isolated witness;
- $\mathcal R$ is an aggregated background, remainder, or interference field;
- the desired global predicate $\Phi(\mathcal A)$ is nonlinear or sign-sensitive;
- knowledge of $\Phi(\mathcal S_\star)$ alone does not determine $\Phi(\mathcal A)$.

A valid closure requires an additional certificate such as:

```text
dominance
orthogonality
spectral separation
positivity
coercivity
exact diagonalization
analytic singularity separation
or another lossless globalizer
```

The obstruction ID is:

```text
O-RH-005
AGGREGATION_ISOLATION_BARRIER
```

---

# 12. Weil instance of the barrier

In the Weil cell-dual route,

$$
\mathcal S_\star
=
-2mB_z\otimes B_z
$$

is the negative witness.

The aggregated object includes

$$
B+2mA_z\otimes A_z.
$$

The desired predicate is operator nonpositivity / a negative quadratic direction.

The unresolved certificate is a constructive domination or Schur-separation statement strong enough to guarantee that the local negative witness survives the full background in the controlled test family.

Canonical instance:

```text
O-RH-005-W
AGGREGATION_ISOLATION_BARRIER / WEIL

status: OPEN
debt:
  CONSTRUCTIVE_GLOBALIZATION_DEBT
  BACKGROUND_DOMINANCE_DEBT
```

This refines `F-RH-001`.

---

# 13. Major-arc instance of the barrier

For one character packet,

$$
Z_\chi
=
W(\rho_\star)
+
\sum_{\rho\neq\rho_\star}
W(\rho).
$$

The isolated witness has positive pole-zero energy

$$
x^{1+2\Re\rho_\star}C_{w,U}(\rho_\star).
$$

But the full energy uses

$$
|Z_\chi|^2.
$$

The desired predicate is a packet-level lower envelope or another certified transfer from the extremal isolated channel to the full character energy.

Canonical instance:

```text
O-RH-005-M
AGGREGATION_ISOLATION_BARRIER / MAJOR_ARC

status: OPEN
debt:
  ZERO_PACKET_INTERFERENCE_DEBT
  EXTREMAL_ZERO_ISOLATION_DEBT
```

This debt was implicit in v3.18 and is promoted here to an explicit frontier.

---

# 14. Fixed-aperture instance is already closed

The fixed-aperture observable also aggregates all zero modes.

Naively, it could have suffered the same cancellation problem.

However the v1.65 Laplace-transform audit proves the exact invariant

$$
\sigma_h=\Delta_\zeta.
$$

Thus the route possesses a certified globalizer.

The globalizer does not need to isolate one zero pointwise.

Instead, any off-axis zero would create a forbidden singularity in the holomorphic continuation region once the growth type is assumed too small.

Canonical instance:

```text
O-RH-005-A
AGGREGATION_ISOLATION_BARRIER / FIXED_APERTURE

status: CLOSED

certificate:
  EXACT_APERTURE_GROWTH_TYPE
  LAPLACE_SINGULARITY_SEPARATION
```

This is one of the most important structural findings of Paper 01.

The fixed-aperture route did not solve RH, but it already solved the witness-globalization subproblem.

---

# 15. Compression without theorem-strength reduction

The fixed-aperture route compresses the entire horizontal zero geometry into one scalar invariant:

$$
\sigma_h=\Delta_\zeta.
$$

But this does not reduce the mathematical strength of the final estimate.

Indeed,

$$
\sigma_h=0
$$

is equivalent to RH.

Equivalently,

$$
\mathfrak E_h(x)=x^{o(1)}
$$

is RH-complete in this framework.

Thus:

```text
LOSSLESS COMPRESSION
does not imply
EASIER PROOF OBLIGATION
```

This is a general CSM_RH warning.

A representation can be excellent for diagnosis and still leave the full theorem strength in the final scalar bound.

---

# 16. Correction to the EMAE strength audit

Paper 00 treated a fixed-power major-arc estimate as if the isolated zero scale automatically forced a fixed zero strip.

This must be made conditional.

Define the major-arc energy gate:

$$
\operatorname{EMAE}(\eta):
\qquad
\mathfrak Z_2+\mathfrak Z_4
\ll
x^{3-\eta+o(1)}.
$$

The isolated q=1 pole-zero scale for a zero

$$
\rho=\beta+i\gamma
$$

is

$$
x^{1+2\beta}.
$$

But without a packet-isolation lower bound, one may not infer that the full packet energy is at least this large.

Therefore:

$$
\operatorname{EMAE}(\eta)
\not\Rightarrow_{\rm currently\ certified}
\beta\le1-\frac{\eta}{2}.
$$

The missing bridge is now named:

```text
F-RH-004
MAJOR_ZERO_PACKET_ISOLATION
abbrev: MZI
status: OPEN
```

A schematic sufficient form is:

$$
\operatorname{MZI}(\rho_\star):
\qquad
\mathfrak Z_2(x;Q,U)
\ge
x^{1+2\Re\rho_\star-o(1)}
$$

along a certified unbounded scale set or in another form strong enough to preserve the extremal power.

Only with such a bridge does the strength implication become legitimate.

## Proposition 16.1

If both

$$
\operatorname{EMAE}(\eta)
$$

and a compatible near-extremal packet-isolation lower bound hold, then

$$
\Delta_\zeta
\le
\frac12-\frac{\eta}{2}.
$$

### Proof sketch

For every $\varepsilon>0$, choose

$$
\Re\rho_\varepsilon
>
\frac12+\Delta_\zeta-\varepsilon.
$$

The isolation bridge gives an energy exponent at least

$$
1+2\Re\rho_\varepsilon
>
2+2\Delta_\zeta-2\varepsilon.
$$

EMAE gives exponent at most

$$
3-\eta.
$$

Hence

$$
2+2\Delta_\zeta-2\varepsilon
\le
3-\eta.
$$

Let

$$
\varepsilon\to0
$$

to obtain

$$
\Delta_\zeta
\le
\frac12-\frac{\eta}{2}.
$$

 $\square$

Thus the correct strength classification is:

```text
EMAE alone:
  strength implication = UNCLASSIFIED WITHOUT MZI

EMAE + MZI:
  at least S2 if eta > 0

EMAE(1) + MZI:
  RH-level strength
```

---

# 17. Density-only no-go remains valid but narrower

The v3.18 density-only no-go states that a counting estimate of the form

$$
\sum_\chi
N(\sigma,T,\chi)
\ll
(qT)^{A(1-\sigma)+o(1)}
$$

does not, by itself, suppress a possible isolated extreme zero strongly enough to yield a fixed-power major-arc saving.

Paper 01 does not weaken that result.

It sharpens its placement.

The no-go acts on:

```text
density-only attempts to discharge F-RH-003 / F-RH-004
```

It does not block:

```text
structural packet separation
exact zero orthogonalization
new positivity
new repulsion theorem
new transform-domain isolation
lossless scale-frequency globalization
```

Therefore the obstruction remains typed and assumption-dependent.

---

# 18. Three frontier types after Paper 01

The current frontiers are no longer treated as one homogeneous set.

## Type A — Constructive isolation frontier

```text
F-RH-001
GLOBAL_WEIL_ISOLATION_DOMINANCE

problem:
  local negative orbit witness
  ->
  controlled global / finite-dimensional negative certificate
```

## Type B — RH-complete estimate frontier

```text
F-RH-002
GLOBAL_TAIL_INVARIANT

problem:
  exact global diagnostic already exists
  ->
  prove zero exponential type / subexponential local-prime tail
```

## Type C — Energy upper-bound frontier

```text
F-RH-003
EXCEPTIONAL_MAJOR_ARC_ENERGY

problem:
  prove weighted character-zero structured variance saving
```

## Type D — Energy isolation frontier

```text
F-RH-004
MAJOR_ZERO_PACKET_ISOLATION

problem:
  isolated near-extremal zero response
  ->
  packet-level lower envelope or equivalent separation certificate
```

This four-frontier split is more faithful than the Paper 00 three-way quotient candidate.

---

# 19. Obstruction topology

The updated topology is:

```text
                 OFF-CRITICAL ZERO
                        |
                        v
              NEAR-EXTREMAL FAMILY
                        |
        +---------------+---------------+
        |                               |
        v                               v
   WEIL ORBIT                      MAJOR-ARC KERNEL
 negative rank-one                positive isolated energy
        |                               |
        v                               v
  aggregation with                aggregation inside
     background                      zero packet
        |                               |
        v                               v
 O-RH-005-W OPEN                 O-RH-005-M OPEN
        |                               |
        +---------------+---------------+
                        |
                        v
             AGGREGATION-ISOLATION
                  OBSTRUCTION
```

The fixed-aperture route enters differently:

```text
OFF-CRITICAL ZERO
      |
      v
FIXED-APERTURE MODE
      |
      v
LAPLACE SINGULARITY / EXACT TYPE
      |
      v
sigma_h = Delta_zeta
      |
      v
O-RH-005-A CLOSED
```

Thus fixed aperture supplies an existence proof that a useful lossless globalizer can exist in an RH representation.

---

# 20. Certified confluence object

Create:

```text
OC-RH-A
NEAR_EXTREMAL_ZERO_WITNESS_CONFLUENCE
```

Members:

```text
WEIL_LOCAL_ORBIT_WITNESS
FIXED_APERTURE_SPECTRAL_WITNESS
MAJOR_ARC_ISOLATED_ENERGY_WITNESS
```

Certificate status:

```text
WITNESS_EXISTENCE_TRANSFER = PASS
HORIZONTAL_DISPLACEMENT_PRESERVATION = PASS
FULL_PREDICATE_EQUIVALENCE = FAIL / NOT_PROVED
REVERSE_BRIDGES = INCOMPLETE
QUOTIENT_PROMOTION = FORBIDDEN
```

This is a CSM obstruction-confluence object, not a mathematical equivalence class.

---

# 21. Why the original quotient fails

A valid three-way mathematical quotient would require enough bridge authority to treat the three frontier obligations as interchangeable for closure purposes.

That authority is absent for at least three reasons.

## 21.1 Different theorem strength

`F-RH-002` contains a criterion exactly equivalent to RH.

`F-RH-003` with a fixed small $\eta>0$ would, even after isolation, yield only a fixed zero-strip improvement.

Thus the strength profiles differ.

## 21.2 Different loss structure

The aperture route has a certified lossless zero-displacement invariant.

The Weil and major-arc routes retain aggregation / interference debt.

## 21.3 Different output predicates

The Weil route is sign / inertia sensitive.

The aperture route is growth-type / analytic-continuation sensitive.

The major-arc route is positive-energy / power-saving sensitive.

Therefore "same zero witness" is insufficient for quotient closure.

## Theorem 21.1 — No Three-Way Quotient at v0.2

Under the current certified bridge set, the frontier family

$$
\{
F\text{-}RH\text{-}001,
F\text{-}RH\text{-}002,
F\text{-}RH\text{-}003
\}
$$

cannot be promoted to a single mathematical quotient class.

Its correct current relation is typed obstruction confluence.

---

# 22. The two-way structural homology

Although a mathematical quotient is not certified, `F-RH-001` and `F-RH-004` share a stronger structural pattern.

Both have:

1. a single off-critical zero producing an explicit local / isolated witness;
2. an aggregated object formed before the final predicate is evaluated;
3. possible masking by other components;
4. an open need for a separation, dominance, or orthogonalization certificate.

This is recorded as:

```text
H-RH-001
WEIL_MAJOR_AGGREGATION_ISOLATION_HOMOLOGY
status: CERTIFIED_STRUCTURAL
authority: NON_EQUIVALENCE
```

The word `homology` here is CSM structural terminology, not algebraic topology.

It means:

```text
same obstruction signature under typed compilation
```

not:

```text
same theorem
```

---

# 23. The high-value transfer question

The fixed-aperture route already closed its aggregation-isolation instance through a lossless analytic transform.

Therefore the new high-value question is:

> Can the globalization mechanism, rather than the final RH-equivalent estimate, be transferred or reinvented in the Weil or major-arc representations?

This changes the research target.

Do not first ask:

```text
Can EMAE be proved?
```

or:

```text
Can the local Weil negative rank-one term dominate?
```

First ask:

```text
Can a new transform make near-extremal zero information noncancellable at the global level?
```

This is a narrower and more structurally informed target.

---

# 24. New survivor family

Create:

```text
S-RH-007
LOSSLESS_WITNESS_GLOBALIZER
status: OPEN / SURVIVOR
```

A candidate globalizer $\mathcal T$ should satisfy as many of the following as possible.

## G1. Zero-faithfulness

For every off-critical zero $\rho$,

$$
\mathcal T(\rho)
$$

is nontrivial.

## G2. Extremal-faithfulness

The response strength is a known strictly monotone function of

$$
\left|
\Re\rho-\frac12
\right|.
$$

## G3. Aggregation resistance

Distinct zero contributions cannot cancel the extremal witness at the level of the chosen invariant.

## G4. Background control

Archimedean, trivial-zero, local-factor, or non-extremal contributions are either explicit, positive, orthogonal, lower order, or separately certifiable.

## G5. Quantifier preservation

The transform preserves the global quantifier over all nontrivial zeros.

## G6. No hidden RH premise

The globalizer itself must not require:

$$
\Delta_\zeta=0
$$

or an equivalent condition as an assumption.

## G7. Strength transparency

If the final bound is RH-equivalent, that fact must remain visible rather than being relabeled as a routine tail estimate.

---

# 25. Fixed aperture as the model globalizer

The fixed-aperture construction demonstrates one successful pattern:

```text
compact local prime observable
    ->
spectral zero filter
    ->
non-annihilation of every off-axis mode
    ->
Laplace transform
    ->
zero singularity localization
    ->
exact exponential type
    ->
Delta_zeta
```

The lesson is not that the same formula should be copied.

The lesson is that a successful RH representation may require two separate layers:

```text
Layer 1:
  local / finite-support arithmetic observable

Layer 2:
  global analytic transform that prevents extremal witness cancellation
```

This two-layer pattern should guide the next `GLM_Backward Search` campaign.

---

# 26. GLM_Backward Search integration

The formal method name remains:

```text
GLM_Backward Search
```

with scope:

```text
Goal-Led Meta-Research
```

The definition-first rule is preserved:

> Never begin backward search before classifying the target.

For the next campaign the target is not classified as `RH` directly.

It is classified as:

```text
target_id:
  GLM-RH-C01

target_name:
  LOSSLESS_WITNESS_GLOBALIZER

target_type:
  method/theorem-family search target

parent_frontiers:
  F-RH-001
  F-RH-004

excluded_false_targets:
  direct RH-equivalent tail repackaging
  density-only extreme-zero suppression
  finite-checkpoint-to-global promotion
  unsupported three-way quotient
```

Thus GLM search begins from a smaller typed target.

---

# 27. Backward target decomposition

The desired terminal object is a certified bridge of the schematic form

$$
\text{near-extremal zero witness}
\Longrightarrow
\text{noncancellable global invariant}.
$$

Backward decomposition gives the following subtargets.

## T1. Choose the global invariant

Candidate invariant classes may include:

```text
analytic singularity
spectral mass
positive integrated energy
operator index / inertia
scale-frequency transform
reproducing-kernel norm
another certificate-carrying invariant
```

These are candidate classes, not asserted solutions.

## T2. Prove zero-faithful response

For each off-critical zero,

$$
\rho
\mapsto
\mathcal I_\rho
$$

must be nonzero.

## T3. Prove extremal separation

If

$$
\Re\rho_1>\Re\rho_2,
$$

the invariant must preserve enough ordering or asymptotic separation to identify the more extreme horizontal displacement.

## T4. Prove aggregation resistance

The total invariant must not allow the extremal contribution to disappear through uncontrolled cross terms.

## T5. Prove background closure

All nonzero non-target pieces must have certified status.

## T6. Strength audit

Determine whether proving a useful bound on the resulting invariant is:

```text
S0
S1
S2
S3
or S4
```

before declaring the route a simplification.

---

# 28. GLM rejection filters

A generated candidate is rejected from the principal route if any of the following holds.

## R1. Repackaging-only

It merely defines

$$
I=0
$$

where

$$
I=0
\Longleftrightarrow RH
$$

without giving a new bridge, invariant, or proof mechanism.

## R2. Hidden isolation premise

It assumes the extremal zero contribution dominates the rest without proving it.

## R3. Hidden attainment premise

It requires a literal rightmost zero rather than working with a near-extremal family.

## R4. Density-only recurrence

It tries to eliminate the extremal witness using only a zero-counting theorem already covered by `O-RH-003`.

## R5. Finite-to-global jump

It promotes finite computation or finitely many cells to RH without a completeness bridge.

## R6. Representation-only novelty

It changes formulas but preserves the same unresolved aggregation debt.

## R7. Strength laundering

It calls an S2 or S3 statement a routine analytic estimate.

---

# 29. First GLM campaign objective

The first campaign should generate candidates for:

```text
GLM-RH-C01
LOSSLESS_WITNESS_GLOBALIZER
```

and score them by closure gain.

A candidate has high value if it closes at least one of:

```text
O-RH-005-W
O-RH-005-M
```

without reopening a stronger hidden debt.

A particularly high-value candidate would close both through one common transform or one certified transfer law.

Such a result would not prove RH automatically.

It would, however, remove one of the currently repeated globalization bottlenecks.

---

# 30. Closure-gain metric for Campaign 01

For a candidate $X$, define a policy score

$$
P(X)
=
\frac{
w_1\Delta I(X)
+
w_2\Delta B(X)
+
w_3\Delta F(X)
+
w_4\Delta Q(X)
}{
1+C(X)+D(X)
},
$$

where:

- $\Delta I(X)$ is isolation debt discharged;
- $\Delta B(X)$ is certified bridge gain;
- $\Delta F(X)$ is frontier contraction;
- $\Delta Q(X)$ is valid quotient or confluence compression;
- $C(X)$ is expected proof cost;
- $D(X)$ is new proof debt.

This score has no theorem authority.

It is a search-priority device only.

---

# 31. Updated bridge ledger

## B-RH-001

```text
name:
  OFFAXIS_ZERO_TO_WEIL_LOCAL_SIGNED_WITNESS

status:
  CERTIFIED

preserves:
  off-axis existence
  local signed witness

does_not_preserve:
  global negativity
  finite certificate
```

## B-RH-002

```text
name:
  OFFAXIS_ZERO_TO_FIXED_APERTURE_MODE

status:
  CERTIFIED

preserves:
  off-axis existence
  non-annihilation
  exact horizontal displacement through exponential type
```

## B-RH-003

```text
name:
  OFFAXIS_ZERO_TO_MAJOR_ARC_ISOLATED_ENERGY

status:
  CERTIFIED

preserves:
  off-axis existence
  isolated positive kernel
  isolated power exponent
```

## B-RH-004

```text
name:
  WEIL_LOCAL_WITNESS_TO_CONTROLLED_GLOBAL_NEGATIVE_CERTIFICATE

status:
  OPEN
```

## B-RH-005

```text
name:
  MAJOR_ARC_ISOLATED_ZERO_TO_PACKET_LOWER_ENVELOPE

status:
  OPEN

frontier:
  F-RH-004
```

## B-RH-006

```text
name:
  FIXED_APERTURE_OBSERVABLE_TO_DELTA_ZETA

status:
  CERTIFIED_LOSSLESS
```

---

# 32. Updated obstruction ledger

```text
O-RH-001
RH_COMPLETE_TAIL_REPACKAGING
ACTIVE

O-RH-002
EXTREME_ZERO_POWER_DOMINANCE
ACTIVE AS ISOLATED-CHANNEL STRENGTH WARNING

O-RH-003
DENSITY_ONLY_NO_GO
ACTIVE

O-RH-004
FINITE_VERIFICATION_NONCOMPLETENESS
ACTIVE

O-RH-005
AGGREGATION_ISOLATION_BARRIER
ACTIVE SCHEMA

O-RH-005-W
WEIL AGGREGATION-ISOLATION
OPEN INSTANCE

O-RH-005-A
FIXED-APERTURE AGGREGATION-ISOLATION
CLOSED INSTANCE

O-RH-005-M
MAJOR-ARC AGGREGATION-ISOLATION
OPEN INSTANCE
```

---

# 33. Updated frontier ledger

```text
F-RH-001
GLOBAL_WEIL_ISOLATION_DOMINANCE
OPEN

F-RH-002
GLOBAL_TAIL_INVARIANT
OPEN
tag:
  RH_COMPLETE

F-RH-003
EXCEPTIONAL_MAJOR_ARC_ENERGY
OPEN

F-RH-004
MAJOR_ZERO_PACKET_ISOLATION
OPEN

S-RH-007
LOSSLESS_WITNESS_GLOBALIZER
OPEN
SURVIVOR
```

---

# 34. State transition from v0.1 to v0.2

The important state changes are:

```text
QO-RH-A:
  QUOTIENT_CANDIDATE
  ->
  NOT_PROMOTED

OC-RH-A:
  CREATED
  NEAR_EXTREMAL_ZERO_WITNESS_CONFLUENCE
  CERTIFIED

O-RH-005:
  CREATED
  AGGREGATION_ISOLATION_BARRIER

F-RH-004:
  CREATED
  MAJOR_ZERO_PACKET_ISOLATION

B-RH-001..003:
  CREATED / CERTIFIED

B-RH-004..005:
  CREATED / OPEN

B-RH-006:
  CREATED / CERTIFIED_LOSSLESS

S-RH-007:
  CREATED
  LOSSLESS_WITNESS_GLOBALIZER
```

The frontier count increases by one.

This is not regression.

It is a correction of a hidden bridge debt that Paper 00 had compressed into `F-RH-003`.

Under CSM, exposing a missing bridge can increase raw frontier size while improving frontier fidelity.

---

# 35. Main closure result

Paper 01 does not contract the RH root frontier.

It does contract ambiguity.

The main result is:

$$
\boxed{
\text{three routes share a persistent near-extremal zero witness}
}
$$

but

$$
\boxed{
\text{they do not yet share one quotient-certified proof obligation}.
}
$$

More precisely:

$$
\boxed{
\text{Weil and major-arc routes share an open aggregation-isolation barrier,}
}
$$

while

$$
\boxed{
\text{fixed aperture has already closed that barrier through an exact global diagnostic.}
}
$$

This identifies a new transferable research objective:

$$
\boxed{
\text{construct a lossless witness globalizer for the remaining open representations.}
}
$$

---

# 36. What should not be done next

The next step should not be:

```text
write v3.19 by assuming the isolated x^(1+2 beta) channel
is automatically a lower bound for the full packet
```

and it should not be:

```text
declare the Weil / aperture / major-arc frontiers equivalent
because all mention off-axis zeros
```

and it should not be:

```text
prove another RH-equivalent scalar tail criterion
and count that alone as closure gain
```

The next step should target the missing globalization mechanism itself.

---

# 37. Canonical next paper / campaign

The next research artifact is:

```text
CSM_RH / GLM Campaign 01
Lossless Witness Globalizer Search
```

The first definition-first classification is already fixed in this paper.

The campaign should generate a small number of candidate globalizer families, compile each into:

```text
statement
representation
zero response
aggregation law
background law
strength class
obstruction hits
bridge debt
falsification test
```

and reject any candidate that merely reproduces `O-RH-001`, `O-RH-003`, or `O-RH-005` under new notation.

---

# 38. Final canonical status

```text
ROOT_RH = OPEN

RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE

THREE_WAY_QUOTIENT = NOT_CERTIFIED
THREE_WAY_WITNESS_CONFLUENCE = CERTIFIED

WEIL_AGGREGATION_ISOLATION = OPEN
FIXED_APERTURE_AGGREGATION_ISOLATION = CLOSED
MAJOR_ARC_AGGREGATION_ISOLATION = OPEN

GLOBAL_TAIL_INVARIANT = OPEN / RH_COMPLETE
EMAE = OPEN
MZI = OPEN

LOSSLESS_WITNESS_GLOBALIZER = OPEN / SURVIVOR

NEXT_METHOD = GLM_Backward Search
NEXT_TARGET = LOSSLESS_WITNESS_GLOBALIZER
```

The substantive change is:

> The current RH program should no longer treat all surviving endgames as one undifferentiated "extreme zero" barrier. The same near-extremal zero is indeed visible in the Weil, fixed-aperture, and major-arc representations, but the globalization status differs. Fixed aperture already possesses a lossless analytic globalizer, whereas the Weil and major-arc routes still require a certified mechanism preventing the local or isolated zero witness from being masked by background or zero-packet interference. The next GLM search should therefore target the missing globalization mechanism, not another direct RH-equivalent estimate.

