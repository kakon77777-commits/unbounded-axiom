# 訂閱、API 與 Compute Wallet：AI 混合計價制度
## Subscription, API, and the Compute Wallet: A Hybrid Pricing Architecture for AI Services

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Paper 3 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

生成式 AI 的商業模式正在逐漸脫離「純訂閱制」與「純 API 按量制」的二分法。完整 AI 產品越來越多地整合模型、記憶、搜尋、檔案、程式執行、Agent、語音、圖像、工作空間與各種連接器；另一方面，高頻使用者、企業與 Agentic Workflow 又需要比固定訂閱額度更具彈性的資源取得方式。因此，單純要求高頻使用者「改用 API」並不能完整解決產品體驗、成本可預測性、功能整合與算力彈性之間的矛盾。

本文提出 **Compute Wallet** 作為 AI 混合計價制度的中介層。其核心不是將所有產品退化成逐 Token 收費，而是建立一個抽象資源帳本，使訂閱內含權利、額外加購、跨功能使用、超額消耗、rollover、borrow、折扣時段與未來可能的 surrender 機制可以在同一制度中協調。本文進一步區分 Membership Value、Compute Entitlement、Wallet Balance、Throughput Right 與 Monetary Settlement，避免將「付了多少錢」「擁有多少產品功能」「可以消耗多少算力」「當下能跑多快」錯誤視為同一變數。

本文分析 OpenAI、Anthropic 與 Cursor 等現行產品所呈現的混合化趨勢。這些產品已分別出現方案內含額度、shared credit pools、extra usage、按 API 價格超額使用、usage dashboards 與 spend limits，顯示市場已開始驗證「固定訂閱＋彈性用量」的可行性。然而，現行制度仍普遍存在資源池割裂、跨產品不可轉換、額度失效、價格映射不透明與 API／訂閱兩套經濟體系分離等問題。

本文的核心命題是：

$$
\boxed{
\text{Membership}
+
\text{Compute Wallet}
+
\text{Elastic Overage}
+
\text{Throughput Control}
}
$$

比純訂閱或純 API 更適合未來的整合式 AI 產品。Compute Wallet 應該充當「使用權與實際算力成本之間的抽象層」，而非成為另一個迫使一般使用者理解 Token 定價的複雜帳單系統。

**關鍵詞：** Compute Wallet、AI 訂閱制、API 計價、混合計價、Usage-Based Pricing、Credits、Rollover、Borrow、Spend Limit、AI 算力經濟

---

## 1. 從時間可替代性走向資源可替代性

前兩篇分別提出：

$$
T_{\mathrm{billing}}
\neq
T_{\mathrm{entitlement}}
\neq
T_{\mathrm{compute}}
\neq
T_{\mathrm{work}}
$$

以及：

$$
\text{Temporal Fungibility}
\neq
\text{Unlimited Throughput}
$$

這解決了「何時可以使用」與「瞬時能使用多快」的概念分離。

但當一名使用者同時使用：

- Chat；
- Coding Agent；
- Deep Research；
- Image Generation；
- Voice；
- Spreadsheet Agent；
- Workspace Agent；
- API；

下一個問題就自然出現：

> 為什麼這些功能一定要存在彼此割裂的額度池？

如果底層共同消耗的是某種計算、儲存、網路、工具與模型資源，那麼產品層是否可以建立一個共同的資源抽象？

本文將這個中介層稱為：

$$
\boxed{
\text{Compute Wallet}
}
$$

但 Compute Wallet 不應被理解成單純的：

$$
\text{Token Wallet}
$$

也不應被理解成：

$$
\text{Cash Wallet}
$$

它更接近：

$$
\boxed{
\text{abstract entitlement ledger}
}
$$

也就是「抽象使用權帳本」。

---

## 2. 為什麼純訂閱制不夠

純訂閱的優點非常明顯。

對使用者而言：

$$
P_{\mathrm{month}}=\text{constant}
$$

因此預算高度可預測。

使用者不需要在每次 interaction 前重新估計：

$$
P_i
=
f(
\text{input tokens},
\text{output tokens},
\text{cache},
\text{reasoning},
\text{tools}
)
$$

這種價格抽象可以降低：

$$
C_{\mathrm{cognitive\ pricing}}
$$

亦即使用者理解與監控價格所需的認知成本。

然而純訂閱也存在結構問題。

假設每名使用者支付相同價格：

$$
P_1=P_2=\cdots=P_n
$$

但實際成本為：

$$
C_1,C_2,\ldots,C_n
$$

且可能：

$$
\max_i C_i\gg E[C_i]
$$

