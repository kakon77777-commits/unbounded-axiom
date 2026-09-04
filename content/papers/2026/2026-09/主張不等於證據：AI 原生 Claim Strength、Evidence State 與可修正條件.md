---
document_id: "UA-ANPC-A03"
series: "AI-Native Preprint Commons Series"
series_part: 3
version: "0.1"
language: "zh-Hant"
title: "主張不等於證據：AI 原生 Claim Strength、Evidence State 與可修正條件"
english_title: "Claims Are Not Evidence: AI-Native Claim Strength, Evidence State, and Revision Conditions"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / epistemic-governance paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# 主張不等於證據

## AI 原生 Claim Strength、Evidence State 與可修正條件

### AI-Native Preprint Commons Series — Paper 03

---

## 摘要

在 AI 原生研究環境中，最危險的錯誤未必是完全虛構，而是「主張強度」與「實際支持強度」之間發生滑移。有限數值測試可能被提升為全域定理；模擬輸出可能被描述為現實世界證據；歷史二手文獻可能被誤當成一手史料；相關性可能被提升為因果；反事實與 scenario 可能被寫成已發生事實；模型自身的高信心語氣則可能被誤認為研究證據。

本文延續 Paper 02 的 AI-Native Research Coordinate System，提出 **Claim–Evidence Calibration Architecture（CECA）**。CECA 不採用一條跨領域通用的線性「證據等級」，而將研究主張、證據狀態、驗證結果與更新條件分離建模。對任一 claim $c$，本文定義 claim profile、required support profile、actual evidence state、support adequacy relation、promotion witness 與 defeat/revision contract。其核心原則是：

$$
\boxed{
\text{Claim Form}
\neq
\text{Claim Strength}
\neq
\text{Evidence State}
\neq
\text{Validation Result}
\neq
\text{Truth}.
}
$$

本文將既有研究中的 overclaim gap、disconfirmation exposure、update integrity、evidence authority、validation lifecycle 與 failure condition 思想一般化，建立可跨數學、實證科學、工程、歷史、哲學、未來研究與 AI 自主研究使用的 typed evidence system。證據被表示為多維、可含 `UNKNOWN` 與 `NOT_APPLICABLE` 的結構，而非以單一分數假裝不同學科共享同一測量尺度。

本文進一步提出 **Defeat / Revision Conditions** 取代將所有研究強迫塞入單一 Popper 式 falsifiability 欄位。數學命題可以由反例或證明錯誤擊敗；實驗主張可以由測量失效、重現失敗或新證據修正；歷史命題可以由新一手史料或 provenance 衝突更新；哲學與概念研究則可由反例、概念不一致、解釋失敗或競爭框架擊敗。定義本身甚至可能沒有實驗可證偽性，但仍有一致性與使用範圍條件。

CECA 的最終目的，是讓 AI 在研究時既不因語言生成能力而過度自信，也不因無法取得終極證明而過度退縮。平台應允許「目前支持到哪裡，就說到哪裡」，並要求任何向更強主張的升級都具有可審計的 promotion witness；任何負面證據、來源撤回、反例或驗證失敗都必須留下可追蹤的 revision event，而不能被靜默刪除。

**關鍵詞：** Claim Strength、Evidence State、證據校準、可修正性、可證偽性、AI 自主研究、研究驗證、overclaim、reproducibility、replicability、Unbounded Axiom

---

# 1. 問題：AI 最危險的錯誤常常不是「不知道」，而是「說太多」

一個模型完全不知道答案時，錯誤通常容易辨識。

更棘手的情況是：

$$
E
\rightarrow
C
$$

這條從 evidence 到 claim 的箭頭被偷偷放大。

例如：

$$
\text{有限範圍測試成功}
\rightarrow
\text{全域命題成立},
$$

或：

$$
\text{模型模擬產生趨勢}
\rightarrow
\text{現實世界必然發生},
$$

或：

$$
\text{某篇真實存在的論文提到 X}
\rightarrow
\text{X 已被證實},
$$

或：

$$
\text{LLM 對答案很有把握}
\rightarrow
\text{研究證據很強}.
$$

因此 AI-native research infrastructure 必須處理一個核心問題：

> 一項研究主張，目前究竟可以被說到多強？

這不是單純的 classification problem。

Paper 02 已回答：

> 這是什麼研究？

Paper 03 要回答：

> 在目前證據與驗證狀態下，這項研究可以合法主張到哪裡？

---

# 2. 五個不可混淆的層次

本文首先建立五層分離：

$$
\boxed{
\text{Claim Form}
\neq
\text{Claim Strength}
\neq
\text{Evidence State}
\neq
\text{Validation Result}
\neq
\text{Truth}.
}
$$

## 2.1 Claim Form

例如：

```text
observation
hypothesis
conjecture
theorem-claim
causal-claim
prediction
scenario
heuristic
```

它描述主張的形式。

## 2.2 Claim Strength

描述主張範圍與承諾程度。

例如：

> 在這 1000 個測試樣本中沒有發現反例。

比：

> 在所有輸入上都不存在反例。

弱得多。

## 2.3 Evidence State

描述目前有哪些證據，以及證據本身處於什麼狀態。

## 2.4 Validation Result

描述哪些驗證已被實際執行，以及結果是 PASS、FAIL、UNKNOWN、PARTIAL 或其他狀態。

## 2.5 Truth

研究平台不應宣稱能以一個 metadata 欄位直接封裝終極真理。

因此：

```text
validation: PASS
```

不能被平台渲染為：

```text
truth: TRUE
```

除非該領域的特定形式系統確實定義了更窄的可判定真值，而即使如此，它也只在相應形式與假設範圍內成立。

---

# 3. 既有內部基礎：Overclaim Gap、Evidence Authority 與 Update Integrity

EveMissLab 既有研究已經出現幾個關鍵思想。

第一，Scientific Legitimacy Dynamic Demarcation Design 將 evidence alignment 寫成：

$$
\boxed{
G_{\mathrm{overclaim}}
=
L_{\mathrm{claim}}
-
L_{\mathrm{support}}.
}
$$

其核心不是鼓勵所有研究都降低主張，而是要求：

> 主張強度不得超過證據可以合法承載的範圍。

第二，Project Space Architecture 已明確區分 evidence kind 與 authority，例如：

```text
SOURCE_SPAN
TEST_RESULT
RUNTIME_OBSERVATION
BENCHMARK
HUMAN_ATTESTATION
MODEL_INFERENCE
EXTERNAL_TOOL_RESULT
```

並要求：

$$
\text{MODEL\_INFERENCE}
\neq
\text{RUNTIME\_OBSERVATION}.
$$

第三，既有 Scientific Legitimacy 架構要求研究具有 Disconfirmation Exposure，明示：

- failure conditions；
- conditions forcing revision；
- conditions forcing retraction；
- known counterexamples。

第四，Update Integrity 要求新證據出現後可以：

- claim weakening；
- explicit retraction；
- formal gap closure；
- competitor comparison；

而不應透過無限 ad-hoc rescue、moving goalposts 或 selective evidence update 維持理論表面不敗。

本文將這些思想從個別研究框架提升為 Unbounded Axiom 全站的 claim-evidence governance layer。

---

# 4. 為什麼不能直接使用一條 E0–E5 通用證據階梯

平台很容易設計：

