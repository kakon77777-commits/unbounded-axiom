# GVSS-10 — Task-Conditioned Visual Routing, Capability Attribution, and Portfolio Learning
## 任務條件式視覺路由、能力歸因與生成器投資組合學習：選擇偏差、探索覆蓋、冷啟動與多階段歸因

**Series:** Global Visual Space & Generative Navigation — Paper 10  
**Bridge:** GVSS × frozen Reflexive Representation Theory (RRT)  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal routing-and-learning paper. Task-conditioned capability definitions, routing-selection-bias counterexamples, off-policy support no-go, inverse-propensity unbiasedness, finite-sample IPS concentration under overlap, cold-start non-identifiability, exploration-based coverage certificates, capability-estimation routing regret, oracle regret decomposition, conditional fallback value under correlated failures, multi-stage attribution non-identifiability, version-drift detection, and Pareto routing statements are proved under the stated hypotheses. Contextual bandits, off-policy evaluation, inverse propensity scoring, doubly robust estimation, model routing, multi-model T2I serving, and cooperative-game attribution are prior research and are not claimed as GVSS inventions. No strong novelty claim is made.

**Keywords:** text-to-image routing, contextual bandit, provider capability, off-policy evaluation, inverse propensity weighting, provider exploration, cold start, image model routing, capability attribution, portfolio learning, GVSS

---

# Abstract

GVSS-09 formalized a provider portfolio

$$
S\subseteq\mathcal P
$$

with provider reachable sets

$$
\mathcal R_\nu
$$

and raw portfolio coverage

$$
\boxed{
f(S)
=
\mu
\left(
\bigcup_{\nu\in S}
\mathcal R_\nu
\right).
}
$$

It also introduced robust multi-coverage, switching cost, calibration debt, and correlated provider failure.

GVSS-10 moves from a static provider portfolio to a **task-conditioned routing system that learns its own provider capability model online**.

Let

$$
\boxed{
\theta
\in
\Theta
}
$$

denote a task/context representation.

A task can include:

- prompt semantics;
- composition complexity;
- number/count constraints;
- typography requirements;
- character identity requirements;
- style coordinates;
- reference/control availability;
- target resolution;
- latency budget;
- privacy/offline constraints;
- current project state;
- previous provider failures.

For provider

$$
\nu\in\mathcal P,
$$

define an outcome vector

$$
\boxed{
Z_\nu(\theta)
=
(
Q_\nu,
A_\nu,
S_\nu,
D_\nu,
C_\nu,
L_\nu,
K_\nu,
F_\nu
)
}
$$

containing, for example:

- quality;
- prompt/constraint adherence;
- style consistency;
- diversity;
- character/reference consistency;
- latency;
- monetary/compute cost;
- failure indicator.

A scalar routing utility may be declared as

$$
\boxed{
U_\nu(\theta)
=
u(
Z_\nu(\theta)
)
}
$$

for a project-specific utility function.

The **task-conditioned provider capability** is

$$
\boxed{
\mathcal C_\nu(\theta)
=
E[
U_\nu(\theta)
\mid
\theta,\nu
].
}
$$

The oracle one-step router is

$$
\boxed{
\nu^\star(\theta)
\in
\arg\max_{\nu\in\mathcal P}
\mathcal C_\nu(\theta).
}
$$

A learned router replaces

$$
\mathcal C_\nu
$$

with an estimate

$$
\widehat{\mathcal C}_\nu.
$$

This appears straightforward, but the main statistical difficulty is that routing determines which provider outcomes become observable.

If historical logging policy is

$$
\boxed{
\mu(\nu\mid\theta),
}
$$

then the runtime observes reward/outcome only for the provider actually selected.

Therefore provider capability data are **bandit feedback**, not supervised labels for every provider.

---

## Routing-selection bias

A naive provider average:

$$
\boxed{
\overline U_\nu^{\mathrm{naive}}
=
E[
U
\mid
A=\nu
]
}
$$

is generally not the population capability

$$
E_\theta
\mathcal C_\nu(\theta).
$$

A concrete reversal example is:

Task classes are equally likely:

$$
\theta\in
\{
\mathrm{easy},
\mathrm{hard}
\}.
$$

Provider A has:

$$
\mathcal C_A(\mathrm{easy})=0.8,
$$

$$
\mathcal C_A(\mathrm{hard})=0.2.
$$

Provider B has:

$$
\mathcal C_B(\mathrm{easy})=0.9,
$$

$$
\mathcal C_B(\mathrm{hard})=0.4.
$$

Thus B is better on **every task class** and its target-distribution mean is:

$$
\boxed{
V_B=0.65>V_A=0.50.
}
$$

Now let the historical router choose:

$$
A
\quad
\text{only on easy tasks},
$$

and:

$$
B
\quad
\text{only on hard tasks}.
$$

The observed logged means are:

$$
\boxed{
\overline U_A^{\mathrm{log}}=0.8,
}
$$

$$
\boxed{
\overline U_B^{\mathrm{log}}=0.4.
}
$$

The historical log therefore ranks A above B even though B dominates A pointwise.

Thus:

$$
\boxed{
\text{historical routed average}
\not\Rightarrow
\text{provider capability ranking}.
}
$$

Provider routing creates its own training-distribution bias.

---

## Off-policy support is an identifiability condition

Suppose a target routing policy is

$$
\pi(\nu\mid\theta)
$$

and historical logging policy is

$$
\mu(\nu\mid\theta).
$$

If:

$$
\boxed{
\pi(\nu\mid\theta)>0
\Longrightarrow
\mu(\nu\mid\theta)>0
}
$$

for all relevant task-provider pairs, then the target policy is supported by the historical logging distribution.

If support fails, off-policy value need not be point identifiable from logged bandit feedback.

A two-world no-go suffices.

There is one task context

$$
\theta_0
$$

and two providers A and B.

The logging policy always chooses A:

$$
\boxed{
\mu(A\mid\theta_0)=1,
\qquad
\mu(B\mid\theta_0)=0.
}
$$

Observed reward for A is always

$$
0.5.
$$

World 1 assigns unobserved provider-B reward:

$$
\boxed{
U_B(\theta_0)=0.
}
$$

World 2 assigns:

$$
\boxed{
U_B(\theta_0)=1.
}
$$

The logged data distribution is identical in both worlds because B is never selected.

Yet a target policy choosing B has value 0 in World 1 and 1 in World 2.

Therefore:

$$
\boxed{
\text{no routing overlap}
\Longrightarrow
\text{no distribution-free point identification of unobserved provider value}.
}
$$

This is a contextual-bandit support/positivity boundary.

---

## Inverse propensity correction

When logging propensities are known and support holds, classical inverse propensity scoring applies.

For logged samples

$$
(
\theta_i,A_i,R_i
),
\qquad
A_i\sim\mu(\cdot\mid\theta_i),
$$

define target policy value

$$
\boxed{
V(\pi)
=
E_\theta
\sum_\nu
\pi(\nu\mid\theta)
\mathcal C_\nu(\theta).
}
$$

The IPS estimator is

$$
\boxed{
\widehat V_{\mathrm{IPS}}(\pi)
=
\frac1n
\sum_{i=1}^n
\frac{
\pi(A_i\mid\theta_i)
}{
\mu(A_i\mid\theta_i)
}
R_i.
}
$$

Under correct logging propensities and bounded/integrable reward:

$$
\boxed{
E[
\widehat V_{\mathrm{IPS}}(\pi)
]
=
V(\pi).
}
$$

If:

$$
0\le R_i\le1
$$

and overlap satisfies

