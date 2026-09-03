# 互動時間拓撲：平行 Agent、偏序因果與不可約互動深度

## Interaction-Time Topology: Parallel Agents, Partial-Order Causality, and Irreducible Interaction Depth

**系列**：AI 互動時間與智能時間經濟學系列，第 4 篇／共 8 篇  
**文件編號**：EML-ITT-2026-04-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Multi-Agent Runtime／偏序因果／平行智能計算／互動時間論擴展  
**狀態**：Public Theory Draft  
**直接前置**：《單輪不是一步：AI Turn、內部迴圈、工具動作與執行軌跡》v0.1

---

## 摘要

前篇已建立「一個可見 AI Turn 不等於一個執行 Step」，並將 Agent 執行拆分為 Run、Attempt、Loop、Action、Observation、Validation、Recovery 與 Commit。然而，一旦多 Agent、平行工具呼叫、分支搜索、異步工作流與 speculative execution 進入同一回合，單純使用線性步數仍然不足：若兩個事件彼此沒有因果依賴，強迫將其排列為先後順序只是表示層的人工壓平，而不是系統本身的必要時間結構。

本文提出「互動時間拓撲」（Interaction-Time Topology, ITT-Topo），將 AI-native 執行表示為帶權有向偏序圖：

$$
G_I
=
(V_I,E_I,\prec,\omega,\lambda),
$$

其中 $V_I$ 為事件或狀態轉換節點， $E_I$ 為依賴邊， $\prec$ 為因果偏序， $\omega$ 為事件成本或工作權重， $\lambda$ 為事件型別、角色、權限、驗證、資源與世界作用等標籤。本文據此正式區分：

$$
W_I
=
\sum_{v\in V_I}\omega(v),
$$

即 Interaction Work，以及：

$$
D_I
=
\max_{\pi\in\mathcal P(G_I)}
\sum_{v\in\pi}\omega(v),
$$

即 Interaction Depth／Span，也就是從意圖到結果所必須跨越的最長不可約因果路徑。

因此：

$$
\boxed{
\text{Total Interaction Work}
\neq
\text{Irreducible Interaction Depth}.
}
$$

本文進一步定義理想平行度：

$$
\Pi_I
=
\frac{W_I}{D_I},
$$

以及有限 Agent／worker 條件下的執行下界：

$$
T_P
\ge
\max
\left(
\frac{W_I}{P},
D_I
\right),
$$

再加入通信、同步、驗證、切換、等待與協調成本，形成 Agent-native 有效延遲模型。本文同時區分 computation graph、communication graph、memory graph、authority graph 與 world-commit graph，避免把「誰和誰說話」誤認為「誰依賴誰」、「誰有權控制誰」或「誰能修改世界」。

本文與經典 Lamport causal order、Brent parallel scheduling、Cilk work–span model 對接；並與 2026 年最新 multi-Agent orchestration 研究形成直接對話。AdaptOrch 已使用 task DAG 在 parallel、sequential、hierarchical 與 hybrid topology 間路由；LAMaS 明確以 critical-path length 最小化 multi-Agent latency；MASFactory 將 multi-Agent workflow 建模為 directed computation graph；近期 inference-time parallelism 研究亦區分 task-level trajectory parallelism 與 intra-trajectory dependency-aware parallelism。本文不主張重新發明 DAG 或 work–span，而主張把它們提升為含有意圖、語義、驗證、通信、權限與世界提交邊界的智能互動時間模型。

**關鍵詞**：互動時間拓撲、Multi-Agent、Partial Order、Causal DAG、Work、Span、Critical Path、Parallelism、Communication Cost、Join、Barrier、Race、Agent Orchestration

---

# 0. 核心問題

前篇得到：

$$
1\text{ Turn}
\neq
1\text{ Step}.
$$

並允許：

$$
a_1
\parallel
a_2
\parallel
a_3.
$$

這立即產生新的問題：

> 如果同一回合中的多個 Agent、工具與分支可以同時執行，那麼「互動時間」究竟應該按總步數、最長依賴鏈、牆鐘時間、Agent 數量，還是其他結構計算？

本文答案是：

$$
\boxed{
\text{互動時間的完整對象首先是偏序因果圖，而不是單一標量。}
}
$$

標量時間應是此圖在特定任務、資源與觀測契約下的投影。

---

# 1. 線性序列不足

考慮完全串行工作：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
D.
$$

若每步成本皆為 $1$：

$$
W=4,
\qquad
D=4.
$$

