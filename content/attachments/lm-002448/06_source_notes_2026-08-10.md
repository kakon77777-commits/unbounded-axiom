# Paper 06 — Fresh Source Notes
## 2026-08-10

本篇開寫前重新核對公開 primary sources，並讀取目前 `mssp-game-computer-runtime-mvp` 專案資訊。

---

## Microsoft — ETW

Official:
https://learn.microsoft.com/en-us/windows/win32/etw/about-event-tracing

2026-07-17 更新文件說明：

- ETW 是 efficient kernel-level tracing facility。
- 可記錄 kernel/application-defined events。
- provider 註冊後，controller 可 enable/disable tracing。
- consumer 可讀多個 tracing sessions。

CDI 使用位置：Windows Evidence Plane。

---

## Microsoft — Event Tracing Tools / WPR / WPA

Official:
https://learn.microsoft.com/en-us/windows/win32/etw/event-tracing-tools

文件目前列：

- WPR：以 predefined/custom profiles 擷取 ETW。
- WPA：visualize/analyze WPR/xperf traces。

WPR CLI:
https://learn.microsoft.com/en-us/windows-hardware/test/wpt/wpr-command-line-options

官方語法包含：

```text
wpr -start <profile> ... -filemode
```

與 stop/merge/cancel。

---

## Microsoft — WPA Exporter

Official:
https://learn.microsoft.com/en-us/windows-hardware/test/wpt/exporter

WPA Exporter 是 command-line automated analysis 工具，
可從一個 ETL trace + WPA profile 匯出 tables 至 CSV。

官方語法：

```text
wpaexporter.exe -i traceFile.etl -profile profile.wpaProfile ...
```

這使 CDI v0.1 可以：

```text
ETL → WPA Exporter → CSV → Normalized Event
```

而不必先重寫 native ETW consumer。

---

## Microsoft — PIX Timing Captures

Official:
https://learn.microsoft.com/en-us/windows/win32/direct3dtools/pix/articles/timing-captures/pix-timing-captures

目前文件指出：

- Timing Capture 結合 CPU + GPU profiling。
- 可看 work 如何分布到 CPU cores。
- 可看 CPU submit 與 GPU execution 的 latency。
- 可收 file I/O、memory allocation、CPU samples、GPU timings 等。
- WinPixEventRuntime markers 可增加 game-specific semantic markers。

CDI 使用位置：
Game PerformanceTracePlane。

---

## SQLite — Atomic Commit / WAL

Official:
https://sqlite.org/atomiccommit.html
https://sqlite.org/wal.html

- SQLite 提供 transaction atomic commit/rollback。
- WAL 將 write-ahead log 作為 transaction mechanism。
- CDI v0.1 使用 SQLite 作 control-plane persistence，不作 raw telemetry warehouse。

---

## MLIR — Transform Dialect

Official:
https://mlir.llvm.org/docs/Dialects/Transform/
https://mlir.llvm.org/docs/Tutorials/transform/

Transform Dialect 將 transformation description 與 payload IR 分離，並提供可組合 transformation infrastructure。

CDI 的 Route/Transformation IR 與此只有工程相鄰性；本文沒有宣稱 MLIR 已實作 24/72 PRL。

---

## Microsoft Research — Detours

Official GitHub:
https://github.com/microsoft/Detours

Detours 定位是 monitoring / instrumenting API calls on Windows。

因此：

```text
CanIntercept != CanParallelizeSafely
```

CDI v0.1 的 binary adapter 只允許 observer boundary。

---

## User project — MSSP Game Computer Runtime

Repository:
https://github.com/kakon77777-commits/mssp-game-computer-runtime-mvp

讀取目前 `pyproject.toml`：

- project version `0.8.0`
- Python `>=3.11`
- MIT
- zero declared runtime dependencies
- CLI:
  - `mssp-game-computer`
  - `mssp-game-control`

README 現有能力包括：

- continuous vision loop
- luma signature / temporal diff
- structured events
- bounded multimodal inference
- live control plane
- DMS JSONL audit
- RDR evidence / authorization

CDI v0.1 因此也採 Python 3.11+ / stdlib-only，方便未來 local bridge。

---

# 本篇實際生成並測試的內容

Synthetic MVP:
`src/cdi_runtime_mvp.py`

Smoke:
`tests/smoke_test.py`

Result:
`tests/MVP_SMOKE_TEST.json`

PASS assertions：

- AIVS R0 / ESCALATE
- valid commit
- non-conflicting stale-version commit
- relevant conflict reject
- idempotent duplicate commit
- stale fencing reject
- irreversible speculative effect reject
- equivalent faster shadow route promote
- non-equivalent faster route reject
- serialization gap

不應把上述 synthetic PASS 說成：

- Windows ETW ingestion 已完成
- real game acceleration 已完成
- AI router 已驗證