$$
\boxed{
\mu(\nu\mid\theta)
\ge
\eta>0
}
$$

whenever

$$
\pi(\nu\mid\theta)>0,
$$

then each IPS summand lies in:

$$
[0,1/\eta].
$$

Hoeffding therefore yields:

$$
\boxed{
P
\left(
|
\widehat V_{\mathrm{IPS}}-V
|
\ge
\epsilon
\right)
\le
2
\exp(
-2n\eta^2\epsilon^2
).
}
$$

Equivalently, with probability at least

$$
1-\delta,
$$

$$
\boxed{
|
\widehat V_{\mathrm{IPS}}-V
|
\le
\frac1\eta
\sqrt{
\frac{
\log(2/\delta)
}{
2n
}
}.
}
$$

Poor exploration therefore appears as a variance/concentration debt through:

$$
1/\eta.
$$

Doubly robust and adaptive off-policy estimators are established prior work and can improve the bias-variance tradeoff.

GVSS does not claim those estimators as new.

---

## Exploration prevents provider starvation

If the router is purely greedy, an initially underestimated provider may never be selected again.

Then its task-conditioned capability remains unlearned.

A simple exploration floor is:

$$
\boxed{
\mu_t(\nu\mid\theta)
\ge
\eta
}
$$

for every active provider and task region during calibration.

For uniform exploration over $N$ providers with exploration mass $\epsilon$:

$$
\boxed{
\eta
=
\epsilon/N.
}
$$

This guarantees propensity support but costs routing performance.

---

## Cold-start non-identifiability

A newly added provider with no routed tasks has no direct empirical reward data.

Without structural transfer assumptions, two worlds can agree on every existing provider and every historical observation while assigning arbitrary capability to the new provider.

Therefore:

$$
\boxed{
\text{zero new-provider exposure}
\not\Rightarrow
\text{identified new-provider capability}.
}
$$

Provider metadata, architecture, benchmark priors, or related-model transfer can produce a prior.

They do not replace empirical exposure unless those transfer assumptions are justified.

---

## Cold-start calibration sample certificate

Suppose tasks are discretized into:

$$
L
$$

task cells and there are:

$$
N
$$

providers.

Suppose rewards lie in:

$$
[0,1].
$$

For every provider-task cell pair, collect:

$$
m
$$

independent calibration samples.

By Hoeffding plus a union bound, with probability at least:

$$
1-\delta,
$$

all cellwise empirical means satisfy:

$$
\boxed{
|
\widehat{\mathcal C}_{\nu,\ell}
-
\mathcal C_{\nu,\ell}
|
\le
\epsilon
}
$$

whenever:

$$
\boxed{
m
\ge
\frac{
\log(
2NL/\delta
)
}{
2\epsilon^2
}.
}
$$

This is a transparent calibration baseline.

Continuous task spaces require function approximation and more sophisticated uncertainty analysis.

---

## Capability-estimation error controls routing regret

For one task $\theta$, let:

$$
\nu^\star
=
\arg\max_\nu
\mathcal C_\nu(\theta).
$$

Let the router choose:

$$
\widehat\nu
=
\arg\max_\nu
\widehat{\mathcal C}_\nu(\theta).
$$

Suppose:

$$
\boxed{
|
\widehat{\mathcal C}_\nu(\theta)
-
\mathcal C_\nu(\theta)
|
\le
\varepsilon_\nu(\theta)
}
$$

for every provider.

Then instantaneous routing regret

$$
\boxed{
r(\theta)
=
\mathcal C_{\nu^\star}(\theta)
-
\mathcal C_{\widehat\nu}(\theta)
}
$$

satisfies:

$$
\boxed{
r(\theta)
\le
\varepsilon_{\nu^\star}(\theta)
+
\varepsilon_{\widehat\nu}(\theta).
}
$$

In particular, if all provider capability estimates have uniform error at most:

$$
\varepsilon,
$$

then:

$$
\boxed{
r(\theta)
\le
2\varepsilon.
}
$$

This directly links capability-model calibration to provider-routing quality.

---

## Oracle regret

Over tasks:

$$
\theta_1,\ldots,\theta_T,
$$

define oracle provider:

$$
\nu_t^\star
\in
\arg\max_\nu
\mathcal C_\nu(\theta_t).
$$

For router decisions:

$$
A_t,
$$

cumulative regret is:

$$
\boxed{
\operatorname{Reg}_T
=
\sum_{t=1}^T
[
\mathcal C_{\nu_t^\star}(\theta_t)
-
\mathcal C_{A_t}(\theta_t)
].
}
$$

If the pointwise capability errors satisfy the preceding bound, then a greedy estimated-capability router has:

$$
\boxed{
\operatorname{Reg}_T
\le
\sum_{t=1}^T
[
\varepsilon_{\nu_t^\star}(\theta_t)
+
\varepsilon_{A_t}(\theta_t)
].
}
$$

This is a deterministic estimation-to-regret bound.

It is not the same as a contextual-bandit regret theorem, because it assumes external confidence bounds on the capability estimates.

---

## Routing should use uncertainty

An optimistic route can use:

$$
\boxed{
\widehat{\mathcal C}_\nu(\theta)
+
\beta_t
\sigma_\nu(\theta)
}
$$

or a posterior sample.

This trades exploration against exploitation.

Contextual bandit algorithms such as UCB/Thompson-style methods are established prior research.

GVSS does not claim the exploration principle as new.

Its application claim is that a provider portfolio **cannot learn capability regions it never routes into**.

---

## Routing-selection bias and off-policy correction

The exact logging propensity should be stored:

$$
\boxed{
p_t
=
\mu_t(
A_t\mid\theta_t
).
}
$$

A minimal routing log is therefore:

$$
\boxed{
L_t
=
(
\theta_t,
A_t,
p_t,
R_t,
\nu_t,
\mathsf{Prov}_t
).
}
$$

Without propensity or an identifiable logging policy, inverse-propensity correction is unavailable.

The runtime should not overwrite the historical routing policy.

---

## Current T2I routing work

Cost-Aware Routing for Efficient Text-to-Image Generation explicitly learns prompt-conditioned routing among multiple T2I generation functions/models to balance output quality and compute cost.

RouteT2I routes prompts between edge and cloud image models using token-level multi-metric quality prediction.

HADIS jointly optimizes diffusion-model cascade selection, query routing, and resource allocation.

OctoT2I performs stateful multi-round tool routing and builds a self-evolving capability knowledge base through its Propose–Solve–Evaluate–Learn loop.

These are direct prior/current precedents for prompt-conditioned T2I routing and capability learning.

GVSS-10 does not claim multi-model visual routing as new.

---

## Conditional fallback under correlated failures

GVSS-09 showed that provider failures can be correlated.

Sequential routing must use conditional fallback value.

Let:

$$
F_A
$$

be primary-provider failure.

Fallback B has success probability:

$$
\boxed{
p_{B\mid A}
=
P(
B\text{ succeeds}
\mid
F_A,\theta
).
}
$$

This, not marginal:

$$
P(B\text{ succeeds}\mid\theta),
$$

is the relevant success probability after A has failed.

If provider failures are positively associated on the task distribution, then often:

$$
\boxed{
P(
B\text{ succeeds}
\mid
F_A,\theta
)
<
P(
B\text{ succeeds}
\mid
\theta
).
}
$$

A fallback router that uses the marginal probability can therefore overestimate recovery.

---

## Fallback threshold

Suppose after primary failure:

- fallback B costs $c_B$ ;
- successful recovery avoids terminal loss $L$ ;
- failed fallback provides no other value.

