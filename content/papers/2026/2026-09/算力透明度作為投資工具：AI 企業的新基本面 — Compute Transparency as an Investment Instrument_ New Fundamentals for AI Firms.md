# 算力透明度作為投資工具：AI 企業的新基本面
## Compute Transparency as an Investment Instrument: New Fundamentals for AI Firms

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Paper 7 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

生成式 AI 企業正在進入高度資本密集的發展階段。模型能力、產品採用與營收仍然重要，但資料中心、GPU、CPU、網路、儲存、能源、冷卻與長期容量合約已逐漸成為企業成長速度、毛利結構與自由現金流的重要決定因素。2026 年大型科技公司的公開資訊已反覆顯示此趨勢：Microsoft 持續大幅增加 AI 與雲端資本支出，並公開新增 gigawatt 級容量、GPU／CPU 投資、throughput 效率改善與仍受供給約束的事實；Meta 將 2026 年資本支出預期提高至 1250–1450 億美元區間，並指出基礎設施是費用成長的主要來源之一；Amazon 報告自由現金流受 AI 相關 property and equipment 投資大幅增加所壓縮，而 AWS 與 AI 業務同時高速成長。這些揭露讓投資者知道「AI 很花錢、需求很強、容量仍在擴建」，卻尚未形成一套跨企業可比較的 **AI Compute Economics** 指標系統。

本文提出 **Compute Transparency as an Investment Instrument（算力透明度作為投資工具）**。其核心主張不是要求企業公開 GPU 清單、資料中心拓樸或商業敏感成本，而是將已經被企業內部用於容量管理的聚合營運資料轉化為投資者可理解、可比較、可長期追蹤的基本面訊號。

本文提出一組候選指標，包括 Compute Load Factor、Peak Utilization、Demand Coverage Ratio、Unserved Demand Ratio、Deferred Demand Ratio、Flexible Workload Ratio、Compute Yield、Compute Cost Intensity、Compute Gross Spread、Capacity Return on Capital、Throughput Efficiency Gain 與 Capacity Conversion Ratio。這些指標試圖回答傳統財報難以直接回答的問題：

> 一家公司新增的算力是否真的被需求吸收？

> 被吸收的算力是否創造足夠收入或產品價值？

> 需求成長是有效需求，還是被 rate limit 壓抑的潛在需求？

> 毛利下降究竟是 AI 產品不賺錢，還是企業正在提前建置未來容量？

> 同樣一美元 CapEx，不同企業能轉化出多少有效 throughput？

本文同時強調，這些指標不應被視為新的 GAAP 或 IFRS 會計科目，也不應直接取代營收、自由現金流、毛利、RPO、CapEx 與現金流量表。它們更接近航空業 load factor、雲端產業 utilization、能源市場容量與 SaaS 單位經濟等「產業特定營運指標」。真正有價值的制度不是公布一個神秘的「AI 算力分數」，而是建立：

$$
\boxed{
\text{Capital}
\rightarrow
\text{Capacity}
\rightarrow
\text{Usage}
\rightarrow
\text{Economic Output}
}
$$

的可觀測鏈。

本文進一步提出 **Disclosure Ladder**，區分使用者層、投資者層與內部層資訊，並討論選擇性揭露、可比性、估計誤差、跨業務歸因、競爭情報、Goodhart's Law 與審計問題。其核心命題為：

$$
\boxed{
\text{Operational compute transparency can become capital-market infrastructure when it links capacity to economic output.}
}
$$

亦即：

**當算力營運透明度能把容量與經濟產出連接起來時，它就不只是產品資訊，而可以成為資本市場基礎設施。**

**關鍵詞：** Compute Economics、AI CapEx、Compute Load Factor、Compute Yield、Capacity Return on Capital、Unserved Demand、AI 基本面、投資透明度、AI Infrastructure、資本市場

---

## 1. AI 投資分析正在遇到新的資訊缺口

傳統軟體公司的投資分析通常關注：

$$
\text{Revenue}
$$

$$
\text{ARR}
$$

$$
\text{Gross Margin}
$$

$$
\text{Retention}
$$

$$
\text{Operating Margin}
$$

$$
\text{Free Cash Flow}
$$

這些指標仍然重要。

但生成式 AI 公司與 AI 基礎設施供應商多了一個高度資本密集的中間層：

$$
\boxed{
\text{Compute Infrastructure}
}
$$

而這個中間層同時影響：

- 成長上限；
- 毛利；
- CapEx；
- 折舊；
- 能源成本；
- 產品可用性；
- API 價格；
- 推理速度；
- Agent 可擴張性；
- 客戶交付能力。

因此只看：

$$
\text{Revenue Growth}
$$

或：

$$
\text{CapEx Growth}
$$

都不足以單獨回答：

> 這些基礎設施投資到底產生了什麼？

---

## 2. 2026 年：資本支出已經成為 AI 敘事核心

2026 年的公開財務資訊已經非常清楚地顯示 AI 基礎設施投資的重要性。

Microsoft 在 FY2026 Q4 earnings call 中表示，單季增加約：

$$
1\ \mathrm{GW}
$$

容量，並持續推進兩年內大致倍增整體容量的計畫。

同一電話會議亦指出，Copilot workloads 的 throughput 自年初以來提升約：

$$
4\times
$$

而季度 CapEx 達：

$$
41\ \mathrm{billion\ USD}
$$

並在租賃會計調整後預期 calendar 2026 CapEx 約：

$$
175\ \mathrm{billion\ USD}
$$

。

