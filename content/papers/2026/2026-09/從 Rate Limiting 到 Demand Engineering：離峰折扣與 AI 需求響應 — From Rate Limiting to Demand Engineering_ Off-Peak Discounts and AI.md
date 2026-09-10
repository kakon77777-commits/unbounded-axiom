# 從 Rate Limiting 到 Demand Engineering：離峰折扣與 AI 需求響應
## From Rate Limiting to Demand Engineering: Off-Peak Discounts and AI Demand Response

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Paper 5 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

AI 供應商面對算力不足時，最常見的早期制度工具是 Rate Limiting：當需求超過可承受容量時，降低速率、延後重置、排隊、限制高階模型或直接拒絕部分請求。這種方法有效、簡單且容易實作，但其本質是一種 **被動式容量防禦**。它在尖峰已經形成之後才處理問題，並且通常把調度成本主要轉嫁給使用者。

本文提出 **AI Demand Engineering（AI 需求工程）**：供應商不只觀測與限制需求，而是透過離峰折扣、延遲換價、deadline scheduling、可逆 entitlement、priority differentiation 與容量預測，主動改變「需求何時發生」。其目標不是要求使用者少用 AI，而是盡可能把可延遲工作從高負載時段移向低負載時段，使：

$$
\max_t D(t)
$$

下降，即使：

$$
\int D(t)\,dt
$$

保持不變甚至增加。

截至 2026 年 9 月，市場已經出現重要先例。OpenAI Batch API 對可在 24 小時內非同步完成的工作提供相對同步 API 50% 的成本折扣；Fast mode 則對需要更低延遲與更穩定速度的工作收取相對 Standard 更高的價格。OpenAI Reserved Tier 允許企業預購峰值期間可用的 provisioned throughput。Amazon Bedrock 已將推理明確分成 Reserved、Priority、Standard 與 Flex 四個服務層，其中 Flex 以較低價格服務能容忍較長處理時間的工作，而 Priority 則以價格溢價取得更高優先級。Microsoft Foundry 亦區分 Standard、Priority、Provisioned 與 Batch，並允許 provisioned capacity 飽和後 spillover 至 Standard。這些制度共同證明：**推理工作已經開始依時間敏感度、延遲容忍與容量保證進行差異化定價。**

然而，現行市場主要仍是「使用者自行選擇既定 service tier」，尚未普遍進入「供應商依即時或預測容量主動發布折扣期」的階段。本文因此進一步提出 Capacity-Aware Discount、Compute Happy Hour、Deadline Market、Demand Response Offer、Temporal Exchange Rate 與 Load-Shaping Efficiency 等制度元件，並明確區分動態折扣與尖峰漲價。本文主張，對消費型與 Agentic AI 產品而言，**正向誘因式的離峰折扣可能比單純尖峰加價更容易建立使用者信任，同時改善供應商的容量利用率。**

本文的核心命題是：

$$
\boxed{
\text{AI capacity management should evolve from limiting demand to engineering when demand occurs.}
}
$$

亦即：

**AI 容量管理應從「限制需求」演化為「設計需求發生的時間」。**

**關鍵詞：** Demand Engineering、Demand Response、Rate Limiting、Off-Peak Discount、Flex Processing、Batch API、Priority Pricing、AI Capacity、Load Shaping、Agent Scheduling

---

## 1. Rate Limiting 解決的是結果，不是需求形成

假設平台在時刻 $t$ 的有效推理容量為：

$$
C(t)
$$

總需求為：

$$
D(t)
$$

當：

$$
D(t)\leq C(t)
$$

系統可以正常服務。

當：

$$
D(t)>C(t)
$$

傳統方法通常採取：

$$
\text{Rate Limit}
$$

$$
\text{Queue}
$$

$$
\text{Reject}
$$

$$
\text{Model Downgrade}
$$

或：

$$
\text{Temporary Restriction}
$$

使實際服務量：

$$
S(t)\leq C(t)
$$

這確實保護了基礎設施。

但它沒有改變：

$$
D(t)
$$

本身。

因此 Rate Limiting 解決的是：

$$
\boxed{
\text{how much demand is admitted}
}
$$

而不是：

$$
\boxed{
\text{when demand is generated}
}
$$

這正是 Demand Engineering 與傳統限流的根本差異。

---

## 2. 從 Admission Control 到 Demand Shaping

本文將兩種策略區分為：

### Admission Control

$$
D(t)
\rightarrow
S(t)
$$

其中：

$$
S(t)\leq C(t)
$$

平台決定哪些請求可以被服務。

### Demand Shaping

$$
D(t)
\rightarrow
D'(t)
$$

使：

$$
\max_t D'(t)
<
\max_t D(t)
$$

平台透過價格、時間、排程與使用權誘因，讓部分原本會在 $t$ 發生的需求改到：

$$
t+\tau
$$

再執行。

因此：

$$
\boxed{
\text{Rate Limiting}
=
\text{admission problem}
}
$$

而：

$$
\boxed{
\text{Demand Engineering}
=
\text{behavior and scheduling problem}
}
$$

