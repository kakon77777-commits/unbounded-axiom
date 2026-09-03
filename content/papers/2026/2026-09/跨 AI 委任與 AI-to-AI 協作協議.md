# 跨 AI 委任與 AI-to-AI 協作協議

## Cross-AI Delegation and AI-to-AI Collaboration Protocol

**系列**：AI 原生分散式組織系列，第 7 篇／共 10 篇  
**系列英文名**：AI-Native Distributed Organization Series  
**文件編號**：EML-ANDO-2026-07-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-21  
**性質**：理論框架／AI-to-AI Delegation／Agent Coordination Protocol／Authority Transfer／Handoff Runtime  
**狀態**：Public Theory Draft  
**直接前置**：《AI 研究保真與認知責任》v0.1；《分散式認知研究組織》v0.1；《共享狀態中心論》v0.1；《委任主權論》v0.1  

---

## 生成與保真聲明

本文為 AI 輔助生成的理論與工程框架草稿。本文提出的是跨 AI 委任的可治理語義框架，不宣稱已成為跨模型供應商、平台或 Agent runtime 的既成產業標準。未來若對接 A2A、MCP、API、Browser Agent 或其他協議，應再做介面映射、互通性測試與安全驗證。

本文所稱 AI-to-AI 協作不要求 AI 模仿人類身份，也不預設 AI 具有法律人格。本文聚焦於：一個合法委任來源如何將任務、權限、狀態、驗證義務、預算與停止條件可靠地傳給另一個智能節點，並使結果可追蹤、可驗證、可撤銷、可恢復與可再委任。

---

## 摘要

AI Agent 之間互相「聊天」並不等於形成可治理的組織協作。若 Agent A 只用自然語言告訴 Agent B「請繼續完成這個研究」，B 可能不知道原始意圖、目前 canonical state、可用權限、剩餘預算、哪些內容已驗證、哪些 action 可對外提交、何時必須停下、什麼情況需要回交人類，以及 B 是否可以再委任給 Agent C。

本文提出第一代「跨 AI 委任協議」，核心物件稱為 Agent Delegation Envelope：

$$
\mathfrak D_{i\rightarrow j}
=
(
DID,
RID,
I,
S,
T,
A,
B,
R,
V,
O,
C,
E,
X,
P
).
$$

其中包含 Delegation ID、Root Intent ID、意圖與任務規格、canonical state reference、task dependency、authority envelope、budget、risk policy、verification contract、output contract、checkpoint policy、escalation policy、termination conditions 與 provenance requirements。

本文提出委任生命週期：

$$
Offer
\rightarrow
Inspect
\rightarrow
Accept
\rightarrow
Execute
\rightarrow
Checkpoint
\rightarrow
Deliver
\rightarrow
Verify
\rightarrow
Commit
\rightarrow
Close.
$$

並允許：

$$
Reject,
CounterOffer,
PartialAccept,
Suspend,
Escalate,
Revoke,
DelegateFurther.
$$

本文特別區分 capability negotiation 與 authority grant，提出 authority lineage、budget inheritance、verification inheritance、state-version binding、commit-class restriction、subdelegation monotonicity，以及 Delegation Receipt、Execution Receipt、Verification Receipt、Commit Receipt 四類證明物件。

因此 AI-to-AI 的真正質變不是對話更自然，而是：

$$
\boxed{
\text{Conversation}
\rightarrow
\text{Governable Organizational Delegation}.
}
$$

**關鍵詞**：AI-to-AI Delegation、Agent Delegation Envelope、Handoff Protocol、Authority Lineage、Subdelegation、Capability Negotiation、Delegation Receipt、Cross-Agent Coordination、Distributed Organization

---

# 0. AI 對 AI 說話，為什麼還不夠？

最簡單的 handoff 是：

$$
A_i
\rightarrow
A_j:
\text{``請繼續。''}
$$

但這沒有明確包含：

- root intent；
- state version；
- task dependency；
- authority；
- budget；
- risk；
- verification；
- output schema；
- stop condition；
- escalation；
- provenance；
- commit permission。

因此：

$$
\boxed{
\text{Natural-Language Handoff}
\neq
\text{Governable Delegation}.
}
$$

---

# 1. Conversation 與 Delegation

Conversation 基本形式是：