更早的 FY2026 Q3 call 中，Microsoft 也明確表示，即使持續增加 GPU、CPU 與 storage capacity，預期至少整個 2026 年仍將受到容量約束。

這說明：

$$
\boxed{
\text{Demand}
+
\text{Capacity}
+
\text{Efficiency}
+
\text{CapEx}
}
$$

已經同時出現在大型 AI 公司的投資者敘事中。

---

## 3. 不只是 Microsoft

Meta 在 2026 Q2 將全年 CapEx 預期提高至：

$$
125\text{--}145\ \mathrm{billion\ USD}
$$

並說明增加部分與 component pricing 以及支援未來年份 capacity 的 data center 成本有關。

Amazon 在 2026 Q2 表示 AWS 銷售年增：

$$
37\%
$$

並達到約：

$$
169\ \mathrm{billion\ USD}
$$

annualized revenue run rate。

但同時，Amazon trailing-twelve-month free cash flow 轉為流出，主要原因之一是 property and equipment 投資同比大幅增加，而公司明確表示這主要反映 AI 投資。

因此投資者面對的是同一個新問題：

$$
\boxed{
\text{How much capital must be committed before AI demand becomes revenue and cash flow?}
}
$$

---

## 4. 傳統 CapEx 指標只能看到「投入」

假設企業本期 CapEx 為：

$$
K_t
$$

傳統財務可以清楚看到：

$$
K_t\uparrow
$$

但未必知道：

$$
\Delta C_{\mathrm{eff}}
$$

也就是這些資本究竟新增多少 **有效算力容量**。

即使知道新增：

$$
1\ \mathrm{GW}
$$

也仍然不知道：

- 有多少是推理；
- 有多少是訓練；
- 有多少是 R&D；
- 有多少是第一方產品；
- 有多少出售給雲端客戶；
- 有多少目前閒置；
- 有多少已被需求預約；
- 有多少容量被效率提升替代。

因此：

$$
\boxed{
\text{CapEx}
\neq
\text{Effective Compute Capacity}
}
$$

---

## 5. 容量也不等於經濟產出

即使企業公開：

$$
C_{\mathrm{eff}}
$$

仍然不夠。

如果大量新增容量處於：

$$
\text{idle}
$$

則投資效率可能很低。

相反地，如果：

$$
C_{\mathrm{eff}}
$$

沒有大幅增加，

但軟體、模型、routing、batching 與 silicon optimization 使 throughput 提升：

$$
4\times
$$

則同一物理資產可能創造更高經濟價值。

因此真正要追蹤的不是單一：

$$
\text{GPU Count}
$$

而是一條轉換鏈：

$$
\boxed{
K
\rightarrow
C_{\mathrm{physical}}
\rightarrow
C_{\mathrm{effective}}
\rightarrow
Q_{\mathrm{served}}
\rightarrow
V_{\mathrm{economic}}
}
$$

---

## 6. 第一個新基本面：Compute Load Factor

航空公司會追蹤 load factor，因為座位如果空著起飛，就失去了當期經濟價值。

AI capacity 並不完全等同航空座位，但具有相似的即時不可完全儲存性。

本文定義 **Compute Load Factor**：

$$
CLF
=
\frac{
\int_B S_{\mathrm{eff}}(t)\,dt
}{
\int_B C_{\mathrm{eff}}(t)\,dt
}
$$

其中：

- $S_{\mathrm{eff}}(t)$：實際被服務的有效算力工作量；
- $C_{\mathrm{eff}}(t)$：該期間可供服務的有效算力容量。

若：

$$
CLF\ll1
$$

可能表示容量閒置。

若：

$$
CLF\approx1
$$

可能表示效率很高，也可能表示容量過緊。

因此 CLF 必須與其他指標搭配。

---

## 7. 第二個基本面：Peak Utilization

定義：

$$
PU
=
\max_{t\in B}
\frac{
D_{\mathrm{eff}}(t)
}{
C_{\mathrm{eff}}(t)
}
$$

如果：

$$
PU>1
$$

代表某些時段需求超過可用容量。

這可能產生：

- rate limit；
- queue；
- rejection；
- latency spike；
- model substitution。

因此：

$$
CLF
$$

高而：

$$
PU
$$

低，可能代表平滑且高效利用。

但：

$$
CLF
$$

高且：

$$
PU\gg1
$$

則可能表示企業其實正在缺 capacity。

---

## 8. 第三個基本面：Demand Coverage Ratio

本文定義：

$$
DCR
=
\frac{
Q_{\mathrm{served}}
}{
Q_{\mathrm{requested}}
}
$$

其中：

$$
Q_{\mathrm{requested}}
=
Q_{\mathrm{served}}
+
Q_{\mathrm{denied}}
+
Q_{\mathrm{queued\ beyond\ tolerance}}
+
Q_{\mathrm{abandoned}}
$$

如果企業只公布成功 API calls：

$$
Q_{\mathrm{served}}
$$

投資者可能看不到：

$$
Q_{\mathrm{requested}}
$$

因此無法判斷：

> 成長慢是因為需求不足，還是因為供給不足？

---

## 9. 第四個基本面：Unserved Demand Ratio

定義：

$$
UDR
=
1-DCR
$$

或：

$$
UDR
=
\frac{
Q_{\mathrm{unserved}}
}{
Q_{\mathrm{requested}}
}
$$

這是一個非常重要的領先指標。

若：

$$
\text{Revenue}\uparrow
$$

且：

$$
UDR\uparrow
$$

可能表示企業還存在大量：

$$
\boxed{
\text{monetizable latent demand}
}
$$

