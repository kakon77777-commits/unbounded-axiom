
**政治系統分析的形式化公理框架：從第一性原理到結構定理**

**作者**：**Neo.K (****許筌崴) & Theia**

**機構**：一言諾科技有限公司（EveMissLab），台灣

**關鍵詞**：公理化政治理論、形式系統、權力結構、狀態轉換、數學社會學、符號分析

**分類號**：JEL D70, D72, C60; AMS 91D10, 91D30

----------

**摘要**

本文提出一個完整的公理化框架，從第一性原理分析政治系統，不依賴規範性假設或特定意識形態立場。通過將權力主體（<![if !msEquation]>  <![endif]>）、行動者集合（<![if !msEquation]>  <![endif]>）、系統狀態（<![if !msEquation]>  <![endif]>）與轉換操作（<![if !msEquation]>  <![endif]>）形式化為基本對象，我們推導出一組核心定理，用以描述狀態轉移、損失函數、純化度量與因果歸屬。本框架引入可測量的量：損失率（<![if !msEquation]>  <![endif]>）、純化係數（<![if !msEquation]>  <![endif]>）、路徑效率（<![if !msEquation]>  <![endif]>）與資源不平等度（<![if !msEquation]>  <![endif]>），這些量可從可觀測的歷史數據中計算。我們證明了若干分類定理，僅基於這些度量即可區分優化驅動型、清洗驅動型、重分配驅動型與破壞型轉換。該系統價值中立、可證偽，且普遍適用於任何政治或組織結構。我們論證傳統政治學概念（如民主和平論、寡頭鐵律、中等收入陷阱）作為我們公理的自然推論出現，而非獨立假設。本研究確立政治符號學作為一門嚴格的數學學科，並為歷史與當代政治現象的定量、理論驅動分析提供基礎。

**重要性陳述**：通過在類似幾何學或概率論的公理基礎上構建政治分析，本框架能夠在不需要主觀判斷或意識形態前提的情況下，對權力動態做出客觀、可證偽的預測。所有結論皆從可觀測數據與形式邏輯演繹得出。

----------

**1.** **引言**

**1.1** **研究動機**

政治學長期面臨規範理論與經驗觀察之間的張力。現有框架常將價值判斷（何為_應然_）嵌入描述性主張（何為_實然_）之中，使得分析結論難以與意識形態承諾分離。此外，許多政治理論以自然語言表述，語義模糊，限制了預測能力與可檢驗性。

我們提出一種不同的進路：**從公理化第一性原理構建政治分析**，類似歐幾里得幾何學從公理構建或概率論從柯爾莫哥洛夫公理構建的方式[1]。我們的目標不是規定政治系統_應該_如何運作，而是創建一種形式語言來描述它們_實際上_如何運作，並具有足夠精確度以實現：

1.  **客觀分類**：基於可測量數據的政治轉換分類
2.  **可證偽預測**：關於系統動力學的可檢驗預測
3.  **演繹推導**：從基本原理推導已知政治現象
4.  **普遍適用性**：跨越文化、時代與政治意識形態

**1.2** **既有研究與局限**

政治分析的形式化進路有悠久歷史：

-   **博弈論模型**[2,3]聚焦於策略互動，但常假設具有已知偏好的理性行動者
-   **社會選擇理論**[4,5]公理化投票與聚合，但主要處理偏好結構
-   **複雜系統進路**[6,7]建模湧現現象，但缺乏公理基礎
-   **比較政治學**[8]使用難以形式化的定性框架

儘管這些進路各有價值，但它們要麼： (a) 處理特定子問題（投票、議價）而非一般政治動力學(b) 依賴強假設（理性、完全信息）(c) 缺乏跨越狀態轉換、資源流動與權力歸屬的統一公理結構

**本文貢獻**在於提供一個_完整_的公理系統，該系統：

-   僅需最小假設（行動者、狀態、轉換的存在性）
-   從基本元素推導可測量量
-   證明劃分所有可能轉換空間的分類定理
-   將現有理論作為特例納入

**1.3** **論文結構**

§2 定義基本對象與測量函數§3 陳述五條核心公理§4 推導關於目標推斷、純化與因果歸屬的基本定理§5 引入複合度量與分類方案§6 展示對抽象案例研究的應用§7 討論與既有政治理論的聯繫§8 結論與未來研究方向

