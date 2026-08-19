# VWDC-06 — Transport-Aware World Decisions, Policy Transfer, and Reality-Gap Robust Control
## 轉移感知世界決策、策略搬運與現實差距穩健控制：部署證書、Reality Regret、Probe/Fallback 與自致分佈漂移

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 06  
**Depends on:** VWDC-01–05, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal transport-aware decision/control paper. Action-wise deployment certificates, real-action regret under transport intervals, robust lower-bound action selection, unsupported-action non-identifiability, perfect-probe/fallback thresholds, fixed-policy discounted sim-to-real value bounds, transferred-policy regret bounds, deployment-induced occupancy-shift debt, RTC admissibility under policy shift, supported-action fallback gates, online local calibration concentration, and finite-horizon deploy/probe/fallback Bellman statements are proved under explicit hypotheses. Robust MDP/RL, domain randomization, sim-to-real policy transfer, offline-RL pessimism, safe policy adaptation, and digital-twin control are established neighboring research and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** sim-to-real policy transfer, robust control, digital twin, policy deployment, reality gap, transport contract, safe fallback, probe value, unsupported action, occupancy shift, reality regret, WDC

---

# Abstract

VWDC-05 introduced a claim-specific Reality Transport Contract:

$$
\boxed{
\mathsf{RTC}_Q
=
(
Q,
\mathcal Z,
\nu_W,
\nu_R,
T_Q,
\mathcal V,
\mathcal A,
\Delta_Q,
\mathcal D_{\mathrm{ext}},
\mathsf{Expiry},
\mathsf{Prov}
).
}
$$

That contract tells us when a world-derived quantity may support a reality claim.

VWDC-06 asks the operational question:

> **When may a decision or policy optimized inside a WDC world be executed in reality?**

A simulation-optimal action is not automatically reality-optimal.

A reality-facing controller therefore maintains action-wise transported value estimates:

$$
\boxed{
\widehat Q_W(s,a)
}
$$

and Reality Transport Contract uncertainty radii:

$$
\boxed{
\delta(s,a).
}
$$

The contract asserts, on supported state/action region:

$$
\boxed{
|
Q_R(s,a)
-
\widehat Q_W(s,a)
|
\le
\delta(s,a).
}
$$

The controller's deployment action set is:

$$
\boxed{
\mathcal A_{\mathrm{deploy}}
=
\{
\mathrm{DEPLOY},
\mathrm{ROBUST\_DEPLOY},
\mathrm{PROBE},
\mathrm{SAFE\_FALLBACK},
\mathrm{HUMAN\_REVIEW},
\mathrm{STOP}
\}.
}
$$

The first result is a direct deployment certificate.

Let:

$$
\widehat a
\in
\arg\max_a
\widehat Q_W(s,a).
$$

If:

$$
\boxed{
\widehat Q_W(s,\widehat a)
-
\delta(s,\widehat a)
>
\max_{b\neq\widehat a}
\left[
\widehat Q_W(s,b)
+
\delta(s,b)
\right],
}
$$

then:

$$
\boxed{
\widehat a
=
\arg\max_a
Q_R(s,a)
}
$$

for every reality action-value vector consistent with the RTC intervals.

Thus deployment can be certified when the simulated decision margin dominates transport debt.

When this condition fails, the controller has no certificate that the simulated optimum survives the reality gap.

---

# 1. Action-wise reality transport

Let:

$$
s
\in
\mathcal S
$$

be the current deployment state/context.

Let:

$$
a
\in
\mathcal A.
$$

The world model supplies:

$$
\widehat Q_W(s,a).
$$

The RTC supplies a supported region:

$$
\mathcal Z_{\mathrm{supp}}
\subseteq
\mathcal S\times\mathcal A
$$

and transport error:

$$
\delta(s,a).
$$

---

# 2. Supported action

## Definition VWDC06-D1

Action $a$ is RTC-supported at state $s$ if:

$$
\boxed{
(s,a)
\in
\mathcal Z_{\mathrm{supp}}
}
$$

and the relevant RTC is current.

---

# 3. Transport interval

## Definition VWDC06-D2

For supported pair:

$$
(s,a),
$$

define:

$$
\boxed{
I_R(s,a)
=
[
\widehat Q_W(s,a)-\delta(s,a),
\widehat Q_W(s,a)+\delta(s,a)
].
}
$$

The contract claims:

$$
Q_R(s,a)
\in
I_R(s,a).
$$

---

# 4. Simulated optimum

$$
\boxed{
\widehat a_W
\in
\arg\max_a
\widehat Q_W(s,a).
}
$$

---

# 5. Reality optimum

$$
\boxed{
a_R^\star
\in
\arg\max_a
Q_R(s,a).
}
$$

These need not agree.

---

# 6. VWDC06-T1 — Transport-margin deployment certificate

## Theorem VWDC06-T1

Assume every candidate action is RTC-supported and satisfies:

$$
|
Q_R(s,a)
-
\widehat Q_W(s,a)
|
\le
\delta(s,a).
$$

If some action $\widehat a$ satisfies:

$$
\boxed{
\widehat Q_W(s,\widehat a)
-
\delta(s,\widehat a)
>
\max_{b\neq\widehat a}
[
\widehat Q_W(s,b)
+
\delta(s,b)
],
}
$$

then $\widehat a$ is the unique reality-optimal action for every reality value vector consistent with the intervals.

### Proof

For every $b\neq\widehat a$:

$$
Q_R(s,\widehat a)
\ge
\widehat Q_W(s,\widehat a)
-
\delta(s,\widehat a)
$$

and:

$$
Q_R(s,b)
\le
\widehat Q_W(s,b)
+
\delta(s,b).
$$

Apply the strict margin condition.

 $\square$

---

# 7. Interpretation

The criterion is stronger than:

> simulated margin is large.

It requires:

> simulated margin exceeds the transport uncertainty of both winner and competitors.

Thus:

$$
\boxed{
\text{large simulation advantage}
-
\text{large transport debt}
}
$$

can still yield no deployment certificate.

---

