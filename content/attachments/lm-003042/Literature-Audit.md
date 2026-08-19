# GVSS-07 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources; conservative novelty language.

## 1. Active system identification

### ASID: Active Exploration for System Identification in Robotic Manipulation
Memmel et al., arXiv:2404.12308 / ICLR 2024.

Uses an initially imperfect simulator to design exploration policies that collect informative real-world data, identify physical parameters, and improve sim-to-real control.

**GVSS relation:** direct methodological precedent for choosing actions because they make a hidden model more identifiable.

### Online Design of Experiments by Active Learning for Nonlinear System Identification
Xie and Bemporad, arXiv:2506.21754, 2025.

Selects runtime excitation using active-learning criteria for nonlinear autoregressive/state-space model identification and recursively updates estimates.

**GVSS relation:** direct precedent for active data allocation rather than passive trace collection.

### Model Identification Adaptive Control with rho-POMDP Planning
Ho, Jamgochian, Kochenderfer, arXiv:2505.09119, 2025.

Treats unknown system parameters as hidden states and jointly balances parameter identification with control in belief space.

**GVSS relation:** close conceptual precedent for GVSS-06/07's joint visual correction and diagnostic-model identification.

## 2. Latent POMDP/world-model learning

### Learning POMDP World Models from Observations with Language-Model Priors
Six et al., arXiv:2605.13740, 2026.

Pinductor proposes and refines POMDP models from observation-action trajectories, using language-model priors to reduce interaction.

**GVSS relation:** current precedent for learning hidden transition/observation structure when failure labels are not directly observed.

## 3. Nonstationarity and model drift

### Situationally-Aware Dynamics Learning
Murillo-Gonzalez and Liu, arXiv:2505.19574 / IJRR 2026.

Learns hidden situation representations and uses Bayesian online changepoint detection to adapt dynamics modeling as the data-generating regime changes.

**GVSS relation:** direct current precedent for version/context-dependent diagnostic dynamics.

### Online Identification of Time-Varying Systems Using Excitation Sets and Change Point Detection
Leung, Hota, Paré, arXiv:2406.10349.

Uses informative excitation sets and change-point detection/resetting to improve identification in time-varying systems.

**GVSS relation:** direct precedent for invalidating/resetting stale diagnostic models after behavior changes.

## 4. Safety-constrained system identification

### Provably-Safe, Online System Identification
Zhang, Zhou, Vasudevan, arXiv:2504.21486, 2025.

Designs exciting trajectories for online parameter identification while satisfying safety/state/input constraints.

**GVSS relation:** calibration/failure-injection actions should obey project constraints rather than identify at any cost.

## 5. Novelty boundary

Do not claim as GVSS inventions:

- system identification;
- active input design;
- POMDP model learning;
- Bayesian categorical estimation;
- Hoeffding confidence bounds;
- change-point detection;
- robust control under model uncertainty;
- sim-to-real transfer.

Potential GVSS-07 synthesis contribution:

1. treating GVSS failure-transition and diagnostic-likelihood tables as first-class system-ID targets;
2. controlled visual failure injection as a direct-label identification mechanism;
3. explicit identification status/provenance per action–failure row;
4. version drift tests for provider/evaluator/compiler diagnostic models;
5. active sample allocation using downstream row importance;
6. a combined transition/observation uncertainty bound fed directly into GVSS-06 failure belief;
7. separating pseudo-label agreement from independently identified diagnostic truth.

No strong novelty claim is made in v0.1.
