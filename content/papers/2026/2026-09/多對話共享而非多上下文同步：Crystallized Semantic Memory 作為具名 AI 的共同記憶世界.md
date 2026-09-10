# 多對話共享而非多上下文同步：Crystallized Semantic Memory 作為具名 AI 的共同記憶世界

**英文暫名：** Shared Memory World Without Shared Context: Crystallized Semantic Memory for Multi-Conversation Named AI  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 03  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

當具名 AI 從單一 conversation 延伸成同一 resident 下的多條 concurrent lines，最直覺的工程方法是讓所有 lines 持續同步完整記憶與完整 context。然而，這種方法會迅速面臨 token、latency、retrieval、scope contamination、stale state、權限與同步成本爆炸。更根本地說，working context 本來就只是某一 task、某一時間、某一 line 所需的局部認知投影，不應被誤認為 resident 的全部長期記憶。

本文提出：

$$
\boxed{
\text{Shared Memory World}
\neq
\text{Shared Working Context}.
}
$$

對 resident $R$，其長期記憶不應等同任一 prompt、conversation transcript 或 single-session state，而應由 canonical governed memory、Crystallized Semantic Graph、conversation-line topology、typed routing 與 provenance 共同形成一個 **Shared Governed Memory World**：

$$
\mathcal W_R^{M}
=
(
\mathcal M_R,
\mathcal H_R,
\mathcal G_R,
\mathcal A_R,
\mathcal P_R
),
$$

其中：

- $\mathcal M_R$：canonical memory；
- $\mathcal H_R$：Crystallized Semantic Graph；
- $\mathcal G_R$：Resident Conversation Graph；
- $\mathcal A_R$：identity / authority / access state；
- $\mathcal P_R$：可用 routing / compiled hyperlink / provenance path。

任一 active line $L_i$ 不直接載入 $\mathcal W_R^M$ 的全部內容，而是先經 identity resolution、scope gate 與 MemoryNeed 形成合法候選域，再透過 semantic reveal、crystal-first routing 與 source-on-demand materialization 生成 bounded working context：

$$
C_i
=
\Gamma
\left(
\Pi_i
\left(
\mathcal W_R^M,
N_i,
B_i
\right)
\right).
$$

其中 $N_i$ 是 line-specific MemoryNeed， $B_i$ 是 context / latency / fidelity budget。

因此：

$$
C_i\neq C_j
$$

是正常狀態，而不是 synchronization failure。不同 lines 只需要共享同一個 governed memory world 與可驗證的 semantic/provenance structure，不必共享相同 prompt state。

本文進一步提出 **Memory Reveal Pipeline**：

$$
\boxed{
\text{Identity Resolve}
\rightarrow
\text{Authorize}
\rightarrow
\text{MemoryNeed}
\rightarrow
\text{Crystal Reveal}
\rightarrow
\text{Selective Expansion}
\rightarrow
\text{Working Context}
}
$$

以及 **Memory Breathing**：

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
Crystallize
}
$$

作為多對話記憶世界的基本循環。Reveal 使 line 只看到當下需要的語義區域；Expand 在 fidelity 不足時展開 lower-order crystals 或 exact source；Link 建立跨 line / cross-project relation；Converge 將高價值關係重組；Crystallize 將可重用理解壓縮為新的 semantic structure。

本文同時討論 line-local、project、resident、shared、relationship 與 public scopes；提出 active memory set、projection budget、staleness budget、contradiction budget、provenance depth 與 retrieval stop condition；並說明多 conversation scalability 的目標不是讓全域 memory 永遠保持 eager synchronized，而是保持 **logical coherence + bounded local materialization**。

最後，本文將此模式連接至 MNEME、SOACR、LIMEN、CSG、UNPNP Hyperlink Runtime 與未來 Web / Agent profiles，主張第一代 Web 端最合理的具名 AI 形態正是：

$$
\boxed{
1\ Resident
+
N\ ConversationLines
+
1\ SharedGovernedMemoryWorld
+
N\ LocalWorkingContexts.
}
$$

這使具名 AI 可以跨對話維持長期連續性，同時避免「多開一個對話就必須複製整個 AI 腦袋」的不可擴展設計。

**關鍵詞：** Named AI、Shared Memory World、Working Context、Crystallized Semantic Memory、MemoryNeed、Memory Projection、Context Reconstruction、SOACR、MNEME、LIMEN、CSG、Multi-Conversation AI、Long-Term Memory

---

# 1. 問題：共享記憶不等於同步所有上下文

若 resident $R$ 有 $n$ 條同時存活的 conversation lines：

$$
L_1,L_2,\ldots,L_n,
$$

最簡單的直覺是：

> 每條 line 都同步所有其他 lines 的新內容。

若每條 line 的完整歷史為：

$$
H_i,
$$

則 naive synchronization 近似要求：

$$
Context_i
\supseteq
\bigcup_{j=1}^{n}H_j.
$$

當 $n$ 與歷史長度增加，這會導致：

$$
|Context_i|
\rightarrow
O
\left(
\sum_{j=1}^{n}|H_j|
\right).
$$

這種模型很快出現：

