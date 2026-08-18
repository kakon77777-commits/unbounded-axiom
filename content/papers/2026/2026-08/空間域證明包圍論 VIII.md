# 空間域證明包圍論 VIII
## Runtime、Benchmark 與 Proof-Space Observatory
### Spatial-Domain Proof Enclosure VIII: Runtime Semantics, Benchmarks, and a Proof-Space Observatory

**Version:** v0.1  
**Date:** 2026-08-14  
**Status:** Phase-I integration paper / executable reference architecture; not a complete proof assistant and not a claim of universal proof-search acceleration  
**Canonical source:** UTF-8 Markdown; canonical mathematics uses ` $...$ ` and `$$...$$` only.

---

## 摘要

前七篇空間域證明包圍論依序建立：sound survivor contraction、route representation faithfulness、global coverage / closure certificates、proof-trace compilation、Discovery–Verification cost dynamics、measure-zero exceptional-core analysis，以及 cost-aware enclosure routing。這些結果共同提出一個新的工程問題：若研究真的被視為一個持續收縮、可回滾、可重播的 counterexample survivor process，那麼其正式 runtime 狀態、authority boundaries、event history、benchmark semantics 與 observability contract 應如何設計？

本文給出 SDPE Phase I 的第一個整合 runtime。其 canonical state 為

$$
\boxed{
\mathbb S_t
=
\langle
\Omega_t,
RouteCert_t,
\mathbf G_t,
GCC_t,
\mathcal H_t,
Compiled_t,
DVI_t,
SurvProf_t,
RouteDecision_t,
Env_t
\rangle.
}
$$

本文採用 append-only event ledger 與 deterministic reducer。令

$$
\mathcal L_t=(e_0,e_1,\ldots,e_t)
$$

為事件序列，則 authoritative state 由

$$
\boxed{
\mathbb S_t
=
\operatorname{Fold}(\mathcal R,\mathbb S_{-1},\mathcal L_t)
}
$$

重建。由此證明 **Event-Sourced Replay Determinism** 與 **Checkpoint–Tail Equivalence**：只要 reducer、schema、environment fingerprint 與 prefix checkpoint 一致，完整重播與 checkpoint 加 tail replay 產生相同 proof state。

本文進一步建立 **proof-authority separation**。Proposer、Router、Observatory 只可產生 proposal、policy decision 與 telemetry；它們都無權直接縮小 $\Omega_t$ 或設定 $GCC.Valid$。只有通過 verifier、route / representation contract、coverage、boundary、必要 gluing、dependency / version 等 gate 的 certificate，才可由 commit controller 激活並改變 authoritative survivor state。這給出 **Certificate-Gated Commit Preservation**：若初始 survivor sound，且每個 activated exclusion certificate 都是 counterexample-safe，則所有 committed states 永遠保持

$$
\boxed{
\mathcal C\subseteq\Omega_t.
}
$$

本文同時把 Paper 04 的 support-aware rollback 實作成 runtime invariant。certificate 失效時，真正 reopen 的區域只包含失去最後一個 active sound support 的 states，而不是所有曾被該 theorem 觸碰的區域。

在 benchmark 層，本文採納一個更嚴格的分層：kernel proof validity、formal statement fidelity、route / coverage fidelity、runtime reproducibility 與 observatory metrics 分屬不同 authority channels。2026 年對 Lean theorem-proving benchmarks 的 audit 顯示，即使 solution kernel-check 通過，benchmark 本身仍可能包含 vacuity、錯誤 formalization、缺 hypothesis 或 unsound axiom。因此 SDPE benchmark 不允許以「Lean 編譯成功」替代 problem-fidelity audit。

本文提出八條 benchmark tracks：finite closure、representation、global coverage、rollback / replay、DVI、exceptional-core、routing，以及 domain adapter。每個 benchmark 必須 pin problem fingerprint、formalization / adapter version、runtime schema、verifier / kernel version、dependency snapshot、routing policy、model / prover version、hardware / concurrency metadata、random seed 與 audit version。Proof-Space Observatory 可以讀取並顯示 survivor geometry、DVI telemetry、gap debt、routing values、dirty replay 與 support multiplicity，但 observatory 是**非權威**的：任何 dashboard 指標都不能自行提交 theorem cut 或 global closure。