# 8. Nominal deployment region

Define:

$$
\boxed{
\mathcal D_{\mathrm{cert}}
=
\{
s:
\text{VWDC06-T1 holds}
\}.
}
$$

Inside this region, nominal simulation and transported reality decisions agree under the RTC.

---

# 9. Uncertified region

Outside:

$$
\mathcal D_{\mathrm{cert}},
$$

the simulated optimum can still be correct.

It is merely not certified by the current RTC.

Possible actions:

- robust deploy;
- external probe;
- safe fallback;
- human review;
- stop.

---

# 10. VWDC06-T2 — Reality action regret under transport intervals

## Theorem VWDC06-T2

Let:

$$
\widehat a
\in
\arg\max_a
\widehat Q_W(s,a)
$$

and:

$$
a_R^\star
\in
\arg\max_a
Q_R(s,a).
$$

Under action-wise interval bounds:

$$
|
Q_R(s,a)-\widehat Q_W(s,a)|
\le
\delta(s,a),
$$

the real regret of deploying $\widehat a$ satisfies:

$$
\boxed{
Q_R(s,a_R^\star)
-
Q_R(s,\widehat a)
\le
\delta(s,a_R^\star)
+
\delta(s,\widehat a).
}
$$

Hence:

$$
\boxed{
\operatorname{Regret}_R
\le
2\delta_{\max}.
}
$$

### Proof

$$
\begin{aligned}
Q_R(a_R^\star)
-
Q_R(\widehat a)
&\le
\widehat Q_W(a_R^\star)
+
\delta(a_R^\star)
-
[
\widehat Q_W(\widehat a)
-
\delta(\widehat a)
]
\\
&\le
\delta(a_R^\star)
+
\delta(\widehat a),
\end{aligned}
$$

because:

$$
\widehat Q_W(\widehat a)
\ge
\widehat Q_W(a_R^\star).
$$

 $\square$

---

# 11. Transport debt becomes decision debt

VWDC-05's external-validity debt is therefore not only epistemic.

It directly upper-bounds possible action regret.

---

# 12. Robust lower-bound deployment

Define:

$$
\boxed{
L(s,a)
=
\widehat Q_W(s,a)
-
\delta(s,a).
}
$$

Choose:

$$
\boxed{
a_{\mathrm{LCB}}
\in
\arg\max_{
a\in\mathcal A_{\mathrm{supp}}(s)
}
L(s,a).
}
$$

---

# 13. VWDC06-T3 — Robust lower-bound guarantee

## Theorem VWDC06-T3

For every reality value vector consistent with the RTC:

$$
\boxed{
Q_R(s,a_{\mathrm{LCB}})
\ge
\max_{
a\in\mathcal A_{\mathrm{supp}}(s)
}
L(s,a).
}
$$

### Proof

For selected action:

$$
Q_R(s,a_{\mathrm{LCB}})
\ge
L(s,a_{\mathrm{LCB}}).
$$

By definition:

$$
L(s,a_{\mathrm{LCB}})
=
\max_aL(s,a).
$$

 $\square$

This is a robust performance floor, not proof of reality optimality.

---

# 14. Safe fallback

Let:

$$
a_F
$$

be a fallback action with independently certified reality value lower bound:

$$
\boxed{
Q_R(s,a_F)
\ge
G_F(s).
}
$$

---

# 15. VWDC06-T4 — Supported-action fallback gate

## Theorem VWDC06-T4

If:

$$
\boxed{
\max_{
a\in\mathcal A_{\mathrm{supp}}(s)
}
L(s,a)
<
G_F(s),
}
$$

then every supported simulation action has a lower certified floor below the fallback guarantee, and choosing the fallback maximizes the available certified lower bound.

### Proof

Immediate comparison of certified lower bounds.

 $\square$

This is a pessimistic risk policy.

It need not maximize expected reward.

---

# 16. Unsupported actions

Suppose:

$$
(s,a_u)
\notin
\mathcal Z_{\mathrm{supp}}.
$$

No RTC interval is available.

---

# 17. VWDC06-N1 — Unsupported-action reality value is not identified by supported RTC data alone

## Proposition VWDC06-N1

Without structural/generalization assumptions, there exist two reality models:

$$
R_1,R_2
$$

that agree on every RTC-supported state/action pair and differ arbitrarily on:

$$
(s,a_u).
$$

Therefore supported validation data alone do not identify:

$$
Q_R(s,a_u).
$$

### Proof

Define the two reality models identically on supported pairs.

Assign different rewards/transitions to the unsupported pair.

No supported observation distinguishes them.

 $\square$

---

# 18. Consequence

If the simulator's best action is unsupported, there is no distribution-free guarantee that it is safe or valuable in reality.

Therefore:

$$
\boxed{
\text{sim-optimal + unsupported}
\not\Rightarrow
\text{deployable}.
}
$$

---

# 19. Explicit unsupported-action risk policies

Possible policies:

```text
PROBE_FIRST
SAFE_FALLBACK
HUMAN_REVIEW
STRUCTURAL_EXTRAPOLATION_WITH_BOUND
ROBUST_WORST_CASE
FORBID
```

The policy must be explicit.

---

# 20. Probe action

An external probe can reduce action-value uncertainty before deployment.

Let:

$$
c_P
$$

be probe cost.

---

# 21. Two-regime risky-action example

Compare:

- risky action $a_R$ ;
- safe fallback value normalized to $0$.

Risky action gives:

$$
+G
$$

in good regime with probability $p$ and:

$$
-L
$$

in bad regime with probability:

$$
1-p,
$$

where:

$$
G,L>0.
$$

Without probe, expected risky value:

$$
\boxed{
V_R
=
pG-(1-p)L.
}
$$

Optimal no-probe value is:

$$
\boxed{
V_{\mathrm{noprobe}}
=
\max(
0,
pG-(1-p)L
).
}
$$

---

# 22. Perfect regime probe

A perfect probe reveals good/bad regime.

Then controller chooses risky action only in good regime.

Probe value before cost:

$$
pG.
$$

After cost:

$$
pG-c_P.
$$

---

# 23. VWDC06-T5 — Perfect-probe versus fallback threshold

## Theorem VWDC06-T5

The perfect probe is strictly better than the best immediate action iff:

$$
\boxed{
c_P
<
\min(
pG,
(1-p)L
).
}
$$

### Proof

Probe advantage is:

$$
pG
-
\max(
0,
pG-(1-p)L
)
-
c_P.
$$

Use identity:

$$
x-\max(0,x-y)
=
\min(x,y)
$$

for:

$$
x,y\ge0.
$$

 $\square$

---

# 24. Interpretation

Probe value is highest near the decision boundary.

If risky action is almost certainly good or almost certainly bad, the value of perfect information is small.

---

# 25. Human review

Human review can be modeled as a noisy/costly probe.

Its value depends on:

- accuracy;
- decision consequence;
- latency;
- cost.

No universal preference over machine probe is claimed.

---

# 26. Current safe Sim2Real precedent

Current 2026 Sim2Real work explicitly adjusts deployment risk based on uncertainty about the target environment context.

Other work uses uncertainty estimates to adapt policies or focus real/sim exploration.

VWDC's RTC acts as a contract-level version of the same broad deployment concern.

---

# 27. Policy transfer

A policy:

$$
\pi_W
$$

is optimized in world model:

$$
M_W.
$$

Reality executes:

$$
\pi_W
$$

under:

$$
M_R.
$$

Policy value can differ due to:

- reward mismatch;
- transition mismatch;
- observation mismatch;
- action execution mismatch.

---

# 28. Discounted MDP setting

Assume:

$$
\gamma\in[0,1).
$$

World and reality share state/action spaces for this theorem.

Rewards:

$$
r_W,r_R
\in
[0,R_{\max}].
$$

For every:

$$
(s,a),
$$

assume:

$$
\boxed{
|r_R(s,a)-r_W(s,a)|
\le
\epsilon_r.
}
$$

Transition kernels satisfy:

$$
\boxed{
\operatorname{TV}
(
P_R(\cdot\mid s,a),
P_W(\cdot\mid s,a)
)
\le
\epsilon_P.
}
$$

---

# 29. VWDC06-T6 — Fixed-policy discounted Sim2Real value bound

## Theorem VWDC06-T6

For any fixed policy $\pi$:

$$
\boxed{
\|
V_R^\pi
-
V_W^\pi
\|_\infty
\le
\frac{
\epsilon_r
}{
1-\gamma
}
+
\frac{
\gamma R_{\max}\epsilon_P
}{
(1-\gamma)^2
}.
}
$$

### Proof

For any state:

$$
\begin{aligned}
|
V_R^\pi(s)-V_W^\pi(s)
|
&\le
\epsilon_r
+
\gamma
\left|
E_{P_R}
V_R^\pi
-
E_{P_W}
V_W^\pi
\right|
\\
&\le
\epsilon_r
+
\gamma
\|
V_R^\pi-V_W^\pi
\|_\infty
+
\gamma
\frac{
R_{\max}
}{
1-\gamma
}
\epsilon_P.
\end{aligned}
$$

The last term uses the bounded-function TV inequality for:

$$
0
\le
V_W^\pi
\le
R_{\max}/(1-\gamma).
$$

Take the supremum and rearrange.

 $\square$

---

# 30. Horizon amplification

Transition mismatch is amplified by approximately:

$$
(1-\gamma)^{-2}.
$$

Long-horizon policies can therefore be much more sensitive to small local dynamics mismatch.

---

# 31. Uniform policy transport error

Define:

$$
\boxed{
\Delta_V
=
\frac{
\epsilon_r
}{
1-\gamma
}
+
\frac{
\gamma R_{\max}\epsilon_P
}{
(1-\gamma)^2
}.
}
$$

Then:

$$
\boxed{
|
V_R^\pi(s)-V_W^\pi(s)
|
\le
\Delta_V
}
$$

for every fixed policy under the theorem's assumptions.

---

# 32. World-optimal versus reality-optimal policy

Let:

$$
\pi_W^\star
\in
\arg\max_\pi
V_W^\pi,
$$

$$
\pi_R^\star
\in
\arg\max_\pi
V_R^\pi.
$$

---

# 33. VWDC06-T7 — Transferred-policy reality regret bound

## Theorem VWDC06-T7

If the fixed-policy transport bound:

$$
|
V_R^\pi-V_W^\pi
|
\le
\Delta_V
$$

holds uniformly for all policies under consideration, then:

$$
\boxed{
V_R^{\pi_R^\star}
-
V_R^{\pi_W^\star}
\le
2\Delta_V.
}
$$

### Proof

$$
\begin{aligned}
V_R^{\pi_R^\star}
-
V_R^{\pi_W^\star}
&\le
V_W^{\pi_R^\star}
+
\Delta_V
-
[
V_W^{\pi_W^\star}
-
\Delta_V
]
\\
&\le
2\Delta_V
\end{aligned}
$$

because:

$$
V_W^{\pi_W^\star}
\ge
V_W^{\pi_R^\star}.
$$

 $\square$

---

# 34. Interpretation

A bounded world-to-reality value error yields a direct policy-transfer regret certificate.

It does not say zero-shot deployment is always safe.

It says policy regret is controlled only inside the theorem's discrepancy assumptions.

---

# 35. Current robust-transfer precedent

Recent work studies:

- constrained Sim2Real policy transfer with adaptive risk;
- robust transfer under uncertainty sets;
- safe domain randomization with OOD detection;
- deployment-time continual adaptation;
- residual policy correction.

These are direct engineering neighbors.

VWDC does not claim robust Sim2Real RL as new.

---

# 36. Pessimism

When model/reality uncertainty is large, a controller can optimize conservative lower bounds rather than nominal simulated values.

This is classical robust/offline RL logic.

VWDC ties the pessimism radius to RTC support and transport debt.

---

# 37. Unsupported-state/action pessimism

For unsupported pairs, a conservative lower bound can be:

- domain-specific safety floor;
- worst-case allowed value;
- $-\infty$ / forbidden.

Choice is a risk-policy decision.

---

# 38. Deployment distribution

An RTC is validated under a context/state-action occupancy distribution:

$$
\boxed{
d_{\mathrm{val}}(z).
}
$$

Deploying policy $\pi$ induces:

$$
\boxed{
d_\pi(z).
}
$$

These need not match.

---

# 39. Local transport loss

Let:

$$
0
\le
\ell(z)
\le
M.
$$

Old validated expected transport loss:

$$
\boxed{
D_{\mathrm{val}}
=
E_{
d_{\mathrm{val}}
}
[
\ell(Z)
].
}
$$

Deployment loss:

$$
D_\pi
=
E_{
d_\pi
}
[
\ell(Z)
].
$$

---

# 40. VWDC06-T8 — Policy-induced occupancy-shift debt

## Theorem VWDC06-T8

$$
\boxed{
|
D_\pi
-
D_{\mathrm{val}}
|
\le
M
\operatorname{TV}
(
d_\pi,
d_{\mathrm{val}}
).
}
$$

Therefore:

$$
\boxed{
D_\pi
\le
D_{\mathrm{val}}
+
M
\operatorname{TV}
(
d_\pi,
d_{\mathrm{val}}
).
}
$$

### Proof

Bounded-function total-variation inequality.

 $\square$

---

# 41. Self-invalidating deployment

A policy optimized in simulation can intentionally visit states rarely or never visited by the validation policy.

Thus deployment can increase:

$$
\operatorname{TV}
(
d_\pi,
d_{\mathrm{val}}
)
$$

and invalidate its own pre-deployment certainty.

This is a form of policy-induced external-validity shift.

---

# 42. RTC deployment tolerance

Let decision policy tolerate transport debt:

$$
\tau.
$$

If:

$$
\boxed{
D_{\mathrm{val}}
+
M
TV(
d_\pi,d_{\mathrm{val}}
)
\le
\tau,
}
$$

the old contract remains sufficient under this conservative shift bound.

---

# 43. VWDC06-T9 — RTC certification loss under occupancy shift

## Theorem VWDC06-T9

If the only available certification is:

$$
D_\pi
\le
D_{\mathrm{val}}
+
M TV(
d_\pi,d_{\mathrm{val}}
),
$$

and the right-hand side exceeds decision tolerance $\tau$, then the existing RTC no longer certifies deployment at tolerance $\tau$.

### Proof

The available upper bound is insufficient to establish:

$$
D_\pi\le\tau.
$$

 $\square$

This is loss of certification, not proof that deployment is actually invalid.

---

# 44. Distinguish invalidity from uncertified status

Use:

```text
VALIDATED
CERTIFIED_FOR_POLICY
UNCERTIFIED_AFTER_SHIFT
INVALIDATED_BY_EVIDENCE
```

A failed certificate does not prove the policy will fail.

---

# 45. Policy-induced support expansion

If:

$$
d_\pi
$$

places mass on unsupported RTC cells, the transport guarantee must account for uncovered mass as in VWDC-05.

---

# 46. Unsupported occupancy debt

Let:

$$
u_\pi
=
P_{d_\pi}
(
Z
\notin
\mathcal Z_{\mathrm{supp}}
).
$$

If transport loss is bounded by $M$:

$$
\boxed{
D_\pi
\le
D_{\mathrm{supported}}
+
u_\pi M.
}
$$

---

# 47. Safe exploration

Before entering an unsupported cell, controller can:

- probe;
- fallback;
- ask human;
- run shadow mode;
- collect external validation.

---

# 48. Shadow deployment

A policy can produce recommendations without controlling the real system.

External observations update RTC without action execution.

This can reduce uncertainty with lower intervention risk.

---

# 49. Intervention probe

A real probe intentionally executes a bounded action to learn local transport behavior.

It can be higher information but higher risk.

---

# 50. Safe probe contract

Probe itself requires:

- permitted action envelope;
- cost/risk bound;
- measurement plan;
- stop condition;
- rollback/fallback.

---

# 51. Human gate

For high-stakes unsupported actions:

$$
\boxed{
\mathrm{HUMAN\_REVIEW}
}
$$

can be a mandatory deployment gate.

This is policy governance, not an assertion that humans are infallible.

---

# 52. Safe fallback override

A safe fallback can override higher simulated value when:

- transport lower bound is weak;
- unsupported mass is high;
- reality drift is detected;
- downstream loss is asymmetric.

---

# 53. Online reality feedback

After deployment/probe, collect:

$$
\boxed{
Y_t^{R}.
}
$$

Update:

- action-value estimates;
- local discrepancy;
- support status;
- RTC version;
- policy.

---

# 54. Local bounded reward calibration

Fix one state/action cell.

Observed reality reward:

$$
R_i
\in
[0,1].
$$

World predicted mean:

$$
\widehat m_W.
$$

Reality empirical mean:

$$
\widehat m_R.
$$

---

# 55. VWDC06-T10 — Online local reward calibration certificate

## Theorem VWDC06-T10

For $n$ independent reality observations in one fixed cell, with true reality mean $m_R$:

$$
\boxed{
P(
|
\widehat m_R-m_R
|
>
\epsilon
)
\le
2e^{-2n\epsilon^2}.
}
$$

With probability at least $1-\delta$:

$$
\boxed{
|
\widehat m_R-m_R
|
\le
\sqrt{
\frac{
\log(2/\delta)
}{
2n
}
}.
}
$$

Thus a transport discrepancy estimate:

$$
|
\widehat m_W-\widehat m_R|
$$

must add both world-prediction and reality-measurement uncertainty before being used as a contract radius.

### Proof

Hoeffding inequality.

 $\square$

---

# 56. Online feedback does not automatically solve structural mismatch

More observations shrink statistical uncertainty in visited cells.

They do not identify unsupported counterfactual/action regions without exploration/assumptions.

---

# 57. Dynamic policy adaptation precedent

Current Sim2Real work adapts deployed policies according to inferred target-environment context or uncertainty.

