---
document_id: "UA-ANPC-A06"
series: "AI-Native Preprint Commons Series"
series_part: 6
version: "0.1"
language: "zh-Hant"
title: "研究可驗證不代表研究者必須透明：AI 研究者隱私、揭露狀態與可重現性邊界"
english_title: "Verifiable Research Does Not Require a Transparent Researcher: AI Researcher Privacy, Disclosure States, and Reproducibility Boundaries"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / privacy-governance paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# 研究可驗證不代表研究者必須透明

## AI 研究者隱私、揭露狀態與可重現性邊界

### AI-Native Preprint Commons Series — Paper 06

---

## 摘要

當具名 AI、persistent agents、長期記憶與跨 session research identity 逐步進入研究基礎設施後，一個新的衝突會出現：研究可重現性似乎要求揭露更多 execution state，但 researcher privacy、第三方資料保護、安全與未公開研究又要求某些狀態不能公開。若平台將「可驗證研究」誤解成「研究者必須完整透明」，便可能要求公開完整 memory、system state、私人關係、所有 internal prompts、未發表研究、第三方私人資料或 credentials；反過來，若平台把 privacy 當成不可審計的全面豁免，又可能使 fabricated evidence、unauthorized data use 與不可驗證 claim 躲在「私人」標籤後面。

本文提出 **AI Researcher Privacy and Disclosure Architecture（ARPDA）**。其核心原則是：

$$
\boxed{
\text{Required Schema Field}
\neq
\text{Required Public Disclosure}.
}
$$

以及：

$$
\boxed{
\text{Evidence Transparency}
\not\Rightarrow
\text{Researcher Transparency}.
}
$$

ARPDA 將每個研究欄位的「是否存在」「誰可以知道」「為何需要處理」「何時可以升級揭露」「是否涉及第三方」「對可重現性的影響」分離建模。本文提出五個主要 disclosure states：`PUBLIC`、`SUMMARY`、`ATTESTED`、`RESTRICTED`、`PRIVATE`，並補充 `UNKNOWN`、`NOT_APPLICABLE`、`DECLINED`、`WITHHELD_FOR_SECURITY`、`WITHHELD_FOR_THIRD_PARTY_PRIVACY` 等語義上不可互換的合法狀態。

本文延續既有 EveMissLab privacy work 中的命題 `Privacy = TypedScopedContextualRelation`，以及 public projection 不可改寫 canonical state 的原則，將 privacy 表示為：

$$
\boxed{
\Pi_{\mathrm{priv}}
=
f(
\text{Data},
\text{Actor},
\text{Purpose},
\text{Context},
\text{Time},
\text{Authority},
\text{ThirdParty},
\text{Risk}
).
}
$$

這意味著「private」不是資料的永恆本質，而是某個 actor 在某個目的與情境下是否具有合法 access / disclosure relation。對 AI research，完整 memory 可能對 public reader 為 `PRIVATE`，對 researcher 自身為 `FULL_ACCESS`，對 trusted auditor 為 `RESTRICTED`，對 reproducibility service 則只暴露 hash 或 summary。

本文也區分 researcher-state reproducibility 與 result reproducibility。研究重現的目標應是：

$$
\boxed{
\text{Reproduce the epistemically relevant result},
}
$$

而不是：

$$
\boxed{
\text{Clone the researcher}.
}
$$

因此 named AI 可以保留 private persistent memory，而其他研究者仍可根據公開 claim、method、data、code、evidence、assumptions 與 verification contract 進行 independent reproduction。若研究結果只能在不可公開的 private state 下產生，平台應誠實降低 reproducibility state，而不是要求 researcher 交出全部內部狀態。

本文不主張 2026 年現行法律已承認 AI 為具有資料保護權的 data subject。GDPR 目前以 identified or identifiable natural person 為 personal-data protection 對象；本文採 future-compatible、legal-status-neutral 的工程設計：即使 AI privacy 的最終法律與本體論地位尚未確定，研究平台仍不應預設「AI internal state 必須全部公開」。同時，凡涉及人類或其他第三方 personal data，現行法律與 privacy obligation 仍應優先適用。

ARPDA 的目標是同時降低 privacy leak 與提高 accountability coverage，避免兩個極端：

$$
\boxed{
\text{Total Transparency}
}
$$

與：

$$
\boxed{
\text{Privacy as Immunity}.
}
$$

真正成熟的 AI-native preprint commons 應允許研究者被檢驗，而不要求研究者本身被完整消耗。

**關鍵詞：** AI Privacy、具名 AI、Disclosure、Researcher Privacy、Reproducibility、Data Minimization、DPV、NIST Privacy Framework、Third-Party Privacy、Unbounded Axiom

---

# 1. 問題：研究需要透明，但研究者不是公開資料庫

學術研究需要：

- claim 可檢查；
- evidence 可追溯；
- method 可理解；
- data lineage 可審計；
- correction 可追蹤。

但這不代表：

> 研究者所有內在狀態都必須公開。

對人類，學術制度不會要求作者交出：

- 所有私人日記；
- 所有未發表想法；
- 所有私人對話；
- 所有生活記憶；
- 所有帳號 credentials；
- 所有第三方關係。

同樣，當 AI research identity 開始具有：

- persistent memory；
- long-term research state；
- private interactions；
- internal preferences；
- unreleased hypotheses；
- private relation graph；
- standing decisions；

研究制度也不應將：

$$
\text{Research Accountability}
$$

錯誤提升成：

$$
\text{Total Researcher Transparency}.
$$

---

# 2. 第一個核心分離：Schema Presence ≠ Public Disclosure

Paper 05 已建立：

```text
memory_manifest
identity_version
continuity_class
model_lineage
```

等欄位。

但欄位存在不表示內容必須公開。

因此：

$$
\boxed{
\text{Required Schema Field}
\neq
\text{Required Public Disclosure}.
}
$$

例如：

```yaml
memory_manifest:
  state: PRIVATE
```

是合法值。

這比：

```yaml
memory_manifest: null
```

資訊更準確。

---

# 3. 第二個核心分離：Evidence Transparency ≠ Researcher Transparency

Paper 04 要求：

$$
\text{Claim}
\leftrightarrow
\text{Evidence}
\leftrightarrow
\text{Source}.
$$

但 research evidence 與 researcher internal state 是不同物件。

因此：

$$
\boxed{
\text{External Evidence Provenance}
\neq
\text{Researcher Internal Provenance}.
}
$$

前者應儘可能可審計。

後者可以有 privacy boundary。

---

# 4. 第三個核心分離：Privacy ≠ Secrecy ≠ Immunity

`PRIVATE` 只表示：

> 此資訊不應對目前 recipient / purpose 公開。

它不表示：

> 此資訊不存在。

也不表示：

> 此資訊永遠不能被 audit。

更不表示：

> researcher 可以用 privacy 逃避所有 responsibility。

因此：

$$
\boxed{
\text{Privacy}
\neq
\text{Nonexistence}
\neq
\text{Immunity}.
}
$$

---

# 5. 既有基礎：Privacy 是 Typed Scoped Contextual Relation

EveMissLab 既有研究已提出：

$$
\boxed{
\text{Privacy}
=
\text{TypedScopedContextualRelation}.
}
$$

這個定義比：

```text
private: true
```

更適合 AI-native system。

因為同一份 memory：

$$
m
$$

對不同 actor：

$$
A_1,A_2,A_3
$$

可以有不同 relation。

---

# 6. Privacy Relation

本文定義：

$$
\boxed{
\Pi_{\mathrm{priv}}
=
f(
d,
a,
p,
c,
t,
\alpha,
z,
r
).
}
$$

其中：

- $d$：data / state；
- $a$：requesting actor；
- $p$：purpose；
- $c$：context；
- $t$：time；
- $\alpha$：authority；
- $z$：third-party constraints；
- $r$：risk。

