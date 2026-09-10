# 類全域 AI 世界—計算—觀察統合系列（Paper 05）
## 域層：看見、可達、判定與驗證不是同一件事
### The Domain Layer: Observation, Reachability, Judgment, and Verification Are Not the Same Qualification

**作者：** Neo.K  
**AI 協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**系列：** 類全域 AI 世界—計算—觀察統合系列  
**英文系列名：** Global-Like AI World–Computation–Observation Synthesis Series  
**篇次：** Paper 05 / 12  
**版本：** v0.1  
**日期：** 2026-09-08  
**研究定位：** DEST × Domain-Stratified Operator Ontology × MWT Global Legality Calculus × Governed World Family × Global Observation × Global Computation × Projection Computation × Certificate-Carrying Runtime  
**前篇：** Paper 04《觀察層：Global Observer 與 Observation Operator Family》  
**狀態：** 域資格與合法作用母規格；不宣稱七域是唯一知識分類，不宣稱存在對所有跨域問題都可判定的通用 oracle

---

## 摘要

Paper 04 已建立 Global Observation State：

$$
\mathfrak O_t^G.
$$

但「已經看到了」仍然不是知識流程的終點。對一個類全域 AI 而言，下列狀態必須被嚴格區分：

- 一個對象有沒有合法定義；
- 系統是否實際觀察到它；
- 現有工具與預算是否可達它；
- 是否已具備合法判定規則；
- 是否存在可檢查的驗證證書；
- 結論是否只在局部成立；
- 局部結果是否能合法黏合成全域結果。

本文承接 Dynamic Epistemic Space Theory（DEST），將這七種資格正式嵌入 WCO-TF：

$$
\boxed{
\mathcal D_{t,\theta}
=
\left\langle
D^{def},
D^{obs},
D^{reach},
D^{judge},
D^{verify},
D^{local},
D^{global}
\right\rangle_{t,\theta}.
}
$$

其中所有資格都不是脫離條件的永久集合，而是相對條件纖維：

$$
\boxed{
\theta
=
(
\tau,
s,
t,
m,
v,
o,
b,
a,
W,
\mu
).
}
$$

分別可包含任務、尺度、時間、模型／公理後端、版本、observer、資源預算、權限、WorldId 與 world mode。

因此同一命題：

$$
p
$$

可以在：

$$
W_1
$$

中已觀察但不可判定，在：

$$
W_2
$$

中可判定但未驗證，在：

$$
W_3
$$

中只對局部成立，在：

$$
W_4
$$

中因 branch divergence 而保持多值。

本文定義 WCO 的 **Domain Qualification State（DQS）**：

$$
\boxed{
\mathfrak D_t^{WCO}
=
\left\langle
\Theta_t,
\mathcal D_t,
\mathcal G_t^{qual},
M_t^{DQF},
\Delta_t^{dom},
\mathfrak B_t^{bridge},
\Lambda_t^{leg},
\mathcal C_t^{cert},
H_t^{dom}
\right\rangle.
}
$$

其中：

- $\Theta_t$：條件空間；
- $\mathcal D_t$：七域纖維族；
- $\mathcal G_t^{qual}$：qualification gate DAG；
- $M_t^{DQF}$：Domain Qualification Fingerprint matrix；
- $\Delta_t^{dom}$：domain-transition debt；
- $\mathfrak B_t^{bridge}$：bridge / representation-navigation registry；
- $\Lambda_t^{leg}$：legality ruleset；
- $\mathcal C_t^{cert}$：certificate / blocker ledger；
- $H_t^{dom}$：domain-history / version ledger。

對任意 claim/object：

$$
x,
$$

定義多域資格指紋：

$$
\boxed{
\mathbf m_t(x\mid\theta)
=
(
M_D,
M_O,
M_R,
M_J,
M_V,
M_L,
M_G
),
}
$$

其中每一格可取：

$$
\{1,0,?,\mathsf B,\mathsf S\},
$$

分別代表通過、不通過、未決、branch-dependent、scope-dependent。

這使類全域 AI 不再把所有未知壓成：

$$
Unknown.
$$

例如：

$$
(1,1,1,1,?,1,0)
$$

表示一個對象已定義、已觀察、可達、可判定、驗證未決、局部成立，但全域黏合失敗。這與：

$$
(1,0,0,0,0,0,0)
$$

完全不是同一種「不知道」。

本文進一步引入 **Domain Transition Debt（域間轉換債務）**：

$$
\boxed{
\Delta_t^{A\rightarrow B}
=
D^A_{t,\theta}
\setminus
D^B_{t,\theta}.
}
$$

高價值債務至少包括：

$$
\Delta^{D\rightarrow J},
\quad
\Delta^{R\rightarrow J},
\quad
\Delta^{J\rightarrow V},
\quad
\Delta^{L\rightarrow G}.
$$

這些債務不是抽象距離，而是具體 proof-obligation queue：

$$
\boxed{
\mathfrak d
=
\left\langle
Id,
SourceDomain,
TargetDomain,
MissingConditions,
MissingEvidence,
MissingBridge,
ResourceEstimate,
FailureRisk,
NextAction
\right\rangle.
}
$$

因此 AI 的下一步不再只是「繼續推理」，而可以根據失敗所在域選擇：

$$
Retrieve,
Define,
Condition,
Verify,
Bridge,
Reframe,
Branch,
Defer.
$$

本文再將分域算子本體論嵌入域轉換層。對 operator：

$$
\mathcal O,
$$

本文保留：

$$
\boxed{
\operatorname{Operatorhood}
\neq
\operatorname{Applicability}
\neq
\operatorname{Executability}
\neq
\operatorname{Realization}.
}
$$

即使一個 operator 合法存在，也不表示它可以作用於任意輸入：

$$
\boxed{
\operatorname{Op}(x)
\land
\operatorname{Op}(y)
\not\Rightarrow
x(y)\downarrow.
}
$$

合法作用必須具有：

$$
\Gamma
\vdash
\mathcal O:
A\rightharpoonup B,
$$

輸入型別：

$$
\Gamma
\vdash
x:A,
$$

以及 admissibility：

$$
\Gamma;\Delta
\vdash
\mathsf{Adm}_{\mathcal O}(x).
$$

成功時：

