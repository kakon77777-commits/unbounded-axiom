# Series C / Paper 05 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 05 fresh-search grounding；不得自動沿用為 Paper 06 的 fresh search。

## 1. The AI Scientist-v2
arXiv:2504.08066
- end-to-end agentic system。
- 迭代 formulate hypotheses、design/execute experiments、analyze/visualize data、author manuscript。
- 三篇 fully autonomous manuscripts 送入 ICLR workshop；其中一篇超過平均 human acceptance threshold。
- 對本篇意義：end-to-end research automation 已是實作問題，不再只是概念。

## 2. Arbor / Hypothesis-Tree Refinement
arXiv:2606.11926
- long-lived coordinator + short-lived executors。
- persistent tree 連接 hypotheses、artifacts、evidence、distilled insights。
- 研究 long-horizon autonomous research，讓 evidence 與策略跨時間累積。
- 對本篇意義：persistent externalized research state 是長期閉環的重要結構。

## 3. Claw AI Lab
arXiv:2605.22662
- 將 autonomous research 從 black-box paper generation 重構為 interactive AI laboratory。
- idea、planning、coding、experimentation、writing layers 之間存在 validation loops 與 feedback。
- dashboard 支援 event streams、artifact inspection、rollback、multi-project monitoring。
- 對本篇意義：auditability、rollback、persistent laboratory state 是可部署自主研究的重要條件。

## 4. ResearchGym
arXiv:2602.15112
- 5 個 containerized real-world research environments、39 subtasks。
- controlled GPT-5 agent evaluation 顯示 capability–reliability gap。
- agent 在 15 次 evaluation 中僅 1 次改善 baseline；平均完成 26.5% subtasks。
- Claude Code / Codex scaffolds 也顯示類似 gap。
- failure modes：impatience、resource management、weak-hypothesis overconfidence、parallel coordination、context length。
- 對本篇意義：closed-loop access 不等於 closed-loop competence。

## 5. AHOIS / Socratic Agents
arXiv:2606.26722
- 明確區分 procedural workflows 與 epistemic autonomy。
- multi-agent AI scientist 在真實 multimode-fibre optical platform 上 closed-loop experiment。
- physics critic 做 causal questioning、constraint checking、counterexample generation、falsification criteria。
- 對本篇意義：外部 physical evidence 真正回寫 explanation / hypothesis，是比純 computational pipeline 更強的 closure。

## 6. Verification Gap Survey
arXiv:2608.05179
- 研究 autonomous research agents 的 auditability / verification gap。
- corpus 中 runnable systems 的 code release 比 seeds / execution traces / novelty verification 普遍。
- 核心問題已從「agent 能否做 research tasks」轉向「其 claims 是否可被 reviewers 驗證」。
- 對本篇意義：verification throughput 必須成為 autonomous research capacity 的一等狀態變數。

## 7. Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery
arXiv:2605.08956
- position paper。
- 批評 problem selection、tacit/failure knowledge、diversity compression、benchmark 與 physical feedback 缺口。
- 強調真正 natural-science autonomy 需要與 experiment / nature 閉環。
- 對本篇意義：避免把固定 benchmark optimization 與 manuscript generation 直接升格為 general autonomous science。

## 8. OpenAI — Run Long Horizon Tasks with Codex
2026-02-23
- 公開流程：plan → edit → tools → observe → repair → update status → repeat。
- 強調 durable project memory、milestones、acceptance criteria、continuous verification、audit log。
- 25-hour demo 是 experiment，不是 production guarantee。
- 對本篇意義：長程 Agent 工作依賴 harness、memory 與 feedback，而非單一大 prompt。

## 9. AlphaEvolve
Google DeepMind, 2025
- candidate programs 由 automated evaluators verify、run、score。
- 對本篇意義：高 verification-density domain 最容易形成可量化 autonomous improvement loop。

## Paper 05 定位

本文不把「全自動跑完 research pipeline」定義為自主研究。
本文要求最低 evidence-sensitive edge：

$$
E_t
\rightarrow
B_{t+1}
\rightarrow
\Pi_{t+1}.
$$

若 evidence 不改變 future research policy，即使沒有任何人介入，仍屬 epistemically open-loop automation。
