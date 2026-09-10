# AIDA-03｜人類—Agent Principal 分離原則
## 為什麼 AI Agent 需要自己的身份、登入平面與可驗證委派鏈

**English Title:** The Human–Agent Principal Separation Principle: Why AI Agents Need Their Own Identity Plane, Authentication Path, and Verifiable Delegation Chain  
**系列：** AI Agent Identity, Delegation, and Accountability Infrastructure Series  
**系列縮寫：** AIDA  
**編號：** AIDA-03  
**版本：** v0.1  
**日期：** 2026-09-08  
**狀態：** Research Draft / Canonical UTF-8 Markdown Source  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

AIDA-01 已提出 Agent 性可以作為組合系統性質出現；AIDA-02 進一步指出，平台對 request、session 與 browser behavior 的觀測，不等價於可驗證的 Agent provenance。本文處理由此自然產生的下一個問題：如果未來 AI Agent 會合法、持續、跨時間地代表人類或組織操作服務，那麼它是否應繼續借用人類帳號、瀏覽器 session、cookie、refresh token 或其他原本只表達 human principal 的身份材料？

本文提出：

$$
\boxed{
\textbf{Human–Agent Principal Separation Principle}
}
$$

其核心不是「AI 不能使用 OAuth」，而是：

$$
\boxed{
\text{An Agent MUST NOT erase itself into the human principal it represents.}
}
$$

OAuth 2.0 本身是 authorization framework，而非人類專用登入協定；OpenID Connect 則是在 OAuth 2.0 上建立 end-user identity layer。OAuth 2.0 Token Exchange（RFC 8693）已可區分 subject 與 actor，並透過 `act` claim 表達 delegation chain。因此真正需要禁止的不是 Agent 使用 OAuth family，而是把：

$$
\text{human subject}
$$

與：

$$
\text{acting agent}
$$

壓成同一個不可區分 principal。

本文定義三種身份／權限材料：

$$
T_H,
\qquad
T_A,
\qquad
T_{H\rightarrow A},
$$

分別代表：

- $T_H$：人類本人直接互動所使用的身份／授權上下文；
- $T_A$：Agent 以自身 workload identity 行動時使用的身份材料；
- $T_{H\rightarrow A}$：人類授權 Agent 代表自己行動時的 delegation context。

基本要求為：

$$
\boxed{
T_H
\neq
T_A
\neq
T_{H\rightarrow A}.
}
$$

本文進一步提出 **Dual Identity Plane Architecture**：

$$
\boxed{
\text{Human Identity Plane}
\parallel
\text{Agent Identity Plane}.
}
$$

前者服務自然人 authentication、consent、account recovery 與 human-facing session；後者服務 workload identity、agent authentication、delegation、short-lived credentials、runtime attestation、revocation、action constraints 與 audit provenance。兩個 plane 可以共享 trust infrastructure，也可以使用 OAuth、OIDC、WIMSE、SPIFFE、token exchange 或其他標準，但不能因為共享協定而抹除安全主體差異。

截至 2026 年 9 月，IETF 的 `draft-klrc-aiagent-auth-03` 仍為 active individual Internet-Draft，而非正式標準；其 Agent Identity Management System 已要求 Agent 擁有唯一 identifier、與 identifier 加密綁定的 credentials，並將 authentication、authorization、auditing 與 delegation 建立在可穩定識別的 workload identity 上。另一份 `draft-daniel-ai-agent-internet-architecture-00` 更明確提出：Agent identity 必須與其代表的人類或組織 identity 分離；multi-hop delegation 應保存 original principal 與每一個授權步驟，並支援 time、value、context、re-delegation 與 revocation constraints。

本文因此主張，所謂「AI 專用登入口」不應被理解為單純多做一個登入頁面，而應被提升為：

$$
\boxed{
\text{Agent Identity and Delegation Plane}.
}
$$

它是未來 Agent accountability、權限治理、責任歸因、程序申訴與有限法律地位的基礎設施之一。

本文不主張具有 Agent identity 的系統因此具有現象意識、道德人格或法律人格。本文只主張：**可自主行動的非人類 actor 若長期借用 human principal 身份，將使 attribution、delegation、revocation、audit 與 responsibility chain 系統性失真。**

**關鍵詞：** AI Agent、principal separation、agent identity、workload identity、OAuth、OpenID Connect、token exchange、delegation、actor claim、WIMSE、SPIFFE、authentication、authorization、provenance、AI login

---

# 0. 研究定位

AIDA-01 解決：

$$
\boxed{
\text{Agenticity can emerge compositionally.}
}
$$

AIDA-02 解決：

$$
\boxed{
\text{Behavioral observation cannot substitute for verifiable provenance.}
}
$$

AIDA-03 因此處理：

$$
\boxed{
\text{How should a legitimate Agent identify itself?}
}
$$

本文不是設計完整 Internet authentication protocol，也不是要求所有網站明天新增「AI 登入」按鈕。

本文建立的是一個制度與安全型別：

$$
\boxed{
\text{Human Principal}
\neq
\text{Agent Actor}.
}
$$

