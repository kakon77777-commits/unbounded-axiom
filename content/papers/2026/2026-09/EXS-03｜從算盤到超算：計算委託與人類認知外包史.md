# EXS-03｜從算盤到超算：計算委託與人類認知外包史
## 從外部算術、數值天氣預報到 AI 推論委託

**系列：** Human Capability Externalization & Intelligence Substrate Evolution Series  
**系列中文名：** 人類能力外部化與智能載體演化系列  
**編號：** EXS-03  
**版本：** v1.0  
**日期：** 2026-08-18  
**狀態：** Canonical Source / UTF-8 Markdown  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

EXS-01 將人類文明描述為能力外部化的長期歷史；EXS-02 進一步指出，外部能力一旦成為基礎設施與環境，就必須區分可達能力與韌性能力。本文沿此脈絡，聚焦其中一條對現代文明尤其重要的支線：人類如何逐步把「計算本身」交給外部載體，並最終走向把部分推論、預測、模型選擇與認知工作交給人工智慧。

本文提出「計算委託」概念，用以區分單純使用工具與把大量中間運算步驟交由外部系統完成。算盤、數表、機械計算器、電子計算機、超級電腦與現代 AI 並非同一類技術，但可以被置於一條連續軸上：外部系統逐步承擔更多計算深度、更多中間狀態與更大的狀態空間，而人類角色從逐步執行者轉向問題定義者、模型設計者、輸入提供者、輸出解讀者與治理者。

數值天氣預報是這條歷史的代表案例。20 世紀初 Lewis Fry Richardson 曾設想以約 64,000 名人類「computers」協同計算，以便讓數值預報速度追上天氣演化；1950 年，ENIAC 完成首批成功的數值天氣預報實驗，證明電子計算可取代大規模人工算術流程；1979 年 ECMWF 開始業務化中期數值預報；到 2025 年，ECMWF 的 Artificial Intelligence Forecasting System 進入業務運行，2026 年 NOAA 亦把 AI 驅動的全球預報模型投入營運。這條路徑顯示，外包的內容已從「算數值」逐步推進到「由學得的模型直接生成世界狀態預測」。

本文區分「計算委託」「模型委託」「推論委託」「決策委託」與「代理委託」，並提出「人類可審閱頻寬」與「機器中間狀態規模」的差距。當一個文明依賴每秒遠超人類可逐步重算的計算系統時，人類知識實踐就不再建立於「我親自完成所有步驟」，而建立於模型、演算法、驗證、交叉檢查、儀器、軟體、硬體與制度所形成的可信鏈。這使超算成為 AI 認知委託之前的重要歷史前身。

本文的核心結論是：AI 並不是人類第一次把認知工作放到外部，而是計算委託歷史第一次大規模跨入語義、生成、推理與行動選擇層。理解這條連續史，可以避免把 AI 認知外包誤解為毫無歷史先例的突然斷裂，也能更精確地指出真正的新問題何在：外部系統不再只回答人類明確形式化後的問題，而開始參與「問題如何表示、哪些中間步驟值得採取、什麼結果具有意義」本身。

---

## 關鍵詞

計算委託；認知外包；認知卸載；算盤；數表；機械計算；電子計算；超級電腦；數值天氣預報；科學模擬；人工智慧；AI 推論；人機分工；可信計算鏈

---

# 1. 從能力外部化進入「計算外部化」

EXS-01 建立：

$$
\boxed{
C_{\mathrm{int}}
\neq
C_{\mathrm{acc}}
}
$$

EXS-02 再建立：

$$
\boxed{
C_{\mathrm{acc}}
\neq
C_{\mathrm{resilient}}.
}
$$

本文處理一個更具體的問題：

> 當人類面對超出裸身大腦可合理完成的運算量時，文明如何把計算過程配置到外部載體？

可先定義：

$$
C_{\mathrm{calc,int}}
=
\text{internally executable calculation capability},
$$

$$
C_{\mathrm{calc,ext}}
=
\text{externally executable calculation capability}.
$$

在具有工具與機器的文明中：

$$
C_{\mathrm{calc,acc}}
=
F(
C_{\mathrm{calc,int}},
C_{\mathrm{calc,ext}}
).
$$

本文的核心不是宣稱：

$$
\text{external computation}
=
\text{human thought}.
$$

而是指出，在大量科學與工程工作中：

$$
\boxed{
\text{Humanly usable knowledge}
}
$$

早已依賴：

$$
\boxed{
\text{calculations no individual human personally executes step by step}.
}
$$

---

# 2. 什麼叫「計算委託」？

本文把「計算委託」定義為：

> 主體保留任務、問題、表示、輸入、驗證或解讀中的一部分，但把其中可形式化的大量運算步驟交由外部載體執行。

令問題為：

$$
P.
$$

傳統純手算流程可簡化為：

$$
H:
P
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
\rightarrow
s_n
\rightarrow
y.
$$

其中 $H$ 是人類， $s_i$ 是中間狀態。

計算委託後：

$$
H
\rightarrow
P'
\rightarrow
M
\rightarrow
y
\rightarrow
H,
$$

其中 $M$ 是外部計算載體。

人類可能不再直接處理：

$$
\{s_1,s_2,\ldots,s_n\}.
$$

因此：

$$
\boxed{
\text{Task Ownership}
\neq
\text{Step Execution}.
}
$$

這個區分是理解超算與 AI 的基礎。

---

# 3. 算盤：外部狀態開始承擔算術中間結構

算盤不是電子計算機，但它已經展示計算外部化的一個核心原理：

$$
\text{Internal Numerical State}
\rightarrow
\text{External Physical State}.
$$

Smithsonian National Museum of American History 將算盤描述為透過移動珠子、石子或計數片完成算術計算的計算裝置。[1]

這意味著：

$$
n
$$

不必只存在於人的工作記憶。

它可以被映射為：

$$
\phi(n)
=
\text{configuration of counters}.
$$

接著，計算操作：

$$
f(n)
$$

可以部分轉化為：

$$
T_f(
\phi(n)
).
$$

人仍然理解規則、選擇操作並移動珠子，但一部分「記住目前數值狀態」的負擔已經移到外部載體。

因此算盤可以被理解成：

$$
\boxed{
\text{Externalized State Memory}
+
\text{Rule-Guided Manipulation}.
}
$$

---

# 4. 數表：甚至答案本身也可以預先被文明計算

在機械與電子計算以前，人類還採取另一種策略：

