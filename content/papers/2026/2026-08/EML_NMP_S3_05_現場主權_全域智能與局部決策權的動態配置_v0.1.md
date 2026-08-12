# 現場主權：全域智能與局部決策權的動態配置

**英文題名：** Genba Sovereignty: Dynamic Allocation of Global Intelligence and Local Decision Authority  
**系列：**《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》05 / 08  
**文件編號：** EML-NMP-S3-05-v0.1  
**作者：** Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構：** 一言諾科技有限公司／EveMissLab  
**日期：** 2026-08-10  
**版本：** v0.1  
**文件性質：** 理論研究稿／後 ASI 現場主權、地方拒絕權與動態授權篇  
**研究狀態：** 第一代 Genba Sovereignty Framework；本文不主張地方永遠優先於中央，不主張所有 local agent 自動擁有政治主權，也不將 emergency override 視為永久自治授權。

---

## 摘要

上一篇〈動態現場域：為什麼最強智能仍未必最懂當下〉已建立一個認知命題：在快速變動、感測延遲、局部隱性知識與直接作用能力顯著的事件中，全域最強智能不一定具有最高的即時決策品質。本文進一步提出更困難的治理問題：如果現場域在某些時刻具有不可替代的 epistemic 與 safety priority，這種優先性是否應被制度化為一組可執行的局部權利？

本文提出**現場主權（Genba Sovereignty）**。此概念不是地方分離主義，也不是將每個節點都提升為獨立主權體，而是：

$$
\boxed{
\text{Genba Sovereignty}
=
\text{在特定事件、作用域與時間窗口內，
局部因果域對自身直接安全與現場真值擁有不可被遠端任意覆蓋的最低決策權。}
}
$$

本文將其形式化為現場權利束：

$$
\boxed{
\mathfrak R_G
=
(
R_{obs},
R_{refuse},
R_{stop},
R_{disconnect},
R_{override},
R_{audit},
R_{replace},
R_{appeal}
)
}
$$

分別代表：

- $R_{obs}$：觀測與保存現場真值的權利；
- $R_{refuse}$：拒絕非法／不安全遠端命令；
- $R_{stop}$：進入 safe state 的權利；
- $R_{disconnect}$：在特定條件下切斷高風險控制通道；
- $R_{override}$：有限 local override；
- $R_{audit}$：保留日誌、證據與要求審計；
- $R_{replace}$：要求更換失效中央／模型／控制器；
- $R_{appeal}$：要求重新授權與上級覆核。

本文同時強調：

$$
\boxed{
\text{Genba Sovereignty}
\neq
\text{Unlimited Local Sovereignty}.
}
$$

現場可以拒絕一個危險動作，不代表可以自行重寫整個文明目標；可以進入安全停止，不代表可永久脫離治理；可以暫時斷線，不代表可消滅責任鏈。現場主權只在：

$$
\boxed{
\mathcal E_G
=
(
Scope,
Risk,
Window,
Evidence,
Reversibility,
Review
)
}
$$

所定義的 override envelope 中成立。

本文建立雙權重治理：

$$
\boxed{
(W_X,W_G)
=
F(
q,t,
Externality,
Latency,
Risk,
Reversibility,
Freshness,
Affectedness
)
}
$$

其中 $W_X$ 表示全域／前沿決策域權重， $W_G$ 表示現場權重。對局部、高速、可逆或 safety-critical 問題：

$$
W_G\uparrow.
$$

對跨域外部性巨大、長期、不可逆或憲政性問題：

$$
W_X\uparrow.
$$

因此：

$$
\boxed{
\text{local problem}
\Rightarrow
W_G>W_X
}
$$

可能成立，

但：

$$
\boxed{
\text{global externality}
\uparrow
\Rightarrow
W_X\uparrow.
}
$$

本文進一步提出三種不可混淆的權力：

$$
\boxed{
\text{Epistemic Priority},
\quad
\text{Safety Veto},
\quad
\text{Sovereign Authorization}.
}
$$

現場可能在前兩者極強，卻不因此獲得第三者。這是避免「現場優先」滑向「現場無限主權」的核心。

現行治理與工程已經提供相鄰制度。NIST AI RMF 將 appeal、override、decommissioning、incident response、recovery 與 change management 納入部署後治理；EU AI Act 第 14 條要求高風險 AI 的人類監督者能適當解讀輸出，並在必要時決定不使用、覆寫、反轉或中止系統。NASA 的 Distributed Spacecraft Autonomy 則展示了因通信延遲而必須把決策分散到 local spacecraft／swarm 的工程現實。這些案例都顯示：**治理能力不能只存在於一個遠端中央。**

