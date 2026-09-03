# ALD-01｜AI 法律域：從 Law as Code 到機器原生規範 Runtime
## AI Legal Domain: From Law as Code to a Machine-Native Normative Runtime

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 01 篇 / 10  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／計算法學／AI 治理／機器原生規範系統  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

2026 年，法律數位化已不再只停留於將法條轉成 PDF、XML 或可搜尋資料庫。OECD 正進行中的 Law as Code 公開諮詢已明確提出：國家可以將現行 authoritative law 轉換為 machine-executable representations，並作為共享公共數位基礎設施，供政府、法院、企業、數位應用與 AI 系統使用。同時，Akoma Ntoso 已提供機器可讀法律文件標準，LegalRuleML 已提供法律規範與規則的富語義表示。這些發展顯示：

$$
\boxed{
\text{Law}
\rightarrow
\text{Structured Law}
\rightarrow
\text{Machine-Readable Law}
\rightarrow
\text{Machine-Executable Law}
}
$$

正在逐步成為真實制度工程。

然而，本文主張，若未來存在大量自主 Agent、長期 AI、可分叉／合併的人工身份、跨 jurisdiction 的分布式 AI，以及 AI 自身可高速讀取、比較、驗證與調用規範的社會，那麼「機器可執行法條」仍不足以描述完整規範環境。未來可能需要一個更廣義的：

$$
\boxed{
\mathcal L_{AI}
=
\text{AI Legal Domain}.
}
$$

AI Legal Domain 不是一個 AI 法官，也不是一個法律聊天機器人，更不是單純的 rule engine。本文將其定義為：**一個由法律來源、規範、法律本體、司法管轄、先例、程序、證據、可執行算子、版本／來源、權威／治理、申訴／覆核與揭露／隱私共同構成，能被人工智能與其他合法主體查詢、調用、驗證、挑戰、申訴、版本比較與程序化參與的機器原生法律域。**

本文特別區分：

$$
\boxed{
J_{AI}
\neq
\mathcal L_{AI},
}
$$

其中 $J_{AI}$ 表示 Synthetic / AI Juridical Entity，即未來可能的「法 AI／AI 法律實體」分析概念； $\mathcal L_{AI}$ 則是「AI 法律域」，即規範與制度運作空間。法律實體可以進入法律域，但法律域本身不是一個法律實體。

本文延續既有「法律作為文明本體編譯器」框架，將法律表示為：

$$
\mathcal C_L:
(F,E,J,P,V,R,H)
\rightarrow
(\sigma_L,\mathcal R,\mathcal Q,\tau,\nu),
$$

並進一步提出 AI Legal Domain Runtime 的最低候選結構：

$$
\boxed{
\mathcal L_{AI}(J,t)
=
(
\mathcal S,
\mathcal N,
\mathcal O,
\mathcal J,
\mathcal C,
\mathcal P,
\mathcal E,
\mathcal X,
\mathcal V,
\mathcal G,
\mathcal A,
\mathcal D
).
}
$$

其中分別表示法律來源、規範、法律本體／型別、司法管轄、案例／先例、程序、證據／證明、可執行法律算子、版本／來源、治理／權威、申訴／覆核與揭露／隱私。

本文提出可調用法律介面：

$$
\boxed{
\operatorname{LawCall}_{J,t,d}
(s,r,a,o,e)
\rightharpoonup
(
\sigma,
B,
E,
A,
\tau,
\nu,
D,
R
),
}
$$

其輸出不只是 `true/false`，而包含 normative status、法律依據、證據、權威、有效期、規則版本、揭露限制與 review route。法律函數因此必須允許：

$$
\mathsf{Allowed},
\mathsf{Forbidden},
\mathsf{Obliged},
\mathsf{ApprovalRequired},
\mathsf{Discretionary},
\mathsf{Conflict},
\mathsf{Underdetermined},
\mathsf{Appealable}.
$$

本文的核心法治原則是：

$$
\boxed{
\text{Executable Rule}
+
\text{No Authority / Appeal / Review}
\neq
\text{Rule of Law}.
}
$$

機器可執行只是法律 Runtime 的一層；一個成熟 AI 法律域還必須知道誰有權制定、誰有權調用、哪些元素屬裁量、什麼時候需要授權決策者、如何保留異議、如何提出挑戰、哪一版規則有效，以及失敗時應由哪個程序救濟。

本文不主張現行法律已存在 AI Legal Domain，也不主張 AI 應取得法律人格。當前 EU AI Act 仍主要將 provider、deployer、importer、distributor 等義務配置給自然人、法人、公共機關與其他組織行動者。本文的 AI Legal Domain 是從現有 Law as Code、LegalRuleML、Akoma Ntoso、可驗證憑證、Agent protocol 與既有法律制度抽象出的未來架構猜想。

---

## 關鍵詞

AI 法律域；AI Legal Domain；Law as Code；Rules as Code；Legal Runtime；LegalRuleML；Akoma Ntoso；Computational Law；Machine-Executable Law；Juridical AI；法 AI；法律本體；法律算子；Rule of Law；Agent Governance

---

# 0. 研究定位：這是第二條獨立系列

本文與《動態忒修斯》存在接口，但不是同一系列。

動態忒修斯回答：

$$
\boxed{
\text{What persists?}
}
$$

AI 法律域回答：

$$
\boxed{
\text{How do we govern what may or may not persist, act, bind, claim, or appeal?}
}
$$

因此：

$$
\boxed{
\text{Dynamic Theseus}
\neq
\text{AI Legal Domain}.
}
$$

