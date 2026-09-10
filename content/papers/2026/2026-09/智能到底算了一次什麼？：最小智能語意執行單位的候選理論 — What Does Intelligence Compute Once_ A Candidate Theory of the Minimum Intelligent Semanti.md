# 智能到底算了一次什麼？：最小智能語意執行單位的候選理論

## What Does Intelligence Compute Once? A Candidate Theory of the Minimum Intelligent Semantic Execution Unit

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**英文系列：** *Physical Metrology of Intelligence: From Minimal Semantic Execution to Quality and Computational Spacetime*  
**系列編號：** EML-IPM  
**篇次：** Paper 02 / 10  
**文件編號：** EML-IPM-02  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開純理論論文  
**工程狀態：** 無 MVP；本文建立候選計量本體，不宣稱已發現唯一神經或模型內部「智能原子」

---

## 摘要

如果 token 不是智能的最小計算單位，FLOP 也不是，attention head、neuron activation、layer、forward pass 亦不是，那麼：

$$
\boxed{
\textbf{
智能到底「算了一次」什麼？
}
}
$$

這是智能物理計量學最基礎、也最危險的問題。若這一步定義錯誤，後續所有「每焦耳智能」「每秒智能」「單次智能產率」都只會變成把錯誤 proxy 精密化。

本文提出 **最小智能語意執行單位**：

$$
\boxed{
\mu_I
=
\text{Minimum Intelligent Semantic Execution Unit}
}
$$

但本文刻意不把 $\mu_I$ 定義成某一種硬體事件，也不把它定義成某一個固定神經結構。相反地， $\mu_I$ 被定義為：

> **對某個已指定任務之求解狀態，造成最小可辨識、具因果效用、且可被後續推理利用的語意狀態轉換。**

形式上：

$$
\boxed{
z_t
\xrightarrow{\mu_I}
z_{t+1}
}
$$

其中 $z_t$ 與 $z_{t+1}$ 是 task-relative semantic solution state。

 $\mu_I$ 必須至少滿足七個條件：

$$
\boxed{
\mathcal C_{\mu}
=
(
C_T,
C_S,
C_C,
C_N,
C_K,
C_R,
C_P
)
}
$$

其中：

- $C_T$：Task Relevance，與指定任務相關；
- $C_S$：State Change，確實改變求解狀態；
- $C_C$：Causal Contribution，對後續成果具有因果貢獻；
- $C_N$：Non-decomposability at the chosen semantic resolution，在指定語意解析度下不可再拆而不失去該功能；
- $C_K$：Composability，可組合成更高階認知操作；
- $C_R$：Realization Independence，語意單位不綁死單一模型或硬體；
- $C_P$：Physical Realizability，必須能向下對應到實際物理執行軌跡。

因此：

$$
\boxed{
Token
\neq
\mu_I
}
$$

因為 token 是表達／序列單位，不保證對求解狀態產生有效語意轉換。

同樣：

$$
\boxed{
FLOP
\neq
\mu_I
}
$$

因為 FLOP 是算術原語，沒有 task semantics。

以及：

$$
\boxed{
NeuronActivation
\neq
\mu_I
}
$$

因為一個語意轉換可能分散於大量神經元、層、注意力路徑與記憶存取中；反過來，一個單一 activation 也未必具有可獨立辨識的語意功能。

本文進一步提出：

$$
\boxed{
\mu_I
\neq
\text{Thought}
}
$$

因為「想法」通常太大、太語言化、太依賴觀察者切分，無法作為穩定計量原子。

因此 $\mu_I$ 不是 literal atom，而是 **最小可用語意解析單位（minimum useful semantic resolution）**。它的最小性是：

$$
\boxed{
\text{resolution-relative}
}
$$

而不是宇宙中存在一個唯一、絕對的「智能量子」。

本文提出四個主要候選族：

$$
\boxed{
\mathcal M_{\mu}
=
(
M_B,
M_R,
M_C,
M_I
)
}
$$

其中：

- $M_B$：Belief Update Unit，信念更新單位；
- $M_R$：Relation Construction Unit，關係建立／改寫單位；
- $M_C$：Constraint Resolution Unit，約束消解單位；
- $M_I$：Information-Gain / Uncertainty-Reduction Unit，資訊增益／不確定性下降單位。

本文並主張，真正成熟的 $\mu_I$ 很可能不是以上四者中的單一一種，而是一個共同形式：

$$
\boxed{
\mu_I
=
\Delta z
\;\text{such that}\;
\Delta z
\text{ is task-relevant, causally useful, and semantically non-redundant}.
}
$$

為了避免把「大量內部活動」誤認成「大量有效智能」，本文再定義：

