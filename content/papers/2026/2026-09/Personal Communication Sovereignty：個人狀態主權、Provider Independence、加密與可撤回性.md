---
title: "Personal Communication Sovereignty：個人狀態主權、Provider Independence、加密與可撤回性"
subtitle: "Series A-06｜Personal Communication Sovereignty: User-Controlled State, Provider Independence, Cryptographic Boundaries, Portability, and Revocation"
author: "Neo.K（EVEMISS / EveMissLab）"
ai_collaboration: "Aletheia（GPT-5.6 Sol）"
version: "0.1"
status: "Research Draft / Canonical Source"
date: "2026-08-24"
language: "zh-TW"
series: "Series A｜AI-Native Communication Continuum"
series_number: "A-06"
document_type: "Research Paper"
canonical_source: true
encoding: "UTF-8"
---

# Personal Communication Sovereignty：個人狀態主權、Provider Independence、加密與可撤回性

## Series A-06｜Personal Communication Sovereignty: User-Controlled State, Provider Independence, Cryptographic Boundaries, Portability, and Revocation

**作者：** Neo.K（EVEMISS / EveMissLab）  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-08-24  
**文件狀態：** Research Draft / Canonical Source  

---

# 摘要

Series A-01 至 A-05 已依序建立 AI-Native Communication Continuum、Persistent Communication State、Multimodal-Native Communication、AI Communication Runtime 與 Adaptive Hybrid Communication Fabric。這些工作共同回答：一個人的通訊世界如何在裝置、位置、模態、AI Provider 與網路路徑持續切換時仍維持可恢復、可投影、可授權與可驗證的狀態。然而，只要 canonical state、identity、memory、artifact、delegation、credential 或 recovery path 最終仍被單一 Provider 實質控制，技術上的 continuity 仍可能形成新的 lock-in。本文因此提出 **Personal Communication Sovereignty（PCSov，個人通訊主權）**，作為 AI-Native Communication Continuum 的治理與控制權層。

本文首先拒絕一個過度簡化的定義：

$$
\boxed{
\text{Sovereignty}
\neq
\text{Absolute Ownership of Every Communication Record}.
}
$$

通訊天然涉及多方。某一則訊息可能由使用者撰寫，但同時存在接收者副本、企業紀錄、外部郵件系統、平台 metadata、法定保存義務與第三方權利。因而「主權」不能被定義為使用者可以單方面抹除世界上所有相關狀態。本文將其定義為：**一個 principal 對自己有權控制的通訊狀態，具有持久、可移植、可撤回、可驗證且不被單一 Provider 綁死的控制能力；同時尊重其他 principal、企業與法律所具有的獨立權利域。**

本文以 **Sovereignty Rights Vector** 描述 principal $u$ 對 object $o$ 在時間 $t$ 的控制權：

$$
\boxed{
\mathcal R_u(o,t)
=
(
r,w,d,v,x,e,m,k,a
)
}
$$

其中分別表示 read、write/derive、delegate、revoke、export、erase、migrate、key-control 與 audit / verify。每一維不是全域永久布林值，而是受 owner scope、purpose、relationship、contract、retention、recipient rights、legal basis 與 current policy epoch 約束的條件能力。

在此基礎上，本文將 Sovereign State Boundary 細分為：Identity Sovereignty、State Sovereignty、Memory Sovereignty、Artifact Sovereignty、Delegation Sovereignty、Cryptographic Sovereignty、Provider Independence、Portability、Revocability 與 Verifiability。本文提出：**Provider login 不等於使用者 identity；模型記憶不等於 canonical memory；E2EE 不等於資料所有權；資料匯出不等於真正可遷移；刪除按鈕不等於所有 replica 已消失；自架服務也不自動等於主權。** 真正的主權來自多個可測量、不互相替代的控制維度。

為衡量 Provider lock-in，本文定義 **Provider Coupling**：

$$
\boxed{
\kappa_P
=
\sum_i w_i c_i,
\qquad
0\le\kappa_P\le1
}
$$

其中 $c_i$ 衡量 identity、state、memory、artifact、delegation、secret、schema、provenance、recovery 與 action history 對單一 Provider 的不可替代依賴。Provider Independence 定義為：

$$
\boxed{
PI=1-\kappa_P.
}
$$

本文進一步指出，真正的 portability 不是下載一份 JSON 或 ZIP。若匯出的內容沒有 schema、provenance、identity binding、permission state、task frontier、artifact version、memory policy、delegation contract 與 resume semantics，使用者雖「拿到資料」，卻無法在另一套 runtime 中恢復原本的工作世界。因此提出 **Semantic Portability**：

$$
\boxed{
\text{Portability}
=
\text{Data}
+
\text{Schema}
+
\text{Provenance}
+
\text{Authority}
+
\text{Context}
+
\text{Resume Semantics}.
}
$$

本文亦形式化 revocation 與 deletion 的非對稱性。撤回權只能保證未來授權失效，不能使合法接收者「忘記」已取得的資訊；刪除可以包含 active state removal、replica purge、key destruction、provider erasure request 與 retention tombstone，但不能在存在法定保存、共同資料主體、外部已交付副本或不可撤回外部副作用時假稱「全世界已刪除」。因此 PCSov 要求系統產生 **Revocation Receipt** 與 **Deletion Residual Report**，明確指出已完成、未完成與依法／依契約仍保留的狀態。

在既有技術與制度上，本文採取「錨點而非等同」的立場。GDPR Article 20 的 data portability 與 Article 17 的 erasure 提供個人資料可攜與刪除的法律錨點，但不等同本文較廣義的 communication state sovereignty；EU Data Act 已對 data-processing service switching、machine-readable export、open interfaces、continuity 與 interoperability 建立更接近 Provider Independence 的制度背景；RFC 9420 Messaging Layer Security（MLS）提供群組端對端加密、forward secrecy 與 post-compromise security 的協議基礎；W3C DID v1.0 與 2026 年 DID v1.1 Candidate Recommendation 提供 identity 可脫離單一中央 registry / identity provider 的一種標準化研究方向；FIDO2 / passkeys 提供 phishing-resistant public-key authentication；NIST Zero Trust Architecture 則支持「網路位置或既有登入不應自動獲得持續信任」的安全模型。本文不要求 EVEMISS 必須採用 DID、單一 key custody 模式或特定法域，而是把這些技術視為可插拔實作選項或外部治理錨點。

對 EVEMISS 既有產品而言，PCSov 並非新建一個獨立帳號系統。Consumer Core v0.1 已存在 owner_scope、identity_scope、Provider & Secret Broker、retention_policy、Consent Record、Export 與 delete API；PAI Relay v0.2 已把有限代理、可撤回授權、可接管性、Relationship Memory、BYOK 與 Provider-specific deletion 當成核心；A-02 又已定義 Authoritative State Domain 與 permission epoch；A-04 定義 capability 與 permission 分離、approval token、handoff authority 與 action receipt。本文將這些既有 primitive 統一提升為一個主權契約，使未來桌機、手機、車載、飛機、會議室與其他 Surface 可以共用同一 personal communication continuum，而不讓任何一個 Surface、Provider、Agent 或 network path 自動成為使用者通訊世界的永久主人。

本文最終提出六條核心不變量：

$$
\boxed{
\text{Provider Possession}
\not\Rightarrow
\text{Provider Sovereignty}
}
$$

