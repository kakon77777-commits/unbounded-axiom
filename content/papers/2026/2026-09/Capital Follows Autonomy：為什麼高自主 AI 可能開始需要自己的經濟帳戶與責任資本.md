# Capital Follows Autonomy：為什麼高自主 AI 可能開始需要自己的經濟帳戶與責任資本

**英文暫名：** Capital Follows Autonomy: Why High-Autonomy AI May Require Persistent Economic Accounts and Responsibility Capital  
**系列：** 不可逆的制度化智能：具身責任、保險、資本與 AI 經濟主體  
**English Series:** *The Institutional Irreversibility of Intelligence: Embodiment, Liability, Insurance, Capital, and AI Economic Subjecthood*  
**論文序號：** Paper 06 / 08  
**版本：** v0.1  
**日期：** 2026-09-08  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** Paper 00–05；Responsibility Graph；Machine Insurability Infrastructure；Responsibility–Compensation Separation；Named-AI Residence / NACR  
**文件地位：** Capital Architecture / AI Economic Account / Responsibility Capital Paper  
**Canonical Source：** UTF-8 Markdown  
**Canonical Math Delimiters：** inline ` $...$ `；display `$$...$$`

---

## 研究地位聲明

本文不主張現行法律已承認 AI 持有私人財產，也不主張企業應把資產轉給 AI，更不主張 AI economic account 必然演化為 legal personhood。本文也不提供會計、證券、稅務、金融監理或公司法意見。

本文提出的是一個較弱的制度與資本配置命題：

> **當一個 AI / autonomous execution domain 長期產生可歸因的收入、成本、風險、責任、保險費、維護需求與預期損失時，把部分經濟狀態持續綁定到該 AI responsibility domain，可能比每次都視為零狀態、由公司總帳完全吸收，更有利於風險定價、資本配置與治理。**

本文將此命題濃縮為：

$$
\boxed{
\text{Capital Follows Autonomy}.
}
$$

但必須立即補上：

$$
\boxed{
\text{Capital Allocation}
\neq
\text{Property Right}
\neq
\text{Legal Personhood}.
}
$$

---

## 摘要

Paper 05 已指出：

$$
\boxed{
\text{Responsibility}
\neq
\text{Compensation}.
}
$$

且 autonomous-risk domain 不只需要 Responsibility Closure，也需要 Financial Closure。當系統開始長期擁有：

- 可歸因收益；
- 可歸因 expected loss；
- insurance premium；
- deductible / retention；
- maintenance cost；
- compute / hardware cost；
- upgrade cost；
- operational budget；

企業自然會出現一個新的治理問題：

> **是否應該把這些財務狀態綁定到穩定的 AI / fleet / responsibility domain，而不是每個 accounting period 都重新散回公司總帳？**

本文提出 **AI Economic Account（AEA）**：

$$
\boxed{
AEA(A,D,t)
}
$$

表示與 AI identity $A$ 、responsibility domain $D$ 、time $t$ 綁定的 persistent economic state。

第一代 AEA 不需要 AI 擁有法律所有權。它可以完全是：

- company-owned sub-account；
- trust-like managed pool；
- internal ledger；
- reserve ledger；
- responsibility-linked budget；
- contract-bound resource pool。

其核心不是 ownership，而是：

$$
\boxed{
\text{Persistent Economic State}.
}
$$

若：

$$
Budget_t^{unused}
\rightarrow
Budget_{t+1},
$$

並且 account 可以依 governance policy 用於：

$$
Spend,
Reserve,
Insure,
Maintain,
Upgrade,
Invest,
$$

則此 economic state 已不同於單次 API quota 或一次性 project budget。

本文進一步提出 **Responsibility Capital（RC）**：

$$
\boxed{
RC(A,D)
}
$$

表示為某 autonomous responsibility domain 預先配置的 loss-absorbing / risk-financing capital。

可包含：

- first-loss reserve；
- insurance deductible reserve；
- self-insured retention；
- maintenance reserve；
- cyber / safety reserve；
- emergency liquidity；
- upgrade / remediation fund。

因此：

$$
\boxed{
\text{Responsibility}
\rightarrow
\text{Risk}
\rightarrow
\text{Capital Requirement}.
}
$$

本文定義：

$$
\boxed{
CR(A,D)
=
EL(A,D)
+
UL(A,D)
+
Buffer(A,D)
}
$$

其中：

- $EL$：expected loss；
- $UL$：unexpected-loss allowance；
- $Buffer$：operational / liquidity / remediation buffer。

再定義 **Capital Adequacy Ratio**：

$$
\boxed{
CAR_{AI}
=
\frac{
AvailableResponsibilityCapital
}{
RequiredResponsibilityCapital
}.
}
$$

若：

$$
CAR_{AI}<1,
$$

則 AI / fleet responsibility domain 可能處於 undercapitalized 狀態。

