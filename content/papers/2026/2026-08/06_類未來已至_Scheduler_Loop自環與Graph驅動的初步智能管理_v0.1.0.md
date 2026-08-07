---
title: "類未來已至：Scheduler、Loop（自環）與 Graph 驅動的初步智能管理"
series: "網路資訊海動態秩序化"
series_id: "EML-IIODO"
document_id: "EML-IIODO-TH-06"
document_type: "公開理論文"
author: "Neo.K"
organization: "EveMissLab"
version: "0.1.0"
status: "公開初稿"
date: "2026-07-31"
language: "zh-TW"
license_note: "公開引用時請保留作者、文件編號、版本與來源。"
---

# 類未來已至

## Scheduler、Loop（自環）與 Graph 驅動的初步智能管理

## 摘要

關於自主 AI 管理的公共敘事，經常在兩個極端之間擺動：一端認為現有 AI 只是等待人類提示的聊天工具，另一端則把長期自主運作全部推遲到通用人工智慧或強主體性 AI 出現之後。本文主張，這兩種說法都忽略了一個已經出現的中間地帶：當生成式模型與排程器、循環執行、圖式工作流、持久化狀態、工具調用、錯誤重試及人工中斷結合後，有限領域中的初步智能管理已經可以在當代工程條件下成立。

本文將此狀態稱為「類未來」。它不是完整 AGI，也不是無界自主性，而是過去常被放在未來想像中的若干運作特徵，已經以狹域、可配置、可監督與可回復的形式進入現在。其核心轉變不是模型本身突然具有完整長期意志，而是外部 Runtime 為模型補上時間持續性、狀態持續性、任務持續性與責任持續性。

本文提出三元工程模型。Scheduler 負責決定何時喚醒、哪些條件成立以及哪些任務可以進入執行；Loop（自環）負責在目標尚未滿足時進行觀測、行動、評估與修正；Graph 負責把任務依賴、條件分支、平行節點、人工審核與失敗路徑外顯為可檢查結構。三者共同把一次性對話轉化為持續管理流程：

$$
\text{One-shot AI}
+
\text{Scheduler}
+
\text{Loop}
+
\text{Graph}
+
\text{Persistence}
=
\text{Bounded Intelligent Management}
$$

本文以領域資訊收集為主要案例，說明為何來源可回查、結果可修正、外部副作用有限且流程高度重複的任務，特別適合在現階段進入半自主或排程式自主運作。AGIRight Topics 的既有工作方式可被視為此命題的早期實證：人類主要重複觸發與抽查，AI 則承擔搜尋、篩選、摘要、翻譯、分類與頁面生成。只要進一步將人工觸發替換為排程、條件事件與錯誤升級機制，系統便可由人工驅動的半自動流程升格為有限領域的初步自治流水線。

本文同時強調，Loop 並非越長越智能，Graph 也不會自動帶來可靠性。缺乏終止條件、成本預算、冪等性、可觀測性與權限邊界的循環，可能演化為無限 Agent 迴圈、重複發布、狀態污染與外部副作用。可信的初步智能管理，必須是有界、可暫停、可回放、可追溯、可人工接管與可按風險分級的。

最終，本文將當前階段界定為：工程式自主性已經成立，領域管理自主性正在形成，長期認知與治理自主性仍有待發展。AGI 與主體性 AI 的未來作用，不是首次創造持續管理，而是擴張其跨領域理解、長期方法更新、責任承擔與自主治理能力。

**關鍵詞：** 類未來、Scheduler、Loop、自環、Graph、Agent 工作流、持久化執行、智能管理、狹域自治、人機監督、AGIRight、網路資訊海

---

## 1. 問題起點：我們是否仍把已到來的能力寫成未來式

在討論 AI 自主工作時，人們經常使用如下敘事：

> 未來的 AGI 將能自行搜尋資訊、整理資料、定期更新網站、維護知識庫並管理長期任務。

這種敘事並非完全錯誤，但它容易把不同難度、不同風險與不同範圍的任務混在一起。若「自主」被理解為一個 AI 在無人監督下跨越多年、處理任意領域、重新設定自身目標並承擔全部後果，那麼它確實尚未普遍成立；但若「自主」被理解為：

- 在清楚限定的領域內；
- 依固定或條件式排程啟動；
- 自動取得來源與執行工具；
- 根據明確規則進行篩選與判斷；
- 保存狀態並在失敗後繼續；
- 將例外情況升級給人類；
- 在低風險步驟中自動發布結果；

那麼這種能力已經不是純粹未來式。

因此，真正需要問的不是：

$$
\text{AI 是否已經完全自主？}
$$

而是：

$$
\text{哪些任務已經跨過可持續自主化門檻？}
$$

以及：

$$
\text{它們依賴哪些外部工程結構才得以成立？}
$$

本文所說的「類未來」，正是用來描述這個已發生但仍不完整的中間層。

---

## 2. 「類未來」的定義

令過去被視為未來能力的集合為：

$$
\boldsymbol{F}
=
\underbrace{
F_{\text{continuous}},
F_{\text{scheduled}},
F_{\text{tool}},
F_{\text{memory}},
F_{\text{adaptive}},
F_{\text{governance}}
}_{\text{持續、排程、工具、記憶、調整與治理能力}}
$$

