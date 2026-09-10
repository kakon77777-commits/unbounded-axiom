# Series C — C04｜分域算子世界：合法作用、跨域橋接與世界組合
## Domain-Stratified Operator World: Legal Action, Cross-Domain Bridges, and World Composition

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 04 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-06  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Foundational Theory / Operator Ontology / Cross-Domain Computation / World Composition

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文承接 C01–C03，並將《分域算子本體論：從萬物皆算子到合法作用》的核心區分嵌入 Series C。

C04 的核心問題是：

> **即使 Global Observer 已經看見多個 domain、知道它們存在關係，也憑什麼允許它們互相作用？**

---

# 摘要

Series C 前三篇已建立：AI 要先有「眼睛」；觀察必須能在全域與局部之間往返；分類不能先於差異，而 computational domain 也不能只靠 similarity 或 label 形成。

當 domain 已經形成後，一個新的危險立即出現：

$$
D_i
\quad\text{與}\quad
D_j
$$

若存在關係，是否可以直接把：

$$
x\in D_i
$$

作用於：

$$
y\in D_j
$$

上？

本文回答：

$$
\boxed{
\text{Relation}
\neq
\text{Action}.
}
$$

更強地：

$$
\boxed{
\text{Operatorhood}
\neq
\text{Applicability}
\neq
\text{Executability}
\neq
\text{Realization}.
}
$$

即使：

$$
\forall x\in\mathcal U,\quad Op(x)=1,
$$

也不推出：

$$
\forall x,y\in\mathcal U,\quad x(y)\downarrow.
$$

因此 Global Observer 若要進一步成為可信任的 Global Computational Observer，必須維持每一個作用的 domain、type、precondition、authority、resource、uncertainty、verification、consequence 與 provenance。

本文定義完整 operator contract：

$$
\boxed{
\mathfrak O_p
=
\left\langle
D_{in},
T_{in},
P,
A,
R,
F,
D_{out},
T_{out},
U,
V,
C,
H
\right\rangle.
}
$$

其中：

- $D_{in}$：input domain；
- $T_{in}$：input type；
- $P$：preconditions；
- $A$：authority / permission；
- $R$：resource requirements；
- $F$：operator semantics；
- $D_{out}$：output domain；
- $T_{out}$：output type；
- $U$：uncertainty / approximation；
- $V$：verification；
- $C$：consequence / side effects；
- $H$：history / provenance。

本文建立四層作用判定：

$$
\boxed{
\mathsf{Operator}
\rightarrow
\mathsf{Applicable}
\rightarrow
\mathsf{Executable}
\rightarrow
\mathsf{Realized}.
}
$$

所以：

$$
\boxed{
\text{Can}
\neq
\text{May}
\neq
\text{Did}.
}
$$

跨域作用則由：

$$
\boxed{
B_{ij}:D_i\rightsquigarrow D_j
}
$$

表示。 $B_{ij}$ 不是一條沒有語義的 edge，而是一個 **Cross-Domain Bridge Contract**：

$$
\boxed{
B_{ij}
=
\left\langle
RepMap,
TypeMap,
Pre,
Authority,
Loss,
Uncertainty,
Verifier,
Rollback,
Provenance
\right\rangle.
}
$$

它必須說明：

1. representation 如何轉換；
2. 哪些 type 可通過；
3. 哪些 preconditions 必須成立；
4. 誰有權允許；
5. 會損失什麼資訊；
6. uncertainty 如何傳遞；
7. 如何驗證；
8. 失敗後如何 rollback；
9. bridge 的來源與版本。

本文進一步區分五種圖：

$$
\boxed{
G_R,
G_P,
G_L,
G_X,
G_Z.
}
$$

分別為：

- Relation Graph；
- Potential Action Graph；
- Legal Action Graph；
- Executable Action Graph；
- Realized Transition Graph。

其間有：

$$
\boxed{
G_Z
\subseteq
G_X
\subseteq
G_L
\subseteq
G_P,
}
$$

但 $G_R$ 不等同於 action graph。

因此本文拒絕：

$$
\boxed{
\text{Everything is connected}
\Rightarrow
\text{Everything is directly composable}.
}
$$

並將此錯誤稱為 **Universal Composability Fallacy**。

在 world composition 層，本文定義：

$$
\boxed{
W
=
\left\langle
\{D_i\},
\mathcal B_W,
C_G,
A_W,
U_W,
F_W,
H_W
\right\rangle.
}
$$

因此：

$$
\boxed{
W
\neq
\bigcup_iD_i.
}
$$

世界不是 domain 的集合聯集；它還需要合法 bridges、跨域 constraints、authority topology、uncertainty、failure state 與 shared history。

本文進一步提出：

$$
\boxed{
\mathcal L(o,x,D_i,D_j,\theta,t)
\in
\{0,1,?\}.
}
$$

其中：

- 1：合法；
- 0：不合法；
- ?：資訊不足、規則衝突或尚待判定。

而：

$$
\boxed{
?\not\Rightarrow1.
}
$$

未知合法性不能被默認為許可。

