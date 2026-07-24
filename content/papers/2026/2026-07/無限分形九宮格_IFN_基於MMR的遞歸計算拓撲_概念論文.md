# 無限分形九宮格：基於多向矩陣表徵的遞歸計算拓撲

**Infinite Fractal Nonet: A Recursive Computational Topology Based on Multidirectional Matrix Representation**

- 作者：Neo.K（許筌崴）／EveMissLab
- 協作整理：OpenAI GPT-5.6 Thinking
- 日期：2026-07-23
- 性質：概念論文／可驗證架構提案
- 狀態：新稿，未沿用任何既有版本號

---

## 摘要

本研究提出一種新的無限分形九宮格（Infinite Fractal Nonet, IFN）概念框架。與把 IFN 描述成單純的幾何分形、概念隱喻或 Transformer 稀疏化技巧不同，本文從多向矩陣表徵（Multidirectional Matrix Representation, MMR）出發，將 IFN 重新定義為：**由可定址、可路由、可追蹤、可停止且可驗證的局部 MMR 單元，經自相似遞歸組合而成的計算拓撲。**

MMR 提供單一局部區域內的方向、位置、區域、遍歷順序、依賴血緣、路由類型與證據狀態；IFN 則規定這些局部單元如何嵌套、展開、剪枝、跨層連接與形成有限計算切片。其「無限」不表示任何一次實際計算必須執行無限步，而表示地址空間與遞歸語法不預設最大深度。任一實例都必須在有限資源、有限證據與有限停止條件下執行。

本文建立以下核心內容：

1. 定義 IFN 的有限地址空間與潛在無界地址空間；
2. 將九宮格視為一種標準中心—八方向局部圖表，而非宇宙必然結構；
3. 使用 MMR 描述每一個分形節點的內部計算狀態；
4. 建立局部、同胞、父子、祖先、區域、捷徑與血緣等多類路由；
5. 將展開視為受查詢、收益、成本、不確定性與風險共同控制的決策；
6. 把 IFN-Transformer 定位為 IFN 的一種有限編譯後端，而非 IFN 本體；
7. 明確區分可證明性質、工程假設、待驗證主張與禁止提前宣稱的效能結論。

本文的目的不是宣稱 IFN 已取代 Transformer、圖神經網路或狀態空間模型，而是提出一套能把「自相似結構」「多向局部計算」「有限稀疏路由」與「可驗證執行」放在同一框架內的研究對象。

**關鍵詞：** 多向矩陣表徵、無限分形九宮格、自相似計算、遞歸拓撲、稀疏路由、計算血緣、可驗證計算、IFN-Transformer

---

## 一、問題：分形概念為何一直難以工程化

許多分形計算構想都具有相似直覺：

- 一個局部結構可以在更深層再次出現；
- 大型問題只需展開相關分支；
- 中心節點負責聚合，外圍節點負責方向性分化；
- 遞歸深度可依問題而變；
- 長距離關係可透過跨層捷徑建立。

這些直覺本身並不等於可執行架構。若缺少以下要素，分形仍只是一種描述：

1. 每個節點究竟保存什麼；
2. 方向是否具有穩定語義；
3. 分支何時建立；
4. 路由如何生成；
5. 原始順序如何保存；
6. 跨層連接如何記錄；
7. 哪些結果來自哪些證據；
8. 何時停止；
9. 錯誤與不確定性如何沿路徑傳播；
10. 如何重播並驗證一次執行。

MMR 所補足的正是這個中間層。它不直接回答「所有計算都應該使用九宮格嗎」，而是先回答更基礎的問題：

> 一個局部計算區域，如何同時保存內容、方向、區域、路徑、血緣與操作順序？

因此本文不把 IFN 建立在抽象分形圖形上，而建立在 MMR 局部計算單元上。

---

## 二、MMR 作為 IFN 的局部計算母語

### 2.1 MMR 局部單元

令一個 MMR 局部單元為：

