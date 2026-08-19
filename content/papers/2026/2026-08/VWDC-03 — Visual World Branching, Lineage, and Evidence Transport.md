# VWDC-03 — Visual World Branching, Lineage, and Evidence Transport
## 視覺世界分支、譜系與證據轉移：共同祖先、Sibling Dependence、失效傳播、Replay 與 Reality Transport

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 03  
**Depends on:** VWDC-01–02, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal branching-evidence paper. Shared-ancestry dependence, equicorrelated effective sample size, paired-counterfactual coupling, evaluator common-mode dependence, lineage-family aggregation, deterministic descendant invalidation, clean-checkpoint replay, merge admissibility, universal-claim counterexample logic, simulation-consensus no-go, evidence-transport error composition, and evidence-provenance DAG results are proved under explicit hypotheses. Counterfactual simulation, digital-twin validation, simulation validation, provenance systems, common-random-number coupling, and causal evidence transport are established neighboring ideas and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** branching worlds, sibling dependence, common ancestry, counterfactual simulation, evidence aggregation, effective sample size, provenance DAG, replay, invalidation, checkpoint, digital twin validation, reality transport, WDC, GVSS

---

# Abstract

VWDC-01 established:

$$
\boxed{
\text{Visual State}
\neq
\text{Runnable World State}.
}
$$

VWDC-02 established a typed mixed visual/world graph with:

- GENERATE;
- EDIT;
- LIFT;
- VALIDATE;
- FORK;
- INTERVENE;
- RENDER;
- CHECKPOINT;
- RESTORE;
- EVALUATE;

and showed that execution state can recur while provenance lineage remains acyclic.

VWDC-03 studies what happens when that graph branches.

The central warning is:

$$
\boxed{
\text{different world IDs}
\not\Rightarrow
\text{independent evidence sources}.
}
$$

Two sibling worlds can have:

- different world IDs;
- different post-fork trajectories;
- different rendered images;

while sharing:

- the same parent checkpoint;
- the same dynamics model;
- the same hidden parameter error;
- the same visual provider;
- the same evaluator;
- the same training data;
- the same external assumptions.

Therefore branch multiplicity is not evidence multiplicity.

---

# 1. Branch ancestry

Let a parent checkpoint be:

$$
\boxed{
C_0.
}
$$

From it fork sibling worlds:

$$
\boxed{
W_1,\ldots,W_n.
}
$$

Each world receives a unique identity and post-fork history:

$$
H_i^{+}.
$$

The shared prefix is:

$$
H^{-}.
$$

The lineage record contains:

$$
\boxed{
\mathsf{Lin}(W_i)
=
(
ParentID,
CheckpointID,
ForkTime,
DivergenceContract_i,
ModelVersion_i,
ProviderVersion_i,
EvaluatorProfile_i
).
}
$$

Sibling worlds are operationally distinct.

That fact alone does not imply statistical or epistemic independence.

---

# 2. Shared latent ancestry model

Let:

$$
\boxed{
H
}
$$

represent all shared branch-level uncertainty inherited from common ancestry.

Examples:

- uncertain parent state;
- model misspecification;
- latent physics parameter;
- shared renderer bias;
- shared evaluator bias;
- common dataset bias.

Let branch-local randomness be:

$$
\varepsilon_i.
$$

Let output statistic be:

$$
\boxed{
Y_i
=
f_i(
H,\varepsilon_i
).
}
$$

Assume:

$$
\varepsilon_i
\perp
\varepsilon_j
\mid H.
$$

Then sibling outputs may be conditionally independent given $H$ while remaining marginally dependent.

---

# 3. VWDC03-T1 — Shared-ancestry covariance decomposition

## Theorem VWDC03-T1

If:

$$
Y_i
\perp
Y_j
\mid H,
$$

and second moments exist, then:

$$
\boxed{
\operatorname{Cov}(Y_i,Y_j)
=
\operatorname{Cov}
\left(
E[Y_i\mid H],
E[Y_j\mid H]
\right).
}
$$

### Proof

By the law of total covariance:

$$
\operatorname{Cov}(Y_i,Y_j)
=
E[
\operatorname{Cov}(Y_i,Y_j\mid H)
]
+
\operatorname{Cov}
(
E[Y_i\mid H],
E[Y_j\mid H]
).
$$

Conditional independence makes the first term zero.

 $\square$

---

# 4. Consequence

Independent post-fork seeds do not erase shared parent/model dependence.

If all siblings respond similarly to a shared model error $H$, their outputs remain correlated.

Thus:

$$
\boxed{
\text{independent branch-local randomness}
\not\Rightarrow
\text{independent sibling evidence}.
}
$$

---

# 5. Simple additive common-mode model

Let:

$$
\boxed{
Y_i
=
\mu
+
B
+
\varepsilon_i,
}
$$

with:

$$
E[B]=0,
$$

$$
E[\varepsilon_i]=0,
$$

$$
B\perp\varepsilon_i,
$$

and independent:

$$
\varepsilon_i.
$$

Then:

$$
\boxed{
\operatorname{Cov}(Y_i,Y_j)
=
\operatorname{Var}(B)
\quad
(i\neq j).
}
$$

All branches can share one common bias even when their local noise is independent.

---

# 6. Branch count versus effective sample size

Suppose branch outputs are exchangeable with:

$$
\operatorname{Var}(Y_i)=\sigma^2
$$

and pairwise correlation:

$$
\operatorname{Corr}(Y_i,Y_j)=\rho.
$$

Then the mean:

$$
\bar Y
=
\frac1n
\sum_{i=1}^n
Y_i
$$

has variance:

$$
\boxed{
\operatorname{Var}(\bar Y)
=
\frac{\sigma^2}{n}
[
1+(n-1)\rho
].
}
$$

---

# 7. VWDC03-T2 — Equicorrelated effective branch count

## Theorem VWDC03-T2

Define:

$$
n_{\mathrm{eff}}
$$

by:

$$
\operatorname{Var}(\bar Y)
=
\frac{\sigma^2}{n_{\mathrm{eff}}}.
$$

Then:

$$
\boxed{
n_{\mathrm{eff}}
=
\frac{
n
}{
1+(n-1)\rho
}.
}
$$

### Proof

Equate the two variance expressions.

 $\square$

---

# 8. Interpretation

If:

$$
\rho=0,
$$

then:

$$
n_{\mathrm{eff}}=n.
$$

If:

$$
\rho\to1,
$$

then:

$$
n_{\mathrm{eff}}\to1.
$$

Thus 100 highly dependent sibling worlds can carry evidence comparable to roughly one independent unit for a mean-estimation task.

---

# 9. Negative correlation boundary

When admissible:

$$
\rho<0,
$$

effective sample size can exceed $n$ for estimating a mean.

The covariance structure must remain positive semidefinite:

$$
\rho
\ge
-\frac1{n-1}.
$$

VWDC therefore does not equate dependence with universally lower statistical value.

---

# 10. Replication versus contrast

The purpose of branches matters.

There are at least two distinct epistemic tasks:

### Independent replication

Ask:

> Does the same conclusion survive independent models/seeds/lineages?

### Paired counterfactual contrast

Ask:

> Holding nuisance factors fixed, what changes when one intervention changes?

These goals prefer different dependence structures.

---

# 11. Noise-coupled counterfactual branches

Let two sibling branches share:

- factual prefix;
- exogenous noise;
- model state;

but diverge only in action/intervention:

$$
a_0
\neq
a_1.
$$

