# AI 賽馬與共同彩池市場：日本 JRA、美國 CAW、香港量化生態與群體價格形成

## AI Horse Racing and Pari-Mutuel Markets: Japan JRA, U.S. CAW, Hong Kong Quant Ecosystems, and Collective Price Formation

**Series:** AI Game Intelligence, Randomness, and Adaptive Markets  
**Paper 03**  
**Version:** v0.1  
**Date:** 2026-09-01
**Author:** Neo.K with Aletheia（GPT-5.6 Sol）  
**Institution:** EveMissLab／一言諾科技有限公司

---

## 摘要

賽馬博彩與固定賠率運動博彩具有一個根本差異：在大量主要賽馬市場中，價格不是由單一博彩公司在下注前固定給出，而是透過 pari-mutuel 共同彩池，由所有參與者的投注共同形成最終派彩。

因此，AI 賽馬不是單純的：

$$
\text{Horse Data}
\rightarrow
P(\text{Horse Wins}).
$$

完整問題至少包含三個相互耦合的模型：

$$
M_H=\text{Horse World Model},
$$

$$
M_C=\text{Crowd Model},
$$

$$
M_P=\text{Pool Dynamics Model}.
$$

第一個模型估計馬匹真實結果概率；第二個模型估計其他投注者如何配置資金；第三個模型估計投注流如何改變最終彩池、賠率與可實現回報。

因此真正需要預測的不是只有：

$$
P_i=P(\text{horse }i\text{ wins}),
$$

還包括：

$$
B_i(T)=\text{closing pool money on horse }i,
$$

以及：

$$
O_i(T)=\text{final dividend or odds at pool close}.
$$

更重要的是，在共同彩池中，大型投注者自己的投注額 $q$ 會改變價格，因此：

$$
O_i=O_i(q).
$$

這產生一種固定賠率市場較弱、共同彩池市場特別明顯的自我價格衝擊：模型即使發現理論上的正期望值，也可能因自己的資金進場而消耗該優勢。

本文以日本 JRA、美國 Computer Assisted Wagering（CAW）與香港賽馬會為三種不同制度路徑。日本呈現 AI handicap 與官方資料工具逐步民主化；美國已形成大型高速量化投注階層，並促使 NYRA 等賽馬機構直接修改高頻投注的時間規則；香港則具有數十年的電腦化賽馬投注歷史，從 William Benter 的實戰模型一路發展到全球 commingled pool、高速賠率基礎設施與巨額流動性。

本文據此提出：

$$
\boxed{
\text{AI horse-racing edge}
=
\text{horse-model edge}
+
\text{crowd-model edge}
+
\text{pool-model edge}
-
\text{takeout}
-
\text{price impact}
-
\text{uncertainty}
}
$$

並進一步主張，賽馬可能是 AI 博弈研究中最接近「群體智能價格形成」與「量化市場微觀結構」的傳統博彩案例之一。

本篇僅研究公開制度、數學結構、歷史案例與市場生態，不提供自動下注、即時 CAW、投注執行、資金最佳化或可直接部署的博彩系統。

---

# 1. 從 Paper 02 的固定價格跨入共同彩池

Paper 02 的核心結構是：

$$
\text{AI World Probability}
\leftrightarrow
\text{Bookmaker Price}.
$$

在 fixed-odds sportsbook 中，只要投注成交於：

$$
O(t_0),
$$

後續價格變化通常不改變已成交票券的回報。

共同彩池則不同。

參與者不是單純接受一個外部價格，而是在共同生成：

$$
O(T).
$$

因此市場從：

$$
\boxed{\text{price-taking}}
$$

部分轉變成：

$$
\boxed{\text{price-forming}}.
$$

---

# 2. Pari-Mutuel 的基本結構

設一個彩池總投注額為：

$$
Q.
$$

營運方扣除比例為：

$$
\tau.
$$

可供派彩的資金約為：

$$
Q_R=(1-\tau)Q.
$$

若某一結果 $i$ 上的總投注為：

$$
B_i,
$$

在最簡化的單一勝出結果模型下，每單位投注的 gross dividend 可近似寫為：

$$
D_i
=
\frac{(1-\tau)Q}{B_i}.
$$

這不是每一司法管轄區的精確法定派彩公式，但足以表示共同彩池的核心市場機制。

---

# 3. Odds 在共同彩池中是內生變數

定義投注份額：

$$
s_i=\frac{B_i}{Q}.
$$

則：

$$
D_i
\approx
\frac{1-\tau}{s_i}.
$$

因此：

$$
B_i\uparrow
$$

會導致：

$$
D_i\downarrow.
$$

也就是：

$$
\boxed{
\text{more money on a horse}
\rightarrow
\text{lower final payoff}
}
$$

這不是博彩公司主動懲罰熱門投注，而是 pari-mutuel 分配公式本身的結果。

---

# 4. 市場概率其實是資金分布

如果忽略抽水與其他制度修正，可以把：

$$
s_i
$$

理解為群體對結果 $i$ 的相對信念投影之一。

所以共同彩池其實把：

$$
\text{belief}
+
\text{capital}
$$

壓縮成：

$$
\boxed{\text{market share of pool}}.
$$

因此 AI 不只可以把 odds 當價格，也可以把它當一個即時的群體感測器。

---

# 5. 共同彩池裡最重要的一件事：自己的錢會改變自己的價格

假設目前：

$$
Q
$$

為總池，某馬已有：

$$
B_i.
$$

若一名大型投注者再加入：

$$
q
$$

到同一結果，則新的 dividend 近似變成：

$$
D_i(q)
=
\frac{(1-\tau)(Q+q)}{B_i+q}.
$$

因此：

$$
\frac{\partial D_i(q)}{\partial q}
=
(1-\tau)
\frac{B_i-Q}{(B_i+q)^2}.
$$

因為一般：

$$
B_i<Q,
$$

所以：

$$
\boxed{
\frac{\partial D_i(q)}{\partial q}<0.
}
$$

也就是自己的資金越大，自己能取得的價格越差。

---

# 6. 這產生 Edge Capacity

Paper 02 已區分：

$$
\text{Edge Magnitude}
$$

與：

$$
\text{Edge Capacity}.
$$

在共同彩池中，這個問題更加直接。

一個模型可能發現：

$$
P_iD_i(0)-1>0.
$$

但不代表對任意：

$$
q
$$

仍然有：

$$
P_iD_i(q)-1>0.
$$

所以：

$$
\boxed{
\text{small-money edge}
\neq
\text{large-capital edge}.
}
$$

---

# 7. 這是賽馬與固定賠率運彩的重要差異

固定賠率市場主要問題是：

$$
\text{Can I execute before the price moves?}
$$

共同彩池則多了一層：

