# 自然動力認知實現命題：自然界能否自行生成 AI-like 功能體？

**系列：認知功能體的物理實現與自然可觀測性研究，第 3 篇**  
**版本：v0.1**  
**日期：2026-08-28**  
**狀態：公開草稿／自然可實現性命題論文**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司

## 摘要

上一篇建立「人工認知功能可實現性」（Artificial Functional Realizability, AFR），指出光學、電子、機械、材料與電磁場—幾何約束等不同物理 substrate 已能實現若干 AI-like functions。人工版本因此具有相當直接的實驗存在性證據。然而，人工可實現性不能推出自然可生成性：工程師可以事先指定目標、選擇材料、布置邊界、設計 loss、訓練參數與建立 readout；自然界若要自行生成等價功能體，則必須由局部物理律、非平衡能量流、自組織、歷史累積、選擇與環境耦合自行形成相應的關係—結構—動力閉環。

本文提出「自然動力認知實現」（Natural Dynamical Realizability, NDR）作為工作性框架。NDR 不以「非人工材料」定義自然，因為人工裝置本身同樣服從自然律；本文改以生成因果史定義：若一個 AI-like 功能體的形成不依賴針對該目標功能的外部智能設計、loss function、target-conditioned parameter update 或外部功能 readout，則其生成路徑可被視為 NDR 候選。

本文進一步定義自然功能盆地。令 $\mathcal F_\theta$ 為達到指定 AI-like 功能門檻 $\theta$ 的軌跡集合，則

$$
\mathcal B_{\mathrm{NDR}}(\theta,T)
=
\left\{
z_0:
\exists t_0,\;
\mathcal D_{\mathrm{nat}}^{[t_0,t_0+T]}(z_0)
\in
\mathcal F_\theta
\right\}
$$

表示在自然動力下，能於某時間進入並持續至少 $T$ 的功能生成盆地。真正的自然存在性問題不只是終態在狀態空間中有沒有一個點，而是：在物理允許的初始條件與環境 ensemble 中，這類 basin 是否非空、是否具有非零有效測度，以及是否存在不依賴極端精細調參的生成路徑。

現有科學尚不能證明非生物自然界存在 AI-like 功能體，但已有若干重要機制性支點。2024 年 Nature 報導的 formose self-organizing chemical reaction network 顯示，複雜化學網路可以在不逐反應設計的情況下展現非線性分類、動力系統模擬、記憶與時間序列預測能力；2026 年 Nature Reviews Chemistry 進一步指出 far-from-equilibrium、non-steady-state chemical dynamics 可作為 molecular-scale neuromorphic information-processing medium。另一方面，非平衡 self-assembly、synthetic protocells、active matter 與 adaptive physical networks 也顯示，物理系統能以能量流維持暫態結構、產生歷史依賴、改變有效關係或形成適應性行為。然而，這些多數仍是人工構建、人工驅動或人工定義目標的實驗，因此只能證明候選機制的物理可行性，而不是 NDR 的自然存在性。

本文最後將 NDR 與 Boltzmann-type direct fluctuation 分離。NDR 關心的是生成路徑與 basin，

$$
z_0
\rightarrow
z_1
\rightarrow
\cdots
\rightarrow
\mathcal F_\theta,
$$

而 direct fluctuation 則允許系統幾乎直接落到高度特定的功能終態。兩者的測度、歷史需求與因果解釋完全不同。下一篇將專門處理這個分離。

**關鍵詞：** 自然動力認知實現、NDR、自組織、非平衡系統、自然計算、化學 reservoir、功能盆地、生成路徑、AI-like 功能體

---

## 1. 人工可實現性成立，不代表自然可生成性成立

第 2 篇建立：

$$
\exists c_{\mathrm{art}}
:
F(c_{\mathrm{art}})
\in
\mathcal F_{\mathrm{AI}}.
$$

這表示在人類可以控制材料、幾何、邊界、外場、訓練與 readout 時，若干 AI-like functions 已可跨 substrate 實現。

但自然版本問的是：

