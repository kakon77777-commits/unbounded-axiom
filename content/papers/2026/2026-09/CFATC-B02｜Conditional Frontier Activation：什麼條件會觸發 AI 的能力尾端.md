# CFATC-B02｜Conditional Frontier Activation：什麼條件會觸發 AI 的能力尾端
## Conditional Frontier Activation: Under What Conditions Do AI Systems Enter Their Capability Tail?

**系列：** Conditional Frontier Activation and Human–AI Tail Coupling（CFATC）  
**系列中文名：** 條件式前沿觸發與人機尾端耦合系列  
**篇次：** Paper 02 / 08  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Frontier Capability／人機耦合／AI 能力觸發／能力歸因與評測

---

## 摘要

CFATC-B01 已提出：

$$
\boxed{
C_{\mathrm{latent}}(AI)
\neq
C_{\mathrm{realized}}(AI\mid H,T,M,E)
}
$$

並將 AI 能力區分為 latent、coupled 與 self-activated 三層。本文進一步研究其中最重要、也最容易被誤判的一個現象：

> **某些 AI 能力是否只有在特定人類、任務、方法、表示、工具、驗證與修復條件共同成立時，才會穩定進入平常互動看不到的高能力區域？**

本文將此稱為：

$$
\boxed{
\text{Conditional Frontier Activation}
}
$$

簡寫：

$$
\boxed{
\mathrm{CFA}.
}
$$

CFA 不等於「多提示幾次後模型終於答對」，也不等於「人類把答案告訴 AI」。本文要求至少同時區分：

1. AI 原本已能獨立完成；
2. 人類直接提供缺失事實或答案；
3. 人類提供問題結構、表示或方法；
4. 人類提供 verifier 與修復方向；
5. 人機互動使 AI 生成新的中間結構；
6. 人機整體產生單獨任一方都未穩定具有的有效能力。

因此，本文提出 **Activation Attribution Ladder（能力觸發歸因階梯）**：

$$
\boxed{
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow
A_4
\rightarrow
A_5.
}
$$

其中：

- $A_0$：Baseline Capability，模型在標準條件下已能完成；
- $A_1$：Information Injection，人類提供關鍵答案材料；
- $A_2$：Search-Space Reduction，人類縮小問題空間或補齊約束；
- $A_3$：Method / Representation Activation，人類提供新的方法、座標或表示；
- $A_4$：Verification / Repair Activation，人類主要提供錯誤定位、驗證與遞迴修復；
- $A_5$：Joint Frontier Emergence，人機閉環產生單方都未能穩定實現的新有效策略或結果。

本文主張，只有 $A_2$ 至 $A_5$ 的一部分情形具有「能力觸發」研究價值；真正強版本 CFA 應主要關注 $A_3$ 至 $A_5$，尤其是：

$$
\boxed{
\Delta_{\mathrm{coupling}}
=
C(H\oplus AI)
-
\max(
C(H),
C(AI)
)
>
0.
}
$$

但 CFA 還需要另一道防偽條件：任務本身必須是有效認知挑戰，而不是因為語義混亂、錯誤前提、欠定義、資料缺失或 moving goalpost 使 AI 失敗。本文因此承接 LHCF 的 Cognitive Challenge Admissibility Gate（CCAG），將有效 frontier activation 寫為：

$$
\boxed{
\mathrm{CFA}^{\mathrm{valid}}
=
G_{\mathrm{CCAG}}
\cdot
\mathrm{CFA}^{\mathrm{observed}}.
}
$$

若：

$$
G_{\mathrm{CCAG}}\approx0,
$$

則模型「很難回答」不能被視為 frontier evidence。

本文進一步定義 **Frontier Activation State**：

$$
\boxed{
\Theta_F
=
(
H,
Q,
R,
M,
T,
V,
B,
E,
L
)
}
$$

其中：

- $H$：Human Coupler State；
- $Q$：Problem / Question Construction；
- $R$：Representation；
- $M$：Method / Methodology；
- $T$：Tools and Runtime；
- $V$：Verification；
- $B$：Resource Budget；
- $E$：Epistemic / Environment Conditions；
- $L$：Learning / Recursive Repair Loop。

對 AI 系統 $A$，定義 frontier activation probability：

$$
\boxed{
p_F(A\mid\Theta_F)
=
P(
C_{\mathrm{realized}}
\in
\mathcal C_{\mathrm{tail}}
\mid
A,\Theta_F
).
}
$$

