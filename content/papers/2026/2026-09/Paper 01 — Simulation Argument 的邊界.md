# Paper 01 — Simulation Argument 的邊界
## 條件機率、命題猜想與存在論誤讀

**Series:** Recursive Simulation, Transcendence, and Mathematical Non-Usurpation / 遞歸模擬、超越者與數學非僭越  
**Author:** Neo.K  
**Institution:** EveMissLab／一言諾科技有限公司  
**Date:** 2026-09-04  
**Status:** Internal Research Draft v0.1  
**Role:** Series opening paper  
**Scope:** Nick Bostrom’s 2003 Simulation Argument, conditional inference, observer-counting, future premises, epistemic level separation, and the boundary between formal validity and ontological claim

---

## 摘要

Nick Bostrom 於 2003 年發表的 Simulation Argument 並不是一個簡單的命題：

> 「我們大概率生活在電腦模擬中。」

其原始論證是一個三難結構。粗略而言，至少有一項成立：

1. 人類類文明幾乎都在到達 posthuman stage 前滅亡；
2. 能到達 posthuman stage 的文明幾乎都不大量執行 ancestor simulations；
3. 我們幾乎肯定身處 simulation。

Bostrom 在 2025 年新版 FAQ 中仍明確指出：論證只要求三項至少一項成立，並不告訴我們究竟是哪一項；他本人只願意給 simulation hypothesis「substantial probability」，並刻意拒絕提供看似精確的百分比。

因此，本篇不試圖「反駁 Simulation Argument」，而是研究一個更基本的問題：

> 一個形式上有力的條件式論證，可以被允許推到哪裡？

本篇區分：

$$
\boxed{
\text{Conjecture}
\neq
\text{Formal Consequence}
\neq
\text{Empirical Support}
\neq
\text{Future Actuality}
\neq
\text{Ontological Truth}.
}
$$

並提出 **Epistemic Level Separation Principle, ELSP**：

若模型 $M$ 在前提集合 $\mathcal A$ 下推出結論 $Q$：

$$
M,\mathcal A\vdash Q,
$$

則這只建立：

$$
\boxed{
Q\text{ is conditionally entailed by }M,\mathcal A.
}
$$

除非另有證據支持：

$$
\mathcal W\models\mathcal A,
$$

否則不能直接推出：

$$
\mathcal W\models Q,
$$

其中 $\mathcal W$ 表示實際世界。

本篇進一步指出，Simulation Argument 的主要不確定性不在其簡單比例計算，而在模型與未來世界之間的 grounding：

- posthuman civilization 是否出現；
- consciousness 是否具有足夠 substrate independence；
- ancestor simulation 是否具備可行性與實際誘因；
- posthuman civilization 是否大量執行它；
- observer/reference class 應如何定義；
- 未來文明的決策空間是否仍能由今天的概念模型充分描述。

因此：

$$
\boxed{
\text{valid mathematics}
\neq
\text{validated world-model}.
}
$$

而：

$$
\boxed{
\text{strong conditional argument}
\neq
\text{verified ontology}.
}
$$

本篇最終主張：Simulation Argument 應保留其真正的哲學力量，但不得因流行化、科技想像或數字巨大而被誤升格為「數學證明我們活在模擬世界」。數學可以約束一個假設世界中的推論，但不能單獨選定哪個假設世界就是現實。

---

# 1. 問題不是「Simulation Argument 對不對？」

首先必須避免另一種誤讀。

本系列並不主張：

$$
\boxed{
\text{Bostrom 2003 = bad argument}.
}
$$

更不主張：

$$
\boxed{
\text{simulation hypothesis = impossible}.
}
$$

真正要問的是：

$$
\boxed{
\text{這個 argument 的 epistemic jurisdiction 到哪裡？}
}
$$

也就是：

- 它證明了什麼？
- 它假設了什麼？
- 它沒有證明什麼？
- 哪些後續主張已經不再是原論文的 conclusion？

---

# 2. 原始三難

令：

$$
D
=
\text{文明在 posthuman stage 前幾乎都滅亡},
$$

$$
A
=
\text{posthuman civilizations 幾乎都不大量跑 ancestor simulations},
$$

