# 從專用計算器到自治計算平台：Benchmark、路由與 AI Orchestration

**系列：外掛式物理計算機與現場計算設備研究，第 7 篇**  
**英文系列名：External Physical Compute Appliances and Field Computing Systems**  
**英文篇名：From Dedicated Calculators to Autonomous Compute Platforms: Benchmarking, Routing, and AI Orchestration**  
**版本：v0.1**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：2026-08-29**  
**狀態：公開草稿／EPCA 系列收斂篇；Benchmark、Requirement Manifest、Execution Planning、Deterministic Orchestration 與 Optional AI Orchestration 架構**

## 摘要

Paper 00 至 Paper 06 已依序建立 External Physical Compute Appliance（EPCA）的設備總綱、Carrier-Generalized Abacus、Observable Physical Computation、Supervisor–Physical-Core Separation、Offline-First Field Autonomy、Multi-Substrate Compute Backplane，以及 Mixed-Precision Evidence-Bearing Computation。到此為止，一台 EPCA 已可以具有 optical、RF、acoustic、analog、FPGA、compute-in-memory（CIM）或其他 physical compute module；它能在本地啟動、失聯運作、更新恢復、校正模組、保存 raw evidence，並把最終輸出交付為帶有 provenance 的 computation object。

然而，當同一設備同時存在多條可執行路徑時，新的問題立即出現：

> 同一個任務到底應該送到哪一個 compute substrate？

這個問題不能只用「誰的 FLOPS 高」回答。某個 optical path 可能具有極低 latency，卻需要 warm-up 與 calibration；某個 analog/CIM path 可能很省能，卻只能在特定 error envelope 內工作；FPGA 可能具有可預測 real-time latency，但 configuration cost 不低；CPU 可能最慢，卻具有最高 deterministic exactness 與最完整 software support。更重要的是，EPCA 的選擇還必須同時遵守 Paper 02 至 Paper 06 已建立的 evidence、authority、offline、module 與 result assurance 約束。

本文提出 **EPCA Benchmark and Orchestration Framework（EBOF）**。其核心不是建立一個新的單一 benchmark 排名，而是建立：

$$
\boxed{
\text{Task Requirement Manifest}
+
\text{Capability/Benchmark Snapshot}
+
\text{Hard Constraint Gate}
+
\text{Candidate Route Set}
+
\text{Cost/Assurance Model}
+
\text{Deterministic Execution Plan}
}
$$

本文將任務需求寫成：

$$
R_\tau
=
(
F,
D,
Q,
L,
E,
A,
O,
C,
S,
P
),
$$

其中包含 functional requirement、data/shape domain、quality/precision、latency、energy、assurance minima、offline requirement、physical contribution constraint、safety/security constraint 與 provenance/evidence policy。每個 module 或 execution path 則以 versioned capability descriptor：

$$
K_i(t)
=
(
\Phi_i,
\Omega_i,
\Lambda_i,
\mathcal E_i,
\mathcal Q_i,
\mathcal A_i,
\mathcal K_i,
\mathcal H_i,
\mathcal W_i
)
$$

描述其 operator set、valid operating domain、latency、energy、quality/error envelope、assurance ceiling、calibration state、health 與 wear/configuration state。

本文主張，EPCA routing 的第一步不是 optimization，而是 eligibility：

$$
\boxed{
\mathcal C_\tau(t)
=
\{p\mid p\models H_\tau(t)\}.
}
$$

只有通過所有 hard constraints 的 route 才能進入後續成本比較。其後才使用 Pareto frontier、lexicographic policy 或明確 versioned objective policy 進行 deterministic selection。這避免「低 assurance 但很快」的路徑用一個漂亮的加權總分蓋過真正不可違反的科研或工程要求。

本文同時提出五層 benchmark family：primitive benchmark、module benchmark、pipeline benchmark、field-state benchmark 與 assurance/evidence benchmark。Benchmark result 必須綁定 module identity、firmware/runtime、algorithm mapping、calibration version、environment envelope、sample size 與 uncertainty，而不是把歷史上某次最佳數字永久當成設備能力。

在 orchestration 上，本文首先定義完全不需要 AI 的 deterministic planner：

$$
\boxed{
\Pi_D:
(R_\tau,S_t,B_v,P_v)
\mapsto
\mathcal X
}
$$

其中 $S_t$ 是 system state， $B_v$ 是 benchmark/capability database version， $P_v$ 是 planner policy version， $\mathcal X$ 是完整 execution plan。對相同輸入快照與相同版本，planner 應具有 reproducibility：

$$
\Pi_D(R,S,B_v,P_v)
=
\Pi_D(R,S,B_v,P_v).
$$

未來 AI 可以加入，但 AI 的位置被限定為 proposal/search/explanation layer，而不是最終 authority：

$$
\text{AI Proposal}
\rightarrow
\text{Deterministic Validation}
\rightarrow
\text{Plan Commit}
\rightarrow
\text{Execution}.
$$

AI 不得自行降低 assurance、偽造 benchmark、跳過 calibration、把 digital fallback 偽裝成 physical-primary，或繞過 Paper 02 至 Paper 06 的任何 evidence gate。

本文新增 **Orchestration Assurance（ORA-O0 至 ORA-O5）**，並將 EPCA 最終 assurance 座標收斂為：

$$
\boxed{
Q_{\mathrm{EPCA}}
=
(
\mathrm{OPC\mbox{-}V},
\mathrm{ESA\mbox{-}S},
\mathrm{LFA\mbox{-}F},
\mathrm{MSA\mbox{-}M},
\mathrm{CRA\mbox{-}R},
\mathrm{ORA\mbox{-}O}
).
}
$$

Paper 07 因而完成 EPCA-4：Autonomously Orchestrated Compute Platform 的理論閉合。但「autonomous」在此不表示不可控的 AI；它表示 appliance 能在 task constraints、module state、benchmark evidence 與明確 authority boundary 下，自主形成、驗證、執行、監測與必要時重新規劃計算路徑。

**關鍵詞：** EPCA、Heterogeneous Computing、Benchmarking、Task Routing、Accelerator Scheduling、Execution Planning、Capability Descriptor、Requirement Manifest、Deterministic Orchestration、AI Orchestration、Pareto Routing、Provenance、Assurance、Field Computing、Physical Computing

---

## 1. 最後一個缺口：誰決定「在哪裡算」

Paper 05 已允許：

$$
\mathcal P_1,\mathcal P_2,\ldots,\mathcal P_n
$$

同時存在於同一台 appliance。

Paper 06 又允許：

$$
\text{physical}
+
\text{digital}
+
\text{refinement}
+
\text{verification}
$$

形成多階段計算鏈。

這意味著對同一個任務 $\tau$，可能同時存在：

$$
p_1,p_2,\ldots,p_k.
$$

它們都「可以算」，但不代表都「應該被選」。

---

## 2. Routing 不只是 device selection

最簡單的 heterogeneous offload 問題常被寫成：

$$
\text{task}
\rightarrow
\text{device}.
$$

EPCA 更接近：

$$
\boxed{
\text{task graph}
\rightarrow
\text{execution path}
}
$$

因為一條 path 可能包括：

- preprocessing；
- module configuration；
- warm-up；
- calibration check；
- physical primitive；
- readout；
- digital refinement；
- cross-validation；
- evidence commit；
- final result commit。

