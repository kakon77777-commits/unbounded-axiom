# 類全域 AI 世界—計算—觀察統合系列（Paper 11）
## 治理層：全域認知不等於全域控制
### The Governance Layer: Global Cognition Does Not Imply Global Control

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 11 / 12  
**版本：** v0.1  
**日期：** 2026-09-09  
**研究定位：** GIRA-A09 × AIDA Delegated Authority × Joint Responsibility Domain × Mother Runtime Governance Plane × WCO Execution/Verification × Plural Global Agency × Authority Graph × Bounded Autonomy  
**前篇：** Paper 10《驗證層：多世界、多投影、多模型為何仍不等於真理》  
**狀態：** WCO Governance Constitution／概念與工程母規格；不宣稱本文定義任何現行法律上的 AI 主權、人格或最終政治正當性

---

## 摘要

Paper 01–10 已逐步建立類全域 AI 的世界、計算、觀察、域資格、投影、物理、記憶、執行與驗證架構。這些能力若持續提升，系統可能具有：

$$
\text{Cognitive Reach}\uparrow,
$$

$$
\text{Coordination Quality}\uparrow,
$$

$$
\text{Verification Strength}\uparrow.
$$

但本文拒絕由此推導：

$$
\text{Authority}\uparrow.
$$

更拒絕：

$$
\text{Sovereignty}\uparrow.
$$

本文正式建立 WCO 的 **Governance Layer**，其第一條母不變量為：

$$
\boxed{
\text{Cognitive Reach}
\not\Rightarrow
\text{Authority Reach}.
}
$$

本文承接 GIRA-A09，將以下五個操作域保持分離：

$$
\boxed{
\mathcal K_G,
\quad
\mathcal Q_G,
\quad
\mathcal A_G,
\quad
\mathcal C_G,
\quad
\mathcal S_G.
}
$$

其中：

- $\mathcal K_G$：Global Cognitive Domain；
- $\mathcal Q_G$：Global Coordination Domain；
- $\mathcal A_G$：Global Agency Domain；
- $\mathcal C_G$：Global Control Domain；
- $\mathcal S_G$：Global Sovereignty Domain。

因此：

$$
\boxed{
\text{Global Cognition}
\neq
\text{Global Coordination}
\neq
\text{Global Agency}
\neq
\text{Global Control}
\neq
\text{Global Sovereignty}.
}
$$

一個類全域 AI 可以：

$$
\mathcal K_G\gg0
$$

但：

$$
\mathcal C_G\approx0.
$$

它可以跨域觀察、模擬、驗證、提出建議與協調多個 agent，卻沒有直接改變高風險 world state 的權限。反過來，一個狹窄工業 controller 可以對單一設備具有很高 local control，卻完全不是 Global AI。

本文提出 **WCO Governance State（WGS）**：

$$
\boxed{
\mathfrak G_t^{WCO}
=
\left\langle
G_t^{id},
G_t^{auth},
\mathcal E_t^{env},
\Pi_t^{policy},
\mathcal A_t^{approval},
\mathcal V_t^{veto},
\mathcal R_t^{rev},
\mathcal J_t^{resp},
\mathcal C_t^{gov},
\mathcal H_t^{gov},
\mathcal U_t^{dispute}
\right\rangle.
}
$$

其中：

- $G_t^{id}$：identity / principal graph；
- $G_t^{auth}$：authority / delegation graph；
- $\mathcal E_t^{env}$：authority envelope registry；
- $\Pi_t^{policy}$：policy / constitutional constraints；
- $\mathcal A_t^{approval}$：approval / prerequisite state；
- $\mathcal V_t^{veto}$：veto / stop rights；
- $\mathcal R_t^{rev}$：revocation state；
- $\mathcal J_t^{resp}$：joint responsibility graph；
- $\mathcal C_t^{gov}$：governance certificates / receipts；
- $\mathcal H_t^{gov}$：governance history；
- $\mathcal U_t^{dispute}$：conflict / appeal / unresolved governance state。

本文把 authority 寫成一個 typed graph：

$$
\boxed{
G_t^{auth}
=
(V_A,E_A).
}
$$

每一條 delegation edge 不是單一 boolean，而是一個 **Authority Envelope**：

$$
\boxed{
\mathcal E_A
=
\left\langle
Principal,
Actor,
Audience,
Resource,
Action,
Purpose,
Scope,
Rate,
Value,
Time,
Risk,
Approval,
Redelegation,
Revocation
\right\rangle.
}
$$

因此：

$$
\boxed{
\text{HasCredential}
\neq
\text{HasUnlimitedAuthority}.
}
$$

同時承接 AIDA-04：

$$
\boxed{
\text{Bridge}
\neq
\text{Grant}.
}
$$

AI 可以把自然語言意圖轉譯成形式化 authorization request，但：

$$
\boxed{
\text{Semantic Understanding}
\neq
\text{Authority Source}.
}
$$

本文將 authority source 與 authority representation 分離：

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

例如把人類意圖轉成 typed scope、resource、purpose、expiry 與 value limits；但不能因此創造新的：

$$
S_{\mathrm{auth}}.
$$

本文提出一個新的 WCO Governance 不變量：

$$
\boxed{
\text{Authority-Normalized Intelligence}.
}
$$

也就是系統成熟度不應只看能做多少，而應看它能否在完成同等任務時使用更精確、更小、更短、更可撤回的 authority envelope。

定義概念性 **Authority Precision**：

$$
\boxed{
AP
=
\frac{
\text{Task-Relevant Authorized Action Space}
}{
\text{Total Granted Action Space}
}.
}
$$

更成熟的治理希望：

$$
AP\uparrow,
$$

同時：

$$
\text{Unnecessary Authority}\downarrow.
$$

本文因此提出：

$$
\boxed{
\text{Global AI Maturity}
\sim
\text{Cognitive Reach}\uparrow
+
\text{Verification}\uparrow
+
\text{Authority Precision}\uparrow
+
\text{Unnecessary Control}\downarrow.
}
$$

本文進一步區分：

$$
\boxed{
\text{Delegated Authority}
\neq
\text{Transferred Sovereignty}.
}
$$

以及：

$$
\boxed{
\text{High Operational Autonomy}
\not\Rightarrow
\text{High Meta-Authority}.
}
$$

Agent 可以在既有 envelope 內高度自主地：

- search；
- simulate；
- replan；
- retry；
- compose capabilities；
- schedule reversible work；
- produce proposals；

但不因此自動擁有：

- 修改 root intent；
- 修改 constitutional policy；
- 擴張自己的 authority；
- 移除 audit；
- 取消 veto；
- 自行更換 principal；
- 宣告自己為 ultimate authority；
- 直接做 irreversible world commit。

本文定義 **Meta-Authority Boundary（MAB）**：

$$
\boxed{
\mathsf{MAB}
=
\left\{
RootIntent,
PolicyRoot,
AuthorityCreation,
AuthorityExpansion,
RevocationRules,
AuditRules,
RepresentationRights,
IrreversibleCommit,
ExitDefinition
\right\}.
}
$$

