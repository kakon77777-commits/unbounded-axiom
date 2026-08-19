# GVSS × WDC Bridge Handoff v0.1
## 從全域視覺空間到分支可運行世界：Visual State、World State、Compositional Reachability 與 Branching Runtime 的正式接口

**Date:** 2026-08-17  
**Status:** Bridge / handoff document  
**Series involved:**  
- Global Visual Space & Generative Navigation (GVSS)  
- Branching World Computation / World-Domain Cognitive Runtime (WDC)  
- Frozen Reflexive Representation Theory (RRT) as shared meta-layer

---

# 1. Canonical non-identity

The first bridge rule is:

$$
\boxed{
\text{Visual State}
\neq
\text{World State}.
}
$$

A digital image:

$$
I\in\Omega_\Sigma
$$

is a visual state or visual observation.

A WDC runnable world is a persistent or transient executable object with at least a declared subset of:

$$
\boxed{
W
=
(
X,
D,
A,
\mathcal I,
R,
\tau,
H,
\mathsf{ID},
\mathsf{Prov},
B
),
}
$$

where these coordinates denote, schematically:

- world state $X$;
- dynamics $D$;
- action interface $A$;
- intervention interface $\mathcal I$;
- rule set $R$;
- local world time $\tau$;
- history $H$;
- world identity;
- provenance;
- budget.

Therefore an image cannot be silently upgraded into a runnable world.

---

# 2. Visual observation operator

A WDC world can expose a visual observation:

$$
\boxed{
O_{\mathrm{vis}}:
X_W
\to
\Omega_\Sigma.
}
$$

At world-local time $\tau$:

$$
\boxed{
I_\tau
=
O_{\mathrm{vis}}(
X_W(\tau)
).
}
$$

This makes GVSS a natural visual observation/representation layer for WDC.

The rendered image is not the full hidden world state.

---

# 3. GVSS as the WDC visual plane

GVSS contributes:

- ambient visual state space $\Omega_\Sigma$;
- visual constraints;
- visual reachable domains;
- visual search policies;
- evaluator/observer geometry;
- provider portfolios;
- task-conditioned routing;
- visual failure diagnosis;
- visual provenance.

WDC contributes:

- runnable state;
- dynamics;
- local time;
- checkpoints;
- world identity;
- fork/branch;
- interventions;
- cross-world evidence;
- world governor;
- world ensembles;
- tri-temporal assimilation.

The bridge is:

$$
\boxed{
\text{WDC World State}
\overset{O_{\mathrm{vis}}}{\longrightarrow}
\text{GVSS Visual State}.
}
$$

---

# 4. Visual generation can instantiate world observations

A visual generator/provider can be used as:

1. a renderer of an already-defined world state;
2. a visual observation synthesizer;
3. a candidate world-state initializer;
4. a world-model backend component.

These roles are not equivalent.

In particular:

$$
\boxed{
\text{generated image}
\not\Rightarrow
\text{world initialized with valid hidden dynamics}.
}
$$

---

# 5. GVSS-11 is the bridge point

The planned GVSS-11 was:

**Compositional Visual Reachability Graphs and Cross-Provider Transformation Paths**

This should now be treated as the transition paper from visual composition to runnable-world composition.

The original GVSS path:

$$
\nu_1
\to
\nu_2
\to
\cdots
\to
\nu_m
$$

transforms visual artifacts.

WDC branch paths:

$$
W_0
\to
W_1
\to
\cdots
\to
W_m
$$

transform executable world states.

The two graphs can be connected, but must not be identified.

---

# 6. Provider transformation edge

GVSS edge:

$$
\boxed{
e_{ij}^{\mathrm{vis}}:
I
\mapsto
I'
}
$$

can represent:

- generation;
- inpainting;
- restyling;
- typography;
- upscaling;
- reference repair;
- character repair.

It changes a visual artifact.

---

# 7. World transformation edge

WDC edge:

$$
\boxed{
e_{ij}^{\mathrm{world}}:
W
\mapsto
W'
}
$$

can represent:

- fork;
- intervention;
- rule mutation;
- state mutation;
- model/backend replacement;
- checkpoint restore;
- counterfactual branch.

It changes a runnable-world object or world lineage.

---

# 8. Observation-only path versus world-changing path

A sequence of image edits may leave the hidden world unchanged:

$$
\boxed{
W
\to
I_0
\to
I_1
\to
I_2.
}
$$

This is a visual observation path.

A world intervention changes world state/dynamics:

$$
\boxed{
W_0
\to
W_1
\to
I_1.
}
$$

This is a world branch followed by observation.

The runtime must declare which type occurred.

---

# 9. Visual reachability versus world reachability

GVSS:

$$
\boxed{
\mathcal R_{\mathrm{vis}}
\subseteq
\Omega_\Sigma.
}
$$

WDC:

$$
\boxed{
\mathcal R_{\mathrm{world}}
\subseteq
\mathcal W,
}
$$

where $\mathcal W$ is the declared world-state/world-contract space.

The projection satisfies:

$$
\boxed{
O_{\mathrm{vis}}
(
\mathcal R_{\mathrm{world}}
)
\subseteq
\mathcal R_{\mathrm{vis}}^{\mathrm{possible}}
}
$$

under a compatible renderer/observer.

But generally:

$$
\boxed{
\mathcal R_{\mathrm{vis}}
\not\Rightarrow
\mathcal R_{\mathrm{world}}.
}
$$

A visually plausible image can correspond to no valid world state under the current world contract.

---

# 10. Visual plausibility trap

A high-fidelity visual frame can violate:

- physical state consistency;
- hidden object persistence;
- agent memory;
- causal history;
- rule consistency;
- world checkpoint semantics.

Therefore:

$$
\boxed{
\text{visual realism}
\not\Rightarrow
\text{world validity}.
}
$$

This is directly compatible with WDC-01's evidence boundary.

---

# 11. World-to-visual contract

Define a visual world contract:

$$
\boxed{
\mathsf{VWC}
=
(
O_{\mathrm{vis}},
\Sigma,
\mathcal C_{\mathrm{vis}},
E_{\mathrm{vis}},
D_{\mathrm{transport}},
\mathsf{Prov}
).
}
$$

It records:

- world-to-image observer;
- raster specification;
- visual constraints;
- evaluator;
- transport/render defect;
- provenance.

---

# 12. GVSS provider portfolio becomes WDC backend portfolio

GVSS-09 defines provider portfolio:

$$
S\subseteq\mathcal P.
$$

WDC can reuse this as a portfolio of:

- render backends;
- learned world-model backends;
- visual simulators;
- repair tools;
- external simulation providers.

But provider capability must be typed.

A provider good at visual rendering need not be valid for world dynamics.

---

# 13. Typed provider capability

For provider $\nu$ define separate capability contracts:

$$
\boxed{
\mathbf C_\nu
=
(
C_{\mathrm{render}},
C_{\mathrm{dynamics}},
C_{\mathrm{state}},
C_{\mathrm{intervention}},
C_{\mathrm{replay}},
C_{\mathrm{evidence}}
).
}
$$

Do not collapse them into one score.

---

# 14. GVSS router becomes a WDC sub-router

GVSS-10 routes a task $\theta$ to provider $\nu$.

WDC can invoke this router for the visual/rendering subproblem:

$$
\boxed{
\pi_{\mathrm{vis}}(
\theta_{\mathrm{vis}}
)
\to
\nu.
}
$$

The WDC Governor remains responsible for world-level choices such as:

- spawn;
- fork;
- pause;
- kill;
- promote;
- compute;
- verify;
- allocate budget.

Thus:

$$
\boxed{
\text{GVSS Router}
\subset
\text{WDC Governor action stack}
}
$$

conceptually, not necessarily as strict software inheritance.

---

# 15. WDC Governor and GVSS controller

GVSS asks:

> Which visual action/provider should I use?

WDC asks:

> Which world or world-operation deserves computation?

The bridge state can be:

$$
\boxed{
S_t
=
(
\mathcal W_t,
\mathcal V_t,
E_t,
B_t,
\mathsf{Prov}_t
).
}
$$

where:

- $\mathcal W_t$ is active world ensemble;
- $\mathcal V_t$ is visual/provider state;
- $E_t$ is evidence state;
- $B_t$ is compute budget.

---

# 16. World Lift Operator from visual candidates

A visual artifact can propose a world candidate:

$$
\boxed{
L_{\mathrm{vis}\to W}:
I
\mapsto
\widehat W.
}
$$

But the lift is partial.

Some images are not liftable into a world satisfying:

- state consistency;
- rules;
- dynamics;
- actor identity;
- checkpoint/replay requirements.

Therefore define:

$$
\boxed{
\operatorname{Dom}(
L_{\mathrm{vis}\to W}
)
\subseteq
\Omega_\Sigma.
}
$$

---

# 17. Unliftable visual state

If:

$$
I
\notin
\operatorname{Dom}(
L_{\mathrm{vis}\to W}
),
$$

then the correct conclusion is:

$$
\boxed{
\text{not liftable under current world contract},
}
$$

not:

$$
\boxed{
\text{impossible world}.
}
$$

This mirrors WDC-08's unliftable-future boundary.

---

# 18. Compositional reachability can cross the union boundary

GVSS-09 one-stage portfolio union is:

$$
\bigcup_\nu
\mathcal R_\nu.
$$

But a cross-provider composition:

$$
K_{\nu_m}
\circ
\cdots
\circ
K_{\nu_1}
$$

can produce states unreachable by any single one-stage provider.

Therefore GVSS-11 should define:

$$
\boxed{
\operatorname{Reach}_{\mathcal G}^{(m)}
}
$$

for a typed provider transformation graph $\mathcal G$.

This is the direct visual precursor of WDC branching reachability.

---

# 19. Typed compositional graph

Define:

$$
\boxed{
G_{\mathrm{VW}}
=
(
V,
E
),
}
$$

with node types:

- visual artifact;
- visual provider;
- world checkpoint;
- runnable world;
- evaluator;
- intervention.

Edges are typed:

- render;
- generate;
- edit;
- lift;
- fork;
- intervene;
- observe;
- evaluate;
- checkpoint;
- restore.

No silent type coercion is allowed.

---

# 20. Defect transport across visual/world paths

Each edge has defect vector:

$$
\boxed{
d_e
=
(
d_{\mathrm{semantic}},
d_{\mathrm{style}},
d_{\mathrm{identity}},
d_{\mathrm{state}},
d_{\mathrm{dynamics}},
d_{\mathrm{evidence}}
).
}
$$

A path:

$$
p=e_1\cdots e_m
$$

must transport/accumulate defects under declared composition rules.

This is the RRT bridge.

---

# 21. World lineage and visual lineage

GVSS preserves visual artifact lineage.

WDC preserves world identity/fork lineage.

The bridge requires both:

$$
\boxed{
\mathsf{Lineage}
=
(
\mathsf{WorldLineage},
\mathsf{VisualLineage},
\mathsf{BridgeEdges}
).
}
$$

An image generated from a child world must not be attributed to the parent world without the branch record.

---

# 22. Evidence boundary

A world output image can provide evidence about the world.

It is not automatically evidence about external reality.

Thus:

$$
\boxed{
\text{GVSS visual evidence}
\to
\text{WDC world-relative evidence}
}
$$

before any reality transport.

This is the WDC-01/WDC-05 evidence boundary.

---

# 23. Cross-world visual comparison

GVSS evaluators can compare observations from sibling worlds:

$$
I^{(1)}_\tau,
I^{(2)}_\tau.
$$

But world evidence aggregation must preserve:

- shared parent;
- shared model assumptions;
- provider dependence;
- evaluator dependence.

Many visually diverse worlds can still share one modeling error.

---

# 24. World portfolio and provider portfolio are nested portfolios

WDC-06 has a world computation portfolio.

GVSS-09 has a provider capability portfolio.

