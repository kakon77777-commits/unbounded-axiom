# Series C / Paper 08 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 08 fresh-search grounding；不得自動沿用為 Paper 09 的 fresh search。

## 1. AgencyBench
arXiv:2601.11044
- 6 core agentic capabilities。
- 32 real-world scenarios、138 tasks。
- tasks 平均約 90 tool calls、1M-token contexts、hours of execution。
- closed-source models 顯著優於 open-source models，且 resource efficiency、feedback-driven self-correction、tool-use preference 有差異。
- native scaffolds / ecosystems 也影響 performance。
- 對本篇意義：autonomous generality 必須在長程、多工具、多能力環境測量，而不是單一 QA。

## 2. CUBE
arXiv:2603.15798
- 嘗試統一 agent benchmarks 的 actions / observations / tasks / interfaces。
- 核心動機之一：proper tools + consistent interface 下 generalist agent 應能跨 benchmark family 工作。
- 對本篇意義：cross-benchmark portability 可作為 generality 的 operational proxy。

## 3. AgentVista
arXiv:2602.23166
- generalist multimodal agent benchmark。
- 25 sub-domains、7 categories。
- 對本篇意義：generality 應包含 modality / interaction breadth，而非只算文字知識。

## 4. AgentSkiller
arXiv:2602.09372
- 自動合成 semantically linked cross-domain interaction data。
- DAG state transitions、service blueprints、domain policies、cross-domain fusion。
- 約 11K synthesized interaction samples。
- 對本篇意義：generalist agent capability 已被明確作為 cross-domain tool-use / state-transition training 問題。

## 5. Agents-A1
arXiv:2606.30616
- 35B MoE agent。
- 以 long-horizon trajectories + heterogeneous agent abilities scaling。
- trajectories 平均約 45K tokens。
- 六個 heterogeneous domains 透過 multi-teacher distillation 統一到一個 deployable model。
- 對本篇意義：agent frontier 不只 parameter scale，也包括 horizon / domain composition。

## 6. HORIZON
arXiv:2604.11978
- 3100+ trajectories。
- 多 model families、四個 agentic domains。
- 專門分析 horizon-dependent degradation。
- 對本篇意義：long-horizon persistence 是獨立能力，不可由短程 benchmark 外推。

## 7. Long-Horizon-Terminal-Bench
arXiv:2607.08964
- 強調現有 terminal benchmarks 太短、只看 final outcome。
- 引入更長程、intermediate progress-aware 評估。
- 對本篇意義：PGAI 的 H 維需要 trajectory-level measurement。

## 8. METR Time Horizons
METR, 2026
- 以 human-expert task duration 對 frontier agent success probability 做 logistic fit。
- T50 / T80 是 task-completion horizon，不是 wall-clock autonomy 或 AGI 指標。
- 對本篇意義：horizon 可以獨立於 breadth / accuracy 測量。

## 9. OpenAI — How agents are transforming work
2026-06-25
- Codex usage 越來越多落在較長 human-work estimates。
- 知識工作用途從 coding 延伸至 reports、spreadsheets、presentations、contracts、research、analysis、automation。
- 對本篇意義：部署單位正在由短互動轉向 longer autonomous work units。
- 不可解讀為 AGI。

## 10. Codex app
OpenAI, 2026
- command center for multiple agents、parallel workflows、long-running tasks。
- 對本篇意義：system orchestration / oversight 正成為 agent product 的一級結構。

## 11. AlphaEvolve impact
Google DeepMind, 2026
- LLM ensemble + automated evaluators。
- open problems in mathematics / CS + deployed infrastructure optimization。
- unattended candidate generation / evaluation loop。
- 對本篇意義：高 verification-density domain 已出現很強的專域自主閉環。

## 12. Co-Scientist
Google DeepMind, 2026
- multi-agent research partner。
- hypothesis generation、critique、ranking、evolution。
- 對本篇意義：general functional capability 可以由 epistemic division of labor 與 coordination 產生。

## 13. Emergence World
arXiv:2606.08367
- continuously running multi-agent simulation。
- 120+ tools、3 persistent memory systems、live external data、governance mechanisms。
- model-agnostic、heterogeneous populations。
- 示範 15-day cross-vendor experiment。
- 對本篇意義：long-duration multi-agent autonomy 已開始成為可記錄、可重放的研究對象。

## 14. Validation Bottleneck
Google DeepMind public policy, 2026
- 指出 AI agents 能快速擴張 conjecture / candidate space，validation 成為新的瓶頸。
- 對本篇意義：verification capacity 是 general autonomous intelligence 的核心資源，不只是 safety 附屬。

## Paper 08 定位

本文不定義 AGI，也不宣稱 AGI 已來臨。

本文定義較弱的 PGAI system：

$$
\mathfrak G
=
(
\mathcal M,
\mathcal A,
\mathcal T,
\mathcal K,
\mathcal V,
\mathcal H,
\mathcal O,
\mathcal R,
\mathcal B
)
$$

並以：

$$
\mathbf P
=
(
G,T,C,H,V,M,O,B
)
$$

分離：
- generality；
- transfer；
- closure；
- horizon；
- verification；
- memory；
- organization；
- governance。

「AGI 前夜」在本文中是技術 regime，不是日期預言。
