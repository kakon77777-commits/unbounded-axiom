# 類全域 AI 世界—計算—觀察統合系列（Paper 08）
## 記憶層：從資訊海到可重建世界與世界族
### The Memory Layer: From Information Oceans to Reconstructable Worlds and World Families

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 08 / 12  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** Operator-Assisted Memory × Multi-Representation Autonomous Memory Fabric × SEDB/SEQL × Crystallized Semantic Graph × Global Knowledge Convergence × PNCW Context Projection × MWT Dynamic Fixed Points × Event Sourcing × World Reconstruction  
**前篇：** Paper 07《物理層：從 Machine Projection 到 Physical Projection》  
**狀態：** WCO 記憶層母規格／世界可重建記憶架構；不宣稱所有世界可由有限記憶完全重建，不宣稱任何單一資料庫、向量索引或摘要格式可以獨立完成類全域 AI 長期記憶

---

## 摘要

Paper 01–07 已逐步建立：

$$
\mathfrak W_t^G,
\quad
\mathfrak C_t^{WF},
\quad
\mathfrak O_t^G,
\quad
\mathfrak D_t^{WCO},
\quad
\mathfrak P_t^G,
\quad
\mathsf{PRS}_t.
$$

然而，如果這些 world、computation、observation、qualification、projection、physical feedback 與 certificate 只存在於當前 context，當一次 session、process、device 或 model invocation 結束後便消失，那麼整個 WCO 仍然只是高階短期智能。

類全域 AI 的長程能力需要一個更強的記憶條件：

$$
\boxed{
\text{Memory}
\neq
\text{Context Window}.
}
$$

更進一步：

$$
\boxed{
\text{Memory}
\neq
\text{Stored Text}.
}
$$

真正有用的長期記憶必須能回答：

- 這個 object 是誰？
- 它的原始來源在哪裡？
- 它目前哪個 version 有效？
- 哪些 claim 是 observation、inference、hypothesis、verification 或 retraction？
- 哪些 branches 曾存在？
- 哪些 branches 被 prune、archive、invalidate 或 reopen？
- 哪些 computation route 曾失敗？
- 哪個 certificate 支撐目前狀態？
- 哪些 dependency 已 stale？
- 哪些 representation 可以重建？
- 是否能重建某個歷史 world state？
- 是否能重建一組 world family，而不是只重播一段文字？

本文提出 **World-Reconstructive Memory Fabric（WRMF，世界可重建記憶織體）**，作為 WCO 的正式 Memory Layer。

其核心形式為：

$$
\boxed{
\mathfrak M_t^{WCO}
=
\left\langle
\mathcal R_t^{raw},
\mathcal E_t^{evt},
\mathcal K_t^{sem},
\mathcal G_t^{mem},
\mathcal X_t^{crystal},
\mathcal B_t^{branch},
\mathcal F_t^{fail},
\mathcal C_t^{cert},
\mathcal H_t^{hist},
\mathcal I_t^{idx},
\mathcal A_t^{access},
\mathcal V_t^{version}
\right\rangle.
}
$$

其中：

- $\mathcal R_t^{raw}$：raw / exact canonical sources；
- $\mathcal E_t^{evt}$：immutable event history；
- $\mathcal K_t^{sem}$：structured semantic / claim state；
- $\mathcal G_t^{mem}$：typed graph / hypergraph relations；
- $\mathcal X_t^{crystal}$：semantic crystals / compressed derived views；
- $\mathcal B_t^{branch}$：branch / lineage memory；
- $\mathcal F_t^{fail}$：failure / counterexample / negative knowledge；
- $\mathcal C_t^{cert}$：certificate / verification memory；
- $\mathcal H_t^{hist}$：computation / observation / projection / physical history；
- $\mathcal I_t^{idx}$：rebuildable lexical / vector / matrix / graph indexes；
- $\mathcal A_t^{access}$：authority / privacy / visibility state；
- $\mathcal V_t^{version}$：version / validity / staleness state。

本文不要求所有內容由同一 database 儲存。相反地，承接 Multi-Representation Autonomous Memory Fabric：

$$
\boxed{
\text{Governed Memory State}
\rightarrow
\text{Multiple Rebuildable Representations}
\rightarrow
\text{Purpose-Aware Strategy Selection}.
}
$$

對 memory object $m$：

$$
\boxed{
\mathcal R(m)
=
\{
R_e,
R_s,
R_y,
R_v,
R_m,
R_g,
R_t
\},
}
$$

其中可分別為 exact、structured semantic、symbolic/addressable、vector、matrix/tensor、graph、temporal/event representation。

但所有 derived representation 都必須遵守：

$$
\boxed{
R_i(m)\neq m.
}
$$

因此：

$$
\boxed{
\text{Vector Similarity}
\neq
\text{Knowledge Authority},
}
$$

$$
\boxed{
\text{Semantic Crystal}
\neq
\text{Raw Source},
}
$$

$$
\boxed{
\text{Retrieval Result}
\neq
\text{Canonical Memory Commit}.
}
$$

本文採用 SEDB 的 event-sourced knowledge evolution 原則：知識狀態不能只靠 silent overwrite，而應記錄 ADD、RETRACT、REVISE、SPLIT、MERGE、DOWNGRADE、DEPRECATE、REVIVE 等語義事件。對 claim：

$$
C_k,
$$

記憶系統首先保存「誰、在何時、何 scope、基於什麼 provenance 提出了什麼 claim」，而不是假裝所有寫入都是 fact。

因此：

$$
\boxed{
\text{Claim}
\neq
\text{Fact}.
}
$$

本文同時承接 Crystallized Semantic Graph（CSG）的 raw–crystal non-collapse：

$$
\boxed{
\text{Raw Canonical Memory}
\rightarrow
\text{Semantic Crystals}
\rightarrow
\text{Semantic Graph}
\rightarrow
\text{Active Working Memory},
}
$$

且：

$$
\boxed{
C_i^{(\theta)}
\neq
R_i,
}
$$

$$
\boxed{
C_i^{(\theta)}
\text{ never replaces }
R_i.
}
$$

因此 compressed memory 可以大量存在，但高風險 claim 必須能沿 provenance hyperlink 展開回 source span。

本文進一步將「記憶是否成功」從 retrieval 問題提升為 **reconstruction problem**。

定義 **World Reconstruction Contract（WRC）**：

$$
\boxed{
\mathsf{WRC}
=
\left\langle
WorldId,
TargetVersion,
BranchPolicy,
TimeHorizon,
Schema,
EvidencePolicy,
QualificationPolicy,
Authority,
Fidelity,
Budget,
ReplayMode,
OpenObligations
\right\rangle.
}
$$

