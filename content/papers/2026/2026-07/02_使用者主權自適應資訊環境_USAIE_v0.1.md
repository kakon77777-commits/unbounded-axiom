# 使用者主權自適應資訊環境：持續式個人資訊中介的理論框架

## User-Sovereign Adaptive Information Environments: A Theoretical Framework for Persistent Personal Information Mediation

**作者：** Neo.K（許筌崴）  
**機構：** 一言諾科技有限公司（EVEMISSLAB）  
**版本：** v0.1 學術草案  
**日期：** 2026-07-19  
**狀態：** 概念建模與理論建構稿；尚未經同儕審查  

> 術語說明：本文將早期工作代號「真 Yahoo」正式化為「使用者主權自適應資訊環境」（User-Sovereign Adaptive Information Environment, USAIE）。工作代號僅用於概念史回溯，不指涉 Yahoo 公司之商標、產品所有權或合作關係。


## 摘要

本文提出「使用者主權自適應資訊環境」（User-Sovereign Adaptive Information Environment, USAIE），用以描述一類由使用者持續治理其資訊來源、推薦規則、知識信任政策、隱私邊界、媒介形式與介面狀態，並由人工智慧依長期個人狀態與即時情境動態生成的資訊入口。USAIE 不是一般個人化首頁、推薦系統、AI 答案引擎、儀表板或個人資料庫的別名；其關鍵差異在於，系統的個人化控制平面必須可被使用者檢視、修正、攜帶、覆寫與撤回。

本文建立 USAIE 的形式定義、必要條件、三層成熟度分級及核心術語，包括使用者主權資訊狀態（USIS）、資訊環境種子（IES）、持續式個人資訊中介（PPIM）、使用者主權自適應資訊門戶（USAIP）及個人注意力配置層（PAAL）。本文並將早期「網站種子」中的世界觀向量修正為「知識信任與觀點多樣性政策」，以避免把人的身份、政治立場或價值觀僵化為平台可操控的固定標籤。

**關鍵詞：** USAIE、使用者主權、個人化門戶、持續資訊狀態、資訊環境種子、可攜式個人化、AI 中介

---

## 1. 理論定位

既有個人化系統多半由平台維護一個隱藏使用者模型：

$$
\hat{\mathbf{u}}_p
=
f_p(
\text{clicks},
\text{watch time},
\text{purchases},
\text{engagement}
)
$$

此模型通常由平台推斷、使用者看不到完整內容、無法逐項修正、難以跨服務移轉，並主要服務平台的留存與商業目標。

USAIE 不否定推斷式個人化，而是要求推斷被置於可治理框架內：

$$
\mathbf{u}^*
=
\mathbf{u}_{explicit}
+
\mathbf{u}_{context}
+
\mathbf{u}_{history}
+
\mathbf{u}_{governance}
$$

其中 $\mathbf{u}_{governance}$ 表示使用者對來源、權重、資料使用、驗證門檻、多樣性及 AI 權限的明確規則。

近期「可治理個人化」與「跨平台使用者治理個人化」研究亦提出相似方向：LLM Agent 可能使使用者整合不同平台的資料與情境，並讓使用者表示變得可檢視、可修正與可攜。USAIE 在此基礎上進一步把研究對象由「推薦結果」擴張為「完整資訊環境」。

## 2. 正式定義

令時間 $t$ 的外部資訊來源集合為：

$$
\mathcal{X}_t=\{x_1,x_2,\ldots,x_n\}
$$

來源可包含網站與 RSS、新聞與論文、電子郵件與私人文件、GitHub、資料庫、即時指標、影音字幕、聲音資訊與 Agent 結果。

令使用者主權資訊狀態為：

$$
\mathbf{s}_u(t)
=
[
\mathbf{L}_u,
\mathbf{C}_u,
\mathbf{R}_u,
\mathbf{E}_u,
\mathbf{P}_u,
\mathbf{M}_u,
\mathbf{H}_u(t)
]
$$

其中：

