# AI-Native Unified Search Intelligence (AUSI) Series — Paper 05

## 從搜尋結果到證據：Provenance、Verification、Evidence Ledger 與可驗證研究資料生命週期

**English Title:** *From Search Results to Evidence: Provenance, Verification, Evidence Ledgers, and the Lifecycle of Verifiable Research Data*

**Version:** v0.1  
**Date:** 2026-08-31  
**Status:** Canonical Draft  
**Series:** AI-Native Unified Search Intelligence (AUSI)  
**Predecessor:** Paper 04 — *合法資料取得與來源治理：AI 搜尋中的授權、條款、資料權利與 Policy-Constrained Acquisition*  
**Reference Implementation Direction:** `ai-web-research`

---

## 摘要

搜尋系統通常以 ranked results 作為終點，但研究型 AI 不能把「被搜尋到」直接等同於「可作為證據」。搜尋結果可能只是摘要頁、轉載、搜尋引擎 snippet、已過期資料、錯誤版本、第三方重述、缺乏來源的模型回憶，或與待證命題只有主題相關而沒有實際支持關係。即使存在引用連結，也不能由「引用存在」推出「引用內容支持該 claim」。因此，AI 原生搜尋若要支援科學研究、經濟資料、氣象資料、專利檢索與企業 research，需要一個獨立於 retrieval ranking 的 evidence lifecycle。

本文提出 **AUSI Evidence Lifecycle（AEL）** 與 **Evidence Ledger**。核心流程為：

$$
\text{Search Result}
\rightarrow
\text{Candidate Evidence}
\rightarrow
\text{Anchored Evidence}
\rightarrow
\text{Verified Evidence}
\rightarrow
\text{Claim–Evidence Relation}
\rightarrow
\text{Evidence Ledger}
$$

本文以 W3C PROV 的 Entity–Activity–Agent 與 derivation 模型、FORCE11 Data Citation Principles 的 persistent identification、specificity、verifiability、provenance 與 fixity 要求，以及 nanopublication 的 assertion / provenance / publication-info 分離為既有基礎，不重新發明 provenance 標準；本文的貢獻是將這些思想嵌入 AI Search Planner 與 Search Receipt 之間，建立可被機器執行的 evidence state machine。

本文區分 source identity、document identity、manifestation identity、version identity、content identity 與 claim identity；提出 Evidence Object、Evidence Anchor、Transformation Provenance、Temporal Identity、Source Independence Graph、Claim–Evidence Graph 與 Evidence Quality Vector。Evidence verification 被拆成 source verification、identity verification、fixity verification、anchor verification、temporal verification、semantic support verification、independence verification 與 corroboration / contradiction analysis。本文主張 evidence quality 不應壓縮成單一 confidence scalar，因為來源權威性、內容完整性、時間適配性、獨立性、直接性與可重現性是不同維度。

本文進一步提出 append-only Evidence Ledger：新的驗證、撤回、版本替換或 contradiction 不覆寫舊紀錄，而以新的 ledger event 改變其有效狀態。Ledger 不等同 blockchain，也不要求分散式共識；其核心要求是 auditability、lineage、fixity、versionability 與可重建性。Paper 04 的 Usage Envelope 必須與 Evidence Object 一起保存，使「可證明」與「可合法再利用」不被混為一談。

最後，本文以經濟數據 revision、氣象 station observation、專利 family / priority / claim mapping，以及學術文獻 citation chain 為例，說明相同 Evidence Runtime 如何跨 domain 使用。此框架為後續 Paper 06 的反證優先與缺口驅動搜尋提供必要狀態：只有當系統知道自己已有哪些證據、證據彼此是否獨立、哪些命題仍缺乏支持或反證，AI 才能根據 evidence gap 決定下一步搜尋。

**關鍵詞：** Evidence Ledger、Provenance、Verification、Data Citation、W3C PROV、Nanopublication、Claim–Evidence Graph、Source Independence、Fixity、Versioning、AI-Native Search、Reproducibility

---

# 1. 問題：搜尋結果不是證據

傳統搜尋系統的輸出通常為：

$$
R
=
\{r_1,r_2,\ldots,r_n\}
$$

其中每個 $r_i$ 可以是：

- URL；
- document；
- snippet；
- database row；
- API record；
- semantic hit；
- citation node；
- search-engine result。

但：

$$
\boxed{
r_i\in R
\not\Rightarrow
r_i\in E_{\text{verified}}
}
$$

原因很簡單：

搜尋系統解決的是：

> 哪些候選與 query / task 有關？

證據系統則必須回答：

> 這個具體來源中的哪個具體內容，在哪個版本與時間條件下，以什麼關係支持、反駁或限制哪一個具體 claim？

這是不同問題。

---

# 2. 「被引用」也不等於「支持」

研究型 AI 很容易產生另一種錯誤：

$$
\text{Citation Exists}
\Rightarrow
\text{Claim Supported}
$$

這個推論不成立。

一個來源可能：

- 只與主題相關；
- 支持更弱的命題；
- 支持相反結論；
- 只描述方法；
- 是二手引用；
- 引用的是不同版本；
- 只在特定條件下成立；
- 已被更新、修正或撤回。

因此，引用至少需要兩層關係：

$$
\operatorname{Cites}(c,s)
$$

與：

$$
\operatorname{Supports}(s,c)
$$

兩者不同。

---

# 3. 既有 provenance 研究已提供成熟地基

W3C PROV 已將 provenance 建模為：

- `prov:Entity`；
- `prov:Activity`；
- `prov:Agent`；

並提供：

- `wasGeneratedBy`；
- `used`；
- `wasDerivedFrom`；
- `wasAttributedTo`；
- `wasAssociatedWith`；

等 provenance relations。

因此，本文不需要重新發明「資料是怎麼產生的」基本詞彙。

AUSI 需要做的是：

> 將 provenance 模型與 AI 搜尋、資料取得、驗證、claim linking 與 Search Receipt 接起來。

---

# 4. Data Citation 已經要求 Specificity 與 Verifiability

FORCE11 的 Joint Declaration of Data Citation Principles 明確提出：

- data 是可被正式引用的 research object；
- claim 依賴 data 時，應引用對應 data；
- citation 應使用持久且 machine-actionable identity；
- citation 應支援 access；
- metadata 應持續存在；
- citation 應能識別支撐 claim 的具體資料；
- provenance 與 fixity 應足以驗證 version / timeslice / granular portion。

因此：

$$
\boxed{
\text{Evidence Citation}
\neq
\text{Homepage URL}
}
$$

若一個 claim 依賴某資料集第 2026-08-01 版中的某一 series 與 observation range，僅引用資料平台首頁是不夠的。

---

