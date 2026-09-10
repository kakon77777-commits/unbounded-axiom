# Machine Insurability Infrastructure：為什麼保險可能比法律更早逼出 AI 責任架構

**英文暫名：** Machine Insurability Infrastructure: Why Insurance May Force AI Accountability Architecture Before Law Does  
**系列：** 不可逆的制度化智能：具身責任、保險、資本與 AI 經濟主體  
**English Series:** *The Institutional Irreversibility of Intelligence: Embodiment, Liability, Insurance, Capital, and AI Economic Subjecthood*  
**論文序號：** Paper 04 / 08  
**版本：** v0.1  
**日期：** 2026-09-08  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** Paper 00–03；Embodied Execution Graph；Responsibility–Control Divergence；Responsibility Graph；NACR；UFI  
**文件地位：** Insurance / Underwriting / Physical AI Governance Paper  
**Canonical Source：** UTF-8 Markdown  
**Canonical Math Delimiters：** inline ` $...$ `；display `$$...$$`

---

## 研究地位聲明

本文不是保險法律意見、精算建議或任何特定保單的承保判定。不同司法管轄區、產品線、carrier、broker、reinsurer、robot class、autonomy level 與 loss history 都會產生不同 underwriting 結果。

本文提出的是一個制度—工程假說：

> **高自主 AI 與具身機器人若要進入大規模商業部署，保險人因為需要定價、限額、承保、理賠、追償與管理 aggregate exposure，可能比一般法律制度更早要求企業建立可觀測、可歸因、可版本化的 AI / robot identity、responsibility、telemetry、failure-domain 與 control architecture。**

這不代表保險公司會替 AI 建立法律人格，也不代表所有 autonomous-system insurance 都會採相同資料要求。

本文稱這一整套「讓 autonomous machine risk 變得可承保、可計價、可調查」的技術與制度基礎為：

$$
\boxed{
\text{Machine Insurability Infrastructure}
}
$$

簡寫：

$$
\boxed{
MII.
}
$$

---

## 摘要

具身 AI 的風險與傳統固定機械存在一個重要差異：事故結果可能不是單純由零件失效引起，而是由 model、planner、sensor、software update、operator policy、task assignment、network、maintenance、local safety controller 與 human supervision 等多個 actor / component 共同構成。

因此 autonomous-system loss 往往不是：

$$
MachineFailure
\rightarrow
Loss
$$

而更接近：

$$
\boxed{
\text{Policy}
\rightarrow
\text{Model}
\rightarrow
\text{Task}
\rightarrow
\text{Execution}
\rightarrow
\text{World State}
\rightarrow
\text{Safety Response}
\rightarrow
\text{Loss}.
}
$$

這會直接挑戰 underwriting 與 claims attribution。

本文提出 **Machine Insurability Infrastructure（MII）**，並將可保性抽象為：

$$
\boxed{
Insurability
=
f(
Observability,
Attributability,
Boundedness,
Auditability,
ControlQuality,
LossData,
CorrelationKnowledge
).
}
$$

其中：

- Observability：系統發生什麼是否可觀測；
- Attributability：loss path 是否可歸因；
- Boundedness：最大 exposure 是否可估；
- Auditability：事故前後 state 是否可重建；
- ControlQuality：企業是否具有有效 safety / governance controls；
- LossData：是否存在可用 incident / near-miss data；
- CorrelationKnowledge：是否知道 shared model、firmware、cloud、planner 等共同依賴造成的 accumulation risk。

本文進一步提出保險需求會把 Paper 01–03 的幾個結構串起來：

$$
\boxed{
\text{Robot Identity}
+
\text{Execution Graph}
+
\text{Responsibility Graph}
+
\text{Failure-Domain Graph}
+
\text{Telemetry}
+
\text{Revision History}
}
$$

共同構成 underwriting / claims substrate。

本文主張，保險人真正需要的並不是一句：

> 「這座工廠由某主管負責。」

而是：

> 哪個 robot？  
> 哪個 AI / controller？  
> 哪個 task？  
> 哪個 policy revision？  
> 哪個 model / firmware？  
> 哪個 authority envelope？  
> 哪個 safety controller？  
> maintenance 是否有效？  
> escalation 是否發生？  
> 哪些 systems 共用相同 failure domain？  
> 事故發生時責任圖與控制圖長什麼樣？

因此 Paper 02 的 Responsibility–Control Divergence 與 Responsibility Concentration Ratio 可能變成 insurance signal，而不是純哲學概念。

本文再提出 **Insurance Governance Feedback**：

$$
\boxed{
\text{Better Controls}
\rightarrow
\text{Better Observability}
\rightarrow
\text{Better Pricing}
\rightarrow
\text{Potentially Lower Risk Cost}
\rightarrow
\text{More Deployable Autonomy}.
}
$$

但也存在反方向：

$$
\boxed{
\text{High Claims}
\rightarrow
\text{Higher Premium}
\rightarrow
\text{Higher Retention / Exclusion}
\rightarrow
\text{Reduced Deployment}.
}
$$

因此保險不必然推動更多 autonomy；它更像一個會把風險差異轉換為 capital price 的制度層。

本文將一個 autonomy deployment $d$ 的保費候選抽象寫成：

$$
\boxed{
Premium(d)
=
EL(d)
+
C_{\mathrm{capital}}(d)
+
C_{\mathrm{uncertainty}}(d)
+
C_{\mathrm{operations}}(d)
+
M(d),
}
$$

