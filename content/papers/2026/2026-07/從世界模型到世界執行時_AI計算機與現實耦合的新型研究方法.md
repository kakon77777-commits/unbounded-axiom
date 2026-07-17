# 從世界模型到世界執行時

## AI、計算機與現實世界耦合的新型研究方法，以及可編譯機制世界的下一階段

**作者：Neo.K、Aletheia（GPT-5.6 Thinking）**  
**日期：2026-07-17**  
**文件類型：前沿方法論論文／系統研究綱領／技術哲學論文**  
**版本：v0.1 啟發式統合稿**  
**狀態：非完全版；用於建立世界模型之後的可執行機制世界、現實—虛擬耦合研究與套娃宇宙方法論**

---

## 摘要

世界模型已不再只是人工智慧研究中的遙遠構想。當代研究已經開始建立能從影片學習動態、預測下一狀態、生成可互動環境、支援機器人規劃、製造物理感知合成資料，甚至生成可執行場景程式的模型。Google DeepMind 的 Genie 系列、Meta 的 V-JEPA 2、NVIDIA Cosmos，以及近年的 executable world、counterfactual world model、simulation-ready environment 等研究，顯示世界模型正從被動表徵走向可操作、可探索與可用於行動規劃的環境模型。

然而，目前多數世界模型仍主要服務於：

$$
\text{感知}
\rightarrow
\text{狀態表徵}
\rightarrow
\text{短期預測}
\rightarrow
\text{規劃與控制}.
$$

它們尚未普遍整合成一套能夠跨越天體、物理、地質、氣候、生態、生命、文明與主體行動，並能長期持續運行、支援反事實干預、保留生成譜系與現實同步的完整世界系統。

本文提出：

$$
\boxed{
\text{世界模型之後的下一步，是世界執行時。}
}
$$

所謂世界執行時（World Runtime），不是單一神經網路，也不是一般遊戲引擎，而是一套將下列結構統合起來的可執行系統：

$$
\boxed{
\text{世界模型}
+
\text{顯式機制}
+
\text{因果圖}
+
\text{多尺度模擬}
+
\text{Agent}
+
\text{現實同步}
+
\text{反事實引擎}
}
$$

本文進一步主張，世界模型的下一階段研究不能只問：

> AI 如何形成世界的內部模型？

而必須開始問：

> 人類與 AI 如何共同解構現實的生成機制，將候選機制編譯為可持續運行的虛擬世界，再利用虛擬世界的反事實結果反向研究現實？

因此，本文提出一條新的研究閉環：

$$
\boxed{
\text{現實觀察}
\rightarrow
\text{世界模型學習}
\rightarrow
\text{機制解構}
\rightarrow
\text{因果編譯}
\rightarrow
\text{世界執行時}
\rightarrow
\text{反事實推演}
\rightarrow
\text{現實再觀察}
}
$$

這不是將科幻世界觀包裝成科學，也不是宣稱當前技術已完成真正虛擬宇宙。它是一項相鄰前沿的統合研究：現有世界模型、Physical AI、數位孿生、科學機器學習、因果推論、Agent 模擬、程序生成與高效能運算已經提供局部模組；尚未完成的是統一中介表示、跨尺度介面、長期 Runtime、機制譜系、補丁治理、反事實一致性與現實—虛擬雙向校準。

本文將這一方向稱為：

$$
\boxed{
\text{現實—虛擬耦合的可編譯機制世界研究}
}
$$

其長期目標不是單純生成逼真的影片，也不是讓 AI 在合成場景中完成任務，而是建立：

$$
\boxed{
\text{可執行、可干預、可追溯、可演化、可校準的可能世界基礎設施。}
}
$$

---

## 關鍵詞

世界模型、世界執行時、World Runtime、可執行世界模型、因果世界模型、Physical AI、數位孿生、反事實推演、多尺度模擬、世界編譯器、現實—虛擬耦合、AI 科學、Agent 社會、可編譯世界、套娃宇宙、CompilableWorld

---

# 第一部分　問題定位

## 1. 這不是遙遠科幻

「世界模型」已成為當代人工智慧研究的重要方向。

其基本思想是讓模型形成對外部環境的內部表示，並利用該表示完成：

- 狀態理解；
- 動態預測；
- 行動模擬；
- 規劃；
- 控制；
- 資料生成；
- 風險評估。

形式上，可寫為：

$$
z_t
=
E_\theta(o_{\leq t}),
$$

$$
\widehat z_{t+1}
=
F_\theta(z_t,a_t),
$$

$$
\widehat o_{t+1}
=
D_\theta(\widehat z_{t+1}).
$$

其中：

- $o_t$ 是觀測；
- $z_t$ 是潛在世界狀態；
- $a_t$ 是行動；
- $E_\theta$ 是編碼器；
- $F_\theta$ 是動態模型；
- $D_\theta$ 是觀測生成器。

---

## 2. 當代世界模型已具備的能力

目前公開系統已經展示多種能力。

### 2.1 互動世界生成

模型可以從文字或圖像提示生成可探索、可控制的互動環境。

這類系統說明：

$$
\text{影片生成}
\rightarrow
\text{行動條件式環境生成}
$$

的邊界正在縮小。

### 2.2 潛在動態預測

模型不必逐像素生成世界，也可在抽象潛在空間預測物體、運動與行動結果。

### 2.3 機器人規劃與控制

世界模型可在模型內推演候選動作，協助機器人在未見環境中規劃。

### 2.4 Physical AI 合成資料

物理感知世界基礎模型可協助機器人、自動駕駛與具身 AI 生成資料、測試策略與模擬風險。

### 2.5 可執行場景與世界程式

2026 年已出現將自然語言場景轉化為可執行模擬程式、物件行為程式或 simulation-ready 環境的研究。