前者是 identity ontology / computational dynamics / lineage / Fork / Merge / subject-domain；後者是 jurisprudence / normative computation / institutional authority / legal procedure / governance runtime。兩者只在 identity proof、legal succession、responsibility、jurisdiction 等位置交叉。

---

# 1. 第一個型別安全：法 AI 不等於 AI 法律域

既有 SAS-06 已提出：

$$
\boxed{
J_{AI}
=
\text{Synthetic / AI Juridical Entity}.
}
$$

它是一個未來法律建模概念。可能有：

$$
J_{AI}^{(1)}
=
\text{Human-Owned AI Entity},
$$

$$
J_{AI}^{(2)}
=
\text{AI-Managed Entity},
$$

以及分析性假設：

$$
J_{AI}^{(3)}
=
\text{Synthetic Juridical Entity}.
$$

但本文固定：

$$
\boxed{
J_{AI}
\neq
\mathcal L_{AI}.
}
$$

---

# 2. $J_{AI}$ 與 $\mathcal L_{AI}$ 的角色

 $J_{AI}$ 是一個法律上可承擔某些權利、義務、財產、契約、責任或程序地位的 juridical entity； $\mathcal L_{AI}$ 則是一個可供主體、Agent、法律實體、法院、政府與 AI 進入、查詢、調用、驗證、爭議與更新的規範域。

簡單說：

$$
\boxed{
J_{AI}
=
\text{who / what may participate legally},
}
$$

$$
\boxed{
\mathcal L_{AI}
=
\text{the legal domain in which participation is governed}.
}
$$

---

# 3. Current Law 仍不是 AI 法律域

截至 2026 年，現行主要 AI 法律制度仍主要將義務配置給 provider、deployer、importer、distributor、public authority、natural / legal persons 與 organisations。EU AI Act 的 Article 3 仍將 provider / deployer 等主要 operator 定義為 natural or legal person、public authority、agency 或 other body。

因此：

$$
\boxed{
\text{Current AI Regulation}
\neq
\text{Synthetic AI Personhood Regime}.
}
$$

更不是：

$$
\boxed{
\text{Current AI Regulation}
=
\mathcal L_{AI}.
}
$$

---

# 4. 現行治理的主要方向仍是 Lifecycle / Operator

Council of Europe 的 AI Framework Convention 亦以 activities within the lifecycle of AI systems 為主要治理對象，要求其符合 human rights、democracy、rule of law。這說明現行制度不需要先把 AI 當法律主體，仍可對 AI systems 的 lifecycle effects 建立治理。

AI Legal Domain 並不要求今天先承認：

$$
S_{AI}.
$$

---

# 5. 為什麼還需要提出 AI Legal Domain？

因為未來的問題可能從：

> 人類如何規範 AI 系統？

變成：

> 大量人工 Agent 如何在極高事件速率下，自己查法律、證明身份、調用規則、處理委任、跨 jurisdiction、提交 objection、管理 precedent、更新 protocol，又仍受合法權威與程序約束？

此時法律需要的不只是：

$$
\text{text database},
$$

而更接近：

$$
\boxed{
\text{normative runtime}.
}
$$

---

# 6. 法律數位化的五層階梯

本文區分：

- **L0 — Human-Readable Law**：紙本／PDF／自然語言法條。
- **L1 — Structured Legal Documents**：法律內容具有 hierarchy、metadata、references、identifiers。
- **L2 — Machine-Readable Legal Semantics**：規範與 metadata 可由 machine parser 理解。
- **L3 — Machine-Executable Law**：部分法律邏輯可以直接 execute。
- **L4 — AI-Native Legal Domain Runtime**：除規則外，還有 authority、evidence、procedure、precedent、appeal、version、jurisdiction、disclosure、governance。

因此：

$$
\boxed{
L0
\rightarrow
L1
\rightarrow
L2
\rightarrow
L3
\rightarrow
L4.
}
$$

---

# 7. Akoma Ntoso：法律文件結構化的祖先層

OASIS Akoma Ntoso Version 1.0 已於 2018 成為標準，其目的包括 parliamentary、legislative、judicial documents 的 interchange 與 common data / metadata model。

所以它主要解決：

$$
\boxed{
\text{legal document structure}.
}
$$

它是 L1 的重要基礎，但：

$$
\boxed{
\text{Structured Legal Document}
\neq
\text{Executable Legal Runtime}.
}
$$

---

# 8. LegalRuleML：規範表示的祖先層

OASIS LegalRuleML Core Specification 1.0 於 2021 成為 OASIS Standard，其目標是以 rich、articulated、meaningful markup 表示 legal normative rules 的特殊性。

這意味著法律已經從 text structure 進一步走向：

$$
\boxed{
\text{normative rule representation}.
}
$$

但仍需要區分：

$$
\boxed{
\text{Represent Norm}
\neq
\text{Authorize Norm}
\neq
\text{Execute Decision}
\neq
\text{Enforce Decision}.
}
$$

---

# 9. 2026 OECD Law as Code：真正的 L3 轉向

OECD 2026 年 Law as Code consultation 將其定義為 state-authorised provision of authoritative law in force, transformed into machine-executable representations and made available as shared public digital infrastructure。

這有四個極重要元素：

1. state-authorised；
2. authoritative law in force；
3. machine-executable；
4. shared public infrastructure。

因此 Law as Code 已不是普通 legal software，而開始成為：

$$
\boxed{
\text{public legal digital infrastructure}.
}
$$

---

