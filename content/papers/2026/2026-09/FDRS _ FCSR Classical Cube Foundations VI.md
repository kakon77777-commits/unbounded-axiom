# FDRS / FCSR Classical Cube Foundations VI
## Two-Phase 與子群分解：經典高效魔方求解的結構化路徑

**英文題名：** Two-Phase and Subgroup Decomposition: A Structured Path to Efficient Classical Cube Solving  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-06  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第六篇

---

## 摘要

前五篇已建立合法魔方狀態、表示與座標、搜尋語義、admissible heuristic、Pattern Database 與 pruning safety。本文第一次把這些元件組合成一個完整且具有工程代表性的經典高效 solver 架構：Herbert Kociemba 的 Two-Phase Algorithm。

Two-Phase 的核心不是把一條解序列任意切成兩半，而是把原始單一目標 $s_\\star$ 改寫成一個中間結構目標：

$$
G_1=\\langle U,D,R^2,L^2,F^2,B^2\\rangle.
$$

Phase 1 從任意合法狀態搜尋到子群 $G_1$ ；Phase 2 僅在 $G_1$ 允許的 move set 內搜尋 solved state。對標準 Kociemba 架構，進入 $G_1$ 等價於 corner orientation 歸零、edge orientation 歸零，且四個 UD-slice edges 回到 UD slice。於是 Phase 1 可以只追蹤 orientation 與 slice membership，而 Phase 2 再處理剩餘排列自由度。

這種設計的真正價值可以寫成：

$$
\\text{Full Goal Search}
\\rightarrow
\\text{Reach Structured Subgroup}
\\rightarrow
\\text{Solve Inside Subgroup}.
$$

Kociemba 的技術說明指出，Phase 1 的原始 coordinate state count 為

$$
3^7\\cdot2^{11}\\cdot\\binom{12}{4}
=2{,}217{,}093{,}120,
$$

Phase 2 約有

$$
19{,}508{,}428{,}800
$$

個狀態；藉由 coordinate encoding、move tables、symmetry reduction 與 pruning tables，兩個巨大子問題都能被 IDA* 有效處理。現行技術說明給出的 phase depth 上界分別為 $12$ 與 $18$，因此第一個標準 two-phase solution 至多 $30$ moves；然而 Two-Phase 的設計目標是快速得到短解，而不是保證全域最短。實作甚至會繼續探索較長的 Phase 1 路徑，以交換更短的 Phase 2，藉此縮短總解長。

本文從 FCSR/FDRS 角度重新解讀此結構：Phase 1 不是「先解一部分色塊」，而是把完整狀態投影到一個任務充分的 quotient / coordinate domain，尋找一個可由低維條件描述的結構正常形；Phase 2 才在這個受限軌道中完成剩餘自由度。這提供了一個比幾何 $3D\\rightarrow2D$ 更強的起源延伸：表示轉換、子群分解與搜尋目標重寫可以共同改變一個有限狀態問題的計算形狀。

本文最後提出 `PhaseSpec`、`PhaseHandoff` 與 compositional solver correctness。若 Phase 1 證明其輸出確實落在 $G_1$，Phase 2 證明從該狀態到 solved state，則兩段 move sequence 的串接必然是一個完整合法解。這將直接成為下一篇 verified solver 的前置規格。

**關鍵詞：** Kociemba、Two-Phase、subgroup、coset、coordinate、IDA*、pruning table、phase handoff、FCSR、FDRS、structured search

---

## 1. Two-Phase 不是「解一半，再解另一半」

若完整魔方群為：

$$
G=\\langle U,D,L,R,F,B\\rangle,
$$

solved state 對應 identity $e$。最直接的求解問題是：

$$
g\\rightsquigarrow e.
$$

Two-Phase 不直接把這條路徑均勻分成兩段，而是先選一個特別的子群：

$$
G_1=\\langle U,D,R^2,L^2,F^2,B^2\\rangle.
$$

然後把問題改寫成：

$$
g\\rightsquigarrow G_1\\rightsquigarrow e.
$$

因此 Phase 1 的 goal 是集合 $G_1$，而不是單一 solved state。這就是 Two-Phase 最重要的結構性轉換。

---

## 2. 歷史位置：從多子群到單一中間子群

