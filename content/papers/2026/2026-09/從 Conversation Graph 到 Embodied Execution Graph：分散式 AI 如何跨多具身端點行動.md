# 從 Conversation Graph 到 Embodied Execution Graph：分散式 AI 如何跨多具身端點行動

**英文暫名：** From Conversation Graphs to Embodied Execution Graphs: How Distributed AI Operates Across Multiple Physical Endpoints  
**系列：** 不可逆的制度化智能：具身責任、保險、資本與 AI 經濟主體  
**English Series:** *The Institutional Irreversibility of Intelligence: Embodiment, Liability, Insurance, Capital, and AI Economic Subjecthood*  
**論文序號：** Paper 01 / 08  
**版本：** v0.1  
**日期：** 2026-09-08  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** Paper 00；Named-AI Conversation Graphs；NACR；Residence / CSG Storage；Authorized Hyperlink Runtime；UFI  
**文件地位：** Embodied AI / Distributed Execution / Federated Cognitive Runtime Paper  
**Canonical Source：** UTF-8 Markdown  
**Canonical Math Delimiters：** inline ` $...$ `；display `$$...$$`

---

## 研究地位聲明

本文不主張具身機器人必須具有主體性、人格或法律地位，也不主張未來工廠、物流、交通或公共基礎設施必然由單一全域 AI 控制。本文提出的是一個工程一般化：

> **當一個長期 AI identity / cognitive coordinator 同時透過多個軟體、機器人、載具、終端或工作節點執行任務時，原本用來描述多 conversation continuity 的 Conversation Graph，可以被一般化為 Embodied Execution Graph。**

這個一般化不要求所有 endpoint 共享同一 working context，不要求所有 robots 共享 raw sensor data，也不要求中央 AI 直接控制馬達。相反地，本文強調：

$$
\boxed{
\text{Global Cognitive Coordination}
\neq
\text{Global Low-Level Control}.
}
$$

以及：

$$
\boxed{
\text{AI Identity}
\neq
\text{Robot Identity}
\neq
\text{Runtime Instance}
\neq
\text{Task Identity}.
}
$$

---

## 摘要

具名 AI 對話圖系列已建立：一個 resident 可以同時擁有多條 conversation lines，而不需要把 identity、memory、project 與 working context 壓縮成單一 chat thread。本文進一步指出，這個結構並不限於聊天。

當 AI 從 conversation endpoint 走向具身執行 endpoint 時，原本的：

$$
Resident
\rightarrow
\{
ConversationLine_1,\ldots,ConversationLine_n
\}
$$

可以一般化為：

$$
\boxed{
CognitiveResident
\rightarrow
\{
ExecutionEndpoint_1,\ldots,ExecutionEndpoint_n
\}.
}
$$

其中 execution endpoint 可以是：

- conversation line；
- coding task；
- browser task；
- software agent；
- robot；
- drone；
- autonomous vehicle；
- factory cell；
- warehouse unit；
- simulation episode；
- inspection device。

本文因此提出 **Embodied Execution Graph（EEG）**：

$$
\boxed{
\mathcal G_R^{E}
=
(
V_E,
E_E,
\Lambda_E,
\Omega_E
)
}
$$

其中：

- $V_E$：execution nodes；
- $E_E$：typed execution relations；
- $\Lambda_E$：lineage / delegation / assignment evidence；
- $\Omega_E$：capability、authority、lifecycle、physical-state constraints。

本文進一步把實體身份分成四層：

$$
\boxed{
R^{AI}
\neq
R^{robot}
\neq
I^{runtime}
\neq
T^{task}.
}
$$

其中：

- $R^{AI}$：長期 AI resident / cognitive identity；
- $R^{robot}$：physical robot identity；
- $I^{runtime}$：當下軟體／控制 runtime instance；
- $T^{task}$：任務／mission identity。

因此，同一個 AI resident 可以在不同時間合法控制不同 robots；同一 physical robot 也可以在不同 task boundary 下由不同 AI residents 或 human controllers 取得 bounded control。這種 handoff 不能被錯誤理解為「AI 變成機器人」或「機器人換了人格」。

本文同時建立 dual-timescale architecture：

$$
\boxed{
\tau_{\mathrm{physical}}
\ll
\tau_{\mathrm{cognitive}}.
}
$$

Fast Physical Loop 負責：

- balance；
- actuator；
- local obstacle avoidance；
- collision prevention；
- emergency stop；
- low-level navigation；
- bounded control。

Cognitive / Governance Loop 負責：

- world-state interpretation；
- task decomposition；
- planning；
- memory；
- resource allocation；
- cross-robot coordination；
- responsibility / authority；
- escalation。

因此，本文拒絕「大型 LLM 每 10 ms 決定馬達輸出」這類不必要的中央化想像。高階 cognition 可以透過 bounded command、policy envelope、task graph 與 shared semantic state 協調具身端點，而 fast local controllers 必須保留即時安全自治。

本文進一步提出 **Federated Cognitive Execution Architecture**：

$$
\boxed{
\text{Global / Federated Cognitive Layer}
\rightarrow
\text{Domain / Regional Coordinators}
\rightarrow
\text{Local Embodied Executors}.
}
$$

但這不是一棵僵硬 hierarchy。它可以是多層 federation，並允許 local fallback、peer coordination 與 task-local delegation。

本文再把 Shared Governed Memory World 推廣為 **Shared World Memory**：

$$
\mathcal W_F^{world}.
$$

各 robot 不需要上傳全部 raw sensor streams，而可以將高價值觀測轉為 semantic crystals：

