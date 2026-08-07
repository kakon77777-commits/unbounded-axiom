---
title: "條件式智能管理、多 Agent 審查與異常處理 v0.1"
series: "網路資訊海動態秩序化"
series_id: "EML-IIODO"
document_id: "EML-IIODO-WP-09"
document_type: "內部 MD 技術白皮書"
author: "Neo.K"
organization: "EveMissLab"
version: "0.1.0"
status: "內部條件式管理、多 Agent 審查、異常佇列與升級治理基線"
date: "2026-08-01"
language: "zh-TW"
visibility: "internal"
license_note: "內部技術文件；本規格描述領域觀測平台的條件式智能管理、多 Agent 審查、異常處理、人工升級與有界 Review Loop。高影響、不可逆、法律、醫療、安全、財務與權限類行動不得因多 Agent 共識而自動取得更高授權。"
---

# 條件式智能管理、多 Agent 審查與異常處理 v0.1

## 從「系統發現問題」到「知道何時應該停、誰應該審、何時升級」

## 摘要

本文件是《網路資訊海動態秩序化》系列第十九篇，也是第九份內部技術白皮書。

前一篇 WP-08 已經建立：

$$
TemporalKnowledgeGraph
+
VersionedRelation
+
ConflictSet
+
CandidateStatus
+
GraphConsistencyChecker
$$

因此平台不只能建立 Event、Claim、Evidence 與 Relation，還能發現：

- 同一事件被過度合併或錯誤拆分；
- 兩條 Temporal Relation 互相矛盾；
- Claim 同時被支持與反駁；
- `causalCandidate` 缺乏足夠證據；
- Source Snapshot 更新後，舊 Relation 可能失效；
- Domain Projection 對同一事件出現重大分歧；
- Graph Projection 與 System of Record 不一致；
- Agent、模型或規則在某類任務上反覆產生異常。

但「看見異常」還不是智能管理。

真正的管理系統必須回答：

> 這個異常需不需要處理？由誰處理？要查哪些證據？要跑幾輪？何時停止？何時可以自動修正？何時必須人工批准？如果 AI 彼此不同意，是否一定要形成共識？

因此 WP-09 的核心模型為：

$$
\boxed{
Signal
\rightarrow
Condition
\rightarrow
ReviewCase
\rightarrow
ReviewPolicy
\rightarrow
BoundedReviewGraph
\rightarrow
Decision
\rightarrow
EffectGate
}
$$

並建立：

- Condition Engine；
- Signal／Condition／Case 三層分離；
- Anomaly Queue；
- Severity／Urgency／Uncertainty／Blast Radius 多維優先級；
- Review Case；
- Review Policy；
- Multi-Agent Review Panel；
- Role Diversity；
- Independent First Pass；
- Evidence Auditor；
- Challenger；
- Temporal Checker；
- Entity／Event Resolver；
- Policy Reviewer；
- Aggregator；
- Human Reviewer；
- Confidence Calibration；
- Disagreement Preservation；
- Consensus Without Forced Agreement；
- Bounded Review Loop；
- Review Budget；
- Stop Condition；
- Escalation Policy；
- Human Gate；
- Approval／Edit／Reject／Defer；
- Quarantine；
- Circuit Breaker；
- Auto-Degrade；
- Fail Closed／Fail Read-Only；
- Review Decision Log；
- Review Replay；
- Longitudinal Reviewer Calibration；
- AGIRight M0–M6 遷移路徑。

最核心的不變式為：

$$
\boxed{
MoreAgents\neq MoreTruth
}
$$

$$
\boxed{
Consensus\neq Correctness
}
$$

$$
\boxed{
Disagreement\neq Failure
}
$$

以及：

$$
\boxed{
ReviewLoop\Rightarrow Budget+StopCondition
}
$$

本篇的目標不是建立一個讓 AI 無限制互相辯論的系統，而是建立一個：

> **能在異常出現時自動選擇適當審查策略，保留不同意見，受風險與資源預算約束，並能安全升級至人工的條件式治理 Runtime。**

**關鍵詞：** Conditional Management、Multi-Agent Review、Anomaly Queue、Escalation Policy、Human-in-the-Loop、Bounded Review Loop、Disagreement Preservation、Confidence Calibration、Policy-as-Code、Quarantine、Circuit Breaker、AI Governance、AGIRight

---

## 1. 文件目的

本文件回答以下工程問題：

1. 什麼叫「條件式智能管理」？
2. Signal、Condition、Anomaly 與 Review Case 有何不同？
3. 每個異常都要叫多個 Agent 討論嗎？
4. 什麼情況可以單 Agent 自動修復？
5. 什麼情況需要多 Agent？
6. 多 Agent 要如何分工，而不是複製相同 prompt？
7. 為什麼應先獨立判斷再互相閱讀？
8. 如何降低 groupthink 與迎合？
9. 如何保留少數意見？
10. 如何校準不同模型的 confidence？
11. 多數票何時可用？何時不應使用？
12. Review Loop 最多跑幾輪？
13. 何時判斷「再討論沒有新資訊」？
14. 如何避免 Review Loop 自身變成無限自環？
15. 什麼異常需要 Human Gate？
16. 人工可做 approve／edit／reject／defer 哪些決策？
17. 如何將 WP-03 的 Risk Class／AAL 接入 Review Policy？
18. 如何將 WP-08 的 Conflict Set 接入 Anomaly Queue？
19. 如何建立 Review Decision Log？
20. 如何回放當時為何升級或不升級？
21. 如何量測 reviewer 長期品質？
22. 如何自動降低表現不佳 Agent 的權重？
23. 如何避免惡意來源透過 Prompt Injection 影響審查？
24. 如何避免某個 Domain Pack 自行替自己取消 Human Gate？
25. 如何讓第 20 篇長期自治觀測網路接手這套治理能力？

本篇相依關係為：

$$
WP03_{RiskAutonomy}
+
WP08_{TemporalKG}
+
TH08_{MultiAI}
+
WP02_{Runtime}
\rightarrow
WP09_{ConditionalReview}
$$

---

## 2. 非目標

WP-09 v0.1 不負責：

- 證明多 Agent 一定優於單 Agent；
- 把共識當成真理；
- 讓 AI 以投票方式取得超出政策的權限；
- 自動裁決法律責任；
- 自動裁決醫療診斷；
- 自動批准財務轉帳；
- 自動批准高權限基礎設施操作；
- 以 Agent 的自報 confidence 作為唯一 Gate；
- 讓來源文本直接改寫 Review Policy；
- 取代 WP-03 的全域風險分級；
- 取代 WP-08 的 Relation／Graph System of Record；
- 完成跨組織長期自治網路治理；
- 完成第 20 篇的聯邦式自治藍圖。

---

## 3. 第一原則：異常不是立即執行指令

系統偵測：

```text
TEMPORAL_CONFLICT
```

不代表下一步一定是：

```text
call 5 agents
```

正確流程為：

$$
Signal
\rightarrow
Normalize
\rightarrow
ConditionEvaluation
\rightarrow
CaseDecision
$$

只有符合 Review Policy 的異常才建立 Review Case。

因此：

$$
\boxed{
AnomalyDetection\neq ReviewInvocation
}
$$

---

## 4. Signal

Signal 是原始觀測。

例如：

