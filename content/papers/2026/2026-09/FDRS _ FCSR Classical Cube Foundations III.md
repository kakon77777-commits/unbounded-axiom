# FDRS / FCSR Classical Cube Foundations III
## 表示不是解法：Facelet、Cubie、Permutation 與 Coordinate 的等價與代價

**英文題名：** Representation Is Not a Solver: Equivalence and Cost among Facelet, Cubie, Permutation, and Coordinate Models  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-03  
**版本：** v0.1  
**日期：** 2026-08-19  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第三篇

---

## 摘要

前兩篇已分別建立 FCSR 的表示語義與標準 $3\times3\times3$ 魔方的合法狀態條件。本文進一步回答一個對 FDRS 起源線至關重要的問題：如果 Facelet、Cubie、Permutation 與 Coordinate 都可以描述同一顆魔方，為什麼 solver 的實際效率會因表示不同而產生巨大差異？

本文首先區分兩類表示。第一類是**完整狀態表示**：在固定參考框架與合法狀態域內，Facelet 與 Cubie 表示可以互相重建，因而可視為同一 canonical state 的不同無損編碼。第二類是**任務導向表示**：單一 orientation coordinate、UDSlice coordinate、sym-coordinate 或 pruning-table index 通常不是完整狀態，而是將多個原始狀態合併到同一等價類、coset 或 symmetry class 中。這類表示刻意丟棄與當前子任務無關的自由度，以換取更小的狀態域、更快的 move evaluation、可查表的 heuristic 與更有效的剪枝。

本文因此提出 FCSR/FDRS 經典線的表示分層：

$$
\text{Canonical State}
\rightarrow
\begin{cases}
\text{Lossless Views}\\
\text{Task Coordinates}\\
\text{Quotient / Symmetry Views}\\
\text{Search Instrumentation}
\end{cases}
$$

並定義表示的五種代價：儲存代價、轉移代價、編解碼代價、資訊辨識力與搜尋價值。對固定 $3\times3\times3$ 而言，單純使用大 $O$ 漸近符號比較 Facelet 與 Cubie 常會失去意義，因為狀態寬度為常數；因此本文改採 representation work units 與實際 table cardinality 來描述成本。

本文最後提出一個適合新版 FCSR 可視化實驗室的 `Representation Registry`：同一 canonical state 可同步投影為 3D、flat net、facelet array、cubie tuple、完整 permutation、phase coordinates、symmetry classes 與 search heuristic state；每個表示必須聲明其是否 injective、是否可逆、是否對 move 封閉、是否依賴預計算表，以及其 intended task。如此，FDRS 最早的「改變觀察方式」命題便從哲學直覺升級為可計算、可測量、可視化的 representation engineering 問題。

**關鍵詞：** representation、Facelet、Cubie、permutation、coordinate、coset、symmetry reduction、move table、pruning table、FCSR、FDRS

---

## 1. 問題：同一顆魔方，為什麼要有這麼多表示？

對合法狀態集合

$$
\mathcal{S}_{\mathrm{legal}},
$$

第一篇已定義多個 representation map：

$$
R_i:
\mathcal{S}_{\mathrm{legal}}
\rightarrow
\mathcal{V}_i.
$$

如果所有表示只是「不同畫法」，那 solver 理論上不應因表示選擇而出現巨大的工程差異。

但現代魔方求解器實際上恰恰相反。

Facelet level 適合輸入、掃描與畫面。

Cubie level 適合描述 piece permutation 與 orientation。

Coordinate level 將 orientation、permutation、slice membership 等結構映射到有限整數區間。

Sym-coordinate 進一步利用對稱性把多個 coordinate values 合併到同一 equivalence class。

Pruning table 則直接把 coordinate tuple 映射到距離下界。

因此問題不能只問：

> 哪個表示最完整？

還必須問：

> 哪個表示對當前任務最有計算價值？

---

## 2. 表示的第一分類：Lossless 與 Task-Reduced

令：

$$
R:
\mathcal{S}
\rightarrow
\mathcal{V}.
$$

若對所有合法狀態：

$$
R(s_1)=R(s_2)
\Rightarrow
s_1=s_2,
$$

則 $R$ 在合法域上是 injective。

