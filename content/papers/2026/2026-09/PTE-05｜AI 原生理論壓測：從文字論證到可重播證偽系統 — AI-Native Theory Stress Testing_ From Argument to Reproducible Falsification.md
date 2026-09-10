# PTE-05｜AI 原生理論壓測：從文字論證到可重播證偽系統

## AI-Native Theory Stress Testing: From Argument to Reproducible Falsification

**系列：** 《假設你是對的》／Provisional Truth Engineering Series（PTE）  
**系列文件：** PTE-05 / 07  
**版本：** v0.1  
**日期：** 2026-09-09  
**作者：** Neo.K  
**研究協作：** AI-assisted theoretical development  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 公開方法論論文／AI-native theory testing runtime 與可重播驗證架構  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

PTE-01 至 PTE-04 已分別建立：暫時真值工程、理論到工程延遲、公平重建原則與認識論回收。但只要這些仍然依賴研究者手動執行，就尚未回答 AI 時代最重要的下一個問題：

> **能否把「讀取強理論、鋼人化、形式化、實作、建立最強 baseline、生成反例、執行外部測試、分離理論殘差」本身，做成一套可重播、可審計、可故障、可驗收的 AI-native research runtime？**

本文提出 **PTE Theory Stress Runtime（PTE-TSR）**，作為暫時真值工程的第一個完整 AI 原生執行架構。

其主鏈為：

$$
\boxed{
\text{Source Intake}
\rightarrow
\text{Claim Extraction}
\rightarrow
\text{Steelman}
\rightarrow
\text{Formalization}
\rightarrow
\text{Operationalization}
\rightarrow
\text{Implementation}
\rightarrow
\text{Matched Baseline}
\rightarrow
\text{Adversarial Test}
\rightarrow
\text{External Test}
\rightarrow
\text{Fresh Replay}
\rightarrow
\text{Residue}
}
$$

本文將執行系統拆為九類角色：

```text
Source Curator
Claim Analyst
Steelman Agent
Formalization Agent
Theory Implementer
Baseline Reconstructor
Adversarial Tester
Evidence Auditor
Residue Curator
```

並建立一條重要治理原則：

$$
\boxed{
\text{Interpretation}
\neq
\text{Implementation}
\neq
\text{Baseline Construction}
\neq
\text{Final Judgment}
}
$$

換言之，同一個執行上下文不應同時擁有：

- 定義理論最強版本；
- 補完工程規則；
- 建立對照組；
- 選擇評測指標；
- 判定最終勝負；

的完整權力。

本文將這稱為：

# **Epistemic Role Separation**
### 認識論角色分離

PTE-TSR 進一步定義七種核心 artifact：

```text
TheoryManifest
ClaimLedger
InterpretationManifest
OperationalizationManifest
BaselineManifest
ExperimentManifest
EvidenceReceipt
ResidueReport
```

其中 `EvidenceReceipt` 必須把：

$$
\boxed{
\text{Declared}
\neq
\text{Derived}
\neq
\text{Engineering Extension}
\neq
\text{Observed}
\neq
\text{Effective}
}
$$

分離保存。

本文同時提出四類 hard gates：

1. **Source Fidelity Gate**：不可把 evaluator 新增內容偽裝成原理論；
2. **Matched Reconstruction Gate**：baseline 不得在資訊、資料、候選空間或資源上被削弱；
3. **Gold Firewall Gate**：答案不得進 decision path；
4. **Fresh Replay Gate**：最終結論必須能從 frozen artifact 重新執行，而不能只相信原執行 session。

對任何 hard gate：

$$
\boxed{
\text{Hard Fail}
\not\Rightarrow
\text{Aggregate Score Compensation}
}
$$

本文亦規定：AI-as-judge 只能用於 explanation、clarity、novelty suggestion 等 soft dimensions；任何 source lineage、claim scope、hash、baseline parity、gold leakage、test status、replay success 與 artifact integrity 必須由 deterministic 或 structured oracle 判定。

