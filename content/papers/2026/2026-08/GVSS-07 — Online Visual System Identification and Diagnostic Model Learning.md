# GVSS-07 — Online Visual System Identification and Diagnostic Model Learning
## 線上視覺系統辨識與診斷模型學習：失敗注入、轉移辨識、版本漂移與不確定性回饋

**Series:** Global Visual Space & Generative Navigation — Paper 07  
**Bridge:** GVSS × frozen Reflexive Representation Theory (RRT)  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal system-identification paper. Controlled-row concentration, direct identifiability under labeled failure injection, latent-state non-identifiability, minimax sample allocation, synthetic-to-real diagnostic transfer, provider-version stationarity tests, pooling-bias no-go, one-step belief robustness from estimated transition/observation kernels, robust Bellman certification, finite-horizon model-error propagation, and self-confirming pseudo-label no-go statements are proved under the stated hypotheses. System identification, active input design, POMDP/world-model learning, Bayesian parameter estimation, active exploration, and change-point detection are established prior research and are not claimed as GVSS inventions. No strong novelty claim is made.

**Keywords:** visual system identification, diagnostic model learning, controlled failure injection, POMDP learning, active system identification, evaluator calibration, provider drift, visual generation agent, transition model, observation model, GVSS

---

# Abstract

GVSS-06 formulated diagnostic visual control using a hidden failure state

$$
F_t\in\mathcal F
$$

with action-dependent transition kernel

