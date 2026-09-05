# GCM × ADRO 統合架構論文

## 從全域計算意圖到物理資源實體化：GCM 與 ADRO/UHRM 的統一計算架構

**English subtitle:** From Global Computation Intent to Physical Resource Materialization: A Unified Architecture for GCM and ADRO/UHRM

版本：v0.1  
日期：2026-08-30  
定位：Integration Hypothesis / Canonical Bridge Architecture  
狀態：概念統合完成；不代表兩套 Runtime 已正式合併或 production-integrated

---

## 摘要

Global Computation Methodology（GCM）與 AI-Native Dynamic Resource Orchestrator / Unified Heterogeneous Resource Model（ADRO/UHRM）原本從不同問題出發。

GCM 處理的是：

> 一個計算目標在全域上如何被描述、分解、約束、驗證、路由與配置？

ADRO/UHRM 處理的是：

> 當一個工作已經被描述後，它在當下可觀測、可授權、可定價、可遷移的 CPU、GPU、NPU、memory、storage、network、DPU、fabric 與 energy 資源上，應如何被實體配置與執行？

兩者因此不是同一層系統，也不應被過早合併成單一 Runtime。然而，它們之間存在天然的上下游關係。

本文提出：

$$
\boxed{
\text{GCM}
=
\text{Global Computation Semantics and Decision Layer}
}
$$

以及：

$$
\boxed{
\text{ADRO/UHRM}
=
\text{Physical Resource Materialization and Orchestration Layer}
}
$$

兩者透過一個 canonical bridge 形成：

$$
\boxed{
\text{GCM Intent}
\rightarrow
\text{Bridge Contract}
\rightarrow
\text{ADRO Materialization}
\rightarrow
\text{Physical Execution}
\rightarrow
\text{Observed Result}
\rightarrow
\text{GCM History / Replanning}
}
$$

本文將此統合模型稱為：

$$
\boxed{
\text{Unified Computation Materialization Architecture}
}
$$

簡稱 UCMA。

UCMA 不要求 GCM 與 ADRO 成為同一 repository，也不要求兩者共享內部 state machine。相反地，本文主張應保留兩者的分層自治，只在橋接層交換 canonical、versioned、auditable contracts。

核心不變量為：

$$
\boxed{
\text{Computation Semantics}
\neq
\text{Physical Resource State}
}
$$

$$
\boxed{
\text{AI Proposal}
\neq
\text{Authority}
}
$$

$$
\boxed{
\text{Global Feasibility}
\neq
\text{Current Materializability}
}
$$

$$
\boxed{
\text{Materialization Failure}
\neq
\text{Computation Invalidity}
}
$$

因此，一個在 GCM 中語義有效的計算，可能因當前資源、budget、policy、data locality 或 hardware availability 而暫時無法 materialize；反過來，ADRO 看見大量可用 GPU，也不代表它有權自行創造新的全域計算目標。

本文提出雙向 bridge contract、狀態映射、錯誤分類、authority invariants 與最小 Integration Adapter MVP，作為兩套系統未來成熟後正式進入更高層 AI-native computation stack 的基礎。

---

# 1. 問題的重新定義

傳統計算系統常隱含：

$$
\text{Program}
\rightarrow
\text{Machine}
\rightarrow
\text{Result}
$$

但 AI-native computation 使這條鏈變得不充分。

因為一個高層目標可能先被 AI 分解成多種可行計算形式：

$$
\mathcal{W}
=
\{
w_1,w_2,\ldots,w_n
\}
$$

每個工作又具有：

- semantic dependency；
- quality requirement；
- execution authority；
- resource requirement；
- cost constraint；
- data locality；
- alternative computation path。

因此真正完整的鏈條更接近：

$$
\text{Intent}
\rightarrow
\text{Computation Semantics}
\rightarrow
\text{Validated Work Graph}
\rightarrow
\text{Physical Materialization}
\rightarrow
\text{Execution}
\rightarrow
\text{Observation}
\rightarrow
\text{Replanning}
$$

GCM 與 ADRO 正好分別覆蓋這條鏈的不同區域。

---

# 2. GCM 的層級定位

本文將 GCM 抽象為：

$$
\mathfrak{G}
=
(
I,
W,
C,
P,
A,
V,
H
)
$$

其中：

$$
I=\text{Computation Intent}
$$

$$
W=\text{Global Work / Computation Graph}
$$

