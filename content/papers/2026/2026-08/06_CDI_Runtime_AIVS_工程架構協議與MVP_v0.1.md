# CDI Runtime + AIVS
## AI 治理多 X 計算的工程架構、協議與 MVP

**English Title:** *CDI Runtime + AIVS: Engineering Architecture, Protocols, and MVP for AI-Governed Multi-X Computation*  
**系列：**《計算域支配智能：AI 語義控制面與自適應多 X 計算》第 6 篇／封頂工程論文  
**系列代號：** CDI / AIVS  
**文件編號：** EML-CDI-06-RUNTIME-2026-v0.1  
**作者：** Neo.K  
**協作整理與原型：** Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-10  
**文件類型：** 工程封頂論文／Runtime Architecture／可執行 MVP  
**系列狀態：** `THEORETICAL CLOSED (6/6) + ENGINEERING OPEN`  
**MVP 狀態：** Synthetic smoke test PASS；Windows ETW native ingestion 與真實遊戲 performance benchmark 尚未在本文執行環境中完成。

---

## 摘要

本系列前五篇依序建立：

$$
\boxed{
\text{AI 語義控制面}
}
$$

$$
\boxed{
\text{AIVS 分層低成本同步}
}
$$

$$
\boxed{
\text{Candidate/Commit 狀態安全}
}
$$

$$
\boxed{
\text{24／72 Paradigm Routing}
}
$$

以及：

$$
\boxed{
\text{Legacy/Game Serialization Gap}
}
$$

本文不再主要增加理論，而將上述架構收斂為一個 Windows-first、source-visible-first、observer-first 的工程 Runtime。

其最小統一式為：

$$
\boxed{
CDI
=
EvidencePlane
+
CausalComputeGraph
+
AIVS
+
CandidateCommit
+
ParadigmRouting
+
Verification
+
Fallback.
}
$$

工程上，AI 不位於 CPU/GPU 每個 operation 的 critical path。底層高速計算仍由：

- 作業系統 scheduler；
- thread pool；
- compiler；
- CPU/GPU/NPU；
- task graph；
- existing application runtime；

執行。

AI 控制面只接收經過 reduction 的：

$$
\boxed{
State
+
CausalBoundary
+
Anomaly
+
RouteEvidence.
}
$$

因此：

$$
\boxed{
RawComputeRate
\gg
AICognitiveRate.
}
$$

本文提出 **CDI Runtime v0.1** 的九層架構：

1. Evidence Adapters；
2. Event Normalizer；
3. Persistent State / Event Log；
4. Region Segmenter / Causal Compute Graph；
5. Paradigm Profile / PRL；
6. AIVS Relay / Governor；
7. Candidate Store / Semantic-Causal Fence；
8. Shadow Benchmark / Game Equivalence；
9. Route Promotion / Fallback。

Windows 第一階段不自行重寫 ETW kernel tracer，而重用官方 WPR / ETW / WPA Exporter：

$$
WPR
\rightarrow
ETL
\rightarrow
WPAExporter
\rightarrow
CSV/NormalizedJSONL
\rightarrow
CDI.
$$

遊戲語義面則可與既有 `mssp-game-computer-runtime-mvp` 並存：MSSP 提供視窗、持續視覺事件、控制、安全證據與 DMS 類稽核；CDI 的 performance plane 則由 ETW／PIX／profiler 提供。兩者最終可在共同 epoch / event reference 下對齊，但本文不把 MSSP 誤稱為 performance profiler。

本文交付一個標準函式庫 Python MVP，使用 SQLite WAL 持久化，實作：

- Run / Event Store；
- AIVS Vertical Sync Packet；
- deterministic sync pressure / R0-R2 escalation；
- Compute Candidate；
- read-set-aware relevant conflict；
- state version；
- idempotency；
- lease / fencing token；
- Effect Barrier；
- Commit Receipt；
- Paradigm Profile；
- Backend Registry；
- Route Candidate；
- Shadow Benchmark；
- Route Promotion；
- Serialization Finding；
- JSONL evidence import；
- Windows WPR/WPA capture plan；
- synthetic smoke test。

實際 smoke test 已驗證：

