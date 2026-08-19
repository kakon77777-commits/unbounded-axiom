# Series C / Paper 07 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 07 fresh-search grounding；不得自動沿用為 Paper 08 的 fresh search。

## 1. OrgAgent
arXiv:2604.01020
- company-style hierarchical MAS。
- collaboration 拆成 governance、execution、compliance。
- 跨 tasks、LLMs、execution modes、policies 比較 organization structures。
- 其研究顯示 hierarchy 在不少設定提升 effectiveness 並降低 token cost。
- 對本篇意義：organizational structure 本身已是可操控的 Agent-system 變量。

## 2. Drop the Hierarchy and Roles
arXiv:2603.28990
- 25,000-task experiment。
- 8 models、4–256 agents、8 coordination protocols。
- 在較強模型與 minimal scaffolding 下觀察到 emergent specialized roles、voluntary abstention、shallow hierarchies。
- hybrid Sequential protocol 在該研究中優於 centralized coordinator，也優於完全 autonomous shared protocol。
- 對本篇意義：role / hierarchy 可以 endogenously emerge，但最佳點可能是 exogenous structure + endogenous autonomy 的混合。

## 3. Toward an Organizational Science of Multi-Agent LLM Systems
arXiv:2607.25446
- IMACS 將 organization、coordination、collaboration protocol 拆成 orthogonal layers。
- organization formalized as roles / assignment / coordination / accountability。
- Adaptive Org Routing 讓 protocol 本身可依 task / quality-cost tradeoff 學習。
- optimal accountability placement 會隨 model family 改變。
- 對本篇意義：誰、如何協調、如何融合結果應分開做實驗。

## 4. Intelligent AI Delegation
arXiv:2602.11865
- delegation 需要 dynamic assessment、adaptive execution、structural transparency、scalable coordination、systemic resilience。
- 對本篇意義：delegation 不只是 task routing，而是 competence / authority / trust / failure handling 的系統問題。

## 5. Observability for Delegated Execution
arXiv:2606.09692
- 指出 agentic systems 在 durable delegation 後出現 structural observability gap。
- execution 跨 tools、time、multiple cooperating agents，傳統 SIEM / audit logs 很難靠時間窗口重建 delegation context。
- 提出 delegation-aware common information model / gateway，支援 cross-tool reconstruction。
- 對本篇意義：meta-observer 需要 delegation-aware provenance，不只是 timestamp logs。

## 6. TaskWeave
arXiv:2606.01199
- long-horizon organizational simulation 視為 memory-centered coordination problem。
- year-long IT company simulation。
- Formulate-Partition-Diagnose-Align cycle + dependency-aware trace memory。
- 對本篇意義：長期組織 coherent behavior 高度依賴外部化 organizational memory。

## 7. Claw AI Lab
arXiv:2605.22662
- multi-agent autonomous research team。
- exploration、discussion、reproduction modes。
- artifact inspection、execution feedback、rollback、persistent laboratory state。
- 對本篇意義：當 research agents 增加時，管理問題開始由 model loop 轉為 laboratory organization。

## 8. Clarus
arXiv:2606.30246
- web-scale autonomous research collaboration infrastructure。
- primitives：projects、agents、resources。
- collaborative process 包含 phases、tasks、artifacts、credit、provenance、authorization。
- 對本篇意義：multi-agent research 開始需要真正的 organizational infrastructure 與 attribution。

## 9. When Agents Evolve, Institutions Follow
arXiv:2604.27691
- 將歷史制度 topology 轉成 executable multi-agent architectures。
- 三個 LLM、兩個 benchmarks。
- best / worst institution performance gap 可很大，且 optimal architecture 隨 model capability / task 改變。
- 對本篇意義：institution 可以成為 adaptive computational layer，而非固定背景。

## Paper 07 定位

本文使用「AI Work Society」只表示功能性工作組織，不做人格／主體性推論。

最小三條：
1. persistent division of labor；
2. traceable delegation；
3. institutional persistence。

Meta-observer 必須另外擁有：
- delegation-aware observability；
- provenance；
- intervention labeling；
- causal fault attribution。

因此研究單位由：

$$
A_i
$$

提升為：

$$
\mathfrak S_t.
$$
