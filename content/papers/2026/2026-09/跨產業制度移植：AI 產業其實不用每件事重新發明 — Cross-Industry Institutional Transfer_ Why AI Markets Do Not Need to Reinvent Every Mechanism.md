# 跨產業制度移植：AI 產業其實不用每件事重新發明
## Cross-Industry Institutional Transfer: Why AI Markets Do Not Need to Reinvent Every Mechanism

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Extra 2 / 2 — Series Paper 10 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

新興 AI 產業常將定價、算力、容量、訂閱、Agent、API、透明度與需求管理問題描述為前所未有的新挑戰。然而，當問題被抽象到足夠高的結構層次後，許多困難其實具有高度熟悉的制度形式：有限容量、尖峰需求、異質使用者、預付權利、資源預約、閒置損失、資訊不對稱、套利、需求響應、收益管理、容量保證與資本回報等，都已在電力、雲端、航空、電信、SaaS、金融、物流與其他成熟市場中經歷長期制度實驗。

本文提出 **Cross-Industry Institutional Transfer（跨產業制度移植）** 與 **Institutional Recombination（制度重組）** 方法論，將成熟市場視為一個可搜尋的「制度實驗資料庫」。其核心不是照搬其他產業，也不是用表面相似性強行類比，而是先把目標問題表示為關係結構，再尋找具有相同約束、資源流、權利結構、時間特性與激勵機制的來源產業。

本文吸收 Structure-Mapping Theory 的核心洞見：有效類比的重點是映射關係與高階結構，而不是對象的表面屬性；亦呼應 technology brokering 與策略類比研究所揭示的創新模式——新解法經常不是完全從零產生，而是將存在於不同產業、但未被目標市場採用的知識重新組合。本文將此思路進一步制度工程化，提出一套十步流程：

$$
\boxed{
\text{Problem Abstraction}
\rightarrow
\text{Structural Search}
\rightarrow
\text{Mechanism Extraction}
\rightarrow
\text{Boundary Test}
\rightarrow
\text{Recombination}
\rightarrow
\text{Simulation}
\rightarrow
\text{Experiment}
\rightarrow
\text{Governance}
\rightarrow
\text{Measurement}
\rightarrow
\text{Iteration}
}
$$

本文以本系列為案例：AI 的尖峰算力問題可以從電力 Demand Response 借用需求側調度；AI 的容量預約可以對照 AWS Capacity Reservations 與 Reserved Instances；低優先、可中斷工作可以對照 Spot；訂閱的固定價格與按量超額可對照 SaaS hybrid pricing；Compute Load Factor 與 Compute Yield 可以借鑑航空容量與收益管理；未來算力合約可以從金融遠期契約理解風險配置；但所有類比都必須經過差異檢查，例如 AI capacity 可透過 routing、batching、模型替換與軟體效率快速變動，因此它並不等同於飛機座位或電力。

本文進一步提出 **Institutional Primitive Library**、**Institutional Transfer Card**、**Structural Isomorphism Score**、**Boundary Mismatch Penalty** 與 **Transfer Readiness Score**，使跨產業類比不再只是靈感，而可以成為可記錄、可比較、可由 AI Agent 輔助搜尋與驗證的方法。

本文的核心命題為：

$$
\boxed{
\text{Innovation does not require novelty at every layer; novel systems can emerge from validated institutional fragments recombined under new constraints.}
}
$$

中文即：

**創新不要求每一層都全新；真正的新制度，完全可以由已驗證的成熟制度切片，在新的技術與約束下重新組合而成。**

**關鍵詞：** Cross-Industry Transfer、Institutional Recombination、Structure Mapping、Technology Brokering、類比推理、制度工程、AI 市場、跨域創新、Structural Isomorphism、Market Design

---

## 1. 為什麼「不是完全新的」反而值得重視

在新技術產業裡，人們很容易把：

$$
\text{novelty}
$$

當成：

$$
\text{value}
$$

的同義詞。

於是出現一種隱含要求：

> 一個好的 AI 商業制度，最好也是從來沒有人做過。

但這個要求本身並不合理。

如果其他產業已經用數十年時間測過：

- 尖峰調度；
- 預付制度；
- 容量預約；
- 中斷式資源；
- 二級市場；
- 收益管理；
- 負載透明度；

那麼 AI 公司真正需要問的，不是：

> 怎麼假裝這些問題歷史上不存在？

而是：

$$
\boxed{
\text{which tested institutional mechanisms remain valid after translation into AI?}
}
$$

---

## 2. 新技術不等於新市場結構

AI 的底層技術非常新。

但市場面對的抽象問題可能很老。

例如：

$$
D(t)>C(t)
$$

是 AI 算力問題。

也是：

- 電網尖峰；
- 網路頻寬壅塞；
- 雲端資源不足；
- 航班座位供給；

等問題的一種結構。

所以：

$$
\boxed{
\text{Technical Novelty}
\neq
\text{Institutional Novelty}
}
$$

。

---

## 3. Institutional Memory of Civilization

如果把成熟產業看成歷史長期實驗，

那麼社會其實累積了：

$$
\boxed{
\text{institutional memory}
}
$$

。

這些記憶包括：

> 哪種價格會導致套利？

> 哪種 capacity reservation 會產生閒置？

> 哪種動態價格會讓客戶反感？

> 哪種需求響應真的能削峰？

> 哪種透明度會被市場操縱？

新產業沒有理由全部忘掉。

---

## 4. 成熟市場是一個制度實驗資料庫

令：

$$
\mathcal I
=
\{
I_1,I_2,\ldots,I_n
\}
$$

表示已存在的制度集合。

不同產業：

$$
\mathcal D
=
\{
D_{\mathrm{energy}},
D_{\mathrm{cloud}},
D_{\mathrm{airline}},
D_{\mathrm{finance}},
D_{\mathrm{telecom}},
\ldots
\}
$$

可以被理解為：

$$
\boxed{
\text{Institutional Experiment Repository}
}
$$

。

---

## 5. 問題不是 Copy，而是 Transfer

直接照搬：

$$
I_A
\rightarrow
I_B
$$

通常是不可靠的。

真正需要的是：

$$
\boxed{
I_B
=
\Psi(
I_A,
C_B,
T_B,
R_B,
U_B
)
}
$$

其中：

- $C_B$：目標產業成本結構；
- $T_B$：技術條件；
- $R_B$：監管與權利條件；
- $U_B$：使用者行為。

這就是「制度移植」。

---

## 6. Structure-Mapping 的核心啟示

Gentner 的 Structure-Mapping Theory 對類比有一個非常重要的原則：

> 有效類比主要映射關係，而不是物體的表面屬性。