$$
\boxed{
T_a(k'\mid k)
=
P(F_{t+1}=F_{k'}\mid F_t=F_k,a_t=a)
}
$$

and diagnostic observation kernel

$$
\boxed{
Q_a(y\mid k)
=
P(Y_t=y\mid F_t=F_k,a_t=a).
}
$$

That controller was formally well-defined only because these kernels were treated as known. Real image-generation systems do not provide them.

GVSS-07 therefore moves from **diagnostic control** to **diagnostic system identification**.

The central object is a versioned diagnostic model

$$
\boxed{
\mathcal M_\nu
=
(\mathcal F,\mathcal A,\mathcal Y,T_\nu,Q_\nu,\mathcal U_\nu,\mathsf{Prov}_\nu),
}
$$

where $\nu$ identifies the exact visual-runtime version, $\mathcal U_\nu$ records uncertainty/confidence sets, and $\mathsf{Prov}_\nu$ records the data, failure injections, labels, provider/model/evaluator/compiler versions, and fitting procedure.

GVSS-07 distinguishes two identification regimes.

## Regime A — controlled failure injection / independent labels

A known failure state can be deliberately created or independently labeled. Examples include contradictory hard constraints, deliberate deletion of a compiled requirement, evaluator corruption, finite toy-provider support, independently supplied latent-intent labels, and human/auditor labels on historical traces.

In this regime, rows of $T_a$ and $Q_a$ are ordinary categorical distributions and can be estimated directly.

Let

$$
K=|\mathcal F|,
\qquad
A=|\mathcal A|,
\qquad
M=|\mathcal Y|.
$$

For observation row $(a,k)$, with $n^Q_{a,k}$ independent labeled samples,

$$
\widehat Q_a(y\mid k)
=
\frac{N^Q_{a,k,y}}{n^Q_{a,k}}.
$$

With probability at least $1-\delta$, simultaneously over all $a,k,y$,

$$
\boxed{
|\widehat Q_a(y\mid k)-Q_a(y\mid k)|
\le
\sqrt{
\frac{\log(2AKM/\delta)}{2n^Q_{a,k}}
}.
}
$$

For transition row $(a,k)$, with independently labeled post-action state and $n^T_{a,k}$ samples,

$$
\boxed{
|\widehat T_a(k'\mid k)-T_a(k'\mid k)|
\le
\sqrt{
\frac{\log(2AK^2/\delta)}{2n^T_{a,k}}
}
}
$$

simultaneously over all $a,k,k'$ with probability at least $1-\delta$.

These are Hoeffding/union-bound certificates, not new concentration theory.

## Regime B — latent failure model learning

In deployment, failure state is usually hidden. The runtime observes actions, reports, images, scores, lineage, and perhaps human corrections. Then $T$ and $Q$ can be non-identifiable.

A minimal no-go is immediate. If two hidden failure states satisfy

$$
\boxed{
Q_a(\cdot\mid F_1)=Q_a(\cdot\mid F_2)=q_a
\quad\forall a,
}
$$

then observations are independent of which hidden state is active. Arbitrarily different transition families $T$ and $\widetilde T$ generate the same report law under every action policy. Therefore hidden dynamics cannot be recovered from reports alone.

This is the system-identification version of GVSS-05 diagnostic equivalence.

## Active identification

Identification data should not be collected blindly when controlled experiments are available. Let $i=(a,k)$ index identifiable rows and let $w_i>0$ be downstream importance. For a Hoeffding-like uncertainty proxy $w_i/\sqrt{n_i}$, consider

$$
\min_{n_i>0,\ \sum_i n_i=N}
\max_i\frac{w_i}{\sqrt{n_i}}.
$$

The continuous minimax allocation is

$$
\boxed{
n_i^*=N\frac{w_i^2}{\sum_jw_j^2},
}
$$

with optimal worst weighted uncertainty

$$
\boxed{
\sqrt{\frac{\sum_jw_j^2}{N}}.
}
$$

Thus important underidentified failure/action rows should receive more calibration effort.

## Synthetic failure injection and transfer

Controlled injection gives labels, not automatic realism. Let $Q_{\rm syn}$ and $Q_{\rm real}$ be diagnostic report laws for a declared failure under synthetic and real episodes. If

$$
\operatorname{TV}(Q_{\rm syn},Q_{\rm real})\le\eta,
$$

then for every bounded diagnostic loss $0\le\ell\le L$,

$$
\boxed{
|E_{\rm syn}\ell-E_{\rm real}\ell|\le L\eta.
}
$$

Without a domain-gap assumption, perfect synthetic diagnosis can be arbitrarily wrong in real deployment.

## Version drift

A diagnostic model must be indexed by exact runtime version. Let $q^{(0)}$ and $q^{(1)}$ be one categorical diagnostic row before and after an update. From independent labeled samples of sizes $n_0,n_1$, define

$$
r(n,\delta)=\sqrt{\frac{\log(4M/\delta)}{2n}}.
$$

With probability at least $1-\delta$,

$$
\boxed{
\max_y
|[\widehat q^{(0)}(y)-\widehat q^{(1)}(y)]-[q^{(0)}(y)-q^{(1)}(y)]|
\le
r(n_0,\delta)+r(n_1,\delta).
}
$$

So if the empirical maximum coordinate gap is larger than that confidence sum, stationarity $q^{(0)}=q^{(1)}$ is rejected on the high-probability event.

Pooling genuinely different versions creates a mixture. With long-run proportions $\lambda$ and $1-\lambda$,

$$
\boxed{
q_{\rm pool}=\lambda q^{(0)}+(1-\lambda)q^{(1)}.
}
$$

In general this equals neither version.

## Identification uncertainty returns to control

Suppose for action $a$:

$$
\sup_k\operatorname{TV}(T_a(\cdot\mid k),\widehat T_a(\cdot\mid k))\le\varepsilon_T,
$$

and for the observed diagnostic report $y$:

$$
\sup_k|Q_a(y\mid k)-\widehat Q_a(y\mid k)|\le\varepsilon_Q.
$$

If the true evidence probability satisfies $Z\ge\zeta>0$, then the exact and approximate posteriors obey

$$
\boxed{
\operatorname{TV}(b^{a,y},\widehat b^{a,y})
\le
\frac{2\varepsilon_T+\varepsilon_Q}{\zeta}
}
$$

whenever $2\varepsilon_T+\varepsilon_Q<\zeta$.

Rare diagnostic reports therefore amplify model-identification error through inverse-evidence conditioning.

## Robust control

Let $\mathcal U_t$ contain plausible $(T,Q)$ pairs. A robust Bellman controller can optimize the worst-case expected cost over this uncertainty set. If the true model belongs to $\mathcal U_t$, the controller's computed worst-case value upper-bounds its true expected cost. If set coverage is at least $1-\delta$, that certificate holds with probability at least $1-\delta$.

## Horizon error

If the true and estimated one-step joint diagnostic kernels differ by at most $\epsilon$ in total variation uniformly, then under the same fixed policy a horizon- $H$ path-law discrepancy is at most

$$
\boxed{H\epsilon.}
$$

For stage cost bounded by $C_{\max}$, the expected horizon-cost difference is coarsely bounded by

$$
\boxed{H^2C_{\max}\epsilon.}
$$

A small one-step diagnostic-model error can therefore matter materially in a long iterative visual-control loop.

## Self-confirming learning

If the controller trains a new diagnostic model only on labels generated by its own current classifier, perfect pseudo-label agreement does not imply truth. For the extreme construction $F^*=1-g(X)$, a model reproducing $g(X)$ has $100\%$ pseudo-label accuracy and $0\%$ true accuracy.

Thus

$$
\boxed{
\text{self-consistency}\not\Rightarrow\text{diagnostic identification}.
}
$$

The canonical GVSS-07 principle is:

$$
\boxed{
\textbf{
The model that diagnoses visual failure must itself be identified, calibrated, versioned, and falsifiable.
A controller that learns only from labels produced by itself can become perfectly self-consistent while remaining perfectly wrong.
}
}
$$

---

# 1. Position in the GVSS sequence

GVSS-05 introduced failure diagnosis.

GVSS-06 introduced diagnostic control.

GVSS-07 identifies the model used by that controller.

The progression is

$$
\boxed{
\text{failure state}
\to
\text{failure belief}
\to
\text{control policy}
\to
\text{learned diagnostic dynamics}.
}
$$

---

# 2. Classical system-identification boundary

System identification is an established field concerned with learning system dynamics from input-output or state-transition data. Active exploration, online experiment design, partial observability, safe identification, and change-point adaptation are existing research areas.

GVSS-07 specializes these ideas to a visual-generation runtime whose latent state is a **failure mode** and whose actions are diagnostics/corrections such as RESAMPLE, RECOMPILE, REPAIR, REBIND, evaluator calibration, and human review.

---

# 3. Diagnostic model version

## Definition GVSS07-D1

A version key is

$$
\boxed{
\nu
=
(G,\text{provider},\text{model hash},\text{adapters},\Gamma,E,\Pi,\text{runtime version}).
}
$$

The exact fields are implementation-specific.

The governing rule is:

> behaviorally relevant versions are separate statistical regimes until compatibility is demonstrated.

---

# 4. Failure-state vocabulary

Use the GVSS-05 default taxonomy

$$
\mathcal F
=
\{F_s,F_c,F_\Gamma,F_\Pi,F_R,F_E,F_I\},
$$

where the labels denote sampling, constraint, compilation, search, reachability, evaluator, and intent failure.

The theory allows another finite taxonomy.

---

# 5. Action and report spaces

Let

$$
\mathcal A=\{a_1,\ldots,a_A\}
$$

and, for the finite-table theory,

$$
\mathcal Y=\{y_1,\ldots,y_M\}.
$$

Continuous reports can be binned or modeled by richer estimators; the elementary concentration theorems below use finite categorical reports.

---

# 6. Transition and observation kernels

## Definition GVSS07-D2

$$
T_a(k'\mid k)=P(F_{t+1}=F_{k'}\mid F_t=F_k,a_t=a).
$$

## Definition GVSS07-D3

$$
Q_a(y\mid k)=P(Y_t=y\mid F_t=F_k,a_t=a).
$$

These are exactly the kernels used by the GVSS-06 belief-state controller.

---

# 7. Controlled failure injection

## Definition GVSS07-D4

A controlled injection $J_k$ is a procedure that creates an episode whose ground-truth dominant failure label $F_k$ is known independently of the diagnostic model being trained.

Every injection must carry provenance.

---

# 8. Injection examples

## Constraint failure

Construct an empty hard target set.

## Compiler failure

Freeze intent, then deliberately delete or mistranslate a required structured constraint.

## Evaluator failure

Corrupt the evaluator response while preserving the generated image.

## Search failure

Use a finite benchmark in which one search policy is denied the successful route but a reference policy can reach it under the same generator binding.

## Reachability failure

Use an exact finite toy provider whose support excludes the target set.

## Intent failure

Provide the latent intended interpretation from an independent benchmark annotation.

---

# 9. Ecological-validity boundary

An injected fault can be easy to classify yet unlike real deployment failures.

Controlled labels improve internal validity.

They do not automatically provide external validity.

This motivates explicit synthetic-to-real gap testing.

---

# 10. Observation-row estimation

For known $(a,k)$, collect independent reports $Y_1,\ldots,Y_n$.

$$
\widehat Q_a(y\mid k)=\frac1n\sum_{i=1}^n\mathbf 1\{Y_i=y\}.
$$

---

# 11. GVSS07-T1 — Simultaneous observation-table concentration

With $n^Q_{a,k}\ge1$ samples for every row, with probability at least $1-\delta$,

$$
\boxed{
|\widehat Q_a(y\mid k)-Q_a(y\mid k)|
\le
r^Q_{a,k}
}
$$

for every $a,k,y$, where

$$
\boxed{
r^Q_{a,k}=\sqrt{\frac{\log(2AKM/\delta)}{2n^Q_{a,k}}}.
}
$$

### Proof

For a fixed coordinate, the indicator $\mathbf 1\{Y=y\}$ is Bernoulli. Apply Hoeffding and union bound over $AKM$ coordinates.

 $\square$

---

# 12. TV observation-row consequence

On the same event,

$$
\operatorname{TV}(\widehat Q_a(\cdot\mid k),Q_a(\cdot\mid k))
\le
\frac M2r^Q_{a,k}.
$$

This is a simple conservative conversion from coordinate error.

---

# 13. Transition-row estimation

With known pre-action failure and independently labeled post-action failure,

$$
\widehat T_a(k'\mid k)=\frac{N^T_{a,k,k'}}{n^T_{a,k}}.
$$

---

# 14. GVSS07-T2 — Simultaneous transition-table concentration

With probability at least $1-\delta$,

$$
\boxed{
|\widehat T_a(k'\mid k)-T_a(k'\mid k)|
\le
r^T_{a,k}
}
$$

for all $a,k,k'$, with

$$
\boxed{
r^T_{a,k}=\sqrt{\frac{\log(2AK^2/\delta)}{2n^T_{a,k}}}.
}
$$

### Proof

Coordinatewise Hoeffding plus a union bound over $AK^2$ coordinates.

 $\square$

---

# 15. GVSS07-T3 — Labeled-row identifiability

Assume every failure state can be independently instantiated or labeled, every action can be executed in every relevant state, post-action states/reports are observed with independent ground truth, and each row is stationary.

Then each categorical row of $T_a$ and $Q_a$ is identified by its population frequencies, and empirical frequencies converge almost surely as row sample count tends to infinity.

### Proof

Each row is an ordinary categorical law observed through independent samples. Apply the strong law coordinatewise.

 $\square$

The hard problem is not the estimator; it is trustworthy state labeling and sufficient row excitation.

---

# 16. Latent-state identification

When failure labels are hidden, the problem becomes a controlled hidden-state/POMDP identification problem.

Identifiability depends on observation separation, action excitation, structure, priors, and sometimes semantic anchors.

---

# 17. GVSS07-N1 — Hidden transition non-identifiability under identical observation rows

Let $\mathcal F=\{F_1,F_2\}$ and suppose

$$
Q_a(\cdot\mid F_1)=Q_a(\cdot\mid F_2)=q_a
$$

for every action.

Then any two transition models $T,\widetilde T$ generate the same report law under every adaptive action policy.

### Proof

Conditioned on action $a_t$, $Y_t\sim q_{a_t}$ regardless of hidden state. Hidden dynamics therefore do not affect report distributions.

 $\square$

---

# 18. Semantic label permutation

Latent-state models can also be identifiable only up to permutation. The labels $F_{\rm compile}$ and $F_{\rm eval}$ have semantic meanings, so controlled anchors/injections can be needed to attach learned hidden states to those meanings.

---

# 19. Independent labels

A label is independent for GVSS purposes if it does not arise solely from the diagnostic model being fitted.

Possible sources include synthetic injection, exact toy benchmark, human audit, causal ablation, and external adjudication.

---

# 20. GVSS07-N2 — Self-confirming pseudo-label no-go

Let current classifier output $g(X)$. Use $\widetilde F=g(X)$ as training labels and fit $\widehat g=g$.

Then pseudo-label accuracy is one. If independent truth is $F^*=1-g(X)$, true accuracy is zero.

Therefore

$$
\boxed{
\text{perfect self-label agreement}\not\Rightarrow\text{failure-model correctness}.
}
$$

 $\square$

---

# 21. Active identification

Rows are not equally important. Let $i=(a,k)$ index a row and let $w_i>0$ encode downstream importance.

Use uncertainty proxy

$$
u_i(n_i)=\frac{w_i}{\sqrt{n_i}}.
$$

---

# 22. GVSS07-T4 — Minimax active row allocation

The continuous problem

$$
\min_{n_i>0,\ \sum_i n_i=N}\max_i\frac{w_i}{\sqrt{n_i}}
$$

has solution

$$
\boxed{
n_i^*=N\frac{w_i^2}{\sum_jw_j^2}
}
$$

and optimum

$$
\boxed{
u^*=\sqrt{\frac{\sum_jw_j^2}{N}}.
}
$$

### Proof

At optimum, active weighted uncertainties equalize. Otherwise transfer sample mass from a lower-uncertainty row to a maximal row. Solve $w_i/\sqrt{n_i}=u$ together with $\sum_i n_i=N$.

 $\square$

---

# 23. Meaning of row importance

Possible weights include failure posterior frequency, wrong-action loss, Bellman sensitivity, provider-switch cost, human burden, and safety/brand impact.

The theorem does not claim these weights are intrinsic.

---

# 24. GVSS07-N3 — Unexecuted-action row is not directly empirically identified

If $n^T_{a,k}=0$, no transition frequency from $(a,k)$ has been observed.

Any estimate of $T_a(\cdot\mid k)$ then comes from prior, transfer, simulation, structural sharing, or assumption—not direct empirical identification of that row.

---

# 25. Persistent excitation analogue

A visual controller that never REBINDs cannot learn what REBIND usually does from the relevant failures. A controller that never calibrates evaluators cannot empirically learn evaluator-calibration transitions.

Active identification must sometimes spend budget on under-observed actions.

---

# 26. Synthetic-to-real transfer

Let $P_{\rm syn}$ and $P_{\rm real}$ be diagnostic distributions for a declared failure.

---

# 27. GVSS07-T5 — Bounded diagnostic transfer under TV shift

If

$$
\operatorname{TV}(P_{\rm syn},P_{\rm real})\le\eta
$$

and $0\le\ell\le L$, then

$$
\boxed{
|E_{\rm syn}\ell-E_{\rm real}\ell|\le L\eta.
}
$$

### Proof

Standard total-variation bounded-function inequality.

 $\square$

---

# 28. GVSS07-N4 — Synthetic correctness without transfer control gives no real guarantee

Take $P_{\rm syn}$ concentrated on $y=0$ and $P_{\rm real}$ concentrated on $y=1$. A diagnostic rule can be perfect synthetically and always wrong in reality.

 $\square$

---

# 29. Failure-injection provenance

Every injection record should contain at least:

```text
injection_id
failure_label
injection_mechanism
generator_version
provider_version
compiler_version
evaluator_version
search_policy
fixture_id
label_source
synthetic_or_real
```

---

# 30. Versioned diagnostic models

Never keep an unversioned global $Q,T$ table if behaviorally relevant components change.

Store:

```text
diagnostic_model_version
Q_versioned
T_versioned
confidence_or_credible_sets
sample_counts
validity_interval
provenance
```

---

# 31. Two-version diagnostic rows

Let $q^{(0)}$ and $q^{(1)}$ be one row under versions $\nu_0$ and $\nu_1$.

Collect independent labeled samples $n_0,n_1$.

---

# 32. GVSS07-T6 — Two-version stationarity rejection certificate

Define

$$
r(n,\delta)=\sqrt{\frac{\log(4M/\delta)}{2n}}.
$$

With probability at least $1-\delta$,

$$
\boxed{
\max_y|[\widehat q^{(0)}(y)-\widehat q^{(1)}(y)]-[q^{(0)}(y)-q^{(1)}(y)]|
\le r(n_0,\delta)+r(n_1,\delta).
}
$$

Hence an empirical max-coordinate gap larger than this sum certifies a nonzero population difference on the high-probability event.

### Proof

Apply Hoeffding simultaneously to all coordinates of both versions, then triangle inequality.

 $\square$

---

# 33. Transition drift

The same construction applies to each transition row with alphabet size $K$.

A provider update can change not only output quality but also the probability that actions repair or create failure modes.

---

# 34. Change-point adaptation

Production identification can use rolling windows, model resets, discounting, or explicit changepoint/situation models.

A version drift event should invalidate calibration status until rechecked.

---

# 35. Cross-version pooling

Suppose asymptotic sample fractions are $\lambda$ and $1-\lambda$ from two stationary versions.

---

# 36. GVSS07-T7 — Cross-version pooling limit

The unversioned pooled empirical law converges almost surely to

$$
\boxed{
q_{\rm pool}=\lambda q^{(0)}+(1-\lambda)q^{(1)}.
}
$$

### Proof

Apply the law of large numbers separately within each version and combine sample proportions.

 $\square$

Unless the two rows coincide or the mixture degenerates, the pooled law is not the true row of either version.

---

# 37. GVSS07-N5 — More stale data does not correct version shift

Infinite old-version data can make variance around the old law arbitrarily small while leaving bias to the new law unchanged.

Thus

$$
\boxed{
\text{more stale data}\not\Rightarrow\text{better current model}.
}
$$

---

# 38. Bayesian row estimation

For one categorical row, a Dirichlet prior is convenient:

$$
q\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_M).
$$