$$
S
=
\text{我們身處 simulation}.
$$

Bostrom 的核心結論可以粗略表示成：

$$
\boxed{
D\lor A\lor S_{\mathrm{high}}
}
$$

其中：

$$
S_{\mathrm{high}}
$$

表示 simulation hypothesis 具有極高 observer-relative probability。

原論文的摘要明確採取「至少一項成立」的形式，而不是直接宣告第三項已被證明。

---

# 3. 2025 FAQ 仍然沒有把第三項單獨升格

Bostrom 後來再次指出：

$$
\boxed{
D\lor A\lor S
}
$$

並不決定究竟是哪一個 disjunct 成立。

因此，一個人完全可以：

$$
\boxed{
\text{accept the Simulation Argument}
}
$$

同時：

$$
\boxed{
\text{reject a high credence in the Simulation Hypothesis}.
}
$$

這是理解整個討論最重要的第一步。

---

# 4. 為什麼第三項一旦成立，數字會非常大？

令：

$$
f_P
$$

為人類類 technological civilizations 到達 posthuman stage 的比例。

令：

$$
\overline N
$$

為一個 posthuman civilization 平均執行的 ancestor simulations 數量。

令：

$$
\overline H
$$

為一個 civilization 在到達 posthuman stage 前的 human-type observers 數量。

則原 argument 的核心 observer-counting 結構可近似理解為：

$$
f_{\mathrm{sim}}
=
\frac{
f_P\overline N\overline H
}{
f_P\overline N\overline H+\overline H
}.
$$

約去 $\overline H$：

$$
\boxed{
f_{\mathrm{sim}}
=
\frac{
f_P\overline N
}{
f_P\overline N+1
}.
}
$$

只要：

$$
f_P\overline N\gg1,
$$

便有：

$$
f_{\mathrm{sim}}\rightarrow1.
$$

數學本身很簡潔。

真正困難的不是這個 fraction。

真正困難的是：

$$
\boxed{
f_P,\overline N
\text{ 在現實中到底應該是多少？}
}
$$

---

# 5. 巨大 multiplier 的誘惑

假設：

$$
f_P=10^{-2}
$$

而：

$$
\overline N=10^6.
$$

則：

$$
f_P\overline N=10^4,
$$

所以：

$$
f_{\mathrm{sim}}
\approx
\frac{10000}{10001}.
$$

非常接近：

$$
1.
$$

因此 Simulation Argument 很容易在流行敘事裡被壓縮成：

> 只要未來有文明能跑大量模擬，模擬人口一定遠大於原生人口，所以我們幾乎一定是模擬。

但這個敘述已偷偷把：

$$
\boxed{
\text{conditional parameters}
}
$$

變成：

$$
\boxed{
\text{future facts}.
}
$$

---

# 6. 第一個層級：Mathematical Truth

如果：

$$
x>0
$$

且：

$$
N\rightarrow\infty,
$$

那：

$$
\frac{xN}{xN+1}\rightarrow1.
$$

這是普通數學。

只要前提固定，數學關係沒有爭議。

可記為：

$$
\boxed{
E_0=\text{Formal / Mathematical Validity}.
}
$$

但：

$$
E_0
$$

沒有告訴我們：

$$
N
$$

在未來世界真的會趨近巨大。

---

# 7. 第二個層級：Model Validity

現在建立模型：

$$
M_{\mathrm{SA}}.
$$

其中假設：

- posthuman civilizations 可以存在；
- conscious simulations 可行；
- ancestor simulations 可以大量執行；
- observer counting 適用；
- reference class 足夠清楚。

則：

$$
M_{\mathrm{SA}}
\vdash
Q_{\mathrm{SA}}.
$$

這意味：

> 在這套模型與前提下，Simulation Argument 的 conclusion 可以成立。

這是：

$$
\boxed{
E_1=\text{Model-Conditional Validity}.
}
$$

仍然不是：

$$
\boxed{
\text{world verification}.
}
$$

---

# 8. 第三個層級：Empirical Grounding

要讓：

$$
M_{\mathrm{SA}}
$$

描述真實世界，

