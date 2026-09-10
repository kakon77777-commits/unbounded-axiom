# 閒置額度、轉讓與供應商回購：AI 使用權的可逆性
## Idle Allowances, Transfer, and Provider Buyback: Reversibility of AI Service Entitlements

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Paper 4 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

當 AI 訂閱逐漸從固定會員權益演化為具有可觀測額度、額外 credits、跨功能使用池與彈性超額付費的混合制度後，一個更困難的制度問題自然出現：**未使用的 AI 使用權是否只能單向失效，還是可以被返還、轉換、轉讓，甚至由供應商主動收回？**

本文提出 **Reversible AI Entitlement（可逆 AI 使用權）** 框架，並區分四種經常被混淆的行為：帳號共享、第三方轉售、供應商控制下的權利轉換，以及供應商回購／surrender。本文強調，使用者的「未用額度」並不等於擁有一塊實體 GPU，也不必然構成可自由交易的財產；真正可以被制度化的，是在契約與產品規則下，使用者對未來服務能力、優先權、額度或可執行工作量所持有的某種 entitlement。

截至 2026 年 9 月，OpenAI 的 Service Credit Terms 明確將 Service Credits 定義為非貨幣、非個人財產權且不可轉讓、出售、贈與或交易；OpenAI 同時已開始推出「另行購買新的 gift credits 給其他帳號」的機制，卻明確區分其與既有 credit balance 的轉移。Anthropic 的消費者條款亦禁止分享帳號憑證、將帳號提供給他人，以及轉售服務。這些規則證明現行制度主要採取「身份綁定、權利不可轉讓」模式，但也同時顯示：**供應商技術上完全可以設計受控的價值移轉，只是目前沒有把既有使用權普遍定義成可移轉資產。**

本文因此不主張將現有訂閱額度直接金融化，也不主張允許第三方任意建立訂閱轉 API 市場。相反地，本文提出一個較保守且可測試的演化方向：供應商可以允許使用者主動 **surrender** 某部分未來使用權或優先服務權，並以 Compute Credits、續訂折抵、離峰額度、未來功能額度或其他非現金補償回饋。這種機制本質上不是「企業買回自己的 GPU」，而是企業買回或消滅一部分 **未來需求請求權**。

本文進一步定義 Entitlement Reversibility Ratio、Transferability Ratio、Latent Demand Liability、Surrender Value、Provider Shadow Price 與 Reclaim Efficiency，並提出反套利、身份隔離、動態報價與需求響應實驗。其核心命題為：

$$
\boxed{
\text{Unused AI entitlement need not be transferable property to become reversible.}
}
$$

亦即：

**未使用的 AI 使用權不必先被定義為可自由交易的財產，才能被設計成可返還、可轉換、可由供應商收回的權利。**

**關鍵詞：** AI 使用權、Reversible Entitlement、Compute Wallet、Surrender、Buyback、Subscription Resale、Credits、Demand Response、套利、AI 算力市場

---

## 1. 從 Compute Wallet 到「方向性」問題

前篇提出：

$$
\boxed{
\text{Compute Wallet}
}
$$

作為：

$$
\text{Subscription}
\leftrightarrow
\text{Usage Interfaces}
$$

之間的抽象資源帳本。

一旦存在 Wallet，資源流可以包含：

$$
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
$$

但目前多數 AI 產品中的資源流仍然高度單向：

$$
\text{Money}
\rightarrow
\text{Subscription / Credits}
\rightarrow
\text{Usage}
$$

若沒有使用，則：

$$
\text{Unused Entitlement}
\rightarrow
\text{Expiration}
$$

因此產生一個新的制度問題：

> 為什麼使用權只能被取得與消耗，卻不能被返還？

這就是本文所謂的：

$$
\boxed{
\text{Directionality of Entitlement}
}
$$

---

## 2. 使用者沒有買下一塊 GPU

討論「把剩餘額度賣回供應商」時，最容易產生的概念錯誤是：

> 我有 100 CU 沒使用，所以我擁有 100 CU 的實體算力。

這通常不成立。

訂閱制度真正提供的更接近：

$$
E_i
=
\text{contractual right to access service under defined conditions}
$$

而不是：

$$
E_i
=
\text{exclusive ownership of physical compute}
$$

供應商通常採取共享容量與統計多工。

因此：

$$
\sum_i E_i
$$

完全可能大於同一瞬間的：

$$
C(t)
$$

因為供應商假設所有使用者不會同時把最大 entitlement 全部兌現。

