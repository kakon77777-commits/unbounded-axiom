# AI 與莊家制賭場：可計算、可預測、可利用與制度限制

## AI and House-Banked Casino Games: Computability, Predictability, Exploitability, and Institutional Constraints

**Series:** AI Game Intelligence, Randomness, and Adaptive Markets  
**Paper 05**  
**Version:** v0.1  
**Date:** 2026-09-02
**Author:** Neo.K with Aletheia（GPT-5.6 Sol）  
**Institution:** EveMissLab／一言諾科技有限公司

---

## 摘要

當人工智慧被引入傳統賭場問題時，最常見的誤解是把「能算得更精確」直接等同於「能提高對莊家的長期期望值」。

然而，輪盤、老虎機、百家樂與 Blackjack 並不是同一種類型的隨機系統。某些遊戲的下一次結果在合理模型下近似獨立；某些遊戲由物理系統生成但實務上不可取得足夠狀態；某些牌靴遊戲則因有限牌組且不放回抽取而具有真實狀態依賴。更進一步，即使某種資訊在數學上可以提高決策品質，賭場規則與司法管轄區仍可能禁止玩家使用電子、電腦或軟體裝置在遊戲進行中取得優勢。

因此本文提出四層區分：

$$
\boxed{
\text{Computable}
\neq
\text{Predictable}
\neq
\text{Exploitable}
\neq
\text{Permitted}.
}
$$

本文進一步把 AI 對合法、正常運作且無作弊的莊家制賭場可能造成的影響分成四類：

$$
E_{\mathrm{AI}}
=
E_{\mathrm{education}}
+
E_{\mathrm{selection}}
+
E_{\mathrm{policy}}
+
E_{\mathrm{state}},
$$

其中：

$$
E_{\mathrm{education}}
$$

代表把缺乏數學知識的玩家提升到較接近正確玩法；

$$
E_{\mathrm{selection}}
$$

代表辨識不同規則、賠表與 house edge；

$$
E_{\mathrm{policy}}
$$

代表在允許的決策空間內採取較佳策略；

而：

$$
E_{\mathrm{state}}
$$

則代表利用遊戲內部仍保留的狀態資訊。

對真正近似 IID、固定負期望值的遊戲，本文提出「歷史適應下注不變性」：若每一單位下注在給定過去資訊後仍具有固定負條件期望，則任何只根據歷史輸贏改變下注額的 AI，都不能把總期望值變成正數。

相反地，Blackjack 類有限牌靴遊戲說明：

$$
P(Y_{t+1}\mid S_t)
\neq
P(Y_{t+1}),
$$

因此狀態資訊確實可能具有數學價值。但這正是現代賭場制度會以洗牌、牌靴管理、桌規與電子輔助限制加以處理的區域。Nevada 現行 NRS 465.075 明確禁止使用設計來取得遊戲優勢的電腦、電子、軟體或硬體，包括預測結果、追蹤牌、分析事件概率或分析遊戲與投注策略。

因此，本篇的核心結論是：在合法、公平且受監管的莊家制賭場中，AI 最穩定的作用通常不是「創造正期望」，而是減少玩家自己的策略錯誤、比較制度條件、理解風險，以及驗證遊戲生成機制是否符合宣稱規則。

---

# 1. 從共同彩池重新回到莊家制市場

Paper 03 的共同彩池具有：

$$
O=F(q_1,\ldots,q_n),
$$

價格由所有投注者共同形成。

莊家制 casino game 則更接近：

$$
\boxed{
\text{Operator defines rules}
\rightarrow
\text{probability/payoff structure}
\rightarrow
\text{player chooses within that structure}.
}
$$

在大量傳統遊戲中，玩家的資金不會像 pari-mutuel 那樣直接重新生成其他玩家的最終派彩。

因此這一次的核心不是：

$$
\text{Can AI predict the market?}
$$

而是：

$$
\boxed{
\text{Can AI change the expectation already encoded in the game rules?}
}
$$

---

# 2. 四道不同的門

本文首先建立四個 Gate。

## Gate 1 — Computability

能否精確或近似計算：

$$
P(Y),
$$

$$
EV,
$$

$$
Var(Y).
$$

---

## Gate 2 — Predictability

給定目前可觀測狀態：

$$
X_t,
$$

是否存在：

$$
I(X_t;Y_{t+1})>0.
$$

---

## Gate 3 — Exploitability

即使可以改善預測或策略，是否存在：

$$
EV_{\mathrm{player}}>0.
$$

---

## Gate 4 — Permission

即使數學上存在可利用結構：

$$
EV_{\mathrm{state}}>0,
$$

玩家是否被遊戲規則與所在地法律允許使用取得該資訊的方法。

因此：

$$
\boxed{
\text{technical capability}
\not\Rightarrow
\text{legal or contractual permission}.
}
$$

---

# 3. House Edge

設一個單位投注的玩家淨收益為隨機變量：

$$
R.
$$

則玩家期望值：

$$
EV_P=E[R].
$$

若：

$$
EV_P<0,
$$

可以定義簡化 house edge：

$$
h=-EV_P.
$$

對每投注一單位而言：

$$
E[R]=-h.
$$

只要規則與策略不變，長期投注總量：

$$
W
$$

的期望損失近似：

$$
E[L]\approx hW.
$$

---

# 4. 勝率不是 House Edge

這是 AI 博彩討論最常見的錯誤之一。

假設策略：

$$
P(\text{win})=0.90,
$$

但九次各贏：

$$
1
$$

