# VWDC-07 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources only; conservative novelty language.

## 1. Continual digital-twin validation and update

### A Continual Validation, Updating, and Decision-Making Framework for Self-Adaptive Digital Twins via Robust Model Predictive Control
Chen et al., arXiv:2607.18164, 2026.

Combines multivariate drift detection, targeted LoRA updating, statistical validation, and robust MPC. Updated surrogates are validated before use in downstream decisions.

**VWDC relation:** direct current precedent for drift-triggered adaptation plus statistically gated promotion.

### Reusing Model Validation Methods for the Continuous Validation of Digital Twins of Cyber-Physical Systems
Mertens and Denil, arXiv:2512.04117, 2025.

Uses recurring validation metrics to detect divergence between a digital twin and its evolving physical counterpart, followed by parameter correction.

**VWDC relation:** precedent for continual rather than one-time twin validity.

## 2. Validation-gated governance

### Validation-Gated Multi-Agent Governance for Online Continual Model Adaptation
arXiv:2606.03321, 2026.

Separates monitor, diagnosis, adaptation, safety-auditor, and orchestrator roles, with champion–challenger gates and shadow learning before model replacement.

**VWDC relation:** very close current precedent for role-separated continual adaptation with guarded promotion.

## 3. Safe policy updates

### SafeAdapt
Anisimov, Belardinelli, Wicker, arXiv:2604.09452, 2026.

Constructs a certified policy-parameter region and projects arbitrary RL updates into it to preserve safety guarantees on previously encountered task distributions.

**VWDC relation:** direct current precedent for adaptation constrained by protected safety guarantees.

### Safe Continual Domain Adaptation after Sim2Real Transfer
Josifovski et al., arXiv:2503.10949, 2025.

Continues policy adaptation after real-world deployment while controlling safety risk and avoiding forgetting of the domain-randomized base policy.

**VWDC relation:** deployment-time adaptation and fallback/preservation precedent.

## 4. Performative / self-consuming feedback loops

### Observations and Remedies for Large Language Model Bias in Self-Consuming Performative Loop
Wang et al., arXiv:2601.05184, 2026.

Studies dynamic feedback loops in which deployed models influence the data later used for retraining, including reduced data collection from groups the current model underserves.

**VWDC relation:** direct contemporary example that deployment policy changes the future data distribution and can create self-confirming adaptation bias.

## 5. Continuous versioning and rollback

### Telecom World Models
arXiv:2604.06882, 2026.

Highlights continual/online adaptation, shadow-mode deployment, safety constraints, versioning, validation, and rollback for live-network world models.

### Network Digital Untwinning
Zhang et al., arXiv:2605.00169, 2026.

Studies checkpoint-based rollback/untwinning mechanisms for selectively removing contributions from network digital twins while preserving model integrity.

**VWDC relation:** direct current precedent for rollback-capable, versioned twin lifecycle management.

## 6. Classical mathematical provenance

The following are classical and not VWDC inventions:

- inverse propensity weighting;
- positivity/support;
- Hoeffding confidence intervals;
- union-bound alpha spending;
- fixed-window mean-change tests;
- dynamic programming;
- version-DAG acyclicity under monotone creation order;
- estimated-action regret bounds.

## 7. Candidate VWDC synthesis

Potential bridge-specific synthesis:

1. world/RTC/policy/safety/authority as one versioned certified deployment pair;
2. explicit adaptation/validation/incident feedback-stream separation;
3. deployment propensity/support as a world-governance object;
4. lifecycle promotion-error budgeting;
5. rollback semantics conditioned on current reality-transport validity;
6. locally preserved action certificates with explicit closed-loop region caveat;
7. incident invalidation tied to dependency blast radius and rollback registry;
8. continual update actions treated as a governed decision problem.

No strong novelty claim is made.
