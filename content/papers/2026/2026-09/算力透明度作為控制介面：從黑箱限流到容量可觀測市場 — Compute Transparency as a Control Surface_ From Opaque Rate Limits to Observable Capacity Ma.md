# 算力透明度作為控制介面：從黑箱限流到容量可觀測市場
## Compute Transparency as a Control Surface: From Opaque Rate Limits to Observable Capacity Markets

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Paper 6 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

生成式 AI 服務的容量管理長期以黑箱形式呈現：使用者通常知道自己「可以使用」或「被限制」，卻不知道平台目前究竟處於低負載、正常、繁忙、接近飽和，還是只是受到個人方案、模型、區域或安全政策的限制。這種不透明性可以簡化產品介面，也能避免暴露敏感基礎設施資訊，但同時犧牲了一個重要的經濟與控制維度：**如果使用者不知道容量狀態，就無法主動配合容量調度。**

本文提出 **Compute Transparency as a Control Surface（算力透明度作為控制介面）**。其基本主張不是要求 AI 供應商公開精確 GPU 數量、資料中心拓樸、電力合約或即時物理餘量，而是將足以支持決策的聚合容量訊號轉化為產品介面，使使用者、企業與 Agent 能夠根據負載、預估延遲、折扣、可用 throughput 與未來容量窗口調整工作時序。

成熟雲端市場已經存在重要先例。Amazon EC2 Spot Placement Score 以 1–10 分評估特定 Region 或 Availability Zone 滿足目標 Spot capacity 的可能性，並明確將其定位為容量規劃與區域選擇建議，而不是容量保證。Microsoft Foundry 則允許客戶透過入口網站或 Model Capacities API 查詢特定模型在不同區域與 deployment type 下的可用部署容量。OpenAI 公開 Status Page 亦提供 ChatGPT、API、Codex 等系統的聚合 availability 狀態，但目前這類資訊主要用於事故透明度，而非日常容量市場訊號。

本文因此區分 **Incident Transparency、Quota Transparency、Capacity Transparency、Forecast Transparency 與 Economic Transparency** 五種層級，並提出 Capacity Load Index、Capacity Confidence Score、Forecast Band、Available Scheduling Window、Reservation Signal 與 Disclosure Gradient 等制度元件。本文同時處理透明度的反效果：若大量使用者看到「現在很空」便同時啟動 Agent，可能形成 thundering herd；若供應商公開過多精確基礎設施資料，又可能增加資安、競爭情報與操縱風險。因此，合理制度不是「完全透明」，而是：

$$
\boxed{
\text{decision-useful transparency}
}
$$

亦即只公開足以改善市場決策、但不必要暴露底層敏感資訊的容量訊號。

本文的核心命題為：

$$
\boxed{
\text{Compute transparency is not merely disclosure; it can be a control surface for demand.}
}
$$

亦即：

**算力透明度不只是資訊揭露，它本身可以成為需求調度的控制介面。**

**關鍵詞：** Compute Transparency、Capacity Visibility、Capacity Index、Demand Engineering、Rate Limit、Spot Placement Score、Model Capacity、AI Infrastructure、Thundering Herd、AI 算力市場

---

## 1. 黑箱限流的基本結構

在典型 AI 產品中，使用者經常只能觀察到結果：

$$
Y_i(t)
\in
\{
\text{available},
\text{slow},
\text{queued},
\text{limited},
\text{unavailable}
\}
$$

但無法直接觀察：

$$
D(t)
$$

$$
C(t)
$$

或：

$$
L(t)
=
\frac{D(t)}{C(t)}
$$

因此使用者通常只能在碰到限制之後才知道：

> 現在可能很擠。

這是一種：

$$
\boxed{
\text{post hoc capacity discovery}
}
$$

平台先隱藏容量，

使用者透過錯誤、等待與限流反推容量。

這對簡單聊天產品尚可接受，但在 Agent、研究、程式開發與長程工作逐漸普及後，會開始限制調度效率。

---

## 2. 不透明本身會製造錯誤決策

假設使用者有一個大型任務：

$$
J_i
$$

可以在未來：

$$
6\text{ h}
$$

內任何時間執行。

如果平台完全不提供容量訊號，使用者通常會：

$$
t_{\mathrm{submit}}
=
t_{\mathrm{now}}
$$

因為：

> 既然不知道什麼時候比較適合，那就現在跑。

如果大量使用者都採取相同策略：

$$
D(t_{\mathrm{now}})\uparrow
$$

這會形成一種制度性同步：