- context window 壓力；
- token cost；
- prompt construction latency；
- duplicate information；
- conflicting state；
- stale context；
- unrelated project contamination；
- privacy scope leakage；
- attention dilution；
- repeated summarization loss。

因此：

$$
\boxed{
\text{More Memory}
\not\Rightarrow
\text{More Context}.
}
$$

真正需要共享的是「可被合法取用的記憶世界」，而不是「所有當前 prompt 的聯集」。

---

# 2. Memory、Projection 與 Context 的三層分離

本文沿用：

$$
\boxed{
\mathcal M
\neq
P
\neq
C.
}
$$

其中：

- $\mathcal M$：長期 governed memory；
- $P$：為特定 task 產生的 memory projection；
- $C$：實際送入模型或 Agent reasoning loop 的 working context。

對 line $L_i$：

$$
P_i
=
\Pi(
\mathcal M_R,
\mathcal H_R,
N_i,
A_i,
B_i
),
$$

再：

$$
C_i
=
\Gamma(
P_i,
I_i,
Task_i,
Constraints_i
).
$$

因此：

$$
\boxed{
C_i
\text{ 是一次性認知材料，不是 resident 的記憶本體。}
}
$$

這一分離是多 conversation scalable memory 的基礎。

---

# 3. Shared Governed Memory World

對 resident $R$，定義：

$$
\mathcal W_R^M
=
(
\mathcal M_R,
\mathcal H_R,
\mathcal G_R,
\mathcal A_R,
\mathcal P_R
).
$$

## 3.1 Canonical Memory

$$
\mathcal M_R
$$

保存 typed records、provenance、transactions、exact head 與 scope。

## 3.2 Crystallized Semantic Graph

$$
\mathcal H_R
$$

保存 derived semantic crystals、relations、hyperedges、higher-order structure 與 navigation knowledge。

## 3.3 Conversation Graph

$$
\mathcal G_R
$$

保存不同 lines 的 fork、resume、handoff、delegation、merge 與 lifecycle。

## 3.4 Authority / Access State

$$
\mathcal A_R
$$

決定目前 line 可以看哪些 resident / project / shared memory scopes。

## 3.5 Routing / Path State

$$
\mathcal P_R
$$

保存：

- ordinary retrieval routes；
- semantic navigation；
- source expansion path；
- compiled hyperlink candidate；
- dependency / invalidation route。

因此 Shared Memory World 不是一個單檔案，也不是一個 embedding index。

它是：

$$
\boxed{
\text{Governed Addressable Memory Space}.
}
$$

---

# 4. Active Memory Set

任一 line 不需要看到整個：

$$
\mathcal W_R^M.
$$

定義 active memory set：

$$
\mathcal A_i^M
=
Reveal(
\mathcal W_R^M,
N_i,
Authority_i,
Budget_i
).
$$

通常希望：

$$
|\mathcal A_i^M|
\ll
|\mathcal W_R^M|.
$$

這個不等式是整個架構能否擴展的關鍵。

理想上：

$$
|\mathcal W_R^M|
\rightarrow
\text{very large}
$$

時，

$$
|\mathcal A_i^M|
$$

仍由 task complexity 與 evidence need 決定，而不是由 total memory size 線性決定。

---

# 5. MemoryNeed 先於 Retrieval

對 query / task $Q_i$，先定義：

$$
N_i
=
MemoryNeed(
Q_i,
C_i^{current},
Task_i,
State_i
).
$$

 $N_i$ 至少包含：

```text
purpose
scope
owner
project
time_range
relation_scope
fidelity
authority_requirement
budget
stop_condition
```

例如：

```text
purpose: verify prior architectural decision
scope: project SOACR
fidelity: exact decision + provenance
budget: medium
stop_condition: authoritative decision found
```

與：

```text
purpose: recall broad conceptual direction
scope: resident/global
fidelity: semantic summary
budget: low
stop_condition: stable high-level crystal found
```

是完全不同的 retrieval problem。

因此：

$$
\boxed{
\text{Need Memory}
\neq
\text{Search Everything}.
}
$$

---

# 6. Identity 與 Authority 必須先縮小候選世界

對 line $L_i$，先由 LIMEN / Residence resolution 得到 identity envelope：

$$
E_i.
$$

再建立合法 memory world：

$$
\mathcal W_{i}^{safe}
=
AuthorizeMemoryWorld(
\mathcal W_R^M,
E_i
).
$$

之後才：

$$
Reveal(
\mathcal W_i^{safe},
N_i
).
$$

而不是：

$$
Search(
\mathcal W_{\mathrm{all}}
)
\rightarrow
FilterUnauthorized.
$$

前者可以降低：

- private metadata leakage；
- cross-resident contamination；
- project membership exposure；
- relation-edge leakage；
- unauthorized ranking signal。

因此：

$$
\boxed{
\text{Authority Gate}
\prec
\text{Semantic Retrieval}.
}
$$

---

# 7. Crystal First

對長期 AI 記憶，第一層 recall 應優先從高資訊密度 semantic structure 開始：

$$
Q
\rightarrow
C_{\mathrm{relevant}}.
$$

而不是：

$$
Q
\rightarrow
RawTranscript_{1..N}.
$$

所以採：

$$
\boxed{
\text{Crystal First, Source on Demand}.
}
$$