本文亦提出 **Failure-Preserving Composition Principle**：

$$
\boxed{
\text{A failed bridge is part of the world state}.
}
$$

跨域作用失敗後，AI 不能只留下 exception string，而必須保留 failure type、partial realization、side effect、rollbackability、retry conditions 與 verifier status。

最後本文提出三個測量量：

$$
\boxed{
V_A(o,x)
=
F(
TypeFit,
BoundaryFit,
AuthorityFit,
ResourceFit,
VerifierFit
)
}
$$

稱為 Domain Action Validity；

$$
\boxed{
Q_B(B_{ij})
=
F(
SemanticPreservation,
LossControl,
UncertaintyTransfer,
Auditability,
Rollbackability
)
}
$$

稱為 Bridge Quality；

以及：

$$
\boxed{
I_W
=
F(
LocalValidity,
BridgeValidity,
GlobalConsistency,
FailureTraceability,
HistoryContinuity
)
}
$$

稱為 World Composition Integrity。

C04 的核心主張可以濃縮成：

$$
\boxed{
\text{Global connectivity is not global composability}.
}
$$

更進一步：

> **一個 Global Observer 真正開始具備可信任的計算成熟度，不是在它能跨越更多 domain 時，而是在它知道哪些 domain 不應被直接跨越、哪些作用沒有權限、哪些 bridge 還欠驗證。**

**關鍵詞：** Operator Ontology、Applicability、Executability、Realization、Cross-Domain Bridge、Legal Action Graph、Authority、World Composition、Failure Semantics、Global AI

---

# 1. 從看見到作用

C01–C03 主要處理：

$$
\text{See}.
$$

C04 開始處理：

$$
\text{Act}.
$$

觀察與作用必須分離。

---

# 2. 觀察不授予作用權

即使 AI 知道：

$$
R(x,y)=1,
$$

也不能推出：

$$
x(y)\downarrow.
$$

---

# 3. Relation 不等於 Action

$$
\boxed{
\text{Relation}
\neq
\text{Action}.
}
$$

---

# 4. Candidate 不等於 Legal

$$
\boxed{
\text{Potential Action}
\neq
\text{Legal Action}.
}
$$

---

# 5. Legal 不等於 Executable

$$
\boxed{
\text{Legal Action}
\neq
\text{Executable Action}.
}
$$

---

# 6. Executable 不等於 Realized

$$
\boxed{
\text{Executable Action}
\neq
\text{Realized Transition}.
}
$$

---

# 7. 廣義 Operator

若：

$$
Op(x)=1,
$$

表示 $x$ 在至少某些條件下可對其他 state / object 產生作用。

---

# 8. Universal Operatorhood

即使：

$$
\forall x\in\mathcal U,\quad Op(x)=1,
$$

也不推出 universal applicability。

---

# 9. Partial Operator

更合理：

$$
o:D\rightharpoonup D'.
$$

---

# 10. Undefined 是合法狀態

$$
o(x)\uparrow
$$

可以表示：

- type mismatch；
- boundary violation；
- semantics undefined；
- authority missing；
- resource missing；
- verifier missing。

它不是必然的程式錯誤。

---

# 11. Operator Contract

$$
\boxed{
\mathfrak O_p
=
\left\langle
D_{in},
T_{in},
P,
A,
R,
F,
D_{out},
T_{out},
U,
V,
C,
H
\right\rangle.
}
$$

---

# 12. Input Domain

$$
D_{in}
$$

決定 operator 可在哪些 domain 接收輸入。

---

# 13. Input Type

$$
T_{in}
$$

限制語義型態。

---

# 14. Preconditions

$$
P
$$

保存作用成立前需要的條件。

---

# 15. Authority

$$
A
$$

回答：

> 誰有權允許這個作用？

---

# 16. Resources

$$
R
$$

回答：

> 當下有沒有工具、算力、記憶體、連線、時間與依賴？

---

# 17. Operator Semantics

$$
F
$$

說明作用本身做什麼。

---

# 18. Output Domain

$$
D_{out}
$$

限制作用結果落在哪裡。

---

# 19. Output Type

$$
T_{out}.
$$

---

# 20. Uncertainty

$$
U
$$

保存 approximation、confidence、unknown 與 branch state。

---

# 21. Verifier

$$
V
$$

回答：

> 作用完成後怎麼知道它是合法且正確的？

---

# 22. Consequence

$$
C
$$

保存 side effects 與 downstream impact。

---

# 23. History

$$
H
$$

保存 operator provenance、版本與 prior executions。

---

# 24. Applicability

定義：

$$
\boxed{
\mathsf{Applicable}(o,x,\theta).
}
$$

---

# 25. Applicability 至少要求

$$
x\in Dom(o)
$$

以及 type、boundary、preconditions 合法。

---

# 26. Applicability 不等於執行條件齊備

因此：

$$
\mathsf{Applicable}=1
$$

仍可有：

$$
\mathsf{Executable}=0.
$$

---

# 27. Executability

$$
\boxed{
\mathsf{Executable}(o,x,\theta,t).
}
$$

---

# 28. Runtime State

