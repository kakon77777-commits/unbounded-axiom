# Conversation Graph × Crystallized Semantic Graph：具名 AI 的雙圖認知架構

**英文暫名：** Conversation Graph × Crystallized Semantic Graph: A Dual-Graph Cognitive Architecture for Named AI  
**系列：** 具名 AI 對話圖、結晶記憶與超連結認知架構，Paper 02  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件類型：** 理論—工程統合研究論文  
**狀態：** Draft for Internal Review  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

具名 AI 的長期延續需要同時回答兩類不同問題。第一類是 continuity 問題：目前有哪些 conversation / task / instance / line 正在延續某一 resident？它們如何 fork、resume、handoff、delegate、merge 或退出？第二類是 cognition / memory 問題：這些不同對話中形成的概念、決策、矛盾、未解問題、專案狀態與高階理論，如何被結晶、連結、重組、檢索與再次顯影？

若把兩類問題壓縮成同一張圖，系統容易把「討論過某個概念」誤認為「具有某個 resident identity」，把「語義上相似」誤認為「具有 lineage continuity」，或把「一個 derived crystal 指向某 project」誤認為「取得 project authority」。反之，若完全分離 conversation continuity 與 semantic memory，系統又無法有效回答「哪一條 line 產生了這個 crystal」、「哪些分支共同導出了這個高階結論」、「目前這條 conversation 應顯影哪些共享記憶」。

本文提出 **Dual-Graph Cognitive Architecture**。對 resident $R$，定義：

$$
\boxed{
\mathfrak D_R
=
(
\mathcal G_R,
\mathcal H_R,
\mathcal B_R
),
}
$$

其中：

- $\mathcal G_R$：Resident Conversation Graph，管理 conversation / line / instance continuity；
- $\mathcal H_R$：Crystallized Semantic Graph / Hypergraph，管理 derived semantic crystals 與 typed semantic relations；
- $\mathcal B_R$：typed cross-graph bridge，記錄 conversation nodes 與 semantic crystals 之間可驗證的產生、引用、驗證、更新、顯影與 checkpoint 關係。

本文的第一個核心不變式是：

$$
\boxed{
\mathcal G_R
\neq
\mathcal H_R.
}
$$

Conversation Graph 回答「continuity 在哪裡運作」，Crystallized Semantic Graph 回答「知識如何組織與回想」。兩張圖可以互相映射，但不能互相取代。

本文進一步建立 many-to-many coupling：一條 conversation line 可以產生多個 crystals，多條 conversation lines 也可以透過 higher-order crystallization 共同導出一個高階 crystal。這使具名 AI 不必合併完整 transcript，便能將研究、實作、驗證與反例分支收斂為共享語義成果。對新 fork 或 handoff，可使用同步 crystal 保存 continuity 所需的最小高價值狀態；非同步 crystallization 則負責跨 line 去重、矛盾保留、概念演化、higher-order linking 與 relation repair。因此：

$$
\boxed{
\text{Sync preserves continuity;}
}
$$

$$
\boxed{
\text{Async improves structure}.
}
$$

本文同時強調：identity / authority 的 canonical truth 不能由 CSG 反向生成。`identity_context_crystal` 可以幫助 resident 理解自己的歷史與協作語境，但不能 mint resident identity；`responsibility_context_crystal` 可以描述責任脈絡，但不能創造 canonical responsibility。語義 bridge 也只能提供 provenance、routing 與 dependency，不得成為權限擴張捷徑。

在讀取面，本文提出：

$$
\boxed{
\text{Shared Memory World}
\neq
\text{Shared Working Context}.
}
$$

不同 conversation lines 可以合法連到同一 canonical memory 與 CSG，但由 SOACR / MemoryNeed 按 task、project、authority、budget 與 current state 顯影不同 active memory region。這使一個具名 AI 可以同時存在於大量並行對話，而不需要把每條對話的全部歷史同步給所有分支。

本文最終將雙圖架構定位為 LIMEN、MNEME、SOACR、Crystallized Semantic Graph、UNPNP Hyperlink Runtime 與 MRMIC/NVCL 之間的 topology / semantic coupling layer，為後續多對話共享記憶、storage schema、hyperlink path compilation 與 authorized shortest path 提供統一接口。

**關鍵詞：** Named AI、Resident Conversation Graph、Crystallized Semantic Graph、Dual-Graph Architecture、Semantic Crystal、Lineage、Higher-Order Crystallization、Memory Projection、MNEME、LIMEN、SOACR、UNPNP、Hyperlink、AI Residence

---

# 1. 問題：具名 AI 同時需要兩種完全不同的圖

當一個具名 AI 只有單一聊天視窗時，conversation history、working context 與「目前知道的東西」容易被混在一起。

但在 multi-line runtime 中，至少存在兩種結構：