$$
C=\text{Constraints}
$$

$$
P=\text{Candidate Computation Paths}
$$

$$
A=\text{Allocation / Decision Semantics}
$$

$$
V=\text{Validation}
$$

$$
H=\text{History / Provenance}
$$

GCM 的核心問題不是：

> 現在 GPU 0 有多少記憶體？

而是：

> 在既定目標與約束下，哪些計算路徑是合法、可驗證、可組合的？

因此：

$$
\boxed{
\text{GCM operates primarily in the computation-decision space.}
}
$$

---

# 3. ADRO/UHRM 的層級定位

ADRO/UHRM 可表示為：

$$
\mathfrak{A}
=
(
R,
G_R,
W',
K,
B,
P_R,
\Pi,
\Omega,
H_R
)
$$

其中：

$$
R=\text{Observed Resources}
$$

$$
G_R=\text{Resource Topology}
$$

$$
W'=\text{Materializable Workload Representation}
$$

$$
K=\text{Resource Contracts}
$$

$$
B=\text{Budget}
$$

$$
P_R=\text{Resource Policies}
$$

$$
\Pi=\text{Placement / Execution Plans}
$$

$$
\Omega=\text{Runtime State}
$$

$$
H_R=\text{Resource History}
$$

ADRO 的核心問題是：

> 在此時此刻的實際 hardware/resource state 下，工作應如何安全 materialize？

因此：

$$
\boxed{
\text{ADRO operates primarily in the machine-resource state space.}
}
$$

---

# 4. 兩者不是重複，而是正交

GCM 與 ADRO 同時談：

- allocation；
- constraint；
- planning；
- history。

但這不表示兩者重複。

因為它們的 domain 不同。

GCM 的 allocation：

$$
A_G:
\text{Computation Requirement}
\rightarrow
\text{Computation Form / Path}
$$

ADRO 的 allocation：

$$
A_R:
\text{Materializable Work}
\rightarrow
\text{Physical Resource}
$$

因此：

$$
\boxed{
A_G
\neq
A_R
}
$$

兩者的關係較接近：

$$
A_G
\rightarrow
A_R
$$

---

# 5. 核心分工

最簡化可以寫成：

$$
\boxed{
\text{GCM asks: What computation should exist?}
}
$$

$$
\boxed{
\text{ADRO asks: Where and how should it physically run now?}
}
$$

GCM 決定：

- 是否需要計算；
- 哪些計算 path 合法；
- 哪些 dependency 必須滿足；
- 哪些 result 有效；
- 哪些 global constraint 不可違反。

ADRO 決定：

- CPU/GPU/NPU placement；
- memory/storage tier；
- local/cluster/remote；
- budget；
- data movement；
- resize；
- migration；
- resource release。

---

# 6. Unified Computation Materialization Architecture

本文提出：

$$
\mathfrak{U}_{UCMA}
=
(
\mathfrak{G},
\mathfrak{B},
\mathfrak{A},
\mathfrak{O}
)
$$

其中：

- $\mathfrak{G}$：GCM；
- $\mathfrak{B}$：Bridge；
- $\mathfrak{A}$：ADRO/UHRM；
- $\mathfrak{O}$：Observation / feedback。

完整流程：

$$
\boxed{
GCM
\rightarrow
Bridge
\rightarrow
ADRO
\rightarrow
Physical Runtime
\rightarrow
Observation
\rightarrow
Bridge
\rightarrow
GCM
}
$$

---

# 7. Forward Bridge

GCM 向 ADRO 輸出：

$$
B_{GA}
=
(
intent,
work\_graph,
constraints,
authority,
quality,
deadline,
budget,
locality,
alternatives
)
$$

這裡最重要的是：

$$
\boxed{
B_{GA}
\text{ is declarative, not executable.}
}
$$

也就是 Bridge 不傳：

> 執行 `/bin/foo --bar`。

而傳：

> 需要完成某種 computation，且具有這組 constraints。

---

# 8. GCM Intent 到 ADRO TaskDescriptor

映射：

$$
\phi:
B_{GA}
\rightarrow
\mathcal{W}_{ADRO}
$$

例如 GCM 工作：

$$
w_1
=
\text{high-parallel numerical stage}
$$

可映射為：

$$
compute\_requirement
=
\{
class:gpu,
minimum\_capacity:x
\}
$$

