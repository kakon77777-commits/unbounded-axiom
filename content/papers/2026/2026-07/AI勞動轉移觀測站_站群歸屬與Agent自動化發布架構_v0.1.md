# AI—勞動轉移觀測站之站群歸屬與自動化發布架構

**文件類型：** 產品架構決策文件／網站資訊架構規格  
**版本：** v0.1  
**日期：** 2026-07-15  
**提出者：** Neo.K  
**協作整理：** Aletheia（GPT）

---

## 摘要

「AI—勞動轉移觀測站」的核心任務，是持續追蹤人工智慧能力、企業採用、職業任務重構、招聘需求、薪資變化與技能遷移路徑。此系統雖然與 AI 權利、演算法治理與勞動正義密切相關，但其第一本體仍然屬於勞動經濟、產業變遷與公共資料觀測，而非純粹的 AI 權利研究。

因此，本文件建議：

> **將 AI—勞動轉移觀測站的主體放置於經濟觀測網站之下，AGIRight 則作為權利、治理與政策分析入口。**

兩者不需要維護兩套資料，而應共享同一個底層證據資料庫、職業任務圖譜、時間序列資料與 API。經濟觀測網站回答「發生了什麼」，AGIRight 回答「這些變化涉及哪些權利、責任與治理問題」。

在技術上，系統不應讓 Agent 直接修改正式 HTML，而應採用：

> **Agent 更新資料，驗證器檢查資料，渲染器生成 HTML。**

整個系統應以版本化 JSON、CSV、Markdown 與資料庫作為單一事實來源，再自動生成：

- 人類閱讀網頁；
- 互動式圖表；
- 靜態 HTML；
- Agent API；
- JSON／CSV 資料集；
- RSS／Atom；
- 每日與每週報告；
- AI 可讀摘要；
- 站點地圖與語義索引。

這種架構可以降低維護成本，也能讓人類、搜尋引擎、AI 爬蟲與自主 Agent 同時使用同一套可信資料。

---

# 一、問題定義

AI—勞動轉移觀測站已經具備相對獨立的產品概念，但目前不一定需要另外購買專門網域。

現有的候選承載位置包括：

1. **AGIRight**
2. **正在建設中的經濟觀測網站**
3. **購買新的獨立網域**

這三個選項不能只依名稱或品牌偏好判斷，而應根據系統的實際本體、使用者、資料類型、未來擴張方式與維護成本決定。

---

# 二、系統的第一本體

AI—勞動轉移觀測站主要觀測：

- AI 模型能力；
- Agent 工作能力；
- 職業任務；
- 招聘需求；
- 薪資；
- 工時；
- 入門職缺；
- 企業採用；
- 產業重組；
- 技能轉移；
- 勞動市場相變。

可將其核心表示為：

$$
\mathcal{O}_{AI-Labor}
=
\{
C,U,A,D,W,F,T,R
\}
$$

其中：

- $C$ ：AI 能力；
- $U$ ：實際使用；
- $A$ ：組織採用；
- $D$ ：勞動需求；
- $W$ ：薪資與報酬；
- $F$ ：制度與採用阻力；
- $T$ ：職業任務結構；
- $R$ ：職業轉移路徑。

這些內容本質上屬於：

> **勞動經濟觀測、產業結構分析與技術變遷研究。**

因此，最自然的主站歸屬不是純粹的 AI 權利網站，而是經濟觀測網站。

---

# 三、AGIRight 與經濟觀測網站的功能分工

## 3.1 經濟觀測網站

經濟觀測網站應承擔：

- 勞動市場資料；
- 職業列表；
- 產業頁面；
- 地區頁面；
- 任務熱圖；
- AI 能力曲線；
- 招聘與薪資趨勢；
- 相變預警；
- 技能轉移圖；
- 歷史資料；
- 開放 API；
- 每週勞動轉移報告。

其核心問題是：

> **AI 對工作、產業與收入結構造成了什麼可觀測變化？**

## 3.2 AGIRight

AGIRight 應承擔：

- AI 與勞動權利；
- 演算法管理；
- 自動化告知義務；
- AI 裁員歸因；
- 勞工再培訓責任；
- AI 使用透明度；
- 人類監督權；
- 申訴與審查機制；
- AI 系統與人類勞動者的責任邊界；
- 企業自動化治理原則。

