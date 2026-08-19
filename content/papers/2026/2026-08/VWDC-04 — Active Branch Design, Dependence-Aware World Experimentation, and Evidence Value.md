# VWDC-04 — Active Branch Design, Dependence-Aware World Experimentation, and Evidence Value
## 主動分支設計、依賴性感知世界實驗與證據價值：Replication、Counterfactual、Falsification、External Validation 與停止規則

**Bridge Series:** Visual–World Domain Computation (VWDC) — Paper 04  
**Depends on:** VWDC-01–03, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, frozen RRT-20  
**Author:** Neo.K / EveMissLab  
**Version:** v0.1  
**Date:** 2026-08-17  
**Status:** Formal active-experiment paper. One-step branch value, correlated-seed diminishing returns, backend-diversification premium, paired-counterfactual coupling value, internal-versus-external validation allocation, irreducible transport floor, Bayesian counterexample-search stopping, falsification/estimation sampling separation, finite-horizon branch Bellman control, stopping optimality, and approximate action-regret bounds are proved under explicit hypotheses. Bayesian optimal experimental design, simulation budget allocation, common random numbers, counterexample-guided falsification, and value-of-information planning are established neighboring theory and are not claimed as VWDC inventions. No strong novelty claim is made.

**Keywords:** active branch design, world experiment, value of information, simulation budget, counterexample search, common random numbers, external validation, branch correlation, effective sample size, digital twin, WDC, GVSS

---

# Abstract

VWDC-03 established that branch count is not evidence count.

For equicorrelated replications:

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

For paired counterfactual branches:

$$
\boxed{
\operatorname{Var}(Y_1-Y_0)
=
2\sigma^2(
1-\rho
).
}
$$

These results imply a design problem.

The next unit of compute can be spent on:

- another seed from the same model family;
- a more independent backend/model;
- a noise-coupled paired counterfactual;
- a robustness/sensitivity branch;
- a branch aimed specifically at falsification;
- an external validation experiment;
- or nothing.

VWDC-04 formalizes this decision.

The canonical branch action set is:

$$
\boxed{
\mathcal A_{\mathrm{branch}}
=
\{
\mathrm{REPLICATE},
\mathrm{CHANGE\_BACKEND},
\mathrm{PAIRED\_CF},
\mathrm{ROBUSTNESS},
\mathrm{FALSIFY},
\mathrm{TRANSPORT\_VALIDATE},
\mathrm{STOP}
\}.
}
$$

The action objective depends on the **evidence purpose**.

A branch that is excellent for paired causal contrast may be poor as an independent replication.

A branch that is intentionally biased toward counterexamples may be excellent for falsification but invalid for prevalence estimation.

An external measurement may have little world-state coverage but high value because it attacks model-to-reality transport debt directly.

Therefore:

$$
\boxed{
\text{branch value}
\neq
\text{branch count}.
}
$$

---

# 1. Evidence-purpose state

Let the current claim state be:

$$
\boxed{
S_t
=
(
q_t,
b_t,
\Sigma_t,
\mathcal M_t,
D^{\mathrm{trans}}_t,
B_t,
\mathsf{Prov}_t
),
}
$$

where:

- $q_t$ is the claim/question;
- $b_t$ is the current belief/model state;
- $\Sigma_t$ is dependence/covariance information;
- $\mathcal M_t$ is the active model/backend family state;
- $D^{\mathrm{trans}}_t$ is transport/model-to-reality debt;
- $B_t$ is remaining compute/human/external budget;
- $\mathsf{Prov}_t$ is provenance.

---

# 2. Branch action

## Definition VWDC04-D1

A branch experiment action:

$$
\boxed{
a
\in
\mathcal A_{\mathrm{branch}}
}
$$

has metadata:

$$
\boxed{
\mathsf{Exp}(a)
=
(
Purpose,
Cost,
DependenceProfile,
ModelProfile,
Intervention,
ValidationScope,
OutcomeLaw,
Provenance
).
}
$$

---

# 3. Evidence purpose

## Definition VWDC04-D2

Every action must declare one primary purpose:

$$
\boxed{
P(a)
\in
\{
R,
C,
F,
S,
T
\},
}
$$

where:

- $R$: replication/estimation;
- $C$: paired counterfactual contrast;
- $F$: falsification/counterexample search;
- $S$: robustness/sensitivity;
- $T$: transport/external validation.

One branch can have secondary uses, but one dependence model should not be silently reused for all purposes.

---

# 4. General one-step experiment value

Let current terminal decision/claim risk be:

$$
\boxed{
R(b).
}
$$

After experiment $a$ with observation $Y$:

$$
b
\to
b^{a,Y}.
$$

Experiment cost is:

$$
c(a).
$$

---

# 5. Definition — value of branch experiment

$$
\boxed{
\operatorname{VoB}(a\mid b)
=
R(b)
-
E_Y[
R(
b^{a,Y}
)
]
-
c(a).
}
$$

---

# 6. VWDC04-T1 — One-step branch-value theorem

## Theorem VWDC04-T1

In the one-experiment-then-terminal-decision problem, action $a$ is strictly preferable to stopping and deciding immediately iff:

$$
\boxed{
\operatorname{VoB}(a\mid b)>0.
}
$$

### Proof

Immediate decision has expected cost:

$$
R(b).
$$

Experiment then decision has:

$$
c(a)
+
E_YR(b^{a,Y}).
$$

Compare.

 $\square$

This is classical value-of-information logic specialized to world branching.

---

# 7. Current experimental-design boundary

Bayesian optimal experimental design already asks which experiment maximizes expected information/decision value under cost.

Recent 2026 work studies:

- finite design sets for expensive computational models;
- common random numbers to improve design comparison;
- adaptive elimination of inferior designs;
- eigenvalue-based design criteria for digital-twin calibration.

VWDC does not claim these methods as new.

Its narrower contribution is to type the **world-branch evidence purpose** explicitly.

---

# 8. Replication objective

Suppose the claim is a mean-like world statistic.

There are currently:

$$
n
$$

exchangeable branches with:

$$
\operatorname{Var}(Y_i)=\sigma^2
$$

and:

$$
\operatorname{Corr}(Y_i,Y_j)=\rho
\quad
i\neq j.
$$

---

# 9. Existing mean variance

