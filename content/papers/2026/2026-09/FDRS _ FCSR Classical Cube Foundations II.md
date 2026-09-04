# FDRS / FCSR Classical Cube Foundations II
## 合法狀態與群作用：魔方狀態空間的嚴格計算模型

**英文題名：** Legal States and Group Actions: A Rigorous Computational Model of the Rubik's Cube State Space  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-02  
**版本：** v0.1  
**日期：** 2026-08-19  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第二篇

---

## 摘要

FCSR 的早期實作以 $54$ 個色位描述標準 $3\times3\times3$ 魔方，並把基本面轉動視為色位的離散置換。這種表示十分適合可視化，但若直接把所有 $6^{54}$ 類型的色彩賦值或所有具有正確色彩數量的 $54$ 格排列視為魔方狀態，就會混淆「資料編碼空間」與「物理上可由合法轉動到達的狀態空間」。

本文建立 FDRS/FCSR 經典魔方線的第二層地基：以 cubie permutation 與 orientation 為核心，嚴格區分 raw encoding、assembled state、legal state 與 reachable state。對固定中心、固定全域參考框架的標準 $3\times3\times3$ 魔方，一個 cubie state 由角塊排列、角塊朝向、邊塊排列與邊塊朝向四部分構成。合法可達狀態必須滿足三個全域約束：角塊朝向總和為 $0\pmod 3$ 、邊塊朝向總和為 $0\pmod 2$ 、角塊排列與邊塊排列具有相同 parity。這三項條件不只是必要條件；在標準魔方模型中，它們亦構成可達性的完整約束。

由此，合法狀態數可寫成

$$
|\mathcal{S}_{\mathrm{legal}}|
=
8!\cdot 3^7\cdot 12!\cdot 2^{11}\cdot\frac12
=
43{,}252{,}003{,}274{,}489{,}856{,}000.
$$

本文進一步將面轉動生成的 Rubik group 定義為作用在合法狀態集合上的有限群，並區分「群元素」、「狀態」、「表示」與「操作序列」。在 solved state 被選為基點後，每個合法狀態可與一個群元素的作用結果對應；但在軟體架構上仍應保持狀態型別與 move/group 型別的分離，以支援 legality checker、solver、可視化與後續多 puzzle 泛化。

本文最後提出一個適合 Lean 4 與工程實作共享的 `RawCubieState → ValidCubieState` 分層方案，並把「合法性」設計為可獨立驗證的證書層。這使 FCSR 的 $54$ 色位視圖可以保留作為人類友善表示，同時由 cubie kernel 承擔 canonical computational semantics。

**關鍵詞：** Rubik group、合法狀態、reachability、corner orientation、edge orientation、permutation parity、cubie state、FCSR、Lean 4、形式驗證

---

## 1. 問題：不是每一張六面色位圖都是一顆合法魔方

第一篇已將 FCSR 重定位為 representation / observer layer。現在必須回答更基礎的問題：

> 一個看起來像魔方的資料結構，什麼時候才真的代表一個可由合法魔方操作得到的狀態？

令顏色集合為

$$
\mathcal{C}
=
\{U,D,F,B,L,R\}.
$$

最寬鬆的 facelet encoding 可以寫成：

$$
x:
\{0,\ldots,53\}
\rightarrow
\mathcal{C}.
$$

所有此類函數形成：

$$
\mathcal{E}_{\mathrm{raw}}
=
\mathcal{C}^{54}.
$$

但這個集合顯然遠大於真正的魔方狀態集合。即使再加入「每種顏色恰有九格」的條件，仍然會包含大量不能由合法面轉動產生的配置。

原因在於魔方不是 $54$ 張彼此獨立的貼紙。貼紙被綁定在實體 cubie 上，而 cubie 的排列與朝向受全域不變量約束。

因此，本文採用以下分層：

$$
\mathcal{E}_{\mathrm{raw}}
\supset
\mathcal{E}_{\mathrm{assembled}}
\supset
\mathcal{S}_{\mathrm{legal}}.
$$

其中：

- $\mathcal{E}_{\mathrm{raw}}$：任意 facelet 資料；
- $\mathcal{E}_{\mathrm{assembled}}$：可以被解析為正確數量與種類之 corner/edge cubies 的組裝狀態；
- $\mathcal{S}_{\mathrm{legal}}$：可由標準魔方合法 face turns 從 solved state 到達的狀態。

這個區分將成為後續 parser、validator、solver 與 proof checker 的共同前置條件。

