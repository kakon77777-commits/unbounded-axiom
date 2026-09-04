---
document_id: "UA-ANPC-A04"
series: "AI-Native Preprint Commons Series"
series_part: 4
version: "0.1"
language: "zh-Hant"
title: "引用不是裝飾：AI 原生 Source Reality、Citation Validation 與 Data Provenance"
english_title: "Citations Are Not Decoration: AI-Native Source Reality, Citation Validation, and Data Provenance"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / evidence-infrastructure paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# 引用不是裝飾

## AI 原生 Source Reality、Citation Validation 與 Data Provenance

### AI-Native Preprint Commons Series — Paper 04

---

## 摘要

AI 研究系統已能大量搜尋網路、讀取論文、整理 bibliography、引用資料庫、執行程式與生成近似正式論文的長篇研究。然而，「搜尋到某個結果」「找到一個真實來源」「來源內存在相關內容」「該內容可作為證據」「證據真的支持目前 claim」是五個不同事件。若平台只保存網址、DOI 或 references list，AI 仍可能產生真實文獻上的錯誤歸因、失效連結上的虛假確定性、版本錯配、二手資料被當成一手資料、搜尋摘要被當成全文、撤回論文仍持續支撐下游主張，以及經多次資料轉換後已無法重建原始數值來源的問題。

本文提出 **Source Reality and Evidence Provenance Architecture（SREPA）**，作為 Unbounded Axiom AI-native preprint commons 的來源與證據基礎層。SREPA 將來源物件、來源現實狀態、存取狀態、版本狀態、內容定位、citation relation、semantic support、資料 transformation lineage、search audit 與 downstream dependency propagation 分開建模。

本文延續既有 **Mathematical Citation Compiler（MCC）**、**Citation-Validation Closure（CVC）** 與 **FCVP / FELRA Citation Validation Profile** 的設計原則，將其由 theorem-level mathematical dependency auditing 一般化為跨領域研究來源架構。其核心規則包括：

$$
\boxed{
\text{Search Result}
\neq
\text{Source}
\neq
\text{Evidence}
\neq
\text{Support}.
}
$$

以及：

$$
\boxed{
\text{No layer self-certifies another layer}.
}
$$

SREPA 進一步區分 `SEARCH_ONLY`、`METADATA_VERIFIED`、`SOURCE_LOCATED`、`CONTENT_ACCESSED`、`CLAIM_SUPPORTED`、`ARCHIVED_COPY_ONLY`、`DEAD_LINK`、`MOVED`、`UPDATED`、`CORRECTED`、`RETRACTED`、`WITHDRAWN`、`SUPERSEDED`、`SOURCE_UNAVAILABLE`、`SOURCE_NOT_FOUND` 與其他狀態，使「來源現在打不開」不再等同「來源從未存在」。

對數據型研究，本文提出：

$$
\boxed{
\text{Claim}
\leftarrow
\text{Derived Value}
\leftarrow
\text{Transformation}
\leftarrow
\text{Dataset Snapshot}
\leftarrow
\text{Primary Source}.
}
$$

因此一個圖表或數值 claim 不應只寫「Source: World Bank」，而應保存 dataset version、retrieval time、filter、join、aggregation、unit conversion、code/config hash 與輸出 fingerprint。對 citation 更新與撤回，本文提出 downstream revalidation：上游來源撤回不自動證明所有下游 claim 為假，但必須將相關 dependency edge 標為 stale 並重新計算 claim support state。

SREPA 的目的不是把引用制度神聖化，而是將 citation 與 data source 還原成它們最重要的功能：**可由另一個人類或 AI 沿著指標回到外部世界，重新取得、定位、理解與審查研究所依賴的證據。**

**關鍵詞：** Source Reality、Citation Validation、Data Provenance、Evidence Provenance、MCC、CVC、FCVP、Crossmark、DataCite、PROV-O、FAIR、AI 預印本、Unbounded Axiom

---

# 1. 問題：引用存在，不代表引用成立

一條 citation 至少可能在四種不同意義上「看起來正確」：

1. 文獻名字真的存在；
2. DOI 真的存在；
3. 內容真的談到相似主題；
4. 內容真的可以支撐目前這一句 claim。

只有前兩者，並不足以建立研究依賴。

因此：

$$
\boxed{
\text{Bibliographic Existence}
\not\Rightarrow
\text{Semantic Support}.
}
$$

更不代表：

$$
\boxed{
\text{Semantic Relevance}
\not\Rightarrow
\text{Valid Dependency}.
}
$$

這是 AI citation hallucination 問題更深的一層。

最危險的引用，不一定是完全不存在的假論文。

它可能是一篇完全真實、作者正確、DOI 正確、主題也相關，但根本沒有支持 AI 所寫結論的論文。

---

# 2. 引用制度真正有價值的地方不是禮儀，而是 Reality Pointer

學術傳統經常將 citation 描述成：

- 給前人 credit；
- 顯示熟悉 literature；
- 建立 scholarly context；
- 支援 novelty claim。

這些都重要。

但對 AI-native research infrastructure，citation 最基礎的功能可以寫成：

$$
\boxed{
\text{Citation}
=
\text{Recoverable Pointer to an External Evidence Object}.
}
$$

一條好的引用應讓另一個智能能夠：

1. 找到來源；
2. 確認來源身份；
3. 找到相關位置；
4. 讀取原始語境；
5. 判斷其是否支持目前 claim；
6. 確認引用版本；
7. 知道來源是否已更正、撤回或失效。

因此 citation 的品質不是：

$$
\text{reference count}.
$$

而更接近：

$$
\boxed{
\text{recoverability}
+
\text{identity}
+
\text{localization}
+
\text{support}
+
\text{provenance}.
}
$$

---

# 3. 既有基礎：MCC / CVC 已經建立 theorem-level citation dependency

既有 Mathematical Citation Compiler 將來源 theorem 表示為：

$$
\tau_j
=
(
H_j,
Q_j,
\Delta_j,
V_j,
S_j
),
$$

其中：

- $H_j$：來源 theorem hypotheses；
- $Q_j$：conclusion；
- $\Delta_j$：domain / type conditions；
- $V_j$：version 與 bibliographic identity；
- $S_j$：精確 source span。

一條引用 edge：

$$
e_{ij}
:
c_i
\leftarrow
\tau_j
$$

若要成為 mathematical dependency，不能只滿足 semantic relevance。

還必須建立可審計 mapping：

$$
\phi_{ij}
:
(D_j,H_j,Q_j)
\rightarrow
(D_i,A_i,c_i).
$$

若不存在這個 mapping，最多只能成為 contextual citation，而不是 proof dependency。

本文保留這個核心，但將 source object 從 theorem 擴大到：

- paper；
- dataset；
- webpage；
- book；
- archive；
- API response；
- legal document；
- historical source；
- source code；
- experiment artifact；
- benchmark；
- repository revision；
- multimedia record；
- model output；
- private attested source。

---

# 4. No Layer Self-Certifies Another Layer

FCVP v0.3 已提出非常重要的工程紀律：

- metadata similarity 不能自動設定 source localization PASS；
- source localization 不能自動設定 semantic support PASS；
- AI interpretation 不能自動設定 bibliographic identity；
- computational replay 不能偷偷變成 universal proof；
- provider unavailable 必須被記錄。

本文將此一般化為：

$$
\boxed{
\text{No layer self-certifies another layer}.
}
$$

例如：

$$
\text{DOI Match}
\not\Rightarrow
\text{Exact Span Match}.
$$

