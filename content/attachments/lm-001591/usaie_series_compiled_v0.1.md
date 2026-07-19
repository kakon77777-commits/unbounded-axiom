# USAIE 論文系列合訂本 v0.1

# USAIE 論文系列 v0.1

作者：Neo.K（許筌崴）  
機構：一言諾科技有限公司（EVEMISSLAB）  
日期：2026-07-19

本套件把早期工作代號「真 Yahoo」正式化為「使用者主權自適應資訊環境」（User-Sovereign Adaptive Information Environment, USAIE）。

## 文件

1. `01_從線性搜尋到個人化門戶_v0.1.md`  
   搜尋功能解體、零點擊、分散式意圖路由與門戶重構假說。

2. `02_使用者主權自適應資訊環境_USAIE_v0.1.md`  
   USAIE、USIS、IES、PPIM、USAIP、PAAL 的正式定義與成熟度分級。

3. `03_個人認知控制平面_PECP_v0.1.md`  
   五平面架構、狀態更新、來源追溯、多樣性約束、實驗設計及可檢驗命題。

4. `04_從平台個人化到使用者治理_v0.1.md`  
   注意力主權、認知自由、資料可攜、平台鎖定及治理悖論。

5. `00_術語與符號總表.md`  
   四篇共用術語、縮寫及符號。

## 建議閱讀順序

$$
\text{入口變遷}
\rightarrow
\text{USAIE 理論}
\rightarrow
\text{PECP 架構}
\rightarrow
\text{治理後果}
$$

## 版本定位

這是可保存、可繼續擴寫的 v0.1 學術草案。文獻與實證資料已納入截至 2026-07-19 可取得的主要公開來源，但尚未進行正式系統性文獻回顧、統計統合或同儕審查。


---

# USAIE 系列術語與符號總表

| 縮寫 | 英文 | 中文 | 定位 |
|---|---|---|---|
| USAIE | User-Sovereign Adaptive Information Environment | 使用者主權自適應資訊環境 | 完整上位系統範式 |
| USAIP | User-Sovereign Adaptive Information Portal | 使用者主權自適應資訊門戶 | USAIE 的可見入口 |
| PPIM | Persistent Personal Information Mediation | 持續式個人資訊中介 | 由事件式查詢轉向持續狀態 |
| PECP | Personal Epistemic Control Plane | 個人認知控制平面 | 使用者治理來源、排序、信任、記憶與權限 |
| USIS | User-Sovereign Information State | 使用者主權資訊狀態 | 完整持續內部狀態 |
| IES | Information Environment Seed | 資訊環境種子 | USIS 的可序列化、可攜、可分享部分 |
| PAAL | Personal Attention Allocation Layer | 個人注意力配置層 | 管理注意力、通知與資訊優先序 |
| PRH | Portal Reconstitution Hypothesis | 門戶重構假說 | 解釋持續入口重新出現的理論 |

## 五平面

$$
\mathrm{USAIE}
=
\mathcal{D}
+
\mathcal{M}
+
\mathcal{C}
+
\mathcal{R}
+
\mathcal{A}
$$

| 符號 | 平面 |
|---|---|
| $\mathcal{D}$ | 資訊資料平面 |
| $\mathcal{M}$ | 語義中介平面 |
| $\mathcal{C}$ | 個人認知控制平面 |
| $\mathcal{R}$ | 自適應渲染平面 |
| $\mathcal{A}$ | 稽核與回退平面 |

## 成熟度

| 等級 | 定義 |
|---|---|
| USAIE-L1 | 個人化 AI 門戶 |
| USAIE-L2 | 可控式自適應門戶 |
| USAIE-L3 | 可攜、本地優先、跨平台的使用者主權資訊環境 |

## 早期名稱映射

| 早期工作名稱 | 正式名稱 |
|---|---|
| 真 Yahoo | USAIE |
| 真 Yahoo 門戶 | USAIP |
| 網站種子 | IES |
| 完整個人狀態 | USIS |
| 個人注意力網站 | PAAL 所在的 USAIP/USAIE 實作 |
| AI 預讀與重渲染 | 語義中介平面＋自適應渲染平面 |
| 原文回退 | 稽核與回退平面中的可逆性機制 |


---

# 從線性搜尋到個人化門戶：AI 時代的搜尋功能解體與門戶重構

## From Linear Search to Personalized Portals: Search Functional Decomposition and Portal Reconstitution in the Age of AI

**作者：** Neo.K（許筌崴）  
**機構：** 一言諾科技有限公司（EVEMISSLAB）  
**版本：** v0.1 學術草案  
**日期：** 2026-07-19  
**狀態：** 概念建模與理論建構稿；尚未經同儕審查  