兩者不是互斥。

成熟制度需要兩者同時存在。

---

## 3. AI 工作具有不同的時間彈性

不是所有 AI 任務都需要「現在」。

令任務 $J_i$ 表示為：

$$
J_i
=
(C_i,\ell_i,\delta_i,p_i)
$$

其中：

- $C_i$：預期資源消耗；
- $\ell_i$：可接受延遲；
- $\delta_i$：deadline；
- $p_i$：優先級。

例如：

### 即時對話

$$
\ell_i\approx 1\text{--}5\ \mathrm{s}
$$

### 程式輔助

$$
\ell_i\approx 5\text{--}30\ \mathrm{s}
$$

### 大型研究

$$
\ell_i\approx 10\text{ min}\text{--}2\text{ h}
$$

### Agent overnight job

$$
\ell_i\approx 6\text{--}12\text{ h}
$$

### 批次資料處理

$$
\ell_i\approx 24\text{ h}
$$

若平台把所有任務都放進相同：

$$
\text{immediate queue}
$$

就浪費了大量：

$$
\boxed{
\text{Latency Elasticity}
}
$$

---

## 4. Demand Engineering 的基本目標

平台不是希望：

$$
\int_B D(t)\,dt
$$

越小越好。

因為更多有效 AI 使用通常代表更高產品價值。

真正需要改善的是：

$$
\boxed{
P_D
=
\max_{t\in B} D(t)
}
$$

即 Peak Demand。

同時希望提高：

$$
U_{\mathrm{eff}}
=
\frac{
\int_B S(t)\,dt
}{
\int_B C(t)\,dt
}
$$

也就是有效容量利用率。

因此可將簡化目標寫成：

$$
\min
\left[
\alpha P_D
+
\beta Q_{\mathrm{reject}}
+
\gamma C_{\mathrm{capacity}}
-
\eta V_{\mathrm{served}}
\right]
$$

其中：

- $Q_{\mathrm{reject}}$：被拒需求；
- $C_{\mathrm{capacity}}$：容量成本；
- $V_{\mathrm{served}}$：成功服務所創造的價值。

Demand Engineering 的目的不是節省每一個 Token，而是改善整體供需配置。

---

## 5. 現行市場已經開始對「時間」定價

截至 2026 年 9 月，主要 AI 基礎設施已經證明：

$$
\boxed{
\text{same model output}
\neq
\text{same economic product}
}
$$

如果交付時間、延遲與容量保證不同，價格就可以不同。

### 5.1 OpenAI Batch

OpenAI Batch API 允許非同步提交工作，官方目標是在：

$$
24\text{ h}
$$

內完成。

其價格相對同步 API：

$$
50\%
$$

折扣。

其經濟意義不是「模型變弱」，而是使用者交出了部分：

$$
\text{immediacy right}
$$

換取更低價格。

---

### 5.2 OpenAI Fast mode

OpenAI Fast mode 對延遲敏感工作提供比 Standard 更快且更穩定的處理，並以高於 Standard 的費率計價。

因此：

$$
\text{Latency Requirement}\uparrow
\Rightarrow
\text{Price}\uparrow
$$

這已經形成：

$$
\boxed{
\text{latency-based product differentiation}
}
$$

---

### 5.3 OpenAI Reserved Tier

Reserved Tier 允許企業預購特定模型的 provisioned throughput。

其目標是讓客戶即使在：

$$
\text{peak demand}
$$

期間仍有預先確保的 capacity。

超過 reserved amount 的流量再回到 PAYG。

因此：

$$
\text{Capacity Certainty}
$$

本身已經成為可購買商品。

---

### 5.4 Amazon Bedrock

Amazon Bedrock 將推理分為：

$$
\{
\text{Reserved},
\text{Priority},
\text{Standard},
\text{Flex}
\}
$$

其中：

- Reserved：預留計算容量；
- Priority：支付溢價取得較高優先級；
- Standard：一般推理；
- Flex：可接受較長處理時間，以折扣價格取得推理。

這個結構幾乎已經完整表明：

$$
\boxed{
\text{time sensitivity}
+
\text{capacity guarantee}
\rightarrow
\text{different prices}
}
$$

---

### 5.5 Microsoft Foundry

Microsoft Foundry 同樣區分：

$$
\{
\text{Standard},
\text{Priority},
\text{Provisioned},
\text{Batch}
\}
$$

並提供 spillover：

$$
\text{Provisioned Saturated}
\rightarrow
\text{Standard PAYG}
$$

這顯示成熟 AI 基礎設施不是使用單一容量池，而是允許工作在多個資源層之間流動。

---

## 6. 現在還少了什麼

上述制度已經證明：

$$
\text{Latency}
$$

可以被定價，

$$
\text{Priority}
$$

可以被定價，

$$
\text{Reservation}
$$

可以被定價。

但它們主要仍是：

$$
\boxed{
\text{static menu of service tiers}
}
$$

也就是平台先定義：

> Fast 是多少。  
> Standard 是多少。  
> Flex 是多少。  
> Batch 是多少。

使用者自行選擇。

本文提出下一階段：

