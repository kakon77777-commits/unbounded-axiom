# FDRS / FCSR Classical Cube Foundations I
## 起源重建：從 FCSR 色位展平到可驗證魔方計算

**英文題名：** Origin Reconstruction: From FCSR Flat Color-State Representation to Verifiable Cube Computation  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-01  
**版本：** v0.1  
**日期：** 2026-08-19  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 起源正統延續稿

---

## 摘要

FDRS（Flattened Dimensional Reconstructive Theory，展平式維度重構理論）的早期發展並非先從抽象算子或一般高維結構開始，而是由 FCSR（Flat Color-State Resolution）魔術方塊模型出發：將標準魔方的立體外觀展開為平面色位表示，使立體旋轉可以被轉寫為有限位置集合上的離散狀態遷移。其後，FDRS 才逐步由具體魔方模型推廣至一般結構映射、維度重構與 RDCM。

本文回到此一起源線，重新建立一個不依賴後期 FDRS 2.x 抽象算子框架的經典魔方計算基礎。本文保留早期 FCSR 的核心直覺，但修正三個重要混淆。第一，魔方從立體視圖展開為二維網格，首先是一種**表示變換**，不等同於組合狀態空間本身必然降維或變小。第二，合法魔方狀態不是任意的 $6\times9$ 色彩矩陣，而是由合法機械轉動所生成的可達狀態子集。第三，求解器的正確性、完備性與最短性是彼此不同的性質，不應混為「能解」單一命題。

在此基礎上，本文把標準經典魔方定義為有限狀態轉移系統，將 FCSR 定位為該系統的一個觀察／表示層，並以交換圖刻畫立體表示、展平表示與抽象狀態遷移之間的一致性。本文進一步定義 solver contract，使任何 BFS、A*、IDA*、Two-Phase 或後續 AI solver 都可以共享同一個「解序列可被獨立驗證」之語義基礎。此重建使 FCSR 從早期的直觀展平模型轉化為後續形式驗證、演算法比較、多表示同步可視化與多類 twisty puzzle 泛化的共同地基。

**關鍵詞：** FCSR、FDRS、Rubik's Cube、twisty puzzle、狀態表示、置換、有限狀態系統、solver verification、可視化計算、形式驗證

---

## 1. 起源：FDRS 先從魔方開始

2025 年 FDRS 起源文本的核心路徑可以重建為：

$$
\text{Rubik-like Cube}
\rightarrow
\text{FCSR}
\rightarrow
\text{Flattening}
\rightarrow
\text{Transformation}
\rightarrow
\text{Reconstruction}
\rightarrow
\text{FDRS / RDCM}.
$$

原始 FCSR 的直覺非常直接：對人類而言，立體魔方要求同時維持多面空間關係；若把六個面展開為十字形或其他平面網格，原本的立體鄰接可以轉寫成平面位置關係，而面轉動則可以寫成色位的機械化遷移規則。

這個起點具有兩個不同層次。

第一層是認知與可視化層：同一個魔方狀態可以在不同觀察形式中呈現。

第二層是計算層：一旦位置與操作被離散化，魔方就可以被視為一個有限狀態轉移系統。

早期文本曾把兩者緊密地描述成「高維到低維展平」。本文保留這個歷史語義，但在現代重建中把它們分開，以避免把「畫面上的幾何降維」直接等同於「組合問題的計算複雜度下降」。

因此，本系列中的 FCSR 不再被定義為「魔方求解法」，而被定義為：

> 一套把同一個 twisty puzzle 抽象狀態投影到可讀、可操作、可同步驗證之表示空間的觀察層。

---

## 2. 現代基線：經典 $3\times3\times3$ 已是一個成熟計算問題

對標準 $3\times3\times3$ 魔方而言，計算求解早已不是「是否存在算法」的問題。標準合法狀態空間共有

$$
43{,}252{,}003{,}274{,}489{,}856{,}000
$$

個可達位置。2010 年的完整計算結果證明，在 half-turn metric（HTM）下，每個合法位置都可在至多 $20$ 步內解決；2014 年進一步確立 quarter-turn metric（QTM）的對應最壞情況為 $26$ 步。

因此，本文不把「電腦能解魔方」視為新結果。真正值得重建的是：

1. 狀態應如何被精確表示；
2. 不同表示是否共享同一個底層語義；
3. move 如何在不同表示間保持一致；
4. solver 輸出的解如何被獨立驗證；
5. 搜尋過程如何被可視化；
6. 後續如何將同一架構泛化到更多 twisty puzzle。