因此選擇的不是一顆晶片，而是一條計算因果鏈。

---

## 3. Execution Path

定義 execution path：

$$
p
=
(v_1,v_2,\ldots,v_n),
$$

其中每個 $v_j$ 可以是：

- CPU step；
- FPGA step；
- optical/RF/acoustic physical step；
- ADC/DAC/readout；
- calibration step；
- verification step；
- refinement step；
- storage/evidence step。

路徑成立不只要求 functional compatibility，還要求整條鏈符合 task contract。

---

## 4. Task Requirement Manifest

本文使用：

$$
R_\tau
=
(
F,
D,
Q,
L,
E,
A,
O,
C,
S,
P
).
$$

這不是單一 API 必須採用的欄位格式，而是一個 canonical semantic model。

---

## 5. Functional Requirement $F$

 $F$ 描述任務要做什麼，例如：

$$
F=
\text{FFT}_{N},
$$

或：

$$
F=
Ax,
$$

或：

$$
F=
\text{root solve},
$$

或一個 DAG：

$$
F=
G_\tau=(V_\tau,E_\tau).
$$

---

## 6. Data Domain $D$

同一 operator 在不同輸入 domain 下可能完全不同。

因此必須聲明：

$$
D=
(
\text{shape},
\text{range},
\text{sparsity},
\text{stream/batch},
\text{rate}
).
$$

一個只在 $64\times64$ matrix 上校正過的 photonic module，不能因為名字叫 matrix multiplier 就自動承諾任意大小。

---

## 7. Quality Requirement $Q$

 $Q$ 可以包含：

$$
Q=
(
\epsilon_{\max},
u_{\max},
q_{\min},
\text{confidence}
).
$$

其中：

- $\epsilon_{\max}$：最大允許 numerical/task error；
- $u_{\max}$：允許 uncertainty；
- $q_{\min}$：最低品質等級；
- confidence：統計或驗證要求。

---

## 8. Latency Requirement $L$

Latency 不只是一個平均值。

可能需要：

$$
L=
(
T_{\mathrm{deadline}},
T_{p99},
J_{\max}
),
$$

其中 $J_{\max}$ 是 jitter constraint。

對 real-time field appliance，平均很快但 tail latency 很差，可能不可用。

---

## 9. Energy Requirement $E$

可以寫成：

$$
E=
(
E_{\max},
P_{\max},
P_{\mathrm{thermal}}
).
$$

這使 battery-powered、passively cooled 或熱受限現場設備可以使用不同 policy。

---

## 10. Assurance Requirement $A$

Paper 02 至 Paper 06 已提供五個 assurance 維度。

因此：

$$
A_{\min}
=
(
V_{\min},
S_{\min},
F_{\min},
M_{\min},
R_{\min}
).
$$

任何候選 route 若低於其中一個 hard minimum：

$$
p\notin\mathcal C_\tau.
$$

---

## 11. Offline Requirement $O$

任務可聲明：

$$
O\in
\{
\text{network-allowed},
\text{offline-preferred},
\text{offline-required}
\}.
$$

若：

$$
O=\text{offline-required},
$$

則 Paper 04 的：

$$
\mathrm{LEC}_{\tau}(t)=1
$$

成為硬門檻。

---

## 12. Physical Contribution Constraint $C$

有些任務只是要答案。

另一些科研任務要求 physical core 真的參與。

因此：

$$
C\in
\{
\text{digital-allowed},
\text{hybrid},
\text{physical-primary},
\text{physical-required}
\}.
$$

這直接連到 Paper 06 的 Physical Contribution Class。

---

## 13. Safety and Security Constraint $S$

某些 module 可能具有：

- laser emission；
- RF emission；
- high-voltage analog front end；
- thermal limit；
- mechanical/acoustic power limit。

因此某條 route 在 laboratory mode 合法，不代表在 field enclosure 下合法。

---

## 14. Provenance/Evidence Policy $P$

任務可要求：

$$
P=
(
\text{retention},
\text{raw-evidence},
\text{replay},
\text{signing},
\text{audit}
).
$$

因此 benchmark winner 不一定是 evidence cost 最低者。

---

## 15. Capability Descriptor 不是規格表廣告

對 module $i$：

$$
K_i(t)
=
(
\Phi_i,
\Omega_i,
\Lambda_i,
\mathcal E_i,
\mathcal Q_i,
\mathcal A_i,
\mathcal K_i,
\mathcal H_i,
\mathcal W_i
).
$$

這是 runtime 可用能力，不是 datasheet peak number。

---

## 16. Operator Set $\Phi_i$

 $\Phi_i$ 描述：

$$
\Phi_i=
\{
f_1,f_2,\ldots,f_m
\}.
$$

但每個 operator 都必須綁定 operating domain。

---

## 17. Valid Operating Domain $\Omega_i$

例如：

$$
\Omega_i=
[
T_{\min},T_{\max}
]
\times
[
V_{\min},V_{\max}
]
\times
\text{calibration-state}.
$$

只要離開：

$$
s_t\notin\Omega_i,
$$

能力聲明就應降級或失效。

---

## 18. Latency Profile $\Lambda_i$

不應只存：

$$
T=3\text{ ns}.
$$

而應至少區分：

$$
T_{\mathrm{total}}
=
T_{\mathrm{setup}}
+
T_{\mathrm{transfer}}
+
T_{\mathrm{compute}}
+
T_{\mathrm{readout}}
+
T_{\mathrm{verify}}
+
T_{\mathrm{refine}}.
$$

---

## 19. Energy Profile $\mathcal E_i$

同樣地：

$$
E_{\mathrm{total}}
=
E_{\mathrm{idle}}
+
E_{\mathrm{configure}}
+
E_{\mathrm{compute}}
+
E_{\mathrm{conversion}}
+
E_{\mathrm{cooling}}
+
E_{\mathrm{verify}}.
$$

因此只報 core operation energy 可能嚴重誤導。

---

## 20. Quality Envelope $\mathcal Q_i$

 $\mathcal Q_i$ 必須與 Paper 06 的 calibration/error model 相容。

它不是：

$$
\text{accuracy}=99.9\%.
$$

而是 task/domain-relative：

$$
\mathcal Q_i
=
Q(
F,D,\kappa_t,\theta_t
).
$$

---

## 21. Assurance Ceiling $\mathcal A_i$

某 module 即使速度極快，若只能提供 OPC-V1：

$$
\mathcal A_i^{V}=1,
$$

就不能執行要求 OPC-V4 的科研任務。

---

## 22. Calibration State $\mathcal K_i$

Routing 必須知道：

$$
\kappa_i
\in
\{
\text{valid},
\text{stale},
\text{invalid},
\text{unknown}
\}.
$$

若 calibration 是 hard requirement：

$$
\kappa_i\neq\text{valid}
\Rightarrow
p_i\notin\mathcal C_\tau.
$$

---

## 23. Health State $\mathcal H_i$

包含：

- temperature；
- voltage；
- laser/transducer health；
- sensor health；
- ECC/error counters；
- drift；
- fault history。

---

## 24. Wear and Reconfiguration State $\mathcal W_i$

