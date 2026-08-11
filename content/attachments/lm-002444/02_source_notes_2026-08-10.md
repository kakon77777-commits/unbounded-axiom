# Paper 02 — Fresh Source Notes
## 2026-08-10

本篇開寫前重新檢索／查閱公開 primary sources。

## NVIDIA CUDA Cooperative Groups
- Cooperative Groups 可組織不同粒度 thread groups。
- group 可 partition。
- `sync()` 在 group 粒度建立同步。
- 同步提供參與 thread 的 memory visibility。
- barrier 具有 arrive / wait phase。
- AIVS 借用的是 granularity / grouping 思想，不等於 CUDA barrier。

## NVIDIA CUDA Asynchronous Barriers
- arrive 與 wait 可分離。
- 可使 local processing 與同步等待交疊。
- 提供 fine-grained、non-blocking coordination。
- 對 AIVS 支持 `NonBlockingFirst` 的工程類比。

## MPI 4.1 — MPI_Reduce
- 多 process input 可依 operation 歸約到 root。
- operation 假設 associative。
- 浮點等非嚴格 associative 情況，reduction order 可能改變結果。
- AIVS 因此將 deterministic aggregate 與 semantic summary 分離。

## OpenTelemetry Sampling
- Head sampling：早期決定、效率高，但無法利用完整 trace 後續資訊。
- Tail sampling：可依 error、latency、attributes 等完整／近完整 trace 資訊判斷。
- Tail sampling 需要 state、buffer 與資源，高負載下甚至需 fallback。
- AIVS 據此提出 `HeadFilter + TailInspection + EventTriggeredDeepDive`。

## Akka Supervision and Monitoring
- supervision 與 business logic 分離。
- failure strategy 包括 resume / restart / stop。
- actor hierarchy 中永久 failure 可以往上 bubble。
- AIVS 借用 local-first / bubble-up 結構，但上行的不只 exception。

## Microsoft .NET TaskScheduler
- 預設 TaskScheduler 使用 .NET ThreadPool。
- 支援 work-stealing、thread injection / retirement。
- TaskScheduler 也是 custom scheduling logic extension point。
- 再次確認 CDI/AIVS 的定位是 higher-level semantic / causal supervision，而非重新發明 OS 排程。

---

# 內部依據

## ACR
核心：

$$
R_t=f(T,U,H,E_t)
$$

以及 minimum sufficient cognition。

本篇映射成：

$$
R=(Depth,Frequency,Context,Evidence,Tools,Authority).
$$

## 適度認知論
核心：「需要多少，就想多少；需要改變時，再改變。」

## MSSP Game Runtime
現有 Continuous Vision Loop：

$$
Frame\rightarrow LumaSignature\rightarrow TemporalDiff\rightarrow StructuredEvent.
$$

並具有 idle/active FPS、event/sampled/every-frame 模式、bounded queue、TTL、keyframe、cursor。

## 2026-08-09 跨任務實驗
已觀察：
- stale read 可在 commit 前隔離；
- candidate failure 不必污染公共序列；
- append-only correction；
- cursor / turn identity 的重要性。

---

# 本篇新提出，不能誤寫成外部文獻已有

- AI Vertical Synchronization（AIVS）。
- State / Causal / Semantic / Commit / Topology / Policy-Capability 六類同步。
- Vertical Sync Packet（VSP）。
- Relay AI / Governor AI 的 ACR 梯度。
- 低層高頻低認知 → 高層低頻高認知。
- Semantic Reduction：typed aggregate + evidence pointer。
- Sync Pressure $Z_i(t)$。
- Cognitive Sync Ratio $\rho_c$。
- Escalation Ratio $\rho_e$。
- Governor Attention Efficiency。
- Sparse Cognition over Dense Computation。
- Vertical Convergence / Vertical Expansion。
