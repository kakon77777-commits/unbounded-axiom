# 額度的時間可替代性：月算力、Burst 與集中式工作
## Temporal Fungibility of AI Allowances: Monthly Compute, Burst Capacity, and Concentrated Work

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Paper 2 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

AI 訂閱產品常以五小時、每日、每週或其他固定時間窗切割使用額度。這種制度可以降低瞬時容量風險，但同時將使用權綁定於曆法片段，使高強度、非均勻的研究、工程、創作與 Agentic Workflow 被迫服從人工平均化的使用節奏。本文在前篇「四時鐘分離」框架之上，提出 **Temporal Fungibility（額度的時間可替代性）**：在不改變某一長週期總資源權利的前提下，允許使用者將可用算力在週期內跨子時段移動、集中或延後，並由獨立的 Burst、Rate Limit、Queue、Priority 與 Capacity Scheduling 機制控制瞬時風險。

本文強調，時間可替代性不等於無限瞬時使用。其核心不是取消物理容量限制，而是將「總量權利」與「何時消耗」分離。對使用者而言，這使 AI 工作模式更接近真實專案：高強度工作可以集中發生，低活動期則不必為避免額度失效而製造人工消耗。對供應商而言，若時間可替代性與離峰誘因、可延遲任務、排隊與預測性容量管理結合，則可能從單純 Rate Limiting 轉向 Demand Shaping。

本文進一步定義 Flexible Entitlement Ratio、Burst Concentration Ratio、Fragmentation Loss、Peak Exposure 與 Effective Utilization 等可測量指標，並提出多種產品實驗設計。本文的基本命題是：**月訂閱可以繼續以曆法作為結算週期，但不應將曆法碎片化直接等同於智能使用權碎片化。** 更成熟的制度應讓使用者擁有一個較長週期的 Compute Budget，同時由獨立的瞬時容量規則保護共享基礎設施。

**關鍵詞：** Temporal Fungibility、AI 算力、月額度、Burst、Rate Limit、Compute Budget、Quota Fragmentation、集中式工作、需求調度、AI 訂閱制

---

## 1. 從四時鐘分離走向額度的時間可替代性

前篇提出：

$$
T_{\mathrm{billing}}
\neq
T_{\mathrm{entitlement}}
\neq
T_{\mathrm{compute}}
\neq
T_{\mathrm{work}}
$$

亦即，帳務結算、使用權、物理算力與實際工作進展不應被視為同一個時間尺度。

但若只完成概念分離，仍然沒有回答下一個問題：

> 如果一個使用者在一個月內擁有某種總體 AI 使用權，他能否自由決定這些使用權在何時消耗？

本文將這個問題形式化為：

$$
\boxed{
\text{Temporal Fungibility}
}
$$

也就是「額度的時間可替代性」。

其基本直覺是：

$$
Q_{\mathrm{month}}
=
\sum_{d=1}^{D}q_d
$$

其中 $Q_{\mathrm{month}}$ 是某一月的總 Compute Budget， $q_d$ 是第 $d$ 日的消耗。

若總量權利已經被定義為：

$$
\sum_{d=1}^{D}q_d\leq Q_{\mathrm{month}}
$$

則使用者是否必須滿足：

$$
q_d\approx \frac{Q_{\mathrm{month}}}{D}
$$

並不是一個必然的經濟要求。

這只是一種可能的容量管理制度。

對高度不均勻的 AI 工作而言，更自然的配置可能是：

$$
(q_1,q_2,\ldots,q_D)
=
(0,0,250,300,200,0,\ldots)
$$

而不是：

$$
(q_1,q_2,\ldots,q_D)
\approx
(\bar q,\bar q,\ldots,\bar q)
$$

只要平台仍能處理瞬時 throughput，集中使用本身不應自動等價於「濫用」。

---

## 2. 什麼是 Temporal Fungibility

本文將一個計費週期 $B$ 內的總額度定義為：

$$
Q_B
$$

其中可跨子時段重新配置的部分為：

$$
Q_{\mathrm{flex}}
$$

不可移動、必須在特定時間窗使用的部分為：

$$
Q_{\mathrm{fixed}}
$$