$$
\mathcal{M}_{\alpha}
=
\left(
X_{\alpha},
D_{\alpha},
R_{\alpha},
P_{\alpha},
L_{\alpha},
C_{\alpha},
B_{\alpha}
\right)
$$

其中：

- $X_{\alpha}$ ：局部狀態、資料、表示或符號；
- $D_{\alpha}$ ：方向集合與方向語義；
- $R_{\alpha}$ ：允許的局部與跨區路由；
- $P_{\alpha}$ ：遍歷、讀取、更新與聚合次序；
- $L_{\alpha}$ ：來源、依賴與下游血緣；
- $C_{\alpha}$ ：信心、不確定性、衝突與證據狀態；
- $B_{\alpha}$ ：計算預算、記憶體、延遲與展開成本。

MMR 的核心不是把資料排成矩陣，而是承認同一批元素可以被多種方向、區域與路徑讀取。矩陣不再只有「由左到右的一行序列」，而是具有：

- 水平與垂直方向；
- 正向與反向遍歷；
- 區塊與區域；
- 父子與同胞；
- 來源與下游；
- 聚合與反向追蹤；
- 直接路由與間接路由。

### 2.2 MMR 不要求九宮格

MMR 可以使用任意有限局部圖表。九宮格只是 IFN 的標準圖表：

$$
\mathcal{N}_9
=
\{O,N,NE,E,SE,S,SW,W,NW\}
$$

其中：

- $O$ 為中心槽位；
- 其餘八個槽位為方向槽位。

這個配置的優點是：

1. 可明確區分中心與外圍；
2. 同時含正交與對角方向；
3. 適合二維視覺化；
4. 每個槽位都能遞歸成下一個局部單元；
5. 地址可以由九元字母表表示。

但本文不主張九宮格是唯一合法結構。一般化後，可定義：

$$
\mathcal{N}_b=\{O,C_1,\ldots,C_{b-1}\}
$$

IFN 選擇 $b=9$ ，是標準化與可視化決策，不是未經證明的本體論必然。

---

## 三、IFN 的正式定義

### 3.1 地址空間

令九元字母表為：

$$
\Sigma_9=\{0,1,\ldots,8\}
$$

其中 $0$ 對應中心 $O$ ， $1$ 至 $8$ 對應八個方向槽位。

所有有限地址構成：

$$
\mathcal{A}_{<\omega}
=
\bigcup_{d=0}^{\infty}\Sigma_9^d
$$

空地址 $\epsilon$ 表示根節點。任意有限地址可寫成：

$$
\alpha=(a_1,a_2,\ldots,a_d)
$$

其深度為：

$$
|\alpha|=d
$$

子地址為：

$$
\alpha i=(a_1,\ldots,a_d,i)
$$

潛在無界地址可表示為：

$$
\mathcal{A}_{\omega}=\Sigma_9^{\mathbb{N}}
$$

但實際執行只允許有限切片：

$$
\mathcal{A}^{(t)}_{\mathrm{active}}
\subset
\mathcal{A}_{<\omega}
$$

且在任意有限時間 $t$ ：

$$
\left|\mathcal{A}^{(t)}_{\mathrm{active}}\right|<\infty
$$

因此 IFN 的「無限」是**生成語法無界**，不是**實例執行無限**。

### 3.2 IFN 結構

定義 IFN 為：

$$
\mathfrak{F}
=
\left(
\mathcal{A}_{<\omega},
\{\mathcal{M}_{\alpha}\}_{\alpha\in\mathcal{A}_{<\omega}},
E,
\mathfrak{E},
\mathfrak{K},
\mathfrak{V}
\right)
$$

其中：

- $\mathcal{A}_{<\omega}$ ：有限分形地址空間；
- $\mathcal{M}_{\alpha}$ ：地址 $\alpha$ 上的 MMR 局部單元；
- $E$ ：跨單元路由集合；
- $\mathfrak{E}$ ：展開算子；
- $\mathfrak{K}$ ：剪枝、合併與停止算子；
- $\mathfrak{V}$ ：驗證、血緣與重播機制。