- $\mathbf{L}_u$ ：版面與表示偏好；
- $\mathbf{C}_u$ ：內容主題與來源偏好；
- $\mathbf{R}_u$ ：排序、推薦與探索政策；
- $\mathbf{E}_u$ ：知識信任與觀點多樣性政策；
- $\mathbf{P}_u$ ：隱私與資料揭露政策；
- $\mathbf{M}_u$ ：媒介、語音、視覺與無障礙偏好；
- $\mathbf{H}_u(t)$ ：可選擇保留的歷史、已讀狀態與長期記憶。

令即時情境為：

$$
\mathbf{k}_u(t)
=
[
\text{task},
\text{time},
\text{device},
\text{attention},
\text{urgency}
]
$$

令使用者明示治理規則為 $\mathbf{g}_u(t)$ ，則 USAIE 產生的個人資訊環境為：

$$
\mathcal{E}_u(t)
=
\mathcal{M}_{\theta}
\left(
\mathcal{X}_t,
\mathbf{s}_u(t),
\mathbf{k}_u(t),
\mathbf{g}_u(t)
\right)
$$

其中 $\mathcal{M}_{\theta}$ 是 AI 中介、選擇、驗證與渲染函數。

### 使用者主權優先序

$$
\text{Explicit User Rules}
>
\text{Inferred Preferences}
>
\text{Platform Commercial Objective}
$$

若平台商業目標可以在不透明情況下覆蓋使用者規則，該系統只能稱為平台型個人化，不能稱為完整 USAIE。

## 3. 持續式個人資訊中介

本文以「持續式個人資訊中介」（Persistent Personal Information Mediation, PPIM）描述其運作範式。

AI 答案引擎通常是：

$$
q_t+h_{t-1}\rightarrow a_t
$$

PPIM 則是：

$$
\mathbf{s}_u(t+1)
=
\mathcal{U}
\left(
\mathbf{s}_u(t),
\mathbf{f}_u(t),
\mathbf{k}_u(t),
\Delta\mathcal{W}_t
\right)
$$

其中 $\mathbf{f}_u(t)$ 為使用者明示修正與回饋， $\Delta\mathcal{W}_t$ 為外部世界的新資訊， $\mathcal{U}$ 為受使用者規則約束的狀態更新函數。

系統不再每次從零回答，而是持續維護已讀內容、事件差分、尚未覆蓋的觀點、需要重新驗證的來源與當前任務。

## 4. 使用者主權資訊狀態與資訊環境種子

完整內部狀態稱為：

$$
\mathrm{USIS}
=
\text{User-Sovereign Information State}
$$

可序列化、可匯出或分享的版本稱為：

$$
\mathrm{IES}
=
\text{Information Environment Seed}
$$

其關係為：

$$
\mathrm{IES}
=
\operatorname{Serialize}(\mathrm{USIS}_{shareable})
$$

IES 不應預設包含全部歷史與敏感資料，而應只包含使用者選擇公開或移轉的政策與偏好。

建議的種子向量為：

$$
\mathbf{z}_u
=
[
\mathbf{L},
\mathbf{C},
\mathbf{R},
\mathbf{E},
\mathbf{P},
\mathbf{M},
\mathbf{D}
]
$$

其中 $\mathbf{D}$ 表示資料可攜、保存與刪除政策。

## 5. 從世界觀向量到知識信任政策

早期構想以 Worldview Vector 表示政治傾向、價值觀與信任域。此表示具有直觀性，但存在風險：

1. 把變動中的思想僵化為固定標籤；
2. 成為政治推斷、歧視或操控工具；
3. 讓系統把迎合誤認為尊重；
4. 把人本身與資訊接觸策略混為一談。

因此本文改用：

$$
\mathbf{E}_u
=
\text{Epistemic and Diversity Policy}
$$

即「知識信任與觀點多樣性政策」。它描述使用者希望系統如何處理資訊，而不是宣稱使用者本身是什麼人。

可包含：

- 原始資料與二手評論的優先序；
- 爭議主張的交叉驗證數量；
- 是否顯示反方、正交或隨機探索內容；
- 學術、新聞、論壇及個人經驗的權重；
- 不確定性、證據等級與時間有效性標示。

## 6. USAIE 與相鄰系統的區別

### 6.1 個人化首頁

$$
\text{Platform Content}
+
\text{Platform Model}
+
\text{User Topics}
\rightarrow
\text{Customized Homepage}
$$