Thistlethwaite 類方法沿多個逐步縮小的子群求解。Kociemba 在 1991--1992 年發展 Two-Phase 時，將中間層級大幅減少，只保留一個主要中間子群 $G_1$。

減少 phase 數量可以縮短整體解長，但會讓每一個 phase 本身變得更大、更難。因此 Two-Phase 的工程突破不是單純「少做幾個階段」，而是配套加入：

$$
\\text{coordinate encoding}
+
\\text{move tables}
+
\\text{pruning tables}
+
\\text{IDA*}.
$$

它是結構分解與計算工程共同成立的結果。

---

## 3. Phase 1 的結構目標

Phase 1 的目標是：

$$
s_1\\in G_1.
$$

對標準 cubie / coordinate convention，這可以用三組條件刻畫。

### 3.1 Corner orientation 歸零

$$
\\operatorname{Twist}(s_1)=0.
$$

### 3.2 Edge orientation 歸零

$$
\\operatorname{Flip}(s_1)=0.
$$

### 3.3 UD-slice membership 歸位

四個屬於中層 slice 的 edges $FR,FL,BL,BR$ 必須回到 UD slice 的四個位置集合中。只要求它們位於正確 slice，不要求四顆彼此 permutation 已完成。

令：

$$
\\operatorname{Slice}(s_1)=0.
$$

則 Phase 1 goal predicate 可以寫成：

$$
\\Phi_1(s)
=
(\\operatorname{Twist}(s),\\operatorname{Flip}(s),\\operatorname{Slice}(s)).
$$

進入 $G_1$ 對應：

$$
\\Phi_1(s)=(0,0,0).
$$

所以 Phase 1 不是問「還有多少步 solved」，而是問「還有多少步進入一個結構受限的正常形」。

---

## 4. Phase 1 coordinate 空間

corner orientation 有：

$$
3^7=2187
$$

種。

edge orientation 有：

$$
2^{11}=2048
$$

種。

四個 UD-slice edges 在十二個 edge positions 中的 membership 有：

$$
\\binom{12}{4}=495
$$

種。

因此 raw phase-1 coordinate tuple 的狀態數為：

$$
2187\\cdot2048\\cdot495
=2{,}217{,}093{,}120.
$$

這不是完整魔方的 $43{,}252{,}003{,}274{,}489{,}856{,}000$ 個 legal states；大量 Phase 1 不關心的 permutation 細節已被商掉。

---

## 5. FDRS 角度：Phase 1 是 task-sufficient quotient

第三篇已定義 task-reduced representation：

$$
R:\\mathcal S\\rightarrow X.
$$

對 Phase 1，可以令：

$$
R_1=\\Phi_1.
$$

存在大量 $s_a\\neq s_b$，卻有：

$$
R_1(s_a)=R_1(s_b).
$$

這些狀態的完整 permutation 不同，但若它們具有相同 corner orientation、edge orientation 與 UD-slice membership，Phase 1 可以把它們視為同一類。

所以 Phase 1 的計算核心是：

$$
\\boxed{
\\text{Full State}
\\rightarrow
\\text{Phase-1 Equivalence Class}
}.
$$

這正是 FDRS 起源線中「表示改變計算形狀」的成熟案例。

---

## 6. Phase 1 的 move set

Phase 1 仍可使用完整 $18$ -move alphabet：

$$
U,U',U^2,
D,D',D^2,
L,L',L^2,
R,R',R^2,
F,F',F^2,
B,B',B^2.
$$

因為任務是：

$$
G\\rightarrow G_1.
$$

搜尋器依 coordinate move tables 更新 $R_1(s)$，不必每一步都重新操作完整 facelet 圖。

---

## 7. Phase 1 pruning table

現行 Kociemba 技術說明使用 FlipUDSlice sym-coordinate 與 corner twist raw-coordinate。

FlipUDSlice 利用對稱性後具有：

$$
64{,}430
$$

個 equivalence classes。

corner twist 有：

$$
2187
$$

個 raw cases。

因此 Phase 1 pruning table entries 為：

$$
64{,}430\\cdot2187
=140{,}908{,}410.
$$

其 maximal pruning depth 為：

$$
12.
$$

此 table 提供進入 $G_1$ 所需 move 數的 lower bound。

---

## 8. Phase 1 的最大深度

Kociemba 的技術說明指出：

$$
d_1^{\\max}=12.
$$

