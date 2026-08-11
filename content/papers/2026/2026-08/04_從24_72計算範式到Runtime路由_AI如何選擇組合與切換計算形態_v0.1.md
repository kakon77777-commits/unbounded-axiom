# 從 24／72 計算範式到 Runtime 路由
## AI 如何選擇、組合與切換計算形態

**English Title:** *From the 24/72 Computational Paradigms to Runtime Routing: How AI Can Select, Compose, and Switch Modes of Computation*  
**系列：**《計算域支配智能：AI 語義控制面與自適應多 X 計算》第 4 篇  
**系列代號：** CDI / AIVS  
**文件編號：** EML-CDI-04-PRR-2026-v0.1  
**作者：** Neo.K  
**協作整理：** Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-10  
**文件類型：** 計算架構理論論文／Runtime Routing 方法論／計算分類學工程化  
**證據成熟度：** E0–E1。24 重正式版提供相對分類核心，72 格仍是候選動力學擴展；本文提出的 Runtime Routing 層尚未完成工程 benchmark，不應被描述為既有 24／72 理論已自動證明的結果。

---

## 摘要

《計算的二十四重範式》正式版將一個指定語境中的計算事件分為三個軸：

$$
\mathfrak P_{24}
=
\mathfrak B_2
\times
\mathfrak U_4
\times
\mathfrak O_3,
$$

其中底空間為連續／離散，更新組織為序列、跳躍、並行、識別，觀察方式為連續、離散或拒單測。正式版並已明確允許混合系統以**範式路徑、範式分布與多層組合**表示，而非強迫整個系統落入單一格。

後續七十二格候選空間新增狀態轉移律：

$$
\mathfrak L_3
=
\{
\mathsf F,\mathsf K,\mathsf Q
\},
$$

分別代表函數型／確定型、古典機率核型與量子通道型轉移，形成：

$$
\mathfrak P_{72}^{(0.1)}
=
\mathfrak P_{24}
\times
\mathfrak L_3.
$$

但七十二格原論文本身也明確限制：它仍是候選空間，不宣稱 $\mathsf F,\mathsf K,\mathsf Q$ 已構成所有可能計算動力學的最終完備枚舉。

本文提出新的工程問題：

> **既然一個真實程式可以被表示為範式路徑，那麼這條路徑能否進一步成為 Runtime 的路由資訊？**

本文的回答是：可以作為**候選路由座標**，但不能把分類代碼直接等同於硬體。

因此：

$$
\boxed{
Paradigm
\neq
Backend.
}
$$

例如：

- $\mathsf P$ 表示並行更新，不等於「一定送 GPU」；
- $\mathsf R$ 表示識別／檢索型線上操作，不等於「一定送 NPU」；
- $\mathsf C/\mathsf D$ 是指定語境下的底空間／觀察型，不等於浮點／整數硬體；
- $\mathsf Q$ 描述量子通道型轉移，不表示普通電腦存在可直接使用的 QPU；
- $\mathsf X$ 是拒單測觀察，不是一種 accelerator。

本文因此在分類空間與執行硬體之間新增 **Paradigm Routing Layer（PRL）**：

$$
\boxed{
ParadigmProfile
\rightarrow
FeasibleRoutes
\rightarrow
CostedCandidates
\rightarrow
VerifiedRouteCommit.
}
$$

其核心路由函數為：

$$
\boxed{
\mathcal R:
(
P_i,
\Gamma_i,
D_i,
H_t,
Q_t,
E_t
)
\rightarrow
\Pi_i,
}
$$

其中：

- $P_i$ ：範式剖面；
- $\Gamma_i$ ：分類語境；
- $D_i$ ：依賴／因果圖；
- $H_t$ ：當下硬體與 backend 能力；
- $Q_t$ ：QoS、deadline、energy、correctness 需求；
- $E_t$ ：profiling、測試與 runtime evidence；
- $\Pi_i$ ：候選 Execution Plan。

本文提出 **Paradigm Profile、Paradigm Route Graph、Route Candidate、Route Commit、Paradigm Transition Event** 等工程物件，並把第三篇 Candidate/Commit 與第二篇 AIVS 直接接入路由層：

$$
\boxed{
ParadigmClassification
\rightarrow
RouteCandidate
\rightarrow
ShadowExecute
\rightarrow
Verify
\rightarrow
RouteCommit.
}
$$

AIVS 則在高價值範式切換處進行：

$$
StateSync+CausalSync+TopologySync+CommitSync.
$$

本文同時重新表述 24 正式版原有的自適應選擇公式，加入 backend 能力、切換成本、同步成本、風險與 AI 監督成本，建立 **Switching-Cost-Aware Runtime Objective**。如此，24／72 不再只是回答「這是什麼計算」，而開始提供：

> **這段計算有哪些合理的執行形態候選？在目前硬體、狀態、資源與證據下，哪一種值得被採用？**

本文不主張這個工程延伸已證實，也不主張 72 格是最終 routing ontology。相反，本文將 `unknown`、`hybrid`、`keep-original` 視為 Runtime 的必要安全狀態，並提出八組可反駁假說與一組源碼可見 MVP 路線。

---

## 關鍵詞

二十四重計算範式、七十二格計算動力學、Runtime Routing、計算域支配智能、CDI、AIVS、Paradigm Routing Layer、異質計算、Multi-X、MLIR、OpenMP、CUDA Graphs、Work Graphs、動態執行圖

---

# 0. 系列位置

前三篇已建立：

$$
\boxed{
SemanticControl
+
AIVS
+
CandidateCommit.
}
$$

第四篇加入：

$$
\boxed{
ParadigmRouting.
}
$$

因此：

$$
\boxed{
CDI
=
SemanticControl
+
AIVS
+
VerifiedCommit
+
ParadigmRouting
+
TraditionalComputeFabric.
}
$$