因此：

$$
Q_B
=
Q_{\mathrm{flex}}
+
Q_{\mathrm{fixed}}
$$

定義 **Flexible Entitlement Ratio**：

$$
F_T
=
\frac{Q_{\mathrm{flex}}}{Q_B}
$$

且：

$$
0\leq F_T\leq 1
$$

當：

$$
F_T=0
$$

代表額度完全被時間碎片化。

當：

$$
F_T=1
$$

代表在該結算週期內，總額度原則上可自由跨時段配置，但仍可能受到 Rate Limit、Burst Limit、Queue 與 Priority 約束。

因此：

$$
F_T=1
$$

並不表示：

$$
R_{\max}\rightarrow\infty
$$

這是本文最重要的區分之一。

---

## 3. 時間可替代性不等於無限 Burst

假設某方案提供：

$$
Q_{\mathrm{month}}=1000\ \mathrm{CU}
$$

如果完全沒有瞬時限制，那麼理論上使用者可以在極短時間內要求：

$$
1000\ \mathrm{CU}
$$

全部執行。

對共享 AI 基礎設施而言，這顯然可能造成不可接受的尖峰。

因此本文提出：

$$
\boxed{
\text{Temporal Fungibility}
\neq
\text{Unlimited Throughput}
}
$$

較合理的制度是：

$$
\sum_{t\in B}q(t)\leq Q_B
$$

同時：

$$
r(t)\leq R_{\max}
$$

其中 $r(t)$ 表示某一短時間窗的實際消耗速率。

若平台負載較高，也可以進一步加入：

$$
R_{\max}=R_{\max}(L(t),P_i,S_i)
$$

其中：

- $L(t)$：平台即時負載；
- $P_i$：使用者或任務優先級；
- $S_i$：所購買的服務層級。

這樣的制度允許：

> 一個月的總量可以集中使用，但不能要求在任意瞬間無限吞吐。

也就是將：

$$
\boxed{
\text{Entitlement Flexibility}
}
$$

與：

$$
\boxed{
\text{Infrastructure Safety}
}
$$

同時保留。

---

## 4. 集中式工作不是例外，而是知識工作的正常型態

許多知識型工作具有明顯的 burst structure。

例如軟體工程可能呈現：

$$
\text{Design}
\rightarrow
\text{Implementation Burst}
\rightarrow
\text{Debug Burst}
\rightarrow
\text{Review}
\rightarrow
\text{Idle}
$$

研究工作可能呈現：

$$
\text{Reading}
\rightarrow
\text{Hypothesis Burst}
\rightarrow
\text{Computation}
\rightarrow
\text{Verification}
\rightarrow
\text{Pause}
$$

創作工作也可能呈現：

$$
\text{Exploration}
\rightarrow
\text{Generation Burst}
\rightarrow
\text{Editing}
\rightarrow
\text{Inactivity}
$$

這些工作流程本身就不是平滑函數。

令使用者的理想 AI 需求為：

$$
d_i^*(t)
$$

則實際工作常見：

$$
\mathrm{Var}[d_i^*(t)]\gg 0
$$

亦即需求變異很高。

如果產品制度強迫：

$$
d_i(t)\approx \bar d_i
$$

那麼平台其實是在用商業規則改寫工作節奏。

這可能造成兩種損失：

第一種是專案被迫延後。

第二種是低需求期間為避免額度失效而產生人工消耗。

因此，過低的時間可替代性可能同時造成：

$$
\text{Delay Loss}
+
\text{Expiration Waste}
$$

---

## 5. Quota Fragmentation：額度碎片化損失

假設一個月被切割成 $K$ 個子時段，每個時段的上限為：

$$
\bar q_k
$$

使用者在第 $k$ 個時段的理想需求為：

$$
q_k^*
$$

若需求超過該時段上限，則未被服務的需求為：

$$
u_k
=
\max(0,q_k^*-\bar q_k)
$$

另一方面，如果該時段使用不足，未被使用且不可轉移的額度為：

$$
w_k
=
\max(0,\bar q_k-q_k^*)
$$

若同一個總結算週期內同時存在：

$$
u_i>0
$$

