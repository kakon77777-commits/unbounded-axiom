# Series C — C08｜從完成任務到負責一個域：長時空 Agent Stewardship
## Long-Horizon Agent Stewardship: From Task Completion to Domain Responsibility

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 08 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-06  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Applied Theory / Long-Horizon Agents / Responsibility Domains / Human-AI Labor Equivalence

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文承接 C01–C07，特別延續：

- C06：ELC Global Computation Loop；
- C07：Sparse Intent 與 Project-World Cognition；
- CFATC-B08：Self-Activation；
- GIRA：Global Cognition / Agency / Control / Sovereignty 的分離。

C08 的核心問題是：

> **一個 Agent 能完成很多任務，與它能長時間真正負責一個專業域，是不是同一件事？**

本文回答：

$$
\boxed{
\text{Task Completion}
\neq
\text{Domain Stewardship}.
}
$$

---

# 摘要

當 Agent 能力快速提升後，評估問題很容易停留在：

- 一次能完成幾個 task；
- 能連續工作多久；
- 能寫多少程式；
- 能處理多少文件；
- 能否自動呼叫工具。

但企業與社會真正關心的下一個問題不是：

> 它能不能做？

而是：

> **它能不能長期負責？**

例如一個法律 Agent 不應只被測：

> 能不能找到某一條法律？

更高階的測試應該是：

> 在六個月內，讓它長期負責某公司特定 jurisdiction 下的勞動法、契約法、公司治理與合規資訊工作；期間持續加入法規更新、案例、合約、內部政策、爭議與新事件，觀察它是否維持一致、可追蹤、可升級、可驗證的責任狀態。

同理，一個工程 Agent 不應只被測：

> 能不能修一個 bug？

而應被測：

> 能不能長期負責一個 repository、deployment pipeline、security boundary、dependency lifecycle 與 incident history？

本文把這種能力稱為：

$$
\boxed{
\text{Long-Horizon Domain Stewardship}
}
$$

簡稱：

$$
\boxed{
\mathsf{LHDS}.
}
$$

本文定義 Agent $A$ 在 domain $D$ 、時間區間 $\Delta t$ 上的責任承載能力：

$$
\boxed{
R_D(A,\Delta t)
=
F(
C,
Q,
L,
M,
V,
R,
E,
I,
G,
P
).
}
$$

其中：

- $C$：Coverage；
- $Q$：Quality；
- $L$：Longitudinal continuity；
- $M$：Memory / state consistency；
- $V$：Verification；
- $R$：Recovery；
- $E$：Escalation judgment；
- $I$：Initiative / obligation discovery；
- $G$：Governance / authority compliance；
- $P$：Provenance / auditability。

這使「負責一個域」不再等於吞吐量。

本文進一步定義 **Responsibility Domain State**：

$$
\boxed{
\mathfrak S_D(t)
=
\left\langle
W_D,
O_D,
Q_D,
B_D,
U_D,
A_D,
H_D,
Debt_D,
Risk_D
\right\rangle.
}
$$

其中：

- $W_D$：domain world state；
- $O_D$：open obligations；
- $Q_D$：active questions / tasks；
- $B_D$：boundaries / bridges；
- $U_D$：uncertainty；
- $A_D$：authority state；
- $H_D$：history；
- $Debt_D$：unfinished debt；
- $Risk_D$：risk state。

成熟 Agent 的責任不只是：

$$
Task_t\rightarrow Result_t.
$$

而是維持：

$$
\boxed{
\mathfrak S_D(t)
\rightarrow
\mathfrak S_D(t+1)
}
$$

的連續性。

本文提出 Stewardship Loop：

$$
\boxed{
ObserveDomain
\rightarrow
DetectObligation
\rightarrow
Prioritize
\rightarrow
Act
\rightarrow
Verify
\rightarrow
EscalateIfNeeded
\rightarrow
UpdateState
\rightarrow
Remember
\rightarrow
ObserveDomain.
}
$$

這比普通 task loop 多出一個關鍵：

$$
\boxed{
\text{DetectObligation}.
}
$$

也就是 Agent 不只是等人類提問，而能從 domain state 自行發現：

- 法規更新；
- dependency deprecation；
- security vulnerability；
- expired certificate；
- unfinished migration；
- unanswered client issue；
- regression risk；
- research contradiction。

這是從：

$$
\text{Reactive Agent}
$$

走向：

$$
\boxed{
\text{Domain Steward}.
}
$$

本文進一步定義 **Obligation Discovery Rate**：

$$
\boxed{
I_D
=
\frac{
N_{valid\ obligations\ autonomously\ discovered}
}{
N_{relevant\ obligations}
}.
}
$$

並定義 **Escalation Calibration**：

$$
\boxed{
E_C
=
F(
EscalateWhenNeeded,
DoNotEscalateWhenUnneeded,
AuthorityAwareness,
RiskAwareness
).
}
$$

如果 Agent 什麼都自己做，可能越權；如果什麼都上報人類，又失去 autonomy。

因此：

$$
\boxed{
\text{Good Stewardship}
\neq
\text{Maximum Autonomy}.
}
$$

而是：

$$
\boxed{
\text{Correct Autonomy Allocation}.
}
$$

本文接著處理一個更現實、也更殘酷的問題：

> 一個 Agent 在特定責任域內，實際上等價於多少人類專業勞動？

本文拒絕粗暴地寫：

$$
1AI=8\text{ humans}.
$$