$$
\boxed{
\exists c_{\mathrm{nat}}
:
F(c_{\mathrm{nat}})
\in
\mathcal F_{\mathrm{AI}}
\quad ?
}
$$

其中 $c_{\mathrm{nat}}$ 不能把答案偷偷放在生成程序裡。

人工設計可以先指定：

$$
F^\star
$$

再求：

$$
c^\star
=
\arg\min_c
L(F(c),F^\star).
$$

自然界若沒有外部設計者，則不能假設存在一個已知 $F^\star$ 的全域 optimizer。

它必須依靠：

$$
\text{local interaction}
+
\text{energy flow}
+
\text{self-organization}
+
\text{persistence}
+
\text{selection}
+
\text{history}
$$

形成一條內生路徑：

$$
c_0
\rightarrow
c_1
\rightarrow
\cdots
\rightarrow
c_n.
$$

因此：

$$
\boxed{
\mathrm{AFR}
\not\Rightarrow
\mathrm{NDR}
}
$$

即使 AFR 與 NDR 最後落入完全相同的功能等價類。

---

## 2. 「自然」不是一種材料，而是一種生成因果史

如果把自然定義成：

> 沒有人造材料。

那麼定義會失敗。

因為：

- 人造晶片仍由自然粒子與自然物理律構成；
- 實驗室裡的化學反應仍是真實化學；
- artificial metasurface 仍只是被人為安排的電磁邊界。

因此 AFR 與 NDR 的真正差異不在物質本體，而在生成因果史。

本文提出：

### NDR 操作性自然條件

若候選系統 $X$ 的形成與持續，不依賴針對目標功能 $\tau$ 的外部智能操作

$$
O_{\mathrm{ext}}^\tau,
$$

尤其不依賴：

- target-conditioned geometry selection；
- external loss function；
- external gradient update；
- task-specific readout；
- externally injected semantic labels；
- 依照目標表現反覆人工挑選結構；

則其路徑可被列入 NDR 候選。

因此我們真正排除的是：

$$
\boxed{
\text{target-conditioned external optimization}
}
$$

而不是排除所有外部環境影響。

自然系統當然可以依賴太陽、重力、化學梯度、潮汐、磁場、熱流或其他外部能源；關鍵在於這些環境並沒有因為知道「我們想要一個 AI」而調整自身參數。

---

## 3. 功能目標集合

延續第 2 篇，定義 AI-like 功能向量：

$$
\Psi_{\mathrm{AI}}(X)
=
(
M,
N,
I,
P,
A,
C,
G,
R
),
$$

其中：

- $M$：memory；
- $N$：nonlinear state-dependent processing；
- $I$：environment-relevant information processing；
- $P$：prediction；
- $A$：adaptation；
- $C$：closed-loop control；
- $G$：generalization；
- $R$：causal restructuring。

給定門檻向量 $\theta$，定義功能候選集合：

$$
\mathcal F_\theta
=
\left\{
\mathcal T:
\Psi_{\mathrm{AI}}(\mathcal T)
\succeq
\theta
\right\}.
$$

這裡 $\mathcal T$ 不是單一 snapshot，而是一段時間軌跡。

因此 NDR 不問：

> 自然界能不能長出一個「像 AI 的物體」？

而問：

> 自然動力能不能生成一段滿足指定認知功能門檻的持續軌跡？

這個改寫把 morphology 從必要條件中移除。

---

## 4. 自然功能盆地

令完整自然狀態為：

$$
z=
(X,M,R,G,S,E,H).
$$

自然動力為：

$$
z(t)
=
\mathcal D_{\mathrm{nat}}^t(z_0).
$$

對功能門檻 $\theta$ 與最小持續時間 $T$，定義：

$$
\boxed{
\mathcal B_{\mathrm{NDR}}(\theta,T)
=
\left\{
z_0:
\exists t_0,\;
\mathcal D_{\mathrm{nat}}^{[t_0,t_0+T]}(z_0)
\in
\mathcal F_\theta
\right\}
}
$$

這就是自然功能生成盆地。

如果：

$$
\mathcal B_{\mathrm{NDR}}(\theta,T)
=
\varnothing,
$$