再考慮四個工作平行後 Join：

$$
A_1
\parallel
A_2
\parallel
A_3
\parallel
A_4
\rightarrow
J.
$$

忽略 Join 成本時：

$$
W=4,
\qquad
D=1.
$$

兩者總工作相同，因果深度不同。

因此：

$$
\boxed{
W\neq D.
}
$$

---

# 2. 互動因果圖

定義一次任務或互動的圖：

$$
G_I
=
(V_I,E_I,\prec,\omega,\lambda).
$$

其中：

- $V_I$：事件、任務、Agent action、validator、checkpoint、join、commit 等節點；
- $E_I$：依賴、消息、資料、控制、驗證或 commit 邊；
- $\prec$：causal precedence；
- $\omega$：節點或邊的成本權重；
- $\lambda$：型別、Agent、工具、權限、風險與資源標籤。

若：

$$
u\prec v,
$$

表示 $u$ 的完成、輸出或證明是 $v$ 合法執行的必要前置之一。

---

# 3. 偏序而非全序

對：

$$
u,v\in V_I,
$$

若：

$$
u\nprec v
$$

且：

$$
v\nprec u,
$$

則目前模型不要求兩者存在必要因果先後，可記為：

$$
u\parallel v.
$$

這不要求兩者在物理時間上精確同時。

因此：

$$
\boxed{
\text{Concurrency}
\neq
\text{Exact Physical Simultaneity}.
}
$$

---

# 4. Lamport 接口

若 Agent $A_i$ 的事件 $e$ 產生訊息 $m$，而 Agent $A_j$ 的事件 $f$ 使用 $m$，則建立：

$$
e\prec f.
$$

因此 multi-Agent runtime 可以依靠 causal metadata 建立偏序，而不需要假設中央全知時鐘。

這使互動時間與分散式系統中的 happens-before discipline 直接接合。

---

# 5. Interaction Work

定義總工作量：

$$
W_I
=
\sum_{v\in V_I}\omega(v).
$$

若所有節點等權：

$$
W_I=|V_I|.
$$

但一般情況下， $\omega(v)$ 可以表示：

- machine time；
- token-equivalent cost；
- accelerator-seconds；
- tool cost；
- human review effort；
- risk-adjusted cost；
- task-relative effective work。

所以：

$$
\boxed{
W_I
\text{ 必須附帶 measurement contract}.
}
$$

---

# 6. Interaction Depth / Span

令：

$$
\mathcal P(G_I)
$$

為所有合法因果路徑集合。

定義：

$$
D_I
=
\max_{\pi\in\mathcal P(G_I)}
\sum_{v\in\pi}\omega(v).
$$

其含義是：

> 即使存在無限多 worker，目前依賴結構仍不能突破的最長必要鏈。

因此：

$$
\boxed{
D_I
=
\text{Irreducible Interaction Depth}.
}
$$

此「不可約」只相對於當前任務圖與依賴契約，而非宇宙絕對不可約。

---

# 7. Critical Path

若：

$$
\pi^\ast
=
\arg\max_{\pi\in\mathcal P(G_I)}
\sum_{v\in\pi}\omega(v),
$$

則 $\pi^\ast$ 是 critical path。

它決定理想平行環境下的 completion latency 下界。

因此優化 Agent 系統不能只問：

> 怎麼少做幾步？

還必須問：

> 哪些步驟位於 critical path 上？

---

# 8. 理想平行度

定義：

$$
\Pi_I
=
\frac{W_I}{D_I}.
$$

若：

$$
\Pi_I\approx1,
$$

代表工作幾乎完全串行。

若：

$$
\Pi_I\gg1,
$$

代表具有較高潛在平行度。

但：

$$
\Pi_I
$$

只是結構性上限指標，不保證真實 speedup。

---

# 9. 有限 Agent 條件

若只有 $P$ 個等價 worker，理想化執行時間至少滿足：

$$
T_P
\ge
\max
\left(
\frac{W_I}{P},
D_I
\right).
$$

因此：

$$
\boxed{
P\rightarrow\infty
\not\Rightarrow
T_P\rightarrow0.
}
$$

依賴鏈本身形成不可被 worker 數量直接消除的下界。

---

# 10. Brent-style 排程直觀

經典 parallel scheduling 給出一個重要直觀：若 computation 的總工作是 $W$，深度是 $D$，則有限 $P$ 處理器下的時間可由 $D$ 與 $W/P$ 共同控制。