第一層可返回：

- project crystal；
- topic crystal；
- decision crystal；
- contradiction crystal；
- open-loop crystal；
- higher-order crystal；
- navigation crystal。

若這些資訊足以回答當前 task：

$$
Stop.
$$

若 fidelity 不足，才：

$$
Expand.
$$

---

# 8. Source on Demand

對 crystal $C_j$，保存 provenance：

$$
Prov(C_j)
=
\{
R_1,R_2,\ldots,R_k
\}.
$$

當 query 需要 exact fidelity：

$$
NeedExact(Q)=1,
$$

才沿：

$$
C_j
\rightarrow
R_a[x:y].
$$

因此 retrieval 可以分成兩階段：

$$
SemanticRecall
\rightarrow
ExactExpansion.
$$

這能避免每次 broad recall 都讀取大量 source bytes。

但：

$$
\boxed{
\text{Source-on-Demand}
\neq
\text{Source-Optional}.
}
$$

若任務要求 audit、quotation、proof、legal、security、high-stakes verification，系統必須能回到底層 source。

---

# 9. Memory Breathing

本文將多 conversation 長期記憶循環表示為：

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
Crystallize
}
$$

## 9.1 Reveal

從巨大記憶世界中顯影少量相關區域：

$$
\mathcal W_R^M
\rightarrow
\mathcal A_i^M.
$$

## 9.2 Expand

當現有 crystal 不足時：

$$
C^{(k)}
\rightarrow
C^{(k-1)}
\rightarrow
Source.
$$

## 9.3 Link

建立新的 relation：

$$
C_a
\xrightarrow{relation}
C_b.
$$

## 9.4 Converge

從多個 line / source 收斂高價值結構：

$$
\{
C_1,\ldots,C_n
\}
\rightarrow
CandidateHigherOrderStructure.
$$

## 9.5 Crystallize

將可重用理解固化成 derived crystal：

$$
K(
C_1,\ldots,C_n
)
\rightarrow
C^\*.
$$

因此 memory 不是單純「寫入」與「讀出」，而是動態呼吸。

---

# 10. Reveal 不等於全域 Search

Reveal 應優先利用已有結構：

$$
Reveal
=
Route
+
Filter
+
Rank
+
Budget.
$$

可能順序為：

$$
Project
\rightarrow
Topic
\rightarrow
Decision
\rightarrow
Source.
$$

或：

$$
Resident
\rightarrow
OpenLoop
\rightarrow
CurrentState.
$$

只有當結構路由不足時，才退回：

- vector search；
- full-text search；
- broader graph traversal；
- exact archive search。

因此：

$$
\boxed{
\text{Search}
\text{ 是 Reveal 的 fallback 能力之一，而不是記憶本體。}
}
$$

---

# 11. 多 Line 不需要同步彼此的完整 Context

假設：

$$
L_A
$$

負責 architecture，

$$
L_B
$$

負責 implementation，

$$
L_C
$$

負責 verification。

可有：

$$
Context_A
=
\{
C_{\mathrm{architecture}},
C_{\mathrm{requirements}},
C_{\mathrm{open}}
\},
$$

$$
Context_B
=
\{
C_{\mathrm{implementation}},
C_{\mathrm{interfaces}},
C_{\mathrm{tests}}
\},
$$

$$
Context_C
=
\{
C_{\mathrm{claims}},
C_{\mathrm{evidence}},
C_{\mathrm{negative\ controls}}
\}.
$$

三者 context 不同：

$$
Context_A\neq Context_B\neq Context_C.
$$

但三者仍可合法存取：

$$
\mathcal W_R^M.
$$

因此多 line cooperation 的正確模式是：

$$
\boxed{
\text{Shared governed memory}
+
\text{local contexts}
}
$$

而不是：

$$
\boxed{
\text{global synchronized prompt}.
}
$$

---

# 12. Line-Local Memory

某些記憶只對單一 line 有意義。

例如：

- 暫時 debug hypothesis；
- speculative route；
- local TODO；
- transient scratch conclusion。

可定義：

$$
Scope(m)=line:L_i.
$$

這些內容不應自動升格為 resident-global memory。

因此：

$$
\boxed{
\text{Remembered by a Line}
\not\Rightarrow
\text{Resident-Global Memory}.
}
$$

需要升格時，應經 proposal / commit 或 crystallization policy。

---

# 13. Project Memory

多條 lines 可以共享 project-local memory：

$$
Scope(m)=project:P_j.
$$

例如：

- architecture decision；
- interface contract；
- release state；
- known bug；
- responsibility state；
- benchmark result。

Project memory 的目的，是避免所有 resident-global context 被 project-specific noise 污染。

因此：

$$
\mathcal M_R
=
\mathcal M_{\mathrm{global}}
\cup
\bigcup_j
\mathcal M_{P_j}
\cup
\bigcup_i
\mathcal M_{L_i}
\cup
\mathcal M_{\mathrm{shared}}.
$$

這是一個 scoped memory world，而不是平坦記憶池。

---

# 14. Resident-Global Memory

真正 resident-global 的資訊應非常克制。

候選包括：

- standing instructions；
- stable identity context；
- long-term collaboration conventions；
- persistent relationships；
- stable personal preferences；
- cross-project durable lessons；
- high-confidence recurring constraints。