> 術語說明：本文將早期工作代號「真 Yahoo」正式化為「使用者主權自適應資訊環境」（User-Sovereign Adaptive Information Environment, USAIE）。工作代號僅用於概念史回溯，不指涉 Yahoo 公司之商標、產品所有權或合作關係。


## 摘要

本文研究一項表面矛盾的網路現象：傳統搜尋業務與查詢活動仍可持續成長，但大量資訊型網站與內容生產者卻感受到外部點擊、自然發現與冷啟動能力的下降。本文主張，矛盾源自「搜尋」一詞長期混合了至少四種不同功能：資訊定位、首次發現、答案完成與外部網站導流。生成式人工智慧、演算法資訊流及平台內答案使這些功能開始解耦。搜尋引擎並未消失，而是由連結分配器轉化為答案生成與任務中介系統；同時，社群平台、影音推薦、AI 對話及個人化首頁分別吸收首次發現與持續資訊追蹤功能。

本文提出「搜尋功能解體命題」與「門戶重構假說」（Portal Reconstitution Hypothesis, PRH）。前者指出，當資訊定位、答案生成、內容發現與網站導流分散到不同系統後，不再存在統一的單一第一入口；後者指出，當反覆查詢、來源切換與情境重建的邊際成本，高於建立並維持個人化資訊入口的成本時，使用者將由事件式線性搜尋轉向持續式資訊環境。Yahoo Scout 與 MyScout 在 2026 年的推出，可被視為 AI 答案引擎與個人化門戶重新結合的早期市場證據，但尚不足以證明使用者主權型門戶已經完成。

**關鍵詞：** 線性搜尋、零點擊搜尋、AI 答案引擎、個人化門戶、門戶重構、資訊發現、網站導流

---

## 1. 問題提出

搜尋引擎過去同時承擔四個角色：

$$
\mathcal{S}_{legacy}=I+D+A+R
$$

其中：

- $I$：Information Location，資訊定位；
- $D$：Discovery，未知內容發現；
- $A$：Answer Completion，答案完成；
- $R$：Referral，向外部網站導流。

在傳統十條藍色連結模式中，四者高度耦合：

$$
\text{提出查詢}
\rightarrow
\text{取得結果列表}
\rightarrow
\text{進入網站}
\rightarrow
\text{完成理解}
$$

但在 AI 搜尋與平台推薦環境中，這條鏈已被拆開：

$$
I\rightarrow\text{搜尋與索引}
$$

$$
D\rightarrow\text{社群、影音與推薦流}
$$

$$
A\rightarrow\text{AI 摘要、答案引擎與聊天介面}
$$

$$
R\rightarrow\text{被壓縮、重新分配或延後}
$$

因此，「搜尋仍然成長」與「網站較難獲得點擊」可以同時成立。

Alphabet 於 2026 年第一季公布 Google Search & other 營收年增 $19\%$，並稱查詢量創新高。這證明搜尋商業系統依然強勁，卻不能直接推出外部網站流量按相同比例成長。Google 另稱整體自然點擊量大致穩定、高品質點擊略增；Pew Research Center 以美國使用者瀏覽資料分析則發現，具有 AI 摘要的搜尋頁面中，傳統結果點擊率約為 $8\%$，未出現摘要時約為 $15\%$，而對摘要引用來源的直接點擊約為 $1\%$。兩者測量層次不同，因此未必互相否定。

## 2. 搜尋活動與網站導流的分離

令搜尋平台營收為：

$$
R_G=Q\cdot p_a\cdot p_c\cdot v_c
$$

其中 $Q$ 為查詢與互動量，$p_a$ 為廣告展示機率，$p_c$ 為廣告點擊或轉換機率，$v_c$ 為單次商業行為價值。

外部網站取得的自然流量則近似為：

$$
T_W=D_q\cdot p_i\cdot p_r\cdot p_v\cdot p_o
$$

其中 $D_q$ 為相關查詢需求，$p_i$ 為被索引機率，$p_r$ 為進入可見排名機率，$p_v$ 為介面可見性，$p_o$ 為外部點擊機率。

因此可能出現：

$$
R_G\uparrow
\qquad\land\qquad
T_W\downarrow
$$

更精確的觀察量應是：

$$
\eta_R=
\frac{\text{外部網站點擊}}{\text{搜尋或答案互動次數}}
$$

本文稱 $\eta_R$ 為「外部導流效率」。搜尋使用量上升並不表示 $\eta_R$ 上升。

## 3. 搜尋功能解體命題

### 命題一：功能解體

$$
\text{Search Share}
\neq
\text{Discovery Share}
\neq
\text{Answer Share}
\neq
\text{Referral Share}
$$

使用者可能先在社群平台得知事件，再到搜尋引擎驗證，最後在 AI 介面整合資料。只以最後一次查詢衡量入口，會忽略首次發現；只以網站推薦流量衡量搜尋使用，則會忽略零點擊答案。