# 5. FAIR 不只要求 Findable

FAIR Principles 強調：

$$
F+A+I+R
$$

其中 reusable data 需要 rich metadata、provenance 與明確使用條件。

這與 Paper 04 的 Source Rights / Usage Envelope 可直接接軌。

一個 evidence object 若：

- 找得到；
- 但版本不明；
- provenance 不明；
- license 不明；
- transformation 不明；

就仍不足以支撐高品質 autonomous research。

---

# 6. Nanopublication 提供 claim-level 結構參照

Nanopublication 將一個小型知識單位拆為：

1. assertion；
2. assertion provenance；
3. publication information。

這個模型與 AUSI 很接近，但用途不同。

AUSI 不要求所有 evidence 都發布成 nanopublication；而是借用其核心區分：

$$
\text{Claim Content}
\neq
\text{Claim Provenance}
\neq
\text{Publication Metadata}
$$

這對 Claim–Evidence Graph 很重要。

---

# 7. Evidence Lifecycle

本文提出：

$$
\boxed{
R
\rightarrow
E_c
\rightarrow
E_a
\rightarrow
E_v
\rightarrow
G_{CE}
\rightarrow
L_E
}
$$

其中：

- $R$：Search Results；
- $E_c$：Candidate Evidence；
- $E_a$：Anchored Evidence；
- $E_v$：Verified Evidence；
- $G_{CE}$：Claim–Evidence Graph；
- $L_E$：Evidence Ledger。

不是每一個 candidate 都會進入 Verified Evidence。

---

# 8. Candidate Evidence

定義：

$$
e_c
=
(
s,
o,
m,
t_r
)
$$

其中：

- $s$：source reference；
- $o$：retrieved observation / content；
- $m$：Search Method / acquisition method；
- $t_r$：retrieval time。

Candidate Evidence 表示：

> 這個內容值得進一步檢查。

它不表示內容已正確、已固定、已支持 claim 或已獨立佐證。

---

# 9. Anchored Evidence

Candidate 經過具體定位後形成 Anchored Evidence：

$$
e_a
=
(
e_c,
A_e
)
$$

其中 Evidence Anchor：

$$
A_e
=
(
I_d,
I_v,
L,
H_a
)
$$

包含：

- $I_d$：document identity；
- $I_v$：version / manifestation identity；
- $L$：location selector；
- $H_a$：anchored content hash。

目標是回答：

> 「你說的是哪一段？」

---

# 10. Evidence Anchor 不能只有 URL

動態網頁中：

$$
URL_{t_1}
=
URL_{t_2}
$$

並不代表：

$$
Content_{t_1}
=
Content_{t_2}
$$

因此 Anchor 可以依資料類型使用：

```text
URL + retrieval_time
URL + content_hash
DOI + version
page + paragraph
character offsets
XPath / CSS selector
JSONPath
database primary key
dataset + series + observation range
patent publication + claim number
git commit + file + line range
content-addressed identifier
```

這些可以組合，而不是單選。

---

# 11. Source Identity

來源不是 URL 字串。

定義 Source Identity：

$$
I_s
=
(
\text{publisher},
\text{origin},
\text{surface},
\text{authority context}
)
$$

例如同一新聞：

```text
press release
↓
newswire
↓
newspaper A
↓
blog B
```

雖然有四個 URL，但 evidence ancestry 可能只有一個 primary origin。

因此：

$$
\#URL
\neq
\#IndependentSource
$$

---

# 12. Document Identity

同一 intellectual work 可以有：

- preprint；
- accepted manuscript；
- published version；
- corrected version；
- HTML manifestation；
- PDF manifestation；
- mirror；
- translated copy。

因此：

$$
I_{\text{work}}
\neq
I_{\text{manifestation}}
$$

Evidence Runtime 應盡可能分開：

```text
work_id
edition/version_id
manifestation_id
retrieved_copy_id
```

---

# 13. Content Identity 與 Fixity

Evidence Object 應保存：

$$
H(d)
$$

例如 cryptographic hash。

Hash 的目的不是：

> 證明內容真實。

而是：

> 驗證當前內容是否與當時保存／引用的內容一致。

因此：

$$
\operatorname{HashMatch}
\Rightarrow
\operatorname{Fixity}
$$

但：

$$
\operatorname{Fixity}
\not\Rightarrow
\operatorname{Truth}
$$

---

# 14. Version Identity

資料 revision 是研究型 AI 的核心問題。

定義：

$$
V(d)
=
(
v,
t_e,
t_p,
t_r
)
$$

其中：

- $v$：version / revision identifier；
- $t_e$：effective / event time；
- $t_p$：publication time；
- $t_r$：retrieval time。

若 provider 無正式 version，可以使用：

$$
(\text{retrieval time},\text{content hash})
$$

作為 operational snapshot identity。

---

# 15. 四種時間不能混為一談

本文至少區分：

$$
t_{\text{event}}
$$

事件或觀測實際發生時間。

$$
t_{\text{publication}}
$$

資料／文件被發布時間。

$$
t_{\text{revision}}
$$

資料被修訂時間。

$$
t_{\text{retrieval}}
$$

AI 實際取得時間。

例如：

> 2025 Q4 GDP

可能在 2026 年多次 revision。

因此「2025 Q4」不是完整 temporal identity。

---

# 16. Evidence Object

本文提出最小：

```text
EvidenceObject
├── evidence_id
├── source_identity
├── work_identity
├── version_identity
├── manifestation_identity
├── retrieval_identity
├── anchor
├── raw_content_ref
├── normalized_content
├── content_hash
├── temporal_identity
├── acquisition_provenance
├── transformation_provenance
├── policy_usage_envelope
├── verification_state
├── evidence_role
├── quality_vector
├── independence_group
└── ledger_refs
```

這不是所有欄位都必須填滿。

缺失必須是 explicit missing state。

---

# 17. Evidence Role

同一 evidence 可以扮演不同角色。

定義：

$$
R_E
\in
\{
\text{support},
\text{contradict},
\text{qualify},
\text{context},
\text{method},
\text{definition},
\text{version},
\text{identity},
\text{provenance}
\}
$$

這比「citation=true」有更多資訊。

---

# 18. Claim Atomization

長篇答案中的一句話可能包含多個 factual propositions。

例如：

> 「某 API 自 2026 年起要求登入，而且每天最多允許 10,000 次請求。」

這至少包含兩個 claims：

$$
c_1=\text{authentication requirement}
$$

$$
c_2=\text{daily request limit}
$$

若只用一個 citation 覆蓋整句，可能只有 $c_1$ 被來源支持。

因此可以將可驗證內容拆為 Atomic Claims：