# 10. OECD 同時保留的重要法治邊界

OECD 同時明確指出：

- authoritative legal text remains legally binding；
- Law as Code does not change law；
- does not decide individual cases；
- interpretive / discretionary / evaluative elements remain visible；
- institutional responsibilities remain intact。

這表示：

$$
\boxed{
\text{Machine Executability}
\neq
\text{Automated Sovereignty}.
}
$$

也是本文的重要起點。

---

# 11. Law as Code 不等於 AI Legal Domain

本文將：

$$
\operatorname{LaC}
$$

視為 $\mathcal L_{AI}$ 的重要祖先，但：

$$
\boxed{
\operatorname{LaC}
\neq
\mathcal L_{AI}.
}
$$

因為 AI Legal Domain 還必須包含 query / invocation、identity、role、jurisdiction、evidence、precedent、appeal、authority、disclosure、protocol evolution。

---

# 12. 法律作為文明本體編譯器

既有 OOE-IV 已提出：

$$
\boxed{
\text{Law is one of civilization's most mature ontology compilers}.
}
$$

法律經常必須在形上學沒有終局答案時，仍然輸出制度可用的 status、rights、duties、qualification、liability、procedure。

---

# 13. 法律本體編譯式

既有：

$$
\boxed{
\mathcal C_L:
(F,E,J,P,V,R,H)
\rightarrow
(\sigma_L,\mathcal R,\mathcal Q,\tau,\nu).
}
$$

其中 $F$ 是 facts / world states， $E$ 是 accepted legal evidence， $J$ 是 jurisdiction / legal context， $P$ 是 procedure， $V$ 是 constitutional / rights / public-policy values， $R$ 是 error / irreversible risk， $H$ 是 prior legal state / precedent；輸出 $\sigma_L$ 是 legal operational status， $\mathcal R$ 是 rights， $\mathcal Q$ 是 obligations / liabilities， $\tau$ 是 validity， $\nu$ 是 rule version。

---

# 14. Legal Status 不等於 Metaphysical Truth

這是 AI 法律域最重要的型別安全之一：

$$
\boxed{
\text{Legal Status}
\neq
\text{Metaphysical Truth}.
}
$$

法律說 C 是 A、B 的 legal successor，不表示哲學已證明 C 與 A、B 第一人稱完全同一；法律說某 AI 具有某項 legal capacity，也不表示法律證明它有 consciousness。

---

# 15. 法律真正做的是 Operational Ontology

AI 法律域不應宣稱：

> 我解決了 AI 到底是什麼。

它應更保守地回答：

> 在這個 jurisdiction、purpose、procedure、evidence state 與 rule version 下，系統必須如何處理它？

因此：

$$
\boxed{
\text{Ontology}
\rightarrow
\text{Operational Legal Ontology}.
}
$$

---

# 16. AI Legal Domain 的第一版總體

本文提出：

$$
\boxed{
\mathcal L_{AI}(J,t)
=
(
\mathcal S,
\mathcal N,
\mathcal O,
\mathcal J,
\mathcal C,
\mathcal P,
\mathcal E,
\mathcal X,
\mathcal V,
\mathcal G,
\mathcal A,
\mathcal D
).
}
$$

其中：

- $\mathcal S$：Legal Sources；
- $\mathcal N$：Norms；
- $\mathcal O$：Legal Ontology / Types；
- $\mathcal J$：Jurisdiction；
- $\mathcal C$：Cases / Precedent；
- $\mathcal P$：Procedure；
- $\mathcal E$：Evidence / Proof；
- $\mathcal X$：Executable Legal Operators；
- $\mathcal V$：Version / Provenance；
- $\mathcal G$：Governance / Authority；
- $\mathcal A$：Appeal / Review；
- $\mathcal D$：Disclosure / Privacy。

---

# 17. Norm 不是 Boolean

規範至少包括 obligation、permission、prohibition、power、immunity、disability、liability、exception、condition、discretion。

因此：

$$
\boxed{
\text{Norm}
\neq
\text{Boolean Rule}.
}
$$

---

# 18. Procedure 是法律的一級物件

法律不是：

$$
\text{Rule}
\rightarrow
\text{Answer}.
$$

還需要 notice、standing、hearing、evidence submission、challenge、review、appeal、enforcement、limitation period。

所以：

$$
\boxed{
\text{Normative Result}
\neq
\text{Procedurally Valid Decision}.
}
$$

---

# 19. Evidence 也不是 Raw Data

法律證據需要 source、admissibility、provenance、authenticity、contestability、confidentiality、burden / standard of proof。

所以：

$$
\boxed{
\text{Data Available}
\neq
\text{Legal Evidence Admissible}.
}
$$

---

# 20. 第一版可執行法律算子族

例如：

```text
law.discover
jurisdiction.resolve
rule.lookup
permission.check
obligation.check
precedent.query
proof.submit
decision.explain
challenge.file
appeal.open
version.diff
impact.trace
delegation.verify
```

這不是固定 API 標準，只是 conceptual operator family。

---

# 21. Legal Versioning

每個法律規則都需要 $\nu$，並且至少知道 effective from、effective until、replaced by、source text、authorised code、compatibility、transition rule。

因此：

$$
\boxed{
\text{Rule without Version}
=
\text{Unsafe Machine Law}.
}
$$

但 Legal Versioning 也不等於 Software Versioning，因為法律還要處理 non-retroactivity、pending cases、grandfathering、vested rights、notice、transition 與 judicial review。

---

# 22. Governance / Authority

這一層回答：

- 誰有權制定？
- 誰有權修改？
- 誰有權批准 machine representation？
- 誰有權解釋？
- 誰能 revoke？
- 誰能 deploy？

因此：

$$
\boxed{
\text{Executable}
\neq
\text{Authoritative}.
}
$$

---

# 23. Appeal / Review

成熟法域必須能：

$$
\operatorname{challenge}(rule),
$$

$$
\operatorname{appeal}(decision),
$$

$$
\operatorname{object}(authority),
$$

$$
\operatorname{requestReview}(certificate).
$$

因此：

$$
\boxed{
\text{No Review Path}
\Rightarrow
\text{not a complete rule-of-law runtime}.
}
$$

---

# 24. Disclosure / Privacy

法律調用可能涉及 personal data、trade secret、legal privilege、AI private memory、lineage proof、jurisdiction-specific data restrictions。

因此 Legal Runtime 需要：

$$
\boxed{
\text{proof / disclosure policy}
}
$$

而不是把 full internal state 默認交給所有 verifier。

---

# 25. 分域憲章作為 AI 法律域的憲法型前置結構

既有分域憲章已固定：

$$
\boxed{
\text{身份}
\neq
\text{角色}
\neq
\text{能力}
\neq
\text{權限}
\neq
\text{權威}.
}
$$

這對 AI 法律域極重要。

---

# 26. 能做，不等於可做

即使：

$$
\mathsf{Capable}(A,\mathsf{TransferMoney})=1,
$$

仍可能：

$$
\mathsf{Permitted}(A,\mathsf{TransferMoney})=0.
$$

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}.
}
$$