### 命題二：來源使用與來源可見分離

$$
\text{Source Used}
\not\Rightarrow
\text{Source Visited}
$$

$$
\text{Source Influenced Answer}
\not\Rightarrow
\text{Source Recognized}
$$

生成式系統可讀取、擷取或綜合來源，而使用者未必造訪或辨識該來源。2026 年針對 Google AI Overviews 的研究已開始測量來源選擇、主張支持程度與出版者衝擊，顯示 AI 摘要不只是搜尋結果的附加層，而是新的編輯與注意力分配層。

### 命題三：單一第一入口消失

| 資訊意圖 | 可能的第一入口 |
|---|---|
| 已知網站、品牌、人物 | 搜尋引擎或網址列 |
| 商品比較與交易 | 電商、搜尋、AI 購物助手 |
| 技術解題 | AI、文件、GitHub、搜尋 |
| 影音教學 | YouTube、短影音、搜尋 |
| 新聞偶然發現 | 社群、影音、推播、聚合器 |
| 長期領域追蹤 | 個人化首頁、RSS、社群、AI 摘要 |
| 複雜研究 | AI、搜尋、資料庫與原始文件組合 |

網路入口因此由單一搜尋框轉向「分散式意圖路由」。

## 4. 無限線性搜尋問題

傳統搜尋任務可表示為：

$$
q_1\rightarrow R_1\rightarrow x_1\rightarrow q_2\rightarrow R_2\rightarrow x_2\rightarrow\cdots\rightarrow q_n
$$

每一輪都需要重新完成查詢構造、結果掃描、頁面切換、來源比較、重複排除與任務狀態回憶。總成本可寫為：

$$
C_{LS}(n)=
\sum_{i=1}^{n}
\left(
c_q^{(i)}+
c_r^{(i)}+
c_v^{(i)}+
c_s^{(i)}
\right)
$$

其中 $c_s$ 代表情境重建與狀態切換成本。對單次明確問題，線性搜尋仍極有效；對每日更新、跨來源、長週期與多專案追蹤，成本可能持續累積。

## 5. 門戶重構假說

> **門戶重構假說（PRH）：當事件式搜尋的反覆查詢、來源切換與狀態重建邊際成本，高於持續式資訊中介的建立與維護成本時，使用者將逐步由線性搜尋轉向個人化門戶或持續資訊環境。**

$$
MC_{search}>MC_{persistent}
\Rightarrow
P(\text{persistent portal adoption})\uparrow
$$

持續式入口的成本可近似為：

$$
C_P(n)=C_0+\sum_{i=1}^{n}c_m^{(i)}
$$

若：

$$
c_m<c_q+c_r+c_v+c_s
$$

則存在臨界使用次數：

$$
n^*=
\frac{C_0}
{(c_q+c_r+c_v+c_s)-c_m}
$$

當 $n>n^*$，持續入口的平均成本低於反覆搜尋。

## 6. 門戶的歷史螺旋

$$
\text{Directory Portal}
\rightarrow
\text{Search Engine}
\rightarrow
\text{Algorithmic Feed}
\rightarrow
\text{AI Answer Engine}
\rightarrow
\text{Personal AI Portal}
$$

舊門戶由編輯部決定所有人看什麼；演算法資訊流依平台推測偏好排序；AI 個人化門戶則開始把自然語言查詢、答案生成、使用者興趣與多種垂直資料整合在同一個持續入口。

Yahoo 於 2026 年 1 月推出 Yahoo Scout，將其描述為結合開放網路、Yahoo 資料及多個垂直產品的 AI 答案引擎；同年 3 月推出 MyScout，提供可自訂資訊卡的個人化首頁。這代表大型既有門戶業者已判斷「答案引擎＋個人化首頁」具有戰略價值。

然而，這只能驗證：

$$
\text{AI Portal Direction}
$$

尚不能驗證：

$$
\text{User-Sovereign Portal Completed}
$$

因為平台仍可能掌握隱藏使用者模型、排序目標、資料攜帶與商業最佳化。

## 7. 研究命題與可證偽條件

### H1：查詢增長—外部點擊脫鉤命題

搜尋與答案互動量增加時，外部導流效率 $\eta_R$ 可能下降。

### H2：重複任務門戶優勢命題

對每日或每週反覆執行的多來源追蹤任務，持續式入口的平均任務時間低於事件式搜尋。

### H3：新概念冷啟動限制命題

$$
D_q\approx0
\Rightarrow
T_W\approx0
$$

搜尋引擎擅長捕捉既有需求，不一定擅長創造尚未形成公共詞彙的新需求。

### H4：平台化發現命題