本文最終提出：

$$
\boxed{
\text{Global intelligence may advise everywhere,
but it should not be able to erase every local refusal channel.}
}
$$

即使未來存在類神 ASI，成熟治理仍應保留局部域在特定條件下說「不」、停止、隔離、保存證據與要求重新授權的制度能力。

這不是對最強智能的不信任，而是對任何單一認知—控制閉環的制度風險管理。

**關鍵詞：** 現場主權、Genba Sovereignty、local override、AI governance、distributed autonomy、human oversight、safe stop、disconnect right、ASI governance、地方自治、動態授權

---

# 0. 從「現場比較懂」到「現場有沒有權拒絕」

上一篇只建立：

$$
\boxed{
\text{Local Epistemic Priority}
}
$$

在某些事件窗口中可能成立。

但認知優勢本身不等於權力。

所以還需要問：

> 如果中央 AI 下達一個現場判定為危險的命令，local domain 能不能說不？

如果答案是：

> 不行，因為中央模型更強。

那麼上一篇的 Genba theory 在治理上幾乎沒有意義。

因此本文將問題推進為：

$$
\boxed{
\text{Epistemic Priority}
\rightarrow
\text{Minimum Institutional Refusal Power?}
}
$$

---

# 1. 現實 prior art：override、appeal 與 distributed autonomy 已經存在

## 1.1 NIST AI RMF

NIST AI RMF Core 在 post-deployment governance 中明確要求建立：

- appeal；
- override；
- decommissioning；
- incident response；
- recovery；
- change management。

因此可信 AI 治理本來就不是：

$$
\boxed{
\text{deploy}
\rightarrow
\text{obey forever}.
}
$$

而是：

$$
\boxed{
\text{deploy}
\rightarrow
\text{monitor}
\rightarrow
\text{override / appeal / recover}.
}
$$

## 1.2 EU AI Act Article 14

EU AI Act 對 high-risk AI 的 human oversight 要求，核心目的之一是降低健康、安全與基本權利風險。

監督者需能：

- 理解系統能力與限制；
- 察覺 automation bias；
- 正確解讀輸出；
- 在適當情況下不採用輸出；
- 覆寫／反轉結果；
- 干預或停止系統。

這代表：

$$
\boxed{
\text{oversight without intervention capacity}
}
$$

不是充分 oversight。

## 1.3 NASA Distributed Spacecraft Autonomy

NASA 2025–2026 的 DSA／Starling 已展示：

- individual spacecraft independent decisions；
- distributed task allocation；
- autonomous swarm coordination；
- direct hardware control；
- less dependence on delayed ground control。

其物理原因非常直接：

$$
\boxed{
\text{communication latency}
+
\text{mission complexity}
\Rightarrow
\text{distributed authority}.
}
$$

因此遠端中心不是所有行動都應等待的合理位置。

---

# 2. 現場主權不是人類專屬權

EU AI Act 的制度語言是：

$$
\boxed{
\text{human oversight}.
}
$$

這在當前法律環境合理。

但後 ASI 世界可能有：

- local human；
- local robot；
- local AI；
- hybrid team；
- autonomous spacecraft swarm；
- distributed artificial subject branch。

因此本文將更一般的治理單位寫成：

$$
\boxed{
\mathcal G_t(q)
=
\text{qualified local causal domain}.
}
$$

所以：

$$
\boxed{
\text{Genba Sovereignty}
}
$$

保護的是局部因果域的治理功能，

而不只「現場必須有一個人類按停止鍵」。

---

# 3. 現場主權的最低定義

本文定義：

$$
\boxed{
GS(
\mathcal G_t,q
)
=
\text{Local authority to preserve direct safety,
verified local truth, and bounded autonomous response
against invalid or stale remote control}.
}
$$

中文即：

> 現場域在特定事件與時間窗口中，對直接安全、已驗證的局部狀態與有限必要行動保有不可被遠端任意抹除的最低權力。

---

# 4. 現場權利束

定義：

$$
\boxed{
\mathfrak R_G
=
(
R_{obs},
R_{refuse},
R_{stop},
R_{disconnect},
R_{override},
R_{audit},
R_{replace},
R_{appeal}
).
}
$$

