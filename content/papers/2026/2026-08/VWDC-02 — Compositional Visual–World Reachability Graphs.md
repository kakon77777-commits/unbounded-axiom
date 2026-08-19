# VWDC-02 — Compositional Visual–World Reachability Graphs
## 組合式視覺—世界可達圖：跨生成器轉換、世界提升、Fork、缺陷傳遞與混合路徑治理

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 02  
**Depends on:** VWDC-01, GVSS-01–10, WDC-01–08, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal bridge paper. Typed-path composability, strict compositional reachability beyond one-step provider union, finite nonnegative-cost shortest valid paths, Lipschitz defect transport, vector defect recursion, runnable-world lift gating, exact-state cycle elimination, useful type-level iteration, lineage acyclicity under restore, deterministic-evidence postprocessing, mixed-path dominance, and bridge Pareto statements are proved under the explicit hypotheses below. Multi-step agentic image editing, tool-using visual generation, action-conditioned world models, graph shortest paths, data processing, and multiobjective path optimization are established neighboring work and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** compositional reachability, visual-world graph, cross-provider pipeline, runnable world, typed graph, world lift, fork, intervention, image editing agent, defect propagation, provenance, evidence transport, GVSS, WDC

---

# Abstract

VWDC-01 established the first bridge boundary:

$$
\boxed{
\text{Visual State}
\neq
\text{Runnable World State}.
}
$$

A runnable world exposes a visual observation:

$$
\boxed{
O_{\mathrm{vis}}:
\mathcal X_W
\to
\Omega_\Sigma
}
$$

and a visual state can be partially lifted toward a world candidate:

$$
\boxed{
L:
D_L
\subseteq
\Omega_\Sigma
\to
\mathcal W_{\mathrm{candidate}}.
}
$$

VWDC-02 asks the next question:

> **What happens when visual generation, editing, world lifting, world validation, forking, intervention, rendering, checkpointing, restoration, and evaluation are composed into one executable path?**

The central object is a typed directed multigraph:

$$
\boxed{
G_{\mathrm{VW}}
=
(
V,E,\tau,\sigma
),
}
$$

where:

- $V$ is a set of versioned artifacts/states;
- $\tau:V\to\mathcal T$ assigns node type;
- $E$ is a set of typed partial transformations;
- $\sigma(e)$ is the operation signature of edge $e$.

The canonical state-bearing node types are:

$$
\boxed{
\mathcal T
=
\{
\mathsf T,
\mathsf V,
\mathsf U,
\mathsf W,
\mathsf C,
\mathsf E
\},
}
$$

with:

- $\mathsf T$: task/constraint state;
- $\mathsf V$: visual artifact;
- $\mathsf U$: unvalidated world candidate;
- $\mathsf W$: runnable world;
- $\mathsf C$: world checkpoint;
- $\mathsf E$: evidence/evaluation packet.

Canonical operation signatures include:

$$
\boxed{
\begin{aligned}
\mathrm{GENERATE}&:\mathsf T\rightharpoonup\mathsf V,\\
\mathrm{EDIT}&:\mathsf V\rightharpoonup\mathsf V,\\
\mathrm{REPAIR}&:\mathsf V\rightharpoonup\mathsf V,\\
\mathrm{LIFT}&:\mathsf V\rightharpoonup\mathsf U,\\
\mathrm{VALIDATE}_\kappa&:\mathsf U\rightharpoonup\mathsf W,\\
\mathrm{RENDER}&:\mathsf W\rightharpoonup\mathsf V,\\
\mathrm{FORK}&:\mathsf W\rightharpoonup\mathsf W,\\
\mathrm{INTERVENE}&:\mathsf W\rightharpoonup\mathsf W,\\
\mathrm{CHECKPOINT}&:\mathsf W\rightharpoonup\mathsf C,\\
\mathrm{RESTORE}&:\mathsf C\rightharpoonup\mathsf W,\\
\mathrm{EVALUATE}&:\mathsf V\cup\mathsf W\rightharpoonup\mathsf E.
\end{aligned}
}
$$

Every edge is a versioned partial map:

$$
\boxed{
F_e:
D_e
\subseteq
X_{\tau(s(e))}
\to
X_{\tau(t(e))}
}
$$

carrying at least:

$$
\boxed{
\mathsf{Edge}(e)
=
(
\mathrm{Type},
\mathrm{Provider},
\mathrm{Version},
c_e,
\eta_e,
\mathsf{EvidencePolicy}_e,
\mathsf{Prov}_e
).
}
$$

A path:

$$
p=e_m\cdots e_1
$$

is **valid** when:

1. edge endpoint types compose;
2. every intermediate state lies in the domain of the next partial map;
3. every contract gate required by an edge passes.

Its composite transformation is:

$$
\boxed{
F_p
=
F_{e_m}
\circ
\cdots
\circ
F_{e_1}.
}
$$

This gives a precise meaning to mixed visual/world reachability.

---

## Composition can exceed one-stage provider union

GVSS-09 showed that one-provider terminal routing is bounded by the raw union:

$$
\bigcup_\nu
\mathcal R_\nu^{(1)}.
$$

VWDC-02 proves that multi-stage provider composition can strictly exceed this one-stage union.

Consider a task root:

$$
t.
$$

Provider A can only generate:

$$
t
\overset{A}{\longrightarrow}
x,
$$

and provider B cannot generate from $t$ but can edit:

$$
x
\overset{B}{\longrightarrow}
y.
$$

Then:

$$
\boxed{
y
\notin
\mathcal R_A^{(1)}
\cup
\mathcal R_B^{(1)},
}
$$

while:

$$
\boxed{
y
\in
\operatorname{Reach}^{(2)}_{G_{\mathrm{VW}}}(t).
}
$$

Therefore:

$$
\boxed{
\text{compositional reachability}
\supsetneq
\text{one-stage provider union}
}
$$

can occur.

This is one formal reason multi-stage agentic image systems can exceed the capability envelope of any single one-shot provider.

Current 2026 systems such as I2E, PhotoAgent, CanvasAgent, RS-Gen, GenClaw, and Qwen-Image-Agent all provide current engineering precedent for decomposition, tool use, multi-step editing/generation, or closed-loop visual workflows.

VWDC does not claim multi-step visual agents as new.

---

## Lift is not a silent type cast

The operation:

$$
\mathrm{LIFT}:
\mathsf V
\to
\mathsf U
$$

creates a **world candidate**, not a runnable world.

Promotion requires:

$$
\boxed{
\mathrm{VALIDATE}_\kappa:
\mathsf U
\rightharpoonup
\mathsf W.
}
$$

The promoted partial lift is:

$$
\boxed{
\mathrm{LIFT}_\kappa
=
\mathrm{VALIDATE}_\kappa
\circ
\mathrm{LIFT}.
}
$$

Its domain is exactly the visual candidates for which the chosen lift mechanism produces a world satisfying the declared contract $\kappa$.

Thus:

$$
\boxed{
\text{scene reconstruction}
\neq
\text{runnable-world promotion}.
}
$$