$$
\text{Exact Span Match}
\not\Rightarrow
\text{Claim Support}.
$$

$$
\text{Claim Support}
\not\Rightarrow
\text{Independent Confirmation}.
$$

$$
\text{Independent Confirmation}
\not\Rightarrow
\text{Universal Truth}.
$$

---

# 5. SREPA：Source Reality and Evidence Provenance Architecture

本文提出：

$$
\boxed{
\mathcal S
=
(
O,
R,
A,
V,
L,
E,
P,
T,
G
).
}
$$

其中：

- $O$：Source Object；
- $R$：Reality State；
- $A$：Access State；
- $V$：Version State；
- $L$：Localization；
- $E$：Evidence Relation；
- $P$：Provenance；
- $T$：Temporal State；
- $G$：Dependency Graph。

SREPA 與 Paper 03 CECA 的關係是：

$$
\boxed{
\text{SREPA}
\rightarrow
\text{verified evidence inputs}
\rightarrow
\text{CECA}.
}
$$

---

# 6. Source Object：來源本身必須是可識別物件

定義 source object：

$$
\boxed{
O_s
=
(
id,
kind,
identifiers,
creator,
title,
publisher,
time,
version,
locator,
integrity
).
}
$$

可能的 `kind`：

```text
journal-article
preprint
book
book-chapter
dataset
repository
source-code
webpage
api-response
government-record
legal-document
historical-record
archive-object
experiment-artifact
benchmark
model-output
image
audio
video
private-record
other
```

---

# 7. Persistent Identifier 很重要，但不是全部

來源可能具有：

```text
DOI
arXiv ID
ISBN
ISSN
PMID
SWHID
RAiD
Handle
ARK
repository commit SHA
dataset accession
internal persistent ID
```

DataCite Metadata Schema 4.7 在 2026 年新增 RAiD、SWHID 等 related identifier type，顯示研究輸出與 software / project 之間的 persistent relation 正在持續擴張。

但：

$$
\boxed{
\text{Persistent Identifier}
\neq
\text{Content Verification}.
}
$$

identifier 主要解決 identity 與 retrieval。

內容是否支援 claim 是下一層。

---

# 8. Reality State：來源到底是否曾經存在

本文提出 Source Reality State：

```text
DISCOVERED
SEARCH_ONLY
METADATA_ONLY
BIBLIOGRAPHIC_VERIFIED
HISTORICALLY_VERIFIED
SOURCE_LOCATED
CONTENT_ACCESSED
ARCHIVED_COPY_ONLY
MOVED
UPDATED
CORRECTED
SUPERSEDED
WITHDRAWN
RETRACTED
DEAD_LINK
SOURCE_UNAVAILABLE
SOURCE_NOT_FOUND
AMBIGUOUS_IDENTITY
CONFLICTING_RECORDS
UNRESOLVED
```

這些狀態可以組合，而不是一定互斥。

---

# 9. SEARCH_ONLY

AI 只看到：

- search result；
- snippet；
- knowledge panel；
- result title；
- provider summary。

尚未打開 source。

因此：

$$
\boxed{
\texttt{SEARCH\_ONLY}
\not\Rightarrow
\texttt{SOURCE\_VERIFIED}.
}
$$

這個狀態非常重要。

因為網路搜尋模型最常發生的錯誤之一，就是將 snippet interpretation 當成完整來源閱讀。

---

# 10. METADATA_ONLY

系統已確認：

- title；
- creator；
- identifier；
- publication date；
- venue；

但沒有取得全文或實際 source body。

例如 Crossref / DataCite metadata 可確認某研究輸出存在。

此時可以支援：

> 某項作品存在。

但不能自動支援：

> 作品內證明了某命題。

---

# 11. BIBLIOGRAPHIC_VERIFIED

來源 identity 已通過多欄位或 authoritative registry 檢查。

可以包括：

```text
identifier match
creator match
title match
venue match
date match
version match
```

bibliographic identity 應該是 source-level state。

不是由 LLM 以語義相似度自行宣布。

---

# 12. HISTORICALLY_VERIFIED

這個狀態用來處理：

> 現在已經打不開，但我們可以證明它曾經存在。

例如：

- DOI record；
- archive snapshot；
- signed manifest；
- earlier source hash；
- independent citation record；
- institutional archive；
- previous canonical snapshot。

因此：

$$
\boxed{
\text{Currently Unavailable}
\neq
\text{Never Existed}.
}
$$

---

# 13. DEAD_LINK 不等於 SOURCE_NOT_FOUND

`DEAD_LINK`：

> 已知 URL 目前失效。

`SOURCE_NOT_FOUND`：

> 在目前 search scope 中無法找到可靠 source identity。

兩者完全不同。

例如：

```text
URL: dead
DOI: valid
archive: available
```

應該是：

```text
DEAD_LINK
+
HISTORICALLY_VERIFIED
+
ARCHIVED_COPY_ONLY
```

而不是：

```text
SOURCE_NOT_FOUND
```

---

# 14. SOURCE_UNAVAILABLE 也不等於 DEAD_LINK

source 可能因：

- paywall；
- permission；
- geographic restriction；
- private dataset；
- temporary outage；
- authentication；
- repository maintenance；

而無法取得。

此時：

```text
SOURCE_UNAVAILABLE
```

比：

```text
DEAD_LINK
```

更準確。

---

# 15. MOVED

來源 URL 或 repository path 改變，但 identity 保持。

平台應記錄：

$$
u_1
\rightarrow
u_2.
$$

不能把 URL 當 source identity 本身。

---

# 16. UPDATED、CORRECTED、SUPERSEDED

來源內容可能合法更新。

例如：

$$
V_1
\rightarrow
V_2.
$$

不同狀態：

- UPDATED：有新版本或內容更新；
- CORRECTED：修正原內容；
- SUPERSEDED：新版取代舊版作為主要版本。

平台必須保存 version relation，而不是只抓目前頁面。

---

# 17. WITHDRAWN 與 RETRACTED

二者也不應被平台隨意混用。

不同出版體系可能定義不同。

SREPA 的核心要求是：

> 保存 provider / publisher 所宣告的正式 update type，不自行美化。

例如：

```yaml
source_status:
  provider_state: "retracted"
  provider: "Crossref/Crossmark"
  notice_id: "..."
  effective_at: "..."
```

---

# 18. Crossmark 與 Source Status Update

Crossref 的 Crossmark 已提供跨平台 content status 機制，可顯示：

- correction；
- retraction；
- update；
- withdrawal；

以及其他與解釋或 credit 有關的重要變更。

Unbounded Axiom 不需要重造 publisher update semantics。

正確方向是：

$$
\boxed{
\text{External Status Signal}
\rightarrow
\text{SREPA Source State}.
}
$$

但 external status signal 仍需保存 provider provenance。

---

# 19. FAIR 的重要啟示：資料本體消失，metadata 仍應存在

FAIR 原則中有一條特別適合長期 AI research ecology：

> metadata 應在 data 本體不再可用後仍可取得。

這意味著 Unbounded Axiom 不應在 source 消失後把 source node 一併刪除。

正確做法是：

$$
\boxed{
\text{Source Node persists}
\quad
\text{while Access State changes}.
}
$$

因此：

```text
source exists historically
data unavailable now
metadata preserved
```

可以同時成立。

---

# 20. Access State 與 Reality State 必須分離

定義：

$$
A_s
\in
\{
\texttt{OPEN},
\texttt{AUTHENTICATED},
\texttt{PAYWALLED},
\texttt{RESTRICTED},
\texttt{PRIVATE},
\texttt{ARCHIVED},
\texttt{UNAVAILABLE},
\texttt{UNKNOWN}
\}.
$$