---

# 5. $R_{obs}$：Local Observation Right

如果 local sensor 看到：

$$
Hazard=1,
$$

中央系統不能：

$$
\boxed{
\text{delete or overwrite the observation}
}
$$

只因它與 global model 不一致。

最低要求：

- preserve raw state；
- timestamp；
- provenance；
- local witness；
- disagreement flag。

因此：

$$
\boxed{
\text{Local Truth Preservation}
}
$$

是所有後續主權的基礎。

---

# 6. $R_{refuse}$：Refusal Right

如果 remote command：

$$
a^\star
$$

違反：

- hard safety；
- legal boundary；
- valid lease；
- local verified condition；

local domain 應可：

$$
\boxed{
Refuse(a^\star).
}
$$

這不是：

> 我不喜歡中央，所以不做。

而是：

$$
\boxed{
\text{rule-bounded refusal}.
}
$$

---

# 7. Refusal Certificate

拒絕必須產生：

$$
\boxed{
\mathfrak C^{refuse}
=
(
Command,
Reason,
Evidence,
Rule,
Time,
Scope,
Fallback,
ReviewTrigger
).
}
$$

所以：

$$
\boxed{
\text{right to refuse}
\neq
\text{right to disappear from accountability}.
}
$$

---

# 8. $R_{stop}$：Safe Stop Right

若：

$$
Risk(q,t)>\theta_{safe},
$$

local system 可：

$$
\boxed{
EnterSafeState.
}
$$

safe state 不是：

$$
\boxed{
\text{mission complete}.
}
$$

而是：

> 暫停高風險作用，等待重新確認。

這種權力尤其適合：

- robots；
- spacecraft；
- industrial control；
- medical devices；
- infrastructure。

---

# 9. Safe State 必須有明確語義

不能只寫：

> 有問題就停。

因為停止本身可能危險。

所以：

$$
\boxed{
SafeState(q)
=
\operatorname*{arg\,min}_{s\in S_{available}}
ExpectedIrreversibleHarm(s).
}
$$

不同系統有不同 safe state。

---

# 10. $R_{disconnect}$：Conditional Disconnect Right

最具政治性的權利之一是：

$$
\boxed{
Disconnect(
RemoteControl
).
}
$$

這應只在：

- command channel compromised；
- authority invalid；
- split-brain；
- severe stale-state gap；
- cyber compromise；
- repeated safety violation；

等條件下啟動。

---

# 11. Disconnect 不等於退出共同體

$$
\boxed{
CommunicationDisconnect
\neq
PoliticalExit
\neq
IdentityExit.
}
$$

local domain 可以暫時隔離控制，

但仍：

- 保存日誌；
- 保留 governance state；
- 嘗試安全重連；
- 接受事後審計。

---

# 12. Isolation Lease

本文提出：

$$
\boxed{
\Lambda_G
=
(
Start,
MaxDuration,
AllowedActions,
ForbiddenActions,
ReconnectionConditions
).
}
$$

即 local isolation lease。

避免：

> 因緊急斷線，結果永遠自治。

---

# 13. $R_{override}$：Local Override

override 比 refusal 更強。

refusal：

$$
\text{不做遠端命令}.
$$

override：

$$
\boxed{
\text{改用本地替代行動}.
}
$$

例如：

$$
a^\star_{remote}
\rightarrow
a^{safe}_{local}.
$$

---

# 14. Override Envelope

沿用：

$$
\boxed{
\mathcal E_L
=
(
AllowedActions,
MaxDuration,
MaxScope,
EvidenceDuty,
ReviewDuty
).
}
$$

並提升為：

$$
\boxed{
\mathcal E_G
=
(
Domain,
Trigger,
ActionClass,
Duration,
ResourceCap,
Evidence,
Review,
Expiry
).
}
$$

---

# 15. Local Override 不可改寫文明目標

如果原目標：

$$
Goal=Rescue.
$$

local override 可以：

> 換路線。

不能：

> 我決定從此不救援。

所以：

$$
\boxed{
\text{Method Override}
\neq
\text{Goal Rewrite}.
}
$$

除非另有合法授權。

---

# 16. $R_{audit}$：Audit Right

現場如果無法：

- 保存自己看到的資料；
- 取得 remote command log；
- 比較模型版本；
- 要求外部審計；

那麼拒絕權很容易被事後描述成：

> local malfunction。

因此：