$$
\boxed{
\text{precompute once}
\rightarrow
\text{reuse many times}.
}
$$

對某些函數：

$$
f(x),
$$

文明可以先建立：

$$
\{(x_i,f(x_i))\}_{i=1}^{N}.
$$

之後使用者不是重新推導，而是查表。

這是非常重要的認知外包模式。

因為：

$$
\text{calculation at use time}
$$

被部分替換成：

$$
\text{retrieval at use time}.
$$

因此：

$$
\boxed{
\text{Computation}
\rightarrow
\text{Stored Representation}
\rightarrow
\text{Lookup}.
}
$$

這個模式到了今天仍然存在，只是規模從紙本數表變成：

- 資料庫；
- cache；
- lookup table；
- 預計算索引；
- embedding；
- 模型權重。

---

# 5. 機械計算器：規則開始由機構執行

當算術規則被編碼到齒輪、輪軸與機構中，委託程度又提高一層。

人類不只外部保存狀態，而是把：

$$
\text{rule execution}
$$

本身部分移交機構。

因此：

$$
\boxed{
\text{External State}
\rightarrow
\text{External Rule Execution}.
}
$$

這是一個質變。

因為在算盤中，人很大程度仍是運算規則的直接執行者。

在機械計算器中，操作員提供：

$$
\text{input}
$$

並觸發：

$$
\text{mechanism},
$$

機器開始承擔更大的中間步驟。

這為後來電子計算奠定了一個一般模式：

$$
\boxed{
\text{Represent}
\rightarrow
\text{Encode Rule}
\rightarrow
\text{Execute Externally}.
}
$$

---

# 6. 「Computer」曾經是人的工作角色

在電子計算機以前，「computer」可以指執行計算工作的人。

這個歷史事實具有很強的理論意義：

$$
\boxed{
\text{Computation}
}
$$

原本不是天然等同於：

$$
\boxed{
\text{Machine}.
}
$$

它是一種工作。

因此，計算機革命的一部分可以重新表達為：

$$
\boxed{
\text{Human Computation Labor}
\rightarrow
\text{Machine Computation}.
}
$$

這與工業革命中：

$$
\text{Human Mechanical Labor}
\rightarrow
\text{Machine Mechanical Labor}
$$

具有結構上的類似性。

差異在於，它外部化的不是主要肌肉功，而是：

$$
\boxed{
\text{formal symbolic transformation}.
}
$$

---

# 7. Richardson 的「預報工廠」：一個幾乎完美的過渡案例

20 世紀初，Lewis Fry Richardson 嘗試用數學方程直接計算未來天氣。

問題不是只有方程是否正確。

還有：

$$
\boxed{
\text{Calculation must finish before the future arrives}.
}
$$

NOAA 的歷史資料記錄，Richardson 的一次計算耗時約六週，而且結果並不成功；他進而設想一座「forecast factory」，約需 64,000 名人類 computers，各自負責地球的一小部分，由中央協調者統一計算。[2]

因此，天氣預報把一個非常深的問題暴露出來：

$$
\boxed{
\text{Correct Computation}
\neq
\text{Useful Computation}.
}
$$

如果：

$$
\tau_{\mathrm{calc}}
>
\tau_{\mathrm{phenomenon}},
$$

即使方法形式上可行，也無法形成即時決策能力。

所以：

$$
\boxed{
\text{Computational Latency}
}
$$

本身就是文明能力的一部分。

---

# 8. 64,000 名人類 computers 與一台電子計算機

Richardson 的設想非常適合本文，因為它展示兩種完全不同的擴展方式。

第一種：

$$
\boxed{
\text{Scale Human Computation Horizontally}.
}
$$

即：

$$
H_1+H_2+\cdots+H_{64000}.
$$

第二種則是：

$$
\boxed{
\text{Move Computation onto Electronic Substrate}.
}
$$

即：

$$
M_{\mathrm{electronic}}.
$$

NOAA 對這段歷史的描述甚至直接指出，Richardson 想像中的 64,000 名人類 computers 最終可以被一台大型電子計算機取代。[2]

因此：

$$
\boxed{
\text{Computational Scaling}
}
$$

第一次大規模脫離：

$$
\boxed{
\text{human headcount scaling}.
}
$$

這正是後續超算、雲端與 AI 能夠成立的重要前提。

---

# 9. 1950：ENIAC 把「計算趕不上天氣」變成可行問題

1950 年，Jule Charney、John von Neumann 等人的團隊使用 ENIAC 完成成功的數值天氣預報實驗。

NOAA 的歷史記錄指出，1950 年 4 月完成的第一個一日非線性天氣預報需要全天候操作，並因 ENIAC 故障等原因耗費超過 24 小時，但它證明了數值天氣預報的可行性。[2]

這是一個非常漂亮的歷史臨界點：

$$
\tau_{\mathrm{calc}}
\approx
\tau_{\mathrm{forecast}}.
$$

雖然還不快。

但至少：

$$
\boxed{
\text{numerical prediction had become computationally realizable}.
}
$$

因此 ENIAC 不是因為「比今天的電腦快」而重要。

而是因為：

$$
\boxed{
\text{machine calculation crossed a domain-usefulness threshold}.
}
$$

---

# 10. 從「機器算」到「機器產生可用預測」

計算委託可以分成兩個層次。

第一層：

$$
\text{Machine computes values}.
$$

第二層：

$$
\text{Machine-generated values become part of operational decision systems}.
$$

這兩者並不相同。

如果計算結果只是研究實驗：

$$
M
\rightarrow
y.
$$

但若預測開始進入：

- 航空；
- 海運；
- 農業；
- 防災；
- 能源；
- 軍事；
- 日常生活；

則：

$$
M
\rightarrow
y
\rightarrow
\text{social action}.
$$

此時，計算載體開始成為：

$$
\boxed{
\text{Epistemic Infrastructure}.
}
$$

也就是社會用來形成「對世界接下來會怎樣」之判斷的基礎設施。

---

# 11. 1979：ECMWF 把超算預測變成持續性制度

ECMWF 於 1975 年成立，其目的之一就是整合歐洲氣象資源，以產生中期預報；1979 年 6 月做出首批即時中期預報，並自 1979 年 8 月 1 日起正式進行業務化中期預報。[3]

這表示計算委託又跨過另一個門檻：

$$
\boxed{
\text{Experiment}
\rightarrow
\text{Institutionalized Operation}.
}
$$

不是：

> 偶爾使用計算機預報天氣。

而是：