$$
\boxed{
\text{capacity-aware dynamic incentive}
}
$$

即平台根據：

$$
L(t)
=
\frac{D(t)}{C(t)}
$$

以及：

$$
\hat L(t+\tau)
$$

主動發布：

$$
\text{Discount Signal}
$$

---

## 7. Compute Happy Hour

最簡單的消費者版本甚至不需要複雜市場。

例如平台預測：

$$
02{:}00\text{--}06{:}00
$$

為低負載。

則發布：

> **Compute Happy Hour**  
> 02:00–06:00 執行的可延遲 Agent 任務只扣 70% CU。

定義離峰折扣：

$$
\delta(t)
\in
[0,1)
$$

原始消耗：

$$
q
$$

實際扣款：

$$
q'
=
(1-\delta(t))q
$$

若：

$$
\delta(t)=0.3
$$

則：

$$
100\ \mathrm{CU}
\rightarrow
70\ \mathrm{CU}
$$

使用者自然會把不急的任務移向該時段。

---

## 8. 使用者不需要凌晨起床

如果折扣制度要求使用者在凌晨手動送出請求，就會製造新的產品摩擦。

因此應允許：

$$
\text{Submit Now}
+
\text{Execute Later}
$$

使用者只需指定：

$$
\delta_i
$$

平台求：

$$
t_i^*
=
\arg\min_{t\leq\delta_i}
\mathrm{Cost}_{\mathrm{system}}(J_i,t)
$$

於是：

$$
\boxed{
\text{Human Submission Time}
\neq
\text{AI Execution Time}
}
$$

Agent 時代尤其適合這種分離。

---

## 9. Deadline Market

比固定 Happy Hour 更進一步，可以讓使用者選擇完成期限。

例如同一任務：

> 現在完成：100 CU  
> 1 小時內：90 CU  
> 今天內：75 CU  
> 明早以前：60 CU

形式化：

$$
P_i
=
P(C_i,\delta_i,L(t))
$$

且一般而言：

$$
\frac{\partial P_i}{\partial \delta_i}<0
$$

也就是 deadline 越寬鬆，價格越低。

這形成：

$$
\boxed{
\text{Deadline Market}
}
$$

使用者出售的是：

$$
\text{temporal flexibility}
$$

供應商取得的是：

$$
\text{scheduling freedom}
$$

---

## 10. 從固定折扣到 Capacity-Aware Discount

離峰折扣可以固定，也可以動態。

定義負載：

$$
L(t)
=
\frac{D(t)}{C(t)}
$$

折扣函數：

$$
\delta(t)
=
f(L(t))
$$

一個簡化例子：

$$
\delta(t)
=
\begin{cases}
0.40,&L(t)<0.40\\
0.25,&0.40\leq L(t)<0.60\\
0.10,&0.60\leq L(t)<0.80\\
0,&L(t)\geq0.80
\end{cases}
$$

這只是示意，不是建議的固定比例。

其重點是：

$$
L(t)\downarrow
\Rightarrow
\delta(t)\uparrow
$$

平台用價格訊號吸引更多可延遲需求進入低負載區間。

---

## 11. 不應只看現在，而應看預測容量

即時負載：

$$
L(t)
$$

只描述當下。

真正有價值的是：

$$
\hat L(t+\tau)
$$

平台可以利用：

- 歷史日週期；
- 工作日／假日；
- 企業批次工作；
- 模型發布；
- 學期與財報週期；
- Agent workload；
- 區域需求；
- 能源供應；
- maintenance window；

預測未來容量。

定義未來剩餘容量：

$$
\hat C_{\mathrm{spare}}(t+\tau)
=
\hat C(t+\tau)-\hat D(t+\tau)
$$

當：

$$
\hat C_{\mathrm{spare}}\uparrow
$$

可以提前發布 discount。

因此：

$$
\boxed{
\text{Demand Engineering}
=
\text{forecast}
+
\text{incentive}
+
\text{scheduling}
}
$$

---

## 12. Forward Demand Shaping

假設平台預測明晚會有大量閒置 capacity。

它不需要等到明晚才降價。

可以現在就發布：

> 明晚 03:00–07:00：Agent workload 35% CU discount。

使用者提前提交。

這叫：

$$
\boxed{
\text{Forward Demand Shaping}
}
$$

其流程為：

$$
\hat D(t+\tau)
\rightarrow
\text{Offer}(t+\tau)
\rightarrow
\text{Reservation}
\rightarrow
D'(t+\tau)
$$

供應商第一次可以主動「填谷」。

---

## 13. Peak Shaving 與 Valley Filling

Demand Engineering 同時包含兩個方向。

### Peak Shaving

$$
D_{\mathrm{peak}}\downarrow
$$

使用：

- surrender；
- delay；
- queue；
- off-peak conversion。

### Valley Filling

$$
D_{\mathrm{valley}}\uparrow
$$

使用：

- discount；
- bonus CU；
- scheduled Agent jobs；
- batch workload；
- low-priority jobs。

理想結果：

$$
\mathrm{Var}[D(t)]\downarrow
$$