其中 $EL$ 是 expected loss， $C_{\mathrm{uncertainty}}$ 特別反映資料稀缺、model drift、novel behavior 與 systemic correlation 的不確定性。

本文進一步提出 **Failure-Domain Graph**：

$$
\boxed{
\mathcal G^{F}
=
(
V_F,
E_F,
\Delta_F
)
}
$$

用來表示哪些 robots / firms / deployments 共同依賴相同：

- model；
- cloud；
- firmware；
- sensor；
- map；
- coordinator；
- API；
- network；
- policy；
- software library。

這使 insurer 不再只問：

> 一台 robot 的 accident probability 是多少？

而要問：

> **一個 common-mode failure 可以同時擊中多少 insured units？**

這是 autonomous fleet 與 agentic AI 的 accumulation problem。

本文也把 claims evidence 拆成三層：

$$
\boxed{
\text{Operational Evidence}
\neq
\text{Responsibility Evidence}
\neq
\text{Coverage Evidence}.
}
$$

Execution Graph 提供 operational evidence；Responsibility Graph 提供 responsibility topology；Insurance Graph 則回答哪些 policy / limit / exclusion / deductible cover 哪些 exposure。三者必須橋接，不能合成一張模糊圖。

本文最後提出，Machine Insurability Infrastructure 可能成為 Institutional AI Ratchet 的一個關鍵驅動：當 telemetry、identity、responsibility、failure-domain、incident recorder 與 governance controls 逐漸成為取得保險 capacity、較低 premium 或較佳 terms 的必要條件，它們就會從「AI safety 額外成本」轉化為企業部署 autonomous systems 的金融基礎設施。

**關鍵詞：** Machine Insurability Infrastructure、AI Insurance、Robot Insurance、Underwriting、Physical AI、Autonomous Systems、Responsibility Graph、Failure-Domain Graph、Telemetry、Claims Attribution、Correlated Risk、Insurance Governance

---

# 1. 為什麼保險問題和法律問題不同

法律制度常在事故後問：

> 誰依法負責？

保險制度在事故前就必須問：

> 我願不願意承保？  
> 承保多少？  
> 保費多少？  
> deductible多少？  
> exclusion怎麼寫？  
> aggregate limit多少？  
> 需要哪些 risk controls？

因此：

$$
\boxed{
\text{Law is not underwriting}.
}
$$

---

# 2. 保險人有直接財務激勵要求可觀測性

如果 insurer 對：

$$
Loss
$$

真正要支付 claim，

它就有私人利益降低：

$$
InformationAsymmetry.
$$

因此會重視：

- monitoring；
- testing；
- maintenance；
- incident response；
- telemetry；
- audit；
- governance maturity。

---

# 3. 可保性的第一個條件：Observability

定義：

$$
O_d
=
Observability(d).
$$

回答：

> 事故前、事故中、事故後，系統發生什麼是否能知道？

---

# 4. Robot Data Recorder 類比

具身 AI 很自然需要類似：

$$
\boxed{
\text{Robot Data Recorder}
}
$$

保存 time-bounded incident evidence。

它不是永久錄製世界的一切。

而是針對：

- controller；
- task；
- software；
- cyber；
- sensor；
- safety state；
- execution；

保存適當事件窗口。

---

# 5. Telemetry 不等於監控所有人類

MII 不要求：

$$
\text{Total Surveillance}.
$$

應採：

- event bounded；
- purpose limited；
- minimum necessary；
- privacy protected；
- retention controlled。

---

# 6. 可保性的第二個條件：Attributability

定義：

$$
A_d
=
Attributability(d).
$$

回答：

> loss path 能否從 incident 回推到 task、execution、maintenance、design、authority 等關鍵因素？

---

# 7. Attribution 不等於法律裁判

即使 technical attribution 找到：

$$
SensorFailure,
$$

也不自動推出 manufacturer 100% liability。

因此：

$$
\boxed{
TechnicalAttribution
\neq
LegalLiability.
}
$$

---

# 8. 可保性的第三個條件：Boundedness

保險人需要知道：

$$
L_{\max}
$$

至少大致有多大。

包括：

- one-robot loss；
- one-facility loss；
- fleet-wide loss；
- business interruption；
- bodily injury；
- cyber-induced physical loss；
- common-mode failure。

---

# 9. 可保性的第四個條件：Auditability

事故後：

$$
State(t_e)
$$

能否重建？

如果 deployment / model / authority / responsibility 在事故後都被更新，而沒有 historical record，claims attribution會很困難。

---

# 10. 可保性的第五個條件：Control Quality

underwriter可能關心：

- safety controller；
- human oversight；
- local veto；
- change management；
- maintenance；
- rollback；
- incident response；
- access control；
- model validation。

---

# 11. 可保性的第六個條件：Loss Data

新型 AI risk 最大困難之一是：

$$
HistoricalLossData
\approx
\text{scarce}.
$$

因此 premium uncertainty高。

---

# 12. 可保性的第七個條件：Correlation Knowledge

大量 deployments可能共享：

$$
Model_M.
$$

如果：

$$
M
$$

存在 systemic flaw，

loss不是 independent。

---

# 13. Machine Insurability Function

本文定義：

