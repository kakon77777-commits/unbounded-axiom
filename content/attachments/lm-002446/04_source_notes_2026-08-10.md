# Paper 04 — Fresh Source Notes
## 2026-08-10

本篇依系列規則，開寫前重新檢索公開技術資料，並重新讀取 24 正式版與 72 候選空間原始文件。

---

# 一、內部來源：24 重正式版

《計算的二十四重範式_正式版_v4.0》目前正式主張：

$$
\mathfrak P_{24}
=
\mathfrak B
\times
\mathfrak U
\times
\mathfrak O
$$

- $\mathfrak B=\{C,D\}$：底空間；
- $\mathfrak U=\{S,J,P,R\}$：序列、跳躍／選擇、並行、識別／檢索；
- $\mathfrak O=\{C,D,X\}$：連續、離散、拒單測觀察。

重要修正與邊界：

- 分類依語境 $\Gamma$。
- 不再將範式與固定時間複雜度一一對應。
- 不主張宇宙絕對完備，只主張固定類型系統內相對閉合。
- 混合系統可用範式路徑、分布、堆疊表示。
- 原文已有範式轉換 $T_{p\to q}$。
- 轉換成本涉及資源差、表示損失、interface cost。
- 原文已有 task-oriented adaptive selection 的多目標公式。
- 研究議程亦包含自動標註器與範式轉換圖最短路徑／Pareto。

因此本篇的工程新增不是「第一次提出範式轉換」，而是：

$$
\text{把範式 Profile 接到 Runtime Execution Routing。}
$$

---

# 二、內部來源：72 格候選動力學

《從二十四重計算形態學到七十二格計算動力學_v0.1》提出第四軸：

$$
\mathfrak L_3=\{F,K,Q\}.
$$

分別：

- F：函數／確定轉移；
- K：古典機率核；
- Q：量子通道。

形成：

$$
\mathfrak P_{72}^{(0.1)}
=
\mathfrak P_{24}
\times
\mathfrak L_3.
$$

原文重要限制：

- 72 是 candidate space。
- 不宣稱 F/K/Q 已絕對完備。
- 仍需研究三軸獨立性、空格、退化格、混合量子—古典系統。
- 實際系統可使用 transition-law path：
  $F\rightarrow Q\rightarrow K\rightarrow F$。
- 分層系統應使用多個 $p_{72}$ 組合，而非單一標籤。
- v0.2 研究計畫原本就包括「轉移律判定器」。
- 原文要求保持 24 編號不變，72 作附加碼，而非破壞舊分類。

因此本文 Runtime 使用 `UNKNOWN/HYBRID/KEEP_ORIGINAL` 只是操作 sentinel，不是新增理論格。

---

# 三、LLVM / MLIR — Transform Dialect

2026-08-10 重新查閱官方 MLIR 文件：

- Transform Dialect 提供 declarative specification 來控制 compiler transformations。
- 可以精確 target payload IR 中的 operations。
- transformation 可以 chain。
- transformation description 與被 transformation 的 payload IR 可以分離。

對 CDI/PRL 的啟示：

Routing policy / transformation plan 最好變成可檢查的 IR／descriptor，
而不是讓 LLM 直接任意 patch machine code。

本文不宣稱 MLIR 已有 24/72 Paradigm Routing。

---

# 四、OpenMP 6.0

官方 OpenMP 6.0 Specification 與 reference：

- `metadirective` 支援依 OpenMP context 選擇 directive variant。
- `declare variant` 支援依 context 選擇 function variant。
- `target` / `declare target` 支援 device offload。
- 既有版本也明確提供 runtime target offload control。

對本篇：

$$
ContextDependentVariantSelection
$$

與：

$$
TargetOffload
$$

早已存在。

本篇新增的是把：

- task semantics；
- 24/72 profile；
- runtime evidence；
- causal flow；
- AIVS；
- Candidate/Commit；

放進更高階路由控制面。

---

# 五、NVIDIA CUDA Graphs

目前官方 Programming Guide：

- CUDA Graphs 將 workflow 表為 graph。
- conditional graph node 支援 IF / WHILE / SWITCH。
- condition 可在 dependency 滿足後於 device 端評估。
- device graph launch 允許 device 端發起 graph，支援 dynamic control flow／device-side scheduler 類 workload。
- device graph 的結構有嚴格限制，並非任意動態程式圖。

對 CDI：

已驗證、穩定的 routing policy 可下沉成 graph/runtime primitive，
中央 AI 不必逐個 kernel 派工。

---

# 六、CUDA Programmatic Dependent Launch

官方 CUDA Programming Guide 亦提供 Programmatic Dependent Launch / synchronization，
可以在 graph edge 表達 programmatic dependency 類型。

對本篇：

dependency-aware launch 已有硬體/runtime primitive；
CDI 要解的是上層 semantic dependency 與 routing policy。

---

# 七、Microsoft Direct3D 12 Work Graphs

Microsoft 官方文件：

- Work Graphs 是 Direct3D 12 的 GPU autonomy 機制。
- 允許 GPU-based work creation。
- driver/interface 管理 work graph capability tier。
- DirectX Samples 已有對應範例。

對遊戲：

動態 work graph 已有現成 GPU 路線。

CDI/PRL 的問題是：

> 哪些舊 main-loop 工作可以被安全地重構、編譯或 offload 成這類 graph？

---

# 八、Microsoft D3D12 Heterogeneous / Linked GPU Sample

官方 sample 說明：

- 多 GPU 情況下 CPU 仍需針對 GPU node 提交 work。
- resources 需用 node mask 正確對應 GPU。
- Microsoft DirectX Graphics Samples 包含 heterogeneous multiadapter 範例。

對 PRL：

multi-X hardware 本身存在 capability / resource affinity。
Paradigm label 不能跳過 backend capability 與 data locality。

---

# 九、本篇新提出，不能誤寫成外部文獻已有

- Paradigm Routing Layer（PRL）。
- `Paradigm != Backend` 作為 CDI routing 邊界。
- Paradigm Profile schema。
- Progressive Paradigm Resolution。
- Minimum Sufficient Routing Ontology。
- Paradigm Route Graph。
- Paradigm + Causal Flow + Backend Path 三層結構。
- Route Candidate / Shadow / Commit 與 Paper 03 的整合。
- Paradigm Transition Event 作為 AIVS 高價值 sync point。
- UNKNOWN / HYBRID / KEEP_ORIGINAL operational sentinel。
- 24 → 72 的 adaptive expansion。
- Vertical Compilation（本文暫定工程詞）。
