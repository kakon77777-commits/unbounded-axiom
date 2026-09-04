# FDRS / FCSR Classical Cube Foundations IX
## 從 $2\times2\times2$ 到多面體：Twisty Puzzle 的通用規格層

**英文題名：** From $2\times2\times2$ to Polyhedra: A General Specification Layer for Twisty Puzzles  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-09  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第九篇

---

## 摘要

前八篇已經把標準 $3\times3\times3$ 魔方拆成合法狀態、表示、搜尋、heuristic、Two-Phase、形式驗證與同步可視化。若系統仍把 $8$ 個 corners、 $12$ 個 edges、 $54$ 個 facelets、六個 face turns 與十字形 flat net 寫死在程式中，則它仍然只是「一個做得比較完整的 3x3 solver」，而不是可延伸至 twisty puzzle 領域的基礎設施。

本文提出通用 `TwistyPuzzleSpec`。核心不再以「立方體」為中心，而以 piece orbit、位置、orientation modulus、move transformation、合法動作判定、goal、metric、notation 與 optional geometry 為中心。對一個 puzzle，令 orbit 集為

$$
\mathcal O=\{O_1,\ldots,O_r\}.
$$

每個 orbit $O_i$ 有

$$
n_i
$$

個位置與 orientation modulus

$$
m_i\geq1.
$$

在沒有額外合法性限制的 raw orbit model 中，該 orbit 的狀態可表示為

$$
S_{n_i}\ltimes\mathbb Z_{m_i}^{n_i},
$$

其中 permutation 描述 pieces 的位置，而 orientation vector 描述每個 piece 的局部朝向。整個 raw state space 是各 orbits 的乘積；真正 legal state space 則不以人工列舉所有 parity / orientation constraints 為必要定義，而直接定義為 solved pattern 在合法 move transformations 生成之系統中的 reachable component。

本文同時區分兩類 classical twisty systems。第一類是 total reversible move systems：每個基本 move 在每個合法 state 上皆定義，典型 group-action puzzle 可以直接以有限生成群描述。第二類是 fixed-rule constrained systems：規則本身不變，但某些 move 是否可執行取決於當前 state，可寫成固定的 legality predicate

$$
\operatorname{Enabled}(s,a).
$$

這類 puzzle 更自然地建模為 partial reversible transition system 或 groupoid-like structure，而不是強迫塞入一個「每個生成元 everywhere-defined」的單一群作用。這一區分可以涵蓋 shape-changing、bandaged 或 alignment-constrained puzzle，同時仍將它們保留在本文的 Static Twisty Computation 範圍內。只要

$$
A_t=A(s_t)
$$

由一個固定不變的函數決定，系統仍是 stationary；真正的 Dynamic Cube 將在未來允許規則、目標或轉移律本身隨時間、事件或外部 agent 改變。

本文還把 geometry 從 semantics 中解耦。Puzzle 可以沒有可用的 $2D$ net、沒有唯一的 polyhedral embedding，甚至主要以 permutation / graph 形式存在；只要 canonical state、moves 與 goal 定義清楚，它仍然是可計算的 twisty puzzle。當代 cubing.js 的 `KPuzzleDefinition` 已採用 `name + orbits + defaultPattern + moves + derivedMoves` 的結構，而 `PuzzleGeometry` 能輸出 permutations、3D geometry、SVG 與 KPuzzle definition，說明「orbit-first puzzle definition + optional geometry」在現代工具鏈中具有實際可行性。另有數學工作已把 Rubik-like move group 泛化到任意 $3$ -valent map，顯示「Rubik structure」本身也可以超出單一立方體幾何。

本文最後定義 `PuzzleSpec`、`OrbitSpec`、`MoveSpec`、`GoalSpec`、`MetricSpec`、`NotationSpec`、`GeometryAdapter` 與 `CapabilityProfile`，並提出 solver capability negotiation：不是每一個 solver 都必須支援每一顆 puzzle，也不是每一顆 puzzle 都必須具備 FCSR flat net、Two-Phase 或 PDB；系統應根據 puzzle 結構與 solver 能力自動決定哪些 representation、heuristic、search 與 proof modules 可用。

至此，FCSR/FDRS 經典線完成從「一顆魔方」到「一類固定規則有限離散 twisty systems」的抽象提升，並為下一篇 Static-Domain Closure 以及後續 Dynamic Twisty Systems 建立精確邊界。

**關鍵詞：** twisty puzzle、PuzzleSpec、orbit、orientation、partial transition、group action、groupoid、polyhedra、KPuzzle、PuzzleGeometry、FCSR、FDRS

---

## 1. 第九篇的任務：把「Cube」從核心型別拿掉

前八篇大量使用：

$$
8\text{ corners},
$$

$$
12\text{ edges},
$$

$$
54\text{ facelets}.
$$

這些對 $3\times3\times3$ 正確。

但若直接擴張到：

- $2\times2\times2$ ；
- $4\times4\times4$ ；
- Pyraminx；
- Skewb；
- Megaminx；
- FTO；
- Icosahedral twisty puzzles；
- bandaged puzzles；

這些常數立即失效。

因此第九篇的核心目標是：

