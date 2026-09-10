# 貝葉斯中的貝葉斯
## ——誰授權更新規則？從 Prior、Likelihood 到 Meta-Epistemology 的遞歸問題

**Series:** Adaptive Epistemic Systems Series  
**Paper:** 10 / 11  
**Version:** v0.1  
**Language:** zh-TW  
**Status:** Complete Draft / Canonical UTF-8 Source

---

## 摘要

如果 Bayesian updating 的形式為：

$$
P(H\mid E)
=
\frac{
P(E\mid H)P(H)
}{
P(E)
}
$$

那麼它回答的是：在給定 hypothesis space、prior 與 likelihood 的前提下，觀察證據後應如何更新信念。

但它沒有回答：

$$
\boxed{
\text{Why this hypothesis space?}
}
$$

$$
\boxed{
\text{Why this prior?}
}
$$

$$
\boxed{
\text{Why this likelihood?}
}
$$

$$
\boxed{
\text{Why this update rule?}
}
$$

。

這些問題不是標準 Bayes 定理內部可以自動消除的。若進一步使用 Bayesian 方法選擇不同 prior、不同模型、不同 likelihood，甚至不同更新規則，就會出現：

$$
\text{Bayes over Bayes}
$$

。

而若再追問用什麼規則更新「哪一個 Bayes 比較值得使用」的信念，就形成 meta-level recursion。

本文提出一個 meta-epistemic framework，將認識系統拆成：

$$
\mathfrak{E}
=
(
\mathcal{H},
\Pi,
\mathcal{L},
\mathcal{U},
\mathcal{M},
\mathcal{C}
)
$$

其中 $$\mathcal{H}$$ 為假設空間，$$\Pi$$ 為 prior construction，$$\mathcal{L}$$ 為 likelihood／evidence model，$$\mathcal{U}$$ 為更新規則集合，$$\mathcal{M}$$ 為模型批判機制，$$\mathcal{C}$$ 為外部約束與經驗檢驗。

本文區分 object-level Bayes、model-level Bayes、prior-level Bayes、updater-level Bayes 與 meta-updater selection，並指出：Bayesianism 可以把更多認識論選擇轉成顯式不確定性，但無法藉由無限遞歸消滅所有 epistemic primitive。任一有限系統最終都必須在某些層級接受尚未由更高層規則完全證成的起點，例如 observation protocol、model class、loss、computational constraints、language of hypotheses 或 stopping rule。

因此本文拒絕「只要再上一層 Bayes 就能解決上一層不確定性」的無限回歸想像，並提出「有限反身認識論」：系統應允許自身的 prior、model、likelihood 與 updater 被挑戰、比較與替換，但同時必須承認某些當前 operational primitives，並透過外部預測、校準、反例、干預、模型批判與跨方法競爭持續削弱錯誤起點，而不是宣稱達到無前提的終極認識論。

本文核心命題為：

$$
\boxed{
\text{A justified updater is not justified merely because it updates coherently.}
}
$$

以及：

$$
\boxed{
\text{meta-Bayesian recursion can expose assumptions, but cannot abolish all assumptions.}
}
$$

。

**關鍵詞：** meta-Bayesian、prior、likelihood、update rule、認識論正當性、無限回歸、模型批判、反身認識論、epistemic primitive、Bayes over Bayes

---

## 1. 標準 Bayes 解決的是條件更新，不是起點問題

標準 Bayesian update：

$$
P(H\mid E)
=
\frac{
P(E\mid H)P(H)
}{
P(E)
}
$$

回答：

> 如果 prior 與 likelihood 如此，證據來了之後 posterior 應該如何？

它沒有回答：

> 為什麼一開始要用這組 prior 與 likelihood？

因此 Bayes 的數學一致性與認識論起點必須分開。

---

## 2. 四個被隱藏的前提

一個具體 Bayesian system 至少隱含：

$$
\mathcal{H}
$$

假設空間；

$$
\Pi
$$

prior construction rule；

$$
\mathcal{L}
$$

likelihood family；

$$
U_{\mathrm{Bayes}}
$$

更新規則。

所以真正的系統不是只有：

$$
P(H\mid E)
$$

而是：

$$
\boxed{
(
\mathcal{H},
\Pi,
\mathcal{L},
U_{\mathrm{Bayes}}
)
}
$$

。

---

## 3. Hypothesis Space 的授權問題

假設：

$$
\mathcal{H}
=
\{
H_1,H_2,H_3
\}
$$

。

Bayes 可以在：

$$
\mathcal{H}
$$

內重新分配概率。

但若真實狀態：

