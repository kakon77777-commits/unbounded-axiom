# AI 市場的制度演化：從商品化到容量市場
## Institutional Evolution of AI Markets: From Commodification to Capacity Markets

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Paper 8 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

生成式 AI 產業的商業制度仍處於快速學習階段。模型能力、Agent、記憶、搜尋、多模態與長程執行的技術演進速度，遠快於定價、使用權、容量調度、跨產品資源配置與投資揭露制度的成熟速度。由此產生一系列看似分散的現象：固定月訂閱與短週期 Rate Limit 並存、API 與訂閱割裂、未用額度失效、訂閱轉 API 的灰色套利、Flex／Batch／Priority／Reserved 等服務層出現、需求響應與離峰折扣逐漸具有經濟合理性，以及投資者開始面對巨額 AI CapEx 卻缺乏標準化 Compute Economics 指標。

本文主張，這些現象不應被視為彼此孤立的產品問題，而可以被理解為一個新型稀缺資源市場在進行典型的制度演化。其大致路徑可抽象為：

$$
\boxed{
\text{Scarcity}
\rightarrow
\text{Commodification}
\rightarrow
\text{Segmentation}
\rightarrow
\text{Arbitrage}
\rightarrow
\text{Formalization}
\rightarrow
\text{Standardization}
\rightarrow
\text{Capacity Market}
\rightarrow
\text{Financialization}
}
$$

本文並不主張此路徑必然、單向或自動導向最優結果。更精確地說，它是一組在資本主義市場中反覆出現的制度壓力：當某種資源開始具有高經濟價值、異質需求、有限供給、時間敏感性與可測量性時，市場參與者就會嘗試細分權利、建立價格、套利差異、形成新合約、導入標準、增加透明度，並在部分情況下發展出預約、遠期、容量與二級市場。

電力市場、雲端運算與 AI 推理已經提供清楚的結構類比。電力市場不只交易實際產出的能源，也存在容量市場，支付資源在未來需要時可提供電力或減少需求的能力；Demand Response 可以因減少尖峰使用而獲得補償。AWS 將計算服務拆分為 On-Demand、Reserved、Spot、Savings Plans 與 Capacity Reservation；Amazon Bedrock 已將推理分為 Reserved、Priority、Standard 與 Flex；OpenAI Reserved Tier 則直接讓企業預購峰值期間的 provisioned throughput。這些機制顯示，當資源具有容量限制與時間價值時，市場會逐步把「使用多少」「何時使用」「是否保證可用」「可以等待多久」拆成不同商品。

本文整合前七篇提出的四時鐘分離、Temporal Fungibility、Compute Wallet、Reversible Entitlement、Demand Engineering、Compute Transparency 與 Investor Compute Fundamentals，提出 **Adaptive AI Compute Market** 作為制度成熟方向。其核心不是把 AI 智能完全金融化，也不是主張所有訂閱額度都應自由交易，而是將 AI 服務中的：

$$
\text{Access}
,\quad
\text{Compute}
,\quad
\text{Time}
,\quad
\text{Priority}
,\quad
\text{Capacity}
,\quad
\text{Risk}
$$

逐步從模糊訂閱福利拆分為可治理、可計價、可調度且可觀測的權利。

本文的核心命題為：

$$
\boxed{
\text{AI competition is evolving from model competition toward institutional competition over how intelligence is allocated.}
}
$$

中文即：

**AI 產業的競爭正在從單純的模型競爭，逐步延伸為「智能資源如何被配置」的制度競爭。**

**關鍵詞：** AI 市場、資本主義演化、商品化、套利、容量市場、Compute Economy、制度經濟學、Demand Response、AI 訂閱、AI 基礎設施

---

## 1. 從最初問題重新開始

整個系列最初可以從一個極其日常的問題開始：

> 我買了 AI 訂閱，但這個月沒用完，為什麼剩下的不能給別人？

乍看之下，這只是：

$$
\text{subscription UX}
$$

問題。

但一旦往下追問，就會遇到：

> 為什麼月額度不能集中在五天使用？

> 為什麼 API 與完整產品要被完全分開？

> 為什麼未用權利只能失效？

> 為什麼供應商不能買回未來使用權？

> 為什麼算力緊張只能 Rate Limit？

> 為什麼不能離峰打折？

> 為什麼不公開容量訊號？

> 為什麼投資者看不到算力利用效率？

這些問題最後指向同一個制度核心：

$$
\boxed{
\text{What exactly is being sold when an AI company sells intelligence access?}
}
$$

---

## 2. 第一階段：先有產品，再有制度

新技術市場通常不是先有完美制度，再有商品。

而是：

$$
\text{Technology}
\rightarrow
\text{Product}
\rightarrow
\text{Usage}
\rightarrow
\text{Institutional Friction}
$$

生成式 AI 早期最重要的問題是：

> 模型能不能工作？

> 能不能讓幾百萬、幾億人使用？

因此最容易理解的價格是：

$$
P_{\mathrm{month}}
$$

或：

$$
P_{\mathrm{token}}
$$

這是合理的早期簡化。

---

## 3. Institutional Lag

技術能力可以快速變化：

$$
\text{Chat}
\rightarrow
\text{Reasoning}
\rightarrow
\text{Multimodal}
\rightarrow
\text{Agent}
\rightarrow
\text{Long-Running Work}
$$

但契約、定價、權利與市場規則的演化速度較慢。

因此可以定義：

$$
L_I
=
M_{\mathrm{technical}}
-
M_{\mathrm{institutional}}
$$

其中：

- $M_{\mathrm{technical}}$：技術成熟度；
- $M_{\mathrm{institutional}}$：制度成熟度；
- $L_I$：Institutional Lag。

當：

$$
L_I\uparrow
$$

就會出現大量「技術已經能做，但產品規則還沒跟上」的摩擦。

---

## 4. AI 並不是單純 SaaS

如果 AI 只是普通 SaaS：

$$
P
=
N_{\mathrm{seat}}
\cdot
P_{\mathrm{seat}}
$$

就已經足夠。

但 AI 同時具有：

$$
\boxed{
\text{Software}
+
\text{Cloud Compute}
+
\text{Energy-Like Capacity}
+
\text{Knowledge Service}
}
$$

其邊際成本可能：

$$
\frac{\partial C}{\partial Q}>0
$$

而且在特定時間：

$$
C(t)
$$

有限。

因此 AI 無法完全套用傳統「多一個使用者成本近乎零」的 SaaS 想像。

---

## 5. AI 也不是普通大宗商品

另一方面，AI Compute 也不是石油、黃金或小麥。

其有效價值取決於：

$$
V
=
f(
\text{model capability},
\text{latency},
\text{context},
\text{tools},
\text{quality},
\text{deadline}
)
$$

同樣：

$$
100\ \mathrm{CU}
$$

