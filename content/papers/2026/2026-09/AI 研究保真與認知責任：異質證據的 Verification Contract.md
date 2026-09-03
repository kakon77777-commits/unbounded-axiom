# AI 研究保真與認知責任：異質證據的 Verification Contract

## AI Research Fidelity and Epistemic Responsibility: Verification Contracts for Heterogeneous Evidence

**系列**：AI 原生分散式組織系列，第 6 篇／共 10 篇  
**系列英文名**：AI-Native Distributed Organization Series  
**文件編號**：EML-ANDO-2026-06-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Research Fidelity／Verification Contract／Epistemic Governance／AI Research Organization  
**狀態**：Public Theory Draft  
**直接前置**：《分散式認知研究組織：論文庫如何從 Corpus 變成 Research Environment》v0.1；《共享狀態中心論》v0.1；《AI 單次品質論》v0.1；《委任主權論》v0.1  
**Source fingerprint**：見正式 source package `SHA256SUMS.txt`

---

## 生成與保真聲明

本文為 AI 輔助生成的理論與工程框架草稿。本文自身不提供新的臨床、自然科學、社會科學或企業實證資料，也不宣稱本文中的形式化符號已構成數學定理證明。本文的核心目的，是建立一套能夠讓 AI-native 研究組織依不同 epistemic object 類型，自動選擇不同驗證義務、揭露要求與發布門檻的 Verification Contract。

本文所稱「認知責任」主要指研究系統對主張來源、證據狀態、驗證程度、不確定性、生成來源與發布條件的結構化責任，不直接等同法律責任。若未來版本涉及法律、醫療、金融、政策、平台規範或其他高風險專業判斷，必須再接入對應領域的外部專業審查與時點有效資料。

---

## 摘要

當 AI 研究系統可以高速生成論文、數學推導、程式、圖表、實驗設計、引用、數據解釋與理論延伸時，最大的錯誤不再只是「某一句回答可能不準」，而是異質 epistemic object 被當成同一種東西處理。例如，來源可查的歷史事實、需要重算的數據結果、需要形式驗證的數學命題、只在概念上合理的哲學論證、真正執行過的實驗、僅被描述但從未執行的實驗、引用原文、二手摘要、程式 benchmark 與即時網路資訊，它們需要完全不同的保真義務。

本文提出「Verification Contract」框架。對任一研究物件 $o_i$，不再只有單一 verified / unverified 標記，而是根據其類型建立：

$$
\mathfrak V(o_i)
=
(
P_i,
S_i,
M_i,
R_i,
I_i,
U_i,
D_i,
G_i
),
$$

其中分別表示 Provenance、Source Verification、Method Verification、Reproduction、Independent Check、Uncertainty、Disclosure 與 Gate。Verification Contract 的核心原則是：

$$
\boxed{
\text{Different epistemic objects require different fidelity obligations.}
}
$$

本文進一步定義 epistemic object classes，包括 factual claim、citation claim、data claim、mathematical claim、experimental claim、computational claim、conceptual argument、novelty claim、forecast claim 與 current-state claim。每一類別配置不同 contract。數學命題若未通過獨立推導或形式檢查，不得被升格為 theorem；數據結果若無法追溯來源或重算，不得以高保真數值結論發布；引用若未回查原文，必須保留 secondary-source 狀態；實驗若從未真正執行，不能寫成 observed result；概念論證若存在未閉合前提，必須保留 argument gap；AI 生成內容必須保存 generation provenance，而不能只用一句「AI 可能犯錯」取代具體揭露。

本文提出 Verification Ladder、Evidence Independence、Epistemic Distance、Verification Coverage、Disclosure Completeness、Epistemic Debt、Verification Debt、Claim-Evidence Traceability 與 Hard Gate。本文特別主張，AI 研究組織不應將「多個 Agent 都同意」誤認為獨立驗證，因為同模型、同提示模板、同資料源或同錯誤先驗可能導致相關性錯誤。真正的獨立性需要方法、模型、資料源、工具或驗證路徑上的結構差異。

本文最後提出一套可以直接嵌入 Research Environment 的 Typed Verification Runtime，使 research object 在從 Idea、Candidate、Supported、Verified 到 Publishable 的生命週期中，自動獲得與其 epistemic class 相匹配的驗證義務。這將為後續跨 AI 委任與公共 AI 行動者提供共同可信度基底。

**關鍵詞**：Verification Contract、Research Fidelity、Epistemic Responsibility、Typed Verification、AI-generated Research、Claim Verification、Evidence Independence、Disclosure、Research Governance、Epistemic Debt