單位，一次輸：

$$
20
$$

單位。

則：

$$
EV
=
0.9(1)+0.1(-20)
=
-1.1.
$$

所以：

$$
\boxed{
P(\text{win})\uparrow
\not\Rightarrow
EV\uparrow.
}
$$

因此本文不使用「AI 提高勝率」作為唯一衡量標準。

---

# 5. AI 對新手仍然可能有價值

若玩家原本策略：

$$
\pi_H
$$

大量偏離數學上較佳策略：

$$
\pi^*,
$$

則 AI 教學可能使：

$$
EV(\pi_H)
<
EV(\pi_{AI})
\leq
EV(\pi^*).
$$

因此：

$$
\boxed{
\text{AI can improve the player}
}
$$

與：

$$
\boxed{
\text{AI can beat the house}
}
$$

是完全不同的命題。

前者在很多遊戲成立。

後者則困難得多。

---

# 6. AI Improvement Gap

本文定義：

$$
G_I
=
EV(\pi_{AI})-EV(\pi_{human}).
$$

以及：

$$
G_H
=
EV(\pi_{AI})-0.
$$

可能出現：

$$
G_I>0,
$$

但：

$$
G_H<0.
$$

意思是：

> AI 確實讓玩家少輸，但仍然沒有使遊戲成為正期望。

這可能是傳統合法賭場中最常見的 AI 效果。

---

# 7. 輪盤：高度可計算，但下一轉未必可預測

以歐式單零輪盤為例。

紅色有：

$$
18
$$

格，

非紅色有：

$$
19
$$

格。

下注紅色一單位：

$$
EV
=
\frac{18}{37}(1)
+
\frac{19}{37}(-1)
=
-\frac{1}{37}.
$$

因此：

$$
h
=
\frac{1}{37}
\approx
2.70\%.
$$

這個數值可以被精確計算。

但：

$$
\boxed{
\text{knowing }EV
\neq
\text{knowing the next spin}.
}
$$

---

# 8. 美式雙零輪盤

若有：

$$
38
$$

個格子，含：

$$
0
$$

與：

$$
00,
$$

則等額紅黑下注的簡化 house edge：

$$
h=
\frac{2}{38}
\approx5.26\%.
$$

因此 AI 很容易告訴玩家：

$$
2.70\%<5.26\%.
$$

這是一個：

$$
\boxed{
\text{game-selection advantage}
}
$$

但不是：

$$
\boxed{
\text{outcome-prediction advantage}.
}
$$

---

# 9. 選比較好的規則不是打敗賭場

如果 AI 從：

$$
h_1=5.26\%
$$

的遊戲改選：

$$
h_2=2.70\%,
$$

則：

$$
\Delta h=-2.56\%.
$$

這可以大幅改善玩家長期期望。

但仍然：

$$
h_2>0.
$$

因此：

$$
EV_P<0.
$$

AI 所做的是：

$$
\boxed{
\text{loss minimization}
}
$$

而不是：

$$
\boxed{
\text{positive-edge creation}.
}
$$

---

# 10. 歷史輸贏不能自動改變下一轉

若理想輪盤滿足：

$$
Y_{t+1}\perp H_t,
$$

則：

$$
P(Y_{t+1}\mid H_t)
=
P(Y_{t+1}).
$$

因此：

- 連續十次紅；
- 連續十次黑；
- 最近黑色偏多；
- 某個號碼很久沒出；

都不會自動改變下一轉的理論概率。

Paper 01 的 Randomness Boundary 在這裡直接成立。

---

# 11. AI 下注系統不能從歷史輸贏創造資訊

設 AI 在第 $t$ 局以前觀察：

$$
H_{t-1}.
$$

它依據歷史選擇投注額：

$$
b_t=b(H_{t-1}).
$$

若每一單位投注的條件期望始終：

$$
E[R_t\mid H_{t-1}]
=
-hb_t,
$$

其中：

$$
h>0,
$$

則由全期望法則：

$$
E[R_t]
=
E[E[R_t\mid H_{t-1}]]
=
-hE[b_t].
$$

對 $n$ 局：

$$
E\left[
\sum_{t=1}^{n}R_t
\right]
=
-hE\left[
\sum_{t=1}^{n}b_t
\right].
$$

因此：

$$
\boxed{
E[R_{\mathrm{total}}]<0
}
$$

只要總投注額為正。

---

# 12. 歷史適應下注不變性

本文稱上述結果為：

$$
\boxed{
\text{History-Adaptive Betting Invariance}.
}
$$

它表示：

在固定負條件期望的遊戲中，只根據過去輸贏改變下注額：

- Martingale；
- Fibonacci；
- loss chasing；
- reinforcement-learning sizing；
- LLM 自動調注；

都不能僅靠下注序列本身改變負期望的符號。

---

# 13. AI 可以改變 Variance

雖然：

$$
EV
$$

不一定改變，

下注策略可以改變：

$$
Var(R),
$$

$$
P(\text{short-term profit}),
$$

$$
P(\text{ruin}),
$$

以及資金路徑。

因此：

$$
\boxed{
\text{bet sizing can change risk geometry without changing underlying edge}.
}
$$

這正是「短期更常贏」與「長期期望為正」不能混在一起的原因。

---

# 14. 物理輪盤比抽象輪盤複雜

真正輪盤是經典力學系統。

可抽象為：

$$
Y
=
F(
v_{\mathrm{ball}},
\omega_{\mathrm{wheel}},
\theta_0,
\mu,
g,
\epsilon
).
$$

