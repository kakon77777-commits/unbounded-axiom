# LRC–COL-04：最大有效算子集與語言複雜度上界
## The Maximum Effective Operator Set and the Upper Bound of Language Complexity

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL-03 從下界研究複合符號算子語言：在指定目標域、Agent、誤差、組合深度與資源限制下，最少需要多少 operator 才能達到形式完備、有效完備與穩健完備。本篇則研究相反方向：

> **一套複合算子語言最多可以擴張到多大，才不會因 operator 過多而讓整體認知、選擇、傳播與執行能力開始下降？**

如果只看儲存能力，數位系統可以保存極大量 operator，因此似乎不存在有意義的上限。但對 AI 而言，真正瓶頸並不只是「能存多少」，而是「每次任務需要同時辨識、區分、檢索、選擇與組合多少」。當 operator 數量增加時，coverage 可能提升，composition depth 可能下降；但同時也可能增加 selection entropy、語義重疊、同義詞碰撞、工具干擾、context cost、long-tail underuse、版本治理成本與 semantic fragmentation。

近年的大型工具使用研究已經直接呈現這個工程問題。真實 LLM Agent 的 toolsets 可擴展到數千個工具，但大規模工具集合中的冗餘、重疊描述、上下文限制與檢索問題會降低工具選擇品質；2026 年 ToolScope 透過 tool merging 與 context-aware filtering 縮減候選工具集合，在多個 benchmark 與模型上提高工具選擇準確率。這說明「增加可用操作」與「提高有效可選操作」不是同一件事。

本文因此提出一個重要區分：

$$
\boxed{
N_G
\neq
N_A
}
$$

其中 $N_G$ 是全域 operator library 的總規模，而 $N_A(q)$ 是特定任務 $q$ 當下真正進入 Agent 選擇／組合視野的 active operator set。全域語言庫可以很大，但活躍候選集必須被控制在 Agent、context 與選擇機制可處理的範圍。

本文正式定義 **Maximum Effective Operator Set（最大有效算子集）**、**Active-Set Upper Bound（活躍集上界）**、**Selection Entropy（選擇熵）**、**Semantic Collision Density（語義碰撞密度）**、**Operator Interference Matrix（算子干擾矩陣）**、**Dead-Operator Ratio（死算子比例）** 與 **Marginal Operator Utility（算子邊際效用）**。本文並提出：

$$
\boxed{
N_{\min}^{effective}
\le
N^*
\le
N_{\max}^{effective},
}
$$

其中 $N^*$ 是效用最佳點，而 $N_{\max}^{effective}$ 是語言仍維持可接受品質的最大有效邊界。

核心結論是：未來複合符號語言的上限不是一個單純的「字典最多幾個詞」問題，而是：

$$
\boxed{
\text{Global Library}
\rightarrow
\text{Retrieval / Routing}
\rightarrow
\text{Active Working Set}
\rightarrow
\text{Composition}
}
$$

的分層架構問題。真正應被限制的，往往不是全域知識庫的大小，而是每次任務必須同時競爭的有效 operator 選擇寬度。

---

## 關鍵詞

最大有效算子集；語言複雜度；operator library；selection entropy；tool retrieval；semantic collision；vocabulary explosion；AI Agent；context window；複合符號語言

---

# 1. 問題：operator 真的可以一直加嗎？

如果新增 operator：

$$
O_{N+1}
$$

可以覆蓋新的能力，

直覺似乎是：

$$
N\uparrow
\Rightarrow
Capability\uparrow.
$$

但這只看到新增能力，

沒有看到新增 operator 同時進入：

- 選擇空間；
- 記憶空間；
- context；
- 版本系統；
- 檢索索引；
- 語義鄰域；
- Agent 的決策分布。

因此更完整應寫：

$$
\boxed{
\Delta V(O_{N+1})
=
\Delta Capability
-
\Delta Complexity.
}
$$

如果：

$$
\Delta V<0,
$$

新增 operator 反而讓整個語言變差。

---

# 2. 最大有效不等於最大可儲存

現代系統可以儲存：

$$
10^6
$$

甚至更多 operator definitions。

所以：

$$
N_{\max}^{storage}
$$

通常不是主要問題。

真正問題是：

$$
\boxed{
N_{\max}^{effective}.
}
$$

即：

> **在不顯著降低檢索、選擇、組合、學習、保真與治理品質的情況下，系統實際可以有效維持多少 operator？**

---

# 3. 第一個重大區分：Global vs Active

令：

$$
\mathcal O_G
$$

是全域 operator library。

$$
N_G
=
|\mathcal O_G|.
$$

但每個 query：

$$
q
$$

真正需要進入工作視野的只有：