這與航空、電信、雲端、保險與其他容量市場中的 oversubscription 或 statistical multiplexing 結構相似。

因此：

$$
\boxed{
\text{unused allowance}
\neq
\text{unused physical GPU reserved for that user}
}
$$

---

## 3. 真正可以回購的是「未來請求權」

如果供應商本來就擁有硬體，那麼「回購算力」在字面上不精確。

更合理的描述是：

$$
\boxed{
\text{Provider buys back future service claims}
}
$$

或者：

$$
\boxed{
\text{User surrenders future entitlement}
}
$$

令使用者 $i$ 在時刻 $t$ 的剩餘 entitlement 為：

$$
E_i(t)
$$

使用者選擇 surrender：

$$
s_i(t)
\leq
E_i(t)
$$

則新的 entitlement 為：

$$
E_i'(t)
=
E_i(t)-s_i(t)
$$

供應商給予補償：

$$
R_i
=
g(s_i,t,L(t),P_i)
$$

其中：

- $s_i$：返還量；
- $L(t)$：平台負載或預測負載；
- $P_i$：使用權類型、優先級或方案；
- $R_i$：供應商支付的補償。

因此，這不是：

$$
\text{GPU}
\rightarrow
\text{Provider}
$$

而是：

$$
\boxed{
\text{Future Claim}
\rightarrow
\text{Extinguished / Reduced}
}
$$

---

## 4. 四種必須分離的制度

「轉讓額度」其實至少包含四個完全不同的結構。

### 4.1 Account Sharing

$$
E_A
+
I_A
\rightarrow
U_B
$$

其中 $I_A$ 是 A 的身份與帳號憑證。

B 直接使用 A 的帳號。

這會混合：

- 身份；
- 記憶；
- 付款；
- 隱私；
- 安全責任；
- 使用政策。

因此它是最不適合作為正式資源市場的方式。

---

### 4.2 Third-Party Resale

$$
E_A
\rightarrow
G
\rightarrow
\{U_1,U_2,\ldots,U_n\}
$$

其中 $G$ 是第三方 gateway。

這就是訂閱轉 API、帳號池與中轉服務可能採用的結構。

它的主要問題不是「技術上做不到」，而是它繞過了供應商對：

$$
\text{identity}
,\quad
\text{pricing}
,\quad
\text{rate control}
,\quad
\text{authorization}
$$

的制度控制。

---

### 4.3 Provider-Mediated Transfer

$$
E_A
\rightarrow
P
\rightarrow
E_B
$$

其中 $P$ 是供應商。

A 與 B 都維持自己的身份與帳號。

這種制度如果被供應商明確授權，就不存在共享密碼的必要。

---

### 4.4 Provider Surrender / Buyback

$$
E_A
\rightarrow
P
\rightarrow
\varnothing
$$

A 的某部分 entitlement 被消滅或延後，平台給予補償。

這裡沒有 B。

因此：

$$
\boxed{
\text{Surrender}
\neq
\text{Secondary Market Transfer}
}
$$

它更接近 demand response。

---

## 5. 現行制度：不可轉讓，但已有受控贈與

截至 2026 年 9 月，OpenAI 的 Service Credit Terms 對 Service Credits 採取非常明確的限制。

其核心規則包括：

- credits 不是法定貨幣；
- 不具有法定貨幣等值；
- 不構成個人財產權；
- 不可轉讓；
- 不可出售；
- 不可交易；
- 除法律要求外不可兌回現金。

這表示現行制度中的：

$$
W_i
$$

不是使用者可自由處分的金融資產。

但同時，OpenAI 已經開始提供 **gifting credits**。

其結構是：

$$
\text{New Purchase by A}
\rightarrow
\text{Provider Claim Link}
\rightarrow
\text{Credit for B}
$$

而不是：

$$
W_A
\rightarrow
W_B
$$

官方說明特別區分：

> 購買 gift 不會把既有 credit balance 轉出。

這是一個非常重要的制度訊號。

因為它證明：

$$
\boxed{
\text{Provider-controlled value transfer is technically feasible}
}
$$

只是供應商目前選擇：

$$
\text{newly purchased value can move}
$$

而：

$$
\text{existing entitlement cannot move}
$$

---

## 6. Anthropic 的身份與轉售邊界

Anthropic 的 Consumer Terms 同樣採取身份綁定模式。

其條款明確禁止：

$$
\text{Account Credentials}
\rightarrow
\text{Another Person}
$$

也禁止：

$$
\text{Resell Services}
$$

並且原則上禁止在非 API Key 或未另行允許時，以 bot、script 或其他非人類方式存取服務。