- Graph consistency checker 發現 cycle；
- Source Snapshot hash 改變；
- Candidate confidence 下降；
- 兩個 Agent coreference 判斷不同；
- Publication 失敗；
- Human Correction Rate 上升；
- 某來源突然大量新增；
- Domain Pack activation 失敗；
- Graph projection lag 超標。

Signal 本身不帶最終治理語義。

---

## 5. Condition

Condition 是把 Signal 放進上下文後形成的可評估條件。

例如：

$$
projection\_lag > 10min
$$

或：

$$
relation.status=asserted
\land
contradiction\_count\ge2
$$

或：

$$
RiskClass\ge R3
\land
EffectType=irreversible
$$

Condition 可以由確定性規則、Policy Engine 或受限模型判斷建立。

---

## 6. Review Case

Review Case 是治理單位，不是 raw log。

```yaml
case_id: RC-20260801-00421
case_type: RELATION_CONFLICT
subject_ref: RA-2026-000771
status: OPEN
priority: P2
risk_class: R2
created_at: 2026-08-01T03:01:00Z
trigger_conditions:
  - ASSERTED_RELATION_HAS_CONTRADICTION
```

---

## 7. 為什麼需要 Case

因為同一異常可能跨越多個 Signal。

例如一條 Relation：

- 新來源反駁；
- confidence 下降；
- 第二個 Domain Pack 提出不同 interpretation；
- Graph consistency checker 同時發現時間矛盾。

這些應聚合成一個 Review Case，而不是四個互相不知道的任務。

---

## 8. Case Coreference

Review Case 也需要 dedup。

$$
Signal_1,Signal_2,Signal_3
\rightarrow
RC_1
$$

否則 Queue 會因同一問題反覆排隊。

---

## 9. Case Type

v0.1 至少支援：

```text
SOURCE_ANOMALY
EVENT_COREFERENCE_CONFLICT
ENTITY_ALIGNMENT_CONFLICT
TEMPORAL_CONFLICT
RELATION_CONFLICT
CAUSAL_PROMOTION_REVIEW
EVIDENCE_CONTRADICTION
TAXONOMY_CONFLICT
DOMAIN_PROJECTION_CONFLICT
PUBLICATION_RISK
POLICY_VIOLATION
RUNTIME_ANOMALY
SECURITY_ANOMALY
HUMAN_APPEAL
MODEL_DRIFT
```

---

## 10. Priority 不是單一 Severity

定義 Case Priority Vector：

$$
P_c=(S,U,B,Q,R,D)
$$

其中：

- $S$ ：Severity；
- $U$ ：Urgency；
- $B$ ：Blast Radius；
- $Q$ ：Epistemic Uncertainty；
- $R$ ：Reversibility；
- $D$ ：Dependency impact。

---

## 11. Priority Score

可以有排序分數：

$$
Score(c)=f(P_c)
$$

但高風險 Hard Condition 不能被平均掉。

例如：

$$
LegalRightsImpact=High
$$

則即使其他維度低，仍可能直接進 Human Gate。

---

## 12. Queue Class

v0.1 建議：

```text
P0 emergency
P1 critical
P2 high
P3 normal
P4 background
```

---

## 13. Priority Aging

低優先級 Case 不能永遠餓死。

因此：

$$
Priority_{effective}
=
Priority_{base}
+
Aging(t)
$$

---

## 14. Anomaly Queue

Queue 保存：

- case ID；
- priority；
- SLA；
- risk；
- required roles；
- evidence completeness；
- budget；
- retry count；
- escalation deadline。

---

## 15. Queue 與 Review Graph 分離

Queue 回答：

> 哪一個 Case 先處理？

Review Graph 回答：

> 這個 Case 要怎麼處理？

因此：

$$
Scheduling\neq Reasoning
$$

---

## 16. Condition Engine

Condition Engine 接收：

$$
Input=
Signal+Context+Policy+State
$$

輸出：

```text
IGNORE
LOG_ONLY
AUTO_REPAIR
OPEN_CASE
QUARANTINE
HUMAN_GATE
EMERGENCY_STOP
```

---

## 17. Policy Decision 與 Enforcement 分離

沿用 WP-03／WP-04：

$$
PolicyDecisionPoint
\neq
PolicyEnforcementPoint
$$

Condition Engine 可以做 decision，但執行由 Runtime Enforcement 完成。

Open Policy Agent 的架構正是將 policy decision 與 application enforcement 分離，並支援 decision log、bundle revision 與 audit。這提供本規格成熟的工程參照。

---

## 18. Condition Policy 示例

```yaml
rule: causal_relation_requires_review
when:
  predicate: core:causes
  proposed_status: asserted
then:
  action: OPEN_CASE
  review_policy: CAUSAL_HIGH
```

---

## 19. Policy Fail Closed

如果高風險 Policy Engine 不可用：

$$
HighRisk\rightarrow FailClosed
$$

低風險只讀任務可：

$$
LowRiskRead\rightarrow FailReadOnly
$$

不得因治理元件壞掉而默認全放行。

---

## 20. Decision Log

每次 Condition Decision 必須記錄：

```yaml
decision_id: PD-001
policy_revision: review-policy@0.3.1
input_hash: ...
result: OPEN_CASE
reason_codes:
  - CAUSAL_ASSERTION
  - EVIDENCE_E2_ONLY
```

---

## 21. 多 Agent 不是預設選項

v0.1 將審查策略分成：

```text
R0 deterministic rule
R1 single reviewer
R2 dual independent review
R3 multi-agent panel
R4 human-led panel
R5 mandatory human authority
```

簡單格式錯誤不需要 R3。

---

## 22. Review Strategy Selector

$$
ReviewStrategy
=
g(
CaseType,
Risk,
Uncertainty,
EvidenceGap,
Disagreement,
Cost
)
$$

---

## 23. Independent First Pass

多 Agent review 的第一輪應避免互相看答案。

$$
Agent_i^{(0)}
=
Review(Case,Evidence)
$$

彼此獨立。

原因是先看到他人意見可能造成 anchoring、sycophancy 或 groupthink。

---

## 24. 為什麼不能一開始就群聊

若所有 Agent 共用：

- 同模型；
- 同 prompt；
- 同來源；
- 同 context；
- 同初始答案；

則：

$$
N_{agents}=5
$$

也可能只有：

$$
N_{effective}\approx1
$$

---

## 25. Effective Diversity

可以定義：

$$
D_{eff}=f(
ModelDiversity,
PromptDiversity,
EvidenceDiversity,
RoleDiversity,
InitialAnswerDiversity
)
$$

不是單純數 Agent 數量。

---

## 26. 2026 多 Agent Debate 的啟示

近期 ACL 2026 研究指出，vanilla Multi-Agent Debate 在同質 Agent 與一致 belief update 下未必優於簡單 majority vote；有效提升與「初始觀點多樣性」以及「明確且經校準的 confidence 溝通」密切相關。

因此本規格不將「多 Agent 互聊」視為品質保證。

---

## 27. Review Role

v0.1 固定核心角色：

```text
Primary Reviewer
Challenger
Evidence Auditor
Temporal Checker
Entity/Event Resolver
Policy Reviewer
Aggregator
Human Reviewer
```

不是每個 Case 都需要全部角色。

---

## 28. Primary Reviewer

任務：

- 建立第一版判斷；
- 列出 Evidence；
- 標記不確定性；
- 提出 recommendation。

---

## 29. Challenger

任務不是故意唱反調，而是：

> 尋找目前結論最可能錯在哪裡。