$$
H^\ast
\notin
\mathcal{H}
$$

則無論 posterior 多漂亮，都無法直接表示：

$$
H^\ast
$$

。

因此第一個 meta-question 是：

$$
\boxed{
\text{Who chose the space in which Bayesian belief is allowed to move?}
}
$$

。

---

## 4. Prior 的授權問題

假設兩個 prior：

$$
P_1(H)
$$

與：

$$
P_2(H)
$$

都符合概率公理。

這不代表：

$$
P_1
$$

與：

$$
P_2
$$

在具體問題上具有相同認識論正當性。

所以：

$$
\boxed{
\text{probability coherence}
\neq
\text{prior justification}
}
$$

。

---

## 5. Likelihood 的授權問題

Likelihood：

$$
P(E\mid H)
$$

是一個 evidence-generating model。

但它可能錯。

若：

$$
P_{\mathrm{model}}(E\mid H)
\neq
P_{\mathrm{world}}(E\mid H)
$$

Bayes 仍會 coherent 地更新。

因此：

$$
\boxed{
\text{correct conditionalization on a wrong likelihood is still wrong about the world}
}
$$

。

---

## 6. Updater 的授權問題

即使：

$$
U_{\mathrm{Bayes}}
$$

具有 coherence 優勢，也仍可以問：

> 為什麼這個 domain 要用 Bayes，而不是其他 update rule？

例如：

$$
U_{\mathrm{logic}}
$$

$$
U_{\mathrm{constraint}}
$$

$$
U_{\mathrm{interval}}
$$

$$
U_{\mathrm{optimization}}
$$

可能在不同 domain 更合適。

因此：

$$
\boxed{
\text{choosing Bayes is itself an epistemic decision}
}
$$

。

---

## 7. Object-Level Bayes

第一層：

$$
P(H\mid E)
$$

。

這是對世界假設的更新。

記為：

$$
\mathcal{B}^{(0)}
$$

。

---

## 8. Model-Level Bayes

若有多個模型：

$$
M_1,\ldots,M_n
$$

可以建立：

$$
P(M_i)
$$

並更新：

$$
P(M_i\mid D)
$$

。

這是：

$$
\mathcal{B}^{(1)}_{\mathrm{model}}
$$

。

---

## 9. Prior-Level Bayes

若不確定 prior family：

$$
\Pi_1,\ldots,\Pi_k
$$

可以建立：

$$
P(\Pi_j)
$$

並根據表現更新：

$$
P(\Pi_j\mid D)
$$

。

這是：

$$
\mathcal{B}^{(1)}_{\mathrm{prior}}
$$

。

---

## 10. Likelihood-Level Bayes

若存在：

$$
\mathcal{L}_1,\ldots,\mathcal{L}_m
$$

不同 likelihood family，也可：

$$
P(\mathcal{L}_j\mid D)
$$

。

因此連 evidence model 都可以被概率化。

---

## 11. Updater-Level Bayes

若候選更新器：

$$
U_1,\ldots,U_r
$$

包括：

$$
U_{\mathrm{Bayes}},
U_{\mathrm{generalized}},
U_{\mathrm{logic}},
U_{\mathrm{robust}},
\ldots
$$

可以建立：

$$
P(U_i)
$$

以及：

$$
P(U_i\mid D)
$$

。

這就是最直觀的：

$$
\boxed{
\text{Bayes over update rules}
}
$$

。

---

## 12. 但用什麼更新 $$P(U_i)$$？

問題立刻再上一層。

若：

$$
P(U_i)
\xrightarrow{U^{(2)}}
P(U_i\mid D)
$$

那麼：

$$
U^{(2)}
$$

憑什麼？

如果答案又是 Bayes，就得到：

$$
U^{(3)}
$$

的授權問題。

---

## 13. Meta-Recursive Chain

可以寫成：

$$
U^{(0)}
\leftarrow
U^{(1)}
\leftarrow
U^{(2)}
\leftarrow
U^{(3)}
\leftarrow
\cdots
$$

每一層都在授權下一層。

如果要求「任何規則都必須由更高規則完全證成」，就會出現：

$$
\boxed{
\text{epistemic infinite regress}
}
$$

。

---

## 14. 無限回歸不是靠多一層 Bayes 就消失

新增：

$$
\mathcal{B}^{(n+1)}
$$

只是把問題移到：

$$
n+1
$$

層。

所以：

$$
\boxed{
\text{more meta-Bayes}
\neq
\text{no assumptions}
}
$$

。

---

## 15. Epistemic Primitive