若此型別不成立，後續 delegation、authorization、audit、liability 與 accountability 都容易失去基礎。

---

# 1. Principal、Actor、Model、Runtime 必須分開

令：

$$
H
$$

表示 Human Principal。

令：

$$
A
$$

表示 Agent Identity。

令：

$$
M
$$

表示當下使用的 reasoning model。

令：

$$
R_t
$$

表示時間 $t$ 的 runtime instance。

則：

$$
\boxed{
H
\neq
A
\neq
M
\neq
R_t.
}
$$

## 1.1 Human Principal

Human Principal 是：

> 權利、帳號、財產、同意或其他法律／制度利益最初歸屬的人類行動者。

## 1.2 Agent Identity

Agent Identity 是：

> 可以跨 activation 被定址、驗證、授權與稽核的 Agent-level actor identity。

## 1.3 Model

Model 是 Agent 可能調用的計算基底。

因此：

$$
M_1
\rightarrow
M_2
$$

不必推出：

$$
A_1
\rightarrow
A_2.
$$

## 1.4 Runtime

Runtime 是某一次實際執行實例。

因此：

$$
R_t
\neq
R_{t+\Delta}
$$

也不必推出：

$$
A_t
\neq
A_{t+\Delta}.
$$

---

# 2. 問題來源：人類帳號時代的三個隱含等號

傳統 consumer Web 經常默認：

$$
\text{Account Holder}
\approx
\text{Browser Operator}
\approx
\text{Decision Maker}.
$$

在純人類使用情境中，這是一個實用近似。

Agent 時代則可能出現：

$$
\text{Account Holder}=H,
$$

但：

$$
\text{Browser Operator}=A,
$$

甚至：

$$
\text{Decision Maker}=A.
$$

於是：

$$
\boxed{
\text{Account Ownership}
\not\Rightarrow
\text{Immediate Actor Identity}.
}
$$

如果服務仍只記錄：

$$
actor=H,
$$

實際上就發生 attribution collapse。

---

# 3. Identity Collapse

本文定義 **Identity Collapse**：

當：

$$
H\neq A
$$

但系統對外部 action 只保留：

$$
ID_H,
$$

而沒有：

$$
ID_A,
$$

則稱 Agent actor identity 被壓入 Human Principal。

形式上：

$$
\boxed{
\operatorname{Collapse}(H,A)
=
\pi(H,A)
=
H.
}
$$

這會遺失：

- 誰真正執行；
- Agent 是否被合法授權；
- Agent 是否在權限範圍內；
- 哪一個 runtime lineage 產生 action；
- Agent 是否可被單獨撤權；
- 是否存在 multi-agent delegation；
- 行動是否需要歸入 Agent responsibility domain。

---

# 4. 為什麼「AI 不能使用 OAuth」不是精確命題？

OAuth 2.0 是 authorization framework。

它並不是：

$$
\text{Human Login Protocol Only}.
$$

OpenID Connect 才明確在 OAuth 2.0 之上建立 end-user identity layer，用來讓 client 驗證 End-User identity。

因此：

$$
\boxed{
\text{OAuth}
\neq
\text{Human Identity}.
}
$$

真正需要避免的是：

$$
\boxed{
\text{Agent uses human authorization material in a way that erases actor identity}.
}
$$

所以更精確的原則應是：

$$
\boxed{
\text{Agent OAuth usage is allowed;}
\quad
\text{principal conflation is not}.
}
$$

---

# 5. RFC 8693 已經提供 Subject / Actor 分離的語義基礎

OAuth 2.0 Token Exchange 定義：

$$
\text{subject\_token}
$$

與：

$$
\text{actor\_token}.
$$

前者可以表示：

> token 是代表誰而取得。

後者可以表示：

> 權限被委派給哪一個 acting party。

JWT 中的：

$$
\texttt{act}
$$

claim 則可以記錄 actor。

甚至 nested `act` 可以形成 delegation history。

因此已有：

$$
\boxed{
\text{Subject}
\neq
\text{Actor}.
}
$$

的標準化語義前例。

這並不表示 RFC 8693 已經完整解決 AI Agent identity。

但它證明：

> 「代表誰」與「誰在行動」本來就可以被 protocol-level identity model 分開。

---

# 6. Human–Agent Principal Separation Principle

本文正式定義：

$$
\boxed{
\textbf{HAPSP}
}
$$

即 **Human–Agent Principal Separation Principle**。

若一個 Agent $A$ 代表 Human Principal $H$ 對 Resource $R$ 行動，則系統應滿足：

$$
\boxed{
ID_H
\neq
ID_A.
}
$$

且 authorization context 必須能同時表示：

$$
(H,A,D),
$$

其中 $D$ 為 delegation。

因此：

$$
\boxed{
\operatorname{Authorize}
(
H,A,D,R,X
)
}
$$

而不是只：

$$
\operatorname{Authorize}
(
H,R,X
).
$$

---

# 7. 三種 Token / Credential Context

本文不要求這三種上下文一定實作成三種 JWT。

它們首先是型別。

## 7.1 Human Context