After counts $N_y$,

$$
q\mid D\sim\operatorname{Dirichlet}(\alpha_y+N_y)_{y=1}^M.
$$

The posterior mean is

$$
E[q_y\mid D]=\frac{\alpha_y+N_y}{\sum_j\alpha_j+n}.
$$

This is classical conjugate estimation.

---

# 39. Structural sharing

Sparse provider/action rows may share a hierarchical prior. This reduces variance only by adding a cross-row similarity assumption.

Do not treat transfer learning as free evidence.

---

# 40. Transition prediction uncertainty

For belief $b$, true predicted belief is $\mu=bT_a$ and estimated predicted belief is $\widehat\mu=b\widehat T_a$.

If every transition row is within $\varepsilon_T$ in TV, convexity gives

$$
\boxed{
\operatorname{TV}(\mu,\widehat\mu)\le\varepsilon_T.
}
$$

---

# 41. Observation uncertainty

For the observed report $y$, suppose

$$
\sup_k|Q_a(y\mid k)-\widehat Q_a(y\mid k)|\le\varepsilon_Q.
$$

---

# 42. GVSS07-T8 — Combined one-step belief robustness

Let true evidence probability be

$$
Z=\sum_k\mu_kQ_a(y\mid k)\ge\zeta>0.
$$

