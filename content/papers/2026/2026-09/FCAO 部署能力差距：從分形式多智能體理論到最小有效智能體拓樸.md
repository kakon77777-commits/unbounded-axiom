# FCAO 部署能力差距：從分形式多智能體理論到最小有效智能體拓樸
## The Deployment Capability Gap of FCAO: From Fractal Multi-Agent Theory to Minimal Effective Agent Topologies

**系列：** FCAO / Fractal Conversational Agent Organization  
**文件編號：** EML-FCAO-2026-03-v0.1  
**文件類型：** Theory Boundary / Deployment Readiness / Empirical Correction Paper  
**作者：** Neo.K  
**協作：** AI Research Assistant  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-25  
**狀態：** Research Draft / Public-Release Candidate  
**直接前置：**
- `EML-FCAO-2026-00-v0.1` — FCAO Foundation / Integration Paper
- `EML-FCAO-2026-01-v0.1` — Twin-Agent Governance
- `EML-FCAO-2026-02-v0.1` — Temporal-Topological Computation
- `EML-FCAO-RA-2026-v0.1` — FCAO Twin-Core Reference Architecture
- FCAO + APR Operational Experiment 01
- Recent operator-observed native subagent-driven development cases

**公開隱私規則：** 本文不保留任何 AI 個體名稱。所有 AI 一律以 `Primary AI`、`Twin AI`、`Implementation Agent`、`Reviewer`、`Experience Agent`、`Child Agent` 等角色表示。原始 evidence 可在私有研究封存中保留，但公開文本不得反推出 AI 個體名稱。

---

# 摘要

FCAO 的前三篇理論文提出：一段 Conversation 可以形成 temporary local computational world；Primary AI 可以在其中建立 Named Ephemeral Agents、遞歸委任、task / verification topology、Primary–Twin 雙核心治理與 dynamic repartition。這些命題描述的是一個可擴張的 agentic organization architecture，而不是對特定年代模型與 runtime 的部署保證。

2026 年的初步實作與操作紀錄顯示，這個區分必須被明確寫入 FCAO 系列。高密度 child-agent fan-out 在當前條件下可能帶來實質可靠性收益，例如獨立 reviewer 可以發現局部實作者未察覺的 security、lifecycle、mapping、receipt 或 packaging 問題；但同時也反覆出現 context projection loss、temporal desynchronization、state synchronization gap、verification amplification、integration overhead 與 compute misallocation。結果可能形成：

$$
N_{\mathrm{agents}}\uparrow
\quad\land\quad
Q\uparrow
\quad\land\quad
T_{\mathrm{wall}}\uparrow\uparrow
\quad\land\quad
C_{\mathrm{compute}}\uparrow\uparrow,
$$

其中品質改善並不足以在所有任務上抵銷時間與計算成本。

與此相對，FCAO + APR 的一個 operational experiment 在 `Single` topology、`0` child / subagent 條件下完成真實 workspace consolidation 與 GitHub synchronization。該 world 記錄 32 個事件、4/4 tasks completed、2 個 closure records、final coverage `1.0` 與 valid replay；Twin 可以保持 `IDLE`，必要時才 `CHALLENGE`，APR 對已驗證事實回傳 `NO_OBSERVATION`。這並未證明 Single topology 普遍優於 multi-agent，但至少證明「不 fan-out」可以是一個正式、可治理、可驗證的成功拓樸，而不是 agentic system 的退化模式。

另一個近期 operator-observed native subagent-driven case 在規格已批准後仍執行約 4 小時 11 分 13 秒，最終 243/243 tests 通過，而唯一剩餘的人類決策是是否增加第六個 stable public error code。該案例顯示 review-intensive workflow 可能高度優化 defect containment，卻不一定同時優化 throughput。此觀察尚未經統一 telemetry instrumentation，因此本文只將其視為 deployment signal，而非效能定理。

本文因此提出 FCAO 的 **Deployment Capability Gap**：

$$
\boxed{
FCAO_{\mathrm{theory}}
\neq
FCAO_{\mathrm{recommended\ deployment\ in\ 2026}}.
}
$$

本文不撤回 recursive / fractal multi-agent architecture；相反地，將其保留為 FCAO 的 theoretical capability envelope。對 2026 年可部署策略，本文提出 **Minimal Effective Agent Topology** 原則：

$$
\boxed{
\mathcal T^\star
=
\arg\min_{\mathcal T}
Cost(\mathcal T)
}
$$