$$
\mathcal O_A(q)
\subseteq
\mathcal O_G.
$$

令：

$$
N_A(q)
=
|\mathcal O_A(q)|.
$$

因此：

$$
\boxed{
N_G
\neq
N_A(q).
}
$$

---

# 4. 為什麼這個區分改變整個問題？

如果所有 operator 都直接放進 prompt / working context：

$$
N_A=N_G.
$$

隨 $N_G$ 增長，

選擇與 context 成本也直接增長。

但如果有：

$$
\boxed{
\mathcal O_G
\xrightarrow{Retrieve}
\mathcal O_A(q)
}
$$

那麼：

$$
N_G\uparrow
$$

不一定要求：

$$
N_A\uparrow.
$$

因此全域 library 可以遠大於 active set。

---

# 5. ToolScope 所揭露的同構問題

2026 年的 ToolScope 研究直接指出：

- 真實工具集常包含冗餘工具；
- 名稱與描述互相重疊；
- 這些重疊造成 ambiguity；
- 大工具集也受到 input context limit 限制。

其解法不是：

> 讓 LLM 一次看更多工具。

而是：

1. merge redundant tools；
2. context-aware filtering；
3. 只保留 query-relevant subset。

這與本文的：

$$
\boxed{
\mathcal O_G
\rightarrow
\mathcal O_A(q)
}
$$

完全同構。

---

# 6. 所以需要四個不同的 N

本文建議至少區分：

### $N_G$ — Global Library Size

全域所有 operator。

### $N_R(q)$ — Retrieved Candidate Size

retriever 找回的候選數。

### $N_A(q)$ — Active Selection Size

真正交給 Agent 競爭選擇的數量。

### $N_C$ — Resident Core Size

永遠常駐、幾乎所有任務都可用的核心 operator。

因此：

$$
\boxed{
N_C
\le
N_A
\le
N_R
\le
N_G.
}
$$

---

# 7. 「最大有效」可能主要是 $N_A$ 的問題

全域：

$$
N_G
$$

可以藉由：

- retrieval；
- hierarchy；
- namespace；
- routing；

持續擴張。

真正受到：

- context；
- attention；
- semantic competition；

限制的通常是：

$$
\boxed{
N_A.
}
$$

所以未來可能需要：

$$
N_{\max}^{active}
$$

而不是只說：

$$
N_{\max}^{global}.
$$

---

# 8. Active Selection Entropy

若 Agent 對 active operators 的選擇分布：

$$
p_i=P(O_i\mid q),
$$

定義：

$$
\boxed{
H_{sel}(q)
=
-\sum_{i=1}^{N_A}
p_i\log p_i.
}
$$

當：

- 候選很多；
- 描述相似；
- 功能接近；

時：

$$
H_{sel}\uparrow.
$$

---

# 9. 高 Selection Entropy 的意思

高：

$$
H_{sel}
$$

不一定表示 Agent 很有彈性。

也可能表示：

> 它根本不知道該選哪一個。

因此需要區分：

$$
\boxed{
\text{Choice Diversity}
\neq
\text{Choice Uncertainty}.
}
$$

---

# 10. Selection Accuracy

如果正確 operator：

$$
O^*
$$

在 active set 中，

選擇成功率：

$$
P_{sel}
=
P(
\hat O=O^*
\mid O^*\in\mathcal O_A
).
$$

總 tool/operator success：

$$
\boxed{
P_{total}
=
P_{retrieve}
\cdot
P_{sel}
\cdot
P_{exec}.
}
$$

所以增加全域 operator：

$$
N_G
$$

可能：

- 提高 coverage；
- 但降低 retrieval 或 selection。

---

# 11. Coverage–Selection Tradeoff

新增 operator：

$$
O_{new}
$$

可能：

$$
Coverage\uparrow.
$$

但：

$$
P_{sel}\downarrow.
$$

因此：

$$
\boxed{
\text{More capability options}
\neq
\text{more usable capability}.
}
$$

---

# 12. 最大有效邊界的第一版直覺

若：

$$
N
$$

增加到某一點後：

$$
\Delta Coverage
<
\Delta SelectionLoss
+
\Delta ContextCost
+
\Delta GovernanceCost,
$$

則已越過最大有效區域。

---

# 13. Marginal Operator Utility

對新 operator：

$$
O,
$$

定義：

$$
\boxed{
\Delta J(O\mid\mathcal O)
=
G_C
+
G_D
+
G_Y
+
G_R
-
C_S
-
C_X
-
C_V
-
C_D.
}
$$

其中正收益：

- $G_C$：coverage gain；
- $G_D$：depth reduction；
- $G_Y$：action-yield gain；
- $G_R$：robustness gain。

負成本：