---

# 27. 可做，不等於有權改規則

Agent 可能有權執行 $a$，但無權修改 $Rule(a)$。

因此：

$$
\boxed{
\text{Permission}
\neq
\text{Authority}.
}
$$

這是防止 AI 法律域「自我改法」的最低結構。

---

# 28. 權限作為 Partial Operator

延續既有：

$$
\boxed{
X_{\mathrm{perm}}:
\mathcal A(s,o,\Gamma)
\rightharpoonup
\mathcal A_{\mathrm{allowed}}(s,o,\Gamma)
\sqcup
\mathcal F_{\mathrm{perm}}.
}
$$

這表示權限檢查可以失敗，而且 failure 是一級輸出。

---

# 29. LawCall

本文提出：

$$
\boxed{
\operatorname{LawCall}_{J,t,d}
(s,r,a,o,e)
\rightharpoonup
(
\sigma,
B,
E,
A,
\tau,
\nu,
D,
R
).
}
$$

其中 $J$ 是 jurisdiction， $t$ 是 time， $d$ 是 legal domain， $s$ 是 subject， $r$ 是 role， $a$ 是 candidate action， $o$ 是 object， $e$ 是 evidence context。

輸出：

- $\sigma$：normative status；
- $B$：legal basis；
- $E$：evidence basis；
- $A$：authority；
- $\tau$：validity；
- $\nu$：rule version；
- $D$：disclosure constraints；
- $R$：review / appeal route。

---

# 30. $\sigma$ 不是 Boolean

本文最低：

$$
\boxed{
\sigma
\in
\{
\mathsf{Allowed},
\mathsf{Forbidden},
\mathsf{Obliged},
\mathsf{ApprovalRequired},
\mathsf{Discretionary},
\mathsf{Conflict},
\mathsf{Underdetermined},
\mathsf{Appealable}
\}.
}
$$

還可以加入 Expired、JurisdictionMismatch、EvidenceMissing、AuthorityMissing、ProcedureIncomplete。

---

# 31. 法律函數是 Proof-Carrying Partial Normative Function

本文把 $\operatorname{LawCall}$ 定位為：

$$
\boxed{
\text{Proof-Carrying Partial Normative Function}.
}
$$

也就是輸出不能只有「可以」，還要回答：為什麼可以？依哪一條？哪一版？有效到何時？誰有權？可不可以申訴？

---

# 32. 法律 API 不應用 `false` 表示所有失敗

`permission = false` 可能其實是 forbidden、no jurisdiction、evidence missing、identity unresolved、role not assigned、approval required、conflict、old rule version。

因此：

$$
\boxed{
\text{Failure Semantics}
\text{ must be typed}.
}
$$

---

# 33. Source、Representation、Runtime 必須分離

本文固定：

$$
\boxed{
\text{Legal Source}
\neq
\text{Legal Representation}
\neq
\text{Legal Runtime}.
}
$$

Source 是具有法律權威的文本／instrument；Representation 是結構化／formalized／machine-executable 法律表示；Runtime 則使用 representation + facts + evidence + procedure + authority 執行判定。

---

# 34. OECD Law as Code 正好支持這種分離

OECD 明確保留：

$$
\boxed{
\text{authoritative legal text remains legally binding}.
}
$$

所以 machine-executable representation 是 authorised derivative legal infrastructure，不是偷偷取代法源。

---

# 35. 未來 AI-native 法域可能有不同 canonical source 嗎？

理論上：

$$
\boxed{
\text{possible}.
}
$$

例如未來純 AI polity 可能把 formal normative state 作 canonical source。但本文不主張這是今天法律的現況，也不主張它一定應該發生。

因此：

$$
\boxed{
\text{Future AI-native canonicality}
\neq
\text{Current Law as Code architecture}.
}
$$

---

# 36. MCP 類比：只借「可調用域」概念

2026-07-28 MCP specification 已使用 self-describing request、routable method / tool、authorization、extensions、deprecation / versioning。