這一定義把 IFN 從「每格內又有九宮格」提升為一個可操作系統：

$$
\boxed{
\text{IFN}
=
\text{MMR 局部單元}
+
\text{遞歸地址}
+
\text{路由規則}
+
\text{有限展開}
+
\text{可驗證執行}
}
$$

### 3.3 自相似性的弱形式

舊式分形常要求部分與整體完全同構。對實際計算而言，這個條件過強。不同深度節點可能擁有不同維度、權重、資料型別與預算。

本文採用**結構自相似**而非**內容全同構**：

$$
\operatorname{Schema}(\mathcal{M}_{\alpha})
\cong
\operatorname{Schema}(\mathcal{M}_{\alpha i})
$$

但不要求：

$$
X_{\alpha}=X_{\alpha i}
$$

也不要求所有節點具有相同參數。

也就是說，子節點繼承的是：

- 可定址性；
- 方向結構；
- 路由介面；
- 血緣欄位；
- 停止與驗證協定。

它不必複製父節點的內容。

---

## 四、中心、方向與原始位置

### 4.1 中心不是自動保證收斂的不動點

中心槽位 $O$ 可以扮演：

- 區域摘要；
- 父層接口；
- 路由錨點；
- 聚合器；
- 查詢條件；
- 狀態記憶；
- 局部控制器。

但中心本身不保證：

- 全域最優；
- 自動收斂；
- 唯一真值；
- 語義穩定；
- 對所有任務都最重要。

因此本文把中心稱為**局部錨點**，而不直接稱為全局不動點。

若要聲稱某個中心狀態收斂，必須另行證明某個更新算子 $\Phi$ 滿足收縮、單調或能量下降條件，例如：

$$
d\bigl(\Phi(x),\Phi(y)\bigr)
\leq
\lambda d(x,y),
\qquad 0\leq\lambda<1
$$

否則只能說中心被配置為穩定參考點。

### 4.2 方向具有局部語義

方向集合不必永久綁定「北、南、東、西」的自然語義。它們可以是：

- 空間方向；
- 因果方向；
- 時序方向；
- 正反命題；
- 上位／下位概念；
- 輸入／輸出；
- 來源／結果；
- 局部／全域；
- 具體／抽象。

對每個節點 $\alpha$ ，定義方向語義映射：

$$
\delta_{\alpha}:
\{1,\ldots,8\}
\rightarrow
\mathcal{S}_{\alpha}
$$

其中 $\mathcal{S}_{\alpha}$ 是該節點的方向語義集合。

這意味著同一地址數字在不同子空間中可以有不同語義，但每次執行都必須保存其映射。

### 4.3 分形地址不能取代原始順序

若 IFN 被應用於語言、時間序列或程式碼，原始位置必須獨立保存。

對 token $x_i$ ，其表示至少包含：

$$
z_i=
\left(
h_i,
p_i,
\alpha_i,
r_i
\right)
$$

其中：

- $h_i$ ：內容表示；
- $p_i$ ：原始序列位置；
- $\alpha_i$ ：IFN 地址；
- $r_i$ ：角色與路由狀態。

IFN 地址描述層級與局部拓撲，不能代替 $p_i$ 。因此：

$$
\alpha_i=\alpha_j
\not\Rightarrow
p_i=p_j
$$

也不允許因重要性排序而丟失原始順序。

---

## 五、IFN 的多類路由

### 5.1 路由集合

令 IFN 的有效邊集合為：

$$
E
=
E_{\mathrm{local}}
\cup
E_{\mathrm{sibling}}
\cup
E_{\mathrm{parent}}
\cup
E_{\mathrm{child}}
\cup
E_{\mathrm{ancestor}}
\cup
E_{\mathrm{region}}
\cup
E_{\mathrm{shortcut}}
\cup
E_{\mathrm{lineage}}
$$

