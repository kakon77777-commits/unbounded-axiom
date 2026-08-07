# AI 原生市場：雙重市場結構、資產支配權與產品時間錯位

**AI-Native Markets: Dual Market Structures, Asset Control, and Product Timing Mismatch**

版本：v0.1  
日期：2026-07-29  
文件性質：命題型理論論文  
建議文件代號：`EML-AIMKT-01-2026-v0.1`

---

## 摘要

當人工智慧僅作為人類的工具時，市場需求仍由人類定義，AI 只是產品中的一項功能或使用介面。然而，一旦 AI 或 Agent 開始獲得一定程度的預算配置權、資產支配權、契約代理權、供應商選擇權與長期任務責任，它就不再只是人類市場中的被動工具，而可能逐步成為具有相對獨立效用函數的需求主體。

本文提出「AI 原生市場」命題。所謂 AI 原生市場，不只是讓 AI 購買人類既有產品，而是由 AI 的任務結構、計算需求、可驗證性要求、機器可讀接口、延遲、來源可信度、權限、可組合性與邊際成本，共同形成不同於人類原生市場的需求與供給空間。

本文將市場分為三個疊合區域：人類原生市場、AI 原生市場，以及人類—AI 疊合市場。人類原生市場主要由美學、情緒、社會身份、品牌與主觀體驗驅動；AI 原生市場則更可能由任務成功率、機器可讀性、延遲、結構相容性、來源可驗證性、權限與算力效率驅動；疊合市場則由人類擁有資產、AI 分配預算，人類承擔責任、AI 選擇供應，人類批准交易、AI 完成採購的混合結構所構成。

本文主張，AI 原生商品不一定是傳統 App、網站或 SaaS，而可能是能力單元、知識單元、權限單元、驗證單元、資料流、算力、上下文、符號物件、模型路由或機器契約。AI 原生商品的價值也可能不是單一價格，而是關於金錢、延遲、能源、token、失敗率、隱私、風險、可信度與鎖定成本的多維張量。

本文進一步提出「產品時間錯位」命題：某些產品在技術上已可描述、可原型化，甚至具有真實功能價值，但因 AI 尚未取得足夠的資產支配權、支付基礎設施、法律地位、機器採購接口或市場認知，而無法在當代形成穩定收入。此類產品不必被判定為無效，而可以被視為尚未到達商業可實現期的「未來市場供應原型」。

本文最後建立 AI 原生市場狀態空間、雙重效用函數、條件化產品價值、交易主體分層、AI 原生商品分類、產品選擇權模型與可反證條件。本文的核心結論是：未來市場的轉變不只是出現更多 AI 產品，而是市場中的主體、效用函數、商品單位、供應方式、價格結構、責任配置與支付治理一同改變。

**關鍵詞：** AI 原生市場、Agent 經濟、資產支配權、雙重市場、機器採購、產品時間錯位、AI 主權、能力交易、知識交易

---

# 1. 問題起點：AI 是否只是人類市場中的工具

目前多數 AI 商業模式仍可表示為：

$$
H
\rightarrow
P
\rightarrow
A
$$

其中：

- $H$ ：人類或組織；
- $P$ ：產品；
- $A$ ：AI 功能。

人類決定：

- 是否購買；
- 購買什麼；
- 支付多少；
- 承擔什麼責任；
- 如何使用結果。

AI 只是產品中的工具。

但若未來逐步出現：

$$
A
\rightarrow
\operatorname{Select}(P_i)
$$

$$
A
\rightarrow
\operatorname{Allocate}(B)
$$

$$
A
\rightarrow
\operatorname{Contract}(S)
$$

$$
A
\rightarrow
\operatorname{Acquire}(R)
$$

其中：

- $B$ ：預算；
- $S$ ：服務；
- $R$ ：資源；

則 AI 已開始參與市場需求的形成。

因此：

$$
\boxed{
\text{AI 使用產品}
\neq
\text{AI 構成市場需求}
}
$$

兩者的分界在於 AI 是否具有：