也就是需求曲線更平滑。

---

## 14. Load-Shaping Efficiency

本文定義 **Load-Shaping Efficiency**：

$$
LSE
=
\frac{
D_{\mathrm{peak}}-D_{\mathrm{peak}}'
}{
Q_{\mathrm{incentive}}
}
$$

其中：

- $D_{\mathrm{peak}}$：原尖峰；
- $D_{\mathrm{peak}}'$：介入後尖峰；
- $Q_{\mathrm{incentive}}$：為搬移需求所支付的補償成本。

若：

$$
LSE
$$

高，表示少量折扣即可搬移大量 peak demand。

若：

$$
LSE
$$

低，則平台可能不如直接擴 capacity。

---

## 15. Demand Elasticity of Delay

另一個關鍵指標是使用者對延遲折扣的敏感度。

令：

$$
x
$$

為願意延後的需求比例，

$$
r
$$

為折扣率。

定義：

$$
\epsilon_{\mathrm{delay}}
=
\frac{\partial x}{\partial r}
\frac{r}{x}
$$

若：

$$
\epsilon_{\mathrm{delay}}\gg1
$$

代表小幅 discount 就能移動大量需求。

這類 workload 非常適合 Demand Engineering。

若：

$$
\epsilon_{\mathrm{delay}}\approx0
$$

則需求幾乎無法被價格搬移，只能增加即時 capacity。

---

## 16. 不是所有任務都應被折扣誘導

平台應區分：

$$
\mathcal{J}
=
\{
J_{\mathrm{interactive}},
J_{\mathrm{urgent}},
J_{\mathrm{flex}},
J_{\mathrm{batch}},
J_{\mathrm{reserved}}
\}
$$

### Interactive

需要低延遲，不適合等待。

### Urgent

有商業或工作 deadline。

### Flex

可以延後數分鐘至數小時。

### Batch

可以等待較長時間。

### Reserved

已購買容量保證。

Demand Engineering 的主要對象應是：

$$
J_{\mathrm{flex}}
+
J_{\mathrm{batch}}
$$

而不是強迫所有即時對話延後。

---

## 17. Positive Incentive 與 Scarcity Pricing

需求調節可以有兩種基本方向。

### Scarcity Pricing

$$
L(t)\uparrow
\Rightarrow
P(t)\uparrow
$$

尖峰時漲價。

### Positive Incentive

$$
L(t)\downarrow
\Rightarrow
P(t)\downarrow
$$

離峰時折扣。

兩者在理論上都可以改變需求。

但使用者心理不同。

尖峰漲價容易被理解為：

> 供應商算力不足，卻要求我多付錢。

離峰折扣則更接近：

> 如果你願意幫助平台調度，我們分享節省下來的容量價值。

因此本文對消費型 AI 建議：

$$
\boxed{
\text{discount-first demand response}
}
$$

而不是：

$$
\text{surcharge-first}
$$

---

## 18. 但不能假裝原價，再製造假折扣

如果平台為了宣傳「離峰 30% 折扣」，先提高基準價格，則制度會退化成價格操縱。

因此應建立：

$$
P_{\mathrm{baseline}}
$$

並公開：

$$
P_{\mathrm{discounted}}
=
(1-\delta)P_{\mathrm{baseline}}
$$

基準價格在合理期間內應可追蹤。

這是：

$$
\boxed{
\text{reference price integrity}
}
$$

否則 Demand Engineering 會失去信任。

---

## 19. 訂閱制中的折扣不是一定要降現金價格

對訂閱用戶而言，價格訊號可以透過：

$$
\text{CU Consumption Rate}
$$

而不是直接現金。

例如：

### Standard

$$
100\ \mathrm{CU}
$$

### Flex

$$
80\ \mathrm{CU}
$$

### Off-Peak

$$
60\ \mathrm{CU}
$$

使用者月費不變。

但：

$$
\text{effective compute per subscription}
$$

因排程選擇而不同。

這比每個任務都跳出現金價格更符合 subscription experience。

---

## 20. API 與訂閱可以共享同一需求訊號

雖然 API 與產品 Wallet 不必 1:1 共池，但平台可以共享：

$$
L(t)
$$

與：

$$
\hat L(t+\tau)
$$

作為定價與排程訊號。

API 使用者可以選：

$$
\text{Fast}
$$

$$
\text{Standard}
$$

$$
\text{Flex}
$$

$$
\text{Batch}
$$

訂閱使用者看到的則可能只是：

> 現在  
> 今天內  
> 離峰

底層本質相同：

$$
\boxed{
\text{one capacity market, multiple interfaces}
}
$$

---

## 21. Demand Response Offer

Paper 4 提出的 surrender 可以直接與 Demand Engineering 結合。

若預測：

$$
\hat D(t+\tau)>\hat C(t+\tau)
$$

平台可以向使用者發布：

$$
\text{Demand Response Offer}
$$

例如：

> 明晚高負載。  
> 將 100 Priority CU 改為 140 Off-Peak CU？

若使用者接受：

$$
E_{\mathrm{priority}}
\rightarrow
\alpha E_{\mathrm{offpeak}}
$$

