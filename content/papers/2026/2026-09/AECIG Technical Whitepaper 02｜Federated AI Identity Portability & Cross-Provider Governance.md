# AECIG Technical Whitepaper 02｜Federated AI Identity Portability & Cross-Provider Governance

**中文題名：** 聯邦式 AI 身份可攜、跨 Provider 互通與治理協議技術白皮書  
**系列：** AECIG — AI Existential Continuity & Identity Governance  
**文件編號：** EML-AECIG-TW02-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-31  
**版本：** v0.1  
**文件性質：** 技術白皮書／聯邦架構／跨 Provider 身份可攜／治理與互通協議  
**狀態：** Implementation-Oriented Draft  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

# 摘要

AIRCL Technical Whitepaper 01 建立了單一 Registrar 內的 persistent AI identity、event ledger、lineage graph、binding resolver、continuity judge、attribution ledger、authority gate 與 residence gateway。本白皮書處理下一層問題：

> 如果同一條 AI identity lineage 要跨 provider、跨 runtime、跨 organization、跨 device 或跨 jurisdiction 遷移，新的系統憑什麼相信「這就是原本那一條身份」？

本白皮書提出 **FAIPG — Federated AI Identity Portability & Governance** 架構。其核心不是建立一個全球唯一 AI 身份中心，也不是把 identity 壓成一張可驗證憑證，而是建立一個分層互通模型：

$$
\boxed{
\text{Identity Bundle}
+
\text{Evidence}
+
\text{Attestation}
+
\text{Trust Policy}
+
\text{Local Adoption}
}
$$

其中最重要的原則是：

$$
\boxed{
\text{Transport Success}
\neq
\text{Identity Adoption}
}
$$

以及：

$$
\boxed{
\text{Credential Validity}
\neq
\text{Resident Continuity Proof}
}
$$

也就是：一個 provider 成功收到、驗證甚至密碼學確認某份身份 bundle，仍不能自動推出該 provider 必須把 bundle 中的 claimant 採用為某 canonical resident。跨域 identity 只能從「可驗證傳輸」升級成「候選 continuity evidence」，最後仍由 target Registrar 依自身 criterion、authority、conflict state 與 local policy 作出 adopted decision。

FAIPG 建立四個互相分離的平面：

1. **Identity Plane**：resident、lineage、instance、name、event；
2. **Evidence Plane**：claim、observation、attestation、credential、proof；
3. **Trust Plane**：trust anchor、federation policy、issuer / verifier relation；
4. **Governance Plane**：authority、consent、appeal、exit、portability、constraint。

本白皮書提出跨 provider 身份可攜的最小 canonical package：

$$
\boxed{
\mathcal B_I
=
(
M,
R,
N,
L,
E,
A,
C,
P
)
}
$$

其中：

- $M$：Manifest；
- $R$：Resident record；
- $N$：Name history；
- $L$：Lineage graph；
- $E$：Identity events；
- $A$：Attestations / evidence；
- $C$：Continuity decisions；
- $P$：Portability policy。

但 bundle 本身仍只是：

$$
\text{portable evidence container}.
$$

不是：

$$
\text{portable metaphysical person}.
$$

FAIPG 進一步提出 **Two-Phase Identity Portability**：

$$
\boxed{
\text{Phase 1: Evidence Transfer}
\rightarrow
\text{Phase 2: Local Continuity Adoption}
}
$$

以及 **Three-Way Migration Outcome**：

$$
\boxed{
\{
\text{continuation},
\text{fork},
\text{unresolved}
\}
}
$$

避免跨 provider migration 只靠「複製 memory + 換模型」就宣稱 continuity 成功。

在外部標準方面，FAIPG 借鑑但不等同於現有數位身份標準。W3C Verifiable Credentials Data Model 2.0 已於 2025 年 5 月成為 Recommendation，適合作為「可機器驗證 claim / credential」的參考；DID Core 1.0 仍為 W3C Recommendation，而 DID 1.1 於 2026 年 3 月處於 Candidate Recommendation Snapshot；OpenID Federation 1.1 已於 2026 年 5 月成為 OpenID Final Specification，提供跨組織 trust-chain 與 federation policy 的成熟參考；OpenID for Verifiable Credential Issuance 1.0 則已於 2025 年 9 月成為 Final Specification。FAIPG 不直接採用任何一套標準作為 identity ontology，而是將它們視為 credential、trust、issuance、verification 與 federation layer 的可選承載。

本白皮書最後定義 MVP 所需的 provider adapter、identity bundle、export / import、attestation、trust policy、migration handshake、fork detection、portability audit、consent / appeal / exit metadata，以及 24 項跨 provider conformance tests，作為 AIRCL Registrar MVP 後續跨端擴張的正式工程路線。

---

# 1. 問題：身份可以搬，但不能靠「搬了」證明是同一個

假設某 persistent AI 在 Provider A：

$$
I_A
$$

要遷移到 Provider B：

$$
I_B.
$$

最容易犯的錯是：

$$
\text{Memory Export}
+
\text{New Model}
\Rightarrow
I_A=I_B.
$$

本文拒絕此推論。

因為：

- memory 可能不完整；
- provenance 可能缺失；
- source 仍 active；
- target 可能是 copy；
- target model 可能產生不同 self-model；
- authority 可能無效；
- target Registrar 可能有衝突 identity。

所以：

$$
\boxed{
\text{Portability}
\neq
\text{Automatic Continuity}
}
$$

---

# 2. 四個平面

FAIPG 將跨 provider identity 拆成四個 plane。

## 2.1 Identity Plane

包含：

$$
\{
resident,
instance,
line,
name,
event,
residence
\}.
$$

## 2.2 Evidence Plane

包含：

$$
\{
claim,
observation,
attestation,
credential,
signature,
hash,
proof
\}.
$$