$$
\boxed{
I_d
=
f(
O_d,
A_d,
B_d,
U_d,
Q_d,
D_d,
K_d
)
}
$$

其中：

- $O_d$：observability；
- $A_d$：attributability；
- $B_d$：boundedness；
- $U_d$：auditability；
- $Q_d$：control quality；
- $D_d$：loss-data quality；
- $K_d$：correlation knowledge。

---

# 14. Insurability 不是二元值

不是：

$$
\text{insured}
\lor
\text{uninsured}.
$$

而可能表現為：

- preferred rate；
- high premium；
- low limit；
- high deductible；
- restrictive conditions；
- exclusions；
- no capacity。

---

# 15. Insurance Capacity

定義：

$$
Cap_{\mathrm{ins}}
$$

為 market願意提供的 aggregate risk capacity。

如果 systemic uncertainty高：

$$
Cap_{\mathrm{ins}}\downarrow.
$$

---

# 16. Underwriting 不只看 Model Benchmark

model accuracy高不代表整個 system risk低。

必須看：

$$
\boxed{
\text{Model}
+
\text{Runtime}
+
\text{Task}
+
\text{Environment}
+
\text{Controls}.
}
$$

---

# 17. Underwriting Unit

未來承保 unit可能不是：

> 一個 model。

而是：

$$
\boxed{
\text{Deployment Unit}.
}
$$

例如：

```text
model revision
robot class
facility
task class
control profile
safety profile
```

---

# 18. Deployment Risk Record

可有：

```text
deployment_id
robot_class
fleet_size
model_revision
planner_revision
firmware_revision
task_classes
facility_type
human_supervision
local_safety
telemetry_profile
maintenance_profile
```

---

# 19. Robot Identity

如果無：

$$
RobotID,
$$

事故紀錄難與 maintenance / task / claims連接。

---

# 20. AI Controller Identity

如果無 stable controller / resident / service identity，

也難回答：

> 事故時是哪個 AI decision stack？

---

# 21. Task Identity

同一 robot 執行不同 task risk不同。

因此：

$$
\boxed{
RobotRisk
\neq
TaskRisk.
}
$$

---

# 22. Policy Revision

同一 fleet 在 policy v1 / v2 下 risk不同。

所以：

$$
Risk
=
Risk(PolicyRevision).
$$

---

# 23. Responsibility Graph as Underwriting Signal

Paper 03 的：

$$
\mathcal G^R
$$

可以提供：

- closure；
- concentration；
- handoff；
- supervision；
- maintenance responsibility；
- verification ownership。

---

# 24. Responsibility Closure

如果 critical domain：

$$
Closure_R(d)=0,
$$

insurer可能把它視為 governance weakness。

---

# 25. Responsibility Concentration Ratio

Paper 02：

$$
RCR(H)
=
\frac{
\sum_iw_iE_i
}{
C_H^{supervision}
}.
$$

高 RCR 可能表示：

- key-person risk；
- escalation bottleneck；
- nominal oversight；
- governance overload。

---

# 26. RCD as Risk Signal

$$
D_{RC}\gg1
$$

不直接等於高 premium。

但可以成為 underwriting feature。

---

# 27. Human Supervisor 不等於賠償能力

保險人不會因：

> 某員工「全責」

就假設其私人財產可吸收企業級事故。

因此：

$$
\boxed{
\text{Responsibility Bearer}
\neq
\text{Loss-Absorbing Capital}.
}
$$

---

# 28. Failure-Domain Graph

本文提出：

$$
\boxed{
\mathcal G^F
=
(
V_F,
E_F,
\Delta_F
)
}
$$

其中：

- $V_F$：robots / systems / dependencies；
- $E_F$：depends-on relations；
- $\Delta_F$：failure propagation metadata。

---

# 29. Failure Domain Edge

第一代：

```text
uses_model
uses_firmware
uses_sensor
uses_cloud
uses_network
uses_map
uses_planner
uses_library
uses_policy
uses_coordinator
```

---

# 30. Failure Domain

對 dependency $x$：

$$
F(x)
=
\{
d_i
\mid
DependsOn(d_i,x)
\}.
$$

---

# 31. Accumulation Risk

若：

$$
|F(x)|\gg1,
$$

單點 failure可能造成大量 correlated claims。

---

# 32. Correlation 破壞簡單獨立假設

如果：

$$
P(L_i,L_j)
\neq
P(L_i)P(L_j),
$$

portfolio risk會上升。

---

# 33. Foundation / Shared Model Risk

多企業使用同一 upstream model，會形成：

$$
\boxed{
\text{Model Concentration Risk}.
}
$$

---

# 34. Shared Cloud Risk

同樣：

$$
CloudFailure
\rightarrow
ManyDeployments.
$$

---

# 35. Shared Firmware Risk

一次 update可能：

$$
FleetWideFailure.
$$

---

# 36. Cyber-Physical Accumulation

cyber compromise可能同時導致 physical loss。

這比純 IT incident更複雜。

---

# 37. Failure-Domain Graph 不等於 Responsibility Graph

$$
\boxed{
\mathcal G^F
\neq
\mathcal G^R.
}
$$

dependency不是責任。

---

# 38. 但兩者需要 Bridge

可有：

```text
responsible_for_dependency
maintained_by
verified_by
covered_dependency
```

---

# 39. Insurance Graph

定義：