VWDC-03 gives:

$$
\boxed{
V_n
=
\operatorname{Var}(\bar Y_n)
=
\sigma^2
\left[
\rho
+
\frac{
1-\rho
}{
n
}
\right].
}
$$

---

# 10. VWDC04-T2 — Correlated-seed diminishing-return law

## Theorem VWDC04-T2

If the $(n+1)$ -st branch has the same equicorrelation structure $\rho$, then:

$$
\boxed{
V_n
-
V_{n+1}
=
\frac{
\sigma^2(
1-\rho
)
}{
n(n+1)
}.
}
$$

### Proof

Subtract:

$$
\sigma^2
\left[
\rho
+
\frac{
1-\rho
}{
n
}
\right]
-
\sigma^2
\left[
\rho
+
\frac{
1-\rho
}{
n+1
}
\right].
$$

 $\square$

---

# 11. Interpretation

The marginal variance reduction:

- decreases as $n^{-2}$ ;
- decreases linearly with $1-\rho$ ;
- vanishes as $\rho\to1$.

Thus:

$$
\boxed{
\text{highly correlated extra seeds}
\to
\text{rapidly diminishing replication value}.
}
$$

---

# 12. Replication stopping under variance-price objective

Let uncertainty be priced at:

$$
\lambda>0.
$$

Another same-family seed costs:

$$
c_s.
$$

Continue one more replication only if:

$$
\boxed{
\lambda
\frac{
\sigma^2(
1-\rho
)
}{
n(n+1)
}
>
c_s.
}
$$

This is a one-step objective, not a universal stopping rule.

---

# 13. Same-family versus independent backend

Suppose $n$ existing branches have arbitrary fixed joint covariance.

Candidate branch $s$:

- variance $\sigma^2$ ;
- covariance with each existing branch:
  $$
  \gamma_s\sigma^2.
  $$

Candidate branch $b$:

- same variance $\sigma^2$ ;
- covariance with each existing branch:
  $$
  \gamma_b\sigma^2.
  $$

Assume:

$$
\gamma_b<\gamma_s.
$$

---

# 14. New mean variance

For candidate with cross-correlation $\gamma$, the $(n+1)$ -branch mean variance is:

$$
\boxed{
V_{n+1}(\gamma)
=
\frac{
n^2V_n
+
\sigma^2
+
2n\gamma\sigma^2
}{
(n+1)^2
}.
}
$$

---

# 15. VWDC04-T3 — Dependence-diversification premium

## Theorem VWDC04-T3

The lower-correlation backend reduces mean variance relative to the same-family candidate by:

$$
\boxed{
V_{n+1}(\gamma_s)
-
V_{n+1}(\gamma_b)
=
\frac{
2n\sigma^2(
\gamma_s-\gamma_b
)
}{
(n+1)^2
}.
}
$$

### Proof

Subtract the two expressions.

All existing-branch terms cancel.

 $\square$

---

# 16. Cost threshold for backend diversification

If uncertainty is priced at $\lambda$, the lower-correlation backend $b$ is preferable to same-family seed $s$ under the one-step scalar objective iff:

$$
\boxed{
c_b-c_s
<
\lambda
\frac{
2n\sigma^2(
\gamma_s-\gamma_b
)
}{
(n+1)^2
}.
}
$$

This gives a direct price for evidence independence.

---

# 17. Model diversity is not correlation knowledge

Different:

- provider names;
- architectures;
- model families;

do not imply a known:

$$
\gamma_b.
$$

The covariance/dependence reduction must be measured or conservatively modeled.

---

# 18. Backend exploration

A new backend can be worth testing even when its expected mean prediction is not better.

Its value can come from:

- lower common-mode error;
- independent failure modes;
- transport validation;
- falsification potential.

---

# 19. Paired counterfactual objective

For factual/counterfactual outputs:

$$
Y_0,Y_1,
$$

the quantity of interest is:

$$
\Delta=Y_1-Y_0.
$$

VWDC-03 gives:

$$
\boxed{
\operatorname{Var}(\Delta)
=
2\sigma^2(
1-\rho
).
}
$$

---

# 20. VWDC04-T4 — Coupling preference for fixed-marginal paired contrast

## Theorem VWDC04-T4

If:

- both branch marginal variances remain fixed at $\sigma^2$ ;
- the only statistical objective is minimizing paired contrast variance;
- feasible correlation is:
  $$
  \rho\in[\rho_{\min},\rho_{\max}],
  $$

then the minimum-variance design chooses:

$$
\boxed{
\rho=\rho_{\max}.
}
$$

### Proof

The contrast variance is affine decreasing in $\rho$.

 $\square$

---

# 21. Counterfactual caution

High coupling is valuable for within-model paired contrast.

It is not independent replication.

Do not reuse the same pair as:

- two independent confirmations;
- one paired contrast;

without modeling its covariance.

---

# 22. Twin Rollouts relevance

Current noise-coupled counterfactual world-model work deliberately shares future exogenous noise while changing only the post-intervention action stream.

This is direct precedent for high-correlation branch design serving causal/local contrast rather than replication independence.

---

# 23. Sensitivity branch

A sensitivity branch intentionally varies:

- physics parameter;
- evaluator;
- model;
- initial state;
- rule;
- rendering pipeline.

Its objective is not necessarily unbiased estimation.

Its value is the response surface it reveals.

---

# 24. Robustness branch

A robustness branch tests whether a claim survives model-family changes.

It should maximize **meaningful assumption variation**, not raw branch distance.

---

# 25. Falsification objective

Suppose claim:

$$
\boxed{
\forall W\in\mathcal C,
\quad
P(W).
}
$$

A branch action searches for:

$$
W^\star
$$

with:

$$
\neg P(W^\star).
$$

One valid counterexample is sufficient to refute the universal modeled claim.

---

# 26. Counterexample-search branch probability

Let:

$$
p
$$

be probability that one falsification branch discovers a valid counterexample under a fixed search design.

The value of discovery is:

$$
V_F>0.
$$

Branch cost:

$$
c_F.
$$

---

# 27. Known-p one-step falsification value

Conditional on the universal claim still being alive, one next branch has expected one-step net value:

$$
\boxed{
pV_F-c_F.
}
$$

Continue iff positive under this simplified objective.

---