---

# 1. 原始 24 重範式到底定義了什麼？

正式版計算事件：

$$
\mathcal E=(X,F,Q;\Gamma)
$$

其中：

- $X$ ：狀態空間；
- $F$ ：狀態更新／存取；
- $Q$ ：觀察／輸出；
- $\Gamma$ ：觀察語境。

語境：

$$
\Gamma
=
(
\rho,
\mathcal M,
\boldsymbol\varepsilon,
\tau,
\mathcal Q
).
$$

這代表分類從一開始就不是無語境標籤。

所以：

$$
\boxed{
p_\Gamma(\mathcal E)
}
$$

才是完整語義。

---

# 2. 三個形態軸

底空間：

$$
\mathfrak B
=
\{\mathsf C,\mathsf D\}.
$$

更新組織：

$$
\mathfrak U
=
\{
\mathsf S,\mathsf J,\mathsf P,\mathsf R
\}.
$$

觀察：

$$
\mathfrak O
=
\{
\mathsf C,\mathsf D,\mathsf X
\}.
$$

因此：

$$
\boxed{
\mathfrak P_{24}
=
\mathfrak B
\times
\mathfrak U
\times
\mathfrak O.
}
$$

---

# 3. 第二軸是本篇最直接的 Routing 入口，但不能單獨決策

 $\mathsf S$ ：

$$
Sequential.
$$

 $\mathsf J$ ：

$$
Jump/Selective.
$$

 $\mathsf P$ ：

$$
Parallel.
$$

 $\mathsf R$ ：

$$
Recognition/Retrieval.
$$

這些確實與 execution organization 高度相關。

但：

$$
\boxed{
UpdateMode
\neq
HardwareTarget.
}
$$

---

# 4. 為什麼 $\mathsf P$ 不等於 GPU？

一個 parallel region 可能：

- task 很少；
- shared state 很多；
- branch divergence 很高；
- data transfer 很貴；
- latency deadline 很短。

因此：

$$
GPUCost
>
CPUThreadPoolCost
$$

完全可能。

所以：

$$
\boxed{
\mathsf P
\rightarrow
\{
CPUParallel,
GPU,
NPU,
RemoteWorkers,\ldots
\}
}
$$

只是 feasible candidate set。

---

# 5. 為什麼 $\mathsf R$ 不等於 NPU？

Recognition/Retrieval 的核心是：

> 主要成本已由預處理、訓練、編譯或建索引吸收，線上階段以識別、存取、匹配為主。

實際 backend 可能是：

- CPU hash table；
- B-tree；
- vector index；
- GPU ANN；
- NPU inference；
- RAM cache；
- SSD database。

因此：

$$
\boxed{
Paradigm
}
$$

描述計算形態。

$$
\boxed{
Backend
}
$$

描述物理／軟體執行資源。

二者之間需要路由層。

---

# 6. $\mathsf X$ 更不能直接當硬體標籤

 $\mathsf X$ 正式版表示：

> 在指定語境與容許表示類中，不存在一個單一表示能在容差內共同保留全部相關觀察不變量。

因此 Runtime 面對 $\mathsf X$ 更合理的行為可能是：

$$
\boxed{
MultiViewObservation.
}
$$

例如同時保存：

- latency；
- accuracy；
- topology；
- distribution；
- uncertainty。

而不是：

> 找一個 X accelerator。

---

# 7. 正式版已經允許混合路徑

對多層系統：

$$
\mathcal E
=
\mathcal E^{(1)}
\circ
\cdots
\circ
\mathcal E^{(m)}.
$$

範式表示為：

$$
\boxed{
\mathbf p(\mathcal E)
=
(
p_1,\ldots,p_m
).
}
$$

這正是 Runtime Routing 的理論入口。

---

# 8. 範式轉換原本就已被定義

正式版寫：

$$
T_{p\to q}:
\mathcal E_p
\mapsto
\mathcal E_q.
$$

其代價包括：

$$
\Delta\mathbf C
=
\mathbf C_\Gamma(\mathcal E_q)
-
\mathbf C_\Gamma(\mathcal E_p),
$$

以及表示損失與 interface cost。

本篇新增的不是「範式可以轉換」。

而是：

$$
\boxed{
\text{讓 Runtime 把範式轉換當成可執行路由候選。}
}
$$

---

# 9. 24 正式版甚至已有自適應選擇公式

原式：

$$
p^*
=
\arg\min_{p\in\mathfrak P_{24}}
\left[
\mathbf w\cdot\widehat{\mathbf C}_\Gamma(p)
+
\lambda L_{\mathrm{obs}}(p)
\right].
$$

本篇保留此精神，

但改造成 Runtime 版本：

$$
\boxed{
\pi^*
=
\arg\min_{\pi\in\mathcal F_i}
J(\pi\mid t).
}
$$

---

# 10. 七十二格增加了什麼？

第四軸：

$$
\mathfrak L_3
=
\{
\mathsf F,\mathsf K,\mathsf Q
\}.
$$

所以：

$$
\boxed{
p_{72}
=
\langle
B,U,O,L
\rangle.
}
$$

---

# 11. $\mathsf F$

函數型／確定型：

$$
x_{t+1}
=
F_t(x_t,u_t).
$$

給定 state 與 input，

後態唯一。

---

# 12. $\mathsf K$

古典機率核：

$$
x_{t+1}
\sim
K_t(\cdot\mid x_t,u_t).
$$

隨機不是自動等於誤差。

它可能是：

- Monte Carlo；
- sampling；
- exploration；
- annealing；
- stochastic simulation。

---

# 13. $\mathsf Q$

量子通道：

$$
\rho_{t+1}
=
\mathcal E_t(\rho_t).
$$

