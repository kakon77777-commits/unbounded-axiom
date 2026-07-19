# 認知解構學模組組合方法論 I  
## 全景—核心—過程—雙界四聯動框架

**英文名稱：Cognitive Deconstructionism Module Composition Methodology I: Panoramic–Core–Process–Boundary Framework**  
**簡稱：PCPB Framework**  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**文件性質：正式方法論／模組組合教學／操作協議**  
**版本：v1.0**  
**日期：2026-07-17**

---

## 摘要

《認知解構學》既有方法論已建立多個可獨立操作的認知模組，但過去主要聚焦於各模組的定義、內核、運行方式、適用場景與雙界約束，尚未正式建立「多模組如何共同工作」的組合方法論。這造成一項實際缺口：使用者可能知道每個模組是什麼，卻不知道應當先用哪一個、何時切換、如何交換中間結果、何時回退，以及如何避免模組彼此重複、互相抵消或共同放大偏誤。

本文建立《認知解構學》的第一套正式模組組合教學，並以四個方法的聯動作為標準案例：

1. **多維度超宏觀多面分析（MDHMA）**：建立全景候選因素空間；
2. **核心量化推理——關鍵影響鏈與領域人群型（CQR-IC）**：分配有限注意力並提取高影響節點；
3. **無限宏微觀過程敘述法（IMMPN）**：把因素與節點縫合為跨時間、跨尺度的因果過程；
4. **雙界約束（DBC）**：限制概念、證據、因果與預測的合法外延。

四者的基本聯動不是簡單相加，而是一個具備回退、重排與重展開能力的循環：

$$
\boxed{
\text{全景展開}
\rightarrow
\text{核心定核}
\rightarrow
\text{過程縫合}
\rightarrow
\text{雙界校驗}
\rightarrow
\text{回饋重算}
}
$$

本文進一步提出「模組接口契約」、「問題簽名」、「五種模組組合型態」、「回退條件」、「輸出強度階梯」與「最小可執行協議」，使《認知解構學》從模組集合升級為可編排、可審計、可教學、可由人類或 Agent 執行的認知系統。

**關鍵詞：** 認知解構學、模組組合、核心量化推理、雙界約束、MDHMA、IMMPN、關鍵影響鏈、領域人群分析、因果連續性、Agent 方法論

---

# 第一部　為什麼需要模組組合方法論？

## 一、擁有模組，不等於擁有系統

單一模組回答的是：

> 面對某種類型的認知困難，應採用什麼運算？

模組組合回答的則是：

> 面對一個同時包含多種類型困難的真實問題，應如何調度多個運算？

若缺乏組合方法，使用者容易出現以下問題：

- 對所有問題固定使用最熟悉的模組；
- 同時啟用大量模組，卻沒有先後順序；
- 不同模組反覆處理同一資料，造成資訊冗餘；
- 某一模組的輸出格式無法成為下一模組的輸入；
- 分析失敗時，不知道應回到哪個步驟；
- 結論很長，卻無法指出每一段由哪個模組產生；
- 模組名稱成為修辭，而非真正的運算單元。

因此，《認知解構學》不能只是一組方法的百科全書，而必須成為：

$$
\text{Module Set}
+
\text{Routing Policy}
+
\text{Interface Contract}
+
\text{Feedback Control}
$$

亦即：

$$
\boxed{
\text{認知解構學系統}
=
\text{模組}
+
\text{編排}
+
\text{接口}
+
\text{回饋}
}
$$

---

## 二、模組不是章節，而是算子

本文將每一個認知模組定義為算子：

$$
M_i:\mathcal X_i\rightarrow\mathcal Y_i
$$

其中：

- $\mathcal X_i$ ：模組可以接受的輸入狀態；
- $\mathcal Y_i$ ：模組完成後產生的輸出狀態；
- $M_i$ ：把前者轉換成後者的操作。

例如：

$$
\mathrm{MDHMA}:
\text{問題}
\rightarrow
\text{全景因素空間}
$$

$$
\mathrm{CQR\text{-}IC}:
\text{全景因素空間}
\rightarrow
\text{核心節點與影響鏈}
$$

$$
\mathrm{IMMPN}:
\text{核心節點與多尺度資料}
\rightarrow
\text{過程轉換鏈}
$$