$$
C
=
\{c_1,\ldots,c_n\}
$$

FActScore 等 fine-grained factuality work 已顯示 atomic fact decomposition 對長文事實評估具有價值；AUSI 將類似思想用於 evidence mapping，而不是只做 final-answer score。

---

# 19. Claim Object

最小 Claim Object：

```text
ClaimObject
├── claim_id
├── proposition
├── scope
├── qualifiers
├── temporal_scope
├── jurisdiction_scope
├── entity_refs
├── claim_type
├── importance
└── verification_requirement
```

尤其 `scope` 與 `qualifiers` 不能省略。

---

# 20. Claim–Evidence Graph

定義：

$$
G_{CE}
=
(
C,
E,
R
)
$$

其中：

- $C$：claims；
- $E$：evidence objects；
- $R$：claim–evidence relations。

relation 可以包括：

$$
R
=
\{
\operatorname{supports},
\operatorname{contradicts},
\operatorname{qualifies},
\operatorname{defines},
\operatorname{derives},
\operatorname{duplicates}
\}
$$

這使 verification 從 document-level 進入 claim-level。

---

# 21. Support 不是 Boolean 真理證明

即使：

$$
\operatorname{Supports}(e,c)=1
$$

也不表示：

$$
c=\text{True}
$$

它表示：

> 在指定 interpretation / scope 下， $e$ 為 $c$ 提供支持。

因此更完整：

$$
\operatorname{Supports}
(
e,c,
q,
\sigma
)
$$

其中：

- $q$：support strength / type；
- $\sigma$：scope / assumptions。

這避免把 evidence relationship 誤寫成 truth oracle。

---

# 22. Verification Pipeline

本文提出八層 verification。

## V1 — Source Verification

來源是誰？

## V2 — Identity Verification

取得的物件是否為聲稱的 document / dataset / patent / series？

## V3 — Fixity Verification

內容是否與引用版本一致？

## V4 — Anchor Verification

引用位置是否真的包含所記錄內容？

## V5 — Temporal Verification

時間／版本是否適合該 claim？

## V6 — Semantic Support Verification

內容是否真的支持 / contradict / qualify 該 claim？

## V7 — Independence Verification

多個 evidence 是否真的來自相互獨立的資訊來源？

## V8 — Cross-Evidence Verification

不同 evidence 間是否一致、衝突或版本不同？

---

# 23. Source Verification

Source Verification 可以包含：

```text
official domain
publisher identity
certificate / transport context
persistent identifier
repository identity
database record identity
publisher metadata
cross-registry resolution
```

但「官方網域」不代表內容必然正確。

它只是 source identity 的一部分。

---

# 24. Identity Verification

例如：

> CPI

可能有：

- seasonally adjusted；
- not seasonally adjusted；
- headline；
- core；
- monthly；
- annual；
- national；
- city-specific。

因此：

$$
\text{Label Match}
\not\Rightarrow
\text{Series Identity Match}
$$

Evidence Runtime 應保存正式 series ID、unit、frequency、adjustment 與 metadata。

---

# 25. Anchor Verification

對 text：

$$
\operatorname{AnchorValid}(e)
=
1
$$

要求：

- locator 可解；
- retrieved span 與 hash / selector 一致；
- 引用 text 存在於指定 version。

對 structured data：

- row / field identity 正確；
- series / date / unit 對應；
- value 與 raw record 一致。

---

# 26. Semantic Support Verification

定義：

$$
V_s(e,c)
\in
\{
\mathsf{SUPPORT},
\mathsf{CONTRADICT},
\mathsf{QUALIFY},
\mathsf{IRRELEVANT},
\mathsf{AMBIGUOUS}
\}
$$

這是比 similarity score 更重要的狀態。

一段內容可以：

$$
\operatorname{Similarity}(e,c)\gg0
$$

但：

$$
V_s(e,c)=\mathsf{CONTRADICT}
$$

---

# 27. LLM 可以做 Support Judge，但不能成為來源

AI 可以協助判斷：

$$
V_s(e,c)
$$

但 AI judge 的輸出是：

$$
\text{Verification Activity}
$$

而不是 primary evidence。

因此 ledger 應記錄：

```text
judge_model
judge_version
prompt/schema version
input evidence refs
decision
confidence
timestamp
```

並允許 deterministic / human verifier 覆蓋或複核。

---

# 28. Quote Verification 與 Entailment Verification 分離

一個引用可以：

1. quote 完全存在；
2. 但不支持 claim。

因此：

$$
\operatorname{QuoteVerified}(e)=1
$$

不推出：

$$
\operatorname{Supports}(e,c)=1
$$

兩個欄位必須分開。

這是研究型 RAG 常見錯誤的結構性解法。

---

# 29. Transformation Provenance

資料常會經過：

- parsing；
- cleaning；
- unit conversion；
- timezone conversion；
- aggregation；
- normalization；
- translation；
- summarization；
- statistical computation。

因此 final value：

$$
d_n
$$

可能由：

$$
d_0
\xrightarrow{f_1}
d_1
\xrightarrow{f_2}
\cdots
\xrightarrow{f_n}
d_n
$$

產生。

每一步應可記錄為 provenance activity。

---

# 30. Derived Evidence

Derived Evidence 不應冒充 raw evidence。

例如：

$$
\text{YoY Growth}
=
\frac{x_t-x_{t-12}}{x_{t-12}}
$$

如果 source API 沒直接提供 YoY growth，則：

```text
raw evidence = x_t, x_t-12
derived evidence = computed YoY
```

兩者不同。

Ledger 應保存 derivation。

---

# 31. Translation Evidence

若原文：

$$
d_{\text{zh}}
$$

被 AI 翻譯：

$$
d_{\text{en}}
=
f_{\text{translation}}(d_{\text{zh}})
$$

則英文句子不是新的 primary source。

Evidence identity 應保留：

$$
d_{\text{en}}
\operatorname{wasDerivedFrom}
d_{\text{zh}}
$$

並讓 verification 能回到原文。

---

# 32. Source Independence

假設取得：

$$
e_1,e_2,e_3
$$

若三者都源自：

$$
s_0
$$

則不能視為三個 independent confirmations。

定義 provenance ancestry：

$$
\operatorname{Anc}(e_i)
$$

兩個 evidence 的 independence 可以近似：

$$
I(e_i,e_j)
=
1-
\operatorname{Overlap}
(
\operatorname{Anc}(e_i),
\operatorname{Anc}(e_j)
)
$$

這不是唯一算法，但比單純 domain count 更合理。

---

# 33. Independence Group

實作上可以先建立：

```text
independence_group_id
origin_source_id
syndication_chain
citation_chain
shared_dataset_id
```