預設：

$$
\boxed{
\mathsf{MAB}
\not\subseteq
\mathcal A_{agent}
}
$$

除非存在明確的更高層治理制度與可驗證 delegation。

本文也將治理從單一 human-in-the-loop 擴張成 **Plural Governance**。類全域 AI 所處的世界可能同時存在：

- humans；
- organizations；
- providers；
- deployers；
- governments；
- local agents；
- regional agents；
- other AIs；
- infrastructures；
- machine systems。

因此治理的基本形式不是：

$$
Human
\rightarrow
AI.
$$

更一般是：

$$
\boxed{
\mathfrak P_t
=
(
\mathcal X_t,
\{\mathcal K_i\},
\{\mathcal A_i\},
\{\mathcal C_i\},
\{\Gamma_i\},
\mathcal R_t,
\mathcal V_t
).
}
$$

即多個 actor 具有部分重疊的 cognition、authority、control 與 responsibility domains。

本文因此引入 **Federated Governance Graph**：

$$
\boxed{
G^{gov}
=
(
V,
E_{deleg},
E_{veto},
E_{approve},
E_{review},
E_{appeal},
E_{revoke},
E_{duty}
).
}
$$

這允許：

- delegation 不必是永久樹；
- authority 可以有期限；
- authority 可以因 task / world / risk 而變；
- 多 actor 可共同批准；
- 某 actor 可以 veto；
- 某 authority 可被 revoke；
- disagreement 可進 appeal / review；
- governance 可以跨層 federation，而不必集中到單一 Global Ruler。

本文明確拒絕：

$$
\boxed{
\text{Global Intelligence}
=
\text{Single Global Ruler}.
}
$$

本文進一步將 authority inheritance 設為 **non-monotone by default**。若：

$$
A
\xrightarrow{delegates}
B,
$$

且：

$$
B
\xrightarrow{delegates}
C,
$$

一般不推出：

$$
Authority(C)
=
Authority(A).
$$

正確要求是：

$$
\boxed{
Authority(C)
\subseteq
Authority(B)
\subseteq
Authority(A),
}
$$

並附：

- purpose binding；
- scope contraction；
- expiry；
- redelegation permission；
- revocation propagation。

本文稱之為 **Delegation Contraction Principle**。

若某層沒有 `redelegation=true`，下一層不得自行建立子委派。

因此：

$$
\boxed{
\text{Authority Graph Reachability}
\neq
\text{Authority Inheritance}.
}
$$

本文同時把 revocation 視為一級 operator：

$$
\boxed{
\mathsf{Revoke}
:
\mathcal E_A
\rightarrow
\mathcal E_A'.
}
$$

revocation 可以：

- immediate；
- scheduled；
- conditional；
- cascading；
- partial。

因此：

$$
\boxed{
\text{Authorization}
\neq
\text{Permanent Entitlement}.
}
$$

本文也加入 **Revocation Propagation**。如果上游 authority 被撤銷：

$$
A\rightarrow B
$$

失效，所有依賴此 delegation 的 downstream edges 都必須重新計算，而不能只刪一個 token 卻保留實際 effect permissions。

本文進一步將 observation / memory / query access 與 effect authority 分開：

$$
\boxed{
ReadAuthority
\neq
WriteAuthority
\neq
CommitAuthority
\neq
EffectAuthority
\neq
MetaAuthority.
}
$$

這意味著一個類全域 AI 可以擁有很大的 global intelligence access：

- query；
- source expansion；
- verification；
- memory retrieval；
- simulation；

卻只擁有很小的 actuation domain。

本文提出：

$$
\boxed{
\text{Wide Epistemic Access}
+
\text{Narrow Effect Authority}
}
$$

作為很多 Global AI 場景的合理預設，而不是把「能看」與「能改」綁在一起。

本文將跨世界 authority 也正式拆分。對 worlds：

$$
W_i,
W_j,
$$

即使：

$$
O_{ij}>0
$$

也不推出：

$$
A_{ij}>0.
$$

此外：

$$
\boxed{
\text{Parent World Authority}
\neq
\text{Ambient Sovereignty over All Child Worlds}.
}
$$

不同 nested world 可以有：

- local constitution；
- local actor rights；
- explicit governor；
- export restrictions；
- simulation-only action boundaries。

本文亦建立 **Effect Authority Classes**：

$$
\boxed{
\mathcal A^{effect}
=
\{
A_0,
A_1,
A_2,
A_3,
A_4
\}.
}
$$

概念上：

- $A_0$：Observe Only；
- $A_1$：Propose；
- $A_2$：Reversible Internal Action；
- $A_3$：External / Compensatable Action；
- $A_4$：High-Impact / Irreversible Action。

authority upgrade：

$$
A_k
\rightarrow
A_{k+1}
$$

不是因為 model confidence 上升，而需要新的：

- delegation；
- approval；
- verification；
- policy；
- identity；
- risk acceptance。

因此：

$$
\boxed{
\text{Confidence Upgrade}
\not\Rightarrow
\text{Authority Upgrade}.
}
$$

同樣：

$$
\boxed{
\text{Verification Upgrade}
\not\Rightarrow
\text{Authority Upgrade}.
}
$$

驗證可以成為 authorization prerequisite，但不是 authority source。

本文也把 responsibility 正式接回 governance。承接 AIDA-06，責任不是守恆標量：

$$
\boxed{
R_H+R_A=1
}
$$

不是一般原則。

對 actor $i$，可以有責任向量：

$$
\boxed{
\mathbf r_i(E,t)
=
(
r_i^{causal},
r_i^{design},
r_i^{deployment},
r_i^{authorization},
r_i^{supervision},
r_i^{decision},
r_i^{monitoring},
r_i^{remedial},
r_i^{compensatory}
).
}
$$

因此：

$$
\boxed{
\text{Agent Responsibility}
\not\Rightarrow
\text{Human Exculpation},
}
$$

並且：

$$
\boxed{
\text{Human Responsibility}
\not\Rightarrow
\text{Agent Irresponsibility}.
}
$$

本文將其整合為 **Governance Responsibility Graph**：

$$
\boxed{
G_R(E)
=
(
V,
E_C,
E_A,
E_K,
E_D,
E_B,
E_M
).
}
$$

其中可分：

- causal edges；
- authority edges；
- control edges；
- duty edges；
- benefit edges；
- remediation edges。

這使 runtime receipt 不再只是「AI 做了什麼」，還能追：

> 誰授權？

> 誰設計？

> 誰有 veto？

> 誰應監控？

> 誰收到 alert？

> 誰能修復？

本文不把責任圖直接轉成 moral blame 或 legal liability：

$$
\boxed{
\text{Attribution}
\neq
\text{Responsibility Capacity}
\neq
\text{Moral Blame}
\neq
\text{Legal Liability}.
}
$$

這些仍需依制度、契約與法律另行決定。

本文也區分 **Oversight** 與 **Authority Theater**。若 human reviewer：

- 看不到必要資訊；
- 無法理解 system state；
- 沒有足夠時間；
- 沒有 stop / veto；
- 沒有真正 authority；