If

$$
2\varepsilon_T+\varepsilon_Q<\zeta,
$$

then

$$
\boxed{
\operatorname{TV}(b^{a,y},\widehat b^{a,y})
\le
\frac{2\varepsilon_T+\varepsilon_Q}{\zeta}.
}
$$

### Proof

Let $a_k=\mu_kq_k$ and $\widehat a_k=\widehat\mu_k\widehat q_k$. Then

$$
\|a-\widehat a\|_1
\le
\|\mu-\widehat\mu\|_1+\sum_k\widehat\mu_k|q_k-\widehat q_k|
\le
2\varepsilon_T+\varepsilon_Q.
$$

Normalizing two nonnegative vectors whose true mass is at least $\zeta$ gives posterior TV at most the unnormalized $L^1$ error divided by $\zeta$.

 $\square$

---

# 43. Identification conditioning debt

The controller now has three explicit sensitivity coordinates:

$$
\varepsilon_T,
\qquad
\varepsilon_Q,
\qquad
\frac1\zeta.
$$

Rare reports can make even a well-calibrated model locally fragile.

---

# 44. Confidence-set controller

Let

$$
\mathcal U_t=\{(T,Q):\text{current confidence/credible constraints hold}\}.
$$

A robust controller evaluates worst-case expected cost over this set.

