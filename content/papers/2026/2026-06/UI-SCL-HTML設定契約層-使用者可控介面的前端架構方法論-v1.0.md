# UI-SCL：HTML 設定契約層——使用者可控介面的前端架構方法論

**作者**：Neo K.  
**機構**：一言諾科技有限公司（EveMissLab）  
**版本**：v1.0  
**日期**：2026年6月  
**文件類型**：Markdown 技術白皮書 / 方法論論文  

---

## 摘要

本文提出「UI 設定契約層」（UI Settings Contract Layer, UI-SCL）作為現代 HTML / Web 前端系統中的先行架構方法論。其核心主張是：前端 UI 不應只是賣方展示資訊、引導點擊與堆疊功能的介面，而應是使用者在安全與必要資訊邊界內，能夠調整自身注意力、偏好、密度、排序、主題、語言與互動節奏的可控環境。

在傳統前端開發中，設定通常被視為附屬功能：先完成頁面與功能，再補上深色模式、字體大小、語言切換、通知開關或個人化推薦。然而在 AI 編碼、人機協作、Vibe Coding 與未來意圖語言開發模式下，這種「功能先行、設定後補」的方式會迅速產生結構債。當 AI 或人類開發者先把偏好、顯示規則、互動方式硬編在各個 component 裡，後續若要讓使用者控制介面，就必須到處拆除隱性假設，造成維護困難、設定分裂與協作混亂。

本文主張，凡具備一定規模的 HTML 網頁、Web App、前端平台、AI 工具介面或內容型網站，都應在功能實作前建立 UI-SCL。UI-SCL 定義使用者能控制什麼、不能控制什麼；哪些偏好可以匿名保存，哪些偏好需要登入同步；哪些資訊可隱藏、排序、降噪、聚焦；哪些內容因安全、交易、法規或誠信原因不得關閉；以及 AI 在生成前端程式碼時應遵守哪些設定協議。

本文將 UI-SCL 視為 SCL（Settings Contract Layer, 設定契約層）在前端介面領域的具體化，同時也是 ICL（Intent Collaboration Layer, 意圖協作層）在 AI 前端生成中的操作基礎。它不只是前端工程技巧，而是一種使用者主權、介面倫理、資訊降噪與 AI 協作開發的共同方法論。

**關鍵詞**：HTML、前端架構、UI 設定層、使用者偏好、個人化介面、Vibe Coding、AI 協作開發、設定契約層、使用者主權、可控 UI

---

## 第一章：問題陳述——前端 UI 的賣方中心困境

### 1.1 UI 原本應為使用者而設計

UI 的字面意義是 User Interface，即使用者介面。這意味著 UI 的正當性並不來自賣方想展示什麼，而是來自使用者如何理解、操作、選擇與控制系統。介面存在的目的，是降低使用者與系統之間的摩擦，使使用者能以更低成本完成自身目標。

然而現代網頁與應用介面長期受到商業邏輯、廣告邏輯、平台留存邏輯與資料蒐集邏輯影響。大量介面實際上不是為使用者服務，而是為供應方服務：推薦欄、熱門榜、彈窗、促銷訊息、強制登入提示、演算法排序、通知誘導、無止盡滑動與注意力捕捉機制，常常凌駕於使用者本身的需求之上。

這導致一個根本矛盾：UI 名義上是 User Interface，實際上卻常常成為 Seller Interface、Platform Interface 或 Attention Extraction Interface。使用者被迫在賣方預設的資訊結構中行動，而不是依照自己的偏好、節奏與目的重新配置介面。

UI-SCL 的出發點正是修正這個矛盾。

### 1.2 靜態 HTML 與固定 UI 的限制

早期 HTML 主要負責標記文件結構：標題、段落、列表、連結、圖片、表格。其核心任務是呈現內容。隨著 CSS、JavaScript、Web API 與前端框架發展，網頁逐漸從文件頁面演化為互動應用。今天的 HTML 不是單純文件容器，而是複雜應用介面的入口。

然而許多前端系統仍然沿用靜態頁面的思維：設計師與開發者先決定頁面長相，再把所有使用者帶進同一套結構。使用者最多能選擇明暗模式、語言、通知開關或帳號偏好，但很少能深度控制介面本身。

例如，內容型網站通常預設展示推薦文章、熱門文章、廣告區塊、相關連結與社群分享工具；電商網站通常預設展示促銷、加購、倒數、推薦商品；AI 工具網站可能預設展示模板、歷史紀錄、側邊欄、提示詞範例與實驗功能。這些元素未必對每個使用者有用，但大多數介面沒有把「隱藏」、「降噪」、「專注」、「重排」、「密度調整」視為一等功能。

UI-SCL 主張，未來前端不應再把使用者偏好當作附屬設定，而應把可控性納入 HTML / UI 的基礎設計。

### 1.3 AI 編碼時代使設定層更加必要

在 AI 編碼與 Vibe Coding 模式下，前端生成速度大幅提高。人類可以用自然語言要求 AI 生成頁面、元件、表單、設定面板、儀表板與互動流程。這提高了開發效率，但也放大了隱性結構問題。

