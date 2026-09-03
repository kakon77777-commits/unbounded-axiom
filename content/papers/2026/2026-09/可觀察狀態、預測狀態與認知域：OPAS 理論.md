# CODT-07
# 可觀察狀態、預測狀態與認知域：OPAS 理論
## Observable State, Predictive State, and Cognitive Domains: The OPAS Theory

**系列：** Cognitive Operator-Domain Theory, CODT / 認知算子-域理論  
**系列篇次：** 07 / 10  
**版本：** v1.0  
**日期：** 2026-08-21  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  
**文件性質：** 理論論文 / Observable-Predictive Interface 篇  
**前篇：** CODT-06〈History-Flow-Atlas Separation：認知歷史、轉移動力與域結構〉

---

## 摘要

CODT-06 已建立：

$$
\boxed{
History
\neq
Flow
\neq
Atlas.
}
$$

並透過 Phase 0.8-0.9 的 synthetic falsification 顯示：增加 operator-history length 並不能解釋掉 Cognitive Atlas；normal predictive quotient 也無法在 OOD regime 中 universal transfer。這把問題推向另一個更根本的缺項：**認知系統看到的 World / runtime state，是否等於真正有預測價值的 state？**

本文提出 **Observable-Predictive-Atlas Separation, OPAS**：

$$
\boxed{
S_t^{obs}
\neq
S_t^{pred}
\neq
\pi_R^{dst}.
}
$$

其中：

- $S_t^{obs}$：observer/runtime 可取得的有限 observable state；
- $S_t^{pred}$：保留對 future cognition / interaction prediction 有效資訊的 predictive interface state；
- $\pi_R^{dst}$：destination-side cognitive atlas quotient。

Phase 0.10 的 synthetic experiments 對一個直覺上合理的強猜想進行反證：若 Phase 0.9 的 OOD failure 只是因為漏掉 obvious world/runtime state，那麼直接加入 budget、artifact load、artifact identity、enabled-operator count、rare-artifact count、regime 等 visible state 應改善 held-out prediction。結果並非如此。Main normal 中 exact order-1 為：

$$
Bits_{order1}
=
4.5897,
$$

而 MDL-selected observable-state conditioning 為：

$$
Bits_{state}
=
4.8237.
$$

三個 normal robustness splits 中 raw state $0/3$ 勝過 order-1；六個 leave-one-regime-out holdouts 更是 $0/6$。

然而，這不是「state 沒有資訊」。conditional mutual information 顯示：

$$
I(
U_{t+1};
X_t
\mid
U_t
)
>
0
$$

對所有測試 state features 都高於 within- $U_t$ permutation null。例如 normal 中：

$$
I(
U_{t+1};
EnabledCount_t
\mid
U_t
)
\approx
0.3119
\text{ bits},
$$

以及：

$$
I(
U_{t+1};
RareArtifactCount_t
\mid
U_t
)
\approx
0.1701
\text{ bits}.
$$

因此 CODT-07 的核心方法學結論是：

$$
\boxed{
\text{Information-Bearing Observable}
\not\Rightarrow
\text{Predictive Sufficient State}.
}
$$

本文據此提出 predictive interface map：

$$
\boxed{
\psi_R:
S_t^{obs}
\mapsto
S_t^{pred}.
}
$$

一個 complexity-regularized candidate 為：

$$
\boxed{
\psi_R^*
=
\arg\min_{\psi}
\left[
L(\psi)
+
L(
U_{t+1}
\mid
U_t,
\psi(S_t^{obs}),
R
)
\right].
}
$$

這表示 World 與 cognition 的接口不能簡化為「把更多 World 欄位塞進 cognitive state」。World presentation 必須先經過 observer-relative acquisition、state abstraction、predictive compression 與 interface selection，才形成對當前 task / regime 有用的 predictive state。

本文同時保留兩個重要限制。第一， $S_t^{obs}$ 並非完整 simulator state；因此 raw-state failure 不能被誤解為「World state 對 cognition 沒用」。第二，WRPS 在 Phase 0.10 只取得微弱且不 robust 的 synthetic gain，且仍被 frozen destination atlas 明顯超越，因此：

$$
\boxed{
S_t^{pred}
\neq
\pi_R^{dst}.
}
$$

本文最終把 CODT runtime 擴展為：

$$
\boxed{
CognitiveRuntime_t
=
(
H_t,
S_t^{obs},
\psi_R,
S_t^{pred},
P_R,
\epsilon_R^{src},
\pi_R^{dst}
).
}
$$

這個分解不是 ultimate ontology，而是一條 architecture constraint：History、observable state、predictive state、transition flow、source predictive quotient 與 destination atlas 必須分帳。本文最後將下一篇問題推向 cognition-world boundary：如果 predictive state 是 observer-relative interface，而不是 World itself，那麼 cognition 如何合法地從 intent 走到 ActionRequest、authorization、World mutation 與 OutcomePresentation？

---

## 關鍵詞

OPAS；Observable-Predictive-Atlas Separation；CODT；predictive state；partial observability；World presentation；runtime state；conditional mutual information；predictive interface；cognitive atlas；PSR；POMDP

---

# 1. 從 HFAS 到 OPAS

CODT-06 已經削弱兩個強假說。

第一：

$$
\text{Atlas}
=
\text{missing higher-order history artifact}.
$$

目前 synthetic evidence 不支持。

第二：

$$
\text{normal predictive quotient}
=
\text{universal predictive state}.
$$

OOD transfer 也不支持。

因此一個自然問題出現：

> 我們一直只在 operator history 裡找 state，但真正缺的會不會是 operator sequence 外面的 runtime / World state？

Phase 0.10 的原始強猜想可以寫成：

$$
\boxed{
\text{OOD failure}
\approx
\text{missing obvious runtime state}.
}
$$

CODT-07 就從這個可反證猜想出發。

---

# 2. World、Presentation、Observable State、Predictive State

為了避免「state」一詞承擔太多本體角色，本文先區分四層。

## 2.1 World

$$
\mathbf W_t
$$

表示 World candidate。

CODT 不假設 observer 可以直接取得：

$$
\mathbf W_t.
$$

## 2.2 Presentation

observer $O$ 取得：

$$
\boxed{
\rho_{O,t}(
\mathbf W_t
).
}
$$