形式化：

$$
M:
R_A(x_i,x_j)
\rightarrow
R_B(y_i,y_j)
$$

而不是優先要求：

$$
Attribute(x_i)
=
Attribute(y_i)
$$

。

---

## 7. 所以「AI 像電力」不是好類比的完整說法

錯誤方式：

> AI 是電力。

正確方式：

> AI 推理與電力系統在特定問題中都存在即時容量上限與尖峰需求，因此 Demand Response 的關係結構可能可移植。

也就是：

$$
\boxed{
\text{similar relation}
\neq
\text{same object}
}
$$

。

---

## 8. Structural Isomorphism

本文將可移植條件定義為：

$$
\boxed{
\text{Structural Isomorphism}
}
$$

。

假設來源產業結構：

$$
G_S
=
(V_S,E_S)
$$

目標產業結構：

$$
G_T
=
(V_T,E_T)
$$

如果存在部分映射：

$$
\phi:
G_S
\rightarrow
G_T
$$

保留關鍵關係，

則制度具有候選可移植性。

---

## 9. 關鍵不是全部同構

真實制度通常只有：

$$
\text{partial isomorphism}
$$

。

例如電力與 AI 都有：

$$
D(t)\leq C(t)
$$

但只有電力具有非常嚴格的：

$$
\text{instantaneous physical balance}
$$

。

AI workload 可以：

- 排隊；
- batch；
- reroute；
- 換模型。

所以映射只在部分成立。

---

## 10. Technology Brokering

Hargadon 與 Sutton 對 IDEO 的研究指出，一個設計組織可以透過跨多個產業取得既有技術知識，再把這些原本分散的解法重新組合到新的產品問題。

其結構可以抽象為：

$$
\boxed{
\text{Acquire}
\rightarrow
\text{Store}
\rightarrow
\text{Retrieve by Analogy}
\rightarrow
\text{Recombine}
}
$$

。

這不是純粹的 invention。

而是：

$$
\boxed{
\text{technology brokering}
}
$$

。

---

## 11. Institutional Brokering

本文將相同概念提升到制度層。

不是搬運：

$$
\text{technology}
$$

而是搬運：

$$
\boxed{
\text{institutional mechanism}
}
$$

。

因此可以定義：

$$
\boxed{
\text{Institutional Brokering}
}
$$

。

---

## 12. 策略類比的價值

Gavetti、Levinthal 與 Rivkin 對新穎、複雜策略環境的研究指出，當完全理性推導與局部搜尋都困難時，類比可以讓決策者從熟悉情境移植高階政策。

AI 市場正好具有：

$$
\text{novelty}
+
\text{complexity}
$$

。

因此類比是一種自然策略工具。

---

## 13. 但策略類比最大的危險也是錯誤類比

如果選錯：

$$
\text{source domain}
$$

就可能把錯誤制度帶入目標市場。

例如：

> AI 是 SaaS，所以 marginal cost 近乎零。

這會忽略 inference cost。

---

## 14. Surface Analogy Failure

本文將只因表面相似而移植稱為：

$$
\boxed{
\text{Surface Analogy Failure}
}
$$

。

例如：

> 都是月費，所以健身房訂閱制度可以完整套用 AI。

不成立。

因為：

$$
MC_{\mathrm{gym,visit}}
$$

與：

$$
MC_{\mathrm{AI,inference}}
$$

結構不同。

---

## 15. Constraint-First Thinking

跨產業制度移植應先列出：

$$
\boxed{
\text{constraints}
}
$$

而不是先找產業故事。

例如 AI capacity 問題先表示：

$$
D(t)>C(t)
$$

$$
\exists J_i:\delta_i>t
$$

$$
MC_{\mathrm{compute}}>0
$$

再搜尋其他產業。

---

## 16. Problem Signature

本文提出 **Problem Signature**：

$$
\Sigma_P
=
(
R,
S,
T,
A,
I,
K,
G
)
$$

其中：

- $R$：resource structure；
- $S$：scarcity；
- $T$：time structure；
- $A$：actors；
- $I$：information；
- $K$：risk/cost；
- $G$：governance。

---

## 17. 例：AI 尖峰算力的 Problem Signature

可以寫成：

$$
\Sigma_{\mathrm{AI,peak}}
=
(
\text{compute},
\text{finite},
\text{time-sensitive},
\text{provider+users},
\text{partially opaque},
\text{high peak cost},
\text{provider governed}
)
$$

。

---

## 18. 搜尋來源產業

根據這個 signature，

可能搜尋：

$$
\{
\text{electricity},
\text{cloud},
\text{telecom},
\text{transport}
\}
$$

。

而不是隨意搜尋：

> 哪個產業最像 AI？

---

## 19. Institutional Primitive

制度通常可以再拆成原子機制。

本文稱為：

$$
\boxed{
\text{Institutional Primitive}
}
$$

例如：

- reservation；
- rollover；
- auction；
- discount；
- priority；
- interruption；
- refund；
- pool；
- quota；
- disclosure；
- insurance；
- forward contract。

---

## 20. Primitive 比產業名稱更適合移植

我們真正移植的通常不是：

$$
\text{electricity market}
$$

整套。

而只是：

$$
\text{Demand Response}
$$

這個 primitive。

同理不是移植：

$$
\text{AWS}
$$

而是：

$$
\text{Capacity Reservation}
$$

。

---

## 21. Institutional Primitive Library

因此企業可以維護：

$$
\mathcal P
=
\{
p_1,p_2,\ldots,p_m
\}
$$

。

每個 primitive 記錄：

- source industries；
- solved problem；
- assumptions；
- failure modes；
- regulation；
- evidence。

形成：

$$
\boxed{
\text{Institutional Primitive Library}
}
$$

。

---

## 22. 本系列其實已經建了一個小型 Primitive Library

例如：

### Temporal Fungibility

來源：

- 電信 rollover；
- 預付制度；
- usage pools。

### Demand Response

來源：

- 電力市場。

### Capacity Reservation

來源：

- 雲端。

### Yield Management

來源：

- 航空。

### Shared Credit Pool

來源：

- SaaS／企業雲端。

### Forward Capacity

來源：

- 能源／金融。

---

## 23. AWS Spot：閒置容量的制度切片

AWS Spot Instances 讓使用者使用雲端中的 spare capacity，價格相較 On-Demand 可低很多，但承擔 capacity 可被收回或不足的風險。

可抽象為：

$$
\boxed{
\text{Lower Price}
\leftrightarrow
\text{Lower Capacity Certainty}
}
$$

。

---

## 24. AI Flex 的同構

AI 低優先 workload 可以：