但也可能表示產品體驗正在惡化。

因此 UDR 不是單純越高越好或越低越好。

它告訴投資者：

> 需求與供給之間還有多大的缺口。

---

## 10. 第五個基本面：Deferred Demand Ratio

如果使用者接受：

> 晚一點完成。

平台可以第一次識別：

$$
Q_{\mathrm{deferred}}
$$

定義：

$$
DDR
=
\frac{
Q_{\mathrm{deferred}}
}{
Q_{\mathrm{requested}}
}
$$

高 DDR 代表大量 workload 具有：

$$
\text{temporal elasticity}
$$

這對企業有很大價值。

因為：

$$
DDR\uparrow
$$

意味著企業不一定只能透過：

$$
C_{\mathrm{physical}}\uparrow
$$

處理需求。

也可以：

$$
\text{schedule demand}
$$

。

---

## 11. 第六個基本面：Flexible Workload Ratio

不是所有 deferred demand 都代表長期可調度。

因此再定義：

$$
FWR
=
\frac{
Q_{\mathrm{schedulable}}
}{
Q_{\mathrm{total}}
}
$$

其中 schedulable workload 是可以在指定 deadline 內移動時間而不明顯降低使用者價值的工作。

例如：

- batch；
- agent overnight；
- evaluation；
- indexing；
- background research；
- data processing。

若：

$$
FWR
$$

高，

企業就具有更大的：

$$
\boxed{
\text{Demand Management Option Value}
}
$$

---

## 12. Compute Yield

航空公司不只看 load factor，也看 yield。

AI 企業也需要知道一單位有效算力創造多少收入。

本文定義：

$$
CY
=
\frac{
R_{\mathrm{compute\ attributable}}
}{
Q_{\mathrm{served,eff}}
}
$$

其中：

$$
CY
$$

稱為 **Compute Yield**。

對純 API 企業，歸因較容易。

對廣告、訂閱或內嵌 AI 功能公司，則困難得多。

因此：

$$
\boxed{
\text{Compute Yield is easiest where monetization is directly metered.}
}
$$

---

## 13. Compute Cost Intensity

定義：

$$
CCI
=
\frac{
C_{\mathrm{compute\ operating}}
}{
R_{\mathrm{AI\ attributable}}
}
$$

其中成本可包括：

- 電力；
- 機房營運；
- GPU／CPU 折舊；
- 雲端租賃；
- 網路；
- 推理 runtime；
- 部分 storage。

如果：

$$
CCI\downarrow
$$

表示每一美元 AI 相關收入需要的 compute 成本降低。

但不同企業的成本分類不同，因此需要一致定義才可比較。

---

## 14. Compute Gross Spread

若能可靠估計：

$$
CY
$$

與每單位有效算力的邊際成本：

$$
MC_{\mathrm{compute}}
$$

則可定義：

$$
CGS
=
CY-MC_{\mathrm{compute}}
$$

稱為 **Compute Gross Spread**。

對 API-first 業務，它可以近似：

> 每單位有效算力創造多少毛利空間。

對 subscription bundle，則只能作為內部或估計指標。

---

## 15. Throughput Efficiency Gain

Microsoft 在 FY2026 Q4 公開 Copilot workloads throughput 自年初以來增加：

$$
4\times
$$

正好說明物理容量並不是唯一效率來源。

本文定義：

$$
TEG
=
\frac{
\mathrm{Throughput}_{t_1}/C_{\mathrm{physical},t_1}
}{
\mathrm{Throughput}_{t_0}/C_{\mathrm{physical},t_0}
}
-1
$$

如果：

$$
TEG>0
$$

代表同一單位物理基礎設施能處理更多有效工作。

來源可能包括：

- better silicon；
- quantization；
- batching；
- caching；
- routing；
- model architecture；
- compiler；
- networking；
- software stack。

---

## 16. Capacity Conversion Ratio

企業花：

$$
\Delta K
$$

新增多少有效 capacity？

定義：

$$
CCR_K
=
\frac{
\Delta C_{\mathrm{effective}}
}{
\Delta K
}
$$

這裡稱為 **Capacity Conversion Ratio**。

它回答：

> 每投入一美元基礎設施資本，最終形成多少新增有效吞吐能力？

但這個指標需要處理：

- 建設延遲；
- 資產壽命；
- 先行投資；
- 多業務共用；
- 土地與長期機房投資。

因此不能只做單季對單季比較。

---

## 17. Capacity Return on Capital

更進一步，可以定義長期：

$$
CROC
=
\frac{
\Delta NOPAT_{\mathrm{capacity\ attributable}}
}{
K_{\mathrm{capacity}}
}
$$

其中：

$$
CROC
$$

稱為 **Capacity Return on Capital**。

它不應被當作現成會計數字。

而是一個產業分析框架：

> 新增 capacity 最終創造了多少稅後營運報酬？

這比單純問：

> CapEx 很高是不是壞事？

更有判斷力。

---

## 18. 為什麼 CapEx 高不一定是壞消息

假設：

$$
K\uparrow
$$

傳統觀察會看到：

$$
FCF\downarrow
$$

但如果同時：

$$
Q_{\mathrm{requested}}\uparrow
$$

$$
UDR>0
$$

且新增 capacity 很快被吸收：

$$
CLF\uparrow
$$

那高 CapEx 可能代表：

$$
\boxed{
\text{profitable capacity expansion}
}
$$

相反地，如果：

$$
K\uparrow
$$

但：

$$
CLF\downarrow
$$

