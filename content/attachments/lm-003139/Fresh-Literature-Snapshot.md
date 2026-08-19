# Series C / Paper 03 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 03 fresh-search grounding；不得自動沿用為 Paper 04 的 fresh search。

## 1. Epistemic Gain, Aleatoric Cost
arXiv:2603.01221
- 以 Bayesian uncertainty decomposition 分析 multi-agent debate。
- 區分跨 agent disagreement 所代表的 epistemic potential，以及 reasoning instability 對應的 aleatoric cost。
- 實驗跨 homogeneous / heterogeneous configurations 與 7 個 base models。
- 對本篇意義：disagreement 不應自動被視為需要消除的 failure；它可能是 information-gain potential。

## 2. Every Response Counts / MATU
arXiv:2604.08708
- 將 multi-agent uncertainty 擴展到 agents × reasoning steps × sampling runs。
- 強調 tool use、multi-step reasoning、inter-agent communication 與 topology 引入 MAS-specific uncertainty。
- 對本篇意義：shared epistemic state 不能只由 final answers 建模。

## 3. Minority Sentinel
arXiv:2606.29270
- 指出 correlated LLM errors 破壞 majority-vote 所需的 independent-error intuition。
- 三個 heterogeneous LLM、六個 benchmarks 的 divergent cases 中，作者報告約四分之一由 minority 持有正確答案。
- 對本篇意義：vote count 不能直接成為 world-elimination criterion。

## 4. Higher-order Uncertainty via Imprecise Probabilities
arXiv:2603.10396
- 使用 probability intervals、credal sets、possibility measures 表示 higher-order uncertainty。
- 作者明確指出 credal sets 對 ensemble-of-LLMs 特別合適。
- 對本篇意義：可將 admissible-world set 再 lift 成其上的 credal set，區分 exact permission 與 graded permission。

## 5. The Consensus Trap
arXiv:2604.17139
- 研究 adversarial majorities 對 response-level majority aggregation 的破壞。
- 對本篇意義：共同答案不能取代 intermediate evidence / logic structure。

## 6. Position: UQ in LLMs is Just Unsupervised Clustering
arXiv:2605.19220
- Position paper；批評大量 UQ 方法更接近 internal consistency measurement，而非 external correctness。
- 對本篇意義：admissible-world construction 必須清楚區分 internally admissible 與 externally grounded admissible。

## 7. ConU
arXiv:2407.00499
- 使用 conformal uncertainty 建構具有 correctness coverage control 的 prediction sets。
- 對本篇意義：set-valued uncertainty 與 calibrated coverage 是相鄰技術路線，但 prediction set 不等於本文的 possible-world set。

## Paper 03 定位

本篇不宣稱發明 possible-world semantics、credal uncertainty 或 set-valued prediction。
本篇的主要組合貢獻是將：
- observer-network normalization；
- admissible world contraction；
- four-valued permission status；
- gauge-equivalence；
- credal lifting；
- minority preservation；
統一成一個 AI shared-cognition runtime theory。