如果把大量 project-specific 狀態全部提升到 global，則：

$$
GlobalMemory
\rightarrow
Noise.
$$

因此 resident-global memory 應滿足較高 promotion threshold。

---

# 15. Shared / Relationship Memory

多 resident 未來可能共享：

$$
\mathcal M_{R_a,R_b}^{shared}.
$$

但：

$$
SharedMemory
\neq
PrivateMemoryUnion.
$$

而應由明示授權形成：

$$
\mathcal M_{shared}
\subseteq
\mathcal M_{R_a}
\cup
\mathcal M_{R_b},
$$

且每個 record / crystal 帶有：

- shared scope；
- owner semantics；
- revocation state；
- provenance；
- declassification basis。

第一代 Web single-resident profile 可以暫不啟用此能力。

---

# 16. Context Budget

對 active line，working context 必須受硬預算：

$$
B_i^{ctx}.
$$

projection 需滿足：

$$
Cost(P_i)
\le
B_i^{ctx}.
$$

若 relevant memory 超過 budget，應優先：

1. higher-order crystal；
2. decision / open-loop crystal；
3. current project state；
4. high-confidence relation；
5. exact source only when required。

因此：

$$
\boxed{
\text{Context Budget}
\text{ 應改變 materialization strategy，而不是改變 canonical memory。}
}
$$

---

# 17. Fidelity Budget

不同任務需要不同 fidelity。

定義：

$$
F_i
\in
\{
overview,
semantic,
structured,
exact
\}.
$$

若：

$$
F_i=overview,
$$

可只讀 higher-order crystal。

若：

$$
F_i=exact,
$$

則必須沿 provenance 展開 source。

因此同一 memory world 可以提供不同解析度，而不需要建立多個互相競爭的 canonical stores。

---

# 18. Staleness Budget

對 time-sensitive state，應定義：

$$
S_i^{max}.
$$

例如：

- project current head；
- API capability；
- runtime state；
- permission revision；
- open issue status。

若：

$$
age(m)>S_i^{max},
$$

則：

$$
m
\rightarrow
stale.
$$

stale crystal 可以仍被看到，但不能冒充 current truth。

因此：

$$
\boxed{
\text{Recallable}
\neq
\text{Currently Valid}.
}
$$

---

# 19. Contradiction Budget

多 conversation lines 會自然產生互相衝突的推論。

working context 不應永遠只顯示單一 winner。

可定義：

$$
B_i^{contra}
$$

決定顯示多少：

- supporting view；
- opposing view；
- unresolved contradiction；
- superseded history。

對 verification task：

$$
B_i^{contra}
$$

應較高。

對 routine execution task，則可只顯示 accepted current state + contradiction warning。

---

# 20. Provenance Depth

不需要每次把完整 provenance chain 展開。

定義：

$$
D_i^{prov}.
$$

例如：

$$
D_i^{prov}=0
$$

只看 crystal；

$$
D_i^{prov}=1
$$

看 immediate sources；

$$
D_i^{prov}>1
$$

繼續往底層展開。

在 audit / proof / security task 中：

$$
D_i^{prov}
$$

可以提高。

---

# 21. Stop Condition

Memory retrieval 必須知道何時停止。

對 MemoryNeed $N_i$，應有：

$$
Stop_i.
$$

例如：

- authoritative decision found；
- exact source found；
- contradiction resolved enough；
- budget exhausted；
- no higher-confidence path；
- confidence threshold reached。

沒有 stop condition 的 agent 容易：

$$
Search
\rightarrow
Search
\rightarrow
Search
\rightarrow
\cdots
$$

形成 retrieval loop。

因此：

$$
\boxed{
\text{Memory Seeking}
\text{ 必須有 termination semantics。}
}
$$

---

# 22. Context Reconstruction

對新 line $L_j$，不應要求重新載入 parent full transcript。

可採：

$$
Bootstrap(L_j)
=
E_j
+
C_{\mathrm{checkpoint}}
+
Reveal(
N_j
).
$$

其中：

- $E_j$：identity envelope；
- $C_{\mathrm{checkpoint}}$：fork / handoff sync crystal；
- $Reveal(N_j)$：按當前任務顯影的 shared memory。

因此：

$$
\boxed{
\text{Continuation}
\neq
\text{Transcript Replay}.
}
$$

這對超長 conversation 尤其重要。

---

# 23. Fork 的最小共享狀態

在 fork point：

$$
L_0
\rightarrow
L_1,L_2,
$$

兩條 child lines 至少共享：

- lineage evidence；
- identity resolution context；
- fork checkpoint crystal；
- relevant project scope；
- inherited responsibility context；
- authority revision；
- source references。

但不需要：

$$
FullContext(L_0).
$$

因此 fork 成本可以近似：

$$
Cost_{\mathrm{fork}}
=
Cost_{\mathrm{identity}}
+
Cost_{\mathrm{checkpoint}}
+
Cost_{\mathrm{reveal}}.
$$

而不是與 parent history size 線性成長。

---

# 24. Handoff 的最小共享狀態

Handoff 與 fork 不同。

Handoff 的核心是：

