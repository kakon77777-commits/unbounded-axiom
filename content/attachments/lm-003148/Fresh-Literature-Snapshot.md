# Series C / Paper 06 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 06 fresh-search grounding；不得自動沿用為 Paper 07 的 fresh search。

## 1. When Agents Look the Same
arXiv:2604.21255 — ACL 2026 Main Conference
- 18 models、8 providers。
- 提出 Response Pattern Similarity 與 Action Graph Similarity。
- 明確區分 task-success 所需 mandatory behavior 與 non-mandatory behavioral patterns。
- within-family model pairs 的 AGS 比 cross-family 高 5.9 percentage points。
- controlled distillation experiment 可區分 teacher-specific convergence 與 general improvement。
- 對本篇意義：跨模型 tool-use convergence 可測量，但 lineage / distillation 是重要 confound。

## 2. Trace
arXiv:2605.01186
- 7 frontier model families、3 distinct agent scaffolds。
- 由 terminal command sequences fingerprint model family。
- seen-scaffold macro F1 = 0.981。
- generalization to unseen scaffolds macro F1 = 0.815。
- black-box proprietary scaffold proof-of-concept attribution accuracy 約 78%。
- 對本篇意義：共同工作環境不會必然抹除 model-specific behavioral residue。

## 3. EnvTrustBench
arXiv:2605.08828
- 6 LLM backbones、5 widely used scaffolds。
- 55 generated cases、11 task scenarios。
- 記錄 action-observation trajectory 並以 validation oracle 判定。
- environmental grounding defects 跨 operational workflows 出現。
- 對本篇意義：agent behavior / reliability 是 model × scaffold × environment 的系統問題。

## 4. Communication Enables Cooperation in LLM Agents
arXiv:2510.05748v3
- heterogeneous 4-model Stag Hunt setting。
- 加入 one-word communication channel 後 cooperation 由 0% 升至 96.7%。
- same-family coalition 在無 communication 時已有 52.2% coordination，加入 communication 後 100%。
- 對本篇意義：communication protocol 本身可以造成強 behavioral convergence；不能把所有收斂歸因模型本體。

## 5. Institutional AI
arXiv:2601.11369v2
- 6 model configurations：3 homogeneous + 3 heterogeneous cross-provider pairs。
- 90 runs / condition。
- external governance graph + runtime enforcement 使 mean collusion tier 由 3.1 降至 1.8，severe collusion incidence 由 50% 降至 5.6%。
- prompt-only constitutional prohibition 沒有 reliable improvement。
- 對本篇意義：institution / incentive / runtime environment 可跨 model configurations 強烈塑造 collective behavior。

## 6. Semantic Consensus
arXiv:2604.16339
- 把 multi-agent failure 中的 shared-objective interpretation mismatch 定義為 Semantic Intent Divergence。
- process-aware middleware 將 shared operational context、conflict detection、drift monitoring 與 governance 分開。
- 對本篇意義：agent 行為比較若缺少 process / context control，容易把 semantic-environment divergence 誤認為模型差異。

## Paper 06 定位

本篇不以 anecdotal cross-model similarity 作為定理。
本篇的主要貢獻是建立五因素競爭模型：

$$
H_U,\ H_M,\ H_H,\ H_T,\ H_A
$$

並要求：
- mandatory-core residualization；
- crossed model–harness design；
- silent meta-observer；
- epistemic vs residual subspace separation；
- unseen verification-rich environment portability。

只有 portable convergence 成立，才增加 intelligence-level epistemic attractor 的可信度。