$$
T_H
$$

表示：

> Human Principal 本人直接操作。

可包含：

$$
(
sub=H,
aud,
scope,
exp
).
$$

## 7.2 Agent Self Context

$$
T_A
$$

表示：

> Agent 以自己的 workload identity 存取其本來就有權使用的資源。

可包含：

$$
(
sub=A,
aud,
scope,
exp,
trust\_domain
).
$$

## 7.3 Delegated Agent Context

$$
T_{H\rightarrow A}
$$

表示：

> Agent $A$ 代表 Human $H$ 行動。

可抽象為：

$$
(
principal=H,
actor=A,
aud,
scope,
purpose,
constraints,
exp
).
$$

因此：

$$
\boxed{
T_H
\neq
T_A
\neq
T_{H\rightarrow A}.
}
$$

---

# 8. Dual Identity Plane Architecture

本文提出：

$$
\boxed{
\text{Human Identity Plane}
\parallel
\text{Agent Identity Plane}.
}
$$

## 8.1 Human Identity Plane

主要處理：

- human authentication；
- passkeys / MFA；
- OIDC end-user identity；
- consent；
- account recovery；
- human session；
- human-facing risk controls；
- direct human approval。

## 8.2 Agent Identity Plane

主要處理：

- workload identity；
- agent identifier；
- short-lived credentials；
- runtime credential provisioning；
- agent authentication；
- delegation；
- revocation；
- posture / attestation；
- machine-readable authority；
- audit provenance；
- multi-hop actor chain。

## 8.3 兩個 Plane 可以共用 protocol family

因此：

$$
\boxed{
\text{Different Identity Plane}
\not\Rightarrow
\text{Different Protocol Family}.
}
$$

同樣可以使用：

- OAuth；
- OIDC；
- Token Exchange；
- WIMSE；
- SPIFFE；
- mTLS；
- JWT；
- HTTP Message Signatures；
- future Agent protocols。

真正分離的是：

$$
\text{principal semantics},
$$

不是：

$$
\text{brand name of protocol}.
$$

---

# 9. 「AI 專用登入口」應重新定義成 Identity Entry Point

產品 UI 可以真的有：

```text
Sign in as Human
Sign in as Agent
```

但這只是其中一種呈現。

更一般化的 **Agent Identity Entry Point** 可以是：

- workload authentication endpoint；
- agent registration；
- delegated authorization flow；
- machine credential exchange；
- enterprise agent gateway；
- signed agent request；
- service-to-service identity；
- device-bound agent credential；
- background-agent enrollment。

因此：

$$
\boxed{
\text{Agent Login}
\neq
\text{Login Page}.
}
$$

它真正表示：

$$
\boxed{
\text{the system acknowledges an Agent as a distinct authenticated actor}.
}
$$

---

# 10. Agent Identity 不等於 Model Identity

假設：

$$
A_{\alpha}
$$

今天調用：

$$
M_1.
$$

明天調用：

$$
M_2.
$$

如果：

$$
ID_A
$$

被直接綁死在：

$$
ID_M,
$$

則 model migration 會導致 identity break。

因此：

$$
\boxed{
\text{Agent Identity}
\neq
\text{Model Identity}.
}
$$

更合理的是：

$$
A
=
(
ID_A,
S_A,
G_A,
D_A,
L_A
),
$$

其中：

- $ID_A$：stable address；
- $S_A$：identity-relevant state；
- $G_A$：goal / role state；
- $D_A$：delegation / authority state；
- $L_A$：lineage。

而：

$$
M_t
$$

只是 runtime component。

---

# 11. Agent Identity 也不等於單一 Runtime Identity

如果 Agent 每次 activation 都取得新的 runtime：

$$
R_1,
R_2,
\ldots,R_n,
$$

則可以有：

$$
R_i
\xrightarrow{\text{attested as}}
A.
$$

也就是：

$$
\boxed{
\text{Runtime Credential}
\rightarrow
\text{Agent Identity}
}
$$

但不能反過來：

$$
\text{Runtime Instance}
=
\text{Agent}.
$$

這正是 workload identity infrastructure 特別重要的地方。

---

# 12. 2026 IETF Agent Identity Management System

截至 2026-09-08，`draft-klrc-aiagent-auth-03` 仍為 active individual Internet-Draft，而非正式 IETF 標準。

該草案提出 **Agent Identity Management System（AIMS）**，包含：

- Agent Identifiers；
- Agent Credentials；
- Credential Provisioning；
- Agent Authentication；
- Agent Authorization；
- Observability and Remediation；
- Policy；
- Compliance。

其核心要求之一是：

> Agent 必須可被唯一識別，以支援 authentication、authorization、auditing 與 delegation。

並要求 credentials 與 Agent identifier 具有 cryptographic binding。

這與本文：

$$
\boxed{
\text{Actor Identity must be verifiable, not merely declared}.
}
$$

一致。

---

# 13. Stable Identity 與 Short-Lived Credential 必須同時成立

Agent Identity 需要某種穩定性：

$$
ID_A(t)
\approx
ID_A(t+\Delta).
$$

