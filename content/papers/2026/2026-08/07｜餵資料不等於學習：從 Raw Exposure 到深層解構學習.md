# 07｜餵資料不等於學習：從 Raw Exposure 到深層解構學習
## Feeding Data Is Not the Same as Learning: From Raw Exposure to Deep Deconstructive Learning

**系列：**《可執行資料與深層解構學習》  
**篇次：** 07 / 10  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1 Research Draft  
**日期：** 2026-08-17  
**文件性質：** AI 學習方法論／系統解構／表徵學習／因果表徵／系統辨識／程式重建  
**範圍聲明：** 本文提出的是一套「研究與資料工程層級」的學習深度框架，不宣稱現有神經網路訓練流程必然具有本文所稱的理解或因果識別能力。  
**術語聲明：** 本文所稱「深層解構學習」（Deep Deconstructive Learning, DDL）不是既有 Deep Learning 的同義詞，而是本文提出的多階段知識抽取、正規化、因果分析、重建與生成方法論。

---

## 摘要

現代人工智慧已能讀取大量文字、圖像、影音、JSON、程式碼、遊戲軌跡與軟體操作資料。由此產生一個容易混淆的命題：只要 AI 已經「看過」資料，就等於 AI 已經「學會」該系統。然而，能預測文字、描述程式碼、模仿軌跡或回答局部問題，並不自動等於模型已抽取出系統的功能模組、狀態結構、因果關係、設計不變量、可替換自由度與重建方法。

本文提出：

$$
\boxed{
\text{Exposure}
\neq
\text{Deconstruction}
\neq
\text{Operational Understanding}
}
$$

並建立八階段深層解構學習階梯：

$$
\boxed{
L_0
<
L_1
<
L_2
<
L_3
<
L_4
<
L_5
<
L_6
<
L_7
}
$$

分別為：

$$
\boxed{
\begin{aligned}
L_0 &: \text{Raw Exposure}\\
L_1 &: \text{Parsing / Entity Extraction}\\
L_2 &: \text{Structural Decomposition}\\
L_3 &: \text{Functional Typing}\\
L_4 &: \text{Cross-System Normalization}\\
L_5 &: \text{Causal / Invariant Extraction}\\
L_6 &: \text{Executable Reconstruction}\\
L_7 &: \text{Generative Synthesis}
\end{aligned}
}
$$

本文強調，這些層級不是在聲稱「較高層必然比低層更智能」，而是在區分不同的研究證據強度與知識可操作性。

現有 representation learning 與 causal representation learning 研究為此提供重要限制。Locatello 等人證明，在一般條件下，僅依靠無監督觀察資料而沒有額外 inductive bias，不能保證唯一恢復真實解耦因子；後續研究則顯示，結構假設、弱監督、時間結構或 intervention 能改善 latent factor 與 causal mechanism 的 identifiability。系統辨識研究亦區分「高精度黑箱預測」與「恢復可描述系統結構」；2026 年的 dynamical-system causal representation work 明確指出，深度模型可以高保真擬合複雜系統，但黑箱函數逼近不必然產生可解耦、可描述的系統參數表示。

本文進一步將程式合成研究納入「重建驗收」脈絡。Program synthesis from input-output examples 的研究顯示，僅符合少量輸入輸出樣例仍可能存在大量候選程式；執行器、搜尋空間約束、debugging 與 counterexample-like feedback 可以進一步消除不正確候選。故本文提出工程上的「重建證據原則」：

$$
\boxed{
\text{If a claimed understanding cannot support reconstruction, transfer, or intervention prediction, its operational depth remains uncertain.}
}
$$

最後，本文將遊戲、軟體、科研流程、工程流程與具身任務統一為可解構系統：

$$
\boxed{
\mathcal D(X)
\rightarrow
(
E,
G,
T,
R,
I,
F,
C,
P
)
}
$$

其中 $E$ 為 entities、 $G$ 為 structure graph、 $T$ 為 functional types、 $R$ 為 relations、 $I$ 為 invariants、 $F$ 為 replaceable freedoms、 $C$ 為 causal/computational mechanisms、 $P$ 為 provenance。這使「資料 ingestion」進一步升級為「結構知識編譯」。

**關鍵詞：** Raw Exposure、Deep Deconstructive Learning、Functional Typing、Causal Representation Learning、System Identification、Program Synthesis、Reconstruction、Inductive Bias、Intervention、Knowledge Compilation

---

# 1. 問題：AI 看過，不代表 AI 已經掌握

現代 AI pipeline 很容易形成：

$$
\boxed{
\text{Collect}
\rightarrow
\text{Ingest}
\rightarrow
\text{Train / Retrieve}
\rightarrow
\text{Answer}.
}
$$

因此，當模型可以回答：

> 這個 repository 在做什麼？

> 這段影片裡角色做了什麼？

> 這個 JSON 欄位代表什麼？