本文不把經典式直接宣稱為一般 Agent 定理，因為 Agent 系統還包含：

- 非均質 worker；
- 不確定 latency；
- communication；
- validation；
- side effect；
- dynamic graph；
- speculative branch；
- human gate。

本文只吸收其核心 discipline：

$$
\boxed{
\text{總工作與 critical depth 應分別入帳}.
}
$$

---

# 11. Agent-native 有效時間

真實系統還存在：

$$
T_{\mathrm{comm}},
\quad
T_{\mathrm{sync}},
\quad
T_{\mathrm{verify}},
\quad
T_{\mathrm{merge}},
\quad
T_{\mathrm{wait}},
\quad
T_{\mathrm{human}},
\quad
T_{\mathrm{external}}.
$$

這些量不應機械地全部相加；更合理的做法是將其標註在 $G_I$ 的節點與邊上，再計算 path-dependent latency。

---

# 12. 五種圖不可混同

至少區分：

$$
G_C
=
\text{Computation Graph},
$$

$$
G_M
=
\text{Communication Graph},
$$

$$
G_K
=
\text{Memory / Knowledge Graph},
$$

$$
G_A
=
\text{Authority Graph},
$$

$$
G_W
=
\text{World-Commit Graph}.
$$

因此：

$$
\boxed{
G_C
\neq
G_M
\neq
G_K
\neq
G_A
\neq
G_W.
}
$$

誰和誰通信，不等於誰依賴誰；誰依賴誰，也不等於誰有權控制誰。

---

# 13. Communication Edge 不等於 Dependency Edge

若：

$$
A_1\rightarrow A_3
$$

表示 $A_1$ 的輸出是 $A_3$ 的必要前件，這是 computation dependency。

但若：

$$
A_1\leftrightarrow A_2
$$

只是交換參考意見，且任一方都可獨立完成，則主要屬於 communication topology。

所以：

$$
\boxed{
\text{Message Edge}
\not\Rightarrow
\text{Hard Dependency Edge}.
}
$$

---

# 14. Hard 與 Soft Dependency

定義硬依賴：

$$
u\prec_Hv
$$

表示若 $u$ 不完成， $v$ 不合法或不可執行。

定義軟依賴：

$$
u\prec_Sv
$$

表示 $u$ 的資訊可能提升 $v$ 品質，但 $v$ 可獨立執行。

所以：

$$
E_I
=
E_H
\cup
E_S.
$$

Scheduler 對 $E_H$ 保持必要順序，對 $E_S$ 則可進行成本—收益決策。

---

# 15. Speculative Parallelism

對 soft dependency，可讓 $v$ 在缺少 $u$ 時先 speculative execution：

$$
v^{spec}.
$$

若後續相容：

$$
Merge(u,v^{spec}).
$$

若衝突：

$$
Invalidate(v^{spec})
$$

或：

$$
Repair(v^{spec}).
$$

其收益是降低 latency，代價是可能增加：

$$
W_{\mathrm{waste}}.
$$

---

# 16. Useful Work 與 Wasted Work

總工作可分解：

$$
W_I
=
W_{\mathrm{useful}}
+
W_{\mathrm{redundant}}
+
W_{\mathrm{invalidated}}
+
W_{\mathrm{coord}}.
$$

因此多 Agent 可以同時出現：

$$
W_I\uparrow
$$

與：

$$
T_P\downarrow.
$$

這表示用更多總工作換取更短曆時，而不是矛盾。

---

# 17. 平行時間槓桿

定義理想 parallel leverage：

$$
\Lambda_P^{ideal}
=
\frac{W_I}{D_I}.
$$

定義觀察到的 wall-clock leverage：

$$
\Lambda_P^{real}
=
\frac{T_1^{ref}}{T_P^{obs}}.
$$

跨系統比較時必須控制：

- 同一任務；
- 同一成功條件；
- 可比品質；
- scheduler；
- model；
- budget。

---

# 18. Width 與平行槽位

令 $\mathcal A$ 為 antichain，即彼此不可比較的事件集合。

定義最大寬度：

$$
B_I
=
\max_{\mathcal A}|\mathcal A|.
$$

它提供結構性的最大可同時工作槽位。

但：

$$
B_I
$$

不等於實際最佳 Agent 數，因為還有成本、通信、驗證與 diminishing return。

---

# 19. Agent 數量飽和

當 $P$ 很小時，增加 Agent 可能降低 latency。

當：

$$
P\gg\Pi_I,
$$

