# AI 運動博彩：世界模型、資訊延遲、概率校準與算法莊家

## AI Sports Betting: World Models, Information Latency, Probability Calibration, and Algorithmic Sportsbooks

**Series:** AI Game Intelligence, Randomness, and Adaptive Markets  
**Paper 02**  
**Version:** v0.1  
**Date:** 2026-09-01
**Author:** Neo.K with Aletheia（GPT-5.6 Sol）  
**Institution:** EveMissLab／一言諾科技有限公司

---

## 摘要

運動博彩與公平彩券、輪盤及合規 RNG 存在根本差異。

在近似 IID 的公平隨機系統中，歷史資料未必包含下一次結果的可利用資訊；但運動賽事是由運動員狀態、戰術、傷病、天候、賽程、旅行、場地、對手互動與其他大量真實世界變數共同生成的事件。

因此一般存在：

$$
I(X;Y)>0,
$$

其中 $X$ 為比賽前可觀測資訊， $Y$ 為比賽結果。

人工智慧可以透過更大的資料容量、更好的時序模型、多模態資訊整合、新聞解析與概率校準降低：

$$
H(Y\mid X).
$$

然而，「更能預測比賽」並不等於「能從運動博彩獲得超額收益」。

真正的對手不是隨機性，而是市場價格。

若模型估計：

$$
\hat P_{\mathrm{AI}}(Y)
$$

而博彩市場隱含概率為：

$$
P_{\mathrm{M}}(Y),
$$

則 AI 所需研究的核心量不是：

$$
\hat P_{\mathrm{AI}}(Y),
$$

而是：

$$
\boxed{
\Delta P
=
\hat P_{\mathrm{AI}}(Y)
-
P_{\mathrm{M}}(Y).
}
$$

即使 $\Delta P>0$，仍需扣除 bookmaker margin、價格變動、執行限制、模型誤差、相關風險與制度成本。

因此更完整的淨優勢為：

$$
\boxed{
\mathcal E_{\mathrm{net}}
=
\mathcal E_{\mathrm{forecast}}
+
\mathcal E_{\mathrm{information}}
+
\mathcal E_{\mathrm{timing}}
-
C_{\mathrm{margin}}
-
C_{\mathrm{execution}}
-
C_{\mathrm{error}}
-
C_{\mathrm{risk}}.
}
$$

本文進一步分析 probability calibration、opening/closing price、資訊延遲、市場效率異質性、favourite–longshot bias、算法莊家、AI 定價與風險管理。

2024 年一項 NBA 機器學習研究發現，以 calibration 而非 accuracy 選擇模型，在其歷史投注實驗中產生顯著不同的結果，顯示對博彩決策而言，知道「模型所說的 $60\%$ 是否真的接近 $60\%$ 」可能比單純猜對多少場更重要。

2025 年歐洲足球市場研究則顯示，同樣一批比賽的傳統 1X2 市場仍可觀察到 favourite–longshot bias，而 Asian handicap 市場卻能產生接近有效市場的概率預測。這表示市場效率並非單一常數，而是一個依市場結構、玩法與時間改變的局部性質。

因此，本篇提出：

$$
\boxed{
\text{AI Sports Betting}
\neq
\text{Sports Prediction}.
}
$$

更準確地說，它是一個：

$$
\boxed{
\text{World Model}
+
\text{Market Model}
+
\text{Latency Model}
+
\text{Uncertainty Model}
}
$$

共同構成的適應性市場問題。

---

# 1. 從 Paper 01 跨過 Randomness Boundary

Paper 01 建立：

若：

$$
I(X;Y)=0,
$$

則任何僅由 $X$ 產生的 representation：

$$
Z=f(X)
$$

都不能創造：

$$
I(Z;Y)>0.
$$

運動賽事則不同。

例如籃球比賽結果可能受到：

$$
X=
(
X_{\mathrm{player}},
X_{\mathrm{injury}},
X_{\mathrm{lineup}},
X_{\mathrm{rest}},
X_{\mathrm{travel}},
X_{\mathrm{strategy}},
X_{\mathrm{opponent}},
X_{\mathrm{venue}},
X_{\mathrm{official}},
\ldots
).
$$

因此通常：

$$
P(Y\mid X)\neq P(Y).
$$

也就是：

$$
\boxed{
I(X;Y)>0.
}
$$

這代表世界真的存在可以學習的 predictive structure。

---

# 2. 運動的不確定性不是純粹隨機

運動結果的不確定性可以粗略拆成：

$$
U
=
U_{\mathrm{epistemic}}
+
U_{\mathrm{aleatory}}.
$$

其中：

$$
U_{\mathrm{epistemic}}
$$

是因為我們不知道足夠資訊。

例如：

- 球員真實健康狀態；
- 戰術；
- 首發名單；
- 疲勞；
- 心理與準備程度。

而：

$$
U_{\mathrm{aleatory}}
$$

則是即使掌握大量資訊後仍存在的事件分岔。

例如：

- 一次失誤；
- 一顆球彈框；
- 臨場紅牌；
- 突發機械故障；
- 意外受傷；
- 裁判判定；
- 極端偶發事件。

AI 主要能降低的是：

$$
U_{\mathrm{epistemic}}.
$$

不能保證：

$$
U_{\mathrm{aleatory}}\rightarrow0.
$$

---

# 3. 所以 AI 的目標不是把 $70\%$ 變成 $100\%$

假設某球隊真正勝率為：

$$
P(Y=1)=0.70.
$$

即使存在一個完美概率模型：

$$
\hat P(Y=1)=0.70,
$$

仍然有：

$$
P(Y=0)=0.30.
$$

所以一次輸掉並不能證明模型錯。

反之，一次猜中也不能證明模型好。

因此：

$$
\boxed{
\text{Outcome correctness}
\neq
\text{probability correctness}.
}
$$

---

# 4. 運動博彩首先是一個 Probability Estimation Problem

一般分類器可能只輸出：

$$
\hat y\in\{0,1\}.
$$

但博彩真正需要：

$$
\hat p=P(Y=1\mid X).
$$

因為市場本身也給出一個概率型價格。

所以運彩 AI 不應只是：

> A 隊會贏。

而應該接近：

> 在目前資訊集合下，模型估計 A 隊勝率為某個概率分布。

因此：

$$
\boxed{
\text{Classification}
\rightarrow
\text{Probability Estimation}.
}
$$

---

# 5. Odds 本質上是一種價格

使用 decimal odds：

$$
O.
$$

最簡單的 implied probability 是：

$$
q=\frac{1}{O}.
$$

例如：

$$
O=2.00
$$

對應：

$$
q=0.50.
$$

但博彩公司通常加入 margin，所以同一市場所有結果的：

$$
\sum_i q_i
$$

通常大於：

$$
1.
$$

---

# 6. Overround

考慮二元市場：

$$
O_A=1.80,
$$

$$
O_B=2.10.
$$

則：