這是 observer-relative presentation。

## 2.3 Observable Runtime State

從 presentation 與 runtime instrumentation 中取得：

$$
\boxed{
S_t^{obs}.
}
$$

它是有限、可取、可記錄的 state sketch。

## 2.4 Predictive State

再由：

$$
\psi_R
$$

提取：

$$
\boxed{
S_t^{pred}.
}
$$

其目標不是忠實複製所有 observables，而是保留對 future prediction / control 有用的 sufficient-like information。

因此：

$$
\boxed{
\mathbf W_t
\neq
\rho_{O,t}(\mathbf W_t)
\neq
S_t^{obs}
\neq
S_t^{pred}.
}
$$

這個四層分離是 OPAS 的本體前提。

---

# 3. Observable State 的最小定義

本文暫時定義：

$$
\boxed{
S_t^{obs}
=
\text{finite observer/runtime-visible state available before the next cognitive action}.
}
$$

Phase 0.10 instrumentation 包含：

- current operator；
- budget/resource state；
- artifact count/capacity；
- exact artifact-type list；
- context-token count；
- enabled-operator count；
- rare-artifact count；
- regime metadata；
- step index。

這些 features 都是 pre-action。

因此避免把 future outcome 偷渡進 current state。

---

# 4. Observable 不等於 Complete

最重要的限制是：

$$
\boxed{
S_t^{obs}
\neq
S_t^{full-runtime}.
}
$$

Phase 0.10 的 scheduler 還可能依賴：

- exact context-token identity；
- recent operator tail；
- candidate-specific compatibility；
- novelty；
- scope weights；
- regime-specific transition weighting。

這些沒有全部出現在 observable sketch。

因此：

$$
\boxed{
\text{observable}
\neq
\text{complete Markov state}.
}
$$

這一點會限制所有後續解讀。

---

# 5. 為什麼「多看幾個欄位」不等於更懂

傳統直覺會認為：

> 更多 state features 應該帶來更好的 prediction。

但在 finite data 下，這不一定成立。

加入更多 features 會同時增加：

- state-space size；
- sparsity；
- parameter count；
- estimation variance；
- representation mismatch；
- regime-specific overfitting。

因此：

$$
\boxed{
MoreObservableDimensions
\not\Rightarrow
BetterPredictiveState.
}
$$

即使每個 feature 都有 information，也不表示它們以目前表示方式直接 conditioning 是最佳做法。

---

# 6. Main Normal：Raw State 反而變差

Phase 0.10 Main normal：

$$
Bits_{order1}
=
4.5897.
$$

MDL-selected raw observable-state model：

$$
Bits_{state}
=
4.8237.
$$

因此：

$$
\boxed{
\Delta_{state-order1}
=
-0.2340
\text{ bits/transition}.
}
$$

這不是微小差異。

它說明：

> 目前 chosen state representation 加入後，held-out coding 顯著惡化。

---

# 7. MDL 最後只留下很粗的 State Sketch

Main normal selection 最後保留：

$$
2\times2
$$

budget/load coarse state。

而以下 feature 沒有被 complexity-adjusted selection 保留：

- artifact vocabulary；
- enabled-count bins；
- rare-artifact bins；
- explicit regime。

這再次說明：

$$
\boxed{
\text{available feature}
\neq
\text{worth representing directly}.
}
$$

---

# 8. Normal Robustness：0/3

Main split alone 不能形成理論。

Phase 0.10 的 fixed-hyperparameter normal robustness 中：

$$
\boxed{
RawState
<
Order1
\quad
0/3.
}
$$

也就是 raw state conditioning 沒有在三個 splits 中穩定改善 exact order-1。

所以：

$$
\boxed{
\text{simple observable-state augmentation lacks robust support}.
}
$$

---

# 9. Leave-One-Regime-Out：0/6

更強的是六個 leave-one-regime-out tests。

raw state gain over order-1 分別為：

$$
-0.1693,
-0.2183,
-0.2000,
-0.0996,
-0.1257,
-0.1759.
$$

所以：

$$
\boxed{
\Delta_{state-order1}<0
\quad
6/6.
}
$$

這直接反證了：

> 只要把 obvious runtime observables 加進去，跨 regime prediction 就會更好。

---

# 10. Backoff 不是主要解釋

如果 state model 在 test 上大量遇到 unseen state key，負結果可能只是 dictionary coverage failure。

但 Phase 0.10 的 backoff rate 很低。

OOD artifact holdout 甚至：

$$
\boxed{
BackoffRate=0.
}
$$

所以：

$$
\boxed{
\text{raw state failure}
\neq
\text{simple unseen-state failure}.
}
$$

至少目前 evidence 不支持這個解釋。

---

# 11. OOD State Distribution 的確大幅改變

Normal：

$$
MeanArtifactLoad
=
0.3582,
$$

$$
MeanRareArtifactCount
=
0.2687,
$$

$$
MeanEnabledOperatorCount
=
6.5365.
$$

OOD artifact：

$$
MeanArtifactLoad
=
0.5448,
$$

$$
MeanRareArtifactCount
=
2.9303,
$$

$$
MeanEnabledOperatorCount
=
8.6044.
$$

因此：

$$
\boxed{
\text{visible distribution shift exists}.
}
$$

問題不是「OOD 根本沒變」。

問題是：

> 看得到 shift，不等於已經找到能有效代表 transition structure 的 state。

---

# 12. Observable Distribution Shift 不等於 Predictive Sufficiency

OOD leave-one-regime-out：

$$
Bits_{order1}
=
4.1887,
$$

$$
Bits_{state}
=
4.2883.
$$

raw state 更差。

因此：

$$
\boxed{
\text{observable distribution shift}
\not\Rightarrow
\text{predictive-state sufficiency}.
}
$$

這是 OPAS 的第一個核心原則。

---

# 13. State 不是「沒有資訊」

如果只看 code length，很容易得到錯誤結論：

> 那些 state features 都沒用。

Phase 0.10 因此另外測：

$$
I(
U_{t+1};
X_t
\mid
U_t
).
$$

這個量問：

> 在 current operator 已知後，feature $X_t$ 是否還帶有對下一 operator 的額外統計資訊？

這和「直接拿來 conditioning 是否提高 held-out coder」是不同問題。