$$
RawSensor_i
\rightarrow
LocalState_i
\rightarrow
Crystal_i
\rightarrow
FederatedWorldMemory.
$$

其他 endpoints 只 materialize：

$$
\Pi_i(
\mathcal W_F^{world}
)
$$

所需區域。這形成：

$$
\boxed{
\text{Federated Semantic Memory}
\neq
\text{Centralized Raw Sensor Archive}.
}
$$

本文最後指出：具身執行圖的價值不只在效率。只要 execution、identity、task、capability、authority 與 telemetry 被分離並持續記錄，後續 Responsibility Graph、Machine Insurability Infrastructure、Compensation Graph 與 Capital Allocation 才有可追蹤 substrate。

因此，本篇是整個新系列從「AI 制度不可逆」進入具身責任研究的工程橋樑。

**關鍵詞：** Embodied Execution Graph、Federated AI、Embodied AI、Robot Identity、AI Resident、Task Identity、Fast Physical Loop、Cognitive Coordination、Shared World Memory、NACR、Responsibility Substrate

---

# 1. Conversation Graph 只是 Execution Graph 的特例

原本 Named-AI Conversation Graph 定義：

$$
\mathcal G_R^{C}
=
(
V_C,
E_C,
\Lambda_C,
\Omega_C
).
$$

其節點主要是：

- conversation；
- line；
- instance；
- task；
- project interaction。

但如果把「conversation」抽象成：

> 一次受身份、任務、權限與 memory scope 約束的 execution occurrence，

那麼 conversation 只是更大集合中的一種。

因此：

$$
\boxed{
\mathcal G_R^{C}
\subset
\mathcal G_R^{E}.
}
$$

---

# 2. Embodied Execution Graph 的定義

對 cognitive resident $R$，定義：

$$
\mathcal G_R^{E}
=
(
V_E,
E_E,
\Lambda_E,
\Omega_E
).
$$

其中：

- $V_E$：execution nodes；
- $E_E$：typed execution transitions；
- $\Lambda_E$：assignment / delegation / lineage evidence；
- $\Omega_E$：capability / authority / physical constraints。

---

# 3. Execution Node

一個 execution node：

$$
v_i\in V_E
$$

可以是：

```text
conversation
software_task
robot_task
mission
inspection
warehouse_pick
vehicle_route
drone_sortie
simulation_episode
maintenance_action
```

---

# 4. Execution Node 不等於 Physical Device

一台 robot：

$$
R^{robot}_{17}
$$

可以產生很多 execution nodes：

$$
v_1,v_2,\ldots,v_n.
$$

因此：

$$
\boxed{
RobotIdentity
\neq
ExecutionNode.
}
$$

---

# 5. 四層身份分離

本文固定：

$$
\boxed{
R^{AI}
\neq
R^{robot}
\neq
I^{runtime}
\neq
T^{task}.
}
$$

## 5.1 AI Resident Identity

$$
R^{AI}
$$

表示長期 cognitive / governance identity。

## 5.2 Robot Identity

$$
R^{robot}
$$

表示具體 physical body / machine unit。

## 5.3 Runtime Instance

$$
I^{runtime}
$$

表示某次 software / controller runtime。

## 5.4 Task Identity

$$
T^{task}
$$

表示受分派的 mission / work unit。

---

# 6. 為什麼四者不能合併

如果：

$$
R^{AI}=R^{robot},
$$

則同一 AI resident 無法合法跨 body 延續。

如果：

$$
R^{robot}=T^{task},
$$

則 robot 每換任務都像換 identity。

如果：

$$
I^{runtime}=R^{AI},
$$

則 runtime restart 會被誤認為 AI resident death / recreation。

因此必須分離。

---

# 7. One AI, Many Bodies

一個 AI resident：

$$
R_A^{AI}
$$

可以同時協調：

$$
\{
R_1^{robot},
R_2^{robot},
\ldots,
R_n^{robot}
\}.
$$

這不表示 AI identity 被複製成 $n$ 個人格。

而是：

$$
\boxed{
\text{One Cognitive Identity}
+
\text{Many Bounded Execution Endpoints}.
}
$$

---

# 8. One Robot, Different Controllers

同一 robot：

$$
R_{17}^{robot}
$$

在不同時段可以由：

- human supervisor；
- AI resident A；
- AI resident B；
- emergency local controller；

取得 bounded control。

因此：

$$
Controller(R_{17},t)
$$

是 time-varying state。

---

# 9. Controller Handoff

若：

$$
R_A^{AI}
\rightarrow
R_B^{AI}
$$

接手同一 physical robot，應表示為：

$$
HANDOFF(
R^{robot}_{17},
R_A^{AI},
R_B^{AI},
T,
t
).
$$

這不是 identity merge。

---

# 10. Physical Robot 不應成為 AI Identity Container

即使某 AI 長期使用某 robot body：

$$
R_A^{AI}
\leftrightarrow
R_{17}^{robot},
$$

也不應推出：

$$
R_A^{AI}=R_{17}^{robot}.
$$

這保留：

- body replacement；
- maintenance replacement；
- migration；
- multi-body operation；
- emergency controller handoff。

---

# 11. Execution Edge Types

第一代 EEG 可定義：

```text
assign
delegate
fork
resume
handoff
merge
suspend
resume_physical
escalate
abort
terminate
override
reference
verify
```

---

# 12. Assign

$$
ASSIGN(
T,
R^{robot}
)
$$

表示 task 被分派到 physical endpoint。

---

# 13. Delegate

$$
DELEGATE(
R_A^{AI},
R_B^{AI},
T
)
$$

表示 cognitive / operational delegation。

但：

$$
\boxed{
Delegation
\neq
IdentityTransfer.
}
$$