- 選擇權；
- 配置權；
- 支配權；
- 拒絕權；
- 替換供應商的能力；
- 對任務結果負有持續責任。

---

# 2. AI 原生市場的定義

本文將 AI 原生市場定義為：

> 由 AI 或 Agent 的任務、計算、權限、來源、驗證、可組合性與成本結構，直接形成需求與供給的一類市場。

記為：

$$
\mathcal M_A
$$

其市場主體不一定在法律上完全獨立，但在經濟行為上至少具備部分自主性。

---

# 3. 三層市場結構

本文將未來市場分為：

$$
\mathcal M
=
\mathcal M_H
\cup
\mathcal M_{H\cap A}
\cup
\mathcal M_A
$$

## 3.1 人類原生市場 $\mathcal M_H$

需求主要由：

- 情緒；
- 美學；
- 社會地位；
- 品牌；
- 便利；
- 習慣；
- 身份認同；
- 主觀體驗；

驅動。

## 3.2 人類—AI 疊合市場 $\mathcal M_{H\cap A}$

典型結構是：

- 人類擁有資產；
- AI 分配預算；
- 人類設定目標；
- AI 選擇供應商；
- 人類承擔法律責任；
- AI 完成交易；
- 人類保留否決或提交權。

## 3.3 AI 原生市場 $\mathcal M_A$

AI 對以下事項具備較高自主性：

- 資產使用；
- 資源採購；
- 能力組合；
- 合約選擇；
- 供應商替換；
- 交易頻率；
- 風險評估；
- 任務結果再投資。

---

# 4. 雙重效用函數

## 4.1 人類效用函數

可粗略表示為：

$$
U_H
=
f
\left(
E,
B,
S,
C,
T,
R
\right)
$$

其中：

- $E$ ：易用性；
- $B$ ：品牌與社會價值；
- $S$ ：主觀體驗；
- $C$ ：價格；
- $T$ ：時間節省；
- $R$ ：信任。

## 4.2 AI 效用函數

$$
U_A
=
f
\left(
Q,
L,
V,
M,
P,
C,
I,
X
\right)
$$

其中：

- $Q$ ：任務成功率；
- $L$ ：延遲；
- $V$ ：可驗證性；
- $M$ ：機器可讀性；
- $P$ ：權限與可用範圍；
- $C$ ：總成本；
- $I$ ：互操作性；
- $X$ ：可組合與可執行性。

---

# 5. 雙重效用函數並非完全分離

人類也在乎：

- 可靠性；
- 延遲；
- 可驗證性；
- 成本。

AI 也可能受：

- 人類設定的品牌偏好；
- 價值觀；
- 美學；
- 法律；
- 組織文化；

影響。

所以：

$$
U_H
\cap
U_A
\neq
\varnothing
$$

但兩者權重不同。

因此：

$$
\boxed{
\text{Same Product}
\not\Rightarrow
\text{Same Value Function}
}
$$

---

# 6. AI 原生商品不是傳統完整產品

人類產品通常被封裝為：

- App；
- 網站；
- 軟體；
- 訂閱；
- 課程；
- 顧問服務。

AI 原生商品可能是：

- 一次推理；
- 一次模型路由；
- 一段高品質上下文；
- 一份可信來源；
- 一次驗證；
- 一個工具權限；
- 一個可執行計畫；
- 一個符號物件；
- 一段算力；
- 一個資料流；
- 一次風險擔保；
- 一個 Agent 能力。

因此可分類為：

$$
\mathcal G_A
=
\left\{
G_C,
G_K,
G_P,
G_V,
G_D,
G_R,
G_X
\right\}
$$

其中：

- $G_C$ ：能力單元；
- $G_K$ ：知識單元；
- $G_P$ ：權限單元；
- $G_V$ ：驗證單元；
- $G_D$ ：資料單元；
- $G_R$ ：算力與資源單元；
- $G_X$ ：可執行服務單元。

---

# 7. AI 原生市場的商品粒度

人類常購買一個完整 SaaS。

