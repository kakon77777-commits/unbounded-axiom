---
title: "超越政治懶人包：勤人 AI 與保存優先的長時序政治分析"
english_title: "Beyond the Political Cheat Sheet: Diligent AI and Preservation-First Longitudinal Political Analysis"
series: "AI-Native Longitudinal Actor Intelligence"
author: "Neo.K"
institution: "EveMissLab／一言諾科技有限公司"
paper: "04"
version: "v0.1"
date: "2026-08-28"
language: "zh-TW"
status: "Working Paper / Canonical UTF-8 Source"
method_status: "Conceptual and methodological framework; not a claim of universal corpus completeness."
---

# 超越政治懶人包：勤人 AI 與保存優先的長時序政治分析

**Beyond the Political Cheat Sheet: Diligent AI and Preservation-First Longitudinal Political Analysis**

**AI-Native Longitudinal Actor Intelligence Series — Paper 04**

## 摘要

傳統政治資訊產品多以壓縮為中心：從大量新聞、演說、政策文件與歷史事件中挑選少數「重要內容」，再轉化為摘要、時間線、懶人包或人物標籤。這種方法降低閱讀成本，卻同時產生不可逆資訊損失：未被選入摘要的反例、角色變化、語境、政策結果、責任鏈與時間關係往往永久消失。大型語言模型與代理式檢索系統的成熟，使另一種方法開始具有技術與經濟可行性。本文將其稱為「勤人 AI」（Diligent AI）：AI 的主要任務不是替人少讀，而是替人執行原本因人力成本過高而無法持續完成的高覆蓋、長時序、跨來源、可追溯分析。

勤人 AI 採用「保存優先、投影後置」（preservation-first, projection-later）原則。系統先在明確宣告的 corpus scope 中保存來源、時間、角色、事件、言論、行動、結果、責任與反證，再依使用者問題生成局部 projection。本文特別拒絕「AI 看完所有政治資料」這種不可驗證敘事，而以 coverage accounting 取代。任何分析必須說明資料範圍、來源類型、已涵蓋比例、缺口、不確定性與時間截點。

本文提出 Diligent Political Analysis Stack，包括 canonical evidence corpus、claim ledger、event ledger、actor-role graph、temporal relation layer、hypothesis layer、counterevidence search、verification layer 與 query projection。本文亦提出 Coverage Ratio、Traceability Ratio、Temporal Fidelity、Counterevidence Completion、Hypothesis Separation、Correction Closure Coverage 與 Diligence Score 等方法指標，用來區分「大量文字輸出」與真正的高勤勉分析。

2026 年政治 NLP 已顯示若干關鍵技術零件正在成熟：研究者已能利用推理型 LLM 將 2006–2023 年歐洲議會演說聚合為長時序敘事訊號；也已有研究把選舉新聞流轉成具 actor–action–target 結構的政治敘事情報 brief。另一方面，大規模政治 fact-checking 實驗顯示，單靠更強推理或一般 web search 仍不可靠，而 curated context 能顯著改善結果；fine-grained fact verification 與 evidence-contract 方法則指出，原子化 claim 與細粒度 provenance 是可信分析的必要條件。這些成果共同支持本文的核心主張：下一代政治 AI 的關鍵不只是更強的生成能力，而是持續建構、保存與驗證長時序證據結構。

本文最後指出，勤人 AI 並不只屬於公共新聞場域。相同方法可以服務政治學研究、企業風險、政策預測、產業監管分析與機構決策。其核心價值不在於替人「快速得到答案」，而在於把原本因認知與人力限制而無法持續維護的政治記憶，轉化為可查詢、可反證、可重播的證據基礎設施。

**關鍵詞：** 勤人 AI、長時序政治分析、政治記憶、證據帳本、事件資料、fact-checking、provenance、coverage accounting、反證、政治 NLP

---

## Abstract

Conventional political information products are compression-first. Large bodies of speeches, news, policy documents, legislative records, and historical events are reduced into short summaries, timelines, cheat sheets, and labels. This lowers reading costs but creates irreversible information loss: omitted counterexamples, role changes, context, policy outcomes, responsibility chains, and temporal relations often disappear from subsequent analysis.

This paper introduces Diligent AI, a preservation-first approach to longitudinal political analysis. The purpose of Diligent AI is not primarily to help humans read less, but to perform high-coverage, cross-source, temporally structured, provenance-preserving analytical work that was previously too costly to sustain manually. The framework follows a preservation-first, projection-later principle: evidence is collected and normalized within a declared corpus scope before question-specific projections are generated.

The paper rejects unverifiable claims that an AI has “read everything.” Instead, it introduces coverage accounting and requires every analysis to report corpus boundaries, source classes, missingness, temporal cutoffs, uncertainty, and counterevidence search status. A Diligent Political Analysis Stack is proposed, consisting of a canonical evidence corpus, claim ledger, event ledger, actor-role graph, temporal relation layer, hypothesis layer, counterevidence search, verification layer, and query projection layer. Metrics including Coverage Ratio, Traceability Ratio, Temporal Fidelity, Counterevidence Completion, Hypothesis Separation, Correction Closure Coverage, and a composite Diligence Score are proposed.