Let branch outputs be:

$$
Y_0,
Y_1.
$$

The contrast is:

$$
\boxed{
\Delta
=
Y_1-Y_0.
}
$$

---

# 12. VWDC03-T3 — Positive branch coupling can reduce contrast variance

## Theorem VWDC03-T3

If:

$$
\operatorname{Var}(Y_0)
=
\operatorname{Var}(Y_1)
=
\sigma^2
$$

and:

$$
\operatorname{Corr}(Y_0,Y_1)=\rho,
$$

then:

$$
\boxed{
\operatorname{Var}(
Y_1-Y_0
)
=
2\sigma^2(
1-\rho
).
}
$$

### Proof

$$
\operatorname{Var}(Y_1-Y_0)
=
\operatorname{Var}(Y_1)
+
\operatorname{Var}(Y_0)
-
2\operatorname{Cov}(Y_1,Y_0).
$$

Substitute:

$$
\operatorname{Cov}(Y_1,Y_0)
=
\rho\sigma^2.
$$

 $\square$

---

# 13. Dependence dual-use principle

Positive correlation:

- reduces independent-replication effective sample size;
- can improve precision of paired intervention contrasts.

Therefore:

$$
\boxed{
\text{dependence for replication}
\neq
\text{coupling for causal contrast}.
}
$$

A runtime should declare which evidence task a branch family serves.

---

# 14. Current Twin Rollouts precedent

The 2026 **Twin Rollouts** framework studies noise-coupled factual/counterfactual branches in interactive video world models.

The two branches:

- share a generated prefix;
- share future exogenous noise;
- differ in action stream after an intervention time.

This is a direct modern precedent for deliberately dependent sibling branches used for minimal-change counterfactual comparison.

VWDC does not claim noise coupling itself as new.

---

# 15. Branch independence profile

## Definition VWDC03-D1

For branch $W_i$, define:

$$
\boxed{
\mathsf{IP}_i
=
(
L_i,
M_i,
D_i,
P_i,
E_i,
R_i,
S_i
),
}
$$

where:

- $L_i$: lineage family;
- $M_i$: dynamics/world-model family;
- $D_i$: training/input data family;
- $P_i$: provider/backend;
- $E_i$: evaluator/observer;
- $R_i$: randomness coupling;
- $S_i$: shared infrastructure/assumption profile.

This is not one scalar independence score.

---

# 16. Lineage family

## Definition VWDC03-D2

A lineage family is a set of branches sharing a declared common root/checkpoint/model ancestry relevant to the evidence claim.

The exact family partition is claim dependent.

---

# 17. Different world ID is insufficient

Two branches can satisfy:

$$
ID(W_i)\neq ID(W_j)
$$

while:

$$
L_i=L_j,
\quad
M_i=M_j,
\quad
E_i=E_j.
$$

They are distinct executions, not necessarily independent confirmations.

---

# 18. Evaluator common-mode dependence

Suppose branch latent scores:

$$
Z_i
$$

are independent.

Shared evaluator bias:

$$
B_E
$$

produces reported scores:

$$
\boxed{
S_i
=
Z_i+B_E.
}
$$

Then for:

$$
i\neq j,
$$

$$
\boxed{
\operatorname{Cov}(S_i,S_j)
=
\operatorname{Var}(B_E).
}
$$

Thus even independent world rollouts can become dependent evidence after a shared evaluator.

---

# 19. VWDC03-N1 — Provider diversity does not imply evaluator diversity

If all branch outputs are judged through the same biased evaluator, increasing provider/world diversity does not remove evaluator common-mode bias.

Therefore:

$$
\boxed{
\text{world/provider diversity}
\not\Rightarrow
\text{observer independence}.
}
$$

This inherits GVSS-09 and WDC-05.

---

# 20. Evidence packet

## Definition VWDC03-D3

Each evidence unit is:

$$
\boxed{
E_i
=
(
EvidenceID,
WorldID,
CheckpointID,
LineageFamily,
InterventionID,
ModelVersion,
ProviderVersion,
EvaluatorVersion,
EvidenceScope,
Dependencies,
TransportStatus
).
}
$$

---

# 21. Evidence dependency DAG

Let:

$$
\boxed{
G_E
=
(
V_E,
E_E
)
}
$$

be a DAG where edge:

$$
u\to v
$$

means evidence/artifact $v$ depends on $u$.

Dependencies include:

- data derivation;
- evaluator use;
- provider transformation;
- checkpoint ancestry;
- world-model inference;
- deterministic postprocessing.

---

# 22. Descendant closure

For invalidated source:

$$
s,
$$

define:

$$
\boxed{
\operatorname{Desc}(s)
}
$$

as all evidence nodes reachable from $s$ in $G_E$.

---

# 23. VWDC03-T4 — Deterministic dependency invalidation closure

## Theorem VWDC03-T4

Assume every outgoing dependency edge from source $u$ means:

> the child artifact/evidence claim is valid only if $u$ is valid.

If source $s$ is invalidated, then every node in:

$$
\boxed{
\{s\}
\cup
\operatorname{Desc}(s)
}
$$

must be marked invalid or pending recomputation.

### Proof

Induction on path length from $s$.

Every direct child depends on invalid $s$.

If all nodes at distance $k$ are invalid, every child at distance $k+1$ has an invalid required parent.

 $\square$

---

# 24. Minimality under exact dependency semantics

If the DAG contains **all and only** necessary deterministic dependencies, descendants not reachable from $s$ do not require invalidation solely because of $s$.

Thus descendant closure is the exact syntactic invalidation set under the declared dependency graph.

Semantic dependencies missing from the graph break this guarantee.

---

# 25. Provenance completeness requirement

If evaluator $E^\star$ influenced a score but the dependency was not recorded, later evaluator invalidation cannot propagate exactly.

Therefore:

$$
\boxed{
\text{missing provenance}
\Longrightarrow
\text{invalidation debt}.
}
$$

---

# 26. Evaluator invalidation example

Suppose:

$$
W_i
\to
I_i
\to
E^\star(I_i)
\to
Score_i
\to
Aggregate.
$$

If:

$$
E^\star
$$

is invalidated, every dependent:

- score;
- branch ranking;
- aggregate;
- downstream decision;

belongs to the invalidation closure.

The raw world trajectory need not be invalidated if it did not depend on $E^\star$.

---

# 27. Provider invalidation example

If a visual transformation provider is invalidated:

$$
I
\to
\widetilde I
\to
Evaluator
\to
Decision,
$$

then transformed descendants require replay.

The original source world observation can remain valid.

---

# 28. Checkpoint replay

Let:

$$
C
$$

be a clean checkpoint preceding the invalid dependency.

Suppose replay pipeline is deterministic conditional on recorded:

- checkpoint;
- actions;
- model versions;
- seeds/random streams;
- external inputs.

---

# 29. Replay function

Define:

$$
\boxed{
\mathsf{Replay}
(
C,
A,
M,
\Xi,
X_{\mathrm{ext}}
)
}
$$

where:

- $A$ is action sequence;
- $M$ model/version bundle;
- $\Xi$ random-state bundle;
- $X_{\mathrm{ext}}$ external inputs.

---

# 30. VWDC03-T5 — Clean-checkpoint replay correctness

## Theorem VWDC03-T5

Assume:

1. the checkpoint is exact under the replay contract;
2. every transition/evaluator/provider used in replay is deterministic conditional on recorded inputs;
3. all external inputs and random states are recorded;
4. invalid components are replaced or removed according to a declared corrected pipeline.