首次接觸資訊的比例將更多分散至社群、影音、AI 與推播介面，而非集中於通用搜尋框。

### 可證偽條件

若長期資料顯示 AI 答案普及後外部導流效率持續上升、使用者在重複資訊任務中仍普遍偏好每次重新搜尋，且個人化首頁長期留存無任何領域優勢，則門戶重構假說應被削弱或限定。

## 8. 限制

本文不主張搜尋引擎將消失，也不主張所有使用者都會採用門戶。導航、交易、在地服務、單一事實與臨時問題仍適合搜尋。本文討論的是長期追蹤、資訊過載與多來源整合情境下的相對優勢。

Yahoo 對自身使用者規模與資料資產的描述屬公司自陳；Google 對整體點擊穩定與高品質點擊的描述亦來自平台方。本文因此將平台陳述、第三方行為資料與學術測量分開處理，不把任何單一來源視為最終結論。

## 9. 結論

搜尋引擎沒有死亡。正在消失的是一個較舊的隱含契約：使用者每提出一次資訊需求，搜尋引擎就會把他送往一個外部網站。

新的結構是：

$$
\text{Search}
\rightarrow
\text{Answer}
\rightarrow
\text{Optional Source Visit}
$$

對長期資訊需求，更可能進一步變成：

$$
\text{Persistent User State}
+
\Delta\text{World}
\rightarrow
\text{Adaptive Portal}
$$

真正的歷史轉變不是 Yahoo 取代 Google，而是事件式線性搜尋逐步讓出部分功能給持續式個人資訊環境。這為 USAIE 理論提供了時代背景與必要性。

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



---

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

- $\mathbf{L}_u$：版面與表示偏好；
- $\mathbf{C}_u$：內容主題與來源偏好；
- $\mathbf{R}_u$：排序、推薦與探索政策；
- $\mathbf{E}_u$：知識信任與觀點多樣性政策；
- $\mathbf{P}_u$：隱私與資料揭露政策；
- $\mathbf{M}_u$：媒介、語音、視覺與無障礙偏好；
- $\mathbf{H}_u(t)$：可選擇保留的歷史、已讀狀態與長期記憶。

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

令使用者明示治理規則為 $\mathbf{g}_u(t)$，則 USAIE 產生的個人資訊環境為：

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

其中 $\mathbf{f}_u(t)$ 為使用者明示修正與回饋，$\Delta\mathcal{W}_t$ 為外部世界的新資訊，$\mathcal{U}$ 為受使用者規則約束的狀態更新函數。

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

其中 $R_u$ 為相關性，$Q_u$ 為證據品質，$D_u$ 為多樣性，$S_u$ 為意外發現，$A_u$ 為自主性，$C_u$ 為認知成本，$P_u$ 為隱私風險，$B_u$ 為偏誤、操控與封閉風險。

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



---

# 個人認知控制平面：使用者治理型資訊環境的系統架構與可檢驗命題

## The Personal Epistemic Control Plane: System Architecture and Testable Propositions for User-Governed Information Environments

**作者：** Neo.K（許筌崴）  
**機構：** 一言諾科技有限公司（EVEMISSLAB）  
**版本：** v0.1 學術草案  
**日期：** 2026-07-19  
**狀態：** 概念建模與理論建構稿；尚未經同儕審查  

> 術語說明：本文將早期工作代號「真 Yahoo」正式化為「使用者主權自適應資訊環境」（User-Sovereign Adaptive Information Environment, USAIE）。工作代號僅用於概念史回溯，不指涉 Yahoo 公司之商標、產品所有權或合作關係。


## 摘要

本文將使用者主權自適應資訊環境（USAIE）進一步形式化為五平面系統架構，並提出其核心機制「個人認知控制平面」（Personal Epistemic Control Plane, PECP）。本文主張，資料是否歸使用者所有並不足以保證資訊主權；真正決定系統性權力的是誰能設定來源選擇、排序目標、驗證門檻、多樣性、摘要深度、記憶更新及 AI 行動權限。若這些控制仍由平台的隱藏模型掌握，系統即使高度個人化，也不能稱為強形式 USAIE。

本文提出資料平面、語義中介平面、認知控制平面、自適應渲染平面、稽核與回退平面，以及一套可實作的狀態更新、權限優先序、種子結構、來源追溯與多樣性約束。最後提出五組對照系統、三類任務及十項實驗指標，使 USAIE 可從概念主張轉化為可證偽的 HCI、資訊檢索與推薦系統研究計畫。

**關鍵詞：** PECP、USAIE、控制平面、資訊檢索、推薦系統、可治理個人化、來源追溯、人機互動

---

## 1. 從資料主權到控制平面主權

數位主權常被簡化為：

$$
\text{Who owns the data?}
$$

