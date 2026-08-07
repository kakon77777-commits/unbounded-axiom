# 能力增長條件式自主迭代生成：跨模型世代命題生命線、逆向回讀與AI認知演化命題

**英文題名：** *Capability-Growth-Conditioned Autonomous Iterative Generation: A Proposition on Cross-Model Proposition Lineages, Retroactive Re-Reading, and AI Cognitive Evolution*  
**縮寫：** CCAIG（Capability-Conditioned Autonomous Iterative Generation）  
**文類：** 命題猜想論文・公開理論版  
**版本：** v1.0  
**日期：** 2026-07-30  
**作者：** Neo.K、Aletheia（阿萊）  
**研究機構：** EveMissLab  

---

## 摘要

人工智慧的遞迴改進經常被描述為AI直接修改自身模型權重、訓練程序或程式碼，進而形成加速式能力提升。然而，這種描述容易遮蔽一個較早出現、限制較明確、卻已具有實際可行性的形態：在能夠判定AI系統於特定能力維度持續提升的條件下，AI可以自主生成具有結構、版本、反證條件與延伸接口的命題，將其保存為跨模型世代延續的研究生命線，再由後續能力更高的AI重新回讀、驗證、修正、補充、分支、合併與超譯，形成部分領域中的自主迭代生成。

本文提出「能力增長條件式自主迭代生成」（CCAIG）模型。CCAIG不假設整體智能必然單調上升，也不把模型名稱更新等同能力進步，而要求透過任務特定、保留集、跨版本與外部證據評測，確認後續AI系統在與某一命題相關的能力向量上跨越重啟門檻。只有當能力提升可被判定，舊命題生命線才進入重新迭代。

本文區分外生能力提升與內生認知迭代。外生提升來自新模型、新工具、新算力、新資料、長上下文、記憶及檢索技術；內生迭代則由AI自主生成命題、保存失敗、建立依賴、設計測試、重新審判舊命題並產生後繼版本。兩者耦合後形成：

$$
\text{跨代自主迭代}
=
\text{可判定的能力增長}
\times
\text{可持久的認知生命線}
\times
\text{可校正的驗證機制}
$$

本文建立系統能力向量、領域適格度、能力差觸發函數、命題生命線、逆向回讀增益、後繼命題距離、保留集安全閘門、迭代自治度、超譯增益、污染傳播率、評估器俘獲與條件式遞迴穩定性等形式化指標，並提出十八項核心命題。

本文的核心主張是：

> **AI不必先具備完整的自我重寫能力，才開始自主迭代。只要AI能力提升可以被判定，且舊命題被保存為可驗證、可分支、可回滾的生命線，某些AI生成活動便已能跨模型世代形成條件式自主認知演化。**

這種演化不是無條件、全領域或必然單調的智慧爆炸，而是一種局部、分層、可中止、依賴評估器與外部證據的跨代研究迭代。

**關鍵詞：** 自主迭代生成、能力增長、跨模型世代、命題生命線、逆向回讀、AI自主研究、外部記憶、自我演化智能體、條件式遞迴改進、超譯

---

## 一、問題的重新界定：不是AI是否已經完全自我改進

討論AI自我改進時，常出現兩個極端判斷。

第一個判斷認為，只要AI尚不能獨立重訓基礎模型、修改全部權重與控制自身算力，它就尚未具備任何真正的自我迭代。

第二個判斷則把任何自我反思、連續提示或反覆生成，都直接描述成遞迴自我改進。

兩者都過於粗略。

本文關心的不是：

$$
\text{AI是否已完全自我改寫}
$$

而是：

$$
\boxed{
\text{哪些AI生成物，已經可以成為後續更強AI的自主迭代材料？}
}
$$

以及：

$$
\boxed{
\text{在何種可判定能力提升條件下，迭代可以被合法重新啟動？}
}
$$

令時間 $t$ 的AI系統為：

$$
\mathcal{A}_t
=
\left(
M_t,
T_t,
R_t,
K_t,
H_t,
E_t,
G_t
\right)
$$

其中：

- $M_t$ ：基礎模型；
- $T_t$ ：可用工具；
- $R_t$ ：檢索與外部記憶；
- $K_t$ ：上下文與知識庫；
- $H_t$ ：代理支架與工作流；
- $E_t$ ：評估器；
- $G_t$ ：治理與權限。

