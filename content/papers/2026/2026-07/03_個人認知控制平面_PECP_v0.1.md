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

- $O_u(t)$ ：當頁或當次明示覆寫；
- $G_u$ ：使用者長期治理規則；
- $I_u(t)$ ：系統推斷偏好；
- $D_p$ ：平台預設與商業目標。

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

其中 $\mathbf{s}_u^{long}$ 為長期穩定規則， $\mathbf{s}_u^{trend}(t)$ 為短期趨勢， $\mathbf{o}_u(t)$ 為當次覆寫。

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

其中 $x_i$ 為原始來源， $w_{ij}$ 為貢獻權重， $r_{ij}$ 為支持、反駁、背景或推斷關係。

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

其中 $\epsilon_u$ 為正交探索比例， $\omega_u$ 為反向或爭議觀點比例。

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