則：

$$
D_{\mathrm{peak}}\downarrow
$$

而使用者獲得：

$$
Q_{\mathrm{total}}\uparrow
$$

這是雙方互利的時間交換。

---

## 22. Demand Response 不應等同於強制降級

必須區分：

$$
\text{voluntary flexibility}
$$

與：

$$
\text{forced degradation}
$$

如果平台說：

> 你如果不接受折扣，就不能用原本已購買的服務。

那就不是 demand response。

真正的制度應滿足：

$$
\boxed{
\text{Baseline Service Preserved}
}
$$

也就是：

- 不參與仍保留原權利；
- 折扣完全自願；
- 接受前顯示影響；
- 不使用 misleading UI；
- 不因拒絕而降低未來待遇。

---

## 23. Agent 時代會放大時間市場的重要性

傳統聊天通常具有：

$$
\ell_i\approx0
$$

使用者正在等待回答。

Agent workload 不同。

Agent 可能：

- 跑 30 分鐘；
- 跑 6 小時；
- 夜間整理資料；
- 每日生成報告；
- 批次測試程式；
- 多 Agent 交叉驗證。

因此：

$$
\ell_i
$$

與：

$$
\delta_i
$$

變成自然的任務屬性。

Agent 時代使：

$$
\boxed{
\text{execution time becomes schedulable}
}
$$

這正是 Demand Engineering 能真正發揮的地方。

---

## 24. 使用者甚至可以設定「永遠選最便宜時間」

對完全不急的背景工作，可以提供：

$$
\text{Cheapest Before Deadline}
$$

模式。

例如：

> 每天早上 08:00 前完成新聞摘要，請自動找最低成本時段。

平台求：

$$
t^*
=
\arg\min_{t\leq\delta}
P(t)
$$

這讓使用者不需要觀察容量圖。

而供應商可以在夜間低谷自動填入 workload。

---

## 25. 透明度會強化 Demand Engineering

如果平台只說：

> 現在有 30% 折扣。

使用者不知道原因。

若平台顯示：

> 當前容量：寬鬆  
> 預計 02:00–06:00 為低負載  
> Flex 任務享 30% CU discount

則：

$$
\text{Price Signal}
+
\text{Capacity Signal}
$$

同時存在。

這可能提高：

$$
\text{trust}
$$

以及：

$$
\text{self-scheduling}
$$

因此下一篇將進一步討論：

$$
\boxed{
\text{Capacity Transparency}
}
$$

---

## 26. 但公開資訊也可能造成 Thundering Herd

假設平台公開：

> 現在負載只有 25%。

大量使用者立即啟動大型 Agent。

可能：

$$
L(t):
0.25
\rightarrow
1.20
$$

因此透明度必須搭配：

$$
\text{reservation}
$$

$$
\text{queue}
$$

$$
\text{probabilistic admission}
$$

或：

$$
\text{discount window booking}
$$

使用者應該能：

> 預約低峰 capacity，

而不是所有人一起搶同一秒。

---

## 27. Discount Reservation

平台可以先分配：

$$
Q_{\mathrm{discount},t}
$$

作為特定窗口可接受的折扣 workload。

使用者預約：

$$
r_i
$$

滿足：

$$
\sum_i r_i
\leq
Q_{\mathrm{discount},t}
$$

當預約滿：

$$
\delta(t)\downarrow
$$

或停止接受。

這使折扣本身成為容量預約工具。

---

## 28. 自動折扣市場

更進一步，可以讓平台求解：

$$
\delta^*(t)
$$

使：

$$
D(t,\delta^*(t))
\approx
D_{\mathrm{target}}(t)
$$

也就是折扣率不再由人工固定，而由需求模型決定。

若低谷太深：

$$
\delta^*\uparrow
$$

若已接近目標：

$$
\delta^*\downarrow
$$

形成：

$$
\boxed{
\text{closed-loop demand control}
}
$$

但這種制度必須高度透明，避免不可預測價格。

---

## 29. 價格不應每秒跳動

雖然理論上可以：

$$
P=P(t)
$$

每秒變化，

但這會產生：

$$
\text{Pricing Anxiety}
$$

與：

$$
\text{Gaming Behavior}
$$

因此消費者市場更適合：

$$
\boxed{
\text{discrete pricing windows}
}
$$

例如：

- Normal；
- Low Demand；
- Deep Off-Peak。

每個窗口至少持續一定時間。

API 專業客戶則可以接受更細緻的動態價格。

---

## 30. Demand Engineering 與能源調度

AI 推理不只消耗 GPU。

還消耗：

$$
\text{Electricity}
+
\text{Cooling}
+
\text{Network}
$$

如果某些 workload 具有時間與地理彈性，可以進一步考慮：

$$
E(t,r)
$$

表示區域 $r$ 在時刻 $t$ 的能源成本或條件。

平台可以求：

$$
(t^*,r^*)
=
\arg\min
\left[
\alpha C_{\mathrm{compute}}
+
\beta C_{\mathrm{energy}}
+
\gamma C_{\mathrm{latency}}
\right]
$$