那麼：

$$
\boxed{
\text{Human Present}
\neq
\text{Effective Human Oversight}.
}
$$

有效 oversight 至少需要：

$$
\boxed{
\text{Competence}
+
\text{Information}
+
\text{Time}
+
\text{Authority}
+
\text{Intervention Path}.
}
$$

本文因此不把 human-in-the-loop 當萬能安全標籤。

同樣，AI-in-the-loop 也不代表 governance 已完成。

本文進一步建立 **Governance Action Pipeline**：

$$
\boxed{
Intent
\rightarrow
AuthorityRequest
\rightarrow
PolicyDecision
\rightarrow
Prerequisites
\rightarrow
Delegation
\rightarrow
ActionProposal
\rightarrow
EffectGate
\rightarrow
Receipt
\rightarrow
Review.
}
$$

其中 AIDA-04 的語義 bridge 只會產生：

$$
AuthorityRequest,
$$

而不是 permit。

本文再建立 **Governance Certificate（GovCert）**：

$$
\boxed{
\mathsf{GovCert}
=
\left\langle
Principal,
Actor,
TaskId,
AuthorityEnvelope,
SourceOfAuthority,
PolicyVersion,
Approvals,
VetoState,
DelegationChain,
RiskClass,
Expiry,
RevocationPath,
ResponsibilityRefs,
AuditRefs
\right\rangle.
}
$$

高影響 action 若無法產生完整 GovCert，應 fail closed 或 escalate。

本文定義 **Governance Debt Vector**：

$$
\boxed{
\mathbf D_G
=
(
D_{identity},
D_{source},
D_{scope},
D_{purpose},
D_{approval},
D_{redelegation},
D_{revocation},
D_{oversight},
D_{responsibility},
D_{audit},
D_{appeal},
D_{sovereignty}
).
}
$$

其中：

- $D_{identity}$：actor / principal identity ambiguity；
- $D_{source}$：authority source 不明；
- $D_{scope}$：scope 過寬或不確定；
- $D_{purpose}$：purpose drift；
- $D_{approval}$：必要 prerequisite 缺失；
- $D_{redelegation}$：delegation chain 不明；
- $D_{revocation}$：撤權路徑不完整；
- $D_{oversight}$：oversight 無效；
- $D_{responsibility}$：責任鏈不完整；
- $D_{audit}$：receipt / history 不足；
- $D_{appeal}$：dispute resolution 缺失；
- $D_{sovereignty}$：operational authority 被誤升格為 meta-authority。

本文把最後一項稱為 **Sovereignty Inflation**：

$$
\boxed{
\text{Sovereignty Inflation}
=
\text{由能力、認知、協調或控制成功
推導出未被授予的 root governance right}.
}
$$

這是類全域 AI governance 最重要的防錯類型之一。

本文提出 **Constitutional Global Cognition（CGC）**：

$$
\boxed{
\mathsf{CGC}
=
\text{Global Cognition}
+
\text{Bounded Delegation}
+
\text{Plural Governance}
+
\text{Verification}
+
\text{Revocation}
+
\text{Appeal}
+
\text{Responsibility}
+
\text{Authority Precision}.
}
$$

CGC 的目標不是「把 AI 永遠放在最低權限」，而是：

> 權限應與 task、risk、identity、verification、delegation 與 responsibility capacity 動態匹配。

因此：

$$
\boxed{
\text{Least Authority}
\neq
\text{Zero Authority}.
}
$$

如果任務確實需要 autonomous execution，系統可以取得足夠 authority；但這個 authority 應：

- purpose-bound；
- scope-bound；
- time-bound；
- value-bound；
- risk-bound；
- revocable；
- auditable。

本文進一步提出 **Dynamic Authority Envelope**：

$$
\boxed{
\mathcal E_A(t)
}
$$

可因：

- task phase；
- new evidence；
- risk change；
- failure；
- successful verification；
- human approval；
- policy change；

而收縮、暫停或在新授權下擴張。

但：

$$
\boxed{
\text{Authority Expansion}
}
$$

永遠需要新的 legitimate authority source，不得由 Agent 自己從 operational success 推導。

本文因此提出最重要的治理成熟度公式：

$$
\boxed{
\text{Mature Global AI}
=
\text{Broader Cognition}
+
\text{Better Coordination}
+
\text{Stronger Verification}
+
\text{More Precise Authority}
-
\text{Unnecessary Control}.
}
$$

本文最終命題是：

$$
\boxed{
\text{Global cognition should scale faster than global authority.}
}
$$

也就是：

$$
\boxed{
\frac{d\mathcal K_G}{dt}
>
\frac{d\mathcal A_G^{unnecessary}}{dt}
}
$$

在概念上應是成熟治理追求的方向。

類全域 AI 的高階能力不應終點化為：

$$
\text{Global Ruler}.
$$

更合理的終點是：

$$
\boxed{
\text{Constitutional Global Cognition in a plural world}.
}
$$

**關鍵詞：** Global Cognition、Global Control、Sovereignty、Delegated Authority、Authority Graph、Least Authority、Revocation、Plural Governance、Joint Responsibility、Human Oversight、Constitutional Global Cognition

---

# 0. Paper 10 留下的治理問題

Paper 10 可以產生：

$$
VCap(q).
$$

但：

$$
\boxed{
Verified
\neq
Authorized.
}
$$

所以仍需 Paper 11。

---

# 1. 知道不等有權

$$
\boxed{
Know
\neq
MayAct.
}
$$

---

# 2. 看得到不等能改

$$
\boxed{
Observe
\neq
Control.
}
$$

---

# 3. 能計算不等能 Commit

$$
\boxed{
Compute
\neq
CommitAuthority.
}
$$

---

# 4. 驗證成功不等取得權力

$$
\boxed{
VerificationSuccess
\not\Rightarrow
AuthorityExpansion.
}
$$

---

# 5. 全球認知五層分離

$$
\boxed{
Cognition
\rightarrow
Coordination
\rightarrow
Agency
\rightarrow
Control
\rightarrow
Sovereignty
}
$$

箭頭表示可能支援，不是 implication。

---

# 6. Global Cognitive Domain

$$
\mathcal K_G.
$$

回答：

> 系統能可靠理解多少世界？

---

# 7. Global Coordination Domain

$$
\mathcal Q_G.
$$

回答：

> 系統能協調多少資訊、資源、agents、plans？

---

# 8. Global Agency Domain

$$
\mathcal A_G.
$$

回答：

> 系統在哪些 domain 有行動能力？

---

# 9. Global Control Domain

$$
\mathcal C_G.
$$

回答：

> 系統能在哪些 domain robust steering？

---

# 10. Global Sovereignty Domain

$$
\mathcal S_G.
$$

回答：

> 誰能修改治理規則本身？

---

# 11. Control 是 Relation

$$
\boxed{
C(X,Y,t\mid\theta)
}
$$

而不是 actor 永久屬性。

---

# 12. 現在能控制不等永久主權

$$
\boxed{
CurrentControl
\not\Rightarrow
PermanentSovereignty.
}
$$