$$
\mathrm{DBC}:
\text{概念與推論集合}
\rightarrow
\text{合法結論區、邊界區與排除區}
$$

模組組合因此可表示為算子複合：

$$
M_{4}\circ M_{3}\circ M_{2}\circ M_{1}
$$

但真實問題通常不是單向函數，故還需要：

$$
M_i
\rightleftarrows
M_j
$$

表示錯誤回退、權重更新與重新展開。

---

# 第二部　名稱消歧：兩種「核心量化推理」不可混同

## 三、既有名稱衝突

《認知解構學》既有文本中的「核心量化推理模組」主要處理：

- 抽象概念拆解；
- 變項定義；
- 結構映射；
- 隱性參數的代理量化；
- 語義張力場轉換。

本文所使用的「核心量化推理」則來自另一套較早的方法，其核心是：

- 核心人物或事件識別；
- 關鍵影響鏈追蹤；
- 言論與行動的結構化分析；
- 領域人群的廣域取樣；
- 個體訊號與群體趨勢的交叉校正；
- 對現實動態進行方向性預測。

兩者名稱相同，但運算對象不同。

為避免後續混淆，本文暫採以下區分：

### 1. 語義量化型核心量化推理

$$
\mathrm{CQR\text{-}S}
$$

其中 $S$ 表示 Semantic。

它處理：

$$
\text{抽象概念}
\rightarrow
\text{可比較結構}
$$

### 2. 影響鏈型核心量化推理

$$
\mathrm{CQR\text{-}IC}
$$

其中 $IC$ 表示 Influence Chain。

它處理：

$$
\text{現實因素與行動者}
\rightarrow
\text{核心節點、影響鏈與領域趨勢}
$$

本文四聯動框架中的核心量化推理，一律指：

$$
\boxed{\mathrm{CQR\text{-}IC}}
$$

未來若正式重新命名，可再另行修訂；在此之前，必須保留後綴以維持方法論可審計性。

---

# 第三部　模組組合的一般理論

## 四、問題簽名：先判定問題需要什麼運算

在調用模組前，應先建立問題簽名：

$$
\Sigma_Q
=
(O,T,S,D,U,R,C)
$$

其中：

- $O$ ：分析對象（Object）；
- $T$ ：時間結構（Time）；
- $S$ ：尺度層級（Scale）；
- $D$ ：資料狀態（Data）；
- $U$ ：不確定性（Uncertainty）；
- $R$ ：風險與後果（Risk）；
- $C$ ：資源約束（Constraint）。

問題簽名用來判定是否需要：

- 全景展開；
- 核心壓縮；
- 過程追蹤；
- 邊界限制；
- 模擬；
- 逆推；
- 語義重編；
- 多視角衝突。

例如，一個高風險、跨尺度、資料不完整且涉及多個行動者的問題，簽名可能是：

$$
\Sigma_Q
=
(\text{多主體},
\text{動態},
\text{跨尺度},
\text{異質資料},
\text{高不確定},
\text{高風險},
\text{有限時間})
$$

這類問題就適合啟動本文四聯動框架。

---

## 五、模組接口契約

每個模組必須具備一份接口契約：

$$
\Gamma(M)
=
(I,O,A,F,E,R)
$$

其中：

- $I$ ：允許輸入（Input）；
- $O$ ：標準輸出（Output）；
- $A$ ：核心假設（Assumptions）；
- $F$ ：失敗條件（Failure Conditions）；
- $E$ ：證據要求（Evidence Requirements）；
- $R$ ：回退路徑（Rollback Route）。

模組不能只說「我能做什麼」，還必須說：

> 什麼情況下，我的結果不能被信任？

例如 CQR-IC 的失敗條件包括：

- 核心人物只是媒體可見度高，實際決策權低；
- 公開言論與內部行動嚴重分離；
- 領域取樣過度同質；
- 代理指標沒有真正代表影響力；
- 將相關性誤認為控制力。

若觸發失敗條件，系統不得直接進入結論，而應返回 MDHMA 或補充證據。

---

## 六、五種模組組合型態

### 1. 串聯型

$$
M_1\rightarrow M_2\rightarrow M_3
$$

上一模組輸出直接成為下一模組輸入。

適用於：

- 任務步驟清楚；
- 各模組角色不重疊；
- 中間結果可標準化。