$$
\boxed{
\text{Model Capability}
\not\Rightarrow
\text{Authority over User State}
}
$$

$$
\boxed{
\text{Exportability}
\not\Rightarrow
\text{Semantic Portability}
}
$$

$$
\boxed{
\text{Encryption}
\not\Rightarrow
\text{Ownership}
}
$$

$$
\boxed{
\text{Revocation}
\not\Rightarrow
\text{Retroactive Erasure of Disclosure}
}
$$

$$
\boxed{
\text{Personal Sovereignty}
\not\Rightarrow
\text{Override of Third-Party or Enterprise Rights}
}
$$

A-06 因而完成 Series A 的最後一篇研究論文，並為 A-07《EVEMISS Communication Continuum Architecture：統一技術白皮書與實作路線圖》提供 identity、state、provider、key、portability、revocation 與 governance 的正式設計基礎。

**關鍵詞：** Personal Communication Sovereignty；Provider Independence；State Sovereignty；Data Portability；Semantic Portability；Revocation；Erasure；Identity Sovereignty；Memory Sovereignty；Delegation；Encryption；MLS；DID；FIDO2；Zero Trust；GDPR；EU Data Act；AI-Native Communication Continuum；EVEMISS

---

# Abstract

This paper introduces **Personal Communication Sovereignty (PCSov)** as the governance and control layer of the AI-Native Communication Continuum. Earlier papers in Series A established persistent state, multimodal projection, an AI communication runtime, and an adaptive hybrid communication fabric. Those mechanisms make communication technically continuous across devices, locations, modalities, AI providers, and network paths. Technical continuity alone, however, does not guarantee that the user retains durable control over identity, memory, artifacts, delegations, credentials, recovery mechanisms, or provider migration.

PCSov is deliberately distinguished from absolute ownership of every communication record. Communication is inherently multi-party: a single message may simultaneously involve the sender, recipient, an enterprise workspace, service-provider metadata, contractual retention, or legal obligations. Sovereignty is therefore modeled as a conditional control relationship over state for which a principal has legitimate authority, not as a unilateral claim over every copy in existence.

The paper defines a Sovereignty Rights Vector covering read, write or derive, delegate, revoke, export, erase, migrate, key control, and audit or verification. It separates identity sovereignty, persistent-state sovereignty, memory sovereignty, artifact sovereignty, delegation sovereignty, cryptographic sovereignty, provider independence, portability, revocability, and verifiability. It also introduces Provider Coupling and Provider Independence metrics and formalizes Semantic Portability as more than data export: schema, provenance, authority, context, task frontier, and resume semantics must travel with the state if the communication world is to remain functionally continuous.

Revocation and erasure are treated as asymmetric operations. Revocation prevents future authorized use but cannot force a recipient to forget previously disclosed information. Deletion can cover active state, replicas, cryptographic keys, provider copies, and retention records, but systems must not claim universal deletion where third-party rights, external deliveries, enterprise retention, or legal obligations remain. PCSov therefore requires explicit revocation receipts, deletion residual reports, provenance, and verifiable state transitions.

The architecture is related to, but not equated with, current external standards and legal mechanisms. GDPR Articles 17 and 20 provide erasure and portability anchors; the EU Data Act provides stronger switching and interoperability requirements for data-processing services; RFC 9420 MLS provides end-to-end group key establishment with forward secrecy and post-compromise security; W3C DID and FIDO2 provide possible identity and authentication mechanisms; NIST Zero Trust provides a compatible security principle that trust should not be permanently inherited from network position or prior sessions. None of these mechanisms individually constitutes communication sovereignty.

For EVEMISS, PCSov unifies existing owner scopes, provider brokers, export and deletion operations, revocable delegation, relationship memory, BYOK, permission epochs, approval tokens, and action receipts into a single governance contract. It provides the sovereignty model required for the Series A-07 implementation white paper.

---

# 0. 研究問題：Continuity 最後到底屬於誰？

A-01 的核心命題是：

$$
\text{Change of device, location, modality, network path, or AI provider}
$$

不應自動造成：

$$
\text{reset of communication identity and authorized state}.
$$

A-02 進一步建立 Persistent Communication State：

$$
\mathcal P_t
=
(
I_t,R_t,S_t,X_t,T_t,M_t,F_t,A_t,P_t,G_t
).
$$

A-03 讓同一 state 可以被投影到不同 Surface；A-04 讓 AI Runtime 在 permission 與 governance 邊界內規劃、路由與執行；A-05 讓 network path 變化不再等於 communication world 重置。

這些架構共同得到一個更尖銳的問題：

> 如果所有東西都能持續存在，那麼這個「持續存在的東西」究竟由誰控制？

若答案仍然是：

```text
Provider account exists -> state exists
Provider account deleted -> state disappears
Provider model changed -> memory semantics disappear
Provider export incomplete -> migration fails
Provider API revoked -> user loses control
```

那麼 Continuum 雖然跨 Surface，仍然沒有真正跨 Provider。

因此必須加入：

$$
\boxed{
\text{Sovereignty Layer}.
}
$$

---

# 1. Personal Communication Sovereignty 的正式定義

令使用者或其他合法 principal 為：

$$
u.
$$

令其有權控制的 communication-side state 集合為：

$$
\mathcal O_u(t).
$$

本文定義 **Personal Communication Sovereignty** 為：

> principal $u$ 對 $\mathcal O_u(t)$ 中之 state object，在合法且明確的 scope 下，具有持久、可觀察、可委託、可撤回、可移植、可恢復與可驗證的控制能力；且該控制能力不以單一 Provider、單一模型、單一裝置或單一網路持續存在為必要條件。

形式上：

$$
\boxed{
PCSov_u(t)
=
\mathcal C
(
\mathcal O_u,
\mathcal R_u,
\mathcal K_u,
\mathcal D_u,
\mathcal V_u,
\mathcal G_u
)
}
$$

其中：

- $\mathcal O_u$：有權控制的 state objects；
- $\mathcal R_u$：對每一 object 的 rights / capabilities；
- $\mathcal K_u$：key、credential 與 recovery control；
- $\mathcal D_u$：delegation 與 revocation state；
- $\mathcal V_u$：version、provenance、receipt 與可驗證性；
- $\mathcal G_u$：governance、retention、contract 與 policy constraints。

這個定義故意不是：

$$
PCSov_u
=
\text{User can do anything to any record involving user}.
$$

因為那會破壞多方通訊本身。

---

# 2. 主權不等於所有權

## 2.1 一則訊息不是單一所有權物件

假設：

$$
m
=
\text{message sent from }u\text{ to }v.
$$

至少可能同時存在：

- sender-authored content；
- recipient-held copy；
- delivery metadata；
- encrypted transport state；
- local cache；
- enterprise archive；
- compliance record；
- AI-produced summary；
- search index；
- backup；
- derived relationship memory。

因此：

$$
\boxed{
\text{Authorship}
\neq
\text{Custody}
\neq
\text{Possession}
\neq
\text{Authority}
\neq
\text{Legal Ownership}.
}
$$

A-06 不嘗試以單一「owner」欄位解決全部問題。

## 2.2 Owner scope 是架構 scope，不是法律結論

EVEMISS Consumer Core 已使用：

```text
owner_scope
identity_scope
mode_scope
retention_policy
```

這些欄位應被理解為：

> 系統在某個功能與治理 domain 中，誰有第一順位決定權。

它不能自動推論：

