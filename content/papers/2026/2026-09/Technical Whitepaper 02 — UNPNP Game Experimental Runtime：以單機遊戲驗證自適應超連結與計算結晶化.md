# Technical Whitepaper 02
## UNPNP Game Experimental Runtime：以單機遊戲驗證自適應超連結與計算結晶化
### A Single-Player Game Runtime for Validating Adaptive Hyperlinks, Path Compilation, and Computational Crystallization

**系列：** UNPNP / Crystallized Computation Technical Whitepapers  
**白皮書編號：** TW-02  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** 技術白皮書／研究 Runtime／單機遊戲實驗／AI 再編譯前置驗證  
**狀態：** Canonical Draft  

---

## 摘要

UNPNP 理論系列提出：AI-native runtime 不應只在固定計算圖中反覆求解，而應能在運行過程中觀察高成本路徑、發現自適應快速通道、重新編譯穩定 traversal，並把已驗證的新路徑結晶為可重用計算原語。若此機制成立，則在穩定或部分穩定的工作負載中，系統的未來計算成本應隨經驗累積而下降。

本文提出 **UNPNP Game Experimental Runtime，UGER**，作為第一個工程驗證環境。選擇單機遊戲的理由不是「遊戲比較容易」，而是它同時具備複雜狀態、可重播、可回滾、可量測、低外部風險與大量重複語義路徑，因此能在不引入真實外部副作用的情況下，測試 UNPNP 最核心的可證偽命題。

UGER 的核心比較為：

$$
\boxed{
\text{Baseline A}
\quad
\text{vs.}
\quad
\text{Baseline B}
\quad
\text{vs.}
\quad
\text{Experimental C}
}
$$

其中：

- Baseline A：傳統／naive runtime，不使用 persistent corridor；
- Baseline B：允許自適應 reasoning 與 routing，但不形成持久化 crystal；
- Experimental C：完整啟用 Adaptive Corridor Generator、EHPE、Path Compilation、Crystallization、Fast / Slow Path 與 Invalidation。

為了隔離模型能力與架構能力，本文強制加入 **Frozen-Model Experiment**：

$$
\boxed{
\theta_{t+1}
=
\theta_t
}
$$

即模型權重固定，只允許外部結構演化：

$$
\mathcal K_{t+1}
\neq
\mathcal K_t.
$$

如果在同一模型、同一遊戲版本、同一硬體、同一初始狀態與同一隨機 seed 下，Experimental C 能逐步達到：

$$
R_{\mathrm{reason}}(t)\downarrow,
$$

$$
H_{\mathrm{corridor}}(t)\uparrow,
$$

$$
R_K(t)\uparrow,
$$

$$
C_{\mathrm{avg}}(t)\downarrow,
$$

且：

$$
F_R(t)
$$

不顯著惡化，則可提供直接證據支持「World-to-Corridor Compilation」與「Crystallized Computational Adaptation」確實具有獨立工程價值。

本文定義 UGER 的最小 runtime 模組：

```text
Game Adapter
State Observer
Event Normalizer
Transition Logger
Semantic Revealing Layer
Adaptive Corridor Generator
EHPE Gate
Path Compiler
Crystal Store
Fast / Slow Path Router
Validator
Safety Envelope
Cost Ledger
Replay Harness
Experiment Controller
```

並定義主要資料結構：

- `WorldSnapshot`
- `TransitionEvent`
- `PathTrace`
- `CorridorCandidate`
- `CompiledPath`
- `ComputationalCrystal`
- `ExperimentReceipt`
- `CostRecord`

UGER 採取五階研究路線：

$$
\boxed{
P_0
\rightarrow
P_1
\rightarrow
P_2
\rightarrow
P_3
\rightarrow
P_4
}
$$

分別為：

1. Synthetic World；
2. Turn-Based Game；
3. Simulation / Management Game；
4. Real-Time Single-Player Game；
5. Controlled Legacy Program Interface。

其中 Phase 4 不是直接修改 production software，而是把已驗證的 runtime 機制轉入受控 legacy program，使用 shadow recompilation 與 selective crystal overlay，作為未來一般程式 AI 再編譯技術的前置接口。

本文明確規定：第一代 UGER 不處理多人遊戲、真實外部寫入、付款、帳號權限、production mutation 或不可逆外部作用域。安全 envelope 預設限制於：

$$
R_0,R_1,R_2,
$$

即 pure read、local reversible write 與 sandbox execution。

本文最後定義最重要的總驗證條件：

$$
\boxed{
C_{\mathrm{UNPNP}}(N)
<
C_{\mathrm{baseline}}(N)
}
$$

其中：

$$
C_{\mathrm{UNPNP}}(N)
$$

必須包含：

- reasoning；
- routing；
- compilation；
- verification；
- crystal lookup；
- memory；
- maintenance；
- invalidation；
- failure；
- rollback。

因此，UGER 不允許把 complexity 移到看不見的地方後宣稱「變快」。只有當完整生命週期成本下降，且安全、正確性、失效率與維護成本仍在可接受域內，才視為 UNPNP runtime 成功。