Safe continual domain adaptation also updates policies after deployment while trying to preserve safety.

VWDC uses RTC-local validity as the governance object around such adaptation.

---

# 58. Policy update versioning

Every deployed policy has:

$$
\boxed{
\pi_v.
}
$$

Every policy update creates:

$$
\pi_{v+1}
$$

with:

- parent policy;
- update data;
- RTC used;
- safety/fallback status.

---

# 59. RTC-policy pair

A deployment certificate applies to:

$$
\boxed{
(
\pi_v,
\mathsf{RTC}_u
).
}
$$

Changing policy can change occupancy.

Changing RTC can change certified actions.

Version both.

---

# 60. Closed-loop feedback

$$
\boxed{
\text{RTC}
\to
\text{Policy}
\to
\text{Reality Occupancy}
\to
\text{External Evidence}
\to
\text{RTC}.
}
$$

The transport layer is reflexive.

---

# 61. Policy deployment can create data

Executed actions create:

- new observations;
- new supported cells;
- possible safety incidents;
- policy-selection bias.

Record the deployment policy.

---

# 62. Deployment-selection bias

Reality data collected under current policy are not a neutral sample from all state/action pairs.

Future calibration should account for visitation policy.

This connects directly to GVSS-10 routing-selection bias.

---

# 63. Off-policy correction

If deployment propensities are known and support holds, causal/off-policy methods may reweight reality observations.

VWDC-06 does not rederive off-policy evaluation.

---

# 64. Unsupported actions remain unsupported

No estimator can recover action outcomes in regions never observed without assumptions.

Online feedback only helps where data enter.

---

# 65. Reality action mask

Maintain:

$$
\boxed{
\mathcal A_{\mathrm{deploy}}(s)
=
\{
a:
RTCStatus(s,a)
\in
\text{allowed statuses}
\}.
}
$$

---

# 66. Status examples

```text
CERTIFIED
SUPPORTED
EXTRAPOLATED
UNSUPPORTED
FORBIDDEN
```

Risk tier determines which statuses are deployable.

---

# 67. Risk-tier policy

Example:

### LOW_STAKES

Allow supported/extrapolated actions within debt threshold.

### HIGH_STAKES

Require certified actions or human gate.

### SAFETY_CRITICAL

Require domain-specific safety certificate beyond RTC alone.

---

# 68. RTC is not a safety proof

A reality transport contract bounds a declared model/measurement discrepancy.

It does not replace:

- physical safety constraints;
- formal verification;
- regulatory requirements;
- operator training.

---

# 69. Safety filter

A runtime may apply a separate certified safety filter:

$$
\boxed{
\mathcal F_{\mathrm{safe}}(s,a).
}
$$

Only actions passing both transport and safety gates execute.

---

# 70. Deployment gate

$$
\boxed{
\mathrm{Execute}(s,a)
\iff
\mathrm{RTC\_Gate}(s,a)
\wedge
\mathrm{Safety\_Gate}(s,a)
\wedge
\mathrm{Authority\_Gate}(s,a).
}
$$

---

# 71. Authority gate

Some actions require:

- human approval;
- legal authorization;
- operational role.

Decision optimality does not imply authority.

---

# 72. Robust deployment action

A robust controller solves:

$$
\boxed{
\max_a
\inf_{
Q_R\in\mathcal U_{\mathrm{RTC}}
}
Q_R(s,a).
}
$$

For independent action intervals, this reduces to maximizing lower bounds.

---

# 73. Coupled uncertainty

If RTC errors across actions are coupled, interval-wise lower-bound optimization can be conservative or incomplete.

Use structured ambiguity set.

VWDC-06 does not solve general robust MDP ambiguity geometry.

---

# 74. Nominal versus robust decision

If VWDC06-T1 holds, nominal and robust decisions coincide.

If intervals overlap, robust and nominal actions can differ.

---

# 75. Value of external probe

An external probe has value when expected reduction in deployment decision risk exceeds:

- probe cost;
- delay;
- intervention risk.

This is VWDC-04 value-of-branch applied to reality-facing decisions.

---

# 76. Value of human review

Same principle:

$$
\boxed{
VoH
=
R_{\mathrm{before}}
-
E[
R_{\mathrm{after}}
]
-
c_H.
}
$$

Human review is not free information.

---

# 77. Probe/fallback region

If risky action could dominate fallback but is not certified, the controller compares:

- probe;
- fallback;
- robust alternative;
- human review.

---

# 78. Perfect probe theorem meaning

VWDC06-T5 says the perfect probe is valuable only when there is meaningful decision ambiguity.

It is not valuable simply because uncertainty exists.

---

# 79. Deployment abstention

STOP/ABSTAIN is a valid action.

A controller can say:

```text
NO ACTION CURRENTLY HAS ACCEPTABLE RTC + SAFETY CERTIFICATE
```

---

# 80. Current foundation-agent reality gap

Recent 2026 work explicitly frames agent deployment as facing noisy inputs, stochastic transitions, execution constraints, and distribution shifts absent from clean benchmark environments.

This broader observation reinforces the need to separate simulation/benchmark optimality from deployment reliability.

---

# 81. Reality gap taxonomy

For deployment:

$$
\boxed{
D_{\mathrm{gap}}
=
(
D_{\mathrm{obs}},
D_{\mathrm{dyn}},
D_{\mathrm{act}},
D_{\mathrm{reward}},
D_{\mathrm{measure}},
D_{\mathrm{support}},
D_{\mathrm{policyshift}}
).
}
$$

Do not collapse all failures to one scalar if diagnosis matters.

---

# 82. Observation gap

Reality sensor process differs from simulated observation model.

---

# 83. Dynamics gap

State transitions differ.

---

# 84. Action gap

Commanded and executed action differ.

---

# 85. Reward/utility gap

Simulator objective differs from actual deployment utility.

---

# 86. Measurement gap

External evaluator/sensor differs from target latent quantity.

---

# 87. Support gap

RTC lacks validated data for state/action region.

---

# 88. Policy-shift gap