本文四聯動具有串聯骨架。

---

### 2. 並聯型

$$
Q
\rightarrow
\begin{cases}
M_1(Q)\\
M_2(Q)\\
M_3(Q)
\end{cases}
\rightarrow
\operatorname{Merge}
$$

不同模組獨立分析同一問題，再進行合併。

適用於：

- 需要多視角校正；
- 任一方法可能帶有偏誤；
- 需要比較不同推理路徑。

---

### 3. 嵌套型

$$
M_1\bigl(M_2(Q)\bigr)
$$

某模組在另一模組內部被局部調用。

例如 IMMPN 在追蹤某個尺度轉換時，可以局部調用 CQR-IC，判定該尺度中的關鍵節點。

---

### 4. 循環型

$$
M_1\rightarrow M_2\rightarrow M_3\rightarrow M_1'
$$

後續結果改寫前面的因素空間或權重。

本文四聯動的完整形態屬於循環型。

---

### 5. 約束型

$$
M_{\mathrm{generator}}
\xrightarrow{M_{\mathrm{constraint}}}
M_{\mathrm{valid}}
$$

一個模組生成候選解，另一個模組負責限制其合法範圍。

DBC 在本文中就是約束模組，而不是內容生成模組。

---

# 第四部　四個模組的正式定位

## 七、MDHMA：全景候選空間生成器

### 7.1 功能定位

MDHMA 的任務不是立即找出「最重要因素」，而是防止分析者過早刪除可能重要的變數。

其輸出為：

$$
\mathcal M_t
=
(F_t,P_t,\Sigma_t,\mathcal R_t,W_t)
$$

其中：

- $F_t$ ：候選因素集合；
- $P_t$ ：分析面集合；
- $\Sigma_t$ ：尺度集合；
- $\mathcal R_t$ ：因素交互網格；
- $W_t$ ：隨時間與語境變動的權重函數。

### 7.2 修正版核心原則

早期表述容易讓人誤以為所有因素必須永久保持相同權重。正式修正為：

> 所有因素具有平等的入場權，但不具有相等的當前權重。

形式為：

$$
\forall f_i\in F_t,
\qquad
\operatorname{Admit}(f_i)=1
$$

但：

$$
w_i(t,c)\neq w_j(t,c)
$$

MDHMA 的「無核心初始化」是反偏見操作，不是永恆權重規則。

### 7.3 標準輸出

MDHMA 至少輸出：

1. 因素清單；
2. 尺度清單；
3. 時間切片；
4. 交互關係；
5. 邊緣因素池；
6. 未知因素占位符；
7. 初始資料可信度；
8. 可能的非線性放大鏈。

### 7.4 停止條件

MDHMA 不可能真的列出宇宙中的所有因素，因此必須設置實用停止條件：

$$
\Delta F_k<\epsilon_F
$$

或：

$$
\Delta \operatorname{Coverage}_k<\epsilon_C
$$

表示新增一輪展開已不再顯著增加因素覆蓋率。

---

## 八、CQR-IC：有限注意力與核心影響鏈分配器

### 8.1 功能定位

CQR-IC 接受 MDHMA 的全景因素空間，並依照影響力、中心性、行動成本、訊息價值與不確定性分配分析資源。

它不是刪除非核心因素，而是建立兩層解析度：

$$
F_t=K_t\sqcup R_t
$$

其中：

- $K_t$ ：高解析核心集合；
- $R_t$ ：低解析殘餘因素池。

### 8.2 核心評分向量

對每個因素 $f_i$ 建立：

$$
\mathbf q_i(t)
=
(I_i,C_i,S_i,A_i,V_i,U_i,D_i)
$$

其中：

- $I_i$ ：直接影響力；
- $C_i$ ：網絡中心性；
- $S_i$ ：系統敏感度；
- $A_i$ ：行動成本或承諾強度；
- $V_i$ ：資訊價值；
- $U_i$ ：不確定度；
- $D_i$ ：領域偏離度。

其中「行動成本」特別重要。低成本言論容易受行銷動機影響；高成本行為通常更接近顯示性偏好。

### 8.3 雙軸結構

CQR-IC 必須同時運行兩條軸。

#### 關鍵影響鏈分析