----------

**2.** **預備知識：基本對象與測量**

**2.1** **本體論**

我們定義四種基本類型：

**定義2.1**（權力主體） *權力主體* <![if !msEquation]>  <![endif]>是能夠發起狀態轉換的決策實體。<![if !msEquation]>  <![endif]>  是所有此類實體的空間。

*註*：<![if !msEquation]>  <![endif]>  可以是個人、委員會、政黨或任何決策單位。我們不對 <![if !msEquation]>  <![endif]>的內部結構做假設。

----------

**定義2.2**（行動者集合） *行動者集合* <![if !msEquation]>  <![endif]>，其中 <![if !msEquation]>  <![endif]>是參與系統的個體集合。<![if !msEquation]>  <![endif]>  表示基數。

----------

**定義2.3**（系統狀態） *狀態* <![if !msEquation]>  <![endif]>編碼：

-   行動者配置：<![if !msEquation]>  <![endif]>
-   資源分佈：<![if !msEquation]>  <![endif]>
-   控制結構：<![if !msEquation]>  <![endif]>

其中 <![if !msEquation]>  <![endif]>是決策空間，<![if !msEquation]>  <![endif]>  表示行動者 <![if !msEquation]>  <![endif]>對決策 <![if !msEquation]>  <![endif]>的影響力。

----------

**定義2.4**（轉換操作） *轉換* <![if !msEquation]>  <![endif]>是狀態間的映射，記為：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

我們記：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

----------

**2.2** **子集定義**

**定義2.5**（存活子集）

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

**定義2.6**（損失子集）

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

**定義2.7**（忠誠子集）

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

滿足特定控制標準 <![if !msEquation]>  <![endif]>的行動者子集（例如與 <![if !msEquation]>  <![endif]>目標一致）。

----------

**2.3** **測量函數**

**定義2.8**（損失率）

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

----------

**定義2.9**（純化係數）

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

----------

**定義2.10**（路徑效率）  
設 <![if !msEquation]>  <![endif]>為狀態空間上的度量（例如物理距離、時間、資源成本）。定義：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

其中 <![if !msEquation]>  <![endif]>是最短路徑，<![if !msEquation]>  <![endif]>  是 <![if !msEquation]>  <![endif]>實際採取的路徑。

----------

**定義2.11**（資源不平等度） 設 <![if !msEquation]>  <![endif]>為時刻 <![if !msEquation]>  <![endif]>對行動者 <![if !msEquation]>  <![endif]>的資源分配。定義：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

這是變異係數，一種尺度不變的不平等度量。

----------

**3.** **公理基礎**

我們現在陳述五條核心公理。這些公理設計為：

-   **最小性**：僅包含必要假設
-   **經驗基礎**：與可觀測政治系統一致
-   **非規範性**：不嵌入價值判斷

----------

**公理A1****（狀態可達性）**

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

_解釋_：任何狀態都可以通過某個轉換序列從任何其他狀態到達。這排除了「禁止」狀態，但不對路徑長度或代價施加約束。

----------

**公理A2****（資源守恆）**

在封閉系統中：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

_解釋_：資源可以重新分配但不能創造或毀滅。（對開放系統可以放寬為近似守恆。）

----------

**公理A3****（目標導向行為）**

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

*解釋*：<![if !msEquation]>  <![endif]>  優化*某個*目標函數 <![if !msEquation]>  <![endif]>，即使 <![if !msEquation]>  <![endif]>不可觀測。我們不假設 <![if !msEquation]>  <![endif]>是什麼——只假設它存在並指導 <![if !msEquation]>  <![endif]>的選擇。

**關鍵點**：<![if !msEquation]>  <![endif]>  不必與公開陳述的目標一致。

----------

**公理A4****（多路徑存在性）**

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

其中 <![if !msEquation]>  <![endif]>表示狀態度量中的 <![if !msEquation]>  <![endif]>-鄰域。

_解釋_：達成近似相同結果總是有多種方式。這些方式之間的選擇揭示了隱藏目標的資訊。

----------

**公理A5****（觀測可追溯性）**

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

*解釋*：轉換留下可觀測痕跡。即使 <![if !msEquation]>  <![endif]>的內部推理被隱藏，我們仍可測量結果。