$$
\boxed{
\text{information opacity}
\rightarrow
\text{immediate submission bias}
}
$$

即使很多任務其實可以延後。

因此不透明並不是中性狀態。

它本身也會塑造需求。

---

## 3. 透明度為什麼可以成為調度工具

若平台提供：

> 現在：繁忙  
> 兩小時後：預計正常  
> 今晚 03:00–06:00：低負載，Flex 任務 30% CU discount

使用者的選擇集合變成：

$$
A_i
=
\{
\text{now},
\text{later},
\text{off-peak},
\text{reserve}
\}
$$

而不是只有：

$$
A_i
=
\{
\text{submit now},
\text{do not submit}
\}
$$

因此：

$$
\text{Capacity Signal}
\rightarrow
\text{Behavioral Adaptation}
$$

進一步：

$$
D(t)
\rightarrow
D'(t)
$$

這就是透明度的控制功能。

---

## 4. 透明不等於公開所有基礎設施

「公開容量」最容易遭遇的反對是：

> 難道要告訴競爭者我們有幾張 GPU、在哪個資料中心、現在用了多少電？

不需要。

本文區分：

$$
\boxed{
\text{Physical Infrastructure Transparency}
}
$$

與：

$$
\boxed{
\text{Market-Relevant Capacity Transparency}
}
$$

前者可能包含：

- GPU 數量；
- GPU 型號；
- rack topology；
- 資料中心位置；
- 電力容量；
- 網路拓樸；
- 故障域；
- 冗餘策略；
- 供應商合約。

這些資訊可能具有高度商業與安全敏感性。

後者只需要回答：

> 現在好不好用？

> 大概能不能排到？

> 多久後可能比較空？

> 如果願意等待，可以省多少？

這兩者完全不同。

---

## 5. Decision-Useful Transparency

本文提出：

$$
\boxed{
T_D
=
\text{decision-useful transparency}
}
$$

其目的不是最大化：

$$
\text{information disclosed}
$$

而是最大化：

$$
\text{decision quality}
$$

在給定資訊揭露成本 $C_I$ 與決策改善 $V_D$ 下，可以表示為：

$$
T_D^*
=
\arg\max_T
\left[
V_D(T)-C_I(T)
\right]
$$

其中資訊揭露成本可能包括：

- 競爭情報；
- 資安；
- 市場操縱；
- 使用者誤解；
- thundering herd；
- 法律與監管成本。

因此最優透明度通常：

$$
0<T_D^*<1
$$

既不是完全黑箱，也不是完全公開。

---

## 6. 五種透明度

本文將 AI 容量透明度分為五層。

### 6.1 Incident Transparency

回答：

> 系統有沒有故障？

例如：

$$
\text{Operational}
$$

$$
\text{Degraded}
$$

$$
\text{Outage}
$$

---

### 6.2 Quota Transparency

回答：

> 我個人的方案還剩多少？

例如：

$$
Q_i^{\mathrm{remaining}}
$$

或：

$$
R_i^{\mathrm{limit}}
$$

---

### 6.3 Capacity Transparency

回答：

> 平台現在大概有多擠？

例如：

$$
L(t)
$$

的區間化表示。

---

### 6.4 Forecast Transparency

回答：

> 未來哪些時間可能比較空？

即：

$$
\hat L(t+\tau)
$$

---

### 6.5 Economic Transparency

回答：

> 不同容量狀態如何改變價格、CU 消耗或等待時間？

例如：

$$
\delta(t)
$$

$$
P(t)
$$

或：

$$
E[\text{latency}\mid L(t)]
$$

這五層可以逐步部署，不必一次全部公開。

---

## 7. 現況：事故透明度已經相對成熟

OpenAI 現行 Status Page 將：

- APIs；
- ChatGPT；
- Codex；
- 其他系統；

以聚合方式報告 operational status。

官方亦明確說明，availability metrics 是跨 tier、模型與錯誤類型的聚合資料，單一使用者實際 availability 可能因方案、模型與功能而不同。

這種制度已經證明：

$$
\boxed{
\text{aggregate operational transparency}
}
$$

是可以公開的。

但它主要回答：

> 有沒有壞？

而不是：

> 現在是不是低負載？

因此：

$$
\text{Incident Transparency}
\neq
\text{Capacity Market Transparency}
$$

---

## 8. AWS Spot Placement Score：公開機率，而不是公開機房

Amazon EC2 Spot 提供 Spot Placement Score。

使用者輸入：

$$
\text{Target Capacity}
$$