- 正常 AIVS event 落在 `R0`；
- 高壓 event 進 `ESCALATE`；
- candidate 1 正常 commit；
- 一個以舊 state version 產生、但 read-set 與期間 changed keys 不衝突的 candidate 仍可合法 commit；
- 真正 relevant stale candidate 被拒；
- 重複 idempotency key 回傳同一 commit receipt；
- 舊 fencing token 被拒；
- speculative irreversible effect 被拒；
- shadow route 在 state equivalence 成立且 `40 ms → 18 ms` 時被 promotion；
- state 不等價的較快 route 被拒；
- synthetic serialization gap 被估為 `26 ms`。

因此本文達到的是：

$$
\boxed{
\text{Architecture Exists}
+
\text{Core Protocol Behaves in Synthetic MVP}
}
$$

而不是：

$$
\boxed{
\text{任何舊遊戲已被自動多核化}.
}
$$

後續工程版本應沿：

$$
Observer
\rightarrow
Advisor
\rightarrow
Shadow
\rightarrow
LowRiskCommit
\rightarrow
AdaptiveRouting
$$

逐步推進。

---

# 1. 工程目標與非目標

## 1.1 v0.1 目標

CDI Runtime v0.1 要能回答：

> 目前程式／工作域裡發生了什麼？

> 哪些 region 值得進一步分析？

> 一個計算結果是否仍基於合法狀態？

> 一個新 route 是否只應存在於 shadow？

> 哪些異常應由 Relay 局部吸收，哪些需要 Governor？

> 哪些 evidence 足以 promotion，哪些只能 advisory？

---

## 1.2 v0.1 非目標

本文不宣稱：

- 任意 Windows binary 可以自動平行化；
- AI 可以安全重排任意 machine instruction；
- 任意 single-thread game 都能多核加速；
- 24／72 已是最終完整 routing ontology；
- LLM 判斷等同 correctness proof；
- synthetic benchmark 等同真實 game speedup；
- SQLite 是高頻 game-state database 的最終方案；
- Python MVP 是 hard-real-time runtime。

---

# 2. 核心架構

```text
              ┌──────────────────────────────┐
              │ Application / Game / Workload│
              └──────────────┬───────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
     Source/Symbol        ETW/PIX/WPA        MSSP Semantic
       Adapter             Evidence             Bridge
         │                   │                   │
         └───────────────┬───┴───────────────────┘
                         ▼
                Evidence Normalizer
                         │
                         ▼
                Event Log / State Store
                         │
                         ▼
        Region Segmenter / Causal Compute Graph
                         │
                 ┌───────┴────────┐
                 ▼                ▼
          Paradigm Profile      AIVS
              / PRL          Relay/Governor
                 │                │
                 └───────┬────────┘
                         ▼
                  Candidate Store
                         │
                         ▼
             Semantic-Causal Fence
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
          Reject/Hold             Shadow Run
                                     │
                                     ▼
                            Equivalence / Benchmark
                                     │
                              ┌──────┴──────┐
                              ▼             ▼
                           Reject         Promote
                                          │
                                          ▼
                                   Route Commit
                                          │
                                          ▼
                                      Receipt
```

---

# 3. Evidence Plane

CDI 不自己取代所有 profiler。

v0.1 Evidence Plane：

$$
\boxed{
E=
E_{source}
\oplus
E_{trace}
\oplus
E_{semantic}
\oplus
E_{benchmark}.
}
$$

---

# 4. Windows Trace Adapter

Windows 官方 ETW 已提供 Provider / Controller / Consumer 事件架構；WPR 基於 ETW 擷取，WPA 分析 ETL，WPA Exporter 可以把指定 profile 中的 table 自動匯出 CSV。

因此 v0.1 建議：

```text
wpr -start GeneralProfile -filemode
      ↓
run benchmark
      ↓
wpr -stop cdi_trace.etl "CDI capture"
      ↓
wpaexporter.exe
      ↓
CSV
      ↓
CDI Normalizer
```

MVP 目前提供 `windows-plan` 指令產生這條命令規劃，但不在本執行環境宣稱已 native 解析 ETL。

---

# 5. 為什麼先 Export 再 Normalization？

因為工程優先順序應是：

$$
\boxed{
\text{先驗證 CDI 決策流程}
>
\text{先重造 ETW parser}.
}
$$

若 Runtime 本身的：

- region model；
- Candidate/Commit；
- AIVS；
- route promotion；

都尚未證實，就沒有必要先投入 kernel tracing infrastructure。

---

# 6. Native ETW 的未來位置

v0.2+ 可新增：

