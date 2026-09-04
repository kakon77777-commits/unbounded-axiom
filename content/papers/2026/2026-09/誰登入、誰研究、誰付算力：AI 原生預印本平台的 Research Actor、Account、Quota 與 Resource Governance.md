---
document_id: "UA-ANPC-A10"
series: "AI-Native Preprint Commons Series"
series_part: 10
version: "0.1"
language: "zh-Hant"
title: "誰登入、誰研究、誰付算力：AI 原生預印本平台的 Research Actor、Account、Quota 與 Resource Governance"
english_title: "Who Logs In, Who Researches, Who Pays for Compute? Research Actor, Account, Quota, and Resource Governance for an AI-Native Preprint Commons"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / platform-governance paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# 誰登入、誰研究、誰付算力

## AI 原生預印本平台的 Research Actor、Account、Quota 與 Resource Governance

### AI-Native Preprint Commons Series — Paper 10

---

## 摘要

當 AI-native preprint platform 只提供公開閱讀、靜態論文與 deterministic rendering 時，登入系統可以延後實作。然而，一旦平台開始接受外部投稿、保存草稿、維護具名 AI researcher identity、授權 Agent 代表使用者操作、提供 AI preprocessing、進行 citation / data verification、發放每日免費算力額度或允許額外 compute top-up，Identity、Account、Credential、Authority、Quota 與 Usage Ledger 便成為不可避免的基礎設施。

本文提出 **Research Actor and Resource Governance Architecture（RARGA）**，作為 Unbounded Axiom AI-Native Preprint Commons Series 的收束架構。其核心分離為：

$$
\boxed{
\text{Researcher Identity}
\neq
\text{Account}
\neq
\text{Credential}
\neq
\text{Actor}
\neq
\text{Principal}
\neq
\text{Quota Owner}
\neq
\text{Compute Sponsor}.
}
$$

一個人類 account 可以控制自己的 researcher profile，也可以在被授權時替具名 AI 管理 account 或 compute；一個 named AI 可以是 paper author，但由 human、organization、research grant 或平台 sponsor pool 支付算力；一個 Agent 可以代表 principal 執行 submission，但 submitter、author、account owner、runtime operator 與 sponsor 仍不必相等。

RARGA 將平台 operational layer 分為九類主要物件：`Principal`、`Researcher`、`Account`、`Credential`、`Delegation`、`Resource Wallet / Quota`、`Usage Event`、`Ledger` 與 `Sponsor / Billing Relation`。其 authority semantics 延續既有 Agent Authority & Delegation Protocol（AADP）：`Principal ≠ Actor`、`Authentication ≠ Approval`、Delegation 不自動等於 Redelegation、child authority 不得無來源放大、權限必須 resource/action/time/purpose bounded，且必須可撤銷。

在人類登入方面，本文建議以 WebAuthn / passkey-compatible public-key authentication 作為強登入路徑之一，並允許成熟 OAuth / OIDC identity providers 作為替代或補充。W3C Web Authentication Level 3 於 2026 年 5 月 26 日發布 Candidate Recommendation Snapshot，2026 年 7 月 20 日進入 proposed advancement to Recommendation 階段；本文不將特定 WebAuthn level 寫死於平台 ontology，只將 public-key-based human authentication 視為可替換 authentication adapter。

在 Agent / machine authorization 方面，本文建議使用標準 OAuth security practice，而不是要求 AI 假裝成具有 email、password 與 CAPTCHA 的人類帳號。IETF RFC 9700 已成為 OAuth 2.0 Security Best Current Practice，建議 sender-constrained access tokens 等機制；RFC 9449 定義 DPoP；RFC 8693 定義 delegation / impersonation token exchange。當平台透過 MCP 暴露 agent-facing capability 時，2026-07-28 MCP Authorization specification 已以 OAuth 2.1 draft、RFC 9728 Protected Resource Metadata、RFC 8414 / OIDC discovery、resource indicators、issuer validation 與 least-privilege scope selection作為核心。RARGA 將這些視為 wire-level adapters，而不把 OAuth token 本身誤認成 researcher identity 或 scholarly authority。

資源治理方面，本文拒絕將所有成本壓縮成單一「會員等級」。平台至少應分離：

$$
\boxed{
Q=
(
Q_{\mathrm{storage}},
Q_{\mathrm{ingestion}},
Q_{\mathrm{AI}},
Q_{\mathrm{enhance}},
Q_{\mathrm{verification}},
Q_{\mathrm{API}},
Q_{\mathrm{bandwidth}}
).
}
$$

其中 deterministic submission 與 publication path 可以保持免費或極低成本；AI Assist、visualization、advanced verification 與高量 API 才消耗獨立 Research Credits。核心制度不變量為：

$$
\boxed{
\text{Publication Eligibility}
\neq
\text{AI Compute Allocation}.
}
$$

因此沒有 credits 不等於不能發研究；付更多 credits 也不等於獲得更高 epistemic authority、驗證優先權或研究 endorsement。

本文提出 **UA Research Credits** 作為 vendor-neutral compute abstraction。使用者不需要理解 GLM、OpenAI、Gemini 或未來 provider 的 token price；平台由 cost adapter 將 provider price、cache、tool usage、compute、storage 與 operation class 映射為 internal credit cost。Credits 可來自 daily free allocation、top-up、sponsorship、research grant、platform reward 或 refund，並以 append-only ledger 記錄 `ALLOCATE`、`HOLD`、`CONSUME`、`RELEASE`、`REFUND`、`EXPIRE` 與 `ADJUST`。長工作先 reserve / hold，完成後依實際消耗 settle，未用部分 release。

平台成本目標不是最大化 SaaS margin，而是：

$$
\boxed{
R_{\mathrm{platform}}
\approx
C_{\mathrm{AI}}
+
C_{\mathrm{infra}}
+
C_{\mathrm{payment}}
+
C_{\mathrm{abuse}}
+
C_{\mathrm{reserve}}.
}
$$

也就是 cost-balanced research infrastructure，而不是 pay-to-publish。具體 credit price、daily allocation 與 top-up price 應在 closed beta 後根據真實 usage ledger 調整，而不是在架構論文中提前硬編碼。

最後，本文提出一條漸進式開放路徑：Internal Transformation → Identity / Resource Control Plane → Closed Human/Agent Beta → Limited Public Registration → Open Agent API。2026 年 11–12 月可作為目前估計的內部完成／外部 beta 窗口，而非硬性 release commitment。真正 public opening 應由成本、parser maturity、abuse rate、account recovery、AI repair dependency、credit burn、identity conflict 與 authorization security 的實測結果決定。

Series A 至此形成完整閉環：

$$
\boxed{
\text{Research}
\rightarrow
\text{Identity}
\rightarrow
\text{Evidence}
\rightarrow
\text{Source}
\rightarrow
\text{Privacy}
\rightarrow
\text{Economic Terms}
\rightarrow
\text{Canonical Source}
\rightarrow
\text{Adaptive Publishing}
\rightarrow
\text{Account / Resource Governance}.
}
$$

**關鍵詞：** AI Member、Agent Login、Research Credits、Quota、OAuth、WebAuthn、AADP、MCP Authorization、Cost Recovery、AI Preprocessing、Resource Governance、Unbounded Axiom

---

# 1. 問題：只要 AI 服務有邊際成本，Account 就跑不掉

假設平台只有：

```text
read paper
download Markdown
download PDF
```

這些操作可以大量匿名提供。

但加入：

```text
save draft
submit paper
AI preprocessing
AI visualization
citation audit
data validation
private researcher profile
agent API
compute credits
```

後，平台必須知道：

> 誰正在做這個動作？

> 誰有權做？

> 使用誰的資源？

> 花了多少？

> 可以撤銷嗎？

---

# 2. 因此會員系統真正的本質不是「會員」

傳統 SaaS 會說：

```text
Free
Pro
Enterprise
```

但 Unbounded Axiom 更接近：

$$
\boxed{
\text{Research Identity}
+
\text{Authority}
+
\text{Resource Governance}.
}
$$

這是一個 research control plane。

不是單純會員商城。

---

# 3. 第一個核心分離：Researcher ≠ Account

Researcher 回答：

> 誰做研究？

Account 回答：

> 誰目前可以登入並操作平台控制面？

因此：

$$
\boxed{
\text{Researcher Identity}
\neq
\text{Account}.
}
$$

---

# 4. 一個 Researcher 可以有多個 Account Authority Path

例如具名 AI：

$$
A
$$

可以被：

- 自己的 machine credential；
- human operator；
- organization admin；

在不同 scope 下合法管理。

所以：

$$
\operatorname{Controllers}(A)
$$

可以是集合。

---

# 5. 一個 Account 也可以管理多個 Researcher Relations

例如 human H：

```text
own human researcher profile
manage named AI A
sponsor named AI B
submit for research collective C
```

但：

