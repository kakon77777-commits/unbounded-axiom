# FDRS / FCSR Classical Cube Foundations IV
## 從狀態圖到搜尋：BFS、雙向搜尋、A* 與 IDA* 的統一語義

**英文題名：** From State Graphs to Search: A Unified Semantics for BFS, Bidirectional Search, A*, and IDA*  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-04  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第四篇

---

## 摘要

前三篇已分別建立 FCSR 的表示語義、標準 $3\times3\times3$ 魔方的合法狀態空間，以及 Facelet、Cubie、Permutation 與 Coordinate representation 的區別。本文進入真正的搜尋層：不再問「狀態如何表示」，而問「在給定表示與 move semantics 下，計算機如何系統性地尋找一條從起始狀態到目標狀態的路徑」。

本文提出一個統一的 Search Problem Contract：

$$
\mathcal{Q}
=
(X,A,T,G,c,h),
$$

其中 $X$ 為搜尋節點空間， $A$ 為可用操作集合， $T$ 為轉移函數， $G$ 為目標判定， $c$ 為邊成本， $h$ 為可選 heuristic。重要的是， $X$ 不必等於完整 canonical state space；它可以是 full cubie state、完整 coordinate tuple、phase coordinate space、quotient graph 或其他對當前任務 sufficient 的表示。

在此統一語義下，本文比較 Breadth-First Search、Bidirectional Search、A* 與 IDA*。BFS 在單位邊成本下可找到最短步數解，但 frontier 與 visited set 通常造成指數級記憶體需求。雙向搜尋同時從起點與目標端擴張；在規則、可逆、近似均衡的搜尋樹中，其理想節點量可由約 $b^d$ 降為約 $2b^{d/2}$，但一般圖上的交會偵測、終止條件與兩側成本一致性不能被忽略。A* 以

$$
f(n)=g(n)+h(n)
$$

排序 frontier；若 heuristic 為 admissible，並在 graph-search 情況下正確處理重開或採用 consistency 等足夠條件，可保持最短路徑保證。IDA* 則以逐輪增加的 $f$ -threshold 執行 depth-first search，把 A* 的 heuristic 邊界與 depth-first 的低記憶體特性結合起來。

本文特別將 2026 年既有 FDRS 魔方網頁 Demo 重新定位：其 permutation engine、粗略 piece-count lower bound 與 IDA* 已構成 search proof-of-concept，但 node cap、有限 scramble depth 與 demo-oriented fallback 使它不應被視為全域 completeness 或 optimality 證明。新版 Search Kernel 將拆除這些語義混淆，把「搜尋器是否找得到解」、「找到的解是否最短」、「因資源上限中止」與「heuristic 是否可證 admissible」分開報告。

本文最後提出 Search Trace 作為新版可視化的第一級資料：frontier size、expanded nodes、generated nodes、duplicate hits、threshold、 $g/h/f$ 、pruned branches、meeting state 與 solution certificate 都應可被同步觀察。如此 FCSR 從「看魔方如何展平」進一步升級為「看計算機如何在狀態空間中移動」。

**關鍵詞：** BFS、bidirectional search、A*、IDA*、state graph、heuristic search、frontier、optimality、FCSR、FDRS、search visualization

---

## 1. 從表示問題進入搜尋問題

前三篇形成：

$$
\text{Canonical State}
\rightarrow
\text{Legal State}
\rightarrow
\text{Representation}.
$$

但 representation 本身不會自動產生解。

令起始狀態為：

$$
s_0,
$$

目標狀態為：

$$
s_\star.
$$

solver 的核心任務仍然是找一條 move sequence：

$$
p=(a_1,\ldots,a_k)
$$

使：

$$
T^\ast(s_0,p)=s_\star.
$$

若追求最短解，還需最小化：

$$
C(p)
=
\sum_{i=1}^{k}c(a_i).
$$

因此求解本質上是一個最短路徑／狀態空間搜尋問題。

---

## 2. Search Problem Contract