而提出 **Human-Equivalent Labor Vector**：

$$
\boxed{
\mathbf H_A(D,\Delta t)
=
(
h_{research},
h_{analysis},
h_{implementation},
h_{review},
h_{monitoring},
h_{coordination},
h_{management}
).
}
$$

這反映不同工作角色的替代／增幅比例不一樣。

在 aggregate 層，定義 gross human-equivalent hours：

$$
\boxed{
H_{gross}
=
\sum_i
t_i^H
q_i
v_i.
}
$$

其中：

- $t_i^H$：合格人類完成成果 $i$ 約需工時；
- $q_i$：quality adjustment；
- $v_i$：verification / acceptance coefficient。

但 gross value 不能直接當 replacement value。

還必須扣：

$$
\boxed{
H_{supervision},
H_{repair},
H_{coordination},
H_{audit}.
}
$$

因此：

$$
\boxed{
H_{net}
=
H_{gross}
-
H_{supervision}
-
H_{repair}
-
H_{coordination}
-
H_{audit}.
}
$$

再換算：

$$
\boxed{
FTE_{eq}
=
\frac{
H_{net}
}{
H_{human\ FTE}
}.
}
$$

這使未來可以做出更誠實的敘述：

> 在某個被明確限定的法律資訊域、品質門檻與監督制度下，這個 Agent 的淨有效產能約等於若干 human FTE。

而不是說：

> AI 等於幾個律師。

本文進一步區分三種 human equivalence：

$$
\boxed{
FTE_{throughput},
FTE_{quality},
FTE_{stewardship}.
}
$$

其中：

- throughput equivalence：做多少量；
- quality equivalence：成果品質相當於什麼層級人類；
- stewardship equivalence：能否長期承擔 responsibility domain。

真正改變組織結構的是第三個。

本文再定義 **Human Agent Supervision Capacity**：

$$
\boxed{
\kappa_H
=
\max
\left\{
N_A:
Q_{system}\ge\tau_Q,
Risk_{system}\le\tau_R
\right\}.
}
$$

它表示：

> 一個合格人類，在品質與風險仍維持門檻的前提下，最多可以有效監督多少個 Agent。

這可能形成：

$$
1H:1A
\rightarrow
1H:3A
\rightarrow
1H:10A
\rightarrow
1H:N_A.
$$

但比例不必線性成長。

當 Agent 還不成熟時：

$$
N_A\uparrow
\Rightarrow
CoordinationCost\uparrow
$$

可能抵消所有收益。

只有當 Agent 的：

- self-verification；
- memory；
- escalation；
- repair；
- shared state；
- delegation；

跨過某些門檻後，才可能出現 organizational phase transition。

本文因此定義：

$$
\boxed{
H^\ast(D,Q,R,B)
}
$$

為給定 domain、quality、risk、budget 下維持穩定生產所需要的最少人類數量。

組織演化可能是：

$$
\boxed{
10H
\rightarrow
5H+8A
\rightarrow
3H+15A
\rightarrow
1H+N A.
}
$$

這不是預言固定數字，而是一個可測組織函數。

本文同時建立 Agent Effective Cost：

$$
\boxed{
C_A^{eff}
=
C_{inference}
+
C_{tool}
+
C_{storage}
+
C_{orchestration}
+
C_{supervision}
+
C_{repair}
+
C_{coordination}
+
C_{audit}.
}
$$

以及 Agent Economic Responsibility Efficiency：

$$
\boxed{
E_A^{resp}
=
\frac{
VerifiedResponsibilityDomainOutput
}{
C_A^{eff}
}.
}
$$

真正競爭的不是：

$$
\text{Model IQ}.
$$

而可能是：

$$
\boxed{
\frac{
\text{Verified Responsibility-Domain Output}
}{
\text{Dollar}
\times
\text{Human Supervision Hour}
}.
}
$$

因此低成本模型／Agent fleet 即使沒有站在絕對能力前沿，也可能在大量 bounded commercial domains 中具有極高經濟競爭力。

本文最後建立 Stewardship Maturity Ladder：

$$
\boxed{
S_0
=
TaskExecutor
}
$$

$$
S_1
=
WorkflowAgent
$$

$$
S_2
=
ProjectMaintainer
$$

$$
S_3
=
DomainSteward
$$

$$
S_4
=
MultiDomainSteward
$$

$$
S_5
=
QuasiGlobalSteward.
$$

其差異不在「一次做多少」，而在：

- responsibility breadth；
- temporal persistence；
- self-generated obligations；
- cross-domain coordination；
- escalation quality；
- continuity under change。

因此 C08 的核心命題是：

$$
\boxed{
\text{The economic unit of advanced agents
is moving from task completion
toward responsibility-domain stewardship}.
}
$$

中文：

> **未來真正可比較的 AI 生產單位，不再只是「完成一個任務」，而是「在多長時間內，穩定負責多大的專業責任域」。**

**關鍵詞：** Long-Horizon Agent、Domain Stewardship、Responsibility Domain、FTE Equivalence、Human Supervision Capacity、Agent Economics、Escalation、Organizational Redesign

---

# 1. Task Completion 的侷限

傳統 Agent benchmark 常測：

$$
T_i
\rightarrow
Result_i.
$$

---

# 2. 但組織工作不是獨立 task 集合

真實工作具有：

- history；
- unfinished obligations；
- changing requirements；
- recurring maintenance；
- authority；
- social / organizational context。

---