$$
\boxed{
\text{Will my own execution move the final price?}
}
$$

因此高資金 AI 投注者不能只研究事件概率。

還必須研究：

$$
\boxed{\text{market impact}}.
$$

---

# 8. AI 賽馬的三模型架構

本文提出：

$$
\boxed{
\mathcal M_{HR}
=
(M_H,M_C,M_P)
}
$$

其中：

$$
M_H=\text{Horse World Model},
$$

$$
M_C=\text{Crowd Model},
$$

$$
M_P=\text{Pool Dynamics Model}.
$$

---

# 9. Horse World Model

第一個模型估計：

$$
P_i^H
=
P(Y_i=1\mid X_H).
$$

其中 $X_H$ 可包含：

- 過往競賽；
- 距離；
- 場地；
- 負磅；
- 檔位；
- 騎師；
- 練馬師；
- 速度；
- 步速；
- 調教；
- 健康；
- 馬齡；
- 休息時間；
- 場地適性；
- 其他可公開取得的賽事狀態。

這是一般人最容易把「AI 賽馬」等同起來的那一層。

但它只是三分之一。

---

# 10. Crowd Model

第二個模型估計其他投注者會怎麼做：

$$
M_C:
X_C
\rightarrow
\hat B_i(T).
$$

也就是預測：

$$
\boxed{
\text{How much money will eventually choose each outcome?}
}
$$

這裡的輸入可以不是馬匹本身，而是：

- 當前 odds；
- 熱門程度；
- 媒體敘事；
- 賽事級別；
- 明星騎師；
- 公眾偏好；
- 大額資金動態；
- 不同時間帶的投注流。

---

# 11. Pool Dynamics Model

第三個模型不是預測馬，也不是預測人本身。

它預測：

$$
(Q_t,B_{1,t},\ldots,B_{n,t})
\rightarrow
(Q_T,B_{1,T},\ldots,B_{n,T}).
$$

因此得到：

$$
\hat D_i(T).
$$

也就是：

$$
\boxed{
\text{What will the final price actually be?}
}
$$

---

# 12. 所以現在看到的 Value 不等於最終 Value

假設在時間 $t$：

$$
P_i^H=0.16,
$$

$$
D_i(t)=8.
$$

則：

$$
EV_i(t)
=
0.16\times8-1
=
0.28.
$$

但若 Crowd Model 與 Pool Model 預測最後：

$$
D_i(T)=5.5,
$$

則：

$$
EV_i(T)
=
0.16\times5.5-1
=-0.12.
$$

所以：

$$
\boxed{
\text{visible value now}
\neq
\text{realized value at pool close}.
}
$$

---

# 13. 共同彩池因此是一個雙重預測問題

固定賠率市場主要是：

$$
\hat P(Y)
\quad\text{vs}\quad
O(t).
$$

共同彩池則是：

$$
\boxed{
\hat P(Y)
\quad+
\hat O(T).
}
$$

第一個預測錯，事件模型失敗。

第二個預測錯，價格模型失敗。

兩者任一失敗都可能讓原本看到的 edge 消失。

---

# 14. 市場不是噪音，而是一個 Sensor

共同彩池中，市場價格包含其他參與者的資訊。

有些資訊可能不在自己的資料裡：

$$
X_H^{\mathrm{private}}
\not\subset
X_H^{\mathrm{AI}}.
$$

但若知道資訊的人下注，他的知識可能被投影成：

$$
\Delta B_i.
$$

於是：

$$
\boxed{
\text{private information}
\rightarrow
\text{capital flow}
\rightarrow
\text{odds movement}.
}
$$

這就是為什麼市場價格本身可以變成 AI 的輸入。

---

# 15. William Benter 的歷史意義

William Benter 1994 年的經典報告研究電腦化賽馬 handicap 與 wagering system，作者單位即標示為香港 Betting Syndicate。

其重要之處不是單純建立一個馬匹模型。

Benter 描述了一種 logit-based 方法，把：

$$
P_F
=
\text{fundamental model probability}
$$

與：

$$
P_P
=
\text{public implied probability}
$$

進行結合。

並報告該電腦化系統在五年實際運行中取得顯著正向結果。這是早期最經典的「模型不排斥市場，而是把市場本身當資訊」案例之一。

---

# 16. Benter 模型揭露的核心原則

如果自己的模型已經知道全部資訊，市場應該沒有額外價值。

但實際上：

$$
I(P_P;Y\mid P_F)>0
$$

可能成立。

也就是在已知 fundamental model 後，公眾價格仍包含額外訊息。

因此：

$$
\boxed{
\text{Market disagreement}
\neq
\text{Market ignorance}.
}
$$

有時候市場知道自己不知道的東西。

---

# 17. 最好的馬不等於最好的投注標的

假設：

$$
P_A=0.40,
$$

$$
P_B=0.15.
$$

A 明顯比較可能獲勝。

但如果市場給出的最終回報使：

$$
P_AD_A<1,
$$

而：

$$
P_BD_B>1,
$$

那麼：

$$
\boxed{
\text{best horse}
\neq
\text{best-priced horse}.
}
$$

這是所有賽馬量化模型最基本但最容易被一般「AI 猜馬」敘事忽略的差別。

---

# 18. 日本 JRA：共同彩池的制度基礎

JRA 現行規則顯示，不同投注方式具有不同設定払戻率。

目前官方列出的比例如下：

$$
R_{\mathrm{Win}}=80\%,
$$

$$
R_{\mathrm{Place}}=80\%,
$$

$$
R_{\mathrm{Bracket/Quinella/Wide}}=77.5\%,
$$

$$
R_{\mathrm{Exacta/Trio}}=75\%,
$$

$$
R_{\mathrm{Trifecta}}=72.5\%,
$$

$$
R_{\mathrm{WIN5}}=70\%.
$$

這些派彩率意味著研究任何長期期望值時，都不能只問模型是否比隨機準，而必須跨過制度性 takeout。

---

# 19. 日本的第一個特徵：AI 工具逐步民主化

截至 2026 年，JRA-VAN Data Lab 公開強調其資料服務可使用約四十年的 JRA 官方競馬資料，包含即時 odds 與賽前馬體重等資訊。

這意味一般研究者不需要自己從零建立數十年的基礎資料庫。

資料基礎設施本身已經形成：

$$
\boxed{
\text{official data}
\rightarrow
\text{consumer software ecosystem}.
}
$$

---

# 20. 2026 年的「競馬 AI 予想メーカー」是一個象徵性事件

JRA-VAN Data Lab 在 2026 年 8 月 30 日更新的第三方軟體「競馬AI予想メーカー」可以從 JV-Link 匯入中央競馬資料，選擇特徵，使用 LightGBM 訓練，輸出勝率、複勝率相關指標，並提供 holdout evaluation 與自有資料匯入功能。