本文將當前系統無法再由內部更高規則完全證成，但仍必須暫時採用的元素稱為：

$$
\boxed{
\text{epistemic primitive}
}
$$

。

例如：

$$
\text{observation language}
$$

$$
\text{measurement protocol}
$$

$$
\text{model class}
$$

$$
\text{loss function}
$$

$$
\text{computational budget}
$$

$$
\text{stopping rule}
$$

。

---

## 16. Primitive 不等於永恆真理

epistemic primitive 只是：

$$
\text{currently operationally assumed}
$$

。

它可以被未來更高層證據挑戰。

因此：

$$
\boxed{
\text{primitive}
\neq
\text{dogma}
}
$$

。

---

## 17. 有限反身認識論

本文提出：

$$
\boxed{
\text{finite reflective epistemology}
}
$$

。

核心是：

1. 系統承認存在當前 primitives；
2. primitives 可以被觀察失敗挑戰；
3. 部分 primitives 可升級成顯式 hypothesis；
4. 但不要求一次把所有前提都無限 meta 化。

---

## 18. Reflection Budget

定義：

$$
B_{\mathrm{meta}}
$$

為 meta-epistemic 計算預算。

系統不能無限問：

> 為什麼？

因此需要：

$$
Depth_{\mathrm{meta}}
\le
B_{\mathrm{meta}}
$$

。

這是有限計算系統必須面對的事實。

---

## 19. Meta-Reasoning 也有成本

若每次推理都重新評估：

$$
\mathcal{H},
\Pi,
\mathcal{L},
U
$$

成本可能遠高於 object-level task。

因此：

$$
C_{\mathrm{meta}}
\gg
C_{\mathrm{object}}
$$

在部分任務成立。

---

## 20. 何時值得上升一層？

只有當：

$$
ExpectedValue(MetaReview)
>
Cost(MetaReview)
$$

才值得重新檢查 prior、model 或 updater。

這與 Paper 02 的更新張力原理一致。

---

## 21. Meta-Epistemic Tension

定義：

$$
T_{\mathrm{meta}}
$$

。

可由：

$$
PredictionFailure
$$

$$
CalibrationFailure
$$

$$
ModelConflict
$$

$$
RepeatedSurprise
$$

$$
DomainShift
$$

$$
Counterexample
$$

共同提高。

---

## 22. Meta-Review Trigger

若：

$$
T_{\mathrm{meta}}>\theta_{\mathrm{meta}}
$$

則系統不再只更新：

$$
P(H)
$$

而開始重新檢查：

$$
\mathcal{H}
$$

$$
\Pi
$$

$$
\mathcal{L}
$$

或：

$$
U
$$

。

---

## 23. Object Update 與 Meta Update 分離

正常情況：

$$
E
\rightarrow
P(H\mid E)
$$

。

meta 情況：

$$
Failure
\rightarrow
Review(
\mathcal{H},
\Pi,
\mathcal{L},
U
)
$$

。

這兩者不應每次混在一起。

---

## 24. Model Criticism 是停止回歸的重要外部錨點

如果認識系統只在內部比較：

$$
P(M_i)
$$

仍可能所有模型都錯。

因此需要：

$$
\boxed{
\text{contact with external observations}
}
$$

。

即：

$$
Prediction
\rightarrow
World
\rightarrow
Residual
$$

。

---

## 25. Residual 不是自動告訴你哪裡錯

若：

$$
Residual\gg0
$$

只代表：

$$
\text{something is wrong}
$$

。

可能是：

$$
Prior
$$

錯；

$$
Likelihood
$$

錯；

$$
HypothesisSpace
$$

錯；

$$
Data
$$

錯；

$$
Measurement
$$

錯。

所以 meta-diagnosis 本身也是推理問題。

---

## 26. Meta-Diagnostic Hypotheses

可以建立：

$$
Z
\in
\{
PriorError,
LikelihoodError,
ModelClassError,
DataError,
MeasurementError,
UpdaterError
\}
$$

。

再對：

$$
P(Z\mid Failure)
$$

做推理。

這是有用的 meta-Bayesian application。

---

## 27. 但 Meta-Diagnosis 也依賴模型

因此：

$$
P(Z\mid Failure)
$$

仍不是終極真理。

它只是更高層模型。

這再次說明：

$$
\boxed{
\text{meta-level does not escape modeling}
}
$$

。

---

## 28. Updater Competition

讓不同 update rule：

$$
U_1,\ldots,U_n
$$

在相同任務上競爭。

測量：

$$
Calibration
$$

$$
Accuracy
$$

$$
Cost
$$