$$
\boxed{
N_{\mu}^{\mathrm{gross}}
}
$$

為所有候選語意轉換數，

以及：

$$
\boxed{
N_{\mu}^{\mathrm{eff}}
}
$$

為實際對最終成果具有因果效用的有效語意轉換數。

其效率為：

$$
\boxed{
\eta_{\mu}
=
\frac{
N_{\mu}^{\mathrm{eff}}
}{
N_{\mu}^{\mathrm{gross}}
}.
}
$$

這使我們可以區分：

$$
\boxed{
\text{Semantic Activity}
\neq
\text{Effective Intelligent Work}.
}
$$

最後，本文建立 $\mu_I$ 的跨層對映：

$$
\boxed{
\mu_I
\rightarrow
\rho_C(\mu_I)
\rightarrow
\rho_P(\mu_I)
\rightarrow
\rho_T(\mu_I)
}
$$

其中：

- $\rho_C$：algorithmic/computational realization；
- $\rho_P$：physical execution trace；
- $\rho_T$：thermodynamic realization。

因此真正的智能物理學問題不再是：

> 一個 token 要多少焦耳？

而是：

$$
\boxed{
\textbf{
完成一個有效的最小語意狀態轉換，
在某個模型與硬體上需要多少實際物理計算？
}
}
$$

本文終端命題為：

$$
\boxed{
\textbf{
智能的最小計量單位不應由輸出格式決定，
也不應由硬體原語決定；
它應由「對求解狀態造成的最小有效語意改變」決定，
再向下追蹤其物理實現。
}
}
$$

**關鍵詞：** MISEU、Minimum Intelligent Semantic Execution Unit、Semantic State Transition、Belief Update、Constraint Resolution、Information Gain、Physical Metrology of Intelligence

---

# 1. 為什麼 token 不是答案

Token 是：

$$
\boxed{
\text{representation / serialization unit}.
}
$$

它適合：

- 計價；
- context budgeting；
- decoding；
- throughput。

但它並不保證代表：

$$
\boxed{
\text{one unit of intelligence}.
}
$$

---

# 2. 相同 token 可以沒有相同語意工作

例如：

> 好的好的好的好的。

和：

> 因此 $A\Rightarrow B$ 與 $B\Rightarrow C$ 可推出 $A\Rightarrow C$。

token 數可能相近。

但：

$$
\boxed{
SemanticWork_1
\neq
SemanticWork_2.
}
$$

---

# 3. 同一語意也可以使用不同 token 數表達

所以：

$$
\boxed{
SemanticUnit
\not\propto
TokenCount.
}
$$

---

# 4. FLOP 也不是答案

FLOP 是 floating-point operation。

它描述：

$$
a+b,
\quad
a\times b
$$

這類算術操作。

---

# 5. 但一個 FLOP 沒有 task semantics

$$
\boxed{
FLOP
\neq
BeliefUpdate.
}
$$

$$
\boxed{
FLOP
\neq
RelationFormation.
}
$$

---

# 6. 同樣 FLOPs 可以實現不同智能功能

同一矩陣乘法形式：

$$
Y=XW
$$

可以在：

- vision；
- language；
- control；
- protein modeling；

中執行完全不同語意角色。

---

# 7. 所以 FLOP 是 implementation primitive

不是 semantic primitive。

---

# 8. Neuron activation 也不夠

如果我們說：

> 一個 neuron fire 就是一個智能單位。

問題立刻出現。

---

# 9. 分散表示

現代神經網路中的語意通常不是：

$$
Concept\leftrightarrow OneNeuron.
$$

更常是：

$$
\boxed{
Concept
\leftrightarrow
DistributedPattern.
}
$$

---

# 10. 一個語意轉換可以跨越多層

例如：

$$
Relation(A,B)
$$

的建立可能涉及：

- attention；
- MLP；
- residual stream；
- memory retrieval；
- routing。

---

# 11. 因此：

$$
\boxed{
NeuronActivation
\neq
SemanticExecutionUnit.
}
$$

---

# 12. Layer 也不是單位

一層 Transformer block 可以同時完成大量不同功能。

所以：

$$
\boxed{
Layer
\neq
OneIntelligentOperation.
}
$$

---

# 13. Forward pass 也太粗

完整 forward pass 可能同時包含：

$$
\mu_1,\mu_2,\ldots,\mu_k.
$$

它更像一次大規模物理實現，而不是語意最小單位。

---

# 14. 「想法」又太大

人可以說：

> 我剛剛想到一個方法。

但這個「一個想法」內部可能包含：

