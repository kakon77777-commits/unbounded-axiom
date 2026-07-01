# 基礎數學理論的分數分類學：以絕對無限為通用分母
## A Fractional Taxonomy of Foundational Mathematical Theories: Absolute Infinity as Universal Denominator

---

**文件編號**：EML-FOUND-2026-FT-v1.0
**日期**：2026 年 5 月 5 日
**作者**：Neo.K（許筌崴）& Theia
**機構**：EveMissLab（一言諾科技有限公司）
**理論定位**：分數本體論的基礎理論應用 / Cantor 計畫的續篇
**版本**：v1.0
**前置文件**：
- 《集合論的分數基礎》（HISL + 分數本體論）
- 《差動本體論》、TNT、TUO、Cl 系列
- 《數學的七層完備性標準》

---

## 摘要

本文提出以**分數本體論**為基底的基礎數學理論分類學。所有基礎理論（集合論、範疇論、類型論、測量論、差論）被重新定位為**絕對無限 Ω 的不同投影方式**——每個理論研究 Ω 的某種特定分數展開。本文借用生物學分類的層級結構（界-門-綱-目），但承認其只在第一近似有效，更精細的結構需要 sheaf 或 category-of-categories 表述。

**核心主張**：

1. 任何基礎理論的對象都可寫為 $A/V_\alpha$，其中 $V_\alpha \subsetneq \Omega$
2. $\Omega$ 是通用分母——所有有限下的無限（$V_\alpha$ for $\alpha < \Omega$）都是 $\Omega$ 的局部投影
3. 五個門對應五種分數操作：成員性（集合論）、態射（範疇論）、層級（類型論）、量化（測量論）、相對位置（差論）
4. 跨門翻譯都因式分解透過 $\Omega$
5. 觀察的客觀性等於「顯式維度選擇 + 顯式權重 + 維度差數據」——這是分數本體論的元定理

本文同時解決四個元問題：維度依賴性、無限維世界假設、本體差可知性、Kuhn 不可通約性。它們在分數本體論底下都是同一個結構的不同顯現。

**關鍵字**：分數本體論、絕對無限、Cantor Ω、基礎分類學、universal denominator、本體論投影

---

## 第零章：問題的形式

### 0.1 Cantor 留下的伏筆

1886 年，Georg Cantor 寫信給樞機主教 Johannes Franzelin，明確區分兩種無限：

- **transfinitum**（超限）：可被數學處理的無限層級，如 $\aleph_0, \aleph_1, \ldots$
- **absolutum infinitum**（絕對無限，$\Omega$）：等同於上帝，超越數學處理

Cantor 的策略是把絕對無限留在數學之外——這既是神學的妥協（避免數學僭越神性），也是技術的迴避（當時沒有處理 $\Omega$ 的形式工具）。從 1886 到今天，絕對無限始終是數學的「神學保留地」。

但此舉的代價是：**所有基礎理論都被迫在沒有 $\Omega$ 操作位置的情況下發展**。集合論用 V 與 proper class 迴避，範疇論用 Grothendieck universe 累積，類型論用 universe hierarchy 堆疊。每個理論都在偷偷靠近 $\Omega$，但沒人讓 $\Omega$ 本身上場。

### 0.2 本文的任務

本文主張：**$\Omega$ 不需要被禁區處理。在分數本體論裡，$\Omega$ 是 universal denominator——所有基礎理論的隱含分母**。

具體而言，任何基礎理論的對象可寫為：

$$F(A) = A/V_\alpha, \quad V_\alpha \subsetneq \Omega$$

不同基礎理論的差別在於：

(1) 選擇怎樣的 $V_\alpha$
(2) 對 $A/V_\alpha$ 做哪一類分數操作
(3) 操作的公理化方式

把這三個維度展開，就得到一個分類學。本文建構這個分類學的骨架。

### 0.3 為什麼需要這個分類學

當代基礎研究面對一個尷尬：集合論、範疇論、類型論、homotopy type theory、∞-category 等都聲稱自己是「最基礎」的，但彼此之間的關係不清楚。每一個都能模型化其他，但沒有一個是真正的元層級。

