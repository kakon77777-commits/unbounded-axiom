# VWDC-07 — Closed-Loop Reality Feedback, Safe Policy Adaptation, and Transport-Aware Continual Worlds
## 閉環現實回饋、安全策略適應與轉移感知持續世界：選擇性回饋、Champion–Challenger、Rollback 與生命週期證書

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 07  
**Depends on:** VWDC-01–06, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal continual-governance paper. Deployment-feedback selection bias, inverse-propensity feedback correction, unsupported-feedback non-identifiability, self-confirming safety loops, independent validation promotion certificates, certificate-preserving champion updates, lifecycle alpha spending, rollback correctness and rollback limits under drift, fixed-window residual drift detection, local certified-action inheritance, support-expansion no-go, incident invalidation closure, immutable version-lineage acyclicity, rollback-value thresholds, and continual update-action regret are proved under explicit hypotheses. Continual learning, performative feedback, safe policy adaptation, digital-twin continual validation, champion–challenger deployment, and rollback engineering are established neighboring ideas and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** continual digital twin, reality feedback, policy adaptation, champion challenger, rollback, selective labels, performative feedback, deployment bias, continual validation, safe update, transport contract, WDC

---

# Abstract

VWDC-06 closed the first reality-facing loop:

$$
\boxed{
\text{World}
\to
\text{RTC}
\to
\text{Policy}
\to
\text{Reality}
\to
\text{Evidence}
\to
\text{RTC}.
}
$$

But once reality feedback is allowed to update:

- the world model;
- the Reality Transport Contract;
- the deployment policy;

the system becomes reflexive.

The deployed policy determines which states are visited, which actions are executed, which outcomes are observed, and therefore which future training data exist.

The central warning is:

$$
\boxed{
\text{deployment feedback}
\neq
\text{policy-independent reality sample}.
}
$$

VWDC-07 therefore separates three feedback streams:

$$
\boxed{
\mathcal D_{\mathrm{adapt}}
\neq
\mathcal D_{\mathrm{validate}}
\neq
\mathcal D_{\mathrm{audit/incident}}.
}
$$

The first can be used to adapt models/policies.

The second is reserved or statistically corrected for promotion decisions.

The third contains external audits, incidents, independent measurements, or other evidence that must retain a distinct provenance role.

The continual runtime maintains a versioned **certified deployment pair**:

$$
\boxed{
C_t
=
(
M_t,
\mathsf{RTC}_t,
\pi_t,
\mathsf{Safety}_t,
\mathsf{Authority}_t,
\mathsf{Prov}_t
).
}
$$

A candidate challenger:

$$
\widetilde C_t
$$

does not replace the current champion merely because it fits recent data better.

It enters:

```text
SHADOW
CHALLENGER
VALIDATION_PENDING
PROMOTED
REJECTED
ROLLED_BACK
SUPERSEDED
```

through explicit gates.

The canonical update actions are:

$$
\boxed{
\mathcal A_{\mathrm{cont}}
=
\{
\mathrm{KEEP},
\mathrm{UPDATE\_WORLD},
\mathrm{UPDATE\_RTC},
\mathrm{UPDATE\_POLICY},
\mathrm{UPDATE\_JOINT},
\mathrm{REVALIDATE},
\mathrm{ROLLBACK},
\mathrm{FREEZE},
\mathrm{FALLBACK}
\}.
}
$$

---

# 1. Deployment-selected feedback

Let reality context be:

$$
S_t.
$$

The deployed policy/logging rule selects:

$$
\boxed{
A_t
\sim
\mu_t(
\cdot\mid S_t
).
}
$$

Only the outcome for the chosen action is observed:

$$
Y_t
=
Y_t(A_t).
$$

Thus the feedback dataset is policy selected.

---

# 2. Potential outcome notation

For each action:

$$
a,
$$

let:

$$
Y(a)
$$

be the potential outcome under that action.

Only:

$$
Y(A_t)
$$

is observed.

This creates the same missing-counterfactual structure found in contextual bandits and causal inference.

---

# 3. Naive deployed-feedback mean

For action $a$:

$$
\boxed{
\overline Y_a^{\mathrm{deploy}}
=
E[
Y
\mid
A=a
].
}
$$

This is generally not the target-population action value:

$$
\boxed{
V(a)
=
E_S[
E(
Y(a)
\mid
S
)
].
}
$$

---

# 4. VWDC07-N1 — Deployment-selection bias can reverse action/model quality

## Counterexample

There are two context classes with equal population mass:

$$
S
\in
\{
\mathrm{easy},
\mathrm{hard}
\}.
$$

Policy/model A has potential outcome means:

$$
0.8,\quad0.2.
$$

Policy/model B has:

$$
0.9,\quad0.4.
$$

Thus B dominates A in every context.

But the deployed policy uses A only on easy cases and B only on hard cases.

Observed deployed means become:

$$
\boxed{
\overline Y_A=0.8,
\qquad
\overline Y_B=0.4.
}
$$

The logging feedback ranks A above B even though B is better everywhere.

Therefore:

$$
\boxed{
\text{deployment feedback average}
\not\Rightarrow
\text{target-population policy quality}.
}
$$

 $\square$

---

# 5. Feedback propensity

Every deployment record should store:

$$
\boxed{
p_t
=
\mu_t(
A_t\mid S_t
).
}
$$

Without this, later off-policy correction can become impossible.

---

# 6. Target feedback estimand

For target policy:

$$
\pi(a\mid s),
$$

define:

$$
\boxed{
V(\pi)
=
E_S
\sum_a
\pi(a\mid S)
E[
Y(a)\mid S
].
}
$$

---

# 7. VWDC07-T1 — Inverse-propensity deployment-feedback unbiasedness

## Theorem VWDC07-T1

Assume:

1. the logging propensity $\mu(a\mid s)$ is known/correct;
2. consistency holds for observed action outcomes;
3. target support condition:
   $$
   \pi(a\mid s)>0
   \Longrightarrow
   \mu(a\mid s)>0;
   $$
4. feedback is otherwise sampled under the stated deployment process.

Then:

$$
\boxed{
\widehat V_{\mathrm{IPS}}(\pi)
=
\frac1n
\sum_{i=1}^n
\frac{
\pi(A_i\mid S_i)
}{
\mu(A_i\mid S_i)
}
Y_i
}
$$

is unbiased for:

$$
V(\pi).
$$

### Proof

Condition on context:

$$
\begin{aligned}
E
\left[
\frac{
\pi(A\mid S)
}{
\mu(A\mid S)
}
Y
\mid S
\right]
&=
\sum_a
\mu(a\mid S)
\frac{
\pi(a\mid S)
}{
\mu(a\mid S)
}
E[Y(a)\mid S]
\\
&=
\sum_a
\pi(a\mid S)
E[Y(a)\mid S].
\end{aligned}
$$

Average over $S$.

 $\square$

This is classical off-policy correction.

---

# 8. Feedback support

## Definition VWDC07-D1

Action/context pair:

$$
(s,a)
$$

has feedback support if:

$$
\boxed{
\mu(a\mid s)>0.
}
$$

---

# 9. VWDC07-N2 — Unsupported deployment feedback cannot identify unexecuted action behavior

## Proposition VWDC07-N2

If:

$$
\mu(a^\star\mid s^\star)=0,
$$

then without structural assumptions there exist two reality models that generate identical deployment logs but assign arbitrary different outcomes to:

$$
Y(a^\star)
$$

at:

$$
s^\star.
$$

### Proof

Make both reality models identical on every action/context pair with positive logging probability.

Assign different counterfactual outcomes only to the unsupported pair.

The logs are identical.

 $\square$

---

# 10. Safety interpretation

If a policy never enters a region or never executes an action, the absence of observed incidents there is not evidence of safety there.

Thus:

$$
\boxed{
\text{no observed failure}
+
\text{no exposure}
\not\Rightarrow
\text{safety}.
}
$$

---

# 11. Self-confirming feedback loop

A dangerous loop can be:

$$
\boxed{
\text{policy predicts region unsafe}
\to
\text{never visits region}
\to
\text{collects no contradictory data}
\to
\text{retraining preserves belief}.
}
$$

The reverse can also occur:

$$
\boxed{
\text{policy visits only easy/safe regions}
\to
\text{feedback looks excellent}
\to
\text{model appears increasingly validated}.
}
$$

---

# 12. VWDC07-N3 — Self-confirming deployment loop no-go

## Counterexample

Two policies/world models are observationally identical on the region visited by current policy:

$$
\mathcal Z_{\mathrm{visit}}.
$$

Outside this region:

- World A is safe;
- World B contains catastrophic failure.

The current policy never leaves:

$$
\mathcal Z_{\mathrm{visit}}.
$$

No amount of on-policy feedback distinguishes A from B.

Therefore perfect agreement on deployment feedback does not establish correctness outside the visited support.

 $\square$

---

# 13. Performative feedback precedent

Current research on self-consuming/performative loops shows that deployed models can alter the data distribution they later train on, including by changing which user or outcome data become available.

VWDC applies the same warning to continual world/policy calibration.

---

# 14. Feedback stream separation

## Definition VWDC07-D2

Maintain:

### Adaptation stream

$$
\mathcal D_A.
$$

Used for:

- model fitting;
- policy adaptation;
- RTC update proposals.

### Validation stream

$$
\mathcal D_V.
$$

Used for promotion/challenger testing.

### Audit/incident stream

$$
\mathcal D_I.
$$

Used for:

- independent audit;
- incident response;
- external challenge;
- transport revalidation.

---

# 15. Independence ideal

For a fixed challenger trained on:

$$
\mathcal D_A,
$$

promotion evaluation should, where feasible, use validation data not used to fit/select that challenger.

This permits ordinary fixed-candidate concentration arguments conditional on the trained challenger.

---

# 16. Challenger loss

Let champion loss on validation item $i$ be:

$$
\ell_i^C
\in
[0,1].
$$

Challenger loss:

$$
\ell_i^N
\in
[0,1].
$$

Define paired difference:

$$
\boxed{
D_i
=
\ell_i^N-\ell_i^C
\in
[-1,1].
}
$$

Negative mean favors the challenger.

---

# 17. VWDC07-T2 — Independent validation promotion certificate

## Theorem VWDC07-T2

Condition on a fixed champion and challenger independent of the held-out validation sample.

Let:

$$
\bar D_n
=
\frac1n
\sum_iD_i.
$$

Define:

$$
\boxed{
r_n(\delta)
=
\sqrt{
\frac{
2\log(2/\delta)
}{
n
}
}.
}
$$

Then with probability at least:

$$
1-\delta,
$$

$$
\boxed{
|
\bar D_n
-
E[D]
|
\le
r_n(\delta).
}
$$

Therefore if:

$$
\boxed{
\bar D_n
+
r_n(\delta)
<
0,
}
$$

the challenger has lower expected validation loss than the champion on the validation distribution with probability at least:

$$
1-\delta.
$$

### Proof

 $D_i\in[-1,1]$ has range width 2.

Apply Hoeffding's inequality.

 $\square$

---

# 18. Promotion is multidimensional

Predictive improvement is not enough.

A challenger may need to pass:

- transport validation;
- safety;
- authority;
- latency/resource;
- rollback;
- provenance.

Thus promotion is an intersection of gates.

---

# 19. Champion–challenger state

Current certified champion:

$$
\boxed{
C_t.
}
$$

Candidate:

$$
\widetilde C_t.
$$

A promotion creates:

$$
C_{t+1}
=
\widetilde C_t
$$

only after all required gates pass.

Old champion remains immutable and available for rollback while its own contracts remain current.

---

# 20. Certified risk bound

Let a certified pair carry an upper decision-risk certificate:

$$
\boxed{
U(C).
}
$$

Lower is better.

---

# 21. VWDC07-T3 — Frozen-regime champion certificate monotonicity

## Theorem VWDC07-T3

Assume:

1. reality regime remains unchanged;
2. old champion certificate remains current;
3. a challenger is promoted only when:
   $$
   U(\widetilde C_t)
   \le
   U(C_t).
   $$