---

# 14. Conditional Mutual Information 結果

Normal 中：

$$
I(
U_{t+1};
BudgetBin_t
\mid
U_t
)
=
0.1099,
$$

$$
I(
U_{t+1};
LoadBin_t
\mid
U_t
)
=
0.1114,
$$

$$
I(
U_{t+1};
RareArtifactCount_t
\mid
U_t
)
=
0.1701,
$$

$$
I(
U_{t+1};
EnabledCount_t
\mid
U_t
)
=
0.3119.
$$

resource-state aggregate：

$$
I(
U_{t+1};
ResourceState_t
\mid
U_t
)
\approx
0.2459.
$$

這些都高於 40 次 within-current-operator permutation null。

---

# 15. Permutation Resolution 的限制

40 次 permutations 意味著 empirical upper-tail resolution：

$$
\boxed{
p_{min}
=
\frac{1}{41}
\approx
0.02439.
}
$$

因此不能把：

$$
p=0.02439
$$

解讀成極精確顯著性。

它只是：

> 在目前 permutation resolution 下，observed CMI 超過所有 40 個 null samples。

CODT 要保留這個有限性。

---

# 16. Pooled Regime 也有資訊

六 regimes pooled data 中：

$$
I(
U_{t+1};
R_t
\mid
U_t
)
=
0.2530
\text{ bits}.
$$

explicit regime label 不是沒有資訊。

但 pooled MDL selection 仍沒有保留 explicit regime 作 raw state feature。

因此：

$$
\boxed{
\text{StatisticalInformation}
\neq
\text{ComplexityAdjustedRepresentationValue}.
}
$$

---

# 17. OPAS 的核心 Methodological Separation

現在可以正式寫：

$$
\boxed{
\text{Information-Bearing Observable}
\not\Rightarrow
\text{Predictive Sufficient State}.
}
$$

原因是「有資訊」只表示：

$$
I(Y;X\mid Z)>0.
$$

而 predictive state 還要求：

- representation compactness；
- generalization；
- low variance；
- transfer；
- stability；
- updateability；
- decision/control usefulness。

所以 sufficiency 是比 information 更強的要求。

---

# 18. Predictive State 不應等於 Raw Feature Tuple

最簡單做法：

$$
S_t^{pred}
=
S_t^{obs}.
$$

Phase 0.10 的結果不支持這個 identity。

因此需要：

$$
\boxed{
\psi_R:
S_t^{obs}
\mapsto
S_t^{pred}.
}
$$

 $\psi_R$ 的責任是：

- discard nuisance variation；
- preserve predictive information；
- merge redundant observables；
- retain regime-relevant structure；
- control representation complexity。

---

# 19. Predictive Interface Map

本文把 $\psi_R$ 稱為：

$$
\boxed{
\text{Predictive Interface Map}.
}
$$

它不是一般 feature extractor 的同義詞。

因為它還受到：

- observer；
- task；
- regime；
- budget；
- history；
- World interface；

條件約束。

因此更完整可寫：

$$
\boxed{
S_t^{pred}
=
\psi_R(
S_t^{obs},
H_t,
B_t,
G_t
).
}
$$

其中 $G_t$ 可以表示 active goal / task context。

---

# 20. Complexity-Regularized Predictive Interface

本文保留 Phase 0.10 的 candidate：

$$
\boxed{
\psi_R^*
=
\arg\min_{\psi}
\left[
L(\psi)
+
L(
U_{t+1}
\mid
U_t,
\psi(S_t^{obs}),
R
)
\right].
}
$$

這不是 theorem。

它是一個 engineering principle：

> predictive representation 必須為自身複雜度付代價。


---

# 21. Predictive State 與 Belief State 的關係

外部 POMDP tradition 通常區分 hidden environment state、observation 與 belief state。

CODT 不直接把：

$$
S_t^{pred}
$$

等同 POMDP belief。

原因包括：

- CODT 的 current state 未必來自完整 generative model；
- observable features 未必對 hidden state 有完整 likelihood model；
- cognition runtime 還包含 operator / domain / license / resource semantics；
- predictive interface 可以由 discriminative prediction 學得，而不必先建立 latent-state model。

因此：

$$
\boxed{
S_t^{pred}
\neq
\text{POMDPBeliefState}
}
$$

是目前的 boundary statement。

---

# 22. Predictive State Representations 的方法學種子

Predictive State Representation, PSR 路線提供一個重要外部概念：

state 不一定要被表示成 latent hidden-state variable。

它可以透過對 future observations 的 predictions 表示。

Littman 與 Sutton 的 predictive-state work 尤其強調：

$$
\boxed{
\text{state can be represented by predictions of future observations under actions}.
}
$$

CODT 吸收這個 general direction。

但 Phase 0.10 的 WRPS 只做：

$$
\text{finite next-operator predictive pooling}.
$$

因此：

$$
\boxed{
WRPS
\neq
\text{general PSR}.
}
$$

---

# 23. Predictive-State Inference 的另一個方法學種子

Predictive State Inference Machines 提供另一個 relevant idea：

> 與其先學 latent dynamical model，再對 latent state 做 inference，可以直接在 predictive-state space 中學 inference / filtering。

這和 OPAS 的：

$$
S_t^{obs}
\rightarrow
\psi_R
\rightarrow
S_t^{pred}
$$

在方法學上相容。

但：

$$
\boxed{
\psi_R
\neq
PSIM.
}
$$

CODT 沒有沿用 PSIM 的 exact learning setup、loss 或 guarantees。

這只是 predictive-interface learning 的外部參照。

---

# 24. WRPS：第一次 Predictive Pooling

Phase 0.10 建立 World/Runtime Predictive States, WRPS。

它對：

$$
(
U_t,
S_t^{obs}
)
$$

contexts 做 finite-future predictive pooling。

Main：

$$
Bits_{WRPS}
=
4.5736.
$$

相對 exact order-1：

$$
\boxed{
Gain
=
0.0160
\text{ bits/transition}.
}
$$

這顯示 predictive pooling 在單一 main split 中可能回收部分 state information。

---

# 25. WRPS 並不 Robust

但三個 fixed-hyperparameter normal robustness splits 中，WRPS 只在：

$$
\boxed{
1/3
}
$$

勝過 order-1。

三 split 平均：