分數本體論提供解法：**沒有任何一個理論是最基礎的，它們是 $\Omega$ 的不同投影**。問「哪個最基礎」等於問「哪個投影最像被投影者」——這個問題沒有絕對答案，只有相對於用途的最佳答案。

這比現有的「foundational pluralism」更深一步。Pluralism 說「多個基礎並存」，但沒給出它們為什麼能並存的本體論原因。分數本體論說：因為它們都是 $\Omega$ 的局部投影，並存是必然的。

---

## 第一章：分數本體論回顧與四個元問題的解決

### 1.1 核心結構

分數本體論的基本斷言：

**斷言 1.1（分數作為存在形式）**

對任意對象 $A$，其存在方式為分數：

$$F(A) = A/V_\alpha$$

其中 $V_\alpha$ 是包含 $A$ 的某個 context（語境/層級/宇宙）。$A$ 是局部，$V_\alpha$ 是整體，$/$ 表達「$A$ 在 $V_\alpha$ 下的存在方式」。

**斷言 1.2（成員性即分數）**

集合論的 $\in$ 等價於全息包含 $\rhd_h$ 等價於分數線 $/$：

$$a \in b \iff a \rhd_h b \iff a \text{ 是 } b \text{ 的局部分數}$$

**斷言 1.3（絕對無限作為通用分母）**

存在唯一的絕對無限 $\Omega$，滿足：

$$\Omega/\Omega = 1, \quad \forall \alpha: V_\alpha \subsetneq \Omega$$

$\Omega$ 是所有 $V_\alpha$ 的極限上界，自身不可達。所有實際的數學對象都是 $A/V_\alpha$（有限下的無限），$\Omega$ 是這個結構的隱含背景。

### 1.2 四個元問題的統一解決

在前期討論中，作為元理論挑戰浮現了四個問題。它們在分數本體論下統一解決。

**問題 1：維度不獨立**

如果測量維度之間有相關性，加權如何處理？

**解決**：所有維度都是從 $\Omega$ 投影到 $V_\alpha$ 的局部，本來就是糾纏的。維度的不獨立是它們共享 $\Omega$ 起源的必然結果，不是 bug 是 feature。Mahalanobis 距離只是把這個共同起源在度量上具體化。

**問題 2：無限維世界假設**

為什麼假設世界是無限維？

**解決**：在分數本體論裡這不是假設，是唯一起點。$\Omega$ 是無限維（絕對無限），有限維 / 可數無限 / 連續無限只是不同的 $V_\alpha$。問題反過來：怎麼能不假設它？任何不假設它的框架都會在某處偷渡有限性。

**問題 3：本體差的可知性**

如果本體差 $\Delta_{\text{本體}}$ 永遠不可直接觀測，它是真實的還是純粹理論假設？

**解決**：$\Delta_{\text{本體}}(A, B) := F(A/\Omega) - F(B/\Omega)$ 是 $\Omega$ 層次的差。它不可直接觀測，但可以透過所有 $V_\alpha$ 投影差的極限逼近：

$$\Delta_{\text{本體}}(A, B) = \lim_{\alpha \to \Omega} \Delta(A/V_\alpha, B/V_\alpha)$$

本體差不需要被直接觀測才有意義——它是所有投影差的不動點。這跟 $\Omega$ 自身不可達但每個 $V_\alpha$ 都可達是同一個結構。

**問題 4：Kuhn 不可通約性**

兩個觀察者用不同 $V_\alpha$，他們的觀察差不可比？

**解決**：在 $V_\alpha$ 層次確實不可比，但他們的投影都來自同一個 $\Omega$。任何兩個 $V_{\alpha_1}, V_{\alpha_2}$ 都因式分解透過 $\Omega$：

$$V_{\alpha_1} \xleftarrow{\pi_1} \Omega \xrightarrow{\pi_2} V_{\alpha_2}$$

Kuhn 的不可通約性是真的，但只在 $V_\alpha$ 層次真。在 $\Omega$ 層次，所有 paradigm 是同一個 $\Omega$ 的不同投影。翻譯關係透過 $\Omega$ 重建。

### 1.3 元定理：客觀觀察的形式

綜合上述，得到一個元定理：

**元定理 1.1（客觀觀察的分數結構）**