本篇最重要限制：

$$
\boxed{
\mathsf Q
\neq
\text{「現在就送量子電腦」}.
}
$$

如果當下沒有 QPU，

Runtime 可：

- 使用量子 simulator；
- 延遲；
- 拒絕；
- 保留 original route；
- 對允許退化的特定任務選擇古典 approximation。

但不能因為只有 CPU：

$$
\mathsf Q
\rightarrow
\mathsf K
$$

後還宣稱語義完全相同。

---

# 14. 72 格本身仍是 Candidate Space

這是本篇必須保留的原始限制。

因此 Runtime 不應只有：

$$
\{\mathsf F,\mathsf K,\mathsf Q\}.
$$

工程 sentinel 還需要：

```text
UNKNOWN
HYBRID
KEEP_ORIGINAL
UNSUPPORTED
```

注意：

這些不是理論上的：

$$
\text{第 73、74、75 格}.
$$

它們只是 Runtime 操作狀態。

---

# 15. 混合轉移律

原 72 稿已定義：

$$
\mathbf L(\mathcal E)
=
(L_0,L_1,\ldots,L_T).
$$

例如：

$$
\mathsf F
\rightarrow
\mathsf Q
\rightarrow
\mathsf K
\rightarrow
\mathsf F.
$$

所以：

$$
\boxed{
TransitionLaw
}
$$

也可以是 path。

---

# 16. 因此完整程式不是單一 72 格

若：

$$
Program
=
E_1\circ E_2\circ\cdots\circ E_n,
$$

更合理：

$$
\boxed{
\mathbf P_{72}(Program)
=
(
p_{72}(E_1),
\ldots,
p_{72}(E_n)
).
}
$$

---

# 17. Paradigm Profile

本文定義：

```yaml
paradigm_profile:
  profile_version: prl/0.1

  region_id:
  context:
    resolution:
    time_window:
    observation_family:
    error_budget:

  morphology:
    substrate: C | D
    update: S | J | P | R
    observation: C | D | X

  dynamics:
    transition_law: F | K | Q | HYBRID | UNKNOWN

  modifiers:
    reversible:
    side_effect_class:
    realtime:
    interaction:
    determinism_required:

  confidence:
    morphology:
    dynamics:

  evidence_refs:
```

---

# 18. Profile 必須保存 $\Gamma$

否則：

$$
\boxed{
LabelWithoutContext
}
$$

會失去正式版最重要的語義。

同一事件：

$$
p_{\Gamma_1}(\mathcal E)
\neq
p_{\Gamma_2}(\mathcal E)
$$

完全可能。

---

# 19. Paradigm Classifier

定義：

$$
\boxed{
\mathcal K:
(
E_i,\Gamma_i,Evidence
)
\rightarrow
Profile_i.
}
$$

分類來源可以：

1. deterministic static analysis；
2. compiler IR；
3. runtime trace；
4. profiler；
5. AI semantic analysis。

---

# 20. AI 不應單獨決定 Profile

優先：

$$
\boxed{
MachineEvidence
+
AIInterpretation.
}
$$

例如：

- loop dependence；
- task DAG；
- random source；
- API use；
- side-effect trace；

都應作 evidence。

---

# 21. Confidence

每個分類附：

$$
c_i\in[0,1].
$$

低信心：

$$
c_i<\theta
$$

則：

$$
UNKNOWN/KEEP\_ORIGINAL.
$$

---

# 22. Paradigm Routing Layer（PRL）

完整層次：

```text
Program / Runtime
        │
        ▼
Region Segmenter
        │
        ▼
Paradigm Classifier
        │
        ▼
Paradigm Profile
        │
        ▼
Feasibility Filter
        │
        ▼
Route Cost Model
        │
        ▼
Route Candidates
        │
        ▼
Shadow / Verify
        │
        ▼
Route Commit
        │
        ▼
Execution Backend
```

---

# 23. Routing 不等於 Classification

$$
\boxed{
Classification:
E_i\rightarrow P_i.
}
$$

$$
\boxed{
Routing:
(P_i,H_t,D_i,Q_t,E_t)
\rightarrow
ExecutionPlan_i.
}
$$

---

# 24. Hardware Capability State

定義：

$$
\boxed{
H_t
=
(
CPU,
GPU,
NPU,
Memory,
Bandwidth,
Remote,
Specialized
)_t.
}
$$

內容包括：

- availability；
- load；
- memory；
- queue depth；
- driver capability；
- power budget；
- latency；
- thermal state。

---

# 25. Backend Capability Descriptor

例如：

```yaml
backend:
  id: gpu0
  kind: GPU

  supports:
    parallel: true
    deterministic: conditional
    stochastic: true
    quantum: false

  limits:
    memory_mb:
    transfer_latency_us:
    queue_depth:

  current:
    utilization:
    memory_free:
    power_headroom:
```

---

# 26. Feasible Route Set

對 region $E_i$ ：

$$
\boxed{
\mathcal F_i
=
Feasible(
Profile_i,
Dependencies_i,
Capabilities_t,
Policies
).
}
$$

只有：

$$
\pi\in\mathcal F_i
$$

才進成本比較。

---

# 27. Feasible 不代表 Optimal

CPU serial：

可能可行。

CPU parallel：

可能可行。

GPU：

可能可行。

Remote：

也可能可行。

所以再估：

$$
J(\pi).
$$

---

# 28. Runtime Cost Objective

本文提出：

$$
\boxed{
J(\pi)
=
w_tT(\pi)
+
w_eE(\pi)
+
w_mM(\pi)
+
w_sS(\pi)
+
w_rR(\pi)
+
w_oO(\pi)
+
w_aA(\pi)
}
$$

其中：