因此它不是本體論上必然 IID 的數學神諭。

若能完整知道初始狀態：

$$
S_0,
$$

原則上：

$$
Y=F(S_0)
$$

可以具有物理結構。

---

# 15. Physical Structure 不等於 Practical Exploitability

現實需要：

$$
\text{sufficient measurement precision}
+
\text{sufficient computation time}
+
\text{stable dynamics}
+
\text{permitted sensing}.
$$

因此：

$$
\boxed{
\text{physically deterministic}
\not\Rightarrow
\text{practically exploitable}.
}
$$

而在受監管賭場中，玩家使用外部電子設備取得這類即時優勢還可能另受法律或場規限制。

---

# 16. RNG 遊戲：制度目標本來就是讓預測失效

截至 2026 年，英國 Gambling Commission 的 Remote Gambling and Software Technical Standards 要求隨機結果達到「acceptably random」。

其 RTS 7 要求 RNG 輸出應符合預期分布，並具有不可預測性；對軟體 RNG，標準明確指出，在不知道完整演算法與 seed 的情況下，下一個數字應達到計算上不可行預測。

同一標準亦禁止 adaptive behaviour，也就是遊戲在進行中根據玩家過去結果改變結果概率。

因此對合規系統：

$$
\boxed{
\text{AI failing to predict the RNG}
}
$$

可能正是：

$$
\boxed{
\text{the regulated system working as intended}.
}
$$

---

# 17. GLI 對 Gaming Device RNG 的要求

Gaming Laboratories International 的 GLI-11 標準亦要求 RNG 最終輸出進行獨立性等統計測試，並要求可用結果具有適當概率，不應因先前產生的結果而改變，除非遊戲設計本身另有規定。

GLI-11 同時把 unpredictability 列為 RNG 設計要求之一。

因此：

$$
\boxed{
\text{regulated gaming RNG}
}
$$

本身就是反歷史預測設計。

---

# 18. 老虎機的 AI 誤解

假設某合規遊戲理論 RTP 為：

$$
RTP=96\%.
$$

長期期望 house edge 大致：

$$
h=1-RTP=4\%.
$$

但：

$$
RTP=96\%
$$

不代表玩家每：

$$
100
$$

元一定拿回：

$$
96
$$

元。

它描述的是大量遊戲下的理論平均結構。

---

# 19. RTP 不告訴你下一次 Spin

如果每次有效 RNG state 對玩家而言不可預測，則：

$$
P(Y_{t+1}\mid H_t)
\approx
P(Y_{t+1}).
$$

所以：

> 這台機器已經很久沒出大獎；

> 它剛剛連吃很多，所以快吐了；

不能僅從歷史結果推出。

---

# 20. AI 在 Slots 中最合理的角色

在不進入漏洞利用的前提下，AI 可以幫助理解：

- RTP；
- volatility；
- paytable；
- bonus rules；
- wager requirements；
- jackpot structure。

因此：

$$
E_{\mathrm{selection}}>0
$$

可能成立。

但：

$$
E_{\mathrm{prediction}}\approx0
$$

在正常受監管 RNG 條件下仍是合理預期。

---

# 21. 複雜遊戲不等於高 AI Edge

一個老虎機可以有：

- 50 條 payline；
- cascading reels；
- multipliers；
- free spins；
- stateful bonus；

使人類難以心算。

AI 可以把：

$$
EV
$$

算得更清楚。

但：

$$
\boxed{
\text{complex payoff structure}
\neq
\text{predictable random generator}.
}
$$

---

# 22. 百家樂位於一個有趣的中間區

標準 shoe baccarat 使用有限牌組，牌不放回。

因此嚴格來說：

$$
P(Y_{t+1}\mid S_t)
\neq
P(Y_{t+1}).
$$

牌組 composition 確實會隨已出牌變化。

所以它不是完全 IID。

---

# 23. 但主投注的決策空間非常小

在標準百家樂中，Player 與 Banker 的抽牌規則大多已由規則固定。

玩家主要決定：

$$
\text{which wager}
$$

而不是像 Blackjack 那樣在每手中連續決策：

- hit；
- stand；
- double；
- split。

因此：

$$
\boxed{
\text{state dependence exists}
}
$$

不代表：

$$
\boxed{
\text{large usable decision space exists}.
}
$$

---

# 24. 百家樂的歷史路紙問題

玩家常觀察：

- Banker streak；
- Player streak；
- alternating pattern；
- road maps。

但：

$$
\text{past Banker/Player labels}
$$

本身並不是完整牌組 composition。

因此：

$$
\boxed{
\text{outcome history}
\neq
\text{state representation}.
}
$$

即使牌組有狀態依賴，也不能推出單純追「莊閒走勢」具有可靠資訊價值。

---

# 25. Composition Effect 與 Pattern Effect 必須分開

牌靴遊戲可以有：

$$
I(S_t;Y_{t+1})>0,
$$

但仍可能：

$$
I(H^{\mathrm{labels}}_t;Y_{t+1})
\approx0.
$$

其中：

$$
S_t
$$

是完整剩餘牌 composition，

$$
H^{\mathrm{labels}}_t
$$

只是過往莊／閒結果序列。

因此：

$$
\boxed{
\text{stateful game}
\not\Rightarrow
\text{every historical pattern is informative}.
}
$$

---

# 26. Blackjack 是最重要的例外

Blackjack 同樣從有限牌靴不放回抽牌。

因此剩餘牌組：

$$
S_t
$$