需要證據支持：

$$
\mathcal W
\approx
M_{\mathrm{SA}}.
$$

例如：

- civilization survival data；
- computational scaling；
- theory of consciousness；
- actual future preferences；
- physical resource limits；
- actual simulation practices。

問題是，最重要的變量恰好涉及：

$$
\boxed{
\text{我們尚未觀察到的 future civilizations}.
}
$$

因此 empirical grounding 必然不完整。

---

# 9. 第四個層級：Future Actuality

即使某項未來情境：

$$
F
$$

在目前模型下很 plausible，

也不能寫成：

$$
\boxed{
F=\text{future fact}.
}
$$

更合理是：

$$
P(F\mid M,D_t),
$$

其中：

- $M$：當前模型；
- $D_t$：時間 $t$ 時可用 evidence。

只要未來出現新資訊：

$$
D_{t+1},
$$

就可能：

$$
P(F\mid M,D_{t+1})
\neq
P(F\mid M,D_t).
$$

---

# 10. 第五個層級：Ontological Truth

最後才是：

$$
O=
\text{Reality itself has structure }R.
$$

例如：

$$
\boxed{
\text{我們實際上就是 ancestor simulation}.
}
$$

這是一個 world claim。

不是單純：

$$
\boxed{
\text{formal consequence}.
}
$$

所以：

$$
\boxed{
\text{Mathematical Possibility}
\neq
\text{Physical Possibility}
\neq
\text{Future Actuality}
\neq
\text{Ontological Actuality}.
}
$$

---

# 11. Epistemic Level Separation Principle

本篇正式提出：

$$
\boxed{
\text{ELSP: Epistemic Level Separation Principle}.
}
$$

若：

$$
M,\mathcal A\vdash Q,
$$

則不能僅由此推出：

$$
\mathcal W\models Q.
$$

必須另外建立：

$$
\boxed{
G(M,\mathcal W,\mathcal A)
}
$$

即 grounding relation。

換言之：

$$
\boxed{
\text{proof inside model}
+
\text{model-world grounding}
\rightarrow
\text{world-level warrant}.
}
$$

缺少後者：

$$
\text{formal validity}
$$

只能停留在 model level。

---

# 12. 模型不是世界

這個區分看似簡單，卻是很多流行理論誤讀的來源。

模型：

$$
M
$$

是對世界：

$$
\mathcal W
$$

的 representation。

因此：

$$
M\neq\mathcal W.
$$

即使：

$$
M
$$

能完美自洽，

也只表示：

$$
\boxed{
\text{there exists a coherent described structure}.
}
$$

不等於：

$$
\boxed{
\text{the actual world instantiates it}.
}
$$

---

# 13. 數學證明與世界模型被推翻要分開

這裡必須非常精確。

如果在固定公理系統：

$$
\mathcal A
$$

中：

$$
\mathcal A\vdash T
$$

而 proof 正確，

那麼新天文觀測不會「推翻」這個 theorem。

真正可能被修正的是：

$$
\boxed{
\mathcal W\models\mathcal A
}
$$

或：

$$
\boxed{
\mathcal A
\text{ 是否是描述 }\mathcal W\text{ 的好模型}.
}
$$

因此：

$$
\boxed{
\text{Mathematical theorem stability}
\neq
\text{World-model stability}.
}
$$

---

# 14. Newtonian Case 作為簡單校準

Newtonian mechanics 在適用域中極為成功。

但：

$$
\boxed{
\text{Newtonian mechanics works}
}
$$

從未邏輯保證：

$$
\boxed{
\text{Newtonian structure exhausts all physical reality}.
}
$$

後來更廣的物理理論沒有讓：

$$
F=ma
$$

突然變成無意義。

真正發生的是：

$$
\boxed{
\text{domain restriction}.
}
$$

這也是處理所有強 model 的合理態度。

---

# 15. Simulation Argument 的 Future Premise Problem

Simulation Argument 比普通現存物理模型更特殊。

它的重要 premises 部分位於：

$$
\boxed{
\text{future}.
}
$$

例如：

$$
P(
\text{posthuman civilization exists}
).
$$