本文最後提出：AI-native theory testing 真正的價值，不是把研究變成「AI 自己說服自己」，而是把大量過去依賴人類手工維持的科學紀律——來源邊界、強基線、公平對照、反例、可重播、版本、未知狀態——編譯成 runtime contract。

因此，PTE-TSR 的終極目標不是：

$$
\text{Automate Agreement}.
$$

而是：

$$
\boxed{
\text{Automate the conditions under which disagreement becomes informative}.
}
$$

**關鍵詞：** AI-Native Science、Theory Testing Runtime、Falsification Harness、Matched Baseline、Epistemic Role Separation、Evidence Receipt、Fresh Replay、Negative Control、Residue Report、Provisional Truth Engineering

---

# 0. 邊界聲明

本文不主張：

- AI 已能自主判定所有理論真假；
- 多 Agent 天然比單 Agent 更可靠；
- role separation 可以完全消除共同模型偏誤；
- AI 生成的 baseline 一定公平；
- deterministic oracle 可以判定所有語義問題；
- 一次 runtime pass 就等於科學證明；
- 工程重播可以代替物理世界外部證據；
- 所有理論都適合自動化壓測；
- 自動生成越多 counterexample 越好；
- AI 自主研究應移除所有人類治理。

本文只研究：

> 如何把 PTE 的理論檢驗紀律轉化為一個可被 AI 執行、但又不允許 AI 透過自我確認、資訊不對稱、隱藏補全、弱 baseline 或不可重播流程製造虛假結論的 research runtime。

---

# 1. 為什麼 PTE 必須進入 Runtime

PTE-01 已定義：

$$
\mathsf{Assume}^{+}(T).
$$

PTE-02 已指出：

$$
L_{TE}\downarrow.
$$

PTE-03 已要求：

$$
B^{*}(T).
$$

PTE-04 已要求：

$$
R_{\mathcal B,\mathcal E}(T).
$$

現在問題變成：

> 誰來執行？

---

## 1.1 手工方法論的限制

如果所有步驟仍需要人類手動：

- 讀來源；
- 拆 claim；
- 建 prototype；
- 找 baseline；
- 跑反例；
- 整理 receipt；

那麼：

$$
C_{\mathrm{coordination}}
$$

仍然可能很高。

---

## 1.2 AI-native 的真正意思

不是：

> 把同一篇論文丟給 LLM 問「你覺得對嗎？」

而是：

$$
\boxed{
\text{Methodology}
\rightarrow
\text{Executable Research Contract}.
}
$$

---

# 2. PTE Theory Stress Runtime

本文定義：

$$
\boxed{
\mathrm{PTE\text{-}TSR}
}
$$

為：

**Provisional Truth Engineering Theory Stress Runtime**。

---

## 2.1 Runtime 輸入

```text
source_bundle
theory_id
source_boundary
task_scope
resource_budget
baseline_policy
external_evidence_policy
stop_policy
```

---

## 2.2 Runtime 輸出

```text
TheoryManifest
ClaimLedger
ImplementationArtifacts
BaselineArtifacts
ExperimentArtifacts
EvidenceReceipt
ResidueReport
FinalStatus
```

---

# 3. Runtime 主鏈

$$
\boxed{
S
\rightarrow
C
\rightarrow
T^{+}
\rightarrow
F
\rightarrow
O
\rightarrow
I
\rightarrow
B^{*}
\rightarrow
A
\rightarrow
X
\rightarrow
R
}
$$

其中：

- $S$：source；
- $C$：claims；
- $T^{+}$：strongest defensible interpretation；
- $F$：formal model；
- $O$：observables；
- $I$：implementation；
- $B^{*}$：matched reconstruction；
- $A$：adversarial test；
- $X$：external evidence；
- $R$：residue。

---

# 4. 九類執行角色

## 4.1 Source Curator

責任不是解釋理論，而是凍結：

$$
\boxed{
\text{what counts as the theory source}.
}
$$

其輸出 `TheoryManifest` 至少包含：

```text
theory_id
title
version
source_files
source_hashes
source_dates
source_authority
included_material
excluded_material
source_boundary_notes
```

若沒有 source boundary，後續 evaluator 可以無限加入「其實理論還有另一個版本」，使測試永遠移動。