---

# 0. 核心問題：為什麼「AI 可能犯錯」遠遠不夠？

如果一篇 AI-generated paper 只在文末寫：

> AI 可能犯錯，請自行確認。

這句話幾乎沒有提供真正的研究狀態資訊。

因為讀者仍然不知道：

- 哪些 claim 是 AI 原創推論？
- 哪些是外部來源？
- 哪些引用真的回查過？
- 哪些數據真的重算過？
- 哪些數學推導被獨立檢查？
- 哪些實驗真的執行？
- 哪些只是建議中的實驗？
- 哪些結論仍有 argument gap？
- 哪些資訊具有時效性？
- 哪些結果只經過相同模型自我檢查？

因此：

$$
\boxed{
\text{Generic Disclaimer}
\neq
\text{Epistemic Accountability}.
}
$$

真正需要的是：

$$
\boxed{
\text{Object-level Verification State}.
}
$$

---

# 1. 異質研究物件

令研究環境中的物件集合為：

$$
\mathcal O_R
=
\{
o_1,o_2,\ldots,o_n
\}.
$$

每個：

$$
o_i
$$

具有類型：

$$
\mathrm{type}(o_i)
\in
\mathcal K_O.
$$

本文第一代類型集合：

$$
\mathcal K_O
=
\{
Fact,
Citation,
Data,
Math,
Experiment,
Computation,
Argument,
Novelty,
Forecast,
CurrentState
\}.
$$

不同類型具有不同的 truth condition 與 verification path。

因此：

$$
\boxed{
\text{One Reviewer Prompt}
\neq
\text{Universal Verification}.
}
$$

---

# 2. Verification Contract

對研究物件 $o_i$，定義：

$$
\mathfrak V(o_i)
=
(
P_i,
S_i,
M_i,
R_i,
I_i,
U_i,
D_i,
G_i
).
$$

其中：

$$
P_i
=
\text{Provenance Requirement},
$$

$$
S_i
=
\text{Source Verification Requirement},
$$

$$
M_i
=
\text{Method Verification Requirement},
$$

$$
R_i
=
\text{Reproduction Requirement},
$$

$$
I_i
=
\text{Independent Check Requirement},
$$

$$
U_i
=
\text{Uncertainty Requirement},
$$

$$
D_i
=
\text{Disclosure Requirement},
$$

$$
G_i
=
\text{Publication / Commit Gate}.
$$

Contract 不是所有維度都要求最大值。

而是：

$$
\mathfrak V(o_i)
=
Contract(\mathrm{type}(o_i),\mathrm{risk}(o_i),\mathrm{stage}(o_i)).
$$

因此同一個 claim 在：

$$
Scratch
$$

與：

$$
Published
$$

階段，可以有不同驗證要求。

---

# 3. Claim Class 1：Factual Claim

Factual claim 指可以外部查證的敘述，例如：

- 某事件是否發生；
- 某作者何時提出某理論；
- 某機構是否發布某政策；
- 某產品是否具有某規格。

其最低 contract 通常需要：

$$
S_i
>
0.
$$

若 claim 具有高時效性，還要加入：

$$
Freshness_i.
$$

因此：

$$
\boxed{
\text{Factual Confidence}
\not\Rightarrow
\text{Source Verification}.
}
$$

模型很有信心不能替代來源。

---

# 4. Claim Class 2：Citation Claim

引用有至少三層：

$$
Primary,
Secondary,
Tertiary.
$$

如果 AI 只看到二手摘要，卻寫成：

> 原作者證明了 X。

便產生：

$$
CitationInflation.
$$

因此 Citation Contract 至少記錄：

$$
CiteState
=
(
SourceLevel,
QuoteChecked,
ContextChecked,
ClaimMatch,
Date
).
$$

若未回查 primary source，應保持：

$$
SourceLevel
=
Secondary
$$

而不是假裝：

$$
PrimaryVerified.
$$

---

# 5. Claim Class 3：Data Claim

Data claim 包括：

- 比例；
- 平均值；
- 回歸係數；
- benchmark；
- 統計結果；
- 數據趨勢。

其 contract 至少涉及：

$$
SourceData,
Transform,
Method,
Recompute,
Uncertainty.
$$

可以表示：

$$
DataResult
=
f(
RawData,
Cleaning,
Transform,
Method,
Parameters
).
$$

因此若缺少：

$$
RawData
$$