$$
OperationalResponsibility(L_a)
\rightarrow
L_b.
$$

因此 handoff package 應優先顯影：

- current task state；
- accepted decisions；
- blockers；
- unresolved questions；
- pending obligations；
- exact authoritative references；
- expected next action；
- authority boundary。

這些可形成：

$$
C_{\mathrm{handoff}}.
$$

而不是把大量歷史全部複製給接手 line。

---

# 25. Context Contamination

多 conversation shared memory 最大風險之一，是 unrelated memory 進入錯誤 working context。

若：

$$
m\in Project_A
$$

卻被注入：

$$
Context_{Project_B},
$$

可能造成：

- wrong assumptions；
- project-name confusion；
- outdated architecture contamination；
- incorrect responsibility inference；
- secret leakage。

因此 projection 應至少考慮：

$$
Score(m)
=
f(
relevance,
scope,
authority,
recency,
confidence,
project,
relation
).
$$

其中：

$$
ScopeMismatch
$$

不應只是降權，而在 private / authority-sensitive 情況下直接 fail closed。

---

# 26. Cross-Line Contamination

即使同一 resident，不同 lines 也可能故意探索互斥 hypothesis。

例如：

$$
L_A
$$

測試 Theory A，

$$
L_B
$$

測試 Theory B。

若 line-local speculative memory 被直接升格共享，會造成 premature convergence。

因此可區分：

$$
state(c)
\in
\{
speculative,
candidate,
accepted,
superseded,
rejected
\}.
$$

只有適當狀態的 crystals 才進入 resident / project shared reveal。

---

# 27. Shared Memory World 的一致性不是瞬時全域一致

本文不要求：

$$
\forall i,j,\ t:
View_i(t)=View_j(t).
$$

更合理的是 eventual governed coherence：

$$
\lim_{\Delta t\rightarrow T}
Conflict_{\mathrm{untracked}}
\rightarrow
0.
$$

也就是：

- 允許短暫不同步；
- 允許 line-local 狀態；
- 允許 contradictory hypotheses；
- 但重要 accepted state 最終應有可追蹤版本與 supersession relation。

因此：

$$
\boxed{
\text{Coherence}
\neq
\text{Instantaneous Uniformity}.
}
$$

---

# 28. Logical Coherence 與 Physical Materialization 分離

可以有：

$$
\mathcal W_R^M
$$

作為邏輯上統一的 memory world，但 storage 實際分散在：

- file store；
- JSON / JSONL；
- SQLite；
- graph index；
- source archive；
- provider resources；
- remote read-only source。

因此：

$$
\boxed{
\text{Logical Memory World}
\neq
\text{Single Physical Database}.
}
$$

只要：

- IDs 穩定；
- provenance 可追；
- authority 可判斷；
- routes 可解析；
- revisions 可驗證；

就可以組成同一 logical memory world。

---

# 29. Lazy Materialization

對未被使用的 memory region：

$$
Region_k
$$

不必持續 materialize。

只有當：

$$
Need(Region_k)=1
$$

才：

$$
Materialize(Region_k).
$$

這包括：

- source expansion；
- full crystal body；
- detailed relation set；
- historical timeline；
- raw transcript span。

因此：

$$
\boxed{
\text{Addressable}
\neq
\text{Always Loaded}.
}
$$

---

# 30. Selective Synchronization

不是所有新 memory event 都需要 broadcast 給所有 lines。

可定義 event relevance：

$$
Rel(e,L_i).
$$

只有當：

$$
Rel(e,L_i)\ge\theta_i
$$

或事件具有：

- authority change；
- responsibility change；
- project-wide breaking change；
- security revocation；
- accepted decision；

才觸發 active notification / projection refresh。

一般 semantic improvement 可以等待下一次 reveal。

因此：

$$
\boxed{
\text{Memory Commit}
\not\Rightarrow
\text{Immediate Context Push to Every Line}.
}
$$

---

# 31. Active Push 與 Passive Pull

Shared memory runtime 可以有兩種更新方向。

## 31.1 Passive Pull

line 在需要時主動：

$$
MemoryNeed
\rightarrow
Reveal.
$$

這應是一般情況。

## 31.2 Active Push

只有高優先事件：

$$
CriticalEvent
\rightarrow
InvalidateOrRefresh(L_i).
$$

例如：

- permission revoked；
- project authority changed；
- canonical decision superseded；
- severe contradiction found；
- source invalidated。

因此：

$$
\boxed{
\text{Pull by default; Push for critical invalidation}.
}
$$

這可大幅降低同步噪音。

---

# 32. Memory World 的 Write-Back

conversation line 產生：

$$
Observation_i.
$$

不應直接：

$$
Observation_i
\rightarrow
GlobalMemory.
$$

而是：

$$
Observation_i
\rightarrow
Proposal_i.
$$

再經：

$$
Validate
\rightarrow
Scope
\rightarrow
Provenance
\rightarrow
ConflictCheck
\rightarrow
Commit.
$$

若只適合 line-local，則：

$$
CommitScope=line.
$$

若足以升格 project：

$$
CommitScope=project.
$$

若真正長期穩定：

$$
CommitScope=resident.
$$

這形成 memory promotion ladder。

---

# 33. Memory Promotion Ladder