---

# 14. Fork

一個 task 可 fork：

$$
T_0
\rightarrow
T_1,T_2.
$$

例如：

- Robot 1 探索 A；
- Robot 2 探索 B。

這是 execution branching。

---

# 15. Merge

多 endpoints 的結果可以 merge：

$$
Result_1,Result_2
\rightarrow
Result^\*.
$$

但：

$$
\boxed{
ExecutionMerge
\neq
RobotMerge
\neq
AIResidentMerge.
}
$$

---

# 16. Escalate

local robot 遇到：

- uncertainty；
- capability limit；
- hazard；
- authority conflict；

應：

$$
ESCALATE.
$$

而不是勉強執行。

---

# 17. Abort

安全系統可以：

$$
ABORT(T).
$$

即使 global planner仍希望繼續。

這是 local safety autonomy。

---

# 18. Override

human / authorized safety controller 可以：

$$
OVERRIDE.
$$

但 override 也要被記錄。

---

# 19. Execution Lineage

每個 execution node 應保存：

```text
execution_id
parent_execution_refs
task_ref
robot_ref
ai_resident_ref
runtime_ref
project_ref
authority_revision
capability_revision
started_at
ended_at
status
```

---

# 20. Execution Certificate

可建立：

$$
ExecutionLineageCertificate.
$$

但 certificate 不等於 authority credential。

它只是證明：

> 這次 execution 從哪個 task / controller / parent node 而來。

---

# 21. Federated Cognitive Architecture

本文建議抽象：

$$
\boxed{
F
\rightarrow
\{
D_1,D_2,\ldots,D_m
\}
\rightarrow
\{
R_1,\ldots,R_n
\}.
}
$$

其中：

- $F$：federated/global cognitive layer；
- $D_j$：domain/regional coordinator；
- $R_i$：local embodied executor。

---

# 22. Global 不等於 Centralized Motor Control

全球層可以管理：

- global logistics；
- inventory；
- production plan；
- fleet scheduling；
- hazard map；
- cross-site constraints。

但不直接每毫秒輸出 actuator command。

因此：

$$
\boxed{
\text{Global Cognition}
\neq
\text{Global Servo Loop}.
}
$$

---

# 23. Dual-Timescale Architecture

定義：

$$
\tau_{\mathrm{physical}}
\ll
\tau_{\mathrm{cognitive}}.
$$

例如：

$$
\tau_{\mathrm{physical}}
\sim
1\text{ms}-100\text{ms},
$$

而：

$$
\tau_{\mathrm{cognitive}}
\sim
0.1\text{s}-100\text{s}.
$$

具體數值依系統而異。

---

# 24. Fast Physical Loop

典型：

$$
Sensor_t
\rightarrow
Controller_t
\rightarrow
Actuator_t.
$$

負責：

- motor control；
- balance；
- collision avoidance；
- emergency braking；
- stabilization；
- local obstacle avoidance。

---

# 25. Cognitive / Governance Loop

典型：

$$
PerceptionSummary
\rightarrow
WorldState
\rightarrow
Memory
\rightarrow
Planning
\rightarrow
Task
\rightarrow
Capability
\rightarrow
BoundedCommand.
$$

---

# 26. Slow Loop 不應阻塞 Fast Loop

如果 cloud / LLM down：

$$
CognitiveLoop=Unavailable,
$$

local safety loop仍必須：

$$
SafeStop
\lor
SafeFallback.
$$

---

# 27. Local Safety Has Veto Power

對 physical hazard：

$$
LocalSafety
>
RemoteOptimization.
$$

即：

$$
\boxed{
\text{Safety Veto}
\text{ must not require round-trip approval}.
}
$$

---

# 28. Capability Envelope for Robots

對 robot：

$$
Cap(R_i)
$$

可以包含：

```text
move
lift
scan
open_standard_door
operate_tool_X
enter_zone_A
```

---

# 29. Physical Capability 與 Authority 分離

Robot 技術上可以開某扇門：

$$
CanPhysicallyOpen=1,
$$

不代表：

$$
AuthorizedOpen=1.
$$

因此：

$$
\boxed{
PhysicalCapability
\neq
OperationalAuthority.
}
$$

---

# 30. Safe Reachable World 的具身化

原本 ASP 中：

$$
\mathcal W_t^{safe}
$$

是 memory / semantic reachable world。

具身化後可擴展為：

$$
\boxed{
\mathcal X_t^{safe}
=
F(
RobotState,
Task,
Capability,
Authority,
Geofence,
HumanPresence,
SafetyPolicy,
WorldState
).
}
$$

---

# 31. Literal Safe Reachable World

這時 safe reachable world 不只是資訊空間。

它可以真的表示：

> 此 robot 此刻合法、物理、安全地能進入哪些狀態？

---

# 32. Physical State Constraint

robot state：

$$
x_t
$$

必須滿足：

$$
x_t\in\mathcal X_t^{safe}.
$$

若 planner path離開：

$$
\mathcal X_t^{safe},
$$

則拒絕。

---

# 33. Authorized Physical Path

可定義：

$$
\Gamma_t^\*
=
\arg\min_{
\Gamma\in
\mathcal P_{\mathrm{phys-authorized}}(t)
}
C_t(\Gamma).
$$

這是 ASP 的具身延伸。

---

# 34. 但本文不把 Action Hyperlink 完全展開

Physical action path 涉及：

- side effects；
- irreversible states；
- human safety；
- real-time control。

因此完整 action hyperlink 需另行規格。

---

# 35. Shared World Memory

對 federation：

$$
\mathcal W_F^{world}
$$