Recent political NLP research demonstrates that several technical components are now feasible: LLMs can aggregate two decades of parliamentary narratives into temporal signals, transform election news streams into structured narrative intelligence, and assist qualitative political analysis. Yet large-scale evaluations of political fact-checking also show that reasoning and generic web search alone remain insufficient; curated context, fine-grained claim decomposition, and strong provenance constraints substantially improve reliability. Diligent AI therefore treats evidence infrastructure, not generation fluency, as the core of political intelligence.

---

# 1. 從「懶人包」開始，但不要停在懶人包

政治資訊長期存在一個現實問題：

$$
Information\ Volume \gg Human\ Attention
$$

因此媒體、研究者、競選團隊與一般公民都需要壓縮。

傳統流程大致是：

$$
Documents
\rightarrow
Selection
\rightarrow
Compression
\rightarrow
Summary
$$

若有一萬筆政治事件，最後可能只保留：

$$
10,000
\rightarrow
100
\rightarrow
20
\rightarrow
5
$$

這種方法非常有用。

問題是，它通常包含不可逆操作：

$$
Compression(C)
\rightarrow
Loss(C)
$$

一旦某筆資料在第一輪被判定「不重要」，後面的讀者甚至不知道它曾經存在。

懶人包真正節省的不是閱讀時間而已，而是：

$$
Attention
+
Search
+
Classification
+
Memory
$$

但它同時把「誰決定重要」藏進摘要裡。

---

# 2. 勤人 AI：懶人包的相反物

本文將 Diligent AI 定義為：

> 在明確宣告且可稽核的資料範圍內，利用 AI 持續進行高覆蓋檢索、結構化、時序對齊、關係建立、反證搜尋與證據驗證，再依具體問題生成局部分析 projection 的系統。

其核心不是：

$$
Read\ Less
$$

而是：

$$
Machine\ Does\ More\ Reading/Structuring
$$

因此：

$$
Human\ Attention
$$

從第一線逐筆閱讀，轉為：

$$
Question
+
Audit
+
Judgment
$$

勤人 AI 的基本資訊哲學是：

$$
Preserve\ First
\rightarrow
Project\ Later
$$

而不是：

$$
Summarize\ First
\rightarrow
Reason\ From\ Summary
$$

---

# 3. 「全部看完」必須改寫成可驗證的 Coverage

「AI 看完某政治人物所有資料」在科學上幾乎沒有意義。

因為：

- 「所有資料」邊界不清；
- 私人資料不可得；
- 部分影音已刪除；
- 地方報紙未數位化；
- 社群平台 API 不完整；
- 新資料持續產生。

因此本文不允許：

$$
Universal\ Completeness
$$

而要求：

$$
Declared\ Corpus\ Scope
$$

令分析範圍：

$$
\Omega=
(
Actor,
TimeRange,
SourceClasses,
Languages,
Jurisdictions,
MediaTypes
)
$$

例如：

$$
\Omega_A=
(
A,
2010\text{-}01\text{-}01:2026\text{-}08\text{-}28,
OfficialRecords+MajorMedia+PublicSocial,
zh\text{-}TW,
Taiwan,
Text+VideoTranscript
)
$$

只有在 $\Omega$ 被宣告後，「高覆蓋」才具有可檢驗意義。

---

# 4. Coverage Accounting

令理論上應取得的來源集合為：

$$
S_{\Omega}
$$

實際成功取得的來源為：

$$
S_{obs}
$$

定義 Coverage Ratio：

$$
CR=
\frac{|S_{obs}|}{|S_{\Omega}|}
$$

但很多來源總量未知。

因此更實際的方法是依來源類別拆分：

$$
CR_k=
\frac{|S_{obs,k}|}{|S_{expected,k}|}
$$

其中 $k$ 可以是：

- 國會逐字稿；
- 政府新聞稿；
- 記者會；
- 政策文件；
- 社群公開貼文；
- 主要媒體；
- 地方媒體；
- 選舉公報；
- 預算；
- 法案；
- 判決；
- 組織文件。

系統最後不應說：

> 已完整分析。

而應說：

> 本次分析涵蓋 2018–2026 年公開國會紀錄 98%、官方新聞稿 94%、主要媒體可檢索報導 81%；地方影音與已刪除社群資料存在顯著缺口。

這才是勤人 AI 的語言。

---

# 5. Preservation-First

勤人 AI 不以摘要作為 canonical source。

canonical layer 應保存：

$$
E_i=
(
SourceID,
Timestamp,
Actor,
Role,
Context,
Content,
Action,
Target,
Outcome,
Provenance
)
$$

上層所有 summary、人物模型、評分與預測都只是 projection。

因此：

$$
Canonical\ Evidence
\neq
Rendered\ Analysis
$$

這個設計有三個理由。

第一，未來問題會改變。

今天問：

> 他是否支持核能？

明天可能問：

> 他在經濟衰退時是否比景氣良好時更支持核能？

如果只保存第一個摘要，第二個問題無法重新計算。

第二，模型會進步。

新的 extraction model 可以重新跑舊 corpus。

第三，政治判斷需要反證。

若 canonical evidence 被摘要吃掉，後續就無法知道模型忽略了什麼。