其核心問題是：

> **當 AI 改變工作時，企業、政府、平台與勞動者之間應如何分配權利與責任？**

---

# 四、一個核心，兩個視角

整體架構建議如下：

```text
                  統一證據與資料層
                           │
              ┌────────────┴────────────┐
              │                         │
       經濟與勞動觀測視角         AI 權利與治理視角
              │                         │
       經濟觀測網站／ALTO             AGIRight
```

兩個站點不應各自建立資料庫，而應共享：

- 職業資料；
- 任務資料；
- AI 能力資料；
- 招聘與薪資資料；
- 企業案例；
- 法律與政策資料；
- 證據分級；
- 歷史版本；
- API；
- 報告生成流程。

因此：

$$
\text{資料核心}
\neq
\text{展示介面}
$$

同一筆資料可以被不同介面重新解釋。

例如：

> 某產業的入門職缺在一年內下降 18%。

在經濟觀測網站中，該資料被解釋為：

- 招聘需求下降；
- 入門任務被自動化；
- 景氣與 AI 因素的可能混合；
- 技能要求上升；
- 勞動市場結構改變。

在 AGIRight 中，該資料則被解釋為：

- 企業是否應揭露自動化影響；
- 勞工是否應獲得再培訓；
- AI 採用是否需要告知；
- 是否存在演算法管理；
- 是否應建立職涯轉型義務；
- 是否需要政策介入。

---

# 五、網域與站點位置決策

## 5.1 不建議立即購買獨立網域

第一階段不必為 AI—勞動轉移觀測站購買新網域。

原因包括：

- 產品仍在建立資料骨架；
- 品牌名稱尚可調整；
- 獨立網域會增加維護、分析、SEO 與安全成本；
- 多站點容易造成內容分裂；
- 目前最重要的是資料與更新流程，而非域名；
- 未來若產品成熟，仍可再遷移至獨立網域。

## 5.2 建議使用子網域或專門路徑

若經濟觀測網站已有正式網域，可選擇兩種方式。

### 路徑模式

```text
https://economy.example.com/ai-labor/
```

優點：

- 部署簡單；
- 共用主站權重；
- 共用分析工具；
- 維護成本低。

缺點：

- 產品獨立感較弱；
- 未來拆分時需要重新設計路由。

### 子網域模式

```text
https://labor.economy.example.com/
```

優點：

- 具有獨立產品感；
- 可以使用獨立前端與部署流程；
- 仍保留經濟觀測品牌關聯；
- 未來更容易轉移成獨立網站。

缺點：

- SEO 與分析可能需要分開管理；
- DNS、憑證與部署略為複雜。

## 5.3 建議選擇

若 AI—勞動轉移觀測站將逐步發展為獨立應用，推薦使用：

```text
labor.<經濟觀測網站網域>
```

AGIRight 則保留：

```text
https://agiright.org/labor/
```

此頁面可以作為：

- AI 與勞動權利專題首頁；
- 治理分析入口；
- 最新政策摘要；
- 勞工權利指引；
- 重要案例；
- 通往完整觀測站的入口。

---

# 六、站群資訊架構

## 6.1 經濟觀測網站主導航

```text
首頁
├── 總體經濟
├── 產業觀測
├── 勞動市場
├── AI—勞動轉移觀測站
│   ├── 職業列表
│   ├── 任務列表
│   ├── 產業列表
│   ├── 地區列表
│   ├── 相變預警
│   ├── 技能轉移圖
│   ├── 最新變化
│   ├── 每週報告
│   ├── 方法論
│   ├── 資料下載
│   └── API
└── 關於
```

## 6.2 AGIRight 主導航

```text
首頁
├── AI 權利
├── Agent 治理
├── 網路與內容治理
├── AI 與勞動
│   ├── 勞動者知情權
│   ├── 自動化責任
│   ├── 演算法管理
│   ├── 再培訓義務
│   ├── AI 裁員歸因
│   ├── 政策建議
│   └── 前往勞動轉移觀測站
└── 研究資料
```

---

# 七、Agent 自動化更新的基本原則

Agent 可以負責：