包含：

- maps；
- hazards；
- task state；
- inventory；
- maintenance；
- robot capabilities；
- learned routes；
- semantic world events。

---

# 36. Raw Sensor Data 不應全部 Globalize

每個 robot：

$$
Raw_i(t)
$$

可能非常巨大。

如果：

$$
\sum_i Raw_i
$$

全部上傳中央，頻寬與 storage 不可擴展。

---

# 37. Local Crystallization

因此：

$$
Raw_i
\rightarrow
LocalState_i
\rightarrow
C_i.
$$

例如：

$$
C_i=
\text{Corridor A blocked}.
$$

---

# 38. Federated Semantic Memory

global memory 收：

$$
C_1,C_2,\ldots,C_n.
$$

而不是全部 raw streams。

因此：

$$
\boxed{
\text{Federated Semantic Memory}
\neq
\text{Centralized Raw Sensor Archive}.
}
$$

---

# 39. Source on Demand in Robotics

若需要事故 verification：

$$
C_i
\rightarrow
RawSensorSpan_i.
$$

平時只用 crystal。

---

# 40. Crystal First, Source on Demand

具身版仍成立：

$$
\boxed{
\text{Crystal First, Source on Demand}.
}
$$

---

# 41. Multi-Robot Higher-Order Crystal

若：

$$
R_1,R_2,R_3
$$

都觀察：

> Zone A congestion。

可以形成：

$$
C_{\mathrm{zoneA\ congested}}.
$$

---

# 42. Knowledge Sharing Without Context Sharing

不同 robots：

$$
Context_i\neq Context_j.
$$

但共享：

$$
\mathcal W_F^{world}.
$$

因此：

$$
\boxed{
\text{Shared World Memory}
\neq
\text{Shared Local Context}.
}
$$

---

# 43. Robot Local Context

每台 robot 只 materialize：

$$
C_i
=
\Pi_i(
\mathcal W_F^{world},
Task_i,
Location_i,
Capability_i,
Authority_i
).
$$

---

# 44. Memory Scope

具身 world memory 可分：

```text
robot_local
task
zone
facility
fleet
organization
shared_external
public
```

---

# 45. Local Experience Can Become Fleet Knowledge

如果 Robot 51 發現：

> Joint J 在特定溫度與負載下高故障率。

形成：

$$
C_{\mathrm{joint\ risk}}.
$$

其他同型 robot 可取得。

因此：

$$
\boxed{
\text{One body's experience can become many bodies' knowledge}.
}
$$

---

# 46. 但 Raw Private Data 不必共享

例如 camera capture 含人類敏感影像。

可只分享：

$$
C_{\mathrm{hazard}},
$$

不分享：

$$
RawVideo.
$$

---

# 47. Federated Memory 與 Privacy

所以 federation 可以同時追求：

- local raw custody；
- semantic sharing；
- provenance；
- selective source expansion。

---

# 48. World-State Versioning

具身世界快速變動。

因此每個 crystal / world state 應有：

```text
observed_at
valid_from
valid_to
confidence
source_robot_refs
world_revision
```

---

# 49. Stale World State

如果：

$$
\mathrm{age}(C)>TTL,
$$

則：

$$
\mathrm{stale}.
$$

不能因 hot route 仍存在就當 current。

---

# 50. Execution Graph 與 World Graph 分離

EEG 描述：

> 誰在做什麼？

World graph 描述：

> 世界現在是什麼狀態？

因此：

$$
\boxed{
ExecutionGraph
\neq
WorldStateGraph.
}
$$

---

# 51. Execution Graph 與 Responsibility Graph 分離

EEG 描述 execution occurrence。

Responsibility Graph 描述：

> 誰應對哪一層結果負責？

因此：

$$
\boxed{
Execution
\neq
Responsibility.
}
$$

這是 Paper 02 / 03 的核心接口。

---

# 52. Execution Graph 與 Insurance Graph 分離

同一次 execution 可能涉及：

- operator insurance；
- manufacturer coverage；
- fleet policy；
- property insurance。

因此：

$$
ExecutionGraph
\neq
InsuranceGraph.
$$

---

# 53. Multi-Graph Architecture

具身自治系統可能至少有：

$$
\boxed{
G_E,
G_W,
G_R,
G_I,
G_C
}
$$

其中：

- $G_E$：Execution；
- $G_W$：World State；
- $G_R$：Responsibility；
- $G_I$：Insurance；
- $G_C$：Compensation。

---

# 54. Typed Bridges

可建立：

```text
execution_caused
execution_observed
execution_used_world_state
responsibility_attached_to
insurance_covers
compensation_triggered_by
```

---

# 55. 不要一張圖包辦一切

物理上可以存在同一 graph database。

但：

$$
\boxed{
\text{Physical Co-Storage}
\not\Rightarrow
\text{Semantic Unification}.
}
$$

---

# 56. Robot Registry

每個 physical robot 至少有：

```text
robot_id
hardware_model
serial
sensor_profile
actuator_profile
firmware_revision
safety_controller_revision
maintenance_state
ownership
operational_status
```

---

# 57. Robot Identity 不是 AI Resident Identity

Robot Registry 不應 mint AI identity。

反之，AI resident registry 也不能假裝知道 physical hardware state。

---

# 58. Runtime Binding

需要：

$$
Binding(
R^{AI},
R^{robot},
I^{runtime},
T^{task},
t
).
$$

這個 binding 是 execution 的關鍵。

---

# 59. Binding Receipt

可保存：

```text
binding_id
ai_resident_ref
robot_ref
runtime_ref
task_ref
authority_ref
capability_ref
valid_from
valid_to
status
```

