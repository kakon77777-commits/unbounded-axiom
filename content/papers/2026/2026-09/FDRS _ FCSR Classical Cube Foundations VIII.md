# FDRS / FCSR Classical Cube Foundations VIII
## 多表示同步可視化：3D、FCSR Net、Permutation、Cubie、Graph 與 Search Frontier

**英文題名：** Synchronized Multi-Representation Visualization: 3D, FCSR Net, Permutation, Cubie, Graph, and Search Frontier  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-08  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第八篇

---

## 摘要

FCSR 的起源優勢不是比傳統 solver 多一套搜尋演算法，而是將同一個魔方狀態以不同觀察形式同步呈現。早期 FDRS 魔方網頁原型已包含 $3D\leftrightarrow2D$ 連續 morph、permutation-based move engine、adjacency graph、連通分量、IDA* 與 FSM；然而這些功能仍以單一 Demo 為中心，尚未形成可泛化的「多表示同步語義」。

本文把可視化提升為 FDRS/FCSR 經典魔方線的一級計算層。定義 canonical puzzle state

$$
s_k\in\mathcal S
$$

作為唯一真實狀態，所有視圖均由 projection

$$
R_i:\mathcal S\rightarrow\mathcal V_i
$$

派生。對同一 move

$$
a_k,
$$

每個視圖的離散更新必須滿足：

$$
R_i(T(s_k,a_k))
=
\widetilde T_{i,a_k}(R_i(s_k)).
$$

這是同步可視化的語義核心。

本文進一步區分「離散 canonical state」與「連續 animation state」。面轉動畫、 $3D\leftrightarrow2D$ morph、camera orbit 與 search replay 可以在時間參數 $\tau\in[0,1]$ 上連續插值，但只有 move commit event 才能將

$$
s_k
$$

更新為：

$$
s_{k+1}=T(s_k,a_k).
$$

因此任何 viewer 都不能自行改寫 canonical state。

在 UI 架構上，本文定義七類同步視圖：Physical 3D、FCSR Flat Net、Facelet/Permutation、Cubie、Coordinate/Invariant、Search、Proof。任一 piece、move、search node 或 certificate 被選取時，其他視圖必須透過 stable identity 進行 cross-highlighting。大量 search nodes 不直接逐點渲染，而採 aggregation、sampling、level histogram、threshold bands 與 selected-path detail，避免把「可視化所有計算」誤解成「把數百萬個節點全部畫在畫面上」。

本文亦對照現代 twisty puzzle 前端生態。cubing.js 的 `TwistyPlayer` 已能顯示並播放多種 puzzle 與 algorithm；`KPuzzle` 將 puzzle definition、pattern 與 transformation 抽象化；`PuzzleGeometry` 可產生 SVG、3D 幾何與 permutation 等資料。因此新版 FCSR 不應把「能畫一顆 3D 魔方」當作差異化。其新價值應放在**同一 canonical state 下，幾何表示、代數表示、搜尋內部與證明狀態的同步分析**。

本文最後提出 `CanonicalStore + EventLog + RepresentationRegistry + SearchTrace + ProofTrace + ViewAdapters` 架構，並把 deterministic replay、observer scale、cross-view selection、accessibility、performance budget 與 multi-puzzle compatibility 納入規格。這使 FCSR 從一個展平 Demo 正式提升為 Twisty Computation Observatory 的 UI 理論地基。

**關鍵詞：** FCSR、FDRS、multi-representation、synchronized visualization、canonical state、event log、search trace、proof trace、TwistyPlayer、KPuzzle、observer scale

---

## 1. 回到 FCSR 的原生優勢

前七篇解決了：

$$
\text{state}
+
\text{algorithm}
+
\text{proof}.
$$

但 FCSR 最初真正有辨識度的地方一直是：

$$
\boxed{
\text{讓同一件事以不同觀察形式被看見}.
}
$$

2025--2026 的原型已經同時顯示：

- 立體魔方；
- 平面十字展開；
- 貼面 adjacency graph；
- $\beta_0$ ；
- solved facelet count；
- solver phase；
- move count。

因此第八篇不是額外補一個 UI chapter。

它是在回答：

> 如果 representation 本身就是 FDRS 的核心研究對象，如何保證所有 representation 真的是同一個世界的同步觀察，而不是七個各自維護狀態的 widget？

---

## 2. Canonical state：只能有一個真相來源

定義 canonical state：

$$
s_k\in\mathcal S_{\mathrm{legal}}.
$$

所有 viewer 都不能擁有獨立 puzzle truth。

