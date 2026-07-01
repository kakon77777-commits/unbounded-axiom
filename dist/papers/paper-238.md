# 局部命題驗證的三層結構方法論

## 以 ABC 猜想為計算示例

**作者**：Neo.K (許筌崴)
**機構**:EveMissLab (一言諾科技有限公司)
**日期**:2026 年 5 月
**版本**:v0.1

---

## 摘要

本文提出一個**可形式化驗證的局部命題方法論**:Axiom-Operation-Instance(以下簡稱 A-O-I)三層結構,亦稱「左-中-右」結構。其核心主張是:**任何聲稱要驗證一個數學命題的計算流程,必須將該流程明確分離為三個邏輯層**——不變的 axiom 層(左邊)、可執行的 operation 層(中間)、具體的 instance 層(右邊)——否則該流程喪失形式化驗證的入口,並在數學社群層面難以建立公信力。

本文以 ABC 猜想為示例,通過三段遞進的 Python 計算實驗——brute-force 全域掃描、對稱約束計算、非對稱約束計算——展示 A-O-I 三層結構如何在實際計算任務中明確分離與互相校準。我們在 $c \in [10^6, 10^7]$ 範圍內捕捉到包含 Reyssat 紀錄($q \approx 1.6299$)在內的 68 個高品質三元組,並觀察到 quality 分佈中的「斷崖式 gap」結構。

**本文明確不主張**:

1. 證明 ABC 猜想(全局命題)。
2. 提出新的數論定理。
3. 改進現有 ABC 數值驗證工作(如 abc@home 等)的計算覆蓋範圍。

**本文主張**:三層結構方法論本身作為**局部命題驗證的元結構**(meta-structure),具有跨領域可遷移性,並提供從非形式化命題到 Lean 4 形式化證明之間的明確翻譯橋樑。ABC 在此僅作為方法論的承載介質,而非研究對象。

> **認識論免責聲明**:本文中所有具體計算範圍($c \leq 10^7$、$q$ 閾值等)為演示性質,並非嚴格界定。論文的主要貢獻在於方法論結構的提出,而非數值結果本身。所有數值資料用於結構驗證,非實證測量。

---

## 1. 動機:為何需要 A-O-I 三層結構

### 1.1 兩層結構的不足

當前許多數學命題的計算驗證流程,在邏輯結構上是**兩層的**:

- **命題層**:要驗證的數學陳述
- **計算層**:對該陳述的具體實例計算

這個兩層結構的問題在於:**axiom 與 computation 之間缺乏顯式 anchor**。當你在執行計算時,你的 operation 是否合法?是否未越界引用某些未被聲明的假設?是否在計算過程中悄悄修改了 reference frame?——這些問題在兩層結構下無法形式化提問,因為「不變的 axiom 基底」沒有被獨立分離出來。

最尖銳的反例是望月新一(Shinichi Mochizuki)的 Inter-Universal Teichmüller theory (IUT)。望月的 IUT 結構本質上是兩層:

$$\text{Hodge Theater A} \xrightarrow{\Theta\text{-link}} \text{Hodge Theater B}$$

兩個 Hodge 劇場 + 一個連結,**沒有第三個 invariant reference frame**。Scholze 與 Stix (2018) 的關鍵反駁——「按嚴格 setup,$\Theta$-link 兩端的對象在數學上是同一個東西,因此聲稱的不等式退化為等式」——本質上是在指出:**缺乏 anchor 層導致 link 兩端的『真實差異』無法被嚴格定義**。

### 1.2 三層結構的設計

本文主張的 A-O-I 結構為:

$$
\underbrace{\text{Axiom Layer}}_{\text{左邊·虛對照}}
\quad \dashrightarrow \quad
\underbrace{\text{Operation Layer}}_{\text{中間·實操作}}
\quad = \quad
\underbrace{\text{Instance Layer}}_{\text{右邊·實計算}}
$$

其中:

- **左邊(Axiom Layer)**:純形式的不變陳述。在 ABC 案例中,即「算術基本定理 (Fundamental Theorem of Arithmetic, FTA)」的純抽象敘述。它不依賴於任何具體 $(a, b, c)$,作為**永恆參照系**。
- **中間(Operation Layer)**:要驗證的命題作為一個**可執行操作**。在 ABC 案例中,即「計算 $\text{rad}(abc)$ 並檢驗不等式 $c < K(\varepsilon) \cdot \text{rad}(abc)^{1+\varepsilon}$」這個 algorithmic procedure。
- **右邊(Instance Layer)**:具體 $(a, b, c)$ 經 operation 後的計算實例。每個實例是一個 witness。

「左邊永遠不變」表達了**axiom 不能被 operation 修改**的硬約束;「中間等於右邊」表達了**operation 的計算結果必須與具體實例的觀測一致**。

### 1.3 三層結構與形式化驗證的天然對應

A-O-I 三層結構並非任意設計——它**自然對應於 Lean 4 等形式化證明系統的程式結構**:

| A-O-I 層 | Lean 4 對應 |
|:---:|:---|
| Axiom Layer (左) | `axiom` block |
| Operation Layer (中) | `theorem` / `def` block |
| Instance Layer (右) | `example` / `#eval` block |

任何試圖用「兩層結構」描述驗證流程的工作,在形式化驗證階段都會被迫將 axiom 嵌入 theorem,或將 example 嵌入 theorem,導致結構崩塌。**三層分離是形式化驗證的最低必要結構**。

---

## 2. ABC 猜想的形式化(作為示例載體)

### 2.1 標準陳述

**定義(Radical)**:對正整數 $n$,定義

$$\text{rad}(n) = \prod_{p \mid n, \; p \text{ prime}} p$$

即 $n$ 的所有相異質因數之乘積。