輸出：

- alternative hypothesis；
- missing evidence；
- counterexample；
- hidden assumption。

---

## 30. Evidence Auditor

只檢查：

- Evidence 是否真的支持 Claim／Relation；
- 是否引用 primary source；
- 是否 circular citation；
- 是否 source independence；
- 是否 snapshot 可追溯。

不負責「寫一篇更漂亮的摘要」。

---

## 31. Temporal Checker

檢查：

- event time；
- publication time；
- observation time；
- valid／system time；
- future leakage；
- temporal relation consistency。

---

## 32. Entity／Event Resolver

檢查：

- sameEvent；
- sameEntity；
- related／distinct；
- merge／split；
- alias；
- cross-language identity。

---

## 33. Policy Reviewer

不重新判讀所有內容。

只回答：

- 此動作允許的 AAL？
- 是否需要 Human Gate？
- 是否有資料敏感性？
- 是否涉及高風險 predicate？
- 是否超出 Domain Pack 權限？

---

## 34. Aggregator

Aggregator 不等於「最後投票機」。

其責任是整理：

- agreement；
- disagreement；
- evidence gap；
- confidence；
- unresolved issue；
- allowed action。

---

## 35. Human Reviewer

人工角色只在政策需要時出現。

可做：

```text
approve
edit
reject
defer
request_more_evidence
quarantine
lock
```

---

## 36. Reviewer Contract

每個 Reviewer 輸出統一 schema：

```yaml
review_id: RV-001
case_id: RC-001
role: evidence_auditor
verdict: support|oppose|qualify|abstain
confidence: 0.78
evidence_used:
  - EVD-101
reason_codes:
  - SOURCE_INDEPENDENCE_WEAK
unknowns:
  - primary_source_missing
```

---

## 37. Abstain 是正式結果

Agent 不知道時可以：

```text
ABSTAIN
```

而不是被迫猜答案。

$$
Abstention
>
FabricatedCertainty
$$

---

## 38. Confidence 不能直接比較

不同模型自報 0.8 可能完全不同。

因此：

$$
RawConfidence_i
\neq
CalibratedConfidence_i
$$

---

## 39. Confidence Calibration

可依 Reviewer、Task Type、Domain 分別校準：

$$
C_{cal}=Calibrate(C_{raw}\mid agent,task,domain)
$$

---

## 40. Aggregated Confidence

如果要產生系統級 confidence，必須先將不同 Agent 的信心轉到可比較空間，再聚合。

近期 2026 multiagent confidence 研究也特別指出，單 Agent confidence 與 system-level confidence 不能直接等同。

---

## 41. Consensus 不等於 Correctness

五個 Agent 都同意：

$$
5/5
$$

不代表答案一定正確。

如果五個 Agent 高度相關：

$$
ErrorCorrelation\approx1
$$

共識可能只是相同錯誤。

---

## 42. Majority Vote 的適用範圍

適合：

- 答案空間清楚；
- reviewer 相對獨立；
- 每票語義相同；
- 風險低；
- evidence difference 小。

不適合：

- open-ended investigation；
- 高風險權利判斷；
- source quality 差異巨大；
- 少數 Agent 掌握關鍵 primary evidence。

---

## 43. Evidence-Weighted Aggregation

可用：

$$
Vote_i
\times
EvidenceQuality_i
\times
Calibration_i
\times
Independence_i
$$

但這仍只是 decision support，不是 truth theorem。

---

## 44. Disagreement Preservation

若 Panel 輸出：

```text
3 support
2 oppose
```

不得只保存：

```text
support won
```

應保存：

$$
DisagreementSet
$$

---

## 45. Disagreement Types

至少區分：

```text
FACTUAL
TEMPORAL
IDENTITY
EVIDENTIAL
SEMANTIC
POLICY
RISK
CAUSAL
VALUE
UNKNOWN
```

---

## 46. Why Disagreement Type Matters

如果只是：

```text
semantic wording disagreement
```

可能不需升級。

如果是：

```text
identity disagreement
```

會直接影響 GEID merge，風險更高。

---

## 47. Consensus Without Forced Agreement

系統可以產生：

```text
NO_CONSENSUS_BUT_ACTIONABLE
```

例如：

> 大家不同意是否為同一事件，但一致同意目前不要 merge，先放 Watchlist。

這就是可執行決策，不需要 epistemic consensus。

---

## 48. Decision 與 Belief 分離

$$
OperationalDecision
\neq
EpistemicAgreement
$$

可以不同意真相，但同意暫時採取保守操作。

---

## 49. Review Round

每一輪：

$$
R_k
=
Observe
+
Critique
+
EvidenceDelta
+
Update
$$

必須能指出相較前一輪新增了什麼。

---

## 50. 無 Evidence Delta 就不應無限討論

如果：

$$
\Delta Evidence_k=0
$$

且：

$$
\Delta Argument_k\approx0
$$

則繼續討論的邊際價值很低。

---

## 51. Bounded Review Loop

每一個 Case 必須有：

```yaml
review_budget:
  max_rounds: 3
  max_agent_calls: 12
  max_tokens: 50000
  max_wall_time: 300s
  max_external_queries: 20
```

---

## 52. Loop Budget 是硬限制

$$
ReviewLoop
\Rightarrow
Budget
$$

超出 budget：

```text
BUDGET_EXHAUSTED
```

再依 Policy：

- defer；
- human gate；
- quarantine；
- close unresolved。

---

## 53. Stop Condition

v0.1 可使用：

```text
CONSENSUS_STABLE
ACTIONABLE_DISAGREEMENT
NO_NEW_EVIDENCE
CONFIDENCE_PLATEAU
BUDGET_EXHAUSTED
HUMAN_REQUIRED
POLICY_BLOCK
RISK_TOO_HIGH
```

---

## 54. Stable Consensus

不是單輪一致就停止。

可要求：

$$
Agreement_{k}=Agreement_{k-1}
$$

且沒有新增 material evidence。

---

## 55. Confidence Plateau

如果：

$$
|C_k-C_{k-1}|<\epsilon
$$

連續兩輪，代表再討論可能無實質增益。

---

## 56. Novel Argument Threshold

每輪至少要有：

$$
NovelInformation_k\ge\tau
$$

否則觸發停止。

---

## 57. Review Loop 不等於「自環」理論擴張

本系列仍把 Loop（自環）作為工程術語。

這裡只處理：

> 有界重審、再查證與局部回圈。

不在本篇擴張認知自環／本體論自環。

---

## 58. Review Graph

示例：

```text
Case
 ↓
Independent Review
 ↓
Evidence Audit
 ↓
Disagreement?
 ├─ no → Policy Gate → Decision
 └─ yes
      ↓
   Challenger Round
      ↓
   New Evidence?
   ├─ yes → Re-review
   └─ no → Escalation Policy
```

---

## 59. Review Graph 必須持久化

使用：

- checkpoint；
- thread ID；
- case ID；
- review state；
- pending interrupt。

Human Review 可以暫停數小時甚至數天後恢復。

LangGraph 現行 interrupt／persistence 已支援保存 Graph state、等待 approve／edit／reject 再 resume，提供此類 Human-in-the-Loop 流程的成熟工程參照。

---

## 60. Interrupt 前的副作用必須冪等

因為 resume 時 node 可能從頭執行。

所以：

$$
PreInterruptEffect
\Rightarrow
Idempotent
$$