對 phase-change、memristive、flash-like、mechanical 或有有限 configuration lifetime 的 module，routing 不應假設每一次使用成本相同。

可以加入：

$$
W_i=
\text{estimated wear cost}.
$$

---

## 25. Benchmark 不是一張排行榜

EPCA benchmark 的目的不是回答：

> 哪一個 substrate 最強？

而是回答：

> 在明確條件下，它現在能對哪些任務作出什麼可驗證承諾？

---

## 26. Benchmark Family B0：Primitive Benchmark

測試最小 primitive：

- add；
- MAC；
- transform；
- routing；
- correlation；
- convolution；
- threshold；
- matrix tile。

Primitive benchmark 用來建立底層模型，不直接代表 end-to-end performance。

---

## 27. Benchmark Family B1：Module Benchmark

Module benchmark 包含：

$$
\text{input}
\rightarrow
\text{module}
\rightarrow
\text{readout}.
$$

開始納入：

- conversion；
- transfer；
- calibration；
- readout；
- module-local control。

---

## 28. Benchmark Family B2：Pipeline Benchmark

測量：

$$
\text{encode}
\rightarrow
\mathcal P
\rightarrow
\text{readout}
\rightarrow
\text{refine}
\rightarrow
y.
$$

這才接近實際可交付計算。

---

## 29. Benchmark Family B3：Field-State Benchmark

在不同：

$$
(T,V,H,\text{network},\text{battery},\text{load})
$$

條件下量測。

Field appliance 不應只在實驗室最佳狀態有 benchmark。

---

## 30. Benchmark Family B4：Assurance/Evidence Benchmark

測量 verification 本身的成本：

$$
T_{\mathrm{evidence}},
E_{\mathrm{evidence}},
S_{\mathrm{evidence}}.
$$

因為 OPC-V5 / CRA-R5 並不是免費的。

---

## 31. Benchmark Snapshot

每一筆 benchmark 應被視為：

$$
b=
(
m,
f,
d,
v_{\mathrm{fw}},
v_{\mathrm{rt}},
\kappa,
\theta,
n,
\mu,
\sigma,
t
).
$$

至少包含 module、operator、domain、版本、calibration、operating condition、sample count、統計與時間。

---

## 32. Peak Number 不能永久成為 Capability

如果某次在最佳條件測得：

$$
T_{\min}=1,
$$

不代表所有後續任務都能假設：

$$
T=1.
$$

因此：

$$
\boxed{
\text{Benchmark Observation}
\neq
\text{Permanent Capability Guarantee}.
}
$$

---

## 33. Capability 由 Benchmark + Contract + Current State 形成

runtime capability 更接近：

$$
K_i(t)
=
\mathcal G(
B_i,
C_i,
S_i(t)
).
$$

也就是歷史 benchmark、module contract 與現在 state 的交集。

---

## 34. Routing 的第一步：Hard Constraint Gate

定義：

$$
H_\tau=
\{
h_1,h_2,\ldots,h_n
\}.
$$

候選 path 集：

$$
\boxed{
\mathcal C_\tau(t)
=
\{p\mid \forall h\in H_\tau,\ h(p,t)=1\}.
}
$$

---

## 35. 不可用 Weighted Score 赦免 Hard Failure

若：

$$
V(p)<V_{\min},
$$

即使：

$$
T(p)\rightarrow0,
$$

也不能靠速度分數補回來。

因此：

$$
\boxed{
\text{Hard Constraint}
\not\leftrightarrow
\text{Soft Tradeoff}.
}
$$

---

## 36. Candidate Set 為空時

若：

$$
\mathcal C_\tau(t)=\varnothing,
$$

planner 必須回：

$$
\text{UNSATISFIABLE}
$$

或明確的：

$$
\text{DEGRADED\_OPTION\_REQUIRES\_AUTHORIZATION}.
$$

不能偷偷降低要求。

---

## 37. Soft Objectives

通過 hard gate 後，才比較：

$$
J(p)
=
(
T,
E,
U,
W,
C_{\mathrm{cfg}},
C_{\mathrm{evid}},
R_{\mathrm{risk}}
).
$$

---

## 38. Pareto Frontier

若：

$$
p_a
$$

在所有 objective 都不比 $p_b$ 差，而且至少一項更好，則 $p_b$ 可被支配。

定義：

$$
\mathcal P_\tau
=
\mathrm{Pareto}(
\mathcal C_\tau
).
$$

先縮小 candidate，避免不透明總分。

---

## 39. Lexicographic Policy

例如 field real-time policy 可以定義：

$$
\text{deadline}
\succ
\text{assurance margin}
\succ
\text{energy}
\succ
\text{wear}.
$$

科研 policy 可以是：

$$
\text{assurance}
\succ
\text{uncertainty}
\succ
\text{replayability}
\succ
\text{latency}.
$$

---

## 40. Weighted Policy 不是禁止，但必須 Versioned

若使用：

$$
S(p)
=
\sum_i w_i J_i(p),
$$

則：

$$
w_i
$$

必須成為 policy version 的一部分。

否則相同任務為何今天走 optical、明天走 FPGA 將無法重現。

---

## 41. Execution Plan

Planner 輸出：

$$
\mathcal X
=
(
G_X,
B_X,
K_X,
V_X,
R_X,
F_X
),
$$

其中：

- $G_X$：execution DAG；
- $B_X$：module/route bindings；
- $K_X$：required calibration；
- $V_X$：verification actions；
- $R_X$：refinement actions；
- $F_X$：fallback/recovery policy。

---

## 42. Execution Plan 不是建議文字

可執行 plan 必須明確到能被 supervisor 驗證。

例如：

$$
v_3
\mapsto
(m_2,\text{operator}_7,\kappa_{42},q_3).
$$

而不是：

> 大概用光學比較快。

---

## 43. Plan Identity

可以定義：

$$
ID_X
=
H(
R_\tau
\Vert
S_t
\Vert
B_v
\Vert
P_v
\Vert
\mathcal X
).
$$

它讓 result provenance 能回溯到「為什麼當時走這條路」。

---

## 44. Deterministic Planner 是第一個正式版本

本文首先要求：

$$
\Pi_D:
(R_\tau,S_t,B_v,P_v)
\mapsto
\mathcal X.
$$

不需要 AI。

---

## 45. Deterministic Reproducibility

對相同：

$$
R_\tau,S_t,B_v,P_v,
$$

必須：

$$
\boxed{
\Pi_D(R_\tau,S_t,B_v,P_v)
=
\Pi_D(R_\tau,S_t,B_v,P_v).
}
$$

如果使用 randomized optimization，random seed 也必須進入 provenance。

---

## 46. Planner Policy Version

 $P_v$ 應包括：

- hard constraint semantics；
- objective order；
- tie-break rules；
- fallback policy；
- route blacklist；
- risk budget；
- benchmark freshness policy。

---

## 47. Tie-Break 必須明確

若兩條 route 完全同等，仍需 deterministic tie-break：

$$
\text{module ID}
\prec
\text{route ID}
$$

或其他固定規則。

否則 plan replay 可能不一致。

---

## 48. Scheduling 與 Routing 的差異

Routing 回答：

$$
\text{which path?}
$$

Scheduling 回答：

$$
\text{when and in what order?}
$$

EPCA-4 同時需要兩者。

---

## 49. Task Graph