與 compute requirements，

AWS 回傳不同：

$$
\text{Region}
$$

或：

$$
\text{Availability Zone}
$$

的分數：

$$
S_{\mathrm{spot}}
\in
\{1,2,\ldots,10\}
$$

其中較高分數代表該位置更可能滿足指定 Spot capacity。

重點是：

AWS 並沒有告訴客戶：

> 這個資料中心還剩 8,423 張某型 GPU。

而是提供：

$$
\boxed{
\text{capacity likelihood signal}
}
$$

這正是 Decision-Useful Transparency 的典型案例。

---

## 9. Score 而不是 Raw Capacity

AWS 的做法揭示一個重要設計原則：

$$
\boxed{
\text{normalized score}
>
\text{raw infrastructure count}
}
$$

在多租戶、動態供需系統中，精確 raw number 可能：

- 很快過時；
- 容易被誤解；
- 暴露競爭資訊；
- 無法直接代表成功機率。

因此 AI 模型也可以顯示：

$$
CI_m(t)
\in
[0,100]
$$

其中：

$$
CI_m(t)
$$

是某模型的 Capacity Index。

例如：

> Sol Capacity Index：82 / 100 — Normal

而不是：

> 剩餘 GPU：12,743。

---

## 10. Azure：直接提供模型容量 API

Microsoft Foundry 的現行 quota 管理更進一步。

它明確區分：

$$
\text{Usages API}
$$

與：

$$
\text{Model Capacities API}
$$

前者回答：

> 我的 quota 用掉多少？

後者回答：

> 某模型在各區域還有多少可部署 capacity？

Model Capacities API 可以按：

- model；
- model version；
- region；
- deployment type；

回傳：

$$
\text{availableCapacity}
$$

這表示：

$$
\boxed{
\text{capacity state can be exposed programmatically}
}
$$

並由客戶自行進行部署決策。

這已經非常接近本文主張的「容量可觀測市場」。

---

## 11. 從企業雲端走向消費 AI

企業雲端客戶願意閱讀：

- quota；
- TPM；
- deployment type；
- region；
- capacity unit。

一般 ChatGPT 或 Claude 使用者不應被迫理解這些概念。

因此消費端需要建立：

$$
\phi:
\text{raw capacity state}
\rightarrow
\text{human-readable signal}
$$

例如：

$$
\phi(L)
=
\begin{cases}
\text{Very Low Demand},&L<0.35\\
\text{Normal},&0.35\leq L<0.70\\
\text{Busy},&0.70\leq L<0.90\\
\text{Peak},&0.90\leq L<1.00\\
\text{Over Capacity},&L\geq1
\end{cases}
$$

這就是產品抽象。

---

## 12. Capacity Load Index

本文定義：

$$
\boxed{
CLI_m(t)
=
\frac{
D_m^{\mathrm{eff}}(t)
}{
C_m^{\mathrm{eff}}(t)
}
}
$$

其中：

- $D_m^{\mathrm{eff}}(t)$：模型 $m$ 的有效需求；
- $C_m^{\mathrm{eff}}(t)$：模型 $m$ 的有效容量。

使用：

$$
\text{effective}
$$

而不是 raw token，

因為不同 workload 成本不同。

例如：

$$
1\text{ M tokens of simple text}
$$

與：

$$
1\text{ M tokens of deep reasoning}
$$

不一定具有相同物理成本。

---

## 13. 不應公開虛假的精確度

如果平台其實只能可靠判斷：

$$
CLI\in[0.6,0.75]
$$

卻顯示：

> 當前負載 67.3812%

會製造：

$$
\boxed{
\text{false precision}
}
$$

因此更合理的是：

> Normal：60–75%

或單純：

> Normal

加：

> Confidence：High

這比虛假的精確數字更可信。

---

## 14. Capacity Confidence Score

容量訊號本身也有不確定性。

定義：

$$
CCS(t)
\in
[0,1]
$$

表示平台對容量估計的信心。

例如：

> 預計 03:00–06:00 為低負載  
> Forecast Confidence：82%

如果突發事件很多：

$$
CCS\downarrow
$$

使用者就知道預測不是承諾。

這與 AWS Spot Placement Score 明確不保證 capacity 的邏輯一致。

---

## 15. Forecast Band

平台可以公開：

$$
\hat L(t+\tau)
$$

但不應假裝預測完全準確。

因此可以顯示區間：

$$
\hat L(t+\tau)
\in
[L^-(t+\tau),L^+(t+\tau)]
$$