- 關係辨識；
- 約束消除；
- 類比；
- 目標重構；
- 結論生成。

---

# 15. 所以：

$$
\boxed{
Thought
\neq
MinimumSemanticExecution.
}
$$

---

# 16. 我們真正需要的是中間層

即：

$$
\boxed{
PhysicalPrimitive
\rightarrow
SemanticPrimitive
\rightarrow
TaskAchievement.
}
$$

---

# 17. 定義 task-relative solution state

令：

$$
z_t
$$

表示時刻 $t$ 的求解語意狀態。

---

# 18. $z_t$ 可以包含

$$
z_t=
(
B_t,
R_t,
C_t,
G_t,
U_t
)
$$

其中：

- $B_t$：beliefs；
- $R_t$：relations；
- $C_t$：constraints；
- $G_t$：goals/subgoals；
- $U_t$：uncertainty。

---

# 19. 這不是要求模型內部真的有這五個欄位

它是 observer-level semantic state abstraction。

---

# 20. 最小智能語意執行單位

本文定義：

$$
\boxed{
\mu_I:
z_t\rightarrow z_{t+1}
}
$$

其中：

$$
z_{t+1}\neq z_t.
$$

---

# 21. 但「有變」仍不夠

如果只是：

> 把句子改寫得更長。

可能：

$$
z_{t+1}
$$

在任務求解上沒有實質進展。

---

# 22. 所以需要 Task Relevance

第一條：

$$
\boxed{
C_T:
\Delta z
\text{ must be task-relevant}.
}
$$

---

# 23. 第二條：State Change

$$
\boxed{
C_S:
d(z_t,z_{t+1})>\epsilon.
}
$$

在指定解析度下必須存在可辨識改變。

---

# 24. 第三條：Causal Contribution

如果移除該轉換：

$$
do(\mu_I=0)
$$

最終成果會受到可檢出的負面影響。

---

# 25. 形式：

$$
\boxed{
Q(Y\mid \mu_I)
>
Q(Y\mid do(\mu_I=0))
}
$$

至少在期望意義下成立。

---

# 26. 這使 $\mu_I$ 不只是相關事件

而是有效工作。

---

# 27. 第四條：Non-decomposability

在指定 semantic resolution $\delta$ 下，

若：

$$
\mu_I=\mu_a\oplus\mu_b
$$

且 $\mu_a,\mu_b$ 各自仍能單獨保有同樣可辨識語意功能，

那原本 $\mu_I$ 就不是最小。

---

# 28. 但「最小」不是絕對

這是本文最重要的保守條件之一：

$$
\boxed{
Minimality
=
Minimality(\delta,Task,Observer).
}
$$

---

# 29. 為什麼不能要求絕對最小

因為不同觀察尺度下：

- 一個 proof step 可以拆成 algebra steps；
- algebra step 又可拆成 symbolic rewrites；
- symbolic rewrite 又可拆成 machine instructions。

永遠可以往下拆。

---

# 30. 所以 $\mu_I$ 是 minimum useful semantic resolution

不是 metaphysical atom。

---

# 31. 第五條：Composability

更高階推理必須能表示成：

$$
\boxed{
\Pi=
\mu_1\oplus\mu_2\oplus\cdots\oplus\mu_n.
}
$$

---

# 32. 否則它不能成為計量學單位

如果每個 $\mu_I$ 都不能組合，就無法建立總工作量。

---

# 33. 第六條：Realization Independence

同樣的語意轉換可以在不同架構上實現。

例如：

$$
A>B,\quad B>C
\Rightarrow
A>C.
$$

---

# 34. Transformer、symbolic engine、人腦都可能完成

所以：

$$
\boxed{
\mu_I
\neq
\text{specific hardware event}.
}
$$

---

# 35. 第七條：Physical Realizability

但 realization independence 不代表脫離物理。

每個真正執行的 $\mu_I$ 必須存在：

$$
\boxed{
\rho_P(\mu_I)
}
$$

即某個物理 trace。

---

# 36. 所以語意不等於非物理

而是：

$$
\boxed{
\text{Semantic Type}
\neq
\text{Physical Token}
}
$$

但：

$$
\boxed{
\text{Semantic Event}
\Rightarrow
\text{Physical Realization}.
}
$$

---

# 37. 七條條件總結

$$
\boxed{
\mathcal C_{\mu}
=
(
C_T,C_S,C_C,C_N,C_K,C_R,C_P
).
}
$$

---

# 38. Candidate Family A：Belief Update

第一個候選：

$$
\boxed{
M_B:
B_t\rightarrow B_{t+1}.
}
$$

---

# 39. 例子

原本：

$$
P(H)=0.4.
$$