---

# 6. Diligent Political Analysis Stack

本文提出九層結構。

## Layer 0：Raw Source Registry

保存來源存在性與基本 metadata：

$$
URL/ID
+
Publisher
+
Timestamp
+
MediaType
+
AccessState
+
Checksum
$$

## Layer 1：Canonical Evidence Corpus

保存可驗證的原始文本、逐字稿、文件與來源片段。

## Layer 2：Atomic Claim Ledger

將複雜政治說法拆成可驗證原子 claim：

$$
C_i=
(
Actor,
Proposition,
Time,
Scope,
Modality,
Target
)
$$

## Layer 3：Event Ledger

保存：

$$
Actor
+
Action
+
Target
+
Context
+
Outcome
$$

Paper 01 的 LPAM 在此發揮核心作用。

## Layer 4：Actor-Role Graph

同一人物會跨角色：

$$
Academic
\rightarrow
Advocate
\rightarrow
Legislator
\rightarrow
Executive
$$

不同角色下權限不同，因此不能只以 person node 分析。

## Layer 5：Temporal Relation Layer

建立：

$$
Before
$$

$$
After
$$

$$
During
$$

$$
Causes/Precedes
$$

$$
Corrects
$$

$$
Contradicts
$$

$$
Updates
$$

等時序關係。

## Layer 6：Hypothesis Layer

所有人物模型均標記為：

$$
HYP
$$

並連接支持證據與反證。

## Layer 7：Verification and Counterevidence

驗證：

- 引文；
- 時間；
- 實體；
- 來源；
- 語境；
- 相反案例；
- 後續修正。

## Layer 8：Query Projection

只有最後才生成：

- 人物分析；
- 時間線；
- 政策比較；
- 風險報告；
- 學術統計；
- 公眾版摘要。

---

# 7. Atomic Claim：不要整段一起判

政治 statement 常同時包含多個命題。

例如：

> 「我們上任後失業率下降，證明產業政策成功，而且反對黨當初的批評完全錯誤。」

至少包含：

$$
C_1:\ Unemployment\ declined
$$

$$
C_2:\ Decline\ occurred\ after\ administration\ took\ office
$$

$$
C_3:\ Industrial\ policy\ caused\ decline
$$

$$
C_4:\ Opposition\ criticism\ was\ false
$$

若整句只標記：

$$
True/False
$$

會失去大量資訊。

2025 年 FactLens 已明確主張 fine-grained verification，將複雜 claim 拆成 subclaims 可以提高證據檢索透明度，雖然拆解本身也可能造成語境流失。

因此勤人 AI 必須保存：

$$
ParentClaim
\leftrightarrow
SubClaims
$$

而不是丟掉原句。

---

# 8. 政治 Event 才是長時序分析的重要單位

傳統 fact-check 偏向：

$$
Claim
\rightarrow
TruthValue
$$

但政治治理更需要：

$$
Actor
\rightarrow
Action
\rightarrow
Institution
\rightarrow
Outcome
$$

政治事件資料研究長期將政治互動編碼成 actor-action 結構，以便進行聚合分析。

2026 年 Wilson、Martin-Morales 與 Nelson 更進一步使用 LLM 將 1990–2024 Freedom House 報告轉成近 20 萬筆、帶文本證據的民主化／民主倒退事件。

這證明：

$$
Long\ Text
\rightarrow
Structured\ Political\ Events
$$

已從昂貴人工流程逐步變成可擴張計算流程。

勤人 AI 需要把：

$$
Claim\ Ledger
$$

與：

$$
Event\ Ledger
$$

同時保存。

---

# 9. 時間不是 metadata，而是核心結構

政治人物分析最常見錯誤之一是把：

$$
Statement_{2012}
$$

與：

$$
Statement_{2026}
$$

直接比較，卻忽略中間：

- 職位不同；
- 法律不同；
- 國際環境不同；
- 新證據出現；
- 政策已執行；
- 人物可能合理改變立場。

所以：

$$
Contradiction
\neq
Textual\ Difference
$$

真正需要的是：

$$
Temporal\ Context
+
Role\ Context
+
Evidence\ State
$$

PoliticalNLP 2026 已有研究利用推理型 LLM 對 2006–2023 歐洲議會演說進行二元敘事分類，再聚合成月度時間訊號。

這證明 LLM 不只可以分析單篇政治文本，也開始能參與：

$$
Diachronic\ Political\ Analysis
$$

。

---

# 10. 從新聞流到 Narrative Intelligence

2026 年 PoliticalNLP 的另一項研究已將匈牙利選前 21 個新聞來源、574 篇選舉相關文章轉成結構化 narrative intelligence brief。

其流程包括：

$$
Article
\rightarrow
Narrative\ Event\ Frame
\rightarrow
Embedding\ Cluster
\rightarrow
Structured\ Brief
$$

事件 frame 特別包含：

$$
Actor
\rightarrow
Action
\rightarrow
Target
$$

與 causal claims。

這已經接近勤人 AI 的局部實作。

但 Diligent AI 要再往前：