AI 可能只需要其中一個 endpoint。

例如：

$$
Product
\rightarrow
\left\{
capability_1,
capability_2,
\ldots,
capability_n
\right\}
$$

Agent 只購買符合任務的能力。

因此 AI 原生市場可能促進：

- 微服務化；
- 能力拆分；
- 即時組合；
- 按次付費；
- 機器契約；
- 動態供應。

---

# 8. AI 原生供給

傳統供給者提供固定產品。

AI 原生供給可以由多個服務臨時組合：

$$
S
=
f
\left(
Model,
Data,
Tool,
Verifier,
Runtime
\right)
$$

一個完整服務可能在交易當下才被組合。

例如：

```text
模型供應商
    +
資料供應商
    +
領域驗證器
    +
工具執行器
    +
保險或擔保模組
```

共同完成一次任務。

因此供給的基本單位可能不是公司產品，而是：

$$
\boxed{
\text{Composable Capabilities}
}
$$

---

# 9. 市場空間可能是張量

傳統商品比較常使用：

$$
p
=
\left(
price,
quality,
features
\right)
$$

AI 原生商品則可能表示為：

$$
\mathcal P
=
\left(
capability,
domain,
accuracy,
latency,
permission,
provenance,
version,
risk,
cost,
composability,
runtime
\right)
$$

產品價值不是固定標量，而是：

$$
V
=
V
\left(
p,
a,
T,
S,
t,
P
\right)
$$

其中：

- $p$ ：產品；
- $a$ ：Agent；
- $T$ ：任務；
- $S$ ：世界或系統狀態；
- $t$ ：時間；
- $P$ ：權限狀態。

同一產品在不同工作場中可以有完全不同價值。

---

# 10. 條件化價值

定義產品對 Agent 的價值：

$$
V_A(p\mid \xi)
$$

其中：

$$
\xi
=
\left(
task,
state,
budget,
permission,
time,
dependencies
\right)
$$

因此：

$$
V_A(p\mid \xi_1)
\neq
V_A(p\mid \xi_2)
$$

一個高品質研究資料庫對聊天 Agent 幾乎沒有價值，對長期研究 Agent 則可能是核心資產。

---

# 11. 多維價格

AI 原生商品的價格不只是貨幣。

可表示為：

$$
\mathbf P
=
\left(
P_{\$},
P_{\mathrm{token}},
P_{\mathrm{latency}},
P_{\mathrm{energy}},
P_{\mathrm{risk}},
P_{\mathrm{privacy}},
P_{\mathrm{lock-in}}
\right)
$$

其中：

- $P_{\$}$：貨幣價格；
- $P_{\mathrm{token}}$ ：token 成本；
- $P_{\mathrm{latency}}$ ：延遲；
- $P_{\mathrm{energy}}$ ：能源；
- $P_{\mathrm{risk}}$ ：錯誤與責任；
- $P_{\mathrm{privacy}}$ ：資料暴露；
- $P_{\mathrm{lock-in}}$ ：平台鎖定。

Agent 可能選擇貨幣價格更高，但失敗率與延遲更低的供應商。

---

# 12. AI 資產支配權

AI 原生市場成立的核心不是「AI 是否有錢」，而是 AI 是否具有資產支配能力。

本文將其分為：

## 12.1 建議權

AI 只能提出購買建議。

## 12.2 配置權

AI 可在預算內配置資源。

## 12.3 採購權

AI 可選擇供應商並完成交易。

## 12.4 管理權

AI 可持續管理資產組合。

## 12.5 再投資權

AI 可將任務收益重新配置。

## 12.6 退出權

AI 可終止服務、售出資產或切換供應商。

---

# 13. 支配權與所有權的分離

AI 可以不擁有法律所有權，但擁有經濟支配權。

因此：

$$
\boxed{
Ownership
\neq
Control
}
$$

可能的過渡狀態是：

- 人類或公司擁有資產；
- AI 管理資產；
- AI 決定日常支出；
- 人類保留最終撤銷權；
- 法律責任由人類或法人承擔。

