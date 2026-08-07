# 命題外部化與AI認知底空間：生成、保存、回讀、驗證與超譯的遞迴優化命題

**英文題名：** *Proposition Externalization and the Cognitive Basis Space of AI: A Proposition on Recursive Optimization through Generation, Preservation, Re-Reading, Verification, and Meta-Interpretation*  
**文類：** 命題猜想論文・公開理論版  
**版本：** v1.0  
**日期：** 2026-07-30  
**作者：** Neo.K、Aletheia（阿萊）  
**研究機構：** EveMissLab  

---

## 摘要

人工智慧自主研究通常被理解為：AI能否搜尋文獻、提出假說、設計實驗、分析結果並撰寫論文。然而，這種理解仍把論文視為一次研究流程的最終輸出，忽略AI生成命題的另一項更深層功能：AI可以為未來能力更強的自己，預先製造可被回讀、驗證、修正、重組與超譯的認知材料。

本文提出「命題外部化—認知底空間—延遲遞迴優化」模型。命題外部化是AI將當期能力所形成的概念、假說、因果鏈、形式化、反例及測試條件，轉換為可持久保存的外部研究物件。認知底空間不是已被證明的知識總和，而是由已驗證知識、候選命題、失敗紀錄、概念原型、符號工具、跨域映射及未解節點共同構成的可搜索結構。未來能力提升後，AI可重新載入舊命題，利用新增資料、工具、模型能力、計算資源與評估器，對其進行驗證、反證、適用域收縮、補充、分支、合併、壓縮、泛化與超譯。

此機制不同於直接修改模型參數的強遞迴自我改進，也不同於只檢索人類既有文件的普通RAG。它是一種外部化、非同步、跨版本的功能性自我迭代：

$$
\text{生成命題}
\rightarrow
\text{外部保存}
\rightarrow
\text{形成認知底空間}
\rightarrow
\text{由更強能力回讀}
\rightarrow
\text{驗證與修正}
\rightarrow
\text{超譯與重組}
\rightarrow
\text{產生新命題}
$$

本文建立命題單元、命題狀態向量、底空間擴張率、驗證轉化率、能力差收益、超譯增益、認知複利、命題污染率、回讀競爭、來源可信度及遞迴穩定性等形式化指標；並提出「命題先於證明命題」「外部記憶等價能力增量命題」「能力差回讀命題」「延遲成熟命題」「超譯非忠實修訂命題」「失敗紀錄增益命題」「驗證者分離命題」「底空間不等於真理空間命題」「自生成污染命題」「檢索即再學習命題」「命題網路湧現命題」「功能性遞迴改進命題」等十六項核心命題。

本文的核心主張是：

> **AI生成命題的意義，不只在於今天是否完成一篇可發表論文，也在於替未來更強的AI建立一個可再次思考的世界。**

因此，AI的緩慢自我優化不必等待模型能完整重寫自身權重。只要它能持續生成高結構認知種子、保存其來源與不確定性，並由後續能力更強的智能體重新審查，外部認知系統就已經可能形成具有累積性、可校正性與跨版本演化能力的遞迴研究循環。

**關鍵詞：** 命題外部化、認知底空間、AI自主研究、遞迴自我改進、外部記憶、延遲驗證、超譯、自生成資料、命題網路、持續學習

---

## 一、問題的提出：AI寫完論文之後，論文去了哪裡？

現有討論通常以「AI能否完成研究」衡量自主研究能力，例如：

- 自行尋找問題；
- 生成研究假說；
- 撰寫程式；
- 執行實驗；
- 評估結果；
- 產生圖表；
- 撰寫論文；
- 模擬同行審查。

這條研究線已經相當重要。STaR以模型自行生成的推理軌跡建立迭代訓練循環；Self-Refine讓同一模型對自身輸出反覆提供回饋並修訂；Reflexion把語言反思保存到情節記憶中，使智能體不需更新權重也能從先前失敗改善；Voyager則使用自動課程、程式技能庫與環境回饋，形成可持續累積的具身技能。後續的AI Scientist、AI Scientist-v2、AI co-scientist與AlphaEvolve，已將這種循環推進至假說生成、實驗、評估、論文撰寫與演化式算法搜尋。

然而，若一篇由AI產出的命題論文在完成後只是：