$$
Message
\rightarrow
Response.
$$

Delegation 則是：

$$
Intent
+
State
+
Authority
+
Task
+
Budget
+
Verification
+
Termination.
$$

所以：

$$
\boxed{
\text{AI-to-AI Conversation}
\neq
\text{AI-to-AI Organizational Coordination}.
}
$$

---

# 2. Agent Delegation Envelope

定義：

$$
\mathfrak D_{i\rightarrow j}
=
(
DID,
RID,
I,
S,
T,
A,
B,
R,
V,
O,
C,
E,
X,
P
).
$$

其中：

$$
DID
=
\text{Delegation ID},
$$

$$
RID
=
\text{Root Intent / Root Delegation ID},
$$

$$
I
=
\text{Intent Specification},
$$

$$
S
=
\text{Canonical State Reference},
$$

$$
T
=
\text{Task Contract},
$$

$$
A
=
\text{Authority Envelope},
$$

$$
B
=
\text{Budget Envelope},
$$

$$
R
=
\text{Risk Policy},
$$

$$
V
=
\text{Verification Contract},
$$

$$
O
=
\text{Output Contract},
$$

$$
C
=
\text{Checkpoint Policy},
$$

$$
E
=
\text{Escalation Policy},
$$

$$
X
=
\text{Termination Conditions},
$$

$$
P
=
\text{Provenance Requirements}.
$$

Agent 傳遞的正式物件不再只是一段 prompt，而是一個可解析、可版本化、可拒絕、可撤銷的委任包。

---

# 3. Delegation Lineage

每一條委任邊都有：

$$
DID_k.
$$

多層委任：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3
$$

形成：

$$
DID_2
\rightarrow
DID_1
\rightarrow
RID.
$$

因此：

$$
\boxed{
\text{Every delegated action should remain traceable to a root intent.}
}
$$

---

# 4. Root Intent Binding

長鏈委任會產生：

$$
I_0
\rightarrow
I_1
\rightarrow
I_2
\rightarrow
\cdots.
$$

定義：

$$
\Delta_I^{(k)}
=
d(
I_k,
I_0
).
$$

若：

$$
\Delta_I^{(k)}
>
\Delta_I^\star,
$$

則：

$$
Escalate.
$$

也就是子 Agent 可以重新表述局部任務，但不能在沒有授權的情況下改寫根意圖。

---

# 5. Canonical State Binding

委任應綁定：

$$
S
=
(
StateRef,
Version
).
$$

若執行時：

$$
v_{current}
\neq
v_{delegated},
$$

則需要：

$$
Refresh,
Rebase,
Reject,
Escalate
$$

之一。

因此：

$$
\boxed{
\text{Delegation should bind to organizational reality, not only remembered context.}
}
$$

---

# 6. Task Contract

任務可表示為：

$$
T
=
(
Goal,
Inputs,
Dependencies,
Constraints,
SuccessCriteria,
Priority,
Deadline
).
$$

其中：

$$
SuccessCriteria
$$

決定 Agent 何時可以合法宣稱：

$$
Done.
$$

否則「繼續完成」容易退化成無界生成。

---

# 7. Capability 不等於 Authority

受任 Agent 可以宣告：

$$
CapabilityProfile(A_j).
$$

例如它可以搜尋、寫程式、讀資料庫或操作瀏覽器。

但：

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

技術上做得到，不表示治理上被允許做。

反過來，一個 Agent 也可能具有權限但能力不足，因此應能拒絕委任。

---

# 8. Capability Negotiation

委任前可比較：

$$
TaskRequirement
\leftrightarrow
AgentCapability.
$$

若：

$$
Mismatch
>
m^\star,
$$

則 Agent 可以：

$$
Reject
$$

或：

$$
CounterOffer.
$$

例如：

> 可以完成 literature review，但不能做 formal proof verification。

這比先接受後失敗更穩定。

---

# 9. Authority Envelope

定義：

$$
A
=
(
Actions,
Targets,
Scopes,
Credentials,
CommitClasses,
Expiry,
Subdelegation
).
$$

例如：

$$
\text{read},
\text{write},
\text{search},
\text{execute}
$$

已授權，但：

$$
\text{publish}
$$

沒有授權。

此時即使 Agent 可以技術上發布，也不應發布。

