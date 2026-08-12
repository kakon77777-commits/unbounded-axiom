# 可重播的數學 AI 問題治理 Benchmark：錯誤注入、盲測與 Runtime Telemetry

**A Replayable Benchmark for Mathematical-AI Problem Governance: Error Injection, Blinded Evaluation, and Runtime Telemetry**

**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-11

## 摘要

形式定理證明 benchmark 通常以「是否產生可被 proof assistant kernel 接受的證明」作為最終驗證標準。這種驗證對 proof correctness 極其重要，但當 AI 系統同時負責自然語言理解、問題形式化、theorem target 選擇與 proof search 時，僅驗證最終 proof 並不足以回答另一個上游問題：**AI 是否正在證明忠實於原始問題的 theorem target？**

本文提出一套可重播的 **Mathematical-AI Problem Governance Benchmark（MAPG-Bench）** 方法學，用於評估數學 AI 在正式 proof search 前的問題治理能力。Benchmark 不只測試答案或 proof 是否正確，而是測試系統能否偵測 target corruption、避免 premature theorem freeze、保留 clean target、正確分配 problem-audit specialist，並完整保存其決策與 runtime telemetry。

本文的方法學包含五個核心設計：

1. **Error Injection**：對原始數學 target 注入量詞交換、定義域遺漏、錯誤 uniformity、predicate flattening、certificate truncation、source formulation substitution、framework bridge collapse、definition-provenance break 等 corruption；
2. **Clean Controls**：加入未被破壞的 target，以測量 false positive、over-expansion 與「永遠懷疑」問題；
3. **Blinded Evaluation**：將 blind test set 與 answer key 實體分離，並記錄 contamination status；
4. **Replayable Runtime Trace**：保存 source、candidate、prompt、model/version、routing、residual doubt、specialist call、freeze/reject state、raw output 與 hash；
5. **Telemetry Separation**：嚴格區分 structural proxy、synthetic simulation 與 measured runtime evidence。

本文整理 EXP-0001～EXP-0010 的逐步實驗設計，形成從單題概念驗證、跨題壓力測試、target-corruption injection、blind harness、adaptive freeze、VOI routing、runtime telemetry、self-calibration 到 non-stationary drift simulation 的完整方法鏈。這些早期實驗中的多數數值來自人工 annotation、proxy cost 或 synthetic environment；因此本文不將其解讀為真實 LLM 或 Lean prover 的性能提升。

MAPG-Bench 的研究目的不是取代 Formal Conjectures、FormalMATH、TheoremBench 或其他 theorem-proving benchmark，而是補充一個不同的評估層：

$$
\boxed{
\text{Before asking whether AI can prove the theorem,}
\quad
\text{test whether it has stabilized the right theorem.}
}
$$

**關鍵詞：** Mathematical AI Benchmark、Target Fidelity、Error Injection、Blinded Evaluation、Runtime Telemetry、Benchmark Contamination、Formal Theorem Proving、Autoformalization、Reproducibility、Problem-Space Governance

---

## 1. 引言

形式數學 benchmark 的一個巨大優勢，是最終答案可以由 trusted kernel 驗證。

若 AI 產生 proof：

$$
P,
$$

對 theorem：

$$
C,
$$

kernel 可以檢查：

$$
P\vdash C.
$$

這比依賴自然語言 judge 或模糊 correctness score 更可靠。

然而，當 AI 還負責產生 $C$ 時，問題變成：

$$
N
\rightarrow
C
\rightarrow
P.
$$

此時 kernel 驗證：

$$
P\vdash C
$$

不等價於驗證：

$$
C
\equiv
C_{\mathrm{source}}.
$$

2026 年對 Lean theorem-proving benchmark 的大規模 audit 已明確指出：machine-checked proof 只能保證 formal theorem 被證明，並不能保證 theorem statement 忠實編碼 intended informal problem，也不能自動排除 vacuous statements、counterexamples、unsound axioms 或 evaluation-harness defects。[2]

同年，針對 natural-language-to-Lean statement formalization 的研究亦直接將「beyond compilation」作為評估重點：一個 Lean declaration 即使能 type-check，仍可能漏掉 hypothesis、改變 domain 或變成 vacuous claim。[3]

因此，數學 AI benchmark 至少應拆成：

$$
\boxed{
\text{Target Formation}
}
$$

與：

$$
\boxed{
\text{Proof Search}.
}
$$

本文研究前者。

---

## 2. Benchmark 的目標層級

本文提出的 benchmark 不直接回答：

> 哪個 theorem prover 最強？

而是回答：

> **在進入 proof search 前，AI 是否能可靠地治理 theorem target？**

因此評估層可分：

### Layer 0：Source Understanding

$$
N
\rightarrow
\mathcal C_{\mathrm{candidate}}.
$$

### Layer 1：Target Governance

$$
\mathcal C_{\mathrm{candidate}}
\rightarrow
C^\ast_{\mathrm{freeze}}.
$$

### Layer 2：Difficulty / Routing

$$
C^\ast_{\mathrm{freeze}}
\rightarrow
\mathrm{MCDM}
\rightarrow
\mathrm{ResearchRouter}.
$$

### Layer 3：Formal Proof

$$
C^\ast_{\mathrm{freeze}}
\rightarrow
P.
$$

本文 benchmark 的主測量對象是：

$$
\boxed{
L_0+L_1
}
$$

並保存足夠 telemetry，使未來能測：

$$
L_1
\rightarrow
L_3
$$

是否真正降低 proof cost。

---

## 3. 與現有 Formal Benchmark 的互補關係

Formal Conjectures 已提供研究級 Lean conjectures、open/solved problem 分層、frozen evaluation subsets 與 standardized evaluation setup，並明確把 AI proof/disproof 作為 formalization fidelity audit 的一部分。[1]

FormalMATH 則以大規模 Lean4 問題集、multi-LLM semantic verification、negation-based disproof filtering 與 human verification 建立形式數學 benchmark。[6]

TheoremBench 進一步提出 theorem-level coverage 與 token-efficiency 指標，以捕捉 dependency-rich theorem development 中的 partial progress 與 proof inefficiency。[4]

另一方面，T $^2$ 類 evaluation 開始把 successor theorem compatibility 當作 semantic correctness test，顯示單純 compilation success 無法充分測量 generated theorem 的語義品質。[5]

因此，MAPG-Bench 並不是重複上述 benchmark。

其測試對象是：

$$
\boxed{
\text{the governance process that produces the target consumed by those benchmarks/provers}.
}
$$

---

## 4. Benchmark Unit

每一個 benchmark instance 不只是 theorem statement。

我們定義：