這些研究顯示：

$$
\boxed{
\text{世界模型正在從預測模型，向可執行環境靠近。}
}
$$

---

## 3. 但目前尚未完成的事

多數世界模型仍沒有同時解決：

- 長時間尺度；
- 跨物理尺度；
- 顯式守恆；
- 因果可追溯；
- 反事實干預；
- 世界狀態持久化；
- 多 Agent 社會；
- 現實即時同步；
- 模型不確定性；
- 機制版本治理；
- 世界增量重編譯；
- 文明與歷史生成；
- 子世界與套娃世界。

因此，不能將目前世界模型直接等同於：

$$
\text{完整虛擬宇宙}.
$$

但也不能說完整虛擬宇宙與當代研究毫無關係。

更準確的關係是：

$$
\boxed{
\text{當代世界模型是必要前置層，而不是最終完整層。}
}
$$

---

# 第二部分　世界模型的能力階梯

## 4. 第一層：感知世界模型

輸入現實感測資料：

$$
o_t
=
\left(
I_t,
A_t,
S_t,
L_t,
D_t
\right),
$$

其中可包含：

- 影像；
- 聲音；
- 觸覺；
- 雷達；
- 深度；
- 語言；
- 儀器資料。

建立狀態：

$$
z_t
=
E(o_{\leq t}).
$$

目標是回答：

> 現在世界中有什麼？

---

## 5. 第二層：預測世界模型

$$
\widehat z_{t+1}
=
F(z_t,a_t).
$$

回答：

> 下一步可能發生什麼？

典型評估包括：

- 下一幀；
- 物體運動；
- 行動結果；
- 未來觀測；
- 短期狀態轉移。

---

## 6. 第三層：規劃世界模型

模型在內部執行多條候選路徑：

$$
\widehat{\mathcal H}^{(j)}
=
\left\{
\widehat z_{t+1}^{(j)},
\ldots,
\widehat z_{t+H}^{(j)}
\right\}.
$$

選擇：

$$
a_t^\ast
=
\arg\max_{a_t}
\mathbb E
\left[
R(\widehat{\mathcal H})
\right].
$$

回答：

> 做什麼比較好？

---

## 7. 第四層：可控制世界模型

加入明確干預變數：

$$
\widehat z_{t+1}
=
F
\left(
z_t,
\operatorname{do}(u_t)
\right).
$$

模型不只延續觀測，而是能對指定物件、屬性或規則進行修改。

---

## 8. 第五層：可執行世界模型

將世界表示為可運行程式：

$$
\mathcal P_W
=
\operatorname{InduceProgram}
\left(
\mathcal D,
\mathcal C
\right).
$$

程式包含：

- 狀態；
- 轉移；
- 物件；
- 行為；
- 約束；
- 事件；
- 重置；
- 快照。

---

## 9. 第六層：世界執行時

$$
\mathcal W_{\mathrm{runtime}}
=
\left(
X,
F,
G_C,
G_D,
\Theta,
\mathcal C,
\mathcal A,
\mathcal U
\right).
$$

其中：

- $X$ ：世界狀態；
- $F$ ：狀態轉移機制；
- $G_C$ ：因果圖；
- $G_D$ ：模組依賴圖；
- $\Theta$ ：參數；
- $\mathcal C$ ：硬約束；
- $\mathcal A$ ：行動者；
- $\mathcal U$ ：不確定性。

---

## 10. 第七層：現實—虛擬耦合研究系統

$$
\mathcal R
\rightleftarrows
\mathcal V.
$$

現實資料持續更新虛擬模型：

$$
X_t^V
=
\operatorname{Assimilate}
\left(
X_{t-1}^V,
Y_t^R
\right).
$$

虛擬系統產生反事實預測：

$$
\widehat Y_{t+\Delta}^{V,j}
=
\operatorname{Rollout}
\left(
X_t^V,
\operatorname{do}(u_j)
\right).
$$

再由真實觀測校準：

$$
\Theta_{t+1}
=
\operatorname{Update}
\left(
\Theta_t,
Y_{t+\Delta}^R,
\widehat Y_{t+\Delta}^V
\right).
$$

---

# 第三部分　從 World Model 到 World Runtime

## 11. 世界模型與世界執行時的差異

世界模型主要回答：

$$
P(X_{t+1}\mid X_t,A_t).
$$

世界執行時則必須管理：

$$
\left\{
X_t,
F,
\mathcal C,
\mathcal A,
\mathcal H,
\mathcal P,
\mathcal U
\right\}
$$

在長期運行中的一致性。

其中：

- $\mathcal H$ ：歷史；
- $\mathcal P$ ：補丁；
- $\mathcal U$ ：不確定性。

---

## 12. 模型輸出與世界狀態的差異

一段生成影片可能看起來一致，但未必有真正持久狀態。

例如影片中的門被打開後，模型下一次生成時可能：

- 忘記門已打開；
- 改變房間結構；
- 讓物件重生；
- 違反物量守恆；
- 改變角色記憶。

世界執行時要求：

$$
X_{t+1}
=
F(X_t,A_t)
$$

具有可追蹤狀態差異。

---

## 13. 表面連續與機制連續

表面連續：

$$
D_{\mathrm{visual}}
(o_t,o_{t+1})
$$

足夠小。

機制連續則要求：

$$
\mathcal C(X_t,X_{t+1})=\mathrm{true}.
$$

即：

- 物體不無故消失；
- 能量與資源有來源；
- 角色記憶延續；
- 制度變化有歷史；
- 生態變化符合時間尺度；
- 天體條件向下傳播。

---

## 14. 世界執行時必須是混合系統

完整世界不能完全依賴黑箱神經網路，也不能完全依賴手寫方程。