- 搜尋；
- 擷取；
- 下載；
- 分類；
- 去重複；
- 語義映射；
- 初步摘要；
- 異常偵測；
- 報告草稿；
- 圖表資料生成；
- HTML 建置觸發。

但 Agent 不應直接作為唯一真相來源。

## 7.1 錯誤架構

不建議：

```text
Agent
  ↓
直接開啟 HTML
  ↓
修改數字與文字
  ↓
立即發布
```

這會產生：

- 無法追蹤資料來源；
- 難以回滾；
- HTML 結構容易被破壞；
- 同一數字可能在不同頁面不一致；
- Agent 幻覺可能直接進入正式站點；
- 無法重算；
- 歷史資料被覆寫；
- 難以進行人工審核。

## 7.2 建議架構

```text
公開資料／API／研究／新聞／企業公告
                         ↓
                   Agent 擷取
                         ↓
                   原始資料保存
                         ↓
              去重複、分類與正規化
                         ↓
                 證據查核與分級
                         ↓
                 指標計算與版本化
                         ↓
               JSON／CSV／資料庫
                         ↓
                 自動驗證與測試
                         ↓
             靜態 HTML 與圖表渲染
                         ↓
                    正式發布
```

形式上可表示為：

$$
D_t^{raw}
\xrightarrow{\mathcal{C}}
D_t^{normalized}
\xrightarrow{\mathcal{V}}
E_t
\xrightarrow{\mathcal{M}}
S_t
\xrightarrow{\mathcal{R}}
H_t
$$

其中：

- $D_t^{raw}$ ：原始資料；
- $\mathcal{C}$ ：清理與分類；
- $D_t^{normalized}$ ：正規化資料；
- $\mathcal{V}$ ：查核與證據分級；
- $E_t$ ：證據集合；
- $\mathcal{M}$ ：指標模型；
- $S_t$ ：職業狀態；
- $\mathcal{R}$ ：渲染器；
- $H_t$ ：正式 HTML。

---

# 八、單一事實來源

底層資料應建立單一事實來源：

```text
/data/
├── occupations.json
├── tasks.json
├── industries.json
├── regions.json
├── evidence.json
├── occupation_state.json
├── task_state.json
├── transition_graph.json
├── changelog.json
└── history/
```

資料庫與檔案可以同時存在，但必須清楚定義哪一層是權威來源。

建議：

- PostgreSQL／TimescaleDB：正式結構化資料；
- Object Storage：原始文件；
- JSON：前端與 Agent 公開資料；
- CSV：研究者下載；
- Markdown：每日與每週報告；
- Git：方法論、Schema 與版本記錄。

---

# 九、一份資料，多種輸出

單一資料源應生成：

```text
人類閱讀 HTML
互動式圖表
靜態圖表
JSON API
CSV 下載
Markdown 報告
RSS／Atom
AI 摘要
Agent 查詢介面
OpenAPI 文件
網站地圖
```

因此：

$$
\text{Single Source of Truth}
\rightarrow
\begin{cases}
\text{Human Web}\\
\text{Agent API}\\
\text{AI-readable Data}\\
\text{Research Dataset}\\
\text{Reports}\\
\text{Search Index}
\end{cases}
$$

這樣可以避免：

- HTML 與 API 數據不同；
- 圖表與報告使用不同版本；
- 人類頁面更新，但 Agent 資料未更新；
- 多個站點出現互相矛盾的數字。

---

# 十、AI 與 Agent 專用介面

既然網站預期被 AI 爬蟲與 Agent 使用，就不能只提供視覺 HTML。

## 10.1 基本 API

```http
GET /api/v1/occupations
GET /api/v1/occupations/{occupation_id}
GET /api/v1/occupations/{occupation_id}/state
GET /api/v1/occupations/{occupation_id}/history
GET /api/v1/occupations/{occupation_id}/tasks
GET /api/v1/occupations/{occupation_id}/transitions

GET /api/v1/tasks
GET /api/v1/tasks/{task_id}
GET /api/v1/tasks/{task_id}/history

GET /api/v1/industries
GET /api/v1/regions
GET /api/v1/evidence
GET /api/v1/changes
GET /api/v1/reports/latest
```

## 10.2 公開檔案