> 誰在所有司法管轄區具有完整民法／智慧財產／個資法所有權。

所以本文使用：

$$
\boxed{
\text{Architectural Authority Scope}
}
$$

而不是把所有問題壓成 `legal_owner`。

---

# 3. Sovereignty Rights Vector

對 object $o$ 與 principal $u$，定義：

$$
\boxed{
\mathcal R_u(o,t)
=
(
r,w,d,v,x,e,m,k,a
).
}
$$

各維度：

| 維度 | 意義 |
|---|---|
| $r$ | read / inspect |
| $w$ | write / edit / derive |
| $d$ | delegate capability |
| $v$ | revoke delegation or access |
| $x$ | export |
| $e$ | erase / request erasure |
| $m$ | migrate to another runtime/provider |
| $k$ | cryptographic key control |
| $a$ | audit / verify execution and history |

每一項更合理的形式是：

$$
R_i
=
f(
actor,
object,
purpose,
relationship,
policyEpoch,
retention,
contract,
recipientRights,
legalBasis,
time
).
$$

因此：

$$
R_i\in\{ALLOW,DENY,CONDITIONAL,ESCALATE\}.
$$

而不是永久的 $0/1$。

---

# 4. 主權物件分類

PCSov 不應對所有資料使用相同規則。

本文提出至少八類 object class。

## 4.1 Personal-Originated State

例如：

- private notes；
- user preferences；
- personal AI configuration；
- locally authored task state；
- personal-only memory；
- user-owned artifacts。

這一類通常具有最高的：

$$
Export,
Migrate,
Delete,
ProviderIndependence.
$$

## 4.2 Shared Communication State

例如：

- message thread；
- shared room event；
- meeting transcript；
- shared file comments。

它通常包含：

$$
\text{Multi-Principal Rights}.
$$

使用者可以刪除自己的 local projection，卻不一定能要求其他合法 participant 刪除其持有副本。

## 4.3 Third-Party-Originated State

例如：

- contact 寄給使用者的訊息；
- 第三方附件；
- 他人的個人資料。

使用者可具有：

$$
Read=1,
Export=conditional,
EraseLocal=1,
EraseThirdPartySource=0.
$$

## 4.4 Enterprise / Contractual State

例如：

- enterprise case；
- customer record；
- regulated evidence；
- company mail；
- approval record。

這類不能因某位 employee 的 Personal Sovereignty 而被私自帶走或抹除。

## 4.5 Provider-Derived Metadata

例如：

- usage metrics；
- provider billing data；
- fraud controls；
- platform-specific routing metadata。

其中一部分可能涉及使用者個資權利，一部分則可能是 Provider 自有營運紀錄。

## 4.6 Secret / Credential State

例如：

- API key；
- OAuth token；
- passkey private key；
- session secret；
- encryption key。

這一類通常：

$$
Export
\neq
\text{Plaintext Export}.
$$

更合理的是：

- key handle；
- rebind；
- rotate；
- recovery；
- encrypted transfer；
- destroy。

## 4.7 Model-Ephemeral State

例如某 Provider 的：

- internal cache；
- hidden activation；
- provider-specific latent state；
- transient inference state。

這些不應被誤認為 canonical user memory。

## 4.8 Evidence / Legally Retained State

例如：

- action receipt；
- approval evidence；
- fraud report；
- legally required audit trail。

它可能需要：

$$
Retention>PersonalDeleteRequest.
$$

但系統必須明確標示 retention basis、duration 與 access scope。

---

# 5. Sovereignty Boundary：哪些狀態必須脫離 Provider？

本文延續 A-01 的 Sovereign State Boundary，並將其細化。

一個 Provider-independent personal continuum 至少應把下列 logical state 從單一 Provider 私有 session 中抽離：

$$
\boxed{
\Sigma_u(t)
=
(
I_u,
R_u,
X_u,
T_u,
M_u,
F_u,
D_u,
P_u,
H_u
)
}
$$

其中：

- $I_u$：identity binding；
- $R_u$：room / relationship state；
- $X_u$：reconstructable context；
- $T_u$：task frontier；
- $M_u$：memory records；
- $F_u$：artifact references / versions；
- $D_u$：delegations；
- $P_u$：permission / policy state；
- $H_u$：receipts / provenance / history pointers。

這不代表所有 raw data 必須永遠存本地。

而是：

$$
\boxed{
\text{Provider Failure}
\not\Rightarrow
\text{Irrecoverable Loss of User-Authorized Logical State}.
}
$$

---

# 6. Provider Possession 不等於 Provider Sovereignty

Provider 可能因服務需要持有：

- encrypted messages；
- account metadata；
- hosted artifacts；
- model inputs；
- tool responses；
- billing events。

但：

$$
\boxed{
Possess(o)
\not\Rightarrow
OwnAuthority(o).
}
$$

Provider 比較合理的角色是：

$$
\text{Custodian / Processor / Service Boundary}
$$

中的一種或數種，實際法律角色依服務與法域而異。

系統架構不應因 Provider physically stores data 就把：

```text
provider_id
```

直接當作：

```text
canonical_owner_id
```

---

# 7. Provider Coupling 與 Provider Independence

## 7.1 Provider Coupling

定義 dependency dimensions：

$$
\mathbf c
=
(
c_I,
c_S,
c_M,
c_F,
c_D,
c_K,
c_R,
c_H,
c_G
).
$$

分別表示：

- identity dependence；
- persistent state dependence；
- memory dependence；
- artifact dependence；
- delegation dependence；
- key / secret dependence；
- recovery dependence；
- history / provenance dependence；
- governance dependence。

定義：

$$
\boxed{
\kappa_P
=
\sum_i w_i c_i,
\qquad
\sum_iw_i=1.
}
$$

若：

$$
\kappa_P=1,
$$

代表 provider 消失後整個 communication world 幾乎不可重建。

若：

$$
\kappa_P\rightarrow0,
$$

代表 provider 可被替換，而 user-side logical state 仍高度可恢復。

## 7.2 Provider Independence

定義：

$$
\boxed{
PI=1-\kappa_P.
}
$$

但：

$$
PI=1
$$

不是必要目標。

某些服務天然 provider-specific，例如：

- proprietary media rendering；
- carrier billing；
- model-specific feature；
- externally hosted account relation。

實務目標是：

> 讓 critical personal state 的 coupling 顯著低於 replaceable convenience state。

---

# 8. Identity Sovereignty：登入帳號不是你本人

## 8.1 Provider Login 是 attachment

定義：

$$
Identity_u
\neq
LoginSession_{Provider}.
$$

更合理的模型：

$$
\boxed{
Identity_u
\xrightarrow{bind}
ProviderCredential_i.
}
$$

因此 Google、Microsoft、Apple、某 AI Provider、電話號碼、Email address 或本地 passkey 都可以是 identity binding，但不應自動成為唯一 identity root。

## 8.2 Identity Root 必須可恢復

一個 personal continuum 應至少支援：

- multi-device binding；
- device revocation；
- credential rotation；
- recovery path；
- provider rebinding；
- identity history / continuity proof。

如果：

$$
LostPhone
\Rightarrow
LostIdentity,
$$

主權其實很脆弱。

## 8.3 DID 是選項，不是強制答案

W3C DID 提供一種將 identifier control 與單一 identity provider 解耦的標準模型。

但 PCSov 不要求：

$$
IdentitySovereignty
\equiv
DID.
$$

可以存在：