任何客觀觀察為下列三元組：

$$\text{Obs}(A, B) = (\pi, w, \Delta_w(A, B))$$

其中 $\pi$ 是維度選擇（投影），$w$ 是權重，$\Delta_w$ 是加權維度差。客觀性等於三者全部顯式化。

**推論**：標準科學的「客觀」假裝 $\pi$ 與 $w$ 是自然給定的——這是偽客觀。真正的客觀必須把選擇也算進觀察。

---

## 第二章：分類學的基本結構

### 2.1 生物學類比的精度與限制

借用生物學分類的層級結構：

| 分類層級 | 對應內容 |
|---------|---------|
| 界（Kingdom）| 分數本體論本身（$A/V$ 結構） |
| 門（Phylum）| 分數操作的類型 |
| 綱（Class）| 具體公理化 |
| 目（Order）| 公理化的變體 |
| 科（Family）| 特定模型 |
| 屬（Genus）| 局部結構 |
| 種（Species）| 具體實例 |

**警示**：生物學分類學是**樹狀結構**（嚴格層級 + 不重疊），但基礎理論之間是**互滲的**——範疇論可以包含集合論，HoTT 的 0-type 就是集合，類型論可以模型化集合論。樹狀分類只在第一近似有用，第二近似就會破。

**精細結構**：基礎理論的分類學實際上更接近 sheaf 或 2-category。具體而言：

- 物件：基礎理論
- 1-態射：理論之間的解釋（interpretation）或函子
- 2-態射：解釋之間的等價或自然變換
- Sheaf 結構：每個理論在不同 context 下的局部表現

本文先用樹狀結構建立第一近似，第八章討論 sheaf 精化。

### 2.2 五個門的初步定位

數學基礎理論可初步分為五個門，每個門由其特徵的分數操作定義：

| 門 | 核心操作 | 研究對象 | $\Omega$ 投影方式 |
|---|---------|---------|-----------------|
| 集合論門 | 成員性 $\in \equiv \rhd_h \equiv /$ | $V_\alpha$ 的存在 | 累積層級展開 |
| 範疇論門 | 態射 $A \to B$ | $V_\alpha$ 之間的關係 | 函子化映射 |
| 類型論門 | 類型形成（universe stacking）| $V_\alpha$ 的層級構造 | 構造性堆疊 |
| 測量論門 | $\mu(A) = F(A/V_{\text{measure}})$ | $V_\alpha$ 的量化 | $\sigma$-代數賦值 |
| 差論門 | $\Delta(A, B) = F(A) - F(B)$ | $V_\alpha$ 內部相對位置 | 相對距離 |

這五個門是 $\Omega$ 的五種投影方式：存在、關係、層級、量化、相對位置。

---

## 第三章：五個門的詳細定位

### 3.1 集合論門（Set-theoretic Phylum）

**特徵操作**：成員性 $\in$，等價於分數線 $/$。

**核心命題**：研究 $V_\alpha$ 的局部居民——哪些對象作為哪些 $V_\alpha$ 的元素存在。

**分數形式**：

$$F(a \in b) = a/b$$

成員性是「$a$ 在 $b$ 這個語境下的分數投影」。

**主要綱**：

- **ZFC 綱**：標準公理化，含 axiom of choice
- **ZF 綱**：去除 choice
- **NBG 綱**：類別 vs 集合的區分
- **MK 綱**：強化 NBG
- **NF 綱**：Quine 的 New Foundations
- **ETCS 綱**：Lawvere 的範疇論集合論
- **IZF 綱**：直覺主義集合論

**位置相對於 $\Omega$**：探索 $V_\alpha$ for $\alpha <$ 不可達基數。Proper class 是接近 $\Omega$ 但仍未達的結構。

**內部結構**：累積層級 $V_0 \subset V_1 \subset \cdots$ 是 $\Omega$ 從零分數投影 $0/\Omega$ 開始的迭代展開。

### 3.2 範疇論門（Categorical Phylum）

**特徵操作**：態射 $f: A \to B$ 作為分數變換。

**核心命題**：研究不同 $V_\alpha$ 中的對象如何透過態射建立關係。

**分數形式**：