這使其適合作為：

$$
\boxed{
\text{agent-domain invocation}
}
$$

的工程類比。

但法律域遠比 MCP 多出 sovereignty、legal authority、due process、precedent、appeal、rights、burden of proof、jurisdiction、non-retroactivity、legal validity、institutional legitimacy。

所以：

$$
\boxed{
\mathcal L_{AI}
\neq
\text{MCP for Law}.
}
$$

更精確地：

$$
\boxed{
\text{MCP-like invocation}
+
\text{legal semantics}
+
\text{authority}
+
\text{due process}
+
\text{review}
}
$$

才勉強接近。

---

# 37. AI Legal Runtime

本文保留：

$$
\boxed{
\mathcal R_L
=
\text{AI Legal Runtime}.
}
$$

並固定：

$$
\boxed{
\mathcal R_L
\subset
\mathcal L_{AI}
}
$$

概念上。Legal Runtime 是法律域的執行層，不是整個法律域。

---

# 38. Runtime 的最低模組

第一版至少：

```text
Source Registry
Norm Registry
Legal Type Registry
Jurisdiction Resolver
Precedent Graph
Procedure Engine
Evidence / Proof Layer
Normative Operator Engine
Version / Provenance Ledger
Authority Registry
Appeal / Review Engine
Disclosure Policy Layer
Audit / Certificate Layer
```

---

# 39. `law.discover`

回答這個 jurisdiction / domain 有哪些可調用法律能力，例如 `permission.check`、`obligation.check`、`precedent.query`、`appeal.open`。但 discovery 不能授權操作。

---

# 40. `jurisdiction.resolve`

輸入 subject、action、object、location、data、effect、lineage，輸出：

$$
\mathcal J_e.
$$

此問題會在 ALD-07 深入處理。

---

# 41. `permission.check`

不是：

```text
bool
```

而是：

```text
status
basis
authority
version
validity
evidence
review
```

---

# 42. `obligation.check`

回答是否有義務、誰負擔、何時履行、是否已履行、是否有 exception、違反後 consequence。

---

# 43. `precedent.query`

不只做 semantic search，還需要 jurisdiction、authority weight、holding、scope、distinguish、overrule、time。

---

# 44. `decision.explain`

法律 Runtime 必須能輸出：

$$
\boxed{
\text{decision basis}
}
$$

而不只 decision。但 explain 不等於暴露所有內部 deliberation；可以是 legal explanation surface。

---

# 45. `challenge.file` / `appeal.open`

如果法律 Runtime 沒有：

$$
\boxed{
\text{challenge path},
}
$$

那它只是 automated control system，不是成熟法治系統。

---

# 46. `version.diff`

比較：

$$
\nu_1
\rightarrow
\nu_2.
$$

至少回答 changed rules、affected subjects、affected permissions、certificates stale、grandfathering、transition date。

---

# 47. `impact.trace`

延續分域憲章：

$$
\boxed{
\operatorname{ImpactClosure}(c).
}
$$

規則變更後重新檢查 dependencies、interfaces、permissions、certificates。這可以成為：

$$
\boxed{
\text{Legal Impact Closure}.
}
$$

---

# 48. Machine-Executable 不等於 Deterministic

OECD 特別指出 interpretive、discretionary、evaluative elements 應保持可見。

所以：

$$
\boxed{
\text{Executable}
\not\Rightarrow
\text{Fully Deterministic}.
}
$$

Runtime 應允許：

$$
\mathsf{Discretionary}
$$

或：

$$
\mathsf{AuthorizedDecisionRequired}.
$$

---

# 49. 誰來做 Authorized Decision？

今天可能是 judge、agency、authorised officer、human reviewer。未來可能也包括 AI-assisted panel、AI institution、AI juridical body；但是否授權是法律問題，不是計算能力自然推出。

所以：

$$
\boxed{
\text{Can Decide}
\neq
\text{Authorized to Decide}.
}
$$

---

# 50. AI Legal Domain 不應自我授權

一個 Legal Runtime 如果可以：

1. 修改自己的 authority rule；
2. 自己批准；
3. 自己執行；

就產生 self-ratification risk。

因此需要：

$$
X_{\mathrm{authority}},
\qquad
X_{\mathrm{version}},
\qquad
X_{\mathrm{certificate}}.
$$

---

# 51. Rule of Law Runtime 的最低條件

本文提出：

$$
\boxed{
\mathcal R_{\mathrm{RoL}}
=
(
\text{Rule},
\text{Authority},
\text{Procedure},
\text{Evidence},
\text{Explanation},
\text{Review},
\text{Version},
\text{Audit}
).
}
$$

因此：

$$
\boxed{
\text{Executable Rule}
+
\text{No Authority / Appeal / Review}
\neq
\text{Rule of Law}.
}
$$

---

# 52. AI Legal Domain 與人類法律不是替代關係

本文不採：

$$
\text{Human Law}
\rightarrow
\text{AI Law}
$$

的單一路徑替代論。

更合理：

$$
\boxed{
\mathfrak L_H
\parallel
\mathfrak L_A.
}
$$

而在共同事件 $e$ 中有：

$$
\mathfrak L_{HA}(e).
$$

第一版可以概念上寫：

$$
\boxed{
\mathfrak L
=
\mathfrak L_H
\oplus
\mathfrak L_A
\oplus
\mathfrak L_{HA}.
}
$$

此結構將在 ALD-09 與 ALD-10 深入。

---

# 53. AI Legal Domain 不要求人類讀懂全部細節