$$
q_A=\frac{1}{1.80}\approx0.5556,
$$

$$
q_B=\frac{1}{2.10}\approx0.4762.
$$

所以：

$$
q_A+q_B
\approx1.0318.
$$

多出的：

$$
0.0318
$$

可以視為簡化意義下的 overround。

因此：

$$
\boxed{
\text{raw implied probability}
\neq
\text{fair probability}.
}
$$

---

# 7. 市場概率需要去除 margin

最簡單的 normalization：

$$
P_M(A)
=
\frac{q_A}
{q_A+q_B}.
$$

於是：

$$
P_M(A)
\approx
\frac{0.5556}{1.0318}
\approx0.5385.
$$

這個數字比：

$$
0.5556
$$

更接近市場真正對 A 的相對概率判斷。

實際市場的 margin 結構可能更複雜，並不一定平均分配。

---

# 8. AI 真正的 benchmark 是市場

設模型：

$$
P_A(Y).
$$

市場：

$$
P_M(Y).
$$

若：

$$
P_A(Y)=P_M(Y),
$$

則 AI 即使非常準，也沒有額外資訊。

所以定義：

$$
\boxed{
\Delta_t(Y)
=
P_A(Y\mid X_t)
-
P_M(Y\mid \mathcal I_t).
}
$$

其中：

$$
X_t
$$

是 AI 的資訊集合，

$$
\mathcal I_t
$$

是市場在時間 $t$ 已經吸收的資訊。

真正研究的是：

$$
\Delta_t.
$$

---

# 9. 這是運彩和一般預測競賽最大的不同

Kaggle 式預測可能只要求：

$$
\min L(P_A,Y).
$$

但博彩市場要求：

$$
\min L(P_A,Y)
$$

同時還必須：

$$
P_A
\neq
P_M
$$

且差異方向正確。

如果市場本身就是非常強的 forecast ensemble：

$$
P_M\approx P^*,
$$

那麼：

$$
P_A\approx P^*
$$

還是不夠。

必須：

$$
\boxed{
P_A\text{ 比市場更接近 }P^*.
}
$$

---

# 10. 為什麼 Accuracy 很危險

假設模型 A：

$$
Accuracy=70\%.
$$

模型 B：

$$
Accuracy=60\%.
$$

直覺上 A 比 B 強。

但如果 A 的預測全部集中在巨大熱門，而市場早已知道：

$$
P_M=0.85,
$$

它即使猜對很多，也不一定存在價格優勢。

B 反而可能只在市場錯價時出手。

因此：

$$
\boxed{
\max Accuracy
\neq
\max Economic Value.
}
$$

---

# 11. Calibration

一個 calibrated model 應滿足：

當模型對大量事件輸出：

$$
\hat p=0.70,
$$

這些事件中約：

$$
70\%
$$

真的發生。

理想形式：

$$
P(Y=1\mid\hat P=p)=p.
$$

這叫：

$$
\boxed{
\text{Probability Calibration}.
}
$$

---

# 12. 為什麼 Calibration 比 Accuracy 更接近博彩問題

因為 expected value 使用的是：

$$
p,
$$

不是：

$$
\hat y.
$$

假設：

$$
O=2.00.
$$

如果模型說：

$$
p=0.52,
$$

跟：

$$
p=0.80
$$

在分類結果上都只是：

$$
\hat y=1.
$$

但兩者的經濟含義完全不同。

因此：

$$
\boxed{
\text{decision quality}
\propto
\text{probability quality}.
}
$$

---

# 13. 2024 NBA 機器學習研究

2024 年《Machine Learning with Applications》一篇研究直接比較：

$$
\text{accuracy-based model selection}
$$

與：

$$
\text{calibration-based model selection}.
$$

研究使用數季 NBA 資料訓練模型，並在單獨賽季進行歷史投注實驗。

作者報告，以 calibration 選擇模型在其設定下平均 ROI 約為：

$$
+34.69\%,
$$

而 accuracy-based selection 約為：

$$
-35.17\%.
$$

這些數字是特定歷史實驗結果，不能直接外推成現實中穩定可複製收益，但它非常清楚地證明：

$$
\boxed{
\text{模型選擇標準本身會改變投注決策品質。}
}
$$



---

# 14. Calibration 也不能只測一次

假設模型在：

$$
2018-2024
$$

整體 calibrated。

但：

$$
2025
$$

聯盟規則、打法、球員輪替或資料來源改變。

此時：

$$
P_t(Y\mid X)
$$

可能漂移。

所以應研究：

$$
Calibration(t).
$$

而不是：

$$
Calibration=\text{constant}.
$$

---

# 15. Brier Score

概率模型可以使用：

$$
BS
=
\frac{1}{N}
\sum_{i=1}^{N}
(\hat p_i-y_i)^2.
$$

若預測越接近真實結果：

$$
BS\downarrow.
$$

這比單純 accuracy 保留更多概率資訊。

---

# 16. Log Loss

另一個常用方法：

$$
LL
=
-\frac1N
\sum_i
\left[
y_i\log\hat p_i
+
(1-y_i)\log(1-\hat p_i)
\right].
$$

錯誤但極度自信的預測會被強烈懲罰。

這對博彩研究很重要，因為：

$$
\boxed{
\text{overconfidence}
}
$$

可能比普通 prediction error 更危險。

---

# 17. AI 的第一個真正優勢：資料規模

人類分析師只能同時追蹤有限資訊。

AI 可以整合：

$$
10^3
$$

甚至更多 variables：

- 球員資料；
- play-by-play；
- tracking；
- 傷病；
- 賽程；
- travel；
- opponent；
- formation；
- referee；
- weather；
- social/news；
- betting market。

因此：

$$
X_{\mathrm{AI}}
\supset
X_{\mathrm{human}}
$$

在某些工作流中可以成立。

---

# 18. 但 More Data 不一定等於 More Signal

Paper 01 的原則仍然成立：

$$
I(X_j;Y)\approx0
$$

的 feature 即使增加一百萬個：

$$
I(X_1,\ldots,X_m;Y)
$$

不一定因此實質增加。

而高維度反而增加：

$$
\text{overfitting}.
$$

因此：

$$
\boxed{
\text{data volume}
\neq
\text{information value}.
}
$$

---

# 19. AI 的第二個優勢：資訊整合

真正重要的往往不是單一資料。

例如：

$$
\text{player injury}
$$

本身可能不夠。

但加上：

$$
\text{replacement quality}
+
\text{opponent matchup}
+
\text{pace}
+
\text{rest}
$$

才形成：

$$
P(Y\mid X).
$$

因此 AI 的價值之一是：

$$
\boxed{
\text{relational integration}.
}
$$

---

# 20. AI 的第三個優勢：非結構化資訊

傳統 quantitative model 很擅長：

$$
CSV.
$$

但現代 LLM／多模態 AI 可以處理：