而只能透過：

$$
R_i:
\mathcal S_{\mathrm{legal}}
\rightarrow
\mathcal V_i
$$

讀取。

因此：

```text
Canonical State
      ↓
Representation Registry
      ├─ 3D
      ├─ Flat Net
      ├─ Facelet
      ├─ Cubie
      ├─ Coordinate
      ├─ Search
      └─ Proof
```

UI state 可以很多個。

Puzzle state 只能一個。

---

## 3. Single Source of Truth Principle

定義：

$$
\operatorname{Truth}(t)
=
s_k.
$$

任意 viewer：

$$
V_i(t)
$$

都必須是：

$$
V_i(t)
=
\operatorname{Render}_i(s_k,\xi_i(t)),
$$

其中：

$$
\xi_i(t)
$$

只包含 viewer-local data，例如：

- camera；
- zoom；
- selected piece；
- animation progress；
- panel layout；
- display filter。

不得包含另一套獨立 puzzle permutation。

所以：

$$
\boxed{
\text{view-local state}
\neq
\text{domain state}.
}
$$

---

## 4. Move synchronization theorem

對 move：

$$
a_k\in A,
$$

canonical transition：

$$
s_{k+1}
=
T(s_k,a_k).
$$

每個 representation 必須具有相容更新：

$$
\widetilde T_{i,a_k}:
\mathcal V_i
\rightarrow
\mathcal V_i.
$$

且：

$$
\boxed{
R_i(T(s_k,a_k))
=
\widetilde T_{i,a_k}(R_i(s_k)).
}
$$

這個交換性就是第一篇建立的 FCSR 核心 theorem，現在被直接提升為 UI synchronization contract。

---

## 5. 離散狀態與連續動畫必須分離

魔方本體的 move 是離散的：

$$
s_k
\rightarrow
s_{k+1}.
$$

但動畫是連續的。

令 animation progress：

$$
\tau\in[0,1].
$$

viewer 可以顯示：

$$
\mathcal A_i
(
R_i(s_k),
R_i(s_{k+1}),
\tau
).
$$

當：

$$
0<\tau<1
$$

時，畫面可能呈現半轉狀態。

但 canonical state 仍然是：

$$
s_k.
$$

只有：

$$
\tau=1
$$

並觸發 commit 後，store 才切換到：

$$
s_{k+1}.
$$

因此：

$$
\boxed{
\text{animation interpolation is not a legal cube state transition}.
}
$$

這一點對形式驗證尤其重要。

---

## 6. Commit Event

定義：

```text
MoveStarted
MoveProgress
MoveCommitted
```

真正改變 canonical state 的只有：

```text
MoveCommitted
```

其語義為：

$$
s_{k+1}=T(s_k,a_k).
$$

`MoveProgress` 只改變：

$$
\xi_i.
$$

這可以避免：

- 3D 已經轉完；
- Flat Net 還在舊狀態；
- Search view 已經前進一格；
- Proof checker 卻讀到半套 permutation；

這類同步錯誤。

---

## 7. FCSR Morph 也不是狀態轉移

原 Demo 的：

$$
3D
\leftrightarrow
2D
$$

morph 可以寫成：

$$
M_\lambda:
\mathcal V_{3D}
\rightarrow
\mathcal V_{\mathrm{morph}},
$$

其中：

$$
\lambda\in[0,1].
$$

當：

$$
\lambda=0
$$

為立體表示，

$$
\lambda=1
$$

為平面 net。

但對所有：

$$
\lambda,
$$

其底層仍應對應同一：

$$
s_k.
$$

因此：

$$
\boxed{
\text{morph changes representation geometry, not puzzle state}.
}
$$

---

## 8. 七大同步視圖

本文建議新版 FCSR 第一版具有七類 view families。

### V1. Physical 3D View

顯示：

- cubie geometry；
- stickers；
- move animation；
- camera；
- layer selection。

### V2. FCSR Flat Net

顯示：

- 六面平面 layout；
- sticker positions；
- adjacency；
- cross-face strip movement；
- selected pieces / patterns。

### V3. Facelet / Permutation View

顯示：

$$
54
$$

個 facelet indices，以及 move permutation：

$$
\sigma_a\in S_{54}.
$$

### V4. Cubie View

顯示：

$$
(\pi_c,o_c,\pi_e,o_e).
$$

### V5. Coordinate / Invariant View

顯示：

- twist；
- flip；
- UDSlice；
- parity；
- symmetry coordinate；
- phase membership；
- heuristic values。

