# AI 的隨機性邊界：彩券、RNG、輪盤、假模式與不可預測性的數學框架

## The Randomness Boundary of Artificial Intelligence: Lotteries, RNGs, Roulette, False Patterns, and the Mathematics of Unpredictability

**Series:** AI Game Intelligence, Randomness, and Adaptive Markets  
**Paper 01**  
**Version:** v0.1  
**Date:** 2026-09-01
**Author:** Neo.K with Aletheia（GPT-5.6 Sol）  
**Institution:** EveMissLab／一言諾科技有限公司

---

## 摘要

人工智慧擅長從大量資料中尋找模式，因此一個直觀問題是：如果把足夠長的彩券、輪盤、老虎機或其他隨機遊戲歷史資料交給 AI，它是否終究可以找到人類無法察覺的規律？

這個問題的答案取決於「規律是否真的存在於資料生成機制中」，而不是模型本身有多大。

本文提出 AI 隨機性邊界框架，正式區分：

$$
\text{Pattern}
$$

$$
\text{Statistical Dependence}
$$

$$
\text{Predictability}
$$

$$
\text{Exploitability}.
$$

四者並不等價。

若未來結果 $Y_{t+1}$ 與可觀測歷史 $H_t$ 相互獨立：

$$
P(Y_{t+1}\mid H_t)=P(Y_{t+1}),
$$

則：

$$
I(Y_{t+1};H_t)=0.
$$

此時增加模型參數、資料量或模型種類，不能憑空創造真實 predictive information。大型語言模型、Transformer、LSTM、強化學習、圖神經網路與 ensemble 皆受此資訊論限制。

然而，現實中的彩券與賭場系統不是抽象數學理想物。實體球組、開獎機、亂數熵源、seed、軟體實作、部署錯誤、設備老化與制度變更都有可能造成生成機制偏離理想模型。

因此 AI 在真正隨機系統中的合理角色，不是「從不存在的訊號中預測下一期」，而是：

$$
\boxed{
\text{Randomness Auditor}
}
$$

亦即檢查資料是否符合宣稱的生成機制、偵測 regime shift、異常、不均勻、序列依賴與系統缺陷。

本文進一步分析熱號與冷號謬誤、multiple testing、data snooping、look-ahead bias、模型選擇偏差以及「AI 預測成功」最容易產生的統計錯覺，並提出一套從 IID 假設、資訊測量到 out-of-sample falsification 的研究框架。

---

# 1. AI 為什麼特別容易讓人誤以為「隨機中有規律」

現代 AI 的核心能力之一就是：

$$
\text{High-dimensional pattern extraction}.
$$

如果給模型：

$$
D=
\{x_1,x_2,\ldots,x_N\},
$$

模型幾乎總能找到某個函數：

$$
f_\theta(D)
$$

使訓練資料上的誤差下降。

問題是：

$$
\boxed{
\text{A model can fit a pattern even when the generating process contains no useful pattern.}
}
$$

這不是 AI 的特殊缺陷。

而是統計學與機器學習的基本事實。

假設資料：

$$
X_t\overset{iid}{\sim}U(0,1).
$$

即使是真正獨立均勻亂數，只要樣本有限，仍然必然出現：

- 長連續；
- 重複；
- 聚集；
- 空窗；
- 特定數字短期過多；
- 特定數字短期過少；
- 奇怪的局部週期。

這不是系統失去隨機性。

恰恰相反：

$$
\boxed{
\text{真正的隨機序列本來就會產生看起來不像隨機的局部結構。}
}
$$

AI 因為比人類更強於搜尋模式，反而更容易在巨大 hypothesis space 中找到偶然關聯。

所以：

$$
\text{AI pattern discovery}
$$

與：

$$
\text{true signal discovery}
$$

必須嚴格區分。

---

# 2. 四個不能混為一談的概念

本文提出四層區分。

## 2.1 Pattern

只代表資料中存在某種可描述結構。

例如：

$$
7,7,7,7
$$

本身就是一個 pattern。

但它完全可以由公平亂數產生。

---

## 2.2 Statistical Dependence

若：

$$
P(Y\mid X)\neq P(Y),
$$

則 $X$ 與 $Y$ 存在統計依賴。

這比單純 pattern 更強。

---

## 2.3 Predictability

即使存在統計依賴，仍要問模型是否能在未見資料中利用它：

$$
L_{\text{test}}(f)
<
L_{\text{baseline}}.
$$

只有 out-of-sample 改善才具有預測意義。

---

## 2.4 Exploitability

即使預測能力存在：

$$
\Delta L>0,
$$

也不代表具有經濟價值。

還需要：

$$
EV_{\text{net}}>0.
$$

因此：

$$
\boxed{
\text{Pattern}
\not\Rightarrow
\text{Dependence}
\not\Rightarrow
\text{Predictability}
\not\Rightarrow
\text{Profitability}.
}
$$

這是整篇最重要的邏輯鏈之一。

---

# 3. 理想 IID 系統

考慮一個結果序列：

$$
X_1,X_2,\ldots,X_t.
$$

若每一次結果：

$$
X_t\sim P_X
$$

且：

$$
X_i\perp X_j
\quad
\forall i\neq j,
$$

則稱為 independent and identically distributed：

$$
X_t\overset{iid}{\sim}P_X.
$$

此時對全部歷史：

$$
H_t=(X_1,\ldots,X_t),
$$

有：

$$
P(X_{t+1}\mid H_t)
=
P(X_{t+1}).
$$

因此：

$$
H(X_{t+1}\mid H_t)
=
H(X_{t+1}).
$$

也就是：

$$
I(X_{t+1};H_t)=0.
$$

這表示歷史資料對下一次結果沒有 predictive information。

因此對任何僅使用 $H_t$ 的 AI：

$$
f_\theta(H_t),
$$

理想情況下都存在：

