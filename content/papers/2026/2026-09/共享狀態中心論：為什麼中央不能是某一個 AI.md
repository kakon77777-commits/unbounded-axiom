# 共享狀態中心論：為什麼中央不能是某一個 AI

## Shared-State Centrality: Why the Center Should Not Be a Single AI

**系列**：AI 原生分散式組織系列，第 4 篇／共 10 篇  
**系列英文名**：AI-Native Distributed Organization Series  
**文件編號**：EML-ANDO-2026-04-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Shared State／Canonical Source／Distributed Agent Organization／Governance Runtime  
**狀態**：Public Theory Draft  
**直接前置**：《從 AI 工具到 AI 組織：操作員退出問題》v0.1；《委任主權論》v0.1；《非階層式 Agent 組織》v0.1；《Interaction-Time Runtime & Agent Temporal Ledger v0.1》  
**Source fingerprint**：見正式 source package `SHA256SUMS.txt`

---

## 生成與保真聲明

本文為 AI 輔助生成之理論與工程框架草稿。本文不主張已證明某種單一架構對所有 multi-agent system 都最優，也不提供新的大規模企業或 Agent runtime 實證資料。本文中的數學表達主要用於形式化狀態、權限、一致性、提交與恢復條件；若未來版本加入 benchmark、平台效能、資料一致性測試或外部文獻引用，應另行驗證與重現。

本文所稱「中央」主要指邏輯上的 canonical coordination center，不等於單一伺服器、單一資料庫、單一模型或單一治理者。核心主張是：

$$
\boxed{
\text{Logical State Centrality}
\neq
\text{Physical Centralization}
\neq
\text{Single-Agent Centralization}.
}
$$

---

## 摘要

當 AI-native 組織開始使用多個可替換 Agent、動態協作拓撲、跨模型委任與長時程 workflow 時，一個根本問題立即出現：如果每個 Agent 都只依賴自身 context、memory 或私有摘要保存「目前做到哪裡」，那麼 Agent 一旦替換、失效、斷線、壓縮上下文或彼此產生不同版本，組織就會發生狀態分裂。此時所謂的分散式組織，實際上只是多個彼此部分失憶的認知孤島。

本文提出「共享狀態中心論」（Shared-State Centrality）：AI-native 組織可以是 Agent 分散、角色動態、模型可替換、執行拓撲可變的，但其可被共同引用與審計的 canonical organizational state 必須具有邏輯中心性。真正的中心不應是某一個 AI，而應是外部化、版本化、可驗證、可恢復、可權限控制的共享狀態結構。

本文定義 canonical shared organizational state：

$$
\mathcal R_t
=
(
I_t,
T_t,
C_t,
E_t,
A_t,
P_t,
B_t,
V_t,
L_t,
W_t
),
$$

其中分別對應意圖、任務圖、主張、證據、權限、政策、預算、驗證狀態、事件／血統帳本與世界提交狀態。Agent 不應成為 source of truth，而應是 reader、reasoner、proposer、executor 與 bounded writer。其私有 context 可作為工作快取，但不應替代 canonical state。

本文進一步提出四平面架構：State Plane、Agent Plane、Governance Plane、Commit Plane。並區分「邏輯單一真實來源」與「物理單點」：canonical state 可以透過多副本、event sourcing、content-addressed artifacts、append-only ledger、資料庫交易、版本向量或其他一致性機制實現，而不要求單台中央機器。不同 state class 可採不同一致性要求：高風險 authority / commit state 需要更強一致性；低風險工作草稿可以容許 eventual consistency。

本文也提出 Shared-State Invariants、State Freshness、Canonicality Ratio、State Divergence、Recovery Completeness、Agent Replaceability 與 Commit Integrity 等診斷量，並描述 stale-state execution、split-brain authority、memory capture、summary drift、orphan artifact、hidden mutation 與 state poisoning 等失敗模式。

本文最後指出：如果 AI-native organization 希望真正做到「Agent 可以一直換，但組織不能一起失憶」，那麼其核心必須從 Agent-centric architecture 轉向 State-centric architecture。這將直接使論文庫、研究圖譜、驗證紀錄、任務狀態與 artifact lineage 由靜態資料庫轉變為可持續運行的 Research Environment，並為本系列第 5 篇建立基礎。