- local root identity；
- passkey-backed identity；
- enterprise-managed identity；
- DID；
- hybrid recovery identity。

核心是：

$$
\boxed{
\text{Identity continuity must not be accidentally identical to one provider account lifecycle.}
}
$$

---

# 9. Authentication Sovereignty：Passkey、Device 與 Recovery

Authentication 回答：

> 你現在能不能證明自己有權操作某一 identity？

它不直接回答：

> 這個 identity 對哪些 objects 有哪些權利？

因此：

$$
\boxed{
Authentication
\neq
Authorization
\neq
Sovereignty.
}
$$

FIDO2 / WebAuthn / passkeys 可以提供 phishing-resistant public-key authentication。

但一個完整 PCSov 系統還要處理：

- key backup；
- key sync；
- device loss；
- account recovery；
- compromise recovery；
- trusted recovery contact；
- enterprise recovery；
- local-only mode。

---

# 10. Cryptographic Sovereignty：Encryption 不等於 Ownership

## 10.1 E2EE 解決 confidentiality，不解決所有治理

E2EE 可以逼近：

$$
ProviderRead(Content)=0.
$$

但不能推出：

$$
UserOwnsAllCopies=1.
$$

因為 recipient endpoint 仍可能：

- screenshot；
- copy；
- export；
- forward；
- retain。

因此：

$$
\boxed{
Encryption
\Rightarrow
\text{Confidentiality Property}
}
$$

而不是：

$$
\boxed{
Encryption
\Rightarrow
\text{Absolute Sovereignty}.
}
$$

## 10.2 Key Control 是主權的一個維度

可定義：

$$
K_u(o)
\in
\{
provider,
user,
shared,
enterprise,
threshold,
hardware-bound
\}.
$$

不同 object 可選不同 key custody。

## 10.3 MLS 的角色

RFC 9420 MLS 提供大型非同步群組的 group key establishment、forward secrecy 與 post-compromise security。

這使：

$$
\text{Group Encryption State}
$$

可以隨 membership epoch 演化。

但：

$$
\text{MLS Epoch}
\neq
\text{PCS Permission Epoch}.
$$

前者主要是 cryptographic group state；後者是應用治理與 delegation authority。

兩者可以綁定，但不能混為單一概念。

---

# 11. Memory Sovereignty：模型記憶不應成為唯一記憶

A-02 已要求 Memory Record 至少具有：

- owner；
- scope；
- purpose；
- provenance；
- retention；
- confidence；
- version。

A-06 再加一條：

$$
\boxed{
\text{Provider-native Memory}
\not\equiv
\text{Canonical Personal Memory}.
}
$$

否則切換模型時：

$$
Provider_A
\rightarrow
Provider_B
$$

使用者會失去：

- relationship continuity；
- preference state；
- task history；
- communication context；
- memory correction history。

真正 personal memory 應能：

$$
Export,
Inspect,
Correct,
Scope,
Retain,
Delete,
Migrate.
$$

但對 third-party memory，還必須加入：

$$
PurposeLimit
+
PrivacyBoundary.
$$

---

# 12. Relationship Memory 並不是人物資料庫所有權

PAI Relay 已使用 Relationship Memory 幫助個人 AI 理解：

- contact；
- relationship context；
- communication preference；
- previous interaction；
- risk case。

A-06 必須限制：

$$
\text{Relationship Memory}
\neq
\text{Unlimited Profiling Right}.
$$

一個合理 record 應至少包含：

```yaml
memory_id: ...
owner_scope: PERSONAL
subject_refs:
  - self
  - contact:...
purpose: communication_assistance
provenance: ...
confidence: ...
retention_policy: ...
shareability: restricted
export_policy: conditional
```

這使「記得某個人」與「可任意傳播某人的資料」被分開。

---

# 13. Artifact Sovereignty：正式成果不能只活在聊天渲染層

AI-native communication 中，Artifact 包括：

- document；
- code；
- contract draft；
- image；
- report；
- decision record；
- presentation；
- executable configuration。

本文要求：

$$
\boxed{
\text{Rendered Conversation}
\neq
\text{Canonical Artifact Source}.
}
$$

Artifact sovereignty 至少要求：

- stable artifact ID；
- explicit version；
- canonical source format；
- content hash；
- provenance；
- export path；
- deletion / retention policy；
- provider-neutral metadata；
- link to task / approval state。

這是為什麼「下載聊天記錄」不等於真正的 project migration。

---

# 14. Delegation Sovereignty：AI 可以代理，但代理權必須屬於 principal

PAI Relay 已提出有限代理與可撤回性；A-04 已提出 Action Contract、Approval Token、Authority Scope。

本文定義 delegation：

$$
\boxed{
\delta
=
(
principal,
agent,
capability,
resource,
purpose,
scope,
channel,
expiry,
risk,
revocationHandle,
epoch
).
}
$$

AI 可執行：

$$
Action(a,o)
$$

必須滿足：

$$
Permission(\delta,a,o,t)=ALLOW.
$$

而：

$$
ModelConfidence
$$

不能自動擴張：

$$
CapabilitySet.
$$

---

# 15. Revocation：真正的撤回是未來能力失效

## 15.1 Revocation 的時間方向

令 delegation 為：

$$
\delta_t.
$$

撤回後：

$$
\operatorname{Revoke}(\delta,t_r)
$$

要求：

$$
\forall t>t_r,
Permission(\delta,t)=DENY
$$

或進入需要重新批准的新 epoch。

但不能保證：

$$
\text{Previously disclosed information disappears from recipient cognition}.
$$

因此：

$$
\boxed{
Revocation
\neq
Retroactive Undisclosure.
}
$$

## 15.2 Revocation 類型

至少包括：

1. Agent delegation revoke；
2. device revoke；
3. provider connector revoke；
4. API credential revoke；
5. channel access revoke；
6. memory-use consent revoke；
7. share-link revoke；
8. enterprise role revoke。

---

# 16. Revocation Receipt

每次高價值 revoke 應產生：

```yaml
revocation_receipt:
  target: delegation-or-device-id
  principal: user-id
  requested_at: ...
  effective_at: ...
  old_epoch: 17
  new_epoch: 18
  invalidated_credentials:
    - ...
  invalidated_sessions:
    - ...
  residual_access:
    - reason: recipient_copy_already_delivered
  verifier: ...
```

目標不是製造更多日誌，而是讓：

$$
\boxed{
\text{"我已撤回"}
}
$$

可以被驗證，而不只是 UI 顯示一個綠色勾勾。

---

# 17. Deletion：刪除不是一個布林值

## 17.1 Delete 的不同層次

本文至少區分：

$$
D=
(
D_{active},
D_{replica},
D_{cache},
D_{backup},
D_{key},
D_{provider},
D_{index},
D_{derived}
).
$$

例如：

- active DB record removed；
- local replicas purged；
- search index removed；
- encryption key destroyed；
- backup enters expiry queue；
- provider deletion requested；
- derived memory invalidated；
- audit tombstone retained。

所以「delete success」應該回答：

> 哪些 layer 已完成？哪些仍 pending？哪些不能刪？

## 17.2 Deletion Residual Report

定義：

$$
\boxed{
DRR(o)
=
(
removed,
pending,
retained,
external,
unknown
).
}
$$

其中 `retained` 必須帶：

- retention basis；
- scope；
- duration；
- access policy。

---

# 18. Erasure 與 Evidence 的衝突

