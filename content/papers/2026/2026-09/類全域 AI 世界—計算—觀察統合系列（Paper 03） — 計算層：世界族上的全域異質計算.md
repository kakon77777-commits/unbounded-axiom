# 類全域 AI 世界—計算—觀察統合系列（Paper 03）
## 計算層：世界族上的全域異質計算
### The Computation Layer: Heterogeneous Global Computation over Governed World Families

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 03 / 12  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** Global Computation Methodology × Governed World Family × Computational Configuration Space × Dynamic Computational Routing × CDI/AIVS × PNCW × Heterogeneous Runtime × Candidate/Commit  
**前篇：** Paper 02《世界層：從單一 World Model 到 Governed World Family》  
**狀態：** 計算層母規格／Runtime composition framework；不宣稱本文提供普遍最優 scheduler，也不宣稱 24/72 分類已被證明為計算形態的完備基底

---

## 摘要

Paper 02 已將類全域 AI 的世界層由單一 world model 擴張為受治理世界族：

$$
\mathfrak W_t^G.
$$

然而，擁有很多可運行 worlds 並不等於知道如何計算它們。一個類全域 AI 可能同時面對 actual-linked world、digital twin、simulation、counterfactual、replay、synthetic 與 nested worlds；每個 world 又可能包含連續物理、離散制度、圖結構、符號約束、機率過程、資料流、神經模型與外部程式。若所有 world、所有 domain 都被強迫使用同一算法、同一 timestep、同一 representation、同一 precision、同一 accelerator 與同一同步方式，所謂「全域計算」反而退化成全域同質化。

本文提出 WCO-TF 的正式 **Computation Layer**，核心命題沿用並擴張既有 Global Computation Methodology：

$$
\boxed{
\text{Global Computation}
=
\text{Globally Coherent Heterogeneous Computation}.
}
$$

本文將 Paper 01 的計算族：

$$
\mathfrak C_t
$$

細化為：

$$
\boxed{
\mathfrak C_t
=
\left(
\mathfrak F_t^{comp},
\mathfrak L_t,
\mathfrak R_t^{exec},
\mathfrak Q_t,
\mathfrak S_t,
\mathfrak V_t
\right),
}
$$

其中：

- $\mathfrak F_t^{comp}$：computational-form family；
- $\mathfrak L_t$：transition-law family；
- $\mathfrak R_t^{exec}$：resource/backend family；
- $\mathfrak Q_t$：precision / fidelity / resolution family；
- $\mathfrak S_t$：scheduling / synchronization modes；
- $\mathfrak V_t$：available validation / reconciliation procedures。

本文特別將既有 GCM 中常以 $\mathfrak P$ 表示的 computational form space 改記為：

$$
\mathfrak F^{comp}
$$

以避免與 WCO 系列中 projection family：

$$
\mathfrak P
$$

發生符號坍縮。這個重新命名本身反映本系列的核心非同一性：

$$
\boxed{
\text{Computational Form}
\neq
\text{Projection Form}.
}
$$

對受治理世界 $W_i$ 的 computational domain $D_{ij}$，本文定義計算配置：

$$
\boxed{
\kappa_{ij,t}
=
\left\langle
W_i,
D_{ij},
f_{ij},
\ell_{ij},
\lambda_{ij}^{comp},
r_{ij},
\tau_{ij},
q_{ij},
\sigma_{ij}
\right\rangle,
}
$$

其中：

- $f_{ij}\in\mathfrak F^{comp}$：computational form；
- $\ell_{ij}\in\mathfrak L$：transition law；
- $\lambda_{ij}^{comp}$：compute resolution / materialization level；
- $r_{ij}$：resource/backend target；
- $\tau_{ij}$：execution order / temporal mode；
- $q_{ij}$：precision / quality target；
- $\sigma_{ij}$：synchronization / consistency mode。

計算路由器因此不只回答「什麼時候、在哪裡跑」，而回答：

$$
\boxed{
\text{what}
+
\text{how}
+
\text{at what resolution}
+
\text{on which backend}
+
\text{under which consistency contract}.
}
$$

本文定義 World-Family Computational Router：

$$
\boxed{
\mathcal R_t^{WFC}
:
(
\mathfrak W_t^G,
D_{ij},
T,
B_t,
Risk_t,
\Gamma_t
)
\mapsto
\kappa_{ij,t}.
}
$$

其中 $T$ 是 task / intent， $B_t$ 是資源預算， $Risk_t$ 是風險狀態， $\Gamma_t$ 是 authority / admissibility constraints。

然而，真正的全域性不在 routing 本身，而在 **Global Composition and Reconciliation**。各 domain 的 local executor 可以異質地計算：

$$
\Delta_{ij}^{cand}
=
\Phi_{ij}^{f_{ij},\ell_{ij}}
\left(
S_{ij},
I_{ij}
\right),
$$

但 local success 不得直接改寫 canonical world。所有候選 delta 必須進入：

$$
\boxed{
\mathsf{Reconcile}_G
\left(
\{\Delta_{ij}^{cand}\},
\mathcal C_t^G,
\mathfrak W_t^G,
H_t
\right)
}
$$

檢查：

- cross-domain dependencies；
- cross-world coupling；
- lineage constraints；
- evidence mode；
- state versions；
- authority；
- resource receipts；
- semantic conflicts；
- global invariants；
- accumulated projection / computation debt。

只有通過 reconciliation 的候選狀態才可：

$$
Candidate
\rightarrow
Commit.
$$

因此：

$$
\boxed{
\text{Local Execution Success}
\not\Rightarrow
\text{Global Commit Admissibility}.
}
$$

本文進一步建立 **World-Family Global Computation Contract（WF-GCC）**：

$$
\boxed{
\mathsf{WF\text{-}GCC}
=
\left\langle
Boundary,
Domains,
Configurations,
Dependencies,
Budgets,
CandidateDeltas,
Reconciliation,
Commit,
History,
Certificates
\right\rangle.
}
$$

其中 `Boundary` 特別重要。全域不是對所有已存在 worlds 無限擴張，而是相對指定任務與 world boundary 建立 coherence：

$$
\boxed{
\text{Global}_B
=
\text{coherence over a designated computation boundary }B.
}
$$