本文最後提供一個標準 Python prototype、JSON state / event / benchmark schemas、append-only example ledger、finite structural checker 與 Hard-Zeta case-study adapter specification。這使 SDPE Phase I 從一組概念論文轉成一個可重播、可 benchmark、可擴充的 proof-space runtime contract。

---

## 關鍵詞

空間域證明包圍；proof runtime；event sourcing；proof-space observatory；Global Closure Certificate；proof provenance；rollback；incremental replay；benchmark fidelity；formal verification；AI theorem proving；proof telemetry；survivor space

---

# 1. Phase I 的整合問題

前七篇回答的問題可以排列為：

$$
\boxed{
\begin{aligned}
&\text{P01: 如何安全縮小反例候選域？}\\
&\text{P02: 如何避免 representation 先丟失 proof-relevant fibers？}\\
&\text{P03: 如何把 local routes 關閉成 global closure？}\\
&\text{P04: 如何編譯 proof history 並做 incremental replay？}\\
&\text{P05: 如何區分 discovery acceleration 與 verification dominance？}\\
&\text{P06: 如何辨認 measure-zero / singular exceptional core？}\\
&\text{P07: 如何選擇下一個研究 action？}
\end{aligned}
}
$$

但若這些對象存在於不同文件、不同 AI session、不同 theorem prover、不同 notebook 或不同版本，它們仍不能形成一個可靠長時程研究系統。

Paper 08 的問題是：

> 如何建立一個最小 runtime，使上述所有 proof objects 具有一致 state semantics、event provenance、authority separation、rollback、replay、benchmark 與 observability？

本文不嘗試建立完整 theorem prover。SDPE Runtime 的角色是**proof-space control plane**：管理證明域、證書、依賴、coverage、routing 與研究 telemetry，而底層 proof checking 可由 Lean、Coq、Isabelle、SMT/SAT certificate checker、domain-specific checker 或人工形式化 audit 承擔。

---

# 2. Fresh literature grounding

## 2.1 Scalable verifier infrastructure

AXLE 在 2026 年把 Lean proof verification、proof manipulation、metadata extraction、多版本支援與 per-request isolation 提升成 scalable cloud infrastructure。這說明 AI mathematics runtime 不應把 verifier 視為單一 `compile` 指令，而應把版本、隔離、request identity、metadata 與 strict verification 當成 first-class runtime state。

SDPE 取其工程原則：

$$
\boxed{
\text{verification service}
\neq
\text{proposal service}.
}
$$

## 2.2 Formal proof validity is not benchmark fidelity

2026 年對五個 Lean theorem-proving benchmarks 的 audit 顯示，kernel-check 只能證明 proof term 證成了 formal statement，不能證明 formal statement 忠實對應 intended problem，也不能保證 benchmark harness 沒有 vacuity、unsound axiom、missing hypotheses 或其它 specification defects。

因此 SDPE 將 benchmark authority 拆成：

$$
\boxed{
\text{Proof Validity}
\neq
\text{Statement Fidelity}
\neq
\text{Coverage Fidelity}
\neq
\text{Performance Telemetry}.
}
$$

## 2.3 Dependency-rich benchmark design

TheoremBench 同時發布 main theorem 與 premise-expanded theorem families，並用 theorem-level coverage / token-efficiency 描述 proof behavior。這支持 SDPE benchmark 不只記錄「最後成功或失敗」，還要保存 dependency / partial progress / closure-obligation structure。

## 2.4 Observable agent loops

OpenProver 將 Planner、Workers、Whiteboard / Repository 與 formal Verifier 分離，並提供 reproducible automatic verification。這與 SDPE authority separation 相容：規劃、生成、儲存與驗證不應由同一個未區分的 agent authority 承擔。

## 2.5 Operational state reuse

Proof-state snapshotting 顯示，重建 elaborated state 可佔 branching search 的主要成本，而直接 reuse state 可以大幅降低 wall time。SDPE 將 snapshot / checkpoint 視為 operational accelerator；它不自動繼承 theorem validity authority。

---

# 3. Canonical SDPE Runtime State

## Definition 3.1 — SDPE State

定義 epoch $t$ 的 runtime state：

$$
\boxed{
\mathbb S_t
=
\langle
\Omega_t,
RouteCert_t,
\mathbf G_t,
GCC_t,
\mathcal H_t,
Compiled_t,
DVI_t,
SurvProf_t,
RouteDecision_t,
Env_t
\rangle.
}
$$

其中：