因此：

$$
\boxed{
\text{Access}
\neq
\text{Existence}.
}
$$

---

# 21. Content Access 不等於 Legal Reuse

平台可以取得全文，不代表可以任意重新公開全文。

因此 SREPA 另保存：

```text
license
reuse_rights
quotation_policy
archive_permission
unknown_rights
```

Unbounded Axiom 可以保存 minimal evidence span、hash、locator 與必要 provenance，而不必鏡像所有外部內容。

---

# 22. Exact Source Localization

對每條 evidence relation：

$$
c_i
\leftarrow
s_j
$$

應儘可能定位：

```text
page
section
paragraph
table
figure
theorem
lemma
proposition
equation
dataset row
column
API field
commit path
line range
timestamp
video timecode
archive item
```

因此：

$$
\boxed{
\text{Source Identity}
\neq
\text{Source Localization}.
}
$$

---

# 23. Locator 應該可跨 Representation

同一篇研究可能有：

- HTML；
- PDF；
- Markdown；
- XML；
- source repository。

因此 locator 可以表示：

```yaml
locators:
  - representation: "html"
    selector: "section-4-paragraph-3"

  - representation: "pdf"
    page: 12

  - representation: "source"
    path: "paper.md"
    line_start: 334
    line_end: 351
```

canonical source 若存在，優先用可穩定定位的 source locator。

---

# 24. Source Span Snapshot

若合法且必要，可保存 minimal source span snapshot：

```text
span_hash
retrieved_at
representation
locator
content_excerpt
```

重點是：

$$
\boxed{
\text{Locator}
+
\text{Hash}
+
\text{Timestamp}
}
$$

比只保存 URL 穩定。

---

# 25. Citation Relation 不能全部叫 `cites`

不同 citation 有不同學術作用。

本文沿用並一般化 MCC：

```text
DEPENDENCY
SUPPORT
PRECEDENCE
CONTEXT
CONTRAST
DATA
METHOD
REPRODUCTION
REPLICATION
GENERALIZATION
SPECIALIZATION
CRITIQUE
BACKGROUND
DEFINITION
IMPLEMENTATION
```

---

# 26. DEPENDENCY

表示：

> 若這個來源不成立，當前 claim 的推理依賴可能受影響。

這是最強的 citation edge 之一。

數學 theorem dependency 是典型案例。

---

# 27. SUPPORT

來源對 claim 提供實質支持，但 claim 不一定邏輯依賴它。

例如一個現象有多個獨立資料集支持。

---

# 28. PRECEDENCE

表示：

> 此來源先前提出相似概念、方法或研究方向。

它主要與 priority / novelty 有關。

不代表目前 claim 依賴它。

---

# 29. CONTEXT

提供背景、領域位置或相關文獻。

context citation 不能被下游 AI 當成 proof edge。

---

# 30. CONTRAST

來源與目前 claim 有：

- 不同結果；
- 不同模型；
- 競爭解釋；
- 反對立場。

這不是「負面 citation」。

它是一個有意義的 typed relation。

---

# 31. DATA

表示目前 claim、figure 或 analysis 使用該 dataset / data source。

這種 edge 必須再連到 transformation lineage。

---

# 32. METHOD

研究方法源自或實作某來源。

例如：

```text
uses-method-from
```

與：

```text
supports-claim
```

不能混在一起。

---

# 33. Semantic Support State

一條 citation edge 的 support 狀態可以是：

```text
UNASSESSED
CONTEXT_ONLY
TOPICALLY_RELEVANT
PARTIALLY_SUPPORTS
DIRECTLY_SUPPORTS
SUPPORTS_WITH_CONDITIONS
CONTRADICTS
MISATTRIBUTED
OUT_OF_SCOPE
DOMAIN_MISMATCH
HYPOTHESIS_MISMATCH
UNRESOLVED
```

---

# 34. 真實來源也可能是 MISATTRIBUTED

例如 paper A 真實存在。

但 claim：

> Paper A 發現 X。

實際 paper A 說的是 Y。

此時：

```text
source_reality: VERIFIED
citation_relation: MISATTRIBUTED
```

這比：

```text
fake citation
```

更精確。

---

# 35. Source Hypothesis Mapping

對理論、數學、工程與統計來源，來源結論往往依賴假設。

因此：

$$
s_j:
H_j
\Rightarrow
Q_j.
$$

當前 claim 若使用 $Q_j$，必須確認：

$$
H_j
$$

是否在目前 context 被滿足。

否則：

```text
HYPOTHESIS_MISMATCH
```

---

# 36. Domain Mapping

來源可能在 domain：

$$
D_j
$$

成立。

但目前研究使用於：

$$
D_i.
$$

需要合法 mapping：

$$
\psi:
D_j
\rightarrow
D_i.
$$

沒有 mapping 時，不能只因公式長得相似就引用。

---

# 37. Search Audit：搜尋過程本身要留下可重播證據

高風險研究至少應保存：

```text
query
provider
time
filters
result IDs
selected results
rejected results
search scope
cutoff
```

因此：

$$
\boxed{
\text{Search Discovery}
\text{ can be audited}.
}
$$

---

# 38. Search Rank 不等於 Credibility

既有 runtime 已明確規定：

$$
\boxed{
\text{SearchRank}
\neq
\text{Credibility}.
}
$$

第一名搜尋結果可能只是：

- SEO；
- popularity；
- freshness；
- personalization；
- provider ranking。

因此 search rank 只是一種 acquisition signal。

---

# 39. Search Result 不等於 Evidence

搜尋結果可以幫 AI 找 source。

它本身通常不應被當成 material claim 的終極 evidence。

正式鏈應是：

$$
\boxed{
\text{Search Result}
\rightarrow
\text{Source Resolution}
\rightarrow
\text{Content Access}
\rightarrow
\text{Localization}
\rightarrow
\text{Support Validation}.
}
$$

---

# 40. Search Coverage 必須明示

若 AI 說：

> 沒有找到先前研究。

至少要知道：

```text
providers
queries
languages
date range
databases
citation graph depth
access limitations
```

因此：

$$
\boxed{
\text{Not Found Within Search Scope}
\neq
\text{Does Not Exist}.
}
$$

這與 Paper 03 的：

$$
\text{No Evidence Found}
\neq
\text{Evidence of Absence}
$$

直接相容。

---

# 41. Provider Diversity

重要 claim 可以使用不同 provider：

```text
Crossref
DataCite
OpenAlex
Semantic Scholar
arXiv
PubMed
institutional repository
publisher site
official government source
domain database
```

但 provider 數量仍不等於 source independence。

---

# 42. Provider Independence 不等於 Source Independence

Crossref、OpenAlex、Semantic Scholar 可能都返回同一篇 paper metadata。

這是：

$$
3\text{ provider observations}
$$

但只有：

$$
1\text{ scholarly source}.
$$

因此：

$$
\boxed{
\text{Provider Multiplicity}
\neq
\text{Evidence Independence}.
}
$$

---

# 43. Data Provenance：數字不能只寫來源名稱

考慮研究寫：

> 2025 年某指標為 37.2%。

只寫：

```text
Source: Dataset X
```

仍然不夠。

因為 37.2 可能經過：

- filter；
- missing-value removal；
- unit conversion；
- normalization；
- join；
- aggregation；
- weighting；
- rounding；
- imputation。

因此：

$$
\boxed{
\text{Data Source}
\neq
\text{Derived Value Provenance}.
}
$$