1. 不以 brief 為終點；
2. brief 不取代 canonical evidence；
3. 不只分析 narrative；
4. 要跨年、跨角色追蹤 actor；
5. 要保留 outcome 與 correction；
6. 要主動找反證。

---

# 11. 為什麼「更強的 LLM + Web Search」仍然不夠？

一個常見想像是：

> 模型夠強，再讓它上網查，就能完成政治事實分析。

2026 年 DeVerna 等人以超過 6,000 筆 PolitiFact claims 測試 15 種近期 LLM，結果顯示一般模型表現有限，reasoning 帶來的改善不大，web search 也只有中度提升；反而使用經整理的 PolitiFact context 的 curated RAG，大幅提升整體 macro F1。

對勤人 AI 而言，這個結果非常重要。

它意味著：

$$
Model\ Intelligence
\neq
Evidence\ Infrastructure
$$

而：

$$
Generic\ Web\ Search
\neq
Curated\ Political\ Memory
$$

即使未來模型更強，若輸入：

- 不完整；
- 混雜；
- 時間錯置；
- 缺乏 provenance；
- 缺少反證；

仍然可能得到高流暢、低可信的答案。

---

# 12. Evidence Contract

下一代系統不能只要求：

> 請附來源。

而應要求 evidence contract。

對每一個衍生 claim：

$$
D_i
$$

至少綁定：

$$
D_i
\rightarrow
\{
EvidenceUnit_1,
EvidenceUnit_2,\ldots
\}
$$

並記錄：

- 支持或反駁；
- 原始來源；
- 精確片段；
- timestamp；
- source ID；
- extraction method；
- confidence；
- 是否有人類驗證。

2026 年 GAVEL 類方法已開始以 Evidence Contract 要求原子 subclaim 綁定明確 evidence units，並用 mechanized scrutiny 檢查 evidence identifier 與引用內容。

Diligent AI 將這種概念從 fact-checking 擴張到：

$$
Actor\ Model
$$

$$
Responsibility\ Model
$$

$$
Longitudinal\ Hypothesis
$$

。

---

# 13. 反證不是附錄，而是第一級資料

一般政治分析常先形成故事：

$$
Narrative
\rightarrow
Supporting\ Examples
$$

勤人 AI 則要求：

$$
Hypothesis
\rightarrow
Support\ Search
+
Counterevidence\ Search
$$

例如假說：

$$
H:
Actor\ tends\ to\ externalize\ responsibility
$$

系統不只找「甩鍋案例」，還必須找：

$$
E^{-}=
\{
Direct\ Acceptance,
Self\ Critique,
Correction,
Costly\ Ownership
\}
$$

若只搜尋支持案例：

$$
Diligence=0
$$

即使找到一百個看似支持的新聞標題，也不能叫勤人分析。

---

# 14. Counterevidence Completion

令一個假說預先定義的反證類型集合為：

$$
K_H=
\{
k_1,k_2,\ldots,k_m
\}
$$

其中已完成搜索與驗證的類型為：

$$
K_{obs}
$$

定義：

$$
CEC_H=
\frac{|K_{obs}|}{|K_H|}
$$

這不是說找到多少反例，而是：

> 應該找的反例類型，是否真的被系統搜尋過？

例如研究「政策反覆」時至少要搜尋：

- 公開承認改變立場；
- 新證據造成合理更新；
- 法律環境改變；
- 角色改變；
- 原始引文被截斷；
- 一致立場的反例。

---

# 15. Hypothesis Separation

Paper 01 已區分：

$$
OBS
\neq
DER
\neq
HYP
\neq
PRED
$$

勤人 AI 必須把這個型別系統變成 runtime rule。

例如：

**OBS**

> 2018 年某人在公開演說中支持政策 A。

**OBS**

> 2024 年某人在部長角色下支持政策 B。

**DER**

> A 與 B 在某一政策維度存在差異。

**HYP**

> 該人物可能發生政策立場更新。

**PRED**

> 若外部條件 X 再次出現，其可能支持 B。

如果系統直接：

$$
OBS
\rightarrow
"FlipFlopper"
$$

就是 inference collapse。

本文定義 Hypothesis Separation Ratio：

$$
HSR=
\frac{
Outputs\ with\ explicit\ epistemic\ type
}{
All\ analytical\ outputs
}
$$

理想值應接近：

$$
1
$$

。

---

# 16. Provenance Traceability

令輸出中的可驗證衍生命題集合為：

$$
D
$$

具有直接 evidence trace 的命題為：

$$
D_t
$$

則：

$$
TR=
\frac{|D_t|}{|D|}
$$

即 Traceability Ratio。

注意：

$$
Citation\ Count
\neq
Traceability
$$

一篇報告引用五十篇新聞，不代表每個重要推論都能追溯。

真正的 traceability 是：

$$
Claim
\rightarrow
Evidence
\rightarrow
Source
$$

可被機器與人重新走一遍。

---

# 17. Temporal Fidelity

政治資料非常容易發生 temporal leakage。

例如：

2020 年的 prediction 是否合理，不能使用 2022 年才知道的資訊來判斷。

因此對每個分析時點 $t$：

$$
Evidence(D_t)
\subseteq
AvailableInformation_{\leq t}
$$