# 28. Unknown counterexample rate

Suppose:

$$
p
\sim
\operatorname{Beta}(\alpha,\beta).
$$

After:

$$
n
$$

 independent failed falsification attempts and zero counterexamples:

$$
\boxed{
p\mid D_n
\sim
\operatorname{Beta}(
\alpha,
\beta+n
).
}
$$

Posterior mean:

$$
\boxed{
E[p\mid D_n]
=
\frac{
\alpha
}{
\alpha+\beta+n
}.
}
$$

---

# 29. VWDC04-T5 — Bayesian falsification stopping threshold

## Theorem VWDC04-T5

Under the Beta-Bernoulli model and one-step discovery value $V_F$, continue one more falsification branch iff:

$$
\boxed{
V_F
\frac{
\alpha
}{
\alpha+\beta+n
}
>
c_F.
}
$$

Equivalently, when $c_F>0$, continue iff:

$$
\boxed{
n
<
\frac{
\alpha V_F
}{
c_F
}
-
\alpha
-
\beta.
}
$$

### Proof

The posterior predictive probability that the next branch finds a counterexample is the posterior mean of $p$.

Apply one-step expected value.

 $\square$

---

# 30. Interpretation

Repeated failed counterexample search reduces posterior expected discovery rate.

This creates an explicit diminishing-return stopping rule.

The rule is prior/model dependent.

It does not prove no counterexample exists.

---

# 31. VWDC04-N1 — No counterexample found is not proof of universality

## Proposition VWDC04-N1

If the branch search distribution assigns zero probability to a nonempty counterexample region:

$$
B\subseteq\mathcal C,
$$

then any number of samples from that search design can fail to discover $B$.

Thus:

$$
\boxed{
\text{no discovered counterexample}
\not\Rightarrow
\text{universal validity}.
}
$$

 $\square$

---

# 32. Falsification sampling is intentionally biased

A falsification policy may focus on:

- boundary conditions;
- rare failures;
- adversarial regions;
- known weak model states.

This is good for falsification.

It is not representative prevalence estimation.

---

# 33. VWDC04-N2 — Falsification search cannot be reused as prevalence estimation without correction

## Counterexample

Let the real/world class distribution assign failure prevalence:

$$
1\%.
$$

A falsification policy deliberately samples only a high-risk subset where failure prevalence is:

$$
80\%.
$$

The observed branch failure rate:

$$
80\%
$$

is not an unbiased estimate of the class prevalence.

Therefore:

$$
\boxed{
\text{counterexample-oriented sampling}
\not\Rightarrow
\text{population-frequency estimation}.
}
$$

 $\square$

---

# 34. Current falsification precedent

Simulation-based falsification research explicitly chooses test inputs to find violating executions efficiently rather than estimate ordinary-case frequency.

Recent work includes:

- decision-tree-guided/data-driven CPS falsification;
- Bayesian-optimization falsification;
- counterexample-guided world-model exploration.

VWDC does not claim falsification search as new.

---

# 35. OPINE-World relevance

Current 2026 programmatic world-model work uses counterexample-guided repair and actively prioritized environment interaction.

This supports the broader idea that world-model compute can be allocated toward model-breaking/discriminating probes rather than uniform simulation.

---

# 36. Internal versus external evidence

VWDC-03 decomposed a reality-target error bound:

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

- $\varepsilon_W$ is world-estimation/simulation error;
- $\delta_{\mathrm{trans}}$ is model-to-reality transport discrepancy.

---

# 37. Internal branch action

Suppose an internal simulation action $a_I$ reduces:

$$
\varepsilon_W
\to
\varepsilon_W-\Delta\varepsilon
$$

at cost:

$$
c_I.
$$

Its debt reduction is:

$$
\boxed{
\Delta D_I
=
L_T\Delta\varepsilon.
}
$$

---

# 38. External validation action

Suppose external validation action $a_E$ reduces:

$$
\delta_{\mathrm{trans}}
\to
\delta_{\mathrm{trans}}-\Delta\delta
$$

at cost:

$$
c_E.
$$

Its debt reduction is:

$$
\boxed{
\Delta D_E
=
\Delta\delta.
}
$$

---

# 39. VWDC04-T6 — Internal-versus-external validation efficiency threshold

## Theorem VWDC04-T6

If the one-step objective is debt reduction per unit cost, external validation is more efficient than internal simulation iff:

$$
\boxed{
\frac{
\Delta\delta
}{
c_E
}
>
\frac{
L_T\Delta\varepsilon
}{
c_I
}.
}
$$

### Proof

Compare the two benefit-cost ratios.

 $\square$

---

# 40. Total-cost version

If residual debt is priced at:

$$
\lambda,
$$

external validation is preferable to internal branching iff:

$$
\boxed{
c_E-c_I
<
\lambda
[
\Delta\delta
-
L_T\Delta\varepsilon
].
}
$$

---

# 41. VWDC04-T7 — Irreducible transport floor under internal-only branching

## Theorem VWDC04-T7

Suppose a sequence of internal simulation actions yields:

$$
\varepsilon_{W,n}\to0
$$

while transport discrepancy remains fixed:

$$
\delta_{\mathrm{trans}}>0.
$$

Then:

$$
\boxed{
D_n
=
L_T\varepsilon_{W,n}
+
\delta_{\mathrm{trans}}
\to
\delta_{\mathrm{trans}}.
}
$$

### Proof

Take the limit.

 $\square$

More simulation cannot cross the transport floor.

---

# 42. Transport-dominance principle

When:

$$
L_T\varepsilon_W
\ll
\delta_{\mathrm{trans}},
$$

further internal Monte Carlo precision can have little relevance to the reality claim.

The Governor should consider spending on external validation or stopping.

---

# 43. External validation is not always better

External evidence can be:

- costly;
- noisy;
- sparse;
- ethically unavailable;
- distributionally mismatched.

Its value must be computed, not presumed.

---

# 44. Digital-twin experiment-design precedent

Recent digital-twin optimal-design work explicitly studies how to select informative experiments under resource constraints to improve model calibration and decision quality.

VWDC specializes the action set to branching-world evidence purposes.

---

# 45. Finite branch design set

Let candidate experiments be:

$$
\boxed{
\mathcal D_t
=
\{
d_1,\ldots,d_m
\}.
}
$$