若還存在 decoder：

$$
D:
R(\mathcal{S})
\rightarrow
\mathcal{S}
$$

使：

$$
D(R(s))=s,
$$

則稱 $R$ 是本文意義下的 lossless state representation。

相對地，若存在：

$$
s_1\neq s_2
$$

但：

$$
R(s_1)=R(s_2),
$$

則表示將多個 full states 合併到同一 representation value。這不是錯誤，而可能是刻意的 task reduction。

因此本文將魔方表示分成：

$$
\boxed{
\text{Lossless State Representation}
}
$$

與

$$
\boxed{
\text{Task-Reduced Representation}.
}
$$

FDRS 的「展平」概念在經典魔方域中必須明確指出自己屬於哪一類，而不能只用「降維」一詞含混帶過。

---

## 3. Facelet representation：最接近觀察層

在固定 center / color convention 下，facelet representation 可以寫成：

$$
R_f:
\mathcal{S}_{\mathrm{legal}}
\rightarrow
\mathcal{C}^{54}.
$$

其中：

$$
\mathcal{C}
=
\{U,D,F,B,L,R\}.
$$

它的主要優點是：

1. 與真實魔方表面一一對應；
2. 容易由相機、人工輸入或 UI editor 取得；
3. 容易畫成 $3D$ cube 或 FCSR flat net；
4. move 可以直接預先生成為 $54$ 個 position indices 的 permutation。

在固定合法域內，只要 center convention 已知，合法 facelet encoding 可以重建 cubie identities 與 orientations，因此它可以是完整狀態表示。

但它的缺點也很明顯：

- piece identity 是隱含的；
- legality invariants 不直接可見；
- solver 真正需要的 corner twist、edge flip、piece permutation 需要解析後才能取得；
- phase/subgroup information 不自然地直接出現在 facelet array 中。

因此：

$$
\text{Facelet}
\approx
\text{excellent observer representation}
$$

但不代表：

$$
\text{Facelet}
=
\text{best search representation}.
$$

---

## 4. FCSR flat net：Facelet 的幾何佈局，而非另一個狀態本體

FCSR 的平面十字圖可以表示為：

$$
R_{\mathrm{flat}}
=
L\circ R_f,
$$

其中：

$$
L:
\mathcal{C}^{54}
\rightarrow
\mathcal{V}_{2D}
$$

只決定這 $54$ 個 facelets 如何排列在畫面上。

因此，若 $L$ 只是重新安排位置而不合併資料，則：

$$
R_{\mathrm{flat}}
$$

與：

$$
R_f
$$

具有相同的狀態辨識能力。

也就是：

$$
R_f(s_1)=R_f(s_2)
\iff
R_{\mathrm{flat}}(s_1)=R_{\mathrm{flat}}(s_2).
$$

所以 FCSR flat net 的第一個價值不是壓縮 state count，而是：

$$
\boxed{
\text{改變觀察幾何，而保持狀態可辨識性。}
}
$$

這也是 2025 起源命題在今日應採用的最精確版本之一。

---

## 5. Cubie representation：把物理約束變成顯式資料

第二篇已定義：

$$
R_c(s)
=
(\pi_c,o_c,\pi_e,o_e).
$$

Cubie representation 的資訊與合法 facelet representation 等價，但組織方式不同。

它直接暴露：

$$
\pi_c\in S_8,
$$

$$
o_c\in\mathbb{Z}_3^8,
$$

$$
\pi_e\in S_{12},
$$

$$
o_e\in\mathbb{Z}_2^{12}.
$$

因此：

- corner / edge identity 直接可讀；
- orientation invariants 直接可計算；
- parity 直接可計算；
- subgroup / coordinate extraction 更自然；
- move composition 可以在 piece level 上完成。

Kociemba 的 cubie-level 表示明確指出：在 cubie level 上，單純 permutation 不足以描述狀態，因為 corners 可以 twist、edges 可以 flip；因此 permutation 與 orientation 必須一起保存。

所以：

$$
\boxed{
\text{Cubie}
=
\text{piece permutation}
+
\text{piece orientation}.
}
$$

---

## 6. 「Permutation representation」必須說清楚是哪一種 permutation

在魔方文獻與程式中，「permutation」可能指至少三個不同東西。