人們很容易推論：

$$
\boxed{
\text{Can Describe}
\Rightarrow
\text{Has Understood}.
}
$$

本文認為這個推論過強。

---

# 2. Exposure 是學習的必要來源之一，但不是理解證書

令：

$$
D
$$

為原始資料。

模型接觸：

$$
D
$$

可以得到：

$$
Z=f_\theta(D).
$$

 $Z$ 可能支援：

- prediction；
- retrieval；
- compression；
- generation；
- classification。

但不能僅由：

$$
\operatorname{Loss}(Z)\downarrow
$$

推出：

$$
\boxed{
Z
=
\text{correct causal / functional decomposition}.
}
$$

---

# 3. 高預測力不等於高結構可解釋力

假設模型：

$$
M
$$

可以準確預測：

$$
s_{t+1}.
$$

即：

$$
\hat s_{t+1}
\approx
s_{t+1}.
$$

仍然可能不知道：

- 哪些 latent state 對應哪個功能；
- 哪個變量是 cause；
- 哪個只是 proxy；
- 哪些模組可替換；
- 哪些 interaction 是不變量。

因此：

$$
\boxed{
\text{Predictive Fidelity}
\not\equiv
\text{Structural Identification}.
}
$$

---

# 4. 表徵辨識本身就是困難問題

Representation learning 的一個核心問題是：

> 從觀察資料中，能否唯一恢復真正生成因素？

Locatello 等人在 2019 年指出：

$$
\boxed{
\text{Unsupervised Disentanglement}
}
$$

在一般條件下，若沒有模型與資料上的 inductive bias，無法保證唯一識別真實 latent factors。

這表示：

$$
\boxed{
\text{Observe More}
}
$$

並不自動等於：

$$
\boxed{
\text{Recover the true factors}.
}
$$

---

# 5. 原始資料中可以存在多個同樣合理的解釋

令：

$$
x=g(z)
$$

其中：

$$
z
$$

是真實 latent factor。

對 observation：

$$
x,
$$

可能存在另一個 transformation：

$$
\tilde z=h(z)
$$

也能產生等價觀察分布。

因此：

$$
\boxed{
\text{Observation Distribution}
}
$$

未必足以唯一指定：

$$
\boxed{
\text{Semantic Decomposition}.
}
$$

---

# 6. 這與遊戲解構完全同構

只看一個 NPC 的行為：

```text
看到敵人
→ 接近
→ 攻擊
```

可能由：

- FSM；
- Behavior Tree；
- Utility；
- Script；
- Planner；

多種架構產生。

所以：

$$
\boxed{
\text{Behavioral Observation}
\not\Rightarrow
\text{Unique Implementation}.
}
$$

---

# 7. Intervention 為何重要？

若只有 observational data：

$$
D_O,
$$

我們看到：

$$
X\sim P(X).
$$

若可以 intervention：

$$
do(A=a),
$$

則可以觀察：

$$
P(X\mid do(A=a)).
$$

這可以排除一部分僅靠 correlation 的解釋。

---

# 8. Causal Representation Learning 的啟示

Causal Representation Learning（CRL）嘗試從高維 observations 中恢復：

- latent causal variables；
- causal structure。

近年理論工作顯示，在特定結構假設、intervention 或 auxiliary information 下，可以得到不同程度的 identifiability。

因此本文不主張：

> intervention 一定能讓 AI 找到真正因果模型。

而主張：

$$
\boxed{
\text{Interventional Evidence}
}
$$

通常比單一靜態 exposure 提供更強的結構約束。

---

# 9. 2026 年 dynamical-system 研究提供直接對照

Baumgartner 等人於 2026 年研究：

# Disentangling Dynamical Systems

其核心問題之一正是：

> deep learning 可以高保真擬合複雜系統，但 black-box function approximation 不必然產生 explicit、descriptive、disentangled representations。

這與本文的區分高度一致：

$$
\boxed{
\text{Fit}
\neq
\text{Deconstruct}.
}
$$

---

# 10. System Identification 與一般預測的差異

System Identification 的目標通常不只是：

$$
y_{t+1}
$$

預測得準。

而是估計：

$$
\theta
$$

使：

$$
F_\theta
$$

能表示目標系統 dynamics。

因此：

$$
\boxed{
\text{System Identification}
}
$$

比單純 sequence prediction 更接近：

> 這個系統怎麼運行？

---

# 11. 但 System Identification 也需要 assumptions

參數式 system identification 常要求：

- model family；
- basis function；
- parameterization；
- physical assumptions。

如果 function family 一開始就錯：

$$
F_\theta
$$

可能無法找到真正 mechanism。

所以：

$$
\boxed{
\text{Structure Discovery}
}
$$

依然不是免費獲得。

---

# 12. Deep Deconstructive Learning 的問題設定

本文將目標系統記為：

$$
X.
$$

其可取得證據為：