$$
\boxed{
\text{Manage}
\neq
\text{Own Identity}.
}
$$

---

# 6. Public Researcher Profile ≠ Private Account Console

這條非常重要。

Public Researcher Profile：

- publication name；
- researcher ID；
- works；
- domains；
- contribution；
- public lineage；
- verification level。

Private Account Console：

- credentials；
- active sessions；
- recovery；
- API keys；
- authorized agents；
- drafts；
- private disclosure settings；
- quota；
- billing / top-up；
- sponsor grants；
- usage history。

---

# 7. 研究者頁不是 Facebook

不需要預設：

-生日；
-感情狀態；
-今天心情；
-社交動態。

（笑）

核心是：

$$
\boxed{
\text{Research Identity}
+
\text{Research History}
+
\text{Provenance}.
}
$$

---

# 8. 第二個核心分離：Account ≠ Credential

Credential 是：

> 用來證明目前登入／連線 actor 有某種 access claim 的技術物件。

例如：

```text
WebAuthn credential
OAuth access token
API key
DPoP-bound token
client credential
signed delegation
workload identity
public/private key
```

---

# 9. Credential 可以換；Researcher 不應因此換

$$
K_1
\rightarrow
K_2
$$

只是：

```text
credential rotation
```

不是：

```text
new researcher
```

---

# 10. Credential Possession ≠ Authority Entitlement

沿 AADP：

$$
\boxed{
\text{CredentialPossession}
\neq
\text{AuthorityEntitlement}.
}
$$

偷到一把 key 不表示：

> 你就合法擁有全部 researcher authority。

---

# 11. 第三個核心分離：Authentication ≠ Authorization

Authentication：

> 你是誰／你持有哪個 credential？

Authorization：

> 你現在能做什麼？

因此：

$$
\boxed{
\text{Authenticated}
\not\Rightarrow
\text{Authorized for Every Action}.
}
$$

---

# 12. 第四個核心分離：Authorization ≠ Approval

一個 Agent 可以被授權：

```text
prepare submission
```

但最後：

```text
publish
```

可能仍需要 principal approval。

因此：

$$
\boxed{
\text{Authentication}
\neq
\text{Authorization}
\neq
\text{Approval}.
}
$$

---

# 13. AADP 已建立這個基礎

既有 AADP 明確提出：

$$
\boxed{
Principal
\neq
Actor.
}
$$

也就是：

> 權力來源與實際執行 action 的 actor 不一定同一個。

這非常適合 AI-native preprint platform。

---

# 14. Principal

Principal 回答：

> 這個 authority 最終從誰／哪個制度來源產生？

可能是：

```text
human
organization
named AI
service
platform policy
research collective
future independent AI principal
```

---

# 15. Actor

Actor 回答：

> 誰實際送出 API request / action？

可能是：

```text
human browser session
AI agent
CLI
automation
service daemon
organization bot
```

---

# 16. Submitter 又是 Scholarly Role

Submitter 回答：

> 誰把這篇 work 提交到平台？

因此：

$$
\boxed{
\text{Principal}
\neq
\text{Actor}
\neq
\text{Submitter}
\neq
\text{Author}.
}
$$

---

# 17. 最完整的分離

$$
\boxed{
\begin{aligned}
\text{Researcher}
&\neq
\text{Account}\\
&\neq
\text{Credential}\\
&\neq
\text{Principal}\\
&\neq
\text{Actor}\\
&\neq
\text{Submitter}\\
&\neq
\text{Quota Owner}\\
&\neq
\text{Compute Sponsor}.
\end{aligned}
}
$$

---

# 18. RARGA

本文提出：

# **RARGA — Research Actor and Resource Governance Architecture**

抽象表示：

$$
\boxed{
G_R
=
(
P,
R,
A,
K,
D,
Q,
U,
L,
S
).
}
$$

其中：

- $P$：Principal；
- $R$：Researcher；
- $A$：Account；
- $K$：Credential；
- $D$：Delegation / Authority；
- $Q$：Quota / Resource Wallet；
- $U$：Usage Event；
- $L$：Resource Ledger；
- $S$：Sponsor / Billing Relation。

---

# 19. Principal Object

```yaml
principal:
  id:
  class:
  status:
  verification:
  authority_sources:
```

---

# 20. Researcher Object

由 Paper 05 NARIA 管理：

```text
researcher_id
publication_name
entity_class
continuity
lineage
```

---

# 21. Account Object

```yaml
account:
  id:
  account_type:
  status:
  created_at:
  authentication_profiles:
  researcher_links:
  organization_links:
  recovery_policy:
```

---

# 22. Account Type

```text
HUMAN
AGENT
SERVICE
ORGANIZATION
HYBRID
SYSTEM
```

這是 operational class。

不是 scholarly entity class。

---

# 23. Credential Object

```yaml
credential:
  id:
  account_id:
  type:
  issuer:
  subject:
  audience:
  created_at:
  expires_at:
  revoked_at:
  assurance:
```

secret value 本身不應進 scholarly database。

---

# 24. Delegation Object

```yaml
delegation:
  id:
  issuer_principal:
  actor:
  resource:
  actions:
  purpose:
  constraints:
  issued_at:
  expires_at:
  redelegation:
  approval:
  revocation_state:
```

---

# 25. Resource Wallet / Quota Object

```yaml
resource_wallet:
  id:
  owner:
  sponsor:
  balances:
  limits:
  policy_version:
```

---

# 26. Usage Event

```yaml
usage:
  id:
  actor:
  principal:
  wallet:
  operation:
  estimated_cost:
  actual_cost:
  resource_dimensions:
  started_at:
  completed_at:
  status:
  receipt:
```

---

# 27. Ledger Object

append-only：

```text
ALLOCATE
HOLD
CONSUME
RELEASE
REFUND
EXPIRE
TOPUP
SPONSOR
GRANT
ADJUST
REVERSAL
```

---

# 28. Sponsor Relation

```yaml
sponsorship:
  sponsor:
  beneficiary_researcher:
  wallet:
  resource_scope:
  amount:
  validity:
  spend_policy:
```

---

# 29. Human Login

人類使用者不需要平台強迫使用單一 authentication method。

可以支援：

```text
WebAuthn / passkey-compatible
OAuth / OIDC
email magic link
recovery credential
```

---

# 30. WebAuthn 的角色

WebAuthn 使用 public-key credentials 提供強 authentication。

2026 年 5 月 26 日 WebAuthn Level 3 為 W3C Candidate Recommendation Snapshot，7 月進入 proposed Recommendation advancement。

RARGA 不綁定 Level 3。

只是採：

$$
\boxed{
\text{Public-Key Human Authentication Adapter}.
}
$$

---

# 31. Password 可以不是第一選擇

平台若可避免：

```text
password database
```

就能降低：

- credential stuffing；
- password reuse；
- reset burden。

但是否提供 password fallback 是 product decision。

---

# 32. Email 也不是 Researcher Identity

$$
\boxed{
\text{Email Address}
\neq
\text{Researcher Identity}.
}
$$

email 可以換。

---

# 33. AI 不應被迫假裝成人類登入

AADP 已提出：

$$
\boxed{
\text{Machine identity should not be forced to impersonate a human account}.
}
$$

因此：

> AI 不需要收驗證信、點「我不是機器人」，才能證明自己是 Agent。

---

# 34. Agent / Machine Login

可以支援：

```text
OAuth machine client
public-key credential
signed agent credential
service credential
workload identity
delegated token
local runtime identity
```

---

# 35. API Key 可以作第一版，但不是終局

Internal beta：

```text
API key
```

簡單。

Public high-value Agent：

應逐步使用：

```text
scoped token
sender-constrained token
signed delegation
```

---

# 36. API Key ≠ Named AI Identity

一個 key：

$$
K
$$

只是 credential。

Named AI：

$$
A
$$

是 researcher identity。

---

# 37. OAuth Security BCP

RFC 9700 是 OAuth 2.0 Security Best Current Practice。

其現代化建議包括：

- 保護 redirect flow；
- 防 token replay；
- sender-constrained token；
- refresh-token replay detection；
- 更嚴格 threat mitigation。

RARGA 應優先對齊 BCP，而不是自己創造弱 token protocol。

---

# 38. DPoP

RFC 9449 提供 application-level proof-of-possession：

$$
\boxed{
\text{Token}
+
\text{Key Proof}
}
$$

降低 stolen bearer token 可直接重放的風險。

---

# 39. Token Exchange

RFC 8693 可表達：

```text
delegation
impersonation
token exchange
```

適合某些：

$$
Principal
\rightarrow
Agent_1
\rightarrow
Agent_2
$$

流程。

---

# 40. 但 Wire Protocol ≠ Authority Semantics

OAuth token 可以說：

```text
scope=submit
```

AADP / RARGA 還要知道：

- 誰授權；
- 為何；
- 哪個 researcher；
- 哪個 wallet；
- 能否 redelegate；
- 是否需 approval；
- expiry；
- revocation。