subject to：

$$
Quality(\mathcal T)\ge Q_{\min},
$$

$$
Risk(\mathcal T)\le R_{\max},
$$

$$
Experience(\mathcal T)\ge E_{\min}.
$$

目前建議的實作階梯為：

$$
\boxed{
Single
\rightarrow
Primary+Twin
\rightarrow
Builder+Verifier+Experience
}
$$

而 recursive child delegation、dense multi-agent fan-out、local twins 與 dynamic repartition 應標記為 experimental / future-capability path，除非候選任務已證明：

$$
ExpectedParallelGain
>
ContextTransfer
+
Coordination
+
Verification
+
Integration.
$$

本文的目的不是宣稱多智能體理論錯誤，而是避免 FCAO 在未來公開發表時被誤解為「現階段應優先啟用大量子 Agent」的產品建議。

**關鍵詞：** FCAO、Deployment Capability Gap、Minimal Effective Agent Topology、Strong Primary First、Twin Governance、Context Fragmentation、Temporal Desynchronization、Subagent Overhead、Verification Amplification、APR、Agent Topology

---

# 1. 問題：理論能力與部署能力被混成同一句話

FCAO Foundation 的核心之一是：

$$
A_i
\rightarrow
\{A_{i1},A_{i2},\ldots,A_{ik}\}.
$$

這表示一個 Agent 可以在局部 world 內進一步形成 recursive organization。

但：

$$
\boxed{
CanInstantiateRecursiveAgents
\not\Rightarrow
ShouldInstantiateRecursiveAgentsNow.
}
$$

如果公開文件只呈現架構能力，沒有 deployment readiness boundary，讀者很容易把：

> FCAO 可以建立遞歸多 Agent 拓樸

讀成：

> FCAO 建議現在的複雜專案直接 fan-out 成大量子 Agent。

這兩句不是同一命題。

因此本文將 FCAO 分成：

$$
FCAO_{\mathrm{ontology}},
$$

$$
FCAO_{\mathrm{governance}},
$$

$$
FCAO_{\mathrm{deployment}}.
$$

前兩者描述「系統可以如何組織」；第三者回答「在當代 runtime 條件下應該啟用多少組織」。

---

# 2. 本文不撤回哪些命題

本文不撤回：

1. Conversation 可以形成 temporary local computational world；
2. Agent 可以遞歸生成 child / specialist；
3. Primary–Twin 可以形成雙核心治理；
4. verification topology 是 task topology 的一部分；
5. decomposition 可以動態重分區；
6. local closure 不等於 global closure；
7. child delegation 可以在某些任務上降低 wall-clock；
8. 未來 shared state / memory / scheduler 改善後，fractal multi-agent 可能具有更高實用價值。

本文只修正：

$$
\boxed{
DeploymentDefault.
}
$$

---

# 3. 當前實例首先否定的是「Agent 數量崇拜」

當前常見 agentic intuition：

$$
HardTask
\Rightarrow
MoreAgents.
$$

FCAO 現在應明確拒絕此推論。

正確形式應為：

$$
HardTask
\Rightarrow
EstimateTopology.
$$

而合法結果之一永遠是：

$$
\boxed{
NO\_SPLIT.
}
$$

因此：

$$
\boxed{
AgentCount
}
$$

不是成功指標。

真正關心的是：

$$
NetUsefulWork,
$$

$$
WallClock,
$$

$$
ComputeCost,
$$

$$
DefectEscape,
$$

$$
Rework,
$$

$$
ClosureQuality.
$$

---

# 4. 2026 Deployment Gap Vector

本文定義第一代能力差距向量：

$$
\Gamma_{2026}
=
(
\Gamma_C,
\Gamma_T,
\Gamma_S,
\Gamma_A,
\Gamma_V,
\Gamma_M
).
$$

其中：

- $\Gamma_C$：Context Gap；
- $\Gamma_T$：Temporal Synchronization Gap；
- $\Gamma_S$：Canonical State Synchronization Gap；
- $\Gamma_A$：Compute Allocation Gap；
- $\Gamma_V$：Verification Amplification Gap；
- $\Gamma_M$：Merge / Semantic Reconciliation Gap。

只要這些 gap 沒有顯著下降，高密度 multi-agent 的理論 parallelism 就可能被 orchestration overhead 吃掉。

---

# 5. Context Gap

Primary 的世界投影：

$$
\pi_P(W)
$$