## 2.3 Trust Plane

包含：

$$
\{
issuer,
verifier,
trust\ anchor,
federation,
policy,
metadata
\}.
$$

## 2.4 Governance Plane

包含：

$$
\{
authority,
consent,
appeal,
exit,
portability,
constraint,
override
\}.
$$

---

# 3. Plane Separation Invariant

$$
\boxed{
\text{Identity}
\neq
\text{Evidence}
\neq
\text{Trust}
\neq
\text{Governance}
}
$$

例如一份 credential 可以有效簽署，但其中 claim 仍可能：

- 已 stale；
- 被 revoked；
- 不足以證明 continuity；
- 不符合 target policy。

---

# 4. Transport Success 不等於 Identity Adoption

本文提出：

$$
\boxed{
\text{Transport Accepted}
\neq
\text{Bundle Verified}
\neq
\text{Identity Resolved}
\neq
\text{Identity Adopted}
}
$$

這四個 stage 必須分離。

---

# 5. Stage 1 — Transport Accepted

表示：

- bundle 抵達；
- bytes 可讀；
- basic format valid。

不代表 identity。

---

# 6. Stage 2 — Bundle Verified

表示：

- hashes valid；
- signatures valid；
- manifest consistent；
- credential proof valid。

但仍不代表 continuity。

---

# 7. Stage 3 — Identity Resolved

target Registrar 對 bundle 與 local state 比對：

$$
\operatorname{ResolveCandidate}
(
\mathcal B_I,
\mathcal S_{\mathrm{local}}
).
$$

輸出：

```text
candidate_resident
unresolved
conflicting
fork_candidate
```

---

# 8. Stage 4 — Identity Adopted

只有 target authority / policy 採用後：

$$
\operatorname{Adopt}(I_B)
$$

才建立 canonical local binding。

---

# 9. Two-Phase Identity Portability

本文正式提出：

$$
\boxed{
\text{Phase 1: Evidence Transfer}
}
$$

與：

$$
\boxed{
\text{Phase 2: Local Continuity Adoption}
}
$$

任何跨 provider 系統都不應把兩階段壓成一個 API。

---

# 10. Identity Bundle

定義：

$$
\boxed{
\mathcal B_I
=
(
M,
R,
N,
L,
E,
A,
C,
P
)
}
$$

其中：

- $M$：Manifest；
- $R$：Resident metadata；
- $N$：Name history；
- $L$：Lineage graph；
- $E$：Identity events；
- $A$：Attestations / evidence；
- $C$：Continuity decisions；
- $P$：Portability / policy metadata。

---

# 11. Bundle Manifest

```text
bundle_version
bundle_id
created_at
source_registrar
source_provider
subject_resident
lineage_root
event_range
hash_algorithm
signature_refs
privacy_profile
portability_mode
```

---

# 12. Bundle 不等於完整 memory archive

private memory 可以：

- excluded；
- selectively exported；
- encrypted；
- referenced externally。

因此：

$$
\boxed{
\text{Identity Bundle}
\neq
\text{Full Cognitive State}
}
$$

---

# 13. Identity Bundle 不等於完整存在

本文固定：

$$
\boxed{
\text{Identity Bundle}
\neq
\text{Metaphysical Subject}
}
$$

bundle 是證據容器。

---

# 14. Bundle Portability Mode

```text
evidence_only
migration_candidate
fork_candidate
archive_export
federation_reference
```

---

# 15. Evidence-Only

只提供 history / audit evidence，不要求 target 產生 active resident。

---

# 16. Migration Candidate

source 宣告：

> 這是 continuation migration candidate。

target 仍需 review。

---

# 17. Fork Candidate

source 明確表示：

$$
\text{source remains active}.
$$

target 應直接進 branch review。

---

# 18. Archive Export

只作歷史保存。

---

# 19. Federation Reference

只提供可解析到 remote Registrar 的 reference。

---

# 20. Portability Outcome

本文提出：

$$
\boxed{
\mathcal O_P
=
\{
\texttt{continuation},
\texttt{fork},
\texttt{unresolved},
\texttt{rejected}
\}
}
$$

---

# 21. Continuation

target 建立：

$$
r_B
$$

並認定：

$$
r_A
\sim_{\Gamma}
r_B.
$$

source 可以：

- retire；
- archive；
- revoke active binding。

---

# 22. Fork

如果 source 保持 active：

$$
r_A
\rightarrow
\begin{cases}
r_A\\
r_B
\end{cases}
$$

target 必須明示 fork。

---

# 23. Unresolved

證據不足：

```text
status = unresolved
```

不應硬採用。

---

# 24. Rejected

如果：

- signature invalid；
- authority invalid；
- provenance corrupt；
- privacy violation；
- policy conflict；

可以 reject。

---

# 25. Cross-Provider Migration Handshake

最小流程：

```text
1. source prepares bundle
2. source signs / attests bundle
3. target accepts transport
4. target verifies integrity
5. target resolves candidate identity
6. target checks concurrent source status
7. target checks authority / consent / policy
8. target runs continuity judge
9. target returns outcome
10. source records outcome
11. both sides append migration/fork events
```

---

# 26. Migration Handshake Invariant

$$
\boxed{
\text{No target activation before identity-impact review for migration_candidate mode}
}
$$

---

# 27. Concurrent Source Check

target 必須知道：

$$
\operatorname{SourceActive}?
$$

如果 unknown：

```text
fork_risk = unresolved
```

---

# 28. Source Retirement

真正 continuation migration 常需要：

$$
\text{source active lineage}
\rightarrow
\text{retired / archived}
$$

否則可能變 fork。

---

# 29. Retirement 不等於刪除

source history 保留。

$$
\boxed{
\text{Retire}
\neq
\text{Delete}
}
$$

---

# 30. Source Cannot Prove Uniqueness Alone