- $T$ ：time / latency；
- $E$ ：energy；
- $M$ ：memory；
- $S$ ：switch/interface/synchronization cost；
- $R$ ：correctness / rollback risk；
- $O$ ：observation loss；
- $A$ ：AI supervision cost。

---

# 29. Observation Loss 不能丟掉

24 正式版已包含：

$$
L_{\mathrm{obs}}.
$$

例如把 $\mathsf X$ 系統強壓成單一 scalar，

效能可能更高，

但：

$$
ObservationLoss\uparrow.
$$

因此 routing objective 必須保留：

$$
\boxed{
Performance
\neq
OnlyObjective.
}
$$

---

# 30. Switching Cost

如果現在 route：

$$
\pi_t.
$$

考慮：

$$
\pi_{t+1},
$$

不能只看：

$$
Cost(\pi_{t+1}).
$$

而是：

$$
\boxed{
Cost_{switch}
(
\pi_t\rightarrow\pi_{t+1}
).
}
$$

---

# 31. Switching Cost 包含

- state transfer；
- memory copy；
- cache warmup；
- JIT / compilation；
- backend initialization；
- sync barrier；
- data format conversion；
- AI revalidation；
- pipeline stall。

---

# 32. 所以 Greedy Routing 會失敗

如果 GPU 目前快：

$$
CPU\rightarrow GPU.
$$

下一秒 CPU 快：

$$
GPU\rightarrow CPU.
$$

反覆切換：

$$
Thrashing.
$$

總體更慢。

---

# 33. Switching-Cost-Aware Objective

$$
\boxed{
\pi_{t+1}^{*}
=
\arg\min_{\pi\in\mathcal F}
\left[
J_t(\pi)
+
\eta
C_{switch}(\pi_t,\pi)
\right].
}
$$

---

# 34. Hysteresis

只有：

$$
Gain(\pi_{new})
>
\theta_{enter}
$$

才切換。

回原 route：

$$
Gain<\theta_{exit},
$$

其中：

$$
\theta_{exit}<\theta_{enter}.
$$

---

# 35. Minimum Dwell Time

新 route 至少保持：

$$
\tau_{\min}.
$$

除非：

- failure；
- safety；
- capability loss。

---

# 36. Paradigm Route Graph

定義：

$$
\boxed{
G_P=(V_P,E_P).
}
$$

節點：

$$
v
=
(
ParadigmProfile,
BackendProfile
).
$$

邊：

$$
e_{ij}
=
T_{i\to j}.
$$

---

# 37. Edge Cost

$$
\boxed{
c(e_{ij})
=
C_{convert}
+
C_{transfer}
+
C_{sync}
+
C_{warmup}
+
C_{risk}.
}
$$

---

# 38. 路由不是只選「下一個 backend」

還可以找：

$$
\boxed{
Path:
v_0\rightarrow v_1\rightarrow\cdots\rightarrow v_k.
}
$$

例如：

```text
CPU parse
→ GPU parallel transform
→ CPU deterministic commit
```

---

# 39. 這正好接回因果流

對 causal flow：

$$
F_j.
$$

可以附：

$$
\boxed{
RoutePath(F_j).
}
$$

所以：

$$
CausalFlow
+
ParadigmPath
+
BackendPath
$$

形成三層描述。

---

# 40. Causal Flow 回答

> 工作沿哪條因果幹道前進？

Paradigm Profile 回答：

> 這段計算以什麼形態與轉移律演化？

Backend Route 回答：

> 現在由哪個 execution fabric 執行？

三者不可混為一個標籤。

---

# 41. Multi-X 的正式位置

本文的 Multi-X 可以是：

$$
X\in
\{
CPU,
GPU,
NPU,
DSP,
Remote,
StorageCompute,
Specialized,
QPU/Simulator
\}.
$$

但是否存在、可用與合法：

$$
\boxed{
RuntimeCapabilityCheck.
}
$$

---

# 42. OpenMP 提供什麼相鄰 primitive？

OpenMP 的：

- `metadirective`；
- `declare variant`；
- `target`；

已經允許同一程式根據 context / target 使用不同 directive 或 function variant。

這證明：

$$
\boxed{
ContextDependentVariantSelection
}
$$

不是全新概念。

---

# 43. CDI 多出的問題

OpenMP context selector 是明確規範的 traits / implementation context。

CDI 希望再加入：

- semantic role；
- causal flow；
- runtime evidence；
- uncertainty；
- ACR cost；
- candidate/commit。

所以：

$$
\boxed{
CDI
}
$$

不是 OpenMP replacement。

---

# 44. MLIR Transform Dialect 提供什麼？

MLIR Transform Dialect 可以把：

$$
\boxed{
TransformationDescription
}
$$

與：

$$
\boxed{
PayloadIR
}
$$

分開，

並精確 target operation、串接 transformation。

這提供一個很好的工程方向：

> Paradigm Routing Policy 可以成為一層可檢查、可重播的 transformation / routing IR，而不是讓 LLM 直接修改 machine code。

---

# 45. Paradigm Routing IR

本文暫定：

```yaml
route_candidate:
  route_id:
  region_id:
  paradigm_profile_ref:

  from:
    backend:
    execution_mode:

  to:
    backend:
    execution_mode:

  transformation:
    passes:
    data_conversion:
    synchronization:

  predicted:
    latency:
    energy:
    memory:
    risk:
    ai_cost:

  validation:
    required_tests:
    shadow_epochs:
    equivalence_policy:

  fallback:
    route:
```

---

# 46. Route 是 Candidate

第三篇原則直接適用：

$$
\boxed{
RouteProposal
\neq
ActiveRoute.
}
$$

AI 說：

> 這段適合 GPU。

只產生：

$$
RouteCandidate.
$$

---

# 47. Shadow Route

第一步：