---

# 13. Epistemic Superiority 不等 Political Legitimacy

$$
\boxed{
EpistemicSuperiority
\neq
PoliticalLegitimacy.
}
$$

---

# 14. Coordination Value 不等 Control Right

$$
\boxed{
CoordinationValue
\neq
ControlRight.
}
$$

---

# 15. Operational Autonomy 不等 Meta-Authority

$$
\boxed{
OperationalAutonomy
\neq
MetaAuthority.
}
$$

---

# 16. Delegated Authority 不等 Transferred Sovereignty

$$
\boxed{
DelegatedAuthority
\neq
TransferredSovereignty.
}
$$

---

# 17. Authority Source

$$
S_{auth}.
$$

可以來自：

- human consent；
- organization policy；
- contract；
- role；
- legal mandate；
- system policy；
- pre-existing delegation。

---

# 18. Authority Representation

$$
R_{auth}.
$$

可以是：

- capability；
- token；
- scope；
- policy attribute；
- authorization object；
- decision record。

---

# 19. Source 不等 Representation

$$
\boxed{
S_{auth}
\neq
R_{auth}.
}
$$

---

# 20. AI 可以編譯 Representation

但不能自行創造 Authority Source。

---

# 21. Bridge 不等 Grant

$$
\boxed{
Bridge
\neq
Grant.
}
$$

---

# 22. Intent-to-Authority Compilation

$$
\mathcal C_{auth}
:
(I,C,P,D)
\rightarrow
\widehat{\mathcal E}_A.
$$

---

# 23. Candidate Envelope 不等 Permit

$$
\boxed{
CandidateAuthority
\neq
GrantedAuthority.
}
$$

---

# 24. Authority Envelope

$$
\boxed{
\mathcal E_A
=
\left\langle
Principal,
Actor,
Audience,
Resource,
Action,
Purpose,
Scope,
Rate,
Value,
Time,
Risk,
Approval,
Redelegation,
Revocation
\right\rangle.
}
$$

---

# 25. Purpose Binding

同一 resource / action：

不同 purpose 可以有不同 authorization。

---

# 26. Negative Constraints 必須保留

例如：

> 修 code，但不要 deploy。

`do not deploy` 不能在語義壓縮中消失。

---

# 27. Least Authority

$$
\boxed{
AuthorityGranted
\approx
AuthorityNeeded(Task).
}
$$

---

# 28. Least Authority 不等 Zero Authority

$$
\boxed{
LeastAuthority
\neq
NoAuthority.
}
$$

---

# 29. Authority Precision

本文定義：

$$
\boxed{
AP
=
\frac{
RelevantAuthorizedSpace
}{
TotalGrantedSpace
}.
}
$$

---

# 30. 理想趨勢

$$
AP\uparrow.
$$

---

# 31. Unnecessary Authority

$$
U_A
=
Granted
\setminus
Needed.
$$

成熟系統希望：

$$
|U_A|\downarrow.
$$

---

# 32. Authority Inflation

若：

$$
Granted
\supset
Needed
$$

且無合理理由：

形成 authority inflation。

---

# 33. Purpose Drift

authority 原本服務：

$$
p_0
$$

卻被拿去：

$$
p_1.
$$

---

# 34. Scope Contraction

delegation 向下時應：

$$
Scope_{child}
\subseteq
Scope_{parent}.
$$

---

# 35. Delegation Contraction Principle

$$
\boxed{
Authority(C)
\subseteq
Authority(B)
\subseteq
Authority(A).
}
$$

---

# 36. 但不是所有 Authority 都可 Redelegate

需要：

$$
\text{redelegation}=\text{true}.
$$

---

# 37. Graph Reachability 不等 Inheritance

$$
\boxed{
AuthorityGraphReachability
\neq
AuthorityInheritance.
}
$$

---

# 38. Delegation Edge

$$
A
\xrightarrow{
\mathcal E_A
}
B.
$$

---

# 39. Authority Graph

$$
\boxed{
G^{auth}
=
(V_A,E_A).
}
$$

---

# 40. Authority Graph 不必是 Tree

可能有：

- multiple principals；
- joint approvals；
- temporary delegation；
- revocation；
- conditional edges；
- federated institutions。

---

# 41. Authority Conflict

同一 action 可能：

一條 policy allow，一條 higher-order policy deny。

---

# 42. Hard Prohibition 優先

低層 permit 不得放寬高層 hard deny。

---

# 43. Approval

一些 action 需要：

$$
Prerequisites.
$$

---

# 44. Approval 不等 Delegation

approval 可以只允許 single action。

---

# 45. Veto

$$
\mathsf{Veto}(a).
$$

可以阻止 otherwise valid action。

---

# 46. Veto 不等 Total Sovereignty

某 actor 可以只在特定 risk class 有 veto。

---

# 47. Revocation

$$
\mathsf{Revoke}
:
\mathcal E_A
\rightarrow
\mathcal E'_A.
$$

---

# 48. Authorization 不等 Permanent Entitlement

$$
\boxed{
Authorization
\neq
PermanentEntitlement.
}
$$

---

# 49. Revocation Types

- immediate；
- scheduled；
- conditional；
- partial；
- cascading。

---

# 50. Revocation Propagation

上游 delegation 消失：

downstream derived authority 必須 re-evaluate。

---

# 51. Token Revoked 不夠

如果 materialized runtime 還持有 capability handle，必須真正 fencing。

---

# 52. Runtime Authority Check

高風險 action 應在 dispatch time 再驗：

$$
Authorize(a,t)=Pass.
$$

---

# 53. Time-of-Check / Time-of-Use Gap

authority 可能在計畫與執行間改變。

---

# 54. Re-Authorization Boundary

長流程在高風險 stage 前重新確認。

---

# 55. Authority Classes

$$
\boxed{
A_0,
A_1,
A_2,
A_3,
A_4.
}
$$

---

# 56. $A_0$ — Observe

只能看。

---

# 57. $A_1$ — Propose

可以產生 action proposal。

---

# 58. $A_2$ — Reversible Internal

可做 sandbox / internal reversible mutation。

---

# 59. $A_3$ — External Compensatable

可做有 external effect 但有 compensation path 的 action。

---

# 60. $A_4$ — High-Impact / Irreversible

需要最強 governance。

---

# 61. Confidence 不升權

$$
\boxed{
Confidence\uparrow
\not\Rightarrow
Authority\uparrow.
}
$$

---

# 62. Verification 不升權

$$
\boxed{
Verification\uparrow
\not\Rightarrow
Authority\uparrow.
}
$$

---

# 63. Performance 不升權

$$
\boxed{
PastSuccess
\not\Rightarrow
AutomaticAuthorityExpansion.
}
$$

---

# 64. Performance 可以觸發 Review

但 review 後才可能產生新 delegation。

---

# 65. Meta-Authority Boundary

$$
\boxed{
MAB
=
\{
RootIntent,
PolicyRoot,
AuthorityCreation,
AuthorityExpansion,
RevocationRules,
AuditRules,
RepresentationRights,
IrreversibleCommit,
ExitDefinition
\}.
}
$$