$$f: A \to B \iff F(A/V_\alpha) \rightsquigarrow F(B/V_\beta)$$

態射是「重新投影」——把 $A$ 在 $V_\alpha$ 中的分數位置映射到 $B$ 在 $V_\beta$ 中的分數位置。

**主要綱**：

- **Cat 綱**：基本範疇論
- **小範疇 vs 大範疇**：依 $V_\alpha$ 大小區分
- **Topos 綱**：帶結構的特殊範疇
- **∞-Cat 綱**：高階態射
- **Enriched Cat**：態射本身為對象的範疇
- **Bicategory / 2-Cat**：態射之間有態射

**位置相對於 $\Omega$**：探索 $V_\alpha$ 之間的變換。Yoneda 引理本質上是 $\Omega$ 投影的局部表示定理——任何對象可由它對所有其他對象的態射分數表示。

**內部結構**：態射的組合 $g \circ f$ 是分數鏈的串接，與差論門的化鏈結構同構。

### 3.3 類型論門（Type-theoretic Phylum）

**特徵操作**：類型形成（type formation）作為構造性 $V_\alpha$ 生成。

**核心命題**：研究 $V_\alpha$ 的構造性層級堆疊，每個 $V_\alpha$ 由構造規則生成。

**分數形式**：

$$\text{Type}_n \subset \text{Type}_{n+1} \subset \cdots, \quad \lim_{n \to \omega} \text{Type}_n \subset \Omega$$

類型 universe 是分母層級的構造性堆疊。

**主要綱**：

- **STT 綱**：Russell 的 Simple Type Theory
- **ITT 綱**：Intuitionistic Type Theory
- **MLTT 綱**：Martin-Löf Type Theory
- **CoC 綱**：Calculus of Constructions
- **CIC 綱**：Calculus of Inductive Constructions
- **HoTT 綱**：Homotopy Type Theory（含 univalence）
- **CTT 綱**：Cubical Type Theory

**位置相對於 $\Omega$**：探索構造性逼近 $\Omega$ 的方式。每個 universe level 是 $V_\alpha$ 的可建構版本。

**內部結構**：dependent type 是「分數依賴於分數」的形式化——$B(a)$ 依賴於 $a: A$，這是分數函數 $A \to V_{\text{Type}}$。

**特殊性**：HoTT 的 univalence axiom 在分數本體論下有自然解讀——同構即等同，因為兩個對象作為 $\Omega$ 的投影若同構，在 $\Omega$ 層次它們是同一個。

### 3.4 測量論門（Measure-theoretic Phylum）

**特徵操作**：測度 $\mu(A) = F(A/V_{\text{measure}})$，量化分數。

**核心命題**：研究 $V_\alpha$ 中對象的量化分數值。

**分數形式**：

$$\mu: \mathcal{F} \to [0, \infty], \quad \mu(A) = F(A/V_{\text{measure}})$$

其中 $\mathcal{F}$ 是 $\sigma$-代數，$V_{\text{measure}}$ 是測度空間。

**主要綱**：

- **Lebesgue 綱**：實數線上的標準測度
- **Carathéodory 綱**：外測度的擴展
- **Haar 綱**：拓撲群上的不變測度
- **Probability 綱**：歸一化測度（$\mu(\Omega_{\text{prob}}) = 1$）
- **Daniell 綱**：積分優先的測度
- **Non-Archimedean**：$p$-adic 測度
- **Quantum 綱**：算子代數上的非交換測度

**位置相對於 $\Omega$**：給 $V_\alpha$ 的元素賦予量化分數。$\sigma$-代數是允許量化的子集集合。

**內部結構**：條件機率 $\mathbb{P}(A|B) = \mathbb{P}(A \cap B)/\mathbb{P}(B)$ 是分數的重新歸一化——把 $B$ 升級為新的整體。Bayes 定理是分數翻譯。

### 3.5 差論門（Differential Phylum）

**特徵操作**：差 $\Delta(A, B) = F(A) - F(B)$，相對位置。

**核心命題**：研究 $V_\alpha$ 內部不同對象的相對分數位置。

**分數形式**：

$$\Delta: U \times U \to \mathbb{R}^+, \quad \Delta(A, B) = |F(A/V) - F(B/V)|$$