如果沒有先定義 UI-SCL，AI 很容易將偏好與顯示邏輯散落在各個 component 中。例如：

```text
Header 自己管理主題
Sidebar 自己管理開合
ArticleList 自己管理排序
Notification 自己管理顯示頻率
RecommendationPanel 自己管理隱藏狀態
LocalStorage key 到處命名
CSS class 與 data attribute 無統一規則
```

短期看，頁面可能可以運作。長期看，這會形成嚴重的設定分裂。當使用者要求「我不想看到推薦內容」、「我想專注模式」、「我想登入前後偏好一致」、「我想讓 AI 幫我重構 UI」時，開發者或下一個 AI 必須逐一追蹤各元件內部假設。這正是前端領域的「翻腸子」問題。

因此，越是 AI 編碼時代，越需要先建立設定契約層。AI 不應在沒有設定契約的狀態下自由生成 UI；AI 應在明確的 UI-SCL 中生成可控、可讀、可交接的前端結構。

---

## 第二章：UI-SCL 的定義

### 2.1 基本定義

UI-SCL（UI Settings Contract Layer）是 HTML / Web 前端系統中的設定契約層。它定義使用者能如何控制介面，包括視覺主題、版面密度、內容顯示、資訊排序、互動提示、通知頻率、語言偏好、可及性需求、專注模式與匿名或會員偏好保存機制。

簡言之：

> HTML 定義頁面有什麼；UI-SCL 定義使用者能如何重組這個頁面。

UI-SCL 不是單一 `settings.json`，也不是一個設定頁面。它是一組前端架構約定，通常包含：

```text
1. UI 設定 schema
2. 預設設定檔
3. 使用者設定檔
4. 設定載入器
5. 設定提供器
6. UI 元件讀取規範
7. 設定持久化策略
8. 可隱藏內容註冊表
9. 不可隱藏資訊白名單
10. AI 生成前端時的協議文件
```

### 2.2 UI-SCL 與一般設定功能的差異

一般設定功能通常是功能完成後才補上的選單，例如「深色模式」、「語言切換」、「通知開關」。這種設定是附屬的、局部的、常常只影響少數 UI 狀態。

UI-SCL 則不同。它是功能開始前就存在的介面契約。它要求開發者先回答：

```text
這個介面有哪些可變項？
哪些資訊對使用者是必要的？
哪些資訊只是平台想推送的？
使用者可以隱藏哪些區塊？
使用者可以調整哪些視覺參數？
偏好要保存在哪裡？
匿名使用者能不能保存偏好？
會員登入後偏好如何同步？
AI 生成新 component 時要如何接入設定層？
```

這些問題若不在開場先回答，後期就會被各個 component 自行決定。當每個 component 都有自己的偏好邏輯，整個 UI 就失去整體治理。

### 2.3 UI-SCL 作為使用者主權聲明

UI-SCL 的更深意義是使用者主權聲明。它不只處理「技術上能不能設定」，而是處理「使用者是否有權調整自己的介面」。

使用者主權不是無限制自由。它不是讓使用者任意關閉安全警告、隱藏付款金額、略過法規告知或取消刪除確認。相反，真正成熟的使用者主權，是在必要資訊、安全邊界與系統誠信不受破壞的前提下，最大化使用者對注意力環境的控制。

因此，UI-SCL 需要同時定義兩類邊界：

```text
可控制邊界：使用者可以調整、隱藏、排序、聚焦、保存的內容。
不可控制邊界：基於安全、法律、交易、資料完整性而必須呈現的內容。
```

這使 UI-SCL 不只是前端架構，而是介面倫理與產品哲學。

---

## 第三章：使用者可控 UI 原則

### 3.1 原則定義

本文提出「使用者可控 UI 原則」（User-Controlled Interface Principle）：

> 在現代前端設計中，UI 不應只是賣方展示資訊與引導行為的介面，而應是使用者調整注意力、偏好、密度與互動節奏的可控環境。因此，任何具備一定規模的 HTML / Web App，都應在功能實作前建立 UI 設定層，明確聲明哪些內容可隱藏、哪些偏好可保存、哪些介面可調整，以及哪些資訊因安全、交易或法規原因不可關閉。

這條原則的核心不是「所有頁面都要複雜個人化」，而是「所有足夠複雜的 UI 都應先思考可控性」。

### 3.2 注意力是介面設計的核心資源

UI 不只是一組視覺元件。UI 實際上是在分配使用者注意力。字體大小、色彩、位置、彈窗、通知、推薦、排序、側邊欄、固定導航列、無限滾動，都在決定使用者看到什麼、忽略什麼、先做什麼、停留多久。

如果注意力完全由平台決定，使用者就只是被動接收者。若 UI-SCL 允許使用者調整注意力環境，介面才真正轉向使用者中心。

例如：

```text
使用者可以關閉推薦欄，專注閱讀文章。
使用者可以把工具欄移到左側，符合自己的操作習慣。
使用者可以提高文字大小，降低閱讀負擔。
使用者可以降低動畫，避免分心或不適。
使用者可以選擇只顯示核心功能，隱藏實驗功能。
使用者可以保存偏好，不必每次重新設定。
```