- 記者文字；
- 教練訪談；
- 傷病報告；
- 新聞；
- 社群；
- 球員訪談；
- 圖像；
- 場地資訊。

因此：

$$
X_{\mathrm{text}}
\rightarrow
Z_{\mathrm{semantic}}
$$

可以被轉換成模型可利用狀態。

---

# 21. 但 LLM 不應該直接取代概率模型

LLM 很容易產生：

> 我認為 A 隊有 68% 勝率。

但如果沒有 calibration：

$$
68\%
$$

可能只是語言生成。

所以比較穩健的架構是：

$$
\text{LLM}
\rightarrow
\text{information extraction}
$$

$$
\downarrow
$$

$$
\text{structured state}
$$

$$
\downarrow
$$

$$
\text{probabilistic model}.
$$

而不是：

$$
\text{prompt}
\rightarrow
\text{magic probability}.
$$

---

# 22. AI 的第四個優勢：速度

假設新資訊在：

$$
t_0
$$

出現。

玩家／AI 解析完成時間：

$$
t_A=t_0+\Delta t_A.
$$

市場完全吸收時間：

$$
t_M=t_0+\Delta t_M.
$$

若：

$$
\Delta t_A<\Delta t_M,
$$

則窗口：

$$
W=
\Delta t_M-\Delta t_A>0.
$$

這是：

$$
\boxed{
\text{Information Latency Window}.
}
$$

---

# 23. Edge 因此是時間函數

不能只寫：

$$
\Delta=P_A-P_M.
$$

更合理：

$$
\Delta(t)
=
P_A(t)-P_M(t).
$$

資訊剛出現：

$$
\Delta(t_0)>0.
$$

市場吸收後：

$$
\Delta(t)\rightarrow0.
$$

因此：

$$
\boxed{
\mathcal E=\mathcal E(t).
}
$$

---

# 24. 市場自己就是一個學習系統

市場中的：

- 專業玩家；
- 博彩公司；
- data provider；
- trading desk；
- public bettors；
- syndicates；

都會更新自己的：

$$
P_i(Y).
$$

下注、報價與賠率調整共同形成：

$$
P_M(Y).
$$

所以市場可以被視為：

$$
\boxed{
\text{Distributed Ensemble Forecaster}.
}
$$

---

# 25. Opening Line 與 Closing Line

設：

$$
P_O
$$

為 opening price 隱含概率，

$$
P_C
$$

為 closing price 隱含概率。

在公開資訊逐步進入市場時，通常可以把：

$$
P_C
$$

理解為吸收更多賽前資訊後的價格。

但：

$$
\boxed{
P_C
\neq
P_{\mathrm{true}}
}
$$

必須一直保留。

Closing line 只是很強的 benchmark，不是真理。

---

# 26. Closing Line Value 的研究意義

假設模型在較早時間預測：

$$
P_A.
$$

之後 closing line 移動到更接近：

$$
P_A.
$$

即：

$$
|P_A-P_C|
<
|P_A-P_O|,
$$

這表示模型可能比 opening market 更早包含後來被市場吸收的資訊。

因此即使短期實際比賽結果 variance 很大，

$$
\text{price movement}
$$

仍可以作為額外研究訊號。

---

# 27. 但不能把 Closing Line 當神

如果市場存在：

- crowd bias；
- liquidity problem；
- segmentation；
- regulatory constraint；
- bookmaker strategic pricing；

則：

$$
P_C
$$

仍然可能偏離：

$$
P^*.
$$

所以研究應同時測：

$$
Calibration(P_C)
$$

和：

$$
Calibration(P_A).
$$

---

# 28. 2024 MLB 即時賠率研究

2024 年《Management Science》研究分析四家 sportsbook、3,681 場 MLB 比賽從 opening 到 closing 的賠率變化。

研究發現市場 forecast 大致可靠，但仍存在部分簡單歷史策略可在其樣本中產生顯著獲利。

這說明：

$$
\boxed{
\text{mostly efficient}
\neq
\text{perfectly efficient}.
}
$$



---

# 29. 市場效率是一個局部概念

最危險的說法之一：

> 運彩市場是有效的。

應該問：

$$
\text{Which market?}
$$

$$
\text{Which sport?}
$$

$$
\text{Which bet type?}
$$

$$
\text{Which time?}
$$

$$
\text{Which liquidity regime?}
$$

---

# 30. 2025 歐洲足球研究給了一個漂亮例子

Hegarty 與 Whelan 比較同一批歐洲足球賽事的：

$$
1X2
$$

市場和：

$$
Asian\ Handicap.
$$

他們在傳統 1X2 市場仍觀察到明顯 favourite–longshot bias。

但 Asian handicap 市場的賠率可以形成高度有效的賽果 forecast。

因此：

$$
\boxed{
Efficiency(g,m,t)
}
$$

比：

$$
Efficiency=\text{True/False}
$$

更合理。

---

# 31. Favourite–Longshot Bias

一般定義可以理解成：

longshot 的價格相對過高，

也就是其實際報酬比市場表面概率暗示得更差。

反之 favourite 相對沒有那麼被高估。

簡化而言：

$$
P_{\mathrm{market}}(\text{longshot})
>
P_{\mathrm{true}}(\text{longshot})
$$

可能成立。

這種偏差在不同市場存在程度不同。

---

# 32. 為什麼市場會產生這種偏差？

可能原因包括：

- 玩家偏好高賠率；
- lottery-like utility；
- 娛樂效用；
- 需求彈性；
- 市場競爭程度；
- bookmaker pricing strategy。

2026 年刊於《Oxford Economic Papers》的研究從市場結構角度指出，競爭程度與 bookmaker 行為可能影響 favourite–longshot bias 是否出現；研究同樣發現 Asian handicap 與傳統賽果市場具有不同表現。

因此：

$$
\boxed{
\text{odds}
}
$$

不只是純粹的概率報告。

它也是：

$$
\boxed{
\text{market price}.
}
$$

---

# 33. 博彩公司也不是純 Prediction Machine

博彩公司的目標一般不是單純：

$$
\min |\hat P-P^*|.
$$

還包括：

$$
\max Profit,
$$

並管理：

$$
Risk,
$$

$$
Liability,
$$

$$
Liquidity,
$$

$$
Customer\ Behavior.
$$

因此 sportsbook price 可以抽象為：

$$
O_t
=
F(
P_t,
L_t,
D_t,
R_t,
C_t
),
$$

其中：

$$
P_t=\text{estimated event probability},
$$

$$
L_t=\text{liability},
$$

$$
D_t=\text{demand},
$$

$$
R_t=\text{risk},
$$

$$
C_t=\text{competition}.
$$

---

# 34. 這就是算法莊家的起點

傳統印象：

$$
\text{human oddsmaker}
\rightarrow
\text{odds}.
$$

現代 sportsbook 越來越接近：

$$
\text{data}
+
\text{models}
+
\text{trading systems}
+
\text{risk engines}
\rightarrow
\text{odds}.
$$

