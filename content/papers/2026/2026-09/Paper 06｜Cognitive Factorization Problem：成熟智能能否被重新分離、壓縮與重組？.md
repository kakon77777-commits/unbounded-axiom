# Paper 06｜Cognitive Factorization Problem：成熟智能能否被重新分離、壓縮與重組？

**English Title:** *The Cognitive Factorization Problem: Can Mature Intelligence Be Decomposed, Compressed, Expanded, Linked, Reconciled, and Reconverged?*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／認知因子化、模型重構與可展開智能研究

---

## 摘要

本文提出 **Cognitive Factorization Problem（CFP，認知因子化問題）**。前五篇已逐步建立：大型模型能力成熟後的 compute-allocation 問題、Cognitive Density、Resident Cognitive Core、MoE Conditional Intelligence，以及 Externalized Mixture of Cognitive Experts。到了這一步，一個無法再迴避的技術—理論問題出現：

> **即使我們知道某些能力「理論上值得常駐」、某些能力「適合條件激活」、某些能力「適合外部展開」，我們是否真的有能力把一個已經成熟但高度糾纏的 Frontier Model 重新拆成這些部分？**

本文主張，這個問題不能被簡化成：

$$
\text{Large Model}
\rightarrow
\text{Small Model}.
$$

因為壓縮不是唯一問題。真正需要處理的是：

$$
\boxed{
\mathfrak F
=
(
D,
C,
X,
L,
R,
G
)
}
$$

其中：

- $D$：Decompose，分解；
- $C$：Compress，壓縮；
- $X$：Expand / Externalize，展開／外部化；
- $L$：Link，連結；
- $R$：Reconcile，調和；
- $G$：Converge，重新收斂。

這六個算子不是本文宣稱已完成的演算法，而是六個彼此獨立、具有不同失敗條件的研究問題。本文特別區分至少六種常被混淆的「可分離」：

$$
\boxed{
\text{Behavioral Separability}
}
$$

$$
\boxed{
\text{Representational Separability}
}
$$

$$
\boxed{
\text{Mechanistic Separability}
}
$$

$$
\boxed{
\text{Parametric Separability}
}
$$

$$
\boxed{
\text{Interface Separability}
}
$$

$$
\boxed{
\text{Operational Separability}.
}
$$

一項能力可以在行為上容易描述，卻在神經機制上高度分散；可以在 Sparse Autoencoder feature 空間中得到較清楚表示，卻無法乾淨刪除或搬移；可以被 causal tracing 定位，卻不代表該位置最適合 editing；可以被獨立 expert 模組近似，卻在重新組合後失去跨領域泛化。因此：

$$
\boxed{
\text{Interpretability}
\neq
\text{Factorization}
\neq
\text{Extractability}
\neq
\text{Recomposability}.
}
$$

本文利用現有研究建立問題邊界。Sparse Autoencoder 與 sparse dictionary learning 顯示，superposition 中的特徵可以在一定程度上被稀疏化與解釋，但 feature absorption、dead features、跨層依賴與表示非唯一性仍然存在；knowledge localization / editing 研究顯示「定位某個 factual behavior 的因果位置」與「在哪裡修改最有效」沒有簡單等價；MQUAKE 顯示單點 factual edit 即使能被 recall，也可能無法正確傳播到多跳衍生知識；BAR、Branch-Train-MiX、BTS 與 model merging 類工作則證明能力模組化、局部更新與重組可以在某些條件下成立，但同時暴露 catastrophic forgetting、interference、alignment 與 merge compatibility 問題。

本文因此把「認知因子化」定義為：

$$
\boxed{
F
\xrightarrow{D}
\mathcal Z
\xrightarrow{C}
K_C
}
$$

以及執行時：

$$
\boxed{
K_C
+
\mathcal X
+
\mathcal M
\xrightarrow{X,L}
Z_T
\xrightarrow{R}
O_T
\xrightarrow{G}
K_C'
}
$$

其中 $F$ 是成熟 Frontier Intelligence； $\mathcal Z$ 是候選能力／表示／機制集合； $K_C$ 是壓縮後的 Cognition-Dense Core； $\mathcal X$ 是外部 expert / tool / knowledge pool； $Z_T$ 是任務展開狀態； $O_T$ 是任務輸出； $K_C'$ 是經過證據與驗證後可能更新的 resident core。

本文進一步提出：認知因子化的目標不是最大化 parameter reduction，而是最大化 **functional preservation under architectural redistribution**。理想上，某些表層知識、低頻專門能力與快速變動能力可以被 externalize，而 interpretation、epistemic control、meta-cognition、verification selection、capability boundary modeling 與 minimum sufficient world basis 被保留或重新編譯至 resident core。但本文不公開任何私人 weight-level extraction、capability projection、latent bridge、parameter remapping 或 reconvergence 方法。

本文提出十六項主要命題、十四類失敗模式與十二組可否證實驗。若未來實驗顯示：高階推理與元認知不可避免地依賴大規模表層知識；能力在不同模型中無法形成穩定、可重用的功能因子；任何顯著壓縮都導致不可恢復的 generalization loss；externalized capability 無法以可接受 interface cost 接回核心；或者重新收斂後系統仍持續低於 monolithic frontier baseline，則 Cognitive Factorization 作為通用架構路線應被限制甚至拒絕。

本文的核心問題不是：

> **我們能不能找到哪些參數是「八卦」、哪些參數是「推理」？**

這種分法過度簡化。

真正的問題是：

$$
\boxed{
\text{Can intelligence be reorganized by function without destroying the relations that made it intelligent?}
}
$$

也就是：

> **成熟智能能否在不失去其關係結構、泛化能力與元認知控制的情況下，被重新因子化成常駐核心、條件能力與外部能力？**

**關鍵詞：** Cognitive Factorization、Decomposition、Compression、Externalization、Linking、Reconciliation、Reconvergence、Sparse Autoencoder、Knowledge Editing、Model Merging、Mother AI、Cognitive Kernel

---

# 0. 研究定位

目前系列已建立：

$$
\boxed{
\mathcal C
=
\mathcal C_R
\cup
\mathcal C_Q
\cup
\mathcal C_X.
}
$$

其中：

- $\mathcal C_R$：Resident；
- $\mathcal C_Q$：Conditional；
- $\mathcal C_X$：External。