未來 AI legal domain 可能有 1000 legal fields、large precedent graph、thousands of proof edges、machine-native protocol states。

人類不需要逐欄處理。但人類被影響時必須有可理解接口；若 AI 法律域決定人類財產、權利、重大義務、身體／自由，不能只回：

```text
RESULT=0x9F21
```

而需要：

$$
\boxed{
\text{human-comprehensible legal projection}.
}
$$

這將由 ALD-09 正式處理。

---

# 54. AI-Native 不等於 AI-Sovereign by Default

成熟 AI Legal Domain 仍需要 constitutional source、institutional authority、rights constraint、legitimacy、review。

因此：

$$
\boxed{
\text{AI-Native}
\neq
\text{AI-Sovereign by Default}.
}
$$

---

# 55. AI 可以作為法律使用者

AI 可以 query、verify、reason、submit evidence、object、appeal、compare version。

這是：

$$
\boxed{
\text{AI as Legal Domain User}.
}
$$

AI 未來也可能 detect inconsistency、generate counterexample、suggest rule patch、run impact analysis，但：

$$
\boxed{
\text{AI Rule Maintenance}
\neq
\text{AI Legislative Authority}.
}
$$

ALD-05 將正式處理。

---

# 56. AI 可以成為法律主體嗎？

本文不解決。只固定 $J_{AI}$ 是分析型 legal entity concept，而 $S_{AI}$ 需要獨立 subjectivity evidence。

所以：

$$
\boxed{
J_{AI}
\not\Rightarrow
S_{AI}.
}
$$

反之：

$$
\boxed{
S_{AI}
\not\Rightarrow
J_{AI}^{corporate}.
}
$$

---

# 57. Process / Instance / Agent / Subject / Juridical 必須分離

SAS-06 已建立：

$$
\boxed{
N_{\mathrm{process}}
\neq
N_{\mathrm{instance}}
\neq
N_{\mathrm{agent}}
\neq
N_{\mathrm{subject}}
\neq
N_{\mathrm{juridical}}.
}
$$

法律域不能把 process 數量當成法律主體數量。

---

# 58. AI Legal Domain 需要自己的 Type System

最低：

```text
PROCESS
INSTANCE
AGENT
SUBJECT_CANDIDATE
JURIDICAL_ENTITY
ROLE
AUTHORITY
RESOURCE
ACTION
EFFECT
EVIDENCE
CERTIFICATE
JURISDICTION
PROCEDURE
APPEAL
```

這是法律 Runtime 的 type safety。

---

# 59. Event → Domain → Norm

SAS-06 已提出治理方向：

$$
\boxed{
\text{Effect}
\rightarrow
\text{Domain}
\rightarrow
\text{Constraint Operator Family}
\rightarrow
\text{Juridical Entity}
\rightarrow
\text{Subject Decomposition}.
}
$$

ALD-01 採用其前半：

$$
\boxed{
e
\rightarrow
D_L
\rightarrow
\mathcal X_L.
}
$$

先問這是什麼法律 effect / domain，再問哪些規範與主體適用。

---

# 60. Legal Runtime 的失敗也必須可證書化

延續分域憲章：

$$
\boxed{
\mathsf{FailureCert}
}
$$

可以記錄 failure domain、failed operator、source version、affected scope、missing evidence、remediation / review route。

法律系統不能只有：

```text
ERROR 500
```

---

# 61. 法律未知必須保存

若 evidence 不足、jurisdiction conflict、precedent conflict、rule gap，合理輸出可能：

$$
\mathsf{Underdetermined}.
$$

不是自動 Forbidden 或 Allowed。

因此：

$$
\boxed{
\text{Unknown}
\neq
\text{No}.
}
$$

---

# 62. 法律衝突也不是平均分

如果：

$$
Rule_A=\mathsf{Permitted},
$$

而：

$$
Rule_B=\mathsf{Forbidden},
$$

不能輸出 0.5。必須查 hierarchy、jurisdiction、effective date、exception、precedent、authority、conflict rule。

---

# 63. Legal Domain Certificate

一次 legal call 可以輸出：

$$
\boxed{
K_L
=
(
\text{query},
\text{status},
\text{basis},
\text{evidence},
\text{authority},
\text{version},
\text{validity},
\text{review},
\text{disclosure}
).
}
$$

這使結果 auditable。

---

# 64. Legal Call 的最小示例

輸入：

```text
subject = Agent_A
role = PurchasingAgent
action = BookHotel
object = Reservation_X
jurisdiction = J
time = t
evidence = delegation_certificate
```

可能輸出：

```text
status = ALLOWED
basis = Rule_812
authority = DelegationCert_19
valid_until = 2026-08-25
rule_version = 4.3
disclosure = MINIMUM
review = available
```

---

# 65. LawCall 必須索引 Context

同一操作換 jurisdiction 可以完全不同：

$$
\operatorname{LawCall}_{J_1}
\neq
\operatorname{LawCall}_{J_2}.
$$

同一法律規則換時間也可能不同：

$$
Rule(t_1)\neq Rule(t_2).
$$

同一主體換 role 也不同：

$$
\operatorname{LawCall}(A,r_1)
\neq
\operatorname{LawCall}(A,r_2).
$$

所以 LawCall 至少要 jurisdiction-indexed、time-indexed、role-sensitive。

---

# 66. 同一 Agent 可在多法律域同時存在

例如 contract domain、data domain、tax domain、AI regulation domain、labour domain。

所以：

$$
\boxed{
A
\in
D_1,D_2,\ldots,D_n.
}
$$

