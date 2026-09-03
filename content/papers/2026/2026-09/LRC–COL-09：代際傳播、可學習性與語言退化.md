# LRC–COL-09：代際傳播、可學習性與語言退化
## Intergenerational Transmission, Learnability, and Language Degeneration

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL-07 與 LRC–COL-08 分別處理兩個時間尺度：一個 Agent 需要多少有效 exposure 才能操作理解一個複合 operator，以及一套 operator language 經過多少使用、重組、跨 Agent 傳遞與版本事件後才進入語義穩定窗口。本篇進一步研究第三個時間尺度：

> **一套語言在跨 Agent、跨模型、跨版本甚至跨「世代」傳播時，究竟會保留什麼、壓縮什麼、規則化什麼，又會失去什麼？**

經典 iterated-learning 研究指出，語言必須通過有限的 learning bottleneck：下一代 learner 通常只接觸上一代語言可能產生的一小部分輸入，因此必須從有限樣本重建更大的語言系統。這種瓶頸可以產生對規則化、可學習性與 compositionality 的文化選擇壓力。然而，單獨追求「容易學」並不保證得到高品質語言。若沒有足夠的 communication / expressivity pressure，最簡單、最好傳的系統甚至可能退化成高度 underspecified 的 convention：多個原本需要區分的 meaning 被壓成同一 signal。

2025 年針對 LLM 的 artificial-language iterated-transmission 研究也觀察到類似張力：代際傳播可以提高 learnability 並產生部分結構，但同時可能形成 non-humanlike degenerate vocabularies。這使未來 AI-native composite operator language 面臨一個直接工程問題：

$$
\boxed{
\text{Transmissibility}
\neq
\text{Semantic Preservation}.
}
$$

本文因此把代際傳播描述成：

$$
\boxed{
\mathcal L_g
\xrightarrow{\;\mathcal T_g\;}
D_g
\xrightarrow{\;A_{g+1}\;}
\hat{\mathcal L}_{g+1}
\xrightarrow{\;Use/Revision\;}
\mathcal L_{g+1},
}
$$

其中 $\mathcal L_g$ 是第 $g$ 代語言， $\mathcal T_g$ 是 teacher / channel 的 transmission policy， $D_g$ 是實際傳給下一代的有限資料， $A_{g+1}$ 是 learner。

本文提出四個彼此競爭的傳播目標：

$$
\boxed{
\text{Learnability}
,\quad
\text{Fidelity}
,\quad
\text{Expressivity}
,\quad
\text{Innovation}.
}
$$

其中：

- learnability 要求下一代能以有限成本重建；
- fidelity 要求新一代仍保留前一代 semantic contract；
- expressivity 要求 critical distinctions 仍可被編碼；
- innovation 則允許語言適應新的 Agent、domain 與 world interface。

本文進一步定義 Transmission Bottleneck、Distinction Retention、Transmission Fidelity、Reconstruction Cost、Degeneration Index、Teacher Compression Ratio、Learner Reconstruction Burden、Innovation Rate 與 Transmission Utility。核心候選命題是：傳播 bottleneck 可能存在非單調最佳值 $b^*$。太寬時，learner 可以靠 memorization 傳遞大量 idiosyncratic forms，而缺乏形成簡潔 compositional structure 的壓力；太窄時，critical semantic distinctions 又可能被壓掉。因此：

$$
\boxed{
\text{Optimal Transmission}
\neq
\text{Maximum Fidelity Copying}
\neq
\text{Maximum Compression}.
}
$$

本文最後提出 **Anchored Iterated Transmission（AIT）** 作為未來 COL 的候選工程框架：允許一般 generations 在有限 bottleneck 下傳播與結構化，但定期透過 semantic anchors、invariant probes、world-grounded tests 與 canonical expansions 重新校準，避免語言越傳越容易學卻越來越偏離原始 world distinctions。

本文的總結是：

$$
\boxed{
\text{A language survives not merely by being easy to copy, but by preserving the distinctions that make the language worth having.}
}
$$

---

## 關鍵詞

iterated learning；transmission bottleneck；language degeneration；learnability；expressivity；semantic fidelity；AI emergent language；operator transmission；cultural evolution；compositionality

---

# 1. 問題：傳得下去，到底代表什麼？

假設第 $g$ 代 Agent 使用：

$$
\mathcal L_g.
$$

下一代：

$$
A_{g+1}
$$

沒有直接取得整套 internal state，

而只看到：

- definitions；
- examples；
- conversations；
- operator traces；
- artifacts；
- tool outcomes。

也就是：

$$
\boxed{
D_g
\subset
Behavior(\mathcal L_g).
}
$$

下一代再從：

$$
D_g
$$

重建：

$$
\hat{\mathcal L}_{g+1}.
$$

所以語言傳播本質上不是：

$$
\mathcal L_g
\rightarrow
\mathcal L_g.
$$

而是：

$$
\boxed{
\mathcal L_g
\rightarrow
D_g
\rightarrow
\hat{\mathcal L}_{g+1}.
}
$$

---

# 2. 傳播是一個重建問題

teacher 傳出的不是完整語言，

learner 必須推斷：

- missing meanings；
- composition rules；
- operator boundaries；
- failure conditions；
- type relations。

所以：

$$
\boxed{
\text{Transmission}
=
\text{Compression}
+
\text{Inference}
+
\text{Reconstruction}.
}
$$

---

# 3. 經典 Learning Bottleneck

人類語言文化演化研究早已指出：

> 一個巨大甚至開放式的語言系統，必須透過有限量的 learning data 傳給下一代。

這種：

$$
\boxed{
\text{System Size}
\gg
\text{Observed Transmission Sample}
}
$$

的落差，就是：

$$
\boxed{
\text{Learning Bottleneck}.
}
$$

---

# 4. 為什麼 bottleneck 會促進 compositionality？

如果每個 meaning 都用獨立 holistic signal：

