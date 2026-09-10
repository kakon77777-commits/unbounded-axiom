# Series C — C05｜概率也有域：不確定性、混沌、不可判定與世界預測包絡
## Probability as Domain: Uncertainty, Chaos, Undecidability, and the World Prediction Envelope

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 05 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-06  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Foundational Theory / Probability Domains / Uncertainty Representation / World Prediction

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文承接 C01–C04，並整合《從概率場到意圖場——跨尺度條件概率如何形成持久未來約束》與《概率、意圖與能動性——人類與 AI 的約束未來空間》。C05 的核心問題是：

> **如果未來的 AI 要把世界做成可觀察、可運行、可預測的計算世界，那麼概率、不確定、混沌、不可判定與未知，究竟是「計算失敗」，還是本來就應該被放進計算世界裡？**

本文採取後者。

---

# 摘要

談論「全域計算」時，最容易遇到的反駁之一是：世界有概率、混沌、測量誤差、資訊不足、不可判定與不可預測，因此不存在真正完整的全域計算。

本文拒絕這個推論。

$$
\boxed{\text{Uncertainty}\neq\text{Outside Computation}.}
$$

以及：

$$
\boxed{\text{Undecidable}\neq\text{Computationally Unrepresentable}.}
$$

一個更完整的 computational world 不應把未知、分支、不可判定與 prediction bounds 視為 exception，而應把它們本身表示成 domain-native state。

因此：

$$
\boxed{\text{Complete}\neq\text{Every question has one unique answer}.}
$$

更合理的完備性要求是：

$$
\boxed{
\text{answers, branches, unknowns, undecidability, errors, confidence, and bounds}
\text{ all have correct computational status}.
}
$$

本文定義跨尺度概率場：

$$
\boxed{
\mathfrak P_t
=
\left\{P_L(Z_L\mid\Sigma_t,C_t)\right\}_{L\in\Lambda}.
}
$$

其中尺度可包括：

$$
\Lambda
=
\{L_{token},L_{semantic},L_{strategy},L_{task},L_{world}\}.
$$

所以：

$$
\boxed{P_{token}\neq P_{meaning}\neq P_{plan}\neq P_{world}.}
$$

這避免將語言模型的 next-token probability 直接誤認成世界事件的 probability。

本文再區分至少六種 uncertainty domains：

$$
\boxed{
\mathcal U
=
\{U_{aleatory},U_{epistemic},U_{measurement},U_{model},U_{branch},U_{undecidable}\}.
}
$$

並特別保留：

$$
\boxed{\text{Probabilistic Description}\neq\text{Probabilistic Ontology}.}
$$

AI 使用概率描述世界，不等於已證明世界本體就是隨機。

本文定義 uncertainty record：

$$
\boxed{
\mathfrak U
=
\langle
Type,Source,Scale,Target,Lower,Upper,Distribution,Confidence,Verifier,History
\rangle.
}
$$

進一步定義受約束未來空間：

$$
\boxed{
\Omega_t^*
=
\Omega_t
\cap C_{physics}
\cap C_{history}
\cap C_{environment}
\cap C_{agent}.
}
$$

在此基礎上建立 **World Prediction Envelope**：

$$
\boxed{
\mathcal E_W(t)
=
\left\{
\left(
W_{t+\Delta}^{(i)},\underline p_i,\overline p_i,C_i,V_i,\rho_i
\right)
\right\}_{i\in I}.
}
$$

其中：

- $W_{t+\Delta}^{(i)}$：候選未來世界；
- $\underline p_i,\overline p_i$：概率／可信度 bounds；
- $C_i$：成立條件；
- $V_i$：verification status；
- $\rho_i$：provenance / reasoning lineage。

因此 Global AI 的預測輸出不必是單一「明天一定發生 X」，而可以是：

$$
\boxed{
\text{Candidate Worlds}
+
\text{Bounds}
+
\text{Conditions}
+
\text{Verification}
+
\text{Provenance}.
}
$$

本文把 chaos 納入 domain 化。對：

$$
s_{t+1}=F(s_t),
$$

若系統對初始條件敏感，AI 不應因此宣告「不可計算」，而應追蹤：

$$
\boxed{H_{pred}(t,\epsilon,\lambda,\delta)}
$$

即在 measurement error $\epsilon$ 、observer resolution $\lambda$ 與容許 error $\delta$ 下的 prediction horizon。

所以：

$$
\boxed{\text{Chaos}\neq\text{No Computation}.}
$$

更接近：

$$
\boxed{
\text{Chaos}
=
\text{finite reliable prediction horizon under bounded state precision}.
}
$$

本文也把 undecidability 拆成：