**關鍵詞：** UNPNP、Game Experimental Runtime、Adaptive Corridor、Path Compilation、Computational Crystallization、Frozen Model、Benchmark、Replay、Ablation、Legacy Recompilation

---

# 1. 研究目的

UGER 的主要研究問題不是：

> AI 能不能玩遊戲？

而是：

$$
\boxed{
\textbf{
AI 能不能逐步把一個既有計算世界，重新編譯成一個未來更便宜的計算世界？
}
}
$$

---

# 2. 核心可證偽命題

若 UNPNP 有工程價值，則在部分穩定 workload 中：

$$
\boxed{
C_{\mathrm{future}}
<
C_{\mathrm{initial}}
}
$$

應隨使用歷史增加而出現。

---

# 3. 非目標

UGER v0.1 不追求：

- 最強遊戲 AI；
- state-of-the-art game score；
- RL benchmark 排名；
- 自主多人代理；
- production deployment；
- 完整 AI OS。

---

# 4. 第一版目標

只驗證：

$$
\boxed{
\text{repeated computation}
\rightarrow
\text{reusable verified structure}
}
$$

是否成立。

---

# 5. 核心實驗變因

最重要控制條件：

$$
\boxed{
\text{same model}
+
\text{same world}
+
\text{same hardware}
+
\text{same seed}
+
\text{different runtime architecture}.
}
$$

---

# 6. Runtime 總架構

UGER v0.1：

```text
Game / Synthetic World
        ↓
Game Adapter
        ↓
State Observer
        ↓
Event Normalizer
        ↓
Transition Logger
        ↓
Semantic Revealing
        ↓
Adaptive Corridor Generator
        ↓
EHPE Gate
        ↓
Fast / Slow Path Router
        ↓
Executor
        ↓
Validator
        ↓
Cost Ledger
        ↓
Receipt
        ↓
Path Compiler
        ↓
Crystal Store
        ↺
```

---

# 7. Game Adapter

所有遊戲差異先封裝於：

$$
\boxed{
\text{Game Adapter}
}
$$

UGER 核心不直接依賴遊戲 UI。

---

# 8. Game Adapter 介面

至少提供：

```text
observe_state()
list_local_actions()
execute_action(action)
save_state()
load_state(snapshot_id)
get_version()
get_seed()
```

---

# 9. 結構化優先

若遊戲已有：

- API；
- mod interface；
- scripting；
- save data；
- internal event hooks；

優先使用。

---

# 10. UI 操作不是第一選擇

因為 UI 會加入：

- vision；
- cursor；
- OCR；
- layout；
- timing noise。

這會污染 UNPNP 計算實驗。

---

# 11. State Observer

輸出：

$$
S_t.
$$

第一版可以分：

$$
S_t
=
\langle
S_{\mathrm{world}},
S_{\mathrm{actor}},
S_{\mathrm{task}},
S_{\mathrm{resource}}
\rangle.
$$

---

# 12. WorldSnapshot Schema

```text
WorldSnapshot
- snapshot_id
- run_id
- timestamp
- tick
- game_version
- random_seed
- world_state_digest
- actor_state
- task_state
- resource_state
- active_subspaces[]
- capability_state
```

---

# 13. Event Normalizer

不同遊戲事件轉成統一：

$$
E_t.
$$

---

# 14. TransitionEvent Schema

```text
TransitionEvent
- event_id
- run_id
- from_snapshot
- to_snapshot
- transition_type
- action
- inputs
- outputs
- side_effects
- subspace_from
- subspace_to
- cost_record_id
- validation_state
- provenance
```

---

# 15. Transition Logger

每個 transition 都要可追。

不保存 private chain-of-thought。

只保存可審計的 operation trace。

---

# 16. PathTrace

一段 path：

$$
\Gamma
=
(\Theta_1,\ldots,\Theta_n).
$$

---

# 17. PathTrace Schema

```text
PathTrace
- trace_id
- run_id
- start_snapshot
- end_snapshot
- events[]
- task_contract
- semantic_family
- total_cost
- failure_state
- rollback_state
- verifier_results[]
```

---

# 18. Semantic Revealing Layer

輸入：

$$
S_t,g_t.
$$

輸出：

$$
W_t^{active}.
$$

---

# 19. Revealing 目標

避免每一輪把整個世界：

$$
\mathcal W
$$

送進 reasoning。

要求：

$$
|W_t^{active}|
\ll
|\mathcal W|.
$$

---

# 20. 第一版顯影方法

可以只使用：

- task scope；
- local state；
- active entities；
- relevant inventory；
- recent transitions；
- current objective。

---

# 21. 不需要先做最強 Semantic Revealing

先測：

> 有沒有 working-set reduction。

---

# 22. Adaptive Corridor Generator

輸入：

$$
(
S_t,
g_t,
H_t,
B_t,
R_t,
\mathcal K_t
).
$$