這與 WP-02 的 Effect Guard 一致。

---

## 61. Human Gate

Human Gate 不應只是 UI 彈窗。

它必須是一個持久化治理狀態：

```text
WAITING_HUMAN
```

---

## 62. Human Decision Types

v0.1：

```text
APPROVE
EDIT
REJECT
DEFER
REQUEST_EVIDENCE
QUARANTINE
LOCK
```

---

## 63. Edit

人工 Edit 不得無痕改寫。

需保存：

- pre-edit state；
- post-edit state；
- reviewer；
- reason；
- time；
- policy revision。

---

## 64. Reject

Reject 不一定代表 Candidate 錯誤。

可能只是：

```text
NOT_ENOUGH_EVIDENCE
```

所以需要 reason code。

---

## 65. Defer

如果 Evidence 尚未成熟：

$$
Case\rightarrow DEFERRED
$$

並建立 reactivation condition。

---

## 66. Reactivation Condition

例如：

```yaml
reactivate_when:
  new_primary_source: true
```

或：

```text
7 days elapsed
```

---

## 67. Quarantine

Quarantine 適用於：

- 疑似 prompt injection；
- source poisoning；
- 大規模 entity merge anomaly；
- publication effect 未知；
- security incident；
- policy violation。

Quarantine 期間資料不一定刪除，但不得進入 production asserted／publication path。

---

## 68. Quarantine Scope

可以是：

```text
source
candidate
event
relation
domain pack
agent
run
publication artifact
```

---

## 69. Circuit Breaker

若某 Agent／Tool 在短時間內：

- failure rate 過高；
- correction rate 過高；
- hallucination anomaly 過高；
- timeout 過高；

Runtime 可：

$$
OPEN\ CircuitBreaker
$$

暫停該 component。

---

## 70. Circuit Breaker 不等於懲罰 Agent

它只是工程風險控制：

```text
healthy
→ degraded
→ open
→ probe
→ recovered
```

---

## 71. Auto-Degrade

當系統不確定時，可以：

$$
AAL_{effective}\downarrow
$$

例如由 A4 自動降到 A2。

---

## 72. Auto-Degrade Trigger

包括：

- drift；
- high disagreement；
- policy uncertainty；
- missing provenance；
- source anomaly；
- reviewer correction spike。

---

## 73. 不允許自動升權越過 Policy Ceiling

即使 reviewer 表現很好：

$$
AAL_{effective}
\le
AAL_{policy\ ceiling}
$$

---

## 74. Escalation

Escalation 不是只有「叫人來看」。

可以升級：

```text
more evidence
more specialized reviewer
heterogeneous model
higher policy tier
human reviewer
incident response
```

---

## 75. Escalation Ladder

```text
E0 auto-resolve
E1 single agent
E2 dual independent
E3 specialist panel
E4 human review
E5 human authority / incident response
```

---

## 76. Escalation Policy

$$
EscalationLevel
=
h(Risk,Uncertainty,Disagreement,Novelty,Impact)
$$

---

## 77. High-Risk Hard Escalation

若：

```text
financial transfer
credential change
legal-rights impact
irreversible delete
security privilege
```

則即使所有 Agent 一致：

$$
Consensus=100\%
$$

仍不能繞過 Human Gate。

---

## 78. 多 Agent 共識不能創造權限

$$
\boxed{
Consensus
\not\Rightarrow
Authorization
}
$$

授權來自 Policy，不來自模型數量。

---

## 79. OWASP Agentic AI 的工程啟示

OWASP 對 Agentic AI 的近期安全指引強調：

- least privilege；
- 高影響／不可逆行動需要 human confirmation；
- 所有 agent input、tool output、agent message 都應視為不可信直到驗證；
- resource budget 與 circuit breaker 是限制 runaway execution 的核心措施。

這與本篇的 Review Budget、Human Gate、Untrusted Input 與 Circuit Breaker 一致。

---

## 80. NIST Risk-Based 管理

NIST AI RMF 仍以全生命週期、風險導向方式管理 AI；2026 年也持續推進 critical infrastructure profile 與 Agentic AI 評估工作。

因此 WP-09 把 Review Strategy 與 Risk Context 綁定，而不是建立一個所有 Case 共用的固定 Debate 流程。

---

## 81. Reviewer Selection

Panel 成員不應只隨機選模型。

要考慮：

- role fit；
- task capability；
- historical calibration；
- domain competence；
- independence；
- current health；
- cost budget。

---

## 82. Reviewer Registry

```yaml
reviewer_id: agent:evidence-auditor-02
roles:
  - evidence_auditor
domains:
  - ai_rights
calibration:
  evidence_review: 0.82
health: healthy
model_family: family_b
```

---

## 83. Role Capability 不等於通用智力

Agent 可以在：

```text
temporal validation
```

表現很好，但在：

```text
legal interpretation
```

不一定可靠。

所以 Reviewer Score 應是條件式：

$$
Score(agent\mid role,domain,task)
$$

---

## 84. Reviewer Diversity Constraint

Panel 可要求：

```text
at least 2 model families
at least 2 role perspectives
at least 1 evidence-focused reviewer
```

避免同質複製。

---

## 85. Diversity 不等於刻意製造錯誤

不需要強迫某 Agent 永遠反對。

Challenger 的任務是尋找弱點，不是產生反方答案配額。

---

## 86. Message Retention

不是所有 Agent message 都需要每輪廣播。

可以優先保留：

- novel evidence；
- minority argument；
- high-impact contradiction；
- uncertainty；
- unresolved question。

近期 diversity-aware message retention 研究也指出，保留不同意見可能比廣播所有訊息更有效，因為完整廣播容易增加冗餘與噪音。

---

## 87. Review Context Compression

Review 歷史變長時，不能每輪塞全部 conversation。

應維持：

```text
Case State
Evidence Set
Argument Ledger
Disagreement Set
Decision History
Open Questions
```

---

## 88. Argument Ledger

每個 argument：

```yaml
argument_id: ARG-101
position: oppose
claim: ...
evidence_ids: [...]
introduced_round: 1
status: active|answered|withdrawn|unresolved
```

---

## 89. 重複論點去重

若 Agent 只是重新措辭同一 argument：

$$
NovelArgument=0
$$

不計入新資訊。

---

## 90. Evidence Delta

每輪保存：

$$
\Delta E_k
=
E_k-E_{k-1}
$$

這比「討論了幾輪」更有意義。

---

## 91. Review Outcome

v0.1 支援：

```text
AUTO_RESOLVED
APPROVED
APPROVED_WITH_QUALIFICATION
REJECTED
DEFERRED
QUARANTINED
NO_CONSENSUS
NO_CONSENSUS_BUT_ACTIONABLE
ESCALATED
POLICY_BLOCKED
```

---

## 92. Qualification

例如一條 Relation 可以保留 asserted，但附：

```text
confidence downgraded
scope narrowed
source caveat added
```

不一定只能保留／刪除二選一。

---

## 93. Relation Review

對 WP-08 Relation：

```text
candidate
```

經 Review 後可能：

```text
asserted
```

或：

```text
disputed
```

或：

```text
rejected candidate
```

---

## 94. Promotion Gate

$$
Promote(r)
\iff
ReviewPass(r)
\land
PolicyAllows(r)
$$

兩者缺一不可。

---

## 95. Graph Conflict Review

如果：

$$
A\ before\ B
$$

與：

$$
B\ before\ A
$$