得到新推論後：

$$
P(H)=0.8.
$$

---

# 40. 這明顯是一個語意狀態改變

而且與 Bayesian cognition、predictive processing、decision theory 都有天然連結。

---

# 41. 優點

Belief update：

- 可形式化；
- 可比較前後；
- 可定義 information gain。

---

# 42. 缺點

不是所有智能活動都可自然寫成 belief probability update。

例如：

- 產生新概念；
- 建構資料結構；
- 創造新 relation。

---

# 43. Candidate Family B：Relation Construction

第二類：

$$
\boxed{
M_R:
R_t\rightarrow R_{t+1}.
}
$$

---

# 44. 例

原本知道：

$$
A,\quad B
$$

但不知道它們之間關係。

---

# 45. 執行後得到：

$$
R(A,B)=\text{causal}.
$$

或：

$$
R(A,B)=\text{equivalent under condition }C.
$$

---

# 46. 這特別適合：

- mathematics；
- analogy；
- causal reasoning；
- conceptual synthesis。

---

# 47. 缺點

若 relation space 定義不佳，幾乎所有活動都可以被說成「建立關係」。

所以需要 task-relative restriction。

---

# 48. Candidate Family C：Constraint Resolution

第三類：

$$
\boxed{
M_C:
\mathcal C_t\rightarrow\mathcal C_{t+1}.
}
$$

---

# 49. 一個問題常可以視為 constraint set

例如：

$$
\mathcal C=
\{c_1,c_2,\ldots,c_n\}.
$$

---

# 50. 一次有效執行可能：

- 消除一個不可能分支；
- 固定一個變數；
- 發現一個衝突；
- 合併兩個約束。

---

# 51. 例

程式 debugging：

$$
Failure
\Rightarrow
\neg H_1.
$$

這就消除一個 hypothesis branch。

---

# 52. 優點

Constraint resolution 特別適合：

- code；
- proof；
- planning；
- search。

---

# 53. 缺點

創意生成中的「增加新可能」不總是 reduction。

有時：

$$
|\mathcal C_{t+1}|>|\mathcal C_t|.
$$

---

# 54. Candidate Family D：Information Gain

第四類：

$$
\boxed{
M_I:
U_t\rightarrow U_{t+1},
\quad
U_{t+1}<U_t.
}
$$

---

# 55. 例如 entropy reduction

$$
\boxed{
IG=
H(Z_t)-H(Z_{t+1}).
}
$$

---

# 56. 優點

這很容易與：

- information theory；
- neuroscience；
- thermodynamics；

往下接。

---

# 57. 缺點

智能不只是在減少 uncertainty。

創造問題、生成候選、增加 hypothesis space 有時會暫時：

$$
H(Z_{t+1})>H(Z_t).
$$

但卻是更高品質推理的重要一步。

---

# 58. 所以 Information Gain 不能單獨定義智能

---

# 59. 統一形式

本文暫時把四個候選統一為：

$$
\boxed{
\mu_I
=
\Delta z_{\text{task}}
}
$$

其中：

$$
\Delta z_{\text{task}}
\neq0
$$

且具有後續因果效用。

---

# 60. Semantic State 可以展開為

$$
\boxed{
z=
(B,R,C,G,U,\Pi)
}
$$

新增：

$$
\Pi
=
\text{available procedures / strategies}.
$$

---

# 61. 因此一個 $\mu_I$ 可以改變任一分量

例如：

$$
\Delta B\neq0
$$

或者：

$$
\Delta R\neq0
$$

或者：

$$
\Delta C\neq0.
$$

---

# 62. 甚至允許同時改變多個分量

只要在目前解析度下不能被可靠地拆成更小獨立功能。

---

# 63. 語意單位不是固定大小

這一點非常重要。

不同任務：

$$
\mu_I^{math}
\neq
\mu_I^{vision}
\neq
\mu_I^{planning}.
$$

---

# 64. 但可以共享共同公理

即：

$$
\boxed{
\mathcal C_{\mu}
}
$$

相同。

---

# 65. 所以我們追求的是 typed semantic units

而不是一個所有領域同字面內容的 operation。

---

# 66. Type System

可以寫：

$$
\boxed{
\mu_I:\mathrm{Type}[d]
}
$$

其中 $d$ 是 domain。

---

# 67. 例如：

$$
\mu_I:\mathrm{Type}[MathRelation]
$$

$$
\mu_I:\mathrm{Type}[CodeConstraint]
$$

$$
\mu_I:\mathrm{Type}[VisualComposition].
$$

---

# 68. Typed 不代表不可比較

因為跨類型仍可比較：