若系統在回顧分析時把後來發生的結果偷偷放回早期決策模型，就產生：

$$
Hindsight\ Leakage
$$

因此本文提出 Temporal Fidelity：

$$
TF=
1-
\frac{
TemporalLeakageCases
}{
EvaluatedTemporalClaims
}
$$

對需要 reconstruct past belief state 的研究尤其重要。

---

# 18. Correction Closure Coverage

Paper 03 定義了 Correction Closure Index。

勤人 AI 還必須知道：

> 有多少已知失敗事件真的被追蹤到新聞週期以後？

令需要後續追蹤的事件集合為：

$$
E_c
$$

實際完成 correction-thread 查詢者為：

$$
E_{ct}
$$

則：

$$
CCC=
\frac{|E_{ct}|}{|E_c|}
$$

如果：

$$
CCC\ll1
$$

系統可能只是在分析危機當天說了什麼，而不是分析治理。

---

# 19. Diligence Score

本文提出一個示意性的 Diligence Score，不建議在沒有基準研究前把它當作絕對分數。

令：

$$
DS=
(
CR\cdot TR\cdot TF\cdot CEC\cdot HSR\cdot CCC
)^{1/6}
$$

這是一個幾何平均。

使用幾何平均是因為：

$$
Any\ Critical\ Dimension\rightarrow0
$$

都應顯著降低整體勤勉程度。

例如一個系統 coverage 很高，但：

$$
TR=0
$$

沒有 provenance，

則不能因為「看了很多」就被認定為高品質。

同理，引用很多資料但從不搜尋反證，也不是勤人 AI。

---

# 20. 「勤」不等於「算力浪費」

勤人 AI 並不是要求每次 query 都重新讀完整 corpus。

真正架構應該是：

$$
Expensive\ Canonicalization\ Once
$$

加上：

$$
Incremental\ Maintenance
$$

再加：

$$
Query\text{-}Specific\ Retrieval
$$

因此：

$$
TotalCost
=
Ingest
+
IncrementalUpdate
+
Projection
$$

而不是：

$$
TotalCost
=
FullCorpusRead\times EveryQuery
$$

這也是勤人 AI 可以進入企業與學術實務的原因。

---

# 21. Longitudinal Political Memory

勤人 AI 最核心的資產不是模型，而是：

$$
Political\ Memory
$$

這個 memory 不是向量資料庫裡的一堆 chunk。

而是：

$$
Source
+
Event
+
Claim
+
Role
+
Time
+
Outcome
+
Attribution
+
Correction
$$

組成的可重播狀態。

一個成熟系統應可以回答：

> 只用 2022 年 6 月以前的資料，重建當時某政治人物對政策 X 的可觀察模型。

也可以回答：

> 加入 2024–2026 的資料後，模型在哪些地方發生更新？

因此：

$$
Model_{t_1}
\rightarrow
Model_{t_2}
$$

本身就是研究對象。

---

# 22. 從人物懶人包到 Actor Query Engine

傳統人物頁面是：

- 學歷；
- 經歷；
- 爭議；
- 立場；
- 政績。

勤人 AI 應改為 queryable actor model。

例如使用者可以問：

> 這個人在擁有行政權與只有立法權時，責任語言是否不同？

> 他對自己人和對手是否使用相同政策證據標準？

> 他的選舉承諾中，哪些後來進入預算？

> 哪些政策立場變化可以由新證據合理解釋？

> 哪些重大失敗後有真正完成修正？

這些問題都不是一頁 static profile 可以回答。

---

# 23. 從 Fact Check 到 Pattern Check

傳統 fact-check：

$$
Claim
\rightarrow
True/False/Mixed
$$

勤人 AI 加入：

$$
Consistency\ Check
$$

$$
Attribution\ Check
$$

$$
Action\ Check
$$

$$
Outcome\ Check
$$

$$
Correction\ Check
$$

$$
Temporal\ Check
$$

因此真正分析單位從：

$$
Statement
$$

提升到：

$$
Behavioral\ Trajectory
$$

。

這不是取消 fact-check，而是把 fact-check 變成底層 primitive。

---

# 24. 對媒體的意義：深度內容的成本結構改變

傳統深度新聞昂貴，因為：

$$
ArchiveSearch
+
Transcription
+
CrossChecking
+
TimelineBuilding
+
ExpertReading
$$

需要大量人力。

AI 將部分成本降為：

$$
Compute
+
Editorial\ Audit
$$

因此未來可能出現：

$$
AI\text{-}Native\ Political\ Observatory
$$

它不是只追逐每天新聞，而是持續維護：

$$
Actor\ Ledger
+
Policy\ Ledger
+
Institution\ Graph
$$

當新事件出現時：

$$
NewEvent
\rightarrow
Historical\ Context
$$

可以近即時產生。

這使「深度」第一次有可能從偶發專題變成持續型產品。

---

# 25. 對學術研究的意義

政治學長期受限於 coding cost。

很多研究只能：

$$
n=20
$$

$$
n=100
$$

或以特定時段抽樣。

LLM-assisted extraction 使：

$$
n\rightarrow10^4,10^5,10^6
$$

逐步成為可能。

但本文強調：