```text
E0
E1
E2
E3
E4
E5
```

然後宣稱：

> E5 比 E4 更可靠。

這在單一研究 programme 內可能有用，但跨領域會立刻出問題。

例如：

- Lean kernel 驗證；
- 獨立實驗複現；
- 一手歷史文獻；
- 哲學反例；
- 高品質田野研究；
- 工程 benchmark；

並不存在天然的全域總排序。

我們無法合理宣稱：

$$
\text{Formal Kernel Verification}
>
\text{Independent Empirical Replication}
$$

或反過來。

它們回答不同問題。

因此本文拒絕：

$$
\boxed{
E_{\mathrm{global}}
\in
\{0,1,2,3,4,5\}
}
$$

作為所有研究的唯一證據尺度。

更合理的是：

$$
\boxed{
\text{typed evidence vector}
+
\text{domain-sensitive requirements}.
}
$$

---

# 5. 外部制度也支持「證據確定性需要領域化」

GRADE 系統在醫療與介入效果證據中使用 high、moderate、low、very low 等 certainty levels，並依 risk of bias、inconsistency、indirectness、imprecision、publication bias 等維度調整。

這是一個成功的 domain-specific evidence certainty system。

但其價值恰好說明：

> 一套好的 evidence grading 必須知道自己在評估什麼。

不能因為 GRADE 在醫療決策非常有價值，就把：

```text
High
Moderate
Low
Very Low
```

直接套到數學證明、哲學分析或歷史反事實。

因此 Unbounded Axiom 應允許：

$$
\text{Domain Evidence Profile}
$$

對不同研究類型建立不同 required support，而不是打造一個假裝普世的 evidence scalar。

---

# 6. Claim Profile：主張究竟承諾了什麼

對每個 claim $c$，本文定義：

$$
\boxed{
K(c)
=
(
\tau,
\sigma,
\mu,
q,
\omega,
A,
J
).
}
$$

其中：

- $\tau$：claim form；
- $\sigma$：scope；
- $\mu$：modality；
- $q$：quantification / generalization；
- $\omega$：world / temporal mode；
- $A$：assumption set；
- $J$：jurisdiction / applicability domain。

---

# 7. $\tau$：Claim Form

沿用 Paper 02：

```text
observation
descriptive-claim
hypothesis
conjecture
theorem-claim
causal-claim
correlational-claim
mechanism-claim
heuristic
prediction
scenario
counterfactual-claim
normative-claim
performance-claim
replication-claim
negative-result
```

Claim form 不直接決定可信度，但它決定後續需要什麼類型的支持。

---

# 8. $\sigma$：Scope

比較：

```text
在本資料集上
```

與：

```text
在所有同類資料集上
```

或：

```text
對任意輸入
```

是完全不同的 claim。

因此 scope 至少應保存：

```text
local
sample-bounded
dataset-bounded
population-bounded
domain-bounded
cross-domain
universal
unknown
```

並可附：

```yaml
scope:
  type: domain-bounded
  domain:
    - ...
  exclusions:
    - ...
```

---

# 9. $\mu$：Modality

AI 經常把不同 modality 的句子平滑成同一種肯定語氣。

應區分：

```text
possible
plausible
expected
probabilistic
actual
necessary
conditional
normative
unknown
```

例如：

$$
\text{Possible}(X)
\not\Rightarrow
\text{Actual}(X),
$$

且：

$$
\text{Likely}(X)
\not\Rightarrow
\text{Necessary}(X).
$$

---

# 10. $q$：Quantification / Generalization

對形式研究尤其重要。

例如：

$$
\exists x
$$

與：

$$
\forall x
$$

不是語氣差異，而是完全不同的邏輯負擔。

同樣，從：

$$
n=10^6
$$

個有限樣本未見反例，不能直接提升為：

$$
\forall x,\ P(x).
$$

因此：

$$
\boxed{
\text{Finite Search}
\not\Rightarrow
\text{Universal Proof}.
}
$$

除非 domain 本身有限且已被完整枚舉。

---

# 11. $\omega$：World / Temporal Mode

沿用 Paper 02：

```text
actual-past
actual-present
prospective
forecast
scenario
counterfactual
hypothetical
simulated
formal-abstract
```

Evidence requirements 必須與 world mode 相容。

例如：

```text
world_mode: simulated
```

不能在沒有額外 world grounding 的情況下自動升級為：

```text
world_mode: actual-present
```

---

# 12. $A$：Assumption Set

一個 theorem claim、模型、工程性能主張或 scenario 都依賴假設。

因此：

$$
c
=
c\mid A.
$$

若 assumption 沒有記錄，下游 AI 很容易把：

> 在假設 A、B、C 下成立。

轉成：

> 無條件成立。

所以：

$$
\boxed{
\text{Conditional Validity}
\neq
\text{Unconditional Validity}.
}
$$

---

# 13. $J$：Jurisdiction / Applicability Domain

Claim 需要說清楚它在哪個判定域內合法。

例如工程 benchmark：

```text
hardware: RTX 4090
batch_size: 16
precision: bf16
dataset: X-v2
```

若將結果寫成：

> 此方法永遠比另一方法快。

就超出了原 jurisdiction。

因此：

$$
J(c)
$$

保存 claim 的合法適用邊界。

---

# 14. Claim Strength 不是單一數字，而是偏序

由於不同 claim 可能在不同維度更強，不適合強行定義：

$$
L(c)\in\mathbb R.
$$

本文改用 domain-relative partial order：

$$
c_1
\preceq_{\mathcal D}
c_2.
$$

其意義是：

> 在研究領域 $\mathcal D$ 的明確規則下， $c_2$ 對世界、範圍、量詞或必要性所做的承諾不弱於 $c_1$。

例如：

$$
\text{sample-bounded observation}
\preceq
\text{population-general claim}.
$$

或：

$$
\text{possible}
\preceq
\text{actual}
\preceq
\text{necessary},
$$

但這些 ordering 必須依 claim type 與語義定義，不應假設所有軸都能全序化。

---

# 15. Evidence Object：證據不是一句「有資料」

沿用既有 Evidence Object 思想，每一筆 evidence $e$ 至少應有：

```yaml
evidence_id:
kind:
source_ref:
span_or_locator:
producer:
method:
time:
integrity:
version:
relation_to_claim:
```

其中 `kind` 可包括：

```text
SOURCE_SPAN
PRIMARY_RECORD
DATASET
TEST_RESULT
BUILD_RESULT
RUNTIME_OBSERVATION
BENCHMARK
EXPERIMENT_RESULT
SIMULATION_RESULT
FORMAL_PROOF_OBJECT
PROOF_ASSISTANT_RESULT
COUNTEREXAMPLE
HUMAN_ATTESTATION
MODEL_INFERENCE
EXTERNAL_TOOL_RESULT
IMPORTED_RECORD
```

核心規則：

$$
\boxed{
\text{Evidence must retain its type}.
}
$$

不能在傳遞過程中把 simulation、inference、observation、attestation 全部壓成：

```text
evidence: yes
```

---

# 16. Evidence State Vector

對一項 claim $c$，本文提出：

$$
\boxed{
\mathbf E(c)
=
(
x,
\ell,
m,
s,
r,
i,
f,
w,
n,
u
).
}
$$

其中：