$$
\boxed{
\text{3x3-specific semantics}
\rightarrow
\text{TwistyPuzzleSpec}.
}
$$

---

## 2. 不是所有 twisty puzzle 都應先被描述成「六面」

Cube-centric model 常以：

$$
\text{face}
\rightarrow
\text{face turn}
$$

作為第一語言。

但 tetrahedral、octahedral、dodecahedral、icosahedral 或 edge / vertex turning puzzles 的自然轉動軸不同。

因此 spec 應以：

$$
\text{piece orbits}
+
\text{transformations}
$$

為核心，而不是固定：

$$
\text{six faces}.
$$

Geometry 可以描述「這個 transformation 對應哪一個實體轉軸」。

但 transformation semantics 不依賴它一定是一個 cube face。

---

## 3. Orbit-first model

令 puzzle 有 orbit 集：

$$
\mathcal O
=
\{O_1,\ldots,O_r\}.
$$

一個 orbit 代表在 move group / transition structure 下屬於同一類型、可互相交換位置的 pieces。

每個 orbit：

$$
O_i
$$

定義：

- 名稱；
- 位置數：

$$
n_i;
$$

- orientation modulus：

$$
m_i.
$$

若 piece 沒有可觀察 orientation：

$$
m_i=1.
$$

若是一般 edge flip 類：

$$
m_i=2.
$$

若是一般 corner twist 類：

$$
m_i=3.
$$

但 generalized spec 不把：

$$
m_i\in\{1,2,3\}
$$

寫死。

---

## 4. Orbit raw state

對 orbit：

$$
O_i,
$$

piece permutation：

$$
\pi_i\in S_{n_i}.
$$

orientation：

$$
o_i\in\mathbb Z_{m_i}^{n_i}.
$$

所以 raw orbit state 可表示為：

$$
x_i
=
(\pi_i,o_i).
$$

在標準 composition convention 下，permutation 會重新索引 orientation，因此自然具有 semidirect-product 結構：

$$
\boxed{
X_i
\cong
S_{n_i}
\ltimes
\mathbb Z_{m_i}^{n_i}.
}
$$

這是 cubie-level model 的一般化。

---

## 5. Raw global state

所有 orbits 的 raw product：

$$
X_{\mathrm{raw}}
=
\prod_{i=1}^{r}
\left(
S_{n_i}
\ltimes
\mathbb Z_{m_i}^{n_i}
\right).
$$

這只是資料結構上可能的狀態。

它不代表每個 tuple 都 legal。

如同 $3\times3\times3$：

$$
X_{\mathrm{legal}}
\subsetneq
X_{\mathrm{raw}}.
$$

---

## 6. 不要為每一顆 puzzle 手寫一套 closed-form legality theorem

 $3\times3\times3$ 有漂亮的：

$$
\sum o_c=0\pmod3,
$$

$$
\sum o_e=0\pmod2,
$$

$$
\operatorname{parity}(\pi_c)
=
\operatorname{parity}(\pi_e).
$$

但 generalized puzzle 未必有同一組約束。

所以通用定義不應要求：

```text
cornerTwistConstraint
edgeFlipConstraint
parityConstraint
```

一定存在。

更穩定的定義是：

$$
\boxed{
X_{\mathrm{legal}}
=
\operatorname{Reach}(x_\star)
}
$$

其中：

$$
x_\star
$$

為 default solved pattern。

---

## 7. Legal state as reachable component

給定 move relation：

$$
T,
$$

定義：

$$
x\in X_{\mathrm{legal}}
$$

若存在合法 move sequence：

$$
p
$$

使：

$$
T^\ast(x_\star,p)=x.
$$

因此 legal state 是：

$$
\boxed{
\text{solved state 的 reachable component}.
}
$$

若 puzzle 屬於 total group-action case，這等價於：

$$
G\cdot x_\star.
$$

若 moves 是 state-dependent partial transformations，則使用 reachable transition component 更一般。

---

## 8. MoveSpec

每個 primitive move：

$$
a
$$

應定義：

```text
MoveSpec
  id
  orbitTransformations
  inverse
  order
  notationTokens
  geometryRef
  enabledPredicate
```

其中 `orbitTransformations` 對每個 orbit 保存：

- permutation；
- orientation delta。

---

## 9. Orbit transformation

對 orbit：

$$
O_i,
$$

move：

$$
a
$$

的 transformation：

$$
M_{a,i}
=
(\sigma_{a,i},\delta_{a,i}).
$$

其中：

$$
\sigma_{a,i}\in S_{n_i}
$$

是位置 permutation，

$$
\delta_{a,i}
\in
\mathbb Z_{m_i}^{n_i}
$$

是 orientation change。

對 state：

$$
(\pi_i,o_i),
$$

move composition 必須依固定 convention 更新 permutation 與 orientation。

這正是第二、三篇 cubie semantics 的一般化。

---

## 10. Move order

move order：

$$
\operatorname{ord}(a)=k
$$

表示：

$$
a^k=e
$$

且：

$$
k
$$

最小。

Cube quarter turn 常有：

$$
k=4.
$$

但 generalized puzzle 的 move order 可以不同。