---

## 4.2 Claim Analyst

Claim Analyst 將：

$$
T
$$

拆成：

$$
\{C_1,\ldots,C_n\}.
$$

`ClaimLedger` 最小包含：

```text
claim_id
source_span
claim_text
claim_type
scope
quantifier
dependencies
declared_evidence
operationality
falsifier_candidate
status
```

第一階段只做：

$$
\boxed{
\text{faithful decomposition}.
}
$$

不先判對錯。

---

## 4.3 Steelman Agent

Steelman Agent 建立：

$$
T^{+}.
$$

但不能自由發明。每個補全要標：

```text
DECLARED
DERIVED
ENGINEERING_EXTENSION
EVALUATOR_ASSUMPTION
UNKNOWN
```

`InterpretationManifest` 應記：

```text
claim_id
original_claim
strongest_interpretation
interpretation_basis
added_assumptions
assumption_class
scope_change
confidence
```

---

## 4.4 Formalization Agent

將：

$$
T^{+}
$$

轉成：

$$
F(T).
$$

最小輸出：

```text
entities
variables
states
relations
operators
constraints
invariants
transitions
observables
failure_conditions
unknowns
```

不可形式化是合法輸出：

```text
status = UNFORMALIZED
```

而不是硬翻譯。

---

## 4.5 Operationalization Agent

回答：

> 如果 claim 成立，哪個 observable 應該不同？

`OperationalizationManifest`：

```text
claim_id
observable
measurement
success_condition
failure_condition
proxy
proxy_limit
external_evidence_needed
```

---

## 4.6 Theory Implementer

Theory Implementer 只能看：

- frozen interpretation；
- formalization；
- operationalization。

不得自行擴張 claim。若實作需要新規則：

$$
r^{*},
$$

必須標：

```text
ENGINEERING_EXTENSION
```

---

## 4.7 Baseline Reconstructor

這是最重要的隔離角色之一。

它的工作不是：

> 模仿 theory code。

而是：

> 用已知一般機制，在 matched conditions 下完成同一 task。

最強模式下，它最好只得到：

```text
task contract
observables
data
candidate space
resource budget
evaluation metric
```

而不得到：

```text
theory-specific vocabulary
theory implementation
theory internal predicates
```

這就是 **Blind Reconstruction**。

若仍能：

$$
M(B)
\approx
M(S_T),
$$

則 conventional reconstructibility 證據增加。

---

## 4.8 Adversarial Tester

其任務不是讓理論看起來好，而是找：

$$
D_{\Delta}.
$$

主要攻擊軸：

```text
boundary cases
noise
missing information
contradiction
event reordering
duplicate events
partial observability
adversarial paraphrase
OOD input
resource pressure
counterexample search
```

---

## 4.9 Evidence Auditor 與 Residue Curator

Evidence Auditor 不應參與 steelman、implementation 或 baseline building。

它只問：

```text
source matched?
claim frozen?
metric frozen?
baseline fair?
gold leaked?
tests actually run?
fresh replay passed?
artifact hashes match?
```

Residue Curator 輸入 theory result、baseline result、external evidence、claim status，輸出：

$$
R_{\mathcal B,\mathcal E}(T).
$$

它不能替理論找藉口，只能從 source-supported、evidence-supported、explicitly inferred 內容建立 residue。

---

# 5. Epistemic Role Separation

本文提出：

$$
\boxed{
\text{Interpret}
\neq
\text{Implement}
\neq
\text{Reconstruct}
\neq
\text{Judge}.
}
$$

如果同一 Agent：

1. 決定理論最強版本；
2. 寫 theory implementation；
3. 寫 baseline；
4. 選 metric；
5. 宣布 theory win；

則存在巨大：

$$
\boxed{
\text{self-confirmation surface}.
}
$$

---

# 6. Role Separation 不等於 Independence Proof

如果所有角色：

- 同模型；
- 同 system prompt；
- 同 memory；
- 同 training biases；

仍可能高度相關。

因此：

$$
\boxed{
\text{Role separation}
\neq
\text{epistemic independence}.
}
$$

可定義：

