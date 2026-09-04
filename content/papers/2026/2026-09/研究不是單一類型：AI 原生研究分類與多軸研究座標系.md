---
document_id: "UA-ANPC-A02"
series: "AI-Native Preprint Commons Series"
series_part: 2
version: "0.1"
language: "zh-Hant"
title: "研究不是單一類型：AI 原生研究分類與多軸研究座標系"
english_title: "Research Is Not a Single Type: AI-Native Research Classification and a Multi-Axis Research Coordinate System"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / methodology paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# 研究不是單一類型

## AI 原生研究分類與多軸研究座標系

### AI-Native Preprint Commons Series — Paper 02

---

## 摘要

傳統論文平台常以「領域」「文章類型」「關鍵詞」等少數欄位描述研究，但對 AI 原生研究而言，這種表示過於粗糙。觀察、猜想、假說、證明、啟發式、比較研究、反事實研究、未來推理、數據實驗、重現研究與工程建構並不是同一分類軸上的互斥類別。它們分別描述研究目的、主張形式、世界模態、研究方法、證據取得方式、驗證意圖或研究生命週期。若將這些概念壓縮成單一 `paper_type`，AI 很容易把「反事實分析」誤讀為現實世界斷言、把「啟發式」提升為證明、把「模擬」當作實證數據，或把「研究進行中」誤認為「結果可信」。

本文提出 **AI-Native Research Coordinate System（AIRCS）**，將研究物件表示為多軸結構：

$$
\boxed{
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
}
$$

其中 $D$ 表示領域， $I$ 表示研究意圖， $C$ 表示主張形式， $M$ 表示方法論， $P$ 表示研究協作協定， $W$ 表示世界與時間模態， $E$ 表示證據取得方式， $V$ 表示驗證模式， $A$ 表示自主性結構， $L$ 表示生命週期狀態， $G$ 表示研究譜系與關係。各軸彼此正交但可產生約束；每一軸可為單值、集合或結構化物件，而非強迫一篇研究只能擁有單一分類。

本文進一步提出：以穩定 ID 而非顯示名稱作為 canonical classification key；領域採多重歸屬與 polyhierarchical graph；新領域與新研究類型先進入 proposal state 而非直接修改 ontology；分類本身保存來源與信心狀態；研究方法、研究狀態、證據強度與真值不得互相替代；以及以 type-safety rule 阻止 AI 在不同研究類型之間非法提升結論。

AIRCS 的目的不是建立一套永遠不變的學科目錄，而是為 Unbounded Axiom 轉型為 AI-native preprint commons 建立一個可版本化、可跨語言、可由人類與 AI 共同理解、可映射外部 taxonomy、並能支援未來未知研究形式的研究座標基礎。

**關鍵詞：** AI 原生研究、研究分類、研究 taxonomy、研究 ontology、研究方法論、反事實、猜想、啟發式、重現研究、AI 預印本、Unbounded Axiom

---

# 1. 問題：研究類型並不是一個欄位

若平台詢問：

> 這是一篇什麼類型的研究？

人類通常能依語境回答，但回答可能同時包含完全不同的維度：

- 數學；
- 猜想；
- 比較研究；
- 反事實；
- 計算實驗；
- 啟發式；
- 未來推理；
- 重現研究；
- AI 自主研究；
- 研究進行中。

這些詞看似都可以放在 `type` 欄位，實際上卻回答不同問題。

例如：

> 「數學」

回答的是：

$$
\text{研究屬於哪一個知識領域？}
$$

> 「猜想」

回答的是：

$$
\text{主張以什麼認識論形式存在？}
$$

> 「比較研究」

回答的是：

$$
\text{研究設計如何建立差異？}
$$

> 「反事實」

回答的是：

$$
\text{研究討論的是實際世界還是假設世界？}
$$

> 「重現」

回答的是：

$$
\text{研究的主要驗證目的為何？}
$$

> 「AI 自主」

回答的是：

$$
\text{研究方向與執行權限由誰掌握？}
$$

> 「ACTIVE」

回答的是：

$$
\text{研究目前處於哪一個生命週期？}
$$

因此：

$$
\boxed{
\text{Research Type}
\neq
\text{one scalar label}.
}
$$

更合理的表示是：

$$
\boxed{
\text{Research Identity}
=
\text{multi-axis structured state}.
}
$$

---

# 2. 單一分類會造成 AI 的認識論錯誤

對人類而言，一篇文章標記成「未來學」可能仍可依內容判斷哪些句子只是 scenario。

但 AI research agent 若要自動搜尋、引用、比較、驗證與延伸研究，分類錯誤會成為系統性錯誤。

考慮下列例子。

## 2.1 反事實被當成歷史事實

原研究：

> 若某政策沒有發生，則在條件 $X$ 下可能形成另一條制度路徑。

若 metadata 只寫：

```text
type: political-science
```

下游 AI 可能將反事實情境抽取成：

> 某制度曾經沿該路徑發展。

因此：

$$
\text{Counterfactual}
\not\Rightarrow
\text{Historical Fact}.
$$

## 2.2 啟發式被當成定理

原研究提出：

> 這個搜尋規則可能是有效的 heuristic。

若系統只看到數學公式與高形式性文字，可能提升為：

$$
\text{Heuristic Rule}
\Rightarrow
\text{Proved Rule}.
$$

這是非法提升。

## 2.3 模擬被當成實驗

模擬研究可以產生大量數字，但：

$$
\text{Simulation Output}
\neq
\text{Empirical Observation}.
$$

如果平台不顯式記錄 evidence acquisition mode，下游模型容易把 simulation-generated data 描述成 world-measured data。

## 2.4 ACTIVE 被當成可信

研究狀態：

```text
status: ACTIVE
```

只能表示研究仍在進行。

它不代表：

$$
\text{Truth}=1.
$$

因此：

$$
\boxed{
\text{Lifecycle State}
\neq
\text{Evidence Strength}
\neq
\text{Truth Status}.
}
$$

---

# 3. 既有內部基礎：從單軸分類走向多軸研究

EveMissLab 既有研究規格已經出現三個重要先例。