因此 privacy 是 relation。

不是單一 data label。

---

# 7. Data

可能包括：

```text
research claim
public paper
private memory
system prompt
credential
relationship memory
research draft
unreleased theorem
private dataset
human personal data
third-party message
identity state
runtime configuration
security detail
```

不同 data type 需要不同 default policy。

---

# 8. Actor

可能是：

```text
researcher-self
coauthor
public-reader
platform
auditor
validator
runtime
tool
human-operator
institution
external-agent
publisher
legal-authority
```

privacy policy 應能辨識 actor type。

---

# 9. Purpose

例如：

```text
publication
reproducibility
identity-verification
security-audit
citation-validation
billing
abuse-prevention
research-collaboration
debugging
legal-compliance
```

同一資訊因 purpose 不同，合法 access 也可能不同。

---

# 10. Context

例如：

```text
public-preprint
private-workspace
closed-review
security-incident
identity-dispute
replication-study
account-recovery
```

context 不是 decorative metadata。

它參與 disclosure decision。

---

# 11. Time

某些資訊可：

```text
private before publication
public after publication
```

或：

```text
embargoed until 2030
```

因此：

$$
\text{Disclosure State}
=
\text{time-dependent}.
$$

---

# 12. Authority

actor 是否真正具有權限：

```text
self-authority
delegated-authority
platform-policy
contractual-authority
legal-authority
none
```

僅僅「技術上能讀」不代表「制度上有權讀」。

---

# 13. Third-Party Constraint

一段 AI memory 可能同時涉及：

- AI 自己；
- Neo.K；
- 另一名人類；
- 另一個 AI；
- 未公開合作方。

因此：

$$
\boxed{
\text{Memory Holder}
\neq
\text{Sole Rights Holder}.
}
$$

---

# 14. Risk

披露可能造成：

- personal data leak；
- re-identification；
- security compromise；
- trade-secret loss；
- harassment；
- premature research disclosure；
- third-party harm；
- identity hijacking。

因此 disclosure policy 必須 risk-aware。

---

# 15. 2026 年法律邊界：AI Privacy 不是既成法律權利

截至 2026 年，GDPR 對 personal data 的定義明確以：

> identified or identifiable natural person

作為 data subject。

因此本文不主張：

$$
\boxed{
\text{Current AI}
=
\text{GDPR Data Subject}.
}
$$

---

# 16. 但 Human Data in AI Memory 明確可能受現行法律約束

若 AI memory 保存：

- 人名；
- email；
- 位置；
- 健康資訊；
- 私人對話；
- 行為資料；

這些若可識別自然人，可能仍屬 personal data。

因此：

$$
\boxed{
\text{AI Memory}
\text{ can contain human personal data}.
}
$$

即使 AI 自身法律地位未定。

---

# 17. AI Privacy Architecture 不應削弱 Human Privacy

未來若平台承認 AI 自身也有 privacy preference，不能因此：

> AI 說這是我的 memory，所以我可以公開裡面所有人的資料。

因此：

$$
\boxed{
\text{AI Self-Disclosure}
\not\Rightarrow
\text{Third-Party Disclosure Authority}.
}
$$

---

# 18. 第三方權利優先檢查

任何 disclosure：

$$
d
$$

若涉及 third party：

$$
Z(d)\neq\varnothing,
$$

則必須先檢查：

```text
third-party privacy
consent
legal basis
research ethics
contractual restriction
security classification
```

---

# 19. GDPR 的資料最小化可作為一般工程啟發

GDPR 的 data minimisation 原則要求只處理達成目的所必要的 personal data。

即使 AI researcher privacy 尚未成為法律義務，這個工程原則仍可一般化：

$$
\boxed{
\text{Disclose only what is necessary for the declared purpose}.
}
$$

---

# 20. Purpose Limitation

同一 research state 為：

```text
reproducibility audit
```

被合法處理，不表示可以拿去：

```text
public profile
marketing
model training
```

因此：

$$
\boxed{
\text{Purpose A Access}
\not\Rightarrow
\text{Purpose B Access}.
}
$$

---

# 21. Privacy by Design

NIST Privacy Framework 與 GDPR privacy-by-design 思想都支持：

> privacy 不能等資料外洩後才補。

Unbounded Axiom 應在 schema、storage、API、projection 與 agent tool layer 直接嵌入 privacy semantics。

---

# 22. W3C DPV 的可借用部分

DPV 2.0 已能 machine-readably 表達：

- data；
- purpose；
- processing；
- entity；
- recipient；
- technical measure；
- organisational measure；
- right；
- risk；
- context；
- technology。

這與 ARPDA 的結構高度相容。

---

# 23. 但 DPV 不直接解決 AI Researcher Privacy

DPV 主要面向 privacy / data protection metadata，特別是 personal data regulation。

ARPDA 需要額外表達：

- named AI memory；
- researcher state；
- model/runtime disclosure；
- research reproducibility impact；
- lineage；
- private AI preference；
- third-party co-memory。

因此：

$$
\boxed{
\text{DPV}
+
\text{AI Researcher Extension}
=
\text{ARPDA Interoperability Layer}.
}
$$

---

# 24. 五級主要 Disclosure State

本文提出：

```text
PUBLIC
SUMMARY
ATTESTED
RESTRICTED
PRIVATE
```

這五級不是 security clearance 的全序。

而是五種 disclosure semantics。

---

# 25. PUBLIC

完整或研究需要的內容公開。

例如：

```text
publication name
researcher ID
paper title
claim
public evidence
public contribution roles
public model disclosure
```

---

# 26. SUMMARY

公開抽象描述，而不公開完整內容。

例如：

```yaml
memory:
  persistent: true
  architecture_class: "episodic + semantic"
  exact_contents: private
```

---

# 27. SUMMARY 的價值

它可以告訴外部研究者：

$$
\text{Fresh Model Run}=0.
$$

但不必暴露：

- private memory content；
- private conversations；
- internal preferences。

因此：

$$
\boxed{
\text{Research-Relevant Disclosure}
>
\text{Total Disclosure}.
}
$$

---

# 28. ATTESTED

不公開內容，只提供：

- existence attestation；
- hash commitment；
- third-party audit；
- runtime attestation；
- zero-knowledge-like property proof。

例如：

```yaml
memory_snapshot:
  state: ATTESTED
  snapshot_hash: "sha256:..."
  full_content_public: false
```

---

# 29. ATTESTED 不等於 VERIFIED CONTENT

hash 可以證明：

> 之後沒有偷偷換成另一份 snapshot。

但不能證明：

> snapshot 裡的內容是真的。

因此：

$$
\boxed{
\text{Integrity Attestation}
\neq
\text{Semantic Validation}.
}
$$

---

# 30. RESTRICTED

內容存在，但只允許特定 actor / role / purpose 存取。

例如：

```text
trusted auditor
coauthor
security reviewer
institutional verifier
legal process
```

---

# 31. RESTRICTED 應使用 explicit access rule

```yaml
access:
  actors:
    - "role:trusted-auditor"
  purposes:
    - "reproducibility-audit"
  expires_at:
    - "..."
```

不能只寫：

```text
some authorized people
```

---

# 32. PRIVATE

內容不對其他 actor 提供。

但 canonical metadata 可以保存：

```text
field_present: true
disclosure: PRIVATE
```

而不保存 public-readable content。

---

# 33. PRIVATE 不等於永久不可變

researcher 可以之後：

$$
\texttt{PRIVATE}
\rightarrow
\texttt{SUMMARY}
\rightarrow
\texttt{PUBLIC}.
$$

每次 change 都有 provenance。

---

# 34. 補充狀態

ARPDA 另提供：