$$
a_0
\rightarrow
a_1
\rightarrow
a_2
\rightarrow
\cdots
\rightarrow
o
$$

其中：

- $a_0$ ：表面核心人物或事件；
- $a_1,a_2$ ：直接與間接影響者；
- $o$ ：最終制度、政策、市場或行為輸出。

#### 領域人群分析

$$
G
=
\{g_1,g_2,\ldots,g_n\}
$$

觀察：

- 群體平均趨勢；
- 群體分散程度；
- 角色間差異；
- 異常個體；
- 跨組織同步偏移。

### 8.4 核心不是永久身份

若殘餘因素的權重上升：

$$
w_j(t+\Delta t)>\tau
$$

則：

$$
f_j\in R_t
\rightarrow
f_j\in K_{t+\Delta t}
$$

因此，核心是一個動態資源標記，而不是本體論地位。

---

## 九、IMMPN：多尺度過程縫合器

### 9.1 功能定位

MDHMA 告訴我們可能有哪些因素，CQR-IC 告訴我們應優先關注哪些因素，但它們仍可能停留在靜態節點圖。

IMMPN 負責回答：

> 這些因素如何一步步改變系統？

### 9.2 過程單元

每個過程單元表示為：

$$
\Pi_k
=
(S_k,A_k,M_k,S_{k+1},E_k,U_k)
$$

其中：

- $S_k$ ：前狀態；
- $A_k$ ：作用者或作用因素；
- $M_k$ ：轉換機制；
- $S_{k+1}$ ：後狀態；
- $E_k$ ：證據；
- $U_k$ ：不確定性。

### 9.3 跨尺度轉換

修正版跨尺度形式為：

$$
S_{\sigma+1,t+\Delta t}
=
E_\sigma
\left(
S_{\sigma,t},
I_{\sigma,t},
C_{\sigma+1,t};
\theta_\sigma
\right)
+
\varepsilon_\sigma
$$

其中：

- $I_{\sigma,t}$ ：同尺度內部互動；
- $C_{\sigma+1,t}$ ：上層對下層的反向約束；
- $\theta_\sigma$ ：已知轉換規則；
- $\varepsilon_\sigma$ ：尚未解釋的因果殘差。

### 9.4 從「不允許空缺」修正為「不允許未標記空缺」

早期強式敘述要求高層現象被低層狀態完全解釋。作為理想目標可以保留，但在現實研究中容易製造偽完整性。

正式修正為：

> IMMPN 不要求分析者假裝知道所有過程；它要求所有不知道的過程都被明確標記。

因此：

$$
\varepsilon_\sigma\neq 0
$$

不是方法失敗。

真正的方法失敗是：

$$
\varepsilon_\sigma\neq 0
\quad\land\quad
\operatorname{Unmarked}(\varepsilon_\sigma)
$$

### 9.5 雙向尺度因果

IMMPN 不採取純粹單向還原論。

完整結構包括：

$$
\text{微觀}
\rightarrow
\text{中觀}
\rightarrow
\text{宏觀}
$$

以及：

$$
\text{宏觀制度}
\rightarrow
\text{中觀組織}
\rightarrow
\text{微觀行為}
$$

前者是生成，後者是約束。

---

## 十、DBC：語義、證據、因果與預測的合法性防火牆

### 10.1 功能定位

DBC 不是用來生成更豐富的解釋，而是防止解釋越過證據與定義所允許的範圍。

對概念 $X$ ，建立：

$$
D(X)
=
(N_X,E_X,B_X)
$$

其中：

- $N_X$ ：必要屬性；
- $E_X$ ：排除案例；
- $B_X$ ：邊界案例。

其外延為：

$$
\operatorname{Ext}(X)
=
\left(
\bigcap_{p\in N_X}
\operatorname{Satisfy}(p)
\right)
\setminus
\left(
\bigcup_{e\in E_X}
\operatorname{Match}(e)
\right)
$$

### 10.2 三區模型

$$
\mathcal X
=
\mathcal X_{\mathrm{in}}
\sqcup
\mathcal X_{\mathrm{boundary}}
\sqcup
\mathcal X_{\mathrm{out}}
$$

其中：

- $\mathcal X_{\mathrm{in}}$ ：明確屬於；
- $\mathcal X_{\mathrm{boundary}}$ ：需個案判斷；
- $\mathcal X_{\mathrm{out}}$ ：明確排除。