其中 $\mathcal C_{\mathrm{tail}}$ 不是固定的「前 1%」，而是相對於指定任務族、模型世代、資源預算與 baseline interaction regime 定義的高能力區域。

為避免把一般 assistance 誤認為 frontier activation，本文提出四個必要檢查：

$$
\boxed{
\text{Difficulty Validity}
+
\text{Baseline Contrast}
+
\text{Attribution}
+
\text{Verification}.
}
$$

更強版本再加入：

$$
\boxed{
\text{Repeatability}
+
\text{Counterfactual Ablation}.
}
$$

只有當移除關鍵耦合條件後能力顯著下降，而保留條件時可反覆重現，才有較強證據支持「這個條件真的在觸發能力」，而不是一次運氣。

本文也將 2026 年的外部研究放入此框架。Anthropic 對約 40 萬次 Claude Code sessions 的分析顯示，較高 domain expertise 的使用者能讓 Claude 每次 instruction 完成更多工作，且 session success 與 expertise 呈正相關；ExPerT 則顯示 AI 可以推斷 query-specific expertise 並調整回答深度。Idan 與 Anand 的隨機實驗進一步提出 AI Interaction Competence：能否誘導、篩選與驗證模型輸出，是 GenAI 收益異質性的強預測變量。另一方面，Dell’Acqua 等人的 Jagged Technological Frontier 顯示，即使看似難度相近的任務，也可能分別位於 AI 能力邊界內外，且使用者若無法辨識這條 jagged frontier，AI 反而可能降低正確率。

這些工作尚未證明本文完整 CFA 理論，但共同支持一個核心前提：

$$
\boxed{
\text{AI capability realization is interaction-, task-, and regime-dependent}.
}
$$

本文最後提出 **Frontier Activation Experiment（FAE）**：對同一 AI、同一有效任務，系統性 ablate problem framing、representation、method、verification、repair、tools 與 expert coupling，建立：

$$
\boxed{
\mathcal A_F
=
\{
p_F(\Theta_F^{(0)}),
p_F(\Theta_F^{(1)}),
\ldots
\}
}
$$

的 activation profile。若某些條件使 verified success 從低概率區跨入穩定高概率區，便可將其視為候選 activation mechanism。

因此本文的核心命題不是：

> 「高手可以讓 AI 變聰明。」

而是：

> **在某些歷史階段，AI 已具有超出日常互動可見範圍的潛在能力，而是否進入該能力尾端，可能取決於特定人機—方法—驗證耦合條件。**

**關鍵詞：** Conditional Frontier Activation、CFA、Human–AI Coupling、Capability Tail、Frontier Capability、Activation Attribution、CCAG、Recursive Repair、Verification、Expertise、Jagged Technological Frontier

---

# 1. 問題：什麼叫「把 AI 推入能力尾端」？

如果 AI 第一次答錯，第二次答對：

$$
0
\rightarrow
1,
$$

不能直接說：

> 我觸發了 AI 的 frontier capability。

可能只是：

- sampling variance；
- 更多 token；
- 剛好猜對；
- 使用者提供答案；
- tool 回傳正解。

因此 CFA 必須比「最後做對」更嚴格。

---

# 2. B01 的起點

B01 已建立：

$$
\boxed{
\text{Latent Capability}
\rightarrow
\text{Coupling Conditions}
\rightarrow
\text{Activated Capability}
\rightarrow
\text{Observed Capability}
\rightarrow
\text{Recognized Capability}.
}
$$

B02 專門處理第二個箭頭：

$$
\boxed{
\text{Coupling Conditions}
\rightarrow
\text{Activated Capability}.
}
$$

---

# 3. Capability Tail

本文定義：

$$
\boxed{
\mathcal C_{\mathrm{tail}}
(
A,
\mathcal T,
B,
\mathcal R_0
)
}
$$

為 AI $A$ 在任務族 $\mathcal T$ 、資源預算 $B$ 與 baseline interaction regime $\mathcal R_0$ 下，低頻但高能力的可實現區域。

---

# 4. Tail 不是固定百分位

本文不要求：

$$
\mathcal C_{\mathrm{tail}}
=
\text{top }1\%.
$$

它可以由：

- benchmark frontier；
- expert-rated novelty；
- long-horizon verified success；
- out-of-distribution difficulty；
- previously unsolved subproblem；

等方式 operationalize。

---

# 5. Frontier 也不是單純「很難」