$$
\text{Lower CU Cost}
\leftrightarrow
\text{Longer / Less Certain Latency}
$$

。

這就是：

$$
\phi_{\mathrm{Spot}\rightarrow\mathrm{AI}}
$$

。

---

## 25. 但不能直接把 Spot 的中斷模型搬過來

VM 被 interruption：

$$
\text{stateful process}
$$

可能需要 checkpoint。

AI inference：

$$
\text{request}
$$

可能更容易 retry。

因此 interruption cost 不同。

所以：

$$
\boxed{
\text{same primitive}
+
\text{different implementation}
}
$$

。

---

## 26. AWS Capacity Reservation：保證本身就是商品

AWS Capacity Reservation 即使保留 capacity 後沒有實際使用，仍可能產生費用。

結構是：

$$
\boxed{
\text{pay for availability}
}
$$

而不只是：

$$
\text{pay for execution}
$$

。

---

## 27. AI Reserved Tier 的同構

AI 企業 production workload 需要：

$$
\text{guaranteed throughput}
$$

。

因此：

$$
\text{Reserved Inference Capacity}
$$

自然對應。

---

## 28. 電力 Demand Response：需求本身可以成為資源

FERC 的 Demand Response 制度允許需求端因尖峰時減少使用而取得補償。

其抽象結構：

$$
\boxed{
-\Delta D
\approx
+\Delta C
}
$$

。

---

## 29. AI Surrender 的同構

若使用者放棄：

$$
100\ \mathrm{Priority\ CU}
$$

則系統未來 peak claim 降低。

因此：

$$
\text{Surrender}
$$

可以被理解為：

$$
\boxed{
\text{virtual AI capacity}
}
$$

。

---

## 30. 航空 Yield Management：同樣座位不同價格

航空業長期處理：

- 固定容量；
- 易逝座位；
- 異質支付意願；
- 時間與退款條件。

其核心 primitive：

$$
\boxed{
\text{segment demand by willingness and constraints}
}
$$

。

---

## 31. AI 服務層的同構

同一模型可提供：

$$
\text{Fast}
$$

$$
\text{Standard}
$$

$$
\text{Flex}
$$

。

不是模型本體不同，

而是：

$$
\text{service rights}
$$

不同。

---

## 32. 但 AI 不像飛機座位那麼固定

飛機起飛後：

$$
C_{\mathrm{seat}}
$$

失效。

AI capacity 可以透過：

- model routing；
- batch；
- software optimization；
- hardware scaling；

改變。

因此 yield management 只能部分移植。

---

## 33. 電信 Rollover：時間碎片可以被放鬆

手機流量市場曾經大量使用固定月流量與 rollover。

其 primitive：

$$
\boxed{
\text{unused entitlement can retain partial future value}
}
$$

。

這正是 Temporal Fungibility 的來源之一。

---

## 34. SaaS Hybrid Billing：固定價格與變動成本共存

很多 SaaS 與雲端服務採：

$$
\text{Base Subscription}
+
\text{Usage Overage}
$$

。

這種 primitive 解決：

$$
\text{predictability}
+
\text{cost alignment}
$$

的張力。

---

## 35. AI Compute Wallet 的同構

Paper 3 提出：

$$
\text{Membership}
+
\text{Included Compute}
+
\text{Wallet}
+
\text{Overage}
$$

。

不是憑空出現。

而是成熟 hybrid pricing 的 AI 重組。

---

## 36. 金融遠期：時間風險可以被合約化

企業若知道未來一定需要資源，

可透過：

$$
\text{forward contract}
$$

提前鎖定價格與供應。

其 primitive：

$$
\boxed{
\text{future uncertainty}
\rightarrow
\text{contractual commitment}
}
$$

。

---

## 37. AI Forward Capacity 的同構

例如：

$$
F
=
(
Q,
t_1,
t_2,
P,
SLA
)
$$

。

企業用戶與 provider 都能降低：

$$
\text{future capacity uncertainty}
$$

。

---

## 38. 第一個核心方法：先抽象，再找來源

錯誤順序：

$$
\text{Find cool industry}
\rightarrow
\text{force analogy}
$$

。

正確順序：

$$
\boxed{
\text{Abstract target problem}
\rightarrow
\text{search structurally similar sources}
}
$$

。

---

## 39. 第二個核心方法：找關係，不找名詞

不要搜尋：

> 哪個產業也有 Token？

應搜尋：

> 哪個產業有「預付、到期、不可完全儲存的使用權」？

這會得到更好的候選來源。

---

## 40. 第三個核心方法：拆 primitive

例如「航空業」太大。

應拆成：

$$
\{
\text{reservation},
\text{yield management},
\text{overbooking},
\text{fare classes},
\text{refund rules}
\}
$$

。

---

## 41. 第四個核心方法：列出 Invariants

制度移植前，要找出來源制度有效的必要關係。

本文稱：

$$
\boxed{
\mathcal I_{\mathrm{inv}}
}
$$

。

例如 Demand Response 的 invariant：

$$
-\Delta D
$$

在尖峰能產生：

$$
+\Delta \text{system margin}
$$

。

---

## 42. 第五個核心方法：列出 Non-Invariants

來源與目標不同的地方：

$$
\mathcal I_{\mathrm{non}}
$$

。

例如：

電：

$$
\text{hard physical balance}
$$

AI：

$$
\text{queueable workload}
$$

。

Non-invariant 不能被一起搬走。

---

## 43. Boundary Mismatch

本文定義：

$$
BMP
=
\sum_j
w_j m_j
$$

為 **Boundary Mismatch Penalty**。

其中：

- $m_j$：某項關鍵差異；
- $w_j$：該差異的重要程度。

---

## 44. Structural Isomorphism Score

定義：

$$
SIS
=
\frac{
\sum_i w_i r_i
}{
\sum_i w_i
}
$$

其中：

- $r_i\in[0,1]$：關鍵關係匹配程度；
- $w_i$：重要權重。

---

## 45. Transfer Readiness Score

可以建立：

$$
TRS
=
\alpha SIS
-
\beta BMP
+
\gamma E
-
\delta C_{\mathrm{impl}}
$$

其中：

- $E$：來源制度實證強度；
- $C_{\mathrm{impl}}$：移植成本。

若：

$$
TRS\uparrow
$$

制度更值得實驗。

---

## 46. 這不是要假裝制度創新可以用一個分數決定

 $TRS$ 只是：

$$
\boxed{
\text{decision aid}
}
$$

。

不是：

$$
\text{truth machine}
$$

。

它的主要價值是迫使團隊明確說出：

> 哪裡真的相同？

> 哪裡其實不同？

---

## 47. Institutional Transfer Card