這說明目前主流消費 AI 的契約邏輯仍然是：

$$
\boxed{
\text{personal entitlement}
+
\text{non-transferability}
}
$$

而 API 則被視為另一種具有不同自動化與商業權利的產品。

因此，從政策現況來看，使用者不能因為「這個月沒用完」就自行推出一個合法二級市場。

但這是：

$$
\text{current contract design}
$$

不是：

$$
\text{technical impossibility}
$$

也不是經濟學上永遠不可改變的定律。

---

## 7. Transferability 與 Reversibility 必須分離

本文提出：

$$
\boxed{
\text{Transferability}
\neq
\text{Reversibility}
}
$$

令：

$$
T_R
=
\frac{
\text{entitlement legally transferable to another user}
}{
\text{total entitlement}
}
$$

定義為 Transferability Ratio。

再令：

$$
R_E
=
\frac{
\text{entitlement returnable to provider}
}{
\text{total entitlement}
}
$$

定義為 Entitlement Reversibility Ratio。

完全可能存在：

$$
T_R=0
$$

但：

$$
R_E>0
$$

也就是：

> 不允許你把額度賣給別人，但允許你返還給供應商換取某種補償。

這可能是比直接建立二級市場更容易實施的第一步。

---

## 8. 為什麼供應商可能願意收回使用權

假設平台預測未來某時間窗：

$$
D(t+\tau)>C(t+\tau)
$$

通常可採取：

$$
\text{Rate Limit}
$$

$$
\text{Queue}
$$

$$
\text{Capacity Expansion}
$$

或：

$$
\text{Model Degradation}
$$

但如果部分使用者其實不急，平台可以改成：

$$
\text{Offer Compensation}
\rightarrow
\text{Voluntary Surrender}
$$

使潛在需求下降：

$$
D'(t+\tau)
=
D(t+\tau)
-
\Delta D_{\mathrm{surrender}}
$$

因此：

$$
\boxed{
\text{Buyback}
=
\text{Demand Reduction Procurement}
}
$$

而不是實體資產回購。

---

## 9. Latent Demand Liability

對訂閱供應商而言，已售出的 entitlement 具有某種未來需求負債。

這不是會計上的正式 liability 定義，而是一個容量規劃概念。

令使用者 $i$ 尚未使用的 entitlement 為：

$$
e_i(t)
$$

其在未來窗口實際兌現的機率為：

$$
p_i(t,\tau)
$$

則可定義 **Latent Demand Liability**：

$$
LDL(t,\tau)
=
\sum_i
p_i(t,\tau)e_i(t)
$$

這表示：

> 已經存在於使用者帳戶中、未來可能被兌現的預期服務需求。

如果大量高頻使用者同時接近重置前、產品發布後或專案高峰，則：

$$
LDL(t,\tau)\uparrow
$$

即使當下：

$$
D(t)
$$

仍然不高。

因此 Wallet telemetry 可以讓企業看見：

$$
\boxed{
\text{future claim pressure}
}
$$

---

## 10. Surrender 如何降低 Latent Demand

如果使用者 $i$ surrender：

$$
s_i
$$

則：

$$
e_i'
=
e_i-s_i
$$

預期需求負債下降：

$$
\Delta LDL_i
=
p_i s_i
$$

若有 $n$ 名使用者參與：

$$
\Delta LDL
=
\sum_{i=1}^{n}p_i s_i
$$

這並不代表平台立刻得到同等物理 capacity。

因為某些人即使不 surrender，最後也可能根本不使用。

因此：

$$
\boxed{
\text{Surrendered Entitlement}
\neq
\text{Reclaimed Physical Capacity}
}
$$

真正價值應依：

$$
p_i
$$

折算。

這是設計回購制度時非常重要的精算問題。

---

## 11. Provider Shadow Price

假設平台在某時間窗的邊際容量價值為：

$$
\lambda(t)
$$

若某一 surrender 預期降低需求：

$$
\Delta D_i
$$

則平台對這次返還的最高合理經濟價值可以近似表示為：

$$
V_{P,i}
=
\lambda(t)\Delta D_i
$$

若給使用者的補償為：

$$
R_i
$$

供應商只有在：

$$
R_i<V_{P,i}
$$

時具有直接容量經濟誘因。

因此回購價格不需要固定。

可以是：

$$
R_i
=
h(
L(t),
\hat D(t+\tau),
p_i,
s_i
)
$$

當未來供需更緊張：

$$
R_i\uparrow
$$

當供應充足：