USAIE 則為：

$$
\text{Multi-source World}
+
\text{Governable State}
+
\text{Portable Policies}
+
\text{AI Mediation}
\rightarrow
\text{Adaptive Environment}
$$

### 6.2 推薦系統

推薦系統主要解決：

$$
\operatorname{Rank}(i\mid u,c)
$$

USAIE 需要共同決定：

$$
\operatorname{Generate}
(
\text{selection},
\text{ranking},
\text{representation},
\text{modality},
\text{verification},
\text{interaction}
)
$$

### 6.3 AI 答案引擎

$$
q\rightarrow a
$$

相對於：

$$
(\mathcal{X}_t,\mathbf{s}_u,\mathbf{k}_u)
\rightarrow
\mathcal{E}_u(t)
$$

前者以問題為中心，後者以持續狀態與世界變化為中心。

### 6.4 個人資料庫

個人資料庫回答「我的資料如何保存、授權與提供給服務」；USAIE 另回答「外部世界如何被整理、驗證並呈現給我」。

### 6.5 儀表板

儀表板將固定資料映射到預先設計的視圖；USAIE 的介面、摘要深度、媒介與驗證路徑都可以是動態輸出。

## 7. USAIE 的七項必要條件

1. **持續狀態性：** 具有可治理、可修改、可刪除的長期資訊狀態。
2. **多來源中介性：** 能跨平台或跨來源接入。
3. **動態表示性：** 可依任務、注意力與裝置改變摘要、版型、媒介及互動方式。
4. **明示治理性：** 使用者可直接調整來源、權重、探索比例、驗證門檻與資料範圍。
5. **可攜性：**

$$
\operatorname{Import}_B
\left(
\operatorname{Export}_A(\mathbf{s}_u)
\right)
\approx
\mathbf{s}_u
$$

6. **可逆與可追溯性：**

$$
\forall y\in\mathcal{E}_u,
\quad
\exists x\in\mathcal{X}_t:
\operatorname{Trace}(y,x)=1
$$

7. **認知多樣性控制：** 使用者可切換熟悉、反向、正交、隨機及高證據門檻模式。

## 8. 成熟度分級

### USAIE-L1：個人化 AI 門戶

具備個人化資訊卡、AI 答案、持續更新首頁與有限主題選擇。Yahoo MyScout 可被視為此方向的代表性實例，但其平台資料、使用者控制與可攜性仍須分別檢驗。

### USAIE-L2：可控式自適應門戶

在 L1 之外增加來源控制、推薦權重調整、多情境模式、動態渲染、原文回退與使用者覆寫。Mini True Yahoo 的 AI 預讀、Render Override 與 Raw Page Fallback 主要對應此層。

### USAIE-L3：使用者主權資訊環境

在 L2 之外增加狀態與政策可攜、本地優先或可選資料治理、跨平台與跨 Agent 生效、多粒度授權與撤回、種子組合分享、多樣性下限，以及平台不得秘密覆蓋使用者規則。

## 9. 個人注意力配置層

$$
\mathrm{PAAL}
=
\text{Personal Attention Allocation Layer}
$$

其核心函數為：

$$
A_i(t)
=
f(
\text{importance},
\text{novelty},
\text{urgency},
\text{relevance},
\text{diversity},
\text{cognitive cost}
)
$$

PAAL 決定資訊獲得多少視覺、時間與通知資源，但 USAIE 還包括資料、信任、來源、隱私、介面與可攜性，因此：

$$
\mathrm{PAAL}\subset\mathrm{USAIE}
$$

## 10. 最佳化目標

平台個人化常最佳化參與與留存：

$$
\max U_p=\alpha E+\beta R+\gamma V
$$

USAIE 應允許使用者治理多目標函數：

$$
\max U_u
=
\alpha R_u
+\beta Q_u
+\gamma D_u
+\delta S_u
+\epsilon A_u
-\lambda C_u
-\mu P_u
-\nu B_u
$$

其中 $R_u$ 為相關性， $Q_u$ 為證據品質， $D_u$ 為多樣性， $S_u$ 為意外發現， $A_u$ 為自主性， $C_u$ 為認知成本， $P_u$ 為隱私風險， $B_u$ 為偏誤、操控與封閉風險。

