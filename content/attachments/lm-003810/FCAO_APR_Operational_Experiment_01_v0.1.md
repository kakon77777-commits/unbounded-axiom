# FCAO + APR Operational Experiment 01
## Primary–Twin 雙核心在 Single Topology、零子 Agent 條件下的初步運作證據

**系列：** FCAO / Fractal Conversational Agent Organization  
**文件類型：** Experimental Note / Preliminary Operational Evidence  
**版本：** v0.1  
**日期：** 2026-08-24  
**對應 Runtime：** FCAO-OpenHarness MVP v0.1.1  
**實驗資料來源：** `docs/experiments/evidence/FCAO_APR_ACTUAL_STATUS_2026-08-24.{md,json}`  
**實驗邊界：** `Single` topology、`0` child / subagent、Primary + Twin + APR operational composition  
**狀態：** Preliminary evidence; not a performance proof

---

## 摘要

本實驗記錄 FCAO 與 APR 的第一次 operational composition。此次測試刻意**不啟動任何 child Agent**，不測多子 AI、不測遞歸派發，也不以增加 Agent 數量換取可靠性；其目的只有一個：先隔離並觀察 **Primary–Twin 雙核心治理**與 **APR 證據／觀測控制**本身是否能在一個真實工作流程中形成可回放、可挑戰、可重新閉合的治理循環。

實際本地運行建立 world：

```text
fcao-apr-mrmic-consolidation-v1
```

並記錄：

- topology：`Single`
- subagents started：`0`
- event count：`32`
- tasks：`4/4 COMPLETED`
- closure records：`2`
- final closure coverage：`1.0`
- blocking tasks：`0`
- replay verification：valid

Twin 實際決策序列為：

```text
IDLE
→ CHALLENGE
→ CONCUR
→ CHALLENGE
→ CONCUR
```

APR 則出現兩種重要行為：對已驗證 FCAO Runtime 完整性回傳 `NO_OBSERVATION`；對尚未取得充分授權與證據的 cleanup 範圍要求額外觀測／結構化檢查，待使用者明確授權成為高信心 evidence 後，不再重複詢問或重新讀取無關資料。

本實驗最重要的結果不是證明 FCAO「更快」或「更省 token」，而是確認三件架構性現象真的可以在 operational flow 中發生：

1. Twin 可以合法 `IDLE`，治理能力不等於持續推理成本。
2. Twin 可以 challenge **verification method 本身**，而不只是 challenge task result。
3. 第一張 closure 可以被後續 evidence 判定為不完整，並以 append-only `supersede` 方式保留歷史而不是重寫歷史。

因此，本 note 將 APR 正式定位為 FCAO 中可供 Primary 與 Twin 共用的 **Evidence / Observation Control Plane**，但不把此次結果擴張成多 Agent、遞歸 Agent 或性能優勢的證明。

---

# 1. 實驗問題

本次實驗只問：

> 在沒有 child Agent 的條件下，FCAO 的 Primary–Twin 雙核心與 APR 是否仍能形成有意義的治理、觀測與 closure loop？

也就是刻意測試：

$$
N_{child}=0
$$

時，是否仍存在：

$$
Primary
\parallel
Twin
$$

以及：

$$
Evidence
\rightarrow
ObservationDecision
\rightarrow
GovernanceAction
\rightarrow
Receipt
\rightarrow
CanonicalState.
$$

若成立，就表示 Twin Governance 與 Child Delegation 在架構上至少可以分離測試，而不是只有「派很多 Agent」時才有意義。

---

# 2. 實驗配置

此次 operational run 的核心配置為：

```text
Topology: Single
Primary: active
Twin: deterministic policy / evidence audit
APR: evidence sufficiency + observation control
Child Agents: 0
Canonical State: FCAO SQLite event ledger
Target Work: MRMIC / NVCL workspace consolidation + GitHub synchronization
```

FCAO Runtime 基線證據：

- FCAO OpenHarness MVP v0.1
- tests：`19/19`
- compile check：PASS
- deterministic demo：PASS
- live OpenHarness child execution：尚未建立

這點非常重要：本次不是在已完成 OpenHarness recursive child runtime 後進行的多 Agent 實驗，而是透過既有 Python APIs、共享 evidence semantics 與 FCAO SQLite world 所完成的 operational composition。