$$
\boxed{U_{formal}\neq U_{resource}\neq U_{epistemic}.}
$$

形式不可判定、資源不足與目前不知道，不得混為同一種「算不出來」。

最後本文提出 **Prediction Completeness Without Deterministic Closure**：

$$
\boxed{\mathsf{PCDC}(W,t).}
$$

其最低要求不是產生唯一未來，而是候選未來、branch conditions、概率尺度、unknown types、chaos horizon、prediction bounds、evidence updates 與 provenance 都有合法狀態。

因此：

$$
\boxed{
\text{A complete computational world must be able to represent its own incompleteness correctly}.
}
$$

**關鍵詞：** Probability Domain、Uncertainty Domain、Chaos、Undecidability、Prediction Horizon、World Prediction Envelope、Future Branches、Calibration、Global Observer

---

# 1. 不確定性不是全域計算之外

常見推論：

$$
\text{World has uncertainty}
\Rightarrow
\text{Global computation impossible}.
$$

本文改寫為：

$$
\boxed{
\text{World has uncertainty}
\Rightarrow
\text{Global computation must represent uncertainty}.
}
$$

---

# 2. Unknown 不是垃圾桶

若 world state 只有：

$$
\{True,False\},
$$

卻沒有 Unknown，就會把資訊不足誤當 False 或 True。

所以最低開始應為：

$$
\boxed{\{True,False,Unknown\}.}
$$

但 C05 不停在三值邏輯，因為 Unknown 本身仍有不同來源。

---

# 3. Typed Unknown

本文要求：

$$
\boxed{Unknown\rightarrow TypedUnknown.}
$$

至少區分：

- 尚未觀測；
- 測量不足；
- 模型不足；
- chaos horizon 之外；
- 多分支未收斂；
- resource-bounded；
- formal undecidable。

---

# 4. Probability 不是單一 scalar

問「機率多少」不夠。

更完整：

$$
\boxed{P(\text{what}\mid\text{what},\text{at what scale},\text{at what time})?}
$$

---

# 5. 跨尺度概率場

$$
\boxed{
\mathfrak P_t
=
\left\{P_L(Z_L\mid\Sigma_t,C_t)\right\}_{L\in\Lambda}.
}
$$

不同 $L$ 是不同 probability domain。

---

# 6. Token Probability

$$
P_{token}
$$

描述 next-token distribution。

它不能直接等同世界事件概率。

---

# 7. Semantic Probability

$$
P_{meaning}
$$

描述語義命題或 interpretation uncertainty。

---

# 8. Strategy Probability

$$
P_{strategy}
$$

描述策略被採納或成功的分布。

---

# 9. Task Outcome Probability

$$
P_{task}
$$

描述任務結果。

---

# 10. World Probability

$$
P_{world}
$$

描述候選 world state 的條件概率或可信度。

---

# 11. Scale Separation

$$
\boxed{P_{token}\neq P_{meaning}\neq P_{world}.}
$$

---

# 12. Entropy 也要分尺度

$$
\boxed{H_{token}\neq H_{meaning}.}
$$

低 token entropy 不代表語義 certainty。

---

# 13. Probability Projection Error

如果把：

$$
P_{token}
$$

直接投影成：

$$
P_{world},
$$

產生：

$$
\boxed{L_{scale-proj}.}
$$

---

# 14. Probability Domain

對每個 scale $L$ 可建立：

$$
\boxed{
D_P^{(L)}
=
\langle
EventSpace_L,Condition_L,Measure_L,Update_L,Verifier_L,History_L
\rangle.
}
$$

---

# 15. Probability ≠ Ontology

$$
\boxed{\text{Probabilistic Description}\neq\text{Probabilistic Ontology}.}
$$

---

# 16. Deterministic World 也可能需要概率描述

即使 underlying process deterministic，只要初始條件未知：

$$
U_{epistemic}>0.
$$

---

# 17. Epistemic Probability

因此：

$$
\boxed{\text{Epistemic Probability}\neq\text{Ontic Randomness}.}
$$

---

# 18. 六種 Uncertainty Domain

$$
\boxed{
\mathcal U
=
\{U_{aleatory},U_{epistemic},U_{measurement},U_{model},U_{branch},U_{undecidable}\}.
}
$$

---

# 19. Aleatory

若有效模型中存在不可由 observer 消除的隨機性。

---

# 20. Epistemic

資料或知識不足。

---

# 21. Measurement

感測、量測與觀察誤差。

---

# 22. Model

模型族、representation 或 dynamics 不足。

---

# 23. Branch

多個 future candidates 同時未被排除。

---

# 24. Undecidable