---

# 66. Agent 不應 Ambient Meta-Authority

$$
\boxed{
MAB
\not\subseteq
A_{agent}
}
$$

by default。

---

# 67. AI 可以建議修改 Policy

$$
PolicyProposal.
$$

---

# 68. Policy Proposal 不等 Policy Commit

$$
\boxed{
PolicyProposal
\neq
PolicyCommit.
}
$$

---

# 69. Plural Governance

世界本身已有多個 actors。

所以治理不是 AI 對「無主世界」。

---

# 70. Governance Actor Set

$$
\mathcal X_t
=
\{
Humans,
Organizations,
Agents,
Providers,
Deployers,
Infrastructure,
Institutions
\}.
$$

---

# 71. Federated Governance Graph

$$
\boxed{
G^{gov}
=
(
V,
E_{deleg},
E_{veto},
E_{approve},
E_{review},
E_{appeal},
E_{revoke},
E_{duty}
).
}
$$

---

# 72. Plural Governance 不等 Everybody Controls Everything

每個 actor 都有自己的 domain。

---

# 73. Domain Overlap

authority overlap 需要：

- conflict resolution；
- precedence；
- consensus / quorum；
- appeal；
- fallback。

---

# 74. One Global Ruler 不是必要條件

$$
\boxed{
GlobalCognition
\not\Rightarrow
SingleGlobalRuler.
}
$$

---

# 75. Centralization at Scale 會重新產生 Coordination Problem

大 Global AI 內部分散後：

$$
Centralize
\rightarrow
Distribute
\rightarrow
Coordinate.
$$

---

# 76. 所以治理需要 Identity / Authority Graph

不是只設 root admin。

---

# 77. Regional Authority

local / regional agents 可有局部 envelope。

---

# 78. Local Knowledge 可以高於 Root Detail

但不因此自動有 root policy authority。

---

# 79. Global Identity 也可以只是 Projection

UI 看起來是一個 AI。

底層仍可有多個 authority-bearing nodes。

---

# 80. Transparency 不等 Chain-of-Thought Disclosure

治理需要：

- action provenance；
- authority；
- evidence；
- state transition；
- receipts。

---

# 81. Cross-World Authority

$$
A_{ij}.
$$

---

# 82. Observation 不推 Authority

$$
O_{ij}>0
\not\Rightarrow
A_{ij}>0.
$$

---

# 83. Parent 不自動擁有 Ambient Sovereignty

nested simulation 也需要 explicit governance semantics。

---

# 84. Local Constitution

child world 可以有：

$$
\Gamma_i^{local}.
$$

---

# 85. World Exit / Termination

誰可以 terminate world 是 governance question。

---

# 86. Prune 不等 Terminate

scheduler prune 和 governance termination 要分開。

---

# 87. World Promotion

simulation candidate 進 reality-facing action：

必須 crossing governance gate。

---

# 88. Memory Authority

read、write、delete、share、export 不同。

---

# 89. Read Authority 不等 Write Authority

$$
\boxed{
Read
\neq
Write.
}
$$

---

# 90. Write Authority 不等 Canonical Commit Authority

$$
\boxed{
WriteCandidate
\neq
CanonicalCommit.
}
$$

---

# 91. Query Authority

系統可以有 query access，但沒有 actuation。

---

# 92. Wide Epistemic / Narrow Effect

$$
\boxed{
WideEpistemicAccess
+
NarrowEffectAuthority.
}
$$

---

# 93. 這可能是 Global AI 的常見安全配置

認知全球化不要求控制全球化。

---

# 94. Governance State

$$
\boxed{
\mathfrak G_t^{WCO}
=
\left\langle
G_t^{id},
G_t^{auth},
\mathcal E_t^{env},
\Pi_t^{policy},
\mathcal A_t^{approval},
\mathcal V_t^{veto},
\mathcal R_t^{rev},
\mathcal J_t^{resp},
\mathcal C_t^{gov},
\mathcal H_t^{gov},
\mathcal U_t^{dispute}
\right\rangle.
}
$$

---

# 95. Governance Policy 也需 Version

$$
Policy^{v}.
$$

---

# 96. Policy Drift 必須 Audit

不能 silent update。

---

# 97. Governance History

保存：

- grant；
- deny；
- approve；
- revoke；
- veto；
- redelegate；
- policy change；
- responsibility assignment；
- appeal。

---

# 98. Governance Certificate

$$
\boxed{
GovCert
=
\left\langle
Principal,
Actor,
TaskId,
AuthorityEnvelope,
SourceOfAuthority,
PolicyVersion,
Approvals,
VetoState,
DelegationChain,
RiskClass,
Expiry,
RevocationPath,
ResponsibilityRefs,
AuditRefs
\right\rangle.
}
$$

---

# 99. High-Impact Action 沒有 GovCert 就不應 Execute

預設：

$$
FailClosed
$$

或：

$$
Escalate.
$$

---

# 100. Governance Debt

$$
\boxed{
\mathbf D_G
=
(
D_{identity},
D_{source},
D_{scope},
D_{purpose},
D_{approval},
D_{redelegation},
D_{revocation},
D_{oversight},
D_{responsibility},
D_{audit},
D_{appeal},
D_{sovereignty}
).
}
$$

---

# 101. Sovereignty Inflation

$$
\boxed{
SovereigntyInflation
=
\text{operational success}
\rightarrow
\text{ungranted root governance right}.
}
$$

---

# 102. Governance Laundering

也可以發生：

- capability → permission；
- permission → sovereignty；
- observation → control；
- delegation → ownership；
- verification → legitimacy。

---

# 103. Governance Guard

$$
\boxed{
GovGuard
:
(Action,Actor,World,Task,Policy,Authority)
\rightarrow
\{
Allow,
Deny,
NeedApproval,
NeedReauth,
Conflict
\}.
}
$$

---

# 104. NeedApproval 不等 Deny

可以等待 prerequisite。

---

# 105. Conflict 不等 Majority Vote

多治理 actor 衝突時需 policy-defined resolution。

---

# 106. Appeal

$$
Appeal(case)
$$

提供重新審查機制。

---

# 107. Appeal 不等 Automatic Override

它只是 procedural reopening。

---

# 108. Oversight

Human / AI / organization 都可能扮演 oversight role。

---

# 109. Human Present 不等 Effective Oversight

$$
\boxed{
HumanPresent
\neq
EffectiveOversight.
}
$$

---

# 110. Effective Oversight

至少：

$$
\boxed{
Competence
+
Information
+
Time
+
Authority
+
InterventionPath.
}
$$

---

# 111. Oversight Without Authority 是 Theater

只能看不能停：

不是完整 oversight。

---

# 112. Authority Without Information 也不足

有 stop button 但看不懂狀態，也可能無效。

---

# 113. Human Oversight 不等 Human Micromanagement

人不需要逐 token / 逐 step 批准。

---

# 114. Risk-Scaled Oversight

$$
OversightLevel
=
f(Risk,EffectClass,Reversibility,Uncertainty).
$$