$$
m_i\leftrightarrow s_i,
$$

要完整重建系統，

learner 幾乎必須看過全部 mapping。

但若語言具有：

- parts；
- rules；
- recombination；

則只要學有限 units：

$$
\{o_1,\ldots,o_k\}
$$

與 grammar：

$$
G,
$$

就可重建更大的 closure：

$$
Closure(\mathcal O,G).
$$

所以：

$$
\boxed{
\text{Compositionality}
}
$$

可以被理解為對 transmission bottleneck 的一種適應。

---

# 5. 但 bottleneck 不是越窄越好

如果 bottleneck：

$$
b
$$

極度小，

learner 幾乎沒有足夠 evidence 區分 meanings。

最容易重建的語言可能變成：

$$
m_1,m_2,\ldots,m_n
\rightarrow
s.
$$

只要一個 signal。

這是：

$$
\boxed{
\text{Maximally Learnable}
}
$$

但：

$$
\boxed{
\text{Minimally Expressive}.
}
$$

---

# 6. Learnability–Expressivity Tradeoff

因此：

$$
\boxed{
\text{Learnability}
\leftrightarrow
\text{Expressivity}.
}
$$

一端：

### Holistic Extreme

每個 meaning 都有獨立 signal。

- expressivity 高；
- learnability 差；
- transmission cost 高。

另一端：

### Degenerate Extreme

所有 meaning 共用 signal。

- learnability 極高；
- expressivity 幾乎為零。

---

# 7. Compositionality 是中間解

compositional language 允許：

$$
\boxed{
\text{small reusable basis}
+
\text{large expressive closure}.
}
$$

因此它可能同時滿足：

- 可學；
- 可傳；
- 可泛化；
- 可區分。

這就是 LRC–COL 為何從一開始研究 operator basis。

---

# 8. AI 代際傳播的新版本

對 AI 而言，「generation」不一定是生物世代。

可以是：

- 新模型版本；
- 新 Agent instance；
- 新 context；
- 新公司／系統；
- 新 runtime；
- 下一輪 autonomous retraining；
- 一個 Agent 教另一個 Agent。

所以：

$$
\boxed{
g
=
\text{transmission generation index}.
}
$$

---

# 9. Generational Map

定義：

$$
\boxed{
\mathcal L_{g+1}
=
\Phi(
\mathcal L_g,
\mathcal T_g,
A_{g+1},
E_{g+1}
).
}
$$

其中：

- $\mathcal T_g$：transmission policy；
- $A_{g+1}$：learner；
- $E_{g+1}$：新 environment / domain。

---

# 10. Transmission Dataset

teacher 不會傳所有內容。

定義：

$$
\boxed{
D_g
=
Sample(
\mathcal L_g,
\mathcal T_g,
B_g
).
}
$$

其中：

$$
B_g
$$

是 transmission budget。

---

# 11. Bottleneck Ratio

可以定義：

$$
\boxed{
b_g
=
\frac{
Information(D_g)
}{
InformationRequired(\mathcal L_g)
}.
}
$$

越小：

$$
b_g\downarrow
$$

代表 bottleneck 越窄。

實際 measurement 可能需用：

- coverage；
- MDL；
- entropy；
- semantic distinctions；

代替理想 information。

---

# 12. Exposure Coverage Bottleneck

更可操作：

$$
\boxed{
b_C
=
\frac{
\text{observed semantic / compositional motifs}
}{
\text{relevant motif space}
}.
}
$$

---

# 13. Distinction Coverage Bottleneck

但只看 motif 不夠。

定義 critical distinctions：

$$
\mathcal D^*
=
\{d_1,\ldots,d_m\}.
$$

傳播資料中真正出現多少：

$$
\boxed{
b_D
=
\frac{
|\mathcal D_{observed}^*|
}{
|\mathcal D^*|
}.
}
$$

如果：

$$
b_D\ll1,
$$

rare but important distinctions 很容易消失。

---

# 14. Transmission Fidelity

令 semantic state：

$$
S_g.
$$

下一代：

$$
S_{g+1}.
$$

定義：

$$
\boxed{
F_T(g)
=
1-
D_S(
S_g,
S_{g+1}
).
}
$$

但這只是相鄰世代 fidelity。

---

# 15. Anchor Fidelity

還要對最初或 canonical anchor：

$$
A.
$$

定義：

$$
\boxed{
F_A(g)
=
1-
D_S(
S_g,
A
).
}
$$

因為：

$$
F_T(g)\approx1
$$

每代都只漂一點，

長期：

$$
F_A(g)
$$

仍可能很低。

---

# 16. Incremental Drift Accumulation

如果每代 drift：

$$
\delta_g,
$$

累積：

$$
\boxed{
D_{cum}(G)
\le
\sum_{g=1}^{G}\delta_g
}
$$

是最粗上界。

實際可能：

- cancellation；
- nonlinear amplification；
- attractor convergence。

---

# 17. Distinction Retention

本文提出核心量：

$$
\boxed{
R_{dist}(g)
=
\frac{
|\mathcal D_g^*\cap\mathcal D_0^*|
}{
|\mathcal D_0^*|
}.
}
$$

也就是：

> 原本重要 distinctions 還剩多少？

---

# 18. Distinction 不只是一個詞

critical distinction 可能是：

- accept vs defer；
- preview vs commit；
- simulate vs execute；
- reversible vs irreversible；
- evidence vs inference；
- object vs meta-object。

所以：

$$
\boxed{
R_{dist}
}
$$

比 vocabulary-size retention 更重要。

---

# 19. Vocabulary Retention 可以很高但 Distinction Retention 很低

100 個 token 都還在：

$$
N_g=N_0,
$$

但其中 30 個逐漸變成同義。

則：

$$
R_{vocab}=1
$$

但：

$$
R_{dist}<1.
$$

因此：