$$
R_i\downarrow
$$

甚至：

$$
R_i=0
$$

也就是平台根本不提出回購。

---

## 12. 使用者的 Surrender Reservation Price

使用者也有自己的最低接受價格。

令使用者對保留 entitlement 的主觀價值為：

$$
V_{U,i}
$$

則只有當：

$$
R_i\geq V_{U,i}
$$

使用者才願意 surrender。

因此市場形成：

$$
\boxed{
V_{U,i}
\leq
R_i
<
V_{P,i}
}
$$

才有互利交易空間。

這與電力 Demand Response 的結構非常相似。

供應商不是強迫使用者不用，而是：

> 用價格購買需求彈性。

---

## 13. 不一定需要支付現金

第一版制度若直接允許：

$$
R_i=\text{cash}
$$

會迅速增加：

- 套利；
- 洗錢／支付監管；
- 稅務；
- 儲值工具；
- 機器人大量養號；
- 多帳號 harvesting；

等問題。

因此較低風險的第一版是：

$$
R_i
\in
\{
\text{future CU},
\text{subscription discount},
\text{off-peak bonus},
\text{feature credit},
\text{priority voucher}
\}
$$

即：

$$
\boxed{
\text{service value}
\rightarrow
\text{service value}
}
$$

而不是：

$$
\text{service value}
\rightarrow
\text{cash}
$$

這保留了可逆性，卻降低金融化程度。

---

## 14. Haircut：返還不應 1:1

若使用者可以：

$$
100\ \mathrm{CU}
\rightarrow
100\ \mathrm{CU\ future}
$$

甚至兌回等值現金，可能使平台承擔過高未來負債。

因此可設定：

$$
R_i
=
\alpha s_i
$$

其中：

$$
0<\alpha<1
$$

例如：

$$
\alpha=0.5
$$

表示 surrender 100 CU 只獲得 50 Future CU。

這個 haircut 可以反映：

- 原額度本來可能根本不會被使用；
- 返還的時間價值；
- 反套利需求；
- 平台的行政與容量風險；
- 不同資源時段的價值差。

---

## 15. 動態 Surrender Offer

平台可以在預測到尖峰之前發布：

> 未來 24 小時高階推理需求偏高。  
> 放棄 100 Priority CU，可獲得 70 Future CU。

形式化：

$$
R(t,\tau)
=
\alpha(t,\tau)s
$$

當：

$$
\hat L(t+\tau)\uparrow
$$

則：

$$
\alpha(t,\tau)\uparrow
$$

這樣供應商開始從：

$$
\text{reactive rate limiting}
$$

轉向：

$$
\boxed{
\text{proactive entitlement management}
}
$$

---

## 16. 使用權回購比直接漲價更柔和

面對尖峰，另一種做法是：

$$
P_{\mathrm{peak}}\uparrow
$$

但這會讓使用者感覺：

> 因為你們容量不足，所以我現在被加價。

Surrender 機制則反過來：

$$
\text{keep baseline terms}
+
\text{pay volunteers to defer}
$$

它是一種：

$$
\boxed{
\text{positive incentive}
}
$$

而不是：

$$
\text{scarcity penalty}
$$

兩者都可以調節需求，但產品心理完全不同。

---

## 17. Surrender 與 Off-Peak Discount 可以組合

假設使用者原有：

$$
100\ \mathrm{Priority\ CU}
$$

平台可以提供：

$$
100\ \mathrm{Priority\ CU}
\rightarrow
140\ \mathrm{OffPeak\ CU}
$$

使用者並沒有失去所有價值，而是：

$$
\text{Priority}
\rightarrow
\text{Quantity}
$$

也就是用時間彈性交換更多算力。

這是一種：

$$
\boxed{
\text{temporal exchange rate}
}
$$

對不急的 Agent workload 特別合理。

---

## 18. Provider Buyback 與二級市場的根本差異

若 A 將額度出售給 B：

$$
A\rightarrow B
$$

總 entitlement 不一定下降：

$$
E_{\mathrm{total}}'
=
E_{\mathrm{total}}
$$

甚至 B 比 A 更可能立即使用，因此：

$$
D_{\mathrm{expected}}\uparrow
$$

但如果 A surrender 給供應商：

$$
A\rightarrow P\rightarrow\varnothing
$$

則：

$$
E_{\mathrm{total}}'
<
E_{\mathrm{total}}
$$

因此：

$$
LDL\downarrow
$$

所以從容量管理角度：

$$
\boxed{
\text{Secondary Transfer}
\neq
\text{Demand Reduction}
}
$$