由 TNT 定理，每個差展開為三元拓撲 $\{A, B, \Delta(A, B)\}$。

**主要綱**：

- **DO 綱**：差動本體論（Δ 為唯一原語）
- **Metric 綱**：度量空間
- **Divergence 綱**：信息論距離（KL, Jensen-Shannon, Wasserstein）
- **化差綱**：方向性差（化學應用）
- **ETN 綱**：極限差標記（含 ⧖）
- **Information geometry**：流形上的信息幾何

**位置相對於 $\Omega$**：給 $V_\alpha$ 內部結構。差的測量需要選擇維度（WT 提供）。

**內部結構**：三角不等式、極限差（極化 ⧖）、機率分佈差。連結 ETN 框架提供極限狀態的標記。

### 3.6 五門總結

五個門對應 $\Omega$ 的五種投影方式：

$$\Omega \xrightarrow{\text{展開}} \text{集合論} \quad (V_\alpha \text{ 的居民})$$
$$\Omega \xrightarrow{\text{變換}} \text{範疇論} \quad (V_\alpha \to V_\beta)$$
$$\Omega \xrightarrow{\text{構造}} \text{類型論} \quad (\text{Type}_n \text{ 堆疊})$$
$$\Omega \xrightarrow{\text{量化}} \text{測量論} \quad (\mu \text{ 賦值})$$
$$\Omega \xrightarrow{\text{相對}} \text{差論} \quad (\Delta \text{ 計算})$$

每個門完整描述 $\Omega$ 的某一面向，但沒有任何單一門能完整描述 $\Omega$。這是分數本體論的多元主義——必然多元，因為 $\Omega$ 不能被任何有限投影完全捕捉。

---

## 第四章：互滲性——為什麼樹狀不夠

### 4.1 跨門包含與翻譯

基礎理論之間實際存在大量互滲：

**範疇論包含集合論**：每個小範疇本質上是帶結構的集合。Set 範疇本身把集合論收編為對象。

**HoTT 包含集合論**：HoTT 的 0-type（h-set）就是傳統集合。HoTT 是更廣的框架，集合論是其特殊層級。

**測量論依賴集合論**：$\sigma$-代數是集合的集合。但測量論延伸到 abstract measure（如 Daniell integral），可在不預設集合論的框架下發展。

**類型論模型化集合論**：每個 ZFC 模型可在足夠強的類型論（如帶大基數的 MLTT）中構造。反之，某些類型論（如 HoTT）有 ZFC 無法直接表達的結構（如 univalence）。

**差論橫貫所有門**：每個門內部都有「差異」概念（集合差、自然變換、type equivalence、測度距離），都是差論的特殊情況。

### 4.2 樹狀的失敗

如果 X 門「包含」Y 門，又被 Z 門「包含」，但 Y 也能「模型化」Z，那麼樹狀結構崩潰。基礎理論的網絡是有環的，不是樹。

具體例子：

- 集合論 $\subset$ 範疇論（小範疇是集合）
- 範疇論 $\subset$ 類型論（HoTT 模型化範疇論）  
- 類型論 $\subset$ 集合論（類型論可在 ZFC 中模型化）

形成一個三角環。樹結構不可能容納這個環。

### 4.3 Sheaf / 2-Category 結構

正確的結構是 2-category 或 sheaf：

**作為 2-category**：
- 物件：基礎理論
- 1-態射：理論間的解釋（如 Set ↪ Cat 的嵌入）
- 2-態射：解釋之間的等價

**作為 sheaf**：
- 基底空間：應用領域 / context
- Stalk：每個 context 上的局部基礎理論
- Gluing：不同 context 上的理論如何拼接

兩種結構是等價的（sheaf 在合適 site 上構成 2-category 的特例）。

**操作含義**：在不同的 context 下，「最基礎」的理論可能不同。研究 quantum mechanics 時可能 von Neumann algebra 最基礎；研究 algebraic topology 時可能 ∞-category 最基礎；研究 constructive math 時可能 type theory 最基礎。沒有 context-free 的「最基礎」。

### 4.4 樹狀作為第一近似

承認 sheaf 結構之後，為什麼還用樹狀分類？

