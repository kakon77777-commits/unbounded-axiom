# 誰負責不等於誰先賠：AI 時代的 Responsibility–Compensation Separation

**英文暫名：** Responsibility Is Not Compensation: Separating Accountability, Financial Liability, Insurance Payment, and Recovery in the AI Era  
**系列：** 不可逆的制度化智能：具身責任、保險、資本與 AI 經濟主體  
**English Series:** *The Institutional Irreversibility of Intelligence: Embodiment, Liability, Insurance, Capital, and AI Economic Subjecthood*  
**論文序號：** Paper 05 / 08  
**版本：** v0.1  
**日期：** 2026-09-08  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** Paper 00–04；Responsibility Graph；Machine Insurability Infrastructure；Responsibility–Control Divergence；Embodied Execution Graph  
**文件地位：** Liability / Compensation / Insurance / Corporate Risk Architecture Paper  
**Canonical Source：** UTF-8 Markdown  
**Canonical Math Delimiters：** inline ` $...$ `；display `$$...$$`

---

## 研究地位聲明

本文不是任何特定司法管轄區的法律意見，也不主張企業、員工、AI、robot、manufacturer、software vendor 或 insurer 在特定事故中應依法承擔何種最終比例的賠償責任。

本文處理的是一個更前置、且對高自主系統極重要的制度問題：

> **責任歸因與賠償能力是兩個不同問題。**

一個 actor 可能對事故形成有 policy、design、deployment、delegation、execution、maintenance 或 supervision responsibility，但這不代表該 actor 的私人資產必須成為受害人的主要 loss-absorbing source。相反地，一個企業或 insurer 可能依法或依契約先行賠償，即使最終事故原因部分來自 vendor、operator、AI system、employee 或 component provider。

本文因此提出：

$$
\boxed{
\text{Responsibility Attribution}
\neq
\text{Compensation Capacity}.
}
$$

並將 autonomous-system loss handling 拆分為 responsibility、liability、coverage、payment、recovery 與 capital 六個不同層級。

---

## 摘要

前四篇已建立：

1. Institutional AI Ratchet；
2. Embodied Execution Graph；
3. Responsibility–Control Divergence；
4. Responsibility Graph；
5. Machine Insurability Infrastructure。

但到真正事故發生時，還會遇到一個非常現實的問題：

> **誰負責，不等於誰先把錢付給受害人。**

假設 autonomous factory 發生事故：

$$
Loss
=
\$100M.
$$

事故調查可能發現：

- human supervisor 有 supervision failure；
- fleet AI 有 assignment failure；
- maintenance contractor 有 maintenance failure；
- software vendor 有 design defect；
- company 有 deployment / governance responsibility。

這不代表應把：

$$
\$100M
$$

按某個責任比例直接要求每一個自然人用私人財產立即支付。

本文將事故後的制度鏈條拆成：

$$
\boxed{
\text{Responsibility}
\rightarrow
\text{Legal / Contractual Liability}
\rightarrow
\text{Coverage}
\rightarrow
\text{Compensation Payment}
\rightarrow
\text{Recovery / Subrogation}
\rightarrow
\text{Final Economic Burden}.
}
$$

本文進一步定義 **Compensation Graph**：

$$
\boxed{
\mathcal G^{C}
=
(
V_C,
E_C,
\Theta_C,
\Pi_C
)
}
$$

其中節點可以包括：

- victim / claimant；
- company；
- employee；
- insurer；
- reinsurer；
- manufacturer；
- software vendor；
- system integrator；
- fleet operator；
- AI economic account；
- reserve pool；
- government compensation fund。

主要 edge types 包含：

```text
owes_compensation_to
pays_first
insured_by
subject_to_deductible
subject_to_retention
indemnified_by
reimbursed_by
subrogates_against
recovers_from
shares_loss_with
funded_by
```

因此 Responsibility Graph 與 Compensation Graph 必須分開：

$$
\boxed{
\mathcal G^{R}
\neq
\mathcal G^{C}.
}
$$

Responsibility Graph 回答：

> 誰在治理、設計、授權、委派、執行、維護或監督上負有責任？

Compensation Graph 回答：

> 受害人先從哪裡得到錢？  
> insurer支付多少？  
> company自留多少？  
> deductible / retention多少？  
> 後續向哪個 vendor、manufacturer 或其他 actor追償？

本文進一步指出，企業級 autonomous risk 若名義上全部壓給一個 employee，會產生一個基本財務錯配：

$$
\boxed{
Loss_{\max}
\gg
PersonalAssets_H.
}
$$

此時「某人負責」不能替代：

$$
\boxed{
\text{Enterprise-Level Financial Responsibility}.
}
$$

因為企業取得收益、部署 system、持有資本、購買保險並管理供應鏈，故企業級 loss 一般需要 company capital、insurance、self-insured retention、vendor indemnity、reinsurance 或其他 financial responsibility architecture 承接。

本文把 loss absorption layer 表示為：

$$
\boxed{
Loss
\rightarrow
Deductible
\rightarrow
CorporateRetention
\rightarrow
Insurance
\rightarrow
Reinsurance
\rightarrow
Recovery.
}
$$