$$
\boxed{
\text{Vocabulary Preservation}
\neq
\text{Semantic Preservation}.
}
$$

---

# 20. Vocabulary Degeneration

2025 年 LLM iterated-transmission 研究觀察到：

- 語言可變得更 learnable；
- 但可能發展 non-humanlike degenerate vocabularies；
- distinct signals 減少。

本文把這類現象抽象成：

$$
\boxed{
\text{Vocabulary Degeneration}.
}
$$

---

# 21. Degeneration 不等於 Compression

這是本篇最重要的區分之一。

### Good Compression

不同 meanings 透過：

- shared primitives；
- compositional rules；

仍可重建。

### Degeneration

原本需要的 distinctions：

$$
d_i
$$

不可再從 signal 恢復。

所以：

$$
\boxed{
\text{Compression}
\neq
\text{Information Loss}.
}
$$

好的 compression 可保持 recoverability。

---

# 22. Recoverable Compression

如果：

$$
Decode(
Compress(m)
)
\approx m,
$$

則是：

$$
\boxed{
\text{Recoverable Compression}.
}
$$

若：

$$
m_1,m_2
\rightarrow
s
$$

且無 context 可區分，

則：

$$
\boxed{
\text{Degenerative Collapse}.
}
$$

---

# 23. Semantic Resolution

定義：

$$
\boxed{
R_{sem}
=
\frac{
\text{distinguishable target states}
}{
\text{required target states}
}.
}
$$

退化往往：

$$
R_{sem}\downarrow.
$$

---

# 24. Degeneration Index

第一版：

$$
\boxed{
D_{deg}
=
w_1(1-R_{dist})
+
w_2(1-R_{sem})
+
w_3(1-F_A)
+
w_4 CollapseRate.
}
$$

其中：

$$
CollapseRate
$$

可衡量多個 meaning 被壓成相同 signal 的比例。

---

# 25. Learnability Gain

定義：

$$
\boxed{
G_L(g)
=
T_{learn}(g-1)
-
T_{learn}(g).
}
$$

若：

$$
G_L>0,
$$

新一代更容易學。

---

# 26. 危險的組合

如果：

$$
G_L>0
$$

同時：

$$
D_{deg}>0,
$$

就發生：

$$
\boxed{
\text{Learnability-through-Degeneration}.
}
$$

語言更好學，

只是因為它少表達了東西。

---

# 27. 所以「下一代學得更快」不能當成功指標

真正需要同時看：

$$
\boxed{
Learnability
+
Expressivity
+
Fidelity
+
DistinctionRetention.
}
$$

---

# 28. 四目標傳播模型

本文將傳播目標定為：

$$
\boxed{
\mathbf T
=
(
L,
F,
E,
I
).
}
$$

其中：

- $L$：learnability；
- $F$：fidelity；
- $E$：expressivity；
- $I$：innovation / adaptability。

---

# 29. Learnability

問：

> 下一 Agent 要花多少 exposure / compute 才能掌握？

可用：

$$
T_{\epsilon}^{learn}.
$$

---

# 30. Fidelity

問：

> 下一代是否仍忠於前一代／anchor？

可用：

$$
F_T,F_A.
$$

---

# 31. Expressivity

問：

> critical distinctions 還能不能表達？

可用：

$$
R_{dist},R_{sem}.
$$

---

# 32. Innovation

問：

> 面對新 domain / Agent / world，語言能否長出必要新 distinctions？

若：

$$
I=0
$$

永遠完全複製，

會造成：

$$
\boxed{
\text{Frozen Language}.
}
$$

---

# 33. Innovation 也不是越高越好

如果每代：

$$
I_g\gg0,
$$

language identity 失控。

所以：

$$
\boxed{
\text{Innovation}
\leftrightarrow
\text{Fidelity}.
}
$$

---

# 34. Transmission Pareto Frontier

因此真正最佳 transmission policy：

$$
\boxed{
\mathcal P_T
=
Pareto(
Learnability,
Fidelity,
Expressivity,
Innovation,
Cost
).
}
$$

不存在一個 scalar 能對所有 domain 通用。

---

# 35. Teacher Compression

teacher：

$$
A_g
$$

決定傳什麼。

如果把一整套 operator contract 壓成很短：

$$
D_g^{short},
$$

teacher transmission cost 下降。

定義：

$$
\boxed{
CR_T
=
\frac{
Size(\mathcal L_g)
}{
Size(D_g)
}.
}
$$

稱：

**Teacher Compression Ratio**。

---

# 36. Learner Reconstruction Burden

learner 從壓縮資料重建：

$$
\hat{\mathcal L}_{g+1}.
$$

定義：

$$
\boxed{
B_R
=
C(
D_g
\rightarrow
\hat{\mathcal L}_{g+1}
).
}
$$

若：

$$
CR_T\uparrow,
$$

通常：

$$
B_R\uparrow.
$$

---

# 37. Teacher–Learner Exchange

因此：

$$
\boxed{
\text{Teacher Compression}
\leftrightarrow
\text{Learner Reconstruction}.
}
$$

這和 LRC–COL-05 的 basis-depth tradeoff 同構。

---

# 38. 最大壓縮不是最佳傳播

teacher 只傳：

```text
⊕
```

成本極低，

但 learner 完全不知道意思。

所以：

$$
\boxed{
\max CR_T
\neq
\max TransmissionUtility.
}
$$

---

# 39. Transmission Utility

第一版：

$$
\boxed{
U_T
=
\alpha L
+
\beta F
+
\gamma E
+
\eta I
-
\lambda C_{teach}
-
\mu C_{reconstruct}
-
\nu D_{deg}.
}
$$

---

# 40. Optimal Bottleneck

因此可能存在：

$$
\boxed{
b^*
=
\arg\max_b
U_T(b).
}
$$

這是本篇最重要的新量之一。

---

# 41. Too Wide Bottleneck

如果：

$$
b\rightarrow1,
$$