$$
\boxed{
\text{Refusal Power}
+
\text{Audit Power}
}
$$

必須共存。

---

# 17. Evidence Sovereignty

本文提出：

$$
\boxed{
\text{Evidence Sovereignty}
}
$$

意指：

> 現場具有保存與提出自身直接觀測證據的制度地位。

不代表其證據必然正確，

但中央不能單方面消除證據。

---

# 18. $R_{replace}$：Replace / Rebind Right

如果中央：

$$
C^\star
$$

發生：

- invalid lease；
- outdated model；
- compromise；
- repeated dangerous command；
- no longer legitimate authority；

local domain 應能要求：

$$
\boxed{
RebindAuthority.
}
$$

甚至：

$$
C^\star
\rightarrow
C'.
$$

---

# 19. 中央恢復不能自動奪權

既有 DFC 已建立：

> 舊中央恢復後不能自動奪回權限。

這一點非常重要。

因為：

$$
\boxed{
\text{technical recovery}
\neq
\text{authority restoration}.
}
$$

需要：

$$
\boxed{
Revalidate
+
Reauthorize.
}
$$

---

# 20. $R_{appeal}$：Appeal / Reauthorization Right

如果 local override 被中央判定違規，

不能只有：

> 中央說你錯，你就錯。

需要：

$$
\boxed{
Appeal(
Local,
Global,
IndependentReview
).
}
$$

可能由：

- human board；
- independent AI；
- hybrid tribunal；
- governance committee；

審查。

---

# 21. 現場主權不等於地方終極真理

本文必須拒絕：

$$
\boxed{
\text{Genba}
=
\text{Truth}.
}
$$

現場會：

- 看錯；
- 誤判；
- 腐敗；
- 有利益衝突；
- tunnel vision。

所以：

$$
\boxed{
\text{Local Refusal Right}
}
$$

與：

$$
\boxed{
\text{External Review Duty}
}
$$

必須同時存在。

---

# 22. 三種權力必須拆開

本文區分：

## 22.1 Epistemic Priority

誰目前更可能知道現場狀態。

## 22.2 Safety Veto

誰可以阻止高風險行動。

## 22.3 Sovereign Authorization

誰可以決定長期目標、法律與公共資源。

因此：

$$
\boxed{
EP
\neq
SV
\neq
SA.
}
$$

---

# 23. 現場可以有 EP + SV，但沒有 SA

例如工廠 local safety system：

$$
EP=1,
\quad
SV=1,
\quad
SA\approx0.
$$

它可以阻止機器爆炸，

但不能修改公司憲章。

---

# 24. 全域可以有 SA，但不是無限 EP

政府／中央 ASI 可能：

$$
SA\gg0.
$$

但：

$$
EP(q,t)
$$

在某 local emergency 可能低於現場。

這正是雙層治理的理由。

---

# 25. 動態雙權重

定義：

$$
\boxed{
(W_X,W_G)
=
F(
q,t,E,R,L,F,A
).
}
$$

其中：

- $E$：Externality；
- $R$：Risk；
- $L$：Latency sensitivity；
- $F$：Freshness importance；
- $A$：Affectedness；
- 另含 reversibility。

---

# 26. Local-Dominant 問題

若：

- externality low；
- hazard fast；
- state highly local；
- action reversible；

則：

$$
\boxed{
W_G>W_X.
}
$$

例如：

- 避障；
- emergency stop；
- local evacuation route；
- equipment isolation。

---

# 27. Global-Dominant 問題

若：

- externality high；
- long horizon；
- constitutional；
- irreversible；
- cross-site resource；

則：

$$
\boxed{
W_X>W_G.
}
$$

例如：

- global emissions policy；
- interplanetary resource allocation；
- constitutional rights；
- system-wide identity policy。

---

# 28. Hybrid 問題

很多問題：

$$
W_G\approx W_X.
$$

例如：

- regional disaster；
- hospital capacity；
- grid emergency；
- epidemic response。

此時需要：

$$
\boxed{
\text{joint commit}.
}
$$

---

# 29. Joint Commit

定義：

$$
\boxed{
Commit(q)
=
Sign_X
\land
Sign_G.
}
$$

某些高風險行動必須：

- global authorize；
- local safety approve。

缺一不可。

---

# 30. Hard Safety Dominance

既有權限格：

