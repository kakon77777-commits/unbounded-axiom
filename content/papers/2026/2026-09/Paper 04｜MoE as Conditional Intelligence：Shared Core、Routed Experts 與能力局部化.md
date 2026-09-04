# Paper 04｜MoE as Conditional Intelligence：Shared Core、Routed Experts 與能力局部化

**English Title:** *MoE as Conditional Intelligence: Shared Cores, Routed Experts, and the Problem of Capability Localization*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／Mixture-of-Experts、條件智能與能力地形研究

---

## 摘要

本文提出 **MoE as Conditional Intelligence（MoE 作為條件智能）** 的架構命題。Mixture-of-Experts 最初與當代主要用途之一，是在不讓每個 token 都付出與總參數規模等比例計算成本的前提下，擴張模型總容量。從 Switch Transformer 到 DeepSeekMoE、DeepSeek-V3、Qwen3 等架構，現代 MoE 已經明確展示：

$$
\boxed{
P_{\mathrm{total}}
\gg
P_{\mathrm{active}}
}
$$

可以與高模型能力同時成立。

本文主張，這個事實的理論價值不只在於「MoE 比 dense model 更省算力」。它第一次把大型神經模型中的一項重要設計原則工程化：

$$
\boxed{
\text{一個智能系統可以擁有大量潛在能力，}
\quad
\text{但一次認知操作只啟動其中部分計算。}
}
$$

本文將這種結構稱為 **Conditional Intelligence（條件智能）**。它不是完整的 Mother AI，也不是 Cognitive Kernel 的證明，而是一座介於「全部能力常駐並全量激活」與「能力外部化成獨立模型／Agent／工具」之間的中介橋樑。

本文進一步分析三個不能被混淆的問題：

$$
\boxed{
\text{Conditional Activation}
}
$$

$$
\boxed{
\text{Expert Specialization}
}
$$

$$
\boxed{
\text{Capability Ownership}
}
$$

某個 expert 經常在數學、程式或某類語義 token 上被 router 選中，只能直接支持「activation correlation」，不能直接推出該 expert 擁有該能力的完整因果責任。現有研究已顯示 MoE expert 可以比 dense FFN 呈現較低 polysemanticity，並出現細粒度語言與語義操作的專門化；但這些 expert 並不必然是「biology expert」「math expert」這種整齊的大領域模組。因此：

$$
\boxed{
\text{Routing Correlation}
\neq
\text{Causal Capability Ownership}.
}
$$

本文提出一套公開的 **MoE Capability Tomography Pre-Framework**，以 routing fingerprint、expert activation entropy、single-expert ablation、group ablation、route forcing、expert substitution、shared-path perturbation、top- $k$ variation、load-balancing perturbation 與 cross-task comparison 等方式，逐步區分：

1. routing 行為；
2. expert contribution；
3. expert redundancy；
4. expert synergy；
5. shared-path dependence；
6. task-specific specialization；
7. cross-task invariant capability。

本文特別討論 shared expert。DeepSeekMoE 將一部分 experts 隔離為 shared experts，以捕捉 common knowledge 並減少 routed experts 的冗餘；這對 Resident Cognitive Core 研究是一個非常重要的類比。但 Qwen3 的 MoE 模型也展示了沒有 shared experts 的 pure-routed design 可以成立，因此：

$$
\boxed{
\text{Shared Expert}
\neq
\text{Cognitive Core}
}
$$

更不能推出「沒有 shared expert 就沒有核心能力」。真正的核心能力可能分散於 attention、embedding、normalization、shared backbone、所有 experts 的共同表示，以及跨層路徑之中。

本文提出十四項主要命題、十二類失敗模式與十組可否證實驗，並把 MoE 放在整個《可展開認知核心》系列的正確位置：MoE 不是終局，而是提供一個可觀測的「內部條件計算層」。若未來能從 MoE 的 routing、干預與能力變化中辨識出穩定的核心—條件能力邊界，這些結果才可能進一步支持 Externalized Mixture of Cognitive Experts；若無法辨識，則外部化仍只能以 task-level engineering abstraction 進行，而不能宣稱它是神經模型內部 expert 的直接延伸。

本文的核心命題是：

$$
\boxed{
\text{MoE 證明了能力容量可以條件化，}
}
$$

但它尚未證明：

$$
\boxed{
\text{能力本身已被乾淨模組化。}
}
$$

**關鍵詞：** Mixture-of-Experts、Conditional Intelligence、Expert Routing、Shared Experts、Routed Experts、Expert Specialization、Capability Localization、Cognitive Density、Cognitive Kernel、MoE Interpretability

---

# 0. 研究定位

前一篇提出 Resident Cognitive Core：

$$
K_R
=
(
B_I,
B_R,
B_E,
B_M,
B_W,
B_C,
B_G
).
$$

並將系統能力分成：

$$
\mathcal C_R
$$

Resident，

$$
\mathcal C_Q
$$

Conditionally Activated，

與：

$$
\mathcal C_X
$$

Externally Expanded。

Paper 04 專門研究：

$$
\boxed{
\mathcal C_Q.
}
$$

也就是：

> **什麼叫做「模型擁有一項能力，但不必在每次推理中完整啟動它」？**

MoE 是目前最成熟的大規模工程答案之一。

---

# 1. Dense Model 的基本計算直覺

對典型 dense Transformer block，

每一個 token 通常都通過同一組主要參數：

$$
h_{l+1}
=
F_l(h_l).
$$

因此模型總容量與每次推理使用的參數量高度耦合。

若：

$$
P_{\mathrm{dense}}\uparrow,
$$

通常：

$$
C_{\mathrm{forward}}\uparrow.
$$

這種架構具有結構簡單、計算規律、訓練與部署成熟等優點，但也存在：

$$
\boxed{
\text{capacity--compute coupling}.
}
$$

---

# 2. MoE 的核心反轉

Mixture-of-Experts 將某些 dense feed-forward computation 替換為：

$$
\boxed{
\mathcal E
=
\{
E_1,E_2,\ldots,E_N
\}.
}
$$

Router：

$$
r_l(h)
$$

為 token 選擇少數 experts。

一般形式：

$$
\boxed{
h_{l+1}
=
h_l
+
\sum_{e\in\operatorname{TopK}(r_l(h_l))}
\alpha_{l,e}(h_l)
E_{l,e}(h_l).
}
$$

其中：

$$
K\ll N.
$$

因此：

$$
P_{\mathrm{total}}
\gg
P_{\mathrm{active}}
$$

可以成立。

---

# 3. Switch Transformer：條件容量的早期大型化

Switch Transformer 將 routing 簡化成：

$$
K=1.
$$

每個 token 只送往一個 expert。

它的核心工程意義是大幅增加總參數容量，同時讓單 token 的 activated computation 保持受控。

這提供本文第一個事實基礎：

$$
\boxed{
\text{Total Intelligence Capacity}
\neq
\text{Per-Token Activated Capacity}.
}
$$

這裡的 Intelligence Capacity 仍是架構性的近似概念，不等於已直接量測真正智能。

---

# 4. DeepSeekMoE：從稀疏擴張走向 specialization

DeepSeekMoE 指出傳統 MoE 的問題之一，是 experts 未必充分形成不重疊且聚焦的專門化。

因此提出兩個主要方向：

1. fine-grained expert segmentation；
2. shared expert isolation。

第一項將 experts 切得更細：

$$
N
\rightarrow
mN
$$

同時增加 activated fine-grained experts：

$$
K
\rightarrow
mK.
$$