所以：

$$
\boxed{
\text{AI bettor}
}
$$

面對的常常不是：

$$
\text{human bookmaker}.
$$

---

# 35. Sportradar Alpha Odds

Sportradar 公開描述 Alpha Odds 為 AI-driven pricing platform。

系統會納入：

- real-time liabilities；
- predicted changes；
- customer behaviour；
- live market data；

進行快速賠率調整。

因此 bookmaker AI 問的是：

$$
\boxed{
\text{What price should be quoted now?}
}
$$

而不只是：

$$
\boxed{
\text{Who will win?}
}
$$

---

# 36. 所以雙方其實解不同最佳化問題

玩家 AI：

$$
\max
\mathcal E_{\mathrm{player}}.
$$

莊家 AI：

$$
\max
\left[
Profit
-
\lambda Risk
+
\eta Competitiveness
\right].
$$

因此兩者的 loss function 不同。

---

# 37. AI Bettor vs Algorithmic Sportsbook

現代結構可以表示：

$$
\begin{array}{ccc}
\text{World}
&&
\text{World}
\\
\downarrow
&&
\downarrow
\\
P_A(Y)
&
\leftrightarrow
&
P_B(Y)
\\
&&
\downarrow
\\
&&
O_t
\end{array}
$$

玩家觀察：

$$
O_t
$$

並比較：

$$
P_A.
$$

莊家則觀察：

$$
\text{world}
+
\text{market}
+
\text{player flow}.
$$

因此這是一個雙向 adaptive system。

---

# 38. 台灣是一個很好的 2026 案例

Sportradar 於 2023 年宣布成為第三屆台灣運動彩券的官方技術與服務供應商。

2024–2033 年的新系統包含：

$$
\text{ORAKO Sportsbook}
+
\text{Player Management}
+
\text{Managed Trading Services}
+
\text{Pre-match Odds}
+
\text{Live Odds}.
$$

Sportradar 也在台北建立本地團隊支援台灣運彩。

---

# 39. 這表示台灣不是「AI 玩家對人工莊家」

Sportradar 後續 case study 將台灣運彩描述為 fixed-odds sportsbook，並說明 ORAKO 系統目前支撐 2,622 個零售據點與線上渠道，搭配 trading 與 risk management 服務。

因此更合理的抽象是：

$$
\boxed{
\text{AI-assisted bettor}
\leftrightarrow
\text{algorithmic trading infrastructure}.
}
$$

---

# 40. 台灣的 Fixed Odds 特性

台灣運彩官方規範明確定義：

投注被彩券電腦系統接受當下的賠率即為固定賠率，後續賠率調整不影響已成立投注。

因此如果成交時：

$$
O(t_0)=O_0,
$$

即使：

$$
O(t_1)\neq O_0,
$$

已成立票券仍使用：

$$
O_0.
$$



---

# 41. 這使資訊時間具有經濟意義

假設：

$$
P_A(t_0)
$$

已經因新資訊更新，

但：

$$
O(t_0)
$$

仍代表舊價格。

則理論上存在：

$$
\Delta(t_0).
$$

等到：

$$
O(t_1)
$$

重新定價後：

$$
\Delta(t_1)\rightarrow0.
$$

這正是：

$$
\boxed{
\text{information latency}
}
$$

的重要性。

---

# 42. 但「看到價格」不等於一定可以成交

台灣運彩官方會員手冊明確提醒：

$$
\boxed{
\text{賠率會隨時變動。}
}
$$

而下注完成當下的賠率可能和下注者在賽事表看到的價格不同。

使用者甚至可以設定：

- 不接受任何賠率變化；
- 接受任何賠率變化；
- 只接受較高賠率變化。

如果選擇不接受，而提交期間價格改變，投注可能無法完成。

這表示：

$$
\boxed{
\text{observed edge}
\neq
\text{executed edge}.
}
$$

---

# 43. Execution Risk

定義：

$$
O_{\mathrm{seen}}
$$

為觀察時價格，

$$
O_{\mathrm{exec}}
$$

為真正成交價格。

若：

$$
O_{\mathrm{exec}}<O_{\mathrm{seen}},
$$

則：

$$
\mathcal E_{\mathrm{exec}}
<
\mathcal E_{\mathrm{observed}}.
$$

因此任何嚴格研究都必須保存：

$$
\boxed{
\text{execution-time price}.
}
$$

而不是只用網頁截圖價格。

---

# 44. 平台還具有 Risk Limits

台灣運彩現行會員條款允許營運方因節制投注或營運風險設定每日、每組合的投注量、最高投注額或最高派彩金額；超過限制時系統會自動拒絕投注。

所以：

$$
\boxed{
\text{model edge}
}
$$

和：

$$
\boxed{
\text{scalable edge}
}
$$

不是同一回事。

---

# 45. Scale Problem

假設存在：

$$
EV>0.
$$

但只能作用於非常小的：

$$
Q.
$$

則：

$$
Profit=Q\times EV.
$$

若：

$$
Q\rightarrow0,
$$

即使：

$$
EV
$$

很漂亮，經濟意義仍有限。

所以必須區分：

$$
\boxed{
\text{Edge Magnitude}
}
$$

與：

$$
\boxed{
\text{Edge Capacity}.
}
$$

---

# 46. 市場會觀察資金流

如果大量 sophisticated players 同時判斷：

$$
P_A>P_M,
$$

投注集中到同一方向。

系統不必知道：

> 這些人是不是使用 AI。

只需要知道：

$$
D_A\uparrow.
$$

於是可能：

$$
O_A\downarrow.
$$

因此：

$$
\boxed{
\text{smart money becomes information}.
}
$$

---

# 47. AI 自己會消滅 AI Edge

假設某方法：

$$
M
$$

有效。

初始：

$$
A=0.01
$$

只有 $1\%$ 市場參與者使用。

後來：

$$
A=0.50.
$$

大量玩家產生相似 probability estimate。

則：

$$
P_M\rightarrow P_M'
$$

更快速吸收該方法。

所以：

$$
\boxed{
\frac{\partial\mathcal E_{\mathrm{private}}}{\partial A}<0
}
$$

再次出現。

---

# 48. 這是 Paper 00 的 Edge Decay 在運彩中的具體形式

可寫成：

$$
\frac{d\Delta}{dt}
=
-\lambda A\Delta
+
\eta N_t,
$$

其中：

$$
A
$$

為 AI adoption，

$$
N_t
$$

為新的私人資訊流。

如果沒有新資訊：

$$
N_t=0,
$$

則：

$$
\Delta(t)
=
\Delta_0e^{-\lambda At}.
$$

這只是一個概念模型，但它清楚表示：

$$
\boxed{
\text{更高 adoption}
\rightarrow
\text{更快 edge decay}.
}
$$

---

# 49. 但新的資訊會不斷重新創造 Edge

運動世界本身持續產生：

$$
N_t>0.
$$