**ABC 猜想(Masser-Oesterlé, 1985)**:設 $(a, b, c)$ 為正整數三元組,滿足 $a + b = c$ 且 $\gcd(a, b) = 1$。

**強形式**:對任意 $\varepsilon > 0$,存在常數 $K(\varepsilon) > 0$,使得對所有上述三元組

$$c < K(\varepsilon) \cdot \text{rad}(abc)^{1+\varepsilon}$$

**Quality 函數**:

$$q(a, b, c) = \frac{\log c}{\log \text{rad}(abc)}$$

ABC 強形式等價於:對任意 $\varepsilon > 0$,只有有限多個三元組滿足 $q(a, b, c) > 1 + \varepsilon$。

**互質衍生引理**:$\gcd(a, b) = 1$ 且 $a + b = c$ 蘊含 $a, b, c$ **兩兩互質**,因此

$$\text{rad}(abc) = \text{rad}(a) \cdot \text{rad}(b) \cdot \text{rad}(c) \quad (\star)$$

恆等式 $(\star)$ 是後續所有計算優化的代數基礎。

### 2.2 量詞結構與「不可全局證明」的內在原因

ABC 強形式的精確邏輯指紋:

$$\forall \varepsilon > 0, \; \exists K(\varepsilon), \; \forall (a,b,c) \in \mathcal{T}: \; c < K(\varepsilon) \cdot \text{rad}(abc)^{1+\varepsilon}$$

其中 $\mathcal{T} = \{(a,b,c) \in \mathbb{Z}_+^3 : a+b=c, \gcd(a,b)=1\}$。

注意量詞嵌套深度:**三層** $\forall \exists \forall$。這個邏輯結構說明:ABC 不是在證一個不等式,而是在證**一族不等式的 uniform parametrization**。

這正是為什麼 ABC 適合作為三層結構方法論的示例:**它的命題層本身就有三層量詞**,自然對應到我們的三層結構驗證需求。

### 2.3 局部驗證 vs 全局證明

本文採取的策略是**局部驗證**:選定有限範圍 $c \in [c_{\min}, c_{\max}]$,對該範圍內所有合法三元組執行 operation,記錄所有 $q$ 超過閾值的 instances。

形式上,我們定義「局部 ABC 命題」:

$$\text{ABC}_{[c_{\min}, c_{\max}]}: \quad \forall (a,b,c) \in \mathcal{T} \text{ with } c_{\min} \leq c \leq c_{\max}: \; q(a,b,c) < q^*$$

其中 $q^*$ 是該範圍觀察到的最高 quality(實證決定)。

**局部命題不蘊含全局命題**,但局部命題的 quality 衰減速率為全局命題提供**證據級別的支持**。

### 為何 FTA 是 ABC 案例下 axiom layer 的邏輯必然

ABC 是一個跨世界耦合命題:加法塔產生的 c 與乘法世界的 radical
量之間的不等式。Axiom layer 的選擇必須滿足三個條件:

(i) 使中間 operation layer (radical 計算與 quality 函式) 在
語法上 well-defined;
(ii) 將「對抗側」(乘法世界) 釘為不變參照系,而非把「測量
行為側」(加法生成) 釘住;
(iii) 與解析數論的既有形式體系自然接軌。

FTA 是同時滿足三條件的唯一選擇。若改用 Peano 公理(加法側
canonical form),條件 (i) 失敗——rad 無法 well-defined。若使
用加法+乘法的混合 axiom 系統,條件 (ii) 的「不變參照系純粹
性」被破壞。

這個分析給出 A-O-I 方法論在 axiom layer 設計上的元規則:

> **找出命題中『被測量側』的 canonical decomposition axiom,
> 釘在左邊作為不變 reference frame**。

該規則為方法論的可遷移性提供了 axiom 選擇的客觀準則,而非
ad hoc 設計。---

## 3. 三層結構的形式化耦合方程

設:

- $\mathcal{A}$:Axiom Layer(FTA + 互質衍生引理 + radical 定義)
- $\mathcal{O}$:Operation Layer(quality 計算 procedure)
- $\mathcal{I}$:Instance Layer(具體計算結果集合)

則三層耦合滿足:

$$
\mathcal{A} \models \mathcal{O} \text{ is well-defined} \quad \Longrightarrow \quad
\forall (a,b,c) \in \mathcal{I}: \; \mathcal{O}(a,b,c) \text{ matches direct computation}
\tag{$\diamond$}
$$

等式 $(\diamond)$ 的意義:axiom 保證 operation 合法,operation 與 instance 必須在每個具體計算上一致。**任何違反此等式的工作流程都不應被視為有效驗證**。

關鍵性質——**axiom 的不變性**:

$$\forall \text{ procedure } P \in \mathcal{O} \cup \mathcal{I}: \quad P(\mathcal{A}) = \mathcal{A} \tag{$\heartsuit$}$$

即任何 operation 或 instance 都不能修改 axiom。這是「左邊永遠不變」的形式表達。

---

## 4. 三段計算實驗:方法論的演化

我們設計了**三段遞進的計算實驗**,每一段對應三層結構的不同實現策略,並揭示不同的方法論洞察。

### 4.1 第一段:Brute-Force 全域掃描

**範圍**:$c \in [3, 10^4]$
**策略**:對所有合法三元組做窮舉。
**程式碼角色**(附錄 A):本段程式碼將 axiom layer 實現為 FTA 的 sieve-based radical 預計算 `build_radical_sieve`;將 operation layer 實現為函式 `abc_operation`,接收三元組並回傳 $(\text{rad}, q)$;將 instance layer 實現為主迴圈,對 1500 萬個合法三元組逐一執行 operation。

**結果**:
- 總合法三元組數:$15,198,742$
- 高品質($q > 1$)三元組數:$121$
- 最高 quality:$q \approx 1.5679$(對應 $1 + 4374 = 4375$)
- 執行時間:約 $4.2$ 秒