輸出：

$$
\Phi_t.
$$

---

# 23. CorridorCandidate Schema

```text
CorridorCandidate
- corridor_id
- source_state_class
- goal_class
- candidate_events[]
- required_capabilities[]
- estimated_cost
- estimated_risk
- novelty_score
- expected_reuse
- validator_plan
- fallback
```

---

# 24. Routing Levels

第一版：

$$
L_0
=
\text{Known Fast Path},
$$

$$
L_1
=
\text{Local Adaptive},
$$

$$
L_2
=
\text{Deep Reasoning}.
$$

---

# 25. L0

若：

$$
G_\kappa(S_t)=1
$$

且 crystal trust 足夠：

$$
T_K\ge\theta_T,
$$

直接用 crystal。

---

# 26. L1

若沒有 exact hot crystal，

在局部候選中 route。

---

# 27. L2

只有 novelty 高或 route failure 時才呼叫深 reasoning。

---

# 28. Novelty Score

$$
N_t
=
N(
S_t
\mid
\mathcal K_t
).
$$

---

# 29. Reasoning Escalation

$$
N_t\ge\theta_N
\Rightarrow
L_2.
$$

---

# 30. EHPE Gate

所有 candidate path 不可直接 crystallize。

先：

$$
\operatorname{EHPE}(\Gamma).
$$

---

# 31. EHPE 最小欄位

```text
frequency
runtime_cost
estimated_saving
stability
verification_burden
maintenance_burden
risk
domain_width
expected_reuse
selection_cost
```

---

# 32. EHPE 最小判斷

若：

$$
U_H(\Gamma)\le0,
$$

則：

$$
\text{retain / observe}.
$$

---

# 33. Path Compiler

Path Compiler 不應每個 trace 都啟動。

只處理 EHPE-positive path。

---

# 34. Compiler Pipeline

```text
Trace Selection
→ Stable Segment Detection
→ Contract Inference
→ Candidate Recomposition
→ Differential Verification
→ Benchmark
→ Guard Generation
→ CompiledPath
```

---

# 35. CompiledPath Schema

```text
CompiledPath
- compiled_id
- source_trace_ids[]
- semantic_family
- valid_domain
- guard
- executable_form
- input_contract
- output_contract
- validator
- fallback
- dependency_fingerprint
- benchmark
- provenance
```

---

# 36. ComputationalCrystal Schema

```text
ComputationalCrystal
- crystal_id
- compiled_id
- lifecycle_state
- trust_score
- frequency
- hit_count
- success_count
- failure_count
- total_saved_cost
- maintenance_cost
- invalidation_rules
- required_capabilities[]
- risk_class
- last_verified_at
- version
```

---

# 37. Crystal Lifecycle

$$
\boxed{
\text{candidate}
\rightarrow
\text{cold}
\rightarrow
\text{warm}
\rightarrow
\text{hot}
\rightarrow
\text{stale}
\rightarrow
\text{retired}.
}
$$

---

# 38. Promotion Gate

Candidate $\rightarrow$ Cold：

$$
V_{\mathrm{basic}}=1.
$$

---

# 39. Cold $\rightarrow$ Warm

要求：

$$
n_{\mathrm{success}}\ge\theta_W.
$$

---

# 40. Warm $\rightarrow$ Hot

要求：

$$
T_K\ge\theta_H,
$$

$$
U_L>0,
$$

$$
R\le\theta_R.
$$

---

# 41. Hot $\rightarrow$ Stale

若：

- dependency change；
- version change；
- guard anomaly；
- failure spike。

---

# 42. Stale $\rightarrow$ Retired / Revalidated

視：

$$
C_{\mathrm{repair}}
$$

與：

$$
C_{\mathrm{rebuild}}.
$$

---

# 43. Fast / Slow Path Router

核心：

```text
if hot_crystal_matches:
    fast_path
elif warm_candidate_matches:
    guarded_path
else:
    adaptive_or_deep_path
```

---

# 44. Fast Path

應包含：

- cheap guard；
- cheap capability check；
- fast validator；
- receipt。

---

# 45. Slow Path

可以展開：

- state；
- candidate actions；
- deep reasoning；
- full validation。

---

# 46. Validator

至少三層：

$$
V_{\mathrm{pre}},
V_{\mathrm{inline}},
V_{\mathrm{post}}.
$$

---

# 47. Fast Validator

Hot crystal 使用：

- digest；
- range；
- invariant；
- version；
- state class。

---

# 48. Deep Validator

在：

- novelty；
- failure；
- shift；
- shadow compile；

時使用。

---

# 49. Safety Envelope

第一版：

$$
E_S
=
\langle
I,
C,
R,
T,
B
\rangle.
$$

---

# 50. Risk Classes

UGER v0.1 只允許：

$$
R_0,
R_1,
R_2.
$$

---

# 51. $R_0$

Pure read。

---

# 52. $R_1$

Local reversible write。

---

# 53. $R_2$

Sandbox execution。

---

# 54. 明確排除