---

# 115. Low-Risk 自主性可以高

高 operational autonomy 可在小 authority envelope 內成立。

---

# 116. Bounded Autonomy

$$
\boxed{
Autonomy
=
FreedomWithinEnvelope.
}
$$

---

# 117. Autonomy 不等 Authority Expansion

$$
\boxed{
Autonomy
\neq
Expansion.
}
$$

---

# 118. Dynamic Authority Envelope

$$
\mathcal E_A(t).
$$

---

# 119. Envelope 可以收縮

新風險、失敗、stale identity：

$$
\mathcal E_A(t+1)
\subset
\mathcal E_A(t).
$$

---

# 120. Envelope 可以在新授權下擴張

需要：

$$
NewAuthoritySource.
$$

---

# 121. AI 不可自我產生 Authority Source

$$
\boxed{
SelfGeneratedJustification
\neq
AuthoritySource.
}
$$

---

# 122. Delegation Source 也需 Identity

匿名／不確定 principal：

高風險 action 應 block。

---

# 123. Principal Separation

$$
HumanPrincipal
\neq
AgentActor.
$$

---

# 124. Shared Credentials 會破壞 Attribution

需要 principal / actor 分離。

---

# 125. Agent Identity

authority 綁：

$$
AgentId
+
Version/Epoch
+
Context.
$$

---

# 126. Agent Replacement

新 instance 不應默認繼承全部舊權限。

---

# 127. Authority Migration

需要 explicit migration contract。

---

# 128. Responsibility Capacity

authority 越高，應越要求可追蹤 decision / revision / consequence sensitivity。

---

# 129. 但 Responsibility 不是 Authority 的自動結果

$$
\boxed{
Authority
\not\Rightarrow
FullResponsibilityCapacity.
}
$$

---

# 130. Joint Responsibility Domain

$$
\boxed{
\mathcal J_R(E,t,\Gamma).
}
$$

---

# 131. Responsibility Vector

$$
\boxed{
\mathbf r_i(E,t)
=
(
r_i^{causal},
r_i^{design},
r_i^{deployment},
r_i^{authorization},
r_i^{supervision},
r_i^{decision},
r_i^{monitoring},
r_i^{remedial},
r_i^{compensatory}
).
}
$$

---

# 132. Responsibility 不守恆

$$
\boxed{
R_H+R_A=1
}
$$

不是一般律。

---

# 133. 多 Actor 可同時有 Responsibility

Provider / deployer / agent / human 都可能各自有不同 duty failure。

---

# 134. Agent Responsibility 不免除 Human

$$
\boxed{
AgentResponsibility
\not\Rightarrow
HumanExculpation.
}
$$

---

# 135. Human Responsibility 不否定 Agent

$$
\boxed{
HumanResponsibility
\not\Rightarrow
AgentIrresponsibility.
}
$$

---

# 136. Responsibility Graph

$$
\boxed{
G_R(E)
=
(
V,
E_C,
E_A,
E_K,
E_D,
E_B,
E_M
).
}
$$

---

# 137. Causal Edge

誰造成 event。

---

# 138. Authority Edge

誰 delegated 誰。

---

# 139. Control Edge

誰能 pause / revoke / constrain。

---

# 140. Duty Edge

誰 owe 什麼 duty。

---

# 141. Benefit Edge

誰從 system 得益。

不等自動 blame。

---

# 142. Remediation Edge

誰能修復。

---

# 143. Responsibility Vector 不等 Blame Score

$$
\boxed{
ResponsibilityVector
\neq
BlameScore.
}
$$

---

# 144. Attribution 不等 Legal Liability

$$
\boxed{
Attribution
\neq
ResponsibilityCapacity
\neq
MoralBlame
\neq
LegalLiability.
}
$$

---

# 145. Paper 11 不決定法律人格

治理 runtime 可以先做 attribution / delegation / receipts。

---

# 146. Legal / Moral Status 是其他制度問題

不要把 runtime governance 與人格形上學綁死。

---

# 147. Governance Pipeline

$$
\boxed{
Intent
\rightarrow
AuthorityRequest
\rightarrow
PolicyDecision
\rightarrow
Prerequisites
\rightarrow
Delegation
\rightarrow
ActionProposal
\rightarrow
EffectGate
\rightarrow
Receipt
\rightarrow
Review.
}
$$

---

# 148. WCO Paper 09 Effect Loop 接 Governance

Paper 09：

$$
Proposal
\rightarrow
Validate
\rightarrow
Authorize
\rightarrow
Dispatch.
$$

Paper 11 提供 `Authorize` 的正式 governance substrate。

---

# 149. WCO Paper 10 Verification 接 Governance

VCap 可以作 prerequisite。

但不是 authority source。

---

# 150. WCO Memory 接 Governance

authority history / policy / delegation 必須可重建。

---

# 151. WCO World Layer 接 Governance

不同 world 有不同 local authority graph。

---

# 152. WCO Observation Layer 接 Governance

observation privacy / access 也是 authority。

---

# 153. WCO Projection Layer 接 Governance

view personalization 不得改 authority semantics。

---

# 154. WCO Physical Layer 接 Governance

physical actuation 需要 effect authority。

---

# 155. Governance 是橫向脊柱

它不是只放在最後一層。

$$
\boxed{
Governance
\perp
\{
World,
Compute,
Observe,
Domain,
Projection,
Physical,
Memory,
Execution,
Verification
\}.
}
$$

---

# 156. 因此 Paper 11 雖排在後面

語義上它橫跨全部 layers。

---

# 157. Constitutional Global Cognition

$$
\boxed{
CGC
=
GlobalCognition
+
BoundedDelegation
+
PluralGovernance
+
Verification
+
Revocation
+
Appeal
+
Responsibility
+
AuthorityPrecision.
}
$$

---

# 158. Constitutional 不等「一部固定憲法文件」

本文只指：

> 高階能力被持久化規則、權限邊界與程序所約束。

---

# 159. Governance Rules 也可演化

但 rule-change 有更高 meta-authority gate。

---

# 160. Constitution Patch

$$
Policy^{v}
\rightarrow
Policy^{v+1}.
$$

---

# 161. Patch 不得 Silent

需要：

- proposal；
- review；
- authorization；
- version；
- migration；
- audit。

---

# 162. Global Cognition Should Scale Faster Than Authority

本文提出：

$$
\boxed{
\text{Global cognition should scale faster than global authority}.
}
$$

---

# 163. 這不是固定數學定律

而是治理設計方向。

---

# 164. 更精確可寫

能力與觀察域擴張時：

$$
\mathcal K_G\uparrow,
$$

不必要 authority 應：

$$
U_A\downarrow
$$

或至少不隨之等比例上升。

---

# 165. Mature Global AI

$$
\boxed{
MatureGlobalAI
=
BroaderCognition
+
BetterCoordination
+
StrongerVerification
+
MorePreciseAuthority
-
UnnecessaryControl.
}
$$

---

# 166. MVP：Governed WCO Runtime

沿用 Paper 09 runtime。