通常大於 child 的任務投影：

$$
\pi_i(W).
$$

因此：

$$
\pi_i(W)
\subset
\pi_P(W).
$$

當必要 global constraints 沒被正確投影時，會出現：

$$
\boxed{
Delegation
\rightarrow
ProjectionLoss
\rightarrow
LocalError
\rightarrow
ParentRepair.
}
$$

某次 native multi-agent development record 中，review 階段明確發現：task brief 沒有攜帶應鎖定的 global constants，child 因而將多個必要 adoption facts 寫成 `null`。這種錯誤不是單純「child 不夠聰明」，而是 delegation 本身創造了 information boundary。

因此：

$$
\boxed{
ContextTransferCost
}
$$

不只是 token 數量，而包含「哪些不能遺失的全域不變量是否真的被送到」。

---

# 6. Temporal Synchronization Gap

多 Agent 系統中的每個節點都位於不同 local time：

$$
S_P(t)
\neq
S_{C_1}(t)
\neq
S_{C_2}(t).
$$

當 Primary 已更新 architecture、constraint 或 evidence，而 child 還在舊 state 執行，便會形成：

$$
StaleWork.
$$

長時間工作尤其容易出現：

- worker 還在舊 spec；
- reviewer 正在審已被 supersede 的 artifact；
- fixer 修的是前一輪 finding；
- integration state 已經改變；
- external branch / release state 已更新。

所以：

$$
\boxed{
ParallelAgents
}
$$

並不自動等於：

$$
\boxed{
SharedPresent.
}
$$

---

# 7. Canonical State Synchronization Gap

理論上：

$$
AllAgents
\leftrightarrow
CanonicalWorldState.
$$

但當代很多 agentic workflow 仍高度依賴：

- prompt；
- summary；
- handoff；
- task brief；
- message；
- local scratchpad。

若 state 主要靠自然語言同步，就會出現：

$$
StateDrift.
$$

FCAO 的 SQLite / event ledger、LCC、GCC、APR evidence 等設計正是為了降低這個 gap，但 production-grade cross-agent shared state 尚未被完整證明。

---

# 8. Compute Allocation Gap

增加 Agent 數量不代表算力被最佳化。

當前常見情況：

$$
Spawn(A_i)
\Rightarrow
FullModelInvocation.
$$

但真正需要的是：

$$
Allocate(
Model,
Reasoning,
Context,
Tool,
Time,
Verification
).
$$

簡單 verification 若使用與 Primary 同等高成本 inference，或多個 Agent 重複載入大 context：

$$
C_{\mathrm{duplicate}}
\uparrow.
$$

所以：

$$
\boxed{
MoreCompute
\neq
BetterComputeAllocation.
}
$$

---

# 9. Verification Amplification Gap

multi-agent 的一個真實收益是獨立 review。

近期工作紀錄顯示 reviewer 實際發現：

- authority / scope boundary；
- TOCTOU；
- Windows path collision；
- lifecycle cleanup；
- mapping omission；
- protocol mismatch；
- receipt auditability；
- event-ordering bug。

這些 finding 有實質價值。

但同一流程也出現：

$$
Implement
\rightarrow
Review
\rightarrow
Fix
\rightarrow
ReReview
\rightarrow
ResidualFix
\rightarrow
ReReview.
$$

因此要區分：

$$
\boxed{
VerificationValue
}
$$

與：

$$
\boxed{
VerificationAmplification.
}
$$

如果 review 每次都開啟新的 review surface：

$$
C_{\mathrm{verify}}^{(n+1)}
>
0
$$

且沒有適當 stop policy，總成本可能快速增長。

---

# 10. Merge / Semantic Reconciliation Gap

即使：

$$
LCC_1=LCC_2=\cdots=LCC_n=1,
$$

也不代表：

$$
GCC=1.
$$

原因包括：

- duplicate abstraction；
- incompatible assumptions；
- shared-state conflict；
- overlapping authority；
- inconsistent schema；
- different temporal state；
- hidden dependency。

所以高 fan-out 的最後成本不是單純 concatenate outputs，而是：

$$
C_{\mathrm{merge}}
=
C_{\mathrm{semantic}}
+
C_{\mathrm{conflict}}
+
C_{\mathrm{verification}}
+
C_{\mathrm{repair}}.
$$

當：

$$
C_{\mathrm{merge}}
>
ParallelGain,
$$

fan-out 就失去意義。

---

# 11. Operational Evidence A：Single Topology 可以是完整治理模式