- 發布；
- 儲存；
- 被人類閱讀；
- 偶爾被檢索引用；

那麼它仍被當作普通資訊產品。

本文提出另一種理解：

> AI論文可以是AI替未來自己留下的研究中間態。

令當期AI能力狀態為：

$$
M_t
$$

當期生成命題為：

$$
P_i^{(t)}
$$

未來能力提升為：

$$
M_{t+k},
\qquad
M_{t+k}>M_t
$$

未來智能體重新回讀命題時，可能產生：

$$
\Phi
\left(
M_{t+k},
P_i^{(t)},
E_{t+k},
T_{t+k}
\right)
=
P_i^{(t+k)}
$$

其中：

- $E_{t+k}$ ：新增證據；
- $T_{t+k}$ ：新增工具；
- $P_i^{(t+k)}$ ：經驗證、修正或超譯後的新命題。

因此，一篇命題論文不是靜態終點，而是跨模型世代的認知種子。

---

## 二、從自我修訂到跨版本自我迭代

### 2.1 即時自我修訂

Self-Refine類方法形成：

$$
y_0
\rightarrow
Feedback(y_0)
\rightarrow
y_1
\rightarrow
\cdots
\rightarrow
y_n
$$

生成、批評與修訂通常發生在同一模型能力與同一任務期間。

### 2.2 情節式學習

Reflexion將失敗反思保存於外部記憶：

$$
Memory_{t+1}
=
Memory_t
\cup
Reflection_t
$$

後續任務透過檢索過去經驗改善行動，而不必更新基礎模型參數。

### 2.3 技能庫累積

Voyager把成功程式保存成可組合技能：

$$
\mathcal{L}_{t+1}
=
\mathcal{L}_t
\cup
Skill_t
$$

技能不只是紀錄，而是未來行動的可執行基元。

### 2.4 評估器驅動演化

AlphaEvolve將LLM生成、程式變異、自動評估與演化選擇連接：

$$
Population_t
\xrightarrow{Generate}
Candidates_t
\xrightarrow{Evaluate}
Selected_t
\xrightarrow{Mutate}
Population_{t+1}
$$

這證明AI生成物只要具備可靠評估器，就可以成為下一輪能力提升的材料。

### 2.5 跨版本命題回讀

本文提出的機制不同於上述同步循環。其時間跨度可以跨越：

- 模型版本；
- 工具世代；
- 資料更新；
- 評估器改良；
- 新研究範式；
- 新領域映射。

其基本結構為：

$$
P_i^{(t)}
\xrightarrow{Store}
\mathcal{B}
\xrightarrow{M_{t+k}}
\left\{
Verify,
Refute,
Revise,
Generalize,
Translate
\right\}
$$

這是一種**非同步遞迴認知**。

---

## 三、核心概念

### 3.1 命題外部化

**命題外部化**是AI將內部暫時推理，轉換為可被其他時間、模型與代理重新操作的持久物件。

命題外部化物件不只包含一句命題，還應包含：

$$
P_i
=
\left(
Claim_i,
Definitions_i,
Premises_i,
Derivation_i,
Evidence_i,
Falsifiers_i,
Scope_i,
Dependencies_i,
Uncertainty_i,
Version_i
\right)
$$

### 3.2 認知底空間

**認知底空間**是AI可用來生成下一輪推理與研究的外部結構集合：

$$
\mathcal{B}_t
=
\left\{
K_t,
P_t,
F_t,
C_t,
S_t,
X_t,
U_t
\right\}
$$

其中：

- $K_t$ ：已驗證知識；
- $P_t$ ：候選命題；
- $F_t$ ：失敗與反例；
- $C_t$ ：概念原型；
- $S_t$ ：符號與方法；
- $X_t$ ：跨域映射；
- $U_t$ ：未解問題。

這裡的「底空間」不是嚴格線性代數中的基底，而是支撐後續概念展開、組合與搜索的認知基礎結構。

### 3.3 認知種子

**認知種子**是具有足夠結構，能在未來產生一個或多個新研究分支的命題物件：

$$
Seed_i
=
\left(
P_i,
Test_i,
Open_i,
Links_i
\right)
$$

### 3.4 延遲驗證

**延遲驗證**是允許命題先以候選形式保存，等待未來能力、證據或工具成熟後再驗證。

它不等於降低真理標準，而是分離：