$$
Scale
\neq
Validity
$$

PoliticalNLP 2026 的 qualitative narrative study 已顯示，LLM 與人類學者在部分語意輸出上可以相當接近，但仍存在 factual errors、過度結構化抽象與忽略低顯著敘事等問題。

因此勤人 AI 在學術上最合理的位置是：

$$
Human\text{-}AI\ Research\ Infrastructure
$$

而不是：

$$
Autonomous\ Political\ Truth\ Machine
$$

。

---

# 26. 對企業與經濟情報的意義

政治分析並不只服務選民。

企業真正需要的往往是：

$$
Policy\ LeadTime
$$

而不是政策公布後的新聞摘要。

例如系統可以長期追蹤：

$$
Actor
\rightarrow
PolicyPreference
\rightarrow
Committee
\rightarrow
Budget
\rightarrow
Regulation
\rightarrow
Industry
$$

並偵測：

$$
P(Policy_X\mid Evidence_{1:t})
$$

是否持續變化。

這使勤人 AI 自然連接 Paper 06 的：

$$
Political\ Actor\ Intelligence
\rightarrow
Economic\ Infrastructure
$$

。

---

# 27. 對民主政治的意義：降低政治遺忘成本

政治人物長期享有一個結構性條件：

$$
Human\ Memory\ Limited
$$

以及：

$$
Archive\ Search\ Cost\ High
$$

因此：

$$
Old\ Statement
$$

很容易退出公共記憶。

勤人 AI 改變的不是「AI 永遠不忘」。

真正改變的是：

$$
Retrieval\ Cost\downarrow
$$

$$
Comparison\ Cost\downarrow
$$

$$
Temporal\ Reconstruction\ Cost\downarrow
$$

當查詢成本下降，政治承諾、責任與立場的半衰期可能被大幅延長。

---

# 28. 但政治記憶不能變成政治監控

政治人物是公眾人物，但並不代表所有資料都應無限制聚合。

Diligent AI 應優先處理：

$$
Public\ Role\ Data
$$

而不是：

$$
Private\ Life\ Surveillance
$$

除非私人事件與公共權責有明確、可證明的關聯。

系統不應因為「資料可以找到」就認為：

$$
Data\ is\ ethically\ relevant
$$

這一點將由 Paper 07 完整處理。

---

# 29. Archive Asymmetry

不同政治人物的可得資料量不同。

現任總統可能有：

$$
10^6
$$

級別公開資料。

地方政治新人可能只有：

$$
10^3
$$

如果系統直接比較「爭議事件數」，曝光較高的人一定吃虧。

因此任何 actor comparison 必須控制：

$$
Exposure
$$

$$
TimeInOffice
$$

$$
MediaVolume
$$

$$
RolePower
$$

$$
SourceAvailability
$$

可以定義標準化事件率：

$$
Rate=
\frac{
ObservedPatternEvents
}{
RelevantExposureUnits
}
$$

而不是使用 raw counts。

---

# 30. Source Ecology Bias

來源不是中性的。

官方來源傾向：

$$
Institutional\ SelfPresentation
$$

反對黨來源傾向：

$$
Adversarial\ Selection
$$

商業媒體受到：

$$
Newsworthiness
$$

影響。

社群媒體受到：

$$
Engagement
$$

影響。

因此勤人 AI 不應把：

$$
More\ Sources
$$

簡化成：

$$
More\ Truth
$$

而要保存：

$$
SourceClass
+
Incentive
+
EditorialContext
$$

並進行跨來源交叉驗證。

---

# 31. Missingness 本身也是資料

假設某地方政府在 2018–2020 年缺乏完整影音紀錄。

系統不能：

$$
No\ Record
\Rightarrow
No\ Event
$$

而必須標記：

$$
Missing
$$

甚至：

$$
Missing\ Not\ At\ Random
$$

可能本身具有制度含義。

因此每個 analysis output 應包含：

$$
Known
+
Unknown
+
Unavailable
+
Disputed
$$

四種狀態。

---

# 32. 不確定性應該可解釋

自動 fact-checking 研究開始指出，只輸出一個 confidence number 不夠；使用者需要知道究竟是哪幾組證據造成衝突與不確定。

對勤人 AI，同理。

不確定性應可拆成：

$$
U=
(
U_{source},
U_{entity},
U_{time},
U_{claim},
U_{causal},
U_{coverage}
)
$$

而不是只說：

> confidence = 0.63。

尤其人物模型與責任模型，本來就不應假裝具有單一真值。

---

# 33. Human-in-the-Loop 的位置

人類不需要逐筆重做 AI 工作。

真正高價值的人類介入點是：

1. corpus scope 定義；
2. schema 設計；
3. 高風險 entity resolution；
4. 爭議 claim adjudication；
5. causal responsibility 判斷；
6. hypothesis review；
7. publication review；
8. ethical boundary。

因此：

$$
AI=Scale
$$

$$
Human=Judgment
$$

不是完整描述，但比「AI 取代研究者」更接近可行系統。

---

# 34. Query Projection 不得反向污染 Canonical Layer

一個重要工程規則是：

$$
Projection
\nrightarrow
Canonical\ Evidence
$$