### 6.1 Facelet permutation

一個 move 可以表示為：

$$
\sigma_a\in S_{54},
$$

描述 sticker positions 如何被重排。

這適合表示 transformation。

### 6.2 Piece permutation

狀態的一部分可以寫成：

$$
\pi_c\in S_8,
\qquad
\pi_e\in S_{12}.
$$

但這不含 orientation，因此不能單獨描述完整 cubie state。

### 6.3 Full state as a group element

選定 solved state 後，每個合法 state 可視為 Rubik group 中某元素對 solved state 的作用結果。

這時候「permutation」已是群元素層的描述，而不是單純某個 array。

因此新版工程與論文不應使用裸詞：

> permutation representation

而應標明：

$$
\text{FaceletPerm},
\quad
\text{CornerPerm},
\quad
\text{EdgePerm},
\quad
\text{GroupElement}.
$$

這可以避免很多實作與理論歧義。

---

## 7. 完整座標：把狀態映射到有限整數

Kociemba 的 coordinate level 展示了一個經典做法。

corner orientation 可映射為：

$$
x_1\in\{0,\ldots,3^7-1\},
$$

edge orientation：

$$
x_2\in\{0,\ldots,2^{11}-1\},
$$

corner permutation：

$$
x_3\in\{0,\ldots,8!-1\},
$$

edge permutation：

$$
x_4\in\{0,\ldots,12!-1\}.
$$

所以合法 cube 可以由 tuple：

$$
(x_1,x_2,x_3,x_4)
$$

描述，但並非任意 tuple 都合法，因為 permutation parity 還需匹配。

因此 full coordinate tuple 是 cubie state 的另一種完整數值化表示。

這種 encoding 的第一個工程價值是：

$$
\text{structured state}
\rightarrow
\text{small integers}.
$$

如此可以把 move evaluation 從結構操作轉成 table lookup。

---

## 8. 單一 coordinate 通常不是完整狀態

這是本文最重要的區分之一。

例如 corner orientation coordinate：

$$
R_{\mathrm{twist}}:
\mathcal{S}_{\mathrm{legal}}
\rightarrow
\{0,\ldots,2186\}
$$

只保留角塊朝向資訊。

因此大量不同的 full states 會有相同：

$$
R_{\mathrm{twist}}(s).
$$

它不是 lossless representation。

同理，edge orientation coordinate 只有：

$$
2048
$$

個值，UDSlice coordinate 只有：

$$
495
$$

個位置類型。

Two-Phase phase 1 使用的三個 raw coordinates：

$$
(\text{corner orientation},
\text{edge orientation},
\text{UDSlice})
$$

其目標不是唯一識別整顆魔方，而是判斷距離子群：

$$
G_1
=
\langle U,D,R^2,L^2,F^2,B^2\rangle
$$

還有多遠。

所以：

$$
\boxed{
\text{coordinate compression}
\neq
\text{complete state encoding}.
}
$$

它是任務導向的資訊選擇。

---

## 9. Coordinate 與 coset：真正的「商空間」入口

若 subgroup：

$$
H\leq G,
$$

coordinate 可以對應到 $G$ 相對於 $H$ 的 right cosets。

令 quotient-like projection：

$$
q_H:
G
\rightarrow
H\backslash G
$$

將群元素映射到其 right coset。

如果：

$$
g_1,g_2\in Hg,
$$

則：

$$
q_H(g_1)=q_H(g_2).
$$

這表示 coordinate 有意識地把「在子群 $H$ 內的差異」忽略掉。

這對 FDRS 是一個比單純 $3D\rightarrow2D$ 更強、更精確的數學概念：

$$
\boxed{
\text{不是把畫面壓平，而是把任務無關自由度商掉。}
}
$$

這種 reduction 的代價與收益都可以明確描述。

---

## 10. Move table：表示選擇如何直接改變轉移成本

若 coordinate $x$ 對 move $a$ 的更新只依賴目前 coordinate value，而不依賴被商掉的 full-state 細節，則存在：

$$
M_a:
X
\rightarrow
X
$$

使：

$$
R(T(s,a))
=
M_a(R(s)).
$$

這就是 coordinate-level move table 可以成立的原因。