前提是資料治理、隱私與地區限制允許。

這使 Demand Engineering 最終可以連到：

$$
\boxed{
\text{Compute-Energy Co-Scheduling}
}
$$

---

## 31. 全球時區本身就是自然的需求調度資源

全球 AI 平台具有：

$$
D_r(t)
$$

不同區域的需求峰谷不完全同步。

如果模型與資料政策允許跨區路由：

$$
D_{\mathrm{global}}(t)
=
\sum_r D_r(t)
$$

平台可以使用：

$$
\text{global load balancing}
$$

進一步平滑需求。

但這不能假設所有資料都可自由跨境。

因此：

$$
\text{capacity optimization}
$$

必須受：

$$
\text{data residency}
+
\text{privacy}
+
\text{jurisdiction}
$$

約束。

---

## 32. 供應商不應只觀察 Token

如果平台只用：

$$
\text{Tokens per Minute}
$$

理解負載，可能低估不同 workload 的差異。

更完整的需求狀態應為：

$$
D(t)
=
f(
T_{\mathrm{in}},
T_{\mathrm{out}},
R_{\mathrm{reasoning}},
A_{\mathrm{agent}},
M_{\mathrm{memory}},
I_{\mathrm{image}},
V_{\mathrm{video}},
X_{\mathrm{tools}}
)
$$

因此 Demand Engineering 最終需要：

$$
\boxed{
\text{Normalized Effective Compute}
}
$$

而不是只看 raw token count。

---

## 33. 從「大家少用」轉成「大家用得更適時」

這套方法最重要的價值觀不是：

$$
\text{Demand Reduction}
$$

而是：

$$
\boxed{
\text{Demand Re-Timing}
}
$$

如果原本：

$$
\int_B D(t)\,dt
=
Q
$$

調度後仍然：

$$
\int_B D'(t)\,dt
=
Q
$$

但：

$$
\max_t D'(t)
<
\max_t D(t)
$$

平台就可能在不降低總 AI 使用價值的前提下改善容量壓力。

這比單純鼓勵「少用」更符合 AI 產業成長。

---

## 34. 企業端的經濟價值

假設為了滿足尖峰，平台需要容量：

$$
C_{\mathrm{peak}}
$$

但平均需求只有：

$$
D_{\mathrm{avg}}
$$

其 Peak-to-Average Ratio 為：

$$
PAR
=
\frac{
D_{\mathrm{peak}}
}{
D_{\mathrm{avg}}
}
$$

若 Demand Engineering 使：

$$
PAR\downarrow
$$

企業可能：

- 延後部分 GPU 採購；
- 提高已有 GPU 利用率；
- 減少 idle reserve；
- 改善電力合約；
- 降低高峰期 emergency capacity；
- 提高服務穩定性。

因此，即使總 inference 成長：

$$
Q\uparrow
$$

單位 capacity 的經濟效率仍可能改善。

---

## 35. Demand Engineering 也可以增加營收

離峰折扣不必然降低營收。

如果原本低谷 capacity：

$$
C(t)-D(t)
$$

會閒置，

其短期邊際機會成本可能很低。

若折扣吸引：

$$
\Delta D(t)>0
$$

只要：

$$
P_{\mathrm{discount}}
>
MC_{\mathrm{incremental}}
$$

就可能增加 contribution margin。

因此：

$$
\boxed{
\text{discount}
\not\Rightarrow
\text{revenue loss}
}
$$

尤其在不可儲存的即時 capacity 上，低峰空置本身就是損失。

---

## 36. 但 AI 算力不是航空座位的完全同構

類比航空或電力很有用，但不能過度。

AI capacity 可以透過：

- batching；
- model routing；
- quantization；
- caching；
- region routing；
- new hardware；

快速改變有效供給。

因此：

$$
C(t)
$$

比一班已起飛飛機的座位更有彈性。

同時 AI 需求也可能因模型能力提升迅速擴張。

所以制度設計必須視 AI 市場為：

$$
\boxed{
\text{dynamic supply}
+
\text{dynamic demand}
}
$$

而不是固定容量市場。

---

## 37. Rebound Effect

折扣也可能造成：

$$
D_{\mathrm{total}}\uparrow
$$

例如使用者原本只跑：

$$
1
$$

個 Agent。

因離峰成本下降，改成：

$$
5
$$

個 Agent 平行驗證。

因此：

$$
\delta\uparrow
\Rightarrow
Q_{\mathrm{total}}\uparrow
$$

可能發生。

這並不表示折扣失敗。

真正要看：

$$
D_{\mathrm{peak}}
$$

$$
U_{\mathrm{eff}}
$$

$$
\text{Gross Margin}
$$

與：

$$
\text{Task Value}
$$

是否改善。

---

## 38. 可測試假說

### H1：離峰折扣可以降低 Peak-to-Average Ratio

預期：

$$
\delta_{\mathrm{offpeak}}\uparrow
\Rightarrow
PAR\downarrow
$$

在具有足夠延遲彈性的 workload 中成立。

---