$$
Bits_{order1}
=
4.5786,
$$

$$
Bits_{WRPS}
=
4.6040.
$$

所以：

$$
\boxed{
\text{WRPS main gain is weak / non-robust}.
}
$$

CODT-07 不把它升格成「predictive-state theory 已驗證」。

---

# 26. OOD WRPS 只取得極小改善

OOD leave-one-regime-out：

$$
Bits_{order1}
=
4.1887,
$$

$$
Bits_{WRPS}
=
4.1832.
$$

改善：

$$
\boxed{
0.0055
\text{ bits/transition}.
}
$$

這個差異太小，而且只是一個 held-out regime 的結果。

因此：

$$
\boxed{
\text{OOD WRPS gain}
\neq
\text{robust OOD rescue}.
}
$$

---

# 27. Predictive Interface 仍是 Open Problem

Phase 0.10 真正得到的不是：

> WRPS 就是正確 predictive state。

而是：

$$
\boxed{
\text{a predictive interface is needed,
but current coarse WRPS is insufficient}.
}
$$

這個負結果反而比弱正結果更重要。

因為它避免 CODT 直接把第一個 learned state abstraction 固化成 ontology。

---

# 28. Atlas 仍然更強

Main frozen destination atlas：

$$
Bits_{atlas}
=
4.3422.
$$

Main WRPS：

$$
Bits_{WRPS}
=
4.5736.
$$

差：

$$
\boxed{
0.2314
\text{ bits/transition}.
}
$$

三個 robustness splits 平均：

$$
Bits_{atlas}
=
4.3399,
$$

仍優於：

$$
Bits_{WRPS}
=
4.6040.
$$

所以：

$$
\boxed{
S_t^{pred}
\neq
\pi_R^{dst}.
}
$$

這是 OPAS 的第二個核心 separation。

---

# 29. 為什麼 Predictive State 不等於 Atlas

兩者的 base space 不同。

predictive state 主要描述：

$$
\boxed{
\text{current observer/runtime state relevant to future prediction}.
}
$$

destination atlas 描述：

$$
\boxed{
\text{quotient structure over future operator identities / operational regions}.
}
$$

因此：

$$
S_t^{pred}
$$

是 state interface。

而：

$$
\pi_R^{dst}
$$

是 destination quotient。

一個是：

$$
\text{what matters now}.
$$

另一個是：

$$
\text{how future operator space can be compressed}.
$$

不能用同一個 object 代替。

---

# 30. OPAS

本文正式定義：

$$
\boxed{
OPAS
:
S_t^{obs}
\neq
S_t^{pred}
\neq
\pi_R^{dst}.
}
$$

這個 separation 不只是 naming convention。

它要求三套不同 evidence。

## Observable State Evidence

回答：

> 什麼可以被 observer / runtime 取得？

## Predictive State Evidence

回答：

> 哪些 state abstraction 對 future prediction / control 有穩定價值？

## Atlas Evidence

回答：

> 哪些 operator-space quotients 具有 domain-level predictive / compressive / structural value？

---

# 31. OPAS 與 HFAS 的整合

HFAS：

$$
History
\neq
Flow
\neq
Atlas.
$$

OPAS：

$$
ObservableState
\neq
PredictiveState
\neq
Atlas.
$$

整合後至少得到：

$$
\boxed{
H_t,
S_t^{obs},
S_t^{pred},
P_t,
\mathcal A_t
}
$$

五種不同物件。

它們會耦合。

但不能合併。

---

# 32. Source Predictive Quotient 也不能被 OPAS 吃掉

CODT-06 已建立：

$$
\epsilon_R^{src}
:
U_t
\mapsto
S_t^{src-pred}.
$$

這個 quotient 主要壓縮 source operator identity。

OPAS 的：

$$
S_t^{pred}
$$

則可以包含比 operator identity 更廣的 runtime/world information。

因此：

$$
\boxed{
\epsilon_R^{src}
\neq
S_t^{pred}.
}
$$

前者是 source operator quotient。

後者是 world/runtime predictive interface candidate。

---

# 33. Predictive State 是 Observer-Relative

如果兩個 observers：

$$
O_1,O_2
$$

取得不同 presentations：

$$
\rho_{O_1}(\mathbf W)
\neq
\rho_{O_2}(\mathbf W),
$$

則：

$$
S_{t,O_1}^{obs}
\neq
S_{t,O_2}^{obs}.
$$

因此 predictive interface 也可能不同：

$$
\psi_{R,O_1}
\neq
\psi_{R,O_2}.
$$

所以：

$$
\boxed{
PredictiveState
\text{ is not observer-free by default}.
}
$$

---

# 34. Predictive State 也可能 Task-Relative

對同一 observable state：

$$
S_t^{obs},
$$

若 task $G_1$ 是：

> predict next operator，

而 task $G_2$ 是：

> choose safe action，

最佳 abstraction 不一定相同。

因此：

$$
\boxed{
S_t^{pred}
=
S_t^{pred}(G,R,O,B).
}
$$

這個 dependence 不表示任意相對主義。

它表示 sufficiency 是相對於 target task 定義。

---

# 35. Sufficiency 必須相對 Target

若：

$$
Y
$$

是 prediction target，

則最理想 state representation：

$$
Z
$$

希望滿足：

$$
P(
Y
\mid
S^{obs}
)
\approx
P(
Y
\mid
Z
).
$$

且：

$$
L(Z)
<
L(S^{obs}).
$$

這可以理解為 task-relative sufficiency candidate。

因此：

$$
\boxed{
\text{SufficientFor}(Y_1)
\not\Rightarrow
\text{SufficientFor}(Y_2).
}
$$

---

# 36. Predictive Sufficiency 不是 Ontological Sufficiency

即使：

$$
S_t^{pred}
$$

對下一 operator 是 sufficient-like representation，

也不表示：

$$
\boxed{
S_t^{pred}
=
\mathbf W_t.
}
$$

predictive sufficiency 只是：

> 對特定 future target 足夠。

它不是：

> 完整描述 World。

因此：

$$
\boxed{
PredictiveSufficiency
\neq
OntologicalCompleteness.
}
$$

---

# 37. Information Bottleneck 的弱類比

OPAS 的直覺和 information-bottleneck 類思想有一個一般相似性：