本文提出每一次移植都生成一張：

$$
\boxed{
\text{Institutional Transfer Card}
}
$$

。

欄位包括：

1. Target problem；
2. Source industry；
3. Source mechanism；
4. Structural match；
5. Required invariants；
6. Boundary mismatches；
7. User impact；
8. Provider economics；
9. Regulatory issues；
10. Experiment design；
11. Kill criteria；
12. Metrics。

---

## 48. Kill Criteria 很重要

跨域創新很容易只看到成功可能。

但移植應事先設定：

$$
\boxed{
\text{kill criteria}
}
$$

例如：

> 若 off-peak discount 使總 peak 反而增加 15%，停止。

> 若轉讓制度 fraud rate 超過門檻，停止。

這可以避免愛上自己的類比。

---

## 49. 第六個核心方法：重新組合而不是單一移植

很多真正有效的 AI 制度不是：

$$
A\rightarrow X
$$

而是：

$$
\boxed{
A+B+C\rightarrow X
}
$$

。

---

## 50. 本系列就是 Institutional Recombination

例如 Adaptive AI Compute Market：

$$
\begin{aligned}
X={}&
\text{Cloud Reservation}\\
&+
\text{Electricity Demand Response}\\
&+
\text{Airline Yield Management}\\
&+
\text{SaaS Subscription}\\
&+
\text{Financial Forward Logic}
\end{aligned}
$$

。

---

## 51. 重組會產生 emergent property

每個 primitive 都已存在。

但組合後：

$$
\boxed{
\text{Compute Wallet}
+
\text{Surrender}
+
\text{Capacity Transparency}
}
$$

可能形成以前不存在的使用者行為與市場結構。

因此：

$$
\text{new whole}
\neq
\text{sum of novelty of parts}
$$

。

---

## 52. Combinatorial Novelty

本文稱：

$$
\boxed{
\text{Combinatorial Novelty}
}
$$

。

即：

> 零件可能都是舊的，但排列、接口與約束使整體成為新的制度。

---

## 53. 這是跨域研究最常見也最實用的創新形式之一

要求：

$$
\text{all components new}
$$

反而會浪費：

$$
\text{civilizational prior}
$$

。

更合理：

$$
\boxed{
\text{reuse validated mechanisms where possible}
}
$$

。

---

## 54. 第七個核心方法：先模擬，再真市場

制度改變會影響：

- 行為；
- 價格；
- 負載；
- fraud；
- fairness。

所以應先：

$$
\text{simulation}
$$

再：

$$
\text{A/B experiment}
$$

。

---

## 55. Agent-Based Institutional Simulation

AI 市場特別適合：

$$
\boxed{
\text{agent-based simulation}
}
$$

。

建立：

$$
N
$$

個使用者 Agent，

各自具有：

$$
(
D_i,
\epsilon_i,
\delta_i,
B_i
)
$$

。

測試不同制度。

---

## 56. 模擬 Demand Response

例如：

$$
\delta_{\mathrm{discount}}
=
\{0,0.1,0.2,0.3\}
$$

觀察：

$$
PAR
$$

$$
Q_{\mathrm{moved}}
$$

$$
Cost
$$

$$
User\ Utility
$$

。

---

## 57. 模擬不是實證替代品

因為：

$$
\text{model behavior}
\neq
\text{real human behavior}
$$

。

所以：

$$
\boxed{
\text{simulation}
\rightarrow
\text{pilot}
\rightarrow
\text{field experiment}
}
$$

。

---

## 58. 第八個核心方法：加入治理邊界

一個經濟上有效的制度，

可能：

$$
\text{legally invalid}
$$

或：

$$
\text{socially unacceptable}
$$

。

因此所有 transfer 都必須檢查：

$$
\boxed{
\text{Governance Filter}
}
$$

。

---

## 59. Governance Filter

至少包含：

$$
G
=
\{
\text{consumer protection},
\text{privacy},
\text{competition},
\text{financial regulation},
\text{safety},
\text{fairness}
\}
$$

。

---

## 60. 電力市場可做，不代表 AI 一定可做

例如高度個人化即時價格：

$$
P_i(t)
$$

可能在能源市場具有特定規則。

搬到 AI 後可能造成：

- discrimination；
- opaque profiling；
- trust problems。

所以制度必須重新合法化與正當化。

---

## 61. 第九個核心方法：設計測量標準

如果移植後無法判斷成功，

就不是制度工程。

每個 transfer 應指定：

$$
\boxed{
\text{success metrics}
}
$$

。

---

## 62. 例：Demand Response 的測量

可以看：

$$
PAR
$$

$$
LSE
$$

$$
FWR
$$

$$
Retention
$$

$$
Gross\ Margin
$$

。

而不只是：

> 使用者有沒有點這個按鈕？

---

## 63. 第十個核心方法：反覆迭代

制度不應一次定死。

流程：

$$
\boxed{
\text{Transfer}
\rightarrow
\text{Observe}
\rightarrow
\text{Update}
\rightarrow
\text{Retransfer}
}
$$

。

來源市場本身也會持續演化。

---

## 64. Institutional Versioning

可以為制度本身設：

$$
I^{(1.0)}
$$

$$
I^{(1.1)}
$$

$$
I^{(2.0)}
$$

。

每次改版保留：

- changed assumptions；
- metric changes；
- observed failures。

形成制度工程 history。

---

## 65. AI 可以幫忙做 Institutional Search

這一方法特別適合 AI Agent。

使用者給：

> 我現在有一個尖峰算力問題。

Agent 可以搜尋：

$$
\mathcal D
$$

中的成熟制度。

---

## 66. AI Institutional Search Pipeline

可以設計：

$$
\boxed{
\text{Problem Parser}
\rightarrow
\text{Structural Encoder}
\rightarrow
\text{Cross-Industry Retriever}
\rightarrow
\text{Mechanism Extractor}
\rightarrow
\text{Boundary Critic}
\rightarrow
\text{Experiment Designer}
}
$$

。

---

## 67. 不要只做 keyword search

如果搜尋：

> AI quota solution

只會找到 AI 產業自己。

真正的 cross-domain search 應搜尋：

$$
\text{relation signature}
$$

。

例如：

> prepaid entitlement + expiry + bursty demand + capacity constraints。

---

## 68. Structural Retrieval

可以將制度表示為 graph：

$$
G_I
=
(
Actors,
Resources,
Rights,
Constraints,
Flows,
Signals
)
$$

。

用 graph similarity 搜尋：

$$
\arg\max_{I_j}
Sim(
G_{\mathrm{target}},
G_{I_j}
)
$$

。

---

## 69. 這會比單純語意 embedding 更穩