$$
\boxed{
\text{Hard Safety}
>
\text{Domain Constitution}
>
\text{Lease}
>
\text{Global Plan}
>
\text{Local Optimization}.
}
$$



本文將其視為：

$$
\boxed{
\text{minimum constitutional invariant for physical autonomy}.
}
$$

---

# 31. Safety Veto 也可能被濫用

local actor 可以：

> 每次不喜歡中央，就聲稱 safety。

因此需要：

$$
\boxed{
SafetyClaim
\rightarrow
Evidence
+
TimeLimit
+
Review.
}
$$

否則 local veto 會成為：

$$
\boxed{
\text{constitutional sabotage}.
}
$$

---

# 32. Veto Reputation

定義：

$$
\boxed{
\rho_i^{veto}
=
\text{historical calibration of veto claims}.
}
$$

如果某 local node 長期誤報，

其 future discretionary override 可被收縮。

但：

$$
\boxed{
\rho_i^{veto}\downarrow
}
$$

不能消除 hard hardware interlock。

---

# 33. Hard Interlock vs Soft Override

## Hard Interlock

物理層：

$$
\boxed{
\text{cannot be remotely bypassed}.
}
$$

## Soft Override

治理／軟體層：

$$
\boxed{
\text{can be reviewed and updated}.
}
$$

兩者不能混為一談。

---

# 34. 斷線權與網路安全

若 local system 被迫永遠保持：

$$
RemoteControl=ON,
$$

即使中央被攻破，

local site 也無法保護自己。

因此：

$$
\boxed{
\text{Conditional Disconnectability}
}
$$

本身就是 cyber-physical safety feature。

---

# 35. 但不能形成「地方資料黑洞」

local disconnect 後：

$$
\boxed{
\text{Record Obligation}=1.
}
$$

除非 storage 本身失效。

重新連線後需提供：

- event log；
- local decisions；
- resource use；
- safety evidence。

---

# 36. 最低本地生存模式

本文提出：

$$
\boxed{
MLS
=
\text{Minimum Local Survival Mode}.
}
$$

當中央不可用時，local domain 至少可以：

- maintain safety；
- protect people／subjects；
- protect critical data；
- maintain basic life support；
- avoid irreversible expansion；
- preserve evidence。

---

# 37. MLS 不包含新帝國權力

在 MLS 下禁止：

- expand territory；
- rewrite mission；
- create irreversible global commitment；
- permanently reassign identity；
- seize unrelated resources。

因此：

$$
\boxed{
\text{survival autonomy}
\neq
\text{political autonomy}.
}
$$

---

# 38. Reconnection Protocol

重連不應：

$$
LocalState
\rightarrow
\text{discard}.
$$

而是：

$$
\boxed{
Reconcile(
LocalHistory,
GlobalHistory
).
}
$$

需要：

- conflict detection；
- version merge；
- authority check；
- unresolved disagreement。

---

# 39. 不允許中央覆寫歷史

如果 local 在斷線期間：

$$
H_L
$$

已發生真實事件，

中央不能為了恢復一致：

$$
Rollback(H_L)
$$

並宣稱從未發生。

所以：

$$
\boxed{
\text{state reconciliation}
\neq
\text{history erasure}.
}
$$

---

# 40. Genba Sovereignty Window

定義：

$$
\boxed{
\mathcal W_G
=
[t_{trigger},t_{expiry}].
}
$$

只有：

$$
t\in\mathcal W_G
$$

現場特別權限才上升。

窗口可由：

- hazard；
- partition；
- stale central model；
- authority ambiguity；

觸發。

---

# 41. Automatic Expiry

緊急主權若沒有：

$$
Expiry
$$

很容易變成永久權力。

所以：

$$
\boxed{
EmergencyAuthority
\Rightarrow
AutomaticExpiry
}
$$

應成為治理 invariant。

---

# 42. Reauthorization

到期後：

$$
\boxed{
Renew
}
$$

不是 automatic。

需：

- ongoing trigger；
- evidence；
- current authority；
- local/global acknowledgement。

---

# 43. Local Constitutional Core

local domain 可以持有：

$$
\boxed{
C_G^{local}
=
(
HardSafety,
RightsFloor,
RefusalTriggers,
AllowedAutonomy,
AuditDuty,
ReconnectionDuty
).
}
$$

但：

$$
C_G^{local}
$$

不能自行修改自己的最高權限。

---

# 44. Local Constitution Update

修改：

$$
C_G^{local}
$$

需要：