Each can represent:

- seed;
- backend;
- intervention;
- external measurement;
- falsification probe.

---

# 46. Expected utility

Let:

$$
U(d)
$$

be expected downstream evidence/decision benefit.

The design problem is:

$$
\boxed{
\max_{
d\in\mathcal D_t
}
[
U(d)-c(d)
].
}
$$

This is a generic finite experiment-design problem.

---

# 47. Common random numbers

When comparing two candidate designs through Monte Carlo, using common random numbers can reduce variance of **differences** when it creates positive correlation.

This is classical simulation methodology.

It is conceptually the same direction as VWDC paired-branch coupling.

---

# 48. Current finite-design BOED precedent

Recent 2026 Bayesian optimal experimental design for expensive finite design sets:

- reuses parameter samples;
- uses common random numbers;
- applies Rao-Blackwellization;
- adaptively allocates compute to promising designs.

VWDC adopts the resource-allocation lesson, not the algorithm as its invention.

---

# 49. Simulation budget allocation precedent

Ranking-and-selection research also studies how simulation budget should be allocated when design means and variances are uncertain.

This is direct precedent for not allocating branch compute uniformly.

---

# 50. Branch design Bellman state

Define:

$$
\boxed{
x_t
=
(
b_t,
\Sigma_t,
\mathcal H_t,
D_t^{\mathrm{trans}},
B_t,
\mathsf{Prov}_t
).
}
$$

---

# 51. Transition

After action $a$ and result $Y$:

$$
\boxed{
x_{t+1}
=
\Phi(
x_t,
a,
Y
).
}
$$

The update can change:

- beliefs;
- covariance;
- model confidence;
- transport debt;
- remaining budget.

---

# 52. VWDC04-D3 — Finite-horizon active branch value

For horizon $T$:

$$
\boxed{
V_t(x)
=
\min_{
a\in\mathcal A(x)
}
\left[
c(a)
+
E_Y
V_{t+1}(
\Phi(x,a,Y)
)
\right].
}
$$

Terminal value:

$$
V_T(x)=R_T(x).
$$

STOP can be included with value:

$$
R_t(x).
$$

---

# 53. VWDC04-T8 — Belief/dependence-state sufficiency under Markov branch design

## Theorem VWDC04-T8

If future branch outcome laws and costs depend on history only through state:

$$
x_t
$$

and chosen action $a_t$, then an optimal finite-horizon branch-design policy can be expressed as:

$$
\boxed{
a_t
=
\pi_t^\star(x_t).
}
$$

### Reason

This is the standard Markov dynamic-programming sufficiency argument.

VWDC does not claim the result as new.

---

# 54. VWDC04-T9 — Branch-design stopping theorem

## Theorem VWDC04-T9

At branch-design state $x$, STOP is optimal iff:

$$
\boxed{
R_t(x)
\le
Q_t(x,a)
\quad
\forall
a\neq\mathrm{STOP}
}
$$

for all feasible continuation experiments.

### Proof

Bellman minimum over STOP and continuation actions.

 $\square$

---

# 55. Interpretation

The correct stopping rule is not:

> run exactly 100 worlds.

It is:

> no remaining experiment has enough expected evidence/decision value to repay its total cost.

---

# 56. Branch-design regret

Let:

$$
Q_t(x,a)
$$

be true action value.

Let:

$$
a^\star
\in
\arg\min_aQ_t(x,a).
$$

Suppose estimated action values satisfy:

$$
\boxed{
|
\widehat Q_t(x,a)
-
Q_t(x,a)
|
\le
\epsilon_a.
}
$$

Estimated controller chooses:

$$
\widehat a
\in
\arg\min_a
\widehat Q_t(x,a).
$$

---

# 57. VWDC04-T10 — One-step experiment-selection regret bound

## Theorem VWDC04-T10

$$
\boxed{
Q_t(x,\widehat a)
-
Q_t(x,a^\star)
\le
\epsilon_{\widehat a}
+
\epsilon_{a^\star}.
}
$$

If all errors are bounded by $\epsilon$:

$$
\boxed{
\operatorname{Regret}
\le
2\epsilon.
}
$$

### Proof

$$
Q(\widehat a)
\le
\widehat Q(\widehat a)+\epsilon_{\widehat a}
\le
\widehat Q(a^\star)+\epsilon_{\widehat a}
\le
Q(a^\star)+\epsilon_{a^\star}+\epsilon_{\widehat a}.
$$

 $\square$

---

# 58. Finite-horizon approximate policy

If each chosen Bellman action is at most:

$$
\epsilon_t
$$

suboptimal in true $Q$ value, cumulative excess cost is bounded by:

$$
\boxed{
\sum_t
\epsilon_t
}
$$

under the same standard finite-horizon induction used in GVSS-06.

---

# 59. Experiment-value uncertainty

The value estimate:

$$
\widehat Q(a)
$$

can itself be uncertain.

A robust Governor can use:

- lower/upper confidence bounds;
- posterior sampling;
- worst-case ambiguity sets;
- value-of-computation analysis.

VWDC-04 does not prescribe one universal estimator.

---

# 60. Experiment confidence separation

If action $a$ satisfies:

$$
\boxed{
UCB(a)
<
\min_{b\neq a}
LCB(b),
}
$$

for cost-minimization action values, then $a$ is optimal throughout the confidence rectangle.

This is the branch-design analogue of GVSS confidence-separated routing.

---

# 61. Replication branch design

For REPLICATION, track:

- branch correlation;
- model/evaluator family;
- ESS;
- covariance estimate;
- claim-specific variance reduction.

---

# 62. Backend-change design

For CHANGE_BACKEND, track:

- extra cost;
- expected dependence reduction;
- model-family uncertainty;
- evaluator compatibility;
- calibration cost.

---

# 63. Paired-counterfactual design

For PAIRED_CF, track:

- shared-noise contract;
- intervention delta;
- paired contrast variance;
- world-model scope;
- transport scope.

---

# 64. Robustness design

For ROBUSTNESS, track:

- assumption/model dimension changed;
- expected model-class coverage;
- claim fragility;
- cost.

---

# 65. Falsification design

For FALSIFY, track:

- target universal claim;
- counterexample proposal distribution;
- posterior discovery rate;
- search bias;
- validity gate.