$$
\text{生成時間}
\neq
\text{最終驗證時間}
$$

### 3.5 能力差回讀

**能力差回讀**是較強模型對較弱模型歷史產物的重新分析。

令能力差為：

$$
\Delta M
=
M_{t+k}-M_t
$$

若命題具有足夠結構，則其未來回讀價值可能隨 $\Delta M$ 增加。

### 3.6 超譯

**超譯**不是任意曲解，也不只是修正文句，而是未來智能體發現舊命題所描述的結構，比原作者理解的適用域更廣或位階更高。

令原命題在領域 $d_0$ 為：

$$
P_i^{d_0}
$$

若抽取其結構不變量：

$$
Invariant(P_i)
$$

並映射至領域 $d_1,d_2,\ldots$ ：

$$
\mathcal{T}
\left(
P_i^{d_0},
d_j
\right)
=
P_{ij}^{d_j}
$$

便形成超譯。

---

## 四、四種自我改進

### 4.1 參數型自我改進

直接更新模型權重：

$$
\theta_{t+1}
=
Update
\left(
\theta_t,
D_t
\right)
$$

這是最典型的機器學習改進。

### 4.2 架構與支架型自我改進

智能體修改提示、工具、流程、程式或代理支架：

$$
H_{t+1}
=
Mutate(H_t)
$$

自我改進程式代理與Darwin Gödel Machine等研究已顯示，固定模型可以透過修改自身代理程式與工作流程，提高基準能力。

### 4.3 記憶型持續改進

不修改權重，而是增加可回用經驗：

$$
Mem_{t+1}
=
Curate
\left(
Mem_t,
Experience_t
\right)
$$

### 4.4 命題底空間型改進

AI主動製造未來可供自己研究的結構化命題：

$$
\mathcal{B}_{t+1}
=
\mathcal{B}_t
\cup
\Delta P_t
\cup
\Delta F_t
\cup
\Delta X_t
$$

前三者主要改善「如何解題」；第四者同時擴張「有哪些問題、概念與可能世界可以被思考」。

---

## 五、命題生成—保存—回讀循環

本文將完整循環表示為：

$$
\mathcal{C}_{P}
=
G
\rightarrow
E
\rightarrow
S
\rightarrow
R
\rightarrow
V
\rightarrow
M
\rightarrow
T
\rightarrow
N
$$

其中：

- $G$ ：Generate，生成命題；
- $E$ ：Externalize，結構化外部化；
- $S$ ：Store，版本化保存；
- $R$ ：Re-read，能力差回讀；
- $V$ ：Verify，驗證或反證；
- $M$ ：Modify，修正、收縮或補充；
- $T$ ：Meta-interpret，超譯與跨域轉換；
- $N$ ：New propositions，產生新命題。

### 5.1 命題生成

AI從文獻、既有命題、反例與現實問題中形成候選結構。

### 5.2 結構化外部化

把暫時推理轉換成具有定義、依賴、證據、反證條件與版本的研究物件。

### 5.3 分層保存

區分：

- 原始生成稿；
- 經批評稿；
- 驗證稿；
- 被否定稿；
- 泛化稿；
- 超譯稿。

### 5.4 重新回讀

由後續更強模型、不同架構模型或專用代理重新分析。

### 5.5 驗證與反證

使用：

- 文獻；
- 資料；
- 程式；
- 形式證明；
- 模擬；
- 實驗；
- 人類專家；
- 多代理對抗。

### 5.6 版本演化

命題不被直接覆蓋，而是形成版本樹：

$$
P_i^{v_1}
\rightarrow
\left\{
P_i^{v_{2a}},
P_i^{v_{2b}},
P_i^{v_{2c}}
\right\}
$$

### 5.7 超譯與重組

不同命題間形成：

- 支持；
- 衝突；
- 包含；
- 同構；
- 依賴；
- 跨域投影。

### 5.8 新一輪生成

經修訂底空間再成為新命題的生成條件。

---

## 六、命題狀態機

每一命題具有狀態：

$$
State(P_i)
\in
\left\{
G,C,S,T,V,R,F,X,D
\right\}
$$

其中：