- $\Omega_t$：authoritative survivor envelope；
- $RouteCert_t$：active route / representation contracts；
- $\mathbf G_t$：typed closure gaps；
- $GCC_t$：Global Closure Certificate state；
- $\mathcal H_t$：proof-history dependency DAG；
- $Compiled_t$：closure basis、support index、snapshots、dirty / reopen state；
- $DVI_t$：Paper 05 cost telemetry；
- $SurvProf_t$：Paper 06 survivor geometry profile；
- $RouteDecision_t$：Paper 07 routing decision / policy provenance；
- $Env_t$：runtime / checker / dependency / model / hardware fingerprints。

## 3.2 Authoritative vs diagnostic fields

將 state fields 分成兩類。

### Proof-authoritative

$$
\boxed{
\Omega_t,
RouteCert_t,
\mathbf G_t,
GCC_t,
\mathcal H_t^{\rm active},
Compiled_t^{\rm support}.
}
$$

### Diagnostic / policy

$$
\boxed{
DVI_t,
SurvProf_t,
RouteDecision_t,
\text{predicted values},
\text{dashboard metrics}.
}
$$

後者可以改變研究排序，不能直接改變數學真值或 closure bit。

---

# 4. Proof Authority Separation

## Definition 4.1 — Authority channels

SDPE Runtime 至少區分：

1. **Proposer**：產生 theorem / refinement / repair candidate；
2. **Router**：排序或選擇 action；
3. **Verifier**：驗證 local certificate；
4. **Coverage Auditor**：驗證 route / branch cover；
5. **Boundary Auditor**：驗證 equality / singular / degenerate strata ownership；
6. **Glue Auditor**：只在 ConstructiveGluing mode 驗證 compatibility / gluing；
7. **Compiler**：建立 proof index / closure basis / snapshot / support map；
8. **Commit Controller**：在 gates 通過後激活 certificate；
9. **Observatory**：只讀 telemetry / visualization。

## Proposition 4.2 — Proposal Non-Authority

若 runtime mutation contract 規定只有 `Commit` / `Invalidate` 類 authority events 能改變 authoritative survivor state，則任意 proposal 或 route-value prediction 都不能單獨推出：

$$
\Omega_{t+1}\subsetneq\Omega_t.
$$

這是系統規格命題，不是數學 theorem：它必須由 runtime enforcement 實作。

## No-Go 4.3 — Model Confidence as Proof Authority

以下都不能激活 theorem cut：

- LLM confidence；
- route score；
- retrieval similarity；
- sampled empirical support；
- observatory anomaly score；
- benchmark historical success rate。

只有 registered proof / audit certificate 可進 commit gate。

---

# 5. Event-Sourced Proof State

## Definition 5.1 — Event Ledger

令 append-only event ledger 為：

$$
\boxed{
\mathcal L_t=(e_0,e_1,\ldots,e_t).
}
$$

每個 event 至少帶有：

$$
\langle
seq,
kind,
payload,
actor,
version,
fingerprint
\rangle.
$$

## Definition 5.2 — Deterministic reducer

令

$$
\mathcal R:
\mathbb S\times\mathcal E\to\mathbb S
$$

為 deterministic reducer。

狀態定義為：

$$
\boxed{
\mathbb S_t
=
\operatorname{Fold}(\mathcal R,\mathbb S_{-1},\mathcal L_t).
}
$$

## Theorem 5.3 — Event-Sourced Replay Determinism

若：

1. initial state 相同；
2. event ledger byte-equivalent / canonically equivalent；
3. reducer version 相同；
4. reducer deterministic；

則 full replay 的 final state 唯一。

### Proof

對 event sequence length induction。零事件時 state 相同。若前 $k$ 個 events 後 state 唯一，由 deterministic $\mathcal R$，第 $k+1$ 個 event 對相同 state 產生唯一 successor。故成立。 $\square$

## Corollary 5.4 — State fingerprint

若 state 使用 canonical serialization，可定義：

$$
\boxed{
F_t
=
H(\operatorname{Canon}(\mathbb S_t)).
}
$$

不同 machine / session replay 應得到相同 fingerprint，否則 runtime / environment drift 必須被視為 verification event。

---

# 6. Checkpoint–Tail Replay

對長時程研究，不應每次從 event 0 完整重播。

令 prefix ledger：

$$
\mathcal L_{0:k}
$$

產生 checkpoint：

$$
\widehat{\mathbb S}_k.
$$

## Theorem 6.1 — Checkpoint–Tail Equivalence