會真正改變：

$$
P(Y_{t+1}\mid S_t).
$$

而玩家又擁有較豐富 action space。

所以：

$$
\boxed{
\text{state information}
+
\text{strategic action}
}
$$

同時存在。

---

# 27. Blackjack 的 AI 價值首先來自 Basic Strategy

對一般玩家而言，AI 不需要任何秘密資訊，就可以把：

$$
\pi_{\mathrm{novice}}
$$

修正到較接近：

$$
\pi_{\mathrm{basic}}.
$$

因此：

$$
EV(\pi_{\mathrm{basic}})
>
EV(\pi_{\mathrm{novice}})
$$

通常成立。

這是合法教育與離線學習層面的典型：

$$
E_{\mathrm{policy}}>0.
$$

---

# 28. 但 Basic Strategy 不等於必然正期望

即使：

$$
\pi=\pi_{\mathrm{basic}},
$$

在常見桌規下仍通常存在小幅 house edge。

因此：

$$
\boxed{
\text{optimal play under fixed rules}
\neq
\text{positive expectation}.
}
$$

---

# 29. 牌組狀態使 Blackjack 與輪盤分離

輪盤在理想模型中：

$$
P(Y_{t+1}\mid H_t)=P(Y_{t+1}).
$$

Blackjack shoe：

$$
P(Y_{t+1}\mid S_t)\neq P(Y_{t+1}).
$$

所以 Paper 01 的零互資訊結論不能直接套用完整 shoe state。

這是數學上真正不同的 regime。

---

# 30. 為什麼 AI 理論上會很強

如果允許機器完整觀察：

$$
S_t,
$$

AI 可以做到：

$$
S_t
\rightarrow
P_t
\rightarrow
Q_t(a)
\rightarrow
\pi_t^*.
$$

也就是依目前牌組狀態重新計算各 action 的期望。

因此：

$$
\boxed{
\text{AI capability}> \text{human mental calculation capability}
}
$$

完全可能成立。

---

# 31. 但這正是 Permission Gate 最重要的地方

Nevada 現行 NRS 465.075 規定，在持牌博彩場所或持牌業者提供的遊戲中，不得使用或意圖使用設計來取得遊戲優勢的：

- computerized device；
- electronic device；
- electrical device；
- mechanical device；
- software；
- hardware。

該條文列出的例子包括：

- 預測遊戲結果；
- 追蹤已出的牌或準備使用的牌；
- 分析遊戲事件概率；
- 分析遊戲或投注策略。

因此：

$$
\boxed{
\text{AI can calculate it}
}
$$

與：

$$
\boxed{
\text{AI may be used at the table}
}
$$

必須完全分離。

---

# 32. 這條法律其實比生成式 AI 早幾十年

Nevada 對這種電子優勢設備的限制早在現代 LLM、vision model 與 agent 以前就已存在。

因此今天：

$$
\text{camera}
+
\text{vision model}
+
\text{probability engine}
+
\text{voice advice}
$$

雖然技術形式全新，

制度所處理的核心問題卻仍是：

$$
\boxed{
\text{external computerized advantage assistance}.
}
$$

---

# 33. Human Skill 與 Device Assistance 可以具有不同法律地位

一個很經典的歷史對照是 1982 年 New Jersey Supreme Court 的 Uston v. Resorts International Hotel。

該案涉及使用人類 card counting 的 Blackjack 玩家。法院當時認為，在 New Jersey Casino Control Act 的架構下，賭場不能僅因 Uston 使用 card counting 策略而自行排除他，遊戲規則的權限屬於監管機構。

這個案件的重要性不是代表所有地方都允許或保障 card counting，而是說明：

$$
\boxed{
\text{human mental strategy}
}
$$

與：

$$
\boxed{
\text{electronic assistance}
}
$$

在法律上可以被視為完全不同的類型。

---

# 34. Jurisdiction Matters

因此不存在全球統一的：

$$
\text{AI casino legality}.
$$

更合理的是：

$$
Permission
=
P(
jurisdiction,
operator,
game,
device,
timing
).
$$

本系列所有法律討論都只能作為制度比較，不能取代特定司法管轄區的正式法律意見。

---

# 35. 賭場還可以改變狀態資訊的生命週期

如果某種策略依賴：

$$
S_t
$$

在多手之間持續累積，

賭場可以縮短：

$$
\tau_S.
$$

例如透過：

- 更頻繁洗牌；
- 較淺牌靴 penetration；
- continuous shuffling；
- 改變牌組數與桌規。

因此：

$$
\boxed{
\text{state edge}
\rightarrow
\text{rule response}
\rightarrow
\text{state-edge decay}.
}
$$

這與 Paper 00 的制度反身性完全一致。

---

# 36. Continuous Shuffling 的理論作用

若棄牌快速重新混回可抽取牌組，則：

$$
S_t
$$

相對前一手的長期記憶下降。

因此：

$$
I(H_{\mathrm{long}};Y_{t+1})
$$

也會下降。

這是一種：

$$
\boxed{
\text{information-reset countermeasure}.
}
$$

---

# 37. 賭場不必「比你的 AI 更聰明」

這點和運彩非常不同。

Sportsbook 若定價錯可能需要重新估計世界。

但 casino operator 往往控制：

$$
\boxed{
\text{game rules themselves}.
}
$$

因此它可以直接改變：

$$
G_t
\rightarrow
G_{t+1}.
$$

例如調整：

- payout；
- shuffle；
- deck count；
- table limits；
- allowed devices。