$$
\boxed{
\Gamma;\Delta
\vdash
\mathcal O(x)
\Downarrow
y:B
\triangleright
\mathsf{Cert}.
}
$$

否則必須允許：

$$
\boxed{
\Gamma;\Delta
\vdash
\mathcal O(x)
\Downarrow
\bot[\mathsf{Reason}].
}
$$

跨域作用若不能直接合成，需要 bridge：

$$
\boxed{
\mathcal B_{B\rightsquigarrow C}
:
B\rightharpoonup C.
}
$$

且 bridge 必須聲明來源域、目標域、身份保存、資訊損失、可逆性、外部假設、證據與證書。沒有合法 bridge 時：

$$
\boxed{
\text{Potential Connection}
\neq
\text{Authorized Cross-Domain Execution}.
}
$$

本文同時接入 MWT Global Legality Calculus 的四態合法性：

$$
\boxed{
\mathbb L
=
\{
\mathsf{Legal},
\mathsf{Illegal},
\mathsf{Undetermined},
\mathsf{Conflicted}
\}.
}
$$

這四態不是 claim truth，而是 interaction admissibility state：

$$
\boxed{
\text{Legally Executable}
\neq
\text{World-Level True}.
}
$$

因此本文把三種常被混在一起的問題徹底拆開：

$$
\boxed{
\text{Epistemic Qualification}
\neq
\text{Operator Admissibility}
\neq
\text{World-Level Truth}.
}
$$

最後，本文新增 WCO Domain Layer 的一條核心防錯規則：

$$
\boxed{
\text{Representation / Projection Change}
\not\Rightarrow
\text{Epistemic Qualification Upgrade}.
}
$$

一個 claim 從 text 換成 graph、XR、數學符號、另一個 world 或另一個模型，看起來變得更清楚，不等於它從：

$$
D^{judge}
$$

自動升到：

$$
D^{verify}.
$$

真正的 qualification upgrade 必須支付相應 domain debt，並附合法 translation / bridge / verification certificate。

本文最終提出：

$$
\boxed{
\text{A Global-Like AI must know not only what it sees,}
}
$$

而且必須知道：

$$
\boxed{
\text{what epistemic qualification that observation has,
what legal transformations are still missing,
and what it is not yet entitled to claim.}
}
$$

**關鍵詞：** DEST、Domain Qualification、Judgment Domain、Verification Domain、Global Gluing、Domain Debt、Admissibility、Bridge、MWT Global Legality Calculus、Certificate、Epistemic Routing、Global AI

---

# 0. Paper 04 留下的問題

Paper 04 建立：

$$
\mathcal O_\beta
:
(B,W,D,\tau,b,\rho)
\rightharpoonup
(Y,\eta).
$$

但得到：

$$
Y
$$

後仍然要問：

> 這個 observation 有什麼知識資格？

> 能不能判？

> 能不能證？

> 是局部還是全域？

> 能不能跨表示、跨 world、跨 model 合法作用？

Paper 05 就處理這一層。

---

# 1. Known / Unknown 太粗

對 claim：

$$
p,
$$

只寫：

$$
K(p)\in\{0,1\}
$$

會抹除最重要的 next-action information。

---

# 2. 七種不同失敗

至少要分：

1. 不知道它怎麼定義；
2. 定義了但沒觀察；
3. 知道目標但目前不可達；
4. 已可達但無合法判定規則；
5. 能判但缺證書；
6. 只在局部成立；
7. 局部結果無法全域黏合。

---

# 3. 七域正式定義

$$
\boxed{
\mathcal D_{t,\theta}
=
\left\langle
D^{def},
D^{obs},
D^{reach},
D^{judge},
D^{verify},
D^{local},
D^{global}
\right\rangle.
}
$$

---

# 4. Domain 不是無條件集合

$$
D^\alpha_{t,\theta}
\subseteq
\Omega_t.
$$

---

# 5. Condition Fiber

$$
\boxed{
\theta
=
(
\tau,
s,
t,
m,
v,
o,
b,
a,
W,
\mu
).
}
$$

---

# 6. Task

$$
\tau
$$

決定需要什麼資格。

日常 recommendation 不一定要求 mathematical proof。

---

# 7. Scale

同一 claim 在不同：

$$
s
$$

下可能可判或不可判。

---

# 8. Time

$$
t
$$

改變資料 freshness、world state 與有效規則。

---

# 9. Model / Foundation

$$
m
$$

可以是：

- statistical model；
- physical model；
- axiomatic foundation；
- world-model backend。

---

# 10. Version

$$
v
$$

不同版本可能改變 domain membership。

---

# 11. Observer

$$
o
$$

不同 observer 具有不同 access。

---

# 12. Budget

$$
b
$$

直接改變：

$$
D^{reach}.
$$

---

# 13. Permission

$$
a
$$

可能限制資料與工具。

---

# 14. World

$$
W
$$

不同 world 的 evidence、mode、history 不同。

---

# 15. World Mode

$$
\mu
$$

區分：

- actual-linked；
- simulation；
- counterfactual；
- replay；
- synthetic。

---

# 16. 同一 Claim 可以跨 World 有不同資格

$$
\mathbf m_t(p\mid W_1,\theta)
\neq
\mathbf m_t(p\mid W_2,\theta).
$$

---

# 17. Definition Domain

$$
\boxed{
D^{def}_{t,\theta}
=
\{x:
\operatorname{WellTyped}(x\mid\theta)=1
\}.
}
$$

---

# 18. Defined 不等 Named

$$
\boxed{
\operatorname{Name}(x)\neq\varnothing
\not\Rightarrow
x\in D^{def}.
}
$$

---

# 19. Observation Domain

$$
\boxed{
D^{obs}_{t,\theta}
=
\{x:
\operatorname{DirectlyRegistered}(x\mid\theta)=1
\}.
}
$$

---

# 20. Observed 不等 Understood

$$
\boxed{
x\in D^{obs}
\not\Rightarrow
x\in D^{judge}.
}
$$

---

# 21. Reachability Domain

$$
\boxed{
D^{reach}_{t,\theta}
=
\left\{
x:
\exists\pi,\;
Cost(\pi)\le B,
\;
\pi:q_t\leadsto x
\right\}.
}
$$

---

# 22. Not Found 不等 Nonexistent