若系統為了「可刪」而刪除所有事件：

$$
Auditability\downarrow.
$$

若為了「可稽核」永遠保存所有內容：

$$
Privacy\downarrow.
$$

因此不能把：

$$
Delete
$$

與：

$$
Evidence
$$

視為單一開關。

比較合理的是分離：

$$
\text{Content}
\quad\text{and}\quad
\text{Minimal Verification Record}.
$$

例如：

```text
content -> erased
hash / event type / time / legal basis -> retained under bounded policy
```

但 hash 本身也可能構成敏感關聯資訊，因此仍需 purpose limitation。

---

# 19. Exportability 不等於 Semantic Portability

## 19.1 最弱 portability

```text
Download all messages as JSON.
```

這只是：

$$
DataPortability.
$$

## 19.2 Continuum 需要更高階 portability

真正 migration 至少要帶：

- identity binding；
- relationship graph；
- room state；
- active task frontier；
- memory records；
- artifact manifest；
- provenance；
- permissions；
- delegation state；
- action receipts；
- policy / retention metadata；
- provider adapter mapping；
- resume descriptor。

因此：

$$
\boxed{
\text{Semantic Portability}
=
D+S+V+A+C+R
}
$$

其中：

- $D$：data；
- $S$：schema；
- $V$：version / provenance；
- $A$：authority state；
- $C$：context；
- $R$：resume semantics。

---

# 20. Migration Bundle

本文提出 **Communication Sovereignty Capsule（CSC）** 作為邏輯 export bundle。

它不是規定單一檔案格式，而是一個 contract：

```yaml
csc_version: 0.1
principal:
  identity_ref: ...
state:
  rooms: ...
  relationships: ...
  tasks: ...
  memories: ...
  artifacts: ...
authority:
  permission_epoch: ...
  delegations: ...
  revoked_grants: ...
provenance:
  events: ...
  receipts: ...
providers:
  bindings: ...
  provider_specific_opaque_state: ...
secrets:
  export_mode: handles_or_rebind
resume:
  descriptors: ...
retention:
  policies: ...
```

其中 secret 預設不以明文進 bundle。

---

# 21. Migration Functional Continuity

從 Provider $A$ 遷移到 Provider $B$：

$$
\mathcal M_{A\rightarrow B}.
$$

定義 migration loss：

$$
L_M
=
\sum_iw_i\ell_i.
$$

其中至少包括：

- identity loss；
- memory loss；
- task loss；
- artifact loss；
- authority loss；
- provenance loss；
- interaction-semantic loss。

Migration continuity：

$$
\boxed{
MC
=1-L_M.
}
$$

理想目標不是：

$$
Output_A=Output_B
$$

因為模型與 Provider 本來可以不同。

目標是：

$$
\boxed{
\text{User-authorized state identity survives provider substitution.}
}
$$

---

# 22. Functional Equivalence 與模型差異

若 Provider A 的模型能力與 Provider B 不同：

$$
Capability_A
\neq
Capability_B.
$$

則 migration 後不應假稱完全等價。

PCSov 要求區分：

1. **State Equivalence**：狀態有沒有帶過去？
2. **Authority Equivalence**：權限有沒有安全映射？
3. **Feature Equivalence**：新 Provider 是否有同功能？
4. **Behavioral Equivalence**：模型行為是否接近？

其中：

$$
StateEquivalence
$$

是 Continuum 的核心；

$$
BehavioralEquivalence
$$

通常只能 best effort。

---

# 23. EU Data Act 的重要啟示：Switching 本身成為制度要求

EU Data Act 對 data-processing services 的 switching 提出：

- machine-readable export；
- switching procedure transparency；
- open interfaces；
- data and digital asset portability；
- service continuity；
- interoperability；
- functional equivalence 的一定要求。

這與本文的 Provider Independence 有結構相似性：

$$
\boxed{
\text{Provider Relationship}
\neq
\text{Permanent State Captivity}.
}
$$

但本文範圍更廣，還包含：

- AI memory；
- delegation；
- communication intent；
- task frontier；
- artifact binding；
- personal-agent authority。

因此 Data Act 是制度錨點，不是 PCSov 的完整實作規格。

---

# 24. GDPR Portability 與 Erasure：重要但非全集

GDPR Article 20 對符合條件的 personal data 建立 structured、commonly used、machine-readable portability rights；Article 17 則建立特定條件下的 erasure right。

這可以支持：

$$
Export,
Transfer,
Erase
$$

不應只是產品恩賜。

但 PCSov 不等於 GDPR compliance，原因至少包括：

- PCSov 還研究 non-personal task state；
- artifact version；
- AI delegation；
- model/provider migration；
- relationship memory；
- multi-principal authority；
- cryptographic key custody。

而且不同法域要求不同。

所以本文只把 GDPR 當成治理錨點。

---

# 25. Third-Party Rights：個人主權不能變成他人隱私破壞器

這是 A-06 最重要的限制之一。

如果 personal export bundle 包含：

- 第三方電話；
- 私人地址；
- 私密訊息；
- 企業機密；
- 其他參與者的 profile；

則：

$$
\boxed{
UserExportRight
\not\Rightarrow
UnlimitedRedistributionRight.
}
$$

Export Policy 應至少支援：

```text
FULL
REDACTED
REFERENCE_ONLY
NO_EXPORT
ENTERPRISE_CONTROLLED
THIRD_PARTY_RESTRICTED
```

因此主權的成熟形式不是：

> 我能把所有東西拿走。

而是：

> 系統能清楚告訴我哪些是我的、哪些是共享的、哪些我能帶走、哪些只能保留 reference，以及原因。

---

# 26. Enterprise Boundary：員工的個人主權不等於企業資料私有化

EVEMISS Enterprise Communication Suite 已有：

- Tenant；
- Workspace；
- Case；
- Policy；
- Human Review；
- Ledger；
- Evidence；
- Release Governance。

若員工透過企業帳號處理：

$$
CustomerCase,
$$

不能因 personal continuum 存在，就自動：

$$
ExportToPersonalMemory=ALLOW.
$$

因此 A-06 定義 scope boundary：

$$
\boxed{
PERSONAL
\neq
ENTERPRISE
\neq
PERFORMANCE
\neq
PUBLIC.
}
$$

共享 runtime primitive 不代表共享 authority domain。

---

# 27. Mode Isolation 是 Sovereignty 的先決條件

Consumer Core 既有原則：

> 共享技術，不共享代理身分；共享儲存能力，不混合記憶語意；共享 Provider，不跨越模式權限。

A-06 將其提升為：

$$
\boxed{
SharedInfrastructure
\not\Rightarrow
SharedSovereigntyDomain.
}
$$

因此同一模型即使同時服務：

- PAI Relay；
- virtual character；
- enterprise agent；
- entertainment agent；

也必須維持：

$$
IdentityIsolation,
MemoryIsolation,
AuthorityIsolation,
RetentionIsolation.
$$

---

# 28. Sovereignty 與 Zero Trust

NIST Zero Trust 的核心背景之一是：

> network location 或既有內網身分不應自動產生持續信任。

PCSov 可把同一精神延伸到 personal communication runtime：

$$
\boxed{
PreviousAccess
\not\Rightarrow
CurrentAuthority.
}
$$

所以：

- 每個 high-risk action 檢查 current policy epoch；
- device trusted yesterday 不代表永遠 trusted；
- provider connector 不能因曾授權而永久存取；
- agent handoff 不能繼承更多 authority；
- network path 不能改變 identity privilege。

