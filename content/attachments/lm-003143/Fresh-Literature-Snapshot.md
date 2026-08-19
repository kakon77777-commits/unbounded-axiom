# Paper 02 — Fresh Literature Snapshot
Date: 2026-08-14
Scope: primary technical sources used for Series C / Paper 02.

## Positive / reliability-improving directions
- SelfCheckGPT — arXiv:2303.08896
- On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents — arXiv:2408.00989
- Rethinking the Reliability of Multi-agent System: A Perspective from Byzantine Fault Tolerance — arXiv:2511.10400
- AgentHallu — arXiv:2601.06818
- AgentAuditor — arXiv:2602.09341
- MAS-FIRE — arXiv:2602.19843
- MARCH — arXiv:2603.24579
- AgentLocate — arXiv:2607.07989

## Negative / failure / instability directions
- Why Do Multi-Agent LLM Systems Fail? — arXiv:2503.13657
- Collective Hallucination in Multi-Agent LLMs — arXiv:2606.07941
- The Consistency Illusion — arXiv:2606.08457
- Delayed Verification Destabilizes Multi-Agent LLM Belief — arXiv:2606.27409
- Emergence of Biased Consensus in Multi-Agent LLM Debates — arXiv:2608.02827

## Research reading
The literature supports neither "more agents => more truth" nor "multi-agent interaction is useless".
The current frontier is architecture- and regime-dependent:
- information isolation can reduce confirmation coupling;
- local auditing can outperform majority aggregation;
- failure attribution is itself a hard task;
- closed-loop topology can improve fault tolerance;
- correlated evidence, conformity and verification delay can produce collective failure.

Paper 02 therefore defines epistemic normalization as evidence-constrained, provenance-aware, fault-localizing state reduction rather than consensus maximization.