$$
\boxed{
x\notin D^{reach}
\not\Rightarrow
x\text{ does not exist}.
}
$$

---

# 23. Reachability 是資源相對的

$$
D^{reach}(B_1)
\neq
D^{reach}(B_2).
$$

---

# 24. 新工具可以突然擴大 Reachability

$$
D^{reach}_{t+1}
\supsetneq
D^{reach}_t.
$$

---

# 25. Judgment Domain

$$
\boxed{
D^{judge}_{t,\theta}
=
\{
p:
JudgmentRule(p\mid\theta)
\text{ sufficiently specified}
\}.
}
$$

---

# 26. Judgment 可以輸出多態

不是只有：

$$
True/False.
$$

還可以：

- conditional；
- branch-dependent；
- undetermined；
- out-of-scope。

---

# 27. 可判定不等已驗證

$$
\boxed{
D^{judge}
\neq
D^{verify}.
}
$$

---

# 28. Verification Domain

$$
\boxed{
D^{verify}_{t,\theta}
=
\{
p:
\exists c\in\mathsf{Cert},
Check(c,p,\theta)=Pass
\}.
}
$$

---

# 29. Certificate 可以多型

例如：

- formal proof；
- interval certificate；
- statistical test；
- replayable experiment；
- external theorem applicability；
- integrity certificate。

---

# 30. Numerical Agreement 不等 General Verification

有限樣本上：

$$
|f(x)-g(x)|<\varepsilon
$$

不推出：

$$
\forall x,\quad f(x)=g(x).
$$

---

# 31. Verification 必須保存 Scope

$$
\boxed{
\text{Certificate}
\neq
\text{Scope-Free Truth}.
}
$$

---

# 32. Local Domain

對 cover：

$$
\mathcal U
=
\{U_i\},
$$

有：

$$
D^{local}(U_i).
$$

---

# 33. Local Success 不等 Global Success

即使：

$$
p_i\in D^{verify}(U_i)
$$

對所有 $i$ 成立，

仍可能：

$$
p\notin D^{global}.
$$

---

# 34. Global-Gluing Domain

$$
\boxed{
D^{global}_{t,\theta}
=
\{
p:
GlueCert(p,\mathcal U,\theta)=Pass
\}.
}
$$

---

# 35. Overlap Conflict

可能：

$$
s_i|_{U_i\cap U_j}
\neq
T_{ji}
\left(
s_j|_{U_i\cap U_j}
\right).
$$

---

# 36. Loop Defect

可能：

$$
H_\gamma
\neq
id.
$$

---

# 37. Branch Non-Single-Valuedness

可能有：

$$
s^{(1)}
\neq
s^{(2)}
$$

且兩者皆合法。

正確輸出可以是：

$$
BranchDependent.
$$

---

# 38. 七域不是線性階梯

錯誤模型：

$$
D^{def}
\subseteq
D^{obs}
\subseteq
D^{reach}
\subseteq
D^{judge}
\subseteq
D^{verify}
\subseteq
D^{global}.
$$

一般不成立。

---

# 39. Qualification Gate DAG

$$
\boxed{
\mathcal G^{qual}(q,\theta)
}
$$

才是較正確表示。

---

# 40. 數學 Claim 的 Gate

可能：

$$
Definition
\rightarrow
Judgment
\rightarrow
Verification
\rightarrow
Scope.
$$

---

# 41. Data Claim 的 Gate

可能：

$$
Observation
\rightarrow
Definition
\rightarrow
Reachability
\rightarrow
Judgment
\rightarrow
Verification.
$$

---

# 42. Domain Qualification Fingerprint

$$
\boxed{
\mathbf m_t(x\mid\theta)
=
(
M_D,M_O,M_R,M_J,M_V,M_L,M_G
).
}
$$

---

# 43. Membership Value

每格：

$$
\{1,0,?,\mathsf B,\mathsf S\}.
$$

---

# 44. Branch-Dependent

$$
\mathsf B
$$

表示不同合法 branch 給不同資格。

---

# 45. Scope-Dependent

$$
\mathsf S
$$

表示只在某子域成立。

---

# 46. DQF 不等 Confidence Score

$$
\boxed{
\text{Domain Qualification Fingerprint}
\neq
\text{Scalar Confidence}.
}
$$

---

# 47. 0.82 Confidence 不能告訴你缺什麼

DQF 可以。

---

# 48. Domain Transition Debt

$$
\boxed{
\Delta_t^{A\rightarrow B}
=
D^A_{t,\theta}
\setminus
D^B_{t,\theta}.
}
$$

---

# 49. Definition-to-Judgment Debt

$$
\Delta^{D\rightarrow J}.
$$

已定義，但缺條件或判定規則。

---

# 50. Reach-to-Judgment Debt

$$
\Delta^{R\rightarrow J}.
$$

資料拿到了，但還不會判。

---

# 51. Judgment-to-Verification Debt

$$
\Delta^{J\rightarrow V}.
$$

已能合理判斷，但缺 proof / experiment / certificate。

---

# 52. Local-to-Global Debt

$$
\Delta^{L\rightarrow G}.
$$

局部都成立，但 global glue 未閉合。

---

# 53. Version Debt

舊版本有 certificate，新版本沒有。

---

# 54. Representation Debt

在表示：

$$
\Pi_1
$$

不可判，

換：

$$
\Pi_2
$$

可能可判，

但 translation 尚未合法化。

---

# 55. Debt 是 Obligation Set

$$
\boxed{
\mathfrak d
=
\left\langle
Id,
SourceDomain,
TargetDomain,
MissingConditions,
MissingEvidence,
MissingBridge,
ResourceEstimate,
FailureRisk,
NextAction
\right\rangle.
}
$$

---

# 56. Epistemic Backlog

當：

$$
D^{reach}
$$

擴張遠快於：

$$
D^{verify},
$$

形成：

$$
\boxed{
EpistemicBacklog
\approx
D^{reach}
\setminus
D^{verify}.
}
$$

---

# 57. 類全域 AI 不只是收集更多

它必須治理 backlog。

---

# 58. Domain Routing

根據 debt 類型選：

$$
Retrieve,
Define,
Condition,
Verify,
Bridge,
Reframe,
Branch,
Defer.
$$

---

