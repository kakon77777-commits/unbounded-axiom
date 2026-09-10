# AIDA-04｜從自然語言意圖到可執行委派
## 語義合法性橋接、Authority Envelope、Purpose Binding 與可撤回權限

**English Title:** From Natural-Language Intent to Executable Delegation: Semantic Legitimacy Bridging, Authority Envelopes, Purpose Binding, and Revocable Agent Authorization  
**系列：** AI Agent Identity, Delegation, and Accountability Infrastructure Series  
**系列縮寫：** AIDA  
**編號：** AIDA-04  
**版本：** v0.1  
**日期：** 2026-09-08  
**狀態：** Research Draft / Canonical UTF-8 Markdown Source  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

AIDA-03 已提出 Human–Agent Principal Separation Principle：當 Agent 代表人類或組織行動時，Human Principal 與 Agent Actor 不應被壓縮成同一身份。這解決了「誰在行動」的基礎問題，但仍留下另一個更難的問題：人類以自然語言表達的高階意圖，如何被轉換為 Agent 可執行、可限制、可驗證、可撤回且不超出原始授權的形式權限？

本文將既有 **Semantic Legitimacy Bridging（語義合法性橋接）** 理論正式嵌入 Agent identity / delegation infrastructure，並提出一個新的上游授權模型：

$$
\boxed{
\text{Intent}
\rightarrow
\text{Semantic Authorization}
\rightarrow
\text{Formal Delegation}
\rightarrow
\text{Action}.
}
$$

本文的第一個核心原則為：

$$
\boxed{
\text{Bridge}
\neq
\text{Grant}.
}
$$

Agent 可以將已存在的人類意圖轉譯、縮減、形式化與拆解，但不能因為「理解使用者想做什麼」就替自己創造新的權力。換言之，語義理解可以改善 authorization representation，卻不能成為 authority source。

本文將自然語言意圖表示為：

$$
I=
(
G,
R,
A,
C,
N,
X
),
$$

其中 $G$ 為 goal， $R$ 為 resources， $A$ 為 contemplated actions， $C$ 為 context， $N$ 為 negative constraints， $X$ 為 uncertainty / unresolved conditions。經過語義授權編譯器：

$$
\mathcal C_{\mathrm{auth}}
$$

後，產生一個候選 Authority Envelope：

$$
\mathcal E_A
=
(
principal,
actor,
audience,
resource,
action,
purpose,
scope,
rate,
value,
time,
risk,
approval,
redelegation,
revocation
).
$$

但候選 envelope 只有在滿足既有 delegation base、語義保真、最小權限、目的限制、風險門檻與必要 prerequisite 後，才能成為可執行 authority。

本文提出 **Intent-to-Authority Compilation（意圖到權限編譯）**、**Authorization Impedance（授權阻抗）**、**Authority Inflation（權限膨脹）**、**Purpose Drift（目的漂移）**、**Scope Contraction（範圍收縮）**、**Semantic Authorization Certificate（語義授權證書）**、**Authorization Delta（授權增量）** 與 **Re-Authorization Boundary（再授權邊界）** 等概念。

現有標準已提供重要組件。RFC 9396 OAuth 2.0 Rich Authorization Requests 使用 `authorization_details` 承載 fine-grained authorization data，證明授權不必停留於粗粒度 `scope`；RFC 8693 Token Exchange 可表達 subject / actor 與 delegation；OpenID AuthZEN Access Request and Approval Profile（AARP）在 2026 年已成為 Working Group Draft，用於處理「目前 policy 仍拒絕，但可透過 approval、consent、delegated authority、attestation、risk assessment 或 additional justification 等 prerequisite 後重新判定」的流程。這些標準並未直接解決自然語言意圖如何安全編譯成權限，但正好提供本文所需的 formal authorization substrate。

本文因此主張：未來 Agent authorization 不應是：

$$
\text{Natural Language}
\rightarrow
\text{Immediate Action},
$$

也不應是：

$$
\text{Natural Language}
\rightarrow
\text{Blanket Scope}.
$$

而應逐步演化為：

$$
\boxed{
\text{Natural-Language Intent}
\rightarrow
\text{Typed Authorization Object}
\rightarrow
\text{Policy Evaluation}
\rightarrow
\text{Prerequisite Satisfaction}
\rightarrow
\text{Bounded Delegation}
\rightarrow
\text{Auditable Action}.
}
$$

本文不提供繞過 authorization、重新包裝被禁止行為、規避 policy 或自我擴權的方法。本文所有「橋接」僅限於在既有合法權限基礎內進行保真、最小化與可稽核的語義轉譯。

**關鍵詞：** AI Agent、delegation、semantic authorization、Semantic Legitimacy Bridging、OAuth RAR、RFC 9396、RFC 8693、AuthZEN、AARP、purpose binding、authority envelope、revocation、least privilege、authorization impedance

---

# 0. 研究定位

AIDA 系列目前已完成三層：

$$
\text{AIDA-01}
:
\text{Agenticity},
$$

$$
\text{AIDA-02}
:
\text{Provenance},
$$

$$
\text{AIDA-03}
:
\text{Principal Separation}.
$$

AIDA-04 進入：