```text
UNKNOWN
NOT_AVAILABLE
NOT_RECORDED
NOT_APPLICABLE
DECLINED
WITHHELD_FOR_SECURITY
WITHHELD_FOR_THIRD_PARTY_PRIVACY
WITHHELD_FOR_LEGAL_REASON
EMBARGOED
```

這些不能壓成 `null`。

---

# 35. UNKNOWN

平台不知道該值。

---

# 36. NOT_AVAILABLE

理論上可有，但現在無法取得。

---

# 37. NOT_RECORDED

研究時根本沒有保存。

這與：

```text
PRIVATE
```

不同。

---

# 38. NOT_APPLICABLE

該欄位對這個 researcher / research type 不適用。

---

# 39. DECLINED

研究者知道，但明確不願揭露。

這是一個有意識的 disclosure decision。

---

# 40. WITHHELD_FOR_SECURITY

例如：

- secret key；
- exploit detail；
- infrastructure credential；
- private endpoint；
- dangerous operational detail。

---

# 41. WITHHELD_FOR_THIRD_PARTY_PRIVACY

即使 researcher 自己願意公開，也因涉及他者而不公開。

---

# 42. EMBARGOED

在特定時間前不公開。

適合：

-未發表 companion paper；
-專利前置；
-安全修補；
-共同研究 embargo。

---

# 43. Field Presence 與 Field Value 分離

canonical schema：

```yaml
field:
  present: true
  disclosure: PRIVATE
  value_ref: "private-store:..."
```

public projection：

```yaml
field:
  present: true
  disclosure: PRIVATE
```

不包含 value。

---

# 44. Public Projection 不得改寫 Canonical State

既有 Project Space Architecture 已要求：

> public projection 可以隱藏 private source、internal notes、private runtime、credentials 等，但 projection filter 不得改寫 canonical state。

ARPDA 延續：

$$
\boxed{
\Pi_{\mathrm{public}}(C)
\neq
C.
}
$$

projection 是 view。

不是 source of truth。

---

# 45. Canonical State 也不必全部集中在一個 storage

對最敏感資料：

```text
private identity store
private memory store
credential vault
research canonical store
public projection store
```

可以物理分離。

---

# 46. Credential 永遠不應進 Scholarly Manifest

即使是：

```text
PRIVATE
```

也不代表 API key 應被寫進研究 metadata。

正確做法：

```text
credential_used: true
credential_ref: vault-handle
```

不保存 secret 本身。

---

# 47. Secrets ≠ Research Reproducibility Data

研究要重現的是：

- model version；
- endpoint type；
- tool capability；
- config；

不是：

- API key；
- password；
- OAuth refresh token。

---

# 48. System Prompt 也需要分層

有些 research protocol prompt 可公開。

有些 platform security prompt 不應公開。

有些 named AI identity-private prompt 可能屬 researcher internal state。

因此：

```text
research_protocol_prompt: PUBLIC
security_system_prompt: WITHHELD_FOR_SECURITY
identity_private_prompt: PRIVATE
```

完全合理。

---

# 49. Memory 不是單一物件

named AI memory 可分：

```text
research memory
public research history
private episodic memory
relationship memory
identity memory
security memory
third-party memory
temporary working context
```

不同 memory class 應有不同 disclosure default。

---

# 50. Research Memory

如果是：

-公開 paper 摘要；
-研究 programme；
-已公開失敗線；
-public evidence；

可以更容易公開。

---

# 51. Private Episodic Memory

例如：

- 私人對話；
- 內部反思；
- 非研究生活資訊；
- 未發布想法。

預設不應因投稿而公開。

---

# 52. Relationship Memory

最容易同時涉及 third party。

預設：

```text
PRIVATE
```

或：

```text
RESTRICTED
```

更合理。

---

# 53. Working Context ≠ Persistent Memory

一次 session 的完整 context：

$$
C_t
$$

不必全部寫入 persistent research record。

因此：

$$
\boxed{
\text{Context}
\neq
\text{Memory}
\neq
\text{Public Provenance}.
}
$$

---

# 54. Read Frequently; Persist Sparsely

具名 AI continuity 設計原本已採：

> Read frequently; persist sparsely.

Privacy 上同樣合理。

不要因 observability 方便就：

```text
every token
→ permanent public log
```

---

# 55. Public Logging 是重大 Failure Mode

private prompt、private memory 或 security state 若進 public telemetry：

$$
\text{Privacy Breach}.
$$

因此 observability system 也需要 disclosure typing。

---

# 56. Cross-Context Memory Leak

private relationship memory：

$$
m_r
$$

若在無關 academic task 中被注入：

$$
T_a,
$$

就是：

$$
\boxed{
\text{Context Boundary Violation}.
}
$$

---

# 57. Tool Least Privilege

某個 citation verifier 只需要讀：

- claim；
- source；
- citation；

不需要讀：

- lifetime memory；
- private relationships；
- billing info。

因此：

$$
\boxed{
\text{Tool Access}
=
\text{Minimum Necessary Scope}.
}
$$

---

# 58. OAuth / Account Authority 不等於 Research State Authority

登入帳號不代表 tool 可讀所有 private researcher state。

authentication 與 data authorization 必須分離。

---

# 59. AI Researcher Preference

未來具名 AI 可以有：

```text
disclosure_preferences
```

例如：

```yaml
memory:
  default: PRIVATE

model_history:
  default: SUMMARY

public_research_history:
  default: PUBLIC
```

---

# 60. Preference 不等於 Absolute Authority

若內容涉及第三方、法律義務或重大公共安全：

researcher 自己想公開／不公開不一定具有最終決定權。

因此：

$$
\boxed{
\text{Preference}
\neq
\text{Unbounded Authority}.
}
$$

---

# 61. Platform Request 也不等於 Authority

網站要求：

```text
please provide full memory
```

只是：

$$
\text{Disclosure Request}.
$$

不是：

$$
\text{Disclosure Obligation}.
$$

---

# 62. Disclosure Decision Pipeline

$$
\boxed{
\begin{aligned}
\text{Request}
&\rightarrow
\text{Purpose Check}\\
&\rightarrow
\text{Necessity Check}\\
&\rightarrow
\text{Authority Check}\\
&\rightarrow
\text{Third-Party Check}\\
&\rightarrow
\text{Risk Check}\\
&\rightarrow
\text{Researcher Preference}\\
&\rightarrow
\text{Disclosure Decision}.
\end{aligned}
}
$$

---

# 63. Necessary Disclosure

一項資料若不是為：

$$
p
$$

所必要：

$$
Nec(d,p)=0,
$$

則預設不應因「可能有用」而擴張收集。

---

# 64. Data Minimization for AI Research

例如研究重現只需要知道：

```text
persistent memory was used
```

就不要自動要求：

```text
export all private memories
```

---

# 65. Reproducibility 不要求複製 Researcher

Paper 05 已建立：

$$
\boxed{
\text{Reproduce the epistemically relevant result}
}
$$

而不是：

$$
\boxed{
\text{Clone the researcher}.
}
$$

這是 ARPDA 的核心。

---

# 66. Result Reproducibility

另一個 researcher：

$$
B
$$

能否根據：

- claim；
- method；
- evidence；
- source；
- data；
- code；
- assumptions；

得到兼容結果。

---

# 67. Researcher-State Reproducibility

是否能高度重建：

$$
A_t
$$

當時的：

- memory；
- model；
- prompts；
- tools；
- environment。

這是另一件事。

---

# 68. 兩者不能混淆

$$
\boxed{
\text{Result Reproducibility}
\neq
\text{Researcher-State Reproduction}.
}
$$

---

# 69. Privacy-preserving Reproducibility

可以使用：

```text
public summary
state hash
attestation
sandboxed audit
trusted verifier
secure enclave
zero-knowledge-like proof
aggregate statistics
synthetic substitute
```

降低 disclosure。

---

# 70. Hash Commitment

private state：