Then replay from the clean checkpoint reproduces exactly the output of the corrected pipeline on those recorded inputs.

### Proof

Induct over the ordered deterministic pipeline.

Equal starting state and equal recorded inputs imply equal next state/artifact at every corrected stage.

 $\square$

---

# 31. Replay does not reconstruct missing counterfactual history

If:

- seeds are missing;
- external API responses changed;
- model version disappeared;
- checkpoint is approximate;

exact replay is not guaranteed.

Provenance and reproducibility are distinct.

---

# 32. Replay status

Recommended:

```text
EXACT_REPLAYABLE
APPROX_REPLAYABLE
PROVENANCE_ONLY
UNREPLAYABLE
```

---

# 33. Replay child identity

A replay creates a new execution identity:

$$
ID_{\mathrm{replay}}
\neq
ID_{\mathrm{historical}}.
$$

Even if states and outputs match exactly, historical lineage is not overwritten.

---

# 34. Invalidation state

Evidence nodes can use:

```text
VALID
STALE
INVALID
PENDING_REPLAY
REPLAYED
SUPERSEDED
```

---

# 35. Branch aggregation

Let branch evidence statistics be:

$$
Y_1,\ldots,Y_n.
$$

A naive aggregate can use:

$$
\bar Y.
$$

But its uncertainty depends on covariance matrix:

$$
\Sigma.
$$

---

# 36. General variance of branch mean

$$
\boxed{
\operatorname{Var}(\bar Y)
=
\frac1{n^2}
\mathbf 1^\top
\Sigma
\mathbf 1.
}
$$

This is the correct second-moment branch aggregation formula.

---

# 37. VWDC03-T6 — Correlation-blind standard error can be arbitrarily optimistic

## Proposition VWDC03-T6

Suppose:

$$
Y_i=Z
$$

for all $i$.

Then:

$$
\rho=1,
$$

and:

$$
\bar Y=Z.
$$

True variance:

$$
\boxed{
\operatorname{Var}(\bar Y)
=
\operatorname{Var}(Z),
}
$$

while an independence-assuming estimator would scale variance as:

$$
\operatorname{Var}(Z)/n.
$$

The ratio is:

$$
\boxed{
n.
}
$$

Thus the independence assumption can underestimate variance by an arbitrarily large factor as branch count grows.

 $\square$

---

# 38. One-world-one-vote no-go

Voting every world ID equally is not justified when branches share dependence structures.

World IDs are runtime identities, not evidence weights.

---

# 39. Cluster-aware aggregation

One conservative approach:

1. group evidence by lineage/model/evaluator families;
2. aggregate within clusters;
3. combine clusters with explicit covariance/robust weighting.

VWDC-03 does not prescribe one universal estimator.

---

# 40. Independent replication unit

A branch can be called an independent replication unit only relative to a declared claim and dependence model.

Examples:

### Stronger independence

- independent root data;
- independent model family;
- independent evaluator;
- independent infrastructure.

### Weaker independence

- same checkpoint;
- same model;
- different seed.

The latter is still useful exploration but not equivalent evidence.

---

# 41. Counterexample asymmetry

Universal claims are logically asymmetric.

Suppose claim:

$$
\boxed{
\forall W\in\mathcal C,\quad
P(W).
}
$$

One valid world in the declared class with:

$$
\neg P(W^\star)
$$

refutes the universal claim over $\mathcal C$.

---

# 42. VWDC03-T7 — Valid branch counterexample refutes a universal world-class claim

## Theorem VWDC03-T7

If:

$$
W^\star\in\mathcal C
$$

and:

$$
\neg P(W^\star),
$$

then:

$$
\boxed{
\neg
[
\forall W\in\mathcal C,\,
P(W)
].
}
$$

### Proof

Elementary first-order logic.

 $\square$

---

# 43. Reality boundary of the counterexample

The theorem refutes a universal claim over the modeled world class.

It does not automatically prove a real-world counterexample exists.

Reality transport remains separate.

---

# 44. Simulation consensus

Suppose 1,000 branches all support claim:

$$
q.
$$

If every branch shares one systematically wrong model assumption, all 1,000 can agree and still be wrong relative to reality.

---

# 45. VWDC03-N2 — Simulation consensus does not validate reality

## Counterexample

Let every simulated world use biased transition law:

$$
M_{\mathrm{bad}}.
$$

Under:

$$
M_{\mathrm{bad}},
$$

every branch deterministically returns:

$$
q=1.
$$

Suppose real system truth is:

$$
q_R=0.
$$

Then simulation consensus is 100% while the reality claim is false.

Therefore:

$$
\boxed{
\text{simulation consensus}
\not\Rightarrow
\text{reality validation}.
}
$$

 $\square$

---

# 46. Current digital-twin validation precedent

The 2026 Digital Twin Counterfactual Framework explicitly separates validation levels and assumption-dependent counterfactual claims.

It emphasizes that simulated counterfactuals require hierarchical validation and that some joint counterfactual quantities remain assumption-indexed.

VWDC adopts the same broad caution:

$$
\boxed{
\text{counterfactual simulation}
\neq
\text{direct observed fact}.
}
$$

---

# 47. Subtrace-conditional validation precedent

2026 work on subtrace-conditional validation repeatedly initializes simulation from observed states and tests conditional output distributions while fixing selected stochastic primitives.

This is particularly relevant to VWDC:

- checkpoint-conditioned validation;
- input-model diagnostics;
- detecting misspecification hidden by marginal agreement.

VWDC does not claim simulation validation methods as new.

---

# 48. World-to-reality transport contract

Let:

$$
q_W
$$

be a world-derived statistic/claim.

Let:

$$
q_R
$$

be the corresponding reality target.

A transport contract supplies a discrepancy bound:

$$
\boxed{
d(
T(q_W),
q_R
)
\le
\delta_{\mathrm{trans}}.
}
$$

---

# 49. World estimation error

Suppose branch aggregation estimates:

$$
q_W
$$

by:

$$
\widehat q_W
$$

with:

$$
\boxed{
d_W(
\widehat q_W,
q_W
)
\le
\varepsilon_W.
}
$$

Assume transport map $T$ is $L_T$ -Lipschitz.

---

# 50. VWDC03-T8 — Evidence transport error composition

## Theorem VWDC03-T8

If:

$$
d_R(
T(q_W),
q_R
)
\le
\delta_{\mathrm{trans}},
$$

and:

$$
d_W(
\widehat q_W,
q_W
)
\le
\varepsilon_W,
$$

with $T$ $L_T$ -Lipschitz, then:

$$
\boxed{
d_R(
T(\widehat q_W),
q_R
)
\le
L_T
\varepsilon_W
+
\delta_{\mathrm{trans}}.
}
$$

### Proof

Triangle inequality:

$$
d_R(
T(\widehat q_W),
q_R
)
\le
d_R(
T(\widehat q_W),
T(q_W)
)
+
d_R(
T(q_W),
q_R
).
$$

Apply Lipschitzness and the two bounds.

 $\square$

---

# 51. Transport debt

Define:

$$
\boxed{
D_{\mathrm{transport}}
=
L_T\varepsilon_W
+
\delta_{\mathrm{trans}}.
}
$$

Branch replication can reduce:

$$
\varepsilon_W
$$

under appropriate independence.

It cannot automatically reduce model-to-reality discrepancy:

$$
\delta_{\mathrm{trans}}.
$$

This is a central asymmetry.

---

# 52. More worlds cannot wash away systematic transport error

If:

$$
\varepsilon_W\to0
$$

as branch count grows but:

$$
\delta_{\mathrm{trans}}>0,
$$

then:

$$
\boxed{
D_{\mathrm{transport}}
\to
\delta_{\mathrm{trans}},
}
$$

not zero.

Thus infinite simulation precision does not imply real-world validity.

---

# 53. World evidence scope

Every evidence packet must state:

```text
WORLD_INTERNAL
WORLD_CLASS_GENERALIZATION
REALITY_CANDIDATE
REALITY_VALIDATED
```

No implicit promotion.

---

# 54. Reality candidate

A world-derived claim can become:

```text
REALITY_CANDIDATE
```

when:

- target semantics match;
- transport contract exists;
- validation evidence exists;
- uncertainty is propagated.

It is not yet automatically reality validated.

---

# 55. External measurement

External real-world measurements can update/validate the transport model.

This is different from adding more simulated branches.

---

# 56. Branch merge

World branches are not merged merely because they agree.

Define partial typed merge:

$$
\boxed{
\mathsf{Merge}_\kappa:
\mathsf W^m
\rightharpoonup
\mathsf W.
}
$$

It is defined only when a reconciliation contract passes.

---

# 57. Merge contract

A world merge contract may require compatibility of:

- state schema;
- time;
- units;
- identity;
- rules;
- dynamics;
- causal history;
- unresolved contradictions;
- provenance.

---

# 58. VWDC03-N3 — Visual agreement does not authorize world merge

## Counterexample

Two sibling worlds render the same image:

$$
O(W_1)=O(W_2).
$$

But hidden velocities differ:

$$
v_1=+1,
\qquad
v_2=-1.
$$

A state merge based on visual equality would erase a genuine dynamics difference.

Therefore:

$$
\boxed{
\text{visual agreement}
\not\Rightarrow
\text{merge admissibility}.
}
$$

 $\square$

---

# 59. Evidence merge versus state merge

Evidence from multiple worlds can be aggregated without merging their states.

This preserves contradictory hypotheses.

Thus:

$$
\boxed{
\text{EvidenceMerge}
\neq
\text{StateMerge}.
}
$$

This inherits WDC-02.

---

# 60. Merge output provenance

A merged derived world receives:

- new identity;
- multiple parent IDs;
- merge contract;
- reconciliation record.

Lineage remains a DAG when the new node is created after all parents.

---

# 61. VWDC03-T9 — Multi-parent merge preserves lineage acyclicity under creation order

## Theorem VWDC03-T9

If every merge creates a new node with creation index greater than every parent node, the lineage graph remains acyclic.

### Proof

Every directed lineage edge strictly increases creation index.

A directed cycle is impossible.

 $\square$

---

# 62. Branch invalidation

Invalidating one branch-local evaluator may invalidate only descendants of that evaluator.

Invalidating a shared parent model may invalidate all sibling descendants that depend on it.

Thus invalidation scope follows dependency topology, not branch count.

---

# 63. Shared-model invalidation

If all siblings depend on:

$$
M^\star
$$

and:

$$
M^\star
$$

is invalidated, all dependent branch conclusions enter:

```text
PENDING_REPLAY
```

unless an alternate validation path exists.

---

# 64. Alternate support

An evidence claim can have multiple independent support paths.

If one support is invalidated but another remains valid, the claim need not be fully invalidated.

The dependency graph should distinguish:

- AND-dependencies;
- OR-supports.

VWDC-03 uses simple deterministic descendant closure only for required dependencies.

---

# 65. Hypergraph boundary

General evidence dependency can require hyperedges:

- claim valid if A AND B;
- claim valid if A OR B;
- claim valid if k-of-n supports.

A plain DAG may be insufficient.

VWDC-03 records this as future formalization.

---

# 66. Provenance research precedent

Pipeline-provenance work emphasizes that end-to-end trust and reproducibility require capture of processing steps, inputs, and dependency structure.

VWDC uses the same broad engineering principle for visual/world evidence lineage.

---

# 67. Provenance is not correctness

A perfectly recorded wrong model is still wrong.

Provenance supports:

- audit;
- invalidation;
- replay;
- diagnosis.

It does not prove semantic validity.

---

# 68. Checkpoint identity

A checkpoint is evidence about a particular world lineage state.

Restoring it twice produces two descendant executions.

They share ancestry even if post-restore seeds differ.

---

# 69. Shared-prefix depth

Define common-prefix depth:

$$
\boxed{
d_{\mathrm{share}}(
W_i,W_j
)
}
$$

as amount of common lineage before divergence.

Greater shared depth can indicate stronger dependence, but no universal monotone correlation theorem is claimed.

Dependence also comes from models/evaluators after the fork.

---

# 70. Lineage distance

A structural lineage distance can combine:

- nearest common ancestor depth;
- model-family divergence;
- evaluator divergence;
- random-stream coupling.

This is an engineering descriptor, not a universal metric.

---

# 71. Branch diversity vector

Define:

$$
\boxed{
\mathbf D_{ij}
=
(
D_{\mathrm{lineage}},
D_{\mathrm{model}},
D_{\mathrm{data}},
D_{\mathrm{provider}},
D_{\mathrm{evaluator}},
D_{\mathrm{random}},
D_{\mathrm{intervention}}
).
}
$$

Do not collapse it to one "independence score" without a claim-specific model.

---

# 72. Image diversity is not evidence diversity

Two sibling images can be visually far apart but generated by the same model/evaluator assumptions.

Conversely, two independent models can produce similar images.

Therefore:

$$
\boxed{
d_{\mathrm{visual}}
\not\Rightarrow
d_{\mathrm{evidence}}.
}
$$

---

# 73. VWDC03-N4 — Visual diversity does not certify evidence independence

Take branches sharing identical model bias $B$ but using different rendering seeds.

Images differ substantially.

The conclusion statistic includes $B$ in every branch.

Evidence remains common-mode dependent.

 $\square$

---

# 74. Branch intervention labels

Every branch should record what changed at fork:

```text
ACTION
PARAMETER
RULE
MODEL
SEED
PROVIDER
EVALUATOR
EXTERNAL_INPUT
```

Without this, causal contrasts are ambiguous.

---

# 75. Minimal-change counterfactual

A paired counterfactual aims to change one declared intervention while coupling nuisance randomness.

This strengthens causal contrast internal to the simulator.

It does not create independent replication.

---

# 76. Counterfactual branch packet

```text
parent_checkpoint
factual_branch
counterfactual_branch
intervention_variable
shared_noise_contract
shared_model_contract
divergence_time
comparison_metric
transport_scope
```

---

# 77. Twin-rollout warning

Shared future noise can make a counterfactual comparison more local/paired.

But the factual and counterfactual branches should not then be counted as two independent replications.

---

# 78. Branch aggregation objectives

Possible objectives:

### Mean prediction

Prefer many low-correlation replications.

### Counterfactual effect

Prefer controlled coupling and paired contrasts.

### Robustness/falsification

Prefer diverse models/assumptions.

### Failure search

Prefer branches that maximize uncovered hypothesis space.

The desired branch dependence depends on objective.

---

# 79. Branch allocation

WDC Governor should therefore allocate branch budget by **evidence purpose**, not simply branch count.

---

# 80. Evidence-purpose label

Recommended:

```text
REPLICATION
PAIRED_COUNTERFACTUAL
ROBUSTNESS_TEST
COUNTEREXAMPLE_SEARCH
SENSITIVITY_ANALYSIS
TRANSPORT_VALIDATION
```

---

# 81. Replication family

A replication family should record:

- independence assumptions;
- covariance estimate;
- effective sample size;
- common-mode risks.

---

# 82. Paired family

A paired counterfactual family should record:

- shared-noise contract;
- intervention delta;
- paired estimator;
- transport scope.

---

# 83. Counterexample family

A counterexample-search branch can be high value even if not representative.

Its job is falsification.

---

# 84. Consensus family

Consensus across branches should record:

- model families;
- evaluator families;
- data families;
- dependence structure.

Do not report only:

```text
97/100 worlds agree.
```

---

# 85. Evidence aggregation packet

```text
claim_id
world_ids
lineage_families
model_families
evaluator_families
dependence_model
covariance_or_cluster_model
effective_sample_size
aggregation_method
counterexamples
transport_scope
```

---

# 86. Effective sample size is claim specific

The same branches can have different correlations for different statistics.

Therefore:

$$
n_{\mathrm{eff}}
$$

must be attached to the specific evidence statistic, not the branch family globally.

---

# 87. Common evaluator audit

Run a subset of branch outputs through independent evaluators.

If conclusions change materially, shared-evaluator dependence is decision relevant.

---

# 88. Common model audit

Repeat selected interventions using an independent world-model/backend.

This tests common-mode model dependence.

---

# 89. Transport validation branch

Some compute budget should be spent not on more internal branches but on comparing simulation to external observed subtraces.

This directly targets:

$$
\delta_{\mathrm{trans}}.
$$

---

# 90. Marginal validation can miss conditional mismatch

A simulator can match overall output distribution while misrepresenting one subset of stochastic inputs/conditions.

Subtrace-conditional validation is a current example of conditioning the validation problem to expose such mismatch.

---

# 91. Reality transport hierarchy

Suggested levels:

```text
T0: NO_TRANSPORT
T1: SEMANTIC_MATCH_ONLY
T2: MARGINAL_VALIDATION
T3: CONDITIONAL_VALIDATION
T4: INTERVENTIONAL_VALIDATION
T5: STRUCTURAL_TRANSPORT_CLAIM
```

The exact labels are VWDC engineering proposals.

---

# 92. Transport claim packet

```text
world_claim
reality_target
transport_level
validation_dataset
validation_protocol
world_estimation_error
transport_discrepancy
assumption_set
expiry/version
```

---

# 93. Transport versioning

A transport contract is version-specific.

Changing:

- world model;
- reality domain;
- evaluator;
- measurement process;

can invalidate the contract.

---

# 94. Reality evidence expiry

External validity can drift over time.

Transport contracts should support:

```text
VALID
STALE
INVALID
REVALIDATION_REQUIRED
```

---

# 95. Simulation precision versus external validity

More simulation branches can shrink Monte Carlo error.

They do not automatically shrink model discrepancy.

Keep:

$$
\boxed{
\varepsilon_{\mathrm{MC}}
}
$$

separate from:

$$
\boxed{
\delta_{\mathrm{model/transport}}.
}
$$

---

# 96. Total claim debt

One simple bound:

$$
\boxed{
D_{\mathrm{claim}}
=
D_{\mathrm{branch}}
+
D_{\mathrm{model}}
+
D_{\mathrm{evaluator}}
+
D_{\mathrm{transport}}.
}
$$

This is an accounting structure, not a universal additive law.

---

# 97. WDC evidence asymmetry

Agreement is gradual evidence.

A valid counterexample can instantly refute a universal modeled claim.

This asymmetry should influence branch search.

---

# 98. Counterexample-directed branching

The Governor can prioritize branches likely to falsify fragile universal claims.

This is a scientific-search strategy.

---

# 99. Confirmation-directed branching

For estimation claims, prioritize independent replication and external validation.

Different scientific claims require different branch portfolios.

---

# 100. Visual branch lineage

Every rendered artifact records:

$$
\boxed{
VisualArtifact
\to
WorldID
\to
CheckpointID
\to
BranchID.
}
$$

---

# 101. World branch lineage

Every world records:

$$
\boxed{
ParentWorldID,
ForkCheckpoint,
DivergenceContract.
}
$$

---

# 102. Bridge lineage

VWDC ties them:

$$
\boxed{
\mathsf{BridgeEdge}
:
W_i
\overset{\mathrm{RENDER}}{\to}
I_{i,t}.
}
$$

---

# 103. Derived image lineage

If:

$$
I_{i,t}
\to
\widetilde I_{i,t}
$$

via EDIT, the derived image remains attached to the same source observation lineage unless a new world is lifted/validated.

---

# 104. Re-lifted world

If edited image:

$$
\widetilde I
$$

is LIFTed and validated into:

$$
W',
$$

 $W'$ receives new world identity and bridge lineage pointing to the edited visual artifact.

It is not the same world as the source render.

---

# 105. Branch evidence with relift

Evidence from $W'$ depends on:

- source world observation;
- edit provider;
- lift model;
- validation;
- new dynamics.

This dependency chain must be explicit.

---

# 106. Invalid edit provider

If the edit provider is later invalidated, the relifted world's evidence may become stale even if the world simulator itself is valid.

This shows why visual and world provenance must interlock.

---

# 107. Sibling blindness

WDC Runtime already includes sibling-blindness concepts.

A child world should not automatically observe sibling branch state unless communication is explicitly permitted.

This preserves branch semantics.

---

# 108. Evidence sharing versus world communication

Evidence aggregator may compare siblings externally.

That does not mean siblings communicate internally.

Keep:

$$
\boxed{
\text{meta-observer access}
\neq
\text{in-world communication}.
}
$$

---

# 109. Cross-branch contamination

If one branch receives information from a sibling during execution, independence assumptions change.

Record communication edges.

---

# 110. Branch communication graph

Define:

$$
\boxed{
G_{\mathrm{comm}}
}
$$

separately from lineage graph.

Sibling communication can create post-fork dependence not explained by common ancestry.

---

# 111. VWDC03-N5 — Lineage alone does not determine evidence dependence

Two branches with distant ancestry can still use the same evaluator/model/data and be strongly dependent.

Two close siblings can be intentionally paired with shared noise for a valid contrast.

Therefore:

$$
\boxed{
\text{lineage distance alone}
\not\Rightarrow
\text{evidence independence}.
}
$$

---

# 112. Dependency dimensions

At minimum track:

- ancestry;
- model;
- data;
- randomness;
- evaluator;
- provider;
- infrastructure;
- communication;
- transport.

---

# 113. Evidence independence is a hypothesis

It should be stated and tested where possible.

Do not make it a default property of branch identity.

---

# 114. Empirical covariance

Repeated branch families can estimate covariance of statistics.

This can support ESS estimates.

Small samples imply large uncertainty in covariance.

---

# 115. Robust aggregation

When dependence is poorly known, use:

- cluster-robust analysis;
- sensitivity analysis;
- worst-case correlation bounds;
- model-family stratification.

VWDC-03 does not prescribe one universal method.

---

# 116. Fréchet-style dependence bounds

Marginal branch success rates do not determine joint success without dependence assumptions.

This inherits GVSS-09.

---

# 117. Branch reliability

For fallback/control use joint failure law.

For evidence estimation use covariance/dependence law.

Reliability and evidence independence are related but not identical.