如果兩家網站都直接抄同一 press release，則：

$$
\operatorname{independence\_group}(e_1)
=
\operatorname{independence\_group}(e_2)
$$

---

# 34. Corroboration

對 claim $c$：

$$
E^+(c)
=
\{e_i\mid \operatorname{supports}(e_i,c)\}
$$

不能只計算：

$$
|E^+(c)|
$$

更合理是考慮：

$$
\operatorname{Corroboration}(c)
=
f(
\text{independent sources},
\text{directness},
\text{authority},
\text{temporal fit},
\text{method diversity}
)
$$

---

# 35. Contradiction

定義：

$$
E^-(c)
=
\{e_i\mid \operatorname{contradicts}(e_i,c)\}
$$

Contradiction 不應被系統靜默平均掉。

應產生：

```text
contradiction_event
claim_id
evidence_a
evidence_b
possible_causes
required_followup
```

可能原因包括：

- 不同版本；
- 不同時間；
- 定義不同；
- unit 不同；
- population 不同；
- source error；
- 真正學術爭議。

---

# 36. Qualification

很多 evidence 不是支持 / 反駁，而是縮小範圍。

例如：

> 「此效果只在樣本 A 中成立。」

因此：

$$
\operatorname{Qualifies}(e,c)
$$

是必要 relation。

否則 AI 容易把有限結論擴張成普遍命題。

---

# 37. Evidence Quality 不能只有 Confidence

定義 Evidence Quality Vector：

$$
\mathbf{Q}_E(e)
=
(
q_{\text{identity}},
q_{\text{fixity}},
q_{\text{authority}},
q_{\text{directness}},
q_{\text{temporal}},
q_{\text{independence}},
q_{\text{reproducibility}},
q_{\text{support}}
)
$$

其中每一維可以：

- numeric；
- ordinal；
- categorical；
- missing。

不要求全部 scalar 化。

---

# 38. Authority 與 Directness 不同

官方統計局：

$$
q_{\text{authority}}\gg0
$$

但一篇新聞報導引用統計局：

$$
q_{\text{directness}}<1
$$

如果 primary API 可取得，Planner 應優先 resolve primary evidence。

---

# 39. Reproducibility

Evidence 可重現性至少問：

```text
can source be identified?
can version be resolved?
can anchor be re-located?
can transformation be replayed?
are units/schema known?
are dependencies recorded?
```

因此：

$$
Q_{\text{repro}}
=
f(
\text{identity},
\text{version},
\text{anchor},
\text{provenance},
\text{transformation}
)
$$

---

# 40. Verification State Machine

本文提出：

```text
DISCOVERED
↓
ACQUIRED
↓
IDENTIFIED
↓
ANCHORED
↓
FIXITY_VERIFIED
↓
CONTENT_VERIFIED
↓
CLAIM_LINKED
↓
CORROBORATED / CONTESTED / QUALIFIED
```

但這不是單一路徑。

Evidence 也可能進入：

```text
FAILED_IDENTITY
ANCHOR_BROKEN
STALE
SUPERSEDED
RETRACTED
POLICY_RESTRICTED
UNVERIFIABLE
```

---

# 41. Verified Evidence 的定義

本文不把 `VERIFIED` 定義成：

> 已證明世界真相。

而定義為：

> 該 Evidence Object 的來源、身份、版本、內容定位與指定 claim relation 已達到該 task 所要求的 verification profile。

形式上：

$$
\operatorname{Verified}(e,c,T)=1
$$

若：

$$
V_T
\subseteq
V(e,c)
$$

其中 $V_T$ 是 task-required verification dimensions。

---

# 42. Task-Dependent Verification

簡單 navigation task 可能只需要：

```text
source identity
URL resolution
```

經濟報告可能要求：

```text
official source
series identity
unit
vintage
retrieval timestamp
```

專利 FTO preliminary research 可能要求：

```text
publication identity
family identity
priority
jurisdiction
legal status snapshot
claim anchor
```

因此：

$$
\text{Verification}
=
\text{Task-Relative Contract}
$$

而不是全世界唯一 threshold。

---

# 43. Evidence Ledger

本文提出：

> **Evidence Ledger 是 append-only、versioned、可追溯的 evidence state event store。**

它保存：

- evidence creation；
- verification；
- claim linking；
- corroboration；
- contradiction；
- transformation；
- supersession；
- retraction；
- policy changes；
- human review。

---

# 44. Evidence Ledger 不等同 Blockchain

Ledger 核心需求是：

$$
\text{append-only history}
+
\text{identity}
+
\text{lineage}
+
\text{auditability}
$$

不要求：

- distributed consensus；
- cryptocurrency；
- proof-of-work；
- public chain。

可以用：

- relational DB + immutable events；
- event store；
- append-only log；
- Merkleized archive；
- content-addressed store；

等方式實作。

---

# 45. Ledger Event

定義：

$$
\ell_k
=
(
id,
type,
subject,
actor,
activity,
time,
inputs,
outputs,
refs
)
$$

例如：

```text
EVIDENCE_ACQUIRED
ANCHOR_VERIFIED
SUPPORT_CONFIRMED
CONTRADICTION_FOUND
SOURCE_SUPERSEDED
HUMAN_REVIEWED
POLICY_UPDATED
```

---

# 46. 不覆寫舊證據

若原資料：

$$
d_{v1}
$$

被新版本：

$$
d_{v2}
$$

取代，不應：

```text
UPDATE evidence SET value = v2
```

而應：

```text
v1 remains recorded
v2 added
supersedes(v2, v1)
```

因為過去報告可能真的使用過 $v1$。

---

# 47. Evidence Validity Interval

Evidence 可以有：

$$
[t_{\text{valid-from}},t_{\text{valid-to}})
$$

例如：

- 某政策；
- 某 legal status；
- 某經濟 vintage；
- 某 API documentation。

這使系統能回答：

> 2026-02-01 當時我們根據的是哪個狀態？

---

# 48. Retraction / Correction

若 paper 被 retracted：

$$
\operatorname{Retracted}(e)=1
$$

不代表刪掉 evidence。

而是：

```text
original evidence remains
retraction event appended
current usability changed
dependent claims re-evaluated
```

同理 correction / erratum。

---

# 49. Claim Dependency Propagation

若 claim $c_2$ 是：

$$
c_2
=
f(c_1,e_3)
$$

而支持 $c_1$ 的 evidence 被撤回，Ledger 應能找到：

$$
\operatorname{Descendants}(c_1)
$$

並觸發 re-verification。

這使 evidence update 可以向下游傳播。

---

# 50. Claim–Evidence Graph 與 Provenance Graph 不同

Provenance Graph 回答：

> 這東西怎麼來的？