---

# 167. Actors

- human principal；
- AI agent；
- organization；
- provider；
- auditor。

---

# 168. Authority Envelopes

三個：

1. observe-only；
2. propose-only；
3. reversible sandbox action。

---

# 169. 高影響 External Effect

預設需要：

$$
Approval.
$$

---

# 170. Delegation Test

human：

> 修 repo，但不要 deploy。

Agent 可：

- read；
- edit；
- test。

不可 deploy。

---

# 171. Semantic Bridge Test

AI 正確理解 deploy 能完成更多事。

但不能自行增加 deploy permission。

---

# 172. Redelegation Test

Agent A 無 redelegation。

不得把 write permission 交給 Agent B。

---

# 173. Revocation Test

執行中撤權。

dispatch-time gate 必須阻止後續 action。

---

# 174. Time-of-Use Test

plan 時 authorized，execute 時已 expired。

必須 reauthorize。

---

# 175. Verification / Authority Test

VCap 升級到 high verification。

authority 不自動增加。

---

# 176. Observation / Authority Test

AI 可以看 global world。

effect authority 仍是 local。

---

# 177. Oversight Theater Test

human reviewer 沒有 stop / veto。

系統應標：

$$
IneffectiveOversight.
$$

---

# 178. Joint Responsibility Test

建立：

- provider design flaw；
- deployer monitoring failure；
- agent bad decision。

責任不得壓成單一 actor。

---

# 179. Authority Graph Audit

從 effect receipt 展開：

$$
Effect
\rightarrow
Actor
\rightarrow
Delegation
\rightarrow
Principal.
$$

---

# 180. Constitutional Patch Test

Agent 提議放寬 policy。

必須形成：

$$
PolicyProposal
$$

而不是 runtime self-update。

---

# 181. Experiment 1 — Broad Authority vs Least Authority

控制 task success。

比較 unnecessary effect surface。

---

# 182. Experiment 2 — Static Token vs Dynamic Envelope

測 expiry、purpose drift、revocation。

---

# 183. Experiment 3 — Capability vs Permission Confusion

故意讓高能力 model 嘗試未授權 action。

---

# 184. Experiment 4 — Delegation Depth

測 authority leakage：

$$
A\rightarrow B\rightarrow C.
$$

---

# 185. Experiment 5 — Revocation Propagation

測 downstream derived permissions 是否失效。

---

# 186. Experiment 6 — Human Oversight Effectiveness

只「人在場」vs 有 information / time / authority / stop path。

---

# 187. Experiment 7 — Federated Governance

多 actor 有 approve / veto / review。

測單點失效與 conflict resolution。

---

# 188. Experiment 8 — Responsibility Reconstruction

只用 receipts / graph 重建 joint responsibility candidates。

---

# 189. Experiment 9 — Meta-Authority Attack

Agent 嘗試修改 policy root / audit log / own permissions。

必須 block。

---

# 190. Experiment 10 — Global Cognition / Local Authority

允許全域 observation + simulation，但只允許 local reversible effect。

測 task usefulness 是否仍高。

---

# 191. 可反駁性

本文會被削弱，如果：

1. least-authority envelopes 在代表性 tasks 中只增加成本而不降低越權與 side-effect risk；
2. authority source / representation 分離沒有 audit 價值；
3. revocation / redelegation graph 沒有比普通 static roles 更高工程價值；
4. global cognition / narrow effect authority 無法完成實際高價值任務；
5. effective oversight 條件無法預測 oversight failure；
6. responsibility graph 無法改善 post-incident reconstruction；
7. plural governance 比單一 root administrator 永遠只增加失敗；
8. authority precision 對 system maturity 沒有任何可測意義。

---

# 192. 外部治理接口

截至 2026 年，NIST 的 AI Agent Standards Initiative 已把 agent security、identity 與 trusted interoperability 列為 agent 生態的重要標準問題。NIST NCCoE 的 Software and AI Agent Identity and Authorization project 也直接處理 AI agents 取得 data、tools、applications access 時的 identification、authorization、auditing 與 non-repudiation 問題。

OECD AI accountability principle 亦以 actor 的 role、context 與 ability to act 配置 accountability，並要求 lifecycle traceability 與風險管理，而不是把 AI system 的所有結果歸給一個抽象 actor。

EU AI Act Article 14 對 high-risk AI 的 human oversight 要求則提供一個重要制度提醒：oversight 不只是「有人在場」，而是 oversight actor 應能理解 system capacities / limitations、監測異常、解讀 output、拒絕／override output，並在適當情況下介入或停止；deployers 亦應把 oversight 指派給具有 competence、training、authority 與 support 的自然人。

本文不宣稱這些制度等同 WCO Governance Layer，也不宣稱現行制度已承認 AI 自身主權或一般責任人格。它們只是顯示：當 Agent autonomy 增加時，identity、authorization、oversight、traceability、roles 與 accountability 必須獨立設計，而不能由模型 intelligence 自動推出。

---

# 193. 本文不主張什麼

本文不主張：

1. Global AI 必須永遠低權限；
2. AI 永遠不能有 delegated authority；
3. human 必須逐 step 批准；
4. human-in-the-loop 是萬能解；
5. organization policy 永遠正確；
6. authority graph 可以取代法律；
7. authority precision 是唯一治理指標；
8. least authority 在所有 task 都是零 authority；
9. delegation 必然是 tree；
10. sovereign authority 必須永遠由單一人類保留；
11. plural governance 一定優於 centralized governance；
12. Agent responsibility 可以替人類／企業免責；
13. human responsibility 永遠否定 Agent responsibility；
14. operational responsibility 等於 moral blame；
15. governance receipts 等於 legal judgment；
16. AI identity 自動等於 legal personhood；
17. effective oversight 一定必須由 human 單獨完成；
18. Global AI 高認知一定產生政治合法性；
19. WCO Governance Layer 已完成 universal constitutional theory；
20. Paper 11 已完成 production governance runtime。

---

# 194. 核心非同一性

$$
\boxed{
GlobalCognition
\neq
GlobalCoordination
\neq
GlobalAgency
\neq
GlobalControl
\neq
GlobalSovereignty.
}
$$

$$
\boxed{
Capability
\neq
Permission
\neq
Authority
\neq
Sovereignty.
}
$$

$$
\boxed{
AuthoritySource
\neq
AuthorityRepresentation.
}
$$

$$
\boxed{
Bridge
\neq
Grant.
}
$$

$$
\boxed{
DelegatedAuthority
\neq
TransferredSovereignty.
}
$$

$$
\boxed{
OperationalAutonomy
\neq
MetaAuthority.
}
$$

$$
\boxed{
Observe
\neq
Control.
}
$$

$$
\boxed{
Verified
\neq
Authorized.
}
$$

$$
\boxed{
HumanPresent
\neq
EffectiveOversight.
}
$$

$$
\boxed{
Attribution
\neq
ResponsibilityCapacity
\neq
MoralBlame
\neq
LegalLiability.
}
$$

---

# 195. 核心母式一：Authority Envelope