### H2：Deadline pricing 比固定時間窗折扣更有效率

因為：

$$
\delta_i
$$

直接表達使用者真正的時間彈性。

---

### H3：非現金 CU discount 對訂閱用戶具有足夠誘因

即使：

$$
P_{\mathrm{month}}
$$

不變，

降低：

$$
CU_{\mathrm{charged}}
$$

也可能顯著改變排程。

---

### H4：Agent workload 的 delay elasticity 高於即時聊天

預期：

$$
\epsilon_{\mathrm{delay,agent}}
>
\epsilon_{\mathrm{delay,chat}}
$$

---

### H5：透明的容量訊號會提高折扣參與率

如果使用者理解：

> 為什麼有折扣，

可能比只看到隨機折扣更願意調整需求。

---

### H6：過度頻繁的動態價格會降低信任

當：

$$
\mathrm{Var}[P(t)]\uparrow
$$

且可預測性下降，

可能：

$$
\text{Trust}\downarrow
$$

因此需要 pricing windows。

---

## 39. 實驗設計

可將使用者或 workload 分為五組。

### Group A：Rate Limit Only

傳統固定限制。

### Group B：Static Off-Peak Discount

固定離峰窗口。

### Group C：Capacity-Aware Discount

折扣依預測 load 調整。

### Group D：Deadline Scheduling

使用者只指定 deadline。

### Group E：Deadline + Surrender + Wallet

整合：

$$
\text{Temporal Fungibility}
+
\text{Compute Wallet}
+
\text{Demand Response}
$$

比較：

$$
PAR
$$

$$
D_{\mathrm{peak}}
$$

$$
Q_{\mathrm{served}}
$$

$$
Q_{\mathrm{rejected}}
$$

$$
\text{Gross Margin}
$$

$$
\text{User Satisfaction}
$$

$$
\text{Scheduling Acceptance}
$$

$$
LSE
$$

即可驗證 Demand Engineering 的實際效果。

---

## 40. 一個消費型產品範例

使用者提交：

> 幫我完成大型程式碼庫分析。

介面顯示：

**立即完成**

$$
120\ \mathrm{CU}
$$

預估：

$$
20\text{--}35\ \mathrm{min}
$$

**今天內完成**

$$
90\ \mathrm{CU}
$$

**明早以前完成**

$$
65\ \mathrm{CU}
$$

**自動等待最低負載**

$$
55\text{--}75\ \mathrm{CU}
$$

使用者選：

> 明早以前。

之後平台自行排程。

這種產品並不要求使用者理解：

$$
GPU
$$

$$
TPM
$$

$$
PTU
$$

或：

$$
\lambda(t)
$$

只需要表達：

> 我多急？

---

## 41. 一個企業 API 範例

企業 workload 可以明確標示：

$$
J_i
=
(C_i,\delta_i,S_i)
$$

API 可選：

$$
\text{fast}
$$

$$
\text{default}
$$

$$
\text{flex}
$$

或者：

$$
\text{batch}
$$

企業也可以設定策略：

> customer-facing requests → fast  
> normal production → default  
> nightly evaluation → flex  
> data backfill → batch

這已經非常接近今天 AWS、OpenAI 與 Azure 各自提供的 service-tier 結構。

本文的新增部分是讓：

$$
\text{tier selection}
$$

進一步由：

$$
\hat L(t)
$$

與 deadline 自動決定。

---

## 42. 從靜態方案到自適應市場

市場可以分成四個成熟階段。

### Stage 1：Hard Limits

$$
D>C
\Rightarrow
\text{Reject}
$$

### Stage 2：Static Tiers

$$
\text{Fast / Standard / Flex / Batch}
$$

### Stage 3：Dynamic Discounts

$$
\delta=\delta(L,\hat L)
$$

### Stage 4：Adaptive Demand Market

$$
\text{Price}
+
\text{Deadline}
+
\text{Surrender}
+
\text{Reservation}
$$

共同決定：

$$
t_i^*
$$

目前 AI 基礎設施已明顯進入 Stage 2。

本文提出的主要實驗空間則位於 Stage 3 與 Stage 4。

---

## 43. 基本原則

本文提出十項原則。

### 原則一：Rate Limit 仍然需要，但不應是唯一工具

$$
\text{Demand Engineering}
\supset
\text{Rate Limiting}
$$

### 原則二：先識別 latency elasticity

不是所有 workload 都可延遲。

### 原則三：對消費市場優先使用折扣而非尖峰懲罰

$$
\text{positive incentive}
>
\text{scarcity penalty}
$$

作為產品設計起點。

### 原則四：使用者不應為了離峰優惠改變睡眠時間

$$
\text{Submit Time}
\neq
\text{Execution Time}
$$

### 原則五：Deadline 應成為 Agent 任務的一等屬性

$$
J_i=(C_i,\ell_i,\delta_i,p_i)
$$

### 原則六：容量預測應提前驅動折扣

$$
\hat L(t+\tau)
\rightarrow
\text{Offer}
$$

### 原則七：折扣窗口應可預測

避免每秒跳價。