但在資訊環境中，更關鍵的問題是：

$$
\text{Who controls the transformation?}
$$

即使使用者擁有原始資料，平台仍可能控制哪些來源被選入、哪些資訊被隱藏、如何排序與摘要、何時改寫長期偏好、哪些商業內容被插入，以及 AI 可以替使用者執行哪些行動。

> **個人認知控制平面（PECP）是使用者對資訊選擇、知識信任、排序、多樣性、表達、記憶與 AI 權限進行明示治理的規則層。**

## 2. 五平面架構

$$
\mathrm{USAIE}
=
\mathcal{D}
+
\mathcal{M}
+
\mathcal{C}
+
\mathcal{R}
+
\mathcal{A}
$$

### 2.1 資訊資料平面 $\mathcal{D}$

負責接入 URL、網頁、RSS、新聞、論文、PDF、郵件、私人文件、GitHub、影音字幕、感測資料、日曆及 Agent 結果。資料平面只負責「有什麼」，不直接決定「應該看什麼」。

### 2.2 語義中介平面 $\mathcal{M}$

負責內容抽取、實體與時間標記、去重、聚類、摘要、翻譯、難度調整、主張—證據對應、來源衝突偵測及世界變化差分。

### 2.3 個人認知控制平面 $\mathcal{C}$

負責來源白名單與黑名單、主題與時效權重、證據門檻、多樣性、隱私、記憶寫入、摘要強度、商業內容政策、Agent 權限及使用者覆寫。

### 2.4 自適應渲染平面 $\mathcal{R}$

依情境輸出卡片、長文、時間線、表格、圖表、來源對照、研究模式、低刺激模式、語音、背景資訊流與無障礙介面。

### 2.5 稽核與回退平面 $\mathcal{A}$

保存原始來源、AI 處理步驟、摘要—證據對應、使用者覆寫、記憶變更、模型與規則版本、狀態快照及還原點。

## 3. 控制優先序

當頁覆寫通常應高於長期規則：

$$
O_u(t)
\succ
G_u
\succ
I_u(t)
\succ
D_p
$$

其中：

- $O_u(t)$：當頁或當次明示覆寫；
- $G_u$：使用者長期治理規則；
- $I_u(t)$：系統推斷偏好；
- $D_p$：平台預設與商業目標。

例外僅限安全、法律或使用者預先設定的不可覆寫限制。

## 4. 狀態更新與記憶污染防止

將使用者狀態分為：

$$
\mathbf{s}_u(t)
=
\mathbf{s}_u^{long}
+
\mathbf{s}_u^{trend}(t)
+
\mathbf{o}_u(t)
$$

其中 $\mathbf{s}_u^{long}$ 為長期穩定規則，$\mathbf{s}_u^{trend}(t)$ 為短期趨勢，$\mathbf{o}_u(t)$ 為當次覆寫。

長期狀態應滿足：

$$
\Delta\mathbf{s}_u^{long}=0
$$

除非使用者明示確認，或多次一致行為達到門檻且使用者同意。

短期趨勢可自動衰減：

$$
\mathbf{s}_u^{trend}(t+\Delta t)
=
\rho\mathbf{s}_u^{trend}(t)
+
\Delta\mathbf{f}_u(t)
$$

其中：

$$
0\leq\rho<1
$$

此設計避免一次點擊、偶然閱讀或研究反方資料直接污染長期模型。

## 5. 來源追溯模型

每一個生成結果 $y_j$ 應對應一個來源集合：

$$
\Gamma(y_j)
=
\{(x_i,w_{ij},r_{ij})\}
$$

其中 $x_i$ 為原始來源，$w_{ij}$ 為貢獻權重，$r_{ij}$ 為支持、反駁、背景或推斷關係。

最低要求為：

$$
|\Gamma(y_j)|\geq1
$$

對無法追溯的事實性主張：

$$
\Gamma(y_j)=\varnothing
$$

系統不得以確定事實形式呈現。

## 6. 多樣性與反繭房約束

只追求相關性時：

$$
\max R_u
\Rightarrow
D_u\downarrow
$$

因此 PECP 應允許設定：

$$
D_u(t)\geq D_{min}
$$

以及探索比例：

$$
\epsilon_u(t)\in[0,1]
$$

資訊輸出可由：

$$
\mathcal{E}_u
=
(1-\epsilon_u-\omega_u)\mathcal{E}_{relevant}
+
\epsilon_u\mathcal{E}_{orthogonal}
+
\omega_u\mathcal{E}_{oppositional}
$$

其中 $\epsilon_u$ 為正交探索比例，$\omega_u$ 為反向或爭議觀點比例。

## 7. 種子結構與可攜介面

最小 IES 可採 JSON、YAML 或其他開放格式：