$$
\boxed{
E[L(f_\theta)]
\geq
L_{\text{Bayes baseline}}.
}
$$

模型再大，也不能突破 Bayes-optimal limit。

---

# 4. 彩券：所有組合都「一樣不特別」

以公平 $6/49$ 彩券為例。

所有六號組合數：

$$
|\Omega|
=
\binom{49}{6}
=
13,983,816.
$$

任一特定組合：

$$
S\in\Omega
$$

都有：

$$
P(S)
=
\frac{1}{13,983,816}.
$$

因此：

$$
P(
\{1,2,3,4,5,6\}
)
$$

和：

$$
P(
\{7,16,22,31,42,49\}
)
$$

完全相同。

即使第一組在人類眼裡「太不像亂數」：

$$
P(S_1)=P(S_2).
$$

這揭露一個很典型的認知錯覺：

$$
\boxed{
\text{Random-looking}
\neq
\text{more probable}.
}
$$

---

# 5. 熱號不會因為熱而更熱

設某數字 $i$ 在前 $n$ 期出現：

$$
k_i
$$

次。

觀察頻率：

$$
\hat p_i
=
\frac{k_i}{n}.
$$

如果真實生成過程均勻：

$$
p_i=p,
$$

則：

$$
\hat p_i\neq p
$$

在有限樣本中完全正常。

根據大數法則：

$$
\hat p_i
\xrightarrow{a.s.}
p.
$$

但這不代表短期一定接近。

所以：

> 「7 最近出了很多次，所以還會繼續熱。」

以及：

> 「7 已經很久沒出，所以快輪到它。」

在真正 IID 系統下都沒有根據。

因為：

$$
P(X_{t+1}=7\mid H_t)
=
P(X_{t+1}=7).
$$

第一種通常對應：

$$
\text{Hot-hand fallacy},
$$

第二種則對應：