Then the sequence of champion certified upper risks is nonincreasing:

$$
\boxed{
U(C_{t+1})
\le
U(C_t).
}
$$

### Proof

Directly from the promotion rule.

 $\square$

This concerns certificate quality, not necessarily true realized performance.

---

# 22. Stability–plasticity interpretation

A continual system can learn aggressively in shadow/challenger mode while keeping production promotion conservative.

This separates:

- plasticity of candidate learning;
- stability of certified deployment.

---

# 23. Current validation-gated precedent

Recent continual digital-twin work uses drift detection, targeted updates, statistical validation, and robust control before accepting updated models.

Other work explicitly uses champion–challenger style validation gates and shadow learning for safety-relevant continual adaptation.

VWDC does not claim champion–challenger governance as new.

---

# 24. Repeated promotion tests

Suppose promotion event:

$$
E_t
$$

means a false promotion occurs at update $t$.

Promotion gate is designed so:

$$
P(E_t)
\le
\delta_t.
$$

No independence is required for the next result.

---

# 25. VWDC07-T4 — Lifecycle alpha-spending promotion bound

## Theorem VWDC07-T4

For any finite or countable sequence of promotion tests:

$$
\boxed{
P(
\exists t:
E_t
)
\le
\sum_t
\delta_t.
}
$$

Therefore if:

$$
\boxed{
\sum_t
\delta_t
\le
\delta_{\mathrm{life}},
}
$$

the probability of at least one false promotion over the declared lifecycle is at most:

$$
\boxed{
\delta_{\mathrm{life}}.
}
$$

### Proof

Union bound.

 $\square$

---

# 26. Lifecycle test budget

Example schedule:

$$
\boxed{
\delta_t
=
\frac{
6\delta_{\mathrm{life}}
}{
\pi^2t^2
}
}
$$

uses:

$$
\sum_{t=1}^{\infty}
\frac1{t^2}
=
\frac{\pi^2}{6}.
$$

Thus:

$$
\sum_t\delta_t
=
\delta_{\mathrm{life}}.
$$

---

# 27. VWDC07-N4 — Per-update 95% confidence is not a lifetime 95% guarantee

If every update uses the same fixed:

$$
\delta=0.05,
$$

the union-bound lifecycle failure budget after $m$ tests is:

$$
0.05m,
$$

capped at 1.

If false-promotion events were independent with exact probability 0.05, the probability of at least one false promotion would be:

$$
\boxed{
1-0.95^m.
}
$$

Therefore repeated 95% gates do not imply 95% lifecycle validity.

 $\square$

---

# 28. Rollback

A rollback selects an earlier certified pair:

$$
C_k,
\qquad
k<t.
$$

It creates a new deployment event/version pointing to:

$$
C_k.
$$

Historical versions are not deleted.

---

# 29. Rollback target status

An old pair can be:

```text
CURRENT_CERTIFIED
HISTORICAL_CERTIFIED
STALE
INVALID
REVALIDATION_REQUIRED
```

Rollback is valid only to a pair whose required contracts are still current for the present reality regime.

---

# 30. VWDC07-T5 — Conditional rollback restoration

## Theorem VWDC07-T5

Suppose old certified pair:

$$
C_k
$$

has:

- current RTCs;
- current safety contracts;
- compatible reality regime;
- available artifacts/runtime dependencies.

Then switching deployment back to $C_k$ restores the same **certified contract status** previously associated with $C_k$ under those still-valid assumptions.

### Proof

The certification predicates are predicates of the pair, current contract versions, and reality-regime assumptions.

If those inputs remain valid and unchanged, the predicate remains satisfied.

 $\square$

This does not imply the current reality is identical to the past.

That compatibility is an explicit hypothesis.

---

# 31. VWDC07-N5 — Rollback cannot restore expired external validity

## Counterexample

Policy/RTC pair:

$$
C_0
$$

was certified for reality regime:

$$
\nu_R^0.
$$

Reality later shifts to:

$$
\nu_R^1
$$

where $C_0$ 's RTC is invalid.

Rolling back software/model versions to $C_0$ does not change reality back to:

$$
\nu_R^0.
$$

Therefore:

$$
\boxed{
\text{version rollback}
\not\Rightarrow
\text{validity rollback}.
}
$$

 $\square$

---

# 32. Rollback principle

Rollback restores:

- code;
- model;
- policy;
- configuration;

not the external world.

Every rollback must re-check current transport/safety contracts.

---

# 33. Rollback cost

Let current candidate certified upper risk be:

$$
U_N.
$$

Old champion upper risk:

$$
U_C.
$$

Rollback switching cost:

$$
c_{\mathrm{rb}}.
$$

---

# 34. VWDC07-T6 — One-step rollback threshold

## Theorem VWDC07-T6

Under a one-step certified-risk-plus-switching-cost objective, rollback to champion is strictly preferred to remaining on the candidate iff:

$$
\boxed{
c_{\mathrm{rb}}
+
U_C
<
U_N.
}
$$

### Proof

Direct cost comparison.

 $\square$

---

# 35. Rollback trigger examples

- predictive degradation;
- safety violation;
- RTC invalidation;
- external incident;
- drift beyond adaptation envelope;
- challenger confidence collapse;
- provenance corruption.

---

# 36. Freeze

FREEZE halts online adaptation while keeping current certified policy or fallback.

Use when:

- feedback insufficient;
- drift uncertain;
- validation unavailable;
- incident investigation underway.

---

# 37. Current rollback-capable twin precedent

Recent digital-twin/system papers explicitly emphasize versioning, validation, shadow deployment, rollback capability, and degraded modes under drift or failed updates.

VWDC places these into the versioned world/RTC/policy pair.

---

# 38. Residual stream

Define reality residual:

$$
\boxed{
R_t
=
\ell(
Prediction_t,
Reality_t
)
}
$$

or another bounded diagnostic statistic.

---

# 39. Old/new windows

Let residuals in two independent windows be bounded:

$$
R\in[0,1].
$$

Old mean:

$$
\mu_0.
$$

New mean:

$$
\mu_1.
$$

Empirical means:

$$
\widehat\mu_0,
\widehat\mu_1
$$

with sample counts:

$$
n_0,n_1.
$$

---

# 40. VWDC07-T7 — Fixed-window regime-drift rejection certificate

## Theorem VWDC07-T7

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
\widehat\mu_1-\widehat\mu_0
]
-
[
\mu_1-\mu_0
]
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
\widehat\mu_1-\widehat\mu_0
|
>
r(n_0,\delta)
+
r(n_1,\delta),
}
$$

the equality:

$$
\mu_1=\mu_0
$$

is rejected on the high-probability event.

### Proof

Hoeffding on both window means and union bound.

 $\square$

---

# 41. Regime split

On behaviorally relevant drift:

$$
\boxed{
\nu_R^k
\to
\nu_R^{k+1}.
}
$$

Do not force all new data into the old reality-regime contract.

---

# 42. World-model version split

If adaptation changes world-model semantics materially:

$$
\nu_W^k
\to
\nu_W^{k+1}.
$$

Create a new version.

---

# 43. Policy version split

Every promoted policy update creates:

$$
\pi_{v+1}.
$$

Never overwrite:

$$
\pi_v.
$$

---

# 44. Version triple

A deployed continual state is:

$$
\boxed{
\mathsf{DepVersion}_t
=
(
\nu_W,
\nu_R,
\nu_\pi,
\nu_{\mathrm{RTC}},
\nu_{\mathrm{safety}}
).
}
$$

---

# 45. Version lineage DAG

Every update records parent IDs and creates a new version node.

Rollback creates a new deployment event referencing an old certified version rather than rewinding history.

---

# 46. VWDC07-T8 — Immutable version-lineage acyclicity

## Theorem VWDC07-T8

If every world/RTC/policy/safety update creates a new node with creation index greater than all parent versions, and rollback creates a new deployment-event node rather than mutating an ancestor, then the version-lineage graph is acyclic.

### Proof

Every version-lineage edge strictly increases creation index.

A directed cycle would require strict increase back to the original index.

Impossible.

 $\square$

---

# 47. Local certified action set

For old certified pair:

$$
C,
$$

let:

$$
\boxed{
\mathcal A_C(s)
}
$$

be the actions carrying all required RTC/safety/authority certificates at state $s$.

---

# 48. Policy update

New policy:

$$
\pi'
$$

is **locally contract preserving** on region:

$$
S_C
$$

if:

$$
\boxed{
\operatorname{supp}
\pi'(
\cdot\mid s
)
\subseteq
\mathcal A_C(s)
\quad
\forall s\in S_C.
}
$$

---

# 49. VWDC07-T9 — Local certified-action inheritance

## Theorem VWDC07-T9

If $\pi'$ is locally contract preserving on $S_C$, then every action selected by $\pi'$ while the system remains inside $S_C$ satisfies the old pair's action-level certification predicates.

### Proof

By support inclusion.

 $\square$

---

# 50. Caveat

The theorem does not guarantee the updated policy keeps the system inside:

$$
S_C.
$$

Dynamics can move the system outside the old certified region.

---

# 51. VWDC07-N6 — Local action inheritance does not guarantee closed-loop certification

## Counterexample

All actions selected by $\pi'$ at initial state $s_0$ are certified.

One certified action transitions reality to:

$$
s_1
\notin
S_C.
$$

At:

$$
s_1
$$

the policy has no valid RTC.

Thus local action certification at current states does not prove the entire future policy trajectory remains certified.

 $\square$

---

# 52. Invariant certified region

A stronger condition requires:

$$
\boxed{
s\in S_C,
\quad
a\in\operatorname{supp}\pi'(\cdot\mid s)
\Longrightarrow
S_{t+1}\in S_C
}
$$

under all allowed reality dynamics.

This is an invariant-set/safety-control problem.

VWDC does not rederive controlled-invariance theory.

---

# 53. SafeAdapt boundary

Current safe-policy-update research explicitly studies policy-parameter update regions that preserve safety guarantees on previously encountered task distributions.

VWDC distinguishes this safety-preservation problem from external-validity preservation.

---

# 54. Independent validation versus same-stream validation

Suppose candidate is selected to minimize loss on the same finite dataset used for promotion.

Ordinary fixed-candidate holdout confidence does not automatically apply after this adaptive reuse.

---

# 55. VWDC07-N7 — In-sample promotion can be perfectly self-confirming

## Counterexample

Take finite adaptation dataset:

$$
D
=
\{
(x_i,y_i)
\}_{i=1}^n.
$$

Allow a challenger model with enough capacity to memorize:

$$
y_i
$$

for every sample.

Its in-sample loss is zero.

Define reality distribution with all mass outside those memorized points and arbitrary opposite labels.

Then:

$$
\boxed{
\text{zero adaptation/promotional in-sample loss}
\not\Rightarrow
\text{external improvement}.
}
$$

 $\square$

---

# 56. Promotion-data policy

Recommended:

- fixed holdout;
- rolling prospective holdout;
- external audit stream;
- valid sequential testing;
- shadow comparison.

The exact method depends on data availability and nonstationarity.

---

# 57. Data reuse provenance

Every evidence row records whether it was used for:

```text
TRAIN
CALIBRATE
VALIDATE
PROMOTE
AUDIT
INCIDENT
```

One row can have multiple roles, but confidence claims must account for reuse.

---

# 58. Incident

An incident is a reality observation that contradicts or violates a required contract/safety predicate.

It may invalidate:

- one RTC cell;
- one policy decision rule;
- one world-model assumption;
- one safety contract;
- downstream aggregates.

---

# 59. Dependency graph

Use VWDC-03 dependency graph:

$$
G_D.
$$

Incident node invalidates contradicted dependency.

---

# 60. VWDC07-T10 — Incident invalidation closure

## Theorem VWDC07-T10

Under exact required-dependency semantics, invalidating a contract/model/evidence node due to a real incident requires every descendant decision/certificate that depends on it to enter:

```text
STALE
INVALID
PENDING_REVALIDATION
```

unless an alternate valid support path exists.

### Proof