與：

$$
w_j>0
$$

且 $i\neq j$，則出現一個制度性現象：

> 同一名使用者在一個時間窗被告知「用太多」，卻在另一個時間窗讓額度失效。

本文將可由跨期轉移消除的部分定義為 **Fragmentation Loss**：

$$
L_F
=
\min
\left(
\sum_{k=1}^{K}u_k,
\sum_{k=1}^{K}w_k
\right)
$$

當：

$$
L_F>0
$$

代表至少有一部分「不足」並非來自整個週期的總額度不足，而是來自額度被切成不可互換的小區塊。

這正是 Temporal Fungibility 要處理的核心問題。

---

## 6. Burst Concentration Ratio

為了區分合理集中使用與極端瞬時負載，本文定義 **Burst Concentration Ratio**。

令長週期總額度為：

$$
Q_B
$$

某一短時間窗 $\tau$ 內使用的額度為：

$$
Q_{\tau}
$$

則：

$$
BCR_{\tau}
=
\frac{Q_{\tau}}{Q_B}
$$

例如某使用者在一個月的五天內使用 80% 的月額度，則其五日尺度：

$$
BCR_{5d}=0.8
$$

這本身不代表違規。

真正需要搭配觀察的是：

$$
R_{\mathrm{peak}}
$$

以及平台負載：

$$
L(t)
=
\frac{D(t)}{C(t)}
$$

因此可以出現：

$$
BCR_{\tau}\uparrow
$$

但：

$$
L(t)<1
$$

的情況。

這表示使用者高度集中工作，但平台仍有能力服務。

相反地，一個總月用量很低的使用者，也可能在某個極短時刻產生非常高的瞬時 request rate。

因此：

$$
\text{Monthly Heavy Use}
\neq
\text{Instantaneous Abuse}
$$

而：

$$
\text{Low Monthly Use}
\neq
\text{Low Peak Load}
$$

這兩者必須分開測量。

---

## 7. 從「平均使用者」假設走向需求分布

傳統固定訂閱很容易隱含一個平均使用者模型：

$$
E[q_i(t)]\approx \bar q
$$

但實際市場可能存在非常不同的使用型態：

$$
\mathcal{U}
=
\{
U_{\mathrm{light}},
U_{\mathrm{steady}},
U_{\mathrm{burst}},
U_{\mathrm{agent}},
U_{\mathrm{enterprise}}
\}
$$

其中：

- $U_{\mathrm{light}}$：低頻一般使用者；
- $U_{\mathrm{steady}}$：穩定工作型使用者；
- $U_{\mathrm{burst}}$：高強度集中型使用者；
- $U_{\mathrm{agent}}$：自動化或長程 Agent 工作；
- $U_{\mathrm{enterprise}}$：具明顯業務週期的企業工作負載。

如果產品只針對：

$$
U_{\mathrm{steady}}
$$

設計，則其他使用型態都會被視為異常。

更成熟的方法應估計需求分布：

$$
p(q,t,\tau,\delta)
$$

其中 $\tau$ 表示任務可接受延遲， $\delta$ 表示 deadline。

如此平台真正需要管理的就不只是「多少人」，而是：

$$
\boxed{
\text{多少需求}
+
\text{何時需要}
+
\text{可以等多久}
}
$$

---

## 8. 現行 AI 產品已經出現「總量與延伸用量」的雛形

截至 2026 年 9 月，主要 AI 產品已經開始出現比純固定限額更彈性的制度。

OpenAI 的個人方案在部分支援功能上允許使用者於方案內含使用量耗盡後購買 credits 繼續使用；Business 與 Enterprise/Edu 的 flexible pricing 則更進一步將方案內含使用量與 shared credit pool 結合。

Anthropic 仍以特定時間週期內的 usage budget 管理 Claude 使用，但其官方說明也明確指出，實際消耗不是單純訊息數，而會受到對話長度、複雜度、功能、模型與 effort level 等因素影響。

這些發展顯示，產業已經逐步承認：

$$
\text{one message}
\neq
\text{one unit of cost}
$$

同時也開始承認：

$$
\text{subscription access}
\neq
\text{all possible usage}
$$