例如：

> 03:00–06:00  
> 預測負載：35%–50%

這形成：

$$
\boxed{
\text{Forecast Band}
}
$$

使用者能據此排程，但不會把數字當保證。

---

## 16. Capacity Calendar

如果需求有明顯週期，可以提供：

$$
\boxed{
\text{Capacity Calendar}
}
$$

例如：

| 時段 | 預測狀態 | Flex CU |
|---|---|---|
| 18:00–22:00 | Peak | 100% |
| 22:00–01:00 | Normal | 90% |
| 01:00–05:00 | Low | 70% |
| 05:00–08:00 | Very Low | 60% |

這不是固定承諾。

而是一個：

$$
\text{forecast scheduling surface}
$$

---

## 17. 透明度與價格訊號應該一致

若平台顯示：

> Very Low Demand

卻沒有任何：

- 折扣；
- 更快 queue；
- 額外 burst；
- Flex incentive；

使用者可能很快發現：

> 這個容量資訊跟我沒有關係。

因此透明度必須連到可行動介面：

$$
\boxed{
\text{Signal}
\rightarrow
\text{Action}
}
$$

例如：

$$
CLI\downarrow
\Rightarrow
\begin{cases}
\delta\uparrow\\
R_{\max}\uparrow\\
\text{Queue Time}\downarrow
\end{cases}
$$

---

## 18. Capacity Transparency 必須避免 Thundering Herd

如果公開：

> 現在低負載！

所有人立刻啟動工作：

$$
D(t)\uparrow\uparrow
$$

可能形成：

$$
\boxed{
\text{thundering herd}
}
$$

這是一個典型的透明度反作用。

因此不能只公開 signal。

還需要：

$$
\text{reservation}
+
\text{queue}
+
\text{capacity window}
$$

共同存在。

---

## 19. Reservation 使透明度從「搶」變成「排」

假設 03:00–04:00 可接受的離峰額外 workload 為：

$$
Q_{\mathrm{available}}(t)
$$

使用者預約：

$$
r_i
$$

滿足：

$$
\sum_i r_i
\leq
Q_{\mathrm{available}}(t)
$$

當容量滿：

> 03:00–04:00 已滿。

系統推薦：

> 04:00–05:00。

因此：

$$
\boxed{
\text{Transparency}
+
\text{Reservation}
\rightarrow
\text{Orderly Demand Migration}
}
$$

而不是大家一起搶。

---

## 20. Capacity Window Token

甚至可以在產品內建立：

$$
W_{t,k}
$$

表示某時窗的可預約 workload entitlement。

它不是自由交易 Token。

只是：

$$
\text{execution reservation}
$$

例如：

> 03:30–04:00 Flex Slot 已預留。

Agent 到時間自動執行。

這讓：

$$
\text{Capacity Forecast}
$$

真正轉化成：

$$
\text{Scheduled Capacity}
$$

---

## 21. 使用者不一定需要自己研究圖表

透明度不等於要求每個人變成雲端架構師。

產品可以提供三種模式。

### Manual

使用者自己看容量狀態。

### Assisted

系統推薦：

> 建議今晚執行，可省 25 CU。

### Automatic

使用者設定：

> Deadline 前自動選最低成本時段。

即：

$$
t^*
=
\arg\min_{t\leq\delta}
P(t)
$$

透明度同時服務人類與 Agent。

---

## 22. Capacity API for Agents

真正進入 Agent 時代後，可以提供：

$$
\boxed{
\text{Capacity API}
}
$$

Agent 查詢：

$$
\mathcal{C}(m,t,\delta)
$$

取得：

- predicted load；
- estimated cost；
- estimated latency；
- available flex windows；
- reservation availability。

Agent 自己決定：

$$
t_i^*
$$

這使容量狀態直接成為機器可讀的控制訊號。

---

## 23. Agent 會把價格與容量變成策略變數

人類可能只偶爾看一次。

Agent 可以持續計算：

$$
U_i(t)
=
V_i
-
P_i(t)
-
\lambda_i L_i(t)
$$

其中：

- $V_i$：任務價值；
- $P_i(t)$：當時成本；
- $L_i(t)$：延遲成本；
- $\lambda_i$：對延遲的敏感程度。

Agent 選：

$$
t^*
=
\arg\max_t U_i(t)
$$

因此容量透明度一旦機器可讀，就會真正形成：

$$
\boxed{
\text{automated compute scheduling}
}
$$

---

## 24. 但 Capacity API 也可能被大量輪詢