```json
{
  "schema_version": "0.1",
  "layout_policy": {},
  "content_sources": [],
  "ranking_policy": {},
  "epistemic_policy": {},
  "privacy_policy": {},
  "modality_policy": {},
  "memory_write_policy": {},
  "agent_permission_policy": {},
  "portability_policy": {}
}
```

可攜性不要求所有平台完全相同，而要求語義近似：

$$
d
\left(
\mathbf{s}_u,
\operatorname{Import}_B(
\operatorname{Export}_A(\mathbf{s}_u))
\right)
\leq\varepsilon
$$

## 8. 最小可實作管線

```text
Content Source
→ Extractor
→ AI Pre-Reader
→ User Seed / Context Seed
→ PECP Policy Check
→ Dynamic Renderer
→ User Override
→ Raw Source Fallback
→ Optional Memory Update
```

最小輸出應包括一句話摘要、核心主張、來源標示、使用者指定版型、原文回退、當頁覆寫，以及是否寫入長期記憶的明確選項。

## 9. 系統比較實驗

### 9.1 對照組

| 組別 | 系統 |
|---|---|
| A | 傳統搜尋引擎 |
| B | AI 答案引擎 |
| C | 平台個人化首頁 |
| D | USAIE-L2 可控式門戶 |
| E | USAIE-L3 可攜、本地優先環境 |

### 9.2 任務類型

1. **明確目標查詢：** 尋找單一已知答案。
2. **每日態勢掌握：** 掌握特定領域過去 24 小時的變化。
3. **開放式探索：** 發現未知但相關的資訊、反方觀點及跨領域連結。

## 10. 測量指標

$$
T_s=\text{達到滿意資訊狀態的時間}
$$

$$
N_q=\text{查詢或提示次數}
$$

$$
N_c=\text{頁面與情境切換次數}
$$

$$
D_s=\text{來源與觀點多樣性}
$$

$$
E_c=\text{主張的證據覆蓋率}
$$

$$
K_r=\text{延遲知識保留}
$$

$$
A_p=\text{感知自主性}
$$

$$
L_c=\text{認知負荷}
$$

$$
P_r=\text{隱私揭露與集中風險}
$$

$$
M_c=\text{錯誤修正與信心校準}
$$

CTR、停留時間與留存率可以保留，但不能作為主要成功標準。

## 11. 可檢驗命題

### P1：持續狀態效率

$$
\bar{C}_{USAIE}
<
\bar{C}_{search}
\quad
\text{when } n>n^*
$$

### P2：可操作控制效應

提供「解釋＋直接修改」的系統，其感知自主性高於只提供解釋的系統。

### P3：來源回退校準

可一鍵比較原文與摘要的系統，應具有較低自動化偏誤。

### P4：多樣性下限

具有 $D_{min}$ 約束的系統，長期來源集中度低於只最佳化相關性的系統。

### P5：可攜狀態降低鎖定

IES 可移轉時，切換平台所需重新訓練與設定成本下降。

### P6：本地優先隱私效應

個人狀態在本地處理、僅選擇性揭露時，集中風險下降，但可能增加運算與維護成本。

## 12. 安全與失敗模式

1. 惡意種子；
2. 來源投毒；
3. 設定劫持；
4. 記憶污染；
5. 摘要漂移；
6. 權限擴張；
7. 虛假可攜。

安全設計應包括簽章、版本歷史、沙箱、權限分級、差異檢視及不可見規則檢測。

## 13. 結論

USAIE 的主權不是由華麗首頁、推薦準確率或資料所有權單獨決定，而由誰控制 $\mathcal{C}$ 決定：

$$
\boxed{\text{Who controls the control plane?}}
$$

完整 USAIE 必須使使用者能看見、修改、暫停、匯出規則，能比較 AI 結果與原文、拒絕記憶寫入、限制 Agent 權限，並保留探索與多樣性。

PECP 是把「個人化」轉化為「治理」的核心機制，也是後續 MVP 與實證研究最重要的架構基準。

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



---

# 從平台個人化到使用者治理：AI 資訊環境中的注意力主權、認知自由與資料可攜性

## From Platform Personalization to User Governance: Attention Sovereignty, Cognitive Liberty, and Data Portability in AI Information Environments

**作者：** Neo.K（許筌崴）  
**機構：** 一言諾科技有限公司（EVEMISSLAB）  
**版本：** v0.1 學術草案  
**日期：** 2026-07-19  
**狀態：** 概念建模與理論建構稿；尚未經同儕審查  

> 術語說明：本文將早期工作代號「真 Yahoo」正式化為「使用者主權自適應資訊環境」（User-Sovereign Adaptive Information Environment, USAIE）。工作代號僅用於概念史回溯，不指涉 Yahoo 公司之商標、產品所有權或合作關係。