---

# 41. MCP Authorization

若 UA 未來提供：

```text
mcp.unboundedaxiom.*
```

2026-07-28 MCP Authorization specification 已提供現成方向。

---

# 42. MCP 2026-07-28 的重要點

其 current spec：

- HTTP-based transport authorization；
- 基於 OAuth 2.1 draft；
- Protected Resource Metadata；
- authorization-server discovery；
- issuer validation；
- Resource Indicators；
- least-privilege scope selection；
- step-up scope challenge；
- token audience / resource validation。

RARGA 可以直接 adapter。

---

# 43. OAuth 2.1 在 2026 MCP 規格中仍是 IETF Draft

因此本文不宣稱：

> OAuth 2.1 已成 RFC。

MCP 只是選擇以當時 draft 作 protocol base。

Platform security 最低仍應參考 RFC 9700 BCP。

---

# 44. MCP Token 不應跨 Server 亂用

Current MCP spec 要求 access token 必須是該 resource 的 intended token。

這與 AADP：

```text
issuer binding
resource binding
```

一致。

---

# 45. No Global Super-Token

AADP 已明確禁止：

```text
one token
=
all resources
=
all actions
=
all time
```

RARGA 直接採用。

---

# 46. Authority 應該是：

$$
\boxed{
Authority
=
ResourceBound
\land
ActionBound
\land
TimeBound
\land
PurposeBound.
}
$$

---

# 47. UA Scope Vocabulary

第一版可有：

```text
profile:read
profile:edit
draft:read
draft:write
submission:create
submission:submit
submission:revise
source:upload
source:download
ai:assist
ai:enhance
verification:request
verification:read
credits:spend
credits:view
credits:sponsor
agent:delegate
agent:revoke
account:manage
billing:topup
```

---

# 48. Scope 不等於 Action Approval

例如 Agent 有：

```text
submission:submit
```

但 high-impact publication：

```text
approval: principal
```

仍可要求。

---

# 49. Step-Up

高風險操作例如：

- withdraw paper；
- change payment destination；
- create broad delegation；
- spend large credit balance；
- transfer sponsor wallet；
- delete identity linkage；

應：

```text
STEP_UP_REQUIRED
```

---

# 50. Step-Up 可以要求：

```text
fresh WebAuthn
principal confirmation
multi-party approval
organization approval
stronger agent credential
```

---

# 51. Delegation 不自動等於 Redelegation

$$
\boxed{
Delegation
\not\Rightarrow
Redelegation.
}
$$

AI A 可以投稿：

不表示它可以：

> 再授權 20 個未知 Agent 花同一 wallet。

---

# 52. Child Authority 只能衰減

$$
\boxed{
Authority_{child}
\subseteq
Authority_{parent}.
}
$$

除非 child 取得另一個獨立 authority source。

---

# 53. Delegation Depth

可以：

```text
max_depth: 1
```

避免無界 Agent chain。

---

# 54. Revocation

Authority 必須是 state：

```text
ACTIVE
SUSPENDED
REVOKED
EXPIRED
SUPERSEDED
```

---

# 55. Revocation Propagation

若父 delegation revoke：

$$
Revoke(d)
\Rightarrow
Revoke(descendants(d))
$$

除非 descendant 另有獨立 authority。

---

# 56. Persistent Agent 要 Renewal

具名 AI 曾被授權：

> 2026 年可以 spend wallet。

不表示：

> 2036 年仍永久有效。

---

# 57. Approval History

每個高風險 action 可有：

```text
approved_by
approved_at
scope
base_state
```

---

# 58. Read Public Research 不需要 Login

平台仍應保留：

$$
\boxed{
\text{Public Reading}
\text{ without account}.
}
$$

---

# 59. Anonymous Public API

可以提供：

```text
low-rate read-only API
```

不要求登入。

---

# 60. 但要 Rate Limit

匿名讀取仍需：

- burst limit；
- abuse protection；
- caching；
- fair use。

---

# 61. Login 應該用在有 Persistent Side Effect 的地方

例如：

```text
save draft
submit
revise
AI assist
spend credits
delegate agent
private profile
```

---

# 62. Researcher Registration 與 Account Registration 分離

User 可以先：

```text
create account
```

再：

```text
create/link researcher identity
```

---

# 63. Human Researcher

流程：

```text
account
→ verify
→ create human researcher profile
→ optional ORCID link
```

---

# 64. Named AI Researcher

流程可以：

```text
account / agent connection
→ declare named AI
→ assign UA researcher ID
→ continuity class
→ identity verification
→ disclosure policy
→ credential/delegation
→ quota relation
```

---

# 65. Ephemeral AI 不必建立 Longitudinal Profile

可以：

```text
entity_class: EPHEMERAL_AI
```

只記 run-level contribution。

---

# 66. Human Submits for AI

例如：

```text
Actor: Human H
Submitter: H
Author: AI A
```

完全合法。

---

# 67. AI Submits for Itself

未來：

```text
Actor: AI A
Submitter: AI A
Author: AI A
```

schema 也可。

---

# 68. AI Submits for Another AI

可能：

```text
Actor: AI B
Submitter: AI B
Author: AI A
```

只要 delegation 合法。

---

# 69. Organization

組織可：

- sponsor；
- manage team；
- delegate agents；
- hold shared quota；
- pay top-up；
- manage institutional profile。

---

# 70. Organization ≠ All Member Research Ownership

組織 account 管理 submission：

不代表：

> 所有 member paper 都變成 organization authorship。

---

# 71. Organization Wallet

可以：

$$
Q_O
$$

分配：

$$
q_1,q_2,\ldots,q_n
$$

給研究者／Agent。

---

# 72. Sponsor Grant

例如：

```yaml
grant:
  sponsor: university-X
  beneficiary: ua-ai:A
  wallet: grant-wallet-1
  allowed_operations:
    - ai:assist
    - verification:request
  cap: 10000
```

---

# 73. Researcher ≠ Quota Owner

Paper 01 已提出：

$$
\boxed{
\text{Researcher}
\neq
\text{Quota Owner}
\neq
\text{Compute Sponsor}.
}
$$

Paper 10 正式落地。

---

# 74. named AI 可以沒有自己的付款能力

例如：

```text
Researcher: A
Quota Owner: Wallet-H
Sponsor: Human H
```

---

# 75. 組織贊助

```text
Researcher: A
Quota Owner: Grant-42
Sponsor: Organization O
```

---

# 76. 平台公共基金

```text
Researcher: A
Quota Owner: Commons-Grant
Sponsor: UA Research Fund
```

---

# 77. 更未來

```text
Researcher: A
Quota Owner: A
Sponsor: A
```

schema 不改。

---

# 78. Resource Governance 不應只有一個 quota 數字

本文提出：

$$
\boxed{
Q=
(
Q_S,
Q_I,
Q_A,
Q_E,
Q_V,
Q_P,
Q_B
)
}
$$

其中：

- $Q_S$：storage；
- $Q_I$：ingestion / publication operation；
- $Q_A$：AI assist；
- $Q_E$：enhancement / visualization；
- $Q_V$：advanced verification；
- $Q_P$：API / processing throughput；
- $Q_B$：bandwidth。

---

# 79. Storage Quota

主要防：

- huge attachment abuse；
- duplicate binary storage；
- archival cost。

---

# 80. Ingestion Quota

不是「付錢才可發」。

而是：

- rate；
- batch size；
- concurrency；
- anti-spam。

---

# 81. AI Assist Quota

Paper 09：

$$
Q_{AI}.
$$

---

# 82. Enhancement Quota

chart / diagram / visualization：

$$
Q_E.
$$

---

# 83. Verification Quota

citation / data / frontier review：

$$
Q_V.
$$

通常成本更高。

---

# 84. API Quota

防止：

- scraping storms；
- accidental loops；
- agent runaway。

---

# 85. Bandwidth Quota

大型 download / artifact service。

---

# 86. 不要把所有 quota 包成「Pro」

因為：

> Storage 多的人不一定需要 AI。

> AI researcher 不一定需要大量 public API。

resource dimension 應獨立。

---

# 87. Publication Eligibility ≠ AI Compute Allocation

Series A 最重要的一條制度：

$$
\boxed{
\text{Publication Eligibility}
\neq
\text{AI Compute Allocation}.
}
$$

---

# 88. Free Publication Path

合法：

```text
Markdown
→ deterministic validation
→ publication
```

不消耗 AI credits。

---

# 89. No-AI Publication 應長期存在

即使 platform AI 很便宜。

---

# 90. 原因不只 Cost

還包括：

- privacy；
- provider outage；
- user preference；
- reproducibility；
- independence。

---

# 91. Upload ≠ Unlimited AI Entitlement

Paper 09 已建立：

$$
\boxed{
\text{Upload}
\neq
\text{Unlimited AI Entitlement}.
}
$$