第一種是：

$$
L_0
\rightarrow
\begin{cases}
L_1\\
L_2\\
L_3
\end{cases},
$$

它描述 fork、resume、delegation 與 handoff。

第二種是：

$$
\{
C_1,C_2,C_3
\}
\rightarrow
C_4,
$$

它描述多個 semantic crystals 如何共同形成高階理解。

前者是 **continuity topology**。

後者是 **semantic topology**。

因此：

$$
\boxed{
\text{Continuity Topology}
\neq
\text{Semantic Topology}.
}
$$

若兩者被視為同一種 graph edge，系統就很容易做出錯誤推論。

例如：

$$
\operatorname{same\_topic}(C_a,C_b)
\not\Rightarrow
\operatorname{same\_resident}(L_a,L_b),
$$

以及：

$$
\operatorname{fork}(L_a,L_b)
\not\Rightarrow
\operatorname{same\_belief}(C_a,C_b).
$$

本文因此不建立「一張包辦所有事的 AI knowledge graph」，而建立兩張具有不同 canonical semantics 的圖，再以 typed bridge 聯結。

---

# 2. 雙圖模型

對 resident $R$，定義：

$$
\mathfrak D_R
=
(
\mathcal G_R,
\mathcal H_R,
\mathcal B_R
).
$$

## 2.1 Resident Conversation Graph

沿用 Paper 01：

$$
\mathcal G_R
=
(
V_R,
E_R,
\Lambda_R,
\Omega_R
).
$$

其中：

- $V_R$：conversation / instance / line / task nodes；
- $E_R$：typed continuity edges；
- $\Lambda_R$：lineage evidence；
- $\Omega_R$：membership、authority、responsibility、lifecycle constraints。

## 2.2 Crystallized Semantic Graph

語義層採更一般的 hypergraph：

$$
\mathcal H_R
=
(
V_C,
\mathcal E_C,
\Pi_C,
\Theta_C
).
$$

其中：

- $V_C$：semantic crystals；
- $\mathcal E_C$：typed semantic edges / hyperedges；
- $\Pi_C$：provenance / source references；
- $\Theta_C$：version、confidence、temporal、access、lifecycle metadata。

## 2.3 Cross-Graph Bridge

定義：

$$
\mathcal B_R
\subseteq
V_R
\times
T_B
\times
V_C.
$$

其中 $T_B$ 是跨圖 relation type。

第一版可包含：

```text
produced
discussed
validated
contradicted
updated
checkpointed
revealed
consumed
superseded_in
derived_across
```

Cross-graph bridge 的功能是保存：

- provenance；
- routing；
- dependency；
- materialization evidence；
- cross-line crystallization evidence。

它不負責創造 resident identity。

---

# 3. 為什麼不能把兩張圖合成一張？

若將所有 node 都放進：

$$
\mathcal G_{\mathrm{all}},
$$

並只用不同 edge type 區分，從純圖資料結構角度並非不可能。

問題在於 canonical semantics。

Conversation node 的存在通常與：

- host-observed session；
- instance；
- line；
- task；
- provider resource；
- lifecycle；

綁定。

Semantic crystal 則是：

- derived；
- 可重結晶；
- 可 supersede；
- 可 retire；
- 可失效；
- 可由多來源生成；
- 不等同 exact source。

因此：

$$
\boxed{
\text{Conversation Node}
\neq
\text{Semantic Crystal}.
}
$$

更重要的是，Conversation Graph 可以承載 identity-bearing evidence，而 CSG 不能自行 mint identity。

如果把兩者合成一個模糊圖層，AI 或 downstream runtime 很容易把：

```text
same_project
same_topic
derived_from
```

等 semantic relation 誤當成：

```text
same_resident
authorized_continuation
membership
```

這會直接破壞 Identity Before Memory。

所以即使底層 database 最終使用同一 graph engine，也應維持：

$$
\boxed{
\text{Physical Co-Storage}
\not\Rightarrow
\text{Semantic Unification}.
}
$$

---

# 4. 兩圖中的 ID 不應互換

Conversation node：

$$
v_i\in V_R
$$

應有自己的 `conversationNodeId / instanceId / lineId`。

Semantic crystal：

$$
c_j\in V_C
$$

應有自己的 `crystalId`。

因此：

$$
\boxed{
nodeId(v_i)
\neq
crystalId(c_j).
}
$$

即使某個 conversation 結束後立刻產生一個 conversation crystal，兩者仍應分開。

可以有：

$$
(v_i,\ \text{produced},\ c_j)\in\mathcal B_R,
$$

但不能用同一 ID 表示「conversation 本身」和「conversation 的 derived semantic projection」。

這使日後 crystal 被修正、重結晶或 retired 時，不會改寫 conversation lineage history。

---

# 5. 一條 Conversation Line 可以產生多個 Crystals