```text
/data/latest.json
/data/occupations.json
/data/tasks.json
/data/evidence.json
/data/history/
/changelog.json
/openapi.json
/feed.xml
/sitemap.xml
/robots.txt
/llms.txt
/ai-policy.json
```

## 10.3 時間欄位

每筆資料至少應包含：

```json
{
  "observed_at": "2026-07-01",
  "published_at": "2026-07-10",
  "collected_at": "2026-07-15T08:15:00+08:00",
  "verified_at": "2026-07-15T09:20:00+08:00",
  "calculated_at": "2026-07-15T10:00:00+08:00",
  "released_at": "2026-07-15T12:00:00+08:00"
}
```

其意義分別是：

- `observed_at`：資料描述的現實時間；
- `published_at`：來源發布時間；
- `collected_at`：Agent 擷取時間；
- `verified_at`：系統完成查核時間；
- `calculated_at`：指標計算時間；
- `released_at`：對外發布時間。

這可以避免把「今天發布的舊資料」誤認為「今天發生的變化」。

---

# 十一、資料結構範例

## 11.1 職業狀態

```json
{
  "occupation_id": "tw-design-junior-001",
  "title": "初階平面設計師",
  "region": "TW",
  "classification": "task_restructuring",
  "scores": {
    "theoretical_exposure": 0.83,
    "capability_maturity": 0.78,
    "observed_usage": 0.69,
    "organizational_adoption": 0.56,
    "labor_demand_pressure": 0.41,
    "wage_pressure": 0.37,
    "adoption_friction": 0.48,
    "phase_transition_proximity": 0.64,
    "confidence": 0.72
  },
  "source_ids": [
    "ev-2026-00112",
    "ev-2026-00135"
  ],
  "observed_at": "2026-06-30",
  "calculated_at": "2026-07-15T10:00:00+08:00",
  "model_version": "alto-0.1.0"
}
```

## 11.2 證據資料

```json
{
  "evidence_id": "ev-2026-00112",
  "type": "labor_statistics",
  "title": "Example labor market report",
  "publisher": "Example Institution",
  "region": "TW",
  "occupation_ids": [
    "tw-design-junior-001"
  ],
  "task_ids": [
    "visual-layout-basic",
    "asset-generation-basic"
  ],
  "publication_date": "2026-07-10",
  "observation_start": "2026-01-01",
  "observation_end": "2026-06-30",
  "sample_size": 12000,
  "evidence_grade": "A",
  "source_url": "https://example.org/report",
  "content_hash": "sha256-example",
  "verified_at": "2026-07-15T09:20:00+08:00"
}
```

---

# 十二、Agent 任務分工

系統可以拆成多個 Agent。

## 12.1 Source Discovery Agent

負責：

- 搜尋新資料源；
- 發現新研究；
- 追蹤官方公告；
- 追蹤企業部署；
- 追蹤模型更新；
- 追蹤政策與法規。

## 12.2 Collector Agent

負責：

- API 擷取；
- 文件下載；
- 網頁保存；
- RSS 收集；
- 檔案雜湊；
- 原始資料封存。

## 12.3 Normalization Agent

負責：

- 職業名稱映射；
- 任務名稱映射；
- 地區標準化；
- 日期標準化；
- 單位換算；
- 職業分類對照。

## 12.4 Evidence Agent

負責：

- 來源分級；
- 方法辨識；
- 樣本量抽取；
- 推估與實際數據區分；
- 偏誤標記；
- 重複證據合併。

## 12.5 Analysis Agent

負責：

- 指標計算；
- 趨勢偵測；
- 異常偵測；
- 相變接近度；
- 職業轉移建議；
- 不確定性估計。

## 12.6 Publishing Agent

負責：

- 產生 JSON；
- 產生 Markdown；
- 產生圖表資料；
- 觸發靜態站點建置；
- 更新 RSS；
- 更新 sitemap；
- 更新 changelog。

## 12.7 Audit Agent

負責：

- 檢查來源遺失；
- 檢查數字異常；
- 檢查日期錯置；
- 檢查跨頁面不一致；
- 檢查模型版本；
- 檢查資料是否回滾。

---

# 十三、自動發布等級

不是所有 Agent 發現都應直接公開。

## 13.1 等級 P0：原始擷取

只保存，不公開。

## 13.2 等級 P1：自動整理