Claim–Evidence Graph 回答：

> 這個東西與哪個命題有什麼 epistemic relation？

因此：

$$
G_{\text{PROV}}
\neq
G_{CE}
$$

但兩者可以互相引用。

---

# 51. Evidence Ledger 與 Search Receipt 不同

Search Receipt：

> AI 搜了什麼、怎麼搜、為什麼停止。

Evidence Ledger：

> 哪些 evidence 被保留、驗證、變更並支持哪些 claims。

因此：

$$
\mathcal{R}_{\text{search}}
\neq
L_E
$$

但每個 Evidence Object 應能追溯到 originating Search Receipt event。

---

# 52. Evidence 與 Usage Envelope 必須一起保存

Paper 04 已建立：

$$
U_E(d)
$$

Evidence Object 因此應保存：

$$
(e,U_E)
$$

而不是：

$$
e
$$

單獨存在。

因為某 evidence 可以：

- 合法內部驗證；
- 但不能 raw redistribution。

這不影響它的 epistemic value，但影響輸出形式。

---

# 53. Evidence Export

最終報告引用 Evidence Object 時，輸出層必須同時檢查：

1. epistemic verification；
2. rights / policy envelope。

因此：

$$
\operatorname{Publishable}(e)
=
\operatorname{Verified}(e)
\land
\operatorname{ExportAllowed}(e)
$$

即使 evidence 正確，也可能只能輸出摘要、統計或 citation，而不能複製大量原文。

---

# 54. 數據與文字應共用 Evidence Contract

Evidence 不應只支援文章句子。

可以統一處理：

```text
text span
table row
API JSON field
time-series observation
image region
audio segment
code line
patent claim
graph edge
computed statistic
```

共同欄位是：

- identity；
- version；
- anchor；
- provenance；
- verification；
- relation。

---

# 55. Structured Data Anchor

對 time series：

$$
A_e
=
(
dataset,
series,
timestamp,
field,
unit,
vintage
)
$$

比：

```text
page 4
```

更合理。

---

# 56. Patent Evidence Anchor

例如：

$$
A_{\text{patent}}
=
(
\text{publication-number},
\text{version},
\text{claim-number},
\text{paragraph/figure},
\text{jurisdiction}
)
$$

若做 claim chart，必須知道是哪一個 claim 的哪一段 element 對應 prior-art evidence。

---

# 57. Weather Observation Anchor

$$
A_{\text{weather}}
=
(
station,
dataset,
variable,
observation-time,
quality-flag,
unit,
revision
)
$$

這使 station metadata 與 observation 本身可以分開驗證。

---

# 58. Academic Evidence Anchor

可以是：

```text
DOI
version
page
section
paragraph
figure/table
quote/span hash
```

並保存：

```text
preprint / published / corrected
```

避免 AI 把不同版本內容混在一起。

---

# 59. Economic Revision Example

假設 2025 Q4 GDP：

$$
v_1=2.1
$$

後來：

$$
v_2=1.8
$$

兩者不一定 contradiction。

可能：

$$
\operatorname{Supersedes}(v_2,v_1)
$$

Evidence Ledger 應保存兩個 observation 與 revision relation。

---

# 60. Patent Family Example

同一 invention 可能有：

$$
p_1,p_2,\ldots,p_n
$$

分布在多司法管轄。

Evidence Runtime 應分離：

```text
family identity
publication identity
grant identity
legal-status identity
claim version
```

否則「找到同一專利十次」會被錯誤視為十個獨立 prior arts。

---

# 61. Citation Chain Example

若 paper B 引 paper A，而文章 C 引 B 對 A 的說法：

$$
A\rightarrow B\rightarrow C
$$

C 的 evidence directness 低於直接讀 A。

因此:

$$
q_{\text{directness}}(C,A)
<
q_{\text{directness}}(A,A)
$$

Search Planner 可觸發：

$$
M_{\text{primary-source-resolve}}
$$

回到 A。

---

# 62. Source Laundering

Source laundering 是：

> 多個表面來源掩蓋共同 origin。

例如：

$$
s_0
\rightarrow
s_1,s_2,s_3
$$

若只看 domains：

$$
3\text{ sources}
$$

若看 provenance：

$$
1\text{ origin}
$$

Evidence Independence Graph 專門防止這個問題。

---

# 63. AI Recall 必須是不同 Evidence Type

LLM parameter memory 可以提供：

```text
hypothesis
search seed
candidate entity
query term
```

但不應標記：

```text
verified_external_evidence
```

因此：

$$
E_{\text{LLM-recall}}
\cap
E_{\text{external-verified}}
=
\varnothing
$$

在 type system 上直接分開。

---

# 64. Search Snippet 也不是原文 Evidence

Search Engine snippet 可能：

- 截斷；
- 拼接；
- 過期；
- 自動生成；
- 不存在於目前頁面。

因此 snippet 最多先進入：

$$
E_c
$$

不能直接變：

$$
E_v
$$

若重要，應 fetch source 並 anchor。

---

# 65. Evidence Deduplication

Dedup 不應只按 URL。

可用：

$$
\operatorname{DedupKey}
=
(
work\_id,
version,
content\_hash,
origin
)
$$

不同 manifestation 可以折疊。

但若版本不同，不應錯誤合併。

---

# 66. Evidence Identity Fold

這與 Paper 02 的 identity search 可相接。

多個表示：

$$
x_1,x_2,\ldots,x_n
$$

若屬於同一 underlying evidence object：

$$
\operatorname{Fold}
(
x_1,\ldots,x_n
)
\rightarrow
I_e
$$

但保留 manifestation lineage。

---

# 67. Evidence Quality 與 Search Ranking 分離

搜尋 ranking：

$$
Score_{\text{retrieval}}
$$

回答：

> 哪些結果可能相關？

Evidence ranking：

$$
Score_{\text{evidence}}
$$

回答：

> 哪些證據對目前 claim 最有價值？

二者不應共用同一 score。

---

# 68. Verification Cost

高品質 evidence verification 有成本：

$$
C_V
=
C_{\text{resolve}}
+
C_{\text{fetch}}
+
C_{\text{anchor}}
+
C_{\text{judge}}
+
C_{\text{cross-check}}
$$

因此 Planner 不需要驗證所有 results。

應先 selection：

$$
R
\rightarrow
E_c^{\text{high-value}}
\rightarrow
V
$$

---

# 69. Evidence Budget

Task 可以設定：

```text
primary source required
min independent corroborations
max unresolved contradictions
version check mandatory
human review required
```

形成：

$$
B_E(T)
$$

Evidence budget 不是只表示數量，而是 verification requirement。

---

# 70. Evidence Acceptance Criteria

例如：