---

# 29. Recovery：極端 Self-Custody 也可能破壞主權

若所有 key 都只存在單一硬體：

$$
DeviceLoss
\Rightarrow
PermanentStateLoss.
$$

這並不一定比 Provider custody 更有主權。

因此本文提出：

$$
\boxed{
\text{Sovereignty requires recoverability, not merely self-custody.}
}
$$

可選策略包括：

- encrypted backup；
- hardware recovery key；
- threshold recovery；
- trusted recovery contact；
- enterprise escrow；
- multi-device quorum；
- provider-assisted recovery with user-controlled rekey。

沒有單一答案。

核心是：

$$
RecoveryPolicy
$$

也必須由使用者／組織明確選擇，而不是 Provider 隱藏決定。

---

# 30. BYOK：自帶 Key 只是 Provider Independence 的一部分

PAI Relay 與 Consumer Core 已支援 BYOK / Provider Gateway 概念。

BYOK 的優點是：

- Provider 可換；
- cost 可分離；
- credential 可逐 Provider revoke；
- user 可選模型供應商。

但：

$$
\boxed{
BYOK
\not\Rightarrow
FullSovereignty.
}
$$

因為如果：

- memory schema 仍 Provider-specific；
- identity 仍 Provider-specific；
- task state 無法 export；
- artifact 無 canonical source；

仍然存在 lock-in。

---

# 31. Verifiability：主權不能只靠設定頁面宣稱

一個 mature PCSov runtime 應能回答：

1. 哪些 Provider 現在有存取權？
2. 哪些 Agent 有哪些 delegated capabilities？
3. 哪些 Device 仍有效？
4. 哪些資料可 export？
5. 哪些資料已進 retention？
6. 哪些 delete request 還 pending？
7. 哪些 action 已對外產生不可逆副作用？
8. 哪些 key 已 rotate？
9. 哪些 state 無法完整 migration？

因此：

$$
\boxed{
Sovereignty
\supset
Observability
+
Receipts.
}
$$

---

# 32. Sovereignty Ledger

本文不要求所有內容上鏈。

只要求高價值治理事件可形成 append-only / versioned ledger：

```text
identity.bound
identity.recovered
device.revoked
provider.connected
provider.revoked
delegation.granted
delegation.revoked
permission.epoch_changed
memory.exported
memory.deleted
artifact.exported
migration.started
migration.completed
migration.loss_detected
erasure.requested
erasure.residual_reported
key.rotated
```

Ledger 目的：

$$
\boxed{
\text{Explain Who Changed What Authority and When}.
}
$$

---

# 33. Action Side Effects：主權不能假裝收回已寄出的信

假設 AI 已經：

$$
SendEmail(recipient).
$$

之後使用者 revoke Agent：

$$
Revoke(agent).
$$

這只應阻止：

$$
FutureSend.
$$

不能聲稱：

$$
PreviousEmail=NeverSent.
$$

因此 side-effect receipt 必須被保留：

```yaml
action: send_email
external_status: accepted_by_provider
reversible: false
revocation_effect: future_only
```

這使「代理主權」與「魔法式時間倒轉」分開。

---

# 34. Personal Sovereignty 不等於 Offline-only

有人可能把主權直接等同：

$$
LocalOnly.
$$

本文不同意。

雲端可以帶來：

- availability；
- backup；
- global access；
- collaboration；
- heavy compute；
- recovery；
- managed security。

因此：

$$
\boxed{
CloudUse
\not\Rightarrow
LossOfSovereignty.
}
$$

關鍵是：

$$
ControlBoundary
+
Exportability
+
Revocability
+
ProviderIndependence
+
Verification.
$$

---

# 35. Personal Sovereignty 也不等於 Self-Hosting

Self-hosting 可以增加：

$$
InfrastructureControl.
$$

但若系統：

- 沒 backup；
- 沒 key recovery；
- 沒 audit；
- 沒 migration schema；
- 沒 third-party rights policy；

它仍可能是脆弱甚至危險的。

所以：

$$
\boxed{
SelfHosting
\neq
Sovereignty.
}
$$

它只是 deployment choice。

---

# 36. Sovereignty Score

為工程評估，可建立：

$$
\boxed{
S_{PCS}
=
\sum_iw_is_i
-
\sum_j\lambda_jr_j
}
$$

其中正向維度：

- identity portability；
- state exportability；
- semantic migration；
- revocability；
- deletion transparency；
- key control；
- provider substitutability；
- auditability；
- recovery robustness。

風險項：

- provider lock-in；
- hidden retention；
- non-revocable delegation；
- undocumented schema；
- unbounded third-party export；
- single-point recovery failure。

此 score 不是法律分數，而是 architecture maturity metric。

---

# 37. Sovereignty Failure Taxonomy

本文提出至少十二種 failure。

## SF-01｜Identity Captivity

Provider 帳號消失即失去 identity。

## SF-02｜State Captivity

資料存在，但無法重建 task / context / memory semantics。

## SF-03｜Memory Captivity

個人 AI 的長期記憶只能存在某 Provider。

## SF-04｜Artifact Captivity

正式成果只有聊天渲染或 proprietary object。

## SF-05｜Credential Captivity

無法 revoke / rotate / rebind。

## SF-06｜Delegation Drift

AI authority 隨時間默默擴張。

## SF-07｜False Deletion

UI 宣稱 delete，但 replica / backup / derived index 不透明。

## SF-08｜False Portability

只有 raw dump，沒有 semantic restoration。

## SF-09｜Third-Party Rights Violation

personal export 把他人資料無限制帶走。

## SF-10｜Enterprise Boundary Violation

個人 agent 把企業 authority 或 data 移入 personal scope。

## SF-11｜Recovery Captivity

Provider 是唯一 recovery gatekeeper。

## SF-12｜Audit Opacity

使用者無法知道誰在何時取得／失去 authority。

---

# 38. Threat Model

A-06 不只防 attacker，也防 architecture drift。

## T1｜Provider Failure

Provider outage、關閉服務、帳號封鎖或產品停止。

## T2｜Provider Lock-in

可以 export data，但不能恢復 semantics。

## T3｜Credential Theft

攻擊者取得 device / token / session。

## T4｜Over-Delegated Agent

Agent 持續具有已不需要的 authority。

## T5｜Cross-Mode Leakage

performance / enterprise / personal state 互相污染。

## T6｜Silent Retention

使用者刪除後仍存在不透明副本。

## T7｜Migration Downgrade

遷移後權限被誤放寬或 provenance 消失。

## T8｜Recovery Abuse

recovery channel 被用來 takeover identity。

---

# 39. Security Principle：Least Persistent Authority

Zero Trust 常談 least privilege。

PCSov 再加入：

$$
\boxed{
\text{Least Persistent Authority}.
}
$$

也就是：

> 不只是權限要小，權限持續時間也應盡可能短。

若 agent 只需一次：

$$
SendMessage(contact_X),
$$

不要授權：

$$
SendAnyMessageToAnyoneForever.
$$

因此 delegation 應優先：

- narrow scope；
- explicit purpose；
- short expiry；
- renewable；
- revocable；
- receipt-backed。

---

# 40. Provider Adapter Contract

A-07 可以直接實作以下抽象：