GCM 的：

$$
deadline
$$

直接映射 ADRO：

$$
TaskDescriptor.deadline
$$

GCM 的：

$$
budget
$$

映射：

$$
IntentConstraint.budget
$$

GCM 的：

$$
data\_residency
$$

映射：

$$
policy\_constraints.data\_must\_remain\_local
$$

---

# 9. Authority Bridge

兩邊共同的不變量：

$$
\boxed{
\text{AI Proposal}
\neq
\text{Authority}
}
$$

因此：

$$
Authority_{ADRO}
\subseteq
Authority_{Bridge}
\subseteq
Authority_{GCM}
$$

Bridge 不得擴張 authority。

形式上：

$$
\boxed{
\mathcal{A}_{out}
\subseteq
\mathcal{A}_{in}
}
$$

任何：

$$
\mathcal{A}_{out}
\supset
\mathcal{A}_{in}
$$

都屬於 contract violation。

---

# 10. Budget Bridge

GCM 可能有 global budget：

$$
B_G
$$

ADRO 具有 machine / provider cost：

$$
C_R
$$

必須：

$$
C_R
\le
B_G
$$

若 GCM 工作圖有：

$$
n
$$

個節點，不能把：

$$
B_G
$$

複製給每個 node。

因此 Bridge 必須保持：

$$
\boxed{
\sum_i C_i
\le
B_G
}
$$

這和 ADRO Phase 9 的 graph-level budget semantics 一致。

---

# 11. Quality Bridge

GCM 的 quality requirement：

$$
Q_G
$$

可對應到 ADRO：

- hardware class；
- deadline；
- precision；
- latency；
- degradation policy。

但 ADRO 不應自行降低：

$$
Q_G
$$

若資源不足：

$$
\boxed{
\text{Defer / Reject / Request Replanning}
}
$$

而不是：

$$
\text{Silently Degrade}
$$

---

# 12. Materialization

ADRO 接受 bridge output 後觀察：

$$
\mathcal{R}(t)
$$

並求：

$$
\pi_t:
\mathcal{W}
\rightarrow
\mathcal{R}(t)
$$

例如：

$$
w_1\rightarrow GPU
$$

$$
w_2\rightarrow CPU
$$

$$
w_3\rightarrow SSD/Memory
$$

此時產生：

$$
M_t
=
\text{Materialization Plan}
$$

---

# 13. Global Feasibility 與 Materializability

定義：

$$
F_G(W)
=
\text{Globally Valid Computation}
$$

以及：

$$
F_R(W,t)
=
\text{Currently Materializable}
$$

可能存在：

$$
F_G(W)=\mathrm{true}
$$

但：

$$
F_R(W,t)=\mathrm{false}
$$

例如：

- 沒有足夠 GPU；
- budget 不足；
- cloud forbidden；
- storage unavailable；
- deadline 無法滿足。

因此：

$$
\boxed{
\text{Materialization Failure}
\neq
\text{Computation Invalidity}
}
$$

ADRO 應把結果回傳 GCM：

$$
\text{REPLAN_REQUIRED}
$$

而不是直接宣告 computation 不成立。

---

# 14. Reverse Bridge

ADRO 回傳：

$$
B_{AG}
=
(
status,
placement,
cost,
latency,
resource\_state,
execution\_result,
failure,
history,
provenance
)
$$

GCM 可以據此：

- 接受結果；
- 更換 computation path；
- 放寬 soft constraint；
- 延後；
- 重新分解工作；
- 終止。

因此：

$$
\boxed{
\text{Execution Feedback Becomes Computation Evidence}
}
$$

---

# 15. Feedback Loop

完整閉環：

$$
I_0
\rightarrow
W_0
\rightarrow
M_0
\rightarrow
O_0
\rightarrow
W_1
\rightarrow
M_1
\rightarrow
O_1
\rightarrow\cdots
$$

其中：

$$
W_{t+1}
=
F_G(W_t,O_t)
$$

而：

$$
M_t
=
F_A(W_t,R_t)
$$

因此：

$$
\boxed{
GCM
\text{ updates computation;}
\quad
ADRO
\text{ updates materialization.}
}
$$

---

# 16. History 的雙層分離

GCM History：

$$
H_G
$$

主要保存：

- computation decisions；
- semantic validation；
- path selection；
- result provenance。

ADRO History：

$$
H_R
$$