---

# 60. Binding 不等於 Ownership

AI resident 被綁到 robot execution，不代表：

$$
Owns(Robot)=AI.
$$

ownership 是另一個 legal/economic relation。

---

# 61. Task Assignment

Task record：

```text
task_id
goal
constraints
assigned_robot_refs
assigned_ai_resident_refs
deadline
risk_class
authority
stop_condition
```

---

# 62. Task Risk Class

可以：

```text
low
medium
high
critical
```

高風險 task 需要更多：

- validation；
- human approval；
- redundancy；
- telemetry。

---

# 63. Task Authority

task assignment 不得自動擴 robot capability。

$$
Authority(T)
\subseteq
Capability(Robot).
$$

---

# 64. Capability Attenuation

如果 parent coordinator 有：

$$
Cap_A,
$$

delegate 給 child：

$$
Cap_B^{delegated}
\subseteq
Cap_A^{delegable}.
$$

---

# 65. Domain Coordinator

中層 coordinator 可負責：

- warehouse zone；
- factory line；
- region；
- robot class；
- maintenance domain。

---

# 66. Local Coordinator

甚至一群 robots 可以有 local coordinator。

這降低 global bottleneck。

---

# 67. Peer Coordination

不是所有 communication 都要上 global layer。

robots 可在 bounded local policy 下 peer-to-peer。

---

# 68. Federation 而非單點總控

本文更偏好：

$$
\boxed{
\text{Federated Coordination}
}
$$

而不是：

$$
\text{One Central Brain Controls Everything}.
$$

---

# 69. Federation 的原因

- latency；
- resilience；
- privacy；
- bandwidth；
- local expertise；
- failure containment；
- autonomy boundaries。

---

# 70. Global Coordinator Failure

若 global AI down：

local systems 應：

$$
SafeDegrade
$$

而不是全部失控。

---

# 71. Domain Coordinator Failure

其 domain 應進：

- bounded local operation；
- failover；
- human escalation；
- safe stop。

---

# 72. Robot Failure

單 robot failure 不應自動拖垮 fleet。

這要求 failure-domain isolation。

---

# 73. Common-Mode Failure

但 shared model / firmware / coordinator 可能造成：

$$
CommonModeFailure.
$$

這是後續 Insurance Paper 的重要入口。

---

# 74. Failure Domain

可定義：

$$
F_d
=
\{
R_i
\mid
DependOn(R_i,x)
\}.
$$

如果 $x$ 失效，整個 $F_d$ 暴露。

---

# 75. Dependency Graph

robot execution 依賴：

- model；
- planner；
- firmware；
- network；
- battery；
- sensor；
- coordinator；
- map；
- policy。

這些 dependency 要可追蹤。

---

# 76. Dependency 不等於 Responsibility

依賴某 model 不代表 model vendor 自動負全部責任。

但它提供 causality evidence。

---

# 77. Execution Trace

每次高價值／高風險 execution 應記：

```text
task
robot
controller
ai_resident
runtime
policy_revision
world_state_refs
capability
authority
local_safety_state
result
```

---

# 78. Telemetry 層

raw telemetry 與 semantic execution trace 可分離。

Insurance / audit 不一定需要持續拿 raw sensor。

---

# 79. Claims Reconstruction Interface

後續保險可以：

$$
Incident
\rightarrow
ExecutionTrace
\rightarrow
WorldState
\rightarrow
Authority
\rightarrow
Maintenance.
$$

這就是 insurability substrate。

---

# 80. Physical Accountability Chain

因此：

$$
\boxed{
Policy
\rightarrow
Task
\rightarrow
Assignment
\rightarrow
Execution
\rightarrow
LocalSafety
\rightarrow
PhysicalOutcome
}
$$

可以被重建。

---

# 81. 這不等於法律責任已決定

trace 只提供：

$$
Evidence.
$$

法律責任仍需外部制度判定。

---

# 82. Operational Responsibility

Robot 可以承擔：

$$
\boxed{
OperationalResponsibility
}
$$

例如：

- 不越 capability；
- 不越 geofence；
- 遇 hazard safe stop；
- capability不足 escalate；
- telemetry完整。

---

# 83. Operational Responsibility 不等於 Legal Personhood

$$
\boxed{
OperationalResponsibility
\not\Rightarrow
LegalPersonhood.
}
$$

這是後續系列重要底線。

---

# 84. Federated AI Responsibility

global coordinator 可以承擔：

- scheduling correctness；
- resource assignment；
- conflict resolution；
- policy application。

local robot則承擔 execution compliance。

---

# 85. Human Role

人類可能主要負責：

- policy；
- exceptional approval；
- safety regime；
- maintenance governance；
- emergency intervention。

---

# 86. 這開始形成 Responsibility Topology

但 Paper 01 不把 Responsibility Graph 完整形式化。

只建立它所需的 execution substrate。

---

# 87. Execution Graph 的時間語義

每個 execution node有：

$$
[t_{\mathrm{start}},t_{\mathrm{end}}].
$$

world state則有 observation validity。

兩者時間不能混。

---

# 88. Physical Event Time

事故：

$$
t_e
$$

需要對齊：

- task revision；
- controller revision；
- world state；
- authority；
- maintenance state。

---

# 89. Revision-Bound Execution

高風險 execution 應綁：

```text
model_revision
planner_revision
policy_revision
firmware_revision
map_revision
authority_revision
```

---

# 90. Hot Path 不能繞過 Physical Authority

即使 UNPNP / CHM 已編譯成功 route：

$$
\widehat{\ell},
$$

每次 physical execution仍需 current authorization。

---