本文也把 GCM 的 **Finite Active Realization + Unbounded Extensibility** 推進到 world-family level。令所有可潛在計算的 world-domain pair 為：

$$
\mathcal U_t^{comp},
$$

當下 active support 為：

$$
\mathcal A_t^{comp}
\subseteq
\mathcal U_t^{comp}.
$$

任何實際 runtime 必須有：

$$
\boxed{
|\mathcal A_t^{comp}|<\infty,
}
$$

但允許：

$$
\mathcal U_{t+1}^{comp}
\supset
\mathcal U_t^{comp}.
$$

所以：

$$
\boxed{
\text{Finite Active Computation}
+
\text{Open-Ended Computational Extensibility}.
}
$$

本文同時保留 PNCW 的四解析度分離：

$$
\boxed{
\lambda^{compute}
\neq
\lambda^{observe}
\neq
\lambda^{carrier}
\neq
\lambda^{render}.
}
$$

一個 world 可以高精度計算但只向 observer 顯示粗粒度摘要；也可以低成本 coarse simulation 先篩選 branches，再只對高價值 branch 提升 computational fidelity。這使 multi-fidelity world family 成為全域計算的自然結果，而不是例外。

最後，本文把計算歷史提升為一級狀態。即使兩條計算路徑最後得到相同 state：

$$
S_a=S_b,
$$

只要它們的 backend、seed、approximation、proof obligation、data version、resource receipt 或 intermediate failure 不同，就不應直接認為 computation history 相同：

$$
\boxed{
\text{State Equality}
\not\Rightarrow
\text{Computation-History Equality}.
}
$$

這與 MWT 的非交換歷史保存及動態不動點系列直接接合。

本文最終提出：

$$
\boxed{
\text{Global-Like AI computation is not one giant calculation.}
}
$$

而是：

$$
\boxed{
\text{a governed routing-and-reconciliation process
over heterogeneous computations distributed across a family of worlds}.
}
$$

**關鍵詞：** Global Computation、Heterogeneous Computing、World Family、Computational Routing、24/72、Transition Law、Finite Active Support、Selective Materialization、Candidate/Commit、Global Reconciliation、CDI、AIVS、PNCW

---

# 0. Paper 02 留下的計算問題

Paper 02 已建立：

$$
\mathfrak W_t^G.
$$

但世界族只是可被計算的對象集合與治理結構。

它本身沒有回答：

> 哪些 world 現在值得算？

> world 裡哪個 domain 應該算？

> 要用 deterministic、probabilistic、symbolic、graph、simulation 還是 learned model？

> 哪個 backend？

> 哪個 precision？

> 哪些可以 parallel？

> 哪些必須 serial？

> 哪些只是 candidate？

> 哪些可以 commit？

這就是 Paper 03。

---

# 1. 全域計算不是一個超大 Algorithm

本文拒絕：

$$
\boxed{
\text{Global Computation}
=
\text{One Universal Algorithm Everywhere}.
}
$$

---

# 2. 全域計算是世界相對的 Coherence

$$
\boxed{
\text{Global}_B
=
\text{coherence relative to designated boundary }B.
}
$$

 $B$ 可以是：

- 一個 world；
- 一組 worlds；
- 一組 domains；
- 一個 organization；
- 一個 simulation portfolio；
- 一個 research problem。

---

# 3. Boundary 不必等於全部 World Family

若：

$$
\mathfrak W_t^G
=
\{W_1,\ldots,W_{1000}\},
$$

一個 task 可能只需要：

$$
B_T
=
\{W_3,W_8,W_{21}\}.
$$

---

# 4. Global Dependency 不等 Full Activation

$$
\boxed{
\text{Global Dependency}
\neq
\text{Full Active Computation}.
}
$$

---

# 5. World Family 與 Computation Family

本文建立：

$$
\boxed{
(\mathfrak W_t^G,\mathfrak C_t).
}
$$

這是 Paper 03 的核心耦合物件。

---

# 6. Computation Family 正式拆解

$$
\boxed{
\mathfrak C_t
=
\left(
\mathfrak F_t^{comp},
\mathfrak L_t,
\mathfrak R_t^{exec},
\mathfrak Q_t,
\mathfrak S_t,
\mathfrak V_t
\right).
}
$$

---

# 7. Computational Form 與 Projection Form 分離

既有研究有時使用：

$$
\mathfrak P
$$

表示 computational paradigms。

但 WCO 已把：

$$
\mathfrak P
$$

保留給 projection family。

因此本文改用：

$$
\boxed{
\mathfrak F^{comp}.
}
$$

---

# 8. 核心非同一性

$$
\boxed{
\text{Computational Form}
\neq
\text{Projection Form}.
}
$$

一個 graph algorithm 可以輸出 text projection。

一個 neural computation 也可以輸出 symbolic projection。

---

# 9. Computational Forms

 $\mathfrak F^{comp}$ 可以包含：

- sequence；
- parallel；
- concurrent；
- dataflow；
- graph traversal；
- symbolic deduction；
- constraint solving；
- optimization；
- stochastic sampling；
- simulation；
- retrieval；
- theorem proving；
- learned inference；
- mixed / hybrid forms。

---

# 10. 24/72 的位置

本文不把 24/72 當成已證明完備分類。

而把它定位為：

$$
\boxed{
\text{addressable computational configuration vocabulary}.
}
$$

---

# 11. Taxonomy 不等 Runtime

$$
\boxed{
\text{Computational Taxonomy}
\neq
\text{Computational Routing}.
}
$$

---

# 12. Configuration Space

$$
\mathcal K^{comp}
=
\mathfrak F^{comp}
\times
\mathfrak L
\times
\mathfrak Q
\times
\mathfrak R^{exec}
\times
\mathfrak S.
$$

---

# 13. Transition-Law Family

$$
\mathfrak L
=
\{\ell_1,\ell_2,\ldots\}.
$$

可包含：

- discrete deterministic；
- continuous dynamics；
- stochastic transition；
- event-driven；
- hybrid；
- learned transition；
- rule-based transition。

---

# 14. 同一 World 可以多 Transition Laws

例如：

