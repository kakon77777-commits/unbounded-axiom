# VWDC-05 — Reality-Tethered World Calibration, Transport Contracts, and External Validity
## 現實繫結世界校準、轉移契約與外部有效性：條件驗證、模型差異、版本漂移與反事實假設邊界

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 05  
**Depends on:** VWDC-01–04, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal transport-calibration paper. Contract localization, marginal-cancellation no-go, conditional-discrepancy aggregation, partial-coverage transport bounds, counterfactual joint non-identifiability, parameter–discrepancy confounding, inverse-variance external evidence fusion, common-bias fusion no-go, distribution-shift transport bounds, version-drift invalidation, calibration/transport error composition, and claim-scope monotonicity are proved under explicit hypotheses. Causal transportability, digital-twin calibration, model discrepancy analysis, subtrace-conditional validation, and counterfactual validation are established neighboring research and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** digital twin calibration, transportability, external validity, model discrepancy, conditional validation, counterfactual validation, sim-to-real, reality gap, transport contract, world model, WDC

---

# Abstract

VWDC-03 and VWDC-04 separated two error classes for a world-derived reality claim:

$$
\boxed{
D
=
L_T\varepsilon_W
+
\delta_{\mathrm{trans}},
}
$$

where:

- $\varepsilon_W$ is world-internal estimation/simulation uncertainty;
- $\delta_{\mathrm{trans}}$ is world-to-reality transport discrepancy.

VWDC-04 proved that internal branching can drive:

$$
\varepsilon_W
\to
0
$$

while leaving:

$$
\delta_{\mathrm{trans}}
$$

unchanged.

Therefore simulation precision alone cannot certify external validity.

VWDC-05 makes the transport layer itself a first-class, calibrated, versioned object.

The central object is a **Reality Transport Contract**:

$$
\boxed{
\mathsf{RTC}
=
(
Q,
\mathcal Z,
\nu_W,
\nu_R,
T,
\mathcal V,
\mathcal A,
\Delta,
\mathcal D_{\mathrm{ext}},
\mathsf{Expiry},
\mathsf{Prov}
),
}
$$

where:

- $Q$ is the exact world/reality target quantity or estimand;
- $\mathcal Z$ is the state/action/task validity region;
- $\nu_W$ is the world-model/runtime version;
- $\nu_R$ is the reality-regime/measurement version;
- $T$ is the world-to-reality transport map;
- $\mathcal V$ is validation level/protocol;
- $\mathcal A$ is the explicit assumption set;
- $\Delta$ is the residual transport-discrepancy bound or uncertainty object;
- $\mathcal D_{\mathrm{ext}}$ is external validation evidence;
- $\mathsf{Expiry}$ specifies drift/revalidation conditions;
- $\mathsf{Prov}$ is provenance.

The contract does **not** say:

> this digital twin is valid.

It says:

> this particular world-derived quantity may be transported to this particular reality target, over this declared region, under these assumptions, with this residual discrepancy and this version scope.

That distinction is the foundation of VWDC-05.

---

# 1. Target-quantity relativity

A world model can be accurate for one quantity and inaccurate for another.

Let:

$$
q_W
=
h_W(W)
$$

be a world-derived quantity.

Let:

$$
q_R
=
h_R(R)
$$

be the corresponding reality quantity.

A transport map is:

$$
\boxed{
T_Q:
\mathcal Q_W
\to
\mathcal Q_R.
}
$$

The subscript $Q$ is essential.

There is no requirement that one transport map validates all world outputs.

---

# 2. Reality Transport Contract

## Definition VWDC05-D1

A transport contract is:

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

The contract is valid only inside all declared scopes.

---

# 3. Scope dimensions

At minimum record:

```text
claim_or_estimand
world_model_version
world_runtime_version
reality_regime
measurement_process
state_region
action_region
task_region
validation_level
assumption_set
residual_discrepancy
validation_data
expiry_condition
```

---

# 4. Global-twin validity no-go

## VWDC05-N1 — No scalar twin-validity score determines all transport claims

### Counterexample

A simulator exactly predicts position:

$$
q_1
$$

but systematically mispredicts temperature:

$$
q_2.
$$

A single scalar "twin accuracy" cannot imply both quantity-specific transport guarantees.

Therefore:

$$
\boxed{
\text{global twin score}
\not\Rightarrow
\text{claim-specific external validity}.
}
$$

Transport validity is quantity and region relative.

---

# 5. Validation region

Let:

$$
z
\in
\mathcal Z
$$

denote a task/state/action context.

Let world and reality conditional target means be:

$$
m_W(z),
$$

$$
m_R(z).
$$

Define local transport discrepancy:

$$
\boxed{
\delta(z)
=
|
T(m_W(z))
-
m_R(z)
|.
}
$$

---

# 6. Marginal discrepancy

Under reality target distribution:

$$
P_Z,
$$

marginal means are:

$$
\bar m_W
=
E_Z[m_W(Z)],
$$

$$
\bar m_R
=
E_Z[m_R(Z)].
$$

---

# 7. VWDC05-N2 — Marginal validation can hide conditional transport failure

## Counterexample

Let:

$$
P(Z=0)=P(Z=1)=1/2.
$$

Reality:

$$
m_R(0)=0.2,
\qquad
m_R(1)=0.8.
$$

World:

$$
m_W(0)=0.6,
\qquad
m_W(1)=0.4.
$$

Then:

$$
\boxed{
\bar m_R
=
\bar m_W
=
0.5.
}
$$

Marginal mean error is zero.

But conditional errors are:

$$
\boxed{
|m_W(0)-m_R(0)|=0.4,
}
$$

$$
\boxed{
|m_W(1)-m_R(1)|=0.4.
}
$$

Thus:

$$
\boxed{
\text{marginal agreement}
\not\Rightarrow
\text{conditional/subtrace agreement}.
}
$$

 $\square$

This is the core reason to validate local/conditional behavior rather than only aggregate outputs.

---