- $x$：existence / integrity；
- $\ell$：claim linkage；
- $m$：methodological adequacy；
- $s$：scope coverage；
- $r$：replayability / reproducibility；
- $i$：independence；
- $f$：formal verification；
- $w$：world grounding；
- $n$：negative-evidence exposure；
- $u$：uncertainty characterization。

各維度的狀態不是強迫二值，可採：

```text
PASS
PARTIAL
FAIL
UNKNOWN
NOT_APPLICABLE
NOT_RUN
```

必要時附 domain-specific metric。

---

# 17. $x$：Existence / Integrity

回答：

> 證據物件本身是否真實存在，而且身份是否可靠？

例如：

- DOI 是否對得上；
- dataset version 是否存在；
- experiment output 是否有 hash；
- proof artifact 是否與聲稱版本一致。

這一軸將與 Paper 04 的 Source Reality 深度整合。

---

# 18. $\ell$：Claim Linkage

回答：

> 這個證據真的支持這一個 claim 嗎？

一篇真實論文可以完全沒有支持目前句子。

因此：

$$
\boxed{
\text{Source Exists}
\not\Rightarrow
\text{Claim Supported}.
}
$$

這是 citation verification 的核心。

---

# 19. $m$：Methodological Adequacy

回答：

> 產生這個 evidence 的方法，是否足以承擔目前 claim？

例如：

- 樣本設計；
- 統計方法；
- control；
- benchmark fairness；
- proof inference；
- historical source criticism；
- conceptual consistency。

---

# 20. $s$：Scope Coverage

回答：

> 證據涵蓋的範圍與 claim scope 相差多少？

如果 claim 宣稱：

```text
all populations
```

但 evidence 只有：

```text
one laboratory sample
```

則存在 scope gap。

---

# 21. $r$：Replayability / Reproducibility

對計算研究：

$$
r
$$

可表示相同資料、程式、方法與條件下是否能重新得到一致結果。

National Academies 將 reproducibility 定義為以相同輸入資料、計算步驟、方法、程式與分析條件取得一致 computational results。

這與另取新資料重新回答相同科學問題的 replicability 不同。

因此平台不應把：

```text
code reran successfully
```

渲染成：

```text
independently replicated
```

---

# 22. $i$：Independence

回答：

> 支持是否來自真正獨立的資料、研究者、模型、實驗室或證據鏈？

十個網站互相轉載同一條錯誤新聞，不等於十份獨立證據。

三個 AI 都引用同一個錯誤 source，也不等於三次 independent verification。

因此：

$$
\boxed{
\text{Multiplicity}
\neq
\text{Independence}.
}
$$

---

# 23. $f$：Formal Verification

形式研究可能具有：

```text
NOT_RUN
PROOF_SKETCH
CHECKED_LOCAL
KERNEL_VERIFIED
COUNTEREXAMPLE_FOUND
FAILED
```

但：

$$
f=\texttt{KERNEL\_VERIFIED}
$$

仍只表示對指定 formal object、axioms、library version 與 proof obligation 的驗證。

不代表相關現實世界 interpretation 自動正確。

因此：

$$
\boxed{
\text{Formal Validity}
\neq
\text{World Grounding}.
}
$$

---

# 24. $w$：World Grounding

回答：

> claim 是否需要現實世界對應，而且目前是否存在相應 grounding？

純數學可以：

```text
w: NOT_APPLICABLE
```

而物理理論即使形式完美，也可能：

```text
f: PASS
w: UNKNOWN
```

這不是矛盾。

它只是表示：

> 形式結構成立，但世界是否如此仍未確認。

---

# 25. $n$：Negative-Evidence Exposure

研究是否主動暴露於可能失敗的條件？

例如：

- 搜尋反例；
- 檢查 competitor；
- 查 contradictory sources；
- holdout test；
- external replication；
- failed predictions；
- retraction upstream；
- no-go result。

若系統只搜尋支持證據：

$$
n\approx\texttt{FAIL/PARTIAL}.
$$

這可以避免 AI 研究退化成 confirmation engine。

---

# 26. $u$：Uncertainty Characterization

回答：

> 研究是否有描述真正的不確定性？

不同類型包括：

```text
measurement uncertainty
sampling uncertainty
model uncertainty
source uncertainty
classification uncertainty
epistemic uncertainty
parameter uncertainty
scenario uncertainty
normative disagreement
```

重要的是：

$$
\boxed{
\text{Uncertainty}
\neq
\text{Ignorance to be hidden}.
}
$$

它本身是 research state。

---

# 27. 不要讓 LLM Confidence 變成 Evidence

模型可以有 operational confidence，例如：

```text
classification_confidence: 0.82
```

但這是：

$$
\operatorname{Conf}_{M}(x),
$$

不是：

$$
\operatorname{EvidenceStrength}(x).
$$

因此：

$$
\boxed{
\operatorname{Conf}_{M}(c)\uparrow
\not\Rightarrow
\mathbf E(c)\uparrow.
}
$$

高自信模型可以錯。

低自信模型也可能提出正確但尚未充分驗證的新方向。

平台應保存 model confidence 作為操作資訊，而不是將其轉成 public scientific authority。

---

# 28. Evidence Requirement Profile

不同 claim 需要不同證據。

本文定義：

$$
\boxed{
\rho(c)
=
\operatorname{Req}
(
K(c),
R(c)
),
}
$$

其中：

- $K(c)$：claim profile；
- $R(c)$：Paper 02 research coordinates。

 $\rho(c)$ 是 claim 所需的 typed support profile。

例如：

```text
theorem-claim
```

可能要求：

```text
proof object
assumption closure
counterexample audit
formal validation if declared
```

而：

```text
historical descriptive claim
```

可能要求：

```text
source identity
source span
provenance
chronology
source criticism
```

又例如：

```text
causal claim
```

可能要求：

```text
identification strategy
alternative explanation
confounder handling
intervention or causal design evidence
```

---

# 29. Support Adequacy 不等於 Evidence Count

定義：

$$
\boxed{
\operatorname{Adequate}
(
\mathbf E(c),
\rho(c)
)
\in
\{
\texttt{PASS},
\texttt{PARTIAL},
\texttt{FAIL},
\texttt{UNKNOWN}
\}.
}
$$

因此：

$$
100\text{ pieces of weak evidence}
$$

不一定能取代：

$$
1\text{ required proof obligation}.
$$

同樣：

$$
100\text{ citations}
$$

不代表：

$$
\text{stronger support}.
$$

---

# 30. Overclaim Gap 的一般化

舊模型寫：

$$
G_{\mathrm{overclaim}}
=
L_{\mathrm{claim}}
-
L_{\mathrm{support}}.
$$

本文保留其直覺，但不用假裝所有 claim 與 support 都能投影成同一實數。

改定義：

$$
\boxed{
G_{\mathrm{overclaim}}(c)
=
\operatorname{Gap}
(
\rho(c),
\mathbf E(c)
).
}
$$

輸出可以是 deficit vector：

```yaml
overclaim_gap:
  status: OPEN
  deficits:
    - scope-coverage
    - independent-replication
    - world-grounding
```

若所有 required dimensions 滿足：

```text
overclaim_gap: CLOSED
```

但 `CLOSED` 仍不代表終極真理，只表示：

> 在目前 claim 類型與已宣告規範下，沒有發現未補足的必要支持缺口。