$$
W_i
=
\text{physics}
+
\text{market rules}
+
\text{agent behavior}.
$$

不同 domain 不必共享一個 $\ell$。

---

# 15. Computational Domain

對 world $W_i$：

$$
\mathcal D_i^{comp}
=
\{D_{ij}\}_{j}.
$$

---

# 16. Domain 不是硬體分區

 $D_{ij}$ 可以是：

- spatial region；
- subsystem；
- semantic domain；
- causal component；
- algorithmic subproblem；
- agent population；
- proof obligation。

---

# 17. Domain 可以跨 World

某比較任務可能建立：

$$
D^{cross}
\subset
W_i\times W_j.
$$

---

# 18. Cross-World Computation

例如：

$$
Compare(W_A,W_B)
$$

本身就是跨 world computational domain。

---

# 19. 計算配置

本文定義：

$$
\boxed{
\kappa_{ij,t}
=
\left\langle
W_i,
D_{ij},
f_{ij},
\ell_{ij},
\lambda_{ij}^{comp},
r_{ij},
\tau_{ij},
q_{ij},
\sigma_{ij}
\right\rangle.
}
$$

---

# 20. $f_{ij}$

computational form。

---

# 21. $\ell_{ij}$

transition law。

---

# 22. $\lambda_{ij}^{comp}$

compute resolution / active materialization。

---

# 23. $r_{ij}$

backend / resource target。

例如：

- CPU；
- GPU；
- NPU；
- FPGA；
- theorem prover；
- database；
- remote cluster；
- external simulator。

---

# 24. $\tau_{ij}$

execution order / temporal mode。

例如：

- immediate；
- deferred；
- batch；
- streaming；
- speculative；
- background；
- deadline-bound。

---

# 25. $q_{ij}$

precision / quality / confidence target。

---

# 26. $\sigma_{ij}$

synchronization / consistency mode。

例如：

- strict barrier；
- local consistency；
- eventual reconciliation；
- snapshot isolation；
- asynchronous relay。

---

# 27. Scheduling 是 Routing 的子集

$$
\boxed{
\text{Scheduling}
\subset
\text{Computational Routing}.
}
$$

Scheduling 主要處理：

- when；
- where；
- resource。

Routing 還要處理：

- how；
- which form；
- which law；
- which precision；
- which materialization；
- which consistency mode。

---

# 28. World-Family Computational Router

$$
\boxed{
\mathcal R_t^{WFC}
:
(
\mathfrak W_t^G,
D,
T,
B_t,
Risk_t,
\Gamma_t
)
\mapsto
\kappa_t.
}
$$

---

# 29. Router 不等 Executor

$$
\boxed{
\mathsf{Router}
\neq
\mathsf{Executor}.
}
$$

---

# 30. Router 不等 Governor

$$
\boxed{
\mathsf{Router}
\neq
\mathsf{Governor}.
}
$$

Governor 決定 admissibility。

Router 在 admissible space 中選方案。

---

# 31. Router 不等 Observer

$$
\boxed{
\mathsf{RouteCompute}
\neq
\mathsf{SelectObservation}.
}
$$

Paper 04 才正式處理 Observation Family。

---

# 32. Route 的輸入包含 World Mode

同一 computation 對：

$$
SIM
$$

與：

$$
AL
$$

可能採不同安全與 precision policy。

---

# 33. Pure Simulation 可以更激進

例如：

- speculative compute；
- destructive branch；
- rollback；
- coarse approximation；
- massive parallelism。

---

# 34. Reality-Coupled World 更嚴格

需要：

- version checks；
- freshness；
- authority；
- effect barriers；
- stronger validation。

---

# 35. Local Executor

對配置：

$$
\kappa_{ij,t},
$$

執行：

$$
\Delta_{ij}^{cand}
=
\Phi_{ij}^{f_{ij},\ell_{ij}}
(S_{ij},I_{ij}).
$$

---

# 36. Executor 先產生 Candidate

$$
\boxed{
\text{Execution Result}
=
\text{Candidate Delta}
}
$$

而不是直接 canonical mutation。

---

# 37. Candidate 不等 Commit

$$
\boxed{
Candidate
\neq
Commit.
}
$$

---

# 38. Candidate Store

所有：

$$
\Delta_{ij}^{cand}
$$

可以先進 candidate store。

---

# 39. Why Candidate First?

因為 local executor 不知道完整 global constraints。

---

# 40. Local Success 不等 Global Admissibility

$$
\boxed{
\text{Local Execution Success}
\not\Rightarrow
\text{Global Commit Admissibility}.
}
$$

---

# 41. Global Constraint Set

$$
\mathcal C_t^G
$$

可以包含：

- cross-domain dependencies；
- cross-world causal coupling；
- authority；
- invariants；
- budget；
- temporal ordering；
- evidence boundaries；
- version conditions；
- safety limits。

---

# 42. Global Reconciliation

$$
\boxed{
\mathsf{Reconcile}_G
\left(
\{\Delta_{ij}^{cand}\},
\mathcal C_t^G,
\mathfrak W_t^G,
H_t
\right)
}
$$

---

# 43. Reconcile 不等 Average

不同 candidates 衝突時，不是取平均。

---

# 44. Reconciliation Outcomes

可以是：

$$
\{
Accept,
Reject,
Defer,
Fork,
Retry,
Recompute,
Escalate
\}.
$$

---

# 45. Accept

candidate 可進指定 world commit。

---

# 46. Reject

candidate 不符合 contract。

---

# 47. Defer

等待 dependency / evidence。

---

# 48. Fork

如果兩個合法 candidate 不可同時合併，可以產生新 worlds。

---

# 49. Retry

同配置重試。

---

# 50. Recompute

改 computational form、precision 或 backend。

---

# 51. Escalate

交給：

- stronger solver；
- proof system；
- human；
- external validator。

---

# 52. World Commit 不等 Reality Actuation

$$
\boxed{
\text{World Commit}
\neq
\text{Reality Actuation}.
}
$$

simulation world commit 只改 simulation state。

---

# 53. Local Commit

$$
Commit_{W_i}.
$$

---

# 54. Cross-World Commit

如果同時更新多個 coupled worlds：