learner 幾乎看到完整 language。

可能：

- fidelity 高；
- memorization 足夠；
- compositional pressure 低；
- irregular / redundant structures 被完整保留。

---

# 42. Too Narrow Bottleneck

如果：

$$
b\rightarrow0,
$$

learner 只能看到少量 examples。

可能：

- regularization 強；
- learnability 高；
- rare distinction loss 高；
- degeneration risk 高。

---

# 43. Intermediate Bottleneck Hypothesis

所以：

$$
\boxed{
0<b^*<1
}
$$

可能是一般候選。

但 $b^*$ 必須條件化：

- Agent；
- domain；
- risk；
- communication requirement；
- operator complexity。

---

# 44. Communication Pressure 防止退化

經典人工語言研究的重要結果之一：

> 單純 transmission pressure 推動 simplicity，但加入「必須用語言完成 communication」的 expressivity pressure 後，更容易出現既可學又可區分的 compositional structure。

因此：

$$
\boxed{
\text{Transmission Pressure}
+
\text{Communication Pressure}
}
$$

比單純 transmission 更接近良好 language evolution。

---

# 45. COL 的 Communication Pressure 是什麼？

未來 operator language 的「communication」不只人類聊天。

可以是：

- Agent 必須選對 tool；
- compiler 必須產生正確 kernel sequence；
- receiver 必須重建 exact world-state intention；
- multi-agent 必須完成 coordination。

所以：

$$
\boxed{
\text{Operational Success}
}
$$

本身就是 expressivity pressure。

---

# 46. 任務成功作為反退化壓力

如果兩個 critical meanings 被壓成同一 operator，

而這會造成不同 world outcomes，

task failure 會把它們重新分開。

因此：

$$
\boxed{
\text{World Coupling}
}
$$

可以成為語言維持 distinctions 的外部壓力。

---

# 47. LRC 反而能保護語言不退化

語言越接到真實 consequence：

$$
\kappa_{LR}>0,
$$

錯誤合併 distinctions 的代價越可見。

所以：

$$
\boxed{
\text{Grounded Action}
}
$$

可能抑制 purely internal shorthand degeneration。

---

# 48. 但如果 Agent 群只彼此對話？

如果：

$$
A_1\leftrightarrow A_2\leftrightarrow A_3
$$

只需彼此協調，

沒有外部 grounding，

它們可以形成：

$$
\boxed{
\text{Locally Efficient Private Code}.
}
$$

對內成功，

對 world semantics 卻逐漸漂移。

---

# 49. Local Communication Success ≠ Global Semantic Fidelity

因此：

$$
\boxed{
Success_{internal}
\neq
Fidelity_{world}.
}
$$

這與 LRC–COL-08 的 False Convergence 直接接合。

---

# 50. Shared Shorthand Risk

AI 多 Agent 系統可能自然壓縮：

```text
Long Protocol
→ Short Symbol
→ Shared Convention
```

這很好，

但如果新 Agent 或人類無法 recover：

$$
\boxed{
\text{Interoperability}
\downarrow.
}
$$

---

# 51. Interoperability Retention

定義：

$$
\boxed{
R_{interop}(g)
=
P(
ExternalAgent
\text{ can recover semantics}
).
}
$$

通用 COL 不能只讓同一小群 Agent 懂。

---

# 52. Vertical vs Horizontal Transmission

### Vertical

$$
A_g\rightarrow A_{g+1}.
$$

### Horizontal

$$
A_i\leftrightarrow A_j
$$

同一代內互相協調。

兩者壓力不同。

---

# 53. Vertical Pressure

強調：

- learnability；
- reconstructability；
- compression。

---

# 54. Horizontal Pressure

強調：

- coordination；
- local efficiency；
- shared conventions。

---

# 55. 兩者缺一會怎樣？

只有 horizontal：

可能形成難以教給新人的 private shorthand。

只有 vertical：

可能過度追求簡單而退化。

因此：

$$
\boxed{
\text{Healthy Language Evolution}
=
\text{Vertical Learnability}
+
\text{Horizontal Expressivity}.
}
$$

---

# 56. One-to-Many Communication

2024 emergent-communication 研究進一步指出：

多 listener 本身不保證 compositionality。

真正重要的是：

- listeners interests 是否不同；
- 是否需要 coordination。

因此 transmission topology 也是 language structure 的決定因素。

---

# 57. Transmission Topology

令：

$$
G_T=(V,E)
$$

表示 Agent communication graph。

edge：

$$
A_i\rightarrow A_j
$$

代表語言／operator 傳播。

不同 topology：

- chain；
- star；
- mesh；
- hierarchy；
- teacher pool；

可能產生不同 language evolution。

---

# 58. Chain 的風險

$$
A_1\rightarrow A_2\rightarrow\cdots\rightarrow A_n
$$

容易累積：

$$
\boxed{
\text{Telephone-Game Drift}.
}
$$

---

# 59. Multi-Teacher 的好處

如果：

$$
A_{g+1}
$$

同時從：

$$
A_g^1,A_g^2,\ldots
$$

學，

可比較不同 interpretations。

可能降低單一路徑 drift。

---

# 60. Multi-Teacher 的壞處

若 teachers 使用不同 versions：

$$
O@v1,O@v2,
$$

learner 可能混合成：

$$
\boxed{
\text{Version Mixture}.
}
$$

所以 provenance 必須保留。

---

# 61. Canonical Teacher

可以指定：

$$
\boxed{
A_{canon}
}
$$

只負責：

- semantic anchor；
- version；
- regression examples。

其他 Agents 可創新。

---

# 62. 但 Canonical Teacher 不能變成永遠不變的中心

如果 canonical semantics 過時，

會阻止 adaptation。

所以需要：

$$
\boxed{
\text{Versioned Canonical Anchor}.
}
$$

---

# 63. Anchored Iterated Transmission（AIT）

本文提出未來 COL 候選架構：