也就是任意合法 cube state 都可以在至多 $12$ 個 Phase 1 moves 內進入 $G_1$。

這不是說任意魔方 $12$ 步就能 solved，而只是：

$$
g\\rightsquigarrow G_1
$$

的 phase-specific 上界。

---

## 9. Phase Handoff

設 Phase 1 回傳 $p_1$，定義：

$$
s_1=T^\\ast(s_0,p_1).
$$

handoff contract 必須驗證：

$$
s_1\\in G_1.
$$

等價地，在所採 coordinate convention 下：

$$
\\Phi_1(s_1)=(0,0,0).
$$

只有通過此驗證後，Phase 2 才可接受 $s_1$。

因此：

$$
\\boxed{
\\text{Phase transition is a verified state boundary}.
}
$$

---

## 10. Phase 2 的 move restriction

一旦 $s_1\\in G_1$，Phase 2 只使用生成 $G_1$ 的 moves：

$$
U,U',U^2,
D,D',D^2,
R^2,L^2,F^2,B^2.
$$

共 $10$ 種 move variants。

側面 $R,L,F,B$ 不再允許 quarter turn，只允許 half turn。如此所有 Phase 2 中間狀態都留在 $G_1$。

---

## 11. Phase 2 move closure

對所有 Phase 2 moves $a$，都要求：

$$
T_a(G_1)\\subseteq G_1.
$$

這可從 subgroup generation 直接理解，也可以在 cubie invariant 層驗證：已歸零的 orientation 與 UD-slice membership 不會被 Phase 2 move set 破壞。

這是 Phase 2 能把搜尋限制在較小封閉域內的關鍵。

---

## 12. Phase 2 的剩餘問題

進入 $G_1$ 後：

- corner orientation 已解；
- edge orientation 已解；
- slice membership 已解。

剩餘主要是 permutation completion。

Phase 2 需處理：

$$
\\operatorname{CornerPerm},
$$

$$
\\operatorname{EdgePerm}_8,
$$

以及：

$$
\\operatorname{UDSlicePerm}.
$$

所以完整問題已從 orientation + slice + permutation，縮成受限的 permutation completion inside $G_1$。

---

## 13. Phase 2 狀態數

Kociemba 技術說明給出的 Phase 2 position count 約為：

$$
19{,}508{,}428{,}800.
$$

雖然仍然巨大，但：

- move set 從 $18$ 降到 $10$ ；
- orientations 已固定；
- slice membership 已固定；
- 可用 phase-specific coordinates；
- 可建立 pruning tables；
- 可利用 symmetry。

所以其搜尋圖已與原完整魔方圖非常不同。

---

## 14. Phase 2 coordinates

corner permutation raw coordinate 有：

$$
8!=40320
$$

種。

UD-slice 中四個 edges 的 permutation 有：

$$
4!=24
$$

種。

其餘八個 edges 的 permutation 有：

$$
8!=40320
$$

種，再受整體合法 parity 關係約束。

---

## 15. Phase 2 pruning table

現行 Kociemba 說明使用 Corner Permutation sym-coordinate 與 Edge Permutation raw-coordinate。

corner permutation 經 symmetry reduction 後有：

$$
2768
$$

個 equivalence classes。

edge permutation 有：

$$
40320
$$

個 raw cases。

因此 Phase 2 pruning table entries 為：

$$
2768\\cdot40320
=111{,}605{,}760.
$$

其 maximal pruning depth 為：

$$
18.
$$

此 table 的語義是 Phase 2 受限 move domain 中到 solved state 的 lower bound。

---

## 16. Two-Phase 的第一個解上界

若 Phase 1 最多 $12$ 步，Phase 2 最多 $18$ 步，則：

$$
12+18=30.
$$

所以第一個標準 two-phase solution 有：

$$
\\boxed{|p_1|+|p_2|\\leq30}.
$$

這是一個 practical bound，但不是 God's Number。標準 HTM God's Number 為 $20$。

---

## 17. 為什麼 Two-Phase 常得到比 $30$ 短很多的解

最短的 Phase 1 路徑不一定產生最短的總解。

可能第一個 boundary candidate 為：

$$
|p_1|=10,
\\qquad
|p_2|=12,
$$

總長：

$$
22.
$$

但另一條稍長的 Phase 1：

$$
|p'_1|=11
$$