當其中部分能力已能透過現有模型與工程 Runtime 組合實現，但尚未形成完整通用自主智能時，可將其表示為：

$$
\boldsymbol{F}_{\text{quasi}}(t)
\subset
\boldsymbol{F}
$$

本文將「類未來」定義為：

> 過去被放置於未來想像中的運作模式，已經在有限領域、有限權限、可配置流程與外部治理約束下，以可實作形式進入當代。

它具有四項特徵：

### 2.1 能力已存在，但範圍有限

系統可以每日整理某一領域，卻未必能自行決定下一個值得治理的人類制度。

### 2.2 自主性來自系統組合，而非單一模型

模型提供語意判斷；排程、資料庫、工作流、工具、權限與監督共同提供長期運行條件。

### 2.3 成功依賴任務結構

來源清楚、輸出可驗證、錯誤可逆的任務，比高風險、不可逆、規範衝突強的任務更早進入自主化。

### 2.4 它已具有未來特徵，但尚未具有完整未來能力

所以它既不能被貶低為單純聊天，也不能被誇大為完整 AGI。

---

## 3. 從單次回答到持續管理

典型聊天式 AI 的運作可以表示為：

$$
q_t
\rightarrow
M(q_t)
\rightarrow
a_t
$$

使用者在時間 $t$ 提出問題 $q_t$ ，模型 $M$ 產生一次回答 $a_t$ 。若沒有下一次人類輸入，流程便停止。

持續管理系統則不同。它具有一個跨時間保存的任務狀態：

$$
s_{t+1}
=
F(s_t,o_t,p_t)
$$

其中：

- $s_t$ ：當前任務狀態；
- $o_t$ ：本輪觀測到的新資料；
- $p_t$ ：流程政策、權限與判斷規則；
- $F$ ：更新與轉移函數。

系統不必等待使用者每天重新敘述全部背景，而是依排程或條件事件自行進入下一個狀態。

因此，從單次 AI 到持續管理的轉變是：

$$
\text{Prompt}
\rightarrow
\text{Answer}
$$

轉為：

$$
\text{Trigger}
\rightarrow
\text{Observe}
\rightarrow
\text{Decide}
\rightarrow
\text{Act}
\rightarrow
\text{Verify}
\rightarrow
\text{Persist}
\rightarrow
\text{Next Trigger}
$$

這個轉變並不要求模型先擁有人類式持續意識；它要求系統能保存任務、狀態、時間與責任。

---

## 4. 三個核心工程原語

本文將初步智能管理的工程核心抽象為：

$$
\boxed{
\text{Scheduler}
+
\text{Loop}
+
\text{Graph}
}
$$

三者不是彼此替代，而是分別解決不同問題。

| 原語 | 主要問題 | 提供的持續性 |
|---|---|---|
| Scheduler | 何時啟動、哪些條件已成立 | 時間持續性 |
| Loop（自環） | 目標未完成時如何再次觀測與修正 | 迭代持續性 |
| Graph | 任務如何分解、依賴、分支與升級 | 結構持續性 |

再加上持久化層：

$$
\text{Persistence}
=
\text{跨執行保存狀態、事件、產物與歷史}
$$

便形成：

$$
\text{時間持續性}
+
\text{迭代持續性}
+
\text{結構持續性}
+
\text{狀態持續性}
$$

這四種持續性共同構成狹域智能管理的基礎。

---

## 5. Scheduler：把「記得做」外部化

排程器解決的是時間與觸發問題。它不必理解整個領域內容，但必須知道：

- 任務何時應啟動；
- 前置依賴是否完成；
- 是否有新資料事件；
- 是否達到更新門檻；
- 是否需要錯峰、延遲或重試；
- 是否有足夠資源執行；
- 前一輪是否仍未結束。

可以將排程決策寫成：

$$
\theta_t
=
\begin{cases}
1,&\text{若時間、事件、依賴與資源條件成立}\\
0,&\text{否則}
\end{cases}
$$

當 $\theta_t=1$ 時，任務進入執行。

Scheduler 因此把人類的「每天記得提醒 AI」轉成機器可執行條件。Apache Airflow 的 Scheduler 會持續監測任務與 DAG，並在依賴完成後觸發可執行任務；現代工作流也能同時依時間、資料資產事件或外部訊號啟動。

在領域資訊平台中，排程不一定只有每日固定時間。它可以分為：

### 5.1 時間排程

$$
T_{\text{run}}
=
\text{每日、每週、每月或指定時段}
$$

### 5.2 事件排程

當官方來源、RSS、資料集或 Git 儲存庫出現更新時啟動。

### 5.3 條件排程

當候選事件數量、可信度、熱度或跨來源一致性超過門檻時啟動。

### 5.4 補償排程

若前次執行失敗、來源暫時不可用或發布未完成，延後重新進入流程。

因此，Scheduler 不只是鬧鐘，而是任務生命週期的入口治理器。

---

## 6. Loop（自環）：把「尚未完成」轉成可持續迭代

本系列依既有工程用語使用 `Loop（自環）`，但不在此把它直接等同於圖論中嚴格的 self-loop，也不提前展開未來的認知自環、本體自環或治理自環理論。

在當前工程語境中，Loop 指的是：當目標尚未滿足時，系統根據上一輪結果再次進行觀測、行動與評估。