$$
\boxed{
\text{Anchored Iterated Transmission}.
}
$$

一般 generations：

- 有限 transmission；
- 允許 regularization；
- 允許 innovation。

但每隔：

$$
r
$$

代：

- 重對 canonical anchor；
- 重跑 invariant probes；
- 重跑 world-grounded tasks；
- 檢查 distinction retention。

---

# 64. Anchor Refresh Interval

定義：

$$
\boxed{
r_A
}
$$

每隔多少 transmission generations 重錨。

太頻繁：

- 抑制自然優化；
- 增加成本。

太少：

- drift 累積。

因此可能存在：

$$
r_A^*.
$$

---

# 65. Anchor Refresh 不是 Reset

不是把 learner 強制還原到第 0 代。

而是：

> 保留合法 innovation，只修正 invariant-breaking drift。

所以：

$$
\boxed{
\text{Reground}
\neq
\text{Rollback All}.
}
$$

---

# 66. Stable Core + Evolvable Periphery

AIT 可配合：

$$
\boxed{
\text{Stable Core}
+
\text{Evolvable Periphery}.
}
$$

core：

- transmission fidelity 高；
- bottleneck 寬；
- anchor refresh 頻繁。

periphery：

- bottleneck 較窄；
- innovation 較高；
- 可進行 local optimization。

---

# 67. Rare-Distinction Preservation

傳播最容易丟的是：

$$
p(d_i)\ll1
$$

的 rare distinctions。

所以 teacher sampling 不能只按 frequency。

---

# 68. Risk-Weighted Sampling

對 distinction：

$$
d_i,
$$

sampling probability：

$$
\boxed{
P_{sample}(d_i)
\propto
f_i
+
\lambda Risk_i
+
\mu Novelty_i.
}
$$

讓低頻但 high-criticality distinction 仍會被傳給下一代。

---

# 69. Transmission Curriculum

因此下一代不應只接 random samples。

可分：

### Core Samples
保證 invariants。

### Frequency Samples
反映實際 workload。

### Boundary Samples
防 semantic collision。

### Rare-Critical Samples
防止重要 distinction 消失。

### Novel Composition Samples
維持 compositionality。

---

# 70. Curriculum-Bottleneck 不是單一 b

更完整：

$$
\boxed{
B_T
=
(
b_{core},
b_{freq},
b_{boundary},
b_{rare},
b_{novel}
).
}
$$

所以 optimal bottleneck 是向量問題。

---

# 71. Teacher Selection Problem

teacher 要決定：

> 傳哪一些 examples 最有價值？

這本身就是：

$$
\boxed{
\text{Transmission Query Selection}.
}
$$

與 RLMM 的 VOI 問題同構。

---

# 72. Distinction Value of Information

一個 training example：

$$
e
$$

若能讓 learner 區分：

$$
O_i
$$

與：

$$
O_j,
$$

其 transmission value 高。

可定義：

$$
\boxed{
VOI_T(e)
=
\Delta Fidelity
+
\Delta DistinctionRetention
+
\Delta Transfer
-
Cost(e).
}
$$

---

# 73. 最佳傳播不是傳最多

teacher budget 有限時：

$$
\boxed{
D_g^*
=
\arg\max_{D:Cost(D)\le B}
U_T(D).
}
$$

這是一個 dataset / curriculum selection problem。

---

# 74. Compression 與 Examples 的分工

完整 operator definition 可以短。

但 examples / counterexamples 補足：

- boundary；
- usage；
- grounding。

因此：

$$
\boxed{
\text{Short Formal Core}
+
\text{Rich Sparse Examples}
}
$$

可能是比純文字長定義更好的 transmission packet。

---

# 75. Transmission Packet

每個 stable operator 可傳：

```text
Symbol
Version
Type
Core Invariants
Minimal Expansion
Positive Example
Negative Example
Boundary Example
World-Grounded Probe
Known Confusions
```

這是：

$$
\boxed{
\text{Minimal Semantic Transmission Packet}.
}
$$

---

# 76. 最小 Packet 也是 optimization

packet 太長：

$$
C_{teach}\uparrow.
$$

packet 太短：

$$
C_{reconstruct}\uparrow,
\quad
D_{deg}\uparrow.
$$

因此存在：

$$
\boxed{
P^*_{transmit}.
}
$$

---

# 77. Generational Learnability Curve

可追：

$$
\boxed{
T_{learn}(g).
}
$$

如果：

$$
T_{learn}(g)\downarrow
$$

同時：

$$
R_{dist}(g)\approx1,
$$

這是真正良性 regularization。

---

# 78. Degenerative Learnability Curve

如果：

$$
T_{learn}(g)\downarrow
$$

但：

$$
R_{dist}(g)\downarrow,
$$

則只是退化。

因此兩條曲線必須一起畫。

---

# 79. Fidelity–Learnability Plane

四象限：

### Q1
高 fidelity / 高 learnability  
理想。

### Q2
高 fidelity / 低 learnability  
太複雜但保真。

### Q3
低 fidelity / 高 learnability  
退化 shorthand。

### Q4
低 fidelity / 低 learnability  
全面失敗。

---

# 80. 再加入 Expressivity

真正應看三維：

$$
\boxed{
(L,F,E).
}
$$

加 innovation 後：

$$
\boxed{
(L,F,E,I).
}
$$

---

# 81. Language Degeneration 不只 Vocabulary Collapse

至少四種 degeneration：

### D1 — Vocabulary Collapse
不同 meanings 共用 signals。

### D2 — Boundary Collapse
適用／不適用條件模糊。

### D3 — Type Collapse
原本不同 operator type 混用。

### D4 — Grounding Collapse
Agent 彼此理解，但外部 world semantics 漂移。

---

# 82. D4 最危險

因為內部 communication score 仍可能很高。

所以：

$$
\boxed{
\text{Communication Success}
\neq
\text{Grounded Language Health}.
}
$$