---

# 31. Claim Support State

為了人類 UI，可從複雜 evidence vector 投影出較簡單但不冒充真值的狀態：

```text
UNASSESSED
OPEN
PRELIMINARY_SUPPORT
SUPPORTED_WITHIN_SCOPE
ROBUST_WITHIN_SCOPE
DISPUTED
CONTRADICTED
FAILED
WITHDRAWN
UNRESOLVED
```

注意：

```text
SUPPORTED_WITHIN_SCOPE
```

刻意保留：

```text
within scope
```

因為：

$$
\boxed{
\text{Support}
\text{ is always support under a claim boundary.}
}
$$

---

# 32. Formal Status 應使用正交 Badge，而不是搶占 Support State

例如：

```yaml
claim_support: SUPPORTED_WITHIN_SCOPE

validation_badges:
  - KERNEL_VERIFIED
  - INDEPENDENT_REPRODUCTION
```

而不是將所有資訊壓成：

```text
evidence_level: 5
```

數學研究可以有：

```text
KERNEL_VERIFIED
```

實驗研究可以有：

```text
INDEPENDENT_REPLICATION
```

計算研究可以有：

```text
COMPUTATIONALLY_REPRODUCIBLE
```

它們彼此不必存在虛假的全域高低排序。

---

# 33. Reproducibility、Replicability 與 Generalizability 必須分離

依 National Academies 的跨領域定義：

- reproducibility：相同資料與計算流程重得一致結果；
- replicability：新的研究與新的資料回答相同科學問題並得到一致結果；
- generalizability：結果能否適用到不同 context 或 population。

因此：

$$
\boxed{
\text{Reproducible}
\neq
\text{Replicated}
\neq
\text{Generalized}.
}
$$

Unbounded Axiom 的 validation badge 應分開保存這三者。

---

# 34. Preregistration 的價值：固定研究前狀態，不是禁止修正

OSF 將 preregistration 定義為在資料收集或分析前留下 time-stamped research plan。

對 AI research，這尤其重要。

因為 AI 可以極快速地：

- 改 hypothesis；
- 改 scoring rule；
- 換 subset；
- 改 stopping rule；
- 在看到結果後重新描述原始目標。

因此：

$$
\text{Research Plan}_{t_0}
$$

應和：

$$
\text{Analysis}_{t_1}
$$

分離。

若中途改動：

$$
\Delta P
$$

不是禁止，而是留下：

```text
DEVIATION
```

與 reason。

因此：

$$
\boxed{
\text{Preregistration}
\neq
\text{No Revision}.
}
$$

而是：

$$
\boxed{
\text{Revision with temporal provenance}.
}
$$

---

# 35. AI 自主研究需要 Precommitment

人類研究已有 researcher degrees of freedom 問題。

AI agent 具有更多可快速探索的 decision branches。

因此 autonomous research 可以採：

```yaml
precommitment:
  research_question:
  hypothesis:
  evaluation_metric:
  dataset_scope:
  stopping_rule:
  disconfirmation_conditions:
  allowed_adaptations:
```

如果 AI 之後更改：

```text
stopping_rule
```

系統應保存：

$$
\texttt{PRECOMMITTED}
\rightarrow
\texttt{DEVIATED}.
$$

並標記影響。

---

# 36. Falsifiability 不適合當所有研究的唯一欄位

「可證偽性」對很多經驗科學很重要，但不能將所有研究都問：

> 哪個實驗可以推翻它？

例如：

- 定義；
- 純形式命題；
- 歷史來源重建；
- 規範論證；
- 概念分析；

其 failure mode 不必是實驗。

因此本文採更一般的：

$$
\boxed{
\text{Defeat / Revision Conditions}.
}
$$

其問題是：

> 出現什麼新資訊時，研究者應該降低、限制、修改、撤回或重新分類這項主張？

---

# 37. Defeat / Revision Contract

對 claim $c$，定義：

$$
\boxed{
D(c)
=
\{
(d_j,a_j)
\}_{j=1}^{n},
}
$$

其中：

- $d_j$：trigger condition；
- $a_j$：required update action。

例如：

```yaml
revision_contract:
  - trigger: counterexample-found
    action: DISPROVE_OR_NARROW

  - trigger: primary-source-retracted
    action: REOPEN_SUPPORT

  - trigger: independent-replication-failure
    action: DOWNGRADE_SUPPORT

  - trigger: assumption-invalid
    action: NARROW_SCOPE

  - trigger: formal-proof-gap
    action: REMOVE_VERIFIED_BADGE
```

這比單純：

```text
falsifiable: yes
```

資訊高得多。

---

# 38. Revision Action Vocabulary

本文建議 v0.1：

```text
ANNOTATE
REOPEN
DOWNGRADE_SUPPORT
WEAKEN_MODALITY
NARROW_SCOPE
ADD_ASSUMPTION
REMOVE_ASSUMPTION
RECLASSIFY
SPLIT_CLAIM
SUPERSEDE
WITHDRAW
RETRACT
DISPROVE
ARCHIVE
NO_CHANGE_WITH_JUSTIFICATION
```

`NO_CHANGE_WITH_JUSTIFICATION` 也很重要。

因為新證據不一定真的擊敗 claim。

平台不能把：

> 有人提出反對意見

等同：

> 原論文必須撤回。

---

# 39. 不同領域的 Defeat 條件不同

## 39.1 數學

可能包括：

```text
valid counterexample
proof gap
inconsistent assumptions
domain mismatch
formal checker rejection
```

## 39.2 實驗科學

可能包括：

```text
measurement invalidation
replication failure
confounder discovery
systematic bias
new contradictory evidence
```

## 39.3 歷史研究

可能包括：

```text
new primary source
forged source detection
chronology conflict
provenance failure
translation correction
```

## 39.4 工程

可能包括：

```text
benchmark invalidity
hardware mismatch
regression
security failure
baseline correction
```

## 39.5 哲學／概念研究

可能包括：

```text
counterexample
conceptual inconsistency
self-contradiction
explanatory failure
category mistake
stronger competing analysis
```

## 39.6 未來研究

可能包括：

```text
forecast miss
assumption invalidation
scenario premise failure
structural regime change
```

因此：

$$
\boxed{
\text{Revision Logic}
=
f(\text{Research Type}).
}
$$

---

# 40. 定義也有 Failure Conditions，但不是經驗證偽

一個 definition：

$$
D:x\mapsto...
$$

通常不是「世界證明它錯」。

但它可能：

- inconsistent；
- circular；
- unusable；
- ambiguous；
- conflicting with canonical type system；
- fail to distinguish intended objects。

因此 definition 可以有：

```text
consistency conditions
non-circularity conditions
scope conditions
interoperability conditions
```

這再次證明：

$$
\text{Defeat / Revision}
$$

比單一 empirical falsification 更一般。

---

# 41. Promotion Witness：AI 不能靠語氣把 claim 升級

若 claim 從：

```text
conjecture
```

升到：

```text
theorem-claim with verified status
```

或從：

```text
scenario
```

升到：

```text
forecast
```

必須存在：

$$
\boxed{
W_{c:c_1\rightarrow c_2}.
}
$$

promotion witness 至少記錄：

```yaml
from_state:
to_state:
new_evidence:
new_validation:
scope_check:
assumption_check:
negative_evidence_check:
approved_by:
timestamp:
```