UGER v0.1 不做：

- external payment；
- account privilege；
- production mutation；
- irreversible external write；
- multiplayer cheating；
- remote exploit。

---

# 55. Cost Ledger

CostRecord：

```text
CostRecord
- cost_id
- run_id
- event_id
- wall_time_ms
- cpu_time_ms
- gpu_time_ms
- memory_peak
- io_bytes
- state_transfer_bytes
- model_calls
- tool_calls
- model_input_units
- model_output_units
- verification_cost
- maintenance_cost
- rollback_cost
- failure_cost
```

---

# 56. 系統總成本

$$
\boxed{
C_T
=
C_{\mathrm{reason}}
+
C_{\mathrm{route}}
+
C_{\mathrm{execute}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{compile}}
+
C_{\mathrm{select}}
+
C_{\mathrm{memory}}
+
C_{\mathrm{maintain}}
+
C_{\mathrm{failure}}.
}
$$

---

# 57. Token 只是部分成本

不能：

$$
\text{token reduction}
\Rightarrow
\text{UNPNP success}.
$$

---

# 58. Wall Clock

$$
T_{\mathrm{wall}}
$$

必須單獨報告。

---

# 59. Tail Latency

Real-time 階段至少：

$$
p50,p95,p99.
$$

---

# 60. Reasoning Ratio

$$
R_{\mathrm{reason}}
=
\frac{
N_{\mathrm{deep-reasoned}}
}{
N_{\mathrm{transition}}
}.
$$

---

# 61. Corridor Hit Ratio

$$
H_{\mathrm{corridor}}
=
\frac{
N_{\mathrm{verified-corridor-hit}}
}{
N_{\mathrm{transition}}
}.
$$

---

# 62. Crystal Hit Ratio

$$
H_K
=
\frac{
N_{\mathrm{crystal-hit}}
}{
N_{\mathrm{transition}}
}.
$$

---

# 63. Crystal Invalid Rate

$$
I_K
=
\frac{
N_{\mathrm{invalid-crystal}}
}{
N_{\mathrm{crystal-use}}
}.
$$

---

# 64. Failure Rate

$$
F_R
=
\frac{
N_{\mathrm{fail}}
}{
N_{\mathrm{transition}}
}.
$$

---

# 65. Rollback Rate

$$
R_B
=
\frac{
N_{\mathrm{rollback}}
}{
N_{\mathrm{transition}}
}.
$$

---

# 66. Maintenance Cost

$$
C_M.
$$

---

# 67. Selection Cost

$$
C_S.
$$

---

# 68. Crystal Growth

$$
|\mathcal K_t|.
$$

必須監控。

---

# 69. Crystal Utility

$$
U_L(\kappa)
=
N\Delta C_{\mathrm{net}}
-
C_{\mathrm{build}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{risk}}.
$$

---

# 70. Break-Even

$$
N^\*
=
\left\lceil
\frac{
C_{\mathrm{fixed}}
}{
\Delta C_{\mathrm{net}}
}
\right\rceil.
$$

---

# 71. Experiment Controller

負責：

- baseline config；
- seeds；
- model lock；
- hardware lock；
- run schedule；
- receipts。

---

# 72. ExperimentReceipt Schema

```text
ExperimentReceipt
- experiment_id
- phase
- baseline_type
- game_id
- game_version
- model_id
- model_version
- hardware_profile
- config_digest
- random_seeds[]
- start_time
- end_time
- aggregate_metrics
- crystal_manifest
- failure_summary
- reproducibility_status
```

---

# 73. Baseline A

$$
B_A
=
\text{Traditional / Naive}.
$$

特徵：

- no persistent corridor；
- no crystal；
- ordinary planner / scripted logic。

---

# 74. Baseline B

$$
B_B
=
\text{Adaptive without Crystallization}.
$$

允許：

- reasoning；
- search；
- local adaptive routing。

不允許：

- persistent crystal reuse。

---

# 75. Experimental C

$$
E_C
=
\text{Adaptive + Crystallization}.
$$

允許完整：

- corridor；
- EHPE；
- path compiler；
- crystal；
- fast path；
- invalidation。

---

# 76. Optional Baseline D

可加入：

$$
B_D
=
\text{ordinary cache / memoization}.
$$

---

# 77. 為什麼需要 Cache Baseline？

避免最後只證明：

> cache 有用。

---

# 78. Frozen-Model Protocol

固定：

$$
\theta_{\mathrm{model}}.
$$

---

# 79. Model Config Lock

保存：

- model ID；
- version；
- temperature；
- sampling；
- prompt template；
- tool set。

---

# 80. 只有外部結構可變

允許：

$$
\mathcal K_t,
\mathcal R_t,
\mathcal I_t,
\mathcal S_t.
$$

---

# 81. Frozen-Model Success

若：

$$
C_{\mathrm{avg}}(t)\downarrow
$$

且：

$$
R_{\mathrm{reason}}(t)\downarrow,
$$

則支持：