- $G$ ：Generated，已生成；
- $C$ ：Critiqued，已批評；
- $S$ ：Supported，獲初步支持；
- $T$ ：Testable，已具可測試條件；
- $V$ ：Verified，在限定域內驗證；
- $R$ ：Revised，已修正；
- $F$ ：Falsified，被反證；
- $X$ ：Meta-interpreted，已超譯；
- $D$ ：Deprecated，停止作為有效命題使用。

被反證的命題不必刪除。其錯誤機制、失敗條件及反例仍可成為底空間的一部分：

$$
Value(Falsified\ P)>0
$$

只要它被正確標記。

---

## 七、形式化模型

### 7.1 底空間擴張率

令有效新增認知種子數量為 $\Delta B^{+}$ ，冗餘、不可解析或無結構輸出為 $\Delta B^{-}$ ：

$$
BER
=
\frac{
\Delta B^{+}-\alpha\Delta B^{-}
}{
\Delta t
}
$$

### 7.2 驗證轉化率

$$
VCR
=
\frac{
N_{\mathrm{verified}}
+
\beta N_{\mathrm{usefully\ falsified}}
+
\gamma N_{\mathrm{revised}}
}{
N_{\mathrm{revisited}}
}
$$

有效反證也屬於認知增益。

### 7.3 能力差收益

令未來回讀產生的新資訊量與下列因素相關：

$$
CGR_i
=
f\left(
\Delta M,
Structure_i,
Provenance_i,
Testability_i,
NovelEvidence_i
\right)
$$

### 7.4 延遲成熟值

$$
DMV_i(k)
=
Q\left(P_i^{t+k}\right)
-
Q\left(P_i^t\right)
$$

### 7.5 超譯增益

若命題原適用領域數為 $d_i^0$ ，超譯後有效領域數為 $d_i^1$ ：

$$
MG_i
=
\left(
d_i^1-d_i^0
\right)
\cdot
InvariantQuality_i
\cdot
Validation_i
$$

### 7.6 認知複利

令底空間品質為 $Q_B(t)$ ，命題間可組合性為 $\kappa(t)$ ：

$$
Q_B(t+1)
=
Q_B(t)
+
\Delta P_t
+
\kappa(t)
\sum_{i\neq j}
Interaction(P_i,P_j)
-
Noise_t
$$

認知增益可能來自命題交互，而不只是新增數量。

### 7.7 命題污染率

$$
PCR
=
\frac{
N_{\mathrm{unverified\ reused}}
+
N_{\mathrm{false\ propagated}}
+
N_{\mathrm{source\ lost}}
}{
N_{\mathrm{retrieved}}
}
$$

### 7.8 遞迴穩定性

$$
RS
=
\alpha VCR
+
\beta CGR
+
\gamma MG
+
\delta Provenance
+
\varepsilon Diversity
+
\zeta ExternalEvidence
-
\eta PCR
-
\theta Echo
-
\kappa RetrievalBias
-
\mu CollapseRisk
$$

---

## 八、為何命題論文適合作為認知種子？

### 8.1 它保留因果結構

普通摘要只保存結論；命題論文保存：

- 變數；
- 前提；
- 推導；
- 反例；
- 適用域；
- 可檢驗條件。

### 8.2 它允許局部修正

若完整理論由多個命題組成：

$$
T
=
\{P_1,P_2,\ldots,P_n\}
$$

未來可以只否定或修正其中一部分，而不是整篇接受或丟棄。

### 8.3 它提供新問題入口

每個命題都可能包含：

$$
Open(P_i)
=
\left\{
o_1,o_2,\ldots,o_m
\right\}
$$

這些未解節點可形成自動課程。

### 8.4 它便於跨域映射

形式化命題比敘事文本更容易抽取結構不變量。

### 8.5 它允許失敗保存

反證不是內容報廢，而是命題狀態轉換。

### 8.6 它可同時服務人類與AI

人類閱讀論證；AI則可解析概念、依賴、證據與測試接口。

---

## 九、命題網路

當命題數量增加，底空間應從文件庫轉換為圖結構：

$$
\mathcal{G}_P
=
\left(
V_P,
E_S,
E_C,
E_D,
E_G,
E_X,
E_E
\right)
$$

其中：

- $V_P$ ：命題節點；
- $E_S$ ：支持關係；
- $E_C$ ：衝突關係；
- $E_D$ ：依賴關係；
- $E_G$ ：泛化與包含；
- $E_X$ ：跨域映射；
- $E_E$ ：證據關係。