需要精確區分：這是 JRA-VAN Data Lab 生態中提供的第三方軟體，不等於 JRA 官方宣稱某一 AI 模型可以獲利。

但它證明一件事：

$$
\boxed{
\text{building an ML horse model has become a consumer-level activity}.
}
$$

---

# 21. 日本模式可以稱為 AI Democratization

日本目前公開可觀察的路徑更接近：

$$
\text{official data}
$$

$$
\downarrow
$$

$$
\text{software ecosystem}
$$

$$
\downarrow
$$

$$
\text{ordinary users build models}.
$$

所以：

$$
\boxed{
\text{Japan}
\approx
\text{AI handicapping democratization}.
}
$$

---

# 22. 民主化同時會侵蝕簡單 Edge

如果只有少數人會利用：

$$
X
$$

則：

$$
I_{\mathrm{private}}(X;Y)
$$

具有更高私人價值。

當所有人都有：

$$
X
+
\text{LightGBM}
+
\text{historical database},
$$

則：

$$
\boxed{
\text{easy model edge}
\rightarrow
\text{market information}.
}
$$

因此工具普及不必然讓所有使用者更容易獲利。

---

# 23. 日本 AI 最終真正需要超越的是「其他 AI」

當越來越多玩家具有：

- 同樣官方資料；
- 類似 ML；
- 類似 odds；
- 類似歷史特徵；

則：

$$
P_A^H
\approx
P_B^H.
$$

因此真正差異逐漸轉向：

$$
\boxed{
\text{unique feature}
+
\text{better validation}
+
\text{better crowd model}
+
\text{better pool model}.
}
$$

---

# 24. 日本公開生態與美國 CAW 的差異

目前公開資訊足以確認日本具有高度成熟的資料分析與 AI 預測工具生態。

但沒有必要因此直接推論：

$$
\text{Japan CAW structure}
=
\text{U.S. CAW structure}.
$$

美國的特殊之處是「高速、大量、自動化投注」已成為具有明確產業名稱與制度回應的市場階層。

---

# 25. 美國：CAW 已經是一種正式市場角色

Computer Assisted Wagering 通常指使用電腦模型與高速基礎設施進行大規模賽馬投注的活動。

2026 年 NYRA 在新規則中甚至直接用執行速度界定 CAW：

$$
\boxed{
\text{execution speed}>6\text{ bets per second}
}
$$

即被 NYRA 視為 CAW activity。

這表示問題已經不只是：

> 使用者是否使用 AI？

而是：

$$
\boxed{
\text{technology has created a distinct market participant class}.
}
$$

---

# 26. CAW 更接近 Quant Trading

一個抽象 CAW 系統可以表示為：

$$
\text{historical racing data}
$$

$$
+
\text{probability models}
$$

$$
+
\text{live pool data}
$$

$$
+
\text{price modelling}
$$

$$
+
\text{high-speed execution}.
$$

所以它跟一般人「看馬經選馬」是完全不同的操作尺度。

---

# 27. CAW 的優勢不只是預測準確度

可以寫成：

$$
\mathcal E_{CAW}
=
E_M+E_D+E_T+E_C,
$$

其中：

$$
E_M=\text{model advantage},
$$

$$
E_D=\text{data advantage},
$$

$$
E_T=\text{timing/execution advantage},
$$

$$
E_C=\text{cost/rebate advantage}.
$$

因此即使普通玩家擁有相同的事件模型，也不代表擁有相同的市場能力。

---

# 28. Rebate 會改變 Effective Takeout

共同彩池表面上的：

$$
\tau
$$

不一定是每個玩家真正承擔的：

$$
\tau_{\mathrm{eff}}.
$$

如果某類玩家具有 rebate：

$$
r>0,
$$

則可以概念化為：

$$
\tau_{\mathrm{eff}}
<
\tau.
$$

因此：

$$
\boxed{
\text{same model}
+
\text{different cost structure}
=
\text{different economic edge}.
}
$$

---

# 29. 美國爭議的核心是 Market Microstructure

很多一般玩家真正不滿的不是：

> 電腦比我聰明。

而是：

> 我在下注時看到的價格，與最終派彩價格之間可能因最後資金大量湧入而劇烈不同。

這是：

$$
\boxed{\text{late odds volatility}}.
$$

---

# 30. Santa Anita 的公開數據

2025 年公開的 Santa Anita 資料顯示，2024 年 7 月 1 日至 2025 年 6 月 30 日期間，CAW 約占該場整體 pool 金額的接近：

$$
23\%.
$$

而每場最後 60 秒進入的投注中，平均約：

$$
30\%
$$

來自 CAW。

但同一份公開討論也指出，其餘約：

$$
70\%
$$

的最後一分鐘資金並非 CAW。

所以：

$$
\boxed{
\text{late odds movement}
\neq
\text{CAW only}.
}
$$

這是一個重要的制度分析細節。

---

# 31. 不能把所有價格波動都歸罪於 AI

即使：

$$
CAW=0,
$$

一般玩家也可能集中在最後下注。

而 tote system 處理跨平台投注亦可能使畫面 odds 更新落後於實際資金進入。

因此需要區分：

$$
\text{CAW effect},
$$

$$
\text{late retail flow},
$$

$$
\text{display/update latency}.
$$

否則容易把多種市場微觀結構問題錯誤壓縮成一個「AI 問題」。

---

# 32. NYRA 2026 年直接修改市場規則

NYRA 於 2026 年 1 月 30 日宣布，自 2 月 5 日開始，在此前未受高速投注限制的所有 wagering pools 中：

$$
\boxed{
\text{CAW must cease at one minute to post}.
}
$$

而 Win Pool 原先已有更早的高頻投注限制。

這是本系列非常重要的案例，因為：

$$
\boxed{
\text{AI/algorithmic edge}
\rightarrow
\text{market rule adaptation}.
}
$$

Paper 00 的制度反身性在此具體發生。

---

# 33. 這不是禁止分析，而是限制 Execution Topology

NYRA 並不是說：

> 不准使用統計學。

而是改變：

$$
\text{when certain high-speed participants may enter the pool}.
$$

所以制度反制不一定針對：

$$
M_H.
$$

可能直接針對：

$$
\boxed{T=\text{timing/execution advantage}}.
$$

---

# 34. 美國因此形成 Technology-Class Regulation

傳統市場規則通常區分：

- bet type；
- minimum stake；
- race；
- account。

CAW 時代開始多了一個新的分類軸：

$$
\boxed{\text{execution technology class}}.
$$

這與高頻金融市場中對 speed、access、market structure 的治理問題具有明顯相似性。

---