Then expected net gain from trying B is:

$$
\boxed{
G_B
=
p_{B\mid A}L-c_B.
}
$$

Fallback is worthwhile exactly when:

$$
\boxed{
p_{B\mid A}
>
c_B/L.
}
$$

The condition depends on **conditional** reliability after primary failure.

This is where GVSS-09 failure dependence enters routing.

---

## Multi-stage provider composition creates attribution ambiguity

Suppose final image is produced by path:

$$
\boxed{
\nu_1
\to
\nu_2
\to
\cdots
\to
\nu_m
}
$$

and only final project reward:

$$
R_{\mathrm{final}}
$$

is observed.

Individual provider contribution is generally not identifiable from the final reward alone.

A two-stage example is enough.

Observed path:

$$
A\to B
$$

has final reward:

$$
1.
$$

World 1 structural contributions:

$$
v(A)=1,
\qquad
v(B)=0.
$$

World 2:

$$
v(A)=0,
\qquad
v(B)=1.
$$

Both worlds generate the same observed final reward.

Therefore:

$$
\boxed{
\text{final path reward alone}
\not\Rightarrow
\text{provider-level causal contribution}.
}
$$

Attribution requires additional assumptions or counterfactual interventions such as:

- remove/replace a stage;
- replay from checkpoints;
- measure intermediate artifacts;
- estimate coalition values;
- use a declared cooperative-game attribution rule.

Shapley-style attribution is classical cooperative-game theory.

Recent multi-agent work also studies semantic contribution attribution in ordered workflows.

GVSS-10 does not claim contribution attribution as new.

---

## Path-level credit is always identifiable from path-level logs

Even when stage attribution is impossible, the path:

$$
p=
(\nu_1,\ldots,\nu_m)
$$

can be treated as one composite action.

Its expected capability can be learned as:

$$
\boxed{
\mathcal C_p(\theta)
=
E[
R_{\mathrm{final}}
\mid
\theta,p
].
}
$$

This sacrifices provider-level credit assignment but preserves empirical routing validity.

---

## Multi-stage lineage

A multi-stage visual artifact should preserve:

$$
\boxed{
\mathsf{Lineage}
=
(
\nu_1,
\nu_2,
\ldots,
\nu_m,
I_0,
I_1,
\ldots,
I_m,
\text{actions},
\text{scores},
\text{versions}
).
}
$$

Without intermediate artifacts and versions, later attribution or replay may be impossible.

---

## Capability drift

Provider capability:

$$
\mathcal C_\nu(\theta)
$$

is version dependent.

Let one fixed task cell $C$ and provider $\nu$ have old/new reward means:

$$
c_0,
c_1
$$

with bounded reward:

$$
R\in[0,1].
$$

Collect independent samples:

$$
n_0,n_1
$$

and empirical means:

$$
\widehat c_0,\widehat c_1.
$$

Define:

$$
\boxed{
r(n,\delta)
=
\sqrt{
\frac{
\log(4/\delta)
}{
2n
}
}.
}
$$

With probability at least:

$$
1-\delta,
$$

$$
\boxed{
|
(\widehat c_1-\widehat c_0)
-
(c_1-c_0)
|
\le
r(n_0,\delta)
+
r(n_1,\delta).
}
$$

Hence if:

$$
\boxed{
|
\widehat c_1-\widehat c_0
|
>
r(n_0,\delta)
+
r(n_1,\delta),
}
$$

the no-drift hypothesis:

$$
c_1=c_0
$$

is rejected on the high-probability event.

Capability routers should therefore be versioned and retrained/recalibrated after behaviorally relevant provider updates.

---

## Global averages hide task specialization

Provider A can have a higher global mean utility than B while B is much better in one critical task region.

Therefore:

$$
\boxed{
E_\theta\mathcal C_A(\theta)
>
E_\theta\mathcal C_B(\theta)
}
$$

does not imply:

$$
\mathcal C_A(\theta)
\ge
\mathcal C_B(\theta)
\quad
\forall\theta.
$$

A one-number leaderboard is not a routing policy.

---

## Capability region

Define provider-optimal region:

$$
\boxed{
\Theta_\nu^\star
=
\{
\theta:
\nu\in
\arg\max_j
\mathcal C_j(\theta)
\}.
}
$$

The router's goal is not to identify one globally best model.

It is to learn the partition/overlap of task space into provider capability regions.

---

## Cost-conditioned capability

Quality alone is insufficient.

One utility form is:

$$
\boxed{
\mathcal C_\nu^\lambda(\theta)
=
E[
Q_\nu(\theta)
-
\lambda K_\nu(\theta)
].
}
$$

Different:

$$
\lambda
$$

produce different provider regions.

For latency-constrained projects, use constrained capability:

$$
\boxed{
\max_\nu
E[Q_\nu(\theta)]
\quad
\text{s.t.}
\quad
P(
L_\nu(\theta)\le L_{\max}
)
\ge
1-\alpha.
}
$$

GVSS does not prescribe one scalarization.

---

## Cold-start provider entry

When new provider $\nu_{\mathrm{new}}$ enters:

1. create versioned identity;
2. import priors/metadata only as prior information;
3. reserve calibration/exploration traffic;
4. record propensities;
5. estimate capability across selected task cells;
6. update routing confidence;
7. expand exploitation only when justified.

A provider that receives zero exploration cannot empirically disprove a pessimistic prior.

---

## Capability exploration debt

Define task-provider exposure:

$$
\boxed{
N_t(\nu,C)
=
\#\{
s\le t:
\theta_s\in C,
A_s=\nu
\}.
}
$$

Low exposure means high capability uncertainty.

A router can track:

$$
\boxed{
D_{\mathrm{explore}}
(
\nu,C
)
=
\frac{
1
}{
\sqrt{
N_t(\nu,C)+1
}
}.
}
$$

This is an engineering uncertainty proxy.

---

## Exploration floor

A safe calibration phase can require:

$$
\boxed{
\mu_t(
\nu\mid\theta
)
\ge
\eta_{\nu,\theta}.
}
$$

The floor should be reduced only after:

- adequate samples;
- confidence;
- safety/cost review.

---

## Provider starvation no-go

If a deterministic router stops selecting provider B in region $C$ after finite time, and there are no external labels or structural transfer assumptions, then future traffic supplies no new direct evidence about:

$$
\mathcal C_B(\theta),
\qquad
\theta\in C.
$$

Thus a wrong capability estimate can become self-maintaining.

This is the routing analogue of GVSS-06 diagnostic self-locking.

---

## Routing self-locking

Belief:

> provider B is weak

causes:

> route no traffic to B

causes:

> collect no counterevidence

causes:

> belief remains B is weak.

Exploration is therefore an epistemic maintenance action.

---

## Off-policy capability correction

Suppose provider-specific target value is:

$$
\boxed{
V_\nu
=
E_\theta[
\mathcal C_\nu(\theta)
].
}
$$

A target policy that always selects provider $\nu$ has:

$$
\pi_\nu(a\mid\theta)
=
\mathbf1\{a=\nu\}.
$$

IPS gives:

$$
\boxed{
\widehat V_\nu
=
\frac1n
\sum_i
\frac{
\mathbf1\{A_i=\nu\}
}{
\mu(A_i\mid\theta_i)
}
R_i.
}
$$

This estimates provider value under the target context distribution when positivity holds.

The raw conditional mean:

$$
E[R\mid A=\nu]
$$

does not.

---

## Doubly robust capability learning

A practical capability learner can combine:

- a direct reward/capability model;
- a logging-propensity correction.