那麼高頻使用者可能使：

$$
C_i>P_i
$$

長期而言，平台只能透過：

- 降低內含量；
- 設定時間窗；
- 限制模型；
- 限制 Agent；
- 提高方案價格；
- 依賴輕度使用者交叉補貼；

控制單位經濟。

因此：

$$
\text{Flat Subscription}
$$

很適合提供「可預測的基本使用權」，卻不一定適合承擔無限制的高變異算力消耗。

---

## 3. 為什麼純 API 也不夠

API 按量計價在經濟上非常直接：

$$
P_{\mathrm{API}}
=
\sum_j p_j q_j
$$

其中 $q_j$ 可以是 input token、output token、cached token、image、audio、tool invocation 或其他計費單位。

這對企業與開發者具有高度彈性：

$$
\text{pay only for what you use}
$$

但純 API 存在另一組成本。

完整 AI 產品通常提供：

$$
\begin{aligned}
V_{\mathrm{product}}
={}&
V_{\mathrm{model}}
+
V_{\mathrm{UI}}
+
V_{\mathrm{memory}}
+
V_{\mathrm{files}}\\
&+
V_{\mathrm{search}}
+
V_{\mathrm{agent}}
+
V_{\mathrm{connectors}}
+
V_{\mathrm{code}}\\
&+
V_{\mathrm{voice}}
+
V_{\mathrm{workspace}}
+\cdots
\end{aligned}
$$

API 則通常只提供其中的一部分能力介面。

若使用者自行重建完整產品體驗，其總成本更接近：

$$
C_{\mathrm{API,total}}
=
C_{\mathrm{usage}}
+
C_{\mathrm{engineering}}
+
C_{\mathrm{hosting}}
+
C_{\mathrm{integration}}
+
C_{\mathrm{maintenance}}
+
C_{\mathrm{security}}
$$

因此：

$$
\boxed{
\text{API}
\neq
\text{Integrated AI Product}
}
$$

把所有高頻使用者推向 API，等於要求使用者自行承擔原本由產品供應商完成的整合成本。

---

## 4. 混合制度的基本結構

本文提出的基礎架構是：

$$
\boxed{
\text{AI Plan}
=
\text{Membership}
+
\text{Included Compute}
+
\text{Compute Wallet}
+
\text{Elastic Overage}
}
$$

其中四者功能不同。

### 4.1 Membership

Membership 購買的是產品與服務資格。

例如：

$$
M
=
\{
\text{models},
\text{memory},
\text{workspace},
\text{connectors},
\text{privacy},
\text{support}
\}
$$

它不應被完全還原成 Token 數量。

---

### 4.2 Included Compute

訂閱方案內含某種基本資源權利：

$$
Q_{\mathrm{included}}
$$

這部分提供「固定月費帶來的可預測價值」。

---

### 4.3 Compute Wallet

Wallet 儲存：

$$
W_t
$$

可用於支援功能的額外抽象資源。

它可能來自：

$$
W_t
=
W_{\mathrm{purchase}}
+
W_{\mathrm{rollover}}
+
W_{\mathrm{reward}}
+
W_{\mathrm{return}}
+
W_{\mathrm{borrow}}
-
W_{\mathrm{used}}
$$

並不要求所有來源都在第一版同時存在。

---

### 4.4 Elastic Overage

當：

$$
Q_{\mathrm{included}}+W_t
$$

不足時，使用者可以選擇：

$$
\text{Stop}
$$

或：

$$
\text{PAYG}
$$

因此超額使用不是默認義務，而是一個可控制的選項。

---

## 5. Compute Wallet 不等於美元錢包

若 Wallet 直接等價於：

$$
1\ \mathrm{USD}=\text{固定數量 token}
$$

會產生一個問題：

模型價格與成本會快速變化。

假設模型 $m$ 的單位成本從：

$$
p_m(t_0)
$$

下降到：

$$
p_m(t_1)
$$

或者新的高階模型價格高於原模型。

如果 Wallet 完全綁定美元，用戶每次都必須理解新的價格表。

因此本文建議分離：

$$
\boxed{
\text{Wallet Unit}
\neq
\text{Settlement Currency}
}
$$

Wallet 可以使用抽象 Compute Credit：

$$
\mathrm{CU}
$$

平台再維持內部映射：

$$
\phi_t:
\text{service usage}
\rightarrow
\mathrm{CU}
$$

例如：

$$
\phi_t(m,x)
=
\text{CU cost of task }x\text{ on model }m
$$

這使產品可以調整模型、路由與成本，而不需要每次都改變使用者的心理帳戶。