# 35. 香港：電腦化賽馬不是 2026 年才開始

香港最特殊的地方是：

$$
\boxed{
\text{computerized horse-race modelling has decades of history}.
}
$$

Benter 的 1994 年報告已經描述一個香港投注 syndicate 的實戰系統。

因此香港不是「生成式 AI 突然進入賽馬」。

更接近：

$$
\text{computer handicapping}
\rightarrow
\text{quantitative syndicates}
\rightarrow
\text{high-speed pool technology}
\rightarrow
\text{modern ML/AI}.
$$

---

# 36. 香港模型的歷史重要性在於 World Model + Market Model

Benter 的核心方法不是排斥公眾 odds。

而是承認：

$$
P_{\mathrm{public}}
$$

具有自己的 predictive content。

這其實就是現代：

$$
\boxed{
\text{Own Model}
+
\text{Market as Sensor}.
}
$$

---

# 37. 香港本地彩池的制度成本

HKJC 現行 Horse Racing Betting Guide 顯示，本地 pari-mutuel pool 的派彩比率依玩法不同。

例如：

$$
R_{\mathrm{Win/Place/Quinella/QP/Double}}=82.5\%,
$$

$$
R_{\mathrm{Forecast}}=80.5\%,
$$

$$
R_{\mathrm{Trio}}=77\%,
$$

$$
R_{\mathrm{Tierce/First4/Quartet/Treble}}=75\%.
$$

所以基本制度摩擦大致已經落在：

$$
17.5\%\text{ to }25\%
$$

這個量級，視玩法而不同。

---

# 38. 香港的 Rebate 又讓不同玩家的成本不同

HKJC 現行規則亦規定，指定 Win、Place、Quinella、Quinella Place losing bet，如果單張票或 betline 的總虧損投注額達：

$$
HK\$10,000
$$

或以上，可以符合 rebate 條件。

本地賽事目前列出的 rebate 包括：

$$
10\%
$$

的 Win / Place losing bet rebate，以及：

$$
12\%
$$

的 Quinella / Quinella Place rebate。

因此：

$$
\boxed{
C_{\mathrm{retail}}
\neq
C_{\mathrm{high-volume}}.
}
$$

---

# 39. 這讓 Hong Kong Quant Ecology 產生成本分層

兩個模型如果完全相同：

$$
M_A=M_B,
$$

但：

$$
C_A<C_B,
$$

則：

$$
\mathcal E_A>\mathcal E_B
$$

可能成立。

所以量化競爭不是只有：

$$
\text{who predicts better}.
$$

還包括：

$$
\boxed{
\text{who operates under better effective economics}.
}
$$

---

# 40. 香港市場本身也高度技術化

HKJC 官方表示，它在 2014 年成為全球第一個把原本為高速證券交易開發的 advanced odds calculation technology 用於 horse-race pool betting products 的賽馬機構。

目前約：

$$
90\%
$$

的 HKJC wagering 已透過 online 與 mobile channels 完成，並由大量資料分析支援。

因此香港不能簡化成：

$$
\text{AI bettor vs old-fashioned tote}.
$$

更準確是：

$$
\boxed{
\text{quant participants}
\leftrightarrow
\text{high-speed pari-mutuel infrastructure}.
}
$$

---

# 41. 香港現在還是一個全球化彩池

HKJC 公布，2025/26 racing season 的總 wagering turnover 為：

$$
HK\$143.31\text{ billion}.
$$

香港賽事吸引的 commingling turnover 則創紀錄達：

$$
HK\$34.4\text{ billion}.
$$

當季有：

$$
26
$$

個國家／司法管轄區與超過：

$$
60
$$

個合作夥伴參與 commingling。

World Pool 賽事數也從上一季的：

$$
296
$$

增加到：

$$
397.
$$

這已經是一個跨國共同流動性市場。

---

# 42. World Pool 把「其他玩家」擴張成全球其他玩家

原本 Crowd Model 可能只要研究：

$$
\text{Hong Kong bettors}.
$$

全球 commingling 後變成：

$$
\boxed{
\text{multi-jurisdictional crowd}.
}
$$

不同國家的：

- 媒體；
- 賽馬文化；
- 偏好；
- 本地明星；
- 模型；
- 資金量；

都可能進入同一 pool。

---

# 43. 深流動性對 AI 同時是好事與壞事

總池：

$$
Q\uparrow
$$

時，同樣的投注：

$$
q
$$

造成的相對價格衝擊：

$$
\frac{q}{Q}
$$

下降。

所以大型資金更容易執行。

但同時：

$$
\text{informed capital}\uparrow.
$$

因此：

$$
\boxed{
\text{capacity}
\uparrow
\quad\text{while}\quad
\text{easy mispricing}
\downarrow
}
$$

可能同時成立。

---

# 44. Liquidity Paradox

本文稱此為：

$$
\boxed{\text{Pari-Mutuel Liquidity Paradox}}.
$$

即：

$$
Liquidity\uparrow
$$

使：

$$
PriceImpact\downarrow,
$$

但也可能使：

$$
MarketEfficiency\uparrow.
$$

因此深流動性既增加可執行容量，也提高找到錯價的難度。

---

# 45. 香港的有限馬群特性對 World Model 有利

HKJC 2026 年資料指出，香港約有：

$$
1,300
$$

匹在訓馬匹。

相對有限而高度重複出賽的馬匹、騎師、練馬師與主要場地，使香港賽馬具有一種相對封閉的 longitudinal observation environment。

因此：

$$
\boxed{
\text{same entities are repeatedly observed over time}.
}
$$

這對時序 world modelling 非常有利。

---

# 46. 但「更容易建模」不等於「更容易獲利」

如果所有 sophisticated participants 都能長期觀察同一批馬：

$$
DataQuality\uparrow,
$$

則自己的模型更好。

但市場模型也更好：

$$
P_M\rightarrow P^*.
$$

所以：

$$
\boxed{
\text{modelability}
\neq
\text{exploitability}.
}
$$

---

# 47. 日本、美國、香港是三種不同的 AI 賽馬 regime

本文暫時將其概念化為：

$$
\boxed{
\text{Japan}
=
\text{AI Democratization}
}
$$

$$
\boxed{
\text{United States}
=
\text{CAW Industrialization}
}
$$

$$
\boxed{
\text{Hong Kong}
=
\text{Mature Quant Ecosystem}
}
$$

這不是說各國只有一種類型，而是描述公開資料中最突出的制度特徵。

---

# 48. Japan：主要矛盾是 Tool Diffusion

日本的主要問題逐漸變成：

$$
\boxed{
\text{如果人人都有資料與 ML，什麼仍然構成私人資訊優勢？}
}
$$

因此 edge 可能從一般歷史統計轉向：