- $C_S$：selection cost；
- $C_X$：context cost；
- $C_V$：version / maintenance；
- $C_D$：drift / ambiguity。

---

# 14. Operator Admission Gate

只有：

$$
\boxed{
\Delta J(O\mid\mathcal O)>\tau_{add}
}
$$

才把新 operator 正式加入 stable language。

否則：

- 保持 experimental；
- 當 local macro；
- 或不加入。

---

# 15. 最大有效基底的第一版定義

對固定 Agent、domain、grammar 與 budget：

$$
\boxed{
N_{\max}^{effective}
=
\max |\mathcal O|
}
$$

subject to：

$$
J(\mathcal O)\ge\tau_J,
$$

$$
P_{sel}\ge\tau_S,
$$

$$
F_{sem}\ge\tau_F,
$$

$$
C_{context}\le B_C,
$$

$$
C_{govern}\le B_G.
$$

---

# 16. $N^*$ 與 $N_{\max}$ 不同

令：

$$
\boxed{
N^*
=
\arg\max_N J(N).
}
$$

這是最佳點。

而：

$$
N_{\max}^{effective}
$$

是仍勉強維持 acceptable quality 的最右邊界。

所以：

$$
\boxed{
N_{\min}^{effective}
\le
N^*
\le
N_{\max}^{effective}.
}
$$

---

# 17. 有效語言區間

因此：

$$
\boxed{
I_{\mathcal O}^{effective}
=
[
N_{\min}^{effective},
N_{\max}^{effective}
].
}
$$

其中：

- 左邊：表達／coverage 不足；
- 中間：有效區；
- 右邊：複雜度開始壓過新增收益。

---

# 18. Vocabulary Explosion

如果任何高頻 workflow 都被創造成 operator：

$$
O_1,O_2,\ldots,O_N,
$$

最後：

$$
N\rightarrow\infty.
$$

這是：

$$
\boxed{
\text{Vocabulary Explosion}.
}
$$

其問題不是 storage，

而是：

- retrieval；
- naming；
- overlap；
- version；
- training；
- governance。

---

# 19. Synonym Collision

如果：

$$
Sem(O_i)\approx Sem(O_j),
$$

但兩個都存在，

Agent 可能難以選擇。

如果兩者功能幾乎相同：

$$
\boxed{
\text{Synonym Redundancy}.
}
$$

如果表面相近但行為不同：

$$
\boxed{
\text{Semantic Collision}.
}
$$

第二種通常更危險。

---

# 20. Semantic Collision Graph

建立：

$$
G_{col}
=
(V,E).
$$

node：

$$
O_i.
$$

若：

$$
Similarity(
Description(O_i),
Description(O_j)
)
>\tau_s
$$

但：

$$
Behavior(O_i)\neq Behavior(O_j),
$$

則加入 collision edge。

---

# 21. Collision Density

定義：

$$
\boxed{
\rho_{col}
=
\frac{
2|E|
}{
N(N-1)
}.
}
$$

若：

$$
\rho_{col}\uparrow,
$$

說明 language vocabulary 的 semantic neighborhood 越來越擁擠。

---

# 22. 為什麼名字相似可能比 operator 多更危險？

如果：

$$
N=1000
$$

但 operators 分在完全不同 namespace，

可能很好選。

如果：

$$
N=30
$$

但 20 個都叫：

- `search`
- `smart_search`
- `deep_search`
- `advanced_search`
- `search_plus`

選擇反而困難。

因此：

$$
\boxed{
\text{Effective Complexity}
\neq
N.
}
$$

---

# 23. Effective Operator Complexity

可以定義：

$$
\boxed{
C_{\mathcal O}^{eff}
=
f(
N_A,
H_{sel},
\rho_{col},
C_{context},
C_{version},
D_{namespace}
).
}
$$

operator count 只是其中一項。

---

# 24. Operator Interference Matrix

定義：

$$
M_{ij}
=
P(
\hat O=O_j
\mid
O_i
\text{ is target}
).
$$

理想：

$$
M_{ii}\approx1.
$$

如果：

$$
M_{ij}
$$

對某些 $i\neq j$ 很高，

表示兩 operator 互相干擾。

---

# 25. Interference Cluster

若一組：

$$
\{O_a,O_b,O_c\}
$$

互相混淆，

可以：

- merge；
- rename；
- namespace；
- add discriminative metadata。

這就是 language maintenance。

---

# 26. Context Cost

每個 active operator 通常需要：

- name；
- description；
- schema；
- examples；
- constraints。

所以：

$$
\boxed{
C_{ctx}
=
\sum_{O_i\in\mathcal O_A}
L(O_i).
}
$$

若：

$$
N_A\uparrow,
$$

通常：

$$
C_{ctx}\uparrow.
$$

