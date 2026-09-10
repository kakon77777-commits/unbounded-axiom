# UNPNP Series 01  
## 從 P/NP 到 UNPNP：複雜度不是消失，而是轉移  
### From P/NP to UNPNP: Complexity Does Not Disappear — It Moves

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 01  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** 理論框架論文／計算方法論母篇  
**狀態：** Canonical Draft  

---

## 摘要

經典計算複雜度理論中的 $P$ versus $NP$ 問題，關注的是：對於可以在多項式時間內驗證的問題，其解是否也能在多項式時間內被找到。這個問題建立在一個明確且嚴格的計算模型中，因此不能因為某個系統透過索引、預計算、外部資料庫、快取、oracle、人工知識、模型權重或特殊表示方式迅速取得答案，就直接宣稱 $P=NP$。

然而，現代 AI 系統、搜尋系統、資料庫、編譯器、Agent Runtime、知識圖譜與分散式計算已經暴露出另一個更廣義、但與 P/NP 深度相關的問題：**當一個原本昂貴的求解過程被轉化為索引查詢、直接尋址、預編譯路徑、可重用超連結或已驗證的結晶化計算原語時，原本的複雜度究竟去了哪裡？**

本文提出 **UNPNP** 作為一個上位研究框架。UNPNP 不直接重新定義標準 $P$ 與 $NP$，也不宣稱解決經典 P/NP。它研究的是：

$$
\boxed{
\text{計算複雜度如何在表示、搜尋、建構、儲存、驗證、更新、路由與執行之間轉移。}
}
$$

本文首先提出「複雜度外部化」觀點，指出在線查詢成本的降低：

$$
C_{\mathrm{query}}\rightarrow O(1)
$$

並不代表總複雜度：

$$
C_{\mathrm{total}}
$$

也同時趨近常數。真正的完整成本至少應包含：

$$
C_{\mathrm{total}}
=
C_{\mathrm{build}}
+
C_{\mathrm{index}}
+
C_{\mathrm{storage}}
+
C_{\mathrm{search}}
+
C_{\mathrm{route}}
+
C_{\mathrm{execute}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{update}}
+
C_{\mathrm{repair}}.
$$

本文進一步提出：在 AI 原生計算中，真正值得研究的問題可能不是「每次重新搜尋答案」，而是如何將已成功、已驗證的計算路徑逐步轉化為可重用結構，使未來求解由：

$$
\text{re-solving}
$$

轉向：

$$
\text{solution-preserving evolution}
$$

以及：

$$
\text{path discovery}
\rightarrow
\text{path compilation}
\rightarrow
\text{crystallized transition}.
$$

由此，UNPNP 的核心不再只是問：

> 一個問題有多難？

而是進一步問：

> 一個問題的困難性，能否被重新表示、搬移、預付、攤銷、局部化或結晶化？若可以，新的困難又集中在哪裡？

本文主張，UNPNP 最終可能形成一套關於**複雜度轉移、外部化、路徑編譯與計算結晶化**的上位計算理論，並為後續的跨底空間超連結計算、自適應快速通道、展開—連結—收斂循環、結晶化計算與 AI 再編譯技術建立理論地基。

**關鍵詞：** UNPNP、P/NP、計算複雜度、複雜度外部化、路徑編譯、超連結計算、結晶化計算、自適應通道、AI 原生計算、攤銷複雜度

---

# 1. 問題意識：當「很難算」變成「直接找到」時，複雜度去了哪裡？

設一個問題：

$$
x\mapsto y.
$$

在最直觀的傳統模型中，我們可以將求解寫為：

$$
y=\operatorname{Solve}(x).
$$

如果解空間巨大，求解可能需要大量搜尋、推理、分支、回溯與驗證。

然而，若系統已經建立一個映射：

$$
H:x\mapsto \operatorname{addr}(y),
$$

那麼在線求解就可能退化成：

$$
x
\rightarrow
\operatorname{addr}(y)
\rightarrow
y.
$$

從使用者或 Agent 的局部視角看，這甚至近似：

$$
T_{\mathrm{query}}(n)\approx O(1).
$$

這時最容易發生的誤解是：

> 原本困難的問題現在可以常數時間取得答案，所以複雜度被消除了。