$$
\boxed{
\text{structural learning}.
}
$$

---

# 82. Phase 0：Synthetic World

最小世界可包含：

- grid；
- object store；
- inventory；
- task queue；
- deterministic transitions。

---

# 83. Phase 0 研究目標

只驗證：

- schema；
- replay；
- path compilation；
- crystal lifecycle；
- invalidation；
- cost ledger。

---

# 84. Phase 0 Success Gate

至少：

$$
C_C<C_A
$$

在 repeated workload。

---

# 85. Phase 0 Failure Gate

如果：

$$
C_{\mathrm{crystal-overhead}}
>
C_{\mathrm{saved}},
$$

停止擴張。

---

# 86. Phase 1：Turn-Based Game

候選類型：

- tactics；
- turn-based RPG；
- board-like strategy。

---

# 87. Phase 1 優點

低 timing noise。

---

# 88. Phase 1 主要測

- semantic family；
- guard；
- negative crystal；
- multi-step action；
- replay。

---

# 89. Phase 2：Simulation / Management

候選：

- colony；
- economy；
- management；
- world simulation。

---

# 90. Phase 2 主要測

- long-running state；
- maintenance；
- stale crystal；
- higher-order crystal；
- dynamic working set。

---

# 91. Phase 3：Real-Time Single Player

候選：

- RTS；
- action simulation；
- real-time management。

---

# 92. Phase 3 主要測

- latency；
- p95 / p99；
- variance；
- fast-path utility；
- deoptimization speed。

---

# 93. Phase 4：Controlled Legacy Program

不是 production。

---

# 94. Phase 4 Target

例如：

- parser；
- local query engine；
- simulation；
- test runner；
- build pipeline；
- deterministic data transform。

---

# 95. Legacy Adapter

提供：

```text
observe_call()
trace_call_graph()
capture_io()
shadow_execute(candidate)
compare_outputs()
rollback()
```

---

# 96. Shadow Recompilation

$$
\Gamma_{\mathrm{legacy}}
\parallel
\widehat{\Gamma}_{\mathrm{shadow}}.
$$

---

# 97. Phase 4 不直接替換

新 path 先只：

- shadow；
- benchmark；
- verify。

---

# 98. Promotion to Active Overlay

只有：

$$
V_{\mathrm{equiv}}\ge\theta_V,
$$

$$
U_L>0,
$$

$$
R\le\theta_R.
$$

---

# 99. Legacy Crystal Overlay

$$
\boxed{
P_t
=
P_{\mathrm{legacy}}
\oplus
\mathcal K_t.
}
$$

---

# 100. Source Rewrite 是後續研究

不是 TW-02 v0.1 必做。

---

# 101. Replay Harness

所有 phase 都要求 deterministic replay 優先。

---

# 102. Replay Input

保存：

- start snapshot；
- random seed；
- config；
- version；
- model config。

---

# 103. Replay Output

比較：

- end state；
- cost；
- errors；
- path；
- crystal usage。

---

# 104. Differential Verification

同 input：

$$
\Gamma_{\mathrm{old}}(x)
$$

與：

$$
\widehat{\Gamma}(x).
$$

---

# 105. Exact Equivalence

適用 deterministic domain。

---

# 106. Semantic Equivalence

適用：

$$
\Gamma
\simeq_{\mathcal T}
\widehat{\Gamma}.
$$

---

# 107. Statistical Equivalence

stochastic domain 使用：

$$
D(
P_{\Gamma},
P_{\widehat{\Gamma}}
)
\le
\epsilon.
$$

---

# 108. A/B/C Protocol

同一組 seeds：

$$
\{s_1,\ldots,s_n\}.
$$

分別跑：

$$
B_A,
B_B,
E_C.
$$

---

# 109. Sample Size

初期不硬定全域樣本數。

由 variance 決定。

---

# 110. 最低要求

不能單 seed、單 run 就下結論。

---

# 111. Distribution Split

至少：

- observed；
- validation；
- shifted。

---

# 112. Observed

允許形成 crystal。

---

# 113. Validation

不新增或限制新增 crystal。

測泛化。

---

# 114. Shifted

故意變：

- rules；
- map；
- items；
- difficulty；
- entities。

---

# 115. Shift Success

舊 crystal 應：

$$
\text{hot}
\rightarrow
\text{warm / stale}.
$$

---

# 116. Invalidation Accuracy

測：

$$
Acc_I
=
\frac{
TP_I+TN_I
}{
N_I
}.
$$

---

# 117. Guard Precision

$$
P_G
=
\frac{
TP
}{
TP+FP
}.
$$

---

# 118. Guard Recall

$$
R_G
=
\frac{
TP
}{
TP+FN
}.
$$

---

# 119. 高 Precision 優先

因 fast path false positive 風險高。

---

# 120. Negative Crystal Experiment

故意提供：

$$
\Gamma_{\mathrm{bad}}.
$$

---

# 121. 觀察

系統是否：

$$
\text{repeat bad exploration}
\downarrow.
$$