則在指定物理模型、環境集合與功能定義下，NDR 不成立。

如果：

$$
\mathcal B_{\mathrm{NDR}}(\theta,T)
\neq
\varnothing,
$$

只代表存在至少一條生成路徑。

更強的問題是：

$$
\mu
\left(
\mathcal B_{\mathrm{NDR}}(\theta,T)
\right)
>0
\quad ?
$$

其中 $\mu$ 必須相對於明確指定的 initial-condition / environment ensemble 定義，不能假裝宇宙存在一個天然唯一的均勻測度。

---

## 5. 為什麼 basin 比終態機率更重要？

假設目標功能區域為：

$$
\mathcal F_\theta.
$$

若只問：

$$
P(z\in\mathcal F_\theta),
$$

我們只是在問隨機 snapshot 落入功能區的概率。

但如果 $\mathcal F_\theta$ 是某個吸引區域、metastable manifold 或由自組織維持的 dynamical regime，那麼真正重要的是：

$$
P
\left(
z_0
\in
\mathcal B_{\mathrm{NDR}}
\right).
$$

只要：

$$
z_0
\in
\mathcal B_{\mathrm{NDR}},
$$

後續物理演化就可能自行完成：

$$
z_0
\rightarrow
z_1
\rightarrow
\cdots
\rightarrow
\mathcal F_\theta.
$$

因此自然生成不需要一次性抽中完整終態。

這使：

$$
\boxed{
\text{terminal-state rarity}
}
$$

與：

$$
\boxed{
\text{generative-path rarity}
}
$$

成為完全不同的問題。

這也是 NDR 與下一篇 Boltzmann-type direct fluctuation 分離的核心。

---

## 6. 第一個機制支點：自組織

Self-organization 已廣泛存在於物理、化學、生物、集體行為與工程系統。

但：

$$
\boxed{
\text{self-organization}
\not\Rightarrow
\text{AI-like cognition}
}
$$

晶體、渦旋、對流胞與化學波都可以形成秩序。

自組織對 NDR 的真正價值只是證明：

> 局部作用律不需要外部設計者逐元素安排，也能形成新的宏觀關係與結構。

可以寫成：

$$
R_{\mathrm{local}}
+
E_{\mathrm{flow}}
\rightarrow
S_{\mathrm{macro}}.
$$

這提供了第一個必要橋樑：

$$
\boxed{
\text{local dynamics}
\rightarrow
\text{emergent constraint architecture}
}
$$

但它仍遠低於認知功能門檻。

---

## 7. 第二個機制支點：非平衡能量流與暫態結構

生命與許多 active systems 都不是平衡態中的靜態物件。

它們依靠：

$$
J_E
=
\text{continuous energy / matter flux}
$$

維持：

$$
S(t)
$$

遠離平衡。

2024 年對 non-equilibrium self-assembly 的綜述指出，reaction networks、transient compartmentalization、self-reproduction、metabolic cycles 與 far-from-equilibrium operation 是建立 living-matter-like properties 的重要組件；但 adaptation、selection、information transfer 與 open-ended evolution 仍是重大挑戰。

因此 NDR 若存在，很可能不應只搜尋：

$$
\text{stable static object},
$$

而應搜尋：

$$
\boxed{
\text{energy-supported persistent dynamical organization}.
}
$$

也就是它可能只有在持續能量流存在時才「是那個系統」。

---

## 8. 第三個機制支點：自組織化學本身具有資訊處理能力

2024 年 Baltussen 等人在 Nature 報導 formose reaction 的 self-organizing chemical reservoir。

該系統的化學網路並不是為每一項 computation 逐反應人工設計；其複雜非線性反應動力本身提供 rich reservoir states。

實驗證明它可以：

- 執行多種 nonlinear classification；
- 模擬複雜 dynamical systems；
- 預測時間序列；
- 保留與輸入歷史相關的 memory-like state；
- 對 Lorenz-type fluctuating input 做 future forecasting。

因此至少存在：