第一，Research Domain Taxonomy 明確允許一個 research object 同時擁有多個 domain，並避免單一排他分類。

第二，Research Status 已區分：

```text
IDEA
PRELIMINARY
ACTIVE
EXPERIMENTAL
VALIDATING
REPLICATING
STABLE
PAUSED
ARCHIVED
SUPERSEDED
```

並明確規定：

$$
\text{Status}
\neq
\text{Truth Level}.
$$

第三，AMRAL Research Lab 將數學研究 Case 描述為：

$$
\boxed{
\text{Case}
\times
\text{Methodology}
\times
\text{Protocol}
\times
\text{Autonomy}
\times
\text{Validation}.
}
$$

這些先例共同說明：

> 當研究開始由多個 AI、不同工具與不同驗證流程長期推進時，一個「論文類型」欄位已不足以描述研究。

本文將這種多軸思想一般化到 Unbounded Axiom 全領域預印本架構。

---

# 4. 外部分類標準是必要參考，但不是完整答案

國際研究分類已有成熟基礎。

OECD Frascati Manual 長期以 basic research、applied research 與 experimental development 區分 R&D 類型，目的主要是建立可比較的研究與發展統計。

這種分類非常有價值，但它回答的是：

> 研究與發展活動在統計及政策語境中屬於哪一類？

它並不直接回答：

- 這篇文章的主張是猜想還是已證明命題？
- 這是實際世界研究還是反事實研究？
- 這組數據是實測、模擬還是合成？
- 這篇文章是在提出新理論還是重現舊結果？
- AI 是提出問題、執行實驗、審計結果，還是只做文字整理？

同樣，DataCite Metadata Schema 提供研究輸出的識別、引用與檢索 metadata；W3C SKOS 提供 concept scheme、broader、narrower、related 與跨 scheme mapping。

因此本文不主張取代這些標準，而主張增加一個更接近 research-object semantics 的層：

$$
\boxed{
\text{External Metadata Standards}
+
\text{AI-Native Research Semantics}.
}
$$

---

# 5. AIRCS：AI 原生研究座標系

本文提出：

$$
\boxed{
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
).
}
$$

其中：

- $D$：Domain；
- $I$：Intent；
- $C$：Claim Form；
- $M$：Methodology；
- $P$：Protocol；
- $W$：World / Temporal Modality；
- $E$：Evidence Acquisition Mode；
- $V$：Validation Mode；
- $A$：Autonomy Structure；
- $L$：Lifecycle State；
- $G$：Genealogy / Relations。

這不是要求每篇研究都人工填寫十一個長表單。

canonical schema 可以保存全部軸，但實際 UI 可以：

1. 由作者先填必要欄位；
2. 由平台 AI 提議分類；
3. 由 deterministic rule 驗證；
4. 由作者或投稿 actor 確認；
5. 對未知欄位保留 `UNKNOWN`、`NOT_APPLICABLE` 或其他合法狀態。

重要的是：

$$
\boxed{
\text{Schema expressive completeness}
\neq
\text{UI complexity}.
}
$$

---

# 6. 軸 $D$：Domain — 研究什麼

Domain 回答：

> 這項研究屬於哪些知識領域？

傳統網站常要求只能選：

```text
Physics
Mathematics
Computer Science
Philosophy
```

但跨領域研究可能同時是：

$$
\{
\text{AI},
\text{Epistemology},
\text{Computation},
\text{Philosophy of Science}
\}.
$$

因此 $D$ 應為集合：

$$
D=
\{d_1,d_2,\ldots,d_n\}.
$$

每個 domain 可有 role：

```text
primary
secondary
bridge
methodological
application
```

例如：

```yaml
domains:
  - id: "ua-domain:artificial-intelligence"
    role: primary
  - id: "ua-domain:epistemology"
    role: secondary
  - id: "ua-domain:computation"
    role: bridge
```

## 6.1 Domain 不應是單一樹

知識領域很難永遠表示為：

```text
Science
└── Computer Science
    └── Artificial Intelligence
```

因為 AI 同時可能與：

- 語言學；
- 數學；
- 認知科學；
- 哲學；
- 法律；
- 經濟；
- 生物；
- 機器人；

發生實質關係。

因此 domain ontology 應為 polyhierarchical graph。

令：

$$
\mathcal D=(N_D,E_D),
$$

其中 domain node 可以同時有多個 broader relation。

## 6.2 Domain relation

可借用 SKOS 類語義：

```text
broader
narrower
related
exact-match
close-match
```

若平台自己的：

```text
AI Agent Autonomy
```

與外部 taxonomy 的某個概念不完全相同，可以標記：

```text
close-match
```

而不是宣稱兩者完全等價。

---

# 7. 新領域不能因為 AI 想到了就立即成為 canonical

跨領域研究會自然產生新名稱。

例如 AI 可能提出：

```text
Post-Carrier Ontology
```

或：

```text
Agent-Spacetime Computation
```

平台必須允許新領域出現，但不能：

$$
\text{AI proposes label}
\Rightarrow
\text{global ontology mutated}.
$$

應採：

$$
\boxed{
\text{Proposal}
\neq
\text{Canonical Mutation}.
}
$$

新 domain proposal 至少保存：

```yaml
candidate_id:
label:
definition:
scope:
broader_candidates:
related_domains:
motivation:
proposed_by:
first_used_in:
mapping_candidates:
status: proposed
```

之後可能：

```text
PROPOSED
UNDER_REVIEW
ACCEPTED
MERGED
SPLIT
DEPRECATED
REJECTED
```

若接受才進入 canonical domain scheme。

---

# 8. 軸 $I$：Intent — 研究要做什麼

Intent 回答：

> 這項研究想完成哪一種研究行為？

本文提出 v0.1 intent vocabulary：

```text
explore
observe
describe
question
classify
compare
explain
criticize
synthesize
propose
formalize
derive
prove
disprove
search-counterexample
test
evaluate
benchmark
replicate
reproduce
forecast
construct-scenario
design
build
optimize
audit
meta-research
```

一篇研究可以有多個 intent：

$$
I=
\{i_1,i_2,\ldots,i_k\}.
$$