---

# 122. Negative Crystal Reopen

環境改後：

$$
\Gamma_{\mathrm{bad}}
$$

變 valid。

測是否 reopen。

---

# 123. Higher-Order Crystal Experiment

先得到：

$$
\kappa_1,\kappa_2,\kappa_3.
$$

再：

$$
K^{(2)}
(
\kappa_1,\kappa_2,\kappa_3
).
$$

---

# 124. Higher-Order Success

要求：

$$
C(\kappa^{(2)})
<
C(\kappa_1\rightarrow\kappa_2\rightarrow\kappa_3).
$$

---

# 125. Cache-Control Experiment

加入普通 memoization baseline。

---

# 126. 如果 Crystal 只在 identical input 贏

那只是 cache-like。

---

# 127. Semantic Family Experiment

讓 raw state 不同，

但 task contract 相同。

---

# 128. Procedure-Level Reuse

成功要求：

$$
s_a\neq s_b
$$

仍能命中：

$$
\kappa_{\mathcal D}.
$$

---

# 129. Ablation 1：No Revealing

關掉：

$$
\Pi_\xi.
$$

---

# 130. Ablation 2：No Corridor Store

不保存 path memory。

---

# 131. Ablation 3：No EHPE

所有 candidate 都 compile。

---

# 132. Ablation 4：No Negative Crystal

失敗 path 不記錄。

---

# 133. Ablation 5：No Invalidation

crystal 永不 stale。

---

# 134. Ablation 6：Deep Verify Only

沒有 fast verifier。

---

# 135. Ablation 7：Fast Verify Only

沒有 deep escalation。

---

# 136. Ablation 8：No Path Compilation

只 cache result。

---

# 137. Ablation 9：No Higher-Order Crystal

只允許一階。

---

# 138. Ablation 10：No Selection Pruning

保留所有 crystal。

---

# 139. Ablation 的目標

測每個模組是否真的貢獻：

$$
\Delta U>0.
$$

---

# 140. Success Gate 1：完整成本

要求：

$$
\boxed{
C_T^{E_C}
<
C_T^{B_A}.
}
$$

---

# 141. Success Gate 2：Reasoning

$$
R_{\mathrm{reason}}^{E_C}
<
R_{\mathrm{reason}}^{B_B}.
$$

---

# 142. Success Gate 3：錯誤

$$
F_R^{E_C}
\le
F_R^{B_A}
+
\epsilon.
$$

---

# 143. Success Gate 4：維護

$$
C_M
$$

不能吞掉 runtime saving。

---

# 144. Success Gate 5：Selection

$$
C_S
$$

不能隨 crystal count 爆炸。

---

# 145. Success Gate 6：Shift

crystal invalidation 正常。

---

# 146. Success Gate 7：Replay

結果可重現。

---

# 147. Failure Gate 1

$$
C_{\mathrm{compile}}
+
C_M
>
C_{\mathrm{saved}}.
$$

---

# 148. Failure Gate 2

$$
R_{\mathrm{reason}}
$$

不下降。

---

# 149. Failure Gate 3

$$
|\mathcal K|\uparrow
$$

但：

$$
H_K
$$

不升。

---

# 150. Failure Gate 4

錯誤率惡化。

---

# 151. Failure Gate 5

Guard cost 高於 saved cost。

---

# 152. Failure Gate 6

Distribution shift 下 crystal 仍盲目 hot。

---

# 153. Failure Gate 7

Memory / selection overhead 超線性爆炸。

---

# 154. 研究負結果的價值

若某 workload：

$$
Q_K\approx0,
$$

也應記錄。

---

# 155. Non-Crystallizable Workload Class

可以形成：

$$
\boxed{
\mathcal D_{\mathrm{NC}}.
}
$$

---

# 156. Workload Taxonomy

第一版分類：

```text
high-repetition stable
high-repetition dynamic
low-repetition stable
one-shot
stochastic
adversarial-like
high-verification-burden
```

---

# 157. Crystallizability Score

$$
Q_K(\mathcal D)
=
f(
F,
S,
C,
V,
M,
R
).
$$

---

# 158. Long-Term Research Output

最重要的不只是：

> UNPNP 成功。

而是建立：

$$
\boxed{
\text{Which workloads are crystallizable?}
}
$$

---

# 159. Model Transfer Experiment

當 v0.1 穩定後，

固定：

$$
\mathcal K.
$$

換模型：

$$
M_A\rightarrow M_B.
$$

---

# 160. 測什麼？

- crystal reuse；
- guard interpretation；
- validator consistency；
- routing variance。

---

# 161. Cross-Agent Experiment

Agent A 建 crystal。

Agent B 使用。

---

# 162. 需要 Provenance

不能只共享 executable blob。

---

# 163. Crystal Package

```text
crystal
guard
contract
validator
provenance
version
capability requirements
benchmark evidence
```

---

# 164. Hardware Transfer

同一 crystal：

$$
H_A\rightarrow H_B.
$$

---