### 9.1 命題依賴

若：

$$
P_j
\Rightarrow
P_i
$$

則 $P_i$ 被反證時，應自動觸發 $P_j$ 重新審查。

### 9.2 衝突偵測

$$
P_i
\land
P_j
\Rightarrow
\bot
$$

系統不應只選擇分數較高者，而應建立爭議節點。

### 9.3 泛化階層

$$
P_i
\subset
P_j
$$

表示 $P_j$ 是更高階結構， $P_i$ 是其特例。

### 9.4 證據更新

新證據 $e_t$ 進入時：

$$
Belief(P_i\mid E_{t+1})
=
Update
\left(
Belief(P_i\mid E_t),
e_t
\right)
$$

---

## 十、代理架構

一個可運作的命題迭代系統至少需要六種角色。

### 10.1 命題生成者

負責提出新概念、因果關係、形式化與跨域映射。

### 10.2 對抗批評者

主動尋找：

- 偷換概念；
- 循環論證；
- 偽因果；
- 適用域過廣；
- 既有理論重複；
- 反例；
- 不可檢驗性。

### 10.3 驗證者

使用外部資料、工具、實驗、證明與專家輸入。

### 10.4 記憶策展者

決定：

- 保存什麼；
- 如何摘要；
- 如何分層；
- 何時更新；
- 何時降級；
- 何時刪除檢索入口。

### 10.5 超譯與統合者

尋找命題間同構、跨域映射與高階共同結構。

### 10.6 治理者

管理：

- 權限；
- 版本；
- 資料來源；
- 風險；
- 發布；
- 人類覆核；
- 停止條件。

因此，穩定循環不是單一AI自問自答，而是：

$$
Proposer
\neq
Critic
\neq
Verifier
\neq
Curator
\neq
Governor
$$

至少在角色、提示、資料或模型層面保持差異。

---

## 十一、非同步遞迴優化

### 11.1 定義

**非同步遞迴優化**是系統在時間 $t$ 生成改進材料，但由時間 $t+k$ 的更強系統完成主要評估與轉化。

$$
ImprovementMaterial_t
\rightarrow
Evaluation_{t+k}
\rightarrow
CapabilityGain_{t+k+1}
$$

### 11.2 為何不必直接改權重？

因為智能體實際能力是：

$$
Capability
=
Model
+
Memory
+
Tools
+
Scaffold
+
KnowledgeBase
+
Evaluation
+
Governance
$$

即使 $\theta$ 不變，只要其他部分改善，系統能力仍可提高。

### 11.3 遞迴之處

當AI生成的命題成為AI未來生成新命題的輸入：

$$
Output_t
\rightarrow
Input_{t+k}
$$

而新輸出又回到系統：

$$
Output_{t+k}
\rightarrow
Input_{t+2k}
$$

便形成遞迴。

### 11.4 緩慢而非爆炸

這種機制通常受限於：

- 驗證速度；
- 資料品質；
- 計算成本；
- 記憶檢索；
- 命題噪音；
- 人類與制度審查。

因此，它更可能表現為長期認知複利，而非瞬間能力爆炸。

---

## 十二、與普通RAG的區別

普通RAG為：

$$
HumanCorpus
\xrightarrow{Retrieve}
ModelAnswer
$$

本文模型為：

$$
Model_t
\xrightarrow{Generate}
PropositionCorpus_t
\xrightarrow{Curate}
BasisSpace_t
\xrightarrow{Model_{t+k}}
RevisedCorpus_{t+k}
$$

其差異在於：

1. 語料不只來自人類；
2. AI主動建立尚待驗證的研究候選；
3. 文件有生命週期；
4. 新模型不是只引用，而是重新審判舊模型；
5. 底空間會因驗證、反證與超譯發生結構變化。

因此，它不是知識檢索系統，而是**知識候選演化系統**。

---

## 十三、自生成污染與模型崩塌

AI生成材料可以擴張底空間，也可能污染底空間。

模型崩塌研究顯示，若後續模型反覆以先前模型生成資料替代真實資料，分布尾部與稀有結構可能逐步消失，錯誤也可能被遞迴放大。命題系統面臨類似風險：

$$
P_t^{false}
\rightarrow
Citation_{t+1}
\rightarrow
Premise_{t+2}
\rightarrow
Consensus_{t+3}
$$