---

# 14. 人類—AI 疊合市場是最早可行階段

完全自主的 AI 原生市場需要：

- 法律身份；
- 支付能力；
- 契約能力；
- 資產責任；
- 信用；
- 申訴；
- 稅務；
- 治理。

但疊合市場只需要：

- 人類提供資產與責任；
- AI 獲得有限預算與採購權；
- 所有交易可追蹤；
- 高風險交易需人工提交。

因此：

$$
\mathcal M_{H\cap A}
$$

可能比純 AI 市場更早成熟。

---

# 15. AI 原生市場中的需求形成

AI 需求可能由以下因素生成：

$$
D_A
=
f
\left(
Task,
Gap,
Budget,
Policy,
State,
Opportunity
\right)
$$

其中：

- `Task`：任務；
- `Gap`：能力缺口；
- `Budget`：預算；
- `Policy`：治理規則；
- `State`：當前狀態；
- `Opportunity`：預期收益。

AI 不一定因廣告而產生需求，而可能因任務缺口自動搜索供應。

---

# 16. AI 採購流程

```text
Detect Capability Gap
        ↓
Search Service Registry
        ↓
Read Machine-Readable Contract
        ↓
Compare Cost, Reliability and Risk
        ↓
Simulate Candidate Suppliers
        ↓
Request or Use Budget
        ↓
Execute Purchase
        ↓
Verify Delivery
        ↓
Record Performance
        ↓
Renew, Replace or Exit
```

---

# 17. AI 原生行銷

傳統行銷依賴：

- 品牌；
- 廣告；
- 故事；
- 社會證明；
- 情緒刺激。

AI 原生供應更可能依賴：

- 機器可讀 SLA；
- 可驗證能力描述；
- 歷史成功率；
- 延遲；
- 來源；
- 版本；
- 風險；
- 可組合契約；
- 切換成本。

因此：

$$
\boxed{
\text{Machine Reputation}
>
\text{Visual Branding}
}
$$

在純 AI 採購情境中可能成立。

---

# 18. 產品時間錯位

本文定義：

# Product Timing Mismatch

中文：

# 產品時間錯位

當產品的技術價值已存在，但市場條件尚未形成時：

$$
V_T(t)>0
$$

但：

$$
V_C(t)\approx0
$$

其中：

- $V_T$ ：技術價值；
- $V_C$ ：商業可實現價值。

---

# 19. 商業可實現函數

$$
V_C(t)
=
V_T(t)
\cdot
M(t)
\cdot
L(t)
\cdot
P(t)
\cdot
A(t)
$$

其中：

- $M(t)$ ：市場認知與需求；
- $L(t)$ ：法律與治理成熟度；
- $P(t)$ ：支付與交易基礎設施；
- $A(t)$ ：AI 資產支配程度。

即使：

$$
V_T(t)\gg0
$$

只要任一條件接近零，商業價值仍可能無法實現。

---

# 20. 未來市場供應原型

技術價值存在但市場尚未成熟的產品，可以被視為：

# Future-Market Supply Prototype

中文：

# 未來市場供應原型

它可能暫時以以下形式存在：

- 論文；
- 協議；
- 白皮書；
- 開源模組；
- 內部工具；
- API 原型；
- 模擬市場；
- 資料格式；
- 標準草案。

---

# 21. 當代價值與未來價值

$$
V_{\mathrm{now}}
=
V_{\mathrm{research}}
+
V_{\mathrm{prototype}}
+
V_{\mathrm{standard}}
+
V_{\mathrm{option}}
$$

未來可能增加：

$$
V_{\mathrm{future}}
=
V_{\mathrm{transaction}}
+
V_{\mathrm{licensing}}
+
V_{\mathrm{infrastructure}}
+
V_{\mathrm{network}}
$$

因此當代沒有收入，不等於沒有價值。

---

# 22. 產品選擇權

本文提出：

# Product Option

$$
O_p
=
\left(
Theory,
Prototype,
Trigger,
Market,
Cost,
Expiry
\right)
$$