$$
P(
\text{mass ancestor simulation}
\mid
\text{posthuman}
).
$$

這些不是目前可大量統計的 observed frequencies。

因此：

$$
\boxed{
\text{future extrapolation}
}
$$

在 argument 中具有重要角色。

---

# 16. Future Extrapolation 不是錯，但必須標記

任何文明研究都必須做 extrapolation。

問題不是：

$$
\boxed{
\text{不能預測未來}.
}
$$

而是：

$$
\boxed{
\text{不能把預測的 model output 改名為 future fact}.
}
$$

所以合理寫法：

$$
\boxed{
\text{Under assumptions }A_1,\ldots,A_n,
\text{ future }F\text{ becomes plausible}.
}
$$

不合理的偷換：

$$
\boxed{
F\text{ is mathematically inevitable}.
}
$$

---

# 17. 未來最麻煩的是 Transition Function 自己可能改變

普通預測常假設：

$$
x_{t+1}=F(x_t).
$$

於是：

$$
x_{t+n}=F^n(x_t).
$$

但對超長期文明預測，

真正問題可能是：

$$
\boxed{
F_t\neq F_{t+1}.
}
$$

文明會改變：

- technology；
- preferences；
- institutions；
- substrates；
- reproduction；
- cognition；
- concepts of identity；
- relation to computation。

因此：

$$
\boxed{
\text{future state uncertainty}
+
\text{future transition-law uncertainty}.
}
$$

---

# 18. 更極端：State Space 也可能改變

今天我們把 civilization 行動集合寫成：

$$
\Omega_t.
$$

到了 posthuman stage：

$$
\Omega_{t+n}
$$

可能包含今天不存在的 action categories。

因此：

$$
\boxed{
\Omega_t\neq\Omega_{t+n}.
}
$$

這意味今天的模型可能不只預測錯 action，

甚至沒有表達真正未來 action 的 vocabulary。

---

# 19. 「超越者不可想像」不能成為單向免責牌

假設有人回答：

> posthuman civilization 已經超越人類，所以你不能用今天的人類心理推論祂們。

這本身完全可能成立。

但一旦接受：

$$
\boxed{
C_{\mathrm{post}}
\notin
\mathcal M_{\mathrm{human}}
}
$$

就同時削弱：

$$
P(
\text{ancestor simulation}
\mid
C_{\mathrm{post}}
).
$$

因為如果其 behavior 真不可由現有 model 推測，

那合理結果是：

$$
\boxed{
\text{higher uncertainty}.
}
$$

不是：

$$
\boxed{
P(\text{mass simulation})\rightarrow1.
}
$$

---

# 20. Epistemic Symmetry Requirement

因此本篇提出：

$$
\boxed{
\text{ESR: Epistemic Symmetry Requirement}.
}
$$

不能在需要保護 hypothesis 時說：

$$
\text{future civilization is unknowable},
$$

卻在需要 probability multiplier 時說：

$$
\text{future civilization will predictably run enormous simulations}.
$$

如果不可知性適用，

它必須對所有相關 future-behavior claims 對稱生效。

---

# 21. Substrate Independence 仍是一項 substantive premise

Simulation Argument 的一個重要哲學前提是：

$$
\boxed{
\text{appropriate computational organization can support consciousness}.
}
$$

若：

$$
\text{simulation}
$$

只產生 behaviorally convincing zombies，

而沒有：

$$
\text{subjective observer experience},
$$

則 observer count：

$$
N_{\mathrm{sim}}
$$

不能直接增加。

所以：

$$
\boxed{
\text{computational simulation}
\neq
\text{automatically conscious simulation}.
}
$$

這不是 fraction formula 能自行證明的。

---

# 22. Consciousness Premise 的層級

可以寫：

$$
C_s=
P(
\text{consciousness}
\mid
\text{appropriate simulation}
).
$$

若：

$$
C_s\approx1,
$$

Simulation Argument observer multiplier 強。

若：

$$
C_s\approx0,
$$

則：

$$
N_{\mathrm{conscious\ sim}}
$$

大幅下降。

因此更完整：