These are different allocation units.

One world may be rendered/executed through several providers.

One provider may serve several worlds.

Therefore the combined allocation is bipartite/multi-layer:

$$
\boxed{
\text{World Portfolio}
\times
\text{Provider Portfolio}.
}
$$

---

# 25. Compute-value decomposition

A world-operation can have value:

$$
\boxed{
V_{\mathrm{world}}
=
V_{\mathrm{epistemic}}
+
V_{\mathrm{decision}}
+
V_{\mathrm{verification}}
+
V_{\mathrm{option}}
-
C_{\mathrm{world}}.
}
$$

A provider path contributes additional cost:

$$
\boxed{
C_{\mathrm{provider}}
+
C_{\mathrm{switch}}
+
C_{\mathrm{calibration}}
+
D_{\mathrm{transport}}.
}
$$

The WDC Governor should choose the full world/provider computation path, not merely the visually strongest provider.

---

# 26. Proposed bridge sequence

Do not immediately continue ordinary GVSS-11 as if WDC did not exist.

Recommended bridge sequence:

## Bridge Paper A

**VWDC-01 — From Visual Reachability to Runnable World Reachability**  
**從視覺可達域到可運行世界可達域**

Core:
- image state vs world state;
- observation operator;
- visual-to-world lift;
- unliftable visual states;
- world validity vs visual realism.

## Bridge Paper B

**VWDC-02 — Compositional Visual-World Reachability Graphs**  
**組合式視覺—世界可達圖**

Core:
- typed nodes/edges;
- provider paths;
- world fork paths;
- composition outside single-provider union;
- defect transport;
- shortest-cost path.

## Bridge Paper C

**VWDC-03 — Visual World Branching, Lineage, and Evidence Transport**  
**視覺世界分支、譜系與證據轉移**

Core:
- checkpoints;
- world/visual lineage;
- sibling-world comparison;
- evidence provenance;
- no silent merge.

Then decide whether later work continues primarily as GVSS, WDC, or the bridge series.

---

# 27. Why not rename this GVSS-11 immediately?

Because GVSS-11's original scope is still visual composition.

WDC introduces:

- persistent state;
- dynamics;
- world-local time;
- branch identity;
- intervention;
- evidence boundary.

These are genuinely new object types.

A bridge paper avoids silently changing the meaning of "reachability" mid-series.

---

# 28. Canonical bridge theorem target

The first bridge theorem should have the form:

Let:

$$
O_{\mathrm{vis}}:
\mathcal W
\to
\Omega_\Sigma
$$

be a visual observer and:

$$
L:
D_L\subseteq
\Omega_\Sigma
\to
\mathcal W
$$

a partial world-lift operator.

Then:

$$
\boxed{
L(
O_{\mathrm{vis}}(W)
)
\sim_{\mathcal C_W}
W
}
$$

only under an explicit world-equivalence/contract condition.

In general:

$$
\boxed{
L\circ O_{\mathrm{vis}}
\neq
\mathrm{Id}_{\mathcal W}.
}
$$

Visual rendering loses hidden state, and world lifting is not inverse rendering without sufficient information.

This should be the bridge's foundational no-go.

---

# 29. Canonical no-go

$$
\boxed{
\textbf{
A visually reachable future is not necessarily a runnable world,
and a runnable world is not validated by visual plausibility alone.
}
}
$$

---

# 30. Canonical positive principle

$$
\boxed{
\textbf{
GVSS can serve as the visual observation, constraint, generation, evaluation, and provider-routing layer of WDC,
while WDC supplies persistent dynamics, branching identity, interventions, world evidence, and governance.
}
}
$$

---

# 31. Immediate next action

Do not draft GVSS-11 in its old form yet.

Start with:

$$
\boxed{
\textbf{
VWDC-01 — From Visual Reachability to Runnable World Reachability
}
}
$$

and use both existing corpora as dependencies.

After that, GVSS-11 can either:

1. be absorbed into VWDC-02; or
2. remain a purely visual compositional-path paper with an explicit WDC bridge.