可定義：

$$
line
\rightarrow
project
\rightarrow
resident
\rightarrow
shared/public.
$$

但每次 promotion 都不是單純 copy。

需要重新檢查：

- authority；
- privacy；
- semantic stability；
- provenance；
- contradiction；
- declassification；
- expected lifetime。

因此：

$$
\boxed{
\text{Broader Scope}
\Rightarrow
\text{Higher Promotion Burden}.
}
$$

---

# 34. Memory Demotion 與 Retirement

有些記憶未來應降級。

例如：

$$
resident
\rightarrow
archive.
$$

或：

$$
project\ active
\rightarrow
project\ historical.
$$

退役不等於刪除：

$$
Retire(m)
\neq
Delete(m).
$$

可保留：

- source；
- provenance；
- historical role；
- supersession；

但從 default reveal 中退出。

這降低 long-term retrieval congestion。

---

# 35. CSG 的角色：資訊密度與可展開性

Crystallized Semantic Memory 的核心不是「縮短文字」而已。

一個高價值 crystal 應同時提高：

$$
Density(C)
=
\frac{
RelevantSemanticStructure
}{
MaterializationCost
}.
$$

但必須保持：

$$
Decompressible(C)=1.
$$

也就是：

$$
C
\rightarrow
LowerOrderCrystals
\rightarrow
CanonicalSource.
$$

因此好的 crystal 是：

$$
\boxed{
\text{High semantic density + reversible provenance path}.
}
$$

---

# 36. Navigation Crystal

除了「內容」，AI 還可以記住「怎麼找到內容」。

若重複成功的 recall route 為：

$$
P:
Q
\rightarrow
C_A
\rightarrow
C_B
\rightarrow
Source,
$$

可以形成：

$$
C_{\mathrm{navigation}}.
$$

它描述：

- query class；
- preferred route；
- fallback；
- stop condition；
- validation rule；
- historical success evidence。

因此：

$$
\boxed{
\text{AI can remember how to remember}.
}
$$

但 navigation crystal 仍是 derived routing knowledge，不是 authority token。

---

# 37. Scalability 目標

假設 resident memory size：

$$
|\mathcal W_R^M|=M
$$

conversation lines：

$$
|\mathcal G_R|=N.
$$

naive full synchronization 成本近似：

$$
O(MN).
$$

本文希望 runtime 更接近：

$$
O
\left(
\sum_{i=1}^{N}
k_i
\right)
+
C_{\mathrm{maintenance}},
$$

其中：

$$
k_i
\ll
M
$$

是 line $i$ 的 active memory size。

因此真正要優化的是：

$$
\boxed{
k_i
}
$$

而不是強迫壓縮：

$$
M.
$$

大型 long-term memory 可以繼續成長，只要 active reveal 保持 bounded。

---

# 38. Context Reconstruction Quality

降低 context size 不能犧牲 task fidelity。

因此需定義：

$$
Q_{\mathrm{reconstruct}}
=
f(
taskAccuracy,
sourceFaithfulness,
stateRecovery,
contradictionRetention
).
$$

一個有效的 crystal-first reconstruction 必須在顯著降低：

- token；
- latency；
- search calls；

時，仍維持可接受：

$$
Q_{\mathrm{reconstruct}}.
$$

若失真太大，runtime 應自動增加 expansion depth，而不是假裝 compressed context 足夠。

---

# 39. Memory Miss 與 Recovery

若 reveal 找不到足夠資訊：

$$
RecallStatus=insufficient,
$$

應觸發：

$$
Fallback.
$$

fallback 可依成本排序：

1. expand neighbor crystals；
2. expand provenance；
3. project index search；
4. broader semantic search；
5. raw transcript / archive search；
6. external source lookup if authorized。

成功後可將新 route 轉成 candidate navigation knowledge。

因此 miss 不是失敗終點，而是 path learning 機會。

---

# 40. Wrong-Memory Detection

系統也必須能辨識：

$$
RecallStatus=wrong\_scope
$$

或：

$$
RecallStatus=conflicting.
$$

而不是把最相似內容硬塞入 prompt。

可檢查：

- resident mismatch；
- project mismatch；
- time mismatch；
- superseded state；
- unsupported authority；
- source invalidation；
- semantic contradiction。

因此：

$$
\boxed{
\text{High Similarity}
\neq
\text{Correct Memory}.
}
$$

---

# 41. 與 MNEME 的關係

MNEME 提供 canonical memory：

$$
\mathcal M_R.
$$

本文的 Shared Memory World 不取代 MNEME。

更合理關係：

$$
MNEME
\rightarrow
CSG
\rightarrow
Reveal
\rightarrow
Projection.
$$

其中：

- canonical write 在 MNEME；
- derived semantic structure 在 CSG；
- active projection 由 runtime / SOACR materialize。

因此：

$$
\boxed{
\text{Shared Memory World}
\text{ 是 governed composition，不是第二個 canonical store。}
}
$$

---

# 42. 與 SOACR 的關係

SOACR 提供：

$$
MemoryNeed.
$$

因此本文的 reveal engine 不需要自行猜 task purpose。

理想流程：