---

# 27. Context Dilution

即使 context window 足夠放下全部 operators，

也不代表 Agent 對每個 operator 都能保持同樣辨識度。

這可以稱：

$$
\boxed{
\text{Context Dilution}.
}
$$

即：

> 能塞進 context，不等於能有效使用。

---

# 28. Context Capacity ≠ Cognitive Capacity

因此：

$$
\boxed{
N_{\max}^{context}
\neq
N_{\max}^{effective}.
}
$$

一個模型能讀 1M tokens，

不代表它能從 50,000 個相似 operator 中穩定挑對。

---

# 29. Live API-Bench 的現實提醒

2026 年 Live API-Bench 建立超過 2,500 個 live APIs 的工具使用 benchmark。

在多種工具調用設定下，受測 LLM 的 task completion 約落在 7–47%，互動式 ReAct Agent 最高也只改善到約 50%。

這不是證明：

> 2500 tools 就是上限。

但它提醒：

$$
\boxed{
\text{Large Tool Availability}
\neq
\text{Solved Tool Competence}.
}
$$

---

# 30. 大工具庫需要 Retrieval Layer

因此未來大 operator language 很可能不是：

$$
q
\rightarrow
\mathcal O_G.
$$

而是：

$$
\boxed{
q
\rightarrow
Retriever
\rightarrow
\mathcal O_R
\rightarrow
Selector
\rightarrow
O^*.
}
$$

---

# 31. Retrieval 其實是語言的一部分

如果 operator 只有被 retriever 找到才能被使用，

那：

$$
\boxed{
\text{retrieval semantics}
}
$$

實際上屬於 language runtime。

所以未來的 operator language 不只是 vocabulary + grammar。

而是：

$$
\boxed{
\text{Vocabulary}
+
\text{Grammar}
+
\text{Index}
+
\text{Retriever}
+
\text{Selector}.
}
$$

---

# 32. Tool-to-Agent Retrieval 的提醒

大型 multi-agent 系統甚至可能：

- 每個 Agent 管大量 tools；
- 上層還要選哪個 Agent。

此時：

$$
\boxed{
\text{tool selection}
+
\text{agent routing}
}
$$

形成二階選擇問題。

所以 operator scale 最終可能是：

$$
\text{hierarchical}.
$$

---

# 33. Hierarchical Language Hypothesis

未來大型 COL 更可能：

$$
\boxed{
Core
\rightarrow
Namespace
\rightarrow
Domain
\rightarrow
Operator
}
$$

而不是一張平坦表。

例如：

```text
core.query
core.branch
memory.retrieve
memory.supersede
agent.delegate
tool.file.move
tool.calendar.search
finance.payment.authorize
```

---

# 34. Hierarchy 降低 Active Width

如果 top-level 先選：

$$
Domain,
$$

再選：

$$
Operator,
$$

每一層需要區分的候選數會下降。

因此：

$$
\boxed{
N_G\uparrow
\text{ can coexist with bounded }N_A.
}
$$

---

# 35. Hierarchical Buffering Proposition

提出：

> **如果 retrieval / namespace quality 足夠高，全域 operator library 的規模可以遠快於 active working set 增長，而不造成等比例 selection degradation。**

形式：

$$
\boxed{
\frac{dN_A}{dN_G}\ll1.
}
$$

這是未來可測命題。

---

# 36. 但 hierarchy 也有 routing error

如果第一層 domain 選錯：

$$
D_{wrong},
$$

後面正確 operator 永遠看不到。

所以：

$$
P_{total}
=
P_{route}
P_{retrieve}
P_{select}
P_{execute}.
$$

層次越多，

每層都增加 failure surface。

---

# 37. Flat vs Hierarchical Tradeoff

### Flat

優點：

- routing 簡單；
- 不會 early branch mistake。

缺點：

- selection entropy 高；
- context 大。

### Hierarchical

優點：

- active set 小；
- namespace 清晰。

缺點：

- routing error；
- ontology maintenance。

所以：

$$
\boxed{
\text{Hierarchy}
\neq
\text{free scalability}.
}
$$

---

# 38. Dead Operator

如果 operator：

$$
O_i
$$

在長期 workload 中幾乎從不使用：

$$
P(O_i)\approx0,
$$

而它又沒有 safety / rare-critical 功能，

則可能是：

$$
\boxed{
\text{Dead Operator}.
}
$$

---

# 39. Dead-Operator Ratio

定義：

$$
\boxed{
\rho_{dead}
=
\frac{
|\{O_i: Usage(O_i)<\tau_u\}|
}{
N_G
}.
}
$$

高：

$$
\rho_{dead}
$$

表示 vocabulary 可能正在膨脹。

---

# 40. 但 rare 不等於 dead