$$
E_X.
$$

深層解構希望產生：

$$
\boxed{
\mathcal D(X)
=
(
E,
G,
T,
R,
I,
F,
C,
P
).
}
$$

其中：

- $E$：entities；
- $G$：structure graph；
- $T$：functional types；
- $R$：relations；
- $I$：invariants；
- $F$：replaceable freedoms；
- $C$：causal / computational mechanisms；
- $P$：provenance / evidence state。

---

# 13. $L_0$ — Raw Exposure

第一層：

$$
\boxed{
L_0=\text{Raw Exposure}.
}
$$

包含：

- text；
- image；
- video；
- audio；
- source code；
- JSON；
- logs；
- replay；
- state traces；
- user interaction。

---

# 14. Raw Exposure 的價值

 $L_0$ 非常重要。

它建立：

$$
\boxed{
\text{Empirical Substrate}.
}
$$

沒有 raw evidence，後面容易變成純猜測。

所以本文不是反對大量資料。

而是反對：

$$
\boxed{
L_0=L_7.
}
$$

---

# 15. Raw Exposure 的典型能力

在 $L_0$，AI 可以：

- retrieve；
- summarize；
- imitate；
- classify；
- autocomplete；
- predict next step。

這些都是有價值能力。

但尚未保證：

- module boundary；
- invariant；
- causal relation；
- functional type。

---

# 16. $L_1$ — Parsing / Entity Extraction

第二層：

$$
\boxed{
L_1=\text{Parsing}.
}
$$

目標：

> 裡面有哪些東西？

例如 source code：

- class；
- function；
- field；
- event；
- file；
- module。

遊戲：

- NPC；
- item；
- location；
- action；
- quest；
- status。

---

# 17. Entity Extraction 還不是 Architecture

假設已抽出：

$$
1000
$$

個 class。

仍然不知道：

- 哪些是核心；
- 哪些是 utility；
- 哪些屬於同一 subsystem；
- 哪些關係是控制流；
- 哪些只是 data model。

因此：

$$
\boxed{
\text{Inventory}
\neq
\text{Architecture}.
}
$$

---

# 18. $L_2$ — Structural Decomposition

第三層：

$$
\boxed{
L_2=\text{Structural Decomposition}.
}
$$

目標建立：

$$
\boxed{
G=(V,E).
}
$$

例如：

```text
Need
→ Candidate Generation
→ Selection
→ Scheduler
→ Execution
→ World Commit
```

---

# 19. 結構圖開始回答「怎麼接」

 $L_2$ 可以保存：

- dependency；
- read/write；
- trigger；
- event；
- state flow；
- control edge；
- feedback。

這比單純 entity list 深一層。

---

# 20. 但 Structural Decomposition 仍可能被命名綁架

假設原始碼叫：

```text
Brain
ThinkNode
WorkGiver
JobDriver
```

直接把名字畫成 graph，

仍然只是：

$$
\boxed{
\text{Implementation Graph}.
}
$$

---

# 21. $L_3$ — Functional Typing

第四層：

$$
\boxed{
L_3=\text{Functional Typing}.
}
$$

目標：

$$
\boxed{
\text{Implementation-specific Symbol}
\rightarrow
\text{General Functional Type}.
}
$$

---

# 22. Functional Typing Example

例如：

```text
WorkGiver
```

可能映射：

$$
\boxed{
\text{Task Candidate Generator}.
}
$$

`JobDriver`：

$$
\boxed{
\text{Task Execution Controller}.
}
$$

`ThinkTree`：

$$
\boxed{
\text{Decision / Arbitration Structure}.
}
$$

---

# 23. 為什麼 Functional Typing 重要？

因為跨系統比較不能依賴：

$$
\text{same name}.
$$

不同作品可能名稱完全不同。

因此需要：

$$
\boxed{
\text{Name Independence}.
}
$$

---

# 24. $L_4$ — Cross-System Normalization

第五層：

$$
\boxed{
L_4=\text{Cross-System Normalization}.
}
$$

目標是比較：

$$
X_1,X_2,\ldots,X_n.
$$

找出：

$$
\boxed{
\text{Functional Equivalence Classes}.
}
$$

---

# 25. Normalization Example

```text
Hunger
FoodNeed
NutritionUrgency
StarvationDrive
```

可能統一成：

$$
\boxed{
\text{Resource-Deficit Drive}.
}
$$

---

# 26. Normalization 不是把所有差異抹掉

如果兩個 system：

$$
A
$$

與：

$$
B
$$

都屬於：

$$
\text{Resource-Deficit Drive},
$$

仍應保存：

- update frequency；
- threshold；
- decay；
- interrupt behavior；
- social consequence。

所以：

$$
\boxed{
\text{Normalize Type}
+
\text{Preserve Instance Difference}.
}
$$

---

# 27. 跨系統 normalization 才開始形成「領域知識」