**關鍵詞**：Canonical Shared State、State-Centric Architecture、Multi-Agent Memory、Event Sourcing、Distributed State、Agent Replaceability、Organizational Memory、Authority Ledger、World Commit、Shared State Fabric

---

# 0. 核心問題：如果 Agent 一直換，什麼不能跟著消失？

第 3 篇允許：

$$
G_t
\rightarrow
G_{t+1}
$$

透過：

$$
\text{spawn},
\text{split},
\text{merge},
\text{reroute},
\text{replace},
\text{retire}
$$

持續重組。

但如果任務狀態只存在：

$$
Context(A_i)
$$

而：

$$
A_i
\rightsquigarrow
A_j,
$$

則：

$$
State(A_i)
\not\Rightarrow
State(A_j).
$$

因此：

$$
\boxed{
\text{Replaceable Agents require persistent externalized state.}
}
$$

---

# 1. Agent-Centric Architecture 的問題

最直覺的 multi-agent 架構是：

$$
A_1
\leftrightarrow
A_2
\leftrightarrow
A_3.
$$

每個 Agent 各自保存：

- 對話記憶；
- 任務摘要；
- 對其他 Agent 的理解；
- 自己認為的完成狀態；
- 自己記得的權限。

短 run 中這可能可行。

長期組織中則容易形成：

$$
S_1
\neq
S_2
\neq
S_3.
$$

也就是每個 Agent 都活在略有不同的「組織現實」。

---

# 2. Shared-State Centrality

本文提出：

$$
A_i
\leftrightarrow
\mathcal R_t
\leftrightarrow
A_j.
$$

其中：

$$
\mathcal R_t
$$

不是某個 Agent，而是 shared canonical state。

因此：

$$
\boxed{
\text{The center is state, not personality.}
}
$$

Agent 的角色變成：

$$
A_i
=
Read(\mathcal R_t)
+
Reason
+
Propose
+
Act
+
WriteBounded(\mathcal R_t).
$$

---

# 3. Canonical Shared Organizational State

定義：

$$
\mathcal R_t
=
(
I_t,
T_t,
C_t,
E_t,
A_t,
P_t,
B_t,
V_t,
L_t,
W_t
).
$$

其中：

$$
I_t
=
\text{Intent State},
$$

$$
T_t
=
\text{Task / Dependency State},
$$

$$
C_t
=
\text{Claim State},
$$

$$
E_t
=
\text{Evidence State},
$$

$$
A_t
=
\text{Authority State},
$$

$$
P_t
=
\text{Policy State},
$$

$$
B_t
=
\text{Budget / Resource State},
$$

$$
V_t
=
\text{Verification State},
$$

$$
L_t
=
\text{Lineage / Event Ledger},
$$

$$
W_t
=
\text{World-Commit State}.
$$

這些 state class 不必物理儲存在同一資料庫，但必須形成同一個可解析的 canonical organizational reality。

---

# 4. 邏輯中心不等於物理中心

區分：

$$
C_L
=
\text{Logical Centrality},
$$

$$
C_P
=
\text{Physical Centralization},
$$

$$
C_A
=
\text{Agent Centralization}.
$$

一個系統可以滿足：

$$
C_L
\text{ high},
$$

但：

$$
C_P
\text{ low}
$$

且：

$$
C_A
\text{ low}.
$$

也就是：

> 所有節點知道哪個版本算正式，不表示正式資料只能放一台機器，更不表示只有一個 AI 能理解與修改它。

---

# 5. Source of Truth 與 Source of Intelligence

$$
\boxed{
\text{Source of Truth}
\neq
\text{Source of Intelligence}.
}
$$

最強模型可以負責最複雜推理，但不應因此成為：

$$
\text{Canonical Memory}.
$$

因為：

- 模型會替換；
- context 會截斷；
- memory 會摘要；
- provider 會改；
- session 會消失；
- reasoning result 可能出錯。

因此：

$$
\boxed{
\text{Model Context}
=
\text{Working Memory / Cache},
}
$$

而不是：