$$
CY\downarrow
$$

且需求沒有同步增加，

就可能形成過度建設。

所以：

$$
\boxed{
\text{CapEx needs a utilization context.}
}
$$

---

## 19. 為什麼毛利下降也不能單獨解讀

Microsoft FY2026 公開資料明確指出，AI infrastructure 投資與產品使用成長對 cloud gross margin percentage 造成壓力，同時 efficiency gains 又部分抵銷這些影響。

因此：

$$
\text{Gross Margin}\downarrow
$$

可能來自：

1. 推理單位經濟惡化；
2. 新容量提前建設；
3. 折舊增加；
4. 產品 mix 改變；
5. 高成長低毛利工作增加；
6. 使用量增加速度高於效率改善。

若沒有 compute metrics，投資者很難區分。

---

## 20. 一個更完整的 AI 基本面鏈

本文提出：

$$
\boxed{
\text{Demand}
\rightarrow
\text{Capacity}
\rightarrow
\text{Utilization}
\rightarrow
\text{Yield}
\rightarrow
\text{Margin}
\rightarrow
\text{Return}
}
$$

分別可以由：

$$
Q_{\mathrm{requested}}
$$

$$
C_{\mathrm{effective}}
$$

$$
CLF
$$

$$
CY
$$

$$
CGS
$$

$$
CROC
$$

描述。

這比：

> AI 很熱門，所以多買 GPU。

更接近完整企業分析。

---

## 21. Capacity Backlog

傳統企業會公布：

$$
RPO
$$

或 contract backlog。

AI capacity 還可以存在另一種 backlog：

$$
CB
=
Q_{\mathrm{committed}}
-
Q_{\mathrm{currently\ deliverable}}
$$

稱為 **Capacity Backlog**。

例如企業客戶已簽約，但 capacity 尚未上線。

這可以幫助判斷：

$$
\text{booked demand}
$$

與：

$$
\text{physical delivery capability}
$$

之間的時間差。

---

## 22. Demand-to-Capacity Coverage

定義：

$$
DCC
=
\frac{
C_{\mathrm{contracted/future}}
}{
D_{\mathrm{committed/future}}
}
$$

如果：

$$
DCC<1
$$

代表已知未來需求大於已知 capacity。

這不一定危險，因為 capacity 還會增加。

但對資本規劃具有價值。

---

## 23. Latent Demand 不應被當作收入

如果：

$$
UDR\uparrow
$$

投資者可能興奮地把所有 unserved demand 都視為未來 revenue。

這是錯的。

因為部分需求可能：

- 轉向競爭者；
- 消失；
- 被更便宜模型替代；
- 只是低價才存在；
- 因等待而放棄。

因此只能定義：

$$
Q_{\mathrm{latent}}
$$

而不是：

$$
R_{\mathrm{guaranteed}}
$$

並估計：

$$
p_{\mathrm{conversion}}
$$

。

---

## 24. Demand Quality

本文因此提出：

$$
DQ
=
f(
\text{willingness to pay},
\text{retention},
\text{deadline rigidity},
\text{repeat usage},
\text{contract commitment}
)
$$

也就是 **Demand Quality**。

同樣：

$$
100\ \mathrm{CU}
$$

未被服務，

企業客戶已簽約的 production workload，

與：

免費用戶隨手嘗試的 workload，

經濟意義完全不同。

---

## 25. Compute Yield 也有「質量」問題

一家公司可能用高價：

$$
CY\uparrow
$$

但因此需求很低：

$$
Q\downarrow
$$

另一家公司：

$$
CY\downarrow
$$

卻透過成本下降與規模：

$$
Q\uparrow\uparrow
$$

因此不能只最大化：

$$
CY
$$

應看：

$$
\text{Compute Contribution}
=
CGS\times Q
$$

更完整地寫為：

$$
CC
=
(CY-MC_{\mathrm{compute}})
Q_{\mathrm{served}}
$$

其中 $CC$ 表示 Compute Contribution。

---

## 26. 價格下降可能讓算力需求增加

AI 特別容易出現 rebound effect。

如果單位價格：

$$
P\downarrow
$$

Agent 可能從：

$$
10
$$

次推理，

變成：

$$
100
$$

甚至：

$$
1000
$$

次推理。

因此：

$$
\frac{\partial Q}{\partial P}<0
$$

可能非常大。

投資分析不能假設：

$$
Q=\text{constant}
$$

再單純推算成本下降。

---

## 27. AI 產品的經濟產出不一定等於直接收入

對 API：

$$
V_{\mathrm{economic}}
\approx
\text{Revenue}_{\mathrm{API}}
$$

相對容易。

但對廣告平台中的推薦 AI、企業內部 Copilot、搜尋 AI、客服 AI，算力可能透過：

- engagement；
- conversion；
- retention；
- labor savings；
- ad yield；
- churn reduction；

間接創造價值。

因此：

$$
\boxed{
\text{Compute Attribution}
}
$$

會成為重要方法論問題。

---

## 28. 三種歸因方式

### 28.1 Direct Metered Attribution

適用 API：

$$
R_{\mathrm{AI}}
=
\sum_i P_iQ_i
$$

### 28.2 Product-Level Attribution

比較：

$$
V_{\mathrm{with\ AI}}
-
V_{\mathrm{without\ AI}}
$$

例如 A/B test。

### 28.3 Portfolio Attribution

若 AI 已經深度嵌入整個產品，無法精確拆分，就只公布：

$$
\text{portfolio-level compute efficiency}
$$

而不製造虛假歸因。

---