---

# 45. GVSS07-T9 — Robust-value certification

For any fixed policy $\pi$, if true $(T^*,Q^*)\in\mathcal U_t$, then

$$
\boxed{
J^\pi(T^*,Q^*)
\le
\sup_{(T,Q)\in\mathcal U_t}J^\pi(T,Q).
}
$$

If the confidence set covers the true model with probability $1-\delta$, this upper-bound statement holds with at least that probability.

### Proof

The true model is an element of the supremum set.

 $\square$

This is a certificate, not true-model optimality.

---

# 46. Robustness can be expensive

Large uncertainty sets may trigger conservative HUMAN_REVIEW, STOP, or fallback actions.

Better system identification can therefore improve control not only by making beliefs more accurate but also by shrinking conservatism.

---

# 47. Joint one-step kernel error

Combine failure transition and diagnostic report into one controlled kernel $K_t$.

Assume uniformly

$$
\sup_x\operatorname{TV}(K_t(x,\cdot),\widehat K_t(x,\cdot))\le\epsilon.
$$

---

# 48. GVSS07-T10 — Finite-horizon path-law error

Under the same fixed policy for horizon $H$,

$$
\boxed{
\operatorname{TV}(P_{0:H},\widehat P_{0:H})\le H\epsilon.
}
$$