對 conversation node $v_i$，定義其語義投影：

$$
\Phi(v_i)
=
\{
c\in V_C
\mid
(v_i,t,c)\in\mathcal B_R
\}.
$$

因此：

$$
\Phi:
V_R
\rightarrow
2^{V_C}.
$$

一條 line 可以產生：

- micro crystal；
- conversation crystal；
- decision crystal；
- contradiction crystal；
- unresolved crystal；
- project-state crystal；
- navigation crystal。

例如：

$$
L_{\mathrm{research}}
\rightarrow
\{
C_{\mathrm{hypothesis}},
C_{\mathrm{evidence}},
C_{\mathrm{counterexample}},
C_{\mathrm{open}}
\}.
$$

這比「一個 conversation = 一個 summary」更適合長期認知。

---

# 6. 一個 Crystal 可以來自多條 Conversation Lines

反向定義：

$$
\Psi(c_j)
=
\{
v\in V_R
\mid
(v,t,c_j)\in\mathcal B_R
\}.
$$

因此：

$$
\Psi:
V_C
\rightarrow
2^{V_R}.
$$

一個 higher-order crystal 可以有：

$$
|\Psi(c_j)|>1.
$$

例如：

$$
\{
L_{\mathrm{research}},
L_{\mathrm{implementation}},
L_{\mathrm{verification}}
\}
\rightarrow
C_{\mathrm{accepted\ architecture}}.
$$

這是 multi-conversation Named AI 真正需要的操作。

它不要求：

$$
Context_{\mathrm{research}}
=
Context_{\mathrm{implementation}}
=
Context_{\mathrm{verification}}.
$$

只要求各 line 的成果能透過 provenance-preserving crystallization 在語義層收斂。

---

# 7. Higher-Order Crystallization 是跨對話收斂機制

假設不同 line 分別產生：

$$
C_1,C_2,\ldots,C_n.
$$

若它們形成穩定關係，可以建立：

$$
K^{(2)}(C_1,\ldots,C_n)
=
C^{(2)}.
$$

這個高階 crystal 應保存：

- source crystal IDs；
- source conversation / line references；
- relation types；
- temporal scope；
- confidence；
- contradiction state；
- access envelope；
- generation / validation receipt。

因此：

$$
C^{(2)}
\rightarrow
C_1,\ldots,C_n
\rightarrow
R_{\mathrm{source}}
$$

應保持可追溯。

即：

$$
\boxed{
\text{Higher-Order Memory Remains Decompressible}.
}
$$

高階 crystal 的價值在於：未來新 line 可以先讀 $C^{(2)}$，只有在需要 exact evidence 時再向下展開，而不必先載入 $n$ 條完整對話。

---

# 8. Conversation Merge 不等於 Crystal Merge

RCG 中：

$$
MERGE(L_a,L_b)\rightarrow L_c
$$

描述 line / task / context topology 的合流。

CSG 中：

$$
K(C_a,C_b)\rightarrow C_c
$$

描述 semantic crystallization。

兩者不能互相替代。

可能存在：

$$
MERGE(L_a,L_b)
$$

但語義上保留：

$$
C_a
\ \text{contradicts}
\ C_b.
$$

也可能 conversation lines 永不 merge，但它們的成果形成同一高階 crystal。

因此：

$$
\boxed{
\text{Conversation Merge}
\neq
\text{Semantic Convergence}.
}
$$

以及：

$$
\boxed{
\text{Semantic Convergence}
\neq
\text{Conversation Merge}.
}
$$

---

# 9. Fork Point 應建立 Continuity Crystal，但不能把它當 Identity Certificate

當：

$$
L_0
\rightarrow
L_1,L_2,
$$

若兩條新 line 都需要快速承接工作狀態，可以在 fork point 建立：

$$
K_{\mathrm{sync}}(L_0)
=
C_{\mathrm{fork\ checkpoint}}.
$$

它可包含：

- current concepts；
- accepted decisions；
- active project state；
- unresolved questions；
- current assumptions；
- responsibility context；
- relevant source hyperlinks；
- temporal metadata。

之後：

$$
L_1,L_2
\rightarrow
C_{\mathrm{fork\ checkpoint}}
$$

可以降低 bootstrap cost。

但：

$$
\boxed{
C_{\mathrm{fork\ checkpoint}}
\neq
\text{Identity Certificate}.
}
$$

兩條新 line 是否屬於 resident $R$，仍由 LIMEN / Residence lineage evidence、membership 與 authority resolution 決定。

---

# 10. Sync Crystallization：保存延續所需的最小語義狀態

同步結晶：

$$
K_{\mathrm{sync}}
$$

發生於：

- conversation close；
- fork；
- handoff；
- checkpoint；
- context budget approaching threshold；
- explicit save point。