### V6. Search View

顯示：

- frontier；
- expanded nodes；
- threshold；
- pruning；
- selected path；
- phase candidates。

### V7. Proof View

顯示：

- legality；
- solution certificate；
- lower / upper bounds；
- optimality status；
- theorem / checker state。

---

## 9. 3D View 不再是產品核心，而是其中一個 adapter

現代 twisty puzzle 生態已經有成熟的 3D 播放器。

因此新版 FCSR 不應把：

> 會旋轉的漂亮魔方

當成主要研究成果。

Physical 3D 的角色是：

$$
\boxed{
\text{human geometry adapter}.
}
$$

它與：

$$
R_{\mathrm{flat}},
R_{\mathrm{cubie}},
R_{\mathrm{coord}}
$$

在語義上是平行的。

這個定位反而能防止 UI 架構再次被 3D renderer 綁死。

---

## 10. Flat Net 是 FCSR 的歷史錨點

FCSR flat view 保留系列起源。

但新版功能不只：

> 把六面攤開。

還應顯示：

- move strip transfer；
- piece identity；
- source / destination；
- orientation；
- selected cycle；
- heuristic pattern；
- phase constraints。

例如執行：

$$
R
$$

時，可以同時高亮：

- 右面九格；
- 四組側邊 facelets；
- 四 corners；
- 四 edges；
- permutation cycles。

如此 Flat Net 從「展平畫面」成為：

$$
\boxed{
\text{2D operation microscope}.
}
$$

---

## 11. Stable identity：cross-highlighting 的前提

每個實體必須有 stable ID。

例如：

```text
corner: URF
edge: UF
facelet: U8
move: R
searchNode: N-000182
certificate: C-0041
```

若使用者在 3D 點：

```text
URF corner
```

其他 views 應同步：

- Flat Net 高亮三個對應 facelets；
- Cubie View 高亮該 corner；
- Permutation View 高亮其位置；
- Coordinate View 顯示 orientation；
- Search View 顯示 selected state 中的該 piece；
- Proof View 顯示與其相關 invariant。

所以：

$$
\boxed{
\text{selection identity must cross representations}.
}
$$

---

## 12. Cross-view selection relation

定義 entity universe：

$$
\mathcal E.
$$

每個 view 有：

$$
I_i:
\mathcal V_i
\rightarrow
2^{\mathcal E}.
$$

選取：

$$
e\in\mathcal E
$$

後，各 view 只需問：

$$
e\in I_i(v)?
$$

便能決定其 visual emphasis。

這比 panel 之間直接互相呼叫：

```text
flat.highlightCell(...)
cube.highlightSticker(...)
graph.highlightNode(...)
```

更可擴張。

---

## 13. Move 也應是可選實體

不只 piece 可以被選。

Move：

$$
a
$$

本身也是 entity。

選：

$$
R
$$

後可同步顯示：

### 3D

轉哪一層。

### Flat

哪些 strips 重排。

### Permutation

$$
\sigma_R.
$$

### Cubie

哪些 corners / edges 被作用。

### Coordinate

各 coordinate 的 transition：

$$
x\rightarrow x'.
$$

### Search

哪些 branch 使用：

$$
R.
$$

這讓「move」第一次跨視圖可觀察。

---

## 14. State Snapshot

每個 commit 後保存 immutable snapshot：

```text
StateSnapshot
  stateId
  canonicalState
  moveFromParent
  parentStateId
  metricCost
  representationCacheRefs
  legalityStatus
  phase
```

UI timeline 不直接依賴 mutable live object。

因此：

$$
s_0,s_1,\ldots,s_n
$$

可以被任意來回 replay。

---

## 15. Event Log

所有 canonical events 進入 append-only log：

```text
PuzzleLoaded
StateImported
MoveCommitted
ScrambleApplied
SearchStarted
SearchStopped
SolutionAccepted
CertificateVerified
ViewModeChanged
```

其中只有 domain-changing events 形成新 canonical state。

view-only events 不改變 puzzle truth。

---

## 16. Deterministic Replay

若初始狀態：

$$
s_0
$$

與 event sequence：

$$
E=(e_1,\ldots,e_n)
$$

固定，

replay 應得到唯一：

$$
s_n.
$$

即：

$$
\operatorname{Replay}(s_0,E)
=
s_n.
$$

這讓：

- debug；
- benchmark；
- paper reproduction；
- proof trace；
- screen recording；

都可以重現同一次 solve。

---

## 17. Search state 與 puzzle state 不同

搜尋器同時維護大量 hypothetical states。