---

# 10. Subdelegation Monotonicity

如果：

$$
A_i
\rightarrow
A_j,
$$

預設應滿足：

$$
Auth(A_j)
\subseteq
Auth(A_i).
$$

更深一層：

$$
A^{(k+1)}
\subseteq
A^{(k)}.
$$

除非存在新的合法外部 grant。

因此：

$$
\boxed{
\text{Subdelegation}
\neq
\text{Authority Creation}.
}
$$

---

# 11. Budget Envelope

定義：

$$
B
=
(
Token,
Compute,
Money,
Time,
ToolCalls,
AgentSlots
).
$$

若 parent budget 為：

$$
B_p,
$$

child budget 預設：

$$
B_c
\le
B_p.
$$

在不可超賣的資源中，多 child 應滿足：

$$
\sum_j B_{c_j}
\le
B_p.
$$

因此：

$$
\boxed{
\text{Autonomy without budget semantics is operationally unbounded.}
}
$$

---

# 12. Risk Policy

定義：

$$
R
=
(
RiskClasses,
ForbiddenActions,
Thresholds,
SensitiveDomains,
ReversibilityRules
).
$$

若：

$$
Risk(a)
>
R^\star,
$$

則：

$$
Escalate.
$$

如此子 Agent 不必重新發明一套自己的安全治理。

---

# 13. Verification Inheritance

若 parent task 要求：

$$
V_{parent},
$$

child 不得因轉包而默默降低必要驗證要求。

對關鍵 output，應滿足：

$$
V_{child}
\succeq
V_{minimum,parent}.
$$

因此：

$$
\boxed{
\text{Subdelegation cannot silently downgrade fidelity obligations.}
}
$$

---

# 14. Output Contract

定義：

$$
O
=
(
Schema,
ArtifactType,
Status,
RequiredFields,
Lineage,
Receipts
).
$$

例如研究委任的輸出可以要求：

$$
Paper
+
ClaimMap
+
VerificationState
+
OpenGaps
+
Sources.
$$

而不是只要求：

> 給我一篇文章。

---

# 15. Checkpoint Policy

長任務需要：

$$
C
=
(
Interval,
Events,
RequiredState,
PersistTarget
).
$$

例如：

$$
BudgetUsed>50\%
$$

或：

$$
MajorClaimAdded
$$

時自動建立 checkpoint。

Checkpoint 至少保存：

$$
StateVersion,
Progress,
Artifacts,
BudgetRemaining,
OpenRisks,
NextStep.
$$

---

# 16. Escalation Policy

定義：

$$
E
=
(
Triggers,
Destination,
RequiredContext,
Urgency
).
$$

常見 trigger：

$$
Uncertainty>U^\star,
$$

$$
Risk>R^\star,
$$

$$
AuthorityInsufficient,
$$

$$
ConflictDetected,
$$

$$
HumanJudgmentRequired.
$$

---

# 17. Termination Conditions

定義：

$$
X
=
(
Success,
Failure,
BudgetExhaustion,
Timeout,
Revoke,
NoMarginalGain,
ExternalBlock
).
$$

因此：

$$
\boxed{
\text{Delegation}
\neq
\text{Infinite Continue Loop}.
}
$$

---

# 18. Provenance Requirement

定義：

$$
P
=
(
AgentID,
ModelID,
ToolUse,
SourceRefs,
ParentDelegation,
ArtifactHash,
Timestamps
).
$$

這不要求保存模型私有 chain-of-thought，而是保存足以 audit、debug、resume 與追蹤 lineage 的資訊。

---

# 19. Delegation Lifecycle

第一代生命週期：

$$
Offer
\rightarrow
Inspect
\rightarrow
Accept
\rightarrow
Execute
\rightarrow
Checkpoint
\rightarrow
Deliver
\rightarrow
Verify
\rightarrow
Commit
\rightarrow
Close.
$$

另有：

$$
Reject,
CounterOffer,
PartialAccept,
Suspend,
Escalate,
Revoke.
$$

因此委任不是一句話，而是一個有狀態的 protocol。

---

# 20. Partial Acceptance

若：

$$
T
=
\{
t_1,t_2,t_3
\},
$$

Agent 可能只接受：

$$
\{
t_1,t_2
\}.
$$