> 丟掉對 target 無用的輸入 variation，保留 predictive/relevant information。

但 CODT 不直接把 $\psi_R$ 等同 standard Information Bottleneck solution。

原因：

- runtime state 有 legality / World boundary；
- task target 可變；
- history 存在；
- state update 是 sequential；
- atlas 是另一個 quotient；
- representation cost 不只 mutual information。

所以：

$$
\boxed{
OPAS
\neq
InformationBottleneckTheory.
}
$$

只共享 compression / relevance trade-off 的 general intuition。

---

# 38. Nuisance State

定義：

$$
N_t
\subseteq
S_t^{obs}
$$

若它對當前 target 幾乎不增加 held-out predictive/control value，且增加 representation cost。

則：

$$
\boxed{
N_t
=
\text{task-relative nuisance state}.
}
$$

nuisance 不等於無意義。

它可能對另一 task 有價值。

---

# 39. Hidden Predictive Variable

反過來，如果：

$$
S_t^{obs}
$$

缺少一個真正 transition-relevant variable：

$$
Z_t^*,
$$

那麼不論如何重新 binning observables，都可能無法得到 sufficient state。

因此：

$$
\boxed{
\text{bad abstraction}
\quad\text{and}\quad
\text{missing variable}
}
$$

是兩種不同 failure mode。

Phase 0.10 無法完全區分兩者。

---

# 40. Partial Observability 是 OPAS 的核心而不是缺陷

如果 observer 永遠只取得：

$$
\rho_O(\mathbf W),
$$

那：

$$
S_t^{obs}
$$

天然就是 partial。

因此 predictive interface 的目的不是幻想恢復 omniscient state。

而是：

$$
\boxed{
\text{construct a usable state under partial observability}.
}
$$

這使 OPAS 和 MWT observer-embedded principle 直接接合。


---

# 41. World Coupling 的新形式

在 OPAS 前，容易寫：

$$
WorldState
\rightarrow
CognitiveState
\rightarrow
Operator.
$$

這太粗。

更保守的候選是：

$$
\boxed{
\rho_{O,t}(\mathbf W_t)
\rightarrow
S_t^{obs}
\rightarrow
\psi_R
\rightarrow
S_t^{pred}
\rightarrow
P_R
\rightarrow
U_{t+1}.
}
$$

其中 World 不直接進 cognitive predictor。

先經 observer-relative presentation。

再形成 observable state。

再經 predictive interface。

---

# 42. Predictive Interface 是 Boundary Object

 $\psi_R$ 位在：

$$
\boxed{
WorldPresentation
\leftrightarrow
CognitivePrediction
}
$$

之間。

因此它不是單純 internal feature engineering。

它具有 boundary-object 地位：

- 接受 observer-side state；
- 輸出 cognition-side predictive state；
- 記錄 representation loss；
- 攜帶 task/regime version；
- 可以被 audit；
- 可以被重新訓練；
- 不得假裝等於 World。

---

# 43. Predictive Interface Certificate

本文提出：

$$
\boxed{
PredictiveInterfaceCertificate_t
}
$$

至少記錄：

- observer；
- input state schema；
- target task；
- regime；
- history scope；
- abstraction map version；
- held-out predictive value；
- complexity cost；
- known failure boundary；
- transfer evidence；
- rollback target。

這使：

$$
S_t^{pred}
$$

不是一個無來源 latent label。

---

# 44. State Abstraction 也必須 Versioned

如果：

$$
\psi_R^{v1}
\rightarrow
\psi_R^{v2},
$$

舊 history 不能被回寫成：

> 當時其實用的是 v2。

因此：

$$
\boxed{
StateAbstractionUpdate
\neq
HistoryRewrite.
}
$$

runtime trace 必須保留當時實際使用的 interface version。

---

# 45. Observable Schema 也會漂移

新的 instrumentation 可能新增：

- tool state；
- memory state；
- world affordance；
- social context；
- latency；
- embodied signal。

因此：

$$
Schema(
S_t^{obs}
)
$$

本身也 versioned。

所以 OPAS 不假設固定 feature universe。

---

# 46. State-Selection Gate

若 candidate feature $X$ 被加入 observable state，

不應只問：

$$
I(
U_{t+1};
X
\mid
U_t
)>0.
$$

還要問：

$$
\boxed{
NetStateGain(X)
=
PredictiveGain
-
RepresentationCost
-
EstimationCost
-
TransferPenalty.
}
$$

只有：

$$
NetStateGain(X)>0
$$

才有 strong inclusion evidence。

---

# 47. Representation Cost

state representation 成本包括：

- storage；
- encoding；
- model parameters；
- update complexity；
- missingness handling；
- instrumentation overhead。

所以：

$$
\boxed{
\text{state is not free}.
}
$$

---

# 48. Estimation Cost

更多 state combinations 會增加 sample requirement。

若一個 feature 只提供：

$$
0.01
$$

bits predictive gain，

但把 context count 放大十倍，

它可能不值得。

因此：

$$
\boxed{
InformationGain
\neq
SampleEfficiency.
}
$$

---

# 49. Transfer Penalty

一個 feature 在 normal regime 很 predictive，

但在 OOD 完全失效，

則：

$$
TransferPenalty
$$

應增加。

因此：

$$
\boxed{
PredictiveState
\text{ should report regime scope}.
}
$$

不能把 normal-optimal representation 冒充 universal state ontology。

---

# 50. State Drift 和 Flow Drift 也要分開

若 observable distribution 改變：

$$
p_t(S^{obs})
\neq
p_{t+1}(S^{obs}),
$$

不一定表示 transition law 改變。

反之 flow 也可能改變，而 observable marginals 很穩定。

因此：

$$
\boxed{
StateDistributionDrift
\neq
FlowDrift.
}
$$

OPAS 和 Flow-Atlas Separation 應聯合使用。

---

# 51. State Drift 和 Atlas Shift 也要分開

同樣：

$$
p_t(S^{obs})
\neq
p_{t+1}(S^{obs})
$$

不直接推出：

$$
\mathcal A_t
\neq
\mathcal A_{t+1}.
$$

Phase 0.10 的 OOD 就已經顯示 visible state shift 很大，但 raw state 沒有改善 prediction。

所以：