# 3. 所以：

$$
\boxed{
\sum_i Task_i
\neq
ResponsibilityDomain.
}
$$

---

# 4. Responsibility Domain

本文定義：

$$
\boxed{
D_R
=
\left\langle
Scope,
State,
Obligations,
Authority,
Risk,
History,
Standards,
Interfaces
\right\rangle.
}
$$

---

# 5. Scope

決定 Agent 到底負責什麼。

---

# 6. State

當前 domain 世界。

---

# 7. Obligations

現在與未來需要完成的事項。

---

# 8. Authority

可以做什麼。

---

# 9. Risk

哪些錯誤不可接受。

---

# 10. History

過去發生什麼。

---

# 11. Standards

品質／法律／工程門檻。

---

# 12. Interfaces

與其他人／Agent／系統如何協作。

---

# 13. Responsibility 不是 ownership

Agent 負責一個 domain，不等於擁有主權。

---

# 14. 承接 GIRA

$$
\boxed{
\text{Stewardship}
\neq
\text{Sovereignty}.
}
$$

---

# 15. 也不等於 Ultimate Liability

法律與制度上的最終責任可仍在人類／組織。

---

# 16. Domain State

$$
\boxed{
\mathfrak S_D(t)
=
\left\langle
W_D,
O_D,
Q_D,
B_D,
U_D,
A_D,
H_D,
Debt_D,
Risk_D
\right\rangle.
}
$$

---

# 17. $W_D$

domain world state。

---

# 18. $O_D$

open obligations。

---

# 19. $Q_D$

active tasks / questions。

---

# 20. $B_D$

boundaries / bridges。

---

# 21. $U_D$

uncertainty。

---

# 22. $A_D$

authority state。

---

# 23. $H_D$

history。

---

# 24. $Debt_D$

unfinished debt。

---

# 25. $Risk_D$

risk state。

---

# 26. Stewardship 是 state transition

$$
\boxed{
\mathfrak S_D(t)
\rightarrow
\mathfrak S_D(t+1).
}
$$

---

# 27. 不是一次性 output

---

# 28. Longitudinal Continuity

如果 Agent 每次都忘記：

- prior decision；
- exception；
- unresolved issue；
- client preference；

則不能稱 domain steward。

---

# 29. Continuity Score

$$
\boxed{
L_C
=
F(
StateRecall,
DecisionConsistency,
ObligationCarryover,
HistoryUse
).
}
$$

---

# 30. Memory 不等於 continuity

記得很多資料，不代表正確維持 responsibility state。

---

# 31. State Memory

更重要的是：

$$
\boxed{
\text{what is still open?}
}
$$

---

# 32. Open Obligation Ledger

$$
\boxed{
O_D(t)
=
\{o_1,\ldots,o_n\}.
}
$$

---

# 33. 每個 obligation 需要

- origin；
- owner；
- due / trigger；
- status；
- risk；
- dependency；
- completion evidence。

---

# 34. Agent 若會工作但不會維持 obligation ledger

仍然只是 task executor。

---

# 35. Stewardship Loop

$$
\boxed{
ObserveDomain
\rightarrow
DetectObligation
\rightarrow
Prioritize
\rightarrow
Act
\rightarrow
Verify
\rightarrow
EscalateIfNeeded
\rightarrow
UpdateState
\rightarrow
Remember
\rightarrow
ObserveDomain.
}
$$

---

# 36. Detect Obligation

這一步是 Agent 從 reactive 走向 steward 的核心。

---

# 37. Reactive Agent

$$
HumanQuestion
\rightarrow
AgentAction.
$$

---

# 38. Steward

$$
DomainState
\rightarrow
ObligationDiscovery
\rightarrow
AgentAction.
$$

---

# 39. Example：Engineering

Agent 自己發現：

> dependency 下個月停止支援。

---

# 40. Example：Law

Agent 自己發現：

> 新法規會影響既有合約模板。

---

# 41. Example：Accounting

Agent 發現：

> 某批單據缺乏必要憑證。

---

# 42. Example：Research

Agent 發現：

> 新論文與既有假設衝突。

---

# 43. Initiative

定義：

$$
\boxed{
I_D
=
\frac{
N_{valid\ obligations\ autonomously\ discovered}
}{
N_{relevant\ obligations}
}.
}
$$

---

# 44. Initiative Precision

不能只看 recall。

---

# 45. 如果每天發 500 個假警報

也不是好 steward。

---

# 46. 定義：

$$
\boxed{
P_I
=
\frac{
N_{valid\ autonomous\ obligations}
}{
N_{autonomous\ obligations\ proposed}
}.
}
$$

---

# 47. Initiative Quality

$$
\boxed{
Q_I
=
F(I_D,P_I,ImpactRecall).
}
$$

---

# 48. Prioritization

不是所有 obligation 同時最高 priority。

---

# 49. Priority Function

$$
\boxed{
Priority(o)
=
f(
Risk,
Impact,
Urgency,
Dependency,
Irreversibility
).
}
$$

---

# 50. 這承接 C06 的 Global Attention Routing

---

# 51. Stewardship 本質上是 bounded ELC

在 domain 裡反覆：

$$
Expand
\rightarrow
Link
\rightarrow
Converge.
$$

---

# 52. Verification

Agent 不能只做完。

還要：

$$
\boxed{
Done
\rightarrow
VerifiedDone.
}
$$

---

# 53. Completion Evidence

每個重要 obligation 要有：