現代經典高效方法亦已展示「表示選擇」對求解效率的重要性。Kociemba Two-Phase Algorithm 將完整狀態先送入子群

$$
G_1=\langle U,D,R^2,L^2,F^2,B^2\rangle,
$$

第一階段使用角塊朝向、邊塊朝向與 UD-slice 等座標，搭配 IDA* 與 pruning table 尋找進入 $G_1$ 的路徑；第二階段再於受限 move set 中完成排列。這說明「求解性能」並不只取決於搜尋器名稱，而高度依賴狀態座標、商空間、下界估計與剪枝結構。

對 FCSR/FDRS 而言，這不是競爭關係，而是一個重要提醒：

$$
\text{representation}
\neq
\text{visual appearance only}.
$$

表示可以直接改變計算代價。

---

## 3. 第一個修正：幾何展平不等於狀態空間降維

令抽象合法狀態集合為 $\mathcal{S}$。

一個具體魔方狀態 $s\in\mathcal{S}$ 可以有多個表示：

$$
R_{3D}:\mathcal{S}\rightarrow\mathcal{V}_{3D},
$$

$$
R_{\mathrm{flat}}:\mathcal{S}\rightarrow\mathcal{V}_{2D},
$$

$$
R_{\mathrm{facelet}}:\mathcal{S}\rightarrow\mathcal{C}^{54},
$$

$$
R_{\mathrm{cubie}}:\mathcal{S}\rightarrow\mathcal{K},
$$

$$
R_{\mathrm{perm}}:\mathcal{S}\rightarrow\mathfrak{S}_{54}.
$$

這些表示描述的是同一個底層狀態，但它們的資料結構、認知負荷與演算法效率可以不同。

因此，從三維視覺模型切換到二維 FCSR net，比較精確的說法不是：

$$
\text{state dimension }3\rightarrow2,
$$

而是：

$$
R_{3D}(s)\rightarrow R_{\mathrm{flat}}(s).
$$

其幾何呈現維度下降，但底層有限組合狀態並沒有因此自動縮小。

這個修正並不否定早期 FDRS 的核心洞見。相反，它把洞見變得更精確：

> 複雜性可能來自表示；改變表示可以改變觀察、操作與搜尋成本，但不能在沒有額外證明的情況下宣稱底層組合複雜度已被消除。

---

## 4. 經典魔方的有限狀態轉移模型

定義一個經典 twisty puzzle：

$$
\mathcal{P}=(\mathcal{S},\mathcal{A},T,s_\star,\mu),
$$

其中：

- $\mathcal{S}$ 為合法狀態集合；
- $\mathcal{A}$ 為基本操作集合；
- $T:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S}$ 為狀態轉移；
- $s_\star\in\mathcal{S}$ 為 solved state；
- $\mu$ 為 move metric。

對標準 $3\times3\times3$，可取基本 face move 生成元：

$$
\mathcal{G}=\{U,D,L,R,F,B\}.
$$

若把逆轉與半轉直接納入 move alphabet，常用搜尋 move 集可以寫成：

$$
\mathcal{A}_{18}
=
\{U,U',U^2,D,D',D^2,L,L',L^2,R,R',R^2,F,F',F^2,B,B',B^2\}.
$$

每個 move 都是可逆的，因此對任意 $a\in\mathcal{A}$ 存在 $a^{-1}$，滿足：

$$
T(T(s,a),a^{-1})=s.
$$

對 move sequence

$$
p=(a_1,a_2,\ldots,a_k),
$$

定義其延伸轉移：

$$
T^\ast(s,p)
=
T(\cdots T(T(s,a_1),a_2)\cdots,a_k).
$$

這就是所有經典 solver 的共同語義地基。

---

## 5. 第二個修正：Facelet array 不是合法狀態集合本身

早期 FCSR 使用 $54$ 個色位表示魔方，這是合理且非常適合可視化的 encoding。但若令顏色集合為 $\mathcal{C}$，則

$$
\mathcal{C}^{54}
$$

包含大量不可能由合法魔方轉動產生的配置。

因此應區分：

$$
\mathcal{E}_{54}=\mathcal{C}^{54}
$$

與

$$
\mathcal{S}_{\mathrm{legal}}
\subsetneq
\mathcal{E}_{54}.
$$