這也是為什麼供應商可能願意接受 buyback，卻仍然不願意接受自由轉售。

---

## 19. Provider-Mediated Transfer 仍然有價值

雖然 buyback 對容量管理更直接，但有限制的官方轉讓市場仍有其他價值。

例如：

$$
A:\text{unused}
$$

$$
B:\text{urgent shortage}
$$

如果供應商容量足夠：

$$
L(t)<L_{\mathrm{safe}}
$$

可以允許：

$$
E_A
\rightarrow
\alpha E_B
$$

其中：

$$
0<\alpha<1
$$

平台收取 conversion haircut：

$$
1-\alpha
$$

如此可以同時：

- 保留身份隔離；
- 阻止帳號共享；
- 控制總量；
- 收取平台費；
- 限制轉售次數；
- 追蹤資金與 entitlement 流。

這比非官方 gateway 更可治理。

---

## 20. Gift Credits 是一個重要制度先例

OpenAI 現行 gifting credits 的意義不只在於「可以送禮」。

真正值得觀察的是：

$$
\boxed{
\text{Provider-mediated claim transfer}
}
$$

已經存在。

供應商可以：

- 建立 claim link；
- 驗證接收帳號；
- 限制可用方案；
- 限制地區與貨幣；
- 設定期限；
- 監控詐欺；
- 明確區分 gift purchase 與 existing balance。

因此，一個未來的：

$$
\text{Authorized Entitlement Transfer}
$$

在技術架構上並不神秘。

真正缺的是：

$$
\text{contractual authorization}
+
\text{economic design}
$$

---

## 21. Reclaim Efficiency

為了衡量回購到底有沒有真的幫助容量，可定義：

$$
RE
=
\frac{
\text{expected demand actually removed}
}{
\text{surrendered entitlement}
}
$$

即：

$$
RE
=
\frac{\Delta D_{\mathrm{real}}}{S}
$$

若：

$$
RE\approx0
$$

代表平台花補償買回了一批本來就不會被使用的額度。

若：

$$
RE\approx1
$$

則代表回購非常有效地降低了真實需求。

因此供應商需要利用歷史行為預測：

$$
p_i(t,\tau)
$$

而不是對所有 unused entitlement 給相同價格。

---

## 22. 但不能懲罰高使用機率者

若回購價格完全依：

$$
p_i
$$

設定，可能出現另一個公平問題：

> 重度使用者反而被平台標記成更昂貴或更值得「買走使用權」的人。

因此個人化報價需要非常謹慎。

較好的設計可以使用：

$$
\text{segment-level pricing}
$$

或：

$$
\text{capacity-window pricing}
$$

而非對每個人的習慣做高度不透明的價格歧視。

例如所有 Pro 使用者在同一時段看到：

> 返還 100 Priority CU → 70 Future CU。

這比每個人出不同價更容易建立信任。

---

## 23. 反套利設計

可逆使用權若沒有反套利設計，可能出現：

$$
\text{Buy Subscription}
\rightarrow
\text{Never Use}
\rightarrow
\text{Harvest Rewards}
$$

因此至少需要以下機制。

### 23.1 Reward Ceiling

$$
R_i
\leq
R_{\max}
$$

每期返還收益有上限。

### 23.2 No Positive-Cash Arbitrage

確保：

$$
E[R_i]
<
P_{\mathrm{subscription}}
$$

不能讓「專門不用服務」成為穩定獲利策略。

### 23.3 Identity Bound

回購必須發生於：

$$
\text{user}
\leftrightarrow
\text{provider}
$$

不能讓 bot farm 大量匿名生成 entitlement。

### 23.4 Cooling / Vesting Period

新購方案不立即具有完整 surrender 權。

### 23.5 Non-Cash First

早期以 Future CU、折抵與 priority vouchers 為主。

### 23.6 Dynamic Offer Only

不是任何時候都可以返還。

只有平台存在：

$$
V_P>0
$$

時才出價。

---

## 24. 使用者保護

可逆制度不能變成另一種操縱。

例如供應商不應先故意降低 capacity，再用小額 reward 誘導使用者放棄原本應有的服務。

因此需要：

$$
\boxed{
\text{Baseline Entitlement Protection}
}
$$

至少包括：

- 原方案基本權利清楚；
- surrender 完全自願；
- 拒絕 surrender 不受懲罰；
- 返還後的影響明確；
- 補償與有效期明確；
- 不使用誤導性倒數計時；
- 不隱藏原先可以正常使用的方案。