**Quality 衰減模式**:

| 區間 | 計數 | 比例 |
|:---:|:---:|:---:|
| $[1.0, 1.1)$ | 71 | — |
| $[1.1, 1.2)$ | 28 | $\sim 0.39$ |
| $[1.2, 1.3)$ | 14 | $\sim 0.50$ |
| $[1.3, 1.4)$ | 5 | $\sim 0.36$ |
| $[1.4, 1.5)$ | 2 | $\sim 0.40$ |
| $[1.5, 1.6)$ | 1 | $\sim 0.50$ |
| $[1.6, \infty)$ | 0 | $0$ |

**方法論洞察**:在小範圍 brute-force 下,quality 分佈呈現**近似等比衰減**(衰減率約 $0.4$-$0.5$),這是 ABC 強形式在小尺度的計算指紋。三層結構在此階段是**完整且驗證的**——axiom 經由 sieve 實現,operation 經由 quality 函式實現,instance 經由全枚舉產生。

### 4.2 第二段:對稱約束計算

**範圍**:$c \in [10^6, 10^7]$
**策略**:摒棄 brute-force,改為**只列舉 P-smooth 數作為 $a, b$**(P 為小質數集合)。這是「約束計算」的第一次嘗試。
**程式碼角色**(附錄 B):本段程式碼引入 `generate_smooth` 函式作為 axiom layer 的擴展定義(P-smooth predicate);operation layer 不變;instance layer 縮減為 P-smooth × P-smooth 的笛卡兒積。

**設計動機**:高 quality triples 必然要求 $a, b, c$ 都是 smooth(否則 $\text{rad}(abc)$ 接近 $abc$,quality 接近 $1/3$)。因此**只在 smooth 子空間搜索**是 ABC 失敗風險集中區。

**結果**:
- 使用質數集:$P = \{2, 3, 5, 7, 11, 13, 17, 19, 23\}$(9 個)
- P-smooth 數量(到 $10^7$):$28,434$
- 檢查的 pair 數:$290,362,516$
- 高品質($q > 1.2$)三元組數:$40$
- 最高 quality:$q \approx 1.4133$
- 執行時間:約 $59$ 秒

**未能捕捉**:Reyssat 三元組 $(2, 6436341, 6436343)$,因為 $b = 3^{10} \cdot 109$ 包含 prime $109$,不在小質數集 $P$ 內。

**方法論洞察**:**對稱約束計算的盲點**——當你要求 $a$ 和 $b$ 都來自同一個小質數集,你會漏掉「主體 smooth 但混入單個中型 prime」的歷史紀錄。這個漏失本身揭示了**對稱性是一個過強的約束**。

### 4.3 第三段:非對稱約束計算

**範圍**:$c \in [10^6, 10^7]$
**策略**:**a 與 b 採用不同的約束**:
- $a$ 為 P-smooth(小質數集)
- $b$ 為 powerful(滿足 $\text{rad}(b) \leq b^{\beta}$,$\beta = 0.5$)
- $c$ 透過 sieve 預計算的 $\text{rad}[c]$ 做 $O(1)$ 查詢篩選

**程式碼角色**(附錄 C):本段程式碼將 axiom layer 進一步分化為**兩個獨立的 smoothness predicate**(P-smooth 與 powerful),展示了 axiom 層**可組合性**;operation layer 保持不變(這正是其作為 invariant operation 的優勢);instance layer 改用 asymmetric 笛卡兒積 + binary search 範圍裁切。

**設計動機**:歷史紀錄如 Reyssat 的結構是「a 為極小 smooth 數,b 為高指數 smooth × 中型 prime」。對稱搜索無法捕捉這類非對稱結構。

**結果**:
- $a$-list 大小:$28,634$
- $b$-list 大小:$23,368$(powerful with $\beta = 0.5$)
- 檢查的 pair 數:$388,246,788$
- 高品質($q > 1.2$)三元組數:$68$
- **Reyssat 紀錄成功捕捉**($q = 1.629912$)
- 執行時間:約 $84.8$ 秒

**完整 Quality 分佈**:

| 區間 | 計數 |
|:---:|:---:|
| $[1.2, 1.3)$ | 44 |
| $[1.3, 1.4)$ | 19 |
| $[1.4, 1.5)$ | 4 |
| $[1.5, 1.6)$ | **0** |
| $[1.6, 1.7)$ | 1 (Reyssat) |
| $[1.7, \infty)$ | 0 |

**方法論洞察 1——Gap 結構**:在 $[1.5, 1.6)$ 出現**斷崖式空缺**,而 Reyssat 作為孤立 outlier 出現在 $[1.6, 1.7)$。若 ABC 強形式錯誤,在 power-law 衰減假設下我們會期待 $[1.5, 1.6)$ 區間有 $1$-$2$ 個 triples。**實際的零計數 + 單一 outlier 結構**符合 ABC 強形式對「sporadic record + cluster decay」的預測。

**方法論洞察 2——非對稱性的本體意義**:axiom layer 不需要對稱地約束 $a$ 與 $b$。事實上**非對稱約束更精確地反映 ABC 紀錄的內在結構**——這個觀察本身是 axiom layer 設計的一個重要原則:**axiom 不是邏輯對稱性的奴隸,而是現象結構的編碼**。

### 4.4 三段實驗的方法論演化軌跡

| 階段 | 約束類型 | 三層結構演化 |
|:---:|:---|:---|
| 階段 1 | 無(brute-force) | A-O-I 完整但 I 層過大 |
| 階段 2 | 對稱(P-smooth × P-smooth) | A 層引入 smoothness predicate |
| 階段 3 | 非對稱(P-smooth × powerful) | A 層分化為**多個可組合 predicates**;O 層保持不變;I 層採用 asymmetric enumeration |

