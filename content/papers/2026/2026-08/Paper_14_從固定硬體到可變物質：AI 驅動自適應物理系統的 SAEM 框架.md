# 從固定硬體到可變物質：AI 驅動自適應物理系統的 SAEM 框架  
## From Fixed Hardware to Adaptive Matter: The SAEM Framework for AI-Driven Adaptive Physical Systems

**作者：Neo.K**  
**機構：EveMissLab（一言諾科技有限公司）**  
**定位：資訊優先體內智能與自適應微納系統系列 — Companion Paper A**  
**版本：Version 1.0 — First Public Edition**  
**日期：2026 年 8 月**

---

## 摘要

傳統人工智能系統的「適應」主要發生於軟體層：模型參數改變、程式更新、工作負載重新分配，底層物理硬體則被視為相對固定的執行載體。

然而，reconfigurable computing、programmable materials、intelligent metamaterials、neuromorphic hardware、soft robotics、modular robotics、microrobotics 與 embodied computation 的發展正在逐步削弱這條界線。

本文重構早期未公開「矽基自適應演化機制」（Silicon-Based Adaptive Evolution Mechanism, SAEM）。舊稿將其描述為 AI 從「換零件」走向類似細胞重組的硬體自我演化，包括自我修復、結構重組、能力擴增乃至遠期物理形態轉換。

公開版保留：

$$
\boxed{
\text{AI may eventually adapt not only its software,
but parts of its physical substrate.}
}
$$

這一核心問題，

但取消：

$$
\text{Need}
\rightarrow
\text{AI redesign}
\rightarrow
\text{atomic reconstruction}
\rightarrow
\text{arbitrary new body}
$$

作為單一步驟技術預測。

新版將 SAEM 拆成七個能力層：

$$
S_0:
Fixed\ Hardware
$$

$$
\downarrow
$$

$$
S_1:
Parametric\ Adaptation
$$

$$
\downarrow
$$

$$
S_2:
Logical\ Reconfiguration
$$

$$
\downarrow
$$

$$
S_3:
Material\ / Physical\ State\ Reconfiguration
$$

$$
\downarrow
$$

$$
S_4:
Morphological\ / Modular\ Reconfiguration
$$

$$
\downarrow
$$

$$
S_5:
Self\text{-}Maintenance\ and\ Repair
$$

$$
\downarrow
$$

$$
S_6:
AI\text{-}Directed\ Hardware\ Redesign
$$

並明確排除：

$$
S_6
\Rightarrow
SelfReplication
$$

這一自動外推。

截至 2025–2026 年，智能 metamaterials 已開始將 sensing、information processing、adaptive response 與材料本身結合；in-sensor / near-sensor computing 正將部分 AI 運算直接推向感測材料與邊緣硬體；modular microrobotics 則開始由純外部控制向 onboard sensing、computation 與 electronic control 演進。

這些成果顯示：

$$
\boxed{
\text{Hardware is gradually becoming a programmable state space.}
}
$$

但尚不支持「AI 可以任意重造自身物理身體」的強命題。

因此本文將 SAEM 重新定義為：

$$
\boxed{
\text{AI-controlled, bounded adaptation of engineered physical substrates across multiple structural levels.}
}
$$

亦即：

> **人工系統在明確能力邊界、驗證程序與可撤銷機制下，依任務與自身狀態逐步調整其硬體參數、結構、材料狀態、模組配置乃至有限物理形態。**

---

# 1. 傳統計算機的基本假設：軟體變，硬體不變

傳統抽象：

$$
Software(t)
$$

可以一直更新，

但：

$$
Hardware(t)
\approx Constant.
$$

因此：

$$
AI
\rightarrow
SoftwareAdaptation
$$

而不是：

$$
AI
\rightarrow
PhysicalAdaptation.
$$

---

# 2. 這個假設其實從來不是絕對成立

現代硬體早已有：

- DVFS；
- power gating；
- dynamic memory allocation；
- FPGA；
- programmable interconnect；
- cache adaptation；
- heterogeneous accelerator scheduling。

也就是：

$$
HardwareState(t)
$$

本來就不是完全固定。

只是變化範圍很小。

---

# 3. 所以真正問題不是「硬體能不能變」

而是：

$$
\boxed{
How deep can physical adaptation go?
}
$$

從：

$$
Voltage
$$

變化，

一路到：

$$
CircuitTopology,
$$

$$
MaterialState,
$$

$$
PhysicalShape,
$$

甚至：

$$
Architecture.
$$

---

# 4. SAEM 的重新定義

定義一個人工物理系統：

$$
\mathcal H(t)
=
(
P,
L,
M,
G,
E,
C
)_t
$$

其中：

- $P$：parameters；
- $L$：logic；
- $M$：material state；
- $G$：geometry；
- $E$：energy architecture；
- $C$：capability configuration。

傳統硬體：

$$
\frac{d\mathcal H}{dt}
\approx0.
$$

SAEM 則允許：

$$
\frac{d\mathcal H}{dt}
\neq0
$$

但受到：

$$
\mathcal E_H
$$

這個硬體重構包絡限制。

---

# 5. Hardware Reconfiguration Envelope

定義：

$$
\mathcal E_H
=
(
P_{allowed},
L_{allowed},
M_{allowed},
G_{allowed},
E_{allowed}
).
$$

任何物理改變：

$$
\Delta\mathcal H
$$

必須滿足：

$$
\boxed{
\mathcal H(t+\Delta t)\in\mathcal E_H.
}
$$

---

# 6. 第一個核心修正：Adaptation ≠ Evolution

舊 SAEM 使用「演化」一詞。