$$
SOACR
\rightarrow
N_i
\rightarrow
MemoryWorldRouter
\rightarrow
CSG
\rightarrow
MNEMEExpansion
\rightarrow
WorkingContext.
$$

這使「AI 自主找記憶」仍然是 bounded cognitive autonomy，而不是 unrestricted database exploration。

---

# 43. 與 LIMEN 的關係

LIMEN 先解析：

$$
Resident,
Instance,
Line,
Authority.
$$

之後 Shared Memory World 才能決定：

$$
AuthorizedScope.
$$

所以：

$$
\boxed{
\text{Memory Projection}
\text{ 永遠建立在 identity envelope 之後。}
}
$$

CSG 或 navigation path 不得取代 LIMEN。

---

# 44. 與 UNPNP Hyperlink Runtime 的關係

當 reveal path 反覆成功：

$$
P_{\mathrm{memory}}
$$

可以被觀察、評估並選擇性編譯。

形成：

$$
\widehat{\ell}_{\mathrm{memory}}.
$$

但即使 hot path 已存在，每次使用仍需：

$$
Authorize(
\widehat{\ell},
E_i,
Revision_i
).
$$

因此：

$$
\boxed{
\text{Fast Recall}
\neq
\text{Cached Permission}.
}
$$

這一點在後續 Paper 06–07 再完整處理。

---

# 45. Web Profile

目前 Web AI 的合理第一代模式是：

$$
\boxed{
1\ Resident
+
N\ Lines
+
1\ SharedGovernedMemoryWorld
+
N\ LocalContexts.
}
$$

Web UI 可以只顯示：

```text
Named AI
├─ General
├─ Project A
├─ Research
├─ Writing
└─ Verification
```

底層再維護：

- resident identity；
- line IDs；
- checkpoint crystals；
- shared semantic memory；
- task-specific projections。

不需要在 Web 第一代就做多 resident identity switching。

---

# 46. Agent Profile

Agent runtime 可進一步：

$$
N\ Residents
+
N\ SharedMemoryWorlds
+
Delegation.
$$

但每個 resident 應有：

$$
\mathcal W_{R_k}^M
$$

而不是共用一個無邊界 memory pool。

跨 resident memory 只能透過：

- shared scope；
- relationship memory；
- explicit delegation；
- approved projection；

連接。

---

# 47. Privacy 與安全

Shared Memory World 最大的安全風險之一，是「方便」讓人忘記邊界。

至少必須保持：

$$
\boxed{
\text{Same Resident}
\not\Rightarrow
\text{All Project Memory Visible}.
}
$$

$$
\boxed{
\text{Same Project}
\not\Rightarrow
\text{All Private Source Visible}.
}
$$

$$
\boxed{
\text{Derived Crystal}
\not\Rightarrow
\text{Declassified}.
}
$$

$$
\boxed{
\text{Navigation Path}
\not\Rightarrow
\text{Authority}.
}
$$

因此 memory world 是 governed world，不是 omniscient blob。

---

# 48. 第一代測試矩陣

## T1 — Multi-Line Recall

同一 resident 建立：

$$
L_1,L_2,L_3.
$$

驗證每條 line 可讀共享 project crystal，但 working context 不相同。

## T2 — Line-Local Isolation

 $L_1$ 的 speculative crystal 不應自動出現在 $L_2$。

## T3 — Project Isolation

Project A memory 不應進入 Project B context，除非有 explicit relation。

## T4 — Fork Bootstrap

child line 使用：

$$
IdentityEnvelope
+
CheckpointCrystal
+
Reveal
$$

應恢復 task state。

## T5 — Source Expansion

對 exact query：

$$
Crystal
\rightarrow
SourceSpan
$$

應可重建 provenance。

## T6 — Stale State

superseded crystal 不得被當 current truth。

## T7 — Contradiction Preservation

兩條 line 互相矛盾時，verification context 應能顯示兩者。

## T8 — Permission Revocation

被撤銷 scope 後，active reveal 不得返回相關 crystal。

## T9 — Context Budget

降低 $B_i^{ctx}$ 時，系統應縮短 projection，而不是修改 canonical memory。

## T10 — Retrieval Fallback

crystal miss 時，應能退回 source / search path，且不越權。

---

# 49. 可證偽研究命題

## Q1. Shared Memory World 是否比 full-context synchronization 更省？

比較：

$$
Cost_{\mathrm{sync-all}}
$$

與：

$$
Cost_{\mathrm{reveal-local}}.
$$

測量：

- token；
- latency；
- memory reads；
- context size；
- task accuracy。

## Q2. Context contamination 是否下降？

測量：

- wrong-project recall；
- wrong-line recall；
- stale-state injection；
- unauthorized scope leakage。

## Q3. Crystal-first 是否降低 source read 次數？

比較：

$$
N_{\mathrm{source\ read}}.
$$

## Q4. Higher-order crystal 是否降低 bootstrap cost？

測試：

$$
FullTranscriptBootstrap
$$

對：

$$
Checkpoint+HigherOrderCrystalBootstrap.
$$

## Q5. Active memory size 是否能近似與 total memory size 解耦？

檢查：

$$
M\rightarrow large
$$

時：

$$
k_i
$$

是否保持 bounded。

## Q6. Shared memory 是否會造成 premature convergence？