目的不是只增加 expert 數量，而是讓：

$$
\boxed{
\text{expert combination space}
}
$$

更靈活。

---

# 5. Fine-Grained Experts

假設原本：

$$
E_i
$$

包含多種功能。

將其切成：

$$
E_i^{(1)},
E_i^{(2)},\ldots,E_i^{(m)}.
$$

如果 router 可以組合：

$$
\{
E_a^{(1)},
E_b^{(3)},
E_c^{(2)}
\},
$$

就可能比：

$$
\{
E_a,E_b
\}
$$

具有更細的條件組合能力。

這提供一個重要命題：

$$
\boxed{
\text{Expert Granularity}
}
$$

可能影響：

$$
\boxed{
\text{Capability Composability}.
}
$$

---

# 6. Shared Experts

DeepSeekMoE 的另一設計：

$$
\mathcal E
=
\mathcal E_S
\cup
\mathcal E_R,
$$

其中：

$$
\mathcal E_S
$$

是 shared experts，

$$
\mathcal E_R
$$

是 routed experts。

其設計動機之一是：

$$
\boxed{
\text{capture common knowledge}
}
$$

並：

$$
\boxed{
\text{reduce redundancy among routed experts}.
}
$$

---

# 7. 這很像 Resident + Conditional

從本系列語言看，

可以產生一個非常誘人的類比：

$$
\mathcal E_S
\sim
\mathcal C_R,
$$

$$
\mathcal E_R
\sim
\mathcal C_Q.
$$

也就是：

$$
\boxed{
\text{Shared}
\sim
\text{Resident},
\qquad
\text{Routed}
\sim
\text{Conditional}.
}
$$

但本文立刻加上一個限制：

$$
\boxed{
\sim
\neq
=
}
$$

這只是結構類比，不是能力本體等價。

---

# 8. Qwen3 提供一個重要反例

Qwen3 的 MoE 版本採用：

- 128 experts；
- top-8 activation；
- pure routed experts；
- no shared experts。

這表示：

$$
\boxed{
\text{Shared Expert}
}
$$

不是所有成功 MoE 的必要條件。

因此如果我們說：

> shared expert 就是模型真正的核心認知，

Qwen3 立即構成一個結構反例。

---

# 9. 沒有 Shared Expert 不等於沒有 Shared Capability

這裡必須區分：

$$
\boxed{
\text{Shared Expert}
}
$$

與：

$$
\boxed{
\text{Shared Capability}.
}
$$

即使：

$$
\mathcal E_S=\varnothing,
$$

模型仍然有：

- attention；
- embedding；
- residual stream；
- normalization；
- tokenizer；
- routing network；
- layer topology；
- experts 之間共同訓練形成的表示。

所以：

$$
\boxed{
\mathcal E_S=\varnothing
\not\Rightarrow
\mathcal C_{\mathrm{shared}}=\varnothing.
}
$$

---

# 10. DeepSeek-V3：總容量與 active capacity 的現實尺度

DeepSeek-V3：

$$
P_{\mathrm{total}}
=
671B,
$$

而每 token activated parameters 約：

$$
P_{\mathrm{active}}
=
37B.
$$

因此：

$$
\boxed{
\frac{
P_{\mathrm{active}}
}{
P_{\mathrm{total}}
}
\ll1.
}
$$

這不表示模型「只有 37B 能力」。

而是單一 token 的單次路徑上，實際被激活的參數遠少於總容量。

這正是 Conditional Intelligence 的核心工程事實。

---

# 11. Qwen3 再次提供不同設計點

Qwen3-235B-A22B：

$$
P_{\mathrm{total}}
\approx235B,
$$

$$
P_{\mathrm{active}}
\approx22B.
$$

128 experts 中：

$$
K=8
$$

被激活。

這說明：

$$
\boxed{
\text{Conditional Capacity}
}
$$

已成為大型模型設計的重要方向之一。

---

# 12. 本文定義 Conditional Intelligence

對智能系統 $S$，

若存在能力資源集合：

$$
\mathcal C_{\mathrm{available}}
$$

但對任務：

$$
t
$$

只激活：

$$
\mathcal C_{\mathrm{active}}(t)
\subset
\mathcal C_{\mathrm{available}},
$$

則稱系統具有：

$$
\boxed{
\text{Conditional Intelligence Structure}.
}
$$

要求：

$$
|\mathcal C_{\mathrm{active}}(t)|
<
|\mathcal C_{\mathrm{available}}|
$$

對大量任務成立。

---

# 13. 這是一個功能定義

Conditional Intelligence 不要求：

$$
\mathcal C_i
$$

一定是一個神經 expert。

它可以由 neural expert、adapter、module、tool、model、Sub-AI 提供。

但 Paper 04 只研究：

$$
\boxed{
\text{internal neural MoE}.
}
$$

外部版本留給 Paper 05。

---

# 14. MoE 的真正架構意義

MoE 已經證明：

$$
\boxed{
\text{擁有能力}
\not\Rightarrow
\text{每次都必須啟動能力}.
}
$$

如果：

$$
\mathcal C
=
\{
c_1,\ldots,c_n
\},
$$

每個任務都強迫：

$$
\forall i,\quad c_i\text{ active},
$$

就會形成：

$$
\boxed{
\text{cognitive over-activation}.
}
$$

---

# 15. Conditional Intelligence 不等於 Modularity

即使：

$$
E_1,\ldots,E_N
$$

是不同 expert，

仍不能直接說：

$$
\boxed{
E_i
=
\text{獨立能力模組}.
}
$$

因為 expert 的輸入來自：

$$
h_l,
$$

而：

$$
h_l
$$

已經包含前面多層共同計算。

Expert 的能力可能依賴 attention、earlier layers、residual state、other experts 與 routing history。

因此：

$$
\boxed{
\text{Sparse Activation}
\neq
\text{Functional Independence}.
}
$$

---

# 16. Conditional Intelligence 也不等於 Expert Identity

如果 expert：

$$
E_i
$$

在某一類 token 高頻啟動，

它可能只是 syntax processor、formatting operator、rare token handler、local semantic transformation 或 load-balancing consequence。

因此不能直接命名：

> Math Expert 17。

除非有足夠因果證據。

---

# 17. Expert-Level Interpretability 的新證據

2026 的 expert-level interpretability 研究提供重要訊號：

MoE expert neurons 相較 dense FFN neurons，可以呈現：

$$
\boxed{
\text{lower polysemanticity}.
}
$$

並且 routing sparsity 增加時，這個差異可能更明顯。

這支持：

$$
\boxed{
\text{MoE experts may be better interpretability units than dense FFNs}.
}
$$

---

# 18. 但 Expert 並不是大領域部門

同一研究的重要結果之一是：

experts 並不主要表現成 biology、physics、history 這種 broad domain expert。

更常見的是：

$$
\boxed{
\text{fine-grained linguistic / semantic operations}.
}
$$

這對本文非常重要。

因為它告訴我們：

$$
\boxed{
\text{human task category}
\neq
\text{neural expert category}.
}
$$

---

# 19. 人類分類與模型內部分解可能不同

人類說：

$$
\text{coding}
$$

可能在模型內部需要 bracket handling、variable relation、indentation、symbolic continuation、API pattern、type relation 與 long dependency。

因此：

$$
\boxed{
C_{\mathrm{coding}}
=
\operatorname{Compose}
(
c_1,c_2,\ldots,c_m
).
}
$$

這些 $c_i$ 可能分散在不同 experts 和 layers。