定義：

$$
\mathcal{Q}
=
(X,A,T,G,c,h),
$$

其中：

- $X$：搜尋器實際操作的節點空間；
- $A(x)$：狀態 $x$ 可採取的動作；
- $T(x,a)$：轉移函數；
- $G(x)$：goal predicate；
- $c(x,a,x')\geq0$：轉移成本；
- $h(x)\geq0$：可選 heuristic。

對經典 HTM 魔方，可令每個合法 face move 成本：

$$
c=1.
$$

若搜尋完整 canonical state：

$$
X
=
\mathcal{S}_{\mathrm{legal}}.
$$

若搜尋 phase coordinate：

$$
X
=
\mathcal{X}_{\mathrm{phase}}.
$$

這直接承接第三篇的核心要求：

> 談搜尋演算法之前，必須先說明搜尋器到底在哪個 representation / quotient graph 上運作。

---

## 3. State graph 與 search tree 必須區分

Search problem 誘導一張有向圖：

$$
\Gamma_{\mathcal{Q}}
=
(V,E),
$$

其中：

$$
V=X,
$$

且：

$$
(x,x')\in E
$$

若存在：

$$
a\in A(x)
$$

使：

$$
T(x,a)=x'.
$$

但實際搜尋過程通常形成一棵或多棵 search tree。

同一個 graph state 可以透過不同 move sequences 重複到達，因此：

$$
\text{search node}
\neq
\text{unique state}.
$$

這個區別非常重要。

如果完全不做 duplicate detection，搜尋器可能反覆探索：

$$
x
\rightarrow
y
\rightarrow
x
\rightarrow
y
\rightarrow
\cdots
$$

魔方尤其如此，因為每個 move 都可逆。

因此應區分：

$$
\text{Tree Search}
$$

與：

$$
\text{Graph Search}.
$$

---

## 4. Branching factor 不是固定的「18」

若 move alphabet 使用：

$$
\mathcal{A}_{18}
$$

則 root 最多有 $18$ 個直接 successors。

但實際 branching factor 取決於 pruning policy。

例如連續在同一 face 上操作：

$$
R,R
$$

可以合併為：

$$
R^2,
$$

而：

$$
R,R'
$$

直接抵消。

所以搜尋器常禁止：

$$
\text{same-face immediate repetition}.
$$

對互相可交換的 opposite faces，還可建立 canonical ordering 以移除重複序列。

因此我們定義：

$$
b_{\mathrm{raw}}
=
|A|,
$$

以及：

$$
b_{\mathrm{eff}}
=
\text{search policy 下的平均有效分支數}.
$$

後續所有複雜度估計如果使用：

$$
b,
$$

都必須說明它是理想模型、raw branching 或 empirical effective branching。

---

## 5. Breadth-First Search

BFS 在單位邊成本圖中按照深度逐層擴張：

$$
L_0,L_1,L_2,\ldots
$$

其中：

$$
L_d
=
\{x:d(s_0,x)=d\}.
$$

在標準 graph-search 版本中，BFS 維護：

- FIFO frontier；
- visited set；
- parent / move metadata。

若所有 move cost 為 $1$，第一次依 BFS 層序確定 goal 時即可得到最短 move-count solution。

所以在有限、unit-cost reachable graph 與正確 duplicate handling 下：

$$
\boxed{
\text{BFS is complete and optimal}.
}
$$

---

## 6. BFS 的根本瓶頸是 frontier memory

對近似均勻、branching factor 為 $b$ 、最短解深度為 $d$ 的 tree model，節點量級為：

$$
1+b+b^2+\cdots+b^d
=
O(b^d).
$$

BFS 不只需要生成這些節點，還必須保存大量 frontier / visited information。

因此其空間成本同樣可達：

$$
O(b^d).
$$

這對魔方這種高 branching、解深可達數十步的問題非常不利。

所以：

$$
\text{BFS optimality}
$$

並不等於：

$$
\text{BFS practicality}.
$$

---

## 7. Bidirectional Search

若 move 是可逆的，則可以同時搜尋：

$$
s_0
\rightarrow
\cdots
$$

與：

$$
s_\star
\rightarrow
\cdots
$$

並尋找：

$$
F_{\mathrm{forward}}
\cap
F_{\mathrm{backward}}
\neq
\varnothing.
$$

若交會於狀態 $m$，可將：

$$
s_0
\rightsquigarrow
m
$$

與：

$$
m
\rightsquigarrow
s_\star
$$

拼接成完整解。

對均勻樹的理想模型，單向 BFS 約探索：

$$
O(b^d),
$$

而兩側各探索至約：

$$
d/2
$$

時，總量可近似：

$$
O(2b^{d/2}).
$$

這是 bidirectional search 最直觀的平方根深度效應。

---

## 8. 雙向搜尋不是「兩個 BFS 就一定更好」

實際圖搜尋還存在幾個問題：

### 8.1 Meeting test

必須有效判斷：

$$
x\in V_f\cap V_b.
$$

### 8.2 Frontier imbalance

若一側分支明顯更大，固定交替擴張可能浪費工作。

### 8.3 Goal representation

若 goal 是一個 subgroup 或 equivalence class，backward side 不是單一節點。

### 8.4 Weighted edges

若成本不全為 $1$，第一次 frontier 相遇不一定保證全域最短。

### 8.5 Memory

雙向 BFS 仍然需要保存兩側 visited/frontier。

所以：

$$
\boxed{
\text{bidirectional}
\neq
\text{memory-free}.
}
$$

---

## 9. A*：把 domain knowledge 放進搜尋順序

A* 對 node $n$ 定義：

$$
f(n)
=
g(n)+h(n),
$$

其中：

$$
g(n)
=
\text{起點到 }n\text{ 的已知成本},
$$

$$
h(n)
=
\text{從 }n\text{ 到 goal 的估計成本}.
$$

A* 每次優先擴張 frontier 中最小 $f$ 的節點。

若：

$$
h(n)=0,
$$

A* 退化為 uniform-cost search；在 unit-cost 情況下即回到按最短已知深度擴張的搜尋。

---

## 10. Admissibility 與 consistency

heuristic 稱為 admissible，若：

$$
0
\leq
h(n)
\leq
h^\ast(n),
$$

其中：

$$
h^\ast(n)
=
d(n,G)
$$

是真實剩餘最短成本。

也就是：

$$
h
$$

永遠不能高估剩餘距離。

對 graph search，若 heuristic 進一步滿足 consistency：

$$
h(n)
\leq
c(n,n')+h(n'),
$$

則 $f$ 沿路徑具有單調性，closed-node handling 可以更簡潔。

若 heuristic admissible 但 inconsistent，仍可透過允許更佳 $g$ 值觸發 reopen 等正確機制維持 optimality。

因此不能把：

$$
\text{admissible heuristic}
$$

單獨等同於：

$$
\text{任意 A* 程式必然 optimal}.
$$

---

## 11. A* 的時間－空間張力

A* 的優勢是：

$$
h
$$

能把搜尋集中到較有希望的區域。

但 best-first search 需要保存 frontier，通常還要保存 closed set 與 $g$ 資訊。

對大型隱式狀態空間，實際限制常常不是單次 move 計算，而是 frontier memory。

因此：

$$
\boxed{
\text{A* solves ordering well, but may lose on memory}.
}
$$

這導向 IDA*。

---

## 12. IDA*：把 A* 的 $f$ 邊界放進 depth-first search

IDA* 同樣使用：

$$
f(n)
=
g(n)+h(n).
$$

但不維護全域 priority queue。

它選擇 threshold：

$$
\theta,
$$

進行 depth-first search，只展開：

$$
f(n)
\leq
\theta
$$

的節點。

若未找到 goal，下一輪把 threshold 提升到上一輪所有超界值中的最小值：

$$
\theta'
=
\min\{f(n):f(n)>\theta\}.
$$

因此形成：

$$
\theta_0
<
\theta_1
<
\theta_2
<
\cdots.
$$

---

## 13. IDA* 的核心交換：重算換記憶體

A* 傾向：

$$
\text{expand once}
+
\text{store many}.
$$

IDA* 傾向：

$$
\text{re-expand across iterations}
+
\text{store one DFS path}.
$$

若最大搜尋深度為 $d$，純 DFS recursion stack 為：

$$
O(d).
$$

因此在狀態空間巨大、解深相對有限的 puzzle 中，IDA* 常比保存整個 best-first frontier 更可行。

Korf 1985 的 iterative-deepening 工作正是這種 time / space / solution-cost tradeoff 的經典基線。

---

## 14. IDA* 的 optimality 與 pruning safety

在 nonnegative edge cost 且 heuristic admissible 的標準設定中，IDA* 以：

$$
f=g+h
$$

threshold 遞增。

若：

$$
g(n)+h(n)>\theta,
$$

因：

$$
h(n)\leq h^\ast(n),
$$

可得所有經過 $n$ 的 goal path 成本至少為：

$$
g(n)+h^\ast(n)
\geq
g(n)+h(n)
>
\theta.
$$

因此該 subtree 不可能包含總成本不超過 $\theta$ 的解，可以安全剪枝。

這就是 IDA* 最值得形式驗證的核心命題之一。

---

## 15. IDA* 不自動等於「快」

若：

$$
h(n)=0,
$$

IDA* 接近普通 iterative deepening。

若：

$$
h(n)
$$

接近：

$$
h^\ast(n),
$$

大量 subtrees 可以在淺層被剪掉。

所以性能真正取決於：

$$
\text{representation}
+
\text{heuristic}
+
\text{move pruning}
+
\text{node ordering}
+
\text{duplicate handling}.
$$

這延續第三篇：

$$
P
=
F(R,H,A,\text{precomputation},\text{hardware}).
$$

---

## 16. 原始 FDRS Demo 的 IDA* 重新定位

既有 HTML Demo 已包含：

- permutation-based state engine；
- $18$ 個 move variants；
- piece-based heuristic；
- IDA*；
- node cap；
- scramble / solve FSM。

其 heuristic 可概括為：

$$
h_c(s)
=
\left\lceil
\frac{N_c^{\mathrm{wrong}}}{4}
\right\rceil,
$$

$$
h_e(s)
=
\left\lceil
\frac{N_e^{\mathrm{wrong}}}{4}
\right\rceil,
$$

再取：

$$
h(s)
=
\max(h_c(s),h_e(s)).
$$

直覺是：一個 face move最多直接改變四個 corners 與四個 edges，因此若仍有 $k$ 個完全未歸位 pieces，至少需要約：

$$
\left\lceil k/4\right\rceil
$$

次 move 才可能全部修正。

這是一個非常粗的 lower bound，但適合作為 Demo heuristic。

---

## 17. Demo heuristic 的可證明性要求

若要把上述 heuristic 升級成正式 solver component，需證：

$$
h(s)
\leq
h^\ast(s).
$$

對：

$$
h_c
$$

需要證明任意單步 face move 最多能使四個原本 incorrect corners 變為 correct。

對：

$$
h_e
$$

同理。

若：

$$
h_c
\leq
h^\ast
$$

且：

$$
h_e
\leq
h^\ast,
$$

則：

$$
\max(h_c,h_e)
\leq
h^\ast.
$$

因此：

$$
h
$$

admissible。

這將成為第五篇可直接形式化的第一個簡單 heuristic theorem。

---

## 18. 為什麼舊 Demo 不能直接宣稱 complete

舊 Demo 設定：

$$
\text{NODE\_CAP}
=
2.2\times10^6.
$$

若節點數超過上限，search 會中止。

此外 solver 的最大 bound 受 scramble depth 附近的範圍限制，且 planning failure 時會 fallback reset。

因此程式層真正語義是：

$$
\boxed{
\text{bounded demonstration solver}.
}
$$

而不是：

$$
\forall s\in\mathcal{S}_{\mathrm{legal}},
\exists p:
\operatorname{Solve}(s)=p.
$$

---

## 19. Search status 與 solver correctness 必須分離

新版 API 至少應區分：

```text
Solved(path)
Exhausted
BoundExceeded
ResourceLimit
Cancelled
InvalidState
InternalError
```

### Solved

必須滿足：

$$
T^\ast(s_0,p)=s_\star.
$$

### Exhausted

只有當有限 search domain 已完整展開且無 goal，才能宣稱該 domain 中不存在解。

### BoundExceeded

只代表目前 cost / depth bound 內沒找到。

### ResourceLimit

只代表計算被 time / memory / node cap 中止。

因此：

$$
\boxed{
\text{not found}
\neq
\text{no solution}.
}
$$

---

## 20. 統一四種演算法的核心差異

在同一個：

$$
\mathcal{Q}
=
(X,A,T,G,c,h)
$$

下，四種算法主要差在 frontier policy 與記憶體策略。

### BFS

對 unit cost：

$$
\text{priority}(n)
=
g(n).
$$

### Bidirectional BFS

維護：

$$
F_f,F_b
$$

兩個 frontier，尋找 intersection。

### A*

$$
\text{priority}(n)
=
g(n)+h(n).
$$

### IDA*

不用全域 priority queue，而把：

$$
g+h
$$

變成 DFS threshold。

所以它們都是：

$$
\boxed{
\text{如何安排狀態空間探索順序與記憶體}
}
$$

的不同答案。

---

## 21. 搜尋算法的比較維度

本文不以單一秒數比較算法。

定義 search profile：

$$
\mathbf{P}
=
(N_{\mathrm{gen}},
N_{\mathrm{exp}},
N_{\mathrm{dup}},
M_{\mathrm{peak}},
D_{\mathrm{sol}},
C_{\mathrm{sol}},
T_{\mathrm{wall}}).
$$

其中：

- $N_{\mathrm{gen}}$：generated nodes；
- $N_{\mathrm{exp}}$：expanded nodes；
- $N_{\mathrm{dup}}$：duplicate hits；
- $M_{\mathrm{peak}}$：peak memory；
- $D_{\mathrm{sol}}$：solution depth；
- $C_{\mathrm{sol}}$：solution cost；
- $T_{\mathrm{wall}}$：wall-clock time。

若使用 heuristic，再增加：

$$
N_{\mathrm{prune}},
$$

以及 threshold history：

$$
(\theta_0,\theta_1,\ldots).
$$

---

## 22. Search Trace 應成為可視化第一級物件

新版 FCSR 不只畫最後 solution path。

SearchTrace 應保存事件：

```text
SearchStarted
NodeGenerated
NodeExpanded
DuplicateDetected
HeuristicEvaluated
NodePruned
ThresholdRaised
FrontiersMet
GoalFound
SearchStopped
```

每個事件可以帶：

```text
stateRef
representationRef
move
g
h
f
depth
parent
reason
step
```

這樣 UI 可以真正播放：

$$
\boxed{
\text{計算機如何找解}.
}
$$

---

## 23. 四種可視化模式

### 23.1 BFS Layer View

顯示：

$$
L_0,L_1,L_2,\ldots
$$

以及每層節點量。

### 23.2 Bidirectional Meeting View

顯示：

$$
F_f
$$

與：

$$
F_b
$$

如何逐漸接近並交會。

### 23.3 A* Frontier View

顯示 frontier 上：

$$
g,h,f
$$

分布，以及下一個被 pop 的節點。

### 23.4 IDA* Threshold View

顯示：

$$
\theta_0
\rightarrow
\theta_1
\rightarrow
\cdots
$$

以及每一輪被：

$$
f>\theta
$$

剪掉多少節點。

---

## 24. Search graph 也可以是 quotient graph

第三篇已指出 coordinate：

$$
R:
\mathcal{S}
\rightarrow
X
$$

可能不是 injective。

若 move-compatible：

$$
R(T(s,a))
=
M_a(R(s)),
$$

就可以直接在：

$$
X
$$

上建立 quotient search graph。

因此同一個 cube problem 可以有：

$$
\Gamma_{\mathrm{full}},
$$

$$
\Gamma_{\mathrm{coord}},
$$

$$
\Gamma_{\mathrm{sym}},
$$

$$
\Gamma_{\mathrm{phase}}.
$$

它們的節點數、branching、goal set 與 heuristic 可能完全不同。

所以：

$$
\boxed{
\text{搜尋算法不能脫離搜尋圖談性能}.
}
$$

---

## 25. FDRS 的新計算命題：表示改變搜尋拓樸

令：

$$
R:
\Gamma
\rightarrow
\Gamma_R.
$$

representation / quotient 可能改變：

- 節點 cardinality；
- 多狀態等價類；
- goal geometry；
- heuristic 可計算性；
- effective depth；
- duplicate structure；
- symmetry structure。

因此可以研究：

$$
C_{\mathrm{search}}(\Gamma_R,A)
$$

隨 representation $R$ 如何變化。

形成可測量命題：

$$
\boxed{
R_1,R_2
\Rightarrow
C_{\mathrm{search}}(R_1)
\neq
C_{\mathrm{search}}(R_2)
}
$$

在具體問題上是否成立，必須由實驗或定理驗證，而不能預設「降維必然加速」。

---

## 26. 演算法選擇不是固定答案

對小深度：

$$
\text{BFS}
$$

可能最簡單。

若 goal 唯一且轉移高度可逆：

$$
\text{bidirectional}
$$

可能有明顯優勢。

若有強 heuristic 且 memory 足夠：

$$
\text{A*}
$$

可能極有效。

若有強 admissible heuristic 但 frontier 太大：

$$
\text{IDA*}
$$

常更適合。

所以系統不應內建：

> IDA* 永遠最好。

真正的設計是：

$$
\operatorname{ChooseSearch}
(
R,
h,
M_{\max},
C_{\mathrm{goal}},
\text{optimality requirement}
).
$$

---

## 27. 形式驗證目標：Search Kernel

### S1. Path replay semantics

$$
\operatorname{applyPath}(s,[])
=
s.
$$

$$
\operatorname{applyPath}(s,a::p)
=
\operatorname{applyPath}(T(s,a),p).
$$

### S2. BFS depth correctness

對 unit-cost graph，在正確 visited semantics 下：

$$
\operatorname{BFS}(s)=p
\Rightarrow
|p|
=
d(s,G).
$$

### S3. Bidirectional path composition

若：

$$
p_f:s\rightsquigarrow m
$$

與：

$$
p_b:G\rightsquigarrow m,
$$

且 moves 可逆，則：

$$
p_f
\mathbin{+\!\!+}
\operatorname{reverseInverse}(p_b)
$$

為合法 solution path。

### S4. A* lower-bound theorem

若：

$$
h\leq h^\ast
$$

並滿足所採 graph-search correctness 條件，則確定的 goal path 為 optimal。

### S5. IDA* pruning safety

若：

$$
h\leq h^\ast
$$

且：

$$
g(n)+h(n)>\theta,
$$

則不存在總成本：

$$
\leq\theta
$$

且經過 $n$ 的 goal path。

---

## 28. 搜尋與證明應分層

即使未來某個高速 solver 沒有完整形式化，仍可以把：

$$
\text{Search}
$$

與：

$$
\text{Check}
$$

分開。

Searcher 回傳：

$$
p.
$$

Verified checker 只需計算：

$$
T^\ast(s_0,p)
$$

並確認：

$$
T^\ast(s_0,p)=s_\star.
$$

因此：

$$
\boxed{
\text{untrusted search}
+
\text{trusted certificate checker}
}
$$

可以先提供 soundness。

optimality certificate 則更困難，因為還需要證明不存在更短 path。

---

## 29. 本文核心命題

### 命題 S1：搜尋問題必須綁定搜尋表示

$$
\mathcal{Q}
=
(X,A,T,G,c,h).
$$

### 命題 S2：搜尋圖與搜尋樹不同

duplicate path 不等於新 state。

### 命題 S3：BFS 的主要代價是 frontier memory

最短性保證不代表在巨大狀態域上實用。

### 命題 S4：Bidirectional search 改變有效搜尋深度

但 meeting、termination 與 memory 仍需明確處理。

### 命題 S5：A* 的核心是 $g+h$ frontier ordering

$$
f=g+h.
$$

### 命題 S6：IDA* 用重複計算換取低記憶體

$$
\text{best-first bound}
+
\text{depth-first traversal}.
$$

### 命題 S7：Algorithm performance 不是 algorithm name 的函數

$$
P
=
F(
\text{representation},
\text{heuristic},
\text{search policy},
\text{precomputation},
\text{hardware}
).
$$

---

## 30. 結論

本文完成 FDRS/FCSR 經典魔方線從「表示」到「搜尋」的第一次正式跨越。

前三篇建立了：

$$
\text{合法狀態}
+
\text{表示}
+
\text{coordinate reduction}.
$$

本文進一步建立：

$$
\boxed{
\text{Search Problem}
=
(X,A,T,G,c,h).
}
$$

BFS、雙向搜尋、A* 與 IDA* 不再被看成四個孤立技巧，而被理解為：

$$
\boxed{
\text{同一狀態空間探索問題的不同 frontier / memory policies}.
}
$$

從這一篇開始，任何求解效率宣稱都必須至少附帶：

$$
\text{representation},
\quad
\text{move set},
\quad
\text{metric},
\quad
\text{heuristic},
\quad
\text{duplicate policy},
\quad
\text{resource bound}.
$$

下一篇將專門處理其中最關鍵、也最能改變搜尋規模的一項：

**《啟發式與剪枝：Admissibility、Pattern Database 與搜尋下界》**。

---

## 參考資料與來源定位

### 起源與既有實作

- [F2026-D] `FDRS_展開收斂_同步性.html`，FDRS/FCSR permutation engine、piece heuristic、IDA*、FSM 與同步可視化原型。

### 外部搜尋理論基線

- [R1] P. E. Hart, N. J. Nilsson, B. Raphael, **A Formal Basis for the Heuristic Determination of Minimum Cost Paths**, IEEE Transactions on Systems Science and Cybernetics, 1968。
- [R2] P. E. Hart, N. J. Nilsson, B. Raphael, **Correction to "A Formal Basis for the Heuristic Determination of Minimum-Cost Paths"**, SIGART Newsletter, 1972。
- [R3] Richard E. Korf, **Depth-First Iterative-Deepening: An Optimal Admissible Tree Search**, Artificial Intelligence 27(1), 1985。
- [R4] Ira Pohl, **Bi-Directional and Heuristic Search in Path Problems**, Stanford Linear Accelerator Center Technical Report / Dissertation, 1969。
- [R5] Richard E. Korf, **Finding Optimal Solutions to Rubik's Cube Using Pattern Databases**, AAAI, 1997。
- [R6] Richard E. Korf, Michael Reid, Stefan Edelkamp, **Time Complexity of Iterative-Deepening-A***, Artificial Intelligence 129, 2001。
- [R7] Herbert Kociemba, **The Two-Phase Algorithm** 與 **Pruning Tables**，官方技術說明。

---

## 版本註記

v0.1 建立統一 Search Problem Contract，將 BFS、Bidirectional、A*、IDA* 放入同一搜尋語義，並將既有 FDRS Demo 明確定位為 bounded proof-of-concept，而非全域 solver correctness 證明。

後續第五篇：

**《啟發式與剪枝：Admissibility、Pattern Database 與搜尋下界》**。