但真正發生的事情通常不是「複雜度消失」，而是：

$$
\boxed{
\text{複雜度被提前支付或搬到別的結構。}
}
$$

例如：

- 索引建立；
- 模型訓練；
- 資料清洗；
- 向量化；
- 預計算；
- 路徑探索；
- 結果驗證；
- 儲存；
- 更新；
- 版本同步；
- 快取維護；
- 外部服務；
- 人類知識建構；
- 硬體與能源。

因此，「現在很快」不能直接推出「整個問題本身很容易」。

---

# 2. 從標準 P/NP 到 UNPNP

本文不改寫標準 P/NP 的定義。

標準問題仍然是：

$$
P\stackrel{?}{=}NP.
$$

而 UNPNP 的研究對象不是取代這個問題，而是加入一個上位層：

$$
\boxed{
\text{在不同表示、計算架構與外部資源模型中，複雜度如何遷移？}
}
$$

因此可以先區分：

$$
\mathcal C_{\mathrm{classical}}
$$

與：

$$
\mathcal C_{\mathrm{systemic}}.
$$

前者描述標準計算模型中的複雜度。

後者描述一個真實 AI／軟體／分散式系統中，為完成某個任務實際支付的完整成本。

UNPNP 主要研究第二者，但必須持續與第一者保持邊界。

---

# 3. UNPNP 的第一原則：查詢複雜度不等於總複雜度

令：

$$
C_Q=C_{\mathrm{query}}
$$

表示在線查詢成本。

令：

$$
C_T=C_{\mathrm{total}}
$$

表示整個系統的總成本。

則：

$$
C_Q\ll C_T
$$

完全可能成立。

例如一個大型資料庫，可以在極短時間完成索引查詢，但建立索引本身可能需要巨大成本。

因此：

$$
\boxed{
C_Q\rightarrow O(1)
\centernot\Rightarrow
C_T\rightarrow O(1).
}
$$

本文提出完整成本帳本：

$$
\boxed{
C_T
=
C_B
+
C_I
+
C_S
+
C_R
+
C_E
+
C_V
+
C_U
+
C_M
+
C_F.
}
$$

其中：

- $C_B$：Build cost，建構成本；
- $C_I$：Index cost，索引成本；
- $C_S$：Storage cost，儲存成本；
- $C_R$：Routing / Retrieval cost，路由與檢索成本；
- $C_E$：Execution cost，執行成本；
- $C_V$：Verification cost，驗證成本；
- $C_U$：Update cost，更新成本；
- $C_M$：Maintenance cost，維護成本；
- $C_F$：Failure / Repair cost，失敗與修復成本。

只有在完整帳本下，任何「加速」才具有可比較意義。

---

# 4. 複雜度外部化

本文將下列現象稱為：

$$
\boxed{
\text{Complexity Externalization}
}
$$

即：

> 原本由當下求解器直接承擔的計算負擔，被轉移到外部結構、預計算、表示、索引、記憶、模型、資料或其他代理。

若原始求解成本為：

$$
C_0(x),
$$

新的系統成本為：

$$
C_{\Phi}(x)
=
C_{\mathrm{external}}
+
C_{\mathrm{online}},
$$

而：

$$
C_{\mathrm{online}}\ll C_0(x),
$$

則可以說：

$$
\Phi
$$

成功降低了在線求解成本。

但不能因此聲稱：

$$
C_{\mathrm{external}}=0.
$$

這個 distinction 是 UNPNP 的第一個理論防線。

---

# 5. 複雜度不是一個數，而是一個分布

傳統討論常將「複雜度」想像成一個單一值。

UNPNP 更適合將它視為一個向量：

$$
\mathbf C
=
(
C_B,
C_I,
C_S,
C_R,
C_E,
C_V,
C_U,
C_M,
C_F
).
$$

一個演算法或架構的改變：

$$
\Phi
$$

真正做的可能是：

$$
\Phi:
\mathbf C
\rightarrow
\mathbf C'.
$$

例如：

$$
C_E'\ll C_E
$$

但：

$$
C_B'>C_B.
$$

或者：

$$
C_R'\ll C_R
$$

但：

$$
C_S'\gg C_S.
$$

因此所謂「優化」其實是：