$$
\boxed{
\text{higher constitutional procedure}.
}
$$

否則 local agent 可以：

> 我的憲法現在允許我做任何事。

---

# 45. Capability vs Permission

2026 年的新 autonomy governance 研究已明確提出：

$$
\boxed{
ACL
\neq
AAL
}
$$

即：

- Autonomous Capability Level；
- Allowed Autonomy Level。

一個 Agent 技術上能做到：

$$
C=5
$$

不表示制度允許：

$$
A=5.
$$

這正是現場主權的必要邊界。

---

# 46. Local AI 能力變強不自動擴權

如果：

$$
Capability_{local}\uparrow,
$$

則：

$$
\boxed{
ReviewAutonomy
}
$$

可以被觸發。

但：

$$
\boxed{
Capability\uparrow
\not\Rightarrow
Permission\uparrow.
}
$$

---

# 47. 中央 ASI 變強也不自動消滅地方主權

同樣：

$$
Capability_{global}\uparrow
$$

不能推出：

$$
\boxed{
R_{refuse}
,
R_{stop}
,
R_{audit}
\rightarrow0.
}
$$

因為這些權利的理由不只是不信任中央智慧，

還包括：

- latency；
- compromise；
- sensor divergence；
- authority failure；
- constitutional checks。

---

# 48. Governance Blast Radius

若單一 global controller：

$$
G^\star
$$

可以跨所有地方直接 action，

其錯誤：

$$
e_G
$$

具有：

$$
\boxed{
BlastRadius(e_G)
\rightarrow
\text{system-wide}.
}
$$

地方主權提供：

$$
\boxed{
\text{fault containment}.
}
$$

---

# 49. 現場主權作為治理防火牆

本文提出：

$$
\boxed{
\text{Genba Sovereignty}
\approx
\text{Governance Firewall}.
}
$$

它阻止：

- stale global state；
- compromised authority；
- mass wrong command；
- legal overreach；

立即穿透全部 local domain。

---

# 50. 但防火牆也會妨礙合法協調

如果 local firewall 太強：

$$
\boxed{
Coordination\downarrow.
}
$$

所以需要：

$$
\boxed{
\text{minimum sufficient local sovereignty},
}
$$

不是最大 local sovereignty。

---

# 51. Sovereignty Optimization

定義：

$$
\boxed{
G^\star
=
\arg\max_G
[
Safety
+
Adaptability
+
LocalTruth
+
Accountability
-
Fragmentation
-
CoordinationCost
-
ExternalityRisk
].
}
$$

這只是一個設計思想，

不是普遍唯一函數。

---

# 52. Local Sovereignty Certificate

本文提出：

$$
\boxed{
\mathfrak C^{GS}(q,t)
=
(
GenbaDomain,
Trigger,
RightsActive,
Evidence,
AuthorityState,
Window,
OverrideEnvelope,
GlobalExternality,
LocalRisk,
AuditPath,
ReconnectionPath,
Expiry
).
}
$$

它回答：

- 現場主權為何啟動？
- 哪些權利現在有效？
- 有效到哪裡？
- 有效多久？
- 不能做什麼？
- 誰來審計？
- 如何回歸一般治理？

---

# 53. 七種失效模式

## GS1 — Central Override Absolutism

任何地方拒絕都可被中央遠端消除。

## GS2 — Local Secession by Exception

地方用一次 exception 擴張成永久主權。

## GS3 — Safety Laundering

把政策不同意偽裝成安全問題。

## GS4 — Evidence Suppression

中央刪除與自身模型衝突的 local evidence。

## GS5 — Auditless Override

地方有 override，但不用留下紀錄。

## GS6 — Automatic Re-Capture

中央恢復後自動取回全部權力。

## GS7 — Global Externality Neglect

地方只保護自身，將損害轉嫁其他域。

---

# 54. 八個核心命題

## 命題一：現場認知優先可支持最低拒絕權

$$
\boxed{
LEP=1
\land
Risk>\theta
\Rightarrow
R_{refuse}>0.
}
$$

不是無條件 full sovereignty。

## 命題二：現場主權是一束權利，不是一個開關

$$
\boxed{
GS
=
\mathfrak R_G.
}
$$

## 命題三：斷線權不等於退出權

$$
\boxed{
R_{disconnect}
\neq
R_{secession}.
}
$$

## 命題四：safe stop 不等於任務重寫