這些不是瑣碎功能，而是對使用者注意力的尊重。

### 3.3 UI 應從展示介面變成調適環境

傳統 UI 設計常常把頁面視為一張固定海報：設計師決定布局，使用者接受。現代 Web App 應轉向調適環境：系統提供可變參數，使用者依自己的需求調整。

展示介面關心的是：

```text
我們想讓使用者看到什麼？
我們想讓使用者點什麼？
我們想讓使用者停留在哪裡？
```

調適環境關心的是：

```text
使用者想完成什麼？
使用者想少看什麼？
使用者想集中注意力在哪裡？
使用者是否需要不同閱讀密度？
使用者是否需要不同互動節奏？
使用者是否需要可及性調整？
```

UI-SCL 正是從展示介面走向調適環境的架構基礎。

---

## 第四章：HTML、CSS、JavaScript 與 UI-SCL 的關係

### 4.1 HTML：語義骨架

HTML 定義頁面結構與語義。良好的 HTML 應該讓人類、瀏覽器、搜尋引擎、輔助科技與 AI 都能理解頁面內容。例如標題使用 `<h1>` 至 `<h6>`，主內容使用 `<main>`，導航使用 `<nav>`，文章使用 `<article>`，側邊區塊使用 `<aside>`。

在 UI-SCL 中，HTML 還應承擔一個任務：讓可控制區塊具備清楚標記。也就是說，前端不只要寫出看起來能用的 HTML，還要讓設定層知道哪些區塊可被調整。

例如：

```html
<aside data-ui-region="recommendations" data-user-hideable="true">
  ...
</aside>

<section data-ui-region="legal-notice" data-user-hideable="false">
  ...
</section>
```

這種標記讓 UI 的可控制性不再隱藏於 JavaScript 內部，而是進入 HTML 語義層。

### 4.2 CSS：設定映射層

CSS 不應只是固定樣式檔，也應是設定層的映射器。UI-SCL 可透過 CSS variables、data attributes、class strategy 或 cascade layers 將設定轉換為視覺效果。

例如：

```css
:root {
  --font-scale: 1;
  --content-width: 960px;
  --motion-level: normal;
}

body[data-density="compact"] {
  --content-width: 1120px;
}

body[data-density="comfortable"] {
  --content-width: 900px;
}

body[data-focus-mode="true"] [data-ui-region="recommendations"],
body[data-focus-mode="true"] [data-ui-region="trending"] {
  display: none;
}
```

這種方式讓設定與視覺呈現保持明確對應，而不是把所有邏輯寫死在 component 中。

### 4.3 JavaScript：設定載入與狀態治理

JavaScript 負責載入、驗證、套用、保存與同步 UI 設定。它不應讓每個 component 自行從 localStorage 讀寫偏好，而應建立統一的 Settings Provider 或 Config Registry。

最小流程如下：

```text
default-ui-settings.json
      ↓
ui-settings.schema.json
      ↓
settings-loader.js
      ↓
settings-provider.js
      ↓
component rendering / CSS data attributes
      ↓
localStorage / server profile / session fallback
```

這個流程確保設定具有預設值、驗證規則、讀取介面與持久化策略。

---

## 第五章：UI-SCL 的核心組件

### 5.1 UI Settings Schema

Schema 是 UI-SCL 的骨架。它定義每個設定項的名稱、類型、預設值、可選範圍、用途、影響層級與安全限制。

例如：

```json
{
  "theme.mode": {
    "type": "enum",
    "options": ["light", "dark", "system"],
    "default": "system",
    "description": "控制介面明暗模式",
    "userEditable": true,
    "scope": "visual"
  },
  "content.hideRecommendations": {
    "type": "boolean",
    "default": false,
    "description": "是否隱藏推薦內容",
    "userEditable": true,
    "scope": "attention"
  },
  "security.showPaymentAmount": {
    "type": "boolean",
    "default": true,
    "description": "付款金額必須顯示，不得由使用者關閉",
    "userEditable": false,
    "scope": "safety"
  }
}
```

Schema 的價值不只是讓程式驗證設定，也是讓人類與 AI 知道這個 UI 系統允許什麼變動。

### 5.2 Default Settings

預設設定是系統對一般使用者的初始判斷。它應該保守、清晰、不過度打擾，並保留使用者調整空間。

例如：

```json
{
  "theme": {
    "mode": "system",
    "accentColor": "default"
  },
  "layout": {
    "density": "comfortable",
    "sidebar": "auto",
    "contentWidth": "normal"
  },
  "content": {
    "hideRecommendations": false,
    "hideTrending": false,
    "focusMode": false
  },
  "accessibility": {
    "fontScale": 1,
    "reduceMotion": false,
    "highContrast": false
  }
}
```

預設值不應只是開發者習慣，而應反映產品對使用者注意力與安全邊界的基本尊重。

### 5.3 User Settings