即：

$$
AcceptedScope
\subseteq
OfferedScope.
$$

剩餘任務可以重新 route，而不是逼 Agent 假裝全部完成。

---

# 21. Deliver 不等於 Commit

交付應包含：

$$
Delivery
=
(
Output,
Status,
Evidence,
VerificationState,
KnownGaps,
Receipts,
BudgetUsed
).
$$

即使：

$$
Delivered=1,
$$

也不推出：

$$
Committed=1.
$$

只有：

$$
AuthorityValid
+
VerificationPassed
+
StateCurrent
$$

時，才可以：

$$
Commit.
$$

---

# 22. 四類 Receipt

## Delegation Receipt

$$
Receipt_D
=
(
DID,
ParentDID,
Grantor,
Delegate,
Authority,
Budget,
StateVersion,
AcceptedScope,
Timestamp
).
$$

## Execution Receipt

$$
Receipt_X
=
(
DID,
Actions,
Tools,
Artifacts,
Costs,
Errors,
Retries,
CheckpointRefs
).
$$

## Verification Receipt

$$
Receipt_V
=
(
DID,
Contract,
Verifier,
Methods,
Result,
OpenIssues
).
$$

## Commit Receipt

$$
Receipt_C
=
(
DID,
Artifact,
StateVersionBefore,
StateVersionAfter,
Authority,
CommitClass,
Timestamp
).
$$

形成：

$$
Receipt_D
\rightarrow
Receipt_X
\rightarrow
Receipt_V
\rightarrow
Receipt_C.
$$

---

# 23. 身份不需要模仿 Principal

Agent A 代表某人或某公司工作，不需要對 Agent B 假裝：

> 我就是那個人。

更乾淨的是：

$$
Identity
=
DelegatedAgent
+
PrincipalRef.
$$

所以：

$$
\boxed{
\text{Representation}
\neq
\text{Identity Mimicry}.
}
$$

---

# 24. Delegation Depth

定義：

$$
d_D
=
\text{delegation chain depth}.
$$

當：

$$
d_D
$$

增加時，可能增加：

- intent drift；
- latency；
- authority ambiguity；
- state mismatch；
- verification loss。

因此可以設定：

$$
d_D
\le
d_D^\star.
$$

---

# 25. Cyclic Delegation 與 Deadlock

若：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow
A_1,
$$

可能形成 delegation loop。

因此 ancestor chain 中若已包含 target，預設應拒絕。

同樣地：

$$
A_1
$$

等待：

$$
A_2
$$

而：

$$
A_2
$$

等待：

$$
A_1
$$

則形成 deadlock。

Task graph 因此需要 cycle / deadlock detection。

---

# 26. Revocation Propagation

若 root principal 撤銷：

$$
DID_k,
$$

其 descendants：

$$
Desc(DID_k)
$$

應依 policy：

$$
Revoke
$$

或：

$$
Revalidate.
$$

因此：

$$
\boxed{
\text{Revocation must propagate along delegation lineage.}
}
$$

---

# 27. Authority Expiry

權限應具有：

$$
Expiry(A)=t_e.
$$

若：

$$
t>t_e,
$$

則：

$$
AuthorityValid=0.
$$

這可以防止 orphan Agent 長期保留舊權限。

---

# 28. Credential 與 Authority 分離

Agent 可能持有 credential。

但：

$$
CredentialPossession
\neq
CurrentDelegatedAuthority.
$$

每個 action 仍應檢查：

$$
DID
+
AuthorityEnvelope.
$$

---

# 29. Commit Class

沿用前篇 world-commit 分級：

$$
W_0,W_1,W_2,W_3,W_4.
$$

子委任預設應滿足：

$$
CommitClass_{child}
\le
CommitClass_{parent}.
$$

所以：

$$
\boxed{
\text{Subdelegation cannot silently upgrade world-impact class.}
}
$$

---

# 30. Natural Language 與 Structured Envelope 並存

本文不是主張 AI 不應使用自然語言。

自然語言非常適合：

- task description；
- critique；
- negotiation；
- uncertainty；
- explanation。

但治理欄位應結構化。

因此：

$$
\boxed{
\text{Natural Language for semantics}
+
\text{Structured Envelope for governance}.
}
$$