$$
\text{Gambler's fallacy}.
$$

兩者方向相反，但共同錯誤是：

$$
\boxed{
\text{把歷史頻率波動誤解成未來概率改變。}
}
$$

---

# 6. 「很久沒出現」到底意味著什麼？

假設某事件單次概率：

$$
P(A)=p.
$$

連續 $n$ 次沒有發生：

$$
P(\text{no }A\text{ for }n)
=
(1-p)^n.
$$

當這個事件已經發生之後，再問下一次：

$$
P(A_{n+1}\mid A_1^c,\ldots,A_n^c)=p.
$$

並不因為：

$$
n\uparrow
$$

而增加。

因此：

$$
\boxed{
\text{Unusual past sequence}
\not\Rightarrow
\text{changed future probability}.
}
$$

---

# 7. 為什麼 AI 會找到「超強熱號模型」？

因為 AI 的搜尋空間太大。

假設研究者測試：

$$
m=100,000
$$

個模型。

每一個模型在純 noise 上，都有：

$$
\alpha=0.05
$$

概率因偶然而達到傳統 $p<0.05$。

期望中的假陽性數：

$$
E[FP]=m\alpha.
$$

所以：

$$
E[FP]
=
100,000\times0.05
=
5,000.
$$

也就是：

> 即使完全不存在訊號，你仍然預期找到五千個「顯著模型」。

這就是：

$$
\boxed{\text{Multiple Testing Problem}.}
$$

---

# 8. AI 讓 Multiple Testing 更嚴重

傳統研究者可能人工測：

$$
10
$$

種特徵。

現代 AutoML / Agent 可以自動測：

$$
10^5
$$

甚至：

$$
10^7
$$

種組合：

- window size；
- number frequency；
- parity；
- sum；
- spacing；
- Fourier transform；
- Markov order；
- embedding；
- Transformer depth；
- random seeds；
- feature subset；
- target encoding；
- loss function。

因此：

$$
|\mathcal H|\uparrow
$$

時，

$$
P(
\exists h\in\mathcal H:
\text{looks predictive by chance}
)
\uparrow.
$$

極端情況下：

$$
\lim_{|\mathcal H|\to\infty}
P(\text{find apparent pattern})
=
1.
$$

因此：

$$
\boxed{
\text{More AI search}
\not\Rightarrow
\text{more truth}.
}
$$

沒有嚴格驗證時，甚至可能：

$$
\text{More AI search}
\Rightarrow
\text{more convincing false discoveries}.
$$

---

# 9. Lottery AI 最常見的第一種錯誤：In-Sample Validation

假設模型在：

$$
D_{\text{train}}
$$

中找到：

$$
Accuracy=75\%.
$$

完全沒有意義，除非：

$$
D_{\text{test}}
\cap
D_{\text{train}}
=
\varnothing.
$$

而且測試集必須：

$$
\boxed{
\text{在模型設計完成之前就保持不可見。}
}
$$

如果研究者：

1. 看 test；
2. 改模型；
3. 再看 test；
4. 再改模型；

那麼 test set 已經成為：

$$
D_{\text{training by feedback}}.
$$

真正需要新的：

$$
D_{\text{untouched}}.
$$

---

# 10. 時序資料尤其不能隨機打散

彩券或市場資料是：

$$
X_1,X_2,\ldots,X_T.
$$

若把所有資料隨機 shuffle 後切：

$$
80\%/20\%,
$$

可能造成未來資料影響過去模型。

正確的 temporal validation 應更接近：

$$
\text{Train: }1,\ldots,t
$$

$$
\text{Test: }t+1,\ldots,t+k.
$$

然後：

$$
t\rightarrow t+k.
$$

形成：

$$
\boxed{
\text{Walk-forward validation}.
}
$$

即：

$$
D_1\rightarrow T_1
$$

$$
D_{1:2}\rightarrow T_2
$$

$$
D_{1:3}\rightarrow T_3
$$

反覆執行。

這才能模擬真實情況：

$$
\boxed{
\text{只能使用當時已知資料預測當時未知未來。}
}
$$

---

# 11. Lottery AI 第二種錯誤：Data Leakage

假設資料列中有：

- draw number；
- jackpot；
- winners；
- payout；
- rollover status；
- sales volume。

其中某些欄位只有**開獎之後**才知道。

如果模型把它們當 feature：

$$
X_t
$$

來預測當期結果：

$$
Y_t,
$$

就形成：

$$
Y_t\rightarrow X_t.
$$

模型看似神準，其實：

$$
\boxed{
\text{future leaked into input}.
}
$$

同樣錯誤也可能更隱蔽：

- normalization 使用全資料；
- feature selection 使用全資料；
- target encoding 使用 test；
- hyperparameter tuning 重複查看 test；
- 欄位本身含日期後資訊。

因此：

$$
\boxed{
\text{No temporal leakage}
}
$$

是所有 AI 彩券研究的最低要求。

---

# 12. Lottery AI 第三種錯誤：選模型本身也是 overfitting

假設訓練：

$$
M_1,M_2,\ldots,M_K.
$$

然後選：

$$
M^*
=
\arg\max_i Performance(M_i).
$$

即使每個模型真實能力都相同，

$$
M^*
$$

的觀察績效仍會因 selection bias 被高估。

可抽象為：

$$
\hat\mu_i
=
\mu_i+\epsilon_i.
$$

選擇：

$$
i^*
=
\arg\max_i \hat\mu_i.
$$

通常：

$$
E[\hat\mu_{i^*}]
>
E[\mu_{i^*}].
$$

這叫：

$$
\boxed{
\text{Winner's Curse in Model Selection}.
}
$$

AutoML 時代尤其重要。

---

# 13. 「AI 比隨機好」到底怎麼驗證？

不能只拿一次 random baseline。

因為 random baseline 自己也有 variance。

應建立：

$$
B_1,B_2,\ldots,B_N
$$

個隨機策略。

得到：

$$
\mu_B
=
E[Score(B)]
$$

以及：

$$
\sigma_B.
$$

AI 分數：

$$
S_A.
$$

研究的不是：

$$
S_A>\mu_B,
$$

而是：

$$
z=
\frac{S_A-\mu_B}{\sigma_B}.
$$

或者更直接進行：

- permutation test；
- bootstrap；
- exact test；
- Monte Carlo null distribution。

真正要回答：

$$
P(
Score\geq S_A
\mid H_0
).
$$

---

# 14. 顯著不等於有用

假設資料量：

$$
N=10^8.
$$

AI 模型比 baseline 多：

$$
0.0001\%
$$

準確率。

由於 $N$ 非常大，可能：

$$
p<10^{-10}.
$$

統計上高度顯著。

但：

$$
\Delta EV
\approx0.
$$

所以還必須區分：

$$
\boxed{
\text{Statistical significance}
\neq
\text{Practical significance}.
}
$$

---

# 15. 統計檢驗也不能「證明隨機」

這一點非常重要。

如果執行某個 randomness test：

$$
H_0=\text{random}.
$$

得到：

$$
p>0.05,
$$

正確說法是：

$$
\boxed{
\text{未能拒絕 }H_0.
}
$$

不是：

$$
\boxed{
\text{已證明序列是隨機。}
}
$$

因為：

- test power 有限；
- 樣本有限；
- 只測特定偏差；
- 未測的結構仍可能存在。

一個序列可以通過：

$$
T_1,T_2,\ldots,T_{100}
$$

仍然存在第 101 種可利用結構。

---

# 16. Statistical Randomness 與 Computational Unpredictability 不同

這是 RNG 問題非常重要的一層。

考慮一個 deterministic PRNG：

$$
X_{t+1}
=
F(X_t).
$$

只要初始 seed：

$$
s
$$

固定，整條序列其實：

$$
X_1,X_2,\ldots
$$

都是確定的。

因此在本體論上：

$$
H(X_{t+1}\mid s)=0.
$$

但如果攻擊者不知道 $s$，且逆推出 seed 在計算上不可行：

$$
C_{\text{recover seed}}
\gg
C_{\text{available}},
$$

則系統仍可以是：

$$
\boxed{
\text{computationally unpredictable}.
}
$$

這就是現代 cryptographic RNG 的基本思想。

---

# 17. NIST 的 RNG 框架也不是「跑一個亂數測試就完成」

截至 2026 年，NIST SP 800-90 系列已把 random bit generation 分成不同層次。

SP 800-90B 處理 entropy source 的設計與驗證，包括 noise source、min-entropy、health testing 與 predictor resistance。2025 年正式發布的 SP 800-90C 則進一步定義如何把 entropy source 與 deterministic random bit generator 組合成完整 RBG construction。

這種設計思想很重要：

$$
\text{Randomness assurance}
\neq
\text{one statistical test}.
$$

而是：

$$
\boxed{
\text{Entropy Source}
+
\text{Generator Design}
+
\text{Implementation}
+
\text{Health Testing}
+
\text{Operational Controls}.
}
$$

---

# 18. 這也解釋為什麼「歷史結果看起來正常」仍然不夠

假設某 RNG：

$$
X_t
$$

在一億次樣本中：

- 頻率均勻；
- serial correlation 很低；
- runs test 正常。

但如果 seed 生成方式是：

$$
s=\text{Unix timestamp},
$$

且攻擊者知道大致啟動時間，

搜尋空間可能只有：

$$
10^4
$$

或：

$$
10^6.
$$

序列仍然可能被預測。

所以：

$$
\boxed{
\text{Statistically random-looking}
\neq
\text{securely unpredictable}.
}
$$

反過來：

某些安全 PRNG 在短樣本裡也可能偶然出現看似偏差。

因此不能從一小段輸出反推整個機制。

---

# 19. 合規博彩 RNG 的目標本來就是讓 AI 沒東西可預測

英國 Gambling Commission RTS 7 明確要求遊戲與虛擬事件的 RNG 達到「acceptably random」，包括輸出符合預期分布、結果不可預測、seed / reseed 不引入可預測性，以及禁止在遊戲過程中根據玩家過去結果動態調整勝率的 compensated/adaptive behaviour。

所以在這類合法合規系統中：

$$
\boxed{
\text{AI cannot predict the RNG}
}
$$

並不是 AI 很弱。

反而可能表示：

$$
\boxed{
\text{the RNG is doing its job}.
}
$$

---

# 20. 世界彩票業本身也把問題當「系統完整性」而不是「歷史號碼神秘學」

WLA-SCS:2024 對電子開獎與 chance-based digital games 的要求，不只關注輸出，而包含：

- RNG entropy source；
- drawing algorithm；
- physical/logical protection；
- independent randomness verification；
- post-deployment testing；
- segregation of duties；
- 防止未授權修改。



因此真正專業的問題是：

$$
\boxed{
\text{Can the generating system be trusted?}
}
$$

而不是：

> 「43 號是不是最近特別熱？」

這是兩種完全不同的研究文化。

---

# 21. 但是現實中的機械彩球不是抽象 IID 神諭

這裡必須小心。

實體彩球系統可以寫成：

$$
Y_t
=
F(
M_t,
B_t,
E_t,
O_t,
\epsilon_t
),
$$

其中：

$$
M_t=\text{machine state},
$$

$$
B_t=\text{ball-set state},
$$

$$
E_t=\text{environment},
$$

$$
O_t=\text{operation/procedure}.
$$

理想狀態希望：

$$
P(Y\mid M,B,E,O)
\approx
U(\Omega).
$$

但實體世界可能存在：

- 重量微差；
- 尺寸微差；
- 表面磨損；
- 機器老化；
- 氣流；
- 溫濕度；
- 操作程序；
- replacement ball；
- equipment rotation。

因此：

$$
\boxed{
\text{Assumed IID}
\neq
\text{guaranteed IID}.
}
$$

---

# 22. 這時 AI 的正確角色改變了

不應該先問：

$$
\hat Y_{t+1}=?
$$

而應該問：

$$
H_0:
P(Y\mid Z)=P(Y)
$$

其中：

$$
Z=(M,B,E,O).
$$

對立假設：

$$
H_1:
P(Y\mid Z)\neq P(Y).
$$

如果存在：

$$
I(Y;Z)>0,
$$

才表示生成系統可能存在 state-dependent structure。

這種研究叫：

$$
\boxed{
\text{System Identification}
}
$$

或：

$$
\boxed{
\text{Randomness Auditing}.
}
$$

而不是「AI 算號碼」。

---

# 23. Regime Shift 是另一個重要問題

即使系統在：

$$
t<t^*
$$

完全符合：

$$
P_0,
$$

在：

$$
t\geq t^*
$$

也可能因設備、軟體或制度改變成：

$$
P_1.
$$

即：

$$
P_t=
\begin{cases}
P_0,& t<t^*\\
P_1,& t\geq t^*
\end{cases}
$$

這叫：

$$
\boxed{
\text{Regime Change}.
}
$$

AI 很適合做：

- change-point detection；
- drift detection；
- sequential hypothesis testing；
- anomaly detection。

這和下一期預測不同。

AI 可能無法說：

> 下一個一定是 24。

但可以說：

> 從 2026-04-17 起，這台設備的輸出分布和歷史顯著不同。

這是非常有價值的監管能力。

---

# 24. 隨機系統中的「異常」也必須避免過度解讀

假設 $N=49$ 個號碼。

總共檢查：

$$
49
$$

個 frequency test。

如果每個都使用：

$$
\alpha=0.05,
$$

即使全部公平：

$$
P(\text{至少一個 false alarm})
=
1-(1-\alpha)^{49}.
$$

計算得：

$$
1-0.95^{49}
\approx0.919.
$$

也就是約：

$$
91.9\%.
$$

所以如果有人說：

> 「49 個號碼裡竟然有一個達到 $p<0.05$！一定有問題！」

這其實非常可能只是 multiple testing。

---

# 25. Family-Wise Error 與 False Discovery Rate

對 $m$ 次測試，一種簡單校正是 Bonferroni：

$$
\alpha'
=
\frac{\alpha}{m}.
$$

如果：

$$
\alpha=0.05,
$$

$$
m=49,
$$

則：

$$
\alpha'
\approx0.00102.
$$

另一類方法控制：

$$
\text{False Discovery Rate}.
$$

例如 Benjamini-Hochberg。

AI 自動 anomaly discovery 特別需要這一層，否則模型會把正常波動報告成：

$$
\text{hundreds of suspicious patterns}.
$$

---

# 26. Base Rate Problem

假設合法彩票真正有重大設備異常的概率：

$$
P(A)=0.001.
$$

某 AI detector：

$$
Sensitivity=0.99,
$$

$$
Specificity=0.99.
$$

看起來極強。

但：

$$
P(A\mid+)
$$

不一定高。

由 Bayes：

$$
P(A\mid+)
=
\frac{
P(+\mid A)P(A)
}{
P(+\mid A)P(A)
+
P(+\mid A^c)P(A^c)
}.
$$

代入：

$$
=
\frac{
0.99(0.001)
}{
0.99(0.001)
+
0.01(0.999)
}
$$

約為：

$$
9\%.
$$

也就是：

> 即使 detector 有 99% sensitivity 和 99% specificity，報警後真正有異常的概率仍可能只有約 9%。

這是因為：

$$
\boxed{
\text{重大異常本來就非常稀有。}
}
$$

所以 AI audit 不能只追求 classifier accuracy。

---

# 27. AI Randomness Auditor 應該輸出的是「證據層級」

例如：

### Level 0

$$
\text{No detectable deviation}.
$$

只代表：

> 目前測試未找到偏離。

不是證明完美隨機。

---

### Level 1

$$
\text{Statistical anomaly}.
$$

存在異常，但可能是偶然。

---

### Level 2

$$
\text{Replicated anomaly}.
$$

在獨立時間／設備／資料中重複。

---

### Level 3

$$
\text{Mechanism-linked anomaly}.
$$

異常和某個：

$$
M_i
$$

或：

$$
B_j
$$

具有穩定關係。

---

### Level 4

$$
\text{Predictive anomaly}.
$$

可以事前預測 out-of-sample deviation。

---

### Level 5

$$
\text{Causal/mechanistic confirmation}.
$$

已找到可重現生成原因。

因此：

$$
\boxed{
\text{Anomaly}
\neq
\text{Bias}
\neq
\text{Prediction}
\neq
\text{Cause}.
}
$$

---

# 28. 一個真正可信的 Lottery AI 實驗應該怎麼設計？

首先預先固定：

$$
H
$$

假設。

例如：

$$
H_0:
P(Y=i)=\frac{1}{N}.
$$

再固定：

- 資料期間；
- feature set；
- algorithm family；
- hyperparameter policy；
- evaluation metric；
- stopping rule；
- multiple-test correction。

最後：

$$
\boxed{
\text{freeze protocol before seeing future outcomes}.
}
$$

然後才進入 prospective test。

---

# 29. Prospective Prediction 比歷史 Backtest 更有說服力

假設研究者說：

> 我的模型用 20 年歷史資料回測，可以中 65%。

首先很難知道：

- 模型試過幾百次？
- 是否挑最好版本？
- 是否偷偷調參？
- 是否看過所有結果？

更好的設計是：

在：

$$
t_0
$$

公開 freeze 模型：

$$
M^*.
$$

之後完全不改。

預測：

$$
t_0+1,\ldots,t_0+N.
$$

再評估。

即：

$$
\boxed{
\text{Precommit}
\rightarrow
\text{Predict}
\rightarrow
\text{Observe}
\rightarrow
\text{Evaluate}.
}
$$

這對「AI 預測彩券」尤其重要。

---

# 30. 如果 AI 真有 edge，應該出現什麼？

假設真實存在：

$$
\epsilon>0
$$

的可利用 advantage。

則隨 $N$ 增加：

$$
\hat\epsilon_N
\rightarrow
\epsilon.
$$

信賴區間：

$$
CI_N
$$

應該逐漸縮小，並持續排除：

$$
0.
$$

如果模型結果是：

第一年：

$$
+15\%
$$

第二年：

$$
+3\%
$$

第三年：

$$
-4\%
$$

第四年：

$$
+2\%,
$$

而總體：

$$
CI\ni0,
$$

更合理解釋通常是：

$$
\boxed{
\text{noise}.
}
$$

---

# 31. AI 的模型越複雜，證據標準反而應該越高

設模型 complexity：

$$
C(M).
$$

若：

$$
C(M)\uparrow,
$$

則 fitting capacity：

$$
\mathcal F(M)\uparrow.
$$

因此找到偶然模式的能力也上升。

所以：

$$
\boxed{
\text{More complex claims require stronger out-of-sample evidence}.
}
$$

這可以視為 AI randomness research 的一種 epistemic regularization。

---

# 32. Deep Learning 並不違反資訊論

常見錯誤：

> Transformer 能找到人類看不到的模式，所以 IID 對它可能不成立。

這把：

$$
\text{observer capability}
$$

和：

$$
\text{statistical dependence}
$$

混為一談。

如果：

$$
I(H_t;X_{t+1})=0,
$$

那麼任何 deterministic representation：

$$
Z=f(H_t)
$$

由 data processing inequality：

$$
I(Z;X_{t+1})
\leq
I(H_t;X_{t+1})
=
0.
$$

因此：

$$
I(Z;X_{t+1})=0.
$$

這是一個非常強的結果。

即：

$$
\boxed{
\text{AI 不能透過 representation learning 從零互資訊創造正互資訊。}
}
$$

---

# 33. 這是 AI 隨機性邊界最乾淨的數學形式

如果：

$$
Y\perp X,
$$

則對：

$$
Z=f_\theta(X),
$$

仍然：

$$
Y\perp Z.
$$

也就是：

$$
\boxed{
\text{No model can manufacture predictive information absent from its inputs.}
}
$$

模型可以：

- 壓縮；
- 組合；
- 投影；
- 發現隱藏結構。

但前提是：

$$
\boxed{
\text{那個結構本來就在資料中。}
}
$$

---

# 34. 那量子亂數呢？

如果結果由真正量子測量產生，在標準量子力學描述下，單次結果本身具有不可約概率性。

例如：

$$
|\psi\rangle
=
\alpha|0\rangle+\beta|1\rangle.
$$

測量：

$$
P(0)=|\alpha|^2,
$$

$$
P(1)=|\beta|^2.
$$

即使 AI 完整知道：

$$
|\psi\rangle,
$$

仍然只能得到概率分布。

不能得到單次確定結果。

因此：

$$
\boxed{
\text{Perfect model of probability}
\neq
\text{perfect prediction of realization}.
}
$$

這也是「認識概率」與「預言事件」的根本差別。

---

# 35. 物理輪盤是不是也完全不可預測？

這裡又不同。

輪盤在抽象博彩數學中可視為：

$$
X\sim P.
$$

但實體輪盤實際上是一個 classical dynamical system。

如果完整知道：

- 球初速；
- 轉盤角速度；
- 摩擦；
- 幾何；
- deceleration；
- launch position；

則原則上：

$$
Y=F(S_0,\theta,\epsilon).
$$

所以它不像量子測量那樣必然具有 fundamental randomness。

但現實問題是：

$$
\delta S_0
$$

的極小測量誤差可能快速放大。

加上賭場規則與裝置限制，因此：

$$
\boxed{
\text{physically structured}
\neq
\text{practically exploitable}.
}
$$

這一部分將在 Paper 05 詳細處理。

---

# 36. 所以 Randomness 應該分層

本文建議至少區分：

## R0 — Epistemic randomness

只是觀察者不知道。

---

## R1 — Statistical randomness

輸出在統計上符合指定隨機模型。

---

## R2 — Computational unpredictability

即使機制 deterministic，也因計算限制難以預測。

---

## R3 — Dynamical unpredictability

系統對初始條件高度敏感，實務無法取得足夠精度。

---

## R4 — Fundamental stochasticity

理論本身只提供概率分布，而無更完整可存取的決定資訊。

因此：

$$
\boxed{
\text{random}
}
$$

其實不是單一概念。

---

# 37. 不同 randomness level 對 AI 的意義不同

若是：

$$
R0,
$$

AI 可能因為知道更多而大幅改善。

若是：

$$
R1,
$$

AI 主要能進行 statistical audit。

若是：

$$
R2,
$$

AI 是否能突破取決於 computational resources 與漏洞。

若是：

$$
R3,
$$

AI 可能改善 state estimation，但仍受 sensitivity limit。

若是：

$$
R4,
$$

AI 最終只能估：

$$
P(Y),
$$

而無法消除單次 realization uncertainty。

---

# 38. 這也解釋了為什麼「AI 會不會預測」不能一概而論

例如：

### 彩券

理想：

$$
R1/R2.
$$

AI prediction edge：

$$
\approx0.
$$

---

### Blackjack shoe

存在 state dependence。

因此：

$$
R0.
$$

更多資訊真的有價值。

---

### 足球

大量 epistemic uncertainty：

$$
R0+R3.
$$

所以 AI 可以有效降低不確定性。

---

### Poker

除了不確定性還存在：

$$
\text{strategic agent}.
$$

因此已超越單純 randomness problem。

---

# 39. AI 真正應該回答「不知道」的情況

未來 AI 系統不應把所有 prediction request 都當成：

$$
\arg\max_yP(y\mid x).
$$

還需要判斷：

$$
\boxed{
\text{Does }x\text{ actually contain information about }y?
}
$$

也就是先估計：

$$
I(X;Y).
$$

如果：

$$
I(X;Y)\approx0,
$$

合理輸出應是：

> 沒有證據顯示可觀測資訊能提高下一次結果的預測能力。

而不是製造：

> 根據最近 30 期，我推薦 7、18、29……

因此 AI 本身需要：

$$
\boxed{
\text{Predictability Gate}.
}
$$

---

# 40. Predictability Gate

我們可以定義：

$$
G_P
=
g(
I,
OOS,
S,
R
),
$$

其中：

$$
I=\text{estimated information},
$$

$$
OOS=\text{out-of-sample performance},
$$

$$
S=\text{statistical strength},
$$

$$
R=\text{replication evidence}.
$$

只有：

$$
G_P>\tau
$$

才允許模型宣稱：

$$
\text{predictive structure detected}.
$$

否則：

$$
\boxed{
\text{No demonstrated predictive edge}.
}
$$

---

# 41. 這比「AI 不會預測彩券」更科學

過去 AI 常直接說：

> 彩票是隨機的，所以不能預測。

這在實務上安全，但科學上太粗糙。

因為真正正確的說法應是：

$$
\boxed{
\text{若生成機制符合公平獨立隨機模型，
則歷史結果本身不提供下一次結果的 predictive information。}
}
$$

但仍然可以研究：

$$
\boxed{
\text{生成機制是否真的符合該模型。}
}
$$

這兩個命題完全可以同時成立。

---

# 42. AI 在真正隨機系統裡仍然非常有用

其用途包括：

### Randomness Audit

$$
P_{\text{observed}}
\overset{?}{=}
P_{\text{expected}}.
$$

### Drift Detection

$$
P_t
\overset{?}{=}
P_{t-k}.
$$

### Hardware Correlation

$$
I(Y;M_i)>0?
$$

### Ball-set Correlation

$$
I(Y;B_j)>0?
$$

### RNG Health Monitoring

檢查 entropy degradation。

### Fraud Detection

檢查不自然序列或操作異常。

### Integrity Verification

把：

$$
\text{draw process}
$$

與：

$$
\text{audit trail}
$$

對齊。

這些用途對監管者甚至比「猜下一期」重要得多。

---

# 43. AI 在這裡應該從 Predictor 轉成 Scientist

Predictor 問：

> 下一次是多少？

Scientist 問：

> 生成這些結果的模型是什麼？

更正式地：

$$
\boxed{
\text{Prediction}
:
H_t\rightarrow X_{t+1}
}
$$

而：

$$
\boxed{
\text{Scientific inference}
:
D\rightarrow\mathcal M.
}
$$

其中：

$$
\mathcal M
$$

是可能的生成機制。

在真正隨機系統裡，後者可能遠比前者有價值。

---

# 44. 一個 AI 看到異常後不應直接跳到「可以賺」

正確推理鏈：

$$
\text{Anomaly detected}
$$

$$
\downarrow
$$

$$
\text{Rule out multiple testing}
$$

$$
\downarrow
$$

$$
\text{Independent replication}
$$

$$
\downarrow
$$

$$
\text{Out-of-sample prediction}
$$

$$
\downarrow
$$

$$
\text{Mechanism correlation}
$$

$$
\downarrow
$$

$$
\text{Causal investigation}.
$$

而不是：

$$
\text{Anomaly}
\rightarrow
\text{bet}.
$$

這條研究邊界也是本系列不進行博彩 exploit engineering 的原因之一。

---

# 45. 隨機系統研究最值得防的是「幻覺式科學」

AI 可以非常容易生成：

> 近期尾數 7 出現密度提高 22%，顯示週期轉折。

句子非常像研究。

甚至可以附：

- 圖；
- Fourier spectrum；
- neural attention；
- correlation matrix。

但如果沒有：

$$
H_0,
$$

$$
OOS,
$$

$$
multiple-testing correction,
$$

$$
replication,
$$

那麼：

$$
\boxed{
\text{mathematical-looking explanation}
\neq
\text{scientific evidence}.
}
$$

這是生成式 AI 時代非常重要的新問題。

---

# 46. AI 可能比人更容易合理化 noise

大型語言模型還多了一個特殊問題：

$$
\text{Pattern Detector}
+
\text{Explanation Generator}.
$$

也就是它不只可以找到偶然 pattern，

還可以為 pattern 生成一個很有說服力的故事。

因此：

$$
\text{noise}
\rightarrow
\text{pattern}
\rightarrow
\text{narrative}.
$$

最後產生：

$$
\boxed{
\text{Narrative Overfitting}.
}
$$

例如：

> 數字 8 最近增加，可能反映開獎球表面摩擦差異。

如果沒有 equipment data，這只是一個 plausible story。

不能當證據。

---

# 47. 因此 AI 隨機研究應有 Explanation Firewall

任何機制解釋：

$$
CausalClaim
$$

都必須跟：

$$
ObservedEvidence
$$

分開。

系統應明確表示：

$$
\boxed{
\text{Observed}
}
$$

與：

$$
\boxed{
\text{Hypothesized}.
}
$$

例如：

> 觀察到機器 A 使用期間數字分布有顯著偏差。

可以。

但：

> 因為機器 A 的風扇造成球偏向。

除非真的有機械證據，否則只能寫：

$$
\text{candidate mechanism}.
$$

---

# 48. 本文提出 Randomness Research Stack

整套流程：

$$
\boxed{
\begin{array}{c}
\text{Layer 0: Define Generator}\\
\downarrow\\
\text{Layer 1: Define Null Model}\\
\downarrow\\
\text{Layer 2: Statistical Tests}\\
\downarrow\\
\text{Layer 3: Multiple-Test Control}\\
\downarrow\\
\text{Layer 4: Temporal Validation}\\
\downarrow\\
\text{Layer 5: Independent Replication}\\
\downarrow\\
\text{Layer 6: Predictive Test}\\
\downarrow\\
\text{Layer 7: Mechanism Investigation}
\end{array}
}
$$

只有越過 Layer 6，才有資格宣稱：

$$
\boxed{
\text{predictive anomaly}.
}
$$

---

# 49. 系列核心命題之一：Randomness Boundary Theorem

在本文框架中，可提出：

## 命題

若：

$$
Y_{t+1}\perp H_t,
$$

且 AI 所有輸入：

$$
Z_t=f(H_t)
$$

完全由 $H_t$ 生成，則：

$$
I(Z_t;Y_{t+1})=0.
$$

因此不存在只依靠 $H_t$ 的模型使其期望預測損失嚴格優於 Bayes baseline。

### 推論

對真正 IID 的公平彩票：

$$
\boxed{
\text{Historical-number AI cannot produce persistent predictive edge}.
}
$$

---

# 50. 第二命題：Finite-Sample Pattern Inevitability

對任何有限隨機序列，若 pattern hypothesis space：

$$
|\mathcal H|
$$

足夠大，則觀察到至少一個高度異常 pattern 的概率可以非常高。

因此：

$$
\boxed{
\text{Finding a surprising pattern is weak evidence when the search space is enormous}.
}
$$

這正是 AI 時代需要比傳統統計更嚴格的原因。

---

# 51. 第三命題：Audit–Prediction Separation

存在：

$$
D(P_{\text{observed}},P_{\text{expected}})>0
$$

並不推出：

$$
I(H_t;Y_{t+1})>0.
$$

也就是：

$$
\boxed{
\text{distributional anomaly}
\not\Rightarrow
\text{next-event predictability}.
}
$$

例如某一號碼確實整體略偏多，不代表可以精準預測它「下一期」會出。

---

# 52. 第四命題：Predictability–Exploitability Separation

即使：

$$
I(X;Y)>0,
$$

且：

$$
L_{\text{AI}}<L_{\text{baseline}},
$$

仍不推出：

$$
EV_{\text{net}}>0.
$$

因為：

$$
EV_{\text{net}}
=
EV_{\text{gross}}
-C.
$$

所以：

$$
\boxed{
\text{predictability}
\not\Rightarrow
\text{economic exploitability}.
}
$$

---

# 53. 第五命題：Randomness Assurance Is Layered

不能只從：

$$
\text{output statistics}
$$

判斷完整 RNG integrity。

更完整應是：

$$
\boxed{
R=
f(
E,
G,
S,
I,
O
),
}
$$

其中：

$$
E=\text{entropy source},
$$

$$
G=\text{generator design},
$$

$$
S=\text{seeding/state management},
$$

$$
I=\text{implementation},
$$

$$
O=\text{operational controls}.
$$

這與 NIST 以及 WLA 現行標準的多層設計方向一致。

---

# 54. 第六命題：AI Randomness Paradox

AI 能力越強：

$$
M\uparrow,
$$

它找到偶然 pattern 的能力也：

$$
F_{\text{false pattern}}\uparrow.
$$

如果 epistemic control 沒同步增加：

$$
E_{\text{control}}\not\uparrow,
$$

則：

$$
\boxed{
\text{Stronger AI can produce stronger false certainty}.
}
$$

這稱為：

$$
\boxed{
\text{AI Randomness Paradox}.
}
$$

---

# 55. 這可能比「AI 能不能猜中彩券」重要得多

因為這個命題不只適用博彩。

也適用：

- 金融；
- 醫療；
- 天文；
- 基因；
- 社會科學；
- 大規模資料探勘；
- 自主科學 AI。

只要：

$$
|\mathcal H|
$$

巨大，

就會出現：

$$
\text{automated false discovery}.
$$

所以未來 AI 科學系統需要的不只是：

$$
\text{better discovery engine},
$$

還需要：

$$
\boxed{
\text{better falsification engine}.
}
$$

---

# 56. 從彩券得到的一個普適 AI 原則

人工智慧最容易被誤解成：

$$
\text{Pattern Machine}.
$$

但真正成熟的科學 AI 應該是：

$$
\boxed{
\text{Pattern Machine}
+
\text{Null-Model Machine}
+
\text{Falsification Machine}.
}
$$

它不只問：

> 我找到什麼？

還要問：

> 如果其實什麼都不存在，我有多容易找到這個東西？

正式寫成：

$$
P(
\text{discovery}
\mid
H_0
).
$$

這個問題甚至比：

$$
P(
H_1
\mid
\text{discovery}
)
$$

更早。

---

# 57. AI 面對隨機性真正成熟的回答

因此，對一個公平彩票問題，最成熟的 AI 回答不是簡單：

> 我不能預測。

也不是：

> 根據近期熱號，我推薦……

而應該是：

> 在目前假設與公開證據下，沒有可靠證據顯示歷史開獎序列包含可以持續改善下一期預測的資訊。若要研究 AI 是否具有優勢，合理方向是檢驗生成機制是否存在狀態依賴、設備偏差、制度變更或可重複的 out-of-sample anomaly。

也就是：

$$
\boxed{
\text{Prediction refusal}
\rightarrow
\text{scientific redirection}.
}
$$

---

# 58. 與 Paper 00 的統合

Paper 00 定義：

$$
\mathcal E
=
f(S,I,M,T,C,R).
$$

對近似公平 IID 系統：

$$
S\approx0,
$$

因此：

$$
I\approx0.
$$

即使：

$$
M\rightarrow\infty,
$$

仍有：

$$
\boxed{
\mathcal E_{\text{prediction}}\approx0.
}
$$

因此：

$$
\frac{\partial \mathcal E}{\partial M}
\approx0
$$

在這個 regime 中成立。

這與運動市場完全不同。

當：

$$
S>0,
$$

$$
I>0,
$$

模型能力才可能真正轉化成：

$$
\mathcal E>0.
$$

---

# 59. 系列中的位置

本篇建立整個系列最左端：

$$
\boxed{
\text{Pure / Near-Pure Randomness}
}
$$

後續將逐步增加結構。

Paper 02：

$$
\text{Real-world state}
+
\text{market pricing}.
$$

Paper 03：

$$
\text{state}
+
\text{crowd}
+
\text{pari-mutuel dynamics}.
$$

Paper 05：

$$
\text{casino randomness}
+
\text{state-dependent exceptions}.
$$

Paper 06：

$$
\text{strategic opponents}.
$$

因此整個系列可以理解成：

$$
\text{Random}
\rightarrow
\text{Stateful}
\rightarrow
\text{Market}
\rightarrow
\text{Strategic}
\rightarrow
\text{Adaptive}.
$$

---

# 60. 研究邊界

本文不提供：

$$
\text{lottery prediction engine},
$$

$$
\text{RNG exploitation code},
$$

$$
\text{seed recovery attack},
$$

$$
\text{casino device exploitation}.
$$

本文研究的是：

$$
\boxed{
\text{何時預測在數學上具有資訊基礎，
以及如何避免把 noise 誤認為 intelligence。}
}
$$

這也是整個系列的共同研究邊界。

---

# 61. 結論

人工智慧並不因為足夠複雜，就能征服隨機性。

對真正 IID 系統：

$$
P(Y_{t+1}\mid H_t)
=
P(Y_{t+1}),
$$

因此：

$$
I(Y_{t+1};H_t)=0.
$$

由 data processing inequality：

$$
I(f(H_t);Y_{t+1})=0.
$$

所以：

$$
\boxed{
\text{AI cannot transform zero predictive information into positive predictive information}.
}
$$

然而，這不代表 AI 在隨機系統中沒有價值。

恰恰相反。

AI 可以從：

$$
\text{Predictor}
$$

轉變為：

$$
\boxed{
\text{Auditor of randomness}.
}
$$

它可以檢驗：

- 理論概率是否成立；
- 設備是否漂移；
- RNG entropy 是否下降；
- 不同機器是否產生不同分布；
- 制度變更是否形成 regime shift；
- 異常是否可以跨樣本重複。

因此真正成熟的問題不是：

> AI 能不能從亂數中找到神秘規律？

而是：

$$
\boxed{
\text{我們有沒有足夠證據相信，眼前的系統真的只剩下不可利用的隨機性？}
}
$$

如果答案是「是」：

$$
\text{Prediction Edge}\rightarrow0.
$$

如果答案是「不知道」：

$$
\text{Audit}.
$$

如果答案是「否」：

$$
\text{Investigate Structure}.
$$

因此可以把 AI 面對隨機性的正確決策流程壓縮成：

$$
\boxed{
\text{Test Structure}
\rightarrow
\text{Validate Information}
\rightarrow
\text{Falsify}
\rightarrow
\text{Only Then Predict}.
}
$$

這是本文所提出的 **AI Randomness Boundary**。

而它所揭露的更一般原則是：

$$
\boxed{
\text{真正強大的智能，
不只是善於找到模式；
更重要的是知道何時沒有足夠證據相信那個模式是真的。}
}
$$

---

## References / Standards Discussed

- UK Gambling Commission, *RTS 7 — Generation of Random Outcomes*, current technical requirements on acceptable randomness, unpredictability, seeding and prohibition of adaptive outcome manipulation.
- World Lottery Association, *WLA Security Control Standard 2024*, especially L.8 on RNG integrity, independent verification, physical/logical protection and segregation of duties.
- NIST SP 800-90B, *Recommendation for the Entropy Sources Used for Random Bit Generation*.
- NIST SP 800-90C, *Recommendation for Random Bit Generator Constructions*, finalized September 2025.

---

**Next:**  
**Paper 02 — AI 運動博彩：世界模型、資訊延遲、概率校準與算法莊家**