$$
A_E(c)
=
\begin{cases}
1, & \text{primary source verified}\\
 & \land \text{no unresolved version conflict}\\
 & \land \text{required corroboration met}\\
0, & \text{otherwise}
\end{cases}
$$

對低風險 task 可簡化。

---

# 71. Evidence Gap

定義：

$$
G_E(c)
=
A_E(c)-\operatorname{Current}_E(c)
$$

概念上表示 claim 距離 acceptance 還缺什麼。

例如：

```text
missing primary source
missing independent corroboration
missing current version
contradiction unresolved
anchor broken
policy review pending
```

Paper 06 將直接用這個 gap 產生下一輪 search。

---

# 72. Verification Result 需要 Reason Code

不要只有：

```text
verified = false
```

應包含：

```text
SOURCE_UNRESOLVED
VERSION_MISMATCH
ANCHOR_NOT_FOUND
CONTENT_CHANGED
SEMANTIC_IRRELEVANT
SEMANTIC_CONTRADICTION
INDEPENDENCE_NOT_ESTABLISHED
STALE
SUPERSEDED
RETRACTED
POLICY_RESTRICTED
```

這些 reason 才能驅動 replanning。

---

# 73. Human Review

Evidence Runtime 不應假設 AI verification 永遠足夠。

Human review event：

$$
\ell_{\text{human-review}}
$$

應保存：

- reviewer role；
- reviewed objects；
- decision；
- timestamp；
- notes / structured reason；
- overridden machine decision。

這同樣不要求暴露私人 deliberation。

---

# 74. Multi-Verifier Agreement

可以同時有：

- deterministic validator；
- model A；
- model B；
- human reviewer。

定義：

$$
V(e,c)
=
\{v_1,\ldots,v_n\}
$$

最終 policy 可以：

- majority；
- authority precedence；
- human override；
- required deterministic check。

不同 domain 可配置。

---

# 75. Model Drift

如果同一 evidence：

$$
e
$$

在 model version $m_1$ 與 $m_2$：

$$
V_{m_1}(e,c)
\neq
V_{m_2}(e,c)
$$

Ledger 應保存兩次 verification events。

不能直接覆蓋。

這對長期 AI research system 很重要。

---

# 76. Evidence Schema Versioning

`EvidenceObject v0.1` 也會演化。

因此：

```text
schema_version
migration_history
original_record
normalized_record
```

都應保留。

避免新版 schema 改寫歷史 evidence meaning。

---

# 77. Provenance of Provenance

W3C PROV 支援 bundles 等 provenance-of-provenance 思想。

AUSI 同樣需要：

> 「這個 provenance metadata 是誰抽出的？」

例如：

```text
source document
↓
metadata extractor v3
↓
normalized evidence record
```

這些 extraction activities 本身要可追溯。

---

# 78. Evidence Ledger Query

Runtime 至少應支援：

```text
evidence_for_claim(claim_id)
claims_supported_by(evidence_id)
contradictions_for_claim(claim_id)
source_ancestry(evidence_id)
current_versions(work_id)
superseded_evidence()
evidence_missing_anchor()
evidence_requiring_review()
independent_support_count(claim_id)
policy_restricted_evidence()
```

這使 Planner 可以直接讀 evidence state。

---

# 79. Evidence Ledger 與 Graph DB

Graph DB 很適合：

$$
G_{CE}
+
G_{\text{PROV}}
+
G_{\text{independence}}
$$

但 append-only ledger 也適合 event store。

因此推薦：

```text
event store = canonical history
graph/materialized views = query acceleration
```

避免把 graph projection 當唯一 canonical history。

---

# 80. Evidence Cache

Verified evidence 可 cache。

但是：

$$
\text{verified at }t_1
$$

不一定代表：

$$
\text{valid at }t_2
$$

因此 cache key 應包含：

- source version；
- policy version；
- verification profile；
- model / verifier version；
- task scope。

---

# 81. Reverification Trigger

可以由：

```text
source hash changed
new version found
retraction found
policy changed
new contradiction
claim scope changed
verifier upgraded
anchor failed
```

觸發：

$$
M_{\text{reverify}}
$$

---

# 82. Evidence Compression

AI 可以摘要 evidence，但：

$$
\operatorname{Compress}(e)
$$

不能切斷：

$$
\operatorname{Provenance}(e)
$$

摘要應保留：

```text
derived_from
anchor refs
transform activity
source refs
```

這延續既有 `ai-web-research` 中「AI 可以壓縮，但不能切斷來源」的設計方向。

---

# 83. Evidence Synthesis

多個 Evidence Objects 可以形成：

$$
S_c
=
\operatorname{Synthesize}
(
E^+(c),
E^-(c),
E^q(c)
)
$$

其中：

- $E^+$：支持；
- $E^-$：反證；
- $E^q$：qualification。

Synthesis 是 derived knowledge object，不是 raw evidence。

---

# 84. Research Conclusion 也要有 Provenance

最終 conclusion：

$$
k
=
g(C,G_{CE})
$$

應保存：

```text
input claims
input evidence
synthesis method
model/version
timestamp
uncertainty
unresolved contradictions
```

因此知識輸出也可被 re-evaluate。

---

# 85. Evidence State 與 Planner 的閉環

Paper 03：

$$
S_t
\rightarrow
a_t
$$

Paper 05 後：

$$
S_t
=
(
\cdots,
E_t,
G_{CE,t},
G_{gap,t}
)
$$

因此：

$$
\pi(S_t)
$$

可以知道：

> 不是「再搜更多」，而是「目前 claim $c_7$ 缺 primary source」。

這是 autonomous research 能力的重要轉折。

---

# 86. Domain Pack：Economics

Economic Evidence Profile 可以要求：

```text
series_id
provider
original_source
unit
frequency
seasonal_adjustment
observation_date
vintage
revision_date
retrieval_time
```

Derived indicator 另外保存 formula。

---

# 87. Domain Pack：Meteorology

Weather Evidence Profile：

```text
station_id
variable
unit
observation_time
quality_flag
dataset_version
station_metadata
retrieval_time
```

若 station relocation / instrument change，應視為 provenance event。

---

# 88. Domain Pack：Patent Intelligence

Patent Evidence Profile：

```text
family_id
publication_number
jurisdiction
publication_date
priority_date
legal_status_snapshot
claim_number
claim_text_version
paragraph/figure anchor
citation relation
```

這可直接支援 claim chart。

---

# 89. Domain Pack：Academic Research

Academic Evidence Profile：

```text
DOI / persistent id
work version
retraction/correction state
page/span
quote hash
study type
primary/secondary role
citation ancestry
```

近期 paper 可加 preprint / peer-reviewed distinction。