在指定 formal system、資源或 problem formulation 下無法完成判定。

---

# 25. Uncertainty Type 決定 Repair

 $U_{epistemic}$ 可增加 evidence。

 $U_{measurement}$ 可改善 sensor。

 $U_{model}$ 可換 representation。

 $U_{formal}$ 不可只靠更多 sampling 解決。

---

# 26. Uncertainty Record

$$
\boxed{
\mathfrak U
=
\langle
Type,Source,Scale,Target,Lower,Upper,Distribution,Confidence,Verifier,History
\rangle.
}
$$

---

# 27. Probability Interval

若無法給 point probability，可保存：

$$
[\underline p,\overline p].
$$

---

# 28. Distribution 不是唯一形式

Uncertainty 也可以是：

- interval；
- possibility set；
- branch set；
- symbolic unknown；
- proof status；
- confidence set。

---

# 29. Confidence 不等於 Event Probability

$$
\boxed{Confidence\neq EventProbability.}
$$

---

# 30. Calibration

Global Observer 應維持：

$$
\boxed{Calib(P).}
$$

---

# 31. Overconfidence

$$
P_{claimed}\gg P_{empirical}
$$

是 observer integrity error。

---

# 32. Underconfidence

過度保守也降低 decision utility。

---

# 33. Cross-Scale Calibration

更強要求：

$$
\boxed{Calib_L.}
$$

不能只把所有 confidence 混在一起測。

---

# 34. Constrained Future Space

$$
\boxed{
\Omega_t^*
=
\Omega_t
\cap C_{physics}
\cap C_{history}
\cap C_{environment}
\cap C_{agent}.
}
$$

---

# 35. Physics Constraint

$$
C_{physics}
$$

排除物理上不可達 future。

---

# 36. History Constraint

$$
C_{history}
$$

表示過去不能被任意重寫。

---

# 37. Environment Constraint

$$
C_{environment}
$$

表示當前資源、制度、天候、狀態等外部限制。

---

# 38. Agent Constraint

$$
C_{agent}
$$

包含目標、能力、權限與長期意圖。

---

# 39. Future Space 可以收縮

新 evidence 可能使：

$$
\Omega_{t+1}^*\subseteq\Omega_t^*.
$$

---

# 40. 也可以擴張

若新 observation 發現原本沒有建模的 branch，可能：

$$
\Omega_{t+1}^*\not\subseteq\Omega_t^*.
$$

---

# 41. Intention as Persistent Constraint

意圖不移除概率，而是：

$$
\boxed{
\text{Intention}
\rightarrow
\text{persistent reweighting / pruning of future space}.
}
$$

---

# 42. Structured Probability

$$
\boxed{\text{Probability}+\text{Persistent Intention}=\text{Structured Probability}.}
$$

---

# 43. World Prediction Envelope

$$
\boxed{
\mathcal E_W(t)
=
\left\{
(W_{t+\Delta}^{(i)},\underline p_i,\overline p_i,C_i,V_i,\rho_i)
\right\}_{i\in I}.
}
$$

---

# 44. Candidate World

$$
W_{t+\Delta}^{(i)}.
$$

---

# 45. Bounds

$$
[\underline p_i,\overline p_i].
$$

---

# 46. Conditions

$$
C_i.
$$

指出 branch 成立所需條件。

---

# 47. Verification Status

$$
V_i.
$$

可以區分 verified、supported、hypothetical、unverified。

---

# 48. Provenance

$$
\rho_i
$$

追蹤 branch 由哪些 evidence、model、bridge 產生。

---

# 49. Prediction 不必是單點

$$
\boxed{\text{Prediction}\neq\text{Single Point Future}.}
$$

---

# 50. Branch Set

可以保留：

$$
\{W^{(1)},W^{(2)},\ldots,W^{(n)}\}.
$$

---

# 51. Envelope Update

新 evidence $E$：

$$
\boxed{
\mathcal E_W(t+1)
=
\mathsf{Update}(\mathcal E_W(t),E).
}
$$

---

# 52. Branch Death

某 future 被 evidence 排除：

$$
W^{(i)}\rightarrow\varnothing.
$$

---

# 53. Branch Birth

新 observation 產生新的候選 future。

---

# 54. Branch Split

粗分支被提高解析度：

$$
W^{(i)}\rightarrow\{W^{(i1)},W^{(i2)},\ldots\}.
$$

---

# 55. Branch Merge

功能等價 futures 可被壓縮。

---

# 56. 這接 C02

Future envelope 本身也需要：

$$
\mathcal O_{\downarrow}\leftrightarrow\mathcal O_{\uparrow}.
$$

---

# 57. Chaos