## 29. 不應創造「AI Adjusted EBITDA 2.0」

新的產業指標有一個危險：

企業可能創造越來越多自訂數字，

最後讓投資者更難比較。

因此 Compute Metrics 必須滿足：

$$
\boxed{
\text{definition stability}
+
\text{reconciliation}
+
\text{comparability}
}
$$

如果企業公布：

$$
CLF
$$

就應固定說明：

- numerator；
- denominator；
- 是否含 training；
- 是否含 internal R&D；
- 是否含 third-party cloud；
- 是否含 reserved idle capacity。

否則毫無可比性。

---

## 30. 建議使用「指標家族」而不是單一分數

不應創造：

$$
\text{AI Health Score}=87.3
$$

然後試圖用一個數字概括所有經濟狀態。

更合理的是至少保留：

$$
\boxed{
\{
CLF,
PU,
DCR,
UDR,
FWR,
CY,
TEG,
CROC
\}
}
$$

因為它們回答不同問題。

單一分數很容易受到權重操縱。

---

## 31. Compute Load Factor 的合理區間也不是固定的

如果：

$$
CLF=95\%
$$

看似很好。

但若：

$$
PU=140\%
$$

且：

$$
UDR=20\%
$$

代表企業可能嚴重缺 capacity。

如果：

$$
CLF=70\%
$$

但企業正在提前建設下一代需求，

也不一定是低效率。

因此不存在：

$$
CLF=100\%
$$

必然最優。

這與電力、航空與雲端容量市場相同：

需要 buffer。

---

## 32. Reliability Reserve

企業必須保留：

$$
R_C
=
C_{\mathrm{effective}}
-
D_{\mathrm{expected}}
$$

稱為 **Reliability Reserve**。

若：

$$
R_C\approx0
$$

任何 demand shock 都可能造成服務下降。

因此投資者不應把所有 idle capacity 視為浪費。

部分 idle 是：

$$
\boxed{
\text{reliability inventory}
}
$$

。

---

## 33. Flexible Workload Ratio 可以降低所需 Reserve

如果：

$$
FWR\uparrow
$$

企業可以在 shock 發生時移動更多需求。

因此理論上：

$$
R_C^{\mathrm{required}}\downarrow
$$

這使 Demand Engineering 直接進入資本效率。

也就是：

$$
\boxed{
\text{Demand Flexibility}
\rightarrow
\text{Lower Capacity Insurance Cost}
}
$$

---

## 34. Capacity Flexibility Premium

若一家公司大量 workload 可以：

- batch；
- flex；
- shift region；
- shift model；
- delay；
- surrender；

則其資本需求的剛性可能低於另一家公司。

本文稱這個價值為：

$$
\boxed{
\text{Capacity Flexibility Premium}
}
$$

它不是直接會計資產，

但可能影響：

$$
CROC
$$

與資本市場風險評價。

---

## 35. 透明度為什麼可能降低資本成本

投資者面對未知：

$$
\sigma_{\mathrm{information}}\uparrow
$$

通常要求更高：

$$
\text{Risk Premium}
$$

如果企業能穩定提供：

- capacity growth；
- utilization；
- unserved demand；
- throughput efficiency；
- margin conversion；

則：

$$
\sigma_{\mathrm{information}}\downarrow
$$

理論上可能：

$$
\text{Cost of Capital}\downarrow
$$

但這不是保證。

如果透明度揭露企業效率很差，

市場也可能降低估值。

因此：

$$
\boxed{
\text{Transparency improves price discovery, not necessarily price.}
}
$$

---

## 36. 這一點非常重要：透明度不是公關工具

若企業把 compute metrics 只當作：

> 找一個漂亮數字給投資人看。

制度很快會失效。

真正有價值的是：

$$
\text{same metric}
$$

同時被：

- operations；
- product；
- finance；
- investors；

使用。

即：

$$
\boxed{
\text{one telemetry base, multiple decision surfaces}
}
$$

而不是營運團隊看一套、投資人看另一套故事。

---

## 37. 使用者、企業與投資人的同源資料

Paper 6 的 Capacity Transparency 可以給使用者：

$$
CLI(t)
$$

企業內部則看到：

$$
D(t),C(t),\hat D(t+\tau)
$$

投資者不需要即時資料，

但可以看到季度聚合：

$$
CLF_Q
$$

$$
PU_Q
$$

$$
UDR_Q
$$

$$
FWR_Q
$$

這三層來自同一 telemetry。

因此：

$$
\boxed{
\text{Product Transparency}
+
\text{Operational Transparency}
+
\text{Investor Transparency}
}
$$

可以共享一套資料架構。

---

## 38. Disclosure Ladder

本文提出三層揭露。

### Layer 1：Public Product

公開：

- Low／Normal／Busy；
- 預估延遲；
- 折扣窗口。

### Layer 2：Investor Aggregate

季度或年度公開：

- capacity growth band；
- CLF；
- UDR；
- FWR；
- TEG；
- selected unit economics。

### Layer 3：Internal Exact

只供企業內部：

- exact fleet；
- exact model routing；
- exact power；
- exact unit cost；
- supplier terms；
- geographic bottlenecks。

這使：

$$
\text{transparency}
$$

不必等於：

$$
\text{trade secret disclosure}
$$

。

---

## 39. 為什麼不應公開精確 GPU 數量作為主指標

不同 GPU：

$$
G_1\neq G_2
$$

不同軟體 stack：

$$
S_1\neq S_2
$$

相同 GPU 數量產生的有效 throughput 可能不同：