某些 operator：

- emergency rollback；
- security revoke；
- catastrophic recovery；

使用頻率很低，

但非常重要。

所以：

$$
\boxed{
\text{Low Frequency}
\neq
\text{Low Value}.
}
$$

---

# 41. Risk-Weighted Operator Value

因此：

$$
Value(O_i)
=
Frequency_i\cdot Utility_i
+
Criticality_i.
$$

high-criticality operator 不能因 long-tail 被刪掉。

---

# 42. Frequency 與 Compositionality

2025 年 emergent communication 研究指出，compositionality 的形成與資料 exposure / frequency 結構有關，而不是 frequency 本身簡單單調決定。

這表示：

$$
\boxed{
\text{operator usage frequency}
}
$$

不只影響保留／刪除，

也可能影響 operator 最終採取：

- regular compositional form；
- idiosyncratic crystallized form。

---

# 43. 高頻 operator 可能值得結晶

若一個複合程序：

$$
P
$$

非常高頻，

直接保留 macro：

$$
O_P
$$

可能比每次重新 composition 更有效。

因此高頻區可能：

$$
\boxed{
\text{less primitive}
+
\text{more crystallized}.
}
$$

---

# 44. Long-Tail Operator 則可能保持 compositional

低頻能力若每個都建立 macro：

$$
N_G
$$

會爆炸。

所以長尾更適合：

$$
\boxed{
\text{compose from shared primitives}.
}
$$

這形成一個很重要的候選設計：

> **高頻功能結晶、低頻功能組合。**

---

# 45. Frequency-Adaptive Vocabulary Hypothesis

設：

$$
f(O)
$$

是 operator 使用頻率。

可能存在 threshold：

$$
f^*.
$$

若：

$$
f(O)>f^*,
$$

允許 macro crystallization。

若：

$$
f(O)<f^*,
$$

優先保留 compositional derivation。

---

# 46. 這可能控制 Nmax

如果所有長尾都不直接加入 stable vocabulary，

而只在需求出現時動態 composition，

則：

$$
N_G
$$

可以被壓制。

這是一種：

$$
\boxed{
\text{Vocabulary Pressure Regulation}.
}
$$

---

# 47. Synonym Merge

如果：

$$
Behavior(O_i)\approx Behavior(O_j)
$$

且差異不具重要價值，

可：

$$
\boxed{
Merge(O_i,O_j)\rightarrow O_k.
}
$$

這降低：

- $N$ ；
- collision；
- maintenance。

---

# 48. ToolLibGen 類研究的啟示

近期 tool-library 研究也開始自動把大量 task-specific tools 重構成較少的 aggregated tools，以改善 retrieval scalability。

這支持：

$$
\boxed{
\text{tool aggregation}
}
$$

可能是 operator library 的自然演化機制。

---

# 49. 但過度 Merge 會造成巨型 Operator

如果：

$$
O_k
$$

合併太多功能，

它可能變成：

$$
\boxed{
\text{God Operator}.
}
$$

也就是：

- schema 複雜；
- semantic contract 太寬；
- selection 簡單但 internal routing 複雜。

---

# 50. God Operator 只是把 N 藏起來

表面：

$$
N\downarrow.
$$

但 operator 內部：

$$
Complexity(O_k)\uparrow.
$$

所以：

$$
\boxed{
\text{Operator Count Compression}
\neq
\text{Complexity Compression}.
}
$$

---

# 51. Effective Vocabulary Size

因此可以定義：

$$
\boxed{
N_{eff}
=
\sum_i
ComplexityWeight(O_i).
}
$$

而不是單純：

$$
N.
$$

一個 God Operator 可能等價於幾十個普通 operators。

---

# 52. Semantic Surface Area

對 operator：

$$
O_i
$$

定義：

$$
S_i
$$

為它需要區分的：

- modes；
- parameters；
- exceptions；
- branches。

總語言表面：

$$
\boxed{
S_{\mathcal O}
=
\sum_i S_i.
}
$$

有時：

$$
N\downarrow
$$

但：

$$
S_{\mathcal O}\uparrow.
$$

---

# 53. 所以真正上界是 Complexity Budget

比：

$$
N_{\max}
$$

更一般的是：

$$
\boxed{
C_{\max}^{language}.
}
$$

即系統能維持的總有效語言複雜度。

---

# 54. Language Complexity Budget

可以寫：

$$
\boxed{
C_{lang}
=
\alpha N_A
+
\beta H_{sel}
+
\gamma \rho_{col}
+
\delta C_{ctx}
+
\eta C_{version}
+
\theta S_{\mathcal O}.
}
$$

要求：

$$
C_{lang}\le B_{lang}.
$$

---

# 55. 版本治理成本