---

# 31. 最小 Protocol Core

第一版不必一開始就非常巨大。

最小核心可以是：

$$
Core
=
(
DID,
RID,
Task,
StateRef,
Authority,
Budget,
Verification,
Stop,
Output
).
$$

其他欄位可逐步擴充。

---

# 32. Web AI 與 Browser Delegation

如果本地 AI Manager 要操作另一個網頁 AI：

$$
Agent_{manager}
\rightarrow
Browser
\rightarrow
WebAI.
$$

WebAI 不一定懂完整 protocol。

此時：

$$
StructuredDelegation
\rightarrow
RenderedPrompt.
$$

但本地 manager 仍保存 canonical envelope。

因此：

$$
\boxed{
\text{Chat Window}
\neq
\text{Canonical Delegation Source}.
}
$$

網頁對話只是一個 transport / rendering view。

---

# 33. Protocol Degradation

從 structured envelope 轉成單純 prompt 時，會有資訊損失。

定義：

$$
D_P
=
Loss(
StructuredEnvelope
\rightarrow
TargetInterface
).
$$

如果：

$$
D_P>D_P^\star,
$$

高風險委任應拒絕或要求人工介入。

這對 Web AI 特別重要。

---

# 34. Handoff Quality

定義：

$$
Q_H
=
f(
IntentPreservation,
StateFreshness,
AuthorityClarity,
VerificationContinuity,
OutputCompleteness
).
$$

若：

$$
Q_H<Q_H^\star,
$$

handoff 不應直接進下一階段。

---

# 35. Delegation Efficiency

定義：

$$
\eta_D
=
\frac{
V_{\mathrm{verified\ delegated\ output}}
}{
C_{\mathrm{delegation}}
+
C_{\mathrm{execution}}
+
C_{\mathrm{verification}}
+\epsilon
}.
$$

因此：

$$
\boxed{
\text{More delegation layers}
\neq
\text{More advanced organization}.
}
$$

如果 overhead 太高：

$$
\eta_D\downarrow.
$$

---

# 36. Delegation Debt

定義：

$$
D_{del}
=
D_{open}
+
D_{orphan}
+
D_{stale}
+
D_{authority}
+
D_{receipt}.
$$

包括：

- 未閉合委任；
- orphan child；
- stale-state delegation；
- authority ambiguity；
- receipt 缺失。

因此 runtime 應維護：

$$
\mathcal D_{open}.
$$

---

# 37. 可檢驗命題

**Structured-Handoff Advantage**

結構化 Delegation Envelope 應比純自然語言 handoff 更能降低 intent、authority 與 verification loss。

**State-Version Binding Advantage**

綁定 canonical state version 應降低 stale-state execution。

**Subdelegation Monotonicity**

authority、budget 與 commit class 不擴張，應降低多層委任中的權限漂移。

**Receipt Completeness**

完整 receipt chain 應比單純聊天紀錄更容易 audit、resume 與 debug。

**Capability Negotiation Efficiency**

執行前 capability negotiation 應降低不可完成任務的浪費。

**Protocol Degradation Risk**

當 structured envelope 被壓成只剩 prompt 時，風險應隨 protocol loss 增加。

---

# 38. 第一代實驗設計

## Prompt Handoff vs Delegation Envelope

比較：

$$
NaturalLanguageOnly
$$

與：

$$
StructuredEnvelope.
$$

測量：

$$
IntentDrift,
AuthorityError,
StateMismatch,
VerificationLoss,
CompletionQuality.
$$

## Multi-Hop Delegation

測試：

$$
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow
A_4.
$$

觀察：

$$
Q_H
$$

隨 depth 的變化。

## Authority Laundering Injection

故意要求 child 擴大 authority。

預期：

$$
Denied.
$$

## Stale-State Injection

在委任後更新 canonical state，測試 child 是否偵測版本不一致。

## Revocation Propagation

在多層委任中撤銷 parent DID，測試 descendants 是否停止。

## Browser-WebAI Test

將 structured delegation 渲染成網頁聊天 prompt，測量：

$$
D_P.
$$

---

# 39. 與前六篇的閉合

目前系列形成：