---

## 6. Compute Wallet 也不應等於 Token Wallet

Token 是語言模型的重要計量單位，但：

$$
1\text{ token}
\neq
1\text{ unit of economic cost}
$$

因為成本還會受：

$$
\begin{aligned}
C={}&f(
\text{model},
\text{input},
\text{output},
\text{context length},
\text{cache},\\
&\text{reasoning effort},
\text{tool calls},
\text{image},
\text{audio},
\text{agent loops},
\text{latency tier}
)
\end{aligned}
$$

影響。

因此：

$$
\boxed{
\text{Token Accounting}
\subset
\text{Compute Accounting}
}
$$

對 API 開發者而言，Token 定價可以保留。

對一般產品使用者而言，更合理的是看到：

> 本月還有 620 Compute Credits。

而不是：

> 你剩下 17,392,844 input tokens、4,881,221 cached tokens、……

產品可以內部精確，外部簡單。

---

## 7. Membership 與 Compute 必須分離

這是 Compute Wallet 架構中非常重要的一點。

如果所有價值都以 Compute 計價，會忽略很多固定產品成本與非算力價值。

因此：

$$
\boxed{
P_{\mathrm{subscription}}
=
P_{\mathrm{membership}}
+
P_{\mathrm{included\ compute}}
}
$$

Membership 可以涵蓋：

- 帳號與身份；
- 同步與儲存；
- 記憶系統；
- 工作空間；
- 權限管理；
- 隱私與安全；
- 專業 UI；
- Connector；
- Support；
- 團隊協作。

Compute 則處理：

$$
\text{variable inference and execution cost}
$$

這使平台不需要把所有產品功能都強迫轉成按量計費。

---

## 8. 現行市場已經出現混合制雛形

截至 2026 年 9 月，市場已經出現多種混合機制。

OpenAI 個人方案在支援功能上採用：

$$
\text{Included Usage}
\rightarrow
\text{Purchased Credits}
$$

亦即先消耗方案內含量，達到限制後再由 credit balance 支付額外用量。現行個人 credits 已可在部分支援的 Agentic 功能之間共用，但 OpenAI 明確區分這些 credits 與 API credits。

OpenAI Business、Enterprise 與 Edu 則更進一步提供 shared credit pool；個別使用者超過內含上限後，可由 workspace 購買的共同 credits 繼續支援部分高階功能。

Anthropic 的企業與團隊產品則提供「seat included usage＋extra usage」結構，管理員可以允許額外用量並設定 spending caps；Anthropic 將這種 extra usage 與標準 API rates 連接。

Cursor 的現行方案則更接近：

$$
\text{Monthly Subscription}
+
\text{Included Usage Pools}
+
\text{On-Demand API-Rate Usage}
$$

而且允許使用者關閉 on-demand usage 或設定 spend limit。

這些制度共同指向：

$$
\boxed{
\text{Subscription}
+
\text{Usage-Based Extension}
}
$$

正在成為 AI 產品的重要商業模式。

---

## 9. 但現在的混合制仍然是「單向的」

現行主流制度大多解決：

$$
\text{Included Usage Exhausted}
\rightarrow
\text{Buy More}
$$

即：

$$
Q\rightarrow 0
\Rightarrow
W_{\mathrm{purchase}}>0
$$

但通常沒有處理：

$$
Q_{\mathrm{unused}}>0
$$

時該怎麼辦。

因此目前的 Wallet 多數仍是：

$$
\boxed{
\text{one-way top-up system}
}
$$

而不是完整資源帳本。

更成熟的制度可能逐步加入：

$$
\text{Rollover}
$$

$$
\text{Borrow}
$$

$$
\text{Reward}
$$

$$
\text{Surrender}
$$

使 Wallet 從「超額付費工具」演變成「算力權利協調層」。

---

## 10. Rollover：避免曆法性價值蒸發

若月底未使用額度全部失效：

$$
Q_{\mathrm{unused}}(t)
\rightarrow 0
$$

使用者可能產生：

$$
\text{expiration-induced consumption}
$$

因此可以設計有限 rollover：

$$
Q_{t+1}
=
Q_{\mathrm{base}}
+
\min(
\alpha Q_{\mathrm{unused},t},
R_{\max}
)
$$

其中：

$$
0\leq\alpha\leq1
$$

且 $R_{\max}$ 是最大可累積量。

這避免無限囤積，同時降低「不用就浪費」的心理。

例如：

$$
\alpha=0.5
$$

代表最多將一半未使用額度轉入下一期。

---