# 59. Retrieve

主要提升：

$$
D^{reach}.
$$

但：

$$
\boxed{
Retrieve
\not\Rightarrow
D^{verify}.
}
$$

---

# 60. Define

把模糊 candidate 推進：

$$
D^{def}.
$$

---

# 61. Condition

補：

- scope；
- parameter；
- boundary；
- time；
- failure condition。

主要降低：

$$
\Delta^{D\rightarrow J}.
$$

---

# 62. Verify

只有合法 certificate 才能：

$$
D^{judge}
\rightarrow
D^{verify}.
$$

---

# 63. Bridge

建立中介：

$$
A
\rightarrow
B
\rightarrow
C
$$

以處理：

$$
A\not\to C.
$$

---

# 64. Reframe

$$
\Pi_1(x)
\mapsto
\Pi_2(x).
$$

---

# 65. Reframe 可以改變可判性

可能：

$$
x\notin D^{judge}(\Pi_1)
$$

但：

$$
x\in D^{judge}(\Pi_2).
$$

---

# 66. 但 Reframe 需要 Translation Certificate

$$
\boxed{
TranslationCert(\Pi_1,\Pi_2).
}
$$

---

# 67. Branch

若不同條件 branch 均合法：

$$
Branch(p)
=
\{
(T_1,J_1),
(T_2,J_2)
\}.
$$

不強迫單值化。

---

# 68. Defer

如果缺失條件短期無法補足：

$$
Defer.
$$

是合法狀態。

---

# 69. Representation Navigation Family

更一般可以包含：

$$
Fold,
Bridge,
Project,
Lift,
Compress,
Reparam,
ClassJump,
Tunnel.
$$

---

# 70. 這些都是 Candidate Navigation Operators

不是看到名字就能直接用。

---

# 71. 每個 Navigation Operator 仍需 Legality Gate

$$
\Gamma;\Delta
\vdash
\mathsf{Adm}_{\mathcal N}(x).
$$

---

# 72. Projection Change 不自動升域

$$
\boxed{
\Pi_1
\rightarrow
\Pi_2
\not\Rightarrow
D^{judge}
\rightarrow
D^{verify}.
}
$$

---

# 73. World Change 不自動升域

把 claim 放進另一個 simulated world：

$$
W_1
\rightarrow
W_2
$$

也不會自動變成 reality evidence。

---

# 74. Model Change 不自動升域

不同 model 都支持同 claim：

$$
\boxed{
\text{Model Agreement}
\neq
\text{Verification}.
}
$$

---

# 75. Observer Agreement 不自動升域

$$
\boxed{
\text{Observer Agreement}
\neq
D^{verify}.
}
$$

---

# 76. Projection Agreement 不自動升域

$$
\boxed{
\text{Projection Convergence}
\neq
\text{Evidence Independence}.
}
$$

---

# 77. Domain Upgrade 需要 Obligation Closure

$$
\boxed{
A\rightarrow B
\quad
\text{requires}
\quad
Close(\Delta^{A\rightarrow B}).
}
$$

---

# 78. 最小合法提升

AI 應求：

$$
\boxed{
\pi^\ast
=
\arg\min_\pi
C(\pi)
\quad
\text{s.t.}
\quad
TargetGate(\pi)=Pass.
}
$$

---

# 79. 不必每題都升到最高域

推薦問題可能只需：

$$
D^{judge}.
$$

新數學定理可能要求：

$$
D^{verify}.
$$

跨域大命題可能要求：

$$
D^{global}.
$$

---

# 80. 先問 Required Qualification

$$
Q_{req}(\tau).
$$

再決定 routing。

---

# 81. Operatorhood 不等 Applicability

承接分域算子本體論：

$$
\boxed{
Operatorhood
\neq
Applicability.
}
$$

---

# 82. Applicability 不等 Executability

$$
\boxed{
Applicability
\neq
Executability.
}
$$

---

# 83. Executability 不等 Realization

$$
\boxed{
Executability
\neq
Realization.
}
$$

---

# 84. Realization 不等 Truth

$$
\boxed{
Realization
\neq
WorldLevelTruth.
}
$$

---

# 85. 完整四分離

$$
\boxed{
Operatorhood
\neq
Applicability
\neq
Executability
\neq
Realization.
}
$$

---

# 86. Partial Operator

$$
\Gamma
\vdash
\mathcal O:
A\rightharpoonup B.
$$

---

# 87. Input Typing

$$
\Gamma
\vdash
x:A.
$$

---

# 88. 但 Type Correct 仍不夠

還要：

$$
\Gamma;\Delta
\vdash
Adm_{\mathcal O}(x).
$$

---

# 89. Admissibility 可以依賴

- history；
- permission；
- semantics；
- evidence；
- invariant；
- resource；
- other certificates。

---

# 90. 成功作用

$$
\boxed{
\Gamma;\Delta
\vdash
\mathcal O(x)
\Downarrow
y:B
\triangleright
Cert.
}
$$

---

# 91. 失敗也要 Typed

$$
\boxed{
\Gamma;\Delta
\vdash
\mathcal O(x)
\Downarrow
\bot[Reason].
}
$$

---

# 92. NoBridge 是一種正式 Failure

如果：

$$
Bridge_{B\rightsquigarrow C}
=
\varnothing,
$$

則：

$$
\mathcal O_2\diamond\mathcal O_1
\Downarrow
\bot[NoBridge].
$$

---

# 93. 潛在連接圖

$$
\mathcal G_{pot}.
$$

表示「可能有關係或值得找 bridge」。

---

# 94. 合法作用圖

$$
\mathcal G_{adm}^{\Gamma}.
$$

---

# 95. 實現轉換圖

$$
\mathcal G_{real}^{\Gamma,\Delta}.
$$

---

# 96. 三圖通常滿足

$$
\boxed{
E_{real}^{\Gamma,\Delta}
\subseteq
E_{adm}^{\Gamma}
\subseteq
E_{pot}.
}
$$

---

# 97. Potential Connection 不等 Direct Execution

$$
\boxed{
PotentialConnection
\neq
AdmissibleAction.
}
$$

---

# 98. Bridge Operator

若：

$$
\mathcal O_1:
A\rightharpoonup B
$$

而：

$$
\mathcal O_2:
C\rightharpoonup D,
$$