並定義：

$$
\boxed{
\widehat W_t
=
\mathsf{ReconstructWorld}
(
\mathfrak M_t^{WCO},
\mathsf{WRC}
).
}
$$

對可 event-source replay 的狀態：

$$
\boxed{
\widehat W_t
=
Replay(
W_0,
E_{1:t}
).
}
$$

但若 reality event 或 stochastic process 不可 deterministic replay，記憶層只能重建：

- evidence；
- provenance；
- observed history；
- model assumptions；
- known uncertainty；

而不能虛構完整世界：

$$
\boxed{
\text{Historical Reconstruction}
\neq
\text{Perfect Reality Replay}.
}
$$

本文更進一步定義 **World-Family Regeneration Contract（WFRC）**：

$$
\boxed{
\mathsf{WFRC}
=
\left\langle
RootWorld,
LineageScope,
BranchModes,
ArchivedBranches,
PruneReasons,
MergeCertificates,
ReopenTriggers,
EvidenceDependencies,
Budget
\right\rangle.
}
$$

使：

$$
\boxed{
\widehat{\mathfrak W}_t^G
=
\mathsf{RegenerateWorldFamily}
(
\mathfrak M_t^{WCO},
\mathsf{WFRC}
).
}
$$

這不是把每個舊 branch 全部重新執行，而是重建：

- WorldId；
- lineage；
- modes；
- state checkpoints；
- branch distinctions；
- evidence dependencies；
- unresolved obligations；
- reopen conditions。

本文因此提出：

$$
\boxed{
\text{Memory Completeness}
\neq
\text{Full Data Retention}.
}
$$

對類全域 AI，更重要的是：

$$
\boxed{
\text{Reconstruction Sufficiency}.
}
$$

如果一個 compressed memory 可以在指定 task / fidelity 下重建必要 world state、history、qualification、certificate 與 lineage，它可能比保存一堆不可導航 raw chunks 更有用；但 raw canonical source 仍應在高風險與可恢復範圍內保留。

本文亦將失敗正式提升為記憶一級物件：

$$
\boxed{
F
=
(
Route,
Assumptions,
Gap,
Counterexample,
FailureReason,
Repair,
ReusableParts
).
}
$$

因此：

$$
\boxed{
\text{Failed Result}
\neq
\text{Zero-Value Memory}.
}
$$

若失敗、反例、invalidated bridges 與 dead-end routes 被保存，可形成：

$$
\mathcal G_F,
$$

即 obstacle / failure graph，幫助未來 AI 不必重複支付相同探索成本。

本文再承接 Global Knowledge Convergence Theory。知識吸收不是「模型讀過」：

$$
\boxed{
Absorb(x)
\iff
x
\text{ can be located, related, checked, reconstructed, and reused}.
}
$$

成熟 memory 不是摘要倉庫，而是：

$$
\boxed{
\mathcal K_{n+1}
=
\Phi(\mathcal K_n),
}
$$

其中：

$$
\Phi
=
Reconstruct
\circ
Compress
\circ
Abstract
\circ
Compare
\circ
Verify
\circ
Align
\circ
Normalize.
$$

其收斂目標不是檔案數變少，而是提高：

- coverage；
- generativity；
- predictivity；
- transferability；
- reconstructability；

並降低獨立解釋自由度。

本文最後把 dynamic fixed-point continuity 接進記憶層：系統可以壓縮 history、prune active branches、更新 crystals、失效 indexes，但必須保留 continuity witness 與 reopen triggers。

因此：

$$
\boxed{
\text{Forgetting}
\neq
\text{Pruning}
\neq
\text{Archiving}
\neq
\text{Invalidation}
\neq
\text{Erasure}.
}
$$

本文最終命題是：

$$
\boxed{
\text{A Global-Like AI does not need to keep everything active;}
}
$$

但它需要：

$$
\boxed{
\text{to preserve enough structured, versioned,
provenance-bearing and reconstructable memory
to rebuild the worlds, branches, qualifications,
failures and histories that future cognition may need}.
}
$$

**關鍵詞：** World-Reconstructive Memory Fabric、OAM、SEDB、CSG、Multi-Representation Memory、Event Sourcing、World Reconstruction、Branch Memory、Failure Memory、Knowledge Convergence、Dynamic Fixed Point

---

# 0. Paper 07 留下的記憶問題

Paper 07 的 physical loop：

$$
W_t
\rightarrow
P^\ast
\rightarrow
\Phi'
\rightarrow
\widehat P
\rightarrow
E_{real}
\rightarrow
W_{t+1}.
$$

如果這些事件沒有長期保存：

$$
W_{t+1}
$$

只能短暫存在。

---

# 1. Memory 不等 Context

$$
\boxed{
Memory
\neq
Context.
}
$$

---

# 2. Memory Existence 不等 Context Residency

$$
\boxed{
MemoryExistence
\neq
ContextResidency
\neq
AttentionActivation.
}
$$

---

# 3. 三層 Context Capacity

$$
\boxed{
C_t^{active}
\subseteq
C_t^{resident}
\subseteq
\mathcal M_t^{total}.
}
$$

---

# 4. Total Memory 不應全部 Active

$$
|\mathcal M_t^{total}|
\gg
|C_t^{active}|.
$$

這是正常狀態。

---

# 5. Memory Retrieval 不等 Context Inclusion

$$
\boxed{
MemoryRetrieval
\neq
ContextInclusion.
}
$$

retrieved object 還需 authority、freshness、scope、sufficiency 與 context compilation。

---

# 6. Memory 不等 Storage

Storage 回答：

> bytes 在哪？

Memory Layer 還必須回答：

> 這些 bytes 對哪個 object、world、claim、history、branch 有什麼意義？

---

# 7. Memory Object

本文定義：

$$
\boxed{
m
=
\left\langle
Id,
Class,
Source,
Time,
Version,
Scope,
EpistemicState,
Authority,
Dependencies,
Representations,
ReconstructionHooks
\right\rangle.
}
$$

---

# 8. Memory Identity 不等 Filename

$$
\boxed{
MemoryIdentity
\neq
FilePath.
}
$$

---

# 9. Memory Identity 不等 Vector

$$
\boxed{
MemoryIdentity
\neq
Embedding.
}
$$

---

# 10. Memory Identity 不等 Summary

$$
\boxed{
MemoryIdentity
\neq
Summary.
}
$$

---

# 11. 多表示 Memory