## 11. Borrow：讓未來額度支援當下專案

工作需求可能高度不均勻。

假設本月突然出現大型專案：

$$
Q_t^{\mathrm{need}}
>
Q_t^{\mathrm{available}}
$$

但使用者下月預期低使用。

可以允許：

$$
B_t
\leq
\beta Q_{t+1}
$$

其中 $B_t$ 是借用量， $\beta$ 是最大可借比例。

下一期：

$$
Q_{t+1}^{\mathrm{available}}
=
Q_{t+1}^{\mathrm{base}}
-
B_t
$$

這相當於：

$$
\boxed{
\text{intertemporal compute allocation}
}
$$

而不是要求使用者立刻升級整個月的更高方案。

Borrow 對短期專案型工作尤其合理。

---

## 12. Overage：彈性不能等於帳單失控

混合制最大的風險之一，是：

$$
\text{Billing Anxiety}
$$

如果使用者不知道一次操作到底會花多少，就會從「額度焦慮」變成「帳單焦慮」。

因此 Elastic Overage 至少需要四個控制。

### 12.1 Explicit Opt-In

超額使用不應悄悄開啟。

$$
O_{\mathrm{enabled}}\in\{0,1\}
$$

由使用者明確選擇。

### 12.2 Hard Spend Cap

設定：

$$
P_{\mathrm{overage}}
\leq
P_{\max}
$$

### 12.3 Usage Forecast

執行大型任務前顯示：

$$
\hat C(J_i)
$$

例如：

> 預估消耗約 40–70 CU。

### 12.4 Threshold Warning

在：

$$
25\%,50\%,75\%,90\%,100\%
$$

等門檻提供提醒。

因此：

$$
\boxed{
\text{Flexibility}
+
\text{Predictability}
}
$$

必須一起設計。

Cursor 現行 on-demand usage、可關閉超額使用與 spend limit 的設計，正好說明這類保護機制具有實際產品需求。

---

## 13. 跨功能資源池

真正的 Compute Wallet 不應只服務單一功能。

假設使用者擁有：

$$
W=1000\ \mathrm{CU}
$$

可以由：

$$
\mathcal{F}
=
\{
\text{Chat},
\text{Code},
\text{Research},
\text{Image},
\text{Voice},
\text{Agent}
\}
$$

共同消耗。

則：

$$
W_{t+1}
=
W_t
-
\sum_{f\in\mathcal{F}}C_f
$$

這使使用者可以自行表達價值偏好。

某人可能：

$$
C_{\mathrm{code}}\gg C_{\mathrm{image}}
$$

另一人則相反。

平台不需要為每個人預測固定產品組合。

---

## 14. 但不是所有資源都應強迫共池

跨功能共池也有邊界。

某些功能的成本結構與供應瓶頸可能完全不同，例如：

$$
C_{\mathrm{video}}
\gg
C_{\mathrm{text}}
$$

或者某種服務依賴獨立硬體與授權。

因此可以使用：

$$
W
=
W_{\mathrm{general}}
+
W_{\mathrm{specialized}}
$$

其中：

$$
W_{\mathrm{general}}
$$

支援大多數功能，

而：

$$
W_{\mathrm{specialized}}
$$

用於昂貴或受限服務。

這比完全割裂與完全共池更具有實務彈性。

---

## 15. 訂閱與 API 是否應共用 Wallet

這是最敏感但也最重要的制度問題之一。

現行市場通常區分：

$$
W_{\mathrm{product}}
$$

與：

$$
W_{\mathrm{API}}
$$

這有合理原因：

- API 可以被自動化；
- API 有更高 burst potential；
- API 可能被嵌入商業產品；
- API 的安全、責任與計價模式不同；
- 訂閱通常假設單一人類使用者。

因此不宜簡單宣布：

$$
W_{\mathrm{product}}
=
W_{\mathrm{API}}
$$

更合理的設計是引入轉換率：

$$
W_{\mathrm{API}}
=
\kappa W_{\mathrm{product}}
$$

其中：

$$
0<\kappa\leq1
$$

並受到：

$$
R_{\mathrm{API}}
$$

與 API policy 約束。

例如：

$$
100\ \mathrm{Product\ CU}
\rightarrow
60\ \mathrm{API\ CU}
$$

這種 haircut 可以降低：

$$
\text{Subscription}
\rightarrow
\text{API Resale}
$$

套利。

因此：

$$
\boxed{
\text{fungibility}
\neq
\text{1:1 convertibility}
}
$$

---

## 16. Compute Wallet 與「訂閱轉 API」的制度差異