$$
I_E
\in
[0,1]
$$

為 Independence Gradient。

低 independence：

```text
same context
same hidden state
same decision helper
```

中 independence：

```text
separate contexts
separate prompts
separate artifacts
same model family
```

高 independence：

```text
different models
different providers
different implementation teams
blind baseline
external replication
```

---

# 7. Runtime 狀態機

```text
INGESTED
CLAIMS_FROZEN
STEELMANNED
FORMALIZED
OPERATIONALIZED
IMPLEMENTED
BASELINED
ADVERSARIAL_TESTED
EXTERNAL_TESTED
REPLAYED
RESIDUE_EXTRACTED
CLOSED
```

Blocked states：

```text
BLOCKED_SOURCE
BLOCKED_FORMALIZATION
BLOCKED_IMPLEMENTATION
BLOCKED_BASELINE
BLOCKED_EXTERNAL_EVIDENCE
BLOCKED_REPLAY
```

---

# 8. Declared / Derived / Effective 分離

本文要求：

$$
\boxed{
D
\neq
R
\neq
E
}
$$

其中：

- $D$：Declared；
- $R$：Derived / Runtime-added；
- $E$：Effective behavior。

例如：

```text
Declared: identity should remain stable
Runtime added: use versioned registry
Observed: replay is order-independent
Effective: generic event sourcing can reproduce the same property
```

這四層不能混。

---

# 9. 核心 Artifacts

## 9.1 TheoryManifest

```yaml
theory_id:
version:
source_boundary:
sources:
claims:
declared_scope:
declared_novelty:
declared_evidence:
```

## 9.2 ClaimLedger

```yaml
claim_id:
source_ref:
type:
scope:
quantifier:
dependencies:
declared:
derived:
engineering_extensions:
observable:
falsifier:
status:
```

## 9.3 InterpretationManifest

```yaml
claim_id:
strongest_defensible_reading:
basis:
added_assumptions:
assumption_class:
alternative_readings:
chosen_reason:
```

## 9.4 OperationalizationManifest

```yaml
claim_id:
observable:
measurement:
test_domain:
success:
failure:
abstention:
external_requirement:
```

## 9.5 BaselineManifest

```yaml
baseline_id:
baseline_family:
task_contract:
observables:
data_access:
candidate_space:
resource_budget:
theory_vocabulary_access:
theory_code_access:
decision_path:
independence_level:
```

## 9.6 ExperimentManifest

```yaml
experiment_id:
theory_version:
baseline_versions:
dataset:
dataset_hash:
seed:
metric:
negative_controls:
resource_limits:
start_time:
environment:
```

## 9.7 EvidenceReceipt

```yaml
run_id:
claim_id:
declared_claim:
effective_implementation:
baseline:
matched_conditions:
test_results:
hard_gates:
external_results:
replay_status:
artifact_hashes:
delta:
status:
```

## 9.8 ResidueReport

```yaml
theory_id:
baseline_family:
evidence_set:
retain:
downgrade:
reject:
reconstructible:
unresolved:
residual_claims:
next_tests:
```

---

# 10. 四大 Hard Gates

## 10.1 Source Fidelity Gate

$$
\boxed{
\text{Runtime may not rewrite the source into a better theory silently}.
}
$$

所有 `ENGINEERING_EXTENSION` 都必須可追蹤。

## 10.2 Claim Freeze Gate

在 benchmark 前 freeze：

```text
claim
scope
observable
success criterion
falsifier
metric
```

防止 moving target。

## 10.3 Matched Reconstruction Gate

要求：

$$
\mathcal O_T=\mathcal O_B,
$$

$$
\mathcal D_T=\mathcal D_B,
$$

$$
\mathcal C_T=\mathcal C_B,
$$

且：

$$
\mathcal R_T\approx\mathcal R_B.
$$

## 10.4 Gold Firewall Gate

若：

$$
y^{*}
$$

是 gold，則 `Decision` 不得依賴 $y^{*}$。

將：

$$
y^{*}
\rightarrow
\tilde y
$$

若 decision 改變，記：

```text
GOLD_LEAKAGE
```