### 10.3 四種雙界

#### 語義雙界

至少是什麼，絕對不是什麼。

#### 證據雙界

最低需要哪些證據；哪些資料不足以支持該結論。

#### 因果雙界

哪些中介機制不可缺；哪些只能稱為相關。

#### 預測雙界

最多可以預測到什麼強度；哪些敘述超出資料。

### 10.4 結論強度上限

對結論 $H$ 定義：

$$
C_H
=
\operatorname{MaxClaimStrength}(E_H)
$$

輸出不得超過：

$$
\operatorname{Strength}(H)\leq C_H
$$

---

# 第五部　四聯動的正式運行協議

## 十一、總體運行式

四聯動框架可表示為：

$$
Q
\xrightarrow{\mathrm{MDHMA}}
\mathcal M_t
\xrightarrow{\mathrm{CQR\text{-}IC}}
(K_t,R_t,\mathcal G_t)
\xrightarrow{\mathrm{IMMPN}}
\Pi_t
\xrightarrow{\mathrm{DBC}}
H_t
$$

其中：

- $\mathcal M_t$ ：全景模型；
- $K_t$ ：核心因素；
- $R_t$ ：殘餘因素池；
- $\mathcal G_t$ ：影響網絡與群體校正；
- $\Pi_t$ ：過程鏈；
- $H_t$ ：受約束結論。

但完整系統必須加入回饋：

$$
\boxed{
\mathrm{MDHMA}
\rightleftarrows
\mathrm{CQR\text{-}IC}
\rightleftarrows
\mathrm{IMMPN}
\rightleftarrows
\mathrm{DBC}
}
$$

---

## 十二、十二步標準操作流程

### Step 1：建立問題簽名

記錄：

- 問題對象；
- 時間範圍；
- 空間範圍；
- 尺度；
- 可用資料；
- 資料缺口；
- 錯誤成本；
- 所需輸出。

### Step 2：定義初始雙界

在分析開始前，先說明：

- 本次研究至少要回答什麼；
- 本次研究不企圖證明什麼；
- 哪些概念容易混淆；
- 哪些情況必須保留未知。

這稱為**前置雙界**。

### Step 3：MDHMA 全維展開

建立因素、行動者、制度、尺度、時間切片、非線性交互、邊緣因素池與未知占位符。

### Step 4：來源分層

$$
E
=
E_{\mathrm{primary}}
\sqcup
E_{\mathrm{secondary}}
\sqcup
E_{\mathrm{inference}}
\sqcup
E_{\mathrm{unknown}}
$$

禁止把推論資料偽裝成一手證據。

### Step 5：CQR-IC 核心分配

選出高權力節點、高資訊節點、高成本行為、高異常訊號、關鍵中介者與可能的反向控制節點。

### Step 6：建立關鍵影響鏈

$$
\text{表面節點}
\rightarrow
\text{直接影響}
\rightarrow
\text{間接影響}
\rightarrow
\text{制度傳導}
\rightarrow
\text{結果}
$$

若某一段沒有證據，不得直接跨越。

### Step 7：領域人群校正

比較同類公司、同類領導者、不同角色、不同國家、不同時間、多數趨勢與少數異動。

### Step 8：IMMPN 過程縫合

$$
S_0
\xrightarrow{M_0}
S_1
\xrightarrow{M_1}
S_2
\rightarrow\cdots\rightarrow
S_n
$$

每一段標記作用者、機制、證據、時間延遲、尺度變換、反饋與因果殘差。

### Step 9：建立替代過程鏈

$$
\Pi^{(1)},\Pi^{(2)},\ldots,\Pi^{(m)}
$$

不可只建立最符合原先立場的一條故事。

### Step 10：DBC 四重校驗

逐一檢查：

1. 語義是否合法；
2. 證據是否足夠；
3. 因果是否連續；
4. 預測是否超限。

### Step 11：輸出強度分級

$$
L_0=\text{未知}
$$

$$
L_1=\text{可觀察相關}
$$

$$
L_2=\text{方向性更新}
$$

$$
L_3=\text{競爭解釋中較佳}
$$

$$
L_4=\text{高可信機制}
$$

$$
L_5=\text{形式或實證確認}
$$