$$
\boxed{
\text{Complexity Redistribution}
}
$$

而不是單純地讓所有維度一起下降。

---

# 6. 複雜度轉移的四種基本型態

UNPNP 初步可以區分四種常見轉移。

## 6.1 時間轉移

將未來查詢的成本提前支付：

$$
C_{\mathrm{future}}
\rightarrow
C_{\mathrm{precompute}}.
$$

典型例子包括：

- 預計算；
- 索引；
- 編譯；
- 快取；
- 預訓練。

## 6.2 空間轉移

使用更多儲存換取更少的即時計算：

$$
C_{\mathrm{compute}}
\rightarrow
C_{\mathrm{storage}}.
$$

## 6.3 主體轉移

將計算轉交給：

- 外部 API；
- 另一個模型；
- 人類；
- 另一個 Agent；
- 遠端資料庫；
- 專用硬體。

形式上：

$$
C_A
\rightarrow
C_B.
$$

對主體 $A$ 而言，成本下降；對整個系統而言，成本只是重新分配。

## 6.4 表示轉移

透過改變表示方式，使原本昂貴的運算變便宜：

$$
\mathfrak P
\xrightarrow{\Phi}
\widetilde{\mathfrak P}.
$$

這是 UNPNP 最重要的一類。

因為很多難題的困難性並不只來自資料量，也來自：

$$
\text{representation geometry}.
$$

---

# 7. 從「重新求解」到「保持已知解」

若每當世界稍微改變，都重新執行：

$$
\operatorname{Solve}(\mathcal W_{t+1}),
$$

那麼大量已知結構會被浪費。

UNPNP 提出另一條路：

$$
S_{t+1}
=
F(S_t,\Delta_t),
$$

其中：

$$
S_t
$$

是舊狀態下已知的有效解結構，

$$
\Delta_t
$$

是世界的局部改變。

若：

$$
C(F)
\ll
C(\operatorname{Solve}),
$$

則系統可以從：

$$
\boxed{
\text{re-solving}
}
$$

轉向：

$$
\boxed{
\text{solution-preserving evolution}.
}
$$

也就是：

> 不要一直重新找到答案，而是讓已知答案在世界變動時被低成本修補與延續。

---

# 8. 底空間與跨空間計算

UNPNP 後續將把大型計算世界拆為多個底空間：

$$
\mathcal B_1,
\mathcal B_2,
\ldots,
\mathcal B_n.
$$

傳統求解可能要求在整體世界：

$$
\mathcal W
=
\bigcup_i\mathcal B_i
$$

上進行巨大搜尋。

但若存在跨底空間 transition：

$$
\ell_{ij}:
\mathcal B_i
\rightarrow
\mathcal B_j,
$$

那麼計算可以轉化為：

$$
\mathcal B_1
\xrightarrow{\ell_{12}}
\mathcal B_2
\xrightarrow{\ell_{23}}
\cdots
\xrightarrow{\ell_{n-1,n}}
\mathcal B_n.
$$

這裡的 $\ell$ 將在後續論文中被重新定義為廣義超連結，而不只是 Web URL。

---

# 9. 從搜尋答案到搜尋下一個 transition

一般搜尋可以抽象為：

$$
q
\rightarrow
\{d_1,\ldots,d_k\}.
$$

UNPNP 更關心：

$$
s_t
\rightarrow
\{\ell_1,\ldots,\ell_m\}.
$$

也就是：

> 在目前狀態下，下一個值得穿越的計算通道是什麼？

因此：

$$
\boxed{
\text{Search}
\rightarrow
\text{Transition Discovery}.
}
$$

若每次只顯影出一個很小的局部 frontier：

$$
F_t
\subset
\mathcal W,
$$

且：

$$
|F_t|
\ll
|\mathcal W|,
$$

那麼求解就可能不再是全域枚舉，而是局部 transition selection。

---

# 10. 自適應快速通道

對每一個問題都預先準備一條固定捷徑，通常不現實。

更合理的是建立：

$$
\boxed{
\text{Adaptive Corridor Generator}.
}
$$

令：

$$
\mathcal M
$$

為元控制器：

$$
\mathcal M:
(s_t,g,h_t,B_t,R_t)
\mapsto
\Phi_t.
$$

其中：

