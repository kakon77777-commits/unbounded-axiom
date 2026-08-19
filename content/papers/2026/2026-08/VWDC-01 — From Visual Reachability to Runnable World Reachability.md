# VWDC-01 — From Visual Reachability to Runnable World Reachability
## 從視覺可達域到可運行世界可達域：觀察纖維、世界提升、動力閉包與可運行契約

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 01  
**Depends on:** GVSS-01–10, WDC-01–08, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal bridge paper. Observation/lift non-invertibility, task-relative reconstruction, visual-liftability, deterministic observation-dynamics closure, static-frame dynamics no-go, probe/history refinement, world-reachability projection, visual-reachability non-converse, render-consistency/world-validity separation, runnable-contract gating, and evidence-boundary results are proved under the stated hypotheses. Interactive world models, latent-state world models, inverse rendering, neural scene reconstruction, POMDP observation models, and generated interactive environments are established neighboring research and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** runnable world, visual state space, world model, world lift, observation quotient, latent state, partial observability, interactive environment, world reachability, inverse rendering, branching worlds, GVSS, WDC

---

# Abstract

The Global Visual Space & Generative Navigation series treats a digital image as a state

$$
\boxed{
I
\in
\Omega_\Sigma
}
$$

inside a finite raster state space.

The World-Domain Computation series treats a runnable world as an executable object with:

- addressable state;
- transition semantics;
- action/intervention interface;
- persistent or replayable history;
- observation/evaluation interface;
- bounded resource contract;
- provenance and termination semantics.

These two objects must not be identified.

The bridge begins with the canonical non-identity:

$$
\boxed{
\text{Visual State}
\neq
\text{Runnable World State}.
}
$$

A world can expose a visual observation through:

$$
\boxed{
O_{\mathrm{vis}}:
\mathcal X_W
\to
\Omega_\Sigma.
}
$$

At world-local time $\tau$:

$$
\boxed{
I_\tau
=
O_{\mathrm{vis}}
(
X_W(\tau)
).
}
$$

A single rendered image can hide:

- velocities;
- occluded objects;
- agent memory;
- causal history;
- random seeds;
- latent physics parameters;
- goals;
- rules;
- branch identity;
- future transition semantics.

Therefore visual rendering is generally many-to-one.

For any image $I$, define the visual observation fiber:

$$
\boxed{
\mathcal F_I
=
O_{\mathrm{vis}}^{-1}(I).
}
$$

A deterministic world-lift operator is a partial map:

$$
\boxed{
L:
D_L
\subseteq
\Omega_\Sigma
\to
\mathcal X_W.
}
$$

The first bridge theorem is elementary but foundational.

If there exists a global exact lift satisfying:

$$
\boxed{
L
\circ
O_{\mathrm{vis}}
=
\operatorname{Id}_{\mathcal X_W},
}
$$

then:

$$
\boxed{
O_{\mathrm{vis}}
\text{ must be injective}.
}
$$

Conversely, an injective observer admits an inverse on its image.

Hence whenever two distinct world states render identically:

$$
x\neq x',
$$