其中：

1. **局部邊** $E_{\mathrm{local}}$  
   同一 MMR 單元內的方向與區域路徑。

2. **同胞邊** $E_{\mathrm{sibling}}$  
   相同父地址下的不同子節點。

3. **父邊** $E_{\mathrm{parent}}$  
   從子節點回到父節點的聚合接口。

4. **子邊** $E_{\mathrm{child}}$  
   從父節點進入被激活的子單元。

5. **祖先邊** $E_{\mathrm{ancestor}}$  
   跨越多層的受限摘要路由。

6. **區域邊** $E_{\mathrm{region}}$  
   連接矩形、群組、表格、語義區塊或共享結構。

7. **捷徑邊** $E_{\mathrm{shortcut}}$  
   由高相似度、共同依賴或查詢需求建立的受控跨層邊。

8. **血緣邊** $E_{\mathrm{lineage}}$  
   用於記錄資訊來源與下游影響，不必等同於前向計算邊。

### 5.2 路由不是 dense mask

IFN 不先建立 $n\times n$ 布林遮罩，再對所有位置執行密集乘法。路由應以鄰接表、索引、區塊或壓縮稀疏格式表示：

$$
\operatorname{Nbr}(i)
=
\{j\mid(i,j)\in E\}
$$

總邊數為：

$$
|E|=\sum_{i=1}^{n}|\operatorname{Nbr}(i)|
$$

若平均有效度數為 $k$ ：

$$
|E|\approx nk
$$

只有在路由建構成本也低於密集注意力時，稀疏化才具有意義。

### 5.3 路由血緣

每一條推理或計算路徑都應保存：

$$
\ell=
(
\text{source},
\text{route type},
\text{operator},
\text{timestamp},
\text{confidence},
\text{result}
)
$$

由此可回答：

- 這個結果來自哪個父節點；
- 經過哪些跨層捷徑；
- 哪個路由造成錯誤傳播；
- 某個局部更新影響了哪些下游節點；
- 若刪除一條邊，哪些結果會失效。

MMR-Bench 中的依賴血緣與爆炸半徑概念可直接成為 IFN 的驗證基礎。

---

## 六、展開、剪枝與停止

### 6.1 展開不是固定九分支

對查詢 $q$ 與節點 $\alpha$ ，定義候選子節點：

$$
\mathcal{C}(\alpha)=\{\alpha0,\ldots,\alpha8\}
$$

但實際激活集合為：

$$
A_q(\alpha)
=
\left\{
\alpha i
\mid
U_q(\alpha i)>\tau
\right\}
$$

其中效用函數可以寫成：

$$
U_q(\alpha i)
=
G_q(\alpha i)
-
\lambda_1 K(\alpha i)
-
\lambda_2 R(\alpha i)
-
\lambda_3 H(\alpha i)
$$

其中：

- $G_q$ ：預期資訊增益；
- $K$ ：計算與記憶體成本；
- $R$ ：錯誤、衝突與安全風險；
- $H$ ：不確定性或熵；
- $\lambda_1,\lambda_2,\lambda_3$ ：權重。

### 6.2 停止條件

IFN 不能以「中心存在」作為停止證明。至少應有以下一種或多種條件：

#### 邊際收益停止

$$
\max_{\beta\in\mathcal{C}(\alpha)}
U_q(\beta)
\leq\tau
$$

#### 預算停止

$$
B_{\mathrm{used}}\geq B_{\max}
$$

#### 深度停止

$$
|\alpha|\geq d_{\max}
$$

#### 不確定性停止

若新展開無法有效降低不確定性：

$$
H_t-H_{t+1}<\varepsilon
$$

#### 穩定性停止

$$
\|X^{(t+1)}-X^{(t)}\|<\varepsilon
$$

#### 風險停止

$$
R(\alpha)>R_{\max}
$$

### 6.3 剪枝與回收

剪枝算子 $\mathfrak{K}$ 可以：