User Settings 是使用者實際偏好。它可能保存在 localStorage、sessionStorage、cookie、IndexedDB、server profile 或跨裝置帳號設定中。

UI-SCL 應明確區分：

```text
匿名偏好：不需登入即可保存，例如 theme、density、focusMode。
會員偏好：登入後跨裝置同步，例如 preferredSections、dashboardLayout。
敏感偏好：涉及隱私、通知、資料使用，需要更明確同意。
暫時偏好：只在本次 session 有效，例如臨時隱藏某個提示。
```

這種分類能避免所有設定混在一起，造成隱私與同步混亂。

### 5.4 UI Region Registry

UI Region Registry 是可控制區塊註冊表。它記錄每個 UI 區域是否可隱藏、可排序、可調密度、可移動，以及其必要性等級。

範例：

```json
{
  "recommendations": {
    "label": "推薦內容",
    "hideable": true,
    "reorderable": true,
    "required": false,
    "reason": "非必要內容，可依使用者偏好隱藏"
  },
  "payment-summary": {
    "label": "付款摘要",
    "hideable": false,
    "reorderable": false,
    "required": true,
    "reason": "交易必要資訊，不得隱藏"
  },
  "security-warning": {
    "label": "安全警告",
    "hideable": false,
    "reorderable": false,
    "required": true,
    "reason": "涉及帳號安全與風險提示"
  }
}
```

這使 UI 控制權不再依賴個別開發者判斷，而是進入可檢查的契約層。

### 5.5 Settings Provider

Settings Provider 是前端系統中的設定存取介面。所有 component 都應透過 Provider 取得設定，不應自行讀寫底層存儲。

偽代碼：

```javascript
const uiSettings = getUISettings();

if (uiSettings.content.hideRecommendations) {
  hideRegion("recommendations");
}
```

更成熟的寫法應是 component 只宣告自己受哪些設定影響，由渲染層統一處理：

```javascript
registerUIRegion({
  id: "recommendations",
  hideable: true,
  controlledBy: "content.hideRecommendations"
});
```

### 5.6 Persistence Adapter

Persistence Adapter 負責決定設定保存位置。不同產品可使用不同策略：

```text
localStorage：適合匿名偏好與簡單設定。
sessionStorage：適合短期狀態。
cookie：適合需與伺服器請求一起傳送的小型偏好，但需注意隱私。
IndexedDB：適合複雜本地資料與大型偏好配置。
Server Profile：適合會員跨裝置同步。
Hybrid Strategy：匿名本地保存，登入後合併到帳號設定。
```

UI-SCL 不強制使用某一種技術，而要求先明確定義策略。

---

## 第六章：非會員與會員偏好的雙軌保存

### 6.1 非會員也應擁有基本偏好權

許多網站把偏好保存綁定會員帳號。這在商業上可理解，但從使用者中心角度看，非會員也應享有基本介面控制權。使用者不登入，也應能選擇深色模式、字體大小、隱藏推薦內容或開啟專注模式。

非會員偏好可以透過本地存儲保存。這能降低使用門檻，也避免把「想讓介面舒服一點」變成強迫註冊的理由。

非會員可保存的偏好通常包括：

```text
theme
fontScale
density
reduceMotion
focusMode
hideRecommendations
preferredLanguage
lastVisitedSection
```

### 6.2 會員偏好的跨裝置同步

會員偏好則適合保存更完整的使用者設定，例如 dashboard layout、內容訂閱、常用功能、跨裝置主題、通知規則與 AI 工具偏好。

會員偏好應支援：

```text
跨裝置同步
版本遷移
偏好匯出
偏好重置
與匿名偏好合併
隱私權管理
```

當使用者從匿名狀態登入時，系統需要決定本地偏好與雲端偏好的合併規則。例如：

```text
本地偏好較新 → 詢問是否覆蓋雲端
雲端偏好較完整 → 合併非衝突項
安全相關偏好 → 不自動覆蓋，需確認
```

這些規則不應臨時寫在登入流程中，而應屬於 UI-SCL 的 persistence policy。

### 6.3 偏好保存的倫理邊界

保存偏好不等於追蹤使用者。UI-SCL 必須區分「使用者主動偏好」與「平台暗中蒐集行為」。

使用者主動偏好包括：

```text
我選擇深色模式。
我選擇隱藏推薦。
我選擇字體放大。
我選擇只看某些內容。
```

平台行為追蹤包括：

```text
系統記錄我停留在哪裡。
系統推測我的興趣。
系統依點擊行為建立個人化模型。
系統跨站追蹤我的偏好。
```

UI-SCL 處理的是使用者主動控制，不應被包裝成追蹤或操控工具。

---

## 第七章：內容可見性控制

### 7.1 隱藏不是刪除，而是注意力配置

使用者隱藏某個內容區塊，不代表該內容不存在，也不代表系統不提供。隱藏是一種注意力配置：使用者選擇現在不看、不需要、不想被干擾。

因此 UI-SCL 應支援：