如果每個 Agent 每秒查一次容量：

$$
N_{\mathrm{poll}}\uparrow\uparrow
$$

又會形成額外系統成本。

因此需要：

- caching；
- publish-subscribe；
- event notification；
- minimum refresh interval；
- coarse time buckets。

例如平台只在：

$$
CLI
$$

跨過某門檻時發事件。

而不是所有 Agent 持續 polling。

---

## 25. 透明度的時間解析度

容量資訊不一定要秒級。

可分：

$$
T_{\mathrm{resolution}}
\in
\{
\text{real-time},
\text{5 min},
\text{30 min},
\text{hourly},
\text{daily}
\}
$$

即時對話可能需要粗略 real-time state。

大型 Agent 排程只需要：

$$
30\text{ min}
$$

或：

$$
1\text{ h}
$$

級別。

解析度越細：

$$
C_{\mathrm{disclosure}}\uparrow
$$

因此應依 workload 選擇。

---

## 26. Disclosure Gradient

本文提出三層公開制度。

### Public Layer

面向所有使用者：

$$
\{
\text{load band},
\text{latency band},
\text{discount window}
\}
$$

### Customer / Enterprise Layer

面向付費企業：

$$
\{
\text{model capacity},
\text{region},
\text{quota},
\text{reservation availability},
\text{forecast}
\}
$$

### Internal Layer

只在企業內部：

$$
\{
\text{exact fleet},
\text{rack topology},
\text{power state},
\text{failure domain},
\text{provider contracts}
\}
$$

這就是：

$$
\boxed{
\text{Disclosure Gradient}
}
$$

---

## 27. 透明度與資安

精確即時容量可能被攻擊者利用。

例如：

$$
\text{identify weak period}
$$

再進行：

$$
\text{traffic amplification}
$$

或利用區域資訊推斷：

$$
\text{infrastructure topology}
$$

因此對公開層應使用：

- aggregation；
- delay；
- bucketing；
- differential detail；
- anti-abuse throttling。

亦即：

$$
\boxed{
\text{observable}
\neq
\text{exploitable}
}
$$

---

## 28. 透明度與競爭情報

競爭者可能試圖從容量資料估計：

$$
\text{fleet size}
$$

$$
\text{customer growth}
$$

$$
\text{regional weakness}
$$

$$
\text{unit economics}
$$

因此公開：

> exact 3.2 million GPU-hours remaining

可能過度。

但公開：

> Current Demand: Normal  
> Flex availability: High

通常無法直接反推出完整基礎設施。

所以制度應遵守：

$$
\boxed{
\text{reveal market state, not infrastructure secrets}
}
$$

---

## 29. 透明度與市場操縱

如果 discount 直接跟：

$$
CLI(t)
$$

連動，

大型客戶可能故意：

1. 暫停 workload；
2. 等 CLI 下降；
3. 等折扣增加；
4. 一次大量執行。

形成：

$$
\text{strategic withholding}
$$

這在成熟市場並不罕見。

因此可以使用：

- minimum discount window；
- randomized allocation；
- reservation commitment；
- anti-gaming thresholds；
- delayed state publication。

透明度越市場化，越需要市場規則。

---

## 30. 不要讓容量指數變成新的焦慮來源

若 UI 永遠顯示：

> 73%  
> 74%  
> 72%  
> 78%

使用者可能開始：

$$
\text{compulsive monitoring}
$$

反而降低產品體驗。

因此一般使用者只需要：

$$
\text{Low}
,\quad
\text{Normal}
,\quad
\text{Busy}
$$

更精細數據可以放在：

> Advanced Usage Dashboard

透明度應：

$$
\boxed{
\text{available on demand}
}
$$

而不是強迫所有人一直看。

---

## 31. Quota Transparency 與 Capacity Transparency 必須分離

使用者碰到限制可能有兩種完全不同的原因。

### Personal Quota

$$
Q_i=0
$$

### System Capacity

$$
D(t)>C(t)
$$

如果平台只顯示：

> Usage limit reached

使用者無法分辨。

因此 UI 應至少區分：

> 你的方案額度已用完。

與：

> 平台目前高負載，稍後重試。

這是很基本但重要的：

$$
\boxed{
\text{causal transparency}
}
$$

---

## 32. Model-Specific Capacity

不同模型可能共享部分基礎設施，也可能具有不同瓶頸。

因此不能只提供一個：

$$
CLI_{\mathrm{global}}
$$

可以有：

$$
CLI_m(t)
$$

例如：