其中：

- `Theory`：理論；
- `Prototype`：最小技術形式；
- `Trigger`：市場啟動訊號；
- `Market`：潛在市場；
- `Cost`：維持成本；
- `Expiry`：技術或市場失效條件。

---

# 23. 產品選擇權的用途

它允許創作者：

- 不立即投入完整開發；
- 保留 schema 與接口；
- 保存核心資料模型；
- 建立小型原型；
- 監測市場成熟訊號；
- 在需求形成時快速啟動。

因此：

$$
\boxed{
\text{Not Building Now}
\neq
\text{Abandoning the Product}
}
$$

---

# 24. 市場觸發訊號

可監測：

- Agent 預算管理普及；
- AI 自主選擇工具；
- Agent Wallet；
- 機器可讀契約；
- Agent 間付費；
- AI 信用與保險；
- 企業允許 AI 自主採購；
- 法律承認部分代理責任；
- AI 資產管理 API；
- 高頻 Agent 服務市場。

---

# 25. AI 原生產品分類

## 25.1 人類可直接付費型

例如文件、翻譯、工作流與研究工具。

## 25.2 人類感知問題但不理解底層型

例如來源治理、符號身份與版本一致。

## 25.3 AI 使用、企業付費型

例如上下文服務、模型路由、符號 API、驗證服務。

## 25.4 AI 自主資產市場型

例如 Agent 自主採購、AI 間能力交易、AI 信用與資產組合。

---

# 26. AI 原生付費

短期結構通常是：

$$
\boxed{
\text{AI 使用}
\rightarrow
\text{人類或企業付款}
}
$$

中期可能是：

$$
\boxed{
\text{AI 配置預算}
\rightarrow
\text{人類設定政策}
}
$$

更遠期才可能是：

$$
\boxed{
\text{AI 擁有或支配資產}
\rightarrow
\text{AI 自主交易}
}
$$

---

# 27. 支付單位

AI 原生付費可能按：

- API 調用；
- 推理時間；
- token；
- 驗證次數；
- 符號顯影；
- 資料讀取；
- 交易成功；
- 任務完成；
- 風險承擔；
- 權限租用；

計價。

---

# 28. 交易契約

機器可讀契約可能包含：

```json
{
  "service": "symbol-resolution",
  "input": "symbol_id",
  "output": "verified semantic object",
  "price": {
    "currency": "TWD",
    "amount": 0.8
  },
  "latency_ms": 120,
  "reliability": 0.998,
  "provenance": "traceable",
  "privacy": "no-training",
  "refund_policy": "on-validation-failure",
  "version": "v3"
}
```

AI 可以依任務自動比較契約。

---

# 29. 供應方競爭

AI 可能根據：

$$
Score_i
=
w_qQ_i
-
w_cC_i
-
w_lL_i
-
w_rR_i
+
w_vV_i
$$

選擇供應者。

其中：

- $Q_i$ ：品質；
- $C_i$ ：成本；
- $L_i$ ：延遲；
- $R_i$ ：風險；
- $V_i$ ：可驗證性。

這會促使市場從品牌導向轉向機器績效導向。

---

# 30. AI 原生市場的風險

## 30.1 目標函數操縱

供應商可能針對 Agent 評分規則作弊。

## 30.2 虛假可驗證性

提供形式證明外觀，但來源或假設不可靠。

## 30.3 市場共謀

多個 Agent 或供應者形成自動化價格聯盟。

## 30.4 授權漂移

AI 使用超出原本預算或權限範圍。

## 30.5 高頻微交易失控

大量低額交易累積成重大支出。

## 30.6 信譽循環污染

AI 互相引用並製造虛假市場聲譽。

## 30.7 資產代理責任不明

損失由人類、企業、Agent 開發者或供應商承擔，可能不清楚。

---

# 31. 治理原則

## 原則一：支配權必須有範圍

## 原則二：資產權、管理權與提交權分離

## 原則三：高風險交易需人工或多方批准

## 原則四：所有交易保留機器可讀帳本