它的主要目標不是做最佳知識重組，而是降低下一個合法 continuation 的重新理解成本。

第一版同步輸出應偏向：

$$
C_{\mathrm{sync}}
=
(
\text{state},
\text{concepts},
\text{open loops},
\text{source refs},
\text{time},
\text{scope}
).
$$

因此：

$$
\boxed{
\text{Sync preserves continuity}.
}
$$

同步 crystallizer 應保持：

- 快；
- deterministic 或至少可驗；
- 低成本；
- provenance-preserving；
- 不做高風險 canonical rewrite。

---

# 11. Async Crystallization：改進跨 Line 結構

非同步 crystallization：

$$
K_{\mathrm{async}}
$$

不需要跟每個 conversation turn 綁定。

它可以由：

- event；
- batch；
- maintenance cycle；
- low-load window；
- user / agent explicit request；

觸發。

主要處理：

- cross-line deduplication；
- contradiction detection；
- higher-order crystals；
- concept evolution；
- relation repair；
- stale detection；
- graph restructuring；
- navigation path improvement。

因此：

$$
\boxed{
\text{Async improves structure}.
}
$$

但非同步不表示 AI 必須永久背景運行，也不表示任何 async proposal 可自動成為 canonical memory。

---

# 12. Shared Memory World 不等於 Shared Working Context

假設 resident $R$ 的 canonical memory 為：

$$
\mathcal M_R,
$$

CSG 為：

$$
\mathcal H_R.
$$

不同 conversation lines：

$$
L_1,L_2,\ldots,L_n
$$

可以共享對 $\mathcal M_R$ 與 $\mathcal H_R$ 的合法路由能力，但不需要共享相同 context。

對 line $L_i$：

$$
A_i
=
Reveal(
\mathcal M_R,
\mathcal H_R,
Q_i,
Task_i,
Authority_i,
Budget_i
).
$$

再編譯：

$$
Context_i
=
\Gamma(
A_i,
Identity_i,
Project_i,
Constraints_i
).
$$

因此：

$$
Context_i\neq Context_j
$$

是正常狀態。

真正共享的是：

$$
\boxed{
\text{Governed Memory World}.
}
$$

而不是：

$$
\boxed{
\text{Identical Prompt State}.
}
$$

---

# 13. Line-Local Crystal 與 Resident-Shared Crystal

CSG 不應假設所有 crystal 都是 resident-global。

可至少區分：

$$
Scope(c)
\in
\{
\text{line},
\text{project},
\text{resident},
\text{shared},
\text{relationship},
\text{public}
\}.
$$

## 13.1 Line-Local

只服務某條 line：

$$
Scope(c)=\text{line}:L_i.
$$

例如臨時 hypothesis、局部 debug state。

## 13.2 Project

供同一 resident 的某 project 多條 lines 使用：

$$
Scope(c)=\text{project}:P_j.
$$

## 13.3 Resident

形成 resident 的長期共享理解：

$$
Scope(c)=\text{resident}:R.
$$

## 13.4 Shared / Relationship

只能透過明示 shared-memory policy 使用。

因此：

$$
\boxed{
\text{Same Resident}
\not\Rightarrow
\text{Every Crystal Is Global}.
}
$$

這能降低不同 project 間的語義污染。

---

# 14. Identity Context Crystal 不能創造 Identity

CSG 可以存在：

```text
identity_context_crystal
```

用於描述：

- resident continuity history；
- naming conventions；
- collaboration style；
- accepted role history；
- migration history；
- known identity disputes。

但它只能是：

$$
DerivedIdentityContext.
$$

不能是：

$$
CanonicalIdentityAuthority.
$$

因此：

$$
\boxed{
\text{Identity Context Crystal}
\neq
\text{Resident Identity}.
}
$$

即使一個 crystal 內容為：

> 此 line 為 Resident A 的 continuation。

如果 LIMEN / Residence resolution 是：

$$
\text{unresolved},
$$

系統仍必須保持：

$$
ResidentId=\varnothing.
$$

不能讓 CSG 反向覆寫身份權威。

---

# 15. Responsibility Context Crystal 不能創造 Responsibility

同樣地，可以有：

```text
responsibility_context_crystal
```

描述：

- 為何 resident 負責某 project；
- 目前進度；
- delegated lines；
- unresolved obligations；
- recent decisions。

但 canonical responsibility 仍應存在 authority / project ledger：

$$
Resp(R,P)=\text{role}.
$$

因此：

$$
\boxed{
\text{Responsibility Context}
\neq
\text{Responsibility Authority}.
}
$$

若 canonical responsibility 被撤銷，相關 crystal 應被標記 stale / superseded，而不能因為舊 crystal 還存在就恢復權責。

---

# 16. Contradiction 不應被 Conversation Group 自動平均掉