語意 embedding 可能因：

> 電力

與：

> AI

字面差異太大而漏掉。

Structural retrieval 則會看到：

$$
\text{peak}
+
\text{capacity}
+
\text{demand reduction}
$$

的同構。

---

## 70. Institutional Knowledge Graph

長期可以建立：

$$
\boxed{
\text{Institutional Knowledge Graph}
}
$$

。

節點：

- mechanisms；
- industries；
- constraints；
- outcomes；
- failures；
- laws；
- metrics。

邊：

- solves；
- requires；
- conflicts-with；
- derived-from；
- analogous-to。

---

## 71. AI 可以做 Multi-Source Recombination

Agent 不只找一個來源。

可以求：

$$
\mathcal S^*
=
\arg\max_{\mathcal S\subset\mathcal I}
Fit(
\oplus_{I\in\mathcal S} I,
P_{\mathrm{target}}
)
$$

。

即搜尋最佳制度組合。

---

## 72. 但組合爆炸會很快出現

若有：

$$
n
$$

個 primitives，

所有組合：

$$
2^n
$$

。

因此需要：

- constraint pruning；
- domain heuristics；
- causal simulation；
- staged search。

---

## 73. Institutional Search 也是一個 P/NP-like Search Problem

不是每個制度組合都能窮舉。

需要：

$$
\boxed{
\text{good abstractions}
}
$$

縮小搜尋空間。

這使制度建模與一般工程架構搜尋具有相似性。

---

## 74. AI 的優勢在於跨域檢索寬度

人類專家通常熟悉：

$$
1\text{--}3
$$

個主要產業。

AI 可以同時檢索：

$$
N\gg1
$$

個產業知識。

這非常適合：

$$
\boxed{
\text{institutional brokering}
}
$$

。

---

## 75. 但 AI 也最容易犯表面類比錯誤

因為模型能快速產生：

> 這就像 Uber。

> 這就像 Airbnb。

卻不一定驗證：

$$
\mathcal I_{\mathrm{inv}}
$$

。

所以 Agent 必須有：

$$
\boxed{
\text{Boundary Critic}
}
$$

角色。

---

## 76. Boundary Critic 的任務

對每個類比問：

1. 哪些 relation 真正一致？
2. 哪些只是語言像？
3. 哪些成本結構不同？
4. 哪些法律權利不同？
5. 哪些 actor 不存在？
6. 哪些 failure mode 會翻轉結果？

---

## 77. Red-Team Transfer

制度移植前應要求另一個 Agent：

> 證明這個類比為什麼不能用。

這叫：

$$
\boxed{
\text{Red-Team Transfer}
}
$$

。

只有在反對後仍存活的 mechanism 才進入試驗。

---

## 78. Institutional TDD

甚至可以把制度工程做成：

$$
\boxed{
\text{Institutional Test-Driven Development}
}
$$

。

先寫：

> 若此機制正確，應觀察到什麼？

再實作。

---

## 79. 例：Off-Peak Discount TDD

RED：

$$
PAR_{\mathrm{new}}
<
PAR_{\mathrm{baseline}}
$$

且：

$$
Retention_{\mathrm{new}}
\geq
Retention_{\mathrm{baseline}}
$$

。

若實驗不成立，

機制 fail。

---

## 80. 這比「我覺得這個 idea 很好」更科學

制度創新應從：

$$
\text{story}
$$

進入：

$$
\boxed{
\text{falsifiable mechanism}
}
$$

。

---

## 81. Cross-Industry Transfer Canvas

企業可以建立一頁模板：

### Target

問題。

### Source

成熟市場。

### Primitive

移植機制。

### Structural Match

相同關係。

### Mismatch

不同關係。

### Adaptation

需要修改什麼。

### Test

怎麼驗證。

### Risk

怎麼失敗。

---

## 82. 這是一種比 brainstorming 更有邊界的創新

一般 brainstorm：

$$
\text{idea space}
$$

幾乎無限。

Institutional Transfer：

$$
\boxed{
\text{search validated mechanism space}
}
$$

。

可以降低：

$$
C_{\mathrm{search}}
$$

。

---

## 83. 也比 Best Practice Copy 更強

Best Practice Copy：

> AWS 這樣做，所以我們也這樣做。

Institutional Transfer：

> AWS 這個機制解決哪些結構問題？我們的結構是否一致？哪些部分不能搬？

兩者差非常多。

---

## 84. Cross-Industry Negative Transfer

也應記錄失敗案例。

如果某 primitive 在 AI 中：

$$
\text{fails}
$$

應加入：

$$
\boxed{
\text{Negative Transfer Library}
}
$$

。

避免其他團隊重複犯錯。

---

## 85. 負面知識同樣是制度資產

例如：

> 秒級動態價格造成 billing anxiety。

> 完全自由轉讓造成套利。

這些失敗：

$$
F_j
$$

本身就是 knowledge。

---

## 86. Institutional Absorptive Capacity

企業不是只要知道其他產業有什麼。

還要具有：

$$
\boxed{
\text{absorptive capacity}
}
$$

能理解、轉譯、實驗與吸收。

沒有這個能力，

跨產業資訊只會變成有趣案例。

---

## 87. 所以跨域團隊有結構優勢

若團隊包含：

- economics；
- software；
- infrastructure；
- law；
- product；
- behavioral science；

則：

$$
\text{Transfer Quality}\uparrow
$$

更可能。

因為 mismatch 更容易被看見。

---

## 88. AI 產業尤其需要這種方法

因為 AI 同時跨：

$$
\boxed{
\text{software}
+
\text{cloud}
+
\text{energy}
+
\text{labor}
+
\text{finance}
+
\text{media}
}
$$

。

它不是單一既有市場的延伸。

---

## 89. 單一產業框架會系統性漏掉東西

只用 SaaS：

漏掉：

$$
\text{compute scarcity}
$$

。

只用電力：

漏掉：

$$
\text{software bundling}
$$

。

只用金融：

漏掉：

$$
\text{human UX}
$$

。

所以需要：

$$
\boxed{
\text{multi-source institutional recombination}
}
$$

。

---

## 90. 本系列的完整來源矩陣

### Paper 1–2

來源：

- 訂閱；
- 電信；
- 預付服務。

解決：

$$
\text{calendar fragmentation}
$$

。

### Paper 3

來源：

- SaaS；
- cloud billing。

解決：

$$
\text{subscription/API split}
$$

。

### Paper 4

來源：

- Demand Response；
- contract options。

解決：

$$
\text{unused entitlement}
$$

。

### Paper 5

來源：

- energy；
- cloud Spot/Flex；
- airline yield。

解決：

$$
\text{peak load}
$$