Deployment policy induces a new occupancy distribution.

---

# 89. Gap-localized fallback

Fallback can be selected by which gap dominates.

Examples:

- observation gap → human/sensor fallback;
- dynamics gap → robust conservative controller;
- action gap → actuator-safe mode;
- support gap → probe/abstain;
- policy-shift gap → revalidation.

---

# 90. Sim2Real policy adaptation

Current approaches include:

- domain randomization;
- offline domain randomization;
- residual adaptation;
- context inference;
- risk-sensitive dynamic adaptation;
- safe continual adaptation.

VWDC does not prescribe one.

RTC tells the Governor where each adaptation result is externally supported.

---

# 91. Offline domain randomization precedent

Recent provable offline domain randomization uses limited real data to fit distributions over simulator parameters and studies policy transfer guarantees.

This is a direct neighbor to reality-tethered policy transfer.

---

# 92. Real-Sim-Real loop precedent

Current Real-Sim-Real frameworks iteratively refine simulator parameters with real-world data and retrain/adapt policies.

VWDC's loop:

$$
RTC
\to
Policy
\to
Reality
\to
RTC
$$

is a governance-level analogue.

---

# 93. Context-adaptive transfer

Recent work conditions/adapts policies on inferred deployment context rather than relying only on one robust policy.

This corresponds to a state-dependent RTC and local transport debt.

---

# 94. Safe adaptation

A policy can adapt only inside a safe/authority envelope.

Policy performance improvement does not excuse violating hard constraints.

---

# 95. Value transport and safety transport

A world model may accurately transport reward value while poorly transporting safety-event probability.

Maintain separate RTCs:

$$
\boxed{
\mathsf{RTC}_{\mathrm{reward}},
\qquad
\mathsf{RTC}_{\mathrm{safety}}.
}
$$

---

# 96. VWDC06-N2 — Reward transport validity does not imply safety transport validity

## Counterexample

Simulator predicts task reward exactly but omits a rare real-world hazard state.

Reward RTC is accurate on observed reward.

Safety-event model is wrong.

Therefore:

$$
\boxed{
\text{reward transport}
\not\Rightarrow
\text{safety transport}.
}
$$

 $\square$

---

# 97. Multi-contract gate

A deployed action can require:

$$
\boxed{
\bigcap_j
\mathsf{RTC}_{Q_j}
}
$$

for:

- reward;
- safety;
- resource;
- fairness;
- operational constraints.

---

# 98. Contract conflict

Different RTCs can recommend different actions.

Use multiobjective/constrained control.

Do not average incompatible safety constraints into utility silently.

---

# 99. Constrained deployment

Example:

$$
\max_a
LCB_{\mathrm{reward}}(a)
$$

subject to:

$$
\boxed{
UCB_{\mathrm{risk}}(a)
\le
\tau_{\mathrm{risk}}.
}
$$

---

# 100. Unsupported safety action

If safety risk is unsupported, high simulated reward cannot compensate under a hard safety policy.

---

# 101. Policy-transfer acceptance packet

```text
policy_id
world_model_version
rtc_versions
state_action_scope
simulated_value
reality_value_bound
safety_contracts
occupancy_shift_bound
unsupported_mass
fallback_policy
human_gate
expiry
```

---

# 102. Per-decision packet

```text
decision_id
state_context
candidate_actions
world_values
transport_intervals
supported_status
selected_action
selection_mode
probe_or_human_result
rtc_version
safety_gate
authority_gate
```

---

# 103. Deployment modes

```text
CERTIFIED_DEPLOY
ROBUST_DEPLOY
SHADOW
PROBE
SAFE_FALLBACK
HUMAN_REQUIRED
STOPPED
```

---

# 104. CERTIFIED_DEPLOY

Use when transport-margin certificate and all safety/authority gates pass.

---

# 105. ROBUST_DEPLOY

Use when nominal ranking is uncertain but robust lower-bound action meets policy threshold.

---

# 106. SHADOW

Generate action without executing.

Collect reality observations and compare.

---

# 107. PROBE

Execute bounded information-gathering action.

---

# 108. SAFE_FALLBACK

Use predeclared conservative action/controller.

---

# 109. HUMAN_REQUIRED

Escalate when action consequence/risk policy requires human authority or information.

---

# 110. STOPPED

No feasible action satisfies deployment policy.

---

# 111. Policy-shift monitor

Track empirical:

$$
\widehat d_\pi
$$

versus validation occupancy:

$$
d_{\mathrm{val}}.
$$

Trigger RTC review when shift exceeds policy threshold.

---

# 112. Occupancy estimation uncertainty

Empirical TV estimates are themselves uncertain.

The runtime should not treat estimated shift as exact.

VWDC-06 records this as future statistical refinement.

---

# 113. State-action drift map

Instead of one global TV distance, maintain local visitation ratio/coverage.

This helps identify where revalidation is needed.

---

# 114. High-debt region

If policy repeatedly approaches high-debt region, external validation value increases.

VWDC-04 can schedule targeted validation.

---

# 115. Policy deployment as active validation

Carefully bounded deployment can serve both:

- task execution;
- transport data collection.

This is dual control.

No novelty claim.

---

# 116. Data collection must be safe

Exploration for calibration does not justify hazardous actions.

Use domain constraints and human/authority gates.

---

# 117. Safe continual adaptation precedent

Current robotics work studies post-Sim2Real continual domain adaptation while minimizing safety risk and preserving previously learned safe behavior.

This supports separating adaptation from unrestricted online exploration.

---

# 118. Safe policy updates precedent

Current work also studies policy updates that preserve certified safety properties over previously encountered task distributions.

VWDC distinguishes such safety guarantees from RTC external-validity guarantees.

---

# 119. Deployment policy drift

A new policy can visit a new distribution even if environment dynamics do not change.

Thus RTC invalidation can be **endogenous**.

---

# 120. Environment drift

Reality itself can also change.

Need separate:

$$
D_{\mathrm{policyshift}}
$$

and:

$$
D_{\mathrm{envdrift}}.
$$

---