$$
\boxed{
\mathcal R(m)
=
\{
R_e,
R_s,
R_y,
R_v,
R_m,
R_g,
R_t
\}.
}
$$

---

# 12. Exact Representation

保留：

- source bytes；
- exact span；
- checkpoint；
- artifact；
- hash。

---

# 13. Structured Semantic Representation

保留：

- entities；
- claims；
- relations；
- epistemic state；
- provenance；
- scope。

---

# 14. Symbolic / Addressable Representation

提供：

- stable address；
- explicit symbol；
- discrete locality；
- low-materialization routing。

---

# 15. Vector Representation

適合 fuzzy discovery。

但：

$$
\boxed{
VectorSimilarity
\neq
KnowledgeAuthority.
}
$$

---

# 16. Matrix / Tensor Representation

適合：

- numerical state；
- sparse intersection；
- computational locality；
- feature comparison。

---

# 17. Graph Representation

適合：

- why-related；
- dependency；
- predecessor；
- supersession；
- branch traversal。

---

# 18. Temporal / Event Representation

適合：

- replay；
- delta；
- ordering；
- version reconstruction；
- causally relevant history。

---

# 19. Representation 不等 Memory Object

$$
\boxed{
R_i(m)
\neq
m.
}
$$

---

# 20. One Canonical Master per Data Class

本文承接：

$$
\boxed{
OneCanonicalMasterPerDataClass.
}
$$

---

# 21. Derived Index 不要反向成為 Truth

vector、graph neighborhood、crystal、cache 都應可 rebuild。

---

# 22. Raw Source Layer

$$
\mathcal R_t^{raw}
$$

保存：

- original documents；
- conversations；
- code；
- experiments；
- files；
- event logs。

---

# 23. Raw Canonical 不等 Always Active

raw 可以 cold storage。

---

# 24. Derived 不等 Canonical

$$
\boxed{
Derived
\neq
Canonical.
}
$$

---

# 25. Semantic Crystal

$$
C_i^{(\theta)}
=
K_\theta(R_i).
$$

---

# 26. Crystal 是 Projection

同一 source：

$$
R_i
$$

可以有多個 crystals：

$$
C_i^{technical},
C_i^{conceptual},
C_i^{chronological},
C_i^{project}.
$$

---

# 27. One Source → Multiple Memory Views

$$
\boxed{
OneSource
\rightarrow
MultipleSemanticProjections.
}
$$

---

# 28. Crystal 不取代 Raw

$$
\boxed{
C_i^{(\theta)}
\neq
R_i.
}
$$

---

# 29. Source Span Link

$$
C_i
\xrightarrow{provenance}
R_i[a:b].
$$

---

# 30. Memory Hyperlink

至少提供：

$$
\boxed{
Navigation
+
Provenance
+
Expansion.
}
$$

---

# 31. Crystallized Semantic Graph

$$
\boxed{
\mathcal G_C
=
(V_C,E_C).
}
$$

---

# 32. Hypergraph 更一般

多個 sources 共同導出：

$$
\{
C_1,C_2,C_3
\}
\rightarrow
C_4
$$

可使用 hyperedge。

---

# 33. Memory Edge Type

至少可包含：

- continues；
- refines；
- contradicts；
- supports；
- updates；
- supersedes；
- derived_from；
- implements；
- depends_on；
- caused_by；
- reopens。

---

# 34. Active Memory Projection

$$
\boxed{
\mathcal M_t^{active}
=
\Pi_{\xi_t}(\mathcal G_C).
}
$$

---

# 35. Active Memory 應遠小於 Stored Memory

$$
|\mathcal M_t^{active}|
\ll
|\mathcal M_{stored}|.
$$

---

# 36. Crystal First, Source on Demand

$$
\boxed{
CrystalFirst,
SourceOnDemand.
}
$$

適用於一般 navigation。

高風險 claim 可以直接 source-first。

---

# 37. OAM Knowledge Object

$$
\boxed{
\mathcal K(d)
=
(
E,L,\Phi,G,P,V,S,C
).
}
$$

---

# 38. OAM 不用 Operator Tag 取代 Vector

而是：

$$
\boxed{
Vector
+
Lexical
+
Operator
+
Graph
+
Provenance
+
Version
+
EpistemicState.
}
$$

---

# 39. Query 也要被編譯

$$
\boxed{
\mathcal Q(q)
=
(
q_{lex},
q_{sem},
q_{op},
q_{graph},
q_{epi},
q_{version},
q_{route}
).
}
$$

---

# 40. Memory Strategy Governor

Agent 先形成：

$$
N_t
=
(
Reason,
Scope,
Purpose,
Fidelity,
Budget,
StopCondition
).
$$

---

# 41. Governor 不直接回答

它編譯：

$$
RetrievalPlan.
$$

---

# 42. Purpose-Aware Retrieval

可能：

- identity lookup；
- claim history；
- exact quote；
- architecture reconstruction；
- counterexample search；
- source trace；
- version trace；
- relation traversal。

---

# 43. Provider Availability 不等 Fusion Preference

$$
\boxed{
ProviderAvailability
\not\Rightarrow
FuseAllScores.
}
$$

---

# 44. Parallel Discovery, Sequential Validation

$$
\boxed{
Vector
\parallel
Symbol
\parallel
Graph
\rightarrow
CanonicalResolution
\rightarrow
EvidenceValidation.
}
$$

---

# 45. Routing Receipt

每次 memory route 應保存：

- need；
- strategy；
- providers；
- fallback；
- budget；
- authority ceiling；
- sufficiency；
- replan count。

---

# 46. Retrieval Receipt 不等 Truth

$$
\boxed{
RoutingReceipt
\neq
KnowledgeTruth.
}
$$

---

# 47. SEDB：Claim-First

$$
\boxed{
Claim
\neq
Fact.
}
$$

---

# 48. Claim Record

$$
C_k
=
(
Subject,
Predicate,
Object,
Scope,
Confidence,
Status,
Time,
Provenance
).
$$

---

# 49. Epistemic State 必須顯式

例如：

$$
OBS
\neq
INF
\neq
UNK
\neq
HYP
\neq
CON
\neq
RET.
$$

---

# 50. AI Inference 不得變成 Observation

$$
\boxed{
InferenceMemory
\neq
ObservationMemory.
}
$$

---

# 51. Event Sourcing

$$
\boxed{
\mathcal K_{t+1}
=
\mathcal U(
\mathcal K_t,
\Delta_t
).
}
$$

---

# 52. Semantic Events

可以：