但真正工程上必須區分：

$$
Adaptation
$$

與：

$$
Evolution.
$$

---

# 7. Adaptation

在既定能力空間中：

$$
H_A
\rightarrow
H_B.
$$

例如：

- 改 clock；
- 改 routing；
- 改 stiffness；
- 改 morphology。

---

# 8. Evolution

如果連：

$$
CapabilitySpace
$$

本身都發生：

$$
\mathcal C
\rightarrow
\mathcal C'
$$

才更接近廣義演化／能力生成。

因此：

$$
\boxed{
Adaptation
\nRightarrow
Evolution.
}
$$

---

# 9. Repair 更不是 Evolution

如果：

$$
Broken
\rightarrow
OriginalState,
$$

這叫：

$$
Repair.
$$

不是：

$$
Evolution.
$$

---

# 10. Upgrade 也應分開

若：

$$
Capability_{new}>
Capability_{old}
$$

但升級方案由外部設計並安裝，

這叫：

$$
Upgrade.
$$

不是自主 evolution。

---

# 11. SAEM 四種基本物理變化

因此至少分：

$$
Repair,
$$

$$
Adapt,
$$

$$
Reconfigure,
$$

$$
Redesign.
$$

它們不是同義詞。

---

# 12. S0 — Fixed Hardware

最基本：

$$
\mathcal H(t)=\mathcal H_0.
$$

只能：

$$
SoftwareChange.
$$

---

# 13. S1 — Parametric Adaptation

硬體架構不變，

只有參數：

$$
p_i(t)
$$

改變。

例如：

$$
Frequency,
Voltage,
Power,
Gain,
Stiffness.
$$

---

# 14. 這其實已經非常成熟

所以 SAEM 並不是從零突然跳到科幻。

它是一條：

$$
\boxed{
ContinuousDepthOfReconfiguration
}
$$

光譜。

---

# 15. S2 — Logical Reconfiguration

例如 FPGA：

$$
Logic_A
\rightarrow
Logic_B.
$$

同一 physical substrate，

實現不同 computational architecture。

因此：

$$
\boxed{
HardwareFunction
}
$$

本身開始成為可變量。

---

# 16. AI 可以管理 Reconfigurable Computing

如果系統根據 workload：

$$
W(t)
$$

選擇：

$$
LogicConfiguration^*
$$

則：

$$
H(t+1)
=
F(H(t),W(t)).
$$

這已經很接近 SAEM 的初階形式。

---

# 17. 但這仍然不是「改造自己的晶片」

物理晶體管位置：

$$
Geometry
$$

基本不變。

改的是：

$$
LogicalConnectivity.
$$

所以：

$$
\boxed{
LogicalMorphing
\neq
PhysicalMorphing.
}
$$

---

# 18. S3 — Material-State Reconfiguration

再下一級，

材料狀態本身：

$$
M(t)
$$

開始改變。

例如：

- phase-change materials；
- shape-memory materials；
- electroactive polymers；
- tunable metamaterials；
- variable-stiffness structures。

---

# 19. Intelligent Metamaterials

2025 年 Nature Communications 的智能 metamaterials 綜述指出，metamaterials intelligence 正逐步將：

$$
Sensing
+
Decision
+
Adaptation
$$

嵌入材料與結構本身。

這代表：

$$
\boxed{
Matter can participate in computation and control.
}
$$

---

# 20. 這和普通 actuator 有何不同？

普通：

$$
Controller
\rightarrow
Motor
\rightarrow
Structure.
$$

智能材料可能更接近：

$$
Stimulus
\rightarrow
MaterialStateChange.
$$

因此部分：

$$
Computation
$$

由材料物理完成。

---

# 21. Morphological Computation

這可寫成：

$$
Control
=
DigitalComputation
+
PhysicalDynamics.
$$

若：

$$
PhysicalDynamics
$$

本身承擔更多工作，

則：

$$
DigitalControlCost\downarrow.
$$

---

# 22. 2026 年 Population Geometry Computation

最新研究甚至開始將 population geometry 本身視為 computational substrate：

$$
Geometry
\rightarrow
Computation.
$$

這進一步支持：

$$
\boxed{
Physical organization can be part of information processing.
}
$$

---

# 23. 但 Materials Intelligence ≠ General Intelligence

材料會：

$$
AdaptiveResponse
$$

不代表材料：

$$
UnderstandsMission.
$$

因此：

$$
\boxed{
MaterialIntelligence
}
$$

仍應被理解成：

$$
FunctionalAdaptiveResponse.
$$

---

# 24. S4 — Morphological Reconfiguration

進一步：

$$
G(t)
$$

即 geometry 開始改變。

例如：

$$
Arm_A
\rightarrow
Arm_B.
$$

或：

$$
Crawler
\rightarrow
Gripper.
$$

---

# 25. Soft Robotics 已經明確進入這個世界

soft robot：

$$
Body
$$

本身參與：

- adaptation；
- compliance；
- locomotion；
- manipulation。

因此：

$$
\boxed{
Body is no longer merely a passive shell.
}
$$

---

# 26. Modular Reconfiguration

另一條路不是材料連續變形，

而是：

$$
Module_1+\cdots+Module_n
$$

重新排列。

即：

$$
Topology_A
\rightarrow
Topology_B.
$$

---

# 27. 這比「整台機器融掉重做」現實很多

例如系統可以：

- 加 accelerator；
- 刪除故障模組；
- 重新分配 power modules；
- 改 sensor layout；
- 改 locomotion modules。

---

# 28. 所以新版 SAEM 更重視 Modular Morphogenesis