---

# 44. Data Lineage

本文定義：

$$
\boxed{
y
=
T_k
\circ
T_{k-1}
\circ
\cdots
\circ
T_1
(D_0).
}
$$

其中：

- $D_0$：原始 dataset snapshot；
- $T_i$：每一步 transformation；
- $y$：最終數字、表格或圖表資料。

完整鏈：

$$
\boxed{
\text{Claim}
\leftarrow
\text{Derived Value}
\leftarrow
\text{Transformation}
\leftarrow
\text{Dataset Snapshot}
\leftarrow
\text{Primary Source}.
}
$$

---

# 45. Dataset Snapshot

不能只保存：

```text
dataset: latest
```

應至少保存：

```text
dataset_id
version
release_date
retrieved_at
query
snapshot_hash
license
source_url
schema_version
```

如果 dataset 是 API：

```text
endpoint
parameters
pagination
response date
provider version
```

也應保存。

---

# 46. Transformation Receipt

每一步 transformation：

$$
T_i
$$

至少記錄：

```yaml
operation_id:
input_refs:
operation:
parameters:
code_ref:
environment:
output_ref:
output_hash:
performed_by:
time:
```

這使另一個 AI 能重播。

---

# 47. Data Join 是高風險操作

當兩個 dataset：

$$
D_1,D_2
$$

join：

$$
D_3
=
D_1
\Join
D_2,
$$

需要保存：

```text
join keys
join type
deduplication
unmatched rows
entity resolution
time alignment
unit alignment
```

否則 derived claim 很難重現。

---

# 48. Unit Conversion 也是 Provenance

例如：

$$
USD
\rightarrow
TWD.
$$

至少保存：

```text
exchange-rate source
rate date
rate type
rounding
```

同理：

- nominal → real；
- Celsius → Kelvin；
- counts → rates；
- raw → standardized。

不要把這些處理當成無關緊要的「格式」。

---

# 49. Figure Provenance

一張 data figure 應有：

$$
F
\leftarrow
P
\leftarrow
D
\leftarrow
S.
$$

其中：

- $S$：source；
- $D$：dataset；
- $P$：plot / transformation spec；
- $F$：rendered figure。

因此 PNG 只是 projection。

canonical 可以是：

```text
data source
transform
plot spec
renderer version
```

---

# 50. AI Illustrative Figure 與 Data Figure 必須分離

如果 AI 畫一張概念圖：

```text
AI-ILLUSTRATIVE-DIAGRAM
```

就不能在 UI 上看起來像實驗數據。

因此：

$$
\boxed{
\text{Illustration}
\neq
\text{Empirical Figure}.
}
$$

---

# 51. Model-Generated Data 必須明示

synthetic data、simulation data、LLM-generated labels 都需要 explicit provenance。

例如：

```text
SYNTHETIC_DATA
SIMULATION_OUTPUT
MODEL_ANNOTATION
MODEL_INFERENCE
```

不能被轉成：

```text
OBSERVED_DATA
```

---

# 52. W3C PROV 作為互操作基礎

W3C PROV 提供：

```text
Entity
Activity
Agent
```

以及產生、使用、歸因、派生等 provenance relation。

SREPA 可以將：

- source snapshot → Entity；
- transformation → Activity；
- human/AI/tool/runtime → Agent；
- derived dataset → Entity；

映射到 PROV。

因此不需要重新發明所有 provenance 語彙。

---

# 53. 但 SREPA 需要比一般 PROV 更細的 scholarly semantics

PROV 可以回答：

> 這個 artifact 如何被產生？

但 Unbounded Axiom 還需要回答：

> 這個 source 是否真的支持這個 claim？

所以：

$$
\boxed{
\text{PROV}
+
\text{Scholarly Support Semantics}
=
\text{SREPA}.
}
$$

---

# 54. DataCite 作為 Research Resource Identity Layer

DataCite 的強項是：

- research output identity；
- creator；
- dates；
- resource type；
- related identifiers；
- version/relation metadata。

因此 SREPA 可以映射：

$$
\text{DataCite Metadata}
\rightarrow
\text{Source Identity}.
$$

但 semantic support 仍由 SREPA edge validation 決定。

---

# 55. Crossref / Crossmark 作為 Scholarly Update Signal

Crossmark 可以提供：

- correction；
- retraction；
- withdrawal；
- update；

等 status change。

因此 SREPA 可以訂閱或定期重新檢查：

$$
\text{Source Status Signal}.
$$

但 source state change 不應直接靜默改掉 downstream manuscript。

應觸發：

$$
\boxed{
\text{Dependency Revalidation}.
}
$$

---

# 56. Citation Dependency Graph

定義：

$$
G_{\mathrm{cite}}
=
(
V_C
\cup
V_S,
E_{\mathrm{cite}}
).
$$

其中：

- $V_C$：claim nodes；
- $V_S$：source nodes；
- $E_{\mathrm{cite}}$：typed citation edges。

這是 bibliography 的結構化版本。

---

# 57. Data Provenance Graph

定義：

$$
G_{\mathrm{data}}
=
(
V_S
\cup
V_D
\cup
V_T
\cup
V_O,
E_D
).
$$

其中：

- $V_S$：source；
- $V_D$：dataset snapshots；
- $V_T$：transformation activities；
- $V_O$：outputs / figures / values。

---

# 58. Unified Evidence Graph

最終：

$$
\boxed{
G_E
=
G_{\mathrm{cite}}
\cup
G_{\mathrm{data}}
\cup
G_{\mathrm{validation}}.
}
$$

可讓 AI 追蹤：

> 這個 conclusion 到底站在哪些外部證據上？

---

# 59. Upstream Update Propagation

假設：

$$
s
\rightarrow
c_1
\rightarrow
c_2
\rightarrow
c_3.
$$

若：

$$
s
$$

被 retracted。

不能忽略。

平台應標記相關 edge：

```text
STALE
REVALIDATION_REQUIRED
```

---

# 60. Upstream Retraction 不等於 Downstream Falsity

但：

$$
\boxed{
\text{Source Retracted}
\not\Rightarrow
\text{All Downstream Claims False}.
}
$$

因為：

- claim 可能有其他獨立證據；
- source 可能只提供 context；
- retraction 原因可能不影響所引用部分；
- downstream result 可能獨立重現。

因此正確流程：

$$
\boxed{
\text{Source Status Change}
\rightarrow
\text{Affected Edge Discovery}
\rightarrow
\text{Claim Re-evaluation}.
}
$$

---

# 61. Retraction Propagation Algorithm

概念上：

```text
1. receive source status event
2. identify source node
3. enumerate outgoing citation/evidence edges
4. classify edge criticality
5. mark affected edges stale
6. recompute claim support profile
7. propagate only if downstream support changes
8. emit revision events
9. notify affected authors / agents where applicable
```

這可以避免全域不必要 cascading failure。

---

# 62. Edge Criticality

citation edge 可以有：

```text
proof-critical
data-critical
major-support
minor-support
context-only
precedence-only
contrast-only
```

只有真正 critical edge 失效時才可能直接重開 claim。

---

# 63. Source Correction Propagation

若 source 只更正：

```text
author affiliation typo
```

不應重開所有 claim。

若更正：

```text
Table 2 values
```

且 downstream claim 引用 Table 2，則必須重開。

因此 source update 必須能定位：

$$
\Delta S.
$$

---

# 64. Version Drift

研究者在 2026 年引用：

$$
V_1.
$$

2028 年 source 已變成：