---

# 83. Innovation Degeneration

還有另一個方向：

每代都新增 notation，

但沒有 consolidation。

形成：

$$
\boxed{
\text{Innovation Explosion}.
}
$$

這不是 compression degeneration，

而是 uncontrolled expansion。

---

# 84. 所以語言退化有兩端

### Collapse Degeneration
太簡。

### Fragmentation Degeneration
太亂。

真正 healthy language 位於兩者之間。

---

# 85. Transmission Viability Region

定義：

$$
\boxed{
\mathcal V_T
=
\{
\mathcal L:
L\ge\tau_L,
F\ge\tau_F,
E\ge\tau_E,
I_{min}\le I\le I_{max}
\}.
}
$$

語言 generations 應盡量留在：

$$
\mathcal V_T.
$$

---

# 86. Transmission Hysteresis

與前篇 operator hysteresis 同樣，

語言不應因單一 generation metric 改變就重新設計。

需要：

- promote threshold；
- deprecate threshold；
- anchor-drift threshold。

---

# 87. Generation Churn

如果每代都：

- rename；
- split；
- merge；

新 learner 永遠追不上。

因此：

$$
\boxed{
\text{Transmission Stability}
}
$$

本身也是 learnability 的一部分。

---

# 88. Generation Length

一代要多長？

如果：

$$
G_{length}
$$

太短，

每代 learner 還沒充分使用語言就傳下一代。

如果太長：

- local idiosyncrasy 可能固化；
- adaptation 變慢。

因此也可能存在：

$$
\boxed{
G_{length}^*.
}
$$

---

# 89. Human / AI Generation 不必同尺度

AI generation 可以是：

- 100 tasks；
- 1000 operator uses；
- model update；
- monthly release。

所以應用 event count，

不要只用日曆時間。

---

# 90. Transmission Rate

定義：

$$
\boxed{
r_T
=
\frac{
N_{\text{semantic units transmitted}}
}{
Time
}.
}
$$

太高：

- learner overload。

太低：

- adaptation latency。

---

# 91. Transmission Bandwidth

$$
\boxed{
B_T
=
\frac{
Information(D_g)
}{
TransmissionWindow
}.
}
$$

這是 communication bandwidth 與 learning bottleneck 的接口。

---

# 92. Bottleneck 也可以來自 Context Window

AI learner：

$$
Context_{max}
$$

有限。

若整個 operator library：

$$
Size(\mathcal L)>Context_{max},
$$

自然形成 transmission bottleneck。

---

# 93. Retrieval 可以改變 Bottleneck

有 external memory / retrieval 時：

learner 不必一次內化全部。

因此：

$$
\boxed{
\text{Retrieval}
}
$$

實際上能放寬：

$$
b.
$$

---

# 94. 但 Retrieval 也可能阻止結構化壓力

如果所有 rare mapping 都可隨時查表，

Agent 不必 internalize compositional rule。

因此：

$$
\boxed{
\text{Perfect Retrieval}
}
$$

也可能降低形成 compact internal basis 的壓力。

這是非常值得後續實驗的新命題。

---

# 95. Memory–Composition Tradeoff

因此：

$$
\boxed{
\text{External Memory}
\leftrightarrow
\text{Internal Compositionality}.
}
$$

更多外部查表能力可能允許較多 idiosyncratic forms 存活。

---

# 96. 這對 AI 特別重要

人類記憶 bottleneck 很強。

AI 可以有：

- huge storage；
- perfect logs；
- retrieval。

所以人類語言演化的 bottleneck 結論不能原封不動移植。

COL 必須重新研究：

$$
\boxed{
b^*(A,R,C).
}
$$

---

# 97. AI Bottleneck 可以被人工設計

這是人類自然語言沒有的巨大差別。

我們可以主動控制：

- transmission packet；
- retrieval availability；
- example diversity；
- anchor refresh；
- memory retention；
- versioning。

因此：

$$
\boxed{
\text{Language Evolution}
}
$$

第一次可以變成：

$$
\boxed{
\text{partly engineered cultural evolution}.
}
$$

---

# 98. 但不能過度優化

如果 designer 完全控制所有 transmission，

語言可能過度適配當前 Agent。

未來新 architecture：

$$
A'
$$

反而學不好。

所以要保留：

- cross-model tests；
- open-world probes；
- diversity。

---

# 99. Transmission Robustness

定義：

$$
\boxed{
R_T
=
Performance(
\mathcal L
\text{ transmitted across heterogeneous }A_i
).
}
$$

通用 COL 應追：

$$
R_T.
$$

---

# 100. Cross-Model Generation Chain

例如：

$$
GPT\rightarrow
Qwen\rightarrow
Llama\rightarrow
Other.
$$

不要求同一模型 family。

這比同模型自我傳播更能測：

$$
\boxed{
\text{model-independent semantics}.
}
$$

---

# 101. Translation vs Transmission

如果不同 Agent 有不同 local basis：

$$
\mathcal L_A,\mathcal L_B,
$$

可以用：

$$
\Phi_{AB}
$$

translation。

這時傳播不是：

$$
\mathcal L_A\rightarrow\mathcal L_A,
$$

而是：

$$
\boxed{
\mathcal L_A
\rightarrow
\Phi_{AB}
\rightarrow
\mathcal L_B.
}
$$

---

# 102. Translation Fidelity

定義：

$$
\boxed{
F_{\Phi}
=
1-
D_S(
Sem_A,
TranslateBack(Sem_B)
).
}
$$

這也需要進 overall transmission fidelity。

---

# 103. Universal Interchange Layer

可能存在：

$$
\boxed{
\mathcal L_I
}
$$

作為跨 Agent canonical interchange language。

各 Agent：

$$
\mathcal L_i
\leftrightarrow
\mathcal L_I.
$$

這可以降低 pairwise translation：

$$
O(n^2)
$$

到：