但這只是其中一種常見抽象；不同 policy / contract / law 可產生不同順序。

本文進一步引入 **Financial Responsibility Capacity**：

$$
\boxed{
FRC(a)
=
\text{actor }a\text{ 可合法、可持續、可實際吸收的損失能力}.
}
$$

並提出：

$$
\boxed{
\text{Responsibility Weight}
\neq
\text{Financial Responsibility Capacity}.
}
$$

因此 employee 可能有高 supervision responsibility，但低 FRC；company 可能有更高 FRC；insurer 則以 contractual coverage 提供額外 loss-absorbing capacity。

本文再提出 **Compensation Priority Principle**：

> **事故制度首先應確保受害人可以從具有實際支付能力、明確 coverage 或法定責任的主體取得賠償；責任歸因與內部追償可在之後更精細地處理。**

這個原則並不表示 company 永遠第一賠，也不表示 insurer 永遠第一賠，而是把「受害人補償效率」與「最終責任精確分配」分成不同時間尺度。

本文同時提出 **Recovery Layer**。若 insurer 或 company 先行支付：

$$
Payer
\rightarrow
Victim,
$$

後續可依 evidence、contract、law 建立：

$$
Payer
\rightarrow
RecoverFrom(
Vendor,
Manufacturer,
Operator,
OtherParty
).
$$

因此：

$$
\boxed{
\text{Pay First}
\neq
\text{Bear Final Economic Burden}.
}
$$

最後，本文把 Compensation Graph 接到後續 Capital Follows Autonomy。當某 AI / autonomous domain長期產生可歸因 risk與收益後，企業可能開始建立：

- AI-specific reserve；
- responsibility reserve；
- insurance contribution；
- first-loss pool；
- dedicated operating capital。

此時 AI-specific capital並不是因為「AI先成為法律人格」，而是因為 autonomous risk domain需要被穩定定價、隔離、追蹤與吸收。

**關鍵詞：** Responsibility–Compensation Separation、Compensation Graph、Corporate Liability、Insurance Payment、Subrogation、Financial Responsibility Capacity、Deductible、Retention、AI Liability、Autonomous Systems

---

# 1. 第一個核心區分：責任不是賠償

本文固定：

$$
\boxed{
\text{Responsibility}
\neq
\text{Compensation}.
}
$$

Responsibility回答：

> 誰在治理或事故形成中負有何種責任？

Compensation回答：

> 哪個有支付能力的主體要把 money transfer 給受害人？

---

# 2. 第二個核心區分：責任不等於支付能力

一個 human supervisor $H$ 可能：

$$
Resp(H)>0.
$$

但：

$$
Assets_H
\ll
Loss_{\max}.
$$

所以：

$$
\boxed{
Resp(H)>0
\not\Rightarrow
FRC(H)\ge Loss_{\max}.
}
$$

---

# 3. Financial Responsibility Capacity

定義：

$$
\boxed{
FRC(a)
}
$$

為 actor $a$ 在不立即失去整個支付能力、且符合法律／契約架構下，可實際吸收的 loss capacity。

---

# 4. FRC 來源

可包括：

- liquid assets；
- corporate capital；
- reserve；
- insurance coverage；
- reinsurance；
- guarantee；
- indemnity；
- compensation fund。

---

# 5. Natural Person FRC

自然人的：

$$
FRC(H)
$$

通常不應被假設等於 enterprise-scale exposure。

---

# 6. Company FRC

公司可透過：

$$
Capital
+
Insurance
+
Retention
+
Contracts
$$

形成較高 loss absorption。

---

# 7. Insurer FRC

insurer透過：

- premium pool；
- capital；
- reinsurance；
- portfolio diversification；

提供 contractual risk capacity。

---

# 8. Responsibility Graph 與 Compensation Graph 分離

Paper 03：

$$
\mathcal G^{R}.
$$

本文：

$$
\mathcal G^{C}.
$$

因此：

$$
\boxed{
\mathcal G^{R}
\neq
\mathcal G^{C}.
}
$$

---

# 9. Compensation Graph 的定義

$$
\boxed{
\mathcal G^{C}
=
(
V_C,
E_C,
\Theta_C,
\Pi_C
)
}
$$

其中：

- $V_C$：claimants / companies / insurers / vendors / reserves / funds；
- $E_C$：payment / recovery relations；
- $\Theta_C$：limits / deductibles / status / currency / timing；
- $\Pi_C$：legal / contract / policy evidence。

---

# 10. Compensation Node Types

第一代：

```text
claimant
company
employee
insurer
reinsurer
manufacturer
software_vendor
system_integrator
operator
reserve_pool
AI_economic_account
government_fund
```

---

# 11. Compensation Edge Types

第一代：

```text
owes_compensation_to
pays_first
insured_by
subject_to_deductible
subject_to_retention
indemnified_by
reimbursed_by
subrogates_against
recovers_from
shares_loss_with
funded_by
```

---

# 12. Responsibility-to-Compensation Bridge

可建立：

```text
responsibility_evidence_for
liability_basis_for
recovery_basis_for
```

但 RG edge不能直接被當成 money-flow edge。