在不同模型與時段並不必然具有相同經濟價值。

因此：

$$
\boxed{
\text{AI Compute is a heterogeneous service commodity.}
}
$$

---

## 6. 第一個演化步驟：Commodification

當智能服務可以被重複提供、計價與大規模銷售時，會逐步形成：

$$
\text{Intelligence Access}
\rightarrow
\text{Economic Commodity}
$$

這裡的 commodity 並不表示所有模型完全同質。

而是指：

> 智能能力第一次可以透過市場規則反覆購買。

例如：

$$
\text{subscription}
$$

或：

$$
\text{API usage}
$$

。

---

## 7. 商品化之後自然出現異質需求

使用者並不相同。

可以表示為：

$$
\mathcal U
=
\{
U_{\mathrm{light}},
U_{\mathrm{steady}},
U_{\mathrm{burst}},
U_{\mathrm{enterprise}},
U_{\mathrm{agent}}
\}
$$

其需求：

$$
D_i(t)
$$

價格彈性：

$$
\epsilon_i
$$

與 deadline：

$$
\delta_i
$$

都不同。

因此單一商品會自然被分層。

---

## 8. 第二個演化步驟：Segmentation

市場開始提供：

$$
\text{Free}
$$

$$
\text{Plus}
$$

$$
\text{Pro}
$$

$$
\text{Business}
$$

$$
\text{Enterprise}
$$

以及：

$$
\text{Standard}
,\quad
\text{Fast}
,\quad
\text{Flex}
,\quad
\text{Batch}
,\quad
\text{Reserved}
$$

這就是：

$$
\boxed{
\text{Market Segmentation}
}
$$

經濟學上，它也涉及不同程度的價格歧視與產品差異化。

---

## 9. 分層本身會創造價差

只要市場中存在：

$$
P_A\neq P_B
$$

與：

$$
\text{rights}_A\neq \text{rights}_B
$$

就會產生：

$$
\boxed{
\text{conversion incentive}
}
$$

例如：

$$
P_{\mathrm{subscription,eff}}
<
P_{\mathrm{API}}
$$

使用者自然會問：

> 能不能把 subscription 轉成 API？

這就是套利的起點。

---

## 10. 第三個演化步驟：Arbitrage

套利不是 AI 特有現象。

一般形式是：

$$
\boxed{
\text{Institutional Difference}
+
\text{Price Difference}
\rightarrow
\text{Arbitrage}
}
$$

如果兩套制度對同一底層能力給出不同價格，

市場參與者就有動機建立：

$$
A\rightarrow B
$$

的橋。

---

## 11. 訂閱轉 API 是制度訊號

非官方訂閱中轉可以被視為：

$$
\text{Contract Boundary Violation}
$$

但同時也是：

$$
\boxed{
\text{Unmet Fungibility Signal}
}
$$

即市場中確實存在：

> 我希望完整產品與 API 資源更可互換。

這不代表供應商必須接受非官方轉售。

而是表示企業可以進一步問：

> 這個需求的哪一部分值得被官方產品化？

---

## 12. 第四個演化步驟：Formalization

當灰色市場或 workaround 持續出現，

供應商通常有兩種反應：

$$
\text{Suppress}
$$

或：

$$
\text{Internalize}
$$

Suppress：

> 封鎖轉售。

Internalize：

> 提供官方 Wallet、Overage、Transfer、Gift、Flex。

成熟制度往往兩者同時存在：

$$
\boxed{
\text{ban unsafe conversion}
+
\text{productize legitimate demand}
}
$$

---

## 13. 正式化不等於放任

官方化的價值在於重新取得：

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
\text{fraud detection}
$$

因此：

$$
\boxed{
\text{formal market}
\neq
\text{unrestricted market}
}
$$

。

---

## 14. Compute Wallet 是正式化工具

Paper 3 提出：

$$
\boxed{
\text{Compute Wallet}
}
$$

其制度角色正是：

$$
\text{informal fungibility demand}
\rightarrow
\text{provider-governed fungibility}
$$

讓：

$$
\text{Subscription}
\leftrightarrow
\text{Usage}
$$

之間不再完全割裂。

---

## 15. 第五個演化步驟：Standardization

市場要真正成熟，就需要共同語言。

今天 Token 看似標準單位，

但：

$$
1\text{ token}
\neq
1\text{ unit of economic compute}
$$

因此未來需要：

$$
\boxed{
\text{Normalized Effective Compute}
}
$$

或其他可比較抽象。

---

## 16. 標準化不代表所有公司使用相同內部模型

企業內部可以：

$$
C_A(x)
\neq
C_B(x)
$$

但外部市場可以逐步形成可比較：

$$
\phi_A(C_A)
$$

與：

$$
\phi_B(C_B)
$$

。

就像：

不同航空公司飛機不同，

仍能比較：

$$
\text{load factor}
$$

。

---

## 17. 第六個演化步驟：Time Differentiation

當市場成熟後，

不再只問：

> 使用多少？

開始問：

> 什麼時候使用？

因此：

$$
\text{Compute}
\rightarrow
(
Q,t,\ell,\delta,p
)
$$

其中：

- $Q$：quantity；
- $t$：execution time；
- $\ell$：latency；
- $\delta$：deadline；
- $p$：priority。

---

## 18. 雲端市場已經高度時間化

AWS Capacity Reservations 即使沒有實際執行 instance，仍會對預留而未使用的 capacity 收費。

這表示：

$$
\boxed{
\text{availability itself has economic value}
}
$$

。

Reserved Instance、Savings Plans 與 Spot 也分別處理：

- 承諾；
- 折扣；
- 中斷風險；
- 容量保證。

AI 推理正在往相同方向發展。

---

## 19. AI 推理已有服務層市場

Amazon Bedrock 已提供：

$$
\{
\text{Reserved},
\text{Priority},
\text{Standard},
\text{Flex}
\}
$$

。

OpenAI Reserved Tier 則允許企業預購 specific model 的 provisioned throughput，並將其作為 rate limit 之外、峰值仍可使用的增量容量。

這意味著：

$$
\boxed{
\text{AI capacity has already become a separately purchasable right.}
}
$$

---

## 20. 從 Usage Market 到 Capacity Market

Usage market 交易的是：

$$
\text{work actually executed}
$$

Capacity market 交易的是：

$$
\boxed{
\text{ability or commitment to serve future work}
}
$$

這個區分在電力市場中非常成熟。

FERC 對 capacity market 的說明正是：

> 支付的是未來需要時可供應能力，而不是當下產出的能源本身。

AI 也可能出現類似結構：

$$
\text{Inference Usage}
$$

與：

$$
\text{Reserved Inference Capacity}
$$

分離。

---

## 21. 電力市場是非常重要的類比

電力具有：