> Luna：Low  
> Sol：Busy  
> Image：Normal  
> Video：Peak

這讓使用者選擇：

$$
\text{model substitution}
$$

若任務允許：

> Sol 現在繁忙，要不要先用 Luna？

這本身也是需求調度。

---

## 33. Capacity-Aware Model Routing

如果使用者授權「自動最佳化」，平台可以求：

$$
m^*,t^*
=
\arg\min_{m,t}
\left[
\alpha C(m,t)
+
\beta L(m,t)
-
\gamma Q(m)
\right]
$$

其中：

- $C$：成本；
- $L$：延遲；
- $Q$：模型品質。

因此透明度不只是：

> 告訴使用者。

也可以是：

$$
\boxed{
\text{routing input}
}
$$

---

## 34. 透明度可以揭露「被壓抑的需求」

今天若平台只看成功請求：

$$
S(t)
$$

就可能低估真正需求：

$$
D(t)
$$

因為：

$$
D(t)
=
S(t)
+
Q_{\mathrm{denied}}
+
Q_{\mathrm{abandoned}}
+
Q_{\mathrm{deferred}}
$$

如果使用者可以看到 capacity 並選：

> 晚三小時執行。

平台第一次能記錄：

$$
Q_{\mathrm{deferred}}
$$

這就是：

$$
\boxed{
\text{latent demand observation}
}
$$

---

## 35. 透明度反過來改善容量預測

平台發布預測：

$$
\hat D(t+\tau)
$$

使用者根據預測移動需求。

因此實際：

$$
D'(t+\tau)
$$

又不同於原預測。

形成：

$$
\boxed{
\text{forecast}
\rightarrow
\text{behavior}
\rightarrow
\text{new forecast}
}
$$

這是一個閉環控制系統。

所以透明度不是被動報表。

它會改變被觀測對象。

---

## 36. Self-Defeating Forecast

如果平台說：

> 明天 03:00 很空。

所有人都改到：

$$
03{:}00
$$

結果：

> 明天 03:00 不空了。

這就是：

$$
\boxed{
\text{self-defeating forecast}
}
$$

因此預測發布必須搭配 reservation。

一旦預約量：

$$
R(t)
$$

增加，

平台應更新：

$$
\hat L'(t)
$$

而不是繼續顯示舊 forecast。

---

## 37. Forecast + Reservation 才是完整控制

因此完整流程是：

$$
\hat C(t)
-
\hat D(t)
=
S(t)
$$

其中 $S(t)$ 為預估 spare capacity。

平台釋出：

$$
Q_{\mathrm{reservable}}(t)
\leq
S(t)
$$

使用者預約後：

$$
Q_{\mathrm{reservable}}'(t)
=
Q_{\mathrm{reservable}}(t)
-
R(t)
$$

介面即時更新。

如此：

$$
\boxed{
\text{Forecast}
+
\text{Reservation}
+
\text{Price}
}
$$

才形成真正可控的容量市場。

---

## 38. Capacity Transparency 與公平性

透明市場也可能讓專業用戶更容易搶到低價時段。

如果：

$$
\text{information processing ability}
$$

不同，

可能形成：

$$
\text{expert advantage}
$$

因此應提供：

$$
\text{Auto-Schedule}
$$

給一般使用者。

例如：

> 在 deadline 前幫我自動選最划算的時間。

如此即使不理解容量市場，也能取得相近利益。

---

## 39. 無障礙的經濟介面

理想 UI 可以非常簡單。

例如：

**Sol**

> Current demand: Busy  
> Normal response may be slower.

**Your options**

> 現在執行：100 CU  
> 2 小時內：85 CU  
> 今晚低峰：65 CU

再加：

> 自動幫我選最適合時間。

這比：

> Error 429

具有高得多的可理解性。

---

## 40. 企業 Capacity Dashboard

企業客戶則可以看到更多。

例如：

$$
\{
CLI_m(t),
\hat CLI_m(t+\tau),
Q_{\mathrm{quota}},
Q_{\mathrm{capacity}},
R_{\mathrm{reserved}},
P_{\mathrm{flex}}
\}
$$

並讓排程系統根據：

$$
\text{SLA}
$$

自動 routing。

這很接近 Azure Model Capacities API 與 AWS capacity scoring 已經驗證的企業工作方式。

---

## 41. 透明度與 SLA

如果平台公開容量，只是「建議」，應清楚標記：

$$
\text{advisory}
$$

如果客戶支付 reserved capacity，則可能具有：

$$
\text{contractual SLA}
$$