如果 AI 只記住：

$$
1000
$$

個 repository，

它可能具有：

$$
\boxed{
\text{Repository Knowledge}.
}
$$

當它能將不同實作映射到共同 functional families 時，才開始形成：

$$
\boxed{
\text{Domain Structure}.
}
$$

---

# 28. $L_5$ — Causal / Invariant Extraction

第六層：

$$
\boxed{
L_5=\text{Causal / Invariant Extraction}.
}
$$

核心問題：

> 哪些東西是系統真正依賴的？

---

# 29. Invariant

令：

$$
I(X)
$$

為系統不變量。

如果移除：

$$
i\in I(X),
$$

則：

$$
Function(X)
$$

不再成立或發生重大改變。

---

# 30. Replaceable Freedom

令：

$$
F(X)
$$

為可替換自由度。

若：

$$
m_1
\rightarrow
m_2
$$

後仍滿足：

$$
Function(X_{m_1})
\approx
Function(X_{m_2}),
$$

則：

$$
m\in F(X).
$$

---

# 31. Invariant 與 Freedom 必須一起學

如果只找 invariant，

系統會過度僵化。

如果只找自由度，

又可能失去身份。

所以：

$$
\boxed{
\text{Understanding}
=
\text{What must remain}
+
\text{What may change}.
}
$$

---

# 32. Intervention 可以測 Invariant

如果假說：

$$
H:
m
\text{ 是必要模組},
$$

則可以：

$$
do(m=0)
$$

觀察：

$$
\Delta Function.
$$

若：

$$
\Delta Function\gg0,
$$

則 $H$ 得到支持。

---

# 33. 但 intervention 仍不能自動證明唯一因果模型

可能存在 compensating mechanisms。

所以：

$$
\boxed{
\text{Intervention Evidence}
\neq
\text{Absolute Causal Truth}.
}
$$

仍然需要：

- multiple interventions；
- alternative hypotheses；
- cross-case comparison。

---

# 34. $L_6$ — Executable Reconstruction

第七層：

$$
\boxed{
L_6=\text{Executable Reconstruction}.
}
$$

此時不再只說：

> 我理解了。

而要求：

$$
\boxed{
\hat X
=
Reconstruct(
\mathcal D(X)
).
}
$$

---

# 35. Reconstruction Test

令：

$$
\mathcal T
$$

為測試族。

要求：

$$
\forall t\in\mathcal T,
$$

有：

$$
d(
Behavior(X,t),
Behavior(\hat X,t)
)
\leq
\epsilon_t.
$$

---

# 36. Reconstruction 不是證明「原始實作就是這樣」

即使：

$$
\hat X
$$

重現原系統，

仍不能推出：

$$
\hat X=X_{\mathrm{internal}}.
$$

只能得到：

$$
\boxed{
\text{Functional / Behavioral Support}.
}
$$

---

# 37. 多種重建可能同時有效

可能：

$$
\hat X_1,
\hat X_2,
\hat X_3
$$

都滿足：

$$
d_B<\epsilon.
$$

此時應保存：

$$
\boxed{
\text{Equivalence Class of Reconstructions}.
}
$$

而不是武斷宣稱只有一種真相。

---

# 38. Program Synthesis 提供一個有用類比

Programming-by-example 問：

$$
\boxed{
\text{IO Examples}
\rightarrow
\text{Program}.
}
$$

但少量 IO 通常不足以唯一指定 program。

這與：

$$
\boxed{
\text{Game Behavior}
\rightarrow
\text{AI Architecture}
}
$$

非常相似。

---

# 39. Under-Specification

假設：

$$
P_1
$$

與：

$$
P_2
$$

都滿足：

$$
P_i(x_j)=y_j
$$

對所有已觀察樣本。

仍可能：

$$
P_1\neq P_2.
$$

所以：

$$
\boxed{
\text{Passing Known Examples}
\neq
\text{Correct General Mechanism}.
}
$$

---

# 40. Counterexample / New Test 的價值

若找到：

$$
x^\*
$$

使：

$$
P_1(x^\*)\neq P_2(x^\*),
$$

則：

$$
x^\*
$$

具有高判別資訊量。

這就是前一篇「experiment selection」與本篇深層解構的連接。

---

# 41. Execute and Debug

程式合成研究中，SED 類方法將：

$$
\boxed{
\text{Synthesize}
\rightarrow
\text{Execute}
\rightarrow
\text{Debug}
}
$$

整合。

核心思想不是「第一次生成就正確」。

而是：

$$
\boxed{
\text{Execution Feedback}
}
$$

可以用來修正候選。

---

# 42. 這正是深層解構需要的閉環

對系統假說：

$$
H_0,
$$

流程應是：

$$
\boxed{
H_0
\rightarrow
\text{Implementation}
\rightarrow
\text{Execution}
\rightarrow
\text{Mismatch}
\rightarrow
H_1.
}
$$