> 一個跨國制度持續依賴大型計算系統來產生預報。

因此：

$$
\boxed{
\text{Computation}
\rightarrow
\text{Operational Infrastructure}.
}
$$

EXS-02 所說的「工具環境化」在此開始非常清楚。

---

# 12. 超級電腦：人類不再能逐步重算文明所使用的結果

超級電腦把計算委託推到極端。

若一台系統每秒執行：

$$
10^{18}
$$

級別的浮點運算，

任何單一人類都不可能：

$$
\text{personally replay every operation}.
$$

2024 年部署的 LLNL El Capitan 是 NNSA 首台 exascale 超級電腦；LLNL 官方資料指出，其峰值能力超過 $2.79$ exaflops，而 exascale 至少意味每秒 $10^{18}$ 級雙精度運算。[4]

因此，現代科學已經必須接受：

$$
\boxed{
\text{Epistemic Use}
\neq
\text{Human Step-by-Step Reproduction}.
}
$$

這不是 AI 才帶來的問題。

它在 HPC 時代已經非常明顯。

---

# 13. 「我沒有重算每一步」為什麼不等於盲信？

若科學可信度要求：

$$
\text{one human personally checks every machine operation},
$$

那現代 HPC 幾乎全部不能使用。

但科學並不是如此運作。

它建立的是分層可信鏈：

$$
\boxed{
\text{Theory}
\rightarrow
\text{Model}
\rightarrow
\text{Algorithm}
\rightarrow
\text{Implementation}
\rightarrow
\text{Execution}
\rightarrow
\text{Output}
\rightarrow
\text{Validation}
\rightarrow
\text{Interpretation}.
}
$$

每一層使用不同的驗證方法。

例如：

- 理論一致性；
- 演算法分析；
- 單元測試；
- 交叉實作；
- 數值收斂；
- benchmark；
- 實驗比對；
- 多模型 ensemble；
- 重複計算；
- 實際觀測。

因此：

$$
\boxed{
\text{Trust}
\neq
\text{Direct Recalculation}.
}
$$

更接近：

$$
\boxed{
\text{Trust}
=
\text{Layered Verification}.
}
$$

---

# 14. 超算其實已經改變「理解」的定義

傳統直覺容易認為：

> 如果我不能把全部步驟在腦中跑一次，我就不理解。

但現代科學大量依賴：

$$
\boxed{
\text{Structural Understanding}
}
$$

而不是：

$$
\boxed{
\text{Complete Executional Reproduction}.
}
$$

一個研究者可以理解：

- 模型方程；
- 邊界條件；
- 初始條件；
- 數值格式；
- 誤差來源；
- 輸出物理意義；

卻不需要記住：

$$
10^{15}
$$

個中間數值。

因此：

$$
\boxed{
\text{Understanding the Process}
\neq
\text{Retaining Every Intermediate State}.
}
$$

這是從計算委託走向 AI 認知委託時非常重要的認識論前置。

---

# 15. 科學模擬：計算機開始成為認知儀器

望遠鏡擴張：

$$
\Omega_{\mathrm{observable}}.
$$

超算則擴張：

$$
\Omega_{\mathrm{simulable}}.
$$

也就是：

$$
\boxed{
\text{states that can be computationally explored}.
}
$$

在核物理、材料、流體、氣候、天文、分子動力學與工程設計中，許多狀態：

- 無法直接安全實驗；
- 太大；
- 太小；
- 太快；
- 太慢；
- 太昂貴；
- 需要大量參數掃描；

因而先透過計算世界被探索。

LLNL 對 El Capitan 的任務描述即包含核武庫安全與可靠性模擬、材料發現、高能量密度物理、材料狀態方程等領域。[4]

所以超算不是「比較快的計算器」。

它逐漸成為：

$$
\boxed{
\text{Scientific Observation through Simulation}.
}
$$

---

# 16. 模擬不是現實：計算委託仍受到覆蓋率限制

本文必須加入一個重要限制：

$$
\boxed{
\text{Simulation}
\neq
\text{Reality}.
}
$$

令世界為：

$$
W.
$$

模型為：

$$
M(W).
$$

則一般情況下：

$$
M(W)
\neq
W.
$$

因此，超算即使精確執行：

$$
M,
$$

也只能保證：

$$
\text{execution fidelity to }M,
$$

不能自動保證：

$$
\text{model completeness with respect to }W.
$$

這也就是為什麼：

$$
\boxed{
\text{more compute}
\neq
\text{global predictive closure}.
}
$$

計算委託解決的是：

$$
\text{execution capacity}.
$$

它不自動解決：

- 不完整觀測；
- 錯誤假設；
- 模型邊界；
- 未知關係；
- 開放世界；
- 反身性；
- 新事件。

---

# 17. 天氣預報再一次展示「計算能力不等於模型完整」

數值天氣預報不只是算得快。

它還需要：

$$
\text{observations}
+
\text{data assimilation}
+
\text{model}
+
\text{numerics}
+
\text{compute}.
$$

NOAA 對現代 NWP 的描述指出，電腦模型會把當前天氣觀測同化進模型，再計算未來的溫度、降水與大量氣象變數。[5]

因此：

$$
\boxed{
\text{Prediction}
=
F(
\text{Observation},
\text{Model},
\text{Assimilation},
\text{Compute}
).
}
$$

只增加：

$$
\text{Compute}
$$

不一定能補掉所有其他項目的缺口。

這與後續 AI 預測具有直接連續性。

---

# 18. Ensemble：當「一個答案」不夠，文明開始委託「可能性分布」

1992 年，ECMWF 首次把 ensemble prediction 納入業務系統。[3]

ensemble 的重要性不只是多跑幾次。

它代表：

$$
\boxed{
\text{Prediction}
\rightarrow
\text{Distribution of plausible futures}.
}
$$

即：

$$
\hat y
\rightarrow
\{\hat y_1,\hat y_2,\ldots,\hat y_n\}.
$$

人類不再要求機器給：

> 唯一未來。

而是：

> 一組具有不同條件與機率結構的未來。

這代表計算委託開始承擔：

$$
\boxed{
\text{uncertainty representation}.
}
$$

而人類工作則轉向：

$$
\boxed{
\text{risk interpretation}.
}
$$

---

# 19. 從計算委託到模型委託

傳統電子計算主要可理解為：

$$
H
\rightarrow
\text{explicit model}
\rightarrow
M
\rightarrow
y.
$$

其中核心模型由人顯式寫出。

但機器學習帶來新的可能：