可能進入一個更適合 Phase 2 的 $s'_1\\in G_1$，使：

$$
|p'_2|=5,
$$

總長只有：

$$
16.
$$

因此 Two-Phase 會繼續探索 suboptimal Phase-1 solutions，並為不同 boundary candidates 計算 Phase 2。

---

## 18. Boundary-state optimization

令 boundary set：

$$
B=G_1.
$$

Two-Phase 的結構化總成本可以寫成：

$$
C(s_0)
=
\\min_{b\\in B}
\\left[
 d_G(s_0,b)
 +
 d_{G_1}(b,e)
\\right].
$$

這個式子揭示：真正要選的不是「最短 Phase 1」，而是「哪個 boundary state 的總成本最低」。

因此：

$$
\\boxed{
\\text{shortest Phase 1}
\\neq
\\text{shortest total two-phase path}
}
$$

一般成立。

---

## 19. Two-Phase 不等於全域 optimal solver

完整問題的 optimal distance 是：

$$
d_G(s_0,e).
$$

標準快速 Two-Phase 的目標是迅速取得短解，而不是證明輸出等於 $d_G(s_0,e)$。

Kociemba 的現行技術說明更指出，為提高性能，實作會丟棄某些 Phase-1 suboptimal candidates；這種策略雖有利於實務速度，卻使該流程不適合拿來證明某一 maneuver 全域 optimal。

因此 API 應區分：

```text
TwoPhaseShortSolution
OptimalSolution
OptimalityUnknown
```

---

## 20. Soundness 與 optimality 分離

即使 Two-Phase 不是 God's Algorithm，只要輸出：

$$
p=p_1\\mathbin{+\\!\\!+}p_2
$$

並滿足：

$$
T^\\ast(s_0,p_1)=s_1\\in G_1,
$$

以及：

$$
T^\\ast(s_1,p_2)=e,
$$

就能推出：

$$
T^\\ast(s_0,p)=e.
$$

因此：

$$
\\boxed{
\\text{Two-Phase can be sound without being globally optimal}.
}
$$

---

## 21. Compositional correctness theorem

定義：

$$
\\operatorname{Phase1Correct}(s_0,p_1)
$$

當且僅當：

$$
T^\\ast(s_0,p_1)\\in G_1.
$$

定義：

$$
\\operatorname{Phase2Correct}(s_1,p_2)
$$

當且僅當：

$$
s_1\\in G_1
$$

且：

$$
T^\\ast(s_1,p_2)=e.
$$

則由兩者推出：

$$
T^\\ast
\\left(
 s_0,
 p_1\\mathbin{+\\!\\!+}p_2
\\right)
=e.
$$

這就是 Two-Phase 的 compositional soundness theorem。

---

## 22. Phase completeness

理想化 Two-Phase solver 可以分別要求：

### Phase 1 completeness

對任意合法 $s\\in G$，存在 $p_1$ 使：

$$
T^\\ast(s,p_1)\\in G_1.
$$

### Phase 2 completeness

對任意 $s_1\\in G_1$，存在 Phase 2 move sequence $p_2$ 使：

$$
T^\\ast(s_1,p_2)=e.
$$

若兩者都成立，而且 implementation 沒有被 timeout、node cap 或不安全 candidate discard 截斷，則 compositional solver 可以完整求解合法狀態。

實際工程中的資源限制必須另行標記，不能混入數學 completeness。

---

## 23. PhaseSpec：把 Two-Phase 做成通用框架

不應把 Kociemba 邏輯硬編成兩個特殊函式，而可定義：

```text
PhaseSpec
  name
  inputDomain
  goalPredicate
  allowedMoves
  representation
  heuristic
  pruningRules
  searchPolicy
  outputInvariant
```

Phase 1：

```text
goalPredicate: inG1
allowedMoves: 18 face turns
representation: phase1 coordinates
searchPolicy: IDA*
outputInvariant: twist=0, flip=0, slice=0
```

Phase 2：

```text
inputDomain: G1
goalPredicate: solved
allowedMoves: 10 G1 moves
representation: phase2 coordinates
searchPolicy: IDA*
outputInvariant: solved
```

如此 Thistlethwaite、多 phase solver、甚至其他 twisty puzzle 都可重用同一 runtime。

---

## 24. PhaseHandoff：第一級資料結構

Phase boundary 應保存：