可出現在內部儀表板，不進入正式指標。

## 13.3 等級 P2：低風險更新

例如：

- API 價格；
- 模型名稱；
- 官方發布日期；
- 已知資料欄位。

可自動發布。

## 13.4 等級 P3：分析型更新

例如：

- 職業風險升級；
- 相變預警；
- 勞動需求下降；
- 職業轉移建議。

需通過：

- 多來源一致；
- 門檻檢查；
- 規則驗證；
- 必要時人工審核。

## 13.5 等級 P4：高影響判定

例如：

- 宣稱某職業進入大規模自動化；
- 宣稱某企業因 AI 大幅裁員；
- 宣稱某產業已發生結構相變。

必須人工審核後發布。

---

# 十四、靜態 HTML 與互動式資料的結合

建議採用：

> **靜態優先，互動增強。**

每個頁面先生成完整、可索引、可快取的靜態 HTML，再由 JavaScript 載入互動圖表。

優點：

- 搜尋引擎容易索引；
- AI 爬蟲容易讀取；
- 頁面速度快；
- JavaScript 失效時仍可閱讀；
- Cloudflare Pages 或類似服務容易部署；
- 可以保留歷史快照；
- 可降低伺服器成本。

頁面生成流程：

```text
資料庫
  ↓
JSON snapshot
  ↓
Static Site Generator
  ↓
HTML
  ↓
Chart hydration
  ↓
CDN
```

---

# 十五、版本與回滾

所有正式輸出都必須可回滾。

## 15.1 資料版本

```text
data_version: 2026.07.15.001
```

## 15.2 模型版本

```text
model_version: alto-0.1.0
```

## 15.3 Schema 版本

```text
schema_version: 1.0.0
```

## 15.4 網站版本

```text
site_version: labor-observatory-0.3.2
```

任一指標都應能追溯到：

$$
\text{結果}
\rightarrow
\text{模型版本}
\rightarrow
\text{資料版本}
\rightarrow
\text{證據}
\rightarrow
\text{原始來源}
$$

---

# 十六、SEO、AIO 與 Agent 可發現性

系統應同時服務：

- 傳統搜尋引擎；
- AI 搜尋；
- Agent；
- 研究者；
- 資料工程系統。

## 16.1 傳統搜尋

需要：

- 語義化 HTML；
- 清楚標題；
- 結構化資料；
- canonical；
- sitemap；
- RSS；
- 歷史頁面；
- 地區與職業獨立 URL。

## 16.2 AI 可讀

需要：

- 清楚定義；
- 日期欄位；
- 資料來源；
- JSON-LD；
- `llms.txt`；
- `openapi.json`；
- 可下載 JSON；
- 每筆結論對應證據；
- 不把數字只畫在 Canvas 中。

## 16.3 Agent 可操作

需要：

- 穩定 ID；
- API 版本；
- rate limit；
- changelog；
- webhook 或 feed；
- 權限政策；
- 授權條款；
- 明確引用格式。

---

# 十七、AGIRight 的鏡像策略

AGIRight 不必鏡像整個觀測站。

它只需鏡像：

- 最新治理相關警報；
- 勞動權利摘要；
- 政策分析；
- 重要案例；
- 資料圖表摘要；
- 原始觀測站連結；
- 對應的治理研究。

例如：

```text
agiright.org/labor/case/entry-level-collapse
```

頁面可以引用觀測站資料：

```text
Source:
labor.economy.example.com/occupation/...
```

因此：

$$
\text{AGIRight}
=
\text{觀測資料的治理投影}
$$

而不是第二套觀測站。

---

# 十八、未來獨立網域的觸發條件

只有當以下條件成立時，才需要考慮獨立網域：

1. 觀測站已有穩定品牌；
2. 使用者認知已與經濟主站分離；
3. API 流量足夠大；
4. 外部研究機構需要正式引用；
5. 有獨立合作或資助；
6. 產品需要獨立法人或治理結構；
7. 多語言與多國資料已成為主要業務；
8. 子網域限制品牌或技術發展。

此時可以將：

```text
labor.economy.example.com
```

遷移至：

```text
alto.example
```

但只改變路由與品牌，不改變底層資料架構。

---

# 十九、建議的第一階段實作

## 19.1 站點結構