但目前多數制度仍然主要解決：

$$
\text{用完之後怎麼繼續}
$$

而 Temporal Fungibility 關注的是另一個問題：

$$
\boxed{
\text{在用完之前，能否更自由地決定何時使用？}
}
$$

---

## 9. 雲端產業提供的結構類比

AI 產業並不是第一個面對 burst workload 的產業。

雲端基礎設施長期處理：

$$
\text{steady load}
+
\text{burst load}
+
\text{reserved capacity}
+
\text{overflow}
$$

例如 provisioned throughput 與 standard spillover 的組合，本質上就是：

$$
\text{Reserved Base}
+
\text{Elastic Overflow}
$$

當預留容量不足時，額外流量可以進入按量計費或標準容量。

這種設計的重要啟示不是要求 AI 訂閱照搬雲端帳單，而是：

$$
\boxed{
\text{Base Entitlement}
+
\text{Elastic Burst}
}
$$

可以被視為兩種不同權利。

對消費型 AI 產品而言，可對應為：

$$
\text{Monthly Compute Budget}
+
\text{Burst Envelope}
+
\text{Optional Overage}
$$

這比單一「每五小時可用多少」更接近成熟容量制度。

---

## 10. Temporal Fungibility 的三種產品版本

Temporal Fungibility 不必一步到位。

可以分為三個制度層級。

### 10.1 Partial Fungibility

只有部分額度可跨時段移動：

$$
F_T\in(0,1)
$$

例如：

$$
Q_{\mathrm{flex}}=0.5Q_B
$$

其餘維持固定窗口，以降低容量風險。

這適合作為早期實驗。

---

### 10.2 Full Period Fungibility

整個月的 Compute Budget 都可自由配置：

$$
F_T=1
$$

但受：

$$
R_{\max}
$$

與平台負載管理。

這是最接近「月額度就是月額度」的制度。

---

### 10.3 Capacity-Aware Fungibility

在 full fungibility 之上加入動態 capacity signal：

$$
R_{\max}(t)
=
f(L(t))
$$

甚至讓單位額度消耗率依時段不同：

$$
\gamma(t)
=
f(L(t))
$$

其中：

$$
Q_{\mathrm{charged}}
=
\int \gamma(t)c(t)\,dt
$$

離峰時：

$$
\gamma(t)<1
$$

尖峰時：

$$
\gamma(t)\geq 1
$$

這就開始與後續的 Demand Engineering、離峰折扣與容量市場連接。

---

## 11. 使用者不是一定要「自己搶算力」

時間可替代性若只做成「額度現在可以集中使用」，仍然可能造成 thundering herd。

因此更合理的產品介面應允許使用者表達 deadline，而不是只表達「現在」。

令任務 $J_i$ 表示為：

$$
J_i
=
(C_i,\delta_i,p_i)
$$

其中：

- $C_i$：所需計算量；
- $\delta_i$：最晚完成時間；
- $p_i$：優先級。

平台可以尋找：

$$
t_i^*
=
\arg\min_{t\leq\delta_i}
\mathrm{Cost}(t)
$$

並在不超過 deadline 的條件下自動排程。

使用者只需要看到：

- 現在執行；
- 今天內完成；
- 明早前完成；
- 離峰執行。

因此：

$$
\text{Human Work Time}
\neq
\text{AI Execution Time}
$$

在 Agent 時代，這個分離尤其重要。

使用者可以白天提交工作，AI 在低峰時段完成，隔天直接取得結果。

---

## 12. Temporal Fungibility 對供應商並非只有成本

乍看之下，提高時間可替代性會增加 burst risk。

但它也可能創造新的營運訊號。

如果使用者可以表達：

$$
\delta_i
$$

與：

$$
p_i
$$

平台就能觀察到過去被隱藏的需求彈性。

現在的硬性限流只會得到：

$$
\text{request denied}
$$

卻不知道使用者是否：

- 願意等一小時；
- 願意等八小時；
- 願意改到明天；
- 願意為即時處理多付費。

若制度允許選擇，供應商可估計：

$$
D(t,\Delta t,P)
$$

也就是需求量、等待彈性與價格彈性的聯合分布。