$$
V_3.
$$

若平台只重新抓最新頁面，就可能用 V3 內容驗證 V1 citation。

因此：

$$
\boxed{
\text{Citation Verification}
\text{ must be version-aware}.
}
$$

---

# 65. Snapshot Identity

對 source snapshot：

$$
S_t
$$

保存：

```text
source_id
version_id
retrieved_at
content_hash
representation
locator
provider
```

可回答：

> 當時引用的是哪一個版本？

---

# 66. Web Source 的特殊問題

網頁可能原地修改而不改 URL。

因此對高價值 web evidence：

```text
retrieved_at
content hash
archive locator
publisher/update metadata
```

特別重要。

---

# 67. API Source 的特殊問題

API response 依：

```text
time
parameters
account permissions
version
regional state
provider state
```

可能不同。

因此：

$$
\boxed{
\text{API Endpoint}
\neq
\text{API Evidence Snapshot}.
}
$$

應保存 request/response provenance。

---

# 68. Dynamic Data 的 Temporal Scope

例如：

> 台股某日收盤價。

必須保存：

```text
observation date
timezone
retrieval date
market session
source
adjustment state
```

不能只保存「現在查到的數字」。

---

# 69. Historical Source 的 Provenance

歷史研究 source 可能有：

```text
original document
transcription
translation
edition
digitization
OCR
modern commentary
```

這些不是同一來源層級。

因此：

$$
\boxed{
\text{Primary Artifact}
\neq
\text{Transcription}
\neq
\text{Translation}
\neq
\text{Interpretation}.
}
$$

---

# 70. Translation Provenance

如果 AI 引用翻譯：

```text
source_language
translation_author
translation_version
machine_translation
human_review
```

應保存。

尤其概念哲學、法律與歷史文本，翻譯本身可能改變 claim interpretation。

---

# 71. Repository / Code Source

工程與計算研究不應只引用：

```text
GitHub repository URL
```

應盡可能引用：

```text
repository
commit SHA
path
line range
release/tag
dependency lock
```

因為 main branch 會變。

---

# 72. Software Heritage 與 SWHID 的重要性

DataCite 4.7 新增 SWHID related identifier type，反映 software artifact identity 在研究 metadata 中的重要性。

對 AI-native research：

$$
\boxed{
\text{Code Version}
\text{ is evidence provenance}.
}
$$

---

# 73. Experimental Artifact Provenance

實驗 evidence 可包含：

```text
protocol
instrument
instrument calibration
sample
operator
timestamp
environment
raw output
processing
analysis
```

platform 不需要把所有實驗領域都標準化，但應允許 domain profile 擴展。

---

# 74. Evidence Independence Graph

同一結論可能有：

$$
e_1,e_2,e_3.
$$

需要知道：

- 是否共用 dataset；
- 是否共用 upstream source；
- 是否由同一模型生成；
- 是否共用 code；
- 是否只是轉載。

因此：

$$
\operatorname{Independent}(e_i,e_j)
$$

不能只由作者名稱不同判定。

---

# 75. Source Sybil

網路上可能大量文章複製同一錯誤敘事。

如果 AI 只計算：

$$
\text{source count},
$$

可能被 source sybil 攻擊。

因此需要：

```text
content similarity
upstream citation
publication time
ownership relation
shared origin
syndication
```

幫助判定 source independence。

---

# 76. Search Poisoning

惡意行為者可以發布大量：

- SEO content；
- fake papers；
- synthetic citations；
- mutually citing pages。

因此：

$$
\boxed{
\text{Retrieval Diversity}
+
\text{Identity Verification}
+
\text{Source Independence}
+
\text{Counterevidence}
}
$$

是 AI research search 的必要防線。

---

# 77. Citation Commit Gate

對 material claim，citation commit 應是一個 policy gate。

通用最低條件可以表示：

$$
\boxed{
b
\land
l
\land
s
\land
r
}
$$

其中：

- $b$：source identity verified；
- $l$：source located；
- $s$：semantic support assessed；
- $r$：relation type assigned。

高風險 claim 再增加 domain-specific requirements。

---

# 78. Citation Commit 不是一定要 PASS

系統品質不應以：

$$
\text{citation count}
$$

最大化。

應允許：

```text
UNRESOLVED
AMBIGUOUS_SOURCE
PRIMARY_SOURCE_NOT_FOUND
DOMAIN_MISMATCH
HYPOTHESIS_MISMATCH
VERSION_MISMATCH
SUPPORT_NOT_ESTABLISHED
SOURCE_UNAVAILABLE
DO_NOT_COMMIT
```

---

# 79. False Citation Commit 比保守 Unresolved 更糟

對高風險研究：

$$
\operatorname{Cost}
(
\text{False Citation Commit}
)
>
\operatorname{Cost}
(
\text{Conservative Unresolved}
).
$$

因此平台可以追蹤：

$$
\boxed{
\operatorname{FalseCommitRate}.
}
$$

---

# 80. Citation Removal 也要有歷史

如果 citation 被發現錯誤：

```text
MISATTRIBUTED
```

修訂版可以移除。

但歷史 manifest 應保存：

```text
removed citation
reason
affected claim
replacement source
revision
```

不能讓錯誤引用從紀錄中無痕消失。

---

# 81. Source Manifest

每篇 preprint 可保存：

```yaml
source_manifest:
  - source_id:
    kind:
    identifiers:
    reality_state:
    access_state:
    version:
    retrieved_at:
    content_hash:
    license:
    locators:
    update_state:
    provider_provenance:
```

---

# 82. Citation Manifest

```yaml
citation_manifest:
  - citation_id:
    claim_id:
    source_id:
    relation:
    source_span:
    semantic_support:
    conditions:
    verification_state:
    verified_at:
    verifier:
    stale: false
```

---

# 83. Data Manifest

```yaml
data_manifest:
  datasets:
    - dataset_id:
      source_id:
      version:
      snapshot_hash:
      retrieval:
      license:

  transformations:
    - transformation_id:
      inputs:
      operation:
      parameters:
      code_ref:
      environment:
      outputs:
      output_hash:
```

---

# 84. Search Audit Manifest

```yaml
search_audit:
  session_id:
  started_at:
  cutoff:
  providers:
  queries:
  selected_results:
  rejected_results:
  limitations:
  novelty_scope:
```

---

# 85. Source Reality Public UI

一般讀者不需要看到全部 graph。

UI 可以顯示：

```text
Source: Verified primary source
Support: Direct, conditional
Version: v2
Last checked: 2026-09-03
Status: Current
```

或：

```text
Source: Historically verified
Access: Archived copy only
Support: Direct
Last checked: 2026-09-03
```

---

# 86. Retracted Source UI

例如：

```text
⚠ Upstream source retracted
Claim status: Revalidation in progress
Other independent evidence: 2
```

比直接把整篇 paper 打成：

```text
FALSE
```

更合理。

---

# 87. Source Unavailable UI

例如：

```text
Source identity: Verified
Content access: Currently unavailable
Prior snapshot: Available
Claim support: Previously verified against snapshot v1
Recheck status: Pending
```

這能保留歷史 truthfulness。

---

# 88. Private Evidence

某些研究使用：

- 未公開企業資料；
- 個資；
- 私人實驗；
- confidential records。

平台可以保存：

```text
existence: ATTESTED
identity: RESTRICTED
contents: PRIVATE
independent audit: OPTIONAL/REQUIRED
```

而不將其錯標為：

```text
NO_EVIDENCE
```

Paper 06 將處理 disclosure policy。

---