$$
\text{Canonical State}.
$$

---

# 6. 四平面架構

## 6.1 State Plane

保存：

$$
\mathcal R_t.
$$

回答：

> 現在正式狀態是什麼？

## 6.2 Agent Plane

包含：

$$
\mathcal A_t
=
\{
A_1,A_2,\ldots,A_n
\}.
$$

回答：

> 現在哪些智能節點可以工作？

## 6.3 Governance Plane

保存：

$$
\Gamma_t,
A_t,
P_t.
$$

回答：

> 誰可以做什麼？什麼情況需要批准、撤銷或 escalation？

## 6.4 Commit Plane

控制：

$$
Candidate
\rightarrow
Verified
\rightarrow
Committed.
$$

回答：

> 哪些只是草稿？哪些已驗證？哪些已對外生效？

---

# 7. Shared State 不是一個超巨大 JSON

共享狀態可寫為：

$$
\mathcal R_t
=
\bigcup_{k=1}^{m}
R_t^{(k)}.
$$

不同 state class 可使用不同 backend：

- task state：relational DB / graph；
- artifact：object store；
- event：append-only ledger；
- authority：transactional store；
- research claim：knowledge graph；
- provenance：content-addressed manifest；
- temporary cache：KV。

因此：

$$
\boxed{
\text{Canonicality is semantic, not a file format.}
}
$$

---

# 8. Event-Sourced Organizational Memory

一種自然做法是將狀態改變記為事件：

$$
e_1,e_2,\ldots,e_n.
$$

並令：

$$
\mathcal R_t
=
Fold(
\mathcal R_0,
e_1,
e_2,
\ldots,
e_n
).
$$

事件可包括：

$$
TaskCreated,
TaskAssigned,
ClaimAdded,
EvidenceLinked,
AuthorityGranted,
AuthorityRevoked,
ValidationPassed,
ArtifactCommitted.
$$

本文不主張 event sourcing 是唯一方案，而要求：

$$
\boxed{
\text{State mutation must be attributable and sufficiently reconstructable for its risk class.}
}
$$

---

# 9. 狀態版本與 stale write

令：

$$
v_t
=
Version(\mathcal R_t).
$$

Agent 讀取：

$$
v_i.
$$

提交前檢查：

$$
v_i
=
v_{current}.
$$

若：

$$
v_i
\neq
v_{current},
$$

則需要：

$$
Rebase,
Merge,
Reject,
Retry
$$

之一。

這避免舊版本 Agent 直接覆蓋新狀態。

---

# 10. State Freshness

Agent 在：

$$
t_0
$$

讀取：

$$
S_{t_0},
$$

但到：

$$
t_1
$$

才執行。

此時可能：

$$
S_{t_1}
\neq
S_{t_0}.
$$

定義：

$$
\Delta_S
=
t_{current}
-
t_{read}.
$$

或概念上的：

$$
F_S
=
Freshness(S).
$$

高風險 action 應要求：

$$
F_S
\ge
F^\star.
$$

---

# 11. Typed Consistency

不是所有 state 都需要同樣的一致性。

例如：

$$
K(R^{draft})
=
EventualConsistency,
$$

而：

$$
K(R^{authority})
=
StrongConsistency
$$

可能更合理。

同理，高影響 financial / legal commit 可以要求比 telemetry 更嚴格的一致性。

因此：

$$
K:
StateClass
\rightarrow
ConsistencyRequirement.
$$

這比「全部強一致」或「全部 eventual」更適合異質 Agent 組織。

---

# 12. Authority Split Brain

最危險的狀態分裂之一是：

$$
A_1:
Authority(X)=Granted,
$$

而：

$$
A_2:
Authority(X)=Revoked.
$$

此時形成：

$$
\boxed{
\text{Authority Split Brain}.
}
$$

所以：

$$
A_t
$$

必須比一般 draft state 有更高一致性與傳播要求。

---

# 13. Model Memory 只能是 Cache

對任一 Agent：

$$
M_i
=
\text{private memory / context}.
$$

更合理的關係是：

$$
M_i
=
Cache_i(\mathcal R_t)
+
PrivateScratch_i.
$$