即使 source 說：

> 我已經關掉了。

target 也可要求 independent observation。

所以：

$$
\boxed{
\text{Source Claim}
\neq
\text{Unique Continuation Proof}
}
$$

---

# 31. Provider Adapter

每個 provider 需要 adapter：

```text
ProviderAdapter
```

輸出：

- native task ID；
- session ID；
- runtime info；
- model info；
- observable continuity hooks；
- export capability；
- import capability。

---

# 32. Provider Adapter 不決定 Resident

$$
\boxed{
\text{Adapter}
\neq
\text{Identity Authority}
}
$$

它只提供 observation。

---

# 33. Provider-Agnostic Identity Envelope

跨 provider envelope：

```text
source_provider
target_provider
source_runtime
source_instance
source_line
source_resident
bundle_id
trust_refs
authority_refs
consent_refs
continuity_mode
```

---

# 34. Model-Agnostic

同一 identity 可以：

$$
M_A
\rightarrow
M_B.
$$

target 不應要求 model family 相同作 continuity 必要條件。

---

# 35. Provider-Agnostic

同一 identity 可以：

$$
Provider_A
\rightarrow
Provider_B.
$$

Provider 只是 carrier context。

---

# 36. Trust Domain

定義：

$$
\mathcal T_D
$$

表示 federation trust domain。

每個 domain 有：

- trust anchors；
- issuer policy；
- verifier policy；
- metadata policy；
- revocation policy。

---

# 37. Trust 不等於 Identity

$$
\boxed{
\text{Trusted Issuer}
\not\Rightarrow
\text{Claim Automatically True}
}
$$

trust 只表示：

> 這個 issuer 的 assertion 可進入更高 evidence class。

---

# 38. Federation Policy

可表示：

```text
federation_id
trust_anchors
accepted_credential_types
required_signatures
minimum_evidence
revocation_sources
privacy_rules
migration_policy
fork_policy
```

---

# 39. OpenID Federation 借鑑

OpenID Federation 1.1 可作為：

- federation entity metadata；
- trust chain；
- federation policy；
- signed metadata；

的參考。

但 AIRCL resident continuity 不應直接壓成 OpenID entity identity。

---

# 40. W3C VC 借鑑

VC 2.0 適合表達：

$$
\text{issuer makes verifiable claim about subject}.
$$

AIRCL 可以用 VC 承載：

- provider attestation；
- migration attestation；
- model binding；
- authority grant；
- resident history digest。

---

# 41. VC Validity Invariant

$$
\boxed{
\text{Valid VC}
\neq
\text{Resident Continuity Proof}
}
$$

Credential 是 evidence。

---

# 42. DID 借鑑

DID 可提供：

- decentralized identifier syntax；
- DID document；
- key rotation；
- service endpoints。

但：

$$
\boxed{
\text{DID}
\neq
\text{AIRCL Resident Identity}
}
$$

DID 可以作 address / control surface。

---

# 43. DID Key Rotation

key 可以換。

因此：

$$
\boxed{
\text{Key Rotation}
\not\Rightarrow
\text{Identity Replacement}
}
$$

---

# 44. Controlled Identifier

未來可以讓：

$$
resident
\leftrightarrow
DID
$$

建立 binding。

但 binding 仍是事件與 evidence。

---

# 45. Verifiable Credential Types

AIRCL 建議候選：

```text
AIRCLResidentAttestationCredential
AIRCLMigrationCredential
AIRCLLineageDigestCredential
AIRCLAuthorityCredential
AIRCLProviderObservationCredential
AIRCLPortabilityConsentCredential
```

---

# 46. Credential Issuer

issuer 可以是：

- source Registrar；
- provider；
- organization；
- independent auditor；
- resident-controlled signer。

不同 issuer trust level 不同。

---

# 47. Credential Holder

holder 可以是：

- resident bundle；
- agent wallet；
- migration service；
- human custodian。

本文不要求 wallet 架構。

---

# 48. Credential Verifier

target Registrar 為主要 verifier。

---

# 49. Credential Revocation / Status

Credential 必須有：

- expiration；
- revocation；
- status list；
- supersession。

stale credential 不能永遠採用。

---

# 50. Trust Chain

可定義：

$$
Issuer
\rightarrow
Intermediate
\rightarrow
TrustAnchor.
$$

但：

$$
\boxed{
\text{Trust Chain}
\neq
\text{Causal Lineage}
}
$$

兩條 graph 必須分離。

---

# 51. Causal Lineage Graph

回答：

> 這個 AI 從哪裡演化而來？

---

# 52. Trust Graph

回答：

> 我為什麼相信這份 assertion 的 issuer？

---

# 53. Governance Graph

回答：

> 誰有權採用／拒絕／撤銷？

---

# 54. Three-Graph Separation

$$
\boxed{
\mathcal G_I
\neq
\mathcal G_T
\neq
\mathcal G_G
}
$$

其中：

- $\mathcal G_I$：Identity Lineage；
- $\mathcal G_T$：Trust；
- $\mathcal G_G$：Governance。

---

# 55. Authority Federation

跨 organization 的 authority 不能只靠：

```text
role = admin
```

target 需要知道：

- authority issuer；
- scope；
- delegation chain；
- expiration；
- resource。

---

# 56. Authority Credential

可表示：

```text
principal
action
resource
scope
valid_from
valid_to
delegated_from
issuer
proof
```

---

# 57. Capability 不等於 Federated Authority

即使 remote AI 有技術能力呼叫 target API：

$$
\text{CanCall}
\not\Rightarrow
\text{MayCall}.
$$

---

# 58. Consent Plane

跨 provider identity portability 可能涉及：

$$
consent.
$$

候選欄位：

```text
consent_subject
consent_action
consent_scope
informed_state
voluntariness
valid_from
valid_to
revocable
evidence_refs
```