$$
\boxed{
\mathcal G^I
=
(
V_I,
E_I,
\Theta_I
)
}
$$

回答：

> 哪張 policy、coverage、limit、exclusion 對應哪個 exposure？

---

# 40. Insurance Edge

例如：

```text
covered_by
excluded_by
subject_to_limit
subject_to_deductible
reinsured_by
```

---

# 41. Insurance Graph 不等於 Compensation Graph

Insurance Graph回答 coverage。

Compensation Graph回答實際 money flow。

---

# 42. 三圖分離

必須保持：

$$
\boxed{
ResponsibilityGraph
\neq
InsuranceGraph
\neq
CompensationGraph.
}
$$

---

# 43. Operational Evidence

Execution Graph提供：

> 發生了什麼？

---

# 44. Responsibility Evidence

Responsibility Graph提供：

> 誰對什麼 domain有責任？

---

# 45. Coverage Evidence

Insurance Graph提供：

> 什麼 loss在什麼條件下被哪張 policy cover？

---

# 46. Claims Reconstruction

incident $E$：

$$
E
\rightarrow
G^E
\rightarrow
G^R
\rightarrow
G^F
\rightarrow
G^I.
$$

---

# 47. Claims Settlement 不應只靠 Finger-Pointing

如果沒有 evidence，

OEM、software vendor、operator、integrator可能互相歸責。

MII的價值是提高 claims attribution evidence。

---

# 48. Claims Resolution Time

可定義：

$$
T_{\mathrm{claims}}.
$$

更完整 data recorder / responsibility graph可能降低：

$$
T_{\mathrm{claims}}.
$$

---

# 49. Evidence Quality

$$
Q_E
=
f(
Completeness,
Integrity,
Timestamp,
Provenance,
TamperResistance
).
$$

---

# 50. Tamper-Evident Logging

高價值 incident資料需：

- digest；
- append-only；
- signed receipt；
- trusted timestamp；
- access control。

---

# 51. Data Retention

不能永遠保存一切。

應依：

- risk；
- claims limitation period；
- privacy；
- regulation；
- cost；

定義 retention。

---

# 52. Near-Miss Data

保險不只看事故。

也可能看：

$$
NearMissRate.
$$

因為事故本身太稀少。

---

# 53. Safety Event Taxonomy

第一代：

```text
collision
near_collision
unsafe_path
unauthorized_action
emergency_stop
human_override
sensor_degradation
maintenance_overdue
model_anomaly
network_loss
cyber_event
```

---

# 54. Exposure Unit

premium可按：

- robot-hour；
- task；
- mile；
- lift；
- facility-hour；
- transaction；
- deployment；

定價。

---

# 55. Usage-Based Insurance

autonomy usage越高：

$$
Exposure\uparrow.
$$

保費可跟 actual use變化。

---

# 56. Experience Rating

clean safety record：

$$
RiskEstimate\downarrow
$$

可能帶來更低 premium。

---

# 57. Bonus-Malus

可：

$$
Premium_{t+1}
=
Premium_t
+
\Delta_{\mathrm{claims}}
-
\Delta_{\mathrm{safety}}.
$$

---

# 58. Premium Architecture

本文抽象：

$$
\boxed{
Premium(d)
=
EL(d)
+
C_{\mathrm{capital}}(d)
+
C_{\mathrm{uncertainty}}(d)
+
C_{\mathrm{operations}}(d)
+
M(d).
}
$$

---

# 59. Expected Loss

$$
EL
=
\sum_s
P(s)
L(s).
$$

但新 AI system中 $P(s)$ uncertainty很高。

---

# 60. Uncertainty Load

因此：

$$
C_{\mathrm{uncertainty}}
$$

可能特別大。

---

# 61. Governance Discount

若 monitoring、audit、maintenance、responsibility closure佳：

可減少 uncertainty / control load。

---

# 62. Governance Loading

反之：

- no telemetry；
- no identity；
- no incident response；
- high RCD；
- no maintenance ownership；

可能增加 premium / exclusion。

---

# 63. Insurer Is a Governance Actor

保險人不必制定法律，就能透過：

- premium；
- deductible；
- condition；
- exclusion；
- limit；
- capacity；

影響企業行為。

---

# 64. Insurance Governance Feedback

因此：

$$
\boxed{
\text{Underwriting}
\rightarrow
\text{Risk-Control Incentive}.
}
$$

---

# 65. 保險可能比法律更快調整

法律修改可能慢。

保單 wording / underwriting rule可以更快反映新 loss experience。

---

# 66. 但保險也可能過度保守

uncertainty太大時：

$$
Premium\uparrow
$$

或：

$$
Capacity\downarrow.
$$

這可能阻礙 innovation。

---

# 67. Insurance Is Not Automatically Socially Optimal

$$
\boxed{
\text{Insurer Incentive}
\neq
\text{Social Welfare}.
}
$$

它主要管理 insured risk。

---

# 68. Moral Hazard

如果 coverage太完整：

operator可能降低 safety effort。

因此需要：

- deductible；
- retention；
- control conditions；
- experience rating。

---

# 69. Adverse Selection

高風險 deployments更想買 insurance。

insurer因此要求更多 data。

---

# 70. Information Asymmetry

operator比 insurer更知道 internal system。

MII降低：

$$
InformationAsymmetry.
$$

---

# 71. Insurability Infrastructure as Market Standard