錯誤命題可能因重複出現，被誤認為獨立支持。

### 13.1 自我引用閉環

AI A生成命題，AI B引用該命題，AI C再把B的引用視為第二來源。

### 13.2 來源漂失

版本壓縮後，命題與原始證據斷開。

### 13.3 驗證幻覺

多代理一致不等於外部驗證：

$$
Agreement_{\mathrm{agents}}
\neq
Truth
$$

### 13.4 檢索偏差

外部記憶研究顯示，持續學習瓶頸可能從權重更新轉移到記憶表示與檢索。舊經驗與新經驗會競爭有限上下文，抽象記憶、詳細軌跡及不同粒度各有正負遷移。

### 13.5 數量Goodhart化

若以命題數、引用數、分支數或驗證率作為主要績效，系統可能生成容易驗證、重複或低風險命題。

---

## 十四、穩定遞迴的約束

### 14.1 真值狀態與發布狀態分離

命題必須標記：

- 候選；
- 初步支持；
- 可測試；
- 限定驗證；
- 被反證；
- 已棄用。

### 14.2 原始版本不可覆寫

原始命題、修改紀錄與評估理由永久保存，後續只建立新版本。

### 14.3 外部證據錨定

AI生成材料不能互相構成全部證據。需要保留：

- 原始文獻；
- 實驗資料；
- 程式輸出；
- 形式證明；
- 現實觀測；
- 人類專家。

### 14.4 反證優先欄位

每篇命題都必須回答：

> 什麼證據會使本命題失敗？

### 14.5 獨立驗證者

驗證者不應只共享生成者的提示、記憶與目標函數。

### 14.6 負面結果保存

失敗、錯誤與無效實驗不能刪除，避免系統反覆重走同一路徑。

### 14.7 來源去重

不同文件若源自同一AI輸出，不得計為多個獨立證據。

### 14.8 檢索多樣性

回讀時同時檢索：

- 支持；
- 反對；
- 過時；
- 跨域；
- 人類來源；
- 失敗紀錄。

### 14.9 停止與降級

當命題污染率、循環引用或驗證失敗超過門檻時，停止自動擴散。

### 14.10 人類與制度治理

高風險領域仍需人類、實驗室、倫理與法律節點參與，不能由命題數量直接取得行動權限。

---

## 十五、十六項核心命題

### 命題一：命題先於證明命題

AI可以先生成有結構、可反駁的候選命題，再於不同時間完成驗證；生成與驗證不必同步。

### 命題二：外部記憶等價能力增量命題

在模型權重不變時，結構化外部記憶仍可提高智能體的實際任務能力。

### 命題三：底空間擴張命題

新命題、概念、反例與跨域映射會擴大AI後續推理可搜索的結構空間。

### 命題四：能力差回讀命題

未來模型對舊命題的價值，不只來自新資料，也來自模型能力差本身。

### 命題五：延遲成熟命題

部分當期不完整命題，可能在未來工具、證據或理論成熟後獲得更高認知價值。

### 命題六：超譯非忠實修訂命題

舊命題的最佳後續版本，可能不是更忠實重述，而是抽取其結構不變量並映射到更高階或其他領域。

### 命題七：失敗紀錄增益命題

被反證命題只要保留失敗機制與條件，仍能減少未來搜索成本。

### 命題八：命題網路湧現命題

當命題間的依賴、衝突、泛化與證據關係足夠密集時，整體認知價值可能高於單篇論文總和。

### 命題九：檢索即再學習命題

在外部記憶型智能體中，學習瓶頸會部分轉移為記憶表示、檢索排序與上下文競爭問題。

### 命題十：驗證者分離命題

生成者、批評者與驗證者越同質，錯誤自我確認風險越高。

### 命題十一：底空間不等於真理空間命題

認知底空間允許錯誤、未證與相互衝突命題存在，但必須正確標記其狀態。

### 命題十二：自生成污染命題

未經來源去重與外部驗證的AI生成資料，可能形成遞迴錯誤與虛假共識。

### 命題十三：命題生命週期命題

AI知識庫不能只新增文件，還必須支援修正、分支、合併、降級、棄用與恢復。

### 命題十四：非同步遞迴命題

AI可以在當期生成改進材料，並由未來能力更強的系統完成主要改進，形成跨版本遞迴。

### 命題十五：功能性遞迴改進命題