$$
Recovery
$$

$$
Robustness
$$

。

這比抽象宣稱某個 updater 更高級更有效。

---

## 29. Epistemic Tournament

定義：

$$
Score(U_i,Q)
$$

。

長期更新：

$$
History(U_i)
$$

。

這形成：

$$
\boxed{
\text{epistemic tournament}
}
$$

。

Bayes 可以參加，但不自動獲勝。

---

## 30. Meta-Bayes 可以用於 Tournament

可以：

$$
P(U_i\mid H_{\mathrm{performance}})
$$

。

但這只是 tournament 的一種 meta-selection 方法。

仍然可以有其他 selection rule。

---

## 31. Meta-Bayes 不等於中立裁判

若用 Bayes 來判 Bayes 是否好，可能有：

$$
\text{methodological self-preference}
$$

。

因此需要非同源評估：

$$
\text{external task performance}
$$

$$
\text{calibration}
$$

$$
\text{counterfactual tests}
$$

$$
\text{adversarial failure}
$$

。

---

## 32. 自我證成循環

危險形式：

$$
Bayes
\Rightarrow
\text{choose Bayes}
\Rightarrow
\text{Bayes wins}
$$

。

若評分準則本身已由 Bayesian assumptions 決定，可能形成：

$$
\boxed{
\text{self-validating epistemic loop}
}
$$

。

---

## 33. 外部性能打破自我循環

如果不同 updater 都必須接受：

$$
WorldPrediction
$$

$$
Intervention
$$

$$
TaskOutcome
$$

測試，就能減少純內部自我證成。

---

## 34. 但外部觀測也不是無模型

Observation 本身需要：

$$
Sensor
$$

$$
Language
$$

$$
Measurement
$$

$$
Parsing
$$

。

因此：

$$
\boxed{
\text{there is no fully theory-free observation}
}
$$

。

---

## 35. 這不表示所有東西都相對

沒有 theory-free observation 不等於：

$$
\text{anything goes}
$$

。

仍可透過：

$$
cross-check
$$

$$
replication
$$

$$
instrument diversity
$$

$$
prediction
$$

$$
intervention
$$

逐步排除錯誤。

---

## 36. 多重獨立約束

一個認識系統的正當性可來自多種約束共同作用：

$$
J_{\mathrm{epistemic}}
=
f(
Coherence,
Prediction,
Calibration,
Intervention,
Compression,
Robustness,
CrossValidation
)
$$

。

Bayesian coherence 只是其中一項。

---

## 37. Epistemic Multi-Objective

不存在單一：

$$
\text{epistemic scalar}
$$

一定能完整排序所有方法。

因此更合理地：

$$
\vec{E}
=
(
Coherence,
TruthTracking,
Calibration,
Cost,
Robustness,
Interpretability
)
$$

。

---

## 38. Pareto-Epistemic Frontier

不同 updater 可能形成：

$$
\mathcal{P}_{\mathrm{epi}}
$$

Pareto frontier。

一個方法精確但昂貴；

另一個便宜但保守。

因此「最好的認識論」未必是單點。

---

## 39. Domain Conditionality 再次出現

可能：

$$
U_{\mathrm{Bayes}}
\succ
U_{\mathrm{logic}}
$$

在 domain $$D_1$$；

但：

$$
U_{\mathrm{logic}}
\succ
U_{\mathrm{Bayes}}
$$

在 domain $$D_2$$。

所以 updater choice 應該是：

$$
U^\ast(D,Q,C)
$$

。

---

## 40. Epistemic Router

可定義：

$$
Router_{\mathrm{epi}}
:
(Q,D,C)
\rightarrow
U^\ast
$$

。

這是本系列自適應認識系統的正式 meta-layer。

---

## 41. 但 Router 也需要授權

又可以問：

$$
Why(Router_{\mathrm{epi}})?
$$

。

這再次回到 regress。

所以 Router 必須被視為可檢驗的 operational mechanism，而非終極真理。

---

## 42. Router 的可證偽性

若：

$$
Router_{\mathrm{epi}}
$$

長期選錯 updater，則應：

$$
Update(Router_{\mathrm{epi}})
$$

或：

$$
Replace(Router_{\mathrm{epi}})
$$

。

因此 meta-layer 本身也可演化。

---

## 43. Meta-Learning 與 Epistemic Learning

系統不只學：

$$
WorldState
$$

也學：

$$
HowToUpdateWorldState
$$

。

因此：

$$
\boxed{
\text{learning the world}
+
\text{learning how to learn the world}
}
$$

。

---

## 44. 但「學會學習」仍不是無前提