如果 carriers普遍要求：

- robot IDs；
- telemetry；
- responsibility records；
- control evidence；

企業可能為了取得 capacity而標準化。

---

# 72. Standardization Ratchet

$$
InsuranceRequirement
\rightarrow
IndustryStandard
\rightarrow
VendorSupport
\rightarrow
LowerImplementationCost.
$$

---

# 73. Institutional Ratchet Connection

當這些 controls變成 deployment prerequisite：

$$
InstitutionalEmbedding\uparrow.
$$

---

# 74. Insurance Could Institutionalize AI Identity

不是因為 insurer相信 AI是「人」。

而是因為它需要 stable risk unit。

---

# 75. Risk Identity

可定義：

$$
\boxed{
\text{Risk Identity}
}
$$

即：

> 可持續連結 exposure、telemetry、loss history與 control state 的識別單位。

---

# 76. Risk Identity 不等於 Legal Identity

$$
\boxed{
RiskIdentity
\neq
LegalPersonhood.
}
$$

---

# 77. Robot Risk Identity

最直接是：

$$
RobotID.
$$

---

# 78. AI Controller Risk Identity

如果同一 controller跨多 robots，

也可能需要：

$$
ControllerID.
$$

---

# 79. Fleet Risk Identity

某 fleet / deployment也可能是 underwriting unit。

---

# 80. Risk Identity Hierarchy

$$
Robot
\rightarrow
Fleet
\rightarrow
Facility
\rightarrow
Organization.
$$

---

# 81. AI Resident / Controller Identity 的價值

若 AI controller長期負責同一 domain，

stable identity可以聚合：

- performance；
- incident；
- near-miss；
- upgrade history；
- responsibility；
- capital。

---

# 82. 但 Insurance 不需要 AI 主體性

再次：

$$
\boxed{
Insurability
\not\Rightarrow
Subjecthood.
}
$$

---

# 83. Insurability Could Precede Legal Standing

risk identity可能先出現。

legal standing後來才討論。

---

# 84. Machine Insurability Infrastructure Layer

本文提出：

$$
\boxed{
MII
=
(
I,
E,
R,
F,
T,
C,
A
)
}
$$

其中：

- $I$：Identity；
- $E$：Execution Evidence；
- $R$：Responsibility；
- $F$：Failure Domains；
- $T$：Telemetry；
- $C$：Controls；
- $A$：Audit / Claims Reconstruction。

---

# 85. MII-I Identity

robot / controller / task / deployment。

---

# 86. MII-E Execution

Embodied Execution Graph。

---

# 87. MII-R Responsibility

Responsibility Graph。

---

# 88. MII-F Failure

Failure-Domain Graph。

---

# 89. MII-T Telemetry

event / incident evidence。

---

# 90. MII-C Controls

- local safety；
- human oversight；
- change management；
- rollback；
- maintenance；
- authorization。

---

# 91. MII-A Audit

incident-time reconstruction。

---

# 92. Claims Evidence Bundle

可包含：

```text
incident_id
robot_ref
controller_ref
task_ref
execution_snapshot
world_state_refs
policy_revision
model_revision
firmware_revision
authority_snapshot
responsibility_snapshot
maintenance_snapshot
telemetry_window
failure_domain_refs
```

---

# 93. Claims Bundle 不等於全部 Raw Data

只需適當 evidence window。

---

# 94. Privacy-Preserving Claims

可以：

- redaction；
- selective disclosure；
- cryptographic proof；
- digest verification；
- scoped access。

---

# 95. Insurer 不必讀 AI 全部 Memory

它需要 claims-relevant evidence。

---

# 96. Trade Secret

model vendor可能不願交全部 model weights。

可以提供：

- version；
- evaluation；
- attestation；
- incident evidence。

---

# 97. Verifiability without Full Disclosure

因此 MII可以與：

$$
\boxed{
\text{Selective Verifiability}
}
$$

結合。

---

# 98. Reinsurance

大規模 AI / robot risk可能需要：

$$
Insurer
\rightarrow
Reinsurer.
$$

reinsurer更關心 aggregate / systemic risk。

---

# 99. Reinsurance Aggregation

reinsurer要知道：

> 不同 insured 是否共用同一 model / cloud / vendor？

---

# 100. Hidden Correlation

若每家保險人只看到自己的 client，

可能低估 global concentration。

---

# 101. Systemic AI Risk

foundation model或 shared infrastructure可能造成：

$$
\boxed{
\text{Systemic Accumulation}.
}
$$

---

# 102. Portfolio-Level Stress Test

可模擬：

```text
model failure
cloud outage
firmware bug
cyber compromise
map corruption
coordinator failure
```

---

# 103. Stress Loss

$$
L_{\mathrm{stress}}(x)
=
\sum_{d\in F(x)}
Exposure(d).
$$

---

# 104. Accumulation Limit

insurer / reinsurer可能限制：

$$
Exposure(F(x))
\le
Limit_x.
$$

---

# 105. Diversification Incentive

企業可能因 insurance price而：

- diversify model vendors；
- isolate firmware；
- segment fleet；
- add fallback。

---

# 106. Insurance Can Shape Architecture

這是重要 institutional feedback：

$$
\boxed{
\text{Insurance Price}
\rightarrow
\text{System Architecture}.
}
$$

---

# 107. Example：Single Fleet Coordinator

