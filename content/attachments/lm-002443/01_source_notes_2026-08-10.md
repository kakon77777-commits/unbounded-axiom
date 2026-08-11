# Paper 01 — Fresh Source Notes
## 2026-08-10

本檔記錄第 1 篇開寫前重新檢索的公開技術資料。

---

## Microsoft — Windows Thread Pool / TaskScheduler

重新查閱：

- Windows Thread Pool 提供由系統管理的 worker thread pool。
- Windows 應用文件指出 thread pool 可利用多 CPU cores、平衡 thread resources。
- .NET `TaskScheduler` 預設提供 work-stealing、thread injection / retirement。
- 因此本系列不應把「OS 不會多核心排程」當成主張。
- 真正研究缺口應定位在高階 application semantics / causal dependency / adaptive routing。

---

## Microsoft — Direct3D 12 Work Graphs

重新查閱：

- Work Graphs 是 D3D12 GPU autonomy 機制。
- shader thread 可以要求其他工作執行。
- system 管理 task 間 data flow 的 scheduling 與 memory。
- Windows 11 24H2 / WDDM 3.2 開始提供相關支援。

對 CDI 的意義：

$$
\text{dynamic work graph}
$$

已是現實的硬體／driver primitive。

CDI 的新問題不是 work graph 是否存在，而是：

$$
AI
\rightarrow
HighLevelSemanticGraphPolicy.
$$

---

## LLVM Polly

重新查閱：

- Polly 是 LLVM polyhedral optimization infrastructure。
- 官方文件包含 automatic OpenMP code generation。
- 因此 automatic parallelization 不是本文新發明。

CDI 應定位為：

$$
CompilerDependence
+
AISemantics
+
RuntimeEvidence
+
AdaptiveSupervision.
$$

---

## Mikek et al. 2026
### Agentic Code Optimization via Compiler-LLM Cooperation

arXiv:2604.04238。

研究把：

- LLM optimization agents；
- compiler components；
- test generation agent；
- guiding LLM；

結合。

核心啟示：

- LLM 可補高階 optimization reasoning。
- LLM 生成可能錯誤，因此需要 compiler / testing cooperation。
- reported evaluation 中，相對 baseline 可取得性能改善，但不能外推到所有程式。

與 CDI 差異：

此工作主要是 code optimization pipeline。
CDI 更強調 runtime control plane / causal supervision / dynamic rerouting。

---

## Winston et al. 2026
### Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling

arXiv:2605.21470。

核心：

- task description compile into executable plan；
- JIT scheduler 探索 parallelization；
- invariant-enforcing protocol 使用 precondition / postcondition state；
- 目標同時處理 latency 與 correctness。

對 CDI 的意義：

支持：

$$
AIPlanning
+
InvariantGuardedExecution.
$$

但該研究是 web-agent workflow，不等於一般 CPU/GPU runtime 已被證明可同樣處理。

---

## Li et al. 2026
### FlowCompile

arXiv:2605.13647。

- 將 structured LLM workflows 視為 compilation 問題。
- profile sub-agents 與 workflow structure。
- 搜索 accuracy / latency trade-off configuration。

對本系列的意義：

可作 ACR / AIVS cost-aware configuration 的相鄰研究。

---

## 本篇自行提出、不可誤寫成既有文獻已證明

- Computational Domain Intelligence（CDI）統一模型。
- Execution Plane / Semantic Control Plane 的本文用法。
- `ImplementationSerialization - NecessarySerialization` 作為潛在平行化研究空間。
- Semantic Pre-Analysis → Causal Compute Graph。
- Green / Yellow / Red compute region。
- AI Relay / Governor 分層架構（後篇正式化）。
- 認知同步率 $\rho_c$。
- 24／72 範式作為 runtime routing coordinate。
- 舊遊戲／傳統應用作為 CDI benchmark。