---

# 3. FCAO 與 APR 的責任分工

此次運行中，FCAO 與 APR 的責任並沒有重疊成同一件事。

FCAO 負責：

$$
\boxed{
World
+
TaskTopology
+
EventLedger
+
TwinDecision
+
LCC
+
Closure
+
Reopen/Supersession
}
$$

APR 負責：

$$
\boxed{
EvidenceSufficiency
+
ObservationDecision
+
MinimalReobservation
+
EvidenceGate
}
$$

因此 APR 不決定 project topology，也不取代 Twin；它回答的是：

> 現在已經知道的 evidence 是否足夠？是否真的需要再觀察？若需要，最小必要觀察是什麼？

FCAO 則回答：

> 根據目前 world state、task topology、evidence 與 governance policy，接下來要不要 challenge、reopen、close 或 commit？

兩者組合後形成：

$$
\boxed{
State
\rightarrow
APR
\rightarrow
ObservationRequirement
\rightarrow
Primary/Twin
\rightarrow
Action
\rightarrow
Evidence/Receipt
\rightarrow
State
}
$$

---

# 4. APR 的 `NO_OBSERVATION`

已驗證 FCAO Runtime 完整性後，APR 對該 evidence 回傳：

```text
NO_OBSERVATION
```

其語義不是「永遠不要再驗證」，而是：

> 在目前 scope、版本與 evidence validity 條件下，重新觀察的預期資訊增益不足以支持再次讀取或重算。

可寫為：

$$
Verified(e)
\land
Confidence(e)\ge\theta
\Rightarrow
NO\_OBSERVATION.
$$

這一點直接對應 FCAO 原先的成本問題：驗證不應默認等於重新讀取所有資料或重新推理全部問題。

---

# 5. 從 evidence gap 到最小追加觀測

MRMIC cleanup 恢復授權在取得前，APR 沒有把「先前知道部分背景」誤當成「已充分授權」。

在原始 operational record 中，其狀態被記為：

```text
INSPECT / structured
```

在 v0.1.1 deterministic reconstruction 中，這一類狀態被規範為三個 observation action：

```text
NO_OBSERVATION
TARGETED_OBSERVATION
STRUCTURED_INSPECTION
```

其中：

- evidence 完全缺失：`TARGETED_OBSERVATION`
- evidence 存在但信心／結構不足：`STRUCTURED_INSPECTION`
- evidence 已驗證且達門檻：`NO_OBSERVATION`

因此 APR 的最小決策函數可先寫成：

$$
APR(e)=
\begin{cases}
TARGETED\_OBSERVATION, & e\text{ missing}\cr
NO\_OBSERVATION, & Verified(e)\land Conf(e)\ge\theta\cr
STRUCTURED\_INSPECTION, & otherwise
\end{cases}
$$

這不是最終 APR 理論，而是 FCAO v0.1.1 所採用的 deterministic operational contract。

---

# 6. Twin `IDLE` 是有效治理結果

Twin 第一次決策為：

```text
IDLE — no-actionable-risk
```

這個結果非常重要，因為它拒絕了以下隱含假設：

$$
TwinExists
\Rightarrow
TwinMustComputeContinuously.
$$

本次實驗支持較弱、也更實用的命題：

$$
\boxed{
GovernanceCapacity
\neq
GovernanceActivity
}
$$

Twin 可以持續存在於 governance model 中，但只有在 evidence、risk 或 closure condition 產生可行動訊號時才介入。

這使未來的 Persistent Twin 可以採 event-driven wake，而不是第二個永遠保持 full-context inference 的模型。

---

# 7. Twin challenge 的第一個對象：驗證方法

第一次 `CHALLENGE` 來自 Git 預設 `quote-path` 對 Unicode path 的轉義行為。原先 allowlist verifier 將路徑轉義結果判為違規，形成 false positive。

Twin 沒有把：

```text
Verifier says FAIL
```

直接等價成：

```text
Task is invalid
```

而是要求重新檢查 audit method。當驗證改為 `core.quotepath=false` 後，14 個變更路徑全部符合 allowlist，Twin 才 `CONCUR`。

這支持 FCAO Twin Paper 的一個重要工程命題：

