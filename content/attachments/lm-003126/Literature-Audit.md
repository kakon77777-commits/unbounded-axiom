# VWDC-05 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources only; conservative novelty language.

## 1. Digital-twin counterfactual validation

### The Digital Twin Counterfactual Framework
Laudy, arXiv:2604.01325, 2026.

Formalizes digital-twin simulation in the potential-outcomes framework and proposes a hierarchical validation regime. It distinguishes marginally testable causal quantities from joint/copula-dependent counterfactual quantities that remain assumption indexed.

**VWDC relation:** direct current precedent for the claim that validated marginals do not empirically identify every individual counterfactual quantity.

## 2. Conditional/subtrace validation

### Subtrace-Conditional Validation of Simulation Models and Digital Twins
Ghasemloo, Eckman, Li, arXiv:2607.17088, 2026.

Repeatedly initializes simulations from observed system states and validates conditional output distributions while fixing selected stochastic input primitives to observed realizations. It can expose misspecifications hidden by marginal output validation.

**VWDC relation:** direct precedent for local/conditional RTC validation and discrepancy localization.

## 3. Causal transportability

### External Validity: From Do-Calculus to Transportability Across Populations
Pearl and Bareinboim, arXiv:1503.01603.

Uses selection diagrams and do-calculus to formalize when causal effects can be transported from one population/environment to another and what source/target data are required.

**VWDC relation:** foundational precedent that transportability requires explicit assumptions about source/target differences and cannot be inferred from source accuracy alone.

## 4. Online calibration and drift

### Online Bayesian Calibration under Gradual and Abrupt Changes
Xu et al., arXiv:2605.06612, 2026.

Studies Bayesian digital-twin calibration with model discrepancy, parameter–discrepancy confounding, gradual drift, abrupt regime changes, restart mechanisms, and online validation concerns.

**VWDC relation:** direct current precedent for versioned calibration and contract expiry/revalidation under drift.

### A Continual Validation, Updating, and Decision-Making Framework for Adaptive Digital Twins
arXiv:2607.18164, 2026.

Combines drift detection, parameter-efficient updating, and online statistical validation.

**VWDC relation:** current precedent for continual validity rather than one-time validation.

## 5. Calibration under misspecification

### Flow Matching Calibration for Simulation-Based Inference under Model Misspecification
Ruhlmann et al., arXiv:2509.23385, revised 2026.

Uses scarce calibration observations to correct simulation-trained posterior estimates under simulator/prior/noise misspecification.

**VWDC relation:** direct example of learning an explicit simulation-to-reality correction rather than assuming synthetic and real distributions coincide.

## 6. Reality-gap management

### Bridging the Reality Gap in Digital Twins with Context-Aware, Physics-Guided Deep Learning
Ma, Flanigan, Bergés, arXiv:2505.11847, 2025.

Introduces a reality-gap analysis module that integrates new sensor data, detects context mismatch, and recalibrates a digital twin while preserving simulator guidance.

### How to Bridge the Sim-to-Real Gap in Digital Twin-Aided Telecommunication Networks
Ruah et al., arXiv:2507.07067, 2025.

Studies digital-twin calibration from real measurements and gap-aware training under residual sim-to-real discrepancy.

## 7. Classical mathematical provenance

The following are classical and are not VWDC inventions:

- triangle inequality;
- total-variation expectation bounds;
- inverse-variance weighting;
- potential-outcome non-identifiability from marginals;
- calibration/discrepancy confounding examples;
- causal transportability theory;
- support/positivity requirements;
- Lipschitz extrapolation bounds.

## 8. Candidate VWDC synthesis

Potential bridge-specific synthesis:

1. claim-specific versioned Reality Transport Contract;
2. local state/action/task transport discrepancy map;
3. validation ladder mapped to allowed world-to-reality claim scope;
4. explicit uncovered-mass and extrapolation debt;
5. world/transport/measurement three-part claim error;
6. contract expiry across both world-model drift and reality-regime drift;
7. assumption-indexed counterfactual statuses;
8. direct integration with VWDC-04 external validation experiment selection.

No strong novelty claim is made.