。

### Paper 6

來源：

- cloud capacity visibility；
- operational status。

解決：

$$
\text{information opacity}
$$

。

### Paper 7

來源：

- airline load factor；
- infrastructure finance；
- SaaS unit economics。

解決：

$$
\text{AI CapEx opacity}
$$

。

### Paper 8

來源：

- institutional economics；
- market design；
- capacity markets。

解決：

$$
\text{system integration}
$$

。

---

## 91. 所以系列本身就是一個方法論示範

我們沒有假設：

$$
\text{AI requires entirely new economics}
$$

。

而是假設：

$$
\boxed{
\text{AI requires new recombinations of old and new economics}
}
$$

。

---

## 92. 新的不是「需求響應」三個字

Demand Response 已經存在。

新的可能是：

> 把 AI subscription entitlement、Compute Wallet、Agent scheduling 與 Demand Response 串在一起。

這才是：

$$
\boxed{
\text{contextual novelty}
}
$$

。

---

## 93. 新的不是「透明度」

Status dashboard 很早就有。

新的可能是：

$$
\text{Capacity Transparency}
\rightarrow
\text{User Scheduling}
\rightarrow
\text{Investor Metrics}
$$

。

這是多層制度連接。

---

## 94. 新的不是「訂閱＋超額」

Hybrid billing 早就存在。

新的可能是：

$$
\text{Membership}
+
\text{Wallet}
+
\text{Rollover}
+
\text{Borrow}
+
\text{Surrender}
+
\text{Capacity Pricing}
$$

。

---

## 95. Innovation Gradient

本文因此提出：

$$
N
=
(
N_{\mathrm{component}},
N_{\mathrm{combination}},
N_{\mathrm{context}},
N_{\mathrm{implementation}}
)
$$

。

一項制度可以：

$$
N_{\mathrm{component}}\approx0
$$

但：

$$
N_{\mathrm{combination}}\gg0
$$

。

仍然具有高度創新性。

---

## 96. 這能降低「一定要全新」的錯誤創新壓力

真正的目標不是：

$$
\text{maximum novelty}
$$

。

而是：

$$
\boxed{
\text{maximum problem-solving value}
}
$$

。

---

## 97. 成熟市場的制度切片也是風險控制

來源機制若有：

$$
20\text{ years evidence}
$$

比完全沒測過的機制具有更多 prior。

因此：

$$
P(\text{success}\mid\text{validated source})
$$

可能高於：

$$
P(\text{success}\mid\text{pure invention})
$$

。

但仍需 target validation。

---

## 98. Bayesian Institutional Transfer

可以表示為：

$$
P(H\mid E_S,E_T)
\propto
P(E_T\mid H)
P(H\mid E_S)
$$

。

其中：

- $E_S$：來源市場證據；
- $E_T$：目標市場新證據。

來源成功提供 prior，

目標實驗更新 posterior。

---

## 99. 來源制度不是證明，只是 Prior

即使：

$$
P(H\mid E_S)
$$

很高，

AI 市場仍可能不同。

因此：

$$
\boxed{
\text{transfer is hypothesis generation, not proof}
}
$$

。

---

## 100. 這是跨域研究最重要的紀律

不能：

> 電力市場有效，所以 AI 一定有效。

只能：

> 因結構相似，這是一個值得測試的高品質假說。

---

## 101. Institutional Transfer 的十步流程

本文將完整方法濃縮為：

### Step 1 — Abstract

$$
P_{\mathrm{target}}
\rightarrow
\Sigma_P
$$

### Step 2 — Search

找 structural source。

### Step 3 — Extract

拆 Institutional Primitive。

### Step 4 — Map

映射關係與 invariants。

### Step 5 — Penalize

列 Boundary Mismatch。

### Step 6 — Recombine

組合多個 primitives。

### Step 7 — Simulate

做 counterfactual。

### Step 8 — Experiment

A/B 或 pilot。

### Step 9 — Govern

法律、公平、安全。

### Step 10 — Iterate

更新制度版本與知識庫。

---

## 102. Canonical Formula

因此：

$$
\boxed{
I_{\mathrm{target}}^{*}
=
\operatorname{Iterate}
\left[
\operatorname{Govern}
\left(
\operatorname{Experiment}
\left(
\operatorname{Recombine}
\left(
\operatorname{Map}
\left(
\operatorname{Retrieve}
(
\Sigma_P
)
\right)
\right)
\right)
\right)
\right]
}
$$

。

---

## 103. 企業可以把這變成正式研發流程

例如每一個 pricing proposal 都必須附：

$$
\text{Transfer Card}
$$

。

Product Review 不只問：

> 使用者喜不喜歡？

還問：

> 來源制度在哪？

> 失敗史在哪？

> 邊界差異在哪？

---

## 104. AI Agent 可以成為 Institutional Broker

未來 Agent 可以持續掃描：

- 法規；
- pricing；
- cloud products；
- utilities；
- financial markets；
- logistics。

當發現：

$$
\text{new primitive}
$$

就加入 Library。

---

## 105. 這會形成 Institution-RAG

可以建立：

$$
\boxed{
\text{Institution-RAG}
}
$$

而不是普通文件 RAG。

檢索單位不是文章，

而是：

$$
\text{mechanism card}
$$

。

---

## 106. Mechanism Card Schema

例如：

```text
name: Demand Response
problem: peak capacity shortage
actors: provider, flexible consumer
resource: time-sensitive capacity
input: forecast scarcity
mechanism: pay demand to defer/reduce
benefit: peak reduction
failure: gaming, measurement error
AI mapping: surrender / off-peak conversion
```

這比儲存整篇電力市場報告更適合 Agent 重用。

---

## 107. 多 Agent 角色分工

可以設：

### Retriever

找來源制度。

### Mapper

做 structural mapping。

### Skeptic

找 mismatch。

### Economist

算 incentive。

### Lawyer

查 regulation。

### Experimenter

設 pilot。

### Synthesizer

組合方案。

形成：

$$
\boxed{
\text{Institutional Design Agent Team}
}
$$

。

---

## 108. AI-Native Institutional R&D

這會把跨產業研究從：

$$
\text{occasional inspiration}
$$

變成：

$$
\boxed{
\text{continuous institutional R\&D}
}
$$

。

---

## 109. 市場本身也可以當實驗回饋

部署後得到：

$$
E_{\mathrm{market}}
$$

更新：

$$
\mathcal P
$$

。

因此 Library 不只是歷史案例。

它還累積：

$$
\text{own experiments}
$$

。

---

## 110. Institutional Memory Loop

形成：

