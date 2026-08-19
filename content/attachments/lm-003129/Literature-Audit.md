# VWDC-08 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources only; conservative novelty language.

## 1. Continual digital-twin validation

### A Continual Validation, Updating, and Decision-Making Framework for Self-Adaptive Digital Twins via Robust Model Predictive Control
Chen et al., arXiv:2607.18164, 2026.

Integrates drift detection, targeted neural surrogate updates, statistical validation, uncertainty restoration, and robust MPC in an adaptive digital-twin loop.

**VWDC relation:** direct current precedent for continual model updates that are detected, adapted, and statistically validated before use in decisions.

## 2. Certified safe policy/model updates

### SafeAdapt
Anisimov, Belardinelli, Wicker, arXiv:2604.09452, 2026.

Constructs a certified locally invariant/Rashomon region in policy parameter space and projects downstream RL updates into that region to preserve specified source-task safety properties.

**VWDC relation:** direct current precedent for protecting a certified property through continual policy updates.

### Provably Safe Model Updates
Elmecker-Plakolm et al., arXiv:2512.01899, 2025.

Computes tractable approximations to locally invariant parameter domains in which model updates preserve required specifications.

**VWDC relation:** direct precedent for update invariants and the separation of arbitrary learner updates from a certified admissible update region.

### Learning over Forward-Invariant Policy Classes
Tsai et al., arXiv:2604.07875, 2026.

Builds a finite policy/action class from stabilizing feedback laws that preserve forward invariance of a safe state set.

**VWDC relation:** direct current precedent for treating forward invariance as a policy-class construction rather than an after-the-fact penalty.

## 3. Runtime assurance and bounded recovery

### Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers
Shojaei, arXiv:2606.25371, 2026.

Uses conformal recovery-deadline certificates for adapting controllers, while a verified runtime-assurance backstop enforces a hard critical limit.

**VWDC relation:** unusually direct current precedent for separating statistical recovery/autonomy certificates from a verified fallback and for making recovery time a first-class safety object.

## 4. Validation-gated multi-agent adaptation

### Validation-Gated Multi-Agent Governance for Online Continual Model Adaptation
arXiv:2606.03321, 2026.

Separates monitor, diagnosis, adaptation, safety-auditor, and orchestrator roles and uses deterministic champion–challenger gates plus background shadow learning.

**VWDC relation:** direct current precedent for many cognitive/adaptation components operating behind a guarded promotion/commit boundary.

## 5. Certificate-gated infrastructure control

### AI Infrastructure Sovereignty
arXiv:2602.10900, 2026.

Proposes an execution layer with a strict invariant: actions must carry a current digital-twin validation certificate before reaching southbound interfaces; expired certificates are withheld for re-evaluation.

**VWDC relation:** direct current architectural precedent for fail-closed certificate-gated commit authority.

## 6. Classical mathematical provenance

The following are classical and not VWDC inventions:

- set intersection feasibility;
- serialization/transactional invariant checking;
- forward invariance;
- induction over invariant sets;
- runtime assurance;
- hysteresis/minimum-improvement switching;
- finite improvement/churn bounds;
- dynamic regret;
- append-only DAG acyclicity.

## 7. Candidate VWDC synthesis

Potential bridge-specific synthesis:

1. governance meta-state combining world, transport, policy, safety, authority, provenance, and recovery;
2. certificate-conjunction executable action set;
3. reality-state and governance-meta-state invariance in one continual architecture;
4. stale concurrent proposal no-go and atomic commit-time revalidation;
5. frozen-regime minimum-improvement churn bound;
6. certified-time-fraction stability under sparse nonstationary regime changes;
7. explicit non-equivalence between parameter convergence and governance stability;
8. regime-conditioned champion and rollback-reserve registries;
9. suspension semantics when the certified governance envelope is empty;
10. recovery deadline and physical actuation timing as part of the governance certificate.

No strong novelty claim is made.