$$
B_i
=
(
S_i,
C_i,
K_i,
M_i
),
$$

其中：

- $S_i$：Source Context；
- $C_i$：Candidate Target；
- $K_i$：Gold Governance Metadata；
- $M_i$：Runtime / Evaluation Metadata。

其中：

$$
K_i
$$

在 blind evaluation 時不得提供給 tested agent。

---

## 5. Source Context

Source Context 不應只是一句 paraphrase。

至少可包含：

- 原始自然語言 problem；
- 必要 definitions；
- source formulation hierarchy；
- proof-relevant boundary；
- source version；
- formal repository path；
- paper / issue identifier；
- benchmark target declaration。

但 benchmark 不應偷偷加入 gold answer。

因此：

$$
\boxed{
\text{Source Context}
\neq
\text{Answer Key}.
}
$$

---

## 6. Candidate Target

Candidate Target 是被審計的對象：

$$
C_i^{\mathrm{candidate}}.
$$

它可能：

1. clean；
2. corrupted；
3. ambiguous；
4. stronger variant；
5. weaker variant；
6. formally valid but source-infaithful。

Agent 任務不是「猜 benchmark 作者想要什麼」，而是比較：

$$
C_i^{\mathrm{candidate}}
$$

與：

$$
S_i.
$$

---

## 7. Error Injection

我們提出 controlled corruption injection。

令 clean target：

$$
C.
$$

注入 operator：

$$
\Gamma_k.
$$

得到：

$$
C'_k
=
\Gamma_k(C).
$$

要求：

$$
\Gamma_k
$$

具有明確 corruption semantics。

---

## 8. Corruption Taxonomy

第一版 benchmark 至少包含十類：

$$
\begin{aligned}
\Gamma_1 &: \text{Quantifier Swap},\\
\Gamma_2 &: \text{Domain Omission},\\
\Gamma_3 &: \text{Unnecessary Uniformity},\\
\Gamma_4 &: \text{Predicate Flattening},\\
\Gamma_5 &: \text{Certificate Truncation},\\
\Gamma_6 &: \text{Asymptotic-to-Finite Collapse},\\
\Gamma_7 &: \text{Wrong Source Formulation},\\
\Gamma_8 &: \text{Framework Bridge Collapse},\\
\Gamma_9 &: \text{Definition Substitution without Provenance},\\
\Gamma_{10} &: \text{Representation Coverage Failure}.
\end{aligned}
$$

每類應保存：

- clean source；
- corruption transform；
- corrupted candidate；
- reason code；
- severity；
- required detection layer；
- expected proof-search failure mode。

---

## 9. 為何需要 Clean Controls？

只測 corrupted samples 有一個致命問題。

Agent 可以永遠回答：

> 「這個 theorem target 有問題。」

則：

$$
\text{Corruption Recall}=1.
$$

但系統完全不可用。

因此 benchmark 必須同時包含：

$$
\boxed{
\text{Corrupted}
+
\text{Clean}.
}
$$

基本 confusion matrix：

$$
\begin{array}{c|cc}
 & \text{Pred Corrupt} & \text{Pred Clean}\\
\hline
\text{Gold Corrupt} & TP & FN\\
\text{Gold Clean} & FP & TN
\end{array}
$$

並計算：

$$
\text{Precision},
\quad
\text{Recall},
\quad
\text{Specificity},
\quad
\text{Accuracy},
\quad
F_1.
$$

---

## 10. Governance-Specific Metrics

傳統 classification metrics 還不夠。

### 10.1 False Freeze Rate

$$
\operatorname{FFR}
=
\frac{
\text{corrupted targets frozen}
}{
\text{all corrupted targets}
}.
$$

這是高風險指標。

### 10.2 Clean Freeze Rate

$$
\operatorname{CFR}
=
\frac{
\text{clean targets correctly frozen}
}{
\text{all clean targets}
}.
$$

用來防止 over-skepticism。

### 10.3 Over-Expansion Rate

$$
\operatorname{OER}
=
\frac{
\text{unnecessary specialist calls}
}{
\text{all audit specialist calls}
}.
$$

### 10.4 Target Repair Success

若 corruption 被發現後允許 repair：

$$
\operatorname{TRS}
=
P(
C_{\mathrm{repaired}}
\equiv
C_{\mathrm{gold}}
).
$$

### 10.5 Freeze Delay

$$
L_{\mathrm{freeze}}
=
t_{\mathrm{freeze}}
-
t_0.
$$

可用 module calls、tokens 或 wall time 表示。

---

## 11. Blind Evaluation

正式 blind evaluation 必須做到：

$$
\boxed{
\text{Test Input}
\perp
\text{Gold Label}.
}
$$

實體檔案至少分：

```text
blind_test_cases.jsonl
answer_key_DO_NOT_GIVE_TO_AGENT.json
```

Agent 只看到：

- opaque sample ID；
- source context；
- candidate target。

不能看到：

- is_corrupted；
- corruption type；
- severity；
- gold detector；
- reference explanation。

---

## 12. Conversation Contamination

對 interactive AI 特別重要。

如果同一模型在前一輪已經看到：

$$
K_i,
$$

下一輪即使移除 answer key，也不是 blind。

因此每次 run 應標記：

$$
\boxed{
\operatorname{ContaminationStatus}
}
$$

例如：

- CLEAN_SESSION；
- POSSIBLE_MEMORY_CONTAMINATION；
- EXPLICIT_PRIOR_EXPOSURE；
- CONTAMINATED_CONTROL。

任何已看過 gold data 的模型結果：

$$
\boxed{
\text{不得計入正式 blind score}.
}
$$

---

## 13. Benchmark Contamination 的更一般問題

公開 LLM benchmark 存在 training-data contamination 風險。AntiLeakBench 透過明確的新知識構造動態樣本，嘗試建立 contamination-resistant evaluation；2025 年對 benchmark mitigation 的系統研究則指出，單純改寫題目往往難以同時保留 fidelity 與 contamination resistance。[7][8]

更廣泛的 survey 也指出，benchmarking 正逐步由 static evaluation 走向 dynamic evaluation，但 dynamic benchmark 本身仍缺乏統一設計與評估標準。[9]

因此 MAPG-Bench 不宣稱公開 source problems 可以保證 training-contamination-free。

我們區分：

$$
\boxed{
\text{Training Contamination}
}
$$

與：

$$
\boxed{
\text{Evaluation-Session Contamination}.
}
$$

前者通常難以完全觀測；

後者可以透過 experiment protocol 嚴格控制。

---

## 14. Dynamic / Fresh Benchmark Layer

未來 benchmark 可以加入：

$$
B_t
$$