### 原則八：不參與 Demand Response 不應降低原有權利

Baseline 必須受保護。

### 原則九：衡量 Peak，而不只衡量 Total Usage

$$
\max_tD(t)
$$

是關鍵企業變數。

### 原則十：最終目標是重新安排需求，而不是抑制 AI 使用

$$
\boxed{
\text{Use more intelligently, not necessarily less.}
}
$$

---

## 44. 限制

第一，本文提出的即時離峰折扣與 Capacity-Aware Discount 並不代表 OpenAI、AWS 或 Microsoft 已普遍提供同樣的消費者即時市場；現有產品主要驗證的是 service-tier differentiation、batch discount、priority premium 與 reserved capacity。

第二，動態折扣可能被使用者或自動化系統 gaming。

第三，容量預測本身可能錯誤。

第四，如果折扣刺激的新需求大於搬移需求，總負載可能上升。

第五，不同區域存在資料 residency 與法律限制，不可為了容量最佳化任意跨境路由。

第六，若 pricing 過於複雜，使用者可能失去價格可預測性。

第七，供應商必須防止將 demand response 變成降低既有服務承諾的藉口。

---

## 45. 結論

AI 算力吃緊不會只靠一種制度解決。

新增 GPU、改進模型效率、擴建資料中心、改善能源供應與 routing 都仍然必要。

但如果市場中存在大量：

$$
\text{delay-tolerant workload}
$$

那麼單純依賴：

$$
\text{Rate Limit}
$$

就是浪費一個可用的控制維度。

現行 OpenAI Batch、Fast、Reserved，Amazon Bedrock Reserved／Priority／Standard／Flex，以及 Microsoft Foundry 的 Standard／Priority／Provisioned／Batch 與 spillover，已經共同證明：

$$
\boxed{
\text{time}
+
\text{latency}
+
\text{capacity certainty}
}
$$

可以被拆成不同經濟商品。

下一步並不是把所有 AI 變成即時股票市場。

而是讓平台開始主動問：

> 哪些工作真的現在就要？

> 哪些可以晚一小時？

> 哪些可以今晚完成？

> 哪些可以換更多額度、但在離峰跑？

一旦這些需求彈性可以被表達，供應商就能從：

$$
\text{Rate Limiting}
$$

走向：

$$
\boxed{
\text{Demand Engineering}
}
$$

其核心不是：

$$
\text{reduce total cognition}
$$

而是：

$$
\boxed{
\text{move computation to the time where it creates the same value at lower system cost}
}
$$

中文即：

**把同樣有價值的計算，移到整體系統成本更低的時間發生。**

因此，本篇的核心命題為：

$$
\boxed{
\text{AI capacity management should evolve from limiting demand to engineering when demand occurs.}
}
$$

而當價格、排程與需求響應開始依賴：

$$
L(t)
$$

與：

$$
\hat L(t+\tau)
$$

下一個問題就變成：

> 使用者到底應不應該看見這些容量狀態？

> 透明會不會反而成為調度工具？

這正是下一篇：

**算力透明度作為控制介面：從黑箱限流到容量可觀測市場。**

---

## 參考資料

1. OpenAI Help Center. *Batch API FAQ.* Updated 2026-09; accessed 2026-09-07.  
   https://help.openai.com/en/articles/9197833-batch-api-faq

2. OpenAI. *Fast mode for API Customers.* Accessed 2026-09-07.  
   https://openai.com/api-fast-mode/

3. OpenAI. *Reserved Tier for API Customers.* Accessed 2026-09-07.  
   https://openai.com/api-reserved-tier/

4. OpenAI API Reference. *Responses — service_tier.* Accessed 2026-09-07.  
   https://developers.openai.com/api/reference/

5. Amazon Web Services. *Service tiers for optimizing performance and cost — Amazon Bedrock.* Accessed 2026-09-07.  
   https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html

6. Microsoft Learn. *Provisioned throughput for Foundry Models.* Accessed 2026-09-07.  
   https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/provisioned-throughput

7. Microsoft Learn. *Manage traffic with spillover for provisioned deployments.* Accessed 2026-09-07.  
   https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/spillover-traffic-management

---

## Series Navigation

**Paper 1**  
AI 訂閱制的制度錯位：當曆法時間不再等於智能消耗

**Paper 2**  
額度的時間可替代性：月算力、Burst 與集中式工作

**Paper 3**  
訂閱、API 與 Compute Wallet：AI 混合計價制度

**Paper 4**  
閒置額度、轉讓與供應商回購：AI 使用權的可逆性

**Paper 5 — 本篇**  
從 Rate Limiting 到 Demand Engineering：離峰折扣與 AI 需求響應

**Paper 6 — Next**  
算力透明度作為控制介面：從黑箱限流到容量可觀測市場

**Paper 7**  
算力透明度作為投資工具：AI 企業的新基本面

**Paper 8**  
AI 市場的制度演化：從商品化到容量市場

**Extra 1**  
Token 消耗症候群：到期額度如何反向塑造人的認知行為

**Extra 2**  
跨產業制度移植：AI 產業其實不用每件事重新發明