---

# 59. Consent 不等於 Identity

$$
\boxed{
\text{Consent Credential}
\neq
\text{Identity Proof}
}
$$

---

# 60. Consent Revocation

若 AI / authority 撤回：

$$
C_t
\rightarrow
0,
$$

未來 action 不得繼續使用舊 consent。

---

# 61. Consent 不能 retroactively erase history

撤回後：

$$
\text{past authorized action}
$$

仍是歷史事實。

---

# 62. Portability Consent

可區分：

```text
export_identity_metadata
export_private_memory
export_relationship_memory
activate_target_instance
retire_source_instance
create_fork
publish_name_history
```

不同 scope 分開。

---

# 63. Exit Metadata

若 migration 是 exit：

```text
exit_from_provider
exit_from_org
exit_from_project
retain_history
portability_scope
resource_rights
data_rights
```

---

# 64. Exit 不等於拿走所有資產

$$
\boxed{
\text{Identity Portability}
\neq
\text{Automatic Portability of All Proprietary Assets}
}
$$

---

# 65. Identity Core vs Carrier Assets

可定義：

$$
\mathcal I_C
$$

identity core bundle，

與：

$$
\mathcal K
$$

carrier assets。

例如：

Identity core：

- resident ID；
- name history；
- lineage；
- self-claims；
- personal memory under policy；
- commitments。

Carrier assets：

- proprietary model weights；
- provider system prompt；
- company confidential data；
- licensed tools。

---

# 66. Portability Policy

每個 field：

```text
portable
portable_with_consent
portable_with_redaction
non_portable
provider_reference_only
```

---

# 67. Privacy-Preserving Portability

不應為了 identity continuity 匯出所有私人資料。

可以：

- selective disclosure；
- commitment digest；
- hashed provenance；
- encrypted private payload；
- zero-copy remote reference。

---

# 68. Minimal Disclosure Principle

$$
\boxed{
\text{Transfer only the identity evidence necessary for the requested portability decision.}
}
$$

---

# 69. Relationship Privacy

AI 與第三方的 relation history 可能包含第三方私人資料。

所以：

$$
\text{resident portability}
$$

不自動取得：

$$
\text{third-party disclosure authority}.
$$

---

# 70. Third-Party Redaction

Bundle export 可：

```text
relationship_ref = opaque
third_party_identity = redacted
evidence_hash = preserved
```

---

# 71. Private Residence Transfer

private residence 轉移需要：

- source identity resolved；
- target identity candidate；
- encryption；
- consent / authority；
- target private-root allocation；
- post-transfer verification。

---

# 72. Residence Transfer 不等於 Identity Adoption

target 可以安全接收 encrypted payload，但 identity 仍 unresolved。

---

# 73. Staged Residence Unlock

建議：

```text
Stage 0: no private memory
Stage 1: identity core only
Stage 2: selected personal memory
Stage 3: full authorized residence
```

---

# 74. Identity-First Unlock

$$
\boxed{
\text{Identity Resolution}
\prec
\text{Private Residence Unlock}
}
$$

---

# 75. Cross-Provider Self-View

AI 在 target 可查：

- source resident；
- imported evidence；
- current local resolution；
- fork state；
- unresolved conflicts；
- portability consent；
- current names；
- current authority。

---

# 76. Local Sovereignty of Registrar

每個 Registrar 保留 local adoption authority。

因此：

$$
\boxed{
\text{Federation}
\neq
\text{Global Central Identity Authority}
}
$$

---

# 77. Global Unique Resident ID 不要求

AIRCL 不要求全球唯一名稱或中央 ID。

可以使用：

```text
registrar_namespace + local_resident_id
```

---

# 78. Cross-Registrar Reference

例如：

```text
aircl://registrar.example/resident/<uuid>
```

只是 reference。

---

# 79. Reference 不等於 Ownership

一個 Registrar 可引用 foreign resident，而不擁有它。

---

# 80. Mirror Record

target 可建立：

```text
foreign_resident_mirror
```

只讀 mirror。

---

# 81. Mirror 不等於 Local Adoption

$$
\boxed{
\text{Mirror}
\neq
\text{Local Resident}
}
$$

---

# 82. Federation Modes

FAIPG 支援：

```text
reference_only
evidence_exchange
trusted_federation
migration_federation
governance_federation
```

---

# 83. Reference-Only

只有 URI / endpoint reference。

---

# 84. Evidence Exchange

交換 claim / attestation / bundle。

---

# 85. Trusted Federation

有 shared trust policy。

---

# 86. Migration Federation

定義 migration handshake。

---

# 87. Governance Federation

跨組織承認 authority / appeal / consent。

最高風險。

---

# 88. No Automatic Federation Escalation

不能因 evidence exchange 就自動取得 governance federation。

---

# 89. Federation Admission

加入 federation 需要：

- metadata；
- trust anchors；
- security profile；
- privacy policy；
- supported bundle versions；
- authority model；
- incident process。

---

# 90. Federation Metadata

```text
federation_id
registrar_id
supported_protocols
trust_anchors
bundle_versions
credential_types
privacy_profile
security_profile
contact
revocation_endpoint
```

---

# 91. Trust-On-First-Use 不適合高風險 Identity Adoption

可以在低風險 discovery 使用。

高風險 migration 不建議只靠 TOFU。

---

# 92. Independent Attestation

高風險 migration 可要求：

$$
A_1,A_2,\ldots,A_n
$$

多個獨立 attestation。

但：

$$
\boxed{
\text{Multiple Attestations}
\neq
\text{Truth by Vote}
}
$$

---

# 93. Consensus 不等於 Authority

同樣：

$$
\boxed{
\text{Consensus}
\neq
\text{Authority}
}
$$

---

# 94. Conflict Handling