---

# 13. Causality 也不等於 Compensation

$$
\boxed{
Causality
\neq
Compensation.
}
$$

component造成 failure，不表示受害人一定先向 component vendor拿錢。

---

# 14. Liability Layer

責任歸因後還需要：

$$
\boxed{
\text{Legal / Contractual Liability Layer}.
}
$$

它回答：

> 哪個 actor依法或依契約對損失負何種 liability？

---

# 15. Liability 不等於 Coverage

即使 actor依法負責：

$$
Liable(a)=1,
$$

也不代表 insurance policy一定 cover。

因此：

$$
\boxed{
Liability
\neq
Coverage.
}
$$

---

# 16. Coverage 不等於 Payment Amount

policy有：

- deductible；
- retention；
- limit；
- exclusion；
- sublimit；
- aggregate。

所以：

$$
Coverage=1
$$

不代表：

$$
Payment=Loss.
$$

---

# 17. Payment 不等於 Final Burden

insurer支付後可 subrogate。

company支付後可 recover from vendor。

所以：

$$
\boxed{
Payment
\neq
FinalEconomicBurden.
}
$$

---

# 18. 六層架構

本文將事故財務處理拆為：

$$
\boxed{
R
\rightarrow
L
\rightarrow
I
\rightarrow
P
\rightarrow
Rec
\rightarrow
B
}
$$

其中：

- $R$：Responsibility；
- $L$：Liability；
- $I$：Insurance Coverage；
- $P$：Payment；
- $Rec$：Recovery；
- $B$：Final Economic Burden。

---

# 19. 受害人補償與責任精確化的時間尺度不同

事故後：

$$
t_1:
\text{Victim Compensation}
$$

可能需要快速。

而：

$$
t_2:
\text{Final Liability Allocation}
$$

可能耗時更久。

因此：

$$
\boxed{
t_1<t_2
}
$$

是可能且合理的制度設計。

---

# 20. Compensation Priority Principle

本文提出：

$$
\boxed{
\textbf{Compensation Priority Principle}
}
$$

弱形式：

> **對可保、可識別的重大事故，制度應盡可能讓受害人先從具備支付能力與明確責任／coverage的主體獲得補償，再透過 claims、subrogation、indemnity與法律程序細化最終經濟負擔。**

---

# 21. 這不代表 insurer 一定先賠

具體順序依：

- policy；
- law；
- claimant；
- liability；
- deductible；
- retention。

---

# 22. Enterprise-Level Financial Responsibility

當：

$$
EnterpriseOperation
\rightarrow
EnterpriseBenefit,
$$

且：

$$
EnterpriseOperation
\rightarrow
EnterpriseScaleRisk,
$$

制度需要：

$$
\boxed{
\text{Enterprise-Level Financial Responsibility}.
}
$$

---

# 23. Employee 不應被當成 Capital Buffer

員工薪資／私人資產不是企業 autonomous deployment的合理主力 loss-absorbing capital。

因此：

$$
\boxed{
Employee
\neq
EnterpriseCapitalBuffer.
}
$$

---

# 24. Supervisor Responsibility 與 Corporate Compensation 可以同時成立

例如：

$$
Resp_{supervisor}>0
$$

同時：

$$
CompanyPaysFirst=1.
$$

沒有矛盾。

---

# 25. 公司先賠不代表公司內部不能追責

公司可以：

- disciplinary action；
- internal recovery；
- termination；
- claims against vendor；

視制度而定。

---

# 26. Company Pays First ≠ Company Bears Final Burden

$$
\boxed{
PayFirst(company)
\not\Rightarrow
FinalBurden(company)=100\%.
}
$$

---

# 27. Insurance Payment Layer

保單可以：

$$
Insurer
\rightarrow
Company/Victim.
$$

但有：

$$
Deductible.
$$

---

# 28. Deductible

$$
D
$$

表示 insured先承擔的 loss layer。

---

# 29. Self-Insured Retention

$$
SIR
$$

可能要求 company先處理一定額度。

---

# 30. Limit

$$
Limit
$$

限制 insurer最大 payment。

---

# 31. Aggregate Limit

多事故累積：

$$
AggregateLoss
$$

受到年度 aggregate limit。

---

# 32. Reinsurance

insurer也可能：

$$
Insurer
\rightarrow
Reinsurer.
$$

---

# 33. Reinsurance 不直接等於受害人 payment relationship

通常是 insurer capital structure的一部分。

---

# 34. Compensation Waterfall

概念性 waterfall：

$$
\boxed{
Loss
\rightarrow
Deductible
\rightarrow
CorporateRetention
\rightarrow
PrimaryInsurance
\rightarrow
ExcessInsurance
\rightarrow
ReinsuranceSupport.
}
$$

這只是 abstract architecture。

---

# 35. Vendor Indemnity

company與 vendor可能有 indemnity contract。

事故後：

$$
Company
\rightarrow
Victim
$$

再：

$$
Company
\rightarrow
RecoverFrom(Vendor).
$$

---

# 36. Subrogation

insurer支付 claim後：

$$
Insurer
\rightarrow
RecoverFrom(ResponsibleThirdParty).
$$