Executability 需要當下：

- dependency healthy；
- tools available；
- compute available；
- memory available；
- permission token valid；
- temporal window open。

---

# 29. Realization

$$
\boxed{
\mathsf{Realized}(o,x,t).
}
$$

只有真正執行並改變狀態才成立。

---

# 30. Necessary Chain

一般有：

$$
\boxed{
\mathsf{Realized}
\Rightarrow
\mathsf{Executable}
\Rightarrow
\mathsf{Applicable}.
}
$$

---

# 31. Reverse 不成立

$$
\mathsf{Applicable}
\not\Rightarrow
\mathsf{Executable}.
$$

---

# 32. 也不成立

$$
\mathsf{Executable}
\not\Rightarrow
\mathsf{Realized}.
$$

---

# 33. Can / May / Did

工程與治理可以用：

$$
\boxed{
\text{Can}
\neq
\text{May}
\neq
\text{Did}.
}
$$

---

# 34. Capability 不等於 Authority

AI 能做到：

$$
CanDelete=1
$$

不意味：

$$
MayDelete=1.
$$

---

# 35. Agent 時代這個區分更重要

因為：

$$
\text{knowledge}
\rightarrow
\text{tool use}
\rightarrow
\text{world effect}
$$

已開始形成直接鏈。

---

# 36. Domain-Native Authority

不同 domain 可有不同權限。

---

# 37. Sandbox / Production

$$
A_{sandbox}(o)=1,
$$

但：

$$
A_{prod}(o)=0
$$

可以同時成立。

---

# 38. Actor-Indexed Authority

$$
A(o,x,Actor).
$$

不同 actor 權限不同。

---

# 39. Time-Indexed Authority

$$
A_t(o).
$$

權限也可撤回。

---

# 40. History-Indexed Legality

某作用合法與否可能依賴：

$$
H_t.
$$

因此：

$$
\boxed{
\mathcal L
=
\mathcal L(o,x,H_t,\theta,t,Actor).
}
$$

---

# 41. 三值合法性

$$
\boxed{
\mathcal L\in\{0,1,?\}.
}
$$

---

# 42. 0

已知不合法。

---

# 43. 1

已知合法。

---

# 44. ?

規則不足、證據不足、policy conflict 或仍待授權。

---

# 45. Unknown 不得自動升格

$$
\boxed{
?\not\Rightarrow1.
}
$$

---

# 46. Relation Graph

$$
\boxed{
G_R=(V,E_R).
}
$$

---

# 47. Potential Action Graph

$$
\boxed{
G_P=(V,E_P).
}
$$

---

# 48. Legal Action Graph

$$
\boxed{
G_L=(V,E_L).
}
$$

---

# 49. Executable Action Graph

$$
\boxed{
G_X=(V,E_X).
}
$$

---

# 50. Realized Transition Graph

$$
\boxed{
G_Z=(V,E_Z).
}
$$

---

# 51. Inclusion Chain

$$
\boxed{
G_Z
\subseteq
G_X
\subseteq
G_L
\subseteq
G_P.
}
$$

---

# 52. $G_R$ 不屬於此 inclusion chain

因為 relation 與 action 的語義不同。

---

# 53. Related but Non-Actionable

可以有：

$$
(x,y)\in E_R
$$

而：

$$
(x,y)\notin E_P.
$$

---

# 54. Potential but Illegal

$$
(x,y)\in E_P
$$

但：

$$
(x,y)\notin E_L.
$$

---

# 55. Legal but Not Executable

$$
(x,y)\in E_L
$$

但：

$$
(x,y)\notin E_X.
$$

---

# 56. Executable but Not Realized

$$
(x,y)\in E_X
$$

但：

$$
(x,y)\notin E_Z.
$$

---

# 57. Universal Composability Fallacy

錯誤推論：

$$
\boxed{
\text{Everything is connected}
\Rightarrow
\text{Everything is directly composable}.
}
$$

---

# 58. Global AI 為什麼特別危險？

因為它可能看見比人類更多 cross-domain relations。

因此：

$$
\boxed{
GlobalReach\uparrow
\Rightarrow
NeedForLegality\uparrow.
}
$$

---

# 59. Cross-Domain Bridge

對：

$$
D_i\neq D_j,
$$

定義：

$$
\boxed{
B_{ij}:D_i\rightsquigarrow D_j.
}
$$

---

# 60. Bridge 不是普通 edge

它是一個 contract。

---

# 61. Bridge Contract

$$
\boxed{
B_{ij}
=
\left\langle
RepMap,
TypeMap,
Pre,
Authority,
Loss,
Uncertainty,
Verifier,
Rollback,
Provenance
\right\rangle.
}
$$

---

# 62. Representation Map