$$
\text{instantaneous balance constraint}
$$

供需必須持續平衡。

AI Compute 雖然不像電力那麼嚴格，

但在特定時刻仍有：

$$
D(t)\leq C(t)
$$

的容量限制。

因此很多電力市場制度具有移植價值。

---

## 22. Energy Market 與 Capacity Market

電力市場中：

$$
\text{Energy Market}
$$

支付實際產出的：

$$
\mathrm{MWh}
$$

。

Capacity Market 則支付：

$$
\text{ability to be available}
$$

。

AI 對應：

$$
\text{Usage Pricing}
$$

支付實際 inference。

而：

$$
\text{Reserved Capacity}
$$

支付可確保未來 inference 能力。

---

## 23. Demand Response 的重要性

FERC 的 Demand Response 制度允許需求端透過：

$$
\text{reduce consumption during peak}
$$

成為可補償資源。

AI 也可以：

$$
\text{User Surrender}
$$

$$
\text{Delay}
$$

$$
\text{Off-Peak Conversion}
$$

作為：

$$
\boxed{
\text{virtual capacity}
}
$$

。

因為少用一單位尖峰需求，

在系統效果上近似增加一單位可服務 capacity。

---

## 24. Demand Reduction 與 Supply Expansion 的結構對偶

若：

$$
D(t)>C(t)
$$

有兩種基本解：

$$
C(t)\uparrow
$$

或：

$$
D(t)\downarrow
$$

因此：

$$
\boxed{
\Delta C
\approx
-\Delta D
}
$$

在特定容量平衡問題中具有結構對偶。

這正是 Paper 4 與 Paper 5 的制度基礎。

---

## 25. 第七個演化步驟：Capacity Market

當：

- capacity 可測量；
- future demand 可預測；
- priority 可區分；
- reservation 可執行；
- demand response 可驗證；

就可能形成：

$$
\boxed{
\text{AI Capacity Market}
}
$$

。

---

## 26. AI Capacity Market 不必是一個交易所

Capacity Market 可以只是：

> Enterprise Reserved Tier。

也可以是：

> Flex Window Reservation。

甚至：

> 使用者返還 Priority CU。

因此：

$$
\boxed{
\text{market}
\neq
\text{public exchange}
}
$$

。

市場是制度化價格與權利配置機制，

不一定需要 order book。

---

## 27. Forward Capacity

企業可能說：

> 明年 Q2 我需要：

$$
10^9\ \mathrm{CU/day}
$$

。

供應商需要：

- 採購 GPU；
- 建資料中心；
- 簽能源；
- 建網路。

因此雙方自然具有：

$$
\boxed{
\text{forward contracting incentive}
}
$$

。

---

## 28. Capacity Forward

簡化的 future capacity contract：

$$
F
=
(
Q,
t_1,
t_2,
p,
P
)
$$

表示：

- 未來時間窗；
- 保證容量；
- priority；
- contract price。

這本質上已接近：

$$
\text{Compute Forward}
$$

。

---

## 29. 第八個演化步驟：Financialization

只要 future capacity contract 可以：

- 標準化；
- 轉讓；
- 定價；
- 對沖；

就可能進一步出現：

$$
\text{Compute Futures}
$$

$$
\text{Capacity Options}
$$

或：

$$
\text{Compute Swaps}
$$

。

但本文不主張 AI 市場現在就應進入此階段。

---

## 30. 金融化不是必然進步

金融化可以：

- 鎖定成本；
- 對沖風險；
- 提前融資；
- 提供價格發現。

但也可能：

- 增加投機；
- 造成槓桿；
- 強化價格波動；
- 形成市場操縱；
- 讓實體服務與金融價格脫鉤。

因此：

$$
\boxed{
\text{financialization}
\neq
\text{automatic welfare improvement}
}
$$

。

---

## 31. 為什麼這仍然是典型資本主義演化

如果抽象到足夠高：

$$
\boxed{
\text{new scarce resource}
\rightarrow
\text{property-like rights}
\rightarrow
\text{pricing}
\rightarrow
\text{exchange}
\rightarrow
\text{institutions}
}
$$

確實是市場資本主義中極常見的制度演化。

但「property-like」不必等於完整私有財產權。

它可以只是：

$$
\text{contractual entitlement}
$$

。

---

## 32. 資本主義真正擅長的是差異商品化

市場會不斷發現：

$$
A\neq B
$$

。

例如原本大家以為：

> 算力就是算力。

後來發現：

$$
\text{Instant Compute}
\neq
\text{Batch Compute}
$$

$$
\text{Guaranteed Compute}
\neq
\text{Interruptible Compute}
$$

$$
\text{Peak Compute}
\neq
\text{Off-Peak Compute}
$$

。

於是差異被商品化。

---

## 33. 商品化會增加效率，也會增加複雜度

如果商品過粗：

$$
\text{misallocation}\uparrow
$$

。

如果商品切得過細：

$$
\text{transaction cost}\uparrow
$$

。

因此制度設計必須求：

$$
k^*
=
\arg\min_k
[
C_{\mathrm{misallocation}}(k)
+
C_{\mathrm{transaction}}(k)
]
$$

其中 $k$ 是市場細分程度。

---

## 34. 這就是為什麼使用者 UI 不能變成華爾街終端

底層可以有：

$$
\text{hundreds of pricing states}
$$

但使用者只需要：

> 現在跑。

> 今天內。

> 最便宜。

因此：

$$
\boxed{
\text{institutional sophistication}
\neq
\text{interface complexity}
}
$$

。

---

## 35. Transaction Cost Economics

如果每一次 AI inference 都要求使用者計算：

- token；
- cache；
- priority；
- region；
- energy；
- deadline；

則：

$$
C_{\mathrm{transaction}}
$$

過高。

訂閱的價值之一正是：

$$
\boxed{
\text{transaction-cost compression}
}
$$

。

因此市場成熟不代表所有東西都改成 spot price。

---

## 36. Subscription 是制度技術，不只是價格

固定訂閱可以看成：

$$
\text{price uncertainty}
\rightarrow
\text{fixed periodic contract}
$$

。

它把大量微交易壓縮成：

$$
1\text{ monthly decision}
$$

。

因此：

$$
\boxed{
\text{Subscription survives because simplicity itself has economic value.}
}
$$

。

---

## 37. API 也是制度技術

API 則把：

$$
\text{human interaction}
$$

轉化為：

$$
\text{programmable consumption}
$$

。

因此 API 不只是技術介面。

它同時改變：

- consumption scale；
- automation；
- resale possibility；
- monitoring；
- pricing granularity。

---

## 38. Agent 會改變市場結構

當 Agent 可以自主：

$$
\text{buy compute}
$$

$$
\text{delay workload}
$$

$$
\text{switch model}
$$

$$
\text{reserve capacity}
$$