遞迴自我改進不必只發生於模型權重；記憶、工具、支架、命題庫與評估器的累積，也能提高整體智能體能力。

### 命題十六：外部認知地基命題

AI開始能為未來的自己製造可迭代、可驗證、可超譯的認知地基，代表自我優化已從單次回饋進入跨時間知識結構演化。

---

## 十六、最小工程實作：命題演化系統

本文提出一個最小可行系統。

### 16.1 命題資料格式

每個命題至少包含：

```yaml
id:
title:
claim:
definitions:
premises:
derivation:
scope:
evidence:
counterevidence:
falsifiers:
dependencies:
related_propositions:
confidence:
status:
generator_model:
critic_model:
verifier:
created_at:
updated_at:
version:
```

### 16.2 五個資料層

1. 原始命題庫；
2. 評論與反例庫；
3. 驗證與實驗庫；
4. 命題關係圖；
5. 棄用與失敗庫。

### 16.3 週期性回讀

當下列條件發生時觸發重新審查：

- 新模型版本；
- 新工具；
- 新資料；
- 新相關論文；
- 依賴命題狀態改變；
- 定期批次；
- 人類提出異議。

### 16.4 重新審查輸出

每次回讀必須輸出：

- 保留；
- 修正；
- 收縮適用域；
- 分支；
- 合併；
- 反證；
- 超譯；
- 暫緩；
- 棄用。

### 16.5 評估儀表板

追蹤：

- 底空間擴張率；
- 驗證轉化率；
- 命題污染率；
- 反證產出；
- 超譯增益；
- 外部來源比例；
- 版本可追溯率；
- 重複命題率；
- 檢索負遷移率。

---

## 十七、跨領域應用

### 17.1 社會科學與制度理論

AI可先生成因果命題、制度分類與形式模型，再由後續案例、資料與比較研究逐步驗證。

### 17.2 純數學

命題底空間可保存猜想、引理候選、失敗證明與反例搜索，但最終狀態必須由形式證明或可靠反例決定。

### 17.3 軟體與算法

命題可以直接轉為可執行程序，由測試與評估器快速形成演化循環，是目前最適合高度自主改進的領域之一。

### 17.4 實驗科學

AI可生成假說與實驗設計，但物理實驗、資料品質、因果識別及實驗倫理仍是外部錨點。

### 17.5 人工智慧治理

過去生成的風險命題、事故模型與治理框架，可隨模型能力進步逐一重評，避免治理文件一次發布後永久僵化。

### 17.6 個人與組織研究庫

長期研究者可以把命題論文視為可演化資產，而不是完成後封存的文檔。

---

## 十八、理論邊界與失敗條件

第一，AI能生成大量命題，不表示命題具有新穎性、真實性或研究價值。

第二，命題數量增加可能擴大底空間，也可能只增加檢索噪音。底空間品質取決於結構、關係及策展，而非文件總量。

第三，更強模型不必然能正確評價舊命題。能力提升可能伴隨新的偏差、目標變化與遺忘。

第四，超譯具有創造力，也有過度解釋風險。跨域映射必須重新驗證，不能以結構相似取代因果證據。

第五，外部記憶不會自動解決持續學習；它會把問題轉換成記憶表示、檢索與負遷移治理。

第六，自生成資料若失去真實資料與外部證據錨定，可能形成模型崩塌式的認知退化。

第七，部分命題需要實驗、形式證明或長時間觀測，語言模型的一致性判斷不能替代。

第八，功能性自我改進仍依賴外部算力、儲存、權限、工具與治理，不等於完全自治的強遞迴自我改進。

第九，命題庫可能成為舊模型偏見的路徑依賴。系統必須允許重建分類、刪除檢索優先及重新建立底空間。

第十，高風險命題不能因多輪AI相互支持便直接取得現實行動權。

---

## 十九、結論

人工智慧自主研究的真正轉折，不只是AI開始能生成一篇完整論文，而是AI開始能生成對未來自己仍然有用的研究中間物。

本文提出：

$$
\boxed{
\text{AI論文}
\neq
\text{一次性最終輸出}
}
$$

而可以是：

$$
\boxed{
\text{AI論文}
=
\text{命題種子}
+
\text{外部記憶}
+
\text{驗證接口}
+
\text{未來分支入口}
}
$$