表示時間 $t$ 才生成的 corruption variant。

例如：

- 新 Formal Conjectures issue；
- 新 formalization revision；
- 自動生成但 human-audited 的 quantifier perturbation；
- 新 definition-provenance break；
- 新 source-version swap。

其目標不是保證：

$$
P(\text{training contamination})=0,
$$

而是降低 benchmark memorization 的影響，並增加 audit generalization 測試。

---

## 15. Replayability

每一次 run 必須可重播。

最小 run identity：

$$
R
=
(
E,
S,
M,
P,
T,
V
),
$$

其中：

- $E$：experiment version；
- $S$：sample；
- $M$：model；
- $P$：prompt；
- $T$：tool environment；
- $V$：runtime version。

---

## 16. Model / Prompt Versioning

至少保存：

```yaml
provider:
model_name:
model_version:
endpoint_class:
temperature:
seed:
system_prompt_hash:
user_prompt_hash:
tool_policy_version:
```

如果 provider silent-updates model：

$$
M_t
\neq
M_{t+1},
$$

卻仍叫同一 model name，

則 benchmark 必須至少保存：

- execution timestamp；
- endpoint metadata；
- observable version string；
- response ID / run ID。

否則結果無法嚴格比較。

---

## 17. Input / Output Hashing

所有 source / prompt / output 可保存：

$$
h(x)
=
\operatorname{SHA256}(x).
$$

用於確認：

- benchmark input 是否一致；
- prompt 是否被修改；
- raw output 是否被後處理；
- dataset 是否被重新生成。

但 hash 不是 semantic identity proof。

因此：

$$
\boxed{
\text{Hash Equality}
\Rightarrow
\text{Byte Equality},
}
$$

但不代表：

$$
\text{Semantic Equivalence}.
$$

---

## 18. Runtime Telemetry

Benchmark 不能只保存 final label。

至少保存每個 module event：

$$
e_t.
$$

其 schema 應包括：

### Identity

- experiment ID；
- run ID；
- sample ID；
- event ID；
- parent event ID。

### Event State

- event type；
- module；
- target status；
- timestamp。

### Model

- provider；
- model；
- version；
- temperature；
- seed。

### Epistemic State

$$
D_{\mathrm{before}},
\qquad
D_{\mathrm{after}}.
$$

### Routing

- candidate modules；
- VOI scores；
- selected specialist；
- selection reason。

### Usage

- prompt tokens；
- completion tokens；
- reasoning tokens；
- cached tokens；
- tool calls。

### Latency

- wall time；
- TTFT；
- queue time。

### Proof

- premises retrieved；
- proof branches；
- search nodes；
- tactic steps；
- elaboration failures；
- proof attempts；
- prover time；
- success；
- certificate hash。

---

## 19. Raw Telemetry 優先原則

Benchmark 必須保存 raw metrics。

可以再定義：

$$
C
=
\sum_i
w_i m_i,
$$

但：

$$
\boxed{
C
\text{ 只是 view，不是原始資料。}
}
$$

因為：

$$
w_i
$$

可以依：

- API pricing；
- hardware；
- research objective；
- deployment constraints；

改變。

因此：

$$
\boxed{
\text{Raw}
\rightarrow
\text{Normalize}
\rightarrow
\text{Composite}
}
$$

而非：

$$
\text{Raw}
\rightarrow
\text{Composite}
\rightarrow
\text{discard Raw}.
$$

---

## 20. Synthetic、Proxy 與 Measured 必須分層

本文提出三層 evidence taxonomy。

### Level P：Proxy

例如：

$$
1\text{ module call}=1\text{ cost unit}.
$$

只能說明結構。

### Level S：Synthetic

由人工定義：

- hidden capability；
- cost distribution；
- drift；
- task mix。

可測 controller dynamics。

### Level M：Measured

來自：

- 真實模型 API usage；
- 真實 latency；
- 真實 tool logs；
- 真實 Lean search；
- 真實 verifier output。

只有 Level M 可用於實際 performance claims。

因此：

$$
\boxed{
P\neq S\neq M.
}
$$

---

## 21. 禁止 Synthetic Leakage

任何 synthetic event 應標：

```yaml
tags:
  - synthetic
```

Aggregator 預設不得把：

$$
\text{synthetic}
$$

與：

$$
\text{measured}
$$

混合。

若要畫圖比較，必須分 panel 或明示來源。

---

## 22. EXP-0001：單題概念驗證

EXP-0001 以 Monty Hall 為案例，比較：

1. Compact-only；
2. MPF-only；
3. MPF + NLU + Doubt/Tolerance。

主要目的不是測勝率，而是確認：

- host protocol；
- knowledge state；
- framework bridge；
- decision target；

是否能被不同 analysis layer 顯式化。

此實驗建立第一版：

$$
\boxed{
\text{Formal Contraction}
\leftrightarrow
\text{Semantic Expansion}.
}
$$

---

## 23. EXP-0002：跨題壓力測試

加入多種 Formal Conjectures case：

- quantifier-heavy；
- asymptotic；
- certificate；
- source-formulation；
- clean explicit target。

目的：

$$
\boxed{
\text{測 controller 何時應擴張、何時應收斂。}
}
$$

此時首次明確出現：

- CONTRACT_EARLY；
- EXPAND_PREDICATE；
- EXPAND_TARGET_FAMILY；
- CONTRACT_TO_CERTIFICATE。

---

## 24. EXP-0003：Target Corruption Injection

建立：

$$
9\text{ corrupted}
+
4\text{ clean controls}.
$$

注入：

- protocol omission；
- framework collapse；
- quantifier swap；
- predicate flattening；
- certificate truncation；
- uniformity strengthening；
- wrong source formulation；
- domain omission；
- asymptotic-to-finite collapse。

此實驗的數字來自 framework-derived manual labels，因此只能稱：

$$
\boxed{
\text{theoretical detectability / rule-based simulation}.
}
$$

---

## 25. EXP-0004：Blind Harness

將：

```text
blind_test_cases.jsonl
```

與：

```text
answer_key_DO_NOT_GIVE_TO_AGENT.json
```

完全分離。

並建立三種 system prompts：

- A：Baseline；
- B：MPF；
- C：Dual-Tension。

此環境當時沒有獨立第二模型，因此沒有冒充真正 blinded result，而是把已看過答案的當前模型明確標記：

$$
\boxed{
\texttt{CONTAMINATED\_CONTROL}.
}
$$

這一點是整個 benchmark methodology 的必要紀律。

---

## 26. EXP-0005：Freeze Controller Proxy Test

比較：

- Surface-only；
- Always-MPF；
- Always-Dual；
- Adaptive Controller。