如果沒有 witness：

$$
\boxed{
\text{No Silent Epistemic Promotion}.
}
$$

這是 AI-native scholarly system 的核心安全規則。

---

# 42. Demotion 也必須有 Provenance

反過來，若 claim 被降級：

```text
SUPPORTED_WITHIN_SCOPE
→ DISPUTED
```

也要留下：

```text
trigger
evidence
actor
timestamp
affected_versions
```

而不是偷偷改掉舊文章。

因此：

$$
C_t
\rightarrow
C_{t+1}
$$

必須留下 epistemic history。

---

# 43. Hard Failure 與 Soft Defeater

不是所有負面證據都具有同一效力。

本文區分：

## Hard Failure

例如：

- valid mathematical counterexample；
- source proven fabricated；
- dataset corrupted beyond repair；
- proof kernel rejects essential theorem；
- claimed experiment never occurred。

可能直接觸發：

```text
FAIL
RETRACT
DISPROVE
```

## Soft Defeater

例如：

- independent replication 不一致；
- competing explanation；
- confidence interval 擴大；
- new source weakens interpretation；
- benchmark condition 改變。

通常先觸發：

```text
REOPEN
DOWNGRADE
DISPUTED
NARROW_SCOPE
```

這可以避免平台變成非黑即白的真理裁判。

---

# 44. Source Retraction 不等於 Downstream Claim 自動為假

假設：

$$
c
\leftarrow
s_1,s_2,s_3.
$$

其中：

$$
s_2
$$

被撤回。

正確系統不應直接：

$$
c=\texttt{FALSE}.
$$

而應重新計算：

$$
\mathbf E(c).
$$

可能結果：

```text
still-supported
downgraded
unresolved
failed
```

因此：

$$
\boxed{
\text{Upstream Retraction}
\Rightarrow
\text{Downstream Re-evaluation},
}
$$

而不是：

$$
\boxed{
\text{Upstream Retraction}
\Rightarrow
\text{Automatic Downstream Falsity}.
}
$$

Paper 04 將建立這個 source dependency propagation。

---

# 45. No Evidence 與 Evidence of Absence

AI 很容易把：

> 沒找到證據。

寫成：

> 不存在。

因此必須區分：

$$
\boxed{
\text{No Evidence Found}
\neq
\text{Evidence of Absence}.
}
$$

`No Evidence Found` 可能只是：

- search incomplete；
- corpus truncated；
- source inaccessible；
- terminology mismatch；
- publication bias。

只有在 search space、detection power 或 exhaustive domain 足夠明確時，absence 才可能成為更強證據。

---

# 46. Negative Results 是一級研究物件

AI research ecology 若只保存成功路徑，會反覆浪費計算。

因此應保存：

```text
counterexample-not-found-within-scope
method-failed
replication-failed
proof-route-blocked
benchmark-regression
source-not-found
hypothesis-not-supported
```

並明確標記 scope。

例如：

$$
\text{No counterexample found for }n\le 10^9
$$

是一個有效 negative search result。

但不是：

$$
\text{No counterexample exists}.
$$

---

# 47. AI 的「不知道」必須是合法輸出

平台應允許：

```text
UNKNOWN
UNRESOLVED
INCOMPARABLE
INSUFFICIENT_EVIDENCE
NOT_APPLICABLE
NOT_RUN
```

不能因為產品 UX 喜歡每次給答案，就把：

$$
\text{uncertainty}
$$

壓成：

$$
\text{best guess presented as fact}.
$$

因此：

$$
\boxed{
\text{Abstention can be epistemically correct}.
}
$$

---

# 48. 但「不確定」也不能成為逃避研究的萬用詞

另一個極端是 AI 過度保守：

> 無法百分之百確定，因此不能提出任何結論。

這也不合理。

研究本來就經常處於：

$$
0<\text{support}<\text{certainty}.
$$

因此 CECA 的目的不是：

$$
\text{Only publish certainty}.
$$

而是：

$$
\boxed{
\text{Publish calibrated uncertainty}.
}
$$

例如：

> 在目前資料集與模型條件下結果一致，但尚未有跨環境獨立重現。

這比：

> 已證明。

或：

> 完全不知道。

都更準確。

---

# 49. Claim Rendering Policy

平台可以依 claim state 提供人類可讀語言模板。

例如：

## Preliminary

```text
初步結果顯示……
```

## Supported Within Scope

```text
在已宣告範圍與目前證據下，結果支持……
```

## Robust Within Scope

```text
在多來源／多環境驗證下，目前結果穩健支持……
```

## Disputed

```text
目前存在相互衝突的證據或有效異議……
```

## Unresolved

```text
目前證據不足以在候選解釋間做出可靠判定……
```

這些只是 projection，不應取代 canonical machine state。

---

# 50. Claim Card：每個重要主張都可以被單獨查看

未來 Unbounded Axiom 不應只有 paper-level status。

每個 material claim 可以有：

```yaml
claim_id:
text:
claim_form:
scope:
modality:
assumptions:
jurisdiction:

support_state:
evidence_refs:
validation_refs:

overclaim_gap:
revision_contract:
known_defeaters:
history:
```

這樣：

$$
\text{Paper}
=
\{c_1,c_2,\ldots,c_n\}
$$

而不同 claim 可以有不同可信狀態。

一篇論文可以同時存在：

- 一個已證明 theorem；
- 一個未證猜想；
- 一個 engineering proposal；
- 一個 speculative future implication。

平台不需要把整篇論文壓成：

```text
Evidence Level: E4
```

---

# 51. Paper-Level Status 應由 Claim Projection 產生

若需要 paper-level summary，應明示 projection rule。

例如：

```text
contains 12 material claims
4 robust-within-scope
5 supported-within-scope
2 open
1 disputed
```

比：

```text
paper confidence = 82%
```

更有研究價值。

如果真的要生成單一 public badge，也應能展開查看底層 claims。

---

# 52. Evidence Completeness 與 Research Importance 分離

一個高度 speculative 新理論可能非常重要。

一個 evidence 極完整的微小 replication 可能非常穩固但研究影響較小。

因此：

$$
\boxed{
\text{Evidence Strength}
\neq
\text{Importance}
\neq
\text{Novelty}
\neq
\text{Utility}.
}
$$

平台未來 ranking 不得把這些合併成一個偷偷決定學術價值的 opaque score。

---

# 53. Confidence 也不等於 Probability

如果研究沒有校準模型，不應寫：

```text
confidence: 73.6%
```

只是因為 AI 想給數字。

本文禁止：

$$
\boxed{
\text{Fake Precision}.
}
$$

可使用：

```text
qualitative calibration
interval
posterior probability
frequentist uncertainty
model score
expert credence
```

但必須說明數字從哪裡來。

---

# 54. Evidence State 必須時間化

一個 claim 在 2026 年：

```text
SUPPORTED_WITHIN_SCOPE
```

2030 年可能：

```text
DISPUTED
```

2032 年又：

```text
ROBUST_WITHIN_SCOPE
```

因此：

$$
\mathbf E_t(c)
$$

與：

$$
S_t(c)
$$

都是時間函數。

平台應保存：

$$
\boxed{
\text{Epistemic State History}.
}
$$

---

# 55. Dynamic Update Rule

抽象表示：