主要保存：

- resource state；
- placement；
- completion time；
- cost；
- failures；
- migration；
- learning outcomes。

因此：

$$
\boxed{
H_G
\neq
H_R
}
$$

但可透過：

$$
BridgeEventID
$$

建立 cross-reference。

---

# 17. Learning 的責任邊界

ADRO Phase 7 可以從：

$$
H_R
$$

學習 placement。

GCM 未來也可能從：

$$
H_G
$$

學習 computation path。

但：

$$
\boxed{
\text{Resource Learning}
\neq
\text{Computation Learning}
}
$$

ADRO 不應因 GPU 歷史表現很好，就自己發明：

> 這個問題應該改成另一種 computation。

那是 GCM 層責任。

---

# 18. Resize 與 GCM

ADRO 可以：

$$
2GPU
\rightarrow
8GPU
$$

但 resize 不改 computation semantics。

因此：

$$
\boxed{
\text{Resource Resize}
\neq
\text{Computation Rewrite}
}
$$

如果工作需要從：

$$
algorithm_A
$$

改：

$$
algorithm_B
$$

才能繼續，

則必須回 GCM replanning。

---

# 19. Migration 與 GCM

ADRO Phase 6 能處理：

$$
\text{checkpoint}
\rightarrow
\text{restore}
\rightarrow
\text{migration}
$$

但若：

$$
replay\_safety=uncertain
$$

則：

$$
migration=\mathrm{false}
$$

GCM 不能因「全域上還需要這個結果」就要求 ADRO blind replay。

因此：

$$
\boxed{
\text{Global Need}
\neq
\text{Replay Authority}
}
$$

---

# 20. Cluster / Fabric 層

GCM 不需要知道：

- Kubernetes ResourceClaim；
- Slurm partition；
- CXL Fabric Manager；
- DPUService CRD。

這些由 ADRO adapter 處理。

因此：

$$
\boxed{
\text{GCM}
\not\rightarrow
\text{Vendor API}
}
$$

而是：

$$
\boxed{
\text{GCM}
\rightarrow
\text{Canonical Bridge}
\rightarrow
\text{ADRO Adapter}
\rightarrow
\text{Vendor / Runtime Interface}
}
$$

---

# 21. Why Not Merge Repositories Yet

現在不應直接：

$$
Repo_{GCM}
+
Repo_{ADRO}
\rightarrow
Repo_{Unified}
$$

原因有四個。

## 21.1 不同演化速度

GCM 偏 semantic / methodology。

ADRO 偏 resource/runtime。

## 21.2 不同 validation

GCM 需要 computation correctness。

ADRO 需要 runtime/resource correctness。

## 21.3 不同 failure domain

GCM path error 與 hardware/resource failure 不同。

## 21.4 可獨立使用

ADRO 可以不依賴 GCM。

GCM 也可以對其他 runtime backend。

因此：

$$
\boxed{
\text{Integration by Contract}
>
\text{Integration by Codebase Fusion}
}
$$

至少在目前階段如此。

---

# 22. Bridge Adapter

最小 adapter：

$$
\mathfrak{B}
=
(
\phi,
\psi,
V_B,
H_B
)
$$

其中：

$$
\phi:
GCM\rightarrow ADRO
$$

$$
\psi:
ADRO\rightarrow GCM
$$

$$
V_B=\text{Bridge Validation}
$$

$$
H_B=\text{Bridge Event History}
$$

---

# 23. 最小 Forward API

可以先只有：

`translate_gcm_workload`

輸入：

$$
GCMWorkSpec
$$

輸出：

$$
ADROIntentEnvelope
$$

與：

$$
ADROTaskDescriptors
$$

`validate_bridge_contract`

檢查：

- authority non-expansion；
- budget preservation；
- deadline；
- quality；
- locality；
- unsupported semantics。

---

# 24. 最小 Reverse API

`translate_adro_result`

輸入：

$$
ADROPlanResult
$$

輸出：

$$
GCMObservation
$$

內容：

- materialized；
- deferred；
- rejected；
- completed；
- failed；
- reconciliation required。

---

# 25. Canonical Status Mapping

GCM → ADRO：

| GCM State | ADRO Meaning |
|---|---|
| COMPUTABLE | eligible for materialization |
| DEFERRED | do not materialize yet |
| FORBIDDEN | reject |
| REPLAN_REQUIRED | return to GCM |
| VALIDATED | computation semantics accepted |