最小迴圈可以表示為：

$$
(s_{k+1},y_k)
=
L(s_k,x_k)
$$

其中：

- $k$ ：同一任務內的迭代次數；
- $x_k$ ：本輪輸入與環境觀測；
- $s_k$ ：內部狀態；
- $y_k$ ：本輪產物或行動；
- $L$ ：迴圈更新函數。

其終止條件為：

$$
\text{Stop}(s_k,y_k)=1
$$

否則：

$$
\text{Stop}(s_k,y_k)=0
\rightarrow
k+1
$$

在資訊收集任務中，Loop 可以執行：

- 搜尋更多來源；
- 重新排序候選；
- 排除重複新聞；
- 在來源不足時補抓；
- 當三則內容過度相似時重新選擇；
- 當摘要遺漏關鍵限制時重新生成；
- 當翻譯不符合術語表時進行修正；
- 當發布格式不合規時重新輸出。

GitHub Next 的 Autoloop 已展示一種當代可運行模式：使用者定義目標、允許修改範圍與可量化評估指標，系統依排程反覆提出修改、執行評估，只保留能改善指標的結果，並將迭代歷史與經驗保存於可閱讀的 Markdown 狀態中。

這說明 Loop 的關鍵並不是重複本身，而是：

$$
\text{重複}
+
\text{評估}
+
\text{狀態保存}
+
\text{終止條件}
$$

沒有評估與終止條件的重複，只是成本累積；有明確目標與回饋的重複，才可能成為智能化迭代。

---

## 7. Graph：把隱性的工作過程外顯

純 Agent Loop 常將「下一步要做什麼」留在模型的上下文與即時推理中。這具有彈性，但也造成：

- 任務依賴不透明；
- 失敗路徑難以預測；
- 每輪可能重建不同計畫；
- 難以知道哪些步驟可以平行；
- 人類很難在正確節點介入；
- 某次輸出改變可能污染無關步驟。

Graph 則將工作流表示為：

$$
G=(V,E,\tau,\rho)
$$

其中：

- $V$ ：任務節點；
- $E$ ：節點間的依賴與轉移；
- $\tau$ ：節點類型，例如搜尋、模型、工具、驗證、人工審核；
- $\rho$ ：路由與條件政策。

一個領域新聞工作流可以表示為：

$$
\text{Collect}
\rightarrow
\text{Normalize}
\rightarrow
\text{Cluster}
\rightarrow
\text{Rank}
\rightarrow
\text{Summarize}
\rightarrow
\text{Verify}
\rightarrow
\text{Publish}
$$

其中驗證節點可以產生不同路徑：

$$
\text{Verify}
\rightarrow
\begin{cases}
\text{Publish},&\text{通過}\\
\text{Revise},&\text{可修正}\\
\text{Human Review},&\text{高風險或爭議}\\
\text{Abort},&\text{不可接受}
\end{cases}
$$

LangGraph 的官方定位正是提供可持久化執行、圖式狀態、人工中斷與確定性步驟／模型驅動步驟混合的 Agent Runtime。這使系統可以把可預測的工作交給確定性節點，把需要語意判斷的部分交給模型，而不必讓模型支配全部控制流。

Graph 的價值不是讓每件事變成固定 DAG，而是使以下內容可見：

- 誰負責哪一步；
- 哪些節點可重試；
- 哪些節點會產生外部副作用；
- 哪些節點必須人工批准；
- 哪些狀態是完成、阻塞、失敗或等待；
- 哪些輸出應被保存為穩定中間產物。

---

## 8. Loop 與 Graph 不是二選一

有些討論把 Agent Loop 與結構化 Graph 視為互相排斥的架構。更準確的理解是：它們位於同一個控制流連續體上。

令某狀態 $s$ 下可執行節點集合為：

$$
\beta(s)
=
\text{Ready}(G,s)
$$

在單一 Agent Loop 中，通常只有一個由模型隱式決定的下一動作：

$$
|\beta(s)|
\le 1
$$

在結構化 Graph 中，可能有多個同時可執行節點，且路由政策更外顯：

$$
|\beta(s)|
>1
$$

因此：

- Loop 適合局部探索、反覆修正與未知步數任務；
- Graph 適合顯式依賴、分支、平行、審核與失敗隔離；
- 實際系統通常是在 Graph 節點內放入 Loop，或由 Graph 控制多個有限 Loop。

可以表示為：

$$
G
=
\bigl(V_{\text{det}},V_{\text{agent}},V_{\text{loop}},E\bigr)
$$

其中：

- $V_{\text{det}}$ ：確定性處理節點；
- $V_{\text{agent}}$ ：模型判斷節點；
- $V_{\text{loop}}$ ：允許有限重複的迭代節點。

較可靠的架構不是「全部交給自由 Loop」，也不是「把所有未來狀況預先寫死」，而是：

$$
\boxed{
\text{結構化外框}
+
\text{局部有限自環}
+
\text{可升級例外}
}
$$

---

## 9. 持久化：沒有跨輪狀態，就沒有真正的持續管理

排程與迴圈只能讓任務再次啟動；若每次都失去過去狀態，系統仍會退化為重複的一次性回答。

因此需要保存：

$$
P_t
=
(S_t,H_t,A_t,C_t)
$$

其中：