這比文字自我反思更接近客觀校正。

---

# 43. $L_7$ — Generative Synthesis

第八層：

$$
\boxed{
L_7=\text{Generative Synthesis}.
}
$$

此時系統不只重建：

$$
X,
$$

而能從：

$$
\mathcal K
=
\{
Types,
Patterns,
Invariants,
Freedoms,
Failures
\}
$$

生成新的：

$$
X^\*.
$$

---

# 44. 生成能力是更強驗收，但不是唯一理解定義

若 AI 能：

$$
\boxed{
\text{Intent}
\rightarrow
\text{Architecture}
\rightarrow
\text{Executable System},
}
$$

這提供非常強的 operational evidence。

但本文不主張：

$$
\text{Cannot Generate}
\Rightarrow
\text{Does Not Understand}.
$$

因為生成還需要：

- 工具；
- coding；
- resources；
- planning。

所以本文只主張：

$$
\boxed{
\text{Successful reconstruction/generation strengthens evidence of operational understanding}.
}
$$

---

# 45. 八層階梯的完整形式

因此：

$$
\boxed{
L_{\text{raw}}
<
L_{\text{parsed}}
<
L_{\text{structured}}
<
L_{\text{typed}}
<
L_{\text{normalized}}
<
L_{\text{causal}}
<
L_{\text{reconstructive}}
<
L_{\text{generative}}.
}
$$

這個：

$$
<
$$

表示：

> 知識結構要求與可操作驗收逐步增加。

不是 intelligence IQ 排名。

---

# 46. 每一層都可以失敗

例如：

### $L_1$ Failure

entity 抽錯。

### $L_2$ Failure

dependency graph 錯。

### $L_3$ Failure

functional type 誤分類。

### $L_4$ Failure

過度 normalization。

### $L_5$ Failure

因果誤判。

### $L_6$ Failure

重建過擬合。

### $L_7$ Failure

生成新系統不可用。

因此每層都需要 validation。

---

# 47. 層級不一定線性完成

實際研究可能：

$$
L_0
\rightarrow
L_2
\rightarrow
L_1
\rightarrow
L_3.
$$

或從 reconstruction failure 回到：

$$
L_5.
$$

所以真正流程是：

$$
\boxed{
\text{Iterative Layered Loop}.
}
$$

---

# 48. 深層解構不是單次 pipeline

更完整：

$$
\boxed{
\mathcal D_{t+1}
=
Update(
\mathcal D_t,
Evidence_t,
Failure_t,
Intervention_t
).
}
$$

每次新證據都可能：

- 改 type；
- 改 relation；
- 降 confidence；
- 推翻 mechanism。

---

# 49. Provenance 是必要層

對每個：

$$
claim_i,
$$

需要：

$$
P_i.
$$

至少區分：

```text
observed
documented
inferred
reconstructed
validated
contested
```

否則 normalization 很容易把猜測變成「事實」。

---

# 50. 深層解構與 Knowledge Graph 的差異

普通 knowledge graph：

$$
A
\xrightarrow{r}
B.
$$

深層解構還需要：

$$
\boxed{
\text{State}
+
\text{Timing}
+
\text{Control}
+
\text{Mechanism}
+
\text{Invariant}
+
\text{Counterfactual}
+
\text{Execution}.
}
$$

---

# 51. Semantic Relation 不等於 Causal Relation

例如：

```text
Hunger related_to Food
```

只是語義關係。

真正因果結構可能是：

$$
Hunger\uparrow
\Rightarrow
Utility(Eat)\uparrow.
$$

或：

$$
Hunger>\tau
\Rightarrow
Interrupt(CurrentJob).
$$

這是不同資料層。

---

# 52. JSON 也不自動等於深層資料

一個：

```json
{"state":"hungry","action":"eat"}
```

仍可能只是：

$$
\boxed{
\text{Serialized Observation}.
}
$$

真正的結構需要：

- condition；
- timing；
- alternative；
- transition；
- priority；
- source；
- confidence。

---

# 53. Source Code 也不自動等於深層資料

Source code 可以包含：

$$
\boxed{
\text{Implementation}.
}
$$

但 AI 還需要抽取：

- function；
- role；
- boundary；
- invariant；
- failure；
- temporal relation。

所以：

$$
\boxed{
\text{Open Source}
\neq
\text{Pre-Deconstructed Knowledge}.
}
$$

---

# 54. 影片也不自動等於技能知識

影片可以提供：

- visual sequence；
- action trace；
- human demonstration。

但如果沒有：

- goal；
- hidden state；
- alternative actions；
- failure；
- intervention；

則它更接近：

$$
\boxed{
\text{Demonstration}
}
$$

而不是完整 mechanism。

---

# 55. 深層資料的理想單位

本文提出：

$$
\boxed{
d_i
=
(
s,
o,
a,
g,
c,
m,
r,
s',
e,
p
)
}
$$