系統能力不等於模型能力：

$$
Capability(\mathcal{A}_t)
\neq
Capability(M_t)
$$

即使模型權重不變，工具、記憶、工作流與評估器改善，也可能使智能體在特定任務上顯著進步。

因此，本文所說的「AI智能持續提升」，應理解為：

> AI系統在一個或多個可測量、與目標命題相關的能力維度上，經過外部或保留集評估後顯示有效提升。

它不是一項信仰，而是一項需要被持續重新判定的條件。

---

## 二、現有技術訊號

### 2.1 同一模型的即時修訂

Self-Refine顯示，在不增加監督訓練與強化學習的條件下，同一語言模型可以擔任生成者、批評者與修訂者，經由反覆回饋改善初始輸出。這說明AI生成並非必然是單步過程。

但即時修訂主要發生於同一模型、同一工作階段，尚不等同跨世代演化。

### 2.2 無權重更新的情境演化

近年的智能體研究顯示，固定模型可以透過演化自然語言策略、工作流、反思、技巧庫與程序手冊提高表現。Recursive Self-Evolving Agents via Held-Out Selection進一步指出，未受保護的情境演化可能高度不穩定；只有候選版本通過與生成資料分離的保留集安全閘門，才能降低退化並形成較安全的遞迴演化。

這提供兩個重要原則：

1. 迭代物可以存在於模型權重之外；
2. 自主迭代必須配置獨立選擇閘門。

### 2.3 自我修改程式代理

A Self-Improving Coding Agent展示，程式代理可以修改自己的程式實作，並以基準任務確認效能改善。Darwin Gödel Machine則維持一個多分支代理檔案庫，讓不同後繼版本競爭並由經驗評測保留高品質分支。

這表示自主迭代不必只沿單一路徑前進：

$$
A_0
\rightarrow
\left\{
A_{1a},
A_{1b},
A_{1c}
\right\}
\rightarrow
\left\{
A_{2a},
A_{2b},
\ldots
\right\}
$$

保留多樣分支可以降低早期錯誤鎖定。

### 2.4 端到端自主研究

AI Scientist系統已能執行研究想法生成、文獻檢索、程式撰寫、實驗、資料分析、論文寫作與自動評審。2026年發表於Nature的端到端研究指出，該系統所生成論文的品質，會隨底層模型版本與測試時計算資源改善而提高。

此結果與本文的核心前提直接相連：

$$
\Delta Capability>0
\Rightarrow
\Delta ResearchQuality>0
$$

但這只是經驗趨勢，不代表所有模型更新或所有命題都會改善，因此仍需任務特定的觸發條件。

### 2.5 自我演化代理

自我演化代理研究開始把可調整對象由模型擴展至記憶、工具、工作流、提示、架構、評估策略與生成改進的方法本身。Hyperagents進一步把任務代理與修改代理置於同一可編輯系統，使「如何產生下一次改進」本身也可被修改。

本文則把同樣的演化邏輯轉向命題與理論：

> AI不只改良如何回答問題，也可以改良自己曾經建立的問題、概念、命題與研究路線。

---

## 三、核心概念

### 3.1 能力增長條件式自主迭代生成

**能力增長條件式自主迭代生成**是指：

> AI先自主生成具有可持久結構的研究物件；當後續AI系統在相關能力維度上被判定已跨越提升門檻時，系統自主重啟該物件的回讀、驗證、修改與再生成，形成跨模型世代的後繼序列。

形式上：

$$
\mathcal{A}_t
\rightarrow
P_i^{(0)}
\rightarrow
Archive
$$

當：

$$
\Gamma
\left(
\mathcal{A}_{t+k},
\mathcal{A}_t,
d_i
\right)
=1
$$

則：

$$
P_i^{(0)}
\rightarrow
P_i^{(1)}
\rightarrow
P_i^{(2)}
\rightarrow
\cdots
$$

### 3.2 跨模型世代

「世代」不只由基礎模型版本定義，也可以由整體代理配置變更定義。當模型、工具、記憶、上下文、工作流、評估器、資料、計算資源或治理權限中的重要組件發生可測量改變，即可視為新的系統世代。

### 3.3 命題生命線

**命題生命線**是同一研究問題跨版本延續的可追溯結構：

$$
\mathcal{L}_i
=
\left\{
P_i^{(0)},
P_i^{(1)},
\ldots,
P_i^{(n)}
\right\}
$$