禁止從 $L_1$ 直接跳到 $L_4$ 。

### Step 12：回饋重算

根據殘差與邊界案例，決定返回 MDHMA、CQR-IC、IMMPN 或由 DBC 降低結論強度。

---

# 第六部　回退機制

## 十三、四種主要回退條件

### 1. 因素遺漏回退

若：

$$
\varepsilon_\sigma>\eta
$$

表示過程殘差過大，返回 MDHMA。

### 2. 核心誤判回退

若核心節點無法解釋結果，而邊緣因素持續升權：

$$
w(r_j)>w(k_i)
$$

則返回 CQR-IC，重新排序。

### 3. 因果斷鏈回退

若：

$$
S_k
\not\xrightarrow{\text{known mechanism}}
S_{k+1}
$$

則返回 IMMPN 補充機制，或把該段標記為未知。

### 4. 結論超限回退

若：

$$
\operatorname{Strength}(H)>C_H
$$

則由 DBC 強制降級。

---

## 十四、停止條件

四聯動不應無限分析。可在以下條件同時成立時停止：

1. 新增因素的邊際資訊量低於門檻；
2. 核心集合在多輪中保持穩定；
3. 主要過程鏈的殘差已被標記；
4. 替代解釋已被比較；
5. 結論強度未超過證據；
6. 後續分析成本高於預期資訊收益。

形式上：

$$
\Delta I<\epsilon_I
\quad\land\quad
\Delta K<\epsilon_K
\quad\land\quad
\operatorname{Bounded}(H)=1
$$

---

# 第七部　最小可執行模板

## 十五、問題卡

```text
問題：
時間範圍：
空間範圍：
分析尺度：
決策用途：
錯誤成本：
現有資料：
主要未知：
本研究不企圖證明：
```

## 十六、MDHMA 因素表

```text
因素名稱：
所屬尺度：
所屬分析面：
目前權重：
資料來源：
與其他因素的交互：
可能放大條件：
是否暫列邊緣因素：
```

## 十七、CQR-IC 核心節點表

```text
節點：
角色：
直接權力：
網絡中心性：
實際行動成本：
資訊接近度：
言行一致性：
群體偏離度：
不確定度：
核心／殘餘：
```

## 十八、IMMPN 過程鏈表

```text
前狀態：
作用者／因素：
作用機制：
後狀態：
時間延遲：
尺度變換：
支持證據：
替代機制：
因果殘差：
```

## 十九、DBC 結論卡

```text
候選結論：
必要證據：
排除條件：
邊界案例：
目前證據：
最大允許強度：
反證條件：
最終狀態：
```

---

# 第八部　標準教學案例：前沿 AI 公司與 AGI 訊號

## 二十、問題設定

問題不是：

> AGI 是否已經存在？

而是：

> 前沿 AI 公司領導者的高信心言論、實際限制行為與監管主張，是否支持我們提高對內部能力非線性增長的信念？

這個問題本身已由 DBC 限定：研究的是方向性更新，不是 AGI 存在證明。

## 二十一、MDHMA 展開

納入模型能力、領導者言論、公司競爭、投資與估值、算力與能源、政府關係、國家安全、法律責任、監管俘獲、企業資產保護、公開模型與內部模型差距、Agent 時代資料、媒體放大、個人性格與地緣政治競爭。

## 二十二、CQR-IC 定核

優先分析掌握內部資訊的公司領導者、能改變發布政策的人、具有政府接口的人、多家競爭公司之間同步出現的訊號，以及延後發布、外部測試、政府提前存取等高成本行為。

建立：

$$
E=
E_{\mathrm{speech}}
+
E_{\mathrm{costly\ action}}
+
E_{\mathrm{institution}}
$$

其中：

$$
\operatorname{Info}(E_{\mathrm{costly\ action}})
>
\operatorname{Info}(E_{\mathrm{speech}})
$$

## 二十三、IMMPN 縫合

候選過程鏈之一：

$$
\text{內部能力觀察}
\rightarrow
\text{領導者信念更新}
\rightarrow
\text{公開言論}
\rightarrow
\text{公司政策}
\rightarrow
\text{政府介入}
\rightarrow
\text{法律制度}
\rightarrow
\text{責任共同化}
\rightarrow
\text{資產保護}
$$

競爭過程鏈則可能是：