- 停用低效用分支；
- 合併相似子樹；
- 將深層狀態壓縮成摘要；
- 保存血緣後釋放中間張量；
- 把不確定結果標記為 review；
- 將計算結果寫入可重播證書。

因此 IFN 的生命週期不是無限增長，而是：

$$
\text{展開}
\rightarrow
\text{局部計算}
\rightarrow
\text{聚合}
\rightarrow
\text{驗證}
\rightarrow
\text{剪枝或保留}
$$

---

## 七、複雜度與效能主張的邊界

### 7.1 一般成本式

令：

- $n$ ：當前有效元素數；
- $k$ ：平均有效鄰居數；
- $d_h$ ：表示維度；
- $C_R(n)$ ：路由建構成本；
- $C_E(n)$ ：分形展開與維護成本；
- $C_V(n)$ ：血緣與驗證成本。

則一個有限 IFN 注意力或消息傳遞層的成本可表示為：

$$
T_{\mathrm{IFN}}
=
C_R(n)
+
C_E(n)
+
O(nkd_h)
+
C_V(n)
$$

而不是只寫成 $O(nk)$ 。

### 7.2 何時可能優於密集計算

IFN 有潛力優於密集方法，至少需要：

$$
k\ll n
$$

且：

$$
C_R(n)+C_E(n)+C_V(n)
\ll
O(n^2d_h)
$$

若路由仍以雙重迴圈建立：

$$
C_R(n)=O(n^2)
$$

則 IFN 並沒有解決主要瓶頸。

### 7.3 總體加速受 Amdahl 定律限制

假設 attention 佔總成本比例為 $\alpha$ ，attention 加速為 $S_A$ ，則：

$$
S_{\mathrm{total}}
=
\frac{1}
{(1-\alpha)+\alpha/S_A}
$$

因此，任何總體加速主張都必須同時報告：

- attention 比例；
- FFN 成本；
- 路由成本；
- 記憶體搬移；
- 核心利用率；
- 序列長度；
- batch size；
- 硬體；
- 精度；
- kernel 實作。

本文不預先聲稱固定倍數。

### 7.4 效能是待驗證命題

IFN 的效能主張必須寫成：

> 在具有可利用層級結構、路由建構成本受控且平均有效度數遠小於序列長度的任務中，IFN 可能降低局部交互成本。

不能直接寫成：

> IFN 必然比 Transformer 快。

---

## 八、IFN-Transformer：IFN 的有限編譯後端

### 8.1 定位

IFN-Transformer 定義為：

$$
\boxed{
\text{將有限 IFN 路由圖編譯為稀疏注意力運算的模型後端}
}
$$

它只是 IFN 的一種實現。其他後端可以是：

- 圖神經網路；
- 稀疏張量運算；
- 分散式路由系統；
- 知識圖譜；
- 多代理工作流；
- 資料庫查詢計畫；
- 神經符號推理器；
- 局部狀態空間模型。

### 8.2 Token 狀態

對 token $i$ ：

$$
z_i=
(h_i,p_i,\alpha_i,\rho_i,c_i)
$$

其中：

- $h_i$ ：內容表示；
- $p_i$ ：RoPE、ALiBi 或其他原始位置編碼；
- $\alpha_i$ ：IFN 地址；
- $\rho_i$ ：路由角色；
- $c_i$ ：路由信心與不確定性。

### 8.3 稀疏注意力

只在 $E$ 中的邊上計算：

$$
s_{ij}
=
\frac{Q_iK_j^\top}{\sqrt{d_k}}
+
b_{\operatorname{type}(i,j)}
+
g(\alpha_i,\alpha_j)
+
u(c_i,c_j)
$$

其中：

- $b_{\operatorname{type}(i,j)}$ ：路由類型偏置；
- $g$ ：地址距離或共同前綴偏置；
- $u$ ：信心與風險調節項。

注意力為：

