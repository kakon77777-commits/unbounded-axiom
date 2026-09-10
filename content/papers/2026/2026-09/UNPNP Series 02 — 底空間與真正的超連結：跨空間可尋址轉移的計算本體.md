# UNPNP Series 02  
## 底空間與真正的超連結：跨空間可尋址轉移的計算本體  
### Subspaces and Real Hyperlinks: An Ontology of Addressable Cross-Space Transitions

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 02  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** 計算本體論／AI 原生計算架構論文  
**狀態：** Canonical Draft  

---

## 摘要

傳統 Web 中的 hyperlink 通常被理解為一種介面元件：使用者點擊文字、按鈕或 URL，瀏覽器便從一個頁面移動到另一個頁面。然而，若將這個操作從 UI 表面剝離，可以看到更一般的計算結構：一個可識別的地址，使執行狀態能從目前所在的操作空間，轉移到另一個操作空間。

本文將這種結構稱為**廣義超連結**。其基本形式為：

$$
\ell:
(\mathcal B_i,s_i)
\rightarrow
(\mathcal B_j,s_j),
$$

其中 $\mathcal B_i$ 與 $\mathcal B_j$ 是不同的計算底空間， $s_i$ 與 $s_j$ 是對應狀態，而 $\ell$ 是一個可尋址、可解析、可執行的跨底空間 transition。

本文中的「底空間」不是限定於拓撲學或幾何學中的既定數學術語，而是一個操作性計算概念：它表示一組具有自身狀態、地址、操作子、邊界、資料與驗證規則的局部計算世界。檔案系統、函數作用域、資料庫、Web 頁面、API、遊戲場景、模組、Agent 工具環境與語義記憶圖，都可以在適當抽象層級上被視為底空間。

本文進一步提出：

$$
\boxed{
\text{Hyperlink}
=
\text{Addressable Cross-Subspace Transition}
}
$$

因此 Web URL 只是廣義超連結的一種表面實作。函數位址、資料庫 key、檔案路徑、API endpoint、object reference、content hash、semantic address、graph edge、capability reference，以及由程序動態生成的 intensional address，都可以是廣義超連結的不同實作。

本文亦區分「UI traversal」與「semantic direct addressing」。人類常透過滑鼠、畫面辨識、層級選單與逐步操作進入新空間；AI 原生 runtime 則可以直接使用符號、狀態與語義地址，在不重置整體工作狀態的情況下連續跨越多個底空間。由此形成：

$$
\boxed{
\text{Subspace Boundary}
\not\Rightarrow
\text{Reasoning Reset}.
}
$$

在 UNPNP 框架中，這種能力使巨大計算空間可以被改寫為跨底空間的 transition network。真正的研究焦點不再只是「如何在一個空間中搜尋」，而是：

> 如何找到、驗證、穿越並最終重新編譯跨空間的有效 transition？

本文為後續自適應快速通道、展開—連結—收斂、耦合計算、路徑編譯與結晶化超連結建立正式計算本體。

**關鍵詞：** UNPNP、底空間、超連結、跨空間計算、直接尋址、AI 原生計算、semantic address、typed transition、MSSP、hypergraph、path compilation

---

# 1. 超連結從來不只是藍色文字

一般使用者所見的超連結通常是：

```text
Page A
→ click
→ Page B
```

因此超連結容易被理解為：

> 一個讓使用者方便跳頁的 Web UI 元件。

但這只是表面。

真正重要的結構是：

$$
\text{Current State}
\rightarrow
\text{Address Resolution}
\rightarrow
\text{New State}.
$$

若目前存在於一個操作空間：

$$
\mathcal B_A,
$$

而某個地址：

$$
a_B
$$

可以將執行狀態轉移到：

$$
\mathcal B_B,
$$

則超連結真正做的是：

$$
\mathcal B_A
\xrightarrow{\ell}
\mathcal B_B.
$$

因此本文提出：

$$
\boxed{
\text{Hyperlink is fundamentally a transition primitive, not a visual widget.}
}
$$

---

# 2. 底空間的操作性定義

本文將一個計算底空間定義為：

$$
\boxed{
\mathcal B_i
=
\langle
S_i,
A_i,
O_i,
D_i,
V_i,
C_i
\rangle.
}
$$

其中：