但這仍然只是一個：

$$
\boxed{
\text{placement theory}.
}
$$

尚未回答：

> 現有成熟模型裡的能力是否真的可以按照這個分類被重新組織？

Paper 06 專門處理這個缺口。

---

# 1. 從「模型壓縮」到「認知因子化」

傳統壓縮可以寫成：

$$
F
\rightarrow
F'.
$$

目標通常是：

$$
P(F')<P(F),
$$

同時：

$$
Q(F')\approx Q(F).
$$

但 Cognitive Factorization 的目標不同。

我們允許：

$$
Q_K(F')<Q_K(F)
$$

某些表層知識覆蓋下降，

只要：

$$
Q_C(F')\approx Q_C(F)
$$

核心認知保持，

並且可透過：

$$
\mathcal X
$$

重新展開缺失能力。

因此：

$$
\boxed{
\text{Compression}
\neq
\text{Factorization}.
}
$$

---

# 2. 蒸餾也不是完整答案

Knowledge Distillation：

$$
f_S(x)
\approx
f_T(x).
$$

其核心通常是：

> 讓 student 模仿 teacher 的 output distribution、hidden states 或 task behavior。

但本文真正問：

> 哪些 teacher 能力值得被保留？

> 哪些能力可以故意不保留？

> 哪些能力應被改成 external dependency？

因此：

$$
\boxed{
\text{Teacher Imitation}
\neq
\text{Functional Allocation}.
}
$$

---

# 3. Pruning 也不是完整答案

Pruning 常尋找：

$$
\theta_i
$$

的重要性。

再移除：

$$
\theta_i\approx0
$$

或低 saliency parameters。

但：

$$
\boxed{
\text{Parameter Importance}
\neq
\text{Cognitive Role}.
}
$$

一個低 magnitude 參數也可能參與關鍵關係。

一個高 magnitude 參數也不等於 high-level reasoning operator。

---

# 4. Cognitive Factorization 的真正對象

本文不先假設：

$$
\boxed{
\text{factor}
=
\text{parameter subset}.
}
$$

Factor 可以是：

- behavior；
- feature；
- representation subspace；
- circuit；
- expert；
- routing path；
- adapter；
- learned operator；
- cognitive operation；
- external capability contract。

因此：

$$
\boxed{
\mathcal Z
=
\{
z_1,z_2,\ldots,z_n
\}
}
$$

是一個多尺度候選因子集合。

---

# 5. 六種 Separability

## 5.1 Behavioral Separability

能力：

$$
c
$$

在行為上可以單獨描述與測量。

例如：

$$
\mathsf{Translate},
\quad
\mathsf{Compile},
\quad
\mathsf{UnknownDetect}.
$$

---

## 5.2 Representational Separability

存在表示空間：

$$
Z
$$

使某能力具有較穩定方向、feature 或 cluster。

---

## 5.3 Mechanistic Separability

模型內存在某些因果機制：

$$
M_c
$$

對能力 $c$ 有可辨識貢獻。

---

## 5.4 Parametric Separability

存在權重子集：

$$
\Theta_c
$$

可以被修改、移除或獨立訓練，而不嚴重破壞其他能力。

---

## 5.5 Interface Separability

能力可以透過明確：

$$
I_c\rightarrow O_c
$$

接口被替換。

---

## 5.6 Operational Separability

能力可以在實際系統中被：

- routed；
- executed；
- verified；
- replaced；

並且總成本可接受。

---

# 6. 六種分離不等價

可能：

$$
\text{Behavioral}=1,
$$

但：

$$
\text{Parametric}\approx0.
$$

也可能：

$$
\text{Representational}\uparrow,
$$

但：

$$
\text{Operational}\downarrow.
$$

因此：

$$
\boxed{
\text{one successful interpretation result}
\not\Rightarrow
\text{factorization success}.
}
$$

---

# 7. Sparse Autoencoder 提供一個候選入口

LLM representations 存在：

$$
\boxed{
\text{superposition}.
}
$$

Sparse Autoencoder 嘗試把：

$$
h
$$

表示成：

$$
\boxed{
h
\approx
W_d z,
}
$$

其中：

$$
z
$$

是稀疏 feature activation。

這提供：

$$
\boxed{
\text{feature-level disentanglement candidate}.
}
$$

---

# 8. SAE 的價值

如果一個 feature：

$$
z_i
$$

跨多 prompt 具有穩定語義，

則：

$$
\boxed{
\text{representation factor}
}
$$

可能成立。

它比直接把 neuron 當語義單位更合理。

---

# 9. 但 SAE 不是能力拆解器

SAE 的 feature 可以：

- dead；
- absorbed；
- duplicated；
- split；
- merge；
- layer-specific。

因此：

$$
\boxed{
\text{Sparse Feature}
\neq
\text{Complete Cognitive Capability}.
}
$$

---

# 10. Feature Absorption

如果真正概念：

$$
c
$$

被另一更高頻 feature 吸收，

則：

$$
z_c
$$

可能不存在清楚單位。

這表示：

$$
\boxed{
\text{disentanglement method}
}
$$

本身會影響我們看到的「因子」。

---

# 11. Feature Non-Uniqueness

可能存在：

$$
Z_1
$$

與：

$$
Z_2
$$

兩套稀疏 dictionary，

都能良好重建：

$$
h.
$$

因此：

$$
\boxed{
\text{representation factorization}
}
$$

可能不是唯一。

---

# 12. RouteSAE 顯示跨層問題

如果能力跨：

$$
l_1,\ldots,l_k
$$

多層展開，

單層 SAE 可能看不到完整結構。

因此：

$$
\boxed{
\text{capability}
\neq
\text{single-layer feature}.
}
$$

---

# 13. Mechanistic Interpretability 不等於可抽離

假設 causal tracing 找到：

$$
M_c.
$$

仍然只能說：

$$
\boxed{
M_c
\text{ contributes causally}.
}
$$

不能直接推出：

$$
\boxed{
M_c
\text{ can be extracted cleanly}.
}
$$

---

# 14. Localization vs Editing 的直接反例

現有研究已顯示：

> causal localization 所指向的 layer，不一定是 knowledge editing 最有效的位置。

因此：

$$
\boxed{
\text{Where behavior is localized}
\neq
\text{Where behavior is easiest to change}.
}
$$

---

# 15. 這對 Factorization 很重要

如果：

$$
\text{localize}(c)=L_i
$$

但：

$$
\text{edit}(c)
$$

最好在：

$$
L_j,
$$

那麼：

$$
\boxed{
\text{causal locus}
}
$$

與：

$$
\boxed{
\text{control locus}
}
$$

不同。

---

# 16. Control Surface

本文提出：

$$
\boxed{
\mathcal S_c^{control}
}
$$

表示最適合控制能力 $c$ 的介面。

它不必等於：

$$
\mathcal S_c^{causal}.
$$

---

# 17. 知識 Editing 也暴露關係傳播問題

若把 factual belief：

$$
a\rightarrow b
$$

改掉，

真正系統還需要更新：

$$
b\rightarrow c,
$$

$$
c\rightarrow d.
$$

如果只改 recall：

$$
Q_{\mathrm{local}}\uparrow
$$

但 multi-hop consequence 不更新，

就不是完整知識重構。

---

# 18. MQUAKE 的意義

MQUAKE 顯示：

$$
\boxed{
\text{local edit success}
\neq
\text{relational consistency}.
}
$$

這對 Cognitive Factorization 是非常重要的反例。

---

# 19. Cognitive Factor 是關係性物件

本文因此不把 factor 定義為：

$$
z_i.
$$

更合理：

$$
\boxed{
F_i
=
(
z_i,
R_i,
C_i,
D_i
)
}
$$

其中：

- $z_i$：representation / mechanism；
- $R_i$：relations；
- $C_i$：constraints；
- $D_i$：dependencies。

---

# 20. 分離能力不能切斷必要關係

如果：

$$
F_i
$$

被 externalize，

其必要 relation：

$$
R_{ij}
$$

也必須保持。

否則：

$$
\boxed{
\text{factor extraction}
\rightarrow
\text{semantic amputation}.
}
$$

---

# 21. Model Merging 提供另一個觀察窗

若不同 task models：

$$
M_1,M_2
$$

可以 merge 成：

$$
M_{12},
$$

表示某些能力可能具有：

$$
\boxed{
\text{parameter-space composability}.
}
$$

---

# 22. Task Vectors

對 base model：

$$
\theta_0
$$

與 finetuned：

$$
\theta_t,
$$

task vector：

$$
\boxed{
\tau_t
=
\theta_t-\theta_0.
}
$$

若：

$$
\theta_0+\tau_1+\tau_2
$$

能保持兩項能力，

表示某種局部近似線性 composability。

---

# 23. 但 Task Arithmetic 不是認知代數

如果 task vectors 可以相加，

不能推出：

$$
\boxed{
\text{all cognition is linearly composable}.
}
$$

模型 parameter space：

- nonlinear；
- symmetry-rich；
- representation-dependent。

因此 task arithmetic 只是有限條件下的證據。

---

# 24. Model Merging 的干擾

如果：

$$
\tau_1
$$

與：

$$
\tau_2
$$

衝突，

則：

$$
Q_{12}<Q_1,Q_2.
$$

這就是：

$$
\boxed{
\text{factor interference}.
}
$$

---

# 25. BAR 提供 Modular Post-Training 證據

BAR 能把 math、code、tool-use、safety 等 domain experts 分開 post-train，再透過 MoE router 組合。

這支持：

$$
\boxed{
\text{capability-local update}
}
$$

在某些結構下可行。

---

# 26. BAR 也提供 Forgetting 對照

Monolithic continued post-training 可能：

$$
\text{new capability}\uparrow
$$

同時：

$$
\text{old capability}\downarrow.
$$

這是 catastrophic forgetting。

分離 expert 可以降低：

$$
\boxed{
\text{cross-capability interference}.
}
$$

---

# 27. 因此 Modularization 有價值

若能力更新可以局部化：

$$
\boxed{
\Delta c_i
}
$$

不必重做：

$$
\forall j,\Delta c_j,
$$

則：

$$
\boxed{
\text{maintenance cost}
\downarrow.
}
$$

---

# 28. 但 Modular Training 不等於 Mature Model Factorization

BAR 的 experts 是設計時／訓練時分支形成。

本文更難的問題是：

> 一個已經訓練完成的 monolithic frontier model，能不能事後重新因子化？

因此：

$$
\boxed{
\text{Native Modularity}
\neq
\text{Post-Hoc Factorization}.
}
$$

---

# 29. Cognitive Factorization 的兩條路

## 路線 A：Reconstructive

$$
\boxed{
F_{\mathrm{mature}}
\rightarrow
K_C+\mathcal C_Q+\mathcal C_X.
}
$$

先有成熟智能，

再重構。

## 路線 B：Native

$$
\boxed{
\text{train}
(
K_C,
\mathcal C_Q,
\mathcal C_X
)
}
$$

一開始就以 modular cognitive placement 為目標。

---

# 30. 第一代更可能是 Reconstructive

原因：

$$
\boxed{
\text{we already possess strong mature teachers}.
}
$$

可以先觀察它們：

- capability；
- failure；
- representation；
- routing；
- intervention。

再反推：

$$
K_C.
$$

---

# 31. Native Training 需要更強理論

如果一開始就訓：

$$
K_C,
$$

問題是：

> 我們是否知道哪些能力真正必要？

目前答案：

$$
\boxed{
\text{not sufficiently}.
}
$$

因此先研究 mature models 更務實。

---

# 32. 六算子總覽

本文正式提出：

$$
\boxed{
\mathfrak F
=
(
D,C,X,L,R,G
).
}
$$

---

# 33. $D$：Decompose

Decompose：

$$
\boxed{
D(F)
\rightarrow
\mathcal Z.
}
$$

目標：

> 找到可被研究的能力因子候選。

不是立刻切權重。

---

# 34. Decomposition 可以多尺度

$$
\mathcal Z
=
\mathcal Z_B
\cup
\mathcal Z_R
\cup
\mathcal Z_M
\cup
\mathcal Z_P
\cup
\mathcal Z_O.
$$

其中：

- behavior；
- representation；
- mechanism；
- parameter；
- operation。

---

# 35. Decomposition 的第一個成功條件

候選 factor：

$$
z_i
$$

至少需要：

$$
\boxed{
\text{repeatability}.
}
$$

也就是跨：

- prompt；
- sample；
- seed；

仍然有穩定訊號。

---

# 36. 第二個條件：Specificity

$$
z_i
$$

對某能力：

$$
c
$$

比其他能力有更高辨識力。

---

# 37. 第三個條件：Causality

干預：

$$
z_i
$$

應對：

$$
Q(c)
$$

產生可重複影響。

---

# 38. 第四個條件：Boundary

必須知道：

$$
\boxed{
\text{where the factor stops}.
}
$$

如果：

$$
z_i
$$

影響所有能力，

它可能是 shared substrate，

不是 specialized factor。

---

# 39. $C$：Compress

Compression：

$$
\boxed{
C(
\mathcal Z_R
)
\rightarrow
K_C.
}
$$

其中：

$$
\mathcal Z_R
$$

是高 resident-value cognition。

---

# 40. Compression 目標不是最小參數

真正目標：

$$
\boxed{
\max
\frac{
Q_{\mathrm{core}}
}{
C_{\mathrm{resident}}
}
}
$$

subject to：

$$
Q_{\mathrm{generalization}}
\ge
\theta_G.
$$

---

# 41. 需要保留 Generalization

如果壓縮後：

$$
Q_{\mathrm{benchmark}}\approx Q_F
$$

但：

$$
Q_{\mathrm{novel}}\downarrow\downarrow,
$$

則：

$$
\boxed{
\text{compression failed cognitively}.
}
$$

---

# 42. Counterfactual Tasks 很重要

標準 benchmark 可能只是：

$$
\text{reciting}.
$$

Counterfactual variants 可以測：

$$
\boxed{
\text{procedure transfer}.
}
$$

因此適合判斷：

> 壓縮保留的是抽象能力，還是 memorized surface behavior？

---

# 43. Compression 不能只蒸餾答案

如果只 imitation：

$$
y_T\rightarrow y_S,
$$

可能保留：

$$
\text{surface behavior}
$$

但失去：

$$
\text{reasoning flexibility}.
$$

因此需要：

$$
\boxed{
\text{structural preservation tests}.
}
$$

---

# 44. $X$：Expand / Externalize

Expansion：

$$
\boxed{
X(
K_C,
T,
\mathcal X
)
\rightarrow
Z_T.
}
$$

它把：

$$
\text{compressed core}
$$

與：

$$
\text{external capability}
$$

組成任務暫時狀態。

---

# 45. Expansion 不是 Retrieval

Retrieval：

$$
q\rightarrow documents.
$$

Expansion：

$$
\boxed{
(
K_C,
evidence,
expert,
tool,
state
)
\rightarrow
Z_T.
}
$$

它是一個：

$$
\boxed{
\text{temporary cognition construction}.
}
$$

---

# 46. Expansion 需要任務條件化

同一 core：

$$
K_C
$$

對：

$$
T_1
$$

與：

$$
T_2
$$

展開：

$$
Z_{T_1}\neq Z_{T_2}.
$$

因此：

$$
\boxed{
\text{cognition becomes dynamically instantiated}.
}
$$

---

# 47. $L$：Link

Link：

$$
\boxed{
L:
(
K_C,
X_i
)
\rightarrow
\mathcal I_i.
}
$$

其中：

$$
\mathcal I_i
$$

是可用 interface。

---

# 48. Linking 是整個架構的命門

如果 core 知道：

> 我需要數學能力。

但無法把：

$$
state_M
$$

轉成 external expert 可理解的：

$$
C_i,
$$

externalization 就失敗。

---

# 49. Linking 不只是文字 Prompt

可能的 link：

- text；
- JSON；
- graph；
- embedding；
- symbolic state；
- program；
- latent packet。

因此：

$$
\boxed{
\text{Interface Representation}
}
$$

本身是研究變數。

---

# 50. Link Fidelity

定義：

$$
\boxed{
F_L
=
\frac{
Q(
X_i\mid\mathcal I_i
)
}{
Q(
X_i\mid\mathcal I_i^\ast
)
}.
}
$$

若：

$$
F_L\ll1,
$$

表示 interface 丟失關鍵認知狀態。

---

# 51. $R$：Reconcile

Reconcile：

$$
\boxed{
R(
K_C,
O_X,
E
)
\rightarrow
O^\ast.
}
$$

其中：

- $O_X$：external outputs；
- $E$：evidence。

---

# 52. Reconcile 處理衝突

如果：

$$
X_1(T)\neq X_2(T),
$$

不能只：

$$
\operatorname{Vote}.
$$

需要比較：

- source；
- assumptions；
- task fit；
- verifier；
- version；
- evidence。

---

# 53. Reconcile 與 Knowledge Editing 的關係

如果 external evidence：

$$
e
$$

與 resident belief：

$$
k
$$

衝突，

系統不應：

$$
\boxed{
\text{immediately overwrite }k.
}
$$

而應建立：

$$
\boxed{
\text{contested state}.
}
$$

---

# 54. $G$：Converge

Converge：

$$
\boxed{
G(
K_C,
\Delta_T,
E
)
\rightarrow
K_C'.
}
$$

其中：

$$
\Delta_T
$$

是任務中產生的可重用增量。

---

# 55. Converge 不是把所有任務資訊塞回 Core

如果每次：

$$
Z_T
\rightarrow
K_C,
$$

則：

$$
K_C
$$

很快重新膨脹。

因此需要：

$$
\boxed{
\text{Selective Consolidation}.
}
$$

---

# 56. 哪些東西值得 Converge？

候選包括：

- new reasoning operator；
- stable capability boundary；
- reusable verifier policy；
- high-frequency relation；
- corrected core assumption。

不一定包括：

- raw documents；
- one-off facts；
- temporary API response。

---

# 57. Core Update Gate

概念：

$$
\boxed{
K_C'
=
\operatorname{Commit}
(
K_C,
\Delta,
V,
R
).
}
$$

需要：

$$
V(\Delta)\ge\theta_V,
$$

$$
\operatorname{Regression}(\Delta)\le\theta_R.
$$

---

# 58. 六算子不是線性流水線

實際可能：

$$
D
\rightarrow
C
\rightarrow
L
\rightarrow
X
\rightarrow
R
\rightarrow
G
$$

但也可能：

$$
R
\rightarrow
D
$$

因為新的衝突讓系統重新分解能力。

因此：

$$
\boxed{
\mathfrak F
}
$$

應被視為 operator graph，

不是固定 sequence。

---

# 59. Factorization Graph

定義：

$$
\boxed{
G_F
=
(
V_F,
E_F
)
}
$$

其中：

$$
V_F
=
\{
D,C,X,L,R,G
\}.
$$

邊表示依賴與反饋。

---

# 60. Factorization Quality

定義：

$$
\boxed{
Q_F
=
f(
P_{\mathrm{preserve}},
S_{\mathrm{sep}},
F_L,
Q_R,
Q_G,
C_{\mathrm{total}}
).
}
$$

其中：

- $P_{\mathrm{preserve}}$：能力保留；
- $S_{\mathrm{sep}}$：可分性；
- $F_L$：link fidelity；
- $Q_R$：reconciliation quality；
- $Q_G$：convergence stability。

---

# 61. Compression Ratio 不是 Factorization Quality

即使：

$$
\frac{
P_F
}{
P_C
}
=10,
$$

如果：

$$
Q_R\downarrow,
$$

$$
Q_G\downarrow,
$$

整體仍然失敗。

---

# 62. Factorization 必須看 System Utility

最終：

$$
\boxed{
U_{\mathrm{fact}}
=
Q_{\mathrm{verified}}
-
\lambda C_{\mathrm{system}}
-
\mu R_{\mathrm{integration}}.
}
$$

而不是：

$$
\boxed{
\text{model bytes saved}.
}
$$

---

# 63. Cognitive Density 是 Factorization 的目標函數之一

Paper 02 定義：

$$
D_M.
$$

理想 Factorization：

$$
\boxed{
D_M^{\mathrm{factorized}}
>
D_M^{\mathrm{monolithic}}.
}
$$

---

# 64. Resident Core 必須保持 Epistemic Sovereignty

如果 factorized core：

$$
K_C
$$

無法驗證外部 experts，

那它只是：

$$
\boxed{
\text{highly compressed router}.
}
$$

因此 Paper 03 的：

$$
B_E,
B_M,
B_G
$$

必須保留。

---

# 65. Externalization 可能降低 Knowledge Update Cost

快速變動 facts：

$$
k(t)
$$

如果 resident：

$$
\text{retraining cost}\uparrow.
$$

如果 external：

$$
\text{update memory / source}.
$$

因此：

$$
\boxed{
\text{surface externalization}
}
$$

可能降低版本成本。

---

# 66. MQUAKE 的另一個啟示

外部 memory 可以避免直接 weight edit 的某些 propagation 問題。

但：

$$
\boxed{
\text{external memory}
}
$$

仍需要：

- retrieval；
- decomposition；
- self-check。

這再一次說明：

$$
\boxed{
\text{core cognition remains necessary}.
}
$$

---

# 67. Model Merging 與 Reconvergence

如果兩個 factorized experts：

$$
E_1,E_2
$$

要重新合併：

$$
E_{12},
$$

可能使用：

- parameter merge；
- router；
- ensemble；
- adapter composition；
- external coordination。

因此：

$$
\boxed{
\text{Reconvergence}
}
$$

可以有多種物理形式。

---

# 68. Logical Reconvergence

不一定要：

$$
\theta_1+\theta_2.
$$

也可以：

$$
\boxed{
\text{shared system state}
}
$$

讓多個 experts 表現成一個 intelligence。

這是本文非常重要的擴張。

---

# 69. One Intelligence 不必 One Parameter Tensor

如果：

$$
M
+
X_1+\cdots+X_n
$$

共享：

- goals；
- state；
- epistemic rules；
- verification；
- memory；

則：

$$
\boxed{
\text{system continuity}
}
$$

不必來自單一 tensor。

---

# 70. 但 Continuity 不能只是 UI Illusion

如果每個 component：

- goals 不一致；
- memory 不一致；
- policy 不一致；

只是前端看起來同一聊天介面，

則：

$$
\boxed{
\text{not one coherent cognitive system}.
}
$$

---

# 71. Reconvergence Consistency

定義：

$$
\boxed{
C_G
=
\operatorname{Consistency}
(
G_t,
M_t,
P_t,
E_t
).
}
$$

其中：

- goals；
- memory；
- policy；
- evidence。

---

# 72. Dynamic Factorization

能力 placement：

$$
p_t(c)
\in
\{
R,Q,X
\}.
$$

未來：

$$
\boxed{
p_{t+1}(c)
\neq
p_t(c)
}
$$

可以成立。

---

# 73. 因此 Factorization 是動態的

一個能力今天：

$$
X
$$

外部，

明天因高頻使用變成：

$$
Q,
$$

最後：

$$
R.
$$

反之亦然。

---

# 74. Capability Lifecycle

$$
\boxed{
\text{Discover}
\rightarrow
\text{Probe}
\rightarrow
\text{Externalize}
\rightarrow
\text{Measure}
\rightarrow
\text{Internalize / Retire}.
}
$$

這是 placement lifecycle。

---

# 75. Factorization 也需要版本化

每次：

$$
\mathfrak F_t
\rightarrow
\mathfrak F_{t+1}
$$

應保存：

- evidence；
- reason；
- regression；
- cost；
- rollback。

---

# 76. Cannot Assume Clean Ontology

我們可能把能力分類成：

- reasoning；
- memory；
- planning；

但模型內部不一定遵守這些 human categories。

因此：

$$
\boxed{
\text{human ontology}
\neq
\text{model factorization}.
}
$$

---

# 77. Factor Discovery 必須允許 Unexpected Factors

可能出現：

$$
z_i
$$

無法用現有詞彙簡單描述。

不能因為：

> 不像人類能力分類

就丟掉。

---

# 78. Parallel Hypothesis Expansion

因此研究應允許：

$$
H_1,H_2,\ldots,H_n
$$

多個能力解釋並行。

不要早期：

$$
\boxed{
H_1\rightarrow\text{canonical truth}.
}
$$

---

# 79. Mechanical Evidence 與 AI Interpretation 分離

機械層保存：

- activation；
- routing；
- ablation；
- loss delta；
- edit delta；
- merge delta；
- hashes。

AI 層產生：

- labels；
- hypotheses；
- explanations。

因此：

$$
\boxed{
\text{Interpretation}
\neq
\text{Evidence}.
}
$$

---

# 80. Multi-AI Parallel Research

不同 AI 可以分別：

- interpret representation；
- search counterexamples；
- analyze causal effects；
- inspect systems cost；
- critique factor labels。

最後才：

$$
\boxed{
\operatorname{Synthesize}.
}
$$

---

# 81. 這也是 Factorization 自身的測試

如果不同 AI：

$$
A_1,\ldots,A_n
$$

對同一 mechanism 形成不同分解，

就表示：

$$
\boxed{
\text{factor ontology uncertain}.
}
$$

這個 disagreement 本身是 evidence。

---

# 82. Factor Stability

定義：

$$
\boxed{
S_F(z)
=
\operatorname{Stability}
(
z
\mid
prompt,
dataset,
checkpoint,
architecture
).
}
$$

越穩定，

越適合作為 reusable factor。

---

# 83. Cross-Architecture Factor

最有價值的可能不是：

$$
\text{same neurons}.
$$

而是：

$$
\boxed{
\text{same functional factor}
}
$$

在不同模型由不同機制實現。

---

# 84. Functional Homology

定義：

$$
\boxed{
z_i^{(A)}
\sim_F
z_j^{(B)}
}
$$

若兩者在：

- task effect；
- failure；
- interface；
- substitution；

上功能同構。

這可以支援跨模型 external expert taxonomy。

---

# 85. Factor Substitution

若：

$$
z_i
$$

移除後，

外部：

$$
X_j
$$

可以恢復：

$$
Q,
$$

則：

$$
\boxed{
X_j
}
$$

是 functional substitute candidate。

---

# 86. Restoration Score

$$
\boxed{
R_S
=
\frac{
Q(-z_i+X_j)-Q(-z_i)
}{
Q-Q(-z_i)
}.
}
$$

若：

$$
R_S\rightarrow1,
$$

表示恢復大部分缺失功能。

---

# 87. Restoration 不代表相同機制

$$
X_j
$$

可以用完全不同算法完成相同功能。

因此：

$$
\boxed{
\text{functional substitution}
\neq
\text{mechanistic identity}.
}
$$

---

# 88. 這正是 Externalization 所需要的

Externalization 不要求：

> 把 expert 原封不動搬出去。

只要求：

$$
\boxed{
\text{system-level function remains available}.
}
$$

---

# 89. Factorization 與 Knowledge Externalization

對表層知識：

$$
k
$$

externalization 更容易，

因為：

$$
\text{retrieve}(k)
$$

常有明確 interface。

---

# 90. Factorization 與 Reasoning Externalization

對 reasoning operator：

$$
r
$$

更困難，

因為它可能：

- high frequency；
- low latency；
- deeply integrated；
- hard to verify。

因此：

$$
N_R(r)\uparrow
$$

通常較高。

---

# 91. Meta-Cognition 更難外置

如果：

$$
\mathsf{UnknownDetection}
$$

都要 externalize，

Mother AI 要先知道：

> 是否需要問外部 unknown detector。

形成：

$$
\boxed{
\text{meta-recursion}.
}
$$

因此某些 meta primitives 必須 resident。

---

# 92. Factorization 的核心不是「越模組化越好」

過度模組化：

$$
N_{\mathrm{module}}\uparrow
$$

會增加：

$$
C_{\mathrm{interface}}
+
C_{\mathrm{coordination}}.
$$

因此存在：

$$
\boxed{
\text{optimal modularity}.
}
$$

---

# 93. Modularity Frontier

$$
\boxed{
M^\ast
=
\arg\max_M
\frac{
Q_{\mathrm{verified}}
}{
C_{\mathrm{compute}}
+
C_{\mathrm{interface}}
+
C_{\mathrm{coord}}
}.
}
$$

---

# 94. Coarse Factors vs Fine Factors

因子太粗：

$$
\text{externalization gain}\downarrow.
$$

因子太細：

$$
\text{interface cost}\uparrow.
$$

因此：

$$
\boxed{
\text{factor granularity crossover}.
}
$$

---

# 95. Factor Boundary 要靠實驗，不靠命名

若一個 factor：

$$
z_i
$$

在不同 task：

$$
T_1,T_2
$$

都必要，

就可能不是 task-specific。

反之：

$$
z_j
$$

只在：

$$
T_3
$$

必要，

較像 conditional factor。

---

# 96. Factor Dependency Graph

定義：

$$
\boxed{
G_Z
=
(
\mathcal Z,
E_Z,
\omega_Z
).
}
$$

邊：

$$
z_i\rightarrow z_j
$$

表示 dependency。

---

# 97. Factorization 不能忽略圖結構

如果只保留：

$$
\mathcal Z
$$

節點，

不保留：

$$
E_Z,
$$

則：

$$
\boxed{
\text{bag of capabilities}
\neq
\text{intelligence}.
}
$$

---

# 98. Intelligence 可能主要存在關係中

一個很重要的命題：

$$
\boxed{
\text{Intelligence}
\not\subseteq
\text{individual factors only}.
}
$$

能力可能來自：

$$
\boxed{
\text{relations among factors}.
}
$$

---

# 99. 因此「拆乾淨」可能本身是錯誤目標

如果所有關係都切斷，

得到的不是：

$$
\text{modular intelligence},
$$

而是：

$$
\boxed{
\text{dead parts}.
}
$$

---

# 100. Better Goal: Controlled Coupling

因此真正目標可能是：

$$
\boxed{
\text{Controlled Coupling}
}
$$

而不是：

$$
\boxed{
\text{Complete Independence}.
}
$$

---

# 101. Factor Interface 是關係的可控化

如果：

$$
z_i
$$

與：

$$
z_j
$$

必須互動，

就建立：

$$
\boxed{
I_{ij}
}
$$

明確 interface。

因此 modularity 的本質：

$$
\boxed{
\text{make coupling explicit}.
}
$$

---

# 102. Cognitive Compiler

概念上：

$$
\boxed{
\mathsf{Compile}
:
\text{implicit coupling}
\rightarrow
\text{explicit interface}.
}
$$

這是未來很重要的方向。

本文不公開實作。

---

# 103. Factorization 的十四類失敗模式

## 103.1 Behavioral-Mechanistic Confusion

行為可描述就誤認機制可分離。

## 103.2 Interpretability-Extractability Confusion

feature 可解釋就誤認可抽離。

## 103.3 Localization-Control Confusion

因果定位位置被誤當最佳控制位置。

## 103.4 Local Edit Propagation Failure

局部修改沒有更新衍生關係。

## 103.5 Catastrophic Forgetting

新因子導致舊能力崩潰。

## 103.6 Factor Interference

合併 factors 後互相破壞。

## 103.7 Overcompression

核心過小，generalization 崩潰。

## 103.8 Surface Memorization Preservation

保留 benchmark behavior，卻丟掉抽象能力。

## 103.9 Interface Loss

外部 link 丟失關鍵 latent state。

## 103.10 Reconvergence Conflict

external results 無法一致整合。

## 103.11 Core Re-Inflation

Converge 把所有資訊重新塞回 core。

## 103.12 Ontology Lock-In

早期錯誤 factor labels 限制後續研究。

## 103.13 Excessive Modularity

module 數過多，coordination cost 爆炸。

## 103.14 Relation Amputation

切出 factors 時破壞真正重要的跨 factor 關係。

---

# 104. 十六項主要命題

## 命題 1：Factorization 非 Compression 命題

$$
\boxed{
\text{Cognitive Factorization}
\neq
\text{Model Compression}.
}
$$

## 命題 2：Separability 多層命題

Behavioral、Representational、Mechanistic、Parametric、Interface、Operational separability 不等價。

## 命題 3：Interpretability 非 Extractability 命題

$$
\boxed{
\text{Interpretability}
\not\Rightarrow
\text{Extractability}.
}
$$

## 命題 4：Localization 非 Control 命題

$$
\boxed{
\text{Causal Locus}
\neq
\text{Optimal Control Surface}.
}
$$

## 命題 5：Local Edit 非 Relational Update 命題

局部 factual edit 成功不能保證衍生關係一致。

## 命題 6：Post-Hoc Factorization 難於 Native Modularity 命題

成熟 monolithic model 的事後因子化比設計時 modular training 更困難。

## 命題 7：Functional Preservation 命題

Factorization 的主要目標是保留 cognition，不是最大化 parameter reduction。

## 命題 8：Externalization Requires Linking 命題

沒有高 fidelity interface，external capability 不構成可用能力。

## 命題 9：Reconciliation Required 命題

多 expert outputs 需要 evidence-aware reconciliation。

## 命題 10：Selective Convergence 命題

任務結果只有可重用、高證據價值部分才應進 resident core。

## 命題 11：Factor Graph 命題

智能能力不只存在因子本身，也存在因子關係中。

## 命題 12：Controlled Coupling 命題

最佳 modularity 可能不是完全獨立，而是可治理的顯式耦合。

## 命題 13：Dynamic Placement 命題

能力可以在 Resident、Conditional、External 間動態遷移。

## 命題 14：Functional Homology 命題

不同模型可以由不同機制實現功能同構的 cognitive factors。

## 命題 15：Restoration 命題

若外部 factor 可恢復移除能力的大部分 verified utility，則 externalization 具有實證支持。

## 命題 16：System-Level Reconvergence 命題

One coherent intelligence 不必要求所有能力重新合併成 one parameter tensor。

---

# 105. 十二組可否證實驗

## 實驗 1：Behavior vs Mechanism

建立行為清楚的 task family，測是否存在穩定 mechanistic factor。

## 實驗 2：SAE Feature Replication

跨 seed、dictionary size、layer 比較 factor stability：

$$
S_F.
$$

## 實驗 3：Localization vs Editing

比較 causal locus 與最佳 editing location 的一致性。

## 實驗 4：Local Edit Propagation

單點 factual edit 後測 multi-hop consistency。

## 實驗 5：Task Vector Composition

測：

$$
\tau_1+\tau_2
$$

在不同能力對上的 interference。

## 實驗 6：BAR / Modular Expert Comparison

比較 modular post-training 與 monolithic continual training 的 forgetting。

## 實驗 7：Core Compression Sweep

逐步降低 resident capacity，測 $Q_C$ 、counterfactual generalization 與 $D_M$。

## 實驗 8：External Restoration

移除某能力因子後，用 external expert 恢復，測：

$$
R_S.
$$

## 實驗 9：Interface Representation Sweep

比較 text、structured、graph、programmatic interfaces 的：

$$
F_L.
$$

## 實驗 10：Factor Granularity Sweep

比較 coarse / medium / fine modules 的 verified utility 與 coordination cost。

## 實驗 11：Reconvergence Stress Test

讓多 experts 提供衝突 outputs，測 evidence-aware reconciliation。

## 實驗 12：Longitudinal Convergence

長期任務下持續 core update，測：

- drift；
- re-inflation；
- regression；
- rollback。

---

# 106. 什麼結果會支持本文？

以下結果會支持：

1. 能力 factor 在多種表示方法下具有一定穩定性；
2. 部分能力可被局部干預並具有 task-specific causal effect；
3. modular post-training 明顯降低 forgetting；
4. smaller core 在 external expansion 後恢復大部分 system utility；
5. external restoration score 高；
6. interface fidelity 可達可接受水平；
7. relation-aware factor graph 比 isolated factor list 更能預測性能；
8. selective convergence 可以維持 core size；
9. factor placement 動態調整可提高 Cognitive Density；
10. system-level reconvergence 不需要重新 merge 所有 weights；
11. cross-model functional homology 可重複；
12. counterfactual task 上保留抽象能力而非只保留 memorized behavior。

---

# 107. 什麼結果會削弱本文？

以下結果會削弱：

1. factor maps 對方法與 seed 極端不穩；
2. SAE features 幾乎無法提供 causal control；
3. 所有高階能力都高度 distributed 且不可替換；
4. post-hoc factorization 一旦壓縮就嚴重掉 generalization；
5. external interface 無法保持關鍵認知狀態；
6. reconvergence cost 長期高於 monolithic inference；
7. external restoration 無法補回失去能力；
8. module granularity 不存在任何有利區間；
9. task vector / merge 類方法在大模型持續出現嚴重 interference；
10. Minimum Sufficient Core 無法在不同 task distribution 重用；
11. factorized system 長期漂移比 monolithic model 更嚴重；
12. relation preservation 的成本接近保存整個原模型。

---

# 108. 公開命題與未公開方法的邊界

本文公開：

- 六算子 $D,C,X,L,R,G$ ；
- separability taxonomy；
- factor graph；
- restoration / interface / reconvergence 的量測問題；
- public experiments；
- falsification criteria。

本文不公開任何：

- private mechanistic search procedure；
- high-dimensional capability projection；
- weight map；
- parameter extraction algorithm；
- latent factor compiler；
- external bridge representation；
- capability substitution optimizer；
- reconvergence training；
- core convergence criterion 的私人實作。

因此：

$$
\boxed{
\text{Problem Architecture}
\neq
\text{Solution Architecture}.
}
$$

---

# 109. 與 Paper 07 的銜接

Paper 06 已經提出：

$$
D,C,X,L,R,G.
$$

但其中：

$$
X,L,R,G
$$

都依賴一個尚未深入研究的問題：

> **外部資料、外部 expert 與 temporary cognition 到底如何被編譯成 Mother AI 當下可使用的認知狀態？**

因此下一篇：

$$
\boxed{
\text{External Expansion}
\neq
\text{Retrieval}.
}
$$

Paper 07 將集中處理：

$$
\boxed{
\text{Information}
\rightarrow
\text{Task-Compatible Cognition}.
}
$$

---

# 110. 結論

成熟 Frontier AI 已經不是一張可以簡單切成：

$$
\text{knowledge}
+
\text{reasoning}
$$

的資料表。

它更像：

$$
\boxed{
\text{high-dimensional entangled cognitive system}.
}
$$

其中 language、world knowledge、representation、reasoning、meta-cognition、task patterns 與 learned heuristics 高度交織。

因此真正困難的問題不是：

> 刪掉哪些「不需要的參數」？

而是：

$$
\boxed{
\text{如何重新組織一個已經成熟的智能，}
}
$$

同時保留：

- relations；
- generalization；
- epistemic control；
- capability boundaries；
- ability to expand again。

本文把這個問題定義為：

$$
\boxed{
\text{Cognitive Factorization Problem}.
}
$$

並以：

$$
\boxed{
\mathfrak F
=
(
D,
C,
X,
L,
R,
G
)
}
$$

描述其六個核心研究算子。

其中：

$$
D
$$

不是找「哪個參數是某個知識」，

而是建立可檢驗的能力因子。

$$
C
$$

不是只縮小模型，

而是保存高價值 resident cognition。

$$
X
$$

不是普通 retrieval，

而是按需建立 temporary cognition。

$$
L
$$

不是 prompt forwarding，

而是保持 capability interface fidelity。

$$
R
$$

不是 majority vote，

而是 evidence-aware reconciliation。

$$
G
$$

不是把所有結果再塞回 weights，

而是選擇性地讓真正穩定、可重用的認知結構重新進入核心。

因此本文最終主張：

$$
\boxed{
\text{The goal is not to split intelligence into dead pieces.}
}
$$

真正目標是：

$$
\boxed{
\text{to make the couplings that constitute intelligence explicit, controllable, replaceable, and recomposable}.
}
$$

若這件事最終可行，

那麼未來 AI 的 scaling 不再只有：

$$
\boxed{
\text{more parameters}
}
$$

而會多出另一條路：

$$
\boxed{
\text{better cognitive factorization}.
}
$$

那時：

$$
\text{Resident Core}
+
\text{Conditional Capacity}
+
\text{External Capability}
$$

就可能不只是系統工程拼接，

而是一種新的：

$$
\boxed{
\text{native architecture of expandable intelligence}.
}
$$

---

# References

1. Shu, D., et al. (2025). *A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models*. arXiv:2503.05613.
2. Shi, W., et al. (2025). *Route Sparse Autoencoder to Interpret Large Language Models*. arXiv:2503.08200.
3. Tang, Y., et al. (2025). *On the Theoretical Foundation of Sparse Dictionary Learning in Mechanistic Interpretability*. arXiv:2512.05534.
4. Hase, P., Bansal, M., Kim, B., & Ghandeharioun, A. (2023). *Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models*. NeurIPS 2023.
5. Zhong, Z., et al. (2023). *MQUAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions*. EMNLP 2023.
6. Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). *Locating and Editing Factual Associations in GPT*. NeurIPS 2022.
7. Fu, Z., et al. (2025). *Model Merging for Knowledge Editing*. arXiv:2506.12384.
8. Zhou, Y., et al. (2024). *MetaGPT: Merging Large Language Models Using Model Exclusive Task Arithmetic*. arXiv:2406.11385.
9. Morrison, J., et al. (2026). *Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts*. arXiv:2604.18473.
10. Sukhbaatar, S., et al. (2024). *Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM*. COLM 2024.
11. Zhang, Q., et al. (2025). *BTS: Harmonizing Specialized Experts into a Generalist LLM*. EMNLP 2025.
12. Wu, Z., et al. (2023). *Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks*. arXiv:2307.02477.
13. Neo.K. & Aletheia. (2026). *Cognitive Density Hypothesis：認知密度命題*.
14. Neo.K. & Aletheia. (2026). *Resident Cognitive Core：Mother Model 到底必須常駐什麼？*.
15. Neo.K. & Aletheia. (2026). *MoE as Conditional Intelligence：Shared Core、Routed Experts 與能力局部化*.
16. Neo.K. & Aletheia. (2026). *Externalized Mixture of Cognitive Experts：為什麼 Expert 一定要住在同一個模型裡？*.
17. Neo.K. & Aletheia. (2026). *主 AI 的雙路形成命題：通用模型認知重構與持續養成式智能的發展路徑*.
18. Neo.K. & Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開命題論文。

本文公開：

- Cognitive Factorization Problem；
- $D,C,X,L,R,G$ 六算子；
- separability taxonomy；
- factor graph / controlled coupling；
- restoration / linking / reconciliation / convergence 的量測架構；
- public falsification tests。

本文不公開任何未驗證或未公開的：

- private mechanistic search；
- capability projection；
- weight-level factorization；
- parameter extraction；
- latent compiler；
- external bridge；
- substitution search；
- reconvergence optimizer；
- native core training / convergence method。

因此：

$$
\boxed{
\text{Public Factorization Theory}
\neq
\text{Private Factorization Method}.
}
$$