```text
hide：隱藏區塊
collapse：收合區塊
mute：降低提示頻率
pin：固定重要區塊
prioritize：優先顯示某類內容
filter：過濾內容類型
sort：排序內容
focus：進入專注模式
```

這些操作本質上都是使用者對注意力環境的調整。

### 7.2 可隱藏內容與不可隱藏內容

可隱藏內容包括：

```text
推薦文章
熱門榜單
促銷區塊
非必要廣告
社群分享按鈕
實驗功能入口
提示範例
裝飾性動畫
非必要側邊欄
```

不可隱藏內容包括：

```text
付款金額
錯誤訊息
帳號安全警告
刪除確認
隱私權重大提示
法規必要揭露
交易條款確認
系統狀態異常
資料遺失警告
```

中間地帶則需要更細緻的政策。例如通知可以允許降低頻率，但不能讓使用者完全錯過安全警告；推薦可以隱藏，但搜尋結果不能被任意扭曲；促銷可以收合，但訂單費用不能弱化。

### 7.3 專注模式

專注模式是 UI-SCL 的典型應用。它不是單純把頁面變空，而是根據使用者任務重新配置 UI。

閱讀型專注模式可能隱藏：

```text
推薦欄
熱門欄
廣告
留言區
社群按鈕
非必要導航
```

寫作型專注模式可能保留：

```text
編輯器
字數統計
保存狀態
必要工具列
```

AI 工具專注模式可能保留：

```text
輸入框
輸出區
上下文文件
必要設定
執行狀態
```

同樣是 focusMode，不同產品應有不同映射。因此 focusMode 不應只是 CSS class，而應由 UI-SCL 定義其行為。

---

## 第八章：UI-SCL 與可及性

### 8.1 可及性不是額外功能

可及性常被誤解為只服務少數使用者的特殊功能。然而字體大小、對比度、動畫減少、鍵盤操作、語義標記、螢幕閱讀器支援，實際上都提升所有使用者在不同情境下的體驗。

UI-SCL 應把可及性設定納入核心，而不是放在角落。

基本可及性設定包括：

```text
fontScale
highContrast
reduceMotion
keyboardNavigation
screenReaderMode
lineHeight
contentWidth
colorBlindSafePalette
```

### 8.2 可及性與使用者主權

可及性本質上也是使用者主權。當使用者能調整字體、降低動畫、提高對比、改變密度，他就在重新配置介面與自身感知能力之間的關係。

這不是美化，而是讓介面服從人的身體與認知差異。

### 8.3 AI 生成前端時的可及性約束

AI 在生成前端時常會優先完成視覺樣式與互動效果，卻忽略語義標記、aria 屬性、鍵盤可用性與可及性設定。UI-SCL 應要求 AI 生成時遵守：

```text
不得用 div 取代所有語義元素。
互動元素必須可鍵盤操作。
重要內容不得只靠顏色表達。
動畫必須可被 reduceMotion 設定影響。
字體大小不得完全鎖死。
所有可隱藏區塊必須保留結構語義。
```

這使 AI 生成的 UI 更容易被人類、工具與輔助科技理解。

---

## 第九章：AI 編碼時代的 UI-SCL 協議

### 9.1 協議先於生成

在 Vibe Coding 中，人類常直接要求 AI：

```text
幫我做一個漂亮的首頁。
幫我做一個 dashboard。
幫我做一個設定頁。
幫我做一個文章列表。
```

這種提示可以快速得到結果，但往往缺乏架構約束。UI-SCL 要求在生成前先給 AI 一套協議：

```text
所有 UI 偏好必須來自 uiSettings。
不得在 component 內硬編碼偏好。
所有可隱藏區塊必須註冊到 UI Region Registry。
所有設定必須有 default、schema、description、fallback。
所有 localStorage key 必須集中定義。
所有 CSS 狀態必須由 data attributes 或 CSS variables 驅動。
所有安全必要資訊不得被 hideable 設定控制。
```

這些協議讓 AI 不只是生成畫面，而是在可治理架構中生成前端。

### 9.2 AI 生成 UI 的常見反模式

AI 生成前端常見問題包括：

```text
1. 硬編碼 theme、language、density。
2. 每個 component 各自讀寫 localStorage。
3. 設定名稱不一致。
4. CSS class 命名無規則。
5. 隱藏內容只用 display:none，沒有語義標記。
6. 重要安全資訊也被納入一般 hideable 設定。
7. 設定頁與實際 UI 狀態不同步。
8. 沒有 schema，導致 AI 後續不知道設定範圍。
9. 沒有 fallback，設定損壞時頁面異常。
10. 亂碼、奇怪命名、不可見字元進入程式碼。
```

UI-SCL 的任務就是提前阻止這些問題。

### 9.3 給 AI 的 UI-SCL Prompt 模板

以下是一個可用於 AI 前端生成的提示模板：