$$
PhysicalCost(\mu_I).
$$

---

# 69. 以及對最終成果的 causal contribution

$$
Contribution(\mu_I\rightarrow Q).
$$

---

# 70. Gross Semantic Activity

模型內部可能發生大量：

$$
\mu_1,\mu_2,\ldots,\mu_n
$$

候選轉換。

---

# 71. 但不是全部都有效

可能存在：

- 重複推理；
- dead-end；
- 自我矛盾；
- 無關聯想；
- 被後續完全撤回的中間工作。

---

# 72. 所以定義：

$$
\boxed{
N_{\mu}^{gross}
}
$$

所有識別到的 candidate semantic executions。

---

# 73. Effective Semantic Work

定義：

$$
\boxed{
N_{\mu}^{eff}
}
$$

對最終成果具正向因果效用的單位。

---

# 74. 語意效率

$$
\boxed{
\eta_{\mu}
=
\frac{
N_{\mu}^{eff}
}{
N_{\mu}^{gross}
}.
}
$$

---

# 75. 這可以測「繞路」

如果兩個模型得到相同答案：

$$
Q_A=Q_B,
$$

但：

$$
N_{\mu,A}^{gross}
\gg
N_{\mu,B}^{gross},
$$

而 effective work 接近，

則 A 的 semantic path 更浪費。

---

# 76. 但這不等於物理浪費

因為不同 $\mu_I$ 的物理實現成本可能不同。

所以：

$$
\boxed{
SemanticEfficiency
\neq
EnergyEfficiency.
}
$$

---

# 77. 需要跨層對映

本文建立：

$$
\boxed{
\mu_I
\rightarrow
\rho_C(\mu_I)
}
$$

---

# 78. $\rho_C$

Algorithmic / Computational Realization。

可能包含：

- attention operations；
- retrieval；
- routing；
- symbolic rewrite；
- recurrent state update。

---

# 79. 再往下：

$$
\boxed{
\rho_C(\mu_I)
\rightarrow
\rho_P(\mu_I)
}
$$

---

# 80. $\rho_P$

Physical Execution Trace。

例如：

$$
\rho_P=
(
Ops,
Bytes,
Interconnect,
DeviceTime
).
$$

---

# 81. 再往下：

$$
\boxed{
\rho_P(\mu_I)
\rightarrow
\rho_T(\mu_I).
}
$$

---

# 82. $\rho_T$

Thermodynamic Realization：

$$
\boxed{
\rho_T=
(
Energy,
Heat,
EntropyProduction
).
}
$$

---

# 83. 因此完整鏈條

$$
\boxed{
\mu_I
\rightarrow
\rho_C
\rightarrow
\rho_P
\rightarrow
\rho_T.
}
$$

---

# 84. 這不是一對一映射

同樣 $\mu_I$ 在不同架構上：

$$
\rho_P^A(\mu_I)
\neq
\rho_P^B(\mu_I).
$$

---

# 85. 這恰恰是我們要比較的

因為它讓我們問：

> 相同語意工作，哪個模型／硬體需要更少物理世界？

---

# 86. Semantic Equivalence Class

如果兩個不同物理過程都完成相同 task-relative semantic transition：

$$
\mu_I^A\sim\mu_I^B,
$$

則它們屬於同一語意等價類。

---

# 87. 定義：

$$
\boxed{
[\mu_I]
=
\{
\rho
\mid
\rho\text{ realizes the same semantic transition}
\}.
}
$$

---

# 88. 這是跨模型計量的核心

否則我們永遠只能比較：

> GPU A 比 GPU B 快多少。

而不能比較：

> 智能工作本身的物理效率。

---

# 89. 如何判斷同一語意轉換？

需要至少三種一致性：

$$
\boxed{
\mathcal E_{\mu}
=
(
E_{pre},
E_{post},
E_{function}
).
}
$$

---

# 90. $E_{pre}$

前置求解狀態語意等價。

---

# 91. $E_{post}$

後置求解狀態語意等價。

---

# 92. $E_{function}$

對後續任務行為的功能效用等價。

---

# 93. 只看輸出字面相同不夠

兩個模型可能都說：

> B。

但一個是推理得到，

一個是猜中。

---

# 94. 所以：

$$
\boxed{
SameAnswer
\neq
SameSemanticExecution.
}
$$

---

# 95. 需要 counterfactual contribution test

移除該中間狀態後：

$$
Q\downarrow?
$$

---

# 96. 若沒有任何影響

那它更可能是 epiphenomenal trace。

---

# 97. 這裡遇到可觀測性難題

黑箱模型內部的 $z_t$ 不一定可直接讀取。