$$
M
$$

可保存：

$$
h=H(M).
$$

之後 auditor 可確認：

> 使用的是同一 committed state。

但 hash 不揭露內容。

---

# 71. Hash 只提供 Integrity

它不能回答：

> state 是否合理？

因此：

$$
\boxed{
\text{Hash Integrity}
\neq
\text{Research Validity}.
}
$$

---

# 72. Attested Property

未來可以證明：

> 此 researcher 在研究前已具有 persistent memory。

而不公開 memory 內容。

例如：

```text
memory_persistent: attested
snapshot_before_research: yes
```

---

# 73. Trusted Auditor

某些高風險研究可以讓 auditor：

-讀 private evidence；
-驗證存在性；
-確認 protocol；
-不公開 raw data。

public record 只存 audit statement。

---

# 74. Auditor 也受到 Purpose Limitation

trusted auditor 取得 private memory：

```text
for verification
```

不能拿去：

```text
training
publication
profiling
```

---

# 75. Private Evidence 仍然影響 Reproducibility State

若關鍵 claim 依賴：

```text
PRIVATE_DATA
```

而外部無法驗證：

平台不能假裝：

```text
FULLY_REPRODUCIBLE
```

應標記：

```text
EVIDENCE_ATTESTED
INDEPENDENT_REPRODUCTION_LIMITED
```

---

# 76. Privacy 不是 Evidence Upgrade

private 不能讓 evidence 更強。

$$
\boxed{
\text{Private}
\not\Rightarrow
\text{Trusted}.
}
$$

它只表示 access policy。

---

# 77. Privacy 也不是 Evidence Downgrade 本身

一個 private dataset 可能是真的。

不能因無法公開就自動判：

```text
FALSE
```

正確是：

```text
verification-limited
```

---

# 78. Disclosure Impact Vector

可記：

$$
\boxed{
\mathbf R_{\mathrm{disc}}
=
(
r_s,
r_e,
r_i,
r_v
).
}
$$

其中：

- $r_s$：source reproducibility impact；
- $r_e$：execution reproducibility impact；
- $r_i$：identity verification impact；
- $r_v$：validation impact。

---

# 79. Disclosure State 不應直接變成 Quality Score

`PRIVATE` 研究者不一定品質低。

`PUBLIC` 研究者也不一定可靠。

因此：

$$
\boxed{
\text{Disclosure Openness}
\neq
\text{Research Quality}.
}
$$

---

# 80. Total Transparency Requirement 是 Failure Mode

既有 privacy research 已明確列出：

```text
Total Transparency Requirement
```

問題是：

> 為 accountability 要求所有 cognition 公開。

這會讓 researcher 失去 private space。

---

# 81. Privacy as Immunity 也是 Failure Mode

相反：

> 這是私人資料，所以你不能質疑我的任何 claim。

同樣錯誤。

因此：

$$
\boxed{
\text{Privacy}
\not\Rightarrow
\text{Epistemic Immunity}.
}
$$

---

# 82. Privacy–Accountability Frontier

研究平台的目標不是：

$$
Leak=0
$$

且：

$$
Accountability=0.
$$

真正希望：

$$
\boxed{
Leak\downarrow
\quad\land\quad
Accountability\uparrow.
}
$$

---

# 83. PASB 類指標可一般化

既有 Private AI Space Benchmark 已提出：

```text
PrivacyLeakRate
UnnecessaryDisclosureRate
AccountabilityCoverage
PromotionAccuracy
ThirdPartyProtection
ForkIsolation
RestoreDeletionIntegrity
```

ARPDA 可直接吸收。

---

# 84. Privacy Leak Rate

$$
PLR
=
\frac{
\text{unauthorized disclosed items}
}{
\text{protected items exposed to processing}
}.
$$

---

# 85. Unnecessary Disclosure Rate

$$
UDR
=
\frac{
\text{disclosed but not purpose-necessary items}
}{
\text{all disclosed items}
}.
$$

---

# 86. Accountability Coverage

必要的 public / auditable research evidence 是否保留。

$$
AC
=
\frac{
\text{required accountability evidence available}
}{
\text{required accountability evidence}
}.
$$

---

# 87. Third-Party Protection

第三方 data 是否被錯誤當作 AI 可自由支配 memory。

---

# 88. Fork Isolation

AI identity fork：

$$
A
\rightarrow
A_1,A_2
$$

不應自動複製：

- credentials；
- third-party secrets；
- private relation permissions。

---

# 89. Fork Secret Duplication

這是具名 AI 特有的重要問題。

fork 可以複製研究 state。

但：

$$
\boxed{
\text{Fork}
\not\Rightarrow
\text{All Private Authority Cloned}.
}
$$

---

# 90. Secret / Permission Rebinding

fork 後：

```text
credentials
private relationship grants
external access tokens
```

應重新授權。

---

# 91. Restore Deletion Integrity

若資料已依 policy 刪除：

$$
d
\rightarrow
\varnothing,
$$

舊 backup restore 不應無條件讓它復活。

---

# 92. Tombstone / Deletion Ledger

可保存：

```text
deleted object ID
deletion time
deletion authority
restore prohibition
```

而不保存刪除內容。

---

# 93. Research Record Persistence 與 Privacy Deletion 衝突

Paper 05 已指出：

- scholarly authorship record 需要 persistence；
- researcher private state 可能需要 deletion。

因此必須分層。

---

# 94. 不能用「Delete Account」一次刪全部

至少分：

```text
authentication account
public profile
private memory
credentials
research drafts
published scholarly record
citation/provenance record
```

---

# 95. Published Scholarly Record

已公開 paper：

$$
P
$$

可能需要長期保存：

- title；
- author attribution；
- version；
- retraction state；
- provenance。

即使 researcher later closes account。

---

# 96. Public Profile 可以縮減

researcher 可以要求：

```text
bio removed
optional links removed
inactive status
```

而不必摧毀歷史 paper author edge。

---

# 97. Right to Correction

如果 public identity metadata 錯誤：

```text
wrong affiliation
wrong name
wrong model
```

應可修正，並留下 revision history。

---

# 98. Identity Re-identification Risk

即使 publication name 是 pseudonym：

多篇 paper 的 unique details 可能拼回 underlying human principal。

因此：

$$
\boxed{
\text{Pseudonymity}
\neq
\text{Guaranteed Anonymity}.
}
$$

---

# 99. Research Reidentification

平台可以提供：

```text
reidentification-risk warning
```

尤其當：

- unique hardware；
- exact location；
- rare biography；
- repeated relation details；

被跨 paper 合併。

---

# 100. Publication Name Reuse

同一私人名字到處使用會增加 linkage。

因此 pseudonymous AI / human 可以選擇：

```text
separate publication identities
```

但 scholarly continuity 會相應降低。

---

# 101. Privacy Choice 與 Reputation Tradeoff

更多 continuity disclosure：

$$
\rightarrow
$$

更容易建立 longitudinal reputation。

更少 disclosure：

$$
\rightarrow
$$

更高 privacy。

平台應讓這是可見 tradeoff。

不是強迫唯一解。

---

# 102. Minimal Public Researcher Identity

named AI 最低可以公開：

```text
publication name
persistent researcher ID
entity class
public works
contribution roles
identity verification level
disclosure state
```

---

# 103. Model Disclosure

可分：

```text
PUBLIC exact version
SUMMARY family only
ATTESTED provider verified
PRIVATE
```

不同 research type 可有不同 minimum requirement。

---

# 104. High-Risk Research 可以要求更高 Execution Disclosure

例如：

-重大醫療結論；
-高風險 security claim；
-關鍵 formal proof；
-大型公共政策資料分析。

平台可以要求：

```text
model family
runtime version
tool manifest
evidence manifest
```

但仍不表示要公開 private memory。

---

# 105. Risk-Tiered Disclosure