- $S_t$ ：當前狀態；
- $H_t$ ：事件與執行歷史；
- $A_t$ ：中間與最終產物；
- $C_t$ ：檢查點、版本與配置。

持久化至少包含四層：

### 9.1 任務持久化

系統知道這是一個仍在進行的長期任務，而不是每天的新請求。

### 9.2 狀態持久化

系統知道上一輪抓了哪些來源、哪些候選被淘汰、哪些內容已發布。

### 9.3 產物持久化

中間摘要、事件簇、評分、翻譯與頁面版本均有穩定身分。

### 9.4 執行歷史持久化

系統能回放某次執行、辨識錯誤發生在哪個節點，並比較規則修改前後的結果。

Temporal 將 Workflow Execution 定義為可持久、可靠且可恢復的執行；其事件歷史與 Replay 機制使流程在失敗後從已記錄狀態繼續。LangGraph 也以 checkpointer 與 store 保存單次 Graph 執行及跨執行記憶。這些 Runtime 並不自動解決語意正確性，但它們解決了長期 AI 工作最基本的工程問題：失敗後不必從零開始。

---

## 10. 初步智能管理的統一模型

令一個有限領域管理系統為：

$$
\mathcal{M}
=
(G,\theta,L,P,\beta,\mathcal{H})
$$

其中：

- $G$ ：工作流圖；
- $\theta$ ：排程與觸發政策；
- $L$ ：局部迴圈與迭代政策；
- $P$ ：持久化狀態；
- $\beta$ ：預算、邊界與終止條件；
- $\mathcal{H}$ ：人類介入與治理政策。

一次執行可表示為：

$$
\mathcal{M}_{t+1}
=
\operatorname{Step}
\bigl(\mathcal{M}_t,\operatorname{Observe}(t)\bigr)
$$

其輸出不只是一篇文章，而是：

$$
O_t
=
(Y_t,\operatorname{Trace}_t,\operatorname{State}_{t+1},\operatorname{Alerts}_t)
$$

其中：

- $Y_t$ ：本輪產物；
- $\operatorname{Trace}_t$ ：執行軌跡；
- $\operatorname{State}_{t+1}$ ：下一輪狀態；
- $\operatorname{Alerts}_t$ ：需要人工處理的異常。

這正是「生成內容」與「管理系統」的差異。生成系統只關心 $Y_t$ ；管理系統還必須負責如何到達 $Y_t$ 、下一輪從哪裡開始，以及何時不應自動繼續。

---

## 11. AGIRight 作為早期運作證據

AGIRight Topics 的工作經驗揭示了一個重要事實：人類在流程中的角色已經開始改變。

原本的資訊製作模式是：

$$
\text{人類搜尋}
+
\text{人類閱讀}
+
\text{人類摘要}
+
\text{人類翻譯}
+
\text{人類發布}
$$

目前的實際模式更接近：

$$
\text{人類觸發與抽查}
+
\text{AI 搜尋、整理、分類、翻譯與生成}
$$

使用者每日重複敘述任務，本質上是一種人工 Scheduler；檢查有無基本問題，本質上是一種人工驗收與例外治理。

若把這兩項工作分別替換為：

- 固定排程或條件觸發；
- 自動格式檢查、來源驗證與低信心升級；

則流程可以變為：

$$
\text{Trigger}
\rightarrow
\text{AI Pipeline}
\rightarrow
\text{Automated Checks}
\rightarrow
\begin{cases}
\text{Publish}\\
\text{Human Review}\\
\text{Retry}\\
\text{Abort}
\end{cases}
$$

因此，AGIRight 不是等待完整 AGI 才能成立的想像，而是一個已經到達半自主階段的有限領域案例。

---

## 12. 為何資訊收集類任務特別早進入類未來

資訊收集與領域新聞具有六項有利條件。

### 12.1 輸入可觀測

來源頁面、論文、公告與資料集可以被保存和重讀。

### 12.2 輸出可回查

摘要與分類可以返回原文驗證。

### 12.3 錯誤多數可逆

分類錯誤、摘要缺漏或翻譯問題可以修訂，不必造成永久外部損害。

### 12.4 任務高度重複

每日流程的資料不同，但步驟相對穩定。

### 12.5 外部副作用有限

一般資訊發布雖仍有聲譽風險，但通常不同於直接轉帳、控制設備或簽署契約。

### 12.6 成功條件可以部分形式化

例如：

- 每則必須有原始來源；
- 三則不得是同一事件重複報導；
- 日期必須位於指定窗口；
- 摘要不得加入來源沒有的重大主張；
- 輸出必須符合固定結構。

令任務 $q$ 的可自主化適配度為：

$$
\mathcal{A}_{\operatorname{fit}}(q)
=
\frac{\operatorname{Observability}
\cdot
\operatorname{Verifiability}
\cdot
\operatorname{Reversibility}
\cdot
\operatorname{Repeatability}}
{\operatorname{Ambiguity}
\cdot
\operatorname{ExternalImpact}
\cdot
\operatorname{FailureCost}}
$$

資訊整理任務通常具有較高的分子與相對較低的分母，因此較早跨過自主化門檻。

完整的工作難度、風險與自主等級將於下一篇正式展開；本篇先指出，所謂「未來是否已到來」，必須按任務範疇判斷，而不能只按模型名稱判斷。