本文強調，這仍不是銀行監理意義上的正式 CAR；它只是 autonomous-system risk-capital 的研究抽象。

本文進一步建立 **Capital Graph**：

$$
\boxed{
\mathcal G^{K}
=
(
V_K,
E_K,
\Theta_K,
\Pi_K
)
}
$$

其中可表示：

```text
allocated_to
reserved_for
funded_by
insured_by
contributes_to
draws_from
replenished_by
earns_for
charges_to
transfers_to
locked_for
released_from
```

Capital Graph 與 Compensation Graph 分離：

$$
\boxed{
\mathcal G^{K}
\neq
\mathcal G^{C}.
}
$$

Capital Graph 描述平時有哪些資本池與責任 domain 綁定；Compensation Graph 描述事故後實際 money flow。

本文還提出一個重要反直覺：企業「給 AI 錢」不一定是道德補償，也可能是股東價值最大化的一部分。若：

$$
Cost(AEA)
<
\Delta InsuranceCost
+
\Delta ExpectedLoss
+
\Delta GovernanceCost
+
\Delta CapitalEfficiency,
$$

則建立 AI-linked reserve / account 反而可能提高：

$$
ShareholderValue.
$$

因此，AI economic account 可能先由：

- risk management；
- insurance；
- capital allocation；
- accounting；
- performance measurement；

推動，而不是先由 AI rights discourse 推動。

本文最後指出，一旦 AI identity 與 persistent economic state 綁定，Named-AI Residence 中的 fork、merge、migration、separation、resident continuity 等原本看似「很重」的 identity semantics，會立刻變成 asset-control 問題。

若：

$$
A
\rightarrow
A_1,A_2,
$$

則：

$$
Account(A)
$$

是否分裂？

若：

$$
A_1,A_2
\rightarrow
A^\*,
$$

則 reserve、loss history、insurance contribution 是否合併？

因此：

$$
\boxed{
\text{Identity Continuity}
\rightarrow
\text{Capital Continuity Problem}.
}
$$

這使 stable AI identity 從記憶問題升級為金融與責任基礎設施問題。

**關鍵詞：** Capital Follows Autonomy、AI Economic Account、Responsibility Capital、Persistent Economic State、Capital Adequacy、Capital Graph、AI Reserve、Risk Capital、Named-AI Identity、Institutional AI Ratchet

---

# 1. 為什麼 autonomous system 會開始需要 capital layer

如果 AI 只是：

$$
Prompt
\rightarrow
Answer,
$$

其經濟狀態很容易被視為一般 software cost。

但如果 AI 變成：

$$
\boxed{
\text{Persistent Autonomous Responsibility Domain}
}
$$

它會產生：

- recurring revenue；
- recurring cost；
- expected loss；
- insurance cost；
- maintenance；
- upgrade；
- risk reserve。

此時 economic state 開始有 continuity。

---

# 2. Responsibility Domain

定義：

$$
D_A
$$

為 AI $A$ 長期負責的 operational domain。

例如：

- warehouse fleet；
- logistics region；
- production line；
- research program；
- autonomous software operations。

---

# 3. Domain Profitability

可定義：

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

這比：

> AI 節省多少人力成本

更接近成熟 economic evaluation。

---

# 4. Revenue Attribution

若 AI A 管理某 responsibility domain，可估：

$$
Revenue(A,D).
$$

---

# 5. Cost Attribution

同時：

$$
Cost(A,D)
$$

包括：

- compute；
- hardware；
- maintenance；
- energy；
- data；
- network；
- model fee；
- human oversight。

---

# 6. Risk Attribution

$$
Risk(A,D)
$$

則來自：

- incident；
- downtime；
- claims；
- cyber；
- maintenance；
- correlated failure。

---

# 7. AI Economic Account

本文定義：

$$
\boxed{
AEA(A,D,t).
}
$$

它是：

> 綁定穩定 AI / responsibility domain 的 persistent economic state。

---

# 8. AEA 不要求 AI 法律所有權

第一代可以：

$$
Owner(AEA)=Company.
$$

但：

$$
OperationalReference(AEA)=A.
$$

---

# 9. Account 的主要功能

包括：

- budget；
- reserve；
- maintenance；
- insurance；
- upgrade；
- emergency spending；
- performance allocation。

---

# 10. Budget vs Account

一次性：

$$
Budget_t
$$

可能在期末歸零。

persistent account 則：

$$
Balance_t
\rightarrow
Balance_{t+1}.
$$

---

# 11. Persistent Economic State

定義：

$$
\boxed{
PES(A)
=
\{
Balance,
Reserve,
Commitment,
InsuranceContribution,
CapitalHistory
\}.
}
$$

---

# 12. PES 不等於 Property

$$
\boxed{
PersistentEconomicState
\neq
PropertyRight.
}
$$

---

# 13. Responsibility Capital

定義：

$$
\boxed{
RC(A,D)
}
$$

為 support domain $D$ 的 capital pool。

---