### Proof sketch

Couple the two processes until the first discrepancy. Before divergence, each next-step conditional mismatch probability is at most $\epsilon$. Union bound over $H$ steps.

 $\square$

---

# 49. GVSS07-C1 — Finite-horizon cost error

If stage cost lies in $[0,C_{\max}]$, total horizon cost is at most $HC_{\max}$. Hence

$$
\boxed{
|EC_{0:H}-\widehat EC_{0:H}|
\le H^2C_{\max}\epsilon.
}
$$

This is deliberately coarse.

---

# 50. Online update

For independently labeled episode

$$
(F_t,a_t,F_{t+1},Y_{t+1}),
$$

update counts/posteriors for the corresponding versioned rows.

If stationarity is trusted, retain all same-version data.

If drift is suspected, use a version reset, sliding window, discounting, or situation model.

---

# 51. Situation-aware models

A richer runtime can introduce hidden context $S_t$ and use

$$
T_{a,S_t},
\qquad
Q_{a,S_t}.
$$

GVSS-07 does not develop the full hidden-context controller.

---

# 52. Version invalidation

When stationarity is rejected, mark the old model stale for the new regime. Do not silently preserve its calibration label.

Possible status:

```text
valid
transferred_with_bound
stale
invalidated
unidentified
```

---

# 53. Active model-identification action

Add runtime action

```text
CALIBRATE_MODEL
```

which can allocate budget to failure injections, provider probes, evaluator anchors, alternate-policy tests, or independent human audits.

---

# 54. Identification value

A calibration action is valuable when expected shrinkage of $\mathcal U$ or correction of $\widehat T,\widehat Q$ reduces downstream GVSS-06 control cost more than the calibration cost.

This is active learning / experimental design, not a new GVSS statistical principle.

---

# 55. Relation to ASID

ASID actively chooses real-world exploration to refine uncertain system parameters.

GVSS controlled failure injection follows the same meta-pattern:

> intervene because the intervention makes the control model more identifiable.

---

# 56. Relation to online design of experiments

Online nonlinear system-ID work actively selects excitation inputs and recursively updates estimates.

GVSS-07's row allocation theorem is a finite categorical simplification of the same identification-budget question.

---

# 57. Relation to Model Identification Adaptive Control

MIAC with belief-space planning treats unknown model parameters as hidden variables that must be identified while control proceeds.

GVSS-06/07 similarly couple image correction and learning of diagnostic dynamics.

---

# 58. Relation to latent POMDP learning

When failures cannot be injected or labeled, GVSS becomes a hidden world-model learning problem.

Current POMDP induction systems demonstrate that priors and structured proposals can reduce interaction needs, but they do not remove general identifiability limits.

---

# 59. Relation to nonstationary system identification

Current dynamics-learning work uses changepoint detection and situation representations to adapt when the data-generating dynamics shift.

GVSS provider/evaluator/compiler updates create the same need for model invalidation and version-aware re-identification.

---

# 60. Safe identification

Calibration experiments can have cost or project risk. An identification action should respect hard project constraints just as safe system-identification methods constrain informative trajectories.

A diagnostic system should not destroy a valuable visual asset merely to learn its own transition model.

---

# 61. Exact toy systems first

Before using learned hidden failure models on frontier black-box image generators, validate the identification/controller stack on finite systems with known $T,Q$.

This separates:

- estimation failure;
- inference failure;
- control failure.

---

# 62. GVSS-07 benchmark structure

A benchmark should contain:

1. known failure states;
2. known action transition tables;
3. known report likelihoods;
4. controlled injection hooks;
5. version-shift events;
6. synthetic-to-real gap variants;
7. hidden-state variants;
8. action costs;
9. GVSS-06 control evaluation.

---

# 63. Table error

Transition error:

$$
E_T=\max_{a,k}\operatorname{TV}(T_a(\cdot\mid k),\widehat T_a(\cdot\mid k)).
$$

Observation error:

$$
E_Q=\max_{a,k}\operatorname{TV}(Q_a(\cdot\mid k),\widehat Q_a(\cdot\mid k)).
$$

---

# 64. Downstream belief error

Measure

$$
E_b=E[\operatorname{TV}(b_t,\widehat b_t)].
$$

A small table error is useful only insofar as it supports good visual diagnosis/control.

---

# 65. Policy-cost error

Run the GVSS-06 controller with true and learned models and compare expected total cost.

This is the primary end-to-end consequence of identification quality.