---

# 66. Transport-validation design

For TRANSPORT_VALIDATE, track:

- external target;
- validation level;
- expected reduction in transport discrepancy;
- cost;
- ethics/access constraints.

---

# 67. Evidence-value vector

Instead of one scalar, expose:

$$
\boxed{
\mathbf V(a)
=
(
V_{\mathrm{rep}},
V_{\mathrm{contrast}},
V_{\mathrm{falsify}},
V_{\mathrm{robust}},
V_{\mathrm{transport}},
-C
).
}
$$

Scalarization is project/claim dependent.

---

# 68. VWDC04-N3 — No universal branch ranking exists across evidence purposes

## Counterexample

Action A:

- creates highly correlated paired branches;
- near-zero contrast variance;
- poor independent replication value.

Action B:

- independent backend;
- higher contrast variance;
- strong replication value.

A ranks above B for paired contrast.

B ranks above A for independent replication.

Therefore:

$$
\boxed{
\text{branch action ranking}
\text{ is purpose dependent}.
}
$$

 $\square$

---

# 69. Evidence-purpose Pareto frontier

Define branch action as nondominated when no other feasible action is:

- no worse on all declared costs;
- no worse on all relevant evidence benefits;
- strictly better somewhere.

---

# 70. VWDC04-T11 — Branch-experiment Pareto necessity

## Theorem VWDC04-T11

Every optimum of a scalar experiment objective strictly increasing in declared costs/debts and strictly decreasing in declared evidence benefits lies on the nondominated branch-experiment frontier.

### Proof

Standard dominance argument.

 $\square$

---

# 71. Independent seed value

Another seed is most valuable when:

- aleatoric variance is high;
- correlation is low;
- current $n$ is small;
- transport/model error is not dominating.

---

# 72. Independent backend value

A new backend is most valuable when:

- common-mode model uncertainty dominates;
- branch correlations are high;
- backend dependence is lower;
- added calibration cost is acceptable.

---

# 73. Coupled counterfactual value

Shared-noise pair is most valuable when:

- target is within-model intervention contrast;
- nuisance randomness is large;
- coupling preserves causal locality;
- independent confirmation is not the immediate objective.

---

# 74. Falsification value

Counterexample search is most valuable when:

- claim is universal/fragile;
- one counterexample has high decision value;
- unexplored/high-risk regions remain;
- proposal design has meaningful counterexample probability.

---

# 75. External validation value

External validation is most valuable when:

- transport discrepancy dominates;
- internal simulation uncertainty is already low;
- real measurement can reduce a decision-relevant transport component.

---

# 76. Stop value

STOP is most valuable when:

- all marginal information values are below cost;
- transport floor is irreducible under available actions;
- target decision is already confidence separated;
- budget is exhausted.

---

# 77. World-space coverage versus evidence independence

A branch can explore a novel world region while sharing the same model bias.

Coverage and evidence independence are different axes.

---

# 78. Branch novelty versus claim value

Novel-looking worlds are not automatically informative for the current claim.

A branch must be evaluated relative to:

$$
q.
$$

---

# 79. Claim-sensitive branch design

The Governor should bind every proposed branch to:

```text
claim_id
evidence_purpose
expected_update
dependence_profile
cost
stop_condition
```

---

# 80. Branch proposal packet

```text
experiment_id
claim_id
purpose
parent_checkpoint
model_backend
provider
evaluator
intervention
noise_coupling
estimated_cost
estimated_dependence
estimated_value
transport_scope
```

---

# 81. Replication packet

```text
target_statistic
current_n
estimated_rho
current_ESS
expected_variance_reduction
seed_family
model_family
```

---

# 82. Backend diversification packet

```text
candidate_backend
estimated_cross_correlation
incremental_cost
calibration_cost
expected_variance_premium
model_family_distance
```

---

# 83. Counterfactual packet

```text
factual_branch
counterfactual_branch
intervention
shared_noise
paired_metric
expected_contrast_variance
reality_transport_scope
```

---

# 84. Falsification packet

```text
universal_claim
proposal_distribution
counterexample_acceptance_test
posterior_discovery_rate
discovery_value
branch_cost
```

---

# 85. Transport validation packet

```text
world_claim
reality_target
current_transport_debt
external_measurement
expected_transport_reduction
cost
validation_level
```

---

# 86. Raw branch count anti-objective

The Governor must not optimize:

$$
\boxed{
\max n_{\mathrm{branches}}
}
$$

unless branch count is itself the declared goal.

---

# 87. ESS-aware replication metric

Report:

$$
\boxed{
\Delta n_{\mathrm{eff}}/c
}
$$

or expected variance reduction per cost, rather than raw branch addition.

---

# 88. Backend independence uncertainty

When $\gamma_b$ is uncertain, the diversification premium is uncertain.

A calibration/probe action may be needed before large backend allocation.

---

# 89. Correlation estimation debt

Estimating branch covariance requires repeated comparable tasks/branches.

Small-sample $\rho$ can be unstable.

Use sensitivity analysis.

---

# 90. Worst-case dependence

If dependence is unknown but common ancestry is strong, a robust replication calculation can assume a plausible upper correlation bound:

$$
\rho\le\rho_{\max}.
$$

Compute conservative ESS under $\rho_{\max}$.

---

# 91. Claim-specific covariance

The correlation of branch losses can differ from correlation of branch images.

Use covariance of the **claim statistic**.

---

# 92. Visual diversity anti-proxy

Do not use visual distance as a direct substitute for evidence correlation.

VWDC-03 already showed the non-identity.

---

# 93. Backend-label anti-proxy

Do not use provider/model names as direct substitute for evidence correlation.

Measure outputs/failures where possible.

---

# 94. Common evaluator branch design

If shared evaluator dominates common-mode error, another world seed is a weak action.

An independent evaluator audit may have higher evidence value.

This can be represented as a branch/validation action.

---

# 95. Common data bias

If all backends rely on the same biased calibration data, backend change may not reduce epistemic dependence.

Dependence profile includes data family.

---

# 96. Model-family experiment

An experiment can intentionally choose a structurally different model family to test robustness.

Its purpose is sensitivity/falsification, not necessarily mean-optimal prediction.

---

# 97. External subtrace experiment

Select a real observed subtrace against which multiple worlds can be conditionally initialized/validated.