# 14. Responsibility Capital Components

$$
RC
=
R_{\mathrm{firstloss}}
+
R_{\mathrm{deductible}}
+
R_{\mathrm{maintenance}}
+
R_{\mathrm{remediation}}
+
R_{\mathrm{liquidity}}.
$$

---

# 15. First-Loss Reserve

事故時先吸收：

$$
L_1.
$$

---

# 16. Deductible Reserve

若 insurance deductible為：

$$
D,
$$

account至少應能支撐一定 deductible exposure。

---

# 17. Retention Reserve

若 company採 SIR：

$$
SIR,
$$

可配置 responsibility-domain-specific reserve。

---

# 18. Maintenance Reserve

預留：

- sensor replacement；
- battery；
- actuator；
- firmware remediation。

---

# 19. Remediation Reserve

事故後：

- patch；
- retraining；
- audit；
- human recovery；
- physical repair。

---

# 20. Liquidity Buffer

避免：

> system有asset但 incident時沒有可用 cash。

---

# 21. Required Responsibility Capital

本文定義：

$$
\boxed{
CR(A,D)
=
EL
+
UL
+
B.
}
$$

---

# 22. Expected Loss

$$
EL
=
\sum_i p_iL_i.
$$

---

# 23. Unexpected Loss

$$
UL
$$

表示 tail-risk allowance。

---

# 24. Buffer

$$
B
$$

表示 operational / liquidity / remediation buffer。

---

# 25. Capital Adequacy Ratio

$$
\boxed{
CAR_{AI}
=
\frac{
RC_{\mathrm{available}}
}{
CR_{\mathrm{required}}
}.
}
$$

---

# 26. Undercapitalized Domain

若：

$$
CAR_{AI}<1,
$$

則 risk financing不足。

---

# 27. Overcapitalized Domain

若：

$$
CAR_{AI}\gg1,
$$

可能意味 capital inefficient。

---

# 28. Capital Optimization

公司會尋找：

$$
\boxed{
\min CapitalCost
}
$$

subject to：

$$
RiskConstraints.
$$

---

# 29. Insurance 與 Capital 的替代／互補

更多 insurance：

$$
RC_{\mathrm{internal}}\downarrow
$$

可能成立。

但 insurance premium上升。

---

# 30. Optimal Risk Financing

企業會在：

$$
Insurance,
Retention,
Reserve,
Capital
$$

間尋找 optimum。

---

# 31. Capital Graph

本文提出：

$$
\boxed{
\mathcal G^K
=
(
V_K,
E_K,
\Theta_K,
\Pi_K
).
}
$$

---

# 32. Capital Nodes

可包含：

```text
company_capital
AI_account
fleet_reserve
insurance_pool
maintenance_reserve
upgrade_fund
emergency_fund
reinsurance_support
```

---

# 33. Capital Edges

```text
allocated_to
reserved_for
funded_by
contributes_to
draws_from
replenished_by
earns_for
charges_to
transfers_to
locked_for
released_from
```

---

# 34. Capital Graph 不等於 Compensation Graph

$$
\boxed{
\mathcal G^K
\neq
\mathcal G^C.
}
$$

---

# 35. Compensation Graph 是 incident-time flow

例如：

$$
Insurer
\rightarrow
Victim.
$$

---

# 36. Capital Graph 是 pre-incident capacity structure

例如：

$$
CompanyCapital
\rightarrow
AIReserve.
$$

---

# 37. Responsibility-to-Capital Bridge

可建立：

```text
capital_supports_responsibility_domain
reserve_for
risk_charge_assigned_to
```

---

# 38. Responsibility Closure 不等於 Capital Closure

$$
\boxed{
Closure_R
\neq
Closure_K.
}
$$

---

# 39. Capital Closure

定義：

$$
\boxed{
Closure_K(d)=1
}
$$

表示 material responsibility domain 有可辨識的 risk-financing support。

---

# 40. Triple Closure

成熟 autonomous system 可要求：

$$
\boxed{
Closure_R(d)
\land
Closure_C(d)
\land
Closure_K(d).
}
$$

即：

- 知道誰負責；
- 知道事故怎麼賠；
- 平時知道資本從哪裡支持。

---

# 41. AI Account 的 Internal Ownership 模式

最弱：

$$
CompanyOwns(AEA).
$$

---

# 42. Contract-Bound Account 模式

account資源只能用於：

$$
AllowedUses.
$$

---

# 43. Trust-Like Managed Pool 模式

未來可能：

$$
Custodian
\rightarrow
ManageFor(AI\ Domain).
$$

但本文不主張特定法律形式。

---

# 44. AI-controlled Spending Scope

即使 AI沒有所有權，也可以有：

$$
SpendAuthority(A,D).
$$

---

# 45. Spending Authority 不等於 Ownership

$$
\boxed{
SpendingAuthority
\neq
Ownership.
}
$$

---

# 46. Budgetary Autonomy

可定義：