一個問題可以極難，但根本無解或欠定義。

所以：

$$
\boxed{
\text{Difficulty}
\neq
\text{Valid Frontier Challenge}.
}
$$

---

# 6. CCAG：第一道防偽門

承接 LHCF：

$$
\mathbf G(X)
=
(
G_S,
G_D,
G_A,
G_R,
G_B,
G_I,
G_N,
G_U
).
$$

只有通過有效性閘門的 challenge 才能進 frontier activation 分析。

---

# 7. Valid Activation

因此：

$$
\boxed{
\mathrm{CFA}^{\mathrm{valid}}
=
G_{\mathrm{CCAG}}
\cdot
\mathrm{CFA}^{\mathrm{obs}}.
}
$$

---

# 8. 如果題目本身壞掉

若：

$$
G_{\mathrm{CCAG}}\rightarrow0,
$$

AI 失敗率：

$$
P(\mathrm{fail})\rightarrow1
$$

也不能證明能力前沿。

---

# 9. 第二道門：Baseline Contrast

必須先知道：

$$
C_{\mathrm{baseline}}.
$$

沒有 baseline，就不知道 improvement 是不是 activation。

---

# 10. Baseline Interaction Regime

定義：

$$
\boxed{
\mathcal R_0
=
(
H_0,
Q_0,
R_0,
M_0,
T_0,
V_0,
B_0
).
}
$$

例如：

- non-expert user；
- standard prompt；
- no special verifier；
- standard toolset；
- fixed budget。

---

# 11. Activated Regime

定義：

$$
\boxed{
\mathcal R_1
=
\mathcal R_0
+
\Delta\Theta.
}
$$

其中 $\Delta\Theta$ 是新增耦合條件。

---

# 12. Activation Gain

定義：

$$
\boxed{
\Delta_F
=
C_{\mathrm{realized}}(\mathcal R_1)
-
C_{\mathrm{realized}}(\mathcal R_0).
}
$$

---

# 13. 但 Gain 不等於 Frontier

如果任務很簡單：

$$
C_{\mathrm{task}}
\ll
C_{\mathrm{latent}},
$$

即使：

$$
\Delta_F>0,
$$

也只是 ordinary improvement。

---

# 14. Frontier Condition

至少要求：

$$
\boxed{
D(T)
\geq
\tau_{\mathrm{frontier}}.
}
$$

其中 $D(T)$ 應由外部或 task-family 對照定義。

---

# 15. Frontier 不一定等於人類世界紀錄

它可以是：

- frontier for model generation；
- frontier for agent reliability；
- frontier for formal proof；
- frontier for human–AI joint work。

因此需聲明：

$$
\boxed{
\text{Frontier Reference Frame}.
}
$$

---

# 16. 第三道門：Attribution

如果人類直接提供：

> 正確答案是 42。

AI 回覆：

> 42。

這不是 AI frontier activation。

---

# 17. Activation Attribution Ladder

本文正式提出：

$$
\boxed{
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow
A_4
\rightarrow
A_5.
}
$$

---

# 18. $A_0$：Baseline Capability

AI 在標準條件下已能穩定完成。

這不是 conditional activation。

---

# 19. $A_1$：Information Injection

人類提供：

- missing fact；
- theorem；
- solution step；
- correct output。

若移除資訊，AI 無法完成。

---

# 20. $A_1$ 的解釋

此時人類主要是：

$$
\boxed{
\text{information source}.
}
$$

不能把結果全歸因於 AI latent capability。

---

# 21. $A_2$：Search-Space Reduction

人類不提供答案，但提供：

- constraints；
- decomposition；
- relevant domain；
- branch elimination。

---

# 22. Search-Space Reduction 的價值

如果原問題空間：

$$
|\Omega|\gg1,
$$

人類縮減：

$$
\Omega
\rightarrow
\Omega',
\quad
|\Omega'|\ll|\Omega|.
$$

AI 可能因此進入可計算區。

---

# 23. $A_2$ 是 activation 還是 assistance？

本文把它視為弱 activation 候選。

因為 AI 的 solver 能力可能本來存在，只是搜索成本過大。

---

# 24. $A_3$：Method / Representation Activation

人類提供：

- new representation；
- theorem family；
- graph transform；
- state machine；
- proof strategy；
- architecture pattern。

---

# 25. 為什麼 $A_3$ 更強？

因為：

$$
\boxed{
\text{Representation Change}
\rightarrow
\text{New Reachable Reasoning Region}.
}
$$

