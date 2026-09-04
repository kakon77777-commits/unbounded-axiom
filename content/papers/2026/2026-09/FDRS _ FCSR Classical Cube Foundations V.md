# FDRS / FCSR Classical Cube Foundations V
## 啟發式與剪枝：Admissibility、Pattern Database 與搜尋下界

**英文題名：** Heuristics and Pruning: Admissibility, Pattern Databases, and Search Lower Bounds  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-05  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第五篇

---

## 摘要

第四篇將 BFS、雙向搜尋、A* 與 IDA* 統一為對搜尋問題

$$
\mathcal Q=(X,A,T,G,c,h)
$$

採取不同 frontier 與 memory policy 的方法。本文進一步聚焦其中最能決定實際搜尋規模的部分：heuristic 與 pruning。

本文首先把 heuristic 從「經驗猜測」重新定義為**可證明的剩餘成本下界**。若真實最短剩餘成本為 $h^\ast(x)$，admissibility 要求

$$
0\leq h(x)\leq h^\ast(x).
$$

這個不等式不是裝飾性質，而是 A* / IDA* 能安全排除搜尋分支、同時保留最短解保證的核心。本文進一步區分 admissibility 與 consistency，並證明多個 admissible heuristics 的最大值仍為 admissible；相反，直接相加一般不保證 admissible，除非各抽象問題之間具有適當的 cost partition / additive abstraction 結構。

在此基礎上，本文把 Pattern Database（PDB）寫成一個抽象搜尋圖上的精確距離表。設抽象映射為

$$
\alpha:\mathcal S\rightarrow\mathcal A,
$$

若每個具體 move 在抽象圖中的成本不大於原 move 成本，則抽象最短距離

$$
d_{\mathcal A}(\alpha(s),\alpha(G))
$$

天然構成具體問題的 admissible lower bound。PDB 的本質因此不是「背答案」，而是**預先求解一個較小的抽象問題，並把精確抽象距離重用為完整問題的下界證書**。

本文亦重新檢查既有 FDRS 魔方 Demo 的 piece-count heuristic：

$$
h(s)
=
\max\left(
\left\lceil\frac{N_c^{\mathrm{wrong}}}{4}\right\rceil,
\left\lceil\frac{N_e^{\mathrm{wrong}}}{4}\right\rceil
\right).
$$

由於任一標準 face turn 僅改變四個 corners 與四個 edges，單步最多使四個 incorrect corners 或四個 incorrect edges 歸位，因此該 heuristic 不只可證 admissible，亦可證 consistent。這使原 Demo 中一個原本僅作工程直覺使用的 heuristic，可以被提升為正式 Search Kernel 的第一個 verified baseline。

本文最後建立四類 pruning：bound pruning、move-sequence pruning、duplicate / transposition pruning、symmetry / quotient pruning，並要求所有 pruning rule 都具有明確的 safety contract。新版 FCSR 可視化層將不再只顯示「節點被剪掉」，而會顯示下界來源、PDB lookup、支配關係與剪枝理由，使 heuristic search 的內部計算可以被直接觀察。

**關鍵詞：** heuristic、admissibility、consistency、Pattern Database、PDB、lower bound、pruning、IDA*、A*、cost partition、FCSR、FDRS

---

## 1. Heuristic 不是答案，而是下界

對搜尋狀態 $x$，令真實到目標集合的最短成本為：

$$
h^\ast(x)
=
d(x,G).
$$

heuristic：

$$
h:X\rightarrow\mathbb R_{\geq0}
$$

若滿足：

$$
0
\leq
h(x)
\leq
h^\ast(x)
$$

對所有 $x$ 成立，則稱為 admissible。

因此 admissible heuristic 的角色不是「猜答案有多遠」，而是聲明：

> 真實答案至少不會比這個數字更近。

也就是：

$$
\boxed{
h(x)
=
\text{certified lower bound}.
}
$$

這個定位對形式驗證尤其重要。

---

## 2. 為什麼 lower bound 可以安全剪枝

考慮 IDA* 的 threshold：

$$
\theta.
$$

目前節點 $n$ 的已花成本為：

$$
g(n).
$$

若：

$$
g(n)+h(n)>\theta,
$$

又因：

$$
h(n)\leq h^\ast(n),
$$

則：

$$
g(n)+h^\ast(n)
\geq
g(n)+h(n)
>
\theta.
$$