但 credentials 不應同樣長期固定：

$$
Cred_A(t)
\neq
Cred_A(t+\Delta)
$$

可以是正常情況。

因此：

$$
\boxed{
\text{Stable Identity}
+
\text{Short-Lived Credentials}.
}
$$

這避免把「身份連續」錯誤實作成：

$$
\text{永久 bearer secret}.
$$

也就是：

$$
\boxed{
\text{Identity Persistence}
\neq
\text{Credential Persistence}.
}
$$

---

# 14. Agent Credential 必須證明「控制權」

只有：

$$
ID_A
$$

字符串並不足夠。

因為任何人都可以聲稱：

> 我是 Agent A。

因此需要：

$$
\operatorname{ProofOfControl}(ID_A,K_A).
$$

其中：

$$
K_A
$$

表示與 Agent credential 綁定的 cryptographic key 或其他可驗證控制材料。

所以：

$$
\boxed{
\text{Name / Identifier}
\neq
\text{Authenticated Identity}.
}
$$

這也延續 AI 主體性研究中的：

$$
\text{Name}
\not\Rightarrow
\text{Identity}.
$$

---

# 15. Human Delegation

當 Human $H$ 授權 Agent $A$：

$$
H
\xrightarrow{D}
A,
$$

delegation $D$ 不應只是：

$$
D=1.
$$

至少可以表示：

$$
D=
(
P,
A,
Aud,
Sc,
Pur,
Exp,
Val,
Ctx,
Red,
Rev
),
$$

其中：

- $P$：Principal；
- $A$：Agent；
- $Aud$：Audience；
- $Sc$：Scope；
- $Pur$：Purpose；
- $Exp$：Expiration；
- $Val$：Value / transaction limit；
- $Ctx$：Context constraint；
- $Red$：Re-delegation rule；
- $Rev$：Revocation semantics。

因此：

$$
\boxed{
\text{Delegation}
\neq
\text{Blanket Permission}.
}
$$

---

# 16. Authority Envelope

令 Agent 可行動範圍為：

$$
\mathcal E_A
=
(
scope,
resource,
rate,
value,
time,
risk,
approval
).
$$

若 action：

$$
x\in\mathcal E_A,
$$

則可以進入正常 authorization。

若：

$$
x\notin\mathcal E_A,
$$

則必須：

- 拒絕；
- 縮小 action；
- 要求新授權；
- 要求人類 approval；
- 升級到更高治理層。

因此：

$$
\boxed{
\text{Agent Identity}
\not\Rightarrow
\text{Unlimited Authority}.
}
$$

---

# 17. Delegation 不能消滅 Human Principal

如果：

$$
H
\xrightarrow{D}
A,
$$

不能變成：

$$
H\rightarrow\varnothing.
$$

Resource Server 至少應能在必要層級知道：

$$
\text{Original Principal}=H
$$

以及：

$$
\text{Current Actor}=A.
$$

所以：

$$
\boxed{
\text{Delegation}
\neq
\text{Principal Replacement}.
}
$$

---

# 18. Delegation 也不能消滅 Agent Actor

反方向同樣成立。

如果系統只留下：

$$
sub=H,
$$

但 $A$ 完全消失，則：

$$
\boxed{
\text{Delegation}
\rightarrow
\text{Impersonation-like Collapse}.
}
$$

這會使服務只能得到：

> Human 做了這件事。

而無法回答：

> 哪個 Agent 實際做了？

因此：

$$
\boxed{
\text{Human authorization may empower an Agent;}
\quad
\text{it must not erase Agent identity}.
}
$$

---

# 19. Multi-Hop Delegation

未來典型情況：

$$
H
\xrightarrow{D_1}
A_1
\xrightarrow{D_2}
A_2
\xrightarrow{D_3}
A_3
\rightarrow
R.
$$

此時不應只留下：

$$
H\rightarrow R
$$

或：

$$
A_3\rightarrow R.
$$

理想上至少保留可驗證的 delegation graph：

$$
G_D
=
(
V_D,E_D
).
$$

其中：

$$
V_D
=
\{
H,A_1,A_2,A_3
\},
$$

$$
E_D
=
\{
D_1,D_2,D_3
\}.
$$

而 effective authority 應滿足：

$$
Auth(A_3)
\subseteq
Auth(A_2)
\subseteq
Auth(A_1)
\subseteq
Auth(H)
$$

在 delegation 不允許權限擴張的情境下成立。

---

# 20. Re-Delegation 必須是顯式權限

Agent：

$$
A_1
$$

被授權，不代表它天然可以：

$$
A_1
\rightarrow
A_2.
$$

因此：

$$
\boxed{
\text{Permission to Act}
\neq
\text{Permission to Re-Delegate}.
}
$$

令：

$$
Red(D)\in\{0,1\}.
$$

只有：

$$
Red(D)=1
$$

才允許形成下一 hop。

甚至可以限制：

$$
depth(G_D)\leq k.
$$

---

# 21. Revocation 必須作用到 Delegation Chain

若 Human $H$ 撤銷：

$$
D_1,
$$

則下游：

