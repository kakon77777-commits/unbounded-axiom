# Token 消耗症候群：到期額度如何反向塑造人的認知行為
## Token Consumption Syndrome: How Expiring AI Allowances Reshape User Cognition and Demand

**Series:** AI 算力經濟：從訂閱額度到自適應容量市場  
**Extra 1 / 2 — Series Paper 9 / 10**  
**Author:** Neo.K  
**Affiliation:** EveMissLab  
**Version:** v1.0  
**Date:** 2026-09-07

---

## 摘要

生成式 AI 訂閱制度正在創造一種具有明顯行為經濟特徵的新型消費情境：使用者先支付固定費用，之後在五小時、每週、每月或其他重置窗口內取得一組會到期、重置或失效的使用權。當這些額度接近重置時，部分高頻使用者可能產生一種熟悉的心理壓力：

> 「不用掉，好像很虧。」

本文將這種現象分析性地稱為 **Token Consumption Syndrome（Token 消耗症候群）**。此名稱不是醫學、精神醫學或臨床診斷，而是一個描述產品制度如何透過心理帳戶、預付消費、到期損失、使用權顯著化與 perceived marginal cost 改變使用者行為的概念工具。

行為經濟學長期指出，消費者並不總是依完全可替代的貨幣與理性邊際效用做決策。Mental Accounting 研究顯示，人們會將支出分入不同心理帳戶，並受帳戶結算週期影響。2026 年針對數位服務的研究更直接指出，較高的預付費用會形成較大的 mental-account deficit，進而促使消費者增加使用，以「把已付的錢用回來」。另一方面，大規模預付消費研究也發現，預付餘額存在大量 breakage，即相當比例的已付價值最終並未被消耗。AI 訂閱將這兩種力量同時放大：有些使用者根本用不完，另一些高峰使用者則會因額度可見、重置時間清楚與推理邊際成本近似零，而在重置前加速使用。

本文提出 Expiration Pressure、Artificial Demand、Consumption Acceleration、Quota Salience、Perceived Marginal Cost、Breakage Ratio 與 Reset-Induced Demand 等概念，並建立：

$$
\boxed{
\text{Prepayment}
+
\text{Expiring Entitlement}
+
\text{Quota Salience}
\rightarrow
\text{Consumption Pressure}
}
$$

的行為模型。

本文同時指出，這種現象對供應商並非純粹有利。額度失效可以產生 breakage、提高方案毛利並降低長期負債，但若大量使用者在重置前為了避免「浪費」而製造低價值 inference，供應商可能得到更多計算消耗，卻沒有得到相同比例的產品價值，甚至增加尖峰負載。這使「到期制度」同時具有：

$$
\text{revenue protection}
$$

與：

$$
\text{artificial demand creation}
$$

兩種相反效果。

本文因此提出 Rollover、Surrender、Off-Peak Conversion、Usage Forecast、Value-Based Nudging 與 Auto-Schedule 等替代設計，並主張 AI 產品不應以「讓使用者想辦法把額度燒完」作為留存或價值感的來源。成熟制度應追求：

$$
\boxed{
\text{task-driven AI consumption}
>
\text{expiration-driven AI consumption}
}
$$

亦即讓 AI 使用重新由真實任務價值驅動，而不是由重置時鐘驅動。

**關鍵詞：** Token 消耗症候群、Mental Accounting、Expiration Effect、Prepaid Consumption、Breakage、AI 訂閱、Quota Reset、Behavioral Economics、Artificial Demand、AI 使用行為

---

## 1. 一個玩笑為什麼值得正式研究

AI 高頻使用者之間很容易出現一種半開玩笑的語言：

> 額度要重置了。

> 還有很多沒用。

> 不用掉好像很虧。

> 趕快找個東西讓 AI 算。

這聽起來只是：

$$
\text{heavy-user joke}
$$

。

但如果把這種行為抽象化，就會發現它非常接近預付消費與心理帳戶研究長期觀察到的現象。

使用者先支付：

$$
P_{\mathrm{sub}}
$$

之後獲得：

$$
E_t
$$

的使用權。

若：

$$
E_t
$$

不能退款、不能轉讓、不能完整 rollover，

並在：

$$
T_{\mathrm{reset}}
$$

失效，

則：

$$
E_t
\rightarrow0
$$

。

這會改變使用者在重置前的決策。

---

## 2. 本文的「症候群」不是醫學診斷

本文使用：

$$
\boxed{
\text{Token Consumption Syndrome}
}
$$

只是分析性名稱。

它不代表：

- 精神疾病；
- 成癮診斷；
- 強迫症；
- 臨床症候群；
- 個體人格缺陷。

更準確地說，它描述：

$$
\boxed{
\text{a product-induced behavioral pattern}
}
$$

。

亦即：

> 某種產品權利設計，使本來不一定需要發生的消費變得更有心理吸引力。

---

## 3. AI 訂閱是一種特殊的預付消費

訂閱的基本結構為：

$$
\text{Pay First}
\rightarrow
\text{Consume Later}
$$

。

這和單次 API：

$$
\text{Consume}
\rightarrow
\text{Pay per Use}
$$

不同。

使用者在付款時已經承擔：

$$
P_{\mathrm{sub}}
$$

。

之後每多用一次，

心理上的即時邊際價格可能近似：

$$
PMC
\approx0
$$

其中 $PMC$ 是 Perceived Marginal Cost。

---

## 4. 但真正的邊際成本並不是零

對供應商而言：

$$
MC_{\mathrm{provider}}>0
$$

因為還有：

- GPU；
- CPU；
- memory；
- network；
- power；
- cooling；
- tool execution。

因此產生：

$$
\boxed{
PMC_{\mathrm{user}}
\neq
MC_{\mathrm{provider}}
}
$$

。

固定訂閱正是利用這個差異提供價格抽象。

---

## 5. 預付會創造 Mental Account

Thaler 的 Mental Accounting 理論指出，人們會將不同支出分入不同心理帳戶，而帳戶的分類與結算方式會改變消費決策。

可將 AI 訂閱心理帳戶表示為：

$$
A_{\mathrm{AI}}
=
P_{\mathrm{sub}}
-
V_{\mathrm{experienced}}
$$

。

付款後：

$$
P_{\mathrm{sub}}>0
$$

但尚未感受到足夠使用價值時，

使用者可能覺得：

$$
A_{\mathrm{AI}}>0
$$

仍然「沒有回本」。

---

## 6. Mental-Account Deficit

2026 年 Bhaskaran、Erat 與 Mukherjee 對數位服務的研究直接提出：