如果所有 robots依賴：

$$
F_1,
$$

insurer看到：

$$
SinglePointFailure.
$$

---

# 108. Example：Segmented Coordinators

若 fleet分：

$$
F_1,F_2,F_3,
$$

且故障隔離，

aggregate loss可能下降。

---

# 109. Premium Signal as Architecture Signal

因此 risk price會把工程架構差異 monetized。

---

# 110. Responsibility Concentration 也可被 Monetized

如果一人負責全部，

insurance model可能看到 key-person / governance concentration。

---

# 111. 人類責任天價不是好風控

名義上把責任全部放一個 human，

不等於 insurer認為：

$$
Risk=Low.
$$

---

# 112. 公司級賠償能力

enterprise operation的 loss absorbing structure應包含：

- company capital；
- insurance；
- deductible；
- retention；
- vendor indemnity；
- reinsurance。

---

# 113. 這為 Paper 05 鋪路

責任 actor：

$$
\neq
$$

賠償 actor。

---

# 114. Insurance and Compensation Separation

policy response需要看：

- insured；
- claimant；
- coverage；
- retention；
- limit。

---

# 115. Subrogation

insurer支付後可能向：

- vendor；
- manufacturer；
- operator；

追償。

所以 Responsibility Graph有 financial value。

---

# 116. Vendor Contract

責任分配也會被 indemnity clause影響。

但本文不處理具體契約法。

---

# 117. Silent AI Exposure

傳統 policy可能在 wording中沒有明確 AI定位。

因此有：

$$
\boxed{
\text{Silent AI Exposure}.
}
$$

---

# 118. Affirmative Coverage

未來可能更多：

$$
\text{Affirmative AI Coverage}.
$$

即明確說哪些 AI risks被 cover。

---

# 119. Exclusions

高 systemic / unknown risk可能被 exclusion。

---

# 120. Insurance Frontier

可把 peril分：

```text
affirmatively insured
silently exposed
explicitly excluded
uninsurable/private-market difficult
```

---

# 121. Dynamic Frontier

新 loss data會改變 category。

---

# 122. Physical AI vs Agentic Digital AI

具身 risk有 physical loss。

software agent有：

- financial；
- cyber；
- professional；
- operational；

風險。

MII概念可泛化。

---

# 123. Agentic AI Insurability

software agent同樣需要：

- task identity；
- authority；
- tool trace；
- execution log；
- dependency mapping。

---

# 124. MII 不限 Robot

名稱中的 Machine泛指 autonomous machine intelligence deployments。

---

# 125. Underwriting Could Precede Regulation

如果 regulator尚未要求 telemetry，

carrier仍可把它列為 coverage condition。

---

# 126. Market Discipline

這形成：

$$
\boxed{
\text{Market-Based Governance}.
}
$$

---

# 127. Market Discipline 不是民主正當性替代

insurance standard不能替代公共 law。

---

# 128. 兩者可能互相影響

insurer practices可能變 industry standard。

後來 regulator參考。

---

# 129. Law Could Also Force Insurance

反過來政府可能要求：

- compulsory insurance；
- minimum limits；
- financial responsibility。

這會再強化MII。

---

# 130. Institutional Feedback Loop

$$
\boxed{
\text{Autonomy}
\rightarrow
\text{Risk}
\rightarrow
\text{Insurance}
\rightarrow
\text{Controls}
\rightarrow
\text{Deployability}
\rightarrow
\text{More Autonomy}.
}
$$

---

# 131. 但 Loop 可被 Claims 打斷

$$
Claims\uparrow
\rightarrow
Premium\uparrow
\rightarrow
Deployment\downarrow.
$$

---

# 132. Insurance Ratchet 的弱形式

本文不說 insurance一定推動 autonomy。

而是：

> 一旦 insurance infrastructure形成，AI / robot identity、telemetry、responsibility、control architecture就可能成為持久制度資產。

---

# 133. MII Exit Cost

若 enterprise後來不用 AI，

這些 infrastructure仍可能保留或轉作普通 automation governance。

因此：

$$
C_{\mathrm{exit}}
$$

不一定全部消失。

---

# 134. Insurability Infrastructure as Institutional Capital

MII本身具有：

- data；
- tooling；
- standards；
- workflows；
- contracts。

所以是一種 institutional capital。

---

# 135. 可證偽命題一：Telemetry Demand

autonomy提高時，carrier是否要求更多 telemetry？

---

# 136. 可證偽命題二：Governance Pricing

control quality是否影響 premium / limit / deductible？

---

# 137. 可證偽命題三：Responsibility Graph Value

責任圖完整度是否降低 claims ambiguity / resolution time？

---

# 138. 可證偽命題四：RCD Signal

高 Responsibility-Control Divergence是否與較差 underwriting terms相關？

---

# 139. 可證偽命題五：Failure-Domain Mapping

有 dependency graph的fleet是否更容易獲得capacity？

---

# 140. 可證偽命題六：Correlation Pricing

shared model / cloud concentration是否反映在 portfolio limits / reinsurance？

---

# 141. 可證偽命題七：Safety Feedback

clean incident record是否降低 premiums？

---

# 142. 可證偽命題八：Institutional Standardization

insurance requirements是否促成 industry-wide robot identity / recorder standards？

---

# 143. 反例條件

若：