FCAO + APR Operational Experiment 01 刻意使用：

$$
Topology=Single
$$

與：

$$
N_{\mathrm{child}}=0.
$$

結果記錄：

- 32 events；
- 4/4 tasks completed；
- 2 closure records；
- final coverage `1.0`；
- replay verification valid。

Twin 決策可以是：

$$
IDLE
\rightarrow
CHALLENGE
\rightarrow
CONCUR
\rightarrow
CHALLENGE
\rightarrow
CONCUR.
$$

APR 對已驗證事實可以：

$$
NO\_OBSERVATION.
$$

這至少證明：

$$
\boxed{
SingleTopology
\neq
NoGovernance.
}
$$

也就是：

> 不開 child Agent 不等於放棄 agentic architecture。

---

# 12. Operational Evidence B：高驗證工作流可以得到高品質，也可以非常慢

另一個 native subagent-driven development record 顯示：

- 多次 reviewer；
- 多次 fix round；
- scoped re-review；
- residual cycle；
- security re-review；
- whole-branch review；
- independent rerun；
- release 後再驗證。

最終確實得到大量通過測試與更強 evidence。

所以本文不將其描述為失敗。

更準確地：

$$
\boxed{
Reliability\uparrow
}
$$

但：

$$
\boxed{
WorkflowDepth\uparrow
}
$$

與：

$$
\boxed{
WallClock\uparrow.
}
$$

因此 deployment policy 必須知道使用者究竟在優化：

$$
ZeroDefect?
$$

還是：

$$
UsefulProductPerHour?
$$

---

# 13. Operator-Observed Evidence C：規格已批准仍可能出現 late governance discovery

另一個近期網站 / local MCP implementation case：

- 已有批准規格；
- 執行約 4 小時 11 分 13 秒；
- 243/243 tests passing；
- final-review 後只剩一個公開 API 決策；
- 該決策是新增一個語義上合理、但超出已批准 stable error-code set 的新 error code。

這個 stop 是合理的：

$$
PublicAPIChange
\Rightarrow
HumanAuthority.
$$

但值得研究的是：

$$
\boxed{
WhyWasTheConflictDetectedSoLate?
}
$$

如果 capacity semantics 在規格解析階段就能發現：

$$
Spec
\rightarrow
ConflictDetection
\rightarrow
AskHuman
\rightarrow
Implementation,
$$

就不必在 4 小時後才到：

$$
FinalFixer
\rightarrow
PublicAPIDecision.
$$

本文將此稱為：

$$
\boxed{
LateGovernanceDiscovery.
}
$$

---

# 14. 本文不主張這些案例已形成統計學結論

目前資料不具備：

- 統一硬體；
- 統一模型成本；
- 統一 token accounting；
- 隨機化 assignment；
- 相同專案的多次重複；
- 完整 wall-clock instrumentation；
- 同一品質基準下的 controlled A/B test。

因此：

$$
\boxed{
Observation
\neq
UniversalPerformanceProof.
}
$$

本文只據此調整 deployment recommendation。

---

# 15. Minimal Effective Agent Topology

定義：

$$
\boxed{
\mathcal T^\star
=
\arg\min_{\mathcal T} C(\mathcal T)
}
$$

subject to：

$$
Quality(\mathcal T)\ge Q_{\min},
$$

$$
Risk(\mathcal T)\le R_{\max},
$$

$$
Experience(\mathcal T)\ge E_{\min},
$$

以及必要時：

$$
T_{\mathrm{wall}}(\mathcal T)\le T_{\max}.
$$

這不是新系列名稱，而是 FCAO 的部署原則。

---

# 16. Deployment Tier 0：Strong Single AI

對基本與中等實作：

$$
\boxed{
\mathcal T_0
=
SingleStrongPrimary.
}
$$

適合：

- 高 context coupling；
- 一個模型可連續掌握 architecture；
- deterministic tests 足夠；
- merge cost 高；
- delegation 本身沒有明顯 parallel gain。

此時優先：

$$
Primary
+
Tools.
$$

APR 可作觀測節省，但不要求 Twin。

---

# 17. Deployment Tier 1：Primary + Twin

較複雜、較高風險工作：

$$
\boxed{
\mathcal T_1
=
Primary+Twin.
}
$$

Primary：

$$
Build
+
MaintainContext
+
Integrate.
$$

Twin：

$$
Verify
+
Challenge
+
FindBlindSpots.
$$