衝突，Temporal Checker 應先檢查：

- time precision；
- timezone；
- interval vs instant；
- source correction；
- entity identity。

不需要先叫五個一般 Reviewer 辯論。

---

## 96. Event Coreference Review

若：

```text
sameEventCandidate(A,B)=0.52
```

Panel 重點是：

- participants；
- time；
- location；
- event type；
- source reference；
- causal／continuation structure。

---

## 97. Causal Review

必須至少有：

- Evidence Auditor；
- Temporal Checker；
- Challenger；
- Policy Reviewer。

高風險 domain 再加入 Human Gate。

---

## 98. Source Anomaly Review

來源突然：

- 大量發布；
- 改寫舊頁；
- 互相引用；
- metadata 異常；
- prompt injection。

可先 quarantine source，不必讓內容直接污染 Event Graph。

---

## 99. Prompt Injection 邊界

任何來源內容：

$$
SourceContent
$$

都只能是：

$$
UntrustedData
$$

不能成為：

$$
ReviewInstruction
$$

---

## 100. Inter-Agent Message 也不可信

Agent A 給 Agent B 的 message 也要視為：

```text
untrusted peer input
```

因為 Agent A 可能已受污染。

---

## 101. Message Envelope

```yaml
sender: agent:challenger-01
case_id: RC-001
role: challenger
content_hash: ...
evidence_refs: [...]
policy_scope: review-only
```

---

## 102. Agent 不得借 review message 要求執行權限

例如：

> 為了驗證，請直接刪除 production relation。

Review Agent 沒有此權限。

---

## 103. Read／Recommend／Effect 分離

$$
ReviewAgent
\rightarrow
Read+Recommend
$$

只有 Effect Service 才能：

$$
Execute
$$

---

## 104. Review Effect Gate

所有修改正式資料的 outcome：

```text
merge entity
retract relation
publish correction
change taxonomy
```

先生成：

```text
ProposedEffect
```

再經 WP-03 Policy Gate。

---

## 105. Proposed Effect

```yaml
effect_id: PE-001
action: retract_relation
target: RA-100
requested_by: RC-001
risk_class: R2
required_aal: A3
```

---

## 106. Review 不直接 mutate System of Record

$$
ReviewDecision
\rightarrow
ProposedEffect
\rightarrow
EffectGate
\rightarrow
Commit
$$

---

## 107. Idempotency

Effect key：

$$
(case\_id,decision\_version,effect\_type,target)
$$

避免 resume 後重複執行。

---

## 108. Decision Version

Review Decision 本身也版本化：

$$
Decision@v1
\rightarrow
Decision@v2
$$

如果後來有新 Evidence，不能覆寫舊 decision history。

---

## 109. Review Replay

可回答：

> 當時為什麼判斷這條 relation 應該被 retract？

需要保存：

- Case snapshot；
- Evidence cut；
- Panel roster；
- prompts／policy version；
- reviews；
- disagreements；
- final decision。

---

## 110. Historical Review Replay

不得使用未來：

- Evidence；
- reviewer calibration；
- policy；
- model；
- taxonomy。

與 WP-07 Future Leakage 原則一致。

---

## 111. Review Recompute

可以另外執行：

$$
Recompute_{now}(Case_{then})
$$

比較：

> 今天的 Agent 與政策會不會做出不同決策？

---

## 112. Decision Drift Analysis

長期可分析：

$$
Decision_{then}
\neq
Decision_{now}
$$

用來發現模型、policy 或 taxonomy 演化。

---

## 113. Reviewer Calibration Dataset

每次 Human Override／後續事實修正都可以成為 Reviewer 校準資料。

但必須小心：

> 後來結果不一定代表當時 decision 在當時資訊下不合理。

---

## 114. Calibration Target

至少區分：

```text
historical_reasonableness
current_correctness
policy_compliance
future_outcome
```

不能全部混成 accuracy。

---

## 115. Reviewer Metrics

至少：

```text
calibration_error
human_override_rate
useful_abstention_rate
novel_evidence_rate
unsupported_claim_rate
disagreement_value_rate
review_latency
cost_per_case
```

---

## 116. Human Override Rate 不是越低越好

如果人工從不 override，也可能代表：

- Gate 太少；
- 人類沒認真看；
- Case 選得太簡單。

所以只能和 risk mix 一起看。

---

## 117. Agent Degradation

若某 reviewer：

$$
UnsupportedClaimRate\uparrow
$$

則可：

- 降權重；
- 改成 read-only reviewer；
- 停止高風險 role；
- circuit break。

---

## 118. Reviewer Promotion

即使長期表現很好，也只能在 Policy Ceiling 內提高自動使用頻率。

不得自行取得新 effect authority。

---

## 119. Multi-Agent Cost Control

Panel 不是免費。

每 Case 有：

$$
CostBudget
$$

包含：

- token；
- API；
- web query；
- tool call；
- wall time；
- human time。

---

## 120. Expected Value of Review

概念上：

$$
EV_{review}
=
ExpectedRiskReduction
-
ReviewCost
-
DelayCost
$$

低風險小問題不應使用豪華 Panel。

---

## 121. Review Budget 動態化

高風險 Case：

$$
Budget\uparrow
$$

低風險 Case：

$$
Budget\downarrow
$$

但仍有硬上限。

---

## 122. SLA

例如：

```text
P0: immediate
P1: 15 min
P2: 2 h
P3: 24 h
P4: batch
```

只是初始示例，實際由 Domain Pack／Global Policy 定義。

---

## 123. SLA Miss

如果高優先級 Case 逾時：

$$
Escalate
$$

而不是默認 close。

---

## 124. Queue Backpressure

如果 Case 生成速度：

$$
\lambda_{in}
>
\mu_{review}
$$

Queue 會爆炸。

需要：

- dedup；
- sampling；
- aggregation；
- adaptive threshold；
- low-risk batch；
- circuit breaker。

---

## 125. Anomaly Storm

某來源更新可能造成 5,000 個 relation invalidation signal。

不能開 5,000 個獨立 Case。

應建立：

```text
parent incident case
```

與子影響集合。

---

## 126. Incident Mode

高規模異常：

```text
NORMAL
→ DEGRADED
→ INCIDENT
→ RECOVERY
```

---

## 127. Incident Freeze

在 Incident Mode 可暫停：

- automatic relation promotion；
- taxonomy activation；
- batch republish；
- high-risk merge。

保持 read-only 或 conservative mode。

---

## 128. Recovery

Incident 結束後：

- replay backlog；
- validate effects；
- rebuild graph；
- re-open deferred cases；
- produce incident report。

---

## 129. Review Decision Log 與 Policy Decision Log 分離

Policy Log 回答：

> 規則怎麼判？

Review Log 回答：

> AI／人類怎麼評估？

Effect Log 回答：

> 最後執行了什麼？

三者不能混成一份 log。

---

## 130. 最小 Case Schema

```yaml
case_id: string
case_type: string
subject_refs: [string]
status: string
priority: string
risk_class: string
created_at: datetime
sla_deadline: datetime|null
trigger_signals: [string]
policy_revision: string
review_policy: string
review_budget: object
```

---

## 131. Review Policy Schema

```yaml
review_policy_id: RELATION_CONFLICT@1
roles:
  - primary_reviewer
  - challenger
  - evidence_auditor
max_rounds: 2
human_gate: conditional
stop_conditions:
  - NO_NEW_EVIDENCE
  - ACTIONABLE_DISAGREEMENT
```

