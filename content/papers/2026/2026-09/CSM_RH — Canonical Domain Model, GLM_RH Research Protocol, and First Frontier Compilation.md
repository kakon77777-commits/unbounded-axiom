# CSM_RH v0.1
# Closure-Space Mathematics for the Riemann Hypothesis
## Canonical Domain Model, GLM_RH Research Protocol, and First Frontier Compilation

**Project code:** `CSM_RH`  
**Parent theory:** Closure-Space Mathematics (`CSM`)  
**Research engine:** `GLM_RH`  
**Date:** 2026-09-03  
**Status:** research framework / proof-space compiler; not a proof or disproof of RH.  
**中文標題：** 閉包空間數學論應用於黎曼猜想：正則域模型、GLM_RH 研究協定與首次前沿編譯  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**Language:** English

---

# 0. Trust boundary

This document does not claim a proof or disproof of the Riemann Hypothesis.

Canonical status:

```text
RH_PROVED = FALSE
RH_DISPROVED = FALSE
GLOBAL_RH_CERTIFICATE = FALSE
CSM_RH_ROOT_STATUS = OPEN
```

Finite computation, finite-height zero verification, finite cell verification, finite matrix positivity, finite prime data, or finite numbers of closure events are not sufficient to promote the root target to `PROVED`.

All generated bridge propositions from `GLM_RH` are provisional proof obligations until independently discharged.

---

# 1. Why CSM_RH is being introduced now

The current RH program has already produced many successful local reductions:

- hypothetical off-axis zeros can be placed into rational off-axis cells;
- local Weil restrictions can expose negative inertia;
- explicit-formula admissibility has been substantially normalized;
- fixed-aperture observables have been tied quantitatively to zero-strip width;
- prime-side minor arcs admit genuine polynomial savings;
- character major arcs can be decomposed into zero packets;
- density-only arguments have been shown insufficient for the fixed-power major-arc gate.

The remaining difficulty repeatedly reappears under different representations.

The present problem is therefore no longer well described as:

> find one more lemma.

It is better described as:

> determine whether the remaining open obligations are genuinely distinct, prove transfer relations between them, quotient equivalent obstruction classes, and force every new generated route to demonstrate real closure gain before research resources are spent on it.

This is the role of `CSM_RH`.

---

# 2. Root mathematical target

Let $Z_{\mathrm{nt}}(\zeta)$ denote the multiset of nontrivial zeros of the Riemann zeta function.

The root target is

$$
\mathrm{RH}:
\qquad
\forall \rho \in Z_{\mathrm{nt}}(\zeta),
\qquad
\Re(\rho)=\frac12.
$$

The canonical negation object is

$$
\neg\mathrm{RH}:
\qquad
\exists \rho \in Z_{\mathrm{nt}}(\zeta)
\text{ such that }
\Re(\rho)\neq\frac12.
$$

By the functional-equation symmetry, an off-axis zero may be represented through a right-half-plane witness

$$
\rho=\frac12+\delta+i\gamma,
\qquad
\delta>0.
$$

`CSM_RH` treats this witness as a typed mathematical object, not merely as a narrative assumption.

---

# 3. CSM_RH is a specialization, not a replacement of CSM

The mother theory remains `CSM`.

`CSM_RH` is the RH-specific domain model obtained by fixing:

- the root theorem target;
- admissible mathematical domains;
- RH-specific representations;
- known equivalence criteria;
- route families;
- obstruction classes;
- frontier classes;
- closure and reopening rules;
- proof-strength auditing rules.

Thus:

```text
CSM
  -> CSM_RH
```

is a specialization relation.

No general CSM axiom is silently strengthened merely because the application target is RH.

---

# 4. Core domain stratification

The first canonical RH domain family is

```text
D0  ROOT-RH
D1  ZERO-GEOMETRY
D2  WEIL-POSITIVITY
D3  LI-CRITERION
D4  EXPLICIT-FORMULA
D5  LOCAL-PRIME
D6  PRIME-CORRELATION
D7  MAJOR-MINOR-ARC
D8  CHARACTER-ZERO-PACKET
D9  FORMAL-VERIFICATION
```

These domains are linked, but they are not identified.

A theorem, obstruction, or closure status transfers between two domains only through a certified bridge.

In particular:

$$
\text{local negative block}
\not\Rightarrow
\text{global Weil negativity}
$$

without an isolation or dominance theorem.

Likewise,

$$
\text{zero-density control}
\not\Rightarrow
\text{fixed rightmost-zero exclusion}
$$

without an additional extreme-zero mechanism.

---