$$
\boxed{
\text{Search}
\rightarrow
\text{Transfer}
\rightarrow
\text{Experiment}
\rightarrow
\text{Memory}
\rightarrow
\text{Better Search}
}
$$

。

---

## 111. 這和 AI 企業學習本身同構

AI 模型透過資料與回饋學習。

AI 公司制度也可以透過：

$$
\text{institutional feedback}
$$

學習。

所以：

$$
\boxed{
\text{learning organization}
}
$$

不只指模型訓練。

---

## 112. 可測試假說

### H1：結構化跨產業搜尋能產生比單產業 brainstorming 更多可測試方案

比較：

$$
N_{\mathrm{viable}}
$$

。

### H2：Structure-first transfer 的失敗率低於 surface analogy

預期：

$$
Failure_{\mathrm{structural}}
<
Failure_{\mathrm{surface}}
$$

。

### H3：Multi-source recombination 比單來源 copy 產生更高 contextual fit

在複合 AI 問題中尤其如此。

### H4：Boundary Critic 會降低負面移植

即：

$$
BMP_{\mathrm{postcritic}}
<
BMP_{\mathrm{precritic}}
$$

。

### H5：AI Agent 可以顯著降低跨產業制度搜尋成本

$$
C_{\mathrm{search,AI}}
<
C_{\mathrm{search,human-only}}
$$

在廣域檢索任務中可能成立。

### H6：制度知識庫會產生組織學習複利

隨：

$$
|\mathcal P|\uparrow
$$

下一次問題的搜尋時間：

$$
T_{\mathrm{solution}}\downarrow
$$

可能成立。

---

## 113. 實驗設計

選擇：

$$
20
$$

個未知產品問題。

隨機分成：

### Group A

自由 brainstorming。

### Group B

同產業 benchmark。

### Group C

Cross-Industry Transfer Pipeline。

比較：

$$
\text{novelty}
$$

$$
\text{feasibility}
$$

$$
\text{testability}
$$

$$
\text{time}
$$

$$
\text{pilot success}
$$

。

---

## 114. 還可以加入 AI-only 與 Human+AI

再比較：

$$
\text{Human}
$$

$$
\text{AI}
$$

$$
\text{Human+AI}
$$

。

這會直接測量 AI institutional brokering 的價值。

---

## 115. 風險一：類比過度自信

模型看到：

$$
SIS\uparrow
$$

可能忽略小但致命的 mismatch。

例如：

$$
m_{\mathrm{legal}}=1
$$

就足以讓制度不可部署。

因此：

$$
\boxed{
\text{critical mismatch veto}
}
$$

應存在。

---

## 116. 風險二：制度脫離歷史脈絡

某市場機制有效，

可能依賴：

- 特定監管；
- 文化；
- 競爭度；
- 基礎設施。

移植時不能只拿機制，不拿其必要背景。

---

## 117. 風險三：倖存者偏誤

成熟市場留下的制度：

$$
I_{\mathrm{survived}}
$$

不代表最優。

可能只是：

$$
\text{path dependence}
$$

。

因此應搜尋：

$$
\boxed{
\text{failed historical alternatives}
}
$$

。

---

## 118. 風險四：只移植企業有利部分

例如從航空學：

> dynamic pricing。

卻不學：

> refund rights。

這是：

$$
\boxed{
\text{selective institutional borrowing}
}
$$

。

制度移植應同時檢查 consumer side。

---

## 119. 風險五：用類比合理化既定答案

先決定：

> 我要動態漲價。

再找：

> Uber 也這樣。

這不叫制度搜尋。

這叫：

$$
\text{post hoc justification}
$$

。

---

## 120. 因此 Search 必須先於 Preference

理想流程：

$$
\boxed{
\text{Problem}
\rightarrow
\text{Candidate Mechanisms}
\rightarrow
\text{Evaluation}
\rightarrow
\text{Choice}
}
$$

而不是：

$$
\text{Choice}
\rightarrow
\text{Search for analogy}
$$

。

---

## 121. 基本原則

本文提出十八項原則。

### 原則一：AI 技術新，不代表市場問題全部新

### 原則二：成熟產業是制度實驗資料庫

### 原則三：移植關係結構，不移植表面屬性

### 原則四：先抽象問題，再搜尋來源

### 原則五：以 Institutional Primitive 為移植單位

### 原則六：明確列出 invariants 與 non-invariants

### 原則七：所有類比都要計算 boundary mismatch

### 原則八：來源制度提供 prior，不提供 proof

### 原則九：真正創新可以是 combinatorial novelty

### 原則十：多來源重組通常比單來源照搬更適合複合 AI 問題

### 原則十一：先模擬，再 pilot，再 field test

### 原則十二：制度必須通過 governance filter

### 原則十三：設定 kill criteria，避免愛上自己的類比

### 原則十四：保存 negative transfer

### 原則十五：建立 Institutional Primitive Library

### 原則十六：AI Agent 適合做跨域 institutional brokering

### 原則十七：AI Agent 必須搭配 Boundary Critic

### 原則十八：真正目標不是最大化新穎性，而是最大化問題解決價值

---

## 122. 本系列的最終回看

整個系列從一句：

> 我用不完的 AI 訂閱，為什麼不能拿去別的地方？

開始。

若只留在 AI 產業內部思考，

很容易得到：

> 改套餐。

但跨產業搜尋後，

會出現：

- Rollover；
- Capacity Reservation；
- Spot／Flex；
- Demand Response；
- Yield Management；
- Forward Contract；
- Capacity Transparency；
- Load Factor。

---

## 123. 每個東西都不完全新

但：

$$
\boxed{
\text{the configuration is new}
}
$$

。

而且新配置恰好對應：

$$
\text{AI-specific constraints}
$$

。

---

## 124. 這就是成熟市場切片方法

將成熟制度切成：

$$
p_1,p_2,\ldots,p_n
$$

。

再對 AI 目標問題求：

$$
\boxed{
X_{\mathrm{AI}}
=
p_{i_1}
\oplus
p_{i_2}
\oplus
\cdots
\oplus
p_{i_k}
}
$$

。

---

## 125. 它不是降低創新，而是提升創新效率

從零發明成本：

$$
C_{\mathrm{zero}}
$$

。

制度移植：

$$
C_{\mathrm{transfer}}
$$

。

若：

$$
C_{\mathrm{transfer}}
<
C_{\mathrm{zero}}
$$

且結果品質更高，

重用文明知識是理性的。

---

## 126. 但保留真正需要從零創新的地方

若：

$$
SIS\approx0
$$

表示沒有好的來源制度。

那就：

$$
\boxed{
\text{invent}
}
$$

。

跨產業移植不是反創新。

而是：

> 不在不必要的地方重複發明。