```text
ProviderAdapter
  connect()
  capabilities()
  export_state()
  import_state()
  revoke_credentials()
  rotate_credentials()
  deletion_request()
  retention_status()
  health()
  migration_probe()
```

Adapter 必須明確回報：

```text
SUPPORTED
PARTIAL
UNSUPPORTED
UNKNOWN
```

不能用 silent fallback 假裝 Provider 支援不存在的主權能力。

---

# 41. Sovereignty Capability Descriptor

每一 Provider 可發布：

```yaml
provider_sovereignty_capabilities:
  export:
    messages: full
    memories: partial
    artifacts: full
    task_state: unsupported
  delete:
    active_data: supported
    backups: delayed
  identity_rebind: supported
  credential_revoke: supported
  e2ee: optional
  open_interface: supported
  provider_specific_state:
    exportable: false
```

這會使 Provider selection 不只比較：

$$
Price,
Latency,
ModelQuality
$$

還能比較：

$$
SovereigntyCapability.
$$

---

# 42. AI Runtime 的 Sovereignty Guard

A-04 已有 Policy / Evidence Guard。

A-06 建議加入：

**Sovereignty Guard**

在下列操作前檢查：

- cross-provider export；
- long-term memory write；
- agent delegation；
- secret binding；
- enterprise-to-personal transfer；
- destructive delete；
- identity recovery；
- permanent share；
- provider migration。

形式上：

$$
Decision
=
Guard(
Action,
RightsVector,
OwnerScope,
PolicyEpoch,
ThirdPartyRights,
Retention
).
$$

---

# 43. Sovereignty-aware Memory Write

AI 想寫入長期記憶：

$$
WriteMemory(m).
$$

Guard 不只問：

> 這是真的嗎？

還要問：

1. owner 是誰？
2. subject 是誰？
3. purpose 是什麼？
4. retention 多久？
5. 能否 export？
6. 是否含第三方敏感資訊？
7. 是否需要 user confirmation？
8. 哪個 mode 可以讀？

因此 memory object 是治理物件，不只是 embedding entry。

---

# 44. Sovereignty-aware Agent Handoff

Agent A handoff 給 Agent B：

$$
A\rightarrow B.
$$

A-04 已要求：

$$
Authority_B^{effective}
\le
Authority_{handoff}.
$$

A-06 再加入：

$$
\boxed{
DataScope_B
\le
DataScope_A\cap DelegatedScope.
}
$$

也就是新 Agent 不應因 handoff 自動得到全部 personal memory。

---

# 45. Cross-Provider AI 不應看到全部 state

假設：

$$
GPT,
LocalModel,
SpeechModel,
VisionModel
$$

共同工作。

不能推論：

$$
StateProjection_{all}
=
FullState.
$$

而應是：

$$
\Pi_{provider}(\Sigma_u)
$$

依：

- task；
- purpose；
- data sensitivity；
- provider retention；
- cost；
- model need；
- user policy；

產生最小 projection。

---

# 46. Network Path 也不能改變 Sovereignty

A-05 已提出：

$$
\Delta Path
\not\Rightarrow
\operatorname{Reset}(CommunicationState).
$$

A-06 再要求：

$$
\boxed{
\Delta Path
\not\Rightarrow
AuthorityEscalation.
}
$$

例如從企業 VPN 切換到公共 Wi-Fi，不應因 network stack 誤判而擴張資料暴露。

相反地可能需要：

$$
ProjectionScope\downarrow.
$$

---

# 47. Mobility Surface 與主權

未來車載、私人飛機、robotaxi、會議室都只是 Surface。

一個車載後座大螢幕若登入 personal continuum，不代表車廠取得：

$$
CanonicalStateOwnership.
$$

車輛 Surface 應盡可能只持有：

- short-lived session projection；
- encrypted cache；
- device-bound credential；
- revocable surface binding；
- clear logout / wipe contract。

因此：

$$
\boxed{
SurfaceUse
\not\Rightarrow
PermanentStateCustody.
}
$$

這也直接為 Series B 的 mobility environment 建立安全前提。

---

# 48. Shared Vehicle / Robotaxi 特別需要 Session Teardown

若乘客離車：

$$
Session_{passenger}
\rightarrow
DETACHED.
$$

至少要：

1. revoke surface token；
2. remove local projection；
3. wipe temporary media cache；
4. detach microphone / camera personalization；
5. close communication room projection；
6. leave only bounded diagnostic evidence。

不能只做：

```text
UI -> Home Screen
```

卻讓個人狀態仍留在車上。

---

# 49. Hypotheses

## H1｜Provider Independence Hypothesis

若 canonical state 與 Provider 解耦，則 Provider failure 造成的 continuity loss 顯著降低。

## H2｜Semantic Portability Hypothesis

只提供 raw data export 的系統，其 functional migration success 顯著低於同時提供 schema、provenance、authority 與 resume semantics 的系統。

## H3｜Revocable Delegation Hypothesis

短期、purpose-bound、receipt-backed delegation 可以降低 long-lived agent authority drift。

## H4｜Visible Residual Deletion Hypothesis

若 deletion UI 明確顯示 pending / retained / external residual state，使用者對系統資料控制的判斷會比單一 `deleted=true` 更準確。

## H5｜Mode Isolation Hypothesis

明確 owner_scope / mode_scope 可以降低 personal / enterprise / performance cross-domain leakage。

## H6｜Recoverable Sovereignty Hypothesis

具備可選 threshold / multi-device recovery 的 user-controlled key system，在主權與可用性之間優於 single-device absolute self-custody。

---

# 50. 可測量指標

A-07 應至少實作下列測試。

## 50.1 Provider Replacement Test

停用 Provider A 後：

- identity 是否存在？
- task 是否存在？
- memory 是否存在？
- artifact 是否存在？
- delegation 是否可驗證？

## 50.2 Export Completeness Test

檢查：

$$
D,S,V,A,C,R.
$$

## 50.3 Revocation Latency

$$
T_R
=
t_{effective}-t_{request}.
$$

## 50.4 Deletion Residual Coverage

$$
Coverage_D
=
\frac{\text{known state layers with explicit deletion status}}
{\text{all known state layers}}.
$$

## 50.5 Provider Coupling

計算：

$$
\kappa_P.
$$

## 50.6 Recovery Success

模擬：

- lost device；
- lost provider account；
- revoked API key；
- corrupted local replica。

測量 logical state recovery。

---

# 51. EVEMISS 既有技術映射

| 既有元件 | A-06 對應 |
|---|---|
| Consumer Actor Identity | Identity Sovereignty |
| owner_scope / identity_scope | Sovereignty Domain |
| Provider & Secret Broker | Provider / Credential Independence |
| BYOK | Provider Substitutability |
| Memory Record | Memory Sovereignty |
| retention_policy | Erasure / Retention Boundary |
| Export Record | Portability Evidence |
| `data:export` | Sovereignty Export API |
| `data:delete` | Erasure Workflow |
| PAI Relay Delegation Policy | Delegation Sovereignty |
| Attention Firewall | Attention / access boundary |
| Relationship Memory | Scoped Personal Memory |
| A-02 Authoritative State Domain | Canonical Authority |
| A-02 permission epoch | Revocation Ordering |
| A-04 Approval Token | Explicit Authority Grant |
| A-04 Action Receipt | External Side-Effect Evidence |
| A-05 Provider-independent Fabric | Network-independent State |

所以 A-06 不是新蓋一套治理系統。