需要：

$$
\boxed{
\mathcal B_{B\rightsquigarrow C}
:
B\rightharpoonup C.
}
$$

---

# 99. Certified Composition

$$
\mathcal O_2
\diamond_{\mathcal B}
\mathcal O_1
=
\mathcal O_2
\circ
\mathcal B
\circ
\mathcal O_1.
$$

---

# 100. Bridge 不是免費轉換

必須聲明：

- source；
- target；
- semantics；
- identity；
- invertibility；
- loss；
- assumptions；
- evidence；
- failure；
- certificate。

---

# 101. 可以翻譯不等翻譯後可以作用

$$
\boxed{
\text{Translatable}
\neq
\text{Operationally Admissible After Translation}.
}
$$

---

# 102. Type Compatibility 不是充分條件

即使：

$$
Cod(\mathcal O_1)
\sim
Dom(\mathcal O_2),
$$

仍可能因 history、semantics、invariant、permission、evidence、loss 而失敗。

---

# 103. Type Compatibility 不等 Refinement Compatibility

$$
\boxed{
\text{Base Type Match}
\neq
\text{Refinement Match}.
}
$$

---

# 104. Composition 通常不交換

$$
\mathcal O_2\diamond\mathcal O_1
\not\simeq
\mathcal O_1\diamond\mathcal O_2.
$$

---

# 105. Composition 也不自動結合

$$
(\mathcal O_3\diamond\mathcal O_2)\diamond\mathcal O_1
$$

不必等於：

$$
\mathcal O_3\diamond(\mathcal O_2\diamond\mathcal O_1).
$$

---

# 106. Local Legality 不等 Path Legality

$$
\boxed{
Legal(A)
\land
Legal(B)
\not\Rightarrow
Legal(B\circ A).
}
$$

---

# 107. Constraint Validity 不等 Joint Satisfiability

每個 constraint 都合法：

$$
X_i,
$$

仍可能：

$$
\bigcap_iD_{X_i}
=
\varnothing.
$$

---

# 108. Unsatisfiable 不等 Illegal Rule

$$
\boxed{
RuleValidity
\neq
JointSatisfiability.
}
$$

---

# 109. MWT Global Legality Judgment

對 interaction episode：

$$
\alpha,
$$

判定：

$$
\boxed{
\Gamma
\vdash
\alpha
\Downarrow_{\Lambda}
\ell.
}
$$

---

# 110. 四態 Legality

$$
\boxed{
\ell
\in
\{
Legal,
Illegal,
Undetermined,
Conflicted
\}.
}
$$

---

# 111. Legal

足夠正向 support，且沒有有效 blocker。

---

# 112. Illegal

存在有效 blocker。

---

# 113. Undetermined

正向證書與 blocker 都不足。

---

# 114. Conflicted

同時存在未解消的正向與阻斷鏈。

---

# 115. Conflicted 不等 True and False

它只表示 legality evidence conflict。

---

# 116. Hard Gate 不能 Majority Vote

十四個 gate 過，一個 hard type gate fail：

$$
\boxed{
\text{仍然 Illegal}.
}
$$

---

# 117. Admissibility 先於 Optimization

$$
\boxed{
Admissibility
\prec
Optimization.
}
$$

---

# 118. Fast / Cheap / Pretty 都不能補回 Illegal

performance 不是 legality。

---

# 119. 高價值 Hard Gates

MWT-02 提供：

- WellFormed；
- Version；
- SourceDomain；
- Bridge；
- Type；
- Identity；
- Semantic；
- Context；
- Constraint；
- Invariant；
- HistoryOrder；
- Permission；
- Resource；
- Certificate；
- Realization。

---

# 120. WCO Domain Layer 不必每次跑十五 Gate

required subset：

$$
G_{req}(\alpha)
$$

由 operator / world / task / mode 決定。

---

# 121. Gate Record

每個 gate 應保存：

$$
R_i
=
(
s_i,
r_i,
C_i^+,
C_i^-,
v_i,
h_i
).
$$

---

# 122. Certificate 有 Validity Horizon

$$
h_i.
$$

過期後不能無條件沿用。

---

# 123. Legality 不等 Truth

即使：

$$
Legal(derive\;\varphi),
$$

不推出：

$$
True_W(\varphi).
$$

---

# 124. 最多先得到相對 Foundation 的結果

例如：

$$
T\vdash\varphi
$$

或：

$$
M\models\varphi.
$$

---

# 125. Epistemic Qualification 不等 Operator Legality

claim 是否 Verified 和 operator 是否 Legal 是兩個 axes。

---

# 126. Domain–Legality Matrix

本文提出：

$$
\boxed{
\mathsf{DLM}(x,\alpha)
=
\left(
\mathbf m_t(x\mid\theta),
\ell_\alpha
\right).
}
$$

---

# 127. 一個 Claim 可以 Verified，但某 Action Illegal

例如證明已成立，但沒有權限修改 production world。

---

# 128. 一個 Action 可以 Legal，但 Claim 未 Verified

例如 sandbox simulation 合法，但輸出只屬：

$$
D^{judge}.
$$

---

# 129. Domain-Legality Orthogonality

$$
\boxed{
\text{Epistemic Qualification}
\neq
\text{Execution Admissibility}.
}
$$

---

# 130. 第三軸：Truth / Reality Status

還要另分：

$$
\mathsf T_W(x).
$$

---

# 131. 三軸不能坍縮

$$
\boxed{
\text{Qualification}
\neq
\text{Legality}
\neq
\text{Truth}.
}
$$

---

# 132. WCO Domain Qualification State

本文定義：

$$
\boxed{
\mathfrak D_t^{WCO}
=
\left\langle
\Theta_t,
\mathcal D_t,
\mathcal G_t^{qual},
M_t^{DQF},
\Delta_t^{dom},
\mathfrak B_t^{bridge},
\Lambda_t^{leg},
\mathcal C_t^{cert},
H_t^{dom}
\right\rangle.
}
$$

---

# 133. Qualification Graph

$$
\mathcal G_t^{qual}
$$

依 task 建立，不是固定 linear chain。

---

# 134. Bridge Registry

$$
\mathfrak B_t^{bridge}
$$

保存：