其中：

- $s$：state；
- $o$：observation；
- $a$：action；
- $g$：goal；
- $c$：constraint；
- $m$：mechanism；
- $r$：relation / rule；
- $s'$：next state；
- $e$：evaluation；
- $p$：provenance。

---

# 56. 如果不知道 mechanism 呢？

就寫：

$$
M
=
\{
m_1,m_2,\ldots,m_k
\}.
$$

以及：

$$
w_i
=
P(m_i\mid E).
$$

不需要強迫唯一解。

---

# 57. Unknown 是合法狀態

成熟解構庫必須允許：

$$
\boxed{
\text{UNKNOWN}.
}
$$

因為：

$$
\text{False Certainty}
$$

比：

$$
\text{Explicit Unknown}
$$

更危險。

---

# 58. Cross-System Deconstruction 可以提供 Inductive Bias

Locatello 類結果指出：

> 完全無偏好的 unsupervised disentanglement 不可識別。

但當我們已經研究：

$$
X_1,\ldots,X_n,
$$

便可能形成：

$$
\boxed{
\mathcal B_{\mathrm{domain}}
}
$$

即 domain inductive bias。

例如：

> 多數 NPC system 都有 perception–selection–execution。

這不是絕對真理。

但可以作為下一個系統的候選 decomposition prior。

---

# 59. Domain Prior 必須可被反例推翻

如果新系統：

$$
X^\*
$$

沒有：

$$
Perception,
$$

卻仍然運作，

則不能硬套。

所以：

$$
\boxed{
\text{Prior}
\neq
\text{Dogma}.
}
$$

---

# 60. 解構資料庫會逐步學會「怎麼解構」

對每個過去案例保存：

- 哪個 experiment 有效；
- 哪個 inference 錯；
- 哪個 source 最有用；
- 哪個 functional type 重複出現。

於是：

$$
\boxed{
\text{Deconstruction Method}
}
$$

本身可以被學習。

---

# 61. Meta-Deconstruction

令：

$$
\mathcal D
$$

為解構算子。

經過：

$$
N
$$

次任務後：

$$
\mathcal D_N
$$

應優於：

$$
\mathcal D_0.
$$

也就是：

$$
\boxed{
\mathcal D_{t+1}
=
Learn(
\mathcal D_t,
Audit_t
).
}
$$

---

# 62. 對遊戲而言，這意味着什麼？

不是只餵：

- game video；
- source；
- save；
- Wiki。

而是建立：

$$
\boxed{
\text{Game}
\rightarrow
\text{Functional Decomposition}
\rightarrow
\text{Composition Graph}
\rightarrow
\text{Mechanism Hypotheses}
\rightarrow
\text{Reconstruction}.
}
$$

---

# 63. 對軟體而言

不是只餵：

$$
GitHub.
$$

而是：

$$
\boxed{
\text{Codebase}
\rightarrow
\text{Modules}
\rightarrow
\text{Functional Contracts}
\rightarrow
\text{Runtime Flows}
\rightarrow
\text{Failure Modes}
\rightarrow
\text{Rebuild}.
}
$$

---

# 64. 對科研而言

不是只餵：

$$
Papers.
$$

而是：

$$
\boxed{
\text{Question}
\rightarrow
\text{Hypothesis}
\rightarrow
\text{Experiment}
\rightarrow
\text{Data}
\rightarrow
\text{Inference}
\rightarrow
\text{Replication}.
}
$$

---

# 65. 對工程而言

不是只餵：

$$
CAD
$$

或：

$$
Final Design.
$$

而是：

$$
\boxed{
\text{Constraint}
\rightarrow
\text{Candidate}
\rightarrow
\text{Simulation}
\rightarrow
\text{Failure}
\rightarrow
\text{Revision}
\rightarrow
\text{Final Design}.
}
$$

---

# 66. 因此真正高價值的是 Process Structure

靜態結果：

$$
Y
$$

只告訴 AI：

> 最後長這樣。

過程資料：

$$
X_0
\rightarrow
X_1
\rightarrow
\cdots
\rightarrow
X_n
$$

告訴 AI：

> 怎麼走到這裡。

深層解構再加入：

$$
\boxed{
\text{Why each transition occurred}.
}
$$

---

# 67. 深層解構的五種資料面

本文將最終資料分成：

$$
\boxed{
\mathcal K
=
K_S
+
K_G
+
K_C
+
K_E
+
K_I.
}
$$

其中：

- $K_S$：semantic；
- $K_G$：structural；
- $K_C$：causal / computational；
- $K_E$：executable；
- $K_I$：intent / rationale。

---

# 68. Semantic

回答：

> 這是什麼？

---

# 69. Structural

回答：

> 怎麼組？

---

# 70. Causal / Computational

回答：

> 為什麼這樣變？

---

# 71. Executable