更多 Agent 可能主要增加：

$$
W_{\mathrm{coord}},
\quad
W_{\mathrm{redundant}},
\quad
C_{\mathrm{comm}}.
$$

因此：

$$
\boxed{
\text{More Agents}
\not\Rightarrow
\text{More Effective Parallelism}.
}
$$

---

# 20. Communication Cost

定義：

$$
C_{\mathrm{comm}}
=
f
\left(
N_{\mathrm{msg}},
B_{\mathrm{msg}},
L_{\mathrm{msg}},
N_{\mathrm{sync}},
R_{\mathrm{round}}
\right).
$$

fully connected communication 可能具有：

$$
|E_M|
=
O(P^2).
$$

因此 sparse topology 可能降低成本，但過度稀疏也可能切斷重要 error-correction edge。

---

# 21. Dynamic Communication Topology

令：

$$
G_M(t)
$$

表示第 $t$ 個 control state 的通信圖。

則：

$$
G_M(t+1)
=
\mathcal T
\left(
G_M(t),
Task,
Uncertainty,
Conflict,
Trust,
Cost,
Evidence
\right).
$$

成熟 runtime 不必讓所有 Agent 永遠互相通信。

---

# 22. Isolate、Share、Join

定義：

$$
\mathcal I
=
\text{Isolate},
$$

$$
\mathcal S
=
\text{Share},
$$

$$
\mathcal J
=
\text{Join}.
$$

Isolate 用來保留獨立思考；Share 交換 artifact、summary、certificate 或 evidence；Join 則進入共同依賴與 synthesis。

因此：

$$
\boxed{
\mathcal I
\leftrightarrow
\mathcal S
\leftrightarrow
\mathcal J
}
$$

本身就是 runtime topology control。

---

# 23. Join 不等於 Concatenate

對兩分支：

$$
B_1,
B_2,
$$

定義 Join：

$$
J
:
(B_1,B_2,C)
\rightarrow
M,
$$

其中 $C$ 是 merge contract。

Join 必須處理：

- schema compatibility；
- semantic conflict；
- duplicate evidence；
- provenance；
- authority；
- version；
- validator state。

所以：

$$
\boxed{
\text{Join}
\neq
\text{Concatenate}.
}
$$

---

# 24. Barrier

Barrier 節點 $\beta$ 要求 predecessors：

$$
Pred(\beta)
=
\{u_1,\ldots,u_m\}
$$

滿足條件後才可繼續。

若等待全部分支：

$$
T_\beta
=
\max_iT(u_i)
+
C_{\mathrm{barrier}}.
$$

不必要 barrier 會直接增加 critical path。

---

# 25. Straggler Effect

若：

$$
T_1,\ldots,T_m
$$

是平行分支 latency，而 Join 等待全部：

$$
T_{join}
=
\max_iT_i
+
C_J.
$$

一個 straggler 即可能支配整體 latency。

Scheduler 因此可能需要 timeout、duplicate、partial join、quorum 或 early stopping。

---

# 26. Quorum Join

若不要求所有分支完成，可定義：

$$
J_q,
\qquad
q\le m.
$$

但 quorum 必須有 adequacy contract。

否則過早停止可能遺失關鍵反例或少數 evidence。

---

# 27. Race Condition

若：

$$
a\parallel b
$$

同時作用於共享狀態，且：

$$
a\circ b
\neq
b\circ a,
$$

則存在非交換性風險。

所以：

$$
\boxed{
a\parallel b
\text{ 合法}
\not\Rightarrow
\text{兩者可安全無序 commit}.
}
$$

---

# 28. Commutativity Certificate

若可證：

$$
a\circ b
=
b\circ a
$$

或至少在任務投影下：

$$
a\circ b
\equiv_T
b\circ a,
$$

則可建立：

$$
Cert_{comm}(a,b).
$$

有 certificate 的 action 可更安全地 parallelize；沒有時可採 serial、sandbox branch、conflict detection 或 post-validation。

---

# 29. Causal Merge

若兩分支有共同 ancestor $A$：

$$
A
\rightarrow
\begin{cases}
B_1,\\
B_2,
\end{cases}
$$

merge 後需保留：

$$
Lineage(M)
=
(A,B_1,B_2,C_{merge}).
$$

因此：

$$
\boxed{
\text{Merge}
\neq
\text{History Collapse}.
}
$$

---

# 30. Redundancy 與 Independence

若：