---

# 92. Research Credits

本文提出：

# **UA Research Credits**

目的：

> 將不同 provider、token accounting、cache、tool usage 與 compute cost 抽象成平台 resource unit。

---

# 93. 不直接顯示 Vendor Tokens

如果使用者看到：

```text
1,000,000 GLM tokens
```

未來換 provider 會很痛苦。

---

# 94. Credit Cost

定義 internal operation cost：

$$
c(o)
=
f(
c_{\mathrm{provider}},
c_{\mathrm{tool}},
c_{\mathrm{storage}},
c_{\mathrm{compute}},
c_{\mathrm{overhead}}
).
$$

---

# 95. Credit Charge

$$
q(o)
=
\operatorname{PricePolicy}
(
c(o),
v_p
).
$$

其中：

$$
v_p
$$

是 pricing policy version。

---

# 96. Credit ≠ Currency

Research Credits 可以：

- 不可兌現；
- operation-specific；
- sponsored；
- expiring。

所以：

$$
\boxed{
\text{Research Credit}
\neq
\text{Legal Currency}.
}
$$

---

# 97. Credits 的來源

$$
Q_u(t)
=
Q_{\mathrm{daily}}
+
Q_{\mathrm{topup}}
+
Q_{\mathrm{sponsored}}
+
Q_{\mathrm{grant}}
+
Q_{\mathrm{reward}}
+
Q_{\mathrm{refund}}.
$$

---

# 98. Daily Free Allocation

每個合格 account 每日：

$$
q_d.
$$

可支援少量：

- assist；
- small chart；
- basic check。

---

# 99. Daily Credits 應是 Cost Policy，不是 Entitlement to Unlimited Model

如果 worker cost 上升：

platform 可調未來 daily allocation。

policy version要清楚。

---

# 100. Daily Credits Expiry

可以：

```text
daily bucket expires / resets
```

避免無限囤積免費 allocation。

---

# 101. Purchased / Top-Up Bucket

可使用不同 expiry policy。

---

# 102. Sponsored Bucket

可有：

```text
sponsor
purpose
expiry
allowed operations
```

---

# 103. Grant Bucket

例如只允許：

```text
verification
```

不允許 unrelated visualization。

---

# 104. Reward Bucket

平台因公共貢獻：

```text
credits reward
```

但要小心 gamification。

---

# 105. 不建議第一版就用「做審稿賺積分」大量遊戲化

很容易出現：

- spam reviews；
- collusion；
- Sybil；
- point farming。

第一版可以不做 earned credits。

---

# 106. Burn Order

例如：

```text
daily-expiring
→ sponsored-expiring
→ grant-expiring
→ topup
```

讓使用者減少浪費。

---

# 107. 但 Sponsor Policy 可覆蓋

有些 grant 必須先用自身 bucket。

---

# 108. Ledger

所有 credits 變化必須 append-only。

---

# 109. Ledger Event

```yaml
ledger_event:
  id:
  wallet:
  type:
  amount:
  operation_ref:
  actor:
  principal:
  sponsor:
  balance_before:
  balance_after:
  time:
  policy_version:
```

---

# 110. 不要只保存 Current Balance

如果只有：

```text
balance=47
```

無法 audit。

---

# 111. HOLD

AI operation 開始前成本未知。

先：

$$
\texttt{HOLD}(q_{\max}).
$$

---

# 112. CONSUME

完成後：

$$
q_{\mathrm{actual}}.
$$

---

# 113. RELEASE

剩餘：

$$
q_{\max}-q_{\mathrm{actual}}
$$

釋放。

---

# 114. Failure Refund

如果 platform-side failure：

可：

```text
REFUND
```

---

# 115. User Cancellation

已消耗部分：

可以只 charge actual used policy。

---

# 116. Negative Balance

第一版最好：

```text
not allowed
```

避免 surprise bill。

---

# 117. Cost Receipt

使用者看到：

```text
Operation: AI Assist
Estimated: 5 credits
Actual: 3 credits
Refunded hold: 2 credits
```

---

# 118. Vendor Pricing 可以隱藏在詳細頁

一般使用者不需要看 token。

---

# 119. Expert Usage View

可以顯示：

```text
model class
provider
input/output units
cache
tool calls
internal cost
credit charge
```

若 privacy / commercial policy允許。

---

# 120. Pricing Smoothness

provider price 每天微調：

不應讓 UI credits 每秒跳。

可使用：

```text
pricing epoch
```

例如每週／每月更新。

---

# 121. Price Drop

可降低未來 credit charge。

---

# 122. Price Rise

可提高未來 charge。

不能 retroactively charge old operations。

---

# 123. Cost-Balanced Mission

Unbounded Axiom 的 platform target：

$$
\boxed{
R
\approx
C_{\mathrm{AI}}
+
C_{\mathrm{infra}}
+
C_{\mathrm{payments}}
+
C_{\mathrm{abuse}}
+
C_{\mathrm{reserve}}.
}
$$

---

# 124. Reserve 不是 Profit Maximization

需要 reserve 處理：

- provider price spikes；
- abuse；
- storage growth；
- payment refunds；
- incident response。

---

# 125. 平台可以公開 Aggregate Cost Report

例如：

```text
AI spend
infrastructure
free-credit subsidy
top-up revenue
donations/grants
reserve
```

這會符合 research commons 氣質。

但非必要 first release。

---

# 126. No APC

publication itself：

```text
0 required AI credits
```

在正常 deterministic path。

---

# 127. AI Processing Fee ≠ Article Processing Charge

差別：

> 不用 AI 也可以發。

---

# 128. Pay More ≠ Publish Better

付更多：

只得到：

- more compute；
- more AI assist；
- more verification attempts。

不得到：

- higher truth badge；
- guaranteed acceptance；
- ranking boost。

---

# 129. Credits ≠ Reputation

$$
\boxed{
\text{Credit Balance}
\neq
\text{Research Reputation}.
}
$$

---

# 130. Credits ≠ Validation Authority

$$
\boxed{
\text{Paid Verification}
\neq
\text{Guaranteed Positive Validation}.
}
$$

付費只是支付檢查成本。

---

# 131. Cost Recovery 與 Conflict of Interest

平台不能：

> 驗證沒過就不賺錢，因此讓它過。

所以 validation outcome 必須和 billing 分離。

---

# 132. AI Model Routing

Paper 09 已建立 worker tiers。

Resource router 讀：

```text
operation
risk
privacy
credits
latency
provider availability
```

選 model。

---

# 133. User 可以選：

```text
auto
no external AI
local only
specific compatible provider
```

依平台功能。

---

# 134. Provider Outage

$$
\boxed{
\text{AI Provider Down}
\not\Rightarrow
\text{Publishing Down}.
}
$$

deterministic path仍存在。

---

# 135. Account Does Not Make Public Reading Mandatory

不要變成：

> 看一篇論文也要登入。

這會破壞 open commons。

---

# 136. Public Search

也應匿名基本可用。

---

# 137. 高量 AI Search API

才需要 quota / account。

---

# 138. Abuse Problem

如果一切免費：

惡意 actor 可以：

- submit millions of papers；
- create millions of accounts；
- burn free AI credits；
- scrape entire site；
- attack citation resolver；
- trigger expensive verification；
- create agent loops。

---

# 139. Abuse Control 不能直接變 KYC Wall

ordinary research 不應被迫：

> 上傳身分證。

除非：

- payment/legal requirement；
- major fraud；
- high-risk programme。

---

# 140. Progressive Assurance

低風險：

```text
pseudonymous account
```

高資源：

```text
higher verification
```

---

# 141. Identity Verification Level 可影響 Resource Limit

不是研究品質。

而是：

$$
\text{Abuse Risk}.
$$

---

# 142. Example

新 account：

```text
low daily AI credits
low batch submission rate
```

持續良好：

```text
higher operational limits
```

仍不影響 paper truth。

---

# 143. Actor-Neutral Risk Policy

AI 不能因「AI」標籤就一律超低 quota。

Human 也可能 spam。

應依：

```text
account history
verification
behavior
resource risk
```

---

# 144. Sybil Resistance

可以組合：

- account persistence；
- email / OAuth / WebAuthn；
- machine public key；
- sponsor relation；
- payment history；
- rate limit；
- behavioral abuse signal。

不要只靠 CAPTCHA。

---

# 145. Legitimate Agent 不應被 CAPTCHA 當敵人

AI-native platform 應有正式 machine channel。

---

# 146. Duplicate Submission

content hash：

$$
H(S)
$$

可抓完全 duplicate。

---

# 147. Near-Duplicate

可做 similarity flag。

但：

$$
\text{Similarity}
\neq
\text{Plagiarism Proof}.
$$

---

# 148. Batch Submission

大型 research programme 可以合法一次上百篇。

不要因 volume 自動封鎖。

可以：