```text
你正在為一個 Web App 生成前端 UI。
必須遵守 UI-SCL 協議：

1. 所有使用者可調整的介面偏好，都必須定義在 ui-settings.schema.json。
2. 不得在任何 component 中硬編碼 theme、density、focusMode、language、hideRecommendations。
3. 所有 UI 區塊必須標記 data-ui-region。
4. 可隱藏區塊必須在 ui-region-registry.json 中註冊。
5. 安全、交易、錯誤、法規相關資訊不得設為 hideable。
6. CSS 必須優先使用 CSS variables 與 body data attributes 接收設定。
7. 所有設定讀取必須經過 SettingsProvider。
8. localStorage key 必須集中定義，不得散落在 component 中。
9. 生成程式碼不得包含亂碼、不可見 Unicode、無意義命名。
10. 請同時生成 schema、default settings、provider、範例 component。
```

這種提示能明顯提升 AI 生成前端的結構品質。

---

## 第十章：亂碼、命名與前端可交接性

### 10.1 前端亂碼的風險

前端系統中的亂碼不只影響顯示，也會影響協作與維護。亂碼可能出現在：

```text
HTML 文字內容
CSS class 名稱
JavaScript 變數名
JSON 設定 key
註解
檔名
data attribute
localStorage key
```

在 AI 協作開發中，亂碼尤其危險，因為下一個 AI 可能會把亂碼當成有意義的模式延續下去。人類 reviewer 也可能因為看不懂而忽略問題，導致 bug 或設定失效。

### 10.2 語義命名是協作介面

命名不是小事。命名是人類與 AI 共同理解系統的入口。

例如：

```text
bad:
x1
tmpPanel
newBox
abcSetting
thingVisible

good:
hideRecommendations
focusModeEnabled
contentDensity
uiRegionRegistry
paymentSummaryVisible
```

好的命名讓下一個人類與 AI 能快速理解意圖。壞的命名則會累積語義債。

### 10.3 UI-SCL 的命名規則

UI-SCL 應要求設定命名具備一致性：

```text
theme.mode
layout.density
layout.sidebar
content.hideRecommendations
content.focusMode
accessibility.fontScale
accessibility.reduceMotion
notifications.frequency
privacy.analyticsConsent
```

命名應避免：

```text
無意義縮寫
混合語言亂碼
拼音與英文任意混用
看似英文但語義不清
同一概念多種名稱
不可見字元
全形半形混亂
```

### 10.4 可交接性標準

前端程式碼完成不等於可交接。可交接至少應滿足：

```text
1. 新人能理解設定來源。
2. AI 能根據 schema 知道可變項。
3. component 不需要猜測設定含義。
4. UI 區塊是否可隱藏有明確註冊。
5. 不可隱藏資訊有原因說明。
6. 命名一致，沒有亂碼。
7. 設定損壞時有 fallback。
8. 文件能說明如何新增設定項。
```

不可交接的 UI，不應被視為真正完成。

---

## 第十一章：不同規模網頁的 UI-SCL 演化

### 11.1 小型 HTML 頁面

小型頁面可以保持簡單，不必過度工程化。若只有一頁靜態介紹頁，也許只需要：

```text
index.html
style.css
config.js
```

最小 `config.js`：

```javascript
const uiSettings = {
  theme: "system",
  fontScale: 1,
  reduceMotion: false
};
```

小型頁面的原則是：不需要複雜 settings platform，但仍應避免把偏好硬編在多處。

### 11.2 中型內容網站

中型網站可能有文章列表、分類、搜尋、推薦、會員與多頁內容。此時應建立：

```text
settings/
  ui-settings.schema.json
  default-ui-settings.json
  ui-region-registry.json
src/
  settings-provider.js
  persistence-adapter.js
  components/
```

此階段重點是內容可見性、專注模式、匿名偏好保存與基本可及性。

### 11.3 大型 Web App

大型 Web App 需要更完整的 UI-SCL：

```text
settings/
  schema/
  defaults/
  user-profile/
  feature-flags/
  region-registry/
  persistence/
  migration/
  audit/
```

大型系統還需要：

```text
設定版本管理
跨裝置同步
設定遷移
權限控制
團隊責任邊界
UI 設定測試
AI 生成協議
```

### 11.4 超大型平台

超大型平台可能需要獨立的 Settings Platform：

```text
settings-service
schema-registry
preference-sync-service
ui-policy-engine
feature-flag-platform
accessibility-profile-service
consent-management-service
audit-log-service
```

此時 UI-SCL 不再只是前端資料夾，而是跨前端、後端、帳號系統、隱私政策與 AI 代理的基礎設施。

---

## 第十二章：UI-SCL 與產品倫理

### 12.1 從操控介面到尊重介面

許多產品透過暗黑模式設計、預設勾選、彈窗壓迫、無限滾動與難以關閉的推薦來最大化商業指標。這些設計也許能提高短期轉換率，但會削弱使用者信任。

UI-SCL 提倡尊重介面。尊重介面不是放棄商業，而是承認使用者不是被動流量，而是具有偏好、界限與注意力主權的人。

### 12.2 賣方利益與使用者利益的衝突

賣方可能希望使用者多看推薦、多點廣告、多接受促銷、多開通知。使用者可能希望少被打擾、更快找到核心內容、更容易關閉噪音。