較高 upfront fee 會形成更大的 mental account deficit，

並促使使用者增加消費，

因為他們希望：

> get their money's worth。

可以簡化成：

$$
MAD
=
P_{\mathrm{prepaid}}
-
V_{\mathrm{consumed}}
$$

。

當：

$$
MAD\uparrow
$$

消費動機可能：

$$
M_{\mathrm{consume}}\uparrow
$$

。

這與 AI 訂閱的高頻使用者行為高度相容。

---

## 7. 「我已經付錢了」如何改變任務門檻

假設一次 AI 任務的真實價值為：

$$
V_i
$$

人類時間成本為：

$$
C_{H,i}
$$

若使用者按 API 付費，

還有：

$$
P_i
$$

。

因此只有：

$$
V_i
>
C_{H,i}
+
P_i
$$

才比較值得執行。

但固定訂閱下：

$$
P_i^{\mathrm{perceived}}
\approx0
$$

條件變成：

$$
V_i
>
C_{H,i}
$$

。

因此更多低價值任務會被執行。

---

## 8. 到期額度會再把門檻往下推

如果額度即將失效，

不使用會被心理上編碼成：

$$
L_{\mathrm{expire}}>0
$$

。

此時使用條件可能變成：

$$
V_i
+
L_{\mathrm{avoided\ expiration}}
>
C_{H,i}
$$

。

換句話說，

即使：

$$
V_i<C_{H,i}
$$

只要「不用掉很浪費」的感覺夠強，

任務仍可能被執行。

---

## 9. Expiration Pressure

本文定義 **Expiration Pressure**：

$$
EP_i(t)
=
\frac{
E_i^{\mathrm{remaining}}(t)
}{
\tau_i(t)+\epsilon
}
$$

其中：

- $E_i^{\mathrm{remaining}}$：剩餘 entitlement；
- $\tau_i(t)$：距離重置或失效剩餘時間；
- $\epsilon$：避免除以零的小量。

當：

$$
E_{\mathrm{remaining}}\uparrow
$$

且：

$$
\tau\downarrow
$$

則：

$$
EP\uparrow
$$

。

---

## 10. 這是一個「額度／時間」壓力比

例如：

使用者 A：

$$
E=10,\quad\tau=7\text{ days}
$$

。

使用者 B：

$$
E=80,\quad\tau=6\text{ hours}
$$

。

B 的：

$$
EP
$$

顯著更高。

因此「剩多少」與「多久後失效」必須一起看。

---

## 11. Quota Salience

若使用者根本不知道額度還剩多少，

Expiration Pressure 對行為的影響可能較弱。

但現代 AI 產品越來越提供：

- usage bar；
- remaining percentage；
- reset clock；
- countdown；
- weekly usage dashboard。

這提高：

$$
QS
=
\text{Quota Salience}
$$

。

---

## 12. Salience 會放大 Expiration Pressure

可以寫成：

$$
EP_i^*
=
EP_i
\cdot
QS_i
$$

其中：

$$
QS_i\in[0,1]
$$

。

若：

$$
QS_i\approx0
$$

使用者幾乎沒有注意額度。

若：

$$
QS_i\approx1
$$

剩餘量與倒數非常顯眼。

---

## 13. Claude 是非常清楚的現行例子

截至 2026 年 9 月，Claude Pro 與 Max 都使用：

$$
5\text{-hour session limit}
$$

以及：

$$
\text{weekly usage limit}
$$

。

官方 Usage Settings 會顯示：

- session usage progress；
- weekly usage progress；
- reset time。

因此使用者面對的是非常明確的：

$$
\boxed{
\text{quota state}
+
\text{reset clock}
}
$$

。

這種制度非常適合研究 quota salience 與使用節奏之間的關係。

---

## 14. OpenAI 也正在增加 Usage 可觀測性

截至 2026 年 9 月，OpenAI 個人方案已提供：

$$
\text{included usage}
+
\text{purchased credits}
$$

。

部分 Plus／Pro 用戶亦可購買 weekly reset，

立即恢復適用的五小時與每週使用量，

並重新啟動下一個週期。

此外，banked resets 會保存到使用或到期。

因此：

$$
\boxed{
\text{reset itself}
}
$$

甚至開始成為一種可購買或可保存的產品權利。

---

## 15. Reset 不再只是時間，它本身開始商品化

當使用者可以：

$$
\text{buy a reset}
$$

意味著：

$$
\boxed{
\text{quota state transition}
}
$$

本身具有價格。

原本：

$$
E_t
\rightarrow0
\rightarrow
E_{t+1}
$$

只是系統規則。

現在某些情境變成：

$$
P_{\mathrm{reset}}
\rightarrow
E_t'
$$

。

這是 AI 訂閱制度非常有意思的進一步商品化。

---

## 16. Purchased Credits 與 Included Entitlement 的心理差異

使用者可能對：

$$
Q_{\mathrm{included}}
$$

與：

$$
Q_{\mathrm{purchased}}
$$

採用不同心理帳戶。

對 included：

> 不用白不用。

對 purchased credits：

> 每用一次都是真金白銀。

因此可能：

$$
PMC_{\mathrm{included}}
<
PMC_{\mathrm{purchased}}
$$

即使底層計算成本相同。

---

## 17. 同一個模型因此可能被兩種心理價格消費

例如：

$$
J
$$

需要 20 CU。

若從方案內含額度扣：

$$
PMC_J\approx0
$$

。

若從額外購買 credits 扣：

$$
PMC_J>0
$$

。

因此使用者策略可能在跨過 quota boundary 的瞬間改變。

---

## 18. Quota Cliff

本文將這種不連續稱為：

$$
\boxed{
\text{Quota Cliff}
}
$$

。

當：

$$
Q_{\mathrm{included}}>0
$$

時，

大量使用。

當：

$$
Q_{\mathrm{included}}=0
$$

並轉為 PAYG，

使用量突然下降：

$$
D_{\mathrm{user}}\downarrow
$$

。

這是一種價格制度造成的非線性需求。

---

## 19. Expiration Cliff

另一個 cliff 出現在：

$$
\tau\rightarrow0
$$

。

若剩餘 entitlement 即將消失，

使用者可能加速：

$$
\frac{dQ_{\mathrm{consume}}}{dt}\uparrow
$$

。

本文稱之為：

$$
\boxed{
\text{Expiration Cliff}
}
$$

。

---

## 20. Consumption Acceleration Index

定義：