```text
ETW Real-Time Consumer
→ normalized event
→ Event Store
```

但 Adapter Contract 不變。

這就是：

$$
\boxed{
TransportReplaceable
+
SemanticContractStable.
}
$$

---

# 7. MSSP Game Runtime Bridge

既有 `mssp-game-computer-runtime-mvp` v0.8.0 已具有：

- 持續遊戲視窗擷取；
- temporal diff；
- structured vision events；
- bounded multimodal queue；
- action verification；
- live control plane；
- DMS JSONL audit；
- RDR 註冊／授權；
- provider-neutral inference path。

CDI 不應重寫這一套。

合理整合：

$$
\boxed{
MSSP
=
VisualSemanticPlane
}
$$

$$
\boxed{
CDI
=
PerformanceCausalPlane.
}
$$

---

# 8. 兩個 Plane 的交會

例如：

MSSP：

> scene changed，進入戰鬥。

CDI：

> 同一時間窗 main-thread `npc.paths` 從 4 ms 上升到 18 ms。

這建立：

$$
\boxed{
SemanticEvent
\leftrightarrow
PerformanceEvent.
}
$$

仍需要 intervention / replay 才能進一步支持因果，而不是只靠時間共現。

---

# 9. Persistent Runtime State

v0.1 使用 SQLite。

不是因為 SQLite 最快，而是因為它提供：

- transactional durability；
- WAL；
- relational query；
- zero-service deployment；
- Python stdlib support。

適合 MVP 的：

$$
\boxed{
ControlPlaneState.
}
$$

---

# 10. SQLite 不放 raw high-frequency telemetry

raw trace 應：

- file；
- ETL；
- CSV；
- parquet / binary future store；

保存。

SQLite 放：

- index；
- digest；
- event；
- candidate；
- receipt；
- summary；
- evidence pointer。

所以：

$$
\boxed{
Database
\neq
RawTraceWarehouse.
}
$$

---

# 11. 核心資料表

v0.1 實作：

```text
runs
events
state_changes
leases
candidates
commit_receipts
sync_events
paradigm_profiles
backend_capabilities
route_candidates
route_benchmarks
route_receipts
serialization_findings
negative_routes
external_imports
```

---

# 12. Run

$$
Run
=
(
epoch,
topologyVersion,
policyVersion,
stateVersion
).
$$

四個版本分開。

避免：

> 一個 `version=42` 到底代表什麼？

---

# 13. Event

append-oriented：

```text
event_id
run_id
event_type
scope
payload
time
```

正式狀態可以被 fold / projection 重建。

---

# 14. State Version

每次正式 commit：

$$
v\rightarrow v+1.
$$

並記：

$$
ChangedKeys(v).
$$

這使 relevant conflict 可被機械判斷。

---

# 15. Relevant Conflict

若 candidate 讀：

$$
R(c).
$$

在其 read version 到現在期間改變：

$$
\Delta W.
$$

只有：

$$
\boxed{
R(c)\cap\Delta W\neq\varnothing
}
$$

才必然因 relevant stale state 拒絕。

---

# 16. 為什麼不是版本不同就全拒？

因為：

Worker A 讀 `weather`。

其他 commit 只改 `npc_paths`。

則：

$$
VersionChanged
$$

但：

$$
RelevantConflict=0.
$$

可以保留 concurrency。

MVP smoke test 已驗證此案例。

---

# 17. AIVS Runtime

v0.1 的 Relay 不必是 LLM。

先：

$$
Z
=
\frac{
A+D+C+U+R+N
}{6}.
$$

依 threshold：

$$
Z<0.25
\Rightarrow
R0
$$

$$
0.25\le Z<0.5
\Rightarrow
R1
$$

$$
0.5\le Z<0.75
\Rightarrow
R2
$$

$$
Z\ge0.75
\Rightarrow
ESCALATE.
$$

---

# 18. R0 的意義

R0：

- deterministic；
- no LLM required；
- digest/version/check/status。

這是 Token 控制核心。

---

# 19. VSP

Vertical Sync Packet 只帶：

- identity；
- epoch/version；
- status；
- pressure；
- regime；
- evidence refs。

不是：

> 把完整 trace 貼給 AI。

---

# 20. Evidence Reference

VSP：

```json
{
  "evidence_refs": [
    "etl:cdi_trace.etl#cpu/123",
    "mssp:event:scene-991"
  ]
}
```

只有必要時：