# 5. Canonical object types

`CSM_RH` uses the following typed objects.

```text
TARGET
CLAIM
LEMMA
ASSUMPTION
REPRESENTATION
ROUTE
BRIDGE
OBSTRUCTION
SURVIVOR
FRONTIER
CERTIFICATE
DEBT
EQUIVALENCE
STRENGTH_AUDIT
COUNTERMODEL
ARTIFACT
VALIDATION
```

A document title such as `CLOSED`, `NO-GO`, `STOP`, or `OPEN` is not itself a theorem-level status.

It must first be compiled into these objects.

---

# 6. Canonical closure statuses

Base status:

```text
OPEN
CONDITIONAL
PROVED
REFUTED
BLOCKED
STALE
DEFERRED
```

Orthogonal tags:

```text
SURVIVOR
RH_EQUIVALENT
RH_COMPLETE
ZERO_STRIP_BREAKTHROUGH
LOCAL_ONLY
FINITE_ONLY
DENSITY_ONLY
REPRESENTATION_DEPENDENT
TRANSFER_DEBT
UNIFORMITY_DEBT
GLOBALIZATION_DEBT
```

`BLOCKED` never means that RH is refuted.

`SURVIVOR` never means that RH is supported.

---

# 7. First compilation of the current RH program

## 7.1 Off-axis rational-cell route

From the conditional off-axis cell program:

$$
\neg\mathrm{RH}
\Rightarrow
\exists C_{\mathbb Q}
\text{ containing an off-axis zero witness}.
$$

This transfer is treated as a closed conditional bridge.

The local Weil restriction then yields a negative direction on a finite-dimensional translated subspace.

But the promotion

$$
\text{local negative inertia}
\Rightarrow
\text{full Weil quadratic-form negativity}
$$

remains open.

Canonical frontier:

```text
F-RH-001
name: GLOBAL_WEIL_ISOLATION_DOMINANCE
status: OPEN
debt: GLOBALIZATION_DEBT
```

---

# 8. Fixed-aperture route

For a fixed-aperture observable, the current audit identifies a growth exponent with maximal horizontal zero displacement.

Write

$$
\Delta_\zeta
=
\sup_{\rho}
\left|
\Re(\rho)-\frac12
\right|.
$$

The audited route has the schematic form

$$
\sigma_h=\Delta_\zeta.
$$

Hence a subexponential tail condition of the form

$$
\mathfrak E_h(x)=x^{o(1)}
$$

is not a routine final estimate: it is an RH-level global condition.

Canonical obstruction:

```text
O-RH-001
name: RH_COMPLETE_TAIL_REPACKAGING
effect:
  reject any route that treats x^{o(1)} tail closure as a low-strength technical remainder
```

Canonical frontier:

```text
F-RH-002
name: GLOBAL_TAIL_INVARIANT
status: OPEN
tag: RH_COMPLETE
```

---

# 9. Character major-arc route

The current prime-side program has separated genuine minor arcs from structured major arcs.

For a zero

$$
\rho=\beta+i\gamma,
$$

the pole-zero channel appears at the scale

$$
x^{1+2\beta}.
$$

A proposed fixed-power energy estimate

$$
E_{\mathrm{pair}}(x)
\ll
x^{3-\eta+o(1)}
$$

with a fixed $\eta>0$ would force

$$
1+2\beta
\le
3-\eta,
$$

hence

$$
\beta
\le
1-\frac{\eta}{2}.
$$

Therefore any candidate proof of such a fixed-power bound must be strength-audited before it is accepted as a mere analytic estimate.

Canonical obstruction:

```text
O-RH-002
name: EXTREME_ZERO_POWER_DOMINANCE
status: PROVED_AS_ROUTE_OBSTRUCTION
scope: character major-arc fixed-power route
```

Canonical obstruction:

```text
O-RH-003
name: DENSITY_ONLY_NO_GO
status: PROVED_AS_METHOD_LIMIT
scope: density-only derivation of fixed-power exceptional-major-arc closure
```

Canonical frontier:

```text
F-RH-003
name: EXCEPTIONAL_MAJOR_ARC_ENERGY
status: OPEN
abbrev: EMAE
```

---

# 10. The first obstruction quotient problem

The following three frontiers must not yet be declared mathematically equivalent:

```text
F-RH-001  GLOBAL_WEIL_ISOLATION_DOMINANCE
F-RH-002  GLOBAL_TAIL_INVARIANT
F-RH-003  EXCEPTIONAL_MAJOR_ARC_ENERGY
```

However, all three currently exhibit the same high-level failure pattern:

$$
\text{local or averaged control}
+
\text{a possible single extreme off-axis zero}
\Rightarrow
\text{global closure failure}.
$$

Define the provisional obstruction class

```text
QO-RH-A
name: SINGLE_EXTREME_ZERO_GLOBALIZATION_BARRIER
status: QUOTIENT_CANDIDATE
```

This quotient is not theorem-authoritative until bridge certificates are proved.

The research question is no longer merely whether each frontier can be solved independently.

It is also whether there exists a common invariant whose discharge closes all three.

---

# 11. CSM_RH novelty filter

Every new `GLM_RH` candidate must pass at least one of the following tests.

A candidate has genuine closure value only if it does one or more of:

1. closes an existing frontier;
2. strictly weakens the theorem strength required by an existing frontier;
3. proves a new transfer certificate between two frontier classes;
4. proves that two obstruction classes are equivalent and may be quotiented;
5. breaks an existing no-go by violating one of its assumptions;
6. supplies a new representation with a formally verified non-lossy bridge;
7. converts an infinite family of proof obligations into a finite or finitely generated certified exhaustion;
8. proves a structural cancellation or positivity theorem not already equivalent to the target.

If none apply, the candidate is classified as:

```text
REPACKAGING_ONLY
```

and is not promoted to a new principal RH version.

---

# 12. GLM_RH role

`GLM_RH` is the generative research engine operating inside `CSM_RH`.

Its purpose is not to decide truth by generation.

Its purpose is to generate candidate mathematical objects and immediately turn them into explicit proof obligations.

The canonical loop is:

```text
TARGET
-> BACKWARD OBLIGATION GENERATION
-> CANDIDATE BRIDGE / LEMMA GENERATION
-> STRENGTH AUDIT
-> ADVERSARIAL AUDIT
-> CSM_RH COMPILE
-> OBSTRUCTION PROPAGATION
-> QUOTIENT / SPLIT / REOPEN
-> PRIORITY SELECTION
-> PROOF ATTEMPT
-> INDEPENDENT VALIDATION
-> LEDGER COMMIT
```

---

# 13. GLM_RH backward generation rule

Let the target be $T$.

`GLM_RH` may generate a candidate intermediate statement $M$ such that

$$
M\Rightarrow T.
$$

But the generation direction

$$
T\rightsquigarrow M
$$

is not a proof direction.

The proof direction remains

$$
M\to T.
$$

Any generated bridge axiom is immediately downgraded to

```text
PROOF_OBLIGATION
```

until independently proved.

This prevents a generated intermediate theorem from silently importing RH itself.

---

# 14. Strength audit

For every candidate gate $G$, `CSM_RH` records:

```text
target_implication:
reverse_implication:
known_equivalence:
fixed_power_required:
uniformity_required:
extreme_zero_effect:
single_zero_test:
known_theorem_strength:
```

Strength classes:

```text
S0  ROUTINE / KNOWN-STRENGTH
S1  NONTRIVIAL BUT SUB-BREAKTHROUGH
S2  NEW ZERO-STRIP STRENGTH
S3  RH-COMPLETE / RH-EQUIVALENT
S4  STRONGER-THAN-RH OR UNJUSTIFIED
```

Example:

If a candidate $G(\eta)$ implies

$$
\Re(\rho)\le1-\frac{\eta}{2}
$$

for every nontrivial zero and some fixed $\eta>0$, then it is at least

```text
S2 = NEW ZERO-STRIP STRENGTH
```

unless that strip already follows from accepted theorems at the same strength.

If the candidate forces

$$
\Re(\rho)\le\frac12,
$$

then by symmetry it reaches RH-level strength and must be marked accordingly.

---

# 15. Single-zero adversarial audit

Every global candidate is tested against the abstract witness

$$
\rho_0
=
\frac12+\delta+i\gamma_0,
\qquad
\delta>0.
$$

The audit asks:

1. does the candidate estimate retain a contribution growing like $x^{c\delta}$ ;
2. does a conductor or height weight become only a fixed nonzero constant for a fixed zero;
3. does smoothing actually suppress the witness in power scale or only in constant scale;
4. is cancellation structural and theorem-forced, or merely hoped for;
5. can the kernel vanish on the dangerous witness without already knowing its location;
6. does the claimed bound imply a new zero strip.

If the witness survives with an uncancelled fixed-power contribution, the route is attached to `O-RH-002`.

---

# 16. Finite-verification firewall

The following implication is forbidden without a separate completeness theorem:

$$
\text{all tested instances pass}
\not\Rightarrow
\mathrm{RH}.
$$