若 checkpoint 經完整 prefix replay 驗證，且 reducer / schema / environment fingerprint 未變，則：

$$
\boxed{
\operatorname{Fold}(\mathcal R,\mathbb S_{-1},\mathcal L_{0:t})
=
\operatorname{Fold}(\mathcal R,\widehat{\mathbb S}_k,\mathcal L_{k+1:t}).
}
$$

### Proof

由 fold associativity 與 checkpoint 定義立即成立。 $\square$

## No-Go 6.2 — Snapshot Equals Certificate

checkpoint 只證明：「在指定 reducer / environment 下可以重建這個 state」。

它不證明 checkpoint 內每個 theorem / route / coverage certificate 的數學正確性。certificate authority 仍由其原始 checker / dependency provenance 承擔。

---

# 7. Certificate-Gated Commit

## Definition 7.1 — Commit gate

令 candidate certificate $c$ 要進 active state，至少要求：

$$
\boxed{
\begin{aligned}
&\mathsf{ProposalExists}(c),\\
&\mathsf{LocalVerify}(c)=\mathrm{pass},\\
&\mathsf{DepsActive}(c),\\
&\mathsf{VersionMatch}(c),\\
&\mathsf{RouteLiftValid}(c),\\
&\mathsf{RequiredAuditsValid}(c).
\end{aligned}
}
$$

若 conclusion 要提交 global closure，還需要 Paper 03 的 GCC obligations。

## Theorem 7.2 — Certificate-Gated Survivor Preservation

設初始 state 滿足：

$$
\mathcal C\subseteq\Omega_0.
$$

若每一個 committed exclusion certificate $c$ 排除的 region $E_c$ 都已 soundly 證明：

$$
E_c\cap\mathcal C=\varnothing,
$$

且 committed survivor update 為：

$$
\Omega_{t+1}
=
\Omega_t\setminus
\bigcup_{c\in A_t}E_c,
$$

則所有 committed epochs 保持：

$$
\boxed{
\mathcal C\subseteq\Omega_t.
}
$$

### Proof

若 $x\in\mathcal C$，由 induction hypothesis $x\in\Omega_t$。又對所有 committed $c$， $x\notin E_c$。故 $x\in\Omega_{t+1}$。 $\square$

## 7.3 GCC bit 的語義

`GCC.Valid = true` 本身不是 proof artifact。它只是一個 runtime result bit，其可置信性來自：

$$
\boxed{
\text{event replay}
+
\text{active certificate basis}
+
\text{cover / boundary / glue obligations}
+
\text{environment fingerprints}.
}
$$

因此最終 publication / submission 應附 closure basis / proof artifacts，而不是只附一個 runtime JSON flag。

---

# 8. Invalidation, Dirty State, and Precise Reopening

Paper 04 定義 support multiplicity：

$$
\kappa_t(x)
=
\#\{c:x\in E_c,\;c\text{ active}\}.
$$

certificate 失效後：

$$
\boxed{
R
=
\{x:\kappa_{\rm old}(x)>0,\;\kappa_{\rm new}(x)=0\}.
}
$$

## Proposition 8.1 — Precise support-aware reopen

若 support index complete，則 certificate invalidation 後：

- $\kappa_{\rm new}(x)>0$ 的 point 仍有 sound active exclusion support，不需 reopen；
- $\kappa_{\rm new}(x)=0$ 且 previously excluded 的 point 必須 reopen。

這是 stale theorem 局部化修復的 runtime realization。

## 8.2 Dependency dirty closure

對失效 proof node $v$：

$$
Dirty(v)
=
\{v\}\cup\operatorname{Desc}(v).
$$

只有 dirty closure 與其受影響 coverage / GCC nodes 需要 incremental replay。

---

# 9. Typed Gap API

Paper 03 / 06 / 07 的 gaps 在 runtime 中至少分為：

$$
\boxed{
\mathbf G
=
(G_D,G_B,G_{\partial},G_C,G_G,G_R,G_{\rm core},G_{\rm repr}).
}
$$

典型 API：

- `register_gap(type, scope, witness, mandatory, dependencies)`；
- `resolve_gap(gap_id, certificate_id)`；
- `reopen_gap(gap_id, stale_dependency)`；
- `query_persistent_gaps()`；
- `query_starvation_age(gap_id)`。

Gap priority 是 routing policy；gap closure 是 certificate semantics。二者不得混淆。