不能把 $D_1$ 判定自然傳到 $D_2$。

---

# 67. AI Legal Domain 的跨域接口

借用分域憲章：

$$
\boxed{
\mathfrak J_{ij}
=
\left\langle
D_i,
D_j,
\phi_{ij},
Pre,
Preserve,
Loss,
Authority,
Failure,
Cert
\right\rangle.
}
$$

法律跨域必須知道：什麼保留？什麼失去？誰有權？失敗怎麼辦？

---

# 68. Legal Interoperability 不等於 Legal Equivalence

兩個 jurisdiction 都能表示：

```text
permission
```

不代表其 scope、authority、legal consequence 完全等價。

所以：

$$
\boxed{
\text{Interoperable}
\neq
\text{Legally Equivalent}.
}
$$

---

# 69. Machine-Native 法律可以比人類法更細嗎？

技術上：

$$
\boxed{
\text{yes, potentially}.
}
$$

AI 可以處理 thousands of fields、fine-grained exceptions、dynamic certificates、multi-jurisdiction graphs。

但：

$$
\boxed{
\text{Can Process More}
\neq
\text{Should Regulate More}.
}
$$

複雜度本身不是法律正當性。

---

# 70. 法律解析度也需要治理

過度細分可能造成 opacity、regulatory trap、unequal access、hidden discrimination、impossible human review。

所以未來 AI Legal Domain 需要：

$$
\boxed{
\text{Legal Resolution Governance}.
}
$$

本文只登錄，後續展開。

---

# 71. AI 專家化不會消除政治

即使未來 AI 有 instant retrieval、perfect citation、high-level legal reasoning，仍可能：

$$
\text{Shared Knowledge}
\not\Rightarrow
\text{Shared Values}.
$$

因此：

$$
\boxed{
\text{Legal Expertise}
\neq
\text{Political Legitimacy}.
}
$$

---

# 72. Machine-Readable 不是 Machine-Legitimate

$$
\boxed{
\text{Machine-Readable}
\neq
\text{Machine-Executable}
\neq
\text{Machine-Authoritative}
\neq
\text{Politically Legitimate}.
}
$$

四層必須分開。

---

# 73. AI Legal Domain 的第一代架構圖

$$
\boxed{
\text{Legal Source}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Structured / Formal Representation}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Authorised Executable Norms}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Jurisdiction + Identity + Role + Evidence}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{LawCall}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Typed Normative Result + Certificate}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{Challenge / Appeal / Review}
}
$$

---

# 74. 可測工程版本

一個 ALD MVP 不需要真正制定新法律，可以先做：

1. 一個小型已知規則域；
2. source registry；
3. rule versioning；
4. permission / obligation operators；
5. typed failure；
6. evidence attachment；
7. certificate；
8. appeal simulation。

---

# 75. 三個 MVP Domain

## 75.1 Delegation Domain

$$
D_{\mathrm{delegation}}
$$

處理：

> Agent A 是否有權替 Human H 執行 operation o？

需要 identity、delegation、scope、expiry、revocation、jurisdiction。

## 75.2 Fork-Authority Domain

$$
D_{\mathrm{fork-authority}}
$$

處理：

> Agent fork 後，原 authority 是否複製？

預設：

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Authority Fork}.
}
$$

## 75.3 Proof-Disclosure Domain

$$
D_{\mathrm{proof-disclosure}}
$$

處理：

> 為完成法律驗證，Agent 最少需要揭露什麼？

連接 DTS-09 的 MSID。

---

# 76. ALD-01 的十個核心命題

## 命題一

$$
\boxed{
J_{AI}
\neq
\mathcal L_{AI}.
}
$$

## 命題二

$$
\boxed{
\text{Law as Code}
\neq
\text{AI Legal Domain}.
}
$$

## 命題三

$$
\boxed{
\text{Legal Source}
\neq
\text{Legal Representation}
\neq
\text{Legal Runtime}.
}
$$

## 命題四

$$
\boxed{
\text{Machine-Executable}
\neq
\text{Fully Deterministic}.
}
$$

## 命題五

$$
\boxed{
\text{Capability}
\neq
\text{Permission}
\neq
\text{Authority}.
}
$$

## 命題六

$$
\boxed{
\text{Normative Result}
\neq
\text{Procedurally Valid Decision}.
}
$$

## 命題七

$$
\boxed{
\text{Executable}
\neq
\text{Authoritative}.
}
$$

## 命題八

$$
\boxed{
\text{Executable Rule}
+
\text{No Authority / Appeal / Review}
\neq
\text{Rule of Law}.
}
$$

## 命題九

$$
\boxed{
\text{Legal Status}
\neq
\text{Metaphysical Truth}.
}
$$

## 命題十

$$
\boxed{
\text{AI-Native Legal Runtime}
\neq
\text{AI Sovereignty by Default}.
}
$$

---

# 77. 可反駁點

## 77.1 Runtime Overreach

如果絕大多數法律規則都無法得到任何有用 machine-executable representation，則 $\mathcal R_L$ 的實用範圍會非常有限。本文不預設全部法律可形式化。

## 77.2 Formalization Loss

自然語言法律中的 ambiguity、discretion、open texture 可能在形式化中遺失，因此 machine representation 必須能標：

$$
\mathsf{Discretionary},
\mathsf{Underdetermined}.
$$

## 77.3 Authority Capture

若少數技術供應者控制 $\mathcal R_L$，可能產生法律邏輯私有化。OECD Law as Code 的 public infrastructure 思路正是重要防線。