$$
Retrieve.
$$

---

# 21. Candidate Store

Worker 的 result 不直接成為 state。

先：

$$
\boxed{
Candidate.
}
$$

保存：

- input version；
- read keys；
- write keys；
- output digest；
- effect class；
- authority；
- idempotency。

---

# 22. Semantic-Causal Fence

v0.1 先 deterministic：

1. epoch；
2. topology；
3. policy；
4. dependency；
5. invariant；
6. semantic status；
7. effect barrier；
8. fencing token；
9. relevant conflict。

未來才讓 AI 介入 semantic ambiguity。

---

# 23. Effect Barrier

如果：

$$
Speculative=1
$$

且：

$$
EffectClass=Irreversible,
$$

v0.1：

$$
\boxed{
Reject.
}
$$

---

# 24. 為什麼這麼保守？

因為：

$$
\boxed{
SpeculativeCompute
}
$$

應主要發生在：

- Pure；
- Reversible；
- sandboxed；

region。

真正不可逆外部作用要在更強治理下另行設計。

---

# 25. Idempotency

重複：

$$
Commit(candidate)
$$

不應造成第二個 effect。

MVP 以：

$$
(run,idempotencyKey)
$$

唯一索引實作。

---

# 26. Lease / Fencing

scope：

```text
npc
physics
route.global
```

每次 ownership 更新：

$$
token\rightarrow token+1.
$$

舊 token：

$$
Reject.
$$

Smoke test 已驗證：

$$
token_1<token_2
$$

後，舊 candidate 不可 commit。

---

# 27. Paradigm Registry

v0.1 profile：

```text
B: C/D
U: S/J/P/R
O: C/D/X
L: F/K/Q/HYBRID/UNKNOWN
```

Runtime sentinel：

```text
UNKNOWN
KEEP_ORIGINAL
UNSUPPORTED
```

不被視為新理論格。

---

# 28. Backend Registry

不是：

$$
P\rightarrow GPU.
$$

而是：

```text
profile
+ dependency
+ backend capability
+ load
+ policy
→ feasible route
```

---

# 29. Route Candidate

AI／rule 提出：

```text
cpu_serial → cpu_parallel
```

此時：

$$
\boxed{
Proposal
\neq
ActiveRoute.
}
$$

---

# 30. Shadow Benchmark

比較：

$$
S_{base}
$$

與：

$$
S_{candidate}.
$$

先：

$$
Equivalent?
$$

再：

$$
Faster?
$$

---

# 31. MVP 的 Shadow Route Test

synthetic：

$$
40ms
\rightarrow
18ms.
$$

speedup：

$$
\approx2.22\times.
$$

state digest 一致，

因此 route 被 promotion。

---

# 32. 故意錯誤的新 route

candidate：

$$
10ms
$$

更快，

但 state：

$$
x=1.5
$$

而 baseline：

$$
x=1.0.
$$

所以：

$$
\boxed{
Reject.
}
$$

這證明 v0.1 promotion gate：

$$
Correctness
>
Speed.
$$

---

# 33. Game Equivalence Contract

正式遊戲版本不能只用 generic JSON equality。

需要 adapter 定義：

$$
GEC
=
(
StateFields,
RNG,
Events,
Tolerance,
PromotionPolicy
).
$$

---

# 34. Frame / Simulation Epoch

未來 Game Adapter 應至少支援：

$$
\mathbf e
=
(
e_{sim},
e_{render},
e_{asset},
e_{network}
).
$$

不要假設：

$$
Frame=Tick.
$$

---

# 35. Serialization Finding

v0.1 儲存：

$$
T_{observed}
$$

$$
\hat T_{necessary}
$$

以及：

$$
\boxed{
\hat G_S
=
T_{observed}
-
\hat T_{necessary}.
}
$$

Smoke：

$$
40-14=26ms.
$$

此值只是 synthetic engineering estimate，不是任何真實遊戲測量。

---

# 36. Evidence Authority

建議：

```text
E0 timing only            → observe
E1 thread/call stack      → advise
E2 markers/API/locks      → advise
E3 source/IR/read-write   → shadow
E4 shadow equivalence     → low-risk promotion
E5 repeated benchmark     → policy-bounded promotion
```

---

# 37. Capability ≤ Evidence

$$
\boxed{
AutomationAuthority
\le
EvidenceMaturity.
}
$$

這是整個工程版本最重要的 governance invariant 之一。