---

# 10. Route API

每個 route 至少帶有：

$$
\boxed{
RouteCert
=
\langle
Scope,
Representation,
FiberPolicy,
Lift,
Boundary,
Dependencies,
Version,
Replay
\rangle.
}
$$

runtime 應提供：

- `register_route_cert`；
- `invalidate_route_cert`；
- `refine_representation`；
- `query_singular_fibers`；
- `query_route_coverage`。

任何 route representation 改版都應使依賴舊 representation fingerprint 的 certificates 進 dirty state。

---

# 11. Proof DAG and Closure-Basis API

proof DAG node 至少保存：

$$
\boxed{
\langle
Stmt,
Scope,
Deps,
Route,
Version,
Fingerprint,
Checker,
Payload,
Region,
Status
\rangle.
}
$$

runtime API：

- `add_verified_certificate`；
- `active_ancestors`；
- `closure_basis(target)`；
- `invalidate_certificate`；
- `dirty_closure`；
- `incremental_replay`；
- `support_index(region)`。

---

# 12. Proof-Space Observatory

## Definition 12.1 — Observatory

Proof-Space Observatory 是 state / event 的只讀 projection：

$$
\boxed{
\mathsf{Obs}_t
=
\Psi(\mathbb S_t,\mathcal L_t).
}
$$

其輸出可以包括：

$$
D_t^{\rm resolve},
\quad
D_t^{\rm frontier},
\quad
W_t,
\quad
\sigma_t,
\quad
h_t,
\quad
\chi_t,
\quad
|Dirty_t|,
\quad
|R_t|,
$$

以及：

$$
SurvProf_t,
\quad
\mathbf G_t,
\quad
RouteValue_t,
\quad
support\ multiplicity,
\quad
certificate\ debt.
$$

## Theorem 12.2 — Observatory Non-Authority

若 runtime mutation rules 不接受 observatory output 作 proof-authoritative event，則 observatory telemetry 的任意改變不能單獨改變：

$$
\boxed{
\Omega_t
\quad\text{或}\quad
GCC_t.Valid.
}
$$

這是安全架構原則：

$$
\boxed{
\text{measurement}
\neq
\text{mathematical authority}.
}
$$

---

# 13. Runtime Pipeline

Phase-I reference pipeline：

$$
\boxed{
\begin{aligned}
&\mathsf{Detect}\\
&\to\mathsf{Profile}\\
&\to\mathsf{GapExtract}\\
&\to\mathsf{ActionGenerate}\\
&\to\mathsf{Route}\\
&\to\mathsf{Propose}\\
&\to\mathsf{Verify}\\
&\to\mathsf{CoverageAudit}\\
&\to\mathsf{BoundaryAudit}\\
&\to\mathsf{GlueAudit}\\
&\to\mathsf{Compile}\\
&\to\mathsf{Commit}.
\end{aligned}
}
$$

這不是強迫所有 domain 逐步執行每一 stage。RefutationOnly problem 可以讓 GlueAudit 返回 `not-required` certificate；沒有 representation change 的 epoch 可以略過 refine action；但**所有被略過的 authority gate 必須有明確的 not-applicable semantics**，不能靠 silent omission。

---

# 14. Benchmark Authority Separation

Formal theorem benchmark 至少有四層 correctness：

## 14.1 Proof validity

底層 kernel / checker 接受 proof artifact。

## 14.2 Statement fidelity

formal statement 是否忠實代表 intended mathematical problem。

## 14.3 Closure / route fidelity

local cases 是否真正 cover domain、representation 是否 sound、boundaries 是否有 ownership。

## 14.4 Evaluation fidelity

metric / harness 是否沒有 leakage、vacuity、shortcut、version mismatch 或不公平 cost accounting。

因此：

$$
\boxed{
\text{proof checks}
\not\Rightarrow
\text{benchmark is sound}.
}
$$

這一點不是理論上的杞人憂天；2026 benchmark audit 已在現有 Lean benchmarks 中機械發現多種問題。

---

# 15. SDPE Benchmark Tracks

本文定義八條最小 tracks。

## Track A — Finite Closure

有限 universe 有 hidden oracle。測：

- survivor soundness；
- theorem cut；
- cover certificate；
- GCC；
- false closure rejection。

## Track B — Representation

測：

- fiber saturation；
- mixed-fiber retention；
- route refinement；
- lift certificate。

## Track C — Global Coverage

測：