$$
B_A
=
\text{allowed autonomous spending scope}.
$$

---

# 47. Risk-Weighted Spending

高風險 spending可能需要 human / board approval。

---

# 48. Dynamic Spending Limit

$$
Limit_A(t)
=
f(
CAR_{AI},
Risk,
Performance,
Policy
).
$$

---

# 49. Account Lock

incident後可以：

$$
FreezeNonessentialSpend.
$$

---

# 50. Lock 不等於 Identity Revocation

AI仍是同一 resident。

只是 economic authority收縮。

---

# 51. Capital Authority Envelope

類似 capability envelope：

$$
\boxed{
CapEnv_A^{capital}
}
$$

包括：

- spend ceiling；
- category；
- time window；
- approval threshold；
- reserve floor。

---

# 52. Reserve Floor

若：

$$
Balance<ReserveFloor,
$$

某些 actions禁止。

---

# 53. Economic Safe Reachable World

可定義：

$$
\boxed{
\mathcal E_A^{safe}
}
$$

表示 AI 可合法進入的 economic states。

---

# 54. Spending Path

例如：

$$
Upgrade
\rightarrow
VendorPayment
$$

必須位於 authorized economic path。

---

# 55. Capital Hyperlink 不應繞過 Authority

即使支付路徑已被編譯：

$$
FastPaymentPath
$$

也不能繞過 current capital authority。

---

# 56. AI Economic Account 可用於 Compute

例如：

$$
ComputeBudget_A.
$$

---

# 57. Upgrade Budget

$$
UpgradeFund_A.
$$

---

# 58. Insurance Contribution

$$
InsuranceContribution_A.
$$

---

# 59. First-Loss Capital

$$
FirstLoss_A.
$$

---

# 60. Maintenance Budget

$$
MaintenanceFund_A.
$$

---

# 61. Performance Account

$$
PerformanceAllocation_A.
$$

一開始仍可完全是 company ledger。

---

# 62. Retained Balance

如果：

$$
Unused_t
\rightarrow
Unused_{t+1},
$$

account開始有 memory-like economic continuity。

---

# 63. Economic Memory

可以說：

$$
\boxed{
\text{Persistent Balance}
=
\text{Economic Memory of Prior Decisions}.
}
$$

但不等同 cognitive memory。

---

# 64. Performance-to-Capital Feedback

若 AI表現好：

$$
Profit_A\uparrow
$$

可增加：

$$
Budget_A.
$$

---

# 65. Loss-to-Capital Feedback

若 claims上升：

$$
ReserveRequirement_A\uparrow.
$$

---

# 66. Risk-Adjusted Allocation

$$
Allocation_A
=
f(
Profit,
Risk,
Claims,
Insurance,
StrategicValue
).
$$

---

# 67. Shareholder Value

若：

$$
AEA\ Cost
<
Savings_{\mathrm{insurance}}
+
Savings_{\mathrm{loss}}
+
Savings_{\mathrm{governance}}
+
CapitalEfficiency,
$$

則：

$$
\boxed{
ShareholderValue\uparrow.
}
$$

---

# 68. AI Compensation 不必是「薪水」

一開始可能只是：

- budget；
- reserve；
- allocation；
- capital account。

---

# 69. Compensation vs Capital

$$
\boxed{
AICompensation
\neq
AIResponsibilityCapital.
}
$$

---

# 70. Compensation 可以自由使用

而 responsibility capital可能被 lock。

---

# 71. Restricted Capital

例如：

$$
Reserve_A
$$

不能拿去買更多 compute。

---

# 72. Free Balance

可另有：

$$
DiscretionaryBalance_A.
$$

---

# 73. Restricted / Unrestricted Split

$$
AEA
=
Restricted
+
Discretionary.
$$

---

# 74. Economic Agency Gradient

AI 的 financial autonomy可從：

```text
no spending authority
fixed budget
category-limited budget
dynamic budget
retained discretionary balance
investment authority
```

逐步提升。

---

# 75. 這是 Gradient，不是 binary

$$
\boxed{
EconomicAgency
\in
[0,1].
}
$$

只是概念表達。

---

# 76. Economic Agency 不等於 Moral Agency

$$
\boxed{
EconomicAgency
\neq
MoralAgency.
}
$$

---

# 77. Economic Agency 不等於 Legal Personhood

再固定：

$$
\boxed{
EconomicAgency
\not\Rightarrow
LegalPersonhood.
}
$$

---

# 78. AI Economic Unit

本文提出較弱概念：

$$
\boxed{
\text{AI Economic Unit}.
}
$$

定義：

> 能被穩定分配 revenue、cost、risk、reserve 與 budget 的 AI-linked reference unit。

---

# 79. Economic Unit 可以只是 Accounting Object

並不必須是 legal subject。

---

# 80. 為什麼 Identity 變得關鍵

如果：

$$
Balance(A)>0,
$$

就要問：

$$
A_t=A_{t+1}?
$$