- bridge id；
- source；
- target；
- loss；
- scope；
- evidence；
- certificate；
- version。

---

# 135. Legality Ruleset

$$
\Lambda_t^{leg}.
$$

必須 versioned。

---

# 136. Certificate Ledger

$$
\mathcal C_t^{cert}.
$$

append-only history 可以與 active status 分離。

---

# 137. 活動判定可以非單調

新 evidence 可以讓：

$$
Verified
\rightarrow
Invalidated
$$

或：

$$
Global
\rightarrow
ScopeRestricted.
$$

---

# 138. 證書歷史仍保留

$$
\boxed{
\text{Certificate History Can Be Monotone,}
}
$$

但：

$$
\boxed{
\text{Active Qualification Need Not Be Monotone}.
}
$$

---

# 139. Domain Patch

理論更新可以改：

- definition；
- reachability；
- judgment；
- verification；
- global glue。

---

# 140. Patch 必須聲明 Domain Effect

例如：

```yaml
domain_effect:
  definition: expand
  observation: same
  reachability: expand
  judgment: same
  verification: shrink
  local: same
  global_gluing: unknown
```

---

# 141. 理論進步不等所有 Domain 都擴大

某次修正可能縮小 scope，反而更正確。

---

# 142. Domain Upgrade 不等 Model Fit Improvement

$$
\boxed{
\text{Better Fit}
\neq
\text{Higher Epistemic Qualification}.
}
$$

---

# 143. Qualification Capsule

本文提出：

$$
\boxed{
\mathsf{QCap}(p)
=
\left\langle
Claim,
WorldId,
ConditionFiber,
DQF,
Judgment,
Evidence,
Legality,
Scope,
Debt,
Certificates,
ReopenTriggers
\right\rangle.
}
$$

---

# 144. AI Output 不應只有 Answer

重要輸出應能攜帶：

$$
\mathsf{QCap}(p).
$$

---

# 145. 對一般用戶可以投影簡化版

但 canonical state 應保留完整 capsule。

---

# 146. UI 的「已驗證」標籤必須有 Certificate Ref

否則只能標：

- observed；
- inferred；
- simulated；
- judged；
- unverified。

---

# 147. 表示逃逸不能洗白證據

如果：

$$
p
$$

在 text 中未驗證，

換成漂亮 graph：

$$
\Pi_{graph}(p)
$$

仍然未驗證。

---

# 148. Simulation World 不能洗白 Evidence

$$
p\in D^{verify}(W^{sim})
$$

也不直接推出：

$$
p\in D^{verify}(\mathcal R).
$$

---

# 149. Formal Proof 也不能替代 Empirical Scope

若 claim 是物理／經驗命題：

形式證明只能證 relative model implication。

---

# 150. Empirical Evidence 也不能自動替代 Formal Universality

有限觀察不能直接推出 universal theorem。

---

# 151. Domain Layer 的核心是拒絕 Qualification Laundering

本文定義：

$$
\boxed{
\text{Qualification Laundering}
=
\text{未支付 domain debt，卻透過表示、語言、模型、
world 或 authority 變換宣稱更高 epistemic status}.
}
$$

---

# 152. 五種常見 Laundering

1. Observed → Verified；
2. Simulated → Real；
3. Model Agreement → Independent Evidence；
4. Local → Global；
5. Legal Execution → True Claim。

---

# 153. Laundering Guard

$$
\boxed{
\mathsf{QLGuard}
:
\mathsf{TransitionClaim}
\rightarrow
\{Pass,Block,Undetermined,Conflict\}.
}
$$

---

# 154. Guard 檢查

- source domain；
- target domain；
- debt closure；
- bridge；
- certificate；
- scope；
- world mode；
- provenance。

---

# 155. Domain Router

$$
\boxed{
\mathsf{DRouter}
:
(
\mathsf{QCap},
Q_{req},
B,
Risk
)
\rightarrow
NextAction.
}
$$

---

# 156. NextAction 可以是

$$
Retrieve,
Define,
Condition,
Verify,
Bridge,
Reframe,
Branch,
Defer,
Stop.
$$

---

# 157. Stop 也可以合法

如果任務只需：

$$
D^{judge}
$$

而已經通過，

就不必浪費成本升到：

$$
D^{global}.
$$

---

# 158. Risk 可以提高 Required Qualification

高風險 decision：

$$
Q_{req}
$$

可以從：

$$
Judge
$$

提升到：

$$
Verify
$$

甚至：

$$
Global.
$$

---

# 159. Authority 不能降低 Epistemic Requirement

有權限的人說「可以」：

$$
\boxed{
\text{Authority}
\neq
\text{Verification}.
}
$$

---

# 160. Verification 也不能自動給 Authority

$$
\boxed{
\text{Verified}
\neq
\text{Authorized to Act}.
}
$$

---

# 161. Domain Layer 與 Paper 02 World Layer

每個 world：

$$
W_i
$$

有自己的 claim domain state。

---

# 162. Cross-World Qualification

$$
\mathbf m(p\mid W_i)
\neq
\mathbf m(p\mid W_j).
$$

---

# 163. Cross-World Transport 必須標記 Domain Effect

例如：

$$
W^{sim}
\rightarrow
W^{AL}
$$

只能把：

$$
Verified_{sim}
$$

轉成：

$$
Candidate_{AL}
$$

除非有額外 reality validation。

---

# 164. Domain Layer 與 Paper 03 Computation Layer

computation result：

$$
\Delta^{cand}
$$

只獲得其 route 能支持的 qualification。

---

# 165. Approximate Solver 不應產生 Exact Verification Label

除非 error certificate 足以支撐 required claim。

---

# 166. Domain Layer 與 Paper 04 Observation Layer

observation：

$$
Y
$$

先進：

$$
D^{obs}.
$$

不自動進：

$$
D^{judge}
$$

或：

$$
D^{verify}.
$$

---

# 167. WCO 四層現在形成

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}.
}
$$

---

# 168. 但 Domain Layer 也會回饋前面三層

若：

$$
\Delta^{R\rightarrow J}
$$

很大，

需要改 observation / computation。

---

# 169. 若缺 Evidence

可能要求：

$$
Reobserve.
$$

---

# 170. 若缺 Bridge

可能要求：

$$
Reframe
$$

或：