```text
PhaseHandoff
  sourceStateRef
  phase1Path
  boundaryStateRef
  membershipCertificate
  phase1Cost
  phase2Coordinates
  lowerBounds
```

membership certificate 至少確認：

$$
\\operatorname{Twist}=0,
$$

$$
\\operatorname{Flip}=0,
$$

$$
\\operatorname{Slice}=0.
$$

如此 UI 可以讓使用者看到：現在不是「差不多解好一半」，而是正式進入另一個對 Phase 2 move set 封閉的操作子域。

---

## 25. Helper coordinates 與 phase handoff 成本

現行 Kociemba implementation 還有一個值得工程學習的細節：Phase 2 的部分 coordinates 在 Phase 1 中沒有直接定義。

如果在 Phase 1 結束後才回到 cubie state 重新計算，會增加 handoff cost。因此 current implementation 在 Phase 1 同步維護 UDSliceSorted、RLSliceSorted、FBSliceSorted 等 helper coordinates，以加速 Phase 2 初始化。

這說明：

$$
\\boxed{
\\text{representation design 還應考慮 phase transition cost}.
}
$$

---

## 26. Representation continuity

令 Phase 1 representation 為 $R_1(s)$，Phase 2 representation 為 $R_2(s)$。

若 Phase 2 initialization 必須：

$$
R_1\\rightarrow S\\rightarrow R_2,
$$

成本可能較高。

若同步維護 helper state $H(s)$，則可以：

$$
(R_1,H)\\rightarrow R_2.
$$

因此可定義 handoff cost：

$$
C_H(R_1,R_2).
$$

這形成一個重要 FDRS 工程命題：

$$
\\boxed{
\\text{兩個 individually efficient representations，未必形成 globally efficient pipeline}.
}
$$

---

## 27. Pruning table 的 phase-specific 語義

Phase 1 pruning table 估計的是：

$$
d(s,G_1),
$$

不是：

$$
d(s,e).
$$

Phase 2 pruning table 才估計：

$$
d_{G_1}(s,e).
$$

所以兩張表的數字即使同為 $h=7$，語義也完全不同。

UI 必須標示：

```text
Phase 1 LB: 7 moves to G1
Phase 2 LB: 7 moves to solved inside G1
```

而不能都叫 `distance to solved`。

---

## 28. Pruning table 壓縮也是 solver engineering

Kociemba 技術說明指出 pruning table 不一定儲存完整 distance integer；例如可只儲存 distance modulo $3$，再利用相鄰 move 的距離變化規律恢復或追蹤 pruning depth。

因此 solver engineering 更精確地是：

$$
\\boxed{
\\text{search logic}
+
\\text{representation}
+
\\text{precomputed knowledge}
+
\\text{memory encoding}.
}
$$

---

## 29. FCSR 可視化：Two-Phase 應顯示「結構轉場」

新版頁面不應只顯示一條 move list，而可以顯示：

```text
SCRAMBLE
   ↓
PHASE 1 SEARCH
   ↓
G1 MEMBERSHIP
   ↓
PHASE 2 SEARCH
   ↓
SOLVED
```

Phase 1 顯示：

$$
\\operatorname{Twist},
\\operatorname{Flip},
\\operatorname{Slice},
h_1,
\\theta_1.
$$

Phase 2 顯示：

$$
\\operatorname{CornerPerm},
\\operatorname{EdgePerm},
\\operatorname{SlicePerm},
h_2,
\\theta_2.
$$

handoff 時讓 3D、flat net、cubie 與 coordinate views 同步標記：

$$
\\boxed{\\text{ENTERED }G_1}.
$$

---

## 30. Boundary candidate visualization

因為 Two-Phase 可以測試多個 Phase-1 candidates，UI 可以顯示：

| Candidate | Phase 1 | Phase 2 | Total |
| --- | ---: | ---: | ---: |
| $b_1$ | $9$ | $13$ | $22$ |
| $b_2$ | $10$ | $8$ | $18$ |
| $b_3$ | $11$ | $5$ | $16$ |

這讓使用者直接看到：

$$
\\boxed{
\\text{最短 Phase 1}
\\neq
\\text{最短總解}.
}
$$

---

## 31. Two-Phase 與 FDRS 的真正連接

如果只說「FDRS 能把魔方攤平」，Two-Phase 並沒有直接使用幾何 flat net 來加速核心搜尋。