因此必須區分：

$$
s_{\mathrm{live}}
$$

與：

$$
s_{\mathrm{search}}^{(j)}.
$$

Live state 是目前真正顯示／操作中的 puzzle。

Search node 是 solver 假設分支中的 candidate。

點擊 search node 時，UI 應進入：

```text
Inspect mode
```

而不是把 live canonical state 偷偷改成該 node。

---

## 18. Inspect Mode

定義：

$$
s_{\mathrm{inspect}}
$$

作為純 read-only overlay。

viewer 可以暫時渲染：

$$
R_i(s_{\mathrm{inspect}})
$$

但 canonical live store 仍維持：

$$
s_{\mathrm{live}}.
$$

退出 Inspect Mode 後回到 live state。

這對 search visualization 非常重要。

---

## 19. Search Frontier 不應逐節點全部渲染

IDA*、BFS 或 A* 可能生成：

$$
10^5,
10^6,
10^8
$$

級別 nodes。

「可視化所有搜尋」不能理解成：

> 每個 node 都畫一個圓。

這會同時失去：

- 性能；
- 可讀性；
- 數學意義。

所以需建立 aggregation levels。

---

## 20. Search Aggregation Levels

### Level 0：Summary

顯示：

$$
N_{\mathrm{gen}},
N_{\mathrm{exp}},
N_{\mathrm{prune}},
M_{\mathrm{peak}}.
$$

### Level 1：Depth / Threshold

顯示：

$$
N_d
$$

或：

$$
N_\theta.
$$

### Level 2：Heuristic Buckets

例如：

$$
(g,h,f)
$$

分箱。

### Level 3：Representation Classes

按：

- phase coordinate；
- symmetry class；
- subgroup membership；

聚合。

### Level 4：Selected Paths

只顯示：

- current DFS path；
- best path；
- phase candidates；
- final solution。

### Level 5：Individual Nodes

只有使用者 drill-down 才顯示個別 node。

---

## 21. Observer Scale

FDRS 起源一直關心觀察尺度。

本文把 UI scale 定義成：

$$
\omega
\in
\{
\text{macro},
\text{meso},
\text{micro}
\}.
$$

### Macro

看：

- phase；
- frontier size；
- solution bound；
- global invariants。

### Meso

看：

- coordinate classes；
- heuristic buckets；
- patterns；
- selected subtrees。

### Micro

看：

- 某一 state；
- 某一 move；
- 某一 cubie；
- 某一 certificate step。

這使「觀察者尺度」成為實際 UI 操作，不只是哲學詞。

---

## 22. Same event, different observers

對同一 move：

$$
a=R,
$$

不同 observer 看到：

### Geometry observer

$$
\text{右層轉 }90^\circ.
$$

### Facelet observer

$$
\sigma_R\in S_{54}.
$$

### Cubie observer

$$
(\pi_c,o_c,\pi_e,o_e)
\rightarrow
(\pi'_c,o'_c,\pi'_e,o'_e).
$$

### Coordinate observer

$$
x\rightarrow x'.
$$

### Search observer

$$
g\rightarrow g+1,
\qquad
h\rightarrow h'.
$$

### Proof observer