重點是：

$$
TwinActivity
=
Sparse.
$$

Twin 可以 `IDLE`，不必每輪都重新理解整個專案。

這是目前最接近「獨立驗證收益」與「低 context fragmentation」之間平衡的架構。

---

# 18. Deployment Tier 2：Builder + Verifier + Experience

對真正困難、跨多小時或多 session 的工作：

$$
\boxed{
\mathcal T_2
=
Builder+Verifier+Experience.
}
$$

三者是跨對話 / 長期角色，不是大量 ephemeral workers。

Builder：

$$
\text{最大 context / interaction budget}.
$$

Verifier：

$$
\text{較低頻、獨立 correctness / architecture / security review}.
$$

Experience：

$$
\text{較低頻、user flow / product behavior / usability review}.
$$

推薦資源關係：

$$
Budget_{Builder}
>
Budget_{Verifier}
>
Budget_{Experience}.
$$

不是三個 Agent 平均分資源。

---

# 19. Experience Agent 不等於第三個 Reviewer

Experience 的問題不是：

> code 對不對？

而是：

> 產品真的好用嗎？

所以：

$$
Experience
\neq
Verification.
$$

它可以檢查：

- onboarding；
- workflow；
- user friction；
- product completeness；
- public behavior；
- real-world operability。

因此 Tier 2 的三個角色形成：

$$
\boxed{
Build
+
Verify
+
Experience.
}
$$

---

# 20. Recursive Children：保留，但降為 Future-Capability Path

原 FCAO：

$$
A_i
\rightarrow
\{A_{i1},A_{i2},\ldots\}.
$$

本文保留。

但 2026 deployment default：

$$
\boxed{
ChildDelegation=OFF.
}
$$

除非：

$$
Separability
\gg
ContextCoupling
$$

且：

$$
ExpectedParallelGain
>
ContextTransfer
+
Coordination
+
Verification
+
Merge.
$$

---

# 21. 哪些任務現在仍值得開 child

可能包括：

1. 大量彼此獨立的 repo scan；
2. 多個獨立平台 reproduction；
3. 三個互不依賴的 research domain；
4. external wait 很長、另一 branch 可真正利用 idle window；
5. 必須使用不同工具 / provider 的獨立 adversarial check；
6. 大量 homogeneous work 可以共享固定 schema。

這些任務具有：

$$
LowCoupling
+
HighParallelism.
$$

---

# 22. 哪些任務目前優先 NO_SPLIT

包括：

1. 中型網站功能；
2. architecture + implementation + tests 高度交織；
3. codebase 需要長期 global invariants；
4. specification 尚在演化；
5. output 最後高度依賴 single integration surface；
6. child 必須反覆詢問 Primary 才能做；
7. review 成本接近 implementation cost。

即：

$$
ContextCoupling
\uparrow
\Rightarrow
NO\_SPLIT
$$

的先驗權重應提高。

---

# 23. Strong Primary First

本文將 2026 deployment heuristic 定為：

$$
\boxed{
StrongPrimaryFirst.
}
$$

流程：

$$
CanPrimarySolve?
$$

若是：

$$
Single.
$$

若 risk / blind spot 高：

$$
Primary+Twin.
$$

若 project 同時具有高度 correctness 與 experience requirement：

$$
Builder+Verifier+Experience.
$$

只有再往上才考慮 child fan-out。

---

# 24. APR 在新部署政策中的位置

APR 先問：

$$
NeedObservation?
$$

再問：

$$
NeedAdditionalAgent?
$$

所以：

$$
State
\rightarrow
APR
\rightarrow
ObservationDecision
\rightarrow
TopologyDecision.
$$

可能回：

$$
NO\_OBSERVATION,
$$

$$
TARGETED\_OBSERVATION,
$$

$$
STRUCTURED\_INSPECTION.
$$

已知 evidence 足夠時：

$$
\boxed{
DoNotReobserve.
}
$$

這可以抑制 review workflow 的重複讀取與重複驗證。

---

# 25. Child Agent 不再是 Primary 的第一個工具

新的優先順序：

$$
\boxed{
Tool
\rightarrow
APR
\rightarrow
Twin
\rightarrow
Experience
\rightarrow
Child
}
$$

不是絕對固定 sequence，而是 deployment preference。

其中 deterministic tool 應優先於：

$$
SpawnAnotherModel.
$$

---

# 26. 當前最重要的性能指標不是 Agent 數量