## 11. 研究命題

1. **持續狀態效率命題：** 在重複性資訊任務中，USAIE 的平均任務成本低於事件式搜尋。
2. **可治理信任命題：** 可操作控制與來源追溯共同存在時，感知自主性與信任高於只有解釋的系統。
3. **多樣性下限命題：** 只最佳化個人相關性的 USAIE 仍會形成私人資訊繭房，因此必須維持：

$$
D_u(t)\geq D_{min}
$$

4. **可攜性競爭命題：** 當個人化狀態可移轉時，平台競爭會由資料封鎖轉向服務品質。
5. **狀態污染命題：** 若短期點擊直接改寫長期偏好，個人化模型將產生漂移與錯誤固化。

## 12. 限制與未決問題

USAIE 仍面臨初始化負擔、跨平台資料標準、個人狀態被竊取或推斷、AI 摘要失真、種子市場操控、不同法域的資料規則，以及使用者是否願意治理複雜設定等問題。

因此，USAIE 追求的是：

$$
\text{More Governable Personalization}
$$

而非：

$$
\text{More Invisible Profiling}
$$

## 13. 結論

USAIE 的核心不是更準確地猜測使用者喜歡什麼，而是把資訊環境的生成條件轉化為使用者可以理解、修改、攜帶與撤回的治理對象。

$$
\mathrm{USAIE}
=
\text{Persistent State}
+
\text{Multi-source Mediation}
+
\text{Explicit Governance}
+
\text{Adaptive Rendering}
+
\text{Traceability}
+
\text{Portability}
$$

個人化首頁是可見外觀；持續資訊狀態是記憶核心；資訊環境種子是可交換表示；使用者主權則取決於控制平面是否真正由使用者治理。

## 參考文獻

1. Alphabet Inc. (2026). *Alphabet Announces First Quarter 2026 Results*. https://abc.xyz/investor/
2. Google. (2025-08-06). *AI in Search is driving more queries and higher quality clicks*. https://blog.google/products-and-platforms/products/search/ai-search-driving-more-queries-higher-quality-clicks/
3. Chapekis, A., & Lieb, A. (2025-07-22). *Google users are less likely to click on links when an AI summary appears in the results*. Pew Research Center. https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/
4. Reuters Institute for the Study of Journalism. (2026). *Digital News Report 2026*. https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026
5. Yahoo Inc. (2026-01-27). *Introducing Yahoo Scout, a New AI Answer Engine*. https://www.yahooinc.com/press/introducing-yahoo-scout-a-new-ai-answer-engine
6. Yahoo Inc. (2026-03-11). *Yahoo Introduces MyScout, the First Personalized Homepage for AI Answers*. https://www.yahooinc.com/press/yahoo-introduces-myscout-the-first-personalized-homepage-for-ai-answers
7. Khosravi, M., & Yoganarasimhan, H. (2026). *Impact of AI Search Summaries on Website Traffic: Evidence from Google AI Overviews and Wikipedia*. arXiv:2602.18455. https://arxiv.org/abs/2602.18455
8. Xu, H., Iqbal, U., & Montgomery, J. M. (2026). *Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact*. arXiv:2605.14021. https://arxiv.org/abs/2605.14021
9. Liu, J., et al. (2026). *From Hidden Profiles to Governable Personalization: Recommender Systems in the Age of LLM Agents*. arXiv:2604.20065. https://arxiv.org/abs/2604.20065
10. Lin, J., et al. (2026). *LLM Agents Enable User-Governed Personalization Beyond Platform Boundaries*. arXiv:2605.09794. https://arxiv.org/abs/2605.09794
11. Wang, W., et al. (2022). *User-controllable Recommendation Against Filter Bubbles*. Proceedings of SIGIR 2022. https://doi.org/10.1145/3477495.3532075
12. Neo.K（許筌崴）. (2026-02). 《真 Yahoo 白皮書：AI 驅動的個人化門戶革命》v1.0，內部概念稿。
13. Neo.K（許筌崴）. (2026-06). 《Mini True Yahoo 技術白皮書：AI 預讀、即時渲染控制與個人化資訊入口》v0.3，內部技術稿。