$$
BridgeSearch.
$$

---

# 171. 若 Local-to-Global Debt 太大

可能要求新增 world / domain / observer。

---

# 172. Domain Feedback Loop

$$
\boxed{
\mathfrak D
\rightarrow
\mathfrak O
\rightarrow
\mathfrak C
\rightarrow
\mathfrak W
\rightarrow
\mathfrak D'.
}
$$

---

# 173. MVP：Claim Qualification Runtime

沿用四世界：

$$
W_A,W_B,W_C,W_N.
$$

---

# 174. 每個 World 產生同一類 Claim

例如：

$$
p_i:
\text{Policy }i\text{ avoids threshold failure}.
$$

---

# 175. 初始 DQF

simulation 後可能：

$$
(1,1,1,1,?,1,?).
$$

---

# 176. Verification Stage

加入：

- repeated simulation；
- independent backend；
- formal invariant check；
- real evidence。

---

# 177. DQF 更新

不同 evidence 只更新相應 domains。

---

# 178. 不允許一次更新全部七格

除非 certificate 明確支持。

---

# 179. Bridge Test

將 graph result 轉成 symbolic constraint。

需要：

$$
TranslationCert.
$$

---

# 180. NoBridge Test

故意移除 translation contract。

runtime 應：

$$
Block.
$$

---

# 181. Laundering Test

讓 UI 嘗試把：

$$
Judged
$$

顯示成：

$$
Verified.
$$

QLGuard 必須拒絕。

---

# 182. Local-to-Global Test

三個 local regions 都通過，

但 overlap conflict。

全域 gate 必須 fail。

---

# 183. Branch-Dependent Test

兩個 foundation / model branches 產生不同 legal judgment。

系統保留：

$$
\mathsf B.
$$

---

# 184. Legality Four-State Test

建立：

- Legal；
- Illegal；
- Undetermined；
- Conflicted；

四種 interaction。

---

# 185. Hard-Gate Test

十四個 soft/positive checks 過，

一個 type hard gate fail。

結果必須：

$$
Illegal.
$$

---

# 186. 實驗一：Scalar Confidence vs DQF

比較 AI 下一步 routing quality。

---

# 187. 實驗二：Known/Unknown vs Seven-Domain State

測是否降低錯誤重試與無效搜尋。

---

# 188. 實驗三：Qualification Laundering

故意混入：

- simulation；
- pretty visualization；
- model consensus；
- local proof。

測 Guard。

---

# 189. 實驗四：Bridge Registry

比較 explicit bridge 與 ad hoc conversion。

---

# 190. 實驗五：Domain Debt Routing

比較：

$$
RandomNextStep
$$

與：

$$
DebtAwareRouting.
$$

---

# 191. 實驗六：Version Migration

舊版 certificate 不自動升級新版 claim。

---

# 192. 實驗七：Global Glue

局部都 verify，但 closed-loop defect。

測 global gate。

---

# 193. 實驗八：Legality vs Truth

建立合法推理但 false premise / wrong model case。

確認 runtime 不把 Legal 標成 WorldTrue。

---

# 194. 實驗九：Authority vs Verification

建立 authorized but unverified action 與 verified but unauthorized action。

確認兩軸分離。

---

# 195. 實驗十：Minimal Qualification

不同 risk/task 指定：

$$
Q_{req}.
$$

測是否降低不必要 verification cost。

---

# 196. 可反駁性

本文會被削弱，如果：

1. 七域 DQF 對 routing / error diagnosis 沒有比 scalar confidence 更好；
2. domain debt 無法改善下一步選擇；
3. qualification laundering 在實務中極少造成錯誤；
4. explicit bridge registry 比 ad hoc conversion 沒有可測價值；
5. Local / Global 分離無法改善 cross-domain correctness；
6. Legality / Truth / Authority 三軸分離沒有工程收益；
7. simpler Known/Unknown + confidence system 在代表性任務中完全等效。

---

# 197. 本文不主張什麼

本文不主張：

1. 七域是唯一完整知識分類；
2. 七域形成固定線性順序；
3. 所有 unknown 都能被解除；
4. verification 永遠單調；
5. local/global 一定有標準 sheaf structure；
6. 所有跨域 bridge 都存在；
7. Fold / Lift / Tunnel 等 navigation 永遠合法；
8. 換 representation 必然提高可判性；
9. DQF 是真理機率；
10. Legal 表示 claim true；
11. Verified 表示 authorized；
12. Authorized 表示 verified；
13. simulation verification 等於 reality verification；
14. formal proof 自動替代 empirical evidence；
15. empirical evidence 自動替代 universal proof；
16. MWT GLC 是 universal decision procedure；
17. Conflicted 表示命題同時真與假；
18. AI 可以為了完成任務臨時虛構 bridge；
19. AI 可以補入無來源權重；
20. 本文已完成 production epistemic runtime。

---

# 198. 核心非同一性

$$
\boxed{
Defined
\neq
Observed
\neq
Reachable
\neq
Judgeable
\neq
Verified
\neq
Local
\neq
Global.
}
$$

$$
\boxed{
Observation
\neq
Judgment
\neq
Verification.
}
$$

$$
\boxed{
Operatorhood
\neq
Applicability
\neq
Executability
\neq
Realization.
}
$$

$$
\boxed{
PotentialConnection
\neq
AdmissibleAction.
}
$$

$$
\boxed{
Translatable
\neq
OperationallyAdmissible.
}
$$

$$
\boxed{
LocalValidity
\not\Rightarrow
GlobalValidity.
}
$$

$$
\boxed{
Legality
\neq
Truth
\neq
Authority.
}
$$

$$
\boxed{
RepresentationChange
\not\Rightarrow
EpistemicUpgrade.
}
$$

---

# 199. 核心母式一：七域

$$
\boxed{
\mathcal D_{t,\theta}
=
\left\langle
D^{def},
D^{obs},
D^{reach},
D^{judge},
D^{verify},
D^{local},
D^{global}
\right\rangle.
}
$$

---

# 200. 核心母式二：DQF

$$
\boxed{
\mathbf m_t(x\mid\theta)
=
(
M_D,
M_O,
M_R,
M_J,
M_V,
M_L,
M_G
).
}
$$

---

# 201. 核心母式三：Domain Debt