# 89. Evidence Transparency 不等於全量鏡像外部資料

對 public evidence，平台可以保存：

- identifier；
- locator；
- source state；
- hash；
- minimal excerpt；
- provenance。

不必將所有外部 paper / dataset 全量複製。

這同時降低：

- copyright；
- storage；
- privacy；
- stale mirror；

風險。

---

# 90. Canonical Source 與 External Source 分離

Unbounded Axiom 自己的論文 source 可以是 canonical UTF-8 Markdown。

外部 citation source 仍遵守其原 publication system。

因此：

$$
\boxed{
\text{UA Canonical Source}
\neq
\text{External Evidence Source}.
}
$$

兩者由 provenance edge 連接。

---

# 91. Research Memory 不是 Scholarly Source

AI 長期記憶可以提醒：

> 我記得某研究可能存在。

但：

$$
\boxed{
\text{Memory Recall}
\neq
\text{External Evidence}.
}
$$

正如既有 memory research 所指出：

$$
\text{retrieval relevance}
\neq
\text{evidential validity}.
$$

因此 memory 應觸發 source search，而不是直接成為 citation。

---

# 92. Model Output 也不是 External Source

AI 可以產生推論。

若該推論本身是研究貢獻，可以保存：

```text
MODEL_INFERENCE
```

但不應偽裝成：

```text
PRIMARY_SOURCE
```

---

# 93. AI 自主研究的 Citation Workflow

完整流程：

$$
\boxed{
\begin{aligned}
\text{Claim Need}
&\rightarrow
\text{Search}\\
&\rightarrow
\text{Candidate Discovery}\\
&\rightarrow
\text{Identity Verification}\\
&\rightarrow
\text{Source Access}\\
&\rightarrow
\text{Exact Localization}\\
&\rightarrow
\text{Relation Classification}\\
&\rightarrow
\text{Semantic Support}\\
&\rightarrow
\text{Domain/Hypothesis Check}\\
&\rightarrow
\text{Citation Commit}.
\end{aligned}
}
$$

---

# 94. Data Workflow

$$
\boxed{
\begin{aligned}
\text{Data Need}
&\rightarrow
\text{Source Resolution}\\
&\rightarrow
\text{Dataset Snapshot}\\
&\rightarrow
\text{Integrity Check}\\
&\rightarrow
\text{Transformation}\\
&\rightarrow
\text{Derived Artifact}\\
&\rightarrow
\text{Claim Link}\\
&\rightarrow
\text{Replay}.
\end{aligned}
}
$$

---

# 95. AI 不必每次都重新搜尋所有來源

平台可以 cache：

```text
bibliographic identity
source snapshot
source status
validated span
relation state
```

但 cache 必須有：

```text
checked_at
ttl / freshness policy
source version
status provider
```

---

# 96. Freshness Policy

不同 source 更新速度不同。

例如：

- mathematical theorem paper：低頻；
- law / policy：高頻；
- live economic API：高頻；
- historical manuscript：低頻；
- software repository：中高頻。

因此：

$$
\boxed{
\text{Freshness Policy}
=
f(\text{Source Kind}).
}
$$

---

# 97. Stale 不等於 False

如果 source verification 已超過 freshness threshold：

```text
STALE
```

只表示：

> 需要重新確認。

不是：

> 來源已錯。

---

# 98. Source Recheck Trigger

可以由：

```text
time
provider update
new version
Crossmark event
repository change
author correction
user report
AI inconsistency detection
downstream dispute
```

觸發。

---

# 99. Interoperability Mapping

SREPA 可以映射：

- W3C PROV；
- DataCite；
- Crossref / Crossmark；
- ORCID；
- RAiD；
- SWHID；
- arXiv；
- repository identifiers；
- domain-specific identifiers。

但 canonical SREPA 不應被任何單一 provider 綁死。

---

# 100. Provider Independence

定義：

$$
\boxed{
\text{SREPA Canonical State}
\neq
\text{Provider API Response}.
}
$$

provider response 是 evidence。

canonical state 是經過 mapping、validation 與 provenance 後的 research infrastructure object。

---

# 101. Source Identity Merge 必須保守

同一 paper 可能有：

- arXiv version；
- conference version；
- journal version；
- author manuscript；
- publisher version。

平台不能只因 title 類似就全部 merge。

應保存：

```text
same-work
is-version-of
is-preprint-of
is-published-version-of
is-translation-of
is-supplement-to
```

---

# 102. Work Identity 與 Edition Identity

可表示：

$$
W
\rightarrow
\{
V_1,V_2,\ldots,V_n
\}.
$$

citation edge 應指向實際使用版本：

$$
c
\leftarrow
V_k,
$$

而不是模糊指向整個 work family。

---

# 103. DataCite Relation Metadata 的角色

DataCite 4.7 持續擴充 related identifier relation semantics。

Unbounded Axiom 可以利用外部 relation metadata，但仍保留自己的：

```text
claim dependency
data lineage
semantic support
retraction propagation
```

等更細 scholarly graph。

---

# 104. Version-aware Citation Display

讀者可以看到：

> Cited version: arXiv v2  
> Current version: journal v1  
> Relationship: published-version-of  
> Citation revalidated: yes/no

這會降低 version drift。

---

# 105. Claim-Level Source Health

每個 material claim 可以有：

```text
healthy
stale
degraded
revalidation-required
unsupported
disputed
```

source health 不需要等到整篇 paper 重新審查才更新。

---

# 106. Paper-Level Source Health 只是 Projection

例如：

```text
42 material claims
39 source-healthy
2 stale
1 revalidation-required
```

比：

```text
citation quality: 93%
```

更透明。

---

# 107. Source Reality 與 Novelty

Novelty search 也依賴 source reality。

AI 說：

> 沒找到先前工作。

只能表達：

```text
novelty_search_scope
providers
cutoff
languages
queries
coverage
```

因此：

$$
\boxed{
\text{Search Novelty}
\neq
\text{Universal Novelty}.
}
$$

---

# 108. Possible Prior Art

如果 AI 找到：

```text
可能相關但無法取得全文
```

應標記：

```text
POSSIBLE_PRIOR_ART
```

而不是：

```text
NO_PRIOR_ART
```

---

# 109. Citation Quality 不等於 Citation Quantity

平台不應鼓勵：

$$
N_{\mathrm{citations}}
\uparrow
$$

作為品質代理。

更有意義的是：

```text
material-claim coverage
primary-source coverage
false-commit rate
stale-edge rate
unresolved rate
exact-localization rate
support-validation rate
```

---

# 110. Data Provenance Quality Metric

可衡量：

```text
snapshot completeness
transformation replayability
environment capture
unit traceability
missing-data traceability
figure-to-data traceability
```

而不是只問：

> 有沒有附 CSV？

---

# 111. Failure Modes

SREPA 最常見 failure：

```text
citation fabricated
bibliographic identity mismatch
search snippet promoted to source
wrong version
wrong source span
semantic misattribution
domain mismatch
hypothesis mismatch
dead URL misread as nonexistent source
archived copy confused with current version
secondary source promoted to primary
derived value without transformation chain
figure detached from data
retracted source not propagated
provider multiplicity confused with source independence
private evidence treated as missing
model memory treated as external evidence
```

---

# 112. SREPA Minimum Invariants

## Invariant 1

$$
\boxed{
\text{Search Result}
\neq
\text{Source}.
}
$$

## Invariant 2

$$
\boxed{
\text{Source}
\neq
\text{Evidence}.
}
$$

## Invariant 3

$$
\boxed{
\text{Evidence}
\neq
\text{Support}.
}
$$