$$
Commit_{\{W_i,W_j\}}.
$$

需要更強 reconciliation。

---

# 55. Reality-Facing Commit

即使 actual-linked world 更新，

也不表示 physical effect 已發生。

---

# 56. Candidate / Commit Pipeline

$$
\boxed{
Resolve
\rightarrow
Route
\rightarrow
Execute
\rightarrow
Candidate
\rightarrow
Reconcile
\rightarrow
Commit
\rightarrow
Observe.
}
$$

---

# 57. WF-GCC

本文正式提出：

$$
\boxed{
\mathsf{WF\text{-}GCC}
=
\left\langle
Boundary,
Domains,
Configurations,
Dependencies,
Budgets,
CandidateDeltas,
Reconciliation,
Commit,
History,
Certificates
\right\rangle.
}
$$

---

# 58. Boundary

指定這次 global coherence 的範圍。

---

# 59. Domains

本次 active computational domains。

---

# 60. Configurations

每個 domain 的：

$$
\kappa_{ij,t}.
$$

---

# 61. Dependencies

跨 domain / world dependency graph。

---

# 62. Budgets

包含：

- compute；
- memory；
- energy；
- bandwidth；
- latency；
- token/model；
- human attention。

---

# 63. CandidateDeltas

未提交結果。

---

# 64. Reconciliation

全域一致性與衝突處理。

---

# 65. Commit

正式 world-state transition。

---

# 66. History

完整計算路徑。

---

# 67. Certificates

為何這條 route / commit 合法。

---

# 68. Finite Active Support

所有潛在可計算 pair：

$$
\mathcal U_t^{comp}.
$$

active support：

$$
\mathcal A_t^{comp}
\subseteq
\mathcal U_t^{comp}.
$$

---

# 69. Runtime 必須有限

$$
\boxed{
|\mathcal A_t^{comp}|<\infty.
}
$$

---

# 70. 但 Potential Space 可以擴張

$$
\mathcal U_{t+1}^{comp}
\supset
\mathcal U_t^{comp}
$$

可以成立。

---

# 71. 這不是矛盾

$$
\boxed{
\text{Finite Active Realization}
+
\text{Unbounded Extensibility}.
}
$$

---

# 72. Recursive Globality 不等 Recursive Full Expansion

nested worlds 可以存在，

但不要求：

$$
\boxed{
\text{expand every child world recursively}.
}
$$

---

# 73. Recursive Budget

對深度 $d$：

$$
B_d.
$$

可以隨深度下降。

---

# 74. World-Family Compute Budget

$$
B_t^{WF}
=
(
B_C,
B_M,
B_E,
B_L,
B_N
).
$$

概念上分別是 compute、memory、energy、latency、network budget。

---

# 75. Resource Allocation

$$
\sum_{(i,j)\in\mathcal A_t^{comp}}
b_{ij}
\leq
B_t^{WF}.
$$

---

# 76. Multi-Fidelity Computation

不同 worlds：

$$
q_i\neq q_j.
$$

---

# 77. Coarse-to-Fine

先：

$$
q_i^{low}
$$

篩選 world。

再對重要 world：

$$
q_i^{high}.
$$

---

# 78. Coarse Result 不得冒充 High-Fidelity Result

$$
\boxed{
\text{Coarse Simulation}
\neq
\text{High-Fidelity Validation}.
}
$$

---

# 79. Fidelity Escalation

$$
q_i^{low}
\rightarrow
q_i^{mid}
\rightarrow
q_i^{high}.
$$

---

# 80. Escalation Trigger

例如：

- decision sensitivity；
- risk；
- disagreement；
- uncertainty；
- counterexample；
- near-threshold result。

---

# 81. Four Resolution Fields

本文保留：

$$
\boxed{
\lambda^{compute}
\neq
\lambda^{observe}
\neq
\lambda^{carrier}
\neq
\lambda^{render}.
}
$$

---

# 82. Compute Resolution

系統實際算多細。

---

# 83. Observe Resolution

observer 需要看多細。

---

# 84. Carrier Resolution

載體可承載多細。

---

# 85. Render Resolution

最終顯示多細。

---

# 86. 高精度 Compute 可以低精度 Observe

例如 solver 算到：

$$
10^{-9}
$$

但人只需要：

$$
\text{safe / unsafe}.
$$

---

# 87. 低精度 Compute 不可假裝高精度 Observe

如果 underlying compute 很粗，

UI 不能用華麗視覺假裝精確。

---

# 88. Materialization 與 Computation 分離

某 dependency 可以存在於 canonical graph，

但不必 active materialize。

---

# 89. Retrieval 可以替代 Recomputation

如果：

$$
Result
$$

仍有效且 provenance compatible，

Router 可以選 retrieval。

---

# 90. Cache 不是 Truth

$$
\boxed{
\text{Cached Result}
\neq
\text{Currently Valid Result}.
}
$$

需要 version / dependency check。

---

# 91. Shadow Execution

高風險新 route 可以先：

$$
ShadowExecute.
$$

---

# 92. Shadow Result 不 Commit

$$
\boxed{
\text{Shadow Result}
\neq
\text{Canonical State}.
}
$$

---

# 93. Route Migration

若 backend 過載：

$$
r_a
\rightarrow
r_b.
$$

---

# 94. Backend Migration 不應改變 Semantic Contract

除非明示 approximate mode。

---

# 95. Heterogeneous Hardware 只是其中一層

CPU / GPU / FPGA / NPU heterogeneity 是：

$$
\mathfrak R^{exec}
$$

的異質性。

---

# 96. Semantic Heterogeneity 更上層

World family 還有：

- algorithm heterogeneity；
- transition-law heterogeneity；
- domain heterogeneity；
- precision heterogeneity；
- evidence-mode heterogeneity。

---

# 97. External Engineering Analogy

2026 task-based data-flow work 已顯示同一應用可以在統一 runtime 下協調 CUDA、SYCL、Triton、OpenMP 與 vendor libraries。

這支持：

$$
\boxed{
\text{heterogeneous execution can be coordinated without forcing one backend}.
}
$$

---

# 98. 但本文層級更高

該類 runtime 主要處理 device / API heterogeneity。