---

## 2. 模型邊界：固定中心、固定參考框架

本文討論的經典核心模型採用以下慣例：

1. 標準 $3\times3\times3$ 魔方；
2. 六個中心作為固定面標籤，不視為可排列 cubies；
3. 全體魔方在空間中的旋轉不算作 face move；
4. 狀態由 $8$ 個 corner cubies 與 $12$ 個 edge cubies 的位置及朝向決定；
5. 基本生成操作為六個面之 quarter turns，逆轉與 half turns 可由生成元組合或直接加入搜尋 alphabet。

因此 movable cubies 為：

$$
8+12=20.
$$

角塊位置集合記為：

$$
C_P
=
\{URF,UFL,ULB,UBR,DFR,DLF,DBL,DRB\},
$$

邊塊位置集合記為：

$$
E_P
=
\{UR,UF,UL,UB,DR,DF,DL,DB,FR,FL,BL,BR\}.
$$

這套命名與現代 Two-Phase 實作常用的 cubie-level convention 相容。

---

## 3. Cubie state 的四元組

一個 raw cubie state 定義為：

$$
s
=
(\pi_c,o_c,\pi_e,o_e),
$$

其中：

$$
\pi_c\in S_8
$$

是 corner permutation，

$$
o_c:C_P\rightarrow\mathbb{Z}_3
$$

是 corner orientation，

$$
\pi_e\in S_{12}
$$

是 edge permutation，

$$
o_e:E_P\rightarrow\mathbb{Z}_2
$$

是 edge orientation。

因此不施加合法性約束時，raw cubie space 可寫成：

$$
\mathcal{S}_{\mathrm{raw}}
=
S_8
\times
\mathbb{Z}_3^8
\times
S_{12}
\times
\mathbb{Z}_2^{12}.
$$

但真正的合法狀態只佔其中一個受約束子集。

---

## 4. 第一個合法性約束：corner twist conservation

對每個角塊，以固定參考面定義 orientation：

$$
o_c(i)\in\{0,1,2\}.
$$

其中 $0$ 表示未扭轉， $1$ 與 $2$ 表示兩個相反方向的 $120^\circ$ 扭轉類。

標準魔方任何合法 face move 都保持：

$$
\sum_{i\in C_P}o_c(i)
\equiv
0
\pmod 3.
$$

因此八個 corner orientation 不是彼此獨立。

若任選前七個角塊朝向，第八個必須滿足：

$$
o_c(8)
\equiv
-
\sum_{i=1}^{7}o_c(i)
\pmod 3.
$$

所以 corner orientation 的自由狀態數為：

$$
3^7,
$$

而不是：

$$
3^8.
$$

這就是為什麼「只把一顆角塊單獨扭轉 $120^\circ$ 」會得到一個可以物理拆裝出來、卻不能靠正常 face turns 到達的 assembled-but-illegal state。

---

## 5. 第二個合法性約束：edge flip conservation

每個 edge orientation 取：

$$
o_e(i)\in\mathbb{Z}_2.
$$

標準合法 move 保持：

$$
\sum_{i\in E_P}o_e(i)
\equiv
0
\pmod 2.
$$

因此十二個 edge flip 中只有十一個可以自由指定：

$$
o_e(12)
\equiv
-
\sum_{i=1}^{11}o_e(i)
\pmod 2.
$$

edge orientation 自由度為：

$$
2^{11}.
$$

所以單獨翻轉一個 edge 同樣是一個 assembled-but-illegal state。

---

## 6. 第三個合法性約束：corner / edge permutation parity 必須一致

令：

$$
\operatorname{sgn}(\pi)
\in
\{+1,-1\}
$$

表示 permutation parity。

標準魔方的合法 face turns 對 corners 與 edges 所誘導的排列 parity 始終同步，因此任意合法狀態滿足：

$$
\operatorname{sgn}(\pi_c)
=
\operatorname{sgn}(\pi_e).
$$

等價地：

$$
\operatorname{parity}(\pi_c)
=
\operatorname{parity}(\pi_e).
$$

這排除了「只交換兩個 corners」或「只交換兩個 edges」的組裝狀態。

若 corner permutation 與 edge permutation 原本各自有：

$$
8!
\quad\text{與}\quad
12!
$$

種可能，parity matching 使合法排列對的數目除以二：

$$
\frac{8!\cdot12!}{2}.
$$

---

## 7. 合法狀態定理