$$
\boxed{
\Delta_t^{A\rightarrow B}
=
D^A_{t,\theta}
\setminus
D^B_{t,\theta}.
}
$$

---

# 202. 核心母式四：Legal Operator

$$
\boxed{
\Gamma;\Delta
\vdash
\mathcal O(x)
\Downarrow
y:B
\triangleright
Cert.
}
$$

---

# 203. 核心母式五：Legality State

$$
\boxed{
\mathbb L
=
\{
Legal,
Illegal,
Undetermined,
Conflicted
\}.
}
$$

---

# 204. 核心母式六：WCO Domain State

$$
\boxed{
\mathfrak D_t^{WCO}
=
\left\langle
\Theta_t,
\mathcal D_t,
\mathcal G_t^{qual},
M_t^{DQF},
\Delta_t^{dom},
\mathfrak B_t^{bridge},
\Lambda_t^{leg},
\mathcal C_t^{cert},
H_t^{dom}
\right\rangle.
}
$$

---

# 205. 核心母式七：Qualification Capsule

$$
\boxed{
\mathsf{QCap}(p)
=
\left\langle
Claim,
WorldId,
ConditionFiber,
DQF,
Judgment,
Evidence,
Legality,
Scope,
Debt,
Certificates,
ReopenTriggers
\right\rangle.
}
$$

---

# 206. 結論：類全域 AI 必須知道「自己還沒有資格說什麼」

一個 AI 能看到：

$$
Y
$$

不表示它能判：

$$
J(Y).
$$

能判：

$$
J(Y)
$$

不表示它已驗證：

$$
V(Y).
$$

局部都通過：

$$
V_i(Y)
$$

也不表示全域可以合法黏合。

同樣地，一個 operator 存在，不表示它能作用；能作用，不表示能在當前 runtime 執行；能執行，也不表示外部世界已實現；即使 interaction 合法，也不表示輸出 claim 自動為真。

所以真正成熟的類全域 AI 不能只有：

> 「我覺得答案是 X，confidence 0.91。」

它應該能知道：

> 我已經定義到哪裡？

> 我真的觀察到什麼？

> 哪些東西只是可達？

> 哪些命題只是可判？

> 哪些已經有 certificate？

> 哪些只在局部成立？

> 哪些全域仍有 glue debt？

> 哪條 bridge 還沒證？

> 哪個 interaction 是 Undetermined？

> 我現在只是沒有證據，還是根本沒有合法作用？

更重要的是，它必須能說：

$$
\boxed{
\text{I am not yet entitled to upgrade this claim.}
}
$$

因此 Paper 05 的核心不是讓 AI 「更保守」。

而是讓 AI 的不確定性與能力缺口變得**有結構、可定位、可派工、可驗證**。

本文最終提出：

$$
\boxed{
\text{Global Intelligence}
\text{ requires qualification-aware cognition}.
}
$$

以及：

$$
\boxed{
\text{A Global-Like AI must know
not only what it sees,
but what epistemic qualification that observation has,
what legal transformations are still missing,
and what it is not yet entitled to claim.}
}
$$

到此，WCO 已形成：

$$
\boxed{
\mathfrak W_t^G
\rightarrow
\mathfrak C_t^{WF}
\rightarrow
\mathfrak O_t^G
\rightarrow
\mathfrak D_t^{WCO}.
}
$$

下一篇將進入：

# Paper 06
## 投影層：AI 如何自行選擇 Computational Way of Seeing

也就是把 Domain Layer 的 qualification、Global Observer 的 operator selection、Projection Computation 的 finite views、CPC 與 PNCW 正式合成一個 **AI-native Projection Compiler Layer**。

---

# 207. 下一篇接口

Paper 06 將處理：

- observation content → projection；
- task-relative projection；
- finite views；
- projection family；
- carrier selection；
- CPC；
- AI-native view；
- observer-aware projection；
- representation escape；
- projection debt；
- translation certificate；
- adaptive reprojection；
- new carrier generation；
- computational way of seeing；
- projection selection vs observation selection；
- Designed Perception vs Designed Truth。

---

# 參考文獻與內部前置研究

## EveMissLab / Neo.K

1. Neo.K × Aletheia，《DEST-01｜多域知識判定論》，2026。
2. Neo.K，《分域算子本體論：從萬物皆算子到合法作用》，2026。
3. Neo.K × Aletheia，《MWT-02｜Global Legality Calculus》，2026。
4. Neo.K，《Mathematical World Theory v0.1》，2026。
5. Neo.K × Aletheia，《DEST-09｜表示逃逸與解空間導航 2.0》，2026。
6. Neo.K × Aletheia，《投影計算論》，2026。
7. Neo.K × Aletheia，《WCO Paper 01》，2026。
8. Neo.K × Aletheia，《WCO Paper 02》，2026。
9. Neo.K × Aletheia，《WCO Paper 03》，2026。
10. Neo.K × Aletheia，《WCO Paper 04》，2026。
11. Neo.K × Aletheia，《Global Observer Series C》，2026。
12. Neo.K × Aletheia，《WDC / SWFR》，2026。

## External Mathematical / Engineering Interfaces

13. Martin-Löf, P. (1984). *Intuitionistic Type Theory*. Bibliopolis.
14. Pierce, B. C. (2002). *Types and Programming Languages*. MIT Press.
15. Freeman, T., & Pfenning, F. (1991). *Refinement Types for ML*. PLDI.
16. Nielson, F., Nielson, H. R., & Hankin, C. (1999). *Principles of Program Analysis*. Springer.
17. Cousot, P., & Cousot, R. (1977). *Abstract Interpretation: A Unified Lattice Model for Static Analysis*. POPL.
18. Abramsky, S., & Jung, A. (1994). *Domain Theory*. Handbook of Logic in Computer Science.
19. Mac Lane, S., & Moerdijk, I. (1992). *Sheaves in Geometry and Logic*. Springer.
20. Belnap, N. D. (1977). *A Useful Four-Valued Logic*. In Modern Uses of Multiple-Valued Logic.

---

**Paper 05 狀態：COMPLETE v0.1**  
**下一篇：Paper 06 — 投影層：AI 如何自行選擇 Computational Way of Seeing**  
**Canonical source：UTF-8 Markdown；數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`。**