WCO Computation Layer 還要選：

- computational form；
- world；
- domain；
- law；
- precision；
- evidence contract。

---

# 99. Computing-Aware Routing 類比

2025 CaRCS 類工作已把：

$$
\text{routing}
+
\text{scheduling}
$$

聯合優化。

本文接受這個工程方向。

但 WCO routing 更偏 semantic computational routing。

---

# 100. Real-Time Constraint

某些 world/domain 有 deadline：

$$
T_{ij}^{exec}
\leq
T_{ij}^{deadline}.
$$

---

# 101. Deadline 會改變 Route

可能從高精度 solver 改為 bounded approximation。

---

# 102. Approximation 必須被標記

$$
\boxed{
\text{Approximate Result}
\neq
\text{Exact Result}.
}
$$

---

# 103. Compute Debt

本文定義：

$$
\boxed{
\mathbf D_{comp}
=
(
D_{approx},
D_{stale},
D_{route},
D_{sync},
D_{backend},
D_{budget},
D_{history}
).
}
$$

---

# 104. Approximation Debt

數值／模型近似造成。

---

# 105. Staleness Debt

依賴過期 state 或 cache。

---

# 106. Routing Debt

選擇 suboptimal / mismatched computational form。

---

# 107. Synchronization Debt

asynchronous regions 暫時不一致。

---

# 108. Backend Debt

backend-specific limitation。

---

# 109. Budget Debt

因資源限制未完成理想計算。

---

# 110. History Debt

關鍵 route / version / seed 未完整保存。

---

# 111. Computation History

本文定義：

$$
H_t^{comp}.
$$

至少保存：

- route；
- configuration；
- backend；
- versions；
- seed；
- inputs；
- candidate deltas；
- reconciliation；
- commit receipt；
- failure。

---

# 112. State Equality 不等 Computation-History Equality

$$
\boxed{
S_a=S_b
\not\Rightarrow
H_a^{comp}=H_b^{comp}.
}
$$

---

# 113. 為什麼歷史重要？

因為未來可達性可能受：

- hidden cache；
- learned state；
- random seeds；
- authority；
- provenance；
- irreversible external effects；

影響。

---

# 114. Noncommutative Computation

可能：

$$
\Phi_a\circ\Phi_b
\neq
\Phi_b\circ\Phi_a.
$$

---

# 115. 因此終點相同仍可能不是同一執行

$$
\boxed{
\text{Endpoint Equality}
\neq
\text{Execution Equivalence}.
}
$$

---

# 116. Computation Equivalence 需要 Task Specification

可定義：

$$
H_a^{comp}
\equiv_{\tau}
H_b^{comp}
$$

表示對 task $\tau$ 所需 invariants 等價。

---

# 117. Global Reconciliation 也要看 History

不能只比較 final values。

---

# 118. Cross-World Coupled Computation

某些 worlds 故意共享：

- random numbers；
- model；
- parameters；

以降低比較 variance。

---

# 119. Coupling 不等 Error

paired counterfactual simulation 可以合理共享 noise。

---

# 120. 但 Coupling 必須入 Ledger

否則會誤判 evidence independence。

---

# 121. Parallel Worlds 不等 Independent Worlds

$$
\boxed{
\text{Parallel Execution}
\neq
\text{Epistemic Independence}.
}
$$

---

# 122. Parallelism 是 Execution Property

independence 是 evidence / model property。

---

# 123. AIVS 接口

當 active compute regions 很多時，

中央 AI 不應收全部 raw trace。

---

# 124. Hierarchical Relay

$$
\boxed{
Worker
\rightarrow
Relay
\rightarrow
Governor.
}
$$

---

# 125. Vertical Synchronization

只上送：

- anomaly；
- summary；
- causal conflict；
- threshold crossing；
- commit request。

---

# 126. No Global Barrier by Default

$$
\boxed{
\text{Global Coherence}
\neq
\text{Global Barrier}.
}
$$

---

# 127. Consistency Mode 應 Task-Relative

有些 domain 需要 strict consistency。

有些可 eventual reconciliation。

---

# 128. Strong Consistency Cost

$$
C_{sync}^{strong}
$$

可能很高。

---

# 129. Weak Consistency Risk

$$
R_{sync}^{weak}
$$

可能增加 temporary conflict。

---

# 130. Router 應做 Trade-off

$$
\sigma^\ast
=
\operatorname*{arg\,min}_{\sigma}
\left(
C_{sync}+\lambda R_{sync}
\right).
$$

---

# 131. Multi-Objective Routing

一般不應假設單一 cost。

可定義：

$$
\mathbf J(\kappa)
=
(
Q,
Latency,
Energy,
Cost,
Risk,
Verifiability,
Reproducibility
).
$$

---

# 132. Pareto Frontier

選擇：

$$
\kappa
\in
\mathcal P_{\mathrm{Pareto}}.
$$

---

# 133. Policy 才做 Scalarization

只有在 policy 明確時：

$$
J_w
=
\sum_iw_iJ_i.
$$

---

# 134. Weight 需要 Governance

不能由 renderer 或 executor 偷偷決定。

---

# 135. Risk-Aware Routing

高風險：

$$
Risk\uparrow
$$

通常要求：

- stronger validation；
- higher precision；
- more provenance；
- stricter commit gate。

---

# 136. 但 Risk-Aware 不等一律最慢

低 latency 本身也可能是 safety requirement。

---

# 137. Value of Information

某 computation 是否值得繼續，可以看：

$$
VoI(\kappa).
$$

---

# 138. Stop 是正式動作

$$
\boxed{
\mathsf{Stop}
\in
\text{valid computation policy}.
}
$$

---

# 139. 不計算也是計算治理的一部分

如果：

$$
VoI<C_{compute},
$$

可以停止。

---

# 140. Replan

新 evidence 可以使 route：

$$
\kappa_t
\rightarrow
\kappa_{t+1}.
$$

---

# 141. Reframe

甚至 computational domain 本身可以改變：

$$
D_t
\rightarrow
D_{t+1}'.
$$

---

# 142. Global-Like AI 的計算智能

不只：

> 算得快。

更包括：