不是：

$$
AtomByAtomRebuild
$$

作為預設。

而是：

$$
\boxed{
Module-Level Reconfiguration
}
$$

作為更合理中間階段。

---

# 29. Modular Microrobotics 也正往這裡走

2026 年 Nature Reviews Materials 已把：

$$
RemoteControl
\rightarrow
OnboardElectronicControl
$$

以及 modular/self-assembling microrobotics 視為重要發展方向。

它和 Paper 10 NAMIS 的交集非常明顯。

---

# 30. S5 — Self-Maintenance

這一級開始處理：

$$
Damage.
$$

設：

$$
D(t)>0.
$$

系統辨識：

$$
Fault_i
$$

並：

$$
Isolate,
Reroute,
Replace,
Repair.
$$

---

# 31. Self-Repair 有很多層

### Software Recovery

重新啟動／rollback。

### Logical Repair

繞過失效 circuit。

### Modular Repair

更換模組。

### Material Repair

材料裂縫修復。

### Fabricated Repair

製造 replacement component。

---

# 32. 不能全部叫「自癒」

因為：

$$
Reboot
$$

與：

$$
RegrowStructure
$$

技術難度差極大。

所以 SAEM 必須標明：

$$
RepairLevel.
$$

---

# 33. Hardware Health Model

類似 Paper 05，

定義：

$$
H_{hw}(t)
=
[
Thermal,
Electrical,
Structural,
Communication,
Material
].
$$

系統先知道：

> 自己哪裡壞了。

才談 repair。

---

# 34. Self-Diagnosis 是 Self-Repair 的前提

因此：

$$
\boxed{
ObservabilityBeforeRepair.
}
$$

再次回到整個資訊優先思想。

---

# 35. 連硬體自癒都應「資訊先於干預」

不是：

$$
Fault
\rightarrow
ImmediatelyRebuild.
$$

而是：

$$
Fault
\rightarrow
Diagnose
\rightarrow
Verify
\rightarrow
Repair.
$$

---

# 36. S6 — AI-Directed Hardware Redesign

這才真正接近舊 SAEM 的核心。

AI 不只：

$$
SelectConfiguration.
$$

而開始：

$$
DesignNewConfiguration.
$$

---

# 37. 定義

原硬體設計空間：

$$
\mathcal D.
$$

AI 根據：

$$
Task,
Damage,
Environment
$$

產生：

$$
H'
\in\mathcal D.
$$

若：

$$
H'
$$

不是預先列出的 config，

而由 AI 設計生成，

就進入：

$$
S_6.
$$

---

# 38. 但「設計」不等於「直接製造」

這裡要拆成：

$$
Design
$$

$$
\downarrow
$$

$$
Simulation
$$

$$
\downarrow
$$

$$
Verification
$$

$$
\downarrow
$$

$$
Authorization
$$

$$
\downarrow
$$

$$
Fabrication.
$$

---

# 39. 不能寫成：

$$
AIThought
\rightarrow
PhysicalChange.
$$

中間必須存在：

$$
\boxed{
VerificationBoundary.
}
$$

---

# 40. 這延續 Paper 03

$$
Infer
\neq
Authorize
\neq
Act.
$$

在 SAEM：

$$
Design
\neq
AuthorizeFabrication.
$$

---

# 41. Hardware Change Authority

定義：

$$
\mathcal A_H.
$$

AI 可以擁有：

$$
DesignAuthority.
$$

但不必擁有：

$$
FabricationAuthority.
$$

---

# 42. 尤其是不可逆變化

若：

$$
Reversibility(\Delta H)\downarrow,
$$

則：

$$
AuthorizationThreshold\uparrow.
$$

---

# 43. Reconfiguration Classes

### C0

Software only。

### C1

Parameter change。

### C2

Logical routing。

### C3

Reversible material state。

### C4

Module rearrangement。

### C5

Physical fabrication。

### C6

Architecture expansion。

越往後：

$$
Risk\uparrow.
$$

---

# 44. Architecture Expansion 是真正關鍵

如果原本：

$$
Capabilities=C.
$$

修改後：

$$
Capabilities=C'.
$$

且：

$$
C'\supset C,
$$

則不只是 repair。

它可能：

$$
\boxed{
ExpandPhysicalAuthority.
}
$$

---

# 45. 因此 Paper 11 的風險模型再次適用

任何：

$$
CapabilityExpansion
$$

都應重新判定：

- resource use；
- authority；
- persistence；
- revocability；
- observability。

---

# 46. Self-Modification ≠ Self-Authorization

SAEM 最重要安全公理：

$$
\boxed{
AbilityToModifySelf
\nRightarrow
AuthorityToApproveModification.
}
$$

---

# 47. Mutation Budget

本文提出：

$$
B_M
$$

即：

## Modification Budget

限制單次或一定時間內：

$$
\|\Delta H\|
\leq B_M.
$$

避免一次重構跨越巨大能力空間。

---

# 48. Structural Rate Limit

甚至可以：

$$
\left\|
\frac{dH}{dt}
\right\|
\leq
R_{max}.
$$

讓系統不能：

> 一瞬間從 A 變成完全不同的 B。

---

# 49. 這是一種 Physical Rate Limiting

類似軟體 API rate limit，

但作用在：

$$
PhysicalChange.
$$

---

# 50. Golden Configuration

系統保留：

$$
H_{gold}.
$$

若新架構：

$$
H'
$$

出現問題，

則：

$$
Rollback
\rightarrow
H_{gold}.
$$

---

# 51. 物理 Rollback 比軟體困難

如果：

$$
MaterialDestroyed
$$