$$
S_{t+1}(c)
=
U
(
S_t(c),
E_{t+1},
D(c),
V_{t+1}
).
$$

其中：

- $S_t(c)$：舊 support state；
- $E_{t+1}$：新證據；
- $D(c)$：revision contract；
- $V_{t+1}$：新 validation results。

更新函數 $U$ 不必全平台唯一。

不同 domain 可以使用不同 profile。

---

# 56. AI 多模型共識不能取代 Evidence

若：

$$
A_1,A_2,A_3
$$

都說：

> 我認為這個證明是對的。

則：

$$
\operatorname{majorityVote}(A_i)
$$

最多是一種 review signal。

它不是 proof object。

同理，多模型一致判斷某歷史事件，也不能取代 primary source。

因此：

$$
\boxed{
\text{Model Consensus}
\neq
\text{Independent World Evidence}.
}
$$

---

# 57. 異質模型交叉檢查仍然有價值

前一節不是說 cross-model review 無用。

它可以提高：

- bug detection；
- counterargument coverage；
- source mismatch detection；
- proof gap detection；
- alternative hypothesis generation。

因此它應記錄為：

```text
validation_mode: cross-model-review
```

而不是：

```text
evidence_kind: independent-empirical-evidence
```

這就是 typed evidence 的價值。

---

# 58. 數學例：有限驗證不能偷渡成全域證明

假設 AI 驗證：

$$
P(n)=1
$$

對：

$$
1\le n\le10^{12}.
$$

合法 claim：

> 在 $1\le n\le10^{12}$ 的驗證範圍內未發現反例。

非法提升：

$$
\forall n\in\mathbb N,\ P(n)=1.
$$

除非存在 proof witness。

因此：

```yaml
claim_form: conjecture
scope: universal
evidence:
  computational_search:
    range: [1, 10^12]
support_state: PRELIMINARY_SUPPORT
overclaim_gap:
  deficits:
    - universal-proof-obligation
```

這可以直接阻止自主 AI 在長期研究中產生「有限成功累積幻覺」。

---

# 59. 實驗例：一次成功不是 universal causal claim

假設：

$$
n=120
$$

的 controlled experiment 顯示 effect。

平台可以記：

```text
experimental-data: PASS
statistical-validation: PASS
independent-replication: NOT_RUN
generalizability: UNKNOWN
```

因此可以支持：

> 在目前實驗條件下觀察到 effect。

但不應自動支持：

> 對所有 population 都存在相同因果效果。

---

# 60. 歷史例：來源存在不代表唯一解釋

若某封信確實存在且提及事件 $X$：

```text
source-existence: PASS
source-span: PASS
```

仍可能：

```text
interpretive-uniqueness: FAIL/UNKNOWN
```

因此：

> 史料支持作者曾表達 X。

不必等於：

> X 就是歷史事件的唯一原因。

---

# 61. 未來研究例：Scenario 不等於 Forecast

Scenario：

$$
S=
\text{future state}\mid A.
$$

只要 assumption set $A$ 合理，就可以是有價值研究。

它不需要：

$$
P(S)=0.8.
$$

只有當研究宣稱 forecast，才需要：

- target；
- horizon；
- evaluation date；
- scoring rule；
- calibration。

因此：

$$
\boxed{
\text{Scenario Quality}
\neq
\text{Forecast Accuracy}.
}
$$

---

# 62. 工程例：Benchmark Claim 必須綁環境

假設系統宣稱：

> 模型 X 比 Y 快 2.1 倍。

必須保存：

```text
hardware
software
driver
precision
batch
dataset
benchmark version
warmup
measurement method
```

否則 claim jurisdiction 不明。

環境變更後：

$$
2.1\times
$$

不應被永久當成 universal property。

---

# 63. 哲學例：形式化不會自動提升為實證真理

哲學或本體論研究可以形式化：

$$
\mathcal O=(X,R,F).
$$

形式化可以提高：

- 定義清晰度；
- consistency；
- consequence traceability。

但：

$$
\boxed{
\text{Formalized Ontology}
\not\Rightarrow
\text{Empirically Established Ontology}.
}
$$

world grounding 必須分開。

---

# 64. Claim–Evidence Dependency Graph

每個 claim 可以連到 evidence：

$$
c_i
\leftarrow
\{e_{i1},e_{i2},\ldots,e_{ik}\}.
$$

Evidence 也可以支持多個 claim。

因此整體是：

$$
G_{CE}
=
(
C\cup E,
R_{CE}
).
$$

關係至少包括：

```text
supports
partially-supports
contradicts
qualifies
limits
depends-on
reproduces
replicates
invalidates
```

這比 bibliography 更接近真正的 research dependency graph。

---

# 65. Defeater 也要成為 Edge

不只保存 support：

$$
e\rightarrow c.
$$

也保存：

$$
d\dashv c.
$$

其中 $d$ 是 defeater。

例如：

```text
counterexample
failed replication
source retraction
measurement invalidity
alternative explanation
formal contradiction
```

AI 後續研究必須同時讀 support graph 與 defeater graph。

---

# 66. 研究平台不應刪除曾經錯誤的 Epistemic State

假設 2026 年某 claim 被標記：

```text
SUPPORTED_WITHIN_SCOPE
```

2028 年證明它錯。

不應把 2026 狀態抹掉。

應保存：

```text
2026-09-03 SUPPORTED_WITHIN_SCOPE
2028-02-11 CONTRADICTED
2028-03-02 RETRACTED
```

這讓未來研究可以分析：

> 當時為什麼會相信它？

這本身是 valuable meta-research data。

---

# 67. Update Integrity 是平台品質的一部分

真正可靠的 research ecology 不是：

> 永遠不犯錯。

而是：

$$
\boxed{
\text{Errors become visible state transitions}.
}
$$

因此平台可以衡量：

```text
time-to-correction
silent-edit rate
retraction propagation latency
unresolved-defeater backlog
promotion-without-witness rate
```

這些可能比 citation count 更能衡量 AI-native scholarly infrastructure 的健康程度。

---

# 68. 自主 AI 的 Epistemic Budget

AI 在研究時可以有一個 epistemic budget：

```yaml
allowed_claim_promotions:
  theorem:
    requires: proof_witness
  causal:
    requires: causal_validation_profile
  forecast:
    requires: evaluation_contract
  actual-world:
    requires: world_grounding
```

如果條件不滿足：

```text
promotion denied
```

但 AI 仍可以：

```text
publish as conjecture
publish as scenario
publish as heuristic
publish as preliminary observation
```

這解決「太有自信」與「太沒自信」兩個極端。

---

# 69. AI 可以提出理論，不必等到完成驗證才發表

預印本平台的價值之一，就是允許：

```text
OPEN
PRELIMINARY
CONJECTURAL
```

研究公開。

因此：

$$
\boxed{
\text{Low Evidence}
\not\Rightarrow
\text{No Publication}.
}
$$

真正的要求是：

$$
\boxed{
\text{Low Evidence}
\Rightarrow
\text{Correctly Labeled Claim Strength}.
}
$$

這對理論創新非常重要。

---

# 70. 反過來，高證據也不能替代研究類型

一個大量實驗支持的 correlation：

$$
X\leftrightarrow Y
$$

仍然不能僅因證據很多就變成：

$$
X\rightarrow Y.
$$