This includes:

- zeros up to finite height;
- finitely many rational cells;
- finitely many Li coefficients;
- finitely many local-prime checkpoints;
- finitely many matrices;
- finitely many major arcs;
- finitely many numerical samples.

Canonical obstruction:

```text
O-RH-004
name: FINITE_VERIFICATION_NONCOMPLETENESS
status: ACTIVE
```

A finite computation may discharge a finite sub-obligation, validate normalization, reject a candidate, or certify an exact finite identity.

It may not close the root theorem without a proved finite-to-global bridge.

---

# 17. Representation firewall

The following representations are currently useful but non-identical:

```text
R-ZERO-CELL
R-WEIL-QUADRATIC
R-LI-SEQUENCE
R-FIXED-APERTURE
R-LOCAL-PRIME
R-FOURIER-PAIR
R-CHARACTER-PACKET
R-MAJOR-ARC-ENERGY
```

A transfer edge must state what is preserved.

For a bridge $B:R_i\to R_j$, record:

```text
target_fidelity
quantifier_preservation
sign_preservation
uniformity_preservation
multiplicity_preservation
asymptotic_loss
exceptional_set_loss
inverse_available
```

A representation change is never considered progress merely because the formula looks simpler.

---

# 18. Reopening rule

A blocked route is reopened when a new candidate invalidates at least one assumption of its obstruction certificate.

For example, `DENSITY_ONLY_NO_GO` blocks only routes whose decisive input is density control alone.

A new theorem containing an independently proved extreme-zero repulsion, exact structural cancellation, or another non-density mechanism is not automatically blocked by that no-go.

Thus:

```text
BLOCKED != DEAD
```

The blockage is typed and assumption-dependent.

---

# 19. First survivor families

After the current obstruction compilation, the following broad survivor mechanisms remain conceptually distinct:

```text
S-RH-001  STRUCTURAL_ZERO_PACKET_CANCELLATION
S-RH-002  EXTREME_ZERO_REPULSION_OR_EXCLUSION
S-RH-003  GLOBAL_POSITIVITY_OR_COERCIVITY
S-RH-004  NONLOSSY_GLOBAL_COMPRESSION
S-RH-005  CERTIFIED_EXHAUSTION_OF_OFF_AXIS_FAILURE_MODES
S-RH-006  NEW_INVARIANT_COUPLING_ZERO_SIDE_AND_PRIME_SIDE
```

These are research families, not claims that such theorems exist.

A GLM_RH run should attempt to instantiate one of these families or generate a genuinely new family.

---

# 20. Priority function

A candidate research object $X$ receives a priority score based on certified closure gain rather than apparent novelty.

A schematic score is

$$
P(X)
=
\frac{
w_f\Delta F(X)
+
w_o\Delta O(X)
+
w_b\Delta B(X)
+
w_q\Delta Q(X)
}{
1+C(X)+D(X)
},
$$

where:

- $\Delta F(X)$ is frontier contraction;
- $\Delta O(X)$ is obstruction discharge;
- $\Delta B(X)$ is new bridge authority;
- $\Delta Q(X)$ is quotient compression;
- $C(X)$ is expected proof cost;
- $D(X)$ is newly introduced proof debt.

The weights are policy parameters and carry no theorem authority.

---

# 21. First CSM_RH research question

The first high-value question is:

> Are `F-RH-001`, `F-RH-002`, and `F-RH-003` three independent hard problems, or three representations of one deeper global single-extreme-zero obstruction?

This becomes a formal bridge program.

Required candidate bridges:

```text
B-RH-A1:
  GLOBAL_WEIL_ISOLATION_DOMINANCE
  -> SINGLE_EXTREME_ZERO_GLOBALIZATION_BARRIER

B-RH-A2:
  GLOBAL_TAIL_INVARIANT
  -> SINGLE_EXTREME_ZERO_GLOBALIZATION_BARRIER

B-RH-A3:
  EXCEPTIONAL_MAJOR_ARC_ENERGY
  -> SINGLE_EXTREME_ZERO_GLOBALIZATION_BARRIER
```

Then attempt reverse or partial reverse bridges.

Only after these are proved may `QO-RH-A` be promoted from `QUOTIENT_CANDIDATE` to a certified obstruction quotient.

This is the first place where `CSM_RH` may create real research compression.

---

# 22. First GLM_RH generation campaign

The first campaign should not ask:

> prove RH.

It should ask:

> generate the weakest new invariant that survives all currently certified no-go filters and would close at least two of the three principal frontiers without assuming an RH-equivalent tail or a fixed zero strip as an input.