PrivateScratch 可以不共享。

但一旦某結果要影響組織：

$$
PrivateScratch
\rightarrow
Proposal
\rightarrow
CanonicalWrite.
$$

所以：

$$
\boxed{
\text{Private Memory}
\neq
\text{Organizational Memory}.
}
$$

---

# 14. Summary Drift

若 handoff 只依賴：

$$
S
\rightarrow
Summary_1
\rightarrow
Summary_2
\rightarrow
Summary_3,
$$

每一次都可能損失資訊。

長鏈容易形成：

$$
\text{Summary Drift}.
$$

Shared state 的目的之一，就是避免讓自然語言摘要單獨承擔 canonical memory。

---

# 15. Claim-Evidence State

研究組織中特別重要的是：

$$
C_t
$$

與：

$$
E_t.
$$

不能只保存文章全文，而應保存：

$$
Claim
\leftrightarrow
Evidence
\leftrightarrow
Verification
\leftrightarrow
Artifact.
$$

例如：

$$
c_i
=
(
\text{text},
\text{type},
\text{source},
\text{confidence},
\text{status},
\text{dependencies}
).
$$

如此 Agent 才能分辨：

- 已驗證事實；
- 外部引用；
- 數學猜想；
- 未驗證推論；
- AI 生成 candidate。

---

# 16. Artifact Lineage

每個 artifact：

$$
a_j
$$

應可追溯：

$$
Inputs(a_j),
Agent(a_j),
Version(a_j),
Validation(a_j),
Parent(a_j).
$$

因此：

$$
L(a_j)
=
\text{artifact lineage}.
$$

這使論文、程式、圖片、測試報告與社群內容都能保留生成鏈。

---

# 17. Content Addressability

對 immutable artifact：

$$
h(a)
=
Hash(a).
$$

以：

$$
h(a)
$$

作為內容身份的一部分。

這不表示所有系統都必須使用 blockchain，而只是：

$$
\boxed{
\text{Content identity can be separated from location and agent identity.}
}
$$

---

# 18. Agent Replaceability

令任務：

$$
\tau
$$

原由：

$$
A_i
$$

執行。

若：

$$
A_i
\rightsquigarrow
A_j,
$$

定義恢復品質：

$$
Q_R
=
Q(
Resume(A_j|\mathcal R_t)
).
$$

若：

$$
Q_R
\ge
Q^\star,
$$

則該任務具有可接受 replaceability。

---

# 19. Recovery Completeness

定義：

$$
RC
=
\frac{
|\text{recoverable required state}|
}{
|\text{required state}|+\epsilon
}.
$$

理想：

$$
RC
\rightarrow1.
$$

如果 Agent crash 後：

- 任務狀態找不到；
- 權限不清；
- 最新 artifact 不知道在哪；
- validator 結果遺失；

則：

$$
RC
\ll1.
$$

---

# 20. Canonicality Ratio

定義：

$$
CR
=
\frac{
|\text{decision-relevant state represented canonically}|
}{
|\text{decision-relevant state}|+\epsilon
}.
$$

若：

$$
CR\rightarrow1,
$$

重要組織狀態大多可以共同解析。

若：

$$
CR\ll1,
$$

組織仍高度依賴：

> 某個 Agent 還記得。

---

# 21. State Divergence

令：

$$
\widehat{\mathcal R}_t^{(i)}
$$

為 Agent $A_i$ 的局部視圖。

定義概念上的：

$$
D_S^{(i)}
=
d(
\widehat{\mathcal R}_t^{(i)},
\mathcal R_t
).
$$

整體：

$$
D_S
=
\frac{1}{n}
\sum_{i=1}^{n}
D_S^{(i)}.
$$

實作時可以依 state class 使用不同 metric。

---

# 22. Hidden Mutation

若 Agent 直接修改 canonical state，卻沒有：

$$
Actor,
Timestamp,
Reason,
ParentVersion,
Authority,
Validation,
$$

則形成：

$$
\text{Hidden Mutation}.
$$

高價值 mutation 至少應滿足：

$$
Mutation
\rightarrow
Attribution
+
Lineage
+
Authority
+
Version.
$$

---

# 23. State Poisoning