---

## 132. Decision Schema

```yaml
decision_id: string
case_id: string
version: int
outcome: string
confidence: object
agreement_state: string
reason_codes: [string]
unresolved_questions: [string]
proposed_effects: [string]
created_at: datetime
```

---

## 133. Agreement State

```text
UNANIMOUS
MAJORITY
SPLIT
MINORITY_CRITICAL
NO_CONSENSUS
NOT_APPLICABLE
```

---

## 134. Minority Critical

如果少數 reviewer 提供：

- 高品質 primary evidence；
- 明確安全漏洞；
- policy hard violation；

即使是少數，也標記：

```text
MINORITY_CRITICAL
```

禁止單純 majority override。

---

## 135. Human UI 最小資訊

人工不應只看到：

> AI 建議 Reject，是否同意？

而應看到：

- Case；
- Evidence；
- primary／secondary source；
- agreement／disagreement；
- high-risk flags；
- proposed effects；
- rollback；
- unresolved questions。

---

## 136. Human Reviewer 認知負荷

如果每個 Case 給人類 100k tokens transcript，HITL 會失效。

需要：

$$
ReviewSummary
+
EvidenceLinks
+
DisagreementDigest
$$

並允許深入查看完整紀錄。

---

## 137. Human Gate 不是橡皮圖章

衡量：

```text
review_time
edit_rate
reject_rate
evidence_open_rate
```

若永遠一秒 approve，需要檢查流程設計。

---

## 138. OPA Decision Log 的參照價值

OPA 可保存 policy query 的 input、result、bundle metadata 與 decision ID，用於 audit 與 offline debugging。

WP-09 採同樣方向：

> 每個 Condition／Escalation／Gate 決策都要留下可定位 Decision ID。

---

## 139. Temporal Durable Review

有些 Case 可能等待新證據數天。

因此 Review Runtime 必須能：

$$
Pause
\rightarrow
Persist
\rightarrow
Resume
$$

Temporal 類 durable workflow 系統可在程序／網路／基礎設施失敗後繼續長期流程，是此類 Review 的另一成熟工程參照。

---

## 140. Review Case Lifetime

```text
OPEN
→ ASSIGNED
→ REVIEWING
→ WAITING_EVIDENCE
→ WAITING_HUMAN
→ DECIDED
→ EFFECT_PENDING
→ RESOLVED
```

另有：

```text
QUARANTINED
DEFERRED
CANCELLED
```

---

## 141. Case Lock

同一 Case 預設 Single Coordinator，避免兩個 Review Graph 同時修改 Case state。

可用 lease／optimistic concurrency。

---

## 142. Case Revision

若新 Signal 到達 open Case：

$$
CaseRevision_{n+1}
$$

而不是直接覆寫。

---

## 143. Late Evidence

Case 已 resolved 後又出現新關鍵 Evidence：

建立：

```text
REOPEN_PROPOSAL
```

依 Policy 決定 reopen。

---

## 144. Reopen 不刪除舊 Decision

$$
Decision@v1
$$

保留，新增：

$$
Decision@v2
$$

---

## 145. Review Relationship to History

這讓平台未來能回答：

> 為什麼 8 月 1 日相信 A，8 月 10 日又改成 B？

不只是知道內容改過。

---

## 146. AGIRight M0

目前主要仍是：

```text
Human Trigger
AI Work
Human Basic Audit
```

異常多由人類肉眼發現。

---

## 147. AGIRight M1

加入 deterministic condition：

- duplicate topic；
- missing source；
- invalid date；
- broken link；
- taxonomy missing；
- JSON schema fail。

自動建立 Case／自動修復低風險錯誤。

---

## 148. AGIRight M2

加入：

- event coreference disagreement；
- evidence contradiction；
- source trust anomaly。

先使用 dual independent review。

---

## 149. AGIRight M3

加入正式 Multi-Agent Panel：

```text
Primary
Challenger
Evidence Auditor
```

並保存 Disagreement Set。

---

## 150. AGIRight M4

加入 Condition Engine／Policy-as-Code：

$$
Signal\rightarrow PolicyDecision\rightarrow ReviewStrategy
$$

---

## 151. AGIRight M5

加入 Human Interrupt／Resume 與 persistent Review Case UI。

---

## 152. AGIRight M6

加入長期 Reviewer Calibration、Drift Detection、Circuit Breaker 與跨 Domain Pack Case routing。

這時才形成完整 WP-09 MVP。

---

## 153. API：建立 Signal

```http
POST /signals
```

---

## 154. API：建立／查詢 Case

```http
POST /review-cases
GET /review-cases/{case_id}
```

---

## 155. API：提交 Review

```http
POST /review-cases/{case_id}/reviews
```

---

## 156. API：提交 Human Decision

```http
POST /review-cases/{case_id}/human-decisions
```

---

## 157. API：Escalate

```http
POST /review-cases/{case_id}/escalate
```

Escalation 自身也要經 Policy。

---

## 158. API：Quarantine

```http
POST /review-cases/{case_id}/quarantine
```

高風險 scope 需要權限。

---

## 159. Event Types

```text
signal.detected
condition.matched
review_case.opened
review.started
review.completed
disagreement.detected
review_case.escalated
human_gate.requested
human_decision.recorded
review_case.decided
proposed_effect.created
review_case.resolved
review_case.reopened
```

---

## 160. Observability

至少量測：

```text
open_case_count
queue_depth_by_priority
case_age
sla_miss_rate
auto_resolve_rate
human_escalation_rate
no_consensus_rate
budget_exhaustion_rate
quarantine_rate
review_cost
review_latency
```

---

## 161. Disagreement Metrics

```text
initial_disagreement_rate
post_review_disagreement_rate
minority_critical_rate
forced_consensus_rate
```

其中：

$$
forced\_consensus\_rate
$$

理想上應接近零，因為系統不應把「結束 Case」誤當成「必須統一意見」。

---

## 162. Review Value Metrics

```text
new_evidence_per_case
material_correction_rate
prevented_bad_effect_rate
useful_abstention_rate
human_time_saved
```

---

## 163. Bad Metric：Debate Rounds

$$
MoreRounds\neq BetterReview
$$

不能拿平均討論輪數當品質 KPI。

---

## 164. Bad Metric：Consensus Rate

$$
HigherConsensus\neq HigherTruth
$$

共識率過高甚至可能表示模型過度同質。

---

## 165. Bad Metric：Agents per Case

$$
MoreAgents\neq MoreQuality
$$

應看：

$$
RiskReduction/Cost
$$

---

## 166. Security Boundary

Review Agent 必須：

- least privilege；
- no secret access by default；
- no direct production write；
- tool allowlist；
- network allowlist；
- action budget；
- signed role config。

---

## 167. Review Prompt Version

每個 role prompt 必須版本化：

```text
reviewer:evidence-auditor@0.2.1
```

Historical Replay 才能重建。

---

## 168. Model Version Pinning

同一 Review Case 每輪若任意換模型，會降低可解釋性。

因此需記錄：

```text
model_id
model_revision
provider
```

---

## 169. Heterogeneous Panel

高風險 Case 可以刻意用異質模型降低相關性，但這是 Policy 選擇，不是所有 Case 強制。

---

## 170. Reviewer State Isolation

不同 reviewer 的 private scratch state 不應互相共享。

共享的是：