FCSR facelet encoding 是映射：

$$
E_{\mathrm{FCSR}}:
\mathcal{S}_{\mathrm{legal}}
\rightarrow
\mathcal{E}_{54}.
$$

它提供完整觀察資料，但「任何 $54$ 格顏色排列都是魔方狀態」並不成立。

這個區分對後續形式驗證非常重要。若 solver 接受任意 facelet array，就必須先執行 legality validation；若 solver 的輸入型別本身已被限制為合法狀態，則合法性可以由型別或構造證明攜帶。

---

## 6. Move 的置換語義

對固定 facelet index set

$$
P=\{0,1,\ldots,53\},
$$

每個基本 move $a$ 可以表示為位置集合上的雙射：

$$
\sigma_a:P\rightarrow P.
$$

因此：

$$
\sigma_a\in\mathrm{Sym}(P).
$$

若 facelet state 寫為

$$
x:P\rightarrow\mathcal{C},
$$

move 的作用可以表示為：

$$
(T_a x)(i)=x(\sigma_a^{-1}(i)).
$$

由於 $\sigma_a$ 為雙射，立刻得到 move 可逆性。

這裡應特別注意：置換語義不是因為 FCSR 把魔方「畫平」才成立。它來自魔方本身的離散可逆操作結構。FCSR 的價值在於把這個置換作用以人類可見的形式同步呈現出來。

---

## 7. FCSR 的核心定理應重寫為「表示－操作交換性」

令

$$
R_i:\mathcal{S}\rightarrow\mathcal{V}_i
$$

為第 $i$ 種表示。

若對每個 move $a$，存在表示域中的對應操作

$$
\widetilde{T}_{i,a}:\mathcal{V}_i\rightarrow\mathcal{V}_i,
$$

使得對所有 $s\in\mathcal{S}$：

$$
R_i(T(s,a))
=
\widetilde{T}_{i,a}(R_i(s)),
$$

則稱表示 $R_i$ 對 move semantics 是一致的。

其交換圖為：

$$
\begin{array}{ccc}
\mathcal{S} & \xrightarrow{T_a} & \mathcal{S} \\
\downarrow R_i & & \downarrow R_i \\
\mathcal{V}_i & \xrightarrow{\widetilde{T}_{i,a}} & \mathcal{V}_i
\end{array}
$$

這個命題比「展平保持所有高維本質」弱得多，但也精確得多，而且可以直接被程式測試與 Lean 形式化。

對 FCSR 而言，真正需要證明的是：

$$
R_{\mathrm{flat}}(T(s,a))
=
\widetilde{T}_{\mathrm{flat},a}(R_{\mathrm{flat}}(s)).
$$

若它成立，則在平面 net 上看到的 move 與抽象魔方狀態中的 move 是同一事件的兩種表示。

---

## 8. Solver Contract：能解、總能解、最短解是三件事

令 solver 為：

$$
\mathrm{Solve}:
\mathcal{S}
\rightarrow
\mathrm{Option}(\mathcal{A}^{\ast}).
$$

### 8.1 Soundness

若 solver 回傳路徑 $p$，則必須真的解掉魔方：

$$
\mathrm{Solve}(s)=\mathrm{some}(p)
\Rightarrow
T^\ast(s,p)=s_\star.
$$

這是最基本的 solver correctness。

### 8.2 Completeness

若輸入是可達合法狀態，solver 最終應能回傳某個解：

$$
s\in\mathcal{S}_{\mathrm{legal}}
\Rightarrow
\exists p,\;
\mathrm{Solve}(s)=\mathrm{some}(p).
$$

這比 soundness 更強。

### 8.3 Optimality

對 metric $\mu$，若 solver 回傳 $p$，還可以要求：

$$
\forall q,\;
T^\ast(s,q)=s_\star
\Rightarrow
\mu(p)\leq\mu(q).
$$

這才是最短解。

因此：

$$
\text{sound}
\not\Rightarrow
\text{complete}
\not\Rightarrow
\text{optimal}.
$$

後續 BFS、IDA*、Two-Phase 與 AI solver 都應放進同一 contract 下比較，而不是只以執行時間或 move count 混合評價。

---

## 9. 最短路徑存在性：應限定在合法可達域

對固定合法魔方，move 生成一個有限圖：

$$
\Gamma=(V,E),
$$

其中：