> 知道現在該算什麼、用什麼算、算到哪裡、何時停止、何時換方法。

---

# 143. Computational Routing Certificate

本文提出：

$$
\boxed{
\mathsf{RouteCert}
=
\left\langle
Task,
World,
Domain,
Configuration,
Alternatives,
Constraints,
Budget,
Risk,
Reason,
Version
\right\rangle.
}
$$

---

# 144. Candidate Certificate

$$
\mathsf{CandCert}
=
(
InputVersion,
RouteCert,
Executor,
Result,
Debt,
FailureState
).
$$

---

# 145. Reconciliation Certificate

$$
\mathsf{ReconCert}
=
(
CandidateSet,
Constraints,
Conflicts,
Resolution,
Accepted,
Rejected,
Deferred
).
$$

---

# 146. Commit Receipt

$$
\mathsf{CommitReceipt}
=
(
WorldId,
BeforeVersion,
AfterVersion,
AcceptedDelta,
Authority,
Timestamp,
HistoryRef
).
$$

---

# 147. Certificate-Carrying Computation

$$
\boxed{
\text{High-Risk Computation}
\rightarrow
\text{Result + Certificate}.
}
$$

---

# 148. Failure 也要結構化

$$
\mathsf{Failure}
=
(
Stage,
Reason,
MissingCondition,
Recoverability,
AffectedWorlds
).
$$

---

# 149. Failure 不等 Zero

不要用：

$$
0
$$

代表所有 failure。

---

# 150. Recovery Ladder

可以依序：

$$
Retry
\rightarrow
Reroute
\rightarrow
Recompute
\rightarrow
Rollback
\rightarrow
Compensate
\rightarrow
Escalate.
$$

---

# 151. Rollback 只對可回退 Computational State 成立

若已有 physical effect：

$$
\boxed{
\text{Compute Rollback}
\neq
\text{Reality Rollback}.
}
$$

---

# 152. World-Family Computation Loop

$$
\boxed{
\begin{aligned}
\mathfrak W_t^G
&\xrightarrow{\mathsf{Resolve}}
\mathcal D_t^{active}
\\
&\xrightarrow{\mathsf{Route}}
\{\kappa_{ij,t}\}
\\
&\xrightarrow{\mathsf{Execute}}
\{\Delta_{ij}^{cand}\}
\\
&\xrightarrow{\mathsf{Reconcile}}
\{\Delta^{acc},\Delta^{rej},\Delta^{def}\}
\\
&\xrightarrow{\mathsf{Commit}}
\mathfrak W_{t+1}^{G}
\\
&\xrightarrow{\mathsf{Observe}}
E_{t+1}.
\end{aligned}
}
$$

---

# 153. Observe 在最後不代表只能最後看

執行中也可以有 monitoring observations。

Paper 04 會細化。

---

# 154. Compute / Observe 分離仍保持

$$
\boxed{
\text{Monitoring Observation}
\neq
\text{Computation State itself}.
}
$$

---

# 155. Computation Layer 的 World-Family State

本文可寫：

$$
\boxed{
\mathfrak C_t^{WF}
=
\left\langle
\mathfrak W_t^G,
\mathcal D_t,
\mathfrak F_t^{comp},
\mathfrak L_t,
\Lambda_t^{comp},
\mathfrak R_t^{exec},
\mathfrak S_t,
\mathcal C_t^G,
\mathcal A_t^{comp},
H_t^{comp}
\right\rangle.
}
$$

---

# 156. $\Lambda_t^{comp}$

compute resolution / materialization field。

---

# 157. $\mathcal A_t^{comp}$

finite active computation support。

---

# 158. $H_t^{comp}$

computation history。

---

# 159. WCO Paper 01 的 $\mathfrak C_t$ 正式升級

Paper 01：

$$
\mathfrak C_t.
$$

Paper 03：

$$
\boxed{
\mathfrak C_t
\rightsquigarrow
\mathfrak C_t^{WF}.
}
$$

---

# 160. 計算層與世界層的接口

World Layer 提供：

- identity；
- mode；
- state；
- lineage；
- authority；
- evidence；
- lifecycle。

Computation Layer 不得繞過這些 contract。

---

# 161. 計算層不能自行創造 Authority

$$
\boxed{
\text{Compute Capability}
\neq
\text{Commit Authority}.
}
$$

---

# 162. 計算層不能自行升格 Evidence

$$
\boxed{
\text{Computed Result}
\neq
\text{Verified Evidence}.
}
$$

---

# 163. 計算層不能把 Branch 當 Reality

$$
\boxed{
SIM
\neq
AL
\neq
\mathcal R.
}
$$

---

# 164. 計算層不能把 Approximation 藏起來

$$
\boxed{
D_{approx}
\text{ must remain visible to later layers}.
}
$$

---

# 165. Computation Layer Constitution

本文提出十條：

1. Globality is boundary-relative.
2. Heterogeneity is allowed.
3. Routing is broader than scheduling.
4. Local success requires global reconciliation.
5. Candidate is not commit.
6. Finite active support is mandatory.
7. Resolution layers are separable.
8. History is first-class.
9. Certificates travel with high-risk computation.
10. Computation cannot create its own authority.

---

# 166. MVP：四世界、五種計算形態

使用 Paper 02 的：

$$
W_A,W_B,W_C,W_N.
$$

---

# 167. Computational Forms

提供：

1. deterministic simulator；
2. Monte Carlo；
3. graph analysis；
4. symbolic constraints；
5. learned surrogate model。

---

# 168. Router

根據：

- world mode；
- task；
- risk；
- budget；

選：

$$
f_i.
$$

---

# 169. Multi-Fidelity

每個 world 先 low fidelity。

---

# 170. Escalation

只有 top-risk / top-disagreement worlds 升級 high fidelity。

---

# 171. Candidate Store

所有結果先不 commit。

---

# 172. Reconciliation

檢查：

- shared resource；
- contradictory invariants；
- state version；
- world mode；
- evidence status。

---

# 173. Commit

更新 simulation worlds。

不觸發 reality action。

---

# 174. MVP Metrics

測：

- quality；
- compute；
- latency；
- energy；
- route accuracy；
- reroute rate；
- reconciliation conflicts；
- human intervention；
- certificate completeness。