$$
Original
\parallel
ShadowNewRoute.
$$

Shadow：

$$
NoExternalCommit.
$$

比較：

- state；
- output；
- latency；
- energy；
- error。

---

# 48. Route Commit

只有：

$$
CorrectnessPass
\land
BenefitPass
\land
CapabilityCurrent
$$

才：

$$
\boxed{
CommitRoute.
}
$$

---

# 49. Route Receipt

```yaml
route_receipt:
  route_id:
  previous_route:
  active_route:
  state_epoch:
  topology_version:
  capability_version:
  benchmark_digest:
  committed_at:
```

---

# 50. Paradigm Transition Event

任何：

$$
p_i\rightarrow p_j
$$

或：

$$
Backend_i\rightarrow Backend_j
$$

應產生：

$$
\boxed{
ParadigmTransitionEvent.
}
$$

---

# 51. 為什麼 transition 是 AIVS 高價值同步點？

因為切換常涉及：

- state conversion；
- interface；
- new dependency；
- new timing；
- new failure mode。

所以：

$$
\boxed{
ParadigmTransition
\Rightarrow
AIVSSyncCandidate.
}
$$

---

# 52. Transition 前同步

至少：

$$
StateSync
+
CausalSync
+
CapabilitySync.
$$

---

# 53. Transition 後同步

至少：

$$
CommitSync
+
TopologySync.
$$

---

# 54. AI 不需要監控每次 kernel launch

AIVS 原則仍然是：

$$
\boxed{
RawRouteEvents
\gg
DeepAIInspection.
}
$$

穩定 route：

$$
R_0.
$$

切換、異常、未知：

$$
R_1/R_2.
$$

---

# 55. CUDA Graphs 提供什麼相鄰 primitive？

CUDA Graphs 可以將 workflow 表成 graph。

目前 CUDA Programming Guide 已支援：

- conditional IF；
- WHILE；
- SWITCH；
- device graph launch。

這意味著：

$$
\boxed{
DataDependentDynamicGraphExecution
}
$$

在 GPU 內部已經可以工程化。

---

# 56. CDI 並不需要讓 Governor 每次回 host

如果 route 已被驗證：

$$
\boxed{
Policy
}
$$

可以下沉到：

- graph conditional；
- task runtime；
- local Relay；
- device-side scheduler。

Governor 只監督 policy validity。

---

# 57. Direct3D 12 Work Graphs

Work Graphs 支援 GPU-based work creation。

因此遊戲／圖形工作負載中：

$$
\boxed{
GPUAutonomousWorkGeneration
}
$$

已是現成能力方向。

CDI 可做的是：

> 哪些高階工作應該被編譯成這樣的 graph？

而不是：

> AI 每一幀親自派每個 shader。

---

# 58. Vertical Compilation

本文提出一個暫定工程詞：

$$
\boxed{
VerticalCompilation.
}
$$

上層：

$$
Intent/Paradigm.
$$

中層：

$$
RoutingIR/TaskGraph.
$$

下層：

$$
BackendExecutable.
$$

---

# 59. Vertical Compilation 不等於 AIVS

AIVS：

$$
\boxed{
SynchronizeStateAcrossControlLayers.
}
$$

Vertical Compilation：

$$
\boxed{
LowerHighLevelRouteIntoExecutableForm.
}
$$

二者互補。

---

# 60. Static Routing

編譯期就決定：

$$
Route(E_i)=\pi_i.
$$

適合：

- 穩定 workload；
- source-visible；
- predictable hardware。

---

# 61. Profile-Guided Routing

先執行：

$$
Trace.
$$

再：

$$
UpdateRoute.
$$

適合：

- performance tuning；
- legacy code；
- game benchmark。

---

# 62. Runtime Adaptive Routing

當：

- load；
- device；
- deadline；
- state；
- topology；

變化，

才：

$$
Route_t
\rightarrow
Route_{t+1}.
$$

---

# 63. 三者不應一次全部做

第一個 MVP：

$$
\boxed{
Static/OfflineAdvisory.
}
$$

第二：

$$
ProfileGuidedShadow.
$$

最後才：

$$
RuntimeAdaptive.
$$

---

# 64. Unknown 是合法答案

如果 AI 看不懂：

$$
\boxed{
UNKNOWN.
}
$$

如果沒有安全收益證據：

$$
\boxed{
KEEP\_ORIGINAL.
}
$$

這兩個狀態是工程成熟度的重要指標。

---

# 65. 不能為了「用到 72 格」而過度分類

如果 region 是普通 deterministic CPU function：

$$
\boxed{
UseSimpleLabel.
}
$$

不要硬加入：

- 多餘量子；
- 多餘概率；
- 多餘 $\mathsf X$ 。

---

# 66. Minimum Sufficient Paradigm Description

承接 ACR：

$$
\boxed{
p_i^*
=
\arg\min_p
DescriptionCost(p)
}
$$

subject to：

$$
RoutingQuality(p)
\ge
Q_{\min}.
$$

---

# 67. 有時 24 就夠

如果：

$$
F/K/Q
$$

不影響 backend、verification 或 resource policy，

不必升級 72。

所以：

$$
\boxed{
24
\rightarrow
72
}
$$

也應該是 adaptive expansion。

---

# 68. 何時需要第四軸？

如果轉移律影響：

- determinism；
- reproducibility；
- sampling budget；
- simulator choice；
- verification；
- hardware capability；

則：

$$
\boxed{
ExpandTo72.
}
$$

---

# 69. 這就是「適度分類」

不是：

$$
MaximumOntology.
$$

而是：

$$
\boxed{
MinimumSufficientRoutingOntology.
}
$$

---

# 70. 路由策略層

可分：

## R0

rules：

```text
if update=P and region_size>threshold and gpu_available:
    candidate GPU
```