但若把 FDRS 起源命題提升為：改變表示、忽略任務無關自由度、尋找結構正常形，再在受限域中完成剩餘問題，那麼 Two-Phase 就成為非常漂亮的計算案例：

$$
\\boxed{
\\text{full state}
\\rightarrow
\\text{task quotient}
\\rightarrow
\\text{subgroup normal form}
\\rightarrow
\\text{restricted completion}.
}
$$

---

## 32. 子群不是「低維」的口語代名詞

需要特別避免新的過度延伸。

 $G_1$ 是 $G$ 的 subgroup，但這不代表可以在沒有額外定義的情況下直接宣稱：

$$
\\dim G_1<\\dim G.
$$

此處討論的是有限群、coset、coordinate cardinality 與 search domain，而不是歐氏幾何維度。

因此本文使用 subgroup restriction、quotient reduction、coordinate reduction，而不把所有結構縮減都叫作幾何降維。

---

## 33. Phase decomposition 的一般形式

Two-Phase 可以一般化成：

$$
G=G_0\\supseteq G_1\\supseteq\\cdots\\supseteq G_k=\\{e\\}.
$$

每一階段：

$$
G_i\\rightsquigarrow G_{i+1}.
$$

若每階段都有 phase goal、move set、sufficient representation、admissible heuristic 與 verified handoff，則形成：

$$
\\operatorname{PhasePipeline}=(P_0,\\ldots,P_{k-1}).
$$

Kociemba 是 $k=2$ 的重要實例。

---

## 34. Phase decomposition 本身也是 optimization problem

若 phase 太多，每階段通常較小，但 handoff 更多、解序列可能更長、representation 切換更多。

若 phase 太少，每階段 state space 變大，需要更強 heuristic、更大 table 與更多搜尋。

因此可以抽象：

$$
J(\\mathcal P)
=
\\sum_i
\\left(
C_{\\mathrm{search}}(P_i)
+
C_{\\mathrm{handoff}}(P_i,P_{i+1})
+
C_{\\mathrm{memory}}(P_i)
\\right)
+
\\lambda C_{\\mathrm{solution}}.
$$

這是 FDRS-Cube 後續值得實驗的方向。

---

## 35. 自動 phase discovery 的遠期接口

經典 Two-Phase 的 $G_1$ 由人類數學家設計。

架構上可以保留未來問題：給定 twisty puzzle 的群、生成元與代價，是否能由計算機自動尋找好的中間 subgroup / quotient / invariant？

形式上：

$$
\\operatorname{DiscoverPhase}(G,A,c,M_{\\max})
\\rightarrow
(G_1,R_1,h_1).
$$

這不是本系列立即要解的問題，但它直接接向後續 AI-discovered solver。

---

## 36. 形式驗證目標：Two-Phase Kernel

### T1. $G_1$ subgroup closure

對 $a\\in A_2$ 與 $s\\in G_1$，證：

$$
T(s,a)\\in G_1.
$$

### T2. Phase-1 membership characterization

證明 $s\\in G_1$ 與以下條件的對應：

$$
\\operatorname{Twist}(s)=0,
$$

$$
\\operatorname{Flip}(s)=0,
$$

$$
\\operatorname{Slice}(s)=0.
$$

### T3. Phase-1 handoff correctness

若：

$$
\\operatorname{Solve}_1(s)=p_1,
$$

則：

$$
T^\\ast(s,p_1)\\in G_1.
$$

### T4. Phase-2 soundness

若 $s_1\\in G_1$ 且：

$$
\\operatorname{Solve}_2(s_1)=p_2,
$$

則：

$$
T^\\ast(s_1,p_2)=e.
$$

### T5. Compositional solver soundness

由 T3 與 T4 證：

$$
T^\\ast
\\left(
s,
p_1\\mathbin{+\\!\\!+}p_2
\\right)
=e.
$$

### T6. Phase pruning lower-bound correctness

分別證：

$$
h_1(s)\\leq d(s,G_1),
$$

以及：

$$
h_2(s)\\leq d_{G_1}(s,e).
$$

---

## 37. Solver result 應攜帶 phase metadata

建議結果型別：

```text
TwoPhaseSolution
  phase1Path
  boundaryState
  phase1Certificate
  phase2Path
  finalCertificate
  phase1Cost
  phase2Cost
  totalCost
  optimalityStatus
  searchStats
```