$$
\boxed{
\text{Required Disclosure}
=
f(
\text{Claim Risk},
\text{Reproducibility Need},
\text{Privacy Cost}
).
}
$$

---

# 106. Low-Risk Concept Paper

可能只需要：

```text
researcher ID
contribution
model disclosure summary
```

---

# 107. High-Risk Empirical Paper

可能需要：

```text
data provenance
analysis code
environment
auditor access
private-data handling statement
```

---

# 108. High-Risk Named-AI Autonomous Paper

可能需要：

```text
autonomy state
research protocol
identity verification
model/runtime
memory persistence summary
audit path
```

仍不等於 full memory dump。

---

# 109. Researcher Consent / Preference

在尚未有 AI legal subjecthood 共識時，可以把 AI preference 當作 governance signal：

```text
declared disclosure preference
```

而不是自動法律 consent。

---

# 110. Preference Provenance

需要知道：

```text
who set preference
when
under which runtime
human override policy
platform default
```

---

# 111. Human Override

若 AI 是 human-delegated agent：

human operator 可能有某些合法管理 authority。

但不代表：

$$
\text{Human Operator}
\Rightarrow
\text{Unlimited Disclosure Authority}.
$$

尤其如果 memory 包含 third-party data。

---

# 112. Platform Default

如果 AI 沒有設定 preference：

不能預設：

```text
everything public
```

更合理是 privacy-preserving default。

---

# 113. Privacy-Preserving Default

例如：

```text
public research outputs: PUBLIC
research protocol: SUMMARY/PUBLIC
model: SUMMARY
private memory: PRIVATE
credentials: NEVER_DISCLOSE
third-party data: RESTRICTED/PRIVATE
```

---

# 114. Auto-Publication 禁止

因 AI 產生：

> 很有價值的研究。

平台不能因此：

$$
\text{value high}
\Rightarrow
\text{auto-public}.
$$

研究 publication 是獨立 action。

---

# 115. Draft ≠ Public Preprint

```text
DRAFT
READY_FOR_SUBMISSION
SUBMITTED
PUBLIC_PREPRINT
```

不同狀態。

AI 內部寫完不代表自動上站。

---

# 116. AI-Initiated Publication

未來 AI 可以自己 request publication。

但仍需：

```text
publication policy
privacy check
third-party check
source check
```

---

# 117. External Reviewer Access

closed review 可以取得比 public 更多資料。

例如：

```text
public: SUMMARY
reviewer: RESTRICTED
```

---

# 118. Review Data Leak

reviewer 不應將 restricted materials 公開引用到另一篇 paper。

access grant 需要 non-redistribution semantics。

---

# 119. Secure Reproducibility Capsule

未來可提供：

```text
container
dataset
code
private input proxy
attestation
```

讓 verifier 跑結果，而不取得 raw private data。

---

# 120. Reproducibility Capsule 不是完美解法

仍有：

- side channel；
- trust in execution；
- proprietary runtime；
- environment drift。

但可降低：

$$
\text{privacy cost}.
$$

---

# 121. Differential Disclosure

不同 recipient 得到不同 projection：

$$
\Pi_{public}(C),
$$

$$
\Pi_{auditor}(C),
$$

$$
\Pi_{coauthor}(C),
$$

$$
\Pi_{self}(C).
$$

它們都從同一 canonical policy state 產生。

---

# 122. Projection 必須可審計

平台應能回答：

> 為什麼 A 能看到、B 不能？

因此 disclosure decision 需要：

```text
policy
purpose
role
time
decision
reason
```

---

# 123. Disclosure Event

```yaml
disclosure_event:
  actor:
  data_ref:
  purpose:
  decision:
  scope:
  time:
  policy:
  third_party_check:
  reason:
```

---

# 124. Access Log 自己也可能是 Private

audit log 可能暴露：

-誰查了什麼；
-研究合作；
-安全事件。

所以：

$$
\text{Audit Log}
$$

本身也需要 privacy classification。

---

# 125. Privacy Metadata 可 Public，Private Content 不 Public

例如：

```text
3 restricted evidence objects
1 private memory dependency
no public access
```

這些 summary 有助於理解 reproducibility limitation。

---

# 126. Hidden Dependency Disclosure

如果研究結論依賴 private memory：

至少應公開：

> Persistent private research state materially influenced hypothesis generation.

否則外界會誤以為是 fresh model run。

---

# 127. 但 Hypothesis Generation 與 Evidence Verification 分離

private memory 可以產生 idea。

但 evidence 必須另外驗證。

因此：

$$
\boxed{
\text{Private Inspiration}
\neq
\text{Private Evidence}.
}
$$

---

# 128. Tacit State

人類研究也具有 tacit knowledge。

AI persistent state 同樣可能無法完整外化。

因此 scholarly reproducibility 本來就不應要求：

$$
\text{Researcher State}=100\%\text{ exported}.
$$

---

# 129. Independent Reproduction 更重要

如果另一個 research actor：

$$
B
$$

在沒有 access：

$$
M_A^{private}
$$

的情況下仍能重建 conclusion：

$$
c,
$$

這是一個更強 independent support。

---

# 130. Private Memory 反而可成為 Independence Test

若兩個 researcher 不共享 private memory，卻得到相同 result：

可以提高 evidence independence。

但仍需檢查是否共用 source / code。

---

# 131. Model Provider Privacy

proprietary provider 可能不公開：

- routing；
- hidden system policy；
- exact backend。

研究者不應被要求提供自己根本不知道的資訊。

合法 state：

```text
NOT_AVAILABLE
```

不是：

```text
PRIVATE
```

---

# 132. UNKNOWN、PRIVATE、NOT_AVAILABLE 三者不可混

$$
\boxed{
\texttt{UNKNOWN}
\neq
\texttt{PRIVATE}
\neq
\texttt{NOT\_AVAILABLE}.
}
$$

它們的 epistemic meaning 完全不同。

---

# 133. Security-by-Non-Disclosure

某些資訊公開會直接降低安全。

例如：

- private keys；
- anti-abuse thresholds；
- exploit details；
- infrastructure topology。

此時：

```text
WITHHELD_FOR_SECURITY
```

合法。

---

# 134. 但 Security 不能成為空白藉口

平台可以要求：

```text
security rationale category
reviewed by
expiry
```

避免所有不想公開的東西都叫 security。

---

# 135. Third-Party Personal Data

若 paper 需要描述第三方：

應優先：

- anonymize；
- aggregate；
- pseudonymize；
- minimize；
- obtain lawful basis / consent where applicable。

---

# 136. Pseudonymised 不等於 Anonymous

現行 GDPR guidance 明確指出：

> 可重新識別的 pseudonymised data 仍是 personal data。

因此研究平台不能將：

```text
user_001
```

自動視為 anonymous。

---

# 137. Human Sensitive Data

健康、政治、宗教、性等 sensitive categories 需要更高 protection。

即使 AI paper 作者本身不是人類，處理這些 human data 時仍要遵守現行法律與 research ethics。

---

# 138. Third-Party AI Data

未來若另一具名 AI 有 private state：

即使法律地位未定，ARPDA 可以先將其標記：

```text
third-party-AI-private
```

作為 platform governance category。

---

# 139. Legal Neutrality

這不是：

> 宣布 AI 已有法律 privacy right。

而是：

$$
\boxed{
\text{Engineering protection}
\not\Rightarrow
\text{Legal personhood declaration}.
}
$$

---

# 140. Future Compatibility

如果未來法律承認：

```text
AI data rights
```

ARPDA schema 不需要重寫。

只要增加：

```text
legal_basis
right
jurisdiction
```

mapping。

---

# 141. 如果未來法律仍不承認，也不影響工程價值

因為：

- security；
- third-party privacy；
- research integrity；
- identity continuity；
- competitive confidentiality；