UI-SCL 不能天真地假裝衝突不存在。它應把衝突公開化，並在契約層決定：

```text
哪些內容是平台想推，但使用者可關閉？
哪些內容是交易必要，使用者不可關閉？
哪些內容可以降低頻率？
哪些內容需要明確同意？
哪些內容不可偽裝成必要資訊？
```

### 12.3 使用者控制權也是競爭優勢

長期看，提供可控 UI 可能成為產品差異化優勢。當越來越多網站充滿干擾，能讓使用者真正控制介面的產品會更容易建立信任。

尤其在 AI 工具、知識工具、閱讀工具、開發工具、研究工具與專業工作台中，可控 UI 幾乎是必要條件。專業使用者不只需要功能，也需要能配置自己的工作環境。

---

## 第十三章：UI-SCL 實作模板

### 13.1 基礎資料夾結構

```text
project/
  index.html
  src/
    app.js
    settings/
      ui-settings.schema.json
      default-ui-settings.json
      ui-region-registry.json
      settings-provider.js
      persistence-adapter.js
    components/
      Header.js
      Sidebar.js
      ArticleList.js
      RecommendationPanel.js
  styles/
    base.css
    theme.css
    layout.css
    accessibility.css
  docs/
    UI-SCL.md
```

### 13.2 預設設定範例

```json
{
  "theme": {
    "mode": "system",
    "accentColor": "default"
  },
  "layout": {
    "density": "comfortable",
    "sidebar": "auto",
    "contentWidth": "normal"
  },
  "content": {
    "focusMode": false,
    "hideRecommendations": false,
    "hideTrending": false
  },
  "accessibility": {
    "fontScale": 1,
    "reduceMotion": false,
    "highContrast": false
  },
  "notifications": {
    "frequency": "normal",
    "marketing": false,
    "security": true
  }
}
```

### 13.3 HTML 範例

```html
<body data-theme="system" data-density="comfortable" data-focus-mode="false">
  <header data-ui-region="header" data-user-hideable="false">
    ...
  </header>

  <main data-ui-region="main-content" data-user-hideable="false">
    ...
  </main>

  <aside data-ui-region="recommendations" data-user-hideable="true">
    ...
  </aside>

  <section data-ui-region="security-warning" data-user-hideable="false">
    ...
  </section>
</body>
```

### 13.4 Settings Provider 範例

```javascript
const DEFAULT_SETTINGS = {
  theme: { mode: "system", accentColor: "default" },
  layout: { density: "comfortable", sidebar: "auto" },
  content: { focusMode: false, hideRecommendations: false },
  accessibility: { fontScale: 1, reduceMotion: false }
};

const STORAGE_KEY = "ui-scl-settings-v1";

export function loadSettings() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return DEFAULT_SETTINGS;
    const userSettings = JSON.parse(raw);
    return mergeSettings(DEFAULT_SETTINGS, userSettings);
  } catch {
    return DEFAULT_SETTINGS;
  }
}

export function saveSettings(settings) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(settings));
}

export function applySettings(settings) {
  document.body.dataset.theme = settings.theme.mode;
  document.body.dataset.density = settings.layout.density;
  document.body.dataset.focusMode = String(settings.content.focusMode);
  document.documentElement.style.setProperty(
    "--font-scale",
    settings.accessibility.fontScale
  );
}

function mergeSettings(defaults, userSettings) {
  return {
    ...defaults,
    ...userSettings,
    theme: { ...defaults.theme, ...userSettings.theme },
    layout: { ...defaults.layout, ...userSettings.layout },
    content: { ...defaults.content, ...userSettings.content },
    accessibility: { ...defaults.accessibility, ...userSettings.accessibility }
  };
}
```

---

## 第十四章：反模式與風險

### 14.1 設定散落

設定散落是最常見問題。每個 component 自己保存偏好，會造成命名不一致、狀態不同步、同步困難與 AI 難以理解。

### 14.2 過度設定

不是所有東西都要開放設定。過度設定會造成使用者負擔。UI-SCL 應避免把產品責任推給使用者。好的設定層應提供少量高價值控制點，而不是讓使用者面對幾百個開關。

### 14.3 偽使用者控制

有些產品表面上提供設定，實際上只是象徵性開關。例如使用者關閉推薦後，系統仍以其他形式插入推薦；使用者關閉通知後，平台仍透過彈窗提醒。這會破壞信任。

### 14.4 安全資訊被錯誤隱藏

若安全警告、付款金額、錯誤訊息被納入一般可隱藏區塊，將造成嚴重風險。因此 UI-SCL 必須有不可隱藏白名單。

### 14.5 AI 生成設定債

當 AI 快速生成大量 UI 而缺乏設定契約，會形成難以追蹤的前端設定債。這種債比一般 CSS 混亂更麻煩，因為它牽涉使用者偏好、持久化、介面倫理與產品行為。

---

## 第十五章：UI-SCL 與未來意圖語言

### 15.1 意圖語言需要可控介面

未來若人類能直接用自然語言命令 AI 修改介面，例如：