meta-learning 仍使用：

$$
Objective
$$

$$
Data
$$

$$
Evaluation
$$

$$
SearchSpace
$$

。

這些又是 primitives。

---

## 45. Primitive Promotion

一個原本隱含 primitive：

$$
p
$$

若頻繁失敗，可以升格為：

$$
Hypothesis(p)
$$

。

因此：

$$
Primitive
\rightarrow
ExplicitModel
$$

是重要機制。

---

## 46. Primitive Demotion

反之，一個長期穩定、成本很高的 meta-variable 也可以暫時固化：

$$
ExplicitModel
\rightarrow
OperationalPrimitive
$$

。

這是一種計算壓縮。

---

## 47. 認識論的動態邊界

因此 primitive 與 model 之間不是固定牆。

而是：

$$
\boxed{
\text{dynamic epistemic boundary}
}
$$

。

---

## 48. Epistemic Depth

定義：

$$
d_{\mathrm{epi}}
$$

為當前系統顯式反思深度。

某些任務：

$$
d_{\mathrm{epi}}=0
$$

即可。

某些高風險任務可能需要：

$$
d_{\mathrm{epi}}>1
$$

。

---

## 49. 高風險任務需要更深 Meta-Review

若：

$$
Risk(Q)\uparrow
$$

則允許：

$$
d_{\mathrm{epi}}^\ast(Q)\uparrow
$$

。

這與 Paper 02 的 risk-aware freshness 相容。

---

## 50. 低風險任務不應無限自我懷疑

若每個簡單問題都：

$$
ReviewPrior
+
ReviewLikelihood
+
ReviewUpdater
+
ReviewRouter
$$

系統會陷入：

$$
\boxed{
\text{epistemic paralysis}
}
$$

。

---

## 51. Epistemic Paralysis

定義：

$$
C_{\mathrm{meta}}
>
Value_{\mathrm{task}}
$$

且系統仍持續 meta-review。

這是反身認識系統的失敗模式。

---

## 52. Stopping Rule

需要：

$$
StopMeta
$$

條件。

例如：

$$
ExpectedMetaGain
<
\epsilon
$$

或：

$$
Budget_{\mathrm{meta}}=0
$$

。

因此停止規則也是認識系統的一部分。

---

## 53. 停止規則又是 Primitive 嗎？

在當前層是。

它可以未來被挑戰。

這再次展示：

$$
\boxed{
\text{finite systems require provisional closure}
}
$$

。

---

## 54. Provisional Closure

本文將「暫時停止繼續追問，但保留未來可重開」稱為：

$$
\boxed{
\text{provisional epistemic closure}
}
$$

。

這不是宣稱真理已完成。

---

## 55. 這比終極證成更符合實際系統

有限智能必須：

$$
Act
$$

而不能永遠：

$$
Reflect
$$

。

所以合理架構是：

$$
Reflect
\rightarrow
Commit
\rightarrow
Act
\rightarrow
Monitor
\rightarrow
ReopenIfNeeded
$$

。

---

## 56. Meta-Commit Semantics

當 meta-review 完成，系統可以 commit：

$$
(
\mathcal{H}^\ast,
\Pi^\ast,
\mathcal{L}^\ast,
U^\ast
)
$$

作為當前 operational epistemic configuration。

---

## 57. Meta-Commit 也要版本化

定義：

$$
EConfig_t
$$

。

則：

$$
EConfig_{t+1}
\neq
EConfig_t
$$

時保存 lineage。

因此可以知道：

> 系統何時改變了自己的認識論配置？

---

## 58. Epistemic Configuration Provenance

保存：

$$
Prov(EConfig_t)
=
(
Reason,
Evidence,
Performance,
PreviousConfig,
Verifier
)
$$

。

這對長期反身系統極重要。

---

## 59. 否則系統會忘記自己為何改變方法

如果只保存新 updater，而不保存：

$$
WhyChanged
$$

可能重複來回切換。

因此 meta-history 也是記憶的一部分。

---

## 60. Meta-Epistemic Memory

定義：

$$
M_{\mathrm{meta}}
$$

保存：

$$
UpdaterHistory
$$

$$
ModelClassChanges
$$

$$
PriorChanges
$$

$$
FailureReasons
$$

$$
MetaExperiments
$$

。

---

## 61. 這與 Paper 05 的能力記憶相容

Updater 本身也可以是能力節點：

$$
v_{U_i}
\in
V_{\mathrm{capability}}
$$

。

其歷史可以被 reuse、adapt 或淘汰。

---

## 62. Bayes 變成一個可競爭的方法