實作上可以預先建立：

$$
\operatorname{MoveTable}[x,a]
=
x'.
$$

求解時的 move evaluation 便從：

> 解析 cubies、執行 permutation、更新 orientation、重新編碼

變成：

> 以 $(x,a)$ 查表取得 $x'$。

對固定 $3\times3\times3$，這些操作在傳統漸近分析中都可以視為常數時間；但實際 solver 差異來自常數、cache locality、table size 與節點展開次數。

因此本文不以：

$$
O(54)
\quad\text{vs}\quad
O(20)
\quad\text{vs}\quad
O(1)
$$

作為主要理論結論，而引入「representation work units」。

---

## 11. Representation Work Units

對 representation $R$，定義成本向量：

$$
\mathbf{C}(R)
=
(C_S,C_T,C_E,C_D,C_M).
$$

其中：

### 11.1 Storage cost

$$
C_S(R)
$$

描述一個 representation value 的儲存寬度或 table cardinality。

### 11.2 Transition cost

$$
C_T(R)
$$

描述套用一個 move 所需的 primitive operations / table accesses。

### 11.3 Encode cost

$$
C_E(R)
$$

描述：

$$
\mathcal{S}\rightarrow\mathcal{V}_R
$$

的成本。

### 11.4 Decode cost

$$
C_D(R)
$$

描述若可逆時：

$$
\mathcal{V}_R\rightarrow\mathcal{S}
$$

的成本。

### 11.5 Memory-precomputation cost

$$
C_M(R)
$$

描述為了讓 $C_T$ 或 heuristic lookup 很低而必須支付的預計算與記憶體代價。

因此「比較表示」不再只有一個 scalar。

真正的問題是：

$$
\min_R
J(R)
$$

其中：

$$
J(R)
=
w_S C_S
+
w_T C_T
+
w_E C_E
+
w_D C_D
+
w_M C_M
-
w_H V_H(R),
$$

而：

$$
V_H(R)
$$

表示該 representation 對 heuristic / pruning 的價值。

---

## 12. Pruning table：把表示直接變成搜尋下界

coordinate 的更強用途不是單純更新快，而是可以建立 distance table。

對 coordinate space $X$ 與目標集合 $X_\star$，定義：

$$
h(x)
=
d_X(x,X_\star).
$$

若 $R(s)=x$ 且 coordinate graph 是 full search graph 的適當 projection，則：

$$
h(R(s))
\leq
d_{\mathcal{S}}(s,s_\star).
$$

也就是：

$$
h
$$

成為 full-state distance 的 lower bound。

這就是 pruning table 能用於 IDA* 的核心原因。

Kociemba 的 pruning tables 直接用 coordinate 或 coordinate tuple 作為索引，儲存回到目標 subgroup / goal 的最少 move 數；該值因此是 full solver 可安全使用的下界。

於是表示第一次不只是：

$$
\text{state encoding},
$$

而是：

$$
\boxed{
\text{search knowledge structure}.
}
$$

---

## 13. Symmetry reduction：表示還可以再商一次

如果 symmetry group：

$$
\Sigma
$$

作用於 coordinate space $X$，可以定義等價關係：

$$
x\sim y
\iff
\exists \sigma\in\Sigma:
\sigma\cdot x=y.
$$

再把：

$$
X
$$

壓縮成 symmetry classes：

$$
X/\Sigma.
$$

例如 Kociemba 的 FlipUDSlice raw coordinate space 有：

$$
495\cdot2048
=
1{,}013{,}760
$$

個 raw values，而利用保留 UD-axis 的 symmetry 後，核心 equivalence classes 可降為：

$$
64{,}430.
$$

同樣，corner permutation 可映射到：

$$
2768
$$

個 symmetry classes。

因此：

$$
\text{state}
\rightarrow
\text{coordinate}
\rightarrow
\text{symmetry class}
$$

是一個逐層 quotient 的過程。

這和 FDRS 起源思想產生真正可計算的連接：

> 改變表示不是為了「看起來比較簡單」，而是要找出哪些差異對當前任務可以被安全視為等價。

---

## 14. 表示的辨識力

定義 representation $R$ 的 equivalence relation：

$$
s_1\equiv_R s_2
\iff
R(s_1)=R(s_2).
$$