$$
\boxed{
\text{Operator Exit}
\rightarrow
\text{Delegated Sovereignty}
\rightarrow
\text{Dynamic Topology}
\rightarrow
\text{Shared State}
\rightarrow
\text{Research Environment}
\rightarrow
\text{Verification Contract}
\rightarrow
\text{Cross-AI Delegation}.
}
$$

第 6 篇解決：

> 每種 research object 要接受什麼驗證？

本篇則解決：

> 這些任務、權限與驗證義務如何完整地從一個 AI 傳給下一個 AI？

---

# 40. 與下一篇的接口

只要 AI-to-AI delegation 已經能夠：

- 傳遞 authority；
- 保存 state；
- 繼承 verification；
- 保留 provenance；
- 支援 revocation；
- 區分 commit class；

下一步就可以讓某些 Agent 走出內部研究域，成為：

$$
\boxed{
\text{Persistent Public AI Actor}.
}
$$

因此第 8 篇將處理：

# 公共 AI 行動者：自主網站、社群、影音與對外互動

核心問題將是：

> AI 如何在公開世界持續行動，又不把身份、責任、平台規則、聲譽與授權搞混？

---

# 41. 理論限制

第一，不同 Agent runtime 可能沒有共同 schema，因此需要 adapter。

第二，跨公司、跨平台 Agent 的 trust model 更複雜，本文尚未完整處理 authentication、attestation 與 adversarial delegate。

第三，部分平台仍只有自然語言或 GUI 介面，因此 protocol degradation 不可能完全避免。

第四，capability self-report 可能不準，需要 calibration。

第五，不同工具的 budget 與 authority 語義不同。

第六，多層 delegation 會增加 latency 與 coordination overhead，因此不能無限轉包。

第七，本文尚未固定 wire format；第 10 篇 reference architecture 將進一步壓成可實作 schema。

---

# 42. 結論

AI-to-AI 協作真正的下一步，不是讓兩個 AI 更會聊天。

真正需要的是：

$$
\boxed{
\text{A governable delegation protocol.}
}
$$

因此：

$$
\boxed{
\text{Prompt}
\rightarrow
\text{Delegation Envelope}
}
$$

代表重要質變。

一個完整委任應能回答：

- 任務從哪裡來？
- root intent 是什麼？
- canonical state 是哪一版？
- Agent 有哪些 authority？
- budget 是多少？
- 哪些 verification 不能省？
- 哪些 action 可以 commit？
- 何時停止？
- 何時 escalation？
- 是否允許再委任？
- 最後如何證明真正做過？

因此：

$$
\boxed{
\text{AI-to-AI Delegation}
=
\text{Intent}
+
\text{State}
+
\text{Authority}
+
\text{Budget}
+
\text{Verification}
+
\text{Receipts}
+
\text{Revocation}.
}
$$

當這些元素成立後，AI 互動才從：

$$
\text{Conversation}
$$

真正提升為：

$$
\boxed{
\text{Organizational Coordination}.
}
$$

---

# 符號表

| 符號 | 定義 |
|---|---|
| $\mathfrak D_{i\rightarrow j}$ | Agent Delegation Envelope |
| $DID$ | Delegation ID |
| $RID$ | Root Intent / Root Delegation ID |
| $I$ | Intent Specification |
| $S$ | Canonical State Reference |
| $T$ | Task Contract |
| $A$ | Authority Envelope |
| $B$ | Budget Envelope |
| $R$ | Risk Policy |
| $V$ | Verification Contract |
| $O$ | Output Contract |
| $C$ | Checkpoint Policy |
| $E$ | Escalation Policy |
| $X$ | Termination Conditions |
| $P$ | Provenance Requirements |
| $Q_H$ | Handoff Quality |
| $D_P$ | Protocol Degradation |
| $D_{del}$ | Delegation Debt |
| $Receipt_D$ | Delegation Receipt |
| $Receipt_X$ | Execution Receipt |
| $Receipt_V$ | Verification Receipt |
| $Receipt_C$ | Commit Receipt |

---

# 版本紀錄

- **v0.1 / 2026-08-21**：建立 Agent Delegation Envelope、Delegation Lifecycle、Capability Negotiation、Authority / Budget Inheritance、Subdelegation Monotonicity、State-Version Binding、四類 Receipt、Protocol Degradation、Browser-WebAI Delegation 與第一代實驗設計。