$$
V=\mathcal{S}_{\mathrm{legal}},
$$

且若存在 $a\in\mathcal{A}$ 使得

$$
T(s,a)=s',
$$

則 $(s,s')\in E$。

由於每個 move 可逆，對標準魔方的合法可達分量，任意狀態與 solved state 之間存在有限路徑。又因圖有限，所有解路徑長度的非空集合在自然數上存在最小值，因此最短解存在。

這裡不需要先使用 God's Number 才能證明「最短解存在」。God's Number 回答的是更強的全域直徑問題：

$$
\max_{s\in\mathcal{S}_{\mathrm{legal}}}
d(s,s_\star).
$$

在 HTM 下此值為 $20$ ；QTM 下為 $26$。

---

## 10. FCSR 新定位：Observer Layer，而非 Solver 本身

本文建議把 FCSR 重新定位為：

$$
\boxed{
\text{FCSR}
=
\text{State Representation}
+
\text{Operation Projection}
+
\text{Synchronized Visualization}.
}
$$

它不與 BFS、IDA* 或 Two-Phase 競爭。

相反，solver 可以被插入 FCSR：

$$
\text{State}
\rightarrow
\text{Solver}
\rightarrow
\text{Move Sequence},
$$

同時每一步都同步顯示：

$$
R_{3D}(s_t),
\quad
R_{\mathrm{flat}}(s_t),
\quad
R_{\mathrm{perm}}(s_t),
\quad
R_{\mathrm{cubie}}(s_t),
\quad
R_{\mathrm{search}}(s_t).
$$

因此，FCSR 的工程優勢是讓使用者同時看到：

1. 魔方現在長什麼樣；
2. 展平後如何表示；
3. 哪些位置被 move 置換；
4. solver 如何評估當前狀態；
5. 哪些搜尋分支被剪掉；
6. 最終解序列如何被逐步驗證。

這比單純顯示「Solved in 0.02 s」更接近本研究的核心。

---

## 11. 從 2025 Demo 到新版實驗室

2025/2026 已有 FDRS 魔方網頁原型實作 permutation-based engine、IDA*、adjacency graph、連通分量、FSM 與 $3D\leftrightarrow2D$ 連續 morph。

新版不應推翻該原型，而應將其拆成可驗證的模組：

$$
\text{Twisty State Kernel}
$$

$$
+
$$

$$
\text{Representation Adapters}
$$

$$
+
$$

$$
\text{Solver Interface}
$$

$$
+
$$

$$
\text{Search Instrumentation}
$$

$$
+
$$

$$
\text{Visualization Runtime}.
$$

最關鍵的工程原則是：

> 所有畫面表示必須讀取同一個 canonical state；所有 solver 必須透過同一個 move semantics 修改狀態；任何表示都不能私自維護一套不同的魔方真相。

---

## 12. 形式驗證的第一批目標

後續 Lean 形式化不應先從「證明 IDA* 很快」開始，而應從最小可信核心開始。

第一批建議目標：

### F1. Move invertibility

$$
\forall s,a,\;
T(T(s,a),a^{-1})=s.
$$

### F2. Sequence composition

$$
T^\ast(T^\ast(s,p),q)
=
T^\ast(s,p\mathbin{+\!\!+}q).
$$

### F3. Representation consistency

$$
R_i(T(s,a))
=
\widetilde{T}_{i,a}(R_i(s)).
$$

### F4. Solution certificate correctness

$$
\mathrm{Check}(s,p)=\mathrm{true}
\Rightarrow
T^\ast(s,p)=s_\star.
$$

### F5. Solver soundness

$$
\mathrm{Solve}(s)=\mathrm{some}(p)
\Rightarrow
\mathrm{Check}(s,p)=\mathrm{true}.
$$

一旦 F1--F5 完成，任何未形式化的高速 solver 也可以先作為「不可信搜尋器」，只要它輸出的解序列交給已形式化 checker 驗證，就可以得到可信的最終求解結果。

這是後續把高效工程與嚴格形式驗證拆開的關鍵。

---

## 13. 與人類速解的關係

本研究不以取代或貶低 speedcubing 為目的。

人類 speedcubing 的主要限制與優化對象包括感知、模式識別、公式重編碼、記憶、預判與手部動作；計算機 solver 則主要處理狀態編碼、搜尋、剪枝、子群分解、查表與證書驗證。兩者共享同一個 puzzle，但優化的資源完全不同。

因此本系列的 KPI 不設定為「比人快」，而設定為：

$$
\text{correctness},
\quad
\text{coverage},
\quad
\text{representation clarity},
\quad
\text{verifiability},
\quad
\text{algorithm observability},
\quad
\text{generality}.
$$

換句話說，我們更在乎：

> 能否讓人與 AI 清楚看到同一個有限狀態世界，是如何被不同表示、不同算法與不同證明層共同處理。

---

## 14. 本文核心命題

本文將 FCSR 的正統起源命題重新收斂為以下五項。

### 命題 O1：抽象狀態優先

魔方本體的計算語義由合法狀態與 move transition 定義； $3D$ 、 $2D$ 、facelet、cubie 與 permutation 都是其表示。

### 命題 O2：展平是表示轉換

FCSR 的 $3D\rightarrow2D$ 首先是 observation / representation transform，不自動推出組合狀態空間縮小。

### 命題 O3：操作必須跨表示一致

任何可接受的 FCSR 表示必須滿足 move semantics 的交換性。

### 命題 O4：solver 與表示解耦

solver 應作用於 canonical state 或其經證明等價的 coordinate representation，而可視化只是同步觀察層。

### 命題 O5：解應可被獨立驗證

solver 的核心輸出不是「相信我已經解了」，而是一個可重播、可檢查、可形式驗證的 move certificate。

---

## 15. 結論

FCSR 的歷史價值不在於它曾提出另一套人類魔方公式，而在於它把魔方視為「同一狀態在不同觀察空間中仍可保持操作語義」的具體示範。

早期 FDRS 從這個具體問題向一般維度重構理論展開；後續 FDRS 2.x 又進一步進入抽象算子與鏈複形。本系列現在做的是另一件事：回到起點，把當年沒有充分形式化的具體計算地基重新完成。

因此，本系列的第一個核心公式不是新的求解捷徑，而是：

$$
\boxed{
R_i(T(s,a))
=
\widetilde{T}_{i,a}(R_i(s)).
}
$$

它說明同一個 move 可以被立體視圖、FCSR 平面網格、置換結構、cubie state 與搜尋器同時理解，而且這些理解必須對同一個底層事件保持一致。

一旦這個地基成立，下一步才能合理地比較不同表示、不同搜尋算法、不同 heuristic、不同證明策略，以及最終擴張到多類 twisty puzzle。

在更遠的未來，當經典固定規則域被完整處理後，才有充分基礎解除其 stationary assumptions，進入 Dynamic Cube / Dynamic Twisty Systems。

---

## 參考資料與來源定位

### 起源文件

- [F2025-A] Neo.K，《展平式維度重構理論：完整數學架構與概念解析》，2025 年 8 月。
- [F2025-B] Neo.K，《展平式維度重構理論：從 FCSR 到 FDRS 的完整數學架構》，2025 年 8 月。
- [F2025-C] Neo.K & Claude，《展平式維度重構理論作為通用問題解決框架：機會與風險的平衡分析》，2025 年 9 月。
- [F2026-D] `FDRS_展開收斂_同步性.html`，FDRS/FCSR 魔方可視化與 IDA* 實驗原型。
- [F2026-E] 《展平式維度重構理論 II：連接算子統一框架 v2.1》，2026 年 6 月。本文僅用其確認後期理論分支歷史，不以其覆寫 FCSR 起源定義。

### 外部計算基線

- [R1] Tomas Rokicki, Herbert Kociemba, Morley Davidson, John Dethridge，God's Number is 20，2010。用於 HTM 全域直徑與標準合法狀態總數基線。
- [R2] Tomas Rokicki, Morley Davidson，God's Number is 26 in the Quarter-Turn Metric，2014。用於 QTM 全域直徑基線。
- [R3] Herbert Kociemba，The Two-Phase Algorithm / Two-Phase Algorithm Details。用於 $G_1$ 、coordinate、IDA*、pruning table 與 two-phase 設計基線。
- [R4] World Cube Association，WCA Regulations，2026。用於現代競賽規則與 move / event 語境參照。

---

## 版本註記

v0.1 的任務不是宣稱 FCSR 已經證明一般性的「高維無損降維」，而是把其魔方起源重新寫成可以被程式、演算法與形式證明逐步驗證的有限離散命題。

後續第二篇將處理：

**《合法狀態與群作用：魔方狀態空間的嚴格計算模型》**。