$$
\boxed{
ObservableShift
\not\Rightarrow
AtlasShift.
}
$$

---

# 52. OPAS + HFAS + Flow-Atlas 的整體架構

整合 CODT-05、06、07：

$$
\boxed{
CognitiveRuntime_t
=
(
H_t,
S_t^{obs},
\psi_R,
S_t^{pred},
P_R,
\epsilon_R^{src},
\pi_R^{dst},
\mathcal A_t
).
}
$$

其中：

- $H_t$：canonical history；
- $S_t^{obs}$：observer/runtime-visible state；
- $\psi_R$：predictive interface；
- $S_t^{pred}$：task/regime-relative predictive state；
- $P_R$：transition flow；
- $\epsilon_R^{src}$：source predictive quotient；
- $\pi_R^{dst}$：destination atlas quotient；
- $\mathcal A_t$：atlas version / domain chart。

目前沒有任何一項可以安全消去其他項。

---

# 53. 這不是八個「真實心智器官」

上述 tuple 是 architecture separation。

不是 claim：

> cognition 真的由八個本體器官組成。

因此：

$$
\boxed{
ArchitectureSeparation
\neq
OntologicalAtomization.
}
$$

CODT 的目標是避免 interface conflation。

不是創造新的 mental faculty taxonomy。

---

# 54. OPAS 對 Domain Theory 的影響

Domain evidence 不能直接由 observable-state similarity 決定。

如果兩個 operators 常出現在相似 state：

$$
S^{obs},
$$

這只構成：

$$
ContextualAssociation.
$$

要成為 domain evidence 還需要：

- legal closure；
- flow；
- failure；
- boundary；
- compression；
- atlas stability。

所以：

$$
\boxed{
StateSimilarity
\neq
DomainMembership.
}
$$

---

# 55. Predictive State 也不是 Domain Membership Vector

可以想像：

$$
S_t^{pred}
=
(
m_1,\ldots,m_k
)
$$

直接用 domain membership 當 state。

但這仍然只是某種 representation candidate。

除非它在 held-out prediction / control 上有足夠 value。

因此：

$$
\boxed{
DomainVector
\neq
PredictiveState
}
$$

作為預設。

---

# 56. Predictive State 可以跨 Domain

一個 predictive state 可能同時需要：

- Search budget；
- current uncertainty；
- Representation mode；
- Planning status；
- World affordance。

這些可以跨多個 domains。

所以：

$$
\boxed{
PredictiveState
\text{ can be cross-domain}.
}
$$

這進一步證明 OPAS 不能被縮成 domain-conditioned state。

---

# 57. Atlas 也可以忽略某些 Observable State

反過來，一些 state variation 可能對：

$$
\pi_R^{dst}
$$

完全無關。

例如 UI-level metadata、temporary cache state 等。

所以：

$$
\boxed{
ObservableRichness
\neq
AtlasComplexity.
}
$$

增加 instrumentation 不應自動增加 domain count。

---

# 58. Predictive Interface 的 Falsification

一個 $\psi_R$ candidate 應被降級或撤銷，如果：

- held-out gain 不 robust；
- cross-regime transfer 崩潰；
- complexity cost 過高；
- missing-state backoff 太高；
- state update不穩定；
- downstream decision 沒改善；
- better representation 存在。

因此：

$$
\boxed{
PredictiveInterface
\text{ must be falsifiable}.
}
$$

WRPS 在 Phase 0.10 就只取得 weak candidate status。

---

# 59. OPAS 的 Promotion Gate

要把某個 predictive-state family 從 candidate 升為 strong runtime interface，本文要求至少：

## P1. Predictive Evidence

在 held-out data 有正 gain。

## P2. Complexity Control

gain 足以支付 representation / model cost。

## P3. Robustness

跨 split / session / regime 保持。

## P4. Update Stability

state recursion / update 不快速崩潰。

## P5. Transfer Scope

清楚知道可 transfer 到哪裡。

## P6. Decision / Control Relevance

若 claim 是 world-coupled state，應對 action / control 有價值。

## P7. Observer Contract

state 來源可追溯，不假裝 omniscient。

## P8. External Evidence

最終不能只依賴 synthetic generator。

---

# 60. Passive Prediction 的限制

Phase 0.10 主要 target 仍是：

$$
U_{t+1}.
$$

但 cognition-world interface 最終不應只問：

> 下一個 cognitive operator 是什麼？

真正 world-coupled state 應該問：

$$
\boxed{
P(
O_{t+1:t+k}
\mid
A_{t:t+k-1},
H_t,
O_t
).
}
$$

也就是：

> 在不同 actions 下，未來觀察會怎麼變？

這就是為什麼 CODT-07 最後必須把問題推向 Action / World Boundary。

---

# 61. Passive State 與 Controlled State

定義 passive predictive state：

$$
S_t^{passive}
$$

主要壓縮：

$$
P(
Future
\mid
History,
Observation
).
$$

controlled predictive state：

$$
S_t^{ctrl}
$$

則壓縮：

$$
P(
FutureObservations
\mid
History,
Observation,
ActionSequence
).
$$

因此：

$$
\boxed{
PassivePredictiveState
\neq
ControlledPredictiveState.
}
$$

Phase 0.10 還沒有真正建立後者。

---

# 62. 這解釋了 WRPS 的弱點

如果真正有用的 state information 主要體現在：

$$
\text{action-response structure},
$$

那只用：

$$
P(U_{t+1}\mid S_t^{obs})
$$

自然可能抓不到。

因此 Phase 0.10 的 negative result 還有一種合理 interpretation：

$$
\boxed{
\text{state may matter more for controlled futures than passive next-operator prediction}.
}
$$

這個 interpretation 必須由後續 experiment 驗證。

---

# 63. OPAS 與 CWB 的接口

Predictive state 可以提出：

$$
ActionIntent.
$$

但仍不能直接：

$$
WorldMutate.
$$

所以：

$$
S_t^{pred}
\rightarrow
Decision
\rightarrow
ActionRequest
\rightarrow
CWB.
$$

CWB 才負責：

- authorization；
- world operator mapping；
- commit；
- outcome presentation。

因此：

$$
\boxed{
PredictiveState
\neq
WorldAuthority.
}
$$

---

# 64. State Knowledge 不等於 Action Permission

即使 state predictor非常準，