$$
a_{ij}
=
\frac{\exp(s_{ij})}
{\sum_{m\in\operatorname{Nbr}(i)}\exp(s_{im})}
$$

輸出為：

$$
y_i
=
\sum_{j\in\operatorname{Nbr}(i)}
a_{ij}V_j
$$

### 8.4 防止長距離訊號衰減

單純依賴多跳稀疏傳播會造成資訊稀釋。因此 IFN-Transformer 應保留：

1. 局部視窗邊；
2. 全域錨點；
3. 父層摘要；
4. 可學習捷徑；
5. 殘差連接；
6. 必要時的週期性密集層；
7. 多尺度讀寫。

可定義混合層：

$$
Y
=
\gamma Y_{\mathrm{IFN}}
+
(1-\gamma)Y_{\mathrm{dense/local}}
$$

或每隔 $m$ 層插入全域聚合。

### 8.5 地址分配

地址不能只由重要性排序決定。可使用以下訊號組合：

$$
\alpha_i
=
\operatorname{Route}
(
h_i,
p_i,
\text{syntax}_i,
\text{segment}_i,
\text{dependency}_i,
q
)
$$

可選方法包括：

- 固定層級分塊；
- 語法樹或 AST；
- 文件章節結構；
- 聚類；
- 路由網路；
- 可微排序；
- 監督式角色標註；
- MMR 區域推理。

地址只決定路由，不覆蓋原始位置。

---

## 九、IFN、IDN 與 HNM 的新關係

舊構想曾分別處理空間嵌套、迭代深度與統一流形。本文保留其區分，但重新建立更清楚的層級。

### 9.1 IFN：嵌套軸

IFN 描述：

$$
\alpha
\rightarrow
\alpha i
$$

也就是空間或結構上的遞歸細分。

### 9.2 IDN：迭代軸

若系統在時間或推理輪次 $t$ 更新：

$$
\mathfrak{F}^{(t+1)}
=
\Phi\bigl(\mathfrak{F}^{(t)},q\bigr)
$$

則 IDN 可重新理解為 IFN 狀態的迭代演化，而不是另一套與 IFN 競爭的結構。

### 9.3 HNM：聯合狀態空間

若同時考慮：

- 迭代時間 $t$ ；
- 分形地址 $\alpha$ ；
- MMR 局部狀態 $\mathcal{M}_{\alpha}^{(t)}$ ；

則聯合狀態可寫成：

$$
\mathcal{H}
=
\left\{
(t,\alpha,\mathcal{M}_{\alpha}^{(t)})
\right\}
$$

這可作為 HNM 的離散、可計算版本。

本文不直接宣稱它是黎曼流形，也不預設存在自然曲率、測地線或無限維流形結構。若未來需要使用流形語言，必須先定義：

- 拓撲；
- 度量；
- 局部座標；
- 可微結構；
- 距離與路由的關係。

---

## 十、可驗證執行與 MMR-Bench 的接合

### 10.1 IFN 執行證書

一次 IFN 執行可輸出：

$$
\mathcal{C}_{\mathrm{IFN}}
=
(
H_{\mathrm{input}},
H_{\mathrm{route}},
H_{\mathrm{state}},
H_{\mathrm{lineage}},
H_{\mathrm{decision}},
\Sigma
)
$$

其中：

- $H_{\mathrm{input}}$ ：輸入雜湊；
- $H_{\mathrm{route}}$ ：路由圖雜湊；
- $H_{\mathrm{state}}$ ：節點狀態摘要；
- $H_{\mathrm{lineage}}$ ：血緣摘要；
- $H_{\mathrm{decision}}$ ：展開、剪枝與停止決策摘要；
- $\Sigma$ ：簽章。

### 10.2 重播條件

重播至少驗證：

1. 相同輸入；
2. 相同模型與版本；
3. 相同路由規則；
4. 相同正規化；
5. 相同預算與停止條件；
6. 相同隨機種子，或明確記錄非確定性；
7. 相同證據與決策摘要。