市場參與者不再只有人類。

而是：

$$
\boxed{
\text{human + machine economic actors}
}
$$

。

---

## 39. 機器速度會放大市場反應

人類看到折扣：

> 等一下再用。

Agent 可以在毫秒級：

$$
\arg\min_tP(t)
$$

並大量改變 workload。

因此：

$$
\text{market responsiveness}\uparrow
$$

同時：

$$
\text{market instability risk}\uparrow
$$

。

---

## 40. 因此 AI 市場需要新的反操縱規則

例如：

- minimum reservation period；
- rate of repricing；
- anti-bot gaming；
- identity-bound entitlement；
- capacity auction limits；
- disclosure delays。

這再次證明：

$$
\boxed{
\text{market growth}
\rightarrow
\text{rule growth}
}
$$

。

---

## 41. 第九個演化步驟：Governance

市場制度演化不是：

$$
\text{less governance}
$$

。

通常反而是：

$$
\boxed{
\text{more explicit governance}
}
$$

。

因為交易越複雜，

越需要定義：

- ownership；
- responsibility；
- fraud；
- default；
- disclosure；
- audit；
- settlement。

---

## 42. 市場與監管共同演化

因此更精確的制度函數是：

$$
I_{t+1}
=
f(
M_t,
T_t,
R_t,
G_t,
U_t
)
$$

其中：

- $M_t$：market pressure；
- $T_t$：technology；
- $R_t$：regulation；
- $G_t$：governance；
- $U_t$：user behavior。

這不是：

$$
I_{t+1}
=
f(M_t)
$$

。

---

## 43. 資本主義不保證最優制度

市場可以產生：

$$
\text{innovation}
$$

也可以產生：

$$
\text{market power}
$$

$$
\text{information asymmetry}
$$

$$
\text{rent extraction}
$$

$$
\text{predatory pricing}
$$

$$
\text{over-financialization}
$$

。

因此不能說：

> 只要讓市場發展就一定最好。

---

## 44. 但套利是一種重要制度感測器

當大量人嘗試套利：

$$
A\rightarrow B
$$

通常表示：

$$
\boxed{
\text{the boundary between A and B has economic tension}
}
$$

。

供應商可以把套利視為：

- abuse signal；
- pricing signal；
- product demand signal。

三者同時存在。

---

## 45. Regulatory Arbitrage 也可能出現

如果不同地區對：

- credits；
- stored value；
- resale；
- consumer rights；
- data residency；

規則不同，

企業可能：

$$
\text{jurisdiction shopping}
$$

。

因此全球 AI Compute Market 必須處理：

$$
\boxed{
\text{regulatory fragmentation}
}
$$

。

---

## 46. 標準化會成為國際競爭的一部分

如果未來：

$$
CU_A
$$

與：

$$
CU_B
$$

無法比較，

跨供應商市場很難形成。

因此可能出現：

$$
\text{Compute Benchmark Standard}
$$

或：

$$
\text{Effective Inference Unit}
$$

的產業標準競爭。

---

## 47. 但「智能」不能完全被壓縮成單一單位

AI 的：

$$
Q_{\mathrm{quality}}
$$

$$
R_{\mathrm{reasoning}}
$$

$$
S_{\mathrm{safety}}
$$

$$
M_{\mathrm{memory}}
$$

差異很大。

因此：

$$
\boxed{
\text{compute standardization}
\neq
\text{intelligence standardization}
}
$$

。

Compute Unit 只能描述資源。

不能完整描述智能品質。

---

## 48. 市場最終交易的是複合商品

未來 AI 服務可能是：

$$
G
=
(
C,
Q,
L,
P,
S,
D
)
$$

其中：

- $C$：compute；
- $Q$：quality；
- $L$：latency；
- $P$：priority；
- $S$：safety／service guarantee；
- $D$：deadline。

因此成熟 AI 市場很可能不是一條 price curve。

而是：

$$
\boxed{
\text{multi-dimensional service market}
}
$$

。

---

## 49. 第十個演化步驟：Transparency

市場越複雜，

資訊越重要。

若使用者不知道：

$$
\text{capacity}
$$

企業不知道：

$$
\text{latent demand}
$$

投資者不知道：

$$
\text{utilization}
$$

就會產生：

$$
\text{information asymmetry}
$$

。

---

## 50. 透明度是價格發現基礎

Paper 6 提出：

$$
\text{Capacity Signal}
\rightarrow
\text{User Scheduling}
$$

Paper 7 提出：

$$
\text{Compute Metrics}
\rightarrow
\text{Investor Price Discovery}
$$

因此透明度同時支援：

$$
\boxed{
\text{product market}
+
\text{capital market}
}
$$

。

---

## 51. 但透明度也會改變市場

如果公開：

> 今晚低負載。

需求就會移動。

如果公開：

> UDR 很高。

投資者可能提高未來需求預期。

因此：

$$
\boxed{
\text{disclosure}
\rightarrow
\text{behavior}
\rightarrow
\text{new market state}
}
$$

。

這是一個動態系統。

---

## 52. Adaptive AI Compute Market

整合前七篇後，

本文提出：

$$
\boxed{
\text{Adaptive AI Compute Market}
}
$$

。

其基本元件為：

$$
\begin{aligned}
\mathcal M
=
\{&
\text{Membership},
\text{Compute Wallet},
\text{Temporal Fungibility},\\
&
\text{Burst Envelope},
\text{Overage},
\text{Rollover},
\text{Borrow},\\
&
\text{Surrender},
\text{Flex},
\text{Reservation},
\text{Transparency}
\}
\end{aligned}
$$

。

---

## 53. 這不是一個單一產品

它更像一個：

$$
\boxed{
\text{market architecture}
}
$$

。

不同公司可以只採用：

$$
\mathcal M_i
\subset
\mathcal M
$$

。

例如：

消費產品：

$$
\{
\text{Membership},
\text{Wallet},
\text{Rollover},
\text{Flex}
\}
$$

。

企業 API：

$$
\{
\text{Reserved},
\text{Priority},
\text{Batch},
\text{Capacity Forecast}
\}
$$

。

---

## 54. 市場成熟度階梯

本文提出十階模型：

### Stage 0

$$
\text{Free / Experimental Access}
$$

### Stage 1

$$
\text{Flat Subscription}
$$

### Stage 2

$$
\text{Subscription + Hard Limits}
$$

### Stage 3

$$
\text{Usage Credits / Overage}
$$

### Stage 4

$$
\text{Service Tiers}
$$

### Stage 5

$$
\text{Temporal Fungibility}
$$

### Stage 6

$$
\text{Demand Response}
$$

### Stage 7

$$
\text{Capacity Transparency}
$$

### Stage 8

$$
\text{Reserved / Forward Capacity}
$$

### Stage 9