---

## 127. Explore vs Reuse

制度研發應平衡：

$$
\boxed{
\text{Exploration}
+
\text{Reuse}
}
$$

。

過度 reuse：

$$
\text{path dependence}
$$

。

過度 explore：

$$
\text{reinvent the wheel}
$$

。

---

## 128. AI 會讓這個平衡改變

因為 AI 大幅降低：

$$
C_{\mathrm{search}}
$$

。

因此未來企業可以更常問：

> 世界其他地方以前怎麼解過類似結構？

這會讓：

$$
\boxed{
\text{institutional search}
}
$$

變得便宜很多。

---

## 129. 這可能是 AI 對管理學的一個低估價值

AI 不只幫企業：

- 寫程式；
- 寫文案；
- 做客服。

還可以：

$$
\boxed{
\text{search the design space of institutions}
}
$$

。

---

## 130. 從知識搜尋到制度搜尋

傳統 AI 搜尋：

> 找資料。

更高階：

> 找可移植的關係結構。

即：

$$
\boxed{
\text{Knowledge Retrieval}
\rightarrow
\text{Institutional Retrieval}
}
$$

。

---

## 131. 最終方法論

本文可以濃縮為：

$$
\boxed{
\text{Do not ask only, “What has never been invented?”}
}
$$

而應再問：

$$
\boxed{
\text{“What has already been solved elsewhere under the same structural constraints?”}
}
$$

。

---

## 132. 結論

AI 產業確實仍然非常年輕。

但「年輕」不代表它面對的所有問題都第一次出現在人類歷史上。

當 AI provider 面對：

$$
\text{scarcity}
$$

$$
\text{capacity}
$$

$$
\text{subscription}
$$

$$
\text{peak demand}
$$

$$
\text{arbitrage}
$$

$$
\text{transparency}
$$

$$
\text{capital allocation}
$$

時，

世界早已有許多制度切片可供研究。

真正需要做的不是：

> 找一個產業，整套照搬。

而是：

$$
\boxed{
\text{extract relations}
\rightarrow
\text{identify primitives}
\rightarrow
\text{test structural isomorphism}
\rightarrow
\text{penalize mismatches}
\rightarrow
\text{recombine}
\rightarrow
\text{experiment}
}
$$

。

這種方法與 Gentner 的 structure-mapping、Hargadon 與 Sutton 的 technology brokering，以及策略研究中的 analogical reasoning 具有共同精神：

> 新解法常來自對既有知識的重新映射與重新組合。

但 AI 時代可以再多走一步。

AI Agent 可以：

- 跨數百產業搜尋；
- 抽取制度 primitive；
- 建立 structural graph；
- 找出 mismatch；
- 模擬使用者；
- 設計 pilot；
- 持續更新制度記憶。

因此：

$$
\boxed{
\text{institutional innovation itself can become an AI-assisted search problem}
}
$$

。

本系列中的 Temporal Fungibility、Compute Wallet、Reversible Entitlement、Demand Engineering、Capacity Transparency 與 Compute Fundamentals，都可以被看成這個方法的產物。

它們並不是每一個零件都前所未有。

真正的價值在於：

$$
\boxed{
\text{validated fragments}
+
\text{new constraints}
+
\text{new recombination}
=
\text{new institutional architecture}
}
$$

。

這也使整個系列最後的核心命題可以寫成：

$$
\boxed{
\text{Innovation does not require novelty at every layer; novel systems can emerge from validated institutional fragments recombined under new constraints.}
}
$$

中文即：

**創新不要求每一層都全新；真正的新制度，完全可以由已驗證的成熟制度切片，在新的技術與約束下重新組合而成。**

因此，AI 企業不需要每一次都重新發明市場。

它們更需要學會：

> **如何搜尋市場曾經學過的東西。**

而在 AI 本身已經能跨領域搜尋、比較、建模與模擬的時代，

這種能力反而可能成為下一階段最值得系統化的企業能力之一：

$$
\boxed{
\text{Institutional Intelligence}
}
$$

——理解制度、搜尋制度、移植制度、驗證制度，並讓制度與技術共同演化的能力。

**《AI 算力經濟：從訂閱額度到自適應容量市場》系列至此完成。**

---

## 參考資料

1. Gentner, D. *Structure-Mapping: A Theoretical Framework for Analogy.* Cognitive Science, 7(2), 155–170, 1983. DOI: 10.1207/s15516709cog0702_3.
2. Hargadon, A., & Sutton, R. I. *Technology Brokering and Innovation in a Product Development Firm.* Administrative Science Quarterly, 42(4), 716–749, 1997.
3. Gavetti, G., Levinthal, D. A., & Rivkin, J. W. *Strategy Making in Novel and Complex Worlds: The Power of Analogy.* Strategic Management Journal, 26(8), 691–712, 2005.
4. Statler, M., Jacobs, C. D., & Roos, J. *Performing Strategy—Analogical Reasoning as Strategic Practice.* Scandinavian Journal of Management, 24(2), 133–144, 2008.
5. Cohen, W. M., & Levinthal, D. A. *Absorptive Capacity: A New Perspective on Learning and Innovation.* Administrative Science Quarterly, 35(1), 128–152, 1990.
6. Federal Energy Regulatory Commission. *Understanding Wholesale Capacity Markets.* Updated 2026-06-02.
7. Federal Energy Regulatory Commission. *Demand Response.* Accessed 2026-09-07.
8. Amazon Web Services. *Amazon EC2 Spot Instances Pricing.* Accessed 2026-09-07.
9. Amazon Web Services. *Capacity Reservation pricing and billing — Amazon EC2.* Accessed 2026-09-07.
10. Amazon Web Services. *Amazon EC2 Reserved Instances.* Accessed 2026-09-07.
11. Amazon Web Services. *Service tiers for optimizing performance and cost — Amazon Bedrock.* Accessed 2026-09-07.
12. Ronald H. Coase. *The Nature of the Firm.* Economica, 4(16), 386–405, 1937.
13. Oliver E. Williamson. *The Economic Institutions of Capitalism.* Free Press, 1985.
14. Douglass C. North. *Institutions, Institutional Change and Economic Performance.* Cambridge University Press, 1990.
15. James G. March. *Exploration and Exploitation in Organizational Learning.* Organization Science, 2(1), 71–87, 1991.

---

## Complete Series Navigation

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

**Paper 8**  
AI 市場的制度演化：從商品化到容量市場

**Extra 1 / Paper 9**  
Token 消耗症候群：到期額度如何反向塑造人的認知行為

**Extra 2 / Paper 10 — 本篇**  
跨產業制度移植：AI 產業其實不用每件事重新發明