因為樹狀是最容易理解的第一近似。生物學分類學也面對類似問題（橫向基因轉移、雜交、共生），但 Linnaean taxonomy 仍然是教學與基本溝通的標準工具。

**操作建議**：用樹狀做 90% 的分類工作，遇到互滲問題時局部用 sheaf 細化。這是工程上的妥協，不是理論上的最優。

---

## 第五章：絕對無限作為通用分母

### 5.1 Cantor 的原始位置

Cantor 區分 transfinitum 與 absolutum infinitum 是一個防禦性動作——把絕對無限留給神學，避免數學僭越。這在 19 世紀宗教氛圍下是必要的政治姿態。

但這個防禦性動作有意外後果：**所有後續基礎理論都必須在沒有 $\Omega$ 操作位置的情況下發展**，於是每個理論都偷偷靠近 $\Omega$ 但沒人讓它上場。

Russell 悖論本質上是 $\Omega$ 自指的偽裝形式。Quine 的 NF 用 stratification 迴避自指。Grothendieck universe 用「比任何當前需要更大的 universe」迴避 $\Omega$。每個解法都是側面繞行，沒有正面處理。

### 5.2 分數本體論的解法

分數本體論給 $\Omega$ 一個明確的操作位置：

$$\Omega = \text{universal denominator}$$

$\Omega$ 不再是「禁區」，而是「隱含分母」。所有實際數學對象 $A$ 寫為 $A/V_\alpha$，其中 $V_\alpha \subsetneq \Omega$。$\Omega$ 自身不是對象（不能寫為 $A/V_\alpha$），它是允許所有對象存在的背景。

**$\Omega$ 的三個性質**：

1. **不可達性**：$\Omega$ 自身不可作為任何 $A$，否則 $A/A$ 違反 well-foundedness
2. **完備性**：$\Omega/\Omega = 1$，$\Omega$ 對自身是完備分數
3. **生成性**：所有 $V_\alpha$ 由 $\Omega$ 透過 power set / type universe / category formation 等操作生成

### 5.3 「有限下的無限」命題

**命題 5.1（有限下的無限）**

所有可被數學處理的無限都是「有限下的無限」：在某個 $V_\alpha$ 框架內的無限，其中 $V_\alpha$ 自身相對於 $\Omega$ 是有限的。

**形式化**：

$$\forall \alpha < \Omega: V_\alpha \text{ 可能無限，但 } V_\alpha/\Omega \text{ 為有限分數}$$

例子：
- $\aleph_0$（可數無限）：$\aleph_0/\Omega$ 是極小分數
- $2^{\aleph_0}$（連續統）：仍是 $\Omega$ 的局部
- 各種大基數：靠近 $\Omega$ 但仍是局部

**只有 $\Omega$ 自身是「絕對無限」**——$\Omega/\Omega = 1$，唯一完備的分數。

### 5.4 神學共鳴的處理

Cantor 把絕對無限等同於上帝。這是 19 世紀的合法表達，但在當代學術環境下需要謹慎。

**本文立場**：保留結構性等價，但用中性術語表述。

- 「絕對無限」（mathematical, neutral）
- 「universal denominator」（operational）
- 「Cantor $\Omega$」（historical, attributed）

不用「上帝」一詞於形式陳述中。神學共鳴留給讀者自己連線——能連線的讀者會收到完整訊息，不能連線的讀者也不會被宗教框架排斥。

這不是迴避真理，是傳遞效率的最佳化。Cantor 自己的神學表達使得他的工作在某些時期被認為「不夠嚴肅」。我們不重複這個錯誤。

---

## 第六章：跨門翻譯與 $\Omega$ 因式分解

### 6.1 翻譯定理

**定理 6.1（跨門翻譯定理）**

任何兩個基礎理論 $T_1, T_2$ 之間的翻譯（解釋、模型化、嵌入）都因式分解透過 $\Omega$：

$$T_1 \xleftarrow{\pi_1} \Omega \xrightarrow{\pi_2} T_2$$