$$
CAI
=
\frac{
Q_{\mathrm{last\ window}}/T_{\mathrm{last\ window}}
}{
Q_{\mathrm{baseline}}/T_{\mathrm{baseline}}
}
$$

。

若：

$$
CAI>1
$$

代表接近重置時的消耗速率高於平常。

若：

$$
CAI\gg1
$$

可能存在明顯 expiration-driven acceleration。

---

## 21. Artificial Demand

真正重要的不是消耗增加，

而是其中有多少來自：

$$
\text{valuable task demand}
$$

多少來自：

$$
\text{expiration avoidance}
$$

。

定義：

$$
D_{\mathrm{observed}}
=
D_{\mathrm{task}}
+
D_{\mathrm{artificial}}
$$

。

其中：

$$
D_{\mathrm{artificial}}
$$

是若額度可完整保存時不會發生的需求。

---

## 22. Counterfactual Definition

更嚴格地定義：

$$
D_{\mathrm{artificial}}
=
D_{\mathrm{expire}}
-
D_{\mathrm{rollover}}
$$

其中：

- $D_{\mathrm{expire}}$：會失效制度下的使用；
- $D_{\mathrm{rollover}}$：完全可保留制度下的反事實使用。

這需要 A/B test 才能估計。

---

## 23. AI 特別容易放大 Artificial Demand

一般健身房會員想「把月費用回來」，

仍然需要：

$$
\text{physical effort}
$$

。

AI 不同。

多做一次推理的使用者成本可能非常低。

甚至 Agent 可以：

$$
\text{autonomously generate more work}
$$

。

因此：

$$
C_{\mathrm{human,marginal}}\downarrow
$$

時：

$$
D_{\mathrm{artificial}}\uparrow
$$

的潛力很大。

---

## 24. Agent 可以把「不用白不用」自動化

假設使用者設定：

> 如果本週還剩很多額度，就多跑幾輪驗證。

Agent 可以：

$$
N_{\mathrm{verify}}
=
f(
Q_{\mathrm{remaining}},
\tau
)
$$

。

當：

$$
Q_{\mathrm{remaining}}\uparrow
$$

且：

$$
\tau\downarrow
$$

自動增加：

$$
N_{\mathrm{verify}}\uparrow
$$

。

這將 Token 消耗症候群從心理現象轉成軟體策略。

---

## 25. 這不一定是「浪費」

額外驗證有時真的會提高品質。

例如：

$$
Q_{\mathrm{quality}}
\uparrow
$$

。

因此不能把所有 expiration-driven usage 都視為無價值。

需要區分：

$$
\boxed{
\text{opportunistic value creation}
}
$$

與：

$$
\boxed{
\text{pure burn}
}
$$

。

---

## 26. Opportunistic Consumption

如果額度快失效，

使用者可能想：

> 那就拿來做原本不值得付費，但仍有小價值的事情。

例如：

- 多跑一次 code review；
- 多做一組翻譯；
- 多生成幾個設計備選；
- 多驗證一個假說。

這些：

$$
V_i>0
$$

只是：

$$
V_i<P_{\mathrm{normal}}
$$

。

因此 expiration 也可能把低價值但正價值需求釋放出來。

---

## 27. 因此 Artificial 不等於 Worthless

更準確地說：

$$
D_{\mathrm{artificial}}
=
D_{\mathrm{positive\ low\ value}}
+
D_{\mathrm{near\ zero}}
+
D_{\mathrm{negative\ net}}
$$

。

企業真正應避免的是：

$$
D_{\mathrm{negative\ net}}
$$

即使用者與供應商整體淨價值皆低的消耗。

---

## 28. Token Burn

本文把近乎沒有任務價值、主要因為額度快失效而發生的推理稱為：

$$
\boxed{
\text{Token Burn}
}
$$

。

判定條件可近似：

$$
V_{\mathrm{task}}
<
C_{\mathrm{system}}
+
C_{\mathrm{human}}
$$

但仍被：

$$
L_{\mathrm{expiration}}
$$

推動執行。

---

## 29. 供應商為什麼可能喜歡 Breakage

預付市場常見：

$$
\boxed{
\text{Breakage}
}
$$

即使用者已支付但最終沒有兌現的價值。

2026 年一項涵蓋數百萬消費者的預付研究指出，約 40% 的預付價值最終沒有被使用。

這顯示：

$$
\text{prepaid revenue}
$$

與：

$$
\text{actual service cost}
$$

之間可以存在很大差距。

---

## 30. AI Subscription Breakage

本文定義：

$$
BR
=
\frac{
Q_{\mathrm{unused\ expired}}
}{
Q_{\mathrm{entitled}}
}
$$

為 Breakage Ratio。

若：

$$
BR\uparrow
$$

供應商實際服務成本可能下降。

因此 expiration 對供應商具有直接經濟價值。

---

## 31. 但 Breakage 太高也可能表示產品價值低

若大量使用者：

$$
Q_{\mathrm{unused}}\uparrow
$$

可能表示：

- 買太高方案；
- 沒有需求；
- 產品不好用；
- 額度設計不符合工作週期。

因此：

$$
BR
$$

不是越高越好。

---

## 32. Breakage 與 Token Burn 是兩種相反力量

一邊：

$$
\text{Unused}
\rightarrow
\text{Breakage}
$$

降低供應商成本。

另一邊：

$$
\text{Expiration Pressure}
\rightarrow
\text{Token Burn}
$$

增加供應商成本。

因此到期制度的淨效果是：

$$
\Pi_{\mathrm{expiration}}
=
V_{\mathrm{breakage}}
-
C_{\mathrm{burn}}
+
V_{\mathrm{retention}}
-
C_{\mathrm{dissatisfaction}}
$$

。

---

## 33. 供應商的最優 Expiration 不一定是零或無限

若完全不過期：

$$
\text{Rollover}\rightarrow\infty
$$

平台可能累積巨大：

$$
\text{latent compute liability}
$$

。

若很快過期：

$$
\tau_{\mathrm{expiry}}\downarrow
$$

則：

- frustration；
- burn；
- perceived unfairness；

可能上升。

因此存在：

$$
\tau^*
$$

使：

$$
\Pi(\tau)
$$

最大化。

---

## 34. 使用者的最優制度與供應商未必相同

使用者希望：

$$
F_T\uparrow
$$

即更多時間可替代性。

供應商可能希望：

$$
BR\uparrow
$$

以降低兌現成本。

因此：

$$
\boxed{
\text{expiration policy is a distributional choice}
}
$$

。

它決定 unused value 最終由誰承擔。

---

