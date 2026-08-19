# Series C / Paper 10 — Fresh Literature Snapshot
日期：2026-08-14
用途：Paper 10 final fresh-search grounding。

## 1. Lean
Official Lean sources
- proof assistant + programming language。
- kernel / proof-checking substrate 可將已 formalized claim 轉成可機器重放的檢查問題。
- 對本篇意義：formal world 提供高 replayability、explicit semantics 與低 marginal verification cost，但仍存在 formalization / specification boundary。

## 2. AlphaEvolve
Google DeepMind
- proposed programs 由 automated evaluation metrics verify、run、score。
- 官方明確指出特別適用於可清楚、系統性測量 progress 的 math / CS domains。
- 對本篇意義：candidate generation 的可擴張性高度依賴 dense evaluator。

## 3. AI agents and the new validation bottleneck in science
Google DeepMind, 2026
- agent 可高速產生 candidate / conjecture，validation 成為新的 bottleneck。
- 對本篇意義：future AI-for-science frontier 不只需要 proposer，也需要 validator infrastructure。

## 4. AHOIS
arXiv:2606.26722
- real multimode-fibre optical platform。
- physics critic 進行 causal questioning、constraint checking、counterexample、falsification criteria。
- evidence 直接回寫 hypothesis / experimental plan。
- 對本篇意義：physical external grounding 已開始成為真正 Agent loop 的一部分。

## 5. Qiushi Discovery Engine
arXiv:2604.27092
- end-to-end autonomous scientific discovery on a real optical platform。
- long-horizon measurement / revision actions、Meta-Trace memory。
- open-ended study：145.9M tokens、3242 LLM calls、1242 tool calls、163 notes、44 scripts。
- 對本篇意義：physical world 可以進入 long-horizon research closure，但成本／latency 遠高於 pure code execution。

## 6. Lab Agent Protocol
arXiv:2606.03755
- instrument edge 與普通 tool edge 不同：stateful、exclusive、safety critical、physical。
- MeasurementResult 必須包含 physical units、calibrationRef、measurement uncertainty、provenance、instrument signature。
- reservation / sample locking / safety-fence handshake。
- 對本篇意義：physical verification 本身需要 infrastructure，不是「tool call -> number」。

## 7. Agentic Self-Driving Lab
arXiv:2607.04508
- 把物理 experiment rounds 與單次 experiment cost 視為瓶頸。
- 對本篇意義：physical VID 直接受 experiment cost / latency 約束。

## 8. AIMS
arXiv:2607.16544
- uncertainty-aware closed-loop experimentalist。
- uncertainty 被轉成 navigation / measurement selection / mechanism-attribution action。
- 對本篇意義：physical verification 可以由「事後 checking」提升成 active measurement policy。

## 9. Autonomous Quantum Sensing Experiments
arXiv:2607.25145
- persistent project records + quantitative tools + deterministic hardware control。
- autonomous NV-center experiment。
- expected-signal calculation 可降低 false positive resonance judgments。
- 對本篇意義：Agent scientific hypothesis layer 與 deterministic hardware/safety layer 的分工是 physical-world trust architecture。

## 10. PhySciBench
arXiv:2606.18648
- strongest general-purpose baseline 約 33.5%。
- failure：long-horizon reasoning、cross-step transfer、physics-grounded verification。
- 對本篇意義：physical-science conclusion formation 的 verification burden 顯著。

## 11. SpatialBench-Long
arXiv:2605.28065
- 24 long-horizon evaluations，raw / near-raw biological measurements。
- candidate claims 經 reproduction、independent scientist review、trajectory inspection hardening。
- 最佳 model-harness combinations 8/72 runs = 11.1%。
- 對本篇意義：complex scientific evidence interpretation 遠難於只執行 procedure。

## 12. Embodied Science
arXiv:2603.19782
- PLAD：Perception-Language-Action-Discovery。
- physical execution 與 experimental feedback 被視為真正 discovery loop 的必要部分。
- 對本篇意義：autonomy 向物理世界外推需要 embodied verifier。

## 13. Agentic World Modeling
arXiv:2604.22748
- scientific / physical regime 中強調 surrogate-to-reality gap。
- 對本篇意義：simulation verification 與 world verification 必須分離。

## 14. Toward Trustworthy Autonomous Science
arXiv:2607.12113
- closed discovery loop + self-driving labs / instruments。
- 將 trust/verification 與 safety/security/governance 拉成第一級層次。
- 對本篇意義：physical autonomy 的 verifier 與 governance 必須同步擴張。

## 15. Autonomous Research Agents / Verification Gap
arXiv:2608.05179
- autonomous research systems 的生成能力已超前於 trace / seed / novelty verification 等可審核性。
- 對本篇意義：verification infrastructure 是 research autonomy 的獨立 frontier。

## Paper 10 定位

本文提出 task-relative Verification Information Density：

$$
\nu(q;\mathcal E)
=
\sup_S
\frac{
D R G J T
}{
1+C+\lambda L
}.
$$

五個 worlds：
- formal；
- computational；
- simulated；
- instrumented physical；
- open world。

它們不是 universal ranking，而是 verification regime map。

Series C final claim：

$$
\text{autonomous-intelligence frontier}
$$

部分等價於：

$$
\text{the frontier of how densely the environment can return
reliable corrective evidence}.
$$