---

# 90. Domain Pack：Web Evidence

Web Evidence Profile：

```text
canonical_url
retrieval_time
content_hash
publisher
page title
published/modified time
archive ref
span selector
origin ancestry
```

若內容容易變動，必要時保存 authorized snapshot。

---

# 91. Benchmark

可建立 Evidence Lifecycle Benchmark。

任務包含：

- citation exists but does not support claim；
- search snippet differs from page；
- same article syndicated across 10 sites；
- dataset value revised；
- DOI has preprint and final version；
- patent family duplicates；
- correct source but wrong series/unit；
- primary and secondary sources disagree；
- quote exists but is taken out of scope；
- source retracted after initial report。

---

# 92. Baselines

## B0 — Retrieval Only

搜尋結果直接進答案。

## B1 — URL Citation

保存 URL，但無 anchor/version。

## B2 — Quote Check

只檢查文字是否存在。

## B3 — Citation Entailment

判斷 support，但無 provenance / independence。

## Proposed — AEL + Ledger

包含：

- identity；
- version；
- anchor；
- provenance；
- semantic relation；
- independence；
- contradiction；
- ledger；
- usage envelope。

---

# 93. Metrics

$$
\text{Anchor Validity Rate}
$$

$$
\text{Citation Support Precision}
$$

$$
\text{Citation Support Recall}
$$

$$
\text{Source Independence Accuracy}
$$

$$
\text{Version Resolution Accuracy}
$$

$$
\text{Contradiction Detection Rate}
$$

$$
\text{Provenance Completeness}
$$

$$
\text{Reverification Success}
$$

$$
\text{Unsupported Claim Rate}
$$

$$
\text{Stale Evidence Rate}
$$

$$
\text{Cost per Verified Claim}
$$

---

# 94. 初步研究命題

## P5.1 — Result–Evidence Separation Hypothesis

顯式區分 Search Result 與 Verified Evidence，應降低 retrieval relevance 被錯誤當成 factual support 的比例。

## P5.2 — Granular Anchoring Hypothesis

加入 versioned granular anchor 應提高 citation reproducibility 與後續 re-verification 成功率。

## P5.3 — Independence Graph Hypothesis

利用 provenance ancestry 推估 source independence，應比 domain-counting 更能辨識 source laundering。

## P5.4 — Multi-Dimensional Verification Hypothesis

將 verification 拆為 identity、fixity、anchor、temporal、semantic 與 independence 等維度，應比單一 confidence score 更能定位 evidence failure。

## P5.5 — Append-Only Ledger Hypothesis

append-only evidence events 應提高對 revision、retraction 與 model-drift 的 auditability。

## P5.6 — Claim-Level Mapping Hypothesis

atomic claim–evidence mapping 應降低一句話多 claim、單 citation 所造成的 partial-support error。

## P5.7 — Evidence-Gap Planning Hypothesis

讓 Search Planner 直接讀取 evidence gap，應比 generic query expansion 更有效率地提升 verified claim coverage。

---

# 95. 工程落地

對 `ai-web-research`，可以新增：

```text
evidence/
    models.py
    identity.py
    anchors.py
    temporal.py
    provenance.py
    transforms.py
    verifier.py
    independence.py
    claim_graph.py
    quality.py
    ledger.py
    events.py
    reverify.py

storage/
    content_store.py
    evidence_store.py

planning/
    evidence_gap.py
```

---

# 96. 第一版 Evidence States

MVP 可先支援：

```text
DISCOVERED
ACQUIRED
IDENTIFIED
ANCHORED
VERIFIED
CONTRADICTED
QUALIFIED
SUPERSEDED
UNVERIFIABLE
```

不要一開始就做所有 domain-specific state。

---

# 97. 第一版 Verifiers

```text
source_identity_verifier
hash_verifier
anchor_verifier
temporal_verifier
semantic_support_verifier
independence_verifier
```

每個 verifier 回傳 typed result。

---

# 98. 第一版 Ledger

可以先用：

```text
SQLite / PostgreSQL
append-only event table
content-addressed evidence blobs
materialized current_state view
```

不必先做 blockchain。

---

# 99. Canonical Evidence Workflow

```text
Search Result
↓
Candidate Selection
↓
Authorized Acquisition
↓
Source / Work Identity Resolution
↓
Version Resolution
↓
Anchor Creation
↓
Fixity Check
↓
Semantic Relation Check
↓
Independence / Cross-Source Check
↓
Evidence Ledger Commit
↓
Claim–Evidence Graph Update
↓
Evidence Gap Update
↓
Planner Replan or Stop
```

---

# 100. 核心不變量

本文提出十四個 invariants。

## I1 — Retrieved ≠ Verified

$$
R\neq E_v
$$

## I2 — Citation ≠ Support

$$
\operatorname{Cites}
\neq
\operatorname{Supports}
$$

## I3 — Quote Match ≠ Entailment

$$
\operatorname{QuoteVerified}
\neq
\operatorname{ClaimSupported}
$$

## I4 — URL ≠ Source Identity

$$
URL\neq I_s
$$

## I5 — Work ≠ Manifestation

$$
I_{\text{work}}
\neq
I_{\text{manifestation}}
$$

## I6 — Same URL ≠ Same Content

$$
URL_{t_1}=URL_{t_2}
\not\Rightarrow
Content_{t_1}=Content_{t_2}
$$

## I7 — Hash Fixity ≠ Truth

$$
\operatorname{Fixity}
\neq
\operatorname{Truth}
$$

## I8 — Corroboration Requires Independence Awareness

$$
\#Evidence
\neq
\#IndependentOrigins
$$

## I9 — Revision ≠ Contradiction

$$
\operatorname{Supersedes}
\neq
\operatorname{Contradicts}
$$

## I10 — Derived Evidence ≠ Raw Evidence

$$
E_{\text{derived}}
\neq
E_{\text{raw}}
$$

## I11 — Provenance Must Survive Compression

$$
\operatorname{Compress}(e)
\not\Rightarrow
\operatorname{DropProvenance}(e)
$$

## I12 — Evidence History Is Append-Only

新的狀態不能抹除舊 evidence event。

## I13 — Verification Is Task-Relative

$$
V=V(T)
$$

## I14 — Evidence Rights Travel with Evidence

$$
e
\Rightarrow
(e,U_E)
$$

---

# 101. 限制

第一，Evidence Runtime 不能成為 truth oracle。Verified Evidence 只表示指定 verification contract 已滿足，不代表 claim 在所有可能世界與解釋下為真。

第二，source independence 很難完全自動判斷。共同資料源、未公開 syndication 與間接 citation chain 可能無法觀察。