This is the classical doubly robust pattern.

The GVSS-specific requirement is to preserve:

- provider/version;
- task context;
- routing propensity;
- observed outcome;
- evaluator version.

---

## Propensity logging requirement

Canonical provider routing record:

```text
task_context
provider_selected
provider_version
routing_policy_version
selection_probability
quality_metrics
cost
latency
failure_status
evaluator_version
final_acceptance
lineage_id
```

Without:

```text
selection_probability
```

future IPS/DR correction may be impossible.

---

# 1. Position in the GVSS sequence

GVSS-09 constructs the portfolio.

GVSS-10 learns **where each provider is valuable** and routes task traffic accordingly.

---

# 2. Current routing literature boundary

Current T2I systems already route prompts among multiple generation models.

Cost-Aware Routing uses prompt-dependent routing among multiple already-trained T2I models/functions.

RouteT2I routes between edge and cloud models using predicted multi-metric quality.

HADIS jointly optimizes routing and serving resources.

OctoT2I uses stateful multi-round routing and learns a capability knowledge base through exploration.

GVSS-10 does not claim prompt-conditioned T2I routing as new.

---

# 3. Contextual-bandit boundary

The statistical structure:

$$
\theta
\to
A
\to
R_A
$$

with unobserved counterfactual rewards for unchosen actions is a contextual bandit.

Off-policy evaluation, IPS, doubly robust estimation, UCB, Thompson sampling, and related methods are established contextual-bandit theory.

GVSS-10 imports this theory into provider capability learning.

---

# 4. Task representation

## Definition GVSS10-D1

A task representation is:

$$
\boxed{
\theta
=
\phi(
\text{prompt},
\text{constraints},
\text{style},
\text{references},
\text{budget},
\text{project state}
).
}
$$

The map $\phi$ is itself a representation and can be misspecified.

---

# 5. Capability vector

## Definition GVSS10-D2

For provider $\nu$:

$$
\boxed{
\mathbf C_\nu(\theta)
=
E[
Z_\nu(\theta)
\mid
\theta,\nu
].
}
$$

Keep the vector when no scalar routing utility is justified.

---

# 6. Scalar routing capability

## Definition GVSS10-D3

Given utility/scalarization:

$$
u,
$$

$$
\boxed{
\mathcal C_\nu(\theta)
=
E[
u(Z_\nu)
\mid
\theta,\nu
].
}
$$

Routing optimality is always relative to this declared utility.

---

# 7. Global provider score

$$
\boxed{
\overline{\mathcal C}_\nu
=
E_{\theta\sim D}
[
\mathcal C_\nu(\theta)
].
}
$$

This is useful for summary but insufficient for task routing.

---

# 8. GVSS10-N1 — Global ranking does not imply pointwise routing dominance

## Counterexample

Two task classes have equal mass.

Provider A:

$$
\mathcal C_A(1)=1,
\quad
\mathcal C_A(2)=0.6.
$$

Provider B:

$$
\mathcal C_B(1)=0.7,
\quad
\mathcal C_B(2)=0.7.
$$

A has global mean:

$$
0.8,
$$

B:

$$
0.7.
$$

Yet on task 2:

$$
\boxed{
\mathcal C_B(2)
>
\mathcal C_A(2).
}
$$

Therefore one global leaderboard cannot implement task-optimal routing.

 $\square$

---

# 9. Logging policy

## Definition GVSS10-D4

Historical router:

$$
\boxed{
A_t
\sim
\mu_t(
\cdot\mid\theta_t
).
}
$$

The selected provider alone produces observed reward:

$$
R_t.
$$

---

# 10. Selection-bias reversal

## GVSS10-N2 — Routed historical means can reverse provider capability ranking

Use easy/hard example from the abstract.

B dominates A pointwise:

$$
0.9>0.8,
$$

$$
0.4>0.2.
$$

But historical router sends easy tasks only to A and hard tasks only to B.

Logged means:

$$
0.8
\quad\text{vs}\quad
0.4.
$$

Thus naive means reverse the actual population ranking.

 $\square$

---

# 11. Counterfactual reward

For each task, define potential provider reward:

$$
R_\nu(\theta).
$$

Only:

$$
R_{A_t}(\theta_t)
$$

is observed.

Capability learning is therefore missing counterfactual feedback.

---

# 12. Positivity/support

## Definition GVSS10-D5

Target policy $\pi$ is supported by logging policy $\mu$ if:

$$
\boxed{
\pi(\nu\mid\theta)>0
\Longrightarrow
\mu(\nu\mid\theta)>0
}
$$

almost surely over target contexts.

---

# 13. GVSS10-N3 — No-overlap provider value non-identifiability

## Proposition GVSS10-N3

If there exists task region with positive target probability where:

$$
\pi(B\mid\theta)>0
$$

but:

$$
\mu(B\mid\theta)=0,
$$

then without additional structural assumptions the target policy value need not be point identifiable from logged bandit feedback.

### Proof

Use the two-world construction in the abstract.

The logs are identical because B is never selected.

Counterfactual B reward differs.

 $\square$

---

# 14. IPS policy value

## Definition GVSS10-D6

$$
\boxed{
\widehat V_{\mathrm{IPS}}(\pi)
=
\frac1n
\sum_i
\frac{
\pi(A_i\mid\theta_i)
}{
\mu(A_i\mid\theta_i)
}
R_i.
}
$$

---

# 15. GVSS10-T1 — IPS unbiasedness

## Theorem GVSS10-T1

Assume:

- contexts are drawn from the target context distribution;
- logging propensities are correct;
- support holds;
- rewards are integrable.

Then:

$$
\boxed{
E[
\widehat V_{\mathrm{IPS}}(\pi)
]
=
V(\pi).
}
$$

### Proof

Condition on $\theta$:

$$
\begin{aligned}
E
\left[
\frac{
\pi(A\mid\theta)
}{
\mu(A\mid\theta)
}
R
\mid
\theta
\right]
&=
\sum_a
\mu(a\mid\theta)
\frac{
\pi(a\mid\theta)
}{
\mu(a\mid\theta)
}
E[R\mid\theta,a]
\\
&=
\sum_a
\pi(a\mid\theta)
\mathcal C_a(\theta).
\end{aligned}
$$

Average over $\theta$.

 $\square$

---

# 16. GVSS10-T2 — IPS finite-sample concentration under overlap

## Theorem GVSS10-T2

Assume:

$$
0\le R\le1
$$

and whenever:

$$
\pi(a\mid\theta)>0,
$$

$$
\mu(a\mid\theta)\ge\eta>0.
$$

Then with probability at least:

$$
1-\delta,
$$

$$
\boxed{
|
\widehat V_{\mathrm{IPS}}(\pi)-V(\pi)
|
\le
\frac1\eta
\sqrt{
\frac{
\log(2/\delta)
}{
2n
}
}.
}
$$

### Proof

Each importance-weighted reward lies in:

$$
[0,1/\eta].
$$

Apply Hoeffding.

 $\square$

Small propensity support increases estimation cost.

---

# 17. IPS variance debt

If:

$$
\eta
$$

is tiny, the estimator can have large variance.

This is why "technically nonzero exploration" can still be practically inadequate.

---

# 18. Doubly robust boundary

Doubly robust policy evaluation combines:

- reward/capability model;
- inverse propensity correction.

It can remain consistent if either component is sufficiently correct under its classical assumptions.

GVSS treats it as prior statistical machinery.

---

# 19. New-provider cold start

New provider:

$$
\nu_{\mathrm{new}}.
$$