$$
\boxed{
\text{self-organizing chemistry}
\rightarrow
\text{intrinsic computational capacity}.
}
$$

2026 年 Nature Reviews Chemistry 進一步指出，non-steady-state、far-from-equilibrium chemical dynamics 可以透過 nonlinear、collective、time-evolving behaviour 支持 molecular-scale neuromorphic computing。

這是 NDR 的重要支點。

但它不是 NDR 的證明。

因為 formose reservoir 實驗仍使用：

- 人工 reactor；
- 人工 input sequence；
- mass-spectrometric readout；
- 外部 linear regression weights；
- 外部指定的 classification / prediction target。

因此它支持：

$$
\text{natural-law mechanism sufficiency},
$$

不支持：

$$
\text{natural autonomous realization}.
$$

---

## 9. 外部 readout 是自然版本最危險的假陽性

假設自然系統 $X$ 產生高維 dynamics：

$$
z(t).
$$

我們訓練一個外部 AI：

$$
D_\theta(z)
\rightarrow
y.
$$

如果 $D_\theta$ 可以從 $z$ 中解出天氣、軌道、分類或未來訊號，並不能推出：

$$
X
\text{ 自己在做該 prediction}.
$$

因為高維非線性物理系統本來就可能是優秀 reservoir。

因此 NDR 必須要求至少部分 readout 位於系統自己的因果鏈：

$$
z
\rightarrow
r_{\mathrm{endo}}
\rightarrow
a
\rightarrow
E'
\rightarrow
z'.
$$

其中：

$$
r_{\mathrm{endo}}
$$

是內生物理 readout，而不是我們實驗室裡的一個 regression head。

所以：

$$
\boxed{
\text{externally decodable information}
\neq
\text{internally used information}.
}
$$

這是 NDR 最重要的判別之一。

---

## 10. 第四個機制支點：物理系統可以改寫自身關係以改善功能

2025 年的 “Physical Networks Become What They Learn” 顯示，一類物理 network 可以藉由局部學習規則修改 internal interactions，使物理響應逐步符合 desired function。

同年的 smart active matter 理論也研究 decentralized learning，其中 local agents 交換 policy 並調整行為。

這些工作仍然包含人工定義 cost／reward 或人工構造系統，因此仍屬 AFR 或 mechanism demonstration。

但它們證明一件對 NDR 極重要的事：

$$
\boxed{
\text{physical interaction graph}
\text{ can itself become a learned state variable}.
}
$$

也就是：

$$
R_t
\rightarrow
R_{t+1}
$$

可以直接由局部物理 learning rule 實現。

因此前一篇的：

$$
\text{causal restructuring}
$$

不一定需要一個中央數位處理器。

---

## 11. 第五個機制支點：適應與功能可以由物理閉環產生

Active matter 與 adaptive materials 顯示，sensor、internal dynamics 與 actuator 可以被整合在同一 physical system。

2025 年 Nature 的 adaptive active solids 展示了能在複雜環境中調整 locomotion 的 active material framework；其他 mechano-chemical adaptive materials 也已將 local sensing、chemical signal propagation 與 global mechanical response 整合起來。

這些同樣不是自然界自主生成的案例。

但它們讓下列機制成為已知物理可能：

$$
E
\rightarrow
X
\rightarrow
A
\rightarrow
E'.
$$

更強地：

$$
E
\rightarrow
X
\rightarrow
\Delta R
\rightarrow
A
\rightarrow
E'.
$$

因此：

$$
\boxed{
\text{closed-loop adaptive function}
}
$$

並不是神經元專屬的微觀機制。

這對 NDR 的 substrate-neutral 版本非常重要。

---

## 12. 從自組織到 NDR，中間至少還缺四道門

現有研究不能讓我們直接從：

$$
\text{self-organizing system}
$$

跳到：

$$
\text{AI-like functional system}.
$$

至少還缺：

### 第一，內生 readout

環境資訊必須被系統自己的 downstream variables 使用。

### 第二，功能閉合

資訊使用必須改變系統自身後續可達狀態，而不是只讓外部觀察者得到一個答案。

### 第三，適應性因果重組