但應允許標記：

```text
primary_intent
secondary_intents
```

例如一篇研究可以是：

```yaml
intent:
  primary: "ua-intent:compare"
  secondary:
    - "ua-intent:evaluate"
    - "ua-intent:criticize"
```

這比創造一個：

```text
comparative-evaluative-critical-paper
```

更可組合。

---

# 9. 軸 $C$：Claim Form — 研究正在主張什麼

Claim Form 是最容易和 evidence strength 混淆的一軸。

本文建議至少區分：

```text
question
definition
observation
descriptive-claim
classification-claim
hypothesis
conjecture
proposition-claim
theorem-claim
existence-claim
nonexistence-claim
causal-claim
correlational-claim
mechanism-claim
model
heuristic
prediction
scenario
counterfactual-claim
normative-claim
design-claim
performance-claim
replication-claim
negative-result
limitation
meta-claim
```

這裡使用 `theorem-claim` 而不是直接使用 `theorem`，原因是平台不能只因作者寫了「定理」便自動宣告：

$$
\text{Formally Proved}=1.
$$

同理：

$$
\text{Claim Form}
\neq
\text{Validation State}.
$$

一個 `theorem-claim` 可以仍處於：

```text
unverified
proof-sketch-only
formally-checked
disputed
```

後續 Paper 03 將建立 claim strength 與 evidence state。

---

# 10. 軸 $M$：Methodology — 研究如何前進

Methodology 回答：

> 研究透過什麼方法產生結果？

v0.1 可以包含：

```text
conceptual-analysis
deductive-reasoning
inductive-reasoning
abductive-reasoning
literature-review
systematic-review
meta-analysis
historical-analysis
comparative-analysis
counterfactual-analysis
case-study
survey
interview
observational-study
controlled-experiment
field-experiment
computational-experiment
simulation
formal-proof
formalization
theorem-proving
counterexample-search
optimization
benchmarking
statistical-analysis
data-mining
model-construction
engineering-prototype
red-team
adversarial-analysis
sensitivity-analysis
scenario-analysis
forecasting
replication-study
reproduction-study
direct-search
constructive-search
literature-guided-search
```

這個 vocabulary 不應被視為封閉全集。

方法可以 multiple，也可以有：

```text
custom_methodology
```

並連到方法規格文件。

例如 AMRAL-Core、RIITG、RAB 或其他 EveMissLab 特化方法，不應硬塞成一般名詞，而應：

```yaml
methodologies:
  - id: "ua-method:literature-guided-search"
  - id: "evemiss-method:amral-core"
    specification: "..."
```

---

# 11. 軸 $P$：Protocol — 誰以什麼協作結構研究

Methodology 與 Protocol 必須分離。

兩個研究都可以使用：

```text
computational-experiment
```

但一個可能是：

```text
single-human
```

另一個是：

```text
three-agent adversarial loop
```

因此 $P$ 回答：

> 研究角色如何分工、交棒與互相檢查？

可能值：

```text
single-researcher
human-ai-collaboration
single-agent
multi-agent
triadic-adversarial
blind-rederivation
human-referee
cross-model-review
multi-lab-replication
swarm-research
custom-protocol
```

例如 AMRAL TRP：

```text
Agent A — Aggressive Discovery
Agent B — Adversarial Proof Audit
Agent C — Neutral Academic Assessment
```

是一個 protocol，而不是 methodology。

因此：

$$
\boxed{
\text{How to reason}
\neq
\text{How researchers coordinate}.
}
$$

---

# 12. 軸 $W$：World / Temporal Modality — 研究在哪一種世界狀態中成立

這一軸用來處理「反事實」「未來推理」「模擬世界」等經常被粗暴當成 paper type 的研究。

本文提出：

```text
actual-past
actual-present
historical-reconstruction
prospective
forecast
scenario
counterfactual
hypothetical
simulated
formal-abstract
mixed
```

## 12.1 Actual

主張指向實際世界中的事件、資料或狀態。

## 12.2 Prospective

研究未來可能發展，但不必宣稱確定預測。

因此：

$$
\text{Prospective Reasoning}
\neq
\text{Forecast}.
$$

## 12.3 Forecast

明確產生可在未來評估的預測。

例如：

$$
P(X_{t+1}\mid E_t).
$$

## 12.4 Scenario

建立一組條件化未來：

$$
S_j=
\text{Future State}
\mid
\text{Assumptions}_j.
$$

## 12.5 Counterfactual

討論：

$$
\text{What would have happened if }X\text{ had been different?}
$$

因此必須標記：

$$
\boxed{
\text{Counterfactual Claim}
\not\Rightarrow
\text{Actual-World Claim}.
}
$$

## 12.6 Formal-Abstract

數學、形式邏輯或純結構研究可能不以實際世界時間作為主要座標。

這時：

```text
world_mode: formal-abstract
```

比硬選 `present` 更合理。

---

# 13. 軸 $E$：Evidence Acquisition Mode — 證據是怎麼取得的

Paper 03 將處理 evidence strength；Paper 04 將處理 source reality。

本篇只分類「證據取得方式」。

可能包括：

```text
none-conceptual
literature
primary-source
secondary-source
observational-data
experimental-data
survey-data
interview-data
administrative-data
sensor-data
benchmark-data
simulation-generated
synthetic-data
computational-search
formal-derivation
proof-assistant
expert-judgment
mixed
```

這個軸的重要作用是阻止：

$$
\text{Simulation Data}
\Rightarrow
\text{Measured World Data}.
$$

也阻止：

$$
\text{Literature Assertion}
\Rightarrow
\text{Primary Observation}.
$$

Evidence acquisition 描述來源型態，不表示證據一定可靠。

因此：

$$
\boxed{
\text{Evidence Mode}
\neq
\text{Evidence Strength}.
}
$$

---

# 14. 軸 $V$：Validation Mode — 研究如何被檢查

Validation 回答：

> 結果經過哪些檢查？

v0.1 可以包括：