---

# 118. Evidence-quality vector

Define:

$$
\boxed{
\mathbf Q_E
=
(
\text{validity},
\text{independence},
\text{diversity},
\text{calibration},
\text{transport strength},
\text{provenance completeness}
).
}
$$

Do not compress by default.

---

# 119. Branch evidence frontier

A branch family can be evaluated on:

- expected information gain;
- independent replication value;
- counterexample probability;
- cost;
- transport strength;
- replayability.

Nondominated branch portfolios form an evidence frontier.

---

# 120. VWDC03-T10 — Evidence-portfolio Pareto necessity

## Theorem VWDC03-T10

Every optimum of a scalar evidence-portfolio objective strictly increasing in declared costs/debts and strictly decreasing in declared evidence benefits lies on the nondominated evidence frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 121. Invalidation priority

Shared dependencies with many descendants have high blast radius.

The runtime can prioritize auditing them.

---

# 122. Dependency centrality

Define:

$$
\boxed{
B(s)
=
|
\operatorname{Desc}(s)
|.
}
$$

Large $B(s)$ indicates large syntactic invalidation blast radius.

This is not semantic importance by itself.

---

# 123. High-centrality evaluator

A shared evaluator used by every branch can have:

$$
B(E^\star)\gg1.
$$

Independent evaluator checks can be disproportionately valuable.

---

# 124. High-centrality parent model

A world model shared by all branches can dominate common-mode error.

More branch seeds do not address it.

---

# 125. Audit allocation

Audit budget should consider:

$$
\boxed{
\text{blast radius}
\times
\text{uncertainty}
\times
\text{claim importance}.
}
$$

Engineering heuristic only.

---

# 126. Replay queue

After invalidation:

1. compute descendant closure;
2. identify last clean checkpoint for each affected path;
3. classify replayability;
4. schedule corrected replay;
5. compare old/new results;
6. update aggregates and transport claims.

---

# 127. Replay divergence

If corrected replay changes results, record:

$$
\boxed{
\Delta_{\mathrm{replay}}
=
d(
Result_{\mathrm{old}},
Result_{\mathrm{new}}
).
}
$$

Large divergence updates confidence in dependent claims.

---

# 128. Counterfactual replay

Replay can also intentionally change one factor while freezing others.

This becomes a paired counterfactual experiment.

Distinguish from recovery replay.

---

# 129. Recovery replay

Purpose:

> reconstruct what the pipeline would have produced without the invalid component.

---

# 130. Counterfactual replay

Purpose:

> estimate the effect of a declared intervention.

Same mechanism, different evidence semantics.

---

# 131. Evidence merge contract

Evidence aggregation must declare:

- target claim;
- allowed evidence scope;
- covariance/dependence model;
- counterexample treatment;
- evaluator treatment;
- transport level.

---

# 132. State merge contract

State merge is separate and stricter.

It reconciles world state/history, not just evidence.

---

# 133. No silent merge

VWDC inherits WDC:

$$
\boxed{
\text{no silent state merge}.
}
$$

---

# 134. Branch forest

Multiple independent root worlds can exist.

Root independence still requires model/data/evaluator analysis.

Different roots do not automatically mean independent evidence.

---

# 135. External roots

Worlds initialized from independent external measurements can offer stronger evidence separation than branches from one shared parent.

But shared model/evaluator dependence may remain.

---

# 136. Data-family independence

If all models are calibrated on the same biased dataset, backend diversity alone may not create independent evidence.

Track data provenance.

---

# 137. Model-family independence

Architectural diversity can reduce shared model error, but cannot be assumed to.

Empirical failure covariance matters.

---

# 138. Evaluator-family independence

Use independent evaluators/human audits when evidence claims depend critically on scoring.

---

# 139. Random-seed diversity

Different seeds primarily explore aleatoric/local stochastic variation.

They do not identify structural model misspecification.

---

# 140. Intervention diversity

Different interventions explore causal/control space.

They are not replications of the same experiment.

---

# 141. Evidence taxonomy

Recommended:

```text
ALEATORIC_REPLICATION
MODEL_REPLICATION
EVALUATOR_REPLICATION
COUNTERFACTUAL_PAIR
SENSITIVITY_BRANCH
FALSIFICATION_BRANCH
TRANSPORT_VALIDATION
```

---

# 142. Statistical independence versus epistemic independence

Statistical independence concerns random variables under a model.

Epistemic independence concerns whether evidence sources share reasons for being wrong.

They are related but distinct.

VWDC tracks both.

---

# 143. Epistemic common cause

A shared flawed assumption can make worlds epistemically dependent even when simulated random variables are statistically independent.

---

# 144. Reality validation cannot be bootstrapped internally

No amount of internal re-rendering or branch consensus can create external measurement evidence.

External validity requires external anchoring or a justified transport contract.

---

# 145. Digital twin caution

Digital twins can provide counterfactual simulations.

The validity of those counterfactuals depends on what parts of the twin have been validated against observable data and which joint/structural assumptions remain untestable.

---

# 146. Validation hierarchy

VWDC recommends separating:

1. code/transition verification;
2. internal consistency;
3. marginal empirical validation;
4. conditional/subtrace validation;
5. interventional validation;
6. structural transport.

---

# 147. Branch evidence and validation

Branching mostly improves:

- internal exploration;
- Monte Carlo precision;
- sensitivity analysis;
- counterexample search.

It does not automatically advance every validation level.

---

# 148. Validation data reuse

If the same external dataset is used repeatedly to tune and validate the world model, independence assumptions weaken.

Record validation data lineage.

---

# 149. Feedback trap

A model updated on data generated by its own prior recommendations can become self-confirming.

This is another cross-world evidence dependence channel.

---

# 150. World-model drift

If model version changes, old branch evidence remains historical evidence under the old version.

Do not silently relabel it as evidence from the new world model.

---

# 151. Transport expiry

A transport contract validated for:

$$
M_v
$$

may not hold for:

$$
M_{v+1}.
$$

Require revalidation or transfer proof.

---

# 152. Evidence packet fingerprint

Hash:

- world/checkpoint IDs;
- model/provider/evaluator versions;
- actions;
- external inputs;
- dependencies;
- transport contract.

This supports audit.

---

# 153. Branch packet fingerprint

Hash:

- parent checkpoint;
- divergence contract;
- seed/noise contract;
- model version;
- provider/evaluator profile.

---

# 154. Evidence replay fingerprint

Record old and corrected pipeline fingerprints.

---

# 155. Branch comparison

When comparing siblings, first state whether the comparison estimates:

- within-model causal contrast;
- robustness across models;
- stochastic variability;
- evaluator sensitivity.

Different claims require different branch designs.

---

# 156. Within-model causal contrast

Noise-coupled siblings can be excellent for estimating:

$$
\Delta_W
$$

within a fixed world model.

Do not present:

$$
\Delta_W
$$

as real causal effect without transport validation.

---

# 157. Cross-model robustness

Repeat the same intervention contrast under multiple independently calibrated world models.

This tests model-family robustness.

---

# 158. Cross-evaluator robustness

Evaluate the same branch outputs with independent evaluators.

This tests observer robustness.

---

# 159. External subtrace validation

Compare selected world trajectory segments to real observations.

This targets transport/model discrepancy directly.

---

# 160. World evidence graph

The full evidence state can be:

$$
\boxed{
\mathsf{WEG}
=
(
G_{\mathrm{lineage}},
G_{\mathrm{dependency}},
G_{\mathrm{communication}},
\mathcal T_{\mathrm{transport}}
).
}
$$