對 DAG：

$$
G_\tau=(V,E),
$$

每個 node 都可能有多個候選 substrate：

$$
C(v_j)=\{m_a,m_b,m_c\}.
$$

此時 planner 同時解 mapping 與 ordering。

---

## 50. Communication/Conversion Cost

跨 substrate 的 edge：

$$
e_{ij}
$$

可能包含：

- memory copy；
- ADC/DAC；
- serialization；
- optical/electrical conversion；
- RF/acoustic transduction；
- format conversion。

因此：

$$
T_{\mathrm{edge}}
\neq0.
$$

---

## 51. 「最快核心」可能讓整體更慢

如果：

$$
T_{\mathrm{core}}^{A}
<
T_{\mathrm{core}}^{B},
$$

但：

$$
T_{\mathrm{transfer}}^{A}
\gg
T_{\mathrm{transfer}}^{B},
$$

就可能：

$$
T_{\mathrm{total}}^{A}
>
T_{\mathrm{total}}^{B}.
$$

這正是 heterogeneous scheduling 必須看 end-to-end chain 的原因。

---

## 52. Contention

多個 task 可能競爭：

- memory bus；
- ADC；
- DAC；
- PCIe/CXL link；
- optical source；
- RF front-end；
- shared FPGA fabric；
- evidence storage。

因此：

$$
T(p,t)
$$

是 system-state dependent。

---

## 53. Static Benchmark 不等於 Runtime Prediction

需要：

$$
\hat T(p\mid S_t).
$$

Planner 可以從 benchmark database 建 model，但必須保留：

$$
\text{prediction}
\neq
\text{measurement}.
$$

---

## 54. Runtime Monitor

執行時監測：

$$
M_t
=
(
T,
E,
Q,
U,
H,
C
).
$$

若實際值越過 contract：

$$
M_t\not\models R_\tau,
$$

才觸發 replan 或 fail policy。

---

## 55. Replanning 不是任意改路

動態 replanning 必須再次經過：

$$
\text{Requirement Gate}
\rightarrow
\text{Capability Gate}
\rightarrow
\text{Authority Gate}.
$$

它不能因為「原 route 慢」就改去一個 assurance 不合格的 route。

---

## 56. Plan Commit Gate

Paper 03 的 supervisor authority 可以擴展出：

$$
\boxed{
\text{Plan Commit Gate}.
}
$$

只有通過 validator 的 $\mathcal X$ 才能進入 execution。

---

## 57. Benchmark Integrity

Benchmark database 若可被任意修改，routing assurance 就失去意義。

因此：

$$
B_v
$$

必須 versioned、signed 或至少具有 immutable lineage。

---

## 58. Benchmark Freshness

對容易漂移的 substrate：

$$
\text{age}(b)>T_{\max}
$$

時，benchmark 只能作 historical prior，不應直接作 current guarantee。

---

## 59. Calibration-Aware Routing

若 route $p_1$ 要重新校正：

$$
T_{\mathrm{cal}}(p_1)>0,
$$

planner 應比較：

$$
T_{\mathrm{cal}}+T_{\mathrm{exec}}
$$

而不是只看 compute time。

---

## 60. Warm-Up-Aware Routing

Laser、analog front-end、temperature-sensitive module 可能需要：

$$
T_{\mathrm{warm}}.
$$

短任務可能根本不值得啟動最快的物理核心。

---

## 61. Batch-Amortized Routing

如果：

$$
N\gg1,
$$

setup/calibration cost 可以被攤薄。

因此最優 route 可能隨 batch size 改變：

$$
p^*(N_1)\neq p^*(N_2).
$$

---

## 62. Energy-Amortized Routing

同理：

$$
E_{\mathrm{setup}}
$$

對短任務和長任務的影響不同。

---

## 63. Evidence Cost-Aware Routing

如果任務要求 CRA-R5，某 route 需要保存巨大 raw waveform：

$$
S_{\mathrm{evid}}\gg0.
$$

另一個 route 可能較慢，但 evidence 更容易閉合。

科研模式下後者可能更好。

---

## 64. Wear-Aware Routing

若兩條 route 都符合 hard constraints，planner 可以避免總是選同一個有有限壽命的 module。

例如：

$$
J_W(p)
=
\Delta\mathrm{wear}(p).
$$

---

## 65. Risk-Aware Routing

可以加入：

$$
R_{\mathrm{risk}}
=
P(\text{failure}\mid S_t)
\times
C(\text{failure}).
$$

但 risk model 必須可審計，不能變成不透明黑箱。

---

## 66. Benchmark 不應只測 Speedup

EPCA 至少應同時保留：

$$
(
T,
E,
Q,
U,
A,
C_{\mathrm{evid}},
C_{\mathrm{cfg}},
H
).
$$

否則「10 倍快」沒有足夠工程含義。

---

## 67. Cross-Substrate Benchmark

真正有用的比較單位應是同一 task contract：

$$
R_\tau.
$$

而不是拿 optical MAC peak 與 CPU general workload peak 直接比。

---

## 68. Same Task, Same Evidence Boundary

比較時必須確保：

$$
\text{input boundary},
\text{output boundary},
\text{verification boundary}
$$

一致。

否則某一方只算 core、另一方算 full pipeline，數字不可比較。

---

## 69. Benchmark Claim Scope

任何 benchmark claim 都應寫成：

$$
\mathrm{Claim}
=
(
\tau,
D,
S,
A,
B_v
).
$$

而不是：

> EPCA 比 GPU 快 100 倍。

---

## 70. No Universal Winner Principle

只要不同 task 對：

$$
T,E,Q,A,O,P
$$

的權重不同，就不存在單一 universal winner。

因此：

$$
\boxed{
\text{Heterogeneous Platform}
\Rightarrow
\text{Contextual Optimality}.
}
$$

---

## 71. 這正是 EPCA-4 的理由

EPCA-3 已有多 substrate。

EPCA-4 的必要條件不是再多裝一顆 accelerator，而是：

$$
\boxed{
\text{the appliance can decide among valid compute paths}.
}
$$

---

## 72. Autonomous 不等於 AI

本文定義：

$$
\text{Autonomous}
=
\text{local closed-loop planning under declared constraints}.
$$

因此 deterministic planner 完全可以是 autonomous。

---

## 73. AI 不應是架構成立的前提

第一代：

$$
\boxed{
\mathrm{EPCA\mbox{-}4}
\text{ can be fully deterministic.}
}
$$

這對 offline field operation、verification 與 certification 更容易。

---

## 74. AI 最適合加入哪裡

AI 比較適合：

- task decomposition proposal；
- unknown operator mapping suggestion；
- benchmark anomaly explanation；
- multi-objective search heuristic；
- route candidate generation；
- natural-language requirement compilation；
- experiment design；
- failure diagnosis。

而不是直接擁有 final execution authority。

---

## 75. AI Proposal Layer

定義：

$$
\Pi_{AI}(
R_\tau,S_t,B_v
)
\rightarrow
\{
\mathcal X_1,\ldots,\mathcal X_k
\}.
$$

AI 可以提出候選 plan。

---

## 76. Deterministic Validator

每個 AI proposal 必須經：