$$
\text{Standardized Capacity Market}
$$

### Stage 10

$$
\text{Selective Financialization}
$$

不是所有市場都必須走到 Stage 10。

---

## 55. 現在 AI 市場在哪裡

截至 2026 年，

不同產品分布在不同階段。

消費 AI 大致仍常見：

$$
\text{Stage 2--3}
$$

。

企業 API 已大量出現：

$$
\text{Stage 4}
$$

甚至：

$$
\text{Stage 8}
$$

的 Reserved Capacity。

而：

$$
\text{Stage 5--7}
$$

仍有很大的制度實驗空間。

---

## 56. 制度創新可能成為競爭優勢

當模型差距：

$$
\Delta M
$$

縮小，

其他差異就會變重要。

例如：

$$
\boxed{
\text{Price}
+
\text{Availability}
+
\text{Flexibility}
+
\text{Transparency}
+
\text{Integration}
}
$$

。

因此：

$$
\text{Model Competition}
$$

不會消失，

但會被：

$$
\boxed{
\text{Institutional Competition}
}
$$

補充。

---

## 57. 同一模型也可以因制度不同產生不同價值

假設兩家公司使用相似模型：

$$
M_A\approx M_B
$$

但 A：

- 額度僵硬；
- 不透明；
- peak 常限流；
- API 與訂閱完全割裂。

B：

- Wallet；
- Flex；
- predictable overage；
- capacity forecast；
- autoschedule。

則：

$$
V_B>V_A
$$

完全可能成立。

---

## 58. 制度本身可以產生網路效應

如果大量使用者願意：

$$
\text{Flex}
$$

平台就能更好：

$$
\text{load balance}
$$

。

容量成本下降後：

$$
P\downarrow
$$

又吸引更多 workload。

形成：

$$
\boxed{
\text{flexibility network effect}
}
$$

。

---

## 59. 透明度也可以形成信任資本

如果平台長期準確公布：

$$
\hat L(t)
$$

與：

$$
\text{actual outcome}
$$

使用者會形成：

$$
\text{Trust}_T
$$

。

投資者也可能對：

$$
\text{Compute Metrics}
$$

形成信任。

因此：

$$
\boxed{
\text{transparency}
\rightarrow
\text{institutional credibility}
}
$$

本身具有經濟價值。

---

## 60. 但市場制度會產生新的階級差異

如果高價方案：

$$
\text{always priority}
$$

低價方案：

$$
\text{always flex}
$$

可能形成：

$$
\boxed{
\text{latency stratification}
}
$$

。

這不一定不合理，

但需要清楚揭露。

---

## 61. AI 市場的公平不等於相同待遇

公平可能是：

$$
\text{same price}
\rightarrow
\text{same right}
$$

而不是：

$$
\text{everyone gets identical latency}
$$

。

只要：

- 權利清楚；
- 不欺騙；
- baseline 有保障；
- 差異有對價；

市場分層可以具有正當性。

---

## 62. 公共政策也會介入

如果 AI Compute 成為：

$$
\text{critical infrastructure}
$$

政府可能關心：

- emergency access；
- healthcare；
- public services；
- national security；
- education；
- small business access。

因此 capacity market 不會只是私人公司內部問題。

---

## 63. Emergency Capacity

未來甚至可能存在：

$$
C_{\mathrm{emergency}}
$$

保留給：

- 災害；
- 公共衛生；
- 關鍵基礎設施。

這和 Reliability Reserve 類似，

但具有公共政策目的。

---

## 64. 市場效率與公共價值可能衝突

單純最大化：

$$
\text{Revenue}/\mathrm{CU}
$$

可能把所有容量都給最高出價者。

但社會可能要求：

$$
\boxed{
\text{minimum universal access}
}
$$

。

因此成熟 AI 市場仍需要政策邊界。

---

## 65. 所以這不是「市場萬能論」

本文真正主張的是：

$$
\boxed{
\text{many current AI frictions are recognizable market-design problems}
}
$$

。

這與：

> 所有問題都應該交給市場。

完全不同。

---

## 66. 跨產業制度切片的力量

本系列大量機制不是從零發明。

例如：

### 電力

$$
\text{Demand Response}
+
\text{Capacity Market}
$$

### 雲端

$$
\text{Reserved}
+
\text{Spot}
+
\text{Flex}
$$

### 航空

$$
\text{Load Factor}
+
\text{Yield}
$$

### SaaS

$$
\text{Subscription}
+
\text{Usage-Based Billing}
$$

### 金融

$$
\text{Forward}
+
\text{Risk Pricing}
$$

。

---

## 67. 真正的新東西在重新組合

單獨：

$$
A
$$

不是新的。

$$
B
$$

也不是新的。

但：

$$
\boxed{
A
\oplus
B
\oplus
C
\rightarrow
X_{\mathrm{AI}}
}
$$

在 AI 新環境中可能形成全新的制度。

這是：

$$
\boxed{
\text{institutional recombination}
}
$$

。

---

## 68. Institutional Recombination Operator

本文可以把制度移植形式化為：

$$
\Phi:
I_j
\rightarrow
I_{\mathrm{AI}}
$$

其中 $I_j$ 是其他成熟產業的制度。

但不是直接 copy。

而是：

$$
I_{\mathrm{AI}}
=
\Psi(
I_j,
T_{\mathrm{AI}},
C_{\mathrm{AI}},
U_{\mathrm{AI}}
)
$$

。

---

## 69. Structural Isomorphism 才是移植條件

真正需要尋找的是：

$$
\boxed{
\text{structural isomorphism}
}
$$

例如 AI 與電力都存在：

$$
D(t)\leq C(t)
$$

以及：

$$
\text{peak demand}
$$

。

因此 demand response 可以移植。

不是因為：

> AI 就是電。

---

## 70. 不同構就不能硬搬

例如航空座位：

$$
\text{flight departs}
\Rightarrow
\text{capacity expires}
$$

AI GPU capacity 則可以：

- reroute；
- batch；
- change model；
- improve software。

因此：

$$
\text{airline analogy}
$$

只能移植部分。

---

## 71. 成熟市場是制度實驗資料庫

因此研究新 AI 商業制度時，

可以把其他產業視為：

$$
\boxed{
\text{institutional experiment repository}
}
$$

。

問題不是：

> 誰有全新 idea？

而是：

> 哪個成熟市場已經測過類似結構？

---

## 72. 這也解釋了為什麼很多 AI 策略看起來「沒有很新」

因為：

$$
\boxed{
\text{AI novelty}
\neq
\text{institutional novelty}
}
$$

。

技術是新的。

市場問題可能很老。

例如：

- peak demand；
- oversubscription；
- price discrimination；
- reservation；
- capacity shortage；
- disclosure；
- arbitrage。

都已有長期歷史。

---