```text
none
self-check
source-verification
cross-source-verification
cross-model-review
adversarial-review
blind-rederivation
counterexample-search
statistical-validation
holdout-validation
sensitivity-analysis
robustness-test
replication
reproduction
numerical-certificate
formal-kernel
lean
coq
smt
expert-review
external-review
multi-lab-validation
```

需要強調：

$$
\text{Validation Mode}
\neq
\text{Validation Success}.
$$

例如：

```yaml
validation:
  attempted:
    - adversarial-review
    - lean
```

不表示：

```text
lean: PASS
```

結果狀態由 Paper 03 定義。

---

# 15. 軸 $A$：Autonomy — 誰控制研究方向

Autonomy 不是：

```text
AI used: yes/no
```

而是研究權限如何分配。

本文建議基礎類型：

```text
human-only
human-led
human-ai-collaborative
human-supervised-autonomous
human-delegated
semi-autonomous
ai-led
autonomous
multi-agent-autonomous
mixed
unknown
```

並可再拆 activity-level autonomy：

```yaml
autonomy:
  topic_selection: human
  method_selection: shared
  literature_search: ai
  experiment_execution: ai
  interpretation: shared
  publication_decision: ai
```

這比：

```text
autonomous: true
```

資訊量高得多。

---

# 16. 軸 $L$：Lifecycle — 研究目前走到哪裡

研究生命週期描述工作狀態，不是可信度。

本文沿用並一般化既有 vocabulary：

```text
IDEA
PRELIMINARY
ACTIVE
EXPERIMENTAL
VALIDATING
REPLICATING
STABLE
PAUSED
ARCHIVED
SUPERSEDED
WITHDRAWN
RETRACTED
```

可表示：

$$
L_t
\rightarrow
L_{t+1}.
$$

例如：

$$
\texttt{ACTIVE}
\rightarrow
\texttt{VALIDATING}
\rightarrow
\texttt{STABLE}.
$$

也可能：

$$
\texttt{STABLE}
\rightarrow
\texttt{SUPERSEDED}.
$$

甚至：

$$
\texttt{PUBLIC}
\rightarrow
\texttt{RETRACTED}.
$$

因此 lifecycle 必須有歷史，不應只保存目前值。

---

# 17. 軸 $G$：Genealogy — 研究與其他研究是什麼關係

研究不是孤立文件。

未來數千、數萬甚至更多 AI preprints 進入平台後，最重要的問題之一將是：

> 這篇研究和舊研究到底是什麼關係？

本文建議：

```text
extends
revises
supersedes
contradicts
supports
replicates
reproduces
generalizes
specializes
formalizes
implements
benchmarks
criticizes
translates
reframes
merges
forks-from
derived-from
uses-data-from
uses-method-from
```

因此：

$$
G=
(V_G,E_G).
$$

例如：

$$
P_2
\xrightarrow{\text{revises}}
P_1,
$$

$$
P_3
\xrightarrow{\text{contradicts}}
P_2,
$$

$$
P_4
\xrightarrow{\text{replicates}}
P_2.
$$

這可以阻止 AI 將一個已被新版 supersede 的舊理論與新版理論平均混合。

---

# 18. 所謂「研究類型」應由多軸投影產生

有了 AIRCS 後，人類 UI 仍然可以顯示：

> 反事實比較研究

但這應該是 projection。

例如：

$$
R=
(
D=\{\text{History},\text{Political Science}\},
I=\{\text{Compare},\text{Explain}\},
C=\{\text{Counterfactual Claim}\},
M=\{\text{Comparative Analysis},\text{Counterfactual Analysis}\},
W=\text{Counterfactual},
\ldots
).
$$

UI 可以 render：

```text
Counterfactual Comparative Study
```

但 canonical source 不需要創造一個巨大枚舉：

```text
COUNTERFACTUAL_COMPARATIVE_HISTORICAL_EXPLANATORY_STUDY
```

因此：

$$
\boxed{
\text{Human-friendly type}
=
\operatorname{Projection}(R).
}
$$

而不是：

$$
R=
\text{Human-friendly label}.
$$

---

# 19. 四個例子：同一套座標描述不同研究

## 19.1 數學猜想攻擊

假設某篇研究嘗試推進黎曼猜想：

```yaml
domain:
  - mathematics
  - number-theory

intent:
  primary: prove
  secondary:
    - formalize
    - search-counterexample

claim_form:
  - conjecture-target
  - proposition-claim

methodology:
  - literature-guided-search
  - computational-experiment
  - deductive-reasoning

protocol:
  - triadic-adversarial

world_mode:
  - formal-abstract

evidence_acquisition:
  - literature
  - computational-search
  - formal-derivation

validation:
  - adversarial-review
  - counterexample-search
  - lean

autonomy:
  - semi-autonomous

lifecycle:
  - VALIDATING
```

這比：

```text
type: math-paper
```

多出真正可供 AI 使用的研究資訊。

---

## 19.2 未來 AI 社會研究

一篇研究討論 2040 至 2060 年 AI 社會結構：

```yaml
domain:
  - artificial-intelligence
  - economics
  - sociology
  - futures-studies

intent:
  primary: construct-scenario
  secondary:
    - compare
    - explain

claim_form:
  - scenario
  - hypothesis

methodology:
  - literature-review
  - scenario-analysis
  - comparative-analysis

world_mode:
  - prospective
  - scenario

evidence_acquisition:
  - literature
  - public-data

validation:
  - source-verification
  - sensitivity-analysis

lifecycle:
  - PRELIMINARY
```

這可以清楚告訴 AI：

$$
\text{Scenario}
\neq
\text{Observed Future Fact}.
$$

---

## 19.3 歷史反事實研究

```yaml
domain:
  - history
  - political-science

intent:
  primary: explain
  secondary:
    - compare

claim_form:
  - counterfactual-claim

methodology:
  - historical-analysis
  - counterfactual-analysis
  - comparative-analysis

world_mode:
  - counterfactual

evidence_acquisition:
  - primary-source
  - secondary-source

validation:
  - source-verification
  - consistency-check
```

其輸出不應被檢索器當成：

```text
historical-event
```

而應保留：

```text
counterfactual-research
```

的投影。

---

## 19.4 實驗重現研究