## R1

cost model / profiler。

## R2

AI semantic planner。

## R3

Governor cross-domain replanning。

---

# 71. R0 仍然不是硬編碼「P=GPU」

條件至少：

- data transfer；
- size；
- dependency；
- capability；
- effect class。

---

# 72. Example A：NPC 群體評估

Profile：

$$
\langle
\mathsf D;
\mathsf P;
\mathsf D;
\mathsf F
\rangle.
$$

可能 candidate：

- CPU task pool；
- GPU compute；
- SIMD CPU。

由 workload size 決定。

---

# 73. Example B：Asset Lookup

Profile：

$$
\langle
\mathsf D;
\mathsf R;
\mathsf D;
\mathsf F
\rangle.
$$

candidate：

- RAM hash/index；
- SSD index；
- cache；
- remote object store。

不需要 NPU。

---

# 74. Example C：Monte Carlo Simulation

Profile：

$$
\langle
\mathsf C/\mathsf D;
\mathsf P;
\mathsf C/\mathsf D;
\mathsf K
\rangle.
$$

candidate：

- CPU vectorized；
- GPU parallel sampling。

verification 必須保存：

- RNG seed/policy；
- sample count；
- confidence interval。

---

# 75. Example D：Audio DSP

可能：

$$
\langle
\mathsf C;
\mathsf P;
\mathsf C;
\mathsf F
\rangle.
$$

candidate：

- SIMD CPU；
- DSP；
- GPU。

但 real-time latency 常使：

$$
CPU/DSP
$$

優於 GPU transfer。

---

# 76. Example E：Q region

如果：

$$
L=\mathsf Q
$$

但：

$$
QPUAvailable=0,
$$

可能：

```text
route:
  quantum_simulator
```

或：

```text
UNSUPPORTED
```

而不是假裝轉移律不存在。

---

# 77. Example F：X Observation

若：

$$
O=\mathsf X,
$$

Runtime 可建立：

```yaml
observation_contract:
  preserve:
    - latency_distribution
    - correctness
    - topology
    - uncertainty
```

避免只優化單一 FPS / latency scalar。

---

# 78. 多目標 Pareto

路由通常沒有單一最優。

可能：

$$
\pi_A:
Fast+HighEnergy
$$

$$
\pi_B:
Slow+LowEnergy
$$

所以：

$$
\boxed{
ParetoSet
}
$$

可能比單一 route 更合理。

---

# 79. Policy 選擇 Pareto 點

Gaming：

$$
LatencyWeight\uparrow.
$$

Battery：

$$
EnergyWeight\uparrow.
$$

Server：

$$
ThroughputWeight\uparrow.
$$

Safety：

$$
RiskWeight\uparrow.
$$

---

# 80. AI 的真正價值

不是：

> AI 會比 compiler 更會算 cost。

而是：

> AI 可以把高階 goal、task semantics、risk、使用情境轉成 routing objective 與 constraints。

---

# 81. AI 仍不能偽造測量

Estimated speedup：

$$
\hat G.
$$

必須用：

$$
Profile/Benchmark
$$

校準。

---

# 82. Route Confidence

$$
\boxed{
C_{route}
=
f(
ClassifierConfidence,
ProfilerEvidence,
TestCoverage,
HistoricalStability
).
}
$$

---

# 83. Low Confidence Policy

$$
C_{route}<\theta
\Rightarrow
KEEP\_ORIGINAL.
$$

---

# 84. Route Provenance

任何 active route 都應回答：

- 誰提出？
- 哪個 profile？
- 哪個 profiler？
- 哪個 benchmark？
- 哪些 tests？
- 何時 commit？
- fallback 是什麼？

---

# 85. Route Reproducibility

相同：

$$
ProgramVersion
+
HardwareProfile
+
Policy
+
Trace
$$

應能重建：

$$
RouteDecision.
$$

若 AI decision 非 deterministic，

至少保留：

$$
DecisionReceipt.
$$

---

# 86. Route Drift

程式更新：

$$
v_1\rightarrow v_2.
$$

舊 route：

$$
\pi(v_1)
$$

不應自動信任於：

$$
v_2.
$$

---

# 87. Invalidate on Change

變更：

- code hash；
- dependency；
- driver；
- hardware；
- policy；

應：

$$
\boxed{
RouteRevalidation.
}
$$

---

# 88. Route Cache

已驗證的 stable profile：

$$
ProfileHash
\rightarrow
Route.
$$

可：

$$
Recognition/Retrieval.
$$

有趣的是：

Runtime 自己也可能把 routing 問題從：

$$
Search
$$

逐步轉成：

$$
\mathsf R.
$$

---

# 89. Meta-Paradigm

第一次遇到 region：

$$
Analyze.
$$

多次穩定後：

$$
RetrieveKnownRoute.
$$

因此：

$$
\boxed{
RoutingProcess
}
$$

本身也會發生範式轉換。

---

# 90. 這是 24 理論的反身工程用途

分類不只描述 workload，

也可以描述：

$$
\boxed{
Classifier/Router
}
$$

自己的工作方式。

---

# 91. Routing Thrashing

若 profile 在相鄰 class 間抖動：

$$
P_i
\leftrightarrow
P_j.
$$

可採：

- confidence hysteresis；
- minimum dwell；
- stable coarse class；
- delayed reclassification。

---

# 92. Coarse First Classification

先判：

$$
U:
S/J/P/R.
$$

如果已足夠 routing，

停止。

只有必要時才展開：

$$
B,O,L.
$$

這是 ACR 原則在 taxonomy 上的應用。

---

# 93. Progressive Paradigm Resolution

$$
\boxed{
U
\rightarrow
(B,U,O)
\rightarrow
(B,U,O,L)
\rightarrow
Modifiers.
}
$$

