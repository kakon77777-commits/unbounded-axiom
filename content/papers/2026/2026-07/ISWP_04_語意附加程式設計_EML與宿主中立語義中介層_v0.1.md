---
title: "語意附加程式設計：EML 與宿主中立語義中介層"
english_title: "Semantic-Overlay Programming: EML and the Host-Neutral Semantic Intermediate Layer"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "04/12"
part: "第二部：後文本語言與結構表示"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-25"
language: "zh-TW"
document_type: "理論論文／語言架構論"
status: "初版完成"
---

# 語意附加程式設計：EML 與宿主中立語義中介層

## Semantic-Overlay Programming: EML and the Host-Neutral Semantic Intermediate Layer

**系列：**《意圖—結構—世界程式論》第四篇  
**部別：**第二部「後文本語言與結構表示」  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 25 日  

---

## 摘要

現代程式系統的語意經常分散於程式碼、型別、註解、設定檔、資料庫綱要、測試、權限政策、工作流、文件與組織慣例之中。這些語意未必屬於單一程式語言，也不必然能由宿主語法完整表達。當 AI Agent 開始跨檔案、跨語言、跨工具與跨媒介工作時，僅依賴單一語法樹或文字檔案作為語意權威，會產生語意碎裂、宿主綁定、投影失真、權限不透明與狀態不可追蹤等問題。

本文提出「語意附加程式設計」：在不破壞既有宿主物件的前提下，將可識別、可版本化、可驗證的結構化語意附著於程式節點、資料欄位、自然語言片段、工作流節點、專案、媒體區段或其他可定位物件，再透過宿主中立語義中介表示，投影為不同語言、介面、執行環境與人類可見形式。

本文以 EML 為主要架構實例，將其正式界定為通用語意附加協議，而非 Python 縮寫、Unicode 符號表、單一新語言、視覺化標註工具或由大型語言模型即時猜測語意的非確定性編譯器。EML 的核心可表示為：

$$
\mathbb E
=
\left\langle
\mathcal H,
\mathcal A,
\mathcal O,
\mathcal R,
\mathcal P,
\mathcal D,
\mathcal V,
\mathcal X,
\mathcal T
\right\rangle
$$

其中依序代表宿主物件、錨點、語意附加、語意註冊表、政策、適配器、驗證器、投影／執行介面與追蹤系統。本文定義附加、解析、合併、驗證、投影、執行、觀測與撤銷等核心操作，並區分宿主身分、語意身分與表面身分，避免把符號外觀誤認為語意本體。

本文提出：宿主中立不等於所有後端語意完全相同，而是語意核心不得由任一宿主的模板或語法所定義。每一個投影都必須明確標記為完整保持、部分保持、近似、拒絕或需要人工決策；未支援語意不得靜默降級。AI 可以提出 overlay 候選、錨點修復與跨宿主映射，但確定性核心、政策閘門、驗證器與批准機制必須獨立存在。

本文亦整理 EML-P 與 EML-U 的雙 Profile 架構：EML-P 是低歧義、線性、可測試、可執行的穩定子集；EML-U 保存通用語意附加、二維與非線性投影、高密度符號、跨媒介與 AI 原生能力。兩者應透過顯式降級、能力狀態與語意損失報告連接，而不能由工程 MVP 取代原始理論，也不能以未實作願景冒充現行能力。

本文最後提出可證偽研究綱領，包括錨點漂移修復率、跨宿主語意保持率、投影損失、政策衝突偵測、round-trip 不動點、AI 理解增益、人類可見性與大型專案中的語意維護成本。本文的核心結論是：後文本程式設計不要求拋棄文字，而要求將語意身分從單一文字表面中解耦，使同一語意能在多宿主、多投影與多主體之間被保存、驗證與治理。

**關鍵詞：** EML、語意附加、宿主中立、語義中介表示、Semantic Overlay、Anchor、Adapter、多宿主投影、後文本程式設計、AI Agent、語意治理

---

## Abstract

The semantics of modern software systems are distributed across source code, types, comments, configuration files, database schemas, tests, permission policies, workflows, documentation, and organizational conventions. These semantics do not necessarily belong to a single programming language and may not be fully expressible by a host syntax. As AI agents begin to operate across files, languages, tools, and media, treating one syntax tree or one textual artifact as the sole semantic authority leads to fragmentation, host lock-in, projection loss, opaque permissions, and untraceable state changes.

This paper proposes semantic-overlay programming: structured, identifiable, versioned, and verifiable semantics are attached to existing host objects without destroying their original representations. These overlays may target program nodes, data fields, natural-language fragments, workflow nodes, projects, media segments, or other addressable entities. A host-neutral semantic intermediate representation then projects the overlays into multiple languages, interfaces, runtimes, and human-visible forms.

EML is developed as the primary architectural instance. It is formally defined as a universal semantic-overlay protocol rather than a Python shorthand, a Unicode symbol table, a single replacement language, a visual annotation tool, or a nondeterministic compiler whose semantics are guessed by a language model. The paper defines attachment, resolution, merge, validation, projection, execution, observation, and revocation operations, while distinguishing host identity, semantic identity, and surface identity.

Host neutrality does not mean that all backends have identical expressive power. It means that no host-specific template or syntax may define the semantic core. Every projection must explicitly report whether semantics are preserved, partially preserved, approximated, rejected, or require human decision. Unsupported semantics must fail loudly rather than degrade silently.

The paper also formalizes the EML-P and EML-U dual-profile architecture. EML-P is a stable, linear, low-ambiguity, executable subset; EML-U preserves universal semantic overlays, multidimensional and nonlinear projections, high-density symbols, cross-media semantics, and AI-native capabilities.

**Keywords:** EML, semantic overlay, host neutrality, semantic intermediate representation, anchors, adapters, multi-host projection, post-textual programming, AI agents

---