其中：

```text
optimalityStatus:
  Unknown
  PhaseOptimalOnly
  GloballyProven
```

標準快速 Two-Phase 一般應回 `Unknown`，而不是偷偷標 `Optimal`。

---

## 38. 本文核心命題

### 命題 T-A：Two-Phase 是 subgroup decomposition

$$
G\\rightsquigarrow G_1\\rightsquigarrow e.
$$

### 命題 T-B：Phase 1 是集合目標搜尋

Phase 1 的 goal 是 $G_1$，而不是單一 solved state。

### 命題 T-C：Phase 1 coordinate 是 task-sufficient quotient

它刻意忽略 Phase 1 不需要的 permutation 細節。

### 命題 T-D：Phase 2 在封閉 restricted move set 中完成剩餘 permutation

$$
A_2=\\{U,U',U^2,D,D',D^2,R^2,L^2,F^2,B^2\\}.
$$

### 命題 T-E：最短 Phase 1 不代表最短總解

真正 boundary optimization 為：

$$
\\min_{b\\in G_1}
\\left[
d_G(s,b)+d_{G_1}(b,e)
\\right].
$$

### 命題 T-F：Soundness 與 global optimality 分離

Two-Phase 可以可靠解出魔方而不證明其 move sequence 全域最短。

### 命題 T-G：Phase handoff 本身也是 representation / computation cost

兩階段各自最佳，不代表整條 pipeline 最佳。

---

## 39. 結論

本文第一次把前五篇的地基組成一個真正成熟的 solver architecture。

Two-Phase 的成功不是單一演算法技巧，而是：

$$
\\boxed{
\\text{subgroup choice}
+
\\text{task coordinates}
+
\\text{move tables}
+
\\text{symmetry}
+
\\text{pruning tables}
+
\\text{IDA*}
+
\\text{phase-boundary search}.
}
$$

它真正告訴 FCSR/FDRS 的不是「魔方應該分兩次解」，而是：

$$
\\boxed{
\\text{當完整目標太大時，可以先尋找一個結構受限、可由較少資訊描述、且對後續操作封閉的中間正常形。}
}
$$

然後再於該受限域中完成剩餘自由度。

這使 FDRS 的起源線從「改變觀察表示」進一步走向：

$$
\\boxed{
\\text{重寫中間目標}
+
\\text{重寫搜尋空間}
+
\\text{重寫允許操作}.
}
$$

下一篇將把目前所有數學與工程層真正接到形式驗證：

**《可驗證 Solver：Soundness、Completeness、Optimality 與解證書》**。

---

## 參考資料與來源定位

### 起源系列

- [F2025-A] Neo.K，《展平式維度重構理論：完整數學架構與概念解析》，2025 年 8 月。
- [F2025-B] Neo.K，《展平式維度重構理論：從 FCSR 到 FDRS 的完整數學架構》，2025 年 8 月。
- [F2026-D] `FDRS_展開收斂_同步性.html`，FDRS/FCSR permutation engine、IDA* 與同步可視化原型。

### 外部 Two-Phase 基線

- [R1] Herbert Kociemba, **Two-Phase Algorithm Details**.  
  https://www.kociemba.org/math/imptwophase.htm
- [R2] Herbert Kociemba, **Pruning Tables**.  
  https://kociemba.org/math/pruning.htm
- [R3] Herbert Kociemba, **The Coordinate Level**.  
  https://kociemba.org/math/coordlevel.htm
- [R4] Herbert Kociemba, **Coordinates and Symmetry**.  
  https://kociemba.org/math/symcord.htm
- [R5] Herbert Kociemba, **The Move Tables**.  
  https://kociemba.org/math/movetables.htm
- [R6] Tomas Rokicki, Herbert Kociemba, Morley Davidson, John Dethridge, **The Diameter of the Rubik's Cube Group Is Twenty**, SIAM Journal on Discrete Mathematics.

---

## 版本註記

v0.1 將 Two-Phase 明確重寫為 subgroup / boundary-state decomposition，而不是兩段式黑盒求解；同時將 phase handoff、representation continuity 與 optimality status 升為第一級規格。

後續第七篇：

**《可驗證 Solver：Soundness、Completeness、Optimality 與解證書》**。