$$
\text{data}
\rightarrow
\text{learned model}
\rightarrow
y.
$$

因此開始出現：

$$
\boxed{
\text{Model Delegation}.
}
$$

更精確地說，人類仍然：

- 選資料；
- 定義目標；
- 選架構；
- 設訓練方式；
- 評估模型；

但中間的：

$$
\text{input-output representation}
$$

不再完全由人類逐條手寫。

這是從傳統計算向 AI 的重要過渡。

---

# 20. 2025：ECMWF AIFS 把 AI 預報帶入業務化

2025 年 2 月 25 日，ECMWF 將 Artificial Intelligence Forecasting System 的單一預報版本正式投入業務運行，與傳統物理型 Integrated Forecasting System 並行。[6]

ECMWF 指出，AIFS 使用與 IFS 相同的初始條件，這些條件結合短期預報與約 6,000 萬筆經品質控制的觀測；AIFS 則利用從歷史天氣演變中學得的模型推算未來。[6]

因此：

$$
\boxed{
\text{Physical Numerical Integration}
}
$$

開始與：

$$
\boxed{
\text{Learned State Transition}
}
$$

共同成為業務預報載體。

這是一個重要的歷史轉折。

不是因為 AI「第一次預測天氣」。

而是因為：

$$
\boxed{
\text{AI inference became part of an institutionalized forecasting infrastructure}.
}
$$

---

# 21. AI 預報不是把「計算」取消，而是改變計算的型別

AIFS 並不是：

$$
\text{no computation}.
$$

它仍依賴大量數值運算。

真正改變的是：

$$
\boxed{
\text{what is being computed}.
}
$$

傳統 NWP：

$$
\text{explicit physical equations}
\rightarrow
\text{numerical integration}.
$$

AI 預報：

$$
\text{learned parameters}
+
\text{current state}
\rightarrow
\text{inference}.
$$

所以：

$$
\boxed{
\text{Computational Delegation}
}
$$

沒有消失。

它只是進一步變成：

$$
\boxed{
\text{Representational Delegation}
+
\text{Inference Delegation}.
}
$$

---

# 22. 2026：AI 天氣預報已不只是單一機構實驗

到 2026 年，NOAA 也開始部署 AI 驅動的全球天氣模型，並形成 2026–2031 AI/ML modeling strategy。[7]

這說明：

$$
\boxed{
\text{AI Weather Prediction}
}
$$

正在從研究競賽逐步進入：

$$
\boxed{
\text{Operational Forecast Ecosystem}.
}
$$

因此，天氣預報歷史可以被壓縮成非常漂亮的一條線：

$$
\boxed{
\text{Human Calculation}
\rightarrow
\text{Electronic Calculation}
\rightarrow
\text{Operational NWP}
\rightarrow
\text{Supercomputing}
\rightarrow
\text{AI Forecasting}.
}
$$

這正是本文「計算委託史」的核心實證案例。

---

# 23. 認知卸載研究也已跨出記憶領域

現代 cognitive offloading 研究並不只研究「把事情寫在紙上」。

2026 年的綜述指出，當代研究中的 offloading 任務已涵蓋：

- 記憶；
- 計算器與統計軟體；
- 決策支援；
- 專家諮詢；
- 創意與寫作輔助工具。[8]

因此：

$$
\boxed{
\text{Cognitive Offloading}
}
$$

已經不是單純：

$$
\text{Memory Offloading}.
$$

而開始接近：

$$
\boxed{
\text{Distributed Cognitive Work}.
}
$$

本文所說的計算委託，可以被理解為其中歷史最成熟的一支。

---

# 24. 為什麼計算器與 AI 不應混成同一種 offloading？

雖然都屬於外部認知工作，仍必須分型。

## 24.1 計算器

通常：

$$
H:
P
\rightarrow
\text{explicit operation}
\rightarrow
M.
$$

例如：

$$
123\times456.
$$

人已經清楚知道要求哪個形式化運算。

## 24.2 傳統程式

人定義：

$$
\text{algorithm}.
$$

機器執行。

## 24.3 AI 系統

人可能只提供：

$$
\text{goal}
$$

或：

$$
\text{natural-language problem}.
$$

AI 再自行選擇：

- 表示；
- 子問題；
- 工具；
- 搜尋路徑；
- 中間推理；
- 候選答案。

因此：

$$
\boxed{
\text{Operation Specification Burden}
\downarrow
}
$$

同時：

$$
\boxed{
\text{Machine Internal Decision Burden}
\uparrow.
}
$$

這就是 AI 相對傳統計算器真正的新層。

---

# 25. 從「幫我算」到「幫我想怎麼算」

計算委託最初是：

> 幫我算。

可形式化為：

$$
H
\rightarrow
f
\rightarrow
M
\rightarrow
f(x).
$$

更後面的 AI 則可能變成：

> 幫我判斷這個問題該怎麼表示、該用什麼方法、該查什麼資料、該怎麼驗證。

可寫成：

$$
H
\rightarrow
P
\rightarrow
A
\rightarrow
\{
f_1,f_2,\ldots,f_k
\}
\rightarrow
y.
$$

因此：

$$
\boxed{
\text{Execution Delegation}
\rightarrow
\text{Method Delegation}.
}
$$

這是從計算史走向 AI 史的真正鉸鏈之一。

---

# 26. 五種委託必須分開

本文提出五種不同層級。

## $D_0$：狀態外部化

$$
\boxed{
\text{State Delegation}
}
$$

外部物件保存中間狀態。

例：

$$
\text{abacus}.
$$

## $D_1$：計算委託

$$
\boxed{
\text{Execution Delegation}
}
$$

外部系統執行明確規則。

例：

$$
\text{calculator},
\text{computer}.
$$

## $D_2$：模型委託

$$
\boxed{
\text{Model Delegation}
}
$$

部分映射關係由資料與訓練產生，而非完全手寫。

例：

$$
\text{machine learning model}.
$$

## $D_3$：推論委託

$$
\boxed{
\text{Inference Delegation}
}
$$

外部系統處理問題分解、候選生成與證據整合。

## $D_4$：決策委託

$$
\boxed{
\text{Decision Delegation}
}
$$

外部系統在多個可能行動中選擇。

## $D_5$：代理委託

$$
\boxed{
\text{Agency Delegation}
}
$$

外部系統持續維持狀態、目標與回饋，完成長鏈世界行動。

這些層級不是道德等級，也不是主體性判定。

---

# 27. AI 的歷史特殊性因此可以更精確描述