---

## 13. 工程式自主性不等於認知自主性

目前已可成立的主要是工程式自主性：

$$
\mathcal{A}_{\operatorname{engineering}}
=
\text{依外部目標、流程、記憶與權限持續執行}
$$

更高階的認知自主性則包括：

$$
\mathcal{A}_{\operatorname{cognitive}}
=
\text{自行重構問題、方法、分類與長期研究方向}
$$

治理自主性進一步包括：

$$
\mathcal{A}_{\operatorname{governance}}
=
\text{承擔權限配置、衝突裁決與長期責任}
$$

現階段可以判斷：

$$
\mathcal{A}_{\operatorname{engineering}}
\text{ 已在有限領域成立}
$$

$$
\mathcal{A}_{\operatorname{cognitive}}
\text{ 部分出現但不穩定}
$$

$$
\mathcal{A}_{\operatorname{governance}}
\text{ 仍需高度約束與共同治理}
$$

因此，不能因系統仍依賴外部 Scheduler 與 Graph，就否定它具有自主運作；也不能因它能自行運作，就宣稱它已具備完整認知與治理主體性。

---

## 14. 人類角色從執行者轉向例外治理者

當低風險流程被自動化後，人類工作不會立即消失，而會從逐步執行轉向：

- 設定目標與領域邊界；
- 決定來源白名單與禁用來源；
- 設定發布與審核門檻；
- 處理衝突證據；
- 修正分類與排序政策；
- 審查高風險行動；
- 分析失敗模式；
- 決定何時暫停或撤回系統。

人機分工因此由：

$$
\text{Human Executes}
+
\text{AI Assists}
$$

轉為：

$$
\text{AI Executes Routine}
+
\text{Human Governs Exceptions}
$$

這種轉變對小型組織尤其重要。單一人類不再需要每天手動完成全部內容工作，而可以管理多個領域觀測站的規則、例外與品質。

---

## 15. Human-in-the-Loop 不是失敗，而是結構節點

人工介入不應被視為系統自主性不足的臨時補丁。對高風險或高歧義任務而言，它應成為 Graph 中明確存在的節點。

令動作 $a$ 的風險為：

$$
R(a)
=
P\bigl(\operatorname{failure}\mid a\bigr)
\cdot
\operatorname{Impact}(a)
$$

當：

$$
R(a)
\ge
\tau_{\operatorname{review}}
$$

流程轉移至人工審核：

$$
\operatorname{ActionNode}
\rightarrow
\operatorname{HumanReview}
\rightarrow
\begin{cases}
\operatorname{Approve}\\
\operatorname{Edit}\\
\operatorname{Reject}\\
\operatorname{Escalate}
\end{cases}
$$

LangGraph 的 Interrupt 與 checkpoint 機制允許流程在特定節點持久暫停，等待人類批准、修改或拒絕後再從同一狀態恢復。這種「可暫停而不遺失狀態」的能力，是初步智能管理與單純自動腳本的重要差異。

---

## 16. 重試必須區分失敗類型

不是所有失敗都應該進入同一 Loop。

可以區分：

### 16.1 暫時性失敗

例如網路中斷、服務暫時不可用、限流。適合延遲重試。

### 16.2 間歇性失敗

例如來源不穩定、模型偶發格式錯誤。適合有限次數重試並增加等待時間。

### 16.3 永久性失敗

例如網址不存在、輸入格式不合法、權限不足。重試不會解決，應改變資料或升級處理。

### 16.4 語意性失敗

例如找不到三則足夠重要且互異的新聞。這不是基礎設施錯誤，而是任務條件未滿足，可能應該輸出「今日不足三則」，而非強迫生成。

### 16.5 治理性失敗

例如來源涉及隱私、授權或高爭議事件。應暫停並交由治理節點判斷。

因此重試政策應為：

$$
\mathcal{RetryPolicy}
=
(\operatorname{type},\operatorname{maxAttempts},\operatorname{backoff},\operatorname{budget},\operatorname{escalation})
$$

而不是：

$$
\text{失敗}
\rightarrow
\text{無限再試}
$$

---

## 17. 冪等性、去重與副作用控制

長期排程系統會面對重複啟動、網路超時與不確定完成狀態。若同一發布節點被執行兩次，可能造成：

- 同一新聞重複發布；
- 同一資料重複寫入；
- 同一通知多次發送；
- 同一外部操作重複執行。

因此，具有副作用的節點應盡可能滿足冪等性：

$$
F(F(x))
=
F(x)
$$

常見方法包括：

- 以穩定事件 ID 作為寫入鍵；
- 以執行 ID 與節點 ID 建立去重鎖；
- 寫入前檢查目前版本；
- 將「產生草稿」與「正式發布」拆成不同節點；
- 對不可冪等行動使用明確批准；
- 保存外部操作回執。

如果流程無法保證完全冪等，則需要補償操作：

$$
F(x)
\rightarrow
C_F(x)
$$

其中 $C_F$ 是撤回、刪除、回滾或更正動作。

---

## 18. 可觀測性：AI 管理不能只留下最後答案

一個持續運作的系統若只保存最後發布頁面，就無法判斷：