---

# 20. Capability Ownership 問題

我們真正想知道：

> 哪個 expert「擁有」某項能力？

但「擁有」必須定義。

本文提出五個層級：

## Level 0：Correlation

$$
E_i
$$

常被某任務激活。

## Level 1：Contribution

移除：

$$
E_i
$$

性能下降。

## Level 2：Specific Contribution

性能只在某類任務顯著下降。

## Level 3：Substitutability Structure

另一 expert 或 module 可以恢復這項能力。

## Level 4：Causal Functional Ownership

存在穩定、可重複、跨 prompt、跨樣本的因果責任結構。

本文主張：

$$
\boxed{
\text{Level 0}
\not\Rightarrow
\text{Level 4}.
}
$$

---

# 21. Routing Correlation

定義任務族：

$$
T.
$$

第 $l$ 層 expert $e$ 的 routing frequency：

$$
\boxed{
\rho_T(l,e)
=
\mathbb E_{x\sim T}
\left[
\frac{
1
}{
|x|
}
\sum_{t\in x}
\mathbf 1
\{
e\in\operatorname{TopK}(r_l(h_t))
\}
\right].
}
$$

這稱為：

$$
\boxed{
\text{Routing Fingerprint}.
}
$$

---

# 22. Routing Fingerprint 的用途

比較：

$$
\rho_{T_1},
\rho_{T_2},
\dots,
\rho_{T_n}
$$

可以觀察 task discrimination、expert reuse、cross-domain commonality、high-frequency experts 與 rare specialized paths。

但只能得到：

$$
\boxed{
\text{observational structure}.
}
$$

---

# 23. Routing Entropy

定義某 token 的 router distribution：

$$
p_{l,e}(x_t).
$$

則：

$$
\boxed{
H_R(l,x_t)
=
-\sum_e
p_{l,e}(x_t)
\log
p_{l,e}(x_t).
}
$$

對任務族：

$$
\boxed{
\overline H_R(T,l)
=
\mathbb E_{x,t}
[
H_R(l,x_t)
].
}
$$

它可以反映 routing concentration、ambiguity、specialization 與 load-balancing pressure。

但：

$$
\boxed{
H_R
\neq
Q_{\mathrm{capability}}.
}
$$

---

# 24. Routing Margin

Top-1 與 Top-2 routing score：

$$
s_1,s_2.
$$

定義：

$$
\boxed{
M_R
=
s_1-s_2.
}
$$

較小：

$$
M_R
$$

可能表示 expert choice 不穩、experts 可替代，或 token 位於能力邊界。

---

# 25. Load Balancing 會污染語義解讀

MoE router 不只追求：

$$
\text{best semantic expert}.
$$

訓練系統還需要 capacity、utilization、load balancing 與 communication constraints。

因此實際 routing 可能是：

$$
\boxed{
\text{semantic fit}
+
\text{optimization pressure}
+
\text{systems pressure}.
}
$$

如果忽略這件事，就會把：

$$
\text{routing artifact}
$$

錯認成：

$$
\text{capability structure}.
$$

---

# 26. Routing Testbed 的方法論意義

2026 的 MoE Routing Testbed 研究指出，如果要研究 specialization，需要分辨 routing 本身是否真的形成非冗餘專門化。

其結果顯示 balancing scope 對 specialization 與 expert utilization 很重要。

這支持：

$$
\boxed{
\text{Routing Policy}
}
$$

本身也是：

$$
\boxed{
\text{experimental variable}.
}
$$

而不是能力觀測的透明窗口。

---

# 27. 因此需要 Causal Tomography

從：

$$
\text{Observe}
$$

進入：

$$
\boxed{
\text{Intervene}.
}
$$

本文提出：

$$
\boxed{
\text{MoE Capability Tomography}
}
$$

作為後續方法論。

Paper 04 只公開一般干預類型，不公開特定私人搜索策略。

---

# 28. Single-Expert Ablation

定義 baseline：

$$
Q(T).
$$

移除 expert：

$$
E_i.
$$

得到：

$$
Q(T\mid -E_i).
$$

定義：

$$
\boxed{
I_i(T)
=
Q(T)-Q(T\mid -E_i).
}
$$

若：

$$
I_i(T)\gg0,
$$

表示：

$$
E_i
$$

對任務 $T$ 有因果貢獻候選。

---

# 29. Ablation 仍然不能直接等於 Ownership

因為：

$$
E_i
$$

可能是 bottleneck、routing hub、generic formatter 或 shared dependency。

移除後所有任務都下降。

因此需要比較：

$$
I_i(T_1),
I_i(T_2),\ldots.
$$

---

# 30. Specificity Score

定義：