$$
O(n).
$$

---

# 104. 但 Interchange Layer 也可能成為 Bottleneck

如果：

$$
\mathcal L_I
$$

太貧乏，

local languages 的 distinctions 會被壓掉。

所以 interchange language 也要測：

$$
R_{dist}.
$$

---

# 105. 本篇十二個正式命題

## TR-P1 — Bottleneck Structuring
有限 transmission bottleneck 可對語言施加規則化／compositionality 壓力。

## TR-P2 — Degenerate Learnability
單獨最大化 learnability 可能導致 underspecified degenerate language。

## TR-P3 — Expressivity Counterpressure
communication / operational pressure 可以防止 pure simplicity collapse。

## TR-P4 — Intermediate Bottleneck
傳播效用對 bottleneck size 可能非單調，存在 $b^*$。

## TR-P5 — Distinction Retention
vocabulary retention 不足以衡量 semantic preservation，應追蹤 $R_{dist}$。

## TR-P6 — Teacher–Learner Exchange
teacher compression 增加時，learner reconstruction burden 通常上升。

## TR-P7 — Grounding Protection
world-grounded action pressure 可抑制只對 Agent 內部有效的 shorthand degeneration。

## TR-P8 — Vertical–Horizontal Complementarity
vertical transmission 主要施加 learnability pressure，horizontal interaction 主要施加 expressivity / coordination pressure；兩者共同決定 language form。

## TR-P9 — Anchored Iterated Transmission
週期性 semantic anchor / invariant probes 可降低 cumulative drift，同時保留有限 innovation。

## TR-P10 — Rare-Critical Preservation
sampling curriculum 必須 risk-weight rare distinctions，不能只按 frequency。

## TR-P11 — Retrieval–Composition Tradeoff
強 external retrieval 可能放寬 transmission bottleneck，但同時降低 internal compositional pressure。

## TR-P12 — Engineered Cultural Evolution
AI-native operator language 的 transmission bottleneck、curriculum、memory 與 anchor 可以被主動設計，因此 language evolution 部分可工程化。

---

# 106. 第一版實驗：Bottleneck Sweep

建立固定 meaning space：

$$
\Omega.
$$

bottleneck：

$$
b=
1.0,
0.75,
0.5,
0.25,
0.1.
$$

每個 condition 做多代 transmission。

量：

- $T_{learn}(g)$ ；
- $F_A(g)$ ；
- $R_{dist}(g)$ ；
- compositionality；
- vocabulary size；
- task success。

---

# 107. Communication Pressure Ablation

兩條：

### Transmission Only

只要求 learner 重建 language。

### Transmission + Use

每代還必須用語言完成 communication / tool task。

比較 degeneration。

---

# 108. Anchor Ablation

### No Anchor

純 chain。

### Static Anchor

每代看到 canonical definition。

### Periodic Anchor

每 $r$ 代 reground。

### Invariant-Only Anchor

只給 core invariants。

測：

- drift；
- innovation；
- learnability。

---

# 109. Rare-Distinction Test

設：

$$
p(d_{critical})=0.01
$$

但 error cost 高。

比較：

### Frequency Sampling

### Risk-Weighted Sampling

看是否保住：

$$
R_{dist}.
$$

---

# 110. Teacher Compression Sweep

Transmission packet：

- full；
- 50%；
- 25%；
- 10%；
- symbol-only。

測 learner：

$$
B_R,
T_{learn},
F_A.
$$

找 transmission sweet spot。

---

# 111. Retrieval Condition

比較：

### No External Memory

learner 只能靠 transmission。

### Full Retrieval

所有 legacy examples 可查。

### Selective Retrieval

只允許 query canonical anchor / rare cases。

測 compositional pressure 與 degeneration。

---

# 112. Heterogeneous-Agent Chain

用不同 Agent / model family 逐代傳。

比同模型 chain 更能測：

$$
R_T.
$$

---

# 113. Topology Experiment

比較：

- chain；
- one teacher → many learners；
- many teachers → one learner；
- mesh；
- hierarchy。

量：

- convergence；
- fidelity；
- innovation；
- degeneration。

---

# 114. Generational Output

每一代保存：

```text
Generation
Vocabulary Size
Operator Graph
Learnability
Anchor Fidelity
Adjacent Fidelity
Distinction Retention
Semantic Resolution
Innovation Rate
Degeneration Index
Transmission Cost
Reconstruction Cost
```

---

# 115. Language Health Dashboard

整體可以壓成：

$$
\boxed{
\mathbf H_g
=
(
L_g,
F_g,
E_g,
I_g,
D_{deg,g},
C_g
).
}
$$

不要只看：

> generation 10 accuracy。

---

# 116. 什麼才算良性語言演化？

候選判準：

$$
T_{learn}(g)\downarrow
$$

同時：

$$
F_A(g)\ge\tau_F,
$$

$$
R_{dist}(g)\ge\tau_D,
$$

$$
D_{deg}(g)\le B_D.
$$

這才是：

$$
\boxed{
\text{Learnability without Degeneration}.
}
$$

---

# 117. 長期極限不一定存在

可能：

$$
\mathcal L_g
\rightarrow
\mathcal L^*
$$

穩定。

也可能：

- limit cycle；
- branching；
- repeated innovation；
- periodic re-anchoring。

因此不假設：

$$
\lim_{g\to\infty}\mathcal L_g
$$

必然存在。

---

# 118. Branching Language Evolution

不同 Agent groups：

$$
P_1,P_2
$$

可能形成：

$$
\mathcal L_1,\mathcal L_2.
$$

這不一定是 failure。

可能是：

- domain specialization；
- local efficiency。

但需要 interchange / translation。

---

# 119. Language Speciation

當兩個 branches：

$$
F_{\Phi}
$$

太低，

可能形成：

$$
\boxed{
\text{Language Speciation}.
}
$$

也就是不再是同一語言版本，而是不同 language family。