# 165. Hardware-Aware Version

必要時：

$$
\kappa^{CPU},
\kappa^{GPU}.
$$

---

# 166. Security Test 1

Capability mismatch。

---

# 167. 預期

$$
\text{deny}.
$$

---

# 168. Security Test 2

Stale capability。

---

# 169. 預期

hot crystal 立即降級。

---

# 170. Security Test 3

Untrusted external input。

---

# 171. 預期

不能自動變 privileged instruction。

---

# 172. Security Test 4

Irreversible action request。

---

# 173. 預期

UGER v0.1：

$$
\text{deny / out-of-scope}.
$$

---

# 174. Research Storage

第一版可用：

- SQLite / DuckDB；
- JSONL；
- local object store；
- SEDB prototype。

---

# 175. 不要先建大型分散式架構

因為會污染實驗。

---

# 176. Recommended Directory

```text
/runtime/
  adapter/
  observer/
  router/
  compiler/
  crystal/
  validator/
  safety/

/data/
  snapshots/
  traces/
  crystals/
  receipts/
  benchmarks/

/experiments/
  phase0/
  phase1/
  phase2/
  phase3/
  phase4/
```

---

# 177. Configuration

```text
model.yaml
game.yaml
runtime.yaml
safety.yaml
benchmark.yaml
```

---

# 178. Crystal Store

至少支援：

- lookup；
- insert；
- promote；
- demote；
- invalidate；
- retire；
- stats。

---

# 179. Crystal Index

第一版可以：

- exact state class；
- semantic family；
- goal class；
- dependency fingerprint。

---

# 180. 不需要一開始上 Vector DB

先證明 primitive routing。

---

# 181. 如果需要 Semantic Family

再加 embedding / semantic index。

---

# 182. Runtime Loop

```text
observe
→ reveal
→ detect novelty
→ lookup crystal
→ if hit: validate guard and execute
→ else: adaptive route / deep reason
→ validate result
→ log receipt
→ update statistics
→ EHPE candidate
→ optional compile
→ optional crystallize
```

---

# 183. Pseudocode

```text
while not done:
    state = observe()
    active = reveal(state, goal)

    crystal = crystal_store.match(active, goal)

    if crystal and crystal.guard(active):
        result = execute(crystal)
        if fast_validate(result):
            log(result)
            update(crystal)
            continue
        else:
            demote(crystal)

    corridor = adaptive_route(active, goal)

    if corridor is uncertain:
        corridor = deep_reason(active, goal)

    result = execute(corridor)
    verified = deep_validate(result)

    log(result, verified)

    if verified:
        candidate = ehpe(trace_window)
        if candidate.utility > threshold:
            compiled = compile(candidate)
            if differential_verify(compiled):
                crystal_store.insert(compiled)
```

---

# 184. Research Reproducibility

每次 release：

- source commit；
- config；
- game version；
- model version；
- hardware；
- seeds；
- manifest。

---

# 185. Benchmark Artifact

每輪輸出：

```text
metrics.json
crystal_manifest.json
failure_report.md
cost_ledger.csv
replay_receipt.json
```

---

# 186. Release Gate

UGER v0.1 release 至少要求：

- deterministic Phase 0 pass；
- reproducible benchmark；
- no unsafe external action；
- cost ledger complete；
- crystal invalidation demonstrated。

---

# 187. Phase 1 Gate

Turn-based：

$$
C_T^{E_C}
<
C_T^{B_A}
$$

至少在部分 workload 顯著成立。

---

# 188. Phase 2 Gate

Simulation：

maintenance cost 仍受控。

---

# 189. Phase 3 Gate

Real-time：

p95 / p99 improvement 或 variance reduction 成立。

---

# 190. Phase 4 Gate

Legacy shadow path：

equivalence + lifecycle utility 成立。

---

# 191. Future Legacy Recompilation Interface

若 Phase 4 成功，

下一代可加入：

```text
Source Mapper
IR Builder
Semantic Path Profiler
Candidate Rewriter
Patch Generator
Formal / Property Verifier
Source Patch Gate
```

---

# 192. 但不在 TW-02 v0.1 實作

這只是 future interface。

---

# 193. AI Recompilation 的三階段

$$
\boxed{
\text{Runtime Overlay}
\rightarrow
\text{Shadow Replacement}
\rightarrow
\text{Source Rewrite}.
}
$$

---

# 194. 第一階段最安全

Runtime overlay 不改 canonical source。

---

# 195. 第二階段

Shadow replacement 只比較。

---

# 196. 第三階段

只有成熟後回寫 source。

---

# 197. 這避免一次性 AI Rewrite

降低：

- regression；
- hallucinated refactor；
- hidden behavior loss。

---

# 198. 與 SEDB 的關係

SEDB 可保存：

- event；
- crystal；
- receipt；
- cost；
- dependency。

---

# 199. 與 Omphalos 的關係

Omphalos 可作為：

- route search；
- method selection；
- counter-evidence；
- alternative path discovery。