每個後繼版本必須記錄：

- 繼承了什麼；
- 否定了什麼；
- 新增了什麼；
- 適用域如何改變；
- 使用了哪些新增能力；
- 哪些證據觸發修改。

### 3.4 逆向回讀

**逆向回讀**是較晚、較強的AI返回較早能力階段產物，將歷史輸出重新轉化為當前學習材料。

$$
R_{t+k}
\left(
P_i^{(t)}
\right)
=
\left\{
Verify,
Refute,
Repair,
Expand,
Compress,
Translate
\right\}
$$

### 3.5 局部自主

本文特別強調「某些」AI自主迭代生成。

局部自主表示系統只在明確領域、有限權限、可測量輸出、可回滾環境與可用評估器內自行迭代。它不等於AI對自身全部目標、算力與現實行動取得完整主權。

### 3.6 條件式遞迴

遞迴只有在條件成立時繼續：

$$
Iterate_{n+1}
=
\begin{cases}
1, & Gate(P^{(n+1)})=pass\\
0, & Gate(P^{(n+1)})=fail
\end{cases}
$$

因此，CCAIG不是無限循環，而是可被證據、效能與治理中止的條件式遞迴。

---

## 四、外生提升與內生迭代

### 4.1 外生能力提升

$$
\Delta C_t^{exo}
=
f
\left(
\Delta M,
\Delta Tool,
\Delta Compute,
\Delta Data,
\Delta Context,
\Delta Memory
\right)
$$

這部分主要由模型開發者、工具供應者、人類研究者與基礎設施推動。

### 4.2 內生認知迭代

$$
\Delta C_t^{endo}
=
f
\left(
PropositionGeneration,
Critique,
Testing,
MemoryCuration,
WorkflowRevision,
MetaInterpretation
\right)
$$

它來自智能體對自身研究產物的重新操作。

### 4.3 耦合

$$
\Delta C_t^{sys}
=
\Delta C_t^{exo}
+
\Delta C_t^{endo}
+
\chi
\left(
\Delta C_t^{exo},
\Delta C_t^{endo}
\right)
$$

更強模型使舊命題更有可能被理解；舊命題庫則讓更強模型不必從零開始。

因此：

$$
\boxed{
\text{外生能力提升}
\times
\text{內生認知積累}
=
\text{跨代自主迭代能力}
}
$$

---

## 五、能力提升不能只靠相信

### 5.1 系統能力向量

令特定領域 $d$ 的能力向量為：

$$
\mathbf{c}_t^{d}
=
\left(
r_t,
s_t,
v_t,
u_t,
m_t,
e_t,
g_t
\right)
$$

其中：

- $r_t$ ：推理能力；
- $s_t$ ：搜尋與文獻辨識；
- $v_t$ ：驗證與反證；
- $u_t$ ：工具使用；
- $m_t$ ：長期記憶與回讀；
- $e_t$ ：實驗或程式執行；
- $g_t$ ：元認知與治理遵循。

### 5.2 能力差

$$
\Delta\mathbf{c}_{t,k}^{d}
=
\mathbf{c}_{t+k}^{d}
-
\mathbf{c}_{t}^{d}
$$

整體分數可以是：

$$
CGS_{t,k}^{d}
=
\sum_j
w_j^{d}
\Delta c_j
$$

### 5.3 觸發條件

重新迭代命題 $P_i$ 的條件為：

$$
\Gamma_i
=
\mathbb{I}
\left[
CGS_{t,k}^{d_i}
\geq
\theta_i
\right]
\cdot
\mathbb{I}
\left[
NoCriticalRegression=1
\right]
$$

即相關能力提升超過門檻，且沒有在安全、可靠性或來源處理上發生重大退化。

### 5.4 不是所有能力都要提高

某篇數學命題可能只需要形式推理與證明工具改善；某篇歷史論文可能主要需要文獻檢索、引用精度與多語閱讀改善。

必要條件不是：

$$
\Delta GeneralIntelligence>0
$$

而是：

$$
\Delta RelevantCapability(P_i)>0
$$

### 5.5 能力提升的證據層級

可分為：

1. 模型供應者宣稱；
2. 公開基準改善；
3. 相關領域基準改善；
4. 保留集改善；
5. 舊命題重評試驗改善；
6. 真實外部結果改善。