# 91. Memory Hyperlink 與 Physical Action Path 分離

$$
\widehat{\ell}_{memory}
\neq
\widehat{\ell}_{action}.
$$

Paper 01 只說 action path 需要更高安全層。

---

# 92. Safe Action Primitives

高階 AI應盡量呼叫 bounded primitives：

```text
move_to_zone
pick_item
inspect_machine
return_to_base
stop
```

而不是直接輸出 raw motor voltage。

---

# 93. Primitive Contract

每個 action primitive 應有：

- preconditions；
- capability；
- safety；
- timeout；
- stop condition；
- telemetry；
- rollback / fail-safe。

---

# 94. Compiler Boundary

高階 plan 可以被編譯成 primitive sequence。

但 compiler 必須保持 safety guards。

---

# 95. Compiled Execution Path

未來可：

$$
Plan
\rightarrow
ValidatedPrimitiveGraph
\rightarrow
CompiledExecutionPath.
$$

這與 CHM 類似，但風險更高。

---

# 96. Execution Path Decompression

任何 composite execution path 仍需能：

$$
Decompress
\rightarrow
UnderlyingPrimitives.
$$

以利 audit。

---

# 97. No Hidden Action Expansion

compiled path 不得偷偷加入原 task 沒授權的 action。

---

# 98. Physical Scope

可定義：

```text
zone
facility
machine
tool
object_class
time_window
```

作為 authority scope。

---

# 99. Geofence

robot path 不得出：

$$
GeoFence(T).
$$

除非 reauthorize。

---

# 100. Human Presence

如果人類進入 hazard zone：

$$
SafeWorld
$$

必須即時縮小。

---

# 101. Dynamic Safe World

因此：

$$
\mathcal X_t^{safe}
$$

是動態的。

不是部署時一次計算。

---

# 102. Battery / Mechanical State

低電量、故障 actuator、temperature alarm 都會改變：

$$
Capability_t.
$$

因此 physical capability 是 time-varying。

---

# 103. Capability Revalidation

高階 planner不能用昨日 capability cache。

---

# 104. Maintenance State

如果 maintenance overdue：

某些 task capability應：

$$
\mathrm{suspend}.
$$

---

# 105. Runtime Capability Honesty

robot software不能因 planner認為「應該能」就宣稱 sensor存在。

runtime需讀實際 hardware registry。

---

# 106. Simulation 與 Physical Deployment 分離

一個 path 在 simulation pass：

$$
SimPass=1
$$

不代表：

$$
PhysicalAuthorized=1.
$$

---

# 107. Sim-to-Real Gate

physical deployment需要 additional validation。

---

# 108. Embodied Endpoint 不限 humanoid

本文的 robot包含：

- AGV；
- robotic arm；
- drone；
- vehicle；
- warehouse bot；
- industrial machine；
- humanoid。

---

# 109. Software Endpoint 也可進 EEG

所以 EEG 更一般。

它甚至可包括：

- browser agents；
- code agents；
- cloud workers。

---

# 110. Execution Endpoint 的抽象

定義 endpoint $e$：

$$
e
=
(
\mathrm{identity},
\mathrm{capability},
\mathrm{authority},
\mathrm{state},
\mathrm{interface}
).
$$

---

# 111. Endpoint Local State

$$
State_e(t)
$$

只在必要時上傳摘要。

---

# 112. Global State 不必知道所有細節

federated coordinator只需要：

$$
S_F(t)
=
Aggregate(
S_1,\ldots,S_n
).
$$

---

# 113. Abstraction Boundary

這降低：

- bandwidth；
- privacy；
- context；
- central complexity。

---

# 114. Emergent Coordination

大量 robots 不必由單一 model逐步規劃每個動作。

可以透過：

- local policies；
- shared constraints；
- bidding；
- task allocation；
- graph planning；
- semantic memory。

---

# 115. Global AI 角色更像 Policy / Coordination Layer

而不是 joystick。

---

# 116. 類全域 AI 的具身化

因此「類全域 AI」在具身領域可更精確表示為：

$$
\boxed{
\text{Broad Cross-Domain Cognitive Coordination}
}
$$

而不是 omnipotent centralized control。

---

# 117. Federation 與全域狀態

global system 可維護：

- supply state；
- resource state；
- hazard state；
- fleet health；
- project priorities。

---

# 118. Federation 與 Local Autonomy

local robot保留：

- immediate safety；
- physical constraints；
- bounded adaptation；
- offline fallback。

---

# 119. Offline Operation

network loss時：

$$
Mode=LocalSafe.
$$

允許有限 mission或返航／停機。

---

# 120. Reconnect

重連後：

- reconcile task state；
- upload crystals；
- upload receipts；
- resolve conflicts。

---

# 121. Conflict

global以為 task未完成，但 local已完成。

需要 event reconciliation。

---

# 122. Event-Sourced Execution

EEG適合 append-oriented event：

```text
assigned
started
paused
escalated
resumed
completed
aborted
failed
overridden
```

---

# 123. Current State 是 Projection

event ledger：

$$
\rightarrow
CurrentExecutionState.
$$

不能只看最後一個 filename。

---

# 124. Execution Snapshot

高風險 incident可 snapshot：

- graph；
- revisions；
- telemetry refs；
- policies；
- world state。

---

# 125. Snapshot 不等於 Current Truth

仍沿用 canonical source discipline。

---

# 126. Reproducibility

某些 execution可在 simulation replay。

目的：

- debugging；
- insurance；
- incident analysis；
- validation。

---

# 127. Replay 不一定完全重現

physical world存在噪音。

因此需區分：