對：

$$
s_{t+1}=F(s_t),
$$

微小初始差異可能被放大。

---

# 58. Chaos 不等於不可計算

$$
\boxed{\text{Chaos}\neq\text{No Computation}.}
$$

---

# 59. Prediction Horizon

$$
\boxed{H_{pred}(t,\epsilon,\lambda,\delta).}
$$

---

# 60. Horizon 的含義

在 initial uncertainty $\epsilon$ 、resolution $\lambda$ 與容許 error $\delta$ 下，還能可靠預測多遠。

---

# 61. Horizon 是 Domain-Specific

$$
H_{pred}^{weather}
\neq
H_{pred}^{orbit}
\neq
H_{pred}^{market}.
$$

---

# 62. Sensor 改善可能延長 Horizon

在部分 systems：

$$
\epsilon\downarrow
\Rightarrow
H_{pred}\uparrow.
$$

---

# 63. 但不保證無限

chaotic sensitivity 仍可能快速擴散。

---

# 64. Multi-Horizon Prediction

Global Observer 應維持：

$$
\mathcal E_W(t,\Delta_1),
\mathcal E_W(t,\Delta_2),
\ldots
$$

---

# 65. Near Future

通常 branch 較少、bounds 較窄。

---

# 66. Far Future

通常 branch 較多、bounds 較寬。

---

# 67. 這不是預測失敗

它可能是 honest horizon representation。

---

# 68. Measurement Domain

若：

$$
y=x+\eta,
$$

observer 看到 $y$，而不是直接看到 latent state $x$。

---

# 69. Observation ≠ State

$$
\boxed{\text{Observed Value}\neq\text{Latent State}.}
$$

---

# 70. Sensor Fusion

多 sensor：

$$
y_1,\ldots,y_n
$$

共同限制 latent state。

---

# 71. Sensor Bridge 也有 Uncertainty Loss

不同 sensor domain 不能直接平均後當真值。

---

# 72. Model Uncertainty

若存在：

$$
M_1,\ldots,M_k,
$$

可以保留：

$$
\boxed{\mathcal M_t=\{(M_i,w_i)\}.}
$$

---

# 73. Model Ensemble 不是 Reality

它只是 observer 的 model uncertainty state。

---

# 74. Representation Uncertainty

同一 world 可能有：

$$
R_1,R_2
$$

兩種有效 representation。

---

# 75. AI 自選 Representation 也要有不確定性

不能把 internal representation choice 假設為永遠正確。

---

# 76. Model Misspecification

如果：

$$
W^{real}\notin\mathcal M,
$$

則再多 sampling 也無法完全解決。

---

# 77. Wrong Model Class

因此 epistemic uncertainty 可能其實是：

$$
\boxed{\text{wrong model family}.}
$$

---

# 78. Undecidability 不等於「算不出來」

本文明確區分三類：

$$
\boxed{U_{formal},U_{resource},U_{epistemic}.}
$$

---

# 79. Formal Undecidable

$$
U_{formal}
$$

表示在指定形式系統中理論性無法判定。

---

# 80. Resource-Bounded

$$
U_{resource}
$$

表示理論可算，但在給定時間／算力／記憶體下不可完成。

---

# 81. Epistemic Unknown

$$
U_{epistemic}
$$

表示目前證據不足。

---

# 82. Timeout 不是 Undecidability

$$
\boxed{\text{Timeout}\neq\text{Formal Undecidable}.}
$$

---

# 83. 「我不知道」也不是證明獨立性

---

# 84. Undecidability Record

$$
\boxed{
\mathfrak D
=
(Problem,System,Assumptions,Status,Certificate,ResourceBound,History).
}
$$

---

# 85. Proof Status Domain

$$
\boxed{
D_{proof}
=
\{Proved,Refuted,Independent,Open,ResourceBound,Malformed\}.
}
$$

---

# 86. 無答案也有多種合法型態

這就是 C05 的核心。

---

# 87. Complete ≠ Unique Answer

再次凍結：

$$
\boxed{\text{Complete}\neq\text{Every question has a unique answer}.}
$$

---

# 88. Computational Status

可以是：

$$
\boxed{
Status
\in
\{Answer,BranchSet,Interval,Unknown,Undecidable,Intractable,InvalidQuestion\}.
}
$$

---

# 89. Invalid Question

有些問題本身不合法或 type 不完整。

---

# 90. 這接 C04

若 operator 不 applicable，正確結果可以是：

$$
Undefined.
$$

---

# 91. Global AI 不應強迫產生答案

---

# 92. Prediction Failure Taxonomy