## 35. 到期其實是一種「隱性價格」

如果兩個方案都是：

$$
200\ \mathrm{USD/month}
$$

但 A：

$$
BR_A=10\%
$$

B：

$$
BR_B=50\%
$$

則使用者實際每單位有效使用成本不同。

可定義：

$$
P_{\mathrm{effective}}
=
\frac{
P_{\mathrm{sub}}
}{
Q_{\mathrm{used}}
}
$$

。

到期制度因此會改變實際價格。

---

## 36. Reset Frequency 也是定價參數

假設相同總額度：

方案 A：

$$
Q_{\mathrm{month}}
$$

一次給。

方案 B：

$$
Q_{\mathrm{week}}
$$

分四次且不能跨週。

即使：

$$
4Q_{\mathrm{week}}
=
Q_{\mathrm{month}}
$$

使用者可實際取得的價值也可能：

$$
V_A>V_B
$$

。

因此：

$$
\boxed{
\text{reset frequency is part of price}
}
$$

。

---

## 37. Choice Bracketing

Mental Accounting 研究指出，人們如何「框住」決策時間範圍會改變選擇。

若 AI 額度以：

$$
5\text{ h}
$$

框住，

使用者可能以五小時為思考週期。

若以：

$$
1\text{ month}
$$

框住，

則更可能進行長期配置。

因此產品實際在提供：

$$
\boxed{
\text{cognitive bracketing}
}
$$

。

---

## 38. 這正好回到 Paper 1 的四時鐘

Paper 1 提出：

$$
T_{\mathrm{billing}}
\neq
T_{\mathrm{entitlement}}
\neq
T_{\mathrm{compute}}
\neq
T_{\mathrm{work}}
$$

。

Token 消耗症候群正是：

$$
T_{\mathrm{entitlement}}
$$

反過來侵入：

$$
T_{\mathrm{work}}
$$

的結果。

---

## 39. Reset Clock 變成 Cognition Clock

理想情況：

$$
T_{\mathrm{work}}
=
f(
\text{task}
)
$$

。

但 quota-driven 狀況：

$$
T_{\mathrm{work}}
=
f(
\text{task},
T_{\mathrm{reset}}
)
$$

。

當：

$$
\frac{\partial T_{\mathrm{work}}}{\partial T_{\mathrm{reset}}}
$$

太大，

就表示產品制度正在強烈塑造工作節奏。

---

## 40. 高峰使用者特別敏感

Light user：

$$
Q_{\mathrm{used}}
\ll
Q_{\mathrm{limit}}
$$

通常不會注意 reset。

Heavy user：

$$
Q_{\mathrm{used}}
\approx
Q_{\mathrm{limit}}
$$

則會持續關注：

$$
Q_{\mathrm{remaining}}
$$

與：

$$
T_{\mathrm{reset}}
$$

。

因此 Token 消耗症候群更可能出現在：

$$
\boxed{
\text{high-engagement users}
}
$$

。

---

## 41. 這也可能出現在企業部門

企業年度預算常有：

> 不用完明年會被砍。

AI credits 也可能出現：

> 這個部門剩很多，趕快用。

形成：

$$
\boxed{
\text{organizational token burn}
}
$$

而不只是個人心理。

---

## 42. Departmental Artificial Demand

若部門知道：

$$
Q_{\mathrm{budget}}
$$

月底歸零，

可能啟動：

- 低優先級 evaluation；
- 重複 benchmark；
- 不必要批次生成；

以證明：

$$
Q_{\mathrm{budget}}
$$

確實有需要。

這與政府或企業的「use-it-or-lose-it budget」非常相似。

---

## 43. 產品設計可能不小心強化這個現象

例如：

> 你還剩 82%！

加上一個紅色倒數：

> 6 小時後歸零！

這會提高：

$$
QS\uparrow
$$

與：

$$
EP\uparrow
$$

。

即使產品只是想「透明」，

也可能產生：

$$
\text{consumption nudge}
$$

。

---

## 44. 透明度不是永遠中性的

Paper 6 主張 Capacity Transparency。

但對個人 quota：

$$
\boxed{
\text{transparency}
\rightarrow
\text{behavior}
}
$$

。

因此應區分：

- decision-useful transparency；
- consumption-pressure transparency。

---

## 45. 好的 Usage Dashboard 應該回答什麼

不只是：

> 剩多少？

還應該回答：

> 依你目前使用速度，是否真的需要擔心？

例如：

> 你本週還有 60%，依目前速度預計用不完。未使用額度可 rollover 30%。

這比單純倒數更能減少焦慮。

---

## 46. Usage Forecast

可以估計：

$$
\hat Q_{\mathrm{end}}
=
Q_{\mathrm{remaining}}
-
\hat D_{\mathrm{future}}
$$

。

若：

$$
\hat Q_{\mathrm{end}}>0
$$

系統可提供：

> 預計剩餘 120 CU。

再給：

- rollover；
- surrender；
- off-peak bonus。

使用者不需要自己想辦法燒掉。

---

## 47. Value-Based Nudge

平台甚至可以說：

> 你不需要為了用完額度額外執行任務。

這看似會降低 usage，

但可能提高：

$$
\text{trust}
$$

與：

$$
\text{long-term retention}
$$

。

---

## 48. 不把 Usage 當唯一 Engagement KPI

如果產品團隊只最大化：

$$
Q_{\mathrm{consumed}}
$$

就可能誤把 Token Burn 當成功。

更合理的是：

$$
\boxed{
\text{Useful Task Completion}
}
$$

。

---

## 49. Useful Compute Ratio

定義：

$$
UCR
=
\frac{
Q_{\mathrm{task\ valuable}}
}{
Q_{\mathrm{total}}
}
$$

。

理想制度希望：

$$
UCR\uparrow
$$

而不是只希望：

$$
Q_{\mathrm{total}}\uparrow
$$

。

---

## 50. Task-Driven Consumption Ratio

可再定義：

$$
TDR
=
\frac{
D_{\mathrm{task}}
}{
D_{\mathrm{observed}}
}
$$

。

若：

$$
TDR\approx1
$$

大部分使用都由真實需求驅動。

若：

$$
TDR\downarrow
$$

可能存在更多 quota-driven usage。

---

## 51. 如何估計 Artificial Demand

不能直接問：

> 你這次是不是在浪費 Token？

更好的實驗是：

### Group A

正常 expiration。

### Group B

允許 rollover。

### Group C

允許 surrender。

### Group D

完全不顯示 reset countdown。

比較：