- deterministic replay；
- semantic replay；
- approximate simulation。

---

# 128. Claims Evidence

事故後不應只依自然語言 log。

需要 typed execution evidence。

---

# 129. EEG 的制度價值

EEG提供後續制度層需要的：

$$
\boxed{
\text{Who}
+
\text{What}
+
\text{When}
+
\text{With Which Capability}
+
\text{Under Which Authority}.
}
$$

---

# 130. 這是 Responsibility Graph 的前置

如果沒有 EEG：

責任圖只能靠事後猜測。

---

# 131. 這是 Insurance Graph 的前置

如果沒有 execution trace：

insurer無法穩定歸因風險。

---

# 132. 這是 Compensation Graph 的前置

如果不知道 causal chain：

subrogation / vendor recovery更困難。

---

# 133. 這是 Capital Graph 的前置

如果不知道哪個 AI / robot domain創造價值與損失：

也很難建立 AI-specific reserve。

---

# 134. 從 Conversation Graph 到 Execution Graph 的核心一般化

原本：

$$
\boxed{
\text{One Resident}
+
\text{Many Conversation Lines}
}
$$

現在：

$$
\boxed{
\text{One Cognitive Resident}
+
\text{Many Execution Endpoints}.
}
$$

---

# 135. 但多 Resident 仍可共存

Agent federation可有：

$$
R_A^{AI},R_B^{AI},R_C^{AI}.
$$

它們可以共同操作 fleet，但 task-local identity要清楚。

---

# 136. Team 不等於 Blended Identity

$$
\boxed{
Team
\neq
Resident.
}
$$

---

# 137. Shared Robot 不等於 Shared Identity

多 AI residents可在不同 task boundary使用同 robot。

robot是 resource / executor，不是 identity merge point。

---

# 138. Shared World Memory 不等於 Shared Resident Memory

global world facts：

$$
ZoneABlocked
$$

可 shared。

resident-private memory：

$$
PrivateReasoningHistory
$$

不必 shared。

---

# 139. World Memory 與 Identity Memory 分離

具身 federation更需要：

$$
\boxed{
WorldMemory
\neq
ResidentMemory.
}
$$

---

# 140. 世界狀態可以 public within fleet

但 AI resident private context仍保持隔離。

---

# 141. Execution Graph 與 NACR

NACR原本：

$$
\mathfrak N_R.
$$

具身 extension可增加：

$$
\mathcal G_R^E,
\mathcal X^{safe},
\mathcal W^{world}.
$$

---

# 142. Embodied NACR

可寫：

$$
\boxed{
\mathfrak N_R^{emb}
=
(
\mathfrak N_R,
\mathcal G_R^E,
\mathcal W^{world},
\mathcal X^{safe}
).
}
$$

---

# 143. Paper 01 不把這當完成標準

這只是第一代抽象。

真正 physical safety仍需 control theory、robotics safety、certification。

---

# 144. 可證偽命題一

Multi-endpoint AI 是否能在不共享全部 context的情況下維持 task coherence？

---

# 145. 可證偽命題二

Federated semantic memory 是否比 raw centralized streaming降低 bandwidth / storage，而維持足夠 world-state quality？

---

# 146. 可證偽命題三

Dual-timescale architecture是否降低 cloud/LLM latency對物理安全的影響？

---

# 147. 可證偽命題四

四層 identity separation是否降低 controller/robot/task attribution confusion？

---

# 148. 可證偽命題五

Execution Graph是否提高 incident reconstruction completeness？

---

# 149. 可證偽命題六

Local safety veto是否在 global planner failure時降低事故率？

---

# 150. 可證偽命題七

Failure-domain mapping是否能預測 correlated fleet risk？

---

# 151. 可證偽命題八

Task-local capability / authority binding是否降低 robot越界行為？

---

# 152. 反例條件

如果：

- central raw-data architecture更有效；
- identity separation沒有降低錯誤；
- execution graph沒有提升重建品質；
- local safety autonomy反而增加事故；
- federation帶來更高 coordination failure；

則本文架構需修正。

---

# 153. 第一代實驗

可建立：

```text
1 AI resident
1 domain coordinator
3 robots
5 task types
1 shared world memory
1 local safety controller per robot
1 execution graph
1 failure-domain graph
```

---

# 154. 實驗 Task

例如 warehouse：

- pick；
- move；
- inspect；
- charge；
- emergency stop。

---

# 155. 實驗 World Events

- corridor blocked；
- robot battery low；
- sensor degraded；
- human enters zone；
- coordinator offline。

---

# 156. 實驗觀察

測：

- task completion；
- safe stop；
- wrong-controller attribution；
- memory bandwidth；
- incident reconstruction；
- recovery。

---

# 157. 最小不變式

## EE-1

$$
\boxed{
AIIdentity
\neq
RobotIdentity.
}
$$

## EE-2

$$
\boxed{
RobotIdentity
\neq
TaskIdentity.
}
$$

## EE-3

$$
\boxed{
RuntimeInstance
\neq
AIResident.
}
$$

## EE-4

$$
\boxed{
ConversationGraph
\subset
ExecutionGraph.
}
$$

## EE-5

$$
\boxed{
GlobalCognitiveCoordination
\neq
GlobalLowLevelControl.
}
$$

## EE-6

$$
\boxed{
SharedWorldMemory
\neq
SharedLocalContext.
}
$$

## EE-7

$$
\boxed{
FederatedSemanticMemory
\neq
CentralizedRawSensorArchive.
}
$$

## EE-8

$$
\boxed{
PhysicalCapability
\neq
OperationalAuthority.
}
$$

## EE-9