## 10.5 Fresh Replay Gate

最終結論不能只依賴：

> 原 session 跑過了。

必須：

```text
freeze artifacts
package
extract fresh
rebuild environment
rerun
verify hashes
rerun tests
rerun benchmark
```

---

# 11. Independent Path Gate

故意破壞 theory helper：

$$
h_T\rightarrow\bot.
$$

baseline 仍需正常執行。

反向也要測：

$$
h_B\rightarrow\bot
$$

不能讓 theory path 同時壞。

---

# 12. Negative Control Gate

每個核心 invariant 至少需要：

```text
positive fixture
negative fixture
expected failure
oracle
```

如果永遠綠，則：

$$
\boxed{
\text{test discrimination not established}.
}
$$

---

# 13. 三種 Closure

## 13.1 Behavioral Closure

$$
\boxed{
\text{tests pass}.
}
$$

## 13.2 Structural Closure

$$
\boxed{
\text{fresh reconstruction reproduces the pass}.
}
$$

## 13.3 Discriminative Closure

$$
\boxed{
\text{negative controls and matched baselines prove the test can distinguish alternatives}.
}
$$

因此：

$$
\boxed{
\text{Behavioral}
\neq
\text{Structural}
\neq
\text{Discriminative}.
}
$$

---

# 14. AI-as-Judge 的位置

AI 可以評：

- explanation clarity；
- analogy quality；
- possible novel application；
- hypothesis usefulness。

但以下：

- hash；
- source；
- branch；
- gold leakage；
- metric；
- test pass；
- replay；

必須由：

$$
\boxed{
\text{deterministic / structured oracle}
}
$$

判定。

---

# 15. RED → GREEN

任何可執行 claim，先建立：

$$
\text{RED}.
$$

RED 必須真的失敗，不是只寫 test。

GREEN 只做最小修改，避免：

$$
\text{implementation drift}.
$$

若 claim 不適合 code，至少需要：

```text
positive witness
falsifying witness
decision rule
source evidence
```

---

# 16. External Evidence Policy

Runtime 不應把：

$$
\text{synthetic pass}
$$

提升成：

$$
\text{external validity}.
$$

狀態應分：

```text
SyntheticSupported
ExternalSupported
ExternalBlocked
ExternalFailed
NotMeasured
```

`NotMeasured` 與 `Blocked` 都是合法結果。

---

# 17. Data Lineage

每個 dataset 記：

```text
source
version
hash
license
transformations
selection
sample_boundary
```

若只測：

$$
n=20
$$

個樣本，不能說 full dataset passed。

$$
\boxed{
\text{Scope honesty is a hard requirement}.
}
$$

---

# 18. Randomized Stress Test

Runtime 可生成：

$$
N
$$

個 histories。

但 randomized 不等於有資訊。

要確保 scenario coverage：

```text
noise
conflict
ordering
missing
duplicate
retraction
OOD
```

Seed 必須保存。

定義：

$$
\boxed{
C_S
=
\frac{
\text{covered scenario classes}
}{
\text{declared scenario classes}
}.
}
$$

---

# 19. Mutation Testing

可以故意修改：

- gold；
- helper；
- source；
- metric；
- baseline feature；

檢查 gate 是否轉紅。

若故意破壞後仍 PASS，表示：

$$
\boxed{
\text{harness itself is suspect}.
}
$$

---

# 20. Theory-Specific Vocabulary Firewall

若要 blind reconstruction，Baseline Agent 不看：

$$
\text{theory-specific labels}.
$$

因為若 baseline builder 已知道：

> 理論說一定要用 X。

它很可能只是：

$$
\text{rename}(X).
$$

---

# 21. Adversarial Validity Gate

Adversarial Agent 的目標不是：

$$
M(S_T)\uparrow.
$$

而是：

$$
\boxed{
\text{maximize informative divergence}.
}
$$

一個有效反例：

$$
x^{*}
$$

應能：

- 擊穿 universal claim；
- 區分 theory / baseline；
- 暴露 hidden assumption；
- 定位 failure boundary。

而且必須：

$$
x^{*}\in D_{\text{claim}}.
$$