若 operator：

$$
O_i
$$

有：

$$
v_1,v_2,\ldots,
$$

每次升版會增加：

- compatibility；
- migration；
- retrieval ambiguity；
- old artifact interpretation。

所以：

$$
C_{version}
$$

可能隨：

$$
N_G
$$

快速增加。

---

# 56. Version Multiplicity

定義：

$$
V_i
=
N_{\text{live versions}}(O_i).
$$

總版本負擔：

$$
\boxed{
B_V
=
\sum_i V_i.
}
$$

比單純 operator count 更能反映維護成本。

---

# 57. 同名不同版的 collision

如果：

$$
O@v1
$$

與：

$$
O@v3
$$

行為不同，

卻都以：

$$
O
$$

出現在 legacy artifact 中，

就會產生：

$$
\boxed{
\text{Temporal Semantic Collision}.
}
$$

---

# 58. Namespace 也有成本

大量 namespace 可以降低局部 collision。

但 hierarchy 太深：

```text
system.agent.memory.semantic.update.v3
```

也增加：

- address cost；
- learning cost；
- migration cost。

因此 namespace depth 也有 optimum。

---

# 59. 最大有效不是固定常數

因此：

$$
\boxed{
N_{\max}^{effective}
=
f(
A,
\Omega,
G,
Retriever,
Context,
Hierarchy,
Versioning,
Risk
).
}
$$

它不可能是：

> 所有 AI 永遠最多 500 個。

---

# 60. Agent 能力提升會推高 Nmax

若 future AI：

- retrieval 更強；
- context 更大；
- semantic discrimination 更好；
- memory 更穩；

則：

$$
N_{\max}^{effective}(t)
$$

可能上升。

---

# 61. 但 operator sophistication 也會推低 count

如果未來一個 operator 能穩定承載更大的 semantic contract，

需要的 operator 數可能下降。

所以：

$$
N_{\max}(t)
$$

不是單調上升。

---

# 62. Global Nmax 甚至可能消失

如果：

- global library externalized；
- retrieval 幾乎完美；
- active set 始終 bounded；

那麼：

$$
N_G
$$

可能沒有明顯 cognitive upper bound。

真正固定的是：

$$
\boxed{
N_A^{max}.
}
$$

這是本文最重要的修正之一。

---

# 63. Active Working-Set Hypothesis

提出：

> **大型複合算子語言的實用上界主要由 active working set 決定，而不是 global library cardinality。**

形式：

$$
\boxed{
Performance
\approx
f(N_A,H_{sel},\rho_{col})
}
$$

而對：

$$
N_G
$$

只間接依賴 retrieval quality。

---

# 64. Selection-Entropy Threshold

可能存在：

$$
H_{sel}^{max}
$$

使：

$$
H_{sel}>H_{sel}^{max}
$$

後：

- wrong-tool；
- wrong-operator；
- clarification；
- latency；

顯著上升。

這可作為：

$$
N_A^{max}
$$

的候選定義方式之一。

---

# 65. Tool Overuse 也屬於複雜度

2025 年 SMART 研究顯示，透過讓 Agent 更策略性地使用工具，可以在減少 24% tool use 的同時提高超過 37% 的 performance。

這說明：

$$
\boxed{
\text{More available tools}
\neq
\text{more tool calls should be used}.
}
$$

因此 COL 需要同時控制：

- vocabulary size；
- active set；
- actual invocation rate。

---

# 66. Invocation Complexity

定義：

$$
C_{invoke}
=
N_{\text{calls}}
+
\lambda N_{\text{redundant calls}}.
$$

即使 operator library 設計很好，

Agent 若過度使用，

仍會降低 Language Action Yield。

---

# 67. 三種不同的「過多」

因此要區分：

### Too Many Defined

$$
N_G
$$

過大、治理困難。

### Too Many Active

$$
N_A
$$

過大、選擇困難。

### Too Many Invoked

$$
N_{call}
$$

過大、執行低效。

這三者不能混在一起。

---

# 68. 最大有效 operator set 的更完整定義

因此更合理地：

$$
\boxed{
N_{\max}^{effective}
=
\max N_G
}
$$

subject to：

$$
N_A(q)\le B_A,
$$

$$
H_{sel}(q)\le B_H,
$$

$$
\rho_{col}\le B_C,
$$

$$
C_{lang}\le B_L,
$$

$$
Y_L\ge\tau_Y.
$$

這表示：

> global library 只要能被 runtime 控制，就可以很大。

---

# 69. 如果沒有 Retrieval Layer

若：

$$
N_A=N_G,
$$

則：

$$
N_{\max}^{effective}
$$

通常會顯著下降。

所以 retrieval architecture 本身決定 language scale。

---