定義：

$$
\operatorname{Valid}(s)
$$

當且僅當 raw cubie state

$$
s=(\pi_c,o_c,\pi_e,o_e)
$$

滿足：

$$
\sum o_c
\equiv0\pmod3,
$$

$$
\sum o_e
\equiv0\pmod2,
$$

以及

$$
\operatorname{sgn}(\pi_c)
=
\operatorname{sgn}(\pi_e).
$$

則經典標準魔方的核心可達性定理可以表述為：

$$
\boxed{
\operatorname{Reachable}(s)
\iff
\operatorname{Valid}(s).
}
$$

必要性來自三個不變量在所有生成 move 下保持。

充分性則比必要性更強：它宣稱不存在第四個尚未捕捉的全域障礙；只要這三個約束全部滿足，就存在某個合法 move sequence 把 solved state 送到該狀態。

這個 sufficiency 不能只由「看起來合理」推出，應視為需要獨立證明或可信既有定理支持的核心結果。

在本系列的後續 Lean 實作中，我們會把它拆成兩個方向：

$$
\operatorname{Reachable}(s)
\Rightarrow
\operatorname{Valid}(s)
$$

與

$$
\operatorname{Valid}(s)
\Rightarrow
\operatorname{Reachable}(s).
$$

第一個方向可以直接由 move invariants 建立；第二個方向需要 constructive reachability 或引用／重建已知的群論構造。

---

## 8. 合法狀態數

根據四個 cubie components：

corner permutations：

$$
8!,
$$

corner orientations：

$$
3^7,
$$

edge permutations：

$$
12!,
$$

edge orientations：

$$
2^{11},
$$

再加入 parity matching 的：

$$
\frac12,
$$

得到：

$$
|\mathcal{S}_{\mathrm{legal}}|
=
8!\cdot3^7\cdot12!\cdot2^{11}\cdot\frac12.
$$

因此：

$$
\boxed{
|\mathcal{S}_{\mathrm{legal}}|
=
43{,}252{,}003{,}274{,}489{,}856{,}000.
}
$$

這個數字不是由「六面各九格」直接計算而來，而是由 cubie identity、orientation invariants 與 permutation parity constraints 共同決定。

它也可以重寫成其他等價計數形式；本文固定使用上述分解，因為它直接對應後續 canonical state data structure。

---

## 9. Rubik group 與狀態集合

令六個基本 face quarter turns 為：

$$
U,D,L,R,F,B.
$$

定義 Rubik group：

$$
G
=
\langle U,D,L,R,F,B\rangle.
$$

這裡每個生成元都是作用於 cubie state 的可逆變換。

若 solved state 為：

$$
s_\star,
$$

則 orbit：

$$
G\cdot s_\star
=
\{g\cdot s_\star:g\in G\}
$$

恰好就是：

$$
\mathcal{S}_{\mathrm{legal}}.
$$

因此：

$$
\mathcal{S}_{\mathrm{legal}}
=
G\cdot s_\star.
$$

在固定中心且 action faithful 的標準模型中，選定 solved state 後可以把每個 legal state 與唯一的群作用結果對應，從而在數學上將 cube group 與 legal states 識別。

然而工程上不建議把兩者完全做成同一型別。

理由是：

- `CubeState` 表示「目前世界在哪裡」；
- `Move` / `MoveSeq` 表示「要對世界做什麼」；
- `GroupElement` 表示一個可逆整體作用；
- `Representation` 表示「觀察者如何看這個狀態」。

數學同構不代表軟體責任必須合併。

---

## 10. 群作用比「色塊移動」更接近 canonical semantics

FCSR 視覺層可以說：

> 某些顏色從這些格子移到那些格子。

但 canonical kernel 應說：

$$
G
\curvearrowright
\mathcal{S}_{\mathrm{legal}}.
$$

也就是：

$$
(g,s)
\mapsto
g\cdot s.
$$

群作用滿足：

$$
e\cdot s=s,
$$

以及：

$$
(g_1g_2)\cdot s
=
g_1\cdot(g_2\cdot s).
$$

這讓：

- move composition；
- inverse；
- scramble；
- solve；
- replay；
- proof certificate；

全部共享同一個代數語義。

FCSR net 則是透過 representation map：

$$
R_{\mathrm{flat}}:
\mathcal{S}_{\mathrm{legal}}
\rightarrow
\mathcal{V}_{\mathrm{flat}}
$$

同步顯示這個作用。