這使：

$$
\text{Demand Response}
$$

不會退化成：

$$
\text{Dark Pattern Capacity Reduction}
$$

---

## 25. 法律與監管邊界

如果 Compute Credits 可以：

$$
\text{freely transfer}
$$

$$
\text{redeem for cash}
$$

$$
\text{trade between users}
$$

甚至：

$$
\text{appreciate in value}
$$

那麼它可能逐漸接近：

- stored value；
- payment instrument；
- transferable financial claim；
- taxable secondary-market asset；

等更複雜的法律領域。

因此：

$$
\boxed{
\text{more liquidity}
\Rightarrow
\text{more regulation}
}
$$

這也是為什麼早期制度更合理的方向可能是：

$$
\text{non-transferable}
+
\text{provider-reversible}
$$

而不是直接建立公開交易所。

本文不對任何特定司法管轄區作法律判定；實際產品仍需依支付、消費者保護、稅務、證券、儲值工具與數位服務相關法律另行審查。

---

## 26. 可逆性不必等於財產化

這是一個理論上非常重要的區分。

傳統思路容易認為：

$$
\text{reversible}
\Rightarrow
\text{property}
$$

但並非如此。

例如某服務商可以在契約中約定：

> 你可以放棄某項未來權利，並取得方案折抵。

這是一種：

$$
\text{contractual option}
$$

不一定代表使用者擁有：

$$
\text{freely alienable property right}
$$

因此可以建立：

$$
\boxed{
\text{Reversible but Non-Transferable Entitlement}
}
$$

這可能正是 AI 訂閱制度最容易跨出的第一步。

---

## 27. Reversibility Ladder

本文提出一個五階制度成熟度。

### Level 0：Expiration Only

$$
E
\rightarrow
0
$$

不用即失效。

### Level 1：Rollover

$$
E_t
\rightarrow
E_{t+1}
$$

部分跨期。

### Level 2：Conversion

$$
E_A
\rightarrow
\alpha E_B
$$

不同服務權利間轉換。

### Level 3：Provider Surrender

$$
E
\rightarrow
P
\rightarrow
R
$$

返還供應商取得補償。

### Level 4：Provider-Mediated Transfer

$$
E_A
\rightarrow
P
\rightarrow
E_B
$$

受控轉讓。

### Level 5：Open Secondary Market

$$
E_A
\leftrightarrow
E_B
$$

自由市場化。

並不是所有產品都必須走到 Level 5。

事實上：

$$
\boxed{
\text{Level 3 may capture much of the economic benefit with far lower risk.}
}
$$

---

## 28. 與電力 Demand Response 的結構同構

電力系統尖峰時不一定只增加供給。

也可以：

$$
\text{pay consumers to reduce demand}
$$

AI 供應商面臨的問題具有類似結構：

$$
D_{\mathrm{AI}}(t)>C_{\mathrm{AI}}(t)
$$

除了新增 GPU：

$$
C_{\mathrm{AI}}(t)\uparrow
$$

也可以：

$$
D_{\mathrm{AI}}(t)\downarrow
$$

透過：

$$
\text{Surrender}
+
\text{Delay}
+
\text{Off-Peak Conversion}
$$

完成。

因此：

$$
\boxed{
\text{AI Entitlement Buyback}
\approx
\text{AI Demand Response}
}
$$

這並非完全相同的產業，但制度結構具有高度可比性。

---

## 29. 一個簡化的 Buyback Market

假設平台希望在未來六小時降低：

$$
\Delta D^*=100,000\ \mathrm{CU}
$$

平台發布：

$$
r=0.5
$$

表示：

$$
100\ \mathrm{Priority\ CU}
\rightarrow
50\ \mathrm{Future\ CU}
$$

使用者提交 surrender：

$$
s_1,s_2,\ldots,s_n
$$

平台估計有效降低量：

$$
\widehat{\Delta D}
=
\sum_i p_i s_i
$$

當：

$$
\widehat{\Delta D}
\geq
\Delta D^*
$$

停止接受新的 surrender。

如果不足：

$$
r\uparrow
$$

直到：

$$
S(r)
$$

足以達到需求降低目標。

這就是一個簡化的：

$$
\boxed{
\text{reverse capacity auction}
}
$$

---

## 30. 對使用者的介面可以非常簡單

底層制度可以很複雜，但 UI 不需要如此。

例如：

> **明晚預計高負載**  
> 你可以保留原額度，不需做任何事。  
>   
> 或選擇：  
> 返還 100 Priority CU  
> → 獲得 70 Future CU  
> → 另送 10 Off-Peak CU