$$
O_1
=
O_2
=
\cdots
=
O_n,
$$

不代表存在 $n$ 份獨立 evidence。

若 Agent 共享 model family、prompt、retrieval source、tool、evaluator 或 upstream artifact，則 independence 可以很低。

因此：

$$
\boxed{
\text{Parallel Replication}
\neq
\text{Independent Confirmation}.
}
$$

---

# 31. Epistemic Parallelism

區分：

## 31.1 Throughput Parallelism

目的是更快完成互不依賴工作。

## 31.2 Epistemic Parallelism

目的是形成真正不同的方法、模型、假設、資料、反例或 evaluator。

所以：

$$
\boxed{
\text{Epistemic Diversity}
\neq
\text{Worker Count}.
}
$$

---

# 32. 多 Agent 協調債務

定義：

$$
D_{\mathrm{coord}}
=
D_{\mathrm{msg}}
+
D_{\mathrm{merge}}
+
D_{\mathrm{conflict}}
+
D_{\mathrm{state}}
+
D_{\mathrm{authority}}.
$$

當 Agent 數量增加但協調基礎設施未同步成熟時：

$$
D_{\mathrm{coord}}\uparrow.
$$

甚至可能：

$$
T_P\uparrow.
$$

---

# 33. Dynamic Computation Graph

真實 Agent 圖可隨執行更新：

$$
G_I^{(0)}
\rightarrow
G_I^{(1)}
\rightarrow
\cdots
$$

原因包括 task decomposition、tool failure、replan、new evidence、branch creation、branch kill、human intervention 與 budget change。

因此：

$$
\boxed{
G_I
=
G_I(t,state,evidence,budget).
}
$$

---

# 34. Graph Revision 必須成為事件

若：

$$
E_I^{(n)}
\rightarrow
E_I^{(n+1)},
$$

應建立：

$$
GraphRevisionEvent.
$$

不能 silent rewrite，否則執行後無法審計為何 topology 改變。

---

# 35. Static DAG 到 Adaptive Semantic-Causal Graph

傳統 task graph：

$$
G=(V,E).
$$

AI-native runtime 可根據語義與 runtime evidence 改變 node decomposition、edge hardness、agent assignment、validator、fallback 與 branch budget。

所以：

$$
\boxed{
\text{Static Task Graph}
\rightarrow
\text{Adaptive Semantic-Causal Graph}.
}
$$

這不是否定 DAG，而是增加 dynamic control plane。

---

# 36. Critical Path 可以被改寫

Agent 可透過：

1. 更好的 decomposition；
2. 提前預取；
3. parallel tool calls；
4. alternate provider；
5. memoization；
6. speculative execution；
7. better interface；
8. relaxed soft dependency；
9. faster validator；
10. partial join；

降低：

$$
D_I.
$$

所以 AI 的高階能力之一是：

$$
\boxed{
\text{Critical-Path Restructuring}.
}
$$

---

# 37. Interaction Depth 與 Reasoning Depth 不同

令：

$$
D_R
=
\text{model reasoning depth}.
$$

一般：

$$
D_R
\neq
D_I.
$$

因為整體 interaction depth 還可能來自 API dependency、human approval、test、build、world observation 與 external event。

因此：

$$
\boxed{
\text{Reasoning Depth}
\neq
\text{Interaction Depth}.
}
$$

---

# 38. Human Gate 位於 Critical Path

若不可逆操作需要人類批准：

$$
A
\rightarrow
H
\rightarrow
Commit,
$$

且無替代路徑，則 $H$ 位於 critical path。

因此即使機器高度自動化，少數 human governance node 仍可能支配整體 latency。

---

# 39. Human Parallelism 不等於 Machine Parallelism

可能：

$$
P_A\gg1,
$$

但：

$$
P_H
$$

受責任、認知與制度限制。

所以：

$$
\boxed{
A_P\uparrow
\not\Rightarrow
H_P\uparrow.
}
$$

---

# 40. Verification Graph

定義：

$$
G_V
=
(V_V,E_V).
$$

syntax、test、citation、safety、schema、proof checker 等驗證可以部分平行，但某些驗證仍需要 sequential aggregation：

$$
Evidence
\rightarrow
Review
\rightarrow
Authority.
$$

因此 validation 也是互動因果圖的一部分。

---

# 41. World Commit Graph

典型外部提交鏈：

$$
InternalResult
\rightarrow
Validator
\rightarrow
Authority
\rightarrow
Commit
\rightarrow
WorldObservation.
$$