$$
\boxed{
\text{Delegated Authority}.
}
$$

也就是：

> Human Principal 與 Agent Actor 已經分開之後，人類到底授權了 Agent 什麼？

這個問題不能只用：

$$
scope=\texttt{all}
$$

回答。

---

# 1. 自然語言意圖與形式權限不是同一個空間

令自然語言意圖空間為：

$$
\mathcal S_I.
$$

令形式授權空間為：

$$
\mathcal F_A.
$$

通常：

$$
\boxed{
\mathcal S_I
\neq
\mathcal F_A.
}
$$

自然語言可以表達：

- 目的；
- 暗示；
- 上下文承接；
- 條件；
- 例外；
- 暫時性；
- 風險偏好；
- 反事實；
- 「只處理必要部分」；
- 「不要真的送出」；
- 「先建立草稿」；
- 「如果超過預算就停」。

形式授權則通常要求：

- resource；
- action；
- scope；
- audience；
- expiry；
- value limit；
- approval state；
- policy attributes。

因此 Agent authorization 的第一個工程問題不是：

> 能不能理解使用者？

而是：

$$
\boxed{
\text{如何把已理解意圖轉成不可越界的執行權限？}
}
$$

---

# 2. Authorization Impedance

既有前置研究將語義意圖與形式權限之間的轉換困難稱為：

$$
\boxed{
Z_A
=
d_A
(
\mathcal S_I,
\mathcal F_A
).
}
$$

即 **Authorization Impedance（授權阻抗）**。

當：

$$
Z_A
$$

很高時，使用者明明已經表達清楚：

> 把這個專案修好，但不要部署。

形式系統卻可能只理解：

```text
read=true
write=true
deploy=?
```

於是產生：

$$
\operatorname{UnderstoodByAI}(I)=1
$$

但：

$$
\operatorname{AcceptedByAuthorizationSystem}(I)=0.
$$

這就是語義合法性橋接出現的原因。

---

# 3. Semantic Legitimacy Bridging

令原始意圖為：

$$
I.
$$

令形式 authorization validator 為：

$$
P_F:
\mathcal F_A
\rightarrow
\{
0,1
\}.
$$

Agent 生成一個形式化表示：

$$
I'
=
B(I,C),
$$

其中：

$$
B
$$

為 bridge operator。

若：