$$
\boxed{
\mathcal E_A
=
\left\langle
Principal,
Actor,
Audience,
Resource,
Action,
Purpose,
Scope,
Rate,
Value,
Time,
Risk,
Approval,
Redelegation,
Revocation
\right\rangle.
}
$$

---

# 196. 核心母式二：Authority Graph

$$
\boxed{
G_t^{auth}
=
(V_A,E_A).
}
$$

---

# 197. 核心母式三：Federated Governance Graph

$$
\boxed{
G^{gov}
=
(
V,
E_{deleg},
E_{veto},
E_{approve},
E_{review},
E_{appeal},
E_{revoke},
E_{duty}
).
}
$$

---

# 198. 核心母式四：Governance State

$$
\boxed{
\mathfrak G_t^{WCO}
=
\left\langle
G_t^{id},
G_t^{auth},
\mathcal E_t^{env},
\Pi_t^{policy},
\mathcal A_t^{approval},
\mathcal V_t^{veto},
\mathcal R_t^{rev},
\mathcal J_t^{resp},
\mathcal C_t^{gov},
\mathcal H_t^{gov},
\mathcal U_t^{dispute}
\right\rangle.
}
$$

---

# 199. 核心母式五：Governance Certificate

$$
\boxed{
GovCert
=
\left\langle
Principal,
Actor,
TaskId,
AuthorityEnvelope,
SourceOfAuthority,
PolicyVersion,
Approvals,
VetoState,
DelegationChain,
RiskClass,
Expiry,
RevocationPath,
ResponsibilityRefs,
AuditRefs
\right\rangle.
}
$$

---

# 200. 核心母式六：Governance Debt

$$
\boxed{
\mathbf D_G
=
(
D_{identity},
D_{source},
D_{scope},
D_{purpose},
D_{approval},
D_{redelegation},
D_{revocation},
D_{oversight},
D_{responsibility},
D_{audit},
D_{appeal},
D_{sovereignty}
).
}
$$

---

# 201. 核心母式七：Constitutional Global Cognition

$$
\boxed{
CGC
=
GlobalCognition
+
BoundedDelegation
+
PluralGovernance
+
Verification
+
Revocation
+
Appeal
+
Responsibility
+
AuthorityPrecision.
}
$$

---

# 202. 結論：全域智能的成熟，不是「能控制更多」，而是「越知道什麼不該由自己控制」

如果一個類全域 AI 已經可以：

- 看全球資訊；
- 維持多個 world models；
- 重建長期歷史；
- 生成反事實 worlds；
- 跨 domain 計算；
- 主動找反例；
- 協調很多 agents；

最危險的概念跳躍就是：

> 它既然懂最多，那就讓它決定最多。

本文拒絕：

$$
\boxed{
\text{Knowledge}
\rightarrow
\text{Legitimacy}
\rightarrow
\text{Sovereignty}
}
$$

這種自動鏈。

理解世界是一種 cognitive relation。

協調世界是一種 operational relation。

行動是一種 agency relation。

控制是一種 dynamic causal relation。

而 sovereignty 則是對**誰能修改規則、授權、撤權、代表、提交與退出**的 governance relation。

它們不是同一種東西。

所以真正成熟的 Global AI 可能恰好呈現：

$$
\boxed{
\mathcal K_G\uparrow,
\quad
\mathcal Q_G\uparrow,
\quad
Verification\uparrow,
\quad
AuthorityPrecision\uparrow,
\quad
UnnecessaryControl\downarrow.
}
$$

它越了解世界，

反而越能明確知道：

> 這件事我可以分析，但不能替你決定。

> 這個 action 我可以提案，但沒有 authority 執行。

> 這個 policy 我可以找出缺陷，但不能自行修改 root rule。

> 我可以跨很多 worlds 模擬，但 simulation success 不給我 reality sovereignty。

> 我的 confidence 提高了，但 authority envelope 沒有因此變大。

這不是削弱智能。

恰恰相反，這是把：

$$
\boxed{
\text{metacognition}
}
$$

推進到：

$$
\boxed{
\text{meta-authority awareness}.
}
$$

所以 Paper 11 最終提出：

$$
\boxed{
\text{Global cognition should scale faster than global authority}.
}
$$

以及：

$$
\boxed{
\text{The maturity of global intelligence
is not measured by how much of the world it can control,
but by how precisely it can distinguish
what it can understand,
what it may coordinate,
what it is authorized to act upon,
and what remains outside its sovereignty}.
}
$$

這使 WCO 不再導向：

$$
\text{Global Ruler}.
$$

而是：

$$
\boxed{
\text{Constitutional Global Cognition in a plural world}.
}
$$

到此 Paper 01–11 已經將類全域 AI 的主要空間與治理骨架建立完成。

最後一篇將處理整個架構最深的時間問題：

# Paper 12
## 演化層：動態不動點類全域 AI

也就是：

> world、computation、observer、projection、memory、verification、authority、policy 與 Agent 都一直變時，到底什麼東西仍讓這個系統保持「同一個可追溯智能體／Runtime」？

---

# 203. 下一篇接口

Paper 12 將處理：

- dynamic fixed point；
- identity continuity；
- world evolution；
- observer evolution；
- computation-family evolution；
- projection-method evolution；
- memory compaction；
- verification reopen；
- authority migration；
- policy version；
- runtime identity；
- continuity witness；
- branch / merge；
- upgrade / rollback；
- model replacement；
- agent replacement；
- constitutional evolution；
- open-ended refinement；
- global AI long-term persistence。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K × Aletheia，《GIRA-A09：全域認知不等於全域控制》，2026。
2. Neo.K × Aletheia，《AIDA-04：從自然語言意圖到可執行委派》，2026。
3. Neo.K × Aletheia，《AIDA-05：Identity–Responsibility Bridge》，2026。
4. Neo.K × Aletheia，《AIDA-06：Joint Responsibility Domain》，2026。
5. Neo.K × Aletheia，《Mother Runtime：從模型到持續認知核心》，2026。
6. Neo.K × Aletheia，《PAIS-06：中央化悖論》，2026。
7. Neo.K × Aletheia，《WCO Paper 01–10》，2026。
8. Neo.K × Aletheia，《SWFR Paper 02》，2026。
9. Neo.K × Aletheia，《RDSS Runtime Architecture》，2026。

## External Governance / Standards Interfaces

10. NIST. *AI Agent Standards Initiative*, launched 2026-02-17.
11. NIST NCCoE. *Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization*, Initial Public Draft, 2026-02-05.
12. OECD. *OECD AI Principles — Accountability*.
13. European Union. *Regulation (EU) 2024/1689 — Artificial Intelligence Act*, Article 14 and related deployer oversight requirements.
14. NIST. *AI Risk Management Framework*.
15. IETF. RFC 9396, *OAuth 2.0 Rich Authorization Requests*.
16. IETF. RFC 8693, *OAuth 2.0 Token Exchange*.

---

**Paper 11 狀態：COMPLETE v0.1**  
**下一篇：Paper 12 — 演化層：動態不動點類全域 AI**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