- branch union；
- boundary omission；
- overlap；
- RefutationOnly / ConstructiveGluing mode。

## Track D — Rollback / Replay

測：

- stale dependency；
- dirty closure；
- support-aware reopen；
- full vs incremental replay；
- checkpoint equivalence。

## Track E — DVI

沿用 Paper 05：

- Queue A known / replay；
- Queue B near-frontier transfer；
- Queue C true frontier；
- cold vs compiled；
- build / maintenance / replay cost。

## Track F — Exceptional Core

測：

- measure-zero survivor；
- singleton localization；
- theorem-language irreducible core；
- representation-singular residue。

## Track G — Routing

測：

- volume greedy；
- gap-aware；
- bridge-aware；
- Pareto routing；
- fairness；
- time-to-GCC。

## Track H — Domain Adapter

將真實數學研究映射成 SDPE objects，例如：

- Hard-Zeta / Collatz；
- SAT / cube-and-conquer；
- finite graph classification；
- repository-scale Lean verification。

Domain adapter benchmark 不應假裝 hidden oracle 存在；它主要測 provenance、state reconstruction、routing、certificate integration 與 research telemetry。

---

# 16. Benchmark Fingerprints

每次 run 至少 pin：

$$
\boxed{
\begin{aligned}
&ProblemHash,\\
&StatementHash,\\
&AdapterVersion,\\
&RuntimeSchema,\\
&ReducerVersion,\\
&VerifierVersion,\\
&DependencySnapshot,\\
&RoutePolicyVersion,\\
&ModelVersion,\\
&HardwareProfile,\\
&Seed,\\
&AuditVersion.
\end{aligned}
}
$$

定義 benchmark identity：

$$
\boxed{
BenchID
=
H(
ProblemHash\Vert
EnvHash\Vert
SchemaHash\Vert
PolicyHash\Vert
Seed
).
}
$$

若這些 fingerprint 不同，runtime 可以比較結果，但不得把它們默認當成同一 experimental condition。

---

# 17. Benchmark Metrics

## 17.1 Correctness metrics

- false exclusion count；
- false GCC count；
- missed reopen count；
- stale certificate activation count；
- route / boundary omission count。

在 sound benchmark 中，proof-authoritative false-positive 應要求：

$$
\boxed{0.}
$$

## 17.2 Replay metrics

- full replay time；
- checkpoint-tail replay time；
- dirty replay fraction；
- state fingerprint mismatch rate。

## 17.3 Compilation metrics

- compiled hit rate $h$ ；
- closure-basis compression $\chi$ ；
- support multiplicity；
- reopen precision；
- build / maintenance cost。

## 17.4 Closure metrics

- active mandatory gap count；
- boundary debt；
- certificate debt；
- time-to-GCC；
- accepted nonredundant cut count。

## 17.5 DVI metrics

沿用：

$$
D^{\rm resolve},
D^{\rm frontier},
W,
\sigma,
G^{\rm compile},
P^{\rm drift}.
$$

## 17.6 Routing metrics

- nonredundant closure yield；
- action cost；
- routing regret；
- mandatory-gap starvation age；
- bridge unlock rate。

---

# 18. Runtime Replay Theorems and Their Boundaries

Event-sourced determinism 證明的是：

$$
\boxed{
\text{same validated history}
\to
\text{same runtime state}.
}
$$

它**不證明**：

$$
\boxed{
\text{the history itself is mathematically valid}.
}
$$

同樣：

$$
\boxed{
\text{incremental replay = full replay}
}
$$

只在 dependency metadata、checker determinism、version fingerprints 完整的 runtime contract 下成立。

因此 runtime theorem 與 mathematical theorem 必須分層記帳。

---

# 19. Benchmark-Fidelity Gate

在正式 benchmark acceptance 前，至少要求：

1. statement fidelity audit；
2. proof-kernel / checker version pinned；
3. banned axioms / shortcuts policy declared；
4. dependency graph audited；
5. test harness replayable；
6. environment fingerprint complete；
7. hidden oracle 只在 toy / synthetic track 使用；
8. metric authority 不超過其定義範圍。

## No-Go 19.1 — Kernel-Checked Means Benchmark-Correct

錯。

kernel 只回答：

> 這個 proof term 是否證成這個 formal statement？

它不回答：

> 這個 formal statement 是否忠實翻譯 intended problem？

也不回答：

> benchmark route / coverage / cost protocol 是否公平？

