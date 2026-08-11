# LOCAL AI HANDOFF — CDI Runtime + AIVS v0.1

你接手的是《計算域支配智能：AI 語義控制面與自適應多 X 計算》6/6 封頂後的工程線。

## 不要做的事

不要開始寫第 7 篇理論論文。
不要先做 arbitrary binary patcher。
不要假裝 synthetic smoke test 等於真實遊戲加速。
不要把 24/72 代碼硬映射成 CPU/GPU/NPU。
不要讓 LLM 直接成為 commit proof。

## 現在已完成

- SQLite schema
- Event/Run state
- AIVS VSP + R0/R1/R2/ESCALATE
- Candidate Store
- read-set-aware relevant conflict
- idempotency
- lease/fencing
- Effect Barrier
- Commit Receipt
- Paradigm Profile
- backend registry
- route candidate
- shadow benchmark
- route promotion
- serialization finding
- JSONL import
- Windows WPR/WPA command plan
- synthetic smoke test PASS

## Smoke test 已驗證

- version mismatch但 read set 無 relevant conflict → 可 commit
- relevant stale conflict → reject
- duplicate commit → 同 receipt
- stale fencing token → reject
- irreversible speculative candidate → reject
- 40ms→18ms 且 state equivalent → route promote
- 20ms→10ms 但 state diverges → reject
- AIVS normal → R0
- AIVS high pressure → ESCALATE

## 下一個任務：M1 Windows Evidence Import

### Goal

在真實 Windows 機器上取得一個應用程式的 WPR ETL，經 WPA Exporter 匯出，再 normalization 進 CDI。

### Do

1. 確認 Windows Performance Toolkit 已安裝。
2. 先執行：
   `python src/cdi_runtime_mvp.py windows-plan`
3. 擷取一個 30–120 秒可重現 workload。
4. 用 WPA 手工確認 trace。
5. 建一個最小 `.wpaProfile`。
6. 用 `wpaexporter.exe` 匯出需要的 table。
7. 寫 `WpaCsvAdapter`：
   - CSV → normalized JSONL
   - preserve original row/table reference
8. `import-jsonl` 進 SQLite。
9. 寫 M1 smoke test。

### Acceptance

- 不修改 target process。
- 可重複 capture。
- 至少能重建 process/thread/CPU sample/wait 的某個最小 timeline。
- 每個 normalized event 有 evidence ref。
- 原始 ETL/CSV 不被覆寫。

## M2 Serialization Advisor

輸入 normalized events，輸出：

```yaml
serialization_finding:
  region_id:
  evidence_level:
  observed_serial_ms:
  estimated_necessary_serial_ms:
  estimated_gap_ms:
  confidence:
  blockers:
  next_measurement:
```

v0.2 不要自動改程式。

## M3 Source-visible Benchmark

選一個 open-source、Windows buildable、無 anti-cheat、可重現 workload 的小型 game/simulation。

優先：
- NPC path batch
- asset decode
- read-only preprocessing

不要第一個做 physics/global state。

## MSSP Bridge

既有 repo：
`kakon77777-commits/mssp-game-computer-runtime-mvp`

CDI 不要重寫它。

先用：
- DMS JSONL / structured events
- capture/event references
- existing game window control

做 VisualSemanticPlane。

ETW/PIX 是 PerformanceTracePlane。

未來把兩者用 run/epoch/event reference 對齊。

## 版本策略

- CDI Runtime v0.1：synthetic core（現在）
- v0.2：Windows observer
- v0.3：source-visible advisor + shadow
- v0.4：Game Adapter/GEC
- v0.5：low-risk local commit
- v1.0：需多 workload repeated evidence

## 核心守則

$$
Capability\le Evidence
$$

$$
CorrectnessBeforeSpeed
$$

$$
Candidate\neq Commit
$$

$$
Paradigm\neq Backend
$$

$$
AIUnavailable\not\Rightarrow ApplicationUnavailable
$$