# 一、問題的提出：程式的語意究竟存在哪裡？

傳統編譯模型通常假設程式的主要語意存在於來源文字及其抽象語法樹中：

$$
\text{Source}
\rightarrow
\text{AST}
\rightarrow
\text{IR}
\rightarrow
\text{Executable}
$$

這個模型對單一語言、單一工具鏈與封閉執行環境非常有效。然而，真實軟體系統中的關鍵語意往往同時存在於：

- 函式與類別；
- 型別註記；
- 註解與文件；
- 測試；
- 資料庫綱要；
- API 契約；
- 權限政策；
- 工作流；
- 部署設定；
- 觀測與追蹤規則；
- 組織慣例；
- 使用者意圖；
- 尚未寫入程式碼的限制。

例如，一個函式是否可以快取，未必只由函式體判斷。它還可能依賴純度、外部狀態、時間、隱私、資料新鮮度、權限與失效條件。若這些語意只存在於文件或人的記憶中，編譯器與 Agent 無法可靠使用；若全部硬塞入單一宿主語法，則會使語言膨脹、宿主綁定並破壞既有工具。

因此需要第三種方式：

> **保留既有宿主，另建立可定位、可結構化、可驗證的語意附加層。**

基本形式為：

$$
h+o
\rightarrow
h^{\langle o\rangle}
$$

其中：

- $h$ ：宿主物件；
- $o$ ：語意附加；
- $h^{\langle o\rangle}$ ：仍保留原始宿主身分、但具備附加語意的複合物件。

這就是本文所稱的語意附加程式設計。

---

# 二、EML 的理論重新定位

## 2.1 正式定義

本文將 EML 定義為：

> **EML（Efficient New Language／Efficient Meta-Language）是一套通用語意附加協議。它允許結構化語意附著於任意可定位宿主物件，形成宿主中立的語意圖與語意中介表示，再透過確定性適配器進行投影、轉譯、驗證、執行與觀測。**

這個定義包含四個不可刪除的要件：

1. 有既存或新建的宿主物件；
2. 有可穩定定位宿主局部的錨點；
3. 有宿主中立的語意身分；
4. 有可驗證的投影與執行鏈。

## 2.2 EML 不是 Python 的縮寫

Python 可以是第一個參考宿主，但不能成為 EML 本體邊界。

錯誤模型：

$$
\mathrm{EML}
\equiv
\mathrm{Python\ Shorthand}
$$

合理模型：