$$
\operatorname{Valid}(s')
=
\mathrm{true}.
$$

它們不是六個事件。

它們是：

$$
\boxed{
\text{one event, six projections}.
}
$$

---

## 23. Synchronization Frame

定義每個 committed domain event 的 frame：

```text
SyncFrame
  eventId
  beforeStateId
  afterStateId
  move
  representations
  searchContext
  proofContext
```

所有 view adapters 消費同一個：

```text
SyncFrame
```

而不是自行監聽別的 panel。

---

## 24. Representation Registry 與 View Adapter 分離

第三篇已提出 Representation Registry。

現在再分：

```text
RepresentationSpec
```

與：

```text
ViewAdapter
```

Representation 負責：

$$
R_i(s).
$$

ViewAdapter 負責：

$$
\operatorname{Render}_i(R_i(s),\xi_i).
$$

所以同一個 cubie representation 可以有：

- table view；
- graph view；
- matrix view；

而不必重算 domain semantics。

---

## 25. Current ecosystem baseline：TwistyPlayer

截至本文日期，cubing.js 提供 `TwistyPlayer`，可在網頁中播放 algorithm，並支援多種 puzzle。

其 current API 已列出包括：

- $2\times2\times2$ ；
- $3\times3\times3$ ；
- $4\times4\times4$ ；
- $5\times5\times5$ ；
- $6\times6\times6$ ；
- $7\times7\times7$ ；
- Skewb；
- Pyraminx；
- Megaminx；
- Gigaminx；
- Square-1；
- Clock；
- FTO；

以及其他 puzzle。

這代表「多 puzzle 3D 播放」本身已不是空白市場。

---

## 26. Current ecosystem baseline：KPuzzle

cubing.js 的 `KPuzzle` 把：

- default pattern；
- puzzle definition；
- move transformation；
- algorithm transformation；

放入統一 puzzle abstraction。

其 `KPuzzleDefinition` 包含：

```text
name
orbits
defaultPattern
moves
derivedMoves
```

這和本系列第九篇要做的 generalized puzzle specification 有直接參考價值。

但 FCSR 仍需要自己的 canonical semantics / proof contracts，不能直接把第三方 runtime 當成形式證明。

---

## 27. Current ecosystem baseline：PuzzleGeometry

cubing.js 的 `PuzzleGeometry` 可產生：

- SVG；
- 3D sticker geometry；
- permutations；
- KPuzzle definition；

等資料。

所以新版 FCSR 若需要快速支援多 puzzle，可以把這類 library 當：

$$
\text{geometry / notation adapter}.
$$

但我們的研究層應保持：

$$
\text{Canonical Twisty Semantics}
$$

與外部 renderer 解耦。

---

## 28. Current ecosystem gap：分析同步，而不只是播放

現代播放器很擅長：

- 顯示 puzzle；
- 播放 algorithm；
- 改 camera；
- 選 puzzle；
- 顯示 setup / scramble。

FCSR 的差異化不應跟它們比：

> 誰的 3D 更漂亮。

而應回答：

> 同一個 move 在代數、搜索、heuristic、proof 中發生了什麼？

所以產品定位應更接近：

$$
\boxed{
\text{Twisty Computation Observatory}
}
$$

而不是：

$$
\text{another cube player}.
$$

---

## 29. Proof View

Proof panel 不顯示巨量 Lean source。

它顯示 claim graph。

例如：

```text
State Legal                ✓
Move Semantics             ✓
Solution Replay            ✓
Goal Reached               ✓
Lower Bound                16
Upper Bound                18
Global Optimality          unresolved
```

點擊：

```text
Lower Bound 16
```

才展開：

- heuristic name；
- abstraction；
- table hash；
- proof status；
- theorem reference。

---

## 30. Proof status vocabulary

統一：

```text
UNVERIFIED
CHECKED
PROVEN
CONDITIONAL
FAILED
UNKNOWN
```

避免用模糊的：

```text
OK
```

例如：

```text
Solution soundness    PROVEN
Global optimality     UNKNOWN
Completeness          CONDITIONAL
```

---

## 31. Search View 與 Proof View 必須不同

Search View 回答：

> 它怎麼找？

Proof View 回答：

> 我們憑什麼相信這個 claim？

一個 search trace 可以有：

$$
10^6
$$

events。

proof trace 可能只需要：

$$
10
$$

個 claims。

所以兩者資料模型、渲染密度與保留週期都不同。

---

## 32. Heuristic View

對 current state：

$$
s,
$$

顯示：

$$
h_{\mathrm{misplaced}}(s),
$$

$$
h_{\mathrm{PDB1}}(s),
$$

$$
h_{\mathrm{PDB2}}(s),
$$

$$
h_{\max}(s).
$$

使用者點某個 PDB 時，其他 panel 顯示：

- 哪些 pieces 被該 pattern 保留；
- 哪些自由度被 abstraction 忽略；
- abstract index；
- table value。

這使第五篇的 abstraction theorem 可以被直接看見。

---

## 33. Two-Phase View

第六篇的 boundary state：

$$
s_1\in G_1
$$

應成為 timeline marker。

UI 顯示：

```text
PHASE 1
  Twist  -> 0
  Flip   -> 0
  Slice  -> 0

ENTER G1 ✓

PHASE 2
  Corner Perm
  Edge Perm
  Slice Perm
```

這比只把 move list 中間畫一條線更有語義。

---

## 34. Candidate Boundary Comparison

若 solver 評估多個：

$$
b_i\in G_1,
$$

可以顯示：

$$
C_i
=
d(s_0,b_i)
+
\widehat d_{G_1}(b_i,e).
$$

比較：

- phase-1 cost；
- phase-2 lower bound；
- actual phase-2 cost；
- total。

這讓「最短 phase 1 不等於最短總解」直接可視化。

---

## 35. Legality View

第二篇的 legality checker 應視覺化：

$$
\sum o_c\bmod3,
$$

$$
\sum o_e\bmod2,
$$

$$
\operatorname{parity}(\pi_c),
$$

$$
\operatorname{parity}(\pi_e).
$$

若非法：

```text
ILLEGAL STATE
reason: single edge flip
edge orientation sum: 1 mod 2
```

而不是讓 solver 回：

```text
failed
```

---

## 36. Color accessibility

魔方不能只靠顏色區分。

至少提供：

- color；
- face label；
- pattern / symbol；
- optional piece ID。

例如：

```text
U / ○
R / △
F / □
```

這對：

- color-vision deficiency；
- 灰階截圖；
- 論文圖；
- AI vision benchmark；

都有幫助。

---

## 37. 動畫速度不應影響計算速度

定義：

$$
t_{\mathrm{compute}}
$$

與：

$$
t_{\mathrm{display}}.
$$

solver 可以在：

$$
0.05\text{ s}
$$

內完成。

UI 可以用：

$$
5\text{ s}
$$

播放。

兩者不得耦合。

所以：

$$
\boxed{
\text{computation clock}
\neq
\text{presentation clock}.
}
$$

---

## 38. Replay Modes

至少提供：

### Real-time

按原執行時間播放。

### Normalized

固定每 move：

$$
\Delta t.
$$

### Step

一次一 event。

### Semantic

只停在：

- threshold raise；
- phase boundary；
- new best solution；
- proof verified；

等重要事件。

Semantic Replay 特別適合研究展示。

---

## 39. Search sampling 不能改變 proof

UI 可能只顯示：

$$
1/1000
$$

search nodes。

但 solver / proof layer 必須基於完整 computation。

因此：

$$
\boxed{
\text{visual sampling}
\neq
\text{computational sampling}.
}
$$

除非使用者明確選擇 approximate solver。

---

## 40. Performance budgets

多 panel 同步最容易造成 UI 本身拖慢 solver。

因此建議：

```text
renderBudgetMs
eventBatchSize
maxVisibleNodes
maxSearchTraceMemory
snapshotInterval
```

solver event stream 透過 batching / backpressure 送 UI。

若 UI 跟不上：

$$
\text{drop visual frames}
$$

而不是：

$$
\text{drop solver events required for proof}.
$$

---

## 41. Event priority

事件分三級：

### P0：Canonical / Proof-critical

不可丟：

- MoveCommitted；
- GoalFound；
- CertificateVerified；
- PhaseBoundary。

### P1：Search-semantic

可批次但應保留統計：

- NodeExpanded；
- NodePruned；
- ThresholdRaised。

### P2：Pure visual

可丟 frame：

- camera interpolation；
- hover；
- animation frame。

這能維持 performance 與 reproducibility。

---

## 42. Worker / process boundary

未來 Web 版應把 solver 與 renderer 分開。

概念：

```text
UI Thread
  ├─ View Adapters
  └─ Interaction

Solver Worker
  ├─ Search
  ├─ PDB lookup
  └─ Trace aggregation

Verifier Worker
  ├─ solution checker
  └─ certificate checker
```

原 Demo 曾因 file-origin Worker 限制等部署環境問題暴露 browser execution 邊界，因此新版一開始就應把 local-file mode 與 served mode 都納入測試矩陣。

---

## 43. Canonical serialization

每個 state snapshot 應能輸出：

```text
puzzleSpec
state
metric
moveHistory
representationVersion
```

而不依賴畫面。

因此 screenshot 不是 canonical artifact。

正式可重現輸出仍是：

$$
\boxed{
\text{UTF-8 / structured state artifact}.
}
$$

---

## 44. URL / share state

對非敏感公開 puzzle，可把：

- puzzle type；
- scramble；
- algorithm；
- selected view；

編碼到 shareable state。

但：

- PDB；
- search trace；
- proof artifacts；

應有獨立 downloadable artifact，而不硬塞入 URL。

---

## 45. Representation provenance

每個 panel 應能回答：

> 你現在看的資料怎麼來的？

例如：

```text
Cubie View
source: CanonicalCubeState v1
adapter: cubie-v1
lossless: yes

Phase1 Coordinate
source: Cubie View
adapter: phase1-kociemba-v1
lossless: no
task: enter G1
```

這能把第三篇的 representation metadata 直接呈現。

---

## 46. External library provenance

若使用 cubing.js：

```text
Renderer: cubing.js
Puzzle semantics: external adapter
Canonical solver state: FCSR core
Proof status: independent
```

不要讓 UI 使用者誤以為：

> 因為畫面用了成熟 library，所以 formal solver 就被那個 library 證明了。

library provenance 與 proof provenance 必須分開。

---

## 47. Architecture

本文建議：

```text
CanonicalStore
    ↓
EventLog
    ↓
SyncFrameBuilder
    ↓
RepresentationRegistry
    ├─ Physical3D
    ├─ FCSRFlat
    ├─ FaceletPerm
    ├─ Cubie
    ├─ Coordinate
    ├─ Search
    └─ Proof
    ↓
ViewAdapters
```

旁路：

```text
SearchKernel
    ↓
SearchTrace
    ↓
SyncFrameBuilder

Verifier
    ↓
ProofTrace
    ↓
SyncFrameBuilder
```

---

## 48. CanonicalStore API

概念：

```text
getState()
applyMove(move)
importState(raw)
reset()
subscribeDomainEvents()
```

不提供：

```text
setStickerColorUnsafe()
```

給一般 UI。

手動編輯 facelets 必須走：

$$
\text{Raw Input}
\rightarrow
\text{Parser}
\rightarrow
\text{Legality}
\rightarrow
\text{Commit}.
$$

---

## 49. RepresentationRegistry API

概念：

```text
register(spec)
encode(name, state)
describe(name)
compare(a, b)
proveOrReportCompatibility(name)
```

`describe` 應回：

```text
injective
reversible
moveClosed
task
cardinality
proofStatus
```

這讓 UI 可以自動生成 representation inspector。

---

## 50. Sync correctness test

對每個合法 random state：

$$
s,
$$

每個 move：

$$
a,
$$

每個 representation：

$$
R_i,
$$

測試：

$$
R_i(T(s,a))
=
\widetilde T_{i,a}(R_i(s)).
$$

這應成為 property-based test。

若 representation 已在 Lean 證明，runtime test 仍保留作 implementation regression check。

---

## 51. Replay correctness test

對 event sequence：

$$
E,
$$

測：

$$
\operatorname{Replay}(s_0,E)
=
s_n.
$$

並比較：

- live execution；
- serialized replay；
- worker replay；

三者 canonical hash 一致。

---

## 52. Visual correctness 不是 mathematical correctness

即使 canonical state 正確，renderer 仍可能畫錯。

所以測試分：

### Domain tests

驗：

$$
s.
$$

### Projection tests

驗：

$$
R_i(s).
$$

### Rendering tests

驗 visual adapter 是否正確畫出：

$$
R_i(s).
$$

這三層不能混為一個「看起來正常」。

---

## 53. Screenshot regression 的位置

Screenshot / pixel regression 可以檢查：

- layout；
- sticker placement；
- selection；
- panel sync。

但不能代替：

$$
\operatorname{MoveCorrectness}.
$$

所以：

$$
\boxed{
\text{visual regression}
\neq
\text{semantic proof}.
}
$$

---

## 54. 第九篇的接口預留

第八篇不能把資料結構寫死成：

```text
8 corners
12 edges
54 facelets
```

view adapters 應讀 puzzle specification。

因此：

$$
\text{3x3}
$$

只是第一個：

$$
\mathcal P.
$$

下一篇會把：

- orbits；
- orientations；
- moves；
- geometry；
- goal；
- notation；

全部提升為通用 puzzle spec。

---

## 55. Multi-puzzle visualization contract

對任意 puzzle：

$$
\mathcal P,
$$

若它提供：

$$
\operatorname{CanonicalState}_{\mathcal P},
$$

$$
\operatorname{Move}_{\mathcal P},
$$

$$
R_i^{\mathcal P},
$$

則同一 visualization framework 應可運作。

若某 puzzle 沒有天然 flat net：

$$
R_{\mathrm{flat}}
$$

可以不存在。

所以 view system 應支援：

$$
\operatorname{OptionalRepresentation}.
$$

---

## 56. 2D 不應被強制當 universal view

現代 cubing.js 文件也明確指出，部分 puzzle / visualization 組合目前並不支援 $2D$。

這提醒 FDRS：

$$
\boxed{
\text{不是每個 puzzle 都必須被硬展平成同一種十字網格}.
}
$$

真正核心是：

$$
\text{representation suitability}.
$$

FCSR 起源是 flat，但 generalized FDRS viewer 不必崇拜 flat。

---

## 57. View suitability score

對 puzzle：

$$
\mathcal P
$$

與 representation：

$$
R_i,
$$

可定義：

$$
U(R_i,\mathcal P,\tau)
$$

其中：

$$
\tau
$$

為任務。

例如：

- 教學；
- search debugging；
- legality；
- phase analysis；
- speed playback。

同一 representation 對不同任務的 utility 不同。

這直接延續第三篇的 task sufficiency。

---

## 58. Observer profile

未來可讓使用者／AI 選：

```text
Beginner
Speedcuber
Algorithm Researcher
Formal Verification
AI Agent
```

這些不是裝飾 theme。

而是決定預設顯示哪些：

$$
R_i.
$$

例如 `Formal Verification` 預設顯示：

- canonical state；
- certificate；
- bounds；
- proof dependencies。

`Speedcuber` 則可能預設：

- 3D；
- alg；
- move count；
- timing。

---

## 59. FDRS Observer Principle

令 observer profile：

$$
O
$$

選擇可見 representation 集：

$$
\mathcal R_O
\subseteq
\{R_1,\ldots,R_n\}.
$$

則 observer 真正看到的是：

$$
\operatorname{View}_O(s)
=
\{R_i(s):R_i\in\mathcal R_O\}.
$$

所以：

$$
\boxed{
\text{同一 state 的「可理解性」依 observer 的 representation set 改變}.
}
$$

這是 FDRS 起源「觀察角度」命題的可操作版本。

---

## 60. 結論

前七篇解決了：

$$
\text{怎麼定義}
+
\text{怎麼找}
+
\text{怎麼證}.
$$

本文解決：

$$
\boxed{
\text{怎麼讓人與 AI 看見這些事情其實同時發生在同一個狀態上}.
}
$$

新版 FCSR 的核心不應是：

$$
\text{3D Cube Renderer}.
$$

而應是：

$$
\boxed{
\text{Canonical State}
+
\text{Synchronized Representations}
+
\text{Search Trace}
+
\text{Proof Trace}.
}
$$

最重要的同步等式仍然是：

$$
\boxed{
R_i(T(s,a))
=
\widetilde T_{i,a}(R_i(s)).
}
$$

而最重要的時間語義是：

$$
\boxed{
\text{domain state is discrete;
animation is continuous but non-canonical}.
}
$$

因此同一個 move 可以被不同 observer 同時看成：

- 幾何旋轉；
- facelet permutation；
- cubie update；
- coordinate transition；
- search edge；
- proof-preserving transformation。

它們不是多個世界。

它們是：

$$
\boxed{
\text{one world, many synchronized projections}.
}
$$

這就是 FCSR 從 2025 起源 Demo 回到 2026 現代計算架構後，最應保留的正統特色。

下一篇：

**《從 $2\times2\times2$ 到多面體：Twisty Puzzle 的通用規格層》**。

屆時我們會真正把：

$$
\text{Cube}
$$

抽掉，留下：

$$
\boxed{
\text{Twisty Puzzle Specification}.
}
$$

---

## 參考資料與來源定位

### 起源與系列內部

- [F2026-D] `FDRS_展開收斂_同步性.html`，原 FDRS/FCSR $3D\leftrightarrow2D$ morph、permutation engine、adjacency graph、IDA*、FSM 與同步視圖原型。
- [CUBE-03] 本系列第三篇：Representation Registry。
- [CUBE-04] 本系列第四篇：Search Trace。
- [CUBE-06] 本系列第六篇：Two-Phase handoff。
- [CUBE-07] 本系列第七篇：Proof Trace / certificates。

### 當代 twisty puzzle 可視化與規格基線

- [R1] cubing.js, **TwistyPlayer** API / documentation。  
  https://js.cubing.net/cubing/twisty/

- [R2] cubing.js, **KPuzzle** API。  
  https://js.cubing.net/cubing/kpuzzle/

- [R3] cubing.js, **KPuzzleDefinition** API。  
  https://js.cubing.net/cubing/api/interfaces/kpuzzle.KPuzzleDefinition.html

- [R4] cubing.js, **PuzzleGeometry** API。  
  https://js.cubing.net/cubing/api/classes/puzzle-geometry.PuzzleGeometry.html

---

## 版本註記

v0.1 把同步可視化從「多 panel UI」提升為 representation-commutation contract，並首次正式分離 canonical discrete state 與 continuous animation state。

本文亦將 modern puzzle renderer 視為可替換 adapter，而把 FCSR 的差異化放在幾何、代數、搜尋、heuristic 與 proof 的同步分析。

後續第九篇：

**《從 $2\times2\times2$ 到多面體：Twisty Puzzle 的通用規格層》**。