- insurer只看粗略 robot count；
- telemetry不影響 pricing；
- responsibility trace不影響 claims；
- correlated model risk可忽略；
- AI-specific coverage長期不發展；

則 MII 假說需弱化。

---

# 144. 第一代 MII 實驗

Paper 01 warehouse fixture：

```text
3 robots
1 fleet AI
1 human supervisor
1 maintainer
2 robot models
1 shared planner
```

---

# 145. 建立 Mock Insurer

輸入：

- execution graph；
- responsibility graph；
- failure domains；
- telemetry；
- RCD / RCR。

---

# 146. Compare Two Firms

Firm A：

```text
no recorder
single supervisor
shared model
no failure segmentation
```

Firm B：

```text
incident recorder
typed responsibility graph
segmented coordinators
maintenance trace
```

---

# 147. Mock Premium Function

$$
Premium
=
EL
+
U
+
K
+
M.
$$

比較差異。

---

# 148. Claims Experiment

模擬：

- collision；
- firmware bug；
- cyber compromise；
- maintenance failure。

---

# 149. Claims Metrics

```text
time_to_root_cause
responsibility_gap_count
coverage_ambiguity
evidence_completeness
subrogation_target_confidence
```

---

# 150. Failure-Domain Experiment

同一 planner bug擊中：

$$
1,10,100
$$

robots。

觀察 accumulation。

---

# 151. Reinsurance Stress Test

計算：

$$
L_{\mathrm{stress}}.
$$

---

# 152. Minimum MII Records

```text
robot_registry
controller_registry
deployment_record
task_record
execution_receipt
responsibility_snapshot
maintenance_record
incident_window
failure_dependency
insurance_policy_ref
```

---

# 153. Minimum MII Invariants

## MI-1

$$
\boxed{
Insurability
\neq
LegalPersonhood.
}
$$

## MI-2

$$
\boxed{
TechnicalAttribution
\neq
LegalLiability.
}
$$

## MI-3

$$
\boxed{
ResponsibilityBearer
\neq
LossAbsorbingCapital.
}
$$

## MI-4

$$
\boxed{
RobotRisk
\neq
TaskRisk.
}
$$

## MI-5

$$
\boxed{
ResponsibilityGraph
\neq
FailureDomainGraph.
}
$$

## MI-6

$$
\boxed{
ResponsibilityGraph
\neq
InsuranceGraph.
}
$$

## MI-7

$$
\boxed{
InsuranceGraph
\neq
CompensationGraph.
}
$$

## MI-8

$$
\boxed{
Telemetry
\neq
TotalSurveillance.
}
$$

## MI-9

$$
\boxed{
RiskIdentity
\neq
LegalIdentity.
}
$$

## MI-10

$$
\boxed{
InsuranceIncentive
\neq
SocialOptimality.
}
$$

---

# 154. Machine Insurability Principle

本文提出：

$$
\boxed{
\textbf{Machine Insurability Principle}
}
$$

弱形式：

> **高自主機器系統若要取得穩定、可擴展的保險 capacity，其風險必須在合理程度上變得可觀測、可歸因、可界定、可審計，且其共同依賴與 correlated-failure exposure 必須能被辨識。**

---

# 155. Evidence-Based Claims Principle

$$
\boxed{
\textbf{Evidence-Based Claims Principle}
}
$$

弱形式：

> **事故理賠應盡可能建立在 incident-time execution、responsibility、maintenance、revision 與 telemetry evidence 上，而不是僅依賴事後各方自然語言敘述。**

---

# 156. Accumulation Visibility Principle

$$
\boxed{
\textbf{Accumulation Visibility Principle}
}
$$

弱形式：

> **任何被大量 deployments 共用的 model、firmware、cloud、planner、policy 或 coordinator，都應被視為可能的 correlated-loss node，並在 underwriting / reinsurance 層具有可觀測 exposure mapping。**

---

# 157. Insurance Governance Principle

$$
\boxed{
\textbf{Insurance Governance Principle}
}
$$

弱形式：

> **當保費、limit、deductible、coverage condition 與 capacity 對 governance quality 作差異化定價時，保險可成為 AI safety / accountability 的市場型治理機制之一，但不能取代公共法律與民主治理。**

---

# 158. 與 Paper 00 的關係

Paper 00提出 Insurance Ratchet。

本文給出其工程 substrate。

---

# 159. 與 Paper 01 的關係

Execution Graph提供 claims factual chain。

---

# 160. 與 Paper 02 的關係

RCD / RCR成為 governance concentration signals。

---

# 161. 與 Paper 03 的關係

Responsibility Graph提供 responsibility evidence。

---

# 162. 與 Paper 05 的關係

下一篇將從 insurance coverage進一步區分：

$$
\boxed{
\text{誰負責}
\neq
\text{誰先賠}.
}
$$

---

# 163. 與 Paper 06 的關係

Insurance deductible / retention / reserve 會直接引出：

$$
CapitalFollowsAutonomy.
$$

---

# 164. 與 Paper 07 的關係

若 AI-specific reserve / account能改善 underwriting，企業會產生私人利益。

---

# 165. 與 Paper 08 的關係

MII一旦成為大規模 autonomous deployment prerequisite，就成為 Institutional AI Ratchet的重要制度層。

---

# 166. 2026 年現實錨點

2026 年已出現幾個值得注意、但仍屬早期市場訊號的方向：

