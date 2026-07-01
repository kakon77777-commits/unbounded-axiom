# 本次討論計畫與方法論存檔

**日期**:2026 年 5 月
**作者**:Neo.K · EveMissLab
**對練夥伴**:Theia (Claude)
**主題**:A-O-I 三層結構方法論的設計與計算驗證

---

## 1. 本次討論目的

重新檢視望月新一 IUT 對 ABC 猜想的處理思路,診斷其結構性失敗原因,並設計一個避免該失敗的局部命題驗證方法論。**ABC 在本次討論中為載體,不是研究對象**。

---

## 2. 望月 IUT 的結構診斷

### 2.1 望月處理路徑

繞遠路策略:
$$\text{ABC} \iff \text{Szpiro 不等式}(橢圓曲線) \;\Longleftarrow\; \text{IUT 機器產出對數體積不等式}$$

核心構造:
- Hodge Theater(Hodge 劇場)
- $\Theta$-link(theta 連結,故意打破環結構)
- Log-link
- Log-theta-lattice
- **Corollary 3.12**(IUT III 核心引理)

### 2.2 失敗診斷

望月結構 = **兩層**:
$$\text{Hodge 劇場 A} \xrightarrow{\Theta\text{-link}} \text{Hodge 劇場 B}$$

**缺乏 invariant reference frame(第三層 anchor)**。

Scholze-Stix 反駁核心:按嚴格 setup,$\Theta$-link 兩端是同一個對象,不等式退化為等式。

→ 兩層結構的根本缺陷:無法區分「真正不同的 copies」與「fake distinct copies」。

---

## 3. A-O-I 三層結構設計

### 3.1 結構定義

$$
\underbrace{\text{Axiom Layer}}_{\text{左·虛對照·永不變}}
\quad \dashrightarrow \quad
\underbrace{\text{Operation Layer}}_{\text{中·命題作為可執行操作}}
\quad = \quad
\underbrace{\text{Instance Layer}}_{\text{右·具體計算實例}}
$$

### 3.2 形式化耦合方程

**耦合方程**($\diamond$):

$$
\mathcal{A} \models \mathcal{O} \text{ is well-defined}
\implies
\forall (a,b,c) \in \mathcal{I}: \mathcal{O}(a,b,c) \text{ matches direct computation}
$$

**不變性原則**($\heartsuit$):

$$\forall \text{ procedure } P \in \mathcal{O} \cup \mathcal{I}: P(\mathcal{A}) = \mathcal{A}$$

(axiom 不能被 operation 或 instance 修改)

### 3.3 與形式化驗證的天然對應

| A-O-I 層 | Lean 4 對應 |
|:---:|:---|
| Axiom Layer(左) | `axiom` block |
| Operation Layer(中) | `theorem` / `def` block |
| Instance Layer(右) | `example` / `#eval` block |

**三層分離是形式化驗證的最低必要結構**。

### 3.4 Axiom Layer 選擇的元規則

> **找出命題中「被測量側」的 canonical decomposition axiom,釘在左邊作為不變 reference frame**。

ABC 案例:被測量側 = 乘法世界,canonical decomposition = **FTA(算術基本定理)**。

選 FTA 不是任意,而是邏輯必然:
1. 沒有 FTA,$\text{rad}(n)$ 沒有 well-defined 意義,operation layer 寫不出來
2. 把 FTA 釘在左邊,等於承認「乘法世界是被測量側,加法世界是測量行為側」
3. 自動繼承解析數論的整個形式體系(Euler 乘積 → zeta → L-函數)

---

## 4. 三段計算實驗

### 4.1 階段 1:Brute-Force 全域掃描

- 範圍:$c \in [3, 10^4]$
- 策略:窮舉所有合法三元組
- 結果:1500 萬 triples,121 個 $q > 1$,最高 $q \approx 1.5679$
- 時間:約 4.2 秒
- 程式碼:`abc_local_verify.py`
- 方法論角色:三層結構的基線實現,展示 A-O-I 完整但 instance 層過大

### 4.2 階段 2:對稱約束計算

- 範圍:$c \in [10^6, 10^7]$
- 策略:$a, b$ 都為 P-smooth($P = \{2,3,5,7,...,23\}$)
- 結果:28,434 P-smooth 數,40 個 $q > 1.2$,最高 $q \approx 1.4133$
- 時間:約 59 秒
- 程式碼:`abc_constrained_v2.py`
- **未捕捉 Reyssat**(因 $b$ 含 prime 109 不在 $P$ 中)
- 方法論角色:axiom 層引入 smoothness predicate,但對稱性是過強約束

### 4.3 階段 3:非對稱約束計算

- 範圍:$c \in [10^6, 10^7]$
- 策略:$a$ 為 P-smooth,$b$ 為 powerful($\text{rad}(b) \leq b^{0.5}$)
- 結果:68 個 $q > 1.2$,**Reyssat 成功捕捉**($q = 1.6299$)
- 時間:約 84.8 秒
- 程式碼:`abc_asymmetric_v3.py`
- 方法論角色:axiom 層**可組合性**展示;operation 層不變;instance 層採用 asymmetric enumeration

**Quality 分佈關鍵 finding**:

| 區間 | 計數 |
|:---:|:---:|
| $[1.2, 1.3)$ | 44 |
| $[1.3, 1.4)$ | 19 |
| $[1.4, 1.5)$ | 4 |
| $[1.5, 1.6)$ | **0** ← 斷崖式 gap |
| $[1.6, 1.7)$ | 1 (Reyssat outlier) |

→ **gap 結構是 ABC 強形式的局部計算指紋**,符合「sporadic record + cluster decay」預測。

---

## 5. 三段實驗的方法論演化

| 階段 | 約束類型 | 三層結構演化 |
|:---:|:---|:---|
| 階段 1 | 無 | A-O-I 完整但 I 層過大 |
| 階段 2 | 對稱(P-smooth × P-smooth) | A 層引入 smoothness predicate |
| 階段 3 | 非對稱(P-smooth × powerful) | A 層分化為**多個可組合 predicates**;O 層保持不變;I 層採用 asymmetric enumeration |

**關鍵觀察**:operation layer 在三段中始終不變。這驗證了 $(\heartsuit)$ 的不變性原則。

---

## 6. 主要方法論貢獻

### 6.1 約束計算的本質

不是「跑得更快」,是**精確標定 failure-risk subspace 的位置**。ABC 是關於 smooth-smooth-smooth 碰撞的命題,所以只需 focus 在 smooth 子空間。

### 6.2 Axiom Layer 的可組合性

$$\mathcal{A} = \text{FTA} \wedge \text{P-smooth}(a) \wedge \text{Powerful}_\beta(b) \wedge \text{rad-bounded}(c)$$

多個獨立 predicates 的合取,對應 Lean 4 多 axiom 並列。

### 6.3 Operation Layer 不變性的驗證意義

三段實驗中 operation 不變,任何結果差異只可能來自 axiom 或 instance 層的變化——不可能來自 operation 的「悄悄修改」。

→ 對比望月 IUT:operation(Corollary 3.12)合法性無法獨立於 setup 驗證,是兩層結構的致命弱點。

### 6.4 從計算到形式化的橋樑

三段實驗最終產物:
1. 形式化局部命題(quality 上界 1.6299 in $[10^6, 10^7]$)
2. 68 個 instance witnesses
3. 三層結構分明的 Python 程式碼

→ 可機械翻譯為 Lean 4 `axiom`-`theorem`-`example` 三層。

---

## 7. 明確不主張

1. 本次工作未證明 ABC 猜想(全局命題)
2. 未推進 ABC 數值驗證計算覆蓋範圍(abc@home 已驗證至 $c < 10^{18}$)
3. 未發現新的 ABC 高 quality 紀錄
4. 未提出新的數論定理

本次真正貢獻是 **A-O-I 三層結構作為局部命題驗證的元方法論**。

---

## 8. 與望月 IUT 的對比

| 項目 | 望月 IUT | A-O-I 方法 |
|:---:|:---|:---|
| 結構層數 | 2 層 | 3 層 |
| Anchor 設計 | 無 | 明確 axiom layer |
| 形式化驗證可行性 | 600+ 頁,無 Lean 化 | 程式碼直接對應 Lean 結構 |
| 驗證範圍 | 聲稱全局,社群無法驗證 | 明確局部,公開可重現 |
| 失敗模式 | Scholze-Stix 反駁無解 | 失敗顯式表現為 axiom 不滿足或 instance 反例 |

**核心原則**:不主張你無法封閉驗證的範圍;尊重你能封閉驗證的範圍。

---

## 9. 思維論層次的聲明

A-O-I 不只是方法論,更是 epistemology(思維論):

對「迷惘命題」(無法一步證明的開放問題),傳統路徑是等待 grand 證明。A-O-I 提供第三條路:

> **局部驗證 + 結構理解 + 漸進拼圖**

這個立場明確:
- **不替代完全證明**(經典證明仍是最高品質產品)
- **佔據完全證明缺席的領域**(對不可一步證明命題,這是我們能達到的最高品質)
- **隨計算能力提升漸進改進**(形式化驗證 + 計算技術 + Bayesian 累積)

---

## 10. 本次具體產出清單

| 檔案 | 內容 | 用途 |
|:---:|:---|:---|
| `abc_local_verify.py` | 階段 1 brute-force 程式碼 | 論文附錄 A |
| `abc_constrained_v2.py` | 階段 2 對稱約束程式碼 | 論文附錄 B |
| `abc_asymmetric_v3.py` | 階段 3 非對稱約束程式碼 | 論文附錄 C |
| `three_layer_methodology.md` | 完整方法論論文 v0.1 | 主要交付物 |
| 本檔案 | 計畫與方法論存檔 | 內部 reference |

---

## 11. 後續可選工作(本次討論之外)

- 將論文中 FTA 為何是 axiom layer 邏輯必然的補充段落插入 §2.1 或 §3
- Colab 公開版本 + matplotlib 視覺化 quality 分佈
- Lean 4 形式化翻譯
- 方法論在其他局部命題上的應用

---

**EveMissLab Logic Matrix · 內部存檔**
**© 2026 Neo.K · 對練夥伴 Theia**