VWDC-03 descendant-closure induction applied to a reality-incident source.

 $\square$

---

# 61. Incident does not erase history

Old decision remains historical.

Its certification status changes.

Do not delete the record.

---

# 62. Incident rollback sequence

Recommended:

1. stop/fallback if risk policy requires;
2. mark contradicted contract node;
3. compute blast radius;
4. select last still-current champion;
5. check reality-regime compatibility;
6. rollback or remain frozen;
7. build challenger repair;
8. revalidate;
9. promote only through gates.

---

# 63. Champion registry

Maintain a set:

$$
\boxed{
\mathcal C_{\mathrm{cert}}
}
$$

of historical certified pairs whose required external contracts are still current.

Rollback can choose among them.

---

# 64. Best fallback champion

For certified risk objective:

$$
\boxed{
C_{\mathrm{fb}}
\in
\arg\min_{
C\in\mathcal C_{\mathrm{cert}}
}
[
U(C)+c_{\mathrm{switch}}(C)
].
}
$$

---

# 65. Regime-aware rollback

A champion can be certified for:

$$
\nu_R^0
$$

but not:

$$
\nu_R^1.
$$

Registry queries must filter by current regime compatibility.

---

# 66. Continual update action

At each cycle choose:

$$
\boxed{
a_t
\in
\mathcal A_{\mathrm{cont}}.
}
$$

---

# 67. Continual state

$$
\boxed{
X_t
=
(
C_t,
\mathcal C_{\mathrm{cert}},
D_A,
D_V,
D_I,
\nu_R,
B_t,
\mathsf{Prov}_t
).
}
$$

---

# 68. Bellman form

For finite horizon:

$$
\boxed{
V_t(X)
=
\min_{
a\in\mathcal A(X)
}
\left[
c(a)
+
E_Y
V_{t+1}(
\Phi(X,a,Y)
)
\right].
}
$$

This is standard dynamic programming.

---

# 69. VWDC07-T11 — Continual action stopping/freeze criterion

## Theorem VWDC07-T11

If KEEP/FREEZE has cost-to-go:

$$
R_t(X),
$$

then it is optimal iff:

$$
\boxed{
R_t(X)
\le
Q_t(X,a)
\quad
\forall
a
\neq
\mathrm{KEEP/FREEZE}.
}
$$

### Proof

Bellman minimum.

 $\square$

---

# 70. Update-action value error

Suppose true continual-action values:

$$
Q(X,a)
$$

and estimates:

$$
\widehat Q(X,a)
$$

satisfy:

$$
\boxed{
|
Q(X,a)
-
\widehat Q(X,a)
|
\le
\epsilon_a.
}
$$

---

# 71. VWDC07-T12 — Continual update-action regret bound

## Theorem VWDC07-T12

Let estimated controller choose:

$$
\widehat a
\in
\arg\min_a
\widehat Q(X,a)
$$

and true best action be:

$$
a^\star
\in
\arg\min_a
Q(X,a).
$$

Then:

$$
\boxed{
Q(X,\widehat a)
-
Q(X,a^\star)
\le
\epsilon_{\widehat a}
+
\epsilon_{a^\star}.
}
$$

Hence with uniform error:

$$
\epsilon,
$$

$$
\boxed{
\operatorname{Regret}
\le
2\epsilon.
}
$$

### Proof

Standard estimated-argmin comparison.

 $\square$

---

# 72. Update policy is itself uncertain

The system may not know whether:

- world-only update;
- policy-only update;
- RTC-only update;
- joint update;

is best.

A conservative governance policy can maintain uncertainty over these choices.

---

# 73. World-only update

Use when external residual indicates predictive/dynamics mismatch but current policy remains supported.

---

# 74. RTC-only update

Use when new external evidence changes transport discrepancy/scope without requiring world-model changes.

---

# 75. Policy-only update

Use when world and RTC remain current but objective/policy can improve safely inside supported regions.

---

# 76. Joint update

Use when changed model semantics require recalibration and policy recomputation.

This has the largest validation burden.

---

# 77. Freeze

Use when evidence is insufficient to identify which update is justified.

"Do nothing" can be the correct continual action.

---

# 78. Shadow challenger

A challenger can run:

- predictions;
- recommended actions;
- world updates;

without controlling reality.

This collects comparison evidence with less intervention risk.

---

# 79. Shadow limitation

Shadow policy does not reveal outcomes of unexecuted challenger actions unless outcome feedback is observable independently.

Counterfactual support remains a limitation.

---

# 80. A/B or randomized deployment

Controlled randomized exposure can identify challenger performance more directly.

It may be inappropriate in high-risk domains.

Risk/authority policy applies.

---

# 81. Safe exploration

External data collection for adaptation is still an intervention problem.

Do not optimize identifiability at the expense of hard safety constraints.

---

# 82. Deployment-feedback IPS

If controlled exploration/logging probabilities are recorded, IPS/DR methods can support evaluation of candidate policies from deployed data.

This is classical off-policy evaluation.

---

# 83. Selective-label feedback

Some outcomes are observed only after certain decisions.

For example:

- failure label only after system proceeds;
- human outcome only after review;
- long-term reward only after action execution.

Missingness can be policy dependent.

---

# 84. Long-term feedback

Delayed outcomes should remain attached to the policy/version that caused them.

Do not credit them solely to the current policy version.

---

# 85. Temporal attribution

Reality outcome at time:

$$
t+k
$$

can depend on multiple prior actions/policies.

Lineage must record the causal/deployment history.

---

# 86. Feedback contamination across versions

A new policy can receive delayed outcomes generated by an old policy.

Training without version attribution can create false update signals.

---

# 87. Cohort/version window

Each feedback record stores:

```text
world_version
rtc_version
policy_version
safety_version
action_time
outcome_time
deployment_context
propensity
```

---

# 88. Continual calibration queue

Delayed feedback updates the correct historical calibration object first, then may be transported to current version only through a version-transfer assumption.

---

# 89. Old feedback is not automatically current feedback

A policy/model update can change semantics.

Historical outcomes require compatibility checks before reuse.

---

# 90. Regime drift versus model failure

Residual increase can come from:

- reality drift;
- sensor drift;
- world-model degradation;
- policy occupancy shift;
- evaluator change.

Drift detection alone does not identify the cause.

---

# 91. Diagnosis before update

Use WDC/VWDC diagnostic actions before choosing which component to update.

This connects back to GVSS-05–08 diagnostic control.

---

# 92. Multi-component fault belief

Maintain:

$$
\boxed{
b_t(
F_{\mathrm{world}},
F_{\mathrm{RTC}},
F_{\mathrm{sensor}},
F_{\mathrm{policy}},
F_{\mathrm{reality}}
).
}
$$

Update action should follow diagnostic evidence.

---

# 93. Blind retraining no-go

Retraining world model whenever residual increases can overfit:

- sensor faults;
- transient incidents;
- policy distribution shift.

Component diagnosis matters.

---

# 94. VWDC07-N8 — Residual increase does not identify which continual component failed

## Counterexample

The same prediction residual can be produced by:

1. world-model bias;
2. sensor bias;
3. reality regime shift.

Observed scalar residual alone is identical.

Therefore:

$$
\boxed{
\text{residual drift}
\not\Rightarrow
\text{identified update target}.
}
$$

 $\square$

---

# 95. Champion–challenger gate by component

A world-model challenger and policy challenger need separate promotion evidence.

Do not promote a joint bundle when only one component was validated unless bundle interactions are also tested.

---

# 96. Bundle interaction

A better world model can make an old policy worse.

A better policy under old world model can fail under new world model.

Joint bundles require joint deployment evaluation.

---

# 97. VWDC07-N9 — Componentwise improvement does not guarantee bundle improvement

## Counterexample

World model $M_1$ improves prediction accuracy over $M_0$.

Policy $\pi_1$ improves simulated reward over $\pi_0$ under $M_0$.

But $\pi_1$ exploits a behavior represented differently in $M_1$ and performs worse in the combined bundle:

$$
(M_1,\pi_1).
$$

Thus separate component rankings do not imply bundle ranking.

 $\square$

---

# 98. Bundle validation

Promote:

$$
(M',RTC',\pi')
$$

as a bundle when interactions can affect decisions.

---

# 99. Safety memory

Old safety incidents, constraints, and certified envelopes should remain available during adaptation.

Do not let recent reward data erase them.

---

# 100. Catastrophic forgetting boundary

Continual adaptation can forget old regimes or constraints.

Current safe-policy-update research explicitly targets preservation of previous safety properties.

VWDC requires old contract/safety evidence to remain versioned and queryable.

---

# 101. Protected regression suite

Before promotion, replay:

- old critical incidents;
- old certified regions;
- known edge cases;
- safety tests;
- transport tests.

This is engineering governance.

---

# 102. Regression gate

Candidate must not violate protected hard contracts.

Soft performance can trade off only where policy permits.

---

# 103. Protected region

Let:

$$
\mathcal Z_{\mathrm{protected}}
$$

contain state/action/task regions with required historical guarantees.

---

# 104. Regression debt

Candidate degradation on protected region can veto promotion even if average current-regime score improves.

---

# 105. Current guarded continual-adaptation precedent

Recent work on validation-gated online adaptation separates monitoring, diagnosis, adaptation, safety audit, and orchestration, and uses challenger validation before promotion.

VWDC's structure is compatible with this pattern.

---

# 106. Continual digital-twin precedent

Recent adaptive digital-twin work combines:

- drift detection;
- targeted parameter updates;
- statistical validation;
- robust model-predictive decisions.

This is a direct current precedent for continual world/RTC/policy maintenance.

---

# 107. Telecom world-model precedent

Current telecom-world-model research explicitly highlights:

- continual adaptation;
- shadow-mode deployment;
- versioning;
- validation;
- rollback.

This supports the governance vocabulary.

---

# 108. Untwinning/rollback precedent

Recent network digital-twin work studies rollback/checkpoint mechanisms for removing or reversing contributions while maintaining twin integrity.

VWDC rollback semantics remain broader and contract based.

---

# 109. Self-improving loop precedent

Current self-improving agent/model research identifies self-confirmation and loop dependence as recurring risks when systems train/evaluate on signals generated by their own behavior.

VWDC extends this concern to reality-facing world-policy loops.

---

# 110. Continual lifecycle state

Suggested runtime:

```text
champion_pair
challenger_pairs
historical_certified_pairs
reality_regime
feedback_adaptation_stream
feedback_validation_stream
incident_audit_stream
promotion_alpha_budget
drift_status
rollback_candidates
freeze_status
```

---

# 111. Champion packet

```text
champion_id
world_version
rtc_versions
policy_version
safety_version
authority_version
certified_region
risk_bound
promotion_evidence
promotion_delta
```

---

# 112. Challenger packet

```text
challenger_id
parent_champion
changed_components
training_data_ids
shadow_results
validation_data_ids
validation_result
protected_regression_result
promotion_status
```

---

# 113. Rollback packet

```text
rollback_event_id
failed_or_rejected_version
target_champion
current_reality_regime
rtc_recheck
safety_recheck
switch_cost
reason
```

---

# 114. Incident packet

```text
incident_id
reality_time
active_deployment_pair
state_action_context
observed_outcome
contradicted_contract
dependency_blast_radius
immediate_mode
replay_required
```

---

# 115. Promotion ledger

```text
promotion_index
delta_budget
cumulative_delta_spent
candidate
champion
validation_statistic
protected_gate
decision
```

---

# 116. Lifetime confidence

Do not display:

> every update passed 95%.

without also displaying lifecycle error accounting.

Prefer:

```text
per_test_delta
lifetime_delta_budget
delta_spent
remaining_delta_budget
```

---

# 117. Promotion alpha exhaustion

If lifecycle statistical promotion budget is exhausted:

- collect stronger/new independent evidence;
- use a revised sequential-valid procedure;
- freeze;
- require human governance.

Do not silently reset history.

---

# 118. Multiple testing is one risk, not all risk

Alpha spending controls stated statistical promotion errors under its assumptions.

It does not cover:

- model misspecification;
- hidden confounding;
- transport drift;
- safety-specification errors.

Keep those debts separate.

---

# 119. Closed-loop validity vector

Define:

$$
\boxed{
\mathbf D_t
=
(
D_{\mathrm{prediction}},
D_{\mathrm{transport}},
D_{\mathrm{safety}},
D_{\mathrm{selection}},
D_{\mathrm{drift}},
D_{\mathrm{promotion}},
D_{\mathrm{provenance}}
).
}
$$

---

# 120. Stability notion

A continual system is not "stable" merely because parameters converge.

A useful governance notion can require:

- bounded certified debt;
- rollback availability;
- no protected-region regression;
- controlled version churn;
- current reality tether.

VWDC-07 does not claim one universal stability theorem.

---

# 121. Frozen-regime certificate stability

VWDC07-T3 gives one minimal stability result:

> under frozen reality regime and monotone promotion rule, champion certified upper risk does not worsen.

This is intentionally limited.

---

# 122. Nonstationary reality

Under true regime drift, old guarantees may expire.

A continual system should prefer honest reversion to:

```text
UNCERTIFIED / FALLBACK
```

over pretending certificate monotonicity continues.

---

# 123. Update churn

Repeated promote/rollback oscillation can be costly.

Use hysteresis, minimum dwell time, or stronger promotion margins if necessary.

Engineering policy only.

---

# 124. Model promotion versus deployment promotion

A model can be promoted to:

```text
VALIDATED_MODEL
```

without immediately becoming:

```text
ACTIVE_DEPLOYMENT
```

Deployment is a separate decision.

---

# 125. RTC promotion

A new RTC can become current while policy remains unchanged.

---

# 126. Policy promotion

A policy can be updated while world model remains unchanged if existing RTC/safety support is sufficient.

---

# 127. Joint promotion

Highest burden.

All interactions must be covered by validation.

---

# 128. Reality incident priority

A severe external incident can override performance statistics and immediately trigger:

- fallback;
- freeze;
- audit.

Decision priority is policy defined.

---

# 129. Incident severity

Suggested:

```text
INFO
MINOR
MAJOR
CRITICAL
```

Critical incidents can bypass ordinary challenger schedule.

---

# 130. Emergency rollback

Emergency rollback still requires checking that rollback target is current enough to be safer than staying active.

If no certified target remains, use safe fallback/stop.

---

# 131. No valid rollback target

Possible status:

```text
NO_CERTIFIED_ROLLBACK_TARGET
```

Then:

- stop;
- human control;
- minimal safe mode.

---

# 132. World model rollback versus policy rollback

Can rollback:

- world only;
- policy only;
- RTC only;
- full bundle.

Dependency graph determines compatible combinations.

---

# 133. Compatibility matrix

Maintain allowed version combinations:

$$
\boxed{
\mathsf{Compat}(
\nu_W,
\nu_{\mathrm{RTC}},
\nu_\pi,
\nu_{\mathrm{safety}}
).
}
$$

Do not mix arbitrary historical versions.

---

# 134. VWDC07-N10 — Individually historical versions need not form a valid mixed bundle

## Counterexample

Old policy expects observation schema from old world model.

New RTC expects new action semantics.

Combining old policy with new world/RTC may be type/semantic incompatible.

Therefore:

$$
\boxed{
\text{historically valid components}
\not\Rightarrow
\text{arbitrarily mixed valid bundle}.
}
$$

 $\square$

---

# 135. Bundle rollback

Prefer rollback to a previously certified compatible tuple:

$$
C_k
$$

rather than ad hoc component mixing.

---

# 136. Online continual learning data

All feedback should remain immutable and version attributed.

Retraining can create new derived datasets.

Do not overwrite original logs.

---

# 137. Data tombstones

If data later invalidated:

- mark;
- propagate dependency;
- retrain/replay if needed.

Do not silently delete without provenance.

---

# 138. Privacy/regulatory removals

Selective data removal may require model/twin rollback or unlearning.

This is orthogonal to predictive drift but interacts with version lineage.

---

# 139. Auditability

An external auditor should reconstruct:

1. which policy acted;
2. which RTC authorized it;
3. which world model supported it;
4. what feedback later arrived;
5. which update consumed that feedback;
6. why a challenger was promoted;
7. whether rollback remained possible.

---

# 140. Continual scientific integrity

The loop should preserve a distinction between:

- evidence generated by deployment;
- evidence used for adaptation;
- evidence used for validation;
- evidence used for audit.

Without this, the system can progressively certify itself with its own selected data.

---

# 141. Main no-go

$$
\boxed{
\textbf{
A closed-loop world system can become increasingly self-consistent while becoming less externally informative.
}
}
$$

This can occur through:

- selective exposure;
- performative feedback;
- shared evaluator bias;
- repeated in-sample validation;
- drift outside support.

---

# 142. Main positive principle

Use:

- propensity/provenance logging;
- independent or valid sequential promotion evidence;
- immutable versions;
- champion–challenger shadowing;
- lifecycle error budgets;
- reality-regime detection;
- contract-aware rollback.

---

# 143. Current literature boundary — continual learning

VWDC-07 does not claim continual learning, concept drift, or online adaptation as new.

---

# 144. Current literature boundary — performativity

VWDC-07 does not claim performative/self-consuming feedback loops or selective labels as new.

---

# 145. Current literature boundary — safe policy adaptation

VWDC-07 does not claim policy-update safety methods or safe continual RL as new.

---

# 146. Current literature boundary — digital-twin governance

VWDC-07 does not claim versioning, champion–challenger, shadow deployment, or rollback engineering as new.

---

# 147. Candidate VWDC-specific synthesis

Subject to broader literature audit, candidate bridge-specific synthesis is:

1. continual deployment state as a versioned tuple of world model, RTC, policy, safety, and authority contracts;
2. explicit adaptation/validation/incident stream separation for reality feedback;
3. feedback propensity/support governance to prevent closed-loop self-confirmation;
4. statistical challenger-promotion certificates plus lifecycle alpha spending;
5. conditional rollback semantics that distinguish software rollback from reality-regime rollback;
6. local certified-action inheritance with explicit closed-loop support caveat;
7. incident-driven dependency invalidation connected to world/RTC/policy rollback;
8. immutable version lineage and compatible-bundle rollback;
9. update-action Bellman control over KEEP/UPDATE/REVALIDATE/ROLLBACK/FREEZE/FALLBACK.

No strong novelty claim is made in v0.1.

---

# 148. What VWDC-07 proves

Under explicit hypotheses, VWDC-07 proves:

1. deployment-selected feedback can reverse apparent model/policy quality;
2. IPS yields unbiased target-policy feedback value under correct propensities and support;
3. unsupported action/context outcomes are not identified from deployment logs without structural assumptions;
4. on-policy feedback can be perfectly self-confirming outside visited support;
5. independent held-out paired loss differences yield the stated promotion confidence certificate;
6. frozen-regime champion certificate upper risk is nonincreasing under monotone promotion rules;
7. lifecycle false-promotion probability is bounded by the sum of per-promotion error budgets;
8. repeating a 95% test does not produce a lifetime 95% guarantee;
9. rollback restores an old certificate only when its RTC/safety/reality-regime assumptions remain current;
10. software/version rollback cannot restore an expired reality transport contract after regime drift;
11. rollback is preferred on a one-step certified-risk objective under the stated threshold;
12. fixed-window bounded residual means yield the stated drift-rejection certificate;
13. immutable update/rollback version lineage remains acyclic under strict creation order;
14. a locally contract-preserving policy inherits action-level certificates while remaining inside the certified region;
15. local action certification does not guarantee the closed-loop trajectory remains in the certified region;
16. in-sample promotion can be perfectly self-confirming;
17. reality incidents propagate invalidation through required dependency descendants;
18. residual drift alone does not identify which world/RTC/sensor/policy/reality component failed;
19. componentwise improvements do not guarantee joint bundle improvement;
20. estimated continual-update action values yield the stated one-step regret bound;
21. historically valid individual versions need not form an arbitrary compatible deployment bundle.

---

# 149. What VWDC-07 does not prove

It does not prove:

- logging propensities are always known;
- IPS is low variance under small support;
- one holdout remains valid after arbitrary repeated adaptive reuse;
- alpha spending covers model misspecification or safety-specification error;
- rollback is safe after reality drift;
- old safety guarantees survive policy updates outside their certified task distributions;
- one residual statistic identifies drift cause;
- champion certificate monotonicity implies true performance monotonicity;
- continual adaptation is computationally stable;
- a universal bundle-compatibility rule exists;
- a closed-loop system can eliminate external validation.

---

# 150. Proposed VWDC-08

The next paper should study the **global stability and governance of the entire continual World–RTC–Policy–Reality loop**:

$$
\boxed{
\textbf{
VWDC-08 — Continual World Governance, Certificate Stability, and Reflexive Deployment Invariants
}
}
$$

Chinese:

**持續世界治理、證書穩定性與反身部署不變量**

Main questions:

1. What invariants should never be violated during continual update?
2. Can a safe/certified envelope be kept forward invariant?
3. How should version churn and rollback debt be bounded?
4. What is the stable notion of "best known certified pair" under drift?
5. When should the entire adaptation loop be suspended?
6. Can update rules be designed so protected certificates only improve in frozen regimes?
7. How should multiple WDC/VWDC worlds coordinate a shared reality-facing champion?
8. What constitutes convergence when reality itself is nonstationary?

---

# 151. References

1. Yi-Ping Chen et al., **A Continual Validation, Updating, and Decision-Making Framework for Self-Adaptive Digital Twins via Robust Model Predictive Control**, arXiv:2607.18164, 2026.
2. Maksim Anisimov, Francesco Belardinelli, Matthew Wicker, **SafeAdapt: Provably Safe Policy Updates in Deep Reinforcement Learning**, arXiv:2604.09452, 2026.
3. Yaxuan Wang et al., **Observations and Remedies for Large Language Model Bias in Self-Consuming Performative Loop**, arXiv:2601.05184, 2026.
4. **Validation-Gated Multi-Agent Governance for Online Continual Model Adaptation**, arXiv:2606.03321, 2026.
5. **Telecom World Models: Unifying Digital Twins, Foundation Models, and Generative AI**, arXiv:2604.06882, 2026.
6. Zifan Zhang et al., **Network Digital Untwinning: Towards Backward Optimization of Digital Twins**, arXiv:2605.00169, 2026.
7. Joost Mertens, Joachim Denil, **Reusing Model Validation Methods for the Continuous Validation of Digital Twins of Cyber-Physical Systems**, arXiv:2512.04117, 2025.
8. Josip Josifovski et al., **Safe Continual Domain Adaptation after Sim2Real Transfer of Reinforcement Learning Policies in Robotics**, arXiv:2503.10949, 2025.
9. VWDC-01–06, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, and frozen RRT-20, internal series artifacts, 2026.

---

# 152. Conclusion

VWDC-06 made world-to-reality policy deployment obey a transport contract.

VWDC-07 makes the deployed system capable of changing while preserving evidence about why it changed.

Reality feedback is policy selected.

Therefore continual learning cannot treat deployment logs as neutral external truth.

The loop must preserve:

$$
\boxed{
\mathcal D_{\mathrm{adapt}}
\neq
\mathcal D_{\mathrm{validate}}
\neq
\mathcal D_{\mathrm{incident}}.
}
$$

Promotion must be gated.

Repeated tests require lifecycle error accounting.

Rollback restores a previous software/model bundle only when the old external contracts remain valid in the current reality regime.

And local preservation of certified actions does not guarantee the updated policy will remain inside the old certified state region.

The canonical VWDC-07 principle is:

$$
\boxed{
\textbf{
A continual world system must never use the reality it selectively created
as unqualified proof that its latest world, contract, and policy are correct.
Adapt aggressively in challengers, validate with provenance-aware evidence,
promote through explicit gates, preserve old certified bundles,
and roll back only to contracts that reality has not already outgrown.
}
}
$$

This establishes a continual, rollback-capable, evidence-aware governance layer for reality-facing WDC systems.

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