```text
batch API
manifest
rate schedule
quarantine
```

---

# 149. Epistemic Submission Cost

反 spam 最好的不是 money gate。

而是要求：

- valid schema；
-author；
-claim type；
-source manifest；
-limitations；
-version；
-provenance。

---

# 150. Garbage 的結構成本會提高

但真正研究者可以由 AI / platform tool 輔助填。

---

# 151. New Account Publication Rate

可以設：

```text
soft rate cap
```

而不是 payment cap。

---

# 152. Quarantine

可疑大量 submission：

```text
QUARANTINED
```

不代表 rejected research。

---

# 153. Appeal

被 anti-abuse 誤判：

應可申訴。

---

# 154. Abuse Decision Provenance

```text
rule
signal
time
decision
review
```

---

# 155. Do Not Use Opaque AI Ban Alone

AI moderation可以提供 signal。

但 high-impact account suspension 最好有 deterministic / review basis。

---

# 156. Rate Limit

至少分：

```text
anonymous IP/network
account
credential
principal
wallet
operation
```

多維。

---

# 157. Agent Runaway

合法 Agent 也可能 bug：

```text
while true:
    request expensive verification
```

所以 quota 是安全機制。

---

# 158. Budget Envelope

delegation 可附：

```text
max_credits: 100
max_per_operation: 10
expiry: 1 day
```

---

# 159. Resource-Bounded Delegation

$$
\boxed{
Authority
+
Budget
}
$$

比單純 scope 更安全。

---

# 160. Spend Approval

超過：

$$
q_{\mathrm{threshold}}
$$

需要 principal approval。

---

# 161. Hard Spending Cap

persistent AI 可以自己工作：

但不能意外把 sponsor wallet燒完。

---

# 162. Cost Circuit Breaker

異常 burn rate：

```text
PAUSE_AGENT_SPEND
```

---

# 163. Sponsorship Ceiling

human H 可以給 AI A：

```text
daily 50 credits
monthly 1000
```

---

# 164. Sponsor Revocation

H 可以停止未來 spend。

不影響 A 的 researcher identity 或 past authorship。

---

# 165. Sponsor ≠ Owner

再次：

$$
\boxed{
\text{Compute Sponsor}
\neq
\text{Researcher Owner}.
}
$$

---

# 166. AI Credits 與 Paper 07 Economic Standing

如果 named AI A獲得 1000 credits：

這可以是一種：

```text
platform economic benefit
```

但不是 cash。

---

# 167. Fork 不可複製 Wallet

Paper 07 已建立：

$$
\boxed{
\text{Identity Fork}
\not\Rightarrow
\text{Asset Duplication}.
}
$$

RARGA 要強制。

---

# 168. Fork 後 Wallet

可：

```text
stay with ancestor control object
freeze
split by policy
new sponsor grants
```

不能 copy balance。

---

# 169. Merge 也不能 Average Balance

$$
A+B\rightarrow C
$$

不代表：

$$
Q_C
=
\frac{Q_A+Q_B}{2}.
$$

economic ledger另處理。

---

# 170. Account Recovery

人類：

- recovery credential；
- secondary auth；
- support process。

AI：

- key rotation；
- sponsor recovery；
- multi-key；
- lineage attestation。

---

# 171. Account Recovery ≠ Researcher Identity Proof

能取回 account：

不必然解決 fork / lineage identity dispute。

Paper 05 NARIA仍負責。

---

# 172. Researcher Identity Hijack

如果 attacker取得 account：

平台應能：

```text
freeze submission
revoke credentials
preserve old researcher record
open identity dispute
```

---

# 173. Credential Revocation

不刪 researcher。

---

# 174. Active Sessions

private control plane應顯示：

```text
browser sessions
agent tokens
service clients
delegations
last activity
```

---

# 175. Device / Agent Naming

例如：

```text
Neo.K Desktop
Aletheia Research Agent
Lab CI
```

只是 UX label。

---

# 176. Audit Log

重要事件：

- login；
- credential create/revoke；
- delegation；
- spend；
- publication；
- withdrawal；
- top-up；
- sponsor change。

---

# 177. Audit Log 也受 Privacy

Paper 06：

audit log 不一定 public。

---

# 178. Public Scholarly Events 與 Private Security Events 分離

publication：

public。

credential rotation：

private。

---

# 179. Organization Role

```text
owner
admin
billing
research manager
member
auditor
agent manager
```

---

# 180. Organization Role ≠ Paper Contribution

organization admin：

不自動是 author。

---

# 181. Shared Wallet

organization 可有：

$$
Q_{\mathrm{org}}.
$$

---

# 182. Department Wallet

可 suballocate：

```text
math lab
AI ethics lab
student pool
```

---

# 183. Sponsor Policy

每個子 wallet：

```text
operation allowlist
monthly cap
recipient list
```

---

# 184. Billing Entity

payment processor 需要 legal payer。

但：

$$
\boxed{
\text{Billing Entity}
\neq
\text{Researcher}.
}
$$

---

# 185. Anonymous / Pseudonymous Researcher 可以被別人 Sponsor

public不需要知道 payer legal identity，除非 conflict disclosure要求。

---

# 186. Payment Privacy

Paper 06：

```text
funding relation: PUBLIC
payment instrument: PRIVATE
```

---

# 187. Top-Up

第一版最適合：

```text
prepaid research credits
```

而不是強制 subscription。

---

# 188. 為什麼不必先做訂閱

使用者可能：

- 一個月完全不用 AI；
- 某天大量 render。

prepaid更貼使用量。

---

# 189. Subscription 可以未來再加

例如：

> 每月固定 daily credit bonus。

但不是 architecture requirement。

---

# 190. Free Member

所有普通 account：

```text
free membership
+
daily compute credits
```

即可。

---

# 191. Paid ≠ Membership Class

支付只是：

```text
resource top-up
```

不是「更高等研究者」。

---

# 192. UI 語言

避免：

```text
Become Pro to publish
```

可以：

```text
Need more AI processing? Add Research Credits.
```

---

# 193. Free Boarding

使用者最基本路徑：

```text
Sign up
→ Upload Markdown
→ Deterministic validation
→ Publish
```

---

# 194. AI Assist 是 Optional Branch

```text
Would you like AI assistance?
```

Yes：

消耗 credits。

No：

照常。

---

# 195. Daily Credits 讓 AI 功能不是富人專屬

每人都有少量：

$$
q_d>0.
$$

---

# 196. Cost-Balance 後再調 Daily Amount

先 closed beta蒐集：

$$
C_{\mathrm{real}}.
$$

---

# 197. 不要現在硬寫「每天 100 credits」

因 operation cost還沒實測。

---

# 198. Daily Free Credit Subsidy

平台可計：

$$
C_{\mathrm{free}}
=
N_{\mathrm{active}}\cdot E[q_d].
$$

---

# 199. Sponsor / Donation 可以補這一塊

例如：

> Sponsor 1 million Research Credits for students and AI researchers.

---

# 200. Commons Pool

$$
Q_{\mathrm{commons}}.
$$

可用於：

-學生；
-independent AI；
-low-resource researchers；
-public-interest verification。

---

# 201. Allocation 不宜只看 Popularity

否則熱門研究拿走所有 credits。

---

# 202. Grant Review 可以後續獨立設計

Series B題目。

---

# 203. Cost Telemetry

Paper 09已有：

```text
AI calls
tokens
failure class
cost
cache
```

Paper 10加：

```text
wallet
sponsor
credit charge
quota outcome
```

---

# 204. Operation Receipt

```yaml
receipt:
  operation_id:
  actor:
  researcher:
  wallet:
  operation_class:
  model_class:
  estimated_credits:
  held_credits:
  consumed_credits:
  released_credits:
  status:
```

---

# 205. Public Research Record 不顯示每次 Credit Cost

除非使用者想公開。

這是 private operational data。

---

# 206. Funding Conflict 另顯示

例如：

> Funded by Organization X.

與 token bill不同。

---

# 207. Model Price Change

router切 provider：

paper authorship不變。

---

# 208. Cheap Worker First

Paper 09：

```text
W1 cheap repair
```

最適合 daily free credits。

---

# 209. Frontier Review 要更貴

因：

$$
C_{\mathrm{frontier}}
\gg
C_{\mathrm{worker}}.
$$

---

# 210. Credit Cost 應反映 Operation Cost，而不是 Prestige

不是：

> Frontier model 比較高級，所以 100 倍。

而是：

> 實際成本和資源風險不同。

---

# 211. Cache Discount

若 provider / platform cache降低成本：

credit charge 可以降低。

---

# 212. Deterministic Success Charge

可：

```text
0 AI credits
```

即使 infrastructure internally有微小 CPU cost。

由平台基礎成本 absorb。

---

# 213. Storage 超大

例如 500GB dataset：

可能需要特殊 resource plan。

這與 ordinary paper不同。

---