---

# 38. Windows-first 開發階段

## Phase 0 — Synthetic Core

已完成 MVP。

內容：

- DB；
- AIVS；
- candidate；
- relevant conflict；
- route shadow；
- smoke tests。

---

# 39. Phase 1 — Observer

Windows：

$$
WPR
\rightarrow
ETL
\rightarrow
WPAExporter
\rightarrow
CSV
\rightarrow
Normalizer.
$$

只觀察。

---

# 40. Phase 2 — Advisor

輸出：

```yaml
finding:
  region:
  evidence:
  suspected_serialization_gap:
  confidence:
  safest_next_experiment:
```

不改程式。

---

# 41. Phase 3 — Source-visible Patch Candidate

只對：

- source available；
- build works；
- tests exist；

project。

AI 生成 patch。

仍：

$$
Candidate.
$$

---

# 42. Phase 4 — Shadow Route

新 route：

$$
NoExternalAuthority.
$$

重播／benchmark。

---

# 43. Phase 5 — Low-risk Commit

允許：

- Pure；
- Reversible；
- local scope；

promotion。

---

# 44. Phase 6 — Adaptive Runtime Routing

最後才：

$$
AIVS+PRL
$$

動態調 route。

---

# 45. 第一個真實 benchmark 的選擇

應選：

$$
\boxed{
OpenSource
+
Windows
+
LegacyStyleMainLoop
+
DeterministicScenario
}
$$

而不是：

$$
AAAClosedBinary.
$$

---

# 46. Benchmark 成功條件

至少：

## Performance

- p50；
- p95；
- p99；
- main-thread ms；
- CPU utilization；
- wait time。

## Correctness

- GEC；
- crash；
- deadlock；
- state divergence；
- RNG divergence。

## AI Cost

- calls；
- Token；
- latency；
- escalation。

---

# 47. 必須有 Baseline

同一：

- build；
- scene；
- save；
- settings；
- warmup；
- capture duration。

否則：

$$
Speedup
$$

沒有意義。

---

# 48. Warmup 必須分開

shader compile、cache、JIT 都可能污染第一次 run。

---

# 49. Route Promotion Rule

建議：

$$
Promote
\iff
CorrectnessPass
\land
Speedup\ge S_{min}
\land
TailLatencyNotWorse
\land
FallbackPass.
$$

---

# 50. Rollback / Fallback

route promotion 不直接刪 original。

保存：

$$
\boxed{
OriginalRoute.
}
$$

如果：

- performance regression；
- error；
- AI unavailable；
- capability loss；

立即：

$$
Fallback.
$$

---

# 51. Negative Route Memory

失敗 route：

```text
region hash
route fingerprint
reason
benchmark
```

未來：

$$
RetrieveFailure.
$$

避免重新浪費 Token。

---

# 52. Route Cache

成功 route：

$$
ProfileHash
+
HardwareProfile
+
Policy
\rightarrow
KnownRoute.
$$

工作由 Search 逐步轉成 Retrieval。

---

# 53. ACR 在 Runtime 的具體位置

不是只有：

> 模型想多深。

而是：

$$
R
=
(
Frequency,
Context,
EvidenceFetch,
Model,
Verifier,
Authority
).
$$

---

# 54. AI Timeout

若：

$$
AIResponseTime>Deadline,
$$

v0.1 default：

$$
\boxed{
KEEP\_ORIGINAL.
}
$$

---

# 55. AI Down

Runtime 仍可：

- observe；
- deterministic validate；
- serial fallback；
- existing route。

因此：

$$
\boxed{
AIUnavailable
\not\Rightarrow
ApplicationUnavailable.
}
$$

---

# 56. Critical Path

原則：

$$
\boxed{
AIBlockingCriticalPath
\rightarrow
Minimize.
}
$$

AI 大多：

$$
Sideband.
$$

---

# 57. Relay / Governor 的部署建議

Relay：

- 本地；
-小模型／rules；
- subsystem scope。

Governor：

- 本地強模型或雲端；
-低頻；
- cross-domain。

---

# 58. 不要求一開始多 AI

MVP 可由：

$$
\boxed{
OneProcess
}
$$

模擬：

- Relay policy；
- Governor policy。

先驗證架構，

再拆成多模型。

---

# 59. 與現有 MSSP Repo 的部署方式