這使莊家擁有一種：

$$
\boxed{
\text{mechanism-design advantage}.
}
$$

---

# 38. House 是規則設計者，不只是對手

玩家問題：

$$
\max_\pi EV(\pi\mid G).
$$

莊家則部分擁有選擇：

$$
G.
$$

所以完整互動更像：

$$
\boxed{
\text{Player optimizes within }G
}
$$

而：

$$
\boxed{
\text{Operator manages }G.
}
$$

這是莊家制遊戲最深的結構性不對稱。

---

# 39. AI 不能只跟「普通玩家」比較

如果一篇論文說：

> AI Blackjack 玩家比一般玩家好 20%。

這只能證明：

$$
EV(\pi_{AI})>EV(\pi_{average}).
$$

真正要問：

$$
EV(\pi_{AI})
\overset{?}{>}
EV(\pi^*),
$$

以及：

$$
EV(\pi_{AI})
\overset{?}{>}0.
$$

這是三個不同 baseline。

---

# 40. 本文提出 Casino AI 三基準

### Baseline A — Naive Human

$$
B_N.
$$

### Baseline B — Optimal Permitted Strategy

$$
B_O.
$$

### Baseline C — Zero Expected Return

$$
B_0=0.
$$

AI 研究應分別報告：

$$
\Delta_N,
$$

$$
\Delta_O,
$$

$$
\Delta_0.
$$

---

# 41. AI 很容易打敗 Baseline A

對複雜賠表與策略遊戲：

$$
\Delta_N>0
$$

很合理。

---

# 42. AI 很難打敗 Baseline B

如果 optimal permitted strategy 已知且可精確計算，

則：

$$
\Delta_O\approx0.
$$

這意味模型再大也只是重新發現同一策略。

---

# 43. AI 更難跨過 Baseline C

若遊戲在最佳合法策略下仍：

$$
EV<0,
$$

則：

$$
\Delta_0<0.
$$

AI 只是讓負值比較小。

---

# 44. 這是 Casino AI 的三層幻覺

第一層：

> AI 贏過普通人，所以 AI 打敗賭場。

錯。

第二層：

> AI 預測比較準，所以 EV 為正。

錯。

第三層：

> AI 短期贏錢，所以找到了 edge。

仍然可能錯。

因此：

$$
\boxed{
\text{relative improvement}
\neq
\text{absolute advantage}.
}
$$

---

# 45. Side Bets 通常讓問題更複雜

很多桌遊加入：

- jackpot；
- pair；
- bonus；
- exotic side bets。

它們可能增加模型維度。

但複雜度本身不代表：

$$
EV\uparrow.
$$

甚至常常：

$$
h_{\mathrm{side}}>h_{\mathrm{main}}.
$$

因此 AI 最常做的合理事情反而可能是：

$$
\boxed{
\text{identify expensive complexity}.
}
$$

---

# 46. Complexity Tax

本文定義一個概念：

$$
C_X
=
h_{\mathrm{complex}}
-
h_{\mathrm{simple}}.
$$

如果某額外玩法只是增加娛樂性卻增加 house edge，

則：

$$
C_X>0.
$$

這可稱為：

$$
\boxed{
\text{Complexity Tax}.
}
$$

AI 可以讓玩家更容易看見它。

---

# 47. 這是一種資訊公平改善

若遊戲規則完全公開，但一般玩家無法理解：

$$
\text{probability complexity},
$$

AI 可以把：

$$
\text{opaque rules}
$$

轉成：

$$
\text{understandable EV}.
$$

因此 AI 的社會作用不一定是「幫人贏」。

也可能是：

$$
\boxed{
\text{reduce informational opacity}.
}
$$

---

# 48. 受監管 RNG 與 AI Audit 可以共存

玩家預測：

$$
\text{next outcome}
$$

可能沒有訊號。

但監管／研究 AI 仍可以測：

$$
P_{\mathrm{observed}}
\overset{?}{=}
P_{\mathrm{declared}}.
$$

因此：

$$
\boxed{
\text{No predictive edge}
\neq
\text{No auditing value}.
}
$$

這延續 Paper 01 的 Randomness Auditor。

---

# 49. Fair Game Integrity AI

在不以利用漏洞為目的的研究下，AI 可以用來檢查：

- 分布偏差；
- RNG drift；
- payout implementation；
- 異常設備；
- unexpected correlations；
- software regression。

這是一個：

$$
\boxed{
\text{operator/regulator-facing AI}
}
$$

而不是投注者 exploit engine。

---

# 50. 英國制度的另一個重要點：禁止 Adaptive Outcome Manipulation

UKGC RTS 7 不只要求不可預測。

它也禁止 compensated/adaptive behaviour：

$$
\boxed{
P(Y_{t+1})
}
$$

不應因玩家最近輸贏而被營運者動態操縱。

因此合法受監管系統中的：

> 你剛贏很多，所以機器故意不讓你贏；

不能被當作預設模型。

若有這類指控，正確問題是：

$$
\boxed{
\text{integrity investigation}
}
$$

而不是建立追輸贏「反算法」。

---

# 51. AI 不應替陰謀敘事生成數學外衣

如果玩家提供：

$$
20
$$

局輸贏資料，

AI 很容易敘述：

> 系統似乎在第 12 局後進入抑制狀態。

但沒有：

- 足夠樣本；
- null model；
- multiple-testing correction；
- game implementation evidence；

就不能推出：

$$
\text{adaptive manipulation}.
$$