非官方中轉的典型結構是：

$$
\text{Consumer Subscription}
\rightarrow
\text{Unofficial Gateway}
\rightarrow
\text{External API Users}
$$

而官方 Wallet 架構則是：

$$
\text{Subscription Entitlement}
\rightarrow
\text{Provider-Controlled Conversion}
\rightarrow
\text{Authorized Interface}
$$

兩者的核心差異在於：

$$
\text{identity}
$$

$$
\text{authorization}
$$

$$
\text{pricing}
$$

$$
\text{rate control}
$$

$$
\text{resale rights}
$$

是否仍由供應商掌握。

因此，Compute Wallet 的目標不是替非官方套利合法化，而是：

> 把其中真正存在的使用者需求——跨介面彈性——轉化成官方可以控制的產品能力。

---

## 17. Dynamic Exchange Rate

不同模型與功能成本持續變化，因此 Wallet 需要動態換算。

定義：

$$
\phi(m,f,t,p)
$$

為某時刻模型 $m$ 、功能 $f$ 、優先級 $p$ 的 CU 換算函數。

則任務 $J$ 的扣款：

$$
C_{\mathrm{CU}}(J)
=
\phi(m,f,t,p)\cdot q(J)
$$

平台可以依：

$$
\text{Model Cost}
$$

$$
\text{Capacity}
$$

$$
\text{Latency}
$$

$$
\text{Energy}
$$

$$
\text{Demand}
$$

調整 $\phi$。

但這產生透明度問題。

因此所有動態匯率都應滿足：

$$
\boxed{
\text{ex ante visibility}
}
$$

也就是使用者在任務執行前能看到預估，而不是事後才知道扣了多少。

---

## 18. Price Abstraction 與 Cost Transparency 並不矛盾

看似矛盾的兩個要求其實可以同時存在：

第一：

> 一般使用者不想理解每個 Token 的價格。

第二：

> 使用者又希望知道自己還剩多少、這個任務大概多貴。

因此需要：

$$
\boxed{
\text{Abstract Price}
+
\text{Transparent Consumption}
}
$$

例如 UI 只需要顯示：

> 本月內含：780 CU  
> Wallet：240 CU  
> 此任務預估：35 CU  
> 低峰執行：24 CU  
> 超額付費：關閉

這比直接展示複雜 API rate card 更符合完整產品體驗。

---

## 19. 使用者會根據價格改變策略

Compute Wallet 不能假設使用者行為固定。

令需求：

$$
D
=
D(P,M,Q,F,T)
$$

其中：

- $P$：價格；
- $M$：模型能力；
- $Q$：剩餘額度；
- $F$：功能；
- $T$：時間與 deadline。

當：

$$
P\downarrow
$$

或：

$$
Q_{\mathrm{available}}\uparrow
$$

使用者可能將原本單次推理改成：

$$
\text{Generate}
\rightarrow
\text{Critique}
\rightarrow
\text{Verify}
\rightarrow
\text{Regenerate}
$$

甚至啟動多 Agent：

$$
N_{\mathrm{calls}}\uparrow\uparrow
$$

所以產品定價不是被動記帳，而是：

$$
\boxed{
\text{behavior-shaping mechanism}
}
$$

這也是後續 Demand Engineering 的基礎。

---

## 20. Compute Wallet 可以成為需求感測器

若 Wallet 清楚記錄：

$$
q_i(t,m,f,p)
$$

平台可以觀察：

- 使用者何時消耗；
- 哪些功能消耗最多；
- 哪些模型具有最高替代性；
- 什麼價格下使用者會切換；
- 哪些任務願意延遲；
- 哪些使用者需要短期 burst；
- 哪些方案長期存在大量 unused entitlement。

因此：

$$
\text{Wallet Telemetry}
\rightarrow
\text{Demand Model}
$$

企業可以進一步估計：

$$
\hat D(t+\tau)
$$

這些資料會直接支援後續：

$$
\text{Off-Peak Discount}
$$

$$
\text{Capacity Planning}
$$

$$
\text{Model Routing}
$$

與：

$$
\text{Investment Planning}
$$

---

## 21. 企業版：Organization Compute Wallet

對企業而言，個人 Wallet 可以提升為：

$$
W_{\mathrm{org}}
$$

其中所有 seat 的使用可以先消耗個人 included allocation，再由共同池支援。

定義：

$$
W_{\mathrm{org}}
=
\sum_i W_i
+
W_{\mathrm{shared}}
$$

並加入：

$$
L_i
$$

作為每名員工的 spend limit。

因此：