No single graph captures every relation.

---

# 161. Lineage graph

Answers:

> Where did this branch/world/artifact come from?

---

# 162. Dependency graph

Answers:

> Which claims become stale if this component is invalid?

---

# 163. Communication graph

Answers:

> Which branches exchanged information after divergence?

---

# 164. Transport graph

Answers:

> Which world claims are connected to which external reality targets and validation contracts?

---

# 165. VWDC03-N6 — One provenance graph is insufficient for all branch semantics

Lineage, dependency, communication, and evidence transport encode different relations.

Collapsing them into one untyped edge relation can lose the distinction between:

- parentage;
- data dependence;
- communication;
- validation.

Therefore:

$$
\boxed{
\text{one untyped provenance DAG}
\not\Rightarrow
\text{complete branch evidence semantics}.
}
$$

---

# 166. Runtime state

Suggested:

```text
world_lineage_graph
evidence_dependency_graph
branch_communication_graph
transport_contract_graph
branch_independence_profiles
evidence_aggregates
invalidation_queue
replay_queue
```

---

# 167. Branch creation API

```text
fork(
  parent_checkpoint,
  divergence_contract,
  noise_coupling,
  model_version,
  evaluator_profile,
  evidence_purpose
)
```

---

# 168. Evidence aggregation API

```text
aggregate(
  claim_id,
  evidence_ids,
  dependence_model,
  aggregation_method,
  transport_scope
)
```

---

# 169. Invalidation API

```text
invalidate(
  dependency_id,
  reason,
  timestamp,
  replacement_version
)
```

---

# 170. Replay API

```text
replay_from_clean_checkpoint(
  checkpoint_id,
  corrected_pipeline,
  random_state_contract
)
```

---

# 171. Transport API

```text
transport_claim(
  world_claim,
  reality_target,
  transport_contract,
  validation_artifacts
)
```

---

# 172. Branch merge API

```text
merge_worlds(
  parent_world_ids,
  reconciliation_contract,
  merge_policy
)
```

No default merge.

---

# 173. Benchmark A — common ancestry ESS

Generate:

$$
Y_i=B+\varepsilon_i.
$$

Vary:

$$
\operatorname{Var}(B).
$$

Compare:

- raw branch count;
- empirical covariance;
- effective sample size.

---

# 174. Benchmark B — coupled counterfactuals

Generate paired outcomes with controlled correlation.

Verify:

$$
\operatorname{Var}(Y_1-Y_0)
=
2\sigma^2(1-\rho).
$$

---

# 175. Benchmark C — evaluator invalidation

Create 100 branches with one shared biased evaluator.

Invalidate evaluator.

Verify all dependent scores/aggregates enter stale/replay state while raw world trajectories remain valid.

---

# 176. Benchmark D — clean replay

Record exact checkpoint, action stream, seeds, model versions.

Replace evaluator.

Replay.

Verify deterministic corrected output.

---

# 177. Benchmark E — simulation consensus failure

Construct one shared biased world model.

Generate many branches.

Consensus remains wrong relative to external ground truth.

---

# 178. Benchmark F — transport error

Specify:

$$
\varepsilon_W,
\delta_{\mathrm{trans}},
L_T.
$$

Verify total bound:

$$
L_T\varepsilon_W+\delta_{\mathrm{trans}}.
$$

---

# 179. Benchmark G — visual agreement/no merge

Two worlds render same frame but differ in hidden state.

Verify merge denied.

---

# 180. Benchmark H — dependency blast radius

Create evidence DAG.

Invalidate high-centrality evaluator.

Check exact descendant closure.

---

# 181. Benchmark I — paired versus replication objective

Same two branches are scored under:

- independent-confirmation objective;
- paired-counterfactual objective.

Demonstrate opposite preferences for correlation.

---

# 182. Branch-quality dashboard

Report:

```text
branch_count
lineage_family_count
model_family_count
evaluator_family_count
estimated_covariance
effective_sample_size
counterexample_count
paired_contrast_precision
transport_level
replayability
```

---

# 183. Raw branch count should not headline alone

Prefer:

> 100 branches, estimated $n_{\mathrm{eff}}=7.4$ for claim $q$.

over:

> 100 independent simulations.

unless independence is justified.

---

# 184. Claim-specific ESS

For claim:

$$
q_1,
$$

branches can have:

$$
n_{\mathrm{eff}}^{(1)}.
$$

For another statistic:

$$
q_2,
$$

the same branches can have different:

$$
n_{\mathrm{eff}}^{(2)}.
$$

---

# 185. Evidence dependence uncertainty

Covariance estimates themselves are uncertain.

A mature runtime should attach confidence/sensitivity bands to ESS.

---

# 186. Conservative default

When dependence is unknown but common ancestry is strong, do not assume independence.

Use:

- sensitivity range;
- lineage clusters;
- external validation.

---

# 187. High-stakes claims

The stronger the reality claim, the stronger transport validation should be.

Internal branch consensus is weakest precisely where shared model assumptions dominate.

---

# 188. Model-class falsification

A branch counterexample can refute a claim inside one model class.

If every model class shares the same structural restriction, that restriction itself can hide real counterexamples.

Model-class expansion remains necessary.

---

# 189. World-class coverage

Evidence from branches applies first to the subset of world space actually explored.

Do not silently universalize over uncomputed branches.

---

# 190. Branch selection bias

WDC Governor chooses which worlds deserve computation.

Evidence collected from selected branches can therefore be selection biased.

This connects to GVSS-10 routing-selection bias.

---

# 191. Evidence weighting by branch policy

If branch sampling policy is known, off-policy or importance-weighted methods may be needed for population claims.

VWDC-03 does not develop the full estimator.

---

# 192. Falsification search is intentionally biased

Counterexample search deliberately oversamples likely failures.

That is appropriate for falsification.

It is not representative-frequency estimation.

---

# 193. Evidence purpose prevents estimator misuse

The same branch set should not be reused for a different statistical claim without checking sampling design.

---

# 194. Replay and selection

After invalidation/replay, branch selection policy may also change.

Record replay-policy version.

---

# 195. Historical immutability

Never delete invalid evidence history.

Mark status and create corrected descendants.

This preserves audit trail.

---

# 196. Evidence supersession

A corrected replay can supersede an invalid score.

The old score remains immutable historical artifact.

---

# 197. Branch provenance persistence

Even terminated worlds retain:

- lineage;
- checkpoints;
- evidence references;
- model versions.

World termination is not evidence deletion.

---

# 198. Counterfactual world deletion

A branch may be pruned from active computation while its evidence remains archived.

---

# 199. WDC Governor interaction

Governor decisions should consider:

- expected evidence gain;
- dependence reduction;
- counterexample potential;
- transport validation value;
- replay cost.

Not merely branch quality.

---

# 200. Independent backend value

Running one branch with a genuinely different model/evaluator can provide more evidence independence than running many extra seeds of the same stack.

This is claim dependent but operationally important.

---

# 201. External validation value

One well-designed external validation measurement can reduce transport debt more than hundreds of internal branches.

---

# 202. Counterexample value

One valid counterexample can have discontinuously high value for a universal claim.

---

# 203. Branch cost frontier

Define:

$$
\boxed{
\mathbf C_{\mathrm{branch}}
=
(
C_{\mathrm{compute}},
C_{\mathrm{human}},
D_{\mathrm{dependence}},
D_{\mathrm{model}},
D_{\mathrm{evaluator}},
D_{\mathrm{transport}},
D_{\mathrm{replay}}
).
}
$$

---

# 204. Evidence benefit vector

$$
\boxed{
\mathbf B_{\mathrm{branch}}
=
(
I_{\mathrm{replication}},
I_{\mathrm{contrast}},
I_{\mathrm{falsification}},
I_{\mathrm{validation}},
I_{\mathrm{transport}}
).
}
$$

---

# 205. Evidence portfolio optimization

A future WDC Governor can choose branches on the joint cost/benefit frontier.

VWDC-03 defines accounting but not the optimal policy.

---

# 206. Current literature boundary

VWDC-03 does not claim as inventions:

- law of total covariance;
- effective sample size under correlation;
- common-random-number coupling;
- paired counterfactual simulation;
- provenance DAGs;
- replay/checkpointing;
- digital twin validation;
- uncertainty quantification;
- causal transport;
- Pareto frontiers.

---

# 207. Candidate VWDC-specific synthesis

Subject to broader literature audit, the bridge-specific synthesis is:

1. treating sibling-world independence as a claim-specific evidence property rather than a consequence of world identity;
2. combining branch lineage, model/evaluator dependence, and evidence-purpose labels;
3. explicitly separating independent replication from noise-coupled paired counterfactuals;
4. using provenance dependency closure for evaluator/provider invalidation and clean-checkpoint replay;
5. separating evidence merge from world-state merge;
6. composing world-estimation error with world-to-reality transport discrepancy;
7. keeping visual lineage, world lineage, dependency, communication, and transport as distinct graph relations;
8. connecting WDC branch governance to GVSS routing-selection-bias and VWDC evidence provenance.

No strong novelty claim is made in v0.1.

---

# 208. What VWDC-03 proves

Under explicit hypotheses, VWDC-03 proves:

1. conditionally independent sibling branches can remain marginally dependent through shared ancestry;
2. equicorrelated branch effective sample size is $n/[1+(n-1)\rho]$ ;
3. positive sibling coupling can reduce paired counterfactual contrast variance;
4. deterministic dependency invalidation propagates through descendant closure;
5. exact replay from a clean checkpoint is correct under recorded deterministic replay conditions;
6. correlation-blind standard errors can underestimate branch-mean variance by factor $n$ in the fully correlated case;
7. one valid world-class counterexample refutes a universal claim over that modeled class;
8. simulation consensus does not imply reality validation;
9. world estimation and transport error compose under a Lipschitz transport map;
10. visual agreement does not authorize world merge;
11. multi-parent merge preserves lineage acyclicity under strict creation order;
12. world/provider diversity does not imply evaluator independence;
13. visual diversity does not certify evidence independence;
14. lineage distance alone does not determine evidence dependence;
15. a single untyped provenance graph is insufficient to encode lineage, dependency, communication, and transport semantics;
16. every strictly monotone scalar evidence-portfolio optimum lies on the nondominated evidence frontier.

---

# 209. What VWDC-03 does not prove

It does not prove:

- branch outputs are exchangeable in real systems;
- pairwise correlation fully characterizes dependence;
- effective sample size is one universal scalar for all claims;
- shared-noise coupling identifies real causal effects;
- replay is exact when APIs/models are unavailable or nondeterministic;
- provenance completeness is automatically achieved;
- branch merge is generally possible;
- digital twin validation resolves unobservable counterfactual dependence;
- world consensus establishes reality truth;
- external transport discrepancy can always be bounded tightly;
- one branch-design objective is universally optimal.

---

# 210. Proposed VWDC-04

The next bridge paper should move from evidence accounting to **branch-design and computation allocation**:

$$
\boxed{
\textbf{
VWDC-04 — Active Branch Design, Dependence-Aware World Experimentation, and Evidence Value
}
}
$$

Chinese:

**主動分支設計、依賴性感知世界實驗與證據價值**

Main questions:

1. Which fork should be created next?
2. When is an independent backend better than another seed?
3. When should shared-noise coupling be used?
4. How should branch correlation enter value-of-information?
5. How should counterexample probability compete with replication value?
6. When should compute be spent on external validation rather than simulation?
7. Can branch allocation regret be bounded?
8. How should the Governor trade exploration of world space against evidence independence?

---

# 211. References

1. Yu Ma, Hongli Shi, Xinran Xu, **Twin Rollouts: Noise-Coupled Counterfactual Branching in Interactive Video World Models**, arXiv:2608.08982, 2026.
2. Olav Laudy, **The Digital Twin Counterfactual Framework: A Validation Architecture for Simulated Potential Outcomes**, arXiv:2604.01325, 2026.
3. Mohammadmahdi Ghasemloo, David J. Eckman, Yaxian Li, **Subtrace-Conditional Validation of Simulation Models and Digital Twins**, arXiv:2607.17088, 2026.
4. Sheeba Samuel, Frank Löffler, Birgitta König-Ries, **Machine Learning Pipelines: Provenance, Reproducibility and FAIR Data Principles**, arXiv:2006.12117, 2020.
5. Michael A. C. Johnson et al., **Pipeline Provenance for Analysis, Evaluation, Trust or Reproducibility**, arXiv:2404.14378, 2024.
6. Julien Deantoni et al., **Quantifying and combining uncertainty for improving the behavior of Digital Twin Systems**, arXiv:2402.10535, 2024.
7. VWDC-01–02, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, and frozen RRT-20, internal series artifacts, 2026.

---

# 212. Conclusion

A branch is a new world identity.

It is not automatically a new independent evidence source.

Shared parent checkpoints, models, evaluators, data, assumptions, infrastructure, and noise coupling create dependence.

For equicorrelated replication:

$$
\boxed{
n_{\mathrm{eff}}
=
\frac{
n
}{
1+(n-1)\rho
}.
}
$$

But dependence has dual use.

For paired counterfactuals:

$$
\boxed{
\operatorname{Var}(Y_1-Y_0)
=
2\sigma^2(1-\rho),
}
$$

so deliberate positive coupling can improve intervention contrasts.

Therefore branch independence must be designed for the evidence purpose.

Invalid evidence propagates through dependency descendants.

A clean checkpoint plus complete replay contract can reconstruct corrected descendants without rewriting history.

Evidence aggregation does not imply state merge.

World consensus does not imply real-world truth.

And reality transport retains an irreducible validation term:

$$
\boxed{
d_R(
T(\widehat q_W),
q_R
)
\le
L_T\varepsilon_W
+
\delta_{\mathrm{trans}}.
}
$$

More worlds can reduce world-estimation error.

They cannot automatically erase model-to-reality discrepancy.

The canonical VWDC-03 principle is:

$$
\boxed{
\textbf{
Branch count is computation.
Evidence independence is structure.
Counterfactual precision may benefit from coupling,
replication credibility may require independence,
and reality claims require transport validation beyond both.
}
}
$$

This establishes dependence-aware evidence governance for branching visual worlds.

---

# Canonical-source policy

This file is the canonical UTF-8 source artifact.

- Canonical inline mathematics uses ` $...$ `.
- Canonical display mathematics uses `$$...$$`.
- No Unicode mathematical-symbol conversion is used as source normalization.
- No `unicode_escape` round trip is used.
- Backslashes and delimiters are preserved literally.
- Validation is required before release.
- This paper does not merge or rename GVSS, WDC, VWDC, or RRT.