這些資料可進一步用於：

$$
\text{Capacity Planning}
$$

$$
\text{Energy Scheduling}
$$

$$
\text{Model Routing}
$$

$$
\text{Discount Design}
$$

與：

$$
\text{Infrastructure Investment}
$$

因此，Temporal Fungibility 不只是消費者福利，也可能成為更高解析度的需求感測器。

---

## 13. Peak Exposure：集中工作真正的企業風險

為了讓供應商衡量某一類用戶是否增加尖峰風險，本文定義 **Peak Exposure**。

令平台負載函數為：

$$
L(t)
=
\frac{D(t)}{C(t)}
$$

使用者 $i$ 的消耗為：

$$
c_i(t)
$$

則可定義：

$$
PE_i
=
\frac{
\int_B c_i(t)L(t)\,dt
}{
\int_B c_i(t)\,dt
}
$$

如果一名使用者總是選擇高負載時間使用，其：

$$
PE_i
$$

較高。

如果另一名使用者雖然總量大，但大部分工作可移到低峰：

$$
PE_i
$$

反而可能較低。

因此企業不應單純把：

$$
Q_i
$$

當成風險。

更有價值的是：

$$
(Q_i,BCR_i,PE_i)
$$

一起觀察。

這也為未來的離峰折扣提供理論基礎。

---

## 14. Effective Utilization：總用量不變也可能改善效率

供應商真正關心的不一定是降低：

$$
\int_B D(t)\,dt
$$

而是降低：

$$
\max_t D(t)
$$

如果原本需求曲線高度尖峰：

$$
D_{\mathrm{peak}}\gg D_{\mathrm{average}}
$$

平台就必須為峰值配置更多冗餘 capacity。

若透過時間可替代性與排程，將部分需求從尖峰移到離峰：

$$
D(t)
\rightarrow
D'(t)
$$

可能達成：

$$
\max_t D'(t)
<
\max_t D(t)
$$

即使：

$$
\int_B D'(t)\,dt
=
\int_B D(t)\,dt
$$

總計算量完全沒有下降。

這代表：

> 使用者沒有少用 AI，但整體基礎設施可能更有效率。

可定義簡化的 Effective Utilization：

$$
U_{\mathrm{eff}}
=
\frac{
\int_B D(t)\,dt
}{
C_{\mathrm{provisioned}}\cdot |B|
}
$$

若峰值被壓平，平台可能在不同比例的 provisioned capacity 下維持相同服務品質。

---

## 15. 可能的反效果：Jevons-like Rebound

提高額度可替代性也可能刺激更多使用。

如果使用者知道：

> 我這個月的額度不會因為週期切割而浪費。

他可能更積極規劃大型 Agent 或研究任務。

因此：

$$
F_T\uparrow
$$

可能導致：

$$
Q_{\mathrm{actual}}\uparrow
$$

這不一定是壞事。

對供應商而言，只要：

$$
\mathrm{Revenue}(Q)
-
\mathrm{Cost}(Q)>0
$$

更高的有效使用反而可能提高產品價值與留存。

真正需要避免的是：

$$
\text{Unit Economics}<0
$$

卻因固定訂閱產生無上限 consumption。

因此 Temporal Fungibility 必須搭配清楚的：

$$
Q_B
$$

而不是取消總量控制。

---

## 16. 一個基礎混合方案

基於前述分析，可以設計一個簡化版本。

假設使用者購買：

$$
Q_B=1000\ \mathrm{CU/month}
$$

其中：

$$
F_T=0.8
$$

因此：

$$
Q_{\mathrm{flex}}=800\ \mathrm{CU}
$$

另外：

$$
Q_{\mathrm{fixed}}=200\ \mathrm{CU}
$$

用於保障基本日常使用。

同時設定：

$$
R_{\mathrm{standard}}=R_s
$$

$$
R_{\mathrm{burst}}=R_b
$$

且：

$$
R_b>R_s
$$

使用者可在低負載時取得較高 Burst，尖峰時則進入 queue 或降低優先級。

若仍不足，可選：

$$
\text{PAYG Overage}
$$

若任務可延遲，則可選：