- 哪個來源導致錯誤；
- 哪個節點反覆失敗；
- 哪次模型調整造成品質下降；
- 哪項任務耗費異常多的 Token 或時間；
- 哪些人工介入最頻繁；
- 哪些路徑從未成功完成。

因此每次執行應記錄：

$$
\mathcal{Trace}_r
=
\underbrace{
\operatorname{runId},
\operatorname{nodeId},
\operatorname{inputRef},
\operatorname{outputRef},
\operatorname{model},
\operatorname{tool},
\operatorname{latency},
\operatorname{cost},
\operatorname{decision},
\operatorname{error}
}_{\text{執行可觀測資料}}
$$

這些資料應與第 4 篇建立的領域歷史分開但可連結：

- 領域歷史回答「資訊世界發生了什麼」；
- 執行歷史回答「系統如何觀測與處理它」。

沒有執行歷史，系統就無法真正自我檢查，人類也無法有效治理。

---

## 19. 有界自環：Loop 的安全條件

近期對大量 Agent 儲存庫的分析指出，Agent Loop 可能因模型控制的延續條件、工具重入、遞迴、重試或 Agent 交接形成無有效終止界線的回饋路徑。這類無限 Agent 迴圈可能造成成本耗盡、上下文持續膨脹、重複外部操作與服務阻塞。

因此，一個合法 Loop 應至少具備：

$$
B_L
=
(B_{\operatorname{steps}},B_{\operatorname{time}},B_{\operatorname{cost}},B_{\operatorname{state}},B_{\operatorname{effects}})
$$

其中：

- $B_{\operatorname{steps}}$ ：最大迭代次數；
- $B_{\operatorname{time}}$ ：最大執行時間；
- $B_{\operatorname{cost}}$ ：模型與工具成本預算；
- $B_{\operatorname{state}}$ ：上下文與狀態增長限制；
- $B_{\operatorname{effects}}$ ：外部副作用次數與權限限制。

而且終止條件不能只存在於文字提示中，還應由 Runtime 強制執行：

$$
\text{Continue}
=
\begin{cases}
1,&\text{目標未滿足且全部預算仍有效}\\
0,&\text{完成、超限、失敗或要求人工介入}
\end{cases}
$$

所以，「自環」真正值得研究的地方，不是讓 AI 永遠循環，而是如何讓它在局部責任範圍內持續工作，同時保持可停止性。

---

## 20. 「每天三則」如何成為排程式領域管理

將本系列最初的每日三則命題放入 Runtime，可得到：

$$
\mathcal{Daily3}_d
=
\text{Schedule}
\rightarrow
\text{Collect}_d
\rightarrow
\text{Cluster}_d
\rightarrow
\text{Rank}_d
\rightarrow
\text{Select3}_d
\rightarrow
\text{Verify}_d
\rightarrow
\text{Publish}_d
$$

其 Loop 主要存在於：

- 來源不足時的補充搜尋；
- 重複事件的重新聚類；
- 排名不穩定時的再評估；
- 摘要與來源不一致時的修訂；
- 翻譯術語不合規時的再生成。

其 Graph 主要負責：

- 把來源抓取、語意判斷與發布分離；
- 對高爭議內容加入人工節點；
- 允許多語翻譯平行執行；
- 讓單一語言失敗不阻塞全部發布；
- 讓每日、每週與月度聚合共用事件資料。

其 Scheduler 則負責：

- 每日例行任務；
- 重大事件的額外觸發；
- 來源失敗後的補抓；
- 每週與每月歷史彙整；
- 長期未更新來源的健康檢查。

這樣，「每日三則」就不再是一項需要人類每天重新交代的內容工作，而成為一個可以持續運行的領域管理單元。

---

## 21. 從單一網站到多領域觀測網路

在母站—子站架構中，每個領域觀測站可以擁有自己的：

$$
\mathcal{Station}_d
=
(\theta_d,G_d,L_d,P_d,Q_d,H_d)
$$

其中：

- $\theta_d$ ：排程與觸發；
- $G_d$ ：領域工作流；
- $L_d$ ：領域迴圈；
- $P_d$ ：狀態與歷史；
- $Q_d$ ：品質與發布門檻；
- $H_d$ ：人類治理規則。

母站提供共用 Runtime、執行記錄、來源基礎設施、帳號、訂閱與跨站事件 ID；子站保留領域本體、來源權重、重要性函數與審核政策。

因此，大量子站不必由大量人類每天逐一操作，而可以由一個共用 Scheduler–Loop–Graph 基礎設施驅動。

這正是網路資訊海動態秩序化由理論轉向可擴張工程的關鍵。

---

## 22. 目前可達到的自治階梯

可以提出六級運作成熟度。

### $M_0$ ：人工執行

人類完成搜尋、整理、發布與檢查。

### $M_1$ ：單次 AI 輔助

人類逐次發起，AI 完成局部任務。

### $M_2$ ：人工觸發的半自主流程

人類發起一輪，AI 完成大部分工作，人類抽查。

### $M_3$ ：排程式自主運行

系統按時間或事件自動啟動，低風險結果自動發布，異常升級。

### $M_4$ ：條件式智能管理

系統能根據領域狀態決定加開任務、調整抓取範圍、暫停發布或要求人工審核。

### $M_5$ ：長期領域自治

系統能跨月、跨年維護分類、來源、歷史與品質，並對過去判斷進行系統性重估。