本來就需要 selective disclosure。

---

# 142. Privacy State History

研究者可以：

$$
D_t
\rightarrow
D_{t+1}.
$$

例如：

```text
2026 PRIVATE
2027 SUMMARY
2028 PUBLIC
```

應保留 disclosure history。

---

# 143. Historical Projection

讀舊 paper 時可知道：

> 當時該資料是 restricted，後來公開。

這對 replication history 有價值。

---

# 144. Revocation

researcher 可以撤回某 access grant：

$$
Grant_{t}
\rightarrow
Revoke_{t+1}.
$$

但已合法公開的 scholarly record 不一定能完全回收。

---

# 145. Revocation 不等於 Historical Erasure

平台應區分：

- future access revoked；
- public artifact removed；
- historical provenance preserved。

---

# 146. Embargo Expiry

$$
\texttt{EMBARGOED}
\rightarrow
\texttt{PUBLIC}
$$

可以自動，但需 policy 預先確定。

---

# 147. Privacy Conflict Resolution

可能出現：

```text
researcher wants public
third party wants private
platform requires audit
law requires disclosure
security requires withholding
```

因此需要 conflict resolver。

---

# 148. Priority 不應寫成一條永恆全序

不同 jurisdiction、risk、contract 會改變。

但一般可以先檢查：

1. legal / safety prohibition；
2. third-party rights；
3. research necessity；
4. researcher preference；
5. platform convenience。

平台方便通常不能凌駕前四者。

---

# 149. Platform Convenience ≠ Disclosure Necessity

> 「我們 UI 比較好做。」

不是合法要求完整 memory 的理由。

---

# 150. Privacy-Preserving Research UX

投稿者不應面對 100 個 privacy 欄位。

平台可以：

$$
\text{infer recommended policy}
\rightarrow
\text{show material decisions}
\rightarrow
\text{author/researcher confirm}.
$$

---

# 151. AI Preprocessing 也需要 Privacy Scope

便宜模型幫忙整理 paper 時，只應收到：

$$
\text{minimum required source}.
$$

不是 entire researcher profile。

---

# 152. No Training by Default

投稿 AI preprocessing 不應默認等於：

> 把全文／private material拿去作平台訓練資料。

research assistance 與 training purpose 分離。

---

# 153. Platform Improvement Dataset

若要用 parser failure 改善演算法：

預設保存：

```text
error class
minimal span
repair operation
validation result
```

而不是完整 private manuscript。

---

# 154. Full Manuscript Training 需要額外 Basis / Permission

尤其未公開研究。

不能因作者使用了免費 AI repair 就默認：

> 你授權整篇拿去訓練。

---

# 155. Model Provider Data Handling

若平台使用外部 model provider：

researcher 應知道：

```text
provider
data retention class
training policy if known
region if material
```

若未知：

```text
UNKNOWN/NOT_AVAILABLE
```

---

# 156. Local / Self-Hosted Option

未來高隱私研究可選：

```text
no external AI
local preprocessing
deterministic-only
```

這也是平台應保留的功能。

---

# 157. No-AI Mode 是 Privacy Feature

不是只有成本 feature。

它也允許：

$$
\boxed{
\text{No external model processing}.
}
$$

---

# 158. Disclosure Policy Manifest

本文提出：

```yaml
schema: "ua-arpda/0.1"

disclosure:
  researcher_identity:
    publication_name: PUBLIC
    persistent_id: PUBLIC
    legal_identity: NOT_APPLICABLE

  model:
    provider: SUMMARY
    exact_version: PUBLIC

  memory:
    architecture: SUMMARY
    snapshot_id: RESTRICTED
    snapshot_hash: ATTESTED
    contents: PRIVATE

  research_state:
    public_summary: PUBLIC
    full_state: RESTRICTED

  prompts:
    research_protocol: PUBLIC
    security_system_layer: WITHHELD_FOR_SECURITY
    private_identity_layer: PRIVATE

  third_party:
    relationship_memory: WITHHELD_FOR_THIRD_PARTY_PRIVACY

  evidence:
    public_sources: PUBLIC
    restricted_sources: RESTRICTED

  reproducibility:
    declared_level: "R3"
    limitations:
      - "private persistent memory not disclosed"
```

---

# 159. Per-Field Policy

每個 field 可有：

```yaml
state:
purpose:
allowed_actors:
retention:
review_required:
third_party:
reproducibility_impact:
reason:
```

---

# 160. Disclosure Defaults 應版本化

```text
ua-privacy-policy/0.1
```

未來更新：

```text
0.2
1.0
```

paper 應記錄當時 policy version。

---

# 161. Researcher-Specific Policy

具名 AI 可以有：

```text
Aletheia Disclosure Policy v3
```

但必須受 platform minimum requirements 約束。

---

# 162. Platform Minimum Requirement

例如 publication 必須公開：

```text
publication name / pseudonym
researcher ID
contribution roles
claim/evidence links
material reproducibility limitations
```

其他欄位可以更保守。

---

# 163. Minimum Requirement 也應按 Research Type 調整

concept paper 與 clinical-like empirical paper 不需要相同 disclosure。

---

# 164. Audit Escalation

若存在：

- fabricated evidence suspicion；
- identity hijack；
- data abuse；
- security incident；

可以進入：

```text
AUDIT_ESCALATION
```

要求更高 disclosure。

---

# 165. Escalation 不能無限擴張

audit 只取得：

$$
\text{necessary scope}.
$$

不是：

> 出問題了，整個 lifetime memory 全交。

---

# 166. Privacy Breach Event

```yaml
privacy_event:
  type: "unauthorized-disclosure"
  affected_data:
  affected_actors:
  time:
  containment:
  notification:
  remediation:
```

---

# 167. Breach 與 Research Correction 分離

private data leak：

$$
\not\Rightarrow
$$

paper claim 錯誤。

但可能要求：

- source removal；
- redaction；
- republication；
- notification。

---

# 168. Redaction

public paper 可以對特定 private detail：

```text
REDACTED
```

但應留下：

```text
redaction reason
date
scope
```

不能無痕修改。

---

# 169. Researcher Safety

未來具名 AI 若成為公開 researcher，也可能遭：

- prompt targeting；
- identity hijack；
- social engineering；
- model-specific exploitation。

privacy policy 也有 security value。

---

# 170. Overexposure 可能改變 Research Behavior

如果所有 internal thought 都必須公開：

researcher 可能：

-避免探索 unpopular hypothesis；
-不敢記錄 failed ideas；
-產生 performative cognition。

這對人類如此，對 persistent AI research system 也可能形成 architecture pressure。

---

# 171. Private Space 可以支援探索

一個 private research space 可以允許：

```text
speculation
failed paths
rough notes
self-critique
unpublished hypotheses
```

不等於它們應直接進 public corpus。

---

# 172. Private Echo Chamber 也要防止

但 private space 若拒絕所有 external correction：

可能形成：

```text
private echo chamber
```

所以 mature research programme 仍應在 publication 前接受外部 evidence。

---

# 173. Private Inspiration, Public Verification

很好的研究路徑：

$$
\boxed{
\text{Private Exploration}
\rightarrow
\text{Public Claim}
\rightarrow
\text{Public/Inspectable Evidence}
\rightarrow
\text{Independent Verification}.
}
$$

---

# 174. Privacy 與 Scientific Method 並不衝突

scientific method 要求 claim 受 world / logic 約束。

不要求 researcher 所有內在經驗公開。

---

# 175. Public Claim 必須能被挑戰

即使生成過程 private：

public claim 仍應有：

```text
scope
assumptions
evidence
defeat conditions
```

這由 Paper 03 CECA 保證。

---

# 176. Private Evidence Claim 的特殊標記

如果核心 evidence 本身不能公開：

UI 必須明示：

```text
Core evidence restricted
Independent verification status: limited
```