不是單純增加資訊量。

---

# 26. $A_4$：Verification / Repair Activation

人類主要不提供解法。

而是提供：

- counterexample；
- failing test；
- missing proof obligation；
- exact error localization；
- definition mismatch。

---

# 27. Repair Activation

若：

$$
E_0
\rightarrow
E_1
\rightarrow
\cdots
\rightarrow
E_n
$$

且：

$$
\|E_{k+1}\|<\|E_k\|,
$$

人類可能充當：

$$
\boxed{
\text{repair direction oracle}.
}
$$

---

# 28. $A_5$：Joint Frontier Emergence

最強情況：

$$
\boxed{
C(H\oplus A)
>
\max(
C(H),
C(A)
).
}
$$

---

# 29. $A_5$ 不要求 AI 單獨原創全部內容

它要求：

> joint system 產生單方都未穩定具有的有效能力。

---

# 30. Strong Coupling Delta

定義：

$$
\boxed{
\Delta_{\mathrm{coupling}}
=
C(H\oplus A)
-
\max(
C(H),
C(A)
).
}
$$

---

# 31. 何時才算 strong CFA？

本文暫定至少要求：

$$
\boxed{
A_k,
\quad
k\geq3,
}
$$

再加 verified frontier result。

---

# 32. CFA State Vector

本文定義：

$$
\boxed{
\Theta_F
=
(
H,
Q,
R,
M,
T,
V,
B,
E,
L
).
}
$$

---

# 33. $H$：Human Coupler State

包含：

- domain expertise；
- problem taste；
- error recognition；
- meta-level reasoning；
- task familiarity。

---

# 34. $Q$：Problem Construction

包括：

- target；
- scope；
- assumptions；
- constraints；
- success condition。

---

# 35. $R$：Representation

問題在哪個 cognitive chart 中表示。

---

# 36. $M$：Method

包括 proof、simulation、search、optimization、graph、causal reasoning 等。

---

# 37. $T$：Tool / Runtime

包括：

- web；
- code；
- CAS；
- prover；
- persistent memory；
- multi-agent runtime。

---

# 38. $V$：Verification

包括：

- unit tests；
- formal proof；
- external source；
- independent review；
- experiment。

---

# 39. $B$：Budget

包括：

$$
\mathbf B
=
(
B_{\mathrm{time}},
B_{\mathrm{compute}},
B_{\mathrm{search}},
B_{\mathrm{tool}},
B_{\mathrm{human}}
).
$$

---

# 40. $E$：Epistemic / Environment Conditions

例如：

- data quality；
- noise；
- task version；
- permission；
- availability。

---

# 41. $L$：Learning / Repair Loop

描述：

- whether failures persist；
- whether memory updates；
- whether repair direction is reused。

---

# 42. Frontier Activation Probability

對 AI $A$：

$$
\boxed{
p_F(A\mid\Theta_F)
=
P(
C_{\mathrm{realized}}
\in
\mathcal C_{\mathrm{tail}}
\mid
A,\Theta_F
).
}
$$

---

# 43. Activation 不是 deterministic magic switch

同一 $\Theta_F$：

$$
p_F<1
$$

完全可能。

因為模型仍具有 stochasticity 與 trajectory variance。

---

# 44. Activation Threshold

可以定義：

$$
p_F
\geq
\tau_F
$$

為穩定 activated regime。

---

# 45. Ordinary Regime

若：

$$
p_F\ll\tau_F,
$$

則 tail capability 只是偶發事件。

---

# 46. Repeatable Activation

若：

$$
p_F\geq\tau_F
$$

跨多次重跑、seed、task variant 仍成立，證據更強。

---

# 47. 第四道門：Verification

沒有 verifier：

$$
\boxed{
\text{Apparent Frontier Success}
\neq
\text{Frontier Success}.
}
$$

---

# 48. 為什麼 frontier 更需要驗證？

因為當人類自己也接近認知邊界時：

$$
\boxed{
\text{plausibility}
\approx
\text{dangerous proxy for correctness}.
}
$$

---

# 49. Verified Frontier Event

定義：

$$
\boxed{
FVE
=
(
T,
\Theta_F,
A_k,
\text{Result},
\text{Verifier},
\text{Receipt}
).
}
$$

---

# 50. Receipt 至少要保存

- task version；
- model / runtime；
- human contribution；
- tools；
- intermediate states；
- verification；
- ablation。