No direct observations:

$$
N(\nu_{\mathrm{new}},\theta)=0.
$$

---

# 20. GVSS10-N4 — Zero-exposure cold-start non-identifiability

## Proposition GVSS10-N4

Without structural transfer assumptions, a provider receiving no actions in a task region has unidentifiable reward distribution there from routing logs alone.

### Proof

Construct two worlds identical on every observed provider outcome but assigning different unobserved rewards to the new provider.

 $\square$

---

# 21. Metadata prior is not empirical identification

Provider description, architecture, benchmark card, or same-family similarity can create:

$$
P(
\mathcal C_{\mathrm{new}}
)
$$

as a prior.

It does not equal same-task empirical evidence.

---

# 22. Cold-start grid calibration

Discretize task space into:

$$
L
$$

cells.

There are:

$$
N
$$

providers.

---

# 23. GVSS10-T3 — Uniform cold-start calibration certificate

## Theorem GVSS10-T3

If rewards lie in $[0,1]$ and every provider-task cell receives $m$ independent calibration samples, then with probability at least:

$$
1-\delta
$$

all empirical cell means satisfy error at most $\epsilon$ whenever:

$$
\boxed{
m
\ge
\frac{
\log(
2NL/\delta
)
}{
2\epsilon^2
}.
}
$$

### Proof

Hoeffding per provider-cell pair plus union bound over $NL$ pairs.

 $\square$

This is a baseline, not a scalable high-dimensional solution.

---

# 24. Capability estimation error

Suppose:

$$
\boxed{
|
\widehat{\mathcal C}_\nu(\theta)
-
\mathcal C_\nu(\theta)
|
\le
\varepsilon_\nu(\theta).
}
$$

---

# 25. GVSS10-T4 — Greedy capability-routing regret bound

## Theorem GVSS10-T4

Let:

$$
\nu^\star
\in
\arg\max_\nu
\mathcal C_\nu(\theta),
$$

and estimated-capability router choose:

$$
\widehat\nu
\in
\arg\max_\nu
\widehat{\mathcal C}_\nu(\theta).
$$

Then:

$$
\boxed{
\mathcal C_{\nu^\star}(\theta)
-
\mathcal C_{\widehat\nu}(\theta)
\le
\varepsilon_{\nu^\star}(\theta)
+
\varepsilon_{\widehat\nu}(\theta).
}
$$

### Proof

$$
\begin{aligned}
\mathcal C_{\nu^\star}
-
\mathcal C_{\widehat\nu}
&\le
[
\widehat{\mathcal C}_{\nu^\star}
+
\varepsilon_{\nu^\star}
]
-
[
\widehat{\mathcal C}_{\widehat\nu}
-
\varepsilon_{\widehat\nu}
]
\\
&\le
\varepsilon_{\nu^\star}
+
\varepsilon_{\widehat\nu},
\end{aligned}
$$

because:

$$
\widehat{\mathcal C}_{\widehat\nu}
\ge
\widehat{\mathcal C}_{\nu^\star}.
$$

 $\square$

---

# 26. Uniform error corollary

If:

$$
\varepsilon_\nu(\theta)\le\epsilon
$$

for all providers:

$$
\boxed{
r(\theta)\le2\epsilon.
}
$$

---

# 27. Cumulative oracle regret

## Definition GVSS10-D7

$$
\boxed{
\operatorname{Reg}_T
=
\sum_{t=1}^T
[
\mathcal C_{\nu_t^\star}(\theta_t)
-
\mathcal C_{A_t}(\theta_t)
].
}
$$

---

# 28. GVSS10-C1 — Estimation-error cumulative routing regret

For the greedy estimated-capability router:

$$
\boxed{
\operatorname{Reg}_T
\le
\sum_{t=1}^T
[
\varepsilon_{\nu_t^\star}(\theta_t)
+
\varepsilon_{A_t}(\theta_t)
].
}
$$

Immediate from GVSS10-T4.

---

# 29. Exploration policy

A router should sometimes choose a provider because its capability is uncertain, not because its current posterior mean is highest.

---

# 30. Optimistic routing

Engineering form:

$$
\boxed{
A_t
=
\arg\max_\nu
[
\widehat{\mathcal C}_\nu(\theta_t)
+
\beta_t\sigma_\nu(\theta_t)
].
}
$$

No universal regret theorem is claimed without specifying the function class/noise model.

---

# 31. Thompson-style routing

Sample one plausible capability function from the posterior and route to its maximizing provider.

This is classical posterior-sampling logic.

---

# 32. Exploration floor

During capability maintenance:

$$
\boxed{
\mu_t(\nu\mid\theta)
\ge
\eta_{\nu,\theta}.
}
$$

This supports off-policy evaluation and prevents provider starvation.

---

# 33. GVSS10-N5 — Provider starvation can self-lock capability estimates

If after some time provider B is never selected in region $C$, no new direct reward samples from B in $C$ arrive.

A pessimistic estimate can therefore persist without opportunity for falsification.

This is an epistemic self-locking mechanism.

---

# 34. Exploration has cost

Exploring a weak provider can reduce current image quality or increase cost.

Therefore routing solves:

$$
\boxed{
\text{exploration value}
-
\text{current routing loss}.
}
$$

This is the classical bandit tradeoff.

---

# 35. Cost-aware routing utility

Define:

$$
\boxed{
\mathcal C_\nu^\lambda(\theta)
=
E[
Q_\nu(\theta)
-
\lambda C_\nu(\theta)
].
}
$$

The oracle provider depends on:

$$
\lambda.
$$

---

# 36. Multi-metric routing

Instead of scalar utility, require Pareto admissibility:

$$
\boxed{
\mathbf C_\nu(\theta)
=
(
Q,
A,
S,
C,
-L,
-K
).
}
$$

The router can filter to nondominated providers and apply project-specific policy.

---

# 37. RouteT2I relevance

RouteT2I predicts multiple quality dimensions from prompt tokens and uses Pareto relative superiority to route edge/cloud models under cost constraints.

This is a direct current precedent for multi-metric provider selection.

---

# 38. Cost-Aware Routing relevance

Cost-Aware Routing learns a cost-aware router over multiple pre-trained T2I generation functions/models and explicitly conditions routing on prompt complexity.

This is a direct current precedent for task-conditioned provider routing.

---

# 39. HADIS relevance

HADIS jointly optimizes prompt routing, cascade configuration, and resource allocation.

GVSS-10's provider cost/latency features fit directly into this serving context.

---

# 40. OctoT2I relevance

OctoT2I learns a capability knowledge base through self-evolving exploration and stateful multi-round routing.

This is especially close to GVSS capability learning.

GVSS-10 focuses on statistical selection bias, exploration coverage, attribution, and provider-version provenance.

---

# 41. Historical routing bias

Suppose capability model is trained only with standard supervised regression on:

$$
(\theta_t,A_t,R_t)
$$

without modeling:

$$
\mu_t(A_t\mid\theta_t).
$$

The learned model may encode the logging policy's provider-context assignment.

This is especially dangerous when providers receive systematically different task difficulty.

---

# 42. Randomized calibration traffic

A small randomized calibration stream provides:

- overlap;
- propensity known exactly;
- counter-bias evidence;
- new-provider exposure.

This can be separated from production exploitation traffic.

---

# 43. Calibration traffic fraction

Let:

$$
\epsilon_{\mathrm{cal}}
$$

be fraction of tasks reserved for controlled provider exploration.

This is a direct quality/cost versus identifiability tradeoff.

---

# 44. Routing logs

The capability learner must preserve selection probabilities.