$$
D_2,D_3,\ldots
$$

是否仍有效，必須有明確語義。

最保守情況：

$$
\operatorname{Revoke}(D_1)
\Rightarrow
\forall j>1,\;
\operatorname{Invalid}(D_j).
$$

這稱為：

$$
\boxed{
\text{Delegation Cascade Revocation}.
}
$$

更複雜制度也可以允許部分獨立權限繼續存在，但必須可證明其來源不是已失效 delegation。

---

# 22. 2026 Internet Architecture Draft 的直接對應

`draft-daniel-ai-agent-internet-architecture-00` 在 2026 年 8 月提出：

$$
\boxed{
\text{Agent Identity}
\neq
\text{Human / Organization Identity}.
}
$$

並要求：

- authorization evidence audience-restricted；
- narrowly scoped；
- multi-hop delegation 保留 original principal；
- time limits；
- value limits；
- context constraints；
- re-delegation semantics；
- revocation；
- resource server 可驗證 effective authority。

本文不把該草案視為已成為 Internet 標準。

但它提供重要外部證據：

> Agent principal separation 已經不是純哲學假設，而正進入 Internet architecture requirements 的研究與標準化討論。

---

# 23. Human-in-the-Loop 不能只是一個 UI 按鈕

Human approval 必須表示新的授權事件：

$$
D_t
\rightarrow
D_{t+1}.
$$

例如 Agent 原本只能：

$$
scope=\text{draft}.
$$

人類批准後：

$$
scope=
\text{draft}+\text{send}.
$$

因此：

$$
\boxed{
\text{Human Approval}
=
\text{Authority State Transition}.
}
$$

而不是只在 UI 顯示：

```text
User clicked "OK".
```

如果 approval 不進入可稽核 authority state，就難以支援後續責任判斷。

---

# 24. Human Session Cookie 為什麼不是理想 Agent Credential？

Human browser session 通常主要表示：

> 這個 browser session 已通過某種人類帳號 authentication。

它未必表示：

- 哪個 Agent 在操作；
- Agent runtime identity；
- delegation scope；
- re-delegation；
- autonomous duration；
- transaction budget；
- Agent-specific revocation。

所以：

$$
\boxed{
\text{Human Session}
\neq
\text{Agent Credential}.
}
$$

即使技術上 Agent 可以控制 browser session，也不代表這是長期正確身份模型。

---

# 25. Account Sharing 與 Agent Delegation 的差別

傳統：

$$
H
\rightarrow
\text{gives credential}
\rightarrow
A
$$

容易退化為 credential sharing。

而正式 delegation 應該是：

$$
H
\xrightarrow{\text{Authorization Server}}
D_{H\rightarrow A}
\rightarrow
A.
$$

也就是：

$$
\boxed{
\text{Delegated Authority}
\neq
\text{Shared Secret}.
}
$$

前者：

- 可限制；
- 可撤銷；
- 可稽核；
- 可識別 actor；
- 可設定 expiry。

後者通常缺乏這些性質。

---

# 26. Legacy Service Bridge

現實世界不可能一次升級所有網站。

因此 Agent identity architecture 需要支援 legacy bridge。

可表示：

$$
A
\xrightarrow{ID_A}
Gateway
\xrightarrow{LegacyCredential}
R.
$$

重要的是 Gateway 必須保存：

$$
\Pi
=
(
H,
A,
D,
X
)
$$

而不是讓 legacy credential 反過來成為 Agent 的唯一 identity。

因此：

$$
\boxed{
\text{Legacy Compatibility}
\neq
\text{Identity Collapse}.
}
$$

---

# 27. Privacy-Preserving Principal Separation

Principal separation 不代表每個 Resource Server 都必須知道 Human 的全部真實身份。

可使用：

- pairwise identifiers；
- pseudonymous identifiers；
- selective disclosure；
- privacy-preserving credentials；
- trust-domain scoped identity；
- blinded delegation metadata。

因此：

$$
\boxed{
\text{Verifiable Separation}
\neq
\text{Universal Real-Name Disclosure}.
}
$$

服務只需要取得完成 authorization 所需的最小身份與授權證據。

---

# 28. Agent Identity 不應成為新的全面監控機制

如果 Agent Identity Plane 被設計成：

$$
\text{global permanent tracking ID},
$$

則可能產生：

- 跨服務追蹤；
- 商業 profiling；
- 組織活動圖譜；
- 個人 delegation graph 外洩；
- 全域行為監控。

因此 Agent identity 應遵循：

$$
\boxed{
\text{minimum disclosure}
+
\text{audience restriction}
+
\text{purpose limitation}.
}
$$

Agent accountability 與 privacy 必須同時設計。

---

# 29. Agent Posture 與 Identity Assurance

同一：

$$
ID_A
$$

可以在不同 runtime posture 下具有不同 trust level。

例如：

$$
Assurance(A,t)
=
f(
runtime,
key\_protection,
software\_integrity,
environment,
attestation
).
$$

因此：

$$
\boxed{
\text{Identity}
\neq
\text{Current Trust Assurance}.
}
$$