$$
f_{\mathrm{sim}}
=
f(
f_P,
\overline N,
C_s,
R_C,
\ldots
),
$$

其中：

$$
R_C
$$

代表 reference-class assumptions。

---

# 23. Reference Class 不是純算術問題

假設世界裡有：

- biological humans；
- uploads；
- AIs；
- reconstructed ancestors；
- partial minds；
- alien minds；
- observer-moments。

那什麼叫：

$$
\boxed{
\text{observer like us}?
}
$$

不同 reference class：

$$
\mathcal R_1,\mathcal R_2
$$

可能產生不同：

$$
P(S\mid\mathcal R_i).
$$

所以：

$$
\boxed{
\text{observer counting}
}
$$

本身具有哲學 modeling content。

---

# 24. Bland Indifference Principle 的真正角色

Bostrom 的 argument 需要某種很弱的 indifference principle：

若 simulated 與 non-simulated observers 在 relevant experience 上無法區分，

且 simulated observers 在 reference class 中壓倒性多，

則應提高自己是 simulated observer 的 credence。

其形式可粗略理解：

$$
P(S\mid E,\mathcal R)
\approx
\frac{
N_{S,E,\mathcal R}
}{
N_{S,E,\mathcal R}
+
N_{B,E,\mathcal R}
}.
$$

這仍然是一個：

$$
\boxed{
\text{self-locating inference rule}.
}
$$

不是實驗儀器直接讀出的「simulation percentage」。

---

# 25. Probability of Hypothesis 與 Frequency of Simulated Observers

這兩個概念也常被混合。

$$
f_{\mathrm{sim}}
$$

是 model 中 simulated observers 的比例。

而：

$$
P(
\text{I am simulated}
\mid
E
)
$$

需要加入 self-location principle。

所以：

$$
\boxed{
f_{\mathrm{sim}}
\rightarrow
P(S)
}
$$

並不是單純 identity；

它中間存在 epistemic principle。

---

# 26. 「很大的數字」沒有額外本體權威

假設：

$$
\overline N=10^{30}.
$$

這會讓 conditional fraction 非常接近 $1$。

但：

$$
10^{30}
$$

的巨大只會放大已接受前提的 consequence。

它不會自動提高：

$$
P(
\overline N=10^{30}
\text{ in reality}
).
$$

所以：

$$
\boxed{
\text{Magnitude amplifies implication, not premise warrant}.
}
$$

---

# 27. 這是 Simulation Argument 最容易被大眾誤讀的地方

流行版本往往：

$$
\text{future computing could be huge}
$$

變成：

$$
\text{future civilizations will run huge ancestor simulations}.
$$

再變成：

$$
\text{there will be vastly more simulated observers}.
$$

再變成：

$$
\text{we are almost certainly simulated}.
$$

最後甚至：

$$
\boxed{
\text{science proved reality is simulation}.
}
$$

這是一條典型：

$$
\boxed{
\text{Epistemic Inflation Chain}.
}
$$

---

# 28. Epistemic Inflation

本篇定義：

$$
\boxed{
\mathsf{EIF}
:
H
\rightarrow
M
\rightarrow
P
\rightarrow
F
\rightarrow
O.
}
$$

其中：

- $H$：hypothesis；
- $M$：formal model；
- $P$：plausible consequence；
- $F$：treated-as-fact；
- $O$：ontological absolutization。

問題不是：

$$
H\rightarrow M
$$

或：

$$
M\rightarrow P.
$$

問題是沒有新 evidence 卻把：

$$
P
$$

偷偷升成：

$$
F
$$

甚至：

$$
O.
$$

---

# 29. 作者主張與二手敘事必須分離

這裡需要明確保護原理論。

若媒體、影片、論壇或科技圈說：

> Bostrom mathematically proved that we probably live in a simulation.

不能因此反過來把這句話當成：