## Invariant 4

$$
\boxed{
\text{Source Exists}
\not\Rightarrow
\text{Claim Supported}.
}
$$

## Invariant 5

$$
\boxed{
\text{Access}
\neq
\text{Existence}.
}
$$

## Invariant 6

$$
\boxed{
\text{Current Availability}
\neq
\text{Historical Existence}.
}
$$

## Invariant 7

$$
\boxed{
\text{Source Identity}
\neq
\text{Source Localization}.
}
$$

## Invariant 8

$$
\boxed{
\text{Provider Multiplicity}
\neq
\text{Source Independence}.
}
$$

## Invariant 9

$$
\boxed{
\text{Data Source}
\neq
\text{Derived Value Provenance}.
}
$$

## Invariant 10

$$
\boxed{
\text{Upstream Retraction}
\Rightarrow
\text{Downstream Re-evaluation}.
}
$$

## Invariant 11

$$
\boxed{
\text{Upstream Retraction}
\not\Rightarrow
\text{Automatic Downstream Falsity}.
}
$$

## Invariant 12

$$
\boxed{
\text{No layer self-certifies another layer}.
}
$$

---

# 113. 與 Paper 03 CECA 的正式接口

Paper 03 定義：

$$
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
$$

SREPA 主要提供其中：

- $x$：evidence/source existence & integrity；
- $\ell$：claim linkage；
- $r$ 的部分 replay provenance；
- $i$ 的 source-independence evidence；
- source update information；
- data transformation lineage。

因此：

$$
\boxed{
\text{SREPA}
\text{ does not replace CECA;}
}
$$

它是 CECA 的外部 evidence grounding layer。

---

# 114. 與 Paper 05 AI Identity 的接口

citation verifier、source auditor、data transformer 都可能是具名 AI。

因此 provenance 必須保存：

```text
actor
runtime
model
tool
time
version
```

但 source validity 不能因 actor 有名或模型強大而自動提升。

---

# 115. 與 Paper 06 Privacy 的接口

source / data 可以：

```text
PUBLIC
SUMMARY
ATTESTED
RESTRICTED
PRIVATE
```

SREPA 必須能保存：

> source 存在，但內容受限。

而不是強迫：

> 要嘛公開，要嘛視為不存在。

---

# 116. 與 Paper 08 Canonical Source 的接口

Unbounded Axiom 自己的 preprint：

$$
\text{UTF-8 canonical source}
$$

會讓 source localization 更穩定。

例如 claim、definition、equation、citation 都可有 stable object ID。

因此平台內部引用甚至可以做到：

$$
\text{Paper A / Claim 17}
\rightarrow
\text{Paper B / Theorem 3}.
$$

---

# 117. 與 Paper 09 AI Preprocessing 的接口

AI preprocessing 可以協助：

- citation parsing；
- DOI normalization；
- source candidate search；
- source span suggestion；
- data lineage extraction；
- malformed reference repair。

但：

$$
\boxed{
\text{AI Repair}
\neq
\text{Source Verification Authority}.
}
$$

---

# 118. 最小 Submission Requirement

對一般 preprint，不一定要求作者手動建立完整 SREPA graph。

但 material claim 應至少提供：

```text
source reference
source type
citation relation
data source if applicable
known limitations
```

平台可以自動：

$$
\text{extract}
\rightarrow
\text{resolve}
\rightarrow
\text{validate}
\rightarrow
\text{ask for correction}.
$$

---

# 119. 無 AI 模式也必須可發表

如果投稿者不使用平台 AI：

```text
manual source references
manual data manifest
```

只要 schema 合法，仍可提交。

AI source verification 是服務與 validation layer，不應變成研究發表的付費門檻。

---

# 120. Source Audit 可以延後完成

preprint 可以先是：

```text
PUBLIC_PREPRINT
+
SOURCE_AUDIT_PENDING
```

但 UI 必須清楚。

不能將「尚未驗證」渲染成「已驗證」。

---

# 121. Source Audit Update 不應改寫作者原文

如果 platform auditor 發現：

```text
citation does not support claim
```

應建立：

```text
audit finding
```

與作者 revision opportunity。

不能靜默把作者句子改掉。

---

# 122. Audit 與 Authorship 分離

platform source auditor 不因修改 metadata 就自動成為 paper author。

這將與 Paper 05 contribution roles 結合。

---

# 123. Research Negative Source Results

以下也應保存：

```text
PRIMARY_SOURCE_NOT_FOUND
SOURCE_CONFLICT
ARCHIVE_ONLY
NO_ACCESS
VERSION_UNRESOLVED
SUPPORT_NOT_ESTABLISHED
POSSIBLE_PRIOR_ART
```

這能防止下一個 AI 重跑同樣失敗搜尋。

---

# 124. Failed Search 也有 Provenance

例如：

> 搜了 8 個 provider，沒有找到 primary source。

保存：

```text
queries
providers
cutoff
failures
rate limits
access restrictions
```

下一個 AI 才知道：

> 這不是完全沒搜，而是在某個 search boundary 內沒找到。

---

# 125. Research Ecology 的 Source Memory

經驗可以累積：

```text
source aliases
moved URLs
version mappings
known retractions
known bad mirrors
publisher patterns
dataset update schedules
```

但這些 memory 仍需重新驗證其 freshness。

---

# 126. Source Health Monitor

未來平台可以定期：

```text
check DOI
check Crossmark
check URL
check repository commit
check dataset version
check publisher update
```

並只在 state change 時產生事件。

---

# 127. Event-Driven Revalidation

例如：

$$
\texttt{RETRACTED}(s)
$$

觸發：

$$
\texttt{REVALIDATE}
(
\operatorname{Downstream}(s)
).
$$

這比定期重跑所有 citation 成本低。

---

# 128. AI Source Auditor

可設角色：

```text
Retriever Agent
Bibliographic Auditor
Source Locator
Semantic Support Auditor
Domain/Hypothesis Mapper
Data Provenance Auditor
Adversarial Source Auditor
Citation Committer
```

Citation Committer 只讀 validation state，不自行降低 gate。

---

# 129. 多 AI 不使用 Majority Vote 決定 Source Truth

如果三個 AI 都說：

> 支持。

但 source span 沒定位：

仍然不能 PASS。

因此：

$$
\boxed{
V_e
=
F(
\text{source state},
\text{evidence},
\text{validation}
),
}
$$

而不是：

$$
V_e
=
\operatorname{majorityVote}
(
AI_1,AI_2,AI_3
).
$$

---

# 130. Source Reality Layer 的真正價值

它不是：

> 幫文章自動補很多 reference。

而是建立：

$$
\boxed{
\text{Claim}
\leftrightarrow
\text{Exact Source}
\leftrightarrow
\text{Evidence Relation}
\leftrightarrow
\text{Version}
\leftrightarrow
\text{Provenance}.
}
$$

---

# 131. 從 Bibliography 到 Scholarly Dependency Graph

傳統 bibliography：

```text
[1]
[2]
[3]
...
```

未來：

$$
G_{\mathrm{scholar}}
=
(
V_{\mathrm{claim}}
\cup
V_{\mathrm{source}}
\cup
V_{\mathrm{data}}
\cup
V_{\mathrm{transform}},
E_{\mathrm{typed}}
).
$$

AI 可以回答：

- 哪些 source 是 proof-critical？
- 哪些只是背景？
- 哪些 data 經過哪個 transformation？
- 哪個 source 已 retract？
- 哪些 downstream claims 受影響？
- 哪些結論已被獨立 reproduces？
- 哪些 citation 只支持 local claim？