$$
ADD,
RETRACT,
REVISE,
SPLIT,
MERGE,
RENAME,
DOWNGRADE,
GENERALIZE,
SPECIALIZE,
ABSORB,
DEPRECATE,
REVIVE.
$$

---

# 53. Correction 不應 Silent Overwrite

錯誤記錄應：

$$
Corrects(new,old)
$$

而不是刪掉 history。

---

# 54. Immutable Event + Mutable Preferred Pointer

$$
\boxed{
ImmutableHistoricalRecord
+
MutablePreferredStatePointer.
}
$$

---

# 55. Event-Sourced World State

若可 deterministic replay：

$$
\boxed{
W_t
=
Replay(
W_0,
E_{1:t}
).
}
$$

---

# 56. 但 Reality 不一定可 Replay

現實與 stochastic process：

$$
ReplayMode
=
NONDETERMINISTIC
$$

是合法狀態。

---

# 57. 此時只能重建 Evidence / Provenance

不能冒充：

$$
PerfectPastReality.
$$

---

# 58. World Reconstruction Contract

$$
\boxed{
WRC
=
\left\langle
WorldId,
TargetVersion,
BranchPolicy,
TimeHorizon,
Schema,
EvidencePolicy,
QualificationPolicy,
Authority,
Fidelity,
Budget,
ReplayMode,
OpenObligations
\right\rangle.
}
$$

---

# 59. World Reconstruction

$$
\boxed{
\widehat W_t
=
ReconstructWorld(
\mathfrak M_t^{WCO},
WRC
).
}
$$

---

# 60. Reconstruction 不等 Reality

$$
\boxed{
\widehat W_t
\neq
\mathcal R_t.
}
$$

---

# 61. Reconstruction Fidelity 是 Task-Relative

$$
F_{rec}
=
F(
Task,
State,
History,
Evidence,
Resolution
).
$$

---

# 62. Perfect Copy 不一定必要

decision-relevant fidelity 可以足夠。

---

# 63. Reconstruction Sufficiency

$$
\boxed{
Suff_{rec}
(
\widehat W,
\tau,
\varepsilon
)
=
1.
}
$$

---

# 64. 記憶成功不應只看 Recall@K

還要測：

- world reconstruction；
- lineage reconstruction；
- qualification reconstruction；
- source reconstruction；
- replayability；
- branch recovery；
- certificate recovery。

---

# 65. Branch Memory

$$
\mathcal B_t^{branch}.
$$

保存：

- parent；
- fork point；
- mode；
- reason；
- state；
- prune reason；
- merge state；
- archive state；
- reopen trigger。

---

# 66. Pruned Branch 不等 Forgotten Branch

$$
\boxed{
Pruned
\neq
Forgotten.
}
$$

---

# 67. World-Family Regeneration Contract

$$
\boxed{
WFRC
=
\left\langle
RootWorld,
LineageScope,
BranchModes,
ArchivedBranches,
PruneReasons,
MergeCertificates,
ReopenTriggers,
EvidenceDependencies,
Budget
\right\rangle.
}
$$

---

# 68. World-Family Regeneration

$$
\boxed{
\widehat{\mathfrak W}_t^G
=
RegenerateWorldFamily(
\mathfrak M_t^{WCO},
WFRC
).
}
$$

---

# 69. Regenerate 不等 Reexecute All

$$
\boxed{
RegenerateFamily
\neq
ReplayEveryBranch.
}
$$

先重建 lineage / checkpoints / obligations。

必要 branch 再執行。

---

# 70. Failure Memory

$$
\boxed{
F
=
(
Route,
Assumptions,
Gap,
Counterexample,
FailureReason,
Repair,
ReusableParts
).
}
$$

---

# 71. Failure 不等 Empty

$$
\boxed{
FailedResult
\neq
ZeroValueMemory.
}
$$

---

# 72. Negative Knowledge

被 refute 的 claim 仍有：

- scope；
- refutation；
- failed assumptions；
- counterexample；
- useful substructure。

---

# 73. Failure Graph

$$
\boxed{
\mathcal G_F
=
Graph(F_1,\ldots,F_n).
}
$$

---

# 74. Failure Graph 可以避免重複探索

當新 route：

$$
r
$$

匹配已知 obstacle pattern，可 early warn。

---

# 75. Failure Memory 也可能 Stale

新 tool / theorem / evidence 出現後，舊 dead-end 可以 reopen。

---

# 76. Failure Reopen

$$
F_{old}
\xrightarrow{NewCapability}
CandidateAgain.
$$

---

# 77. Certificate Memory

$$
\mathcal C_t^{cert}.
$$

保存：

- proof；
- test；
- measurement；
- legality；
- bridge；
- projection；
- physical realization；
- commit receipt。

---

# 78. Certificate Validity Horizon

certificate 不是永久有效：

$$
h_c.
$$

---

# 79. Version Change 可能使 Certificate Stale

$$
v_1
\rightarrow
v_2
$$

不自動遷移 certificate。

---

# 80. Observation Memory

保存：

- observer；
- operator；
- time；
- world；
- resolution；
- uncertainty；
- source；
- debt。

---

# 81. Computation Memory

保存：

- route；
- backend；
- seed；
- precision；
- candidate；
- reconciliation；
- commit；
- failure。

---

# 82. Projection Memory

保存：

- projection id；
- carrier；
- task；
- QCap；
- debt；
- transition；
- round-trip results。

---

# 83. Physical Memory

保存：

- device；
- material；
- calibration；
- environment；
- control；
- measured field；
- percept；
- safety events。

---

# 84. History 不等 Snapshot

$$
\boxed{
History
\neq
FinalState.
}
$$

---

# 85. MWT World-State Memory

穩定 world state 至少還需：

$$
\boxed{
(
StableCore,
Branches,
Conflicts,
Unresolved,
History,
Versions,
ReopenSet
).
}
$$

---

# 86. Stable Core 不等 Entire Memory

$$
K_t
$$

只是一部分。

---

# 87. Conflict Memory 不應被「整理掉」

$$
\boxed{
Conflict
\neq
Noise.
}
$$

---

# 88. Unresolved Obligation 也是 Memory

未完成 proof / bridge / evidence task：

$$
U_t.
$$

必須跨時間延續。

---

# 89. Reopen Set

$$
R_t.
$$

保存何時必須重新打開 stable closure。

---

# 90. Dynamic Fixed-Point Continuity

狀態：

$$
\mathfrak M_t
\neq
\mathfrak M_{t+1}
$$

並不表示 identity 失去。

需要：