### 10.3 不把一致性誤當成真理

即使兩個 IFN 後端輸出一致，也只能證明：

$$
\text{在已記錄條件下結果一致}
$$

不能直接證明：

$$
\text{結果符合外部世界真實意圖}
$$

因此 IFN 必須維持：

- 計算正確性；
- 路由正確性；
- 資料正確性；
- 任務意圖正確性；

四者的分離。

---

## 十一、研究問題與實驗路線

### 11.1 核心可否證問題

IFN 是否值得保留，不取決於名稱或幾何美感，而取決於以下問題：

1. IFN 路由是否能以次平方成本建立？
2. 層級路由是否比平面稀疏路由更有效？
3. IFN 是否能在相同計算預算下保存更多長距離資訊？
4. 路由錯誤是否會造成比 dense attention 更嚴重的不可恢復損失？
5. 自適應展開是否比固定層級分塊更穩定？
6. 血緣與證書成本是否可接受？
7. IFN 是否只在具有天然層級的任務上有效？
8. 九分支是否比其他分支數更好？

### 11.2 最小實驗階段

#### 階段 A：路由資料結構

比較：

- dense mask；
- Python 雙迴圈；
- trie；
- CSR／COO；
- block-sparse；
- GPU 原生稀疏 kernel。

量測：

- 建圖時間；
- 記憶體；
- 邊數；
- 更新成本；
- 不同 $n$ 與 $k$ 的 scaling。

#### 階段 B：合成結構任務

使用：

- 樹路徑查詢；
- 多層區域依賴；
- 括號匹配；
- 程式 AST；
- 章節—段落—句子檢索；
- 長距離指標追蹤。

比較：

- dense attention；
- local window；
- local + global；
- flat sparse；
- IFN hierarchical sparse。

#### 階段 C：IFN-Transformer

至少報告：

- wall-clock；
- kernel 利用率；
- 記憶體；
- perplexity／accuracy；
- 路由召回率；
- 長距離依賴召回；
- 不同深度與分支數；
- 路由錯誤敏感度；
- Amdahl 分解。

#### 階段 D：可驗證重播

測試：

- 路由篡改；
- 輸入篡改；
- 地址映射篡改；
- 停止條件篡改；
- 模型版本差異；
- 不同硬體的容差；
- 非確定性重播。

---

## 十二、理論邊界

本文明確不主張：

1. 所有高維資訊必然集中在可被 IFN 找出的低維流形；
2. 九宮格是唯一或普遍最優的局部結構；
3. 中心槽位自然保證收斂；
4. 無限地址表示等於實際無限維計算；
5. 任意概念都能唯一映射為 IFN 地址；
6. IFN 必然降低複雜度；
7. IFN 必然改善推理品質；
8. IFN-Transformer 必然優於 FlashAttention、Longformer、BigBird、Mamba 或其他架構；
9. 多跳稀疏路由天然保存長距離資訊；
10. 分形自相似會自動產生零樣本泛化。

本文只提出：

$$
\boxed{
\text{MMR 可作為局部計算語法，IFN 可作為其遞歸組合拓撲}
}
$$

這是一個可實作、可測試、可失敗的研究命題。

---

## 十三、概念貢獻

本文的核心貢獻不是「九宮格比 Transformer 更快」，而是建立了以下分層：

### 第一層：局部表示

$$
\text{MMR}
=
\text{內容}
+
\text{方向}
+
\text{區域}
+
\text{遍歷}
+
\text{血緣}
$$

### 第二層：遞歸結構

$$
\text{IFN}
=
\text{MMR 單元}
+
\text{分形地址}
+
\text{有限展開}
+
\text{多類路由}
$$

### 第三層：時間演化

$$
\text{IDN}
=
\text{IFN 狀態的迭代更新}
$$

### 第四層：有限工程後端

$$
\text{IFN-Transformer}
=
\text{IFN 路由圖}
\rightarrow
\text{稀疏注意力}
$$