回答：

> 能不能重做？

---

# 72. Intent

回答：

> 為什麼要這樣設計？

最後一層會在本系列第 10 篇完整展開。

---

# 73. 理解的操作性定義

本文避免形而上地宣稱：

> AI 真正理解。

而使用：

$$
\boxed{
U_{\mathrm{op}}
}
$$

表示 operational understanding evidence。

---

# 74. Operational Understanding Score

可粗略建立：

$$
\boxed{
U_{\mathrm{op}}
=
f(
Prediction,
Explanation,
Intervention,
Reconstruction,
Transfer
).
}
$$

不是一個真正普遍標準。

但比：

> 模型回答得很像懂。

更可驗證。

---

# 75. Prediction

能否預測：

$$
s_{t+1}.
$$

---

# 76. Explanation

能否提出可被驗證的 mechanism hypothesis。

---

# 77. Intervention

能否預測：

$$
do(a)
$$

的結果。

---

# 78. Reconstruction

能否建立：

$$
\hat X.
$$

---

# 79. Transfer

能否將：

$$
I(X)
$$

與：

$$
F(X)
$$

應用到新系統。

---

# 80. Reconstruction 是第 08 篇的核心

到本篇為止，

我們已經可以說：

$$
\boxed{
\text{Reading}
<
\text{Deconstruction}
<
\text{Operational Verification}.
}
$$

下一個問題：

> 要怎麼證明 AI 不只是會解釋，而是真的掌握到可以工作的程度？

最直接的工程回答是：

$$
\boxed{
\text{Rebuild It}.
}
$$

因此下一篇：

# **08｜理解的工程驗收：如果真的懂，就重建給我看**

將正式建立：

- reconstruction benchmark；
- behavioral equivalence；
- hidden test；
- counterexample；
- cross-domain transfer；
- reconstruction failure taxonomy。

---

# 81. 命題一：Exposure–Understanding 非同一命題

$$
\boxed{
\text{Exposure}
\not\equiv
\text{Operational Understanding}.
}
$$

Raw data 可以支援強大能力，但本身不能作為結構與因果理解的充分證據。

---

# 82. 命題二：Prediction–Identification 非同一命題

$$
\boxed{
\text{Predictive Accuracy}
\not\equiv
\text{Mechanism Identification}.
}
$$

黑箱模型可以高精度預測而沒有可解耦的系統結構。

---

# 83. 命題三：Intervention Strengthening 命題

在可干預系統中，適當 intervention 可以為 latent structure 與 causal mechanism 提供比純觀察更強的辨識約束。

此命題需依系統假設判斷，不宣稱 intervention 自動得到唯一真因果。

---

# 84. 命題四：Functional Typing 命題

跨系統學習若只保存 implementation-specific 名稱，其泛化能力有限。

將：

$$
\text{Source Symbol}
\rightarrow
\text{Functional Type}
$$

是形成 domain structure 的重要步驟。

---

# 85. 命題五：Reconstruction Evidence 命題

若一個解構模型能生成獨立重建，並在未見測試條件下保持功能等價，則其 operational understanding evidence 強於只在已見資料上提供文字描述。

---

# 86. 命題六：Multiple Reconstruction 命題

成功重建：

$$
\hat X
$$

不代表識別到唯一原始 implementation。

因此必須區分：

$$
\boxed{
\text{Functional Equivalence}
}
$$

與：

$$
\boxed{
\text{Implementation Identity}.
}
$$

---

# 87. 命題七：Deconstruction-as-Learning 命題

解構本身可以形成可迭代學習方法：

$$
\boxed{
\mathcal D_{t+1}
=
Update(
\mathcal D_t,
Evidence,
Intervention,
ReconstructionFailure
).
}
$$

因此不只是 AI 學 domain；

AI 也可以學：

> 如何更有效地拆 domain。

---

# 88. 結論

AI 時代最容易產生的一個錯覺是：

> 我們已經把資料餵給模型，所以模型已經學會。

本文認為更精確的描述是：

$$
\boxed{
\text{Raw Exposure}
}
$$

只是知識取得鏈的第一層。

真正要形成可泛化的系統知識，需要逐步完成：

$$
\boxed{
\text{Exposure}
\rightarrow
\text{Parsing}
\rightarrow
\text{Structure}
\rightarrow
\text{Functional Typing}
\rightarrow
\text{Normalization}
\rightarrow
\text{Causal / Invariant Analysis}
\rightarrow
\text{Reconstruction}
\rightarrow
\text{Synthesis}.
}
$$

這不是否定神經模型從大規模資料中自主學習 representation 的能力。

相反，它是在區分：

$$
\boxed{
\text{Implicit Representation}
}
$$

與：

$$
\boxed{
\text{Explicit, auditable, reusable system knowledge}.
}
$$

當目標只是生成相似文字、預測下一步或模仿行為時，隱式 representation 可能已經足夠。