---

# 37. Subrogation 需要 Responsibility Evidence

如果沒有 Responsibility Graph / execution evidence：

$$
RecoveryConfidence\downarrow.
$$

---

# 38. Responsibility Graph 因此有 Financial Value

Paper 03 的 graph不只是 governance record。

它可降低：

- claims ambiguity；
- recovery uncertainty；
- litigation uncertainty。

---

# 39. Compensation Graph 需要 Coverage Evidence

包括：

- policy；
- endorsements；
- limits；
- exclusions；
- effective dates；
- insured entities。

---

# 40. Time-Varying Coverage

事故：

$$
t_e
$$

要看：

$$
Coverage(t_e).
$$

不能看事故後的新 policy。

---

# 41. Compensation Snapshot

對 incident建立：

```text
claimant
loss estimate
responsibility snapshot
coverage snapshot
deductible
retention
policy limits
indemnity refs
recovery targets
```

---

# 42. Compensation Graph 是 time-versioned

$$
\mathcal G^C(t).
$$

因為 coverage / payments / recoveries會變。

---

# 43. Claim State

```text
reported
reserved
accepted
partially_paid
paid
denied
disputed
recovered
closed
```

---

# 44. Reserve

insurer / company會建立：

$$
Reserve_{claim}.
$$

---

# 45. Reserve 不等於 Payment

$$
\boxed{
Reserve
\neq
Payment.
}
$$

只是 expected future obligation。

---

# 46. AI-specific Reserve 的前置概念

如果某 AI / fleet domain能被穩定歸因：

$$
Reserve_{AI-domain}
$$

就可能出現。

Paper 06會展開。

---

# 47. Compensation Capacity

對 actor $a$：

$$
C_a^{comp}.
$$

表示實際支付 capability。

---

# 48. Responsibility Weight vs Compensation Capacity

$$
\boxed{
w_a^{resp}
\neq
C_a^{comp}.
}
$$

---

# 49. Responsibility 高但 Capacity 低

employee例子：

$$
w_H^{resp}>0,
$$

$$
C_H^{comp}\ll Loss.
$$

---

# 50. Responsibility 低但 Capacity 高

insurer可能不對事故形成有 operational responsibility，

但有：

$$
CoverageObligation>0.
$$

---

# 51. Insurer 不因賠錢而成事故 responsible actor

$$
\boxed{
InsurancePayment
\not\Rightarrow
OperationalResponsibility.
}
$$

---

# 52. Company Financial Responsibility 與 Fault 分離

有些制度會要求 company對外負責，即使 internal fault attribution尚未完成。

本文只描述可能的 architecture，不預設具體 law。

---

# 53. Victim-Facing Layer

受害人最在意：

$$
\boxed{
\text{Can I actually be compensated?}
}
$$

而不是 organizational blame map。

---

# 54. Internal Allocation Layer

企業 / insurer則在後面處理：

$$
\boxed{
\text{Who ultimately bears the loss?}
}
$$

---

# 55. Public Policy Tension

若責任圖太複雜、受害人必須向十個 actors逐一求償：

$$
VictimTransactionCost\uparrow.
$$

---

# 56. Compensation Simplicity Principle

可能需要：

$$
\boxed{
\text{Victim-Facing Simplicity}
+
\text{Backend Responsibility Complexity}.
}
$$

---

# 57. Front-End vs Back-End Liability Architecture

front-end：

> claimant向有財力、明確主體請求。

back-end：

> insurers / firms / vendors再細分。

---

# 58. Single Compensation Interface

未來某些高 autonomy domain可能建立：

$$
SingleCompensationInterface.
$$

例如：

- operator；
- mandatory insurer；
- compensation fund。

---

# 59. 這不等於 Single Responsibility

$$
\boxed{
SingleCompensationInterface
\neq
SingleResponsibleActor.
}
$$

---

# 60. Mandatory Insurance 的可能性

某些高風險 domain可能被要求 compulsory insurance。

本文不主張一定如此。

---

# 61. Financial Responsibility Requirement

即使不用 insurance，也可能要求：

- minimum capital；
- bond；
- guarantee；
- reserve。

---

# 62. Insurance vs Self-Insurance

企業可以：

$$
Insurance
$$

或：

$$
SelfInsuredRetention.
$$

差別在 risk transfer程度。

---

# 63. Autonomous-System Capital Stack

可表示：

$$
\boxed{
\text{Operating Capital}
+
\text{Risk Reserve}
+
\text{Insurance}
+
\text{Reinsurance}.
}
$$

---

# 64. Responsibility-to-Capital Link

如果 domain $d$ 有：

$$
Resp(A,d),
$$

企業可能配置：

$$
Capital(d).
$$

這就是 Paper 06入口。

---

# 65. AI Economic Account 可以先作 Risk Account

一開始不必說：

> 這是 AI 私人財產。

只可定義：

$$
\boxed{
\text{AI-Linked Risk Account}.
}
$$

---

# 66. AI-Linked Risk Account

用途：

- deductible；
- maintenance；
- insurance contribution；
- upgrade；
- first-loss reserve。

---

# 67. Risk Account 與 Company Ownership