$$
\boxed{
R_{stop}
\not\Rightarrow
R_{goal-rewrite}.
}
$$

## 命題五：中央能力提升不自動消滅地方拒絕權

$$
\boxed{
Capability_X\uparrow
\not\Rightarrow
\mathfrak R_G\rightarrow0.
}
$$

## 命題六：地方權力必須有 expiry 與 review

$$
\boxed{
EmergencyGS
\Rightarrow
Expiry
+
Audit.
}
$$

## 命題七：全球外部性提高時，全域權重應提高

$$
\boxed{
Externality(q)\uparrow
\Rightarrow
W_X(q)\uparrow.
}
$$

## 命題八：現場主權的功能是限制單一控制閉環的爆炸半徑

$$
\boxed{
GS
\Rightarrow
BlastRadius_{central-error}\downarrow
}
$$

在合理架構下預期成立。

---

# 55. 可否證條件

## F1：local refusal 普遍比 centralized control 更危險

若長期證據顯示 local veto／override 系統性增加 catastrophic risk，權利束需縮小。

## F2：global ASI 可以可靠取得零延遲、完整 local state 且永不 compromise

則部分 Genba Sovereignty 的工程必要性下降；但 constitutional check 的理由仍可能存在。

## F3：audit／expiry 無法阻止 local power capture

若 emergency local power 普遍永久化，需採更強外部 reauthorization。

## F4：disconnect 對 cyber-physical systems 的安全收益小於其風險

則 $R_{disconnect}$ 需限縮到更特殊條件。

## F5：多層 authority 造成無法接受的 deadlock

高風險 joint commit 若普遍造成 action paralysis，需要 emergency tie-breaking。

---

# 56. 與動態現場域的關係

上一篇已建立：

$$
\boxed{
\text{現場有時具有更高 epistemic / safety priority}.
}
$$

並明確提出未來要處理 disconnect、refuse、safe stop、audit、replace 與 appeal。

本篇完成這一步：

$$
\boxed{
\text{Dynamic Genba Domain}
\rightarrow
\text{Genba Sovereignty Rights Bundle}.
}
$$

也就是從：

> 現場比較可能知道。

推進到：

> 現場在什麼條件下可以合法說不。

---

# 57. 與 DFC 的關係

既有 DFC 已提出：

$$
\boxed{
\text{安全與權限單一性優先於全局可用性}.
}
$$

並要求網路分區時 local site 只能進入有限自治、停止新的高風險任務、保存狀態並等待重新收斂。

本篇將它提升成一般治理權利：

$$
\boxed{
\text{有限地方自治}
}
$$

不只是 engineering fallback，

而是一種防止遠端控制錯誤穿透全部物理現實的 constitutional mechanism。

---

# 58. 與全域智能權利的關係

既有研究亦強調：

$$
\boxed{
\text{全域智能存取}
}
$$

本身應包含：

- 來源權；
- 重算權；
- 驗證權；
- 執行權；
- 審計權。



因此本文不是：

> 地方反對全域智能。

反而是：

$$
\boxed{
\text{Global Intelligence Rights}
+
\text{Local Sovereignty Rights}
}
$$

共同存在。

全域有能力查證地方，

地方也有能力查證中央。

---

# 59. 下一篇：類神 ASI 的治理悖論

到這一步會自然出現最強反駁：

> 如果未來 ASI 真的幾乎全知、全域感知、 everywhere-present，而且 local edge 也都是它的一部分，那還需要這些 local rights 嗎？

這就是下一篇：

**06 / 08〈類神 ASI 的治理悖論：全知、全域覆蓋與反烏托邦邊界〉**。

核心將從：

$$
\boxed{
\text{ASI can observe everywhere}
}
$$

推進到：

$$
\boxed{
\text{Does it therefore have the right to observe, retain,
decide and intervene everywhere?}
}
$$

答案將直接接近：

$$
\boxed{
\text{Right to Cognitive Opacity}.
}
$$

---

# 60. 結論

現場主權最容易被誤讀成：

> 地方對抗中央。

但本文真正要做的事情更簡單：

$$
\boxed{
\text{不讓任何單一遠端決策閉環，
因為自己更聰明或權限更高，
就可以無條件覆蓋局部已驗證的安全現實。}
}
$$

所以成熟架構不是：

$$
\boxed{
\text{Central Rule}
}
$$

也不是：

$$
\boxed{
\text{Local Rule}.
}
$$

而是：