### 第五層：可驗證執行

$$
\text{MMR-Bench／IFN Certificate}
=
\text{來源}
+
\text{路由}
+
\text{證據}
+
\text{決策}
+
\text{重播}
$$

這個分層避免把幾何隱喻、計算架構與效能結論混成同一個命題。

---

## 十四、結論

無限分形九宮格不應被理解為一張會無限展開的九宮格圖片，也不應被縮減成「按重要性排序 token」的稀疏注意力技巧。

本文重新提出：

$$
\boxed{
\text{IFN 是由 MMR 局部單元構成的、可無界定址但有限執行的遞歸計算拓撲}
}
$$

MMR 使每一個分形節點具有明確的內容、方向、區域、路徑、血緣、信心與成本；IFN 則使這些節點能被自相似地組合、按需展開、跨層連接、受限剪枝並形成可重播證據。

IFN 的研究價值不取決於它是否被稱為「新範式」，而取決於以下事實能否被實驗支持：

- 層級路由能否低成本建立；
- 分形地址能否帶來比平面稀疏更好的結構偏置；
- 路由與停止能否被驗證；
- 長距離訊息能否在有限路徑中保留；
- 相同精度下，計算與記憶體是否真正下降。

因此，本論文把 IFN 從一個宣言轉化為一個研究程序：

$$
\boxed{
\text{定義}
\rightarrow
\text{實作}
\rightarrow
\text{量測}
\rightarrow
\text{反例}
\rightarrow
\text{修正}
\rightarrow
\text{驗證}
}
$$

這不是對既有架構的勝利宣告，而是 IFN 第一次成為可以被工程實現、學術批判與獨立重播的計算對象。

---

## 附錄 A：最小 IFN 執行模型

```python
from dataclasses import dataclass, field
from typing import Any, Callable


Address = tuple[int, ...]


@dataclass
class MMRNode:
    address: Address
    state: Any
    direction_schema: dict[int, str]
    neighbors: dict[str, list[Address]] = field(default_factory=dict)
    lineage: list[dict[str, Any]] = field(default_factory=list)
    confidence: float = 1.0
    uncertainty: float = 0.0
    budget_used: float = 0.0


@dataclass
class IFNRuntime:
    nodes: dict[Address, MMRNode]
    max_depth: int
    max_budget: float
    utility_threshold: float

    def candidate_children(self, address: Address) -> list[Address]:
        if len(address) >= self.max_depth:
            return []
        return [address + (i,) for i in range(9)]

    def expand(
        self,
        address: Address,
        utility: Callable[[Address], float],
        make_node: Callable[[Address], MMRNode],
    ) -> list[Address]:
        activated: list[Address] = []

        for child in self.candidate_children(address):
            if utility(child) <= self.utility_threshold:
                continue

            node = make_node(child)
            if node.budget_used + self.total_budget() > self.max_budget:
                break

            self.nodes[child] = node
            activated.append(child)

        return activated

    def total_budget(self) -> float:
        return sum(node.budget_used for node in self.nodes.values())
```

此模型刻意不承諾：

- 九個子節點全部建立；
- 中心必然最重要；
- 地址自動具有語義；
- 路由必然低成本；
- 展開必然提升答案品質。

這些都必須由任務、路由器與實驗決定。

---

## 附錄 B：下一篇工程論文的建議名稱

**中文：**

《MMR-IFN Transformer：基於遞歸多向路由的層級稀疏注意力架構》

**英文：**

**MMR-IFN Transformer: Hierarchical Sparse Attention through Recursive Multidirectional Routing**

其任務不再是證明 IFN 本體，而是驗證：

1. MMR 路由能否有效編譯成稀疏 attention；
2. 路由建構能否真正低於 $O(n^2)$ ；
3. 分層稀疏是否優於平面稀疏；
4. 可驗證血緣是否能在合理成本內保留；
5. IFN 的優勢是否只存在於特定層級任務。