二者不能混淆。

因此：

$$
\boxed{
\text{Capacity Signal}
\neq
\text{Capacity Guarantee}
}
$$

AWS Spot Placement Score 特別強調 score 不保證 capacity，正是這個區分。

---

## 42. 一個三層容量訊號模型

本文提出簡化模型：

### Layer 1：State

$$
S(t)
\in
\{
\text{Low},
\text{Normal},
\text{Busy},
\text{Peak}
\}
$$

### Layer 2：Forecast

$$
F(t+\tau)
=
\{
\text{state},
\text{confidence},
\text{window}
\}
$$

### Layer 3：Action

$$
A(t)
=
\{
\text{run now},
\text{reserve},
\text{flex},
\text{surrender}
\}
$$

只有三層同時存在，透明度才真正具備控制能力。

---

## 43. 可測試假說

### H1：容量透明度會增加自願排程

若使用者看到：

$$
CLI(t)
$$

與：

$$
\hat CLI(t+\tau)
$$

預期：

$$
Q_{\mathrm{scheduled}}\uparrow
$$

---

### H2：透明度搭配折扣比單獨折扣更有效

因為：

$$
\text{reason signal}
+
\text{price signal}
$$

共同提高可信度。

---

### H3：透明度若沒有 reservation，可能增加短期峰值

即：

$$
T_D\uparrow
\Rightarrow
D_{\mathrm{herd}}\uparrow
$$

在低負載訊號發布後可能成立。

---

### H4：容量 band 比虛假精確數字更有信任度

當預測不確定時：

$$
\text{banded disclosure}
$$

可能優於：

$$
\text{exact percentage}
$$

---

### H5：一般用戶偏好簡化訊號，企業偏好原始容量資訊

因此：

$$
T_D^*
$$

會因使用者類型不同而不同。

---

### H6：Auto-Schedule 可以降低資訊能力造成的不公平

即使使用者不理解市場，也能透過 Agent：

$$
t^*=\arg\min P(t)
$$

取得低峰福利。

---

## 44. 實驗設計

可以測試五種介面。

### Group A：Opaque

只有傳統 rate limit。

### Group B：Current State Only

顯示：

$$
CLI(t)
$$

### Group C：State + Forecast

加入：

$$
\hat CLI(t+\tau)
$$

### Group D：State + Forecast + Discount

加入價格訊號。

### Group E：State + Forecast + Discount + Reservation

形成完整控制迴路。

比較：

$$
PAR
$$

$$
Q_{\mathrm{deferred}}
$$

$$
Q_{\mathrm{rejected}}
$$

$$
\text{Reservation Rate}
$$

$$
\text{User Trust}
$$

$$
\text{Forecast Error}
$$

$$
\text{Thundering Herd Incidence}
$$

即可觀察透明度是否真的改善供需。

---

## 45. 從產品透明度走向投資透明度

一旦企業已經內部計算：

$$
CLI
$$

$$
\text{Capacity Forecast}
$$

$$
\text{Deferred Demand}
$$

$$
\text{Reservation Rate}
$$

下一個自然問題就是：

> 這些資料是否只應該給使用者看？

或者：

> 某些聚合指標是否可以提供給投資者？

例如：

$$
\text{Compute Load Factor}
$$

$$
\text{Peak Utilization}
$$

$$
\text{Unserved Demand}
$$

$$
\text{Flexible Workload Ratio}
$$

都可能成為 AI 企業新的營運基本面。

因此：

$$
\text{Product Transparency}
\rightarrow
\text{Operational Metrics}
\rightarrow
\text{Investor Signal}
$$

這正是下一篇的主題。

---

## 46. 基本原則

本文提出十二項原則。

### 原則一：透明度不是目的，而是控制工具

$$
\text{Disclosure}
\rightarrow
\text{Decision}
\rightarrow
\text{Demand Shaping}
$$

### 原則二：公開市場狀態，不必公開實體基礎設施秘密

$$
\text{Market State}
\neq
\text{Fleet Topology}
$$

### 原則三：使用 score、band 與 confidence

避免 false precision。

### 原則四：Quota 與 Capacity 必須分開

$$
Q_i=0
$$

與：

$$
D>C
$$

是不同原因。

### 原則五：Incident Status 與 Capacity Status 也不同

「沒壞」不代表「很空」。

### 原則六：Forecast 必須附帶不確定性

$$
\hat L
\neq
L
$$

### 原則七：透明度必須連到可行動選項

否則只是資訊裝飾。