這是 Paper 01 的 Narrative Overfitting 在 casino domain 的版本。

---

# 52. 線上合法 Casino 的核心信任問題

線上玩家無法直接觀察：

$$
\text{physical wheel}
$$

或：

$$
\text{internal RNG state}.
$$

因此公平性依賴：

$$
\boxed{
\text{regulation}
+
\text{testing}
+
\text{software integrity}
+
\text{audit}.
}
$$

這也是為什麼像 UKGC 與 GLI 的 RNG 標準比「AI 猜不猜得中」更根本。

---

# 53. AI 在這裡應該是 Verification Tool

合理研究方向：

$$
\text{declared rule}
\rightarrow
\text{expected distribution}
$$

再比較：

$$
\text{observed distribution}.
$$

即：

$$
D(
P_{\mathrm{obs}},
P_{\mathrm{rule}}
).
$$

這是：

$$
\boxed{
\text{verification}
}
$$

而不是：

$$
\boxed{
\text{exploitation}.
}
$$

---

# 54. Bankroll Management 不會創造 Alpha

AI 可以幫助控制：

$$
P(\text{ruin}),
$$

$$
Drawdown,
$$

$$
Variance.
$$

但若每個可選行動都滿足：

$$
EV(a)<0,
$$

單純資金管理不能創造：

$$
\exists a:EV(a)>0.
$$

所以：

$$
\boxed{
\text{risk management}
\neq
\text{alpha generation}.
}
$$

---

# 55. 但 Risk Management 仍有 Utility

如果玩家本來就把賭場視為娛樂消費：

$$
U
=
U_{\mathrm{entertainment}}
-
\lambda L
-
\gamma Risk,
$$

那 AI 可能透過：

- 預算；
- session limit；
- variance understanding；
- game selection；

增加：

$$
U.
$$

這仍然是真實價值，只是不是「打敗莊家」。

---

# 56. Gambling Utility 與 Profit Utility 不同

和 Paper 04 馬主效用類似，

玩家可能不是：

$$
\max E[\Pi].
$$

而是：

$$
U
=
\alpha E[\Pi]
+
\beta Entertainment
+
\gamma Social
-
\lambda Risk.
$$

因此一個理性娛樂玩家甚至可以接受：

$$
E[\Pi]<0,
$$

只要：

$$
U>0.
$$

---

# 57. 這不代表 House Edge 消失

娛樂效用只是表示：

$$
\boxed{
\text{negative financial EV}
}
$$

可能與：

$$
\boxed{
\text{positive total subjective utility}
}
$$

同時成立。

兩者不能混淆。

---

# 58. Casino 的 AI Counterpart 並不一定是「AI 莊家」

在 roulette / slot 類遊戲裡，莊家不需要即時預測玩家才能保持 edge。

因為：

$$
\boxed{
\text{edge is embedded in mechanism}.
}
$$

這比 sportsbook 更根本。

---

# 59. Mechanism Edge

定義：

$$
E_M
=
-EV_{\mathrm{player}}(\pi^*).
$$

如果即使最佳允許策略：

$$
EV_{\mathrm{player}}(\pi^*)<0,
$$

則：

$$
E_M>0.
$$

這就是莊家最強的優勢：

$$
\boxed{
\text{the rules themselves}.
}
$$

---

# 60. 所以 Casino 不需要每局打敗玩家

莊家可以輸：

$$
1,
10,
100
$$

局。

只要在足夠多獨立或弱相關投注中：

$$
E[R_{\mathrm{house}}]>0,
$$

大數法則會逐漸穩定 aggregate result。

因此：

$$
\boxed{
\text{house advantage is statistical, not prophetic}.
}
$$

---

# 61. AI 玩家與 Casino 的根本不對稱

玩家希望：

$$
\text{find positive conditional states}.
$$

莊家則希望：

$$
\text{design away or price those states}.
$$

因此：

$$
\boxed{
\text{Player searches the state space;}
}
$$

$$
\boxed{
\text{House partly controls the state space.}
}
$$

---

# 62. State Compression 是重要反制思想

如果 advantage 依賴長歷史：

$$
H_{t-k:t},
$$

賭場可透過頻繁 reset 使有效記憶長度：

$$
k_{\mathrm{eff}}\downarrow.
$$

因此：

$$
I(H_{\mathrm{old}};Y_{\mathrm{future}})
\downarrow.
$$

這是一個比「抓 AI」更根本的設計方法。

---

# 63. Rule Design 可以比 Anti-Cheat 更強

若能讓：

$$
S\rightarrow0,
$$

AI 就沒有大量可利用結構。

因此：

$$
\boxed{
\text{remove exploitable information}
}
$$

常常比：

$$
\boxed{
\text{detect every intelligent player}
}
$$

更容易。

---

# 64. 但不能把所有 Skilled Play 都等同作弊

必須區分：

$$
\text{mental skill},
$$

$$
\text{legal pre-game study},
$$

$$
\text{approved in-game information},
$$

$$
\text{prohibited external assistance}.
$$

不同地區與遊戲的界線不同。

因此治理不能用：

> 玩家太會算了。

作為唯一判準。

---

# 65. Permission Frontier

本文定義：

$$
\mathcal P
=
\{
a:
a\text{ is technically possible and permitted}
\}.
$$

真正允許玩家最佳化的是：

$$
\boxed{
\pi^*
=
\arg\max_{\pi\in\mathcal P}EV(\pi).
}
$$

而不是所有技術上可行策略的全集。

---

# 66. AI 時代使 Permission Frontier 更重要