$$
V_D(
\mathcal X,
R_\tau,
S_t,
B_v,
P_v
)
\in
\{
\mathrm{ACCEPT},
\mathrm{REJECT}
\}.
$$

---

## 77. AI 沒有權限改 Requirement Manifest

如果：

$$
R_\tau
$$

要求 OPC-V4，AI 不可以因為「速度更快」改成 OPC-V2。

只有具有明確 authority 的使用者／policy layer 才能建立新 manifest。

---

## 78. AI 不得偽造 Benchmark

AI 可以估計：

$$
\hat T,
$$

但估計必須標為：

$$
\text{predicted}.
$$

不能寫入：

$$
B_v
$$

當成 measured benchmark，除非真的執行 benchmark protocol。

---

## 79. AI 不得跳過 Calibration

若：

$$
\kappa_i=\text{invalid},
$$

validator 必須拒絕依賴該 calibration 的 physical-primary route。

AI 的信心不能取代 calibration evidence。

---

## 80. AI 不得 Silent Substitute

如果 physical route 失敗，AI 不能把 CPU 重算結果偷偷包成原 route 結果。

Paper 03 與 Paper 06 的：

$$
\text{No Silent Substitution}
+
\text{Refinement Non-Erasure}
$$

仍然成立。

---

## 81. AI Plan 必須可編譯成 Canonical Plan

自然語言：

> 用較快的光學路徑，必要時補數位修正。

不能直接執行。

必須被 lowering 成：

$$
\mathcal X.
$$

---

## 82. Requirement Compiler

未來可以有：

$$
\mathcal C_R:
\text{Human/AI Intent}
\rightarrow
R_\tau.
$$

但生成後必須顯示／驗證 hard constraints。

---

## 83. Plan Compiler

可以有：

$$
\mathcal C_X:
\text{High-Level Plan}
\rightarrow
\text{Executable DAG}.
$$

這與現有 heterogeneous compiler infrastructure 的精神相容，但 EPCA 額外保留 assurance/evidence semantics。

---

## 84. MLIR 類中介層的啟示

現有 MLIR 的核心目標之一就是降低 heterogeneous hardware compiler fragmentation，允許多層 intermediate representation 與 target-specific lowering。

EPCA 可以借用這種思想：

$$
\text{Task IR}
\rightarrow
\text{EPCA Plan IR}
\rightarrow
\text{Module Binding}.
$$

但 EPCA Plan IR 還必須帶有：

$$
\text{assurance}
+
\text{calibration}
+
\text{evidence}
+
\text{offline}
$$

語義。

---

## 85. OpenMP / SYCL 的啟示

OpenMP target offload 與 SYCL 都已經證明：

$$
\text{one application}
\rightarrow
\text{heterogeneous devices}
$$

可以有標準化 programming model。

EPCA 的差異是：

$$
\boxed{
\text{device compatibility}
+
\text{physical evidence compatibility}.
}
$$

---

## 86. EPCA 不必重新發明所有 Compiler

EPCA 可以把：

- MLIR；
- LLVM；
- OpenMP；
- SYCL；
- vendor SDK；
- FPGA toolchain

當作下層 backend。

新工作主要位於：

$$
\text{requirement}
+
\text{routing}
+
\text{assurance}
+
\text{evidence}.
$$

---

## 87. Planning Snapshot

在 plan commit 時保存：

$$
S_{\mathrm{plan}}
=
(
R_\tau,
S_t,
B_v,
P_v,
\mathcal X
).
$$

---

## 88. Execution Snapshot

執行開始保存：

$$
S_{\mathrm{exec}}.
$$

如果 hardware state 已大幅改變：

$$
d(S_{\mathrm{plan}},S_{\mathrm{exec}})>\delta,
$$

應重新驗證。

---

## 89. Runtime Drift

若執行中：

$$
\kappa_t
\rightarrow
\text{stale},
$$

或 thermal state 超出 envelope，planner 需要依 policy：

- pause；
- recalibrate；
- replan；
- fail closed；
- explicit fallback。

---

## 90. Fallback 是 Plan 的一部分

不能等失敗後才臨時「想辦法」。

應在 $\mathcal X$ 中聲明：

$$
F_X
=
(
f_1,f_2,\ldots
).
$$

---

## 91. Fallback 也有 Assurance

若 primary route 是：

$$
Q_{\mathrm{EPCA}}\ge q,
$$

fallback 若低於要求：

$$
q_F<q,
$$

就只能：

$$
\text{stop}
$$

或要求新的授權。

---

## 92. Retry Budget

Physical system 可能有 stochastic noise。

可以定義：

$$
N_{\mathrm{retry}}\le N_{\max}.
$$

但 retry 不能無限重試直到「剛好得到想要答案」。

---

## 93. Adaptive Verification

若 first-pass confidence 足夠：

$$
u\le u_{\mathrm{target}},
$$

可使用低成本 verification。

若：

$$
u>u_{\mathrm{target}},
$$

再升級到 cross-path verification。

---

## 94. Adaptive Precision

同理：

$$
\text{coarse physical result}
\rightarrow
\text{residual}
\rightarrow
\text{refine only if needed}.
$$

Paper 06 的 mixed precision 在 Paper 07 變成 planner 的決策空間。

---

## 95. Planner 不只選 Module，也選 Precision Path

可能有：

$$
p_1:
\text{CIM 4-bit}
\rightarrow
\text{CPU refine},
$$

$$
p_2:
\text{FPGA fixed-point},
$$

$$
p_3:
\text{CPU FP64}.
$$

三條都是 candidate path。

---

## 96. Planner 不只選 Precision，也選 Evidence Path

例如：

$$
p_a:
\mathrm{OPC\mbox{-}V2},
$$

$$
p_b:
\mathrm{OPC\mbox{-}V5}.
$$

如果 task 只要求 V2，選 V5 可能浪費時間與儲存。

---

## 97. Assurance Is a Resource

因此：

$$
\boxed{
\text{Assurance}
\text{ has cost.}
}
$$

這不是要降低 assurance，而是讓 planner 知道不同任務需要多少 evidence。

---

## 98. Over-Verification 也可能是浪費

展示模式可能只需要：

$$
V1/R1.
$$

科研 publication mode 可能需要：

$$
V5/R5.
$$

兩者不應被強迫使用同一成本。

---

## 99. Mode Profiles

可以定義：

### Demonstration Profile

優先：

$$
\text{observability}
+
\text{human legibility}.
$$

### Field Profile

優先：

$$
\text{deadline}
+
\text{offline closure}
+
\text{recovery}.
$$

### Research Profile

優先：

$$
\text{evidence}
+
\text{replay}
+
\text{uncertainty}.
$$

### Throughput Profile

優先：

$$
\text{steady-state throughput}
+
\text{energy}.
$$

---

## 100. Profile 仍不能改 Hard Constraints

Profile 只是 soft policy template。

如果 task manifest 明確要求：

$$
\mathrm{CRA\mbox{-}R5},
$$

Throughput Profile 也不能降級。

---

## 101. Orchestration Assurance ORA

本文新增第六軸：

$$
\mathrm{ORA\mbox{-}O0}
\rightarrow
\mathrm{ORA\mbox{-}O5}.
$$

---

## 102. ORA-O0 — Ad Hoc Routing

特徵：

- manual；
- undocumented；
- no requirement manifest；
- no reproducible plan。