# 70. Static Flat-Language Upper Bound

對平坦、全部常駐的語言：

$$
\boxed{
N_{\max}^{flat}
}
$$

可能相對小。

---

# 71. Hierarchical-Retrieval Upper Bound

對 hierarchy + retrieval：

$$
\boxed{
N_{\max}^{hier}
\gg
N_{\max}^{flat}
}
$$

是合理候選猜想。

但需實驗驗證。

---

# 72. Max Effective Set 的第一批命題

## MX-P1 — Non-Monotonic Vocabulary Utility

$$
J(N)
$$

對 $N$ 不單調。

---

## MX-P2 — Active-Set Bottleneck

主要認知上限由：

$$
N_A
$$

而非：

$$
N_G
$$

決定。

---

## MX-P3 — Collision-Limited Selection

高：

$$
\rho_{col}
$$

會降低 tool / operator selection fidelity。

---

## MX-P4 — Hierarchical Buffering

hierarchy / retrieval 能讓：

$$
N_G
$$

增長而：

$$
N_A
$$

保持 bounded。

---

## MX-P5 — High-Frequency Crystallization

高頻複合程序適合 macro crystallization。

---

## MX-P6 — Long-Tail Composition

低頻能力更適合由共享 primitives 動態組合，而不是各自常駐 operator。

---

## MX-P7 — God-Operator Conservation

過度 merge 不會真正消除 complexity，只會從 vocabulary size 移到 internal semantic surface。

---

## MX-P8 — Version-Burden Upper Bound

live versions 過多會降低 effective language capacity。

---

## MX-P9 — Retrieval-Conditioned Nmax

$$
N_{\max}
$$

必須條件化 retriever quality。

---

## MX-P10 — Dynamic Upper Bound

隨 Agent、context、retrieval 與 operator ecology 演化：

$$
N_{\max}^{effective}(t)
$$

會動態漂移。

---

# 73. 如何實際估計 Nmax？

固定：

- Agent；
- domain；
- tool/operator definitions；
- workload；
- retriever。

逐步增加：

$$
N=10,20,50,100,200,\ldots
$$

量：

- retrieval recall；
- selection accuracy；
- semantic fidelity；
- latency；
- token/context；
- action yield；
- collision；
- tool calls。

---

# 74. Distractor Injection Test

最乾淨的方法之一：

保持真正需要的 operator 不變。

逐步加入：

### Type A
完全不相關 distractors。

### Type B
語義相近 distractors。

### Type C
功能重疊 aliases。

### Type D
版本衝突 operators。

觀察：

$$
Performance(N).
$$

---

# 75. 不同 distractor 會測不同上界

完全不相關：

測 context / scale。

語義相近：

測 selection discrimination。

alias：

測 synonym redundancy。

版本衝突：

測 governance / temporal semantics。

---

# 76. Active-Set Sweep

固定 global：

$$
N_G=10,000.
$$

改變 retriever top-k：

$$
N_A
=
5,10,20,50,100.
$$

找：

$$
\boxed{
N_A^*.
}
$$

這可能比直接找 global Nmax 更有實際價值。

---

# 77. Collision Sweep

固定：

$$
N_A.
$$

逐步提高：

$$
\rho_{col}.
$$

找：

$$
\boxed{
\rho_{col}^{critical}.
}
$$

這能測語言在「同義／近義 operator」下的抗干擾程度。

---

# 78. Hierarchy Sweep

比較：

### Flat
100 operators 一層。

### 2-Level
10 domains × 10 operators。

### 3-Level
5 × 5 × 4。

比較：

- routing；
- latency；
- final selection；
- error localization。

---

# 79. Macro-Merge Sweep

從多個相近 operator：

$$
O_1,\ldots,O_k
$$

逐步 merge。

觀察：

- $N$ 下降；
- schema complexity 上升；
- selection 改善；
- execution parameter error 是否上升。

找到 merge optimum。

---

# 80. 最終不是一條 Nmax 曲線

完整結果應是：

$$
\boxed{
\mathcal F
=
Pareto(
N_G,
N_A,
H_{sel},
\rho_{col},
C_{ctx},
Y_L,
F_{sem}
).
}
$$

而不是：

> 最大就是 317 個。

---

# 81. 與 LRC–COL-03 的合併

上一篇得到：

$$
N_{\min}^{effective}.
$$

本篇得到：

$$
N_{\max}^{effective}.
$$

因此：

$$
\boxed{
I_{\mathcal O}^{effective}
=
[
N_{\min}^{effective},
N_{\max}^{effective}
].
}
$$

這就是最初命題空間中所說的：

> 靜態有效語言區間。

---

# 82. 但目前仍是靜態切片

本篇假設：