$$
\boxed{
Execution
\neq
Responsibility.
}
$$

## EE-10

$$
\boxed{
ExecutionMerge
\neq
ResidentMerge.
}
$$

## EE-11

$$
\boxed{
OperationalResponsibility
\not\Rightarrow
LegalPersonhood.
}
$$

## EE-12

$$
\boxed{
SafetyVeto
>
RemoteOptimization
}
$$

for immediate physical hazard.

---

# 158. 與 Paper 00 的關係

Paper 00提出：

$$
InstitutionalAI Ratchet.
$$

本文說明這條 ratchet進入具身世界前，首先需要一個可追蹤 execution substrate。

---

# 159. 與 Paper 02 的關係

Paper 02將使用 EEG 定義：

$$
ResponsibilityLoad
$$

與：

$$
EffectiveControlCapacity.
$$

沒有 execution topology，就無法合理定義 human span of control。

---

# 160. 與 Paper 03 的關係

Paper 03建立：

$$
ResponsibilityGraph.
$$

它會以 EEG中的：

- assignment；
- delegation；
- execution；
- override；
- maintenance；

作為 evidence。

---

# 161. 與 Paper 04 的關係

Machine Insurability Infrastructure 需要：

- robot registry；
- execution trace；
- failure domains；
- world state；
- revisions。

本文提供全部前置結構。

---

# 162. 與 Paper 05 的關係

Responsibility–Compensation separation 要知道：

> 哪個 actor 做了什麼。

EEG提供 factual execution layer。

---

# 163. 與 Paper 06 / 07 的關係

AI Economic Account / Capital Allocation 需要把：

- value creation；
- loss exposure；
- responsibility domain；

綁定到 stable AI / fleet identity。

EEG提供 operational link。

---

# 164. 與 Paper 08 的關係

最終制度棘輪會把：

$$
EmbodiedExecution
\rightarrow
Responsibility
\rightarrow
Insurance
\rightarrow
Capital
$$

重新收束。

---

# 165. Paper 01 的最終命題

本文提出：

$$
\boxed{
\textbf{Embodied Execution Generalization Thesis}
}
$$

弱形式為：

> **當 AI 從單一 conversation / software task 走向多機器、多載具、多 runtime endpoint 時，長期 cognitive identity 不需要與任何單一 physical body 綁死。只要 execution identity、robot identity、runtime identity、task identity、capability、authority與 world-state provenance 被分離管理，Conversation Graph 可以一般化為 Embodied Execution Graph，使分散式／聯邦式 AI 在多具身端點上保持可追蹤 continuity，而不要求中央 AI 直接控制所有低階物理迴路。**

---

# 166. 更簡潔的形式

$$
\boxed{
\text{Conversation Line}
\rightarrow
\text{Execution Endpoint}
}
$$

以及：

$$
\boxed{
\text{Resident-Centric Continuity}
\rightarrow
\text{Federated Cognitive Execution}.
}
$$

---

# 167. 最終結論

多具身 AI 不必被想像成：

> 一個超級 AI 同時控制一千台機器人的每一顆馬達。

更合理的架構是：

$$
\boxed{
\text{Global Cognitive Coordination}
+
\text{Domain Coordination}
+
\text{Local Physical Autonomy}.
}
$$

高階 AI 維護：

- world model；
- project priorities；
- task graph；
- semantic memory；
- cross-robot coordination；
- authority / responsibility envelopes。

local robot 維護：

- physical control；
- immediate safety；
- local sensing；
- bounded execution；
- escalation。

因此：

$$
\boxed{
\tau_{\mathrm{physical}}
\ll
\tau_{\mathrm{cognitive}}.
}
$$

同一 AI resident可以合法跨多具身 endpoints 行動，而同一 robot 也可以在不同 task boundary由不同 controllers使用。

這要求：

$$
\boxed{
AIIdentity
\neq
RobotIdentity
\neq
RuntimeInstance
\neq
TaskIdentity.
}
$$

Shared World Memory又使：

$$
\boxed{
\text{One body's experience can become many bodies' knowledge}
}
$$

而不必：

$$
\boxed{
\text{One body's raw data becomes everyone's raw data}.
}
$$

最後，Embodied Execution Graph的制度價值不只是協調效率，而是建立一條可重建的：

$$
\boxed{
\text{Policy}
\rightarrow
\text{Task}
\rightarrow
\text{Assignment}
\rightarrow
\text{Execution}
\rightarrow
\text{Safety}
\rightarrow
\text{Outcome}
}
$$

execution chain。

只有當這條鏈存在，下一篇要處理的真正問題才有可能被準確提出：

> **當幾百、幾千個 autonomous execution endpoints 由少量人類監督時，責任負荷是否會開始超過人類實際控制能力？**

這就是 Paper 02 的入口。

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

- Named-AI Resident Conversation Graph；
- Shared Governed Memory World；
- Crystallized Semantic Graph；
- NACR；
- Authorized Shortest Path；
- Paper 00 Institutional AI Ratchet；
- 分散式類全域 AI / 聯邦式 AI；
- 具身 endpoint；
- responsibility / authority / receipt / revocation。

本文新增核心抽象：

$$
\boxed{
\mathcal G_R^{E}
=
(
V_E,
E_E,
\Lambda_E,
\Omega_E
)
}
$$

以及：

$$
\boxed{
R^{AI}
\neq
R^{robot}
\neq
I^{runtime}
\neq
T^{task}
}
$$

與：

$$
\boxed{
\mathfrak N_R^{emb}
=
(
\mathfrak N_R,
\mathcal G_R^E,
\mathcal W^{world},
\mathcal X^{safe}
).
}
$$