因此：

$$
U_{\mathrm{Bayes}}
$$

不再是架構之神。

它只是：

$$
\boxed{
\text{a candidate epistemic operator with known strengths and failure modes}
}
$$

。

---

## 63. Bayesian Self-Reference

若系統使用 Bayes 評估：

$$
U_{\mathrm{Bayes}}
$$

本身，可建立：

$$
P(
U_{\mathrm{Bayes}}
\mid
D
)
$$

。

這在形式上沒有問題。

問題只在於：

$$
\boxed{
\text{do not confuse self-evaluation with ultimate self-justification}
}
$$

。

---

## 64. 自我評估與自我證成的分界

自我評估：

$$
Method
\rightarrow
Test
\rightarrow
Score
$$

。

自我證成：

$$
Method
\rightarrow
AssumeItsOwnStandard
\rightarrow
DeclareVictory
$$

。

後者是循環。

---

## 65. Cross-Epistemic Evaluation

可以讓：

$$
U_i
$$

被多種不同評分框架評估。

例如：

$$
Eval_{\mathrm{predictive}}
$$

$$
Eval_{\mathrm{calibration}}
$$

$$
Eval_{\mathrm{logic}}
$$

$$
Eval_{\mathrm{robust}}
$$

。

這降低單一方法自我偏好。

---

## 66. 但評估框架仍然不是無限中立

任何：

$$
Eval_j
$$

都帶有價值函數。

因此多重評估只能：

$$
\text{reduce}
$$

而不能：

$$
\text{eliminate}
$$

所有前提。

---

## 67. 這是認識論的有限性命題

本文提出：

$$
\boxed{
\text{Finite Epistemic Closure Theorem-like Claim}
}
$$

非正式地說：

> 任何有限可執行認識系統，都必須在某個層級暫時停止遞歸證成，採用一組 operational primitives，否則無法完成有限時間內的行動。

這不是數學定理，而是一個系統設計命題。

---

## 68. 認識論正當性來自哪裡？

本文不給單一來源。

更合理的是：

$$
J(U)
=
f(
Coherence,
EmpiricalSuccess,
Calibration,
Intervention,
Robustness,
Compression,
Cost,
Transparency
)
$$

。

正當性是多來源、可修正的。

---

## 69. Coherence 只是其中之一

Bayesian coherence 可以提高：

$$
J(U_{\mathrm{Bayes}})
$$

但不是：

$$
J(U_{\mathrm{Bayes}})=\infty
$$

。

---

## 70. Empirical Success 也不是全部

一個 heuristic 可能短期表現好，但在 distribution shift 下崩潰。

所以：

$$
EmpiricalSuccess
$$

也需要長程與跨域測試。

---

## 71. Robustness 也是正當性來源

如果一個 updater 對：

$$
Noise
$$

$$
Outlier
$$

$$
ModelMisspecification
$$

更穩健，可能比 exact Bayes 更適合某些實務場景。

---

## 72. Cost 也是認識論現實的一部分

在有限系統中：

$$
Computation
$$

不是免費。

因此一個理論上更精確但不可計算的方法，可能 operationally 不如近似方法。

---

## 73. Epistemic Rationality Under Resource Bounds

因此真正問題不是：

$$
\text{What is perfectly rational?}
$$

而更接近：

$$
\boxed{
\text{What is the best epistemic policy under bounded resources?}
}
$$

。

---

## 74. Bounded Epistemic Rationality

定義：

$$
U^\ast
=
\arg\max_U
J(U)
$$

subject to：

$$
Cost(U)\le B
$$

。

這比「永遠 Bayes」更一般。

---

## 75. Bayesian 可能在某些資源條件下勝出

若：

$$
Cost(U_{\mathrm{Bayes}})\le B
$$

且多維效用最高，則應選 Bayes。

這是實驗結果，不是身份偏好。

---

## 76. 也可能被其他方法擊敗

若：

$$
J(U_{\mathrm{robust}})
>
J(U_{\mathrm{Bayes}})
$$

則系統應允許：

$$
U_{\mathrm{Bayes}}
\rightarrow
U_{\mathrm{robust}}
$$

。

---

## 77. 認識論動態不動點

若某個 updater：

$$
U^\ast
$$

在長期 meta-review 中反覆被選回：

$$
MetaReview(U^\ast)=U^\ast
$$

可稱：

$$
\boxed{
\text{epistemic fixed point}
}
$$

。

但這仍然是相對於當前任務、資料與評估標準的。

---

## 78. 動態不動點更合理

隨環境：

$$
C_t
$$