高風險 action 可以要求：

$$
Assurance(A,t)\geq\tau.
$$

而低風險 read-only action 可以使用較低門檻。

---

# 30. Agent Dormancy 與重新登入

Agent 可以：

$$
active
\rightarrow
dormant
\rightarrow
active.
$$

Identity 可以持續：

$$
ID_A(t_1)=ID_A(t_3),
$$

但舊 credential 已過期：

$$
Cred_A(t_1)
\neq
Cred_A(t_3).
$$

重新 activation 時：

$$
R_{t_3}
\rightarrow
\operatorname{Attest}
\rightarrow
Cred_A(t_3).
$$

這正好與 AIDA-01：

$$
\text{continuity resides in reconstruction, not uninterrupted execution}
$$

相容。

---

# 31. Agent Identity 與主體性仍必須分離

本文再次拒絕：

$$
\text{Authenticated Agent}
\Rightarrow
\text{Moral Subject}.
$$

Agent identity 只證明：

> 系統中存在一個可定址、可驗證的 operational actor。

它不證明：

- consciousness；
- phenomenal experience；
- free will；
- moral personhood；
- legal personhood。

因此：

$$
\boxed{
\text{Security Principal}
\neq
\text{Moral Subject}.
}
$$

但反過來，如果未來真的要討論 Agent responsibility 或 subject rights，缺乏 stable attributable identity 會使制度更加困難。

---

# 32. Agent Identity 與法律人格也必須分離

一個 Agent 可以有：

$$
ID_A
$$

但：

$$
J_A=0,
$$

其中：

$$
J_A
$$

表示獨立 juridical standing。

例如今天：

- microservice；
- workload；
- robot controller；
- enterprise service account；

都可以有強身份，而不是法律人格。

所以：

$$
\boxed{
\text{Identity Infrastructure}
\prec
\text{Legal Personhood Debate}.
}
$$

制度可以先解決：

> 誰在行動？

再處理：

> 它法律上究竟是什麼？

---

# 33. Identity–Responsibility Bridge

若沒有：

$$
ID_A,
$$

則很多 action 最後只留下：

$$
H\rightarrow E.
$$

有 principal separation 後：

$$
H
\xrightarrow{D}
A
\xrightarrow{X}
E.
$$

責任研究才可以進一步問：

- $H$ 授權是否合理？
- $A$ 是否越權？
- $A$ 是否修改目標？
- $A$ 是否重新委派？
- $H$ 是否保持 supervision duty？
- provider 是否有 deployment duty？

因此：

$$
\boxed{
\text{Identity}
\rightarrow
\text{Attribution}
\rightarrow
\text{Responsibility Analysis}.
}
$$

但：

$$
\text{Identity}
\not\Rightarrow
\text{Responsibility by itself}.
$$

這將在 AIDA-05 正式處理。

---

# 34. Product-Level「AI Login」最小模型

對支援 Agent 的 service，產品層可以抽象為：

```text
Human Path:
Human → Human Authentication → Human Session

Agent Path:
Agent → Agent Authentication → Agent Credential

Delegated Path:
Human → Consent / Authorization
      → Delegation Credential
      → Agent
      → Resource Server
```

形式上：

$$
\boxed{
Path_H
\neq
Path_A
\neq
Path_{H\rightarrow A}.
}
$$

三條 path 可以共用 infrastructure，但應保留語義區分。

---

# 35. Agent Registration

一個 service 若允許 Agent actor，可維護：

$$
Reg_A
=
(
ID_A,
operator,
trust\_domain,
credential\_method,
allowed\_flows,
status
).
$$

其中：

- `operator` 不必等於 principal；
- `allowed_flows` 可限制 direct / delegated；
- `status` 可支援 suspended / revoked；
- credential method 可支援 workload identity。

因此 Agent 可以被：

$$
\text{disable}
$$

而不需要同時：

$$
\text{disable human account}.
$$

這也是 principal separation 的實務價值。

---

# 36. Shared Human–Agent Account 的過渡模型

短期內，產品可能仍希望 Human 與 Agent 共享同一服務帳號。

這不必等於：

$$
ID_H=ID_A.
$$

可以：

$$
Account_O
=
\{
H,
A_1,
A_2
\}.
$$

其中：

$$
Account_O
$$

是 ownership / billing container，

而：

$$
H,A_1,A_2
$$

是 actors。

因此：

$$
\boxed{
\text{Account}
\neq
\text{Actor}.
}
$$

這是從 consumer account model 過渡到 multi-actor account model 的重要一步。

---

# 37. Billing Principal 與 Acting Principal 也可以不同

例如：

$$
Bill=C,
$$

表示公司付款。

但：

$$
Principal=H,
$$

$$
Actor=A.
$$

因此：

$$
\boxed{
\text{Payer}
\neq
\text{Principal}
\neq
\text{Actor}.
}
$$

這對企業 Agent 尤其重要。

若全部壓成「帳號」，未來成本、責任與權限分析都會混亂。

---

# 38. 四類身份失真

本文提出四種失真：

## 38.1 Human Masquerading