AI 不是：

$$
\boxed{
\text{first cognitive tool}.
}
$$

也不是：

$$
\boxed{
\text{first computation outside the brain}.
}
$$

AI 比較特殊的是：

$$
\boxed{
D_2
\rightarrow
D_3
\rightarrow
D_4
\rightarrow
D_5
}
$$

開始大規模工程化。

也就是：

$$
\boxed{
\text{External Computation}
\rightarrow
\text{External Method Selection}
\rightarrow
\text{External Agency}.
}
$$

這樣才能同時保留：

$$
\boxed{
\text{historical continuity}
}
$$

與：

$$
\boxed{
\text{functional discontinuity}.
}
$$

---

# 28. 人類的角色不是消失，而是沿著委託鏈上移

當計算交給機器後，人類並沒有立刻退出。

角色可能從：

$$
\text{Arithmetic Executor}
$$

移向：

$$
\text{Problem Formulator}.
$$

再從：

$$
\text{Problem Formulator}
$$

移向：

$$
\text{Model Designer}.
$$

再從：

$$
\text{Model Designer}
$$

移向：

$$
\text{Validator}.
$$

再往後：

$$
\boxed{
\text{Goal Setter}
+
\text{Constraint Setter}
+
\text{Interpreter}
+
\text{Governor}.
}
$$

因此：

$$
\boxed{
\text{Delegation}
\neq
\text{Human Disappearance}.
}
$$

但：

$$
\boxed{
\text{Human Role}
}
$$

確實可能改變。

---

# 29. 這也產生「人類可審閱頻寬」問題

假設機器每秒產生：

$$
R_M
$$

個內部運算或決策事件。

人類可有意義審閱：

$$
R_H.
$$

當：

$$
R_M
\gg
R_H,
$$

就不可能採取：

$$
\boxed{
\text{review every internal event}.
}
$$

此時治理必須轉向：

- 抽樣；
- 性質驗證；
- 規則驗證；
- 邊界條件；
- 日誌；
- 可重現測試；
- 統計監控；
- 獨立交叉驗證；
- 異常偵測。

因此：

$$
\boxed{
\text{Scale}
\rightarrow
\text{Verification Architecture}.
}
$$

這其實早在 HPC 時代就已經成立。

---

# 30. 「超算神諭」早於「AI 神諭」

天氣預報提供一個非常有意思的文化案例。

一般使用者每天接受：

> 明天降雨機率 $70\%$。

但他通常不會：

- 重跑氣象模型；
- 重新同化幾千萬筆觀測；
- 檢查數值穩定性；
- 重建 ensemble；
- 驗證每一個程式碼路徑。

他接受的是一整條制度化可信鏈。

因此，早在生成式 AI 以前，人類已經生活在：

$$
\boxed{
\text{Machine-Mediated Epistemic Systems}.
}
$$

這不表示：

$$
\text{forecast}
=
\text{oracle}.
$$

而表示：

$$
\boxed{
\text{civilization already accepts machine-produced knowledge artifacts it cannot individually recompute}.
}
$$

---

# 31. 人類真正保留的是「解讀權」嗎？

在傳統 HPC 時代，一個常見結構是：

$$
\boxed{
\text{Machine Calculates}
\rightarrow
\text{Human Interprets}.
}
$$

因此可以暫時定義：

$$
I_H
=
\text{Human Interpretive Share}.
$$

即：

> 在整條知識鏈中，哪些語義判斷仍主要由人類完成？

例如：

- 這個數值代表什麼？
- 是否可信？
- 是否具有政策意義？
- 是否需要採取行動？
- 風險值多少算高？

AI 出現後真正可能下降的是：

$$
I_H.
$$

因為 AI 不只算：

$$
y.
$$

還開始生成：

$$
\boxed{
\text{interpretation of }y.
}
$$

因此：

$$
\boxed{
\text{Computational Delegation}
\rightarrow
\text{Interpretive Delegation}.
}
$$

這比單純「算得更快」重要。

---

# 32. 但解讀也不是全或無

不能把問題寫成：

$$
I_H=1
$$

或：

$$
I_H=0.
$$

現實更可能是：

$$
0<I_H<1.
$$

例如 AI：

- 先整理結果；
- 找出異常；
- 生成圖表；
- 提供候選解釋；

人類再：

- 選擇；
- 判斷；
- 反駁；
- 結合倫理與制度條件。

因此：

$$
\boxed{
\text{Human-AI Interpretation}
}
$$

可能成為新的混合型態。

本文不預設哪一方必然永遠在最上層。

---

# 33. 計算委託與主體性完全是兩個問題

一個超級電腦可以完成：

$$
10^{18}
$$

級運算，

不代表：

$$
\boxed{
\text{it is a subject}.
}
$$

同樣地，一個 AI 承擔：

$$
D_3,D_4,D_5
$$

中的部分功能，也不能僅從功能委託推出：

$$
\boxed{
\text{moral subjecthood}.
}
$$

所以：

$$
\boxed{
\text{Cognitive Delegation}
\neq
\text{Subjecthood Attribution}.
}
$$

這條型別安全對後續 AI 主體性研究非常重要。

---

# 34. 計算委託與信任也不是同一件事

把計算交給機器：

$$
\text{Delegation}
$$

不代表：

$$
\text{Unconditional Trust}.
$$

反之：

$$
\boxed{
\text{High Delegation}
+
\text{High Verification}
}
$$

完全可能成立。

例如：

- 航太；
- 核能；
- 氣象；
- 金融；
- 密碼；
- 科學模擬；

都大量使用外部計算，同時也發展出複雜驗證制度。

因此：

$$
\boxed{
\text{Delegation}
\neq
\text{Epistemic Surrender}.
}
$$

真正的問題是：

$$
\boxed{
\text{whether verification scales with delegation}.
}
$$

---

# 35. AI 時代的認知委託其實繼承了超算時代的治理問題

AI 常被批評：

> 人類無法逐步檢查全部內部計算。

但若把這句當成絕對拒絕條件，超算、現代編譯器、作業系統、網路與大型數值模型也很難通過。

真正可行的制度一直都是：

$$
\boxed{
\text{Selective Inspection}
+
\text{Formal Constraints}
+
\text{Empirical Validation}
+
\text{Cross-Checking}
+
\text{Monitoring}.
}
$$

所以 AI 治理不必假裝：

$$
\text{every internal token}
$$

都能由人逐個批准。

而應研究：