因此 UI 不應假設所有 move 都只有：

```text
clockwise
counterclockwise
double
```

三種 variant。

---

## 11. Derived moves

很多 notation 不是 primitive generator，而是：

$$
a
=
b_1b_2\cdots b_k.
$$

因此 spec 可允許：

```text
derivedMoves
```

把語法 token 映射成 move sequence。

當代 `KPuzzleDefinition` 也明確包含 optional `derivedMoves`，同時具有 `orbits`、`defaultPattern` 與 `moves`。這提供了現有工程基線。

---

## 12. DefaultPattern

定義：

$$
x_\star
$$

作為 default solved pattern。

但 generalized puzzle 的「solved」未必只是一個 state。

例如中心 orientation 可忽略、整體 puzzle orientation 可忽略，或多個外觀等價狀態皆可接受。

所以應區分：

$$
\text{defaultPattern}
$$

與：

$$
\text{goalPredicate}.
$$

---

## 13. GoalSpec

定義：

$$
G:
X_{\mathrm{legal}}
\rightarrow
\{\mathrm{true},\mathrm{false}\}.
$$

標準單一 solved state：

$$
G(x)
\iff
x=x_\star.
$$

若忽略整體旋轉或某些 center orientations，可有：

$$
G(x)
\iff
x\sim x_\star.
$$

所以 GoalSpec 必須是一級規格，而不是把：

```text
state == defaultPattern
```

寫死。

---

## 14. MetricSpec

move cost：