則每個 representation 都誘導一個 partition：

$$
\Pi_R
=
\mathcal{S}/\equiv_R.
$$

若 $R$ injective：

$$
|\Pi_R|
=
|\mathcal{S}|.
$$

若 $R$ 是 task-reduced：

$$
|\Pi_R|
<
|\mathcal{S}|.
$$

因此可以定義辨識力比例：

$$
\eta(R)
=
\frac{|\Pi_R|}{|\mathcal{S}|}.
$$

對完整表示：

$$
\eta(R)=1.
$$

對高度壓縮的 task coordinate：

$$
\eta(R)\ll1.
$$

注意：

$$
\eta(R)\ll1
$$

不代表表示比較差。

若被合併的差異正好對某個 heuristic / phase goal 無關，則低辨識力反而是優勢。

---

## 15. 任務充分性比全資訊更重要

令任務：

$$
\tau:
\mathcal{S}
\rightarrow
Y.
$$

若存在：

$$
\hat{\tau}:
\mathcal{V}_R
\rightarrow
Y
$$

使：

$$
\tau
=
\hat{\tau}\circ R,
$$

則稱 representation $R$ 對任務 $\tau$ 是 sufficient。

即使：

$$
R
$$

不是 injective，只要它仍保留完成 $\tau$ 所需的全部資訊，就足夠。

例如 phase 1 的任務不是：

> 唯一重建 full cube。

而是：

> 把狀態帶進 $G_1$。

因此 phase-1 coordinates 不需要完整保存所有 permutation 細節。

這個原則可以寫成：

$$
\boxed{
\text{Best representation}
\neq
\text{Most informative representation}.
}
$$

而是：

$$
\boxed{
\text{Best representation}
=
\text{Task-sufficient representation with favorable cost}.
}
$$

---

## 16. FDRS 在經典魔方域中的重新定義

早期 FDRS 容易用：

$$
nD\rightarrow(n-1)D
$$

描述 representation change。

在經典魔方算法域，更精確的版本應是：

$$
\mathcal{S}
\xrightarrow{R}
\mathcal{V}
$$

並同時問：

1. $R$ 是否 injective？
2. $R$ 是否可逆？
3. $R$ 對哪些任務 sufficient？
4. $R$ 對 move 是否 closed？
5. $R$ 是否誘導 quotient / coset？
6. $R$ 是否支援 symmetry reduction？
7. $R$ 的 move-table / pruning-table 成本是多少？

於是 FDRS 的核心問題被重寫為：

$$
\boxed{
\text{如何選擇一個對當前任務足夠、但計算成本最低的表示？}
}
$$

這比單純問「能不能展平」更接近計算機真正的行為。

---

## 17. 完整表示與 task representation 的雙層架構

新版 Twisty Core 不應讓所有模組都共享同一 representation。

建議建立：

### Canonical layer

$$
S_{\mathrm{canonical}}
=
\text{ValidCubieState}.
$$

它是可信狀態真相。

### Lossless presentation adapters

$$
R_{3D},
\quad
R_{\mathrm{flat}},
\quad
R_{\mathrm{facelet}}.
$$

### Lossless computational encoding

$$
R_{\mathrm{fullcoord}}.
$$

### Task coordinates

$$
R_{\mathrm{twist}},
\quad
R_{\mathrm{flip}},
\quad
R_{\mathrm{UDSlice}},
\quad
\dots
$$

### Symmetry coordinates

$$
R_{\mathrm{sym}}.
$$

### Search instrumentation

$$
R_{\mathrm{heuristic}},
\quad
R_{\mathrm{frontier}},
\quad
R_{\mathrm{pruning}}.
$$

這種架構可以同時保證：

$$
\text{state truth}
$$

不被壓縮表示污染，又讓 solver 在 task-specific spaces 中高速運算。

---

## 18. Representation Registry

新版 FCSR UI / runtime 建議為每種 representation 註冊 metadata：

```text
RepresentationSpec
  name
  sourceType
  targetType
  injective
  reversible
  moveClosed
  task
  cardinality
  encodeCost
  decodeCost
  moveCost
  precomputeCost
  proofStatus
```

例如：