只有三個選項：

- 保留；
- 返還；
- 改為離峰。

使用者不需要理解：

$$
LDL,\lambda,p_i,RE
$$

這些都應由平台內部處理。

---

## 31. 可測試假說

### H1：Provider Surrender 可以降低預測尖峰需求

若：

$$
R_E>0
$$

且補償足夠，則：

$$
\hat D_{\mathrm{peak}}\downarrow
$$

---

### H2：非現金補償足以誘發部分需求彈性

對低急迫性使用者：

$$
V_{U,i}
$$

可能低於 Future CU 的主觀價值。

因此未必需要現金市場。

---

### H3：Provider Buyback 的 Reclaim Efficiency 高於自由轉讓

因為自由轉讓：

$$
E_A\rightarrow E_B
$$

不一定降低需求，

而 surrender：

$$
E_A\rightarrow\varnothing
$$

直接降低 entitlement。

---

### H4：完全可轉讓會提高套利與帳號市場風險

預期：

$$
T_R\uparrow
\Rightarrow
A_{\mathrm{arbitrage}}\uparrow
$$

若缺乏身份與定價控制。

---

### H5：受控 gift／transfer 可以降低帳號共享誘因

若官方提供：

$$
\text{Provider-mediated Transfer}
$$

則部分原本透過共享帳號完成的需求可能轉入官方渠道。

---

### H6：透明的 surrender offer 比隱性限流具有更高信任度

使用者可能更接受：

> 「現在容量緊張，我們補償你晚點用。」

而不是：

> 「你已達限制，請稍後再試。」

這需要實證驗證，但具有明確產品假說價值。

---

## 32. 實驗設計

可在自願參與的使用者中測試四組。

### Group A：Control

只有原始額度與 expiration。

### Group B：Rollover

允許部分：

$$
E_t\rightarrow E_{t+1}
$$

### Group C：Surrender

高負載預測時提供：

$$
E_t\rightarrow Future\ CU
$$

### Group D：Surrender + Off-Peak Conversion

允許：

$$
Priority\ CU
\rightarrow
\alpha OffPeak\ CU
$$

觀察：

$$
D_{\mathrm{peak}}
$$

$$
RE
$$

$$
Retention
$$

$$
User\ Trust
$$

$$
Artificial\ Consumption
$$

$$
Gross\ Margin
$$

$$
Capacity\ Cost
$$

即可驗證制度是否具實際效益。

---

## 33. 對供應商的真正價值

這套制度的企業價值不是「少送一些額度」。

而是把：

$$
\text{unknown future demand}
$$

轉成：

$$
\text{partially priced demand elasticity}
$$

平台開始知道：

> 有多少需求可以延後？

> 要給多少補償才會延後？

> 哪些 workload 幾乎沒有時間彈性？

> 哪些 entitlement 長期不會被兌現？

因此：

$$
\boxed{
\text{Reversibility}
\rightarrow
\text{Demand Discovery}
}
$$

它同時是一個產品機制與需求研究機制。

---

## 34. 對投資與容量規劃的延伸

若企業開始記錄：

$$
R_E
$$

$$
LDL
$$

$$
RE
$$

與：

$$
S(r)
$$

就能得到非常有價值的容量資料。

例如：

> 本季 35% 的 Agent workload 願意延後六小時。

或者：

> 每提供 20% Future CU bonus，可移動 12% 的尖峰需求。

這些資訊將直接影響：

$$
\text{CapEx Planning}
$$

$$
\text{GPU Procurement}
$$

$$
\text{Power Contracting}
$$

與：

$$
\text{Data Center Scheduling}
$$

這也為本系列後續「容量透明度作為投資工具」建立基礎。

---

## 35. 基本原則

本文提出九項原則。

### 原則一：未用額度不是實體 GPU 所有權

$$
\text{Entitlement}
\neq
\text{Physical Asset}
$$

### 原則二：Transferability 與 Reversibility 必須分離

$$
T_R
\neq
R_E
$$

### 原則三：第一階段可以只允許返還，不允許自由轉售

$$
T_R=0,\quad R_E>0
$$

### 原則四：回購的是未來需求請求權

不是供應商自己的硬體。

### 原則五：Buyback 應由需求影子價格驅動

$$
R_i<V_{P,i}
$$

才具有直接經濟合理性。

### 原則六：返還不必支付現金

Future CU、折抵與離峰 bonus 均可成為補償。

### 原則七：避免正套利