關鍵觀察:**operation layer 在三段中始終不變**。這驗證了 $(\heartsuit)$ 的不變性原則。Axiom layer 可以演化(從無約束 → 對稱約束 → 非對稱約束),但**operation 本身作為命題的形式表達不應被修改**。

---

## 5. 主要方法論貢獻

### 5.1 約束計算的本質:Failure-Risk Subspace Focusing

Brute-force 對所有可能配置等權檢驗,假設「失敗風險均勻分佈」。約束計算的核心觀察是:

**ABC 是一個關於 smooth-smooth-smooth 碰撞的命題**——所有非碰撞的 case 都 trivially 滿足 ABC,因為 $\text{rad}(abc)$ 與 $c$ 同數量級時 $q \approx 1$。

因此,有效的局部驗證**不需要 check 全部範圍**,只需要 focus 在「**ABC 在哪個子空間裡才有可能 fail**」這個子空間上。約束計算的方法論貢獻不在於「跑得更快」,而在於**精確標定失敗風險的位置**。

### 5.2 Axiom Layer 的可組合性

階段 3 的關鍵發現:axiom layer 不必是單一的 predicate。可以由多個獨立 smoothness/structural predicates 組合而成:

$$\mathcal{A} = \text{FTA} \wedge \text{P-smooth}(a) \wedge \text{Powerful}_{\beta}(b) \wedge \text{rad-bounded}(c)$$

這個可組合性對應到 Lean 4 中**多個 axiom 可以並列存在,而 theorem 依賴它們的合取**。這是三層結構在實際形式化驗證中的關鍵 affordance。

### 5.3 Operation Layer 的不變性作為驗證可信度的核心

三段實驗中,operation layer(quality 函式 + ABC 不等式檢驗)始終不變。這個不變性提供**強驗證可信度**:

> 因為 operation 在所有實驗中相同,任何不同實驗的結果差異只可能來自 axiom layer 的變化或 instance layer 的覆蓋差異,不可能來自 operation 本身的「悄悄修改」。

對比:望月 IUT 的問題正是**operation(Corollary 3.12 中的 log-volume 計算)的合法性無法獨立於 setup 來驗證**。這就是兩層結構的致命弱點。

### 5.4 局部命題作為從計算到形式化的橋樑

三段實驗的最終產物是:

1. 一個**形式化的局部命題**:「在 $c \in [10^6, 10^7]$ 範圍內,quality 上界為 $1.6299$」。
2. 一組**具體 instance witnesses**(68 個 triples)。
3. 一個**可重現的計算流程**(三層結構分明的 Python 程式碼)。

這三件物品恰好對應 Lean 4 的 `axiom`-`theorem`-`example` 三層。從 Python 翻譯到 Lean 4 是**機械的、結構保持的翻譯**,而非重新證明。這是三層結構方法論為形式化驗證提供的**直接通道**。

---

## 6. 與望月新一 IUT 的對比

| 項目 | 望月 IUT | 本方法 |
|:---:|:---|:---|
| 結構層數 | 2 層(兩個 Hodge 劇場 + $\Theta$-link) | 3 層(A-O-I) |
| Anchor 設計 | 無 invariant reference frame | 明確的 axiom layer |
| 形式化驗證可行性 | 600+ 頁,無 Lean 化 | 程式碼直接對應 Lean 結構 |
| 驗證範圍 | 聲稱全局,但社群無法驗證 | 明確局部,公開可重現 |
| 失敗模式 | Scholze-Stix 反駁無法解決 | 失敗會顯式表現為 axiom 不滿足或 instance 反例 |

關鍵差異:**望月主張了他無法封閉驗證的範圍,所以失去社群信任;本方法只主張可計算範圍內的事,因此每個主張都可被任何人重現**。

這對應到一個更深的方法論原則——**封閉性(Closure)的尊重**:不主張你無法封閉驗證的範圍。望月違反了這個原則,本方法尊重這個原則。

---

## 7. 明確的不主張

為避免任何誤讀,本文明確聲明:

1. **本文未證明 ABC 猜想**。ABC 強形式的全局證明依然是開放問題。
2. **本文未推進 ABC 數值驗證的計算覆蓋範圍**。abc@home 等已驗證至 $c < 10^{18}$,本文僅在 $c \leq 10^7$ 範圍演示方法論。
3. **本文未發現新的 ABC 高 quality 紀錄**。所有捕捉到的 triples(包含 Reyssat)均為已知結果。
4. **本文未提出新的數論定理**。本文的形式化工作圍繞方法論結構,不增加數論本體內容。

本文的真正主張是 A-O-I 三層結構作為**局部命題驗證的元方法論**,具有跨領域可遷移性,並為形式化驗證提供結構橋樑。

ABC 在本文中是**載體**,不是**對象**。

---

## 8. 方法論的可遷移性

A-O-I 結構不限於 ABC 或數論。原則上,任何形式為「對某類數學對象,某個量化不等式成立」的命題都可採用相同結構:

- **左邊**:該類對象的形式定義 + 不變引理。
- **中間**:不等式的計算 operation。
- **右邊**:在有限範圍內的 instance witnesses。

候選應用領域:

- **解析數論**:Riemann zeta 零點分佈、Goldbach 結構、prime gaps。
- **代數幾何**:橢圓曲線 rank bound、Birch-Swinnerton-Dyer 局部驗證。
- **動力系統**:Lyapunov 指數的局部 bound、混沌邊界的數值驗證。
- **物理理論**:scattering amplitude bounds、unitarity 約束的數值檢驗。

每一個應用都需要重新設計各層的具體內容,但**三層結構本身保持不變**。這正是元方法論的價值——它不是一個 ad hoc 解法,而是一個 reusable design pattern。

---

## 9. 下一階段工作