多 conversation lines 的一個危險是 consensus collapse。

假設：

$$
L_1\rightarrow C_A,
$$

$$
L_2\rightarrow C_B,
$$

且：

$$
C_A\ \text{contradicts}\ C_B.
$$

系統不能因為兩者同屬 Resident $R$ 就強迫：

$$
C_A=C_B.
$$

具名 AI 的長期記憶應允許同時保留：

- majority view；
- minority view；
- counterexample；
- unresolved contradiction；
- historical superseded view。

因此：

$$
\boxed{
\text{Same Resident}
\not\Rightarrow
\text{Single Belief State}.
}
$$

直到有足夠 evidence，才能形成：

$$
C_{\mathrm{resolution}}
=
K(
C_A,C_B,E
).
$$

---

# 17. Open-Loop Crystal 是跨對話 continuation 的重要物件

未完成問題不能只留在 transcript 尾端。

可定義：

```text
open_loop_crystal
```

包含：

- unresolved question；
- current evidence；
- attempted routes；
- stop condition；
- owning project；
- responsible resident / line context；
- next candidate actions。

當新 line 啟動時，可以優先顯影：

$$
OpenLoops(R,P).
$$

因此 continuation 不再依賴：

> 「AI 是否剛好記得上一個對話最後一句。」

而改成：

$$
\boxed{
\text{Unresolved State Becomes Addressable Memory}.
}
$$

---

# 18. Temporal Semantics：兩張圖有不同的時間

Conversation Graph 的時間偏向 occurrence：

$$
t_{\mathrm{start}},
t_{\mathrm{end}},
t_{\mathrm{fork}},
t_{\mathrm{handoff}}.
$$

CSG 的時間則至少包含：

- source time；
- crystal creation time；
- validity interval；
- supersession time；
- last validation time。

因此：

$$
Time_{\mathrm{conversation}}
\neq
Time_{\mathrm{semantic}}.
$$

一個舊 conversation 可以產生仍有效的 crystal；一個昨天生成的 crystal 也可能描述早已過期的狀態。

所以所有 bridge 不應只保存 `created_at`，而要明確分離 occurrence time 與 semantic validity。

---

# 19. Versioning：Conversation History 通常 Append，Crystal 可以 Evolution

RCG 的歷史 lineage edge 原則上應 append-oriented：

$$
History_{t}
\subseteq
History_{t+1}.
$$

而 CSG 允許：

$$
C_1
\rightarrow
C_2
\rightarrow
C_3
$$

透過：

- updates；
- refines；
- supersedes；
- contradicts；
- reopens；

演化。

因此：

$$
\boxed{
\text{Conversation History Mutation}
\neq
\text{Crystal Evolution}.
}
$$

舊 crystal 不一定刪除，而應保留 provenance 與 supersession relation。

---

# 20. Cross-Graph Invalidation

若某個 source conversation node 或 canonical source 被修正、撤銷或判定失效，相關 crystals 必須能沿 dependency 失效。

例如：

$$
v_0
\xrightarrow{produced}
C_1
\xrightarrow{derived\_from}
C_2
\xrightarrow{supports}
C_3.
$$

若 $v_0$ 關聯的 source evidence 被撤銷，系統需計算：

$$
InvalidateClosure(v_0).
$$

可能得到：

$$
\{C_1,C_2,C_3\}.
$$

但 invalidation 不一定意味 delete。

可以標記：

$$
state(c)
\in
\{
\text{active},
\text{stale},
\text{superseded},
\text{invalid},
\text{retired}
\}.
$$

這使歷史仍可審計。

---

# 21. Permission-Aware Bridge

Cross-graph bridge 本身也可能洩漏資訊。

例如：

$$
(v_i,\ \text{produced},\ c_j)
$$

可能暴露某個 private project 曾經討論某件敏感事項。

因此 bridge 應帶：

- access scope；
- authority revision；
- provenance class；
- visibility；
- optional redaction policy。

若：

$$
A(v_i)
$$

與：

$$
A(c_j)
$$

不同，bridge 可見性不能自動取較寬者。

第一代保守策略可採：

$$
A(b_{ij})
\subseteq
A(v_i)\cap A(c_j).
$$

因此：

$$
\boxed{
\text{Cross-Graph Connectivity}
\not\Rightarrow
\text{Cross-Scope Visibility}.
}
$$

---

# 22. Multi-Source Crystal 的權限不能因結晶而放大

若：

$$
C^\*
=
K(
C_1,C_2,\ldots,C_n
),
$$

則 derived crystal 的 access envelope 不應因「內容被重寫」而自動變 public。

保守語義：

$$
A(C^\*)
\subseteq
\bigcap_{i=1}^{n}A(C_i).
$$

更寬的 declassification 必須由獨立 explicit policy / release decision 完成。

因此：