$$
\boxed{
TwinAudit
=
Audit(Task, Evidence, VerificationMethod)
}
$$

而不是只有：

$$
Audit(TaskResult).
$$

換句話說，verification 本身也是 governance topology 的一部分，也必須可被 challenge。

---

# 8. 第一張 closure 為何被 supersede

第一次 closure 在當時已知 task graph 中看似滿足 closure，但 Twin 後來指出 scope 漏掉：

- GitHub merge
- 正式 local `main` synchronization

這代表：

$$
AllRepresentedTasksClosed
$$

不必然等於：

$$
AllMandatoryTasksRepresented.
$$

因此第一次 closure 被 challenge，world `REOPEN`，新增 GitHub synchronization 節點與 LCC，之後才簽發第二張 closure。

最重要的是，第一張 closure 沒有被刪除。

而是：

$$
\boxed{
GCC_2
\ supersedes\
GCC_1
}
$$

歷史保留：

```text
gcc-1 -> superseded by gcc-2
```

而不是把資料重寫成「第一次從未 closure」。

這正是 versioned closure 的 operational evidence。

---

# 9. 實際 Twin 決策序列

此次記錄為：

```text
1. IDLE
2. CHALLENGE — verifier method false positive
3. CONCUR — corrected audit satisfies evidence
4. CHALLENGE — candidate closure omitted mandatory GitHub sync node
5. CONCUR — reopened world satisfies all mandatory nodes
```

可以抽象為：

$$
IDLE
\rightarrow
CHALLENGE_{verify}
\rightarrow
CONCUR
\rightarrow
CHALLENGE_{closure}
\rightarrow
CONCUR.
$$

這個序列至少說明 Twin 並不是固定「反對者」，也不是固定「第二驗證器」。它可以：

- 不介入；
- challenge；
- 接受修正；
- 再 challenge 不同層級問題；
- 最終 concur。

---

# 10. Canonical state 與 replay

此次 world 由 SQLite event ledger 保存，event count 為 `32`，並通過 replay verification。

因此 governance history 不只存在 Primary context 或對話記憶中。

至少下列資訊被外部化：

- task state
- evidence
- Twin decisions
- LCC
- closure
- reopen / supersession

這使：

$$
AgentContextLoss
\not\Rightarrow
ProjectHistoryLoss.
$$

也使第一次錯誤 closure 能被保留並重建，而不依賴某個模型「記得自己以前判錯」。

---

# 11. 本次沒有證明的事情

本實驗不能用來宣稱以下結論：

## 11.1 沒有證明多子 AI 效果

因為：

$$
N_{child}=0.
$$

所以不能推論：

- FCAO 多子 Agent 比固定 subagent orchestration 快；
- recursive delegation 已可用；
- child-local Twin 已可用。

## 11.2 沒有證明 token 節省比例

本次沒有建立：

$$
\Delta Token\%
$$

或完整 wall-clock baseline，因此只可提出 qualitative observation，不能報出節省百分比。

## 11.3 Deterministic Twin 不等於獨立模型觀點

此次 Twin 是 deterministic policy / evidence audit，證明的是治理與 event semantics 能工作，不是證明兩個不同模型的 epistemic diversity 已被測量。

## 11.4 尚未完成 live OpenHarness recursive child execution

OpenHarness adapter 目前仍為 carrier-ready boundary；本次 operational composition 不等於已完成原生 child spawn、native parent lineage 或 nested team runtime。

---

# 12. 本次可接受的初步結論

在上述限制下，本次至少提供以下 preliminary operational evidence：

### O1 — Twin Governance 與 Child Delegation 可分開測試

在 `0` child 下，Twin 仍有可觀察治理作用。

### O2 — Twin `IDLE` 合法且必要

Twin 不需要持續耗用第二份完整推理成本。

### O3 — Verification method 可以成為 challenge 對象

Verifier signal 不是不可挑戰真理。

### O4 — Closure 可以被 supersede 而不改寫歷史

FCAO 的 versioned closure 在真實流程中出現了實際案例。

### O5 — APR 可以避免對已驗證事實的重複觀測

`NO_OBSERVATION` 可成為一個正式、可記錄、可 replay 的 computational decision。

---

# 13. APR 在 FCAO Reference Architecture 的新位置