以前：

$$
\mathcal P
$$

主要區分：

- 自己心算；
- 外部設備。

現在又增加：

- smartwatch；
- phone vision；
- cloud model；
- earbuds；
- remote human/AI assistance。

所以：

$$
\boxed{
\text{AI expands capability space faster than rule text changes}.
}
$$

但像 Nevada NRS 465.075 這類功能性法律因描述的是「取得遊戲優勢的電腦化設備／軟硬體用途」，仍可涵蓋大量新技術形式。

---

# 67. AI Casino Research 的安全邊界

本系列研究：

- house edge；
- information structure；
- optimal permitted policy；
- regulation；
- RNG integrity；
- countermeasure theory。

不提供：

$$
\text{device-assisted advantage play implementation},
$$

$$
\text{real-time casino prediction tooling},
$$

$$
\text{RNG seed recovery workflow},
$$

$$
\text{surveillance evasion},
$$

$$
\text{casino countermeasure bypass}.
$$

---

# 68. 第一核心命題：Computability Separation

$$
\boxed{
\text{Computable}
\not\Rightarrow
\text{Predictable}.
}
$$

House edge 可以被精確計算，但下一次結果仍可能不可預測。

---

# 69. 第二核心命題：Prediction Separation

$$
\boxed{
\text{Predictable}
\not\Rightarrow
\text{Profitable}.
}
$$

改善某些狀態預測不代表總 EV 已跨過：

$$
0.
$$

---

# 70. 第三核心命題：Permission Separation

$$
\boxed{
\text{Exploitable}
\not\Rightarrow
\text{Permitted}.
}
$$

Blackjack 電子輔助是最清楚的案例之一。

---

# 71. 第四核心命題：History-Adaptive Betting Invariance

若所有可下注時點都滿足：

$$
E[R_t\mid H_{t-1}]
=
-hb_t,
$$

其中：

$$
h>0,
$$

則任何只依據歷史決定：

$$
b_t
$$

的策略皆有：

$$
E[R_{\mathrm{total}}]<0.
$$

因此：

$$
\boxed{
\text{adaptive staking alone cannot reverse a fixed negative edge}.
}
$$

---

# 72. 第五核心命題：Relative Improvement Separation

可以同時成立：

$$
EV(\pi_{AI})
>
EV(\pi_{human}),
$$

以及：

$$
EV(\pi_{AI})<0.
$$

因此：

$$
\boxed{
\text{AI can make a gambler better without making gambling profitable}.
}
$$

---

# 73. 第六核心命題：Mechanism-Design Dominance

在莊家可調整規則的市場：

$$
\boxed{
\text{house can respond to information advantage by changing the mechanism}.
}
$$

因此 AI edge 不是固定自然常數，而受：

$$
G_t
$$

控制。

---

# 74. 第七核心命題：State-Lifetime Principle

若策略優勢依賴：

$$
I(S_t;Y_{t+1})>0,
$$

則縮短狀態有效生命：

$$
\tau_S
$$

通常會降低可累積資訊價值。

因此：

$$
\boxed{
\frac{\partial E_{\mathrm{state}}}{\partial \tau_S}>0
}
$$

可作為條件性假說。

---

# 75. 第八核心命題：Integrity–Exploitation Separation

發現：

$$
D(
P_{\mathrm{obs}},
P_{\mathrm{declared}}
)>0
$$

首先意味：

$$
\boxed{
\text{integrity question}.
}
$$

不應自動被轉化為：

$$
\boxed{
\text{player exploitation opportunity}.
}
$$

這是本系列研究倫理的重要邊界。

---

# 76. 四類遊戲的理論位置

| 類型 | 典型例子 | 歷史資訊價值 | AI 合理主要價值 |
|---|---|---:|---|
| 近 IID / RNG | Slots、電子 RNG | 很低 | 規則理解、RTP、audit |
| 物理但實務不可觀測 | Roulette | 通常很低 | EV、規則比較、integrity |
| 有限牌靴但低策略自由 | Baccarat | composition 有限影響 | 規則、EV、狀態研究 |
| 有限牌靴且策略自由較高 | Blackjack | 明確存在 | basic strategy、狀態理論、治理 |

這是一個理論分類，不代表所有場館、變體與司法管轄區完全相同。

---

# 77. 與 Paper 01 的關係

Paper 01 問：

$$
\boxed{
\text{Does history contain predictive information?}
}
$$

Paper 05 更進一步問：

$$
\boxed{
\text{If it does, can the player legally and economically use it?}
}
$$

因此 Paper 05 新增了：

$$
\boxed{
\text{Permission Gate}.
}
$$

---

# 78. 與 Paper 02 的差異

運彩市場中：

$$
\text{market price}
$$

會因新資訊重新調整。

莊家制 casino 則常把：

$$
\text{expected advantage}
$$

直接寫進規則。

所以：

$$
\boxed{
\text{Sportsbook}
\approx
\text{adaptive pricing problem},
}
$$

而：

$$
\boxed{
\text{Casino table/RNG game}
\approx
\text{mechanism-design problem}.
}
$$

---

# 79. 與 Paper 03 的差異

共同彩池：

$$
\text{participants create price}.
$$

莊家制賭場：

$$
\text{operator largely defines payoff mechanism}.
$$

因此：

$$
\boxed{
\text{AI participates in pricing}
}
$$

與：

$$
\boxed{
\text{AI operates inside a predefined mechanism}
}
$$

是兩種不同的博弈世界。

---