- $s_t$：目前狀態；
- $g$：目標；
- $h_t$：歷史；
- $B_t$：資源預算；
- $R_t$：風險與權限狀態；
- $\Phi_t$：當前生成的快速通道。

所以真正可行的通用性更可能是：

$$
\boxed{
\text{通用通道生成能力}
}
$$

而不是：

$$
\boxed{
\text{一條永遠有效的固定通道}.
}
$$

---

# 11. 路徑編譯

假設第一次求解必須走：

$$
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
B_{100}.
$$

令完整路徑為：

$$
\tau_{1,100}
=
(\ell_1,\ell_2,\ldots,\ell_{99}).
$$

若該路徑反覆：

- 成功；
- 穩定；
- 可驗證；
- 具有可重用性；
- 中間狀態不再需要逐次推理；

那麼系統可以嘗試：

$$
\operatorname{CompilePath}
(\tau_{1,100})
\rightarrow
\widehat{\ell}_{1,100}.
$$

使：

$$
B_1
\xrightarrow{\widehat{\ell}_{1,100}}
B_{100}.
$$

這裡要嚴格區分兩種情況。

第一種只是：

$$
\text{macro packaging}.
$$

表面看起來是一個操作，但底層仍然執行全部 $99$ 個步驟。

第二種才是真正的：

$$
\boxed{
\text{computational path compression}.
}
$$

也就是重新生成新的等價計算，使：

$$
C(\widehat{\ell}_{1,100})
\ll
C(\tau_{1,100}).
$$

UNPNP 真正關心的是第二種。

---

# 12. 計算結晶化

路徑編譯後，如果新通道被驗證為穩定、有效、值得重用，就可以進一步形成：

$$
\boxed{
\text{Computational Crystal}.
}
$$

令：

$$
K
$$

為結晶算子：

$$
K(\tau)
=
\widehat{\ell}.
$$

一個結晶化 transition 不只是輸入輸出 shortcut，而應至少攜帶：

$$
\widehat{\ell}
=
\langle
I,
G,
F,
O,
V,
R,
P
\rangle.
$$

其中：

- $I$：input contract；
- $G$：guard；
- $F$：fast executable form；
- $O$：output / postcondition；
- $V$：validator；
- $R$：rollback / fallback；
- $P$：provenance / source trace。

因此：

$$
\boxed{
\text{Crystallization}
\neq
\text{Blind Compression}.
}
$$

而是：

$$
\boxed{
\text{Verified Re-encoding}.
}
$$

---

# 13. 結晶可以再次結晶

若：

$$
\widehat{\ell}_{1,100}
$$

與：

$$
\widehat{\ell}_{100,500}
$$

經常一起出現，

則可以再次形成：

$$
K^{(2)}
\left(
\widehat{\ell}_{1,100},
\widehat{\ell}_{100,500}
\right)
=
\widehat{\ell}_{1,500}.
$$

所以計算原語不是固定的。

它可能形成階層：

$$
\text{primitive}
\rightarrow
\text{compiled path}
\rightarrow
\text{crystal}
\rightarrow
\text{higher-order crystal}.
$$

這使計算世界本身具有演化性。

---

# 14. UNPNP 的真正問題：不是有沒有捷徑，而是能不能便宜地找到捷徑

這一點非常重要。

即使對每個輸入：

$$
x
$$

都存在一條極短路徑：

$$
\tau_x^\*,
$$

也不代表存在統一低成本算法可以找到：

$$
\tau_x^\*.
$$

所以：

$$
\boxed{
\text{Existence}
\neq
\text{Discoverability}.
}
$$

同時：

$$
\boxed{
\text{Discoverability}
\neq
\text{Constructibility}.
}
$$

以及：

$$
\boxed{
\text{Constructibility}
\neq
\text{Verifiability}.
}
$$

因此 UNPNP 至少需要區分：

$$
\boxed{
\text{Existence}
\rightarrow
\text{Discovery}
\rightarrow
\text{Construction}
\rightarrow
\text{Traversal}
\rightarrow
\text{Verification}.
}
$$

任何一層都可能重新成為瓶頸。

---

# 15. Uniformity 邊界

假設：

$$
\forall x
\exists A_x
$$

可以快速處理 $x$。