$$
\boxed{
\text{Which properties must remain auditable?}
}
$$

這將成為第二系列中「Human Governance Bandwidth」的重要前置。

---

# 36. 「計算快於人」早就不是未來式

Richardson 的問題是：

$$
\text{human calculation too slow for weather}.
$$

1950 年電子計算開始突破。

現在 exascale 系統已將：

$$
R_M
$$

推到：

$$
10^{18}
$$

級操作每秒。

因此：

$$
\boxed{
\text{Machine Calculation Rate}
\gg
\text{Human Calculation Rate}
}
$$

並不是 AGI 才會出現的條件。

AI 真正新增的問題是：

$$
\boxed{
\text{Machine Semantic/Decision Rate}
}
$$

也可能逐步超過：

$$
\boxed{
\text{Human Review Rate}.
}
$$

這就是從 EXS-03 走向第二系列的重要橋樑。

---

# 37. 計算世界與現實世界有不同速度

數位運算具有一種非常特殊的文明屬性：

$$
\boxed{
\text{State transition can often be accelerated by more compute}.
}
$$

但現實世界中：

- 建築；
- 材料老化；
- 生物成長；
- 電網施工；
- 工廠建設；
- 法律協調；

並不都能以同樣方式加速。

因此，從計算委託歷史可進一步得到：

$$
\boxed{
B_{\mathrm{digital}}
\neq
B_{\mathrm{reality}}.
}
$$

本文只建立這個接口。

「Reality Bandwidth」將在第二系列正式展開。

---

# 38. AI 可以讓「計算結果」比「物理實現」累積得更快

如果 AI 大幅提高：

$$
R_{\mathrm{idea}},
$$

$$
R_{\mathrm{model}},
$$

$$
R_{\mathrm{digital\ verification}},
$$

但物理世界的：

$$
R_{\mathrm{experiment}},
$$

$$
R_{\mathrm{manufacturing}},
$$

$$
R_{\mathrm{deployment}}
$$

提高較慢，

則：

$$
\boxed{
\text{Abstract Capability Backlog}
}
$$

可能增加。

因此：

$$
\boxed{
\text{Faster Cognition}
\neq
\text{Instant Civilization}.
}
$$

這正是後續系統奇點研究需要處理的物理斷層。

---

# 39. 計算委託的七相位模型

本文提出一個歷史—功能混合尺度。

## $C_0$：內部計算

$$
\text{Human mental calculation}.
$$

## $C_1$：外部狀態計算

$$
\text{abacus},
\text{written arithmetic}.
$$

## $C_2$：機械規則執行

$$
\text{mechanical calculator}.
$$

## $C_3$：電子通用計算

$$
\text{electronic computer}.
$$

## $C_4$：大型科學計算

$$
\text{HPC},
\text{supercomputer}.
$$

## $C_5$：制度化計算基礎設施

$$
\text{operational forecasting},
\text{cloud},
\text{large simulation systems}.
$$

## $C_6$：學習式推論

$$
\text{machine learning},
\text{AI forecasting}.
$$

## $C_7$：認知／代理委託

$$
\text{AI reasoning},
\text{AI planning},
\text{agents}.
$$

這些不是嚴格年代。

同一時代可以同時存在：

$$
C_0,\ldots,C_7.
$$

---

# 40. 核心命題

本文提出以下十二個核心命題。

## 命題 1：計算是一種可以跨載體分配的工作

$$
\boxed{
\text{Computation}
\neq
\text{Machine by definition}.
}
$$

## 命題 2：計算委託早於電子計算

$$
\boxed{
\text{Computational Delegation}
\not\equiv
\text{Electronic Computing}.
}
$$

## 命題 3：計算能力取決於速度是否足以匹配問題時間尺度

$$
\boxed{
\tau_{\mathrm{calc}}
<
\tau_{\mathrm{useful}}
}
$$

是許多即時問題的必要條件。

## 命題 4：超算使文明知識生產脫離單一人類可逐步重算範圍

$$
\boxed{
R_M
\gg
R_H.
}
$$

## 命題 5：不可逐步重算不等於不可驗證

$$
\boxed{
\text{No Full Human Replay}
\neq
\text{No Verification}.
}
$$

## 命題 6：現代可信計算依賴分層驗證鏈

$$
\boxed{
\text{Trust}
\sim
\text{Layered Verification}.
}
$$

## 命題 7：科學模擬擴張的是可模擬狀態空間

$$
\boxed{
\Omega_{\mathrm{simulable}}
\uparrow.
}
$$

## 命題 8：計算能力不等於世界模型完整性

$$
\boxed{
\text{More Compute}
\neq
\text{Complete World Coverage}.
}
$$

## 命題 9：AI 是計算委託向表示與推論委託的延伸

$$
\boxed{
\text{Execution Delegation}
\rightarrow
\text{Inference Delegation}.
}
$$

## 命題 10：AI 的特殊性不在於第一次外部計算

$$
\boxed{
\text{AI novelty}
\neq
\text{first cognitive offloading}.
}
$$

## 命題 11：認知委託不等於主體性

$$
\boxed{
\text{Cognitive Delegation}
\neq
\text{Subjecthood}.
}
$$

## 命題 12：人類角色可能由執行轉向目標、約束、驗證與解讀

$$
\boxed{
\text{Human Execution Share}
\downarrow
\not\Rightarrow
\text{Human Governance Share}
\downarrow.
}
$$

是否下降必須另行研究。

---

# 41. 可檢驗研究計畫

## 41.1 計算委託歷史指數

對不同時代 $t$ 與領域 $d$，建立：

$$
D_{\mathrm{calc}}(d,t)
=
\frac{
\text{machine-executed formal operations}
}{
\text{total formal operations required}
}.
$$

這不是要求精確計算所有歷史運算，而可透過 proxy 建模。

---

## 41.2 人類中間狀態可見度

定義：

$$
V_H
=
\frac{
\text{meaningfully human-inspected intermediate states}
}{
\text{all relevant intermediate states}
}.
$$

比較：

- 手算；
- 計算器；
- 傳統程式；
- HPC；
- ML；
- LLM agents。

預期：

$$
V_H
\downarrow
$$

但不等於：

$$
\text{verification quality}
\downarrow.
$$

---

## 41.3 天氣預報委託史

以：

$$
1950,
1979,
1992,
2025,
2026
$$

等節點重建：

- 計算速度；
- 模型型別；
- 預報範圍；
- ensemble；
- AI 模型；
- 人類氣象員角色。

測試：

