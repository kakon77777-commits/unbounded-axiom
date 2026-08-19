# 外部定位參考資料

檢索日期：2026-08-13。

1. Reijo Jaakkola, Antti Kuusisto, “First-order logic with self-reference,” arXiv:2207.07397.
   https://arxiv.org/abs/2207.07397
   - 以 recursion operator 讓 formulas refer to themselves；不同 semantics、自然演繹與 decision problems。
   - 用途：self-reference 必須有明確 syntax/semantics，而不是把一般 meta-query 直接等同 self-reference。

2. Ivano Ciardelli, “Inquisitive Neighborhood Logic,” arXiv:2411.04031.
   https://arxiv.org/abs/2411.04031
   - conditional/modal operators 可作用於 statements 與 questions。
   - 用途：questions 本身可作為 modal/semantic operator 的正式 operand。

3. Ivano Ciardelli, Martin Otto, “Bisimulation in Inquisitive Modal Logic,” arXiv:1707.08742.
   https://arxiv.org/abs/1707.08742
   - epistemic inquisitive modal logic 不只描述 agents 擁有的 information，也描述其 interested questions。
   - 用途：agent-relative question states 的外部形式接口。

4. Philipp Koralus, “The Erotetic Theory of Attention: Questions, Focus and Distraction,” Mind & Language 29(1), 2014.
   DOI: 10.1111/mila.12040
   - questions encode task completion conditions；attention 與對 answers 的 sensitivity 相關。
   - 用途：active query / attention-control 的相鄰理論背景。

5. Matthew Renze, Erhan Guven, “Self-Reflection in LLM Agents: Effects on Problem-Solving Performance,” arXiv:2405.06682.
   https://arxiv.org/abs/2405.06682
   - LLM agent self-reflection 的實驗研究。
   - 用途：工程上的 reflection-like behavior，不作形式 self-reference 證據。

6. “Uncertainty of Thoughts: Uncertainty-Aware Planning,” arXiv:2402.03271.
   https://arxiv.org/abs/2402.03271
   - LLM 生成 candidate questions，模擬 possible futures，依 uncertainty-based reward 選擇下一問。
   - 用途：Speculative Question Expansion 的工程鄰近例。

## 邊界

本文的：
- \(X^O/X^Q\) typed separation；
- Query-as-Object Lift；
- Meta-Query Depth；
- Question Frontier；
- Self-Reference Barrier；
- Heterogeneous-Observer Meta-Query Runtime；
- Convergent Re-linking；
皆為本系列自行提出的工作定義。