---

# 98. 因此 $\mu_I$ 需要兩種版本

$$
\boxed{
\mu_I^{obs}
}
$$

Observer-Reconstructed Semantic Unit。

---

# 99. 以及：

$$
\boxed{
\mu_I^{int}
}
$$

True Internal Semantic Unit。

---

# 100. 現階段我們通常只能近似前者

所以：

$$
\boxed{
\mu_I^{obs}
\approx
\mu_I^{int}
}
$$

不是已證明等號。

---

# 101. 這必須寫在理論裡

否則會犯認識論錯誤：

> 我們可以描述一個語意步驟，所以模型內部一定就是這樣運算。

不成立。

---

# 102. Semantic Instrumentation

未來如果模型提供：

- latent probes；
- causal interventions；
- activation patching；
- mechanistic traces；

則可以逐步提高：

$$
Confidence(
\mu_I^{obs}
\approx
\mu_I^{int}
).
$$

---

# 103. 但 IPM 不依賴完全可解釋性才開始

因為即使無法看透所有 latent computation，

仍可以先做：

- black-box intervention；
- task decomposition；
- ablation；
- paired behavior test。

---

# 104. Measurement Ladder

本文提出 $\mu_I$ 的四級量測：

### Level 0 — Behavioral Proxy

只從輸入／輸出推斷 semantic steps。

---

# 105. Level 1 — Structured Trace

使用可見 reasoning trace、tool trace、symbolic proof steps。

---

# 106. Level 2 — Causal Internal Probe

透過 internal intervention 驗證某 latent transition 是否有因果作用。

---

# 107. Level 3 — Physical-Semantic Alignment

直接把 semantic event 與 physical trace 對齊。

---

# 108. Level 3 才接近完整 IPM

但不應假裝現在所有模型都能做到。

---

# 109. $\mu_I$ 與 information bit 的關係

一個 $\mu_I$ 可能帶來：

$$
IG(\mu_I)
$$

資訊增益。

---

# 110. 但：

$$
\boxed{
\mu_I
\neq
1\ bit.
}
$$

---

# 111. 一次語意轉換可能產生多 bits 的 uncertainty reduction

也可能暫時增加 entropy。

---

# 112. 所以 bit 是量測某個屬性

不是 $\mu_I$ 本身。

---

# 113. $\mu_I$ 與 cognitive operation

認知科學常用 elementary mental operation。

我們可以借其：

- operation；
- cost；
- utility；

三元結構。

---

# 114. 但 IPM 多加一層

$$
\boxed{
\text{operation}
\rightarrow
\text{physical trace}
\rightarrow
\text{energy}.
}
$$

---

# 115. 最小性問題的正式處理

令解析度：

$$
\delta.
$$

---

# 116. 在 $\delta$ 下，

如果任何拆分：

$$
\mu_I\rightarrow
(\mu_a,\mu_b)
$$

都使至少一個子單位失去獨立 task-semantic function，

則：

$$
\mu_I
$$

在 $\delta$ 下是最小。

---

# 117. 表示：

$$
\boxed{
Minimal_{\delta}(\mu_I)=1.
}
$$

---

# 118. 更細解析度：

$$
\delta'<\delta
$$

可能重新拆開。

---

# 119. 所以：

$$
\boxed{
AbsoluteSemanticAtom
}
$$

不是本文主張。

---

# 120. 本文主張的是

$$
\boxed{
\text{operationally minimal semantic unit}.
}
$$

---

# 121. 語意單位也可能有粒度層級

$$
\mu^{(0)}
\rightarrow
\mu^{(1)}
\rightarrow
\mu^{(2)}.
$$

---

# 122. 例如數學：

Level 0：

$$
x=2.
$$

---

# 123. Level 1：

從：

$$
x+1=3
$$

推出：

$$
x=2.
$$

---

# 124. Level 2：

完成一個 lemma。

---

# 125. Level 3：

完成整個 theorem strategy。

---

# 126. 只有最低仍保有 task-semantic function 的層才適合作為當前 $\mu_I$。

---

# 127. Semantic Work Vector

不是所有 $\mu_I$ 功能都一樣。

可以建立：

$$
\boxed{
\mathbf N_{\mu}
=
(
N_B,
N_R,
N_C,
N_I,
N_G
)
}
$$

其中：

- $N_B$：belief update；
- $N_R$：relation construction；
- $N_C$：constraint resolution；
- $N_I$：information restructuring；
- $N_G$：goal/strategy transformation。

---

# 128. 這比只報總數更好

因為兩個系統可能：

$$
N_{\mu,A}=N_{\mu,B}
$$

但工作結構完全不同。