A path containing a raw LIFT edge but no successful world-contract validation has not yet reached a $\mathsf W$ node.

---

## Defect transport

Each implemented edge approximates an intended transformation.

Let:

$$
f_j
$$

be implemented maps and:

$$
g_j
$$

their declared ideal/reference maps.

Suppose for every admissible input:

$$
\boxed{
d_j(
f_j(x),
g_j(x)
)
\le
\eta_j.
}
$$

Suppose ideal downstream map:

$$
g_k
$$

is:

$$
L_k
$$

-Lipschitz.

Then for path length $m$:

$$
\boxed{
d(
f_m\circ\cdots\circ f_1(x),
g_m\circ\cdots\circ g_1(x)
)
\le
\sum_{j=1}^m
\eta_j
\prod_{k=j+1}^m
L_k.
}
$$

Local visual/world translation defects therefore survive according to downstream conditioning.

A small early defect can become large when later transformations are expansive.

This is the mixed visual/world specialization of the RRT defect-transport law.

For a multi-axis defect vector:

$$
e_j
\in
\mathbb R_+^d,
$$

if:

$$
\boxed{
e_{j+1}
\preceq
A_j e_j
+
\varepsilon_j
}
$$

with nonnegative matrices $A_j$, then:

$$
\boxed{
e_m
\preceq
A_{m-1:0}e_0
+
\sum_{j=0}^{m-1}
A_{m-1:j+1}\varepsilon_j.
}
$$

The vector can include:

- semantic defect;
- style drift;
- identity drift;
- world-state uncertainty;
- dynamics defect;
- evidence/provenance debt.

---

## Costed paths

Let every edge have nonnegative scalar execution cost:

$$
c_e\ge0.
$$

Path cost is additive:

$$
\boxed{
C(p)
=
\sum_{e\in p}
c_e.
}
$$

In a finite explicit state graph, if a target is reachable, there exists a minimum-cost valid path and at least one minimum-cost path can be chosen simple: no exact state node is repeated.

Any exact node cycle with nonnegative cost can be deleted without increasing scalar cost.

This does **not** mean iterative workflows are useless.

It means:

$$
\boxed{
\text{exact state-return cycle}
\neq
\text{type-level iterative loop}.
}
$$

A sequence:

$$
\mathsf V
\to
\mathsf V
\to
\mathsf V
$$

can create new artifacts at every step and expand practical reachability.

The lineage nodes differ even though the node type repeats.

---

## Null cycles versus productive iteration

Define an exact null cycle $q$ at node $v$ by:

1. it starts and ends at the same exact versioned state node;
2. it contributes no new independent evidence;
3. all costs are nonnegative;
4. its declared defect vector is non-improving.

Then any valid path containing $q$ is weakly dominated by the path with $q$ removed.

But a type-level loop can be productive.

Example:

$$
I_0
\overset{\mathrm{EDIT}_1}{\longrightarrow}
I_1
\overset{\mathrm{EDIT}_2}{\longrightarrow}
I_2,
$$

where:

$$
I_2
$$

satisfies constraints unavailable at $I_0$ or $I_1$.

The type signature repeats:

$$
\mathsf V\to\mathsf V,
$$

but no exact artifact node is revisited.

Thus:

$$
\boxed{
\text{cycles in the operator grammar can be useful}
}
$$

while exact state-return cycles can be removable debt.

---

## Restore does not require lineage cycles

A WDC world can RESTORE a checkpoint:

$$
C_j
\overset{\mathrm{RESTORE}}{\longrightarrow}
W_{\mathrm{new}}.
$$

The new world can have hidden state equal to the checkpointed state.

But it receives a new world identity and a new lineage node.

If every derivation edge points from an older artifact/checkpoint to a newly created node, lineage remains a DAG even when execution semantics revisit an old state.

Therefore:

$$
\boxed{
\text{execution-state recurrence}
\not\Rightarrow
\text{provenance-lineage cycle}.
}
$$

This preserves auditability.

---

## Edit is not intervention

A visual edit:

$$
I
\to
I'
$$

can alter only an observation artifact while the world remains unchanged.

A world intervention:

$$
W
\to
W'
$$

changes the world state/dynamics/branch.

The same resulting pixels can therefore have different causal semantics.

For example:

### Observation edit

Add rain to a rendered screenshot.

World remains:

$$
W.
$$

### World intervention

Change world weather state to rain, then render.

World becomes:

$$
W'.
$$

Even if:

$$
O(W')=I',
$$

the two paths differ in hidden dynamics and future observations.

Thus:

$$
\boxed{
\text{image edit}
\not\Rightarrow
\text{world intervention}.
}
$$

Typed edges prevent this causal ambiguity.

---

## Evidence does not multiply under deterministic postprocessing

Suppose evidence-bearing variable is:

$$
X.
$$

A deterministic visual transformation/evaluation produces:

$$
Y=f(X).
$$

Then:

$$
\boxed{
\sigma(Y)
\subseteq
\sigma(X).
}
$$

Therefore deterministic postprocessing does not create independent information beyond the source evidence.

Multiple restyles, renders, crops, deterministic evaluator summaries, or exact format translations of the same world observation should not be counted as independent world evidence.

An actual intervention/rollout can generate new **world-internal** evidence because a new trajectory is sampled or executed.

Even then, WDC's reality-transport boundary remains:

$$
\boxed{
\text{world-internal evidence}
\neq
\text{external reality evidence}.
}
$$

---

## Mixed-path evidence labels

Every edge receives one evidence policy, for example:

$$
\boxed{
\{
\mathsf{DERIVED},
\mathsf{WORLD\_OBSERVATION},
\mathsf{INTERVENTIONAL},
\mathsf{EXTERNAL\_MEASUREMENT}
\}.
}
$$

### DERIVED

No new independent evidence; transformed from existing artifact.

### WORLD_OBSERVATION

New observation from a runnable world trajectory.

### INTERVENTIONAL

Observation generated after an explicit world intervention/fork.

### EXTERNAL_MEASUREMENT

Evidence imported from outside the simulated world under an explicit transport contract.

These labels prevent visual transformations from silently becoming epistemic multiplication.

---

## Mixed lineage

Visual lineage and world lineage are different relations.

Define:

$$
\boxed{
\mathsf{Lineage}_{\mathrm{VW}}
=
(
\mathsf{VisualLineage},
\mathsf{WorldLineage},
\mathsf{BridgeEdges}
).
}
$$

A rendered image from child world:

$$
W_2
$$

belongs to $W_2$ 's observation lineage even if it visually matches a frame from parent $W_1$.

Visual equality does not authorize world-identity merge.

Similarly, RESTORE creates a new child identity referencing an old checkpoint.

It does not overwrite history.

---

## Path dominance

Let two valid paths:

$$
p,q
$$

connect the same declared start condition to the same target acceptance class.

Associate path vector:

$$
\boxed{
\mathbf C(p)
=
(
C_{\mathrm{exec}},
D_{\mathrm{semantic}},
D_{\mathrm{identity}},
D_{\mathrm{dynamics}},
D_{\mathrm{evidence}},
D_{\mathrm{provenance}}
).
}
$$

Path $p$ dominates $q$ when it is no worse in every declared cost/debt coordinate and strictly better in at least one, while satisfying at least the same target/world contracts.

A scalar optimum with strictly monotone preferences must lie on the mixed-path Pareto frontier.

Thus the "shortest" path is objective dependent.

The minimum API-price path need not be the minimum-defect or maximum-evidence path.

---

## Current engineering precedent

The visual side of this graph is increasingly real.

I2E decomposes an image into manipulable object layers and lets a vision-language-action agent execute atomic actions in a structured editing environment.

PhotoAgent uses a closed-loop suite of editing/evaluation tools and explores long-horizon editing action sequences.

CanvasAgent uses specialized visual tools for generation, editing, localization, segmentation, extraction, compositing, geometric transformation, OCR, and super-resolution.

RS-Gen implements a multi-stage reasoning/search-augmented image-generation workflow.

GenClaw separates cognitive structuring, executable canvas construction, visual generation, and review.

These systems support the practical relevance of typed multi-stage visual transformations.

On the world side, action-conditioned models such as COMBAT, LIVE, DreamX-World, GameNGen, Genie, and DAWN demonstrate interactive or action-conditioned world evolution.

VWDC-02 does not claim these systems or their architectures as new.

Its purpose is to supply one contract-aware graph connecting visual transformations to runnable-world operations.

---

# 1. Canonical graph types

Let:

$$
\boxed{
\mathcal T
=
\{
\mathsf T,
\mathsf V,
\mathsf U,
\mathsf W,
\mathsf C,
\mathsf E
\}.
}
$$

---

# 2. Task state $\mathsf T$

Contains:

- intent;
- constraints;
- budget;
- project state;
- target contract.

---

# 3. Visual artifact $\mathsf V$

A versioned image/layered canvas/video observation with:

- provider;
- parent;
- visual specification;
- visual provenance.

---

# 4. World candidate $\mathsf U$

A candidate lifted scene/world state that has not yet satisfied the runnable-world contract.

It may contain:

- scene graph;
- geometry;
- hidden-state proposal;
- dynamics proposal;
- uncertain latent variables.

---

# 5. Runnable world $\mathsf W$

A WDC world instance satisfying the selected:

$$
\kappa.
$$

---

# 6. Checkpoint $\mathsf C$

A replayable WDC checkpoint with:

- world ID;
- state;
- model/version;
- local time;
- history digest;
- random-state semantics;
- provenance.

---

# 7. Evidence packet $\mathsf E$

An observation/evaluation/evidence artifact carrying:

- source world/artifact;
- observer;
- edge history;
- evidence scope;
- dependence/provenance.

---

# 8. Typed operation

## Definition VWDC02-D1

An edge:

$$
e
$$

has signature:

$$
\boxed{
\sigma(e):
\tau_s
\rightharpoonup
\tau_t
}
$$

and partial implementation:

$$
\boxed{
F_e:
D_e
\subseteq
X_{\tau_s}
\to
X_{\tau_t}.
}
$$

---

# 9. Edge metadata

## Definition VWDC02-D2

$$
\boxed{
M_e
=
(
\mathrm{OpType},
\mathrm{Provider},
\mathrm{Version},
c_e,
\varepsilon_e,
\mathsf{EvidencePolicy},
\mathsf{Prov}
).
}
$$

---

# 10. Canonical signatures

$$
\boxed{
\begin{array}{c|c}
\text{Operation} & \text{Signature}\\
\hline
\mathrm{GENERATE} & \mathsf T\to\mathsf V\\
\mathrm{EDIT} & \mathsf V\to\mathsf V\\
\mathrm{REPAIR} & \mathsf V\to\mathsf V\\
\mathrm{LIFT} & \mathsf V\to\mathsf U\\
\mathrm{VALIDATE}_\kappa & \mathsf U\rightharpoonup\mathsf W\\
\mathrm{RENDER} & \mathsf W\to\mathsf V\\
\mathrm{FORK} & \mathsf W\to\mathsf W\\
\mathrm{INTERVENE} & \mathsf W\to\mathsf W\\
\mathrm{CHECKPOINT} & \mathsf W\to\mathsf C\\
\mathrm{RESTORE} & \mathsf C\to\mathsf W\\
\mathrm{EVALUATE} & \mathsf V\cup\mathsf W\to\mathsf E
\end{array}
}
$$

---

# 11. Valid path

## Definition VWDC02-D3

A sequence:

$$
p=e_m\cdots e_1
$$

is valid from state $x_0$ iff:

1. type signatures match;
2. $x_{j-1}\in D_{e_j}$ ;
3. $x_j=F_{e_j}(x_{j-1})$ ;
4. required contracts/gates pass.

---

# 12. Composite map

$$
\boxed{
F_p
=
F_{e_m}
\circ\cdots\circ F_{e_1}.
}
$$

This is defined only on inputs for which every intermediate partial map is defined.

---

# 13. VWDC02-T1 — Typed path composability

## Theorem VWDC02-T1

For a valid path $p=e_m\cdots e_1$ from $x_0$, the composite map:

$$
F_p(x_0)
$$

is well-defined and its output type is the target type of $e_m$.

### Proof

Induction over path edges using the validity conditions.

 $\square$

This is elementary typed composition.

---

# 14. Typed invalidity

The sequence:

$$
\mathsf V
\overset{\mathrm{EDIT}}{\longrightarrow}
\mathsf V
\overset{\mathrm{INTERVENE}}{\longrightarrow}
?
$$

is invalid because INTERVENE requires a $\mathsf W$ input.

A LIFT/VALIDATE bridge is required first.

---

# 15. VWDC02-N1 — Image edit is not world intervention

A visual edit can change:

$$
I\to I'
$$

while leaving world:

$$
W
$$

unchanged.

A world intervention changes:

$$
W\to W'.
$$

Therefore no type-preserving identity equates EDIT and INTERVENE in general.

 $\square$

---

# 16. One-stage provider reachability

For task state $t$, define:

$$
\boxed{
\mathcal R_\nu^{(1)}(t)
=
\{
v:
t
\overset{\nu}{\longrightarrow}
v
\text{ in one GENERATE operation}
\}.
}
$$

---

# 17. m-stage reachability

## Definition VWDC02-D4

$$
\boxed{
\operatorname{Reach}^{(\le m)}(t)
}
$$

is the set of states reachable from $t$ by valid paths of at most $m$ operation edges.

---

# 18. VWDC02-T2 — Composition can strictly exceed one-stage provider union

## Theorem VWDC02-T2

There exist typed provider graphs such that:

$$
\boxed{
\operatorname{Reach}^{(\le2)}(t)
\cap\mathsf V
\supsetneq
\bigcup_\nu
\mathcal R_\nu^{(1)}(t).
}
$$

### Proof by construction

Let:

$$
t
\overset{A:\mathrm{GENERATE}}{\longrightarrow}
x.
$$

Let B have no GENERATE edge from $t$, but:

$$
x
\overset{B:\mathrm{EDIT}}{\longrightarrow}
y.
$$

Then the one-stage union contains $x$ but not $y$.

The two-stage path reaches $y$.

 $\square$

---

# 19. World composition extension

Likewise a path:

$$
t
\to
I
\to
U
\to
W
\to
W'
\to
I'
$$

can produce visual observation $I'$ that no one-stage T2I provider generates directly from $t$.

Its semantics depend on the lifted/intervened world.

---

# 20. Lift candidate

## Definition VWDC02-D5

$$
\boxed{
\mathrm{LIFT}:
\mathsf V
\rightharpoonup
\mathsf U.
}
$$

A candidate is not yet runnable.

---

# 21. World validation

## Definition VWDC02-D6

$$
\boxed{
\mathrm{VALIDATE}_\kappa:
\mathsf U
\rightharpoonup
\mathsf W.
}
$$

The partial domain is the candidate set satisfying the WDC runnable contract.

---

# 22. Promoted lift

$$
\boxed{
\mathrm{LIFT}_\kappa
=
\mathrm{VALIDATE}_\kappa
\circ
\mathrm{LIFT}.
}
$$

---

# 23. VWDC02-T3 — Runnable-world lift gate

## Theorem VWDC02-T3

A visual-to-world path reaches a node of type $\mathsf W$ through the promoted lift iff:

1. the raw LIFT is defined on the visual artifact;
2. its output lies in the domain of $\mathrm{VALIDATE}_\kappa$.

### Proof

Definition of partial-map composition.

 $\square$

Therefore raw scene reconstruction is not a silent world promotion.

---

# 24. Validation failure

If candidate:

$$
U
$$

fails:

- state;
- dynamics;
- action;
- history;
- resource;
- provenance;

contract obligations, the graph remains at:

$$
\mathsf U
$$

or emits failure evidence.

It does not create a $\mathsf W$ node.

---

# 25. Scalar path cost

## Definition VWDC02-D7

$$
\boxed{
C(p)
=
\sum_{e\in p}
c_e,
\qquad
c_e\ge0.
}
$$

---

# 26. Target set

Let:

$$
\mathcal G_{\mathrm{target}}
\subseteq V
$$

be accepted terminal nodes.

---

# 27. VWDC02-T4 — Finite nonnegative-cost shortest valid path

## Theorem VWDC02-T4

In a finite explicit state graph with nonnegative edge costs, if a target node is reachable from source $s$, there exists a minimum-cost valid path from $s$ to the target set.

At least one minimum-cost path can be chosen with no repeated exact state node after zero-cost null repetitions are removed.

### Proof

Take any minimum-cost walk among finitely many simple paths plus possible cycles.

If a node repeats, the intervening cycle has nonnegative cost.

Delete the cycle; the remaining walk connects the same exact state node to the same continuation and has no greater cost.

Repeat until simple.

A finite graph has finitely many simple paths.

 $\square$

---

# 28. Shortest path boundary

This theorem applies to:

- explicit nodes;
- scalar additive nonnegative costs.

For continuous state spaces or path-dependent costs, additional machinery is required.

---

# 29. Dijkstra boundary

When all valid transitions are explicitly enumerated and cost is additive/nonnegative, ordinary shortest-path algorithms apply after type-invalid edges are excluded.

This is classical graph theory.

---

# 30. Local transformation defect

Let:

$$
f_j
$$

be implemented edge transformation.

Let:

$$
g_j
$$

be declared reference/ideal transformation.

Assume:

$$
\boxed{
d_j(
f_j(z),
g_j(z)
)
\le
\eta_j.
}
$$

---

# 31. Downstream Lipschitz constant

Assume:

$$
g_j
$$

is:

$$
L_j
$$

-Lipschitz under declared metrics.

---

# 32. VWDC02-T5 — Mixed-path Lipschitz defect transport

## Theorem VWDC02-T5

For a valid path of $m$ transformations:

$$
\boxed{
d_m(
f_m\circ\cdots\circ f_1(x),
g_m\circ\cdots\circ g_1(x)
)
\le
\sum_{j=1}^m
\eta_j
\prod_{k=j+1}^m
L_k.
}
$$

### Proof

Use the telescoping decomposition:

$$
\begin{aligned}
&d(
f_m\cdots f_1(x),
g_m\cdots g_1(x)
)
\\
&\le
\eta_m
+
L_m
d(
f_{m-1}\cdots f_1(x),
g_{m-1}\cdots g_1(x)
).
\end{aligned}
$$

Iterate recursively.

 $\square$

---

# 33. Interpretation

A defect from:

- prompt compilation;
- visual edit;
- visual-to-world lift;
- world intervention;
- render;

can be amplified by later path stages.

A local low-error edge is not automatically harmless globally.

---

# 34. Defect vector

## Definition VWDC02-D8

$$
\boxed{
e_j
=
(
e_{\mathrm{semantic}},
e_{\mathrm{style}},
e_{\mathrm{identity}},
e_{\mathrm{world}},
e_{\mathrm{dynamics}},
e_{\mathrm{evidence}}
).
}
$$

---

# 35. Vector propagation

Suppose:

$$
\boxed{
e_{j+1}
\preceq
A_je_j
+
\varepsilon_j
}
$$

with nonnegative transfer matrix $A_j$.

---

# 36. VWDC02-T6 — Vector mixed-path defect recursion

## Theorem VWDC02-T6

$$
\boxed{
e_m
\preceq
A_{m-1:0}e_0
+
\sum_{j=0}^{m-1}
A_{m-1:j+1}\varepsilon_j.
}
$$

### Proof

Induction, identical to the RRT/GVSS vector defect recursion.

 $\square$

---

# 37. Identity drift example

A world lift can reconstruct geometry correctly but misassign character identity.

A later high-fidelity renderer can preserve that wrong identity perfectly.

Visual fidelity can therefore amplify confidence in a semantic/world defect.

---

# 38. Evidence defect

A path can also corrupt evidence scope.

Example:

- simulation observation;
- visual enhancement;
- evaluator score;
- exported chart.

If the chart is later labeled "real-world measurement", the path has evidence-provenance defect even if pixels are correct.

---

# 39. Exact state cycle

## Definition VWDC02-D9

An exact state cycle is a valid subpath:

$$
q:
v
\to
\cdots
\to
v
$$

returning to the same versioned state node.

---

# 40. Null cycle

A null cycle satisfies:

1. exact node return;
2. no new independent evidence;
3. nonnegative total cost;
4. no target-relevant defect improvement.

---

# 41. VWDC02-T7 — Null-cycle elimination

## Theorem VWDC02-T7

If valid path:

$$
p=p_2\circ q\circ p_1
$$

contains a null exact state cycle $q$, then:

$$
\boxed{
p'
=
p_2\circ p_1
}
$$

is valid and weakly dominates $p$ under additive nonnegative cost and non-improving defect assumptions.

### Proof

 $q$ returns to the identical versioned node, so $p_2$ is still executable.

Removing $q$ does not remove independent evidence by assumption.

Cost cannot increase.

Defect cannot worsen by the null-cycle assumption.

 $\square$

---

# 42. Operator-type loop

An operator loop repeats a type signature:

$$
\mathsf V
\to
\mathsf V
\to
\mathsf V
$$

or:

$$
\mathsf W
\to
\mathsf W.
$$

It need not repeat an exact state.

---

# 43. VWDC02-N2 — Type-level cycles can be productive

## Counterexample

States:

$$
I_0,I_1,I_2
$$

all have type $\mathsf V$.

Two EDIT actions:

$$
I_0\to I_1,
$$

$$
I_1\to I_2.
$$

Only $I_2$ satisfies the target contract.

The operator grammar is:

$$
\mathsf V\to\mathsf V
$$

repeated, yet reachability strictly increases.

Thus:

$$
\boxed{
\text{type-cycle}
\not\Rightarrow
\text{useless cycle}.
}
$$

 $\square$

---

# 44. Iterative editing precedent

Current multi-step editing agents explicitly use repeated perception/planning/editing loops.

This is compatible with the distinction between:

- productive new artifact nodes;
- exact state-return cycles.

---

# 45. Checkpoint edge

$$
\boxed{
\mathrm{CHECKPOINT}:
\mathsf W
\to
\mathsf C.
}
$$

Checkpoint stores declared replay state.

---

# 46. Restore edge

$$
\boxed{
\mathrm{RESTORE}:
\mathsf C
\to
\mathsf W.
}
$$

RESTORE creates a **new world identity** even when hidden state equals the checkpointed state.

---

# 47. Lineage creation index

Assign every newly created artifact/world/checkpoint:

$$
\boxed{
t_{\mathrm{create}}(v).
}
$$

Every provenance derivation edge points from earlier to later creation index.

---

# 48. VWDC02-T8 — Lineage acyclicity under restore

## Theorem VWDC02-T8

If every derivation operation, including RESTORE, creates a new node with strictly larger creation index than all parent/source nodes, then the provenance lineage graph is acyclic.

### Proof

Along every lineage edge creation index strictly increases.

A directed cycle would require returning to the starting node/index after strict increase.

Impossible.

 $\square$

---

# 49. VWDC02-N3 — Execution recurrence does not imply lineage recurrence

A restored world can have:

$$
X_{\mathrm{new}}
=
X_{\mathrm{checkpoint}}
$$

while:

$$
ID_{\mathrm{new}}
\neq
ID_{\mathrm{old}}.
$$

Thus execution state can recur while lineage remains acyclic.

 $\square$

---

# 50. Fork edge

$$
\boxed{
\mathrm{FORK}:
W
\to
W'.
}
$$

A fork records parent world/checkpoint.

---

# 51. Fork siblings

Sibling worlds can later render visually identical images.

Their world identities remain distinct unless a full identity/merge contract proves equivalence.

---

# 52. No visual merge

$$
\boxed{
O(W_1)=O(W_2)
}
$$

does not authorize:

$$
ID(W_1)=ID(W_2).
$$

This inherits VWDC-01.

---

# 53. Visual edit semantics

EDIT changes artifact:

$$
I\to I'.
$$

It can be:

- restyle;
- inpaint;
- composite;
- typography;
- crop;
- color transform.

---

# 54. World intervention semantics

INTERVENE changes:

- state;
- rules;
- actor state;
- environment parameter;
- branch.

---

# 55. Rain example

### Edit path

$$
W
\overset{\mathrm{RENDER}}{\to}
I
\overset{\mathrm{EDIT}}{\to}
I_{\mathrm{rain}}.
$$

World weather remains unchanged.

### Intervention path

$$
W
\overset{do(\mathrm{rain})}{\to}
W_{\mathrm{rain}}
\overset{\mathrm{RENDER}}{\to}
I'_{\mathrm{rain}}.
$$

The pixels can look similar.

Future world evolution differs.

---

# 56. Causal typing principle

$$
\boxed{
\textbf{
Pixel equivalence does not imply intervention equivalence.
}
}
$$

---

# 57. Evidence source variable

Let:

$$
X
$$

be an evidence-bearing random variable.

---

# 58. Derived visual variable

Let:

$$
Y=f(X)
$$

deterministically.

---

# 59. VWDC02-T9 — Deterministic postprocessing does not create new information

## Theorem VWDC02-T9

$$
\boxed{
\sigma(Y)
\subseteq
\sigma(X).
}
$$

Hence every decision/statistic computable from $Y$ is also computable from $X$.

### Proof

For measurable $f$, preimages of events in $Y$ belong to the sigma-algebra generated by $X$.

 $\square$

This is the deterministic data-processing boundary.

---

# 60. Evidence counting consequence

The following do not automatically create independent world evidence:

- deterministic restyle;
- deterministic crop;
- deterministic upscaling;
- deterministic evaluator summary;
- exact format conversion.

They produce derived artifacts.

---

# 61. Stochastic postprocessing

A randomized visual transform can create a new random output.

But randomness generated by the transform is not automatically new evidence about the source world.

The correct question is whether new world/external measurement information entered.

---

# 62. World observation

A new world rollout can produce new world-internal evidence:

$$
W_t
\to
W_{t+1}
\to
O(W_{t+1}).
$$

It remains evidence **about the simulated world** unless reality transport is justified.

---

# 63. Intervention evidence

A fork/intervention can test a counterfactual inside the runnable world.

Its result is interventional world evidence.

It does not automatically validate the corresponding real-world counterfactual.

---

# 64. Evidence policy

## Definition VWDC02-D10

Each edge carries:

$$
\boxed{
\mathsf{EP}(e)
\in
\{
\mathsf{DERIVED},
\mathsf{WORLD\_OBSERVATION},
\mathsf{INTERVENTIONAL},
\mathsf{EXTERNAL\_MEASUREMENT}
\}.
}
$$

---

# 65. DERIVED

No new independent source measurement.

---

# 66. WORLD_OBSERVATION

New observation produced by a world trajectory.

---

# 67. INTERVENTIONAL

Observation after explicit world intervention/fork.

---

# 68. EXTERNAL_MEASUREMENT

Evidence imported from outside the simulated world under explicit transport provenance.

---

# 69. Evidence path ledger

For path $p$ store:

$$
\boxed{
\mathsf{EvidenceLedger}(p)
=
(
\text{source IDs},
\text{derived edges},
\text{world observations},
\text{interventions},
\text{external measurements}
).
}
$$

---

# 70. VWDC02-N4 — Final visual quality is not world evidence

## Counterexample

Take two paths producing identical high-quality image:

$$
I^*.
$$

Path A:

- real/world observation;
- faithful render.

Path B:

- hallucinated visual generation from prompt only.

The final image-quality evaluator assigns the same score.

But evidential provenance differs.

Therefore:

$$
\boxed{
\text{final image quality}
\not\Rightarrow
\text{world evidence status}.
}
$$

 $\square$

---

# 71. Path contract

A path has terminal contract:

$$
\boxed{
\kappa_p
}
$$

specifying required:

- output type;
- world validity;
- visual constraints;
- evidence scope;
- budget.

---

# 72. Path cost/debt vector

## Definition VWDC02-D11

$$
\boxed{
\mathbf C(p)
=
(
C_{\mathrm{exec}},
D_{\mathrm{semantic}},
D_{\mathrm{style}},
D_{\mathrm{identity}},
D_{\mathrm{world}},
D_{\mathrm{dynamics}},
D_{\mathrm{evidence}},
D_{\mathrm{prov}}
).
}
$$

---

# 73. Path dominance

## Definition VWDC02-D12

For paths satisfying the same terminal contract, $p$ dominates $q$ if every cost/debt coordinate is no greater and at least one is strictly smaller.

Benefit coordinates can be sign-normalized.

---

# 74. VWDC02-T10 — Mixed-path Pareto necessity

## Theorem VWDC02-T10

Every optimum of a scalar path objective strictly increasing in every declared cost/debt coordinate lies on the nondominated mixed-path Pareto frontier.

### Proof

If an optimum were dominated, the dominating path would strictly improve the scalar objective.

Contradiction.

 $\square$

---

# 75. Cheapest path is not universally best

A cheaper path may:

- lose identity;
- violate world dynamics;
- rely on untrusted lift;
- erase evidence provenance.

Path comparison is contract dependent.

---

# 76. Shortest valid path

When the objective is only scalar additive execution cost and all gates are encoded in the graph, VWDC02-T4 reduces the problem to ordinary shortest valid path.

---

# 77. Multiobjective path

When multiple debts matter, maintain a set of nondominated labels per node.

This is classical multiobjective shortest-path methodology.

---

# 78. Provider role

Provider identity belongs on operation edges, not only output artifacts.

The same provider can support:

- GENERATE;
- EDIT;
- RENDER;
- world model;
- evaluation.

Each role has separate contract.

---

# 79. Provider version

Every edge stores exact model/backend version.

A path with an updated provider is a different path artifact.

---

# 80. Cross-provider translation

When provider B consumes provider A's output, a compatibility transform may be required.

Add explicit edge:

$$
\boxed{
\mathrm{TRANSLATE}_{A\to B}
}
$$

when formats/semantics differ.

---

# 81. Translation defect

Translation can create:

- resolution loss;
- color change;
- metadata loss;
- coordinate mismatch;
- semantic loss.

Do not hide this inside switching cost.

---

# 82. Lift-provider translation

A visual image generator may output pixels that a world-lift model cannot interpret reliably.

The bridge can require a structural decomposition edge before LIFT.

---

# 83. I2E relevance

I2E explicitly decomposes a flat image into manipulable object layers and executes atomic actions in a structured environment.

This is a direct visual-side precedent for adding an intermediate structured representation rather than editing only raw pixels.

---

# 84. CanvasAgent relevance

CanvasAgent uses specialized tools including compositing, segmentation, geometric transformation, OCR, editing, and super-resolution.

This is direct engineering evidence for typed visual tool graphs.

---

# 85. PhotoAgent relevance

PhotoAgent uses long-horizon action planning over editing/evaluation tools.

This is evidence that iterative path search is already an active image-editing paradigm.

---

# 86. RS-Gen relevance

RS-Gen explicitly describes image generation/editing as a multi-stage reasoning/search-augmented closed-loop workflow.

---

# 87. GenClaw relevance

GenClaw decomposes agentic visual creation into cognitive structuring, executable canvas construction, generation, and review.

This supports multi-stage state typing.

---

# 88. World-action model relevance

DAWN couples world prediction and action generation recursively.

It is evidence that world/action transformations can be mutually conditioned rather than strictly serial.

VWDC's graph can represent this with compound/recurrent world edges.

---

# 89. COMBAT relevance

COMBAT is an action-controlled real-time world model with reactive agent behavior.

It demonstrates a world edge semantics richer than image editing.

---

# 90. LIVE relevance

LIVE targets long-horizon action-conditioned video world modeling and explicitly addresses accumulated rollout error.

This is directly relevant to VWDC path defect accumulation.

---

# 91. DreamX-World relevance

DreamX-World supports long-horizon interactive generation with navigation, revisits, and promptable events.

It is a current example of visual-world trajectories that go beyond isolated frame generation.

---

# 92. Current visual-generation taxonomy

Recent 2026 work explicitly frames progress from atomic generation to agentic generation and world-modeling generation.

VWDC's type system makes one operational distinction inside that spectrum:

- visual artifact transformation;
- runnable-world transformation.

---

# 93. Typed graph validation

Before executing path:

1. check node types;
2. check edge domains;
3. check provider versions;
4. check budgets;
5. check contract gates;
6. initialize provenance ledger.

---

# 94. Runtime path packet

Suggested:

```text
path_id
source_node
target_contract
edges[]
total_cost
defect_vector
evidence_ledger
world_lineage
visual_lineage
provider_versions
validation_status
```

---

# 95. Edge packet

```text
edge_id
operation_type
source_type
target_type
provider
provider_version
domain_contract
cost
local_defect
evidence_policy
parent_artifact_ids
output_artifact_id
```

---

# 96. LIFT packet

```text
source_visual_id
lift_model
world_candidate_id
hidden_state_init
dynamics_model
lift_uncertainty
render_check
world_contract
validation_result
```

---

# 97. FORK packet

```text
parent_world_id
parent_checkpoint
child_world_id
intervention_delta
random_seed_policy
local_time
```

---

# 98. RESTORE packet

```text
checkpoint_id
source_world_lineage
new_world_id
restored_state_hash
new_execution_branch
```

---

# 99. Evidence packet

```text
evidence_id
source_node
source_world_id
evidence_scope
evidence_policy
observer
intervention_id
derived_from[]
external_transport_contract
```

---

# 100. Graph validation invariant

No edge may silently change:

- node type;
- world identity;
- evidence scope;
- provider version.

All such changes are explicit metadata or explicit operations.

---

# 101. World/visual mixed reachability

Define:

$$
\boxed{
\operatorname{Reach}_{G_{\mathrm{VW}}}(s)
}
$$

as all typed nodes reachable by valid finite paths.

---

# 102. Visual slice

$$
\boxed{
\operatorname{Reach}_{\mathsf V}(s)
=
\operatorname{Reach}_{G_{\mathrm{VW}}}(s)
\cap
V_{\mathsf V}.
}
$$

---

# 103. World slice

$$
\boxed{
\operatorname{Reach}_{\mathsf W}(s)
=
\operatorname{Reach}_{G_{\mathrm{VW}}}(s)
\cap
V_{\mathsf W}.
}
$$

---

# 104. Evidence slice

$$
\boxed{
\operatorname{Reach}_{\mathsf E}(s)
=
\operatorname{Reach}_{G_{\mathrm{VW}}}(s)
\cap
V_{\mathsf E}.
}
$$

One graph supports multiple reachability questions without confusing types.

---

# 105. Visual target versus world target

A request can terminate at:

$$
\mathsf V
$$

if only an image is needed.

It must terminate at:

$$
\mathsf W
$$

if a runnable world is required.

A beautiful image is not a successful world-target path.

---

# 106. World target with visual constraints

Target can require both:

$$
W\in\mathcal W_\kappa
$$

and:

$$
O_{\mathrm{vis}}(W)\in\mathcal A_{\mathrm{vis}}.
$$

This is a cross-type terminal contract.

---

# 107. Path verification

A candidate path can be rejected because:

- output type wrong;
- lift invalid;
- dynamics defect too large;
- visual target failed;
- budget exceeded;
- evidence provenance missing.

---

# 108. Productive iterative loop benchmark

Construct a visual repair chain where every edit reduces one defect coordinate until target threshold.

Compare with exact-state cycle.

This tests the type-cycle/state-cycle distinction.

---

# 109. Compositional reachability benchmark

Create providers:

- A generates layout;
- B edits typography;
- C lifts scene;
- D validates world;
- E renders.

Target requires all five stages.

No single provider reaches it.

---

# 110. Defect propagation benchmark

Inject early identity defect.

Pass through later high-gain transformation with:

$$
L>1.
$$

Verify downstream amplification.

---

# 111. Lineage restore benchmark

Checkpoint one world.

Intervene.

Restore twice.

Verify:

- hidden states can repeat;
- all restored world IDs are distinct;
- lineage remains acyclic.

---

# 112. Evidence benchmark

Start from one world observation.

Create ten deterministic visual transformations.

A correct evidence ledger still records one source world observation, not ten independent observations.

---

# 113. Path dominance benchmark

Create two valid paths:

- cheap/high-defect;
- expensive/low-defect.

Ensure neither dominates unless task scalarization is declared.

---

# 114. Path search benchmark

For finite graph with scalar nonnegative cost, compare Dijkstra result against brute-force simple paths.

---

# 115. Contract-aware graph search

A runtime should search only paths whose intermediate states satisfy hard contracts.

Do not search first and "validate everything at the end" if invalid operations can corrupt lineage/state.

---

# 116. World fork search

Forking can create parallel candidate worlds.

The graph becomes a branching computation tree/DAG.

WDC Governor chooses which branches continue.

---

# 117. GVSS router role

Within a path, GVSS-10 can select provider for each visual subtask.

WDC Governor selects higher-level world operations and branch budget.

---

# 118. Nested control

Conceptually:

$$
\boxed{
\text{WDC Governor}
\supset
\text{VWDC Path Planner}
\supset
\text{GVSS Provider Router}.
}
$$

This is a decision hierarchy, not mandatory software inheritance.

---

# 119. Edge failure

An edge can fail execution.

The graph planner can:

- retry;
- choose alternate edge/provider;
- roll back;
- fork;
- stop.

This connects to GVSS failure diagnosis and WDC governance.

---

# 120. Dynamic graph

Provider availability, versions, and costs can change.

Therefore:

$$
G_{\mathrm{VW}}=G_{\mathrm{VW}}(t)
$$

in production.

VWDC-02 studies a fixed graph snapshot.

---

# 121. Graph provenance

A saved result must identify the graph/version under which the path was valid.

---

# 122. Path replay

Replay requires:

- edge versions;
- seeds;
- source artifacts;
- checkpoints;
- external dependency snapshots.

Without them, path lineage may be auditable but not reproducible.

---

# 123. Reproducibility versus provenance

Provenance means knowing what happened.

Reproducibility means being able to recreate it.

These are separate.

---

# 124. Evidence independence

Two branches from one checkpoint are not automatically independent experiments.

They share:

- parent state;
- world model;
- renderer;
- evaluator.

Evidence dependence must be preserved.

---

# 125. Fork diversity

Forks can vary:

- action;
- seed;
- model;
- rule;
- provider.

The source of diversity determines which uncertainties are actually explored.

---

# 126. Branch merge

Merging sibling worlds requires explicit merge semantics.

Visual similarity is insufficient.

VWDC-02 does not define general world merge.

---

# 127. Visual composite merge

Two image layers can be composited with explicit visual semantics.

This does not imply their source worlds can be merged.

---

# 128. Cross-world render composite no-go

A single image can visually combine objects rendered from two incompatible worlds.

The composite visual artifact need not be liftable to a single contract-valid world.

---

# 129. VWDC02-N5 — Visual composability does not imply world composability

## Counterexample

World A has rule:

$$
g=+1.
$$

World B has incompatible rule:

$$
g=-1.
$$

Render one object from each and composite them into one plausible image.

The visual composite exists.

A single world contract requiring one global gravity parameter cannot realize both source dynamics simultaneously.

Therefore:

$$
\boxed{
\text{visual composition}
\not\Rightarrow
\text{world-contract composition}.
}
$$

 $\square$

---

# 130. Composition contract

When combining world components, require compatibility over:

- units;
- coordinates;
- time;
- physics;
- identity;
- rules;
- action semantics.

This is stronger than pixel-layer compatibility.

---

# 131. Translation edge for coordinates

A provider/world may use:

- image pixels;
- normalized coordinates;
- 3D world coordinates.

Transformations between them must be explicit.

---

# 132. Time translation

World-local time:

$$
\tau_W
$$

and visual/video frame index:

$$
t_V
$$

must be related by a declared mapping.

Do not infer synchronization from frame order alone.

---

# 133. RRT relation

RRT supplies the cross-layer rule:

$$
\boxed{
\text{adaptation/transformation can move defect rather than erase it}.
}
$$

VWDC path defect makes this concrete across mixed visual/world transformations.

---

# 134. GVSS relation

GVSS supplies:

- visual state space;
- constraints;
- providers;
- routing;
- evaluators;
- visual failure diagnosis.

These populate the $\mathsf V$ side of $G_{\mathrm{VW}}$.

---

# 135. WDC relation

WDC supplies:

- runnable worlds;
- checkpoints;
- forks;
- interventions;
- local time;
- world evidence;
- governor.

These populate the $\mathsf W/\mathsf C$ side.

---

# 136. Bridge claim

VWDC does not replace GVSS or WDC.

It formalizes typed operations that cross between them.

---

# 137. Current literature boundary — visual workflows

Agentic image systems increasingly plan long, tool-using visual workflows.

VWDC does not claim this trend as new.

Its narrower contribution is to distinguish which workflow steps merely transform observations and which cross into runnable-world state.

---

# 138. Current literature boundary — world models

Interactive world models increasingly support:

- action conditioning;
- longer horizons;
- reactive agents;
- navigation;
- promptable events.

VWDC does not claim world-model interactivity as new.

Its narrower contribution is the typed bridge to visual artifact workflows and WDC contracts.

---

# 139. Current literature boundary — graph theory

Shortest paths, Pareto paths, graph reachability, and cycle removal under nonnegative cost are classical.

They are implementation tools here.

---

# 140. Current literature boundary — information theory/statistics

Data processing/postprocessing cannot create independent information about a source.

VWDC applies this to evidence accounting.

---

# 141. Candidate VWDC-specific synthesis

Subject to broader audit, candidate bridge-specific synthesis is:

1. one typed graph containing both visual artifact transformations and runnable-world transformations;
2. an explicit $\mathsf U$ candidate-world type separating LIFT from runnable promotion;
3. strict compositional reachability beyond one-stage provider union;
4. common path defect transport across visual, lift, world, intervention, and render edges;
5. exact-state cycle versus productive type-level iteration distinction;
6. RESTORE semantics that permits state recurrence while preserving lineage DAGs;
7. evidence-policy labels preventing deterministic visual derivations from being counted as independent world evidence;
8. mixed visual/world path Pareto governance.

No strong novelty claim is made in v0.1.

---

# 142. What VWDC-02 proves

Under explicit hypotheses, VWDC-02 proves:

1. valid typed operation paths compose into a well-defined partial transformation;
2. multi-stage provider composition can reach visual states outside the one-stage provider union;
3. runnable-world promotion requires both raw LIFT success and world-contract validation;
4. finite explicit nonnegative-cost graphs admit a minimum-cost valid path to reachable targets;
5. scalar local edge defects propagate with downstream Lipschitz amplification;
6. vector defects obey the nonnegative matrix recursion;
7. exact null state cycles can be deleted without worsening the declared cost/debt objective;
8. repeated same-type editing operations can still expand reachability when they create new states;
9. RESTORE can revisit checkpoint state while the provenance graph remains acyclic through new identities;
10. deterministic postprocessing creates no additional sigma-algebra information beyond source evidence;
11. final visual quality does not determine world evidence status;
12. every strictly monotone scalar mixed-path optimum lies on the nondominated path frontier;
13. visual composability need not imply world-contract composability.

---

# 143. What VWDC-02 does not prove

It does not prove:

- every useful workflow is representable by a finite explicit graph;
- one scalar defect metric is universal;
- Dijkstra solves multiobjective or path-dependent planning;
- every iterative loop is beneficial;
- every cycle is removable;
- LIFT can always construct a runnable world;
- deterministic postprocessing never improves usability;
- world-internal evidence is reality evidence;
- sibling branch evidence is independent;
- visual composites always admit world composition;
- provider-edge defects are easy to estimate;
- graph search is computationally cheap at world scale.

---

# 144. Proposed VWDC-03

The next paper should focus on lineage/evidence rather than expand the graph vocabulary again:

$$
\boxed{
\textbf{
VWDC-03 — Visual World Branching, Lineage, and Evidence Transport
}
}
$$

Chinese:

**視覺世界分支、譜系與證據轉移：Checkpoint、Sibling Worlds、依賴性與跨域證據邊界**

Main questions:

1. How should world and visual lineage be jointly represented?
2. Which sibling-world outputs are dependent?
3. When can branch evidence be aggregated?
4. How should checkpoints define common ancestry?
5. What does a valid branch merge require?
6. How should invalid evaluator/provider evidence be replayed?
7. When may world evidence cross to real-world claims?
8. How should branch diversity be measured without assuming independence?

---

# 145. References

1. Jinghan Yu et al., **I2E: From Image Pixels to Actionable Interactive Environments for Text-Guided Image Editing**, arXiv:2601.03741, 2026.
2. Feifei Bian et al., **RS-Gen: A Multi-Stage Agentic Framework for Reasoning and Search-Augmented Image Generation**, arXiv:2606.23221, 2026.
3. **PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning**, arXiv:2602.22809, 2026.
4. **CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Use**, arXiv:2607.05465, 2026.
5. **GenClaw: Code-Driven Agentic Image Generation**, arXiv:2605.30248, 2026.
6. **Qwen-Image-Agent: Bridging the Context Gap in Real-World Image Generation**, arXiv:2606.26907, 2026.
7. Anmol Agarwal et al., **COMBAT: Conditional World Models for Behavioral Agent Training**, arXiv:2603.00825, 2026.
8. Junchao Huang et al., **LIVE: Long-horizon Interactive Video World Modeling**, arXiv:2602.03747, 2026.
9. **DreamX-World 1.0: A General-Purpose Interactive World Model**, arXiv:2606.16993, 2026.
10. Hongbo Lu et al., **The DAWN of World-Action Interactive Models**, arXiv:2605.11550, 2026.
11. Dani Valevski et al., **Diffusion Models Are Real-Time Game Engines**, arXiv:2408.14837, 2024.
12. Jake Bruce et al., **Genie: Generative Interactive Environments**, arXiv:2402.15391, 2024.
13. VWDC-01, GVSS-01–10, WDC-01–08, and frozen RRT-20, internal series artifacts, 2026.

---

# 146. Conclusion

VWDC-01 showed that an image is an observation, not a world.

VWDC-02 shows how visual artifacts and worlds can nevertheless participate in one typed computational graph.

The graph distinguishes:

$$
\boxed{
\text{GENERATE}
}
$$

$$
\boxed{
\text{EDIT}
}
$$

$$
\boxed{
\text{LIFT}
}
$$

$$
\boxed{
\text{VALIDATE}
}
$$

$$
\boxed{
\text{FORK}
}
$$

$$
\boxed{
\text{INTERVENE}
}
$$

$$
\boxed{
\text{RENDER}
}
$$

$$
\boxed{
\text{CHECKPOINT/RESTORE}
}
$$

$$
\boxed{
\text{EVALUATE}.
}
$$

Composition can reach states outside any one provider's one-step union.

But every additional edge can also transport cost, semantic defect, identity drift, dynamics uncertainty, and evidence debt.

A repeated operation type can be productive when it creates new states.

An exact state-return cycle with no new evidence and nonnegative debt is removable.

RESTORE can revisit old state without creating a provenance cycle because the restored world receives a new identity.

And deterministic visual transformations do not multiply independent evidence.

The canonical VWDC-02 principle is:

$$
\boxed{
\textbf{
Composition creates capability only when the transformations are type-valid,
contract-valid, and provenance-preserving.
A longer path can reach farther than any single provider,
but every edge also creates a place where cost, defect, identity, dynamics,
or evidence semantics can change.
}
}
$$

This establishes the mixed visual/world reachability graph on which later branching and evidence governance can operate.

---

# Canonical-source policy

This file is the canonical UTF-8 source artifact.

- Canonical inline mathematics uses ` $...$ `.
- Canonical display mathematics uses `$$...$$`.
- No Unicode mathematical-symbol conversion is used as source normalization.
- No `unicode_escape` round trip is used.
- Backslashes and delimiters are preserved literally.
- Validation is required before release.
- This paper does not merge or rename GVSS, WDC, or RRT.