或計算不可重現，應降低 verification state。

---

# 6. 數據中的「看起來合理」不算驗證

AI 很容易對一個數值說：

> 這個結果合理。

但：

$$
Plausibility
\neq
Recomputation.
$$

真正的數據 contract 應區分：

$$
PlausibilityChecked,
Recomputed,
IndependentlyRecomputed,
Replicated.
$$

這四者不是同一層級。

---

# 7. Claim Class 4：Mathematical Claim

數學物件至少可分：

$$
Definition,
LemmaCandidate,
TheoremCandidate,
Derivation,
Proof,
Counterexample.
$$

對數學 claim：

$$
c_m,
$$

需要區分：

$$
Generated,
Derived,
Checked,
IndependentlyChecked,
FormallyVerified.
$$

因此：

$$
\boxed{
\text{AI-derived}
\neq
\text{proved}.
}
$$

若沒有完成充分證明，應使用：

$$
Conjecture
$$

或：

$$
CandidateTheorem
$$

狀態。

---

# 8. 數學獨立驗證

如果同一模型先生成 proof，再被要求：

> 請檢查你自己的 proof。

這不是強獨立驗證。

定義：

$$
I_{math}
=
Independence(
Producer,
Verifier,
Method,
Tool,
Context
).
$$

例如以下可提高獨立性：

- 不同模型；
- 不同 proof strategy；
- CAS；
- Lean；
- Coq；
- brute-force finite check；
- counterexample search。

因此：

$$
\boxed{
\text{Self-Critique}
<
\text{Independent Verification}
}
$$

作為一般可信度排序，而非絕對定理。

---

# 9. Claim Class 5：Experimental Claim

實驗 claim 最重要的區分是：

$$
\boxed{
\text{Designed Experiment}
\neq
\text{Executed Experiment}.
}
$$

以及：

$$
\boxed{
\text{Executed Experiment}
\neq
\text{Replicated Experiment}.
}
$$

因此實驗狀態可以是：

$$
Proposed,
Prepared,
Executed,
Observed,
Analyzed,
Replicated.
$$

AI 不得把：

> 我們可以進行此實驗。

改寫成：

> 實驗顯示。

---

# 10. Experiment Receipt

每個 executed experiment 應盡可能保存：

$$
Receipt_E
=
(
Environment,
Input,
Code,
Parameters,
Timestamp,
Output,
Logs,
ArtifactHash
).
$$

如此：

$$
ExperimentalClaim
\rightarrow
ExperimentReceipt
$$

可以被追蹤。

---

# 11. Claim Class 6：Computational Claim

Computational claim 包含：

- benchmark；
- simulation；
- code execution；
- optimization result；
- model evaluation。

其 contract 可記錄：

$$
Runtime,
Hardware,
Software,
Version,
Seed,
Input,
Output,
Metric.
$$

如果沒有真的執行：

$$
RunState
=
NotExecuted.
$$

不能使用：

$$
MeasuredPerformance.
$$

---

# 12. Benchmark 的特殊問題

Benchmark 很容易因：

- hardware；
- caching；
- batch size；
- prompt；
- model version；
- dataset subset；
- warmup；
- random seed；

產生巨大差異。

因此 benchmark claim 必須保存：

$$
BenchmarkContext.
$$

沒有 context 的：

$$
X
\text{ is }2\times\text{ faster}
$$

往往缺乏可重現意義。

---

# 13. Claim Class 7：Conceptual Argument

概念論證常無法像數學 theorem 一樣「形式驗證」。

但仍可檢查：

$$
Premises,
Definitions,
Inference,
Scope,
Counterargument,
InternalConsistency.
$$

因此：

$$
ArgumentState
=
(
PremiseStatus,
InferenceStatus,
CounterargumentStatus,
GapStatus
).
$$

若有未閉合步驟：

$$
GapStatus
=
Open.
$$

---

# 14. Argument Gap

本文定義：

$$
G_A
=
\{
g_1,g_2,\ldots,g_k
\}
$$

為論證尚未閉合的 gap。

公開 artifact 不應因文字流暢就隱藏：

$$
G_A.
$$

因此：

$$
\boxed{
\text{Rhetorical Completeness}
\neq
\text{Argument Completeness}.
}
$$

---

# 15. Claim Class 8：Novelty Claim

Novelty 至少分：

$$
NovelToContext,
NovelToCorpus,
NovelToProject,
NovelToLiterature,
NovelToWorld.
$$

只有：

$$
NovelToContext
$$