# 80. 真正的 Casino AI 四層模型

本文最終提出：

$$
\boxed{
\mathcal C_{AI}
=
(
G,
S,
\Pi,
P
)
}
$$

其中：

$$
G=\text{Game Mechanism},
$$

$$
S=\text{Observable State},
$$

$$
\Pi=\text{Permitted Strategy Space},
$$

$$
P=\text{Probability/Payoff Model}.
$$

AI 真正能做的是：

$$
\pi^*
=
\arg\max_{\pi\in\Pi}
E[R\mid G,S,P].
$$

如果：

$$
\max_{\pi\in\Pi}E[R]<0,
$$

那麼：

$$
\boxed{
\text{perfect AI still has negative expected return}.
}
$$

---

# 81. 這可能是整個系列最清楚的 AI 能力邊界之一

人工智慧可以：

- 計算得更快；
- 記得更多；
- 分析更多狀態；
- 執行更一致；
- 找到人類策略錯誤。

但它不能僅因為「智能更高」就違反：

$$
\boxed{
\text{probability structure}
}
$$

或：

$$
\boxed{
\text{game mechanism}.
}
$$

---

# 82. 結論

一般合法、正常運作、不作弊的莊家制賭場，確實是 AI 最不容易憑純粹預測能力取得持續正期望的傳統博弈環境之一。

原因並不是 AI 不夠強。

而是遊戲本身通常已經經過：

$$
\boxed{
\text{probability engineering}.
}
$$

在輪盤與合規 RNG 類遊戲中：

$$
I(H_t;Y_{t+1})\approx0.
$$

因此 AI 可以精確知道自己長期平均會輸多少，卻沒有足夠資訊知道下一次會發生什麼。

在 slots 類遊戲中，監管標準本來就要求 RNG 不可預測、符合宣稱分布，並禁止依玩家先前結果動態操縱下一次結果概率。

在百家樂中，牌靴 composition 使系統嚴格來說具有狀態依賴，但固定抽牌規則與有限決策空間使「存在狀態資訊」與「存在大型可用 edge」不能直接畫上等號。

Blackjack 則形成最重要的例外：

$$
\boxed{
P(Y_{t+1}\mid S_t)
\neq
P(Y_{t+1}),
}
$$

而且：

$$
\boxed{
\text{player action matters}.
}
$$

因此數學上確實存在更高的 AI state-analysis potential。

但也正因如此，制度開始直接介入：

$$
\boxed{
\text{Capability}
\rightarrow
\text{Permission Boundary}.
}
$$

Nevada 的現行法律甚至直接列出「預測結果、追蹤牌、分析事件概率、分析策略」等電子輔助用途作為禁止範圍。

所以最後形成：

$$
\boxed{
\text{Computable}
\neq
\text{Predictable}
\neq
\text{Exploitable}
\neq
\text{Permitted}.
}
$$

這四個詞不能再混用。

對一般玩家而言，AI 最現實的合法價值往往是：

$$
\boxed{
\text{bad strategy}
\rightarrow
\text{better strategy},
}
$$

$$
\boxed{
\text{opaque rules}
\rightarrow
\text{understandable expected value},
}
$$

以及：

$$
\boxed{
\text{high-cost game}
\rightarrow
\text{lower-cost game}.
}
$$

也就是：

$$
\boxed{
\text{reduce avoidable loss}
}
$$

而不是自動：

$$
\boxed{
\text{create positive alpha}.
}
$$

對監管者與營運者而言，AI 的價值則可能反過來是：

$$
\boxed{
\text{verify randomness}
+
\text{detect anomalies}
+
\text{protect game integrity}.
}
$$

因此傳統 casino game 為 AI 博弈研究提供了一個非常重要的負面邊界案例：

$$
\boxed{
\text{More intelligence does not guarantee more exploitable information.}
}
$$

如果遊戲機制已經把資訊結構壓縮到近似：

$$
I(X;Y)=0,
$$

那麼 AI 的最高手段也可能只是更快、更精確地得到同一個結論：

$$
\boxed{
EV<0.
}
$$

真正會讓下一篇產生巨大轉折的，是 Poker 與策略卡牌遊戲。

因為那裡不再是：

$$
\text{Player vs fixed mechanism}.
$$

而是：

$$
\boxed{
\text{Intelligence vs Intelligence}.
}
$$

當對手會觀察、欺騙、調整策略，而 AI 又可以即時進入決策迴路時，「公平」將不再只是 RNG 與 house edge 問題，而會正式變成：

$$
\boxed{
\text{Who generated the decision?}
}
$$

---

## References / Regulatory Anchors

1. UK Gambling Commission, *Remote Gambling and Software Technical Standards — RTS 7: Generation of Random Outcomes*, current standards accessed in 2026.  
2. UK Gambling Commission, *Remote Gambling and Software Technical Standards — Introduction*, updated March 2026.  
3. Gaming Laboratories International, *GLI-11: Gaming Devices*, RNG independence, available outcomes and unpredictability requirements.  
4. Nevada Revised Statutes, *NRS 465.075 — Use or possession of device, software or hardware to obtain advantage at playing game prohibited*, current Nevada statutory text accessed in 2026.  
5. *Uston v. Resorts International Hotel, Inc.*, 89 N.J. 163 (1982), Supreme Court of New Jersey, historical legal distinction involving human card counting.

---

**Next:**  
**Paper 06 — Poker、卡牌遊戲與 Human–AI Hybrid：從 Bot、Solver、RTA 到決策來源危機**