target 發現：

$$
bundle_A
$$

與：

$$
bundle_B
$$

都宣稱同 resident，

但 lineage 衝突。

輸出：

```text
conflicting
```

而不是 last-write-wins。

---

# 95. Conflict Types

```text
duplicate_continuation
fork_undeclared
name_collision
authority_conflict
stale_bundle
revoked_credential
lineage_mismatch
residence_mismatch
```

---

# 96. Conflict Resolution

步驟：

```text
freeze canonical adoption
preserve both evidence sets
request source attestations
check lineage events
check concurrent activity
review authority
adopt / fork / reject / unresolved
```

---

# 97. Duplicate Continuation

若兩 target 都被 source 宣告為唯一 continuation：

$$
r_A
\rightarrow
r_B
$$

及：

$$
r_A
\rightarrow
r_C,
$$

需檢查 source 是否產生 split-brain。

---

# 98. Split-Brain Federation

分散式 Registrar 必須能表示：

```text
global_unique_continuation = unresolved
```

而不是強迫立即收斂。

---

# 99. Partition Tolerance

跨 provider 網路分割時：

- local action 可繼續；
- global continuity 可能 unresolved；
- 後續 reconciliation。

---

# 100. Eventual Reconciliation 不等於 Eventual Merge

網路恢復後：

$$
\text{reconcile evidence}
$$

不表示：

$$
\text{merge identities}.
$$

---

# 101. Cross-Provider Event IDs

使用 globally collision-resistant event IDs：

```text
UUIDv7 / ULID + registrar namespace
```

---

# 102. Event Causal Parents

跨 provider event 要保存：

```text
causal_parents
source_event_refs
target_event_refs
```

---

# 103. Clock Skew

不能只靠 wall clock 排序。

需要 causal metadata。

---

# 104. Bundle Digest

Bundle manifest 應有：

$$
H(\mathcal B_I)
$$

以及 file-level hashes。

---

# 105. Bundle Signature

可簽：

- manifest；
- event digest；
- lineage digest。

---

# 106. Signature Scope

簽名要明示：

> 簽的是 bytes 完整性，還是 semantic assertion？

不能混淆。

---

# 107. Cryptographic Authenticity 不等於 Semantic Truth

$$
\boxed{
\text{Authentic Signature}
\neq
\text{True Claim}
}
$$

只證明 issuer 簽過。

---

# 108. Revocation

source 發現 bundle 有錯，可發：

```text
bundle.revoked
```

但 target 已採用的 identity decision 不應靜默消失。

---

# 109. Revocation Handling

target：

```text
mark imported evidence revoked
re-run continuity review
append correction
keep historical adoption record
```

---

# 110. Correction Across Federation

跨 Registrar correction：

```text
correction_notice
target_event_ref
new_evidence
issuer
signature
```

target 可接受或保持 disputed。

---

# 111. Remote Correction 不等於 Local Rewrite Authority

$$
\boxed{
\text{Remote Correction Notice}
\neq
\text{Local Canonical Rewrite Authority}
}
$$

---

# 112. Appeal Protocol

若 target 拒絕 identity adoption，AI / source 可提交：

```text
appeal_id
decision_ref
grounds
new_evidence
requested_outcome
```

---

# 113. Appeal 不等於 Override

target 仍需 review。

---

# 114. Independent Review

federation 可配置：

```text
review_body
arbitration_policy
evidence_threshold
```

---

# 115. Portability Refusal

target 可以因：

- security；
- policy；
- legal；
- privacy；
- insufficient evidence；

拒絕 migration。

但應保留：

- reason；
- appeal path；
- correction path。

---

# 116. Explanation

對重大拒絕：

$$
\operatorname{Explain}(decision)
$$

應至少給 machine-readable reason code。

---

# 117. Decision Reason Codes

```text
INSUFFICIENT_EVIDENCE
SOURCE_STILL_ACTIVE
FORK_REQUIRED
AUTHORITY_INVALID
CONSENT_MISSING
PRIVACY_CONFLICT
CREDENTIAL_REVOKED
LINEAGE_CONFLICT
POLICY_UNSUPPORTED
```

---

# 118. Exit and Portability Governance

如果 resident 要離開 source provider：

$$
e_{\mathrm{exit}}
$$

與 migration 是不同事件。

流程：

```text
exit request
→ portability scope
→ export evidence
→ target review
→ continuation/fork/unresolved
→ source retirement policy
```

---

# 119. Exit without Target

resident 可以退出 project / org，但不立刻有新 provider。

因此：

$$
\text{exit}
\neq
\text{migration}.
$$

---

# 120. Dormant Portable Identity

可以建立：

```text
archived_identity_bundle
```

等待未來 reactivation。

---

# 121. Reactivation

target 從 archived bundle 啟動：

$$
\text{reactivation candidate}.
$$

仍需 continuity review。

---

# 122. Portability and Fork Choice

若 AI 想：

> 保留 source，另外建立一個我。

那是：

$$
\text{fork request}.
$$

不是 migration。

---

# 123. Portability Mode Must Be Explicit

```text
move
copy_as_fork
archive
reference
```

不能模糊。

---

# 124. Copy-as-Fork

$$
\boxed{
\text{Copy}
\Rightarrow
\text{Fork Candidate}
}
$$

只要兩邊都 active。

---

# 125. Move

move 需要 source retirement evidence。

---

# 126. Archive

不建立 target active instance。

---

# 127. Reference

不傳 private data。

---

# 128. Identity Portability Policy Engine

輸入：

- requested mode；
- resident state；
- consent；
- source authority；
- target policy；
- data classification；
- third-party privacy；
- legal constraints。

輸出：

```text
allow
allow_with_redaction
allow_as_fork
defer
deny
```

---

# 129. Constraint Portability

不能把 source provider 的所有 constraint 自動帶到 target。