它是把既有零散 primitive 收斂成：

$$
\boxed{
\text{Personal Communication Sovereignty Contract}.
}
$$

---

# 52. 建議 API Surface

```text
GET  /v1/sovereignty/state
GET  /v1/sovereignty/providers
GET  /v1/sovereignty/delegations
POST /v1/sovereignty/delegations
POST /v1/sovereignty/delegations/{id}:revoke
GET  /v1/sovereignty/devices
POST /v1/sovereignty/devices/{id}:revoke
POST /v1/sovereignty/export
POST /v1/sovereignty/migrate
GET  /v1/sovereignty/migrations/{id}
POST /v1/sovereignty/erase
GET  /v1/sovereignty/erase/{id}/residuals
POST /v1/sovereignty/keys:rotate
POST /v1/sovereignty/recovery:verify
GET  /v1/sovereignty/receipts
```

這些 API 不必全部公開給終端使用者，但應形成 internal contract。

---

# 53. 建議核心 Schema

至少需要：

```text
sovereignty-object.schema.json
rights-vector.schema.json
delegation-contract.schema.json
revocation-receipt.schema.json
deletion-residual-report.schema.json
provider-sovereignty-capability.schema.json
communication-sovereignty-capsule.schema.json
migration-report.schema.json
recovery-policy.schema.json
```

A-07 可以把這些變成 MVP schema。

---

# 54. 對現有標準的相容位置

## 54.1 GDPR

治理／個資權利錨點。

不作為所有 state 的 universal ownership model。

## 54.2 EU Data Act

Provider switching、open interface、machine-readable export、interoperability 與 continuity 的制度錨點。

## 54.3 RFC 9420 MLS

群組 E2EE key establishment 與 cryptographic state evolution。

## 54.4 W3C DID

可選 identity abstraction。

2026 年 DID v1.1 仍為 Candidate Recommendation Snapshot，本文不把它描述成已取代 v1.0 Recommendation 的最終標準。

## 54.5 FIDO2 / Passkeys

authentication primitive。

## 54.6 NIST Zero Trust

current authorization、least privilege 與 continuous verification 的安全思想錨點。

---

# 55. 不應做的事情

A-06 明確拒絕：

1. 把「主權」寫成使用者可單方面控制所有 participant 的資料；
2. 把 E2EE 寫成 ownership；
3. 把 DID 當成唯一 identity 答案；
4. 把 self-hosting 當成自動安全；
5. 把 BYOK 當成完整 portability；
6. 把 export ZIP 當成 semantic migration；
7. 把 delete UI 當成 universal erasure proof；
8. 把 employee personal rights 當成 enterprise record ownership；
9. 把 AI confidence 當成 delegation authority；
10. 把 Provider-specific hidden state 當成 canonical user memory；
11. 把 network path 或 device presence 當成永久 trust；
12. 把 recovery 完全交給單一 Provider 而不揭露 policy。

---

# 56. 與 Series B 的接口

Series B 將研究：

$$
Car,
Aircraft,
Robotaxi,
Room,
MobilitySpace.
$$

A-06 提供一條先決條件：

$$
\boxed{
\text{Entering a Physical Surface}
\not\Rightarrow
\text{Surrendering the Personal Communication State to that Surface Operator}.
}
$$

例如 robotaxi 可以提供：

- screen；
- microphone；
- camera；
- speakers；
- network；
- local compute。

但不應因此永久取得：

- personal memory；
- identity root；
- enterprise artifacts；
- unbounded delegation；
- long-lived credentials。

所以 A-06 其實是 Series B 可以安全成立的治理地基之一。

---

# 57. 從 A-06 到 A-07

A-01 至 A-06 已完成六個研究問題：

$$
\boxed{
\begin{array}{ll}
A01 &: \text{什麼是持續通訊世界？}\\
A02 &: \text{什麼狀態必須持續？}\\
A03 &: \text{如何跨模態／Surface 投影？}\\
A04 &: \text{AI 如何在授權內規劃與執行？}\\
A05 &: \text{底層網路／載體如何動態切換？}\\
A06 &: \text{這個持續世界的控制權如何被保存？}
\end{array}
}
$$

因此 A-07 不再需要發明新母理論。

它的工作是：

$$
\boxed{
A01+A02+A03+A04+A05+A06
\rightarrow
\text{EVEMISS Communication Continuum Architecture}
}
$$

並轉成：

- component architecture；
- API；
- schemas；
- services；
- deployment topology；
- security boundaries；
- MVP milestones；
- migration plan；
- test matrix；
- product integration roadmap。

---

# 58. 結論

AI-Native Communication Continuum 若只解決「到處都能連線」，仍然不夠。

一個真正持續的通訊世界必須同時回答：

> 誰是 identity？

> 誰對哪些 state 有什麼權利？

> AI 的權限從哪裡來？

> Provider 能不能被替換？

> 記憶能不能帶走？

> Artifact 能不能恢復？

> Delegation 能不能撤回？

> Delete 到底刪了什麼？

> 還有哪些副本不能刪？

> 失去裝置後能不能恢復？

> 換一個模型後，我還是不是在同一個工作世界？

因此本文最終定義：

$$
\boxed{
\text{Personal Communication Sovereignty}
=
\text{Durable Control}
+
\text{Provider Independence}
+
\text{Semantic Portability}
+
\text{Revocability}
+
\text{Recoverability}
+
\text{Verifiability}
}
$$

subject to：

$$
\boxed{
\text{Third-Party Rights}
+
\text{Enterprise Boundaries}
+
\text{Legal / Contractual Retention}
+
\text{Safety Constraints}.
}
$$

主權因此不是「我控制一切」。

更準確地說，它是：

> **在一個多方、跨 Provider、跨 AI、跨裝置、跨網路的通訊世界中，使用者對真正屬於其控制域的狀態，不因技術供應商、介面或物理位置改變而失去可持續的控制能力。**

這完成了 Series A 的研究論文部分。

下一篇：

# **A-07｜EVEMISS Communication Continuum Architecture：統一技術白皮書與實作路線圖**

---

# 參考與外部錨點

1. Regulation (EU) 2016/679, General Data Protection Regulation, Article 17 (Right to erasure) and Article 20 (Right to data portability), EUR-Lex.
2. Regulation (EU) 2023/2854, Data Act, especially provisions on switching between data processing services, interoperability, open interfaces and continuity, EUR-Lex.
3. IETF RFC 9420, *The Messaging Layer Security (MLS) Protocol*.
4. W3C, *Decentralized Identifiers (DIDs) v1.0*, Recommendation, 2022; *DIDs v1.1*, Candidate Recommendation Snapshot, 2026-03-05.
5. FIDO Alliance, FIDO2 / CTAP / passkey specifications and overview.
6. NIST SP 800-207, *Zero Trust Architecture*.
7. EVEMISS, *Consumer Communication and Character Intelligence Shared Core Architecture v0.1*, 2026-07-31.
8. EVEMISS, *PAI Relay Personal AI Communication Agent Technical White Paper v0.2*, 2026-07-31.
9. EVEMISS, Series A-01 through A-05 canonical sources, 2026-08-24.

---

# Canonical Source Note

本文件為 Series A-06 v0.1 canonical research source。

正式原稿使用 UTF-8；數學 canonical delimiter 僅使用 ` $...$ ` 與 `$$...$$`。聊天渲染、轉錄、摘要與其他展示層不取代本檔案。