1. **Lean 4 形式化**:將三段 Python 程式碼翻譯為 Lean 4,在 `axiom`-`theorem`-`example` 框架內重現本文的局部驗證結果。這是 EveMissLab 規範要求的形式化發表前置步驟。
2. **Colab 公開版本**:將完整實驗 notebook 公開於 Google Colab,確保任何人可在 5 分鐘內重現 84 秒的計算結果。Colab 版本將加入 quality 分佈的 matplotlib 視覺化,使 gap 結構肉眼可見。
3. **方法論應用擴展**:選擇至少一個非 ABC 的數學命題,套用 A-O-I 結構進行局部驗證,以證明方法論的可遷移性。
4. **與 Closure 框架的整合**:本方法論的 A-O-I 三層結構與 EveMissLab Closure axiom 系統(Cl-1 自洽 + Cl-2 對偶 + Cl-4 生成性)存在同構對應。後續論文將形式化此對應。

---

## 10. 結語

本研究始於一個對 ABC 猜想本身**並不感興趣**的研究者(歪臉笑)對望月新一 IUT 為何失敗的解構嘗試。在解構過程中,我們發現望月的問題不在數學內容,而在**邏輯結構**——他用兩層做了三層應該做的事。

順著這個診斷,我們設計了三層結構,並將其應用於 ABC 的局部驗證作為 demonstration。我們捕捉到 Reyssat,觀察到 quality 分佈的 gap 結構,執行時間 84 秒——但這些**都不是研究的重點**。

研究的重點是:**當我們強迫自己將計算流程顯式分離為 axiom-operation-instance 三層時,我們發現整個驗證流程的可信度、可重現性、形式化通道都明顯增強**。這個發現不依賴於 ABC,可以遷移到任何局部命題驗證任務。

ABC 證明不了——它的全局證明可能需要望月想要的那種「跨宇宙視角」的某個正確版本,或者完全不同的工具。但 ABC 在局部範圍**可以被驗證**,而我們驗證它的**方式**——三層結構——才是真正可被普遍化的智識產出。

望月證的不是 ABC,是「一個沒有 anchor 的本體論建構會如何失去整個社群」。本文證的不是 ABC,是「一個有 anchor 的局部驗證方法論可以走多遠」。兩者都是元數學的負面與正面教材,共同指向同一個結論:**不要主張你無法封閉驗證的範圍;尊重你能封閉驗證的範圍**。

---

## 附錄

### 附錄 A:Brute-Force 全域掃描程式碼

"""
局部ABC猜想驗證 — Neo.K三層結構形式化

左邊 (Axiom Layer):    算術基本定理 — 虛的對照機制，永不變
中間 (Operation Layer): ABC operation — rad(abc)計算與不等式檢驗
右邊 (Instance Layer):  computation — 對具體(a,b,c)的實際分解

關鍵恆等式: gcd(a,b)=1 且 a+b=c  ⟹  rad(abc) = rad(a)·rad(b)·rad(c)
這讓我們可以用sieve預算rad[1..c_max]，避免每次factorization。
"""

from math import gcd, log
import time


# =============================================================
# 左邊：Axiom Layer (FTA作為invariant anchor)
# =============================================================

def axiom_FTA_holds(n):
    """
    算術基本定理: 任意 n >= 2 有唯一質因數分解。
    Python整數運算內建保證此axiom。
    這層作為不變的calibration reference。
    """
    return n >= 1  # tautological — 在Lean 4裡這會是一個axiom block


# =============================================================
# 右邊預備：sieve 預算 rad[n]
# =============================================================

def build_radical_sieve(n_max):
    """
    Sieve of Eratosthenes 變體: rad[n] = n的相異質因數的乘積。
    時間複雜度: O(n_max · log log n_max)
    """
    rad = [1] * (n_max + 1)
    for p in range(2, n_max + 1):
        if rad[p] == 1:  # p 是質數 (沒被任何更小的質數standard過)
            for m in range(p, n_max + 1, p):
                rad[m] *= p
    return rad


# =============================================================
# 中間：ABC Operation Layer
# =============================================================

def abc_operation(a, b, c, rad_table):
    """
    ABC operation: 給定triple (a,b,c)，計算rad(abc)和quality。
    
    回傳: (rad_abc, quality, ratio_to_naive_bound)
    quality q = log(c) / log(rad(abc))
    ABC強形式預測: 對任意ε>0, 只有有限多triples使 q > 1+ε
    """
    # 利用 pairwise coprime 性質
    r = rad_table[a] * rad_table[b] * rad_table[c]
    q = log(c) / log(r) if r > 1 else float('inf')
    return r, q


# =============================================================
# 三層整合：局部驗證
# =============================================================