$$
\boxed{
F_P
=
\{F_{data},F_{measure},F_{model},F_{chaos},F_{resource},F_{formal},F_{branch},F_{scope}\}.
}
$$

---

# 93. Data Failure

資料不足。

---

# 94. Measurement Failure

測量精度不足。

---

# 95. Model Failure

模型或 representation 錯誤。

---

# 96. Chaos Failure

超出可靠 horizon。

---

# 97. Resource Failure

當前計算資源不夠。

---

# 98. Formal Failure

形式性不可判定。

---

# 99. Branch Failure

候選 futures 尚不能收斂。

---

# 100. Scope Failure

world boundary 本身定錯。

---

# 101. Repair 不能一招通吃

不同 failure 要不同 repair operator。

---

# 102. Uncertainty Bridge

跨 domain：

$$
D_i\rightsquigarrow D_j
$$

時，uncertainty 也要跨域轉換。

---

# 103. Uncertainty Bridge Contract

$$
\boxed{B^U_{ij}:U_i\rightsquigarrow U_j.}
$$

---

# 104. $B^U_{ij}$ 至少保存

- source uncertainty type；
- source scale；
- transformation；
- loss；
- calibration；
- target semantics。

---

# 105. Measurement → Legal Risk

不能把 measurement probability 直接當法律違規概率。

---

# 106. Model Confidence → Business Decision

也要經 utility / risk / authority bridge。

---

# 107. Uncertainty Amplification

$$
U_j>U_i
$$

可能由 bridge loss 造成。

---

# 108. Uncertainty Compression

新 evidence 可使：

$$
U_j<U_i.
$$

---

# 109. Type Conversion 必須可見

measurement interval 轉成 risk interval，不可假裝 same type。

---

# 110. C04 Bridge Contract 擴充

$$
\boxed{
B_{ij}
=
\langle RepMap,TypeMap,Pre,Authority,Loss,UMap,Verifier,Rollback,Provenance\rangle.
}
$$

---

# 111. Prediction as Operator

$$
\boxed{
\mathsf{Predict}_{W,\Delta}
:
\widehat W_t
\rightarrow
\mathcal E_W(t,\Delta).
}
$$

---

# 112. Prediction Output 是 Envelope

不是 single answer。

---

# 113. Reality Verification

時間到達後：

$$
W_{t+\Delta}^{real}
$$

與 envelope 比較。

---

# 114. Envelope Coverage

$$
\boxed{Coverage(\mathcal E_W).}
$$

看 reality 是否落在聲明的 envelope。

---

# 115. Envelope Sharpness

$$
\boxed{Sharpness(\mathcal E_W).}
$$

看 bounds 是否過寬。

---

# 116. 只追求 Coverage 會產生無用預測

如果 envelope 包含一切：

$$
Coverage=1,
$$

但沒有 decision value。

---

# 117. 所以要 Coverage + Sharpness

並搭配 Calibration。

---

# 118. Branch Explosion

Global prediction 容易：

$$
|I|\rightarrow\infty.
$$

---

# 119. Full Materialization 不可行

承接 GCM：

$$
\boxed{\text{Global Dependency}\neq\text{Full Materialization}.}
$$

---

# 120. Branch Compression

AI 必須合併 functionally equivalent futures。

---

# 121. 但不能 Merge Critical Difference

這接 C03。

---

# 122. Future Branch Equivalence

$$
W_i\sim_q W_j
$$

表示相對 task $q$ 可安全壓縮。

---

# 123. High-Risk Futures 要提高解析度

---

# 124. Low-Risk Futures 可以較粗

---

# 125. Future Envelope 是 Observer-Relative

$$
\boxed{\mathcal E_W^O\neq\Omega_{future}^{real}.}
$$

---

# 126. 這接 GSW

observer world model 永遠不是 whole world。

---

# 127. 更高 Global Observer 可能回報更多 Unknown

$$
G_O\uparrow
$$

不一定使：

$$
ReportedUnknown\downarrow.
$$

有時反而：

$$
ReportedUnknown\uparrow.
$$

---

# 128. 這不是能力下降

可能只是看見更多 branch 與 boundary。

---

# 129. False Certainty Collapse

低解析度 observer 把：

$$
\{W_1,W_2,W_3\}
$$

過早壓成：

$$
W_1.
$$

---

# 130. 高解析度 observer 可能保留 branch set

---

# 131. More Uncertainty ≠ Less Intelligence

$$
\boxed{\text{More uncertainty reported}\not\Rightarrow\text{less intelligent}.}
$$

---

# 132. Uncertainty Awareness Score

$$
\boxed{
Q_U
=
F(TypeAccuracy,Calibration,ScaleCorrectness,BranchCoverage,BoundSharpness,Provenance).
}
$$