共享狀態也有一個新的危險：

> 錯誤一旦被寫成 canonical，所有 Agent 都可能共同相信它。

因此：

$$
\boxed{
\text{Shared State amplifies both truth and error.}
}
$$

所以 canonical write 應依內容 class 決定：

$$
WriteClass,
ValidationClass,
RollbackPolicy.
$$

---

# 24. Provisional 與 Canonical 必須分離

定義：

$$
S^{prop}
=
\text{provisional state},
$$

$$
S^{can}
=
\text{canonical state}.
$$

任何 Agent 都可以產生：

$$
\Delta S^{prop}.
$$

但只有通過 policy 的狀態才可以：

$$
\Delta S^{prop}
\rightarrow
\Delta S^{can}.
$$

因此：

$$
\boxed{
\text{Agent Output}
\neq
\text{Organizational Truth}.
}
$$

---

# 25. Commit Semantics

沿用 ITR/ATL：

$$
Intent
\rightarrow
Plan
\rightarrow
Run
\rightarrow
Validation
\rightarrow
Completion
\rightarrow
Commit.
$$

共享狀態應清楚區分：

$$
Candidate,
Validated,
Committed,
Published,
Archived.
$$

尤其：

$$
Committed
\neq
Published.
$$

內部 canonical commit 不必等於對外公開。

---

# 26. Shared-State Invariants

本文提出第一代不變量。

## Invariant 1

$$
CanonicalMutation
\Rightarrow
Logged.
$$

## Invariant 2

$$
WorldAction
\Rightarrow
AuthorityLineage.
$$

## Invariant 3

$$
Commit
\Rightarrow
ParentVersion.
$$

## Invariant 4

非 root Agent 不應成為唯一 state holder。

## Invariant 5

$$
Proposal
\neq
Canonical.
$$

## Invariant 6

高價值 state 必須存在可接受 recovery path。

## Invariant 7

authority revocation 必須快速傳播至相關 Agent。

## Invariant 8

world commit 必須可追溯：

$$
Agent,
Policy,
Authority,
SourceArtifact.
$$

---

# 27. Canonical 不等於絕對真理

Shared-state centrality 最危險的誤用，是把：

$$
\mathcal R_t
$$

當成不可挑戰的神諭。

本文明確區分：

$$
\boxed{
\text{Canonicality}
\neq
\text{Epistemic Infallibility}.
}
$$

Canonical 只表示：

> 這是組織目前正式採用的版本。

因此仍必須允許：

$$
Challenge,
Correction,
Deprecation,
Rollback,
Fork.
$$

---

# 28. Canonical Fork

在真正爭議尚未解決時，可以形成：

$$
\mathcal R_t^{(a)},
\mathcal R_t^{(b)}.
$$

但必須明示：

$$
Status
=
Forked.
$$

避免兩個分支都假裝自己是唯一真實狀態。

最後可：

$$
Merge,
Select,
Archive.
$$

---

# 29. 從 Corpus 到 Research Environment

普通論文庫主要回答：

> 有哪些文章？

Research Environment 則需要回答：

- 哪些研究線仍活躍？
- 哪些 claim 未驗證？
- 哪些文章彼此依賴？
- 哪些數學命題等待形式驗證？
- 哪些引用需要更新？
- 哪些 artifact 完成但未 publish？
- 哪些 Agent 正處理哪個 branch？
- 哪些工作可平行？
- 哪些問題需要 human governance？

因此：

$$
\boxed{
\text{Corpus}
+
\text{State}
+
\text{Graph}
+
\text{Verification}
+
\text{Runtime}
=
\text{Research Environment}.
}
$$

---

# 30. State-Centric Organization

本文最終提出：

$$
\text{Agent-Centric Organization}
\rightarrow
\text{State-Centric Organization}.
$$

Agent-centric 模式關心：

> 誰記得？

State-centric 模式關心：

> 現在 canonical 地知道什麼？由誰產生？證據是什麼？狀態是什麼？誰驗證過？

因此 Agent 成為：

$$
\boxed{
\text{Replaceable Intelligence over Persistent Organizational State}.
}
$$

---

# 31. 第一代診斷向量