account法律上可以仍由 company持有。

但 operationally綁 AI responsibility domain。

---

# 68. Persistent Domain Accounting

如果 AI A長期負責 domain D：

$$
Account(A,D,t)
$$

可以跨年度存在。

---

# 69. 這開始形成 Economic State

$$
\boxed{
PersistentEconomicState(A,D).
}
$$

---

# 70. Compensation Layer 推動 Capital Layer

$$
\boxed{
\text{Loss Attribution}
\rightarrow
\text{Reserve Allocation}
}
$$

---

# 71. Company Benefit 與 Company Responsibility

如果 company取得 autonomous system收益：

$$
Benefit_C>0,
$$

也應把 loss architecture納入 capital planning。

---

# 72. Limited Liability Corporation 的意義

公司本來就是將企業資產、契約與責任組織化的法律載體。

因此 autonomous risk進 company financial layer並不奇怪。

---

# 73. 但 AI-specific Sub-Accounting 可能出現

由於 AI domain可跨 project / robot / time，

企業可能更細：

$$
SubAccount_{AI}.
$$

---

# 74. AI Sub-Account 不等於 AI Legal Personhood

$$
\boxed{
AISubAccount
\not\Rightarrow
AILegalPerson.
}
$$

---

# 75. Compensation Graph 與 Capital Graph 分離

Compensation Graph：

> loss money怎麼流？

Capital Graph：

> 哪些 pool平時承擔 capacity？

因此：

$$
\boxed{
CompensationGraph
\neq
CapitalGraph.
}
$$

---

# 76. Capital Graph

下一篇可定義：

$$
\mathcal G^K.
$$

---

# 77. Compensation Graph 與 Insurance Graph

Insurance Graph提供 coverage edges。

Compensation Graph記實際 claim / payment edges。

---

# 78. Coverage Exists but No Payment Yet

因此：

$$
Coverage=1,
Payment=0
$$

可以合法存在。

---

# 79. Payment Exists but Coverage Disputed

例如 insurer provisional payment。

因此 payment state與 legal state分離。

---

# 80. Partial Payment

$$
Payment<Loss.
$$

剩餘 loss需其他 sources。

---

# 81. Uninsured Loss

若：

$$
Loss>CoverageCapacity,
$$

company capital可能承擔。

---

# 82. Insolvency Risk

若：

$$
Loss>CompanyCapital+Insurance,
$$

可能出現 insolvency / undercompensation。

---

# 83. Compensation Adequacy

定義：

$$
\boxed{
A_C
=
\frac{
AvailableCompensationCapacity
}{
EstimatedLoss
}
}
$$

---

# 84. Adequate Compensation

$$
A_C\ge1.
$$

---

# 85. Underfunded Exposure

$$
A_C<1.
$$

表示 risk financing不足。

---

# 86. Underinsurance as Governance Failure

大量 autonomy部署若無足夠 financial responsibility：

$$
UnderinsuranceRisk\uparrow.
$$

---

# 87. Insurer Underwriting 因此關心 Company Capital

不僅看 technology。

---

# 88. Corporate Balance Sheet Matters

同一 robot system在不同公司：

$$
FinancialResilience
$$

不同。

---

# 89. Financial Responsibility Architecture

本文提出：

$$
\boxed{
FRA
=
(
Capital,
Retention,
Insurance,
Reinsurance,
Indemnity,
Reserve
)
}
$$

---

# 90. FRA 與 Responsibility Graph Bridge

可映射：

$$
ResponsibilityDomain
\rightarrow
FinancialSupport.
$$

---

# 91. Unsupported Responsibility Domain

如果某 high-risk domain有責任，卻沒有任何 financial support：

$$
FinancialGap(d)=1.
$$

---

# 92. Financial Closure

類似 Responsibility Closure：

$$
\boxed{
Closure_C(d)=1
}
$$

表示 material loss domain有至少一個可識別 financial compensation path。

---

# 93. Responsibility Closure ≠ Financial Closure

$$
\boxed{
Closure_R(d)
\neq
Closure_C(d).
}
$$

兩者都要。

---

# 94. Compensation Gap

若：

$$
Closure_R=1
$$

但：

$$
Closure_C=0,
$$

即：

> 知道誰負責，但沒人賠得起。

---

# 95. Attribution Gap

反之：

$$
Closure_C=1
$$

但：

$$
Closure_R=0,
$$

即：

> 有保險先賠，但根本不知道事故為何發生。

---

# 96. 雙閉合目標

理想：

$$
\boxed{
Closure_R(d)=1
\quad\land\quad
Closure_C(d)=1.
}
$$

---

# 97. Compensation Graph 的證據

包括：

- policy；
- contract；
- claim；
- payment receipt；
- reserve；
- subrogation；
- indemnity；
- court / settlement reference。

---

# 98. Compensation Receipt

每次 payment記錄：

```text
payment_id
claim_ref
payer_ref
payee_ref
amount
currency
coverage_basis
deductible_applied
limit_remaining
paid_at
status
```

---

# 99. Recovery Receipt

```text
recovery_id
original_payment_ref
recovering_party
target_party
amount
basis
status
```