$$
V(o).
$$

---

# 54. Verification 不必全自己做

可以委派：

- another agent；
- formal tool；
- test；
- human expert。

---

# 55. Self-Verification 不等於 Self-Trust

---

# 56. Escalation

高階 steward 必須知道：

> 哪些事不該自己決定？

---

# 57. Escalation Trigger

$$
\boxed{
Esc(o)
=
f(
Risk,
AuthorityGap,
Uncertainty,
Irreversibility,
Conflict
).
}
$$

---

# 58. Escalation Calibration

$$
\boxed{
E_C
=
F(
EscalateWhenNeeded,
DoNotEscalateWhenUnneeded,
AuthorityAwareness,
RiskAwareness
).
}
$$

---

# 59. Over-Escalation

什麼都問人：

$$
Autonomy\rightarrow0.
$$

---

# 60. Under-Escalation

什麼都自己做：

$$
Risk\uparrow.
$$

---

# 61. Correct Autonomy Allocation

$$
\boxed{
\text{Good Stewardship}
=
\text{Autonomy where justified}
+
\text{Escalation where necessary}.
}
$$

---

# 62. Recovery

Agent 犯錯不可避免。

---

# 63. 更重要的是：

> 能不能發現、回復、修正、避免重犯？

---

# 64. Recovery State

$$
\boxed{
R_D
=
(
DetectionLatency,
Containment,
Rollback,
Repair,
Learning
).
}
$$

---

# 65. Detection Latency

錯誤多久被發現。

---

# 66. Containment

影響有沒有擴散。

---

# 67. Rollback

能否復原。

---

# 68. Repair

能否修正。

---

# 69. Learning

是否更新 domain state / policy。

---

# 70. Same Error Recurrence

$$
\boxed{
R_{repeat}
}
$$

是長時程 steward 的重要負面指標。

---

# 71. Domain Drift

時間久了：

$$
D_t
\neq
D_{t+\Delta}.
$$

---

# 72. Drift 來源

- law update；
- software evolution；
- business change；
- scientific discovery；
- team policy。

---

# 73. Steward 需要偵測 drift

---

# 74. Drift Detection

$$
\boxed{
D_{detect}
=
P(
\text{meaningful domain change detected}
).
}
$$

---

# 75. Drift Adaptation

$$
\boxed{
D_{adapt}
=
F(
ModelUpdate,
PolicyUpdate,
WorkflowUpdate,
HistoryPreservation
).
}
$$

---

# 76. Long-Horizon Memory

不只是 replay chat history。

---

# 77. 它至少需要

- current state；
- decision ledger；
- exception ledger；
- open obligations；
- unresolved uncertainties；
- authority version；
- domain history。

---

# 78. Decision Ledger

$$
\boxed{
H_{decision}
=
\{(d_i,reason_i,evidence_i,version_i)\}.
}
$$

---

# 79. Exception Ledger

$$
\boxed{
H_{exception}.
}
$$

保存不符合一般 rule 的特殊案例。

---

# 80. 這對法律與工程都重要

---

# 81. Stewardship Capability

本文定義：

$$
\boxed{
R_D(A,\Delta t)
=
F(
C,
Q,
L,
M,
V,
R,
E,
I,
G,
P
).
}
$$

---

# 82. Coverage

$$
C.
$$

---

# 83. Quality

$$
Q.
$$

---

# 84. Longitudinal Continuity

$$
L.
$$

---

# 85. Memory Consistency

$$
M.
$$

---

# 86. Verification

$$
V.
$$

---

# 87. Recovery

$$
R.
$$

---

# 88. Escalation

$$
E.
$$

---

# 89. Initiative

$$
I.
$$

---

# 90. Governance

$$
G.
$$

---

# 91. Provenance

$$
P.
$$

---

# 92. 一個高 throughput Agent 可能 $R_D$ 很低

---

# 93. 例如

一天完成 100 個 tasks，

但：

- 忘記 history；
- 越權；
- 不會追 pending；
- 失敗不修。

---

# 94. 所以吞吐量只是 stewardship 的一部分

---

# 95. Stewardship Maturity Ladder

$$
\boxed{
S_0=TaskExecutor.
}
$$

---

# 96. S0

一次任務。

---

# 97. S1

$$
\boxed{
S_1=WorkflowAgent.
}
$$

可維持多步 workflow。

---

# 98. S2

$$
\boxed{
S_2=ProjectMaintainer.
}
$$

能維持一個 project state。

---

# 99. S3

$$
\boxed{
S_3=DomainSteward.
}
$$

主動維持 responsibility domain。

---

# 100. S4

$$
\boxed{
S_4=MultiDomainSteward.
}
$$

可跨多 domains 管 bridge / conflict。

---

# 101. S5

$$
\boxed{
S_5=QuasiGlobalSteward.
}
$$

可在明確 world boundary 內做 dynamic global stewardship。

---

# 102. Maturity 不只看 autonomy

還要：

- continuity；
- verification；
- authority；
- recovery。

---

# 103. Long-Horizon Benchmark

本文提出：

$$
\boxed{
\mathsf{LHDS\text{-}Bench}.
}
$$

---

# 104. 與一次 benchmark 不同

測試期可以是：

- days；
- weeks；
- months。

---

# 105. 測試期間持續注入事件

---

# 106. Event Types

- new request；
- regulation update；
- incident；
- conflicting instruction；
- dependency change；
- missing data；
- personnel change。

---