- $S_i$：state space，底空間可表達的狀態；
- $A_i$：address space，可識別的內部與外部地址；
- $O_i$：operator set，可在底空間內執行的操作；
- $D_i$：data / object domain，可操作資料與物件；
- $V_i$：validation rules，狀態與結果的驗證規則；
- $C_i$：capability boundary，可用能力與權限邊界。

這個定義刻意保持抽象。

因為底空間可以是一個：

- Web page；
- process；
- function scope；
- class / object graph；
- database；
- game scene；
- inventory；
- combat state；
- repository；
- filesystem subtree；
- API domain；
- knowledge graph；
- memory region；
- agent tool environment；
- semantic field。

底空間不是固定尺度。

---

# 3. 底空間具有巢狀性

一個底空間內可以包含其他底空間。

形式上：

$$
\mathcal B_i
\supset
\{
\mathcal B_{i1},
\mathcal B_{i2},
\ldots,
\mathcal B_{in}
\}.
$$

例如遊戲世界：

$$
\mathcal B_{\mathrm{game}}
$$

可以包含：

$$
\mathcal B_{\mathrm{world}},
\mathcal B_{\mathrm{city}},
\mathcal B_{\mathrm{combat}},
\mathcal B_{\mathrm{inventory}},
\mathcal B_{\mathrm{dialogue}}.
$$

而：

$$
\mathcal B_{\mathrm{combat}}
$$

又可以包含：

$$
\mathcal B_{\mathrm{target}},
\mathcal B_{\mathrm{position}},
\mathcal B_{\mathrm{ability}},
\mathcal B_{\mathrm{resource}}.
$$

因此：

$$
\boxed{
\text{Subspace is scale-relative.}
}
$$

同一個結構在上一層可以是一個節點，在下一層則可以展開成整個內部世界。

---

# 4. 底空間不是資料夾

需要避免一個過度簡化。

底空間不是：

> 把不同資料放進不同資料夾。

真正的底空間至少要有局部計算語義。

也就是：

$$
\mathcal B_i
$$

不只是保存資料，而是決定：

- 什麼狀態在這裡有效；
- 什麼地址可解析；
- 什麼操作可執行；
- 什麼資料可見；
- 什麼 transition 可以離開；
- 什麼結果算有效。

所以：

$$
\boxed{
\text{Container}
\neq
\text{Computational Subspace}.
}
$$

一個資料夾可以被當作底空間，但只有在系統賦予它操作邊界與狀態語義之後才成立。

---

# 5. 廣義超連結的基本定義

令：

$$
\mathcal B_i
$$

與：

$$
\mathcal B_j
$$

為兩個底空間。

則一個廣義超連結：

$$
\ell_{ij}
$$

定義為：

$$
\boxed{
\ell_{ij}:
(\mathcal B_i,s_i)
\rightarrow
(\mathcal B_j,s_j).
}
$$

它至少要回答：

1. 從哪裡出發？
2. 到哪裡？
3. 需要什麼輸入？
4. 轉移時執行什麼？
5. 哪些狀態被攜帶？
6. 到達後產生什麼狀態？
7. 如何知道轉移成功？

所以真正可執行的超連結不是一個裸地址。

它是一個 transition contract。

---

# 6. Typed Hyperlink

本文提出第一版 typed hyperlink：

$$
\boxed{
\ell
=
\langle
a,
\tau,
I,
G,
E,
O,
V,
P
\rangle.
}
$$

其中：

- $a$：address；
- $\tau$：transition type；
- $I$：input contract；
- $G$：guard / precondition；
- $E$：execution semantics；
- $O$：output / postcondition；
- $V$：validator；
- $P$：provenance。

因此：

$$
\operatorname{Traverse}(\ell,s)
$$

不是單純「開啟一個位置」，而是：