ADRO → GCM：

| ADRO State | GCM Meaning |
|---|---|
| accepted | materializable |
| deferred | globally valid but temporarily unavailable |
| rejected | current contract cannot materialize |
| completed | execution observation available |
| reconciliation_required | result/state cannot yet be trusted as final |

---

# 26. Error Taxonomy

需要至少區分：

$$
E_G=\text{GCM Semantic Error}
$$

$$
E_B=\text{Bridge Translation Error}
$$

$$
E_R=\text{Resource Materialization Error}
$$

$$
E_X=\text{Execution Error}
$$

$$
E_O=\text{Observation / State Uncertainty}
$$

禁止把所有 failure 都回成：

> computation failed。

因為：

$$
\boxed{
\text{Failure Classification Determines Replanning Strategy}
}
$$

---

# 27. GCM × ADRO Integration MVP

第一版不需要真的整合全部 Phase C / v1.0 ADRO。

只做：

## Step 1

定義：

`GCMWorkSpec`

## Step 2

定義：

`GCMToADROBridgeContract`

## Step 3

轉：

$$
GCMWorkSpec
\rightarrow
IntentEnvelope
$$

## Step 4

呼叫 ADRO：

$$
plan\_intent
$$

## Step 5

轉：

$$
AdvisoryBundle
\rightarrow
GCMObservation
$$

全程：

$$
execute=\mathrm{false}
$$

---

# 28. Integration MVP 的成功條件

至少驗證：

## Case 1

GCM valid + ADRO materializable：

$$
\rightarrow accepted
$$

## Case 2

GCM valid + no resources：

$$
\rightarrow deferred
$$

## Case 3

GCM valid + budget too low：

$$
\rightarrow rejected/replan
$$

## Case 4

GCM forbidden：

ADRO 不應收到 executable workload。

## Case 5

Bridge authority expansion：

$$
\rightarrow \mathrm{FAIL}
$$

## Case 6

ADRO result state uncertain：

GCM 不得當成 final result。

---

# 29. 未來更完整的 Stack

長期可以形成：

$$
\boxed{
\text{Intent Layer}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{GCM Computation Layer}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{GCM-ADRO Bridge}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{ADRO/UHRM Materialization Layer}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OS / Cluster / Fabric / Provider}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Physical Hardware}
}
$$

---

# 30. AI-Native Computation Stack

本文最終提出：

$$
\boxed{
\text{AI-Native Computation}
=
\text{Semantic Computation Reasoning}
+
\text{Deterministic Governance}
+
\text{Physical Resource Materialization}
+
\text{Observed Feedback}
}
$$

缺少任何一層都不完整。

只有 reasoning：

$$
\rightarrow
\text{No Reliable Execution}
$$

只有 resource scheduler：

$$
\rightarrow
\text{No Global Computation Semantics}
$$

只有 execution：

$$
\rightarrow
\text{No Governance}
$$

只有 history：

$$
\rightarrow
\text{No Action}
$$

---

# 31. 共同不變量

GCM 與 ADRO 最重要的共同結構不是 API，而是不變量。

第一：

$$
\boxed{
\text{AI Proposal}
\neq
\text{Authority}
}
$$

第二：

$$
\boxed{
\text{Plan}
\neq
\text{Execution}
}
$$

第三：

$$
\boxed{
\text{Observation}
\neq
\text{Truth Without Validation}
}
$$

第四：

$$
\boxed{
\text{Capability}
\neq
\text{Permission}
}
$$

第五：

$$
\boxed{
\text{Failure}
\neq
\text{Invalidity}
}
$$

這些共同不變量使兩個系統能自然拼接。

---

# 32. 更一般的統一命題

若把 computation 表示為：

$$
\mathcal{C}
$$

資源表示為：

$$
\mathcal{R}(t)
$$

則 AI-native 系統需要建立：

$$
\mu_t:
\mathcal{C}
\rightarrow
\mathcal{R}(t)
$$

但：

$$
\mu_t
$$

不能直接由單一 AI model 任意決定。

它必須滿足：

$$
\mu_t
\in
Feasible
(
Semantics,
Authority,
Policy,
Budget,
Resources
)
$$

因此：

$$
\boxed{
\text{AI-Native Computing}
=
\text{Constrained Dynamic Materialization of Valid Computation}
}
$$