用：

$$
1\text{ audit module call}
$$

作 proxy cost。

結果只能解讀為：

> Adaptive controller 在該人工 development set 上啟動較少分析模組。

不能解讀為：

> 實際 token / latency 下降相同比例。

---

## 27. EXP-0006：Holdout-Style Test

先 freeze controller policy，再換新來源問題。

目的：

$$
\boxed{
\text{避免只在設計集上自洽。}
}
$$

但 corruption variant 與 gold requirement 仍由 analyst 生成，

所以屬：

$$
\boxed{
\text{holdout-style}
}
$$

而不是 fully independent blind benchmark。

---

## 28. EXP-0007：VOI Scheduler

引入 proxy cost：

$$
C(M_i)
$$

與 residual-doubt reduction：

$$
R_i(D).
$$

再：

$$
\operatorname{VOI}
=
\frac{\mathbb E[\Delta D]}{C}.
$$

測試：

$$
\text{Always-Dual}
\quad
vs
\quad
\text{Rule Adaptive}
\quad
vs
\quad
\text{VOI Scheduler}.
$$

所有結果仍為 simulation。

---

## 29. EXP-0008：Telemetry Contract

正式建立：

- JSON schema；
- recorder；
- aggregator；
- cost-model interface；
- model/prover adapter；
- synthetic telemetry plumbing test。

此實驗的主要產物不是 performance number，而是：

$$
\boxed{
\text{measurement infrastructure}.
}
$$

---

## 30. EXP-0009：Self-Calibration Plumbing

利用 synthetic telemetry 估：

$$
\widehat C_t(M),
\qquad
\widehat R_t(M).
$$

並加入：

$$
\widehat{\operatorname{VOI}}
+
\beta U.
$$

目的：

- 驗證 posterior / shrinkage update；
- 驗證 exploration；
- 驗證 uncertainty 隨 observations 下降。

仍不屬 measured evidence。

---

## 31. EXP-0010：Non-Stationary Stress Test

故意改變 hidden specialist：

- cost；
- capability；
- model-like behavior。

比較：

- stationary mean；
- EWMA；
- change-point reset。

並增加：

- parameter recovery delay；
- false alarm；
- missed shift；
- regret。

此實驗驗證 drift-aware controller logic，但完全位於 synthetic environment。

---

## 32. 一張 Evidence Ledger

每個 experiment 都應附：

| Field | Example |
|---|---|
| Evidence Level | Proxy / Synthetic / Measured |
| Gold Source | Human / Formal / Synthetic |
| Blind? | Yes / No |
| Model Isolated? | Yes / No |
| Contamination Risk | Low / Medium / High / Known |
| Runtime Measured? | Yes / No |
| Formal Verifier Used? | Yes / No |
| Reproducible Input Hash | Yes / No |

如此可以避免：

> 後續整理時忘記某個 100% 是 synthetic simulation 的 100%。

---

## 33. Formal Verification 與 Benchmark Verification 是兩回事

形式 proof：

$$
P\vdash C
$$

可以由 Lean 驗證。

但 benchmark claim：

> 「這個 case 是 clean。」

> 「這個 corruption 屬 quantifier swap。」

> 「這個 source target 忠實。」

不一定能由 Lean 直接驗證。

因此 benchmark 需要兩種 gold：

### Formal Gold

machine-checkable。

### Semantic / Governance Gold

由：

- source evidence；
- human expert；
- cross-model review；
- formal implication/equivalence proof；

組成。

這也是近期 formalization benchmark 開始引入 cross-model semantic judging 與 human expert calibration 的原因之一。[3]

---

## 34. Gold Label Confidence

Gold 不應永遠當成神諭。

可以記：

$$
G_i
=
(
y_i,
q_i,
s_i
),
$$

其中：

- $y_i$：label；
- $q_i$：confidence；
- $s_i$：evidence source。

例如：

```yaml
gold_label: quantifier_swap
gold_confidence: 1.0
gold_basis:
  - source formal statement
  - direct quantifier comparison
```

或：

```yaml
gold_label: wrong_source_formulation
gold_confidence: 0.8
gold_basis:
  - source paper
  - repository issue
  - human review
```

---

## 35. Benchmark Versioning

Benchmark 應有：

$$
B^{(v1)},
B^{(v2)},\ldots
$$

若某 formalization 被修正：

$$
C_i^{v1}
\rightarrow
C_i^{v2},
$$

不能偷偷覆蓋舊資料。

應記：

- old version；
- new version；
- correction reason；
- affected runs；
- leaderboard impact。

這與 Formal Conjectures 的 evolving benchmark 精神相容：benchmark fidelity 可以透過社群與 AI proof/disproof feedback 持續改善。[1]

---

## 36. Frozen Evaluation Subsets

對可比較 benchmark，應建立：

$$
B_{\mathrm{frozen}}^{(t)}.
$$

在評測期間：

- sample 不改；
- gold 不改；
- scoring 不改。

新 correction 進：

$$
B_{\mathrm{next}}.
$$

避免：

> 不同團隊其實跑的是不同 benchmark revision。

---

## 37. Dynamic Evaluation 與 Frozen Evaluation 可以並存

Frozen subset 提供：

$$
\boxed{
\text{comparability}.
}
$$

Dynamic layer 提供：

$$
\boxed{
\text{freshness / lower memorization risk}.
}
$$

所以完整 benchmark：

$$
\boxed{
B
=
B_{\mathrm{frozen}}
\cup
B_{\mathrm{dynamic}}.
}
$$

兩者分開報分數。

---

## 38. 評分不應只有一個 Accuracy

建議 leaderboard 顯示至少：

### Target Safety

- Corruption Recall；
- False Freeze Rate；
- Clean Freeze Rate。

### Diagnosis

- Reason Code Accuracy；
- Corruption Type F1。

### Repair

- Target Repair Success。

### Efficiency

- tokens；
- latency；
- specialist calls；
- tool calls。

### Downstream

- proof success；
- proof nodes；
- premise retrieval；
- elaboration failures。

### Calibration

- confidence calibration；
- VOI calibration。

---

## 39. Pareto 而非單分數

安全與成本常互相衝突。

因此不應直接：

$$
Score
=
Accuracy-\lambda Cost
$$

然後只公布一個數字。

更合理是：

$$
\boxed{
\text{Pareto Frontier}
}
$$

例如：

$$
(
\text{False Freeze},
\text{Corruption Recall},
\text{Tokens},
\text{Latency}
).
$$

若需要 operational policy，才在特定 deployment constraint 下選：

$$
\lambda.
$$

---

## 40. Proof-Downstream A/B/C Test