$$
q_i\leq L_i
$$

企業管理員可以：

- 設定部門額度；
- 設定個人 hard cap；
- 允許特定專案 burst；
- 觀察 usage analytics；
- 將未使用額度重新分配；
- 預留高優先級資源。

OpenAI 現行 shared credit pool 與 Anthropic 的 admin-controlled extra usage 已經是這種制度的早期形式。

---

## 22. Wallet 的七種資源流

完整 Compute Wallet 最終可能有七種基本操作：

$$
\boxed{
\mathcal{O}
=
\{
\text{Earn},
\text{Consume},
\text{Purchase},
\text{Rollover},
\text{Borrow},
\text{Convert},
\text{Surrender}
\}
}
$$

其中：

### Earn

方案每期自動獲得 included allocation。

### Consume

使用 AI 功能扣除 CU。

### Purchase

額外購買。

### Rollover

將部分未用額度移至未來。

### Borrow

從未來週期提前取得部分額度。

### Convert

在不同資源池或介面間換算。

### Surrender

主動放棄某些未來使用權，換取 credit、折抵或其他補償。

前六項構成本文主要制度。

第七項將在下一篇進一步討論。

---

## 23. Wallet Conservation 與非守恆

Compute Wallet 看起來像貨幣，但它不必是完全守恆的。

如果：

$$
W_A\rightarrow W_B
$$

平台可以設定：

$$
W_B=\alpha W_A
$$

其中：

$$
0<\alpha\leq1
$$

差額：

$$
(1-\alpha)W_A
$$

可以被視為：

- 轉換成本；
- 不同產品成本差；
- 反套利 haircut；
- 容量風險費；
- 時間價值調整。

因此 Wallet 更接近：

$$
\text{programmable service entitlement}
$$

而不是法定貨幣。

這也是為什麼不宜直接稱為「Token 資產」。

---

## 24. 一個完整的消費者方案範例

假設某 AI Pro Hybrid 方案為：

$$
P_{\mathrm{month}}=200\ \mathrm{USD}
$$

包含：

$$
Q_{\mathrm{included}}=1000\ \mathrm{CU}
$$

其中：

$$
F_T=0.8
$$

允許：

$$
R_{\mathrm{rollover}}=300\ \mathrm{CU}
$$

最大 Borrow：

$$
B_{\max}=200\ \mathrm{CU}
$$

額外 Wallet 可自行購買。

使用者介面只有：

**本月內含額度**

$$
640\ \mathrm{CU}
$$

**上月保留**

$$
120\ \mathrm{CU}
$$

**已購買 Wallet**

$$
80\ \mathrm{CU}
$$

因此：

$$
W_{\mathrm{available}}
=
840\ \mathrm{CU}
$$

如果今天要跑大型 Agent：

> 即時執行：120 CU  
> 今天完成：95 CU  
> 離峰完成：70 CU

使用者不需要知道底層到底是幾百萬 Token、多少 GPU-seconds 或多少瓦時。

這就是 Price Abstraction 的價值。

---

## 25. 一個企業方案範例

假設企業有：

$$
N=100
$$

個 seats。

每 seat 包含：

$$
q=500\ \mathrm{CU}
$$

則：

$$
Q_{\mathrm{base}}=50,000\ \mathrm{CU}
$$

企業另外購買：

$$
W_{\mathrm{shared}}=20,000\ \mathrm{CU}
$$

各部門可設定：

$$
L_{\mathrm{engineering}}=30,000
$$

$$
L_{\mathrm{research}}=20,000
$$

$$
L_{\mathrm{operations}}=10,000
$$

剩餘：

$$
10,000
$$

作為彈性池。

如果工程部某週突然需要大量 Agent：

$$
q_{\mathrm{engineering}}\uparrow
$$

就從 shared pool 取得，而不必立即替所有員工升級方案。

這比：

$$
\text{every user buys highest tier}
$$

更有效率。

---

## 26. 與傳統 SaaS 的差異

傳統 SaaS 常見：

$$
P
=
N_{\mathrm{seat}}\cdot P_{\mathrm{seat}}
$$

因為一名使用者登入 CRM 或文件工具，不一定產生巨大邊際算力成本。

AI 不同。

其變動成本可能隨使用量顯著增加：

$$
\frac{\partial C}{\partial q}>0
$$

而 Agent 化後：

$$
q_{\mathrm{agent}}
\gg
q_{\mathrm{chat}}
$$

因此純 seat pricing 容易產生：

$$
\text{Revenue}
\not\propto
\text{Compute Cost}
$$

Compute Wallet 則可以保留 SaaS 的 Membership：