在 v0.1.1 之後，FCAO reference flow 應補為：

$$
\boxed{
CanonicalState
\rightarrow
APR
\rightarrow
ObservationDecision
\rightarrow
Primary/Twin
\rightarrow
Topology/Action
\rightarrow
Evidence/Receipt
\rightarrow
CanonicalState
}
$$

APR 不是新的最高治理核心。

它是：

$$
\boxed{
EvidenceObservationControlPlane
}
$$

可被 Primary 與 Twin 共同呼叫。

因此：

$$
Primary
\parallel
Twin
$$

仍然是治理雙核心；APR 只決定資訊取得是否必要與應採哪一種最小觀測策略。

---

# 14. v0.1.1 的最小 Runtime 規格

FCAO-OpenHarness MVP v0.1.1 新增：

```text
EvidenceRecord
ObservationDecision
APRController
EVIDENCE_RECORDED
OBSERVATION_DECIDED
CLOSURE_SUPERSEDED
active_closure()
apr-demo
```

APR v0.1.1 action set：

```text
NO_OBSERVATION
TARGETED_OBSERVATION
STRUCTURED_INSPECTION
```

Closure 則新增 append-only supersession relation：

```text
old_closure_id -> new_closure_id
```

而 `verify` 只驗證 active、未 supersede 的 closure。

---

# 15. Deterministic reconstruction 與實際 operational run 的區別

v0.1.1 package 內新增：

```bash
python -m fcao.cli apr-demo --db <path>
```

這個 demo 不是原始本機 SQLite world 的複製品，也不宣稱重播原本全部 32 events。

它是一個 **deterministic reconstruction**，用最小事件序列重現下列 invariant：

- `Single` topology
- `0` child Agents
- APR `NO_OBSERVATION`
- authorization evidence gap
- Twin `IDLE / CHALLENGE / CONCUR`
- first closure superseded
- second closure active
- replay equivalence

原始 operational evidence 則原封保存在：

```text
docs/experiments/evidence/FCAO_APR_ACTUAL_STATUS_2026-08-24.md
docs/experiments/evidence/FCAO_APR_ACTUAL_STATUS_2026-08-24.json
```

如此避免把「可重現測試」與「原始現場紀錄」混成同一種證據。

---

# 16. 下一輪實驗

## E2 — Multi-Child FCAO + APR

下一輪才開始：

$$
Primary
+
Twin
+
APR
+
Children.
$$

至少測：

- `NO_SPLIT` 與 `SPLIT` 同時存在；
- 2–4 Named Ephemeral Agents；
- child LCC；
- verification queue；
- Twin selective audit；
- APR 是否減少 child / Twin 的不必要重觀測。

## E3 — Recursive Children + Local Twin + Dynamic Repartition

再下一輪：

$$
A_0
\rightarrow
A_1
\rightarrow
A_{1,1}
$$

並測：

- logical / native parent lineage；
- child-local Twin activation；
- temporal envelope breach；
- dynamic repartition；
- hierarchical merge；
- local closure → global closure。

只有 E2、E3 都完成後，才適合評估是否需要一篇新的統合實驗論文。

---

# 17. 結論

本次測試不是「多 Agent 成功展示」。恰好相反，它的重要性就在於 **沒有派任何 child Agent**。

在：

$$
N_{child}=0
$$

的條件下，仍然觀察到：

$$
Primary
\parallel
Twin
$$

可以形成具有 `IDLE`、`CHALLENGE`、`CONCUR`、reopen 與 closure supersession 的治理循環；APR 則能把「是否需要重新觀測」提升成正式 decision，避免把已驗證事實反覆讀取與驗證。

因此本次真正得到的不是 performance proof，而是一個更基礎的 operational conclusion：

$$
\boxed{
ComputeOnlyWhatNeedsComputing
+
ObserveOnlyWhatNeedsObserving
}
$$

可以被拆成兩個彼此相容但不同的控制問題：

- FCAO 控制 **計算、委任、驗證、閉合拓樸**；
- APR 控制 **證據充分性與觀測需求**。

這足以支持把 APR 正式加入 FCAO v0.1.1 Runtime；但在多子 AI、遞歸派發與動態重分區實驗完成前，不應把它擴張成新的完整理論系列。

---

**End of Experimental Note 01.**