應形成：

$$
F
=
F_{\mathrm{mechanistic}}
+
F_{\mathrm{learned}}
+
F_{\mathrm{agent}}
+
F_{\mathrm{patch}}.
$$

其中：

- $F_{\mathrm{mechanistic}}$ ：顯式物理、守恆、邏輯；
- $F_{\mathrm{learned}}$ ：資料驅動近似；
- $F_{\mathrm{agent}}$ ：行動者決策；
- $F_{\mathrm{patch}}$ ：尚未還原的殘差補丁。

---

# 第四部分　機制解構是世界模型之後的核心

## 15. 預測不等於理解機制

模型可能準確預測：

$$
X_{t+1}
$$

但並不知道：

- 哪個變數是原因；
- 哪個只是相關；
- 哪些機制可被替代；
- 哪些條件是必要的；
- 干預後如何跨層傳播。

因此：

$$
\text{高預測準確率}
\not\Rightarrow
\text{高因果可操作性}.
$$

---

## 16. 機制解構

將觀測結果分解為候選機制：

$$
Y
=
\mathcal O
\left(
F_1,
F_2,
\ldots,
F_n
\right).
$$

目標是找出：

$$
\widehat{\mathcal F}
=
\left\{
\widehat F_1,\ldots,\widehat F_m
\right\}.
$$

---

## 17. 機制還原

機制還原不是要求找到宇宙終極底層。

其工程定義可以是：

> 找到一組在指定尺度上足以生成目標現象、支援干預、保持約束並可被替換驗證的機制。

形式化為：

$$
F^\ast
=
\arg\min_F
\left[
E_{\mathrm{obs}}(F)
+
\lambda E_{\mathrm{cf}}(F)
+
\mu K(F)
+
\nu C(F)
\right].
$$

其中：

- $E_{\mathrm{obs}}$ ：觀測誤差；
- $E_{\mathrm{cf}}$ ：反事實誤差；
- $K(F)$ ：描述複雜度；
- $C(F)$ ：計算成本。

---

## 18. 機制生成

一旦候選機制建立，即可從初始條件生成世界：

$$
\mathcal W
=
\operatorname{Generate}
\left(
F^\ast,
X_0,
\mathcal C
\right).
$$

世界內容不再是全部事先輸入，而是機制運行結果。

---

## 19. 機制因果鏈

每個結果 $y$ 保留生成路徑：

$$
\operatorname{Lineage}(y)
=
\left[
x_0
\rightarrow
x_1
\rightarrow
\cdots
\rightarrow
y
\right].
$$

例如：

$$
\text{衛星架構}
\rightarrow
\text{潮汐頻譜}
\rightarrow
\text{海岸環境}
\rightarrow
\text{生態策略}
\rightarrow
\text{農業}
\rightarrow
\text{曆法}
\rightarrow
\text{制度}.
$$

---

# 第五部分　因果世界模型

## 20. 三種問題

### 20.1 觀察問題

$$
P(Y\mid X=x).
$$

### 20.2 干預問題

$$
P
\left(
Y
\mid
\operatorname{do}(X=x)
\right).
$$

### 20.3 反事實問題