但當目標變成：

> 幫我重新做一個。

> 幫我換一個架構。

> 告訴我哪個部分不能動。

> 把這個方法搬到另一個 domain。

那 AI 需要的就不再只是：

$$
\text{Have Seen}.
$$

而逐漸接近：

$$
\boxed{
\text{Can Decompose}
+
\text{Can Explain}
+
\text{Can Intervene}
+
\text{Can Reconstruct}
+
\text{Can Transfer}.
}
$$

這就是本文所稱的：

# **Deep Deconstructive Learning**

它不是另一種神經網路名稱。

而是一種把人類文明中大量未結構化、已實作、已運行的成果，逐步編譯成 AI 可以重建與重新創造之知識結構的方法論。

---

# 參考資料

1. Locatello, F., Bauer, S., Lucic, M., Rätsch, G., Gelly, S., Schölkopf, B., & Bachem, O. (2019). **Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations.** ICML 2019, PMLR 97:4114–4124.  
   <https://proceedings.mlr.press/v97/locatello19a.html>

2. Locatello, F., Poole, B., Rätsch, G., Schölkopf, B., Bachem, O., & Tschannen, M. (2020). **Weakly-Supervised Disentanglement Without Compromises.** ICML 2020, PMLR 119:6348–6359.  
   <https://proceedings.mlr.press/v119/locatello20a.html>

3. Lachapelle, S. et al. (2022). **Disentanglement via Mechanism Sparsity Regularization: A New Principle for Nonlinear ICA.** CLeaR 2022, PMLR 177:428–484.  
   <https://proceedings.mlr.press/v177/lachapelle22a.html>

4. Ahuja, K., Mahajan, D., Wang, Y., & Bengio, Y. (2023). **Interventional Causal Representation Learning.** ICML 2023, PMLR 202:372–407.  
   <https://proceedings.mlr.press/v202/ahuja23a.html>

5. Rajendran, G., Reizinger, P., Brendel, W., & Ravikumar, P. K. (2024). **An Interventional Perspective on Identifiability in Gaussian LTI Systems with Independent Component Analysis.** CLeaR 2024, PMLR 236:41–70.  
   <https://proceedings.mlr.press/v236/rajendran24a.html>

6. Morioka, H., & Hyvärinen, A. (2024). **Causal Representation Learning Made Identifiable by Grouping of Observational Variables.** ICML 2024, PMLR 235:36249–36293.  
   <https://proceedings.mlr.press/v235/morioka24a.html>

7. Varici, B., Acartürk, E., Shanmugam, K., & Tajer, A. (2024). **General Identifiability and Achievability for Causal Representation Learning.** AISTATS 2024, PMLR 238:2314–2322.  
   <https://proceedings.mlr.press/v238/varici24a.html>

8. Baumgartner, M. W., Lei, A., Watson, J., & Posner, I. (2026). **Disentangling Dynamical Systems: Causal Representation Learning Meets Local Sparse Attention.** CLeaR 2026, PMLR 323:119–165.  
   <https://proceedings.mlr.press/v323/baumgartner26a.html>

9. Ha, D., & Schmidhuber, J. (2018). **World Models.**  
   <https://arxiv.org/abs/1803.10122>

10. Chen, X., Liu, C., & Song, D. (2017). **Towards Synthesizing Complex Programs from Input-Output Examples.**  
    <https://arxiv.org/abs/1706.01284>

11. Gupta, K., Christensen, P. E., Chen, X., & Song, D. (2020). **Synthesize, Execute and Debug: Learning to Repair for Neural Program Synthesis.**  
    <https://arxiv.org/abs/2007.08095>

12. Chen, X., Song, D., & Tian, Y. (2021). **Latent Execution for Neural Program Synthesis.**  
    <https://arxiv.org/abs/2107.00101>

13. Vaduguru, S., Fried, D., & Pu, Y. (2023). **Generating Pragmatic Examples to Train Neural Program Synthesizers.**  
    <https://arxiv.org/abs/2311.05740>

---

## 系列導航

- 01｜AI 時代的資料資產：從「賣資料」到授權可計算知識
- 02｜高品質資料之後：從 Quality Paradigm 到 Novelty Paradigm
- 03｜遊戲不是內容資料：遊戲作為可執行因果世界
- 04｜商業遊戲智能考古：從 AI 名作到普通遊戲群
- 05｜遊戲解構經濟學：成本、難度、資訊增益與研究深度
- 06｜商業遊戲 AI 的隱藏層：真正稀缺的是組合，而非基礎演算法
- 07｜餵資料不等於學習：從 Raw Exposure 到深層解構學習
- 08｜理解的工程驗收：如果真的懂，就重建給我看
- 09｜合成資料之後：從模仿既有設計到探索新穎可執行設計空間
- 10｜慣老闆測試：意圖重建、設計生成與可執行世界考古
