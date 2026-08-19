# GVSS-10 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources; conservative novelty language.

## 1. T2I routing

### Cost-Aware Routing for Efficient Text-To-Image Generation
Li et al., arXiv:2506.14753, 2025.

Learns prompt-conditioned routing among multiple pre-trained T2I generation functions/models, balancing quality and computational cost.

**GVSS relation:** direct precedent for task-conditioned provider routing.

### Edge-Cloud Routing for Text-to-Image Model with Token-Level Multi-Metric Prediction
Xin et al., arXiv:2411.13787, 2024.

Routes prompts between lightweight edge and large cloud T2I models using token-level multi-metric quality prediction and cost constraints.

**GVSS relation:** direct precedent for multi-metric task-conditioned routing.

### HADIS
Yang et al., arXiv:2509.00642, 2025.

Jointly optimizes cascade-model configuration, prompt routing, and resource allocation for diffusion serving.

**GVSS relation:** direct precedent for routing under latency/resource constraints.

### OctoT2I
Jiang et al., arXiv:2606.01803, 2026.

Stateful multi-round routing across T2I tools; self-evolving capability knowledge base built through Propose-Solve-Evaluate-Learn exploration.

**GVSS relation:** especially close precedent for online capability learning and routing.

## 2. Off-policy evaluation / routing-selection bias

### Doubly Robust Policy Evaluation and Learning
Dudík, Langford, Li, arXiv:1103.4601.

Develops doubly robust policy evaluation/learning for contextual bandits when only selected-action reward is observed.

**GVSS relation:** classical machinery for provider capability/routing evaluation under historical selection bias.

### Optimal and Adaptive Off-policy Evaluation in Contextual Bandits
Wang, Agarwal, Dudík, arXiv:1612.01205.

Studies minimax limits and IPS/DR/SWITCH-style off-policy evaluation.

**GVSS relation:** supports the claim that provider-routing logs require explicit off-policy treatment.

### Cross-Domain Off-Policy Evaluation and Learning for Contextual Bandits
Natsubori, Ushiku, Saito, arXiv:2607.22012, 2026.

Targets few-shot, deterministic logging, and new-action settings by borrowing source-domain logs.

**GVSS relation:** current neighboring direction for provider cold-start and support-limited routing.

## 3. Contribution attribution

### Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems
Jiang, Zhu, Zhu, arXiv:2607.18255, 2026.

Studies contribution attribution in ordered multi-agent workflows and connects a semantic attribution value to classical Shapley value under special conditions.

**GVSS relation:** relevant modern precedent for attribution after multi-stage provider workflows.

## 4. Novelty boundary

Do not claim as GVSS inventions:

- contextual bandits;
- exploration/exploitation;
- IPS;
- doubly robust estimation;
- off-policy evaluation;
- support/positivity;
- model routing;
- T2I routing;
- Shapley attribution;
- cold-start exploration.

Potential GVSS-10 synthesis contribution:

1. task-conditioned provider capability as a visual-routing object linked to GVSS provider reachable regions;
2. routing-selection-bias governance and mandatory propensity provenance for visual providers;
3. provider-starvation/cold-start as capability non-identifiability;
4. capability-estimation error translated directly into visual routing regret;
5. fallback value conditioned on prior provider failure/common-mode structure;
6. path-level visual capability separated from provider-stage causal contribution;
7. capability/version drift integrated into provider routing model maintenance.

No strong novelty claim is made in v0.1.