多 Agent 共識不能自動跳過 authority。

所以：

$$
\boxed{
\text{Consensus}
\neq
\text{Commit Authority}.
}
$$

---

# 42. Parallel World Exploration

WDC 類系統可：

$$
F
\rightarrow
\begin{cases}
W_1,\\
W_2,\\
\vdots\\
W_m.
\end{cases}
$$

這是一種高成本 epistemic parallelism。

若：

$$
ExpectedGain
<
C_{world},
$$

應跳過深度 world expansion。

---

# 43. Topology Routing

對 task graph：

$$
G_T,
$$

可由 router：

$$
\mathcal R_{topo}
:
G_T
\times
ResourceState
\times
Risk
\times
LatencyTarget
\rightarrow
\Theta,
$$

其中：

$$
\Theta
\in
\{
parallel,
sequential,
hierarchical,
hybrid
\}.
$$

Topology 因而成為 runtime decision，而不是固定架構。

---

# 44. 2026 Multi-Agent 外部近鄰

2026 年已有多個直接近鄰：

- AdaptOrch：task decomposition DAG 到多種 orchestration topology；
- MASFactory：directed computation graph 表示 Agent/subworkflow 與依賴；
- LAMaS：把 critical-path length 納入 multi-Agent latency optimization；
- inference-time parallelism：區分 parallel trajectories 與 intra-trajectory dependency-aware parallelism；
- GTD：動態生成 communication topology，平衡 accuracy、cost 與 robustness。

這些工作共同支持：

$$
\boxed{
\text{Agent capability}
\text{ partly depends on execution topology}.
}
$$

---

# 45. Dynamic Topology 與 Token Cost

若通信圖完全連接：

$$
|E_M|
\sim
O(P^2),
$$

可能增加 token、latency、noise、redundancy 與 correlated error。

因此 sparse、task-adaptive communication 具有工程價值；但過度稀疏也可能犧牲 error correction。

所以 topology design 是多目標問題。

---

# 46. Topology Objective

可定義：

$$
J(\Theta)
=
\alpha Q
-
\beta T
-
\gamma C
-
\delta R
+
\eta D_{epi},
$$

其中：

- $Q$：quality；
- $T$：latency；
- $C$：compute / token / communication cost；
- $R$：risk；
- $D_{epi}$：epistemic diversity。

最佳 topology：

$$
\Theta^\ast
=
\arg\max_\Theta J(\Theta).
$$

---

# 47. Interaction-Time Efficiency

定義：

$$
\eta_I
=
\frac{V_{\mathrm{effective}}}{W_I},
$$

與：

$$
\eta_D
=
\frac{V_{\mathrm{effective}}}{D_I}.
$$

兩者不同。

因此：

$$
\boxed{
\text{Efficiency}
\text{ is vector-valued}.
}
$$

---

# 48. Parallel Waste Ratio

定義：

$$
\rho_W
=
\frac{
W_{\mathrm{redundant}}
+
W_{\mathrm{invalidated}}
+
W_{\mathrm{coord}}
}{W_I}.
$$

 $\rho_W$ 可作為 adaptive topology 的 feedback signal。

---

# 49. Critical-Path Contribution

定義：

$$
CP(v)
\in
\{0,1\}
$$

表示節點是否屬於至少一條 critical path。

更一般可用 sensitivity：

$$
S_D(v)
=
-
\frac{\partial D_I}{\partial\omega(v)}.
$$

這使 scheduler 區分 expensive node 與 latency-critical node。

---

# 50. 第一代 Interaction-Time Topology Ledger

```text
InteractionTopology
  topology_id
  intent_version
  run_id
  graph_version
  node_id
  node_type
  actor_id
  agent_model
  action_ref
  weight_contract
  work_weight
  parent_node_ids
  hard_dependencies
  soft_dependencies
  message_edges
  memory_edges
  authority_edges
  commit_edges
  branch_id
  join_id
  barrier_id
  checkpoint_ref
  validation_ref
  communication_cost
  synchronization_cost
  completion_delta
  knowledge_delta
  risk_delta
  useful_work_class
  critical_path_membership
  provenance_ref
```

---

# 51. 第一代核心指標

$$
W_I
=
\text{Interaction Work},
$$

$$
D_I
=
\text{Interaction Depth / Span},
$$

$$
B_I
=
\text{Maximum Parallel Width},
$$

$$
\Pi_I
=
\frac{W_I}{D_I},
$$