## 73. AI 企業仍然需要重新學一次

即使制度已在其他產業存在，

移植仍需要：

- 新計量單位；
- 新 UX；
- 新安全；
- 新法律；
- 新 Agent behavior；
- 新成本函數。

因此：

$$
\text{known principle}
\neq
\text{solved AI implementation}
$$

。

---

## 74. Institutional Search 可以成為企業方法論

當 AI 公司遇到問題：

$$
X_{\mathrm{AI}}
$$

可以搜尋：

$$
\{
X_{\mathrm{cloud}},
X_{\mathrm{energy}},
X_{\mathrm{airline}},
X_{\mathrm{telecom}},
X_{\mathrm{finance}}
\}
$$

。

再尋找：

$$
\phi:
X_j
\rightarrow
X_{\mathrm{AI}}
$$

。

這本身就是制度創新方法。

---

## 75. 從產品管理走向制度工程

傳統 Product Management 問：

> 這個 button 怎麼設計？

制度工程會問：

> 權利如何定義？

> 風險由誰承擔？

> 價格如何形成？

> 需求如何移動？

> 資訊如何揭露？

因此 AI 產品越成熟，

越需要：

$$
\boxed{
\text{Institutional Engineering}
}
$$

。

---

## 76. AI Native Economics

最終可能需要一套：

$$
\boxed{
\text{AI-Native Economic Design}
}
$$

它不再假設：

- 人類手動請求；
- 工作必須即時；
- token 是唯一單位；
- 月份是認知週期；
- API 與訂閱永遠分離。

---

## 77. Agent 會要求機器可讀的市場規則

未來價格、容量與 entitlement 需要：

$$
\text{machine-readable}
$$

。

例如：

$$
\text{Capacity API}
$$

$$
\text{Pricing API}
$$

$$
\text{Reservation API}
$$

$$
\text{Surrender API}
$$

。

Agent 才能真正自動調度。

---

## 78. 市場規則也需要可驗證

若 Agent 自動購買 capacity，

就需要：

$$
\boxed{
\text{verifiable settlement}
}
$$

。

例如：

- 執行了多少；
- 扣了多少；
- 為何扣；
- SLA 是否滿足；
- refund 是否成立。

這會推動：

$$
\text{economic observability}
$$

。

---

## 79. 從 Token Economy 到 Compute Economy

早期 AI 經濟常被描述為：

$$
\text{Token Economy}
$$

。

但真正成熟後：

$$
\boxed{
\text{Compute Economy}
}
$$

更準確。

因為：

$$
\text{Token}
\subset
\text{Compute Cost}
$$

。

---

## 80. 從 Compute Economy 到 Intelligence Economy

再往後，

如果：

$$
\text{quality}
$$

與：

$$
\text{task completion}
$$

可以可靠衡量，

市場甚至可能從：

$$
\text{pay per compute}
$$

進入：

$$
\boxed{
\text{pay per outcome}
}
$$

。

---

## 81. Outcome Pricing

例如：

> 不是付 100 CU。

而是：

> 完成一個驗證通過的程式修復。

價格：

$$
P_{\mathrm{outcome}}
$$

。

供應商自己承擔：

$$
C_{\mathrm{compute}}
$$

的不確定性。

---

## 82. Outcome Market 會再改變整個市場

當：

$$
P_{\mathrm{outcome}}
$$

出現，

供應商有強烈誘因改善：

$$
\frac{
\text{successful outcomes}
}{
\text{compute}
}
$$

。

這會讓市場從：

$$
\text{sell compute}
$$

走向：

$$
\boxed{
\text{sell completed intelligence work}
}
$$

。

---

## 83. 但 Outcome Pricing 更難

需要判定：

$$
\text{success}
$$

。

例如：

> 文章算完成嗎？

> 程式修好了嗎？

> 研究正確嗎？

因此 outcome market 需要：

- verification；
- evaluation；
- dispute resolution。

這是更後期的制度。

---

## 84. 本系列的整體架構

前七篇可以重新排列成：

### Layer A：Time

Paper 1–2：

$$
\text{Billing Time}
\neq
\text{Cognition Time}
$$

### Layer B：Resource

Paper 3：

$$
\text{Compute Wallet}
$$

### Layer C：Rights

Paper 4：

$$
\text{Reversible Entitlement}
$$

### Layer D：Demand

Paper 5：

$$
\text{Demand Engineering}
$$

### Layer E：Information

Paper 6：

$$
\text{Capacity Transparency}
$$

### Layer F：Capital

Paper 7：

$$
\text{Compute Fundamentals}
$$

。

---

## 85. Paper 8 把它們全部制度化

因此：

$$
\boxed{
\text{Time}
+
\text{Resource}
+
\text{Rights}
+
\text{Demand}
+
\text{Information}
+
\text{Capital}
}
$$

共同形成：

$$
\boxed{
\text{AI Compute Institution}
}
$$

。

---

## 86. 一個統一狀態模型

令 AI 市場狀態為：

$$
\mathcal S(t)
=
(
D(t),
C(t),
P(t),
E(t),
I(t),
K(t)
)
$$

其中：

- $D$：demand；
- $C$：capacity；
- $P$：price；
- $E$：entitlement；
- $I$：information；
- $K$：capital。

制度：

$$
\mathcal R
$$

決定：

$$
\mathcal S(t)
\rightarrow
\mathcal S(t+1)
$$

。

---

## 87. 市場設計就是選擇轉移規則

例如：

$$
D>C
$$

時，

Rule A：

$$
\text{Rate Limit}
$$

。

Rule B：

$$
\text{Surcharge}
$$

。

Rule C：

$$
\text{Off-Peak Discount}
$$

。

Rule D：

$$
\text{Surrender}
$$

。

不同規則產生不同：

$$
\mathcal S(t+1)
$$

。

這就是制度工程。

---

## 88. 制度競爭可以被實驗化

企業可以 A/B test：

$$
\mathcal R_1
$$

與：

$$
\mathcal R_2
$$

比較：

$$
\text{Retention}
$$

$$
\text{Peak Load}
$$

$$
\text{Gross Margin}
$$

$$
\text{Trust}
$$

$$
\text{Task Completion}
$$

。

因此制度不只是哲學。

它可以被工程化測試。

---

## 89. 可測試假說

### H1：AI 市場會持續增加 service segmentation

隨 workload 異質性增加：

$$
N_{\mathrm{tiers}}\uparrow
$$

可能成立。

### H2：灰色套利會預測官方 fungibility 產品出現

當：

$$
A_{\mathrm{arbitrage}}\uparrow
$$

供應商更有動機：

$$
\text{formalize selected conversions}
$$

。

### H3：Agent adoption 會提高時間差異化定價的重要性

因：

$$
FWR_{\mathrm{agent}}
>
FWR_{\mathrm{chat}}
$$

