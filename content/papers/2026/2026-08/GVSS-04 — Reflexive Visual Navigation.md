# GVSS-04 — Reflexive Visual Navigation
## 反身視覺空間導航：自適應表示、閉環約束搜尋與可達性感知生成

**Series:** Global Visual Space & Generative Navigation — Paper 04  
**Bridge:** GVSS × Reflexive Representation Theory (RRT)  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal bridge paper. The abstract state-space, reachability, action-separation, vector-defect, protected-regression, representation-chart, evaluator-gating, lineage, and Pareto statements are proved under the explicit hypotheses below. Closed-loop text-to-image refinement, diffusion guidance/control, multimodal verification, test-time search, and agentic image generation are established neighboring research directions and are not claimed as GVSS inventions. No strong novelty claim is made.

**Keywords:** Global Visual State Space, reflexive visual navigation, closed-loop generation, constraint compiler, generative reachability, test-time refinement, visual verifier, diffusion control, agentic image generation, representation reflexivity, AI art direction

---

# Abstract

The first three papers of the Global Visual Space & Generative Navigation series established three different objects.

Paper 01 defines the complete finite raster state space

$$
\boxed{
\Omega_\Sigma
}
$$

for a fixed digital image specification

$$
\Sigma=(W,H,C,b).
$$

Paper 02 interprets visual generation as constrained navigation:

$$
\boxed{
\text{Intent}
\to
\text{Constraint Program}
\to
\text{Search Policy}
\to
I.
}
$$

Paper 03 separates complete representability from practical generative reachability and introduces an operational reachable domain

$$
\boxed{
\mathcal R_G(B)
}
$$

under bounded search resources.

GVSS-04 adds the missing fourth layer:

> **How should an intelligent controller change its own visual representation, constraint program, generator binding, workflow, observer, verifier, and search budget in response to the images that its current regime produces?**

The central object is a **visual generation regime**

$$
\boxed{
r_t
=
(
G_t,
\Gamma_t,
C_t,
\Lambda_t,
P_t,
\Pi_t,
O_t,
E_t,
B_t,
\mathsf{Prov}_t
),
}
$$

where:

- $G_t$ is the bound generator/model stack;
- $\Gamma_t$ is the current intent compiler;
- $C_t$ is the compiled constraint program;
- $\Lambda_t$ contains constraint weights;
- $P_t$ contains references, adapters, LoRAs, controls, style providers, and related bindings;
- $\Pi_t$ is the search/sampling/refinement policy;
- $O_t$ is the visual observer/evaluation interface;
- $E_t$ is the verifier/evaluator configuration;
- $B_t$ is the remaining resource budget;
- $\mathsf{Prov}_t$ is the lineage/provenance state.

Generation produces

$$
\boxed{
I_t
\sim
\mathcal G(r_t).
}
$$

Evaluation returns the existing eight-axis runtime vector

$$
\boxed{
M_t
=
(
P_t^{\mathrm{score}},
Q_t,
A_t,
S_t,
D_t,
H_t,
C_t^{\mathrm{score}},
R_t
)
\in
[0,100]^8,
}
$$

corresponding to:

- Prompt / Constraint Adherence;
- Technical Image Quality;
- Human Preference / Aesthetic Proxy;
- Style Consistency;
- Diversity / Coverage;
- Anti-Homogenization;
- Character / Subject Consistency;
- Reference / Control Consistency.

Given target thresholds

$$
\tau\in[0,100]^8,
$$

define the deficit vector

$$
\boxed{
e_{t,i}
=
[
\tau_i-M_{t,i}
]_+.
}
$$

A reflexive visual controller chooses an action

$$
\boxed{
a_t
=
\pi_{\mathrm{RVN}}
(
r_t,
M_t,
e_t,
H_t
),
}
$$

from an action vocabulary containing, for example,

$$
\boxed{
\{
\text{ACCEPT},
\text{RESAMPLE},
\text{RECOMPILE},
\text{REBIND},
\text{REPAIR},
\text{SWITCH\_BACKEND},
\text{HUMAN\_REVIEW},
\text{STOP}
\}.
}
$$

The regime then updates:

$$
\boxed{
r_{t+1}
=
\Psi(
r_t,
a_t,
M_t,
e_t
).
}
$$

This is the GVSS specialization of representation reflexivity.

The first structural theorem separates three commonly conflated forms of refinement.

Let

$$
\mathcal R(G,P)
$$

denote the base reachable set of a fixed generator/provider binding.

Let

$$
\mathcal A(C)
$$

denote the accepted visual set defined by a constraint program.

Define the effective target domain

$$
\boxed{
\mathcal T(G,P,C)
=
\mathcal R(G,P)
\cap
\mathcal A(C).
}
$$

Then, under fixed binding semantics:

1. **RESAMPLE** changes the sampled trajectory but leaves both $\mathcal R(G,P)$ and $\mathcal A(C)$ unchanged;
2. **RECOMPILE** can change $\mathcal A(C)$ while leaving the base generator reachable set $\mathcal R(G,P)$ unchanged;
3. **REBIND** can change $\mathcal R(G,P)$ itself.

Thus:

$$
\boxed{
\text{sampling failure}
\neq
\text{constraint-representation failure}
\neq
\text{generator-reachability failure}.
}
$$

This is the central diagnostic separation of GVSS-04.

Practical reachability is made policy dependent.

For controller/search policy $\Pi$ and budget $B$, define

$$
\boxed{
\mathcal R_{G,P,\Pi}(B)
}
$$

as the set of images that can be produced or reached by the declared policy within the resource budget.

If:

$$
B_1\le B_2
$$

and unused budget may simply be discarded, then

$$
\boxed{
\mathcal R_{G,P,\Pi}(B_1)
\subseteq
\mathcal R_{G,P,\Pi}(B_2).
}
$$

If policy $\Pi_2$ can simulate every bounded execution of $\Pi_1$, then

$$
\boxed{
\mathcal R_{G,P,\Pi_1}(B)
\subseteq
\mathcal R_{G,P,\Pi_2}(B).
}
$$

Therefore practical reachable visual space is not a property of the foundation generator alone.

It depends on:

$$
\boxed{
\text{generator}
+
\text{provider binding}
+
\text{search policy}
+
\text{budget}.
}
$$

The closed-loop error geometry is represented by a vector recurrence

$$
\boxed{
e_{t+1}
\preceq
A_t e_t
+
\varepsilon_t,
}
$$

where $A_t$ is a nonnegative action-dependent transfer matrix and $\varepsilon_t$ is newly injected model/compiler/evaluator defect.

Unrolling yields

$$
\boxed{
e_n
\preceq
A_{n-1:0}e_0
+
\sum_{j=0}^{n-1}
A_{n-1:j+1}\varepsilon_j,
}
$$

with the empty matrix product interpreted as identity.

Thus a refinement action can reduce one deficit while transporting or amplifying another.

This gives a formal version of the existing runtime rule that one metric improvement must not silently destroy protected dimensions.

If accepted refinement steps satisfy

$$
\boxed{
M_{t+1,i}
\ge
M_{t,i}
-
\delta_{t,i}
}
$$

for a protected metric coordinate $i$, then after $n$ accepted refinement steps

$$
\boxed{
M_{n,i}
\ge
M_{0,i}
-
\sum_{t=0}^{n-1}
\delta_{t,i}.
}
$$

The paper also formalizes the role of the Global Style Map.

Any finite-dimensional style map is a representation chart

$$
\boxed{
\phi:
\Omega_\Sigma
\to
\mathbb R^d.
}
$$

A Euclidean style distance

$$
\|\phi(I)-\phi(J)\|_2
$$

is not automatically intrinsic.

For an invertible but non-isometric coordinate change

$$
T,
$$

generally

$$
\boxed{
\|
T\phi(I)-T\phi(J)
\|_2
\neq
\|
\phi(I)-\phi(J)
\|_2.
}
$$

Hence:

$$
\boxed{
\text{style-coordinate distance}
\not\Rightarrow
\text{intrinsic visual distance}.
}
$$

Style coordinates are navigation representations, not declarations of the unique geometry of visual meaning.

Evaluation itself also changes practical reachability.

For verifier $E$ and threshold $\tau_E$, define

$$
\boxed{
\mathcal A_E(\tau_E)
=
\{
I:
E(I)\ge\tau_E
\}.
}
$$

The verifier-gated reachable set is

$$
\boxed{
\mathcal R^{\mathrm{acc}}_{G,P,\Pi,E}(B,\tau_E)
=
\mathcal R_{G,P,\Pi}(B)
\cap
\mathcal A_E(\tau_E).
}
$$

If

$$
\tau_1\le\tau_2,
$$

then:

$$
\boxed{
\mathcal R^{\mathrm{acc}}(B,\tau_2)
\subseteq
\mathcal R^{\mathrm{acc}}(B,\tau_1).
}
$$

A stricter verifier reduces accepted reachability.

But a stricter or more strongly optimized verifier does not necessarily improve true human intent if the evaluator is misaligned.

A two-image counterexample is sufficient:

$$
U(I_1)=1,
\qquad
U(I_2)=0,
$$

but proxy evaluator

$$
E(I_1)=0,
\qquad
E(I_2)=1.
$$

Optimizing $E$ selects the worse image according to true utility $U$.

Therefore:

$$
\boxed{
\text{closed-loop optimization}
\not\Rightarrow
\text{true-intent improvement}.
}
$$

The loop is only as valid as the representation, evaluator, and protected constraints used to drive it.

GVSS-04 consequently defines the **Visual Reflexive Pareto Frontier** over a vector such as

$$
\boxed{
\mathbf C_{\mathrm{RVN}}
=
(
e,
C_{\mathrm{compute}},
C_{\mathrm{verify}},
C_{\mathrm{switch}},
D_{\mathrm{homog}},
D_{\mathrm{provenance}}
).
}
$$

The objective is not one universal image score.

It is a nondominated frontier over visual deficit, compute, verification, switching, homogenization, and lineage debt.

The central conclusion is:

$$
\boxed{
\textbf{
GVSS gives the geometry of possible and reachable visual states.
Reflexive Visual Navigation gives the closed-loop law by which an intelligent system changes
the representation and search regime used to navigate that geometry.
}
}
$$

---

# 1. Position in the series

Paper 01 asks:

> Where can digital images exist?

Answer:

$$
I\in\Omega_\Sigma.
$$

Paper 02 asks:

> How can desired visual regions be specified?

Answer:

$$
\text{constraints define an effective target domain}.
$$

Paper 03 asks:

> Which regions can a generator practically reach?

Answer:

$$
\mathcal R_G(B).
$$

Paper 04 asks:

> How can an intelligent search system alter its own navigation regime when generation fails?

This introduces reflexivity into GVSS.

---

# 2. Classical and current neighboring work

Modern text-to-image generation already supports many forms of conditional control.

Latent Diffusion Models use cross-attention and latent-space generation to support flexible conditioning.

Classifier-Free Guidance changes the tradeoff between fidelity and diversity by combining conditional and unconditional scores.

ControlNet introduces additional structural conditioning such as edges, depth, segmentation, and pose.

Prompt-to-Prompt manipulates cross-attention to control semantic edits while preserving image structure.

Therefore GVSS-04 does not claim conditional visual control as new.

---

# 3. Current closed-loop generation precedent

By 2025--2026, visual generation research contains explicit closed-loop and test-time refinement systems.

Examples include:

- test-time prompt refinement using an MLLM to inspect generated images and rewrite prompts;
- iterative image-generation loops using a VLM critic;
- VisionDirector-style structured-goal extraction, semantic verification, staged editing, and rollback;
- Agentic Retoucher-style perception-reasoning-action retouching;
- agentic image generators that integrate planning, search, memory, and feedback;
- verifier-guided test-time search over diffusion noise candidates.

Thus the contribution of GVSS-04 is not the existence of a generation/evaluation loop.

The intended contribution is the **state-space and regime-separation synthesis**:

$$
\boxed{
\text{visual state space}
+
\text{constraint domain}
+
\text{reachable domain}
+
\text{representation-reflexive controller}.
}
$$

---

# 4. Digital image state space

Let fixed raster specification be

$$
\boxed{
\Sigma
=
(W,H,C,b).
}
$$

Let:

$$
Q_b
=
\{0,\ldots,2^b-1\}.
$$

Then:

$$
\boxed{
\Omega_\Sigma
=
Q_b^{WHC}.
}
$$

Its cardinality is:

$$
\boxed{
|\Omega_\Sigma|
=
2^{bWHC}.
}
$$

This is inherited from GVSS Paper 01.

---

# 5. Structured visual domain

The complete raster space contains:

- natural images;
- artificial images;
- meaningful images;
- noise-like states;
- invalid project assets;
- perceptually redundant states.

Let:

$$
\mathcal M_{\mathrm{vis}}
\subseteq
\Omega_\Sigma
$$

denote a declared structured/meaningful domain.

RRT does not make this subset intrinsic.

Its definition depends on the observer and task.

---

# 6. Generator binding

## Definition GVSS04-D1

A **generator binding** is

$$
\boxed{
\mathsf G
=
(
G,
P
),
}
$$

where $G$ identifies the base generator and $P$ identifies provider-side control assets such as:

- model profile;
- LoRA;
- adapter;
- reference;
- ControlNet;
- image-to-image source;
- backend-specific workflow;
- sampler family.

The pair determines a base generation regime.

---

# 7. Base reachable set

## Definition GVSS04-D2

Let:

$$
\boxed{
\mathcal R(\mathsf G)
\subseteq
\Omega_\Sigma
}
$$

be the declared base reachable set of generator binding $\mathsf G$ under the allowed finite-precision control surface.

This can be interpreted as:

- exact algorithmic reachability;
- positive-probability support;
- effective support above a probability threshold;
- empirical bounded reachable set.

The interpretation must be stated.

---

# 8. Constraint program

Let human intent be:

$$
\mathcal I_h.
$$

The compiler produces:

$$
\boxed{
\Gamma(
\mathcal I_h
)
=
(C,\Lambda),
}
$$

where:

- $C$ is a structured constraint program;
- $\Lambda$ contains weights/priorities.

---

# 9. Accepted constraint set

## Definition GVSS04-D3

For compiled constraint program $C$, define:

$$
\boxed{
\mathcal A(C)
=
\{
I\in\Omega_\Sigma:
I
\text{ satisfies the declared hard acceptance semantics of }C
\}.
}
$$

Soft constraints can instead contribute an energy/reward.

The hard-set notation is used for structural theorems.

---

# 10. Effective target domain

## Definition GVSS04-D4

$$
\boxed{
\mathcal T(
\mathsf G,
C
)
=
\mathcal R(\mathsf G)
\cap
\mathcal A(C).
}
$$

A target can fail because:

1. $\mathcal A(C)$ is empty/internally inconsistent;
2. $\mathcal A(C)$ is nonempty but does not intersect $\mathcal R(\mathsf G)$ ;
3. the intersection is nonempty but the search policy fails to find it within budget;
4. the compiler does not represent the human intent correctly;
5. the evaluator rejects valid target images or accepts invalid ones.

These failures require different actions.

---

# 11. Search policy

## Definition GVSS04-D5

A search policy

$$
\boxed{
\Pi
}
$$

maps history, current constraints, bound generator, and remaining budget into generation/refinement actions.

The history can include:

- previous seeds;
- previous images;
- scores;
- diagnoses;
- failed constraints;
- provider switches;
- human feedback.

---

# 12. Bounded practical reachability

## Definition GVSS04-D6

Let:

$$
\boxed{
\mathcal R_{\mathsf G,\Pi}(B)
}
$$

be the set of images that can be produced within budget $B$ by executions permitted under policy $\Pi$ and generator binding $\mathsf G$.

The budget can include:

$$
\boxed{
B
=
(
N_{\mathrm{retry}},
T_{\mathrm{GPU}},
C_{\mathrm{cloud}},
N_{\mathrm{switch}},
N_{\mathrm{human}}
).
}
$$

---

# 13. GVSS04-T1 — Budget monotonicity

## Theorem GVSS04-T1

Suppose the budget feasibility relation is nested and the policy may leave unused resources unspent.

If:

$$
\boxed{
B_1
\preceq
B_2,
}
$$

then:

$$
\boxed{
\mathcal R_{\mathsf G,\Pi}(B_1)
\subseteq
\mathcal R_{\mathsf G,\Pi}(B_2).
}
$$

### Proof

Every execution feasible under $B_1$ remains feasible under $B_2$.

Therefore every image reachable with $B_1$ remains reachable with $B_2$.

 $\square$

This is a resource-monotonicity statement.

It does not say extra budget is always useful.

---

# 14. Policy simulation order

## Definition GVSS04-D7

Write:

$$
\boxed{
\Pi_1
\preceq_B
\Pi_2
}
$$

if policy $\Pi_2$ can reproduce every execution trajectory permitted by $\Pi_1$ under budget $B$.

---

# 15. GVSS04-T2 — Policy reachability dominance

## Theorem GVSS04-T2

If:

$$
\Pi_1
\preceq_B
\Pi_2,
$$

then:

$$
\boxed{
\mathcal R_{\mathsf G,\Pi_1}(B)
\subseteq
\mathcal R_{\mathsf G,\Pi_2}(B).
}
$$

### Proof

Every $\Pi_1$ execution is also a $\Pi_2$ execution by simulation.

 $\square$

Thus **Search Intelligence** has a mathematically distinct role from model weights.

---

# 16. Practical reachable domain

RRT/GVSS therefore recommends:

$$
\boxed{
\mathcal R_{\mathrm{practical}}
=
\mathcal R(
\text{model},
\text{binding},
\text{policy},
\text{budget}
).
}
$$

Do not assign practical reachability to the base model alone when orchestration/search differs.

---

# 17. Visual generation regime

## Definition GVSS04-D8

The complete visual regime is:

$$
\boxed{
r_t
=
(
\mathsf G_t,
\Gamma_t,
C_t,
\Lambda_t,
\Pi_t,
O_t,
E_t,
B_t,
\mathsf{Prov}_t
).
}
$$

This state is intentionally larger than a prompt.

---

# 18. Generation step

$$
\boxed{
I_t
\sim
K_{r_t}.
}
$$

Here:

$$
K_{r_t}
$$

is the stochastic generation kernel induced by the bound workflow.

For deterministic seed/workflow mappings, $K_{r_t}$ can be a Dirac measure conditional on seed.

---

# 19. Observer step

The observer produces:

$$
\boxed{
Y_t
=
O_t(
I_t,
C_t,
\mathsf{Prov}_t
).
}
$$

A report can include:

- metric vector;
- hard-gate results;
- failure labels;
- region masks;
- natural-language critique;
- human preference;
- reference comparison.

---

# 20. Runtime metric vector

The existing runtime uses:

$$
\boxed{
M_t
=
(P,Q,A,S,D,H,C,R).
}
$$

To avoid collision with provider set $P_t$, the paper will write:

$$
\boxed{
M_t
=
(
m_P,
m_Q,
m_A,
m_S,
m_D,
m_H,
m_C,
m_R
).
}
$$

---

# 21. Deficit vector

Given desired thresholds:

$$
\tau_i,
$$

define:

$$
\boxed{
e_{t,i}
=
[
\tau_i-m_{t,i}
]_+.
}
$$

The vector:

$$
\boxed{
e_t
}
$$

is not claimed to measure all visual failure.

It measures failure under the declared evaluator coordinates.

---

# 22. Hard gates

Some conditions are not scalar preferences.

Let:

$$
\boxed{
g_t
\in
\{0,1\}^k
}
$$

record hard-gate validity.

Examples:

- prohibited artifact;
- missing mandatory subject;
- wrong image dimensions;
- project identity violation;
- impossible reference mismatch.

A high composite score cannot override a failed hard gate unless the policy explicitly permits it.

---

# 23. Reflexive visual controller

## Definition GVSS04-D9

$$
\boxed{
a_t
=
\pi_{\mathrm{RVN}}
(
r_t,
M_t,
g_t,
e_t,
H_t
).
}
$$

The action changes zero or more coordinates of $r_t$.

---

# 24. Canonical action vocabulary

The bridge adopts the existing runtime vocabulary:

$$
\boxed{
\begin{aligned}
\mathcal A_{\mathrm{RVN}}
=
\{
&\text{ACCEPT},
\text{RESAMPLE},
\text{RECOMPILE},
\text{REBIND},
\\
&\text{REPAIR},
\text{SWITCH\_BACKEND},
\text{HUMAN\_REVIEW},
\text{STOP}
\}.
\end{aligned}
}
$$

Not every backend must support every action.

---

# 25. RESAMPLE semantics

RESAMPLE keeps:

- generator binding;
- compiled constraints;
- provider set;
- evaluator regime;

fixed, while changing sampling state such as:

- seed;
- noise;
- stochastic branch;
- candidate multiplicity.

This is **trajectory adaptation inside one regime**.

---

# 26. RECOMPILE semantics

RECOMPILE changes:

$$
\boxed{
(\Gamma,C,\Lambda)
}
$$

while keeping generator/provider binding fixed.

It is used when:

> the current representation of human intent is suspected to be wrong or incomplete.

This is **constraint-representation adaptation**.

---

# 27. REBIND semantics

REBIND changes:

$$
\boxed{
\mathsf G=(G,P).
}
$$

Examples:

- model checkpoint;
- LoRA;
- adapter;
- ControlNet;
- reference strategy;
- model profile;
- provider combination.

This can change the generator's reachable visual domain.

---

# 28. REPAIR semantics

REPAIR preserves selected global content while applying a local or structured image edit.

It can be modeled as an image-conditioned transition kernel:

$$
\boxed{
K_{\mathrm{repair}}
(
I_{t+1}
\mid
I_t,
C_t,
r_t
).
}
$$

---

# 29. SWITCH_BACKEND semantics

SWITCH_BACKEND changes execution mechanism/provider.

This may change:

- model family;
- control vocabulary;
- sampler;
- resolution constraints;
- cost;
- verifier interface.

It is a strong regime change.

---

# 30. HUMAN_REVIEW semantics

HUMAN_REVIEW introduces an external observer:

$$
\boxed{
O_t
\to
(
O_t,
O_{\mathrm{human}}
).
}
$$

This can refine the joint observation but costs human attention/time.

It does not guarantee correctness.

---

# 31. GVSS04-T3 — Action-level reachability separation

## Theorem GVSS04-T3

Let current generator binding be $\mathsf G$, constraint program be $C$, and target domain:

$$
\mathcal T(\mathsf G,C)
=
\mathcal R(\mathsf G)
\cap
\mathcal A(C).
$$

Under the canonical action semantics:

### RESAMPLE

If $\mathsf G$ and $C$ remain fixed,

$$
\boxed{
\mathcal T_{\mathrm{after}}
=
\mathcal T_{\mathrm{before}}.
}
$$

Only the sampled trajectory/candidate changes.

### RECOMPILE

If $\mathsf G$ remains fixed while:

$$
C\to C',
$$

then:

$$
\boxed{
\mathcal R(\mathsf G)
\text{ is unchanged},
}
$$

while:

$$
\boxed{
\mathcal T
\to
\mathcal R(\mathsf G)
\cap
\mathcal A(C').
}
$$

### REBIND

If:

$$
\mathsf G\to\mathsf G',
$$

then:

$$
\boxed{
\mathcal R(\mathsf G')
}
$$

may differ from:

$$
\boxed{
\mathcal R(\mathsf G).
}
$$

### Proof

Each conclusion follows directly from which arguments of $\mathcal T(\mathsf G,C)$ are changed by the declared action.

 $\square$

---

# 32. Diagnostic consequence

A system should not use REBIND merely because one seed failed.

Likewise, repeated RESAMPLE cannot repair a compiler that consistently represents the wrong intent.

This motivates action escalation.

---

# 33. Failure ladder

GVSS-04 recommends a first-pass hierarchy:

$$
\boxed{
\begin{aligned}
F_0 &: \text{candidate / sampling failure},\\
F_1 &: \text{constraint contradiction},\\
F_2 &: \text{intent compilation failure},\\
F_3 &: \text{search-policy failure},\\
F_4 &: \text{generator reachability failure},\\
F_5 &: \text{evaluator / observer failure},\\
F_6 &: \text{human-intent ambiguity}.
\end{aligned}
}
$$

This extends but does not overwrite the failure classes already developed in Paper 02/runtime documents.

---

# 34. Failure escalation rule

Do not escalate from:

$$
\boxed{
\text{sample failure}
}
$$

to:

$$
\boxed{
\text{generator failure}
}
$$

without evidence that the current search policy has exhausted an appropriate bounded search region.

Do not escalate from:

$$
\boxed{
\text{generator failure}
}
$$

to:

$$
\boxed{
\text{visual representation/language failure}
}
$$

without a broader reachability certificate.

This is the GVSS specialization of RRT failure escalation.

---

# 35. Vector defect model

The runtime has multiple quality coordinates.

Therefore scalar error is too coarse.

Let:

$$
\boxed{
e_t
\in
\mathbb R_+^d.
}
$$

---

# 36. Action-dependent transfer matrix

For action $a_t$, define nonnegative matrix:

$$
\boxed{
A_t
=
A(
a_t,
r_t
)
\in
\mathbb R_+^{d\times d}.
}
$$

The matrix describes how previous deficit coordinates survive or cross-couple after the action.

---

# 37. Defect injection

Let:

$$
\boxed{
\varepsilon_t
\in
\mathbb R_+^d
}
$$

represent new defect caused by:

- model stochasticity;
- prompt/compiler error;
- edit artifacts;
- reference drift;
- evaluator instability;
- provider mismatch.

---

# 38. GVSS04-T4 — Vector visual-defect recursion

## Theorem GVSS04-T4

Suppose:

$$
\boxed{
e_{t+1}
\preceq
A_t e_t
+
\varepsilon_t
}
$$

componentwise, with $A_t$ nonnegative.

Then:

$$
\boxed{
e_n
\preceq
A_{n-1}\cdots A_0e_0
+
\sum_{j=0}^{n-1}
A_{n-1}\cdots A_{j+1}
\varepsilon_j,
}
$$

where the empty product is identity.

### Proof

Induction using nonnegativity of all transfer matrices.

 $\square$

---

# 39. Interpretation

An action can improve one coordinate while amplifying another.

Example:

- stronger style binding may reduce style deficit;
- but can increase homogenization;
- strong reference control may increase identity consistency;
- but reduce diversity;
- aggressive local repair can improve anatomy;
- but alter texture/style.

This is why one composite score is insufficient.

---

# 40. Protected metric coordinates

The existing runtime gives special protection to:

- Prompt;
- Style;
- Character;
- Reference.

Let:

$$
\boxed{
\mathcal P_{\mathrm{metric}}
}
$$

be the protected index set.

---

# 41. GVSS04-T5 — Cumulative protected-regression bound

## Theorem GVSS04-T5

Suppose every accepted refinement satisfies, for protected coordinate $i$:

$$
\boxed{
M_{t+1,i}
\ge
M_{t,i}
-
\delta_{t,i}.
}
$$

Then after $n$ accepted steps:

$$
\boxed{
M_{n,i}
\ge
M_{0,i}
-
\sum_{t=0}^{n-1}
\delta_{t,i}.
}
$$

### Proof

Sum the one-step inequalities telescopically.

 $\square$

The theorem does not guarantee improvement.

It only bounds accepted cumulative regression.

---

# 42. Monotonic improvement is too strong

Requiring every metric to increase at every step can make useful tradeoffs impossible.

The runtime therefore should combine:

- hard regression bounds;
- Pareto acceptance;
- budget;
- protected coordinates.

---

# 43. Visual Reflexive Pareto Frontier

## Definition GVSS04-D10

Define visual regime cost vector:

$$
\boxed{
\mathbf C_{\mathrm{RVN}}(r)
=
(
e,
C_{\mathrm{compute}},
C_{\mathrm{verify}},
C_{\mathrm{switch}},
D_{\mathrm{homog}},
D_{\mathrm{lineage}}
).
}
$$

The exact coordinates are application dependent.

The **Visual Reflexive Pareto Frontier** is the nondominated regime/action set.

---

# 44. GVSS04-T6 — Pareto necessity

## Theorem GVSS04-T6

Every optimum of a scalar objective strictly increasing in all declared cost/deficit coordinates lies on the Visual Reflexive Pareto Frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 45. Test-time compute as navigation budget

Recent text-to-image work uses test-time compute through:

- multiple noise candidates;
- verifiers;
- iterative correction;
- edit loops;
- prompt refinement.

GVSS interprets this compute as a larger bounded navigation budget.

---

# 46. Candidate-parallel search

One policy can allocate budget to parallel candidates:

$$
\boxed{
I_1,\ldots,I_k
\sim
K_r.
}
$$

A verifier selects one.

This increases search breadth.

---

# 47. Iterative search

Another policy uses:

$$
I_0
\to
\text{critic}
\to
I_1
\to
\text{critic}
\to
\cdots.
$$

This changes search depth and conditions future actions on past results.

Recent work shows that iterative refinement can outperform compute-matched parallel sampling on some compositional benchmarks.

GVSS-04 treats both as different search policies on the same visual-state problem.

---

# 48. Policy-dependent practical reachability

Parallel sampling and iterative refinement can expose different bounded reachable regions.

Thus:

$$
\boxed{
\mathcal R_{G,\Pi_{\mathrm{parallel}}}(B)
}
$$

and:

$$
\boxed{
\mathcal R_{G,\Pi_{\mathrm{iter}}}(B)
}
$$

need not coincide.

No universal inclusion is claimed.

---

# 49. GVSS04-N1 — Same model does not imply same practical reachable set

Two systems can use the same foundation model $G$ but different:

- prompt compilers;
- control providers;
- verifiers;
- search policies;
- retry budgets.

Then their practical reachable sets can differ.

This follows from the definition of:

$$
\mathcal R_{\mathsf G,\Pi}(B).
$$

---

# 50. Intent compiler as representation

The human does not provide a pixel address.

The compiler constructs a lower-dimensional representation of intent.

Define:

$$
\boxed{
\Gamma_t:
\mathcal I_h
\to
(C_t,\Lambda_t,P_t,\Pi_t).
}
$$

This is more than prompt rewriting.

It can choose:

- constraints;
- weights;
- references;
- providers;
- control models;
- workflow.

---

# 51. Intent representation defect

Suppose a declared semantic comparison space for intent is available.

Let:

$$
\widehat{\mathcal I}(C_t)
$$

be the intent reconstructed from compiled constraints.

Define:

$$
\boxed{
d_{\mathrm{intent},t}
=
d_\mathcal I
(
\mathcal I_h,
\widehat{\mathcal I}(C_t)
).
}
$$

This is only meaningful after a metric/observer on intent has been declared.

---

# 52. Recompile trigger

RECOMPILE is appropriate when evidence suggests:

$$
\boxed{
d_{\mathrm{intent},t}
}
$$

or prompt-adherence deficit is high while base generator capability is not yet implicated.

The system should not interpret every low image score as a model-capability failure.

---

# 53. Generator reachability suspicion

Repeated failure can justify REBIND only under a declared bounded-search policy.

A practical heuristic is:

- prompt/constraint representation stable;
- evaluator stable;
- multiple diverse trajectories tried;
- protected metrics remain persistently below threshold.

This remains an empirical diagnostic, not a mathematical impossibility proof.

---

# 54. Reachability proof versus reachability suspicion

Paper 03 distinguishes operational reachability from ideal support.

GVSS-04 adds another distinction:

$$
\boxed{
\text{reachability suspicion}
\neq
\text{reachability proof}.
}
$$

Most real image systems can only estimate practical reachability.

---

# 55. Style map as a chart

Let:

$$
\boxed{
\phi:
\Omega_\Sigma
\to
\mathbb R^d.
}
$$

The Global Artist Keyword Style Map can be viewed as an empirical chart in which artists/styles are indexed by coordinates or feature descriptions.

---

# 56. GVSS04-N2 — Style chart is not the whole visual space

A finite-dimensional style map does not replace:

$$
\Omega_\Sigma.
$$

It is a low-dimensional representation chosen for:

- retrieval;
- navigation;
- interpolation;
- prompt compilation;
- style diagnosis.

The map can be useful even if it is highly non-injective.

---

# 57. GVSS04-T7 — Coordinate-distance non-intrinsicness

## Theorem GVSS04-T7

Let:

$$
x=\phi(I),
\qquad
y=\phi(J).
$$

Let $T$ be invertible but not an Euclidean isometry.

Then there exist $x,y$ such that:

$$
\boxed{
\|Tx-Ty\|_2
\neq
\|x-y\|_2.
}
$$

### Proof

Because $T$ is not an isometry, by definition there exists vector $v$ with:

$$
\|Tv\|_2
\neq
\|v\|_2.
$$

Choose $x-y=v$.

 $\square$

Therefore raw Euclidean style distance is representation dependent unless an invariance/normalization rule is supplied.

---

# 58. Example

In two style coordinates let:

$$
T
=
\begin{pmatrix}
100&0\\
0&1
\end{pmatrix}.
$$

A one-unit difference on axis 1 becomes a 100-unit difference.

The underlying images did not change.

Only the coordinate chart did.

---

# 59. Style chart refinement

Future style maps may move from:

$$
\phi_8
$$

to:

$$
\phi_{16}
$$

or a nonlinear graph representation.

GVSS does not collapse if the chart changes.

The chart is a navigation representation inside the larger theory.

---

# 60. Verifier-gated reachability

## Definition GVSS04-D11

Given evaluator/verifier:

$$
E:
\Omega_\Sigma
\to
\mathbb R,
$$

and threshold $\tau$:

$$
\boxed{
\mathcal A_E(\tau)
=
\{
I:E(I)\ge\tau
\}.
}
$$

Define:

$$
\boxed{
\mathcal R^{\mathrm{acc}}_{\mathsf G,\Pi,E}(B,\tau)
=
\mathcal R_{\mathsf G,\Pi}(B)
\cap
\mathcal A_E(\tau).
}
$$

---

# 61. GVSS04-T8 — Evaluator-threshold monotonicity

## Theorem GVSS04-T8

If:

$$
\tau_1\le\tau_2,
$$

then:

$$
\boxed{
\mathcal R^{\mathrm{acc}}(B,\tau_2)
\subseteq
\mathcal R^{\mathrm{acc}}(B,\tau_1).
}
$$

### Proof

$$
E(I)\ge\tau_2
$$

implies:

$$
E(I)\ge\tau_1.
$$

 $\square$

A stricter gate cannot increase the accepted set.

---

# 62. Evaluator-guided search

A verifier can be used for:

- ranking parallel candidates;
- stopping;
- choosing which constraint to repair;
- choosing a seed;
- choosing a provider;
- choosing whether to edit or regenerate.

Therefore $E$ changes the effective navigation policy even if $G$ is fixed.

---

# 63. Evaluator misalignment

Let:

$$
U(I)
$$

represent the intended downstream utility.

The evaluator is a proxy:

$$
E(I).
$$

A proxy can be misaligned.

---

# 64. GVSS04-N3 — Closed-loop proxy optimization no-go

Consider two images:

$$
I_1,I_2.
$$

Let:

$$
U(I_1)=1,
\qquad
U(I_2)=0.
$$

Let proxy evaluator:

$$
E(I_1)=0,
\qquad
E(I_2)=1.
$$

A controller that optimizes $E$ chooses $I_2$.

Therefore:

$$
\boxed{
\max E
\not\Rightarrow
\max U.
}
$$

Even a perfect closed loop can optimize the wrong objective.

 $\square$

---

# 65. Metric pluralism

This is one reason the runtime uses:

$$
\boxed{
\text{Hard Gates}
+
\text{Metric Vector}
+
\text{Optional Composite Score}.
}
$$

A single learned preference score should not silently replace:

- prompt adherence;
- technical validity;
- identity;
- reference consistency;
- diversity;
- anti-homogenization.

---

# 66. GenEval / VQAScore boundary

Fine-grained compositional benchmarks and VQA-based image-text evaluation provide stronger evaluation than one holistic similarity number on some tasks.

They remain task-dependent proxies.

GVSS-04 treats evaluation as a representation/observer layer rather than an oracle.

---

# 67. Human review as observer fusion

Let automated observer be:

$$
O_A.
$$

Human observer:

$$
O_H.
$$

Joint report:

$$
\boxed{
O_{\mathrm{joint}}(I)
=
(
O_A(I),
O_H(I)
).
}
$$

This can contain at least as much raw report information as either coordinate alone.

It also costs human time.

---

# 68. Human review is not infallible

Human evaluators can disagree.

Project intent can be underspecified.

A single human approval does not define universal aesthetic truth.

The human observer is another declared information source.

---

# 69. Visual lineage

The existing runtime creates lineage child packets rather than overwriting parent packets.

GVSS-04 makes this a formal provenance rule.

---

# 70. Lineage record

## Definition GVSS04-D12

Every refinement artifact has:

$$
\boxed{
L_t
=
(
id_t,
parent_t,
action_t,
r_t,
M_t,
artifact_t
).
}
$$

For pure one-parent refinement:

$$
parent_t
$$

references exactly one earlier artifact.

---

# 71. GVSS04-T9 — Single-parent lineage acyclicity

## Theorem GVSS04-T9

Suppose every child artifact has a unique ID greater than its parent's creation index and records exactly one earlier parent.

Then the lineage graph is acyclic.

Every artifact has a finite parent path ending at a root artifact.

### Proof

Every edge strictly decreases creation index when followed from child to parent.

A directed cycle would require the index to strictly decrease and return to its starting value.

Impossible.

Finite descent ends at a node with no parent.

 $\square$

---

# 72. Merge workflows

If an artifact can merge multiple parents, lineage becomes a DAG rather than a tree.

The same acyclicity proof holds if every parent is older than the child.

---

# 73. Provenance-preserving refinement

A child should record:

- parent;
- action;
- prompt/compiler delta;
- provider delta;
- seed/workflow;
- evaluator result;
- backend;
- cost.

This allows later audit of which regime change produced which improvement/regression.

---

# 74. Reflexive visual state

The minimal closed-loop state can now be written:

$$
\boxed{
\mathcal V_t
=
(
\Omega_\Sigma,
\mathsf G_t,
C_t,
\Pi_t,
O_t,
E_t,
M_t,
e_t,
B_t,
\mathsf{Prov}_t
).
}
$$

 $\Omega_\Sigma$ is fixed for one raster specification.

Most other coordinates can change.

---

# 75. Reflexive update

$$
\boxed{
\mathcal V_{t+1}
=
\Psi(
\mathcal V_t,
a_t,
I_t,
M_t
).
}
$$

The controller is reflexive because the report generated under the current visual regime changes the future visual regime.

---

# 76. Open-loop generator

An open-loop system uses:

$$
\boxed{
r_{t+1}=r_t
}
$$

except for predetermined sampling state.

No report-dependent regime adaptation occurs.

---

# 77. Closed-loop generator

A closed-loop system permits:

$$
\boxed{
r_{t+1}
=
\Psi(
r_t,
O_t(I_t)
).
}
$$

The representation/control regime can therefore move.

---

# 78. Reflexive visual navigation

## Definition GVSS04-D13

A system performs **Reflexive Visual Navigation (RVN)** if:

1. it generates or edits visual states under regime $r_t$ ;
2. an observer evaluates the resulting state;
3. the report can change a future representation/control coordinate of $r_{t+1}$ ;
4. the change is recorded with cost and provenance.

---

# 79. RVN is not ordinary rerolling

Repeated random sampling under a fixed prompt/model can be closed-loop only if results influence later policy.

Blindly generating 100 independent samples is search, but not representation-reflexive adaptation.

---

# 80. RVN is not prompt engineering alone

Prompt rewriting is one RVN action.

Other actions can change:

- model;
- adapter;
- reference;
- control architecture;
- evaluator;
- backend;
- human review.

The theory is deliberately broader than prompt optimization.

---

# 81. RVN is not model fine-tuning alone

Fine-tuning changes $G$ or $P$.

RVN can operate without any training by changing:

- search;
- constraints;
- bindings;
- editing;
- verification.

Many current closed-loop T2I systems are training-free.

---

# 82. Search breadth versus search depth

Parallel best-of- $N$ increases breadth.

Iterative critic/edit/refine increases depth.

Provider rebind changes the local domain being searched.

The runtime controller can allocate budget among all three.

---

# 83. Test-time scaling

Define test-time budget:

$$
\boxed{
B_{\mathrm{test}}.
}
$$

Increasing it can permit:

- more candidate seeds;
- more verifier calls;
- more edit rounds;
- more provider trials.

By GVSS04-T1, the feasible bounded reachability set cannot shrink if old executions remain allowed.

The expected quality need not monotonically increase under a bad policy.

---

# 84. Reachability-aware controller

A controller should maintain hypotheses about failure cause.

Example state:

$$
\boxed{
h_t
=
(
p_{\mathrm{sample}},
p_{\mathrm{compile}},
p_{\mathrm{search}},
p_{\mathrm{reach}},
p_{\mathrm{eval}}
).
}
$$

The next action can depend on this failure belief.

This is an engineering proposal.

---

# 85. Bayesian diagnostic controller

A probabilistic implementation could maintain:

$$
P(
F_k
\mid
H_t
).
$$

The controller then selects action $a$ maximizing expected reduction of relevant deficit minus cost.

GVSS-04 does not derive the optimal Bayesian controller.

---

# 86. Rule-based controller

The existing runtime uses rule-based triggers.

For example:

- low prompt adherence -> RECOMPILE;
- persistent low style/character/reference scores -> REBIND;
- local technical defect -> REPAIR;
- near threshold -> RESAMPLE.

This is a practical first implementation.

---

# 87. Learned controller

A learned policy can replace rules.

But it should still expose:

- action;
- budget;
- metric changes;
- lineage.

Otherwise failure diagnosis becomes opaque.

---

# 88. Controller no-go

A more intelligent controller cannot reach an image outside the semantic/algorithmic reachability of every provider it is allowed to bind.

Search intelligence can enlarge **practical bounded reachability**.

It cannot manufacture expressivity absent from the entire admissible generator family.

This is the visual version of RRT language-search incompleteness.

---

# 89. Multi-provider reachable domain

Let allowed bindings be:

$$
\mathfrak G
=
\{
\mathsf G_1,\ldots,\mathsf G_k
\}.
$$

With zero-cost switching idealization:

$$
\boxed{
\mathcal R_{\mathrm{union}}
=
\bigcup_{j=1}^k
\mathcal R(\mathsf G_j).
}
$$

Real switching cost can reduce practical bounded coverage.

---

# 90. GVSS04-T10 — Union upper bound for multi-provider reachability

## Theorem GVSS04-T10

Any policy restricted to provider family:

$$
\mathfrak G
$$

can only produce images in:

$$
\boxed{
\bigcup_{
\mathsf G\in\mathfrak G
}
\mathcal R(\mathsf G).
}
$$

### Proof

Every produced image is produced under one currently bound generator in $\mathfrak G$.

 $\square$

No controller can exceed the union of its admissible generator semantic reachability without adding a new provider/edit operation that enlarges the family.

---

# 91. Repair operators enlarge the action family

If REPAIR can map an image to a state not directly reachable from the base generator, the relevant reachable system must include repair kernels too.

Therefore:

$$
\boxed{
\text{reachable domain belongs to the whole runtime action system},
}
$$

not necessarily the T2I generator alone.

---

# 92. Runtime reachable closure

Let action kernels be:

$$
\mathcal K
=
\{
K_{\mathrm{generate}},
K_{\mathrm{repair}},
K_{\mathrm{edit}},
\ldots
\}.
$$

The runtime reachable closure is all states reachable by finite admissible compositions under budget.

This is the proper object for a multi-tool visual agent.

---

# 93. Model Intelligence versus Search Intelligence

Paper 03 distinguishes generator capability from the ability to find useful regions.

GVSS-04 sharpens this into:

$$
\boxed{
\mathcal R_{\mathrm{practical}}
=
f(
\mathcal K,
\Pi,
O,
E,
B
).
}
$$

The observer and evaluator affect which trajectories are pursued.

Search intelligence is therefore observer dependent.

---

# 94. Evaluator-induced blindness

If evaluator $E$ assigns low scores to an actually valuable visual mode, the controller may systematically avoid that region.

Thus the practical reachable **accepted** set can be smaller than raw runtime reachability.

This is a representation-induced blind spot.

---

# 95. Anti-homogenization axis

The runtime explicitly contains:

$$
H
=
\text{Anti-Homogenization}.
$$

This is theoretically important.

A controller that maximizes only prompt adherence/aesthetic preference can collapse toward common high-reward modes.

Anti-homogenization acts as a diversity debt constraint.

---

# 96. Style consistency versus diversity

These objectives can conflict:

$$
\boxed{
S\uparrow
}
$$

can accompany:

$$
\boxed{
D\downarrow.
}
$$

There is no universal optimum without a project-specific objective.

This motivates Pareto evaluation.

---

# 97. Unrealized Visual Frontier under a controller

Paper 03 defines:

$$
\mathcal F_{\mathrm{UV}}.
$$

GVSS-04 can make it policy dependent:

$$
\boxed{
\mathcal F_{\mathrm{UV}}(
\Pi,
B
)
=
\mathcal R_{\mathrm{runtime},\Pi}(B)
\cap
\mathcal M_{\mathrm{meaningful}}
\setminus
\mathcal N_\epsilon(
\mathcal H_{\mathrm{ref}}
).
}
$$

Thus better search intelligence can enlarge the **discovered** frontier even without changing the base model.

---

# 98. Frontier discovery is observer relative

The neighborhood:

$$
\mathcal N_\epsilon(
\mathcal H_{\mathrm{ref}}
)
$$

depends on a distance/observer.

Therefore "novel" remains metric-relative.

RRT-05 style intrinsicness warnings apply directly.

---

# 99. Style chart and novelty chart are different

A style map may be useful for one kind of novelty.

A semantic scene-graph metric may reveal another.

A perceptual embedding may reveal another.

No one chart is the full GVSS geometry.

---

# 100. Closed-loop novelty search

A future controller can explicitly optimize for:

- target satisfaction;
- distance from reference modes;
- anti-homogenization;
- style coherence.

This creates a constrained novelty navigation problem.

GVSS-04 does not claim an optimal novelty objective.

---

# 101. Current literature: Latent Diffusion

Latent Diffusion Models show that a powerful image generator can operate in a learned latent representation rather than raw pixels and support flexible conditioning through cross-attention.

This is a clear example that the representation used for navigation need not be the raster state space itself.

GVSS treats:

$$
\Omega_\Sigma
$$

as the ambient representable image space, not necessarily the computational search coordinate system.

---

# 102. Current literature: Classifier-Free Guidance

Classifier-Free Guidance explicitly changes the fidelity/diversity tradeoff at inference.

This is a prior example of a control parameter altering the practical sampling geometry.

GVSS-04 treats guidance scale as part of the regime.

---

# 103. Current literature: ControlNet

ControlNet adds structural visual controls such as:

- edges;
- depth;
- pose;
- segmentation.

This supports Paper 02's claim that a "prompt" is not the complete visual coordinate/control system.

---

# 104. Current literature: Prompt-to-Prompt

Prompt-to-Prompt controls cross-attention to perform semantic edits while preserving more of an existing image structure.

This is a precursor to REPAIR / representation-preserving local transition ideas.

---

# 105. Current literature: Test-time Prompt Refinement

TIR uses a multimodal model to:

1. inspect generated image;
2. diagnose prompt/image mismatch;
3. rewrite prompt;
4. regenerate;
5. verify again.

This is directly a RECOMPILE-style loop.

GVSS adds the possibility that the correct action may instead be RESAMPLE, REBIND, or REPAIR.

---

# 106. Current literature: Iterative Refinement

Recent iterative compositional image generation uses a VLM critic to propose corrections and can outperform compute-matched parallel sampling on several compositional benchmarks.

This supports the distinction between:

$$
\Pi_{\mathrm{parallel}}
$$

and:

$$
\Pi_{\mathrm{iterative}}.
$$

---

# 107. Current literature: VisionDirector

VisionDirector decomposes long instructions into structured goals, uses multimodal verification, chooses staged edits, and supports rollback.

This is especially close to the runtime logic developed before GVSS-04.

The overlap must be cited explicitly.

---

# 108. Current literature: Agentic Retoucher

Agentic Retoucher formulates editing as a perception-reasoning-action loop and performs targeted local refinement.

This is a current direct precedent for REPAIR as a closed-loop visual action.

---

# 109. Current literature: Qwen-Image-Agent

Qwen-Image-Agent identifies a **Context Gap** between user context and the generation context needed by T2I systems.

It integrates planning, reasoning, search, memory, and feedback.

This is very close to the GVSS idea that user intent must be compiled into a richer generation regime rather than treated as a complete prompt coordinate.

GVSS-04 therefore avoids claiming the broad "intent/context compiler" problem as uniquely new.

---

# 110. Current literature: Verifier-guided Test-Time Scaling

Recent test-time scaling work searches over diffusion/flow noise samples and uses reward/verifier models to allocate compute.

This is a direct neighboring approach to budgeted reachable-space search.

---

# 111. Evaluation boundary

GenEval evaluates object-focused compositional properties such as:

- count;
- color;
- position;
- co-occurrence.

VQAScore/GenAI-Bench evaluate complex image-text alignment through visual question answering.

These demonstrate that different observers reveal different failure modes.

GVSS formalizes this as observer/evaluator dependence rather than choosing one universal metric.

---

# 112. What is classical / neighboring

GVSS-04 does not claim as inventions:

- diffusion sampling;
- latent diffusion;
- classifier-free guidance;
- ControlNet;
- cross-attention editing;
- best-of-N sampling;
- image reward models;
- VLM image criticism;
- prompt refinement;
- iterative image refinement;
- test-time scaling;
- agentic image generation;
- multi-agent visual refinement;
- Pareto optimization.

---

# 113. Candidate GVSS-specific synthesis

Subject to deeper novelty audit, the bridge-specific synthesis is:

1. embedding the existing GVSS state-space and reachable-set hierarchy into an RRT-style regime state;
2. formally separating RESAMPLE, RECOMPILE, and REBIND by which part of the target/reachable geometry they can change;
3. defining policy- and budget-dependent practical visual reachability;
4. carrying the existing eight-axis runtime evaluation vector into a vector defect recursion;
5. interpreting finite-dimensional style maps as representation charts rather than intrinsic visual geometry;
6. treating evaluator thresholds as gates on practical accepted reachability;
7. joining visual generation, evaluation, action selection, cost, and lineage into one reflexive visual state;
8. defining the Visual Reflexive Pareto Frontier.

No strong novelty claim is made in v0.1.

---

# 114. What GVSS-04 proves

Under its explicit definitions/hypotheses, GVSS-04 proves:

1. bounded practical reachability is monotone in nested budget;
2. a policy that can simulate another policy weakly dominates its bounded reachable set;
3. RESAMPLE, RECOMPILE, and REBIND act at distinct geometric levels under the declared action semantics;
4. nonnegative vector visual-defect recursions unroll into transported historical defects plus injected defects;
5. protected-coordinate regression bounds accumulate additively;
6. every strictly monotone scalar optimum lies on the declared visual Pareto frontier;
7. Euclidean style-coordinate distance is not intrinsic under arbitrary invertible coordinate changes;
8. stricter evaluator thresholds shrink the accepted reachable set;
9. proxy-evaluator optimization can worsen true intent under evaluator misalignment;
10. single-parent refinement lineage is acyclic when parent indices precede children;
11. a multi-provider controller cannot exceed the union of the reachable domains of its admissible runtime action family without adding a new generative/edit operator.

---

# 115. What GVSS-04 does not prove

It does not prove:

- a complete intrinsic metric on visual meaning;
- the exact reachable set of any proprietary image model;
- that more test-time compute always improves expected quality;
- that a VLM evaluator represents human intent exactly;
- that iterative refinement always dominates parallel sampling;
- that REBIND always fixes persistent failure;
- that a finite style map captures all visual style;
- that the current eight metric dimensions are complete;
- that human review is infallible;
- that the Unrealized Visual Frontier can be globally measured over all human visual history.

---

# 116. Engineering correspondence to the existing runtime

The existing runtime sequence

$$
\boxed{
Run
\to
Verify
\to
Diagnose
\to
SelectAction
\to
Refine
\to
Run
}
$$

is the operational implementation boundary of RVN.

GVSS-04 supplies the theoretical interpretation of each stage.

---

# 117. Run

Run samples from:

$$
K_{r_t}.
$$

---

# 118. Verify

Verify applies observer/evaluator:

$$
O_t,
E_t.
$$

---

# 119. Diagnose

Diagnose estimates which failure layer is responsible.

---

# 120. SelectAction

SelectAction chooses which regime coordinate to change.

---

# 121. Refine

Refine applies the action-specific transition.

---

# 122. Repeat

The resulting child regime/artifact becomes the state for the next iteration.

---

# 123. Closed-loop stopping

Possible stop reasons:

- ACCEPT: target/gates satisfied;
- STOP: budget or policy limit reached;
- HUMAN_REVIEW: automated diagnosis insufficient.

Stopping is not equivalent to proof that no better image exists.

---

# 124. Bounded rationality

The runtime acts under:

$$
B<\infty.
$$

Therefore the output is best interpreted as:

> the result selected under one finite search policy and budget,

not:

> the globally optimal image in $\Omega_\Sigma$.

---

# 125. Visual search debt

A more complex controller can improve search but adds:

- inference calls;
- VLM calls;
- image edits;
- provider switches;
- latency;
- state management.

This is **search debt**.

---

# 126. Verification debt

More evaluators can expose more failure modes but add:

- compute;
- disagreement;
- calibration burden;
- false-rejection risk.

This is **verification debt**.

---

# 127. Switching debt

REBIND / SWITCH_BACKEND can enlarge capability but add:

- format translation;
- style drift;
- seed discontinuity;
- provider cost;
- reproducibility loss.

This is **switching debt**.

---

# 128. Provenance debt

A runtime that overwrites prompts/workflows/images loses causal information about why an improvement occurred.

Lineage logging reduces provenance debt.

---

# 129. Visual regime cost vector

A fuller cost vector can be:

$$
\boxed{
\mathbf C_{\mathrm{vis}}
=
(
e,
C_{\mathrm{GPU}},
C_{\mathrm{cloud}},
C_{\mathrm{latency}},
C_{\mathrm{verify}},
C_{\mathrm{switch}},
C_{\mathrm{human}},
D_{\mathrm{homog}},
D_{\mathrm{prov}}
).
}
$$

---

# 130. No universal scalar objective

Different projects weight:

- style coherence;
- novelty;
- character consistency;
- cost;
- turnaround time;

differently.

Therefore the bridge keeps the vector explicit.

---

# 131. RRT relation

The RRT closure principles specialize as follows.

### RRT defect transport

becomes:

$$
e_{t+1}
\preceq
A_te_t+\varepsilon_t.
$$

### RRT information/representation order

becomes:

- observer/evaluator refinement;
- style-chart representation;
- human/automated observer fusion.

### RRT cost debt

becomes:

- compute;
- verification;
- switching;
- homogenization.

### RRT escalation certificate

becomes:

$$
\text{RESAMPLE}
\to
\text{RECOMPILE}
\to
\text{REBIND}
$$

only when lower-level failure is sufficiently diagnosed.

### RRT provenance

becomes lineage-preserving packet evolution.

---

# 132. Why this is not RRT-21

RRT is closed at RRT-20.

GVSS-04 is a domain specialization.

It imports frozen RRT meta-laws without reopening RRT numbering.

---

# 133. Canonical bridge formula

The entire bridge can be written:

$$
\boxed{
\begin{aligned}
I_t
&\sim
K_{r_t},
\\
Y_t
&=
O_t(I_t,C_t),
\\
e_t
&=
D(Y_t,\tau),
\\
a_t
&=
\pi_{\mathrm{RVN}}(
r_t,e_t,Y_t,B_t,H_t
),
\\
r_{t+1}
&=
\Psi(
r_t,a_t,Y_t
).
\end{aligned}
}
$$

---

# 134. Canonical visual state

$$
\boxed{
r_t
=
(
G_t,
P_t,
\Gamma_t,
C_t,
\Lambda_t,
\Pi_t,
O_t,
E_t,
B_t,
\mathsf{Prov}_t
).
}
$$

This is the default formal state for later GVSS closed-loop papers.

---

# 135. Canonical failure separation

$$
\boxed{
\textbf{
A bad generated image does not identify the level at which the visual system failed.
}
}
$$

The failure can live in:

- sampling;
- constraints;
- compiler;
- search;
- generator reachability;
- evaluator;
- intent.

---

# 136. Canonical runtime principle

$$
\boxed{
\textbf{
Change the weakest justified layer, not the largest available layer.
}
}
$$

Do not rebind the whole model when a seed reroll is enough.

Do not reroll indefinitely when the compiled intent is wrong.

---

# 137. Canonical reachability principle

$$
\boxed{
\textbf{
Practical visual reachability is a property of the whole search-and-control runtime,
not of the foundation image generator alone.
}
}
$$

---

# 138. Canonical observer principle

$$
\boxed{
\textbf{
A visual evaluator changes what the controller can see,
and therefore changes which parts of visual space the controller will practically explore.
}
}
$$

---

# 139. Canonical provenance principle

$$
\boxed{
\textbf{
Every refinement should be a lineage-preserving child state,
not a silent overwrite of the parent regime.
}
}
$$

---

# 140. Proposed GVSS-05

The next paper should not broaden the domain again.

It should sharpen failure diagnosis.

Proposed title:

$$
\boxed{
\textbf{
GVSS-05 — Visual Failure Stratification and Reachability Diagnosis
}
}
$$

Chinese:

**視覺失敗分層與可達性診斷：從 Seed Failure 到 Generator-Boundary Failure**

Main questions:

1. How many failures justify escalation from RESAMPLE to RECOMPILE?
2. When is persistent failure evidence of provider reachability mismatch?
3. Can evaluator disagreement distinguish observer failure from generator failure?
4. How should failure beliefs update across iterations?
5. What stopping rule prevents infinite rerolling?
6. Can diagnostic policies be benchmarked independently of generators?

---

# 141. References

1. Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer, **High-Resolution Image Synthesis with Latent Diffusion Models**, arXiv:2112.10752 / CVPR 2022.
2. Jonathan Ho, Tim Salimans, **Classifier-Free Diffusion Guidance**, arXiv:2207.12598.
3. Lvmin Zhang, Anyi Rao, Maneesh Agrawala, **Adding Conditional Control to Text-to-Image Diffusion Models**, arXiv:2302.05543.
4. Amir Hertz et al., **Prompt-to-Prompt Image Editing with Cross Attention Control**, arXiv:2208.01626.
5. Dhruba Ghosh, Hanna Hajishirzi, Ludwig Schmidt, **GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment**, arXiv:2310.11513.
6. Jiazheng Xu et al., **ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation**, arXiv:2304.05977.
7. Zhiqiu Lin et al., **Evaluating Text-to-Visual Generation with Image-to-Text Generation**, arXiv:2404.01291.
8. Mohammad Abdul Hafeez Khan et al., **Test-time Prompt Refinement for Text-to-Image Models**, arXiv:2507.22076.
9. Shantanu Jaiswal et al., **Iterative Refinement Improves Compositional Image Generation**, arXiv:2601.15286.
10. Meng Chu et al., **VisionDirector: Vision-Language Guided Closed-Loop Refinement for Generative Image Synthesis**, arXiv:2512.19243.
11. Shaocheng Shen et al., **Agentic Retoucher for Text-To-Image Generation**, arXiv:2601.02046.
12. **Qwen-Image-Agent: Bridging the Context Gap in Real-World Image Generation**, arXiv:2606.26907.
13. Vignesh Sundaresha et al., **An Efficient Test-Time Scaling Approach for Image Generation**, arXiv:2512.08985.
14. GVSS Paper 01, **The Global Visual State Space Hypothesis**, internal series artifact, 2026.
15. GVSS Paper 02, **Visual Generation as Constraint-Domain Solving**, internal series artifact, 2026.
16. GVSS Paper 03, **Generative Reachability and Unrealized Visuals**, internal series artifact, 2026.
17. RRT-20, **Reflexive Representation Theory: Unified Closure, Meta-Theorems, Limits, and Research Program**, internal series artifact, 2026.

---

# 142. Conclusion

GVSS Paper 01 turns digital images into points in:

$$
\Omega_\Sigma.
$$

Paper 02 turns generation into constrained search.

Paper 03 turns model capability into bounded reachability.

GVSS-04 turns the **search regime itself** into a dynamical state.

The controller no longer asks only:

> Which image should I sample?

It can ask:

> Which representation of intent should I use?

> Which constraint should I relax or strengthen?

> Which provider should I bind?

> Which observer should I trust?

> Which region should I repair?

> How much budget should I spend?

> When should I stop?

The key state is:

$$
\boxed{
r_t
=
(
\mathsf G_t,
\Gamma_t,
C_t,
\Lambda_t,
\Pi_t,
O_t,
E_t,
B_t,
\mathsf{Prov}_t
).
}
$$

The key recursion is:

$$
\boxed{
e_{t+1}
\preceq
A_te_t+\varepsilon_t.
}
$$

The key geometric separation is:

$$
\boxed{
\text{RESAMPLE}
\neq
\text{RECOMPILE}
\neq
\text{REBIND}.
}
$$

The key reachability claim is:

$$
\boxed{
\mathcal R_{\mathrm{practical}}
=
f(
\text{generator},
\text{binding},
\text{search policy},
\text{observer},
\text{verifier},
\text{budget}
).
}
$$

And the bridge principle is:

$$
\boxed{
\textbf{
GVSS gives the visual state-space geometry.
RRT gives the law for changing the representation and control regime used to navigate that geometry.
}
}
$$

This establishes Reflexive Visual Navigation as the fourth formal layer of the GVSS sequence.

---

# Canonical-source policy

This file is the canonical UTF-8 source artifact.

- Canonical inline mathematics uses ` $...$ `.
- Canonical display mathematics uses `$$...$$`.
- No Unicode mathematical-symbol conversion is used as source normalization.
- No `unicode_escape` round trip is used.
- Backslashes and delimiters are preserved literally.
- Validation is required before release.
- This paper does not reopen RRT numbering.