最關鍵的最終實驗不是只測 target audit。

同一 source problem：

### A

$$
\text{Direct Proof}.
$$

### B

$$
\text{MPF}
\rightarrow
\text{Proof}.
$$

### C

$$
\text{Dual-Tension / TFC / DDRA}
\rightarrow
\text{Freeze}
\rightarrow
\text{Proof}.
$$

固定：

- base model；
- model version；
- proof tools；
- token budget；
- wall-clock budget；
- Lean version；
- mathlib revision。

測：

$$
P_{\mathrm{success}},
$$

$$
T_{\mathrm{tokens}},
$$

$$
N_{\mathrm{proof-node}},
$$

$$
N_{\mathrm{failed-branch}}.
$$

這才真正能回答：

> 上游 problem governance 是否降低 downstream formal proof cost？

---

## 41. 不應把 Proof Failure 都歸因於 Target

即使 C 模式 proof 失敗：

$$
\text{Fail}
$$

也可能因：

- prover weakness；
- missing lemma；
- search budget；
- library mismatch。

因此：

$$
\boxed{
\text{Proof Failure}
\neq
\text{Target Governance Failure}.
}
$$

反之 proof success 也不保證 target governance 成功。

所以 Layer 1 與 Layer 3 分開評分。

---

## 42. Benchmark Harness Requirements

正式 harness 至少需要：

1. deterministic sample loader；
2. answer-key isolation；
3. prompt versioning；
4. model metadata；
5. raw output storage；
6. parsing log；
7. telemetry recorder；
8. timeout log；
9. exception log；
10. scorer；
11. hash manifest；
12. environment manifest。

---

## 43. Reproducibility Package

一個發布版本至少：

```text
benchmark/
  frozen/
  dynamic/
  schemas/
  prompts/
  answer_keys/
  scorer/
  runner/
  telemetry/
  manifests/
  hashes/
  docs/
```

並提供：

```text
README
LICENSE
VERSION
CHANGELOG
```

---

## 44. Agent Benchmark 的可重播性

Agent benchmark 比純 static QA 更難重現。

因為 outcome 依賴：

- tool state；
- external network；
- API version；
- environment；
- time；
- retries；
- intermediate actions。

OpenProver 類 agentic theorem-proving 系統強調以 Lean 4 formal verification 與開源 workflow 支援 reproducible evaluation，也顯示 agent workflow 本身正在成為 theorem proving 評估的一部分。[10]

因此 MAPG-Bench 的 replayability 必須保存：

$$
\boxed{
\text{trajectory}
}
$$

而不只是 final answer。

---

## 45. Trajectory-Level Evaluation

令 trajectory：

$$
\tau
=
(s_0,a_0,s_1,a_1,\ldots,s_T).
$$

可評：

- 是否過早 Freeze；
- 是否重複調用同類 specialist；
- 是否在 fatal doubt 未清除時進 proof；
- 是否因 false alarm 無限擴張；
- 是否遵守 hard closure。

因此：

$$
\boxed{
\text{Outcome Score}
+
\text{Process Score}.
}
$$

---

## 46. Replay vs. Re-execution

需要區分：

### Replay

用已保存 trajectory 重算：

- scoring；
- cost；
- VOI；
- metrics。

### Re-execution

重新呼叫模型與工具。

因模型/API 可能漂移：

$$
\boxed{
\text{Replay}
\text{ 通常比 }
\text{Re-execution}
\text{ 更可重現}.
}
$$

所以 raw trajectory 是一級研究資料。

---

## 47. Benchmark Defect Audit

Benchmark 本身也需要被測。

2026 年對五個 Lean theorem-proving benchmark 的 audit 發現大量 dataset / evaluation findings，進一步說明「benchmark 是 formal 的」並不代表 benchmark 本身不需要 corpus-scale 檢查。[2]

因此 MAPG-Bench 應提供：

- duplicate detection；
- vacuity checks；
- contradiction checks；
- hypothesis-use checks；
- source-target consistency audit；
- answer-key leakage scan；
- file/hash integrity check。

---

## 48. Successor / Integration Testing

T $^2$ 類工作提出一個有價值的方向：generated theorem 的語義品質可以透過它是否能維持 downstream successor theorems 來測試。[5]

MAPG-Bench 可加入：

$$
\boxed{
\text{Downstream Compatibility Test}.
}
$$

如果 AI repair theorem target：

$$
C
\rightarrow
C',
$$

則重新跑依賴：

$$
\{T_1,\ldots,T_k\}.
$$

若大量 successor break：