$$
c:
(X,a,X')
\rightarrow
\mathbb R_{\geq0}.
$$

經典 metric 可以是：

- quarter-turn metric；
- half-turn metric；
- slice-turn metric；
- puzzle-specific move count。

因此 solver output：

$$
C(p)
$$

只有在：

$$
\operatorname{MetricSpec}
$$

固定後才有意義。

---

## 15. NotationSpec

符號不是 semantics 本身。

Move：

$$
a
$$

可能顯示為：

```text
R
```

另一個 puzzle 使用：

```text
R++
```

或 vertex-turn token。

因此：

$$
\boxed{
\text{Move ID}
\neq
\text{Notation Token}.
}
$$

NotationSpec 負責：

- parse；
- print；
- aliases；
- derived algorithms。

MoveSpec 負責真正 transformation。

---

## 16. GeometryAdapter

Geometry 不進入 canonical algebraic state 的必要核心。

定義 optional：

```text
GeometryAdapter
  pieceMeshes
  stickerGeometry
  axes
  cuts
  cameraDefaults
  flatViews
  pickingMap
```

這使 puzzle 即使只有 permutation spec，也可以先被 solver / verifier 使用。

等 geometry adapter 加入後，再得到 3D / 2D viewer。

---

## 17. 為什麼 geometry 必須 optional

某些 puzzle 可能：

- 只有抽象圖定義；
- 還沒有建模 mesh；
- $2D$ 展開不自然；
- 有多種外觀但相同 algebraic puzzle；
- 是 shape modification。

若 solver kernel 依賴 mesh：

$$
\text{no geometry}
\Rightarrow
\text{no computation},
$$

架構就倒置了。

正確順序：

$$
\boxed{
\text{Semantics first, geometry optional}.
}
$$

---

## 18. 同一 algebraic puzzle 可以有多個 geometry skins

若：

$$
\mathcal P_{\mathrm{alg}}
$$

固定，

可能存在：

$$
\Gamma_1,\Gamma_2,\ldots
$$

多個 geometry adapters。

例如 shape mod 可以在保留核心 transformation structure 的同時改變外觀與人類辨識方式。

所以：

$$
\boxed{
\text{geometry identity}
\neq
\text{algebraic identity}.
}
$$

這對 FDRS 的 representation 理論非常重要。

---

## 19. Total reversible move system

第一類 classical puzzle：

對所有：

$$
s\in X_{\mathrm{legal}},
$$

所有 primitive move：

$$
a\in A,
$$

都有：

$$
T(s,a)
$$

定義。

且存在 inverse：

$$
a^{-1}.
$$

這時候：

$$
A
$$

生成有限群：

$$
G.
$$

legal state：

$$
G\cdot x_\star.
$$

標準 $3\times3\times3$ 屬於此類。

---

## 20. Partial reversible move system

第二類 classical puzzle：

某些 move：

$$
a
$$

只有在：

$$
\operatorname{Enabled}(s,a)
$$

成立時可執行。

定義 partial transition：

$$
T:
X\times A
\rightharpoonup
X.
$$

若：

$$
T(s,a)=s',
$$

則仍要求存在 inverse transition：

$$
T(s',a^{-1})=s.
$$

所以局部 transition 仍可逆。

---

## 21. 為什麼需要 partial transition

這能表達：

- alignment-dependent moves；
- shape-changing puzzles；
- bandaged puzzles；
- mechanism-constrained turns。

關鍵是：

$$
\operatorname{Enabled}
$$

本身仍是一個固定規則。

所以它不是本文未來所說的 Dynamic Cube。

---

## 22. Static 不等於 $A(s)$ 為常數

Static puzzle 可以有：

$$
A(s)
=
\{a:\operatorname{Enabled}(s,a)\}.
$$

只要：

$$
A(\cdot)
$$

這個函數本身在整場 puzzle 中不變。

也就是：

$$
\boxed{
A_t=A(s_t)
}
$$

而不是：

$$
A_t
=
A(s_t,t,E_t,\text{external agent})
$$

隨外部世界改規則。

---

## 23. Group-action 與 groupoid-like 兩層語言

對 total moves，使用：

$$
G\curvearrowright X.
$$

非常自然。

對 partial moves，更自然的是把合法 states 當 objects、合法 reversible transitions 當 arrows。

若：

$$
s\xrightarrow{a}s',
$$

就是一個 arrow。

每個 arrow 有 inverse。

可合成的 arrows 依路徑合成。

這具有 groupoid-like 結構。

本文不要求第一版 runtime 實作完整 category / groupoid library，但規格語言不能假裝所有 puzzle 都是 everywhere-defined group action。

---

## 24. 這仍然是「傳統問題」

即使 move availability 依 state，

只要：

- rule fixed；
- goal fixed；
- transition law fixed；
- environment 不主動改變；

它仍是一個 static finite puzzle。

因此：

$$
\boxed{
\text{state-dependent legality}
\neq
\text{dynamic rules}.
}
$$

這個邊界留到第十篇再次封閉。

---

## 25. PuzzleSpec v0

本文提出：

```text
TwistyPuzzleSpec
  id
  name
  orbits
  defaultPattern
  primitiveMoves
  derivedMoves
  goal
  metric
  notation
  legalityModel
  capabilityHints
  geometryAdapters
  provenance
  version
```

這是系列後續實作的核心規格。

---

## 26. OrbitSpec

```text
OrbitSpec
  id
  pieceCount
  orientationModulus
  labels
  indistinguishability
  displayRole
```

`indistinguishability` 是重要欄位。

某些 puzzle pieces 在外觀上可能不可區分，但 algebraic model 仍可選擇把它們標記成 distinguishable pieces，再由 goal / representation 層商掉。

---

## 27. Indistinguishable pieces

若 pieces：

$$
p_i,p_j
$$

在 puzzle goal 上不可區分，則 physical solved equivalence 可能比 labeled algebraic state 更粗。

因此：

$$
\text{labeled state count}
$$

可能大於：

$$
\text{visually distinct state count}.
$$

solver 與 UI 都必須知道正在使用哪個 quotient。

不能只說：

> 這顆 puzzle 有 $N$ states

卻不說 pieces 是否被視為 distinguishable。

---

## 28. Orientation convention

orientation 不只需要 modulus：

$$
m_i.
$$

還需要 convention。

同一 physical orientation 可能因 reference frame 定義不同而得到不同數值。

所以 OrbitSpec / RepresentationSpec 應保存：

```text
orientationConventionId
```

並要求 move transformations 與 parser 使用同一 convention。

---

## 29. Facelets 不再是 canonical 必需品

某些 puzzle 有：

- tiles；
- stickers；
- uncolored pieces；
- shape cues；
- orientation marks。

因此 generalized core 不應要求：

$$
\mathcal C^{N}
$$

facelet array 一定存在。

Facelet representation 只是 optional adapter：

$$
R_{\mathrm{facelet}}.
$$

---

## 30. Flat Net 也不再是 canonical 必需品

FCSR 起源來自 flat net。

但 generalized FCSR 應允許：

$$
R_{\mathrm{flat}}
=
\varnothing.
$$

若 puzzle 沒有自然、清晰、保結構的 2D net，就不要硬做。

第八篇已指出 modern viewer 也存在部分 puzzle 無 $2D$ visualization 的情況。

因此：

$$
\boxed{
\text{FCSR origin is flat;
FDRS generalization is representation-selective}.
}
$$

---

## 31. Graph view 是更一般的 fallback

如果沒有 natural flat geometry，可以使用：

$$
R_{\mathrm{graph}}:
X
\rightarrow
\mathcal G.
$$

graph 可以表示：

- piece adjacency；
- orbit membership；
- move incidence；
- state transitions；
- constraint structure。

因此 generalized viewer 至少可以保有抽象 graph representation。

---

## 32. Solver capability 不應假設 universal

定義 solver capability：

```text
SolverCapability
  requiresTotalMoves
  supportsPartialMoves
  requiresUnitCost
  supportsWeightedMetric
  requiresGroupAction
  supportsMultipleGoals
  requiresCoordinates
  supportsPDB
  proofLevel
```

某個 Two-Phase solver 可能只支援：

$$
3\times3\times3.
$$

這不是 bug。

只要 capability declaration 清楚。

---

## 33. Capability negotiation

給 puzzle：

$$
\mathcal P
$$

與 solver：

$$
S,
$$

系統計算：

$$
\operatorname{Compatible}(S,\mathcal P).
$$

若 false，不應讓 UI 顯示一個會 crash 的：

```text
Solve
```

按鈕。

而應顯示：

```text
Solver unavailable
reason: requires total move action
```

或：

```text
reason: no compatible heuristic representation
```

---

## 34. Heuristic capability

heuristic 也需要 capability：

```text
HeuristicCapability
  puzzleSpecId
  representation
  metric
  admissible
  consistent
  stateDomain
```

PDB：

$$
h
$$

若是在 HTM 建構，就不能直接被當成 QTM lower bound 使用，除非另有證明。

因此 metric 也是 heuristic certificate 的一部分。

---

## 35. Search Kernel generalized interface

第四篇的：

$$
\mathcal Q
=
(X,A,T,G,c,h)
$$

現在改成由 PuzzleSpec 生成。

對 total puzzle：

$$
A(x)=A.
$$

對 constrained puzzle：

$$
A(x)
=
\{a:\operatorname{Enabled}(x,a)\}.
$$

所以 BFS、A*、IDA* 本身不必知道 puzzle 是 cube、dodecahedron 或其他 polyhedron。

它只需要：

```text
successors(state)
goal(state)
cost(edge)
heuristic(state)
```

---

## 36. Verification Kernel generalized interface

第七篇的 checker 同樣泛化：

$$
\operatorname{checkSolution}_{\mathcal P}(s,p).
$$

它逐步檢查：

1. move token 是否解析；
2. move 是否 enabled；
3. transition 是否合法；
4. final goal 是否成立。

因此 partial-move puzzle 的 certificate checker 會比 total group puzzle 多一個：

$$
\operatorname{Enabled}
$$

驗證。

---

## 37. Legal-state verification 的兩種模式

### Constructive

若 state 是由：

$$
x_\star
$$

重播合法 move sequence 得到，legality 自帶 witness。

### Imported state

若使用者從 UI / scanner 直接輸入 state，則需要 puzzle-specific validator。

因此：

```text
StateProvenance
  DerivedFromSolved(path)
  ParsedAndValidated(certificate)
  UnverifiedImport
```

可以成為 canonical metadata。

---

## 38. Geometry-derived puzzle spec

當代 `PuzzleGeometry` 類工具展示了一個很有價值的方向：

$$
\text{Puzzle Geometry Description}
\rightarrow
\text{Orbits / Moves / Permutations / 3D / SVG}.
$$

其 API 可產生：

- `getKPuzzleDefinition`；
- `getMovesAsPerms`；
- `get3d`；
- `generatesvg`。

這說明 geometry compiler 可以作為 PuzzleSpec generator。

但生成結果仍應經：

$$
\text{semantic validation}
$$

後才進 canonical registry。

---

## 39. Algebra-derived geometry

反方向也可以：

$$
\text{PuzzleSpec}
\rightarrow
\text{GeometryAdapter}.
$$

若已有：

- orbits；
- moves；
- labels；

可以再指定：

- piece meshes；
- axes；
- cuts；
- sticker maps；

形成可視化。

所以 geometry 與 algebra 之間是雙向工具鏈，而不是單一依賴關係。

---

## 40. Polyhedral puzzle

對 polyhedron：

$$
P=(V,E,F),
$$

可以以：

- face；
- edge；
- vertex；

作為 geometric features。

但 piece orbits 不必和：

$$
V,E,F
$$

一一相等。

不同 cutting scheme 會產生不同 pieces 與 move groups。

因此：

$$
\boxed{
\text{same base polyhedron}
\neq
\text{same twisty puzzle}.
}
$$

---

## 41. Turning type 應是 geometry metadata

Face-turning、edge-turning、vertex-turning 是人類非常有用的分類。

所以可保存：

```text
turningType:
  face
  edge
  vertex
  hybrid
  custom
```

但 canonical move semantics 仍由：

$$
M_a
$$

決定。

分類標籤不取代 transformation data。

---

## 42. 從 Platonic solids 到更一般 map

傳統 twisty polyhedra 常建立在：

- tetrahedron；
- cube；
- octahedron；
- dodecahedron；
- icosahedron；

等幾何上。

但 generalized Rubik-like mathematics 不必停在五種 Platonic solids。

Mathieu Dutour Sikirić 的工作把 Rubik-like move group 泛化到任意 $3$ -valent map，並研究相應群的大小上界。

這說明：

$$
\boxed{
\text{Rubik-like combinatorics}
}
$$

可以由：

$$
\text{map / incidence structure}
$$

而不只由實體 cube geometry 驅動。

---

## 43. Map-based puzzle spec

更抽象時，可讓：

$$
\mathcal M
$$

為 combinatorial map。

定義：

- cells；
- adjacency；
- local rotations；
- move generators。

再生成：

$$
\mathcal P(\mathcal M).
$$

這為未來程序生成陌生 twisty puzzle 留下數學入口。

---

## 44. 程序生成 puzzle

如果 PuzzleSpec 已抽象化，就可以生成：

```text
GeneratePuzzle(seed)
  -> orbits
  -> moves
  -> goal
  -> geometry optional
```

然後驗證：

- moves 可逆；
- solved state well-defined；
- legal component finite；
- puzzle 非平凡；
- goal reachable。

這比只收藏現有商品 puzzle 更接近 AI benchmark。

但程序生成仍屬後續工程，不是本文 immediate implementation requirement。

---

## 45. Puzzle identity 與 version

PuzzleSpec 必須 versioned。

例如：

```text
puzzleId: megaminx-standard
specVersion: 1.0.0
notationVersion: 1
metricVersion: htm-like-1
```

因為 certificate：

$$
p
$$

只有在 move semantics 固定時才可重播。

---

## 46. PuzzleSpec fingerprint

定義 canonical serialization：

$$
\operatorname{Ser}(\mathcal P).
$$

再取：

$$
H_{\mathcal P}
=
\operatorname{SHA256}
(
\operatorname{Ser}(\mathcal P)
).
$$

SolutionCertificate 保存：

$$
H_{\mathcal P}.
$$

這保證 verifier 知道自己正在用哪一份 puzzle ruleset。

注意 checksum 驗證的是 spec identity，不是數學正確性。

---

## 47. Derived representation registry

每個 PuzzleSpec 可註冊：

$$
\mathcal R_{\mathcal P}
=
\{R_1,\ldots,R_k\}.
$$

可能包括：

- 3D；
- flat；
- orbit table；
- facelet；
- coordinate；
- symmetry；
- search graph；
- proof view。

不是所有 puzzle 都有全部 representations。

---

## 48. CapabilityProfile

定義：

```text
CapabilityProfile
  totalMoveAction
  partialMoveAction
  geometry3D
  geometry2D
  faceletView
  orbitView
  coordinateView
  symmetryData
  exactLegalityChecker
  solverIds
  heuristicIds
  formalProofLevel
```

UI 根據 capability 自動組合，而不是每顆 puzzle 手寫頁面。

---

## 49. $2\times2\times2$ 作為第二個實例

 $2\times2\times2$ 沒有 edge orbit 與固定 face centers。

它可以測試：

> 我們的 core 是否真的沒有偷偷依賴 $12$ edges？

Orbit 主要是：

$$
O_c
$$

with：

$$
n_c=8,
\quad
m_c=3.
$$

這是 generalized core 的第一個 regression puzzle。

---

## 50. $3\times3\times3$ 作為 reference instance

 $3\times3\times3$ 保留：

$$
O_c:
(8,3),
$$

$$
O_e:
(12,2).
$$

若追蹤 centers：

$$
O_z
$$

可依 representation / supercube requirement 決定 orientation semantics。

它是目前 proof / solver / visualization 功能最完整的 reference implementation。

---

## 51. $4\times4\times4$ 作為 orbit stress test

 $4\times4\times4$ 引入：

- additional centers；
- paired wing-like edge pieces；
- inner slice moves；
- 不同 parity phenomena。

這能測試：

- 多 orbit；
- derived piece grouping；
- solver capability；
- representation scalability。

因此它比單純把 $N$ 改成 $4$ 更有價值。

---

## 52. Pyraminx / Skewb 作為 turning-axis stress test

這類 puzzle 可以測試：

> runtime 是否仍把 move 當 cube face turn？

如果核心只接受：

```text
face: U/D/L/R/F/B
```

立即失敗。

正確核心只接受：

$$
\operatorname{MoveId}.
$$

geometry adapter 才解釋其實體轉軸。

---

## 53. Megaminx 作為 non-cubic polyhedron stress test

Megaminx 測試：

- dodecahedral geometry；
- 更多 face axes；
- 更大 notation set；
- 多面 flat visualization；
- UI scaling。

若 FCSR 仍只能畫十字 net，就代表第八篇的 generalized viewer 尚未完成。

---

## 54. Icosahedral puzzle 作為高面數 stress test

二十面體或相關 twisty puzzle 特別適合原始研究動機：

> 當面數與局部關係增加時，不同 observer representations 的可理解性如何變化？

這裡 FDRS 的 representation-selection 實驗比「人類背公式」更有價值。

---

## 55. 多 puzzle benchmark 不應只比解速

定義 benchmark vector：

$$
B(\mathcal P,S)
=
(
C_{\mathrm{solve}},
M,
N_{\mathrm{exp}},
L,
V,
P
).
$$

其中：

- $C_{\mathrm{solve}}$：計算時間；
- $M$：記憶體；
- $N_{\mathrm{exp}}$：展開節點；
- $L$：解長；
- $V$：verification coverage；
- $P$：representation / visualization coverage。

如此更符合本系列目標。

---

## 56. Puzzle complexity profile

對 puzzle：

$$
\mathcal P,
$$

不只報：

$$
|X_{\mathrm{legal}}|.
$$

還可報：

- orbit count；
- generator count；
- move orders；
- state-dependent move ratio；
- symmetry group size；
- average effective branching；
- known diameter / bound；
- representation cardinalities；
- heuristic availability。

這比單一 state count 更能描述計算形狀。

---

## 57. FDRS representation experiment generalized

對同一 puzzle：

$$
\mathcal P,
$$

比較：

$$
R_1,\ldots,R_k.
$$

測：

$$
C_{\mathrm{search}}
(
\mathcal P,R_i,A,h
).
$$

再跨 puzzle：

$$
\mathcal P_1,\ldots,\mathcal P_m.
$$

可以研究：

$$
\boxed{
\text{哪一類 representation 對哪一類 twisty structure 最有效？}
}
$$

這已經從「魔方技巧」提升成 representation engineering。

---

## 58. FDRS 不預設低維必勝

某個 Megaminx 或高面數 puzzle 的最佳 solver representation 可能：

- 不是 2D；
- 不是 geometry；
- 是 orbit coordinate；
- 是 quotient graph；
- 是 mixed representation。

所以 generalized principle 是：

$$
\boxed{
\text{選最適任務表示，而不是固定追求最低幾何維度}.
}
$$

這是 2025 起源論述經過九篇重建後最重要的修正之一。

---

## 59. Formalization strategy

Lean 不應先形式化所有現存 puzzle。

先形式化 generic kernel：

```text
OrbitSpec
MoveTransformation
PuzzleSpec
State
applyMove
applyMoves
Goal
Solves
```

再做 instances：

```text
Cube2
Cube3
```

之後逐步增加其他 puzzle。

---

## 60. Generic total-move theorem

若：

$$
a
$$

的每個 orbit transformation 都是 permutation + orientation update，且具有 inverse：

$$
a^{-1},
$$

則：

$$
T_{a^{-1}}(T_a(s))=s.
$$

這個 theorem 可在 generic orbit kernel 證一次。

所有 total-move puzzle instances 自動繼承。

---

## 61. Generic partial-move theorem

對 partial puzzle：

若：

$$
\operatorname{Enabled}(s,a)
$$

且：

$$
T(s,a)=s',
$$

要求：

$$
\operatorname{Enabled}(s',a^{-1})
$$

以及：

$$
T(s',a^{-1})=s.
$$

這成為 constrained static puzzle 的 reversible-transition contract。

---

## 62. Generic solution checker

對任意 PuzzleSpec：

$$
\operatorname{checkSolution}_{\mathcal P}(s,p)
$$

逐步：

1. 檢查 move token；
2. 檢查 enabled；
3. apply transition；
4. 最後檢查 goal。

其 soundness theorem 可通用證明一次：

$$
\boxed{
\operatorname{checkSolution}_{\mathcal P}(s,p)=\mathrm{true}
\Rightarrow
\operatorname{Solves}_{\mathcal P}(s,p).
}
$$

這是第七篇架構向 multi-puzzle 的最重要升級。

---

## 63. Generic visualization contract

對可用 representation：

$$
R_i^{\mathcal P},
$$

要求：

$$
R_i^{\mathcal P}(T(s,a))
=
\widetilde T_{i,a}^{\mathcal P}
(
R_i^{\mathcal P}(s)
).
$$

所以第八篇同步框架也可以 generic 化。

---

## 64. Generic search contract

第四篇的：

$$
\mathcal Q
=
(X,A,T,G,c,h)
$$

由：

$$
\mathcal P
$$

與：

$$
R
$$

共同生成：

$$
\mathcal Q(\mathcal P,R).
$$

搜尋器因此不需要知道：

> 這是一顆五魔方還是十二面體。

只需要其 search contract。

---

## 65. 產品層：Puzzle Gallery 不是固定頁面集合

未來 UI 可以讀 registry：

```text
PuzzleRegistry
  cube2
  cube3
  cube4
  pyraminx
  skewb
  megaminx
  ...
```

點入 puzzle 後由 CapabilityProfile 自動組合：

- view tabs；
- solver buttons；
- proof panels；
- available metrics；
- notation help。

這比每顆 puzzle 寫一套 app 更可維護。

---

## 66. Import / export

通用 artifact：

```text
puzzle-spec.json
state.json
algorithm.txt
solution-certificate.json
verification-report.json
```

若有 geometry：

```text
geometry.json
mesh/*
```

若有 heuristic：

```text
pdb/*
heuristic-metadata.json
```

這為之後整包 ZIP 與研究資料庫留下標準。

---

## 67. Canonical source 與 renderer 分離

正式規格必須保存：

$$
\operatorname{PuzzleSpec}.
$$

HTML viewer、3D renderer、SVG 只是 rendering artifacts。

因此：

$$
\boxed{
\text{viewer is not the canonical puzzle definition}.
}
$$

這也避免未來只能從網頁程式逆向提取 puzzle rules。

---

## 68. 外部規格 adapter

cubing.js 的 `KPuzzleDefinition` 可以作為 import / export adapter。

它目前包含：

- `name`；
- `orbits`；
- `defaultPattern`；
- `moves`；
- optional `derivedMoves`。

這和本文 Orbit-first spec 高度相容。

但 FCSR `TwistyPuzzleSpec` 還需額外保存：

- goal；
- metric；
- legality model；
- proof metadata；
- capability profile；
- version / fingerprint。

所以不是直接等同。

---

## 69. PuzzleGeometry adapter

`PuzzleGeometry` 目前能：

- 產生 SVG；
- 產生 3D sticker geometry；
- 產生 permutations；
- 產生 KPuzzle definition；
- 產生 scramble / solved permutation；
- 輸出其他數學工具格式。

因此它可以作為：

$$
\boxed{
\text{geometry compiler / importer}
}
$$

而不是 FCSR canonical solver core。

---

## 70. 研究邊界：通用規格不等於通用 solver

建立：

$$
\operatorname{TwistyPuzzleSpec}
$$

不代表立刻存在：

$$
\operatorname{UniversalOptimalSolver}.
$$

通用規格解決的是：

> 系統能否精確描述、重播、驗證、可視化與交給 solver？

不是：

> 所有 puzzle 都能同樣快地最短求解。

所以：

$$
\boxed{
\text{Universal Representation Layer}
\neq
\text{Universal Efficient Solver}.
}
$$

---

## 71. 本文核心命題

### 命題 G-A： $3\times3\times3$ 應成為 spec instance

而不是核心型別。

### 命題 G-B：Orbit 是比 cube face 更一般的 canonical state primitive

$$
X_i
\cong
S_{n_i}
\ltimes
\mathbb Z_{m_i}^{n_i}.
$$

### 命題 G-C：Legal state 最一般地由 reachable component 定義

$$
X_{\mathrm{legal}}
=
\operatorname{Reach}(x_\star).
$$

### 命題 G-D：Static puzzle 可以有 state-dependent enabled moves

$$
A(s)
$$

不必為常數。

### 命題 G-E：State-dependent legality 不等於 Dynamic Rules

只要：

$$
A(\cdot)
$$

本身固定。

### 命題 G-F：Geometry 是 optional adapter

不是 canonical semantics。

### 命題 G-G：Solver / heuristic / visualization 都應 capability-negotiated

而不是假設 universal。

### 命題 G-H：Generic certificate checker 可以跨 puzzle 重用

只要 PuzzleSpec 提供 canonical transition 與 goal semantics。

---

## 72. 結論

本文完成經典系列從：

$$
\text{Rubik's Cube}
$$

到：

$$
\boxed{
\text{Twisty Puzzle}
}
$$

的正式抽象化。

通用 puzzle 不再由：

$$
6\text{ faces}
+
54\text{ stickers}
$$

定義。

而由：

$$
\boxed{
\text{Orbits}
+
\text{Orientations}
+
\text{Moves}
+
\text{Legality}
+
\text{Goal}
+
\text{Metric}
+
\text{Notation}
+
\text{Optional Geometry}.
}
$$

對 total reversible puzzles，可使用：

$$
G\curvearrowright X.
$$

對固定規則但 move availability 依 state 的 constrained puzzles，可使用：

$$
T:
X\times A
\rightharpoonup
X.
$$

兩者都仍屬：

$$
\boxed{
\text{Static Twisty Computation}.
}
$$

因為規則、目標與 transition law 本身沒有在遊戲過程中外生改變。

這一區分非常重要。

它讓我們在下一篇可以精確回答：

> 經典 twisty puzzle 的「靜態」究竟意味著什麼？

也讓後續 Dynamic Cube 不需要靠「亂加會變的規則」來定義，而可以嚴格寫出：

$$
\boxed{
\text{何時 stationary puzzle specification 被解除。}
}
$$

到第九篇，FCSR 的原始魔方已不再是一個被丟棄的玩具例子。

它變成了一條完整抽象鏈的起點：

$$
\boxed{
\text{Cube}
\rightarrow
\text{Canonical State}
\rightarrow
\text{Representation}
\rightarrow
\text{Search}
\rightarrow
\text{Verification}
\rightarrow
\text{TwistyPuzzleSpec}.
}
$$

下一篇將封頂本系列：

**《經典域封頂：Static Twisty Computation 的邊界與 Dynamic Cube 的前置條件》**。

---

## 參考資料與來源定位

### 起源與系列內部

- [F2025-A] Neo.K，《展平式維度重構理論：完整數學架構與概念解析》。
- [F2025-B] Neo.K，《展平式維度重構理論：從 FCSR 到 FDRS 的完整數學架構》。
- [CUBE-01] 至 [CUBE-08]：本系列前八篇。

### 當代工程基線

- [R1] cubing.js, `KPuzzleDefinition` API reference。其結構包含 `name`、`orbits`、`defaultPattern`、`moves` 與 optional `derivedMoves`。
- [R2] cubing.js, `PuzzleGeometry` API reference。其功能包含 SVG、3D geometry、permutations、KPuzzle definition 與其他 puzzle-geometry 輸出。
- [R3] cubing.js, `TwistyPlayer` documentation。作為多 puzzle playback 與 optional 2D visualization 的現代 viewer 基線。

### 數學泛化基線

- [R4] Mathieu Dutour Sikirić, **A variation on the Rubik's cube**, 2020。將 Rubik-like puzzle group 泛化到任意 $3$ -valent map，研究對應群大小上界。

---

## 版本註記

v0.1 首次將 FCSR/FDRS 魔方線提升成通用 `TwistyPuzzleSpec`，並明確區分 total group-action puzzles 與 fixed-rule partial reversible puzzles。

本文保留「state-dependent enabled moves」在 Static Twisty Computation 內，將真正 Dynamic Cube 留給規則、目標、transition law 或外部環境本身發生時間性變化的後續系列。

後續第十篇：

**《經典域封頂：Static Twisty Computation 的邊界與 Dynamic Cube 的前置條件》**。