系統必須能根據歷史結果改變：

$$
R,S,\Theta
$$

中的至少部分有效因果結構。

### 第四，持續與泛化

功能不能只在單一窄條件下瞬時出現，而需要：

$$
T>T_{\min}
$$

且面對某些未預設擾動時仍維持有效行為。

所以：

$$
\boxed{
\text{self-organization}
<
\text{information processing}
<
\text{adaptive functional closure}
<
\text{AI-like NDR candidate}
}
$$

是一個合理的證據階梯。

---

## 13. NDR 分級

本文提出：

### NDR-0：Natural Computational Richness

自然或自組織物理 dynamics 具有可被外部讀出的非線性計算能力。

這一層很弱。

### NDR-1：Natural Persistent Organization

在沒有 target-conditioned designer 的條件下形成持續結構或 dynamical regime。

### NDR-2：Natural Memory and History Dependence

系統的未來反應依賴：

$$
H_t
$$

而不只依賴當下 stimulus。

### NDR-3：Endogenous Functional Readout

系統內部有：

$$
X
\rightarrow
r_{\mathrm{endo}}
\rightarrow
A
$$

的因果鏈，使資訊改變自己的後續行為。

### NDR-4：Adaptive Causal Restructuring

歷史結果能造成：

$$
R_t
\rightarrow
R_{t+1}
$$

或：

$$
S_t
\rightarrow
S_{t+1},
$$

而且這種更新提高持續性、資源利用或任務相關表現。

### NDR-5：AI-like Autonomous Functional Organization

系統在非人工目標調參下，同時形成：

$$
\Psi_{\mathrm{AI}}
\succeq
\theta
$$

的多項能力，例如記憶、預測、適應、閉環控制、泛化與因果重組。

目前：

$$
\boxed{
\text{非生物自然界的 NDR-5 尚無可靠實證。}
}
$$

---

## 14. 生物版本與非生物版本必須分開

若把生命包含進去，「自然界能不能生成具有高階認知功能的系統？」幾乎會被現存生物直接回答。

動物與人類顯然是自然物理系統，而且 evolution 可以在沒有外部工程師指定最終神經架構的情況下形成高度複雜的認知功能。

但這會掩蓋本文真正有趣的問題。

因此定義：

$$
\mathrm{NDR}_{\mathrm{bio}}
$$

與：

$$
\mathrm{NDR}_{\mathrm{NB}},
$$

其中 NB 表示 non-biological / non-known-life-lineage。

真正開放的是：

$$
\boxed{
\mathrm{NDR}_{\mathrm{NB}}
\quad ?
}
$$

也就是：

> 是否存在不依靠已知生命譜系的自然物理系統，自行進入 AI-like functional class？

這可能涉及：

- non-biological chemical networks；
- plasma；
- electromagnetic / photonic structures；
- active matter；
- geological or atmospheric dynamical systems；
- 尚未知的自然 field–matter organizations。

目前沒有可靠證據證明其中任何一類已形成 AI-like autonomous functional organization。

---

## 15. 起源問題與「分子 bricolage」

自然生成不一定需要一步形成今天的完整功能。

2025 年對生命起源複雜 biochemical systems 的討論提出 molecular bricolage 視角：現代複雜機制中的組件可能最初為不同用途出現，之後被逐步整合成新的大型功能系統。

這對 NDR 非常重要。

因為自然路徑可以是：

$$
f_1
\rightarrow
f_1+f_2
\rightarrow
f_1+f_2+f_3
\rightarrow
F_{\mathrm{new}}.
$$

也就是：

$$
\boxed{
\text{complex function}
\text{ need not appear as a single coordinated novelty}.
}
$$

如果非生物 NDR 存在，它也可能依靠大量：

- exaptation-like reuse；
- modular accumulation；
- local persistence；
- hierarchical coupling；

逐步形成，而不是一次找到完整「AI architecture」。

---

## 16. 生成路徑的四種類型

為了避免所有「自然出現」被混成同一機率事件，本文至少區分四種 route。

### Route A：Self-organization

$$
z_0
\rightarrow
S.
$$