例如：

- 新傷病；
- 戰術改變；
- 天候；
- 臨場名單；
- 教練決策；
- 球員狀態。

因此 edge 不一定永遠消失。

它可能是：

$$
\text{appear}
\rightarrow
\text{decay}
\rightarrow
\text{appear}
\rightarrow
\text{decay}.
$$

所以：

$$
\boxed{
\mathcal E(t)
}
$$

是一個 stochastic process。

---

# 50. 運動 AI 的真正難題是 Regime Shift

設某球員歷史：

$$
P(Y\mid X,\theta_0).
$$

更換教練後：

$$
\theta_0\rightarrow\theta_1.
$$

此時舊資料仍然存在，但 mapping 改變：

$$
P_{\theta_0}(Y\mid X)
\neq
P_{\theta_1}(Y\mid X).
$$

所以：

$$
\boxed{
\text{more historical data}
}
$$

甚至可能降低模型品質。

---

# 51. Concept Drift

AI 必須區分：

$$
P_t(X)
$$

改變，

與：

$$
P_t(Y\mid X)
$$

改變。

前者是：

$$
\text{covariate shift},
$$

後者更接近：

$$
\text{concept drift}.
$$

例如三分球革命可以改變整個 NBA 的 scoring environment。

舊時代資料不一定能直接等權重使用。

---

# 52. 所以不能只做 Random Train/Test Split

運動資料也是時間序列。

應更接近：

$$
Train:
t_0,\ldots,t_k
$$

$$
Validate:
t_{k+1},\ldots,t_m
$$

$$
Test:
t_{m+1},\ldots,t_n.
$$

並且進行：

$$
\boxed{
\text{walk-forward evaluation}.
}
$$

這與 Paper 01 的原則相同。

---

# 53. 賠率也必須是當時真的存在的價格

最嚴重的 backtest 錯誤之一：

使用：

$$
\text{closing odds}
$$

來模擬：

$$
\text{morning decision}.
$$

但 closing odds 包含：

$$
t_{\mathrm{morning}}
$$

之後才出現的資訊。

這是：

$$
\boxed{
\text{price leakage}.
}
$$

---

# 54. 新聞資料更加危險

例如文章顯示：

> 球星因傷缺陣。

研究者必須知道：

$$
t_{\mathrm{publish}}.
$$

不能只知道：

$$
date.
$$

如果市場 14:03 得知，

模型假裝 09:00 已知：

$$
X_{09:00}=X_{14:03},
$$

就形成：

$$
\boxed{
\text{temporal information leakage}.
}
$$

---

# 55. LLM Search Agent 特別容易發生這個問題

因為今天搜尋到的網頁通常包含：

- 更新後版本；
- 最終名單；
- 比賽後分析；
- 修訂內容。

如果 AI 用今天的 web reconstruction 回測昨天：

$$
\boxed{
\text{future knowledge contamination}
}
$$

極其容易出現。

因此嚴格運彩 AI 需要：

$$
\boxed{
\text{point-in-time data}.
}
$$

---

# 56. World Model 與 Market Model 必須分離

本文提出兩個主要模型。

第一：

$$
M_W:
X_t\rightarrow P_W(Y).
$$

這是：

$$
\boxed{
\text{World Model}.
}
$$

第二：

$$
M_M:
Z_t\rightarrow P_M(Y,t+\Delta t).
$$

這是：

$$
\boxed{
\text{Market Model}.
}
$$

---

# 57. 為什麼還要預測市場？

假設現在：

$$
P_W(A)=0.60.
$$

當前市場：

$$
P_M(A)=0.52.
$$

看似：

$$
\Delta=0.08.
$$

但是另一個模型預測：

$$
P_M(A,t+10min)=0.60.
$$

代表市場正在快速修正。

所以：

$$
\boxed{
\text{event forecast}
}
$$

與：

$$
\boxed{
\text{price forecast}
}
$$

是兩個問題。

---

# 58. 更完整的是三模型結構

$$
M_1=\text{World Model},
$$

$$
M_2=\text{Market Model},
$$

$$
M_3=\text{Uncertainty Model}.
$$

第三個模型估：

$$
U_A=
P(
|P_A-P^*|>\epsilon
).
$$

也就是：

> AI 對自己的 probability estimate 有多不確定？

---

# 59. Meta-Uncertainty

假設：

$$
\hat P_A=0.60.
$$

不能只輸出：

$$
0.60.
$$

更理想：

$$
P_A
\sim
\mathcal D(\mu=0.60,\sigma).
$$

例如：

$$
\sigma=0.02
$$

跟：

$$
\sigma=0.15
$$

完全不同。

即：

$$
\boxed{
\text{Probability estimate}
+
\text{uncertainty of probability estimate}.
}
$$

---

# 60. 小 Edge 最容易被模型誤差吃掉

如果：

$$
P_A=0.53,
$$

$$
P_M=0.52,
$$

則：

$$
\Delta=0.01.
$$

但若模型 uncertainty：

$$
\sigma=0.05,
$$

那：

$$
\Delta
$$

幾乎沒有可靠意義。

因此更合理的判斷不是：

$$
\Delta>0,
$$

而是：

$$
\boxed{
P(\Delta>0\mid D)
}
$$

足夠高。

---

# 61. AI 不應把 Point Estimate 當真理

運動 AI 很容易產生：

$$
P=63.7481\%.
$$

看起來非常精確。

但真實資料可能只支持：

$$
P\in[0.54,0.69].
$$

所以：

$$
\boxed{
\text{decimal precision}
\neq
\text{epistemic precision}.
}
$$

這與生成式 AI 的 false certainty 問題直接相關。

---

# 62. Correlated Risk

運動市場中的多個預測不一定獨立。

例如：

- 同一球隊；
- 同一天候；
- 同一傷病資訊；
- 同一聯盟 regime；
- 同一模型 feature。

因此：

$$
Cov(R_i,R_j)\neq0.
$$

所以不能把：

$$
N
$$

個正期望事件簡單視為：

$$
N
$$

個獨立機會。

---

# 63. Portfolio View

設報酬向量：

$$
\mathbf R.
$$

期望：

$$
\boldsymbol\mu=E[\mathbf R].
$$

協方差：

$$
\Sigma=Cov(\mathbf R).
$$

那麼整體研究對象已開始接近：

$$
\boxed{
\text{portfolio decision under uncertainty}.
}
$$

這就是為什麼運彩研究與 quantitative finance 會逐漸靠近。

---

# 64. 但 Sports Event 不等於 Financial Asset

差異仍然存在。

比賽一旦結束：

$$
Y
$$

就確定。

博彩票券具有：

$$
\text{finite expiry}.
$$

而股票價格則持續演化。

因此運動博彩提供了一個很乾淨的研究環境：

$$
\text{forecast}
\rightarrow
\text{market price}
\rightarrow
\text{final truth}.
$$

---