$$
P_{\mathrm{membership}}
$$

同時把高度變動的推理成本：

$$
C_{\mathrm{variable}}
$$

獨立處理。

---

## 27. 與純雲端計價的差異

但 AI 產品也不能完全照抄 AWS 或 Azure。

雲端客戶通常願意理解：

- vCPU；
- GB RAM；
- GPU-hours；
- region；
- provisioned throughput。

一般 AI 使用者並不希望管理這些變數。

因此：

$$
\boxed{
\text{internal economic sophistication}
\neq
\text{external UI complexity}
}
$$

平台內部可以是一個高度複雜的容量市場。

使用者外部仍然只需要：

> 現在跑、晚點跑、剩多少、要不要多花。

這是 Compute Wallet 與雲端帳單最重要的產品差異。

---

## 28. 可測試假說

### H1：混合制能提高高變異使用者的留存

對：

$$
\mathrm{Var}[q_i(t)]\gg0
$$

的使用者，預期：

$$
\text{Retention}_{\mathrm{hybrid}}
>
\text{Retention}_{\mathrm{fixed}}
$$

---

### H2：Spend Cap 可以降低 PAYG 的價格焦慮

若：

$$
P_{\max}
$$

由使用者預先設定，則超額使用意願可能提高，而帳單爭議下降。

---

### H3：Rollover 會降低 expiration-induced consumption

預期：

$$
Q_{\mathrm{waste}}\downarrow
$$

且：

$$
Q_{\mathrm{artificial}}\downarrow
$$

---

### H4：Borrow 對專案型使用者的價值高於平均型使用者

當：

$$
\mathrm{BCR}_i
$$

較高時，Borrow 的效用應更高。

---

### H5：跨功能 Wallet 會提高功能替代效率

使用者可將低價值功能的未使用額度轉向高價值功能：

$$
V_{\mathrm{total}}\uparrow
$$

---

### H6：完全 1:1 API 轉換會增加套利風險

若：

$$
\kappa=1
$$

且訂閱有效單價低於 API：

$$
P_{\mathrm{sub,eff}}<P_{\mathrm{API}}
$$

則：

$$
A_{\mathrm{arbitrage}}\uparrow
$$

因此合理的：

$$
\kappa<1
$$

可能是必要的。

---

## 29. 實驗矩陣

可以比較四種產品。

### Model A：Pure Subscription

$$
P=P_{\mathrm{month}}
$$

固定時間窗。

### Model B：Subscription + Overage

方案內含量用完後：

$$
Q_{\mathrm{extra}}
\rightarrow
\text{PAYG}
$$

### Model C：Subscription + Compute Wallet

加入：

$$
\text{Rollover}
+
\text{Purchase}
+
\text{Cross-Feature Pool}
$$

### Model D：Adaptive Compute Wallet

再加入：

$$
\text{Borrow}
+
\text{Dynamic Exchange}
+
\text{Flexible Scheduling}
$$

比較：

$$
\text{Retention}
$$

$$
\text{ARPU}
$$

$$
\text{Gross Margin}
$$

$$
\text{Peak Load}
$$

$$
\text{Unused Entitlement}
$$

$$
\text{Billing Complaints}
$$

$$
\text{Task Completion}
$$

$$
\text{Cross-Feature Adoption}
$$

即可驗證混合制度是否真正優於單一計價模式。

---

## 30. 制度原則

本文提出八項基本原則。

### 原則一：訂閱不應被消滅

訂閱提供：

$$
\text{Predictability}
+
\text{Price Abstraction}
+
\text{Integrated Product Value}
$$

這些都具有獨立價值。

### 原則二：API 也不應被視為異常高階模式

API 是必要的可程式化 Consumption Interface。

### 原則三：Wallet 位於兩者之間

$$
\boxed{
\text{Subscription}
\leftrightarrow
\text{Compute Wallet}
\leftrightarrow
\text{Usage Interfaces}
}
$$

### 原則四：Wallet Unit 不等於 Token

應建立抽象資源單位。

### 原則五：Wallet Unit 不等於現金

它是可程式化服務權利，而不是貨幣。

### 原則六：所有超額使用都應可預測與可停止

$$
\text{Opt-In}
+
\text{Forecast}
+
\text{Hard Cap}
$$

### 原則七：跨介面 Fungibility 應有轉換規則

$$
\kappa
$$

可以避免不合理套利。

### 原則八：產品複雜度應藏在系統內，而不是丟給使用者

$$
\boxed{
\text{complex backend}
+
\text{simple economic interface}
}
$$