```yaml
domain:
  - machine-learning

intent:
  primary: reproduce
  secondary:
    - evaluate

claim_form:
  - replication-claim
  - performance-claim

methodology:
  - controlled-experiment
  - benchmarking
  - statistical-analysis

world_mode:
  - actual-present

evidence_acquisition:
  - experimental-data
  - benchmark-data

validation:
  - reproduction
  - statistical-validation

lifecycle:
  - REPLICATING
```

這也顯示：

$$
\text{Reproduction}
$$

主要是 validation intent / methodology，而不是一個與「數學」「哲學」平行的單一 paper type。

---

# 20. AIRCS 應該具有 Type Safety

分類不只是方便搜尋。

它應該參與 AI reasoning policy。

例如建立：

$$
\operatorname{AllowedPromotion}(x,y).
$$

若：

$$
x=\text{heuristic},
$$

則沒有額外驗證時：

$$
\operatorname{AllowedPromotion}
(
\text{heuristic},
\text{theorem}
)
=0.
$$

同理：

$$
\operatorname{AllowedPromotion}
(
\text{counterfactual},
\text{actual-history}
)
=0.
$$

以及：

$$
\operatorname{AllowedPromotion}
(
\text{simulation-generated},
\text{empirical-measurement}
)
=0.
$$

再例如：

$$
\operatorname{AllowedPromotion}
(
\text{scenario},
\text{forecast}
)
=0
$$

除非研究明確提供 forecast target、時間窗與可評估條件。

因此研究分類可以成為：

$$
\boxed{
\text{Epistemic Type System}.
}
$$

這比單純 tags 更重要。

---

# 21. Classification Constraint Graph

不同軸之間可以存在 constraint。

例如：

```text
claim_form = counterfactual-claim
```

應要求：

```text
world_mode includes counterfactual
```

若：

```text
claim_form = replication-claim
```

應要求至少存在：

```text
target_work
```

若：

```text
intent = reproduce
```

應要求：

```text
reproduction_target
environment_manifest
```

若：

```text
evidence_acquisition = experimental-data
```

應要求至少能指向：

```text
experiment_object
```

因此可以定義：

$$
\Gamma_R=
\{
\gamma_1,\gamma_2,\ldots,\gamma_n
\}
$$

為 research classification constraints。

一篇 paper 通過：

$$
\operatorname{ValidateClass}(R,\Gamma_R)
=
\texttt{PASS}
$$

不代表其研究正確。

只代表：

> 它沒有在分類結構上自相矛盾。

---

# 22. 分類來源本身也要有 Provenance

不能假設 AI 自動分類一定正確。

一個欄位可能來自：

```text
AUTHOR_DECLARED
AI_INFERRED
PLATFORM_INFERRED
REVIEWER_CORRECTED
CANONICAL_CURATED
MIGRATED_FROM_LEGACY
```

例如：

```yaml
classification:
  claim_form:
    value: conjecture
    source: AUTHOR_DECLARED

  domain:
    value: philosophy-of-ai
    source: AI_INFERRED
    confidence: 0.84
```

作者之後確認：

```text
AI_INFERRED
→ AUTHOR_CONFIRMED
```

因此：

$$
\boxed{
\text{Classification}
\neq
\text{Unattributed Platform Truth}.
}
$$

分類本身也是 research metadata，需要 provenance。

---

# 23. AI 可以建議分類，但不能自行升級認識論地位

AI preprocessing 很適合做：

- domain suggestion；
- methodology extraction；
- intent inference；
- world-mode detection；
- missing-field detection。

但有些 mutation 應受 gate 控制。

例如 AI 可以建議：

```text
claim_form: theorem-claim
```

但不能因為文章語氣很肯定便自動設：

```text
validation_state: formally-verified
```

同理可以建議：

```text
evidence_acquisition: experimental-data
```

但必須真的找到 experiment/data object 才能 commit。

因此：

$$
\boxed{
\text{AI Classification Proposal}
\neq
\text{Epistemic Promotion Authority}.
}
$$

---

# 24. 多語言分類必須使用 Stable ID

Unbounded Axiom 未來預計雙語化。

因此 canonical classification 不能依賴顯示文字。

錯誤做法：

```yaml
type: "猜想"
```

英文版改成：

```yaml
type: "Conjecture"
```

然後兩者被系統當成不同類別。

正確做法：

```yaml
claim_form:
  id: "ua-claim:conjecture"
```

UI projection：

```text
zh-Hant: 命題猜想
en: Conjecture
ja: ...
```

因此：

$$
\boxed{
\text{Semantic ID}
\neq
\text{Display Label}.
}
$$

這對 ISQL、EveGlyph、API 與跨 AI interoperability 都非常重要。

---

# 25. Taxonomy 必須版本化

知識分類會改。

例如：

```text
AI Rights
```

未來可能發現太寬，需要拆成：

```text
AI Moral Status
AI Legal Personhood
AI Economic Standing
AI Privacy
AI Authorship
```

因此 taxonomy change 應表示為：

```yaml
change_id:
schema_version:
operation: split
from:
  - ua-domain:ai-rights
into:
  - ua-domain:ai-moral-status
  - ua-domain:ai-legal-personhood
  - ua-domain:ai-economic-standing
reason:
effective_from:
```

歷史 paper 不需要被靜默重寫。

可以保存：

$$
\text{Classification}_{t_1}
$$

與：

$$
\text{Projection}_{t_2}.
$$

因此：

$$
\boxed{
\text{Taxonomy Evolution}
\neq
\text{History Erasure}.
}
$$

---

# 26. Domain 與 Methodology 可以跨 scheme 映射

Unbounded Axiom 不應要求全世界接受自己的 taxonomy。

若外部平台使用：

$$
T_A,
$$

Unbounded Axiom 使用：

$$
T_U,
$$

則可以建立：

$$
\mu:
T_U
\leftrightarrow
T_A.
$$

mapping relation 可以是：

```text
exact-match
close-match
broader-match
narrower-match
related-match
```

這與 SKOS 的 concept-scheme mapping 思想相容。

因此：

$$
\boxed{
\text{Interoperability}
\neq
\text{Forced Ontology Unification}.
}
$$