$$
\Xi_{t\rightarrow t+1}.
$$

---

# 91. Continuity Witness 可以保存

- source lineage；
- world lineage；
- semantic migration；
- certificate migration；
- memory compaction mapping；
- deleted / archived references。

---

# 92. Forgetting 不等 Pruning

$$
\boxed{
Forgetting
\neq
Pruning.
}
$$

---

# 93. Pruning

表示：

> 不在 active / preferred path。

---

# 94. Archiving

表示：

> 轉成低成本保存。

---

# 95. Invalidation

表示：

> 當前不能被依賴。

---

# 96. Erasure

表示：

> 記錄被不可逆刪除或不可恢復。

---

# 97. 四者必須分開

$$
\boxed{
Prune
\neq
Archive
\neq
Invalidate
\neq
Erase.
}
$$

---

# 98. High-Risk Erasure 需要 Audit

不可逆 memory loss 應回答：

- 刪了什麼；
- 為何刪；
- 誰授權；
- 哪些 dependencies 受影響；
- 是否留 tombstone；
- 是否仍有 recovery path。

---

# 99. Semantic Irreversibility

多對一 compression 若沒有 side information：

$$
\boxed{
\text{later intelligence cannot reconstruct distinctions
that were never preserved}.
}
$$

---

# 100. 所以 Raw / Recovery Kernel 很重要

不是所有東西都永遠 full-retain。

但高價值不可逆差異應留 recovery information。

---

# 101. Global Knowledge Absorption

$$
\boxed{
Absorb(x)
\iff
x
\text{ is locatable, relatable, checkable,
reconstructable, reusable}.
}
$$

---

# 102. Read Once 不等 Absorbed

$$
\boxed{
ModelRead(x)
\neq
GlobalAbsorb(x).
}
$$

---

# 103. Embedding 不等 Absorption

$$
\boxed{
EmbeddingStored
\neq
KnowledgeIntegrated.
}
$$

---

# 104. Global Knowledge State

$$
\boxed{
\mathcal K_n
=
(
G_n,
A_n,
C_n,
U_n,
R_n
).
}
$$

---

# 105. $G_n$

knowledge / dependency graph。

---

# 106. $A_n$

axioms / assumptions / definitions。

---

# 107. $C_n$

conflicts / contradictions。

---

# 108. $U_n$

unresolved / undecidable。

---

# 109. $R_n$

reconstructable / executable / verifiable resources。

---

# 110. Global Knowledge Operator

$$
\boxed{
\Phi
=
Reconstruct
\circ
Compress
\circ
Abstract
\circ
Compare
\circ
Verify
\circ
Align
\circ
Normalize.
}
$$

---

# 111. Knowledge Convergence 不等 Summary

$$
\boxed{
KnowledgeConvergence
\neq
Summarization.
}
$$

---

# 112. Generative Knowledge Core

若：

$$
Generate(\mathcal C,\Theta)
\approx
\mathcal D,
$$

則：

$$
\mathcal C
$$

是 generative core。

---

# 113. Generative Core 必須能 Re-expand

不能只是漂亮總結。

---

# 114. Knowledge Density

目標可概念化為：

$$
D(\mathcal K)
=
\frac{
Coverage
+
Generativity
+
Predictivity
+
Transferability
+
Reconstructability
}{
IndependentAssumptions
+
RepresentationComplexity
}.
$$

---

# 115. 收斂不要求檔案數下降

$$
|\mathcal K_{n+1}|
>
|\mathcal K_n|
$$

也可能是進步。

---

# 116. 真正希望下降的是 Independent Explanatory Degrees of Freedom

而不是 bytes。

---

# 117. Memory Breathing

本文承接：

$$
\boxed{
Reveal
\rightarrow
Expand
\rightarrow
Link
\rightarrow
Converge
\rightarrow
Crystallize.
}
$$

---

# 118. Re-expand 必須保留

crystal 不能成為 dead-end summary。

---

# 119. Successful Retrieval Path 也可以記憶

$$
P_{memory}
\rightarrow
\widehat\ell_{memory}.
$$

---

# 120. 但 Retrieval Habit 不等 Truth

成功 route 只是 operational knowledge。

---

# 121. Memory Strategy 可以學習

$$
U(s\mid q,c)
=
Q_s
-
\lambda C_s
-
\mu L_s
-
\nu R_s.
$$

---

# 122. Empirical Preference 不等 Canonical Authority

$$
\boxed{
EmpiricalPreference
\neq
CanonicalAuthority.
}
$$

---

# 123. Memory Need First

Agent 不應：

$$
SearchEverything.
$$

而應先：

$$
Need
\rightarrow
Strategy
\rightarrow
Provider.
$$

---

# 124. Stop Condition

至少：

- task sufficient；
- exact evidence found；
- canonical state resolved；
- no new information；
- budget exhausted；
- identity unresolved；
- authority blocked；
- human review required。

---

# 125. Memory Storm

沒有 stop condition 的 autonomous recall 會：

$$
\boxed{
MemoryStorm.
}
$$

---

# 126. Memory Reconstruction Metrics

本文提出至少：

$$
\mathbf M_{rec}
=
(
F_{state},
F_{lineage},
F_{source},
F_{epi},
F_{cert},
F_{branch},
F_{history},
F_{failure}
).
$$

---

# 127. State Fidelity

能否重建 relevant state。

---

# 128. Lineage Fidelity

能否重建 fork / merge / supersession。

---

# 129. Source Fidelity

能否回到 exact origin。

---

# 130. Epistemic Fidelity

OBS / INF / HYP / RET 等是否被保留。

---

# 131. Certificate Fidelity

是否找得到真正支撐。

---

# 132. Branch Fidelity

是否把 distinct branches 壓錯成一條。

---

# 133. History Fidelity

是否保留 route / transition order。

---

# 134. Failure Fidelity

是否能重建為何以前失敗。

---

# 135. Reconstruction Debt

本文定義：

$$
\boxed{
\mathbf D_{mem}
=
(
D_{source},
D_{identity},
D_{version},
D_{lineage},
D_{semantic},
D_{epistemic},
D_{history},
D_{certificate},
D_{branch},
D_{failure},
D_{replay},
D_{access}
).
}
$$

---

# 136. Source Debt

derived memory 找不到 source。

---

# 137. Identity Debt

不同 object 被錯合併。

---

# 138. Version Debt

當前與歷史版本混淆。

---

# 139. Lineage Debt

fork / merge / correction chain 不完整。

---

# 140. Semantic Debt

crystal 過度概括。

---