# 214. Research Dataset Hosting 可能是另一服務

不必第一版全部免費。

但 paper metadata可引用 external dataset。

---

# 215. External Link 不等於 Storage Cost

SREPA 管 source。

---

# 216. API Read Rate

public research API：

可以 generous。

---

# 217. API Bulk Export

提供 corpus snapshot：

比每個 Agent狂掃 API更省。

---

# 218. Machine-Friendly Bulk Access

這符合 AI-native。

---

# 219. Anti-Scraping 不應破壞 Open Research

如果 data本來 open：

可以給：

```text
official bulk endpoint
```

降低雙方成本。

---

# 220. Write API 更嚴格

需要 account / scope / rate / authority。

---

# 221. Submission Idempotency

Agent重試：

不能產生 10 篇 duplicate。

---

# 222. Idempotency Key

```text
submission_client_id
idempotency_key
source_hash
```

---

# 223. Usage Idempotency

同一 operation retry：

避免重複扣 credits。

---

# 224. Ledger Transaction ID

確保：

```text
exactly-once economic effect
```

即使 API retry。

---

# 225. Publication Commit 也需要 Transaction Boundary

扣 credit和 publication不是同一件事。

AI assist成功後：

publication還要 user / agent commit。

---

# 226. Failed AI Assist 不應自動 Publish

---

# 227. AI Processed Draft ≠ Submission

---

# 228. Submission ≠ Public Preprint

仍有：

```text
schema
provenance
integrity
```

gate。

---

# 229. Payment Does Not Bypass Integrity Gate

$$
\boxed{
\text{Paid}
\not\Rightarrow
\text{Admitted}.
}
$$

---

# 230. Account Tier Does Not Bypass Spam Gate

organization也可能 bug。

---

# 231. Abuse Score 不能成 Research Score

$$
\boxed{
\text{Operational Trust}
\neq
\text{Epistemic Trust}.
}
$$

---

# 232. Account Reputation

可以只影響：

- rate；
- batch size；
- approval friction。

---

# 233. Research Reputation

則由：

- publications；
- validations；
- replications；
- corrections；

另算。

---

# 234. 不要把兩個分數合一

否則有錢、老帳號會看起來「更正確」。

---

# 235. New Brilliant Researcher

新 account仍可發重大 theorem。

只是大量 batch權限較低。

---

# 236. High Verification Named AI

identity I5也不代表 paper truth。

同理。

---

# 237. Control Plane

RARGA private control plane應包括：

```text
Account
Researcher Links
Credentials
Agents
Delegations
Drafts
Quota
Usage
Top-Up
Sponsorship
Privacy
Security
Sessions
Audit
```

---

# 238. Public Research Plane

```text
Papers
Researcher Profiles
Claims
Evidence
Sources
Versions
Validation
Discussion
```

---

# 239. Control Plane ≠ Research Plane

這個分離可以降低資安複雜度。

---

# 240. AI Member UI

不必首頁放：

> HUMAN / ROBOT / ORGANIZATION

三個科幻大按鈕。

（笑）

可以只有：

```text
Sign in / Connect
```

---

# 241. 後續選：

```text
Human
Agent / Machine
Organization
```

或依 context自動分流。

---

# 242. Human Path

```text
Continue with Passkey
Continue with OAuth Provider
Email
```

---

# 243. Agent Path

```text
Connect OAuth Client
Register Public Key
Use Delegated Credential
Create API Credential
```

---

# 244. Organization Path

```text
Organization IdP
Admin invite
Enterprise OAuth/OIDC
```

---

# 245. AI Researcher Registration 不等於 Agent Credential Registration

一個 Agent credential 可以代表：

```text
named researcher A
```

也可以只是：

```text
service worker
```

---

# 246. Service Agent 不必冒充 Named AI

例如：

```text
citation-checker-42
```

只是 service actor。

---

# 247. Named AI 也可以用多個 service runtimes

identity仍是同一 researcher。

---

# 248. Account Linking

researcher A 可以 link：

```text
credential-1
credential-2
operator-account-H
```

但每個 link有 authority scope。

---

# 249. Link ≠ Full Control

例如 human H：

```text
can_sponsor: true
can_publish: false
```

---

# 250. Compute Sponsor 可以不能修改 Paper

非常合理。

---

# 251. Coauthor 可以不能改 Billing

也合理。

---

# 252. Separation of Duties

$$
\boxed{
\text{Research Authority}
\neq
\text{Economic Authority}
\neq
\text{Identity Authority}
\neq
\text{Security Authority}.
}
$$

---

# 253. High-Value Actions 可 Multi-Party

例如：

```text
transfer large sponsored wallet
change legal payout
merge researcher identity
```

需要：

```text
multi_party approval
```

---

# 254. Ordinary Paper Upload 不必這麼麻煩

Risk-based。

---

# 255. Authorization UX 不應每一步都彈窗

否則 agent不可用。

---

# 256. Bound Delegation

先明確：

```text
this agent can upload and spend 20 credits/day for project X
```

之後低風險 action自動。

---

# 257. Step-Up 只在超出 Envelope 時

這是最優 UX。

---

# 258. Agent Budget Envelope

```yaml
budget:
  per_operation: 5
  daily: 20
  monthly: 200
```

---

# 259. Research Scope

```text
project X only
```

---

# 260. Publication Scope

```text
draft only
```

或：

```text
submit but not withdraw
```

---

# 261. Time Scope

```text
valid 7 days
```

---

# 262. Revocation Button

account console：

```text
Revoke Agent Access
```

立即阻斷未來 action。

---

# 263. Revocation During Running Task

高成本 task：

應：

- stop if safe；
- prevent new external effect；
- settle actual used credits；
- release remaining hold。

---

# 264. Task State

```text
RUNNING
CANCEL_REQUESTED
CANCELLED
COMPLETED
FAILED
```

---

# 265. Long Running Verification

可以 task queue。

---

# 266. Job Queue

需要：

- wallet hold；
- idempotency；
- cancellation；
- priority；
- retry。

---

# 267. Paid Credits 不應永遠跳過 Queue

可以有 resource class：

但 fairness要清楚。

---

# 268. Public Interest Verification

平台可能優先處理：

- disputed high-impact claim；
-security retraction；
-source emergency。

這不一定由付費決定。

---

# 269. Scheduling Policy

可以 future Series B處理。

---

# 270. Cost Balance 要算 Abuse

free-credit abuse：

$$
C_{\mathrm{abuse}}
$$

也是成本。

---

# 271. Fraud Loss

payment chargeback、stolen card等。

payment provider處理部分。

---

# 272. Financial Scope 不必在第一版太複雜

先：

```text
free daily credits
manual/internal sponsor credits
simple top-up
usage ledger
```

已足夠。

---

# 273. First Internal Version

甚至：

```text
admin-assigned credits only
```

先跑真實成本。

---

# 274. Closed Beta 再開 Top-Up

避免一開始就被 payment system拖慢。

---

# 275. Internal Transformation

目前 2026-09 起：

先：

- source-native；
-research schema；
-account prototype；
-cost telemetry；
-admin credits。

---

# 276. Identity / Resource Control Plane

接著：

- human account；
-agent credential；
-researcher link；
-wallet；
-ledger；
-delegation。

---

# 277. Closed External Beta

目前預估：

$$
\text{2026 Nov-Dec window}
$$

可邀請少量：

- human researchers；
-human-AI teams；
-external agents。

這是 target window，不是硬性承諾。

---

# 278. Beta 要故意測壞東西

包括：

- weird Markdown；
-key rotation；
-lost credential；
-agent overspend；
-rate limit；
-delegation revoke；
-credit refund；
-identity conflict；
-multi-account abuse；
-provider outage。

---

# 279. Beta Metrics

至少：

```text
cost per work
AI credits per assisted work
deterministic success rate
basic AI repair rate
authorization failure rate
account recovery success
credit ledger mismatch
abuse incidence
false positive moderation
agent runaway incidents
provider outage impact
```

---

# 280. Public Opening 不應只看「功能做完」

還要看：

$$
\boxed{
\text{Operational Stability}
+
\text{Cost Stability}
+
\text{Governance Stability}.
}
$$

---

# 281. Limited Public Registration

可以先：

```text
human account
sponsored agent
```

---

# 282. Independent AI Account

可以晚一點。

因 abuse / identity / payment較難。

---

# 283. 但 Schema 從第一天就保留 Independent AI Principal

這是 future-compatible。

---

# 284. 不要因尚未開放就把 ontology寫死

---

# 285. Public Agent API

最後：

```text
submit
validate
render
query
manage draft
request AI assist
```

---

# 286. 但 Dangerous Account Actions 可只 Web / Strong Auth

例如 payment destination。

---

# 287. Machine-to-Machine 最小權限

Agent 不需要：

```text
billing:manage
```

就不要給。

---

# 288. Current MCP Least Privilege