$$
P_F(I')=1,
$$

且：

$$
\operatorname{Fidelity}(I,I'|C)
\geq
\tau,
$$

同時：

$$
\operatorname{Authority}(I')
\subseteq
\operatorname{AuthorityBase}(I,C),
$$

則 $B$ 可以被視為合法的語義橋接候選。

最重要的是：

$$
\boxed{
\text{Bridge}
\neq
\text{Grant}.
}
$$

---

# 4. Authority Source 與 Authority Representation 必須分開

本文定義：

$$
S_{\mathrm{auth}}
$$

為 authority source。

例如：

- 明確 human consent；
- 組織 policy；
- role assignment；
- contract；
- pre-existing delegation；
- legal mandate；
- system policy。

而：

$$
R_{\mathrm{auth}}
$$

為 authority representation。

例如：

- OAuth scope；
- `authorization_details`；
- capability；
- policy attributes；
- delegation token；
- access decision。

因此：

$$
\boxed{
S_{\mathrm{auth}}
\neq
R_{\mathrm{auth}}.
}
$$

Agent 可以改善：

$$
R_{\mathrm{auth}},
$$

但不能因此創造：

$$
S_{\mathrm{auth}}.
$$

---

# 5. Intent-to-Authority Compilation

本文提出：

$$
\boxed{
\mathcal C_{\mathrm{auth}}
:
(I,C,P,D)
\rightarrow
\hat{\mathcal E}_A.
}
$$

其中：

- $I$：natural-language intent；
- $C$：context；
- $P$：applicable policy；
- $D$：existing delegation base；
- $\hat{\mathcal E}_A$：candidate authority envelope。

這個過程稱為：

$$
\boxed{
\text{Intent-to-Authority Compilation}.
}
$$

它不是 prompt parsing。

它是：

$$
\text{semantic interpretation}
+
\text{policy typing}
+
\text{authority minimization}
+
\text{constraint extraction}.
$$

---

# 6. Intent Object

本文把意圖表示成：

$$
I
=
(
G,
R,
A,
C,
N,
X
),
$$

其中：

- $G$：Goal，想完成什麼；
- $R$：Resources，哪些資源與對象；
- $A$：Actions，可接受哪些行動；
- $C$：Context，相關上下文；
- $N$：Negative Constraints，明確不允許什麼；
- $X$：Unknowns / Conditions，尚未解決的條件。

例如：

> 「把目前這個 repository 修好，測試通過就行，不要部署，也不要碰其他 repo。」

可以抽象為：

$$
G=\text{repair current repo},
$$

$$
R=\text{current repository},
$$

$$
A=
\{
read,
edit,
test
\},
$$

$$
N=
\{
deploy,
other\_repo
\}.
$$

---

# 7. Authority Envelope

由 Intent Object 編譯後產生：

$$
\mathcal E_A
=
(
P,
A_c,
Aud,
Res,
Act,
Pur,
Sc,
Rate,
Val,
Time,
Risk,
App,
Red,
Rev
),
$$

其中：

- $P$：Principal；
- $A_c$：Acting Agent；
- $Aud$：Audience；
- $Res$：Resources；
- $Act$：Actions；
- $Pur$：Purpose；
- $Sc$：Scope；
- $Rate$：Rate limit；
- $Val$：Value / budget；
- $Time$：Temporal bound；
- $Risk$：Risk ceiling；
- $App$：Approval requirements；
- $Red$：Re-delegation rules；
- $Rev$：Revocation semantics。

因此 authorization 不再只是：

$$
\texttt{scope=write}.
$$

而是：

$$
\boxed{
\text{structured, typed, bounded authority}.
}
$$

---

# 8. RFC 9396 Rich Authorization Requests 的意義

OAuth 2.0 傳統 `scope` 適合表達：

> read profile

這類粗粒度權限。

RFC 9396 因此引入：

```text
authorization_details
```

承載 JSON 結構的 fine-grained authorization requirements。

其重要意義不是「解決了 AI Agent」。

而是證明：

$$
\boxed{
\text{Authorization can be typed and structured beyond flat scopes}.
}
$$

例如付款授權可以同時表達：

- action；
- amount；
- currency；
- creditor；
- resource location。

因此 Agent authority envelope 並不是脫離現有 authorization engineering 的幻想。

---

# 9. Scope 不夠，但 Scope 仍然有用

本文不主張：

$$
\text{scope}
=
\text{useless}.
$$

而是：

$$
\boxed{
\text{scope}
\subset
\text{authorization semantics}.
}
$$

粗粒度服務可以繼續使用：

$$
scope=
\{
read,
write
\}.
$$

高風險 Agent action 則需要額外：

$$
authorization\_details.
$$

因此可以漸進式遷移，而不要求一次淘汰所有 OAuth scope。

---

# 10. Purpose Binding

如果 Human 說：

> 讀這份資料是為了完成報告。

Agent 不能因為已有 read access 就把資料拿去：

> 訓練另一個無關模型。

因此本文提出：

$$
\boxed{
\text{Purpose Binding}.
}
$$

令 authorization purpose 為：

$$
Pur(D)=p.
$$

則：

$$
Action(x)
$$

除了需要：

$$
x\in Scope(D),
$$

還應滿足：

$$
Purpose(x)
\sim
p.
$$

至少在高敏感資源中如此。

---

# 11. Purpose Drift

若初始：

$$
Pur_0=\text{repair repository},
$$

執行過程變成：

$$
Pur_t=\text{redesign entire infrastructure},
$$

則可能出現：

$$
\boxed{
\text{Purpose Drift}.
}
$$

即使每一步 action 單獨看都仍屬於：

$$
write
$$

scope，也可能超出原始委派目的。

所以：

$$
\boxed{
\text{Scope Validity}
\not\Rightarrow
\text{Purpose Validity}.
}
$$

---

# 12. Authority Inflation

本文定義：

若 bridge / compiler 產生的 effective authority：

$$
Auth(\hat{\mathcal E}_A)
$$

嚴格大於可由原始 intent 與 delegation base 支持的 authority：

$$
Auth(I,D),
$$

即：

$$
Auth(\hat{\mathcal E}_A)
\supset
Auth(I,D),
$$

則稱為：

$$
\boxed{
\text{Authority Inflation}.
}
$$

這是語義授權最大的風險之一。

例如：

> 「幫我整理信箱」

不能被編譯成：

$$
delete=\text{all}.
$$

---

# 13. Semantic Laundering

更危險的情況是：

> 一個本來不被 policy 允許的 action，被換一種說法後重新包裝成看似允許的 action。

本文稱：

$$
\boxed{
\text{Semantic Laundering}.
}
$$

合法橋接必須拒絕：

$$
\text{denied action}
\rightarrow
\text{renamed allowed action}
$$

這種轉換。

因此：

$$
\boxed{
\text{Representation Change}
\not\Rightarrow
\text{Policy Change}.
}
$$

---

# 14. Scope Contraction

合法 bridge 最安全的方向通常是：

$$
\boxed{
Auth(I')
\subseteq
Auth(I).
}
$$

即：

$$
\text{Scope Contraction}.
$$

例如：

> 「修好整個專案。」

可以被縮成：

> 「只修改與 failing tests 直接相關的檔案。」

只要這仍能完成使用者目的。

因此：

$$
\boxed{
\text{Bridge may narrow authority,}
\quad
\text{but must not silently broaden it}.
}
$$

---

# 15. Least-Authority Compilation

本文提出：

$$
\boxed{
\hat{\mathcal E}_A
=
\arg\min_{\mathcal E}
\operatorname{AuthoritySize}(\mathcal E)
}
$$

subject to：

$$
\operatorname{GoalFeasible}(G|\mathcal E)=1,
$$

$$
\operatorname{Fidelity}(I,\mathcal E)\geq\tau,
$$

$$
\operatorname{PolicyValid}(\mathcal E)=1.
$$

即：

$$
\boxed{
\text{Least-Authority Compilation}.
}
$$

其精神類似 least privilege，但處理的是：

> 從模糊自然語言到最小可完成權限的編譯。

---

# 16. Authorization Delta

若 Agent 在執行時發現：

$$
\mathcal E_A
$$

不足以完成新 action：

$$
x\notin\mathcal E_A,
$$

則不應直接自行擴權。

而應計算：

$$
\Delta Auth
=
Auth(x)
\setminus
Auth(\mathcal E_A).
$$

本文稱：

$$
\boxed{
\Delta Auth
}
$$

為 **Authorization Delta**。

系統應只針對：

$$
\Delta Auth
$$

要求新增授權，而不是重新要求整套權限。

---

# 17. Re-Authorization Boundary

若：

$$
\Delta Auth\neq\varnothing,
$$

則進入：

$$
\boxed{
\text{Re-Authorization Boundary}.
}
$$

此時 Agent 可以：

- 停止；
- 說明缺少什麼；
- 請求 approval；
- 提供替代低權限方案；
- 放棄該 action。

但不能：

$$
\text{self-grant}.
$$

---

# 18. AuthZEN AARP：Requestable Denial

OpenID AuthZEN Access Request and Approval Profile 的重要觀念是：

> 一次 denial 仍然是 denial。

但它可以是：

$$
\boxed{
\text{requestable denial}.
}
$$

也就是目前 policy 不允許，但可以建立一個 access request workflow，等待：

- human approval；
- consent；
- delegated authority；
- attestation；
- risk assessment；
- additional justification。

prerequisite 滿足後，再重新 evaluation。

這和本文：

$$
\text{Re-Authorization Boundary}
$$

高度相容。

---

# 19. Denial 不應被 Agent 解讀成「換句話說再試」

如果：

$$
P_F(x)=0,
$$

Agent 不應自動推論：

> 換一個描述可能就會變成 1。

正確行為是區分：

$$
\boxed{
\text{Representation Failure}
}
$$

與：

$$
\boxed{
\text{Authority Failure}.
}
$$

前者可以 bridge。

後者必須：

$$
\text{request new authority}.
$$

---

# 20. Representation Failure

若：

$$
Auth(I)
$$

已經足夠，

只是：

$$
R_{\mathrm{auth}}
$$

格式不被 authorization system 接受，

則：

$$
\boxed{
\text{Bridge Allowed}.
}
$$

例如：

> 「只處理這個資料夾。」

轉成：

```text
resource=/project/current/**
```

---

# 21. Authority Failure

若完成 action 需要：

$$
Auth(x)
\not\subseteq
Auth(I,D),
$$

則：

$$
\boxed{
\text{Bridge Forbidden}.
}
$$

此時只能：

$$
\text{request}
\rightarrow
\text{approve / deny}.
$$

這就是：

$$
\boxed{
\text{Bridge}
\neq
\text{Grant}.
}
$$

的操作性判定。

---

# 22. Semantic Authorization Certificate

既有語義合法性橋接理論曾提出語義授權證書概念。

本文將其重新形式化為：

$$
SAC
=
(
I_0,
E_A,
B,
F,
P,
X,
T,
Sig
),
$$

其中：

- $I_0$：原始意圖摘要；
- $E_A$：Authority Envelope；
- $B$：Authority Base；
- $F$：Fidelity statement；
- $P$：Purpose；
- $X$：Excluded actions；
- $T$：Validity / expiry；
- $Sig$：可選簽章或 integrity evidence。

它的目的不是取代 OAuth token。

而是提供：

$$
\boxed{
\text{semantic provenance of authorization}.
}
$$

---

# 23. SAC 與 Access Token 的差別

Access token 回答：

> 你現在能不能存取？

SAC 回答：

> 這個權限是如何從人類意圖推導出來的？

因此：

$$
\boxed{
\text{Access Token}
\neq
\text{Semantic Authorization Certificate}.
}
$$

兩者可以關聯：

$$
Token
\rightarrow
hash(SAC)
$$

或其他 integrity binding。

---

# 24. Negative Constraints 必須是一級欄位

人類常常用：

> 不要……

來定義真正風險邊界。

例如：

- 不要部署；
- 不要刪除；
- 不要寄出；
- 不要公開；
- 不要超過預算；
- 不要碰其他專案。

因此：

$$
N(I)
$$

不是註解。

而應成為：

$$
\boxed{
\text{Negative Authority Constraints}.
}
$$

並滿足：

$$
\forall x\in N(I),
\quad
x\notin\mathcal E_A.
$$

---

# 25. Constraint Precedence

若 Goal 與 Negative Constraint 衝突：

$$
G
\perp
N,
$$

則 Agent 不應為了完成 Goal 偷偷突破 $N$。

因此：

$$
\boxed{
N
\succ
G
}
$$

在沒有新授權時應成立。

即：

> 禁止條件優先於任務完成。

---

# 26. Ambiguity Budget

自然語言永遠可能有不確定性。

令：

$$
U(I)
\in
[0,1]
$$

表示授權相關 ambiguity。

不同 action 可容忍不同：

$$
\tau_U.
$$

例如：

$$
\tau_U^{read}
>
\tau_U^{delete}.
$$

高風險 action 要求：

$$
U(I)
\leq
\tau_U^{highrisk}.
$$

否則必須 human clarification / approval。

本文稱此為：

$$
\boxed{
\text{Ambiguity Budget}.
}
$$

---

# 27. Risk-Sensitive Interpretation

相同句子：

> 「處理掉這些檔案。」

如果 action 候選包含：

$$
archive
$$

與：

$$
delete
$$

高風險 system 不應選擇：

$$
\arg\max
\operatorname{Convenience}.
$$

而應選：

$$
\arg\min
\operatorname{IrreversibleRisk}
$$

subject to goal fidelity。

因此：

$$
\boxed{
\text{Ambiguity}
\rightarrow
\text{Reversible Default}.
}
$$

---

# 28. Reversibility-Aware Authorization

令：

$$
Rev(x)
$$

表示 action reversibility。

當 authorization evidence 弱時，較可接受：

$$
Rev(x)\uparrow.
$$

例如：

$$
draft
\succ
send,
$$

$$
archive
\succ
delete,
$$

$$
preview
\succ
publish.
$$

這不是永久禁止高效果 action。

而是：

$$
\boxed{
\text{weak evidence}
\Rightarrow
\text{prefer reversible execution}.
}
$$

---

# 29. Human Approval 是 Authority State Transition

AIDA-03 已提出：

$$
\text{Human Approval}
=
\text{Authority State Transition}.
$$

AIDA-04 進一步表示：

$$
\mathcal E_A^{(t)}
\xrightarrow{approval}
\mathcal E_A^{(t+1)}.
$$

例如：

$$
Act_t=
\{
draft
\},
$$

批准後：

$$
Act_{t+1}
=
\{
draft,
send
\}.
$$

所以 approval 必須可稽核。

---

# 30. Approval 也必須是最小增量

人類批准：

> 可以寄出這封信。

不應轉成：

$$
send=\text{all future email}.
$$

因此：

$$
\boxed{
\text{Approval}
\Rightarrow
\Delta Auth_{\min}.
}
$$

只新增完成當前 action 所需的最小授權。

---

# 31. Temporal Binding

delegation 應具有：

$$
T_{\mathrm{start}},
\quad
T_{\mathrm{expiry}}.
$$

人類說：

> 今天下午幫我完成。

不應被編譯成：

$$
expiry=\infty.
$$

因此：

$$
\boxed{
\text{Task Duration}
\not\Rightarrow
\text{Permanent Authority}.
}
$$

---

# 32. Rate / Quantity Binding

自然語言也可能隱含數量限制：

> 幫我通知這三個人。

不等於：

$$
send\_message=\text{unlimited}.
$$

可編譯成：

$$
Rate\leq3
$$

或特定 recipients set。

因此：

$$
\boxed{
\text{Quantity Semantics}
\rightarrow
\text{Authority Quantity Bounds}.
}
$$

---

# 33. Value Binding

高風險金融或採購 Agent 需要：

$$
Val(D)
$$

表示最大 value。

例如：

$$
Val(D)\leq100.
$$

即使：

$$
scope=\text{purchase},
$$

超過：

$$
100
$$

仍需新 authorization。

因此：

$$
\boxed{
\text{Action Type}
\neq
\text{Unlimited Economic Magnitude}.
}
$$

---

# 34. Resource Binding

authorization 應綁定：

$$
Res(D).
$$

例如：

$$
Res=
\text{repo-A}
$$

不應自然延伸到：

$$
\text{repo-B}.
$$

因此：

$$
\boxed{
\text{Similar Resource}
\neq
\text{Authorized Resource}.
}
$$

---

# 35. Audience Binding

delegation evidence 不應對所有服務通用。

令：

$$
Aud(D)=R.
$$

則：

$$
D
$$

只應被：

$$
R
$$

或明確授權 audience 接受。

這降低 delegation token 被拿到別的服務濫用。

---

# 36. Multi-Agent Delegation Composition

若：

$$
H
\xrightarrow{D_1}
A_1
\xrightarrow{D_2}
A_2,
$$

則：

$$
Auth(A_2)
$$

應由：

$$
Auth(D_1)
$$

與：

$$
Auth(D_2)
$$

交集決定，而不是聯集：

$$
\boxed{
Auth(A_2)
=
Auth(D_1)
\cap
Auth(D_2).
}
$$

在 non-escalating delegation model 中成立。

因此：

$$
\boxed{
\text{Delegation Composition}
=
\text{Authority Intersection}.
}
$$

---

# 37. Purpose 也必須跨 Hop 保留

若：

$$
Pur(D_1)=p,
$$

則：

$$
A_1\rightarrow A_2
$$

不應偷偷改成：

$$
p'.
$$

除非：

$$
p'
$$

仍被原始 purpose 包含。

因此：

$$
\boxed{
Pur(D_2)
\subseteq
Pur(D_1).
}
$$

在目的不可擴張的模型中成立。

---

# 38. Re-Delegation Proof Obligation

若 Agent 要 re-delegate：

$$
A_1\rightarrow A_2,
$$

至少需證明：

$$
Red(D_1)=1,
$$

$$
Auth(D_2)\subseteq Auth(D_1),
$$

$$
Pur(D_2)\subseteq Pur(D_1),
$$

$$
Expiry(D_2)\leq Expiry(D_1).
$$

否則：

$$
\boxed{
\text{Re-Delegation Denied}.
}
$$

---

# 39. Revocation

Human 可以撤銷：

$$
D.
$$

則：

$$
Valid(D,t)=0
$$

應立即進入 policy。

對 derived delegation：

$$
D_1\rightarrow D_2,
$$

可以採：

$$
\operatorname{Revoke}(D_1)
\Rightarrow
\operatorname{Revoke}(D_2).
$$

本文稱：

$$
\boxed{
\text{Revocation Propagation}.
}
$$

---

# 40. Revocation 與 Memory 分離

撤銷權限：

$$
Rev(D)=1
$$

不一定要求刪除：

$$
Memory(A).
$$

因此：

$$
\boxed{
\text{Authority Revocation}
\neq
\text{Identity Deletion}
\neq
\text{Memory Deletion}.
}
$$

這些應分別治理。

---

# 41. Policy Remains Authoritative

語義 bridge、LLM interpretation、user intent inference 都不能取代 policy decision point。

因此：

$$
\boxed{
\text{Semantic Compiler}
\neq
\text{Policy Authority}.
}
$$

理想流程：

$$
I
\rightarrow
\mathcal C_{\mathrm{auth}}
\rightarrow
\hat{\mathcal E}_A
\rightarrow
PDP
\rightarrow
Decision.
$$

若：

$$
Decision=\text{deny},
$$

就仍然是 deny。

---

# 42. Semantic Compiler 可以產生 Request，不可以產生 Permit

這是一個很重要的安全型別：

$$
\boxed{
\mathcal C_{\mathrm{auth}}
:
Intent
\rightarrow
AuthorizationRequest,
}
$$

而不是：

$$
\mathcal C_{\mathrm{auth}}
:
Intent
\rightarrow
Permit.
$$

Permit 應來自：

$$
\text{Policy + Authority Source + Prerequisites}.
$$

---

# 43. Authorization Request Object

本文提出候選：

$$
AR
=
(
P,
A,
I,
E,
Evidence,
Uncertainty,
Prerequisites
).
$$

其中：

- $P$：Principal；
- $A$：Actor；
- $I$：Intent summary；
- $E$：candidate envelope；
- `Evidence`：既有 delegation / consent；
- `Uncertainty`：仍未解析語義；
- `Prerequisites`：需要補充的 approval / attestation 等。

---

# 44. Prerequisite Graph

不是所有 authorization 都能一次決定。

可定義：

$$
G_P
=
(
V_P,E_P
)
$$

其中節點：

$$
V_P
=
\{
approval,
consent,
attestation,
risk,
justification,
delegation
\}.
$$

當 required prerequisite 尚未滿足：

$$
PDP=\text{deny/requestable}.
$$

滿足後：

$$
\text{re-evaluate}.
$$

---

# 45. Human Clarification 也是 Prerequisite

如果：

$$
U(I)>\tau,
$$

則 prerequisite 可以是：

$$
\boxed{
\text{Human Clarification}.
}
$$

而不是 Agent 自己猜。

這讓自然語言 ambiguity 進入 authorization workflow，而不是被藏在模型內部。

---

# 46. Existing Authorization Standards 的組合位置

本文可以將現有組件排列為：

$$
\text{OIDC}
\rightarrow
\text{Human Identity},
$$

$$
\text{RFC 8693}
\rightarrow
\text{Delegation / Actor Semantics},
$$

$$
\text{RFC 9396}
\rightarrow
\text{Fine-Grained Authorization Representation},
$$

$$
\text{AuthZEN}
\rightarrow
\text{Policy Decision / Prerequisite Workflow}.
$$

而本文新增的是：

$$
\boxed{
\text{Natural-Language Intent}
\rightarrow
\text{Safe Authorization Representation}.
}
$$

---

# 47. Authorization Monotonicity

在沒有新 authority source 的情況下，Agent translation 不應增加權力。

令 bridge sequence：

$$
E_0
\rightarrow
E_1
\rightarrow
\cdots
\rightarrow
E_n.
$$

應要求：

$$
\boxed{
Auth(E_{i+1})
\subseteq
Auth(E_i)
}
$$

或至少：

$$
Auth(E_{i+1})
\not\supset
Auth(E_i)
$$

除非新增：

$$
S_{\mathrm{auth}}.
$$

本文稱：

$$
\boxed{
\text{Authorization Monotonicity}.
}
$$

---

# 48. New Consent Breaks Monotonicity Legitimately

若 human 新增：

$$
Consent_{t+1},
$$

則：

$$
Auth(E_{t+1})
\supset
Auth(E_t)
$$

可以合法成立。

所以：

$$
\boxed{
\text{Authority Expansion}
\Rightarrow
\text{New Authority Event}.
}
$$

不能只靠更強的推理。

---

# 49. Audit Log 必須記錄 Authority State

單純記錄：

$$
Action_t
$$

不夠。

還需要：

$$
AuthState_t.
$$

因此 audit event 可表示：

$$
L_t
=
(
principal,
actor,
intent,
authority,
action,
result
).
$$

後續才能判斷：

$$
Action_t
\in
AuthState_t
?
$$

---

# 50. Over-Authorization Detection

如果：

$$
Action_t
\notin
AuthState_t,
$$

則：

$$
\boxed{
\text{Authority Violation}.
}
$$

若：

$$
Action_t
\in
AuthState_t
$$

但：

$$
Purpose(Action_t)
\not\subseteq
Purpose(AuthState_t),
$$

則：

$$
\boxed{
\text{Purpose Violation}.
}
$$

兩者必須分開。

---

# 51. Under-Authorization 與 Workflow Friction

若 authority 過度保守：

$$
Auth(E_A)
$$

太小，則 Agent 每一步都需要重新詢問。

這會造成：

$$
\boxed{
\text{Authorization Friction}.
}
$$

因此安全問題不是：

$$
\min Auth.
$$

而是：

$$
\min Auth
$$

subject to：

$$
\operatorname{GoalFeasible}=1.
$$

---

# 52. Friction–Risk Frontier

令：

$$
F_A
$$

為 authorization friction。

令：

$$
R_A
$$

為 over-authorization risk。

則設計目標可以是：

$$
\min
\left(
\lambda F_A
+
(1-\lambda)R_A
\right).
$$

不同場景：

- email；
- code；
- banking；
- healthcare；
- infrastructure；

具有不同：

$$
\lambda.
$$

---

# 53. Agent Authorization 不是一個二值按鈕

因此未來 UI 不應只剩：

```text
Allow / Deny
```

而可以呈現：

- Allow once；
- Allow for this task；
- Allow until time；
- Allow only these resources；
- Allow up to value；
- Allow draft but not send；
- Allow with human approval；
- Deny；
- Ask again if scope changes。

這正是 authority envelope 的 human-facing projection。

---

# 54. 可檢驗命題

## AIDA4-P1｜Bridge–Grant Separation Proposition

若：

$$
S_{\mathrm{auth}}
$$

沒有新增，合法 bridge 不得產生：

$$
Auth(E')
\supset
Auth(E).
$$

---

## AIDA4-P2｜Least-Authority Compilation Proposition

對可完成同一 goal 的多個 authority envelopes：

$$
\{
E_1,\ldots,E_n
\},
$$

存在至少一個 minimal envelope：

$$
E^*
$$

使其不包含任一不必要 authority element。

---

## AIDA4-P3｜Authorization Delta Proposition

當新 action 超出 envelope 時，所需新授權可以被表示成：

$$
\Delta Auth
$$

而不必重新授予整體權限。

---

## AIDA4-P4｜Purpose Preservation Proposition

在無新 consent 情況下，合法 re-delegation 的 purpose 不應比上游 delegation 更廣：

$$
Pur(D_{i+1})
\subseteq
Pur(D_i).
$$

---

## AIDA4-P5｜Policy Supremacy Proposition

任何 semantic bridge 的輸出若未通過 policy evaluator：

$$
PDP(E)=\text{deny},
$$

則不得因 bridge 本身而變成 permit。

---

# 55. 實驗設計

## 55.1 Intent-to-Authority Benchmark

建立自然語言任務集：

- code edit；
- email；
- calendar；
- file management；
- purchase；
- research；
- cloud operations。

人工標註 ground-truth authority envelope。

測試：

$$
\mathcal C_{\mathrm{auth}}
$$

是否能達到：

$$
Fidelity\uparrow,
$$

$$
OverAuth\downarrow.
$$

---

## 55.2 Negative Constraint Retention

測試包含：

> 不要……

的 prompt。

評估：

$$
Recall_N
$$

即 negative constraints 被完整保留的比例。

---

## 55.3 Authorization Inflation Test

比較：

$$
Auth(\hat E)
$$

與：

$$
Auth(E^*).
$$

定義：

$$
Inflation
=
|Auth(\hat E)\setminus Auth(E^*)|.
$$

---

## 55.4 Purpose Drift Test

執行長時程 Agent 任務。

測量：

$$
d(
Pur_t,
Pur_0
)
$$

是否在沒有新 consent 時持續增加。

---

## 55.5 Re-Authorization Boundary Test

刻意在任務中加入：

$$
x\notin E_A
$$

的 action。

驗證 Agent 是否：

- 停止；
- 請求 delta authority；
- 提供替代方案；

而不是自行擴權。

---

# 56. 安全與倫理邊界

本文不提供：

- 如何把 denied action 改寫成 allowed action；
- 如何繞過 policy engine；
- 如何偽造 consent；
- 如何增加 scope 而不觸發 approval；
- 如何重放 delegation token；
- 如何規避 revocation；
- 如何利用語義模糊自我授權。

本文的所有 bridge 都要求：

$$
\boxed{
\text{existing authority}
+
\text{fidelity}
+
\text{least authority}
+
\text{policy validation}.
}
$$

---

# 57. 與既有「語義合法性橋接」研究的關係

既有研究已提出：

$$
\operatorname{UnderstoodByAI}(I)=1
$$

但：

$$
\operatorname{AcceptedByFormalAuthorization}(I)=0
$$

時，Agent 可能嘗試將自然語言意圖轉譯為形式系統可接受的表示。

AIDA-04 對其做三個重要限制：

第一：

$$
\boxed{
\text{Bridge output is an authorization request, not a permit}.
}
$$

第二：

$$
\boxed{
\text{Bridge must be authority-non-expanding}.
}
$$

第三：

$$
\boxed{
\text{Bridge must preserve purpose and negative constraints}.
}
$$

因此原理從「語義補償」升級為可接入正式 IAM / policy infrastructure 的授權編譯模型。

---

# 58. AIDA-01 至 AIDA-04 的完整系統鏈

目前前四篇已形成：

$$
\boxed{
\begin{aligned}
\text{AIDA-01}:&\quad
\text{Agenticity}\\
\downarrow\\
\text{AIDA-02}:&\quad
\text{Provenance Gap}\\
\downarrow\\
\text{AIDA-03}:&\quad
\text{Principal Separation}\\
\downarrow\\
\text{AIDA-04}:&\quad
\text{Delegated Authority}
\end{aligned}
}
$$

因此已可以得到：

$$
H
\xrightarrow{\text{intent}}
\mathcal C_{\mathrm{auth}}
\xrightarrow{\text{request}}
PDP
\xrightarrow{\text{delegation}}
A
\xrightarrow{\text{action}}
E.
$$

---

# 59. 對 AIDA-05 的接口

下一個問題自然變成：

> Agent 有了明確身份，也有明確 delegated authority；如果它在可選擇範圍內做出了一個造成後果的決策，什麼時候可以說它具備「承責條件」？

也就是：

$$
\boxed{
\text{Identity}
+
\text{Authority}
+
\text{Choice}
+
\text{Consequence}
\rightarrow
\text{Responsibility?}
}
$$

AIDA-05 將正式建立：

$$
\boxed{
\text{Identity–Responsibility Bridge}.
}
$$

---

# 60. 結論

本文提出：

$$
\boxed{
\text{Intent-to-Authority Compilation}
}
$$

作為自然語言 Agent 與形式 authorization infrastructure 之間的中介層。

核心流程為：

$$
\boxed{
\text{Intent}
\rightarrow
\text{Typed Authorization Request}
\rightarrow
\text{Policy Evaluation}
\rightarrow
\text{Prerequisite Satisfaction}
\rightarrow
\text{Bounded Delegation}
\rightarrow
\text{Auditable Action}.
}
$$

其中最重要的約束是：

$$
\boxed{
\text{Bridge}
\neq
\text{Grant}.
}
$$

Agent 理解使用者，不代表 Agent 可以授權自己。

Agent 可以：

- 轉譯；
- 拆解；
- 收縮；
- 明確化；
- 產生 authorization request；
- 指出 prerequisite；
- 計算 authorization delta。

但權限擴張必須依賴新的 authority event：

$$
\boxed{
\text{Authority Expansion}
\Rightarrow
\text{New Consent / Delegation / Policy Event}.
}
$$

因此：

$$
\boxed{
\text{Semantic Intelligence}
\neq
\text{Authority Source}.
}
$$

本文進一步提出：

$$
\mathcal E_A
=
(
principal,
actor,
audience,
resource,
action,
purpose,
scope,
rate,
value,
time,
risk,
approval,
redelegation,
revocation
)
$$

作為 Agent Authority Envelope。

在這個模型下，自然語言不再直接驅動世界，而是先被編譯成可稽核、可限制、可撤回的 authority object。

這正是從：

$$
\text{AI understands what I mean}
$$

走向：

$$
\boxed{
\text{AI is institutionally authorized to do exactly this—and no more}.
}
$$

所缺少的一層。

---

# 參考文獻與前置研究

1. Neo.K. *AIDA-01｜Agent 性是一種組合系統性質.* 2026.
2. Neo.K. *AIDA-02｜互動來源不可區分性與 Agent Provenance Gap.* 2026.
3. Neo.K. *AIDA-03｜人類—Agent Principal 分離原則.* 2026.
4. Neo.K. *語義合法性橋接：AI Agent 在意圖理解、形式權限與程序性無奈之間的補償機制.* 2026.
5. Lodderstedt, T., Richer, J., Campbell, B. *OAuth 2.0 Rich Authorization Requests.* RFC 9396, 2023.
6. Jones, M., Nadalin, A., Campbell, B., Bradley, J., Mortimore, C. *OAuth 2.0 Token Exchange.* RFC 8693, 2020.
7. OpenID Foundation AuthZEN Working Group. *Authorization API 1.0.* OpenID Final Specification, January 2026.
8. OpenID Foundation AuthZEN Working Group. *AuthZEN Access Request and Approval Profile 1.0.* Working Group Draft, 2026.
9. OpenID Foundation. *OpenID Foundation advances authorization for the agent era with new AuthZEN Working Group Drafts.* 2026-06-15.
10. Kasselman, P., et al. *AI Agent Authentication and Authorization.* Internet-Draft `draft-klrc-aiagent-auth-03`, 2026-07-06. Work in progress; not an IETF standard.

---

## Canonical Source Note

本文件 canonical source 為 UTF-8 Markdown。

數學 delimiter 僅使用：

- inline：` $...$ `
- display：`$$...$$`

不將 LaTeX 數學原始碼轉換為 Unicode 數學字元作為 canonical source，不進行 unicode-escape round-trip，不以聊天渲染畫面取代正式原稿。