$$
C_{\mathrm{comm}}
=
\text{Communication Cost},
$$

$$
D_{\mathrm{coord}}
=
\text{Coordination Debt},
$$

$$
\rho_W
=
\text{Parallel Waste Ratio}.
$$

這些不應被強迫合併成單一分數。

---

# 52. 可檢驗命題

## 命題一：Work–Depth 分離

存在 $A,B$：

$$
W_I^{(A)}
=
W_I^{(B)}
$$

但：

$$
D_I^{(A)}
\neq
D_I^{(B)}.
$$

## 命題二：Parallelism Saturation

對固定因果圖：

$$
P\rightarrow\infty
$$

時仍受 $D_I$ 限制。

## 命題三：Coordination Reversal

存在任務區間，使：

$$
P_2>P_1
$$

但：

$$
T_{P_2}^{eff}
>
T_{P_1}^{eff}.
$$

## 命題四：Topology Dominance

同一模型集合在不同 topology 下可產生顯著不同的：

$$
(Q,T,C).
$$

## 命題五：Soft-Dependency Relaxation

speculative execution 可降低 $D_I$，但增加 $W_{\mathrm{invalidated}}$。

## 命題六：Independent-Evidence

增加 worker count 不保證增加 epistemic independence。

---

# 53. 實驗設計

## 53.1 Same Work / Different Span

保持 $W_I$ 相同，人工改變 DAG 的 $D_I$。

## 53.2 Same Agents / Different Topology

固定 Agent pool，比較 sequential、parallel、hierarchical、hybrid。

## 53.3 Barrier Ablation

移除非必要 barrier，測量 $\Delta D_I$ 與一致性錯誤。

## 53.4 Sparse Communication

比較 fully connected 與 sparse adaptive graph 的 token、latency 與 error-correction。

## 53.5 Straggler Injection

比較 all-join、quorum-join 與 timeout-fallback。

## 53.6 Independence Test

比較同源與異源模型／資料的多 Agent 驗證。

---

# 54. 與時代拓撲論的回接

時代拓撲論反對：

$$
\text{shared clock}
\Rightarrow
\text{shared epoch}.
$$

在微觀尺度上：

$$
\text{shared wall-clock interval}
\not\Rightarrow
\text{shared interaction depth}.
$$

兩個系統即使都執行十分鐘，其：

$$
W_I,
D_I,
B_I,
C_{\mathrm{comm}},
Q
$$

仍可完全不同。

因此：

$$
\boxed{
\text{Physical Co-time}
\neq
\text{Computational Co-depth}.
}
$$

---

# 55. 與時間經濟學的接口

多 Agent 平行化把時間配置問題寫成：

$$
\text{Human Time}
+
\text{Machine Work}
+
\text{Critical Depth}
+
\text{Coordination Cost}.
$$

同一預算可以選擇：

- 少量 Agent 深度串行；
- 大量 Agent 平行；
- 多分支搜索；
- 一條高品質 critical path；
- 先 parallel 再 Join。

最優配置取決於任務。

---

# 56. 與第 5 篇的接口

本文回答：

> Agent 系統的總工作與不可約因果深度如何表示？

下一篇將問：

> 在 token、compute、context、tool quota、parallel slots 與金錢都有限時，下一單位智能計算應配置到哪個節點、branch、Agent 或 validator？

將建立：

$$
B_A
=
(
B_{\mathrm{token}},
B_{\mathrm{compute}},
B_{\mathrm{context}},
B_{\mathrm{tool}},
B_{\mathrm{parallel}},
B_{\mathrm{runtime}}
),
$$

以及：

$$
\boxed{
\text{Machine-Time Portfolio Allocation}.
}
$$

---

# 57. 規範與倫理邊界

互動時間拓撲不應被用來：

1. 把 Agent 數量當能力指標；
2. 把通信密度當協作品質；
3. 為縮短 critical path 而繞過安全與授權；
4. 把 speculative branch 當已驗證結果；
5. 把多 Agent 一致誤報成獨立證據；
6. 將 authority topology 與 computation topology 混同；
7. 因追求平行而忽略 race、conflict 與 side effect；
8. 用 nominal speedup 隱藏總 compute 急升；
9. 以更多 world simulation 取代 reality validation；
10. 把 work–span 誤宣稱為所有 Agent 系統的完整性能定律。

---

# 58. 理論限制

第一，本文以 DAG／偏序表示 execution；顯式循環可透過 event unfolding 或版本化節點處理。