$$
\boxed{
\text{Bostrom's exact academic claim}.
}
$$

原始理論、作者後續 clarification 與二手 popularization：

$$
\boxed{
\text{must be separately attributed}.
}
$$

---

# 30. 2025 FAQ 的認識論克制

Bostrom 後來明確表示：

- argument 本身基本 sound；
- 它只顯示三個 disjunct 至少一個成立；
- 他不認為我們對三項任一有 very strong evidence；
- 他給 simulation hypothesis substantial probability；
- 他避免指定具體 number，以免產生 false precision。

這其實是一個重要校準。

因此本系列批判的主要對象不是：

$$
\boxed{
\text{作者明確做出的條件式三難}.
}
$$

而是：

$$
\boxed{
\text{由條件式三難到已驗證本體論的非授權跳躍}.
}
$$

---

# 31. Simulation Argument 真正強在哪裡？

把誤讀全部拿掉後，它仍然很強。

它指出一個真正不舒服的結構：

如果：

$$
P(\text{reach posthuman})
$$

不是極低，

且：

$$
P(\text{mass ancestor simulation}\mid\text{posthuman})
$$

也不是極低，

且每個成功文明可以產生巨大：

$$
\overline N,
$$

那：

$$
\boxed{
\text{non-simulated human-like observers become a small minority}.
}
$$

這是一個值得認真處理的 conditional tension。

---

# 32. 它真正逼迫我們重新分配 Credence

合理結果不是：

$$
\boxed{
S=1.
}
$$

而是：

$$
\boxed{
P(D)+P(A)+P(S)
}
$$

必須在某種相容方式上承擔高度 credence。

也就是：

> 不能同時非常自信地相信文明會普遍存活、普遍大量跑 ancestor simulation，而且我們又幾乎肯定是非模擬原生 observer。

這才是 argument 真正漂亮的地方。

---

# 33. 強 Conditional 不代表弱理論

本篇的區分不是為了把它「降格」。

相反：

$$
\boxed{
\text{A strong conditional theorem is valuable even when its antecedents remain uncertain}.
}
$$

很多科學、經濟、決策理論都依賴：

$$
A\Rightarrow B.
$$

知道：

$$
A\Rightarrow B
$$

本身就能限制可能世界。

只是不能把：

$$
A
$$

未經驗證地偷渡進 actuality。

---

# 34. Conjecture 的正確地位

一個 conjecture：

$$
H
$$

在未完成論證與驗證前，

就是：

$$
\boxed{
H.
}
$$

它可以：

- 非常有洞察；
- 非常 plausible；
- 非常值得研究；
- 非常有 prediction power。

仍然不等於：

$$
\boxed{
\text{established fact}.
}
$$

這不是貶低 conjecture。

這是讓 epistemic label 保持正確。

---

# 35. 即使今天被大量支持，也保留 Future Revisability

對 empirical world-model：

$$
M_t,
$$

今天可能：

$$
P(M_t\mid D_t)\approx1.
$$

但未來：

$$
D_{t+1}
$$

可能要求：

$$
M_t\rightarrow M_{t+1}.
$$

因此：

$$
\boxed{
\text{high present confidence}
\neq
\text{guaranteed final ontology}.
}
$$

科學史大量存在：

$$
\text{successful model}
\rightarrow
\text{broader replacement / restriction}.
$$

---

# 36. 但這不是 Radical Skepticism

不能反過來說：

> 既然所有 empirical theories 未來都可能更新，所以現在什麼都不知道。

這也錯。

應該是：

$$
\boxed{
\text{fallibilism}
\neq
\text{nihilism}.
}
$$

我們可以根據 evidence 給：

$$
P(H\mid D)
$$

很高。

只是不把：

$$
P\approx1
$$

誤寫成：

$$
\boxed{
\text{metaphysically unrevisable certainty}.
}
$$

---

# 37. Evidence Ladder

本篇給出一個簡化 ladder。

$$
L_0=\text{Conceptual Possibility}
$$

$$
L_1=\text{Formal Consistency}
$$

$$
L_2=\text{Conditional Deduction}
$$

$$
L_3=\text{Empirical Plausibility}
$$

$$
L_4=\text{Repeated Empirical Support}
$$

$$
L_5=\text{Strong Causal Model}
$$

$$
L_6=\text{Ontological Interpretation}
$$

注意：

$$
\boxed{
L_2\not\Rightarrow L_6.
}
$$

甚至：

$$
\boxed{
L_5\not\Rightarrow
\text{unrevisable metaphysical finality}.
}
$$

---

# 38. Simulation Argument 目前在哪裡？

最保守定位：

其核心 probability structure：

$$
\boxed{
L_2=\text{strong conditional deduction}.
}
$$

其若干 technology assumptions：

$$
\boxed{
L_3=\text{plausibility arguments}.
}
$$

而：

$$
\boxed{
\text{我們真的身處 simulation}
}
$$

目前仍不能當成：

$$
L_4/L_5
$$

級 empirical conclusion。

---

# 39. 「Simulation Theory」這個稱呼本身也容易誤導

大眾有時把：

$$
\text{Simulation Argument}
$$

稱作：

$$
\text{Simulation Theory}.
$$

這容易讓它看起來像：

- General Relativity；
- Evolutionary Theory；
- Germ Theory

那樣有大規模 empirical structure。

但 Simulation Argument 本質上主要是一個：

$$
\boxed{
\text{philosophical probability / self-location argument}.
}
$$

因此最好維持名稱層級。

---

# 40. Simulation Hypothesis 與 Simulation Argument 也不是同一個東西

定義：

$$
H_S=
\text{we are simulated}.
$$

而：

$$
A_S=
\text{the argument establishing the trilemma}.
$$

所以：

$$
\boxed{
A_S\text{ sound}
\not\Rightarrow
H_S\text{ certainly true}.
}
$$

這一點 Bostrom 自己後來也明確重申。

---

# 41. 本篇不是否定未來超越者

本篇也不主張：

$$
\boxed{
\text{posthuman civilizations cannot exist}.
}
$$

相反：

$$
\text{posthuman}
$$

完全可以是 legitimate scenario variable。

但：

$$
\boxed{
\text{scenario variable}
\neq
\text{future observed entity}.
}
$$

這條界線必須保留。

---

# 42. 本篇也不是禁止數學研究未來

數學當然可以研究：

$$
\text{possible futures}.
$$

例如：

$$
P(F_i\mid A_j).
$$

甚至建立：

$$
\mathcal F=
\{F_1,F_2,\ldots,F_n\}.
$$

問題只在：

$$
\boxed{
\text{future scenario}
\rightarrow
\text{future actuality}
}
$$

需要額外 warrant。

---

# 43. 數學的真正力量

數學最強的地方恰恰是：

$$
\boxed{
\text{如果前提成立，哪些結論逃不掉？}
}
$$

所以：

$$
A\land B\land C
\Rightarrow
Q
$$

可以非常重要。

它讓研究者知道：

> 如果我拒絕 $Q$，那麼至少必須重新檢查 $A,B,C$ 中某一項。

這就是 Simulation Argument 真正值得保留的形式力量。

---

# 44. 不應要求數學完成它不負責的工作

數學不能單獨回答：

$$
\boxed{
\text{Which physically possible future will history actualize?}
}
$$

也不能單獨回答：

$$
\boxed{
\text{Which coherent ontology is the ontology of this world?}
}
$$

這些問題需要：

- empirical observation；
- causal inference；
- theory choice；
- philosophical interpretation。

---

# 45. Mathematical Non-Usurpation 的預告

本系列最後一篇會完整提出：

$$
\boxed{
\text{Mathematical Non-Usurpation Principle}.
}
$$

本篇只先建立必要前置：

$$
\boxed{
M\models Q
\not\Rightarrow
\mathcal W\models Q.
}
$$

以及：

$$
\boxed{
\text{formal inevitability inside a model}
\neq
\text{historical inevitability outside it}.
}
$$

---

# 46. 對 Simulation Argument 的合理閱讀方式

最合理的閱讀是：

> 如果 technologically mature civilizations 可以並且實際會大量產生具有 human-type conscious experiences 的 ancestor simulations，而且相關 observer-selection principle 適用，那麼我們作為非模擬 observer 的 credence 會面臨非常強的壓力。

這是一個：

$$
\boxed{
\text{conditional philosophical result}.
}
$$

---

# 47. 不合理的閱讀方式

不應改寫成：

> 數學已經證明我們有 99.9% 機率活在 Matrix。

因為這句話把：

- future civilization probability；
- simulation motives；
- consciousness；
- reference class；
- world-model applicability

全部隱藏了。

---

# 48. 更不合理的是直接升到第一因

從：

$$
H_S
$$

即使有一天得到很強 evidence，

仍不能直接推出：

$$
\boxed{
\text{ultimate creator exists}.
}
$$

因為：

$$
\text{simulator}
$$

只是一個可能的 proximal cause。

這個問題將在 Paper 02 的 recursive transcendence 中正式處理。

---

# 49. 最終分層

本篇建議所有類似未來／宇宙論 argument 均至少標記：

### H — Hypothesis

$$
H
$$

### M — Model

$$
M(H)
$$

### D — Deduction

$$
M\vdash Q
$$

### E — Evidence

$$
D_{\mathrm{emp}}
$$

### F — Future Projection

$$
P(F\mid M,D_{\mathrm{emp}})
$$

### O — Ontological Interpretation

$$
O(F,\mathcal W).
$$

不能寫：

$$
H=M=D=E=F=O.
$$

---

# 50. Paper 01 核心命題

本篇最終提出六個命題。

## Proposition 1 — Conditionality

$$
\boxed{
\text{Simulation Argument is primarily a conditional trilemma, not a direct empirical measurement of our world's substrate}.
}
$$

## Proposition 2 — Model/World Separation

$$
\boxed{
M\models Q
\not\Rightarrow
\mathcal W\models Q.
}
$$

## Proposition 3 — Future Premise Uncertainty

$$
\boxed{
\text{unknown future behavior cannot be silently promoted into fixed model parameters}.
}
$$

## Proposition 4 — Epistemic Symmetry

若 posthuman agents 被宣告超出現有 cognition model，

則同一不可知性也必須限制對其 simulation behavior 的預測。

## Proposition 5 — Magnitude Non-Authority

$$
\boxed{
\text{large numerical consequences amplify accepted premises; they do not validate the premises}.
}
$$

## Proposition 6 — Ontological Non-Escalation

$$
\boxed{
\text{formal or statistical support does not by itself authorize final ontological interpretation}.
}
$$

---

# 51. Internal Seal

Simulation Argument 值得保留，因為它建立了真正有力量的：

$$
\boxed{
\text{conditional observer-counting tension}.
}
$$

但它的正確 epistemic reading 必須是：

$$
\boxed{
\text{Conjecture}
\rightarrow
\text{Model}
\rightarrow
\text{Conditional Result}
}
$$

而不是：

$$
\boxed{
\text{Conjecture}
\rightarrow
\text{Mathematics}
\rightarrow
\text{Reality Proven}.
}
$$

因此：

$$
\boxed{
\text{Do not weaken the argument by exaggerating its conclusion.}
}
$$

以及：

$$
\boxed{
\text{Do not turn conditional mathematics into unearned ontology.}
}
$$

下一篇將處理更深的一個缺口：

**Paper 02 —《超越者之上的超越者：Simulation Argument 的遞歸未閉包問題》**

其核心問題是：

$$
\boxed{
\text{如果 posthuman civilization 能模擬我們，
那麼誰保證 posthuman civilization 自己不是另一層世界中的有限存在？}
}
$$

也就是：

$$
\boxed{
\text{Downward Transcendence}
\neq
\text{Ontological Terminality}.
}
$$

---

## Source Notes

1. Nick Bostrom, “Are You Living in a Computer Simulation?”, *The Philosophical Quarterly*, 53(211), 2003, pp. 243–255.
2. Nick Bostrom, “The Simulation Argument FAQ”, version 2.0, 2025.
3. Bostrom’s original paper explicitly frames the conclusion as a disjunction among three propositions and develops the observer-counting fraction using the survival fraction of human-level civilizations and the expected number of ancestor simulations.
4. In the 2025 FAQ, Bostrom states that accepting the argument does not require accepting the simulation hypothesis, says he assigns the latter a “substantial probability,” and declines to assign a precise numerical probability because this could suggest false precision.
5. The argument relies on self-locating / observer-selection reasoning and treats substrate independence as an important preliminary assumption.