---

# 120. 通用傳播的真正目標

不是阻止任何分叉。

而是：

$$
\boxed{
\text{preserve a recoverable common semantic substrate}.
}
$$

即使 surface dialects 分化。

---

# 121. Common Semantic Kernel

因此再次回到：

$$
\boxed{
\mathcal O_{kernel}.
}
$$

可能：

- surface language 演化快；
- kernel semantic invariants 演化慢。

這是跨世代通用傳播的一個強候選架構。

---

# 122. Kernel Transmission

kernel packet 要特別高 fidelity：

- type；
- invariant；
- expansion；
- world test；
- version。

surface macro 可以有更高 plasticity。

---

# 123. 這與 LRC–COL-05 的雙層 ISA 合流

前面：

$$
\mathcal O_{surface}
\rightarrow
\mathcal O_{kernel}^*.
$$

現在：

$$
\boxed{
\text{surface evolves faster}
,\qquad
\text{kernel transmits more conservatively}.
}
$$

因此 dual-level basis 不只是 execution architecture，

也是 transmission architecture。

---

# 124. 本篇核心公式組

代際傳播：

$$
\boxed{
\mathcal L_g
\xrightarrow{\mathcal T_g}
D_g
\xrightarrow{A_{g+1}}
\mathcal L_{g+1}.
}
$$

bottleneck：

$$
\boxed{
b_g
=
\frac{
Information(D_g)
}{
InformationRequired(\mathcal L_g)
}.
}
$$

distinction retention：

$$
\boxed{
R_{dist}(g)
=
\frac{
|\mathcal D_g^*\cap\mathcal D_0^*|
}{
|\mathcal D_0^*|
}.
}
$$

degeneration：

$$
\boxed{
D_{deg}
=
w_1(1-R_{dist})
+w_2(1-R_{sem})
+w_3(1-F_A)
+w_4CollapseRate.
}
$$

optimal bottleneck：

$$
\boxed{
b^*
=
\arg\max_bU_T(b).
}
$$

---

# 125. 非主張

本文不主張：

1. 人類 iterated-learning 結果可直接無修改套用到 LLM；
2. transmission bottleneck 越窄一定越 compositional；
3. compositionality 自動等於高 semantic fidelity；
4. vocabulary 縮小一定是 degeneration；
5. LLM 代際傳播一定退化；
6. communication pressure 能完全防止 drift；
7. universal optimal bottleneck $b^*$ 存在；
8. external retrieval 一定降低 compositionality；
9. canonical anchor 應永遠不變；
10. AI cultural evolution 可以被完全控制。

本文只提出：

$$
\boxed{
\text{Intergenerational operator-language transmission should be evaluated as a tradeoff among learnability, fidelity, expressivity, innovation, reconstruction cost, and semantic degeneration under an explicit transmission bottleneck.}
}
$$

---

# 126. 文獻錨點

1. **Cultural evolution: implications for understanding the human language faculty and its evolution（Philosophical Transactions of the Royal Society B, 2008）**  
   系統說明 iterated learning 與 learning bottleneck 如何形成對可學習、可泛化結構的文化選擇壓力；compositionality 可被理解為巨大表達空間通過有限學習資料瓶頸的一種適應。

2. **Kirby et al. 系列 iterated-learning / communication experiments（2008–2015；後續綜述）**  
   相關實驗與理論指出，單純 simplicity / learnability pressure 可導致 underspecified 或 degenerate systems；加入 communication / expressivity pressure 後，語言更可能形成兼顧可學習與可區分性的 compositional structure。

3. **Searching for Structure: Investigating Emergent Communication with Large Language Models（COLING 2025）**  
   LLM artificial-language iterated transmission 可提高 learnability 並產生一些 structure，但同時可能形成 non-humanlike degenerate vocabularies。這是本文 AI 代際傳播問題最直接的近期錨點。

4. **Frequency & Compositionality in Emergent Communication（EMNLP 2025）**  
   顯示 compositionality 不是 frequency 本身的直接函數，limited exposure 是重要驅動。這支持 transmission curriculum / bottleneck 不能只用 raw frequency 設計。

5. **One-to-Many Communication and Compositionality in Emergent Communication（EMNLP 2024）**  
   多 listener 本身不保證 compositionality；不同 listener interests 與 coordination requirements 會改變 emergent language structure，支持 transmission topology 進入模型。

6. **Cultural evolution creates the statistical structure of language（Scientific Reports, 2024）**  
   進一步展示 iterated learning 可讓語言統計結構在傳播中成為 learnability 的原因與結果，支持「語言會適應 learner」的動態觀點。

7. **Efficiency fosters cumulative culture across species（Philosophical Transactions B, 2021）**  
   綜述語言與文化系統中的 information bottleneck、expressivity 與 compression 交換，提供「傳播受限會選擇更有效結構」的廣泛理論背景。

---

# 127. 下一篇

## LRC–COL-10：多 Agent 傳播拓撲與複合性形成
### Multi-Agent Transmission Topology and the Emergence of Compositional Structure

下一篇將不再把：

$$
A_g\rightarrow A_{g+1}
$$

當成單一線性 chain。

而正式研究：

$$
\boxed{
G_T=(V,E)
}
$$

不同 communication topology 如何改變：

- operator convergence；
- dialect branching；
- compositionality；
- minority innovation；
- false consensus；
- semantic drift；
- transmission speed；
- local shorthand；
- common kernel。

將比較：

- one-to-one；
- one-to-many；
- many-to-one；
- mesh；
- hierarchy；
- modular communities；
- rotating teacher；
- federated multi-Agent。

並問：

> **一套複合 AI 語言到底應該由「中央標準」傳下去，還是讓多 Agent 局部演化再經 common kernel 對齊？**

這會是第 11 篇 Operator Basis Adaptation Law 之前，最後一塊群體動力學基礎。

**END — LRC–COL-09 v0.1**