---

# 66. Calibration efficiency

Report confidence-radius reduction per:

- injected episode;
- GPU dollar;
- provider probe;
- human label;
- evaluator anchor.

---

# 67. Drift metric

Inject version shifts at known times and measure:

- detection delay;
- false alarms;
- stale-model control cost;
- recovery time.

---

# 68. Coverage map

For every row store sample count $n_{a,k}$.

Define directly covered set

$$
\mathcal C_{\rm ID}=\{(a,k):n_{a,k}>0\}.
$$

A large total dataset can still have catastrophic holes in this coverage map.

---

# 69. Identification status

Each row should be marked:

$$
\boxed{
\text{directly identified}
\vee
\text{transferred}
\vee
\text{latent inferred}
\vee
\text{unidentified}.
}
$$

This status should enter GVSS-06 uncertainty handling.

---

# 70. Evidence quality

A million pseudo-labeled rows can be weaker evidence than a smaller independently injected set if pseudo-label bias is uncontrolled.

Keep direct labels, transferred labels, and endogenous labels separate.

---

# 71. Human audit

Human labels can provide independent supervision but can disagree.

Use versioned rubrics, multiple reviewers where appropriate, confidence, and adjudication.

---

# 72. Evaluator-side failure labels

Do not use evaluator $E$ alone to generate the ground-truth labels for estimating $F_E$.

That is circular calibration.

Use an independent judge, human, benchmark, or controlled corruption with known ground truth.

---

# 73. Search-failure labels

A strong empirical label for $F_{\rm search}$ is an episode in which one policy fails but another succeeds under the same generator binding and target constraints.

This follows GVSS05-T5.

---

# 74. Reachability labels

For frontier black-box systems, prefer

```text
bounded_reachability_failure(provider, policy_class, budget, target)
```

over an absolute semantic-unreachability label.

Finite search is not an impossibility proof.

---

# 75. Failure-taxonomy misspecification

The seven GVSS failure states can themselves be too coarse.

For example evaluator failure may contain spatial blindness, counting error, style bias, or reward hacking.

---

# 76. GVSS07-N6 — More data does not repair a structurally wrong failure taxonomy

If two distinct predictive/transition modes are forced into one failure state, infinite row data converges to the aggregated mixture model. Sampling variance vanishes; structural aggregation error remains.

Therefore

$$
\boxed{
\text{more parameter-estimation data}\not\Rightarrow\text{correct failure representation}.
}
$$

---

# 77. Taxonomy expansion trigger

If high-coverage rows still show systematic multimodality, poor held-out likelihood, or action-conditioned residual structure, consider expanding

$$
\mathcal F\to\mathcal F'.
$$

This is a model-class revision problem, not ordinary row-frequency learning.

---

# 78. Diagnostic model artifact

Canonical artifact:

$$
\boxed{
\mathsf{DM}_\nu
=
(\nu,\widehat T,\widehat Q,\mathcal U,D,\mathsf{Fit},\mathsf{Validation},\mathsf{Hash}).
}
$$

---

# 79. Diagnostic model lineage

Every update should create a child model version with parent ID and data delta.

Do not silently overwrite the calibrated model that produced historical decisions.

---

# 80. Runtime schema sketch

```text
diagnostic_model:
  version_key
  parent_model_id
  transition_rows
  observation_rows
  row_sample_counts
  confidence_or_credible_sets
  identification_status
  calibration_data_refs
  injection_refs
  provider_version
  evaluator_version
  compiler_version
  search_policy_version
  drift_status
  provenance_hash
```

---

# 81. Provider capability maps

The same infrastructure can estimate conditional success/repair probabilities by provider, failure type, style regime, and constraint regime.

This is the beginning of a learned practical reachability/capability map.

GVSS-07 does not yet formalize the full map.

---

# 82. What is classical / neighboring

GVSS-07 does not claim as inventions:

- system identification;
- active system identification;
- POMDP parameter learning;
- Bayesian categorical estimation;
- Hoeffding bounds;
- active experimental design;
- change-point detection;
- robust control under model uncertainty;
- sim-to-real system identification.

---

# 83. Candidate GVSS-specific synthesis

Subject to broader literature audit, candidate synthesis contributions are:

1. treating the GVSS failure transition and diagnostic likelihood tables as versioned system-ID targets;
2. separating controlled/labeled visual failure identification from latent POMDP learning;
3. explicit finite-table confidence certificates for the seven-layer visual failure model;
4. active sample allocation over action/failure rows using downstream importance;
5. synthetic failure transfer controlled by a diagnostic domain-gap bound;
6. version-drift tests for provider/evaluator/compiler diagnostic behavior;
7. a combined $T/Q$ uncertainty bound directly feeding the GVSS-06 failure posterior;
8. diagnostic-model artifacts/provenance as first-class runtime state;
9. explicit separation of pseudo-label consistency from independently identified truth.

No strong novelty claim is made.

---

# 84. What GVSS-07 proves

Under explicit hypotheses, GVSS-07 proves:

1. simultaneous Hoeffding confidence bands for finite diagnostic observation rows;
2. simultaneous confidence bands for finite action-conditioned failure transition rows;
3. consistency/direct identifiability with independent state labels and stationary row sampling;
4. non-identifiability of hidden transitions when hidden states share identical diagnostic observation laws;
5. minimax continuous sample allocation proportional to squared row importance weights;
6. bounded synthetic-to-real diagnostic-loss transfer under TV shift;
7. a two-version categorical stationarity rejection certificate;
8. pooled cross-version data converges to a mixture law rather than either component law in general;
9. combined transition/observation error yields an inverse-evidence one-step posterior-TV bound;
10. robust worst-case value upper-bounds true policy value when the true model lies in the uncertainty set;
11. finite-horizon path-law TV error grows at most linearly under uniform one-step TV error;
12. corresponding bounded cost error has a coarse $H^2$ bound;
13. self-label agreement does not imply true diagnostic correctness;
14. zero row excitation gives no direct empirical transition-row identification;
15. stale data cannot remove an unmodeled version shift;
16. fixed failure-taxonomy misspecification is not repaired by more row-frequency data.

---

# 85. What GVSS-07 does not prove

It does not prove:

- general latent-POMDP identifiability;
- that synthetic injections match deployment failures;
- that human labels are always correct;
- that finite categorical tables are sufficient for continuous VLM reports;
- that drift is abrupt rather than gradual;
- that the simple Hoeffding bands are sample-optimal;
- that the row allocation theorem minimizes Bellman regret;
- that robust control is cheaper than nominal control;
- exact reachability of black-box frontier generators;
- completeness of the seven-state failure taxonomy.

---

# 86. Proposed GVSS-08

The next paper should use the uncertainty model in control.

$$
\boxed{
\textbf{GVSS-08 — Robust Visual Diagnostic Control under Model Uncertainty and Regime Drift}
}
$$

Chinese:

**模型不確定性與生成環境漂移下的穩健視覺診斷控制**

Main questions:

1. When should nominal and robust policies differ?
2. How should uncertainty-set size affect HUMAN_REVIEW and STOP?
3. How should drift probability affect REBIND or model recalibration?
4. What is the control cost of stale diagnostic models?
5. How should evaluator/provider fallback and quarantine work?
6. Can multiple provider-specific models be fused without hiding version conflicts?

---

# 87. References

1. Marius Memmel et al., **ASID: Active Exploration for System Identification in Robotic Manipulation**, arXiv:2404.12308 / ICLR 2024.
2. Michelle Ho, Arec Jamgochian, Mykel J. Kochenderfer, **Model Identification Adaptive Control with $\rho$ -POMDP Planning**, arXiv:2505.09119, 2025.
3. Kui Xie, Alberto Bemporad, **Online Design of Experiments by Active Learning for Nonlinear System Identification**, arXiv:2506.21754, 2025.
4. Valentin Six et al., **Learning POMDP World Models from Observations with Language-Model Priors**, arXiv:2605.13740, 2026.
5. Alejandro Murillo-Gonzalez, Lantao Liu, **Situationally-Aware Dynamics Learning**, arXiv:2505.19574 / IJRR 2026.
6. Chi Ho Leung, Ashish R. Hota, Philip E. Paré, **Online Identification of Time-Varying Systems Using Excitation Sets and Change Point Detection**, arXiv:2406.10349.
7. Bohao Zhang, Zichang Zhou, Ram Vasudevan, **Provably-Safe, Online System Identification**, arXiv:2504.21486, 2025.
8. GVSS-01 through GVSS-06, internal series artifacts, 2026.
9. RRT-20, **Reflexive Representation Theory: Unified Closure, Meta-Theorems, Limits, and Research Program**, internal series artifact, 2026.

---

# 88. Conclusion

GVSS-06 assumes a diagnostic model.

GVSS-07 makes that model an object of science.

The runtime now carries

$$
\boxed{
\mathsf{DM}_\nu=(\widehat T_\nu,\widehat Q_\nu,\mathcal U_\nu,D_\nu,\mathsf{Prov}_\nu).
}
$$

Rows can be identified directly when failure states can be injected or independently labeled.

When failure states remain latent, identifiability becomes a POMDP/world-model problem and can fail completely under observational aliasing.

Active calibration should allocate samples to important underidentified rows rather than passively collecting whatever the current controller happens to encounter.

Synthetic failure injection is useful only with a transfer argument.

Provider, evaluator, compiler, and runtime updates can alter diagnostic dynamics; stale data must be versioned and tested instead of silently pooled.

Finally, learned model uncertainty feeds directly into visual diagnosis through

$$
\boxed{
\operatorname{TV}(b^{a,y},\widehat b^{a,y})
\le
\frac{2\varepsilon_T+\varepsilon_Q}{\zeta}.
}
$$

The canonical GVSS-07 principle is:

$$
\boxed{
\textbf{
The model that diagnoses visual failure must itself be identified, calibrated, versioned, and falsifiable.
A controller that learns only from labels produced by itself can become perfectly self-consistent while remaining perfectly wrong.
}
}
$$

This completes the transition from fixed diagnostic control to a visual runtime whose own diagnostic dynamics are learned from controlled evidence.

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