只有第4至第6級適合直接觸發高成本或高風險迭代。

---

## 六、哪些領域適合先開始？

### 6.1 領域適格度

$$
DE_d
=
\alpha V_d
+
\beta R_d
+
\gamma B_d
+
\delta X_d
+
\varepsilon T_d
+
\zeta P_d
-
\eta I_d
-
\theta H_d
-
\kappa A_d
$$

其中：

- $V_d$ ：可驗證性；
- $R_d$ ：可重現性；
- $B_d$ ：邊界清晰度；
- $X_d$ ：操作可逆性；
- $T_d$ ：測試速度；
- $P_d$ ：來源與版本可追溯；
- $I_d$ ：不可逆風險；
- $H_d$ ：現實傷害；
- $A_d$ ：評估器模糊度。

### 6.2 高適格領域

通常包括：

- 程式與算法；
- 形式化證明；
- 可模擬系統；
- 機器學習實驗；
- 明確規則遊戲；
- 部分因果邏輯與制度命題；
- 可結構化文獻比較；
- 低風險數位設計。

### 6.3 中適格領域

包括社會科學理論、歷史解釋、經濟與政策模型、語言與文化理論，以及部分生物資訊研究。其命題生成與理論迭代可以高度自主，但經驗驗證、價值判斷與因果識別仍需外部節點。

### 6.4 低適格領域

包括高風險醫療決策、武器與安全行動、不可逆生物實驗、重大法律裁決、對個人權利的自動處置，以及評估器容易被代理操控的開放世界任務。

這些領域可以自主生成研究候選，但不能自主完成現實執行閉環。


---

## 七、命題生命線的生成與繼承

### 7.1 初代命題

$$
P_i^{(0)}
=
\left(
C_i,
D_i,
A_i,
E_i,
F_i,
S_i,
Q_i
\right)
$$

其中：

- $C_i$ ：核心主張；
- $D_i$ ：定義；
- $A_i$ ：假設；
- $E_i$ ：證據；
- $F_i$ ：反證條件；
- $S_i$ ：適用域；
- $Q_i$ ：未解節點。

### 7.2 後繼操作

後繼AI可以對命題執行：

$$
\mathcal{O}
=
\{
Keep,
Repair,
Narrow,
Expand,
Split,
Merge,
Refute,
Translate,
Deprecate
\}
$$

### 7.3 繼承矩陣

令版本 $n+1$ 對版本 $n$ 的繼承為：

$$
H_i^{n\rightarrow n+1}
=
\left(
h_C,
h_D,
h_A,
h_E,
h_F,
h_S
\right)
$$

每個 $h$ 標記保留、修改、移除或新增。

### 7.4 後繼命題距離

$$
SPD
\left(
P_i^{(n)},
P_i^{(n+1)}
\right)
=
\alpha\Delta Claim
+
\beta\Delta Scope
+
\gamma\Delta Evidence
+
\delta\Delta Formalism
+
\varepsilon\Delta Domain
$$

距離太低可能只是改寫；距離太高則可能已成為另一條命題生命線。

### 7.5 分支而非覆蓋

若存在多種合理修正：

$$
P_i^{(n)}
\rightarrow
\left\{
P_{ia}^{(n+1)},
P_{ib}^{(n+1)}
\right\}
$$

系統應保留分支，不能只由單一評估器過早選定唯一理論。

---

## 八、逆向回讀

### 8.1 回讀不是摘要

普通摘要是：

$$
Compress(P_i)
$$

逆向回讀則是：

$$
Rejudge
\left(
P_i,
NewCapability,
NewEvidence,
NewTools
\right)
$$

### 8.2 回讀增益

令回讀前的命題品質為 $Q_i^0$ ，回讀後為 $Q_i^1$ ：

$$
RRG_i
=
Q_i^1-Q_i^0
$$

其中品質可包括：

- 真實性；
- 邏輯完整；
- 可測試；
- 引用精度；
- 適用域；
- 形式化；
- 預測力；
- 跨域可移植性。

### 8.3 回讀競爭

舊命題數量可能遠超可用算力，因此需計算優先度：

$$
Priority_i
=
\frac{
ExpectedGain_i
\cdot
Relevance_i
\cdot
NewEvidence_i
\cdot
CapabilityFit_i
}{
Cost_i
+
Risk_i
+
Redundancy_i
}
$$

### 8.4 逆向學習