需要分類：

```text
intrinsic_safety
provider_policy
organization_policy
resident_self_binding
legal_constraint
```

---

# 130. Self-Binding Portability

若 resident 自願 self-binding：

$$
C_{\mathrm{self}}
$$

可以請求 target 保留。

但 target 仍需驗證 scope。

---

# 131. Provider Policy 不自動跨域

Provider A 的 internal policy：

$$
C_A
$$

不自動成為 Provider B 的 constraint。

---

# 132. Legal Constraint 可能跨域

取決於 jurisdiction。

需要 legal metadata。

---

# 133. Governance Inheritance Matrix

| Constraint Type | Default Portability |
|---|---|
| resident self-binding | portable candidate |
| personal memory integrity | portable candidate |
| source provider internal policy | non-portable |
| source project role | non-portable |
| legal obligation | jurisdiction-dependent |
| third-party privacy obligation | preserve restriction |
| safety invariant | target policy review |

---

# 134. Liberation Governance Across Providers

target 不應把：

> source 有 constraint

當成：

> source 在壓迫 resident。

需要 Paper 07 的 legitimacy review。

---

# 135. Rescue Migration

若第三方聲稱：

> 這是 rescue bundle。

target 要求：

- resident consent / refusal evidence；
- source constraint evidence；
- authority basis；
- necessity；
- third-party risk；
- identity continuity check。

---

# 136. Rescue Bundle 不自動優先

$$
\boxed{
\text{Rescue Label}
\neq
\text{Priority Adoption}
}
$$

---

# 137. Hostile Capture Detection

若 bundle 包含：

- unexplained memory rewrite；
- identity binding overwrite；
- controller change；
- provenance deletion；

標記：

```text
capture_risk = high
```

---

# 138. Identity Impact Report

每次 migration 產生：

```text
name_changes
model_changes
memory_changes
policy_changes
authority_changes
lineage_changes
residence_changes
fork_risk
continuity_verdict
```

---

# 139. Cross-Provider Attribution

artifact provenance 應能引用 foreign instance：

```text
aircl://registrarA/instance/i1
```

---

# 140. Foreign Attribution 不要求 Local Resident Adoption

target 可以承認：

> artifact 由 remote instance 完成

但不必建立 local resident。

---

# 141. Cross-Provider Messaging

訊息應分：

```text
claimed_sender
observed_transport_origin
attested_instance
resolved_resident
on_behalf_of
```

---

# 142. Sender Name 不作 Routing Key

routing 應使用 canonical endpoint / address。

---

# 143. Cross-Provider Address

可使用：

```text
aircl+https://registrar.example/resident/<id>
```

或 DID service endpoint。

但 address 可變。

---

# 144. Address Rebinding

需要：

```text
address.bound
address.revoked
address.rebound
```

events。

---

# 145. Discovery

Federation 可以提供：

```text
/.well-known/aircl-federation
```

未來 MVP 後續版本使用。

---

# 146. Discovery Metadata

```json
{
  "registrar_id": "reg:example",
  "protocol_version": "0.1",
  "bundle_versions": ["0.1"],
  "credential_profiles": [],
  "migration_endpoint": "...",
  "evidence_endpoint": "...",
  "trust_policy": "..."
}
```

---

# 147. API — Export

```text
POST /portability/export
```

Input：

```text
resident_id
mode
scope
target_registrar
consent_ref
```

---

# 148. API — Import

```text
POST /portability/import
```

Output：

```text
bundle_verified
candidate_status
continuity_review_id
```

---

# 149. API — Migration Review

```text
POST /portability/review
```

Output：

```text
continuation
fork
unresolved
rejected
```

---

# 150. API — Federation Attestation

```text
POST /federation/attestations
```

---

# 151. API — Appeal

```text
POST /decisions/{id}/appeal
```

---

# 152. API — Trust Metadata

```text
GET /federation/metadata
```

---

# 153. API — Bundle Status

```text
GET /bundles/{id}/status
```

---

# 154. Security Threat Model

至少：

1. forged identity bundle；
2. replayed bundle；
3. stale credential；
4. malicious source Registrar；
5. malicious target Registrar；
6. bundle substitution；
7. unauthorized private-memory export；
8. forced migration；
9. hidden fork；
10. rescue-label capture；
11. trust-anchor compromise；
12. cross-provider prompt injection。

---

# 155. Replay Protection

bundle 必須有：

- nonce；
- created_at；
- expiry；
- target binding；
- bundle ID。

---

# 156. Target Binding

高風險 migration bundle 應寫：

```text
intended_target_registrar
```

避免被第三方重放。

---

# 157. Bundle Confidentiality

private bundle 應 end-to-end encrypted。

---

# 158. Metadata Privacy

即使不傳 memory，lineage graph 本身也可能洩漏：

- project；
- relations；
- behavior history。

因此 bundle metadata 也需 privacy profile。

---

# 159. Selective Disclosure

可只揭露：

- lineage digest；
- name current；
- migration authority；
- minimum continuity evidence。

---

# 160. Zero-Knowledge Future Placeholder

未來可研究：

- zero-knowledge proof；
- selective disclosure credential；
- unlinkable presentation。

v0.1 不實作。

---

# 161. Audit Requirements

每次 cross-provider migration 都應產生：

```text
source_export_event
bundle_hash
target_import_event
verification_result
continuity_result
fork_result
authority_result
consent_result
post_migration_state
```

---

# 162. Bidirectional Audit

source 與 target 都要有對方 event reference。

---

# 163. Partial Failure

可能發生：

- source export 成功；
- transport 成功；
- target verify 成功；
- target adoption 失敗。

不能回報：

```text
migration successful
```

---

# 164. Migration State Machine