---

# 51. 第五道門：Repeatability

一次成功：

$$
n=1
$$

只能是 anecdote。

---

# 52. Repeated Frontier Activation

若：

$$
P(FVE\mid\Theta_F)
$$

在 task family 中持續高，

才形成 stronger evidence。

---

# 53. 第六道門：Counterfactual Ablation

最重要的問題之一：

> 如果移除人類提供的某個 coupling component，結果還會成功嗎？

---

# 54. Ablation Set

對：

$$
\Theta_F
$$

依序移除：

- $Q$ ；
- $R$ ；
- $M$ ；
- $V$ ；
- $L$。

---

# 55. Causal Activation Contribution

定義：

$$
\boxed{
\Delta_i^{\mathrm{act}}
=
p_F(\Theta_F)
-
p_F(\Theta_F\setminus i).
}
$$

---

# 56. 若 $\Delta_i^{\mathrm{act}}\approx0$

表示該條件可能不是關鍵 activation factor。

---

# 57. 若 $\Delta_i^{\mathrm{act}}\gg0$

表示它是候選 causal activator。

---

# 58. Interaction Effects

兩個條件可能單獨都弱：

$$
\Delta_i\approx0,
\quad
\Delta_j\approx0,
$$

但一起：

$$
\Delta_{ij}\gg0.
$$

---

# 59. 因此 activation 可能是高階交互作用

更完整：

$$
p_F
=
\Phi(
H,Q,R,M,T,V,B,E,L
).
$$

不能假設線性加法。

---

# 60. Activation Bottleneck

如果：

$$
V\approx0,
$$

即使：

$$
H,Q,R,M,T
$$

都很好，

frontier result 仍可能不可證成。

---

# 61. Multiplicative Intuition

概念上：

$$
\boxed{
p_F
\propto
H
\cdot
Q
\cdot
R
\cdot
M
\cdot
V
\cdot
L
}
$$

只表達 bottleneck intuition，不主張真實世界必為純乘法。

---

# 62. Cognitive Resistance 與 CFA

LHCF 已把 AI 對理論的阻抗寫成：

$$
R_i(T,\mathbb A,\mathbf b).
$$

B02 的另一種表述是：

$$
\boxed{
\text{Activation}
=
\text{conditions that reduce effective cognitive resistance}.
}
$$

---

# 63. Resource-Dependent Resistance

某任務在低預算：

$$
R\approx1,
$$

高預算：

$$
R\approx0.
$$

此時 activation 可能只是 compute scaling。

---

# 64. Method-Dependent Resistance

若加入新方法後：

$$
R_M\downarrow,
$$

則屬方法 activation。

---

# 65. Verification-Dependent Resistance

若 verifier 使：

$$
R_V\downarrow,
$$

則 frontier capability 可能從「能生成候選」提升為「能證成」。

---

# 66. Representation-Invariant Activation

強理解應該對等價表示具有一定穩定性。

若只在一個特定 wording 成功：

$$
\boxed{
\text{Prompt Fragility}
}
$$

很高。

---

# 67. Robust Activation

應測：

$$
T'
=
\phi(T),
\quad
T'\equiv T.
$$

如果仍成功，activation 更可信。

---

# 68. Jagged Technological Frontier 的支點

Dell’Acqua 等人的研究指出，外觀看似相近的知識工作任務可以分別落在 AI 能力邊界內外。

因此：

$$
\boxed{
\text{Human-Perceived Difficulty}
\neq
\text{AI Capability Position}.
}
$$

---

# 69. 這對 CFA 很重要

人類不能只用：

> 這題看起來很難。

判斷 frontier。

需要 empirical baseline。

---

# 70. Frontier Navigation Skill

Jagged frontier 研究也顯示：

> 能辨識 AI 何時可靠、何時不可靠，本身會影響人機績效。

這與：

$$
E,
V
$$

高度相關。

---

# 71. Anthropic Expertise Result

Anthropic 2026 對約 40 萬次 Claude Code sessions 的分析指出：

- 人類多做 what-to-do planning；
- Claude 多做 how-to-do execution；
- domain expertise 越高，Claude 每次 instruction 做的工作越多；
- expertise 與 session success 正相關。

---

# 72. CFA 的解讀

這不證明 expert users 一定觸發 frontier tail。

但支持：

$$
\boxed{
H
\text{ changes the realized agent regime}.
}
$$

---

# 73. ExPerT 的支點