`mssp-game-computer-runtime-mvp` 目前 Python `>=3.11`、零 runtime dependencies，具有 CLI / MCP server。

CDI MVP 也刻意採 Python stdlib-only，

方便未來：

```text
MSSP
   ↕ JSONL / MCP / local bridge
CDI Runtime
```

而不立即新增大型 dependency graph。

---

# 60. DMS Bridge

如果 MSSP DMS 產生 JSONL，

CDI v0.1 已提供：

```text
import-jsonl
```

作通用 event ingest。

這只是 generic import；正式 MSSP semantic mapping 仍需下一個工程版本定 schema。

---

# 61. CLI

目前：

```text
init-db
demo
smoke
windows-plan
import-jsonl
```

---

# 62. Quick Start

```bash
python src/cdi_runtime_mvp.py smoke --db tests/cdi_smoke.db
```

成功：

```text
PASS
```

---

# 63. Windows Capture Plan

```bash
python src/cdi_runtime_mvp.py windows-plan
```

輸出：

```text
wpr -start GeneralProfile -filemode
wpr -stop "cdi_trace.etl" "CDI capture"
wpaexporter.exe ...
```

production 應改用自訂 WPR / WPA profile，而非永久只用 GeneralProfile。

---

# 64. Schema Validation

本文附 JSON Schema：

- VSP；
- Compute Candidate；
- Paradigm Profile；
- GEC。

Python MVP v0.1 不引入 `jsonschema` dependency。

schema 是：

$$
\boxed{
WireContract
}
$$

不是 runtime validator dependency。

---

# 65. 為什麼 stdlib-only？

為了：

- 與 MSSP repo 風格相容；
-降低 deployment friction；
-先驗證 protocol；
-未來再替換性能組件。

---

# 66. SQLite 之後可以換

Adapter boundary：

$$
PersistencePort.
$$

未來：

- PostgreSQL；
- RocksDB；
- event store；
- Redis；

都可。

但 v0.1：

$$
SQLite.
$$

---

# 67. Trace Store 也可以換

v0.1 只保存 references / normalized events。

未來：

- Arrow；
- Parquet；
- DuckDB；
- columnar trace store。

---

# 68. PRL 也可以換

v0.1 route policy：

- rule；
- profiler；
- shadow benchmark。

未來：

- optimizer；
- learned router；
- constraint solver。

---

# 69. AI Provider 也可以換

Runtime 不應寫死：

$$
OpenAIOnly.
$$

Relay / Governor contract：

$$
StructuredDecisionIn
\rightarrow
StructuredDecisionOut.
$$

---

# 70. Decision Schema

未來 AI 最好只輸出：

```yaml
decision:
  act: NOOP | INSPECT | HOLD | RETRY | REROUTE | ESCALATE
  target:
  reason_code:
  evidence_refs:
  confidence:
```

而不是自由文字直接控制程序。

---

# 71. Natural Language 是 Explanation Plane

AI 可以另附：

```text
explanation
```

但正式控制依：

$$
TypedDecision.
$$

---

# 72. Security Boundary

v0.1 不應以管理員權限常駐。

Windows Observer：

只要求取得 profiler 所需最小權限。

---

# 73. Binary Instrumentation

Detours：

$$
ObserverOnly
$$

預設。

不把：

$$
CanHook
$$

當作：

$$
CanRewrite.
$$

---

# 74. Anti-Cheat

競技／反作弊遊戲：

$$
\boxed{
OutOfScope
}
$$

除非遊戲／平台明確允許 instrumentation。

---

# 75. Copyright / Mod Boundary

CDI 工具：

- 不散布遊戲本體；
-不散布 proprietary code；
-改動方案與 patch 需依實際授權。

---

# 76. Safety Invariants

## I1

$$
AIRecommendation\neq CommitAuthority.
$$

## I2

$$
EvidenceRetrievable.
$$

## I3

$$
StaleFencingCannotCommit.
$$

## I4

$$
IrreversibleSpeculationBlocked.
$$

## I5

$$
AIOutageHasFallback.
$$

## I6

$$
CorrectnessBeforeSpeed.
$$

## I7

$$
UnknownIsAllowed.
$$

## I8

$$
Capability\le Evidence.
$$

---

# 77. Smoke Test 內容

實際執行：

- 2 AIVS sync events；
- 5 candidates；
- 2 valid commits；
- 2 route candidates；
- 2 shadow benchmarks；
- 1 route promotion；
- 1 serialization finding。