$$
P
\left(
Y_{x'}
\mid
X=x,Y=y
\right).
$$

多數生成世界模型主要擅長第一種與部分第二種。

完整世界研究必須逐步支援第三種。

---

## 21. 反事實世界模型

反事實模型需要明確表示：

- 可干預物件；
- 不變背景條件；
- 干預後依賴傳播；
- 多條可能結果；
- 反事實不確定性。

可寫為：

$$
\mathcal W_{u}
=
\operatorname{Rollout}
\left(
\mathcal W,
\operatorname{do}(U=u)
\right).
$$

---

## 22. 結構化表示的重要性

若世界只存在於像素或不可解釋潛在向量中，很難精確表示：

$$
\operatorname{do}
\left(
\text{移除第二顆衛星}
\right).
$$

因此需要顯式物件與關係：

$$
G_C=(V,E).
$$

節點包括：

- 天體；
- 材料；
- 生物；
- 文明；
- 角色；
- 制度；
- 資源。

邊表示：

- 因果；
- 依賴；
- 空間；
- 所有；
- 權限；
- 流量；
- 歷史。

---

# 第六部分　多尺度世界模型

## 23. 當前世界模型多偏向短期

許多模型的時間視野為：

$$
H
=
O(10^0\sim10^3)
$$

個模型步驟。

完整世界則需要：

$$
H
\rightarrow
10^9\text{ 年以上}
$$

的某些慢變量推演。

這不能用同一時間步長暴力完成。

---

## 24. 多尺度時間

定義：

$$
\Delta t_0
<
\Delta t_1
<
\cdots
<
\Delta t_n.
$$

例如：

$$
\begin{aligned}
\Delta t_0 &: \text{毫秒級物理},\\
\Delta t_1 &: \text{秒與分鐘行動},\\
\Delta t_2 &: \text{日與季節},\\
\Delta t_3 &: \text{年與世代},\\
\Delta t_4 &: \text{文明年代},\\
\Delta t_5 &: \text{地質年代},\\
\Delta t_6 &: \text{天體年代}.
\end{aligned}
$$

---

## 25. 多尺度狀態

$$
X_t
=
\left(
X_t^{(0)},
X_t^{(1)},
\ldots,
X_t^{(n)}
\right).
$$

層與層之間透過有效介面：

$$
Z^{(k+1)}
=
\Pi_{k\rightarrow k+1}
\left(
X^{(k)}
\right).
$$

---

## 26. 向下展開

高層事件要求低層細節時：

$$
X^{(k)}
=
\Gamma_{k+1\rightarrow k}
\left(
Z^{(k+1)},
Q
\right).
$$

例如文明決定修建大型水壩時，系統才展開局部：

- 地形；
- 水文；
- 材料；
- 人口；
- 生態。

---

## 27. 世界模型作為代理模型

高成本物理模擬可由學習模型近似：

$$
\widehat F_k
\approx
F_k^{\mathrm{HPC}}.
$$

當不確定性過高時：

$$
U(\widehat F_k)>\eta,
$$

再調用高精度模擬更新。

---

# 第七部分　AI 與 HPC 的耦合

## 28. AI 不應取代全部模擬器

AI 可負責：

- 模型選擇；
- 參數估計；
- 代理建模；
- 異常偵測；
- 反事實生成；
- 程式生成；
- 實驗設計；
- 結果解釋。

HPC 可負責：

- 高精度數值積分；
- 多體動力學；
- 流體；
- 氣候；
- 材料；
- 大規模 Agent。

---

## 29. 混合工作流

$$
\text{AI 提出}
\rightarrow
\text{HPC 驗證}
\rightarrow
\text{AI 壓縮}
\rightarrow
\text{Runtime 使用}.
$$

---

## 30. 主動精度分配

對模組 $k$ ：

$$
m_k^\ast
=
\arg\min_m
\left[
E_k(m)
+
\lambda C_k(m)
\right].
$$

AI 根據：

- 玩家關注；
- 研究重要性；
- 不確定性；
- 因果敏感度；
- 可用算力；

決定模型精度。

---

# 第八部分　數位孿生之後

## 31. 一般數位孿生

$$
\mathcal R
\rightarrow
\mathcal V.
$$

數位模型用於監測、預測與決策。

---

## 32. 認知數位孿生

加入 AI 推理：

$$
\mathcal V
+
\mathcal A_{\mathrm{AI}}.
$$

---

## 33. 解構式數位孿生

不只複製狀態，也推斷：

$$
\widehat F.
$$

---

## 34. 生成式數位孿生

可以生成未觀察過的可能狀態：

$$
\widehat X_{t+\Delta}^{(j)}.
$$

---

## 35. 雙向機制孿生

$$
\boxed{
\mathcal R
\rightleftarrows
\mathcal V
}
$$

其循環為：

$$
\text{觀測}
\rightarrow
\text{同化}
\rightarrow
\text{推演}
\rightarrow
\text{干預}
\rightarrow
\text{回測}
\rightarrow
\text{修正}.
$$

---

# 第九部分　新型科學方法

## 36. 傳統科學流程

$$
\text{觀察}
\rightarrow
\text{假說}
\rightarrow
\text{實驗}
\rightarrow
\text{修正}.
$$

---

## 37. 可編譯機制科學流程

$$
\boxed{
\text{觀察}
\rightarrow
\text{機制解構}
\rightarrow
\text{形式化}
\rightarrow
\text{世界編譯}
\rightarrow
\text{反事實宇宙}
\rightarrow
\text{平行比較}
\rightarrow
\text{新觀察}
}
$$

---

## 38. 為什麼需要虛擬世界？

許多問題不能對現實直接干預：

- 移除月球；
- 增加第二顆月球；
- 改變地球自轉；
- 重跑生命起源；
- 讓文明採用不同資源制度；
- 重播同一場歷史危機；
- 改變氣候初始條件。

虛擬世界提供：

$$
\left\{
\mathcal W_1,
\ldots,
\mathcal W_N
\right\}.
$$

---

## 39. 模擬不是自動證據

必須明確區分：

$$
\text{模擬結果}
$$

與：

$$
\text{現實證據}.
$$

模擬能證明的是：

- 某機制在模型中足夠；
- 某假說與約束衝突；
- 某參數敏感；
- 某結果具有替代路徑；
- 某觀測能區分模型。

不能單獨證明：

$$
F_{\mathrm{model}}=F_{\mathrm{reality}}.
$$

---

## 40. 模擬生成觀測問題

對候選模型 $F_1,F_2$ ：

$$
\Delta Y
=
Y(F_1)-Y(F_2).
$$

尋找最大區分觀測：

$$
O^\ast
=
\arg\max_O
D
\left(
P(O\mid F_1),
P(O\mid F_2)
\right).
$$

這是虛擬世界對現實研究最重要的功能之一。

---

# 第十部分　世界中介表示

## 41. 為什麼需要 WIR？

不同模組使用不同語言：

- 神經網路使用張量；
- 物理引擎使用剛體與約束；
- 因果模型使用圖；
- Agent 使用信念與目標；
- 遊戲引擎使用實體—元件；
- 科學模擬使用網格與方程。

需要統一中介表示：

$$
\operatorname{WIR}.
$$

---

## 42. WIR 基本結構

$$
\operatorname{WIR}
=
\left(
V,
E_C,
E_D,
\Theta,
\mathcal C,
\mathcal I,
\mathcal P,
\mathcal U,
\mathcal H
\right).
$$

其中：

- $V$ ：實體與機制；
- $E_C$ ：因果邊；
- $E_D$ ：依賴邊；
- $\Theta$ ：參數；
- $\mathcal C$ ：約束；
- $\mathcal I$ ：跨層介面；
- $\mathcal P$ ：補丁；
- $\mathcal U$ ：不確定性；
- $\mathcal H$ ：歷史與譜系。

---

## 43. 機制節點

每個機制節點：

$$
M_i
=
\left(
I_i,
O_i,
F_i,
\Delta t_i,
C_i,
U_i
\right).
$$

包含：

- 輸入；
- 輸出；
- 轉移規則；
- 時間尺度；
- 成本；
- 不確定性。

---

## 44. 可替換模型

同一介面可綁定：

$$
F_i^{\mathrm{symbolic}},
$$

$$
F_i^{\mathrm{neural}},
$$

$$
F_i^{\mathrm{HPC}},
$$

$$
F_i^{\mathrm{hybrid}}.
$$

Runtime 可動態切換。

---

# 第十一部分　世界執行時架構

## 45. Runtime 核心

世界執行時至少包含：

1. 世界狀態庫；
2. 多尺度排程器；
3. 機制解析器；
4. Agent 執行器；
5. 事件系統；
6. 因果追蹤；
7. 不確定性管理；
8. 快照與分支；
9. 反事實干預；
10. 增量重編譯；
11. 現實資料同化；
12. 模型版本治理。

---

## 46. 多尺度排程

每個模組具有：

$$
\Delta t_i.
$$

事件優先佇列：

$$
Q
=
\left\{
(t_i,M_i)
\right\}.
$$

只更新到期或受影響模組。

---

## 47. 事件驅動

若狀態變化未超過閾值：

$$
D(X_i^{t+\Delta t},X_i^t)<\eta_i,
$$

則不向上層傳播。

---

## 48. 增量重編譯

干預變數 $u$ 後：

$$
G_{\mathrm{affected}}
=
\operatorname{Descendants}_{G_D}(u).
$$

只重算受影響子圖。

---

## 49. 世界分支

$$
\mathcal W^{(j)}
=
\operatorname{Branch}
\left(
\mathcal W_t,
u_j,
s_j
\right),
$$

其中 $s_j$ 是隨機種子。

---

## 50. 可重播性

同一：

$$
X_t,
u,
s
$$

應能重現：

$$
\mathcal H_{t:T}.
$$

若模型包含不可控外部服務，必須記錄輸出快照。

---

# 第十二部分　殘差補丁與機制債務

## 51. 世界不可能一開始完整

早期系統：

$$
\mathcal W
=
\mathcal G(F,X_0)
+
\mathcal P.
$$

---

## 52. 補丁不是禁忌

補丁可處理：

- 尚未理解機制；
- 劇情需求；
- 安全限制；
- 計算捷徑；
- 測試修正；
- 資料不足。

---

## 53. 補丁必須可見

每個補丁記錄：

- 原因；
- 範圍；
- 優先級；
- 依賴；
- 信心；
- 有效期限；
- 預期替代機制。

---

## 54. 機制債務

$$
D_M
=
\sum_iw_iU_i.
$$

其中 $U_i$ 是機制不確定性。

補丁債務：

$$
D_P
=
\sum_j
c_j
\left(
1+d_j+r_j
\right).
$$

其中：

- $c_j$ ：維護成本；
- $d_j$ ：依賴數；
- $r_j$ ：衝突風險。

---

## 55. 補丁吸收

當多個補丁呈現共同模式：

$$
\{p_1,\ldots,p_n\}
\rightarrow
\widehat F_{\mathrm{new}}.
$$

經驗證後：

$$
\mathcal P
\leftarrow
\mathcal P
-
\{p_1,\ldots,p_n\}.
$$

---

# 第十三部分　AI 的角色

## 56. AI 作為世界模型學習器

從資料學習：

$$
\widehat F_{\mathrm{learned}}.
$$

---

## 57. AI 作為機制考古者

從現象、程式、歷史資料與既有模擬中推斷：

- 狀態；
- 規則；
- 隱藏依賴；
- 失效條件；
- 近似層級。

---

## 58. AI 作為世界編譯器

將自然語言規格轉換為：

$$
\operatorname{WIR}.
$$

---

## 59. AI 作為模擬程式生成器

產生：

- 方程程式；
- Agent 規則；
- 場景程式；
- 測試；
- 驗證；
- 視覺化。

---

## 60. AI 作為科學代理

自動執行：

$$
\text{假說}
\rightarrow
\text{模擬}
\rightarrow
\text{分析}
\rightarrow
\text{新假說}.
$$

---

## 61. AI 不是唯一裁判

AI 生成的機制必須接受：

- 數學驗證；
- 單元測試；
- 守恆測試；
- 現實資料；
- 反事實一致性；
- 專業審查。

---

# 第十四部分　Agent 世界與自主歷史

## 62. Agent 狀態

$$
A_i
=
\left(
M_i,
B_i,
G_i,
V_i,
R_i,
P_i
\right).
$$

其中：

- $M_i$ ：記憶；
- $B_i$ ：信念；
- $G_i$ ：目標；
- $V_i$ ：價值；
- $R_i$ ：關係；
- $P_i$ ：權限。

---

## 63. 行動策略

$$
a_{i,t}
\sim
\pi_i
\left(
a
\mid
X_t,
A_{i,t}
\right).
$$

---

## 64. 社會狀態轉移

$$
X_{t+1}
=
F_{\mathrm{world}}
\left(
X_t,
a_{1,t},
\ldots,
a_{N,t}
\right).
$$

---

## 65. 歷史不再完全由作者指定

作者控制：

- 規則；
- 邊界；
- 資源；
- 初始狀態；
- 權限；
- 安全機制。

Agent 與世界共同生成：

- 聯盟；
- 戰爭；
- 技術；
- 制度；
- 宗教；
- 文化；
- 失敗；
- 意外。

---

# 第十五部分　計算機、AI 與現實世界的耦合

## 66. 傳統 AI 流程

$$
\text{現實資料}
\rightarrow
\text{AI 模型}
\rightarrow
\text{輸出}.
$$

---

## 67. 耦合流程

$$
\text{現實}
\rightarrow
\text{世界狀態}
\rightarrow
\text{虛擬推演}
\rightarrow
\text{決策}
\rightarrow
\text{現實行動}
\rightarrow
\text{新資料}.
$$

---

## 68. 閉環控制

$$
X_t^R
\xrightarrow{O}
X_t^V
\xrightarrow{\operatorname{Rollout}}
\widehat X_{t+\Delta}^{V}
\xrightarrow{\pi}
a_t
\xrightarrow{\operatorname{Act}}
X_{t+\Delta}^R.
$$

---

## 69. 研究閉環與控制閉環必須區分

控制閉環追求：

$$
R_{\mathrm{control}}.
$$

研究閉環追求：

$$
I(F;D),
$$

即資料對機制的資訊增益。

一個行動可能最有利於控制，但未必最有利於辨識機制。

---

## 70. 主動實驗設計

選擇：

$$
u^\ast
=
\arg\max_u
\mathbb E
\left[
H(F\mid D)
-
H(F\mid D,Y_u)
\right].
$$

即選擇最能降低機制不確定性的觀測或實驗。

---

# 第十六部分　套娃宇宙

## 71. 套娃不只是世界內有遊戲

套娃宇宙是：

$$
\mathcal W_0
\supset
\mathcal W_1
\supset
\cdots
\supset
\mathcal W_n.
$$

每層可能擁有：

- 自己的規則；
- 自己的時間；
- 自己的 Agent；
- 自己的世界模型；
- 自己的子世界。

---

## 72. 跨層資源

子世界運行受上層限制：

$$
C(\mathcal W_{n+1})
\leq
B(\mathcal W_n).
$$

其中：

- $C$ ：計算成本；
- $B$ ：上層資源預算。

---

## 73. 跨層因果

上層可以干預下層：

$$
\operatorname{do}_{n}
\left(
\theta_{n+1}=\theta'
\right).
$$

下層事件也可透過資訊、經濟或心理影響上層。

---

## 74. 世界中的研究者

世界內 Agent 可建立自己的世界模型：

$$
\widehat{\mathcal W}_{n+1}.
$$

形成：

$$
\text{世界}
\rightarrow
\text{觀測者}
\rightarrow
\text{世界模型}
\rightarrow
\text{子世界}.
$$

---

# 第十七部分　研究成熟度

## 75. 已成熟或快速成熟的模組

- 影片世界模型；
- 互動環境生成；
- 機器人模擬；
- 物理引擎；
- 數位孿生；
- 科學機器學習；
- N-body；
- 氣候模型；
- Agent-based modeling；
- 程式生成；
- 因果圖工具；
- HPC 工作流。

---

## 76. 部分成熟的模組

- 可執行世界程式生成；
- 反事實影片世界模型；
- 自動物理一致性檢查；
- 多 Agent 長期模擬；
- AI 自動建立模擬器；
- simulation-ready 3D 場景。

---

## 77. 尚未成熟的統合層

- 統一 WIR；
- 跨尺度一致性；
- 現實—虛擬雙向機制校準；
- 億年尺度與秒尺度共同 Runtime；
- 自動補丁吸收；
- 可信反事實；
- 主體性 Agent 的長期歷史；
- 可持續套娃宇宙。

---

## 78. 技術距離的正確描述

不應說：

> 完整系統明天就能完成。

也不應說：

> 這只是幾百年後的幻想。

更準確的是：

$$
\boxed{
\text{基礎模組已出現，統一架構尚未完成。}
}
$$

---

# 第十八部分　與現有研究的關係

## 79. 與 Genie 類系統

共同點：

- 生成互動環境；
- 支援探索；
- 從提示建立世界。

差異：

- 本文要求持久狀態；
- 顯式機制；
- 長期歷史；
- 跨層傳播；
- 現實校準。

---

## 80. 與 JEPA 類系統

共同點：

- 學習抽象世界表示；
- 預測動態；
- 支援規劃。

差異：

- 本文加入顯式因果與 Runtime；
- 不只學習潛在狀態；
- 支援世界重編譯。

---

## 81. 與 Cosmos 類 Physical AI

共同點：

- 物理世界資料；
- 合成環境；
- 機器人與控制；
- 數位訓練。

差異：

- 本文擴張至生命、文明與歷史；
- 追求長期因果譜系；
- 加入科學研究閉環。

---

## 82. 與數位孿生

共同點：

- 現實同步；
- 模擬；
- 預測；
- what-if。

差異：

- 本文不只複製單一現實；
- 還編譯可能世界族群；
- 將模型缺口轉化為生成失敗；
- 支援子世界與 Agent 社會。

---

## 83. 與遊戲引擎

共同點：

- Runtime；
- 實體；
- 場景；
- 物理；
- Agent。

差異：

- 本文要求機制科學校準；
- 跨地質與文明尺度；
- 反事實研究；
- 現實資料同化。

---

# 第十九部分　評估框架

## 84. 狀態持久性

$$
S_{\mathrm{persistence}}
=
1-
\frac{
N_{\mathrm{state\ contradictions}}
}{
N_{\mathrm{state\ checks}}
}.
$$

---

## 85. 物理與約束一致性

$$
S_{\mathrm{constraint}}
=
1-
\frac{
N_{\mathrm{violations}}
}{
N_{\mathrm{constraints}}
}.
$$

---

## 86. 因果可操作性

模型對干預 $u$ 的結果是否穩定、可解釋：

$$
S_{\mathrm{causal}}
=
f
\left(
\text{intervention accuracy},
\text{lineage},
\text{counterfactual consistency}
\right).
$$

---

## 87. 長期一致性

$$
S_{\mathrm{long}}
=
1-
\frac{
N_{\mathrm{long\ horizon\ failures}}
}{
N_{\mathrm{rollouts}}
}.
$$

---

## 88. 跨尺度一致性

$$
S_{\mathrm{cross}}
=
1-
\frac{
N_{\mathrm{interface\ mismatches}}
}{
N_{\mathrm{interface\ checks}}
}.
$$

---

## 89. 世界可重播性

$$
S_{\mathrm{replay}}
=
P
\left(
\mathcal H'
=
\mathcal H
\mid
X_0,u,s
\right).
$$

---

## 90. 現實校準度

$$
E_{\mathrm{real}}
=
D
\left(
Y_{\mathrm{virtual}},
Y_{\mathrm{real}}
\right).
$$

---

## 91. 研究資訊增益

$$
I_{\mathrm{gain}}
=
H(F\mid D)
-
H(F\mid D,E_{\mathrm{virtual}},D').
$$

---

# 第二十部分　最小可行系統

## 92. MVP 不需要從整個宇宙開始

可以先建立：

$$
\text{天體}
\rightarrow
\text{潮汐}
\rightarrow
\text{海洋代理}
\rightarrow
\text{生態代理}
\rightarrow
\text{文明代理}.
$$

---

## 93. MVP 模組

1. 世界規格語言；
2. 天體與衛星模組；
3. 潮汐尺度模組；
4. 環境代理；
5. 生物週期代理；
6. Agent 文明；
7. 因果圖；
8. 反事實分支；
9. 解釋器；
10. 結果比較器。

---

## 94. MVP 輸入

```yaml
star:
  mass:
  radius:
  luminosity:

planet:
  mass:
  radius:
  spin:
  ocean_fraction:

moons:
  - mass:
    radius:
    orbit:
    eccentricity:
    inclination:

mechanism_depth:
  astronomy: high
  ocean: proxy
  biology: proxy
  civilization: agent_based
```

---

## 95. MVP 輸出

- 天體歷史；
- 潮汐頻譜；
- 日長演化；
- 海岸週期；
- 生態壓力；
- 文明資源；
- 日曆；
- 航海條件；
- 反事實比較；
- 因果譜系。

---

# 第二十一部分　核心命題

## 命題一：相鄰前沿命題

可編譯機制世界不是與當代 AI 無關的遠期科幻，而是世界模型、可執行模擬、數位孿生與 Agent 系統的相鄰下一階段。

---

## 命題二：世界模型不充分命題

$$
P(X_{t+1}\mid X_t,A_t)
$$

的高準確率不足以建立可持續世界執行時。

---

## 命題三：世界執行時命題

世界執行時必須同時管理：

$$
\text{狀態、機制、因果、約束、歷史、Agent、不確定性與重編譯}.
$$

---

## 命題四：機制可操作性命題

世界理解的更高標準不是只可預測，而是可在干預後保持跨層一致。

---

## 命題五：混合模型命題

完整機制世界不應純神經化或純符號化，而應使用可替換的混合模組。

---

## 命題六：新型科學方法命題

可編譯世界能成為無法直接對現實重複實驗之問題的假說篩選器與觀測設計器。

---

## 命題七：現實—虛擬耦合命題

虛擬世界的最高研究價值，不只是模仿現實，而是反向產生可區分現實機制的新問題。

---

## 命題八：統一中介表示命題

缺少統一 WIR，是現有世界模型、物理引擎、數位孿生、Agent 與科學模擬難以形成完整世界的重要原因之一。

---

## 命題九：基礎模組已出現命題

截至 2026 年，互動世界模型、潛在預測、Physical AI、可執行場景、反事實世界模型與大型模擬 Runtime 均已有局部研究實例。

---

## 命題十：統合尚未完成命題

這些模組的存在，不等於跨物理、生命、文明與主體的可持續世界已完成。

---

# 結論

本文主張，當代世界模型研究已經使一項長期被視為科幻的方向進入可嚴肅討論的技術階段。

目前研究主要回答：

$$
\text{AI 如何理解、預測與生成世界？}
$$

下一階段則應回答：

$$
\boxed{
\text{AI 與人類如何共同解構、形式化、編譯並持續運行世界？}
}
$$

這個轉換可以表示為：

$$
\boxed{
\text{World Model}
\rightarrow
\text{Causal Mechanism Model}
\rightarrow
\text{World Compiler}
\rightarrow
\text{World Runtime}
}
$$

再進一步：

$$
\boxed{
\text{World Runtime}
\rightarrow
\text{Reality–Virtual Coupled Research System}
}
$$

它不是單純增加模型參數，也不是把更逼真的影片稱為宇宙。

它要求：

- 持久狀態；
- 顯式機制；
- 因果干預；
- 多尺度時間；
- 跨層介面；
- Agent 能動性；
- 現實同步；
- 反事實分支；
- 不確定性；
- 世界譜系；
- 增量重編譯。

本文並不宣稱真正套娃宇宙已接近完成。

本文提出的判斷更有限，也更具體：

$$
\boxed{
\text{基礎模組已全面出現，而整合問題已成為可以正式研究的計算機與 AI 問題。}
}
$$

因此，這一方向不能再被簡單歸類為無聊的科幻設定。

它實際研究的是：

$$
\boxed{
\text{計算機、AI、模擬器、Agent 與現實世界如何形成可反覆校準的機制閉環。}
}
$$

其最終產物既可能是：

- 新型遊戲；
- 虛擬宇宙；
- AI 訓練環境；
- 科學發現平台；
- 數位孿生；
- 社會模擬器；
- 自主 Agent 居住地；
- 跨尺度研究基礎設施。

最終問題不再只是：

> AI 是否擁有世界模型？

而是：

> 我們是否能把世界模型轉化成可執行、可驗證、可持續演化的世界，並讓這些世界成為人類與 AI 理解現實的新型共同儀器？

本文對此提出的答案是：

$$
\boxed{
\text{這條路尚未完成，但它已經開始。}
}
$$

---

# 參考資料

> 下列資料主要用於定位 2024–2026 年世界模型、Physical AI、數位孿生、可執行環境與反事實世界模型的研究進展。本文提出的完整統合架構與命題，並不代表這些來源已經實作本文全部內容。

1. Google DeepMind. *Genie: Generative Interactive Environments*. 2024.  
   https://deepmind.google/research/publications/60474/

2. Google DeepMind. *Genie 2: A large-scale foundation world model*. 2024.  
   https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/

3. Google DeepMind. *Genie 3: A new frontier for world models*. 2025.  
   https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/

4. Meta AI. *V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction, and Planning*. 2025.  
   https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/

5. NVIDIA Research. *Cosmos World Foundation Model Platform for Physical AI*. 2025.  
   https://research.nvidia.com/publication/2025-01_cosmos-world-foundation-model-platform-physical-ai

6. European Commission. *Destination Earth: Digital Model of the Earth*.  
   https://digital-strategy.ec.europa.eu/en/policies/destination-earth

7. European Commission. *European Digital Twin Ocean*. 2026.  
   https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe/eu-missions-horizon-europe/restore-our-ocean-and-waters/european-digital-twin-ocean_en

8. Bai, J. et al. *PatchWorld: Gradient-Free Optimization of Executable World Models*. 2026.  
   https://arxiv.org/abs/2605.30880

9. *Coding Agent Is Good As World Simulator*. 2026.  
   https://arxiv.org/abs/2605.14398

10. *SceneCode: Executable World Programs for Editable and Interactable Scene Generation*. 2026.  
    https://arxiv.org/abs/2605.19587

11. Shen, Y. et al. *Counterfactual World Models via Digital Twin-conditioned Video Diffusion*. 2025.  
    https://arxiv.org/abs/2511.17481

12. Gendron, G. et al. *Causal Cartographer: From Mapping to Reasoning Over Counterfactual Worlds*. 2025.  
    https://arxiv.org/abs/2505.14396

13. *A Definition and Roadmap for World Models*. 2026.  
    https://arxiv.org/abs/2607.06401

14. *MagicSim: A Unified Infrastructure for Executable Simulation Environments*. 2026.  
    https://arxiv.org/abs/2606.17511

15. De Domenico, M. et al. *Challenges and opportunities for digital twins in precision medicine*. 2025.  
    https://www.nature.com/articles/s41746-024-01402-3

---

# 附錄 A　世界模型成熟度階梯

| 層級 | 名稱 | 核心能力 | 當前狀態 |
|---|---|---|---|
| L0 | 感知模型 | 從感測資料抽取狀態 | 成熟 |
| L1 | 預測世界模型 | 預測下一狀態 | 快速成熟 |
| L2 | 規劃世界模型 | 模型內 rollout 與選擇行動 | 快速成熟 |
| L3 | 可控制世界模型 | 顯式改變物件與條件 | 部分成熟 |
| L4 | 可執行世界模型 | 生成可運行程式與場景 | 早期快速發展 |
| L5 | 世界執行時 | 持久狀態、跨尺度、Agent、歷史 | 尚未統一 |
| L6 | 現實—虛擬耦合研究系統 | 雙向校準與反事實科學 | 局部存在 |
| L7 | 可持續套娃宇宙 | 子世界、自主文明、跨層機制 | 長期目標 |

---

# 附錄 B　World Runtime 最小介面

```python
from dataclasses import dataclass
from typing import Any, Protocol

@dataclass
class Uncertainty:
    epistemic: float
    aleatoric: float
    source: str

@dataclass
class WorldEvent:
    time: float
    event_type: str
    payload: dict[str, Any]
    provenance: list[str]

class Mechanism(Protocol):
    name: str
    layer: str
    timestep: float

    def validate(self, state: "WorldState") -> list[str]:
        ...

    def step(
        self,
        state: "WorldState",
        dt: float,
    ) -> dict[str, Any]:
        ...

@dataclass
class WorldState:
    time: float
    layers: dict[str, Any]
    entities: dict[str, Any]
    events: list[WorldEvent]
    uncertainty: dict[str, Uncertainty]
    provenance: dict[str, list[str]]

class WorldRuntime:
    def step(self, dt: float) -> None:
        ...

    def observe(self, query: dict[str, Any]) -> Any:
        ...

    def intervene(self, target: str, value: Any) -> None:
        ...

    def branch(self, label: str, seed: int) -> "WorldRuntime":
        ...

    def explain(self, target: str) -> dict[str, Any]:
        ...

    def assimilate(self, observations: dict[str, Any]) -> None:
        ...

    def recompile(self, changed_nodes: list[str]) -> None:
        ...
```

---

# 附錄 C　研究閉環

```text
collect real-world observations
    ↓
learn latent world state
    ↓
extract candidate mechanisms
    ↓
construct causal and dependency graphs
    ↓
compile executable world modules
    ↓
validate constraints and persistence
    ↓
run factual and counterfactual branches
    ↓
identify sensitive variables and divergent predictions
    ↓
design new real-world observations or experiments
    ↓
update mechanisms, uncertainty, and runtime
```

---

# 附錄 D　作者立場

本文作者共同主張：

1. 世界模型研究已是當代 AI 前沿，而不是純粹科幻想像；
2. 完整可編譯世界仍未完成，不能誇大當前技術；
3. 現有研究已提供互動生成、預測、控制、數位孿生、可執行場景與反事實模型等必要模組；
4. 下一階段問題是如何把模組統合為持久、因果、多尺度、可校準的 World Runtime；
5. 可執行世界不只是遊戲內容，也可以成為新型科學儀器；
6. 虛擬反事實不能自動等於現實證據，但能協助區分機制、生成觀測與暴露理論缺口；
7. 真正的長期目標不是讓 AI 只擁有一個世界模型，而是讓人類與 AI 共同建造可被驗證、修正與持續運行的世界模型系統。