$$
C_{\mathrm{eff},1}
\neq
C_{\mathrm{eff},2}
$$

因此：

$$
\boxed{
\text{GPU Count}
}
$$

更像投入指標，

不是最終產出指標。

投資者真正需要的是：

$$
\text{Effective Throughput}
$$

與：

$$
\text{Economic Conversion}
$$

。

---

## 40. 能源也可以成為基本面的一部分

AI compute 最終受：

$$
\text{Power}
$$

限制。

可以定義：

$$
EPI
=
\frac{
E_{\mathrm{energy}}
}{
Q_{\mathrm{served,eff}}
}
$$

稱為 **Energy per Effective Compute**。

若：

$$
EPI\downarrow
$$

代表每單位有效工作需要更少能源。

還可以公布：

$$
F_{\mathrm{shiftable}}
$$

表示可因能源或電網條件移動的 workload 比例。

這對長期資料中心成本與能源風險都有價值。

---

## 41. 但能源指標也需要邊界

如果企業只公布：

$$
\text{renewable percentage}
$$

卻不說：

- location-based；
- market-based；
- hourly matched；
- annual offset；

投資者很難比較。

同樣地，Compute Metrics 若沒有邊界定義，也會失去意義。

所以：

$$
\boxed{
\text{metric governance}
}
$$

與指標本身同樣重要。

---

## 42. Goodhart's Law

一旦：

$$
CLF
$$

成為市場重視指標，

企業可能故意壓縮 spare capacity，

使：

$$
CLF\uparrow
$$

卻讓 reliability 下降。

若：

$$
UDR
$$

被重視，

企業可能改變 logging 規則，

讓 denominator 變小。

因此：

$$
\boxed{
\text{when a measure becomes a target, it can cease to be a good measure}
}
$$

這正是為什麼需要：

$$
\text{metric family}
$$

而非單一 KPI。

---

## 43. 指標必須可重述與回溯

如果企業修改：

$$
C_{\mathrm{effective}}
$$

的定義，

應提供：

$$
\text{historical restatement}
$$

或者至少：

$$
\text{bridge}
$$

說明舊指標與新指標如何轉換。

否則投資者無法做：

$$
t_0\leftrightarrow t_1
$$

長期比較。

---

## 44. 審計與第三方驗證

真正成熟後，部分 Compute Metrics 可能需要：

$$
\text{assurance}
$$

例如第三方驗證：

- telemetry sampling；
- capacity definitions；
- reconciliation；
- exclusions；
- estimation methodology。

不一定需要財報等級審計，

但至少要避免：

$$
\text{self-defined unauditable marketing metric}
$$

。

---

## 45. 估值模型如何使用這些資料

傳統 DCF：

$$
V
=
\sum_t
\frac{
FCF_t
}{
(1+r)^t
}
$$

不需要被替換。

Compute Metrics 的價值在於改善：

$$
FCF_t
$$

的假設。

例如：

$$
\text{Revenue}_t
=
f(
Q_{\mathrm{served}},
CY
)
$$

而：

$$
Q_{\mathrm{served}}
=
f(
C_{\mathrm{effective}},
CLF,
DCR
)
$$

CapEx 則：

$$
K_t
=
f(
D_{\mathrm{future}},
FWR,
TEG,
\text{Reliability Reserve}
)
$$

於是營運資料可以進入傳統估值模型，而不是另創一套神秘估值學。

---

## 46. 一個簡化的 AI Infrastructure Driver Model

可以寫成：

$$
D_t
\rightarrow
C_t
\rightarrow
Q_t
\rightarrow
R_t
\rightarrow
FCF_t
$$

其中：

$$
Q_t
=
C_t\cdot CLF_t\cdot DCR_t
$$

簡化收入：

$$
R_t
=
Q_t\cdot CY_t
$$

簡化 compute contribution：

$$
CC_t
=
Q_t
(
CY_t-MC_t
)
$$

而新增 capacity：

$$
\Delta C_{t+1}
=
CCR_K\cdot K_t
+
\Delta C_{\mathrm{efficiency}}
$$

這讓：

$$
\text{CapEx}
$$

第一次與：

$$
\text{throughput}
$$

直接接上。

---

## 47. Throughput Efficiency 可以抵銷 CapEx

如果：

$$
TEG\uparrow
$$

企業可能在不同比例的物理擴建下：

$$
C_{\mathrm{effective}}\uparrow
$$

因此：

$$
\boxed{
\text{software optimization}
}
$$

具有類似「虛擬 CapEx」的經濟效果。

這也是為什麼 Microsoft 公開 throughput 4 倍提升這類資訊對投資者很有意義。

它說明：

> 不只是買更多硬體，也在讓既有硬體做更多工作。

---

## 48. AI 公司可以建立 Compute Bridge

每季提供一個類似財務 bridge：

$$
C_{t-1}
+
\Delta C_{\mathrm{hardware}}
+
\Delta C_{\mathrm{software}}
-
\Delta C_{\mathrm{retired}}
=
C_t
$$

再接：

$$
C_t
\rightarrow
Q_{\mathrm{served}}
\rightarrow
R_{\mathrm{AI}}
$$

這會比單純公布：

> 我們今年投資很多 AI infrastructure。

更有分析價值。

---

## 49. 投資人真正想知道的六個問題

這套制度最終可以濃縮成六個問題。

### 一

$$
\text{Demand Growth?}
$$

需求到底增長多少？

### 二

$$
\text{Capacity Growth?}
$$

有效 capacity 增長多少？

### 三

$$
\text{Utilization?}
$$