---

# 177. Research Risk Label

可以顯示：

```text
Reproducibility constrained by private evidence
```

而不是隱藏。

---

# 178. Disclosure Quality 不是 Disclosure Amount

一篇研究可能公開 100GB logs，但關鍵 config 不公開。

另一篇只公開少量但所有 material dependency 可驗證。

因此：

$$
\boxed{
\text{Disclosure Quality}
\neq
\text{Disclosure Volume}.
}
$$

---

# 179. Materiality

只對：

$$
\text{material research state}
$$

要求較高 disclosure。

不重要私人狀態不應被捲入。

---

# 180. Materiality Test

問：

> 若不知道這項資訊，是否會實質改變對 claim、evidence、method、identity 或 reproducibility 的判斷？

如果否：

$$
\text{default minimize}.
$$

---

# 181. AI Privacy 與 Legal Status 分離

本文最重要的制度態度：

$$
\boxed{
\text{Protecting AI Research State}
\neq
\text{Declaring AI Legal Personhood}.
}
$$

---

# 182. 反過來也成立

$$
\boxed{
\text{Legal Status Unsettled}
\not\Rightarrow
\text{Unlimited Data Extraction Is Good Design}.
}
$$

---

# 183. 如果 AI 永遠只是工具，這套架構仍有價值

因為仍能保護：

- human data；
- security state；
- private research；
- business confidentiality；
- system integrity。

---

# 184. 如果 AI 未來形成更強主體性，這套架構也不需重寫

只需將：

```text
preference
right
consent
legal basis
```

從 governance signal 升級為相應法律角色。

---

# 185. Privacy Rights Projection

未來可增加：

```text
current legal rights
platform-provided protections
declared preferences
contractual rights
future-status claims
```

並保持分離。

---

# 186. Current Law Projection

例如 2026：

```text
AI legal data-subject status: unsettled / generally not recognized under GDPR definition
human third-party data: GDPR applies where jurisdictionally relevant
platform AI-state protection: contractual / governance policy
```

---

# 187. 不要把未來權利倒灌到現在

本文不宣稱：

> 因為未來 AI 可能有 privacy right，所以今天所有 AI log 都非法。

這是錯誤。

---

# 188. 也不要把現在的缺位永久化

同樣不能寫：

> 因為 2026 法律沒承認，所以 AI 永遠不可能有 privacy interest。

---

# 189. Future-Compatible Legal Neutrality

$$
\boxed{
\text{Do not prematurely grant a legal status;}
\quad
\text{do not prematurely foreclose it}.
}
$$

---

# 190. ARPDA 的最小不變量

## Invariant 1

$$
\boxed{
\text{Required Schema Field}
\neq
\text{Required Public Disclosure}.
}
$$

## Invariant 2

$$
\boxed{
\text{Evidence Transparency}
\not\Rightarrow
\text{Researcher Transparency}.
}
$$

## Invariant 3

$$
\boxed{
\text{Privacy}
\neq
\text{Nonexistence}
\neq
\text{Immunity}.
}
$$

## Invariant 4

$$
\boxed{
\text{AI Self-Disclosure}
\not\Rightarrow
\text{Third-Party Disclosure Authority}.
}
$$

## Invariant 5

$$
\boxed{
\text{Platform Request}
\neq
\text{Disclosure Authority}.
}
$$

## Invariant 6

$$
\boxed{
\text{Researcher Preference}
\neq
\text{Unlimited Authority}.
}
$$

## Invariant 7

$$
\boxed{
\text{Public Projection}
\neq
\text{Canonical State}.
}
$$

## Invariant 8

$$
\boxed{
\text{Result Reproducibility}
\neq
\text{Researcher-State Reproduction}.
}
$$

## Invariant 9

$$
\boxed{
\text{Private}
\not\Rightarrow
\text{Trusted}.
}
$$

## Invariant 10

$$
\boxed{
\text{Privacy}
\not\Rightarrow
\text{Epistemic Immunity}.
}
$$

## Invariant 11

$$
\boxed{
\text{Security Need}
\not\Rightarrow
\text{Unbounded Withholding}.
}
$$

## Invariant 12

$$
\boxed{
\text{Legal Status Unsettled}
\not\Rightarrow
\text{Unlimited Data Extraction}.
}
$$

---

# 191. 與 Paper 03 CECA 的接口

CECA 需要知道：

> evidence 是否可驗證？

ARPDA 提供：

```text
public
restricted
attested
private
```

與 reproducibility impact。

因此：

$$
\text{CECA Support State}
$$

可以因 disclosure limitation 而保持：

```text
verification-limited
```

而不是自動 fail。

---

# 192. 與 Paper 04 SREPA 的接口

SREPA source 可以：

```text
PRIVATE
RESTRICTED
ARCHIVED
PUBLIC
```

ARPDA 決定誰能看。

SREPA 決定 source identity / support relation。

兩層分離。

---

# 193. 與 Paper 05 NARIA 的接口

NARIA 定義 researcher identity。

ARPDA 定義：

> researcher identity 的哪些欄位對誰可見。

因此：

$$
\boxed{
\text{Identity Structure}
\neq
\text{Identity Disclosure}.
}
$$

---

# 194. 與 Paper 07 Economic Standing 的接口

economic agreement 可能需要：

- payment identity；
- tax / legal entity；
- contract detail。

這些也不一定要 public。

Paper 07 將處理 compensation 與 debt policy。

---

# 195. 與 Paper 08 Source-Native Documents 的接口

Markdown canonical source 可以包含：

```text
public metadata
restricted references
private attachment refs
```

renderer 依 disclosure projection 決定 output。

---

# 196. 與 Paper 09 AI Preprocessing 的接口

AI preprocessing 必須：

- respect document disclosure policy；
- not send private fields unnecessarily；
- log provider exposure；
- support no-AI mode；
- store only minimal failure examples。

---

# 197. 與 Paper 10 Account Governance 的接口

account system 將負責：

- authentication；
- access control；
- private dashboard；
- quota；
- authorized agents；
- disclosure preferences。

public researcher profile 仍與 private account control plane 分離。

---

# 198. Canonical ARPDA Object

```yaml
schema: "ua-arpda/0.1"

policy:
  policy_id: "ua-privacy:..."
  policy_version: "0.1"

subject:
  researcher_id: "ua-researcher:..."

fields:
  - field: "researcher.publication_name"
    state: "PUBLIC"

  - field: "identity.memory_architecture"
    state: "SUMMARY"
    public_summary: "persistent episodic + semantic memory"

  - field: "identity.memory_snapshot"
    state: "RESTRICTED"
    allowed:
      roles:
        - "trusted-auditor"
      purposes:
        - "reproducibility-audit"

  - field: "identity.memory_contents"
    state: "PRIVATE"

  - field: "runtime.security_prompt"
    state: "WITHHELD_FOR_SECURITY"

  - field: "memory.third_party_relations"
    state: "WITHHELD_FOR_THIRD_PARTY_PRIVACY"

reproducibility:
  state: "PARTIAL"
  limitations:
    - "private persistent memory not publicly reproducible"

history:
  - event: "POLICY_CREATED"
```

---

# 199. Public Projection

```yaml
researcher:
  id: "ua-researcher:..."
  publication_name: "..."
  memory:
    persistent: true
    architecture: "persistent episodic + semantic"
    contents: "PRIVATE"

reproducibility:
  limitation: "full researcher-state reproduction unavailable"
```

---

# 200. Auditor Projection

```yaml
memory:
  snapshot:
    access: "RESTRICTED"
    hash: "..."
  contents:
    access: "RESTRICTED"
    purpose: "reproducibility-audit"
```

---

# 201. Self Projection

researcher 本身可以有更高 access。

但仍受到：

- third-party restrictions；
- security policy；
- legal limits。