# 141. Epistemic Debt

inference 被記成 fact。

---

# 142. History Debt

只剩 final state。

---

# 143. Certificate Debt

claim 有 status 但 certificate 缺失。

---

# 144. Branch Debt

branch 被壓平。

---

# 145. Failure Debt

失敗只記「failed」，未記原因。

---

# 146. Replay Debt

event history 不足以重建 state。

---

# 147. Access Debt

memory 存在但合法 observer 無法取得。

---

# 148. WRMF 正式定義

$$
\boxed{
\mathfrak M_t^{WCO}
=
\left\langle
\mathcal R_t^{raw},
\mathcal E_t^{evt},
\mathcal K_t^{sem},
\mathcal G_t^{mem},
\mathcal X_t^{crystal},
\mathcal B_t^{branch},
\mathcal F_t^{fail},
\mathcal C_t^{cert},
\mathcal H_t^{hist},
\mathcal I_t^{idx},
\mathcal A_t^{access},
\mathcal V_t^{version}
\right\rangle.
}
$$

---

# 149. WRMF 不是一個 Database Product

它是：

$$
\boxed{
\text{memory governance architecture}.
}
$$

---

# 150. SEDB 的位置

$$
\boxed{
SEDB
=
\text{canonical structured semantic evolution / provenance layer}.
}
$$

---

# 151. CSG 的位置

$$
\boxed{
CSG
=
\text{semantic crystallization and routing overlay}.
}
$$

---

# 152. OAM / Memory Fabric 的位置

$$
\boxed{
OAM/MRAF
=
\text{purpose-aware multi-representation retrieval and navigation}.
}
$$

---

# 153. Raw Store 的位置

$$
\boxed{
RawStore
=
\text{exact source and recovery substrate}.
}
$$

---

# 154. Event Store 的位置

$$
\boxed{
EventStore
=
\text{state evolution / replay substrate}.
}
$$

---

# 155. Indexes 的位置

$$
\boxed{
Indexes
=
\text{rebuildable discovery accelerators}.
}
$$

---

# 156. 五者不要坍縮

$$
\boxed{
Raw
\neq
Event
\neq
SemanticState
\neq
Crystal
\neq
Index.
}
$$

---

# 157. Memory-to-World Compiler

本文提出：

$$
\boxed{
\mathsf{MWC}
:
(
\mathfrak M_t^{WCO},
WRC
)
\rightarrow
(
\widehat W_t,
RecCert,
RecDebt
).
}
$$

---

# 158. Memory-to-World-Family Compiler

$$
\boxed{
\mathsf{MWFC}
:
(
\mathfrak M_t^{WCO},
WFRC
)
\rightarrow
(
\widehat{\mathfrak W}_t^G,
FamilyRecCert,
FamilyDebt
).
}
$$

---

# 159. Reconstruction Certificate

$$
\boxed{
RecCert
=
\left\langle
WorldId,
Sources,
Events,
Versions,
Schema,
Branches,
Evidence,
Qualification,
Missing,
Fidelity,
ReplayMode,
Timestamp
\right\rangle.
}
$$

---

# 160. Missing 必須顯式

重建不完整：

$$
Missing\neq\varnothing
$$

時不可默認填空。

---

# 161. Unknown State 是合法 Reconstruction Result

$$
\boxed{
Unknown
\neq
ReconstructionFailure.
}
$$

---

# 162. Unrecoverable State 也要顯式

$$
\boxed{
UNRECOVERABLE
}
$$

比幻覺補全更好。

---

# 163. Memory Write 也是 Candidate / Commit

新 memory：

$$
m_{cand}
$$

不能直接成 canonical。

---

# 164. Memory Commit Gate

$$
\boxed{
CommitMemory
\iff
Validate
\land
Authorize
\land
ProvenanceComplete
\land
VersionConsistent.
}
$$

---

# 165. Routing State 不等 Memory Commit

$$
\boxed{
RoutingState
\neq
MemoryCommit.
}
$$

---

# 166. Write-Back Proposal

cognition 產生：

$$
MemoryWriteCandidate.
$$

---

# 167. 先判定寫什麼類別

- raw event；
- claim；
- crystal；
- relation；
- certificate；
- failure；
- branch state；
- index update。

---

# 168. Derived Index Write 可以低權威

但 canonical claim write 需更高 gate。

---

# 169. Foreign-Memory Contamination

多 agent 系統中：

$$
Agent_A
$$

的 inference 不應自動變成：

$$
Agent_B
$$

的 observed memory。

---

# 170. Memory Namespace / Observer Provenance

每個 memory claim 應能回答：

> 誰知道？

> 怎麼知道？

---

# 171. Shared Memory 不等 Shared Subject

$$
\boxed{
SharedMemory
\neq
SharedSubjectivity.
}
$$

---

# 172. World-Local Memory 不等 World-Global Memory

$$
\boxed{
WorldLocalMemory
\neq
WorldGlobalMemory
\neq
CrossWorldMemory.
}
$$

---

# 173. Branch-Local Secret 不應 Leakage

memory access graph 需與 world authority 對齊。

---

# 174. Cross-World Memory Transport

需要：

$$
MemoryTransportContract.
$$

---

# 175. Simulation Memory 不能自動變 Reality Memory

$$
\boxed{
SimulatedMemory
\neq
ObservedRealityMemory.
}
$$

---

# 176. Memory Layer 與 Paper 05 Domain Layer

每個 memory claim 應保存：

$$
QCap
$$

或相容 epistemic fingerprint。

---

# 177. Memory Layer 與 Paper 04 Observation Layer

每次 observation 應形成可追蹤 memory event。

---

# 178. Memory Layer 與 Paper 03 Computation Layer

computation history / route certificate 可進 memory。

---

# 179. Memory Layer 與 Paper 02 World Layer

WorldId / lineage / mode 是 reconstruction anchor。

---

# 180. Memory Layer 與 Paper 06 Projection Layer

memory projection 是 task-relative view。

projection 不改 canonical memory identity。

---

# 181. Memory Layer 與 Paper 07 Physical Layer

physical calibration history 與 sensor provenance 可決定未來 observation validity。

---

# 182. WCO 七層鏈

至此：

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}
\rightarrow
\mathfrak P_t^G
\rightarrow
\mathsf{PRS}_t
\rightarrow
\mathfrak M_t^{WCO}.
}
$$

---

# 183. 但 Memory 不是末端

Memory 反過來重建：

$$
\mathfrak M_t^{WCO}
\rightarrow
\widehat{\mathfrak W}_{t+1}^G.
$$