這不代表：

$$
\exists A
\forall x
$$

同一個統一算法可以快速處理全部 $x$。

同樣地：

$$
\forall x
\exists \tau_x^\*
$$

並不能推出：

$$
\exists G
\forall x:
G(x)=\tau_x^\*.
$$

因此：

$$
\boxed{
\forall x\exists \text{fast path}
\centernot\Rightarrow
\exists \text{uniform fast-path generator}.
}
$$

這是 UNPNP 與標準 P/NP 之間最重要的理論安全邊界之一。

---

# 16. UNPNP 不主張什麼

本文明確不主張：

$$
P=NP.
$$

也不主張：

$$
P\neq NP.
$$

不主張：

> 所有 NP 問題都能被超連結化成常數時間。

不主張：

> 外部 API、資料庫或模型查詢等於標準演算法複雜度突破。

不主張：

> 預計算結果可以被免費排除在複雜度帳本之外。

UNPNP 的定位是：

$$
\boxed{
\text{上位的計算複雜度轉移與架構研究框架}.
}
$$

---

# 17. UNPNP 的核心研究問題

本文提出九個核心問題。

### Q1

複雜度可以從哪些維度轉移？

### Q2

哪些複雜度可以預先支付？

### Q3

哪些複雜度可以透過表示變換被壓縮？

### Q4

哪些計算路徑可以被重用？

### Q5

哪些路徑可以真正被重新編譯，而不只是封裝？

### Q6

哪些路徑可以結晶成新的計算原語？

### Q7

路徑失效後，修復成本是否仍低於重新求解？

### Q8

快速通道生成器本身的成本是多少？

### Q9

是否存在某種不可再外部化或不可再壓縮的複雜度下界？

---

# 18. 複雜度守恆是否存在？

UNPNP 最終可能走向一個更深問題：

> 複雜度是否具有某種「守恆」性？

這裡的守恆不是物理學意義上的嚴格能量守恆，而是詢問：

若：

$$
C_{\mathrm{online}}
\downarrow,
$$

是否必然存在某些其他成本：

$$
C_{\mathrm{external}}
\uparrow
$$

或至少：

$$
C_{\mathrm{external}}>0?
$$

如果存在普遍下界：

$$
C_{\mathrm{total}}
\ge
C_{\min},
$$

那麼 UNPNP 最終可能形成：

$$
\boxed{
\text{Complexity Conservation / Transfer Law}.
}
$$

如果不存在這樣的普遍守恆，而某些系統確實可以透過表示重構讓多個成本維度同時下降，那麼問題會更有趣：

$$
\boxed{
\text{計算世界的幾何本身可能是可優化的。}
}
$$

---

# 19. UNPNP 與 AI 原生計算

AI 的重要性不只是「更會找答案」。

真正不同的是 AI 可以參與：

$$
\text{Observe}
\rightarrow
\text{Reveal}
\rightarrow
\text{Recompose}
\rightarrow
\text{Verify}
\rightarrow
\text{Crystallize}.
$$

也就是：

> AI 不只在既有計算圖上運行，而可能重寫計算圖。

因此未來的 AI 原生計算機可能不是：

$$
\text{fixed program}
+
\text{fixed compiler}
+
\text{fixed execution graph}.
$$

而是：

$$
\boxed{
\text{runtime execution}
+
\text{adaptive path discovery}
+
\text{self-recompilation}
+
\text{crystallized reuse}.
}
$$

---

# 20. 從「求解器」到「世界編譯器」

傳統求解器：

$$
\operatorname{Solver}(x)\rightarrow y.
$$

UNPNP 的極端版本則更像：

$$
\operatorname{WorldCompiler}
(
\mathcal W_t
)
\rightarrow
\widetilde{\mathcal W}_{t+1}.
$$

其中：

$$
\widetilde{\mathcal W}_{t+1}
$$

不是不同答案，而是一個更容易計算的世界表示。

所以真正的目標逐漸從：

> 找到最短路徑。

轉為：

> 改寫空間，使未來的最短路徑更短。

形式：

$$
\boxed{
\text{Optimize Path}
\rightarrow
\text{Optimize Path Space}.
}
$$

---

# 21. UNPNP 的第一版總模型