$$
O_{\mathrm{vis}}(x)=O_{\mathrm{vis}}(x'),
$$

no deterministic image-only lift can reconstruct both exactly.

Thus:

$$
\boxed{
\text{rendering}
\not\Rightarrow
\text{invertible world encoding}.
}
$$

The correct object reconstructed from one image is generally an observation-equivalence class:

$$
\boxed{
[x]_{\mathrm{vis}}
=
\{
x':
O_{\mathrm{vis}}(x')=O_{\mathrm{vis}}(x)
\}.
}
$$

A world lift chooses one candidate from this class or from an approximation to it.

It does not identify the original world without additional information.

---

## Visual liftability

Let:

$$
\mathcal W_\kappa
$$

be the set of world states/instances satisfying a declared runnable-world contract $\kappa$.

Define the visual images realizable by valid worlds:

$$
\boxed{
\mathcal L_\kappa
=
O_{\mathrm{vis}}
(
\mathcal W_\kappa
).
}
$$

Then an image is liftable under contract $\kappa$ exactly when:

$$
\boxed{
I
\in
\mathcal L_\kappa.
}
$$

This is contract-relative liftability.

It does not imply uniqueness.

A visually plausible image can lie outside:

$$
\mathcal L_\kappa
$$

because no state satisfying the declared world rules, hidden-state requirements, identity constraints, or dynamics can render that image.

Therefore:

$$
\boxed{
\text{visual plausibility}
\not\Rightarrow
\text{world-contract liftability}.
}
$$

---

## Dynamics closure is stronger than render consistency

A world is runnable because it changes.

Let deterministic action-conditioned dynamics be:

$$
\boxed{
D_a:
\mathcal X_W
\to
\mathcal X_W.
}
$$

One may ask whether image state alone supports a deterministic visual dynamics:

$$
\boxed{
\overline D_a:
\Omega_\Sigma
\to
\Omega_\Sigma
}
$$

such that:

$$
\boxed{
O_{\mathrm{vis}}
\circ
D_a
=
\overline D_a
\circ
O_{\mathrm{vis}}.
}
$$

This is possible exactly when the next rendered observation is constant on every current visual fiber:

$$
\boxed{
O_{\mathrm{vis}}(x)
=
O_{\mathrm{vis}}(x')
\Longrightarrow
O_{\mathrm{vis}}(
D_a(x)
)
=
O_{\mathrm{vis}}(
D_a(x')
)
}
$$

for all $x,x'$ and action $a$.

This is the deterministic **visual dynamics closure criterion**.

If the criterion fails, current image alone is not a sufficient Markov state for the rendered dynamics.

A minimal counterexample has two hidden states:

$$
x_1,
x_2
$$

with identical current image:

$$
O_{\mathrm{vis}}(x_1)
=
O_{\mathrm{vis}}(x_2)
=
I_0,
$$

but one action produces:

$$
O_{\mathrm{vis}}(
D_a(x_1)
)
=
I_L,
$$

$$
O_{\mathrm{vis}}(
D_a(x_2)
)
=
I_R,
$$

where:

$$
I_L\neq I_R.
$$

Then no function:

$$
\overline D_a(I_0)
$$

can equal both outputs.

Therefore:

$$
\boxed{
\text{one rendered frame}
\not\Rightarrow
\text{closed runnable dynamics}.
}
$$

This is why modern world-model systems frequently maintain latent state, observation history, or action-conditioned temporal representations rather than treating each image as an independent world state.

Genie learns a spatiotemporal tokenizer, autoregressive dynamics model, and latent action model for action-controllable generated environments.

GameNGen predicts the next game frame conditioned on past frames and actions.

These are prior systems results.

VWDC-01 uses them only as engineering evidence that interactive visual worlds require temporal/action structure beyond isolated image generation.

---

## History can refine world identifiability

Let a diagnostic/action sequence be:

$$
\mathbf a
=
(
a_0,\ldots,a_{T-1}
).
$$

Define history observation:

$$
\boxed{
O_{\mathbf a}^{(T)}(x)
=
(
O(x),
O(D_{a_0}x),
\ldots,
O(D_{a_{T-1}}\cdots D_{a_0}x)
).
}
$$

If one history observer contains all probes of another plus additional observations, then its equivalence classes refine the older classes.

Thus additional action-conditioned observations can split world states that one frame cannot distinguish.

This is the deterministic bridge to:

- active observation;
- POMDP belief state;
- system identification;
- WDC interventions;
- RRT probe-set refinement.

But no finite history is guaranteed to identify every world.

---

## Task-relative world reconstruction

Exact full-state recovery is often unnecessary.

Let:

$$
h:
\mathcal X_W
\to
\mathcal Z
$$

be the world property needed for a task.

Examples:

- whether the world satisfies one safety invariant;
- whether a target object exists;
- whether a particular intervention outcome is possible;
- whether two worlds belong to the same contract-equivalence class.

A task property is visually recoverable iff it is constant on observation fibers:

$$
\boxed{
O(x)=O(x')
\Longrightarrow
h(x)=h(x').
}
$$

Then there exists:

$$
\boxed{
\bar h:
O(\mathcal X_W)
\to
\mathcal Z
}
$$

such that:

$$
\boxed{
h
=
\bar h
\circ
O.
}
$$

This is the correct task-relative replacement for full world inversion.

The image can be sufficient for one task while insufficient for another.

---

## Reachability projection

Let:

$$
\boxed{
\mathcal R_W(
x_0,
\mathcal A,
B
)
}
$$

be the states reachable by a runnable world from initial state $x_0$ under admissible actions/interventions and budget $B$.

The corresponding visually observable reachable set is:

$$
\boxed{
\mathcal R_{\mathrm{obs}}
=
O_{\mathrm{vis}}
(
\mathcal R_W
).
}
$$

Therefore every world-reachable state produces a reachable observation:

$$
\boxed{
O_{\mathrm{vis}}
(
\mathcal R_W
)
=
\mathcal R_{\mathrm{obs}}.
}
$$

But a GVSS generator/provider portfolio can have visual reachable domain:

$$
\boxed{
\mathcal R_{\mathrm{GVSS}}
\subseteq
\Omega_\Sigma
}
$$

strictly larger than:

$$
\mathcal R_{\mathrm{obs}}.
$$

A generative image model can synthesize an image that no valid runnable state under the current world contract can produce.

Therefore:

$$
\boxed{
\mathcal R_{\mathrm{GVSS}}
\not\subseteq
O_{\mathrm{vis}}(
\mathcal R_W
)
}
$$

in general.

The correct bridge target is:

$$
\boxed{
\mathcal R_{\mathrm{GVSS}}
\cap
\mathcal L_\kappa,
}
$$

the visually reachable states that are also liftable under the declared world contract.

---

## Render consistency is not world validity

A world-lift candidate:

$$
\widehat W=L(I)
$$

can satisfy perfect image reconstruction:

$$
\boxed{
O_{\mathrm{vis}}(
\widehat W
)
=
I.
}
$$

Yet still violate:

- transition rules;
- hidden-state consistency;
- identity;
- history;
- replay;
- action interface;
- resource contract;
- provenance.

Hence:

$$
\boxed{
\text{zero render error}
\not\Rightarrow
\text{runnable-world validity}.
}
$$

The bridge therefore distinguishes three nested conditions:

### Render-consistent lift

$$
\boxed{
O_{\mathrm{vis}}(
L(I)
)
\approx I.
}
$$

### Contract-valid lift

$$
\boxed{
L(I)
\in
\mathcal W_\kappa.
}
$$

### Evidence-valid lift

Any claim transported outside the world must additionally satisfy a world-to-reality evidence-transport contract.

Thus:

$$
\boxed{
\text{render consistency}
\not\Rightarrow
\text{world validity}
\not\Rightarrow
\text{reality evidence}.
}
$$

---

## Runnable-world contract

VWDC-01 inherits the WDC runnable minimum:

$$
\boxed{
\begin{aligned}
R_1 &: \text{Addressable State},\\
R_2 &: \text{Transition Semantics},\\
R_3 &: \text{Action / Intervention Interface},\\
R_4 &: \text{Persistent or Replayable History},\\
R_5 &: \text{Observation / Evaluation Interface},\\
R_6 &: \text{Bounded Resource Contract},\\
R_7 &: \text{Provenance / Termination Contract}.
\end{aligned}
}
$$

A visual artifact that provides only:

$$
I
$$

and perhaps an aesthetic score is not thereby a runnable world.

Conversely, a symbolic or nonvisual environment can be a runnable world if it satisfies the runnable contract.

Therefore:

$$
\boxed{
\text{Worldness}_{WDC}
\neq
\text{Visual Realism}.
}
$$

---

## Current interactive world-model boundary

Modern systems increasingly blur the engineering boundary between rendered video and executable simulation.

Genie generates action-controllable interactive environments from videos/images/text/sketches using temporal and latent-action modeling.

GameNGen demonstrates a diffusion model acting as a real-time neural game engine with next-frame generation conditioned on past frames and actions.

DIAMOND trains agents in diffusion world models and also demonstrates an interactive neural game engine.

Genie 3, as described by Google DeepMind, generates real-time interactive worlds with consistency over a limited interaction horizon and supports promptable world events.

These systems support the practical importance of visual world modeling.

They do **not** erase the VWDC distinction between:

- rendered observations;
- complete hidden state;
- explicit replayable world contract;
- external real-world evidence.

---

# 1. Permanent bridge boundaries

The bridge begins with four non-identities.

$$
\boxed{
\text{Image}
\neq
\text{World}.
}
$$

$$
\boxed{
\text{Visual Plausibility}
\neq
\text{Runnable Validity}.
}
$$

$$
\boxed{
\text{Render Consistency}
\neq
\text{Dynamics Consistency}.
}
$$

$$
\boxed{
\text{World-Internal Evidence}
\neq
\text{Reality Evidence}.
}
$$

---

# 2. Visual state

For fixed raster specification:

$$
\Sigma=(W,H,C,b),
$$

GVSS defines:

$$
\boxed{
\Omega_\Sigma
=
\{0,\ldots,2^b-1\}^{WHC}.
}
$$

An image is:

$$
I\in\Omega_\Sigma.
$$

---

# 3. Runnable world instance

VWDC inherits the WDC instance tuple:

$$
\boxed{
W
=
(
ID,
Parent,
X,
\mathcal D,
\mathcal A,
\mathcal G,
\mathcal H,
\Theta,
\mathcal O,
\mathcal E,
\mathbf B,
\kappa
).
}
$$

The visual observer is one component/sub-interface of:

$$
\mathcal O.
$$

---

# 4. World state versus world instance

The current world state:

$$
X_t
$$

is not the entire world instance.

The instance also carries:

- identity;
- transition system;
- rules;
- history;
- model/version;
- evaluator;
- budget;
- contract.

Thus even an exact reconstruction of $X_t$ may not reconstruct the world instance.

---

# 5. Visual observer

## Definition VWDC01-D1

A visual observer is:

$$
\boxed{
O_{\mathrm{vis}}:
\mathcal X
\to
\Omega_\Sigma.
}
$$

It can be:

- renderer;
- camera model;
- screen capture;
- learned decoder;
- generated visual report.

---

# 6. Observation fiber

## Definition VWDC01-D2

For image:

$$
I,
$$

$$
\boxed{
\mathcal F_I
=
\{
x\in\mathcal X:
O_{\mathrm{vis}}(x)=I
\}.
}
$$

World states in the same fiber are visually indistinguishable under the current observer.

---

# 7. Visual equivalence

## Definition VWDC01-D3

$$
\boxed{
x
\sim_{\mathrm{vis}}
x'
\iff
O_{\mathrm{vis}}(x)
=
O_{\mathrm{vis}}(x').
}
$$

This is an equivalence relation.

---

# 8. Visual quotient

$$
\boxed{
\mathcal X/
\sim_{\mathrm{vis}}.
}
$$

A rendered frame identifies at most one visual equivalence class unless the observer is injective.

---

# 9. World lift

## Definition VWDC01-D4

A world lift is a partial map:

$$
\boxed{
L:
D_L
\subseteq
\Omega_\Sigma
\to
\mathcal X
}
$$

or, for full instances:

$$
\boxed{
L_W:
D_L
\to
\mathcal W_\kappa.
}
$$

---

# 10. VWDC01-T1 — Exact global visual inversion requires injectivity

## Theorem VWDC01-T1

If there exists:

$$
L:
O(\mathcal X)
\to
\mathcal X
$$

such that:

$$
\boxed{
L\circ O
=
\operatorname{Id}_{\mathcal X},
}
$$

then $O$ is injective.

### Proof

Assume:

$$
O(x)=O(x').
$$

Apply $L$:

$$
L(O(x))
=
L(O(x')).
$$

By the left-inverse condition:

$$
x=x'.
$$

 $\square$

---

# 11. Converse

If $O$ is injective, its inverse on:

$$
O(\mathcal X)
$$

is a left inverse.

Therefore exact reconstruction from observations is equivalent to injectivity on the domain being reconstructed.

---

# 12. VWDC01-N1 — One image can be compatible with multiple worlds

If:

$$
x\neq x'
$$

but:

$$
O(x)=O(x'),
$$

then no deterministic image-only lift can return both original states.

Any lift must choose at most one representative.

 $\square$

---

# 13. Example: hidden velocity

World state:

$$
x=(q,v).
$$

Observer:

$$
O(q,v)=q.
$$

Then:

$$
(q,+1)
$$

and:

$$
(q,-1)
$$

render identically.

Under one time step:

$$
q'=q+v,
$$

they produce different future observations.

A still frame cannot recover velocity.

---

# 14. Example: occluded object

Two worlds can render the same camera image while differing in an object behind the camera.

If later action rotates the camera, the observations diverge.

The hidden object is world state but not current visual state.

---

# 15. Example: agent memory

Two visually identical agents can carry different internal memories/goals.

They can choose different future actions despite identical current frames.

Visual state is not agent state.

---

# 16. Task property

## Definition VWDC01-D5

Let:

$$
h:
\mathcal X
\to
\mathcal Z
$$

be a world property needed by a task.

---

# 17. VWDC01-T2 — Task-relative visual sufficiency

## Theorem VWDC01-T2

There exists:

$$
\bar h:
O(\mathcal X)
\to
\mathcal Z
$$

such that:

$$
\boxed{
h
=
\bar h
\circ
O
}
$$

if and only if:

$$
\boxed{
O(x)=O(x')
\Longrightarrow
h(x)=h(x').
}
$$

### Proof

Necessity follows by applying $\bar h$ to equal observations.

For sufficiency, define:

$$
\bar h(O(x))
=
h(x).
$$

Fiber constancy makes this well-defined.

 $\square$

---

# 18. Interpretation

A visual frame can be sufficient to answer:

> Is the door visibly open?

while insufficient to answer:

> Is the unseen room occupied?

Sufficiency is task-relative.

---

# 19. Approximate reconstruction

Let world target space:

$$
(\mathcal Z,d)
$$

be metric.

Define:

$$
\boxed{
\delta_\infty(h\mid O)
=
\inf_T
\sup_x
d(
h(x),
T(O(x))
).
}
$$

This is the deterministic reconstruction deficiency inherited from the RRT observer layer.

---

# 20. Fiber-radius reconstruction

Under the same conditions as the RRT-07 fiber-radius theorem:

$$
\boxed{
\delta_\infty(h\mid O)
=
\sup_I
\operatorname{rad}
h(\mathcal F_I).
}
$$

Thus visual ambiguity is quantified by the spread of task values inside one image fiber.

VWDC does not re-claim this observer theorem as new.

---

# 21. Runnable contract set

## Definition VWDC01-D6

For world contract $\kappa$, define:

$$
\boxed{
\mathcal W_\kappa
=
\{
W:
W
\text{ satisfies all declared runnable-world obligations}
\}.
}
$$

---

# 22. Liftable visual set

## Definition VWDC01-D7

$$
\boxed{
\mathcal L_\kappa
=
O_{\mathrm{vis}}(
\mathcal W_\kappa
).
}
$$

---

# 23. VWDC01-T3 — Contract-relative liftability criterion

## Theorem VWDC01-T3

An image $I$ admits at least one world satisfying contract $\kappa$ and rendering exactly to $I$ iff:

$$
\boxed{
I\in\mathcal L_\kappa.
}
$$

### Proof

Definition of image/range of the restricted observer.

 $\square$

---

# 24. Liftability is not uniqueness

If:

$$
|\mathcal F_I\cap\mathcal W_\kappa|>1,
$$

then multiple valid worlds lift to the same visual frame.

---

# 25. Visual plausibility set

Let:

$$
\mathcal P_{\mathrm{vis}}
$$

be a visual plausibility/acceptance set produced by GVSS evaluators.

No general inclusion holds:

$$
\mathcal P_{\mathrm{vis}}
\subseteq
\mathcal L_\kappa.
$$

---

# 26. VWDC01-N2 — Visual plausibility does not imply world liftability

## Counterexample

Let a contract require:

- two-sided door geometry;
- persistent room topology;
- deterministic collision rules.

Construct an image judged visually plausible but whose depicted geometry violates the contract's realizable topology.

Then:

$$
I\in\mathcal P_{\mathrm{vis}}
$$

but:

$$
I\notin\mathcal L_\kappa.
$$

Therefore:

$$
\boxed{
\text{visual plausibility}
\not\Rightarrow
\text{contract liftability}.
}
$$

The example is contract dependent.

---

# 27. Deterministic world dynamics

Let:

$$
D_a:
\mathcal X
\to
\mathcal X.
$$

---

# 28. Visual dynamics closure

## Definition VWDC01-D8

Visual dynamics are closed under observer $O$ if there exists:

$$
\boxed{
\bar D_a:
O(\mathcal X)
\to
O(\mathcal X)
}
$$

such that:

$$
\boxed{
O\circ D_a
=
\bar D_a\circ O
}
$$

for every admissible action $a$.

---

# 29. VWDC01-T4 — Deterministic visual dynamics closure criterion

## Theorem VWDC01-T4

For fixed action $a$, a well-defined:

$$
\bar D_a
$$

exists iff:

$$
\boxed{
O(x)=O(x')
\Longrightarrow
O(D_a(x))
=
O(D_a(x'))
}
$$

for all $x,x'$.

### Proof

### Necessity

If:

$$
O\circ D_a
=
\bar D_a\circ O,
$$

then equal current observations give equal $\bar D_a$ inputs and therefore equal next observations.

### Sufficiency

Define:

$$
\bar D_a(O(x))
=
O(D_a(x)).
$$

The fiber-constancy hypothesis makes the definition independent of representative.

 $\square$

---

# 30. VWDC01-N3 — Static-frame dynamics no-go

If there exist:

$$
x,x'
$$

with:

$$
O(x)=O(x')
$$

but:

$$
O(D_a(x))
\neq
O(D_a(x')),
$$

then no deterministic image-only next-frame law can represent the world dynamics exactly.

 $\square$

---

# 31. Hidden velocity example revisited

Current frame shows object at coordinate:

$$
q=0.
$$

World A:

$$
v=+1.
$$

World B:

$$
v=-1.
$$

Same image now.

Next images differ.

Therefore the rendered image is not Markov sufficient.

---

# 32. Observation lumpability

VWDC calls the criterion:

$$
\boxed{
\text{visual dynamics lumpability}
}
$$

only as convenient terminology.

Markov/lumpability concepts are classical.

---

# 33. Stochastic dynamics

For stochastic world dynamics:

$$
P(dx'\mid x,a),
$$

a closed Markov observation process requires stronger distributional fiber consistency:

$$
\boxed{
P(
O(X_{t+1})\in B
\mid
x,a
)
}
$$

must depend on $x$ only through:

$$
O(x).
$$

This is the stochastic analogue.

VWDC-01 does not develop the full stochastic theorem.

---

# 34. Belief state

When observations are insufficient, a history-conditioned belief:

$$
\boxed{
b_t(x)
=
P(
X_t=x
\mid
O_{0:t},
A_{0:t-1}
)
}
$$

can serve as a sufficient information state under standard POMDP assumptions.

This is classical POMDP theory.

---

# 35. World history observer

For action sequence:

$$
\mathbf a
=
(a_0,\ldots,a_{T-1}),
$$

define:

$$
\boxed{
O_{\mathbf a}^{(T)}(x)
=
(
O(x_0),
O(x_1),
\ldots,
O(x_T)
)
}
$$

where:

$$
x_{t+1}=D_{a_t}(x_t).
$$

---

# 36. History equivalence

$$
\boxed{
x
\sim_{\mathbf a,T}
x'
\iff
O_{\mathbf a}^{(T)}(x)
=
O_{\mathbf a}^{(T)}(x').
}
$$

---

# 37. Probe family

Let:

$$
\mathcal A_{\mathrm{probe}}
$$

be allowed action/probe sequences.

Define worlds equivalent if all permitted histories agree.

---

# 38. VWDC01-T5 — Additional probes refine observational equivalence

## Theorem VWDC01-T5

Let probe families:

$$
\mathcal Q_1
\subseteq
\mathcal Q_2.
$$

Define:

$$
x\sim_{\mathcal Q}x'
$$

iff all observations induced by all probes in $\mathcal Q$ agree.

Then:

$$
\boxed{
\sim_{\mathcal Q_2}
\subseteq
\sim_{\mathcal Q_1}.
}
$$

### Proof

Agreement on every probe in a larger family implies agreement on every probe in its subset.

 $\square$

This is an RRT-20 probe-set refinement specialization.

---

# 39. More probes do not guarantee identification

Even an infinite set of visual probes can fail to identify hidden variables that never affect visual observations.

Example:

- unused random seed;
- hidden label with no dynamical effect;
- inaccessible internal state.

---

# 40. Active world identification

Interventions can be selected specifically to split visual fibers.

This is the VWDC bridge to:

- WDC branching interventions;
- GVSS diagnostic control;
- active system identification.

---

# 41. World reachable set

## Definition VWDC01-D9

For initial state:

$$
x_0,
$$

admissible action/intervention family:

$$
\mathcal A,
$$

and budget:

$$
B,
$$

define:

$$
\boxed{
\mathcal R_W(
x_0,\mathcal A,B
)
}
$$

as all world states reachable under the runnable contract.

---

# 42. Visual observation reachability

## Definition VWDC01-D10

$$
\boxed{
\mathcal R_{\mathrm{obs}}
(
x_0,\mathcal A,B
)
=
O_{\mathrm{vis}}
\left(
\mathcal R_W(
x_0,\mathcal A,B
)
\right).
}
$$

---

# 43. VWDC01-T6 — World reachability projects to visual reachability

## Theorem VWDC01-T6

Every world-reachable state has a rendered observation in:

$$
\mathcal R_{\mathrm{obs}}.
$$

Equivalently:

$$
\boxed{
O_{\mathrm{vis}}(
\mathcal R_W
)
=
\mathcal R_{\mathrm{obs}}.
}
$$

### Proof

Definition.

 $\square$

The theorem is trivial but fixes the direction of the bridge.

---

# 44. GVSS reachable set

Let:

$$
\boxed{
\mathcal R_{\mathrm{GVSS}}(
S,\Pi,B
)
}
$$

be the practical visual reachable set from the GVSS provider/runtime portfolio.

This set is defined at the image/artifact level.

---

# 45. VWDC01-N4 — Visual reachability has no general world-reachability converse

## Proposition VWDC01-N4

There need not exist:

$$
x\in\mathcal R_W
$$

for every:

$$
I\in\mathcal R_{\mathrm{GVSS}}.
$$

### Proof by construction

Let:

$$
\Omega_\Sigma
=
\{I_0,I_1\}.
$$

Let current world contract admit only one valid world state rendering:

$$
I_0.
$$

Let a visual generator be able to synthesize both:

$$
I_0
$$

and:

$$
I_1.
$$

Then:

$$
I_1\in\mathcal R_{\mathrm{GVSS}}
$$

but:

$$
I_1\notin O(\mathcal R_W).
$$

 $\square$

---

# 46. Bridge-compatible visual reachable set

Define:

$$
\boxed{
\mathcal R_{\mathrm{bridge}}
=
\mathcal R_{\mathrm{GVSS}}
\cap
\mathcal L_\kappa.
}
$$

These are visual states both:

- reachable by the visual generation/navigation stack;
- realizable by at least one world satisfying the current world contract.

---

# 47. Bridge state is still not unique world state

Even:

$$
I\in\mathcal R_{\mathrm{bridge}}
$$

does not identify one world.

It identifies a nonempty world fiber:

$$
\boxed{
\mathcal F_I^\kappa
=
\mathcal F_I
\cap
\mathcal W_\kappa.
}
$$

---

# 48. World-lift candidate set

## Definition VWDC01-D11

$$
\boxed{
\mathsf{LiftSet}_\kappa(I)
=
\{
W\in\mathcal W_\kappa:
O_{\mathrm{vis}}(W)=I
\}.
}
$$

A lift algorithm chooses from this set or approximates it.

---

# 49. Unique lift condition

A unique contract-valid world lift exists iff:

$$
\boxed{
|
\mathsf{LiftSet}_\kappa(I)
|
=
1.
}
$$

This is often too strong.

---

# 50. Render-consistent lift

## Definition VWDC01-D12

A lift is render-consistent at tolerance $\epsilon$ if:

$$
\boxed{
d_{\mathrm{vis}}
(
O_{\mathrm{vis}}(
L(I)
),
I
)
\le
\epsilon.
}
$$

---

# 51. Contract-valid lift

## Definition VWDC01-D13

$$
\boxed{
L(I)
\in
\mathcal W_\kappa.
}
$$

---

# 52. Dynamics-valid lift

A lift is dynamics-valid over test family $\mathcal Q$ if predicted action-conditioned observations satisfy the declared world transition contract over all required probes in $\mathcal Q$.

This is stronger than render consistency.

---

# 53. Evidence-valid lift

A lift is evidence-valid for a real-world claim only when a separately declared evidence-transport contract supports that claim.

This is stronger again.

---

# 54. Validity ladder

$$
\boxed{
\text{render-consistent}
}
$$

$$
\not\Rightarrow
$$

$$
\boxed{
\text{world-contract valid}
}
$$

$$
\not\Rightarrow
$$

$$
\boxed{
\text{dynamics identified}
}
$$

$$
\not\Rightarrow
$$

$$
\boxed{
\text{reality evidence}.
}
$$

---

# 55. VWDC01-N5 — Zero render error does not imply world validity

## Counterexample

Image:

$$
I
$$

depicts a ball suspended in air.

Construct lift:

$$
\widehat W
$$

with a hidden state/rule set violating the declared gravity/transition contract while still rendering exactly to $I$ at current time.

Then:

$$
d_{\mathrm{vis}}(
O(\widehat W),I
)=0,
$$

but:

$$
\widehat W
\notin
\mathcal W_\kappa.
$$

 $\square$

---

# 56. Zero render error also does not identify dynamics

Two contract-valid worlds can render the same current image and satisfy different admissible parameter settings/dynamics if the contract allows them.

One frame cannot select between them.

---

# 57. Dynamic validation

A lift can be challenged with probes:

$$
a_1,\ldots,a_m.
$$

If predicted/rendered trajectories violate observed or contractual constraints, eliminate the candidate world.

This is active world lifting.

---

# 58. World lift as model selection

Single-image world lifting is better understood as:

$$
\boxed{
\text{observation}
+
\text{priors}
+
\text{contract}
\to
\text{candidate world model}.
}
$$

not exact inverse graphics in general.

---

# 59. Inverse rendering literature

Inverse rendering attempts to infer geometry, lighting, reflectance, and related scene attributes from image observations.

Single-image methods rely on learned/physical priors because images do not explicitly contain every hidden scene variable.

NeRF reconstructs scene representations from multiple posed images.

pixelNeRF uses learned priors to infer a scene representation from one or a few images.

These are powerful scene-reconstruction methods.

VWDC does not interpret them as proofs of unique full-world reconstruction.

---

# 60. Scene representation versus runnable world

A 3D radiance field or geometry model can support novel-view rendering.

A runnable world additionally needs:

- transition semantics;
- interventions;
- persistent history;
- actor/state semantics;
- world identity;
- replay;
- provenance.

Thus:

$$
\boxed{
\text{scene representation}
\neq
\text{runnable world instance}.
}
$$

---

# 61. World model literature

World models commonly separate:

- observation representation;
- latent state;
- transition dynamics.

This directly reflects the visual-state/world-state distinction.

A learned world model can be useful even if latent state is not physically interpretable.

VWDC concerns runtime contract semantics, not latent interpretability alone.

---

# 62. Genie relation

Genie creates action-controllable interactive environments from visual/video data.

Its architecture includes temporal representation and latent action dynamics.

This is a direct practical neighbor to the bridge from visual generation to interactive worlds.

---

# 63. GameNGen relation

GameNGen generates the next game frame conditioned on history and action.

This is an explicit example in which current visual state alone is not the only input to the interactive generator.

---

# 64. DIAMOND relation

DIAMOND uses diffusion as a world model for RL and demonstrates interactive neural game-engine behavior.

It supports the claim that high-fidelity visual generation can participate in executable interactive systems.

---

# 65. Genie 3 relation

Google DeepMind describes Genie 3 as a real-time interactive world model capable of generating controllable environments, maintaining consistency for minutes, and supporting promptable world events.

Its published limitations include limited action space and interaction duration.

This is engineering evidence that generated world interaction is real but bounded.

---

# 66. Runnable-world contract gate

Before promoting a visual artifact to a WDC world, check:

$$
\boxed{
R_1,\ldots,R_7.
}
$$

A missing contract field is not repaired by higher visual quality.

---

# 67. R1 — Addressable State

The runtime can name/read/write or otherwise reference the current world state.

A video stream with no internal state access can fail this stronger WDC requirement depending on contract.

---

# 68. R2 — Transition Semantics

The runtime declares how world state evolves.

A next-frame generator can instantiate transition semantics if its state/action update is explicit enough for the contract.

---

# 69. R3 — Action / Intervention Interface

The world responds to permitted actions or interventions.

Passive generated video alone does not satisfy this.

---

# 70. R4 — Persistent or Replayable History

A runnable world should support persistent trajectory history or deterministic/stochastic replay semantics.

---

# 71. R5 — Observation / Evaluation Interface

The visual observer is one interface.

Worlds can have nonvisual query/evaluation interfaces too.

---

# 72. R6 — Bounded Resource Contract

Specify:

- compute;
- horizon;
- storage;
- network;
- provider budget;
- termination conditions.

---

# 73. R7 — Provenance / Termination Contract

Specify:

- world ID;
- parent;
- model versions;
- seeds;
- providers;
- fork history;
- evidence scope;
- archive/termination.

---

# 74. Visual provider as renderer

GVSS provider can implement:

$$
O_{\mathrm{vis}}.
$$

Example:

- world state contains scene graph;
- image model renders a visual observation.

Provider output is then a world observation.

---

# 75. Visual provider as world candidate generator

GVSS provider can also propose:

$$
I
$$

before any world exists.

Then a world-lift module must construct:

$$
\widehat W.
$$

These two uses must not be confused.

---

# 76. World-model provider

A provider can jointly maintain latent dynamics and images.

Then it may implement part of:

$$
(\mathcal D,\mathcal O).
$$

But WDC still needs identity, history, budget, provenance, and evidence scope.

---

# 77. Typed provider contract

For provider $\nu$:

$$
\boxed{
C_\nu
=
(
C_{\mathrm{render}},
C_{\mathrm{state}},
C_{\mathrm{dynamics}},
C_{\mathrm{action}},
C_{\mathrm{replay}},
C_{\mathrm{evidence}}
).
}
$$

Do not infer dynamics capability from image quality.

---

# 78. Visual realism no-go

A photorealistic provider can have poor:

- temporal consistency;
- object permanence;
- controllability;
- action semantics.

Photorealism is one coordinate.

---

# 79. Dynamic realism no-go

A low-fidelity symbolic simulator can have exact transition semantics and reproducibility.

Visual quality is not a monotone proxy for world validity.

---

# 80. World identity

Two lifted worlds from the same image must receive distinct IDs unless proven identical under the full world contract.

Same image does not authorize identity merge.

---

# 81. Lift provenance

Every lift should record:

```text
source_visual_artifact
visual_provider
world_lift_algorithm
world_contract
priors
hidden-state initialization
dynamics_model
seed
validation_probes
rejected_alternatives
```

---

# 82. Lift uncertainty

A world lift can preserve a set/distribution:

$$
\boxed{
P(W\mid I,\kappa).
}
$$

This is often more faithful than selecting one world immediately.

---

# 83. Branching lift

From one image:

$$
I
$$

instantiate:

$$
\boxed{
W_1,\ldots,W_m
}
$$

representing different hidden-state/dynamics hypotheses.

This connects directly to WDC branching.

---

# 84. Lift-then-fork versus fork-then-render

Two workflows:

### Lift then fork

$$
I
\to
W
\to
W_1,W_2.
$$

### Multiple lifts

$$
I
\to
W_1,W_2.
$$

They have different lineage semantics.

---

# 85. Shared visual prefix does not imply shared world prefix

Two worlds can share one rendered frame without sharing hidden-state history.

Therefore do not assign a shared WDC checkpoint solely from image equality.

---

# 86. VWDC01-N6 — Visual equality does not imply checkpoint equality

If:

$$
O(W_1)=O(W_2)
$$

but:

$$
X_1\neq X_2
$$

or histories differ:

$$
\mathcal H_1\neq\mathcal H_2,
$$

then they cannot be treated as the same checkpoint under a state/history-sensitive contract.

 $\square$

---

# 87. Checkpoint equality requirement

A shared checkpoint requires the declared checkpoint state/hashes/contracts to agree.

Visual hash equality is insufficient.

---

# 88. Evidence packet

A visual observation can enter a world evidence packet:

$$
\boxed{
E_W
=
(
WorldID,
Contract,
Observation,
ObserverID,
ActionHistory,
Evaluator,
Provenance
).
}
$$

---

# 89. Visual evidence about a world

If a world produces image $I$ under contract $\kappa$, the image is evidence about:

- that world observation;
- possibly hidden variables through a justified observation model.

It is not automatically evidence about reality.

---

# 90. VWDC01-N7 — Visually identical worlds can support different hidden claims

Let worlds:

$$
W_1,W_2
$$

render the same image at current time but have different hidden parameter:

$$
h(W_1)\neq h(W_2).
$$

The image alone cannot decide the hidden claim.

Thus visual agreement across worlds does not prove hidden-state agreement.

 $\square$

---

# 91. Cross-world image agreement

Many sibling worlds can render similar frames.

Their evidence can still be highly dependent because they share:

- parent checkpoint;
- visual provider;
- dynamics model;
- evaluator.

This inherits WDC-05 dependence rules.

---

# 92. Reality transport

To claim:

$$
q_R
$$

about reality from world observations, require:

$$
\boxed{
\mathcal T_{W\to R}.
}
$$

VWDC-01 does not weaken WDC's evidence boundary.

---

# 93. Reality image matching no-go

A simulated world rendering that resembles a real photograph does not by itself validate hidden simulation dynamics.

Image similarity is one observation match.

---

# 94. Visual twin versus live-tethered twin

A visual duplicate is not necessarily a digital twin.

A live-tethered twin requires explicit synchronization/evidence/state mapping.

---

# 95. Bridge runtime architecture

Suggested layers:

$$
\boxed{
\text{World State Plane}
}
$$

$$
\boxed{
\text{Visual Observation / Generation Plane}
}
$$

$$
\boxed{
\text{Lift / Validation Plane}
}
$$

$$
\boxed{
\text{Branch / Governor Plane}
}
$$

$$
\boxed{
\text{Evidence / Provenance Plane}.
}
$$

---

# 96. World State Plane

Contains:

- state;
- dynamics;
- actors;
- rules;
- history;
- checkpoints.

---

# 97. Visual Plane

Uses GVSS:

- providers;
- renderer;
- visual constraints;
- evaluator;
- routing;
- visual failure diagnosis.

---

# 98. Lift Plane

Maps visual candidates to world candidates and performs:

- contract validation;
- hidden-state initialization;
- dynamics selection;
- uncertainty tracking.

---

# 99. Branch Plane

Uses WDC:

- fork;
- replay;
- intervention;
- world selection;
- compute allocation.

---

# 100. Evidence Plane

Maintains:

- visual lineage;
- world lineage;
- bridge transforms;
- world evidence;
- reality transport boundaries.

---

# 101. Bridge state object

A combined runtime state can be:

$$
\boxed{
\mathsf{VW}_t
=
(
\mathcal W_t,
\mathcal V_t,
\mathcal L_t,
\mathcal E_t,
B_t,
\mathsf{Prov}_t
).
}
$$

---

# 102. GVSS substate

$$
\mathcal V_t
$$

contains:

- provider portfolio;
- task-conditioned router;
- visual constraint program;
- evaluators;
- visual deficit;
- provider uncertainty.

---

# 103. WDC substate

$$
\mathcal W_t
$$

contains:

- active worlds;
- checkpoints;
- branch graph;
- local times;
- world contracts;
- governor state.

---

# 104. Lift substate

$$
\mathcal L_t
$$

contains:

- candidate lifts;
- fiber uncertainty;
- liftability status;
- dynamics validation status.

---

# 105. Proposed lift status

```text
VISUAL_ONLY
RENDER_CONSISTENT
CONTRACT_VALID
DYNAMICS_TESTED
RUNNABLE
WORLD_EVIDENCE_VALID
REALITY_TRANSPORT_REVIEWED
```

---

# 106. Promotion rule

A visual artifact may be promoted to RUNNABLE only after:

$$
R_1,\ldots,R_7
$$

pass under $\kappa$.

---

# 107. No silent promotion

Do not infer:

```text
RUNNABLE=true
```

because:

- evaluator score is high;
- video is temporally smooth;
- provider calls it a "world model";
- image is photorealistic.

Worldness is contract based.

---

# 108. Generated interactive world systems

Interactive world-model systems can satisfy substantial subsets of the runnable contract.

Whether they satisfy the full WDC contract depends on:

- external state access;
- reproducibility;
- identity;
- checkpoint semantics;
- evidence/provenance.

VWDC treats these as contract questions, not branding questions.

---

# 109. Current systems are important precedents

Genie, GameNGen, DIAMOND, and Genie 3 demonstrate rapidly improving:

- interactive generation;
- action conditioning;
- temporal consistency;
- world-model use for agents.

They make the bridge practically relevant.

---

# 110. Current limitations remain relevant

Generated interactive worlds can still have:

- limited action spaces;
- finite interaction horizons;
- visual/physics inconsistencies;
- weak explicit state APIs.

These reinforce the need to separate visual interactivity from a full runtime contract.

---

# 111. Research program — world lifting

Future work:

1. single-frame lift;
2. multi-view lift;
3. action-probed lift;
4. history-conditioned lift;
5. latent-world ensemble lift;
6. contract-aware lift.

---

# 112. Research program — lift benchmark

Construct toy worlds where hidden state is known.

Give only:

- one image;
- multiple images;
- action histories.

Measure:

- state ambiguity;
- dynamics ambiguity;
- contract validity;
- lift posterior calibration.

---

# 113. Research program — visual lumpability benchmark

Generate world pairs sharing the same current observation.

Test whether:

$$
O(D_a(x))
=
O(D_a(x'))
$$

for actions.

This measures whether image state is a closed dynamics representation.

---

# 114. Research program — render/world mismatch

Create images that are:

- visually plausible;
- impossible under world contract.

Train validators to detect liftability rather than aesthetic quality.

---

# 115. Research program — provider role classification

For each GVSS provider, classify:

```text
renderer_only
image_generator
editor
scene_reconstructor
latent_world_model
runnable_backend
```

with evidence.

---

# 116. Research program — world lift uncertainty

Maintain multiple hypotheses rather than one reconstructed world.

Use WDC branching to run them in parallel.

---

# 117. What is classical / neighboring

VWDC-01 does not claim as inventions:

- observation functions;
- equivalence classes/fibers;
- injectivity and left inverses;
- task-sufficient statistics;
- POMDP belief states;
- lumpability/quotient dynamics;
- inverse rendering;
- neural scene reconstruction;
- latent-state world models;
- interactive generated environments.

---

# 118. Candidate VWDC-specific synthesis

Subject to broader literature audit, the bridge-specific synthesis is:

1. explicitly positioning GVSS visual states as observations/representations of WDC runnable worlds rather than world states themselves;
2. defining contract-relative visual liftability $\mathcal L_\kappa$ ;
3. making exact visual inversion, task-relative sufficiency, and dynamics closure separate gates;
4. applying the observation-fiber criterion to distinguish static frame state from runnable dynamics;
5. defining the bridge-compatible visual reachable set:
   $$
   \mathcal R_{\mathrm{GVSS}}\cap\mathcal L_\kappa;
   $$
6. defining render-consistent, contract-valid, dynamics-tested, and evidence-valid lift stages;
7. preserving visual lineage and world lineage as separate but linked provenance objects;
8. using WDC branching to represent multiple hidden-world hypotheses consistent with one visual state.

No strong novelty claim is made in v0.1.

---

# 119. What VWDC-01 proves

Under explicit hypotheses, VWDC-01 proves:

1. a global exact deterministic world lift requires visual-observer injectivity;
2. task-relative visual recoverability is equivalent to task constancy on observation fibers;
3. contract-relative liftability is exactly membership in the image of valid world states;
4. deterministic image-state dynamics exist exactly when next observations are constant on current observation fibers;
5. a static image cannot close world dynamics when hidden states in one visual fiber have different action-conditioned future observations;
6. enlarging the diagnostic/probe family can only refine observational equivalence;
7. world reachability projects into visual observation reachability;
8. visually generable states need not be reachable observations of any valid world;
9. zero render error does not imply world-contract validity;
10. visual equality does not imply checkpoint equality;
11. visual agreement does not identify hidden world claims;
12. the bridge-compatible visual reachable domain is the intersection of GVSS visual reachability and contract liftability.

---

# 120. What VWDC-01 does not prove

It does not prove:

- every image can be lifted to a runnable world;
- a unique world can be reconstructed from one image;
- current world models expose complete hidden state;
- a photorealistic interactive generator satisfies the WDC runnable contract;
- finite visual histories always identify world dynamics;
- visual dynamics are Markov;
- one visual metric defines world validity;
- a scene representation is a full runnable world;
- a world simulation is evidence about reality without a transport contract;
- GVSS and WDC should be merged into one theory.

---

# 121. Proposed VWDC-02

The next bridge paper should now absorb the original GVSS-11 composition problem:

$$
\boxed{
\textbf{
VWDC-02 — Compositional Visual–World Reachability Graphs
}
}
$$

Chinese:

**組合式視覺—世界可達圖：跨生成器轉換、世界提升、Fork 與缺陷傳遞**

Main questions:

1. What typed node/edge system connects visual artifacts and runnable worlds?
2. When can cross-provider composition reach beyond simple provider union?
3. How should visual-to-world lift edges be typed?
4. How do semantic/state/dynamics defects accumulate along paths?
5. What is the least-cost valid path to a target world/visual region?
6. How do world forks and visual edits interact in lineage?
7. When are path cycles useful versus pure debt?
8. How should evidence provenance move along mixed visual/world paths?

---

# 122. References

1. Jake Bruce et al., **Genie: Generative Interactive Environments**, arXiv:2402.15391, 2024.
2. Dani Valevski, Yaniv Leviathan, Moab Arar, Shlomi Fruchter, **Diffusion Models Are Real-Time Game Engines**, arXiv:2408.14837, 2024.
3. Eloi Alonso et al., **Diffusion for World Modeling: Visual Details Matter in Atari**, arXiv:2405.12399, 2024.
4. Google DeepMind, **Genie 3: A New Frontier for World Models**, 2025 research release.
5. Ben Mildenhall et al., **NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis**, arXiv:2003.08934, 2020.
6. Alex Yu et al., **pixelNeRF: Neural Radiance Fields from One or Few Images**, arXiv:2012.02190, 2020.
7. Soumyadip Sengupta et al., **Neural Inverse Rendering of an Indoor Scene from a Single Image**, arXiv:1901.02453, 2019.
8. Aleksandr Ermolov, Nicu Sebe, **Latent World Models For Intrinsically Motivated Exploration**, arXiv:2010.02302, 2020.
9. GVSS-01 through GVSS-10, internal series artifacts, 2026.
10. WDC-01 through WDC-08 and WDC Runtime Whitepaper, internal series artifacts, 2026.
11. RRT-20, **Reflexive Representation Theory: Unified Closure, Meta-Theorems, Limits, and Research Program**, internal series artifact, 2026.

---

# 123. Conclusion

GVSS provides a formal space of visual states and a navigation system over those states.

WDC provides executable worlds with state, dynamics, interventions, history, identity, budget, and evidence governance.

The bridge is an observation map:

$$
\boxed{
O_{\mathrm{vis}}:
\mathcal X_W
\to
\Omega_\Sigma.
}
$$

But rendering is generally many-to-one.

Therefore:

$$
\boxed{
L\circ O_{\mathrm{vis}}
\neq
\operatorname{Id}_{\mathcal X_W}
}
$$

in general.

A rendered frame identifies an observation fiber, not necessarily one world.

Even perfect render reconstruction does not establish valid hidden dynamics.

Exact deterministic image-state dynamics exist only when:

$$
\boxed{
O(x)=O(x')
\Longrightarrow
O(D_a(x))
=
O(D_a(x'))
}
$$

for every action.

When this fails, latent state or history is necessary.

The visually reachable states relevant to WDC are not all of GVSS reachability, but:

$$
\boxed{
\mathcal R_{\mathrm{bridge}}
=
\mathcal R_{\mathrm{GVSS}}
\cap
\mathcal L_\kappa.
}
$$

And a visual artifact becomes a runnable world only after passing the WDC runnable contract.

The canonical VWDC-01 principle is:

$$
\boxed{
\textbf{
A picture can describe a world without containing the world.
A generated frame can propose a world without instantiating its hidden dynamics.
A runnable world begins only when observation is joined by explicit state, transition, intervention, history, identity, resource, and provenance semantics.
}
}
$$

This establishes the formal bridge from Global Visual Space to Branching World Computation.

---

# Canonical-source policy

This file is the canonical UTF-8 source artifact.

- Canonical inline mathematics uses ` $...$ `.
- Canonical display mathematics uses `$$...$$`.
- No Unicode mathematical-symbol conversion is used as source normalization.
- No `unicode_escape` round trip is used.
- Backslashes and delimiters are preserved literally.
- Validation is required before release.
- This paper does not reopen RRT numbering and does not rename GVSS or WDC.