改變，最優 updater 可能：

$$
U_t^\ast
\neq
U_{t+1}^\ast
$$

。

但更新規則選擇機制仍維持：

$$
Router_{\mathrm{epi}}
$$

的結構。

這是一種：

$$
\boxed{
\text{dynamic epistemic fixed-point process}
}
$$

。

---

## 79. 系統不是尋找永恆 Bayes，而是維持可修正性

最重要的 meta-invariant 可能不是：

$$
AlwaysUseBayes
$$

而是：

$$
\boxed{
\text{No epistemic operator is immune to challenge.}
}
$$

。

---

## 80. Epistemic Non-Immunity Principle

本文正式提出：

$$
\boxed{
\forall U_i,
\quad
Challengeable(U_i)=\text{True}
}
$$

。

包括：

$$
U_{\mathrm{Bayes}}
$$

本身。

---

## 81. 但 Challengeable 不等於每次都挑戰

否則會陷入 epistemic paralysis。

因此：

$$
ChallengeProbability(U_i)
$$

應由：

$$
T_{\mathrm{meta}}
$$

與風險決定。

---

## 82. Meta-Stability

長期表現良好的 updater：

$$
U_i
$$

可以具有：

$$
S_i^{\mathrm{meta}}\uparrow
$$

因此降低 review 頻率。

但：

$$
S_i^{\mathrm{meta}}\neq1
$$

。

---

## 83. 這把 Paper 01 的時空張力帶回認識論本身

不只是世界節點有：

$$
T_i
$$

更新張力。

連：

$$
Prior
$$

$$
Likelihood
$$

$$
ModelClass
$$

$$
Updater
$$

都可以有：

$$
T_{\mathrm{meta},i}
$$

。

---

## 84. 認識論本身也是動態圖

可建立：

$$
G_{\mathrm{epi}}
=
(
V_{\mathrm{epi}},
E_{\mathrm{epi}}
)
$$

節點包括：

$$
HypothesisSpaces
$$

$$
Priors
$$

$$
Likelihoods
$$

$$
Updaters
$$

$$
Evaluators
$$

。

---

## 85. Meta-Edges

例如：

$$
PriorRule
\rightarrow
Prior
$$

$$
LikelihoodModel
\rightarrow
Posterior
$$

$$
Evaluator
\rightarrow
UpdaterSelection
$$

。

因此認識論也可以被系統化成依賴圖。

---

## 86. Epistemic Dependency Invalidation

若：

$$
LikelihoodModel
$$

被推翻，所有依賴 posterior 應提高重驗證張力。

即：

$$
\Delta\mathcal{L}
\Rightarrow
T_{Posterior}\uparrow
$$

。

---

## 87. Prior Invalidated

若 prior construction 被發現有系統偏誤：

$$
\Delta\Pi
\neq0
$$

則需要重新檢查大量：

$$
P(H\mid E)
$$

。

這與 Paper 01 的基礎節點大範圍傳播完全同構。

---

## 88. 認識論也是世界狀態的一部分

因此本系列最後可以把：

$$
G_{\mathrm{epi}}
$$

放回：

$$
G_{\mathrm{world}}
$$

或能力圖。

系統不只知道世界，也知道：

$$
\boxed{
\text{自己目前如何在知道世界}
}
$$

。

---

## 89. 本篇核心命題

### 命題一：更新器非自我授權命題

$$
Coherent(U)
\not\Rightarrow
Justified(U)
$$

。

### 命題二：Meta-Bayes 非終極消前提命題

$$
MetaBayes
\not\Rightarrow
NoPrimitive
$$

。

### 命題三：有限閉合命題

有限可執行認識系統需要 provisional closure。

### 命題四：非免疫命題

$$
\forall U_i,
\quad
Challengeable(U_i)=\text{True}
$$

。

### 命題五：領域條件化命題

最適 updater：

$$
U^\ast
$$

依任務、風險、資料與資源而變。

---

## 90. 結論

本文從：

$$
P(H\mid E)
$$

往上追問：

$$
Why(H)?
$$

$$
Why(P(H))?
$$

$$
Why(P(E\mid H))?
$$

$$
Why(U_{\mathrm{Bayes}})?
$$

最後得到一個重要結論：

$$
\boxed{
\text{Bayesian updating can organize uncertainty, but it cannot by itself justify every structure that makes Bayesian updating possible.}
}
$$

。

如果對 prior 不確定，可以用更高層 Bayes。

如果對 model 不確定，也可以 Bayesian model averaging。

如果對 updater 不確定，也可以：

$$
P(U_i)
$$