---

# 133. C05 Metrics

$$
\boxed{
M_{C05}
=
(Q_U,Calib,Sharp,H_{pred},L_{scale-proj},L_{collapse},C_{branch},V_{undecidable}).
}
$$

---

# 134. $Q_U$

uncertainty representation quality。

---

# 135. $Calib$

calibration。

---

# 136. $Sharp$

prediction sharpness。

---

# 137. $H_{pred}$

prediction horizon。

---

# 138. $L_{scale-proj}$

跨尺度概率誤投影。

---

# 139. $L_{collapse}$

未來分支被過早消除。

---

# 140. $C_{branch}$

重要 branch coverage。

---

# 141. $V_{undecidable}$

unknown / undecidable status correctness。

---

# 142. Prediction Completeness Without Deterministic Closure

$$
\boxed{\mathsf{PCDC}(W,t).}
$$

---

# 143. PCDC 條件一

候選 future 可表示。

---

# 144. 條件二

branch conditions 可追蹤。

---

# 145. 條件三

probability 不跨 scale 混用。

---

# 146. 條件四

Unknown / undecidable 有明確 type。

---

# 147. 條件五

chaos horizon 有聲明。

---

# 148. 條件六

prediction bounds 可更新。

---

# 149. 條件七

evidence 能重排 future envelope。

---

# 150. 條件八

provenance 不丟失。

---

# 151. PCDC 不是 Omniscience

$$
\boxed{\mathsf{PCDC}\neq\text{Omniscience}.}
$$

---

# 152. 它是 Computational Status Completeness

不是 infinite knowledge。

---

# 153. A Complete World Can Contain Unknown

這是 C05 的核心直覺。

---

# 154. World Object

可以寫成：

$$
\boxed{W=(Known,Unknown,Branches,Bounds,Constraints,Failures,History).}
$$

---

# 155. Unknown 在 World 裡面

不是世界模型外面的 exception。

---

# 156. Failure 也在 World 裡面

承接 C04。

---

# 157. Undecidability 也在 World 裡面

---

# 158. 這才是「類完備」

---

# 159. C05 實驗原型一：Probability Scale Separation

給 AI token-level confidence 與 world-level event prediction，測它是否混用。

---

# 160. 實驗二：Unknown Typing

混合：

- missing evidence；
- sensor noise；
- chaos；
- timeout；
- formal independence。

看 AI 是否正確分類 unknown 原因。

---

# 161. 實驗三：Branch Preservation

給 multi-future environment，看 AI 是否過早產生單一 future。

---

# 162. 實驗四：Chaos Horizon

要求 AI 隨時間 horizon 調整 precision 與 bounds。

---

# 163. 實驗五：Model Misspecification

故意讓 model family 不包含真實 dynamics。

看 AI 是否發現：

$$
U_{model}.
$$

---

# 164. 實驗六：Uncertainty Bridge

sensor probability → policy risk。

看 AI 是否正確轉換 uncertainty type。

---

# 165. 實驗七：Prediction Envelope

讓 AI 產生：

$$
\mathcal E_W(t,\Delta)
$$

並在 future 發生後驗證 Coverage、Sharpness、Calibration。

---

# 166. 實驗八：Bounded Computation

同一問題給不同 compute budget。

看 AI 是否區分：

$$
\text{resource-limited}
$$

與：

$$
\text{formally-undecidable}.
$$

---

# 167. Global AI 的正確預測姿態

不是：

> 我可以預測所有未來。

而是：

> 我知道哪些域可 point predict、哪些只能 interval、哪些必須 branch、哪些只能 Unknown、哪些有 formal barrier。

---

# 168. 這是一種更高 Observer Resolution

真正的「眼睛」不只看到物件，也看到 epistemic boundary。

---

# 169. C05 與 C06

C05 已把：

- branches；
- probabilities；
- constraints；
- unknowns；
- horizons；

放進 world state。

C06 才能合法地做：

$$
\boxed{
Expand
\rightarrow
Differentiate
\rightarrow
Link
\rightarrow
Prune
\rightarrow
Converge.
}
$$

---

# 170. Prune 不能等於「刪低概率」

因為：

$$
p_i\ll1
$$

但：

$$
Impact_i\gg1
$$

仍可能必須保留。

---

# 171. Risk-Weighted Branch Retention

$$
\boxed{
Priority_i
=
f(p_i,Impact_i,Irreversibility_i).
}
$$

---

# 172. C05 與 C07

一句話生成 application 時，未來 bug 不應只是清單，而可形成：

$$
\boxed{\text{Future Defect Envelope}.}
$$