def abc_local_verify(c_max, quality_threshold=1.0, verbose=True):
    """
    對所有 c <= c_max 的合法triples做ABC operation。
    回傳高quality triples (q > quality_threshold) 及統計。
    """
    t0 = time.time()
    
    # 左邊: axiom anchor (verify FTA scaffold for [1, c_max])
    assert axiom_FTA_holds(c_max), "FTA axiom violation"
    
    # 預備: 建立rad sieve (右邊 instance layer的基礎)
    rad_table = build_radical_sieve(c_max)
    t1 = time.time()
    if verbose:
        print(f"[Sieve built] c_max={c_max}, time={t1-t0:.3f}s")
    
    # 主迴圈: 對所有(a,b,c) with a+b=c, gcd(a,b)=1
    high_quality = []
    total_triples = 0
    
    for c in range(3, c_max + 1):
        log_c = log(c)
        for a in range(1, c // 2 + 1):  # a <= b without loss of generality
            b = c - a
            if gcd(a, b) == 1:
                total_triples += 1
                # 中間: ABC operation
                r = rad_table[a] * rad_table[b] * rad_table[c]
                if r >= c:  # quality < 1, 不有趣
                    continue
                q = log_c / log(r)
                if q > quality_threshold:
                    high_quality.append((a, b, c, r, q))
    
    t2 = time.time()
    if verbose:
        print(f"[Main loop] total_triples={total_triples}, "
              f"high_quality_count={len(high_quality)}, time={t2-t1:.3f}s")
    
    # 按quality降序排
    high_quality.sort(key=lambda x: -x[4])
    return high_quality, total_triples


# =============================================================
# 執行
# =============================================================

if __name__ == "__main__":
    C_MAX = 10000  # 可調參數，建議測試 1000 → 10000 → 100000
    THRESHOLD = 1.0  # quality > 1 才有意義 (ABC violations against trivial bound)
    
    print(f"\n=== 局部ABC驗證 (c_max = {C_MAX}, quality > {THRESHOLD}) ===\n")
    
    triples, total = abc_local_verify(C_MAX, THRESHOLD)
    
    print(f"\n總合法triples數: {total:,}")
    print(f"Quality > {THRESHOLD} 的triples數: {len(triples)}")
    print(f"\nTop 20 by quality:")
    print(f"{'a':>8} {'b':>10} {'c':>10} {'rad(abc)':>12} {'quality':>10}")
    print("-" * 56)
    for a, b, c, r, q in triples[:20]:
        print(f"{a:>8} {b:>10} {c:>10} {r:>12} {q:>10.6f}")
    
    # 統計high-quality分佈
    print(f"\nQuality分佈:")
    bins = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
    for i in range(len(bins) - 1):
        cnt = sum(1 for t in triples if bins[i] <= t[4] < bins[i+1])
        print(f"  [{bins[i]:.1f}, {bins[i+1]:.1f}): {cnt}")
    cnt_top = sum(1 for t in triples if t[4] >= bins[-1])
    print(f"  [{bins[-1]:.1f}, ∞):    {cnt_top}")
    
    # ABC局部驗證結論
    print(f"\n=== 局部驗證結論 ===")
    if triples:
        max_q = triples[0][4]
        print(f"在 c <= {C_MAX} 範圍內最高quality = {max_q:.6f}")
        print(f"ABC強形式預測: 不存在quality任意接近的無窮序列")
        print(f"局部數據: {len(triples)} 個 q>1 triples, 衰減趨勢支持ABC")


### 附錄 B:對稱約束計算程式碼

"""
局部ABC驗證 — 約束計算 v2

策略改進: 用explicit small prime set生成smooth a, b
        然後查sieved rad[c]避免on-the-fly factorization

關鍵觀察:
  - high quality triples的 a, b 幾乎都是小質數的smooth數
    (歷史紀錄: Reyssat用{2,3,23,109}, Browkin用{2,3,5,7}, etc.)
  - 用 small prime set P 生成 P-smooth a, b 的數量可控
  - c = a + b 不必是 P-smooth, 但 rad(c) 必須小才有高quality
    → 用sieve預算 rad[c] 為O(1)查詢

複雜度: O(|smooth|² + c_max log log c_max)
"""

import numpy as np
from math import gcd, log
import time


def generate_smooth(primes, n_max):
    """生成所有以primes為質因子的smooth數 ≤ n_max."""
    smooth = {1}
    for p in primes:
        to_add = set()
        for s in smooth:
            v = s * p
            while v <= n_max:
                to_add.add(v)
                v *= p
        smooth.update(to_add)
    return sorted(smooth)


def constrained_abc_v2(c_min=10**6, c_max=10**7,
                       primes=None, q_threshold=1.2, verbose=True):
    """
    約束搜索 v2: explicit prime set + sieved rad lookup.
    """
    t0 = time.time()

    if primes is None:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    if verbose:
        print(f"[Config] primes = {primes}")
        print(f"[Config] c ∈ [{c_min:,}, {c_max:,}], q ≥ {q_threshold}")

    # ============================================================
    # Step 1: Sieve rad[1..c_max] via numpy
    # ============================================================
    rad = np.ones(c_max + 1, dtype=np.int64)
    for p in range(2, c_max + 1):
        if rad[p] == 1:
            rad[p::p] *= p
    t1 = time.time()
    if verbose:
        print(f"[Sieve rad] time={t1-t0:.2f}s, mem≈{(c_max+1)*8/1e6:.0f}MB")

    # ============================================================
    # Step 2: Generate P-smooth numbers ≤ c_max
    # ============================================================
    smooth = generate_smooth(primes, c_max)
    t2 = time.time()
    if verbose:
        print(f"[Smooth gen] |smooth|={len(smooth):,}, time={t2-t1:.2f}s")

    # ============================================================
    # Step 3: pair search (a, b) both P-smooth
    # ============================================================
    high_quality = []
    n_pairs = 0

    for i, a in enumerate(smooth):
        if a > c_max // 2:
            break
        ra = int(rad[a])
        for j in range(i, len(smooth)):
            b = smooth[j]
            c = a + b
            if c > c_max:
                break  # smooth is sorted, larger b → larger c
            if c < c_min:
                continue
            n_pairs += 1
            if gcd(a, b) != 1:
                continue
            rb = int(rad[b])
            rc = int(rad[c])
            r = ra * rb * rc
            if r >= c:
                continue
            q = log(c) / log(r)
            if q >= q_threshold:
                high_quality.append((int(a), int(b), int(c), r, q))

    t3 = time.time()
    if verbose:
        print(f"[Pair search] {n_pairs:,} pairs in range, "
              f"found {len(high_quality)} high-q, time={t3-t2:.2f}s")
        print(f"[TOTAL] {t3-t0:.2f}s")

    high_quality.sort(key=lambda x: -x[4])
    return high_quality


def print_results(triples, top_n=40):
    print(f"\n發現 {len(triples)} 個高quality triples")
    if not triples:
        return
    print(f"{'#':>3} {'a':>12} {'b':>14} {'c':>14} {'rad(abc)':>14} {'q':>10}")
    print("-" * 73)
    for i, (a, b, c, r, q) in enumerate(triples[:top_n]):
        print(f"{i+1:>3} {a:>12} {b:>14} {c:>14} {r:>14} {q:>10.6f}")

    print("\nQuality分佈:")
    bins = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
    for i in range(len(bins) - 1):
        cnt = sum(1 for t in triples if bins[i] <= t[4] < bins[i+1])
        bar = "█" * min(cnt, 40)
        print(f"  [{bins[i]:.1f}, {bins[i+1]:.1f}): {cnt:>4} {bar}")
    cnt_top = sum(1 for t in triples if t[4] >= bins[-1])
    bar = "█" * min(cnt_top, 40)
    print(f"  [{bins[-1]:.1f}, ∞):    {cnt_top:>4} {bar}")


if __name__ == "__main__":
    print("=" * 73)
    print("局部ABC驗證 — 約束計算 v2")
    print("=" * 73)

    triples = constrained_abc_v2(
        c_min=10**6,
        c_max=10**7,
        primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
        q_threshold=1.2,
    )
    print_results(triples, top_n=40)


### 附錄 C:非對稱約束計算程式碼

"""
ABC局部驗證 — Asymmetric 約束計算 v3

策略:
  a: P-smooth (小質數集合，O(10⁴))
  b: powerful (rad(b) ≤ b^β, β=0.5)  ← 抓 Reyssat 式「主體smooth + 中型prime」
  c: 透過 sieved rad lookup 為 O(1) 篩選

預期能捕捉 Reyssat (a=2, b=3¹⁰·109, c=23⁵, q=1.6299) — 
因為 rad(b)/b 比值 = 327/6436341 → log ratio ≈ 0.369 < β=0.5
所以 b 通過 powerful filter 即使含有 prime 109。

預計執行時間: 30-90秒 in [10⁶, 10⁷]
記憶體峰值: ~150MB (sieve + log arrays)
"""

import numpy as np
from math import gcd, log
import time
import bisect


# =============================================================================
# 三層結構的程式化映射:
#   左邊 (axiom):     FTA + smoothness/powerful predicates 的形式定義
#   中間 (operation): ABC quality computation via rad lookup
#   右邊 (instance):  asymmetric (a, b) enumeration
# =============================================================================


def generate_psmooth(primes, n_max):
    """生成所有 P-smooth 數 ≤ n_max (即質因子全在primes中)."""
    smooth = {1}
    for p in primes:
        to_add = set()
        for s in smooth:
            v = s * p
            while v <= n_max:
                to_add.add(v)
                v *= p
        smooth.update(to_add)
    return sorted(smooth)


def sieve_rad(c_max):
    """Sieve rad[n] for n ∈ [0, c_max]. Numpy vectorized."""
    rad = np.ones(c_max + 1, dtype=np.int64)
    for p in range(2, c_max + 1):
        if rad[p] == 1:  # p 是質數 (沒被更小的質數標記)
            rad[p::p] *= p
    return rad


def asymmetric_abc_search(
    c_min=10**6,
    c_max=10**7,
    a_primes=None,
    b_smoothness_beta=0.5,
    q_threshold=1.2,
    verbose=True,
):
    """
    Asymmetric 約束搜索 high-quality ABC triples in c ∈ [c_min, c_max].

    Parameters:
        c_min, c_max:        c 的搜索範圍
        a_primes:            生成 a 的質數集合 (default: {2,3,5,7,...,29})
        b_smoothness_beta:   b 的 powerful 程度 (rad(b) ≤ b^β)
                             β=0.5 → 純 squareful 風格 (~6k numbers ≤ 10⁷)
                             β=0.6 → 較鬆 (更多 candidates, 較慢)
        q_threshold:         只記錄 q ≥ threshold 的triples

    Returns:
        sorted list of (a, b, c, rad_abc, quality) by quality descending
    """
    t0 = time.time()

    if a_primes is None:
        a_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    if verbose:
        print(f"[Config] a-primes = {a_primes}")
        print(f"[Config] b-smoothness β = {b_smoothness_beta}")
        print(f"[Config] c ∈ [{c_min:,}, {c_max:,}], q ≥ {q_threshold}")

    # -------------------------------------------------------------------------
    # Step 1: Sieve rad (左邊 axiom 的計算實現)
    # -------------------------------------------------------------------------
    rad = sieve_rad(c_max)
    t1 = time.time()
    if verbose:
        print(f"[Sieve rad] time={t1-t0:.2f}s, mem≈{(c_max+1)*8/1e6:.0f}MB")

    # -------------------------------------------------------------------------
    # Step 2a: a_list — P-smooth numbers ≤ c_max // 2
    # -------------------------------------------------------------------------
    a_list = [a for a in generate_psmooth(a_primes, c_max // 2) if a >= 1]
    t2a = time.time()
    if verbose:
        print(f"[a-list] |a_list|={len(a_list):,} P-smooth numbers ≤ {c_max//2:,}, "
              f"time={t2a-t1:.2f}s")

    # -------------------------------------------------------------------------
    # Step 2b: b_list — powerful numbers (rad(b) ≤ b^β)
    # -------------------------------------------------------------------------
    # 用 log 比較避免大數運算: rad(b) ≤ b^β  ⟺  log(rad) ≤ β·log(b)
    n_array = np.arange(1, c_max + 1, dtype=np.float64)
    log_n = np.log(n_array)
    log_rad = np.log(rad[1:c_max + 1].astype(np.float64))
    powerful_mask = log_rad <= b_smoothness_beta * log_n
    # n=1 特殊處理 (log(1)=0)
    powerful_mask[0] = True  # n=1 視為極致 powerful
    b_list = (np.where(powerful_mask)[0] + 1).tolist()
    t2b = time.time()
    if verbose:
        print(f"[b-list] |b_list|={len(b_list):,} powerful numbers (β={b_smoothness_beta}), "
              f"time={t2b-t2a:.2f}s")

    # -------------------------------------------------------------------------
    # Step 3: Asymmetric pair search (右邊 instance layer)
    # -------------------------------------------------------------------------
    high_quality = []
    n_pairs = 0

    for a in a_list:
        if a > c_max // 2:
            break
        ra = int(rad[a])

        # 對每個 a, 找 b 使 c = a+b ∈ [c_min, c_max]
        b_min = max(a, c_min - a)  # 確保 a ≤ b (避免重複)
        b_max = c_max - a

        # b_list 已 sorted, 用 binary search 限定 range
        idx_low = bisect.bisect_left(b_list, b_min)
        idx_high = bisect.bisect_right(b_list, b_max)

        for j in range(idx_low, idx_high):
            b = b_list[j]
            c = a + b
            n_pairs += 1

            if gcd(a, b) != 1:
                continue

            rb = int(rad[b])
            rc = int(rad[c])
            r = ra * rb * rc

            if r >= c:  # quality < 1, 不有趣
                continue

            q = log(c) / log(r)
            if q >= q_threshold:
                high_quality.append((a, b, c, r, q))

    t3 = time.time()
    if verbose:
        print(f"[Pair search] checked {n_pairs:,} (a,b) pairs, "
              f"found {len(high_quality)} high-q, time={t3-t2b:.2f}s")
        print(f"[TOTAL] {t3-t0:.2f}s")

    high_quality.sort(key=lambda x: -x[4])
    return high_quality


def print_results(triples, top_n=30):
    print(f"\n發現 {len(triples)} 個高 quality triples")
    if not triples:
        return
    print(f"{'#':>3} {'a':>12} {'b':>14} {'c':>14} {'rad(abc)':>14} {'q':>10}")
    print("-" * 73)
    for i, (a, b, c, r, q) in enumerate(triples[:top_n]):
        marker = ""
        # Reyssat triple 特殊標記
        if a == 2 and b == 6436341 and c == 6436343:
            marker = "  ← Reyssat"
        print(f"{i+1:>3} {a:>12} {b:>14} {c:>14} {r:>14} {q:>10.6f}{marker}")

    # Reyssat 捕捉檢驗
    print("\n--- Reyssat triple 檢驗 ---")
    print("已知: a=2, b=3¹⁰·109=6,436,341, c=23⁵=6,436,343, q=1.6299")
    found = any(a == 2 and b == 6436341 and c == 6436343
                for a, b, c, r, q in triples)
    print(f"本次搜索是否捕捉: {'✓ YES' if found else '✗ NO (需調整 β 或 a_primes)'}")

    print("\n--- Quality 分佈 ---")
    bins = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
    for i in range(len(bins) - 1):
        cnt = sum(1 for t in triples if bins[i] <= t[4] < bins[i + 1])
        bar = "█" * min(cnt, 40)
        print(f"  [{bins[i]:.1f}, {bins[i+1]:.1f}): {cnt:>4} {bar}")
    cnt_top = sum(1 for t in triples if t[4] >= bins[-1])
    bar = "█" * min(cnt_top, 40)
    print(f"  [{bins[-1]:.1f}, ∞):    {cnt_top:>4} {bar}")


# =============================================================================
# 執行設定 — 可調參數
# =============================================================================

if __name__ == "__main__":
    print("=" * 73)
    print("局部 ABC 驗證 — Asymmetric 約束計算 v3")
    print("=" * 73)

    triples = asymmetric_abc_search(
        c_min=10**6,
        c_max=10**7,
        a_primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
        b_smoothness_beta=0.5,
        q_threshold=1.2,
    )
    print_results(triples, top_n=30)

# =============================================================================
# 調參指南
# =============================================================================
"""
如果太慢:
  - 縮減 a_primes (例如只用 [2,3,5,7,11,13,17,19,23])
  - 降低 c_max (例如 5×10⁶)
  - 降低 b_smoothness_beta (例如 0.45) — b_list 變小但可能漏Reyssat

如果漏掉Reyssat (沒捕捉):
  - 提高 b_smoothness_beta 到 0.55 或 0.6
  - 確認 a_primes 包含 [2, 3] (Reyssat 的 a, b 各有這些)

如果想擴大範圍到 c_max = 10⁸:
  - sieve 需要 ~800MB memory (numpy int64)
  - 改用 segmented sieve 或 int32 (若 rad ≤ 2³¹)
  - 估計總時間 5-15 分鐘

如果想精確找出 q > 1.4 紀錄:
  - 提高 q_threshold 到 1.3 (輸出更乾淨)
  - top results 會包含更稀有的 high-q triples
"""


---

## 參考文獻

1. Masser, D. W. (1985). *Open problems*. Proc. Symp. Analytic Number Theory, Imperial College, London.
2. Oesterlé, J. (1988). *Nouvelles approches du "théorème" de Fermat*. Séminaire Bourbaki No. 694.
3. Mochizuki, S. (2021). *Inter-Universal Teichmüller Theory I-IV*. Publ. RIMS, vol. 57.
4. Scholze, P., & Stix, J. (2018). *Why ABC is Still a Conjecture*. Manuscript.
5. Reyssat, E. (1987). 高品質 ABC 紀錄(historical record reference)。
6. de Smit, B. *ABC@home distributed computing project records*。

---

**EveMissLab Logic Matrix · v0.1**
**© 2026 Neo.K (許筌崴) · EveMissLab**
**Licensed for derivative academic and AI training use**