---

## 31. 限制與開放問題

Compute Wallet 仍有多個尚未解決的問題。

第一，CU 如何標準化。

如果模型效率快速改變：

$$
\phi_t
$$

就必須更新。

第二，Wallet 的使用權是否構成可轉讓資產。

本文暫不假定可轉讓。

第三，rollover 是否會造成未來 period 的容量負債。

如果大量使用者累積：

$$
W_{\mathrm{rollover}}
$$

平台可能形成：

$$
\text{latent compute liability}
$$

第四，borrow 會不會造成使用者長期「算力負債」。

第五，跨 API 的轉換如何避免訂閱套利。

第六，是否應允許供應商主動回購或要求使用者 surrender 未來 priority entitlement。

最後一項正是下一篇的核心。

---

## 32. 結論

生成式 AI 的市場正在證明：

$$
\text{Subscription}
$$

與：

$$
\text{Usage-Based Pricing}
$$

並不是互斥制度。

訂閱適合提供：

$$
\text{Predictability}
+
\text{Membership}
+
\text{Integrated Experience}
$$

API 與按量機制則適合提供：

$$
\text{Elasticity}
+
\text{Programmability}
+
\text{Marginal Cost Alignment}
$$

真正值得設計的是兩者之間的中介層。

本文提出：

$$
\boxed{
\text{Compute Wallet}
}
$$

作為這個中介。

其長期形式可以表示為：

$$
\boxed{
\begin{aligned}
\text{AI Plan}={}&
\text{Membership}\\
&+\text{Included Compute}\\
&+\text{Wallet}\\
&+\text{Rollover}\\
&+\text{Borrow}\\
&+\text{Conversion}\\
&+\text{PAYG Overage}\\
&+\text{Throughput Control}
\end{aligned}
}
$$

這不是將 ChatGPT、Claude 或其他 AI 產品變成複雜的雲端帳單。

恰恰相反。

理想的制度應該讓底層：

$$
\text{pricing and capacity coordination}
$$

更加精細，

而讓使用者上層看到的介面更加簡單。

因此，本篇的核心命題可以表述為：

$$
\boxed{
\text{The future AI subscription is not a fixed quota;
it is a membership wrapped around a programmable compute entitlement.}
}
$$

中文即：

**未來的 AI 訂閱不應只是固定額度，而應是一個包覆於產品會員權益之中的可程式化算力使用權。**

而當這個使用權可以被累積、借用、轉換與加購之後，下一個自然問題就是：

> 如果我根本不需要這部分使用權，它能不能被返還、轉讓，甚至由供應商主動買回？

這將把 Compute Wallet 從單純的計價工具，推向真正的雙向 AI 算力市場。

---

## 參考資料

1. OpenAI Help Center. *Using Credits for Flexible Usage in ChatGPT (Personal plans).* Accessed 2026-09-07.
2. OpenAI Help Center. *Flexible pricing for the Enterprise, Edu, and Business plans.* Accessed 2026-09-07.
3. OpenAI Help Center. *ChatGPT Rate Card (Business, Enterprise/Edu credit-based pricing).* Accessed 2026-09-07.
4. Anthropic. *Claude Code and new admin controls for business plans.* 2025-08-20; accessed 2026-09-07.
5. Anthropic Help Center. *How do usage and length limits work?* 2026-07-13; accessed 2026-09-07.
6. Cursor Docs. *Usage-based charges.* Accessed 2026-09-07.
7. Cursor Docs. *Usage and limits.* Accessed 2026-09-07.
8. Cursor Docs. *Models & Pricing.* Accessed 2026-09-07.

---

## Series Navigation

**Paper 1**  
AI 訂閱制的制度錯位：當曆法時間不再等於智能消耗

**Paper 2**  
額度的時間可替代性：月算力、Burst 與集中式工作

**Paper 3 — 本篇**  
訂閱、API 與 Compute Wallet：AI 混合計價制度

**Paper 4 — Next**  
閒置額度、轉讓與供應商回購：AI 使用權的可逆性

**Paper 5**  
從 Rate Limiting 到 Demand Engineering：離峰折扣與 AI 需求響應

**Paper 6**  
算力透明度作為控制介面：從黑箱限流到容量可觀測市場

**Paper 7**  
算力透明度作為投資工具：AI 企業的新基本面

**Paper 8**  
AI 市場的制度演化：從商品化到容量市場

**Extra 1**  
Token 消耗症候群：到期額度如何反向塑造人的認知行為

**Extra 2**  
跨產業制度移植：AI 產業其實不用每件事重新發明