只形成結構。

### Route B：Dissipative Functional Organization

$$
z_0
\rightarrow
S
\rightarrow
\text{energy-supported functional cycle}.
$$

形成持續物理功能。

### Route C：Cumulative Adaptive / Selective Path

$$
z_0
\rightarrow
z_1
\rightarrow
\cdots
\rightarrow
z_n,
$$

而每一階段的 persistence、replication、performance 或 environmental filtering 改變下一階段 distribution。

這是最接近生物演化與長期自然學習的路線。

### Route D：Direct Fluctuation

$$
z_0
\xrightarrow{\mathrm{fluctuation}}
z^\star
\in
\mathcal F_\theta.
$$

幾乎直接生成終態。

Route D 就是下一篇與 Boltzmann brain 類問題最接近的情形。

本文 NDR 主要研究 A–C。

---

## 17. 路徑概率不能由終態複雜度直接推斷

一個高度複雜終態：

$$
z^\star
$$

可能看似極端 improbable。

但如果存在：

$$
\mathcal B(z^\star)
$$

而且大量不同初始狀態都會被 dynamics 推向同一 effective functional regime，那麼真正相關的不是：

$$
P(z=z^\star),
$$

而是：

$$
P
\left(
z_0\in\mathcal B(z^\star)
\right).
$$

反之，一個外觀看似簡單的系統也可能需要極端精細的初始條件才能維持高階功能。

所以：

$$
\boxed{
\text{morphological complexity}
\not\Rightarrow
\text{generative improbability}.
}
$$

真正要測的是：

- basin width；
- attraction rate；
- robustness；
- required free-energy flux；
- historical path dependence；
- environmental prevalence。

這把 NDR 變成可以由 dynamical-systems 與 statistical-physics 方法研究的問題。

---

## 18. Designer leakage：自然版本最需要避免的實驗錯誤

研究者很容易聲稱：

> 「我們讓物理系統自己學會了功能。」

但實際上可能：

1. 人選了最適合的材料；
2. 人選了 architecture；
3. 人定義 reward；
4. 人不停挑表現最好的樣本；
5. 人提供 labels；
6. 人訓練 readout；
7. 人只報告成功條件。

這會把大量 target information 注入系統。

因此可以概念性定義 designer leakage：

$$
\Lambda_{\mathrm{ext}}
=
I
\left(
\tau;
O_{\mathrm{ext}}
\mid
\mathcal L,\Omega
\right),
$$

表示外部操作中包含多少與目標 $\tau$ 相關的資訊。

這裡不主張實驗上已存在唯一標準的 mutual-information estimator；它是一個方法論提醒。

真正強的 NDR 候選應使：

$$
\Lambda_{\mathrm{ext}}
\rightarrow
0
$$

同時仍有：

$$
\Psi_{\mathrm{AI}}
\succeq
\theta.
$$

也就是：

> 減少設計者告訴系統「應該變成什麼」的資訊後，功能仍自行形成。

---

## 19. 如何研究 NDR，而不偷偷人工製造答案？

至少有三種路徑。

### 19.1 自然觀察

直接分析未經人工設計的：

- astrophysical；
- atmospheric；
- geological；
- chemical；
- ecological；

自然 systems。

優點是 designer leakage 低。

缺點是干預能力弱。

### 19.2 Minimal-bias physical ensemble

實驗室只設定廣泛物理條件，例如：

$$
\text{energy flux},
\text{material pool},
\text{boundary class},
$$

不針對特定 AI task 調參。

然後大規模觀察是否自發產生：

$$
M,A,C,R,\ldots
$$

等功能。

這不是純自然證據，但可以研究 basin 是否需要高度 target-specific design。

### 19.3 Generative physics simulation

對明確物理模型：

$$
\mathcal L
$$

建立初始條件 ensemble：

$$
p(z_0),
$$

讓系統不經 task-conditioned optimization 演化，再對結果做盲式功能篩查。

如果大量初始條件會自行進入同一 AI-like functional regime，就能提供 NDR 的理論支持。