$$
\mathrm{EML\ Core}
\rightarrow
\left\{
\begin{array}{l}
\mathrm{Python\ Adapter}\\
\mathrm{C++\ Adapter}\\
\mathrm{JavaScript\ Adapter}\\
\mathrm{SQL\ Adapter}\\
\mathrm{Workflow\ Adapter}\\
\mathrm{Natural\ Language\ Adapter}
\end{array}
\right.
$$

宿主適配器可以不完整，但不能反過來定義語意核心。

## 2.3 EML 不是符號面板

符號面板只負責搜尋與插入表面符號：

$$
\text{Palette}
:
\text{Query}
\rightarrow
\text{Surface Form}
$$

完整語意附加系統則必須處理：

$$
\text{Host Selection}
\rightarrow
\text{Anchor}
\rightarrow
\text{Semantic Node}
\rightarrow
\text{Scope}
\rightarrow
\text{Policy}
\rightarrow
\text{Projection}
\rightarrow
\text{Validation}
$$

因此「右上角」可以是視覺投影位置，但不是底層資料結構。

## 2.4 EML 不是純 metadata

一般 metadata 可能只是任意鍵值對，沒有統一語意、作用域、衝突規則、投影義務或驗證器。

EML overlay 至少需要：

- 語意識別碼；
- 適用宿主類型；
- 作用域；
- 型別與參數；
- 前置條件；
- 效果；
- 政策；
- 驗證器；
- 投影狀態；
- 來源與版本。

因此：

$$
\boxed{
\text{Overlay}
\supsetneq
\text{Unstructured Metadata}
}
$$

## 2.5 EML 不是 LLM 猜測層

大型語言模型可以提出 overlay 候選、將自然語言轉為結構候選、修復錨點、解釋投影損失與建議跨宿主映射。但模型輸出只是：

$$
o_{\mathrm{candidate}}
$$

正式接受仍需：

$$
\operatorname{Validate}
\left(
o_{\mathrm{candidate}}
\right)
\land
\operatorname{PolicyAllow}
\left(
o_{\mathrm{candidate}}
\right)
$$

EML 的確定性核心不得被模型的即時猜測悄悄改變。

---

# 三、語意附加系統的九元模型

本文定義 EML 系統：

$$
\boxed{
\mathbb E
=
\left\langle
\mathcal H,
\mathcal A,
\mathcal O,
\mathcal R,
\mathcal P,
\mathcal D,
\mathcal V,
\mathcal X,
\mathcal T
\right\rangle
}
$$

其中：

- $\mathcal H$ ：宿主物件空間；
- $\mathcal A$ ：錨點空間；
- $\mathcal O$ ：overlay 空間；
- $\mathcal R$ ：語意註冊表；
- $\mathcal P$ ：政策與權限系統；
- $\mathcal D$ ：宿主適配器集合；
- $\mathcal V$ ：驗證器集合；
- $\mathcal X$ ：投影與執行介面；
- $\mathcal T$ ：來源、版本與執行追蹤。

## 3.1 宿主物件

宿主物件：

$$
h\in\mathcal H
$$

可以是文字、AST 節點、程式模組、資料欄位、資料表、API、工作流節點、自然語言段落、圖形物件、音訊區段、影片時間片、專案、Agent 任務或世界狀態節點。

EML 不要求所有宿主具有相同結構，只要求適配器能提供可定位界面。

## 3.2 錨點

錨點將 overlay 綁定到宿主的全部或局部：

$$
a
=
\operatorname{Anchor}
\left(
h,
\ell,
s,
v
\right)
$$

其中：

- $\ell$ ：定位描述；
- $s$ ：作用域；
- $v$ ：宿主版本或快照。

錨點不是單純字元位置。它可以組合結構路徑、節點識別碼、內容雜湊、前後文指紋、語義定位器、時間區間、幾何區域與關係選擇器。

## 3.3 語意附加

定義 overlay：

$$
o
=
\left\langle
\operatorname{id},
a,
\sigma,
\theta,
c,
e,
q,
v,
\gamma
\right\rangle
$$

其中：

- $\operatorname{id}$ ：overlay 實例識別碼；
- $a$ ：錨點；
- $\sigma$ ：semantic ID；
- $\theta$ ：參數；
- $c$ ：限制與契約；
- $e$ ：效果；
- $q$ ：政策與權限；
- $v$ ：驗證規則；
- $\gamma$ ：來源、版本與有效期。

## 3.4 語意註冊表

註冊表不只保存符號外觀，而保存語意型別：

$$
\mathcal R
:
\sigma
\mapsto
\left\langle
\text{schema},
\text{domain},
\text{effects},
\text{validators},
\text{projection contracts}
\right\rangle
$$

一個 semantic ID 可以有多個表面形式：

$$
\operatorname{SurfaceForms}(\sigma)
=
\{s_1,s_2,\ldots,s_n\}
$$

同一符號外觀也可能因作用域不同而指向不同語意，但必須顯式解析，不得以宿主模板暗示。

## 3.5 政策

政策層決定誰能建立 overlay、誰能修改、哪些 overlay 可執行、哪些只能作說明、哪些需要批准、哪些不得跨宿主投影，以及哪些具有法律或安全優先級。

## 3.6 適配器

宿主適配器：

$$
D_j
:
\mathcal H_j
\leftrightarrow
\mathcal R_{\mathrm{semantic}}
$$

負責讀取宿主、定位節點、產生宿主投影、回報不支援能力，以及追蹤版本與差分。

## 3.7 驗證器

驗證器可以檢查 schema、型別、作用域、前後條件、純度、權限、投影保持、round-trip 與執行狀態。

## 3.8 投影與執行介面

投影：

$$
\pi_j
:
\mathcal O
\rightarrow
\mathcal Y_j
$$

其中 $\mathcal Y_j$ 可以是 Python、C++、JavaScript、SQL、文件、圖形、UI、工作流、人類說明、Agent API 或執行事件。

## 3.9 追蹤

追蹤系統保存：

$$
\operatorname{Trace}
\left(
o,
D_j,
\pi_j,
V,
\Delta W
\right)
$$

使人類與 Agent 能回答：哪個 overlay 經哪個適配器，產生何種投影，通過哪些驗證，並改變哪些狀態。

---

# 四、三種身分：宿主、語意與表面

語意附加系統若沒有分離身分，容易把字串、位置或後端模板誤當成本體。

## 4.1 宿主身分

宿主身分：

$$
\operatorname{HID}(h)
$$

描述被附加的物件本身，例如某函式、欄位、工作流節點、文字段落或影片時間片。

## 4.2 語意身分

語意身分：

$$
\operatorname{SID}(\sigma)
$$

描述 overlay 所表達的結構化語意，例如：

```text
eml.algebra.aggregate.sum
eml.execution.purity.cold
eml.policy.requires_approval
eml.time.wait_until
```

語意身分應獨立於 Python、C++ 或符號字形。

## 4.3 表面身分

表面身分：

$$
\operatorname{SurfaceID}(s)
$$

描述某個投影中的字形、關鍵字、UI 圖示或節點外觀。

同一語意可能投影為：

$$
\{
\Sigma,
\operatorname{SUM},
\texttt{sum},
\text{加總},
\text{圖形節點}
\}
$$

因此：

$$
\boxed{
\operatorname{HID}
\neq
\operatorname{SID}
\neq
\operatorname{SurfaceID}
}
$$

這個區分是宿主中立架構的基礎。

---

# 五、錨點模型：語意如何附著而不漂移？

## 5.1 位置錨點的不足

若 overlay 只綁定字元範圍：

$$
a=(i,j)
$$

當宿主前方插入內容，位置便可能錯位。

## 5.2 複合錨點

本文建議：

$$
a
=
\left\langle
\operatorname{host\_id},
\operatorname{structural\_path},
\operatorname{content\_hash},
\operatorname{context\_fingerprint},
\operatorname{semantic\_locator},
\operatorname{version}
\right\rangle
$$

不同宿主可採不同組合。

程式碼可以使用 AST path、symbol ID、source range、signature hash 與 surrounding tokens；自然語言可以使用 document ID、paragraph path、text span、鄰句雜湊與實體關係；音訊與影片可以使用 media ID、time range、track 與 perceptual fingerprint；工作流則可以使用 graph ID、node ID 與邊關係簽章。

## 5.3 錨點解析

宿主更新後，解析器尋找：

$$
a'
=
\operatorname{Resolve}
\left(
a,
h^{(v+1)}
\right)
$$

並給出信心：

$$
\kappa(a')\in[0,1]
$$

當：

$$
\kappa(a')<\tau
$$

不得自動移動 overlay，應標記為：

```text
orphaned
ambiguous
manual-review-required
```

## 5.4 AI 錨點修復

AI 可以提出：

$$
\{a'_1,a'_2,\ldots,a'_k\}
$$

但正式重綁仍應由結構匹配、雜湊、版本規則、測試與人類批准共同決定。

---

# 六、Overlay 的作用域與生命週期

## 6.1 作用域

overlay 可作用於：

$$
\operatorname{Scope}(o)
\in
\{
\text{node},
\text{block},
\text{file},
\text{module},
\text{project},
\text{runtime},
\text{organization},
\text{world}
\}
$$

局部 overlay 不應無條件擴張為全域規則。

## 6.2 有效期

令有效區間為：

$$
[t_{\mathrm{start}},t_{\mathrm{end}})
$$

也可以由事件終止：

$$
\operatorname{ValidUntil}(o)=\text{event}
$$

例如直到部署完成、人工撤回、資料版本更新或下次審核。

## 6.3 狀態

overlay 應有明確狀態：

```text
candidate
draft
validated
approved
active
suspended
deprecated
revoked
orphaned
unsupported
```

只有：

$$
\operatorname{status}(o)=\text{active}
$$

且通過政策，才可影響執行。

## 6.4 撤銷

撤銷不是刪除歷史，而是：

$$
o_{\mathrm{active}}
\rightarrow
o_{\mathrm{revoked}}
$$

並保存撤銷主體、原因、時間、影響範圍，以及是否需要回復已產生的狀態。

---

# 七、核心操作代數

本文定義八個核心操作。

## 7.1 附加

$$
\operatorname{Attach}
:
(h,a,\sigma,\theta)
\mapsto
o
$$

建立 overlay 候選。

## 7.2 解析

$$
\operatorname{Resolve}
:
(o,h^{(v)})
\mapsto
a'
$$

在當前宿主版本中定位 overlay。

## 7.3 合併

$$
\operatorname{Merge}
:
(o_1,o_2,\ldots,o_n)
\mapsto
O^\ast
$$

形成當前有效語意集合。

## 7.4 驗證

$$
\operatorname{Validate}
:
(O^\ast,\mathcal R,\mathcal P)
\mapsto
\{\text{pass},\text{fail},\text{review}\}
$$

## 7.5 投影

$$
\operatorname{Project}_{D_j}
:
O^\ast
\mapsto
y_j
$$

## 7.6 執行

$$
\operatorname{Execute}
:
(y_j,W_t)
\mapsto
\Delta W_t
$$

## 7.7 觀測

$$
\operatorname{Observe}
:
(o,y_j,\Delta W_t)
\mapsto
\tau
$$

其中 $\tau$ 是執行軌跡。

## 7.8 撤銷

$$
\operatorname{Revoke}
:
(o,\text{authority})
\mapsto
o'
$$

並觸發必要的回復或重新投影。

---

# 八、Overlay 衝突與優先序

多重語意附加可能互相衝突。例如，專案層標記某函式可快取，但安全政策標記該函式處理敏感即時資料，不得快取。

## 8.1 衝突類型

- 值衝突：同一語意欄位具有不同值；
- 效果衝突：一個 overlay 要求寫入，另一個禁止寫入；
- 權限衝突：執行語意與主體權限不一致；
- 時間衝突：舊規則與新規則同時有效；
- 作用域衝突：局部例外與全域政策交錯；
- 投影衝突：不同 overlay 在目標宿主中需要互斥實作。

## 8.2 優先序不能只靠最後寫入

合理決策應考慮：

$$
\operatorname{Priority}(o)
=
F
\left(
\text{authority},
\text{policy level},
\text{specificity},
\text{time},
\text{explicit override},
\text{risk}
\right)
$$

較新的低權限 overlay 不得取代高權限安全政策。

## 8.3 衝突結果

合併結果可以是：

```text
resolved
blocked
requires-approval
multiple-projections
unsupported
```

高風險衝突不得由 AI 以「最可能」方式靜默決定。

---

# 九、宿主中立語義中介表示

## 9.1 宿主中立的定義

宿主中立不是：

> 所有宿主都能完整表達所有語意。

而是：

> 語意核心的定義不得依賴任一宿主的表面模板。

錯誤註冊：

```json
{
  "symbol": "Σ",
  "python": "sum({expr} for {iter} in {range})"
}
```

改良方向：

```json
{
  "semantic_id": "eml.algebra.aggregate.sum",
  "schema": {
    "operation": "aggregate",
    "algebra": "additive_monoid",
    "binding": "iterator",
    "range": "declared"
  },
  "effects": [],
  "projection_contracts": {
    "python": "supported",
    "cpp": "supported",
    "javascript": "supported"
  }
}
```

## 9.2 Semantic IR 節點

定義語意節點：

$$
n
=
\left\langle
\sigma,
\theta,
\operatorname{type},
\operatorname{effects},
\operatorname{constraints},
\operatorname{links}
\right\rangle
$$

語意圖：

$$
G_S=(V_S,E_S)
$$

其中邊可表示依賴、作用於、覆蓋、例外、時序、因果、權限、驗證與投影來源。

## 9.3 核心不應保存後端真相

後端模板應位於 adapter：

$$
D_j(\sigma,\theta)
\mapsto
y_j
$$

而不是：

$$
\sigma
\equiv
y_j
$$

這使語意核心可以跨宿主存活。

---

# 十、投影契約與語意損失

## 10.1 五種投影狀態

每個目標宿主都必須回報：

```text
preserved
partially-preserved
approximated
unsupported
human-decision-required
```

## 10.2 語意保持

令來源語意為：

$$
S(o)
$$

目標投影語意為：

$$
S(\pi_j(o))
$$

完全保持要求：

$$
S(\pi_j(o))
\equiv_{\mathcal T}
S(o)
$$

## 10.3 投影損失

定義：

$$
L_{\pi_j}
=
d_{\mathcal T}
\left(
S(o),
S(\pi_j(o))
\right)
$$

系統必須報告被保留內容、被近似內容、被丟失內容、新增後端假設與是否可回復。

## 10.4 靜默降級禁止

若語意要求 `non-blocking temporal wait`，而目標後端只能產生忙等，則不能直接宣稱已投影成功。

應回報：

```yaml
status: approximated
lost:
  - non_blocking
introduced:
  - active_cpu_wait
approval_required: true
```

## 10.5 Round-trip

對可逆子集：

$$
o
\xrightarrow{\pi_j}
y_j
\xrightarrow{\rho_j}
\hat o
$$

期待：

$$
\hat o
\equiv_{\mathcal T}
o
$$

但不是所有投影都可逆。不可逆性必須成為能力標籤，而不是隱藏缺陷。

---

# 十一、確定性核心與 AI 協作邊界

## 11.1 確定性核心鏈

EML-P 的最小閉環：

```text
source
→ normalize
→ lex
→ parse
→ AST
→ semantic analysis
→ host-neutral IR
→ adapter
→ emit
→ validate
→ execute
→ trace
→ round-trip
```

對相同輸入、版本與工具鏈：

$$
F(x,v)=y
$$

應可重現。

## 11.2 AI 的候選角色

AI 可以執行：

$$
\operatorname{SuggestOverlay}
$$

$$
\operatorname{SuggestAnchorRepair}
$$

$$
\operatorname{SuggestProjection}
$$

$$
\operatorname{ExplainLoss}
$$

$$
\operatorname{GenerateTests}
$$

## 11.3 AI 不得取得的默認權力

AI 不得自行宣告 conceptual 能力已實作、建立未登錄語法、靜默選擇高風險語意、擴張權限、隱藏 unsupported、把測試建議當成測試通過、修改高層政策，或以自然語言說明取代執行證書。

## 11.4 接受條件

候選 overlay 的接受條件：

$$
\operatorname{Accept}(o)
=
V_{\mathrm{schema}}
\land
V_{\mathrm{anchor}}
\land
V_{\mathrm{policy}}
\land
V_{\mathrm{projection}}
\land
V_{\mathrm{authority}}
$$

---

# 十二、EML-P 與 EML-U 雙 Profile 架構

## 12.1 EML-P

EML-P 是線性文字、低歧義、可 Git diff、可解析、可轉譯、可測試、可執行、可除錯，且具有明確 round-trip 邊界的穩定 Profile。

$$
\mathrm{EML\text{-}P}
=
\text{Stable Executable Profile}
$$

## 12.2 EML-U

EML-U 保存通用語意附加、多位置附加、二維與非線性結構、高密度符號、跨宿主、跨媒介、AI 自適應投影、意圖級壓縮與多閱讀者視圖。

$$
\mathrm{EML\text{-}U}
=
\text{Universal Semantic Profile}
$$

## 12.3 關係

$$
\boxed{
\mathrm{EML\text{-}P}
\subseteq
\mathrm{EML\text{-}U}
}
$$

EML-P 的正式語意都應能被 EML-U 理解；EML-U 的全部語意不保證能立即降級到 EML-P。

## 12.4 降級

降級映射：

$$
\lambda
:
\mathrm{EML\text{-}U}
\rightarrow
\mathrm{EML\text{-}P}
\cup
\{\text{metadata},\text{unsupported},\text{review}\}
$$

不得將無法表達的語意直接刪除。

## 12.5 能力狀態

每個能力必須標記：

```text
implemented
partial
conceptual
planned
deprecated
```

這防止理論、規格、工程與產品 UI 互相冒充。

---

# 十三、EML 與傳統技術的區別

## 13.1 與註解

註解通常不參與執行語意；overlay 可以被驗證、投影與政策控制。

## 13.2 與 annotation／attribute

語言內 annotation 通常綁定單一宿主文法。EML 可以使用 annotation 作表面投影，但語意身分位於宿主中立註冊表。

## 13.3 與巨集

巨集主要執行語法展開；overlay 可以只表達限制、權限、時間或觀測，不必直接產生程式碼。

## 13.4 與 DSL

DSL 通常建立一個領域語法；EML 可以承載多個領域語意包，並附著於既有宿主，不必要求所有物件重寫成 DSL。

## 13.5 與 AST 擴充

AST 擴充通常屬於單一語言工具鏈；EML 需要跨 AST、資料、工作流與非程式媒介。

## 13.6 與 knowledge graph

知識圖主要描述實體與關係；EML 還需要錨點、執行、投影、驗證、政策、版本與回復。

## 13.7 與一般 metadata

metadata 不必有語意契約；EML overlay 必須能被解析與治理。

---

# 十四、跨宿主案例

## 14.1 程式碼純度

對 Python 函式附加：

```yaml
semantic_id: eml.execution.purity.cold
constraints:
  external_writes: false
  time_dependency: false
```

Python Adapter 可投影為 decorator 或分析規則；C++ Adapter 可投影為 attribute、靜態分析設定或文件契約。語意核心不等於任何一種語法。

## 14.2 資料欄位隱私

對資料欄位附加：

```yaml
semantic_id: eml.data.privacy.sensitive
policy:
  external_transfer: prohibited
  retention_days: 30
```

可投影至資料庫政策、API 過濾器、日誌遮罩、Agent 工具權限與人類 UI 警告。

## 14.3 自然語言限制

對需求句：

> 每次公開發布前必須人工批准。

附加為：

```yaml
semantic_id: eml.policy.requires_approval
scope: project
event: public_release
authority: human_owner
```

其後可投影至 CI gate、Agent Runtime 與工作流節點。

## 14.4 工作流時間語意

對工作流節點附加：

```yaml
semantic_id: eml.time.wait_until
condition: invoice_paid
timeout: P7D
```

不同 Runtime 可用事件訂閱、排程或狀態機實現，但不得以忙等冒充完整保持。

## 14.5 媒體區段

對影片時間片附加：

```yaml
semantic_id: eml.media.privacy.blur_face
range: 00:01:22.100-00:01:27.900
```

它可以投影為編輯器標記、渲染任務與審核規則。

---

# 十五、語意包與可組合性

## 15.1 語意包

領域語意可以組成：

$$
\mathcal R_{\mathrm{domain}}
\subseteq
\mathcal R
$$

例如數學、資料治理、時間控制、安全、醫療、遊戲、機器人、工作流與文件出版。

## 15.2 命名空間

semantic ID 應具有穩定命名：

```text
eml.<domain>.<family>.<concept>
```

私人擴充則使用：

```text
org.<organization>.<domain>.<concept>
```

## 15.3 組合

兩個 overlay：

$$
o_1\otimes o_2
$$

只有在 schema 相容、作用域相容、效果不衝突、權限成立且目標 adapter 支援時，才能形成複合語意。

## 15.4 語意爆炸

若註冊表無限制增加符號與概念，會產生重複語意、近義分裂、命名衝突、學習成本、投影負擔與驗證器缺口。

新語意進入核心前應評估：

$$
V(\sigma)
=
G_{\mathrm{semantic}}
+
G_{\mathrm{reuse}}
+
G_{\mathrm{crosshost}}
-
C_{\mathrm{ambiguity}}
-
C_{\mathrm{maintenance}}
-
C_{\mathrm{projection}}
$$

---

# 十六、語意附加治理

## 16.1 語意權限

能建立 overlay 不代表能使其生效。

定義：

$$
A_o(s,\sigma,h)
$$

表示主體 $s$ 是否有權對宿主 $h$ 建立語意 $\sigma$ 。

另定義：

$$
A_x(s,o)
$$

表示主體是否有權批准 overlay 進入執行。

## 16.2 語意供應鏈

一個 overlay 可能經過：

```text
提出者
→ 解析器
→ 註冊表
→ 政策引擎
→ 適配器
→ 驗證器
→ Runtime
```

任一層被污染，都可能造成語意供應鏈攻擊。

## 16.3 簽章與來源

高風險 overlay 應保存作者、組織、版本、簽章、審核者、依賴與有效期限。

## 16.4 政策不可被一般 overlay 覆寫

若：

$$
o_{\mathrm{local}}
$$

與：

$$
p_{\mathrm{security}}
$$

衝突，不能只依「較新」或「較具體」決定。高層政策的覆寫需要獨立授權程序。

---

# 十七、觀測、差分與人類可見狀態

## 17.1 Overlay diff

系統應顯示：

```text
added
removed
modified
moved
orphaned
conflicted
projection-changed
policy-changed
```

## 17.2 語意 diff 與文字 diff 不同

字串未改變，語意註冊表更新也可能改變行為。因此版本應包含：

$$
\Delta_{\mathrm{text}}
$$

與：

$$
\Delta_{\mathrm{semantic}}
$$

## 17.3 執行 trace

每個狀態差分應追溯到：

$$
\Delta W
\rightarrow
\left(
o,
\sigma,
D_j,
\pi_j,
V,
\text{authority}
\right)
$$

## 17.4 人類可見回報

人類不應被迫閱讀所有 IR。系統應回答：附加了什麼語意、影響哪個物件、哪些投影完整、哪些投影有損、哪些權限生效、執行後改變了什麼，以及如何撤銷。

---

# 十八、主要失敗模式

## 18.1 錨點漂移

overlay 附著到錯誤節點。

## 18.2 語意遮蔽

局部 overlay 意外覆蓋重要全域規則。

## 18.3 宿主洩漏

核心語意被某個後端模板綁定。

## 18.4 靜默近似

目標 adapter 無法完整表達，卻宣稱成功。

## 18.5 Profile 混淆

conceptual 或 EML-U 能力被誤稱為 EML-P 已實作能力。

## 18.6 UI 本體錯置

符號面板、右上角顯示或某個編輯器被誤認為 EML 本體。

## 18.7 註冊表碎裂

同一語意在不同專案具有不相容定義。

## 18.8 權限幻覺

模型理解 overlay，卻沒有批准它的權限。

## 18.9 過時 overlay

宿主或制度已變更，附加語意仍被視為有效。

## 18.10 不可見性債

機器使用大量 overlay，但人類無法理解其實際影響。

---

# 十九、可證偽研究綱領

## 19.1 錨點修復基準

對宿主進行插入、刪除、重命名、重排、格式化與重構，測量：

$$
\eta_{\mathrm{anchor}}
=
\frac{
\text{correctly relocated overlays}
}{
\text{all surviving overlays}
}
$$

並記錄錯綁率，因錯綁通常比 orphan 更危險。

## 19.2 跨宿主語意保持

對相同 Semantic IR 投影至多個宿主，測量：

$$
\phi_j
=
1-L_{\pi_j}
$$

並以測試與狀態差分，而非文字相似度判斷。

## 19.3 Round-trip 不動點

對可逆子集：

$$
o
\rightarrow
y_j
\rightarrow
\hat o
$$

測量：

$$
d(o,\hat o)
$$

## 19.4 靜默降級率

$$
R_{\mathrm{silent}}
=
\frac{
\text{unsupported semantics emitted without warning}
}{
\text{all unsupported cases}
}
$$

理想值為：

$$
R_{\mathrm{silent}}=0
$$

## 19.5 政策衝突偵測

建立多作用域、多權限與多時間規則，測量系統是否能正確產生 `resolved`、`blocked` 與 `review-required`。

## 19.6 AI 理解增益

比較 Agent 在只有宿主程式碼與加入 overlay 後，對修改正確率、權限遵守率、測試生成、錯誤定位、跨語言遷移與人類意圖保持的表現。

## 19.7 人類可見性

測量人類能否在不閱讀完整 IR 的情況下回答：什麼語意正在生效、哪些物件受影響、哪些投影有損，以及如何撤銷。

## 19.8 維護成本

比較語意散落於註解、文件與慣例，和語意集中於 EML overlay 兩種架構在大型專案中的：

$$
C_{\mathrm{maintenance}}
+
C_{\mathrm{handoff}}
+
C_{\mathrm{audit}}
$$

---

# 二十、與 Nova、SOS、Intent IR 的邊界

## 20.1 EML 與 Nova

EML 的起點是：

$$
\text{Existing Host}
+
\text{Semantic Overlay}
$$

Nova 的起點是：

$$
\text{Structure-Native Program Object}
$$

EML 偏向漸進附加與跨宿主中介；Nova 偏向讓型別化結構圖直接成為程式本體。

未來可有：

$$
\mathrm{EML\ Overlay}
\rightarrow
\mathrm{Nova\ Structural\ Node}
$$

但兩者不應互相吞併。

## 20.2 EML 與 SOS

SOS 研究：

$$
\widehat O(S)
=
\left(
G_S,
\operatorname{Sem}_S,
\operatorname{Comp}_S
\right)
$$

即符號自身如何成為算子閉包。

EML 研究：

$$
\text{Host Object}
+
\text{Attached Semantic Node}
$$

符號可以是 overlay 的表面投影，但 EML 不要求所有語意都濃縮為單一符號。

## 20.3 EML 與 Intent IR

Intent IR 負責表示目標、非目標、限制、偏好、成功條件、終止條件與權限。EML 可以承載 Intent IR 節點或把其部分語意附著於宿主，但不應把完整意圖編譯流程塞入 overlay 註冊表。

## 20.4 EML 與 Runtime

EML 描述語意及其投影契約；Runtime 負責能力選擇、工具調用、暫停與恢復、世界狀態執行與失敗恢復。EML 不是完整 Runtime。

---

# 二十一、本文的十五項命題

## 命題一

$$
\boxed{
\text{Program Semantics}
\not\subseteq
\text{One Source File}
}
$$

## 命題二

$$
\boxed{
\text{Semantic Overlay}
=
\text{Addressable Structured Meaning Attached to a Host}
}
$$

## 命題三

右上角是投影位置，不是語意本體。

## 命題四

$$
\boxed{
\operatorname{HID}
\neq
\operatorname{SID}
\neq
\operatorname{SurfaceID}
}
$$

## 命題五

EML 是通用語意附加協議，不是 Python 縮寫。

## 命題六

宿主中立不代表所有宿主能力相同，而代表核心語意不由單一宿主定義。

## 命題七

$$
\boxed{
\text{Unsupported}
\neq
\text{Approximately Supported Without Disclosure}
}
$$

## 命題八

AI 可以生成候選，但確定性核心、政策與驗證器決定是否接受。

## 命題九

overlay 必須具有作用域、有效期、權限、版本與撤銷機制。

## 命題十

文字 diff 不足以表示語意 diff。

## 命題十一

$$
\boxed{
\mathrm{EML\text{-}P}
\subseteq
\mathrm{EML\text{-}U}
}
$$

## 命題十二

EML-P 應優先工程化；EML-U 應獨立保存並逐步形式化。

## 命題十三

EML、Nova、SOS 與 Intent IR 位於不同層次，統一於共享介面，而非合併成單一超級語言。

## 命題十四

語意附加是一種治理權，建立、批准與執行必須分離。

## 命題十五

後文本程式設計不消滅文字，而是使語意身分能跨越單一文字表面存續。

---

# 二十二、第二部的起點：從語意附加走向結構本體

第一部已完成：

$$
\text{程式本體擴張}
\rightarrow
\text{自然語言原生計算}
\rightarrow
\text{形式化壓縮}
\rightarrow
\text{算子抽取}
$$

本篇開始回答：

> 形式化後的語意應如何存在，而不被綁死在單一文字或單一宿主？

EML 的答案是：

$$
\boxed{
\text{Host}
+
\text{Anchor}
+
\text{Semantic Overlay}
\rightarrow
\text{Host-Neutral Semantic IR}
\rightarrow
\text{Verified Projection}
}
$$

下一篇將進一步提出更激進的問題：

> 若語意與結構已能獨立於單一文字存在，程式是否還需要先寫成文字，再由解析器恢復結構？

Nova 的答案將是：

$$
\boxed{
\text{Structure Before Text}
}
$$

---

# 二十三、結論：語意必須能離開它第一次出現的表面

程式系統的語意經常第一次出現在某種表面上：一行 Python、一個符號、一段需求、一個資料欄位、一張工作流圖或一則組織規則。

但語意若永遠被困在第一次出現的表面，它就難以跨語言、跨工具、跨媒介、跨版本，被 Agent 使用，被獨立驗證，或被人類治理。

語意附加程式設計的核心，不是替所有物件貼更多標籤，而是建立一條可驗證的語意生命週期：

$$
\boxed{
\text{Attach}
\rightarrow
\text{Identify}
\rightarrow
\text{Validate}
\rightarrow
\text{Project}
\rightarrow
\text{Execute}
\rightarrow
\text{Observe}
\rightarrow
\text{Revise or Revoke}
}
$$

EML 的價值也不在於某一組特殊符號有多短，而在於它嘗試回答：

> 同一個語意，如何在不破壞既有系統的條件下，被附著、保存、投影、驗證、執行與追蹤？

因此本文的最終命題是：

$$
\boxed{
\text{文字可以承載語意，但不應永久壟斷語意身分。}
}
$$

$$
\boxed{
\text{宿主可以實現語意，但不應反過來定義全部語意。}
}
$$

$$
\boxed{
\text{AI 可以協助生成語意，但不能獨占語意的接受、授權與驗證。}
}
$$

當語意能離開單一表面，又能在多種表面之間保持來源、契約與驗證，程式設計才真正開始進入後文本時代。

---

# 附錄 A：最小 Overlay 格式

```yaml
overlay:
  overlay_id: "ovl-20260725-001"
  semantic_id: "eml.policy.requires_approval"
  status: "validated"

host:
  host_id: "project.release.workflow"
  host_type: "workflow"
  host_version: "git:4f29a1"

anchor:
  structural_path: "nodes/public_release"
  content_hash: "sha256:..."
  scope: "node"

parameters:
  authority: "human_owner"
  event: "public_release"

constraints:
  bypass_allowed: false
  expires_at: null

effects:
  - "block_until_approved"

policy:
  author: "project_owner"
  approver: "security_admin"
  risk_level: "high"

validation:
  schema: "passed"
  anchor: "passed"
  policy: "passed"
  projection:
    workflow_runtime: "preserved"
    human_summary: "preserved"

provenance:
  created_at: "2026-07-25T00:00:00+08:00"
  created_by: "authorized_user"
  interpreter_version: "eml-overlay-core-0.1"
```

---

# 附錄 B：宿主中立語意註冊項目

```json
{
  "semantic_id": "eml.algebra.aggregate.sum",
  "version": "1.0.0",
  "domain": "algebra",
  "schema": {
    "operation": "aggregate",
    "algebra": "additive_monoid",
    "iterator_binding": true,
    "range_policy": "declared"
  },
  "effects": [],
  "validators": [
    "type.compatible_addition",
    "range.declared",
    "binding.no_capture"
  ],
  "surface_forms": {
    "eml_p": ["Σ", "SUM"],
    "zh_tw": ["加總"],
    "en": ["sum"]
  },
  "projection_contracts": {
    "python": {
      "status": "preserved",
      "adapter": "eml.adapter.python.aggregate"
    },
    "cpp": {
      "status": "preserved",
      "adapter": "eml.adapter.cpp.aggregate"
    },
    "javascript": {
      "status": "partially-preserved",
      "adapter": "eml.adapter.js.aggregate",
      "notes": ["numeric type policy required"]
    }
  }
}
```

---

# 附錄 C：投影損失報告

```yaml
projection:
  source_semantic_id: "eml.time.wait_until"
  target_host: "legacy_shell"
  status: "approximated"

preserved:
  - "condition"
  - "timeout"

lost:
  - "non_blocking"
  - "persistent_resume"

introduced:
  - "polling_interval"
  - "process_lifetime_dependency"

risk:
  level: "medium"
  human_approval_required: true

alternatives:
  - target_host: "workflow_runtime"
    status: "preserved"
```

---

# 附錄 D：系列十二篇位置

1. 從程式碼到意圖：程式概念的歷史轉換與後文本時代
2. 自然語言原生計算：從語句生成到語義狀態轉換
3. 形式化壓縮與算子演化：自然語言、形式語言與計算結構的生成
4. **語意附加程式設計：EML 與宿主中立語義中介層**
5. 結構先於文字：Nova 與後文本程式語言本體論
6. 符號作為算子：從靜態字元到可組合計算閉包
7. 意圖中介表示：從自然語言要求到可驗證能力計畫
8. 時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行
9. Agent Runtime：能力規劃、工具調用與可恢復執行
10. 可編譯世界：從程式執行到世界狀態演化
11. 人類可見狀態：意圖程式系統的稽核、解釋與可逆治理
12. 意圖程式文明：後文本語言、持續 Agent 與可編譯世界的統一理論

---

# 參考文獻

## Neo.K／EveMissLab 理論與規格文件

1. Neo.K with Aletheia，《從程式碼到意圖：程式概念的歷史轉換與後文本時代》，2026。
2. Neo.K with Aletheia，《自然語言原生計算：從語句生成到語義狀態轉換》，2026。
3. Neo.K with Aletheia，《形式化壓縮與算子演化：自然語言、形式語言與計算結構的生成》，2026。
4. Neo.K，《EML 2026：通用語意附加協議與多宿主投影架構》，v2.0，2026。
5. Neo.K，《EML 雙版本架構：EML-P／EML-U》，v1.0，2026。
6. Neo.K，《EML 1.5 AI 語義規格：自足重寫版》，2026。
7. Neo.K，《EML-LANG-2026 v1.0》，2026。
8. Neo.K，《EML 2026：面向 AI Agent 的高密度語意附加程式語言》，2026。
9. Neo.K，《EML Minimal Intent Challenge》，2026。
10. Neo.K，《符號算子系統（Symbol-as-Operator System, SOS）》，2026。
11. Neo.K，《Nova Core Baseline v3.0》，2026。

## 一般理論背景

12. Codd, E. F., “A Relational Model of Data for Large Shared Data Banks,” 1970.
13. W3C, *RDF 1.1 Concepts and Abstract Syntax*, 2014.
14. Fowler, M., *Domain-Specific Languages*, 2010.
15. Kiczales, G. et al., “Aspect-Oriented Programming,” 1997.
16. Gamma, E. et al., *Design Patterns*, 1994.
17. Hoare, C. A. R., “An Axiomatic Basis for Computer Programming,” 1969.
18. Lamport, L., “Time, Clocks, and the Ordering of Events in a Distributed System,” 1978.

---

# 版本紀錄

## v0.1 — 2026-07-25

- 完成系列第四篇與第二部開篇。
- 將 EML 正式定位為通用語意附加協議。
- 建立宿主、錨點、overlay、註冊表、政策、適配器、驗證、投影與追蹤九元模型。
- 區分宿主身分、語意身分與表面身分。
- 建立複合錨點、漂移修復與 orphan 處理規則。
- 定義 overlay 作用域、有效期、狀態與撤銷。
- 建立八項核心操作代數。
- 加入 overlay 衝突、政策優先序與合併結果。
- 形式化宿主中立 Semantic IR 與投影損失。
- 明確區分確定性核心與 AI 候選生成。
- 整理 EML-P／EML-U 雙 Profile 及降級映射。
- 區分 EML 與 annotation、metadata、DSL、巨集、AST 擴充及 knowledge graph。
- 加入治理、供應鏈、觀測、失敗模式與八項可證偽研究基準。
- 明確界定 EML、Nova、SOS、Intent IR 與 Runtime 的邊界。