Generation constraints:

```text
C1  no RH-equivalent premise
C2  no unproved fixed zero strip
C3  no finite verification promoted to global proof
C4  no density-only closure of extreme zeros
C5  no local-to-global promotion without certificate
C6  no representation change counted as theorem progress
C7  every provisional axiom becomes a proof obligation
C8  every candidate must expose its single-zero response
C9  every candidate must state exact quantifier order
C10 every candidate must state uniformity requirements
```

---

# 23. Candidate output schema

Every GLM_RH candidate should be emitted in the form:

```yaml
candidate_id:
title:
source_frontier_ids:
target_frontier_ids:
statement:
domain:
representation:
assumptions:
quantifiers:
proof_direction:
known_implications:
possible_reverse_implications:
single_zero_response:
strength_class:
known_obstruction_hits:
new_debt:
required_bridge_certificates:
falsification_tests:
finite_checks:
formalization_notes:
status: PROOF_OBLIGATION
```

No candidate receives theorem status at generation time.

---

# 24. Canonical first seed graph

The seed graph contains:

```text
ROOT
  T-RH-000  RIEMANN_HYPOTHESIS

FRONTIERS
  F-RH-001  GLOBAL_WEIL_ISOLATION_DOMINANCE
  F-RH-002  GLOBAL_TAIL_INVARIANT
  F-RH-003  EXCEPTIONAL_MAJOR_ARC_ENERGY

OBSTRUCTIONS
  O-RH-001  RH_COMPLETE_TAIL_REPACKAGING
  O-RH-002  EXTREME_ZERO_POWER_DOMINANCE
  O-RH-003  DENSITY_ONLY_NO_GO
  O-RH-004  FINITE_VERIFICATION_NONCOMPLETENESS

QUOTIENT CANDIDATE
  QO-RH-A   SINGLE_EXTREME_ZERO_GLOBALIZATION_BARRIER

SURVIVOR FAMILIES
  S-RH-001  STRUCTURAL_ZERO_PACKET_CANCELLATION
  S-RH-002  EXTREME_ZERO_REPULSION_OR_EXCLUSION
  S-RH-003  GLOBAL_POSITIVITY_OR_COERCIVITY
  S-RH-004  NONLOSSY_GLOBAL_COMPRESSION
  S-RH-005  CERTIFIED_EXHAUSTION_OF_OFF_AXIS_FAILURE_MODES
  S-RH-006  NEW_INVARIANT_COUPLING_ZERO_SIDE_AND_PRIME_SIDE
```

---

# 25. Versioning rule

The previous AMRAL RH artifacts are not discarded.

They become source artifacts compiled into the `CSM_RH` graph.

Therefore the relationship is:

```text
AMRAL_RH corpus
  -> source evidence / routes / local certificates

CSM_RH
  -> canonical closure-space state

GLM_RH
  -> active candidate generator

formal / analytic verification
  -> authority promotion
```

This preserves the full research trace while preventing version-number growth from being mistaken for mathematical progress.

---

# 26. Immediate next artifact

The recommended next artifact is:

```text
CSM_RH_Paper_01
Obstruction Quotient and Single-Extreme-Zero Globalization Barrier
```

Its target is not RH directly.

Its target is to determine whether the current Weil, fixed-aperture, and character-major-arc frontiers share a certified common obstruction.

Success criteria:

1. construct explicit typed bridges from all three frontiers to a common obstruction object;
2. identify exactly what information is lost in each transfer;
3. test whether any reverse bridge can be proved;
4. classify the common obstruction's theorem strength;
5. derive a minimal survivor condition that is not already RH-equivalent by definition;
6. emit the resulting reduced frontier for the first constrained `GLM_RH` generation campaign.

---

# 27. Canonical status

At `CSM_RH v0.1`:

```text
ROOT_RH = OPEN

F-RH-001 = OPEN
F-RH-002 = OPEN
F-RH-003 = OPEN

QO-RH-A = QUOTIENT_CANDIDATE

GLM_RH = ENABLED_AS_GENERATIVE_RESEARCH_PROTOCOL
AUTOMATIC_THEOREM_PROMOTION = DISABLED
FINITE_TO_GLOBAL_PROMOTION = DISABLED
UNVERIFIED_BRIDGE_PROMOTION = DISABLED
```

The strategic change is therefore:

> Stop treating each newly derived RH-equivalent condition as a new endgame. Compile it into the closure space first. Generate only against the surviving frontier, and require measurable closure gain before a candidate becomes a new principal route.

This is the canonical starting point of `CSM_RH`.