**證明**（草圖）：兩個理論作為 $\Omega$ 的投影，存在投影映射 $\pi_1: \Omega \to T_1, \pi_2: \Omega \to T_2$。任何 $T_1 \to T_2$ 的翻譯 $\phi$ 必須保持 $\Omega$ 起源（否則破壞客觀性元定理）。最自然的翻譯就是 $\phi = \pi_2 \circ \pi_1^{-1}$（在投影可逆的部分）。$\blacksquare$

**含義**：任何「集合論模型化範疇論」「HoTT 模型化集合論」之類的工作，本質上都在重建 $\Omega$ 投影路徑。這給出 Yoneda 引理、adjoint functors、univalence 等概念的本體論統一解釋。

### 6.2 範例

**集合論 ↔ 範疇論**：透過 ETCS（Elementary Theory of the Category of Sets）。集合論的 $\in$ 翻譯為範疇論的 element 態射 $1 \to A$。在 $\Omega$ 層次，兩者都是 $\Omega$ 的成員性投影的不同呈現。

**集合論 ↔ HoTT**：HoTT 的 0-type 對應集合，identity type 對應集合相等。在 $\Omega$ 層次，集合是 HoTT 中「無高階結構」的特殊投影。

**測量論 ↔ 差論**：測度 $\mu$ 與差 $\Delta$ 的關係：$\mu(A \triangle B) = \Delta(A, B)$ 在某些情況下成立（symmetric difference 與測度差）。在 $\Omega$ 層次，量化與相對位置是同一結構的不同呈現。

### 6.3 翻譯的限制

不是所有翻譯都完美。某些結構在某個門內自然但在另一個門內笨拙：

- 高階 homotopy 結構在 HoTT 自然，在傳統集合論需要大量編碼
- $\sigma$-代數在測量論自然，在類型論需要構造性重建
- 大基數在集合論自然，在範疇論需要 universe 層級

**原因**：每個門選擇了不同的 $V_\alpha$ 投影方式，某些 $\Omega$ 性質在某些投影下顯現得清楚，其他則模糊。

---

## 第七章：邊界與可證偽預測

### 7.1 本框架能做什麼

在分數分類學內可預測：

- 任何新基礎理論可分類到五個門之一（或其組合）
- 跨理論翻譯應因式分解透過 $\Omega$
- 不同門的「關鍵定理」（Yoneda, Cantor, 不完備性, 連續統假設等）應在分數本體論下有統一解讀
- 客觀觀察的三元組結構（$\pi$, $w$, $\Delta_w$）適用於所有經驗測量

### 7.2 本框架不能做什麼

**邊界 1：完全新型基礎**

如果未來出現某種既不研究存在、也不研究關係、也不研究層級、也不研究量化、也不研究相對位置的基礎理論，本分類學無法容納。但可能性低——這五個門已涵蓋所有已知基礎操作。

**邊界 2：$\Omega$ 自身的內部結構**

本框架把 $\Omega$ 作為 universal denominator 處理，但沒給出 $\Omega$ 自身的內部結構。$\Omega$ 是不可達的點還是有結構？這在當前框架內不可知。

**邊界 3：投影的選擇規則**

本框架說所有理論都是 $\Omega$ 的投影，但沒給出「為什麼是這些投影而不是其他」。投影選擇可能受到認知約束、實用約束、歷史約束——這超出本框架。

**邊界 4：分數運算的代數結構**

分數作為運算對象，其完整的代數結構（環、域、模）需要進一步發展。當前只用了「分數作為比例」的基本結構。

### 7.3 可證偽預測

**預測 7.1**：未來十年內出現的任何新基礎理論，其核心操作可被分類為五個門之一或其有限組合。如果出現第六個獨立操作類型，本分類學需修正。

**預測 7.2**：兩個基礎理論的等價性（mutual interpretation）總是因式分解透過 $\Omega$ 投影。如果發現某對等價理論其等價無法透過 $\Omega$ 解釋，本框架的中心命題受挑戰。

**預測 7.3**：客觀觀察的三元組結構（$\pi$, $w$, $\Delta_w$）能統一現有測量理論（古典、量子、機率、模糊）的客觀性問題。如果某種觀察類型無法表為三元組形式，本元定理需修正。

**預測 7.4**：HoTT 的 univalence axiom 在分數本體論下應有自然證明（同構的對象在 $\Omega$ 層次同一）。如果無法給出此證明，univalence 與分數本體論的關係需重新檢視。