---

# 100. Compensation Ledger

append-oriented。

不能事故後 silent rewrite。

---

# 101. Claim Timeline

$$
Reported
\rightarrow
Reserved
\rightarrow
Investigated
\rightarrow
Paid
\rightarrow
Recovered
\rightarrow
Closed.
$$

---

# 102. Disputed Claim

允許：

```text
disputed
```

並保存 competing evidence。

---

# 103. Responsibility Dispute vs Coverage Dispute

兩者不同。

---

# 104. Coverage Denial 不等於 No Responsibility

insurer不cover不代表 company無責任。

---

# 105. No Legal Fault 不等於 No Insurance Payment

某些 coverage可不以fault為必要條件。

本文只保留概念分離。

---

# 106. Contractual Allocation

vendor contracts可影響：

$$
Recovery.
$$

---

# 107. Indemnity

manufacturer / integrator可能 indemnify operator。

---

# 108. Waiver / Limitation

contract may cap recovery。

因此 final burden不是純技術責任圖決定。

---

# 109. Public Compensation Fund

極端 systemic AI loss可能需要：

$$
GovernmentFund.
$$

本文不主張一定建立，只保留 graph node。

---

# 110. Catastrophic Layer

如果 autonomous-system loss具有 systemic scale：

$$
PrivateInsuranceCapacity<Loss.
$$

可能需要：

- pooling；
- public backstop；
- catastrophe bonds；
- alternative risk transfer。

---

# 111. Systemic AI Risk 與 Compensation

shared foundation model failure可能同時打到很多 insureds。

這會耗盡 aggregate capacity。

---

# 112. Compensation Graph 因此需要 Reinsurance / Systemic Layer

不應只看 single claim。

---

# 113. Accumulation

$$
AggregateClaims
=
\sum_i Claim_i
+
CorrelationEffect.
$$

---

# 114. Correlation 影響 Capital

這直接接 Paper 06。

---

# 115. 公司為什麼可能支持 AI-specific Reserve

若 AI A 的 responsibility domain可穩定追蹤，

company可以：

$$
Reserve_A
$$

隔離 risk。

---

# 116. Reserve Improves Visibility

enterprise可以知道：

$$
RiskAdjustedReturn(A).
$$

---

# 117. Risk-Adjusted AI Profitability

定义：

$$
\boxed{
\Pi_A^{risk}
=
Revenue_A
-
OperatingCost_A
-
ExpectedLoss_A
-
InsuranceCost_A
-
CapitalCharge_A.
}
$$

---

# 118. 這比只看 AI 節省多少工資更成熟

autonomous system真正經濟價值需扣風險。

---

# 119. Compensation Data 改善 AI Capital Allocation

事故歷史可以更新：

$$
ExpectedLoss_A.
$$

---

# 120. Loss Experience

更安全 AI domain可獲得更低 capital charge / premium。

---

# 121. AI-specific Economic Signal

於是 AI identity開始連接：

- performance；
- loss；
- insurance；
- reserve；
- capital。

---

# 122. 這開始推動 Economic Subjecthood

仍不等於人格。

但形成：

$$
\boxed{
\text{Stable Economic Reference Unit}.
}
$$

---

# 123. Private Interest

公司股東可能支持這種 sub-account，因為更好：

- pricing；
- risk isolation；
- capital efficiency；
- transfer pricing；
- performance measurement。

---

# 124. Compensation Layer 是 Institutional Ratchet 中間層

$$
Responsibility
\rightarrow
Compensation
\rightarrow
Capital.
$$

---

# 125. 誰先賠的制度重要性

受害人不會因為 Responsibility Graph很漂亮就自動得到錢。

因此 compensation architecture是現實必要層。

---

# 126. 誰最後承擔損失

最终：

$$
FinalBurden
$$

可能由：

- company；
- insurer；
- vendor；
- manufacturer；
- shareholder；
- state；
- AI-linked reserve；

共同承擔。

---

# 127. Final Burden Attribution

這是比 responsibility更後端的經濟結果。

---

# 128. Compensation Efficiency

可定义：

$$
E_C
=
f(
PaymentSpeed,
Adequacy,
TransactionCost,
RecoveryEfficiency
).
$$

---

# 129. Fast Payment vs Accurate Allocation

存在 trade-off。

---

# 130. Provisional Payment

制度可允許先賠後查。

但需 fraud / recovery controls。

---

# 131. Claims Automation

未來 AI可自動處理 claims。

但 claims AI本身又需要 responsibility / audit。

形成遞歸制度。

---

# 132. Compensation Graph 也可能由 AI 維護

但 canonical authority仍由 insurer / company / law決定。

---

# 133. AI 不能自行認定自己免賠

同样：

$$
AIClaim
\neq
CanonicalLiabilityDecision.
$$

---

# 134. 可證偽命題一：Responsibility vs Payment

現實事故中，responsible actor與first payer是否經常不同？

---

# 135. 可證偽命題二：Corporate Capacity

enterprise-scale autonomous loss是否更多依賴 company / insurance capital，而非 individual employee assets？

---

# 136. 可證偽命題三：RG Financial Value

