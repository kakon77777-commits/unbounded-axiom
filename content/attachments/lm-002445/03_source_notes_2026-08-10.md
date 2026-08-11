# Paper 03 — Fresh Source Notes
## 2026-08-10

本篇開寫前重新檢索／查閱公開 primary sources。

---

## FoundationDB — Transactions / Conflict Checking

官方 Developer Guide 與 Transaction Processing 文件指出：

- transaction 取得 read version 後執行。
- read-write transaction 在 commit 時檢查是否與已提交 transaction 發生衝突。
- 若 transaction 所讀內容在期間被別的已提交 transaction 修改，commit 可被拒絕。
- conflict 後由 client retry。
- FoundationDB 對 conflict checking 做平行／多執行緒優化。

對 CDI 的結構啟示：

$$
ComputeFirst
\rightarrow
ConflictCheckAtCommit.
$$

這支持「版本改變不一定全部重算，而應檢查 relevant conflict」。

---

## FoundationDB — Commit Unknown / Idempotency

官方 Automatic Idempotency 文件指出：

- `commit_unknown_result` 表示 client 可能不知道 transaction 是否其實已經成功。
- 若無條件 retry，effect 可能執行兩次。
- FoundationDB 專門提供 automatic idempotency 能力處理此類問題。

對 CDI：

$$
Attempt\neq KnownCommit.
$$

以及：

$$
Retry\Rightarrow IdempotencyNeeded.
$$

---

## SQLite — Atomic Commit / WAL

官方文件指出：

- SQLite 的 rollback journal 與 WAL 都用來提供 atomic commit / rollback。
- WAL 模式將改動先寫入 WAL，commit marker 決定 transaction commit。
- rollback journal / WAL 提供「正式資料」與「尚未確認修改」分離的成熟例子。

對 CDI：

支持：

$$
JournalBeforeUnsafeMutation.
$$

但遊戲／外部設備的不可逆 effect 不能直接等同資料庫 rollback。

---

## Linux Kernel — Sequence Counters / Seqlock

官方文件指出：

- reader 讀 sequence count；
- 讀取資料；
- 再檢查 sequence；
- 若 sequence 在讀取期間改變，reader retry。
- 適合 read-mostly data，reader 願意在 writer 更新時 retry。

對 CDI：

支持：

$$
Read
\rightarrow
ValidateVersion
\rightarrow
Accept/Retry.
$$

並提醒簡單 version check 能處理的問題不應先呼叫 AI。

---

## Intel TSX / RTM

Intel 官方資料指出：

- Intel TSX 提供 hardware transactional memory / Restricted Transactional Memory。
- RTM transaction 可 commit 或 abort。
- Intel 文件強調軟體需有非 transaction fallback；不能假設 RTM region 一定會成功 commit。
- 新版 Intel 支援文件亦指出部分處理器／microcode 環境可能預設強制 abort RTM transaction。

對 CDI：

最重要的不是綁定 TSX，而是成熟模式：

$$
Speculate
\rightarrow
Commit/Abort
\rightarrow
Fallback.
$$

這支持本文「提前計算 + 延後承諾」的抽象。

---

## Kubernetes — Lease / Coordinated Leader Election

官方文件指出：

- Lease API 用於 node heartbeat 與 component leader election。
- Coordinated Leader Election 使用 Lease / LeaseCandidate 維護 component leadership。
- Lease 具有 holder identity、renewal 與 duration 等時效語義。

對 CDI：

支持：

$$
AuthorityHasLifetime.
$$

本篇的 fencing token、semantic scope、commit authority 是 CDI 自行增加的層次，不能說 Kubernetes 已提供完整保證。

---

## Herlihy & Moss 1993 — Transactional Memory

原始 transactional memory 工作提出：

- multiprocessor architecture 支援 transaction-like read-modify-write；
- 目標是讓並行資料結構避免傳統 locking 的部分問題；
- transaction 概念後來成為 speculative + atomic commit/abort 計算的重要基礎。

本篇只借用 transaction boundary 思想，不主張 CDI 是 transactional memory 的替代。

---

# 與使用者 2026-08-09 實驗的連接

兩篇工作論文記錄：

- 固定接力曾發生 stale read，但在正式 Board commit 前攔截。
- 自由接力有 5 個候選失敗回合，正式 `1..100` 序列仍無缺號重號。
- PSE 論文把 candidate 與 commit 分開，並定義 append-only correction。

本篇把這個已觀察結構映射為：

$$
ComputedResult
\neq
CommittedProgramState.
$$

但這只是一種工程映射，不能把跨任務 AI 實驗直接當成一般 CPU/GPU transaction correctness 的證明。

---

# 本篇新提出，不能誤寫成外部來源已有

- Compute Candidate Object（CCO）。
- Semantic-Causal Fence（SCF）。
- Effect Barrier。
- Pure / Reversible / Compensatable / Irreversible 四類 effect。
- Local / Domain / Global Commit 作為 CDI commit scope。
- Recovery Ladder。
- Causal Misalignment heuristic。
- Proof-Carrying Candidate（本文工程用法）。
- AIVS Attention Routing vs Commit State Authority Routing。
- Adaptive Fast Fence / Deep Fence。