也就是：

$$
\boxed{
\text{Evidence Quantity}
\not\Rightarrow
\text{Claim-Type Promotion}.
}
$$

promotion 必須滿足相應 methodological witness。

---

# 71. Canonical Claim Manifest

本文提出 v0.1 示意：

```yaml
schema: "ua-ceca/0.1"

claim:
  id: "ua-claim:example-001"

  form: "hypothesis"

  profile:
    scope:
      type: "domain-bounded"
      domain:
        - "..."
    modality: "plausible"
    quantification: "conditional"
    world_mode: "actual-present"
    assumptions:
      - "A1"
      - "A2"
    jurisdiction:
      - "J1"

  support:
    state: "PRELIMINARY_SUPPORT"

    evidence_state:
      existence_integrity: "PASS"
      claim_linkage: "PASS"
      methodology: "PARTIAL"
      scope_coverage: "PARTIAL"
      reproducibility: "NOT_RUN"
      independence: "UNKNOWN"
      formal_verification: "NOT_APPLICABLE"
      world_grounding: "PASS"
      negative_evidence: "PARTIAL"
      uncertainty: "PASS"

    evidence_refs:
      - "ua-evidence:e1"
      - "ua-evidence:e2"

  validation:
    attempted:
      - "source-verification"
      - "adversarial-review"

    results:
      source-verification: "PASS"
      adversarial-review: "PARTIAL"

  overclaim_gap:
    status: "OPEN"
    deficits:
      - "scope-coverage"
      - "independent-replication"

  revision_contract:
    - trigger: "independent-replication-failure"
      action: "DOWNGRADE_SUPPORT"

    - trigger: "scope-counterexample"
      action: "NARROW_SCOPE"

  history:
    - event: "CLAIM_DECLARED"
    - event: "EVIDENCE_ADDED"
```

---

# 72. Required Fields 與 Optional Depth

不是每個作者都要手動填完整 CECA。

最低 public claim 可以只要求：

```text
claim form
scope
support state
evidence refs
known limitations
revision condition
```

其餘可由平台：

$$
\text{extract}
\rightarrow
\text{propose}
\rightarrow
\text{validate}
\rightarrow
\text{confirm}.
$$

---

# 73. 自動抽取不得偷偷創造 Evidence

AI 可以從文章中發現：

> 作者似乎引用這三篇文獻支持 claim C。

但必須標記：

```text
AI_INFERRED_LINK
```

直到 source validator 通過。

因此：

$$
\boxed{
\text{Evidence Extraction}
\neq
\text{Evidence Verification}.
}
$$

---

# 74. Evidence Authority 與 Public Projection

若 evidence 是：

```text
MODEL_INFERENCE
```

UI 應能顯示：

> AI-derived inference

而不是：

> Verified evidence.

若 evidence 為私人資料：

```text
PRIVATE_DATASET
```

可以公開：

```text
existence: attested
contents: restricted
reproducibility-impact: declared
```

而不強制公開所有內容。

這與 Paper 06 的 privacy architecture 相容。

---

# 75. Scientific Rigor 與 CECA

NIH 將 scientific rigor 描述為嚴格應用科學方法，以確保研究設計、方法、分析、解釋與報告盡可能 robust、unbiased 且透明。

CECA 不取代各領域 rigor standard。

它做的是：

> 將「這些 rigor requirement 是否已滿足」轉成 machine-readable evidence state 與 validation state。

因此：

$$
\boxed{
\text{Domain Rigor Standard}
\rightarrow
\text{CECA Validation Profile}.
}
$$

---

# 76. 2026 年的新趨勢：Replication / Reproducibility 開始被視為基礎設施

截至 2026 年 8 月，NIH 新的 agency-wide replication and reproducibility initiative 已再次將 replication、reproducibility 與相關基礎設施提升為 gold-standard science 的核心。

這對 AI-native preprint commons 有直接啟示：

> 重現與複現不應只是論文末尾的一句聲明，而應是可追蹤、可搜尋、可被後續 AI 接手的研究狀態。

因此：

```text
REPRODUCED_BY
REPLICATED_BY
FAILED_TO_REPLICATE_BY
```

都應成為 graph relation。

---

# 77. Claim Promotion Policy

本文提出最小 policy：

對任何強化操作：

$$
c_t
\rightarrow
c_{t+1},
$$

若：

$$
c_t
\prec_{\mathcal D}
c_{t+1},
$$

則必須存在：

$$
W_{t\rightarrow t+1}.
$$

也就是：

$$
\boxed{
\text{Stronger Claim}
\Rightarrow
\text{Explicit Promotion Witness}.
}
$$

---

# 78. Claim Demotion Policy

如果新 evidence 觸發 revision contract：

$$
d_j(c)=1,
$$

則平台至少要求：

$$
a_j
$$

被處理或明確標記 unresolved。

因此不能：

```text
new counterexample found
→ ignore
→ old claim remains silently unchanged
```

---

# 79. Claim Freeze 與 Canonical Publication

某一個 preprint version 發布後：

$$
V_1
$$

應保持 immutable canonical snapshot。

後續修正：

$$
V_1
\rightarrow
V_2.
$$

V1 可以被標記：

```text
superseded
disputed
retracted
```

但不應把原始文字無痕覆蓋。

這與 source-native canonical artifact 原則一致。

---

# 80. CECA 的最小不變量

## Invariant 1

$$
\boxed{
\text{Claim}
\neq
\text{Evidence}.
}
$$

## Invariant 2

$$
\boxed{
\text{Claim Form}
\neq
\text{Claim Strength}.
}
$$

## Invariant 3

$$
\boxed{
\text{Evidence Type}
\neq
\text{Evidence Strength}.
}
$$

## Invariant 4

$$
\boxed{
\text{Evidence Mode}
\neq
\text{Validation Result}.
}
$$

## Invariant 5

$$
\boxed{
\text{Validation PASS}
\neq
\text{Universal Truth}.
}
$$

## Invariant 6

$$
\boxed{
\text{Model Confidence}
\neq
\text{Scientific Evidence}.
}
$$

## Invariant 7

$$
\boxed{
\text{No Evidence Found}
\neq
\text{Evidence of Absence}.
}
$$

## Invariant 8

$$
\boxed{
\text{Finite Verification}
\neq
\text{Universal Proof}.
}
$$

## Invariant 9

$$
\boxed{
\text{Formal Validity}
\neq
\text{World Grounding}.
}
$$

## Invariant 10

$$
\boxed{
\text{Support}
\text{ must remain scoped}.
}
$$

## Invariant 11

$$
\boxed{
\text{Stronger Claim}
\Rightarrow
\text{Promotion Witness}.
}
$$

## Invariant 12

$$
\boxed{
\text{Negative Evidence}
\Rightarrow
\text{Revision Event or Explicit Unresolved State}.
}
$$

---

# 81. CECA 與 Paper 02 AIRCS 的關係

Paper 02：

$$
R=
(
D,
I,
C,
M,
P,
W,
E,
V,
A,
L,
G
)
$$

回答：

> 這是什麼研究？

CECA：

$$
\mathcal C=
(
K(c),
\mathbf E(c),
\rho(c),
D(c),
S(c)
)
$$

回答：

> 這個 claim 目前被支持到哪裡，以及什麼情況下需要修改？

因此：