- 更好的特徵；
- 更好的狀態估計；
- 更好的模型校準；
- 更好的市場流預測。

---

# 49. United States：主要矛盾是 Technology Asymmetry

美國 CAW 爭議更接近：

$$
\boxed{
\text{different participants have different execution technology and effective cost}.
}
$$

所以治理焦點開始落在：

- speed；
- access；
- cutoff；
- rebates；
- CAW-free pools；
- late odds volatility。

---

# 50. Hong Kong：主要矛盾是 Mature Efficiency

香港則更像：

$$
\boxed{
\text{how much edge remains in a market that has been quantitatively modelled for decades?}
}
$$

市場大、資料多、技術成熟、流動性全球化。

這讓香港同時成為：

$$
\boxed{
\text{excellent AI laboratory}
}
$$

與：

$$
\boxed{
\text{extremely difficult benchmark market}.
}
$$

---

# 51. AI 賽馬最終是 Multi-Agent System

設：

$$
A_1,\ldots,A_n
$$

為不同投注者。

每個投注者都有：

$$
P_i^H,
$$

$$
C_i,
$$

$$
q_i,
$$

$$
\pi_i.
$$

所有人的行動共同形成：

$$
B(T).
$$

再由：

$$
B(T)
$$

決定所有人的最終價格。

所以：

$$
\boxed{
\text{each agent changes the payoff landscape of every other agent}.
}
$$

---

# 52. 這是真正的 Endogenous Price Game

固定賠率中，玩家通常把：

$$
O
$$

視為外生價格。

pari-mutuel 中：

$$
O=F(q_1,q_2,\ldots,q_n).
$$

因此：

$$
\boxed{
\text{price is an endogenous state variable}.
}
$$

---

# 53. 最終 odds 本身具有不確定性

賽前某時間 $t$：

$$
O_i(t)
$$

已知。

但：

$$
O_i(T)
$$

未知。

所以它本身具有：

$$
P(O_i(T)\mid\mathcal I_t).
$$

即：

$$
\boxed{
\text{odds uncertainty}.
}
$$

這在 fixed-odds 市場成交後通常大幅降低，但在 pari-mutuel 市場直到關池前都不能完全忽略。

---

# 54. AI 應該預測 Odds Distribution，而不是單一 Odds

與 Paper 02 的 meta-uncertainty 一致，更合理的是：

$$
O_i(T)
\sim
\mathcal D_i.
$$

而不是只說：

$$
\hat O_i(T)=5.7.
$$

因為：

$$
Var(O_i(T))
$$

本身會改變決策可靠度。

---

# 55. Crowd Model 也不是「大眾心理學」而已

在成熟市場中：

$$
Crowd
=
\text{retail}
+
\text{professional}
+
\text{syndicate}
+
\text{algorithmic capital}.
$$

所以：

$$
\boxed{
\text{crowd intelligence}
\neq
\text{average casual bettor intelligence}.
}
$$

尤其美國與香港，市場中可能包含非常 sophisticated 的模型資金。

---

# 56. Smart Money 不是神諭

即使大型資金下注：

$$
B_i\uparrow,
$$

也不能直接推出：

$$
P_i\uparrow.
$$

因為大型資金也可能：

- 錯；
- hedge；
- 受 rebate 影響；
- 跨 pool 組合；
- 以不同目標函數行動。

所以：

$$
\boxed{
\text{money flow is evidence, not truth}.
}
$$

---

# 57. Market as Sensor 需要 Calibration

設：

$$
s_i
$$

為 pool share。

研究者應測：

$$
P(Y_i=1\mid s_i\in[a,b]).
$$

是否與 market-implied probability 一致。

也就是：

$$
\boxed{
\text{pool calibration}.
}
$$

這跟 Paper 02 的 sportsbook calibration 是同一理論，只是價格生成機制不同。

---

# 58. Favourite–Longshot Bias 仍可能存在

共同彩池並不保證完美市場效率。

如果一般投注者偏好：

$$
\text{high payout / low probability outcomes},
$$

可能形成：

$$
P_M(\text{longshot})
>
P^*(\text{longshot}).
$$

所以：

$$
\boxed{
\text{pari-mutuel}
\neq
\text{perfectly efficient}.
}
$$

Benter 歷史成果本身就曾被解讀為賽馬共同彩池存在可利用 inefficiency 的證據。

---

# 59. 但 Edge 是歷史條件下的 Edge

1990 年代香港存在的：

$$
\mathcal E_{1994}>0
$$

不推出：

$$
\mathcal E_{2026}>0.
$$

因為：

$$
\text{data access},
$$

$$
\text{compute},
$$

$$
\text{ML adoption},
$$

$$
\text{pool size},
$$

$$
\text{market participants}
$$

全部已經改變。

這是所有歷史「成功賽馬系統」研究必須保留的時間條件。

---

# 60. Edge Decay 在 Pari-Mutuel 中具有直接價格機制

Paper 00 提出：

$$
\frac{\partial\mathcal E_{\mathrm{private}}}{\partial A}<0
$$

作為一個條件性命題。

在共同彩池中，這甚至可以有直接機制：

若更多使用者判斷同一結果被低估：

$$
A\uparrow
$$

導致：

$$
B_i\uparrow
$$

再導致：

$$
D_i\downarrow.
$$

所以：

$$
\boxed{
\text{discovered edge}
\rightarrow
\text{capital flow}
\rightarrow
\text{price correction}.
}
$$

---

# 61. 這是最乾淨的 AI Self-Consumption 案例之一

在某些領域，AI 普及如何消滅 edge 很抽象。

但 pari-mutuel 中可以直接看到：

$$
\text{same signal adopted by more capital}
$$

$$
\downarrow
$$

$$
\text{same horse receives more pool share}
$$

$$
\downarrow
$$

$$
\text{dividend declines}.
$$

因此：

$$
\boxed{
\text{the act of exploiting information reveals and prices the information}.
}
$$

---

# 62. 賽馬市場因此也是 Information Aggregation Machine

很多投注者各自擁有：

$$
X_1,X_2,\ldots,X_n.
$$

各自產生：

$$
a_1,a_2,\ldots,a_n.
$$

最後形成：

$$
B.
$$

所以：

$$
\boxed{
\{X_i\}_{i=1}^{n}
\rightarrow
\{a_i\}_{i=1}^{n}
\rightarrow
B
\rightarrow
O.
}
$$

Odds 是一種壓縮後的 distributed belief state。

---

# 63. 但市場壓縮會丟失資訊

不同原因可能產生相同下注：

$$
a_i=a_j
$$

但：

$$
X_i\neq X_j.
$$

因此只看：

$$
B_i
$$

無法重建所有人的 reasoning。

這表示：