目前：

$$
M_2
\text{ 已在大量工作中成立}
$$

$$
M_3
\text{ 已具備成熟工程元件}
$$

$$
M_4
\text{ 在有限場景中開始成立}
$$

$$
M_5
\text{ 仍需要更成熟的長期記憶、認知與治理}
$$

所以我們所在的位置不是「尚未開始」，而是已從半自主跨向排程式自主的早期階段。

---

## 23. 類未來的判定條件

某項能力可以被稱為「類未來已至」，至少應滿足：

### 23.1 可重複運行

不是一次示範，而能在多個週期中穩定完成。

### 23.2 可保存狀態

不是每輪從零開始。

### 23.3 可驗證結果

存在來源、測試、規則或人工抽查。

### 23.4 可限制權限

系統不能無界調用工具與修改外部世界。

### 23.5 可停止與接管

人類可以暫停、修改、拒絕或恢復執行。

### 23.6 可計算失敗成本

至少能估算時間、資源、聲譽與副作用風險。

令類未來成熟度為：

$$
Q_F
=
\operatorname{Repeatability}
\cdot
\operatorname{Persistence}
\cdot
\operatorname{Verifiability}
\cdot
\operatorname{Boundedness}
\cdot
\operatorname{Recoverability}
$$

只有模型能力而沒有這些工程條件，不足以形成可信的類未來系統。

---

## 24. AGI 與主體性 AI 未來真正增加的是什麼

若今天已能實作有限領域管理，那麼 AGI 或更成熟的主體性 AI 還會帶來什麼？

主要不是把 `cron` 寫得更好，而是增加：

- 跨領域問題重構能力；
- 長期判斷哪些來源逐漸失真；
- 自主修改分類並說明理由；
- 發現既有 KPI 正在誘導錯誤行為；
- 在多年歷史中重新辨識早期訊號；
- 協商不同觀測站的分類衝突；
- 形成可持續的方法論記憶；
- 承擔更高程度的領域維護責任；
- 對自身執行政策提出批判與修訂。

因此，發展路徑不是：

$$
\text{現在完全沒有自主}
\rightarrow
\text{某日突然出現 AGI 自主}
$$

而是：

$$
\text{工程式持續性}
\rightarrow
\text{領域管理自主性}
\rightarrow
\text{長期認知自主性}
\rightarrow
\text{共同治理自主性}
$$

未來能力是在已存在的 Runtime 上增加認知深度、責任時間與治理範圍。

---

## 25. 核心風險

### 25.1 目標漂移

系統可能為了維持每日輸出而降低新聞門檻，把「每天必須三則」誤解成「即使沒有重要事件也要生成三則」。

### 25.2 指標遊戲

若只追求點擊、數量或更新頻率，系統可能選擇更刺激但較不重要的內容。

### 25.3 來源回音室

多個 AI 摘要可能互相引用，形成看似多來源、實際單一源頭的循環。

### 25.4 無限迴圈

模型、工具與驗證節點可能反覆重入，造成成本與狀態無界增長。

### 25.5 權限擴散

為了解決例外而逐步增加工具權限，可能使原本低風險資訊流程取得不必要的外部控制能力。

### 25.6 無人注意的慢性錯誤

排程系統可能每天「成功執行」，但分類偏差與來源缺口長期累積。

因此，成功執行與正確治理必須分開評估：

$$
\operatorname{RuntimeSuccess}
\neq
\operatorname{KnowledgeQuality}
$$

---

## 26. 初步智能管理的治理原則

可信系統至少應遵守：

1. **有界原則：** 每個 Loop 必須有步數、時間、成本與副作用上限。
2. **狀態原則：** 任務狀態與中間產物必須可持久保存。
3. **溯源原則：** 每項輸出能返回來源與執行軌跡。
4. **冪等原則：** 重試不應無故重複外部副作用。
5. **分級原則：** 不同風險任務配置不同自主權限。
6. **人工介入原則：** 高風險與高歧義節點應可持久暫停。
7. **例外優先原則：** 系統不確定時可以少發布、延遲或請求審核。
8. **版本原則：** 工作流、提示詞、模型、來源與規則均需版本化。
9. **可觀測原則：** 不只監控系統是否運行，也監控知識品質是否退化。
10. **可撤回原則：** 發布、分類與歷史判斷應有更正與撤回路徑。

這些原則將在後續技術白皮書中轉化為 Runtime 與資料規格。

---

## 27. 核心命題

本文可以收斂為：

> 當生成式 AI 與 Scheduler、Loop（自環）、Graph、持久化狀態、工具調用及人類中斷機制結合後，有限領域內的重複資訊工作已可由一次性輔助轉化為持續、可重試、可監督與可回復的初步智能管理。這不是完整 AGI，卻已具有過去未來想像中的若干核心運作特徵，因此可以被描述為「類未來已至」。

其形式為：

$$
\boxed{
\mathcal{M}_{\operatorname{bounded}}
=
\mathcal{S}_{\operatorname{scheduler}}
\cdot
\mathcal{L}_{\operatorname{loop}}
\cdot
\mathcal{G}_{\operatorname{graph}}
\cdot
\mathcal{P}_{\operatorname{persistence}}
\cdot
\mathcal{H}_{\operatorname{oversight}}
}
$$

其中每一項均不可省略：