$$
Q_{\mathrm{last\ window}}
$$

與：

$$
Q_{\mathrm{total}}
$$

。

---

## 52. 如果 Rollover 顯著降低重置前使用

則可以推論：

$$
D_{\mathrm{artificial}}>0
$$

。

若：

$$
Q_{\mathrm{rollover}}
\approx
Q_{\mathrm{expiration}}
$$

則 Token Burn 可能很低。

這是可直接驗證的產品假說。

---

## 53. Rollover 是最直接的治療機制

假設：

$$
Q_{\mathrm{unused}}
$$

可部分移至未來：

$$
Q_{t+1}
=
Q_{\mathrm{base}}
+
\alpha Q_{\mathrm{unused},t}
$$

。

則 expiration loss：

$$
L_{\mathrm{expire}}\downarrow
$$

進而：

$$
EP\downarrow
$$

。

---

## 54. 但完全 Rollover 會增加企業負債

如果：

$$
\alpha=1
$$

且：

$$
Q
$$

永不失效，

平台可能累積：

$$
LDL
=
\text{Latent Demand Liability}
$$

。

因此 rollover 可以：

- capped；
- time-limited；
- discounted。

---

## 55. Surrender 比 Rollover 更有企業價值

Paper 4 提出：

$$
E
\rightarrow
P
\rightarrow
R
$$

。

使用者不需要燒額度。

供應商也不需要把全部 unused entitlement 推到未來。

因此：

$$
\boxed{
\text{Surrender}
}
$$

可能同時降低：

$$
\text{Token Burn}
$$

與：

$$
\text{Latent Demand Liability}
$$

。

---

## 56. Off-Peak Conversion

使用者也可以：

$$
100\ \mathrm{Peak\ CU}
\rightarrow
140\ \mathrm{OffPeak\ CU}
$$

。

這會把：

> 不用掉很浪費。

轉成：

> 先保存價值，晚點在更適合時段用。

因此：

$$
D_{\mathrm{peak}}\downarrow
$$

。

---

## 57. Borrow 的反方向心理

Borrow 讓使用者：

$$
Q_t
>
Q_{\mathrm{base},t}
$$

。

但如果沒有清楚介面，

也可能產生：

> 下個月欠了額度。

形成：

$$
\text{Compute Debt Anxiety}
$$

。

因此所有跨期制度都需要心理帳戶設計。

---

## 58. Compute Wallet 可以降低碎片化心理

如果 Chat、Code、Research 的額度完全分開，

使用者可能看到：

> Research 還剩很多，Code 不夠。

形成：

$$
\text{category-specific burn}
$$

。

Compute Wallet 讓：

$$
Q_A+Q_B+Q_C
$$

部分共池，

可以降低：

$$
\text{mental account fragmentation}
$$

。

---

## 59. 但 Wallet 也可能讓成本太抽象

如果所有東西都只顯示：

> CU。

使用者可能不知道：

> 這個任務為什麼這麼貴？

因此需要：

$$
\boxed{
\text{Price Abstraction}
+
\text{Cost Explainability}
}
$$

。

---

## 60. 產品應顯示「價值替代」而不是「快燒完」

例如：

> 你還有 200 CU 即將於月底失效。

可以提供：

- rollover 100；
- surrender 80 換 50 future CU；
- 安排 3 個已排隊的低優先任務。

而不是：

> 快來多用！

---

## 61. Provider Incentive 也需要重新設計

若收入已經收取：

$$
P_{\mathrm{sub}}
$$

短期內供應商最便宜的使用者是：

$$
Q=0
$$

。

但長期若：

$$
Q=0
$$

使用者會退訂。

因此供應商要最大化：

$$
\boxed{
\text{perceived value}
}
$$

而不是：

$$
\text{minimum compute}
$$

或：

$$
\text{maximum compute}
$$

。

---

## 62. Optimal Consumption Zone

可能存在：

$$
Q^*
$$

使：

$$
\text{Retention}(Q)
-
\text{Cost}(Q)
$$

最大。

太低：

$$
\text{Retention}\downarrow
$$

。

太高：

$$
\text{Cost}\uparrow
$$

。

因此企業真正希望的是：

$$
\boxed{
\text{high-value efficient consumption}
}
$$

。

---

## 63. Expiration Policy 也是 Demand Engineering

Paper 5 將 Demand Engineering 定義為：

$$
\text{design when demand occurs}
$$

。

Expiration 其實也是一種 demand engineering。

只是它往往是：

$$
\boxed{
\text{unintentional demand engineering}
}
$$

。

---

## 64. 好制度與壞制度的差別

好的：

$$
\text{Off-Peak Discount}
\rightarrow
\text{move valuable demand}
$$

。

壞的：

$$
\text{Hard Expiration}
\rightarrow
\text{manufacture low-value demand}
$$

。

兩者都會改變：

$$
D(t)
$$

。

---

## 65. Reset Boundary 可能形成需求尖峰

若大量使用者具有同一 reset time：

$$
T_R
$$

並且存在 expiration acceleration，

則可能：

$$
D(T_R-\epsilon)\uparrow
$$

。

但現實中許多 AI 服務的 reset 時間可能依帳戶分散，因此 aggregate peak 是否明顯，需要實證測量。

本文不假定所有平台都必然出現全局 reset spike。

---

## 66. Staggered Reset 是一種容量工具

若供應商把：

$$
T_{R,i}
$$

分散，

則：

$$
\mathrm{Var}[
\sum_i D_i(t)
]
\downarrow
$$

可能成立。

因此 individualized reset 具有：

$$
\boxed{
\text{load smoothing}
}
$$

價值。

---

## 67. 但 Staggering 不解決個體 Expiration Pressure

即使：

$$
T_{R,A}\neq T_{R,B}
$$

每個使用者仍可能在自己的：

$$
T_{R,i}
$$

前加速。

因此：

$$
\text{aggregate smoothing}
$$

不等於：

$$
\text{behavioral distortion removal}
$$

。

---

## 68. Token 消耗症候群與 FOMO 不完全相同

FOMO：

$$
\text{fear of missing opportunity}
$$

。

Token Consumption：

$$
\text{fear of wasting prepaid entitlement}
$$

。

兩者都涉及 loss aversion，

但 reference point 不同。

---

## 69. Reference Point

使用者可能把：

$$
Q_{\mathrm{entitled}}
$$

心理上視為：

> 我已經擁有的東西。

因此失效：

$$
Q_{\mathrm{unused}}\rightarrow0
$$

被感知成：

$$
\text{loss}
$$