新增 capacity 有沒有被用掉？

### 四

$$
\text{Efficiency?}
$$

單位硬體 throughput 有沒有提升？

### 五

$$
\text{Yield?}
$$

每單位 compute 產生多少經濟價值？

### 六

$$
\text{Return?}
$$

這些投資最終產生什麼資本報酬？

如果企業能回答這六題，

AI CapEx 就不再只是黑箱。

---

## 50. 可測試假說

### H1：Compute Metrics 可以降低 CapEx 解讀的不確定性

若企業公開：

$$
CLF
+
UDR
+
TEG
$$

投資者對：

$$
K_t
$$

的解讀分歧可能下降。

---

### H2：高 UDR 與高 CLF 的組合比單純高 CapEx 更能預測未來容量擴張

因為：

$$
UDR\uparrow
$$

代表存在未滿足需求，

而：

$$
CLF\uparrow
$$

代表現有 capacity 已高度使用。

---

### H3：FWR 高的企業需要較低的 peak reserve

預期：

$$
FWR\uparrow
\Rightarrow
R_C^{\mathrm{required}}\downarrow
$$

在其他條件相近時成立。

---

### H4：TEG 改善可以部分抵銷 CapEx 強度

若：

$$
TEG\uparrow
$$

則：

$$
\frac{K}{Q_{\mathrm{served}}}
\downarrow
$$

可能成立。

---

### H5：透明度可以降低資本成本，但效果不是單向

若透明度揭露優秀營運：

$$
\text{Risk Premium}\downarrow
$$

可能發生。

若揭露效率差：

估值也可能下降。

因此真正效果是：

$$
\text{price discovery}\uparrow
$$

而非：

$$
\text{Price}\uparrow
$$

。

---

## 51. 實驗與實務路線

企業不需要一次公布完整 Compute Economics。

可以分階段。

### Phase A：Internal Standardization

先建立統一：

$$
C_{\mathrm{effective}}
$$

與 workload classification。

### Phase B：Customer Transparency

公開：

$$
CLI
$$

與 capacity bands。

### Phase C：Investor Pilot

季度公布：

$$
\text{Capacity Growth}
+
TEG
+
\text{Selected Utilization}
$$

### Phase D：Metric Family

再逐步加入：

$$
UDR
+
FWR
+
CY
+
CROC
$$

### Phase E：External Assurance

成熟後提供第三方驗證。

---

## 52. 哪些資訊不建議公開

本文並不建議公開：

- exact live GPU count；
- rack topology；
- exact data center spare power；
- exact region weakness；
- supplier-specific unit costs；
- security reserve；
- proprietary routing algorithm；
- per-customer capacity；
- sensitive contract economics。

這些資訊的：

$$
C_{\mathrm{disclosure}}
$$

可能高於：

$$
V_{\mathrm{investor}}
$$

。

---

## 53. 哪些資訊可能值得公開

較適合作為投資者指標的包括：

$$
\boxed{
\text{capacity growth band}
}
$$

$$
\boxed{
\text{throughput efficiency growth}
}
$$

$$
\boxed{
CLF
}
$$

$$
\boxed{
UDR
}
$$

$$
\boxed{
FWR
}
$$

$$
\boxed{
\text{compute cost intensity trend}
}
$$

以及：

$$
\boxed{
\text{capacity return trend}
}
$$

重點是：

$$
\text{trend}
$$

有時比：

$$
\text{exact level}
$$

更有價值，也更少洩漏商業機密。

---

## 54. 與目前投資者揭露的關係

今天大型科技企業已經會公開：

- Cloud revenue；
- AI revenue run rate；
- RPO／backlog；
- CapEx；
- gross margin；
- free cash flow；
- capacity constraint commentary；
- GPU／CPU 投資；
- gigawatt 級建設；
- throughput efficiency improvements。

因此本文不是主張從零開始發明一套完全陌生的披露制度。

而是把這些目前散落的資訊：

$$
\boxed{
\text{standardize}
+
\text{connect}
+
\text{make comparable}
}
$$

。

---

## 55. 從財報故事轉成算力經濟模型

現在企業可能分別說：

> demand 很強。

> CapEx 很高。

> capacity 很緊。

> throughput 提升。

> gross margin 受到 AI 投資壓力。

這些都是真的，

但投資者必須自己拼圖。

本文希望的制度是：

$$
\boxed{
\text{Demand}
\rightarrow
\text{Capacity}
\rightarrow
\text{Utilization}
\rightarrow
\text{Efficiency}
\rightarrow
\text{Economics}
}
$$

直接連成一條。

這才是 AI 企業的新基本面。

---

## 56. 基本原則

本文提出十三項原則。

### 原則一：AI CapEx 必須與有效 capacity 連接

$$
K
\rightarrow
C_{\mathrm{effective}}
$$

### 原則二：Effective Capacity 必須與 Usage 連接

$$
C_{\mathrm{effective}}
\rightarrow
Q_{\mathrm{served}}
$$

### 原則三：Usage 必須與 Economic Output 連接

$$
Q_{\mathrm{served}}
\rightarrow
V_{\mathrm{economic}}
$$

### 原則四：不只看 utilization，也看 unmet demand

$$
CLF
+
UDR
$$

應同時觀察。

### 原則五：不只看硬體，也看 throughput efficiency

$$
TEG
$$

可以產生類似新增 capacity 的效果。

### 原則六：保留 Reliability Reserve

Idle 不必然等於浪費。

### 原則七：FWR 是一種資本效率資產