# 65. 這也是為什麼博彩市場常被拿來研究 Market Efficiency

最終事件：

$$
Y
$$

是可以觀察的。

因此可以測：

$$
P_M
$$

到底 calibrated 不 calibrated。

金融中的：

$$
\text{true intrinsic value}
$$

通常沒有這麼清楚。

---

# 66. AI 與市場的資訊角色可以互換

一開始：

$$
AI
$$

使用市場：

$$
P_M
$$

當 feature。

之後 AI 大量普及：

$$
P_M
$$

本身越來越受到 AI 影響。

所以：

$$
\boxed{
AI\rightarrow Market\rightarrow AI.
}
$$

形成 feedback loop。

---

# 67. Reflexive AI Market

設：

$$
P_M(t)
=
F(
P_{H}(t),
P_{AI}(t),
Q(t)
),
$$

其中：

$$
P_H
$$

是人類資金判斷，

$$
P_{AI}
$$

是算法／AI 判斷，

$$
Q
$$

是資金分布。

當：

$$
AI\ share\uparrow,
$$

市場逐漸：

$$
\boxed{
\text{AI endogenous}.
}
$$

---

# 68. 所以未來 AI 不是「打敗人類市場」

可能變成：

$$
\boxed{
AI_A
+
Human_A
\quad
vs
\quad
AI_B
+
Human_B.
}
$$

甚至：

$$
\boxed{
\text{Model ecology}.
}
$$

不同模型：

- 對不同運動強；
- 對不同時間強；
- 對不同市場強；
- 對不同 regime 強。

---

# 69. 市場效率會因 AI 變得更局部、更快

以前某錯價可能存在：

$$
6\ hours.
$$

未來可能：

$$
20\ minutes.
$$

再往後：

$$
30\ seconds.
$$

因此：

$$
\boxed{
\text{Edge Half-Life}
}
$$

成為重要概念。

定義：

$$
\tau_{1/2}
$$

使：

$$
\Delta(t+\tau_{1/2})
=
\frac12\Delta(t).
$$

AI adoption 越高：

$$
\tau_{1/2}\downarrow.
$$

---

# 70. 本文提出 Information Edge Half-Life Hypothesis

對公開、機器可讀、容易解釋的資訊：

$$
\tau_{1/2}^{\mathrm{machine-readable}}
$$

應隨 AI adoption 上升快速下降。

但對：

- 模糊資訊；
- 私人資訊；
- 因果高度複雜資訊；
- 難以量化的人類觀察；

可能：

$$
\tau_{1/2}
$$

較長。

因此未來最大的 edge 可能從：

$$
\text{processing advantage}
$$

轉移成：

$$
\boxed{
\text{observation advantage}.
}
$$

---

# 71. 當人人都有同一個 LLM，LLM 本身就不再是 Edge

如果：

$$
Model_A=Model_B,
$$

$$
Data_A=Data_B,
$$

$$
Prompt_A\approx Prompt_B,
$$

則：

$$
P_A\approx P_B.
$$

於是：

$$
\Delta\rightarrow0.
$$

所以：

$$
\boxed{
\text{access to AI}
\neq
\text{AI advantage}.
}
$$

真正優勢來自：

$$
\text{unique data}
+
\text{better validation}
+
\text{better model}
+
\text{better timing}
+
\text{better uncertainty control}.
$$

---

# 72. AI 甚至可能讓普通玩家變得過度自信

生成式 AI 可以產生非常完整的理由：

> A 隊近十場攻守效率、主場、傷兵、對位都佔優。

但：

$$
\text{good explanation}
$$

不等於：

$$
\text{calibrated probability}.
$$

因此 Paper 01 的：

$$
\boxed{
\text{Narrative Overfitting}
}
$$

在運彩仍然成立。

---

# 73. Sports Narrative Overfitting

例如模型看到：

$$
10
$$

項支持 A 隊的理由。

人會以為：

$$
P(A)\uparrow\uparrow.
$$

但這十項可能高度相關：

$$
X_1\approx X_2\approx\cdots\approx X_{10}.
$$

其實都在描述同一個 underlying factor。

所以：

$$
10\ reasons
\neq
10\ independent\ evidence.
$$

---

# 74. 因果性問題

例如：

$$
\text{team has won 8 straight}
$$

跟：

$$
P(\text{next win})
$$

相關。

但真正原因可能是：

$$
\text{opponent strength},
$$

$$
\text{injury recovery},
$$

$$
\text{schedule}.
$$

如果模型只學：

$$
winning\ streak\rightarrow win,
$$

regime 改變後可能失效。

所以：

$$
\boxed{
\text{correlation feature}
\neq
\text{stable causal feature}.
}
$$

---

# 75. Market Feature 也可能造成 Circularity

假設 AI 使用：

$$
O_t
$$

作為重要 feature。

模型表現很好。

但這可能只是：

$$
AI
\approx
Market.
$$

而不是：

$$
AI>Market.
$$

所以必須分別測：

$$
L(P_A,Y)
$$

與：

$$
L(P_M,Y).
$$

以及：

$$
L(P_A,Y)-L(P_M,Y).
$$

---

# 76. 市場是非常強的 Baseline

因此運彩 AI 研究不應只跟：

$$
random
$$

比較。

最低 baseline 應包括：

$$
\boxed{
\text{market-implied probability}.
}
$$

如果連市場都沒有 beat：

$$
L_A\geq L_M,
$$

則：

$$
\boxed{
\text{沒有證據顯示模型提供額外概率資訊。}
}
$$

---

# 77. 甚至「Beat Market」也必須 Prospective

歷史中反覆：

- 挑 feature；
- 改模型；
- 換聯盟；
- 換季；
- 換市場；

直到找到：

$$
ROI>0
$$

仍然可能是：

$$
\boxed{
\text{researcher overfitting}.
}
$$

所以最終仍應：

$$
Freeze
\rightarrow
Forward Test.
$$

---

# 78. 運彩研究的四個驗證層級

本文提出：

### Level 1 — Outcome Prediction

$$
L_A<L_{\mathrm{naive}}.
$$

只證明模型比 naive 好。

### Level 2 — Market Prediction

$$
L_A<L_M.
$$

證明模型概率優於市場 benchmark。

### Level 3 — Price-Timed Prediction

模型在當時可取得的價格與資訊下仍有：

$$
\Delta>0.
$$

### Level 4 — Net Economic Evidence

扣除：

$$
C
$$

後仍：

$$
EV_{\mathrm{net}}>0
$$

且能 out-of-sample 重複。

四層不能跳級。

---

# 79. 這解釋很多「AI 運彩 70% 勝率」宣傳為什麼沒有意義

因為沒有告訴：

$$
O_i,
$$

不知道：

$$
P_M,
$$

不知道：

$$
margin,
$$

不知道：

$$
sample selection,
$$

不知道：

$$
timing.
$$

所以：

$$
\boxed{
Accuracy=70\%
}
$$