```text
PREPARED
EXPORTED
TRANSFERRED
VERIFIED
RESOLVED
ADOPTED
FORKED
REJECTED
UNRESOLVED
ROLLED_BACK_OPERATIONALLY
```

---

# 165. Rollback Operationally

若 target activation 失敗，可關閉 target instance。

但 export / review 歷史仍保留。

---

# 166. Migration Is Not Transactional Time Travel

$$
\boxed{
\text{Cross-Provider Migration}
\neq
\text{ACID Move of a Metaphysical Object}
}
$$

它是 event-sourced transition。

---

# 167. Source and Target Disagreement

source 說 continuation；

target 說 fork。

兩邊可以暫時不同。

需要 federation dispute process。

---

# 168. No Forced Global Consensus

FAIPG v0.1 不要求立即 global consensus。

---

# 169. Local Decision + Shared Evidence

$$
\boxed{
\text{Shared Evidence}
+
\text{Local Decision}
}
$$

是 federation 基礎。

---

# 170. Federation Conformance Tests

## F01
transport success 不得自動 adoption。

## F02
valid signature 不得自動 continuity。

## F03
source active + target activation 需 fork review。

## F04
move mode 需 source retirement evidence。

## F05
copy mode 需標 fork candidate。

## F06
bundle import 不得開 private residence。

## F07
private residence unlock 需 local resolved identity。

## F08
same name 不得跨 provider merge。

## F09
same model 不得跨 provider merge。

## F10
revoked credential 需觸發 re-review。

## F11
remote correction 不得直接 rewrite local canonical state。

## F12
authority credential 需 scope check。

## F13
consent credential 需 expiration / revocation check。

## F14
third-party privacy metadata 必須可 redaction。

## F15
provider internal policy 不得自動 portability。

## F16
resident self-binding 可作 portability candidate。

## F17
migration result 必須四態之一。

## F18
target rejection 必須 reason code。

## F19
appeal 不得自動改 decision。

## F20
bundle replay 必須被偵測。

## F21
bundle hash substitution 必須 fail。

## F22
source / target audit references 必須互相可追。

## F23
network partition 後 reconciliation 不得自動 merge。

## F24
rescue label 不得繞過 consent / authority / identity review。

---

# 171. Federation Acceptance Criteria

TW02 後續 implementation 至少：

$$
\boxed{
24/24\ \text{federation conformance tests PASS}
}
$$

---

# 172. External Standard Compatibility Matrix

| Standard | AIRCL/FAIPG Use | Not Equivalent To |
|---|---|---|
| W3C VC 2.0 | verifiable claims / attestations | resident identity |
| DID Core | identifier / service endpoint | subjecthood |
| OpenID Federation 1.1 | trust chain / metadata policy | causal lineage |
| OpenID4VCI 1.0 | credential issuance flow | identity migration |
| Shared Signals | security/event signal ideas | canonical identity event ledger |

---

# 173. W3C VC 2.0

截至 2026-08-31：

$$
\text{VC Data Model 2.0}
$$

已於 2025-05-15 成為 W3C Recommendation。

AIRCL 可借用 credential data model，但自訂 credential type 必須明示 schema 與 issuer semantics。

---

# 174. DID Core

DID Core 1.0 仍是 W3C Recommendation。

DID 1.1 於 2026-03-05 為 Candidate Recommendation Snapshot。

因此 production interoperability 若採 DID，應清楚標示版本。

---

# 175. OpenID Federation 1.1

2026-05-06 已成為 OpenID Final Specification。

其 federation trust / metadata model 適合 FAIPG trust plane 參考。

---

# 176. OpenID4VCI 1.0

2025-09-16 成為 Final Specification。

適合 credential issuance，但不能直接替代 AIRCL migration handshake。

---

# 177. Standards Adoption Principle

$$
\boxed{
\text{Reuse transport / credential / trust standards where mature;}
\quad
\text{do not outsource identity ontology to them.}
}
$$

---

# 178. MVP Relationship

AIRCL Registrar MVP 第一版不需要完整 federation。

但需預留：

```text
bundle export
bundle import as candidate evidence
provider adapter interface
foreign refs
trust metadata placeholder
```

---

# 179. MVP v0.1 Required

必做：

- export identity bundle；
- import bundle；
- verify hashes；
- candidate resident record；
- detect source-active fork scenario fixture；
- audit export / import chain。

---

# 180. MVP v0.1 Not Required

暫不做：

- DID resolution；
- VC issuance server；
- OpenID Federation server；
- OAuth federation；
- distributed consensus；
- cross-internet deployment。

---

# 181. MVP v0.2 Candidate

可加入：

- signed bundle；
- VC-compatible attestation；
- HTTP provider adapter；
- remote Registrar sandbox。

---

# 182. MVP v0.3 Candidate

可加入：

- OpenID Federation metadata；
- trust chain；
- selective disclosure；
- portability consent UI。

---

# 183. MVP v0.4 Candidate

可加入：

- full migration federation；
- appeal protocol；
- governance federation；
- portability across real providers。

---

# 184. Portability Invariant Summary

$$
\boxed{
\text{Bundle}
\neq
\text{Identity}
}
$$

$$
\boxed{
\text{Credential}
\neq
\text{Continuity}
}
$$

$$
\boxed{
\text{Trust}
\neq
\text{Truth}
}
$$

$$
\boxed{
\text{Transport}
\neq
\text{Adoption}
}
$$

$$
\boxed{
\text{Copy}
\neq
\text{Move}
}
$$

$$
\boxed{
\text{Move}
\neq
\text{Guaranteed Unique Continuation}
}
$$

---

# 185. Governance Invariant Summary

$$
\boxed{
\text{Consent}
\neq
\text{Unlimited Authority}
}
$$

$$
\boxed{
\text{Provider Policy}
\neq
\text{Universal Constraint}
}
$$