但 simulation 的物理模型仍必須接受實驗驗證。

---

## 20. NDR 最強的證據不應是「看起來很複雜」

湍流、天氣、星際介質與化學波都可以：

$$
H(X)\gg0.
$$

這只能說 complexity 高。

更好的 NDR evidence 應逐步包含：

$$
\boxed{
\text{persistence}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{history-dependent information processing}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{endogenous readout}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{closed-loop causal action}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{adaptive causal restructuring}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\text{generalized AI-like functional organization}.
}
$$

這條階梯直接為第 5、6 篇的自然認知觀測問題鋪路。

---

## 21. 什麼結果會支持 NDR？

### 第一類：存在性模型

找到一個不含 target-conditioned external optimizer 的物理模型，使：

$$
\mathcal B_{\mathrm{NDR}}(\theta,T)
\neq
\varnothing.
$$

### 第二類：robust basin

不只一個精細初始點，而有：

$$
\mu
\left(
\mathcal B_{\mathrm{NDR}}
\right)
>0
$$

的實用 ensemble evidence。

### 第三類：內生 readout

資訊不是只被外部 observer 解碼，而實際進入：

$$
X
\rightarrow
A
\rightarrow
E'
$$

閉環。

### 第四類：自發 causal restructuring

在沒有外部 loss update 下，系統因歷史結果形成：

$$
R_t\rightarrow R_{t+1}
$$

且提高 future viability／functional performance。

### 第五類：跨環境泛化

功能不是只對單一固定條件，而能在新環境中維持。

如果一個非生物自然系統同時滿足這些條件，NDR 的證據會變得非常強。

---

## 22. 什麼結果會削弱強 NDR？

若廣泛搜尋後發現：

- self-organization 普遍存在，但不形成 endogenous readout；
- memory 普遍存在，但不能形成 adaptive action；
- adaptive behaviour 只在人工 reward 下出現；
- 功能 basin 極端窄，必須注入大量 target information；
- 所有高階候選都需要 biological evolution 或 engineered structure；

那麼：

$$
\mathrm{NDR}_{\mathrm{NB}}
$$

的強版本就會被削弱。

甚至可能得到：

$$
\boxed{
\text{physical multiple realizability is broad,}
\quad
\text{natural generability is narrow.}
}
$$

這本身也是重要科學結果。

---

## 23. 與 Boltzmann-type fluctuation 的接口

現在可以正式看到下一篇為何必須獨立。

NDR A–C 路線：

$$
z_0
\rightarrow
z_1
\rightarrow
\cdots
\rightarrow
z^\star.
$$

它需要研究：

$$
\mathcal B_{\mathrm{NDR}},
$$

即生成 basin。

Boltzmann-type direct fluctuation：

$$
z_0
\xrightarrow{\mathrm{rare\ fluctuation}}
z^\star.
$$

它主要研究：

$$
P(z^\star)
$$

或相應 fluctuation measure。

兩者即使得到相同終態：

$$
z^\star,
$$

其：

- causal history；
- probability measure；
- entropy cost；
- robustness；
- persistence；
- explanatory structure；

都完全不同。

所以：

$$
\boxed{
\text{same endpoint}
\not\Rightarrow
\text{same realization problem}.
}
$$

下一篇將專門研究這一點。

---

## 24. 結論：真正未知的是自然界有沒有進入功能類的「路」

人工物理計算已經告訴我們：

$$
\text{photons},
\text{electrons},
\text{mechanical modes},
\text{chemical states},
\text{electromagnetic scattering}
$$

都可以在適當人工約束下承載 AI-like functional transformations。

所以 substrate possibility 並不是這個問題最困難的部分。

真正未知的是：

$$
\boxed{
\text{自然動力是否會自行產生那些約束、關係、記憶、readout 與回授閉環？}
}
$$

本文將這個問題形式化為：

$$
\boxed{
\mathcal B_{\mathrm{NDR}}(\theta,T)
\stackrel{?}{\neq}
\varnothing
}
$$

以及更強的：

$$
\boxed{
\mu
\left(
\mathcal B_{\mathrm{NDR}}(\theta,T)
\right)
\stackrel{?}{>}
0.
}
$$