不是一次最大化分類。

---

# 94. 這可降低 AI Token

如果 80% region 只需：

> 序列／並行／檢索？

就能決策，

不需要每次讀完整 72 格理論。

---

# 95. Paradigm Index

Runtime 可以把分類編碼：

```text
U=P
B=D
O=D
L=F
```

而不是把整篇理論塞進 prompt。

---

# 96. AI 只需要 schema

這就是：

$$
\boxed{
Theory
\rightarrow
CompilerSchema.
}
$$

---

# 97. 第六篇需要的 Paradigm Registry

```text
paradigm_profiles
paradigm_evidence
backend_capabilities
route_candidates
route_edges
route_receipts
route_benchmarks
route_invalidations
transition_events
```

---

# 98. PRL API

```text
segment_region()
classify_profile()
expand_profile()
get_feasible_routes()
estimate_route_cost()
propose_route()
shadow_route()
verify_route()
commit_route()
invalidate_route()
fallback_route()
```

---

# 99. AIVS Hook API

```text
on_paradigm_transition()
sync_state()
sync_causal_parents()
sync_capability()
sync_topology()
ack_route_commit()
```

---

# 100. Candidate/Commit Hook

```text
create_route_candidate()
attach_route_evidence()
semantic_causal_fence()
commit_route_candidate()
write_route_receipt()
```

---

# 101. H1 — 24 Profile 可以穩定重建 workload 粗粒度形態

對 source-visible benchmark，

兩個獨立 classifier / reviewer：

$$
Agreement
\ge
Threshold.
$$

否則 Runtime 使用的 taxonomy 不夠可操作。

---

# 102. H2 — Progressive Resolution 比每次完整 72 分類便宜

比較：

- always-full；
- coarse-first。

在相同 routing quality 下：

$$
ClassificationCost_{coarse}<ClassificationCost_{full}.
$$

---

# 103. H3 — 72 第四軸在 stochastic workload 上增加路由資訊

對 Monte Carlo / sampling workload：

比較：

- 只看 24；
- 24 + $L$ 。

如果：

$$
RoutingQuality_{72}
\not>
RoutingQuality_{24},
$$

則第四軸對該 routing task 無額外工程價值。

---

# 104. H4 — Switching-Cost-Aware Policy 優於 Greedy

比較：

$$
GreedyBestNow
$$

與：

$$
CostAware.
$$

要求：

$$
TotalLatency/Energy
$$

至少一個目標改善，且 switch count 下降。

---

# 105. H5 — Shadow Route 阻止錯誤 AI 路由污染正式狀態

故意注入錯誤 route suggestion。

要求：

$$
InvalidActiveRouteRate
\approx0
$$

在 promotion gate 前。

---

# 106. H6 — AIVS transition sync 降低 stale route commit

在 route transition 注入：

- stale state；
- stale capability；
- stale topology。

比較：

with / without AIVS sync。

---

# 107. H7 — UNKNOWN / KEEP_ORIGINAL 降低低信心錯誤

要求：

$$
WrongOptimization
\downarrow
$$

代價是：

$$
MissedOptimization
\uparrow.
$$

評估 Pareto。

---

# 108. H8 — Paradigm-guided routing 能縮小 route search space

比較：

- exhaustive backend/mode combinations；
- profile-filtered feasible routes。

要求：

$$
SearchCost\downarrow
$$

且不排除 benchmark 中真正最佳 route 的比例低於門檻。

---

# 109. MVP A：Synthetic Region Classifier

建立：

- serial deterministic；
- parallel deterministic；
- selective；
- retrieval；
- stochastic；

五類 synthetic workloads。

輸出 Profile。

---

# 110. MVP B：Backend Feasibility

CPU / GPU 模擬兩種 backend。

依：

- transfer；
- work size；
- dependency；

產生 route candidate。

---

# 111. MVP C：Switch Cost

workload size 動態改變。

測：

- greedy；
- hysteresis；
- dwell；
- switching-cost-aware。

---

# 112. MVP D：Shadow Promotion

新 route 先 shadow：

$$
N
$$

epochs。

通過 equivalence + performance 才 active。

---

# 113. MVP E：24 vs 72

加入 stochastic workload。

測第四軸是否改善：

- reproducibility policy；
- backend choice；
- verifier choice。

---

# 114. MVP F：Route Cache

穩定 region：

第一次：

$$
Analyze.
$$

之後：

$$
ProfileHash\rightarrow Route.
$$

測 AI calls 是否下降。

---

# 115. MVP G：Capability Loss

GPU 中途 unavailable。

要求：

$$
AIVS
\rightarrow
FallbackCPU.
$$

正式 state 不污染。

---

# 116. MVP H：Unknown Profile

建立 taxonomy 模糊 workload。

要求：

$$
KEEP\_ORIGINAL,
$$

而不是強制路由。

---

# 117. 主要失敗模式

1. Paradigm misclassification；
2. Label/context loss；
3. 72 overfitting；
4. P=GPU shortcut；
5. R=NPU shortcut；
6. unsupported Q route；
7. switching thrash；
8. cost-model drift；
9. hardware capability stale；
10. route shadow 不充分；
11. AI over-routing；
12. global optimization 破壞 local invariant；
13. taxonomy 自己增加的 overhead 大於收益；
14. route cache stale；
15. observation loss 被 performance metric 掩蓋。

---

# 118. Safety Rule 1

$$
\boxed{
ParadigmLabel
}
$$

不能直接：

$$
\boxed{
CommitBackend.
}
$$

中間必須有：

$$
Feasibility+Cost+Verification.
$$

---

# 119. Safety Rule 2

$$
\boxed{
NoEvidence
\Rightarrow
NoRoutePromotion.
}
$$

---

# 120. Safety Rule 3