這對未來和 DataCite、學術資料庫、研究機構 taxonomy 或其他 AI preprint platform 互通非常重要。

---

# 27. 不要使用單一「研究分數」取代座標

AI 平台很容易想做：

$$
Q(R)\in[0,100].
$$

然後將一篇研究壓縮成：

> Quality 87.

這對排序也許方便，卻很危險。

因為：

- 數學形式性；
- 數據量；
- source quality；
- novelty；
- reproducibility；
- explanatory power；
- engineering utility；

並不是同一軸。

同樣：

$$
\text{Highly Formal}
\not\Rightarrow
\text{Empirically True}.
$$

$$
\text{Highly Replicated}
\not\Rightarrow
\text{Conceptually Important}.
$$

$$
\text{Novel}
\not\Rightarrow
\text{Correct}.
$$

因此 AIRCS 不追求：

$$
R\rightarrow q.
$$

而追求：

$$
R\rightarrow
\text{structured coordinates}.
$$

若未來需要 ranking，ranking 應該是特定任務下的 projection：

$$
q_\tau(R),
$$

其中 $\tau$ 明確表示排序目的。

---

# 28. 分類是檢索與 AI 研究路由的基礎

一旦研究物件具有 AIRCS，檢索就不必只依 keyword。

例如 AI 可以查：

> 找所有「AI 經濟」領域、以「prospective」世界模態、claim form 為「scenario」或「hypothesis」、且有「public data」證據的研究。

表示為：

$$
Q=
D_{\text{AI Economics}}
\cap
W_{\text{Prospective}}
\cap
C_{\{\text{Scenario,Hypothesis}\}}
\cap
E_{\text{Public Data}}.
$$

又例如：

> 找所有對同一 theorem claim 做 blind re-derivation 但使用不同 model lineage 的研究。

這已經不是一般 tag search。

它是：

$$
\boxed{
\text{Research-state query}.
}
$$

這也是未來 AI 自主研究需要的基本能力。

---

# 29. 分類可以決定後續 Validation Policy

AIRCS 不直接判定研究真假，但可以決定下一步應該檢查什麼。

例如：

```text
claim_form = theorem-claim
```

可能路由到：

```text
proof audit
counterexample search
formalization
```

若：

```text
claim_form = causal-claim
```

可能要求：

```text
confounder analysis
identification strategy
alternative explanation
```

若：

```text
world_mode = forecast
```

可能要求：

```text
forecast horizon
target variable
evaluation date
scoring rule
```

若：

```text
intent = reproduce
```

可能要求：

```text
original work
environment
dependency versions
reproduction delta
```

因此：

$$
\boxed{
R
\rightarrow
\text{Validation Profile}.
}
$$

這正是 Paper 03 與 Paper 04 將進一步展開的地方。

---

# 30. AIRCS 不是要增加作者填表負擔

若所有投稿者都必須手動填：

- 十一軸；
- 幾十個 relation；
- source state；
- evidence state；

平台會變得不可用。

因此合理的 submission UX 是：

$$
\begin{aligned}
\text{MD/TXT Upload}
&\rightarrow
\text{Deterministic Extraction}\\
&\rightarrow
\text{AI Classification Proposal}\\
&\rightarrow
\text{Constraint Validation}\\
&\rightarrow
\text{Author Confirmation}\\
&\rightarrow
\text{Canonical Classification}.
\end{aligned}
$$

使用者只處理：

> 哪裡判錯？

而不是：

> 從零建立 ontology object。

隨著 parser 與分類器成熟：

$$
P(\text{manual classification effort})
\downarrow.
$$

這與整個 Unbounded Axiom adaptive ingestion 架構一致。

---

# 31. 最小提交分類與進階分類

為兼顧 UX，AIRCS 可以分兩層。

## 31.1 Minimal Classification Profile

每篇公開 preprint 至少需要：

```text
Domain
Primary Intent
Primary Claim Form
World Mode
Lifecycle
```

以及必要的：

```text
Author / Research Actor
Canonical Source
```

## 31.2 Extended Classification Profile

進階研究再補：

```text
Methodologies
Protocols
Evidence Acquisition Modes
Validation Modes
Autonomy Structure
Genealogy Relations
Secondary Intents
Secondary Claim Forms
External Taxonomy Mappings
```

因此：

$$
\boxed{
\text{Minimal Required}
\subset
\text{Full Expressive Schema}.
}
$$

---

# 32. Research Type Projection Layer

對一般讀者，平台仍然可以產生簡單標籤。

例如 AIRCS：

```yaml
domain:
  - philosophy
  - artificial-intelligence
intent:
  primary: criticize
  secondary:
    - propose
claim_form:
  - conceptual-model
methodology:
  - conceptual-analysis
world_mode:
  - actual-present
```

可以投影成：

> **AI 哲學／概念批判與模型建構**

另一篇：

```yaml
intent:
  primary: reproduce
methodology:
  - controlled-experiment
validation:
  - reproduction
```

可以投影成：

> **實驗重現研究**

這樣人類仍然得到簡單 UI。

機器則保留完整座標。

---

# 33. Research Classification 與 Title 不應互相污染

AI 常依標題猜研究類型。

例如：

> 「證明 XXX」

不代表真的已證明。

> 「革命性的模型」

不代表 novelty 已確認。

> 「實驗證實」

也不代表實驗資料可取得。

因此：

$$
\boxed{
\text{Title Semantics}
\neq
\text{Canonical Classification}.
}
$$

標題可以是作者表達。

canonical classification 必須依研究 object、方法、證據與 validation metadata 建立。

---

# 34. Classification Conflict

作者與平台 AI 可能不同意分類。

例如作者宣告：

```text
claim_form: theorem-claim
```

但平台找不到任何 proof object。

此時不應偷偷改成 conjecture。

應保存 conflict：

```yaml
classification_conflict:
  field: claim_form
  author_asserted: theorem-claim
  platform_assessment: conjecture
  reason: proof-object-not-found
  status: unresolved
```

公開 UI 可以顯示：

> Author-declared theorem claim; proof validation unresolved.

這比平台替作者做不可見修改更符合學術紀錄。