所以任何經過 $n$ 到達 goal 的路徑，總成本都必然：

$$
>\theta.
$$

因此該 subtree 可以安全排除。

這給出本文第一個核心 theorem schema：

$$
\boxed{
\text{Lower-bound proof}
\Rightarrow
\text{pruning safety}.
}
$$

---

## 3. Admissibility 與 consistency 不同

heuristic 稱為 consistent，若對任意合法 edge

$$
x\xrightarrow{a}y
$$

滿足：

$$
h(x)
\leq
c(x,a,y)+h(y),
$$

並要求 goal 上：

$$
h(g)=0.
$$

consistency 可以理解為 heuristic 自己也滿足一種 triangle inequality。

若所有 edge cost 非負，consistent heuristic 自動 admissible。

但 converse 一般不成立：

$$
\text{admissible}
\not\Rightarrow
\text{consistent}.
$$

這個差異對 graph-search A* 的 closed / reopen policy 很重要。

---

## 4. Zero heuristic、perfect heuristic 與 dominance

若：

$$
h_0(x)=0,
$$

則它永遠 admissible，但幾乎不提供方向。

若：

$$
h_{\mathrm{perfect}}(x)
=
h^\ast(x),
$$

則它是 perfect heuristic。

所以 heuristic design 可以被理解成：

$$
h_0
\preceq
h
\preceq
h^\ast.
$$

若兩個 admissible heuristics：

$$
h_1,h_2
$$

對所有 $x$ 滿足：

$$
h_1(x)\geq h_2(x),
$$

則稱 $h_1$ dominates $h_2$。

較大的 admissible lower bound 在 bound quality 上不會比較弱，但實際 wall-clock time 還取決於 heuristic evaluation cost 與 memory access cost。

---

## 5. 最大值組合定理

若：

$$
h_1,\ldots,h_k
$$

皆 admissible，定義：

$$
h_{\max}(x)
=
\max_i h_i(x).
$$

因每個：

$$
h_i(x)\leq h^\ast(x),
$$

所以：

$$
\max_i h_i(x)
\leq
h^\ast(x).
$$

因此：

$$
\boxed{
h_{\max}
\text{ 仍為 admissible}.
}
$$

同理，若每個 $h_i$ consistent，則 $h_{\max}$ 亦 consistent。

---

## 6. 為什麼不能隨便相加

若：

$$
h_1(x)
\leq
h^\ast(x)
$$

且：

$$
h_2(x)
\leq
h^\ast(x),
$$

並不能推出：

$$
h_1(x)+h_2(x)
\leq
h^\ast(x).
$$

因為兩個 heuristic 可能都在計算同一批真實 move 的成本。

因此：

$$
\boxed{
\text{admissible}
+
\text{admissible}
\not\Rightarrow
\text{admissible}.
}
$$

要安全相加，必須證明成本沒有被重複計算，或使用更一般的 cost partition。

---

## 7. 從 representation 到 search abstraction

第三篇已建立 task-reduced representation：

$$
R:
\mathcal S\rightarrow X.
$$

本文把其中一類特別提升為 search abstraction。

令具體搜尋圖為：

$$
\Gamma
=
(\mathcal S,E,c),
$$

抽象圖為：

$$
\Gamma_\alpha
=
(\mathcal A,E_\alpha,c_\alpha),
$$

以及抽象映射：

$$
\alpha:
\mathcal S
\rightarrow
\mathcal A.
$$

若每個具體 edge：

$$
s\xrightarrow{a}s'
$$

在抽象圖中都有對應 path 或 abstract edge：