If a router changes policy version, log:

$$
\boxed{
\mu_t
}
$$

or enough information to reconstruct it.

---

# 45. Deterministic routing problem

A deterministic historical router has propensity 1 for selected provider and 0 for all others.

This creates support violations for counterfactual providers.

Off-policy evaluation cannot recover the missing values without extra assumptions/data.

---

# 46. Cross-domain transfer

Recent contextual-bandit work studies cross-domain off-policy evaluation to borrow source-domain logs under limited target overlap.

This may be relevant for new providers or new visual task regions.

Transfer assumptions must be explicit.

---

# 47. Conditional fallback reliability

After provider A fails, the task distribution is no longer the unconditional task distribution.

The failure itself is evidence about task difficulty.

---

# 48. GVSS10-T5 — Conditional fallback value

Suppose after A fails, provider B succeeds with probability:

$$
p_{B\mid A,\theta}.
$$

Successful B avoids loss:

$$
L>0.
$$

Trying B costs:

$$
c_B.
$$

Then trying B has positive one-step expected value iff:

$$
\boxed{
p_{B\mid A,\theta}
>
c_B/L.
}
$$

### Proof

Expected avoided loss is:

$$
p_{B\mid A,\theta}L.
$$

Subtract $c_B$.

 $\square$

The marginal success rate of B is not the correct quantity after A has failed.

---

# 49. Positive common-mode failure

If:

$$
P(B\text{ fails}\mid A\text{ fails},\theta)
>
P(B\text{ fails}\mid\theta),
$$

then:

$$
P(B\text{ succeeds}\mid A\text{ fails},\theta)
<
P(B\text{ succeeds}\mid\theta).
$$

Naive fallback estimates overstate recovery.

---

# 50. Sequential provider state

After each provider attempt:

$$
H_t^{\mathrm{route}}
$$

includes:

- task;
- provider;
- generated image;
- score;
- failure type;
- cost;
- latency.

Router state should update before selecting fallback.

---

# 51. Higher-order common cause

For more than two providers, fallback value can depend on:

- previous provider failures;
- shared evaluator;
- shared model family;
- common infrastructure.

Pairwise unconditional statistics are insufficient, as GVSS-09 showed.

---

# 52. Multi-stage provider path

## Definition GVSS10-D8

$$
\boxed{
p
=
(
\nu_1,
a_1,
\nu_2,
a_2,
\ldots,
\nu_m
).
}
$$

The path can include generation, edit, repair, evaluation, and upscaling providers.

---

# 53. Path capability

$$
\boxed{
\mathcal C_p(\theta)
=
E[
R_{\mathrm{final}}
\mid
\theta,p
].
}
$$

This is identifiable from sufficiently supported path-level data even when individual stage contribution is not.

---

# 54. GVSS10-N6 — Final reward alone does not identify stage contribution

## Counterexample

Observed path:

$$
A\to B
$$

always returns final reward:

$$
1.
$$

World 1:

$$
\text{A contributes }1,\quad
\text{B contributes }0.
$$

World 2:

$$
\text{A contributes }0,\quad
\text{B contributes }1.
$$

The observable final reward law is identical.

Therefore provider-stage contribution is not identified by final reward alone.

 $\square$

---

# 55. Attribution requires interventions or structure

Possible additional data:

- intermediate score before/after each stage;
- stage ablation;
- provider substitution;
- replay from checkpoint;
- coalition/path evaluation;
- causal structural model.

---

# 56. Shapley boundary

If a well-defined coalition value:

$$
v(S)
$$

is available, Shapley values give one classical contribution allocation satisfying standard axioms.

In ordered nonlinear pipelines, coalition values may be expensive or ill-defined.

Recent work on multi-agent semantic contribution also studies attribution beyond naive final-score decomposition.

GVSS-10 does not prescribe Shapley attribution universally.

---

# 57. Multi-stage provenance

Store every provider-stage identity.

Without this, routing learner may credit the final provider for gains introduced by earlier stages.

---

# 58. Intermediate evaluation

If:

$$
R_j
$$

is recorded after each stage, marginal observed improvement:

$$
R_j-R_{j-1}
$$

is a descriptive stage delta.

It is not automatically a causal contribution because later/earlier interactions may matter.

---

# 59. Provider version

Capability is version indexed:

$$
\boxed{
\mathcal C_{\nu,v}(\theta).
}
$$

A provider update creates a new capability object unless transfer is validated.

---

# 60. Drift calibration cell

Fix provider $\nu$ and task region/cell $C$.

Collect old/new bounded rewards.

---

# 61. GVSS10-T6 — Capability-drift rejection certificate

## Theorem GVSS10-T6

Let:

$$
R\in[0,1].
$$

Old/new means:

$$
c_0,c_1.
$$

Empirical means from independent samples:

$$
\widehat c_0,\widehat c_1
$$

with sizes:

$$
n_0,n_1.
$$

Define:

$$
\boxed{
r(n,\delta)
=
\sqrt{
\frac{
\log(4/\delta)
}{
2n
}
}.
}
$$

With probability at least:

$$
1-\delta,
$$

$$
\boxed{
|
[
\widehat c_1-\widehat c_0
]
-
[
c_1-c_0
]
|
\le
r(n_0,\delta)
+
r(n_1,\delta).
}
$$

Therefore if:

$$
\boxed{
|
\widehat c_1-\widehat c_0
|
>
r(n_0,\delta)
+
r(n_1,\delta),
}
$$

then:

$$
c_1\neq c_0
$$

on the high-probability event.

### Proof

Hoeffding on both means plus union bound and triangle inequality.

 $\square$

---

# 62. Drift can be local

Provider may drift only on:

- typography tasks;
- long prompts;
- specific styles;
- safety-sensitive content.

Use task-conditioned drift tests.

---

# 63. Router retraining trigger

A behaviorally significant drift detection should:

1. mark capability cells stale;
2. increase exploration;
3. retrain/recalibrate capability model;
4. preserve old version;
5. compare routing regret before/after.

---

# 64. Model retraining is not always needed

If drift occurs in a task region never used by the project, current router decision may remain stable.

Retraining priority should be weighted by task-distribution importance.

---

# 65. Capability region

## Definition GVSS10-D9

$$
\boxed{
\Theta_\nu^\star
=
\{
\theta:
\nu
\in
\arg\max_j
\mathcal C_j(\theta)
\}.
}
$$

These regions can overlap under ties.

---

# 66. Capability frontier

For vector capability, define provider Pareto region:

$$
\boxed{
\Theta_\nu^{\mathrm{Pareto}}
=
\{
\theta:
\mathbf C_\nu(\theta)
\text{ is nondominated}
\}.
}
$$

---

# 67. Router goal

The router should learn:

- provider capability regions;
- uncertainty;
- costs;
- failure dependence;
- version drift.

Not one global model score.

---

# 68. Capability map

A practical capability database can store:

```text
task_cell
provider
provider_version
sample_count
mean_quality
mean_cost
mean_latency
failure_rate
confidence
routing_propensity_coverage
last_calibrated
```

---

# 69. Capability map must record counterfactual support

For each task-provider cell:

```text
support_status:
  randomized
  observed_nonrandom
  transferred
  unsupported
```

This tells the router how much of the capability map is directly identified.

---

# 70. Selection-bias audit

For each provider compare:

- task distribution routed to provider;
- global task distribution.

Large discrepancy signals that raw provider averages are not directly comparable.

---

# 71. Propensity audit

Track:

$$
\boxed{
\eta_{\min}
=
\min_{
\theta,\nu
\text{ relevant}
}
\mu(\nu\mid\theta).
}
$$

Small $\eta_{\min}$ predicts high IPS variance.

---

# 72. Off-policy evaluation boundary

Off-policy estimators can evaluate candidate routing policies from logged data.

They do not create information for unsupported provider-task pairs.

No estimator defeats a true support violation without assumptions/transfer.

---

# 73. New-provider prior

A prior capability model may use:

- architecture;
- public benchmark;
- provider description;
- same-family version;
- zero-shot task embeddings.

The runtime should mark it as:

```text
prior_only
```

until direct exploration occurs.

---

# 74. Cold-start exploration value

New provider uncertainty is valuable only if there is plausible upside.

A terrible prior plus high exploration cost may justify little traffic.

A promising but uncertain provider may justify active calibration.

This is a Bayesian exploration decision.

---

# 75. Exploration quota

A simple engineering rule:

$$
\boxed{
N_t(\nu,C)
\ge
m_{\min}
}
$$

before declaring provider incapable in cell $C$.

This is not a universal theorem.

---

# 76. Capability extrapolation

A function approximator can infer nearby task regions.

But this introduces representation assumptions:

$$
\theta
\approx\theta'
\Longrightarrow
\mathcal C_\nu(\theta)
\approx
\mathcal C_\nu(\theta').
$$

This smoothness must be validated.

---

# 77. Task representation drift

If the task encoder $\phi$ changes, old capability map coordinates may not be directly comparable.

Version the task representation.

---

# 78. RRT relation

This is another representation-normalization problem.

Provider capability is defined relative to:

- task representation;
- evaluator;
- utility;
- provider version.

None is globally intrinsic.

---

# 79. Routing utility provenance

Store:

```text
utility_function_version
metric_weights
hard_constraints
cost_exchange_rate
latency_penalty
```

Changing the scalarization can change the oracle provider even if provider behavior is fixed.

---

# 80. Multi-objective route

If no scalar utility is acceptable, route by:

1. hard feasibility;
2. Pareto filtering;
3. user/project preference.

---

# 81. Budgeted routing

Provider $\nu$ is feasible only if:

$$
K_\nu(\theta)\le B_t.
$$

The oracle becomes:

$$
\boxed{
\nu^\star_B(\theta)
\in
\arg\max_{
\nu:
K_\nu(\theta)\le B_t
}
\mathcal C_\nu(\theta).
}
$$

---

# 82. Route plus fallback

A routing action can be a sequence policy:

$$
\boxed{
\pi:
\theta
\to
(
\nu_1,
\nu_2\mid F_{\nu_1},
\nu_3\mid F_{\nu_1},F_{\nu_2},
\ldots
).
}
$$

This is more than a one-shot contextual bandit.

It becomes a sequential decision problem.

---

# 83. Sequential routing regret

Oracle can choose optimal fallback tree.

Comparing against it requires a full MDP/POMDP regret definition.

GVSS-10 keeps the clean oracle regret theorem for one-step routing.

---

# 84. Shared evaluator bias

If provider capability labels are produced by one biased evaluator, router can learn the evaluator's preference rather than human/project value.

Evaluator version is therefore part of capability model provenance.

---

# 85. Human acceptance

Human project approval can be one downstream reward.

But human labels can be sparse and selection biased too.

Log when human review was requested.

---

# 86. Accepted output reward

Final acceptance can combine:

- hard gates;
- metric vector;
- human approval;
- project-specific cost.

The capability model should not silently treat evaluator score as true reward.

---

# 87. Current OctoT2I self-evolving knowledge base

OctoT2I's PSEL loop autonomously explores conceptual dimensions and tool capability frontiers.

GVSS-10's exploration/support perspective supplies one statistical caution:

> capability knowledge should distinguish explored evidence from self-generated extrapolation.

---

# 88. Current cross-domain OPE relevance

2026 cross-domain off-policy work directly targets few-shot, deterministic-logging, and new-action settings by borrowing logged data from source domains.

This is a promising neighboring direction for provider cold start.

GVSS requires explicit transfer assumptions/version provenance when using it.

---

# 89. OPE beyond overlap

Partial-identification methods can bound policy value when overlap fails under additional weak assumptions.

Thus "not point identifiable" does not always mean "nothing can be said."

GVSS-10 uses the stronger warning:

> do not report unsupported point estimates as identified capability.

---

# 90. Capability confidence

For each provider/task region report:

$$
\boxed{
(
\widehat{\mathcal C},
\text{interval},
N,
\text{support status}
).
}
$$

---

# 91. Routing confidence

If top provider lower confidence bound exceeds all others' upper bounds:

$$
\boxed{
LCB_{\nu^\star}(\theta)
>
\max_{\nu\neq\nu^\star}
UCB_\nu(\theta),
}
$$

the provider choice is confidence-separated.

This is analogous to the robust action-margin theorem of GVSS-08.

---

# 92. GVSS10-T7 — Confidence-separated provider choice

## Theorem GVSS10-T7

Suppose true capabilities satisfy:

$$
\mathcal C_\nu(\theta)
\in
[
L_\nu(\theta),
U_\nu(\theta)
]
$$

for all providers.

If some provider $a$ satisfies:

$$
\boxed{
L_a(\theta)
>
\max_{b\neq a}
U_b(\theta),
}
$$

then:

$$
\boxed{
a
}
$$

is the unique optimal provider for every capability vector inside the intervals.

### Proof

For every $b\neq a$:

$$
\mathcal C_a
\ge
L_a
>
U_b
\ge
\mathcal C_b.
$$

 $\square$

No exploration is decision-necessary for this one-step task if the intervals are trusted and the objective is fixed.

---

# 93. Exploration region

If provider confidence intervals overlap near the decision boundary, additional provider probes can change routing.

This is where exploration has direct decision value.

---

# 94. Router self-evolution

A self-evolving router updates:

$$
\widehat{\mathcal C}_{\nu,t}
$$

and routing policy:

$$
\pi_t.
$$

Because policy changes data collection, learning is reflexive.

---

# 95. Routing-policy provenance

Each capability training row should record the policy that caused it to be observed.

Otherwise future users cannot reconstruct selection bias.

---

# 96. Multi-stage attribution provenance

Each final image should reference all providers that contributed to it.

Do not attach final reward only to the terminal provider.

---

# 97. Capability attribution status

For each provider contribution claim label:

```text
direct_single_stage
path_level
intermediate_delta
counterfactual_ablation
shapley_or_game_rule
model_inferred
unknown
```

---

# 98. Routing benchmark

A GVSS-10 benchmark should contain:

- task contexts;
- provider potential reward table;
- cost/latency;
- logging policy;
- propensity;
- provider drift event;
- cold-start provider;
- multi-stage path tasks.

This allows exact oracle regret.

---

# 99. Benchmark 1 — selection bias reversal

Use the easy/hard example.

A correct learner should not rank A over B from raw means.

---

# 100. Benchmark 2 — support violation

Never route provider B in one task cell.

A correct system should mark capability there:

```text
unsupported
```

rather than point-estimated from logs.

---

# 101. Benchmark 3 — exploration

Start with pessimistic prior on best provider.

Compare greedy router against exploration-aware router.

Measure whether provider starvation causes persistent regret.

---

# 102. Benchmark 4 — cold start

Add new provider midway.

Measure:

- calibration cost;
- discovery delay;
- regret;
- propensity coverage.

---

# 103. Benchmark 5 — drift

Change provider capability in one task cell.

Measure detection and retraining delay.

---

# 104. Benchmark 6 — multi-stage attribution

Construct known two-stage contribution mechanisms.

Evaluate whether attribution method recovers only what its data identify.

---

# 105. Routing Pareto vector

Define:

$$
\boxed{
\mathbf C_{\mathrm{route}}
=
(
-\text{quality},
\text{cost},
\text{latency},
\text{regret},
\text{exploration debt},
\text{support debt},
\text{failure risk},
\text{provenance debt}
).
}
$$

---

# 106. GVSS10-T8 — Routing Pareto necessity

## Theorem GVSS10-T8

Every optimum of a scalar objective strictly increasing in all declared routing costs/risks and strictly decreasing in all declared benefits lies on the routing Pareto frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 107. What is classical / neighboring

GVSS-10 does not claim as inventions:

- contextual bandits;
- exploration versus exploitation;
- IPS;
- doubly robust policy evaluation;
- off-policy evaluation;
- support/positivity requirements;
- UCB/Thompson-style routing;
- propensity logging;
- Shapley attribution;
- model routing;
- edge/cloud routing;
- multi-model serving.

---

# 108. Candidate GVSS-specific synthesis

Subject to broader literature audit, the GVSS-specific synthesis is:

1. treating image-provider capability as a task-conditioned function over the GVSS task/visual regime rather than a global model score;
2. making routing-selection bias and propensity support first-class provider-capability governance;
3. connecting provider starvation directly to unsupported reachable/capability regions;
4. integrating cold-start provider calibration with GVSS portfolio learning;
5. linking capability-estimation uncertainty to visual routing regret;
6. conditioning fallback value on previous provider failures/common-mode structure;
7. separating path-level capability from provider-stage causal attribution;
8. versioning capability drift and task representation alongside provider identity;
9. requiring routing-policy propensity and provider lineage in every capability-learning artifact.

No strong novelty claim is made in v0.1.

---

# 109. What GVSS-10 proves

Under explicit hypotheses, GVSS-10 proves:

1. routed historical means can reverse the true provider ranking under task-selection bias;
2. unsupported target provider actions are not distribution-free point identifiable from logged bandit feedback;
3. IPS is unbiased under correct logging propensities and support;
4. IPS has the stated Hoeffding concentration bound under a positive propensity floor;
5. zero provider exposure cannot empirically identify its task-region capability without transfer assumptions;
6. uniform cold-start cell calibration obtains the stated simultaneous Hoeffding guarantee;
7. provider-selection regret from estimated capabilities is bounded by the estimation errors of the oracle and selected providers;
8. cumulative one-step oracle regret inherits the sum of those estimation errors;
9. fallback after a primary failure is worthwhile according to the conditional fallback success probability, not its marginal success rate;
10. final reward from a multi-stage provider path does not identify individual stage contribution without extra assumptions/interventions;
11. provider capability drift in a fixed task cell can be detected with the stated two-sample Hoeffding certificate;
12. confidence-separated provider intervals certify a unique provider decision;
13. every strictly monotone scalar routing optimum lies on the routing Pareto frontier.

---

# 110. What GVSS-10 does not prove

It does not prove:

- a particular task representation is sufficient;
- provider capability is stationary across versions;
- IPS is low variance when propensities are small;
- cold-start calibration grid scales to high-dimensional prompt spaces;
- any specific UCB/Thompson router achieves a regret bound without further model assumptions;
- pairwise failure statistics suffice for sequential fallback trees;
- final-image reward can uniquely identify provider-stage causal contribution;
- a Shapley attribution is the unique correct explanation of multi-stage contribution;
- evaluator-based reward equals human/project utility;
- cross-domain off-policy transfer is valid without explicit domain assumptions;
- exploration traffic is always worth its immediate quality/cost loss.

---

# 111. Proposed GVSS-11

The next paper should move from routing providers to **multi-stage cross-provider composition geometry**.

Proposed title:

$$
\boxed{
\textbf{
GVSS-11 — Compositional Visual Reachability Graphs and Cross-Provider Transformation Paths
}
}
$$

Chinese:

**組合式視覺可達圖與跨生成器轉換路徑：生成、編輯、修復與升頻的多階段幾何**

Main questions:

1. When does cross-provider composition reach states outside provider union?
2. How should provider edges be typed by input/output compatibility?
3. What is shortest-cost path to a target visual region?
4. How do transformation defects accumulate along provider paths?
5. How should lineage constrain attribution?
6. When is one provider path dominated by another?
7. Can cycles in editing workflows create useful reachability or only debt?
8. How should routing and composition be jointly optimized?

---

# 112. References

1. Qinchan Li, Kenneth Chen, Changyue Su, Wittawat Jitkrittum, Qi Sun, Patsorn Sangkloy, **Cost-Aware Routing for Efficient Text-To-Image Generation**, arXiv:2506.14753, 2025.
2. Zewei Xin, Qinya Li, Chaoyue Niu, Fan Wu, **Edge-Cloud Routing for Text-to-Image Model with Token-Level Multi-Metric Prediction**, arXiv:2411.13787, 2024.
3. Qizheng Yang, Tung-I Chen, Siyu Zhao, Ramesh K. Sitaraman, Hui Guan, **HADIS: Hybrid Adaptive Diffusion Model Serving for Efficient Text-to-Image Generation**, arXiv:2509.00642, 2025.
4. Xu Jiang et al., **OctoT2I: A Self-Evolving Agentic Text-to-Image Router**, arXiv:2606.01803, 2026.
5. Miroslav Dudík, John Langford, Lihong Li, **Doubly Robust Policy Evaluation and Learning**, arXiv:1103.4601.
6. Yu-Xiang Wang, Alekh Agarwal, Miroslav Dudík, **Optimal and Adaptive Off-policy Evaluation in Contextual Bandits**, arXiv:1612.01205.
7. Yuta Natsubori, Masataka Ushiku, Yuta Saito, **Cross-Domain Off-Policy Evaluation and Learning for Contextual Bandits**, arXiv:2607.22012, 2026.
8. Pengyi Jiang, Xiaoguang Zhu, Quanyan Zhu, **Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems**, arXiv:2607.18255, 2026.
9. GVSS-01 through GVSS-09, internal series artifacts, 2026.
10. RRT-20, **Reflexive Representation Theory: Unified Closure, Meta-Theorems, Limits, and Research Program**, internal series artifact, 2026.

---

# 113. Conclusion

GVSS-09 defines the provider portfolio.

GVSS-10 turns that portfolio into an adaptive routing problem.

The key capability object is:

$$
\boxed{
\mathcal C_\nu(\theta)
=
E[
U
\mid
\theta,\nu
].
}
$$

The router must learn it from bandit feedback created by its own past decisions.

Therefore the data are not neutral.

A provider that was routed easy tasks can look artificially strong.

A provider that was routed hard tasks can look artificially weak.

A provider never routed into one region is unsupported there.

Logging propensity is therefore part of scientific provenance.

Under overlap, IPS and doubly robust methods can correct historical routing bias.

Without overlap, point capability can be unidentifiable.

Cold-start providers need exploration.

Capability uncertainty translates directly into routing regret.

Fallback value depends on the conditional success probability after previous provider failures, not marginal provider quality.

And multi-stage final rewards identify the provider path more readily than individual causal contribution.

The canonical GVSS-10 principle is:

$$
\boxed{
\textbf{
A visual router learns from the traffic it creates.
Therefore provider capability estimates are inseparable from the policy that decided which provider was allowed to be observed.
}
}
$$

This turns provider routing from a leaderboard lookup into a reflexive statistical learning problem.

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