$$
\boxed{
\text{odds are an information-rich but lossy projection}.
}
$$

---

# 64. AI 的優勢可能來自「解碼市場」而不是「忽略市場」

未來更強的 horse-racing AI 不一定追求：

$$
P_H
$$

完全脫離 odds。

反而可能研究：

$$
\boxed{
P(Y\mid X_H,O_t,\Delta O_t,Q_t).
}
$$

也就是：

$$
\text{horse state}
+
\text{market state}.
$$

這正是 Benter 歷史方法在現代 AI 下最值得延伸的理論方向。

---

# 65. 但使用市場資料會產生 Circularity Risk

如果模型全部依賴：

$$
O_t,
$$

它可能只是複製市場：

$$
P_{AI}\approx P_M.
$$

因此應測：

$$
L(P_{AI},Y)
$$

相對：

$$
L(P_M,Y).
$$

真正重要的是：

$$
\boxed{
\Delta L
=
L(P_M,Y)-L(P_{AI},Y).
}
$$

而不是模型單獨看起來很準。

---

# 66. Horse Model 與 Price Model 應分離驗證

本文建議至少分開驗證：

$$
V_H
=
\text{horse-outcome calibration},
$$

與：

$$
V_P
=
\text{final-pool forecast accuracy}.
$$

否則一個最終回報失敗時無法知道：

- 馬匹概率錯；
- 群眾預測錯；
- 彩池價格預測錯。

---

# 67. 一個科學研究甚至不需要真正下注

如果目的是研究 AI 是否具有資訊優勢，可以保存：

$$
P_i^H(t),
$$

$$
O_i(t),
$$

$$
O_i(T),
$$

$$
Y_i.
$$

然後事後測：

$$
Calibration(P_i^H),
$$

$$
Error(\hat O_i(T)),
$$

以及：

$$
P_i^H
\quad\text{vs}\quad
P_M.
$$

因此研究市場效率不需要把模型變成實際投注工具。

---

# 68. 這符合本系列的 No-MVP 邊界

本文不需要：

$$
\text{bet execution API},
$$

$$
\text{high-speed order engine},
$$

$$
\text{CAW automation}.
$$

因為理論命題可以透過：

$$
\boxed{
\text{observation}
+
\text{timestamped prediction}
+
\text{final market data}
}
$$

驗證。

---

# 69. 科學研究應該保存 Point-in-Time Pool Data

如果研究者只保存最後 odds：

$$
O(T),
$$

就無法重建：

$$
O(t).
$$

因此也無法研究：

$$
\text{information absorption},
$$

$$
\text{late money},
$$

$$
\text{edge half-life}.
$$

所以嚴格研究需要時間序列：

$$
\{O(t_k),Q(t_k),B_i(t_k)\}_{k=1}^{m}.
$$

---

# 70. 但資料 timestamp 本身必須可信

共同彩池資料有：

- display update time；
- source ingestion time；
- pool accounting time；
- race start time。

因此：

$$
\boxed{
\text{screen timestamp}
\neq
\text{necessarily economic event timestamp}.
}
$$

這正是研究美國 late odds movement 時特別需要注意的問題。

---

# 71. 研究 CAW 不能只看 Winning Percentage

CAW 可能具有：

$$
P_{\mathrm{win}}
$$

優勢，也可能主要依靠：

$$
\text{pricing}
+
\text{rebate}
+
\text{volume}.
$$

所以：

$$
\boxed{
\text{CAW success}
\neq
\text{superhuman horse prediction alone}.
}
$$

---

# 72. 這是 AI 博弈研究很重要的去神話化

當一個量化團隊長期成功，人們容易說：

> AI 太會預測馬了。

但完整因果可能是：

$$
\text{good model}
+
\text{market model}
+
\text{cost advantage}
+
\text{execution}
+
\text{capital discipline}.
$$

所以必須避免把整個系統能力歸因給單一 AI 模型。

---

# 73. 反過來，Retail Player 也不只是「比較笨」

一般玩家可能承擔：

$$
C_R>C_Q,
$$

執行速度：

$$
T_R>T_Q,
$$

可觀察資料：

$$
X_R\subset X_Q.
$$

因此結果差異可以源自整個制度與技術位置，而不是純粹認知能力。

---

# 74. 公平問題因此不是單純「是否允許 AI」

真正治理問題可能是：

$$
\boxed{
\text{what asymmetries are acceptable in a common pool?}
}
$$

例如：

- 更好的模型是否可接受？
- 更快的執行是否可接受？
- 特殊 rebate 是否可接受？
- 專用接口是否可接受？
- 最後幾秒大量下注是否可接受？

NYRA 的政策代表其選擇限制其中一部分 execution asymmetry，而不是全面禁止量化分析。

---

# 75. Market Fairness 與 Market Efficiency 甚至可能衝突

CAW 資金可能：

$$
Liquidity\uparrow,
$$

$$
PriceEfficiency\uparrow.
$$

但一般玩家可能感受到：

$$
PredictabilityOfFinalPrice\downarrow,
$$

或：

$$
EffectiveReturn\downarrow.
$$

因此：

$$
\boxed{
\text{more efficient market}
\not\Rightarrow
\text{better perceived market fairness}.
}
$$

---

# 76. 這是 AI 市場治理的一個普適問題

同樣問題也會出現在：

- high-frequency finance；
- ad auctions；
- prediction markets；
- online marketplaces；
- ticket markets。

只要：

$$
\text{shared market}
+
\text{asymmetric automation}
$$

存在，就會出現：

$$
\boxed{
\text{efficiency vs access fairness}.
}
$$

賽馬只是非常早就顯現出這個問題。

---

# 77. 本文提出 Pari-Mutuel AI Edge Equation

可以把 AI 在共同彩池中的淨資訊優勢概念化為：

$$
\boxed{
\mathcal E_{PM}
=
E_H
+
E_C
+
E_P
+
E_T
+
E_{Cost}
-
C_{takeout}
-
C_{impact}
-
C_{uncertainty}.
}
$$

其中：

$$
E_H=\text{horse model edge},
$$

$$
E_C=\text{crowd model edge},
$$

$$
E_P=\text{pool model edge},
$$

$$
E_T=\text{timing advantage},
$$

$$
E_{Cost}=\text{relative cost advantage}.
$$

---

# 78. 第一核心命題：Horse–Price Separation

即使：

$$
P_i>P_j,
$$

仍不推出：

$$
EV_i>EV_j.
$$

因此：

$$
\boxed{
\text{ranking horses by win probability}
\neq
\text{ranking market value}.
}
$$

---

# 79. 第二核心命題：Pool Endogeneity

在共同彩池中：

$$
\boxed{
O_i(T)
=
F(B_1(T),\ldots,B_n(T)).
}
$$