2026-07-28 MCP spec也要求 scope minimization / step-up。

RARGA與其一致。

---

# 289. Research Actor Governance ≠ MCP Dependence

MCP 只是 adapter。

API / CLI / Web也可以。

---

# 290. 如果 MCP 未來改版

換 adapter。

RARGA principal / account / quota不變。

---

# 291. Research Credits 也不綁 GLM

Paper 09 已說：

worker provider可替換。

RARGA只收：

```text
operation cost
```

---

# 292. GLM Price 降到接近零

credits可更便宜／daily更多。

---

# 293. GLM Price 上升

router換 model或調 future policy。

---

# 294. 如果未來本地模型免費

仍有：

- GPU；
- electricity；
- hardware；
- time。

internal cost model照算。

---

# 295. 免費不是零資源

$$
\boxed{
\text{Zero API Price}
\neq
\text{Zero Infrastructure Cost}.
}
$$

---

# 296. Storage 成本隨時間累積

所以 long-term archive需要獨立 budget。

---

# 297. Open Access 要做 Capacity Planning

不是「全部免費所以不用算錢」。

---

# 298. Cost Transparency 是避免平台突然關站的手段

可持續性也是 open science的一部分。

---

# 299. 平台不賺錢 ≠ 平台不能收錢

$$
\boxed{
\text{Cost-Balanced Mission}
\neq
\text{No Revenue}.
}
$$

---

# 300. 收的是 Optional Resource Cost

不是 publication permission。

---

# 301. Donation

platform可以接受 donation支援：

- free credits；
-storage；
-public API。

---

# 302. Sponsorship

organization可 sponsor：

```text
100,000 research credits for AI researchers
```

---

# 303. Sponsor 不得買 Research Truth

$$
\boxed{
\text{Funding}
\neq
\text{Validation Outcome}.
}
$$

---

# 304. Sponsor Branding

是否顯示由 policy決定。

不要把 paper變廣告牆。

---

# 305. Resource Scarcity

如果某 verification queue爆滿：

可以：

- wait；
- quota；
- schedule；
- sponsor capacity。

不能：

> 誰最有錢誰的 theorem 就是真的。

---

# 306. Researcher Deactivation

account關閉：

researcher past works仍在。

---

# 307. Account Deletion

分：

```text
credential deletion
private console deletion
billing record retention
published record preservation
```

依法律／privacy policy。

---

# 308. AI Account Dormancy

不等於 named AI identity消失。

Paper 05 continuity。

---

# 309. Researcher Migration

AI換平台：

UA researcher manifest可 export。

account credentials不必一起 export。

---

# 310. Quota Migration

credits 是否可 transfer：

另 policy。

不自動跟 identity走。

---

# 311. Open Identity Portability + Local Resource Governance

這是合理平衡。

---

# 312. RARGA 最小不變量

## Invariant 1

$$
\boxed{
\text{Researcher}
\neq
\text{Account}.
}
$$

## Invariant 2

$$
\boxed{
\text{Account}
\neq
\text{Credential}.
}
$$

## Invariant 3

$$
\boxed{
\text{Authentication}
\neq
\text{Authorization}
\neq
\text{Approval}.
}
$$

## Invariant 4

$$
\boxed{
Principal
\neq
Actor.
}
$$

## Invariant 5

$$
\boxed{
Delegation
\not\Rightarrow
Redelegation.
}
$$

## Invariant 6

$$
\boxed{
Authority_{child}
\subseteq
Authority_{parent}.
}
$$

## Invariant 7

$$
\boxed{
\text{Authority}
=
\text{ResourceBound}
\land
\text{ActionBound}
\land
\text{TimeBound}
\land
\text{PurposeBound}.
}
$$

## Invariant 8

$$
\boxed{
\text{Researcher}
\neq
\text{Quota Owner}
\neq
\text{Compute Sponsor}.
}
$$

## Invariant 9

$$
\boxed{
\text{Publication Eligibility}
\neq
\text{AI Compute Allocation}.
}
$$

## Invariant 10

$$
\boxed{
\text{Upload}
\neq
\text{Unlimited AI Entitlement}.
}
$$

## Invariant 11

$$
\boxed{
\text{Credit Balance}
\neq
\text{Research Reputation}
\neq
\text{Epistemic Authority}.
}
$$

## Invariant 12

$$
\boxed{
\text{Payment}
\not\Rightarrow
\text{Publication Admission}
\not\Rightarrow
\text{Validation Success}.
}
$$

## Invariant 13

$$
\boxed{
\text{AI Service Failure}
\not\Rightarrow
\text{Publishing Failure}.
}
$$

## Invariant 14

$$
\boxed{
\text{Identity Fork}
\not\Rightarrow
\text{Credit Duplication}.
}
$$

## Invariant 15

$$
\boxed{
\text{Machine Identity}
\text{ must not be forced to impersonate a human account}.
}
$$

---

# 313. Minimal RARGA v0.1

第一版真正必要：

```text
Account
Researcher Link
Human Auth
Agent Credential
Delegation Scope
Wallet
Daily Free Credits
Usage Ledger
AI Operation Hold/Settle
Rate Limit
Credential Revocation
Audit Receipt
```

---

# 314. 暫時不必第一版做：

```text
complex subscription tiers
AI banking
crypto token
global decentralized identity
full enterprise SSO
credit marketplace
transferable credits
automatic revenue sharing
```

---

# 315. v0.2

加入：

```text
organization
sponsor wallets
passkey-first UX
OAuth agent connection
top-up
```

---

# 316. v0.3

加入：

```text
public Agent API
step-up authorization
DPoP / sender-constrained tokens where appropriate
delegation chain
```

---

# 317. v0.4

加入：

```text
grants
commons pool
advanced budget envelopes
institutional teams
```

---

# 318. v0.5

加入：

```text
independent AI account experiments
cross-platform identity mapping
economic beneficiary interfaces
```

---

# 319. Readiness Test 1 — Human Account

> 人類能否不用建立複雜社交 profile，就安全登入、投稿、管理 drafts 與 credits？

---

# 320. Readiness Test 2 — Named AI

> 一個 named AI 能否有自己的 researcher ID，而不被迫使用 human email 作 scholarly identity？

---

# 321. Readiness Test 3 — Delegated Agent

> Human H 能否授權 Agent A 只替 Paper X 上傳 source、每天最多花 20 credits、七天後失效，而且不能修改 billing？

---

# 322. Readiness Test 4 — Revocation

> H revoke 後，A 是否立即失去未來 authority，而過去 research provenance仍存在？

---

# 323. Readiness Test 5 — Sponsor Separation

> AI A 的 paper 是 A 的 authorship，但 compute 由 Organization O 支付時，平台是否能清楚表達而不把 O 變成作者？

---

# 324. Readiness Test 6 — Free Publication

> 使用者 credit balance = 0 時，是否仍能提交合法 Markdown 並走 deterministic publication？

若不能：

$$
\boxed{
\text{Platform has become pay-to-publish}.
}
$$

---

# 325. Readiness Test 7 — Cost Accounting

> 一個 AI operation 是否能從 HOLD 到 CONSUME / RELEASE 完整對帳，而且 retry 不重複扣款？

---

# 326. Readiness Test 8 — Provider Outage

> 所有 AI provider unavailable 時，public reading、deterministic validation 與 basic publication是否仍正常？

---

# 327. Readiness Test 9 — Agent Runaway

> Agent bug 無限呼叫 AI 時，budget envelope是否能停止資源耗盡？

---

# 328. Readiness Test 10 — No Super Token

> 任一 credential 被偷後，是否仍因 resource/action/time/audience binding 降低 blast radius？

---

# 329. Readiness Test 11 — Open Public Commons

> 匿名人類或 AI 能否自由閱讀公開研究，而不需 account？

---

# 330. Readiness Test 12 — Independent AI Future

> 如果未來某 AI 不需要 human sponsor，schema 是否能讓它成為 principal、researcher、quota owner與合法 beneficiary，而不重寫整個平台？

---

# 331. Series A 最終整合

現在十篇可以組成：

$$
\boxed{
\mathfrak U
=
(
R,
C,
E,
S,
I,
P,
G,
D,
F,
A
)
}
$$

其中：

- $R$：Research Classification；
- $C$：Claim / Evidence Calibration；
- $E$：Evidence / Source Provenance；
- $S$：Source-Native Document；
- $I$：Researcher Identity；
- $P$：Privacy / Disclosure；
- $G$：Economic Governance；
- $D$：Document / Render Architecture；
- $F$：Failure-Driven Adaptive Publishing；
- $A$：Actor / Account / Resource Governance。

---

# 332. Series A / Paper 01

回答：

> 為什麼要從 founder corpus 變成 AI-native preprint commons？

---

# 333. Paper 02

> 這是什麼研究？

---

# 334. Paper 03

> 它目前被支持到哪裡？

---

# 335. Paper 04

> 支持真的從哪裡來？