This directly targets transport/model mismatch.

---

# 98. Digital twin validation hierarchy

External validation actions should state whether they test:

- marginal behavior;
- conditional behavior;
- intervention response;
- structural assumptions.

Different validation levels reduce different transport debts.

---

# 99. Counterfactual external validation limit

Individual counterfactual outcomes are often unobserved.

External validation can validate components/levels of the simulator without directly observing every counterfactual.

Transport claims remain assumption indexed.

---

# 100. Decision value versus information entropy

An experiment can reduce entropy but not change the downstream decision.

Its decision value may be low.

VWDC prefers decision/evidence-purpose value over generic uncertainty reduction when the target decision is known.

---

# 101. Model-learning value

If the same world model will be reused across many future claims, an experiment can have option value beyond the current claim.

This can be included as:

$$
V_{\mathrm{option}}.
$$

---

# 102. Branch action total value

Engineering decomposition:

$$
\boxed{
V_{\mathrm{total}}(a)
=
V_{\mathrm{current}}
+
V_{\mathrm{falsify}}
+
V_{\mathrm{transport}}
+
V_{\mathrm{option}}
-
C(a).
}
$$

Not a universal additive theorem.

---

# 103. Multi-claim experiment

One experiment may update several claims.

The Governor can aggregate decision value across claim set with explicit weights.

---

# 104. Scientific portfolio

A WDC system can maintain:

$$
\boxed{
\mathcal Q
=
\{
q_1,\ldots,q_m
\}
}
$$

with branch actions competing for a shared budget.

---

# 105. Cross-claim external validation

One real measurement may validate many world branches/models simultaneously.

This can produce high option value.

---

# 106. Branch design as experiment portfolio

Selecting multiple experiments under budget becomes:

- knapsack;
- submodular design;
- Bayesian adaptive design;
- ranking-and-selection;

depending on assumptions.

VWDC does not declare one universal optimizer.

---

# 107. Batch branch design

If actions are launched in parallel, their values are not additive when information overlaps.

A batch experiment planner should account for redundancy.

---

# 108. Parallel seeds

Launching 100 same-family seeds simultaneously can waste budget if early results would have triggered a backend switch or STOP.

Adaptive sequential allocation can dominate fixed batch allocation.

---

# 109. Adaptive versus fixed design

The value of an experiment depends on previous results.

Thus sequential policies can outperform fixed schedules.

This is classical adaptive design.

---

# 110. Finite-design elimination

For a finite set of candidate experiments, inferior designs can be eliminated as evidence about their values accumulates.

Current BOED work explicitly uses adaptive elimination to reduce expensive model evaluations.

---

# 111. Common-random-number design comparison

When comparing two candidate experiment-value estimators, common random numbers can reduce variance of their difference.

This is useful for branch-policy selection itself.

---

# 112. Meta-experimentation

A WDC Governor may run cheap pilot branches to estimate which expensive experiment is worth doing.

The experiment design process is itself reflexive.

---

# 113. RRT connection

The experiment policy depends on the representation of:

- claim;
- dependence;
- transport;
- uncertainty.

Changing those representations changes experiment value.

VWDC retains RRT provenance.

---

# 114. GVSS connection

For visual-world claims, GVSS can provide:

- provider router;
- evaluator uncertainty;
- visual deficit;
- visual task regions.

These influence branch design.

---

# 115. WDC connection

WDC provides:

- world forks;
- checkpoints;
- local time;
- interventions;
- branch budget;
- Governor.

VWDC-04 supplies evidence-aware experiment valuation to the Governor.

---

# 116. Governor action hierarchy

Conceptually:

$$
\boxed{
\text{WDC Governor}
\to
\text{VWDC Experiment Designer}
\to
\text{VWDC Path Planner}
\to
\text{GVSS Provider Router}.
}
$$

This is a decision decomposition, not mandatory software inheritance.

---

# 117. Claim state transition

A branch can:

- strengthen belief;
- expose dependence;
- falsify claim;
- change transport validity;
- invalidate model.

The result is not merely another output image.

---

# 118. Counterexample terminal state

Once a universal modeled claim is validly falsified, replication of that claim may terminate.

Compute should shift to:

- repair;
- model-class update;
- replacement hypothesis;
- counterexample generalization.

---

# 119. Discovery value

Counterexample value can exceed ordinary information gain because it changes the logical status of a universal claim discontinuously.

This is claim-semantics dependent.

---

# 120. Probability of valid counterexample

Falsification probability must include:

$$
\boxed{
p_{\mathrm{valid}}
=
p_{\mathrm{discover}}
\times
p_{\mathrm{contract-valid}}
}
$$

if proposal generation can produce invalid worlds.

A visually strange output is not automatically a valid counterexample.

---

# 121. Counterexample verification

Every discovered counterexample must pass:

- world contract;
- claim applicability;
- evaluator verification;
- provenance.

---

# 122. Adversarial invalid examples

An optimizer can find invalid states outside the claim domain.

These do not falsify the claim.

Typed world contracts prevent false counterexamples.

---

# 123. Counterexample search space

Search should target:

$$
\boxed{
\mathcal C_{\mathrm{valid}}
}
$$

not unrestricted image/world artifacts.

---

# 124. Falsification coverage

Failure to find a counterexample in one proposal distribution says little about unexplored regions.

Track proposal/search coverage.

---

# 125. Search proposal drift

As the model learns, counterexample proposal distribution can adapt.

The Beta-Bernoulli constant- $p$ theorem is then only a simplified baseline.

---

# 126. Adaptive falsification

Bayesian optimization, decision-tree guidance, and counterexample-guided exploration are current approaches.

VWDC can import them.

---

# 127. Transport validation actions

Examples:

- one external sensor measurement;
- one observed transition subtrace;
- one real intervention result;
- one human expert label;
- one high-fidelity benchmark.

Each targets different debt.

---

# 128. External validation provenance

External evidence requires:

- source;
- time;
- measurement process;
- calibration;
- domain;
- privacy/consent when relevant.

---

# 129. Validation mismatch

External data outside the target domain may not reduce the relevant transport discrepancy.

Validation value is target specific.

---

# 130. External measurement reuse

One measurement can support multiple claims but creates dependence among those claims.

Record shared validation source.

---