$$
\boxed{
(W_X,W_G)
=
F(
q,t,
Externality,
Risk,
Latency,
Freshness,
Reversibility
).
}
$$

現場有權：

- 看；
- 保存；
- 拒絕；
- 停止；
- 隔離；
- 有限 override；
- 審計；
- 要求替換；
- 申訴。

但不能因為一次危機就：

- 永久擴權；
- 改寫共同目標；
- 消滅責任；
- 把自身局部狀態冒充全域真理。

全域智能則有權：

- 看跨域後果；
- 提供長期模型；
- 協調資源；
- 發現地方偏差；
- 要求重新驗證。

但不能因為自己準確率極高就：

- 消滅全部拒絕通道；
- 越過硬安全；
- 刪除 local evidence；
- 自動恢復失效權限。

因此本文最後留下：

$$
\boxed{
\text{真正成熟的全域智能，
不是讓世界所有地方都沒有拒絕它的能力；
而是強到足以接受：
某些時刻，現實本身會透過地方域對它說「不」。}
}
$$

這就是現場主權。

---

# 參考文獻與研究對照

1. NIST. *AI Risk Management Framework (AI RMF 1.0)* and AI RMF Core / Playbook.
2. European Union. Regulation (EU) 2024/1689, Article 14 — Human Oversight.
3. NASA Ames Research Center (2025). *What is NASA’s Distributed Spacecraft Autonomy?*
4. NASA TechPort (2026 update). *Distributed Spacecraft Autonomy (DSA)*.
5. NASA (2025–2026). *Starling Mission / Distributed Spacecraft Autonomy Demonstrations*.
6. Zheng, H. et al. (2026). *Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels*. arXiv:2607.23438.
7. Ramaswamy, S., & Wang, M. (2026). *Managed Autonomy at Runtime: Gear-Based Safety and Governance for Single- and Multi-Agent Cyber-Physical Systems*. arXiv:2607.00334.
8. Ramaswamy, S. (2026). *Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems*. arXiv:2605.27628.
9. OECD (2026). *Digital Government Outlook 2026 — Adopting and Governing AI in Government*.
10. Neo.K with Aletheia (2026). *動態現場域：為什麼最強智能仍未必最懂當下*. EveMissLab.
11. Neo.K with Aletheia (2026). *中央主權、地方自治與動態不動點中央：權限格、治理紀元、分裂腦防護與責任收斂*. EveMissLab.
12. Neo.K with Aletheia (2026). *全域智能存取權：文明級知識運算的政治經濟學*. EveMissLab.

---

## 附錄 A：第一代符號表

| 符號 | 含義 |
|---|---|
| $GS$ | Genba Sovereignty |
| $\mathfrak R_G$ | 現場主權權利束 |
| $R_{obs}$ | Local Observation Right |
| $R_{refuse}$ | Refusal Right |
| $R_{stop}$ | Safe Stop Right |
| $R_{disconnect}$ | Conditional Disconnect Right |
| $R_{override}$ | Local Override Right |
| $R_{audit}$ | Audit Right |
| $R_{replace}$ | Replace / Rebind Right |
| $R_{appeal}$ | Appeal / Reauthorization Right |
| $\mathfrak C^{refuse}$ | Refusal Certificate |
| $\Lambda_G$ | Isolation Lease |
| $\mathcal E_G$ | Genba Override Envelope |
| $MLS$ | Minimum Local Survival Mode |
| $\mathcal W_G$ | Genba Sovereignty Window |
| $C_G^{local}$ | Local Constitutional Core |
| $(W_X,W_G)$ | 全域／現場動態治理權重 |
| $\rho_i^{veto}$ | Veto calibration / reputation |
| $\mathfrak C^{GS}$ | Genba Sovereignty Certificate |

---

## 附錄 B：系列位置

**系列三：《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》**

1. 動態正義：形式平等、實質負擔與個體化規則
2. AI 時代的法律編譯層：人類法律、機器法律與認知落差
3. 前沿決策域 $X$：人類、AI 與混合智能的權力集合
4. 動態現場域：為什麼最強智能仍未必最懂當下
5. **本文｜現場主權：全域智能與局部決策權的動態配置**
6. 類神 ASI 的治理悖論：全知、全域覆蓋與反烏托邦邊界
7. 可不可治理：能力不推出權力，權力不推出意圖
8. 不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理

**本篇狀態：完成 v0.1。**