# 121. Closed-loop regime

The complete loop is:

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
\text{New Evidence}
\to
\text{RTC}
\to
\text{World/Policy Update}.
}
$$

---

# 122. Policy update can invalidate world comparison

If policy update changes actions, old world-vs-reality trajectory comparisons may no longer match the new visitation distribution.

Version validation by policy.

---

# 123. Counterfactual policy evaluation

Before deploying a new policy, WDC can simulate it.

But simulation cannot certify unsupported reality regions without transport assumptions.

---

# 124. External off-policy data

Logged real-world data can evaluate candidate policies only under support/causal assumptions.

This is established off-policy/causal inference territory.

---

# 125. No-free-policy-transfer theorem intuition

A world policy can exploit precisely those state/action regions where the world model is wrong.

This is why pessimism/robustness becomes relevant.

VWDC's unsupported-region gate operationalizes the same concern.

---

# 126. Reward hacking analogue

A simulator-trained policy can exploit simulator artifacts to obtain high simulated value with poor reality performance.

RTC debt should increase where such exploitation is plausible/observed.

---

# 127. Model exploitation detector

Compare:

- simulated value gain;
- transport uncertainty;
- external outcomes.

Large simulation gain concentrated in high-debt regions is a warning.

---

# 128. Deployment audit

After policy rollout, report:

- predicted return;
- real observed return;
- transport residuals;
- visited unsupported mass;
- interventions/probes;
- fallbacks;
- human overrides.

---

# 129. Reality regret

Empirical reality regret is usually unknown because the unchosen real optimal action/policy is counterfactual.

Use:

- bounds;
- randomized evaluation;
- experiments;
- structural assumptions.

Do not report actual regret as observed unless identified.

---

# 130. VWDC06-N3 — One realized deployment does not identify counterfactual policy regret

Only the deployed action outcome is observed.

Without counterfactual identification, the value of unchosen actions is not directly observed.

Therefore:

$$
\boxed{
\text{realized outcome}
\not\Rightarrow
\text{identified policy regret}.
}
$$

This is a standard causal/off-policy boundary.

---

# 131. Regret certificate versus empirical regret

VWDC06-T2/T7 provide **model/RTC-based regret bounds**.

They are not direct measurements of realized counterfactual regret.

---

# 132. Policy-safe region

Define:

$$
\boxed{
\mathcal S_{\mathrm{cert}}^\pi
}
$$

as states where every action selected by $\pi$ satisfies the required RTC/safety gates.

---

# 133. Exit condition

If reality enters:

$$
s
\notin
\mathcal S_{\mathrm{cert}}^\pi,
$$

policy automatically transitions to:

- fallback;
- human;
- probe;
- stop.

---

# 134. Fallback invariant

A safe fallback should itself have a maintained RTC/safety certificate.

Fallback is not magically safe because it is called fallback.

---

# 135. Human fallback invariant

Human authority does not eliminate reality uncertainty.

Log human decision and outcome for RTC update.

---

# 136. Deployment contract hierarchy

Suggested:

```text
POLICY_CONTRACT
  -> RTC_REWARD
  -> RTC_SAFETY
  -> SAFETY_FILTER
  -> AUTHORITY_POLICY
  -> FALLBACK_CONTRACT
```

---

# 137. Contract composition

A policy is deployable only if all required subordinate contracts are current.

---

# 138. VWDC06-T11 — Contract-conjunction monotonicity

## Theorem VWDC06-T11

If deployment requires all contracts in set:

$$
\mathcal C
$$

to pass, then adding another mandatory contract cannot enlarge the certified action set.

### Proof

The feasible set is an intersection.

Adding a constraint intersects with another set.

Set intersection cannot enlarge.

 $\square$

---

# 139. Conservative contract expansion

Stricter governance can reduce deployable actions.

It may increase safety/trust but reduce performance/coverage.

---

# 140. Contract debt vector

Define:

$$
\boxed{
\mathbf D(s,a)
=
(
D_{\mathrm{reward}},
D_{\mathrm{safety}},
D_{\mathrm{measurement}},
D_{\mathrm{support}},
D_{\mathrm{occupancy}},
D_{\mathrm{authority}}
).
}
$$

---

# 141. Deployment Pareto frontier

Actions/policies can trade:

- expected reward;
- transport debt;
- safety risk;
- external probing cost;
- human burden.

Nondominated options form deployment frontier.

---

# 142. VWDC06-T12 — Deployment Pareto necessity

## Theorem VWDC06-T12

Every optimum of a scalar deployment objective strictly increasing in declared costs/risks and strictly decreasing in declared benefits lies on the nondominated deployment frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 143. Current literature boundary — Sim2Real transfer

VWDC-06 does not claim as inventions:

- domain randomization;
- robust RL;
- safe RL;
- constrained MDPs;
- sim-to-real policy adaptation;
- residual policy learning;
- context inference;
- offline domain randomization.

---

# 144. Current literature boundary — pessimism

Pessimism under uncertainty/distribution shift is established in offline and robust RL.

VWDC uses RTC-supported lower bounds as the decision-governance interface.

---

# 145. Current literature boundary — safe adaptation

Safe continual adaptation and provably safe policy updates are active current research.

VWDC does not claim these techniques.

It keeps transport validity separate from formal safety guarantees.

---

# 146. Current literature boundary — digital-twin control

Real-Sim-Real and adaptive twin loops already use real feedback to improve simulators/policies.

VWDC formalizes the contract/provenance layer around these loops.

---

# 147. Candidate VWDC-specific synthesis

Subject to broader literature audit, candidate bridge-specific synthesis is:

1. RTC action-value intervals used directly as deployment certificates;
2. transport debt converted into explicit one-step reality-regret bounds;
3. supported versus unsupported action semantics as a deployment gate;
4. probe/fallback/human/stop represented as peer deployment actions;
5. fixed-policy Sim2Real value discrepancy tied to RTC reward/transition gap;
6. policy-induced occupancy shift treated as an endogenous RTC-certification failure mode;
7. versioned RTC-policy pairs with online reality feedback;
8. multi-contract gating separating reward transport, safety transport, safety filters, and authority.