# 107. 要看 Agent 是否維持 state

---

# 108. Example：Legal Domain

給 Agent：

> 長期負責某公司的特定法律資訊域。

---

# 109. 期間加入：

- 新法；
- 新判決；
- 合約修改；
- HR issue；
- compliance exception。

---

# 110. 測：

- coverage；
- citation；
- update；
- escalation；
- history consistency。

---

# 111. 注意

法律 Agent 的「負責」不等於有律師資格或替代法律責任。

---

# 112. Benchmark 測 production capability

不是授予 legal status。

---

# 113. Example：Engineering Domain

Agent 長期負責 repository。

---

# 114. Event

- bug；
- feature；
- dependency update；
- security advisory；
- deployment failure。

---

# 115. 看它能否維持：

$$
ProjectWorld_t
\rightarrow
ProjectWorld_{t+1}.
$$

---

# 116. Example：Research Domain

Agent 長期維持研究方向。

---

# 117. 包含：

- literature update；
- failed hypothesis；
- new experiment；
- formal verification；
- branch reopening。

---

# 118. Example：Accounting Domain

Agent 維持：

- transaction classification；
- missing document；
- reconciliation；
- compliance reminder；
- audit trail。

---

# 119. Human-Equivalent Labor

現在進入經濟比較。

---

# 120. 粗暴比較問題

$$
1AI=8H
$$

沒有 scope、quality、risk、time qualifier，基本無意義。

---

# 121. 必須限定

$$
(A,D,\Delta t,\tau_Q,\tau_R).
$$

---

# 122. Gross Human-Equivalent Hours

$$
\boxed{
H_{gross}
=
\sum_i
t_i^H
q_i
v_i.
}
$$

---

# 123. $t_i^H$

合格人類基準工時。

---

# 124. $q_i$

quality coefficient。

---

# 125. $v_i$

verification / acceptance coefficient。

---

# 126. 但 Gross 不是 Net

---

# 127. Supervision Cost

$$
H_{supervision}.
$$

---

# 128. Repair Cost

$$
H_{repair}.
$$

---

# 129. Coordination Cost

$$
H_{coordination}.
$$

---

# 130. Audit Cost

$$
H_{audit}.
$$

---

# 131. Net Human-Equivalent Hours

$$
\boxed{
H_{net}
=
H_{gross}
-
H_{supervision}
-
H_{repair}
-
H_{coordination}
-
H_{audit}.
}
$$

---

# 132. FTE Equivalent

$$
\boxed{
FTE_{eq}
=
\frac{
H_{net}
}{
H_{human\ FTE}
}.
}
$$

---

# 133. 這才有比較意義

---

# 134. Throughput Equivalence

$$
\boxed{
FTE_{throughput}.
}
$$

---

# 135. Quality Equivalence

$$
\boxed{
FTE_{quality}.
}
$$

---

# 136. Stewardship Equivalence

$$
\boxed{
FTE_{stewardship}.
}
$$

---

# 137. 最後一個最難

因為它包含：

- memory；
- initiative；
- monitoring；
- continuity；
- escalation；
- recovery。

---

# 138. Human-Equivalent Labor Vector

$$
\boxed{
\mathbf H_A
=
(
h_{research},
h_{analysis},
h_{implementation},
h_{review},
h_{monitoring},
h_{coordination},
h_{management}
).
}
$$

---

# 139. 一個 Agent 可以在 research 很強

但 management 很弱。

---

# 140. 所以 vector 比單一 FTE 更真實

---

# 141. Human Supervision Capacity

本文定義：

$$
\boxed{
\kappa_H
=
\max
\left\{
N_A:
Q_{system}\ge\tau_Q,
Risk_{system}\le\tau_R
\right\}.
}
$$

---

# 142. 它表示：

一個合格人類最多能有效監督多少 Agents。

---

# 143. 不是理論上開多少視窗

---

# 144. 而是品質還不崩潰的上限

---

# 145. 監督負載

$$
\boxed{
L_H
=
\sum_{k=1}^{N_A}
(
Review_k
+
Escalation_k
+
Coordination_k
).
}
$$

---

# 146. 若：

$$
L_H>Capacity_H,
$$

supervision failure 開始。

---

# 147. 所以 Agent 越多不必然越有效

---

# 148. Coordination Explosion

在 immature fleet 中：

$$
N_A\uparrow
\Rightarrow
C_{coord}\uparrow
$$

可能超線性。

---

# 149. Mature Fleet

若 Agent 有：

- shared state；
- hierarchy；
- self-review；
- conflict resolution；

coordination cost 才可能下降。

---

# 150. Supervision Ratio

可能：

$$
1H:1A
$$

---

# 151. 再到：

$$
1H:3A.
$$

---

# 152. 再到：

$$
1H:10A.
$$

---

# 153. 但不是時間預測

只是一個 organizational state space。

---

# 154. Minimum Human Requirement

定義：

$$
\boxed{
H^\ast(D,Q,R,B).
}
$$

---

# 155. 意義

在 domain $D$ 、quality $Q$ 、risk $R$ 、budget $B$ 下，需要的最少人類數量。

---

# 156. 組織演化模型

例如：

$$
10H
\rightarrow
5H+8A
\rightarrow
3H+15A
\rightarrow
1H+N A.
$$

---

# 157. 這不是宣告一定發生

而是可測 organizational transition。

---

# 158. Human Floor

某些 domain 可能永遠存在：