---

# 129. 某些模型可能是「關係型」

$$
N_R\uparrow.
$$

---

# 130. 某些是「搜尋型」

$$
N_C\uparrow.
$$

---

# 131. 某些是「策略重構型」

$$
N_G\uparrow.
$$

---

# 132. 這可能形成 Intelligence Work Profile

$$
\boxed{
\mathcal W_I=
\mathbf N_{\mu}.
}
$$

---

# 133. 這讓智能不再只有「多少」

還有：

$$
\boxed{
\text{what kind of semantic work}.
}
$$

---

# 134. 與 Paper 01 的連接

Paper 01 定義：

$$
\mathfrak E=
(
Q,U,G,I,L,R,S,T,E,V_{CST}
).
$$

---

# 135. 現在插入新的中間層：

$$
\boxed{
\mathfrak E'=
(
Q,
\mathbf N_{\mu},
U,G,I,L,R,S,T,E,V_{CST}
).
}
$$

---

# 136. 這第一次把「做了多少語意工作」放進事件向量。

---

# 137. 但仍不能直接拿 $N_\mu$ 當智能

因為：

$$
Q
$$

才是最終成果。

---

# 138. 如果做了很多 $\mu_I$ 但答案很差

那只是：

$$
\boxed{
\text{large semantic work with low yield}.
}
$$

---

# 139. 所以需要 Semantic Yield

$$
\boxed{
Y_{\mu}
=
\frac{
Q
}{
N_{\mu}^{eff}
}.
}
$$

---

# 140. 這表示

每一單位有效語意工作產生多少成果品質。

---

# 141. 再往物理接

Paper 04–05 之後可定義：

$$
\boxed{
Y_{\mu/J}
=
\frac{
N_{\mu}^{eff}
}{
E_{\mathrm{marginal}}
}.
}
$$

---

# 142. 以及：

$$
\boxed{
Y_{Q/J}
=
\frac{
Q
}{
E_{\mathrm{marginal}}
}.
}
$$

---

# 143. 完整鏈條

$$
\boxed{
E_{\mathrm{physical}}
\rightarrow
N_{\mu}^{eff}
\rightarrow
Q.
}
$$

---

# 144. 兩個效率可以分開

$$
\boxed{
\eta_{P\rightarrow \mu}
=
\frac{
N_{\mu}^{eff}
}{
C_{\mathrm{phys}}
}
}
$$

---

# 145. 以及：

$$
\boxed{
\eta_{\mu\rightarrow Q}
=
\frac{
Q
}{
N_{\mu}^{eff}
}.
}
$$

---

# 146. 概念上：

$$
\boxed{
Q
=
C_{\mathrm{phys}}
\cdot
\eta_{P\rightarrow \mu}
\cdot
\eta_{\mu\rightarrow Q}.
}
$$

---

# 147. 這很重要

因為一個系統可以：

- 物理→語意 很高效；
- 語意→成果 很低效。

---

# 148. 另一個可能相反

所以總能效相同，不代表智能機制相同。

---

# 149. $\mu_I$ 與創造力

創造力常不是只減少 search space。

---

# 150. 一次創造性 $\mu_I$ 可能：

$$
\boxed{
\text{introduce a new relation / variable / representation}.
}
$$

---

# 151. 因此：

$$
|\Omega_{t+1}|>|\Omega_t|
$$

不代表退步。

---

# 152. 真正判準是

新增空間是否提高後續：

$$
ExpectedQ.
$$

---

# 153. 所以 creative semantic execution 也能納入 $\mu_I$。

---

# 154. $\mu_I$ 與錯誤

錯誤推理是否算一個 $\mu_I$？

---

# 155. 如果它改變了語意狀態：

$$
\Delta z\neq0,
$$

它可以算：

$$
\mu_I^{gross}.
$$

---

# 156. 但若最終被證明無助甚至有害：

$$
\boxed{
\mu_I^{eff}=0
}
$$

或負貢獻。

---

# 157. 因此可以再定義 signed contribution

$$
\boxed{
w_i^{Q}
=
\Delta Q_i.
}
$$

---

# 158. $w_i^Q>0$

有效正向智能工作。

---

# 159. $w_i^Q=0$

語意活動但無結果貢獻。

---

# 160. $w_i^Q<0$

誤導性智能工作。

---

# 161. 所以總有效語意功

可以概念性寫：

$$
\boxed{
W_{\mu}
=
\sum_i w_i^Q.
}
$$

---

# 162. 但本文暫不把 $W_\mu$ 當物理 work

避免和 Joule 混淆。

---

# 163. Semantic Work 只是功能性計量