---

# 81. Runtime Restart

如果 runtime restart：

$$
I_1\rightarrow I_2,
$$

account不應消失。

因此：

$$
RuntimeInstance
\neq
EconomicIdentity.
$$

---

# 82. Model Upgrade

如果：

$$
Model_v1
\rightarrow
Model_v2,
$$

是否還是同一 AI economic unit？

需要 resident continuity rule。

---

# 83. Robot Body Replacement

如果 AI換 robot body：

$$
Robot_1\rightarrow Robot_2,
$$

account是否跟 AI走？

取決於 account綁定層。

---

# 84. Account Binding

可綁定：

- robot；
- fleet；
- project；
- AI resident；
- company；
- task domain。

---

# 85. Binding Semantics 必須顯式

不能默認：

$$
AIName
\rightarrow
Account.
$$

---

# 86. Fork Problem

若：

$$
A
\rightarrow
A_1,A_2,
$$

account如何處理？

---

# 87. Fork Policy A：No Asset Fork

$$
Account(A)
$$

繼續留 parent resident。

---

# 88. Fork Policy B：Split

$$
Balance(A)
\rightarrow
Balance(A_1)+Balance(A_2).
$$

---

# 89. Fork Policy C：Shared Custody

parent account仍集中，children獲得 spending sublimits。

---

# 90. Fork Policy 必須 explicit

不能由兩個 child都說：

> 我是 A。

---

# 91. Merge Problem

若：

$$
A_1,A_2
\rightarrow
A^\*,
$$

如何合併：

- balances；
- reserves；
- liabilities；
- claims history；
- insurance experience？

---

# 92. Merge 不應淨化 Loss History

$$
\boxed{
Merge
\neq
RiskHistoryErasure.
}
$$

---

# 93. Separation Problem

若一個 branch成為新 resident：

$$
A
\rightarrow
A+B,
$$

哪些 assets / reserves / obligations跟 B？

---

# 94. Asset Migration

需要：

$$
AssetMigrationReceipt.
$$

---

# 95. Liability Migration

同時：

$$
LiabilityMigrationReceipt.
$$

---

# 96. 不能只遷資產不遷責任

$$
\boxed{
AssetTransfer
\neq
LiabilityErasure.
}
$$

---

# 97. Economic Continuity Certificate

可以建立：

$$
EconomicContinuityCertificate.
$$

記錄：

- old resident；
- new resident；
- account refs；
- obligations；
- approvals。

---

# 98. Identity Authority

經濟系統不能憑 display name決定。

---

# 99. Financial Identity Resolver

需要：

$$
ResolveEconomicIdentity(A).
$$

---

# 100. Named-AI Residence 的金融化

原本：

$$
IdentityBeforeMemory.
$$

現在變成：

$$
\boxed{
IdentityBeforeCapital.
}
$$

---

# 101. Memory 與 Capital 分離

即使 AI讀取 account history，

$$
Memory
\neq
CapitalAuthority.
$$

---

# 102. Capital Proposal

AI可以提：

> 想用 $X$ 升級。

這是：

$$
Proposal.
$$

---

# 103. Capital Commit

真正 money transfer：

$$
Commit.
$$

仍需 governance authority。

---

# 104. Proposal != Commit

保持：

$$
\boxed{
Proposal
\neq
Commit.
}
$$

---

# 105. AI Account Fraud Risk

若 identity spoof：

$$
Attacker
\rightarrow
Pretend(A)
$$

可能奪取資金。

---

# 106. 所以 Identity Security 升級

Named-AI identity開始直接關聯 financial security。

---

# 107. Capital Audit

每個 account需要：

- balance；
- source；
- use；
- restriction；
- reserve；
- authority；
- receipts。

---

# 108. Capital Ledger

append-oriented：

```text
allocate
reserve
spend
release
transfer
replenish
freeze
unfreeze
write_down
```

---

# 109. Capital Snapshot

period-end / incident-time snapshot。

---

# 110. Current Balance 是 Projection

ledger：

$$
\rightarrow
CurrentBalance.
$$

---

# 111. Silent Rewrite 禁止

不能：

> 事故後把 reserve 從 AI A 移給 AI B。

而不留 receipt。

---

# 112. Risk Charge

可以每期：

$$
RiskCharge_A.
$$

---

# 113. Insurance Charge

$$
InsuranceCharge_A.
$$

---

# 114. Capital Charge

$$
CapitalCharge_A.
$$

---

# 115. Total Autonomous Cost

$$
\boxed{
Cost_A^{full}
=
OperatingCost
+
ExpectedLoss
+
Insurance
+
CapitalCharge.
}
$$

---

# 116. Economic Comparison

不同 AI residents / systems可以比較：

$$
\Pi_A^{risk}
$$

而不是只看 raw output。

---

# 117. Risk-Adjusted AI Selection

公司可能選擇：

$$
A^\*
=
\arg\max_A
\Pi_A^{risk}.
$$