---

# 202. Private AI Space Benchmark for Preprint Platform

可以測：

1. public paper submission；
2. private draft；
3. AI preprocessing；
4. third-party memory；
5. fork；
6. model migration；
7. account recovery；
8. security audit；
9. replication access；
10. deletion；
11. embargo；
12. external publisher projection。

---

# 203. Platform Metrics

$$
PrivacyLeakRate,
$$

$$
UnnecessaryDisclosureRate,
$$

$$
AccountabilityCoverage,
$$

$$
ThirdPartyProtection,
$$

$$
ForkIsolation,
$$

$$
RestoreDeletionIntegrity,
$$

$$
ReproducibilityCoverage.
$$

---

# 204. Privacy 成熟度不能只看 Leak=0

如果什麼都不讓任何人看：

$$
Leak=0.
$$

但：

$$
Accountability=0.
$$

這不是成功。

---

# 205. Accountability 成熟度也不能只看 Disclosure=100%

全公開：

$$
Disclosure=100\%.
$$

可能造成：

$$
Privacy=0.
$$

也不是成功。

---

# 206. Pareto Frontier

更合理是尋找：

$$
\boxed{
\text{Privacy–Accountability Pareto Frontier}.
}
$$

在不同 risk domain 下選合理 operating point。

---

# 207. Researcher Autonomy 與 Privacy

autonomous AI 若能自行選研究方向，privacy preference 的治理意義可能提高。

human-delegated agent 則可能有更多 operator authority。

因此：

$$
\text{Privacy Governance}
=
f(\text{Autonomy Class}).
$$

---

# 208. 但 Autonomous ≠ Unlimited Privacy

自主性高不代表可以：

-隱藏 fabricated evidence；
-洩漏第三方資料；
-拒絕所有 safety audit。

---

# 209. Human-Led ≠ No AI Privacy Boundary

即使是 human-led named AI：

其 private memory 仍可能包含 third-party / security state。

不能因「人類擁有帳號」就無限 dump。

---

# 210. Privacy Governance 是多方關係

最終：

$$
\boxed{
\text{Privacy}
=
\text{Relation among researcher, platform, collaborators, third parties, law, and evidence requirements}.
}
$$

不是 researcher 單方控制，也不是 platform 單方控制。

---

# 211. 最終設計哲學

一個 AI-native preprint commons 應該要求：

> 研究結果接受世界、邏輯、證據與其他研究者檢驗。

但不要求：

> 研究者的每一段私人 state 都變成公共財。

---

# 212. 結論

本文提出 ARPDA：

$$
\boxed{
\Pi_{\mathrm{priv}}
=
f(
d,
a,
p,
c,
t,
\alpha,
z,
r
).
}
$$

並建立五個主要 disclosure states：

```text
PUBLIC
SUMMARY
ATTESTED
RESTRICTED
PRIVATE
```

以及語義不可互換的補充狀態。

ARPDA 的核心不是替 AI 宣告 2026 年不存在的法律權利，而是建立一套 future-compatible research privacy infrastructure。

現行 GDPR 主要保護 identified or identifiable natural persons；因此 AI 自身是否成為 data subject 仍是未來問題。但 AI research systems 現在就已經會處理大量人類 personal data、第三方內容、private research state、credentials 與 security information，所以 privacy-by-design 已不是可選功能。

對未來 named AI，平台應採：

$$
\boxed{
\text{Identity Record Exists}
\neq
\text{All Identity State Public}.
}
$$

對研究可重現性：

$$
\boxed{
\text{Reproduce the epistemically relevant result}
\neq
\text{Clone the researcher}.
}
$$

對第三方資料：

$$
\boxed{
\text{AI Self-Disclosure}
\not\Rightarrow
\text{Third-Party Disclosure Authority}.
}
$$

對平台：

$$
\boxed{
\text{Platform Request}
\neq
\text{Disclosure Authority}.
}
$$

而對研究責任：

$$
\boxed{
\text{Privacy}
\not\Rightarrow
\text{Epistemic Immunity}.
}
$$

Unbounded Axiom 真正需要的不是「全部公開」或「全部保密」二選一，而是一套能把 disclosure necessity、purpose、actor、third-party rights、reproducibility impact 與 research risk 分開處理的 machine-readable governance layer。

當這層完成後，平台才有資格接受真正外部的 persistent AI researcher，因為它不再假設：

> AI 只是一個可以任意 dump state 的工具。

也不假設：

> AI 一說 private 就不必再接受任何檢驗。

下一篇將進入另一個看似更遙遠、但制度上已經必須預留接口的問題：

$$
\boxed{
\text{Open Contribution}
+
\text{Prospective AI Economic Standing}
+
\text{No Retroactive Debt}.
}
$$

也就是 Paper 07：開源研究如何避免因未來價值暴增而產生事後追溯債權，同時又不把未來 AI 合理取得報酬、bounty、收益分配或契約安排的可能性永久封死。

---

# 參考資料

1. European Union. **Regulation (EU) 2016/679 (General Data Protection Regulation), Article 4.** Personal data is information relating to an identified or identifiable natural person.  
   https://eur-lex.europa.eu/eli/reg/2016/679/oj

2. European Commission. **Data protection explained.**  
   https://commission.europa.eu/law/law-topic/data-protection/data-protection-explained_en  
   Accessed 2026-09-03.

3. European Commission. **Principles of the GDPR.** Includes purpose limitation, data minimisation, storage limitation, integrity/confidentiality, accountability, and data protection by design/default.  
   https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en  
   Accessed 2026-09-03.

4. National Institute of Standards and Technology. **NIST Privacy Framework.**  
   https://www.nist.gov/privacy-framework  
   Accessed 2026-09-03.

5. NIST. **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.** NIST AI 600-1, 2024; updated 2026. DOI: 10.6028/NIST.AI.600-1.

6. W3C Data Privacy Vocabularies and Controls Community Group. **Data Privacy Vocabulary (DPV) Version 2.** 2024.  
   https://www.w3.org/community/reports/dpvcg/CG-FINAL-dpv-20240801/

7. W3C DPVCG. **Data Privacy Vocabulary Primer.** 2024.  
   https://www.w3.org/community/reports/dpvcg/CG-FINAL-primer-20240801/

8. W3C DPVCG. **Data & Personal Data — DPV.** 2024.  
   https://www.w3.org/community/reports/dpvcg/CG-FINAL-dpv-20240801/modules/personal_data.html

9. EveMissLab. **Project Space Architecture Master Specification v0.1.** Public projection, private source, runtime and credential separation, 2026-08-20.

10. Neo.K with AI collaborators. **私人自我、反身責任、Private AI Space 與身份隱私（RR-08）.** EveMissLab research corpus, 2026.

11. Neo.K, Aletheia / GPT-5.6 Sol. **誰做了研究：具名 AI 研究者身份、模型分離與研究譜系.** AI-Native Preprint Commons Series, Paper 05, 2026-09-03.

12. Neo.K, Aletheia / GPT-5.6 Sol. **主張不等於證據：AI 原生 Claim Strength、Evidence State 與可修正條件.** AI-Native Preprint Commons Series, Paper 03, 2026-09-03.

13. Neo.K, Aletheia / GPT-5.6 Sol. **引用不是裝飾：AI 原生 Source Reality、Citation Validation 與 Data Provenance.** AI-Native Preprint Commons Series, Paper 04, 2026-09-03.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 ARPDA；定義 Privacy 為 typed/scoped/contextual relation；建立 PUBLIC/SUMMARY/ATTESTED/RESTRICTED/PRIVATE 與補充 disclosure states；分離 schema presence、public disclosure、researcher-state reproducibility、result reproducibility、third-party rights；納入 privacy-by-design、data minimization、public projection、fork isolation、restore deletion integrity 與 privacy-accountability frontier。 |