Physical Work 才是物理量。

---

# 164. 二者必須保持型別分離

$$
\boxed{
W_{\mu}^{semantic}
\neq
W^{physical}.
}
$$

---

# 165. 這是一條核心 type safety rule

不允許把「語意功」直接當焦耳。

---

# 166. 十四個 Canonical Invariants

**Invariant 1**

$$
\boxed{
Token\neq \mu_I.
}
$$

**Invariant 2**

$$
\boxed{
FLOP\neq \mu_I.
}
$$

**Invariant 3**

$$
\boxed{
NeuronActivation\neq \mu_I.
}
$$

**Invariant 4**

$$
\boxed{
Layer\neq \mu_I.
}
$$

**Invariant 5**

$$
\boxed{
Thought\neq \mu_I.
}
$$

**Invariant 6**

$$
\boxed{
Minimality
=
Minimality(\delta,Task,Observer).
}
$$

**Invariant 7**

$$
\boxed{
SemanticUnit
\neq
SpecificPhysicalImplementation.
}
$$

**Invariant 8**

$$
\boxed{
SemanticEvent
\Rightarrow
PhysicalRealization.
}
$$

**Invariant 9**

$$
\boxed{
SemanticActivity
\neq
EffectiveIntelligentWork.
}
$$

**Invariant 10**

$$
\boxed{
SameAnswer
\neq
SameSemanticExecution.
}
$$

**Invariant 11**

$$
\boxed{
InformationGain
\neq
IntelligenceItself.
}
$$

**Invariant 12**

$$
\boxed{
SemanticEfficiency
\neq
EnergyEfficiency.
}
$$

**Invariant 13**

$$
\boxed{
\mu_I^{obs}
\neq
\mu_I^{int}
}
$$

除非有額外證據支持近似。

**Invariant 14**

$$
\boxed{
SemanticWork
\neq
PhysicalWork.
}
$$

---

# 167. 結論：智能的最小單位應由「有效語意改變」決定

如果我們用 token 當智能單位，

會把語言表示誤認成認知工作。

如果用 FLOP，

會把算術原語誤認成語意工作。

如果用 neuron activation，

又會把特定實現方式誤認成跨架構智能本體。

所以：

$$
\boxed{
\textbf{
智能的最小計量單位必須位於語意與物理之間。
}
}
$$

它需要足夠抽象，才能跨：

- Transformer；
- RNN；
- symbolic system；
- neuromorphic hardware；
- biological brain。

但又不能抽象到失去物理落點。

因此本文提出：

$$
\boxed{
\mu_I:
z_t\rightarrow z_{t+1}
}
$$

其中這個狀態轉換必須：

- 對任務有關；
- 真正改變求解狀態；
- 對最終成果有因果效用；
- 在指定語意解析度下不可再有意義地拆分；
- 能與其他單位組合；
- 不綁死單一硬體；
- 但可以向下追到真實物理 trace。

所以 $\mu_I$ 不是：

> 一個字。

不是：

> 一次乘法。

不是：

> 一個 neuron。

也不是：

> 一個完整想法。

它更接近：

$$
\boxed{
\textbf{
一次最小、有效、可利用的求解語意狀態改變。
}
}
$$

而這使 IPM 第一次具有完整中間橋：

$$
\boxed{
\text{Physical Computation}
\rightarrow
\mu_I
\rightarrow
\text{Task Quality}.
}
$$

但現在還有一個極大的空白。

我們提出了語意中間層，

卻仍然不知道生物智能世界過去是怎麼處理這個問題的。

人腦研究已經使用：

- cognitive operation；
- spike；
- synaptic event；
- bits/spike；
- ATP；
- behavioral throughput；

建立跨尺度 proxy。

所以下一篇不再繼續抽象發明。

而要回頭看：

$$
\boxed{
\textbf{
人類到底是怎麼把「認知」一路量到「神經事件」的？
}
}
$$

這就是 Paper 03。

---

## 系列路徑

1. **Paper 01｜一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義**  
2. **Paper 02｜智能到底算了一次什麼？：最小智能語意執行單位的候選理論**  
3. **Paper 03｜從認知到神經元：人腦如何跨層測量智能計算**  
4. **Paper 04｜從神經元到焦耳：智能計算的能量、熱力學與物理下界**  
5. **Paper 05｜計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積**  
6. **Paper 06｜成果品質到底怎麼量？：從形式化正確性到結構化智能品質**  
7. **Paper 07｜不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估**  
8. **Paper 08｜自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間**  
9. **Paper 09｜拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本**  
10. **Paper 10｜一個答案值多少物理世界？：智能產率的統一計量框架**