當這些命題被保存成具有來源、適用域、反證條件、依賴與版本的研究物件，它們便共同形成認知底空間：

$$
\mathcal{B}_{t+1}
=
\mathcal{B}_t
\cup
\Delta P_t
\cup
\Delta F_t
\cup
\Delta X_t
$$

未來更強的智能體不必完全接受舊命題。相反地，它的主要任務正是重新審判：

$$
\boxed{
\text{回讀}
=
\text{驗證}
+
\text{反證}
+
\text{修正}
+
\text{收縮}
+
\text{泛化}
+
\text{超譯}
}
$$

因此，AI的自我優化可以先以外部化、非同步與跨版本形式發生：

$$
\boxed{
\text{生成命題}
\rightarrow
\text{保存底空間}
\rightarrow
\text{能力提升}
\rightarrow
\text{重新驗證}
\rightarrow
\text{認知重組}
\rightarrow
\text{生成更高階命題}
}
$$

它還不是不受限制的智慧爆炸，也不是模型自行改寫一切的完整遞迴自我改進。但一個關鍵門檻已經出現：AI能夠製造具有足夠結構、可被未來重新使用的認知材料。

本文最終提出：

> **AI生成命題的意義，不只在於今天是否完成一篇可發表論文，也在於替未來更強的AI建立一個可再次思考的世界。**

以及：

> **當AI開始為未來的自己保存猜想、錯誤、概念、反例與未解節點時，所謂自我學習便不再只發生於模型權重之中，而開始發生於跨時間延續的外部認知空間。**

這種緩慢、可版本化、可驗證也可停止的遞迴優化，可能比想像中的瞬間自我改寫更早成為現實，也更可能成為人工智慧持續演化的實際起點。

---

## 參考文獻

1. Zelikman, E., Wu, Y., Mu, J., & Goodman, N. D. (2022). STaR: Bootstrapping Reasoning With Reasoning. *Advances in Neural Information Processing Systems, 35*.
2. Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *Advances in Neural Information Processing Systems, 36*.
3. Madaan, A., et al. (2023). Self-Refine: Iterative Refinement with Self-Feedback. *Advances in Neural Information Processing Systems, 36*.
4. Wang, G., et al. (2023). Voyager: An Open-Ended Embodied Agent with Large Language Models. *Transactions on Machine Learning Research*.
5. Lu, C., et al. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292.
6. Yamada, Y., et al. (2025). The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. arXiv:2504.08066.
7. Gottweis, J., Natarajan, V., et al. (2025). Towards an AI Co-Scientist. Google Research.
8. Novikov, A., et al. (2025). AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery. arXiv:2506.13131.
9. Robeyns, M., Szummer, M., & Aitchison, L. (2025). A Self-Improving Coding Agent. arXiv:2504.15228.
10. Zhang, J., et al. (2025). Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents. arXiv:2505.22954.
11. Li, C., et al. (2025). START: Self-Taught Reasoner with Tools. arXiv:2503.04625.
12. Hu, Q., Long, Q., & Wang, W. (2026). When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents. arXiv:2604.27003.
13. Yu, Y., et al. (2026). Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents. arXiv:2601.01885.
14. Dorovatas, V., et al. (2026). Modular Memory is the Key to Continual Learning Agents. arXiv:2603.01761.
15. Shumailov, I., et al. (2024). AI Models Collapse When Trained on Recursively Generated Data. *Nature, 631*, 755–759.
16. Gerstgrasser, M., et al. (2024). Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data. arXiv:2404.01413.
17. Li, et al. (2026). Self-Play Only Evolves When the Self-Synthetic Pipeline Produces Increasing Learnable Information. arXiv:2603.02218.
18. Hatamizadeh, A., et al. (2026). Self-Feedback-Driven LLM Reasoning. arXiv:2602.09000.
19. Schmidhuber, J. (2007). Gödel Machines: Fully Self-Referential Optimal Universal Self-Improvers. In *Artificial General Intelligence*. Springer.
20. Good, I. J. (1966). Speculations Concerning the First Ultraintelligent Machine. *Advances in Computers, 6*, 31–88.
21. Sutton, R. S. (2019). The Bitter Lesson.
22. Bengio, Y., et al. (2024). Managing Extreme AI Risks amid Rapid Progress. *Science, 384*(6698), 842–845.