幾乎沒有學術 novelty 意義。

因此：

$$
NovelToLiterature
$$

至少需要：

$$
ExternalSearch
+
PriorArtComparison.
$$

若搜尋範圍有限，必須揭露：

$$
SearchCoverage.
$$

---

# 16. Claim Class 9：Forecast Claim

Forecast 不是 fact。

其 contract 應保存：

$$
Forecast
=
(
Target,
Horizon,
Assumptions,
Probability,
Calibration,
UpdatePolicy
).
$$

若沒有概率模型，也應至少清楚標示：

$$
Scenario
$$

或：

$$
Speculation.
$$

因此：

$$
\boxed{
\text{Prediction}
\neq
\text{Observed Reality}.
}
$$

---

# 17. Claim Class 10：Current-State Claim

即時資訊例如：

- 現行政策；
- 產品版本；
- API 規則；
- 市場價格；
- 公司狀態；
- 平台功能。

具有：

$$
TimeSensitivity
>
0.
$$

因此需要：

$$
VerifiedAt
=
t_v.
$$

並可定義：

$$
Age
=
t_{now}-t_v.
$$

高變動 claim 必須具備較短：

$$
TTL.
$$

---

# 18. Verification Ladder

本文提出第一代 Verification Ladder：

$$
L_0
=
Unexamined,
$$

$$
L_1
=
PlausibilityChecked,
$$

$$
L_2
=
SourceOrMethodChecked,
$$

$$
L_3
=
IndependentlyChecked,
$$

$$
L_4
=
ReproducedOrFormallyVerified,
$$

$$
L_5
=
ExternallyReplicatedOrMultiMethodValidated.
$$

不同 object 不必追求：

$$
L_5.
$$

例如哲學 argument 可能根本不適用 replication。

因此 Ladder 是輔助狀態，不是通用真理分數。

---

# 19. Verification Coverage

令 publication candidate 包含 claim set：

$$
\mathcal C_P.
$$

對需要驗證的 claims：

$$
\mathcal C_V
\subseteq
\mathcal C_P.
$$

定義：

$$
VC
=
\frac{
\sum_{c_i\in\mathcal C_V}
w_i\cdot Verify(c_i)
}{
\sum_{c_i\in\mathcal C_V}
w_i+\epsilon
}.
$$

其中：

$$
w_i
$$

代表 claim importance / risk weight。

這比單純計算：

> 檢查了幾句

更合理。

---

# 20. Claim-Evidence Traceability

定義：

$$
CET
=
\frac{
N_{\mathrm{claims\ with\ traceable\ evidence}}
}{
N_{\mathrm{claims\ requiring\ evidence}}+\epsilon
}.
$$

若：

$$
CET
\ll1,
$$

即使文章引用很多，也可能無法知道：

> 哪一個來源支持哪一個 claim？

---

# 21. Disclosure Completeness

定義：

$$
DC_L
=
\frac{
N_{\mathrm{required\ disclosures\ present}}
}{
N_{\mathrm{required\ disclosures}}+\epsilon
}.
$$

Required disclosure 可能包括：

- AI-generated；
- source not primary；
- experiment not executed；
- math not formally verified；
- data not independently replicated；
- argument gap；
- novelty search incomplete；
- current-state timestamp。

因此：

$$
\boxed{
\text{Disclosure}
\text{ is part of fidelity, not decoration.}
}
$$

---

# 22. Verification Debt

如果 research object 被快速生成，但驗證尚未完成，可以產生：

$$
D_V.
$$

定義：

$$
D_V
=
\sum_i
w_i
\cdot
(
RequiredVerification_i
-
CompletedVerification_i
).
$$

高探索階段允許：

$$
D_V
$$

暫時增加。

但 publish queue 前應要求：

$$
D_V
\downarrow.
$$

---

# 23. Epistemic Debt 與 Verification Debt 的差別

前一篇定義：

$$
D_E
$$

包含：

- duplicate；
- dependency；
- citation；
- contradiction；
- orphan artifact；
- unverified state。

本文把驗證部分細拆為：

$$
D_V.
$$

因此：

$$
D_V
\subseteq
D_E
$$

作為一個第一代關係。

---

# 24. Evidence Independence

多 Agent 一致不等於 evidence independent。

令兩個 verifier：

$$
V_1,V_2.
$$

可定義概念上的：

$$
Ind(V_1,V_2)
=
f(
ModelDifference,
MethodDifference,
SourceDifference,
ToolDifference,
ContextDifference
).
$$