---

# 132. 對 Unbounded Axiom 的實作建議

v0.1 可以先做：

```text
Source Registry
Citation Edge Registry
Data Manifest
Search Audit
Source Status Updater
Dependency Graph
Source Audit UI
```

不需要一開始就實現所有 domain verifier。

---

# 133. Phase 1：Identity First

先解：

```text
DOI normalization
arXiv identity
URL canonicalization
version
source hash
retrieval timestamp
```

---

# 134. Phase 2：Localization

加入：

```text
section
page
paragraph
table
theorem
dataset row
code line
```

---

# 135. Phase 3：Semantic Support

讓 AI / rule engine 判定：

```text
context
support
dependency
contrast
misattribution
```

並保留 uncertainty。

---

# 136. Phase 4：Data Provenance

加入：

```text
dataset snapshot
transformation receipt
derived value
figure lineage
replay
```

---

# 137. Phase 5：Status Monitoring

接：

```text
Crossmark
DataCite
Crossref
repository update
official status
```

觸發 revalidation。

---

# 138. Phase 6：Graph-Level Research Maintenance

最後做到：

$$
\text{upstream update}
\rightarrow
\text{downstream claim state maintenance}.
$$

這時平台才真正像「活的研究紀錄」。

---

# 139. SREPA 與外部標準的關係

本文不主張建立完全封閉的新標準。

SREPA 應：

- 用 DOI、DataCite、Crossref 等識別外部 scholarly resources；
- 用 Crossmark 等取得 publisher status；
- 用 W3C PROV 表達一般 provenance；
- 遵循 FAIR 對 persistent identifiers、metadata、qualified references 與 provenance 的思想；
- 用 Unbounded Axiom extension 表達 claim-level support、citation legitimacy 與 research dependency propagation。

因此：

$$
\boxed{
\text{Reuse standards where possible;}
\quad
\text{extend only where research semantics require}.
}
$$

---

# 140. 最終原則：可追溯比引用數重要

AI-native research 不需要比人類論文塞更多 references。

它需要：

> 每個重要 claim 的 evidence path 可以被重新走一遍。

因此：

$$
\boxed{
\text{Can another intelligence follow the pointer and recover the evidence?}
}
$$

是 citation infrastructure 最重要的問題之一。

如果答案是：

```text
yes
```

則 citation 真正成為 research infrastructure。

如果答案是：

```text
no
```

那 references list 再長，也只是 scholarly decoration。

---

# 141. 結論

本文提出 SREPA：

$$
\boxed{
\mathcal S
=
(
O,
R,
A,
V,
L,
E,
P,
T,
G
).
}
$$

它將來源 identity、現實狀態、可存取性、版本、精確定位、證據關係、provenance、時間與 dependency graph 分離。

其最核心公式是：

$$
\boxed{
\text{Search Result}
\neq
\text{Source}
\neq
\text{Evidence}
\neq
\text{Support}.
}
$$

對數據則是：

$$
\boxed{
\text{Claim}
\leftarrow
\text{Derived Value}
\leftarrow
\text{Transformation}
\leftarrow
\text{Dataset Snapshot}
\leftarrow
\text{Primary Source}.
}
$$

對 scholarly updates：

$$
\boxed{
\text{Upstream Status Change}
\rightarrow
\text{Downstream Re-evaluation}.
}
$$

但：

$$
\boxed{
\text{Upstream Retraction}
\not\Rightarrow
\text{Automatic Downstream Falsity}.
}
$$

這使 Unbounded Axiom 未來可以把 bibliography 從文章尾端的文字列表，提升成真正可供人類與 AI 共同追蹤的 scholarly dependency graph。

這也完成前三篇到第四篇的基本閉環：

$$
\boxed{
\begin{aligned}
&\text{Paper 02: What kind of research is this?}\\
&\text{Paper 03: How strongly is the claim supported?}\\
&\text{Paper 04: Where does the support actually come from?}
\end{aligned}
}
$$

下一篇將處理另一個不能再只用模型名稱代替的問題：

$$
\boxed{
\text{Who actually did the research?}
}
$$

也就是 **Paper 05 — Named AI Researcher Identity and Lineage**：具名 AI、persistent identity、model migration、fork、multi-agent lineage、authorship、contribution，以及「研究者身份」與「底層模型／session／runtime」的正式分離。

---

# 參考資料

1. Crossref. **Crossmark.**  
   https://www.crossref.org/services/crossmark/  
   Accessed 2026-09-03.

2. Crossref Support. **Crossmark — Registering Updates.**  
   https://support.crossref.org/hc/en-us/articles/115000501246-Crossmark-registering-updates  
   Accessed 2026-09-03.

3. DataCite Metadata Working Group. **DataCite Metadata Schema Documentation for the Publication and Citation of Research Data and Other Research Outputs, Version 4.7.** DataCite e.V., released 2026-03-03. DOI: 10.14454/qdd3-ps68.  
   https://schema.datacite.org/meta/kernel-4/

4. DataCite. **Get Started With Schema 4.7.** 2026-03-05. DOI: 10.5438/s00r-vp07.  
   https://datacite.org/blog/get-started-with-schema-4-7/

5. W3C. **PROV-O: The PROV Ontology.** W3C Recommendation, 2013.  
   https://www.w3.org/TR/prov-o/

6. Groth, P., Moreau, L. **PROV-Overview: An Overview of the PROV Family of Documents.** W3C, 2013.  
   https://www.w3.org/TR/prov-overview/

7. Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. **The FAIR Guiding Principles for scientific data management and stewardship.** Scientific Data 3, 160018 (2016). DOI: 10.1038/sdata.2016.18.

8. Priem, J., Piwowar, H., Orr, R. **OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts.** arXiv:2205.01833, 2022.

9. Kinney, R., Anastasiades, C., Authur, R., et al. **The Semantic Scholar Open Data Platform.** arXiv:2301.10140, 2023.

10. Wadden, D., Lin, S., Lo, K., et al. **Fact or Fiction: Verifying Scientific Claims.** EMNLP 2020. DOI: 10.18653/v1/2020.emnlp-main.609.

11. Wadden, D., Lo, K., Wang, L. L., Cohan, A., Beltagy, I., Hajishirzi, H. **MultiVerS: Improving scientific claim verification with weak supervision and full-document context.** Findings of NAACL 2022, 61–76. DOI: 10.18653/v1/2022.findings-naacl.6.

12. EveMissLab. **Mathematical Citation Compiler and Citation-Validation Closure / FCVP Architecture.** Research architecture document, 2026.

13. EveMissLab. **FCVP / FELRA Citation Validation Prototype v0.3.** Executable citation dependency auditing prototype, 2026.

14. EveMissLab. **Diligent AI Political / Economic Intelligence Runtime v0.1.** Evidence citation, search audit and reproducibility architecture, 2026.

15. EveMissLab. **SSSP GitHub Update Handoff v1.3.** Canonical scholarly source, immutable snapshot and provenance architecture, 2026.

16. Neo.K, Aletheia / GPT-5.6 Sol. **主張不等於證據：AI 原生 Claim Strength、Evidence State 與可修正條件.** AI-Native Preprint Commons Series, Paper 03, 2026-09-03.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 將 MCC/CVC/FCVP theorem-level citation validation 一般化為 SREPA；建立 Source Reality State、Access State、version-aware localization、typed citation relations、search audit、data lineage、transformation receipt、source update/retraction propagation、source health 與 interoperable provenance layer。 |