---

# 184. 因此 Memory Closing Loop

$$
\boxed{
World
\rightarrow
Experience
\rightarrow
Memory
\rightarrow
Reconstruction
\rightarrow
World'.
}
$$

---

# 185. MVP：World-Reconstructive Memory

第一版不用一次做所有 provider。

---

# 186. MVP Stores

至少：

1. RawSourceStore；
2. EventStore；
3. SemanticClaimStore；
4. ProvenanceStore；
5. BranchStore；
6. CertificateStore；
7. FailureStore；
8. DerivedIndexStore。

---

# 187. MVP Raw Principle

raw 不被 summary overwrite。

---

# 188. MVP Event Principle

correction 用新 event，不 edit 舊 event。

---

# 189. MVP Claim Principle

OBS / INF / HYP / RET 分離。

---

# 190. MVP World Reconstruction

從：

$$
W_0
+
E_{1:t}
$$

重建：

$$
\widehat W_t.
$$

---

# 191. MVP Branch Reconstruction

從 lineage event 重建：

$$
W_0
\rightarrow
W_A,W_B,W_C.
$$

---

# 192. MVP Crystal

每個 session 產生：

- technical crystal；
- decision crystal；
- unresolved crystal。

---

# 193. MVP Retrieval

採：

$$
Structured
+
Lexical
+
VectorDiscovery
+
GraphTraversal.
$$

---

# 194. MVP Failure Memory

故意失敗 route 存入：

$$
FailureStore.
$$

下次相似 task 應可 early surface。

---

# 195. MVP Staleness

source update：

$$
v_1
\rightarrow
v_2
$$

觸發 dependent crystal / claim：

$$
STALE.
$$

---

# 196. MVP Reopen

new evidence 使 archived branch 重新 relevant：

$$
Reopen(W_B).
$$

---

# 197. Experiment 1 — Summary-Only vs Reconstructive Memory

測 world reconstruction success。

---

# 198. Experiment 2 — Vector-Only vs Multi-Representation

測：

- exact source；
- relation；
- history；
- claim status；
- reconstruction。

---

# 199. Experiment 3 — Event Sourcing vs Overwrite

故意進行 correction / downgrade。

測 history recovery。

---

# 200. Experiment 4 — Failure Memory

比較有無 failure graph 的重複探索成本。

---

# 201. Experiment 5 — Crystal First / Source on Demand

測 context cost 與 source fidelity。

---

# 202. Experiment 6 — Branch Reconstruction

故意 prune / archive / reopen。

測 lineage fidelity。

---

# 203. Experiment 7 — Epistemic Fidelity

故意將 INF 與 OBS 混入。

測 memory system 是否維持區分。

---

# 204. Experiment 8 — Certificate Staleness

改 dependency version。

舊 certificate 應被標 stale。

---

# 205. Experiment 9 — Fresh-Context Restore

清空 active context。

只用 WRMF 恢復 task。

測：

$$
TaskSuccess_{restore}.
$$

---

# 206. Experiment 10 — World-Family Regeneration

從 memory 重建：

- root；
- branches；
- modes；
- evidence dependency；
- unresolved obligations。

---

# 207. 可反駁性

本文會被削弱，如果：

1. world reconstruction 指標對長程 task 沒有比普通 retrieval 更高價值；
2. event sourcing 在代表性 knowledge evolution 中沒有改善 audit / recovery；
3. multi-representation memory 比單一 structured store 只增加 overhead；
4. failure memory 無法降低重複探索；
5. crystal/source separation 無法降低 context cost 或提高 fidelity；
6. branch memory 對 long-horizon planning 無用；
7. epistemic-state memory 不降低 fact/inference confusion；
8. simpler summary + vector RAG 在代表性 world-restoration tasks 中完全等效。

---

# 208. 本文不主張什麼

本文不主張：

1. 所有原始資料都必須永久熱存；
2. 所有 raw data 都永遠不能刪除；
3. event sourcing 適合所有資料類型；
4. SEDB 應取代所有 SQL / graph / vector systems；
5. CSG 應取代 raw archive；
6. vector database 沒有價值；
7. semantic crystal 等於 truth；
8. world reconstruction 等於 reality copy；
9. deterministic replay 可重建所有現實事件；
10. failure memory 永遠有效；
11. archived branch 永遠值得 reopen；
12. 所有 memory representations 都必須同時 materialize；
13. memory capacity 等於 context capacity；
14. AI inference 可以無審核進 canonical fact memory；
15. retrieval result 可以自動 commit；
16. shared memory 等於 shared subject；
17. high compression 一定代表高 knowledge convergence；
18. generative core 必然唯一；
19. dynamic fixed point 表示 memory 不再變化；
20. WRMF 已完成 production implementation。

---

# 209. 核心非同一性

$$
\boxed{
Memory
\neq
Context
\neq
Attention.
}
$$

$$
\boxed{
MemoryObject
\neq
Representation
\neq
Index.
}
$$

$$
\boxed{
RawSource
\neq
SemanticCrystal
\neq
ActiveMemory.
}
$$

$$
\boxed{
Claim
\neq
Fact.
}
$$

$$
\boxed{
InferenceMemory
\neq
ObservationMemory.
}
$$

$$
\boxed{
Retrieval
\neq
ContextInclusion
\neq
MemoryCommit.
}
$$

$$
\boxed{
HistoricalReconstruction
\neq
PerfectRealityReplay.
}
$$

$$
\boxed{
Prune
\neq
Archive
\neq
Invalidate
\neq
Erase.
}
$$

$$
\boxed{
KnowledgeConvergence
\neq
Summarization.
}
$$

---

# 210. 核心母式一：WCO Memory State

$$
\boxed{
\mathfrak M_t^{WCO}
=
\left\langle
\mathcal R_t^{raw},
\mathcal E_t^{evt},
\mathcal K_t^{sem},
\mathcal G_t^{mem},
\mathcal X_t^{crystal},
\mathcal B_t^{branch},
\mathcal F_t^{fail},
\mathcal C_t^{cert},
\mathcal H_t^{hist},
\mathcal I_t^{idx},
\mathcal A_t^{access},
\mathcal V_t^{version}
\right\rangle.
}
$$

---

# 211. 核心母式二：Memory-to-World Compiler

$$
\boxed{
\mathsf{MWC}
:
(
\mathfrak M_t^{WCO},
WRC
)
\rightarrow
(
\widehat W_t,
RecCert,
RecDebt
).
}
$$

---

# 212. 核心母式三：Memory-to-World-Family Compiler