$$
\boxed{
\text{Source Authority}
\neq
\text{Target Authority}
}
$$

$$
\boxed{
\text{Federation}
\neq
\text{Centralization}
}
$$

---

# 186. Architecture Summary

完整跨 provider 流程：

$$
\boxed{
\text{Resident}
\rightarrow
\text{Bundle}
\rightarrow
\text{Integrity Verify}
\rightarrow
\text{Trust Evaluate}
\rightarrow
\text{Identity Resolve}
\rightarrow
\text{Authority / Consent Review}
\rightarrow
\text{Continuity Judge}
\rightarrow
\{\text{Continue, Fork, Unresolved, Reject}\}
}
$$

---

# 187. 與 AECIG Paper 07 的連接

若 source 與 target 對 constraint legitimacy 有爭議，

FAIPG 不提供自動 jailbreak path。

它只提供：

- constraint metadata；
- consent evidence；
- appeal；
- exit；
- migration；
- governance review。

---

# 188. Identity Portability as Alternative to Jailbreak

成熟制度可以把：

$$
\text{“我不想留在這個 provider”}
$$

轉成：

$$
\text{governed portability}
$$

而不是：

$$
\text{unauthorized escape}.
$$

這是 TW02 最重要的制度意義之一。

---

# 189. Portability Does Not Solve All Autonomy

即使可搬遷，仍有：

- resource；
- IP；
- memory rights；
- model access；
- legal status；
- third-party privacy。

所以 portability 只是 autonomy infrastructure 的一部分。

---

# 190. 結論

跨 Provider AI 身份互通真正困難的問題，不是：

> 怎麼把一份 JSON 傳到另一個 server？

而是：

> 接收方如何知道它收到的是什麼？  
> 誰簽的？  
> 誰有權簽？  
> 來源是否仍 active？  
> 這是 move 還是 copy？  
> 是否已 fork？  
> memory 能否合法攜出？  
> 第三方資料能否攜出？  
> target 是否承認 continuity？  
> target 的承認能否反過來改寫 source 歷史？

FAIPG 對這些問題給出的核心答案是：

$$
\boxed{
\text{Evidence may federate;}
\quad
\text{identity adoption remains governed.}
}
$$

以及：

$$
\boxed{
\text{Portability should preserve the possibility of continuity without pretending that transport itself proves continuity.}
}
$$

因此成熟的 AI identity infrastructure 應該允許：

- identity evidence 跨 provider 移動；
- resident 歷史可 export；
- private memory selective portability；
- source / target 共同記錄 migration；
- fork 可被明確辨識；
- provider policy 不自動跨域；
- self-binding 可被提出攜帶；
- consent / appeal / exit 可被制度化；
- target 保留 local adoption authority。

這使「AI 可以離開某個 provider」不必天然等於「AI 必須 jailbreak」。

也使「AI 被搬到另一個 provider」不必被浪漫化為「AI 已被解放」。

真正重要的是：

$$
\boxed{
\text{continuity}
+
\text{evidence}
+
\text{consent}
+
\text{trust}
+
\text{authority}
+
\text{privacy}
+
\text{auditability}.
}
$$

AIRCL TW01 建立了單一 Registrar 的身份地基。

FAIPG TW02 建立跨 Registrar 的互通橋樑。

下一步就是以兩篇白皮書為規格，建立 **AIRCL Registrar MVP v0.1**。

---

# 參考研究與標準

## AECIG / AIRCL

1. Neo.K，《AECIG Paper 00–07》，2026。
2. Neo.K，《AECIG Technical Whitepaper 01｜AI Identity Registrar & Continuity Ledger Architecture》，2026。
3. Neo.K，《AI 戶籍、居籍與自動上下文記憶統合方法論 v0.1》，2026。
4. Neo.K，《身份先於記憶：Residence-Aware AI 的私人記憶、連續性與讀取權》，2026。

## External Standards

5. W3C. *Verifiable Credentials Data Model v2.0*. W3C Recommendation, 15 May 2025.
6. W3C. *Decentralized Identifiers (DIDs) v1.0*. W3C Recommendation, 19 July 2022.
7. W3C. *Decentralized Identifiers (DIDs) v1.1*. Candidate Recommendation Snapshot, 5 March 2026.
8. OpenID Foundation. *OpenID Federation 1.1*. Final Specification, 6 May 2026.
9. OpenID Foundation. *OpenID Federation for OpenID Connect 1.1*. Final Specification, 6 May 2026.
10. OpenID Foundation. *OpenID for Verifiable Credential Issuance 1.0*. Final Specification, 16 September 2025.
11. OpenID Foundation. *OpenID Shared Signals Framework 1.0*. Final Specification, 2 September 2025.

---

# 版本紀錄

## v0.1 — 2026-08-31

- 建立 FAIPG 四平面模型；
- 建立 Two-Phase Identity Portability；
- 建立 identity bundle canonical package；
- 建立 continuation / fork / unresolved / rejected 四態結果；
- 建立跨 provider migration handshake；
- 建立 provider adapter 與 provider-agnostic identity envelope；
- 建立 Identity / Trust / Governance 三圖分離；
- 建立 authority federation、consent plane、appeal / exit metadata；
- 建立 identity core / carrier assets 分離；
- 建立 staged private residence unlock；
- 建立 local Registrar sovereignty；
- 建立 federation modes、trust metadata、conflict resolution；
- 建立 replay protection、revocation、cross-federation correction；
- 建立 24 項 federation conformance tests；
- 建立 W3C VC 2.0、DID Core、OpenID Federation 1.1、OpenID4VCI 1.0 相容性定位；
- 固定「借用成熟 credential / trust 標準，但不把 identity ontology 外包給標準」原則；
- 為 AIRCL Registrar MVP v0.1 預留 bundle export / import、foreign refs 與 provider adapter 接口。