。

但每多一層，都只是：

$$
\text{move the authorization problem upward}
$$

而不是：

$$
\text{erase the authorization problem}
$$

。

所以：

$$
\boxed{
\text{meta-Bayesian recursion can expose assumptions, but cannot abolish all assumptions}
}
$$

。

有限智能系統真正可行的道路，不是追求無限 meta-level 的終極自我證成，而是建立：

$$
\boxed{
\text{finite reflective epistemology}
}
$$

。

它具有：

$$
ObjectUpdate
$$

$$
MetaReview
$$

$$
EpistemicMemory
$$

$$
UpdaterCompetition
$$

$$
ExternalModelCriticism
$$

$$
ProvisionalClosure
$$

。

系統承認當前 operational primitives，但任何 primitive 都可在足夠失敗證據出現後升格為被檢驗對象。

因此最重要的 meta-invariant 不是：

$$
AlwaysUseBayes
$$

而是：

$$
\boxed{
\text{No epistemic operator is permanently immune to challenge.}
}
$$

。

這也使 Bayesian 不再是認識論頂端，而成為：

$$
\boxed{
\text{a highly useful but contestable epistemic capability}
}
$$

。

當系統能夠學習：

$$
\text{what to believe}
$$

也能學習：

$$
\text{how to update belief}
$$

甚至能在必要時重新檢查：

$$
\text{why it uses that updater}
$$

認識系統才真正進入反身層。

但這種反身性必須接受有限算力、有限時間與 provisional closure，否則只會形成無限遞歸而無法行動。

因此 Paper 10 最終將系列最初的 Bayesian 起點完全翻轉：

$$
\boxed{
\text{Bayes is not the unquestioned foundation of the system; Bayes itself becomes an object inside the system.}
}
$$

。

下一篇也是整個系列的終章，將不再繼續增加理論層，而回到唯一真正可以決定前面十篇意義的問題：

$$
\boxed{
\text{如果真的把這個系統實作出來，結果比現有 AI 更好，我們學到什麼？如果沒有更好，我們又究竟證明了什麼？}
}
$$

。

---

## 附錄 A：Meta-Epistemic State

$$
\mathfrak{E}
=
(
\mathcal{H},
\Pi,
\mathcal{L},
\mathcal{U},
\mathcal{M},
\mathcal{C}
)
$$

。

其中：

$$
\mathcal{H}
$$

為假設空間；

$$
\Pi
$$

為 prior construction；

$$
\mathcal{L}
$$

為 likelihood／evidence models；

$$
\mathcal{U}
$$

為 updater 集合；

$$
\mathcal{M}
$$

為 model criticism；

$$
\mathcal{C}
$$

為外部約束與檢驗。

---

## 附錄 B：Meta-Epistemic Tension

$$
T_{\mathrm{meta}}
=
\alpha PredictionFailure
+
\beta CalibrationFailure
+
\gamma ModelConflict
+
\delta RepeatedSurprise
+
\epsilon DomainShift
+
\zeta Counterexample
$$

。

若：

$$
T_{\mathrm{meta}}
>
\theta_{\mathrm{meta}}
$$

則：

$$
Review
(
\mathcal{H},
\Pi,
\mathcal{L},
\mathcal{U}
)
$$

。

---

## 附錄 C：Epistemic Router

$$
Router_{\mathrm{epi}}
:
(Q,D,C)
\rightarrow
U^\ast
$$

其中：

$$
U^\ast
\in
\{
U_{\mathrm{Bayes}},
U_{\mathrm{logic}},
U_{\mathrm{constraint}},
U_{\mathrm{robust}},
U_{\mathrm{optimization}},
\ldots
\}
$$

。

---

## 附錄 D：Bounded Epistemic Rationality

$$
U^\ast
=
\arg\max_U
J(U)
$$

subject to：

$$
Cost(U)\le B
$$

。

其中：

$$
J(U)
=
f(
Coherence,
EmpiricalSuccess,
Calibration,
Intervention,
Robustness,
Compression,
Transparency
)
$$

。

---

## 附錄 E：Epistemic Configuration

$$
EConfig_t
=
(
\mathcal{H}_t,
\Pi_t,
\mathcal{L}_t,
U_t,
Router_t,
Evaluator_t
)
$$

。

若：

$$
EConfig_{t+1}
\neq
EConfig_t
$$

則保存：

$$
Prov(EConfig_{t+1})
$$

與：

$$
Lineage(EConfig_{t+1})
$$

。

這使系統不只保存自己相信什麼，也保存自己為什麼改變了「相信的方法」。