$$
\text{Flex Queue}
$$

這樣一個產品同時具備：

$$
\boxed{
\text{Predictable Subscription}
+
\text{Temporal Flexibility}
+
\text{Infrastructure Protection}
}
$$

---

## 17. 可測試假說

### H1：提高 $F_T$ 會降低 Fragmentation Loss

預期：

$$
\frac{\partial L_F}{\partial F_T}<0
$$

---

### H2：Burst 型使用者對 $F_T$ 的效用提升高於 steady 型使用者

若使用者需求變異：

$$
\mathrm{Var}[d_i(t)]
$$

越高，則提高 Temporal Fungibility 所帶來的效用增益越大。

---

### H3：若沒有 capacity-aware scheduling，提高 $F_T$ 可能增加峰值

即：

$$
F_T\uparrow
\Rightarrow
D_{\mathrm{peak}}\uparrow
$$

但加入 Flex、Queue 與 off-peak incentive 後，該效果可能被反轉。

---

### H4：允許 deadline expression 可降低 Peak Exposure

若使用者能提交：

$$
\delta_i
$$

則平台可將彈性任務移往低負載區間，使：

$$
E[PE_i]\downarrow
$$

---

### H5：高 Temporal Fungibility 可能提高總使用量，但同時提高留存與方案價值

因此評估不能只看：

$$
Q_{\mathrm{actual}}
$$

而應同時觀察：

$$
\text{Retention}
,\quad
\text{Gross Margin}
,\quad
\text{Task Completion}
,\quad
\text{Peak Load}
$$

---

## 18. 實驗設計

可以將使用者隨機分為四組。

### Group A：固定時間窗

傳統制度。

$$
F_T\approx 0
$$

### Group B：50% 可跨期

$$
F_T=0.5
$$

### Group C：100% 月內可跨期，但固定 Rate Limit

$$
F_T=1
$$

### Group D：100% 可跨期，加上 capacity-aware Flex scheduling

$$
F_T=1
$$

且具有：

$$
\gamma(t)
$$

與 deadline scheduling。

比較指標包括：

$$
L_F
$$

$$
D_{\mathrm{peak}}
$$

$$
U_{\mathrm{eff}}
$$

$$
\text{Retention}
$$

$$
\text{User Satisfaction}
$$

$$
\text{Task Completion Rate}
$$

$$
\text{Gross Margin per User}
$$

如果 Group D 同時降低碎片化損失與峰值壓力，就能支持：

> 更自由的額度制度不必然與容量管理衝突。

---

## 19. 制度邊界與反套利

時間可替代性若設計不當，也可能重新創造「訂閱轉 API」套利。

因此至少需要：

### 19.1 身分與使用權不可直接外借

Temporal Fungibility 是：

$$
\text{same user, different time}
$$

不是：

$$
\text{different users, same entitlement}
$$

### 19.2 Rate Limit 與 Automation Policy 分離

允許集中使用不代表允許無限制自動化。

### 19.3 Compute Unit 應反映不同任務成本

因為：

$$
1\text{ token}
\neq
1\text{ unit of compute}
$$

長 context、reasoning、agent loop、圖片與工具使用都可能需要不同換算。

### 19.4 Overage 應明確且可預測

避免使用者因額度彈性反而產生 billing anxiety。

因此，理想制度應提供：

$$
\text{Hard Spend Cap}
$$

$$
\text{Usage Forecast}
$$

與：

$$
\text{Clear Remaining Budget}
$$

---

## 20. 從 Temporal Fungibility 到 Compute Wallet

當額度可以在月內自由移動後，下一個自然問題就是：

> 為什麼它只能存在於某一個產品介面？

如果 Chat、Code、Agent、Research 與 API 都在消耗同一個供應商的計算資源，那麼長期制度可能進一步形成：

$$
\boxed{
\text{Compute Wallet}
}
$$

也就是把：

$$
Q_B
$$

從單一功能額度提升為跨產品的可計量資源池。

但這會產生新的問題：

- 不同模型如何換算；
- 訂閱功能與 API 是否共池；
- 額度是否 rollover；
- 是否允許 borrow；
- 是否可以加購；
- 是否可以返還或轉換。