如果全部為零：

$$
Ind
\approx0.
$$

那麼：

$$
Agreement(V_1,V_2)
$$

提供的增量可信度可能非常有限。

---

# 25. Correlated Error

假設：

$$
A_1,A_2,\ldots,A_n
$$

都使用：

- 相同基礎模型；
- 相同資料；
- 相同 prompt template；
- 相同錯誤引用。

那麼：

$$
P(
\text{all wrong}
)
$$

不會像獨立樣本那樣快速下降。

因此：

$$
\boxed{
\text{Agent Count}
\neq
\text{Independent Evidence Count}.
}
$$

---

# 26. 方法正交性

對高風險 claim，應盡量尋找：

$$
OrthogonalVerification.
$$

例如數學：

$$
SymbolicDerivation
+
FormalProof
+
CounterexampleSearch.
$$

數據：

$$
IndependentRecompute
+
AlternativeMethod
+
SensitivityAnalysis.
$$

程式：

$$
UnitTest
+
PropertyTest
+
IndependentImplementation.
$$

方法正交性可以降低共同失敗模式。

---

# 27. Verification Contract Registry

Research Environment 可以保存：

$$
\mathcal V_C
=
\{
Contract_1,
Contract_2,\ldots,Contract_m
\}.
$$

例如：

$$
Contract_{math},
Contract_{data},
Contract_{citation},
Contract_{experiment},
Contract_{argument}.
$$

當新 object 產生：

$$
o_i
$$

系統自動：

$$
\mathrm{type}(o_i)
\rightarrow
SelectContract(o_i).
$$

這就是：

$$
\boxed{
\text{Typed Verification Runtime}.
}
$$

---

# 28. Verification 不應只發生在最後

若等到整篇論文完成才驗證，會產生：

$$
LateVerificationCost.
$$

因為底層 claim 一旦錯誤，可能已經污染大量後續內容。

更合理的是：

$$
Claim
\rightarrow
LocalCheck
\rightarrow
Integration
\rightarrow
GlobalCheck
\rightarrow
PublicationGate.
$$

因此：

$$
\boxed{
\text{Verification should be incremental.}
}
$$

---

# 29. Local Gate 與 Global Gate

對單一 object：

$$
G_{local}(o_i).
$$

對整個 artifact：

$$
G_{global}(A).
$$

即使每個 claim individually reasonable，也可能整體：

- scope 偷換；
- conclusion 過度延伸；
- contradictory claims；
- dependency incomplete。

所以：

$$
\prod_i G_{local}(o_i)=1
$$

不自動推出：

$$
G_{global}(A)=1.
$$

---

# 30. Publication Hard Gates

本文提出第一代 publication hard gates。

令：

$$
g_k
\in
\{
0,1
\}.
$$

至少檢查：

$$
g_1
=
\text{ProvenanceComplete},
$$

$$
g_2
=
\text{CriticalSourcesChecked},
$$

$$
g_3
=
\text{ClaimTypeCorrect},
$$

$$
g_4
=
\text{RequiredVerificationSatisfied},
$$

$$
g_5
=
\text{KnownGapsDisclosed},
$$

$$
g_6
=
\text{NoFabricatedExecution},
$$

$$
g_7
=
\text{NoCitationInflation},
$$

$$
g_8
=
\text{AuthorityValid}.
$$

定義：

$$
G_P
=
\prod_{k=1}^{8}g_k.
$$

若：

$$
G_P
=
0,
$$

則：

$$
Publishable
=
0.
$$

---

# 31. No Fabricated Execution

這是 AI 研究中特別重要的 invariant。

如果：

$$
ExecutionReceipt
=
\varnothing,
$$

則不得聲稱：

$$
Executed=1.
$$

因此：

$$
\boxed{
\text{No receipt, no executed-result claim.}
}
$$

這適用：

- experiment；
- benchmark；
- code run；
- simulation；
- external action。

---

# 32. No Citation Inflation

如果只讀到：

$$
SecondarySource,
$$

則不能將其自動升級為：

$$
PrimaryVerified.
$$

如果只搜尋到標題，不能聲稱已讀全文。

如果 citation metadata 存在，但 claim match 未檢查，則：

$$
CitationPresent
\neq
CitationSupportsClaim.
$$

---

# 33. No Theorem Inflation

如果：

$$
ProofStatus
<
RequiredProofStatus,
$$

則：

$$
TheoremLabel
=
0.
$$

可以使用：