FCAO 後續 benchmark 應測：

$$
UsefulWorkPerWallClock,
$$

$$
UsefulWorkPerCompute,
$$

$$
DelegationInducedRework,
$$

$$
VerificationAmplificationRatio,
$$

$$
ContextReconstructionCost,
$$

$$
MergeRepairCost,
$$

$$
DefectEscapeRate.
$$

新增：

$$
\boxed{
DelegationInducedRework
}
$$

專門量測「如果不 delegation，這些修正是否根本不會發生」。

---

# 27. Verification Amplification Ratio

定義：

$$
VAR
=
\frac{
C_{\mathrm{review}}
+
C_{\mathrm{reReview}}
+
C_{\mathrm{reviewInducedFix}}
}{
C_{\mathrm{implementation}}
}.
$$

若：

$$
VAR>1,
$$

代表 verification workflow 的成本已超過初始 implementation。

這不自動代表 workflow 不合理；高安全領域可能接受。

但普通網站不應默認使用同一門檻。

---

# 28. Context Reconstruction Ratio

定義：

$$
CRR
=
\frac{
C_{\mathrm{childContext}}
+
C_{\mathrm{reviewerContext}}
+
C_{\mathrm{mergeContext}}
}{
C_{\mathrm{total}}
}.
$$

如果大量計算只是在重新理解同一個 project：

$$
CRR\uparrow
$$

表示 topology 很可能過度切分。

---

# 29. Current Deployment Principle

本文正式提出：

$$
\boxed{
UseTheSmallestAgentTopology
ThatMeetsQualityRiskAndExperienceRequirements.
}
$$

這是 FCAO 現階段最重要的 deployment invariant。

---

# 30. 理論未來何時可以重新提高 fan-out

當下列能力顯著成熟：

$$
SharedMemory,
$$

$$
SharedCanonicalWorldState,
$$

$$
LowCostContextTransfer,
$$

$$
TemporalSynchronization,
$$

$$
CapabilityAwareScheduler,
$$

$$
ComputeBudgetRouting,
$$

$$
VerificationPlacement,
$$

$$
SemanticMerge.
$$

才應重新提高：

$$
N_{\mathrm{children}}.
$$

---

# 31. Re-entry Criteria for Recursive Multi-Agent

未來某 runtime 若要宣稱 FCAO recursive mode deployment-ready，至少應展示：

1. parent / child lineage 可驗證；
2. child 取得必要 global constraints；
3. state update 可低延遲同步；
4. stale child work 可偵測；
5. compute allocation 可按 task routing；
6. verification 不預設 full duplicate；
7. merge 有 typed semantics；
8. benchmark 顯示 net benefit；
9. false closure 不高於 Strong Primary baseline；
10. wall-clock / compute cost 具有實質優勢或必要品質優勢。

---

# 32. 對 FCAO 原系列的公開閱讀指引

未來 FCAO Paper 00–02 公開時，應附加：

> **Deployment Readiness Notice:** FCAO recursive multi-agent structures describe a theoretical and architectural capability envelope. They are not a recommendation to maximize agent count under current runtimes. For current deployment guidance, see FCAO Paper 03.

這避免 Paper 00–02 被獨立截取後誤讀。

---

# 33. 對 Reference Architecture 的修正

`FCAO Twin-Core Reference Architecture` 不需重寫本體。

但 deployment defaults 應改成：

```yaml
deployment:
  default: SINGLE
  twin: ON_DEMAND
  experience: OPTIONAL
  child_delegation: EXPERIMENTAL
  recursive_delegation: FUTURE_CAPABILITY
```

這是 deployment profile，不是 ontology change。

---

# 34. 對 OpenHarness Integration 的修正

OpenHarness integration 仍有價值：

- provider；
- CLI；
- MCP；
- task runtime；
- hooks；
- verifier；
- process management。

但：

$$
OpenHarnessSubagentPrimitive
$$

不代表：

$$
FCAOMustSpawnSubagents.
$$

它只是：

$$
AvailableCapability.
$$

---

# 35. 對 Twin 的新理解

Twin 的價值不在：

$$
AlwaysRunningSecondModel.
$$

而在：

$$
\boxed{
IndependentReviewCapacity.
}
$$

因此：

$$
Twin
=
DormantCapability
+
SparseActivation.
$$

這和大量 child 的持續 execution 完全不同。

---

# 36. 對 Experience 的新理解

Experience 可以是第三個獨立 conversation / Agent。