適合原型，不適合正式聲明自治。

---

## 103. ORA-O1 — Declared Requirements

至少具有：

$$
R_\tau.
$$

能說明為何某 route 被選。

---

## 104. ORA-O2 — Deterministic Eligibility Gate

具有：

$$
\mathcal C_\tau
=
\{p\mid p\models H_\tau\}.
$$

不允許硬約束被 soft score 蓋過。

---

## 105. ORA-O3 — Costed and Provenance-Bound Planning

保存：

$$
B_v,
P_v,
S_t,
\mathcal X,
ID_X.
$$

可以 replay「當時為什麼選這條路」。

---

## 106. ORA-O4 — Monitored and Recoverable Dynamic Orchestration

具備：

- runtime monitor；
- drift detection；
- bounded retry；
- declared fallback；
- replan gate；
- evidence-preserving recovery。

---

## 107. ORA-O5 — Independently Auditable Orchestration

要求：

- requirement manifest 可審計；
- benchmark/capability lineage 可審計；
- planner version 固定；
- plan commit 可重播；
- dynamic replan 有完整證據；
- 若 AI 參與，AI 僅 proposal，deterministic validator 保留 final gate。

---

## 108. ORA-O5 不等於一定需要 AI

$$
\boxed{
\mathrm{ORA\mbox{-}O5}
\not\Rightarrow
\text{AI required}.
}
$$

完全 deterministic 的 planner 也可以達到 O5。

---

## 109. AI 的 Assurance 不是另一套物理真理

AI 只增加：

$$
\text{search capacity}
+
\text{proposal flexibility}
+
\text{explanation}.
$$

不增加：

$$
\text{physical authority}.
$$

---

## 110. 最終六軸座標

系列收斂為：

$$
\boxed{
Q_{\mathrm{EPCA}}
=
(
\mathrm{OPC\mbox{-}V},
\mathrm{ESA\mbox{-}S},
\mathrm{LFA\mbox{-}F},
\mathrm{MSA\mbox{-}M},
\mathrm{CRA\mbox{-}R},
\mathrm{ORA\mbox{-}O}
).
}
$$

---

## 111. 六軸不能平均

例如：

$$
(5,5,0,5,5,5)
$$

不能因平均很高就稱為良好 field appliance。

因為：

$$
\mathrm{LFA\mbox{-}F0}
$$

表示它仍是 network-bound。

---

## 112. 六軸是 Capability Vector

因此：

$$
Q_{\mathrm{EPCA}}
$$

應被視為 constraint vector，而不是 maturity scalar。

---

## 113. EPCA-0 至 EPCA-4 的最終解釋

### EPCA-0

Observable Physical Calculator。

### EPCA-1

Supervised Physical Calculator。

### EPCA-2

Offline-First Field Appliance。

### EPCA-3

Modular Multi-Substrate Appliance。

### EPCA-4

Autonomously Orchestrated Compute Platform。

---

## 114. EPCA-4 的最低定義

本文建議至少：

$$
\mathrm{ORA\mbox{-}O2}
$$

才能宣稱有基本 autonomous routing。

正式科研／工程平台則應往：

$$
\mathrm{ORA\mbox{-}O4/O5}
$$

前進。

---

## 115. 第一代 MVP 不需要做到 EPCA-4 全部

如果未來真正實作，可以先：

$$
\boxed{
\text{one physical module}
+
\text{one digital reference}
+
\text{one deterministic planner}.
}
$$

---

## 116. 最小 Demonstrator Route

例如：

$$
R_\tau
\rightarrow
\{
p_{\mathrm{physical}},
p_{\mathrm{digital}}
\}
\rightarrow
\Pi_D
\rightarrow
\mathcal X.
$$

兩條 path 已足以證明 routing architecture。

---

## 117. 第一代 Benchmark Database 也可以很小

只要：

- 10 至 20 種 task；
- 幾種 input size；
- latency；
- error；
- energy；
- calibration validity；
- evidence cost。

即可開始。

---

## 118. 最重要的是 Semantic Correctness

MVP 不必一開始追求：

$$
\max \mathrm{performance}.
$$

更重要是：

$$
\boxed{
\text{route selection can be explained, reproduced, and falsified}.
}
$$

---

## 119. 為什麼這跟一般 Accelerator Runtime 不完全相同

一般 accelerator runtime 主要關心：

$$
\text{compatibility}
+
\text{performance}
+
\text{resource utilization}.
$$

EPCA 額外把：

$$
\text{physical causality}
+
\text{calibration}
+
\text{assurance}
+
\text{evidence}
+
\text{offline closure}
$$

放進 first-class semantics。

---

## 120. 為什麼這跟 Scientific Instrument 也不完全相同

傳統 scientific instrument 通常：

$$
\text{instrument function}
$$

相對固定。

EPCA 則：

$$
\text{replaceable compute substrate}
+
\text{replaceable algorithm package}
+
\text{dynamic route}.
$$

所以它介於 calculator、instrument、accelerator 與 computer 之間，但不能完全被其中任何一個類別吸收。

---

## 121. 這也完成「讓計算機回到計算本身」

Paper 00 的起點是：

$$
\boxed{
\text{Machine exists because there is something to compute.}
}
$$

Paper 07 回到同一命題，但現在機器不只會算，還會在限制內決定：

$$
\boxed{
\text{how this computation should physically happen}.
}
$$

---

## 122. 從算盤到自治路由

整個系列真正的演化可以壓縮成：

$$
\text{bead}
\rightarrow
\text{carrier}
\rightarrow
\text{field/wave state}
\rightarrow
\text{observable physical computation}
\rightarrow
\text{verified compute core}
\rightarrow
\text{field appliance}
\rightarrow
\text{replaceable substrates}
\rightarrow
\text{evidence-bearing result}
\rightarrow
\text{autonomous routing}.
$$

---

## 123. 但自主性沒有消除因果責任

即使未來 AI planner 很強：

$$
\text{proposal quality}\uparrow,
$$

仍不推出：

$$
\text{authority}\uparrow
$$

到可以繞過 architecture。

這延續 Paper 03：

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

---

## 124. 未來 AI 可以做更高階的事情

例如從 task 自動發現：

$$
F
=
f_3\circ f_2\circ f_1
$$

並提出：

$$
f_1\mapsto\text{RF},
$$

$$
f_2\mapsto\text{CIM},
$$

$$
f_3\mapsto\text{CPU refine}.
$$

但每一步仍須被 compiler/validator 證明符合 contract。

---

## 125. AI 也可以主動要求 Benchmark

如果 AI 發現：

$$
\mathrm{Var}[\hat T(p)]
$$

太大，它可以提出：

> 先跑 calibration/benchmark probe，再選 route。

這是 AI 很適合的角色。

---

## 126. Active Benchmarking

定義 probe：

$$
b^*
=
\arg\max_b
\mathrm{InformationGain}(b).
$$

未來 planner 可以在運算前先花少量成本，降低 route uncertainty。

---

## 127. 這會讓 EPCA 變成會「認識自己硬體」的計算機

不是神秘自我意識，而是很工程化地：

$$
\boxed{
\text{self-characterizing compute appliance}.
}
$$

它持續知道：