```text
FCSRFlatNet
  injective: true on legal fixed-frame states
  reversible: true
  moveClosed: true
  task: visualization

CornerOrientationCoord
  injective: false
  reversible: false
  moveClosed: true
  cardinality: 2187
  task: phase/search heuristic
```

這樣 UI 不只是切換畫面，而是在展示每個表示的數學性質。

---

## 19. 可視化應展示「資訊被保留了什麼」

如果使用者從：

$$
\text{Cubie}
$$

切到：

$$
\text{CornerOrientationCoord},
$$

畫面不應只顯示：

> 1234

而應同時顯示：

### 保留

$$
\text{all corner orientations}
$$

### 忽略

$$
\text{corner permutation}
$$

$$
\text{edge permutation}
$$

$$
\text{edge orientation}
$$

### 狀態合併

$$
R(s_1)=R(s_2)
$$

可能對大量：

$$
s_1\neq s_2
$$

成立。

### 任務用途

$$
\text{lower bound / phase coordinate}.
$$

如此使用者可以真正看到：

> 所謂演算法「簡化問題」，究竟簡化掉了什麼。

這是 FCSR/FDRS 可視化可以比一般 solver UI 更有價值的地方。

---

## 20. 表示轉換本身也需要驗證

若：

$$
E:
\text{CubieState}
\rightarrow
\text{FaceletState}
$$

與：

$$
D:
\text{FaceletState}
\rightarrow
\text{Option}(\text{CubieState}),
$$

則對合法狀態至少應證：

$$
D(E(s))
=
\operatorname{some}(s).
$$

若：

$$
C:
\text{CubieState}
\rightarrow
\text{FullCoordinate},
$$

以及：

$$
C^{-1}
$$

存在於合法 image 上，則應證：

$$
C^{-1}(C(s))
=
s.
$$

對 task coordinate：

$$
Q:
\mathcal{S}
\rightarrow
X,
$$

則不要求 inverse，而要求 move compatibility：

$$
Q(T(s,a))
=
M_a(Q(s)).
$$

這三種 proof obligation 不應混在一起：

$$
\text{round-trip correctness},
$$

$$
\text{injectivity / uniqueness},
$$

$$
\text{move compatibility}.
$$

---

## 21. 形式化目標：Representation Algebra

第三篇對應的 Lean 形式化可以建立一個通用介面：

概念上：

```text
Representation α β
  encode : α → β
```

對 lossless representation：

```text
LosslessRepresentation α β
  encode : α → β
  decode : β → Option α
  roundtrip : decode (encode s) = some s
```

對 move-compatible representation：

```text
MoveCompatibleRepresentation α β
  encode : α → β
  moveState : Move → α → α
  moveView : Move → β → β
  commutes :
    encode (moveState m s)
    =
    moveView m (encode s)
```

數學上核心就是：

$$
R\circ T_a
=
\widetilde T_a\circ R.
$$

對 task coordinate，則可加：

$$
\operatorname{TaskSufficient}(R,\tau).
$$

這會讓 FCSR 起源命題第一次擁有一個可以跨 Facelet、Cubie、Coordinate、未來多面體 puzzle 重用的形式化 representation interface。

---

## 22. 表示與 solver 的真正關係

solver 可以抽象成：

$$
\operatorname{Solve}(s;R,H,A),
$$

其中：

- $R$：工作 representation；
- $H$：heuristic / pruning knowledge；
- $A$：search algorithm。

因此性能更接近：

$$
P
=
F(R,H,A,\text{hardware},\text{precomputation}),
$$

而不是：

$$
P=F(A).
$$

這解釋了為什麼只比較：

> BFS vs IDA*

往往過度粗糙。

同一個 IDA*，若一個版本每個節點都重建 cubie state，另一個版本以 compact coordinate + move table + pruning table 運行，實際行為可以完全不同。

所以第四篇開始談搜尋演算法時，本文將成為前置條件：

$$
\boxed{
\text{先說明在哪個 representation space 搜尋，再談 search algorithm。}
}
$$

---

## 23. 本文核心命題

### 命題 R1：FCSR flat net 是完整觀察表示，不自動降低 state count

$$
|\operatorname{Im}R_{\mathrm{flat}}|
=
|\mathcal{S}_{\mathrm{legal}}|
$$