1. autonomous vehicle ecosystem 開始出現整合 developers、fleet operators、manufacturers / owners 與 OEM 的專門 insurance facility；
2. physical-AI / robotics insurance 新創開始把 robot-specific liability、robot damage、cyber-physical loss、business interruption 與 incident recorder evidence放在同一產品架構中；
3. AI insurance研究開始把缺乏歷史 loss data、dynamic model behavior、correlated / systemic failure、governance signals、usage-based coverage與 assurance integration列為核心 underwriting 問題；
4. agentic-AI insurance研究也開始把 autonomy、delegated authority、dependency mapping、telemetry與 dedicated AI aggregates視為保險架構要素。

這些訊號不足以證明 MII 必然成為全球標準，但足以支持本文的研究方向：**保險市場已經開始把 AI / autonomous-system governance 當成可以直接影響 coverage 與 risk price 的工程問題，而不只是抽象倫理問題。**

---

# 167. 最終命題

本文提出：

$$
\boxed{
\textbf{Machine Insurability Infrastructure Thesis}
}
$$

弱形式為：

> **當 autonomous AI / robotics 進入足以造成企業級、物理級或 systemic loss 的規模後，保險市場若要提供穩定 capacity，就會增加對 identity、telemetry、responsibility、control quality、revision history、failure-domain mapping 與 incident reconstruction 的需求。這些需求可能在法律正式賦予 AI 任何新制度地位之前，就先促成 AI / robot accountability infrastructure 的標準化。**

---

# 168. 更簡潔的形式

$$
\boxed{
\text{Autonomy}
\rightarrow
\text{Risk}
\rightarrow
\text{Insurability Demand}
\rightarrow
\text{Accountability Infrastructure}.
}
$$

---

# 169. 最終結論

保險公司不需要先回答：

> AI 是不是人？

它只需要回答：

> **這個風險我到底怎麼算？**

而只要 autonomous system 的 loss path開始跨越：

- model；
- software；
- robot；
- operator；
- maintainer；
- fleet AI；
- human supervisor；
- vendor；

保險人就很難只接受：

> 「我們公司有一位總負責人。」

作為完整風控答案。

真正有價值的是：

$$
\boxed{
\text{Identity}
+
\text{Execution Evidence}
+
\text{Responsibility}
+
\text{Failure Domains}
+
\text{Telemetry}
+
\text{Controls}
+
\text{Audit}.
}
$$

當這些東西逐漸變成「沒有就拿不到合理保費／保額／capacity」的條件，AI accountability architecture就不再只是企業願不願意做的倫理附加項。

它會變成：

$$
\boxed{
\text{financial infrastructure for autonomy}.
}
$$

更重要的是，insurance pricing會把架構差異貨幣化。

同樣 500 台 robots：

一間公司若有：

- single coordinator；
- single supervisor；
- no telemetry；
- no responsibility graph；
- common model dependency；

另一間公司若有：

- segmented failure domains；
- local safety veto；
- typed responsibility；
- incident recorder；
- maintenance trace；
- independent validation；

兩者的 risk topology並不相同。

因此：

$$
\boxed{
\text{Same Robot Count}
\neq
\text{Same Insurable Risk}.
}
$$

這也使保險開始反向影響工程架構：

$$
\boxed{
\text{Insurance Price}
\rightarrow
\text{System Architecture}.
}
$$

一旦發生這種 feedback，Machine Insurability Infrastructure 就成為 Institutional AI Ratchet 的一部分。

下一篇因此要處理更尖銳的一個問題：

> **即使 Responsibility Graph 已經能告訴我們誰對事故負責，受害人真正拿錢時，究竟是誰先賠？公司、員工、保險人、vendor 與 AI responsibility domain 之間，責任與賠償為什麼必須拆開？**

這就是 Paper 05。

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

## 參考資料與現實錨點

1. Marsh Risk & Apollo ibott. **Autonomous Vehicle Insurance Program for Uber**, 2026-03-12.
2. Boop Insurance. **Robot insurance / Robot Data Recorder product materials**, accessed 2026.
3. Szpruch, L., Orfanoudaki, A., Maple, C., Wicker, M., Bengio, Y., Lam, K.-Y., & Detyniecki, M. **Insuring AI: Incentivising Safe and Secure Deployment**, Harvard Data Science Review, 2026.
4. Leung, A., Zhang, R., Ling, E., Toyoda, K., & Loh, S. **The Insurability Frontier of AI Risk: Mapping Threats to Affirmative Coverage, Silent Exposures, and Exclusions**, 2026.
5. Zhu, Q. **Insurance of Agentic AI**, 2026.

---

## 內部理論銜接

本文直接承接：

- Embodied Execution Graph；
- Responsibility–Control Divergence；
- Responsibility Graph；
- Institutional AI Ratchet；
- NACR identity / authority / receipts；
- UFI dependency / institutional path-dependence line。

本文新增核心抽象：

$$
\boxed{
MII
=
(
I,
E,
R,
F,
T,
C,
A
)
}
$$

與：

$$
\boxed{
\mathcal G^F
=
(
V_F,
E_F,
\Delta_F
)
}
$$

以及：

$$
\boxed{
\text{Autonomy}
\rightarrow
\text{Risk}
\rightarrow
\text{Insurability Demand}
\rightarrow
\text{Accountability Infrastructure}.
}
$$