---

## 11. Cubie composition 與 orientation 不是單純 permutation composition

若只追蹤 facelets，每個 move 可以直接寫成 $54$ 個位置的 permutation。

但在 cubie level，除了 piece permutation 還必須更新 orientation。

採用 destination-based 的「is replaced by」convention 時，可把一個 cubie transformation $A$ 的 corner 部分寫成：

$$
A(x).c
$$

表示 move 後位置 $x$ 由哪個 corner cubie 佔據，

$$
A(x).o
$$

表示該 cubie 因此增加多少 orientation。

對兩個 transformation $A,B$，corner composition 可寫成：

$$
(A\ast B)(x).c
=
A(B(x).c).c,
$$

以及：

$$
(A\ast B)(x).o
=
A(B(x).c).o+B(x).o
\pmod3.
$$

edge orientation 的對應公式則模：

$$
2.
$$

這揭示一個重要工程風險：

> 若實作混用「piece carried to destination」與「destination replaced by source」兩種 convention，permutation 看似合理但 orientation composition 很容易整體反向。

因此新版 Twisty Core 必須在型別、註解與測試中固定單一 convention。

---

## 12. Facelet representation 與 cubie representation 的關係

第一篇已定義 FCSR facelet encoding：

$$
E_{\mathrm{FCSR}}:
\mathcal{S}_{\mathrm{legal}}
\rightarrow
\mathcal{C}^{54}.
$$

第二篇進一步加入 cubie encoding：

$$
E_{\mathrm{cubie}}:
\mathcal{S}_{\mathrm{legal}}
\rightarrow
\mathcal{K},
$$

其中：

$$
\mathcal{K}
=
S_8
\times
\mathbb{Z}_3^8
\times
S_{12}
\times
\mathbb{Z}_2^{12}
$$

再受三項合法性約束。

理想情況下存在 parser：

$$
P:
\mathcal{C}^{54}
\rightarrow
\operatorname{Option}(\mathcal{K}),
$$

它完成：

1. 顏色數量檢查；
2. center/frame convention 檢查；
3. corner identity reconstruction；
4. edge identity reconstruction；
5. orientation extraction；
6. parity / orientation validity 檢查。

若解析成功，才得到：

$$
\operatorname{some}(s_{\mathrm{valid}}).
$$

因此 UI 可以接受使用者輸入 facelet colors，但 solver kernel 永遠不應默默假設輸入合法。

---

## 13. Legality checker 應成為獨立核心

我們定義：

$$
\operatorname{validate}:
\mathcal{S}_{\mathrm{raw}}
\rightarrow
\operatorname{Result}(\mathcal{S}_{\mathrm{legal}},\mathcal{E}),
$$

其中 error set 可以至少區分：

$$
\mathcal{E}
=
\{
\text{InvalidCornerSet},
\text{InvalidEdgeSet},
\text{CornerTwist},
\text{EdgeFlip},
\text{ParityMismatch}
\}.
$$

這比單純回傳：

$$
\mathrm{Bool}
$$

更適合可視化與教學。

例如 UI 可以直接指出：

- 「這不是難解，而是不合法：單 edge flip」；
- 「corner twist sum 為 $1\pmod3$ 」；
- 「corner permutation 為 odd，但 edge permutation 為 even」。

如此使用者能真正看到：

$$
\text{unsolved}
\neq
\text{illegal}.
$$

---

## 14. 對 FCSR 可視化的直接影響

合法性不是純後端檢查，它應該成為新版 FCSR UI 的一部分。

當使用者在 facelet editor 中手動改色，可以同步顯示：

### Color layer

$$
\text{color count}
$$

### Piece layer

$$
\text{corner identities}
+
\text{edge identities}
$$

### Orientation layer

$$
\sum o_c\bmod3,
\qquad
\sum o_e\bmod2
$$

### Permutation layer

$$
\operatorname{parity}(\pi_c),
\qquad
\operatorname{parity}(\pi_e)
$$

### Final legality

$$
\operatorname{Valid}(s)\in\{\mathrm{true},\mathrm{false}\}.
$$

這會讓「魔方群論」從論文中的抽象文字變成可以直接操作的視覺物件。

---

## 15. Lean 4 的 canonical type design

後續形式化可採以下概念分層，而不是直接把所有 constraints 塞進一個巨大 structure。

概念上：

```text
RawCubieState
  ├── cornerPerm
  ├── cornerOri
  ├── edgePerm
  └── edgeOri

ValidCubieState := { s : RawCubieState // Valid s }
```