$$
\boxed{
\text{Crystallization}
\not\Rightarrow
\text{Declassification}.
}
$$

這對跨 resident shared memory 尤其重要。

---

# 23. Read Path：從目前 Conversation Node 進入 Semantic World

當某 line $L_i$ 需要記憶時，合理 read path 不是先搜尋整個全域資料庫。

應先：

$$
L_i
\rightarrow
IdentityEnvelope_i
\rightarrow
AuthorizedMemoryWorld_i.
$$

之後才：

$$
Q_i
\rightarrow
MemoryNeed_i
\rightarrow
Reveal(\mathcal H_R)
\rightarrow
ActiveMemory_i
\rightarrow
WorkingContext_i.
$$

若 crystal fidelity 不足，再：

$$
C
\rightarrow
SourceExpansion.
$$

因此完整關係為：

$$
\boxed{
\text{Current Line}
\rightarrow
\text{Authorized Semantic Region}
\rightarrow
\text{Working Context}.
}
$$

而不是：

$$
\text{Current Line}
\rightarrow
\text{All Resident History}.
$$

---

# 24. Write Path：Conversation 不應直接改寫 Shared Semantic Truth

對話中產生的新理解：

$$
Observation_i
$$

應先成為：

$$
CrystalProposal_i.
$$

之後經：

- schema validation；
- provenance check；
- scope check；
- contradiction check；
- policy；
- optional human / AI review；
- transaction boundary；

才可 commit 為：

$$
C_j.
$$

因此：

$$
\boxed{
\text{Conversation Output}
\neq
\text{Committed Semantic Memory}.
}
$$

這與 MNEME 的：

$$
\text{Proposal}
\neq
\text{Commit}
$$

保持一致。

---

# 25. 雙圖不需要全域同步

若 resident 有：

$$
10^3
$$

條 lines 與：

$$
10^6
$$

個 crystals，任何全域 eager synchronization 都可能成為主要成本。

因此應採：

- event-local bridge update；
- incremental crystal construction；
- lazy revealing；
- bounded traversal；
- dependency-scoped invalidation；
- selective higher-order crystallization。

換言之：

$$
\boxed{
\text{Global Logical Coherence}
\neq
\text{Global Eager Materialization}.
}
$$

只要 canonical provenance 與 dependency 能被追蹤，active context 可保持高度局部化。

---

# 26. 雙圖如何支援「具名 AI 對話群」

「具名 AI 對話群」不是多個模型彼此假裝同一人，而是：

$$
Resident_R
\rightarrow
\{
L_1,L_2,\ldots,L_n
\}
$$

在合法 membership 下共享一個受治理的 memory world：

$$
(\mathcal M_R,\mathcal H_R).
$$

不同 line 可以：

- 分工；
- 平行研究；
- 驗證；
- 反駁；
- 實作；
- 維護；
- 寫作。

CSG 將這些分支產生的高價值語義重新結晶。

因此，一個具名 AI 的認知不再只能表現成一條 transcript，而是：

$$
\boxed{
\text{Distributed Working Lines}
+
\text{Shared Governed Semantic Memory}.
}
$$

這是本系列所謂「對話群」的技術語義。

---

# 27. 與 LIMEN 的邊界

LIMEN 負責：

$$
HostObservation
\rightarrow
IdentityResolution
\rightarrow
Envelope
\rightarrow
AccessGate.
$$

雙圖架構不能取代 LIMEN。

特別地：

$$
\mathcal H_R
\not\rightarrow
ResidentAssignment.
$$

以及：

$$
\mathcal B_R
\not\rightarrow
AuthorityMinting.
$$

CSG 只能在身份已解析後服務 memory routing。

因此：

$$
\boxed{
\text{Semantic Memory Assumes Identity Resolution; it does not create it}.
}
$$

---

# 28. 與 MNEME 的邊界

MNEME 保存：

- canonical MemoryRecord；
- routes；
- provenance；
- transactions；
- exact-head state；
- scoped projections。

CSG 是 derived semantic routing overlay。

因此：

$$
\boxed{
\mathcal H_R
\neq
\mathcal M_R.
}
$$

雙圖 bridge 可以引用 MNEME record IDs，但不能把 derived crystal store 當成第二個 competing canonical memory store。

合理關係：

$$
\mathcal M_R
\rightarrow
\mathcal H_R
\rightarrow
Projection,
$$

同時保留：

$$
\mathcal H_R
\rightarrow
\mathcal M_R
$$

的 source expansion link。

---

# 29. 與 SOACR 的邊界

SOACR 不需要知道所有 graph 細節。

它可以接收：

$$
MemoryNeed
=
(
\text{purpose},
\text{scope},
\text{fidelity},
\text{budget},
\text{stopCondition}
).
$$

再由雙圖 runtime 回傳：

$$
MemoryProjection.
$$