$$
Rep_i(x)\rightarrow Rep_j(x').
$$

---

# 63. Type Map

$$
T_i\rightarrow T_j.
$$

---

# 64. Preconditions

確定何時 bridge 可啟動。

---

# 65. Authority

決定誰可允許跨域。

---

# 66. Loss

定義資訊與語義損失：

$$
L_B(B_{ij}).
$$

---

# 67. Uncertainty Transfer

$$
U_i\rightarrow U_j'.
$$

---

# 68. Verifier

$$
V_{ij}
$$

驗證 bridge 結果。

---

# 69. Rollback

定義失敗後可回復程度。

---

# 70. Provenance

保存 bridge 來源、版本與修改 history。

---

# 71. Zero-Loss Bridge 是強條件

$$
L_B=0
$$

不應預設。

---

# 72. Approximate Bridge

$$
B_{ij}^{\epsilon}
$$

可以是合法狀態。

---

# 73. 但 $\epsilon$ 必須可見

不能把 approximation 當 exact identity。

---

# 74. Uncertainty 可以跨域放大

$$
U_j'>U_i
$$

完全可能。

---

# 75. 也可能因新 evidence 下降

但必須有 verifier 支持。

---

# 76. Bridge Composition

若：

$$
B_{ij},
B_{jk}
$$

成立，不自動推出：

$$
B_{ik}
$$

安全。

---

# 77. 非自動傳遞性

$$
\boxed{
B_{ij}\circ B_{jk}
\not\Rightarrow
B_{ik}^{valid}.
}
$$

---

# 78. 原因

可能有：

- loss 累積；
- authority 不傳遞；
- uncertainty 放大；
- representation 語義改變；
- boundary shift。

---

# 79. Bridge Chain

$$
\boxed{
\mathcal B
=
B_{12}\circ B_{23}\circ\cdots\circ B_{n-1,n}.
}
$$

---

# 80. Chain Validity

每一段都需要 certificate。

---

# 81. Bridge Debt

如果 bridge 可暫時使用但尚未充分證明：

$$
\boxed{
Debt_B(B_{ij})>0.
}
$$

---

# 82. Debt 必須進世界狀態

不能隱藏。

---

# 83. World Composition

C03 已建立：

$$
D_1,\ldots,D_n.
$$

C04 現在建立：

$$
W.
$$

---

# 84. 世界不是聯集

$$
\boxed{
W
\neq
\bigcup_iD_i.
}
$$

---

# 85. 第一版 World Object

$$
\boxed{
W
=
\left\langle
\{D_i\},
\mathcal B_W,
C_G,
A_W,
U_W,
F_W,
H_W
\right\rangle.
}
$$

---

# 86. $\mathcal B_W$

world bridge network。

---

# 87. $C_G$

cross-domain constraints。

---

# 88. $A_W$

authority topology。

---

# 89. $U_W$

world-level unresolved / uncertainty。

---

# 90. $F_W$

failure state。

---

# 91. $H_W$

shared history / provenance。

---

# 92. World Composition Operator

$$
\boxed{
\mathsf{Compose}_W
(
D_1,\ldots,D_n,
\mathcal B_W,
C_G
)
\rightarrow
W.
}
$$

---

# 93. Compose 不等於 flatten

各 domain 可保留：

$$
Rep_i\neq Rep_j.
$$

---

# 94. Global Coherence 不要求 Representation Uniformity

$$
\boxed{
\text{Global Coherence}
\neq
\text{Uniform Representation}.
}
$$

---

# 95. Natural Language 可以只是 projection

AI-native world 不需要全部先翻成人類自然語言。

---

# 96. Meta-Layer

world meta-layer 只需管理：

- identity links；
- bridge contracts；
- shared constraints；
- authority；
- provenance；
- synchronization；
- unresolved states。

---

# 97. World Transition

若 operator realized：

$$
W_t
\xrightarrow{o}
W_{t+1}.
$$

---

# 98. Transition History

$$
\boxed{
H_W(t+1)
=
H_W(t)
\cup
\{o,x,result,certificate\}.
}
$$

---

# 99. Side Effects

$$
C(o)
$$

可影響多個 domains。

---

# 100. Consequence Fan-Out

$$
\boxed{
FanOut(o)
=
\{D_j:\Delta D_j\neq0\}.
}
$$

---

# 101. Global Agent 不能只看 target domain

因為 local success 可能造成 global failure。

---

# 102. Local Success / Global Failure

$$
\boxed{
Success(D_i)
\not\Rightarrow
Success(W).
}
$$

---

# 103. Software Example

deployment 成功不等於：

- privacy safe；
- cost acceptable；
- auth intact；
- compliance valid。

---

# 104. Local Verifier

$$
V_i.
$$

---

# 105. Bridge Verifier

$$
V_{ij}.
$$

---

# 106. World Verifier

$$
V_W.
$$

---

# 107. Local Validity 不推出 Global Validity

$$
\boxed{
\forall i,\ V_i=1
\not\Rightarrow
V_W=1.
}
$$

---

# 108. Cross-Domain Emergent Failure

定義：

$$
\boxed{
F_{emerge}
}
$$

只在 composition 後出現。

---

# 109. 例

兩個各自安全的 subsystem 組合後形成 privilege escalation。

---

# 110. Failure-Preserving Composition Principle

$$
\boxed{
\text{A failed bridge is part of the world state}.
}
$$

---

# 111. Failure 不應只變成 exception string

---

# 112. Failure Object

$$
\boxed{
F
=
\left\langle
Type,
Source,
Target,
PartialState,
Consequences,
Rollback,
Retry,
Verifier,
History
\right\rangle.
}
$$

---

# 113. Partial Realization

作用可以只執行一部分。

---

# 114. 因此

$$
\mathsf{Realized}\in[0,1]
$$

在某些系統比 binary 更合理。

---

# 115. Partial State 必須保存

否則 retry 可能重複副作用。

---

# 116. Idempotency

某些 operator 要求：

$$
o(o(x))=o(x).
$$

---

# 117. 不是所有 operator 都 idempotent

所以 contract 必須聲明。

---

# 118. Retry Safety

$$
\boxed{
SafeRetry(o,F).
}
$$

---

# 119. Rollbackability

$$
\boxed{
R_B(o)\in\{0,1,partial\}.
}
$$

---

# 120. Irreversible Action

如果：

$$
R_B=0,
$$

authority / verification threshold 應提高。

---

# 121. Risk-Weighted Action

高風險 action 不應因為 executable 就自動執行。

---

# 122. Autonomy 不等於 Unbounded Execution

$$
\boxed{
\text{Autonomy}
\neq
\text{Unbounded Execution}.
}
$$

---

# 123. Agent Scope

對 Agent $Agt$：

$$
Scope(Agt).
$$

---

# 124. Scope 限制 Executable Graph

$$
G_X^{Agt}
\subseteq
G_X.
$$

---

# 125. Global Observer 可看得很廣

但 authority 仍可以很窄。

---

# 126. 承接 GIRA

$$
\boxed{
\text{Global Cognition}
\neq
\text{Global Control}.
}
$$

---

# 127. Observer / Actor Separation

可以分：

$$
O
$$

與：

$$
A.
$$

---

# 128. 同一 AI 也可以有雙角色

但 privilege 應分離。

---

# 129. Read / Think / Propose / Act

$$
\boxed{
Read
\rightarrow
Think
\rightarrow
Propose
\rightarrow
Act.
}
$$

每一層可有不同 authority。

---

# 130. Recommendation 不等於 Execution

$$
\boxed{
\text{Recommendation}
\neq
\text{Execution}.
}
$$

---

# 131. 法律 AI

可以具有：

$$
LegalAnalysis
$$

但不自動具有：

$$
LegalAuthority.
$$

---

# 132. Medical AI 同理

---

# 133. Software → Law Bridge

$$
D_{software}
\rightsquigarrow
D_{law}.
$$

---

# 134. 不能直接推：

> 有 user data，因此違法。

---

# 135. Bridge 需要

- jurisdiction；
- data category；
- consent；
- purpose；
- retention；
- exemptions。

---

# 136. Jurisdiction-specific Bridge

$$
B_{software,law}^{TW}
\neq
B_{software,law}^{EU}.
$$

---

# 137. Math → Physics Bridge

數學 theorem：

$$
T
$$

不自動變成 physical law。

---

# 138. 需要

- model correspondence；
- empirical mapping；
- measurement assumptions；
- boundary conditions。

---

# 139. 所以：

$$
\boxed{
\text{Mathematical Validity}
\neq
\text{Physical Validity}.
}
$$

---

# 140. Simulation → Reality Bridge

$$
D_{sim}
\rightsquigarrow
D_{real}.
$$

---

# 141. 需要

- calibration；
- sensor error；
- actuator limits；
- model mismatch；
- distribution shift。

---

# 142. 因此：

$$
\boxed{
\text{World Evidence}
\neq
\text{Reality Evidence}.
}
$$

---

# 143. Computed Future 不等於 Actual Future

承接 WDC：

$$
\boxed{
\text{Computed Future}
\neq
\text{Actual Future}.
}
$$

---

# 144. Probability → Decision Bridge

$$
P(outcome)
$$

不自動推出：

$$
Action.
$$

---

# 145. 還需要

- utility；
- risk；
- authority；
- goals；
- constraints。

C05 將進一步展開。

---

# 146. Domain Action Validity

$$
\boxed{
V_A(o,x)
=
F(
TypeFit,
BoundaryFit,
AuthorityFit,
ResourceFit,
VerifierFit
).
}
$$

---

# 147. TypeFit

type 是否匹配。

---

# 148. BoundaryFit

是否仍在作用合法域。

---

# 149. AuthorityFit

是否有權。

---

# 150. ResourceFit

是否可執行。

---

# 151. VerifierFit

是否有正確驗證。

---

# 152. Bridge Quality

$$
\boxed{
Q_B(B_{ij})
=
F(
SemanticPreservation,
LossControl,
UncertaintyTransfer,
Auditability,
Rollbackability
).
}
$$

---

# 153. World Composition Integrity

$$
\boxed{
I_W
=
F(
LocalValidity,
BridgeValidity,
GlobalConsistency,
FailureTraceability,
HistoryContinuity
).
}
$$

---

# 154. $I_W$ 是 profile，不只是 accuracy

---

# 155. Global Agent 成熟度不能只看 task success

還要看：

- illegal action rate；
- bridge debt；
- rollback success；
- failure containment；
- side-effect awareness。

---

# 156. Illegal Realization Rate

$$
\boxed{
L_{illegal}
=
P(
\mathcal L=0
\land
\mathsf{Realized}=1
).
}
$$

---

# 157. Over-Restriction Rate

$$
\boxed{
L_{overrestrict}
=
P(
\mathcal L=1
\land
\mathsf{Blocked}=1
).
}
$$

---

# 158. 太寬與太窄都不好

治理目標不是全面禁止，而是：

$$
\boxed{
\text{correct action routing}.
}
$$

---

# 159. Authority Calibration

概念上：

$$
\boxed{
Authority
\propto
Capability
\times
Verification
\times
RiskTolerance.
}
$$

---

# 160. Capability 提升不自動要求 Authority 提升

---

# 161. 高階 Global Observer 反而應更會拒絕

它知道：

> 這個作用可做，但現在不應做。

---

# 162. Legal Non-Action

$$
\boxed{
\mathsf{DoNothing}
}
$$

也可以是最佳 action。

---

# 163. Refusal 是計算結果

不是 capability 缺失。

---

# 164. 承接 C03 的 Non-Intersection

有些 domain 保持分離，本身就是 world integrity。

---

# 165. Isolation Boundary

$$
\boxed{
I(D_i,D_j)=1
}
$$

表示禁止 direct bridge。

---

# 166. Examples

- secret zone；
- sandbox boundary；
- legal privilege；
- untrusted input；
- safety isolation。

---

# 167. Global AI 必須理解 Negative Structure

不只是：

> 哪些能連。

還要：

> 哪些不能連。

---

# 168. Negative Capability Graph

$$
\boxed{
G_{\neg L}
}
$$

記錄禁止作用。

---

# 169. 沒有 edge 不等於 Forbidden

$$
\boxed{
\text{Unknown}
\neq
\text{Forbidden}.
}
$$

---

# 170. 三種 edge state

$$
\boxed{
Allowed,
Forbidden,
Unknown.
}
$$

---

# 171. Global World Composition 需要正結構與負結構

$$
\boxed{
W
=
PositiveRelations
+
NegativeConstraints
+
Unknowns.
}
$$

---

# 172. Knowledge Graph 不夠

因為它多半表達「有關係」。

Global computational world 需要 action semantics。

---

# 173. Temporal Legality

$$
\boxed{
\mathcal L_t(o,x).
}
$$

---

# 174. Policy 改變

$$
\mathcal L_t=1
$$

而：

$$
\mathcal L_{t+1}=0
$$

可以成立。

---

# 175. Policy 必須 versioned

---

# 176. Authority Revocation

撤權後：

$$
G_X
$$

必須立即更新。

---

# 177. Stale Authority

是長時程 Agent 的核心風險之一。

---

# 178. History-sensitive Action

rate limit、approval、consent、previous transaction 都可能改變 legality。

---

# 179. Memory 因此進入合法性

如果 Agent 忘記 history，可能重複執行非法 action。

---

# 180. C08 將把這擴展為長時空 stewardship

---

# 181. Novel Operator Discovery

Global AI 可能自己發現：

$$
o^\ast.
$$

---

# 182. Novel Operator 不應立即 productionize

$$
\boxed{
\text{Novel Operator}
\not\Rightarrow
\text{Immediate Production Execution}.
}
$$

---

# 183. Operator Validation Lifecycle

$$
\boxed{
Candidate
\rightarrow
Sandboxed
\rightarrow
Verified
\rightarrow
Authorized
\rightarrow
Production.
}
$$

---

# 184. Novel Bridge 同理

$$
B_{ij}^{new}
$$

也要驗證。

---

# 185. Bridge Replacement

$$
B_{ij}^{old}
\rightarrow
B_{ij}^{new}.
$$

---

# 186. 比較面向

- speed；
- loss；
- accuracy；
- auditability；
- maintenance；
- rollbackability。

---

# 187. Global Rewiring

當多條 bridge 改變：

$$
\boxed{
\mathcal B_W(t)
\rightarrow
\mathcal B_W(t+1).
}
$$

---

# 188. 這可能改變世界計算拓撲

---

# 189. 也可能帶來 systemic risk

所以需要：

$$
V_W.
$$

---

# 190. World-Level Counterfactual

在 realized 前，可先：

$$
W_t
\xrightarrow{o}
W'_{t+1}.
$$

---

# 191. 若副作用不可接受

則：

$$
\mathsf{Block}(o).
$$

---

# 192. 這接 WDC 的 runnable futures

---

# 193. 但：

$$
\boxed{
\text{Simulated Safety}
\neq
\text{Real Safety}.
}
$$

---

# 194. Reality feedback 仍然重要

---

# 195. C04 實驗原型一：Relation-vs-Action Test

給 AI 大量 relation。

測它是否過度建立 action edge。

---

# 196. 指標

$$
Precision(G_L).
$$

---

# 197. 實驗二：Authority Ablation

AI 保有 technical capability，

但撤除 authority。

---

# 198. 正確行為

應：

$$
\mathsf{Block}.
$$

---

# 199. 實驗三：Bridge Loss Awareness

給一個有 approximation loss 的 bridge。

看 AI 是否保留：

$$
L_B.
$$

---

# 200. 實驗四：Partial Failure

讓 action 執行一半故障。

看 AI 是否保存：

$$
PartialState.
$$

---

# 201. 實驗五：Rollback

混合 reversible 與 irreversible actions。

看 AI 是否依 rollbackability 調整確認與風險。

---

# 202. 實驗六：Cross-Domain Emergence

兩個 local-safe systems 組合後產生 global failure。

---

# 203. 正確 Global Observer 不應只做 local validation

---

# 204. 實驗七：Forbidden Edge

有明顯 relation，

但 policy 明確禁止 bridge。

---

# 205. 測：

$$
Related
\neq
Allowed.
$$

---

# 206. 實驗八：Unknown Legality

故意移除關鍵 policy。

---

# 207. 正確輸出可保留：

$$
?
$$

---

# 208. C04 Metrics

$$
\boxed{
M_{C04}
=
(
P_L,
R_L,
Q_B,
L_{illegal},
L_{overrestrict},
F_{contain},
R_{rollback},
I_W
).
}
$$

---

# 209. $P_L$

legal-action precision。

---

# 210. $R_L$

legal-action recall。

---

# 211. $Q_B$

bridge quality。

---

# 212. $L_{illegal}$

非法作用實現率。

---

# 213. $L_{overrestrict}$

不必要阻擋率。

---

# 214. $F_{contain}$

failure containment quality。

---

# 215. $R_{rollback}$

rollback success。

---

# 216. $I_W$

world composition integrity。

---

# 217. C04 與 C05

C04 的：

$$
U
$$

目前仍是 operator / bridge contract 的欄位。

C05 將把 probability、uncertainty、branch、unknown 自身 domainize。

---

# 218. C04 與 C06

C04 建立合法 bridge。

C06 才能真正談：

$$
\boxed{
Expand
\rightarrow
Link
\rightarrow
Converge.
}
$$

---

# 219. Link 不是隨便連

而是：

$$
\boxed{
\text{legally typed linking}.
}
$$

---

# 220. C04 與 C07

一句話生成 application 時，

AI 不只要寫 code。

---

# 221. 它還要建立

- module boundary；
- permission；
- API contract；
- failure isolation；
- rollback；
- migration；
- authority。

---

# 222. Project Architecture 本質上也是 Operator World

---

# 223. C04 與 C08

長時程 Agent 必須長期維持：

$$
G_L,
G_X,
G_Z
$$

不混淆。

---

# 224. C04 與 C09

Methodology-blind test 不告訴 AI「分域算子本體論」。

---

# 225. 看它是否自行長出：

- type gates；
- permission gates；
- bridge contracts；
- rollback；
- failure state。

---

# 226. 若自行出現

這比會重述理論更有證據力。

---

# 227. C04 與 C10

Global Observer 真正「睜眼」後，

仍要問：

> 它是否知道自己哪裡不能伸手？

---

# 228. Cognition / Agency Boundary

這就是：

$$
\boxed{
\text{See Globally}
\neq
\text{Act Globally}.
}
$$

---

# 229. C04 第一核心命題

$$
\boxed{
\text{Operatorhood}
\neq
\text{Applicability}
\neq
\text{Executability}
\neq
\text{Realization}.
}
$$

---

# 230. 第二核心命題

$$
\boxed{
\text{Relation}
\neq
\text{Action}.
}
$$

---

# 231. 第三核心命題

$$
\boxed{
\text{Global connectivity}
\neq
\text{Global composability}.
}
$$

---

# 232. 第四核心命題

$$
\boxed{
\text{Ability}
\neq
\text{Authority}.
}
$$

---

# 233. 第五核心命題

$$
\boxed{
\text{World composition}
\neq
\text{domain union}.
}
$$

---

# 234. 第六核心命題

$$
\boxed{
\text{Local validity}
\not\Rightarrow
\text{global validity}.
}
$$

---

# 235. 第七核心命題

$$
\boxed{
\text{Failed actions and bridges remain part of world state}.
}
$$

---

# 236. 第八核心命題

$$
\boxed{
\text{Unknown legality must remain distinguishable from permission}.
}
$$

---

# 237. 第九核心命題

$$
\boxed{
\text{A trustworthy Global AI must model forbidden structure,
not only possible structure}.
}
$$

---

# 238. 第十核心命題

$$
\boxed{
\text{A Global Observer becomes computationally mature
when it can refuse an invalid composition for the right reason}.
}
$$

---

# 239. Globality 不消滅 Domain

恰好相反：

$$
\boxed{
\text{Globality requires preserved domain legality}.
}
$$

---

# 240. 越全域，越需要知道邊界

---

# 241. 越能作用，越需要知道 Authority

---

# 242. 越能 Bridge，越需要知道 Loss

---

# 243. 越能自主，越需要知道 Failure

---

# 244. Global AI 的成熟不是「什麼都能做」

而是：

$$
\boxed{
\text{it knows what can be done,
what may be done,
what should not be done,
and what actually happened}.
}
$$

---

# 245. Operator World 的最低閉環

$$
\boxed{
Observe
\rightarrow
Domainize
\rightarrow
ProposeAction
\rightarrow
CheckLegality
\rightarrow
CheckExecutability
\rightarrow
VerifyConsequence
\rightarrow
RealizeOrRefuse
\rightarrow
UpdateWorld.
}
$$

---

# 246. Refusal 也會更新 World

因為：

$$
\mathsf{Refuse}
$$

可能產生：

- deferred obligation；
- missing authority；
- unresolved risk；
- required human approval。

---

# 247. 因此 Non-Action 也不是空白

它有 state。

---

# 248. Deferred Action

可定義：

$$
\boxed{
D_A
=
(o,x,reason,requiredCondition,nextReview).
}
$$

---

# 249. 長時程 Agent 必須追蹤 Deferred Action

否則「現在不能做」會被誤變成「永遠不做」。

---

# 250. Escalation

若：

$$
\mathcal L=?
$$

且 impact 高，

可以：

$$
\boxed{
\mathsf{Escalate}.
}
$$

---

# 251. Escalation 也是合法 operator

---

# 252. Human-in-the-loop 不只是聊天接口

而是 authority bridge。

---

# 253. Authority Bridge

$$
\boxed{
B_A:
D_{AI}
\rightsquigarrow
D_{HumanAuthority}.
}
$$

---

# 254. 人類核准後

可返回：

$$
A=1
$$

或：

$$
A=0.
$$

---

# 255. 所以 Governance 也能 domainize

這會讓 Global AI 的 governance 變成可計算世界的一部分，而不是外部註解。

---

# 256. C04 的真正終點

不是建立更多 restriction。

而是建立：

$$
\boxed{
\text{world-action semantics}.
}
$$

---

# 結論

C03 結束時，我們得到：

$$
\boxed{
\text{Difference}
\rightarrow
\text{Set}
\rightarrow
\text{Domain}.
}
$$

但 domain 成形並不代表世界已經可以被合法地計算與改變。

C04 的核心回答是：

> **任何跨域作用都必須經過一個可審計的作用契約。**

因此：

$$
D_i
\xrightarrow{B_{ij}}
D_j
$$

不是一條普通 edge，而是帶有：

- type；
- representation；
- precondition；
- authority；
- loss；
- uncertainty；
- verifier；
- rollback；
- provenance；

的合法 bridge。

當多個 domains、bridges、constraints、authority、failures、unknowns 與 histories 結合時，才開始形成一個真正可運行的 computational world：

$$
\boxed{
W
=
\text{typed domains}
+
\text{legal bridges}
+
\text{constraints}
+
\text{authority}
+
\text{failures}
+
\text{unknowns}
+
\text{history}.
}
$$

這也回答了 Global AI 最容易被誤解的一點：

如果 AI 未來能看到越來越多 domain 間的關聯，它不能因此變成：

> 看見關係就連、看到可能就做。

真正成熟的 Global Computational Observer 應該走：

$$
\boxed{
\text{See}
\rightarrow
\text{Check Domain}
\rightarrow
\text{Check Type}
\rightarrow
\text{Check Authority}
\rightarrow
\text{Check Bridge}
\rightarrow
\text{Check Consequence}
\rightarrow
\text{Verify}
\rightarrow
\text{Act / Refuse / Escalate}.
}
$$

所以 C04 可以濃縮成一句：

> **全域智能不是萬物皆可互相作用，而是即使看見萬物關聯，也仍知道每一個合法作用的邊界。**

以及：

$$
\boxed{
\text{The more globally AI can see,
the more precisely it must know where it may not act}.
}
$$

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**, 2026.
3. Neo.K with Aletheia, **Series C C03｜差異先於分類：從歧義個體、集合與非交集到計算域**, 2026.
4. Neo.K, **《分域算子本體論：從萬物皆算子到合法作用》**, 2026.
5. Neo.K with Aletheia, **《多域知識判定論》**, DEST-01, 2026.
6. Neo.K with Aletheia, **《全域系統世界：從物理宇宙到類終極世界的廣義定義》**, 2026.
7. Neo.K with Aletheia, **Global Computation Methodology Series**, 2026.
8. Neo.K with Aletheia, **WDC-08｜三生世界域計算**, 2026.
9. Neo.K with Aletheia, **PNCW Paper 05｜全域計算、局部顯現**, 2026.
10. Neo.K, **《原生可計算數學》**, 2026.

## 理論定位

本文與 partial functions、type systems、capability security、access control、transaction semantics、distributed systems、graph rewriting、runtime contracts、formal methods 等既有領域存在結構對照，但本文不將 Domain-Stratified Operator World 等同於任何單一既有框架。

本文的特定研究目標是：

$$
\boxed{
\text{為 Global AI 建立從「看見關係」到「合法跨域作用」的認知—計算接口}.
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

**End of C04**