第二， $W_I$ 與 $D_I$ 依賴事件粒度與權重契約。

第三，動態 graph 下 serial 與 parallel run 可能產生不同 computation，因此 speedup baseline 需審慎定義。

第四，通信與驗證成本對 Agent 數量可能呈非線性。

第五，epistemic independence 仍需更完整的來源、模型與 evaluator dependency measure。

第六，本文不提供所有 topology routing 問題的全域最優算法。

---

# 59. 結論

本文把 AI 互動由線性：

$$
e_1
\rightarrow
e_2
\rightarrow
\cdots
\rightarrow
e_n
$$

提升為：

$$
\boxed{
G_I
=
(V_I,E_I,\prec,\omega,\lambda).
}
$$

並正式區分：

$$
\boxed{
W_I
=
\text{Interaction Work}
}
$$

與：

$$
\boxed{
D_I
=
\text{Irreducible Interaction Depth}.
}
$$

因此：

$$
\boxed{
\text{做了多少}
\neq
\text{必須走多深}.
}
$$

多 Agent 的真正價值不只是「更多 AI 同時工作」，而是能否找到真正可平行的子問題、刪除不必要依賴、保留必要因果、控制通信與同步、避免無效 branch、正確 Join、保存 lineage，並在不繞過驗證與權限的前提下縮短 critical path。

成熟 Agent runtime 的時間問題因此不再只是：

> 要多少秒？

而是：

$$
\boxed{
\text{在有限智能資源下，能否重編排意圖的因果圖，
讓更多工作平行，同時不增加不可接受的錯誤、協調與治理成本？}
}
$$

這就是本文所稱的互動時間拓撲。

---

# 參考文獻與前置理論

## EveMissLab 前置理論

1. Neo.K，《互動時間論：從鐘錶時間到意圖驅動的智能狀態轉換》v0.1，EveMissLab，2026。
2. Neo.K，《意圖週期論：使用者意圖、AI 接受、執行與結果的閉環結構》v0.1，EveMissLab，2026。
3. Neo.K，《單輪不是一步：AI Turn、內部迴圈、工具動作與執行軌跡》v0.1，EveMissLab，2026。
4. Neo.K，《MWT-03：Global Interaction Graph and Noncommutative Scheduler》，EveMissLab，2026。
5. Neo.K，《MWT-09：World Computability, Complexity and Resource-Bounded Mathematics》，EveMissLab，2026。
6. Neo.K，《動態協作拓撲：從 Isolate、Share 到 Join》v0.1，EveMissLab，2026。
7. Neo.K，《WDC-08: Tri-Temporal World-Domain Computation》，EveMissLab，2026。
8. Neo.K，《Compositional Visual-World Reachability Graphs》v0.1，EveMissLab，2026。

## 外部研究

9. Lamport, L. *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM, 21(7), 558–565, 1978.
10. Brent, R. P. *The Parallel Evaluation of General Arithmetic Expressions*. Journal of the ACM, 21(2), 201–206, 1974.
11. Blumofe, R. D., Joerg, C. F., Kuszmaul, B. C., Leiserson, C. E., Randall, K. H., Zhou, Y. *Cilk: An Efficient Multithreaded Runtime System*. Journal of Parallel and Distributed Computing, 37, 55–69, 1996.
12. *AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence*. arXiv:2602.16873, 2026.
13. *Learning Latency-Aware Orchestration for Parallel Multi-Agent Systems*. arXiv:2601.10560, 2026.
14. *MASFactory: A Graph-Centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing*. arXiv:2603.06007, 2026.
15. *A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems*. arXiv:2608.05791, 2026.
16. Jiang, E. H., et al. *Dynamic Generation of Multi-LLM Agents Communication Topologies with Graph Diffusion Models*. arXiv:2510.07799v2, 2026.
17. Gou, W., Liu, Z. *Dynamic Trust-Aware Sparse Communication Topology for LLM-Based Multi-Agent Consensus*. arXiv:2606.01828, 2026.
18. Chen, H., et al. *GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems*. arXiv:2603.19677, 2026.

---

## 一句話版本

> **多 Agent 的互動時間不是所有步驟相加，也不是牆鐘時間本身，而是「總工作量」與「最長不可約因果路徑」共同決定、並受通信、驗證、協調與世界提交成本修正的偏序拓撲。**

---

*EML-ITT-2026-04-v0.1*  
*AI 互動時間與智能時間經濟學系列 04/08*