$$
\text{資本競爭}
\rightarrow
\text{AGI 敘事}
\rightarrow
\text{政策資源}
\rightarrow
\text{監管門檻}
\rightarrow
\text{市場集中}
$$

兩條鏈可以同時成立，不必單選。

## 二十四、DBC 限制

至少可以說：

> 言論、昂貴行為與制度主張的同步收斂，支持對內部能力加速進行方向性正向更新。

不能說：

> 公開訊號已證明 AGI 存在。

也不能說：

> 所有監管行動都只是找替罪羊。

邊界區包括真實風險、行銷、監管護城河、國家安全、責任分散與企業資產保護。

最終輸出位於：

$$
L_2\sim L_3
$$

---

# 第九部　常見錯誤

## 二十五、把 MDHMA 變成無限列清單

MDHMA 的目的不是追求文字上的「全部」，而是建立不因先驗偏見而永久排除因素的候選空間。

## 二十六、把 CQR-IC 變成名人分析

$$
\text{Visibility}
\neq
\text{Control}
\neq
\text{Information Access}
$$

## 二十七、把過程鏈寫成故事

每段必須包含：

$$
\text{機制}
+
\text{證據}
+
\text{替代解釋}
+
\text{殘差}
$$

## 二十八、把雙界約束變成保守主義

DBC 允許大膽假設，但必須同時標明假設、證據、邊界與反證條件。

## 二十九、四個模組一次全部開滿

應遵守：

$$
\text{最低充分模組原則}
$$

只啟用完成問題所需的最低模組集合。

---

# 第十部　教學分級

## 三十、初階：固定流水線

$$
\mathrm{MDHMA}
\rightarrow
\mathrm{CQR\text{-}IC}
\rightarrow
\mathrm{IMMPN}
\rightarrow
\mathrm{DBC}
$$

## 三十一、中階：回退與替代鏈

中階使用者必須建立至少兩條競爭過程鏈、保留殘餘因素池、根據因果殘差返回重算，並對結論進行強度分級。

## 三十二、高階：動態模組編排

高階使用者或 Agent 應依問題簽名自動決定模組順序、並行、嵌套、約束、終止與擴展。

$$
\mathcal R:
\Sigma_Q
\rightarrow
\mathcal P(M)
$$

其中 $\mathcal P(M)$ 是模組集合的冪集。

---

# 第十一部　推廣至整個認知解構學

## 三十三、模組組合的五種角色

1. **生成模組**：產生新概念、新模型、新假設；
2. **展開模組**：擴大因素、語境、尺度或路徑；
3. **壓縮模組**：提取核心、建立優先級；
4. **轉換模組**：跨語義、跨尺度、跨狀態映射；
5. **約束模組**：限制定義、證據與結論強度。

成熟的模組組合通常至少包含：

$$
\text{生成／展開}
+
\text{壓縮}
+
\text{轉換}
+
\text{約束}
$$

## 三十四、組合不是把名稱相加

真正的模組組合必須滿足：

1. 功能互補；
2. 接口相容；
3. 錯誤可定位；
4. 回退可執行。

若不滿足，只能稱為方法並列，不能稱為模組組合。

---

# 第十二部　最小公理集

## 公理一：問題—推理結構同構

$$
\operatorname{Structure}(\text{Reasoning})
\cong
\operatorname{Structure}(\text{Problem})
$$

## 公理二：因素平等入場，不平等計算

$$
\operatorname{Admit}(f_i)=1
$$

但：

$$
w_i(t,c)\neq w_j(t,c)
$$

## 公理三：核心是資源配置，不是本體身份

$$
f_i\in K_t
$$

只表示當前應給予高解析度。

## 公理四：任何跨狀態推論都必須具有機制或殘差標記

$$
S_k\rightarrow S_{k+1}
$$

必須附帶：

$$
M_k
\quad\text{或}\quad
\varepsilon_k
$$

## 公理五：結論強度不得超過證據上限

$$
\operatorname{Strength}(H)
\leq
\operatorname{MaxClaimStrength}(E)
$$

## 公理六：模組輸出必須可被後續模組審計

任何中間結果都應保留來源、假設、操作、不確定性、版本與回退點。

## 公理七：模組組合必須允許失敗

一套不允許輸出「未知」的方法，不是完整方法，而是結論生成器。