---

# 20. Hard-Zeta Adapter as a Case-Study Interface

SDPE Runtime 不重新證明 Hard-Zeta 的任何 theorem。adapter 只規定如何映射已存在的研究 artifacts。

可將 B-side frontier branches 映射成：

$$
G_B
$$

與 route nodes；把每個 theorem / no-go / reduction 放入 proof DAG；把 survivor parameter inequalities 存成 symbolic constraint payload；把 checker / JSON / literature provenance 綁到 certificate nodes；把 `Sparse / Huge-PQ / structured survivor ladder` 等 branch frontier 當作 typed gaps / route obligations。

任何 numerical exponent、checker PASS 或 paper statement 都只有在其 upstream proof certificate 被正式接入 runtime 後，才可對 authoritative survivor state 產生作用。

因此 adapter 不是「把聊天紀錄直接變 proof」，而是：

$$
\boxed{
\text{research artifacts}
\to
\text{typed candidates}
\to
\text{verification}
\to
\text{certificate nodes}
\to
\text{committed SDPE state}.
}
$$

---

# 21. Reference Prototype

本 bundle 提供：

- `sdpe_runtime.py`：deterministic event reducer；
- `SDPE_State_Schema_v1.json`；
- `SDPE_Event_Schema_v1.json`；
- `SDPE_Benchmark_Schema_v1.json`；
- `example_finite_closure_run.jsonl`；
- `example_final_state.json`；
- `verify_SDPE_Paper08_runtime.py`；
- Hard-Zeta adapter specification。

prototype 刻意保持簡單：finite explicit survivor universe 用於 structural checker；真正 infinite / symbolic mathematics 必須由 domain adapter 與外部 proof checker 提供 sound symbolic region semantics。

---

# 22. Structural Checker Results

companion checker 驗證：

1. reference ledger replay 到 empty survivor + valid GCC；
2. $1500$ 組 random event histories deterministic replay；
3. $1500$ 組 checkpoint-tail equivalence；
4. $1500$ 組 hidden-oracle survivor soundness；
5. proposal non-authority；
6. telemetry non-authority；
7. unverified-certificate commit rejection；
8. redundant-support rollback precision；
9. GCC authority separation。

checker 只驗證 finite runtime semantics，不驗證 arbitrary mathematical certificate 的內容真偽。

---

# 23. No-Go Ledger

## No-Go 23.1 — Runtime State Equals Mathematical Truth

runtime 只能攜帶 certificate-backed belief state；真理不由 database bit 創造。

## No-Go 23.2 — Proposer Can Commit Its Own Result

proposal / verification / commit 必須 authority-separated。

## No-Go 23.3 — Observatory Metric Can Close Proof

telemetry 沒有 proof authority。

## No-Go 23.4 — Kernel Acceptance Guarantees Statement Fidelity

formal proof validity 與 intended-problem fidelity 是不同 obligations。

## No-Go 23.5 — Checkpoint Is a New Proof

checkpoint 是 replay accelerator，不是新增 theorem。

## No-Go 23.6 — Event Replay Repairs Missing Dependencies

若 dependency metadata 本身不完整，deterministic replay 只能穩定重現錯誤 state。

## No-Go 23.7 — JSON Schema Proves Semantics

schema 只保證 shape；route / theorem / coverage soundness 需要各自 certificate。

## No-Go 23.8 — A Benchmark Score Is a Proof-Space Law

benchmark 只能支持被其 design / controls 覆蓋的 empirical claim。

## No-Go 23.9 — Domain Adapter Imports Proof Automatically

adapter 只做 typed mapping；原 artifacts 必須驗證後才能 commit。

## No-Go 23.10 — Phase-I Runtime Is a Complete Proof Assistant

不是。它是 proof-space orchestration / audit layer。

---

# 24. Theorem / System-Assumption / External-Input Ledger

## 24.1 Internal runtime theorems / propositions

1. Event-Sourced Replay Determinism；
2. Checkpoint–Tail Equivalence；
3. Proposal Non-Authority under enforced mutation rules；
4. Certificate-Gated Survivor Preservation；
5. Precise Support-Aware Reopen under complete support index；
6. Observatory Non-Authority；
7. Benchmark Identity under canonical fingerprints。

## 24.2 Inherited SDPE theorems

- P01 survivor soundness；
- P02 representation faithfulness；
- P03 global cover / GCC；
- P04 closure basis / rollback / incremental replay；
- P05 DVI cost architecture；
- P06 exceptional-core semantics；
- P07 enclosure routing。