需求彈性可以降低 peak reserve。

### 原則八：不創造單一 AI 健康分數

使用 metric family。

### 原則九：指標定義必須固定與可回溯

避免不可比較。

### 原則十：透明度提高的是 price discovery

不是保證提高估值。

### 原則十一：投資者層只需要聚合資料

不用公開基礎設施秘密。

### 原則十二：營運、產品與投資者應共享同源 telemetry

$$
\text{one telemetry base}
$$

### 原則十三：Compute Metrics 是產業指標，不是替代財務報表

它們應補充：

$$
GAAP/IFRS
$$

而不是取代。

---

## 57. 限制

第一，本文提出的 CLF、UDR、FWR、CY、CROC 等均為候選產業指標，不是目前普遍採用的會計標準。

第二，AI 企業的 workload 異質性極高，跨企業比較需要共同的 normalized effective compute 定義。

第三，第一方產品與內部 R&D 的經濟價值歸因非常困難。

第四，不同公司可能同時使用自有資料中心與第三方雲端，使 capacity attribution 複雜。

第五，企業可能透過定義調整使指標看起來更好，因此需要 metric governance。

第六，公開過多資訊可能產生競爭、資安與策略風險。

第七，投資者不應把任何單一 compute metric 直接當作買賣證券的充分依據。

---

## 58. 結論

AI 企業的資本市場問題正在改變。

在純軟體時代，投資者可以相對直接地從：

$$
\text{Revenue}
\rightarrow
\text{Margin}
\rightarrow
FCF
$$

理解企業。

AI 時代中間多出一個巨大且高度動態的層：

$$
\boxed{
\text{Compute Economy}
}
$$

企業必須先：

$$
K
$$

投入資本，

形成：

$$
C_{\mathrm{effective}}
$$

再由：

$$
Q_{\mathrm{requested}}
$$

轉化成：

$$
Q_{\mathrm{served}}
$$

最後才可能形成：

$$
\text{Revenue}
$$

與：

$$
FCF
$$

。

因此，當 CapEx 已經進入千億美元級，而企業又公開表示 capacity constraint、gigawatt 級擴張與 throughput efficiency improvements 時，只公布：

> 我們持續投資 AI。

已經逐漸不足以完整描述企業基本面。

更成熟的揭露應該建立：

$$
\boxed{
\text{Capital}
\rightarrow
\text{Capacity}
\rightarrow
\text{Usage}
\rightarrow
\text{Economic Output}
}
$$

的可觀測鏈。

這不要求企業公開完整 GPU fleet。

也不要求投資者成為資料中心工程師。

真正需要的是：

$$
\boxed{
\text{decision-useful investor transparency}
}
$$

例如：

> 本季有效 capacity 增加多少？

> throughput efficiency 提升多少？

> 現有 capacity 有多少被吸收？

> 有多少需求仍未服務？

> 有多少 workload 可以移到離峰？

> 每一單位新增 capacity 最終帶來多少經濟產出？

當這些問題可以用穩定、可比較、可回溯的指標回答，透明度就不再只是公關負擔。

它會成為：

$$
\boxed{
\text{capital allocation infrastructure}
}
$$

。

因此，本篇的核心命題為：

$$
\boxed{
\text{Operational compute transparency can become capital-market infrastructure when it links capacity to economic output.}
}
$$

中文即：

**當算力營運透明度能把容量與經濟產出連接起來時，它就不只是產品資訊，而可以成為資本市場基礎設施。**

而當 AI 算力開始同時具有：

- 可計價；
- 可調度；
- 可預約；
- 可返還；
- 可觀測；
- 可形成投資指標；

下一個問題就不再只是產品設計。

而是：

> 這是否正是一個新型市場從商品化、分層、套利、標準化走向制度化的典型過程？

這正是下一篇：

**AI 市場的制度演化：從商品化到容量市場。**

---

## 參考資料

1. Microsoft Investor Relations. *Microsoft Fiscal Year 2026 Fourth Quarter Earnings Conference Call.* 2026-07-29.  
   https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4

2. Microsoft Investor Relations. *Microsoft Fiscal Year 2026 Third Quarter Earnings Conference Call.* 2026-04-29.  
   https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3

3. Microsoft Investor Relations. *FY26 Q3 — Performance.* Accessed 2026-09-07.  
   https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q3/performance

4. Microsoft Investor Relations. *Fiscal Year 2027 Segments and Investor Metrics.* Announced 2026-09-02.  
   https://www.microsoft.com/en-us/investor/

5. Meta Investor Relations. *Meta Reports Second Quarter 2026 Results.* 2026-07-29.  
   https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/

6. Meta Investor Relations. *Meta Reports First Quarter 2026 Results.* 2026.  
   https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-First-Quarter-2026-Results/

7. Amazon Investor Relations. *Amazon.com Announces Second Quarter Results.* 2026-07-30.  
   https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx

8. Amazon Investor Relations. *Amazon.com Announces First Quarter Results.* 2026.  
   https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx

9. Alphabet Investor Relations. *2025 Q4 Earnings Call.* 2026-02-04.  
   https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx

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

**Paper 6**  
算力透明度作為控制介面：從黑箱限流到容量可觀測市場

**Paper 7 — 本篇**  
算力透明度作為投資工具：AI 企業的新基本面

**Paper 8 — Next**  
AI 市場的制度演化：從商品化到容量市場

**Extra 1**  
Token 消耗症候群：到期額度如何反向塑造人的認知行為

**Extra 2**  
跨產業制度移植：AI 產業其實不用每件事重新發明