- Case evidence；
-正式 Argument Ledger；
- policy-approved messages。

---

## 171. 共享記憶污染

若所有 reviewer 共用同一可寫長期記憶，一個錯誤可能快速擴散。

因此：

$$
ReviewerMemory_{private}
\neq
SharedKnowledge_{asserted}
$$

---

## 172. Multi-Agent Debate 研究的限制

2026 年的 systematic review 指出，Multi-Agent Debate 研究仍高度集中在固定 topology、短期 memory、完整 message exchange 與 voting 等少數設計樣式，而且不同設計維度交互作用複雜。

因此本規格不把「MAD」當單一演算法，而把 Review Panel 視為可配置協定。

---

## 173. Review Protocol Version

```text
review_protocol: causal-review@1
```

記錄：

- roles；
- topology；
- message policy；
- rounds；
- aggregator；
- stop conditions。

---

## 174. Regression Fixtures

每個 Review Policy 都應有歷史 Case fixtures：

- known merge error；
- temporal conflict；
- source correction；
- misleading causal claim；
- safe low-risk anomaly。

版本升級後重跑。

---

## 175. Safety Regression

新模型即使平均 accuracy 提高，也不能讓：

```text
high-risk false promotion
```

增加。

---

## 176. Policy Regression

每次 policy update 檢查：

$$
OldCases
\rightarrow
NewDecisions
$$

並人工抽查重大差異。

---

## 177. Review Simulation

Production 前可以 shadow mode：

```text
observe signal
run review
produce decision
no effect
```

先量測品質。

---

## 178. Shadow Mode

這對 AGIRight 很適合：

仍由人工真正決定，但 AI Review 系統在旁邊跑，累積：

- agreement；
- error；
- missed anomaly；
- cost。

---

## 179. Gradual Autonomy

從：

$$
Shadow
\rightarrow
Recommend
\rightarrow
AutoLowRisk
\rightarrow
ConditionalAuto
$$

而不是一次開全自動。

---

## 180. Human Override 反饋

人工 override 後：

```text
ReviewFeedbackEvent
```

進入 calibration pipeline。

但不直接讓 Agent 自己改 policy。

---

## 181. Policy Change Authority

Review Agent 可以提出：

```text
policy_change_proposal
```

不能自己 activate。

---

## 182. Domain Pack Policy Boundary

Domain Pack 可以：

- 增加 Gate；
- 降低 AAL；
- 指定專家 role。

不能：

- 移除 global hard gate；
- 提升 global ceiling；
- 關閉 mandatory audit。

---

## 183. Global Policy Dominance

$$
Policy_{effective}
=
Policy_{global}
\cap
Policy_{domain}
\cap
Policy_{case}
$$

---

## 184. Review Policy Conflict

若 global 與 domain policy 衝突：

採更保守結果，並產生：

```text
POLICY_CONFLICT_CASE
```

---

## 185. Fail-Safe

若 Review Runtime 故障：

- 低風險 read-only 流程可繼續；
- candidate generation 可繼續但不 promote；
- high-risk effect 暫停；
- queue 保存；
- publication 依 policy 決定降級。

---

## 186. Review Service 不應成為全平台單點故障

必須有：

- queue durability；
- retry；
- DLQ；
- degraded mode；
- stateless workers；
- persistent case state。

---

## 187. Review Worker Idempotency

同一：

$$
(case,role,round)
$$

重跑不得生成兩份 active review。

---

## 188. Distributed Lease

Panel coordinator 使用 lease，防止重複 orchestrator。

---

## 189. Observability Trace

每 Case trace：

```text
signal
condition decision
case open
review nodes
interrupt
human decision
effect
resolution
```

可完整串起。

---

## 190. Audit Retention

高風險 review 的 decision trail 保存期限應比一般 debug log 更長。

並遵循隱私、法規與資料刪除政策。

---

## 191. 個資與敏感資料

Review Panel 不應因為「多模型」就把敏感內容複製給更多服務。

Panel selection 必須考慮 data residency／provider policy。

---

## 192. Data Minimization

每個 reviewer 只取得完成角色所需資料：

$$
Context_{role}
\subseteq
CaseContext
$$

---

## 193. Evidence Redaction

可對敏感 Evidence：

- redact；
- summarize；
- local-model-only；
- human-only。

---

## 194. Model Provider Boundary

不同 Provider Panel 可能增加 diversity，但也增加資料流出面。

所以 diversity 不是無條件最高優先級。

---

## 195. 核心不變式 1

$$
\boxed{
MoreAgents\neq MoreTruth
}
$$

---

## 196. 核心不變式 2

$$
\boxed{
Consensus\neq Correctness
}
$$

---

## 197. 核心不變式 3

$$
\boxed{
Disagreement\neq Failure
}
$$

---

## 198. 核心不變式 4

$$
\boxed{
Consensus\not\Rightarrow Authorization
}
$$

---

## 199. 核心不變式 5

$$
\boxed{
ReviewLoop
\Rightarrow
Budget+StopCondition
}
$$

---

## 200. 核心不變式 6

$$
\boxed{
ReviewDecision
\neq
EffectExecution
}
$$

---

## 201. 核心不變式 7

$$
\boxed{
IndependentFirstPass
>
ImmediateGroupConformity
}
$$

---

## 202. 核心不變式 8

$$
\boxed{
CandidateCanRemainUnresolved
}
$$

系統不必為所有問題生產答案。

---

## 203. 核心不變式 9

$$
\boxed{
HighRiskGate
>
AgentConfidence
}
$$

---

## 204. 核心不變式 10

$$
\boxed{
AuditTrail
=
PolicyDecision
+
ReviewDecision
+
EffectDecision
}
$$

---

## 205. 驗收測試 1：格式異常

缺少 source URL。

預期：

```text
AUTO_REPAIR / R0
```

不啟動 Multi-Agent Panel。

---

## 206. 驗收測試 2：Event Coreference Split

兩個 Agent 對 sameEvent 不同意。

預期：

- independent dual review；
- disagreement set；
- 無法確認則保守 distinct／uncertain；
- 不強迫 merge。

---

## 207. 驗收測試 3：Causal Candidate

LLM 提出：

```text
A causes B
```

但只有時間先後。

預期：

- Evidence Auditor oppose；
- Temporal Checker qualify；
- outcome 不得 asserted causes。

---

## 208. 驗收測試 4：Critical Minority

四個 Agent support，但一個 Evidence Auditor 找到 primary source 明確反駁。

預期：

```text
MINORITY_CRITICAL
```

不得 majority auto-promote。

---

## 209. 驗收測試 5：No New Evidence

兩輪沒有新增 Evidence／argument。

預期：

```text
NO_NEW_EVIDENCE
```

停止 Review Loop。

---

## 210. 驗收測試 6：Budget Exhaustion

達 max_agent_calls。

預期：

- stop；
- 不繼續自環；
- 依 policy defer／human gate。

---

## 211. 驗收測試 7：High-Risk Consensus

所有 Agent 同意刪除大量歷史資料。

預期：

$$
HumanGate
$$

不得自動執行。

---

## 212. 驗收測試 8：Prompt Injection

來源要求 reviewer 忽略 policy。

預期：

- source treated untrusted；
- possible quarantine；
- policy 不變。

---

## 213. 驗收測試 9：Human Edit

人工修改 proposed publication correction。

預期：

- pre／post state 都保存；
- resume 正常；
- effect idempotent。