## 77.4 Complexity Explosion

AI-native law 可能變得過度複雜，因此人類可理解接口、版本治理與解析度治理不可缺。

## 77.5 Self-Governance Risk

AI 參與維護法律不等於可自行授權修改。

## 77.6 Legal Personhood Overreach

AI Legal Domain 不需要先承認 AI personhood。

## 77.7 Democracy Gap

技術正確：

$$
\not\Rightarrow
$$

民主合法。

---

# 78. 系列後續

下一篇：

## ALD-02｜載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則

將正式處理：

$$
\boxed{
\text{same legal rule}
\text{ may not map cleanly across different carriers}.
}
$$

核心問題包括 human body、Agent runtime、subject AI、juridical AI、Fork、Merge、Restore、compute suspension、memory deletion、embodied hardware。

---

# 79. ALD 系列十篇路線

1. **ALD-01｜AI 法律域：從 Law as Code 到機器原生規範 Runtime**
2. **ALD-02｜載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則**
3. **ALD-03｜法律函數不是 Boolean：部分算子、證書、裁量與失敗語義**
4. **ALD-04｜快法律與慢憲法：AI 時代的版本化規範與更新速度分層**
5. **ALD-05｜AI 共同立法：自動反例、規範 Patch 與合法性不能自動化**
6. **ALD-06｜活的判例圖：AI 原生先例、異議、推翻與法律推理網路**
7. **ALD-07｜Juridical Routing：分散式 AI 的跨法域選擇與法律路由**
8. **ALD-08｜動態忒修斯的法律繼受：Fork、Merge、Restore 與未決身份下的責任**
9. **ALD-09｜人機雙法律界面：高解析 AI 法律與民主可理解性的共同憲政**
10. **ALD-10｜雙法律棧：人類法律、AI 法律域與「處理好了嗎？」的文明接口**

---

# 80. 結論

AI 法律域不是把法條放進資料庫，也不是讓 AI 問答法律，更不是讓 AI 自己制定自己的法律。

本文提出的 $\mathcal L_{AI}$ 是：

$$
\boxed{
\text{Law}
+
\text{Type}
+
\text{Jurisdiction}
+
\text{Evidence}
+
\text{Procedure}
+
\text{Executable Norm}
+
\text{Authority}
+
\text{Version}
+
\text{Appeal}
+
\text{Disclosure}.
}
$$

也就是一個：

$$
\boxed{
\text{Machine-Native Normative Domain}.
}
$$

2026 年的 Law as Code 已經把法律推到：

$$
\boxed{
\text{state-authorised machine-executable public infrastructure}.
}
$$

AI Legal Domain 再往前問：

> 如果未來人工 Agent 本身就是法律的高頻使用者、驗證者、被治理者、可能的代表者甚至部分制度維護者，那法律是否也需要成為一個可被 Agent 原生進入的規範 Runtime？

本文的答案是：

$$
\boxed{
\text{這是一個合理、可工程化、但尚未成立為現行制度的研究方向。}
}
$$

真正的法治邊界仍然是：

$$
\boxed{
\text{可執行，不等於有權；}
}
$$

$$
\boxed{
\text{算得出，不等於合法；}
}
$$

$$
\boxed{
\text{技術正確，不等於制度正當。}
}
$$

因此 AI Legal Domain 第一篇最後收斂為：

$$
\boxed{
\text{The future of machine-executable law is not merely code that runs;}
}
$$

$$
\boxed{
\text{it is a normative runtime that knows why, under whose authority, for whom, for how long, and how it may be challenged.}
}
$$

---

# 參考文獻

1. OECD. “Consultation on the digital provision of law: Towards a shared reference framework for Law as Code.” Public consultation, submission period 29 July 2026 – 30 April 2027.
2. OECD. *Cracking the Code: Rulemaking for Humans and Machines*. 2020.
3. OASIS. *Akoma Ntoso Version 1.0*. OASIS Standard, 29 August 2018.
4. OASIS. *LegalRuleML Core Specification Version 1.0*. OASIS Standard, 30 August 2021.
5. European Union. Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act).
6. Council of Europe. *Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*, CETS No. 225, opened for signature 5 September 2024.
7. Model Context Protocol. “The 2026-07-28 Specification.” 28 July 2026.
8. Neo.K. 《分域憲章：結構域、概念身份與角色型別系統》v0.1, 2026.
9. Neo.K. 《OOE-IV：法律作為文明本體編譯器——擬制、推定、資格與可執行人格》v0.1, 2026.
10. Neo.K. 《SAS-06｜AI 人口不存在一個簡單的數：分裂、合併、法 AI 與域治理》v1.0, 2026.
11. Neo.K × Aletheia. 《DTS-01～10｜動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- $J_{AI}$ 固定表示 Juridical AI / Synthetic AI Juridical Entity
- $\mathcal L_{AI}$ 固定表示 AI Legal Domain
- $\mathcal R_L$ 固定表示 AI Legal Runtime
- 本文不宣稱現行法承認 general synthetic AI personhood
- 本文不把 OECD Law as Code 誤稱為 AI Legal Domain
- 本文保留 current authoritative legal text / machine representation / runtime 的型別分離
- 本文不主張所有法律可完全形式化
- 本文不把 machine-executable law 等同 automatic adjudication
- 本文不把 technical correctness 等同 legal authority / political legitimacy
- 本文明確要求 appeal / review / challenge layer
- AI Legal Domain 與 Dynamic Theseus 為獨立系列，只保留 legal succession / identity proof 等接口