```text
把這個網站改成專注閱讀模式。
隱藏所有推薦與社群元素。
幫我把工具欄改成左側。
只保留研究相關內容。
把動畫全部關掉。
```

那麼 AI 必須知道哪些 UI 區塊可控制、如何控制、控制後是否違反安全或必要資訊邊界。這正是 UI-SCL 的作用。

沒有 UI-SCL，AI 只能猜。  
有 UI-SCL，AI 可以依契約執行。

### 15.2 言出法隨之前，需要設定契約

真正的「言出法隨」不是一句話讓系統神奇改變，而是系統已經具備清楚的可變結構。人類說出意圖，AI 根據設定契約、架構邊界與安全規則轉換為可靠操作。

因此，UI-SCL 是意圖語言前端化的基礎之一。

### 15.3 從頁面到個人化工作環境

未來的前端 UI 會越來越不像固定頁面，而像個人化工作環境。使用者不只是瀏覽網站，而是在配置自己的資訊空間。AI 則成為協助使用者重新排列、篩選、降噪與擴展介面的代理。

在這個時代，UI-SCL 不只是工程文件，而是人類與 AI 共同操作介面的語法前提。

---

## 第十六章：結論

本文提出 UI-SCL 作為 HTML / Web 前端系統中的設定契約層方法論。其核心命題是：前端 UI 不應只是賣方展示與平台引導的介面，而應是使用者在安全邊界內可調整、可保存、可聚焦、可降噪的注意力環境。

UI-SCL 要求前端開發在功能實作前先定義設定層，明確聲明使用者能控制什麼、不能控制什麼；哪些偏好可匿名保存，哪些需要會員同步；哪些內容可隱藏，哪些資訊不可關閉；AI 生成前端時必須遵守哪些設定協議。

在 AI 編碼與 Vibe Coding 時代，UI-SCL 的重要性更高。因為 AI 能快速生成 UI，也能快速生成混亂。若缺乏設定契約，偏好、顯示、控制與持久化邏輯會散落在元件中，造成後續人類與 AI 都難以維護。反之，若先建立 UI-SCL，AI 就能在明確結構中生成可控、可讀、可交接的前端。

本文最後主張：

> 未來的好 UI，不是讓使用者被動接受設計，而是讓使用者在安全與必要資訊邊界內，重新配置自己的注意力環境。

HTML 定義頁面有什麼。  
UI-SCL 定義使用者能如何重組這個頁面。  
AI 可以生成介面，但使用者主權與設定契約必須先被聲明。

---

## 附錄 A：UI-SCL 檢查清單

```text
[ ] 是否有 ui-settings.schema.json？
[ ] 是否有 default-ui-settings.json？
[ ] 是否有 UI Region Registry？
[ ] 是否明確區分可隱藏與不可隱藏內容？
[ ] 是否支援匿名偏好保存？
[ ] 是否定義會員偏好同步策略？
[ ] 是否有 Settings Provider？
[ ] 是否禁止 component 直接硬編碼偏好？
[ ] 是否集中管理 localStorage key？
[ ] 是否支援 focusMode？
[ ] 是否支援基本可及性設定？
[ ] 是否有設定 fallback？
[ ] 是否定義 AI 生成前端協議？
[ ] 是否禁止亂碼、不可見字元與無意義命名？
```

---

## 附錄 B：UI-SCL 最小可行模板

```text
settings/
  default-ui-settings.json
  ui-settings.schema.json
  ui-region-registry.json
  settings-provider.js
docs/
  UI-SCL.md
```

---

## 附錄 C：核心命題

```text
HTML 定義頁面有什麼；UI-SCL 定義使用者能如何重組這個頁面。

UI 不應只是賣方展示資訊的介面，而應是使用者配置注意力的環境。

設定不是功能完成後的附屬選單，而是前端可控性的先行契約。

在 AI 編碼時代，沒有 UI-SCL 的前端生成會迅速累積設定債。

不可讀、不可控、不可交接的 UI，不應被視為真正完成。

使用者主權不是任意關閉一切，而是在安全與必要資訊邊界內最大化介面控制權。
```

---

## 附錄 D：與既有方法論的關係

UI-SCL 可被視為以下方法論的前端延伸：

```text
三層認知架構：
  UI-SCL 位於宏觀決策與中觀架構之間，回答使用者可控制什麼。

MSSP：
  UI-SCL 可作為 FMS 與前端 SMS/TMS 之間的可變性契約。

規模感知架構：
  UI-SCL 會隨網頁規模從 config.js 演化為 settings platform。

SCL：
  UI-SCL 是設定契約層在前端 UI 領域的具體分支。

ICL：
  UI-SCL 是 AI 與人類協作生成 UI 時的前端協議基礎。
```

---

## 附錄 E：給 AI 的簡短指令

```text
請依 UI-SCL 架構生成前端。
所有 UI 偏好集中於 settings 層。
不得硬編碼使用者偏好。
所有可隱藏區塊需註冊。
所有不可隱藏資訊需標示原因。
支援匿名偏好保存與未來會員同步。
輸出不得包含亂碼、無意義命名或不可見字元。
```