$$
E[R_i]<P_{\mathrm{subscription}}
$$

### 原則八：所有 surrender 都應完全自願

拒絕返還不應降低原有權利。

### 原則九：市場制度應先解決真實需求，再決定是否金融化

不要因為「可以交易」就自動建立公開二級市場。

---

## 36. 限制

第一，本文的 entitlement、LDL 與 CU 是制度模型，不代表任何現行 AI 公司已採用相同會計處理。

第二，未使用額度的真實未來兌現機率：

$$
p_i
$$

難以準確預測。

第三，回購制度本身可能改變行為，使：

$$
p_i
$$

內生化。

第四，過度個人化報價可能造成公平與信任問題。

第五，若 credits 開始高度可轉讓、可兌現或具有二級市場價格，可能產生新的金融、支付、稅務與監管問題。

第六，現行 OpenAI 與 Anthropic 的服務條款並未普遍承認本文提出的自由轉讓或 provider buyback 權利；本文描述的是產品與制度設計空間，而非對現有契約權利的法律主張。

---

## 37. 結論

最初的問題可以非常簡單：

> 我這個月根本用不完，為什麼不能把剩下的給別人？

但深入之後，至少要區分：

$$
\boxed{
\text{Account Sharing}
}
$$

$$
\boxed{
\text{Third-Party Resale}
}
$$

$$
\boxed{
\text{Provider-Mediated Transfer}
}
$$

與：

$$
\boxed{
\text{Provider Surrender}
}
$$

它們的身份、安全、容量與經濟效果完全不同。

現行 AI 服務普遍採取：

$$
\text{non-transferable personal entitlement}
$$

具有充分的安全與商業理由。

但：

$$
\text{non-transferable}
$$

並不必然推出：

$$
\text{irreversible}
$$

一個使用權完全可以：

$$
\text{不可賣給第三者}
$$

卻同時：

$$
\text{可以返還給供應商}
$$

因此本文提出：

$$
\boxed{
\text{Reversible but Non-Transferable AI Entitlement}
}
$$

作為比自由二級市場更保守、更容易實驗的制度階段。

對使用者而言，它降低 unused entitlement 的浪費。

對供應商而言，它提供：

$$
\text{Demand Response}
+
\text{Capacity Relief}
+
\text{Demand Discovery}
$$

對市場而言，它讓原本只有：

$$
\text{buy}
\rightarrow
\text{use}
\rightarrow
\text{expire}
$$

的單向 AI 訂閱，第一次具備：

$$
\boxed{
\text{buy}
\leftrightarrow
\text{hold}
\leftrightarrow
\text{convert}
\leftrightarrow
\text{surrender}
}
$$

的可逆性。

因此，本篇的核心命題是：

$$
\boxed{
\text{Unused AI entitlement need not be transferable property to become reversible.}
}
$$

中文即：

**未使用的 AI 使用權不必先成為可自由交易的財產，才能被設計成可返還、可轉換與可由供應商收回的權利。**

而一旦供應商開始以價格或額度誘因主動購買需求彈性，下一步就不再只是「如何處理未用額度」。

而是：

> 如何主動把尖峰需求搬到低峰？

這正是下一篇：

**從 Rate Limiting 到 Demand Engineering：離峰折扣與 AI 需求響應。**

---

## 參考資料

1. OpenAI. *Service Credit Terms.* Updated 2026-01-01.  
   https://openai.com/policies/service-credit-terms/

2. OpenAI Help Center. *Gifting credits in ChatGPT.* Accessed 2026-09-07.  
   https://help.openai.com/en/articles/20001417-gifting-credits-in-chatgpt

3. OpenAI Help Center. *OpenAI Account Sharing Policy.* Accessed 2026-09-07.  
   https://help.openai.com/en/articles/10471989

4. OpenAI Help Center. *Using Credits for Flexible Usage in ChatGPT (Personal plans).* Accessed 2026-09-07.  
   https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-free-go-plus-pro

5. Anthropic. *Consumer Terms of Service.* Effective 2025-10-08; accessed 2026-09-07.  
   https://www.anthropic.com/legal/consumer-terms

---

## Series Navigation

**Paper 1**  
AI 訂閱制的制度錯位：當曆法時間不再等於智能消耗

**Paper 2**  
額度的時間可替代性：月算力、Burst 與集中式工作

**Paper 3**  
訂閱、API 與 Compute Wallet：AI 混合計價制度

**Paper 4 — 本篇**  
閒置額度、轉讓與供應商回購：AI 使用權的可逆性

**Paper 5 — Next**  
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