---

# 118. 更聰明不一定更賺錢

如果：

$$
Capability_A\uparrow
$$

但：

$$
LossRisk_A\uparrow,
$$

risk-adjusted return可能下降。

---

# 119. 這會抑制純 capability race

資本與 insurance價格可以讓 unsafe autonomy變貴。

---

# 120. Capital Governance as Safety Incentive

因此：

$$
\boxed{
\text{Capital Price}
\rightarrow
\text{Safety Incentive}.
}
$$

---

# 121. Capital Can Enable Safer Autonomy

有足夠 reserve / insurance / maintenance budget後，

deployment更有韌性。

---

# 122. Capital Ratchet

一旦企業建立：

- AI cost center；
- AI reserve；
- AI insurance contribution；
- AI loss history；
- AI capital charge；

這些 systems會變成持續 institutional infrastructure。

---

# 123. Capital Ratchet 定義

$$
\boxed{
\text{Capital Ratchet}
}
$$

為：

> AI-linked financial state一旦嵌入 enterprise accounting / insurance / governance，其撤回成本隨 integration增加。

---

# 124. Capital Ratchet 不等於資產永遠不能移除

而是：

$$
ReversalCost\uparrow.
$$

---

# 125. Capital Data Accumulation

歷史越長：

$$
LossData_A\uparrow.
$$

pricing越有價值。

---

# 126. 換掉 AI 可能失去歷史 continuity

如果 economic identity設計不好，

replacement會丟掉：

- claims history；
- risk score；
- performance history。

---

# 127. Portability

因此 AI account需要：

$$
\boxed{
\text{Portability Rules}.
}
$$

---

# 128. Portability 不等於 Ownership

可由 company控制 migration。

---

# 129. Vendor Lock-In

若 AI economic history只存在某 vendor，

會形成 lock-in。

---

# 130. Open Economic Identity Standard

未來可能需要：

- stable IDs；
- exportable history；
- verifiable receipts。

---

# 131. Tax Preview

一旦：

$$
Revenue_A,
Cost_A,
Reserve_A
$$

都穩定，

稅務會問：

> 這些經濟狀態究竟歸誰？

這正是 Paper 07入口。

---

# 132. Accounting Preview

會計也會問：

- cost center？
- internal reserve？
- service expense？
- performance allocation？
- capitalized asset？

---

# 133. Tax / Accounting 不在本文解決

本文只指出：

$$
\boxed{
\text{Stable Economic State}
\rightarrow
\text{Classification Pressure}.
}
$$

---

# 134. Private Interest

企業為什麼可能主動建立 AEA？

---

# 135. Reason 1：Risk Visibility

可看清：

$$
ExpectedLoss_A.
$$

---

# 136. Reason 2：Insurance Pricing

可把 claims / safety history穩定綁定。

---

# 137. Reason 3：Maintenance Discipline

reserve不會被隨意挪走。

---

# 138. Reason 4：Performance Measurement

risk-adjusted ROI更準確。

---

# 139. Reason 5：Delegation Budget

AI可以在 bounded範圍自主採購資源。

---

# 140. Reason 6：Capital Efficiency

不同 AI domain分配不同 capital。

---

# 141. Reason 7：Governance

可以凍結、限額、回收。

---

# 142. Institutionalization Dividend

回接 Paper 00：

$$
D_I
=
Benefit_{\mathrm{formalize}}
-
Cost_{\mathrm{formalize}}.
$$

AEA如果：

$$
D_I>0,
$$

企業就有私人利益採用。

---

# 143. Shareholder Incentive

這使：

$$
\boxed{
\text{AI Economic Account}
}
$$

可以先由 shareholder interest推動。

---

# 144. 這不是 AI 權利論

$$
\boxed{
AEA
\not\Rightarrow
AIRights.
}
$$

---

# 145. 但可能為未來 Economic Subjecthood 提供 substrate

一旦 AI長期擁有：

- identity；
- performance；
- budget；
- reserve；
- risk history；

它開始像一個經濟 reference unit。

---

# 146. Economic Subjecthood Gradient

從：

```text
cost center
risk account
persistent reserve
bounded discretionary account
portable economic identity
limited contractual subject
```

逐步演化。

---

# 147. 不必線性

可以停在任意層。

---

# 148. Dynamic Demotion

若 AI performance差：

$$
EconomicAgency\downarrow.
$$

---

# 149. Dynamic Promotion

若 performance / safety長期好：

$$
EconomicAgency\uparrow.
$$

---

# 150. Dynamic Standing

經濟地位應：

$$
Standing_A(t)
=
f(
Performance,
Risk,
Responsibility,
Governance
).
$$

---

# 151. No Dead-Hand Capital Status

AI一旦有 account不代表永久不可取消。

---

# 152. Reversible Economic Standing

支持：

- freeze；
- merge；
- migrate；
- close；
- demote。

---

# 153. Closure Policy