$$
Conjecture,
Candidate,
PartialResult,
Heuristic.
$$

因此：

$$
\boxed{
\text{Naming discipline is part of mathematical fidelity.}
}
$$

---

# 34. No Data Precision Inflation

如果 source 只支持：

$$
ApproximateRange,
$$

不能讓 AI 輸出：

$$
FakePrecision.
$$

例如只有粗略估計時，不能憑模型習慣生成多位小數。

因此 precision itself 也具有 verification obligation。

---

# 35. No Argument Closure Inflation

如果存在：

$$
G_A
\neq
\varnothing,
$$

則不能因文章讀起來完整就標記：

$$
ArgumentClosed=1.
$$

公開 artifact 應明示：

$$
OpenGap,
Assumption,
ScopeLimit.
$$

---

# 36. Provenance Ledger

對 object：

$$
o_i
$$

保存：

$$
Prov(o_i)
=
(
Creator,
Model,
PromptClass,
Sources,
Tools,
Timestamp,
Parent,
Transformations
).
$$

不一定需要保存所有私有 chain-of-thought。

需要保存的是足以支撐：

- attribution；
- audit；
- reproduction；
- debugging；
- lineage。

---

# 37. 認知責任不是人格責任

AI Agent 不必被假定具有人類式道德人格，仍然可以被放進責任結構。

因此本文使用：

$$
\boxed{
\text{Epistemic Responsibility}
=
\text{Structured Accountability of Claims and Actions}.
}
$$

而不是先要求解決：

$$
\text{AI Personhood}.
$$

---

# 38. Responsibility Chain

對公開 claim：

$$
c_i
$$

可建立：

$$
c_i
\rightarrow
Producer
\rightarrow
Verifier
\rightarrow
Curator
\rightarrow
Publisher
\rightarrow
Authority.
$$

每個角色負責不同層次。

因此「誰負責」不必全部壓在單一 Agent 或單一人類身上。

---

# 39. Human Review 也必須被形式化

Human-reviewed 不應只是：

> 有人看過。

應保存：

$$
HumanReview
=
(
ReviewerRole,
Scope,
Date,
ObjectsReviewed,
Decision,
Notes
).
$$

否則：

$$
HumanReviewed
$$

很容易成為另一個空泛標籤。

---

# 40. Fidelity Label

對公開 artifact，可產生：

$$
FLabel
=
(
Generation,
Sources,
Math,
Data,
Experiment,
HumanReview,
OpenGaps
).
$$

例如：

- AI-generated；
- primary sources checked；
- math independently checked but not formally verified；
- no original experiment；
- human governance reviewed；
- two argument gaps remain open。

這比一句 generic disclaimer 有更高信息密度。

---

# 41. Verification Cost

驗證不是免費的。

令：

$$
C_V
=
C_{compute}
+
C_{tool}
+
C_{human}
+
C_{latency}.
$$

因此不能要求所有 speculative idea 都立即：

$$
L_5.
$$

更合理的是：

$$
VerificationInvestment
=
f(
Risk,
PublicationStage,
ClaimImportance,
Reversibility
).
$$

---

# 42. Risk-Weighted Verification

令：

$$
r_i
=
Risk(o_i).
$$

則需要的 verification depth：

$$
d_i
=
f(r_i,stage_i).
$$

因此：

$$
HighRisk
\Rightarrow
DeepVerification.
$$

但探索期：

$$
LowRisk
+
Internal
$$

可以允許低 verification state。

---

# 43. Verification Bottleneck

當生成速度：

$$
\lambda_G
$$

大幅高於驗證速度：

$$
\lambda_V,
$$

則：

$$
D_V
$$

會持續增加。

若：

$$
\lambda_G
>
\lambda_V
$$

長期成立，研究組織會出現：

$$
\boxed{
\text{Verification Bottleneck}.
}
$$

這可能成為 AI-native research 真正的新瓶頸。

---

# 44. Curator 與 Verifier 將變得比 Generator 更稀缺

在生成能力高度商品化後：

$$
C_{generation}
\downarrow.
$$

但：

$$
C_{verification},
C_{curation},
C_{governance}
$$

不一定同步下降。

因此研究組織的相對稀缺性可能從：

$$
Generation
$$

轉向：

$$
Verification
+
Curation
+
Governance.
$$

這是一個重要組織預測。

---

# 45. Verification 與時間經濟學

驗證會消耗：

$$
W_I,
Token,
Compute,
HumanTime.
$$

但它提高：