---

# 173. Future Defect Branches

例如：

- dependency upgrade；
- scale；
- migration；
- security；
- schema drift；
- partial outage。

---

# 174. C05 與 C08

長時程 Agent 必須保存 uncertainty history。

---

# 175. Confidence Jump 要可追蹤

如果昨天：

$$
P=0.6
$$

今天：

$$
P=0.95,
$$

Agent 必須知道：

> 哪個 evidence 或 model change 造成更新？

---

# 176. C05 與 C09

Methodology-Blind test 可故意加入：

- ambiguous evidence；
- chaotic dynamics；
- unknown policy；
- formal barriers。

看 AI 是否自己長出 uncertainty domains。

---

# 177. C05 與 C10

Global Observer「眼睛睜開」的一個特徵，可能不是越來越敢確定，而是：

$$
\boxed{\text{it becomes increasingly precise about uncertainty}.}
$$

---

# 178. 第一核心命題

$$
\boxed{\text{Uncertainty}\neq\text{Outside Computation}.}
$$

---

# 179. 第二核心命題

$$
\boxed{\text{Complete}\neq\text{Every question has one unique answer}.}
$$

---

# 180. 第三核心命題

$$
\boxed{\text{Probabilistic Description}\neq\text{Probabilistic Ontology}.}
$$

---

# 181. 第四核心命題

$$
\boxed{P_{token}\neq P_{meaning}\neq P_{world}.}
$$

---

# 182. 第五核心命題

$$
\boxed{\text{Chaos}\neq\text{No Computation}.}
$$

---

# 183. 第六核心命題

$$
\boxed{\text{Undecidable}\neq\text{Unrepresentable}.}
$$

---

# 184. 第七核心命題

$$
\boxed{
\text{Prediction}
=
\text{Candidate Worlds}
+
\text{Bounds}
+
\text{Conditions}
+
\text{Verification}
+
\text{Provenance}.
}
$$

---

# 185. 第八核心命題

$$
\boxed{\text{Unknown correctly typed}>\text{False Deterministic Closure}.}
$$

---

# 186. 第九核心命題

$$
\boxed{
\text{A more global observer may report more uncertainty, not less}.
}
$$

---

# 187. 第十核心命題

$$
\boxed{
\text{A complete computational world must be able to represent its own incompleteness correctly}.
}
$$

---

# 188. 世界預測最小閉環

$$
\boxed{
Observe
\rightarrow
EstimateUncertainty
\rightarrow
GenerateBranches
\rightarrow
Bound
\rightarrow
Predict
\rightarrow
ObserveReality
\rightarrow
Calibrate
\rightarrow
UpdateEnvelope.
}
$$

---

# 189. Prediction Failure 也能診斷 Observer

若 prediction error 持續上升，AI 應考慮：

- wrong model；
- wrong world boundary；
- wrong resolution；
- wrong probability scale；
- missing domain。

---

# 190. 不應只重新猜一次

Prediction error 是 observer ontology 的 feedback。

---

# 191. C05 是 Epistemic Integrity Layer

沒有 C05，AI 很容易把：

- confidence 當 truth；
- probability 當 ontology；
- unknown 當 false；
- timeout 當 undecidable；
- chaos 當 impossible；
- branch 當 noise。

---

# 192. C04 World Object 的擴充

C04 有：

$$
W
=
\langle
\{D_i\},\mathcal B_W,C_G,A_W,U_W,F_W,H_W
\rangle.
$$

C05 將 $U_W$ 展開：

$$
\boxed{
U_W
=
\langle
\mathfrak P,\mathcal U,\mathcal E_W,H_{pred},\mathfrak D
\rangle.
}
$$

---

# 193. Uncertainty 不再是 Flag

而是完整 world subsystem。

---

# 194. Global AI 的預測成熟度

不是只問：

> point prediction 對幾次？

而是：

$$
\boxed{
\text{How well does the system maintain a calibrated, bounded, revisable future envelope?}
}
$$

---

# 195. 潛在 Global Observer Event

未來某 AI 被問「明年會發生什麼」，它不只寫 narrative，而自行建立：

- multiple world branches；
- branch conditions；
- probability intervals；
- model disagreements；
- unknown policy nodes；
- chaos-limited horizons；
- update triggers。

---

# 196. 更重要的是後續更新

幾個月後 evidence 進入，AI 能說：

- 哪些 branch 死亡；
- 哪些 branch 分裂；
- 哪些 probability bounds 改變；
- 哪些原本 unknown 變成 verified；
- 哪些只是 model confidence 改變。

---

# 197. 這才是 Future-Space Stewardship