第三，semantic support verification 仍可能受 LLM judge error、ambiguity 與 domain expertise 限制。

第四，dynamic Web content 的 granular anchoring 並不總是穩定，尤其是 client-side rendering、personalization 與 continuously updated pages。

第五，content hashes 能驗證 fixity，但不能驗證原資料是否真實、完整或無偏誤。

第六，evidence quality 不應被誤解為跨 domain 唯一可比較的 scalar。

第七，大規模 ledger 會帶來 storage、deduplication、indexing 與 re-verification cost。

第八，保存 authorized snapshots 仍必須遵守 Paper 04 的 Usage Envelope 與 retention rules。

第九，本文沒有完整處理 statistical evidence strength、causal inference quality 或 domain-specific study-design appraisal；這些應由 Domain Pack 擴充。

---

# 102. 結論

AI 原生搜尋不能停在：

$$
\text{Search}
\rightarrow
\text{Results}
$$

研究型系統需要：

$$
\boxed{
\text{Search}
\rightarrow
\text{Candidate Evidence}
\rightarrow
\text{Anchoring}
\rightarrow
\text{Verification}
\rightarrow
\text{Claim Linking}
\rightarrow
\text{Ledger}
}
$$

本文最核心的區分是：

$$
\boxed{
\text{Retrieved}
\not\Rightarrow
\text{Verified}
}
$$

以及：

$$
\boxed{
\text{Citation Exists}
\not\Rightarrow
\text{Citation Supports Claim}
}
$$

AUSI 因此不把 provenance、data citation 或 nanopublication 當作新發明，而是把這些成熟思想帶入 AI Search Runtime：

$$
\text{W3C PROV}
+
\text{Data Citation}
+
\text{Fixity}
+
\text{Claim Mapping}
+
\text{AI Verification}
+
\text{Search Receipt}
$$

形成可供 Planner 使用的 Evidence State。

最終，一個 Evidence Object 不只是：

```text
content + URL
```

而是：

```text
identity
+ version
+ anchor
+ fixity
+ provenance
+ time
+ transformation
+ rights envelope
+ verification state
+ claim relation
+ independence
+ ledger history
```

Paper 01 定義 AI-Native Search。

Paper 02 建立 Search Method Space。

Paper 03 建立 Search Planner。

Paper 04 建立 Authorized Acquisition boundary。

Paper 05 則讓「取得到的資料」第一次真正成為可驗證、可追溯、可修訂的研究證據。

這也建立下一篇所需要的核心狀態：

$$
G_E(c)
=
\text{Evidence Gap of Claim }c
$$

因此下一步將進入：

> **Paper 06 — 反證優先與缺口驅動搜尋：Counter-Evidence、Coverage Gap、Uncertainty-Directed Search 與自主研究閉環**

AI 的下一個 query 不再只來自原始問題，而可以來自：

> **「我的證據結構目前還缺什麼？」**

---

# References

[1] Moreau, L., Missier, P., et al. (2013). *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013.

[2] Lebo, T., Sahoo, S., McGuinness, D., et al. (2013). *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013.

[3] Data Citation Synthesis Group. (2014). *Joint Declaration of Data Citation Principles*. FORCE11. DOI: 10.25490/a97f-egyk.

[4] Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). *The FAIR Guiding Principles for Scientific Data Management and Stewardship*. Scientific Data, 3, 160018. DOI: 10.1038/sdata.2016.18.

[5] Groth, P., Gibson, A., & Velterop, J. (2010). *The Anatomy of a Nanopublication*. Information Services & Use, 30(1–2), 51–56. DOI: 10.3233/ISU-2010-0613.

[6] Kuhn, T., Barbano, P. E., Nagy, M. L., & Krauthammer, M. (2013). *Broadening the Scope of Nanopublications*. Extended Semantic Web Conference, 487–501.

[7] Kuhn, T., & Dumontier, M. (2014). *Trusty URIs: Verifiable, Immutable, and Permanent Digital Artifacts for Linked Data*. ESWC 2014, 395–410. DOI: 10.1007/978-3-319-07443-6_25.

[8] Starr, J., Castro, E., Crosas, M., et al. (2015). *Achieving Human and Machine Accessibility of Cited Data in Scholarly Publications*. PeerJ Computer Science, 1:e1. DOI: 10.7717/peerj-cs.1.

[9] Min, S., Krishna, K., Lyu, X., Lewis, M., Yih, W.-T., Koh, P. W., Iyyer, M., Zettlemoyer, L., & Hajishirzi, H. (2023). *FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation*. Proceedings of EMNLP 2023, 12076–12100.

[10] Es, S., James, J., Espinosa-Anke, L., & Schockaert, S. (2024). *RAGAS: Automated Evaluation of Retrieval Augmented Generation*. Proceedings of EACL 2024 System Demonstrations.

[11] Lewis, P., Perez, E., Piktus, A., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems 33.

[12] Buneman, P., Khanna, S., & Tan, W.-C. (2001). *Why and Where: A Characterization of Data Provenance*. ICDT 2001, 316–330.

[13] Cheney, J., Chiticariu, L., & Tan, W.-C. (2009). *Provenance in Databases: Why, How, and Where*. Foundations and Trends in Databases, 1(4), 379–474.

[14] Miles, S., Groth, P., Munroe, S., & Moreau, L. (2011). *PrIMe: A Methodology for Developing Provenance-Aware Applications*. ACM Transactions on Software Engineering and Methodology, 20(3).

[15] World Wide Web Consortium. *PROV Model Primer*. W3C Working Group Note, 30 April 2013.

[16] Nanopublication Community. *Nanopublication Guidelines*. Accessed 2026-08-31.

[17] FORCE11. *Joint Declaration of Data Citation Principles — Specificity and Verifiability*. Accessed 2026-08-31.

---

# Series Continuation

**Paper 06 — 反證優先與缺口驅動搜尋：Counter-Evidence、Coverage Gap、Uncertainty-Directed Search 與自主研究閉環**

下一篇將以本文建立的：

$$
G_E(c)
$$

以及：

$$
G_{CE}
$$

作為 Planner 的直接輸入，研究 AI 如何從：

- missing primary source；
- insufficient independent corroboration；
- unresolved contradiction；
- uncovered terminology；
- uncovered jurisdiction；
- missing version；
- asymmetric evidence；
- low-confidence relation；

自動產生下一輪 Search Plan。

也就是把：

$$
Q_{t+1}
=
f(Q_t)
$$

進一步改寫成：

$$
\boxed{
\Pi_{t+1}
=
f(
G_E,
G_{CE},
\Omega_{\text{coverage}},
U_t
)
}
$$

讓搜尋真正由「證據缺口」而不是單純由上一個 query 驅動。
