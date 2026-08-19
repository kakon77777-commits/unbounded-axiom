# VWDC-04 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources only; conservative novelty language.

## 1. Bayesian optimal experimental design

### Efficient Bayesian Optimal Experimental Design for Expensive Computational Models over Finite Design Sets
Dinkel et al., arXiv:2607.16933, 2026.

Develops adaptive BOED for expensive finite experiment sets, including nested Monte Carlo reuse, common random numbers, Rao–Blackwellization, bootstrap design comparisons, and adaptive elimination of inferior designs.

**VWDC relation:** strong current precedent for spending expensive simulation/model evaluations only on experiment designs likely to be informative.

### Optimal Experimental Design using Eigenvalue-Based Criteria with Pyomo.DoE
Laky et al., arXiv:2604.03354, 2026.

Extends digital-twin optimal experiment design with eigenvalue-based information/conditioning criteria and a software abstraction for experiment construction.

**VWDC relation:** direct current precedent for external/digital-twin calibration experiments chosen under limited time/resources.

## 2. Simulation budget allocation

### Optimal Simulation Budget Allocation Under Unknown Sampling Variance
Du, Ryzhov, Gao, arXiv:2509.02138, 2025.

Studies ranking-and-selection simulation allocation when design means and variances are unknown and develops sequential allocation procedures.

**VWDC relation:** direct precedent for nonuniform allocation of simulation compute across candidate world experiments.

## 3. Paired counterfactual coupling

### Twin Rollouts
Ma, Shi, Xu, arXiv:2608.08982, 2026.

Creates factual/counterfactual world-model branches that share generated prefix and future exogenous noise and differ only in post-intervention action stream.

**VWDC relation:** direct precedent for dependence as a deliberate variance-reduction/control device for paired counterfactuals.

## 4. Falsification

### Data-Driven Falsification of Cyber-Physical Systems
Kundu, Gon, Ray, arXiv:2505.03863, 2025.

Searches for violating executions using learned surrogates and decision-tree guidance rather than trying to prove absence of violations.

### Falsification of Cyber-Physical Systems using Bayesian Optimization
Ramezani et al., arXiv:2209.06735.

Uses Bayesian optimization and local surrogate models to choose simulations aimed at specification violation.

### OPINE-World
Courtis, Li, Sanner, arXiv:2607.01531, 2026.

Uses interactive exploration, counterexample-guided programmatic world-model refinement, replay verification, and ontology-error-prioritized testing.

**VWDC relation:** direct precedent for spending world-model interaction budget on discriminating/counterexample-producing probes.

## 5. External validation / digital twins

### The Digital Twin Counterfactual Framework
Laudy, arXiv:2604.01325, 2026.

Introduces a hierarchical validation architecture for digital-twin counterfactual claims and separates observable/marginal validation from assumption-dependent joint counterfactual quantities.

### Subtrace-Conditional Validation of Simulation Models and Digital Twins
Ghasemloo, Eckman, Li, arXiv:2607.17088, 2026.

Uses observed-state initialization and conditional validation over stochastic subtraces to expose simulator/input-model mismatch that marginal validation can miss.

**VWDC relation:** strong precedent for treating external validation as a distinct experiment targeting transport/model discrepancy rather than just adding more simulation rollouts.

## 6. Classical mathematical provenance

The following are classical and not VWDC inventions:

- value of information;
- Bayesian experimental design;
- common random numbers;
- simulation ranking-and-selection;
- equicorrelated variance formulas;
- Beta-Bernoulli conjugacy;
- Bayesian falsification stopping under a specified utility;
- Bellman dynamic programming;
- Pareto necessity.

## 7. Candidate VWDC synthesis

Potential bridge-specific synthesis:

1. branch experiment vocabulary by evidence purpose;
2. explicit same-family correlated-seed marginal-value law;
3. quantitative cost premium for lower-correlation backend evidence;
4. explicit opposite correlation preference for replication versus paired counterfactuals;
5. falsification stopping combined with world-contract-valid counterexample semantics;
6. internal simulation versus external validation through transport-debt decomposition;
7. transport discrepancy as an internal-branching floor;
8. branch-design Bellman state including dependence and transport debt.

No strong novelty claim is made.