定義：

$$
\mathbf Z_S
=
(
CR,
D_S,
RC,
F_S,
Q_R,
Q_L,
Q_C,
R_{split},
R_{poison}
).
$$

其中：

- $CR$：Canonicality Ratio；
- $D_S$：State Divergence；
- $RC$：Recovery Completeness；
- $F_S$：State Freshness；
- $Q_R$：Replaceability / Resume Quality；
- $Q_L$：Lineage Quality；
- $Q_C$：Commit Integrity；
- $R_{split}$：Split-Brain Risk；
- $R_{poison}$：State Poisoning Risk。

---

# 32. 可檢驗命題

## 命題一：Externalized-State Replaceability

若 decision-relevant state 被充分 externalize，Agent replacement 的恢復品質應提高。

## 命題二：Canonicality-Divergence Relation

在相同工作負載下，提高：

$$
CR
$$

應降低：

$$
D_S
$$

至某一合理區間。

## 命題三：Summary-Only Degradation

只依賴自然語言 handoff summary 的長鏈 Agent 系統，在 chain depth 增加時更容易發生 state drift。

## 命題四：Typed Consistency Advantage

依 state class 配置不同一致性要求，比全域統一採最強或最弱一致性更可能取得合理成本與安全折衷。

## 命題五：Shared-State Error Amplification

canonical state 一旦被錯誤污染，其影響節點數通常高於私有 memory error，因此 canonical write 應具有更嚴格 verification contract。

## 命題六：State-Centric Continuity

若：

$$
\mathcal R_t
$$

保持完整，即使：

$$
\mathcal A_t
$$

大量替換，組織 continuity 仍可維持。

---

# 33. 第一代實驗設計

## 33.1 Agent Replacement Test

比較：

$$
PrivateMemoryOnly
$$

與：

$$
CanonicalSharedState.
$$

測量：

$$
ResumeLatency,
Q_R,
RC.
$$

## 33.2 Long-Handoff Drift Test

讓：

$$
A_1
\rightarrow
A_2
\rightarrow
\cdots
\rightarrow
A_n
$$

只靠 summary relay，再與 shared-state 版本比較。

## 33.3 Authority Revocation Propagation

撤銷 authority，測量所有受影響 Agent 收到新狀態所需時間。

## 33.4 State Poisoning Injection

故意寫入錯誤 claim，測試 validator、rollback、lineage 與 affected-agent detection。

## 33.5 Split-Brain Simulation

製造：

$$
\mathcal R^{(a)}
\neq
\mathcal R^{(b)}
$$

並測試 conflict resolution。

## 33.6 Model Provider Swap

不保留原 session context，直接更換模型，測試能否從：

$$
\mathcal R_t
$$

恢復工作。

---

# 34. 與前三篇的閉合

第 1 篇：

$$
HumanOperator
\rightarrow
OperationalExit.
$$

第 2 篇：

$$
Delegation
+
RetainedSovereignty.
$$

第 3 篇：

$$
PermanentTree
\rightarrow
DynamicGraph.
$$

本篇補上：

$$
DynamicGraph
+
ReplaceableAgents
\Rightarrow
CanonicalSharedState.
$$

因此目前形成：

$$
\boxed{
\text{Operator Exit}
\rightarrow
\text{Delegated Sovereignty}
\rightarrow
\text{Dynamic Topology}
\rightarrow
\text{Shared State}.
}
$$

---

# 35. 與下一篇的接口

只要：

$$
\mathcal R_t
$$

可以保存：

- research claims；
- evidence；
- theory dependencies；
- paper lineage；
- active tasks；
- verification state；
- unresolved branches；

論文庫就不再只是被查詢的資料集合。

它開始成為：

$$
\boxed{
\text{Executable Research Environment}.
}
$$

下一篇將處理：

# **分散式認知研究組織：論文庫如何從 Corpus 變成 Research Environment**

其核心轉換是：

$$
\boxed{
\text{Knowledge Base}
\rightarrow
\text{Research State}
\rightarrow
\text{Research Organization}.
}
$$

---

# 36. 理論限制

第一，shared state 本身可能形成新的單點故障，因此需要 replication、backup、permission separation 與 recovery strategy。