$$
\boxed{
\text{human role shifts from calculation toward interpretation and decision support}.
}
$$

---

## 41.4 HPC 與知識產出

研究：

$$
\Delta C_{\mathrm{HPC}}
$$

與：

- 模擬解析度；
- 參數空間；
- 不確定性量化；
- 實驗替代率；
- 科學發現速度；

的關係。

---

## 41.5 AI 認知委託深度

定義：

$$
D_{\mathrm{AI,cog}}
=
(
d_{\mathrm{representation}},
d_{\mathrm{method}},
d_{\mathrm{inference}},
d_{\mathrm{decision}},
d_{\mathrm{agency}}
).
$$

避免只用：

$$
\text{AI usage rate}
$$

描述認知外包。

---

## 41.6 驗證架構研究

測試在：

$$
R_M/R_H
\uparrow
$$

時，哪些驗證模式可以維持可信度：

- formal verification；
- independent reproduction；
- model ensembles；
- adversarial review；
- theorem prover；
- empirical checks；
- multi-model cross-checking。

---

# 42. 可反駁條件

本文至少存在以下可反駁方向。

1. 若歷史資料顯示算盤、數表、機械計算與電子計算之間不存在任何有解釋力的「外部計算狀態／規則執行」連續性，本文的統一框架需要縮小。
2. 若 HPC 的使用並未降低人類逐步重算需求，本文對「不可逐步重放」的歷史判斷將被削弱。
3. 若科學界的計算結果可信度主要建立於單一人類完整重算，而不是分層驗證，本文的 epistemic chain 模型將被否定。
4. 若 AI 模型長期始終只執行人類完全形式化的明確運算，而不參與表示、方法選擇與推論，本文對 $D_2$ 到 $D_4$ 的斷點預期需下修。
5. 若 AI 天氣模型無法持續進入業務化預報或被證明不具實用價值，本文將其視為委託史新相位的強度需要降低。
6. 若計算速度對即時科學問題幾乎沒有影響，Richardson—ENIAC 案例的普遍性需縮小。
7. 若高機器運算率並未改變驗證方法與人機角色，本文的 review bandwidth 命題需要修正。
8. 若「模型委託」「推論委託」「決策委託」在實證上無法區分，本文五層委託分類需合併。

---

# 43. Non-Claims

本文明確不主張以下命題：

1. 不主張算盤等同現代電腦。
2. 不主張機械計算器等同 AI。
3. 不主張所有外部計算都是認知的一部分。
4. 不主張所有計算都應外包。
5. 不主張使用計算器必然降低數學能力。
6. 不主張使用超算等於放棄理解。
7. 不主張任何不能手算的結果都可信。
8. 不主張超算輸出等於現實。
9. 不主張模擬可以完全替代物理實驗。
10. 不主張 ensemble 可以消除所有不確定性。
11. 不主張數值天氣預報可以完美預測天氣。
12. 不主張 AI 天氣模型已完全取代物理模型。
13. 不主張 AIFS 或 NOAA AI 模型代表所有 AI 預報系統。
14. 不主張更多算力必然帶來更好的世界模型。
15. 不主張 HPC 的歷史等於整個認知外包史。
16. 不主張 cognitive offloading 必然對人類有利。
17. 不主張 cognitive offloading 必然對人類有害。
18. 不主張 AI 使用等於 epistemic surrender。
19. 不主張 AI 可以無條件取代專家判斷。
20. 不主張 AI 已經具有主體性。
21. 不主張認知功能等於人格或道德地位。
22. 不主張 AI 一定會走到完整決策委託。
23. 不主張 AI 一定會走到代理委託。
24. 不主張人類治理角色一定會保持不變。
25. 不主張人類治理角色一定會消失。
26. 不主張機器計算速度可以消除物理世界的時間限制。
27. 不主張數位驗證等於物理實現。
28. 不主張所有形式驗證都能自動化。
29. 不主張所有科學問題都適合形式化。
30. 不主張本文的七相位模型是唯一合理分期。
31. 不主張任何單一國家的計算史可代表全球計算史。
32. 不主張本文已完成對中國、日本、歐洲、美國與其他地區計算委託史的跨國比較。
33. 不主張電子計算機之後的人類計算勞動完全消失。
34. 不主張「computer 曾指人」即可證明 AI 與人具有同一本體地位。
35. 不主張計算委託可以取代政治、經濟、教育與制度分析。

---

# 44. 結論：AI 認知委託不是突然出現，而是計算委託跨過了語義邊界

從算盤到數表，人類首先學會：

$$
\boxed{
\text{把中間狀態放到外面}.
}
$$

從機械計算器到電子計算機，人類進一步學會：

$$
\boxed{
\text{把規則執行放到外面}.
}
$$

從 ENIAC 到超級電腦，人類開始：

$$
\boxed{
\text{把巨大到任何個體無法逐步重算的計算放到外面}.
}
$$

從業務化數值天氣預報到科學模擬，人類又進一步：

$$
\boxed{
\text{把對世界的可操作預測建立在機器計算上}.
}
$$

而 AI 帶來的新階段則是：

$$
\boxed{
\text{把表示、方法選擇、推論與部分解讀也逐步放到外面}.
}
$$

因此，整條歷史可以寫成：

$$
\boxed{
\text{External State}
\rightarrow
\text{External Calculation}
\rightarrow
\text{External Simulation}
\rightarrow
\text{External Inference}
\rightarrow
\text{External Agency}.
}
$$

這不是說 AI 只是另一台計算器。

恰恰相反。

真正的斷點正是：

$$
\boxed{
\text{the external computational system begins to participate in deciding how computation itself should proceed}.
}
$$

所以 AI 的特殊性只有放在這條長歷史裡才會變得清楚。

它既不是：

$$
\text{完全沒有前例},
$$

也不是：

$$
\text{毫無新意}.
$$

它是：

$$
\boxed{
\text{an old human strategy crossing into a new functional layer}.
}
$$

而下一篇 EXS-04 將把這條歷史正式拉進日常社會：

> AI 是什麼時候真正進入手機、個人電腦、汽車、家庭、工業、醫療與其他日常系統的？

研究重點將不再只問「哪一年第一次有 AI」，而區分：

$$
T_{\mathrm{first}},
T_{\mathrm{consumer}},
T_{\mathrm{mass}},
T_{\mathrm{default}},
T_{\mathrm{dependent}}.
$$

這將是從「計算委託史」進入「AI 滲透史」的正式接口。

---