---

# 175. 實驗一：One Form Everywhere vs Routed Heterogeneity

Baseline：

$$
f_i=f_0
$$

for all domains。

比較 dynamic routing。

---

# 176. 實驗二：Fixed Fidelity vs Adaptive Fidelity

比較：

$$
q_i=q_{max}
$$

與 coarse-to-fine。

---

# 177. 實驗三：Local Commit vs Global Reconciliation

測沒有 reconciliation 時的 cross-world / cross-domain conflict。

---

# 178. 實驗四：Schedule-only vs Computational Routing

控制相同 hardware budget。

比較只決定 when/where 與同時決定 how。

---

# 179. 實驗五：History-Aware vs Endpoint-Only

建立相同 endpoint、不同 route history 的 cases。

測後續 recovery / audit。

---

# 180. 實驗六：Strong Barrier vs AIVS

比較：

- global barrier；
- hierarchical relay；
- asynchronous reconciliation。

---

# 181. 實驗七：Cache Validity

故意使 upstream version 改變。

測 runtime 是否拒絕 stale cached result。

---

# 182. 實驗八：Route Failure Recovery

故意讓 backend 失效。

測：

$$
Retry
\rightarrow
Reroute
\rightarrow
Recompute.
$$

---

# 183. 實驗九：Risk-Aware Routing

高風險 world 與低風險 synthetic world 使用不同 validation level。

---

# 184. 實驗十：World-Family Scaling

逐步增加：

$$
|\mathfrak W|
$$

測 active support 是否維持 bounded。

---

# 185. 可反駁性

本文會被削弱，如果：

1. routed heterogeneity 在控制總 compute 後沒有穩定收益；
2. global reconciliation 在代表性 coupled tasks 中沒有降低 conflict；
3. finite active support 無法阻止 world-family scaling 的資源爆炸；
4. history preservation 對 recovery / audit 沒有價值；
5. route certificates 無法提高 reproducibility；
6. multi-fidelity routing 只增加 overhead；
7. simpler schedule-only runtime 在所有代表性 tasks 上同等有效。

---

# 186. 外部研究接口

2026 的 task-based data-flow methodology 已展示，一個應用可在 OmpSs-2 / OpenMP-style task graph 下協調 CUDA、SYCL、Triton、OpenMP offload 與 vendor libraries，並透過統一 threading/runtime 機制降低多 runtime 競爭。這證明 heterogeneous execution orchestration 已是現實工程問題。

2025 的 computing-aware routing / collaborative scheduling 工作也證明 routing 與 scheduling 可以被聯合建模，而非互相獨立。

2025 的 accelerator-based heterogeneous real-time scheduling survey 則顯示 deadline、energy、thermal constraints 與 heterogeneous device characteristics 本來就會改變 scheduler 的決策。

本文不宣稱取代上述研究。它在更高語義層追問：

> 如果除了 hardware heterogeneity，連 world、domain、computational form、transition law、precision、evidence mode 與 authority 都是可變項，AI runtime 應如何組合它們？

---

# 187. 本文不主張什麼

本文不主張：

1. 24/72 是完備的計算分類；
2. 存在單一普遍最優 routing policy；
3. 所有 task 都需要 heterogeneous computation；
4. AI 應取代 OS scheduler；
5. AI 應取代 compiler；
6. AI 應取代 numerical solver；
7. GPU 一定優於 CPU；
8. learned model 一定優於 symbolic solver；
9. global reconciliation 必須是 global barrier；
10. approximate compute 一定不安全；
11. strong consistency 一定更好；
12. more compute 一定提高 quality；
13. more worlds 一定需要更多 active compute；
14. parallel execution 等於 independent evidence；
15. endpoint equality 等於 history equality；
16. world commit 等於 reality actuation；
17. candidate result 等於 verified evidence；
18. routing layer 可以自行取得 authority；
19. WF-GCC 已完成 production implementation；
20. 本文取代 GCM、CDI/AIVS、PNCW、heterogeneous runtime literature 或 operating-system scheduling theory。

---

# 188. Computation Layer 核心非同一性

$$
\boxed{
\text{Computational Form}
\neq
\text{Projection Form}.
}
$$

$$
\boxed{
\text{Scheduling}
\subset
\text{Computational Routing}.
}
$$

$$
\boxed{
\text{Computation}
\neq
\text{Observation}.
}
$$

$$
\boxed{
\text{Global Dependency}
\neq
\text{Full Materialization}.
}
$$

$$
\boxed{
\text{Local Success}
\not\Rightarrow
\text{Global Commit}.
}
$$

$$
\boxed{
Candidate
\neq
Commit
\neq
RealityActuation.
}
$$

$$
\boxed{
\text{Parallel Execution}
\neq
\text{Epistemic Independence}.
}
$$

$$
\boxed{
\text{State Equality}
\not\Rightarrow
\text{Computation-History Equality}.
}
$$

---

# 189. 核心母式一：計算配置

$$
\boxed{
\kappa_{ij,t}
=
\left\langle
W_i,
D_{ij},
f_{ij},
\ell_{ij},
\lambda_{ij}^{comp},
r_{ij},
\tau_{ij},
q_{ij},
\sigma_{ij}
\right\rangle.
}
$$

---

# 190. 核心母式二：路由

$$
\boxed{
\mathcal R_t^{WFC}
:
(
\mathfrak W_t^G,
D,
T,
B_t,
Risk_t,
\Gamma_t
)
\mapsto
\kappa_t.
}
$$

---

# 191. 核心母式三：全域 Reconciliation

$$
\boxed{
\mathsf{Reconcile}_G
\left(
\{\Delta_{ij}^{cand}\},
\mathcal C_t^G,
\mathfrak W_t^G,
H_t
\right).
}
$$

---

# 192. 核心母式四：WF-GCC

$$
\boxed{
\mathsf{WF\text{-}GCC}
=
\left\langle
Boundary,
Domains,
Configurations,
Dependencies,
Budgets,
CandidateDeltas,
Reconciliation,
Commit,
History,
Certificates
\right\rangle.
}
$$

---

# 193. 核心母式五：有限活動計算