本身幾乎不能回答：

$$
\boxed{
EV>0?
}
$$

---

# 80. 運動中的運氣沒有被 AI 消滅

即使一個模型：

$$
P_A
$$

完全正確，

短期仍可能：

$$
R<0.
$$

這是：

$$
\boxed{
\text{variance}.
}
$$

因此：

$$
\text{short-term loss}
\not\Rightarrow
\text{bad model}.
$$

反過來：

$$
\text{short-term profit}
\not\Rightarrow
\text{good model}.
$$

---

# 81. 真正要看的是 Long-Run Calibration 與 Expected Return

如果：

$$
N\rightarrow\infty,
$$

且模型穩定，

才能逐步判斷：

$$
\hat P\rightarrow P.
$$

但是運動世界又會 drift。

因此實際問題永遠介於：

$$
\text{need more samples}
$$

與：

$$
\text{old samples become stale}.
$$

這是運動 AI 的核心統計困境之一。

---

# 82. Sample Efficiency–Drift Tradeoff

資料窗口太短：

$$
Variance\uparrow.
$$

太長：

$$
Bias_{\mathrm{stale}}\uparrow.
$$

所以存在：

$$
W^*
=
\arg\min_W
\left[
Variance(W)
+
StalenessBias(W)
\right].
$$

這個最佳窗口會隨運動與 regime 不同。

---

# 83. 這也是 AI 可能真正超過傳統模型的地方

AI 可以學：

$$
W=W(X,t)
$$

而不是固定：

$$
W=3\ years.
$$

例如：

某些球員資訊使用：

$$
30\ days.
$$

某些教練特性使用：

$$
5\ years.
$$

某些主場效應使用：

$$
10\ years.
$$

形成：

$$
\boxed{
\text{multi-timescale world model}.
}
$$

---

# 84. 但模型越複雜，Falsification 越重要

如果模型可以自動：

- 選 window；
- 選 feature；
- 選 sport；
- 選 market；
- 選 threshold；

hypothesis space：

$$
|\mathcal H|\uparrow.
$$

Paper 01 的 multiple-testing 問題再次回來。

所以：

$$
\boxed{
\text{better AutoML}
\Rightarrow
\text{need stronger epistemic control}.
}
$$

---

# 85. AI Sports Betting 的真正研究架構

本文提出：

$$
\boxed{
\mathcal S=
(
W,
M,
L,
U,
V
)
}
$$

其中：

$$
W=\text{World Model},
$$

$$
M=\text{Market Model},
$$

$$
L=\text{Latency Model},
$$

$$
U=\text{Uncertainty Model},
$$

$$
V=\text{Validation Layer}.
$$

缺任何一層都容易把 prediction 誤認成 edge。

---

# 86. World Model

$$
M_W:
X_t\rightarrow P_W(Y).
$$

問題：

> 世界現在發生什麼？

---

# 87. Market Model

$$
M_M:
O_t,Q_t,Z_t
\rightarrow
P_M(t+\Delta t).
$$

問題：

> 市場目前怎麼理解世界，而且接下來會怎麼重新定價？

---

# 88. Latency Model

$$
M_L:
I_t
\rightarrow
\tau_{\mathrm{absorb}}.
$$

問題：

> 這項資訊多久會被市場吸收？

---

# 89. Uncertainty Model

$$
M_U:
D_t
\rightarrow
U(P_W).
$$

問題：

> 我們有多不確定自己的 probability estimate？

---

# 90. Validation Layer

$$
M_V
$$

不負責預測。

它負責問：

$$
\boxed{
\text{這個 edge 到底是真的，還是我們自己回測出來的？}
}
$$

因此：

$$
V
$$

可能是整個系統最重要的一層。

---

# 91. 第一核心命題：World–Market Gap

定義：

$$
G_{WM}
=
P_W(Y)-P_M(Y).
$$

只有：

$$
G_{WM}\neq0
$$

才存在值得進一步研究的 market disagreement。

因此：

$$
\boxed{
\text{Sports prediction value}
\propto
\text{correct disagreement with market}.
}
$$

不是：

$$
\text{prediction accuracy alone}.
$$

---

# 92. 第二核心命題：Calibration Dominance

若兩個模型 accuracy 相近，但：

$$
Cal(M_A)<Cal(M_B),
$$

其中較小代表較佳 calibration error，

則在依賴 probability magnitude 的決策中：

$$
M_A
$$

可能比：

$$
M_B
$$

具有更高實用價值。

因此：

$$
\boxed{
\text{Calibration is a first-class variable}.
}
$$

2024 NBA 研究提供了支持這一方向的具體實驗案例。

---

# 93. 第三核心命題：Efficiency Heterogeneity

不存在單一：

$$
E_{\mathrm{market}}.
$$

更合理：

$$
\boxed{
E
=
E(
sport,
league,
market,
time,
liquidity,
information
).
}
$$

2025 足球研究中 1X2 與 Asian handicap 的差異正是此命題的一個實證例子。

---

# 94. 第四核心命題：Information Half-Life

任何公開資訊 $I$ 存在：

$$
\tau_I.
$$

使其私人可利用價值逐漸下降。

AI adoption：

$$
A\uparrow
$$

通常導致：

$$
\tau_I\downarrow.
$$

因此：

$$
\boxed{
\text{AI competition compresses informational time}.
}
$$

---

# 95. 第五核心命題：Adaptive Bookmaker Response

博彩公司並非固定函數：

$$
O=f(P).
$$

而是：

$$
\boxed{
O_t
=
f(
P_t,
Q_t,
L_t,
R_t,
C_t
).
}
$$

因此玩家 edge 改變：

$$
Q_t
$$

後，

又會反過來改變：

$$
O_t.
$$

這形成：

$$
\boxed{
\text{endogenous counter-response}.
}
$$

---

# 96. 第六核心命題：AI Edge Self-Consumption

若一個方法：

$$
M
$$

被足夠大量資金採用：

$$
A_M\uparrow,
$$

則由該方法產生的市場價格修正會使：

$$
\mathcal E_M\downarrow.
$$

即：

$$
\boxed{
\text{successful public strategy tends to consume its own edge}.
}
$$

---

# 97. 第七核心命題：Prediction–Execution Separation

即使：

$$
P_W>P_M,
$$

也只有在：

$$
O_{\mathrm{exec}}
$$

仍保留足夠價格時才可能實現。

因此：

$$
\boxed{
\text{Detected Edge}
\neq
\text{Executable Edge}.
}
$$

台灣運彩官方「賠率可於投注提交期間變動」的機制就是清楚案例。

---

# 98. 第八核心命題：AI vs AI Equilibrium

當：

$$
A_{\mathrm{player}}\uparrow
$$

且：

$$
A_{\mathrm{bookmaker}}\uparrow,
$$

長期均衡不一定是：

$$
\text{players win}.
$$

更可能是：

$$
\boxed{
\text{market efficiency}\uparrow.
}
$$

