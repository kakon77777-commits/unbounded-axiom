# VWDC-06 Literature Audit

**Date:** 2026-08-17  
**Policy:** Primary research sources only; conservative novelty language.

## 1. Adaptive Sim2Real policy transfer

### Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment
Han and Feng, arXiv:2605.27659, 2026.

Formulates varying deployment contexts as a family of constrained MDPs, infers latent environment context, and dynamically adjusts policy risk according to context-estimation accuracy.

**VWDC relation:** direct current precedent for deployment risk/adaptation changing with uncertainty about the target reality context.

## 2. Real-Sim-Real loops

### An Real-Sim-Real Loop Framework for Generalizable Robotic Policy Transfer with Differentiable Simulation
Shi et al., arXiv:2503.10118, 2025.

Iteratively uses real-world data to refine differentiable simulation parameters and support policy transfer, with data collection designed to improve representativeness/informativeness.

**VWDC relation:** direct precedent for the closed World/Simulation -> Reality -> Model/Policy update loop.

## 3. Uncertainty-aware safe transfer

### Safe Domain Randomization via Uncertainty-Aware Out-of-Distribution Detection and Policy Adaptation
Danesh et al., arXiv:2507.06111, 2025.

Uses uncertainty-aware OOD detection and progressive randomization/adaptation to improve robust deployment under unseen dynamics.

**VWDC relation:** direct precedent for treating unsupported/high-uncertainty regions differently from ordinary deployment regions.

### Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning More Powerful
Tang et al., arXiv:2504.16680, revised 2026.

Uses epistemic uncertainty in world-model rollouts and policy optimization to reduce reliance on uncertain imagined trajectories.

**VWDC relation:** direct precedent for pessimistic/uncertainty-aware policy control under model error.

## 4. Safe continual adaptation

### Safe Continual Domain Adaptation after Sim2Real Transfer of Reinforcement Learning Policies in Robotics
Josifovski et al., arXiv:2503.10949, 2025.

Adapts policies after real-world deployment as environment dynamics change while reducing safety risk and avoiding forgetting of the domain-randomized base policy.

**VWDC relation:** current precedent for deployment-time feedback and policy adaptation under changing target dynamics.

### SafeAdapt
Anisimov, Belardinelli, Wicker, arXiv:2604.09452, 2026.

Studies policy updates that preserve certified safety properties on previously encountered task distributions.

**VWDC relation:** important boundary: transport/external-validity certificates and formal safety certificates are distinct contracts.

## 5. Robust/provable transfer

### Provable Sim-to-Real Transfer via Offline Domain Randomization
arXiv:2506.10133, 2025.

Fits simulator-parameter distributions using offline target-domain data and studies policy-transfer guarantees.

**VWDC relation:** direct neighboring work for using limited real data to build transfer-relevant simulator uncertainty rather than assuming one simulator is exact.

## 6. Deployment distribution shift

### The Sim-to-Real Gap of Foundation Model Agents
arXiv:2606.07017, 2026.

Frames deployment as exposing agents to distribution shifts, noisy inputs, execution constraints, and stochastic transitions absent from clean benchmarks.

**VWDC relation:** supports the broad warning that benchmark/simulation optimality is not deployment reliability.

### Can Context Bridge the Reality Gap?
arXiv:2511.04249, revised 2026.

Studies context-conditioned policy adaptation to deployment dynamics rather than relying exclusively on broad robustness.

**VWDC relation:** direct precedent for state/context-dependent deployment adaptation.

## 7. Classical mathematical provenance

The following are classical and not VWDC inventions:

- robust lower-bound action selection;
- simulation lemmas/value-difference bounds for MDPs;
- total-variation expectation bounds;
- value of perfect information;
- Hoeffding concentration;
- robust MDP/RL;
- constrained/safe RL;
- Pareto necessity.

## 8. Candidate VWDC synthesis

Potential bridge-specific synthesis:

1. RTC action-value intervals as explicit world-to-reality deployment certificates;
2. transport error converted into action/policy reality-regret bounds;
3. unsupported RTC regions as first-class deploy/probe/fallback/human gates;
4. policy-induced occupancy shift as endogenous loss of RTC certification;
5. versioned policy–RTC deployment pairs;
6. explicit separation of reward-transport and safety-transport contracts;
7. multi-contract action gating with authority and fallback semantics.

No strong novelty claim is made.