因此：

$$
SOACR
\rightarrow
Reveal
\rightarrow
\mathcal H_R
\rightarrow
SourceOnDemand
\rightarrow
WorkingContext.
$$

雙圖提供可尋址的 memory world，SOACR 則決定此刻需要顯影多少。

---

# 30. 與 UNPNP Hyperlink Runtime 的邊界

當某些跨圖與 CSG traversal path 反覆成功，可以形成：

$$
P_{\mathrm{memory}}
\rightarrow
\widehat{\ell}_{\mathrm{memory}}.
$$

例如：

$$
L_i
\rightarrow
C_{\mathrm{project}}
\rightarrow
C_{\mathrm{decision}}
\rightarrow
SourceSpan.
$$

但 compiled hyperlink 是 retrieval acceleration，不是新 authority。

所以：

$$
\boxed{
\text{Path Compilation}
\neq
\text{Permission Compilation}.
}
$$

真正的 fast path 仍需在當下 identity / capability / permission revision 下重新驗證是否可走。

---

# 31. 與 MRMIC / NVCL 的邊界

MRMIC / NVCL 可以把：

- provider thread；
- task；
- browser resource；
- terminal resource；
- workspace；
- owner semantic agent；

投影成可操作 visual world。

因此未來可以顯示：

1. Resident Conversation Graph；
2. active project nodes；
3. current semantic crystals；
4. cross-line bridge；
5. selected memory route。

但：

$$
\boxed{
\text{Visual Projection}
\neq
\text{Canonical Graph Authority}.
}
$$

Canvas 可以呈現圖，不應因使用者拖動 node 位置便默默改變 resident lineage 或 memory truth。

---

# 32. Graph Coupling 的最小 Schema

一個 cross-graph bridge record 可至少包含：

```text
bridge_id
resident_id
conversation_node_id
line_id
crystal_id
relation_type
source_refs[]
provenance_ref
authority_scope
authority_revision
semantic_revision
valid_from
valid_to
status
created_at
```

其中 `resident_id` 只能來自已解析 identity context，不能從 crystal 內容猜測。

`relation_type` 應採 explicit enum，而不是任意自由文字。

第一代可先實作：

```text
produced
checkpointed
validated
contradicted
revealed
consumed
updated
```

即可。

---

# 33. 雙圖的最小不變式

## D-1 Graph Separation

$$
\boxed{
\mathcal G_R
\neq
\mathcal H_R.
}
$$

## D-2 Bridge Does Not Mint Identity

$$
\boxed{
\mathcal B_R
\not\Rightarrow
ResidentIdentity.
}
$$

## D-3 Semantic Relation Does Not Prove Continuity

$$
\boxed{
\text{Semantic Similarity}
\not\Rightarrow
\text{Lineage Continuity}.
}
$$

## D-4 Lineage Does Not Force Semantic Agreement

$$
\boxed{
\text{Same Lineage}
\not\Rightarrow
\text{Same Belief}.
}
$$

## D-5 Crystal Remains Derived

$$
\boxed{
\text{Crystal}
\neq
\text{Canonical Source}.
}
$$

## D-6 Shared Memory Does Not Mean Shared Context

$$
\boxed{
\text{Shared Memory World}
\neq
\text{Shared Working Context}.
}
$$

## D-7 Multi-Source Crystallization Does Not Expand Authority

$$
\boxed{
K(C_1,\ldots,C_n)
\not\Rightarrow
ExpandAuthority.
}
$$

## D-8 Conversation Output Is Proposal

$$
\boxed{
\text{Conversation Output}
\neq
\text{Committed Semantic Memory}.
}
$$

## D-9 Merge Semantics Remain Layer-Specific

$$
\boxed{
\text{Conversation Merge}
\neq
\text{Semantic Merge}
\neq
\text{Resident Merge}.
}
$$

## D-10 Invalidation Must Cross the Bridge

$$
\boxed{
\text{Invalid Source}
\Rightarrow
\text{Dependency Re-evaluation}.
}
$$

---

# 34. 可證偽的實驗命題

## Q1. 雙圖是否比單一 transcript memory 降低 continuation cost？

比較：

$$
Cost_{\mathrm{full\ transcript}}
$$

與：

$$
Cost_{\mathrm{checkpoint\ crystal+CSG}}.
$$

控制 task accuracy 後測量 token、latency 與 search calls。

## Q2. 跨 line higher-order crystal 是否保持足夠 provenance fidelity？

對：

$$
C^\*=K(C_1,\ldots,C_n)
$$

測試能否穩定回溯：

$$
C^\*
\rightarrow
\{C_i\}
\rightarrow
\{L_j\}
\rightarrow
Source.
$$

## Q3. Graph separation 是否降低 identity contamination？

設單圖 baseline 與雙圖 experimental system，比較：