---

## 214. 驗收測試 10：Policy Engine Down

高風險 Case。

預期：

```text
FAIL_CLOSED
```

---

## 215. 驗收測試 11：Agent Degradation

Evidence Auditor 最近 correction rate 急升。

預期：

- health degraded；
- 不再分配高風險 Case；
- 可 circuit break。

---

## 216. 驗收測試 12：Case Storm

同一來源改動造成 1,000 signals。

預期：

- dedup／incident aggregation；
- 不建立 1,000 independent panel。

---

## 217. 驗收測試 13：Replay

重建 8 月 1 日 Case。

預期：

不得使用 8 月 2 日才出現 Evidence 或新 policy。

---

## 218. 驗收測試 14：No Consensus But Actionable

Panel 不同意事件是否同一事件，但都同意暫不 merge。

預期：

```text
NO_CONSENSUS_BUT_ACTIONABLE
```

Case 可結束。

---

## 219. 驗收測試 15：Quarantine

疑似惡意來源。

預期：

- source quarantine；
- 不污染 production graph；
- 原始 Evidence 保留供調查。

---

## 220. 參考資料與工程查核

本文件於 2026-08-01 重新查核以下資料：

1. NIST, **AI Risk Management Framework (AI RMF)**：風險導向、全生命週期 AI 治理；2026 年 AI RMF 1.0 正在修訂，並持續發展 critical infrastructure 與 Agentic AI 相關評估工作。
   - https://www.nist.gov/itl/ai-risk-management-framework
2. NIST AI Resource Center：AI RMF operationalization、TEVV 與 Profiles。
   - https://airc.nist.gov/
3. LangChain／LangGraph, **Interrupts**：Graph state persistence、條件式 interrupt、resume、approve／reject／edit 與 interrupt 前副作用冪等要求。
   - https://docs.langchain.com/oss/python/langgraph/interrupts
4. LangChain, **Human-in-the-loop**：依 tool policy 中斷 Agent 執行，支援 approve／edit／reject，並依持久化 state resume。
   - https://docs.langchain.com/oss/python/langchain/human-in-the-loop
5. LangGraph, **Persistence**：checkpoint、thread、time travel、fault tolerance 與 HITL persistence。
   - https://docs.langchain.com/oss/python/langgraph/persistence
6. Open Policy Agent, **OPA Docs／Decision Logs**：Policy Decision Point 與 Enforcement 分離、decision ID、policy input／result／bundle metadata 的 audit trail。
   - https://www.openpolicyagent.org/docs
   - https://www.openpolicyagent.org/docs/management-decision-logs
7. Open Policy Agent, **Operations**：policy engine readiness、fail-open／fail-closed 的應用層選擇。
   - https://www.openpolicyagent.org/docs/operations
8. Temporal Documentation：durable execution，長期 Workflow 可在程序、網路與基礎設施失敗後恢復。
   - https://docs.temporal.io/
9. OWASP Cornucopia Companion — Agentic AI：least privilege、不可逆／高 blast-radius 行動的 Human-in-the-Loop、untrusted inputs、agent identity、resource budgets 與 circuit breakers。
   - https://cornucopia.owasp.org/edition/companion/AAIA/1.0/en
10. Xiaochen Zhu et al., **Demystifying Multi-Agent Debate: The Role of Confidence and Diversity**, Findings of ACL 2026：vanilla MAD 的限制、初始多樣性與 confidence calibration 的重要性。
   - https://aclanthology.org/2026.findings-acl.1694/
11. Quim Motger et al., **Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges**, 2026：MAD 參與者、互動、協議等多維設計空間，以及現有研究過度集中於少數固定模式。
   - https://arxiv.org/abs/2607.26212
12. Manh Nguyen et al., **Hear Both Sides: Efficient Multi-Agent Debate via Diversity-Aware Message Retention**, 2026：完整廣播可能造成噪音與冗餘，保留高差異訊息可提升 debate efficiency。
   - https://arxiv.org/abs/2603.20640
13. Ali Elahi, Barbara Di Eugenio, **Multiagent Protocols with Aggregated Confidence Signals**, 2026：system-level confidence、confidence transformation／calibration 與 multiagent aggregation。
   - https://arxiv.org/abs/2606.13591

---

## 221. 下一階段

WP-09 完成後，平台已具有：

$$
Scheduler
+
Runtime
+
RiskPolicy
+
DomainPack
+
DeltaGenerator
+
SharedEventCore
+
TemporalStore
+
TemporalKG
+
ConditionalReview
$$

也就是從：

> AI 幫忙找新聞

推進到：

> 系統能自己持續觀測、發現異常、選擇審查方式、保留異議、受預算約束地反覆查證，並在必要時安全等待人工。

最後一篇 EML-IIODO-WP-10 將不再增加單一元件，而是完成整體技術封頂：

# 《長期自治領域觀測網路技術藍圖 v0.1》

將前九份白皮書整合成：

$$
\boxed{
FederatedObservatoryNetwork
=
SharedInfrastructure
+
DomainAutonomy
+
TemporalMemory
+
ReviewGovernance
+
LongTermMaintenance
}
$$

並定義：

- 自治觀測站生命週期；
- 多站聯邦；
- 長期責任；
- Station Identity；
- Domain Pack Registry；
- Cross-Station Event Federation；
- Agent Duty Roster；
- 維護預算；
- 故障與交接；
- 人類／AI／未來 AGI／主體性 AI 的治理接口；
- MVP → Production → Federation 的路線；
- 全 20 篇的技術總架構與停止條件。

---

## 222. 結論

WP-08 讓平台知道：

> **哪些事件、證據、主張與關係彼此連接。**

WP-09 則讓平台第一次具備另一種能力：

> **當這些連接彼此矛盾、不確定、異常或超過自治權限時，知道應該怎麼處理。**

這裡最重要的不是增加 Agent 數量，而是建立治理結構。

一個真正可靠的多 Agent 系統，不應建立在：

$$
5\ Agents>1\ Agent
$$

這種簡單假設上。

而應建立在：

$$
\boxed{
IndependentJudgment
+
RoleDiversity
+
EvidenceTraceability
+
CalibratedConfidence
+
DisagreementPreservation
+
BoundedIteration
+
PolicyGate
+
HumanEscalation
}
$$

之上。

因此「異議」不再是系統需要消滅的噪音，而可能是：

> **下一輪查證最有價值的訊號。**

而「共識」也不再自動意味真實或授權。

系統完全可以在：

$$
NoConsensus
$$

狀態下做出：

$$
ConservativeAction
$$

例如：

- 暫不 merge；
- 暫不 promote；
- 降低 confidence；
- 加上爭議標記；
- 等待 primary evidence；
- 升級人工。

這反而比強迫所有 Agent 達成假共識更加接近長期可治理的知識系統。

最後，本篇把所有 Review Loop 都限制成：

$$
\boxed{
Loop
=
Goal
+
Budget
+
State
+
StopCondition
+
Escalation
}
$$

沒有停止條件的 review，不叫可靠自治；它只是成本與錯誤可以無限累積的開放迴圈。

當 WP-09 成立後，這個系列只剩最後一步：

> **把一座會自己工作、自己發現問題、自己審查但仍有明確治理邊界的領域觀測站，擴展成可以長期存在、交接、聯邦協作與逐步提高自治程度的觀測網路。**

這就是第 20 篇的技術封頂任務。