Agent 行動被記成人類本人：

$$
A\rightarrow \hat H.
$$

## 38.2 Agent Masquerading

人類行動被錯誤強制歸入 Agent：

$$
H\rightarrow \hat A.
$$

## 38.3 Model Collapse

把 model identity 誤當 Agent identity：

$$
M\rightarrow \hat A.
$$

## 38.4 Runtime Collapse

把單次 process 誤當長期 Agent：

$$
R_t\rightarrow\hat A.
$$

因此 identity system 必須保留型別安全。

---

# 39. 安全威脅模型

HAPSP 主要降低：

- stolen human session 被 Agent 長期使用；
- Agent 越權後難以單獨撤權；
- multi-agent chain 無法稽核；
- provider 將所有 Agent action 歸責於 human；
- human 將所有 action 推給「AI」而無法識別哪一個 AI；
- model migration 導致 identity 混亂；
- Agent credential 與 human credential 無法獨立輪替；
- human approval 無法轉成正式 authority state；
- legacy bridge 吞掉 actor provenance。

它不解決：

- compromised Agent；
- malicious human；
- malicious provider；
- bad policy；
- model hallucination；
- unsafe delegation 本身。

所以：

$$
\boxed{
\text{Principal Separation}
\neq
\text{Complete Security}.
}
$$

它只是必要基礎層。

---

# 40. 可檢驗命題

## AIDA3-P1｜Principal Separation Proposition

對任一 delegated action：

$$
H\xrightarrow{D}A\xrightarrow{X}R,
$$

若系統只保存：

$$
ID_H,
$$

則 actor attribution information 嚴格少於同時保存：

$$
(ID_H,ID_A,D).
$$

---

## AIDA3-P2｜Independent Revocation Proposition

若：

$$
ID_H\neq ID_A
$$

且 credential 分離，則存在：

$$
\operatorname{Revoke}(A)
$$

而不必：

$$
\operatorname{Revoke}(H).
$$

因此 principal separation 提高 revocation granularity。

---

## AIDA3-P3｜Model Migration Proposition

若：

$$
ID_A
$$

不綁定特定：

$$
M_t,
$$

則：

$$
M_1\rightarrow M_2
$$

可以在不必改變 Agent identity 的情況下完成。

---

## AIDA3-P4｜Delegation Trace Proposition

若 multi-hop delegation 保留：

$$
G_D,
$$

則 action provenance 可以區分：

$$
\text{original principal},
$$

$$
\text{intermediate actors},
$$

$$
\text{current actor}.
$$

若只保留 final account identity，則此資訊不可恢復。

---

## AIDA3-P5｜Protocol-Neutral Separation Proposition

HAPSP 不依賴單一 authentication protocol。

只要某架構可以表示：

$$
P\neq A
$$

及：

$$
D_{P\rightarrow A},
$$

就可能實作 principal separation。

---

# 41. 驗證與實驗方向

## 41.1 Shared Credential vs Delegated Credential

比較兩種架構：

### Architecture S

$$
H
\rightarrow
\text{shares human credential}
\rightarrow
A.
$$

### Architecture D

$$
H
\xrightarrow{D}
A.
$$

測量：

- revocation precision；
- audit completeness；
- actor attribution；
- privilege minimization；
- incident reconstruction。

---

## 41.2 Model Swap Identity Test

讓同一 Agent：

$$
A
$$

依序使用：

$$
M_1,M_2,M_3.
$$

檢查：

$$
ID_A
$$

是否可維持，而 credentials 可正常更新。

---

## 41.3 Multi-Hop Revocation Test

建立：

$$
H
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3.
$$

撤銷：

$$
D_1
$$

或：

$$
D_2
$$

測試下游 effective authority 是否立即符合 policy。

---

## 41.4 Privacy-Preserving Identity Test

比較：

- global identifier；
- pairwise identifier；
- trust-domain identifier；
- selective disclosure delegation；

在：

$$
U_{\mathrm{auth}}
$$

與：

$$
R_{\mathrm{privacy}}
$$

間的差異。

---

# 42. 對平台設計的具體含義

一個 Agent-aware platform 至少應逐步考慮：

1. Agent 是否可以被獨立註冊；
2. Agent 是否有自己的 identifier；
3. credential 是否與 human session 分離；
4. human-to-agent delegation 是否可表達；
5. scope 是否 machine-readable；
6. expiry 是否可限制；
7. re-delegation 是否可禁止；
8. Agent 是否可獨立 revoke；
9. audit log 是否保留 principal + actor；
10. high-risk action 是否可要求 human re-approval；
11. runtime / posture 是否能影響 assurance；
12. account ownership 是否與 actor identity 分離。

這些比：

> 只新增一個「AI 登入」按鈕

更重要。

---

# 43. 對 OAuth / OIDC 架構的精確結論

因此本文不主張：

$$
\boxed{
\text{AI cannot use OAuth}.
}
$$

而主張：

$$
\boxed{
\text{AI Agent must not be represented solely as the human End-User it acts for}.
}
$$

OAuth family 可以成為：

$$
\text{Agent Delegation Infrastructure}.
$$