而不是：

$$
\text{non-consumption}
$$

。

這就是權利 framing 的重要性。

---

## 70. 契約上不是財產，心理上卻可能像財產

Paper 4 已指出：

$$
\text{entitlement}
\neq
\text{property}
$$

。

但在使用者心理上：

$$
E_i
$$

可以被編碼成：

$$
\boxed{
\text{mine}
}
$$

。

所以：

> 它要消失了。

會產生 loss aversion。

---

## 71. Endowment-Like Effect

一旦使用者看到：

> 你本週有 100%。

這個：

$$
100\%
$$

就可能形成 reference endowment。

消耗後：

> 還剩 30%。

如果剩餘 30% 直接歸零，

心理上可能像失去：

$$
30\%
$$

而不是單純沒有使用。

---

## 72. 這解釋了為什麼「明確顯示總額度」有雙面性

Paper 6 主張透明。

但本文提醒：

$$
\boxed{
\text{Quota Transparency}
}
$$

同時提高：

- planning ability；
- loss salience。

所以透明介面需要：

$$
\text{neutral framing}
$$

。

---

## 73. Neutral Framing

比較：

> 還有 70% 沒用！3 小時後失效！

與：

> 本週使用 30%。下一週將自動重置。可 rollover 20%。

後者比較不像：

$$
\text{urgent consumption nudge}
$$

。

---

## 74. 不要用 Gamification 鼓勵燃燒

例如：

> 恭喜你用了 100% 額度！

可能讓：

$$
Q=100\%
$$

變成遊戲目標。

除非：

$$
100\%
$$

真的代表高價值工作完成，

否則這種 KPI 可能錯誤。

---

## 75. Better Progress Metric

可以顯示：

$$
\text{Tasks Completed}
$$

$$
\text{Projects Advanced}
$$

$$
\text{Useful Agent Jobs}
$$

而不是只顯示：

$$
\text{Tokens Consumed}
$$

。

---

## 76. 從 Consumption Metric 到 Outcome Metric

真正理想：

$$
\boxed{
\text{engagement}
\rightarrow
\text{outcome}
}
$$

。

例如：

> 本月完成 12 個程式任務。

比：

> 本月用了 95% 額度。

更符合 AI 生產力產品。

---

## 77. 用戶有權選擇「不工作」

如果使用者今天：

> 想休息、玩遊戲、度假。

AI 產品不應透過：

$$
\text{expiring quota}
$$

製造：

> 我是不是該趕快找工作做？

這不是道德問題。

而是產品是否把：

$$
\text{subscription clock}
$$

不必要地變成：

$$
\text{behavioral obligation}
$$

。

---

## 78. Permission to Idle

成熟產品可以默認：

$$
\boxed{
\text{idle is a valid user state}
}
$$

。

「今天不用 AI」不應自動被產品設計成損失。

---

## 79. 這與 AI 的生產力悖論有關

AI 原本應該：

$$
T_{\mathrm{work}}\downarrow
$$

。

但如果節省下來的時間又因：

> 額度還沒用完。

被填回更多低價值工作，

可能形成：

$$
\boxed{
\text{productivity rebound}
}
$$

。

---

## 80. AI 可以讓工作更快，也可以讓人永遠有更多工作可做

因為任務空間：

$$
\mathcal T
$$

幾乎無限。

如果：

$$
C_{\mathrm{marginal}}\downarrow
$$

人會發現：

> 還可以再驗證一次。

> 還可以再改一版。

> 還可以再研究一題。

因此 AI 的：

$$
\boxed{
\text{latent task demand}
}
$$

可能非常巨大。

---

## 81. Expiring Quota 會激活 Latent Task Demand

令：

$$
\mathcal T_{\mathrm{latent}}
=
\{
J_i:
V_i>0,\text{ but normally not executed}
\}
$$

。

當：

$$
EP\uparrow
$$

更多：

$$
J_i
$$

跨過執行門檻。

這解釋高頻使用者為什麼永遠「找得到東西算」。

---

## 82. 這可能造成認知過度擴張

人類真正稀缺的不只 GPU。

還有：

$$
\boxed{
\text{attention}
+
\text{verification capacity}
+
\text{rest}
}
$$

。

如果 AI 生成：

$$
N_{\mathrm{outputs}}\uparrow
$$

但人類驗證能力：

$$
H_{\mathrm{verify}}
$$

固定，

可能：

$$
\frac{
N_{\mathrm{outputs}}
}{
H_{\mathrm{verify}}
}
\uparrow
$$

。

---

## 83. Token Burn 可能轉化成人類 Review Debt

例如為了用完額度生成：

$$
100
$$

份分析。

之後還需要人類：

$$
R_{\mathrm{human}}
$$

驗證。

於是：

$$
\boxed{
\text{Compute Surplus}
\rightarrow
\text{Human Review Debt}
}
$$

。

這甚至可能降低總生產力。

---

## 84. 所以 Useful Compute 需要人機共同衡量

不是：

$$
Q_{\mathrm{AI}}
$$

越大越好。

而是：

$$
\boxed{
\eta
=
\frac{
V_{\mathrm{completed}}
}{
Q_{\mathrm{AI}}
+
H_{\mathrm{human}}
}
}
$$

。

Expiration-driven consumption 可能讓 denominator 上升，

但 numerator 幾乎不變。

---

## 85. 可測試假說

### H1：接近 reset 時，部分高頻使用者的 Consumption Acceleration 會上升

$$
\tau\downarrow
\Rightarrow
CAI\uparrow
$$

。

### H2：顯示剩餘額度與明確倒數會提高 quota salience

$$
QS_{\mathrm{visible}}
>
QS_{\mathrm{hidden}}
$$

。

### H3：Rollover 會降低 reset 前使用加速

$$
\alpha_{\mathrm{rollover}}\uparrow
\Rightarrow
CAI\downarrow
$$

。

### H4：Surrender 會降低 Token Burn 且不必增加 latent liability

比純 rollover 更可能同時改善供需。

### H5：Purchased Credits 的使用彈性低於 Included Usage

因：

$$
PMC_{\mathrm{purchased}}
>
PMC_{\mathrm{included}}
$$

。

### H6：Agentic workload 比手動聊天更容易把 expiration-driven usage 自動放大

因：

$$
C_{\mathrm{human,marginal}}
$$

更低。

### H7：過高 breakage 會降低續訂

當使用者長期：

$$
BR_i\uparrow
$$

可能認為方案不值得。

---

## 86. 實驗設計

可以進行六組 A/B test。