$$
\boxed{
\mathsf{MWFC}
:
(
\mathfrak M_t^{WCO},
WFRC
)
\rightarrow
(
\widehat{\mathfrak W}_t^G,
FamilyRecCert,
FamilyDebt
).
}
$$

---

# 213. 核心母式四：Knowledge Absorption

$$
\boxed{
Absorb(x)
\iff
x
\text{ is locatable, relatable, checkable,
reconstructable, and reusable}.
}
$$

---

# 214. 核心母式五：Global Knowledge Operator

$$
\boxed{
\Phi
=
Reconstruct
\circ
Compress
\circ
Abstract
\circ
Compare
\circ
Verify
\circ
Align
\circ
Normalize.
}
$$

---

# 215. 核心母式六：Memory Loop

$$
\boxed{
World
\rightarrow
Experience
\rightarrow
Memory
\rightarrow
Reconstruction
\rightarrow
World'.
}
$$

---

# 216. 結論：長期智能的關鍵不是「記得很多」，而是「未來還能重新建立現在」

最弱的記憶觀是：

$$
\text{save text}.
$$

再強一點是：

$$
\text{retrieve similar text}.
$$

再強一點是：

$$
\text{structured knowledge graph}.
$$

但對類全域 AI 而言，真正關鍵的問題變成：

> 如果今天的 active context、model process、runtime session 都消失，明天的 AI 能不能重新知道現在發生過什麼？

它是否能重建：

- canonical object identity；
- world state；
- world lineage；
- branches；
- conflicts；
- observations；
- computation routes；
- epistemic qualification；
- projection choice；
- physical calibration；
- failed attempts；
- certificates；
- unresolved obligations；
- reopen conditions？

如果不能，那麼它只是擁有一個大型 archive。

如果可以，它才開始具有：

$$
\boxed{
\text{Reconstructive Long-Term Cognition}.
}
$$

因此本文認為：

$$
\boxed{
\text{Long-Term Memory Quality}
\neq
\text{Stored Token Count}.
}
$$

更合理的衡量是：

$$
\boxed{
\text{Reconstruction Fidelity}
+
\text{Lineage Fidelity}
+
\text{Epistemic Fidelity}
+
\text{Source Fidelity}
+
\text{Replayability}
+
\text{Failure Recoverability}.
}
$$

這也改變了「壓縮」的定義。

真正好的 memory compression 不是：

> 把十萬字變成一千字。

而是：

> 用更低成本的生成核心、semantic crystals、events、indexes 與 provenance roots，保留未來需要時重新展開重要差異的能力。

所以：

$$
\boxed{
\text{Compression}
\neq
\text{Forgetting}.
}
$$

以及：

$$
\boxed{
\text{Memory Convergence}
=
\text{lower active complexity}
+
\text{preserved reconstructability}.
}
$$

類全域 AI 不需要永遠把所有東西放在 context。

它甚至不應這麼做。

它真正需要的是：

$$
\boxed{
\text{a governed memory fabric that can hide most history,
reveal the right fragments,
expand back to sources,
reconstruct world state,
regenerate branches,
and preserve the reasons why the present became the present}.
}
$$

因此：

$$
\boxed{
\text{A Global-Like AI does not need to keep everything active;}
}
$$

但它需要：

$$
\boxed{
\text{to preserve enough structured, versioned,
provenance-bearing and reconstructable memory
to rebuild the worlds, branches, qualifications,
failures and histories that future cognition may need}.
}
$$

到此 WCO 七個主要層已形成：

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}
\rightarrow
\mathfrak P_t^G
\rightarrow
\mathsf{PRS}_t
\rightarrow
\mathfrak M_t^{WCO}.
}
$$

但記憶層同時把箭頭折回：

$$
\boxed{
\mathfrak M_t^{WCO}
\rightarrow
\widehat{\mathfrak W}_{t+1}^G.
}
$$

下一篇將進入：

# Paper 09
## 執行層：方法選擇、MSSP、RDR、WFS 與 Runtime Routing

正式回答：

> 當 world、memory、computation、observer、domain、projection 與 physical capability 都存在後，類全域 AI 到底如何把「我想做什麼」變成真正可執行、可驗證、可停止、可重規劃的 runtime plan？

---

# 217. 下一篇接口

Paper 09 將處理：

- intent；
- capability discovery；
- MSSP structural routing；
- CAIR semantic authority；
- RDR materialization / dispatch；
- WFS world scheduling；
- computation router；
- memory router；
- observer router；
- projection router；
- execution plan graph；
- candidate / commit；
- stop condition；
- replan；
- failure recovery；
- runtime receipt；
- cross-layer scheduler separation；
- Mother Runtime / orchestration shell。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K × Aletheia，《Operator-Assisted Memory：算子標籤、混合檢索與可解釋 AI 知識導航》，2026。
2. Neo.K × Aletheia，《Multi-Representation Autonomous Memory Fabric 統合技術白皮書》，2026。
3. Neo.K，《AI 原生語義演化資料庫：SEDB / SEQL》，2026。
4. Neo.K × Aletheia，《Crystallized Semantic Graph：結晶化語義圖長期記憶架構》，2026。
5. Neo.K × AI，《全域知識收斂論：AI、資訊海與萬有理論的生成極限》，2026。
6. Neo.K × Aletheia，《PNCW Paper 02：Virtual Context Projection》，2026。
7. Neo.K × Aletheia，《MWT-04：World State, Branch Convergence, and Dynamic Fixed Points》，2026。
8. Neo.K × Aletheia，《DTIL Runtime Unified Historical State Architecture》，2026。
9. Neo.K × Aletheia，《WCO Paper 01–07》，2026。
10. Neo.K × Aletheia，《AI-Native Game Runtime / Agentic World Reconstruction》，2026。

## External Research Interfaces

11. Fowler, M. (2005). *Event Sourcing*.
12. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.
13. Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS.
14. Cao, Y. et al. (2024). *LEGO-GraphRAG: Modularizing Graph-based Retrieval-Augmented Generation for Design Space Exploration*. arXiv:2411.05844.
15. W3C. *PROV-O: The PROV Ontology*.
16. Tulving, E. (1985). *Memory and Consciousness*. Canadian Psychology.
17. Squire, L. R. (2004). *Memory Systems of the Brain: A Brief History and Current Perspective*. Neurobiology of Learning and Memory.

---

**Paper 08 狀態：COMPLETE v0.1**  
**下一篇：Paper 09 — 執行層：方法選擇、MSSP、RDR、WFS 與 Runtime Routing**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