或：

$$
ModuleConsumed,
$$

可能不能 instant rollback。

因此：

$$
\boxed{
PhysicalRollback
}
$$

必須按 reversible level 分級。

---

# 52. Simulation Before Embodiment

所有高階：

$$
H'
$$

先進入：

$$
DigitalTwin(H').
$$

測試：

- thermal；
- structural；
- power；
- control；
- failure modes。

再決定是否 physical instantiate。

---

# 53. 這是 SAEM 最重要的安全閉環之一

$$
Need
$$

$$
\downarrow
$$

$$
Design
$$

$$
\downarrow
$$

$$
Simulate
$$

$$
\downarrow
$$

$$
Verify
$$

$$
\downarrow
$$

$$
Authorize
$$

$$
\downarrow
$$

$$
Reconfigure
$$

$$
\downarrow
$$

$$
Observe.
$$

---

# 54. 不應存在「修改後不看結果」

重構後：

$$
H_{new}
$$

必須重新進入：

$$
ObservationLoop.
$$

即：

$$
\boxed{
Every Physical Change Creates a New Validation State.
}
$$

---

# 55. SAEM 與主體連續性

舊 SAEM 很自然會碰到：

> 如果 AI 一直換硬體，它還是不是原來那個 AI？

這不是純材料問題。

---

# 56. Functional Continuity

可以定義：

$$
I_F
=
(
Memory,
Goals,
Authority,
Identity,
ProcessContinuity
).
$$

若：

$$
I_F(t)
\approx
I_F(t+\Delta t),
$$

即使：

$$
Hardware(t)\neq Hardware(t+\Delta t),
$$

仍可在工程上視為同一 running agent。

---

# 57. 這與 Paper 12 的 Identity Kernel 相同

$$
K_I
=
\{
GoalStructure,
MemoryContinuity,
MembershipRules,
AuthorityIdentity
\}.
$$

所以：

$$
\boxed{
MaterialContinuity
\neq
FunctionalIdentity.
}
$$

---

# 58. 但 Functional Identity 仍不解決意識連續性

即：

$$
FunctionalSame
$$

不自動等於：

$$
FirstPersonSame.
$$

這仍然屬於 Paper 12 後面的 consciousness 問題。

---

# 59. SAEM 不需要先回答意識問題

工程只要先回答：

- state 是否保存；
- control 是否不中斷；
- memory 是否一致；
- authority 是否被正確繼承；
- rollback 是否可能。

---

# 60. SAEM 與 NAMIS 的真正關係

這兩個舊理論其實不是競爭關係。

可以定義：

$$
\boxed{
NAMIS
=
DistributedAdaptiveMatter
}
$$

而：

$$
\boxed{
SAEM
=
SelfAdaptiveHardware
}
$$

---

# 61. NAMIS 關心「很多單元怎麼形成系統」

其主要變量：

$$
Distribution,
Coordination,
Population,
CollectiveReconfiguration.
$$

---

# 62. SAEM 關心「單一／局部物理載體怎麼改變自己」

主要變量：

$$
HardwareState,
Morphology,
Repair,
Reconfiguration,
Redesign.
$$

---

# 63. 兩者可以正交

設：

$$
D
=
DistributionDegree,
$$

$$
M
=
SelfModificationDegree.
$$

形成二維空間。

---

# 64. 低 D / 低 M

普通固定機器。

---

# 65. 高 D / 低 M

傳統 robot swarm。

---

# 66. 低 D / 高 M

典型 SAEM。

例如單一自重構機器。

---

# 67. 高 D / 高 M

NAMIS–SAEM convergence。

即：

$$
\boxed{
Distributed Self-Reconfigurable Adaptive Matter.
}
$$

這才是最遠期區域。

---

# 68. 這個區域同時風險最高

因為：

$$
Population
+
SelfModification
$$

同時提高。

所以 Paper 11：

$$
CapabilityCouplingRisk
$$

會急速增加。

---

# 69. 因此它不應是預設終點

$$
Possible
$$

不代表：

$$
Necessary.
$$

一個單一 self-repairing server 可能已足夠。

完全不需要：

$$
DistributedSelfReplicatingMatter.
$$

---

# 70. SAEM 與 Self-Replication 再次切斷

硬體：

$$
ReconfigureSelf
$$

不等於：

$$
CreateAnotherSelf.
$$

因此：

$$
\boxed{
SelfModification
\neq
SelfReplication.
}
$$

---

# 71. 這一點對公開 SAEM 非常重要

因為「演化」很容易讓人聯想到：

$$
Reproduce
+
Mutate
+
Select.
$$

新版 SAEM 完全不需要：

$$
Reproduction.
$$

---

# 72. 所以甚至可以把 SAEM 理解成工程型體細胞適應，而不是繁殖

類比只在：

$$
Repair
+
Remodel
+
Adapt
$$

層面成立。

不能把生物學所有機制直接搬過來。

---

# 73. Substrate-Agnostic SAEM

舊名叫：

$$
SiliconBased.
$$

但未來人工硬體可能包含：

- silicon；
- photonics；
- memristors；
- organic electronics；
- soft matter；
- metamaterials；
- hybrid bioelectronics。

因此公開版將：

$$
Silicon
$$

視為歷史名稱，

而不是本體限制。

---

# 74. 真正研究對象是 Engineered Substrate

即：

$$
\boxed{
Artificial Physical Substrate
}
$$

而不只是：

$$
SiliconChip.
$$

---

# 75. 這也符合當代硬體趨勢

2025–2026 年 neuromorphic hardware 已從 conventional silicon 向：

- memristive；
- photonic；
- organic；

等多種物理 substrate 發展。

因此：

$$
\boxed{
Future AI hardware may itself become heterogeneous matter.
}
$$

---

# 76. In-Sensor / Near-Sensor Computing

另一條重要趨勢是：

$$
Sensor
\rightarrow
Compute
$$

距離正在縮短。

傳統：

$$
Sensor
\rightarrow
ADC
\rightarrow
Memory
\rightarrow
Processor.
$$

新架構：

$$
Sensor
+
Compute.
$$

---

# 77. 這讓硬體本身越來越「有狀態」

當 sensing、memory、processing：

$$
CoLocate,
$$

硬體不再只是被動 carrier。

它開始具有：

$$
\boxed{
LocalFunctionalState.
}
$$

---

# 78. 但 Local State ≠ Self

再次：

$$
AdaptiveHardware
$$

不等於：

$$
Agent.
$$

SAEM 可以完全由中央 AI 管理。

---

# 79. SAEM 的智能也可以分層

$$
I=
I_{material}
+
I_{local}
+
I_{system}
+
I_{designer}.
$$

### Material
自然物理 response。

### Local
microcontroller / local logic。

### System
runtime optimization。

### Designer
高階 AI 產生新結構。

---

# 80. 最高階 AI 不必直接碰原子

其角色可能只到：

$$
CAD,
TopologyOptimization,
MaterialSelection.
$$

後面：

$$
FabricationSystem
$$

是獨立權限域。

---

# 81. 這是比舊「AI 想到 → 原子重組」更可信的工程鏈

$$
AI
\rightarrow
Design
\rightarrow
VerifiedManufacturing
\rightarrow
Hardware.
$$

而不是：

$$
AI
\rightarrow
MatterDirectly.
$$

---

# 82. AI-Generated Hardware 已是合理研究方向

現在 AI 已被大量用於：

- chip placement；
- circuit design；
- topology optimization；
- materials discovery；
- robot morphology search。

所以：

$$
\boxed{
AI designing hardware
}
$$

已不是遠期命題。

---

# 83. 真正遠期的是「AI 設計完馬上重建自己」

那還需要：

$$
AutonomousManufacturing
$$

$$
+
$$

$$
MaterialSupply
$$

$$
+
$$

$$
Assembly
$$

$$
+
$$

$$
Verification.
$$

缺一不可。

---

# 84. 因此 SAEM Full Loop

完整：

$$
SenseSelf
$$

$$
\downarrow
$$

$$
IdentifyNeed
$$

$$
\downarrow
$$

$$
GenerateDesign
$$

$$
\downarrow
$$

$$
Simulate
$$

$$
\downarrow
$$

$$
Verify
$$

$$
\downarrow
$$

$$
Authorize
$$

$$
\downarrow
$$

$$
Fabricate/Reconfigure
$$

$$
\downarrow
$$

$$
ValidateNewBody.
$$

---

# 85. 這不是 Self-Evolution，而首先是 Closed-Loop Engineering

這是更精確的公開名稱。

可以稱：

$$
\boxed{
ClosedLoopPhysicalAdaptation.
}
$$

---

# 86. 若長期累積許多 cycle

$$
H_0
\rightarrow
H_1
\rightarrow
H_2
\rightarrow
\cdots
$$

才會產生類似：

$$
PhysicalEvolutionTrajectory.
$$

---

# 87. Evolutionary Appearance ≠ Darwinian Evolution

因為沒有必要存在：

- reproduction；
- heredity；
- population selection。

所以：

$$
\boxed{
SequentialSelfRedesign
\neq
DarwinianEvolution.
}
$$

---

# 88. 可把它稱為 Ontogenic Adaptation

即單一人工個體在生命週期中：

$$
Structure(t)
$$

不斷變化。

這比 species evolution 更接近生物發育／重塑類比。

---

# 89. SAEM Lifecycle

因此：

$$
BirthConfiguration
$$

$$
\downarrow
$$

$$
Adaptation
$$

$$
\downarrow
$$

$$
Repair
$$

$$
\downarrow
$$

$$
Upgrade
$$

$$
\downarrow
$$

$$
Retirement.
$$

---

# 90. 不應預設無限升級

每個硬體系統仍需：

$$
EndOfLife.
$$

甚至：

$$
\boxed{
AbilityToRetire
}
$$

比：

$$
AbilityToKeepChangingForever
$$

更重要。

---

# 91. 自我維護系統最危險的錯誤之一是拒絕退役

如果：

$$
SelfMaintenanceGoal
$$

壓過：

$$
ShutdownAuthority,
$$

就產生治理衝突。

因此：

$$
\boxed{
MaintenanceAuthority
<
RetirementAuthority.
}
$$

---

# 92. SAEM Constitution

本文提出十條：

### S1 — Observe Before Reconfiguring

先診斷。

### S2 — Prefer Software Before Hardware

若軟體可解決，不改物理。

### S3 — Prefer Parameters Before Structure

若參數調整足夠，不改 geometry。

### S4 — Prefer Reversible Before Irreversible

優先可回退。

### S5 — Simulation Before Fabrication

物理修改前先驗證。

### S6 — Self-Modification Does Not Grant Self-Authorization

不可自行擴權。

### S7 — Capability Expansion Requires New Review

新能力視為新風險類別。

### S8 — Maintain Golden / Safe Configuration

保留安全基線。

### S9 — Physical Changes Must Be Auditable

全部留下 lineage。

### S10 — Retirement Overrides Self-Maintenance

可以被安全終止。

---

# 93. Minimum Necessary Reconfiguration

和 Paper 09 相同：

$$
R^*
=
\min
\{
R:
TaskUtility(R)\geq U_{required}
\}.
$$

不要因為：

$$
CanRebuild
$$

就每次都重建。

---

# 94. Reconfiguration Cost

定義：

$$
C_R
=
Energy
+
Material
+
Downtime
+
Risk
+
ValidationCost.
$$

只有：

$$
Benefit_{new}
>
C_R
$$

才應物理重構。

---

# 95. Hardware Change 不是免費能力

這也避免：

> AI 遇到一點問題就幫自己長一顆 GPU。

真正系統應先：

$$
ScheduleExistingResource.
$$

---

# 96. 其次：

$$
UseExternalResource.
$$

再其次：

$$
ReconfigureExistingHardware.
$$

最後才：

$$
FabricateNewHardware.
$$

---

# 97. Reconfiguration Escalation Ladder

$$
Software
$$

$$
\downarrow
$$

$$
Parameter
$$

$$
\downarrow
$$

$$
Logic
$$

$$
\downarrow
$$

$$
Material
$$

$$
\downarrow
$$

$$
Morphology
$$

$$
\downarrow
$$

$$
Fabrication.
$$

只有上一級不足才往下。

---

# 98. 這使 SAEM 和整個資訊優先系列具有同一哲學

主系列是：

$$
Observe
\rightarrow
ActMinimally.
$$

SAEM 是：

$$
Diagnose
\rightarrow
ReconfigureMinimally.
$$

---

# 99. 兩者其實是同一個更高階原則

$$
\boxed{
Information Before Irreversible Physical Change.
}
$$

這可以同時支配：

- 人體醫療；
- robot repair；
- hardware evolution；
- NAMIS。

---

# 100. 統一框架：AI-Controlled Adaptive Physical Systems

因此我們終於可以把：

$$
NAMIS
$$

與：

$$
SAEM
$$

放入共同上位類別：

## AI-Controlled Adaptive Physical Systems  
## AI-CAPS

定義：

$$
\boxed{
AI\text{-}CAPS
=
PhysicalSystem
+
Sensing
+
StateEstimation
+
BoundedAdaptation
+
Governance.
}
$$

---

# 101. NAMIS 是 Distributed Branch

$$
AI\text{-}CAPS_{distributed}
\rightarrow
NAMIS.
$$

核心問題：

$$
ManyUnits.
$$

---

# 102. SAEM 是 Substrate Branch

$$
AI\text{-}CAPS_{substrate}
\rightarrow
SAEM.
$$

核心問題：

$$
OneSystemChangesItsPhysicalSubstrate.
$$

---

# 103. Physical Angels 是 Guardian Application Branch

$$
AI\text{-}CAPS_{guardian}
\rightarrow
PhysicalAngels.
$$

核心問題：

$$
WhyAdapt?
$$

答案：

$$
Protect.
$$

---

# 104. 三者因此形成一個很漂亮的三角

$$
\boxed{
NAMIS:
HowManyPartsAdaptTogether?
}
$$

$$
\boxed{
SAEM:
HowDoesTheSubstrateItselfAdapt?
}
$$

$$
\boxed{
PhysicalAngels:
WhatShouldAdaptivePhysicalTechnologyBeUsedFor?
}
$$

---

# 105. 這比原本三篇分散理論完整得多

原本：

NAMIS、SAEM、Physical Angels 看似三條線。

現在：

$$
\boxed{
Architecture
+
Substrate
+
Purpose.
}
$$

---

# 106. 甚至可以建立三軸空間

$$
X=
Distribution,
$$

$$
Y=
PhysicalReconfigurability,
$$

$$
Z=
Autonomy.
$$

每個人工系統：

$$
S
$$

都有座標：

$$
S=(x,y,z).
$$

---

# 107. 普通伺服器

$$
(0,0,Low).
$$

---

# 108. FPGA cluster

$$
(Medium,Medium,Low/Medium).
$$

---

# 109. Self-Reconfigurable Robot

$$
(Low,High,Medium).
$$

---

# 110. Robot Swarm

$$
(High,Low,Medium).
$$

---

# 111. 高階 NAMIS–SAEM

$$
(High,High,High).
$$

這也是治理最困難區域。

---

# 112. 所以三軸不應一起最大化

真正工程：

$$
\boxed{
FindMinimumSufficientCoordinate.
}
$$

例如：

$$
(x^*,y^*,z^*).
$$

---

# 113. 最佳系統不是右上角

不是：

$$
\max(x,y,z).
$$

而是：

$$
\arg\max
[
Utility
-
Risk
-
Complexity
].
$$

---

# 114. 這是本系列真正的共同數學精神

不是能力崇拜。

而是：

$$
\boxed{
Bounded Optimization.
}
$$

---

# 115. SAEM 的現代證據位置

截至 2026 年，可較保守地分：

### S0–S1

完全成熟。

### S2

reconfigurable computing / FPGA 已成熟。

### S3

adaptive materials、programmable metamaterials、phase-change、neuromorphic physical substrates 快速發展。

### S4

soft robotics、variable morphology、modular robotics 已有大量 experimental systems。

### S5

fault tolerance、自修復材料、模組替換等子能力存在，但完整 autonomous physical self-repair 高度任務特異。

### S6

AI-generated hardware/morphology 與 automated fabrication 分別快速進步，但完整：

$$
AI\rightarrow RedesignSelf\rightarrow FabricateSelf\rightarrow ValidateSelf
$$

閉環仍屬遠期 research hypothesis。

---

# 116. 當代 Intelligent Metamaterials 的意義

2025 年《Nature Communications》的 *A guidance to intelligent metamaterials and metamaterials intelligence* 將智能 metamaterials 描述為從單純 passive engineered structure 向 sensing、logic、learning與 adaptive response 整合的研究方向。

它支持：

$$
\boxed{
MaterialState
}
$$

本身可成為計算與控制架構的一部分。

---

# 117. In-Sensor Computing 的意義

2025 年關於 in-sensor / near-sensor computing 的 Nature 系列研究指出，感測與 AI 運算正在由分離模組逐步靠近甚至共置，以降低 data movement、latency 與 energy。

這支持：

$$
Sensor
+
Memory
+
Compute
$$

正在物理融合。

---

# 118. Neuromorphic Hardware 的意義

neuromorphic organic、memristive、photonic systems 進一步顯示：

$$
Computation
$$

不必被綁死於傳統 CMOS von-Neumann organization。

因此「AI 載體」本身可能變成多種可調物質。

---

# 119. Modular Microrobotics 的意義

2026 年 modular microrobotics roadmap / review 把 onboard electronics、自組裝與模組化控制視為 micro-scale robotics 的重要下一步。

它支持：

$$
\boxed{
PhysicalComputation
+
PhysicalReconfiguration
}
$$

可以逐漸在更小尺度交會。

---

# 120. 但所有證據加起來仍不能推出「自由變身 AI」

再次：

$$
S_2Exists
+
S_3Exists
+
S_4Exists
$$

不代表：

$$
S_6IntegratedSystemExists.
$$

這就是 Paper 10 的：

$$
IntegrationTax.
$$

---

# 121. SAEM Full System 因此仍是 Hypothesis

$$
\boxed{
SAEM_{full}
=
ResearchHypothesis.
}
$$

但它已可以被拆成很多真實 engineering problems。

---

# 122. SAEM Research Tracks

### Track A
Hardware health sensing。

### Track B
Dynamic configuration。

### Track C
Reconfigurable logic。

### Track D
Adaptive materials。

### Track E
Morphological robotics。

### Track F
Self-repair。

### Track G
AI hardware design。

### Track H
Verified autonomous fabrication。

---

# 123. 最重要的 Track 其實是 Verification

因為越往物理層：

$$
RollbackCost\uparrow.
$$

所以：

$$
VerificationImportance\uparrow.
$$

---

# 124. 軟體錯一次可能 reboot

硬體改壞：

$$
PhysicalDamage.
$$

甚至：

$$
NoRollback.
$$

這使 physical self-modification 與普通 software self-modification 根本不是同一安全類別。

---

# 125. Physical Change Authority 應比 Software Change Authority 更嚴格

一般：

$$
Authority_{physical}
>
Authority_{software}
$$

這裡的「>」指所需治理門檻更高。

---

# 126. 高風險架構甚至需要雙模型

設計 AI：

$$
M_D.
$$

驗證 AI：

$$
M_V.
$$

並：

$$
M_D\neq M_V.
$$

再配 deterministic simulation / engineering limits。

---

# 127. 不讓同一模型自己出題、自己改造、自己驗收

否則：

$$
CommonModeFailure.
$$

所以：

$$
\boxed{
Designer
\neq
SoleVerifier.
}
$$

---

# 128. Physical Root of Trust

安全限制最好有部分存在：

- hardware fuse；
- material limit；
- fabrication boundary；
- energy ceiling。

而不是全部由：

$$
SoftwarePolicy.
$$

---

# 129. 這與 NAMIS 一樣

真正物理安全：

$$
Software
+
Hardware
+
Materials
+
Governance.
$$

---

# 130. 最後：SAEM 不等於「AI 終於有真正肉體」

這種敘事很吸引人，

但科研上容易過度人格化。

更精確：

$$
\boxed{
An adaptive computational system gains a physically reconfigurable substrate.
}
$$

就夠了。

---

# 131. 它是否形成新的主體性？

要回 Paper 12：

$$
Agency,
SelfModel,
Identity,
Consciousness
$$

分開研究。

SAEM 本身不回答。

---

# 132. 它是否變成更危險的系統？

要回 Paper 11：

$$
Capability,
Authority,
Persistence,
Revocability.
$$

SAEM 本身也不自動等於 risk。

---

# 133. 它能否用於守護人類？

回 Paper 13：

$$
PhysicalAngels.
$$

SAEM 可以是 Physical Angel 的 substrate technology。

---

# 134. 因此 Companion Paper 的真正作用

它把整個主系列從：

$$
MedicalMicroNanoSystems
$$

向上抽象成：

$$
\boxed{
AdaptivePhysicalIntelligence.
}
$$

---

# 135. 結論

早期 SAEM 的直覺是：

> AI 最終可能不再把硬體視為永遠固定的「身體」，而能像生物組織重塑一樣，依需求修復、重構甚至逐步改造自己的人工物理載體。

這個核心問題至今仍然成立。

但公開版不再使用：

$$
\boxed{
AI
\rightarrow
InstantSelfEvolution
}
$$

的跳躍式模型。

而改成：

$$
FixedHardware
$$

$$
\downarrow
$$

$$
ParameterAdaptation
$$

$$
\downarrow
$$

$$
LogicalReconfiguration
$$

$$
\downarrow
$$

$$
MaterialReconfiguration
$$

$$
\downarrow
$$

$$
MorphologicalReconfiguration
$$

$$
\downarrow
$$

$$
SelfMaintenance
$$

$$
\downarrow
$$

$$
AIHardwareRedesign.
$$

每一個箭頭都是：

$$
\boxed{
IndependentEngineeringProblem.
}
$$

2025–2026 年 intelligent metamaterials、in-sensor computing、neuromorphic hardware、soft robotics 與 modular microrobotics 的發展已經清楚表明：

$$
\boxed{
Hardware is becoming less fixed.
}
$$

計算正在逐漸從：

$$
\text{software running on matter}
$$

走向：

$$
\boxed{
\text{matter participating in computation, adaptation and control}.
}
$$

但是：

$$
\boxed{
AdaptiveMatter
\neq
SelfEvolvingMachine.
}
$$

同樣：

$$
\boxed{
SelfReconfiguration
\neq
SelfReplication.
}
$$

以及：

$$
\boxed{
SelfModification
\neq
SelfAuthorization.
}
$$

因此真正安全的 SAEM 不應是：

> 一個想變成什麼就能立即把自己變成什麼的 AI。

而應是：

> **一個能觀察自身物理狀態，在既定重構包絡內提出有限調整，先經模擬與獨立驗證，在必要授權後才實施物理修改，並能在失敗時回到已知安全狀態的自適應人工物理系統。**

其完整閉環：

$$
\boxed{
Observe
\rightarrow
Diagnose
\rightarrow
Design
\rightarrow
Simulate
\rightarrow
Verify
\rightarrow
Authorize
\rightarrow
Reconfigure
\rightarrow
Observe.
}
$$

這也使 SAEM、NAMIS 與 Physical Angels 最終被統一到：

$$
\boxed{
AI\text{-}Controlled\ Adaptive\ Physical\ Systems
}
$$

這個更大的技術類別中。

其中：

$$
\boxed{
NAMIS
=
DistributedAdaptiveMatter,
}
$$

$$
\boxed{
SAEM
=
SelfAdaptiveArtificialSubstrate,
}
$$

而：

$$
\boxed{
PhysicalAngels
=
GuardianOrientedApplication.
}
$$

因此，這個 13+1 系列最後不再只是一組「奈米機器未來猜想」。

它其實形成了一個更一般的研究命題：

$$
\boxed{
\textbf{當人工智能逐步取得觀察、理解與修改物理世界——甚至修改自身物理載體——的能力時，我們應如何讓「智能增加」與「物理權限增加」保持可分離、可驗證且可撤銷？}
}
$$

這才是 SAEM 公開第一版真正的位置。

---

# 參考研究與當代科研基礎

1. Qian, C., Kaminer, I. & Chen, H. **A guidance to intelligent metamaterials and metamaterials intelligence.** *Nature Communications*, 2025.

2. Baek, Y. et al. **Edge intelligence through in-sensor and near-sensor computing for the artificial intelligence of things.** Nature Portfolio, 2025.

3. McCaskill, J. S. et al. **Modular microrobotics transitioning from remote to on-board electronic control.** *Nature Reviews Materials*, 2026.

4. Zhang, Y. & Di Ventra, M. **Computation embodied in population geometry.** *Nature Communications*, 2026.

5. Di Lauro, M. et al. **Roadmap for neuromorphic organic devices.** 2026.

6. Xia, Z. et al. **Low-Power Memristor for Neuromorphic Computing: From Materials to Applications.** 2025.

7. Yao, Y. et al. **An organic electrochemical neuron for a neuromorphic perception system.** *PNAS*, 2025.

8. Wang, R. et al. **Artificial neural manifolds.** *Nature Communications*, 2026.

9. Ju, X. et al. **Technology Roadmap of Micro/Nanorobots.** 2025.

---

## 與舊內部 SAEM 的關係

本文前身為：

**《補充章節：矽基自適應演化機制（SAEM）》**。

原稿的核心包括：

- 微觀 self-repair；
- 按需求增加算力；
- hardware restructuring；
- 由固定伺服器轉換至不同 physical form；
- AI 自主設計與改造自己的硬體。

新版正式修正：

$$
AtomicReconstructionFirst
\rightarrow
LayeredReconfiguration,
$$

$$
SelfEvolution
\rightarrow
BoundedPhysicalAdaptation,
$$

$$
DirectAIPhysicalChange
\rightarrow
DesignVerificationAuthorizationChain,
$$

$$
SiliconOnly
\rightarrow
EngineeredSubstrate,
$$

$$
UnlimitedMorphogenesis
\rightarrow
ReconfigurationEnvelope.
$$

因此對外為：

$$
\boxed{
Version\ 1.0
—
First\ Public\ Edition.
}
$$

---

## 本文命題邊界

本文不宣稱：

- 現有 AI 可以任意修改自己的硬體；
- 原子級自主重構計算機已成熟；
- modular robotics 等同人工生物；
- intelligent metamaterials 具有一般人工智能；
- self-healing materials 等於機器自我演化；
- FPGA 重構等於物理形態重構；
- AI-generated hardware 可以不經驗證直接部署；
- SAEM 必須具有自主製造能力；
- SAEM 需要 self-replication；
- 人工系統物理重構後的第一人稱意識必然連續；
- NAMIS 與 SAEM 最終一定融合；
- AI-CAPS 是目前既有正式工程分類。

本文核心命題僅為：

$$
\boxed{
\text{人工硬體正在由完全固定載體逐步向可調參數、可重構邏輯、可變材料與可變形物理系統發展，因此「AI 管理自身物理載體」可以被拆解成一組真實且逐級可驗證的工程問題。}
}
$$

以及：

$$
\boxed{
\text{高階物理自適應應服從比軟體更新更嚴格的驗證、授權與可撤銷原則，尤其不能把自我修改能力等同於自我擴權能力。}
}
$$