這些問題將在下一篇正式處理。

因此，Temporal Fungibility 是 Compute Wallet 的制度前提之一：

$$
\text{Time Fungibility}
\rightarrow
\text{Resource Fungibility}
$$

但兩者不是同一件事。

---

## 21. 基本原則

本文可濃縮為七項原則。

### 原則一：月額度應優先被理解為長週期資源權利

$$
Q_B
$$

而不是一系列彼此不可交換的碎片。

### 原則二：時間可替代性與無限 Burst 必須分離

$$
F_T\uparrow
\not\Rightarrow
R_{\max}\uparrow\infty
$$

### 原則三：集中式工作是正常需求型態

不能只以平均使用者作為唯一產品模型。

### 原則四：額度碎片化本身會創造制度損失

$$
L_F>0
$$

表示同一長週期內同時存在被拒需求與失效額度。

### 原則五：Deadline 應逐漸成為 AI 任務的可表達屬性

$$
J_i=(C_i,\delta_i,p_i)
$$

使系統可以主動調度。

### 原則六：供應商應管理 Peak Exposure，而不只是 Monthly Usage

$$
PE_i
$$

比單純總量更接近容量風險。

### 原則七：更自由的使用權必須搭配更好的容量市場

Temporal Fungibility 最終不是取消限制，而是：

$$
\boxed{
\text{replace crude temporal fragmentation with explicit resource coordination}
}
$$

---

## 22. 結論

AI 訂閱制度面對的核心矛盾，不是「時間到底重不重要」。

時間當然重要。

GPU capacity、電力、網路、排隊與使用者併發都存在於真實時間。

真正需要修正的是：

$$
\boxed{
\text{physical time constraints}
\neq
\text{calendar-fragmented user rights}
}
$$

平台需要限制的是共享基礎設施的瞬時風險，而不是假定每一個人的認知工作都應平均分布於曆法。

因此，較成熟的 AI 訂閱制度應逐步從：

$$
\text{Fixed Window Quota}
$$

轉向：

$$
\boxed{
\text{Long-Period Compute Budget}
+
\text{Burst Envelope}
+
\text{Rate Control}
+
\text{Flexible Scheduling}
}
$$

這使一個使用者可以在需要時高度集中工作，在不需要時真正休息，而不必因額度即將失效而製造沒有實際價值的消耗。

更重要的是，這並不必然增加供應商的長期總成本。

如果彈性任務可以被辨識、延後與移往離峰，則：

$$
\max_t D(t)
$$

甚至可能下降。

因此，本篇的核心命題可以表述為：

$$
\boxed{
\text{Monthly compute should be temporally fungible within a controlled burst envelope.}
}
$$

中文即：

**月度 AI 算力應在受控制的 Burst 邊界內具有時間可替代性。**

從這一步開始，「月額度」才真正從曆法碎片轉變為可以被管理的資源權利；而下一步，則是把這種資源權利進一步整合成跨功能、可加購、可延續、可借用的 Compute Wallet。

---

## 參考資料

1. OpenAI Help Center. *Using Credits for Flexible Usage in ChatGPT (Personal plans).* Accessed 2026-09-07.
2. OpenAI Help Center. *ChatGPT Rate Card (Business, Enterprise/Edu credit-based pricing).* Accessed 2026-09-07.
3. Anthropic Help Center. *How do usage and length limits work?* Published 2026-07-13; accessed 2026-09-07.
4. Microsoft Learn. *Provisioned throughput for Foundry Models.* Accessed 2026-09-07.
5. Microsoft Learn. *Manage traffic with spillover for provisioned deployments.* Accessed 2026-09-07.
6. Amazon Web Services. *Best practices for Amazon EC2 Spot.* Accessed 2026-09-07.

---

## Series Navigation

**Paper 1**  
AI 訂閱制的制度錯位：當曆法時間不再等於智能消耗

**Paper 2 — 本篇**  
額度的時間可替代性：月算力、Burst 與集中式工作

**Paper 3 — Next**  
訂閱、API 與 Compute Wallet：AI 混合計價制度

**Paper 4**  
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