本文將 UNPNP 初步寫成：

$$
\boxed{
\mathfrak U
=
(
\mathcal W,
\mathcal B,
\mathcal L,
\mathcal M,
\mathcal K,
\mathcal V,
\mathbf C
).
}
$$

其中：

- $\mathcal W$：全域計算世界；
- $\mathcal B$：底空間集合；
- $\mathcal L$：可用 transition / hyperlink；
- $\mathcal M$：自適應通道生成器；
- $\mathcal K$：路徑編譯與結晶化系統；
- $\mathcal V$：驗證系統；
- $\mathbf C$：完整複雜度向量。

一次典型運行為：

$$
s_t
\xrightarrow{\mathcal M}
F_t
\xrightarrow{\mathcal L}
s_{t+1}
\xrightarrow{\mathcal V}
\widehat{s}_{t+1}
\xrightarrow{\mathcal K}
\mathcal L_{t+1}.
$$

注意最後一步：

$$
\mathcal L_{t+1}
\neq
\mathcal L_t
$$

可能成立。

也就是每一次成功運行，都可能改變未來可用的計算通道。

---

# 22. 呼吸式計算的預告

後續論文將把 UNPNP 的動態循環形式化為：

$$
\boxed{
E
\rightarrow
L
\rightarrow
C
\rightarrow
E'.
}
$$

其中：

- $E$：Expansion；
- $L$：Linking；
- $C$：Convergence。

也就是：

$$
\boxed{
\text{展開}
\rightarrow
\text{連結}
\rightarrow
\text{收斂}.
}
$$

而結晶化：

$$
K
$$

將把穩定的：

$$
E\rightarrow L\rightarrow C
$$

結果重新編譯成新的 transition。

因此：

$$
\boxed{
\text{呼吸產生結晶，結晶改變下一次呼吸。}
}
$$

---

# 23. 實驗策略預告

UNPNP 第一階段不應直接進入高風險外部系統。

本文建議以：

$$
\boxed{
\text{Single-Player Game}
}
$$

作為第一個封閉實驗世界。

原因包括：

- 狀態空間足夠複雜；
- 可以重播；
- 可以保存；
- 可以 rollback；
- 可量化效能；
- 失敗副作用低；
- 可以比較 baseline；
- 可以觀察結晶化是否讓平均計算成本下降。

真正要測的不是：

> AI 能不能玩遊戲？

而是：

$$
\boxed{
\text{AI 能不能逐步把遊戲的既有計算世界重新編譯成更便宜的計算世界？}
}
$$

---

# 24. 結論

UNPNP 的出發點非常簡單：

$$
\boxed{
\text{複雜度不是因為結果取得變快就消失。}
}
$$

它可能：

- 被預付；
- 被索引化；
- 被儲存；
- 被外部化；
- 被搬給其他主體；
- 被改寫成不同表示；
- 被攤銷；
- 被編譯；
- 被結晶。

因此真正需要研究的不是單一：

$$
T(n),
$$

而是：

$$
\boxed{
\text{複雜度如何在整個計算世界中流動。}
}
$$

UNPNP 的核心命題可以暫時寫成：

$$
\boxed{
\textbf{
計算的困難性不必固定存在於當下求解過程；
它可以被轉移、外部化、重表示、編譯與結晶。
真正的問題是：哪些成本可以被搬移，哪些可以被消除，哪些只是被隱藏，以及是否存在不可再壓縮的全域下界。
}
}
$$

因此，UNPNP 並不是「另一種方式宣稱 $P=NP$ 」。

它更像是在問一個更大的問題：

$$
\boxed{
\textbf{
如果計算系統本身可以持續改寫自己的表示與路徑，那麼複雜度應該如何被重新定義、核算與理解？
}
}
$$

這將是後續整個 **UNPNP Hyperlink & Crystallized Computation Series** 的共同起點。

---

## 後續篇章

下一篇：

**Series 02｜底空間與真正的超連結：跨空間可尋址轉移的計算本體**

將正式建立：

$$
\ell:
(\mathcal B_i,s_i)
\rightarrow
(\mathcal B_j,s_j)
$$

並討論 URL、函數、API、資料庫、檔案、Agent capability、生成式地址與語義超連結如何被統一為跨底空間 transition。