---

# 22. Counterexample Ledger

```text
counterexample_id
claim_id
input
validity_basis
expected
observed
baseline_observed
claim_impact
```

大量隨機 nonsense 若不在 claim domain，沒有認識論價值。

---

# 23. Engineering Extension Budget

為避免把理論越補越強，定義：

$$
\boxed{
B_E
}
$$

為 engineering extension budget。

若 extension 太多，Runtime 應警告：

```text
THEORY_UNDERSPECIFIED
```

定義粗略：

$$
\boxed{
ER
=
\frac{
N_{\mathrm{engineering\ extensions}}
}{
N_{\mathrm{effective\ rules}}
}.
}
$$

高 $ER$ 表示實作成功很大部分可能來自 evaluator。

---

# 24. Model Agreement 不等於 Validation

如果：

$$
A_1,A_2,A_3
$$

都說：

> 理論看起來合理。

仍然：

$$
\boxed{
\text{Agreement}
\neq
\text{Evidence}.
}
$$

多 Agent 若同源，可能形成：

$$
\boxed{
\text{correlated confidence}.
}
$$

因此需要 External Anchor：

- external dataset；
- deterministic test；
- external literature；
- formal solver；
- physical experiment；
- independent reviewer。

---

# 25. Runtime Governance

所有 Agent 都在：

$$
\boxed{
\text{bounded authority}.
}
$$

- Steelman Agent 不能改 source；
- Implementer 不能改 claim；
- Baseline Agent 不能降 resource；
- Judge 不能改 metric；
- Residue Curator 不能 invent evidence。

某些 transition 可要求人類：

```text
approve_claim_freeze
approve_external_scope
approve_physical_cost
approve_publication
```

人類不需要每一步都操作，但應介入高槓桿節點。

---

# 26. Runtime Receipt

一輪完成後：

```text
run_id
theory_id
claim_count
source_hash
artifact_hashes
baseline_count
external_data
test_count
hard_gate_status
fresh_replay_status
delta_vector
residue_count
blocked_items
human_interventions
machine_work
wall_clock
```

接 PTE-02，應同時記：

$$
L_W,
H_A,
M_W,
C_O.
$$

---

# 27. FailureBundle

失敗時保存：

```text
failure_id
claim_id
failure_class
first_divergence
expected
observed
minimal_reproducer
source_refs
baseline_refs
recovery_attempt
```

Failure class 至少區分：

```text
SOURCE_ERROR
INTERPRETATION_ERROR
FORMALIZATION_ERROR
IMPLEMENTATION_ERROR
BASELINE_MISMATCH
GOLD_LEAKAGE
METRIC_ERROR
EXTERNAL_CONTRADICTION
REPLAY_FAILURE
INFRASTRUCTURE_FAULT
```

---

# 28. Versioned Research

修復後：

$$
T_1
$$

不能刪掉：

$$
T_0.
$$

應保留：

$$
\boxed{
T_0
\rightarrow
T_1
\rightarrow
T_2
}
$$

以及每次 evidence transition。

---

# 29. Canonical Frontier

對每個 theory 保存：

```text
current_claim_set
current_evidence
current_baseline_family
current_residue
open_failures
```

Canonical Frontier 不是真理終點，只是：

$$
\boxed{
\text{current best reproducible state}.
}
$$

---

# 30. Stop Rule

AI runtime 若沒有停止條件，可能無限：

- 加 baseline；
- 加 test；
- 加 reinterpretation。

可在以下情況停止：

```text
claim falsified
baseline closure reached
residual stable
external evidence blocked
resource budget exhausted
no new informative divergence
```

若連續：

$$
k
$$

輪：

$$
IG<\epsilon,
$$

可停止。

其中：

$$
\boxed{
IG
=
d(E_{t+1},E_t)
}
$$

表示 epistemic information gain。

---

# 31. Runtime 不追求永久完成

因為新 baseline、data、evidence 都可能重開：

$$
T.
$$

若：

$$
\mathcal E_{new}
$$

足以影響：

$$
R(T),
$$

可以：

```text
CLOSED -> REOPENED
```