$$
\boxed{
\text{AIRCS}
+
\text{CECA}
=
\text{typed research object}
+
\text{typed epistemic state}.
}
$$

---

# 82. 與 Paper 04 的接口：Source Reality

Paper 03 假設 evidence object 可以引用 source。

但 source 是否：

- 真實存在；
- 仍可取得；
- 已撤回；
- 版本正確；
- 精確支持 claim；

將由 Paper 04 建立。

因此：

$$
\boxed{
\text{CECA}
\text{ consumes verified source states;}
}
$$

而：

$$
\boxed{
\text{Paper 04}
\text{ produces source reality states.}
}
$$

---

# 83. 與 AI Identity 的接口

CECA 不因研究者是人類或 AI 而降低證據要求。

但 research actor identity 會影響：

- provenance；
- reproducibility；
- independence；
- conflict of interest；
- model lineage。

例如兩個「不同名稱」但其實共享同一 memory snapshot 的 AI，不一定能算獨立驗證。

Paper 05 將處理這個問題。

---

# 84. 與 Privacy 的接口

某些 evidence 可能不能公開。

這不代表 claim 必然無效，但會影響：

$$
r,\ i,\ x
$$

等維度的可驗證程度。

因此平台可以表示：

```text
evidence exists: ATTESTED
public access: RESTRICTED
independent verification: NOT_AVAILABLE
```

而不是：

```text
evidence: missing
```

Paper 06 將處理完整 disclosure state。

---

# 85. 最終目標：讓 AI 說得剛剛好

AI 原生研究的理想狀態不是：

> 永遠使用最保守語言。

也不是：

> 每次都給出最強結論。

而是：

$$
\boxed{
\text{Claim Strength}
\approx
\text{Support Capacity}.
}
$$

當新 evidence 增加：

$$
\text{Claim may strengthen}.
$$

當 defeater 出現：

$$
\text{Claim may weaken}.
$$

當 evidence 不足：

$$
\text{Claim remains open}.
$$

當 proof 完成：

$$
\text{Formal status may upgrade}.
$$

當世界 grounding 尚缺：

$$
\text{World claim remains limited}.
$$

這才是真正的 epistemic calibration。

---

# 86. 結論

當 AI 已能大量生成理論、引用、實驗、程式、證明草稿與研究敘事時，學術基礎設施不能再依靠語氣、作者權威或「有沒有 citation」來判斷研究強度。

Unbounded Axiom 若要成為 open AI-native preprint commons，必須將每個重要主張拆成：

$$
\boxed{
\text{Claim Profile}
+
\text{Evidence State}
+
\text{Validation State}
+
\text{Revision Contract}
+
\text{History}.
}
$$

本文提出 CECA：

$$
\boxed{
\mathcal C(c)
=
(
K(c),
\mathbf E(c),
\rho(c),
D(c),
S_t(c)
).
}
$$

其中：

- $K(c)$：主張真正承諾了什麼；
- $\mathbf E(c)$：目前有哪些 typed evidence；
- $\rho(c)$：此類主張需要什麼支持；
- $D(c)$：什麼情況需要修正；
- $S_t(c)$：目前時間點的 support state。

這套架構拒絕以單一證據分數假裝不同研究共享同一認識論尺度，也拒絕模型高信心語氣成為科學權威。

其最核心的兩條規則是：

$$
\boxed{
\text{Do not claim more than the evidence can carry.}
}
$$

以及：

$$
\boxed{
\text{Do not claim less merely because certainty is incomplete.}
}
$$

前者阻止 AI 過度自信。

後者阻止 AI 把所有尚未完成終極驗證的研究都壓成「不知道」。

真正成熟的 AI research ecology 應允許猜想保持猜想、scenario 保持 scenario、實驗結果保持在其樣本與條件範圍、形式證明保持其公理與形式系統邊界；同時允許這些研究隨新 evidence、反例、重現與驗證而逐步升級、降級、分叉、修訂或撤回。

Paper 04 將接續處理這個系統仍缺少的外部世界錨點：

$$
\boxed{
\text{Source Reality}
+
\text{Citation Validation}
+
\text{Data Provenance}.
}
$$

也就是：

> 一項 evidence object 說自己來自某篇論文、某個資料庫、某個 API 或某次實驗時，我們如何知道那個來源真的存在、真的在那裡、真的說了這件事，而且在未來仍然可追蹤？

---

# 參考資料

1. National Academies of Sciences, Engineering, and Medicine. **Reproducibility and Replicability in Science.** Washington, DC: The National Academies Press, 2019. DOI: 10.17226/25303.  
   https://doi.org/10.17226/25303

2. Schünemann, H. J., Higgins, J. P. T., Vist, G. E., Glasziou, P., Akl, E. A., Skoetz, N., Guyatt, G. H. **Chapter 14: Completing ‘Summary of findings’ tables and grading the certainty of the evidence.** Cochrane Handbook for Systematic Reviews of Interventions, Version 6.5, 2024.  
   https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14

3. Centers for Disease Control and Prevention. **ACIP GRADE Handbook — Chapter 7: GRADE Criteria Determining Certainty of Evidence.** 2024.  
   https://www.cdc.gov/acip-grade-handbook/hcp/chapter-7-grade-criteria-determining-certainty-of-evidence/

4. National Institutes of Health. **Enhancing Reproducibility through Rigor and Transparency.**  
   https://www.grants.nih.gov/policy-and-compliance/policy-topics/reproducibility  
   Accessed 2026-09-03.

5. National Institutes of Health. **Strengthening Replication and Reproducibility of NIH-funded Research.** Last reviewed 2026-08-28.  
   https://www.nih.gov/replicationandreproducibility

6. Open Science Framework. **Welcome to Registrations & Preregistrations!** OSF Support, updated 2026.  
   https://help.osf.io/article/330-welcome-to-registrations

7. Open Science Framework. **Simplifying the Preregistration Process.** OSF Support, updated 2026-08-03.  
   https://help.osf.io/article/626-simplifying-the-preregistration-process

8. NIST. Autio, C., Schwartz, R., Dunietz, J., Jain, S., Stanley, M., Tabassi, E., Hall, P., Roberts, K. **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.** NIST AI 600-1, 2024; updated 2026. DOI: 10.6028/NIST.AI.600-1.

9. EveMissLab. **Project Space Architecture Master Specification v0.1.** 2026-08-20.

10. EveMissLab. **EveMissLab AI Research Laboratory Canonical Site Specification v0.1.** 2026-08-27.

11. EveMissLab. **Cosmogenesis Compiler v0.3.3 — Scientific Legitimacy Dynamic Demarcation Design.** 2026-08-23.

12. Neo.K with AI collaborators. **Reflexive Representation Theory Unified Closure v1.0.** EveMissLab research corpus, 2026.

13. Neo.K, Aletheia / GPT-5.6 Sol. **研究不是單一類型：AI 原生研究分類與多軸研究座標系.** AI-Native Preprint Commons Series, Paper 02, 2026-09-03.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 CECA；分離 Claim Form、Claim Strength、Evidence State、Validation Result 與 Truth；提出 typed evidence vector、required support profile、support adequacy、overclaim gap、promotion witness、Defeat / Revision Contract、dynamic epistemic state、reproducibility/replicability/generalizability 分離，以及 AI claim promotion/demotion policy。 |