所以最終價格由參與者行動內生生成，而非固定外部參數。

---

# 80. 第三核心命題：Self-Impact

對單一結果追加資金 $q$，在簡化模型下：

$$
\boxed{
\frac{\partial D_i(q)}{\partial q}<0.
}
$$

因此：

$$
\boxed{
\text{an exploitable edge has finite capacity}.
}
$$

---

# 81. 第四核心命題：Market-as-Sensor

若群體中存在未被 AI world model 直接觀測的資訊，而該資訊透過投注反映：

$$
I(O_t;Y\mid X_H)>0
$$

可能成立。

因此：

$$
\boxed{
\text{odds can contain residual predictive information}.
}
$$

Benter 的歷史模型提供了經典實戰案例。

---

# 82. 第五核心命題：Liquidity Paradox

當：

$$
Q\uparrow,
$$

通常：

$$
C_{impact}\downarrow.
$$

但若流動性增加同時引入更多 informed capital：

$$
MarketEfficiency\uparrow.
$$

所以：

$$
\boxed{
\text{more capacity can coexist with less alpha}.
}
$$

---

# 83. 第六核心命題：Technology-Class Reflexivity

當某類技術參與者造成足夠大的市場外部性：

$$
Externality_{tech}>\theta,
$$

制度可能從：

$$
R_t
$$

轉成：

$$
R_{t+1}.
$$

NYRA 的 2026 CAW cutoff 是此命題的具體案例。

---

# 84. 第七核心命題：Democratization–Efficiency Coupling

當官方資料與 ML 工具普及：

$$
A_{AI}\uparrow,
$$

普通玩家的分析能力可能：

$$
M_{retail}\uparrow.
$$

但同時：

$$
MarketEfficiency\uparrow.
$$

所以：

$$
\boxed{
\text{democratized intelligence does not guarantee democratized alpha}.
}
$$

日本 JRA-VAN 生態提供了非常好的研究場景。

---

# 85. 第八核心命題：Mature-Market Difficulty

一個市場越具有：

$$
\text{long history}
+
\text{good data}
+
\text{deep liquidity}
+
\text{sophisticated participants},
$$

它可能同時越適合訓練 AI，卻越難取得持續私人超額優勢。

即：

$$
\boxed{
Trainability\uparrow
\not\Rightarrow
Exploitability\uparrow.
}
$$

香港是這個命題最典型的候選市場之一。

---

# 86. 三地比較

| 面向 | 日本 JRA | 美國 | 香港 HKJC |
|---|---|---|---|
| 核心博彩結構 | Pari-mutuel | Pari-mutuel 為主 | Pari-mutuel 為主 |
| 公開 AI 特徵 | 官方資料生態與民用 ML 工具 | CAW 高速量化投注 | 長期量化 syndicate 歷史 |
| 主要制度議題 | AI/分析工具普及 | CAW speed、rebate、late odds | 全球流動性、成熟定價、成本分層 |
| 2026 代表現象 | JRA-VAN 列出 LightGBM AI 工具 | NYRA 一分鐘 CAW cutoff | HK\$143.31b 年度 turnover、397 World Pool races |
| 理論類型 | AI Democratization | CAW Industrialization | Mature Quant Ecosystem |

這張表是概念分類，不代表三個市場內部沒有其他類型的參與者。

---

# 87. AI 賽馬不是「比賽預測」而是市場預測

最簡單的 AI horse model：

$$
X_H
\rightarrow
P(Y).
$$

真正的 pari-mutuel model：

$$
(X_H,X_C,Q_t,B_t)
$$

$$
\downarrow
$$

$$
(P(Y),P(O_T),U).
$$

因此：

$$
\boxed{
\text{race prediction}
\subset
\text{pari-mutuel intelligence}.
}
$$

---

# 88. 更完整的是四層系統

本文將 Paper 03 最終架構整理為：

$$
\boxed{
\begin{array}{c}
\text{Layer 1: Horse State}\\
\downarrow\\
\text{Layer 2: Human/AI Belief}\\
\downarrow\\
\text{Layer 3: Capital Flow}\\
\downarrow\\
\text{Layer 4: Pool Price}
\end{array}
}
$$

最後才得到：

$$
\text{Realized Dividend}.
$$

---

# 89. 每一層都有自己的不確定性

Horse State：

$$
U_H.
$$

Crowd Behaviour：

$$
U_C.
$$

Pool Closing State：

$$
U_P.
$$

所以整體不是：

$$
U=U_H.
$$

而是：

$$
\boxed{
U_{total}
=
f(U_H,U_C,U_P).
}
$$

這解釋為什麼「很準的賽馬預測模型」仍可能無法穩定預測最終市場價值。

---

# 90. AI 普及後甚至可能形成 Model Ecology

不同 agent 可能專門研究：

$$
M_H,
$$

另一些研究：

$$
M_C,
$$

另一些研究：

$$
M_P.
$$

最後所有模型透過資金互相作用。

因此市場本身變成：

$$
\boxed{
\text{AI model ecology coupled through capital}.
}
$$

---

# 91. 這比「AI vs 人類」更準確

2026 年真正成熟市場中的問題已經不是：

$$
AI
\quad\text{vs}\quad
Human.
$$

更接近：

$$
\boxed{
(Human+AI)_1
\quad\text{vs}\quad
(Human+AI)_2
\quad\text{vs}\quad
\cdots
}
$$

並共同產生：

$$
O(T).
$$

---

# 92. 賽馬因此是 AI 適應性市場研究的天然實驗室

它同時具有：

- 明確事件終局；
- 高頻重複比賽；
- 公開歷史資料；
- 明確價格；
- 可觀察市場變化；
- 真實資金；
- 人類與算法共同參與。

所以可以觀察：

$$
\boxed{
\text{information}
\rightarrow
\text{belief}
\rightarrow
\text{capital}
\rightarrow
\text{price}
\rightarrow
\text{truth}.
}
$$

這在很多其他市場反而沒這麼乾淨。

---

# 93. 但這也是為什麼研究要特別避免濫用

研究：

$$
\text{market efficiency}
$$

與：

$$
\text{AI information aggregation}
$$

並不要求建立：

$$
\text{automatic wagering system}.
$$

而 CAW 已經證明自動化一旦進入高速度、高資本層級，問題會立即從模型研究變成市場公平與制度治理。

---

# 94. 本系列在 Paper 03 的實作邊界

本文不提供：

$$
\boxed{
\text{CAW implementation}
}
$$

$$
\boxed{
\text{automatic pool execution}
}
$$

$$
\boxed{
\text{real-time wager sizing}
}
$$

$$
\boxed{
\text{rebate exploitation workflow}
}
$$