Responsibility Graph是否提高 subrogation / recovery效率？

---

# 137. 可證偽命題四：Financial Closure

高 autonomy firms是否開始建立明確 loss-financing architecture？

---

# 138. 可證偽命題五：AI Reserve

是否出現 AI/fleet/domain-specific reserve？

---

# 139. 可證偽命題六：Risk-Adjusted Performance

企業是否開始按 AI-specific expected loss / insurance cost評估 profitability？

---

# 140. 可證偽命題七：Victim-Facing Simplicity

single compensation interface是否降低 transaction cost？

---

# 141. 可證偽命題八：Systemic Backstop

systemic AI losses是否推動 reinsurance / public-private pooling？

---

# 142. 反例條件

若：

- 絕大多數 autonomous losses可由單一自然人有效賠償；
- responsibility與first payer幾乎總是同一 actor；
- insurer / company無需回收 / subrogation；
- AI-specific reserve沒有經濟價值；

則本文分層的重要性應下修。

---

# 143. 第一代 Compensation Graph 實驗

沿用 warehouse fixture：

```text
company
supervisor
fleet AI
robot vendor
software vendor
insurer
reinsurer
claimant
```

---

# 144. 模擬 Incident A

robot collision造成：

$$
Loss=1M.
$$

---

# 145. Responsibility Graph

顯示：

- operator supervision；
- vendor software defect；
- maintenance delay。

---

# 146. Compensation Graph

設：

```text
company deductible = 100k
insurer pays = 700k
vendor indemnity recovery = 200k
```

---

# 147. Observe

同一事故中：

$$
Responsibility
\neq
PaymentFlow.
$$

---

# 148. 模擬 Incident B

common firmware bug造成：

$$
100\ robots
$$

同時 loss。

測試 aggregate limits / reinsurance。

---

# 149. 模擬 Incident C

employee override造成 loss。

比較 personal responsibility vs corporate first payment。

---

# 150. 測量

```text
time_to_compensate
coverage_gap
financial_closure
recovery_rate
subrogation_confidence
victim_transaction_cost
company_retention
insurer_loss
final_burden_distribution
```

---

# 151. Minimum Compensation Invariants

## CP-1

$$
\boxed{
Responsibility
\neq
Compensation.
}
$$

## CP-2

$$
\boxed{
ResponsibilityWeight
\neq
FinancialResponsibilityCapacity.
}
$$

## CP-3

$$
\boxed{
Liability
\neq
Coverage.
}
$$

## CP-4

$$
\boxed{
Coverage
\neq
Payment.
}
$$

## CP-5

$$
\boxed{
Payment
\neq
FinalEconomicBurden.
}
$$

## CP-6

$$
\boxed{
InsurancePayment
\not\Rightarrow
OperationalResponsibility.
}
$$

## CP-7

$$
\boxed{
SingleCompensationInterface
\neq
SingleResponsibleActor.
}
$$

## CP-8

$$
\boxed{
Employee
\neq
EnterpriseCapitalBuffer.
}
$$

## CP-9

$$
\boxed{
CompensationGraph
\neq
CapitalGraph.
}
$$

## CP-10

$$
\boxed{
Closure_R
\neq
Closure_C.
}
$$

---

# 152. Financial Closure Principle

本文提出：

$$
\boxed{
\textbf{Financial Closure Principle}
}
$$

弱形式：

> **對每個 material autonomous-risk domain，系統不只應知道誰負有責任，也應能識別至少一條足以處理合理損失規模的 compensation / risk-financing path。**

---

# 153. Responsibility–Compensation Separation Principle

$$
\boxed{
\textbf{Responsibility–Compensation Separation Principle}
}
$$

弱形式：

> **責任歸因用於解釋治理、行為與因果責任；補償結構用於確保受害人獲得實際支付能力。兩者應彼此橋接，但不得被壓縮為同一圖、同一比例或同一 actor。**

---

# 154. Loss-Absorption Alignment Principle

$$
\boxed{
\textbf{Loss-Absorption Alignment Principle}
}
$$

弱形式：

> **企業級 autonomous exposure 應由與其規模匹配的 company capital、insurance、retention、reserve、indemnity 或其他 financial responsibility mechanisms 承擔，而不應以單一自然人的名義責任替代實際 loss-absorbing capacity。**

---

# 155. Compensation Reconstruction Principle

$$
\boxed{
\textbf{Compensation Reconstruction Principle}
}
$$

弱形式：

> **重大 incident 應能重建事故發生時的 responsibility state、coverage state、financial capacity 與 subsequent payment / recovery path。**

---

# 156. 與 Paper 00 的關係

Paper 00提出 Compensation / Capital Ratchet。

本文建立中間的 financial-flow layer。

---

# 157. 與 Paper 01 的關係

Execution Graph提供 factual incident evidence。

---

# 158. 與 Paper 02 的關係

RCD解釋為什麼不能把 enterprise exposure全壓給一個 human。

---

# 159. 與 Paper 03 的關係

Responsibility Graph提供 attribution evidence。

---

# 160. 與 Paper 04 的關係

Insurance Graph提供 coverage / underwriting substrate。