----------

**4.** **核心定理**

我們現在推導主要理論結果。

----------

**定理4.1****（目標識別定理）**

**陳述**：  
假設 <![if !msEquation]>  <![endif]>滿足：

1.  <![if !msEquation]>  <![endif]>（結果相似）
2.  <![if !msEquation]>  <![endif]>，其中 <![if !msEquation]>  <![endif]>（顯著更高的損失）
3.  <![if !msEquation]>  <![endif]>對 <![if !msEquation]>  <![endif]>均可行

則存在隱藏目標 <![if !msEquation]>  <![endif]>使得：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

**證明思路**：  
由公理A3，<![if !msEquation]>  <![endif]>  選擇 <![if !msEquation]>  <![endif]>。由於 <![if !msEquation]>  <![endif]>在可觀測損失更高的情況下選擇了 <![if !msEquation]>  <![endif]>而非 <![if !msEquation]>  <![endif]>，且結果相似，因此該決策無法用表面目標（達到 <![if !msEquation]>  <![endif]>）解釋。故 <![if !msEquation]>  <![endif]>優化了不同的函數 <![if !msEquation]>  <![endif]>，對於該函數 <![if !msEquation]>  <![endif]>得分更高。<![if !msEquation]>  <![endif]>

**推論4.1.1**：當 <![if !msEquation]>  <![endif]>很大時，偏離信號表明強烈的隱藏目標。

----------

**定理4.2****（純化定理）**

**陳述**：  
設 <![if !msEquation]>  <![endif]>為閾值。若：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

則 <![if !msEquation]>  <![endif]>的主要功能是*行動者子集選擇*而非狀態轉移。

**證明思路**：  
高 <![if !msEquation]>  <![endif]>意味著大規模移除行動者。高 <![if !msEquation]>  <![endif]>意味著存活者相對於控制標準 <![if !msEquation]>  <![endif]>高度同質。若目標僅為到達 <![if !msEquation]>  <![endif]>，低損失路徑即可滿足（公理A4）。高損失與高純化的結合表明基於 <![if !msEquation]>  <![endif]>的系統性篩選。<![if !msEquation]>  <![endif]>

**註**：典型閾值為 <![if !msEquation]>  <![endif]>。

----------

**定理4.3****（因果歸屬定理）**

**陳述**：  
假設兩個轉換 <![if !msEquation]>  <![endif]>依次發生，分別由權力主體 <![if !msEquation]>  <![endif]>主導。若：