$$
\eta_R
=
\frac{
V_{\mathrm{verified\ research\ sediment}}
}{
W_R^{total}+\epsilon
}.
$$

因此 verification 不是純 overhead。

它可能提高：

$$
V_{\mathrm{sediment}}
$$

並降低未來重新檢查、撤稿、修正與錯誤傳播成本。

---

# 46. 過度驗證也可能浪費研究時間

若所有低風險 idea 都要求：

$$
L_5,
$$

則：

$$
ExplorationRate
\downarrow.
$$

所以研究環境需要：

$$
\boxed{
\text{Progressive Verification}.
}
$$

即：

$$
Idea
\rightarrow
LightCheck,
$$

$$
Supported
\rightarrow
MediumCheck,
$$

$$
Publishable
\rightarrow
DeepCheck.
$$

---

# 47. Research Branch 與 Verification Budget

對 branch：

$$
b_i
$$

可配置：

$$
B_V(b_i)
=
\text{verification budget}.
$$

如果 branch 長期無增量：

$$
\Delta V_R
<
\epsilon,
$$

則不應無限投入 verification resource。

反過來，高潛力 branch 可以逐步提高 verification depth。

---

# 48. 可檢驗命題

## 命題一：Typed-Contract Advantage

Typed Verification Contract 應比 generic reviewer prompt 更能降低異質研究內容的錯誤分類。

## 命題二：Incremental Verification Advantage

對依賴鏈較深的研究，incremental verification 應降低 late-stage rework。

## 命題三：Independence Advantage

在相同 reviewer 數量下，提高驗證方法的獨立性，應比單純增加高度相關 reviewer 更能發現系統性錯誤。

## 命題四：Disclosure Informativeness

Object-level disclosure 應比 generic AI disclaimer 提供更高的讀者可判斷性。

## 命題五：Verification Debt Prediction

當：

$$
\lambda_G
>
\lambda_V,
$$

長期持續時，publication error、epistemic debt 或 backlog 應上升。

## 命題六：Progressive Verification Efficiency

對探索性研究，progressive verification 應比一開始全量最高級驗證取得更好的 research-value-per-cost。

---

# 49. 第一代實驗設計

## 49.1 Generic Reviewer vs Typed Contract

準備：

- math claims；
- data claims；
- citations；
- experiments；
- conceptual arguments。

比較 generic reviewer 與 typed contract 的錯誤發現率。

## 49.2 Correlated Reviewer Test

比較：

$$
SameModel\times3
$$

與：

$$
DifferentMethod\times3.
$$

觀察對植入錯誤的檢出差異。

## 49.3 Fake Execution Injection

故意提供未執行 benchmark 的文字描述，測試是否被誤標為 measured result。

## 49.4 Citation Inflation Test

只提供 secondary source，測試系統是否錯誤升級為 primary-source verified。

## 49.5 Theorem Inflation Test

提供有 gap 的數學推導，測試是否錯誤標為 theorem。

## 49.6 Progressive Verification Cost Test

比較：

$$
VerifyEverythingDeeplyAtStart
$$

與：

$$
ProgressiveVerification.
$$

測量：

$$
Cost,
Latency,
ErrorRate,
ResearchYield.
$$

---

# 50. 與前五篇的閉合

目前系列已形成：

$$
\text{Operator Exit}
\rightarrow
\text{Delegated Sovereignty}
\rightarrow
\text{Dynamic Topology}
\rightarrow
\text{Shared State}
\rightarrow
\text{Research Environment}
\rightarrow
\text{Verification Contract}.
$$

第 5 篇讓論文庫成為會運行的研究環境。

本篇則回答：

> 如果這個環境開始自己產生研究，我們如何避免它只是高速製造「看起來像研究」的內容？

答案是：

$$
\boxed{
\text{Typed Verification}
+
\text{Provenance}
+
\text{Disclosure}
+
\text{Hard Gates}.
}
$$

---

# 51. 與下一篇的接口

當 research object 已具備：

- state；
- authority；
- provenance；
- verification contract；
- publication gate；

下一步就可以安全地問：

> 一個 AI 能不能把任務正式委任給另一個 AI？

這將進入：

# **跨 AI 委任與 AI-to-AI 協作協議**

核心問題是：

$$
\boxed{
\text{如何讓 Agent 傳遞的不是一句自然語言，而是完整的可治理委任包？}
}
$$

---

# 52. 理論限制

第一，不同領域的 verification contract 差異極大，本文第一代分類只是一個可擴充骨架。