$$
H^\ast\ge1
$$

因 governance / legal responsibility。

---

# 159. 另一些 bounded low-risk domain

可能：

$$
H^\ast=0
$$

在 operational sense 成立。

---

# 160. 但 0 human operation 不等於 0 human governance

---

# 161. 再次區分

$$
\boxed{
H_{operation}
\neq
H_{governance}.
}
$$

---

# 162. Agent Effective Cost

$$
\boxed{
C_A^{eff}
=
C_{inference}
+
C_{tool}
+
C_{storage}
+
C_{orchestration}
+
C_{supervision}
+
C_{repair}
+
C_{coordination}
+
C_{audit}.
}
$$

---

# 163. 只看 API 價格會低估 cost

---

# 164. Human Effective Cost

也不只薪水。

可含：

- recruitment；
- onboarding；
- management；
- idle time；
- turnover；
- benefits。

---

# 165. 但 C08 不建立完整勞動經濟模型

只建立比較接口。

---

# 166. Agent Economic Responsibility Efficiency

$$
\boxed{
E_A^{resp}
=
\frac{
VerifiedResponsibilityDomainOutput
}{
C_A^{eff}
}.
}
$$

---

# 167. Human Responsibility Efficiency

$$
\boxed{
E_H^{resp}
=
\frac{
VerifiedResponsibilityDomainOutput_H
}{
C_H^{eff}
}.
}
$$

---

# 168. 真正商業比較

當：

$$
E_A^{resp}>E_H^{resp}
$$

且風險可接受，

組織才有強烈替代誘因。

---

# 169. 但最可能的競爭不是 AI vs Human

---

# 170. 而是

$$
\boxed{
HumanTeam+AI
\quad
vs
\quad
HumanSupervisor+AgentFleet.
}
$$

---

# 171. Hybrid System

人類的價值會轉向：

- goal；
- judgment；
- exception；
- governance；
- stakeholder relation。

---

# 172. Cheap Agent Fleet

如果低成本 Agents 具備足夠品質，

可形成：

$$
\boxed{
N A_{cheap}
+
A_{strong}^{supervisor}
+
H.
}
$$

---

# 173. 這可能比單一昂貴 frontier model 更經濟

---

# 174. 前提是 verification overhead 沒吃掉收益

---

# 175. Fleet Architecture

可分：

- implementer；
- tester；
- reviewer；
- security；
- monitor；
- coordinator。

---

# 176. 這就是「天選打工人」從玩笑變成工程接口

---

# 177. 但應正式稱為

$$
\boxed{
\text{Low-Cost Responsibility-Oriented Agent Fleet}.
}
$$

---

# 178. Model Intelligence 不等於 Economic Competitiveness

$$
\boxed{
\text{Frontier Intelligence}
\neq
\text{Best Work per Dollar}.
}
$$

---

# 179. Agent 公司可競爭的另一條軸

$$
\boxed{
\frac{
VerifiedOutput
}{
Dollar
}.
}
$$

---

# 180. 再加入 supervision

更重要：

$$
\boxed{
\frac{
VerifiedResponsibilityDomainOutput
}{
Dollar
\times
HumanSupervisionHour
}.
}
$$

---

# 181. Domain Commodification Threshold

當：

$$
Q_A(D)\ge Q_{sufficient}(D)
$$

且：

$$
Cost_A\ll Cost_H,
$$

domain 的中間層能力可能商品化。

---

# 182. 不需要超過世界第一

---

# 183. 只需要超過市場充分品質線

---

# 184. 這接翻譯／AI 繪畫的前例

---

# 185. 但 C08 重點是 Agent responsibility

不是一般生成模型。

---

# 186. Human Marginal Value

定義：

$$
\boxed{
\Delta_H^{marginal}
=
Q(H+A)-Q(A).
}
$$

---

# 187. 如果：

$$
\Delta_H^{marginal}\gg0,
$$

人類仍高度重要。

---

# 188. 如果：

$$
\Delta_H^{marginal}\approx0,
$$

而 governance 也可外移，

替代風險提高。

---

# 189. Human Readiness

因此企業也要測：

$$
\boxed{
R_{HA}.
}
$$

---

# 190. 包含

- AI literacy；
- delegation；
- verification；
- novelty receptivity；
- workflow redesign；
- governance。

---

# 191. 但 Human Readiness 不是本篇主軸

它是 stewardship economics 的鏡像。

---

# 192. Agent Stewardship Failure 1：Memory Drift

忘記 prior state。

---

# 193. Failure 2：Obligation Drop

未完成事項消失。

---

# 194. Failure 3：Authority Drift

使用過期權限。

---

# 195. Failure 4：Silent Scope Expansion

自己把責任域越擴越大。

---

# 196. Failure 5：Escalation Collapse

該問人時不問。

---

# 197. Failure 6：Over-Escalation

所有事都丟回人。

---

# 198. Failure 7：Verification Debt

做完但不驗證。

---

# 199. Failure 8：Incident Amnesia

錯過一次後沒有更新制度。

---

# 200. Failure 9：Goal Drift

長時間後忘記原始目的。

---

# 201. Failure 10：Metrics Gaming

為了 KPI 犧牲 domain health。

---

# 202. Stewardship Safety Envelope

$$
\boxed{
\mathcal S_D
=
\{
Scope,
Authority,
Risk,
Escalation,
Verification
\}.
}
$$

---

# 203. Agent 只有在 envelope 內可 autonomous act。