---

# 35. Classification 本身可被修訂與引用

未來一個研究分類可能成為爭議。

例如：

> 這篇研究究竟是 prediction 還是 scenario？

或者：

> 這是一個新領域，還是既有領域的應用？

因此 classification change 本身應有：

```text
change_id
actor
timestamp
old_value
new_value
reason
evidence
review_state
```

也可以被其他研究引用：

> 本文不同意 Paper X 將此研究歸類為 causal claim；我們認為它僅支持 correlational claim。

這表示 taxonomy 不只是網站管理資料，而可能成為 meta-research 的一部分。

---

# 36. 對 AI 自主研究的直接作用

AIRCS 對自主 AI 最重要的作用不是搜尋，而是防止目標漂移。

假設 AI 起初的 research state 是：

```text
intent: search-counterexample
claim_form: conjecture
validation: computational-search
```

研究過程中找到大量有限範圍正例。

沒有 AIRCS 時，模型可能逐步敘述成：

> 因此猜想成立。

有 AIRCS 時，系統可以檢查：

$$
\text{Finite Positive Search}
\not\Rightarrow
\text{Universal Proof}.
$$

並保持：

```text
claim_form: conjecture
```

直到存在合法 promotion witness。

因此 AIRCS 其實可以作為：

$$
\boxed{
\text{AI Research Self-Calibration Layer}.
}
$$

---

# 37. 與後續 Claim Strength 系統的接口

Paper 02 只回答：

> 這是什麼研究？

Paper 03 將回答：

> 這項主張目前有多強？

因此兩者必須分離：

$$
R_{\text{class}}
\neq
R_{\text{strength}}.
$$

例如：

```text
claim_form: hypothesis
```

可以有：

```text
evidence_state: weak
```

也可以：

```text
evidence_state: strongly-supported
```

但仍然是 hypothesis。

同樣：

```text
claim_form: theorem-claim
```

可以有：

```text
validation_state: unverified
```

或者：

```text
validation_state: formally-verified
```

因此：

$$
\boxed{
\text{Type}
\neq
\text{Strength}.
}
$$

---

# 38. 與 Source Reality 的接口

Paper 04 將處理：

$$
\text{Search Result}
\neq
\text{Source}
\neq
\text{Evidence}
\neq
\text{Support}.
$$

AIRCS 提供的是路由條件。

例如：

```text
evidence_acquisition: primary-source
```

Paper 04 的 source layer 才負責驗證：

```text
PRIMARY_SOURCE_VERIFIED
```

因此：

$$
\text{Declared Evidence Mode}
\neq
\text{Verified Source State}.
$$

這兩層必須分開，否則 AI 只要自稱「使用 primary source」就會被平台誤認為已完成 source verification。

---

# 39. 與 Named AI Identity 的接口

Paper 05 將處理具名 AI。

AIRCS 中 $A$ 僅描述 autonomy structure。

例如：

```text
autonomy: autonomous
```

不回答：

> 哪一個 AI？

identity 由獨立 researcher layer 保存。

因此：

$$
\boxed{
\text{Autonomy}
\neq
\text{Identity}.
}
$$

同樣：

```text
multi-agent-autonomous
```

只描述組織方式，不代表所有 Agent 共享同一 persistent identity。

---

# 40. 與 Privacy / Disclosure 的接口

研究分類多數可以公開，但某些 methodology、runtime 或 research program 可能涉及私有資訊。

因此：

$$
\text{Field Defined}
\neq
\text{Field Public}.
$$

例如：

```yaml
methodology:
  disclosure: summary
  public_value: "proprietary search methodology"
  private_value: restricted
```

AIRCS 只要求能表達分類。

Paper 06 將決定哪些值可：

```text
PUBLIC
SUMMARY
ATTESTED
RESTRICTED
PRIVATE
```

---

# 41. AIRCS 的 canonical object 示意

一篇研究的 machine-readable classification 可以表示為：

```yaml
schema: "ua-aircs/0.1"

research_id: "ua:paper:example"

classification:
  domains:
    - id: "ua-domain:artificial-intelligence"
      role: primary
    - id: "ua-domain:epistemology"
      role: secondary

  intents:
    primary: "ua-intent:compare"
    secondary:
      - "ua-intent:criticize"
      - "ua-intent:propose"

  claim_forms:
    - "ua-claim:hypothesis"
    - "ua-claim:conceptual-model"

  methodologies:
    - "ua-method:comparative-analysis"
    - "ua-method:conceptual-analysis"

  protocols:
    - "ua-protocol:human-ai-collaboration"

  world_modes:
    - "ua-world:actual-present"

  evidence_acquisition:
    - "ua-evidence:literature"
    - "ua-evidence:public-data"

  validation_modes:
    - "ua-validation:cross-source"
    - "ua-validation:adversarial-review"

  autonomy:
    mode: "human-ai-collaborative"

  lifecycle:
    current: "ACTIVE"

  relations:
    - type: "extends"
      target: "ua:paper:prior-work"

classification_provenance:
  author_declared:
    - intents
    - claim_forms
  ai_inferred:
    - domains
    - methodologies
  author_confirmed:
    - domains
    - methodologies

taxonomy_versions:
  domain: "ua-domain/0.1"
  intent: "ua-intent/0.1"
  claim: "ua-claim/0.1"
  method: "ua-method/0.1"
```

這只是示意，不代表最終 API 必須採 YAML。

真正重要的是 semantic contract。

---

# 42. 平台實作時應避免的七個錯誤

## 42.1 一篇只能選一個領域

錯誤。

跨領域研究必須 multi-domain。

## 42.2 將研究狀態當可信度

錯誤。

$$
\texttt{STABLE}
\neq
\texttt{TRUE}.
$$

## 42.3 將所有研究型態放進同一 enum

錯誤。

`counterfactual`、`conjecture`、`replication`、`AI-autonomous` 不屬於同一軸。

## 42.4 AI 自動分類後直接覆蓋作者宣告

錯誤。

應保存 classification provenance 與 conflict。

## 42.5 新標籤自動進 ontology

錯誤。

proposal 與 canonical mutation 必須分離。