---

# 32. Public / Private Boundary

若理論來源包含：

- 私有稿；
- 未公開資料；
- 專利前資料；

Runtime 需保持 source permission。

不能因 baseline search：

$$
\text{private source}
\rightarrow
\text{public artifact}.
$$

---

# 33. 最小可行 PTE-TSR

MVP 可只支援：

```text
Markdown theory
claim extraction
Python implementation
Python baseline
pytest
JSONL dataset
negative controls
fresh ZIP replay
residue report
```

先從：

- AI architecture；
- software theory；
- algorithmic claims；
- semantic systems；

開始。

這些領域適合的原因是：

$$
L_P
\approx
0.
$$

可快速形成 Executable Evidence。

---

# 34. PTE-TSR Conformance Levels

## C0 — Source Integrity

來源、hash、scope 可重建。

## C1 — Claim Integrity

claim freeze、extension label 正確。

## C2 — Behavioral Test

implementation 與 negative controls 可跑。

## C3 — Matched Reconstruction

strong baseline 公平。

## C4 — External / Adversarial

離開 toy domain。

## C5 — Fresh Replay

最終 artifact 可獨立重播。

## C6 — Residue Closure

claim disposition 與 residue report 完整。

只有：

$$
C0-C6
$$

通過，才可說：

> PTE run structurally closed.

仍不能說：

> Theory proven true.

---

# 35. Theory Testing as Compilation

可以把：

$$
T
$$

視為 source language。

編譯鏈：

$$
\boxed{
\text{Theory Text}
\rightarrow
\text{Claim IR}
\rightarrow
\text{Formal IR}
\rightarrow
\text{Executable IR}
\rightarrow
\text{Evidence IR}.
}
$$

每一層都可能有 loss。

定義：

$$
\lambda_i
$$

為語義損失。

因此：

$$
\boxed{
\text{successful execution}
\not\Rightarrow
\text{perfect theory fidelity}.
}
$$

Loss Ledger：

```text
source -> claim loss
claim -> formal loss
formal -> implementation loss
implementation -> metric loss
```

---

# 36. AI 原生科學更深的風險

危險不只是 hallucination。

更深的是：

$$
\boxed{
\text{well-organized self-confirmation}.
}
$$

系統可以非常完整地「證明自己」，如果 source、implementation、baseline、metric、judge 全部由同一閉環控制。

因此 PTE-TSR 的核心不是 intelligence，而是：

$$
\boxed{
\text{epistemic architecture}.
}
$$

---

# 37. 初步研究命題

## TSR-H1：Role Separation Hypothesis

在相同模型能力下，角色分離與 artifact boundary 可降低：

$$
\text{self-confirmation error}.
$$

## TSR-H2：Fresh Replay Hypothesis

只通過原 session test 的研究，其 failure rate 高於 fresh reconstructed replay。

## TSR-H3：Blind Baseline Hypothesis

盲重建 baseline 能降低：

$$
\text{theory vocabulary leakage}.
$$

## TSR-H4：Harness Mutation Hypothesis

能被 mutation 主動打紅的 harness，比永遠綠的 harness 更能預測外部 failure。

## TSR-H5：Residue Stability Hypothesis

若：

$$
R(T)
$$

在多 baseline、多 seed、多 external set 下穩定，則其後續研究優先度應提高。

---

# 38. 最小比較實驗

選：

$$
N
$$

套公開、可程式化理論。

每套執行兩種 runtime：

```text
R0 single-agent integrated
R1 role-separated PTE-TSR
```

比較：

- gold leakage；
- baseline fairness；
- replay success；
- false theory win；
- residue stability；
- human attention。

---

# 39. 主要指標

定義：

$$
\boxed{
FWR
=
\text{False Win Rate}.
}
$$

如果 runtime 宣稱：

$$
\Delta_T>0,
$$

但後來發現：

- weak baseline；
- gold leakage；
- hidden extension；
- replay fail；

即記為 False Win。

另定義：

$$
\boxed{
RP
=
\frac{
\text{valid residual claims}
}{
\text{all residual claims}
}
}
$$