ExPerT 發現 user expertise 是 query-specific。

所以：

$$
\boxed{
H=H(q),
}
$$

而不是固定 personality score。

---

# 74. Human Coupler 因而是 task-relative

同一人：

$$
H(q_1)\gg H(q_2)
$$

完全可能。

---

# 75. AI Interaction Competence

Idan 與 Anand 2026 的隨機實驗指出，GenAI 收益高度異質，而 AI Interaction Competence 對增益具有強預測力。

---

# 76. AIC 的核心

其概念包括：

- elicit；
- filter；
- verify。

這與 B02 的：

$$
Q,V,L
$$

部分重疊。

---

# 77. Scaffolding 會降低 variance

該研究中的 conceptual-map scaffolding 降低結果差異。

這表示：

$$
\boxed{
\text{some coupling advantage can be infrastructuralized}.
}
$$

---

# 78. 這對未來很重要

如果高手 coupling procedure 可以被系統自己提供：

$$
C_{\mathrm{self}}
\uparrow.
$$

---

# 79. CFA 不應被理解成「永遠需要高手」

相反：

$$
\boxed{
\text{human activation procedures may migrate into AI runtime}.
}
$$

---

# 80. Historical Coupling Window

因此本系列研究的可能歷史窗口是：

$$
\boxed{
C_{\mathrm{latent}}
>
C_{\mathrm{self}}
}
$$

而：

$$
C_{\mathrm{coupled}}
\approx
C_{\mathrm{latent}}
$$

對少數高耦合配置成立。

---

# 81. 這是一個可消失的現象

若未來：

$$
C_{\mathrm{self}}
\rightarrow
C_{\mathrm{latent}},
$$

則強人類 activation 的邊際價值下降。

---

# 82. Activation Surface

對固定 AI，定義：

$$
\boxed{
\mathcal S_F
:
\Theta_F
\rightarrow
[0,1].
}
$$

輸出：

$$
p_F.
$$

---

# 83. Surface Ridge

某些條件區可能形成：

$$
\boxed{
\text{Activation Ridge}.
}
$$

即少量條件變化造成 $p_F$ 大幅上升。

---

# 84. Activation Threshold Effect

例如：

$$
V<0.7
\Rightarrow
p_F\approx0.1,
$$

但：

$$
V\geq0.7
\Rightarrow
p_F\approx0.8.
$$

這就是 threshold-like behavior。

---

# 85. Coupling Phase Transition

若多個條件共同跨過門檻：

$$
\Theta_F
\rightarrow
\Theta_F^\ast,
$$

能力表現可能呈非線性跳升。

---

# 86. 這不必是模型內部相變

需要區分：

$$
\boxed{
\text{Model Phase Transition}
}
$$

與：

$$
\boxed{
\text{Coupled-System Phase Transition}.
}
$$

---

# 87. 同一權重也可能出現後者

因為變的是：

- interaction；
- tools；
- verifier；
- strategy；
- memory。

---

# 88. Frontier Activation Experiment（FAE）

本文提出標準實驗。

固定：

$$
AI,
T,
B.
$$

系統性改變：

$$
H,Q,R,M,T_{\mathrm{tool}},V,L.
$$

---

# 89. FAE Step 1：Validate Challenge

先通過：

$$
G_{\mathrm{CCAG}}.
$$

---

# 90. FAE Step 2：Establish Baseline

測：

$$
p_F(\mathcal R_0).
$$

---

# 91. FAE Step 3：Add Coupling Component

例如加入：

$$
M^\ast.
$$

---

# 92. FAE Step 4：Repeat

跨：

- random seeds；
- equivalent task variants；
- independent runs。

---

# 93. FAE Step 5：Verify

由外部 verifier 判定。

---

# 94. FAE Step 6：Ablate

移除：

$$
M^\ast
$$

重新測量。

---

# 95. FAE Step 7：Attribute

判定屬於：

$$
A_0,\ldots,A_5.
$$

---

# 96. FAE Step 8：Generalize

測試是否只對：

$$
T_1
$$

有效，還是對：

$$
\mathcal T
$$

任務族有效。

---

# 97. Activation Profile

最終輸出：

$$
\boxed{
\mathcal A_F
=
\left[
p_F(
\Theta_F^{(i)}
)
\right]_{i=1}^{n}.
}
$$

---

# 98. 不要只輸出平均值

還要保存：

- variance；
- failure modes；
- attribution class；
- verifier disagreement。

---