。

### H4：Capacity reservation 會隨企業 AI production 化增加

當：

$$
\text{mission critical AI}
\uparrow
$$

對：

$$
\text{capacity certainty}
$$

支付意願上升。

### H5：Compute transparency 會逐步成為產業競爭變數

尤其當模型能力差距縮小。

### H6：標準化 Compute Metrics 會在資本密集度上升後變得更重要

因：

$$
K_{\mathrm{AI}}\uparrow
$$

使投資者需要更高：

$$
\text{capital accountability}
$$

。

---

## 90. 可能的失敗路徑

市場也可能走向：

### Failure A

$$
\text{Too Many Tiers}
$$

使用者無法理解。

### Failure B

$$
\text{Opaque Dynamic Pricing}
$$

降低信任。

### Failure C

$$
\text{Compute Speculation}
$$

脫離實際需求。

### Failure D

$$
\text{Market Concentration}
$$

少數供應商控制 capacity。

### Failure E

$$
\text{Regulatory Fragmentation}
$$

全球市場難整合。

---

## 91. 因此成熟制度應追求適度市場化

不是：

$$
\text{maximum marketization}
$$

而是：

$$
\boxed{
\text{appropriate marketization}
}
$$

。

對某些權利：

$$
\text{transferable}
$$

可能有效。

對其他權利：

$$
\text{non-transferable}
$$

更安全。

---

## 92. 三種市場邊界

### Private Contract Market

企業與供應商雙邊簽約。

### Provider Internal Market

Wallet、Flex、Surrender。

### Open Market

可自由轉讓的標準 capacity contract。

AI 市場可以長期停留在前兩者。

---

## 93. 開放市場不是成熟的唯一終點

成熟市場也可以是：

$$
\boxed{
\text{highly governed provider-mediated market}
}
$$

。

例如雲端 compute 很多 capacity product 仍由單一 provider 內部定價與管理。

---

## 94. 市場演化的真正核心：權利明確化

從：

> 你大概可以用。

走向：

$$
\boxed{
\text{what}
+
\text{how much}
+
\text{when}
+
\text{how fast}
+
\text{what happens if unused}
}
$$

。

這就是權利從模糊到明確。

---

## 95. 權利越清楚，市場越容易形成

如果：

$$
E
$$

沒有清楚定義，

就難以：

- 定價；
- 轉換；
- 返還；
- 預約；
- 比較。

因此：

$$
\boxed{
\text{property-like clarity precedes sophisticated exchange}
}
$$

。

---

## 96. 但 AI 使用權不一定需要變成財產權

Paper 4 已區分：

$$
\text{Reversibility}
\neq
\text{Transferability}
$$

。

因此市場成熟可以建立在：

$$
\text{contractual clarity}
$$

而不必建立在：

$$
\text{full property rights}
$$

。

---

## 97. 這一點避免過度金融化

如果每個 CU 都立即變成：

$$
\text{tradeable asset}
$$

可能過早引入投機。

所以更合理的是：

$$
\boxed{
\text{rights clarity first}
\rightarrow
\text{liquidity later if useful}
}
$$

。

---

## 98. 資本主義演化其實是一連串「拆分」

原本：

$$
\text{AI Subscription}
$$

是一個 bundle。

之後拆成：

$$
\text{Membership}
$$

$$
\text{Compute}
$$

$$
\text{Priority}
$$

$$
\text{Latency}
$$

$$
\text{Reservation}
$$

$$
\text{Rollover}
$$

$$
\text{Surrender}
$$

。

這就是：

$$
\boxed{
\text{unbundling of economic rights}
}
$$

。

---

## 99. 拆分之後又會重新 Bundling

市場不會永遠越拆越細。

當使用者覺得複雜，

企業又會推出：

> Pro Everything Plan。

因此：

$$
\boxed{
\text{Unbundle}
\leftrightarrow
\text{Rebundle}
}
$$

是循環。

---

## 100. Compute Wallet 正是 Rebundling Layer

底層細分很多權利。

Wallet 再把它們抽象成：

$$
\text{simple user balance}
$$

。

因此：

$$
\boxed{
\text{economic unbundling underneath}
+
\text{product rebundling above}
}
$$

可能是最穩定結構。

---

## 101. 最終不是「訂閱 vs API」

而是：

$$
\boxed{
\text{Membership}
+
\text{Metering}
+
\text{Scheduling}
+
\text{Capacity}
}
$$

。

API 與 Chat UI 只是：

$$
\text{consumption interfaces}
$$

。

---

## 102. 也不是「市場 vs 計畫」

供應商內部本來就在做：

$$
\text{central planning}
$$

例如：

- routing；
- capacity allocation；
- GPU scheduling。

外部又可以有：

$$
\text{price signals}
$$

。

因此最終系統是：

$$
\boxed{
\text{planning}
+
\text{market}
}
$$

混合。

---

## 103. AI 公司本身就是小型經濟體

大型 AI provider 同時管理：

- currency-like credits；
- capacity；
- queues；
- price tiers；
- scarcity；
- allocation；
- subsidies；
- user classes。

因此可以說：

$$
\boxed{
\text{AI platform}
\approx
\text{micro-economy}
}
$$

。

---

## 104. 平台治理就是微型制度政治

例如：

> 誰先拿到 GPU？

這不是純技術問題。

也是：

$$
\text{allocation rule}
$$

問題。

> 免費用戶與企業用戶怎麼分？

也是制度問題。

---

## 105. 因此未來產品團隊需要更多制度思維

除了：

- engineer；
- designer；
- economist；

還需要更強：

$$
\boxed{
\text{market design}
+
\text{governance}
+
\text{behavioral economics}
}
$$

能力。

---

## 106. Adaptive AI Compute Economy

本文最後將整個系列概念濃縮為：

$$
\boxed{
\text{Adaptive AI Compute Economy}
}
$$

其目的不是最大化：

$$
\text{compute consumption}
$$

而是最大化：

$$
\boxed{
\frac{
\text{useful intelligence work}
}{
\text{economic + physical resource cost}
}
}
$$

。

---

## 107. 這會成為模型之外的競爭維度

未來企業可能比較：

$$
M
=
\text{Model Capability}
$$

同時比較：

$$
I
=
\text{Institutional Efficiency}
$$

。

最終產品價值：

$$
V
=
f(M,I)
$$

。

---

## 108. Institutional Efficiency

可以暫時定義：

$$
\eta_I
=
\frac{
V_{\mathrm{served}}
}{
C_{\mathrm{compute}}
+
C_{\mathrm{transaction}}
+
C_{\mathrm{friction}}
}
$$

。

制度越好，

在相同模型下：

$$
\eta_I\uparrow
$$

。

---

## 109. 制度競爭甚至可能反過來改變模型設計

如果 Flex 市場很大，