$$
\boxed{
\mathcal A_t^{comp}
\subseteq
\mathcal U_t^{comp},
\qquad
|\mathcal A_t^{comp}|<\infty.
}
$$

同時允許：

$$
\boxed{
\mathcal U_{t+1}^{comp}
\supset
\mathcal U_t^{comp}.
}
$$

---

# 194. 核心母式六：World-Family Computation Loop

$$
\boxed{
\begin{aligned}
\mathfrak W_t^G
&\xrightarrow{\mathsf{Resolve}}
\mathcal D_t^{active}
\\
&\xrightarrow{\mathsf{Route}}
\{\kappa_{ij,t}\}
\\
&\xrightarrow{\mathsf{Execute}}
\{\Delta_{ij}^{cand}\}
\\
&\xrightarrow{\mathsf{Reconcile}}
\{\Delta^{acc},\Delta^{rej},\Delta^{def}\}
\\
&\xrightarrow{\mathsf{Commit}}
\mathfrak W_{t+1}^{G}.
\end{aligned}
}
$$

---

# 195. 結論：類全域 AI 不只是「算得更多」，而是「知道世界族該怎麼被算」

普通 compute scheduler 問：

> 哪個 task 先跑？

heterogeneous scheduler 再問：

> 跑在哪個 CPU / GPU / accelerator？

類全域 AI 的 Computation Layer 還必須問：

> 這是哪一個 world？

> 哪一個 domain？

> 該使用哪一種 computational form？

> 該使用哪種 transition law？

> 要算到什麼 resolution？

> 是 exact、approximate、retrieval 還是 simulation？

> 是否值得先用 coarse solver？

> 是否可以 parallel？

> 是否需要 strict synchronization？

> 結果只能作 candidate，還是可以 local commit？

> 這些 local candidates 是否和其他 worlds 的 constraint 衝突？

> 這條 route 的 history、backend、seed、precision 和 approximation 有沒有被保存？

因此本文把全域計算重新濃縮為：

$$
\boxed{
\text{Global Computation}
=
\text{Route Heterogeneously}
+
\text{Execute Locally}
+
\text{Reconcile Globally}
+
\text{Commit Explicitly}.
}
$$

它不是一個巨大、同質、全同步的計算。

它是一個在受治理世界族中，依 task、world、domain、risk 與 budget 持續重配置的計算組合過程。

因此：

$$
\boxed{
\text{Global-Like AI computation is not one giant calculation.}
}
$$

而是：

$$
\boxed{
\text{a governed routing-and-reconciliation process
over heterogeneous computations distributed across a family of worlds}.
}
$$

Paper 01 的：

$$
\mathfrak C_t
$$

因此在本文正式升級為：

$$
\boxed{
\mathfrak C_t^{WF}.
}
$$

下一篇將轉向 WCO 三重族的第三個核心：

# Paper 04
## 觀察層：Global Observer 與 Observation Operator Family

也就是：

> **世界已經建立、計算也已經進行後，AI 到底應該看哪裡、看什麼、用什麼 observation operator，又如何開始自行發明自己的 computational way of seeing？**

---

# 196. 下一篇接口

Paper 04 將正式處理：

- observer identity；
- observer-relative slice；
- Global Observer；
- observation family；
- active observation；
- passive observation；
- internal / external observation；
- cross-world observation；
- observation accessibility；
- observation budget；
- observer-specific resolution；
- observation operator selection；
- AI-native observer emergence；
- computational way of seeing；
- observation debt；
- observation vs projection。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K × Aletheia，《從計算 24／72 範式到全域計算方法論：總綱與交接索引》v0.1，2026。
2. Neo.K × Aletheia，《全域計算方法論：異質計算的全域一致組合》v0.1，2026。
3. Neo.K × Aletheia，《計算形態空間：從 24 範式與 72 格動力學到可路由計算配置》v0.1，2026。
4. Neo.K × Aletheia，《動態計算路由：多域、多範式與異質轉移律的 Runtime 組合》v0.1，2026。
5. Neo.K × Aletheia，《計算不等於觀察：全域演化、局部物化與解析度相對計算》v0.1，2026。
6. Neo.K × Aletheia，《有限活動實現與無界計算展開》v0.1，2026。
7. Neo.K × Aletheia，《終點不等於歷史：非交換計算序列、世界狀態與可追溯全域演化》v0.1，2026。
8. Neo.K × Aletheia，《CDI / AIVS Series》，2026。
9. Neo.K × Aletheia，《PNCW Paper 05：全域計算、局部顯現》v0.1，2026。
10. Neo.K × Aletheia，《WCO Series Paper 01》v0.1，2026。
11. Neo.K × Aletheia，《WCO Series Paper 02：Governed World Family》v0.1，2026。
12. Neo.K × Aletheia，《SWFR Paper 02》v0.1，2026。

## External Research Interfaces

13. Boné, A., Aguirre, A., Álvarez, D., Martínez-Ferrer, P. J., & Beltran, V. (2026). *A task-based data-flow methodology for programming heterogeneous systems with multiple accelerator APIs*. Future Generation Computer Systems, 180, 108383.
14. Feng, L., Xie, R., Tang, Q., et al. (2025). *CaRCS: Joint Optimization of Computing-Aware Routing and Collaborative Scheduling in Computing Power Networks*. IEEE Network, 39(6), 270–278.
15. Zou, A., Xu, Y., Ni, Y., et al. (2025). *A Survey of Real-time Scheduling on Accelerator-based Heterogeneous Architecture for Time Critical Applications*. arXiv:2505.11970.
16. Bauer, M., Treichler, S., Slaughter, E., & Aiken, A. (2012). *Legion: Expressing Locality and Independence with Logical Regions*. SC '12.
17. Augonnet, C., Thibault, S., Namyst, R., & Wacrenier, P.-A. (2011). *StarPU: A Unified Platform for Task Scheduling on Heterogeneous Multicore Architectures*. Concurrency and Computation: Practice and Experience, 23(2), 187–198.

---

**Paper 03 狀態：COMPLETE v0.1**  
**下一篇：Paper 04 — 觀察層：Global Observer 與 Observation Operator Family**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