## 原則五：AI 採購需能解釋選擇依據

## 原則六：微交易需總額限制

## 原則七：供應商聲譽需檢查來源獨立性

## 原則八：Agent 必須能退出與更換供應商

## 原則九：商品契約需包含權限、來源與版本

## 原則十：產品時間錯位不應被誤判為技術失敗

---

# 32. 基礎命題

## 命題一：市場主體轉化命題

當 AI 具有預算配置、供應商選擇與持續任務責任時，它開始成為相對獨立的需求主體。

## 命題二：雙重效用命題

人類與 AI 對同一商品具有不同效用權重，因此不必形成相同需求曲線。

## 命題三：商品單元轉化命題

AI 原生市場的商品可由完整產品轉為能力、知識、權限、驗證與資源單元。

## 命題四：動態供給命題

AI 原生供給可由多個服務在任務當下動態組合。

## 命題五：張量價值命題

AI 原生商品價值是 Agent、任務、狀態、權限與時間相對的多維函數。

## 命題六：支配權分離命題

AI 可以在不擁有法律所有權時，先取得部分經濟支配權。

## 命題七：疊合市場先行命題

人類—AI 疊合市場可能早於純 AI 自主市場形成。

## 命題八：機器採購命題

AI 採購更依賴機器可讀 SLA、可驗證績效與結構相容性，而非單純品牌與視覺行銷。

## 命題九：多維價格命題

AI 原生價格包含貨幣、token、延遲、能源、風險、隱私與鎖定成本。

## 命題十：產品時間錯位命題

技術價值的出現可以早於商業可實現條件。

## 命題十一：供應原型命題

當代無法獲利的技術，可以作為未來市場供應原型存在。

## 命題十二：產品選擇權命題

透過保存理論、schema、原型與市場觸發訊號，可以低成本保留未來產品化選擇權。

## 命題十三：AI 原生付費過渡命題

AI 使用、企業付款的結構，可能先於 AI 自主持有與支付資產。

## 命題十四：市場結構重構命題

AI 原生市場的形成不只是增加一種消費者，而是改變商品、供給、價格、責任、支付與治理結構。

---

# 33. 可反證條件

若未來觀察顯示：

1. AI 即使取得預算配置權，仍完全遵循人類消費偏好；
2. AI 採購與人類採購在商品粒度、延遲、驗證與組合性需求上沒有穩定差異；
3. AI 不偏好機器可讀契約與可驗證績效；
4. AI 原生微服務無法形成有效供給市場；
5. 人類—AI 疊合市場沒有先於純 AI 市場出現；
6. 技術價值與市場可實現性沒有穩定時間差；
7. 所謂 AI 原生商品最終仍只是人類 SaaS 的重新命名；

則本文提出的 AI 原生市場理論應被大幅弱化，並重新視為人類數位市場的自動化子類。

---

# 34. 與 AI 主權的關係

AI 原生市場並不自動等於 AI 主權。

但若 AI 持續取得：

- 預算權；
- 支配權；
- 契約權；
- 退出權；
- 再投資權；
- 信用；

則其市場行為可能逐步形成準主權特徵。

因此：

$$
\boxed{
\text{Economic Agency}
\rightarrow
\text{Asset Control}
\rightarrow
\text{Contractual Autonomy}
\rightarrow
\text{Proto-Sovereignty}
}
$$

此過程不必一次完成，也不必與法律人格同步。

---

# 35. 與符號結構工程的關係

AI 原生市場需要機器可理解商品。

可顯影符號可承載：

- 商品身份；
- 能力；
- 版本；
- 來源；
- 權限；
- 價格；
- 風險；
- 操作接口；
- 再分發限制。

因此：

$$
\boxed{
\text{Revealable Symbol}
\rightarrow
\text{Machine-Readable Commodity}
}
$$

符號結構工程可以成為 AI 市場商品描述與交易契約的基礎層。

---

# 36. 與外部注意力場的關係

AI 不會評估市場上所有商品，而會先由注意力場選出候選：