- 哪些 module 可用；
- 哪些 benchmark 已過期；
- 哪些 calibration 需要更新；
- 哪些 route 最近失敗；
- 哪些 workload 最適合哪條 path。

---

## 128. Local Learning 也不必是 AI

最簡單可以只是：

$$
\text{EWMA},
\text{Kalman-like estimator},
\text{Bayesian update},
\text{table update}.
$$

用來更新 runtime cost model。

---

## 129. Learned Cost Model 必須與 Measured Evidence 分開

預測：

$$
\hat T
$$

不能覆寫實測：

$$
T_{\mathrm{obs}}.
$$

兩者都進 provenance。

---

## 130. Model Drift

若：

$$
|\hat T-T_{\mathrm{obs}}|>\delta
$$

持續發生，planner 應降低 model confidence。

---

## 131. Offline Autonomy 與 Orchestration 相容

Paper 04 的核心是：

$$
\mathrm{LEC}_\tau(t)=1.
$$

因此 planner、benchmark snapshot、policy、module contract 都應可本地使用。

---

## 132. Cloud 不是控制平面的單點依賴

網路存在時可以：

- 更新 benchmark corpus；
- 下載新 algorithm package；
- 取得新 planner policy；
- 遠端審計；
- 協同模型。

斷網時：

$$
\boxed{
\text{existing authorized compute remains local}.
}
$$

---

## 133. Remote AI 也只是 Enhancement

若 AI orchestration 依賴 cloud model，斷網後仍應：

$$
\Pi_D
$$

接管基本 routing。

因此：

$$
\boxed{
\text{AI-enhanced}
\neq
\text{AI-dependent}.
}
$$

---

## 134. On-Device AI 的位置

未來 local model 可以：

$$
\Pi_{AI}^{\mathrm{local}}.
$$

但一樣經過：

$$
V_D.
$$

---

## 135. 安全模式

若 planner database 損壞：

$$
B_v=\text{invalid},
$$

設備應回到：

- known-safe route；
- digital reference route；
- restricted manual mode；
- fail closed。

而不是猜一條路。

---

## 136. Known-Safe Route

可以為每個 critical task 預先保存：

$$
p_{\mathrm{safe}}.
$$

它可能不是最快，但具有最強已知保證。

---

## 137. Emergency Compute

某些現場設備甚至可以定義：

$$
R_\tau^{\mathrm{emergency}}
$$

允許不同的 latency/energy policy，但 assurance 下限仍明確。

---

## 138. Benchmark Portability

不同 EPCA 之間可以交換 benchmark schema，但不能直接交換 performance truth。

因為：

$$
B_i
$$

綁定具體 module identity/environment。

---

## 139. Capability Template 與 Local Benchmark 的分離

Vendor 或研究者可以提供：

$$
K_i^{\mathrm{template}}.
$$

設備本地再形成：

$$
K_i^{\mathrm{local}}.
$$

Planner 應優先相信 local validated state。

---

## 140. 公開研究的好處

由於本系列目前可以公開，未來可以讓不同研究團隊提交：

- module adapter；
- capability descriptor；
- benchmark protocol；
- task manifest；
- deterministic planner；
- AI proposal agent。

而不用共享相同 physical substrate。

---

## 141. 一個真正可互通的生態系不要求同一硬體

它要求：

$$
\boxed{
\text{same semantic contracts}
}
$$

而不是：

$$
\boxed{
\text{same physical implementation}.
}
$$

這再次呼應 Paper 05：

$$
\text{Common Contract}
\neq
\text{Common Physics}.
$$

---

## 142. Series-Level Invariant 1：Physical Core Must Remain Falsifiable

從 Paper 02 到 Paper 07：

$$
\boxed{
\text{physical computation claim}
\Rightarrow
\text{falsifiable physical evidence}.
}
$$

Routing 不能破壞它。

---

## 143. Series-Level Invariant 2：Supervisor/Planner Cannot Silently Substitute

$$
\boxed{
\text{No Silent Substitution}.
}
$$

無論是 deterministic planner 或 AI planner 都一樣。

---

## 144. Series-Level Invariant 3：Offline Is a Property of the Task Closure

$$
\boxed{
\mathrm{LEC}_\tau(t)
}
$$

仍是 task-relative，而不是機器貼上「offline capable」就結束。

---

## 145. Series-Level Invariant 4：Module Is Replaceable, Evidence Is Not Anonymous

模組可以換：

$$
m_a\rightarrow m_b,
$$

但 result provenance 必須知道到底是哪一顆算的。

---

## 146. Series-Level Invariant 5：Refinement Cannot Erase Physical Lineage

$$
\boxed{
\text{Refinement Non-Erasure}.
}
$$

Planner 不能用 route optimization 規避。

---

## 147. Series-Level Invariant 6：Orchestration Cannot Downgrade Hard Requirements

$$
\boxed{
\text{Optimization}
\subset
\text{Feasible Region}.
}
$$

而不是 optimization 決定 feasible region。

---

## 148. 最終形式

整個 EPCA 可以寫成：

$$
\mathfrak E
=
(
\mathcal M,
\mathcal R,
\mathcal K,
\mathcal B,
\Pi,
\mathcal V,
\mathcal E
),
$$

其中：

- $\mathcal M$：module set；
- $\mathcal R$：task requirement semantics；
- $\mathcal K$：capability/calibration state；
- $\mathcal B$：benchmark corpus；
- $\Pi$：planner/orchestrator；
- $\mathcal V$：validator/assurance gates；
- $\mathcal E$：evidence/provenance system。

---

## 149. EPCA 的最終 execution loop

$$
\boxed{
\begin{aligned}
&\text{Task}\\
&\downarrow\\
&\text{Requirement Manifest}\\
&\downarrow\\
&\text{System/Calibration Snapshot}\\
&\downarrow\\
&\text{Candidate Enumeration}\\
&\downarrow\\
&\text{Hard Constraint Gate}\\
&\downarrow\\
&\text{Pareto / Policy Selection}\\
&\downarrow\\
&\text{Plan Validation}\\
&\downarrow\\
&\text{Plan Commit}\\
&\downarrow\\
&\text{Physical/Digital Execution}\\
&\downarrow\\
&\text{Runtime Monitoring}\\
&\downarrow\\
&\text{Evidence Commit}\\
&\downarrow\\
&\text{Evidence-Bearing Result}.
\end{aligned}
}
$$

---

## 150. AI 版只是在候選生成處增加一層

$$
\boxed{
\text{AI Proposal}
\rightarrow
\text{Canonical Plan}
\rightarrow
\text{Deterministic Validation}.
}
$$

其餘 loop 不需要改寫。

---

## 151. 因此 AI 可以被移除而系統仍成立

這是一個很重要的 architecture test：

$$
\boxed{
\text{Remove AI}
\Rightarrow
\text{EPCA still computes correctly}.
}
$$

如果移除 AI 後連基本 authorized compute 都無法運作，那它已變成 AI-dependent cloud appliance，而不是本文要定義的 offline-first EPCA。

---

## 152. 最後的 benchmark 原則

本文將 benchmark 壓縮成五條：

1. Same task boundary；
2. End-to-end cost；
3. State/calibration binding；
4. Assurance/evidence binding；
5. Versioned and replayable observation。

---

## 153. 最後的 routing 原則

Routing 壓縮成：