例如使用者問：

> 某人是不是逃避責任？

AI 生成一個 hypothesis：

$$
H_{avoidance}
$$

這個 H 不得被寫回 evidence corpus 當成 actor property。

正確流程是：

$$
Query
\rightarrow
Hypothesis
\rightarrow
Evidence\ Test
$$

而不是：

$$
Query\ Label
\rightarrow
Actor\ Database
$$

這可以避免長期 profile 被一次偏見污染。

---

# 35. 勤人 AI 的最小可行系統

一個 MVP 不需要一開始收錄全國所有政治人物。

可以先選：

$$
N_{actors}=10
$$

$$
TimeRange=5\ years
$$

$$
SourceClasses=
Official+Legislative+MajorMedia
$$

建立：

1. canonical source registry；
2. transcript store；
3. actor/entity resolution；
4. claim extraction；
5. event extraction；
6. temporal ledger；
7. provenance；
8. counterevidence query；
9. human review；
10. report projection。

這已經足以驗證核心命題。

---

# 36. 評估方式

Diligent AI 不應只用：

$$
Answer\ Accuracy
$$

評估。

至少要測：

$$
Extraction\ Accuracy
$$

$$
Entity\ Accuracy
$$

$$
Temporal\ Accuracy
$$

$$
Evidence\ Traceability
$$

$$
Counterevidence\ Recall
$$

$$
Coverage
$$

$$
Calibration
$$

$$
Human\ Audit\ Time
$$

最終產品價值則可能再加：

$$
LeadTime
$$

$$
DecisionImpact
$$

但那屬於 Paper 06。

---

# 37. 研究命題

**命題 1：保存優先命題**

相較於先摘要再分析，先保存 canonical evidence 再依 query 投影，能顯著降低後續跨問題分析中的不可恢復資訊損失。

**命題 2：覆蓋透明命題**

明確報告 corpus coverage 與 missingness 的系統，比宣稱「完整分析」但不揭露範圍的系統具有更高可審計性。

**命題 3：curated context 命題**

政治 fact-checking 與 actor analysis 的可靠性高度依賴經整理、具 provenance 的 context，而非只依賴模型 reasoning 能力。

**命題 4：反證搜尋命題**

強制 counterevidence search 能降低人物模型中的 confirmation bias。

**命題 5：時序結構命題**

加入 role、timestamp 與 evidence-state 後，政治立場「矛盾」的誤判率將低於純文本配對。

**命題 6：事件層命題**

以 actor-event-outcome 作為分析單位，能提供比 claim-only fact-check 更完整的治理與責任分析。

**命題 7：長期修正命題**

將 correction thread 納入分析後，政治人物的責任評估會與只分析危機當日發言產生系統性差異。

**命題 8：AI-native 深度內容命題**

當檢索、逐字化、分類與關聯成本下降，持續型深度政治觀測將變得比傳統人工時代更具經濟可行性。

---

# 38. Diligent AI 不是「勤勞的聊天機器人」

如果一個模型：

- 回答很長；
- 找很多網頁；
- 引很多來源；

仍不代表它是勤人 AI。

本文認為至少需要：

$$
Coverage
+
Preservation
+
Provenance
+
Temporality
+
Counterevidence
+
Uncertainty
+
Replayability
$$

七項。

少掉任一核心層，都可能只是一個更會寫長文的摘要系統。

---

# 39. 從政治人物模型走向 Longitudinal Actor Intelligence

本文雖以政治人物為主要例子，但「勤人 AI」的真正一般化形式是：

$$
Longitudinal\ Actor\ Intelligence
$$

同一架構可以研究：

$$
Politician
$$

$$
CEO
$$

$$
Central\ Banker
$$

$$
Regulator
$$

$$
Institution
$$

$$
Corporation
$$

只要對象具有：

$$
Actions
+
Statements
+
Roles
+
Outcomes
+
Time
$$

就能建立長時序 actor model。

政治領域只是：

- 公開資料較多；
- 社會價值高；
- 長期一致性重要；
- 政策與經濟外溢大；

因此特別適合作為第一個實證領域。

---

# 40. 與本系列後續工作的關係

Paper 01：

$$
Actor\ Temporal\ Ledger
$$

Paper 02：

$$
Discourse
\neq
Execution
$$

Paper 03：

$$
Responsibility
\neq
Attribution
\neq
Ownership
$$

Paper 04：

$$
Evidence\ Preservation
+
Longitudinal\ Analysis
+
Query\ Projection
$$

Paper 05 將回答：

> 當勤人 AI 讓資訊整合與論述能力不再稀缺，政治能力如何重新定價？

Paper 06 將回答：

> 這套 actor intelligence 如何成為企業與經濟決策基礎設施？

Paper 07 將處理：

> 什麼資料可以收？什麼假說可以公開？如何避免 AI 人格定罪、政治監控與名譽傷害？

Paper 08 將處理：

> 政治人物本身是如何被教育、職業與制度路徑生成的？

---

# 41. 結論

政治資訊的上一個時代主要解決：

$$
Too\ Much\ Information
$$

方法是：

$$
Compression
$$

下一個時代仍然有太多資訊，但 AI 使我們第一次可以考慮另一種解法：