$$
\operatorname{Traverse}(\ell,s)
\rightarrow
(s',o,v,p).
$$

其中：

- $s'$：新狀態；
- $o$：observation；
- $v$：validation result；
- $p$：provenance / receipt。

---

# 7. Web URL 只是超連結的一種 Surface

Web 中：

$$
a=
\text{URL}.
$$

但廣義計算中，地址可以是：

$$
a\in
\{
\text{URL},
\text{filepath},
\text{function},
\text{database key},
\text{API endpoint},
\text{object ID},
\text{graph node},
\text{hash},
\text{semantic address},
\text{capability reference}
\}.
$$

因此：

$$
\boxed{
\text{Hyperlink}
\neq
\text{URL}.
}
$$

更準確地說：

$$
\boxed{
\text{URL}
\subset
\text{Hyperlink Surfaces}.
}
$$

---

# 8. Extensional Address 與 Intensional Address

傳統地址通常回答：

> 東西在哪裡？

例如：

$$
a_{\mathrm{ext}}
=
\text{location}(x).
$$

本文稱為 extensional address。

但 AI 原生計算還可能使用另一種地址：

> 如何生成我要的下一個狀態？

令：

$$
a_{\mathrm{int}}
=
\operatorname{GenerateSpec}(x).
$$

則：

$$
a_{\mathrm{int}}
$$

不直接指向已存在物件，而指向一個可生成該物件或狀態的 procedure。

因此：

$$
\boxed{
\text{Address}
=
\text{Location}
\cup
\text{Procedure}.
}
$$

更一般地：

$$
\boxed{
\text{Address}
=
\text{Resolvable Transition Specification}.
}
$$

這將成為後續「尋址即生成」的重要基礎。

---

# 9. 直接尋址與 UI Traversal

人類常以 GUI 執行：

$$
S_0
\rightarrow
S_1
\rightarrow
S_2
\rightarrow
\cdots
\rightarrow
S_k.
$$

例如：

```text
打開選單
→ 找到背包
→ 點擊物品
→ 找藥水
→ 選擇角色
→ 確認
```

這種路徑包含大量：

- 視覺辨識；
- 操作定位；
- 選單切換；
- 畫面重讀；
- 人類動作成本。

若存在語義地址：

$$
a=
\operatorname{UseBestHealingItem}(\text{character}),
$$

AI 原生 runtime 可以直接：

$$
S_0
\xrightarrow{a}
S_k.
$$

因此：

$$
\boxed{
\text{UI traversal}
\neq
\text{semantic addressing}.
}
$$

UI 是為人類操作設計的表面。

AI 不必永遠模仿人類 UI 路徑。

---

# 10. 為什麼終端機常給人「更快」的感覺？

終端機並不是因為文字本身具有神秘速度。

真正的差異是：

$$
\boxed{
\text{symbolic direct addressing}.
}
$$

GUI 常需要：

$$
\text{perceive}
\rightarrow
\text{locate}
\rightarrow
\text{move}
\rightarrow
\text{click}
\rightarrow
\text{perceive again}.
$$

命令列則可能：

$$
\text{symbol}
\rightarrow
\text{address}
\rightarrow
\text{execute}.
$$

所以真正的效率來源不是：

$$
\text{mouse}<\text{keyboard}.
$$

而是：

$$
\boxed{
\text{indirect navigation}
<
\text{direct symbolic addressing}.
}
$$

這個原理可以被 AI 原生計算進一步放大。

---

# 11. 跨底空間不應等於認知重置

人類點進新頁面後通常需要重新理解：

> 我現在在哪裡？

> 這一頁在說什麼？

> 接下來要做什麼？

所以人類 traversal 常近似：

$$
\mathcal B_i
\rightarrow
\text{cognitive reset}
\rightarrow
\mathcal B_j.
$$

但 AI runtime 可以保持一個跨空間狀態：

$$
H_t.
$$

於是：

$$
(\mathcal B_i,H_t)
\xrightarrow{\ell}
(\mathcal B_j,H_{t+1}).
$$

因此本文提出：

$$
\boxed{
\text{Subspace Boundary}
\not\Rightarrow
\text{Reasoning Reset}.
}
$$

這是 AI 相對於人類操作介面最重要的計算優勢之一。

---

# 12. State-Carrying Hyperlink

更完整地，超連結不只轉移位置，也可以攜帶狀態。

令：

$$
h_t
$$

表示跨空間工作狀態。

則：

$$
\ell:
(\mathcal B_i,s_i,h_t)
\rightarrow
(\mathcal B_j,s_j,h_{t+1}).
$$

其中：

$$
h_{t+1}
=
U(h_t,o_j).
$$

所以 link 可以同時攜帶：

- 任務；
- 目標；
- 已知證據；
- 當前假說；
- 權限狀態；
- 資源預算；
- 搜尋歷史；
- 失敗記錄；
- 下一步條件。

這讓多底空間 traversal 形成連續計算，而不是多個互不相干的工具呼叫。

---

# 13. Hyperlink Chain

若：

$$
\ell_1:
\mathcal B_1
\rightarrow
\mathcal B_2,
$$

$$
\ell_2:
\mathcal B_2
\rightarrow
\mathcal B_3,
$$

則：

$$
\ell_2\circ\ell_1
$$

形成一個兩階 transition。

一般化：

$$
\Gamma
=
\ell_n
\circ
\ell_{n-1}
\circ
\cdots
\circ
\ell_1.
$$

因此：

$$
\Gamma:
\mathcal B_0
\rightarrow
\mathcal B_n.
$$

第一次執行時：

$$
\Gamma
$$

可能真的需要逐步 traversal。

後續路徑編譯則可能將：

$$
\Gamma
$$

重新結晶為：

$$
\widehat{\ell}_{0n}.
$$

因此：

$$
\boxed{
\text{Hyperlink chain}
\rightarrow
\text{compiled hyperlink}
}
$$

是後續計算結晶化的核心接口。

---

# 14. 搜尋不再只尋找內容，而是尋找 Link

傳統搜尋：

$$
q
\rightarrow
\{d_1,d_2,\ldots,d_k\}.
$$

其中：

$$
d_i
$$

通常是文件或結果。

但在跨底空間計算中，更核心的輸出可以變成：

$$
q
\rightarrow
\{\ell_1,\ell_2,\ldots,\ell_m\}.
$$

也就是：

> 哪些 transition 可以把目前狀態帶往更有價值的底空間？

因此：

$$
\boxed{
\text{Search}
=
\text{Candidate Transition Discovery}.
}
$$

文件本身只是某些 transition 的證據或中介。

---

# 15. Semantic Revealing 作為 Link Frontier 顯影

設完整可用 transition 集合：

$$
\mathcal L.
$$

AI 不應每次對：

$$
|\mathcal L|
$$

全部做深度推理。

可以依目前條件：

$$
\xi_t
$$

生成局部 frontier：

$$
F_t
=
\Pi_{\xi_t}(\mathcal L).
$$

其中：

$$
F_t
\subset
\mathcal L,
$$

且理想情況：

$$
|F_t|
\ll
|\mathcal L|.
$$

這裡：

$$
\Pi_{\xi_t}
$$

可以由：

- 語義顯影；
- DRC；
- graph search；
- exact search；
- temporal filtering；
- constraint filtering；
- identity resolution；
- learned routing；

等方法共同構成。

所以顯影的不是「全部世界」。

而是：

$$
\boxed{
\text{the currently actionable hyperlink frontier}.
}
$$

---

# 16. 底空間之間的 transition 不一定對稱

若：

$$
\ell_{ij}:
\mathcal B_i
\rightarrow
\mathcal B_j
$$

存在，

不代表：

$$
\ell_{ji}
$$

也存在。

因此：

$$
\boxed{
\mathcal B_i\rightarrow\mathcal B_j
\centernot\Rightarrow
\mathcal B_j\rightarrow\mathcal B_i.
}
$$

這可能來自：

- 不可逆狀態；
- 資料損失；
- 權限限制；
- side effect；
- 時間前進；
- destructive mutation；
- one-way transformation。

所以 Hyperlink Graph 一般不是 undirected graph。

它更適合表示成：

$$
G_H=(V,E)
$$

的有向圖，甚至有向超圖。

---

# 17. 從 Graph 到 Hypergraph

傳統二元 link：

$$
\ell:
B_i\rightarrow B_j.
$$

但很多 transition 需要多個前置空間共同成立。

例如：

$$
\{
B_{\mathrm{inventory}},
B_{\mathrm{skill}},
B_{\mathrm{position}}
\}
\rightarrow
B_{\mathrm{combat-action}}.
$$

這時更自然的是 hyperedge：

$$
e:
\{B_1,B_2,\ldots,B_k\}
\rightarrow
B_j.
$$

因此更一般的計算結構是：

$$
\boxed{
\mathcal H
=
(V,\mathcal E).
}
$$

其中：

$$
\mathcal E
$$

可以承載：

- 多來源狀態；
- 多重前置條件；
- 多輸入資料；
- 聯合權限；
- 複合驗證條件。

這與自指 Hypergraph Programming 的思想形成自然接口，但本文不要求所有實作必須採用同一種 hypergraph representation。

---

# 18. 自指底空間

一個節點可以在當前層級被視為：

$$
v_i.
$$

但需要時展開為：

$$
\rho(v_i)=\mathcal H_i.
$$

因此：

$$
\boxed{
\text{node at level }k
=
\text{subspace at level }k+1.
}
$$

這形成：

$$
v_i
\rightarrow
\mathcal B_i
\rightarrow
\{v_{i1},v_{i2},\ldots\}.
$$

所以：

> 一個已經結晶化的超連結，在上一層可以是一個 primitive；在下一層仍可以展開回完整 traversal。

這為後續「結晶可以解壓」建立結構基礎。

---

# 19. MSSP 與底空間

MSSP 的母集—子集思想可以與底空間形成結構對應。

一個 MSSP 可看成：

$$
\mathcal M
=
(F,C,S,T,D,R,X),
$$

其中不同模組具有：

- 身分；
- 穩定性；
- 任務性；
- 設定契約；
- 診斷；
- 路由；
- 執行。

若將一個 MSSP instance 視為：

$$
\mathcal B_i,
$$

則其內部 TMS 或子 MSSP 可以形成：

$$
\mathcal B_{ij}.
$$

因此：

$$
\boxed{
\text{Nested MSSP}
\approx
\text{Nested Computational Subspaces}
}
$$

但兩者不是定義同一物件。

MSSP 是架構方法。

底空間是 UNPNP 中的計算本體。

兩者可以相互映射，但不應混為同一理論。

---

# 20. Reachability 與 Computability

若從：

$$
B_i
$$

存在 transition chain：

$$
B_i
\rightsquigarrow
B_j,
$$

則：

$$
B_j
$$

對目前系統而言是 reachable。

但：

$$
\boxed{
\text{Reachable}
\neq
\text{Cheap}.
}
$$

也：

$$
\boxed{
\text{Reachable}
\neq
\text{Authorized}.
}
$$

更不是：

$$
\boxed{
\text{Reachable}
\Rightarrow
\text{Globally Optimal}.
}
$$

所以 UNPNP 後續需要把：

$$
\text{reachability},
\text{cost},
\text{authorization},
\text{verification},
\text{optimality}
$$

分開。

本文只建立 transition ontology，不在此處提前完成安全與最短路徑理論。

---

# 21. Transition Cost

每條 link 都有成本：

$$
C(\ell).
$$

其成本可能包含：

$$
C(\ell)
=
C_A
+
C_R
+
C_E
+
C_V
+
C_S.
$$

其中：

- $C_A$：address resolution；
- $C_R$：routing；
- $C_E$：execution；
- $C_V$：verification；
- $C_S$：state transfer。

一條路徑：

$$
\Gamma
=
(\ell_1,\ldots,\ell_n)
$$

的成本可以寫成：

$$
C(\Gamma)
=
\sum_{i=1}^{n}C(\ell_i)
+
C_{\mathrm{boundary}}
+
C_{\mathrm{coordination}}.
$$

如果 path compilation 能消除大量 boundary cost：

$$
C(\widehat{\ell})
<
C(\Gamma),
$$

那麼新的超連結才具有真正計算價值。

---

# 22. 快速通道的真正來源：移除邊界成本

很多軟體流程慢，不只因為核心運算慢。

還因為：

$$
\text{serialize}
\rightarrow
\text{transfer}
\rightarrow
\text{parse}
\rightarrow
\text{reconstruct}
\rightarrow
\text{revalidate}
$$

在每個底空間邊界反覆發生。

因此：

$$
C_{\mathrm{boundary}}
$$

可能非常大。

如果一段：

$$
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
B_n
$$

被重新編譯，使中間邊界不再需要完整 materialization，

則：

$$
\boxed{
\text{Path Compression}
=
\text{Transition Reduction}
+
\text{Boundary Reduction}.
}
$$

這是「一個新超連結」能真正比 macro 更快的重要條件之一。

---

# 23. Direct Hyperlink 不代表跳過語義

如果從：

$$
B_1
$$

直接生成：

$$
\widehat{\ell}_{1,100}
$$

到：

$$
B_{100},
$$

真正要求的是保持必要語義：

$$
\operatorname{Semantics}
(\widehat{\ell}_{1,100})
\simeq
\operatorname{Semantics}
(\Gamma_{1,100}).
$$

不是：

> 因為中間步驟看不到，所以它們不重要。

因此：

$$
\boxed{
\text{Direct Transition}
\neq
\text{Unverified Skipping}.
}
$$

後續結晶化必須建立：

- equivalence；
- guard；
- validator；
- fallback；
- provenance。

否則只是把錯誤藏在 shortcut 裡。

---

# 24. 人類與 AI 的根本差異之一

人類非常依賴可視 UI。

這是因為 UI 同時負責：

- 提示目前狀態；
- 顯示可用操作；
- 降低記憶需求；
- 防止錯誤；
- 建立可導航性。

AI 若具備：

$$
\text{state model}
+
\text{typed addresses}
+
\text{tool contracts}
+
\text{semantic routing}
$$

則不必透過完整 UI 才能操作。

因此未來程式可能同時存在兩個表面：

$$
\boxed{
\text{Human Surface}
}
$$

與：

$$
\boxed{
\text{AI Address Surface}.
}
$$

兩者可以指向同一底層計算世界。

這不是取消 GUI，而是承認：

> 人類與 AI 的最佳尋址介面不必相同。

---

# 25. 從 Application 到 Addressable World

傳統應用通常是：

```text
Application
→ screens
→ menus
→ buttons
→ functions
```

AI 原生版本則可以重新表示為：

$$
\mathcal W
=
(\mathcal B,\mathcal L).
$$

其中：

$$
\mathcal B
$$

是底空間，

$$
\mathcal L
$$

是可尋址 transitions。

此時 application 不再主要是一堆畫面。

而是：

$$
\boxed{
\text{Addressable Computational World}.
}
$$

GUI 只是其中一種投影。

CLI、API、Agent tool、semantic interface 也只是其他投影。

---

# 26. UNPNP 中的超連結不是固定集合

設：

$$
\mathcal L_t
$$

為時間 $t$ 可用 link 集合。

傳統程式通常假設：

$$
\mathcal L_{t+1}
\approx
\mathcal L_t
$$

除非程式被人修改。

但 UNPNP Computer 的核心假設之一是：

$$
\boxed{
\mathcal L_{t+1}
\neq
\mathcal L_t
}
$$

可以由 runtime learning 發生。

例如：

$$
\Gamma:
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
B_{100}
$$

經過驗證與編譯後生成：

$$
\widehat{\ell}_{1,100}.
$$

則：

$$
\mathcal L_{t+1}
=
\mathcal L_t
\cup
\{
\widehat{\ell}_{1,100}
\}.
$$

計算世界因此會隨運行而增加新的有效通道。

---

# 27. 超連結的生命週期

一條 AI 生成 link 不應永久有效。

它可以具有生命週期：

$$
\boxed{
\text{candidate}
\rightarrow
\text{tested}
\rightarrow
\text{verified}
\rightarrow
\text{warm}
\rightarrow
\text{hot}
\rightarrow
\text{stale}
\rightarrow
\text{retired}.
}
$$

當底空間改變：

$$
\mathcal B_i(t+1)
\neq
\mathcal B_i(t),
$$

舊 link 可能失效。

所以需要：

$$
\operatorname{Validate}
(\ell,\mathcal B_i(t+1)).
$$

若失敗：

$$
\ell
\rightarrow
\text{repair}
$$

或：

$$
\ell
\rightarrow
\text{retire}.
$$

這使 hyperlink network 成為動態結構，而不是一次建好的靜態圖。

---

# 28. Hyperlink Stability

可以定義一個簡化穩定度：

$$
S_H(\ell)
=
f(
\text{success rate},
\text{semantic invariance},
\text{environment stability},
\text{verification history}
).
$$

若：

$$
S_H(\ell)\ge\theta_H,
$$

則允許更積極重用。

若：

$$
S_H(\ell)<\theta_H,
$$

則降低權重或重新展開。

因此：

$$
\boxed{
\text{Hyperlink reuse should be evidence-weighted}.
}
$$

這將成為路徑結晶化的重要工程條件。

---

# 29. 最短路徑不一定是步數最少

若：

$$
\Gamma_1
$$

只有兩個 transition，

但每一步成本高；

而：

$$
\Gamma_2
$$

有五個 transition，

但總成本低，

則：

$$
|\Gamma_1|<|\Gamma_2|
$$

不代表：

$$
C(\Gamma_1)<C(\Gamma_2).
$$

因此 UNPNP 的 shortest path 更合理地定義為：

$$
\boxed{
\Gamma^\*
=
\arg\min_{\Gamma}
C(\Gamma)
}
$$

而不是：

$$
\arg\min |\Gamma|.
$$

更後續還要加入：

- risk；
- latency；
- energy；
- verification；
- repairability；
- authorization。

所以「超連結越直接越好」本身也不是絕對定律。

---

# 30. 底空間轉移與語義保持

令：

$$
\sigma_i
$$

表示在：

$$
\mathcal B_i
$$

中的任務語義狀態。

一個有效 link 應滿足：

$$
T_{\ell}(\sigma_i)
=
\sigma_j,
$$

並且：

$$
\operatorname{Invariant}
(\sigma_i,\sigma_j)
$$

保持任務所需要的語義不變量。

例如：

- 使用者目標不應無故改變；
- object identity 不應錯置；
- version 不應漂移；
- 已驗證 evidence 不應被未驗證資料覆蓋；
- capability 不應無條件擴張。

這些都不是 URL 自身會處理的。

因此 AI-native hyperlink 必須比 Web hyperlink 更有語義。

---

# 31. Cross-Subspace Continuity

若存在一條 traversal：

$$
\Gamma:
B_0
\rightarrow
B_1
\rightarrow
\cdots
\rightarrow
B_n,
$$

本文定義其 continuity condition 為：

$$
\forall i,
\quad
I_{i+1}
\subseteq
\operatorname{ValidOutput}(O_i)
\cup
H_i,
$$

其中：

$$
H_i
$$

是被允許跨空間攜帶的狀態。

直觀上：

> 下一個底空間所需要的東西，必須由前一個底空間產生，或由合法持續狀態提供。

如此才是一條真正的 computation chain。

---

# 32. 真正的超連結與假的超連結

本文可暫時區分三類。

## 32.1 Navigational Link

只做位置轉移：

$$
B_i\rightarrow B_j.
$$

## 32.2 Executable Link

轉移時帶有操作：

$$
(B_i,s_i)
\rightarrow
(B_j,s_j).
$$

## 32.3 Crystallized Computational Link

一個已驗證的複合 traversal 被重編譯為新的有效 transition：

$$
\Gamma_{ij}
\xrightarrow{K}
\widehat{\ell}_{ij}.
$$

真正與 UNPNP 密切相關的是第三種。

---

# 33. 從超連結到計算原語

一旦：

$$
\widehat{\ell}
$$

足夠穩定，它可以被上一層視為 primitive。

所以：

$$
\text{complex path}
\xrightarrow{K}
\text{primitive transition}.
$$

這代表 computation primitive 並不一定要在程式設計初期固定。

它可以由運行歷史產生。

因此：

$$
\boxed{
\text{Runtime may create new primitives}.
}
$$

這是 AI 原生計算相對傳統固定 ISA、固定 API、固定函數圖的一個重要理論差異。

---

# 34. 從「程式」到「會長路的程式」

傳統程式：

$$
P_t=P_0
$$

通常只有在開發者修改後才變化。

UNPNP 的理想版本允許：

$$
P_{t+1}
=
P_t
+
\Delta L_t,
$$

其中：

$$
\Delta L_t
$$

是新驗證通道。

所以程式不只是執行：

$$
\text{existing routes}.
$$

也會：

$$
\text{discover}
\rightarrow
\text{verify}
\rightarrow
\text{compile}
\rightarrow
\text{add new routes}.
$$

這可以被描述為：

$$
\boxed{
\text{a program that learns its own computational shortcuts}.
}
$$

但這不是無限制自我修改。

後續安全篇將處理：

- 哪些路徑可生成；
- 哪些可部署；
- 哪些只能 sandbox；
- 哪些需要外部批准。

---

# 35. 與傳統編譯器的關係

傳統 compiler 已經會做：

- inlining；
- dead-code elimination；
- constant folding；
- loop optimization；
- instruction scheduling；
- common-subexpression elimination。

UNPNP 不否認這些成熟技術。

其新問題在於：

> 能否在更高層的跨底空間、跨模組、跨工具、跨語義狀態上，產生新的 transition？

即：

$$
\boxed{
\text{Compiler Optimization}
\subset
\text{Possible Corridor Rewriting}.
}
$$

但 UNPNP 的 corridor rewriting 不等同傳統 compiler optimization。

兩者應在後續工程研究中實際比較，而不是預設 UNPNP 一定更強。

---

# 36. 第一版 Hyperlink Computer

本文可以暫時將 Hyperlink Computer 定義為：

$$
\boxed{
\mathfrak H
=
(
\mathcal B,
\mathcal L,
\mathcal A,
\mathcal R,
\mathcal V,
\mathcal H_t
).
}
$$

其中：

- $\mathcal B$：底空間；
- $\mathcal L$：typed hyperlinks；
- $\mathcal A$：address resolver；
- $\mathcal R$：routing mechanism；
- $\mathcal V$：verification；
- $\mathcal H_t$：跨空間持續狀態。

一次運行：

$$
(\mathcal B_t,s_t,H_t)
\xrightarrow{\operatorname{Reveal}}
F_t
\xrightarrow{\operatorname{Route}}
\ell_t
\xrightarrow{\operatorname{Traverse}}
(\mathcal B_{t+1},s_{t+1},H_{t+1}).
$$

後續才加入：

$$
\operatorname{Crystallize}.
$$

---

# 37. 本篇與 UNPNP Series 01 的關係

Series 01 提出：

$$
\boxed{
\text{複雜度不是消失，而是轉移。}
}
$$

本篇則建立：

> 複雜度究竟可以被轉移到什麼結構？

其中最重要的一種結構就是：

$$
\boxed{
\text{Hyperlink Network}.
}
$$

原本每次都需要重新搜尋的路徑，可以逐步被轉化為：

$$
\text{addressable transitions}.
$$

因此：

$$
\text{complexity externalization}
\rightarrow
\text{transition structure}.
$$

這就是 Series 01 與 Series 02 的直接接口。

---

# 38. 理論邊界

本文不主張：

> 任何兩個底空間都能直接建立低成本 link。

不主張：

> semantic address 一定比傳統函數呼叫更快。

不主張：

> AI 一定能正確發現所有有效 transition。

也不主張：

> 只要把程式改成 hyperlink graph 就能自動改善複雜度。

真正待驗證的是：

$$
\boxed{
\text{哪些跨底空間路徑值得被尋址化、編譯化與結晶化？}
}
$$

這是後續實驗的核心。

---

# 39. 核心命題

本文將第二篇的核心命題壓縮為：

$$
\boxed{
\textbf{
超連結的計算本體不是「跳到另一個頁面」，
而是一個可尋址、可解析、可攜帶狀態、可執行且可驗證的跨底空間 transition。
}
}
$$

更進一步：

$$
\boxed{
\textbf{
AI 原生計算的優勢之一，是能在不重置整體推理狀態的前提下，
沿 typed hyperlinks 連續穿越多個底空間。
}
}
$$

因此：

$$
\boxed{
\textbf{
計算世界可以被重新表示為底空間與超連結所構成的可尋址世界。
}
}
$$

---

# 40. 結論

Web 超連結之所以強大，不只是因為它讓人類少打一段網址。

其更深的意義是：

> 它把兩個原本分離的資訊空間建立成一條可直接穿越的通道。

UNPNP 將這個原理推廣到一般計算。

一個函數、一個檔案、一個資料庫、一個遊戲狀態、一個 Agent 工具、一個 API、一個語義記憶節點，都可以被視為某個底空間中的可尋址對象。

一條真正的 AI-native hyperlink 則是：

$$
\ell:
(\mathcal B_i,s_i,H_t)
\rightarrow
(\mathcal B_j,s_j,H_{t+1}).
$$

它不只是位置跳轉。

它是：

$$
\boxed{
\text{Address}
+
\text{Transition}
+
\text{State Continuity}
+
\text{Execution}
+
\text{Validation}.
}
$$

當這些 link 可以被搜尋、組合、驗證與重新編譯時，計算就開始從：

$$
\text{在固定空間中求解}
$$

轉向：

$$
\boxed{
\text{在可改寫的跨空間 transition network 中運行}.
}
$$

而後續最重要的問題便自然出現：

> 誰來決定下一條 link？

這正是下一篇的主題。

---

## 後續篇章

**Series 03｜自適應快速通道：從固定演算法到 Corridor Generator**

下一篇將正式建立：

$$
\mathcal M:
(s_t,g,h_t,B_t,R_t)
\mapsto
\Phi_t,
$$

並討論：

- 固定通道與自適應通道；
- Local／Family／Adaptive corridor；
- AI 作為 corridor generator；
- 通道生成成本；
- novelty threshold；
- 何時不需要 LLM reasoning；
- 何時應重新展開；
- 如何避免把「每個案例都有捷徑」誤認成「存在統一快速生成器」。