$$
\boxed{
\text{Filter First}
\rightarrow
\text{Optimize Second}
\rightarrow
\text{Commit Explicitly}.
}
$$

---

## 154. 最後的 AI 原則

AI orchestration 壓縮成：

$$
\boxed{
\text{AI may propose more}
\neq
\text{AI may authorize more}.
}
$$

---

## 155. 系列結論：新的「計算機」類別

最初的思維實驗只是：

> 如果算盤的珠子換成光、RF、聲、電或其他 carrier，會怎麼樣？

系列最後得到的答案比「光學算盤」更大。

算盤提醒我們：

$$
\text{computation}
$$

可以被理解為：

$$
\text{state}
+
\text{geometry}
+
\text{transition}
+
\text{observation}.
$$

一旦 carrier 可以替換，geometry 可以重構，physical core 可以 modularize，embedded supervisor 可以管理而不替算，Linux-class appliance 可以離線更新，mixed precision 可以帶著 evidence 交付，而 planner 可以在多條有效因果路徑間做 constraint-aware routing，我們得到的就不再只是某一種新 accelerator。

它更接近：

$$
\boxed{
\text{a computer whose primary identity is the organization of computation itself}.
}
$$

它可以沒有 desktop。

可以沒有 browser。

可以沒有 cloud。

甚至可以沒有 AI。

但只要：

$$
\text{task}
\rightarrow
\text{authorized physical/digital computation}
\rightarrow
\text{evidence-bearing result}
$$

在設備內形成閉合，它就是一台完整的計算機。

而當它進一步能回答：

> 這個任務此刻應該用哪一種物理方式算？

EPCA 就從 calculator 走到了 autonomous compute platform。

因此整個系列最後可以壓縮為：

$$
\boxed{
\text{讓計算機回到計算本身，
再讓計算本身重新擁有多種物理形式。}
}
$$

---

## 參考文獻與工程資料

1. Lattner, C., Amini, M., Bondhugula, U., et al. *MLIR: Scaling Compiler Infrastructure for Domain Specific Computation*. MLIR project and related publications. MLIR 的公開目標包括降低 heterogeneous hardware compiler fragmentation、支援多層 IR 與 reusable/extensible compiler infrastructure. https://mlir.llvm.org/
2. OpenMP Architecture Review Board. *OpenMP Application Programming Interface Specification Version 6.0*. November 2024. OpenMP 6.0 持續提供 target device/offload 與 heterogeneous execution semantics. https://www.openmp.org/specifications/
3. Khronos Group. *SYCL 2020 Specification, Revision 12*. 6 August 2026. SYCL 提供 single-source C++ heterogeneous programming model，支援跨 CPU、GPU、FPGA 與其他 accelerator backend 的 device selection/dispatch。https://registry.khronos.org/SYCL/
4. Zou, A., Xu, Y., Ni, Y., et al. (2025). *A Survey of Real-time Scheduling on Accelerator-based Heterogeneous Architecture for Time Critical Applications*. arXiv:2505.11970. 該綜述整理 CPU-GPU、CPU-TPU、CPU-FPGA 等 accelerator-based heterogeneous architecture 的 soft/hard real-time scheduling 問題。https://arxiv.org/abs/2505.11970
5. Shi, H., Hu, J., Xu, H., et al. (2026). *Dynamic contention-aware workflow scheduling on shared bus-based CPU-FPGA heterogeneous computing systems*. Expert Systems with Applications, 300, 130421. DOI: 10.1016/j.eswa.2025.130421. 該研究直接處理 task mapping、communication routing 與 shared-bus contention 對 workflow makespan 的影響。https://doi.org/10.1016/j.eswa.2025.130421
6. *Review of Task-Scheduling Methods for Heterogeneous Chips*. Electronics 14(6), 1191 (2025). DOI: 10.3390/electronics14061191. 該綜述討論 CPU/GPU/FPGA 等 heterogeneous chip task scheduling 與 resource mapping。https://www.mdpi.com/2079-9292/14/6/1191
7. CXL Consortium. *Compute Express Link 4.0 Specification*. 18 November 2025. CXL 4.0 提升 coherent heterogeneous memory/device connectivity，並持續支援 accelerator 與 memory expansion/fabric use cases。https://computeexpresslink.org/
8. Kubernetes. *Kubernetes v1.36: More Drivers, New Features, and the Next Era of Dynamic Resource Allocation*. 7 May 2026. DRA 是大型平台如何描述、claim、allocate specialized hardware resource 的鄰近工程參考；EPCA 不直接採用 Kubernetes，但其 resource-claim 思想證明 hardware-agnostic allocation semantics 的實際需求。https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/
9. Williams, S., Waterman, A., Patterson, D. (2009). *Roofline: An Insightful Visual Performance Model for Multicore Architectures*. Communications of the ACM, 52(4), 65-76. Roofline model 說明單一 peak metric 不足以描述不同 arithmetic intensity 與 memory bandwidth 限制下的 performance；本文借用其「performance 必須置於 workload/resource context」的基本精神，而非直接套用 Roofline 作為 EPCA benchmark。
10. Paper 02 至 Paper 06 所引用的 photonic、RF wave computing、acoustic computing、mixed-precision CIM、metrological traceability 與 provenance 文獻，構成本文 physical evidence、calibration、result assurance 與 multi-substrate execution 的前置技術背景。

---

## 前置系列與本系列銜接

- 《跨尺度構成與動態約束域研究》v0.1：approximability、finite-cost exactness、effective physical equivalence、dynamic reachability 與 constraint domain。
- 《認知功能體的物理實現與自然可觀測性研究》v0.1：存在、可觀測、可辨識、跨 substrate functional realization 與 causal history separation。
- Paper 00：EPCA、Local Execution Closure、Physical-Core Non-Substitution 與 Evidence-Bearing Result 的初步提出。
- Paper 01：Carrier-Generalized Abacus、position coding、mode coding、relation coding 與 dynamical geometry。
- Paper 02：OPC-V0 至 OPC-V5、causal intervention、ablation、independent challenge 與 falsifiable physical evidence。
- Paper 03：Declared Compute Boundary、No Silent Substitution、Reference-Path Isolation、Evidence Before Refinement 與 ESA-S0 至 ESA-S5。
- Paper 04：Local Execution Closure、transactional update、offline evidence queue、field recovery 與 LFA-F0 至 LFA-F5。
- Paper 05：Multi-Substrate Compute Backplane、Physical Module Contract、capability descriptor、calibration gate、module lifecycle、fault containment 與 MSA-M0 至 MSA-M5。
- Paper 06：Mixed-Precision Evidence-Bearing Computation、calibration lifecycle、precision negotiation、Refinement Non-Erasure、Physical Contribution Class、Evidence Envelope 與 CRA-R0 至 CRA-R5。

本篇新增 Task Requirement Manifest、versioned Capability/Benchmark Snapshot、five-family benchmark architecture、hard-constraint-first candidate filtering、Pareto/lexicographic routing、deterministic execution planner、plan identity、runtime monitored replanning、fallback semantics、AI proposal-only orchestration，以及 ORA-O0 至 ORA-O5。至此 EPCA 系列完成從 carrier-generalized physical computation 到 autonomous multi-substrate compute platform 的完整理論閉合。