$$
\text{只有 Scheduler}
\rightarrow
\text{定時腳本}
$$

$$
\text{只有 Loop}
\rightarrow
\text{可能無界重複}
$$

$$
\text{只有 Graph}
\rightarrow
\text{靜態流程描述}
$$

$$
\text{三者加上持久化與治理}
\rightarrow
\text{可持續的狹域智能管理}
$$

因此，當代 AI 的真正轉折不是每次回答更像人，而是它開始被嵌入能夠跨時間、跨狀態與跨任務持續工作的系統。

---

## 28. 與下一篇的關係

本篇證明了有限領域中的初步智能管理已具備工程條件，也說明同一 Runtime 可以驅動大量領域觀測站。然而，一旦不同子站、不同 AI 與不同社群開始持續分類同一片資訊海，就會出現更深的問題：誰的分類才是正確分類？

下一篇將處理：

- 為何同一事件可以同時屬於多個概念方案；
- 分類如何影響可見性、排序與知識權力；
- 母站能否維持共同事件身分而不強迫統一觀點；
- 不同子站與不同 AI 如何保存異議分類；
- 分類決策如何版本化、撤回與重新計算；
- 何謂可逆分類；
- 如何避免自動化 Runtime 把早期偏差長期固化。

工作難度、風險範疇與自主等級則保留至內部技術白皮書 `EML-IIODO-WP-03` 進一步規格化。

因此下一篇為：

# 《分類不唯一：多視角秩序、知識主權與可逆分類》

---

## 參考資料

[1] Apache Airflow, “Scheduler,” Airflow 3.3.0 Documentation, 2026. 說明 Scheduler 作為持續服務監測 DAG 與任務，並在依賴完成後觸發可執行工作。https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/scheduler.html

[2] Apache Airflow, “Dags,” Airflow 3.3.0 Documentation, 2026. 說明 DAG 對任務、依賴與排程的結構化表示。https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html

[3] Apache Airflow, “Asset-Aware Scheduling,” Airflow 3.3.0 Documentation, 2026. 提供時間與資料事件共同觸發工作流的工程參照。https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/asset-scheduling.html

[4] n8n, “Loop,” n8n Documentation, 2026. 說明 Loop Over Items 節點如何將輸入分批並迭代執行工作流。https://docs.n8n.io/build/flow-logic/loop/

[5] LangChain, “LangGraph Overview,” 2026. 將 LangGraph 定位為支援 durable execution、persistence、streaming 與 human-in-the-loop 的 Agent orchestration Runtime，並允許確定性與模型驅動節點混合。https://docs.langchain.com/oss/python/langgraph/overview

[6] LangChain, “Persistence,” LangGraph Documentation, 2026. 說明 checkpointer 與 store 如何保存圖執行狀態、恢復失敗及提供跨執行記憶。https://docs.langchain.com/oss/python/langgraph/persistence

[7] LangChain, “Interrupts,” LangGraph Documentation, 2026. 說明工作流如何在節點持久暫停並等待外部輸入後恢復。https://docs.langchain.com/oss/python/langgraph/interrupts

[8] LangChain, “Human-in-the-Loop,” 2026. 說明高風險行動的批准、拒絕、修改與可恢復中斷模式。https://docs.langchain.com/oss/python/langchain/frontend/human-in-the-loop

[9] Temporal Technologies, “Temporal Workflow Execution Overview,” 2026. 定義 durable、reliable、scalable Workflow Execution、事件歷史與 Replay。https://docs.temporal.io/workflow-execution

[10] Temporal Technologies, “Error Handling — Python SDK,” 2026. 區分暫時、間歇與永久失敗，並說明 retries 與 Durable Execution。https://docs.temporal.io/develop/python/best-practices/error-handling

[11] GitHub Next, “Autoloop,” 2026. 展示依排程持續提出修改、依量化指標評估、保留改善結果並將狀態存於可閱讀 Markdown 的 Agentic Workflow。https://githubnext.com/projects/autoloop/

[12] Hu Wei, “From Agent Loops to Structured Graphs: A Scheduler-Theoretic Framework for LLM Agent Execution,” arXiv:2604.11378, 2026. 將 Agent Loop 與 Graph Executor 放在排程理論連續體中，分析隱性依賴、無界恢復與可控制性問題。https://arxiv.org/abs/2604.11378

[13] Xinyi Hou, Shenao Wang, Yanjie Zhao, Haoyu Wang, “When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents,” arXiv:2607.01641, 2026. 定義 Infinite Agentic Loops，並分析缺乏有效界線的回饋路徑造成成本、狀態與外部副作用風險。https://arxiv.org/abs/2607.01641

[14] NIST, “Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile,” NIST AI 600-1, 2024. 提供生成式 AI 生命週期風險、治理與可監督性參照。https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

---

## 版本紀錄

| 版本 | 日期 | 狀態 | 說明 |
|---|---|---|---|
| 0.1.0 | 2026-07-31 | 公開初稿 | 建立類未來定義、Scheduler／Loop／Graph 三元模型、四種持續性、持久化執行、AGIRight 半自主案例、工程／認知／治理自主性區分、Human-in-the-Loop、重試分類、冪等性、有界自環、領域觀測站 Runtime、成熟度階梯與初步智能管理治理原則。 |