---

# 33. 與傳統 Compiler / Scheduler 的差異

傳統 compiler：

$$
Program
\rightarrow
MachineCode
$$

傳統 scheduler：

$$
Process
\rightarrow
CPU
$$

UCMA：

$$
\boxed{
\text{Intent}
\rightarrow
\text{Validated Computation Graph}
\rightarrow
\text{Dynamic Heterogeneous Resource Graph}
\rightarrow
\text{Audited Execution}
}
$$

其變化不只是規模增加，而是：

- computation graph 本身可動態重構；
- resource graph 本身也時變；
- authority/budget 進入 mapping；
- result 回流 computation layer。

---

# 34. Why This Matters for AI

AI 特別適合此架構，因為 AI workload 自身就具有：

- dynamic task generation；
- heterogeneous compute；
- large memory demand；
- data locality；
- long-running execution；
- adaptive replanning。

所以：

$$
\boxed{
\text{Static Program}
+
\text{Static Machine}
}
$$

逐漸被：

$$
\boxed{
\text{Dynamic Computation}
+
\text{Dynamic Resource State}
}
$$

取代。

GCM 與 ADRO 分別處理兩個 dynamic axis。

---

# 35. Epistemic Status

本文不是證明：

> GCM + ADRO 已經形成完整通用 AI 計算平台。

目前最多可主張：

1. 兩者抽象層具有清楚可組合關係；
2. bridge contract 可以形式化；
3. authority invariants 相容；
4. ADRO 已具備 materialization runtime 的 reference implementation；
5. GCM 已具備 computation orchestration 的工程基礎；
6. 真正跨系統 integration 尚需獨立 MVP 驗證。

因此本文狀態為：

$$
\boxed{
\text{Architecture Convergence Hypothesis}
}
$$

而不是：

$$
\boxed{
\text{Production Integration Proof}
}
$$

---

# 36. 未來正式合併條件

只有在至少滿足以下條件後，才值得考慮更高程度的 formal integration。

## GCM side

- canonical computation contract 穩定；
- allocator / planning semantics 穩定；
- failure classification 穩定；
- history/provenance 穩定。

## ADRO side

- resource contract 穩定；
- real provider/runtime adapters 成熟；
- migration/recovery 經實體驗證；
- budget/authority productionized。

## Bridge side

- versioned schema；
- property tests；
- replay tests；
- fault-injection；
- cross-runtime provenance。

因此：

$$
\boxed{
\text{Maturity First, Fusion Later}
}
$$

---

# 37. 結論

GCM 與 ADRO/UHRM 並不是兩個偶然相似的系統。

它們實際上分別回答 AI-native computation 的兩個不同核心問題：

$$
\boxed{
\text{What computation should exist?}
}
$$

與：

$$
\boxed{
\text{How should that computation physically exist now?}
}
$$

GCM 處理：

$$
\text{Computation Possibility Space}
$$

ADRO 處理：

$$
\text{Resource Materialization Space}
$$

Bridge 則建立：

$$
\boxed{
\text{Computation}
\leftrightarrow
\text{Physical Reality}
}
$$

的可驗證映射。

因此完整統一架構可以表示為：

$$
\boxed{
\text{Intent}
\rightarrow
\text{GCM}
\rightarrow
\text{Bridge}
\rightarrow
\text{ADRO/UHRM}
\rightarrow
\text{Physical Execution}
\rightarrow
\text{Observation}
\rightarrow
\text{GCM Replanning}
}
$$

本文最終命題為：

$$
\boxed{
\text{AI-native computation is not merely the generation of computation;}
}
$$

$$
\boxed{
\text{it is the governed materialization of valid computation into a changing physical resource world.}
}
$$

GCM 描述「有效計算」。

ADRO 描述「可用物理世界」。

兩者之間的 Bridge，才使 AI 原生計算從：

$$
\text{Reasoning}
$$

真正走向：

$$
\boxed{
\text{Reasoning}
+
\text{Materialization}
+
\text{Execution}
+
\text{Feedback}
}
$$

的完整閉環。

現階段最合理的工程策略不是合併兩個 repository，而是先保留：

$$
\boxed{
GCM
\rightarrow
ADRO\ Adapter
\rightarrow
ADRO/UHRM
}
$$

等兩邊都更成熟後，再決定是否在更高層 Runtime、平台或產品中正式合一。