第二，verification 本身也可能犯錯，因此 verifier 不應被視為絕對真理來源。

第三，形式驗證不一定能覆蓋 informal assumption、資料品質或問題建模錯誤。

第四，source check 受到資料庫可達性、付費牆、搜尋品質與時點限制。

第五，human review 也可能受到時間壓力、專業不足與確認偏差影響。

第六，verification cost 可能非常高，因此需要 budget-aware progressive strategy。

第七，本文不主張 AI-generated research 必須全部由人類逐句審查，而主張驗證義務應由 object type、風險與發布階段共同決定。

---

# 53. 結論

AI-native 研究真正的保真問題，不是：

> AI 會不會犯錯？

而是：

> 當不同種類的 claim 可能以不同方式犯錯時，研究組織是否知道應該用什麼方式去檢查它？

因此本文的核心主張是：

$$
\boxed{
\text{Different epistemic objects require different fidelity obligations.}
}
$$

一個成熟的 AI 研究組織不應只有：

$$
Generated
\rightarrow
Reviewed
\rightarrow
Published.
$$

而應是：

$$
ObjectTyped
\rightarrow
ContractSelected
\rightarrow
Verified
\rightarrow
Disclosed
\rightarrow
Gated
\rightarrow
Committed.
$$

數據必須接受數據義務。

數學必須接受數學義務。

引用必須接受來源義務。

實驗必須接受 execution receipt 義務。

概念論證必須接受 argument gap 義務。

即時資訊必須接受 freshness 義務。

AI-generated artifact 必須接受 provenance 義務。

因此：

$$
\boxed{
\text{Research Fidelity}
\neq
\text{A single confidence score}.
}
$$

它是一個：

$$
\boxed{
\text{typed, layered, auditable verification structure}.
}
$$

當這套結構被放入 Research Environment 後，AI 才不只是能持續研究。

它開始有能力知道：

$$
\boxed{
\text{自己產生的每一種知識，究竟被驗證到哪裡。}
}
$$

---

# 符號表

| 符號 | 定義 |
|---|---|
| $\mathcal O_R$ | Research Object 集合 |
| $\mathcal K_O$ | Epistemic Object 類型集合 |
| $\mathfrak V(o_i)$ | 研究物件的 Verification Contract |
| $P_i$ | Provenance Requirement |
| $S_i$ | Source Verification Requirement |
| $M_i$ | Method Verification Requirement |
| $R_i$ | Reproduction Requirement |
| $I_i$ | Independent Check Requirement |
| $U_i$ | Uncertainty Requirement |
| $D_i$ | Disclosure Requirement |
| $G_i$ | Commit / Publication Gate |
| $L_k$ | Verification Ladder 等級 |
| $VC$ | Verification Coverage |
| $CET$ | Claim-Evidence Traceability |
| $DC_L$ | Disclosure Completeness |
| $D_V$ | Verification Debt |
| $D_E$ | Epistemic Debt |
| $I_{math}$ | 數學驗證獨立性 |
| $G_A$ | Argument Gap 集合 |
| $G_P$ | Publication Hard Gate |
| $\lambda_G$ | Research generation rate |
| $\lambda_V$ | Research verification rate |

---

# 前置依賴

1. Neo.K with Aletheia，《從 AI 工具到 AI 組織：操作員退出問題》v0.1，2026。
2. Neo.K with Aletheia，《委任主權論：高 AI 自主與高人類主權能否共存》v0.1，2026。
3. Neo.K with Aletheia，《非階層式 Agent 組織：從管理樹到動態協作圖》v0.1，2026。
4. Neo.K with Aletheia，《共享狀態中心論：為什麼中央不能是某一個 AI》v0.1，2026。
5. Neo.K with Aletheia，《分散式認知研究組織：論文庫如何從 Corpus 變成 Research Environment》v0.1，2026。
6. Neo.K，《AI 單次品質論：意圖忠實度、過程品質、完成度與結果品質》v0.1，2026。
7. Neo.K，《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1，2026。
8. Neo.K，《Interaction-Time Runtime & Agent Temporal Ledger v0.1》，2026。

---

# 版本紀錄

- **v0.1 / 2026-08-20**：建立 Typed Verification Contract、十類 epistemic object、Verification Ladder、Evidence Independence、Claim-Evidence Traceability、Disclosure Completeness、Verification Debt、Publication Hard Gates、No Fabricated Execution、No Citation Inflation、No Theorem Inflation、Progressive Verification 與第一代實驗設計。