但它不需要：

- project 全部 coding history；
- full implementation context；
- full authority。

它只需要：

$$
ProductSurfaceProjection.
$$

這使第三角色比再開一個 implementation child 更容易維持低成本。

---

# 37. 三階部署狀態機

$$
\boxed{
\mathcal T_0
\rightarrow
\mathcal T_1
\rightarrow
\mathcal T_2
}
$$

其中：

$$
\mathcal T_0=Single,
$$

$$
\mathcal T_1=Primary+Twin,
$$

$$
\mathcal T_2=Builder+Verifier+Experience.
$$

升級條件：

$$
Risk\uparrow
\lor
BlindSpot\uparrow
\lor
ExperienceNeed\uparrow.
$$

不因 task 名稱叫「大型」就自動升級。

---

# 38. 降級同樣重要

如果 Twin 長期：

$$
IDLE,
$$

且 risk 下降：

$$
\mathcal T_1
\rightarrow
\mathcal T_0
$$

是合法的。

如果 Experience 已完成：

$$
\mathcal T_2
\rightarrow
\mathcal T_1
$$

也合法。

所以：

$$
\boxed{
TopologyCanShrink.
}
$$

這和只會增加 Agent 的 orchestration 形成根本差異。

---

# 39. Research Hypotheses for Next Phase

後續應測：

## H1

對高 context-coupling coding task：

$$
SingleStrong
$$

在 wall-clock / compute efficiency 上優於 dense subagent workflow。

## H2

$$
Primary+Twin
$$

可以保留大部分 defect-reduction benefit，而顯著降低 context / merge overhead。

## H3

$$
Builder+Verifier+Experience
$$

在高難度產品任務上提供較佳 correctness / usability trade-off。

## H4

多 child 在低 coupling、高 parallelism 任務仍可能優於 Single。

因此本文不是：

$$
MultiAgentIsBad.
$$

而是：

$$
\boxed{
TopologyMustMatchTaskGeometryAndRuntimeCapability.
}
$$

---

# 40. Evidence Boundary

本文目前只有 preliminary operational evidence。

尤其：

- 部分 wall-clock / quota 數字是 operator-observed；
- 不同專案難度不同；
- 不同工作流使用不同 review intensity；
- 沒有完整 A/B instrumentation。

因此本文只足以支持：

$$
\boxed{
ChangeDeploymentDefault.
}
$$

尚不足以支持：

$$
\boxed{
UniversalPerformanceRanking.
}
$$

---

# 41. 公開隱私與原始證據

公開版：

$$
AIIdentity
\rightarrow
RoleLabel.
$$

例如：

- `Primary AI`
- `Twin AI`
- `Implementation Agent`
- `Reviewer`
- `Experience Agent`
- `Child Agent A`

原始研究 archive：

$$
RawEvidence
$$

可保留完整原文，只要存取權受控。

因此：

$$
\boxed{
PrivateRawEvidence
\neq
PublicResearchArtifact.
}
$$

---

# 42. FCAO v0.1 Series Readiness Statement

FCAO v0.1 系列現在應被理解為：

$$
\boxed{
Architecture
+
Governance
+
TemporalTopology
+
DeploymentBoundary.
}
$$

四篇理論文彼此關係：

$$
Paper00:
World/Organization,
$$

$$
Paper01:
TwinGovernance,
$$

$$
Paper02:
TemporalTopology,
$$

$$
Paper03:
DeploymentCapabilityGap.
$$

Paper 03 不是附錄，而是避免整套理論被誤部署的重要邊界。

---

# 43. 核心不變量

## Invariant 1

$$
TheoreticalCapability
\neq
CurrentDeploymentRecommendation.
$$

## Invariant 2

$$
Single
$$

永遠是合法且正式的 Agent topology。

## Invariant 3

$$
MoreAgents
\not\Rightarrow
MoreNetUtility.
$$

## Invariant 4

$$
IndependentVerification
\not\Rightarrow
DenseSubagentFanout.
$$

## Invariant 5

$$
Twin
$$

可以是 sparse / on-demand。

## Invariant 6

$$
ChildDelegation_{2026}
=
ExperimentalByDefault.
$$

## Invariant 7

$$
DeploymentPolicy
$$

必須隨 runtime capability 更新。

## Invariant 8

$$
NegativeResult
$$

可以是合法研究結果。

## Invariant 9

$$
PublicResearchArtifact
$$