模型可能針對：

$$
\text{batch efficiency}
$$

最佳化。

如果 Reserved market 很重要，

可能針對：

$$
\text{predictable throughput}
$$

最佳化。

因此：

$$
\boxed{
\text{market design}
\rightarrow
\text{technical design}
}
$$

。

---

## 110. 技術與制度會共同演化

最終：

$$
T_{t+1}
=
f(I_t)
$$

且：

$$
I_{t+1}
=
g(T_t)
$$

。

因此：

$$
\boxed{
\text{Technology}
\leftrightarrow
\text{Institution}
}
$$

是共同演化。

---

## 111. 基本原則

本文提出十五項總原則。

### 原則一：AI Compute 是新型稀缺經濟資源

但不是完全同質商品。

### 原則二：市場分層會隨 workload 異質性增加

$$
\text{one price}
\rightarrow
\text{multiple rights}
$$

。

### 原則三：套利既是風險，也是制度訊號

不要只封鎖，也要理解需求。

### 原則四：正式化應保留 provider governance

身份、定價與 rate control 仍然重要。

### 原則五：標準化應描述資源，不應假裝量化完整智能

### 原則六：時間、priority 與 reservation 都可以成為獨立商品維度

### 原則七：Demand Response 可以被視為虛擬 capacity

### 原則八：Capacity Market 不必等於公開交易所

### 原則九：Financialization 只能在有實際風險管理需求時逐步出現

### 原則十：市場成熟同時需要 governance 與 regulation

### 原則十一：透明度提高價格發現，但也改變市場行為

### 原則十二：跨產業制度移植應尋找 structural isomorphism

而不是表面類比。

### 原則十三：底層制度可以複雜，上層介面必須保持簡單

### 原則十四：AI 競爭將逐步包含 Institutional Competition

### 原則十五：最終目標不是讓算力交易越複雜，而是讓智能資源配置更有效率

---

## 112. 限制

第一，本文提出的是制度演化框架，不是歷史決定論。

第二，不同 AI 公司具有不同商業模式，不會沿完全相同路徑發展。

第三，電力、航空、雲端與金融類比只能移植結構，不能直接視為同一市場。

第四，Compute Unit 尚不存在全球統一標準。

第五，AI 模型能力仍高速變化，可能使今天的容量制度很快重新設計。

第六，金融化會引入新的法律與系統性風險，因此不應被預設為終點。

第七，公共政策、反壟斷、消費者保護與能源政策都可能深刻改變市場路徑。

---

## 113. 結論

回到最初那個看似非常小的問題：

> 我這個月沒用完的 AI 額度，為什麼不能拿去做別的事？

它真正暴露的是：

$$
\boxed{
\text{an immature entitlement system}
}
$$

。

現有 AI 訂閱把大量不同經濟權利壓縮在一起：

$$
\text{Access}
+
\text{Compute}
+
\text{Time}
+
\text{Priority}
+
\text{Capacity}
$$

。

市場成熟的自然壓力之一，就是把它們逐步拆開。

因此本系列從：

$$
\text{Billing Time}
$$

一路推進到：

$$
\text{Temporal Fungibility}
$$

$$
\text{Compute Wallet}
$$

$$
\text{Reversible Entitlement}
$$

$$
\text{Demand Engineering}
$$

$$
\text{Capacity Transparency}
$$

$$
\text{Investor Compute Fundamentals}
$$

最後形成：

$$
\boxed{
\text{Adaptive AI Compute Market}
}
$$

。

這並不是因為 AI 產業必須照抄電力、雲端、航空或金融市場。

而是因為很多今天看起來非常新的 AI 商業問題，其底層其實仍然是：

$$
\text{scarcity}
$$

$$
\text{allocation}
$$

$$
\text{pricing}
$$

$$
\text{risk}
$$

$$
\text{information}
$$

$$
\text{rights}
$$

。

這些問題，人類市場已經實驗了很長時間。

因此 AI 企業下一階段的創新，不一定總是發明完全前所未有的制度。

很多時候更有效的方法是：

$$
\boxed{
\text{find a mature institutional fragment}
\rightarrow
\text{identify structural isomorphism}
\rightarrow
\text{adapt it to AI}
}
$$

。

這也正是為什麼，當前 AI 商業制度看起來仍然具有大量可改造空間。

不是因為企業「不懂資本主義」。

而是因為：

$$
\boxed{
\text{AI has created a new resource environment faster than its institutions can mature.}
}
$$

。

市場正在學習：

> 智能到底該怎麼賣？

> 算力到底該怎麼分？

> 高峰到底該怎麼處理？

> 使用權到底能不能移動？

> 投資者到底要看什麼？

這本身就是制度形成的過程。

因此本篇最後的核心命題是：

$$
\boxed{
\text{AI competition is evolving from model competition toward institutional competition over how intelligence is allocated.}
}
$$

中文即：

**AI 產業的競爭正在從單純的模型競爭，逐步延伸為「智能資源如何被配置」的制度競爭。**

主系列至此完成。

接下來兩篇番外將分別處理：

**Extra 1：Token 消耗症候群——到期額度如何反向塑造人的認知行為**

以及：

**Extra 2：跨產業制度移植——AI 產業其實不用每件事重新發明**

前者從行為經濟學回到使用者，

後者則把整個系列背後的跨產業制度搜尋方法正式化。

---

## 參考資料

1. Federal Energy Regulatory Commission. *Understanding Wholesale Capacity Markets.* Updated 2026-06-02.
2. Federal Energy Regulatory Commission. *Energy Markets.* Updated 2026-06-02.
3. Federal Energy Regulatory Commission. *Demand Response.* Accessed 2026-09-07.
4. Amazon Web Services. *Service tiers for optimizing performance and cost — Amazon Bedrock.* Accessed 2026-09-07.
5. Amazon Web Services. *Capacity Reservation pricing and billing — Amazon EC2.* Accessed 2026-09-07.
6. Amazon Web Services. *EC2 Reserved Instance Pricing.* Accessed 2026-09-07.
7. OpenAI. *Reserved Tier for API Customers.* Accessed 2026-09-07.
8. Ronald H. Coase. *The Nature of the Firm.* 1937.
9. Douglass C. North. *Institutions, Institutional Change and Economic Performance.* 1990.
10. Oliver E. Williamson. *The Economic Institutions of Capitalism.* 1985.
11. Karl Polanyi. *The Great Transformation.* 1944.

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

**Paper 7**  
算力透明度作為投資工具：AI 企業的新基本面

**Paper 8 — 本篇**  
AI 市場的制度演化：從商品化到容量市場

**Extra 1 — Next**  
Token 消耗症候群：到期額度如何反向塑造人的認知行為

**Extra 2**  
跨產業制度移植：AI 產業其實不用每件事重新發明