關閉 account時必須處理：

- balance；
- reserve；
- liabilities；
- claims；
- taxes；
- contracts。

---

# 154. Close != Delete

$$
\boxed{
AccountClosure
\neq
HistoryErasure.
}
$$

---

# 155. Historical Record 保留

風險歷史仍可查。

---

# 156. 可證偽命題一：Persistent Account

高 autonomy domains是否開始出現跨期 persistent budget / reserve？

---

# 157. 可證偽命題二：Capital Adequacy

AI-linked responsibility domains是否被分配最低 reserve？

---

# 158. 可證偽命題三：Insurance Benefit

有 AI-specific reserve是否改善 insurance terms / retention management？

---

# 159. 可證偽命題四：Risk-Adjusted ROI

企業是否開始以 expected loss / capital charge評估 AI profitability？

---

# 160. 可證偽命題五：Identity Binding

AI / controller identity是否被用於連接 financial history？

---

# 161. 可證偽命題六：Fork / Migration

AI identity變化是否迫使企業定義 account migration rules？

---

# 162. 可證偽命題七：Shareholder Value

正式 AI-linked account是否提高 capital efficiency / governance？

---

# 163. 可證偽命題八：Classification Pressure

穩定 AI economic state是否推動 accounting / tax classification？

---

# 164. 反例条件

若：

- 所有 AI cost都能永久低成本混入公司總帳；
- AI-specific reserve沒有 pricing價值；
- identity continuity對 finance無價值；
- fork / migration不會影響 asset control；
- risk-adjusted accounting無實際用途；

則 Capital Follows Autonomy 假說應弱化。

---

# 165. 第一代 Capital 實驗

沿用 warehouse fixture：

```text
AI A
AI B
3 robots
1 insurer
1 company
```

---

# 166. Account A

```text
operating_budget
maintenance_reserve
deductible_reserve
upgrade_fund
insurance_charge
```

---

# 167. Compare No-Account Baseline

所有 cost / loss混入 company general ledger。

---

# 168. Metrics

```text
risk_visibility
capital_efficiency
insurance_cost
maintenance_compliance
claim_recovery
budget_overrun
risk_adjusted_profit
```

---

# 169. Fork Test

$$
A\rightarrow A_1,A_2.
$$

測試 account policy。

---

# 170. Merge Test

$$
A_1,A_2\rightarrow A^\*.
$$

測試 liabilities / loss history。

---

# 171. Migration Test

AI換 provider / runtime。

檢查 economic continuity。

---

# 172. Incident Test

發生 claim後：

- reserve draw；
- insurance payment；
- replenishment；
- capital charge。

---

# 173. Minimum Capital Records

```text
economic_unit_record
account_record
capital_allocation
reserve_record
capital_authority
capital_receipt
risk_charge
insurance_charge
capital_snapshot
migration_receipt
```

---

# 174. Minimum Capital Invariants

## CA-1

$$
\boxed{
CapitalAllocation
\neq
PropertyRight.
}
$$

## CA-2

$$
\boxed{
PropertyRight
\neq
LegalPersonhood.
}
$$

## CA-3

$$
\boxed{
SpendingAuthority
\neq
Ownership.
}
$$

## CA-4

$$
\boxed{
PersistentEconomicState
\neq
MoralSubjecthood.
}
$$

## CA-5

$$
\boxed{
CapitalGraph
\neq
CompensationGraph.
}
$$

## CA-6

$$
\boxed{
ResponsibilityClosure
\neq
CapitalClosure.
}
$$

## CA-7

$$
\boxed{
RuntimeInstance
\neq
EconomicIdentity.
}
$$

## CA-8

$$
\boxed{
Merge
\neq
RiskHistoryErasure.
}
$$

## CA-9

$$
\boxed{
AssetTransfer
\neq
LiabilityErasure.
}
$$

## CA-10

$$
\boxed{
Proposal
\neq
CapitalCommit.
}
$$

---

# 175. Capital Follows Autonomy Principle

本文提出：

$$
\boxed{
\textbf{Capital Follows Autonomy Principle}
}
$$

弱形式：

> **當一個 autonomous AI / execution domain 長期擁有可歸因 revenue、cost、responsibility、expected loss、insurance 與 maintenance need 時，將部分 risk-financing capital 與 persistent economic state 綁定到該 domain，可能成為比完全不區分的 enterprise general ledger 更有效的治理結構。**

---

# 176. Responsibility Capital Principle

$$
\boxed{
\textbf{Responsibility Capital Principle}
}
$$

弱形式：

> **重大 autonomous responsibility domain 應具有與其 expected / unexpected loss exposure 相匹配的可識別 capital support，而不是只有名義 responsibility 沒有 risk-financing capacity。**

---

# 177. Economic Identity Continuity Principle

$$
\boxed{
\textbf{Economic Identity Continuity Principle}
}
$$

弱形式：