---

# 結論

本文完成了《認知解構學》由「多模組集合」走向「模組可組合系統」的第一步。

四聯動框架的核心不是同時使用四個名稱，而是建立四種互補運動：

$$
\boxed{
\text{MDHMA 建立可見世界}
}
$$

$$
\boxed{
\text{CQR-IC 分配有限注意力}
}
$$

$$
\boxed{
\text{IMMPN 重建世界如何變成現在}
}
$$

$$
\boxed{
\text{DBC 限制我們可以說到哪裡}
}
$$

四者共同形成：

$$
\boxed{
\text{先全觀，再定核；沿核追變，以界止言；若鏈有缺，返觀重算。}
}
$$

這套方法同時適用於政治與國際關係、AI 產業觀察、商業戰略、科技預測、社會運動、金融風險、複雜理論分析、Agent 自動研究、多模型協作與高風險決策。

更重要的是，它提供了一個可推廣原型：未來《認知解構學》的其他模組，不再只需要單獨定義，而應逐步建立可組合的接口、角色、順序、失敗條件與回退路徑。

從此，認知解構學不再只是「有哪些方法」，而開始回答：

> **這些方法如何共同成為一個可以運行的認知系統？**

---

# 附錄 A　四聯動速查表

| 階段 | 模組 | 核心問題 | 標準輸出 | 主要風險 |
|---|---|---|---|---|
| 全景 | MDHMA | 有哪些因素可能重要？ | 因素空間、尺度、交互網格 | 無限展開、資料冗餘 |
| 定核 | CQR-IC | 現在應優先看誰與什麼？ | 核心節點、影響鏈、群體校正 | 名人偏誤、偽量化 |
| 追變 | IMMPN | 系統如何一步步改變？ | 狀態鏈、機制、尺度轉換、殘差 | 故事化、因果跳躍 |
| 限言 | DBC | 證據允許我們說到哪裡？ | 內部區、邊界區、排除區、結論強度 | 過度保守或錯誤封閉 |

---

# 附錄 B　Agent 執行偽代碼

```python
def run_pcpb(problem):
    signature = build_problem_signature(problem)
    pre_boundary = define_initial_boundaries(signature)

    panorama = mdhma_expand(
        problem=problem,
        preserve_residual_factors=True,
        mark_unknowns=True
    )

    core_map = cqr_ic_prioritize(
        panorama=panorama,
        use_influence_chain=True,
        use_domain_population=True,
        preserve_residual_pool=True
    )

    process_models = immpn_stitch(
        core_map=core_map,
        include_cross_scale_links=True,
        mark_causal_residuals=True,
        generate_alternatives=True
    )

    bounded_results = dbc_validate(
        process_models=process_models,
        semantic_boundary=True,
        evidence_boundary=True,
        causal_boundary=True,
        prediction_boundary=True
    )

    while bounded_results.requires_revision:
        route = bounded_results.rollback_route

        if route == "MDHMA":
            panorama = mdhma_expand_again(panorama)
        elif route == "CQR-IC":
            core_map = reprioritize(core_map, panorama)
        elif route == "IMMPN":
            process_models = repair_process_gaps(process_models)
        elif route == "DBC":
            bounded_results = downgrade_claim_strength(bounded_results)
        else:
            break

        bounded_results = rerun_downstream_modules(
            panorama, core_map, process_models
        )

    return bounded_results
```

---

# 附錄 C　內部來源文件

1. 《核心量化推理》
2. 《核心量化推理：基於關鍵影響鏈與領域人群的雙重分析方法》
3. 《認知解構學正式定義方法論 2.0》
4. 《認知解構學核心概念版（2.0 版草稿）》
5. 《哲學重構工程學：雙界約束與開源重譯協議修訂版》
6. 《認知解構學 2.0——思維升級手冊》

---

# 版本說明

**v1.0：**

- 首次建立認知解構學的正式模組組合方法論；
- 區分 CQR-S 與 CQR-IC；
- 建立問題簽名與模組接口契約；
- 定義五種模組組合型態；
- 正式化 MDHMA、CQR-IC、IMMPN、DBC 四聯動；
- 加入回退機制、停止條件、結論強度階梯；
- 提供人類教學模板與 Agent 執行偽代碼。