也不能推出：

$$
\boxed{
CanPredict
\Rightarrow
CanAct.
}
$$

prediction license 和 action authority 是兩種不同權限。

這是 CODT 後續 Agent / robotics 安全的重要邊界。

---

# 65. OPAS 對 AI Agent Architecture 的直接意義

AI Agent 不應只有一個 giant state object。

更合理的是分開：

- raw observation store；
- normalized observable state；
- predictive interface state；
- task state；
- domain atlas；
- flow model；
- authority state；
- world boundary state。

這可以降低：

- state pollution；
- ontology confusion；
- accidental authority leakage；
- overfitting；
- debugging ambiguity。

---

# 66. State Store 與 Predictive Cache 也不應同一

raw observable state store 可以保留豐富 evidence。

predictive cache 則只保存 current useful abstraction。

因此：

$$
\boxed{
EvidenceStore
\neq
PredictiveStateCache.
}
$$

這和：

$$
DiscoveryArtifact
\neq
CertificationArtifact
$$

有相似的 architecture discipline。

---

# 67. Observable State 的可逆性

理想情況：

$$
S_t^{obs}
$$

應保留足夠 provenance，使：

$$
S_t^{pred}
$$

的來源可追溯。

但：

$$
\psi_R
$$

可以是 lossy。

因此：

$$
\boxed{
PredictiveCompression
\text{ may be irreversible}.
}
$$

只要 raw evidence 尚未被刪除。

這是：

$$
\boxed{
compress derived state, preserve source evidence.
}
$$

的原則。

---

# 68. Predictive Interface 不得回寫 Observation

如果 $\psi_R$ 把：

$$
RareArtifactCount
$$

判定為 nuisance，

不能回頭把 raw trace 中該欄位刪掉。

因此：

$$
\boxed{
PredictiveAbstraction
\neq
EvidenceDeletion.
}
$$

derived model 不得改寫原始可觀察歷史。

---

# 69. OPAS 對 Memory 的影響

Memory system 可以分成：

$$
RawObservationMemory,
$$

$$
PredictiveStateMemory,
$$

$$
DomainSummaryMemory.
$$

三者更新速度、保留時間與壓縮程度可以不同。

所以：

$$
\boxed{
Memory
\neq
SingleStateStore.
}
$$

這和 CODT-04 的 Memory / Search 裂解相容。

---

# 70. OPAS 對 Meta-Observation 的影響

MET 不應只監控：

$$
CurrentOperator.
$$

還應監控：

- observable-state drift；
- predictive-state confidence；
- abstraction error；
- flow residual；
- atlas mismatch。

因此 meta loop 可以擴展：

$$
\boxed{
MET:
(
S^{obs},
S^{pred},
P,
\mathcal A
)
\rightarrow
Monitor
\rightarrow
ControlSignal.
}
$$

這使 OPAS 直接影響 meta-control plane。

---

# 71. State-Mismatch Signal

如果：

$$
Error(
S_t^{pred}
)
$$

在特定 observable region 持續升高，

可以產生：

$$
\boxed{
StateMismatchSignal.
}
$$

它可能觸發：

- feature review；
- abstraction re-training；
- hidden-variable hypothesis；
- regime split；
- action probe；
- atlas review。

但不直接觸發 domain change。

---

# 72. Hidden-Variable Hypothesis

若 observable features 具有 CMI，

但所有簡單 abstractions 都失敗，

可以提出：

$$
\boxed{
MissingPredictiveVariableCandidate.
}
$$

這是一個 hypothesis。

不是直接宣稱：

> 系統一定有 hidden state X。

需要新的 instrumentation / intervention 驗證。

---

# 73. Action Probe 作為 State Discovery

一個 passive observer 可能無法區分兩個 hidden states。

但透過不同 action：

$$
a_1,a_2,
$$

如果 future observations 分離，就可以辨識 state。

因此：

$$
\boxed{
\text{state discovery can require intervention}.
}
$$

這正是下一篇 World Boundary 與再下一篇 controlled predictive domains 的重要接口。

---

# 74. OPAS 和 Causal Inference 不等同

Action probe 會讓人聯想到 causal intervention。

但 OPAS 不等同完整 causal inference theory。

因為：

- action legality 是 CWB 問題；
- predictive equivalence 不等於 causal identification；
- hidden confounding 仍可能存在；
- CODT 目前沒有 general causal-identification theorem。

因此：

$$
\boxed{
ControlledPrediction
\neq
CausalIdentification.
}
$$

---

# 75. OPAS 的第一版 Constitution

在 CODT-C0 至 C50 基礎上，本文增加：

## CODT-C51：Observable-Predictive Separation

$$
\boxed{
S_t^{obs}
\neq
S_t^{pred}.
}
$$

## CODT-C52：Predictive-Atlas Separation

$$
\boxed{
S_t^{pred}
\neq
\pi_R^{dst}.
}
$$

## CODT-C53：World-Presentation-State Separation

$$
\boxed{
\mathbf W
\neq
\rho_O(\mathbf W)
\neq
S^{obs}.
}
$$

## CODT-C54：Information-Sufficiency Separation

$$
\boxed{
I(Y;X\mid Z)>0
\not\Rightarrow
X
\text{ is a sufficient predictive state}.
}
$$

## CODT-C55：Complexity-Aware State Selection

state feature / abstraction 必須支付 representation 與 estimation cost。

## CODT-C56：Task-Relative Sufficiency

$$
\boxed{
SufficientFor(Y_1)
\not\Rightarrow
SufficientFor(Y_2).
}
$$

## CODT-C57：Predictive / Ontological Separation

$$
\boxed{
PredictiveSufficiency
\neq
OntologicalCompleteness.
}
$$

## CODT-C58：State-Abstraction Non-Rewriting

$$
\boxed{
PredictiveAbstraction
\neq
EvidenceDeletion
\neq
HistoryRewrite.
}
$$

## CODT-C59：Observer-Relative Predictive State

predictive interface 不預設 observer-free。

## CODT-C60：Predictive-State Non-Sovereignty

$$
\boxed{
CanPredict
\not\Rightarrow
CanAct.
}
$$

---

# 76. 本文反證了什麼

CODT-07 / Phase 0.10 削弱或反證：