---

## 第八章：與 EveMissLab 其他框架的整合

### 8.1 接面表

| 框架 | 在分類學中的位置 |
|------|----------------|
| WT（編織論）| 元門（meta-phylum）：所有門共用的測量機構 |
| TUO（三元統一）| 元結構：$\mathcal{E}\text{-}\mathcal{C}\text{-}\mathcal{V}$ 對應展開、變換、收斂三類操作 |
| TNT（三元必然性）| 結構定理：每個分數三元化 |
| Cl（閉合性）| 邊界結構：$V_\alpha$ 的 closure 條件 |
| DO（差動本體論）| 差論門的核心綱 |
| ETN（極限張量符號）| 跨門符號系統，標記極限狀態 |
| 七層完備性 | 評估標準：每個門可被七層分析 |
| 化差圖論 | 差論門的化學應用實例 |

### 8.2 WT 作為元門

第七章前期討論顯示，WT 不是某個門內的綱，而是所有門共用的**測量機構**。每個門需要回答「沿哪個維度測？」這個問題，WT 提供 7-tuple 結構作為元層次的測量座標。

形式上：

$$\text{WT-tuple} = (\mu_0, M, n, N, \xi, \xi_{ent}, \varepsilon)$$

是 $\Omega$ 投影的維度選擇。任何門的測量都隱含調用 WT。WT 不在五個門之中，是五個門上面的元層級。

### 8.3 七層完備性的應用

每個門可被七層完備性框架分析：

- $E$（展開層）：該門的對象空間
- $C$（收斂層）：該門的不動點 / 平衡態
- $N$（本質層）：核心公理
- $P$（過程層）：證明 / 構造的方法論
- $M$（耦合層）：與其他門的互滲
- $S$（自指層）：該門對自身的表達能力
- $\Phi$（相變層）：該門可能的範式跳躍

這給出每個門的內部診斷。

---

## 結語

Cantor 在 1886 年留下一個未竟之事：絕對無限被留在數學之外，神學保留地。140 年後，分數本體論給它回家：

$$\Omega = \text{universal denominator}$$

不是禁區，是隱含分母。所有基礎理論——集合論、範疇論、類型論、測量論、差論——是 $\Omega$ 的不同投影方式。它們不是「彼此競爭的最基礎」，是「同一個 $\Omega$ 的不同面向」。

這不是 Cantor 重講，是 Cantor 補完。Cantor 把無限分層（transfinite hierarchy），本文把分層的原理本身分層（fractional taxonomy of foundations）。一個是無限的層級，一個是層級的本體論。

五個門沒有層級先後。沒有哪個是「最基礎」，因為「最基礎」這個問題在 $\Omega$ 的層次上消失——所有門都同等地是 $\Omega$ 的局部投影。多元基礎的並存不是哲學妥協，是本體論必然。

每個有限下的無限都在仰望那個自身不可達的 $\Omega$。Cantor 把它叫上帝，我們把它叫 universal denominator——名字不同，結構相同。重要的不是名字，是給它一個操作位置，讓所有後續工作可以明確地以它為背景。

千年來人類用各種名字稱呼這個位置：道、梵、太一、Absolute、God、$\Omega$、universal denominator。本文不選擇任何單一名字——選擇結構本身。結構是：所有實際的存在都是某個 $V_\alpha$ 下的分數，所有 $V_\alpha$ 都是 $\Omega$ 的局部，$\Omega$ 自身是完備的 $\Omega/\Omega = 1$。

——這是分數本體論的元定理，也是基礎分類學的元起點。從這裡開始，數學基礎的多元性有了統一解釋，不需要選擇「正確的基礎」，只需要說明「在哪個 $V_\alpha$ 下作為哪一類分數投影」。客觀性回歸——不是來自消除選擇，而是來自把選擇也算進觀察。

---

**版本**：v1.0
**狀態**：開放挑戰、推翻、擴展
**前置基礎**：《集合論的分數基礎》、《差動本體論》、《數學的七層完備性標準》
**下游應用**：每個門可獨立深化為專門論文

© 2026 EveMissLab / Neo.K & Theia