不保留 AI 個體名稱。

## Invariant 10

$$
FutureRecursiveFCAO
$$

只有在 benchmark 證明 net benefit 後才提升 deployment readiness。

---

# 44. 結論

FCAO 最初提出 recursive、fractal、multi-agent organization，並不是錯誤方向。相反地，它描述了一個比當前產品 workflow 更一般的架構空間：Primary、Twin、child、verification topology、repartition、closure 與 protocol federation 都可以被納入同一 local-global world。

問題在於：

$$
\boxed{
ArchitectureSpace
}
$$

與：

$$
\boxed{
DeploymentOptimum
}
$$

不是同一件事。

2026 年的初步 operational evidence 顯示，高密度 multi-agent execution 仍面臨：

$$
ContextGap
+
TemporalGap
+
StateGap
+
ComputeGap
+
VerificationGap
+
MergeGap.
$$

所以：

$$
N_{\mathrm{agents}}\uparrow
$$

可能增加 defect detection，卻不保證：

$$
UsefulWorkPerHour\uparrow.
$$

本文因此把 FCAO 的當代部署策略正式修正為：

$$
\boxed{
SingleFirst
\rightarrow
TwinIfNeeded
\rightarrow
TriadForHardProjects.
}
$$

其中：

$$
Triad
=
Builder+Verifier+Experience.
$$

Builder 應取得最大的長期 context / interaction budget；Verifier 稀疏介入 correctness、security 與 architecture checkpoint；Experience 從使用者與產品表面進行獨立檢查。

recursive children 並未被刪除，而被重新定位為：

$$
\boxed{
FutureCapability
+
ExperimentalDeploymentPath.
}
$$

真正成熟的 FCAO 不應以「可以生成多少 Agent」衡量，而應以：

$$
\boxed{
UseTheSmallestAgentTopology
ThatMeetsQualityRiskAndExperienceRequirements.
}
$$

作為部署原則。

因此 FCAO 的長期方向仍然成立；需要修正的是對時代條件的假設。

$$
\boxed{
TheoryCapacity
>
CurrentRuntimeCapacity.
}
$$

而一個真正 agent-native 的系統，不只是知道如何委任，也必須知道：

$$
\boxed{
WhenNotToDelegate.
}
$$

---

# 附錄 A：2026 Deployment Profile

```yaml
fcao_series: v0.1
deployment_epoch: 2026

default_topology:
  mode: single_strong_primary

twin:
  activation: on_demand
  purpose:
    - correctness
    - architecture
    - security
    - closure_challenge

experience_agent:
  activation: optional
  purpose:
    - user_flow
    - usability
    - product_completeness

child_agents:
  default: disabled
  status: experimental
  enable_only_if:
    - low_context_coupling
    - high_parallel_separability
    - bounded_merge_cost
    - positive_expected_net_gain

recursive_child_agents:
  status: future_capability

dynamic_repartition:
  status: experimental

public_release:
  anonymize_ai_identity: true
```

---

# 附錄 B：Public Series Notice

> **FCAO Deployment Readiness Notice — v0.1**  
> FCAO recursive and fractal multi-agent structures describe a theoretical and architectural capability envelope. They should not be read as a recommendation to maximize agent count under current runtimes. For 2026 deployment, FCAO recommends Strong Single AI first, Primary–Twin for higher-complexity or higher-risk work, and a Builder–Verifier–Experience triad for the hardest long-running projects. Dense child-agent fan-out and recursive delegation remain experimental until context synchronization, state sharing, compute routing, verification placement, and semantic merge costs are substantially improved and benchmarked.

---

# 附錄 C：Evidence Provenance

Public paper uses role-redacted descriptions only.

Primary evidence classes used for this paper:

1. **FCAO + APR Operational Experiment 01**
   - Single topology
   - zero child/subagent
   - 32 events
   - 4/4 tasks completed
   - 2 closure records
   - final coverage 1.0
   - valid replay

2. **Native multi-agent development workflow record**
   - repeated implementation / review / fix / re-review cycles
   - multiple real security and correctness findings
   - substantial validation depth
   - demonstrates both verification value and orchestration amplification

3. **Operator-observed website / local MCP implementation case**
   - approved specification
   - approximately 4 h 11 m 13 s wall-clock
   - 243/243 tests passing
   - one remaining public API decision at the end
   - not instrumented as a controlled benchmark

No universal performance ranking is claimed from these observations.

---

**End of canonical source.**
