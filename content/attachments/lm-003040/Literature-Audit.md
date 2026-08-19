# GVSS-05 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources; conservative novelty language.

## 1. Closed-loop T2I correction

### Test-time Prompt Refinement for Text-to-Image Models
arXiv:2507.22076.

Uses an MLLM to inspect a generated image, diagnose prompt-image mismatch, refine the prompt, regenerate, and verify.

**GVSS relation:** direct RECOMPILE precedent. GVSS-05 asks when prompt recompilation is the correct failure layer rather than a universal default.

### Iterative Refinement Improves Compositional Image Generation
arXiv:2601.15286.

Uses a VLM critic to produce sequential corrections; reports gains over compute-matched parallel sampling on several compositional benchmarks.

**GVSS relation:** direct evidence that search policy can change practical visual success under the same broad model family.

### VisionDirector
arXiv:2512.19243, revised 2026.

Uses structured goals, multimodal verification, staged edits, confidence filtering, and rollback.

**GVSS relation:** strong operational overlap with verify-diagnose-refine runtime structure.

## 2. Failure-localized correction

### Agentic Retoucher
arXiv:2601.02046.

Perception-reasoning-action loop; context-aware localization of subtle distortions and targeted retouching.

**GVSS relation:** direct precedent for local failure diagnosis followed by layer-specific REPAIR.

### Agentic Flow Steering and Parallel Rollout Search
arXiv:2603.18627.

Treats T2I generation as sequential decision making; VLM critic diagnoses intermediate latent semantic deviations and guides parallel rollout/flow steering.

**GVSS relation:** strong precedent for search-policy diagnosis/control.

### AnchorSteer
arXiv:2607.26647.

Uses VLM diagnosis during denoising and targeted latent correction.

**GVSS relation:** direct current example of active mid-generation failure diagnosis.

## 3. Structured T2I evaluation

### SANEval
arXiv:2602.00249.

Open-vocabulary compositional evaluation with interpretable feedback for attributes, relations, numeracy, and object-level failures.

**GVSS relation:** demonstrates that structured failure reports can expose specific visual failure dimensions.

### DynEval
arXiv:2607.11199.

Dynamic/structured evaluator with fine-grained analysis over multiple semantic dimensions and many T2I models.

**GVSS relation:** supports multi-axis diagnosis rather than one scalar quality number.

## 4. Evaluator failure

### Seeing Isn't Believing
arXiv:2604.21523.

Evaluates VLM judges on perturbed multimodal outputs and reports substantial blind spots, including spatial/compositional and hallucination-related failures.

**GVSS relation:** strong current evidence for explicitly including evaluator failure state $F_E$.

### VLM Judges Can Rank but Cannot Score
arXiv:2604.25235.

Studies task-dependent calibration gaps in VLM-as-a-judge systems.

**GVSS relation:** ranking capability and calibrated score interpretation should be separated.

### DiagEval
arXiv:2605.17439.

Developed for GUI-agent evaluation, not T2I, but explicitly diagnoses evaluator-side errors versus genuine execution/environment failures.

**GVSS relation:** close methodological precedent for failure-source attribution in a closed-loop evaluator.

## 5. Seed-local versus systemic failure

### OmniPhys
arXiv:2607.25641.

Notes that high stochasticity can mislead prompt optimization through transient artifacts; aggregates multiple stochastic samples before meta-policy updates to filter seed/query-local noise.

**GVSS relation:** very close support for the sample-local/systemic-failure distinction.

## 6. Candidate GVSS contribution

Do not claim as inventions:

- Bayesian diagnosis;
- sequential testing;
- VLM critics;
- iterative refinement;
- evaluator calibration;
- value of information;
- POMDP diagnosis.

Potential GVSS-05 synthesis contribution:

1. seven-layer visual failure taxonomy tied directly to runtime action levels;
2. explicit seed-reroll stopping theorem under a lower-bound success hypothesis;
3. finite-failure/no-unreachability no-go;
4. alternate-policy success as a hard refutation of generator-boundary impossibility;
5. evaluator failure and intent ambiguity as first-class latent visual failure states;
6. diagnostic equivalence over failure hypotheses;
7. least-cost justified action and diagnostic regret as runtime metrics.

No strong novelty claim is made.