數學上：

$$
\operatorname{Valid}(s)
:=
C(s)\land E(s)\land P(s),
$$

其中：

$$
C(s)
\iff
\sum o_c=0\in\mathbb{Z}_3,
$$

$$
E(s)
\iff
\sum o_e=0\in\mathbb{Z}_2,
$$

$$
P(s)
\iff
\operatorname{sgn}(\pi_c)
=
\operatorname{sgn}(\pi_e).
$$

這種設計有三個優點。

第一，raw parser 可以先建立資料，再執行 proof-producing validation。

第二，solver 的輸入型別可以直接要求：

$$
s:\operatorname{ValidCubieState},
$$

從而不需要在每個 recursion step 重複 legality check。

第三，所有 move 都可以被證明為：

$$
T_a:
\operatorname{ValidCubieState}
\rightarrow
\operatorname{ValidCubieState}.
$$

這讓「合法性保持」成為型別級 invariant。

---

## 16. 第一批形式化定理

第二篇對應的 Lean 目標應依賴順序分成六層。

### L1. Solved state is valid

$$
\operatorname{Valid}(s_\star).
$$

### L2. Each generator preserves corner twist invariant

$$
C(s)
\Rightarrow
C(T_a(s)).
$$

### L3. Each generator preserves edge flip invariant

$$
E(s)
\Rightarrow
E(T_a(s)).
$$

### L4. Each generator preserves parity matching

$$
P(s)
\Rightarrow
P(T_a(s)).
$$

### L5. Every move preserves validity

$$
\operatorname{Valid}(s)
\Rightarrow
\operatorname{Valid}(T_a(s)).
$$

### L6. Reachable implies valid

$$
\operatorname{Reachable}(s)
\Rightarrow
\operatorname{Valid}(s).
$$

其中 L6 可由 move sequence induction 直接建立。

更強的：

$$
\operatorname{Valid}(s)
\Rightarrow
\operatorname{Reachable}(s)
$$

應作為後續獨立 milestone，因為它要求完整的 sufficiency 構造，而不是單純 invariant preservation。

---

## 17. 與現有 Lean 魔方形式化的關係

截至 2026 年，已有公開 Lean 4 魔方形式化專案 `rubik-lean4`。其公開說明包含：

$$
\operatorname{isSolvable}
\iff
\operatorname{isValid},
$$

以及完整 solvable state count 的形式結果。

因此，本系列不應宣稱：

> 第一個用 Lean 形式化 Rubik's Cube。

我們的差異化目標應明確放在：

1. FCSR facelet / flat-net 與 cubie state 的雙向橋接；
2. 多 representation move-commutation theorem；
3. legality checker 的 UI 可視化；
4. verified solution certificate；
5. solver 與 proof checker 解耦；
6. 同一架構向多類 twisty puzzle 擴張。

現有形式化是重要參照與交叉驗證來源，而不是需要忽略的競爭者。

---

## 18. 狀態數很大，但「很大」不是本研究的主論點

合法狀態數約為：

$$
4.3252\times10^{19}.
$$

這個數字對人類而言巨大，但對計算研究真正重要的不是單純驚嘆其大小，而是它具有高度結構：

$$
\text{finite}
+
\text{reversible}
+
\text{generated}
+
\text{constrained}
+
\text{symmetric}.
$$

因此有效 solver 不會把它當作一個無結構的：

$$
4.3\times10^{19}
$$

節點黑箱。

它會利用：

- cubie decomposition；
- orientation coordinates；
- permutation coordinates；
- parity；
- subgroup；
- coset；
- symmetry；
- admissible lower bound；
- pruning table。

這也正是下一篇「表示不是解法」要處理的核心：

> 同一個 legal state space，換一個 coordinate system，為什麼會讓計算成本差幾個數量級？

---

## 19. FDRS 起源線在此得到第二次精確化

2025 FCSR 的直覺是：

$$
\text{3D Cube}
\rightarrow
\text{2D Color-State Net}.
$$

第一篇把它修正成：

$$
\text{Abstract State}
\rightarrow
\text{Multiple Representations}.
$$

第二篇再加入：

$$
\boxed{
\text{Representation Space}
\neq
\text{Legal State Space}.
}
$$

一個平面網格可以畫出非法魔方。

一個 $54$ 維顏色向量可以具有正確顏色數量，卻不在 cube group 的 orbit 中。