# 99. Frontier Activation Efficiency

可定義：

$$
\boxed{
\eta_F
=
\frac{
\Delta p_F
}{
\Delta C_{\mathrm{coupling}}
}
}
$$

衡量增加某 coupling cost 帶來多少 activation gain。

---

# 100. Human Cost 也是成本

高 expert coupling 可能很昂貴。

所以：

$$
\boxed{
\text{High CFA}
\neq
\text{Scalable CFA}.
}
$$

---

# 101. Scalable Activation

如果 activation procedure 可以被：

- workflow；
- software；
- verifier；
- AI-generated scaffold；

複製，就更有工程價值。

---

# 102. Transferable Activation

如果：

$$
\Theta_F^\ast
$$

能從：

$$
AI_1
$$

轉移到：

$$
AI_2,
$$

可能表示它是通用方法論，而不是模型-specific prompt。

---

# 103. Model-Specific Activation

有些方法只對特定模型有效。

這也是合法結果。

---

# 104. User-Specific Activation

某 human coupler 可能與某 AI 形成特殊 relational capital。

所以：

$$
\boxed{
\text{Activation Procedure}
}
$$

也可能 person–model specific。

---

# 105. Relational Activation Memory

若成功 activation 被保存：

$$
\Theta_F^\ast
\rightarrow
\mathcal R_{HA},
$$

下次成本可以下降。

---

# 106. Frontier Activation Compounding

因此：

$$
\boxed{
\text{successful activation}
\rightarrow
\text{relational capital}
\rightarrow
\text{lower future activation cost}.
}
$$

---

# 107. 也可能形成錯誤複利

若偶發錯誤被當成成功方法：

$$
\text{FalseActivation}
\rightarrow
\text{Memory},
$$

會造成 systematic misrouting。

---

# 108. 所以每個 activation pattern 必須有 verifier lineage

不能只有：

> 以前這樣 prompt 很有效。

---

# 109. CFA 與 B03 的接口

B02 回答：

> 哪些條件能讓能力進入 tail？

B03 將回答：

> **為什麼一般人根本看不到 tail 已經存在？**

---

# 110. CFA 與 B04 的接口

當 AI 進入 tail 後，錯誤不一定消失。

可能改成更高階的：

- omission；
- boundary mismatch；
- formalization debt；
- architecture residual。

---

# 111. CFA 與 B05 的接口

若 frontier activation 需要越來越高階 coupler：

$$
H^\ast(A,t),
$$

則可研究：

$$
\frac{|H^\ast|}{|H|}
$$

是否下降。

---

# 112. CFA 與 B06 的接口

B06 將把：

$$
\Theta_F
$$

展開成更完整的前沿耦合狀態空間。

---

# 113. CFA 與 B07 的接口

B07 將以高能力專家—AI 協作作為現實 probe，檢查是否出現：

$$
A_3,A_4,A_5
$$

級 activation。

---

# 114. 可證偽命題一

若 CFA 不存在，則：

$$
p_F(\Theta_F)
$$

在控制資訊量與計算預算後，不應隨 coupling structure 穩定大幅變化。

---

# 115. 可證偽命題二

若只是 information injection，則移除人類提供的答案材料後：

$$
p_F\rightarrow p_0.
$$

而 method / verifier 本身不會有顯著 effect。

---

# 116. 可證偽命題三

若方法 activation 真實存在，則：

$$
\Delta_M^{\mathrm{act}}>0
$$

應在多個等價 task variants 重現。

---

# 117. 可證偽命題四

若 AI self-activation 提升，則相同 task family 中：

$$
p_F(\mathcal R_0)
\uparrow
$$

且：

$$
\Delta_H^{\text{act}}
\downarrow.
$$

---

# 118. 可觀測預測

本文提出九個預測：

1. frontier tasks 上，人機 coupling 的 performance variance 會比 ordinary tasks 大。
2. method / representation changes 對 frontier success 的影響會高於表面 prompt wording。
3. external verifier availability 會顯著提高可證成 frontier success。
4. human expert contribution 將逐步從提供答案，移向 problem framing、method selection、error localization 與 verification。
5. 最有價值的 coupling pattern 會被 Agent runtime 逐步吸收與產品化。
6. activation advantage 會因此從低階 prompt skill 移向更高階 meta-cognition。
7. 某些任務會出現明顯 activation threshold，而非線性平滑提升。
8. strong CFA event 應能透過 ablation 與 repeatability 與偶發成功區分。
9. 當 self-activating AI 成熟後，人類 activator 的必要性會降低，但 joint frontier emergence 不一定消失。