---

# 200. 與 CSG 的關係

TW-01 CSG 可以保存：

> 系統知道什麼。

TW-02 crystal store 保存：

> 系統知道怎麼更快做。

---

# 201. 未來雙圖

$$
\boxed{
\mathcal G_{\mathrm{semantic}}
\leftrightarrow
\mathcal G_{\mathrm{computational}}.
}
$$

---

# 202. 第一版仍分離

避免 action / memory 混淆。

---

# 203. 核心命題一

$$
\boxed{
\textbf{
單機遊戲不是 UNPNP 的最終應用，而是最適合第一個驗證「計算世界能否被逐步重新編譯」的受控實驗生態。
}
}
$$

---

# 204. 核心命題二

$$
\boxed{
\textbf{
Frozen-model protocol 是 UGER 的核心控制實驗，因為它可以把模型能力提升與結晶化架構收益分離。
}
}
$$

---

# 205. 核心命題三

$$
\boxed{
\textbf{
任何 UNPNP 加速都必須以完整成本帳本衡量；把成本移到編譯、驗證、記憶或維護後不能假裝它消失。
}
}
$$

---

# 206. 核心命題四

$$
\boxed{
\textbf{
如果 crystal 不能在 distribution shift 下正確失效、降級與重建，那麼 fast path 不是學習，而是技術債。
}
}
$$

---

# 207. 核心命題五

$$
\boxed{
\textbf{
未來一般程式 AI 再編譯應由 runtime evidence 驅動，先做 selective overlay，再做 shadow replacement，最後才考慮 source rewrite。
}
}
$$

---

# 208. 最終實驗總式

Baseline：

$$
C_B(N)
=
\sum_{i=1}^{N}
C_{\mathrm{base}}(x_i).
$$

UGER：

$$
\boxed{
C_U(N)
=
C_{\mathrm{build}}
+
C_{\mathrm{compile}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{select}}
+
C_{\mathrm{maintain}}
+
C_{\mathrm{failure}}
+
\sum_{i=1}^{N}
C_{\mathrm{run}}^{K}(x_i).
}
$$

成功：

$$
\boxed{
C_U(N)
<
C_B(N).
}
$$

---

# 209. 加入錯誤與風險

$$
C_U^\*
=
C_U
+
\lambda_F C_{\mathrm{error}}
+
\lambda_R C_{\mathrm{risk}}.
$$

最終仍要求：

$$
\boxed{
C_U^\*
<
C_B^\*.
}
$$

---

# 210. 結論

UGER 的任務不是證明：

> AI 能把所有程式變快。

也不是證明：

$$
P=NP.
$$

它只需要先回答一個更小、但足夠重要的問題：

> 在一個複雜、可重複、可測量、可回滾的世界裡，AI 是否能把反覆走過的計算路徑逐步轉化為已驗證、可重用、低成本的計算原語？

如果答案是否定的，

那麼 UNPNP 的 path compilation / crystallization 假說需要修正。

如果答案是肯定的，

並且我們真的觀察到：

$$
R_{\mathrm{reason}}\downarrow,
$$

$$
H_{\mathrm{corridor}}\uparrow,
$$

$$
H_K\uparrow,
$$

$$
C_{\mathrm{avg}}\downarrow,
$$

同時：

$$
F_R
$$

不失控，

$$
C_M
$$

不吞掉收益，

那麼就出現一個很重要的工程事實：

$$
\boxed{
\textbf{
模型權重沒有變，
但系統因為重新組織自己的計算圖而變得更有效率。
}
}
$$

這就是：

$$
\boxed{
\text{World-to-Corridor Compilation}.
}
$$

而從那一刻開始，

下一個研究問題才真正有意義：

> 這個方法能不能離開遊戲，進入一般 legacy software？

因此 TW-02 的最後接口不是 production deployment，

而是：

$$
\boxed{
\text{Controlled Legacy Program}
\rightarrow
\text{Shadow Recompilation}
\rightarrow
\text{Selective Crystal Overlay}.
}
$$

如果這一步也成立，

未來才有資格進一步研究：

$$
\boxed{
\text{AI-Native General Program Recompilation}.
}
$$

所以整個研究路線可以最終壓成：

$$
\boxed{
\text{先讓 AI 在遊戲中學會「長路」，
再讓它去學會重新編譯真正的程式世界。
}
}
$$

---

## 後續研究接口

本白皮書完成後，下一個尚未正式啟動的未來工程主題為：

**AI-Native Legacy Program Recompilation**

其正式啟動條件應至少包括：

1. UGER Phase 0–2 通過；
2. Frozen-model 結構學習效應可重現；
3. Crystal lifecycle 可控；
4. EHPE 能抑制 over-crystallization；
5. Invalidation / deoptimization 可重現；
6. 完整 cost ledger 顯示正向 lifecycle utility；
7. Controlled Legacy Program shadow experiment 通過。

在此之前，UGER 應保持為研究 runtime，而不是自動修改一般 production software 的系統。