如果答案為是，則自然界不需要生成一個看起來像人腦、晶片或人工神經網路的物體。

它只需要形成：

$$
\boxed{
\text{與 AI-like 功能相容的關係—結構—動力等價類}.
}
$$

如果答案為否，則人工 functional realizability 與自然 generability 之間存在真正深刻的斷層。

目前科學能說的是：自組織、非平衡結構、化學資訊處理、物理學習、adaptive matter 等候選機制都已分別存在；但它們尚未被證明會在非生物、非人工自然系統中自行閉合成完整 AI-like functional organization。

因此 NDR 仍是一個真正開放的存在性問題。

下一篇將處理它的一個極端邊界版本：

> 如果自然界不走逐步生成路徑，而是由熱／量子／統計 fluctuation 直接產生足以具有指定功能的終態，這與 NDR 到底差在哪裡？

這將把 Boltzmann brain 從「奇怪的腦形思想實驗」重新定位成更一般的：

$$
\boxed{
\text{direct-state realization}
\quad\text{vs.}\quad
\text{path-generated realization}.
}
$$

---

## 參考文獻

1. Baltussen, M. G., de Jong, T. J., Duez, Q., Robinson, W. E., et al. (2024). “Chemical reservoir computation in a self-organizing reaction network.” *Nature*, 631, 549–555. DOI: 10.1038/s41586-024-07567-x.
2. Ji, X., Chen, Y., Yu, X., et al. (2026). “Making chemistry compute with non-steady-state chemical dynamics.” *Nature Reviews Chemistry*, 10, 92–94. DOI: 10.1038/s41570-026-00796-w.
3. Gershenson, C. (2025). “Self-organizing systems: what, how, and why?” *npj Complexity*, 2, 10. DOI: 10.1038/s44260-025-00031-5.
4. Singh, A., Parvin, P., Saha, B., et al. (2024). “Non-equilibrium self-assembly for living matter-like properties.” *Nature Reviews Chemistry*, 8, 723–740. DOI: 10.1038/s41570-024-00640-z.
5. Seelig, B., & Chen, I. A. (2025). “Intellectual frameworks to understand complex biochemical systems at the origin of life.” *Nature Chemistry*, 17, 11–19. DOI: 10.1038/s41557-024-01698-4.
6. Stern, M., Guzman, M., Martins, F., Liu, A. J., & Balasubramanian, V. (2025). “Physical Networks Become What They Learn.” *Physical Review Letters*, 134, 147402. DOI: 10.1103/PhysRevLett.134.147402.
7. Jung, G., Ozawa, M., & Bertin, E. (2025). “Kinetic Theory of Decentralized Learning for Smart Active Matter.” *Physical Review Letters*, 134, 248302.
8. Veenstra, J., Scheibner, C., Brandenbourger, M., et al. (2025). “Adaptive locomotion of active solids.” *Nature*, 639, 935–941. DOI: 10.1038/s41586-025-08646-3.
9. Samanta, A., Baranda Pellejero, L., Masukawa, M., et al. (2024). “DNA-empowered synthetic cells as minimalistic life forms.” *Nature Reviews Chemistry*, 8, 454–470. DOI: 10.1038/s41570-024-00606-1.
10. Eleveld, M. J., Geiger, Y., Wu, J., et al. (2025). “Competitive exclusion among self-replicating molecules curtails the tendency of chemistry to diversify.” *Nature Chemistry*, 17, 132–140. DOI: 10.1038/s41557-024-01664-0.

---

## 新系列進度

1. 關係、結構與功能：從單向決定論到耦合生成系統
2. 認知功能的跨基底實現：從神經元到光、電子與場
3. **自然動力認知實現命題：自然界能否自行生成 AI-like 功能體？**
4. 從波爾茲曼大腦到自然功能體：終態漲落與生成路徑的分離
5. 自然認知可觀測性問題：如何辨識非神經、非生物認知候選？
6. 秩序化因果結構能力：從複雜自然系統到候選認知功能體
