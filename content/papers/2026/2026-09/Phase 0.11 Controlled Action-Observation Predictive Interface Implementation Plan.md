# Phase 0.11 Controlled Action-Observation Predictive Interface Implementation Plan

> **For agentic workers:** Execute task-by-task with TDD and preserve all negative results.

**Goal:** Build a synthetic but explicit CWB/MWT world loop in which cognition emits ActionRequest objects, the boundary authorizes/maps/commits World transitions, observer-relative presentations are emitted, and predictive states are learned from action-conditioned future observations.

**Architecture:** Use a finite partially observable world with hidden stock/gate/stability/energy variables, a six-action CWB-controlled interface, noisy observer presentations, and six world regimes. Learn Controlled Action-Observation Predictive Interface States (CAPIS) by pooling observable presentations whose action-conditioned future-observation signatures are similar. Compare against passive observation, exact observation+action, an unavailable hidden-state oracle, action-shuffled nulls, and leave-one-regime-out transfer.

**Tech Stack:** Python 3 standard library plus pytest; scikit-learn only for optional NMI/ARI diagnostics.

## Hard constraints

- `ActionRequest`, CWB authorization, `WorldTransition`, and `OutcomePresentation` remain separate records.
- Cognitive operators do not directly mutate World.
- Hidden world state is available only to the simulator/oracle baseline, never to CAPIS.
- CAPIS is not called an exact PSR, belief state, causal state, or world ontology.
- Train+validation only selects CAPIS thresholds/support; test never selects.
- Human cognitive family labels are not used to generate world transitions.
- No domain promotion from synthetic Phase 0.11 evidence.

## Tasks

1. TDD the controlled world and CWB legality chain.
2. TDD the observer-relative noisy presentation and exploratory behavior policy.
3. TDD factorized action-conditioned coders and CAPIS predictive-signature pooling.
4. Run normal train/validation/test and five stress regimes.
5. Run leave-one-regime-out and action-shuffled null tests.
6. Write theory, runtime contract, promotion gate, results, validation, checksums, and ZIP.