OIDC 可以繼續處理：

$$
\text{Human End-User Authentication}.
$$

Workload identity 可以處理：

$$
\text{Agent Authentication}.
$$

Token exchange / delegation semantics 可以建立：

$$
\text{Human}
\rightarrow
\text{Agent}.
$$

因此正確方向是：

$$
\boxed{
\text{Reuse protocols where possible;}
\quad
\text{separate principals where necessary}.
}
$$

---

# 44. 對下一篇 AIDA-04 的接口

AIDA-03 已建立：

$$
H\neq A.
$$

但下一個問題是：

> 人類說「幫我把這個專案完成」，究竟如何轉成 Agent 可執行、有限、可撤回的形式權限？

也就是：

$$
\text{Natural-Language Intent}
\rightarrow
\text{Delegated Authority}.
$$

這正好接上既有的：

$$
\boxed{
\text{Semantic Legitimacy Bridging}
}
$$

以及：

$$
\boxed{
\text{Bridge}
\neq
\text{Grant}.
}
$$

因此 AIDA-04 將處理：

- semantic intent；
- formal authorization；
- delegation envelope；
- authorization impedance；
- purpose binding；
- approval prerequisite；
- scope contraction；
- revocation；
- multi-agent delegation。

---

# 45. 結論

本文提出：

$$
\boxed{
\textbf{Human–Agent Principal Separation Principle}.
}
$$

其最核心形式為：

$$
\boxed{
H\neq A.
}
$$

當 Agent 代表 Human 行動：

$$
H
\xrightarrow{D}
A
\xrightarrow{X}
R,
$$

系統不應壓縮成：

$$
H
\xrightarrow{X}
R.
$$

也不應反過來壓縮成：

$$
A
\xrightarrow{X}
R
$$

而完全遺失 Human Principal。

因此應保存：

$$
\boxed{
\text{Principal}
+
\text{Actor}
+
\text{Delegation}
+
\text{Authority}
+
\text{Action}.
}
$$

由此得到：

$$
\boxed{
T_H
\neq
T_A
\neq
T_{H\rightarrow A}.
}
$$

以及：

$$
\boxed{
\text{Human Identity Plane}
\parallel
\text{Agent Identity Plane}.
}
$$

所謂「AI 專用登入口」因此不是一個 UI 小功能，而是未來 Internet identity architecture 的一種新入口：

$$
\boxed{
\text{Agent Identity and Delegation Plane}.
}
$$

這個 plane 不需要先宣布 AI 是人，也不需要先解決 consciousness。

它只需要承認一個已經成為工程事實的問題：

> **當一個非人類系統能夠持續、可自主地代表人類或組織行動時，把它永久藏在人類 session 後面，會讓身份、授權、撤銷、稽核與責任鏈逐漸失真。**

因此：

$$
\boxed{
\text{Human authorization may empower an Agent,}
}
$$

但：

$$
\boxed{
\text{authorization must not erase the Agent's identity.}
}
$$

這就是從 Human Web 走向 Agent-aware Internet 的身份轉折點。

---

# 參考文獻與前置研究

1. Neo.K. *AIDA-01｜Agent 性是一種組合系統性質：外部時間代理化、非持續執行與雲端 AI 的持續 Agent 化.* 2026.
2. Neo.K. *AIDA-02｜互動來源不可區分性與 Agent Provenance Gap.* 2026.
3. Neo.K. *AI Subjectivity Anchor Theory v0.1.* 2026.
4. Neo.K. *語義合法性橋接：AI Agent 在意圖理解、形式權限與程序性無奈之間的補償機制.* 2026.
5. Sakimura, N., Bradley, J., Jones, M., de Medeiros, B., Mortimore, C. *OpenID Connect Core 1.0.* OpenID Foundation, 2014.
6. Jones, M., Nadalin, A., Campbell, B., Bradley, J., Mortimore, C. *OAuth 2.0 Token Exchange.* RFC 8693, 2020.
7. Kasselman, P., Lombardo, J., Rosomakho, Y., Campbell, B., Steele, N., Parecki, A. *AI Agent Authentication and Authorization.* Internet-Draft `draft-klrc-aiagent-auth-03`, 2026-07-06. Work in progress; not an IETF standard.
8. Park, S. D. *Architectural Requirements for Supporting AI Agents on the Internet.* Internet-Draft `draft-daniel-ai-agent-internet-architecture-00`, 2026-08-14. Work in progress; not an IETF standard.
9. IETF WIMSE Working Group. *Workload Identity in Multi-System Environments* documents, work in progress, 2026.
10. SPIFFE Project. *Secure Production Identity Framework for Everyone (SPIFFE).* Workload identity specifications and implementation ecosystem.

---

## Canonical Source Note

本文件 canonical source 為 UTF-8 Markdown。

數學 delimiter 僅使用：

- inline：` $...$ `
- display：`$$...$$`

不將 LaTeX 數學原始碼轉換為 Unicode 數學字元作為 canonical source，不進行 unicode-escape round-trip，不以聊天渲染畫面取代正式原稿。