### 原則八：透明度必須搭配 reservation

避免 thundering herd。

### 原則九：Agent 應能機器讀取容量訊號

形成自動排程。

### 原則十：公開資料應分層

Public、Enterprise、Internal 不應相同。

### 原則十一：透明度不能變成焦慮介面

高解析度資料應 opt-in。

### 原則十二：真正需要的是 Decision-Useful Transparency

$$
\boxed{
\text{not maximum disclosure, but maximum decision value}
}
$$

---

## 47. 限制

第一，本文提出的消費者 Capacity Index、Capacity Calendar 與公開 forecast 並不代表現行主要 AI 消費產品已經提供這些功能。

第二，容量本身可能高度動態，預測會有誤差。

第三，公開資訊會改變需求，因此模型必須處理 feedback loop。

第四，透明度可能增加 gaming、資安與競爭情報風險。

第五，過度細緻的資訊可能降低一般使用者體驗。

第六，不同模型共享底層基礎設施，使模型級 capacity attribution 並不一定簡單。

第七，供應商可能不希望公開任何可被用於估算 fleet economics 的指標，因此需要 aggregation 與 disclosure gradient。

---

## 48. 結論

在 AI 服務的早期階段，黑箱容量管理具有合理性。

平台只需要告訴使用者：

> 可以用。

或者：

> 現在不能用。

但當 AI 進入長程 Agent、研究、程式開發、批次工作與企業生產環境後，這種二元介面逐漸不夠。

成熟雲端市場已經證明，可以在不公開完整基礎設施秘密的前提下，向客戶提供：

$$
\text{capacity likelihood}
$$

$$
\text{quota state}
$$

$$
\text{regional availability}
$$

與：

$$
\text{deployment capacity}
$$

作為決策訊號。

因此 AI 消費市場也可以逐步從：

$$
\text{Opaque Rate Limit}
$$

走向：

$$
\boxed{
\text{Observable Capacity Market}
}
$$

但關鍵不是：

> 公開所有 GPU。

而是：

$$
\boxed{
\text{reveal enough information to coordinate behavior}
}
$$

一套成熟介面可能只需要告訴使用者：

> 現在：Busy  
> 今晚：Low  
> 今晚執行：省 30 CU  
> 要不要幫你自動排？

底層則由：

$$
CLI
+
\text{Forecast}
+
\text{Reservation}
+
\text{Pricing}
$$

共同控制。

這使透明度從：

$$
\text{passive disclosure}
$$

變成：

$$
\boxed{
\text{active coordination mechanism}
}
$$

因此本文的核心命題為：

$$
\boxed{
\text{Compute transparency is not merely disclosure; it can be a control surface for demand.}
}
$$

中文即：

**算力透明度不只是資訊揭露，它本身可以成為需求調度的控制介面。**

而一旦這些 capacity metrics 已經被企業穩定計算，下一個問題便自然出現：

> 為什麼它們只能拿來調度使用者？

> 它們能不能同時讓投資者更精確理解一家 AI 企業的真正算力經濟？

這正是下一篇：

**算力透明度作為投資工具：AI 企業的新基本面。**

---

## 參考資料

1. Amazon Web Services. *Spot placement score — Amazon Elastic Compute Cloud.* Accessed 2026-09-07.
2. Amazon Web Services. *GetSpotPlacementScores API Reference.* Accessed 2026-09-07.
3. Amazon Web Services. *Best practices for Amazon EC2 Spot.* Accessed 2026-09-07.
4. Microsoft Learn. *Manage Azure OpenAI in Microsoft Foundry Models quota.* Updated 2026-05-07; accessed 2026-09-07.
5. Microsoft Learn. *Azure OpenAI in Microsoft Foundry Models Quotas and Limits.* Updated 2026-08-20; accessed 2026-09-07.
6. OpenAI. *OpenAI Status.* Accessed 2026-09-07.
7. OpenAI. *OpenAI Status History.* Accessed 2026-09-07.

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

**Paper 5**  
從 Rate Limiting 到 Demand Engineering：離峰折扣與 AI 需求響應

**Paper 6 — 本篇**  
算力透明度作為控制介面：從黑箱限流到容量可觀測市場

**Paper 7 — Next**  
算力透明度作為投資工具：AI 企業的新基本面

**Paper 8**  
AI 市場的制度演化：從商品化到容量市場

**Extra 1**  
Token 消耗症候群：到期額度如何反向塑造人的認知行為

**Extra 2**  
跨產業制度移植：AI 產業其實不用每件事重新發明