也就是：

$$
\text{obvious mispricing}\downarrow,
$$

$$
\text{information absorption speed}\uparrow.
$$

---

# 99. 因此 AI 的社會結果可能與個人結果相反

個人：

$$
\mathcal E_{\mathrm{private}}\downarrow.
$$

市場：

$$
\mathcal E_{\mathrm{system}}\uparrow.
$$

即：

$$
\boxed{
\text{smarter participants}
\rightarrow
\text{harder market}.
}
$$

這就是 Paper 00 的 Market Intelligence Hypothesis 在運彩市場的具體版本。

---

# 100. 研究邊界

本文不提供：

$$
\text{real-time betting assistant},
$$

$$
\text{automatic odds scraper-to-bet execution},
$$

$$
\text{live wager automation},
$$

$$
\text{deployable exploitation system}.
$$

本文研究：

- AI probability estimation；
- calibration；
- market efficiency；
- information latency；
- bookmaker adaptation；
- sports-world uncertainty；
- validation；
- market ecology。

核心目標是理解：

$$
\boxed{
\text{AI 在真實世界事件市場中如何改變資訊、價格與競爭。}
}
$$

而不是建立自動下注工具。

---

# 101. 與 Paper 01 的核心差異

Paper 01：

$$
I(X;Y)\approx0.
$$

因此：

$$
\mathcal E_{\mathrm{prediction}}\approx0.
$$

Paper 02：

$$
I(X;Y)>0.
$$

但即使如此：

$$
\boxed{
\mathcal E_{\mathrm{economic}}
}
$$

仍可能：

$$
\leq0.
$$

因為還存在：

$$
P_M,
$$

$$
C,
$$

$$
R.
$$

所以：

$$
\boxed{
\text{information existence}
\neq
\text{market advantage}.
}
$$

---

# 102. 從 Randomness Boundary 到 Market Boundary

Paper 01 問：

$$
\boxed{
\text{Is there anything to predict?}
}
$$

Paper 02 問：

$$
\boxed{
\text{Does the market already know it?}
}
$$

這兩個問題形成 AI 博弈研究的前兩道 Gate。

第一道：

$$
G_1:
I(X;Y)>0?
$$

第二道：

$$
G_2:
P_A\neq P_M?
$$

再下一道：

$$
G_3:
EV_{\mathrm{net}}>0?
$$

---

# 103. AI Sports Betting 三重門

可以正式寫成：

$$
\boxed{
\begin{array}{c}
\text{Predictability Gate}\\
I(X;Y)>0
\\
\downarrow\\
\text{Market Edge Gate}\\
P_A-P_M\neq0
\\
\downarrow\\
\text{Net Value Gate}\\
EV-C>0
\end{array}
}
$$

只有三道都成立：

$$
\boxed{
\text{demonstrated economic edge}
}
$$

才有研究意義。

---

# 104. 結論

運動博彩不是對純隨機性的預測。

運動世界具有：

$$
I(X;Y)>0.
$$

因此 AI 理論上確實可以透過更好的資料、更完整的 world model、更快的資訊處理與更好的 probability calibration 降低預測誤差。

但是：

$$
\boxed{
\text{better sports prediction}
\neq
\text{better sports betting}.
}
$$

因為在博彩市場中，另一個智能系統已經存在：

$$
\boxed{
\text{the market}.
}
$$

市場本身持續聚合：

- 博彩公司的模型；
- 專業玩家；
- 公開資訊；
- 資金流；
- 新聞；
- 交易風險。

因此真正的 AI 問題不是：

> 哪支隊伍會贏？

而是：

$$
\boxed{
P_{\mathrm{AI}}(Y)
-
P_{\mathrm{market}}(Y)
=
?
}
$$

即使存在：

$$
\Delta P>0,
$$

仍必須問：

$$
\boxed{
\text{Is the model calibrated?}
}
$$

$$
\boxed{
\text{Is the information point-in-time valid?}
}
$$

$$
\boxed{
\text{Will the price still exist when executed?}
}
$$

$$
\boxed{
\text{Does the edge survive costs and uncertainty?}
}
$$

$$
\boxed{
\text{How quickly will the market learn it?}
}
$$

因此現代 AI 運彩的完整問題不是：

$$
\text{AI}
\rightarrow
\text{Sports Result}.
$$

而是：

$$
\boxed{
\text{World}
\rightarrow
\text{AI World Model}
\rightarrow
\text{Probability}
}
$$

同時：

$$
\boxed{
\text{World}
\rightarrow
\text{Market}
\rightarrow
\text{Price}.
}
$$

兩者之間暫時存在：

$$
\Delta(t).
$$

但：

$$
\Delta(t)
$$

會受到其他 AI、資金、博彩公司、價格調整與資訊傳播反向影響。

因此最終形成：

$$
\boxed{
\text{AI}
\leftrightarrow
\text{Market}
\leftrightarrow
\text{AI}.
}
$$

這不是一個單向的 prediction problem。

而是一個：

$$
\boxed{
\text{Adaptive Intelligence Market}.
}
$$

人工智慧越強，不一定代表投注者越容易獲取超額收益。

在某些情況下，更可能發生：

$$
\boxed{
\text{AI capability}\uparrow
\Rightarrow
\text{information absorption}\uparrow
\Rightarrow
\text{market efficiency}\uparrow
\Rightarrow
\text{obvious private edge}\downarrow.
}
$$

因此，AI 對運動博彩最深刻的影響可能不是：

> AI 終於能預測體育。

而是：

$$
\boxed{
\text{體育賽事的概率價格形成，本身逐漸變成 AI 與 AI 之間的競爭。}
}
$$

---

## References / Empirical Anchors

- 2024 年《Machine Learning with Applications》研究：在 NBA 歷史資料實驗中，比較 accuracy-based 與 calibration-based 模型選擇，強調 calibration 對概率型博彩決策的重要性。
- Hegarty & Whelan，2025，《International Journal of Forecasting》：比較歐洲足球 1X2 與 Asian handicap 市場，發現兩者存在顯著不同的效率特徵。
- Simon，2024，《Management Science》：分析 MLB opening-to-closing sportsbook price movement，發現市場整體高度可靠但並非完全無效率。
- Oxford Economic Papers，2026：討論 bookmaker 市場結構與 favourite–longshot bias 的形成。
- Sportradar Alpha Odds：AI/ML pricing 系統納入即時 liability、客戶行為與市場資訊。
- Sportradar / Taiwan Sports Lottery：第三屆台灣運彩 2024–2033 使用 ORAKO、Managed Trading Services、pre-match/live odds 與相關 sportsbook infrastructure。
- 台灣運彩現行投注規範與線上條款：固定賠率、動態賠率變更、交易拒絕與風險投注限制。

---

**Next:**  
**Paper 03 — AI 賽馬與共同彩池市場：日本 JRA、美國 CAW、香港量化生態與群體價格形成**