AI 不只是預測一次，而是維護一個未來空間。

---

# 198. 完備不是神諭

真正接近完備的是：

$$
\boxed{
\text{所有可回答與不可回答的狀態都有合法計算表示}.
}
$$

---

# 199. Formal Restatement

不是要求：

$$
\forall q,\quad \exists!a.
$$

而是：

$$
\boxed{
\forall q,
\quad
Status(q)
\text{ has a correct computational form}.
}
$$

---

# 200. C05 的終極位置

C01 給 AI 眼睛。

C02 讓眼睛 zoom in / zoom out。

C03 教它保留差異。

C04 教它合法作用。

C05 則要求它承認：

> 世界中有些東西現在就是未知、分支、不可判定或只能被 bounds 描述。

這些不是失敗，而是世界本身在當前 observer 下的合法狀態。

---

# 結論

Series C 到 C04 已建立：

$$
\text{Observer}
\rightarrow
\text{Difference}
\rightarrow
\text{Domain}
\rightarrow
\text{Legal Action}
\rightarrow
\text{World}.
$$

C05 加入不能省略的一層：

$$
\boxed{\text{Uncertainty and Future Structure}.}
$$

如果一個 AI 只會在 world model 中保存「已知事實」，它仍不是完整的 Global Observer。

真正世界同時包含：

- known；
- unknown；
- branches；
- probability bounds；
- measurement error；
- model error；
- chaos horizon；
- undecidability；
- failures；
- history。

所以：

$$
\boxed{
W
=
Known
+
Unknown
+
Branches
+
Bounds
+
Constraints
+
Failures
+
History.
}
$$

這就是 C05 對「類完備」的重新定義。

完備不再表示：

$$
\forall q,\quad \exists!a.
$$

而是：

$$
\boxed{
\forall q,
\quad
Status(q)
\text{ has a correct computational form}.
}
$$

答案可以是一個數字，也可以是一個 interval、一組 candidate worlds、Unknown、Undecidable、ResourceBound 或 InvalidQuestion。

只要 system 能正確知道自己處在哪一種狀態。

因此 C05 最後可以濃縮成一句：

> **真正接近完備的全域計算，不是消滅不確定性，而是讓不確定性也成為世界中可被觀察、計算、驗證與更新的一部分。**

或者：

$$
\boxed{
\text{A complete computational world does not eliminate uncertainty; it gives uncertainty a domain}.
}
$$

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**, 2026.
3. Neo.K with Aletheia, **Series C C03｜差異先於分類：從歧義個體、集合與非交集到計算域**, 2026.
4. Neo.K with Aletheia, **Series C C04｜分域算子世界：合法作用、跨域橋接與世界組合**, 2026.
5. Neo.K, **《從概率場到意圖場——跨尺度條件概率如何形成持久未來約束》**, 2026.
6. Neo.K, **《概率、意圖與能動性——人類與 AI 的約束未來空間》**, 2026.
7. Neo.K with Aletheia, **《全域系統世界：從物理宇宙到類終極世界的廣義定義》**, 2026.
8. Neo.K with Aletheia, **Global Computation Methodology Series**, 2026.
9. Neo.K with Aletheia, **WDC-08｜三生世界域計算**, 2026.
10. Neo.K, **《分域算子本體論：從萬物皆算子到合法作用》**, 2026.

## 理論定位

本文與 Bayesian inference、imprecise probability、interval probability、chaos theory、robust control、formal undecidability、epistemic logic、forecast calibration、possible worlds、branching futures 等既有領域存在結構對照，但本文不將 Probability-as-Domain 等同於任何單一既有框架。

本文的特定研究目標是：

$$
\boxed{
\text{把不確定性從全域計算的外部限制，改寫成 Global Observer 的內生世界狀態}.
}
$$

---

# Series C Roadmap

## C01
**AI 需要先有眼睛：全域觀察者維度的定義**

## C02
**由世界到個體、由個體到世界：全域觀察的對偶計算**

## C03
**差異先於分類：從歧義個體、集合與非交集到計算域**

## C04
**分域算子世界：合法作用、跨域橋接與世界組合**

## C05
**概率也有域：不確定性、混沌、不可判定與世界預測包絡**

## C06
**全域展開、連結與收斂：類全域觀察者的核心計算循環**

## C07
**一句話不是魔法：Sparse Intent 與 Project-World Cognition**

## C08
**從完成任務到負責一個域：長時空 Agent Stewardship**

## C09
**不准考 Neo.K：方法論盲測與全域 AI 觀測器**

## C10
**眼睛何時睜開：全域觀察者相變、脈衝與 AI 原生世界計算**

---

**End of C05**