第二，不同資料類型的一致性需求很難一次正確設定；過強一致性可能降低效能，過弱則造成治理錯誤。

第三，externalization 不是免費的。把 private reasoning 全部結構化可能成本過高，因此必須區分必要 canonical state 與可拋棄 scratch state。

第四，資料模型若設計不良，可能把研究與創造力過度形式化。

第五，canonical state 仍可能錯誤。它只是正式版本，不是絕對真理。

第六，本文不要求保存模型私有 chain-of-thought；組織需要保存的是可治理、可驗證、可追溯的 decision-relevant state。

---

# 37. 結論

AI-native 分散式組織真正需要的「中央」，不是一個永遠在線、永遠記得全部事情、永遠負責路由所有 Agent 的超級 AI。

真正需要的是：

$$
\boxed{
\text{A canonical, externalized, versioned, auditable shared state.}
}
$$

因此：

$$
\boxed{
\text{The organization may be decentralized in agency while centralized in canonical reference.}
}
$$

更精確地說：

$$
\boxed{
\text{Logical State Centrality}
+
\text{Distributed Intelligence}
+
\text{Distributed Execution}
+
\text{Bounded Governance}
}
$$

可以同時成立。

Agent 可以一直換：

$$
A_1
\rightsquigarrow
A_2
\rightsquigarrow
A_3.
$$

角色可以一直變：

$$
Role_t(A_i)
\neq
Role_{t+1}(A_i).
$$

拓撲可以一直重組：

$$
G_t
\neq
G_{t+1}.
$$

但：

$$
\boxed{
\mathcal R_t
}
$$

必須維持可追溯 continuity。

這就是從「很多 AI 一起工作」走向「可持續存在的 AI-native organization」的關鍵。

而當共享狀態開始包含研究 claim、證據、理論依賴、未解問題與驗證狀態時：

$$
\boxed{
\text{論文庫不再只是庫，而開始變成會運行的研究環境。}
}
$$

---

# 符號表

| 符號 | 定義 |
|---|---|
| $\mathcal R_t$ | canonical shared organizational state |
| $I_t$ | Intent State |
| $T_t$ | Task / Dependency State |
| $C_t$ | Claim State |
| $E_t$ | Evidence State |
| $A_t$ | Authority State |
| $P_t$ | Policy State |
| $B_t$ | Budget / Resource State |
| $V_t$ | Verification State |
| $L_t$ | Lineage / Event Ledger |
| $W_t$ | World-Commit State |
| $C_L$ | Logical Centrality |
| $C_P$ | Physical Centralization |
| $C_A$ | Agent Centralization |
| $M_i$ | Agent private memory / context |
| $\Delta_S$ | State Staleness |
| $F_S$ | State Freshness |
| $S^{prop}$ | Provisional State |
| $S^{can}$ | Canonical State |
| $RC$ | Recovery Completeness |
| $CR$ | Canonicality Ratio |
| $D_S$ | State Divergence |
| $Q_R$ | Agent Resume / Replaceability Quality |

---

# 前置依賴

1. Neo.K with Aletheia，《從 AI 工具到 AI 組織：操作員退出問題》v0.1，2026。
2. Neo.K with Aletheia，《委任主權論：高 AI 自主與高人類主權能否共存》v0.1，2026。
3. Neo.K with Aletheia，《非階層式 Agent 組織：從管理樹到動態協作圖》v0.1，2026。
4. Neo.K，《互動時間拓撲：平行 Agent、偏序因果與不可約互動深度》v0.1，2026。
5. Neo.K，《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1，2026。
6. Neo.K，《AI 單次品質論：意圖忠實度、過程品質、完成度與結果品質》v0.1，2026。
7. Neo.K，《Interaction-Time Runtime & Agent Temporal Ledger v0.1》，2026。

---

# 版本紀錄

- **v0.1 / 2026-08-20**：建立 Shared-State Centrality、Canonical Shared Organizational State、四平面架構、邏輯中心／物理中心／Agent 中心分離、typed consistency、state freshness、state divergence、recovery completeness、canonicality ratio、state poisoning 與 Shared-State Invariants。