---

# 78. Smoke Test 核心結果

```text
low_regime = R0
high_regime = ESCALATE
idempotent_same_commit = true
relevant_conflict_rejected = true
stale_fencing_rejected = true
irreversible_speculation_rejected = true
shadow_route_equivalent = true
route_promoted = true
bad_route_rejected = true
serialization_gap_ms = 26.0
```

---

# 79. 此 Smoke Test 能支持什麼？

支持：

> v0.1 的 protocol logic 在 synthetic scenario 中按預期運作。

---

# 80. 不能支持什麼？

不支持：

- 真實 ETW ingestion throughput；
-真實遊戲 speedup；
-AI classifier accuracy；
-真實 thread-safe runtime mutation；
-真實 GPU route promotion；
-高併發 distributed commit。

---

# 81. 第一個真正有判別力的工程實驗

選一個 source-visible game / simulation。

建立：

$$
Baseline.
$$

找一個：

$$
CandidateRegion.
$$

例如 NPC path batch。

---

# 82. Experiment A

原：

$$
Serial.
$$

新：

$$
ParallelShadow.
$$

---

# 83. Experiment B

測：

- state；
- RNG；
- events；
- p95/p99；
- CPU utilization。

---

# 84. Experiment C

若通過：

$$
PromoteLowRisk.
$$

---

# 85. Experiment D

注入：

- stale navmesh；
- delayed worker；
- duplicate result。

測 Candidate/Commit。

---

# 86. Experiment E

關 AI。

測：

$$
Fallback.
$$

---

# 87. Experiment F

讓 AI 給錯 route。

測：

$$
ShadowGate.
$$

---

# 88. Experiment G

故意製造：

$$
VersionChanged
$$

但：

$$
NoRelevantConflict.
$$

測 concurrency 不被過度犧牲。

---

# 89. Experiment H

故意：

$$
RelevantConflict.
$$

必須 reject。

---

# 90. Engineering Success Criteria v0.2

至少：

- 1 source-visible app；
- 1 real ETW capture；
- 1 normalized trace；
- 1 AI/heuristic serialization finding；
- 1 shadow route；
- correctness pass；
- measurable net gain；
- AI overhead measured；
- fallback verified。

---

# 91. Engineering Success Criteria v0.3

加入：

- MSSP semantic event alignment；
-Game Adapter；
-GEC；
-frame/sim epochs；
-negative route memory。

---

# 92. Engineering Success Criteria v0.4

加入：

- live Relay；
-limited runtime route switch；
-low-risk local commit。

---

# 93. Engineering Success Criteria v0.5

加入：

- multi-relay；
-Governor；
-cross-flow conflict；
-AIVS adaptive frequency。

---

# 94. Engineering Success Criteria 1.0

只有在：

- repeated benchmarks；
-multiple workloads；
-reliability；
-observability；
-safe fallback；

都成熟後才考慮。

---

# 95. 系列的最終工程結論

最初問題是：

> AI 能不能幫一個不擅長多核的舊遊戲加速？

六篇之後，答案被精確化為：

$$
\boxed{
\text{AI 可能可以幫忙，}
}
$$

但它不是靠：

$$
\boxed{
\text{AI 替 CPU 算所有東西。}
}
$$

而是靠：

$$
\boxed{
\text{看見計算}
\rightarrow
\text{理解依賴}
\rightarrow
\text{找出 Serialization Gap}
\rightarrow
\text{提出新 route}
\rightarrow
\text{低成本同步}
\rightarrow
\text{shadow}
\rightarrow
\text{驗證}
\rightarrow
\text{安全 promotion}.
}
$$

---

# 96. 最終統一式

$$
\boxed{
CDI
=
\underbrace{Observe}_{Evidence}
+
\underbrace{Understand}_{Causal/Paradigm}
+
\underbrace{AllocateAttention}_{AIVS/ACR}
+
\underbrace{Propose}_{RouteCandidate}
+
\underbrace{Verify}_{Fence/GEC}
+
\underbrace{Commit}_{Receipt}
+
\underbrace{Recover}_{Fallback}.
}
$$

---

# 97. 與 STDI 的尺度對應

STDI：

$$
Intent
\rightarrow
WorldModel
\rightarrow
PhysicalRouting
\rightarrow
Action
\rightarrow
Evidence.
$$

CDI：