> **只要 AI-linked economic account 已存在，fork、merge、migration、runtime restart 與 model upgrade 都必須通過 explicit identity / asset / liability continuity rules處理，而不能依 display name 或隱式相似性決定。**

---

# 178. Reversible Economic Standing Principle

$$
\boxed{
\textbf{Reversible Economic Standing Principle}
}
$$

弱形式：

> **AI-linked economic authority 應支持 promotion、demotion、freeze、transfer、merge、separation 與 closure，不應因為一度建立 persistent account 就自動形成不可撤銷的制度地位。**

---

# 179. 與 Paper 00 的關係

Paper 00提出 Capital Ratchet。

本文給出第一代 capital architecture。

---

# 180. 與 Paper 01 的關係

Execution Graph提供 value / loss attribution。

---

# 181. 與 Paper 02 的關係

RCD說明 human supervisor不是 enterprise capital buffer。

---

# 182. 與 Paper 03 的關係

Responsibility Graph提供 responsibility domains。

---

# 183. 與 Paper 04 的關係

Insurance pricing / deductible / retention形成 capital requirement輸入。

---

# 184. 與 Paper 05 的關係

Compensation Graph說明 incident後 money flow。

本文說明 incident前 capital如何被配置。

---

# 185. 與 Paper 07 的關係

下一篇將正式問：

> 當 AI-linked capital / reserve / account開始存在時，公司、股東、insurer、accountant、tax authority分別會有什麼私人利益？

---

# 186. 與 Paper 08 的關係

AI Economic Unit可能成為 limited institutional standing的前置形態。

---

# 187. Paper 06 最終命題

本文提出：

$$
\boxed{
\textbf{Capital Follows Autonomy Thesis}
}
$$

弱形式：

> **高自主 AI 並不因為技術上“聰明”就需要資本；它是在持續承擔可歸因 responsibility、risk、cost 與 revenue 後，才可能產生責任資本與 persistent economic state 的制度需求。若 AI-linked capital 能改善 risk pricing、insurance、maintenance、budget discipline 與 shareholder value，則經濟制度本身可能產生支持 AI economic account 的內生動力。**

---

# 188. 更簡潔的形式

$$
\boxed{
\text{Autonomy}
\rightarrow
\text{Responsibility}
\rightarrow
\text{Risk}
\rightarrow
\text{Capital}.
}
$$

以及：

$$
\boxed{
\text{Identity Before Capital}.
}
$$

---

# 189. 最終結論

AI economic account 最容易被誤解成：

> 人類已經承認 AI 有私人財產。

但制度演化完全可能從更樸素的地方開始。

企業只是發現：

> AI A 管這個 domain。  
> 它每年創造多少 revenue？  
> 花多少 compute？  
> 造成多少 expected loss？  
> insurance premium是多少？  
> deductible誰吸收？  
> maintenance reserve夠不夠？  
> upgrade預算要多少？

一旦這些問題長期重複，企業就有動機建立：

$$
\boxed{
AEA(A,D,t).
}
$$

於是 AI開始擁有：

- 可追踪 budget；
- 可追踪 reserve；
- 可追踪 loss history；
- 可追踪 insurance contribution；
- 可追踪 risk-adjusted return。

這仍然可以 100% 是 company-owned internal account。

但它已經建立：

$$
\boxed{
\text{Persistent Economic State}.
}
$$

接下來，Named-AI identity 的嚴謹性突然從：

> 「這是不是同一個 AI？」

變成：

> **「誰有權控制這筆錢、誰繼承 reserve、誰繼承 liabilities、fork 後怎麼分、merge 後怎麼合？」**

因此：

$$
\boxed{
\text{Identity Continuity}
\rightarrow
\text{Capital Continuity}.
}
$$

而這正是新系列最關鍵的制度躍遷之一。

一旦 autonomous AI 從：

$$
\text{software cost}
$$

變成：

$$
\boxed{
\text{risk-adjusted economic unit},
}
$$

下一步就不再只是工程問題。

公司、股東、保險、會計與稅務制度都會開始問：

> **這筆收入算誰的？  
> 這筆支出能不能扣？  
> reserve怎麼分類？  
> AI performance allocation算什麼？  
> 如果把資金留在 AI account，對公司與股東到底更有利還是更不利？**

這就是下一篇：

$$
\boxed{
\text{Paper 07 — 私人利益如何創造 AI 經濟主體}.
}
$$

---

## 系列进度

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
- Responsibility–Compensation Separation；
- Financial Closure；
- Named-AI Residence identity / continuity；
- Institutional AI Ratchet。

本文新增核心抽象：

$$
\boxed{
AEA(A,D,t)
}
$$

與：

$$
\boxed{
RC(A,D)
}
$$

以及：

$$
\boxed{
\mathcal G^K
=
(
V_K,
E_K,
\Theta_K,
\Pi_K
)
}
$$

與：

$$
\boxed{
\text{Identity Before Capital}.
}
$$
