# VWDC-03 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources only; conservative novelty language.

## 1. Noise-coupled counterfactual branching

### Twin Rollouts
Ma, Shi, Xu, arXiv:2608.08982, 2026.

Formalizes factual/counterfactual branches inside interactive video world-model rollouts. The two branches share the generated prefix and future exogenous noise and differ only in the post-intervention action stream.

**VWDC relation:** unusually direct current precedent for deliberately dependent sibling branches used for minimal-change paired counterfactual comparison.

**Boundary:** coupled branches are not independent replications.

## 2. Digital-twin counterfactual validation

### The Digital Twin Counterfactual Framework
Laudy, arXiv:2604.01325, 2026.

Places digital-twin simulation inside the potential-outcomes framework and introduces hierarchical validation levels. It distinguishes marginally testable causal quantities from joint/counterfactual quantities that remain assumption dependent.

**VWDC relation:** strong current precedent for the rule that simulated counterfactuals require explicit validation/assumption scopes before reality transport.

## 3. Conditional simulation validation

### Subtrace-Conditional Validation of Simulation Models and Digital Twins
Ghasemloo, Eckman, Li, arXiv:2607.17088, 2026.

Repeatedly initializes simulations from observed states and validates conditional output distributions while fixing selected stochastic primitives. The approach can expose input-model misspecification that marginal-output validation misses.

**VWDC relation:** direct current precedent for checkpoint/subtrace-conditioned validation and diagnosis of hidden simulator mismatch.

## 4. Provenance and reproducibility

### Machine Learning Pipelines: Provenance, Reproducibility and FAIR Data Principles
Samuel, Löffler, König-Ries, arXiv:2006.12117, 2020.

Studies end-to-end provenance requirements for reproducible ML workflows.

### Pipeline Provenance for Analysis, Evaluation, Trust or Reproducibility
Johnson et al., arXiv:2404.14378, 2024.

Presents automated provenance generation/modeling for processing pipelines and relates provenance to evaluation, trust, and reproducibility.

**VWDC relation:** prior engineering precedent for explicit dependency/provenance structures used for audit and replay.

## 5. Digital-twin uncertainty

### Quantifying and combining uncertainty for improving the behavior of Digital Twin Systems
Deantoni et al., arXiv:2402.10535, 2024.

Explicitly represents uncertainty in physical/twin systems and studies comparison and combination under uncertainty.

**VWDC relation:** prior precedent for keeping simulation/twin uncertainty explicit rather than treating the twin as exact.

## 6. Classical mathematical provenance

The following are classical and not VWDC inventions:

- law of total covariance;
- equicorrelated effective sample size;
- paired-difference variance;
- common-random-number coupling ideas;
- graph descendant closure;
- deterministic replay induction;
- first-order logical falsification;
- triangle-inequality error transport;
- DAG acyclicity under creation order;
- Pareto necessity.

## 7. Candidate VWDC synthesis

Potential bridge-specific synthesis, subject to wider audit:

1. sibling-world independence as a claim-specific evidence property, not a world-ID property;
2. explicit dual-use separation between dependent paired counterfactuals and independent replication;
3. evidence invalidation/replay integrated with world checkpoints and visual/provider lineage;
4. separate graphs for lineage, dependency, communication, and reality transport;
5. world-estimation/transport error composition for reality claims;
6. branch-purpose labels for replication, falsification, paired counterfactuals, sensitivity, and transport validation.

No strong novelty claim is made.