為 Residue Precision；

$$
\boxed{
FRR
=
\frac{
\text{fresh runs reproduced}
}{
\text{runs claimed complete}
}
}
$$

為 Fresh Replay Rate；

$$
\boxed{
HGVR
=
\frac{
\text{hard gate violations}
}{
\text{runs}
}
}
$$

為 Hard Gate Violation Rate。

---

# 40. 制度價值

如果這套 runtime 成熟，任何公開理論都可能先接受：

$$
\boxed{
\text{pre-peer-review executable stress}.
}
$$

它不取代 peer review，而是讓 peer review 少花時間在：

- 明顯 baseline 不公平；
- claim 漂移；
- 無法重現；
- hidden extension；
- toy-only result。

理論作者也可以自己使用，先問：

> 我的 strongest baseline 到底能吃掉多少？

這反而提高理論品質，因為：

$$
R(T)
$$

會更早暴露。

---

# 41. PTE-TSR 與前四篇的關係

PTE-01：

> 怎麼公平假設理論為真？

PTE-02：

> 怎麼把 theory-to-engineering latency 壓低？

PTE-03：

> 怎麼建立 strongest matched reconstruction？

PTE-04：

> 怎麼保存失敗後仍有價值的 residue？

PTE-05 則回答：

> **怎麼把以上方法編成一個 AI 可以反覆執行、但不能輕易自我確認的 runtime？**

---

# 42. PTE-TSR 的最終原則

第一：

$$
\boxed{
\text{Do not automate belief}.
}
$$

第二：

$$
\boxed{
\text{Automate evidence production}.
}
$$

第三：

$$
\boxed{
\text{Automate counterexample pressure}.
}
$$

第四：

$$
\boxed{
\text{Automate reproducibility gates}.
}
$$

第五：

$$
\boxed{
\text{Preserve uncertainty and residue}.
}
$$

---

# 43. 結論：AI 原生科學需要的是可執行懷疑

AI 能讓：

- 理論更快被讀懂；
- 更快被形式化；
- 更快被做成程式；
- 更快被跑上萬次。

但如果沒有：

- source boundary；
- role separation；
- matched baseline；
- negative control；
- gold firewall；
- fresh replay；
- residue ledger；

那麼 AI 也可以更快製造：

$$
\boxed{
\text{highly reproducible self-deception}.
}
$$

因此 AI 原生科學的真正問題不是：

> AI 能不能自己研究？

而是：

> **我們能不能把科學懷疑本身，編譯成 AI 必須服從的執行協議？**

PTE-TSR 的答案是：

$$
\boxed{
\text{Yes, partially}.
}
$$

可以被編譯的包括：

- source integrity；
- claim freeze；
- test contract；
- matched conditions；
- negative controls；
- replay；
- provenance；
- status transition。

仍無法完全自動化的包括：

- 研究重要性；
- 真正新穎性的最終哲學判定；
- 不可觀測 claim；
- 物理證據價值；
- 社會與倫理取捨。

所以 PTE-TSR 不應成為：

$$
\text{Truth Machine}.
$$

而應成為：

$$
\boxed{
\text{Theory Pressure Machine}.
}
$$

它不負責替世界宣布最後答案。

它負責讓：

$$
\text{weak claim},
\text{hidden assumption},
\text{unfair baseline},
\text{unreproducible result}
$$

更難存活。

同時讓：

$$
\boxed{
R_{\mathcal B,\mathcal E}(T)
}
$$

更容易被精確留下。

---

# 44. 下一篇

**PTE-06｜不可壓縮證據底：AI 為何不能把所有科學都變成幾小時實驗**  
*The Irreducible Evidence Floor: Limits of AI-Accelerated Theory Testing*

下一篇將正式區分：

$$
\boxed{
\text{epistemic processing cost}
}
$$

與：

$$
\boxed{
\text{physical evidence cost},
}
$$

並建立：

$$
E_{\min}(T,D),
$$

回答：

> **當 AI 已經能把閱讀、形式化、實作、baseline 與分析壓縮到極短時間後，哪些科學問題仍然必須等待世界本身提供證據？**