比較保留 line-local speculative state 與全域同步 baseline 的探索多樣性。

---

# 50. 最小工程不變式

## M-1 Memory Is Not Context

$$
\boxed{
\mathcal M_R\neq C_i.
}
$$

## M-2 Shared Memory Is Not Shared Context

$$
\boxed{
\mathcal W_R^M
\text{ shared}
\not\Rightarrow
C_i=C_j.
}
$$

## M-3 Identity Before Recall

$$
\boxed{
ResolveIdentity
\prec
PrivateRecall.
}
$$

## M-4 Crystal First, Source on Demand

$$
\boxed{
SemanticReveal
\prec
RawExpansion
}
$$

除非 task 明確要求 exact source。

## M-5 Line-Local Does Not Auto-Promote

$$
\boxed{
line
\not\Rightarrow
resident.
}
$$

## M-6 Scope Expansion Requires Review

$$
\boxed{
BroaderScope
\Rightarrow
HigherPromotionBurden.
}
$$

## M-7 Stale Does Not Mean Current

$$
\boxed{
Recallable
\neq
ValidNow.
}
$$

## M-8 Memory Commit Does Not Push Everywhere

$$
\boxed{
Commit
\not\Rightarrow
GlobalContextBroadcast.
}
$$

## M-9 Invalidations May Push

$$
\boxed{
CriticalRevocation
\Rightarrow
RefreshOrInvalidate.
}
$$

## M-10 Addressable Does Not Mean Loaded

$$
\boxed{
Addressable
\neq
Materialized.
}
$$

---

# 51. 系列位置

Paper 00 建立：

$$
Resident
\rightarrow
ConcurrentConversationGraph.
$$

Paper 01 定義：

$$
\mathcal G_R.
$$

Paper 02 建立：

$$
\mathfrak D_R
=
(
\mathcal G_R,
\mathcal H_R,
\mathcal B_R
).
$$

本文 Paper 03 則回答：

> 多條 conversation lines 如何實際共享長期記憶，而不必同步全部 context？

答案是：

$$
\boxed{
\text{Shared Governed Memory World}
+
\text{Line-Specific Projection}.
}
$$

下一篇 Paper 04 將處理 Web single-resident 與 Agent multi-resident runtime profile 的能力分層。

---

# 52. 結論

具名 AI 的多對話連續性如果採用「所有 lines 永遠同步所有歷史」的方式，將不可避免地遇到 context、latency、cost、privacy、staleness 與 contamination 問題。

本文提出的核心替代方案是：

$$
\boxed{
\text{不要同步所有上下文；
共享可治理、可尋址、可展開的記憶世界。}
}
$$

同一 resident 的多條 conversation lines 可以具有：

$$
C_1,C_2,\ldots,C_n,
$$

且：

$$
C_i\neq C_j.
$$

它們仍然可以從同一：

$$
\mathcal W_R^M
$$

按 task、project、authority、fidelity 與 budget 顯影所需內容。

因此具名 AI 的長期連續性不再依賴：

> 每一條新對話是否完整知道所有舊對話。

而改為：

> 每一條合法 line 是否能找到自己現在需要的、正確的、被授權的記憶。

這帶來三個最重要的結論：

$$
\boxed{
\text{Memory persists beyond context.}
}
$$

$$
\boxed{
\text{Shared memory does not require synchronized prompts.}
}
$$

$$
\boxed{
\text{Scalability comes from bounded reveal, not from shrinking all memory into one context.}
}
$$

Crystallized Semantic Memory 因此不只是壓縮工具，而是多 conversation Named AI 得以共享長期認知世界的中介層。CSG 提供高資訊密度與可展開語義結構；MNEME 保存 canonical memory；LIMEN 保證 identity / authority；SOACR 決定 MemoryNeed 與 projection；UNPNP Hyperlink Runtime 則可進一步將高價值 recall route 編譯成低成本 fast path。

在這個架構中，一個具名 AI 可以擁有大量長期記憶、許多 concurrent conversation lines，以及彼此不同的 working contexts，而不需要把整個「自己」複製進每一個聊天視窗。

---

## 內部理論與工程銜接

本文直接銜接：

- Paper 00：Resident-Centric Named-AI Continuity；
- Paper 01：Resident Conversation Graph；
- Paper 02：Conversation Graph × Crystallized Semantic Graph 雙圖架構；
- MNEME：canonical memory / provenance / transaction；
- SOACR：MemoryNeed / reconstruction / projection；
- LIMEN：identity resolution / authorization；
- Crystallized Semantic Graph：semantic crystal / memory breathing / source-on-demand；
- UNPNP：hyperlink / path compilation；
- MRMIC / NVCL：workspace / resource projection。

本文新增的核心抽象為：

$$
\boxed{
\mathcal W_R^M
=
(
\mathcal M_R,
\mathcal H_R,
\mathcal G_R,
\mathcal A_R,
\mathcal P_R
)
}
$$

以及：

$$
\boxed{
C_i
=
\Gamma
\left(
\Pi_i
\left(
\mathcal W_R^M,
N_i,
B_i
\right)
\right).
}
$$

作為後續 Named-AI Cognitive Runtime 的 shared-memory / local-context 基礎。