---

# 119. 與既有 EveMissLab 研究的關係

## 119.1 CFATC-B01

B01 建立：

$$
C_{\mathrm{latent}}
\neq
C_{\mathrm{realized}}.
$$

B02 正式研究中間的 activation mechanism。

## 119.2 MPD-16

MPD-16 建立：

$$
\text{Same Model}
\neq
\text{Same Effective Productive Tool}.
$$

B02 將 user-effect 分解為可 ablate 的 activation conditions。

## 119.3 LHCF-03 認知阻抗

LHCF 已提出：

$$
R_i(T,\mathbb A,\mathbf b)
$$

是資源條件化成功曲線，而不是單一難度常數。

B02 將 CFA 解釋為：

> 一組能顯著降低有效 cognitive resistance 的耦合條件。

## 119.4 LHCF-04 CCAG

LHCF 已指出：

$$
\text{AI fails}
\not\Rightarrow
\text{task is cognitively deep}.
$$

B02 因此要求 frontier activation 先通過 challenge validity gate。

## 119.5 GIRA Series A

GIRA-A05 已把 method selection、strategy composition、verification 與 reframe 建立為 Global Cognitive Operating Architecture。

CFATC 將同一組能力反過來作為：

> 人類現階段可能替 AI 提供的 frontier activation structure。

---

# 120. 外部研究支點

1. Anthropic, **Agentic Coding and Persistent Returns to Expertise**, June 16, 2026. 約 40 萬次 Claude Code sessions；domain expertise 與 AI work per instruction、session success 具有關聯。
2. Park, Y., Tark, J. & Gong, T., **ExPerT: Personalizing LLM Responses to Users’ Domain Expertise via Query-Wise Semantic and Keystroke Behavioral Cues**, ACL 2026.
3. Dell’Acqua, F. et al., **Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality**, *Organization Science*, published online 2026.
4. Idan, L. & Anand, B., **Generative AI and the Productivity Divide: Human–AI Complementarities in Education and Knowledge Work**, 2026 working paper.
5. Shen, J. H. & Tamkin, A., **How AI Impacts Skill Formation**, 2026.

上述研究都不直接提出本文的 Conditional Frontier Activation；它們分別提供 expertise sensitivity、query-specific expertise adaptation、jagged task frontier、AI interaction competence 與 interaction-pattern heterogeneity的實證支點。

---

# 121. 結論

本文正式提出：

$$
\boxed{
\text{Conditional Frontier Activation}
}
$$

並將其定義為：

> **在有效、可驗證的高難任務上，某組人類—問題—表示—方法—工具—驗證—修復條件，使同一 AI 的 verified realized capability 從 baseline regime 的低概率區，穩定進入其 capability tail。**

形式上：

$$
\boxed{
p_F(A\mid\Theta_F)
=
P(
C_{\mathrm{realized}}
\in
\mathcal C_{\mathrm{tail}}
\mid
A,\Theta_F
).
}
$$

真正強版本 CFA 必須避免三種誤認：

$$
\boxed{
\text{Hard Problem}
\neq
\text{Valid Frontier Problem},
}
$$

$$
\boxed{
\text{Human Gives Answer}
\neq
\text{AI Capability Activation},
}
$$

$$
\boxed{
\text{One Lucky Success}
\neq
\text{Stable Frontier Regime}.
}
$$

所以至少需要：

$$
\boxed{
\text{CCAG}
+
\text{Baseline}
+
\text{Attribution}
+
\text{Verification}
+
\text{Repeatability}
+
\text{Ablation}.
}
$$

本文最重要的歸因階梯是：

$$
\boxed{
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3
\rightarrow
A_4
\rightarrow
A_5.
}
$$

其中真正值得作為人機前沿研究重點的是：

$$
A_3,
A_4,
A_5.
$$

也就是：

> **方法／表示觸發、驗證／修復觸發，以及人機共同產生單方都未穩定具有的新能力。**

因此 CFATC 系列接下來已經有了真正可測量的核心物件。

下一篇 CFATC-B03 將研究：

$$
\boxed{
\text{Capability Visibility Threshold}.
}
$$

即：

> **如果 CFA 真的存在，為什麼大多數普通互動、一般 benchmark 與一般使用者根本看不出 frontier AI 的尾端能力在哪裡？**

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