---

# 161. 與 Paper 06 的關係

下一篇將從：

$$
Compensation
$$

進一步進入：

$$
\boxed{
CapitalFollowsAutonomy.
}
$$

即 AI-specific reserve / economic account / first-loss capital。

---

# 162. 與 Paper 07 的關係

一旦 AI-specific capital帶來 shareholder / insurance / tax利益，就會產生 Institutionalization Dividend。

---

# 163. 與 Paper 08 的關係

Responsibility、Insurance、Compensation、Capital最終共同推動 AI limited institutional standing。

---

# 164. Paper 05 的最終命題

本文提出：

$$
\boxed{
\textbf{Responsibility–Compensation Separation Thesis}
}
$$

弱形式為：

> **在高自主、多 actor、企業級 risk system 中，責任歸因、法律／契約責任、保險 coverage、實際 payment、subrogation / recovery 與最終經濟負擔應被視為不同層級。把某個 human supervisor 或 AI actor 標為 responsible，並不能自動證明其具有足以承受企業級損失的支付能力；穩定的 autonomous deployment 因此需要與 risk scale 相匹配的 enterprise-level compensation architecture。**

---

# 165. 更简洁的形式

$$
\boxed{
\text{Who caused / governed}
\neq
\text{Who pays first}
\neq
\text{Who bears the final loss}.
}
$$

---

# 166. 最終結論

具身 AI 時代若只建立 Responsibility Graph，還不夠。

因為事故發生後，真正現實的問題是：

> 受害人從哪裡拿到錢？

如果回答仍是：

> 「找那個名義上負責的主管。」

而事故 scale 是：

$$
Loss_{\max}
\gg
Assets_H,
$$

那麼制度並沒有真正建立補償能力。

它只是把 enterprise-scale risk 在組織圖上塞給一個 natural person。

因此：

$$
\boxed{
\text{Responsibility Attribution}
\neq
\text{Compensation Capacity}.
}
$$

成熟的 autonomous-risk architecture 必須同時有：

$$
\boxed{
\text{Responsibility Closure}
}
$$

以及：

$$
\boxed{
\text{Financial Closure}.
}
$$

前者回答：

> 誰負什麼責任？

後者回答：

> 真出事時，哪條 financial path 能支付？

所以未來更完整的事故鏈條不是：

$$
Incident
\rightarrow
ResponsiblePerson.
$$

而是：

$$
\boxed{
Incident
\rightarrow
Responsibility
\rightarrow
Liability
\rightarrow
Coverage
\rightarrow
Payment
\rightarrow
Recovery
\rightarrow
FinalBurden.
}
$$

這套分離一旦建立，會直接把我們推向下一篇的問題。

因為如果一個 autonomous AI / fleet / embodied execution domain 長期擁有穩定的：

- risk profile；
- expected loss；
- insurance premium；
- deductible；
- maintenance cost；
- revenue；
- reserve need；

企業自然會開始問：

> **為什麼不把這些 financial states直接綁定到這個 AI responsibility domain？**

一旦出現：

$$
Reserve_A,
InsuranceContribution_A,
FirstLossCapital_A,
UpgradeFund_A,
$$

就從 Compensation Layer進入了 Capital Layer。

這正是下一篇：

$$
\boxed{
\text{Capital Follows Autonomy}.
}
$$

---

## 系列進度

1. **Paper 00 — 從能力不可凍結到制度不可逆：UFI 之後的第二條 AI 棘輪**
2. **Paper 01 — 從 Conversation Graph 到 Embodied Execution Graph：分散式 AI 如何跨多具身端點行動**
3. **Paper 02 — 責任—控制背離：高自主系統為什麼不能把全部責任壓回一個人類主管**
4. **Paper 03 — Responsibility Graph：分散式具身 AI 的設計、授權、委派、執行與維護責任拓撲**
5. **Paper 04 — Machine Insurability Infrastructure：為什麼保險可能比法律更早逼出 AI 責任架構**
6. **Paper 05 — 誰負責不等於誰先賠：AI 時代的 Responsibility–Compensation Separation**
7. **Paper 06 — Capital Follows Autonomy：為什麼高自主 AI 可能開始需要自己的經濟帳戶與責任資本**
8. **Paper 07 — 私人利益如何創造 AI 經濟主體：股東、保險、會計與稅制的內生激勵**
9. **Paper 08 — 制度棘輪：從工具 AI 到責任實體、經濟實體與有限法律主體**

---

## 內部理論銜接

本文直接承接：

- Responsibility Graph；
- Machine Insurability Infrastructure；
- Responsibility–Control Divergence；
- Embodied Execution Graph；
- Institutional AI Ratchet。

本文新增核心抽象：

$$
\boxed{
\mathcal G^{C}
=
(
V_C,
E_C,
\Theta_C,
\Pi_C
)
}
$$

與：

$$
\boxed{
FRA
=
(
Capital,
Retention,
Insurance,
Reinsurance,
Indemnity,
Reserve
)
}
$$

以及：

$$
\boxed{
\text{Who is responsible}
\neq
\text{Who pays first}
\neq
\text{Who bears the final loss}.
}
$$