# 參考文獻

[1] Smithsonian National Museum of American History. **The Abacus and the Numeral Frame / Suan-p'an, or Chinese Abacus.** Smithsonian 將算盤描述為透過滑動珠子、石子或計數片進行算術計算的 computing device。本文於 2026-08-18 重新核對。

[2] National Oceanic and Atmospheric Administration (NOAA). **The History of Numerical Weather Prediction.** NOAA 歷史資料記錄 Lewis Fry Richardson 的數值天氣預報、約 64,000 名人類 computers 的 forecast factory 構想，以及 1950 年 ENIAC 完成首批成功數值天氣預報的歷史。本文於 2026-08-18 重新核對。

[3] European Centre for Medium-Range Weather Forecasts (ECMWF). **History.** ECMWF 於 1975 年成立，1979 年開始即時與業務化中期預報，並於 1992 年將 ensemble prediction 納入 operational forecasting system。本文於 2026-08-18 重新核對。

[4] Lawrence Livermore National Laboratory / NNSA Advanced Simulation and Computing. **El Capitan: NNSA's First Exascale Machine.** El Capitan 於 2024 年部署，峰值能力超過 2.79 exaflops；其任務包括核安全與可靠性模擬、材料、高能量密度物理等。本文於 2026-08-18 重新核對。

[5] NOAA National Centers for Environmental Information. **Numerical Weather Prediction.** NOAA 說明 NWP 電腦模型如何使用當前觀測與資料同化產生未來氣象變數預測。

[6] ECMWF. (2025). **ECMWF's AI forecasts become operational.** AIFS Single 於 2025-02-25 進入業務運行，與傳統 physics-based IFS 並行；ECMWF 說明其使用由約 6,000 萬筆品質控制觀測等形成的初始條件，並以學習式模型進行未來天氣推論。

[7] NOAA. (2026). **AI-driven global weather models / Office of Modeling and Development AI/ML Modeling Strategy 2026–2031.** 2026 年 NOAA 將多個 AI 驅動的天氣模型推向 operation，並發布 AI/ML modeling strategy。

[8] **Meta-cognitive insights into cognitive offloading: mechanisms, interventions, and educational implications.** *Humanities and Social Sciences Communications* (2026). 該綜述指出當代 cognitive offloading 研究涵蓋記憶、計算器與統計軟體、決策支援與創意輔助等多類任務。

[9] Gilbert, S. J., Boldt, A., Sachdeva, C., Scarampi, C., & Tsai, P.-C. (2023). **Outsourcing memory to external tools: A review of intention offloading.** *Psychonomic Bulletin & Review*, 30, 60–76.

[10] TOP500. **Performance Development / Timeline.** TOP500 自 1993 年起持續追蹤高效能計算系統性能演化；本文使用其作為 HPC 性能歷史的參照，而不把 LINPACK 排名等同所有科學運算能力。

[11] ECMWF. (2026). **AIFS Machine Learning Data / 2025 Forecast Evaluation.** AIFS deterministic model 自 2025-02-25 業務運行，並於 2026 年持續升級；ECMWF 2026 年評估亦將機器學習預報列為近年重大業務發展之一。

[12] LLNL. **Computing Facilities / Exascale Computing.** LLNL 將 exascale 系統用於高解析模擬、AI、材料、製造與國家安全研究，展示 HPC 已成為科學與工程能力載體的一部分。

---

# 附錄 A｜最小符號表

| 符號 | 意義 |
|---|---|
| $H$ | 人類行動者 |
| $M$ | 外部計算載體 |
| $A$ | AI 系統 |
| $P$ | 問題 |
| $s_i$ | 計算中間狀態 |
| $C_{\mathrm{calc,int}}$ | 內在計算能力 |
| $C_{\mathrm{calc,ext}}$ | 外部計算能力 |
| $\tau_{\mathrm{calc}}$ | 計算時間 |
| $\tau_{\mathrm{phenomenon}}$ | 被預測現象的時間尺度 |
| $R_M$ | 機器運算／事件速率 |
| $R_H$ | 人類可審閱／運算速率 |
| $\Omega_{\mathrm{simulable}}$ | 可模擬狀態空間 |
| $I_H$ | 人類解讀份額的概念變量 |
| $D_{\mathrm{calc}}$ | 計算委託程度 |
| $D_{\mathrm{AI,cog}}$ | AI 認知委託深度 |
| $V_H$ | 人類中間狀態可見度 |
| $B_{\mathrm{digital}}$ | 數位計算／認知頻寬 |
| $B_{\mathrm{reality}}$ | 現實實現頻寬 |

---

# 附錄 B｜EXS-01 → EXS-02 → EXS-03

EXS-01：

$$
\boxed{
\text{Internal Capability}
\neq
\text{Accessible Capability}.
}
$$

EXS-02：

$$
\boxed{
\text{Accessible Capability}
\neq
\text{Resilient Capability}.
}
$$

EXS-03：

$$
\boxed{
\text{Humanly Usable Knowledge}
\neq
\text{Humanly Executed Every Step}.
}
$$

三篇合併：

$$
\boxed{
\text{Capability Externalization}
\rightarrow
\text{Dependency Structure}
\rightarrow
\text{Computational Delegation}.
}
$$

---

# 附錄 C｜從天氣預報看完整歷史鏈

$$
\boxed{
\text{Richardson Human Computers}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{1950 ENIAC Numerical Forecast}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{1979 Operational ECMWF Forecasting}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{1992 Operational Ensemble Prediction}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Supercomputer-Based Earth-System Prediction}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{2025–2026 Operational AI Forecasting}
}
$$

這條歷史的理論意義是：

$$
\boxed{
\text{Calculation Delegation}
\rightarrow
\text{Prediction Delegation}
\rightarrow
\text{Inference Delegation}.
}
$$

---

# 附錄 D｜下一篇接口

**EXS-04｜AI 是什麼時候進入日常世界的？**
**手機、PC、汽車、家庭、醫療、工業與跨國 AI 滲透史**

核心時間型別：

$$
\boxed{
T_{\mathrm{first}}
\neq
T_{\mathrm{consumer}}
\neq
T_{\mathrm{mass}}
\neq
T_{\mathrm{default}}
\neq
T_{\mathrm{dependent}}.
}
$$

下一篇將特別避免「第一個 AI 手機」這類過度簡化的單點歷史敘事，而研究：

$$
\boxed{
\text{AI Penetration as a multi-stage, multi-domain, multi-country process}.
}
$$