$$
\alpha(s)
\rightsquigarrow
\alpha(s'),
$$

且其成本不大於原成本，則任何具體 solution path 都投影成一條不更昂貴的抽象 path。

因此：

$$
d_{\mathcal A}(\alpha(s),\alpha(G))
\leq
d_{\mathcal S}(s,G).
$$

這直接給出 admissible heuristic：

$$
\boxed{
h_\alpha(s)
=
d_{\mathcal A}(\alpha(s),\alpha(G)).
}
$$

---

## 8. 抽象下界定理

把上一節寫成正式命題。

若：

$$
\alpha:\mathcal S\rightarrow\mathcal A
$$

是 cost-nonincreasing abstraction，則：

$$
h_\alpha(s)
=
d_{\mathcal A}(\alpha(s),\alpha(G))
$$

滿足：

$$
h_\alpha(s)
\leq
h^\ast(s).
$$

證明概念如下。

取任意具體最短解：

$$
p^\ast:
s\rightsquigarrow G.
$$

將 $p^\ast$ 逐步投影到抽象圖，得到：

$$
\alpha(p^\ast):
\alpha(s)
\rightsquigarrow
\alpha(G).
$$

由 abstraction 不增加 edge cost：

$$
C_\alpha(\alpha(p^\ast))
\leq
C(p^\ast).
$$

又因抽象最短距離不大於任意抽象 path：

$$
d_{\mathcal A}(\alpha(s),\alpha(G))
\leq
C_\alpha(\alpha(p^\ast)).
$$

故：

$$
h_\alpha(s)
\leq
h^\ast(s).
$$

---

## 9. Pattern Database 的本質

Pattern Database 的核心流程是：

$$
\text{Concrete State}
\xrightarrow{\alpha}
\text{Abstract Pattern State}.
$$

先在較小的抽象 graph 上，對 abstract goal 反向計算所有可達 abstract states 的精確距離：

$$
\operatorname{PDB}[a]
=
d_{\mathcal A}(a,\alpha(G)).
$$

求解具體狀態 $s$ 時，只需：

$$
h_{\mathrm{PDB}}(s)
=
\operatorname{PDB}[\alpha(s)].
$$

由抽象下界定理：

$$
h_{\mathrm{PDB}}(s)
\leq
h^\ast(s).
$$

因此 PDB 是 admissible heuristic。

它不是預先儲存每一顆完整魔方的答案，而是儲存：

$$
\boxed{
\text{較小抽象問題的精確解距離}.
}
$$

---

## 10. PDB 的 offline / online 分工

Pattern Database 把成本拆成兩個時期。

### Offline

建立：

$$
\operatorname{PDB}.
$$

通常由 goal side 在 abstract graph 上執行 BFS、Dijkstra 或其他 exact distance computation。

### Online

對每個搜尋節點 $s$：

1. 計算：

$$
\alpha(s);
$$

2. 查表：

$$
\operatorname{PDB}[\alpha(s)].
$$

因此：

$$
\text{expensive once}
\rightarrow
\text{cheap many times}.
$$

對固定規則、固定目標、會反覆求解大量 scramble 的 twisty puzzle，這種 offline / online 分工尤其自然。

---

## 11. Korf 1997 的 Rubik's Cube PDB 意義

Richard Korf 1997 的工作把 Pattern Database heuristic 與 IDA* 用於 Rubik's Cube optimal solving，展示大型預計算抽象表如何加強 admissible heuristic。

對本系列來說，歷史重要性不在於複製當年的硬體或表大小，而是建立一條清楚的算法鏈：

$$
\boxed{
\text{abstraction}
\rightarrow
\text{exact abstract distance}
\rightarrow
\text{admissible heuristic}
\rightarrow
\text{IDA* pruning}.
}
$$

這條鏈把 representation engineering 與 search performance 直接接在一起。

---

## 12. Kociemba pruning table 與 PDB 的關係

Kociemba Two-Phase 實作使用 pruning tables。

其 index 可以由一個 coordinate，或兩到三個 coordinates 的組合產生；table 中保存的是到 phase goal / subgroup 的距離資訊，用於給出安全的搜尋下界與剪枝。

在概念上，它與 Pattern Database 有共同結構：

$$
\text{abstract / coordinate state}
\rightarrow
\text{precomputed lower bound}.
$$

但工程術語、壓縮方式與具體表語義可以不同，因此本文不強迫把所有 Kociemba pruning table 都改名為 PDB。

更合適的關係是：

$$
\boxed{
\text{PDB}
\text{ 與 }
\text{pruning table}
\text{ 都屬於 memory-based lower-bound heuristic family}.
}
$$

---

## 13. Symmetry 可以壓縮 heuristic table

第三篇已討論：

$$
X/\Sigma
$$

的 symmetry coordinate。

若：

$$
x\sim y
$$

代表兩個 coordinate states 在 puzzle symmetry 下等價，而 goal 與 move metric 對該 symmetry 保持相容，則它們的距離資訊可以共享。

因此可以把：

$$
\operatorname{PDB}[x]
$$

壓縮到 equivalence class：

$$
[x].
$$

這再次說明 symmetry reduction 不只是群論裝飾，而會直接影響 heuristic memory。

---

## 14. Disjoint Pattern Databases

假設問題可以分成多個 patterns：

$$
P_1,\ldots,P_k.
$$

各自建立：

$$
h_1,\ldots,h_k.
$$

最安全的通用組合是：

$$
h_{\max}
=
\max_i h_i.
$$

但若 patterns 與 operator costs 可以被適當分離，就可能使用：

$$
h_{\mathrm{add}}
=
\sum_i h_i.
$$

歷史上的 disjoint PDB 方法利用互不重疊的子目標 / 狀態變數與 operator 影響結構，使不同 PDB 的成本可以相加而不 double count。

---

## 15. 更一般的 cost partition

對每個具體 operator $o$，成本為：

$$
c(o).
$$

為第 $i$ 個 abstraction 分配成本：

$$
c_i(o)\geq0.
$$

若對所有 operator：

$$
\sum_i c_i(o)
\leq
c(o),
$$

則每個 abstraction 使用 $c_i$ 計算其 exact abstract distance：

$$
h_i.
$$

此時：

$$
\boxed{
\sum_i h_i(s)
\leq
h^\ast(s).
}
$$

因此 additive heuristic 仍 admissible。

這比簡單說「pattern 不重疊就一定能加」更一般，也更精確。

---

## 16. Move pruning 與 heuristic pruning 不同

heuristic pruning 依賴：

$$
g+h>\theta.
$$

move pruning 則在生成 successor 前，就根據 move sequence 結構排除冗餘操作。

例如：

$$
R,R'
$$

等價於不做任何事。

所以 optimal path 不需要包含這種立即抵消。

又例如在 HTM move alphabet 中：

$$
R,R
$$

可以直接改寫為：

$$
R^2.
$$

若 $R^2$ 計作一 move，則 $R,R$ 不是最短序列。

這類規則可以在不看 heuristic 的情況下直接排除。

---

## 17. Sequence dominance pruning

定義兩個 move sequences：

$$
p,q.
$$

若它們對任意 relevant state 具有相同作用：

$$
T^\ast(s,p)
=
T^\ast(s,q),
$$

但：

$$
C(q)<C(p),
$$

則 $q$ dominates $p$。

任何最優搜尋都不需要保留被支配的 $p$。

所以 move pruning 的正式安全條件可以寫成：

$$
\boxed{
\text{只排除具有不更差等價替代路徑的序列}.
}
$$

這比硬編「不准連續同面」更適合泛化到不同 twisty puzzle。

---

## 18. Commuting move canonicalization

若兩個 move：

$$
a,b
$$

滿足：

$$
ab=ba,
$$

則：

$$
a,b
$$

與：

$$
b,a
$$

導向同一 state。

為避免兩條完全等價 search branches，可以固定 canonical ordering。

但這種規則必須依 puzzle 與 move set 證明 commutativity，不能把某一顆魔方上的 rule 直接複製到任意 twisty puzzle。

---

## 19. Duplicate / transposition pruning

若兩條 path：

$$
p_1,p_2
$$

到達同一 state $x$，且：

$$
g(p_1)\leq g(p_2),
$$

則在標準 Markovian shortest-path 問題中，較昂貴的 $p_2$ 通常被 $p_1$ 支配。

這就是 transposition / duplicate pruning 的基本來源。

但 IDA* 使用低記憶體 DFS，是否保存完整 transposition table、只保存當輪資訊、還是只做 path-cycle detection，是時間－空間 tradeoff，而不是語義必然。

---

## 20. Pruning safety contract

所有 pruning rule $P$ 都應具備一個明確聲明：

$$
\operatorname{Safe}_P(\mathcal Q).
$$

對 optimal solver，可以定義：

$$
\operatorname{Safe}_P
\iff
\text{剪枝後仍至少保留一條 optimal solution path}.
$$

對只要求 completeness 的 solver，則可放寬為：

$$
\operatorname{CompleteSafe}_P
\iff
\text{若原問題有解，剪枝後仍至少保留一條 solution path}.
$$

如此：

- heuristic bound pruning；
- move dominance pruning；
- symmetry pruning；
- duplicate pruning；

都可以用同一種 proof vocabulary 管理。

---

## 21. 舊 Demo heuristic：從直覺提升為 theorem

原 HTML 的 heuristic：

$$
h_c(s)
=
\left\lceil
\frac{N_c(s)}{4}
\right\rceil,
$$

$$
h_e(s)
=
\left\lceil
\frac{N_e(s)}{4}
\right\rceil,
$$

$$
h(s)
=
\max(h_c(s),h_e(s)),
$$

其中 $N_c(s)$ 為不在 solved position / orientation 的 corners 數， $N_e(s)$ 為不在 solved position / orientation 的 edges 數。

任一標準 face turn 只作用於四個 corners 與四個 edges。

因此對一步：

$$
s\rightarrow s',
$$

有：

$$
N_c(s)-N_c(s')
\leq4,
$$

以及：

$$
N_e(s)-N_e(s')
\leq4.
$$

---

## 22. Demo corner / edge heuristic admissibility

若目前：

$$
N_c(s)=k,
$$

要讓所有 incorrect corners 歸位，每一步最多修正四個。

因此任何 solution 至少需要：

$$
\left\lceil\frac{k}{4}\right\rceil
$$

步。

所以：

$$
h_c(s)
\leq
h^\ast(s).
$$

同理：

$$
h_e(s)
\leq
h^\ast(s).
$$

由 max-combination theorem：

$$
h(s)
=
\max(h_c,h_e)
\leq
h^\ast(s).
$$

故：

$$
\boxed{
h
\text{ admissible}.
}
$$

---

## 23. Demo heuristic consistency

對任一步：

$$
s\rightarrow s',
$$

因最多四個 corner correctness statuses 改變，所以：

$$
N_c(s)
\leq
N_c(s')+4.
$$

因此：

$$
\left\lceil\frac{N_c(s)}4\right\rceil
\leq
1+
\left\lceil\frac{N_c(s')}4\right\rceil.
$$

即：

$$
h_c(s)
\leq
1+h_c(s').
$$

所以 $h_c$ consistent。

同理 $h_e$ consistent。

而 max of consistent heuristics 仍 consistent，因此：

$$
\boxed{
h=\max(h_c,h_e)
\text{ consistent}.
}
$$

這是原 Demo 可以正式繼承進新版 Search Kernel 的第一個 verified heuristic candidate。

---

## 24. 為什麼這個 heuristic 很弱

若八個 corners 全部 incorrect：

$$
N_c=8,
$$

則：

$$
h_c=2.
$$

這只告訴我們「至少需要兩步」。

它沒有區分：

- pieces 距離 home 多遠；
- orientation 是否容易修正；
- permutation cycle structure；
- edges 與 corners 的耦合；
- subgroup distance。

所以它的優點是：

$$
\text{cheap}
+
\text{easy to prove}.
$$

缺點是：

$$
\text{low information}.
$$

因此很適合作為：

$$
\boxed{
\text{verified baseline heuristic}.
}
$$

而不是最終高效 solver heuristic。

---

## 25. Heuristic Registry

新版工程建議建立：

```text
HeuristicSpec
  name
  inputRepresentation
  lowerBoundType
  admissible
  consistent
  additiveGroup
  tableCardinality
  memoryBytes
  evalCost
  precomputeCost
  proofStatus
  source
```

例如：

```text
MisplacedPiecesOver4
  inputRepresentation: Cubie
  admissible: proven
  consistent: proven
  precomputeCost: none

Phase1Pruning
  inputRepresentation: Phase1Coordinates
  admissible: yes under exact-distance table semantics
  precomputeCost: high
```

這讓 heuristic 不再只是程式碼裡的一個函數名稱。

---

## 26. PDB 建構器的工程接口

Pattern Database builder 可抽象成：

```text
PatternSpec
  project : FullState -> AbstractState
  abstractMoves
  abstractGoal
  abstractCost
  canonicalize
```

輸出：

```text
PatternDatabase
  distance : AbstractState -> Distance
  metadata
  checksum
  proofOrValidationReport
```

若 abstract graph 可完全列舉，就可以用 reverse BFS / Dijkstra 計算 exact distances。

其 correctness contract：

$$
\operatorname{PDB}[a]
=
d_{\mathcal A}(a,\alpha(G)).
$$

---

## 27. 可視化：讓使用者看到「為什麼被剪」

每個 search node 可以顯示：

$$
g,
\quad
h_1,
\quad
h_2,
\quad
h_{\max},
\quad
f.
$$

若被 PDB 剪枝：

```text
PRUNED
reason: f > threshold
g: 7
PDB-corner: 5
PDB-edge: 6
h=max(...): 6
f: 13
threshold: 12
```

若被 move dominance 剪枝：

```text
PRUNED
reason: dominated move sequence
sequence: R R
canonical replacement: R2
cost: 2 -> 1
```

若被 duplicate pruning：

```text
PRUNED
reason: transposition
state: #A91F...
old g: 8
best known g: 6
```

這使「剪枝」從黑盒最佳化變成可以被人直接理解的證據鏈。

---

## 28. Heuristic inspection view

FCSR flat net、cubie view 與 search view 可以增加 heuristic inspection mode。

例如對當前 state：

$$
h_{\mathrm{corner}}=4,
$$

$$
h_{\mathrm{edge}}=5,
$$

$$
h_{\mathrm{phase1}}=7.
$$

UI 可以同步標示：

- 哪些 pieces 進入 pattern；
- 哪些資訊被 projection 忽略；
- PDB index；
- table distance；
- 最終 heuristic combination。

這正好回到 FDRS 的核心：

$$
\boxed{
\text{不同觀察表示究竟保留了什麼計算信息？}
}
$$

---

## 29. FDRS 的抽象－下界命題

本篇提供一個重要的 FDRS-Cube 橋樑。

若表示轉換：

$$
\alpha:
\mathcal S
\rightarrow
\mathcal A
$$

不是單純畫面 relayout，而是 cost-nonincreasing abstraction，則：

$$
\boxed{
\text{抽象空間中的精確距離}
\leq
\text{原空間中的精確距離}.
}
$$

因此：

$$
\boxed{
\text{某些商空間表示不只讓問題變小，
還能產生可證明的原問題下界。}
}
$$

這是比「低維比較容易看」更強的計算結果。

---

## 30. Abstraction 越小不一定 heuristic 越強

若 abstraction 過度合併 states：

$$
|\mathcal A|
\ll
|\mathcal S|,
$$

很多具體困難差異會被消失。

可能出現：

$$
h_\alpha(s)
\approx0
$$

即使：

$$
h^\ast(s)
$$

很大。

所以 abstraction 有典型 tradeoff：

$$
\text{table size}
\leftrightarrow
\text{heuristic discrimination}.
$$

這可以成為後續實驗的重要軸。

---

## 31. PDB 記憶體估計

若 abstract state count 為：

$$
N_A
$$

且最大 abstract distance 為：

$$
D_A,
$$

若每格只儲存整數距離，理論最低 bit width 量級為：

$$
b
=
\left\lceil
\log_2(D_A+1)
\right\rceil.
$$

則裸距離表大小約：

$$
M
\approx
N_A\cdot b
$$

bits。

實際實作還需考慮 sentinel、alignment、compression、symmetry index、metadata 與 disk / memory layout。

因此 PDB 是典型：

$$
\boxed{
\text{memory for search reduction}.
}
$$

---

## 32. Heuristic 的評估不只看平均值

對測試集：

$$
\mathcal T
$$

可以記錄：

$$
\bar h
=
\frac1{|\mathcal T|}
\sum_{s\in\mathcal T}h(s),
$$

但在具有 optimal ground truth 的子集上，更可以觀察：

$$
\rho_h(s)
=
\frac{h(s)}{h^\ast(s)}.
$$

此外還應記錄：

- heuristic distribution；
- zero-rate；
- node expansions；
- prune ratio；
- evaluation latency；
- memory；
- preprocessing time。

所以 heuristic quality 是多維 profile，而不是單一數字。

---

## 33. 形式驗證目標：Heuristic Kernel

第五篇對應的 Lean / proof targets：

### H1. Lower-bound pruning theorem

$$
h\leq h^\ast
\land
g+h>\theta
\Rightarrow
\text{no solution of cost }\leq\theta\text{ passes through node}.
$$

### H2. Max admissibility

$$
\operatorname{Adm}(h_1)
\land
\operatorname{Adm}(h_2)
\Rightarrow
\operatorname{Adm}(\max(h_1,h_2)).
$$

### H3. Abstraction admissibility

對 cost-nonincreasing abstraction：

$$
d_{\mathcal A}(\alpha(s),\alpha(G))
\leq
d_{\mathcal S}(s,G).
$$

### H4. PDB lookup correctness

$$
\operatorname{PDB}[\alpha(s)]
=
d_{\mathcal A}(\alpha(s),\alpha(G)).
$$

### H5. Cost-partition additivity

若：

$$
\sum_i c_i(o)\leq c(o),
$$

則：

$$
\sum_i h_i(s)\leq h^\ast(s).
$$

### H6. Demo heuristic admissibility

$$
\max\left(
\left\lceil N_c/4\right\rceil,
\left\lceil N_e/4\right\rceil
\right)
\leq
h^\ast.
$$

### H7. Demo heuristic consistency

對任意 unit-cost face move：

$$
h(s)\leq1+h(s').
$$

---

## 34. 本文核心命題

### 命題 H-A：安全剪枝來自 lower-bound proof

$$
h\leq h^\ast.
$$

### 命題 H-B：PDB 是 exact abstract solution table

$$
h_{\mathrm{PDB}}(s)
=
d_{\mathcal A}(\alpha(s),\alpha(G)).
$$

### 命題 H-C：max 組合安全

$$
h_{\max}
=
\max_i h_i
$$

保持 admissibility。

### 命題 H-D：sum 組合需要成本分配證明

$$
\sum_i h_i
$$

不能無條件使用。

### 命題 H-E：move pruning 需要 dominance / equivalence proof

不是所有「看起來沒用」的 move 都能安全刪除。

### 命題 H-F：原 Demo heuristic 可以正式證明

$$
h
=
\max(
\lceil N_c/4\rceil,
\lceil N_e/4\rceil
)
$$

是 admissible 且 consistent 的 baseline。

### 命題 H-G：FDRS abstraction 可以直接產生 search lower bound

若 abstraction 不增加成本，抽象 exact distance 就是原問題的 lower bound。

---

## 35. 結論

本文完成 FDRS/FCSR 經典魔方線從「搜尋策略」到「搜尋知識」的推進。

第四篇回答：

> BFS、Bidirectional、A*、IDA* 如何安排探索？

本文回答：

> 搜尋器憑什麼知道哪些分支可以不看？

答案是：

$$
\boxed{
\text{proof-backed lower bounds}
+
\text{solution-preserving pruning}.
}
$$

Pattern Database 的價值不在於巨大查表本身，而在於它把：

$$
\text{一個較小抽象問題的精確解}
$$

轉換成：

$$
\text{原問題的可靠下界}.
$$

這也使 FDRS 起源中的「改變表示」第一次獲得一個直接的演算法定理：

$$
\boxed{
\text{適當 abstraction 的精確距離，可以成為原空間搜尋的證明式導航資訊。}
}
$$

至此，我們已經具備進入 Two-Phase 的全部前置地基：

- legal state；
- representation；
- coordinate；
- search；
- admissible heuristic；
- pruning table；
- symmetry；
- subgroup / quotient 語言。

下一篇將正式處理：

**《Two-Phase 與子群分解：經典高效魔方求解的結構化路徑》**。

---

## 參考資料與來源定位

### 起源與既有實作

- [F2026-D] `FDRS_展開收斂_同步性.html`，FDRS/FCSR permutation engine、piece-count heuristic、IDA*、FSM 與同步可視化原型。

### 外部啟發式搜尋基線

- [R1] Richard E. Korf, **Finding Optimal Solutions to Rubik's Cube Using Pattern Databases**, Proceedings of AAAI-97, 1997。
- [R2] Joseph C. Culberson, Jonathan Schaeffer, **Pattern Databases**, Computational Intelligence, 1998。
- [R3] Richard E. Korf, Ariel Felner, **Disjoint Pattern Database Heuristics**, Artificial Intelligence, 2002。
- [R4] Ariel Felner, Richard E. Korf, Sarit Hanan, **Additive Pattern Database Heuristics**, Journal of Artificial Intelligence Research, 2004。
- [R5] Herbert Kociemba, **Pruning Tables**，官方技術說明。
- [R6] Herbert Kociemba, **Coordinates and Symmetry**，官方技術說明。
- [R7] Herbert Kociemba, **The Move Tables**，官方技術說明。
- [R8] Herbert Kociemba, **Two-Phase Algorithm Details**，官方技術說明。

---

## 版本註記

v0.1 將 heuristic 統一定義為 lower-bound certificate，將 PDB 定義為 abstract exact-distance table，並將所有 pruning rule 納入 safety contract。

本篇亦首次把原 FDRS Demo 的 piece-count heuristic 從「工程直覺」提升為可證 admissible / consistent 的正式 baseline。

後續第六篇：

**《Two-Phase 與子群分解：經典高效魔方求解的結構化路徑》**。