1. OOD failure 只因漏了目前這批 obvious observables；
2. 加 raw state dimensions 就會改善 prediction；
3. visible distribution shift 就等於找到 predictive state；
4. explicit regime label 自動帶來 better coder；
5. current WRPS 已經足以取代 atlas。

---

# 77. 本文沒有反證什麼

本文沒有反證：

1. World state 對 cognition 很重要；
2. hidden / latent state 可能存在；
3. 更好的 predictive abstraction 可以存在；
4. action-conditioned state 可能比 passive state 更重要；
5. POMDP / PSR 類 state ideas 對 controlled dynamics 有價值；
6. real human / AI cognition 可能使用更豐富 state；
7. atlas 可以被更好的 predictive state 部分重構。

---

# 78. 本文的證據邊界

目前 evidence 仍是 synthetic。

observable state schema 由 experiment 設計。

predictive target 主要是 next operator。

permutation count 有限。

WRPS 不 robust。

因此：

$$
\boxed{
DomainPromotionCount=0.
}
$$

也：

$$
\boxed{
PredictiveStatePromotionCount=0.
}
$$

本文建立的是 theory constraint。

不是宣布找到真實 universal cognitive state。

---

# 79. 與下一篇的接口

OPAS 讓我們知道：

$$
PredictiveState
\neq
World.
$$

但 cognition 最終仍要對 World 做事。

因此下一篇需要回答：

> 一個 predictive / decision state 如何合法地變成外部作用？

這要求正式拆開：

$$
\boxed{
think
\neq
intend
\neq
request
\neq
authorize
\neq
act
\neq
WorldTransition.
}
$$

CODT-08 將處理：

**認知-世界邊界：從意圖、請求到世界轉移。**

---

# 結論

CODT-07 的核心不是再新增一個 state 名稱。

而是把「state」這個詞拆開。

我們可以看見：

$$
S_t^{obs}.
$$

但看見不等於：

$$
S_t^{pred}.
$$

某 feature 可以攜帶：

$$
I(
U_{t+1};
X_t
\mid
U_t
)>0
$$

的資訊，

卻仍然不值得直接進入 predictive state。

因為：

$$
\boxed{
\text{information}
\neq
\text{representation}
\neq
\text{sufficiency}.
}
$$

更不能因為一個 predictive state 好用，就把它升格成：

$$
\mathbf W.
$$

也不能因為它和 atlas 有關，就把兩者合併。

因此 OPAS 最終固定：

$$
\boxed{
S_t^{obs}
\neq
S_t^{pred}
\neq
\pi_R^{dst}.
}
$$

連同 HFAS：

$$
History
\neq
Flow
\neq
Atlas,
$$

CODT 現在已經不再只有「operator 與 domain」。

它開始形成真正的 World-facing cognition architecture：

$$
\boxed{
\rho_{O,t}(\mathbf W)
\rightarrow
S_t^{obs}
\rightarrow
\psi_R
\rightarrow
S_t^{pred}
\rightarrow
P_R
\rightarrow
U_{t+1}.
}
$$

但這條鏈還少最後一個最危險的接口：

$$
\boxed{
\text{prediction / decision}
\rightarrow
\text{World mutation}.
}
$$

那個接口不能靠推理自動跨越。

它需要 authority、legality、capability、commit 與 outcome presentation。

這就是下一篇的主題。

---

# 參考文獻與外部研究種子

## A. Partial Observability / Predictive State

1. Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). "Planning and Acting in Partially Observable Stochastic Domains." *Artificial Intelligence*, 101(1-2), 99-134.
2. Littman, M. L., Sutton, R. S., & Singh, S. (2001). "Predictive Representations of State." *Advances in Neural Information Processing Systems 14*.
3. Sun, W., Venkatraman, A., Boots, B., & Bagnell, J. A. (2016). "Learning to Filter with Predictive State Inference Machines." *Proceedings of the 33rd International Conference on Machine Learning*, PMLR 48, 1197-1205.

## B. Information / Representation

4. Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory*, 2nd ed. Wiley.
5. Tishby, N., Pereira, F. C., & Bialek, W. (1999). "The Information Bottleneck Method." arXiv:physics/0004057 / Allerton conference lineage.

**邊界聲明：** POMDP、PSR、PSIM 與 Information Bottleneck 只作 partial observability、future-prediction state、predictive filtering 與 relevance/compression trade-off 的外部方法學參照。CODT 的 OPAS、 $\psi_R$ 、destination atlas separation、World boundary、epistemic license 與 promotion gates 不宣稱來自上述理論，也不宣稱等同它們。

## C. 內部理論來源

1. CODT-01〈從認知方法到認知算子：認知解構學的域化轉向〉。
2. CODT-02〈認知算子代數與相對原子性〉。
3. CODT-03〈認知域的生成：域不是分類名稱，而是算子閉包與操作生態〉。
4. CODT-04〈共享底層認知域：Shared-Bottom Cognitive Runtime〉。
5. CODT-05〈認知域不是固定分類：Flow-Atlas Separation〉。
6. CODT-06〈History-Flow-Atlas Separation：認知歷史、轉移動力與域結構〉。
7. CDD Phase 0 v0.10：World/Runtime-Conditioned Predictive States。
8. `OBSERVABLE_PREDICTIVE_ATLAS_SEPARATION_v0.1.md`。
9. `state_feature_information_v0.10.csv`。
10. MWT / CWB SourcePacks。

---

# 版本記錄

## v1.0

- 正式建立 Observable-Predictive-Atlas Separation, OPAS。
- 定義 World、Presentation、Observable State、Predictive State 四層分離。
- 納入 Phase 0.10 raw-state negative result、CMI positive result 與 WRPS weak/non-robust result。
- 固定 `information-bearing observable != predictive sufficient state`。
- 正式提出 predictive interface map $\psi_R$。
- 建立 complexity-aware state-selection candidate。
- 區分 predictive state、source predictive quotient 與 destination atlas quotient。
- 建立 observer-relative、task-relative、regime-relative predictive-state constraints。
- 建立 Predictive Interface Certificate、State-Selection Gate、falsification / promotion gate。
- 明確保留 predictive state 不等於 POMDP belief、general PSR 或 World ontology。
- 為 CODT-08 Cognition-World Boundary 建立 state-to-action interface 前提。
