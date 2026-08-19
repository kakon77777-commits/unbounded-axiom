# GVSS-06 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources; conservative novelty language.

## 1. State-aware agentic image control

### Generation Navigator
Jinming Liu et al., arXiv:2605.17969, 2026.

Reformulates image generation as a state-conditioned action-making problem. Its PRE-GRPO objective explicitly rewards peak quality, retention, and efficiency, penalizing unnecessary or degrading turns.

**GVSS relation:** very close current precedent for dynamic image-generation action selection. GVSS-06 adds an explicit hidden failure belief and information-acquisition/correction separation.

### GenAgent
Kaixun Jiang et al., arXiv:2601.18543, 2026.

Uses multimodal reasoning, image-generation tools, judgment, reflection, and multi-turn refinement; reports test-time scaling and cross-tool generalization.

**GVSS relation:** direct precedent for tool-using multi-turn visual generation control.

## 2. Human clarification / interaction

### Twin-Co
Jianhui Wang et al., arXiv:2504.14868, 2025/revised 2026.

Uses synchronized co-adaptive dialogue to progressively refine generated images and reduce user-prompt ambiguity.

**GVSS relation:** direct image-generation precedent for human clarification as part of the visual loop.

### Clarify or Answer
arXiv:2601.16400, 2026.

Defines an ask-or-answer decision problem for ambiguous visual contexts and learns ambiguity-resolving clarification behavior.

**GVSS relation:** direct multimodal precedent for clarification as an action selected according to uncertainty.

## 3. Sequential experimental design

### Active Visual Reasoning via Sequential Experimental Design
Anjie Liu et al., arXiv:2605.01345, 2026.

Formalizes task-relevant visual evidence acquisition as sequential Bayesian optimal experimental design.

**GVSS relation:** direct current precedent for deciding which visual information to acquire before acting.

## 4. Evaluator uncertainty and calibration

### VLM Judges Can Rank but Cannot Score
Kumar et al., arXiv:2604.25235, 2026.

Uses conformal prediction to quantify task-dependent uncertainty in multimodal judges and documents ranking/scoring decoupling.

**GVSS relation:** strong support for evaluator calibration/deferral as explicit control state.

### Calibrating MLLM-as-a-judge via Multimodal Bayesian Prompt Ensembles
Slyman et al., arXiv:2509.08777, 2025.

Studies multimodal-specific calibration for MLLM judges in TTI evaluation and reports improved human alignment/calibration.

**GVSS relation:** direct TTI evaluator-calibration precedent.

## 5. Active diagnosis / belief-action coupling

### On Information Self-Locking in Reinforcement Learning for Active Diagnosis
arXiv:2603.12109, 2026.

Analyzes coupling between action selection and belief tracking in active diagnosis and shows how weak belief/action policies can self-lock by failing to acquire informative observations.

**GVSS relation:** very close methodological precedent for GVSS diagnostic self-locking.

## 6. Novelty boundary

Do not claim as GVSS inventions:

- POMDP belief control;
- Bayesian dynamic programming;
- EVPI/value of information;
- Blackwell comparison;
- active diagnosis;
- sequential Bayesian experimental design;
- human clarification policies;
- agentic image-generation action selection;
- VLM calibration.

Potential GVSS-06 synthesis contribution:

1. using GVSS-05's seven-layer visual failure posterior as the belief state of an image-generation controller;
2. unifying diagnose/correct/clarify/stop actions;
3. explicit perfect-diagnostic and human-clarification cost thresholds for visual correction;
4. a visual-controller counterexample showing least-cost justified correction can be sequentially suboptimal;
5. posterior sensitivity bound for learned visual-diagnostic likelihoods;
6. finite-horizon diagnostic-control regret;
7. explicit diagnostic provenance fields for human/evaluator/action decisions.

No strong novelty claim is made in v0.1.