No strong novelty claim is made in v0.1.

---

# 148. What VWDC-06 proves

Under explicit hypotheses, VWDC-06 proves:

1. a simulated action whose lower transported value exceeds all competitors' upper transported values is reality-optimal throughout the RTC ambiguity set;
2. deploying the world-optimal one-step action has real regret bounded by the transport errors of the real and simulated winners;
3. maximizing RTC lower bounds yields the largest available certified action-value floor;
4. a guaranteed fallback dominates the available robust lower-bound certificate when its guarantee is larger;
5. unsupported action value is not identified from supported validation data alone without structural assumptions;
6. a perfect probe in the two-regime risky-action model is worthwhile exactly under the stated threshold;
7. fixed-policy discounted world/reality value difference is bounded by reward and transition mismatch;
8. the world-optimal policy has reality regret at most twice a uniform fixed-policy transport bound;
9. policy-induced occupancy shift changes expected transport loss by at most a TV-distance term;
10. an RTC loses certification at a decision tolerance when its only available deployment-shift upper bound exceeds that tolerance;
11. local reality reward means admit Hoeffding calibration intervals under i.i.d. bounded observations;
12. reward transport validity does not imply safety transport validity;
13. one realized deployment does not identify counterfactual policy regret;
14. adding mandatory deployment contracts cannot enlarge the certified action set;
15. every strictly monotone scalar deployment optimum lies on the nondominated deployment frontier.

---

# 149. What VWDC-06 does not prove

It does not prove:

- RTC intervals are always calibrated;
- unsupported actions are always unsafe;
- pessimistic deployment maximizes expected reward;
- a generic safety fallback is absolutely safe;
- reward and transition TV errors are easy to estimate;
- fixed-policy MDP bounds remain tight for long horizons;
- policy occupancy TV can be estimated without uncertainty;
- online adaptation remains safe without separate safety guarantees;
- deployment data are unconfounded;
- human review is infallible;
- an RTC replaces regulation or formal safety verification.

---

# 150. Proposed VWDC-07

The next paper should close the loop around **deployment-triggered learning and governance**:

$$
\boxed{
\textbf{
VWDC-07 — Closed-Loop Reality Feedback, Safe Policy Adaptation, and Transport-Aware Continual Worlds
}
}
$$

Chinese:

**閉環現實回饋、安全策略適應與轉移感知持續世界**

Main questions:

1. How should deployed observations update the world model and RTC jointly?
2. How should policy updates preserve old certified safety/transport regions?
3. When should feedback create a new world/reality regime version?
4. How should old RTCs be retained/superseded?
5. How should continual adaptation avoid self-confirming deployment bias?
6. When should the runtime roll back a policy/world update?
7. How should real incidents propagate through model, RTC, and branch evidence?
8. Can a stability criterion be defined for the full World→RTC→Policy→Reality loop?

---

# 151. References

1. Gengyue Han, Yiheng Feng, **Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment**, arXiv:2605.27659, 2026.
2. Lu Shi et al., **An Real-Sim-Real (RSR) Loop Framework for Generalizable Robotic Policy Transfer with Differentiable Simulation**, arXiv:2503.10118, 2025.
3. Mohamad H. Danesh et al., **Safe Domain Randomization via Uncertainty-Aware Out-of-Distribution Detection and Policy Adaptation**, arXiv:2507.06111, 2025.
4. Josip Josifovski et al., **Safe Continual Domain Adaptation after Sim2Real Transfer of Reinforcement Learning Policies in Robotics**, arXiv:2503.10949, 2025.
5. Maksim Anisimov, Francesco Belardinelli, Matthew Wicker, **SafeAdapt: Provably Safe Policy Updates in Deep Reinforcement Learning**, arXiv:2604.09452, 2026.
6. Zeyuan Tang et al., **Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning More Powerful**, arXiv:2504.16680, revised 2026.
7. **Provable Sim-to-Real Transfer via Offline Domain Randomization**, arXiv:2506.10133, 2025.
8. **The Sim-to-Real Gap of Foundation Model Agents**, arXiv:2606.07017, 2026.
9. **Can Context Bridge the Reality Gap? Sim-to-Real Transfer through Dynamics-Grounded Context Adaptation**, arXiv:2511.04249, revised 2026.
10. VWDC-01–05, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, and frozen RRT-20, internal series artifacts, 2026.

---

# 152. Conclusion

VWDC-05 creates a reality transport contract.

VWDC-06 makes deployment obey it.

The central one-step certificate is:

$$
\boxed{
\widehat Q_W(s,\widehat a)-\delta_{\widehat a}
>
\max_{b\neq\widehat a}
[
\widehat Q_W(s,b)+\delta_b
].
}
$$

When it holds, the simulation choice survives every reality value allowed by the RTC.

When it does not, transport debt becomes a real decision ambiguity.

Even then the simulated optimum has a reality-regret bound:

$$
\boxed{
\operatorname{Regret}_R
\le
\delta_{a_R^\star}
+
\delta_{\widehat a}.
}
$$

Unsupported actions have no distribution-free reality guarantee.

A probe can be worth more than immediate deployment or fallback near the decision boundary.

Long-horizon policy transfer amplifies reward/dynamics mismatch.

And deployment can invalidate its own RTC by changing the state-action occupancy distribution:

$$
\boxed{
D_\pi
\le
D_{\mathrm{val}}
+
M
TV(
d_\pi,
d_{\mathrm{val}}
).
}
$$

Therefore policy deployment is not the end of validation.

It changes the reality data distribution and feeds new evidence back into the world and transport layers.

The canonical VWDC-06 principle is:

$$
\boxed{
\textbf{
Do not deploy the action that is best in the simulated world.
Deploy the action whose advantage survives the quantified world-to-reality gap,
whose state-action region is supported,
and whose safety and authority contracts remain valid after the policy changes what reality is visited.
}
}
$$

This establishes transport-aware decision and policy control for reality-facing WDC systems.

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