## 24.3 Runtime correctness assumptions

1. event ledger append-only / tamper-evident；
2. reducer deterministic；
3. canonical serialization stable；
4. certificate checker identity / version pinned；
5. dependency metadata complete；
6. support index complete；
7. authority boundaries enforced；
8. benchmark formalization audit honest and versioned。

## 24.4 External grounding

- AXLE scalable strict Lean infrastructure；
- 2026 formal benchmark fault audit；
- TheoremBench dependency-rich benchmark structure；
- OpenProver Planner / Worker / Verifier runtime；
- Lean proof-state snapshotting；
- testing-style semantic evaluation of formal statements。

---

# 25. Phase-I Closure

八篇形成第一階段完整 stack：

$$
\boxed{
\begin{aligned}
&\text{P01 Survivor Soundness}\\
&\downarrow\\
&\text{P02 Representation Faithfulness}\\
&\downarrow\\
&\text{P03 Global Coverage / Closure}\\
&\downarrow\\
&\text{P04 Trace Compilation / Incremental Replay}\\
&\downarrow\\
&\text{P05 Discovery--Verification Dynamics}\\
&\downarrow\\
&\text{P06 Exceptional-Core Geometry}\\
&\downarrow\\
&\text{P07 Cost-Aware Enclosure Routing}\\
&\downarrow\\
&\text{P08 Runtime / Benchmark / Proof-Space Observatory}.
\end{aligned}
}
$$

Phase I 現在不再只是「一套想法」；它具有：

- proof-space semantics；
- closure obligations；
- representation contracts；
- event provenance；
- certificate / dependency state；
- rollback / replay；
- cost telemetry；
- routing semantics；
- benchmark protocol；
- executable finite prototype。

---

# 26. Final Status

Paper 08 的核心原則可以壓縮成五句。

第一：

$$
\boxed{
\text{SDPE state 應由可重播 event history 重建，而不是依賴聊天記憶。}
}
$$

第二：

$$
\boxed{
\text{proposal、prediction、telemetry 都沒有 proof commit authority。}
}
$$

第三：

$$
\boxed{
\text{verified certificate + global obligations 才能改變 authoritative survivor state。}
}
$$

第四：

$$
\boxed{
\text{benchmark 必須同時驗證 proof、statement、coverage 與 environment fidelity。}
}
$$

第五：

$$
\boxed{
\text{proof-space observability 應提高研究可理解性，但不能反過來成為數學真理來源。}
}
$$

因此，空間域證明包圍第一階段現在形成一個完整迴圈：

$$
\boxed{
\text{Detect}
\to
\text{Enclose}
\to
\text{Route}
\to
\text{Propose}
\to
\text{Verify}
\to
\text{Audit}
\to
\text{Compile}
\to
\text{Commit}
\to
\text{Observe}
\to
\text{Detect again}.
}
$$

它仍然不能保證任意猜想會被證明；但它把「長期 AI 輔助數學研究如何留下可驗證痕跡、如何安全收縮反例域、如何避免局部正確冒充全域閉合、如何重用歷史、如何辨認 exceptional hard core、如何選下一刀、如何 benchmark 整個過程」統一成了一個可執行的 proof-space architecture。

---

# References

1. Jimmy Xin, Alex Schneidman, Chris Cummins, Karun Ram, Srihari Ganesh, Jannis Limperg, **AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities**, arXiv:`2606.26442`, 2026.
2. Pawan Sasanka Ammanamanchi, Siddharth Bhat, Stella Biderman, **Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving**, arXiv:`2606.29493`, 2026.
3. QuocViet Pham, Elvir Karimov, Andrey Galichin, Ivan Oseledets, **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics**, arXiv:`2606.09450`, 2026.
4. Matěj Kripner, Milan Straka, **OpenProver: Agentic and Interactive Theorem Proving with Lean 4**, arXiv:`2607.09217`, 2026.
5. Austin Shen, Yunong Shi, **Keep the Proof State Live: Snapshotting for Efficient Tactic Search in Lean 4**, arXiv:`2605.25556`, 2026.
6. Jongyoon Kim, Hojae Han, Seung-won Hwang, **Benchmarking Testing in Automated Theorem Proving**, arXiv:`2604.23698`, 2026.
7. Prior SDPE artifacts: Papers 01--07.