## 摘要

隨著搜尋、新聞、購物、娛樂與工作逐步被 AI 中介，個人化系統不再只是排列內容，而開始決定人如何接觸世界、如何理解來源及如何配置有限注意力。本文從治理與政治經濟角度分析使用者主權自適應資訊環境（USAIE），主張未來資訊權力的核心將由「誰擁有資料」進一步轉向「誰控制個人化模型、注意力分配與認知中介規則」。

本文提出注意力主權、認知自由與個人化可攜性三個治理概念，並分析個人化—隱私、控制—負擔、認知卸載—認知退化、探索—安全及開放—操控五組悖論。本文不假設使用者控制天然善良；高度可控的個人化環境也可能形成更封閉的私人繭房、惡意種子市場或由強勢代理人代替使用者作決定。因此，強形式 USAIE 必須結合透明、可撤回授權、來源追溯、多樣性下限、非操控預設及公共利益約束。

**關鍵詞：** 注意力主權、認知自由、資料可攜、平台治理、資訊繭房、AI 中介、數位主權

---

## 1. 個人化正在成為認知基礎設施

傳統平台個人化影響哪些貼文排在前面、哪些商品被推薦、哪些影片自動播放。AI 資訊環境進一步影響哪些來源被納入答案、哪些衝突主張被省略、哪些資料被視為可信、使用者是否需要看到原文、哪些問題被判定重要，以及哪些任務由 Agent 自動執行。

個人化的治理對象因此由內容排序擴張為：

$$
\mathcal{G}
=
\{
\text{selection},
\text{ranking},
\text{summarization},
\text{verification},
\text{memory},
\text{action}
\}
$$

## 2. 注意力主權

注意力主權是個人對其有限注意力如何被資訊系統請求、排序、占用、延後與保留，具有可理解、可操作及可撤回的治理能力。

令每日可用注意力為：

$$
B_u=\sum_{i=1}^{n}a_i
$$

注意力主權要求：

$$
\operatorname{Allocate}(B_u)
=
f(
\mathbf{g}_u,
\mathbf{k}_u,
\Delta\mathcal{W}
)
$$

而非主要由：

$$
\operatorname{Allocate}(B_u)
=
f(\text{engagement maximization})
$$

使用者應能設定哪些主題可以即時打斷、哪些內容只能進入每日摘要、商業內容比例、重複資訊壓縮、高焦慮內容呈現方式、深度閱讀與快速掃描模式，以及不被個人化的中立模式。

## 3. 認知自由

認知自由不是否定一切中介，而是保留使用者形成、修正及拒絕觀點的能力。

AI 中介可能提供認知卸載、多來源綜合、複雜資訊簡化、對比與驗證；也可能造成自動化偏誤、來源失憶、過度依賴摘要、觀點範圍由模型預先決定，以及把模型選擇誤認為世界本身。

最低要求為：

$$
\text{Reversibility}
+
\text{Source Visibility}
+
\text{Alternative Views}
+
\text{User Override}
$$

## 4. 個人化可攜性

平台鎖定的一個主要來源，是使用者離開平台後必須重新累積行為歷史、偏好、關注清單、隱私設定、推薦模型與已讀狀態。

$$
C_{switch}
=
C_{data}
+
C_{profile}
+
C_{training}
+
C_{workflow}
$$

若 IES 與治理政策可移轉：

$$
C_{switch}'<C_{switch}
$$

平台競爭可能由「誰掌握最多不可攜資料」轉向「誰能最好執行使用者的既有規則」。

但完整個人模型可能比密碼或瀏覽紀錄更敏感，因此可攜不應等於一次匯出全部人格模型，而應採最小揭露、模組化匯出、加密、到期、撤回與裝置端解密。

## 5. 五組治理悖論

### 5.1 個人化—隱私悖論

$$
Q_{personalization}\uparrow
\quad\text{as}\quad
D_{personal}\uparrow
$$

同時：

$$
R_{privacy}\uparrow
\quad\text{as}\quad
D_{personal}\uparrow
$$

解法是本地優先、選擇性揭露及可撤回授權。

### 5.2 控制—負擔悖論

$$
A_{agency}\uparrow
\qquad
C_{configuration}\uparrow
$$

若要求使用者設定數百個參數，主權將變成責任轉嫁。合理架構應是：

$$
\text{AI Suggestion}
+
\text{Progressive Disclosure}
+
\text{Final User Override}
$$

### 5.3 認知卸載—認知退化悖論

USAIE 應最小化：

$$
\text{Redundant Cognitive Labor}
$$

而不是最小化：

$$
\text{Human Thinking}
$$

應將去重、格式轉換與初步整理交給 AI，同時保留來源判斷、價值取捨與重要決策給人。