### Group A：Hard Expiry + Visible Countdown

傳統高 salience。

### Group B：Hard Expiry + Neutral UI

不強調剩餘。

### Group C：30% Rollover

$$
\alpha=0.3
$$

。

### Group D：Surrender

提供 future CU。

### Group E：Off-Peak Conversion

剩餘額度轉成低峰額度。

### Group F：Outcome-Oriented Dashboard

顯示任務成果而不是 quota completion。

---

## 87. 需要測量的指標

包括：

$$
CAI
$$

$$
BR
$$

$$
UCR
$$

$$
TDR
$$

$$
\text{Retention}
$$

$$
\text{Peak Demand}
$$

$$
\text{Review Debt}
$$

$$
\text{User Satisfaction}
$$

。

只有這樣才能知道：

> 更多使用到底是不是更好的產品。

---

## 88. 供應商的最佳制度可能是混合式

例如：

$$
30\%
$$

可 rollover，

$$
20\%
$$

可 surrender，

其餘：

$$
50\%
$$

照常到期。

這讓：

$$
BR
$$

仍然存在，

又降低極端 expiration pressure。

---

## 89. 用戶也可以自己選方案

例如：

### Stable Plan

較高月費：

$$
F_T\uparrow
$$

更多 rollover。

### Discount Plan

較低月費：

$$
F_T\downarrow
$$

額度較容易過期。

讓：

$$
\text{expiration risk}
$$

本身成為可選價格維度。

---

## 90. Expiration Risk Pricing

如果使用者願意承擔：

$$
R_{\mathrm{expiry}}
$$

可以取得：

$$
P_{\mathrm{discount}}
$$

。

這比把 expiration 隱藏在方案條款裡更透明。

---

## 91. 高透明度不代表高壓迫

關鍵是：

$$
\boxed{
\text{Transparency}
+
\text{Choice}
}
$$

。

例如：

> 你的額度將失效。

旁邊同時提供：

- rollover；
- surrender；
- convert。

使用者就不需要 burn。

---

## 92. Token Consumption Syndrome 的完整模型

可表示為：

$$
TCS_i
=
f(
P_i,
E_i,
\tau_i,
QS_i,
PMC_i,
F_i,
A_i
)
$$

其中：

- $P_i$：預付成本；
- $E_i$：剩餘 entitlement；
- $\tau_i$：距離失效時間；
- $QS_i$：quota salience；
- $PMC_i$：perceived marginal cost；
- $F_i$：fungibility；
- $A_i$：automation capacity。

---

## 93. 預期方向

一般而言：

$$
\frac{\partial TCS}{\partial P}>0
$$

$$
\frac{\partial TCS}{\partial E}>0
$$

$$
\frac{\partial TCS}{\partial QS}>0
$$

$$
\frac{\partial TCS}{\partial A}>0
$$

。

而：

$$
\frac{\partial TCS}{\partial \tau}<0
$$

在接近到期時表示壓力增加。

---

## 94. Fungibility 會降低症候群

若：

$$
F_i\uparrow
$$

例如：

- rollover；
- transfer；
- surrender；
- conversion；

則未使用價值不會立刻歸零。

因此預期：

$$
\frac{\partial TCS}{\partial F}<0
$$

。

這將本篇直接接回整個系列。

---

## 95. 這不是使用者「不理性」這麼簡單

如果制度明確說：

> 你已經付了錢。

> 不用就消失。

那麼增加使用某種程度上是合理反應。

因此：

$$
\boxed{
\text{behavioral bias}
+
\text{rational response to contract}
}
$$

會混在一起。

---

## 96. 不能把所有責任丟給使用者

平台不能一方面：

$$
\text{make entitlement expire}
$$

另一方面又說：

> 使用者為什麼一直想用完？

行為部分正是制度內生產物。

---

## 97. 也不能把所有責任丟給企業

到期具有：

- capacity planning；
- anti-hoarding；
- revenue predictability；
- liability reduction；

等合理功能。

因此：

$$
\boxed{
\text{expiration is not inherently bad}
}
$$

。

問題是：

> 到期的成本是否過度由使用者承擔？

---

## 98. 成熟制度的目標不是消除所有到期

而是：

$$
\boxed{
\text{minimize low-value expiration-driven consumption}
}
$$

同時維持：

$$
\text{manageable provider liability}
$$

。

這是一個市場設計問題。

---

## 99. 從 Token Burn 回到 Adaptive AI Compute Economy

整個系列提出：

$$
\text{Temporal Fungibility}
$$

$$
\text{Compute Wallet}
$$

$$
\text{Surrender}
$$

$$
\text{Demand Engineering}
$$

。

這些機制都可以被重新理解為：

$$
\boxed{
\text{anti-burn mechanisms}
}
$$

。

---

## 100. 更好的制度把「不用」變成一個合法選項

現在：

$$
\text{Use}
\quad\text{or}\quad
\text{Lose}
$$

。

更成熟：

$$
\boxed{
\text{Use}
,\quad
\text{Save}
,\quad
\text{Convert}
,\quad
\text{Return}
}
$$

。

只要這四個選項存在，

使用者不需要製造任務。

---

## 101. AI 產品應該容許休息

如果 AI 真正是：

$$
\text{productivity tool}
$$

那麼它的成功不應該要求：

$$
\text{continuous consumption}
$$

。

真正成功可能是：

> 五天完成工作。

> 接著二十五天不用。

---

## 102. 這反而是生產力提高的證據

如果同樣成果：

$$
W
$$

原本需要：

$$
30\text{ days}
$$

現在：

$$
5\text{ days}
$$

則：

$$
\eta_{\mathrm{productivity}}\uparrow
$$

。

產品不應因為剩下 25 天低使用，就把使用者視為 engagement 下降。

---

## 103. 從 Engagement Economy 轉向 Completion Economy

社群平台希望：

$$
T_{\mathrm{screen}}\uparrow
$$

。

AI 生產力產品若照抄：

$$
T_{\mathrm{AI}}\uparrow
$$

可能方向錯誤。

更合理：

$$
\boxed{
\text{Task Completion}
+
\text{User Value}
}
$$

。

---

## 104. 這是 AI 產品經濟的一個重要分水嶺

如果 AI 企業仍然用：

$$
\text{time spent}
$$

或：

$$
\text{tokens consumed}
$$

作為唯一成功指標，

就可能：

$$
\boxed{
\text{optimize consumption instead of intelligence value}
}
$$

。

---

## 105. 基本原則

本文提出十五項原則。