- Agent 固定；
- workload 固定；
- version 固定；
- retriever 固定。

所以只是：

$$
I_{\mathcal O}^{S}.
$$

真正：

$$
I_{\mathcal O}^{D}(t)
$$

留給 LRC–COL-06。

---

# 83. 本篇核心公式組

全域與活躍：

$$
\boxed{
N_C
\le
N_A
\le
N_R
\le
N_G.
}
$$

選擇熵：

$$
\boxed{
H_{sel}
=
-\sum_i p_i\log p_i.
}
$$

碰撞密度：

$$
\boxed{
\rho_{col}
=
\frac{2|E|}{N(N-1)}.
}
$$

邊際 operator 效用：

$$
\boxed{
\Delta J(O\mid\mathcal O)
=
G_C+G_D+G_Y+G_R
-
C_S-C_X-C_V-C_D.
}
$$

有效範圍：

$$
\boxed{
N_{\min}^{effective}
\le
N^*
\le
N_{\max}^{effective}.
}
$$

---

# 84. 非主張

本文不主張：

1. 存在跨所有 Agent 的固定 $N_{\max}$ ；
2. tool 數量本身能完整代表 operator language complexity；
3. 大型 tool benchmark 的低成功率完全由 toolset size 造成；
4. hierarchy 永遠優於 flat namespace；
5. retrieval 可以消除所有大型 vocabulary 問題；
6. 所有低頻 operator 都應刪除；
7. 所有高頻 workflow 都應結晶成 macro；
8. merge 越多越好；
9. context window 是唯一上限；
10. $N_G$ 永遠可以無限增長。

本文只提出：

$$
\boxed{
\text{The upper bound of an executable operator language is governed less by raw storage cardinality than by active selection width, semantic interference, retrieval quality, context cost, and governance complexity.}
}
$$

---

# 85. 文獻錨點

1. **ToolScope: Enhancing LLM Agent Tool Use through Tool Merging and Context-Aware Filtering（ACL 2026）**  
   指出大型 toolsets 中的 redundancy、overlapping names/descriptions、ambiguity 與 input-context limits；透過 tool merging 與 context-aware filtering，在三個模型、三個 benchmark 上提高 8.38%–38.6% 的 tool-selection accuracy。這直接支援本文「Global Library 與 Active Working Set 應分離」的研究方向。

2. **Live API-Bench: 2500+ Live APIs for Testing Multi-Step Tool Calling（EACL 2026）**  
   建立超過 2,500 個 live API 的真實工具調用 benchmark；受測 LLM 的 task-completion 仍偏低，顯示「大量可用 API」並不等同「大型工具集合已被有效掌握」。

3. **Tool Preferences in Agentic LLMs are Unreliable（EMNLP 2025）**  
   顯示工具文字描述的表述可以大幅改變工具選擇行為，說明 operator 之間的語義競爭與 wording sensitivity 是 selection complexity 的真實因素。

4. **Frequency & Compositionality in Emergent Communication（EMNLP 2025）**  
   顯示 compositionality 與 exposure / frequency 結構互動，不是單純由 frequency 單調決定。這提供「高頻結晶、低頻組合」命題的外部研究背景，但本文不宣稱該規律已被直接證明於 LLM operator languages。

5. **SMART: Self-Aware Agent for Tool Overuse Mitigation（ACL Findings 2025）**  
   顯示降低不必要工具使用可以同時提高效率與任務表現，支持「operator availability、active selection 與 actual invocation」必須分開評估。

6. **Toolshed / large-scale tool retrieval research（2024–2025）**  
   大型工具系統已開始透過 tool knowledge base、retrieval、top-k selection 等機制避免將全部工具直接送入 Agent context，與本文的分層 operator-runtime 架構同構。

---

# 86. 下一篇

## LRC–COL-05：基底大小—組合深度—表達能力交換律
### The Tradeoff Law of Basis Size, Composition Depth, and Expressive Capacity

下一篇將把前兩篇的：

$$
N_{\min}^{effective}
$$

與：

$$
N_{\max}^{effective}
$$

中間真正的核心函數拉出來：

$$
\boxed{
N
\leftrightarrow
d
\leftrightarrow
Expressivity
\leftrightarrow
Fidelity
\leftrightarrow
LearningCost.
}
$$

我們將研究：

- 為什麼更小 basis 會需要更深 composition；
- 更深 composition 何時造成 semantic drift / execution error；
- macro operator 如何用 vocabulary 換 depth；
- 是否存在類似「最短程式 vs 最小指令集」的 Pareto frontier；
- 最佳點 $(N^*,d^*)$ 是否可以由 workload distribution 推導；
- operator granularity $g^*$ 如何進入交換律。

**END — LRC–COL-04 v0.1**