### 5.4 探索—安全悖論

反向與隨機探索可打破繭房，也可能增加錯誤資訊、仇恨或操控內容。系統必須把「不同觀點」與「低可信度」分開，不以多樣性為由取消證據門檻。

### 5.5 開放—操控悖論

種子分享與市場可能出現偽裝成中立的宣傳種子、針對脆弱族群的操控配置、隱藏廣告、惡意資料來源與追蹤個人狀態的模板。因此 IES 需要簽章、權限清單、來源清單、商業揭露與安全掃描。

## 6. 平台個人化與使用者治理

| 面向 | 平台個人化 | 使用者治理型個人化 |
|---|---|---|
| 使用者模型 | 隱藏推斷 | 可檢視、可修正 |
| 最佳化目標 | 留存、廣告、交易 | 使用者自定多目標 |
| 資料範圍 | 平台局部資料 | 使用者選擇的跨域資料 |
| 規則可攜 | 通常不可 | 原則上可 |
| 來源控制 | 平台決定 | 使用者可設定 |
| 多樣性 | 平台策略 | 使用者政策＋最低保障 |
| 原文回退 | 不一定 | 必須 |
| 記憶寫入 | 常為隱式 | 可拒絕、可撤回 |
| 商業內容 | 與推薦混合 | 應清楚揭露 |

核心對立為：

$$
\text{Platform-Governed Personalization}
\quad\text{vs.}\quad
\text{User-Governed Information Environment}
$$

## 7. 使用者主權並非使用者絕對主義

USAIE 不應被理解為使用者可以要求系統隱藏所有相反證據、偽造來源、將推測標示為事實、取消法律與安全限制、未經同意使用他人資料或讓 Agent 執行高風險行動。

使用者主權指向個人資訊環境的治理權，而不是對事實、他人權利或公共安全的無限制支配。

$$
\text{Personal Preference}
\neq
\text{Epistemic Integrity Constraint}
$$

使用者可選擇呈現與探索策略，但系統仍應標示證據品質、來源衝突與不確定性。

## 8. 治理原則

1. **明示優先：** 平台推斷不得秘密覆蓋使用者明示規則。
2. **資料最小化：** 只使用完成當前任務所需的最低資料。
3. **可撤回性：** 使用者可撤回資料、記憶與 Agent 權限。
4. **可逆性：** 摘要、重渲染及建議必須能回到原始來源與處理記錄。
5. **多樣性保障：** 提供可見的多樣性與來源集中度指標。
6. **商業透明：** 廣告、贊助、聯盟分潤及平台自有服務偏好必須標示。
7. **非操控預設：** 不得利用使用者弱點最大化依賴、焦慮或衝動行為。
8. **加強保護：** 兒童與脆弱族群不應直接套用成人的完全可配置種子市場。

## 9. 制度與市場影響

### 9.1 從資料護城河轉向執行競爭

平台需競爭推理品質、渲染品質、隱私保障、來源覆蓋、速度、成本與開放標準相容性。

### 9.2 新型中介者

可能出現個人資訊環境託管者、種子設計師、認知安全審計者、來源評級服務、個人模型備份服務及跨平台偏好轉譯器。

### 9.3 開放網路的新交換問題

若 AI 入口大量使用網站內容卻不產生點擊，USAIE 仍需處理原始內容生產者的激勵。可能機制包括微支付、訂閱權限轉接、引用與收益分配、使用量透明及出版者授權協議。

## 10. 研究問題

1. 使用者是否願意編輯與攜帶個人化模型？
2. 哪些設定應由使用者明示，哪些可由 AI 建議？
3. 多樣性下限應由個人、平台或法律設定？
4. 如何測量認知自由，而不只測量滿意度？
5. 種子可攜是否會降低平台鎖定，還是形成新的個人模型壟斷者？
6. 本地優先架構能否在成本、速度與隱私間取得可接受平衡？
7. AI 中介對內容生產者的補償應採市場機制、協議標準或法律制度？

## 11. 結論

AI 個人化正在由「讓人更容易找到喜歡的內容」轉化為「替人預先構造可見世界」。個人化不再只是產品功能，而是注意力、知識與行動的治理問題。

強形式 USAIE 的目標不是：

$$
\max\text{Personalization}
$$

而是：

$$
\max
(
\text{Agency}
+
\text{Traceability}
+
\text{Portability}
+
\text{Epistemic Integrity}
)
$$

同時：

$$
\min
(
\text{Manipulation}
+
\text{Privacy Risk}
+
\text{Lock-in}
+
\text{Cognitive Dependency}
)
$$

使用者主權的真正標準，不是系統看起來多懂使用者，而是使用者能否理解系統如何理解自己，並有能力修正、拒絕、攜帶或終止這種理解。

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