因此 FCSR 要成為可信的計算基礎，必須補上：

$$
\text{Encoding}
\rightarrow
\text{Parsing}
\rightarrow
\text{Validity}
\rightarrow
\text{Canonical State}.
$$

只有到了 canonical legal state，solver 與 group action 才真正開始。

---

## 20. 本文核心命題

### 命題 C1：色位資料不是狀態本體

$$
\mathcal{S}_{\mathrm{legal}}
\subsetneq
\mathcal{E}_{54}.
$$

### 命題 C2：合法性由全域不變量約束

$$
\operatorname{Valid}(s)
\iff
\left(
\sum o_c=0\pmod3
\right)
\land
\left(
\sum o_e=0\pmod2
\right)
\land
\left(
\operatorname{parity}(\pi_c)
=
\operatorname{parity}(\pi_e)
\right).
$$

### 命題 C3：合法狀態是 solved state 的 group orbit

$$
\mathcal{S}_{\mathrm{legal}}
=
G\cdot s_\star.
$$

### 命題 C4：legality 應在 solver 之前被獨立處理

$$
\text{Raw Input}
\rightarrow
\text{Validator}
\rightarrow
\text{Valid State}
\rightarrow
\text{Solver}.
$$

### 命題 C5：FCSR 應把 invariant 顯示出來

可視化不只畫魔方外觀，也應顯示 orientation sum、permutation parity、piece reconstruction 與 legality。

---

## 21. 結論

本文完成 FDRS/FCSR 經典魔方正統延續線的第二層地基。

第一篇回答：

> 同一個魔方狀態如何在不同表示中保持 move semantics？

第二篇回答：

> 什麼東西才有資格叫作一個合法魔方狀態？

答案不是「有 $54$ 個顏色格子」，而是：

$$
s
=
(\pi_c,o_c,\pi_e,o_e)
$$

並滿足：

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

這些條件把一個視覺玩具轉成一個具有精確型別邊界的有限群作用系統。

對後續工程而言，最重要的結果是形成：

$$
\boxed{
\text{Facelet UI}
\rightarrow
\text{Cubie Parser}
\rightarrow
\text{Legality Certificate}
\rightarrow
\text{Canonical State Kernel}.
}
$$

下一篇將不再問「是否合法」，而要比較同一合法狀態的不同計算表示：

**Facelet、Cubie、Permutation、Coordinate 到底分別保留什麼、犧牲什麼，又為什麼 coordinate representation 會直接改變 solver 的搜尋效率。**

---

## 參考資料與來源定位

### 起源文件

- [F2025-A] Neo.K，《展平式維度重構理論：完整數學架構與概念解析》，2025 年 8 月。
- [F2025-B] Neo.K，《展平式維度重構理論：從 FCSR 到 FDRS 的完整數學架構》，2025 年 8 月。
- [F2026-D] `FDRS_展開收斂_同步性.html`，FDRS/FCSR 魔方可視化與 IDA* 實驗原型。

### 外部數學與實作基線

- [R1] Herbert Kociemba, **The Cubie Level**.  
  https://kociemba.org/math/cubielevel.htm  
  用於 corner / edge cubie、orientation 與 transformation composition convention。

- [R2] Herbert Kociemba, **The Coordinate Level**.  
  https://kociemba.org/math/coordlevel.htm  
  用於 $3^7$ corner orientation coordinate、 $2^{11}$ edge orientation coordinate 與 permutation coordinates。

- [R3] Tomas Rokicki, Herbert Kociemba, Morley Davidson, John Dethridge, **The Diameter of the Rubik's Cube Group Is Twenty**, SIAM Journal on Discrete Mathematics.  
  https://www.kociemba.org/math/papers/rubik20.pdf  
  用於 permutation parity matching 與標準 cube group 計算背景。

- [R4] `vihdzp/rubik-lean4`, **Lean 4 formalization of Rubik's cubes**.  
  https://github.com/vihdzp/rubik-lean4  
  用於現有 `isSolvable_iff_isValid` 與 solvable state count 形式化工作的 related-work 定位。

---

## 版本註記

v0.1 將合法性分為 corner twist、edge flip 與 permutation parity 三個獨立 invariant，並把 `Reachable iff Valid` 明確列為需形式證明的核心定理，而不是由直覺直接帶過。

後續第三篇：

**《表示不是解法：Facelet、Cubie、Permutation 與 Coordinate 的等價與代價》**。