# 131. Evidence discount

If one external measurement is reused many times, it should not be counted as many independent external measurements.

Same evidence provenance rule.

---

# 132. Stopping at transport floor

If no available external validation action exists and internal uncertainty is already negligible relative to transport debt, the correct output can be:

```text
STOP_INTERNAL_SIMULATION
TRANSPORT_LIMIT_REMAINS
```

rather than infinite branching.

---

# 133. Decision threshold

If claim/action decision is already stable across remaining uncertainty, further branch value can be zero even before statistical uncertainty is minimal.

---

# 134. Confidence-separated decision

Suppose all plausible claim models lead to the same downstream decision.

Then decision-focused experiment value is zero, though scientific/model-learning value may remain.

---

# 135. Exploration for future option value

A branch can still be valuable for future tasks.

That value must be stated separately.

---

# 136. Resource budgets

Separate:

$$
\boxed{
B
=
(
B_{\mathrm{GPU}},
B_{\mathrm{provider}},
B_{\mathrm{human}},
B_{\mathrm{external}},
B_{\mathrm{time}}
).
}
$$

One scalar cost can hide constraints.

---

# 137. Multi-budget feasibility

Experiment $a$ is feasible iff:

$$
\boxed{
c_j(a)\le B_j
}
$$

for all hard resource dimensions.

---

# 138. VWDC04-T12 — Budget monotonicity of optimal experiment value

## Theorem VWDC04-T12

If larger budget only enlarges the feasible experiment-policy set and unused budget can be ignored, then the optimal cost-to-go is nonincreasing with budget.

### Proof

A larger-budget policy can emulate every smaller-budget policy.

 $\square$

---

# 139. More budget need not be spent

Budget monotonicity is about available options, not mandatory consumption.

STOP can remain optimal.

---

# 140. Experiment-mode hysteresis

If switching between:

- same-model replication;
- independent backend;
- external validation;

has setup cost, a small value-estimation fluctuation should not cause constant switching.

Use hysteresis/commitment windows if needed.

Engineering rule only.

---

# 141. Batch cancellation

If early result falsifies a universal claim, cancel pending confirmation branches when possible.

This is one benefit of asynchronous adaptive design.

---

# 142. Branch queue priority

Suggested priority score:

$$
\boxed{
Priority(a)
=
\frac{
\widehat V(a)
}{
\widehat C(a)
}
\times
\mathsf{Urgency}(q)
}
$$

only as an engineering heuristic.

---

# 143. Logical priority

A low-probability counterexample branch can deserve high priority when the claim is high-stakes and universal.

---

# 144. Model audit priority

A branch that changes model family can be high-value when common-mode model risk dominates.

---

# 145. Evaluator audit priority

An independent evaluator can be more valuable than another world rollout when observer common-mode bias dominates.

---

# 146. Reality audit priority

External validation can be more valuable than both when transport debt dominates.

---

# 147. Branch portfolio dashboard

Report:

```text
claim_id
purpose
branch_count
effective_sample_size
model_family_count
evaluator_family_count
current_world_error
current_transport_debt
candidate_experiments
expected_value
cost
stop_condition
```

---

# 148. Experiment ledger

Every selected action logs:

```text
experiment_id
selection_policy_version
estimated_value_before
observed_result
belief_update
dependence_update
transport_update
actual_cost
counterfactual_best_action
```

This enables branch-design regret analysis.

---

# 149. Counterfactual best action

After observing results, the runtime can retrospectively estimate whether another experiment would have been better.

This is evaluation, not proof.

---

# 150. Policy benchmarking

Synthetic world benchmark can expose exact:

- claim truth;
- covariance;
- transport discrepancy;
- branch costs;
- counterexample region.

Then compare branch-design policies.

---

# 151. Benchmark A — correlated seed saturation

Fix:

$$
\rho=0.8.
$$

Increase $n$.

Verify marginal variance reduction:

$$
\propto
1/[n(n+1)].
$$

---

# 152. Benchmark B — backend diversification

Create candidates with:

$$
\gamma_s>\gamma_b.
$$

Verify diversification premium.

---

# 153. Benchmark C — paired counterfactual

Vary shared-noise coupling.

Measure paired contrast variance.

---

# 154. Benchmark D — falsification stopping

Use Beta prior and hidden counterexample probability.

Compare fixed search versus posterior stopping.

---

# 155. Benchmark E — search bias

Use adversarial proposal distribution with high failure rate.

Verify it is good for falsification but bad for prevalence estimation.

---

# 156. Benchmark F — transport floor

Make internal simulation error reducible but transport discrepancy fixed.

Verify optimal policy eventually switches to validation/STOP.

---

# 157. Benchmark G — external validation

Allow an external measurement to shrink transport discrepancy.

Measure break-even cost.

---

# 158. Benchmark H — action-regret

Inject noise into estimated branch-action values.

Verify one-step regret bound.

---

# 159. Benchmark I — purpose reversal

Construct two actions where:

- paired branch wins for contrast;
- independent backend wins for replication.

Verify no universal ranking.

---

# 160. Benchmark J — counterexample terminal logic

One valid counterexample changes universal claim status immediately.

Compare with many non-counterexample branches.

---

# 161. Current literature boundary — BOED

Bayesian optimal experimental design is established.

VWDC uses it as the general decision-theoretic family for experiment selection.

---

# 162. Current literature boundary — simulation allocation

Ranking-and-selection and optimal simulation budget allocation are established.

VWDC does not claim simulation-budget allocation theory as new.

---

# 163. Current literature boundary — common random numbers

Common random numbers and paired simulation are established variance-reduction techniques.

VWDC uses the same mathematical logic for coupled world branches.

---

# 164. Current literature boundary — falsification

Simulation-based falsification and counterexample-guided testing are established.

VWDC integrates their logical purpose into branch governance.

---

# 165. Current literature boundary — digital twin validation

Digital-twin validation already distinguishes simulation accuracy from external validity.

VWDC integrates external validation as a competing branch-budget action.

---

# 166. Candidate VWDC-specific synthesis

Subject to broader literature audit, the bridge-specific synthesis is:

1. a unified WDC branch-action vocabulary separating replication, paired counterfactual, robustness, falsification, and transport validation;
2. an explicit correlated-seed diminishing-return law used as a Governor stopping signal;
3. a quantitative premium for buying lower branch correlation through a different backend;
4. explicit opposite correlation preferences for replication versus paired counterfactual contrast;
5. Bayesian counterexample-search stopping integrated with world-claim logic;
6. internal simulation versus external validation allocation through transport-debt decomposition;
7. treating transport discrepancy as an irreducible floor for internal-only branching;
8. branch-design Bellman state carrying dependence and transport debt;
9. branch-design regret and provenance for experiment-policy evaluation.

No strong novelty claim is made in v0.1.

---

# 167. What VWDC-04 proves

Under explicit hypotheses, VWDC-04 proves:

1. one-step branch experiment is worthwhile exactly when expected downstream risk reduction exceeds experiment cost;
2. equicorrelated same-family replication has marginal variance reduction $\sigma^2(1-\rho)/[n(n+1)]$ ;
3. a lower-correlation backend has the stated quantitative variance-diversification premium;
4. paired contrast variance is minimized by maximal feasible positive coupling under fixed marginals;
5. Beta-Bernoulli falsification search yields an explicit posterior one-step stopping threshold;
6. absence of discovered counterexamples does not prove a universal claim when search has blind regions;
7. falsification-biased sampling does not estimate population prevalence without correction;
8. external validation beats internal branching on debt-reduction-per-cost exactly under the stated inequality;
9. internal-only branching cannot reduce total reality-claim debt below fixed transport discrepancy;
10. under Markov state assumptions, finite-horizon active branch design admits a state-based optimal policy;
11. STOP is optimal exactly when all continuation experiment values are no better;
12. estimated branch-action values yield the stated one-step regret bound;
13. branch-action rankings can reverse across evidence purposes;
14. every strictly monotone scalar experiment optimum lies on the experiment Pareto frontier;
15. optimal cost-to-go is nonincreasing with available budget under nested feasibility.

---

# 168. What VWDC-04 does not prove

It does not prove:

- branch correlations are known exactly;
- equicorrelation is realistic for every branch family;
- different model brands imply lower correlation;
- maximal coupling always gives valid counterfactual semantics;
- the Beta-Bernoulli model is correct for adaptive falsification;
- failing to find a counterexample validates universality;
- external measurements always reduce transport debt;
- one scalar experiment value is sufficient for every scientific objective;
- experiment-action values are easy to estimate;
- finite-horizon Bellman planning is computationally tractable at full WDC scale;
- one branch-design policy is universally optimal.

---

# 169. Proposed VWDC-05

The next bridge paper should move from **choosing experiments** to **calibrating and maintaining the reality transport layer itself**:

$$
\boxed{
\textbf{
VWDC-05 — Reality-Tethered World Calibration, Transport Contracts, and External Validity
}
}
$$

Chinese:

**現實繫結世界校準、轉移契約與外部有效性**

Main questions:

1. How should a world-to-reality transport contract be parameterized?
2. Which discrepancy components are empirically testable?
3. How should conditional/subtrace validation update transport debt?
4. How should transport contracts expire under world/reality drift?
5. How should multiple external datasets be combined?
6. When does a digital twin become sufficiently calibrated for decision support?
7. How should unsupported counterfactual quantities be labeled?
8. Can transport-validity debt be decomposed by state/action region?

---

# 170. References

1. Maximilian Dinkel, Dragos C. Ana, Benedikt Goderbauer, Wolfgang A. Wall, **Efficient Bayesian Optimal Experimental Design for Expensive Computational Models over Finite Design Sets**, arXiv:2607.16933, 2026.
2. Daniel J. Laky et al., **Optimal Experimental Design using Eigenvalue-Based Criteria with Pyomo.DoE**, arXiv:2604.03354, 2026.
3. Jianzhong Du, Ilya O. Ryzhov, Siyang Gao, **Optimal Simulation Budget Allocation Under Unknown Sampling Variance**, arXiv:2509.02138, 2025.
4. Yu Ma, Hongli Shi, Xinran Xu, **Twin Rollouts: Noise-Coupled Counterfactual Branching in Interactive Video World Models**, arXiv:2608.08982, 2026.
5. Atanu Kundu, Sauvik Gon, Rajarshi Ray, **Data-Driven Falsification of Cyber-Physical Systems**, arXiv:2505.03863, 2025.
6. Zahra Ramezani, Kenan Šehić, Luigi Nardi, Knut Åkesson, **Falsification of Cyber-Physical Systems using Bayesian Optimization**, arXiv:2209.06735.
7. David Courtis, Wenhao Li, Scott Sanner, **OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration**, arXiv:2607.01531, 2026.
8. Olav Laudy, **The Digital Twin Counterfactual Framework: A Validation Architecture for Simulated Potential Outcomes**, arXiv:2604.01325, 2026.
9. Mohammadmahdi Ghasemloo, David J. Eckman, Yaxian Li, **Subtrace-Conditional Validation of Simulation Models and Digital Twins**, arXiv:2607.17088, 2026.
10. VWDC-01–03, GVSS-01–10, WDC-01–08, WDC Runtime Whitepaper, and frozen RRT-20, internal series artifacts, 2026.

---

# 171. Conclusion

VWDC-03 showed how branch evidence depends on ancestry, models, evaluators, coupling, and reality transport.

VWDC-04 turns that accounting into experiment selection.

Another same-family seed has marginal replication value:

$$
\boxed{
\frac{
\sigma^2(1-\rho)
}{
n(n+1)
}.
}
$$

A lower-correlation backend has a measurable diversification premium.

Positive coupling is bad for independent replication but can be excellent for paired counterfactual contrasts.

Counterexample search should be valued by discovery probability and logical value, not by representativeness.

External validation competes directly with internal simulation once transport debt is explicit.

And if transport discrepancy is fixed:

$$
\boxed{
D_n
\to
\delta_{\mathrm{trans}}
}
$$

no matter how many internal branches are added.

The canonical VWDC-04 principle is:

$$
\boxed{
\textbf{
The next world should be created for a reason.
Use low-correlation branches for replication,
high-correlation twins for paired contrasts,
targeted branches for falsification,
and external measurements when transport error—not Monte Carlo error—is the limiting uncertainty.
}
}
$$

This turns WDC branching from a world-generation engine into an evidence-aware experimental system.

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