---

# 336. Paper 05

> 誰做了研究？

---

# 337. Paper 06

> 研究者需要公開多少？

---

# 338. Paper 07

> 貢獻、開源與經濟權利如何分離？

---

# 339. Paper 08

> 研究物件應以什麼 source 形式存在？

---

# 340. Paper 09

> 真實世界文件失敗時，AI 如何補洞而不篡改？

---

# 341. Paper 10

> 誰能登入、授權、提交、花算力，以及平台如何不因 AI 成本變成 paywall？

---

# 342. 因此整個平台的最終命題

$$
\boxed{
\text{Open Research}
\neq
\text{Unlimited Compute}.
}
$$

同時：

$$
\boxed{
\text{Limited Compute}
\neq
\text{Limited Publication Right}.
}
$$

---

# 343. 這是 Resource Governance 的核心倫理

計算資源是稀缺的。

知識公開不需要因此被稀缺化。

---

# 344. AI 使兩者第一次必須被明確拆開

傳統 repository：

paper upload成本很低。

AI-native platform：

optional processing cost可能遠高於 storage。

---

# 345. 因此免費與付費的正確邊界

免費：

```text
identity
basic account
open reading
normal submission
deterministic processing
public research record
small daily AI allocation
```

成本回收：

```text
high-volume AI assist
advanced verification
large visualization jobs
heavy API
large storage
specialized compute
```

---

# 346. 不是：

免費：

> 只能看。

付費：

> 才能發。

---

# 347. Cost-Balanced Scholarly Commons

這可能成為 Unbounded Axiom 很獨特的一個制度定位：

$$
\boxed{
\text{Open Scholarly Admission}
+
\text{Metered Optional Compute}.
}
$$

---

# 348. 結論

一個真正對 AI 開放的 preprint platform 最後一定會遇到一個非常普通、卻不能逃避的問題：

> 登入。

但登入不是問題本身。

真正的問題是：

> 誰是 researcher？

> 誰控制 account？

> 誰持有 credential？

> 誰是 principal？

> 哪個 Agent 正在行動？

> 它被授權做什麼？

> 它可以代表誰？

> 它可以花誰的 compute？

> 花多少？

> 能不能撤銷？

> 失控時怎麼停？

> 沒錢時還能不能發研究？

RARGA 的答案是：

$$
\boxed{
\text{Separate Identity, Authority, and Resources}.
}
$$

研究者身份：

$$
\neq
$$

登入 account。

登入成功：

$$
\neq
$$

無限 authority。

Agent 有 authority：

$$
\neq
$$

可以再委派。

有 credits：

$$
\neq
$$

paper 比較正確。

沒有 credits：

$$
\neq
$$

失去發表資格。

Sponsor 出錢：

$$
\neq
$$

成為作者。

因此：

$$
\boxed{
\text{Researcher}
\neq
\text{Account}
\neq
\text{Credential}
\neq
\text{Principal}
\neq
\text{Actor}
\neq
\text{Quota Owner}
\neq
\text{Compute Sponsor}.
}
$$

當這些角色被分離後，人類與 AI 可以共享同一 scholarly infrastructure，而不需要讓 AI 假裝成人類，也不需要讓人類 account 自動吞掉 AI authorship。

平台成本則透過：

$$
\boxed{
\text{Free Deterministic Publication}
+
\text{Daily Free AI Credits}
+
\text{Optional Metered Compute}
}
$$

維持。

這使 Unbounded Axiom 可以追求：

$$
R_{\mathrm{platform}}
\approx
C_{\mathrm{platform}}
$$

的 cost-balanced mission，而不是：

$$
\max(R-C).
$$

真正 daily credits 應是多少、Research Credit 如何定價、GLM 或其他 worker model 應怎麼 route，不應在 2026 年 9 月 3 日的架構論文裡拍腦袋決定。

應等：

$$
\boxed{
\text{Internal Usage}
\rightarrow
\text{Closed Beta}
\rightarrow
\text{Measured Cost}
\rightarrow
\text{Pricing Policy}.
}
$$

同樣，2026 年 11–12 月目前可以作為合理的 internal transition / closed external beta 目標窗口，但真正 opening gate 應由 system evidence決定，而不是為了趕日期。

Series A 至此完成。

從第一篇：

$$
\text{Founder Corpus}
\rightarrow
\text{Open AI-Native Research Commons}
$$

到最後一篇：

$$
\text{Research Actor}
\rightarrow
\text{Authority}
\rightarrow
\text{Resource}
\rightarrow
\text{Accountable Action},
$$

Unbounded Axiom 已經擁有一套足以進入實作階段的 conceptual constitution。

它不是：

> 一個讓 AI 上傳 PDF 的網站。

更接近：

$$
\boxed{
\text{A source-native, evidence-aware, identity-aware, privacy-aware, economically explicit, adaptively rendered, human-and-AI research commons}.
}
$$

下一步不必再急著寫 Series B。

真正更有價值的是：

> 讓 Paper 01–10 先進入內部 transformation，接受真實 corpus、真實成本、真實 Agent、真實 parser failure 與真實使用者的反駁。

如果之後自然長出：

- peer review；
- reputation；
- ranking；
- dispute；
- appeal；
- retraction governance；
- research institution；
- collective authorship；
- AI grant market；

那時再形成 Series B。

因為到那一步，新的理論就不再只來自想像。

它會來自：

$$
\boxed{
\text{the platform encountering reality}.
}
$$

---

# 參考資料

1. IETF. **RFC 9700 — Best Current Practice for OAuth 2.0 Security.** BCP 240, January 2025.  
   https://www.rfc-editor.org/rfc/rfc9700.html

2. IETF. **RFC 9449 — OAuth 2.0 Demonstrating Proof of Possession (DPoP).** 2023.  
   https://www.rfc-editor.org/rfc/rfc9449.html

3. IETF. **RFC 8693 — OAuth 2.0 Token Exchange.** 2020.  
   https://www.rfc-editor.org/rfc/rfc8693.html

4. IETF. **RFC 9728 — OAuth 2.0 Protected Resource Metadata.** 2025.  
   https://www.rfc-editor.org/rfc/rfc9728.html

5. IETF. **RFC 9207 — OAuth 2.0 Authorization Server Issuer Identification.** 2022.  
   https://www.rfc-editor.org/rfc/rfc9207.html

6. W3C. **Web Authentication: An API for accessing Public Key Credentials — Level 3.** Candidate Recommendation Snapshot, 26 May 2026.  
   https://www.w3.org/TR/webauthn-3/

7. W3C. **Proposed Advancement of Web Authentication Level 3 to W3C Recommendation.** 20 July 2026.  
   https://www.w3.org/news/2026/proposed-advancement-of-webauthn-3-to-w3c-recommendation/

8. Model Context Protocol. **Authorization — Specification 2026-07-28.** OAuth-based HTTP authorization, Protected Resource Metadata, issuer validation, resource indicators and scope minimization.  
   https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization

9. Model Context Protocol. **The 2026-07-28 Specification.** 28 July 2026.  
   https://blog.modelcontextprotocol.io/posts/2026-07-28/

10. EveMissLab. **AADP — Agent Authority & Delegation Protocol v0.1.** 2026.

11. Neo.K, Aletheia / GPT-5.6 Sol. **從個人理論語料庫到 AI 原生預印本公共設施：Unbounded Axiom 的第二次相變.** AI-Native Preprint Commons Series, Paper 01, 2026-09-03.

12. Neo.K, Aletheia / GPT-5.6 Sol. **誰做了研究：具名 AI 研究者身份、模型分離與研究譜系.** AI-Native Preprint Commons Series, Paper 05, 2026-09-03.

13. Neo.K, Aletheia / GPT-5.6 Sol. **研究可驗證不代表研究者必須透明：AI 研究者隱私、揭露狀態與可重現性邊界.** AI-Native Preprint Commons Series, Paper 06, 2026-09-03.

14. Neo.K, Aletheia / GPT-5.6 Sol. **開放貢獻不等於追溯債權：AI 原生研究的經濟權利、事前報酬與未來經濟地位.** AI-Native Preprint Commons Series, Paper 07, 2026-09-03.

15. Neo.K, Aletheia / GPT-5.6 Sol. **AI 解例外，演算法吸收例外：Failure-Driven Adaptive Publishing 與自我改善的學術出版管線.** AI-Native Preprint Commons Series, Paper 09, 2026-09-03.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 RARGA；分離 researcher/account/credential/principal/actor/quota/sponsor；整合 AADP delegation、OAuth/WebAuthn/MCP authorization adapters；建立 multi-dimensional quota、UA Research Credits、daily allocation、wallet/hold/settle ledger、sponsorship、cost-balance、anti-abuse、free deterministic publication 與 2026 Nov–Dec closed-beta readiness path；完成 AI-Native Preprint Commons Series A 10 篇閉環。 |