<![if !msEquation]>  
<![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

則存在*歸屬不對稱*：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

其中 <![if !msEquation]>  <![endif]>測量問責性。

**證明思路**：  
根據假設，相同的績效度量（<![if !msEquation]>  <![endif]>）導致不同後果。由於 <![if !msEquation]>  <![endif]>，<![if !msEquation]>  <![endif]>  下的客觀績效更差。缺乏懲罰意味著問責性不僅是 <![if !msEquation]>  <![endif]>的函數，而是權力結構的函數。<![if !msEquation]>  <![endif]>  已將自己與歸屬機制隔離。<![if !msEquation]>  <![endif]>

**推論4.3.1**：不對稱歸屬是權力鞏固的標誌。

----------

**定理4.4****（資源流向定理）**

**陳述**：  
若 <![if !msEquation]>  <![endif]>在 <![if !msEquation]>  <![endif]>上單調遞增，且存在特權子集 <![if !msEquation]>  <![endif]>使得：

<![if !msEquation]>  
<![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

則資源分配優先級為：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

**證明思路**：  
不平等上升（<![if !msEquation]>  <![endif]>）伴隨頂層資源增長和底層損失，意味著重分配有利於 <![if !msEquation]>  <![endif]>，即使以他人生存為代價。由公理A2（守恆），流向 <![if !msEquation]>  <![endif]>的資源從 <![if !msEquation]>  <![endif]>轉移而來。儘管 <![if !msEquation]>  <![endif]>有資源，仍發生損失，證明了分配優先級。<![if !msEquation]>  <![endif]>

----------

**5.** **分類與複合度量**

**5.1** **複合度量**

**定義5.1**（清洗指數）

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

_解釋_：同時高損失與高純化。

----------

**定義5.2**（目標偏離度）  
對於 <![if !msEquation]>  <![endif]>的轉換 <![if !msEquation]>  <![endif]>：

<![if !msEquation]>  <![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

測量 <![if !msEquation]>  <![endif]>在陳述目標上表現差多少。

----------

**定義5.3**（系統性操作指標）  
$$\Xi(T) := \begin{cases} 1 & \text{若 } L(T) > 0.5 \land \phi(T) > 0.8 \land \eta(T) < 0.3 \ 0 & \text{否則} \end{cases}$$

「明顯系統性」操作的二元標記。

----------

**5.2** **轉換分類學**

**定理5.1**（分類定理）  
任何轉換 <![if !msEquation]>  <![endif]>可根據其 <![if !msEquation]>  <![endif]>特徵分為四類：

**類型I****（優化型）**：<![if !msEquation]>  <![endif]>  
**類型II****（清洗型）**：<![if !msEquation]>  <![endif]>  無關  
**類型III****（重分配型）**：<![if !msEquation]>  <![endif]>  與資源五分位相關  
**類型IV****（破壞型）**：<![if !msEquation]>  <![endif]>  大

**證明**：通過劃分度量空間並對每個區域應用定理4.1-4.4。<![if !msEquation]>  <![endif]>

----------

**6.** **應用：抽象案例研究**

我們在風格化範例上展示該框架。所有數據均為假設但具代表性。

**6.1** **案例研究A****：長距離遷移**

**情境**：<![if !msEquation]>  <![endif]>  個行動者從區域 <![if !msEquation]>  <![endif]>遷往 <![if !msEquation]>  <![endif]>。

**數據**：

-   直接路徑：<![if !msEquation]>  <![endif]>  公里
-   實際路徑：<![if !msEquation]>  <![endif]>  公里
-   存活者：<![if !msEquation]>  <![endif]>
-   歷史記錄顯示 <![if !msEquation]>  <![endif]>

**計算**：

<![if !msEquation]>  
  
<![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

**分析**：

-   定理4.2適用（<![if !msEquation]>  <![endif]>）：主要功能是純化
-   定理4.1適用（高 <![if !msEquation]>  <![endif]>）：隱藏目標 <![if !msEquation]>  <![endif]>主導
-   分類：**類型****II****（清洗型）**

**詮釋**：儘管表面目標為遷移，極端的路徑低效與高損失-純化乘積表明系統性的行動者選擇。

----------

**6.2** **案例研究B****：資源分配危機**

**情境**：在時期 <![if !msEquation]>  <![endif]>內，總資源 <![if !msEquation]>  <![endif]>保持恆定，但：

-   <![if !msEquation]>  <![endif]>
-   <![if !msEquation]>  <![endif]>
-   頂層5%的 <![if !msEquation]>  <![endif]>：<![if !msEquation]>  <![endif]>  增加30%
-   底層50%的 <![if !msEquation]>  <![endif]>：1500萬行動者損失

**計算**：

<![if !msEquation]>  
<![endif]><![if !supportLineBreakNewLine]>  
<![endif]>

**分析**：

-   定理4.4適用：資源優先級傾向向上集中
-   分類：**類型****III****（重分配型）**

**詮釋**：儘管總體資源充足，分配機制優先保障精英而非大眾生存。

----------

**7.** **討論**

**7.1** **與既有理論的關係**

我們的框架**包含**若干經典結果：

**民主和平論**[9]：  
若 <![if !msEquation]>  <![endif]>（民主指數，將在未來論文定義）高，則 <![if !msEquation]>  <![endif]>（參與度）高，由公理A3使得最大化 <![if !msEquation]>  <![endif]>的行動（戰爭）可能性降低。

**寡頭鐵律**[10]：  
無制度約束時，<![if !msEquation]>  <![endif]>（集中度，未來論文）單調遞增，從我們的公理推導出米歇爾斯的觀察。

**中等收入陷阱**[11]：  
若增長依賴 <![if !msEquation]>  <![endif]>（績效正當性）單一支柱，且 <![if !msEquation]>  <![endif]>增加，定理4.4預測停滯——符合經驗模式。

**7.2** **相較於先前進路的優勢**

1.  **價值中立**：無嵌入的規範主張
2.  **可證偽性**：數值閾值可被檢驗
3.  **普遍性**：適用於任何 <![if !msEquation]>  <![endif]>系統
4.  **演繹力**：傳統理論作為推論出現

**7.3** **局限與未來工作**

-   **靜態框架**：當前版本分析單一轉換；需要動態擴展
-   **度量選擇**：<![if !msEquation]>  <![endif]>  選擇影響 <![if !msEquation]>  <![endif]>；需要穩健性分析
-   **不完全信息**：假設歷史數據可得；需要部分觀測方法

----------

**8.** **結論**

我們構建了政治系統分析的首個完整公理基礎。通過定義基本元素（<![if !msEquation]>  <![endif]>）、陳述最小公理（A1-A5）並推導定理（4.1-4.4），我們實現了對政治轉換的客觀、定量分類。我們的框架證明：

1.  隱藏目標可從路徑選擇**推斷**（定理4.1）
2.  清洗可通過損失-純化乘積**檢測**（定理4.2）
3.  權力鞏固創造**歸屬不對稱**（定理4.3）
4.  資源優先級通過不平等動態**揭示**（定理4.4）

所有結論源於邏輯與數據，而非意識形態。

**未來研究**將擴展至：

-   針對民主、經濟、資訊流動的模組化公理集
-   帶微分方程的動態模型
-   多主體博弈論精煉
-   自動分析的計算工具

通過確立政治符號學為嚴格學科，我們為學者、政策制定者與公民提供了**理論驅動、可證偽、價值中立**的理解權力工具。

----------

**參考文獻**

[1] Kolmogorov, A.N. (1933). _概率論基礎_[2] Von Neumann, J., Morgenstern, O. (1944). _博弈論與經濟行為_  
[3] Nash, J. (1950). n人博弈中的均衡點. _美國科學院院刊_ 36(1), 48-49  
[4] Arrow, K.J. (1951). _社會選擇與個人價值_[5] Sen, A. (1970). _集體選擇與社會福利_[6] Axelrod, R. (1997). _合作的複雜性_[7] Epstein, J.M. (2006). _生成社會科學_[8] Lijphart, A. (1999). _民主模式_[9] Russett, B. (1993). _把握民主和平_[10] Michels, R. (1911). _政黨_[11] Eichengreen, B., et al. (2012). 當快速增長經濟體放緩. _亞洲經濟論文_ 11(1), 42-87

----------

**補充材料**

**SM1****：支持引理的證明**

[詳細證明因篇幅限制省略；擴展版本中提供]

**SM2****：敏感性分析**

[閾值 <![if !msEquation]>  <![endif]>的穩健性檢驗]

**SM3****：計算實現**

Python函式庫 polsym 實現所有度量與定理：[GitHub連結]

----------

**附錄A****：術語對照表**

**英文術語**

**中文術語**

**符號**

Power Entity

權力主體

<![if !msEquation]>  <![endif]>

Actor Set

行動者集合

<![if !msEquation]>  <![endif]>

System State

系統狀態

<![if !msEquation]>  <![endif]>

Transformation

轉換操作

<![if !msEquation]>  <![endif]>

Loss Rate

損失率

<![if !msEquation]>  <![endif]>

Purity Coefficient

純化係數

<![if !msEquation]>  <![endif]>

Path Efficiency

路徑效率

<![if !msEquation]>  <![endif]>

Resource Inequality

資源不平等度

<![if !msEquation]>  <![endif]>

Purge Index

清洗指數

<![if !msEquation]>  <![endif]>

Goal Deviation

目標偏離度

<![if !msEquation]>  <![endif]>

----------

**附錄B****：數值範例**

為便於理解，我們提供具體數值範例（完全虛構）：

**範例1****：優化型轉換**

輸入：N₀ = 10000, Nf = 9500, d直 = 100km, d實 = 105km

計算：L = 0.05, η = 0.95, Ψ = 0.05×0.6 = 0.03

分類：類型I（優化型）

**範例2****：清洗型轉換**

輸入：N₀ = 50000, Nf = 5000, d直 = 500km, d實 = 4000km, φ = 0.92

計算：L = 0.90, η = 0.125, Ψ = 0.90×0.92 = 0.828

分類：類型II（清洗型）