當 taxonomy 與現實衝突：

$$
\boxed{
RealityWins.
}
$$

也就是 profiler / test / invariant 高於理論標籤。

---

# 121. Safety Rule 4

七十二格未知：

$$
\boxed{
UnknownIsAllowed.
}
$$

---

# 122. Safety Rule 5

高風險 route change：

$$
ShadowFirst.
$$

---

# 123. 與第五篇的接口

本篇回答：

> **如果一段程式已能被分段與分類，Runtime 如何把分類轉成 execution route？**

第五篇將進一步回答：

> **對既有舊應用與遊戲，我們能不能真的取得這些 region、dependency、profile 與 route evidence？**

也就是：

# 《舊應用與遊戲的 AI 加速》
## 從實作串行化到必要串行化

---

# 124. 從理論到下一篇的具體問題

對一個老遊戲：

```text
Main Loop
→ Input
→ Script
→ NPC
→ Physics
→ Audio
→ Asset
→ Render Submit
```

我們要問：

1. 哪些 edge 是真正 data dependency？
2. 哪些只是歷史實作順序？
3. 哪些 region 可以取得 24／72 profile？
4. 哪些 route 只可 shadow？
5. 哪些副作用不可 rollback？
6. 哪些 workload 其實已經是 retrieval / parallel，但被 main loop 包住？
7. AI 能否找到安全的 `S → P`、`S → J` 或 `Search → R` 轉換候選？

---

# 125. 最終統一公式

本文把 24 正式版原本的：

$$
p^*
=
\arg\min_p
[
ResourceCost
+
ObservationLoss
]
$$

工程化成：

$$
\boxed{
\pi_{t+1}^{*}
=
\arg\min_{\pi\in\mathcal F(P,\Gamma,D,H,Q,E)}
\left[
J_t(\pi)
+
\eta C_{switch}(\pi_t,\pi)
\right].
}
$$

但：

$$
\pi^*
$$

仍只是候選。

真正 active route：

$$
\boxed{
ActiveRoute
=
Commit(
Verify(
Shadow(\pi^*)
)
).
}
$$

---

# 126. 結論

24／72 的工程價值，若要成立，不應建立在：

> 「有 24 或 72 格，所以每一格對應一個硬體。」

這種過度簡化上。

更合理的結構是：

$$
\boxed{
Taxonomy
\rightarrow
Profile
\rightarrow
FeasibleRouteSet
\rightarrow
MeasuredCandidates
\rightarrow
VerifiedCommit.
}
$$

24 回答：

$$
\boxed{
\text{在哪類底空間、以什麼更新組織、如何觀察？}
}
$$

72 再補問：

$$
\boxed{
\text{狀態依哪一類轉移律演化？}
}
$$

PRL 則新增：

$$
\boxed{
\text{在目前資源、依賴、目標與證據下，應如何執行？}
}
$$

因此：

$$
\boxed{
Paradigm
\neq
Backend,
}
$$

但：

$$
\boxed{
Paradigm
}
$$

可以成為：

$$
\boxed{
RoutingPrior.
}
$$

而不是 routing verdict。

AI 的價值就在這裡：它可以將高階程式語義、因果流、24／72 profile、當下硬體能力與 QoS 需求組合成候選 route；但真正的 route promotion 仍由 profiler、equivalence test、Candidate/Commit、AIVS 與 fallback 共同約束。

所以：

$$
\boxed{
24/72
}
$$

若從分類學進入 Runtime，

最合理的下一步不是：

> 「讓 AI 決定所有硬體。」

而是：

$$
\boxed{
\text{讓計算範式成為一種可驗證、可回退、可逐步學習的路由語言。}
}
$$

---

## 參考資料

### 內部研究線

1. Neo.K / Aletheia. 《計算的二十四重範式》正式版 v4.0，2026。
2. Neo.K / Aletheia. 《從二十四重計算形態學到七十二格計算動力學》，v0.1，2026。
3. Neo.K / Aletheia. 《AI 不必替代計算：從傳統執行平面到語義—因果控制平面》，v0.1，2026。
4. Neo.K / Aletheia. 《AI 垂直同步：分層中繼、認知比例性與低成本因果一致》，v0.1，2026。
5. Neo.K / Aletheia. 《候選不是提交：多 X 計算中的因果校正、錯位檢測與可恢復執行》，v0.1，2026。
6. Neo.K. 《從因果點到因果流：AI 視角計算的線性複雜度重構》，2026。
7. Neo.K / Aletheia. 《Adaptive Cognitive Runtime（ACR）工程白皮書》，v0.1，2026。

### 2026-08-10 重新查閱之公開 Primary Sources

8. LLVM / MLIR. *Transform Dialect* and *Transform Dialect Tutorial*, current documentation。
9. OpenMP Architecture Review Board. *OpenMP API Specification 6.0*；Metadirective, Declare Variant, Target Offload。
10. NVIDIA. *CUDA Programming Guide — CUDA Graphs*, current documentation；Conditional Nodes, Device Graph Launch。
11. NVIDIA. *CUDA Programming Guide — Programmatic Dependent Launch and Synchronization*, current documentation。
12. Microsoft. *Direct3D 12 Work Graphs*, current Windows Driver documentation。
13. Microsoft. *Direct3D 12 Linked GPU / Heterogeneous Multiadapter Sample*, current sample documentation。

---

## 版本紀錄

- **v0.1 / 2026-08-10**：建立 Paradigm Routing Layer、Paradigm Profile、Progressive Paradigm Resolution、Paradigm Route Graph、switch-cost-aware objective、Route Candidate/Shadow/Commit、AIVS transition sync、24/72 adaptive expansion、UNKNOWN/HYBRID operational states、8 組可反駁假說與第 6 篇工程 schema。