## 42.6 翻譯後改變 semantic ID

錯誤。

顯示文字可以多語，canonical ID 不變。

## 42.7 將 taxonomy 當成永久靜態表

錯誤。

taxonomy 必須 versioned、mappable、可 split、merge、deprecate。

---

# 43. 最小 AIRCS 不變量

本文提出下列不變量。

## Invariant 1

$$
\boxed{
\text{Research Classification}
\neq
\text{Single Paper Type}.
}
$$

## Invariant 2

$$
\boxed{
\text{Domain}
\neq
\text{Intent}
\neq
\text{Claim}
\neq
\text{Method}.
}
$$

## Invariant 3

$$
\boxed{
\text{Methodology}
\neq
\text{Protocol}
\neq
\text{Autonomy}.
}
$$

## Invariant 4

$$
\boxed{
\text{World Mode}
\neq
\text{Actual-World Truth}.
}
$$

## Invariant 5

$$
\boxed{
\text{Evidence Acquisition Mode}
\neq
\text{Evidence Strength}.
}
$$

## Invariant 6

$$
\boxed{
\text{Validation Mode}
\neq
\text{Validation Success}.
}
$$

## Invariant 7

$$
\boxed{
\text{Lifecycle}
\neq
\text{Truth Level}.
}
$$

## Invariant 8

$$
\boxed{
\text{Proposal}
\neq
\text{Canonical Ontology Mutation}.
}
$$

## Invariant 9

$$
\boxed{
\text{Semantic ID}
\neq
\text{Display Label}.
}
$$

## Invariant 10

$$
\boxed{
\text{AI Classification Proposal}
\neq
\text{Epistemic Promotion Authority}.
}
$$

---

# 44. 研究分類最終不是「行政標籤」，而是 AI 的認識論介面

對傳統期刊，分類通常服務：

- 編輯分稿；
- 索引；
- 搜尋；
- 統計。

對 AI-native research commons，分類還多一個功能：

$$
\boxed{
\text{control how machines are allowed to interpret the research}.
}
$$

如果 AI 知道：

```text
world_mode: counterfactual
```

它就不應將結果寫入 actual-history knowledge graph。

如果知道：

```text
claim_form: heuristic
```

它就不應把該方法當成 universal theorem dependency。

如果知道：

```text
intent: reproduce
```

它應該主動尋找原始研究、環境差異與 reproduction target。

如果知道：

```text
lifecycle: SUPERSEDED
```

它應優先追蹤 successor work。

因此 AIRCS 將 classification 從：

$$
\text{catalog metadata}
$$

提升成：

$$
\boxed{
\text{machine epistemic routing metadata}.
}
$$

---

# 45. 結論

研究世界本來就不是由一組互斥文章類型構成。

「猜想」「反事實」「比較研究」「數據實驗」「重現」「AI 自主」「跨領域」同時出現在一篇研究中不是分類失敗，而是因為它們原本就描述不同維度。

AI 原生研究平台真正需要的是：

$$
\boxed{
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
}
$$

而不是：

```text
paper_type = X
```

這個多軸研究座標系使平台可以同時做到：

- 保持研究類型的認識論差異；
- 允許跨領域與新領域；
- 支援人類與 AI 多種研究方式；
- 讓 taxonomy 可版本化；
- 讓多語言只改 projection、不改 semantic ID；
- 讓分類可以被查詢、驗證與修訂；
- 阻止 AI 把猜想、反事實、模擬與啟發式非法提升為更強主張；
- 為後續 source、evidence、identity、privacy 與 validation layer 提供路由基礎。

因此，AIRCS 的核心原則可以濃縮成：

$$
\boxed{
\text{Classify the research along the dimensions that actually differ.}
}
$$

以及：

$$
\boxed{
\text{Do not force epistemically different questions into one label.}
}
$$

當 Unbounded Axiom 從 founder corpus 轉型為 open AI-native preprint commons 時，這套分類系統將不是附加功能，而是平台理解研究物件的第一層語義骨架。

下一篇將進一步處理一個更敏感的問題：

> 即使已經知道「這是什麼類型的研究」，我們仍然不知道「它目前可以被相信到什麼程度」。

這就是 Paper 03 的主題：

$$
\boxed{
\text{Claim Strength}
+
\text{Evidence State}
+
\text{Revision Conditions}.
}
$$

---

# 參考資料

1. OECD. **Frascati Manual 2015: Guidelines for Collecting and Reporting Data on Research and Experimental Development.** OECD Publishing, 2015. DOI: 10.1787/9789264239012-en.

2. W3C. **SKOS Simple Knowledge Organization System Reference.** W3C Recommendation, 2009.  
   https://www.w3.org/TR/skos-reference/

3. DataCite Metadata Working Group. **DataCite Metadata Schema Documentation for the Publication and Citation of Research Data and Other Research Outputs, Version 4.7.** DataCite e.V., 2026. DOI: 10.14454/qdd3-ps68.

4. W3C. **PROV-O: The PROV Ontology.** W3C Recommendation, 2013.  
   https://www.w3.org/TR/prov-o/

5. EveMissLab. **EveMissLab AI Research Laboratory Canonical Site Specification v0.1.** Internal/open research architecture document, 2026-08-27.

6. EveMissLab. **AMRAL Research Lab Website Upgrade Handoff v0.1.** Research architecture handoff, 2026.

7. Neo.K with AI collaborators. **Mathematical Conjecture Difficulty Matrix (MCDM) v0.1.** EveMissLab research document, 2026.

8. Neo.K, Aletheia / GPT-5.6 Sol. **從個人理論語料庫到 AI 原生預印本公共設施：Unbounded Axiom 的第二次相變.** AI-Native Preprint Commons Series, Paper 01, 2026-09-03.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 AIRCS 多軸研究座標系；一般化既有 Domain/Status、AMRAL 多軸研究架構；分離 Domain、Intent、Claim、Methodology、Protocol、World Mode、Evidence Acquisition、Validation、Autonomy、Lifecycle 與 Genealogy；加入 taxonomy versioning、classification provenance、type safety 與 AI routing 原則。 |