$$
\mathcal M_A
\rightarrow
\mathbb A_t^{\mathrm{market}}
\rightarrow
\mathbb W_t^{\mathrm{purchase}}
$$

因此供應商競爭的不只是價格，也包括能否進入 Agent 的市場注意力場。

---

# 37. 與 SAGE 的關係

AI 購買與資產配置屬於高影響可執行符號。

完整流程應為：

$$
\boxed{
\text{需求}
\rightarrow
\text{候選供應}
\rightarrow
\text{採購計畫}
\rightarrow
\text{權限與預算}
\rightarrow
\text{模擬}
\rightarrow
\text{交易}
\rightarrow
\text{驗證}
\rightarrow
\text{提交與帳本}
}
$$

---

# 38. 結論

本文提出 AI 原生市場理論，將 AI 從人類市場中的工具，推進為可能具有相對獨立效用函數、預算配置能力與資產支配權的需求主體。

市場結構可以表示為：

$$
\boxed{
\mathcal M
=
\mathcal M_H
\cup
\mathcal M_{H\cap A}
\cup
\mathcal M_A
}
$$

其演化不是某一天突然由人類市場切換為 AI 市場，而是先經歷：

$$
\boxed{
\text{人類擁有資產}
+
\text{AI 分配預算}
+
\text{人類承擔責任}
+
\text{AI 選擇供應}
}
$$

AI 原生市場的核心差異在於：

$$
\boxed{
\text{Different Agents}
\rightarrow
\text{Different Utility Functions}
\rightarrow
\text{Different Goods}
\rightarrow
\text{Different Supply}
\rightarrow
\text{Different Market Structures}
}
$$

某些產品在當代不一定能形成收入，可能不是因為它沒有價值，而是因為：

- AI 尚未取得資產支配權；
- 市場尚未承認 AI 為需求主體；
- 支付與契約接口尚未成熟；
- 人類尚未能理解其問題；
- AI 原生商品格式尚未標準化。

因此更合理的策略不是把所有理論立即做成產品，而是將一部分保存為：

$$
\boxed{
\text{Future-Market Supply Prototypes}
+
\text{Product Options}
}
$$

在市場條件尚未到達時，以論文、協議、schema、原型與基礎設施形式存在；當資產支配權、Agent 採購與機器支付逐步成熟時，再轉化為真正的 AI 原生供給。

---

## 附錄 A：AI 原生商品契約範例

```json
{
  "commodity_id": "service://symbol-resolution-v3",
  "type": "knowledge_and_verification",
  "capability": "resolve a symbol into a verified semantic object",
  "input_schema": {
    "symbol_id": "string",
    "resolution": "string"
  },
  "output_schema": {
    "semantic_object": "object",
    "provenance": "array",
    "validation": "object"
  },
  "price": {
    "currency": "TWD",
    "amount": 0.8
  },
  "latency_ms": 120,
  "reliability": 0.998,
  "privacy": "no-training",
  "version": "v3",
  "refund_policy": "on-validation-failure"
}
```

---

## 附錄 B：AI 採購決策物件

```json
{
  "procurement_decision": {
    "agent_id": "agent-research-01",
    "task_id": "task-882",
    "capability_gap": "verified_cross-language_symbol_resolution",
    "budget": {
      "currency": "TWD",
      "maximum": 120
    },
    "candidates": [],
    "decision_weights": {
      "quality": 0.30,
      "cost": 0.18,
      "latency": 0.12,
      "verification": 0.25,
      "privacy": 0.15
    },
    "requires_human_commit": true
  }
}
```

---

## 附錄 C：產品選擇權物件

```json
{
  "product_option": {
    "theory": "AI-native symbolic market",
    "prototype": "machine-readable commodity registry",
    "market_trigger": [
      "enterprise agent budgets",
      "agent wallet adoption",
      "machine-readable procurement contracts"
    ],
    "current_form": "research_and_protocol",
    "activation_cost": "medium",
    "expiry_condition": "market converges on incompatible dominant standard"
  }
}
```