$$
\boxed{
S_i(T)
=
\frac{
I_i(T)
}{
\epsilon+
\mathbb E_{T'\neq T}
[
I_i(T')
]
}.
}
$$

如果：

$$
S_i(T)\gg1,
$$

才比較支持：

$$
\boxed{
\text{task-specific contribution}.
}
$$

---

# 31. Group Ablation

真正能力可能由：

$$
\{
E_i,E_j,E_k
\}
$$

共同提供。

因此：

$$
I_{\{i,j\}}(T)
$$

不一定：

$$
=
I_i(T)+I_j(T).
$$

定義 synergy：

$$
\boxed{
Y_{ij}(T)
=
I_{\{i,j\}}(T)
-
I_i(T)
-
I_j(T).
}
$$

如果：

$$
Y_{ij}>0,
$$

可能存在互補作用。

---

# 32. Redundancy

如果：

$$
I_i(T)\approx0,
$$

$$
I_j(T)\approx0,
$$

但：

$$
I_{\{i,j\}}(T)\gg0,
$$

則：

$$
E_i,E_j
$$

可能互為備援。

這對 externalization 非常重要。

因為：

$$
\boxed{
\text{低單點重要性}
}
$$

不等於：

$$
\boxed{
\text{能力不重要}.
}
$$

---

# 33. Route Forcing

對 token：

$$
x_t,
$$

強迫 router 選：

$$
E_i
$$

而不是原本：

$$
E_j.
$$

比較：

$$
Q(T\mid r\rightarrow i).
$$

這可以測 expert 是否真的適合該 token，而不只是 router 喜歡選它。

---

# 34. Expert Substitution

假設：

$$
E_i
$$

被移除。

嘗試：

$$
E_j
\rightarrow
E_i.
$$

若性能恢復：

$$
Q(T\mid -E_i,+E_j)
\approx
Q(T),
$$

則：

$$
\boxed{
E_i
}
$$

不是不可替代。

---

# 35. Expert Permutation

如果將 routing identity：

$$
E_i
\leftrightarrow
E_j
$$

交換，

觀察：

$$
\Delta Q.
$$

可以研究 expert identity、routing dependence 與 layer-specific specialization。

---

# 36. Top- $k$ Variation

改變：

$$
k.
$$

例如：

$$
k=1,2,4,8.
$$

測：

$$
Q_C,
C_A,
H_R,
\text{specialization}.
$$

若：

$$
k\uparrow
$$

使能力增加但 specialization 下降，

則存在：

$$
\boxed{
\text{capacity--specialization trade-off}.
}
$$

---

# 37. Shared-Expert Ablation

對具有 shared experts 的模型，

比較：

$$
Q(T)
$$

與：

$$
Q(T\mid -\mathcal E_S).
$$

再比較：

$$
Q(T\mid -\mathcal E_R^{specific}).
$$

如果 shared experts 在大量任務都高度重要，

它們可能是：

$$
\boxed{
\text{common dependency}.
}
$$

但仍不能直接叫：

$$
\boxed{
\text{Cognitive Kernel}.
}
$$

---

# 38. Why Shared Expert Is Not Cognitive Kernel

至少有五個原因：

1. shared expert 只是 FFN path 的一部分；
2. attention 仍高度重要；
3. embeddings / residual stream 不在 shared expert 中；
4. shared expert 可能保存 common statistical knowledge，不一定是 meta-cognition；
5. pure-routed MoE 也可以工作。

因此：

$$
\boxed{
\mathcal E_S
\subsetneq
\text{possible shared computation}.
}
$$

---

# 39. Core Capability 可能是 Distributed Core

本文提出：

$$
\boxed{
\mathcal C_{\mathrm{core}}
}
$$

可以由：

$$
\text{attention}
+
\text{shared representations}
+
\text{routing}
+
\text{cross-expert invariants}
+
\text{runtime state}
$$

共同提供。

因此真正的 core：

$$
\boxed{
\text{may be distributed rather than localized}.
}
$$

---

# 40. Capability Locality Spectrum

本文提出：

$$
\boxed{
L_C(c)\in[0,1].
}
$$

其中：

$$
L_C(c)\rightarrow1
$$

表示能力高度集中於少數可辨識結構。

$$
L_C(c)\rightarrow0
$$

表示能力高度分散。

這不是現成可直接量測的標準，而是研究目標。

---

# 41. Expert Concentration Proxy

對能力 $c$，

若已得到各 expert contribution：

$$
I_i(c),
$$

可以正規化：

$$
p_i(c)
=
\frac{
\max(I_i(c),0)
}{
\sum_j
\max(I_j(c),0)
}.
$$

再計算：

$$
\boxed{
H_C(c)
=
-\sum_i
p_i(c)\log p_i(c).
}
$$

較低：

$$
H_C
$$

可能代表能力更集中。

---

# 42. 但 Concentration 不等於 Separability

即使：

$$
H_C(c)\ll1,
$$

能力可能仍依賴：

$$
h_l
$$

中的 distributed representation。

所以：

$$
\boxed{
\text{Concentrated Contribution}
\neq
\text{Cleanly Extractable Module}.
}
$$

---

# 43. Separability Score

真正 externalization 需要更強條件。

概念上定義：

$$
\boxed{
S_{\mathrm{sep}}(c)
=
f(
L_C,
R_{\mathrm{sub}},
C_{\mathrm{interface}},
Q_{\mathrm{restore}}
).
}
$$

其中：

- $L_C$：locality；
- $R_{\mathrm{sub}}$：substitutability；
- $C_{\mathrm{interface}}$：interface cost；
- $Q_{\mathrm{restore}}$：移除後由外部能力恢復品質。

Paper 04 不實作它。

Paper 05 會利用這個方向。

---

# 44. MoE 是能力地形的顯微鏡

本文因此提出：

$$
\boxed{
\text{MoE as Capability Microscope}.
}
$$

理由是 dense model 的主要 FFN 參數缺乏天然的條件分派界面，而 MoE 自然產生：

$$
\boxed{
\text{routing variation}.
}
$$

這提供 conditional paths、identifiable expert units 與 intervention targets。

---

# 45. 但顯微鏡不是地圖

Router 顯示：

$$
\text{where computation went},
$$

不直接顯示：

$$
\text{why cognition succeeded}.
$$

因此：

$$
\boxed{
\text{MoE Routing Map}
\neq
\text{Capability Causal Map}.
}
$$

---

# 46. Multi-Layer Path

真正 routing 應表示成：

$$
\boxed{
\pi(x)
=
(
e_1,e_2,\ldots,e_L
).
}
$$

其中：

$$
e_l
$$

是第 $l$ 層選中的 expert set。

能力可能不在：

$$
e_l
$$

單點，

而在：

$$
\boxed{
\pi(x)
}
$$

整條 path。

---

# 47. Path Fingerprint

對 task family $T$，

定義：

$$
\boxed{
P_T
=
\operatorname{Distribution}
(
\pi(x)
\mid
x\sim T
).
}
$$

這可能比單 expert frequency 更接近：

$$
\boxed{
\text{cognitive route signature}.
}
$$

---

# 48. Path Intervention

可以對：

$$
\pi(x)
$$

進行 prefix preservation、suffix replacement、middle-layer swap 與 selected-layer forcing。

測：

$$
\Delta Q.
$$

這有助於區分：

$$
\boxed{
\text{where capability emerges along depth}.
}
$$

---

# 49. Expert Specialization 可能是階層式

可能存在：

早層：

$$
\text{syntax / token pattern},
$$

中層：

$$
\text{semantic relation},
$$

後層：

$$
\text{task output transformation}.
$$

因此：

$$
\boxed{
\text{expert semantics}
=
f(
layer,
context,
route history
).
}
$$

不能只用單一全模型標籤。

---

# 50. 共享能力可能是跨 expert 的 intersection

若多個 experts：

$$
E_1,\ldots,E_N
$$

都包含某種共同子能力：

$$
c_0,
$$

則：

$$
\boxed{
c_0
\in
\bigcap_i
\mathcal C(E_i)
}
$$

但它沒有被放在一個 shared expert。

這就是：

$$
\boxed{
\text{distributed shared capability}.
}
$$

---

# 51. 冗餘可能是 feature，不只是 waste

DeepSeekMoE 希望降低 routed expert redundancy。

但對 reliability 而言，

某些 redundancy 可能提供 failover、robustness 與 uncertainty smoothing。

因此：

$$
\boxed{
\text{redundancy}
\neq
\text{always waste}.
}
$$

Externalized experts 也必須考慮這點。

---

# 52. Expert Specialization 與 Robustness

過度 specialization：

$$
S_E\uparrow
$$

可能導致：

$$
R_{\mathrm{robust}}\downarrow.
$$

如果某 expert：

$$
E^\ast
$$

失效，

整類能力可能消失。

因此需要研究：

$$
\boxed{
\text{specialization--redundancy frontier}.
}
$$

---

# 53. Conditional Intelligence 與 Cognitive Density

Paper 02 定義：

$$
D_A
=
\frac{
Q_C
}{
\mathbb E[C_A]
}.
$$

MoE 的理想就是：

$$
P_{\mathrm{total}}\uparrow
$$

而：

$$
C_A
$$

受控。

因此：

$$
\boxed{
D_A
}
$$

是評估 MoE 是否真的提高認知密度的重要量。

---

# 54. 不能只看 activated parameters

因為實際 MoE 成本還包括：

$$
\boxed{
C_{\mathrm{MoE}}
=
C_{\mathrm{expert}}
+
C_{\mathrm{router}}
+
C_{\mathrm{dispatch}}
+
C_{\mathrm{communication}}
+
C_{\mathrm{imbalance}}
+
C_{\mathrm{cache}}.
}
$$

所以：

$$
P_{\mathrm{active}}\downarrow
$$

不必然：

$$
\text{wall-clock cost}\downarrow.
$$

---

# 55. Communication Tax

如果 experts 分散在不同 devices，

會產生：

$$
C_{\mathrm{all-to-all}}.
$$

這可能使 theoretical sparse FLOPs 與 real serving efficiency 差距很大。

因此 Paper 04 不將 MoE 描述成免費容量。

---

# 56. Load Imbalance Tax

如果大量 token 都選：

$$
E_i,
$$

會造成 queue、token drop、capacity overflow 與 utilization loss。

因此 router 需要 balancing。

但 balancing 又會改變 routing semantics。

這是一個：

$$
\boxed{
\text{interpretability--systems coupling}.
}
$$

---

# 57. Conditional Intelligence 的三層成本

本文將 MoE 成本分成：

$$
\boxed{
C_{\mathrm{semantic}}
}
$$

能力是否選對 expert；

$$
\boxed{
C_{\mathrm{routing}}
}
$$

選 expert 的計算與錯誤；

$$
\boxed{
C_{\mathrm{systems}}
}
$$

dispatch、communication、memory、load balancing。

只有三者一起評估，才能知道 MoE 是否真的提高：

$$
D_A.
$$

---

# 58. Mother Model 對 MoE 的新問題

對一般 MoE：

問題是：

> 怎麼在同樣 FLOPs 下提高模型品質？

對 Mother Model：

還要問：

> 哪些 abilities 應該是 shared / resident？

> 哪些應該 routed？

> 哪些根本不該留在模型內？

這將 MoE 問題推成：

$$
\boxed{
\text{Cognitive Placement Problem}.
}
$$

---

# 59. Cognitive Placement

對能力：

$$
c,
$$

選擇：

$$
\boxed{
\operatorname{Place}(c)
\in
\{
R,Q,X
\}.
}
$$

其中：

- $R$：Resident；
- $Q$：Conditional；
- $X$：External。

Paper 03 定義 Resident Necessity。

Paper 04 開始研究：

$$
\boxed{
Q.
}
$$

---

# 60. Conditional Necessity

可以定義：

$$
\boxed{
N_Q(c)
=
f(
F_c,
L_c,
S_c,
C_c,
X_c
).
}
$$

能力較適合 conditional，如果它不是每個任務都需要、activation latency 必須很低、與模型 hidden representation 緊耦合、外部 API 往返太慢，或仍需要神經模型內部細粒度組合。

---

# 61. Conditional vs External

如果某能力：

$$
c
$$

只在：

$$
1\%
$$

任務需要，

但每次需要時必須 token-level 與其他能力交互，

它可能適合：

$$
\boxed{
Q
}
$$

而不是：

$$
X.
$$

反之，如果能力可以 subtask-level call 完成，則可能適合：

$$
X.
$$

---

# 62. Granularity Boundary

因此 externalization 的核心問題之一是：

$$
\boxed{
G_c
=
\text{interaction granularity}.
}
$$

如果：

$$
G_c
\rightarrow
\text{token-level},
$$

外部化很困難。

如果：

$$
G_c
\rightarrow
\text{task-level},
$$

外部化較可行。

---

# 63. 這是 Paper 05 的橋

Paper 05 將問：

$$
\boxed{
\text{Why must an expert live inside one model?}
}
$$

但答案不能只是：

> API call。

因為 Micro-MoE expert 的 interface：

$$
h_l\in\mathbb R^d
$$

而 external model 的 interface 通常是：

$$
\text{text / structured context / multimodal input}.
$$

因此需要：

$$
\boxed{
\text{Granularity Lift}.
}
$$

從 token-level expert 提升為 cognitive-operation-level expert。

---

# 64. Internal MoE 與 External MoE 不同

本文先明確：

$$
\boxed{
\text{Internal MoE}
\neq
\text{External Model Routing}.
}
$$

Internal MoE：

- joint training；
- shared hidden space；
- token-level routing；
- low interface latency。

External model routing：

- independent training；
- heterogeneous representation；
- coarse-grained context；
- network / process boundary；
- higher latency。

---

# 65. 但兩者共享一個抽象

兩者都可以寫成：

$$
\boxed{
x
\rightarrow
r(x)
\rightarrow
E_i(x).
}
$$

差別在：

$$
\boxed{
\text{routing granularity}
+
\text{representation boundary}
+
\text{coordination cost}.
}
$$

這就是 Paper 05 可以從 MoE 往外延伸的原因。

---

# 66. MoE 與 Sub-AI Fabric 的結構同構

Sub-AI Fabric：

$$
\mathcal A
=
\{
A_1,\ldots,A_n
\}.
$$

MoE：

$$
\mathcal E
=
\{
E_1,\ldots,E_N
\}.
$$

都存在：

$$
\boxed{
\text{selection}
+
\text{specialization}
+
\text{combination}.
}
$$

但：

$$
\boxed{
\text{structural analogy}
\neq
\text{implementation identity}.
}
$$

---

# 67. 為什麼這個同構仍然重要？

因為它讓我們可以跨尺度問同一個問題：

$$
\boxed{
\text{What should be shared?}
}
$$

$$
\boxed{
\text{What should be specialized?}
}
$$

$$
\boxed{
\text{What should be routed?}
}
$$

$$
\boxed{
\text{What should be redundant?}
}
$$

$$
\boxed{
\text{What should be retired?}
}
$$

---

# 68. MoE 可以反向教 Mother AI

如果一個成熟 MoE 在大量 task 上形成：

$$
\rho_T(l,e),
$$

我們可以研究哪些 computation repeatedly appear across tasks，以及哪些只在特定 task family 出現。

這可能對：

$$
\boxed{
\text{Resident Core Hypothesis}
}
$$

提供經驗線索。

---

# 69. 但不能直接從 activation frequency 決定 residency

高頻 expert：

$$
\rho(e)\uparrow
$$

可能只是 punctuation、common token、syntax 或 balancing artifact。

所以：

$$
\boxed{
\text{Frequency}
\neq
\text{Global Cognitive Centrality}.
}
$$

需要 Paper 03 的：

$$
N_R(z)
$$

與 causal tests。

---

# 70. Shared Core Candidate 的必要證據

若要將某 neural structure 稱為：

$$
\boxed{
\text{Core Candidate},
}
$$

至少應有：

1. high cross-task contribution；
2. low substitutability；
3. high error propagation radius；
4. cross-prompt stability；
5. cross-domain involvement；
6. causal, not merely routing correlation；
7. regression under ablation；
8. limited recovery by unrelated experts。

---

# 71. Routed Capability Candidate

反過來，一個 conditional capability candidate 應更像：

1. task-selective activation；
2. task-selective causal contribution；
3. low cross-task necessity；
4. substitutable by related experts；
5. bounded failure radius；
6. stable routing signature；
7. performance gain larger than routing cost。

---

# 72. Expert Pair / Set 才可能是能力單位

能力 $c$ 可能：

$$
c
\not\approx
E_i.
$$

而：

$$
\boxed{
c
\approx
\{
E_{i_1},
E_{i_2},
\ldots,
E_{i_k}
\}.
}
$$

甚至依 layer sequence：

$$
\boxed{
c
\approx
(
E_{i_1}^{l_1}
\rightarrow
E_{i_2}^{l_2}
\rightarrow
\cdots
).
}
$$

因此 tomography 必須支援 set / path analysis。

---

# 73. Emergent Modular Composition

如果任務能力：

$$
c
$$

來自不同細粒度 expert 組合，

就可能形成：

$$
\boxed{
\text{emergent modularity}.
}
$$

模組不是一個 expert，

而是：

$$
\boxed{
\text{dynamically composed expert subgraph}.
}
$$

這個概念對外部 Cognitive MoE 很重要。

---

# 74. Dynamic Expert Subgraph

定義對任務：

$$
T,
$$

激活圖：

$$
\boxed{
G_E(T)
=
(
V_E(T),
E_E(T),
\omega_E(T)
).
}
$$

其中：

- $V_E(T)$：被激活 expert；
- $E_E(T)$：跨層 path 關係；
- $\omega_E(T)$：routing weights / contribution。

能力可能屬於：

$$
\boxed{
G_E(T)
}
$$

而不是：

$$
E_i.
$$

---

# 75. Capability Tomography 的第一個目標

不是找「數學 expert」。

而是：

$$
\boxed{
\text{估計能力在 expert graph 中的因果分布}.
}
$$

形式上：

$$
\boxed{
\Phi_c:
G_E
\rightarrow
\mathbb R_{\ge0}.
}
$$

其中：

$$
\Phi_c(v)
$$

表示某結構對能力 $c$ 的因果貢獻估計。

---

# 76. 第二個目標：找能力邊界

比較：

$$
c_1,c_2
$$

的：

$$
\Phi_{c_1},
\Phi_{c_2}.
$$

定義 overlap：

$$
\boxed{
O(c_1,c_2)
=
\operatorname{Overlap}
(
\Phi_{c_1},
\Phi_{c_2}
).
}
$$

若：

$$
O\rightarrow1,
$$

兩能力高度共享計算。

若：

$$
O\rightarrow0,
$$

較容易分離。

---

# 77. 第三個目標：找 Shared Cognitive Substrate

對能力集合：

$$
\mathcal C^\ast
=
\{
c_1,\ldots,c_m
\},
$$

找：

$$
\boxed{
\Phi_{\mathrm{shared}}
=
\bigcap_i
\Phi_{c_i}.
}
$$

這可能提供：

$$
\boxed{
\text{Resident Cognitive Core candidate}.
}
$$

但仍需 cross-model validation。

---

# 78. Cross-Model Validation

若只在：

$$
M_1
$$

看到某結構，

可能是該模型偶然形成。

因此比較：

$$
M_1,M_2,\ldots,M_n.
$$

真正強命題需要：

$$
\boxed{
\text{functional invariance across architectures}
}
$$

而不是：

$$
\boxed{
\text{same neuron indices}.
}
$$

---

# 79. Cross-Version Validation

模型：

$$
M^{v_1}
\rightarrow
M^{v_2}
$$

後，

若：

$$
\Phi_c
$$

完全改變，

但能力仍保持，

表示：

$$
\boxed{
\text{mechanism is non-identifiable or highly plastic}.
}
$$

這會降低乾淨 externalization 的可能性。

---

# 80. MoE 是天然的 Parallel Research Surface

MoE 有：

$$
N
$$

個 experts，

可以同時展開 routing analysis、activation analysis、causal ablation、expert labeling 與 cross-task comparison。

因此非常適合：

$$
\boxed{
\text{parallel AI-assisted research}.
}
$$

---

# 81. Parallel Analysis 不應提前收斂

可以讓不同分析通道分別研究：

$$
H_1:
\text{linguistic specialization}
$$

$$
H_2:
\text{semantic specialization}
$$

$$
H_3:
\text{causal contribution}
$$

$$
H_4:
\text{systems routing}
$$

$$
H_5:
\text{expert redundancy}
$$

最後才：

$$
\boxed{
\operatorname{Synthesize}(H_1,\ldots,H_5).
}
$$

避免：

$$
\boxed{
\text{first interpretation lock-in}.
}
$$

---

# 82. Mechanical Analysis 與 AI Interpretation 要分開

AI 可以 label expert behavior、summarize activation patterns、propose hypotheses。

但機械層應保存：

- raw routing；
- logits；
- activation；
- ablation result；
- benchmark delta；
- checkpoint；
- hash。

因此：

$$
\boxed{
\text{AI interpretation}
\neq
\text{mechanical evidence}.
}
$$

---

# 83. Expert Label 必須版本化

如果 AI 說：

> Expert 17 = bracket closer，

這只是：

$$
\boxed{
\text{hypothesis label}.
}
$$

需要保存：

$$
(
label,
model,
layer,
expert,
dataset,
method,
confidence,
timestamp
).
$$

避免 label 變成永久真理。

---

# 84. Load-Balancing Counterfactual

修改 balancing policy，

但保持 model family 與 task 相近。

若 expert semantics 大幅改變，

表示：

$$
\boxed{
\text{specialization partly induced by routing policy}.
}
$$

而不是自然固定能力器官。

---

# 85. Expert Count Counterfactual

比較：

$$
N=8,32,128,256,\ldots.
$$

測 specialization、redundancy、polysemanticity、active compute 與 quality。

可能存在：

$$
\boxed{
\text{expert granularity phase transition}.
}
$$

這是一個公開可研究命題。

---

# 86. Active Expert Count Counterfactual

固定：

$$
N,
$$

改：

$$
K.
$$

如果：

$$
K\downarrow
$$

specialization 提高，

但：

$$
Q\downarrow,
$$

則：

$$
\boxed{
\text{sparsity--capability trade-off}.
}
$$

---

# 87. Shared Expert Count Counterfactual

對具有 shared expert 設計：

$$
K_s=0,1,2,\ldots
$$

比較 routed redundancy、common-task quality、expert diversity 與 load distribution。

這可測：

$$
\boxed{
\text{shared capacity necessity}.
}
$$

---

# 88. Capability Restoration Test

如果移除 expert set：

$$
A,
$$

性能下降：

$$
\Delta Q<0.
$$

再加入：

$$
B
$$

若：

$$
Q(-A+B)
\approx
Q,
$$

則 $B$ 可以視為：

$$
\boxed{
\text{functional substitute candidate}.
}
$$

這比單純 routing label 更接近 externalization evidence。

---

# 89. Latent Interface 問題

即使 expert：

$$
E_i
$$

功能很乾淨，

它接收的是：

$$
h_l.
$$

如果拿到模型外：

$$
E_i^{external},
$$

需要：

$$
\boxed{
h_l
\rightarrow
\text{external interface}
}
$$

再：

$$
\boxed{
\text{return}
\rightarrow
h_{l+1}.
}
$$

這在 latency、representation、security 上非常困難。

因此：

$$
\boxed{
\text{separable}
\not\Rightarrow
\text{externally deployable}.
}
$$

---

# 90. 因此真正外部化需要 Granularity Lift

不是：

$$
\boxed{
\text{copy internal expert to API}.
}
$$

而可能是：

$$
\boxed{
\text{internal fine-grained capability}
\rightarrow
\text{higher-level cognitive operation}
\rightarrow
\text{external executor}.
}
$$

這就是 Paper 05 的中心問題。

---

# 91. MoE 不是 Mother AI

MoE 本身通常沒有 persistent goal、world state、model market、Sub-AI lifecycle、authority graph 或 durable self-model。

因此：

$$
\boxed{
\text{MoE}
\neq
\text{Mother AI}.
}
$$

它只是：

$$
\boxed{
\text{conditional neural computation substrate}.
}
$$

---

# 92. 但 MoE 很適合 Mother Model

因為 Mother Model 理論上需要 high-frequency core、lower-frequency specialized reasoning 與 heterogeneous task adaptation。

MoE 提供：

$$
\boxed{
\text{internal low-latency conditional capacity}.
}
$$

所以它可能是：

$$
\boxed{
\text{Resident Core + Conditional Expert Layer}
}
$$

的一種候選實作方向。

---

# 93. Dense Core + MoE Shell

一個公開架構猜想：

$$
\boxed{
M
=
K_{\mathrm{dense}}
+
E_{\mathrm{MoE}}.
}
$$

其中：

$$
K_{\mathrm{dense}}
$$

偏向高 resident necessity，

$$
E_{\mathrm{MoE}}
$$

偏向 conditional abilities。

本文不宣稱這一定優於 pure MoE，只是可測架構。

---

# 94. Shared MoE Core + Routed Experts

另一個：

$$
\boxed{
M
=
E_S
+
E_R.
}
$$

但必須：

$$
E_S
$$

真正被訓練與驗證成 interpretation、epistemic、meta 與 governance-supporting reasoning。

現有 shared expert 設計本身不能保證。

---

# 95. Pure Routed MoE + Distributed Core

Qwen3 類架構提醒：

$$
\boxed{
\text{core may remain distributed}.
}
$$

因此：

$$
M
=
A_{\mathrm{shared}}
+
E_R,
$$

其中：

$$
A_{\mathrm{shared}}
$$

可能主要存在於 attention / shared backbone。

這也是合法候選。

---

# 96. Hierarchical MoE

未來可能：

$$
r_1
\rightarrow
\text{capability family}
$$

再：

$$
r_2
\rightarrow
\text{fine expert}.
$$

這更接近：

$$
\boxed{
\text{cognitive hierarchy}.
}
$$

但同樣需要因果驗證。

---

# 97. Dynamic Expert Generation

更遠一步：

$$
\mathcal E_t
$$

不是固定。

而：

$$
\boxed{
\mathcal E_{t+1}
=
F(
\mathcal E_t,
T,
H
).
}
$$

也就是 expert 可以 spawn、merge、retire、specialize。

這就開始接近 Sub-AI Fabric。

---

# 98. Internal Expert Lifecycle 與 Sub-AI Lifecycle

Sub-AI：

$$
\text{Template}
\rightarrow
\text{Spawn}
\rightarrow
\text{Bind}
\rightarrow
\text{Operate}
\rightarrow
\text{Evaluate}
\rightarrow
\text{Retire}.
$$

若未來 neural expert 也能：

$$
\boxed{
\text{dynamically generated / retired},
}
$$

兩者架構距離會進一步縮小。

---

# 99. 但本文不宣稱它們必然收斂

神經 expert 與 Agent 仍有巨大差異：

- timescale；
- interface；
- autonomy；
- memory；
- tool use；
- authority。

因此：

$$
\boxed{
\text{MoE--Agent convergence}
}
$$

目前只是研究方向，不是本文結論。

---

# 100. 十二類失敗模式

## 100.1 Routing-as-Meaning Fallacy

把 routing frequency 直接當 capability semantics。

## 100.2 Shared-Expert-as-Core Fallacy

把 shared expert 直接等同 Cognitive Kernel。

## 100.3 Broad-Domain Labeling Error

硬把 fine-grained expert 標成 broad domain expert。

## 100.4 Load-Balancing Confound

routing 受到 balancing policy 影響而被誤讀。

## 100.5 Single-Expert Fallacy

忽略能力由 expert set / path 組成。

## 100.6 Ablation Misinterpretation

性能下降來自一般 bottleneck，而非 task-specific capability。

## 100.7 Redundancy Blindness

單 expert ablation 無影響就誤判能力不存在。

## 100.8 Systems-Cost Blindness

只看 FLOPs，不看 communication / dispatch / imbalance。

## 100.9 Static-Expert Assumption

假設 expert semantics 永遠不隨版本與訓練變化。

## 100.10 Extractability Fallacy

局部化後直接假設可以抽離。

## 100.11 Externalization Granularity Error

把 token-level expert 直接當 API-level expert。

## 100.12 AI-Label Authority Error

把另一個 AI 的 expert 解釋文字當機械證據。

---

# 101. 十四項主要命題

## 命題 1：總容量—活躍容量分離命題

$$
\boxed{
P_{\mathrm{total}}
\gg
P_{\mathrm{active}}
}
$$

可以與高能力共存。

## 命題 2：條件智能命題

一個系統可以擁有：

$$
\mathcal C_{\mathrm{available}}
$$

而每個任務只激活：

$$
\mathcal C_{\mathrm{active}}(T).
$$

## 命題 3：稀疏激活非功能獨立命題

$$
\boxed{
\text{Sparse Activation}
\not\Rightarrow
\text{Functional Independence}.
}
$$

## 命題 4：Routing 非 Ownership 命題

$$
\boxed{
\text{Routing Correlation}
\neq
\text{Causal Capability Ownership}.
}
$$

## 命題 5：Shared Expert 非 Core 命題

$$
\boxed{
\text{Shared Expert}
\neq
\text{Resident Cognitive Core}.
}
$$

## 命題 6：Distributed Shared Capability 命題

即使：

$$
\mathcal E_S=\varnothing,
$$

仍可能：

$$
\mathcal C_{\mathrm{shared}}\neq\varnothing.
$$

## 命題 7：Fine-Grained Specialization 命題

expert specialization 可以出現在細粒度操作，而非 broad domain。

## 命題 8：Expert-Set Capability 命題

某些能力的最小因果單位可能是 expert set 或 routing path，而非單 expert。

## 命題 9：Routing Policy Confound 命題

specialization 受到 routing / balancing policy 影響。

## 命題 10：Conditional Placement 命題

不是所有低頻能力都應 externalize；高交互粒度能力可能更適合 internal conditional activation。

## 命題 11：Capability Locality Spectrum 命題

能力可能分布於：

$$
L_C\in[0,1]
$$

的局部—分散連續譜，而非二元 localized / distributed。

## 命題 12：Separability 非 Externalizability 命題

$$
\boxed{
\text{Functional Separability}
\not\Rightarrow
\text{Practical Externalizability}.
}
$$

## 命題 13：MoE Tomography 命題

MoE 的天然 routing 與 expert units 可以比 dense FFN 提供更直接的能力干預表面。

## 命題 14：MoE Bridge 命題

MoE 可以成為 Resident Cognitive Core 與 External Cognitive Experts 之間的實驗橋梁，但不是兩者等價的證明。

---

# 102. 十組可否證實驗

## 實驗 1：Routing Fingerprint Replication

對多個 task family：

$$
T_1,\ldots,T_n
$$

重複測：

$$
\rho_T(l,e).
$$

要求不同 prompt template、seed、sample 下穩定。

## 實驗 2：Single / Group Ablation

比較：

$$
I_i(T),
$$

$$
I_{\{i,j\}}(T).
$$

測 redundancy 與 synergy。

## 實驗 3：Route Forcing

改變 router choice，測：

$$
\Delta Q.
$$

## 實驗 4：Expert Substitution

移除：

$$
E_i
$$

並以：

$$
E_j
$$

替代，測：

$$
Q_{\mathrm{restore}}.
$$

## 實驗 5：Shared Expert Ablation

對有 shared expert 架構，測 cross-task degradation。

## 實驗 6：Pure Routed Counterexample

比較 pure-routed 與 shared+routed architecture，避免 shared-core 假說過度泛化。

## 實驗 7：Load-Balancing Perturbation

改 balancing scope / auxiliary loss，觀察 routing semantics 是否改變。

## 實驗 8：Top- $k$ / Expert Count Sweep

比較：

$$
(N,K).
$$

測 specialization、quality、latency、redundancy。

## 實驗 9：Path-Level Intervention

對：

$$
\pi(x)
$$

做 layer-wise path replacement，測 capability emergence depth。

## 實驗 10：Cross-Model Capability Map

在不同 MoE family 重複：

$$
\Phi_c.
$$

找 functional invariants。

---

# 103. 什麼結果會支持本文？

以下結果會支持：

1. task families 有穩定 routing fingerprints；
2. expert ablation 顯示 task-selective causal contribution；
3. group ablation 顯示可重複 synergy / redundancy；
4. expert substitution 可以恢復局部能力；
5. shared expert ablation 對多任務產生穩定共通影響；
6. pure-routed models 仍存在 distributed shared capability；
7. routing sparsity 與 expert interpretability / specialization 有穩定關係；
8. route forcing 可以改變 task-specific behavior；
9. capability maps 在版本或模型間存在功能級相似性；
10. conditional compute 在 verification-adjusted cognitive density 上優於 comparable dense baseline。

---

# 104. 什麼結果會削弱本文？

以下結果會削弱：

1. routing fingerprint 對 prompt 極端敏感且無法重複；
2. expert ablation 幾乎只有全局退化，無 task specificity；
3. experts 完全高度冗餘，無可辨識專門化；
4. load-balancing 一變，所有 expert semantics 完全消失；
5. expert-level labels 與 causal interventions 無關；
6. ability map 完全無法跨 checkpoint 重現；
7. MoE 的主要收益只來自參數容量，而沒有可利用的 conditional capability structure；
8. communication / routing overhead 長期抵消 active compute 優勢；
9. pure dense model 在等總成本下持續支配；
10. internal expert separability 對後續 externalization 沒有任何預測價值。

---

# 105. 與 Paper 03 的回饋關係

Paper 03 提出：

$$
N_R(z).
$$

Paper 04 可以提供：

$$
\boxed{
\text{conditional evidence}.
}
$$

例如能力 $c$ 跨任務都需要、shared-path dependence 高、不可替代，則：

$$
N_R(c)\uparrow.
$$

反之，如果 task-selective、expert-local、可替代、bounded failure，則：

$$
N_Q(c)\uparrow.
$$

---

# 106. 與 Paper 02 的回饋關係

Paper 02 定義：

$$
D_A,
D_{\mathrm{MoE}}.
$$

Paper 04 提供：

$$
\boxed{
\text{what active compute actually represents}.
}
$$

因此 Cognitive Density 不再只是成本比率，而開始接近：

$$
\boxed{
\text{conditional capability allocation}.
}
$$

---

# 107. 與 Paper 05 的銜接

Paper 04 的最終問題：

> 如果某些能力真的可以在模型內被條件激活，

那麼：

$$
\boxed{
\text{Why must they remain physically inside the same model?}
}
$$

但要回答這個問題，必須解決 granularity、interface、state transfer、latency、representation translation、verification 與 authority。

因此下一篇：

$$
\boxed{
\text{Externalized Mixture of Cognitive Experts}.
}
$$

---

# 108. 公開命題與未公開機械方法的邊界

本文公開：

- routing fingerprint；
- routing entropy；
- ablation；
- group ablation；
- route forcing；
- substitution；
- path analysis；
- locality / separability concepts；
- public falsification criteria。

本文不公開：

- 內部實際 expert-search heuristic；
- 高維能力投影方法；
- 私有 intervention scheduling；
- capability graph compiler；
- parameter remapping；
- latent expert extraction；
- external bridge encoding；
- reconvergence optimization。

因此：

$$
\boxed{
\text{Public Experimental Questions}
\neq
\text{Private Mechanical Pipeline}.
}
$$

---

# 109. 結論

Mixture-of-Experts 對本系列最重要的意義，不只是：

$$
\boxed{
\text{MoE saves FLOPs}.
}
$$

而是它已經在大型模型中實際建立：

$$
\boxed{
\text{Conditional Capacity}.
}
$$

也就是：

$$
\boxed{
\text{模型可以擁有遠大於單次推理所激活的能力容量。}
}
$$

這使 Resident 與 Conditionally Activated 第一次有了非常直接的神經架構參照。

但是本文也劃出明確邊界：

$$
\boxed{
\text{Expert}
\neq
\text{Human-Named Capability}.
}
$$

$$
\boxed{
\text{Routing}
\neq
\text{Ownership}.
}
$$

$$
\boxed{
\text{Shared Expert}
\neq
\text{Cognitive Core}.
}
$$

$$
\boxed{
\text{Localized Contribution}
\neq
\text{Clean Externalizability}.
}
$$

因此 MoE 真正值得研究的地方，不是急著說：

> 我們已經找到模型裡的數學腦、程式腦與歷史腦。

而是利用：

$$
\boxed{
\text{routing}
+
\text{sparsity}
+
\text{expert units}
+
\text{causal intervention}
}
$$

第一次較系統地建立：

$$
\boxed{
\text{Capability Topography}.
}
$$

如果這張能力地形最終顯示：

- 某些能力跨任務、跨 expert、跨模型都具有高中心性；
- 某些能力只在特定任務被條件激活；
- 某些能力能被替代；
- 某些能力能在更高粒度下被外部執行器重建；

那麼：

$$
\boxed{
\text{Resident}
+
\text{Conditional}
+
\text{External}
}
$$

就不再只是概念分類。

它會開始成為：

$$
\boxed{
\text{empirically grounded cognitive placement architecture}.
}
$$

因此本文最終命題是：

$$
\boxed{
\text{MoE 證明了智能的計算可以條件化；}
}
$$

而接下來真正要證明的是：

$$
\boxed{
\text{智能的能力是否也能被可靠地辨識、分離、替換與跨邊界展開。}
}
$$

---

# References

1. Fedus, W., Zoph, B., & Shazeer, N. (2022). *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*. Journal of Machine Learning Research, 23(120), 1–39.
2. Dai, D., et al. (2024). *DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models*. arXiv:2401.06066.
3. DeepSeek-AI. (2024). *DeepSeek-V3 Technical Report*. arXiv:2412.19437.
4. Qwen Team. (2025). *Qwen3: Think Deeper, Act Faster*.
5. Yang, X., et al. (2025). *Mixture of Experts Made Intrinsically Interpretable*. arXiv:2503.07639.
6. Herbst, J., Lee, J. H., & Wermter, S. (2026). *The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expert Level*. arXiv:2604.02178.
7. Falke, T., et al. (2026). *MoE Routing Testbed: Studying Expert Specialization and Routing Behavior at Small Scale*. arXiv:2604.07030.
8. Li, J. (2026). *The Evolution of Mixture-of-Experts Architectures in Large Language Models: Routing, Topology, Load Balancing, and Expert Parallelism*. arXiv:2608.08650.
9. Neo.K. & Aletheia. (2026). *當 Frontier AI 基本能力逐漸成熟：從 Scaling 轉向 Cognitive Efficiency*.
10. Neo.K. & Aletheia. (2026). *Cognitive Density Hypothesis：認知密度命題*.
11. Neo.K. & Aletheia. (2026). *Resident Cognitive Core：Mother Model 到底必須常駐什麼？*.
12. Neo.K. & Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.
13. Neo.K. & Aletheia. (2026). *子 AI 是認知器官，不是獨立 Workflow*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開命題論文。

本文公開 Conditional Intelligence 定義、MoE routing / specialization 的理論邊界、routing fingerprint、causal intervention 類型、capability locality / separability 問題與 falsification framework。

本文不公開任何未驗證或未公開的 expert-search private heuristic、capability projection algorithm、parameter-level extraction、latent bridge、expert externalization implementation 或 reconvergence training method。

因此：

$$
\boxed{
\text{MoE as Experimental Surface}
\neq
\text{Disclosure of the Private Separation Method}.
}
$$