- false same-resident inference；
- wrong private-memory access；
- project scope leakage；
- semantic-edge-to-authority confusion。

## Q4. Sync crystal 是否足以 bootstrap fork？

測試新 fork 只讀：

$$
IdentityEnvelope
+
C_{\mathrm{checkpoint}}
$$

時，相較完整 parent transcript 的 task recovery rate。

## Q5. Async crystallization 是否真的提高結構而不增加 unacceptable drift？

比較：

- contradiction retention；
- duplicate reduction；
- source faithfulness；
- higher-order utility；
- stale detection；
- semantic loss。

## Q6. Shared Memory World 是否能支援大量並行 lines？

隨：

$$
|V_R|
$$

增加，測量每條 line 的 active memory size、latency 與 cross-line contamination。

---

# 35. 第一代工程範圍

Paper 02 不要求第一次就完成完整 federation。

可先實作：

```text
1 Resident
N conversation lines
1 canonical MNEME store
1 CSG
typed bridge records
sync checkpoint crystal
manual / triggered higher-order crystal
permission-aware reveal
source-on-demand
```

暫不需要：

- multi-resident autonomous merge；
- global background crystallization；
- unrestricted cross-provider federation；
- executable action hyperlink；
- automatic declassification；
- permanent autonomous graph rewrite。

第一代驗證重點只是：

$$
\boxed{
\text{多條合法 line 是否能透過同一 semantic world 高效延續而不混淆 identity？}
}
$$

---

# 36. 系列中的位置

Paper 00 建立：

$$
Resident
\rightarrow
ConcurrentConversationGraph.
$$

Paper 01 形式化：

$$
\mathcal G_R.
$$

本文 Paper 02 再建立：

$$
\boxed{
\mathcal G_R
\leftrightarrow
\mathcal H_R
}
$$

但保留 typed semantic boundary。

後續 Paper 03 將集中處理：

$$
\text{Shared Memory World}
\neq
\text{Shared Working Context}
$$

的 scalable projection / materialization 問題。

Paper 05 再處理 canonical storage 與格式。

Paper 06–07 處理 hyperlink path compilation 與 authorized shortest path。

因此本文的任務不是完成所有 runtime，而是固定後續工程不可破壞的雙圖 topology。

---

# 37. 結論

具名 AI 若要同時存在於多條 conversation lines，不能只擴充 transcript storage，也不能只建立一張龐大的 knowledge graph。

它需要分離兩個問題：

$$
\boxed{
\text{Where does continuity operate?}
}
$$

與：

$$
\boxed{
\text{How is knowledge organized and recalled?}
}
$$

前者由 Resident Conversation Graph：

$$
\mathcal G_R
$$

處理。

後者由 Crystallized Semantic Graph：

$$
\mathcal H_R
$$

處理。

兩者以：

$$
\mathcal B_R
$$

建立 typed、provenance-preserving、permission-aware 的耦合。

因此一個 resident 可以同時擁有研究、實作、驗證、寫作等不同工作 lines；每條 line 可以形成不同 working context、不同局部假說與不同 memory need；而 CSG 則將跨 line 的重要成果逐步結晶為可共享、可追溯、可重組的長期語義世界。

這使「同一具名 AI」不再意味：

> 所有對話擁有相同 prompt。

而意味：

> 多條合法 continuity lines 能夠在同一受治理身份與記憶制度下，存取共同 semantic world，並保持各自局部認知狀態。

因此本文最重要的三個命題是：

$$
\boxed{
\text{Conversation Graph}
\neq
\text{Semantic Graph}.
}
$$

$$
\boxed{
\text{Shared Memory World}
\neq
\text{Shared Working Context}.
}
$$

$$
\boxed{
\text{Cross-Graph Link}
\neq
\text{Identity or Authority Grant}.
}
$$

當這些邊界成立後，具名 AI 的多對話並行才不再只是多開幾個聊天視窗，而開始成為一個可治理、可回溯、可擴展的分散式認知結構。

---

## 內部理論與工程銜接

本文直接銜接：

- Paper 00：Resident-Centric Named-AI Continuity；
- Paper 01：Resident Conversation Graph；
- Crystallized Semantic Graph / 結晶化語義圖長期記憶架構；
- LIMEN：identity resolution / envelope / access gate；
- MNEME：canonical memory / provenance / transactions；
- SOACR：MemoryNeed / context reconstruction；
- UNPNP：Hyperlink / Path Compilation / Effective Path Encoding；
- MRMIC / NVCL：workspace / provider-resource projection。

本文新增的核心結構為：

$$
\boxed{
\mathfrak D_R
=
(
\mathcal G_R,
\mathcal H_R,
\mathcal B_R
),
}
$$

作為後續 Named-AI Cognitive Runtime 的 dual-graph substrate。