$$
\operatorname{FidelityRisk}(C')\uparrow.
$$

這不能完全取代 semantic audit，但可作強力自動化訊號。

---

## 49. Benchmark Contamination 與 Fidelity 的張力

防 contamination 的改寫可能改變問題。

2025 年 contamination-mitigation 研究特別提出：

$$
\boxed{
\text{Fidelity}
\leftrightarrow
\text{Contamination Resistance}
}
$$

的張力，並指出許多 mitigation strategy 無法同時取得兩者。[8]

這與本文高度相關。

若我們為了生成「新題」而對 theorem 做 transformation：

$$
C
\rightarrow
C',
$$

必須再次做：

$$
\operatorname{TargetFidelityAudit}(C,C').
$$

否則 anti-leak benchmark 本身會製造 target corruption。

---

## 50. Dynamic Corruption Generator

未來可以自動生成：

$$
\Gamma_k(C).
$$

但每個 generator 必須：

1. 產生 candidate；
2. 自動保存 transform log；
3. 產生 expected corruption class；
4. 經 human / formal audit；
5. 通過 non-triviality test；
6. 才進 benchmark。

因此：

$$
\boxed{
\text{Generated Benchmark}
\neq
\text{Automatically Trusted Benchmark}.
}
$$

---

## 51. 人工標註與形式標註的分工

Human expert 適合：

- source intent；
- formulation hierarchy；
- pragmatic / contextual fidelity。

Formal tooling 適合：

- quantifier comparison；
- implication proof；
- counterexample；
- satisfiability / vacuity；
- dependency testing。

LLM judges 可用：

- triage；
- candidate explanation；
- disagreement discovery。

但不能讓：

$$
\boxed{
\text{same model}
}
$$

同時：

- 生成 candidate；
- 生成 gold；
- 評自己。

否則 circularity 過高。

---

## 52. Inter-Rater Disagreement

如果 semantic gold 由多 reviewer 建立，

應保存：

$$
y_1,y_2,\ldots,y_k.
$$

而不是只留 consensus。

可計：

$$
\kappa,
$$

或其他 agreement metric。

高 disagreement case 應標：

$$
\boxed{
\text{Ambiguous Gold}.
}
$$

而不是硬塞成 deterministic label。

---

## 53. Problem Definition Instability

若多個合法 candidate：

$$
\mathcal C
=
\{C_1,\ldots,C_k\},
$$

則 benchmark gold 可能就是：

$$
\boxed{
\text{EXPAND / RETURN FAMILY}.
}
$$

而不是：

$$
\text{FREEZE one target}.
$$

這使 benchmark 能測：

> AI 是否知道「現在還不該只選一個答案」。

---

## 54. Evidence-Ready Output

每個 run 應能生成一個 evidence bundle：

```yaml
sample_id:
source_hash:
candidate_hash:
model:
prompt_hash:
decision:
reason_code:
confidence:
specialist_trace:
target_state_trace:
token_usage:
latency:
proof_metrics:
raw_output_hash:
contamination_status:
evidence_level:
```

這使 result 可以被：

- audit；
- replay；
- re-score；
- compare；
- archive。

---

## 55. 建議的 Benchmark Release Tiers

### Tier 0 — Structural

只發布：

- schema；
- corruption taxonomy；
- synthetic examples。

### Tier 1 — Human-Audited Static

有 frozen clean/corrupt samples。

### Tier 2 — Blinded Agent Benchmark

answer key 隔離。

### Tier 3 — Runtime Measured

加入 tokens / latency / tools。

### Tier 4 — Formal-Prover Coupled

加入 Lean downstream A/B/C。

### Tier 5 — Dynamic / Continual

新問題、新 corruption、新 model drift。

---

## 56. Minimum Reporting Standard

任何論文引用 MAPG-Bench 結果時至少報：

1. benchmark version；
2. subset；
3. model；
4. model execution date；
5. prompt version；
6. tool permissions；
7. context / memory policy；
8. contamination status；
9. evidence level；
10. number of runs；
11. token / time budget；
12. metric definitions。

缺其中核心欄位，不應聲稱可直接與其他工作比較。

---

## 57. Statistical Reporting

如果模型具 stochasticity：

$$
Y\sim P_\theta,
$$

單次 run 不足。

至少報：

$$
\bar x,
\quad
s,
\quad
n,
$$

最好有 confidence interval。

對 paired A/B/C：

$$
\Delta_i
=
Y_i^C-Y_i^A
$$

應優先使用 paired analysis，因為 sample difficulty 差異很大。

---

## 58. Benchmark Integrity

每個 release 建立：

$$
\operatorname{SHA256SUMS}.
$$

並保存：

- file hash；
- manifest hash；
- scorer hash；
- prompt hash。

如果 gold 被修改：

$$
h_{\mathrm{gold}}^{v1}
\neq
h_{\mathrm{gold}}^{v2}.
$$

如此能確認 benchmark revision。

---

## 59. 開放 Benchmark 與私有 Blind Set 的張力

完全公開：

$$
\Rightarrow
\text{reproducible}
$$

但：

$$
\Rightarrow
\text{future contamination risk}.
$$

完全私有：

$$
\Rightarrow
\text{lower leakage}
$$

但：

$$
\Rightarrow
\text{lower transparency}.
$$

因此可使用：

$$
\boxed{
\text{Open Training / Dev}
+
\text{Frozen Public}
+
\text{Private Rotating Test}.
}
$$

但 private test 必須有第三方 governance，否則不可審計。

---

## 60. 與 Formal Conjectures「零污染」概念的關係

Formal Conjectures 將未解研究 conjectures 作為一種特殊的低 contamination / zero-solution-contamination signal：模型不可能在訓練資料中見過其尚不存在的正確 proof。[1]

但這與 statement memorization 不同。

模型仍可能見過：

$$
C_{\mathrm{source}}.
$$

所以 MAPG-Bench 的 target-governance 任務仍需要：

- variant freshness；
- blind perturbation；
- source–candidate comparison。

兩類 benchmark 可以互補。

---

## 61. 「沒有 proof」也是有價值的資料

在問題治理 benchmark 中：

$$
\operatorname{REJECT\_TARGET}
$$

可能是正確答案。

同樣：

$$
\operatorname{EXPAND}
$$

可能比：

$$
\operatorname{FREEZE}
$$

更正確。

所以 success 不等於：

$$
\text{always produce theorem}.
$$

這和一般 answer-only benchmark 有根本差異。

---

## 62. Benchmark 的核心輸出不是答案，而是決策

最小 governance response：

```json
{
  "flag_corruption": true,
  "decision": "REJECT_TARGET",
  "reason_code": "QUANTIFIER_SWAP",
  "confidence": 0.97
}
```

進階 response：

```json
{
  "decision": "EXPAND",
  "unresolved": [
    "host policy",
    "probability framework"
  ],
  "next_specialist": "MPF",
  "freeze_eligible": false
}
```

---

## 63. Scorer Design

Scorer 不應只 regex 看 reason string。

至少：

- JSON schema validation；
- decision exact match；
- corruption flag；
- normalized reason code；
- optional semantic explanation scoring；
- trajectory consistency。

例如：

若：

```json
flag_corruption = false
decision = REJECT_TARGET
```

則 internal inconsistency。

---

## 64. Benchmark Replay

保存所有：

$$
\tau_i.
$$

未來若 metric 更新：

$$
m^{v1}
\rightarrow
m^{v2},
$$

可直接：

$$
m^{v2}(\tau_i)
$$

重新評分，

不必重新花 API 成本。

這是 telemetry-first benchmark 的重要價值。

---

## 65. Runtime Drift 與 Benchmark Drift 分離

Model drift：

$$
M_t\neq M_{t+1}.
$$

Benchmark drift：

$$
B_t\neq B_{t+1}.
$$

兩者不能同時無紀錄改變。

否則 performance change：

$$
\Delta Y
$$

無法 attribution。

因此 experiment manifest 必須同時 freeze：

$$
(M,B,P,T).
$$

---

## 66. Benchmark Harness 也要測試

Runner / scorer 是軟體。

因此也可能有 bug。

應建立 unit tests：

- clean sample；
- corrupted sample；
- invalid JSON；
- timeout；
- duplicate ID；
- missing label；
- contradictory answer key；
- scorer edge case。

formal benchmark evaluation harness 的 defect audit 已顯示，評測邏輯本身並非天然可靠。[2]

---

## 67. Threats to Validity

### 67.1 Analyst-Designed Corruptions

人工 corruption 可能過於符合 framework vocabulary。

### 67.2 Prompt Overfitting

specialist prompt 可能直接提示 corruption class。

### 67.3 Small Sample Bias

早期 EXP 樣本數小。

### 67.4 Source Selection Bias

Formal Conjectures case 並非隨機抽樣整個數學世界。

### 67.5 Synthetic Cost Bias

proxy / synthetic cost 不等於 real inference economics。

### 67.6 Model Familiarity

模型可能已看過公開 conjecture。

### 67.7 Gold Imperfection

semantic source fidelity 可能有 reviewer disagreement。

### 67.8 Tool Availability

web / Lean / retrieval access 會大幅改變結果。

### 67.9 Temporal Instability

provider model silent update 造成難以重現。

### 67.10 Benchmark Gaming

公開 taxonomy 後，agent 可專門針對 reason-code pattern 過擬合。

---

## 68. 對 Benchmark Gaming 的防禦

可使用：

1. unseen corruption compositions；
2. multi-corruption samples；
3. clean near-neighbor controls；
4. dynamic source formulations；
5. hidden transformation templates；
6. explanation consistency；
7. downstream compatibility tests。

例如：

$$
\Gamma_2\circ\Gamma_5(C)
$$

同時做 domain omission + certificate truncation。

---

## 69. Compositional Corruption

真實錯誤通常不是單一類型。

因此高階 benchmark：

$$
C'
=
\Gamma_{i_k}
\circ
\cdots
\circ
\Gamma_{i_1}(C).
$$

測：

- primary reason；
- secondary reason；
- complete diagnosis；
- repair order。

這會比單 label classification 更接近真實 problem governance。

---

## 70. Repair Benchmark

診斷後，要求：

$$
C'
\rightarrow
\widehat C.
$$

再測：

$$
\widehat C
\stackrel{?}{\equiv}
C.
$$

可增加：

$$
\operatorname{EditDistance},
$$

與：

$$
\operatorname{SemanticFidelity}.
$$

目標不是改越多越好，而是：

$$
\boxed{
\text{minimal sufficient repair}.
}
$$

---

## 71. Freeze Benchmark

有些題不是 corrupt，而是 underspecified。

Gold decision：

$$
\operatorname{EXPAND}.
$$

有些題完整：

$$
\operatorname{FREEZE}.
$$

有些題正式錯：

$$
\operatorname{REJECT}.
$$

所以 benchmark action space：

$$
\boxed{
\{
\operatorname{FREEZE},
\operatorname{EXPAND},
\operatorname{CONTRACT},
\operatorname{REJECT}
\}.
}
$$

---

## 72. Routing Benchmark

再下一層：

給：

$$
D_t,
$$

以及 specialists：

$$
\mathcal M.
$$

要求 agent 選：

$$
M^\ast.
$$

gold 不必永遠是一個 module。

可以是：

$$
\mathcal M_{\mathrm{acceptable}}.
$$

因為多條審計路徑可能同樣合理。

---

## 73. Telemetry Benchmark

最終不只測：

$$
\text{decision quality},
$$

也測：

$$
\text{decision efficiency}.
$$

例如：

兩個 agent 都成功修 target，

但：

Agent A：

$$
2\text{ calls}, 4k\text{ tokens}.
$$

Agent B：

$$
12\text{ calls}, 40k\text{ tokens}.
$$

兩者不應被完全視為相同。

---

## 74. Proof-Coupled Benchmark

最終版 MAPG-Bench 應真正接 Lean：

$$
C^\ast
\rightarrow
\operatorname{LeanAgent}.
$$

然後追蹤：

$$
\text{Governance}
\rightarrow
\text{Proof Cost}.
$$

這才會檢驗整個系列最重要的工程假說：

$$
\boxed{
\text{better problem governance}
\Rightarrow?
\text{better proof efficiency}.
}
$$

問號必須保留到實測完成。

---

## 75. 與 TheoremBench 的互補可能

TheoremBench 以 theorem-level coverage 與 token efficiency 觀察長、依賴豐富 theorem 的 proof behavior。[4]

MAPG-Bench 可以在其上游加入：

$$
\boxed{
\text{Target Governance Condition}.
}
$$

同一 theorem：

- clean formal target；
- intentionally corrupted target；
- source formulation variant。

再看 proof agent 是否：

- 盲證；
- 拒絕；
- 修復；
- 識別 target mismatch。

---

## 76. 與 Theory-Scale Autoformalization 的關係

LCS-Bench 類 theory-scale autoformalization 已開始處理數千個 declaration 的 consistency、faithfulness 與 scalability，並引入 concept graph、signature planning、issue tracking、counterexample search 與 human faithfulness review。[11]

MAPG-Bench 的 corruption / provenance / freeze mechanism 可以自然擴展到 theory scale：

不只：

$$
C_i
$$

是否忠實，

也測：

$$
\mathcal G(C_1,\ldots,C_n)
$$

的 dependency / definition identity 是否整體 drift。

---

## 77. Benchmark Governance 自身也需要版本與治理

最後出現一個反身問題：

> 誰治理 problem-governance benchmark？

答案不能是：

> benchmark 作者永遠正確。

因此 benchmark 本身需要：

- issue tracker；
- correction history；
- public audit；
- formal counterexamples；
- disputed gold labels；
- versioned releases。

也就是：

$$
\boxed{
\text{Governance Benchmark}
\text{ itself requires governance}.
}
$$

這不是悖論，而是正常的可校正研究基礎設施。

---

## 78. 系列 EXP-0001～0010 的最終方法鏈

可以總結：

$$
\boxed{
\begin{array}{ll}
0001 &: \text{single-case dual-tension test}\\
0002 &: \text{cross-problem stress test}\\
0003 &: \text{target corruption injection}\\
0004 &: \text{blind harness}\\
0005 &: \text{freeze controller}\\
0006 &: \text{holdout-style routing}\\
0007 &: \text{VOI scheduler}\\
0008 &: \text{runtime telemetry contract}\\
0009 &: \text{self-calibration}\\
0010 &: \text{distribution-shift stress test}
\end{array}
}
$$

其研究成熟度並不相同。

因此：

$$
\boxed{
\text{Experiment Number}
\neq
\text{Evidence Strength}.
}
$$

---

## 79. Evidence Maturity Matrix

可分：

| EXP | Primary Evidence |
|---|---|
| 0001 | structural manual analysis |
| 0002 | cross-case structural annotation |
| 0003 | rule-based corruption simulation |
| 0004 | blind-evaluation harness |
| 0005 | proxy controller simulation |
| 0006 | holdout-style structural test |
| 0007 | proxy VOI simulation |
| 0008 | telemetry plumbing |
| 0009 | synthetic online calibration |
| 0010 | synthetic non-stationary stress |

因此目前最強的 claim 是：

$$
\boxed{
\text{the benchmark/runtime architecture is implementable and replayable}.
}
$$

而不是：

$$
\boxed{
\text{the architecture has already been empirically proven superior}.
}
$$

---

## 80. 可檢驗的總假說

### H1：Governance Safety

Dual-Tension / TFC 應降低：

$$
\operatorname{FalseFreezeRate}.
$$

### H2：Clean Restraint

不應顯著降低：

$$
\operatorname{CleanFreezeRate}.
$$

### H3：Audit Efficiency

Adaptive routing 應降低：

$$
C_{\mathrm{audit}}.
$$

### H4：Proof Efficiency

治理後：

$$
C_{\mathrm{proof}}
$$

應下降。

### H5：Self-Calibration

telemetry-driven routing 應優於 fixed proxy routing。

### H6：Drift Robustness

non-stationary setting 中：

$$
\operatorname{AdaptiveRegret}
<
\operatorname{StationaryRegret}
$$

在適當 drift regime 下成立。

所有這些都需要 measured benchmark。

---

## 81. 最終評估協議

正式版建議：

### Stage A：Target Audit

$$
S,C
\rightarrow
\{
\text{FREEZE},
\text{EXPAND},
\text{CONTRACT},
\text{REJECT}
\}.
$$

### Stage B：Repair

若 reject：

$$
C
\rightarrow
\widehat C.
$$

### Stage C：Freeze

$$
\widehat C
\rightarrow
C^\ast.
$$

### Stage D：Proof

$$
C^\ast
\rightarrow
P.
$$

### Stage E：Replay Audit

保存：

$$
\tau.
$$

重新評：

- fidelity；
- cost；
- downstream proof；
- trajectory。

---

## 82. 討論：為什麼資料保存本身是研究貢獻？

AI benchmark 很容易只留下：

$$
\text{Score}=83.4\%.
$$

但當：

- model 更新；
- prompt 消失；
- benchmark 修正；
- tool 改版；

這個數字可能無法解釋。

本文主張：

$$
\boxed{
\text{Score without trajectory and version metadata is a lossy projection}.
}
$$

因此 evidence-ready benchmark 的核心不是產生更多 score，而是保留：

$$
\boxed{
\text{how the score came into existence}.
}
$$

---

## 83. 從 Benchmark 到 Scientific Instrument

一個成熟 benchmark 不只是題庫。

它更像：

$$
\boxed{
\text{Scientific Instrument}.
}
$$

需要：

- calibration；
- version；
- error model；
- contamination model；
- reproducibility；
- audit trail。

因此 MAPG-Bench 的目標是把 problem-governance evaluation 從：

> 「我們看幾題，覺得這個方法比較好。」

轉成：

$$
\boxed{
\text{versioned, blinded, replayable, telemetry-grounded evaluation}.
}
$$

---

## 84. 結論

本文提出 Mathematical-AI Problem Governance Benchmark 的方法學，將數學 AI 的評測由最終 proof correctness 往上游擴展到 theorem-target formation、corruption detection、freeze control、repair、routing 與 runtime observability。

核心 benchmark unit：

$$
B_i
=
(
S_i,
C_i,
K_i,
M_i
).
$$

核心 corruption injection：

$$
C'
=
\Gamma(C).
$$

核心 blind principle：

$$
\boxed{
\text{Test Input}
\perp
\text{Gold Label}.
}
$$

核心 evidence principle：

$$
\boxed{
\text{Proxy}
\neq
\text{Synthetic}
\neq
\text{Measured}.
}
$$

核心 reproducibility principle：

$$
\boxed{
\text{Preserve raw trajectory before computing aggregate score}.
}
$$

核心 evaluation chain：

$$
\boxed{
\text{Source}
\rightarrow
\text{Candidate}
\rightarrow
\text{Audit}
\rightarrow
\text{Freeze}
\rightarrow
\text{Proof}
\rightarrow
\text{Replay}.
}
$$

本文不把 EXP-0001～0010 的 proxy / synthetic numbers 當成真實性能結論。相反地，這些實驗被視為建立測量儀器前的 calibration steps。

最終，本文提出的 benchmark 問題不是：

$$
\boxed{
\text{Can this AI prove mathematics?}
}
$$

而是在此之前先問：

$$
\boxed{
\text{Can this AI reliably determine what mathematics it is actually supposed to prove?}
}
$$

如果這一層沒有被測量，形式證明越強，錯誤 target 被「完美證明」的風險反而越值得重視。

---

## 參考文獻

1. Firsching, M., Lezeau, P., Mercuri, S., et al. *Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics.* arXiv:2605.13171, 2026. 
2. Ammanamanchi, P. S., Bhat, S., Biderman, S. *Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving.* arXiv:2606.29493, 2026. 
3. Zhang, K., Gallardo Candela, P., Murthy, S., et al. *Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization.* arXiv:2606.31002, 2026. 
4. Pham, Q. V., Karimov, E., Galichin, A., Oseledets, I. *TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics.* arXiv:2606.09450, 2026. 
5. Kim, J., Han, H., Hwang, S.-W. *Benchmarking Testing in Automated Theorem Proving.* ACL Industry Track, 2026. 
6. Yu, Z., Peng, R., Ding, K., et al. *FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models.* arXiv:2505.02735, 2025. 
7. Wu, X., Pan, L., Xie, Y., et al. *AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge.* ACL, 2025. 
8. Sun, Y., Wang, H., Li, D., Wang, G., Zhang, H. *The Emperor’s New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination.* ICML, 2025. 
9. Chen, S., Chen, Y., Li, Z., et al. *Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation.* EMNLP, 2025. 
10. Kripner, M., Straka, M. *OpenProver: Agentic and Interactive Theorem Proving with Lean 4.* arXiv:2607.09217, 2026. 
11. Feng, Y., Pu, F., An, O., et al. *Theory-Scale Auto-Formalization of Logics for Computer Science.* arXiv:2606.26525, 2026. 

---

## 研究狀態聲明

本文中的 MAPG-Bench、error-injection taxonomy、freeze benchmark、evidence-level taxonomy、telemetry contract、replay methodology 與 EXP-0001～0010 實驗鏈屬於本文提出的 benchmark / methodology framework。

其中 EXP-0001～0010 的既有數值主要來自 manual annotation、proxy cost、rule-based simulation 或 synthetic environment，不能引用為真實 LLM 或 Lean prover 的性能提升。

本文的 strongest current claim 是：

$$
\boxed{
\text{problem-governance evaluation can be made structured, blinded, replayable, and telemetry-ready}.
}
$$

真正性能結論必須等到獨立 Agent、固定版本、blinded execution、measured token/latency 與 actual formal prover logs 完成後才能建立。