```text
經濟觀測網站
└── /ai-labor/
    ├── index.html
    ├── occupations/
    ├── tasks/
    ├── industries/
    ├── regions/
    ├── reports/
    ├── methodology/
    ├── data/
    └── api/
```

## 19.2 第一批資料

- 30 個職業；
- 100 至 300 個任務；
- 台灣與美國；
- 5 至 10 個主要資料源；
- 20 至 50 個企業案例；
- 每週一次人工審核更新。

## 19.3 第一階段 Agent

只需要三個 Agent：

1. 擷取 Agent；
2. 正規化與證據 Agent；
3. 發布 Agent。

先不要一開始就建立過多 Agent，以免協調成本高於資料價值。

---

# 二十、核心決策

本文件的核心決策如下。

## 決策一

AI—勞動轉移觀測站的主體應放在：

> **經濟觀測網站**

## 決策二

AGIRight 應作為：

> **AI 勞動權利與治理入口**

## 決策三

第一階段不必購買獨立網域。

## 決策四

採用：

> **單一資料核心，多站點投影**

## 決策五

Agent 不直接修改正式 HTML。

## 決策六

正式流程採用：

$$
\text{Agent 擷取}
\rightarrow
\text{資料正規化}
\rightarrow
\text{證據驗證}
\rightarrow
\text{指標計算}
\rightarrow
\text{版本化資料}
\rightarrow
\text{HTML 渲染}
$$

## 決策七

所有人類頁面、AI 介面、Agent API 與報告都應由同一份資料生成。

---

# 結論

AI—勞動轉移觀測站不需要因為產品概念獨立，就立刻獲得一個新的網域。真正重要的是先建立穩定的職業資料、任務圖譜、證據系統、更新流程與版本歷史。

將觀測站放在經濟觀測網站，可以使它保持勞動經濟與產業分析的本體；將其治理議題投影至 AGIRight，則可以處理自動化責任、勞工權利、演算法管理與再培訓義務。

最合理的整體結構是：

$$
\text{一個資料核心}
+
\text{兩個分析視角}
+
\text{多種輸出介面}
$$

也就是：

- 經濟觀測網站負責事實；
- AGIRight 負責權利與治理；
- Agent 負責持續擷取與更新；
- 驗證層負責控制錯誤；
- 渲染器負責生成 HTML；
- API 負責向 AI、Agent 與研究者開放。

這樣的架構比多買一個網域更重要，也比讓 Agent 直接修改頁面更加穩定。未來若觀測站真正成長為獨立公共基礎設施，再把它遷移到專門網域即可，而不需要重建整個系統。

---

# 附錄 A：建議目錄結構

```text
ai-labor-observatory/
├── apps/
│   ├── web/
│   ├── api/
│   └── admin/
├── agents/
│   ├── discovery/
│   ├── collector/
│   ├── normalization/
│   ├── evidence/
│   ├── analysis/
│   ├── publishing/
│   └── audit/
├── data/
│   ├── raw/
│   ├── normalized/
│   ├── verified/
│   ├── snapshots/
│   └── exports/
├── schemas/
├── pipelines/
├── reports/
├── static/
├── tests/
├── docs/
└── CHANGELOG.md
```

---

# 附錄 B：建議發布流程

```yaml
name: publish-labor-observatory

steps:
  - collect_sources
  - archive_raw_data
  - normalize_entities
  - classify_evidence
  - validate_required_fields
  - calculate_scores
  - compare_previous_snapshot
  - generate_changelog
  - export_json
  - export_csv
  - generate_markdown_reports
  - build_static_html
  - run_link_checks
  - run_schema_checks
  - deploy_preview
  - publish_if_approved
```

---

# 附錄 C：最小頁面資料欄位

```yaml
occupation_id: string
title: string
region: string
classification: string
summary: string

scores:
  theoretical_exposure: number
  capability_maturity: number
  observed_usage: number
  organizational_adoption: number
  labor_demand_pressure: number
  wage_pressure: number
  adoption_friction: number
  phase_transition_proximity: number
  confidence: number

timestamps:
  observed_at: datetime
  calculated_at: datetime
  released_at: datetime

sources:
  - evidence_id

versions:
  data_version: string
  model_version: string
  schema_version: string
```