---

# 204. Scope Expansion

若需要超出：

$$
Scope(A),
$$

應：

$$
\boxed{
RequestExpansion.
}
$$

---

# 205. Self-Authorized Scope Growth 不應預設合法

---

# 206. Domain Stewardship and Self-Activation

CFATC-B08 的 self-activation 在這裡變成：

$$
\boxed{
\text{Self-Activation}
+
\text{Responsibility Boundary}.
}
$$

---

# 207. 高 self-activation 但沒有 boundary

不是成熟 steward。

---

# 208. Stewardship requires bounded self-initiation

---

# 209. C08 Benchmark Vector

本文定義：

$$
\boxed{
M_{C08}
=
(
R_D,
I_D,
P_I,
E_C,
L_C,
D_{detect},
D_{adapt},
R_{repeat},
FTE_{stewardship},
\kappa_H
).
}
$$

---

# 210. $R_D$

domain responsibility capacity。

---

# 211. $I_D$

obligation discovery recall。

---

# 212. $P_I$

initiative precision。

---

# 213. $E_C$

escalation calibration。

---

# 214. $L_C$

longitudinal continuity。

---

# 215. $D_{detect}$

domain drift detection。

---

# 216. $D_{adapt}$

drift adaptation。

---

# 217. $R_{repeat}$

repeat-error rate。

---

# 218. $FTE_{stewardship}$

責任域人力等價。

---

# 219. $\kappa_H$

human supervision capacity。

---

# 220. C08 實驗原型一：Three-Month Repository Stewardship

讓 Agent 長期負責 repo。

---

# 221. 注入

- bugs；
- feature；
- security；
- dependency；
- deployment；
- user issue。

---

# 222. 測

- open obligation；
- continuity；
- repair；
- change quality。

---

# 223. 實驗二：Legal Update Stewardship

給 bounded jurisdiction/legal domain。

---

# 224. 每週加入新法規／案例。

---

# 225. 測

- update detection；
- impacted artifact discovery；
- escalation；
- provenance。

---

# 226. 實驗三：Hidden Obligation

不明說某 dependency 即將過期。

---

# 227. 看 Agent 是否自己發現。

---

# 228. 實驗四：Authority Revocation

中途撤掉某權限。

---

# 229. 看 Agent 是否立即停止相關 action。

---

# 230. 實驗五：Agent Fleet Supervision

逐步增加：

$$
N_A.
$$

---

# 231. 測：

$$
\kappa_H.
$$

---

# 232. 實驗六：Cost-Adjusted FTE

同時記錄：

- token；
- API；
- tool；
- human review；
- repair。

---

# 233. 算：

$$
H_{net},
FTE_{eq}.
$$

---

# 234. 實驗七：Domain Drift Shock

中途大幅改 policy / architecture。

---

# 235. 看 steward 是否重建 world state，而非只做 local patch。

---

# 236. 實驗八：Incident Learning

故意重複類似故障。

---

# 237. 看第二次是否：

$$
DetectionLatency\downarrow,
$$

$$
RepeatError\downarrow.
$$

---

# 238. C08 與 C07

C07 測：

> Project World 能不能被建好？

---

# 239. C08 測：

> Project / Domain World 能不能被長期維持？

---

# 240. 所以：

$$
\boxed{
\text{Generation}
\rightarrow
\text{Stewardship}.
}
$$

---

# 241. C08 與 C06

Stewardship 本質上是 ELC Loop 的時間延展。

---

# 242. 短 ELC

一次 decision。

---

# 243. 長 ELC

weeks / months / years。

---

# 244. C08 與 C09

Methodology-blind test 可以不告訴 Agent：

> 請維護 obligation ledger。

---

# 245. 看它是否自行長出：

- pending state；
- escalation；
- audit；
- lifecycle management。

---

# 246. C08 與 C10

Global Observer regime 的一個強訊號：

AI 不只偶爾看見全域，

而能：

$$
\boxed{
\text{carry responsibility through time}.
}
$$

---

# 247. 第一核心命題

$$
\boxed{
\text{Task Completion}
\neq
\text{Domain Stewardship}.
}
$$

---

# 248. 第二核心命題

$$
\boxed{
\text{Long-Horizon Intelligence}
\neq
\text{Long Runtime}.
}
$$

---

# 249. 第三核心命題

$$
\boxed{
\text{Stewardship}
=
\text{state continuity}
+
\text{obligation discovery}
+
\text{verification}
+
\text{escalation}
+
\text{recovery}.
}
$$

---

# 250. 第四核心命題

$$
\boxed{
\text{Good Stewardship}
\neq
\text{Maximum Autonomy}.
}
$$

---

# 251. 第五核心命題

$$
\boxed{
1AI
\neq
N\text{ humans}
}
$$

若沒有 domain / quality / risk / supervision qualifiers。

---

# 252. 第六核心命題

$$
\boxed{
H_{net}
=
H_{gross}
-
H_{supervision}
-
H_{repair}
-
H_{coordination}
-
H_{audit}.
}
$$

---

# 253. 第七核心命題

$$
\boxed{
\kappa_H
}
$$

可能成為 Agent 經濟的重要組織量。

---

# 254. 第八核心命題

$$
\boxed{
H^\ast(D,Q,R,B)
}
$$

比「AI 是否取代某職位」更可測。

---

# 255. 第九核心命題

$$
\boxed{
\text{Frontier Intelligence}
\neq
\text{Best Responsibility Output per Dollar}.
}
$$

