# Paper 05 — Fresh Source Notes
## 2026-08-10

本篇依系列規則，開寫前重新查閱公開 primary sources。以下只整理其真正能支持的工程 primitive，不把它們寫成「已證明 CDI」。

---

# 1. Microsoft — Event Tracing for Windows (ETW)

Microsoft Learn 目前文件指出：

- ETW 是 Windows 的高效率 kernel-level tracing facility。
- 可記錄 kernel 或 application-defined events。
- event tracing 可動態 enable / disable，不必重新啟動 process / machine。
- consumer 可即時處理或從 log 讀取。
- ETW model 具有 Controller / Provider / Consumer。

對本文：

$$
WindowsEventPlane
$$

已成熟。

所以第 6 篇 Windows MVP 不必先寫 kernel profiler，可以直接從 ETW/WPR 開始。

---

# 2. Microsoft — Event Tracing Tools / WPR / WPA

2026-07 更新的 Microsoft Learn `Event Tracing Tools` 列出：

- WPR：以 predefined / custom profiles 擷取 ETW trace；
- WPA：分析 WPR/xperf 擷取的 ETW trace，支援 CPU、disk、memory、UI responsiveness；
- tracerpt；
- xperf；
- PerfView。

WPR 官方頁：

- WPR 基於 ETW；
- 收集 system / application events；
- WPA 用於後續分析。

WPA：

- 開啟 ETL；
- 以 graph / data table 分析。

對本文：

$$
ETL
\rightarrow
TraceReducer
\rightarrow
CDI
$$

是合理 MVP 路徑。

---

# 3. Microsoft PIX — Timing Capture

2026 Microsoft Learn 文件指出：

- PIX Timing Capture 將 CPU 與 GPU profiling data 放進同一 capture。
- 收集時 overhead 以低負擔為設計目標。
- 可觀察 work 如何分散到 CPU cores。
- 可觀察 CPU submit GPU work 到 GPU execution 的 latency。
- 可收集 file I/O、memory allocation、CPU samples、GPU timing、residency / counter 等。
- 透過 WinPixEventRuntime instrumentation 可加入 game-specific markers。

對本文：

Game performance evidence 不應只看 CPU profiler；
CPU / GPU / I/O timeline 對判定 bottleneck 很重要。

---

# 4. Visual Studio — Concurrency Visualizer

目前 Microsoft Learn 文件指出可以觀察：

- performance bottleneck；
- CPU underutilization；
- thread contention；
- cross-core migration；
- synchronization delays；
- DirectX activity；
- overlapped I/O。

Threads / Cores views 可連到 call stacks / source（若可用）。

對本文：

這些是「observed serialization」的 evidence，
但不是 parallel safety proof。

---

# 5. Intel VTune Profiler 2026

Intel 2026 User Guide：

- VTune 可 profile serial / multithreaded applications。
- platform 包括 CPU / GPU / FPGA。
- 可定位 hot functions。
- 可找 available processor time 使用不佳的位置。
- 可分析 synchronization object。
- 可判斷 CPU/GPU bound 與 offload effectiveness。

2026 Hotspots：

- 用於理解 application flow / hottest regions。
- sampling modes 包括 user-mode 與 hardware-event based。
- 文檔把 threading analysis 列為 parallel/multicore application 的後續分析之一。

Threading Analysis：

- 用於識別 processor core 利用效率與 synchronization/contention 問題。

對本文：

VTune 可作 external profiler evidence source。

---

# 6. Microsoft Research Detours

官方 GitHub / Wiki：

- Detours 用於 Windows API call monitoring / instrumentation。
- 可 intercept ARM/ARM64/x86/x64 binary functions。
- runtime 修改 target function entry 並建立 trampoline。
- 沒有 source 時可將 detour function 放在 DLL，於 process creation 注入。
- Microsoft README 明確定位為 monitoring / instrumenting API calls。

對本文：

能支持：

$$
BinaryBoundaryObservation.
$$

不能支持：

$$
ArbitraryBinaryParallelization.
$$

而官方 wiki 亦提醒 Microsoft 不保證被 detour 或其他方式修改的第三方程式。

所以 Paper 05 把 binary rewrite 留在 ResearchOnly / HighRisk。

---

# 7. Intel VTune / Microsoft profiler 的共同啟示

Profiler 可以告訴：

- 哪裡花時間；
- 哪裡等待；
- 哪裡 cores underutilized；
- 哪裡 synchronization；
- CPU/GPU 關係。

但：

$$
Hotspot
\not\Rightarrow
ParallelSafe.
$$

$$
IdleCore
\not\Rightarrow
ParallelizableWork.
$$

這是本文的重要方法論邊界。

---

# 8. 本篇與 MSSP Game Runtime 的接口

既有 MSSP Game Computer Runtime v0.8：

- continuous window capture；
- luma signature；
- temporal diff；
- structured events；
- idle/active FPS；
- bounded multimodal queue；
- action verification；
- audit。

它可作：

$$
VisualSemanticPlane.
$$

ETW / PIX / VTune 則作：

$$
PerformanceTracePlane.
$$

本篇提出未來把兩者時間／事件對齊，但尚未工程驗證。

---

# 9. 本篇新提出，不可誤寫成外部工具已有

- Serialization Gap：
  $G_S=ImplementationSerialization-NecessarySerialization$。
- L1/L2/L3 visibility policy。
- Legacy Acceleration Pipeline（LAP）。
- Serialization Finding schema。
- Evidence Ladder 與 automation authority coupling。
- Five Acceleration Channels。
- Sidecar Acceleration policy。
- Game Equivalence Contract（GEC）。
- Epoch Vector $(e_{sim},e_{render},e_{asset},e_{network})$。
- Acceleration Promotion Gate（APG）。
- Negative Optimization Memory。
- Visual Semantic Plane + Performance Trace Plane 的 CDI 結合。
- 12 組 legacy/game benchmark hypotheses。