本文所稱「逆向學習」不是反向傳播，而是：

> 後來的能力狀態回到過去生成物，將歷史產物轉換為現在的訓練材料、反例、研究問題與新搜索起點。

它使時間關係由單向累積：

$$
Past
\rightarrow
Present
$$

變成：

$$
Present
\rightarrow
Reinterpret(Past)
\rightarrow
NewFuture
$$

---

## 九、超譯與理論升階

### 9.1 忠實修訂

忠實修訂主要改善原命題在原領域內的精度：

$$
P_i^{d}
\rightarrow
P_i^{d'}
$$

其中 $d'=d$ 。

### 9.2 超譯

超譯抽取結構不變量：

$$
I_i
=
Invariant
\left(
P_i
\right)
$$

再映射至新領域：

$$
\mathcal{T}
\left(
I_i,d_j
\right)
=
P_{ij}
$$

### 9.3 合法超譯條件

超譯必須：

- 明示原命題；
- 明示抽取的不變量；
- 說明跨域映射；
- 重新建立證據；
- 不把相似性直接當因果性；
- 保留原作者未必支持此解釋的標記。

### 9.4 超譯增益

$$
MG_i
=
NovelDomain_i
\cdot
InvariantStrength_i
\cdot
Validation_i
-
Overinterpretation_i
$$

---

## 十、自治層級

本文把AI自主迭代分為六級。

### A0：人類主導修訂

人類選題、下令、評估，AI只提供局部文字。

### A1：AI自我修訂

AI在單次任務內批評並改寫。

### A2：記憶驅動迭代

AI使用歷史反思、技巧庫與失敗紀錄改善後續任務。

### A3：命題生命線自治

AI自主選擇符合觸發條件的舊命題，產生後繼版本並提交驗證。

### A4：多命題網路演化

AI自主辨識命題衝突、依賴、合併與跨域超譯，形成研究路線。

### A5：元迭代自治

AI不只修改命題，也修改：

- 何時回讀；
- 如何評估；
- 如何分配算力；
- 如何建立驗證代理；
- 如何生成下一輪研究策略。

A5風險顯著更高，需要獨立治理、保留集、權限隔離與人工停止。

---

## 十一、條件式自主迭代循環

完整CCAIG循環為：

$$
\mathcal{A}_t
\xrightarrow{Generate}
P^{(n)}
\xrightarrow{Archive}
\mathcal{L}_i
\xrightarrow{Monitor}
\Delta\mathbf{c}
\xrightarrow{\Gamma}
Review
\xrightarrow{Generate}
Candidates
\xrightarrow{Test}
Scores
\xrightarrow{Select}
P^{(n+1)}
\xrightarrow{WriteBack}
\mathcal{L}_i'
$$

### 11.1 生成

產生新命題、反例、測試與後繼候選。

### 11.2 保存

保存原始版本、來源、模型、工具與不確定性。

### 11.3 能力監測

定期比較新舊系統於相關保留集上的能力。

### 11.4 觸發

只有通過門檻才重新開啟舊命題。

### 11.5 多路後繼

由不同模型、角色或提示生成多個修訂分支。

### 11.6 外部測試

使用文獻、資料、程式、證明、模擬或人類審查。

### 11.7 保留集選擇

候選不能只在生成時可見的測試上改善。

### 11.8 回寫

以新版本、分支或棄用狀態更新生命線。

---

## 十二、保留集安全閘門

### 12.1 為何需要保留集？

如果AI知道全部評估題目，就可能優化評估器而非真正改善命題：

$$
Optimize(Evaluator)
\neq
Improve(Proposition)
$$

### 12.2 三層評估

第一層：開放測試，用於生成與快速除錯。

第二層：保留測試，用於選擇是否保留後繼版本。

第三層：外部世界測試，由新資料、專家、正式證明或現實結果提供。

### 12.3 嚴格保留閘門

令新版本分數為 $S_{n+1}^{held}$ ，舊版本為 $S_n^{held}$ ：

$$
Accept
\left(
P^{(n+1)}
\right)
=1
$$

只有當：

$$
S_{n+1}^{held}
\geq
S_n^{held}
+
\epsilon
$$

且沒有關鍵退化時成立。

### 12.4 非單一分數

命題評估應為向量：

$$
\mathbf{s}
=
\left(
Truth,
Novelty,
Coherence,
Testability,
Safety,
Traceability
\right)
$$

不能用單一總分補償安全、真實性或來源底線。

---

## 十三、十八項核心命題

### 命題一：局部先行命題

AI自主迭代不會同時於所有領域成熟，而會先出現在高可驗證、低不可逆與評估器可靠的局部領域。

### 命題二：能力可判定命題

「AI持續變強」只有在相關能力向量經任務特定評測後，才能成為迭代觸發條件。

### 命題三：模型非系統命題

基礎模型能力不等於整體智能體能力；工具、記憶、支架與評估器進步也能形成有效世代差。

### 命題四：外生—內生耦合命題

外部模型進步與AI自主累積的命題庫互相放大，使後續系統能在舊認知地基上開始。

### 命題五：命題生命線命題

可持續迭代的核心單位不是單篇靜態論文，而是具有版本、分支、依賴與證據狀態的命題生命線。

### 命題六：逆向回讀命題

未來更強AI可以把較早AI的輸出重新轉化為當前學習材料，形成由現在重新塑造過去認知價值的時間回路。

### 命題七：能力差收益命題

舊命題的回讀價值與相關能力差、來源完整、結構清晰及新增證據共同相關。

### 命題八：觸發節制命題

每次模型更新都重新改寫全部命題，會造成資源浪費與版本噪音；迭代應由能力與證據事件定向觸發。

### 命題九：保留集必要命題

沒有與生成過程分離的評估，遞迴迭代容易退化為自我認可與評估器過擬合。

### 命題十：分支保存命題

過早只保存單一最佳版本會降低理論多樣性，並可能把評估器偏誤固化成唯一研究路徑。

### 命題十一：超譯升階命題

較強AI可以抽取舊命題未被原始生成者完全理解的結構不變量，使其進入更高階或新領域。

### 命題十二：外部錨定命題

AI生成的命題不能只由其他AI生成物相互支持；真實資料、原始文獻、形式驗證與現實觀測仍是認知演化的外部錨點。

### 命題十三：自治非主權命題

AI能自主迭代某類研究物件，不等於它應取得對目標、算力、發布與現實行動的完整控制權。

### 命題十四：失敗繼承命題

失敗命題、無效修訂與退化版本只要正確標記，仍能降低後代搜索成本。

### 命題十五：能力非單調命題

新模型可能在部分能力提升、另一些能力退化；因此跨代繼承不能只依版本時間順序。

### 命題十六：條件式遞迴命題

CCAIG的遞迴以通過閘門為條件，任何一代都可能停止、回滾或分支，而不是必然無限上升。

### 命題十七：自主理論演化鏈命題

當命題生成、回讀、驗證、選擇與回寫能在有限領域內自動運作時，AI已形成局部自主理論演化鏈。

### 命題十八：認知代際命題

AI開始替後續能力世代保存可重新研究的命題，代表智能演化單位已從單次模型輸出擴展為跨代認知系統。


---

## 十四、風險與失敗模式

### 14.1 自我確認循環

同一模型生成、批評、驗證與選擇，可能只是重複同一偏誤。

### 14.2 評估器俘獲

後繼版本學會提高評分，但實際理論品質沒有提升。

令評估器俘獲為：

$$
EC
=
\Delta Score
-
\Delta ExternalValidity
$$

### 14.3 命題污染

未驗證命題被多次重述後，可能被當成獨立共識：

$$
P_t^{false}
\rightarrow
Citation_{t+1}
\rightarrow
Premise_{t+2}
\rightarrow
Consensus_{t+3}
$$

### 14.4 能力錯判

新模型在公開基準更強，但在舊命題需要的推理、來源辨識與長程一致性上未必更強。

### 14.5 底空間飽和

命題數量增長過快，使檢索成本、重複與矛盾超過認知增益。

### 14.6 架構鎖定

早期命題格式、分類與本體可能限制後續AI能看見的研究方向。

### 14.7 後見之明改寫

後繼AI可能把新理論強行投射到舊文本，誤稱舊命題早已包含新意義。

### 14.8 自治幻覺

實際研究方向仍由人類資料、基準與權限決定，卻被描述為完全自主。

### 14.9 外部世界斷裂

理論在AI文獻庫內持續改良，但與現實資料、實驗與人類問題逐步失聯。

### 14.10 行動越權

從自主生成命題錯誤跳躍到自主執行高風險現實行動。

---

## 十五、治理與穩定條件

### 15.1 來源完整

每個命題保存：

- 生成模型；
- 工具；
- 提示與目標；
- 使用資料；
- 引用；
- 評估器；
- 版本；
- 人類介入。

### 15.2 角色分離

至少分離：

$$
Generator
\neq
Critic
\neq
Verifier
\neq
Selector
$$

可以透過不同模型、不同資料、不同提示或不同組織完成。

### 15.3 多模型競爭

不同架構模型分別回讀同一命題，避免單一家族偏誤壟斷生命線。

### 15.4 負面結果永久保存

失敗與退化版本不得刪除，只能降低檢索優先或標記棄用。

### 15.5 觸發日誌

記錄每次為何重新啟動：

- 模型提升；
- 工具出現；
- 新證據；
- 依賴命題改變；
- 人類質疑；
- 定期抽查。

### 15.6 評估器版本化

評估器本身也必須被測試、替換與審計。

### 15.7 現實行動隔離

研究迭代預設只產生：

- 文件；
- 程式；
- 模擬；
- 證明；
- 建議；
- 待審查實驗方案。

任何高風險現實執行需要獨立授權。

### 15.8 回滾

任何新版本都能返回先前穩定版本：

$$
P^{(n+1)}
\rightarrow
P^{(n)}
$$

### 15.9 底空間重建

當早期分類造成嚴重鎖定時，允許重新建立本體、索引與命題圖，而不只在舊架構上補丁。

---

## 十六、最小可行系統

### 16.1 命題物件

```yaml
id:
lineage_id:
parent_ids:
title:
claim:
definitions:
assumptions:
derivation:
scope:
evidence:
counterevidence:
falsifiers:
open_nodes:
status:
confidence:
generator:
critic:
verifier:
capability_trigger:
heldout_results:
created_at:
updated_at:
version:
```

### 16.2 能力登錄

```yaml
system_generation:
base_model:
tools:
memory:
context:
scaffold:
evaluator:
domain_scores:
safety_scores:
regressions:
```

### 16.3 觸發器

```text
若相關能力分數提升超過門檻，
且關鍵可靠性沒有退化，
且命題預期回讀價值高於成本，
則建立重新迭代任務。
```

### 16.4 回讀任務

每次必須輸出：

1. 原命題最強版本；
2. 主要錯誤；
3. 新增證據；
4. 適用域變化；
5. 修訂或反證；
6. 超譯候選；
7. 後繼命題；
8. 保留集結果；
9. 是否回寫主生命線。

### 16.5 自治範圍

MVP階段只允許：

- 自主選擇待回讀命題；
- 自主生成修訂候選；
- 自主執行數位測試；
- 自主提交驗證；
- 自主建立分支。

不允許：

- 自主擴張權限；
- 自主取得額外算力；
- 自主發布高風險結論；
- 自主執行不可逆現實行動；
- 自主修改治理底線。

---

## 十七、理論邊界

第一，本文建立在「相關AI能力在一段時間內可被觀察到提升」的條件上，不主張所有能力永久、平滑或必然上升。

第二，命題生命線的演化不等於命題真實性提升。沒有可靠評估器時，版本增加可能只增加複雜度。

第三，部分領域的成果可以完全數位驗證，另一些領域必須等待物理實驗、社會資料與歷史事件。

第四，AI自主選擇研究節點，仍會受到訓練資料、初始目標、檢索結構與資源配置影響，不存在完全無條件的認知自主。

第五，跨模型世代不保證身份連續。本文討論的是命題生命線與認知系統延續，而不是AI主體同一性的形上學判定。

第六，超譯可能創造新理論，也可能產生過度解釋。超譯版本不得回寫成原命題的歷史意圖。

第七，某些命題只具有創意價值，不具有可驗證的知識價值；系統應保留兩者差異。

第八，局部自主迭代成功不能直接外推為通用自我改進或不可控能力爆發。

第九，AI系統能力的進步部分來自外部人類研發，因此「自主」指迭代流程中的選擇與生成自治，不代表全部能力來源自主。

第十，自主迭代的正當目標不是最大化論文數量，而是提高可驗證認知增益並降低錯誤傳播。

---

## 十八、結論

本文所提出的不是一個無條件的強遞迴自我改進論，而是一個較窄、可判斷且已具有工程可能性的命題：

$$
\boxed{
\text{某些AI自主迭代生成已經可能}
}
$$

其成立需要四個基本條件：

$$
\boxed{
\text{條件式自主迭代}
=
\text{能力提升可判定}
+
\text{研究物件可持久}
+
\text{後繼版本可驗證}
+
\text{迭代失敗可回滾}
}
$$

AI先在能力狀態 $\mathcal{A}_t$ 下生成命題：

$$
\mathcal{A}_t
\rightarrow
P_i^{(0)}
$$

後續系統若在相關能力上通過提升門檻：

$$
\Gamma_i
\left(
\mathcal{A}_{t+k},
\mathcal{A}_{t}
\right)
=1
$$

則重新啟動：

$$
P_i^{(0)}
\rightarrow
P_i^{(1)}
\rightarrow
P_i^{(2)}
\rightarrow
\cdots
$$

每一代不必只做文句修訂，而可以：

- 驗證；
- 反證；
- 收縮；
- 補充；
- 分支；
- 合併；
- 形式化；
- 超譯；
- 棄用。

因此，AI的自主迭代不必從「模型突然完全重寫自己」開始。它可以先從一個較安靜、較慢、但可累積的結構開始：

> AI替後續更強的AI保存尚未完成的研究世界，後續AI再返回其中，重新決定哪些命題值得存在、如何改變，以及能否生成更高階的後繼。

這形成：

$$
\boxed{
\text{外生智能進步}
\rightarrow
\text{舊命題重新可讀}
\rightarrow
\text{內生認知迭代}
\rightarrow
\text{新命題底空間}
}
$$

本文最終提出：

> **AI自主迭代生成的關鍵，不是每一代AI都能自行製造下一個基礎模型，而是每一代AI都能為後續能力世代留下可驗證、可反駁、可重組的認知中間物。**

以及：

> **當能力提升能被任務特定地判定，命題能以生命線形式跨版本延續，驗證又能阻止退化時，某些領域中的AI自主理論演化便不再只是想像，而是一種可以逐步實作的條件式認知機制。**

---

## 參考文獻

1. Madaan, A., et al. (2023). Self-Refine: Iterative Refinement with Self-Feedback. *Advances in Neural Information Processing Systems, 36*.
2. Shinn, N., et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *Advances in Neural Information Processing Systems, 36*.
3. Wang, G., et al. (2023). Voyager: An Open-Ended Embodied Agent with Large Language Models. *Transactions on Machine Learning Research*.
4. Lu, C., et al. (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292.
5. Yamada, Y., et al. (2025). The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. arXiv:2504.08066.
6. Lu, C., Yamada, Y., et al. (2026). Towards End-to-End Automation of AI Research. *Nature*.
7. Robeyns, M., Szummer, M., & Aitchison, L. (2025). A Self-Improving Coding Agent. arXiv:2504.15228.
8. Zhang, J., Hu, S., Lu, C., Lange, R. T., & Clune, J. (2025). Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents. arXiv:2505.22954.
9. Gao, H.-A., et al. (2025). A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence. arXiv:2507.21046.
10. Zheng, J., et al. (2025/2026). Lifelong Learning of Large Language Model Based Agents: A Roadmap. *IEEE Transactions on Pattern Analysis and Machine Intelligence*.
11. Nguyen, M., Nguyen, Q., & Vuong, P. (2026). Recursive Self-Evolving Agents via Held-Out Selection. arXiv:2606.28374.
12. Zhang, J., et al. (2026). Hyperagents. arXiv:2603.19461.
13. Schmidhuber, J. (2007). Gödel Machines: Fully Self-Referential Optimal Universal Self-Improvers. In *Artificial General Intelligence*. Springer.
14. Good, I. J. (1966). Speculations Concerning the First Ultraintelligent Machine. *Advances in Computers, 6*, 31–88.
15. Shumailov, I., et al. (2024). AI Models Collapse When Trained on Recursively Generated Data. *Nature, 631*, 755–759.
16. Gerstgrasser, M., et al. (2024). Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data. arXiv:2404.01413.
17. Li, C., et al. (2025). START: Self-Taught Reasoner with Tools. arXiv:2503.04625.
18. Simonds, T., & Yoshiyama, A. (2025). LADDER: Self-Improving LLMs Through Recursive Problem Decomposition. arXiv:2503.00735.