# 8. Conditional validation precedent

Current subtrace-conditional validation research repeatedly initializes simulations from observed system states, fixes selected stochastic primitives to observed realizations, and validates conditional output distributions.

It is explicitly designed to detect misspecified input models that can be invisible under marginal-output validation.

VWDC adopts this as a direct validation precedent.

---

# 9. Conditional discrepancy aggregation

Suppose a finite partition:

$$
\mathcal Z
=
\{1,\ldots,K\}.
$$

Reality target weights:

$$
w_k
\ge
0,
\qquad
\sum_kw_k=1.
$$

Local signed discrepancies:

$$
d_k
=
T(m_{W,k})-m_{R,k}.
$$

---

# 10. VWDC05-T1 — Aggregate transport discrepancy bound

## Theorem VWDC05-T1

$$
\boxed{
\left|
\sum_kw_kd_k
\right|
\le
\sum_kw_k|d_k|
\le
\max_k|d_k|.
}
$$

### Proof

Triangle inequality and convexity of the weighted average.

 $\square$

---

# 11. Interpretation

Marginal error can cancel.

A local maximum bound cannot.

Therefore transport validation should report at least:

- signed marginal discrepancy;
- weighted absolute discrepancy;
- worst validated local discrepancy.

---

# 12. Local transport debt

Define:

$$
\boxed{
D_{\mathrm{local}}
=
\{
\delta(z):
z\in\mathcal Z
\}.
}
$$

Do not collapse this object too early.

---

# 13. Partial validation coverage

Let:

$$
C
\subseteq
\mathcal Z
$$

be validated cells.

Let reality target probability mass outside covered cells be:

$$
\boxed{
u
=
P_Z(
Z\notin C
).
}
$$

Assume target discrepancy/loss is bounded in:

$$
[0,M].
$$

---

# 14. VWDC05-T2 — Partial-coverage transport bound

## Theorem VWDC05-T2

If for each covered cell:

$$
z\in C,
$$

transport discrepancy is bounded by:

$$
\delta_z,
$$

then total expected discrepancy satisfies:

$$
\boxed{
E[\delta(Z)]
\le
\sum_{z\in C}
P(Z=z)\delta_z
+
uM.
}
$$

### Proof

Split expectation over covered and uncovered regions.

Use known cell bounds on $C$ and the global boundedness $M$ outside $C$.

 $\square$

---

# 15. Coverage debt

Define:

$$
\boxed{
D_{\mathrm{coverage}}
=
uM.
}
$$

A highly accurate contract over a tiny region can still have large target-domain debt.

---

# 16. Validation coverage map

Recommended:

```text
region_id
state_scope
action_scope
task_scope
target_mass
sample_count
local_discrepancy
confidence
validation_level
support_status
```

---

# 17. Validation levels

VWDC proposes the following engineering ladder.

```text
V0 INTERNAL_ONLY
V1 MARGINAL_EXTERNAL
V2 CONDITIONAL_SUBTRACE
V3 INTERVENTIONAL
V4 STRUCTURAL_COUNTERFACTUAL
```

These are VWDC labels, not a claim to replace existing validation taxonomies.

---

# 18. V0 — Internal only

Checks:

- code;
- transition invariants;
- replay;
- internal consistency.

No external validity claim.

---

# 19. V1 — Marginal external

Checks:

$$
P_W(Y)
\approx
P_R(Y)
$$

or selected marginal moments/distributions.

Useful but can hide conditional mismatch.

---

# 20. V2 — Conditional/subtrace

Checks:

$$
P_W(
Y_{t:t+h}
\mid
X_t=x,
C
)
$$

against observed conditional behavior.

This can localize discrepancy.

---

# 21. V3 — Interventional

Checks world predictions against observed effects of real interventions/actions in matching scope.

Stronger for intervention claims.

---

# 22. V4 — Structural/counterfactual

Claims about unobserved joint potential outcomes, latent couplings, or structural mechanisms.

Some components can remain assumption indexed even after strong marginal/interventional validation.

---

# 23. Counterfactual estimands

Let binary potential outcomes:

$$
Y(0),Y(1)
\in
\{0,1\}.
$$

Suppose both marginals are known exactly:

$$
P(Y(0)=1)=1/2,
$$

$$
P(Y(1)=1)=1/2.
$$

---

# 24. VWDC05-N3 — Correct potential-outcome marginals do not identify individual benefit probability

## Counterexample

### World A — perfectly coupled

$$
Y(1)=Y(0).
$$

Then:

$$
P(Y(1)>Y(0))=0.
$$

Both marginals are Bernoulli $(1/2)$.

### World B — opposite coupling

$$
Y(1)=1-Y(0).
$$

Then:

$$
\boxed{
P(Y(1)>Y(0))=1/2.
}
$$

Again both marginals are Bernoulli $(1/2)$.

Therefore the two potential-outcome marginals do not identify:

$$
\boxed{
P(Y(1)>Y(0)).
}
$$

 $\square$

---

# 25. Counterfactual assumption label

Joint/counterfactual claims should record:

```text
MARGINAL_IDENTIFIED
JOINT_ASSUMPTION_INDEXED
STRUCTURAL_ASSUMPTION_INDEXED
SENSITIVITY_BOUNDED
```

Do not report an assumption-indexed quantity as empirically identified.

---

# 26. DTCF relation

Current Digital Twin Counterfactual Framework work distinguishes marginally testable causal quantities from copula/joint-dependent counterfactual quantities whose identification still relies on unobservable within-unit dependence assumptions.

VWDC uses the same boundary.

---

# 27. Model calibration

A simulator often has calibration parameters:

$$
\theta
$$

and model discrepancy:

$$
\delta.
$$

Observed reality data can be represented schematically as:

$$
\boxed{
Y_R
=
f_W(
\theta
)
+
\delta
+
\varepsilon.
}
$$

---

# 28. VWDC05-N4 — Parameter–discrepancy confounding

## Counterexample

Let:

$$
f_W(\theta)=\theta
$$

and noiseless observation:

$$
Y_R=1.
$$

Then every pair:

$$
\boxed{
(\theta,\delta)
=
(t,1-t)
}
$$

for any real $t$ fits the observation exactly.

Therefore:

$$
\boxed{
\text{field fit}
\not\Rightarrow
\text{unique calibration parameter identification}
}
$$

without further constraints.

 $\square$

This is a minimal instance of calibration/discrepancy confounding.

---

# 29. Current online calibration precedent

Recent 2026 Bayesian digital-twin calibration work explicitly addresses model discrepancy, parameter–discrepancy confounding, gradual drift, and abrupt regime changes.

It reinforces the need to version and continuously revalidate calibration contracts.

---

# 30. Calibration target

VWDC requires calibration objective to state whether it targets:

- predictive accuracy;
- physical parameter interpretation;
- intervention response;
- transport bound;
- latent-state inference.

A parameter value calibrated for prediction need not be physically identifiable.

---

# 31. External validation dataset

Let external datasets be:

$$
\boxed{
\mathcal D_1,\ldots,\mathcal D_J.
}
$$

Each has:

- measurement process;
- target region;
- time;
- bias assumptions;
- variance;
- provenance.

---

# 32. Independent unbiased scalar estimators

Suppose dataset $j$ yields:

$$
\widehat\delta_j
$$

with:

$$
E[
\widehat\delta_j
]
=
\delta
$$

and variance:

$$
v_j>0.
$$

Assume estimators are independent.

---

# 33. VWDC05-T3 — Minimum-variance linear external-evidence fusion

## Theorem VWDC05-T3

Among unbiased linear estimators:

$$
\widehat\delta
=
\sum_jw_j\widehat\delta_j,
\qquad
\sum_jw_j=1,
$$

the minimum-variance weights are:

$$
\boxed{
w_j
=
\frac{
v_j^{-1}
}{
\sum_kv_k^{-1}
}.
}
$$

The fused variance is:

$$
\boxed{
\operatorname{Var}(
\widehat\delta
)
=
\frac{
1
}{
\sum_jv_j^{-1}
}.
}
$$

### Proof

Lagrange multiplier minimization of:

$$
\sum_jw_j^2v_j
$$

subject to:

$$
\sum_jw_j=1.
$$

 $\square$

This is classical inverse-variance weighting.

---

# 34. Shared external bias

Suppose:

$$
\widehat\delta_j
=
\delta
+
B
+
\varepsilon_j,
$$

with common bias:

$$
B.
$$

Then averaging many datasets reduces:

$$
\varepsilon_j
$$

but not $B$.

---

# 35. VWDC05-N5 — Many external datasets do not remove shared measurement bias

If:

$$
E[B]\neq0,
$$

then even as:

$$
J\to\infty,
$$

the fused estimator remains biased by:

$$
B.
$$

Therefore:

$$
\boxed{
\text{external dataset count}
\not\Rightarrow
\text{external evidence independence}.
}
$$

 $\square$

The same dependence logic used for world branches applies to external measurements.

---

# 36. External evidence independence profile

Track:

- measurement device family;
- institution/source;
- preprocessing;
- calibration standard;
- time period;
- target population;
- evaluator/labeler;
- shared pipeline.

---

# 37. Reality regime

Let:

$$
\boxed{
\nu_R
}
$$

identify the target reality regime.

Examples:

- operating season;
- hardware configuration;
- patient population;
- policy environment;
- sensor calibration state.

Transport validity is regime relative.

---

# 38. Distribution drift

Let old validation context distribution be:

$$
P
$$

and current target distribution:

$$
Q.
$$

Let discrepancy function:

$$
0\le
\ell(z)
\le
M.
$$

---

# 39. VWDC05-T4 — Distribution-shift transport bound

## Theorem VWDC05-T4

Using total variation convention:

$$
\operatorname{TV}(P,Q)
=
\sup_A
|P(A)-Q(A)|,
$$

for:

$$
0\le\ell\le M,
$$

$$
\boxed{
|
E_Q[\ell]
-
E_P[\ell]
|
\le
M\operatorname{TV}(P,Q).
}
$$

### Proof

Standard bounded-function total-variation inequality.

 $\square$

---

# 40. Drift-adjusted discrepancy

If old validated expected discrepancy is:

$$
D_P,
$$

then current expected discrepancy obeys:

$$
\boxed{
D_Q
\le
D_P
+
M\operatorname{TV}(P,Q).
}
$$

provided the discrepancy function itself remains unchanged.

---

# 41. Structural drift caveat

If the conditional discrepancy mechanism also changes:

$$
\ell_P(z)
\neq
\ell_Q(z),
$$

covariate-distribution TV alone is insufficient.

Require model/regime drift testing.

---

# 42. World-model version drift

A new world-model version:

$$
\nu_W
\to
\nu_W'
$$

can change:

- predictions;
- latent representation;
- action semantics;
- calibration parameters;
- discrepancy pattern.

An old transport contract is not automatically inherited.

---

# 43. Reality-regime drift

Likewise:

$$
\nu_R
\to
\nu_R'
$$

can invalidate transport without any world-model update.

---

# 44. VWDC05-N6 — Validation of one version does not validate another version without an invariance argument

## Counterexample

Old model:

$$
M_0
$$

matches reality exactly on validation region.

New model:

$$
M_1
$$

returns the negated prediction.

The old validation data contain no evidence that:

$$
M_1
$$

is valid.

Therefore:

$$
\boxed{
\text{old-version validation}
\not\Rightarrow
\text{new-version transport validity}.
}
$$

 $\square$

---

# 45. Contract status

Recommended:

```text
VALID
CONDITIONALLY_VALID
STALE
REVALIDATION_REQUIRED
INVALID
SUPERSEDED
```

---

# 46. Expiry triggers

A transport contract should expire or enter review when:

- world-model version changes;
- evaluator changes;
- measurement process changes;
- target distribution drifts beyond threshold;
- reality regime changes;
- validation age exceeds policy;
- anomaly/drift test rejects stationarity.

---

# 47. Continual validation precedent

Current adaptive digital-twin work explicitly combines drift detection, model updating, and statistical validation to decide when and whether a digital twin update improves predictive performance.

This is direct precedent for contract expiry/revalidation.

---

# 48. World estimate and transport

Let:

$$
\widehat q_W
$$

estimate world target:

$$
q_W.
$$

Assume:

$$
d_W(
\widehat q_W,
q_W
)
\le
\varepsilon_W.
$$

Let transport map be:

$$
L_T
$$

-Lipschitz.

Transport discrepancy:

$$
d_R(
T(q_W),
q_R
)
\le
\delta_T.
$$

---

# 49. External measurement/calibration error

Suppose reality target estimate:

$$
\widehat q_R
$$

satisfies:

$$
d_R(
\widehat q_R,
q_R
)
\le
\varepsilon_R.
$$

---

# 50. VWDC05-T5 — Three-part calibrated claim bound

## Theorem VWDC05-T5

$$
\boxed{
d_R(
T(\widehat q_W),
\widehat q_R
)
\le
L_T\varepsilon_W
+
\delta_T
+
\varepsilon_R.
}
$$

### Proof

Insert:

$$
T(q_W)
$$

and:

$$
q_R
$$

and apply triangle inequality plus Lipschitzness.

 $\square$

---

# 51. Three error classes

The bound separates:

$$
\boxed{
D_{\mathrm{world}}
=
L_T\varepsilon_W,
}
$$

$$
\boxed{
D_{\mathrm{transport}}
=
\delta_T,
}
$$

$$
\boxed{
D_{\mathrm{measurement}}
=
\varepsilon_R.
}
$$

More simulation primarily attacks the first.

Better transport calibration attacks the second.

Better external measurement attacks the third.

---

# 52. Measurement precision no-go

Perfect external sensor precision:

$$
\varepsilon_R\to0
$$

does not remove transport/model discrepancy.

Likewise perfect simulation precision does not remove external measurement bias.

---

# 53. Regional transport map

A practical contract can be:

$$
\boxed{
T(
q_W,
z
).
}
$$

Different state/action/task regions can require different corrections.

---

# 54. Local discrepancy map

Store:

$$
\boxed{
\Delta(z)
=
(
\widehat\delta(z),
CI(z),
N(z),
ValidationLevel(z)
).
}
$$

This is the transport analogue of GVSS provider capability maps.

---

# 55. Local unsupported region

If no external validation exists in region:

$$
z^\star,
$$

status is:

```text
UNSUPPORTED
```

unless an explicit transfer assumption links it to validated regions.

---

# 56. VWDC05-N7 — Unsupported region transport is not empirically identified by neighboring validation alone

Without smoothness/invariance assumptions, two reality systems can agree on all validated regions and differ arbitrarily on an unvalidated region.

Therefore:

$$
\boxed{
\text{neighboring validation}
\not\Rightarrow
\text{unvalidated-region identification}.
}
$$

 $\square$

---

# 57. Spatial/task smoothness

A model can extrapolate transport discrepancy across nearby regions if assuming:

$$
|\delta(z)-\delta(z')|
\le
L_zd(z,z').
$$

This assumption must be recorded and validated where possible.

---

# 58. VWDC05-T6 — Lipschitz regional extrapolation bound

## Theorem VWDC05-T6

If:

$$
\delta
$$

is $L_z$ -Lipschitz over context metric $d_Z$, and region $z$ has nearest validated point $z_v$, then:

$$
\boxed{
\delta(z)
\le
\delta(z_v)
+
L_zd_Z(z,z_v).
}
$$

### Proof

Lipschitz inequality.

 $\square$

This converts geometric coverage gaps into explicit extrapolation debt.

---

# 59. Validation density

Define:

$$
\boxed{
r(z)
=
\min_{
z_v\in\mathcal Z_{\mathrm{validated}}
}
d_Z(z,z_v).
}
$$

Then extrapolation debt grows with:

$$
L_zr(z).
$$

---

# 60. Validation design

VWDC-04 can now choose external validation actions where:

$$
\boxed{
\text{target mass}
\times
\text{transport uncertainty}
\times
\text{decision importance}
}
$$

is high.

---

# 61. Subtrace validation localization

Observed checkpoints/subtraces can define regions:

$$
z=(x_t,\text{input subset},h).
$$

Conditional tests update only the contract cells they actually validate.

Do not globally upgrade the twin because one subtrace passed.

---

# 62. Marginal test pass

A passed V1 test can update:

```text
MARGINAL_VALIDATED
```

not:

```text
STRUCTURALLY_VALIDATED
```

---

# 63. Conditional test pass

A passed V2 test can reduce local discrepancy in its conditional scope.

It does not identify unobserved joint potential-outcome couplings.

---

# 64. Interventional test pass

A real intervention can validate:

$$
P_R(Y\mid do(a),z)
$$

against world predictions over matched scope.

Still do not extrapolate to unmatched actions/states without transport assumptions.

---

# 65. Structural claim

A structural model asserts invariances/mechanisms beyond directly observed distributions.

These assumptions can support transport.

They should remain explicit.

---

# 66. Classical causal transportability boundary

Causal transportability theory uses structured knowledge about differences between source and target populations/environments to decide whether causal effects can be transported and what data are required.

VWDC does not claim causal transportability as new.

The Reality Transport Contract is a runtime engineering wrapper around claim-specific transport assumptions, validation, discrepancy, and versioning.

---

# 67. Selection diagram relation

A future implementation can attach a causal/selection diagram to:

$$
\mathsf{RTC}.
$$

This can encode which mechanisms differ between world and reality target.

VWDC-05 does not develop do-calculus.

---

# 68. Transport contract acceptance

A claim transport is accepted only if:

1. target quantity is named;
2. source/target semantics align;
3. state/action/task region is supported;
4. validation level meets policy;
5. residual discrepancy is below claim tolerance;
6. structural assumptions are accepted;
7. versions are current;
8. provenance is complete.

---

# 69. Claim tolerance

Let downstream decision tolerate error:

$$
\boxed{
\tau_Q.
}
$$

Transport is decision-admissible when:

$$
\boxed{
D_Q
\le
\tau_Q.
}
$$

This does not mean the model is "true."

It means residual debt is within declared decision tolerance.

---

# 70. VWDC05-T7 — Claim-scope restriction cannot increase worst-case validated discrepancy

## Theorem VWDC05-T7

Let:

$$
A\subseteq B
$$

be two validity regions.

Define:

$$
D_{\max}(S)
=
\sup_{
z\in S
}
\delta(z).
$$

Then:

$$
\boxed{
D_{\max}(A)
\le
D_{\max}(B).
}
$$

### Proof

Supremum over a subset cannot exceed supremum over the full set.

 $\square$

Narrower claim scope can support a stronger guarantee.

---

# 71. Scope expansion debt

Expanding a contract to more:

- states;
- actions;
- populations;
- time regimes;

requires new evidence or stronger assumptions.

---

# 72. Generalization label

Recommended:

```text
DIRECTLY_VALIDATED
INTERPOLATED
EXTRAPOLATED
STRUCTURALLY_TRANSPORTED
UNSUPPORTED
```

---

# 73. Contract inheritance

A child contract can inherit validated information from a parent only if:

- same quantity semantics;
- compatible versions;
- subset region;
- no weaker validation requirement;
- discrepancy bound remains valid.

---

# 74. VWDC05-T8 — Safe subset inheritance

## Theorem VWDC05-T8

If contract $C_B$ is valid on region $B$ with uniform discrepancy:

$$
\delta(z)\le D
\quad
\forall z\in B,
$$

then for any:

$$
A\subseteq B,
$$

the same discrepancy bound $D$ remains valid on $A$.

### Proof

Immediate set restriction.

 $\square$

---

# 75. Superset inheritance no-go

Validation on:

$$
A
$$

does not establish the same bound on:

$$
B\supset A.
$$

This is the external-validity analogue of unsupported routing regions in GVSS-10.

---

# 76. Calibration artifact

Define:

$$
\boxed{
\mathsf{Cal}_Q
=
(
\theta,
\delta(\cdot),
\mathcal D_{\mathrm{ext}},
\mathcal V,
\nu_W,
\nu_R,
\mathsf{Fit},
\mathsf{Uncertainty},
\mathsf{Prov}
).
}
$$

---

# 77. Contract artifact

Define:

$$
\boxed{
\mathsf{RTC}_Q
=
(
\mathsf{Cal}_Q,
T_Q,
\mathcal Z_Q,
\mathcal A_Q,
D_Q,
\tau_Q,
\mathsf{Expiry}
).
}
$$

---

# 78. Contract fingerprint

Hash:

- world model;
- world runtime;
- external datasets;
- measurement process;
- target quantity;
- state/action/task region;
- validation protocol;
- assumption set;
- discrepancy model.

---

# 79. Contract versioning

Never overwrite:

$$
\mathsf{RTC}_{v}.
$$

Create:

$$
\mathsf{RTC}_{v+1}
$$

and retain parent/supersession relation.

---

# 80. Contract expiry

Possible rules:

```text
ON_WORLD_MODEL_CHANGE
ON_REALITY_REGIME_CHANGE
ON_MEASUREMENT_CHANGE
ON_DRIFT_TEST
AFTER_TIME_WINDOW
ON_VALIDATION_FAILURE
```

---

# 81. Online calibration

Streaming external data can update:

$$
\theta_t,
\delta_t,
\Delta_t.
$$

The contract remains valid only if update/validation policy passes.

---

# 82. Gradual drift

Use forgetting/windowing/state-space discrepancy models if stationarity fails gradually.

---

# 83. Abrupt drift

A changepoint/reset policy may create a new reality regime:

$$
\nu_R'.
$$

Do not force new data into the old contract.

---

# 84. Continual calibration boundary

Online Bayesian calibration under gradual/abrupt drift is established current research.

VWDC uses the output as versioned calibration evidence.

---

# 85. Calibration does not equal validation

Fitting the twin to observed data uses data to reduce discrepancy.

Validation should reserve independent or appropriately corrected evidence where possible.

Otherwise calibration and validation can become circular.

---

# 86. VWDC05-N8 — Perfect in-sample calibration does not prove out-of-sample transport

## Counterexample

Fit arbitrary interpolator to finite validation points with zero residual error.

Choose a target point outside those points where the interpolator differs arbitrarily from reality.

Therefore:

$$
\boxed{
\text{zero calibration residual}
\not\Rightarrow
\text{external validity outside calibrated support}.
}
$$

 $\square$

---

# 87. Holdout / prospective evidence

When possible, use:

- holdout external data;
- future temporal data;
- independent sensors/sites;
- interventions;

to challenge the transport contract.

---

# 88. Reality Gap Analysis relation

Recent digital-twin reality-gap work explicitly treats continuous integration of new sensor data, context mismatch detection, and recalibration across a twin lifecycle.

VWDC places such modules inside the transport contract lifecycle.

---

# 89. Simulation-based inference correction relation

Recent work on simulation-based inference under model misspecification uses scarce calibration observations to transport/correct simulation-trained posterior estimates toward reality-supported posteriors.

This is another current example of explicit sim-to-real correction rather than assuming synthetic and real distributions match.

---

# 90. Model discrepancy map

Possible representation:

$$
\boxed{
\delta_t(z)
=
g_\psi(
z,t
)
+
\epsilon.
}
$$

The model form can be:

- Gaussian process;
- neural residual;
- basis expansion;
- piecewise constant cells;
- robust interval.

VWDC does not prescribe one.

---

# 91. Identifiability profile

Each calibrated parameter/claim should record:

```text
DIRECTLY_IDENTIFIED
IDENTIFIED_UP_TO_EQUIVALENCE
PRIOR_REGULARIZED
DISCREPANCY_CONFOUNDED
ASSUMPTION_INDEXED
```

---

# 92. Parameter meaning versus prediction

A calibration can improve prediction while making latent parameter interpretation unreliable.

Separate:

$$
\boxed{
\text{predictive calibration}
}
$$

from:

$$
\boxed{
\text{parameter identification}.
}
$$

---

# 93. Multiple fidelity sources

External evidence can include:

- real measurement;
- hardware-in-loop;
- high-fidelity simulator;
- low-fidelity simulator;
- expert annotation.

Their evidential status is not identical.

---

# 94. Evidence fidelity label

```text
REAL_MEASUREMENT
HARDWARE_IN_LOOP
HIGH_FIDELITY_SIM
LOW_FIDELITY_SIM
EXPERT_LABEL
DERIVED
```

---

# 95. High-fidelity simulation is not reality

Even a more expensive simulator remains a model unless directly tethered to external measurement.

---

# 96. Measurement model

Reality observation itself may be:

$$
\boxed{
Y_{\mathrm{obs}}
=
H_R(
X_R
)
+
\epsilon_R.
}
$$

Transport validation therefore compares two modeled observation processes, not omniscient reality state.

---

# 97. Sensor calibration

Measurement uncertainty belongs in:

$$
\varepsilon_R.
$$

A bad sensor can make a good twin look wrong or a bad twin look correct.

---

# 98. Measurement-process version

If sensor calibration/process changes:

$$
\nu_M
\to
\nu_M',
$$

the transport contract requires review.

---

# 99. External-label evaluator

Human/expert labels are measurement processes with:

- disagreement;
- bias;
- protocol;
- version.

Do not treat them as perfect truth automatically.

---

# 100. Target-semantic mismatch

World and reality quantities must have matching semantics.

Example:

- simulator "collision" event;
- real-world safety incident.

If definitions differ, numerical agreement is not transport.

---

# 101. VWDC05-N9 — Numeric agreement without semantic alignment does not establish transport

Two quantities can share the same numeric values while denoting different events/constructs.

Therefore:

$$
\boxed{
\text{numeric match}
\not\Rightarrow
\text{semantic transport validity}.
}
$$

---

# 102. Semantic contract

Record:

```text
world_quantity_definition
reality_quantity_definition
units
time_window
aggregation_rule
population
intervention_semantics
```

---

# 103. Units

All transport maps should state unit conversion.

Silent unit mismatch is contract failure.

---

# 104. Time alignment

World local time:

$$
\tau_W
$$

must map to reality time:

$$
t_R
$$

under an explicit synchronization rule.

---

# 105. Intervention alignment

World action:

$$
a_W
$$

and real intervention:

$$
a_R
$$

must be semantically aligned before an interventional transport claim.

---

# 106. Policy transport

A world-derived optimal policy may fail in reality even if one-step outcome predictions calibrate well.

Policy transport requires sequential/state-distribution validation.

---

# 107. Distribution shift under deployed policy

Deploying a policy changes the visited reality distribution.

A contract validated under historical policy may face new state distribution after deployment.

---

# 108. Closed-loop transport

Transport contracts for control should include:

- policy;
- induced state distribution;
- action support;
- feedback effects.

---

# 109. Off-policy support relation

If a real action/state region was never externally observed, policy effects there are unsupported without structural assumptions.

This mirrors contextual-bandit positivity.

---

# 110. VWDC05-N10 — Observational support gaps block nonparametric interventional validation

If real validation data contain no support for action $a$ in state region $z$, then without causal/structural assumptions the conditional interventional response in that region is not identified from those observational data alone.

This is a classical positivity/causal-identification boundary.

---

# 111. Transportability literature

Causal transportability formalizes when experimental findings can be moved across populations using explicit structural knowledge about which mechanisms differ.

VWDC inherits the principle:

> transport requires assumptions about invariance/difference, not merely source accuracy.

---

# 112. Contract graph

A runtime can store:

$$
\boxed{
G_{\mathrm{RTC}}
}
$$

whose nodes are transport contracts and whose edges are:

- derived from;
- supersedes;
- subset of;
- structurally transported from;
- invalidated by.

---

# 113. Contract dependency

If world model:

$$
M
$$

is invalidated, every RTC depending on $M$ enters review.

This uses VWDC-03 dependency invalidation.

---

# 114. Contract replay

After recalibrating a world model, validation tests can be replayed from archived external evidence when semantics remain compatible.

New reality data may still be required for current-regime validity.

---

# 115. Validation provenance

Every validation result records:

```text
dataset
data_time
data_domain
measurement_version
world_model_version
validation_code_version
test_statistic
threshold
result
scope
```

---

# 116. Contract audit

An auditor should be able to answer:

1. What exact reality claim is allowed?
2. In what region?
3. Under which model version?
4. Which external data support it?
5. What assumptions remain?
6. What discrepancy remains?
7. What invalidates the contract?

---

# 117. Allowed claim scope

Examples:

```text
WORLD_ONLY
REALITY_MARGINAL
REALITY_CONDITIONAL
REALITY_INTERVENTIONAL
COUNTERFACTUAL_ASSUMPTION_INDEXED
```

---

# 118. Claim renderer

User-facing output should display scope.

Example:

> Validated for one-step marginal prediction on region Z under model v3 and sensor process s2; intervention and individual counterfactual claims are unsupported.

---

# 119. Do not hide assumption-indexed claims

A numeric output can be accompanied by:

```text
assumption_set:
  - shared_latent_rank_invariance
  - copula_family_gaussian
```

rather than presenting it as empirically identified.

---

# 120. Sensitivity interval

For assumption-indexed counterfactual quantity:

$$
q(\alpha),
$$

report:

$$
\boxed{
[
\inf_{\alpha\in\mathcal A}q(\alpha),
\sup_{\alpha\in\mathcal A}q(\alpha)
].
}
$$

This makes structural dependence explicit.

---

# 121. External validation branch

VWDC-04 selects external experiments.

VWDC-05 updates:

$$
\mathsf{RTC}
$$

with their results.

---

# 122. Calibration/validation loop

$$
\boxed{
\text{World Model}
\to
\text{External Compare}
\to
\text{Discrepancy Model}
\to
\text{RTC}
\to
\text{Drift Watch}
\to
\text{Revalidate}.
}
$$

---

# 123. Reality-tether strength

A contract can expose a vector:

$$
\boxed{
\mathbf S_{\mathrm{tether}}
=
(
S_{\mathrm{coverage}},
S_{\mathrm{conditional}},
S_{\mathrm{interventional}},
S_{\mathrm{structural}},
S_{\mathrm{recency}}
).
}
$$

Do not collapse unless a policy demands it.

---

# 124. Recency

Older validation can become less relevant under nonstationary reality.

Track age and drift indicators.

---

# 125. Region-weighted current validity

For deployment distribution:

$$
Q_Z,
$$

compute weighted current debt over cells rather than raw average across validation dataset.

---

# 126. Deployment-shift audit

Compare:

$$
P_{\mathrm{validation}}(Z)
$$

and:

$$
P_{\mathrm{deploy}}(Z).
$$

Large difference increases reweighting/extrapolation debt.

---

# 127. Calibration sample selection

VWDC-04 can actively choose external measurements in high-debt/high-mass regions.

This becomes active reality tethering.

---

# 128. Reality-tethered world

## Definition VWDC05-D2

A world instance/model is **reality tethered for claim $Q$** if there exists a current:

$$
\boxed{
\mathsf{RTC}_Q
}
$$

whose allowed scope contains the intended claim/deployment context.

This is claim relative.

---

# 129. Not globally tethered

A world can be tethered for:

- temperature forecast;

and untethered for:

- failure counterfactual.

No contradiction.

---

# 130. Twin promotion

Possible runtime status:

```text
SIMULATION_ONLY
EXTERNALLY_COMPARED
REALITY_TETHERED_MARGINAL
REALITY_TETHERED_CONDITIONAL
REALITY_TETHERED_INTERVENTIONAL
STRUCTURAL_COUNTERFACTUAL_ASSUMPTION_INDEXED
```

---

# 131. Digital twin naming boundary

VWDC does not legislate who may use the industry term "digital twin."

It defines stricter runtime evidence statuses for WDC claims.

---

# 132. Calibration versus reality tether

A calibrated twin is not necessarily transport-valid for every target claim.

Tether requires claim-specific external validity.

---

# 133. Decision-support threshold

If transport debt is below:

$$
\tau_Q,
$$

claim can be admitted for that decision support policy.

Higher-stakes policy can demand smaller:

$$
\tau_Q.
$$

---

# 134. Risk-tiered transport

Recommended:

```text
LOW_STAKES
OPERATIONAL
HIGH_STAKES
SAFETY_CRITICAL
```

Each can impose different validation/transport thresholds.

---

# 135. Safety-critical boundary

A formal RTC is not a substitute for domain-specific regulatory validation, safety engineering, or legal requirements.

---

# 136. Benchmark A — marginal cancellation

Use the two-stratum counterexample.

Verify marginal error zero while conditional errors are nonzero.

---

# 137. Benchmark B — partial coverage

Leave target mass unvalidated.

Verify uncovered mass contributes explicit worst-case debt.

---

# 138. Benchmark C — counterfactual coupling

Construct two joint potential-outcome laws with identical marginals and different probability of benefit.

---

# 139. Benchmark D — calibration confounding

Use:

$$
Y=\theta+\delta.
$$

Verify nonunique decomposition.

---

# 140. Benchmark E — external fusion

Simulate independent estimators with known variance.

Verify inverse-variance weighting.

---

# 141. Benchmark F — shared external bias

Add common bias.

Verify averaging does not remove it.

---

# 142. Benchmark G — distribution shift

Create bounded discrepancy function and two context distributions.

Verify total-variation transport bound.

---

# 143. Benchmark H — version invalidation

Validate version 0.

Swap to deliberately incorrect version 1.

Ensure RTC enters REVALIDATION_REQUIRED.

---

# 144. Benchmark I — regional extrapolation

Use Lipschitz discrepancy function.

Validate sparse grid.

Check nearest-neighbor extrapolation bound.

---

# 145. Benchmark J — three-part error

Inject known:

- world error;
- transport discrepancy;
- measurement error.

Verify triangle/Lipschitz bound.

---

# 146. Benchmark K — semantic mismatch

Create two numerically identical but differently defined outcome variables.

Ensure transport rejected.

---

# 147. Benchmark L — support gap

Remove real observations for one action/state cell.

Ensure status is UNSUPPORTED absent structural assumptions.

---

# 148. Current literature boundary — transportability

Causal transportability and external-validity theory are established.

VWDC does not claim selection diagrams, do-calculus, or transport formulas as new.

---

# 149. Current literature boundary — Bayesian calibration

Computer-model calibration and model-discrepancy methods are established.

VWDC does not claim calibration/discrepancy modeling as new.

---

# 150. Current literature boundary — digital twin validation

Digital-twin validation, continual updating, uncertainty quantification, and sim-to-real gap analysis are established active research areas.

VWDC provides a runtime contract vocabulary connecting them to branching-world evidence.

---

# 151. Candidate VWDC-specific synthesis

Subject to broader literature audit, the bridge-specific synthesis is:

1. making world-to-reality transport a first-class versioned contract attached to a specific claim/estimand;
2. localizing transport validity over state/action/task regions rather than using a global twin-validity label;
3. integrating marginal, conditional/subtrace, interventional, and structural/counterfactual validation into explicit claim scopes;
4. separating world-estimation, transport, and measurement error in one runtime claim bound;
5. representing unsupported validation mass and regional extrapolation as explicit transport debt;
6. attaching contract expiry to both world-model and reality-regime drift;
7. carrying joint/counterfactual non-identifiability as an assumption-indexed status rather than an implicit simulator output;
8. connecting VWDC-04 external-experiment selection to a persistent reality-tether contract lifecycle.

No strong novelty claim is made in v0.1.

---

# 152. What VWDC-05 proves

Under explicit hypotheses, VWDC-05 proves:

1. marginal agreement can coexist with arbitrarily important conditional mismatch;
2. aggregate signed transport discrepancy is bounded by weighted absolute and maximum local discrepancy;
3. partial validation coverage yields an explicit uncovered-mass worst-case term;
4. identical potential-outcome marginals do not identify individual benefit probability;
5. calibration parameters and model discrepancy can be non-identifiable from field fit alone;
6. inverse-variance weights minimize variance among independent unbiased linear external-evidence fusions;
7. adding many external datasets does not remove shared measurement bias;
8. expected bounded discrepancy under distribution shift changes by at most $M\,TV(P,Q)$ when the discrepancy function itself is stable;
9. validation of one world/reality version does not imply validation of another without an invariance argument;
10. world-estimation, transport, and reality-measurement error compose additively under Lipschitz/triangle assumptions;
11. unsupported regions are not empirically identified without transfer assumptions;
12. Lipschitz regional discrepancy yields an explicit nearest-validation extrapolation bound;
13. restricting claim scope cannot increase worst-case discrepancy;
14. a uniform validated bound safely inherits to subsets of the validated region;
15. perfect in-sample calibration does not prove out-of-support external validity;
16. numeric agreement without semantic alignment does not establish valid transport;
17. observational support gaps block nonparametric intervention validation without additional assumptions.

---

# 153. What VWDC-05 does not prove

It does not prove:

- one transport map works for every quantity;
- conditional validation identifies every latent mechanism;
- interventional validation identifies all individual counterfactuals;
- model-discrepancy functions are identifiable without assumptions;
- external datasets are unbiased or independent;
- total-variation covariate shift captures structural drift;
- Lipschitz discrepancy is valid in every domain;
- continual calibration automatically preserves external validity;
- a digital twin satisfying one RTC is globally reality-valid;
- a VWDC transport contract replaces domain regulation or safety validation.

---

# 154. Proposed VWDC-06

The next paper should use the calibrated transport layer inside **decision and control**:

$$
\boxed{
\textbf{
VWDC-06 — Transport-Aware World Decisions, Policy Transfer, and Reality-Gap Robust Control
}
}
$$

Chinese:

**轉移感知世界決策、策略搬運與現實差距穩健控制**

Main questions:

1. When may a policy optimized in WDC be deployed to reality?
2. How should local transport debt alter action choice?
3. What is robust policy regret under bounded reality gap?
4. How should unsupported action/state regions trigger safe fallback or data collection?
5. How should reality feedback update policy and transport contract jointly?
6. When does policy deployment shift invalidate its own validation distribution?
7. Can a transport-aware Governor choose between simulation policy, conservative policy, human review, and external probe?
8. What guarantees remain under partial transport validity?

---

# 155. References

1. Olav Laudy, **The Digital Twin Counterfactual Framework: A Validation Architecture for Simulated Potential Outcomes**, arXiv:2604.01325, 2026.
2. Mohammadmahdi Ghasemloo, David J. Eckman, Yaxian Li, **Subtrace-Conditional Validation of Simulation Models and Digital Twins**, arXiv:2607.17088, 2026.
3. Judea Pearl, Elias Bareinboim, **External Validity: From Do-Calculus to Transportability Across Populations**, arXiv:1503.01603.
4. Yanqi Xu et al., **Online Bayesian Calibration under Gradual and Abrupt Changes**, arXiv:2605.06612, 2026.
5. Pierre-Louis Ruhlmann et al., **Flow Matching Calibration for Simulation-Based Inference under Model Misspecification**, arXiv:2509.23385, revised 2026.
6. Sizhe Ma, Katherine A. Flanigan, Mario Bergés, **Bridging the Reality Gap in Digital Twins with Context-Aware, Physics-Guided Deep Learning**, arXiv:2505.11847, 2025.
7. Clement Ruah et al., **How to Bridge the Sim-to-Real Gap in Digital Twin-Aided Telecommunication Networks**, arXiv:2507.07067, 2025.
8. **A Continual Validation, Updating, and Decision-Making Framework for Adaptive Digital Twins**, arXiv:2607.18164, 2026.
9. VWDC-01–04, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, and frozen RRT-20, internal series artifacts, 2026.

---

# 156. Conclusion

VWDC-04 asks which external validation experiment deserves budget.

VWDC-05 turns the result into a durable, scoped, versioned Reality Transport Contract.

The contract is not:

> the twin is valid.

It is:

$$
\boxed{
\text{claim}
+
\text{region}
+
\text{versions}
+
\text{validation level}
+
\text{assumptions}
+
\text{residual discrepancy}.
}
$$

Marginal agreement can conceal conditional failure.

Conditional agreement does not identify every counterfactual joint quantity.

Perfect calibration fit can confound physical parameters with model discrepancy.

More external datasets do not remove shared measurement bias.

Old validation does not automatically survive model or reality drift.

And the complete comparison to reality contains at least three distinct error terms:

$$
\boxed{
D
=
D_{\mathrm{world}}
+
D_{\mathrm{transport}}
+
D_{\mathrm{measurement}}.
}
$$

The canonical VWDC-05 principle is:

$$
\boxed{
\textbf{
A simulated world earns the right to support a reality claim one quantity,
one region, one validation level, one assumption set, and one version at a time.
External validity is not a property inherited from visual realism, simulation precision,
or calibration fit; it is a maintained transport contract.
}
}
$$

This establishes the reality-tether layer required before WDC policies can be responsibly transported beyond their simulated worlds.

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