$$
Structure
+
Preserve
+
Relate
+
Verify
$$

然後才：

$$
Project
$$

勤人 AI 的核心不是產生更多文字，而是建立一個可被重新提問的政治記憶。

因此：

$$
Lazy\ Summary
=
Compress\ Before\ Question
$$

而：

$$
Diligent\ AI
=
Preserve\ Before\ Question
$$

兩者不是速度快慢的差別，而是資訊架構的差別。

真正成熟的政治 AI 不應說：

> 「我已經幫你看完所有資料，所以答案是 X。」

而應說：

> 「在已宣告的資料範圍內，我涵蓋了哪些來源、漏了哪些來源；以下是觀察事實、衍生關係、支持證據、反證、不確定性與目前最能解釋資料的假說。你可以沿著任何一條 evidence path 回到原始來源。」

這才是從懶人包跨入勤人 AI 的分界。

最終，勤人 AI 的價值可以壓縮成：

$$
\boxed{
Human\ cannot\ read\ everything\ repeatedly;
a\ system\ can\ preserve\ enough\ structured\ evidence\ to\ make\ repeated\ deep\ inquiry\ possible.
}
$$

這不保證政治分析永遠正確。

它做的是另一件更基礎的事：

$$
Make\ Diligence\ Computable
$$

。

---

# References

Beieler, J., Brandt, P. T., Halterman, A., Schrodt, P. A., & Simpson, E. M. (2016). Generating Political Event Data in Near Real Time: Opportunities and Challenges. In R. M. Alvarez (Ed.), *Computational Social Science*. Cambridge University Press.

DeVerna, M. R., Yang, K.-C., Yan, H. Y., & Menczer, F. (2026). Large Language Models Require Curated Context for Reliable Political Fact-Checking—Even with Reasoning and Web Search. *Findings of the Association for Computational Linguistics: ACL 2026*, 29338–29360. https://doi.org/10.18653/v1/2026.findings-acl.1467

Hou, Z., Jin, X., Li, Z., Bai, L., Guan, S., Zeng, Y., Guo, J., & Cheng, X. (2023). Temporal Knowledge Graph Reasoning Based on N-tuple Modeling. *Findings of EMNLP 2023*. https://aclanthology.org/2023.findings-emnlp.77/

Loginova, E., Ermakov, M., & Khramov, S. (2026). From News Streams to Narrative Intelligence Briefs: LLM-Assisted Political Discourse Analysis in the Hungarian 2026 Pre-Election Context. *Proceedings of the 3rd Workshop on Natural Language Processing for Political Sciences (PoliticalNLP 2026)*. https://aclanthology.org/events/politicalnlp-2026/

Mitra, K., Zhang, D., Rahman, S., & Hruschka, E. (2025). FactLens: Benchmarking Fine-Grained Fact Verification. *Findings of the Association for Computational Linguistics: ACL 2025*, 18085–18096. https://aclanthology.org/2025.findings-acl.929/

Osmonova, T., Tikhonov, A., & Yamshchikov, I. P. (2024). Knowledge Graph Representation for Political Information Sources. *Proceedings of the Workshop on Natural Language Processing for Political Sciences*. https://aclanthology.org/2024.politicalnlp-1.6/

Shukla, S., Dutta, H., & Bhattacharyya, P. (2025). Recon, Answer, Verify: Agents in Search of Truth. *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track*. https://aclanthology.org/2025.emnlp-industry.167/

Stephens, L., Llewellyn, C., Rogers, L., Kyritsopoulos, C., Prangere, A., Long, F., Snyder, P., & Cram, L. (2026). Can Large Language Models Facilitate Qualitative Political Narrative Analysis? *Proceedings of the 3rd Workshop on Natural Language Processing for Political Sciences (PoliticalNLP 2026)*. https://aclanthology.org/events/politicalnlp-2026/

Wiegmann, M., Neyer, J., & Stein, B. (2026). Exploring Two Decades of Parliamentary Speeches on the Use of Narratives. *Proceedings of the 3rd Workshop on Natural Language Processing for Political Sciences (PoliticalNLP 2026)*. https://aclanthology.org/events/politicalnlp-2026/

Wilson, M., Martin-Morales, K., & Nelson, G. (2026). From Text to Events: Turning Freedom House Reports into Evidence of Democratization and Democratic Backsliding. *APSA Preprints*. https://preprints-apsa.prod.orp.cambridge.org/engage/apsa/article-details/69cc1305810b9dcc82c34a47

Xu, R., Li, G., & Sheng, V. S. (2026). GAVEL: Evidence-Contract Debate with Mechanized Scrutiny for Provenance-Grounded Fact-Checking. *Findings of the Association for Computational Linguistics: ACL 2026*. https://aclanthology.org/2026.findings-acl.1789/

---

## Canonical Source Note

本檔為 Paper 04 v0.1 的 UTF-8 canonical Markdown source。正式數學 source 僅使用 ` $...$ ` 與 `$$...$$` delimiter。本文所有 summary、圖表、PDF、HTML 與聊天畫面均屬 rendering/projection，不取代本檔。任何人物模型亦不得回寫為 canonical evidence。