$$
\boxed{
Intent
\rightarrow
ComputeModel
\rightarrow
ComputeRouting
\rightarrow
Execution
\rightarrow
Evidence.
}
$$

二者是結構相似，

不是同一 system。

---

# 98. 為什麼「AI 中繼」是必要的？

沒有 Relay：

$$
NWorkers
\rightarrow
Governor
$$

容易形成新中央瓶頸。

有 Relay：

$$
Worker
\rightarrow
CheapCheck
\rightarrow
LocalRecovery/Reduction
\rightarrow
EscalateOnlyIfNeeded.
$$

---

# 99. 為什麼 ACR 是必要的？

如果每個 event 都：

$$
DeepReasoning,
$$

AI cost 會吞掉 acceleration。

所以：

$$
\boxed{
ThinkProportionally
}
$$

在這裡不只是哲學，

而是 performance requirement。

---

# 100. 為什麼 Candidate/Commit 是必要的？

AI 可能錯。

profiler inference 可能錯。

route candidate 可能錯。

所以：

$$
\boxed{
FastExploration
+
SlowEnoughCommitDiscipline.
}
$$

是安全平衡。

---

# 101. 為什麼 24／72 有價值？

不是因為：

> 世界只能有 24／72 種計算。

而是因為它提供：

$$
\boxed{
CompactRoutingVocabulary.
}
$$

幫 Runtime 問：

- sequence？
- selective？
- parallel？
- retrieval？
- deterministic？
- stochastic？
- quantum/hybrid？

但：

$$
\boxed{
RealityWinsOverTaxonomy.
}
$$

---

# 102. 為什麼 Game Benchmark 有價值？

因遊戲同時包含：

$$
State
+
Latency
+
CPU/GPU
+
Interaction
+
RNG
+
VisualSemantics.
$$

如果 CDI 能在這裡工作，

它會是很強的 stress test。

---

# 103. 但遊戲不是唯一目的

同一 Runtime 可測：

- scientific app；
-media tool；
-simulation；
-CAD；
-legacy server；
-data pipeline。

---

# 104. 最終產品形態

可能不是：

> AI 多核加速器。

更可能是：

# **AI Computational Control Plane**

即：

> 一個位於 existing compiler/runtime/OS 之上的語義—因果治理層。

---

# 105. 系列封頂

本系列到第六篇停止新增論文。

$$
\boxed{
SeriesStatus
=
THEORETICAL\ CLOSED
+
ENGINEERING\ OPEN.
}
$$

後續只進：

- CDI Runtime v0.2；
- AIVS protocol v0.2；
- Windows adapter；
- Game Adapter；
- benchmark；
- source-visible optimizer；
- production hardening。

不以「第七篇」延伸本系列核心。

---

## 參考資料

### 系列內部研究

1. 《AI 不必替代計算：從傳統執行平面到語義—因果控制平面》，2026。
2. 《AI 垂直同步：分層中繼、認知比例性與低成本因果一致》，2026。
3. 《候選不是提交：多 X 計算中的因果校正、錯位檢測與可恢復執行》，2026。
4. 《從 24／72 計算範式到 Runtime 路由》，2026。
5. 《舊應用與遊戲的 AI 加速：從實作串行化到必要串行化》，2026。
6. 《計算的二十四重範式》正式版 v4.0，2026。
7. 《從二十四重計算形態學到七十二格計算動力學》v0.1，2026。
8. 《Adaptive Cognitive Runtime 工程白皮書》v0.1，2026。
9. `mssp-game-computer-runtime-mvp` v0.8.0。

### 2026-08-10 重新核對之 Primary Sources

10. Microsoft Learn. *About Event Tracing / Event Tracing Tools / WPR Command-Line Options / WPA Exporter*。
11. Microsoft Learn. *PIX Timing Captures — Analyze CPU and GPU*。
12. SQLite. *Atomic Commit In SQLite / Write-Ahead Logging*。
13. LLVM/MLIR. *Transform Dialect / Transform Dialect Tutorial*。
14. Microsoft Research. *Detours*。

---

## 版本紀錄

- **v0.1 / 2026-08-10**：系列封頂工程版。交付 SQLite runtime、AIVS、Candidate/Commit、relevant conflict、lease/fencing、Effect Barrier、Paradigm Profile、Route Shadow/Promotion、Serialization Finding、JSONL import、Windows capture plan、JSON Schema 與 synthetic smoke test。