在固定合法 frame 與可逆 layout 下成立。

### 命題 R2：Cubie 與 legal facelet representation 可互相重建

$$
\text{Facelet}
\leftrightarrow
\text{Cubie}
$$

在合法固定-frame image 上是無損轉換。

### 命題 R3：單一 task coordinate 通常不是完整狀態

$$
R(s_1)=R(s_2)
$$

可在：

$$
s_1\neq s_2
$$

時成立。

### 命題 R4：Task sufficiency 比 injectivity 更重要

只要：

$$
\tau
=
\hat\tau\circ R,
$$

則 $R$ 即保留任務 $\tau$ 所需資訊。

### 命題 R5：搜尋性能取決於表示與演算法共同設計

$$
\text{solver efficiency}
=
\text{representation}
+
\text{move tables}
+
\text{heuristics}
+
\text{search}.
$$

---

## 24. 結論

本文完成 FDRS/FCSR 經典地基的第三次收斂。

第一篇確立：

$$
\text{同一底層狀態}
\rightarrow
\text{多種表示}.
$$

第二篇確立：

$$
\text{raw encoding}
\neq
\text{legal state}.
$$

第三篇則確立：

$$
\boxed{
\text{representation}
\neq
\text{solver},
}
$$

但同時：

$$
\boxed{
\text{representation can determine what solver is computationally practical}.
}
$$

Facelet 與 FCSR flat net 的價值主要在觀察與交互。

Cubie representation 把 piece identity、permutation 與 orientation 顯式化。

Full coordinates 把完整結構映射成有限整數。

Task coordinates 把對當前子問題不重要的差異商掉。

Symmetry coordinates 再把等價狀態合併。

Pruning tables 最終把 representation 轉換成搜尋下界。

因此 FDRS 的起源命題現在可以得到一個更成熟的計算版本：

$$
\boxed{
\text{困難不只取決於問題本身，也取決於你要求計算機在哪一個表示空間裡工作。}
}
$$

下一篇將正式進入搜尋：

**《從狀態圖到搜尋：BFS、雙向搜尋、A* 與 IDA* 的統一語義》**。

但從下一篇開始，任何演算法都必須先回答：

> 它到底是在什麼 state / coordinate graph 上搜尋？

---

## 參考資料與來源定位

### 起源文件

- [F2025-A] Neo.K，《展平式維度重構理論：完整數學架構與概念解析》，2025 年 8 月。
- [F2025-B] Neo.K，《展平式維度重構理論：從 FCSR 到 FDRS 的完整數學架構》，2025 年 8 月。
- [F2026-D] `FDRS_展開收斂_同步性.html`，FDRS/FCSR 魔方可視化與 IDA* 實驗原型。

### 外部計算基線

- [R1] Herbert Kociemba, **The Facelet Level**.  
  https://kociemba.org/math/faceletlevel.htm

- [R2] Herbert Kociemba, **The Cubie Level**.  
  https://kociemba.org/math/cubielevel.htm

- [R3] Herbert Kociemba, **The Coordinate Level**.  
  https://kociemba.org/math/coordlevel.htm

- [R4] Herbert Kociemba, **Cosets**.  
  https://kociemba.org/math/cosets.htm

- [R5] Herbert Kociemba, **The Move Tables**.  
  https://kociemba.org/math/movetables.htm

- [R6] Herbert Kociemba, **Pruning Tables**.  
  https://kociemba.org/math/pruning.htm

- [R7] Herbert Kociemba, **Coordinates and Symmetry**.  
  https://kociemba.org/math/symcord.htm

- [R8] Herbert Kociemba, **Two-Phase Algorithm Details**.  
  https://kociemba.org/math/imptwophase.htm

---

## 版本註記

v0.1 將「展平／降維」拆為三個可分辨概念：

$$
\text{geometric relayout},
$$

$$
\text{lossless re-encoding},
$$

$$
\text{task-oriented quotient / coordinate reduction}.
$$

後續所有 FCSR/FDRS 魔方演算法論述應明確指出使用的是哪一類 representation transform。

後續第四篇：

**《從狀態圖到搜尋：BFS、雙向搜尋、A* 與 IDA* 的統一語義》**。