$$
\boxed{
\text{high-speed betting infrastructure}
}
$$

研究僅限於制度、數學、歷史、公開資料與市場行為。

---

# 95. 與 Paper 02 的關係

Paper 02 問：

$$
\boxed{
\text{Does AI know more than the sportsbook price?}
}
$$

Paper 03 則問：

$$
\boxed{
\text{What if the price itself is created by all bettors, including the AI?}
}
$$

這讓市場問題從：

$$
\text{AI vs Price}
$$

升級為：

$$
\boxed{
\text{AI participates in producing Price}.
}
$$

---

# 96. 從 Market Boundary 到 Collective Intelligence Boundary

Paper 01：

$$
\text{Is there signal?}
$$

Paper 02：

$$
\text{Does the market already know it?}
$$

Paper 03：

$$
\boxed{
\text{How does everyone knowing and acting on it create the price?}
}
$$

因此第三篇正式跨入：

$$
\boxed{\text{Collective Intelligence}}.
$$

---

# 97. AI Pari-Mutuel 三重門

可以把本篇壓縮成三個 Gate。

第一：

$$
G_H:
P_H\text{ 是否優於基準？}
$$

第二：

$$
G_C:
\text{是否能理解群眾與其他模型的資金流？}
$$

第三：

$$
G_P:
\text{是否能正確描述最終 pool price dynamics？}
$$

若任一失敗：

$$
\mathcal E_{PM}
$$

都可能消失。

---

# 98. 最終統一式

本篇最終提出：

$$
\boxed{
\mathcal E_{PM}(t,q)
=
F(
P_H,
P_C,
P_P,
\tau,
r,
q,
Q,
U,
R
)
}
$$

其中：

$$
P_H=\text{horse probability quality},
$$

$$
P_C=\text{crowd prediction quality},
$$

$$
P_P=\text{pool-price prediction quality},
$$

$$
\tau=\text{takeout},
$$

$$
r=\text{rebate/cost structure},
$$

$$
q=\text{participant capital entering the outcome},
$$

$$
Q=\text{pool liquidity},
$$

$$
U=\text{model and price uncertainty},
$$

$$
R=\text{rules and market response}.
$$

這比單純：

$$
P(\text{horse wins})
$$

多了整整一個市場世界。

---

# 99. 結論

人工智慧進入賽馬後，最初看起來只是：

> 用更多資料預測哪匹馬會贏。

但共同彩池制度揭露，真正問題遠比這複雜。

一匹馬的真實勝率只是：

$$
P_H.
$$

市場上還有：

$$
P_C,
$$

也就是其他人的信念與行為；以及：

$$
P_P,
$$

也就是資金進入後形成的最終 pool state。

因此：

$$
\boxed{
\text{Horse Racing AI}
\neq
\text{Horse Prediction AI}.
}
$$

更準確的形式是：

$$
\boxed{
\text{Horse Racing AI}
=
\text{World Model}
+
\text{Crowd Model}
+
\text{Pool Model}.
}
$$

日本顯示，當官方資料與 ML 工具普及後，AI handicap 正逐漸民主化；但工具普及本身也會使簡單訊號更快被價格吸收。

美國則顯示，當模型再加上高速執行、大量資本與差異化成本後，AI/算法投注可以形成獨立的市場技術階層。2026 年 NYRA 對 CAW 的一分鐘 cutoff 表明，市場制度已經開始直接為算法執行重新畫邊界。

香港則顯示，這不是一個突然出現的新故事。從 Benter 1994 年的電腦化模型，到 HKJC 將高速證券交易技術導入 odds calculation，再到 2025/26 年超過：

$$
HK\$143\text{ billion}
$$

的年度 racing turnover 與全球 commingling，賽馬早已演化成高度資料化與量化的群體市場。

因此，本篇最重要的結論不是：

> AI 能不能猜中馬？

而是：

$$
\boxed{
\text{當大量 AI 同時預測同一匹馬，並把自己的信念轉化為資金時，
那些 AI 的行動本身就成為市場價格的一部分。}
}
$$

於是 AI 不再只是外部觀察市場。

它開始：

$$
\boxed{
\text{observe the market}
\rightarrow
\text{act on the market}
\rightarrow
\text{change the market}
\rightarrow
\text{observe the changed market again}.
}
$$

這正是適應性市場。

也因此，賽馬提供了一個極其乾淨的 AI 博弈命題：

$$
\boxed{
\text{Intelligence does not merely predict price; collective intelligence produces price.}
}
$$

而當 AI 能力繼續普及時，真正值得研究的也許不是「AI 是否會讓所有人更會賭」，而是：

$$
\boxed{
\text{一個由人類與 AI 共同形成價格的市場，
最後會收斂成什麼樣的資訊均衡？}
}
$$

這將直接銜接後續 Paper 04：當 AI 不只預測一匹已存在的馬，而開始介入配種、遺傳、育成、拍賣與馬主選擇時，博弈問題將從「如何評價生命」進一步進入「如何參與生命週期決策」。

---

## References / Empirical Anchors

1. Japan Racing Association (JRA), current horse-betting payout rules and configured payout ratios for Win, Place, Quinella, Exacta, Trio, Trifecta and WIN5.
2. JRA-VAN Data Lab, 2026 service information describing approximately forty years of JRA official racing data and its racing-software ecosystem.
3. JRA-VAN Data Lab, *競馬AI予想メーカー*, updated 2026-08-30, describing LightGBM training, JV-Link ingestion, feature selection, holdout evaluation and custom-data support.
4. William Benter, *Computer Based Horse Race Handicapping and Wagering Systems: A Report*, reporting a fundamental/public-odds combination method and significant positive results over five years of actual implementation.
5. New York Racing Association (NYRA), 2026 CAW guardrail policy defining CAW by execution speed above six bets per second and imposing a one-minute-to-post cutoff in previously unrestricted pools.
6. Equibase / BloodHorse reporting on Santa Anita CAW market share and last-60-second wagering composition during 2024-2025.
7. Hong Kong Jockey Club, current Horse Racing Betting Guide, including pari-mutuel payout percentages and high-value losing-bet rebate rules.
8. Hong Kong Jockey Club, *World-Class Technology*, describing the 2014 adoption of advanced odds calculation technology originally developed for high-speed securities trading and current online/mobile wagering share.
9. Hong Kong Jockey Club, 2025/26 season results, reporting HK $143.31 billion total racing wagering turnover, HK$ 34.4 billion record commingling turnover on Hong Kong races, participation from 26 countries/jurisdictions and more than 60 partners, and expansion to 397 World Pool races.

---

**Next:**  
**Paper 04 — 從賽馬預測到生命週期智能：AI、遺傳學、配種、育成、拍賣與馬主效用**