### 原則一：Token 消耗症候群不是臨床診斷

它是制度誘發的行為分析概念。

### 原則二：預付與到期共同創造使用壓力

$$
\text{Prepayment}
+
\text{Expiration}
\rightarrow
\text{Consumption Pressure}
$$

### 原則三：剩餘額度與剩餘時間必須一起研究

$$
EP
=
f(E,\tau)
$$

### 原則四：Quota Salience 會改變行為

透明介面不是中性。

### 原則五：Included 與 Purchased Usage 具有不同心理價格

$$
PMC_{\mathrm{included}}
<
PMC_{\mathrm{purchased}}
$$

可能成立。

### 原則六：Artificial Demand 不等於全部無價值

需要區分 opportunistic value 與 pure burn。

### 原則七：Breakage 與 Burn 是到期制度的兩個反方向結果

### 原則八：Reset Frequency 本身就是價格與權利設計

### 原則九：Rollover 可以降低 Expiration Pressure

### 原則十：Surrender 可以同時降低 Burn 與 Latent Liability

### 原則十一：Usage Dashboard 應避免鼓勵 quota completion

### 原則十二：Agent 會放大 expiration-driven behavior

### 原則十三：企業應追蹤 Useful Compute，而非只有 Total Compute

### 原則十四：AI 生產力產品應允許低使用甚至完全不用

### 原則十五：產品目標應從 Consumption 走向 Completion

---

## 106. 限制

第一，本文的「Token Consumption Syndrome」是新提出的分析框架，不是現有臨床或心理學標準術語。

第二，目前尚缺乏大規模公開資料直接測量 AI 使用者在 reset 前是否普遍增加 consumption。

第三，不同平台 reset 時間可能錯開，因此個體級加速不必然形成整體系統峰值。

第四，額外使用可能提高品質，因此不能只以更多 inference 判定為浪費。

第五，使用者對額度的主觀價值高度異質。

第六，企業有合理的 anti-hoarding 與容量管理需求，因此本文不主張所有額度永久不失效。

---

## 107. 結論

「Token 消耗症候群」最初可以只是一句玩笑：

> 額度要重置了，不用好像很虧。

但這句話背後其實連接到非常成熟的行為經濟學問題：

$$
\text{Mental Accounting}
$$

$$
\text{Prepayment}
$$

$$
\text{Sunk Cost}
$$

$$
\text{Breakage}
$$

$$
\text{Choice Bracketing}
$$

以及：

$$
\text{Expiration Pressure}
$$

。

AI 把這些問題放大，是因為 inference 的使用邊際摩擦極低，而可以執行的潛在任務幾乎沒有上限。

因此：

$$
\text{unused quota}
$$

不只是：

> 沒有使用。

它可能被心理編碼成：

$$
\text{value about to be lost}
$$

。

一旦：

$$
E_{\mathrm{remaining}}\uparrow
$$

且：

$$
\tau_{\mathrm{reset}}\downarrow
$$

使用者就可能從：

$$
\text{I have a task, so I use AI}
$$

轉變為：

$$
\boxed{
\text{I have AI allowance, so I search for a task.}
}
$$

這就是本文真正要捕捉的反轉。

它將：

$$
\text{Task}
\rightarrow
\text{Compute}
$$

改成：

$$
\text{Compute Entitlement}
\rightarrow
\text{Task Creation}
$$

。

這種反轉不是必然有害。

它有時可以釋放低成本創造、額外驗證與探索。

但當：

$$
V_{\mathrm{task}}
$$

低於：

$$
C_{\mathrm{human}}
+
C_{\mathrm{system}}
$$

它就變成：

$$
\boxed{
\text{Token Burn}
}
$$

。

因此成熟 AI 產品真正應追求的，不是：

$$
\text{100\% quota consumption}
$$

而是：

$$
\boxed{
\text{high-value task completion}
}
$$

。

Rollover、Compute Wallet、Surrender、Off-Peak Conversion 與 Temporal Fungibility 的價值，也因此不只是「讓使用者比較爽」。

它們還在做另一件事：

$$
\boxed{
\text{restore task-driven consumption}
}
$$

。

也就是讓使用者重新因為：

> 我真的需要完成這件事。

才使用 AI，

而不是因為：

> 星期天晚上額度又要歸零了。

這使本篇最終命題可以寫成：

$$
\boxed{
\text{An AI subscription should create permission to compute, not an obligation to consume.}
}
$$

中文即：

**AI 訂閱應該提供「可以使用智能」的權利，而不應逐漸變成「必須把智能額度消耗完」的義務。**

下一篇，也是整個系列最後一篇，將把我們一路大量使用的研究方法本身正式化：

**跨產業制度移植——AI 產業其實不用每件事重新發明。**

---

## 參考資料

1. Bhaskaran, S., Erat, S., & Mukherjee, R. *Pay more, use more: Consumer bias and demand management for digital services.* Journal of Service Research, 2026.
2. Thaler, R. H. *Mental Accounting and Consumer Choice.* Marketing Science, 4(3), 199–214, 1985. DOI: 10.1287/mksc.4.3.199.
3. Thaler, R. H. *Mental Accounting Matters.* Journal of Behavioral Decision Making, 12(3), 183–206, 1999.
4. Soman, D. *The mental accounting of sunk time costs: why time is not like money.* Journal of Behavioral Decision Making, 14(3), 169–185, 2001. DOI: 10.1002/bdm.370.
5. Liu, Y., Zhang, H., & Zou, E. *Pay Now, Buy Never: The Economics of Consumer Prepayment Schemes.* NBER Working Paper No. 34918, 2026.
6. OpenAI Help Center. *Using Credits for Flexible Usage in ChatGPT (Personal plans).* Accessed 2026-09-07.
7. OpenAI Help Center. *Paid weekly Work and Codex rate limit resets.* Accessed 2026-09-07.
8. OpenAI Help Center. *How banked Codex resets work.* Accessed 2026-09-07.
9. Anthropic Help Center. *How do usage and length limits work?* Published 2026-07-13; accessed 2026-09-07.
10. Anthropic Help Center. *What is the Max plan?* Accessed 2026-09-07.
11. Anthropic Help Center. *Usage limit best practices.* Accessed 2026-09-07.

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

**Paper 8**  
AI 市場的制度演化：從商品化到容量市場

**Extra 1 — 本篇 / Series Paper 9**  
Token 消耗症候群：到期額度如何反向塑造人的認知行為

**Extra 2 — Next / Series Paper 10**  
跨產業制度移植：AI 產業其實不用每件事重新發明