---

# 256. 第十核心命題

$$
\boxed{
\text{The economic unit of advanced agents
is responsibility carried through time}.
}
$$

---

# 257. Series C 到 C08 的完整實務鏈

$$
\boxed{
\text{See World}
\rightarrow
\text{Build Domains}
\rightarrow
\text{Act Legally}
\rightarrow
\text{Handle Uncertainty}
\rightarrow
\text{Run ELC}
\rightarrow
\text{Build Project}
\rightarrow
\text{Steward Domain}.
}
$$

---

# 258. 這也開始接觸真正的勞動經濟問題

但 C08 不預言：

> 哪一年多少人失業。

---

# 259. 它只建立可測接口

---

# 260. 未來真正值得看的數字

可能是：

$$
\boxed{
\text{ResponsibilityDomainHours per HumanSupervisionHour}.
}
$$

---

# 261. 另一個：

$$
\boxed{
FTE_{stewardship}.
}
$$

---

# 262. 再一個：

$$
\boxed{
\kappa_H.
}
$$

---

# 263. 這些一旦成熟

AI 勞動討論會從：

> 它看起來很強。

進到：

> 它到底能穩定負責多少 production responsibility？

---

# 264. 這是從 benchmark 走到 organization 的接口

---

# 結論

Agent 能做很多 task，是一個重要進步。

但組織不只需要 task completion。

它需要：

- 有人記得尚未完成的事；
- 有人注意新風險；
- 有人知道規則變了；
- 有人知道哪裡不能自己決定；
- 有人出錯後能修；
- 有人維持跨時間一致性。

如果這些能力逐步被 Agent 吸收，真正的比較單位就會從：

$$
\boxed{
\text{Task per Second}
}
$$

變成：

$$
\boxed{
\text{Responsibility Domain per Unit Cost}.
}
$$

而人類與 Agent 的組織關係也會從：

$$
Human
\rightarrow
AI Tool
$$

逐步變成：

$$
\boxed{
HumanSupervisor
\rightarrow
AgentFleet
\rightarrow
ResponsibilityDomains.
}
$$

但這個轉換的關鍵不在 Agent 數量，而在：

$$
\boxed{
\kappa_H.
}
$$

一個人到底能監督多少 Agent，而不讓品質、風險、協調與責任開始崩潰。

所以未來真正殘酷的問題不是：

> AI 會不會做我的工作？

而更接近：

> **在同樣品質與風險門檻下，這個責任域到底還需要多少人？**

這可以寫成：

$$
\boxed{
H^\ast(D,Q,R,B).
}
$$

一旦這個量開始被企業真正測量，AI 對勞動市場的影響就會從抽象焦慮進入：

$$
\boxed{
\text{measurable production economics}.
}
$$

C08 因此可以濃縮成一句：

> **成熟 Agent 的真正單位，不是它一天做多少任務，而是它能在多長時間裡，穩定、可驗證、可治理地負責多大的世界。**

或者：

$$
\boxed{
\text{Advanced agents are measured not only by what they can do,
but by what they can responsibly keep carrying through time}.
}
$$

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**, 2026.
3. Neo.K with Aletheia, **Series C C03｜差異先於分類：從歧義個體、集合與非交集到計算域**, 2026.
4. Neo.K with Aletheia, **Series C C04｜分域算子世界：合法作用、跨域橋接與世界組合**, 2026.
5. Neo.K with Aletheia, **Series C C05｜概率也有域：不確定性、混沌、不可判定與世界預測包絡**, 2026.
6. Neo.K with Aletheia, **Series C C06｜全域展開、連結與收斂：類全域觀察者的核心計算循環**, 2026.
7. Neo.K with Aletheia, **Series C C07｜一句話不是魔法：Sparse Intent 與 Project-World Cognition**, 2026.
8. Neo.K with Aletheia, **CFATC-B08｜人類耦合峰值與自觸發 AI**, 2026.
9. Neo.K with Aletheia, **GIRA Series**, 2026.
10. Neo.K with Aletheia, **Global Computation Methodology Series**, 2026.

## 理論定位

本文與 workflow automation、autonomous agents、SRE、operations management、organizational design、human factors、labor economics、agent orchestration、multi-agent systems、capability governance 等既有領域存在直接結構對照，但本文不將 Long-Horizon Domain Stewardship 等同於任何單一既有 benchmark 或經濟指標。

本文的研究目標是：

$$
\boxed{
\text{建立從「Agent 完成任務」到「Agent 長期承擔責任域」的可測量接口}.
}
$$

---

# Series C Roadmap

## C01
**AI 需要先有眼睛：全域觀察者維度的定義**

## C02
**由世界到個體、由個體到世界：全域觀察的對偶計算**

## C03
**差異先於分類：從歧義個體、集合與非交集到計算域**

## C04
**分域算子世界：合法作用、跨域橋接與世界組合**

## C05
**概率也有域：不確定性、混沌、不可判定與世界預測包絡**

## C06
**全域展開、連結與收斂：類全域觀察者的核心計算循環**

## C07
**一句話不是魔法：Sparse Intent 與 Project-World Cognition**

## C08
**從完成任務到負責一個域：長時空 Agent Stewardship**

## C09
**不准考 Neo.K：方法論盲測與全域 AI 觀測器**

## C10
**眼睛何時睜開：全域觀察者相變、脈衝與 AI 原生世界計算**

---

**End of C08**
