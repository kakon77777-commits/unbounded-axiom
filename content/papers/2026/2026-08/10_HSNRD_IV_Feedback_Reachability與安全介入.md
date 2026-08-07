# HSNRD IV：Feedback、Reachability 與安全介入
## ——從迴路極性、路徑閘門到反事實介入與約束式安全優化

### 摘要

前三篇數學方法論已依序建立 HSNRD 的 typed hierarchical ontology、micro-to-macro projection，以及可重寫的 CTMC / PDMP 混合結構動力學。但一個能夠出生、死亡、合併、分裂與改型的高階系統，仍然留下最重要的控制問題：哪些 feedback 真正支配系統？哪些節點只是局部迴路的重要元件，哪些卻控制世界線的入口與出口？如果介入某條強回饋迴路，系統是否必然變得「更好」？如何避免一個看似合理的 intervention 反而把系統推進新的吸收陷阱？

本文建立 HSNRD 最後一層方法論：Feedback–Reachability–Intervention。首先將 PDMP 的連續狀態與 rewrite hazards 聯合展開成異質 feedback graph：

$$
\boxed{
\mathcal F
=
(
V_X\cup V_R,\,
E_{XR}\cup E_{RX}\cup E_{RR}
)
}
$$

其中 state-to-rule 邊由 hazard sensitivity 建立，rule-to-state 邊由 jump reset 建立，rule-to-rule 邊則描述一個 rewrite 對另一個 rewrite 的適用域或 hazard 所造成的影響。本文將 feedback polarity 與 dynamical stability 嚴格分離：閉環權重的符號積可以區分 reinforcing 與 balancing loop，但：

$$
\boxed{
ReinforcingLoop
\not\Rightarrow
LocalInstability.
}
$$

真正的局部穩定性仍需考察 effective drift Jacobian：

$$
\boxed{
b_{\mathrm{eff}}(G,x)
=
F_G(x)
+
\sum_{\rho,m}
\lambda_{\rho,m}(G,x)\Delta_{\rho,m}x,
}
$$

及其 spectral abscissa。

其次，本文將 loop topology 與 reachability topology 分離。Feedback Vertex Set（FVS）與 cycle hitting set 可用於找出打斷閉環的候選節點／邊，但它們不告訴我們 intervention 後系統會落入哪個可達 macrostate。HSNRD 因而定義 Path Gate：對進入、退出、改型、恢復等結構路徑具有高控制力、但不一定具有高 loop centrality 的節點。核心命題為：

$$
\boxed{
CycleControl
\neq
ReachabilityControl
\neq
OutcomeControl.
}
$$

第三，本文引入 intervention world：

$$
\boxed{
\mathcal M^I
=
(
F^I,
\lambda^I,
R^I,
\mathcal P^I
)
}
$$

並以 paired-world simulation、terminal distribution distance、path reachability、absorbing-trap risk 與 intervention cost 進行模型內反事實比較。這是一種模型式 counterfactual，不等同於從觀察資料完成的 empirical causal identification。

最後，本文將介入問題寫成帶安全約束的優化：

$$
\boxed{
I^*
=
\arg\min_{I\in\mathcal I}
J(I)
}
$$

subject to structural legality、recovery reachability、undesired-state probability、distributional concentration 與 intervention budget 等條件。特別地，NOOP 必須是合法候選；若所有非空介入的結構風險或代價都高於 baseline，最佳決策可以是：

$$
\boxed{
I^*=NOOP.
}
$$

本文由此完成 HSNRD 的整體方法鏈：

$$
\boxed{
Set
\rightarrow
TypedGraph
\rightarrow
Projection
\rightarrow
Rewrite
\rightarrow
CTMC
\rightarrow
PDMP
\rightarrow
Sensitivity
\rightarrow
Feedback
\rightarrow
Reachability
\rightarrow
Counterfactual
\rightarrow
SafeOptimization.
}
$$

**關鍵詞：** HSNRD、feedback loop、feedback vertex set、reachability、path gate、counterfactual intervention、PDMP、safe optimization、absorbing trap

---

## 1. 最後一個問題：知道系統怎麼動之後，怎麼安全地改它？

HSNRD III 已得到：

$$
Z_t=(G_t,x_t)
$$

與生成元：

$$
(\mathcal L f)(G,x)
=
\nabla_x f\cdot F_G(x)
+
\sum_{\rho,m}
\lambda_{\rho,m}(G,x)
[
f(G'_{\rho,m},R_{\rho,m}(G,x))-f(G,x)
].
$$

這已經能描述：

- continuous flow；
- state-dependent hazard；
- structural rewrite；
- topology change；
- reset。

但如果我們想：

> 改變系統結果，

仍缺至少四個問題：

1. 哪些 feedback loops 真正重要？
2. 哪些 structural paths 決定可達終局？
3. intervention 會不會創造新的 trap？
4. 怎樣定義「安全」而不是只定義「有效」？

因此：

$$
\boxed{
Dynamics
\neq
ControlTheory.
}
$$

更不是：

$$
\boxed{
Control
=
CutTheStrongestLoop.
}
$$

---

## 2. 三種不同的 feedback

在 HSNRD 中，「feedback」不能只用一張 causal-loop diagram 全部代表。

至少有三個層次。

### 2.1 Continuous feedback

連續狀態：

$$
x_j
$$

改變某個 structural event hazard：

$$
\lambda_\rho.
$$

定義：

$$
\boxed{
J_{\lambda,\rho j}
=
\frac{\partial
\lambda_\rho
}{
\partial x_j
}.
}
$$

這是：

$$
x_j
\rightarrow
\rho
$$

的局部 differential sensitivity。

### 2.2 Structural feedback

一個 rewrite：

$$
\rho
$$

改變另一 rule：

$$
\sigma
$$

的：

- applicability；
- match count；
- hazard；
- type legality。

這是：

$$
\boxed{
\rho
\rightarrow
\sigma.
}
$$

它不一定能用普通導數表示。

### 2.3 Hybrid dynamical feedback

state 改變 hazard，

hazard 觸發 jump，

jump 改變 state / topology，

新的 topology 再改變 continuous flow。

因此：

$$
\boxed{
x
\rightarrow
\lambda
\rightarrow
Jump
\rightarrow
G'
\rightarrow
F_{G'}
\rightarrow
x.
}
$$

這是 HSNRD 真正的閉環。

---

## 3. State-to-Rule 邊

對 rule：

$$
\rho
$$

與 continuous variable：

$$
x_j,
$$

定義：

$$
\boxed{
w_{x_j\rightarrow\rho}
=
\frac{\partial
\lambda_\rho
}{
\partial x_j
}.
}
$$

如果：

$$
w>0,
$$

代表：

$$
x_j\uparrow
\Rightarrow
\lambda_\rho\uparrow.
$$

如果：

$$
w<0,
$$

代表抑制。

這只是 local sensitivity。

所以：

$$
\boxed{
LargeDerivative
\neq
LargeGlobalEffect.
}
$$

---

## 4. Rule-to-State 邊

若 event：

$$
\rho
$$

發生後：

$$
x
\rightarrow
R_\rho x,
$$

定義：

$$
\boxed{
\Delta_\rho x
=
R_\rho x-x.
}
$$

對 coordinate：

$$
x_j
$$

建立：

$$
\boxed{
w_{\rho\rightarrow x_j}
=
\Delta_\rho x_j.
}
$$

這表示 rewrite 對 continuous state 的 immediate effect。

注意：

$$
\Delta_\rho x
$$

與：

$$
F_{G'}(x)-F_G(x)
$$

不同。

前者是 jump reset，

後者是 rewrite 之後 flow field 的改變。

---

## 5. Immediate Differential Loop

若：

$$
x_j
\rightarrow
\rho
\rightarrow
x_j,
$$

則最簡單 local feedback contribution：

$$
\boxed{
K_{\rho j}
=
\frac{\partial\lambda_\rho}{\partial x_j}
\Delta_\rho x_j.
}
$$

總合：

$$
\boxed{
K_\rho
=
\sum_j
K_{\rho j}.
}
$$

若：

$$
K_{\rho j}>0,
$$

event effect 會使自身 hazard tendency 增強。

若：

$$
K_{\rho j}<0,
$$

則為局部 balancing tendency。

但若 rule 發生後直接失去適用域，

這個量仍不能被解讀成：

> rule 會自我無限複製。

所以：

$$
\boxed{
DifferentialSelfEffect
\neq
StructuralSelfReproduction.
}
$$

---

## 6. Rule-to-Rule 邊

假設：

$$
\rho
$$

發生前：

$$
\lambda_\sigma^{before},
$$

發生後：

$$
\lambda_\sigma^{after}.
$$

可定義：

$$
\boxed{
I_{\sigma\leftarrow\rho}
=
\log
\frac{
\lambda_\sigma^{after}+\epsilon
}{
\lambda_\sigma^{before}+\epsilon
}.
}
$$

若：

$$
I>0,
$$

$\rho$ 促進 $\sigma$ 。

若：

$$
I<0,
$$

$\rho$ 抑制 $\sigma$ 。

如果：

$$
\rho
$$

直接讓：

$$
\sigma
$$

失去 domain，

這是更強的：

$$
\boxed{
StructuralDisable.
}
$$

不能只當普通 small negative derivative。

---

## 7. Feedback Graph

因此建立：

$$
\boxed{
\mathcal F
=
(
V_X\cup V_R,
E_{XR}\cup E_{RX}\cup E_{RR}
).
}
$$

其中：

$$
V_X
=
\{x_1,\ldots,x_d\}
$$

為 continuous state nodes。

$$
V_R
=
\{\rho_1,\ldots,\rho_R\}
$$

為 rewrite-rule nodes。

邊：

$$
E_{XR}
$$

表示 state → rule。

$$
E_{RX}
$$

表示 rule → state。

$$
E_{RR}
$$

表示 rule → rule。

這不是原始 institutional graph：

$$
G.
$$

所以：

$$
\boxed{
FeedbackGraph
\neq
InstitutionGraph.
}
$$

---

## 8. Feedback graph 的異質單位問題

一條：

$$
x\rightarrow\rho
$$

邊可能是：

$$
\partial\lambda/\partial x.
$$

一條：

$$
\rho\rightarrow x
$$

則是 reset magnitude。

另一條：

$$
\rho\rightarrow\sigma
$$

是 log hazard ratio。

它們單位不同。

所以如果要放進同一視覺化 adjacency matrix，

通常必須做 channel-specific normalization。

例如：

$$
\boxed{
\tilde w_e
=
clip
\left(
\frac{w_e}{Q_{0.75}(|w|_{channel})},
-c,c
\right).
}
$$

這只能稱：

$$
\boxed{
DiagnosticNormalization.
}
$$

不能宣稱：

> 所有邊已被轉成同一個物理量。

---

## 9. Loop polarity

對 directed cycle：

$$
C=(e_1,\ldots,e_n),
$$

定義符號：

$$
\boxed{
Polarity(C)
=
sign
\left(
\prod_{e\in C}
w_e
\right).
}
$$

若：

$$
Polarity(C)>0,
$$

稱：

$$
\boxed{
ReinforcingLoop.
}
$$

若：

$$
Polarity(C)<0,
$$

稱：

$$
\boxed{
BalancingLoop.
}
$$

這與 system dynamics 中 feedback-loop polarity 的標準概念一致。

---

## 10. Negative edge 不等於 balancing loop

例如：

$$
A
\xrightarrow{-}
B
\xrightarrow{-}
A.
$$

整個 loop：

$$
(-)\times(-)=+.
$$

所以：

$$
\boxed{
MutualInhibition
}
$$

可以形成：

$$
\boxed{
Positive/ReinforcingLoop.
}
$$

因此：

$$
\boxed{
NegativeEdge
\not\Rightarrow
NegativeLoop.
}
$$

這在制度互斥、競爭性規則與歷史 lock-in 中非常重要。

---

## 11. Loop strength

可用：

$$
\boxed{
Gain(C)
=
\prod_{e\in C}
w_e.
}
$$

但長 loop 乘積自然變小，

所以可用幾何平均：

$$
\boxed{
S(C)
=
|Gain(C)|^{1/|C|}.
}
$$

這只是一個 diagnostic strength。

如果 edges 已經被異質 normalization，

則：

$$
S(C)
$$

不是物理增益。

所以：

$$
\boxed{
LoopStrength
=
ModelDiagnostic,
}
$$

除非所有邊有一致可乘語義。

---

## 12. Reinforcing loop 不等於局部不穩定

這是本篇最重要的校正之一。

system dynamics 中：

$$
PositiveLoop
$$

表示沿迴路的變化傾向會被強化。

但 hybrid system 的 local stability 取決於完整 effective dynamics。

所以：

$$
\boxed{
ReinforcingLoop
\not\Rightarrow
LocalInstability.
}
$$

一個 positive loop 可以存在於整體仍局部 stable 的系統。

---

## 13. Effective drift

對 PDMP，

在 infinitesimal expectation sense 下，可以定義：

$$
\boxed{
b_{\mathrm{eff}}(G,x)
=
F_G(x)
+
\sum_{\rho,m}
\lambda_{\rho,m}(G,x)
\Delta_{\rho,m}x.
}
$$

其中：

$$
\Delta_{\rho,m}x
=
R_{\rho,m}(G,x)-x.
$$

第一項：

$$
F_G
$$

是 continuous flow。

第二項：

$$
\lambda\Delta x
$$

是 jump 的 expected instantaneous drift contribution。

---

## 14. Effective Jacobian

定義：

$$
\boxed{
J_{\mathrm{eff}}
=
\frac{\partial b_{\mathrm{eff}}}{\partial x}.
}
$$

基礎 continuous Jacobian：

$$
\boxed{
J_F
=
\frac{\partial F_G}{\partial x}.
}
$$

再看 spectral abscissa：

$$
\boxed{
\alpha(J)
=
\max
\Re
\sigma(J).
}
$$

若：

$$
\alpha(J_{\mathrm{eff}})<0,
$$

表示該線性化下局部收斂。

即使 feedback graph 中存在強 reinforcing cycle，

也完全可能：

$$
\boxed{
\alpha(J_{\mathrm{eff}})<0.
}
$$

---

## 15. 三層 loop interpretation

因此 HSNRD 應固定三種 loop language：

### Level A — Differential loop

$$
x_j
\rightarrow
\lambda_\rho
\rightarrow
\Delta_\rho x_j.
$$

用：

$$
K_{\rho j}
$$

分析。

### Level B — Structural event loop

$$
\rho
\rightarrow
\sigma
\rightarrow
\rho.
$$

用：

$$
I_{\sigma\leftarrow\rho}
$$

與 applicability 分析。

### Level C — Hybrid dynamical loop

$$
x
\rightarrow
Hazard
\rightarrow
Jump
\rightarrow
EffectiveDrift
\rightarrow
x.
$$

用：

$$
J_{\mathrm{eff}}
$$

與 spectrum 分析。

因此：

$$
\boxed{
OneScalarLoopScore
}
$$

不應取代全部三層。

---

## 16. Feedback Vertex Set

對 directed graph：

$$
\mathcal F,
$$

若節點集合：

$$
S\subseteq V(\mathcal F)
$$

滿足：

$$
\mathcal F-S
$$

為 acyclic，

則：

$$
\boxed{
S
}
$$

是 Feedback Vertex Set。

FVS 在非線性網路控制中確實具有重要理論地位：

> 控制一組打斷所有 feedback cycles 的節點，可在特定 dissipative nonlinear-system 類別中對 attractor control 提供結構性保證。

這使 FVS 成為 HSNRD 很有價值的候選 generator。

---

## 17. 但 FVS 是計算問題

minimum FVS 一般是經典困難問題。

在 signed digraph 中：

- positive feedback vertex set；
- negative feedback vertex set；

等問題也可為 NP-complete。

2026 年 bounded-degree / planar feedback-set complexity 的新分類亦再次顯示，feedback-set family 的計算複雜度高度依 graph class 而變。

因此：

$$
\boxed{
FindAllOptimalFVS
}
$$

不是大系統中可被假定為廉價操作。

HSNRD 工程上通常需要：

- heuristic；
- approximation；
- bounded cycle enumeration；
- ILP / SAT；
- domain constraints。

---

## 18. HSNRD 的 selective cycle hitting set

HSNRD 不一定想打斷：

$$
AllCycles.
$$

例如 balancing loops 可能非常重要。

因此可以定義：

$$
\mathcal C_R^\theta
$$

為強度高於：

$$
\theta
$$

的 reinforcing cycles。

找：

$$
\boxed{
S
\subseteq V
}
$$

使：

$$
\forall C\in\mathcal C_R^\theta,
\quad
S\cap C\neq\varnothing.
$$

這是：

$$
\boxed{
StrongReinforcingCycleHittingSet.
}
$$

它不是標準 full FVS。

因此必須在術語上分開。

---

## 19. Break Loop 不等於控制結果

即使：

$$
S
$$

打斷全部 reinforcing cycles，

仍不能推出：

$$
Outcome
$$

變成想要的狀態。

原因是：

$$
\boxed{
FeedbackTopology
\neq
ReachabilityTopology.
}
$$

cycle graph 告訴我們：

> 哪些 causal dependencies 閉合。

rewrite meta-graph 告訴我們：

> 哪些世界線仍然可走。

這是兩張不同的圖。

---

## 20. 一個最簡單的 trap 例子

假設：

$$
Temporary
\xrightarrow{Split}
Ordinary
$$

是主要 exit path。

如果：

$$
Split
$$

同時位於強 reinforcing loop，

我們做：

$$
Cut(Split).
$$

feedback loop 被打斷。

但 exit path 也消失。

於是：

$$
\boxed{
Temporary
}
$$

可能變成 absorbing trap。

所以：

$$
\boxed{
BreakReinforcingLoop
\Rightarrow
CreateAbsorbingTrap
}
$$

完全可能。

---

## 21. Reachability graph

沿用 HSNRD III：

$$
\boxed{
\mathcal G_R
=
(V_R,E_R).
}
$$

對 current state：

$$
G,
$$

定義：

$$
Reach(G,A)
$$

表示能否到達 macroset：

$$
A.
$$

若有 stochastic rates，

則還可分析：

$$
\boxed{
P_G(
\tau_A\le T
)
}
$$

或 hitting probability：

$$
\boxed{
h_A(G)
=
P_G(
\tau_A<\infty
).
}
$$

這比 loop existence 更直接回答：

> 系統能不能出去？

---

## 22. Entry Gate 與 Exit Gate

定義一個 node / rule：

$$
v
$$

如果移除後：

$$
Reach(G,A)
$$

顯著下降，

則：

$$
v
$$

對集合 $A$ 是：

$$
\boxed{
PathGate.
}
$$

若 $A$ 是某制度狀態的進入區：

$$
\boxed{
EntryGate.
}
$$

若 $A$ 是 recovery / exit：

$$
\boxed{
ExitGate.
}
$$

一個 path gate：

$$
\boxed{
LoopCentrality(v)
}
$$

可以非常低。

---

## 23. Loop Importance 與 Gate Importance

因此定義兩個不同軸：

$$
\boxed{
I_L(v)
}
$$

表示 feedback-loop importance。

以及：

$$
\boxed{
I_G(v)
}
$$

表示 reachability / outcome-gate importance。

例如：

$$
I_G(v)
\approx
TV
\left(
P(G_T),
P(G_T\mid do(I_v))
\right).
$$

這只是一種 empirical model-based proxy。

因此節點可分成：

| $I_L$ | $I_G$ | 類型 |
|---:|---:|---|
| 高 | 高 | Core controller |
| 高 | 低 | Local amplifier |
| 低 | 高 | Path gate |
| 低 | 低 | Peripheral |

---

## 24. 為什麼 Path Gate 很重要？

傳統 centrality 很容易找到：

- 高 degree；
- 高 betweenness；
- 高 loop participation；

節點。

但一個：

$$
BirthRule
$$

可能只發生一次，

loop participation 很低，

卻控制：

$$
\boxed{
CanSystemEnterTheRegime?
}
$$

同樣：

$$
SplitRule
$$

可能不在主要循環中心，

卻控制：

$$
\boxed{
CanSystemEscape?
}
$$

因此：

$$
\boxed{
LowLoopImportance
\not\Rightarrow
LowOutcomeImportance.
}
$$

---

## 25. Feedback Dormancy

如果某 checkpoint：

$$
\mathcal F_t
$$

找不到短 reinforcing cycles，

不能說：

> 系統沒有因果結構。

可能有兩種不同 dormancy。

### Stable dormancy

系統已進入低 feedback、可恢復區域。

### Locked dormancy

exit rules 已不可適用，

因此：

$$
\boxed{
NoActiveLoop
}
$$

只是因為：

$$
\boxed{
NoAvailableExit.
}
$$

所以：

$$
\boxed{
FeedbackFree
\neq
Healthy
\neq
Adaptive.
}
$$

---

## 26. Counterfactual Intervention World

現在正式定義介入。

baseline model：

$$
\boxed{
\mathcal M
=
(
F,
\lambda,
R,
\mathcal P
).
}
$$

介入：

$$
I
$$

建立：

$$
\boxed{
\mathcal M^I
=
(
F^I,
\lambda^I,
R^I,
\mathcal P^I
).
}
$$

也就是 intervention 可以改變：

- continuous flow；
- event hazard；
- reset；
- rewrite grammar。

不同 intervention 類型必須有不同 semantics。

---

## 27. 四類 intervention

### 27.1 State → Rule edge intervention

原 hazard：

$$
\lambda_\rho(G,x).
$$

切除：

$$
x_j\rightarrow\rho
$$

可以定義為：

$$
\boxed{
\lambda_\rho^I(
G,x
)
=
\lambda_\rho(
G,
x_{-j},
x_j^{ref}
).
}
$$

也就是 hazard 不再讀 live $x_j$ ，

而讀固定 reference。

這是**一種** edge-cut semantics，

不是唯一可能定義。

### 27.2 Rule → State intervention

若：

$$
\rho
$$

原本 reset：

$$
x_j
\rightarrow
R_{\rho,j}(x),
$$

可以 suppress：

$$
\boxed{
R_{\rho,j}^I(x)=x_j.
}
$$

### 27.3 Rule node intervention

直接：

$$
\boxed{
\lambda_\rho^I=0.
}
$$

或從 grammar：

$$
\mathcal P^I
=
\mathcal P-\{\rho\}.
$$

### 27.4 Structural grammar intervention

直接改寫：

- match legality；
- type schema；
- rewrite outcome；
- relation routing。

這是最強、也最需要 formal rewrite semantics 的介入。

---

## 28. State-node cut 必須小心定義

如果說：

$$
Cut(x_j),
$$

可能至少有三種含義：

1. 把 $x_j$ 固定；
2. 移除 $x_j$ 對 hazards 的影響；
3. 從 continuous ODE 中刪除該 state。

這三者完全不同。

所以：

$$
\boxed{
NodeCut
}
$$

不是自明操作。

每一個 intervention 都必須明確定義：

$$
\boxed{
InterventionSemantics(I).
}
$$

---

## 29. Paired-world simulation

如果要比較：

$$
\mathcal M
$$

與：

$$
\mathcal M^I,
$$

可使用：

$$
\boxed{
CommonRandomNumbers.
}
$$

即：

- 相同 initial state；
- 相同 random seed / exponential stream；
- 能共用的 stochastic randomness 儘量共用。

這有助於降低：

$$
Outcome_I-Outcome_0
$$

估計 variance。

但 structural path 分岔後，

兩世界的 event sequence 可能不再一一對應。

因此：

$$
\boxed{
PairedRandomness
\neq
IdenticalHistory.
}
$$

---

## 30. 這不是 empirical causal identification

HSNRD 中：

$$
do(I)
$$

表示：

> 在已指定模型內修改 structural equations / hazards / rewrite grammar。

它不是：

> 已從現實 observational data 證明 intervention 有 causal effect。

因此：

$$
\boxed{
ModelCounterfactual
\neq
EmpiricalCausalIdentification.
}
$$

如果要對現實做因果結論，

還需要：

- identification assumptions；
- data；
- measurement validity；
- model validation。

---

## 31. Terminal distribution

若 macro outcome：

$$
M(G_T)
\in
\{
m_1,\ldots,m_K
\},
$$

baseline distribution：

$$
p^0.
$$

介入：

$$
p^I.
$$

可用 total variation distance：

$$
\boxed{
TV(p^I,p^0)
=
\frac12
\sum_k
|p_k^I-p_k^0|.
}
$$

衡量 intervention 對 terminal macro distribution 的總體改變。

---

## 32. Global effect 不等於 desirable effect

大：

$$
TV
$$

只表示：

> 介入改變很多。

它不表示：

> 改變得好。

所以：

$$
\boxed{
EffectSize
\neq
Desirability.
}
$$

同理：

$$
TV=0
$$

也不保證 intervention 無作用，

因為：

- path distribution；
- timing；
- continuous state；

仍可能改變。

因此 terminal TV 只是其中一個 summary。

---

## 33. Pathwise metrics

對 safety 更重要的可能是：

$$
\boxed{
P(
\tau_{\mathcal U}<T
)
}
$$

其中：

$$
\mathcal U
$$

是 unsafe region。

也可以看：

$$
\boxed{
P(
\tau_{\mathcal R}<T
)
}
$$

其中：

$$
\mathcal R
$$

是 recovery set。

再加：

$$
ExpectedTimeToExit,
$$

$$
ExpectedOccupationTime(\mathcal U).
$$

所以：

$$
\boxed{
TerminalSafety
\neq
PathwiseSafety.
}
$$

---

## 34. 三層安全

HSNRD 最少需要三種 safety。

### 34.1 Structural safety

intervention 後仍滿足：

- type legality；
- rewrite semantics；
- graph consistency。

即：

$$
\boxed{
I
\in
\mathcal I_{legal}.
}
$$

### 34.2 Reachability safety

不能意外殺死：

- recovery；
- exit；
- reform；

通道。

例如：

$$
\boxed{
P_G^I(
\tau_\mathcal R<T
)
\ge
\eta.
}
$$

### 34.3 Distributional safety

不能讓全部機率集中到單一 undesired macrostate。

例如：

$$
\boxed{
\max_k
P^I(M_T=m_k)
\le
\kappa.
}
$$

但 concentration 只是 trap proxy，

不等於真正 absorbing-state probability。

---

## 35. 第四層：Continuous State Safety

若 continuous state 有 forbidden region：

$$
\mathcal X_U,
$$

可再要求：

$$
\boxed{
P^I(
\exists t\le T:
x_t\in\mathcal X_U
)
\le
\epsilon_x.
}
$$

這比只看 final graph 更接近完整 hybrid safety。

---

## 36. Absorbing Trap

若 intervention 使某：

$$
G^*
$$

滿足：

$$
\boxed{
Reach^I(
G^*,
\mathcal H-\{G^*\}
)
=0,
}
$$

則：

$$
G^*
$$

是 structural absorbing state。

若它不是 desired target，

稱：

$$
\boxed{
InterventionInducedTrap.
}
$$

因此：

$$
\boxed{
BreakLoops
\Rightarrow
CreateTrap
}
$$

是必須被檢查的 failure mode。

---

## 37. Cycle Control、Reachability Control、Outcome Control

現在可以正式寫：

$$
\boxed{
CycleControl
\neq
ReachabilityControl
\neq
OutcomeControl.
}
$$

### Cycle control

問：

> 哪些 feedback loops 被打斷？

### Reachability control

問：

> 哪些 states 還能到達？

### Outcome control

問：

> 機率質量最後怎麼分布？

三者互相關聯，

但沒有任何一個可以單獨替代另外兩個。

---

## 38. Structural intervention 的一般意義

網路研究本身也區分：

- characteristic intervention；
- structural intervention。

前者改變 node intrinsic state / incentive，

後者改變 network links。

HSNRD 更進一步，

因為 intervention 甚至可以改：

$$
\boxed{
Ontology.
}
$$

例如：

- Birth rule；
- Split rule；
- institution type；
- rewrite admissibility。

所以：

$$
\boxed{
StructuralIntervention
}
$$

在 HSNRD 中至少包括：

$$
Edge,
Node,
Rule,
Grammar.
$$

---

## 39. Safe Intervention Optimization

令 intervention set：

$$
\boxed{
\mathcal I.
}
$$

每個：

$$
I
$$

有：

$$
Cost(I).
$$

以及 outcome metrics：

$$
P^I(M_T),
$$

$$
Reachability^I,
$$

$$
TV^I.
$$

定義：

$$
\boxed{
I^*
=
\arg\min_{I\in\mathcal I}
J(I)
}
$$

subject to safety constraints。

---

## 40. 一個 generic objective

例如：

$$
\boxed{
J(I)
=
w_C Cost(I)
+
w_U P^I(\mathcal U_T)
+
w_T P^I(\mathcal T_T)
+
w_V TV(P_T^I,P_T^0)
+
w_K Concentration(P_T^I).
}
$$

其中：

- $\mathcal U$ ：undesired macroset；
- $\mathcal T$ ：temporary / intermediate undesirable set；
- $TV$ ：distribution shift；
- concentration：trap proxy。

但：

$$
w_C,w_U,w_T,w_V,w_K
$$

是：

$$
\boxed{
ExplicitNormative/DesignChoices.
}
$$

不是自然常數。

---

## 41. Generic constraints

例如：

### Recovery

$$
\boxed{
P^I(
G_T\in\mathcal R
)
\ge
\eta.
}
$$

### Undesired-state bound

$$
\boxed{
P^I(
G_T\in\mathcal U
)
\le
\epsilon.
}
$$

### Concentration

$$
\boxed{
\max_k
P^I(M_T=m_k)
\le
\kappa.
}
$$

### Budget

$$
\boxed{
Cost(I)\le B.
}
$$

### Structural legality

$$
\boxed{
I\in\mathcal I_{legal}.
}
$$

---

## 42. Pareto frontier

如果不想預先指定單一權重，

可以找：

$$
\boxed{
ParetoFront
}
$$

對：

- cost ↓；
- undesired probability ↓；
- TV ↓；
- recovery ↑；

做 multi-objective comparison。

這比一開始就寫死：

$$
J(I)
$$

更透明。

然後再由 decision layer 選擇 trade-off。

---

## 43. NOOP 必須存在

安全 intervention optimizer 不應預設：

> 一定要做點什麼才算有用。

所以：

$$
\boxed{
NOOP\in\mathcal I.
}
$$

若所有非空 intervention：

$$
I\neq NOOP
$$

都增加：

- cost；
- trap risk；
- distribution shift；

則：

$$
\boxed{
I^*=NOOP.
}
$$

這不是 optimizer 失敗。

而是：

$$
\boxed{
DoNotIntervene
}
$$

本身是一個有效決策。

---

## 44. 必須介入與允許不介入是兩個問題

可以定義兩個 optimization mode。

### Mode A — NOOP allowed

$$
\boxed{
I^*
=
\arg\min_{I\in\mathcal I\cup\{NOOP\}}
J(I).
}
$$

### Mode B — Must intervene

$$
\boxed{
I^*_{nonempty}
=
\arg\min_{I\in\mathcal I,\ I\neq NOOP}
J(I).
}
$$

兩個答案可以完全不同。

因此：

$$
\boxed{
BestIntervention
\neq
BestDecision.
}
$$

---

## 45. FVS 在 optimizer 中的正確位置

FVS / cycle hitting set 不應被當成：

$$
Solution.
$$

它應該放在：

$$
\boxed{
CandidateGeneration.
}
$$

即：

$$
FVS
\rightarrow
CandidateCuts
\rightarrow
CounterfactualScreen
\rightarrow
SafetyFilter.
$$

所以：

$$
\boxed{
FVS/CycleCut
\subset
CandidateGeneration.
}
$$

這是 HSNRD v1.0 最重要的方法論收斂之一。

---

## 46. Candidate Generator

候選介入可以來自：

1. high loop-centrality nodes；
2. strong reinforcing cycle hitting sets；
3. high gate-importance nodes；
4. high sensitivity edges；
5. domain-specified legal interventions；
6. low-cost pair combinations；
7. NOOP。

所以 candidate space：

$$
\boxed{
\mathcal I
=
\mathcal I_{loop}
\cup
\mathcal I_{gate}
\cup
\mathcal I_{sensitivity}
\cup
\mathcal I_{domain}
\cup
\{NOOP\}.
}
$$

---

## 47. Screen → Confirm

Monte Carlo counterfactual optimization 若候選很多，

可以兩階段。

### Screening

低成本：

- 較少 runs；
- 粗步長；
- 快速 elimination。

### Confirmation

對 shortlist：

- 更多 paired runs；
- 更小 timestep；
- bootstrap confidence；
- robustness tests。

因此：

$$
\boxed{
CheapScreen
\rightarrow
HighPrecisionConfirmation.
}
$$

這比對所有候選一開始就做大量 simulation 更實用。

---

## 48. Uncertainty 必須保留

Monte Carlo outcome：

$$
\hat p
$$

不是精確概率。

所以應報告：

- sample size；
- confidence / bootstrap interval；
- random seed strategy；
- timestep sensitivity。

因此：

$$
\boxed{
EstimatedSafe
\neq
ProvedSafe.
}
$$

production-grade safety 還需要：

- formal reachability；
- verified bounds；
- robust control；
- uncertainty set。

---

## 49. 工程 v0.9 / v1.0 的 synthetic evidence

前期 toy HSNRD runtime 已提供幾個非常重要的 construction examples。

它們不是現實政治資料。

只證明：

> 本方法描述的 failure mode 在一個具體可執行混合模型中可以出現。

其中包括：

### Balanced regime：Cut SplitEA

介入後：

$$
P(Permanent)\approx0.99.
$$

原本想切斷某個重要路徑，

卻幾乎把系統鎖進 permanent macrostate。

### Balanced hitting set

切：

$$
\{DeathEC,MergeEC_B,RetypeEC\}
$$

後：

$$
P(Temporary)=1
$$

於 toy confirmation 中形成 temporary trap。

### Capture regime：Cut BirthEC

系統：

$$
P(Ordinary)=1.
$$

這降低了 permanent outcome，

但 terminal concentration：

$$
=1
$$

因此仍違反示範 safety constraint。

### Capture regime：Cut SplitEA

則：

$$
P(Permanent)=1.
$$

這些共同展示：

$$
\boxed{
BreakStrongLoops
\not\Rightarrow
DesirableOutcome.
}
$$

---

## 50. 「Ordinary」標籤也不等於安全

如果：

$$
P(Ordinary)=1,
$$

看起來可能是好結果。

但如果這是因為：

$$
Birth
$$

被完全禁止，

系統其實失去：

> 在真正 crisis 下生成必要新機構

的能力。

所以：

$$
\boxed{
DesirableLabel
\neq
SafeStructuralOutcome.
}
$$

這和第一部：

$$
Descriptive
\neq
Normative
$$

的區分完全一致。

---

## 51. NOOP 的 toy result

在 v1.0 示範權重下，

三個 synthetic regimes 的確認結果都出現：

$$
\boxed{
J(NOOP)
<
J(I^*_{nonempty}).
}
$$

因此：

$$
\boxed{
I^*=NOOP.
}
$$

這不是要證明：

> 現實世界最好永遠不要介入。

而是證明：

> 一個安全 optimizer 若真的允許 NOOP，可能合理拒絕所有非必要結構介入。

---

## 52. Cross-regime robustness

若希望同一 intervention：

$$
I
$$

在多個 regime：

$$
r_1,\ldots,r_n
$$

都安全，

可要求：

$$
\boxed{
I
\in
\bigcap_r
\mathcal I_{safe}^{(r)}.
}
$$

或最小化：

$$
\boxed{
\max_r
J_r(I).
}
$$

這是：

$$
\boxed{
RobustIntervention.
}
$$

但如果 regimes 只是 toy profiles，

robustness 也只在這個 synthetic family 內成立。

---

## 53. Feedback graph 不能取代 original model

feedback graph：

$$
\mathcal F
$$

只是：

$$
\boxed{
DiagnosticAbstraction.
}
$$

真正 outcome 仍由：

$$
\mathcal M
=
(F,\lambda,R,\mathcal P)
$$

決定。

所以：

$$
\boxed{
FeedbackGraph
\neq
GenerativeModel.
}
$$

這和 HSNRD II 的 projection principle 完全一致。

---

## 54. Spectral radius 也不能被誤當 stability theorem

若把 normalized feedback graph 寫成 adjacency：

$$
W_F,
$$

可以計算：

$$
\rho(W_F)
$$

或：

$$
\max\Re\sigma(W_F).
$$

這些是 graph diagnostics。

但：

$$
\boxed{
\rho(W_F)>1
}
$$

不等於：

> PDMP 系統局部 unstable。

真正 local stability：

$$
J_{\mathrm{eff}}
$$

才是更直接的線性化對象。

因此：

$$
\boxed{
FeedbackAdjacencySpectrum
\neq
DynamicalStabilitySpectrum.
}
$$

---

## 55. Structural sensitivity 與 differential sensitivity

一個 intervention 可以：

### 微小改變 hazard

$$
\frac{\partial\lambda}{\partial\theta}.
$$

這是 differential sensitivity。

也可以：

### 直接關閉 rule domain

$$
Dom(\rho)\rightarrow\varnothing.
$$

這是 structural sensitivity。

兩者不可只用同一 Jacobian。

所以：

$$
\boxed{
DifferentialSensitivity
\neq
StructuralSensitivity.
}
$$

PDMP sensitivity literature 對離散與連續 contributions 分離的做法，正好提供一個相鄰的數學參照。

---

## 56. Safe intervention 不是只看局部穩定

甚至：

$$
\alpha(J_{\mathrm{eff}})<0
$$

也不夠。

因為 system 可以局部穩定在：

$$
\boxed{
BadAttractor/Trap.
}
$$

所以：

$$
\boxed{
LocalStability
\neq
GlobalSafety.
}
$$

必須再看：

- reachable sets；
- invariant sets；
- absorbing classes；
- pathwise risk。

---

## 57. 也不是只看 terminal distribution

terminal distribution 看不到：

> 中途是否曾進入 forbidden region？

所以：

$$
\boxed{
TerminalSafe
\not\Rightarrow
PathwiseSafe.
}
$$

真正 production HSNRD optimizer 最終應接：

- reach-avoid probability；
- chance constraints；
- temporal logic；
- barrier / viability analysis；

等更強工具。

本篇只建立方法論接口。

---

## 58. 規範層必須保持外置

第一部已建立：

$$
\boxed{
CausalImportance
\not\Rightarrow
MoralImportance.
}
$$

所以安全 optimizer 裡的：

$$
\mathcal U,
\mathcal R,
w_i,
Cost
$$

不是從數學動力自動長出來。

它們必須由：

$$
\boxed{
Normative/DesignSpecification
}
$$

明確給定。

因此：

$$
\boxed{
Optimizer
}
$$

不會替研究者自動回答：

> 哪一個國家制度才是 morally good？

它只能回答：

> 在你明確定義的目標與安全條件下，哪個 intervention 在模型內表現較好？

---

## 59. HSNRD 安全介入架構

完整流程可寫：

$$
\boxed{
CandidateGenerator
}
$$

$$
\Downarrow
$$

$$
\boxed{
CounterfactualScreen
}
$$

$$
\Downarrow
$$

$$
\boxed{
StructuralSafetyFilter
}
$$

$$
\Downarrow
$$

$$
\boxed{
ReachabilitySafetyFilter
}
$$

$$
\Downarrow
$$

$$
\boxed{
Distributional/PathwiseSafetyFilter
}
$$

$$
\Downarrow
$$

$$
\boxed{
ParetoRanking
}
$$

$$
\Downarrow
$$

$$
\boxed{
HighPrecisionConfirmation
}
$$

$$
\Downarrow
$$

$$
\boxed{
NOOPComparison.
}
$$

這就是 HSNRD 最終 control layer。

---

## 60. HSNRD IV 的核心公理／限制

### Axiom C1 — Feedback Type Separation

$$
\boxed{
DifferentialFeedback
\neq
StructuralFeedback
\neq
HybridFeedback.
}
$$

### Axiom C2 — Loop Polarity Is Structural

$$
\boxed{
ReinforcingLoop
\not\Rightarrow
LocalInstability.
}
$$

### Axiom C3 — Feedback Graph Is Diagnostic

$$
\boxed{
\mathcal F
\neq
\mathcal M.
}
$$

### Axiom C4 — FVS Is Not Outcome Control

$$
\boxed{
FVSControl
\neq
ReachabilityControl.
}
$$

### Axiom C5 — Gate Importance Is Distinct

$$
\boxed{
I_L
\neq
I_G.
}
$$

### Axiom C6 — Cycle, Reachability, Outcome Separation

$$
\boxed{
CycleControl
\neq
ReachabilityControl
\neq
OutcomeControl.
}
$$

### Axiom C7 — Intervention Semantics Must Be Explicit

$$
\boxed{
InterventionName
\not\Rightarrow
UniqueOperation.
}
$$

### Axiom C8 — Counterfactual Is Model-Based

$$
\boxed{
ModelCounterfactual
\neq
EmpiricalCausalIdentification.
}
$$

### Axiom C9 — Effect Is Not Value

$$
\boxed{
LargeEffect
\neq
GoodEffect.
}
$$

### Axiom C10 — Safety Is Multi-Layered

$$
\boxed{
StructuralSafety
+
ReachabilitySafety
+
DistributionalSafety
+
PathwiseSafety.
}
$$

### Axiom C11 — NOOP Is a Valid Candidate

$$
\boxed{
NOOP\in\mathcal I.
}
$$

### Axiom C12 — Estimated Safety Is Not Formal Safety

$$
\boxed{
MonteCarloSafe
\neq
ProvedSafe.
}
$$

---

## 61. 四篇 HSNRD 數學方法論的統一

HSNRD I：

$$
\boxed{
WhatExistsAndHowItRelates.
}
$$

HSNRD II：

$$
\boxed{
HowMicroBecomesMacro.
}
$$

HSNRD III：

$$
\boxed{
HowStructureChangesThroughHistory.
}
$$

HSNRD IV：

$$
\boxed{
HowFeedbackAndReachabilityConstrainSafeIntervention.
}
$$

因此四篇形成：

$$
\boxed{
Ontology
\rightarrow
Projection
\rightarrow
Dynamics
\rightarrow
Control.
}
$$

---

## 62. 與第一部高階欲求理論重新接合

現在可以重新把第一部的：

$$
GroupReflexivelyWants(S,x)
$$

翻成數學問題。

需要：

### Existence

$$
X^{(k,\tau)}
$$

合法形成。

### Projection

$$
\pi_A
$$

保留 agency-relevant state。

### Dynamics

$$
(G_t,x_t)
$$

形成 persistent preference / decision / action。

### Feedback

$$
x
\leftrightarrow
Hazard
\leftrightarrow
Rewrite
$$

形成 goal-tracking closure。

### Reachability

系統真的存在：

$$
ActionPath
\rightarrow
GoalRelevantStates.
$$

因此：

$$
\boxed{
Want
}
$$

不再只是自然語言 predicate，

而能拆解成一組 dynamical conditions。

---

## 63. Leviathan Reversal 也得到完整數學接口

第五篇定義：

$$
\mathbf L_S
=
(
D_P,S_D,E_L,R_D
).
$$

現在：

### Purpose Drift

進入：

$$
x_t
$$

中的 objective state。

### Self-Preservation Dominance

影響：

$$
\lambda_\rho(G,x).
$$

### Exit Loss

表現為：

$$
Reach(
G,\mathcal R
)\downarrow.
$$

### Downward Reshaping

進入：

$$
F_G
$$

與：

$$
R_\rho.
$$

所以：

$$
\boxed{
LeviathanReversal
}
$$

可以被表示為：

> feedback topology、hazard field 與 reachability topology 共同發生 regime transition。

---

## 64. 為什麼這比單一 LRI 更成熟？

早期 LRI：

$$
LRI
=
Divergence
\times
SelfReference
\times
Asymmetry
\times
Coherence
$$

可以當 synthetic diagnostic。

但完整 HSNRD 顯示：

$$
\boxed{
OneScalar
}
$$

不可能同時完整代表：

- loop structure；
- reachability；
- agent preference；
- legitimacy；
- trap risk。

因此 LRI 類 scalar 最適合：

$$
\boxed{
MonitoringIndicator.
}
$$

不是：

$$
\boxed{
CompleteTheory.
}
$$

---

## 65. HSNRD 的完整對象

現在可以把整套狀態寫成：

$$
\boxed{
\mathbb H_t
=
(
G_t,
x_t,
\Pi_t,
\mathcal B_t,
\mathcal P_t,
\mathcal N_t
).
}
$$

其中：

- $G_t$ ：typed attributed structural graph；
- $x_t$ ：continuous / discrete attributes；
- $\Pi_t$ ：micro–macro projections；
- $\mathcal B_t$ ：realization bases；
- $\mathcal P_t$ ：rewrite grammar；
- $\mathcal N_t$ ：外置 normative / safety specification。

動力：

$$
\boxed{
\mathbb H_t
\rightarrow
\mathbb H_{t+\Delta t}
}
$$

可以同時改變：

- state；
- topology；
- type；
- projection；
- grammar。

---

## 66. HSNRD 不再是一個「國家模型」

這一點必須在全系列最後明確說明。

雖然 Leviathan / state 是主要 toy domain，

HSNRD 的數學結構並不限定：

$$
\tau=State.
$$

它可以建模：

- 公司；
- 科研組織；
- AI multi-agent systems；
- 機器人群；
- 生物組織；
- 軟體 service graph；
- 生態制度；
- 跨組織治理。

只要存在：

$$
\boxed{
HierarchicalConstitution
+
TypedRelations
+
StructuralRewrite
+
HybridDynamics.
}
$$

---

## 67. HSNRD 也不是普遍萬物理論

同樣不能反向誇大。

HSNRD 是：

$$
\boxed{
ModelingMethodology.
}
$$

不是：

> 所有社會、物理、生物現象都必須用 HSNRD 描述。

若研究問題只需要：

- ordinary ODE；
- simple graph；
- Bayesian model；

就不應強行加入：

$$
Birth/Death/PDMP/FVS.
$$

因此：

$$
\boxed{
UseOnlyTheStructureRequiredByTheQuestion.
}
$$

是最後一條方法論節制。

---

## 68. 完整 HSNRD 方法鏈

最後，整個第二部可以濃縮成：

$$
\boxed{
Set
}
$$

$$
\Downarrow
$$

$$
\boxed{
TypedSetNode
}
$$

$$
\Downarrow
$$

$$
\boxed{
Incidence/Realization
}
$$

$$
\Downarrow
$$

$$
\boxed{
RelationBundle/MultilayerGraph
}
$$

$$
\Downarrow
$$

$$
\boxed{
Projection/CoarseGraining
}
$$

$$
\Downarrow
$$

$$
\boxed{
GraphRewrite
}
$$

$$
\Downarrow
$$

$$
\boxed{
RuleComposition/Reachability
}
$$

$$
\Downarrow
$$

$$
\boxed{
CTMC
}
$$

$$
\Downarrow
$$

$$
\boxed{
PDMP
}
$$

$$
\Downarrow
$$

$$
\boxed{
Sensitivity/FeedbackGraph
}
$$

$$
\Downarrow
$$

$$
\boxed{
PathGate/Reachability
}
$$

$$
\Downarrow
$$

$$
\boxed{
CounterfactualIntervention
}
$$

$$
\Downarrow
$$

$$
\boxed{
ConstrainedSafeOptimization.
}
$$

---

## 69. 全系列的最終統一式

第一部處理：

$$
\boxed{
WhatDoesAHigherOrderEntityMeanWhenItWants?
}
$$

第二部處理：

$$
\boxed{
HowCanSuchAnEntityBeRepresentedAndDynamicallyTested?
}
$$

因此全系列最終可寫：

$$
\boxed{
HigherOrderSubject
=
ExistenceStructure
+
Projection
+
AgencyClosure
+
HistoricalRewrite
+
Feedback
+
Reachability.
}
$$

而：

$$
\boxed{
NormativePriority
}
$$

仍然外置，

不能由以上結構自動推導。

---

## 70. 結論

HSNRD 最終得到的，不是一個：

> 找到最強 feedback 然後切掉它

的控制方法。

而是一個更保守的原則：

$$
\boxed{
InterveneOnlyAfterUnderstanding
Feedback
+
Reachability
+
CounterfactualOutcome
+
SafetyConstraints.
}
$$

Feedback graph 告訴我們：

> 哪些 closed causal structures 正在作用。

Reachability graph 告訴我們：

> 哪些未來仍然可走。

Path gates 告訴我們：

> 哪些節點／規則控制入口與出口。

Counterfactual runtime 告訴我們：

> 改變後概率質量可能去哪裡。

Safe optimizer 最後才問：

> 在明確安全與成本約束下，哪個 intervention 值得選？

因此：

$$
\boxed{
CycleControl
\neq
ReachabilityControl
\neq
OutcomeControl.
}
$$

而：

$$
\boxed{
BreakAllStrongReinforcingLoops
\not\Rightarrow
DesirableOutcome.
}
$$

甚至：

$$
\boxed{
BreakLoops
\Rightarrow
CreateAbsorbingTrap
}
$$

完全可能。

因此 NOOP 必須永遠保留：

$$
\boxed{
I^*=NOOP
}
$$

有時正是理性的安全答案。

至此，HSNRD 的數學方法論完成：

$$
\boxed{
Set
\rightarrow
TypedGraph
\rightarrow
Projection
\rightarrow
Rewrite
\rightarrow
CTMC
\rightarrow
PDMP
\rightarrow
Sensitivity
\rightarrow
Feedback
\rightarrow
Reachability
\rightarrow
Counterfactual
\rightarrow
SafeOptimization.
}
$$

而整個十篇系列也完成了從哲學問題：

> 「國家、文明與制度真的能『想要』嗎？」

到數學問題：

> 「一個高階集合如何形成、持續、投影、改寫、行動、回饋、被介入，並保持可檢驗的安全條件？」

的完整轉換。

---

## 參考文獻

Bai, T., Cao, Y., & Xiao, M. (2026). “Feedback Set Problems on Bounded-Degree (Planar) Graphs.” arXiv:2605.11407.

Bao, L., et al. (2018). Work on feedback-vertex-set-based control of nonlinear networks.

Czapla, D. (2024). “On the Existence and Uniqueness of Stationary Distributions for Some Piecewise Deterministic Markov Processes with State-Dependent Jump Intensity.” *Results in Mathematics*, 79, 177.

Ford, A. (2019). “A System Dynamics Glossary.” *System Dynamics Review*.

Gupta, A., & Khammash, M. (2018). “Sensitivity Analysis for Multiscale Stochastic Reaction Networks Using Hybrid Approximations.” arXiv:1801.04708.

Mochizuki, A., Fiedler, B., Kurosawa, G., & Saito, D. (2013). “Dynamics and Control at Feedback Vertex Sets. II: A Faithful Monitor to Determine the Diversity of Molecular Activities in Regulatory Networks.” *Journal of Theoretical Biology*, 335, 130–146.

Montalva, M., Aracena, J., & Gajardo, A. (2008). “On the Complexity of Feedback Set Problems in Signed Digraphs.” *Electronic Notes in Discrete Mathematics*, 30, 249–254.

Sun, Y., Zhao, W., & Zhou, J. (2021). “Structural Interventions in Networks.” arXiv:2101.12420.

Behr, N. (2021). “On Stochastic Rewriting and Combinatorics via Rule-Algebraic Methods.” arXiv:2102.02364.

Davis, M. H. A. (1984). “Piecewise-Deterministic Markov Processes: A General Class of Non-Diffusion Stochastic Models.” *Journal of the Royal Statistical Society, Series B*, 46(3), 353–376.

---

## 本篇核心命題表

| 編號 | 命題 |
|---|---|
| C1 | $DifferentialFeedback\neq StructuralFeedback\neq HybridFeedback$ |
| C2 | $NegativeEdge\not\Rightarrow BalancingLoop$ |
| C3 | $ReinforcingLoop\not\Rightarrow LocalInstability$ |
| C4 | $FeedbackGraph\neq GenerativeModel$ |
| C5 | $FeedbackAdjacencySpectrum\neq DynamicalStabilitySpectrum$ |
| C6 | $FVS/CycleCut\subset CandidateGeneration$ |
| C7 | $LoopImportance\neq GateImportance$ |
| C8 | $LowLoopImportance\not\Rightarrow LowOutcomeImportance$ |
| C9 | $FeedbackFree\neq Healthy\neq Adaptive$ |
| C10 | $CycleControl\neq ReachabilityControl\neq OutcomeControl$ |
| C11 | $BreakStrongLoops\not\Rightarrow DesirableOutcome$ |
| C12 | $BreakLoops\Rightarrow CreateAbsorbingTrap$ can occur |
| C13 | $ModelCounterfactual\neq EmpiricalCausalIdentification$ |
| C14 | $EffectSize\neq Desirability$ |
| C15 | $TerminalSafety\neq PathwiseSafety$ |
| C16 | $EstimatedSafe\neq ProvedSafe$ |
| C17 | $BestIntervention\neq BestDecision$ |
| C18 | $NOOP\in\mathcal I$ |
| C19 | $CausalImportance\not\Rightarrow MoralImportance$ |
| C20 | Safe intervention requires feedback, reachability, outcome and explicit normative constraints |

---

# 全系列最終核心命題總表

| 區域 | 核心命題 |
|---|---|
| 高階存在 | $HigherOrderExistence\neq HigherOrderAgency$ |
| 欲求語義 | $Preference\neq Intention\neq Propensity$ |
| 群體欲求 | $GroupWant\neq\sum_i IndividualWant_i$ |
| 自主性 | $Supervenience\neq Reduction\neq Autonomy$ |
| 正當性 | $Existence\not\Rightarrow Agency\not\Rightarrow Legitimacy$ |
| Leviathan | $Persistence\neq Entrenchment$ |
| 結構本體 | $Constitution\neq Interaction$ |
| 自環合法性 | $GraphSelfLoop\neq MembershipSelfReference$ |
| 投影 | $GoodProjection\neq LosslessProjection$ |
| 動力封閉 | $MarkovMicro\not\Rightarrow MarkovMacro$ |
| 歷史 | $FinalState\neq History$ |
| 結構重寫 | $ClassicalLinearDPO\neq AllStructuralRewrite$ |
| 隨機歷史 | $Reachable\neq Likely\neq Realized$ |
| Feedback | $ReinforcingLoop\not\Rightarrow LocalInstability$ |
| 控制 | $CycleControl\neq ReachabilityControl\neq OutcomeControl$ |
| 安全 | $BreakLoops\Rightarrow CreateAbsorbingTrap$ can occur |
| 介入 | $BestIntervention\neq BestDecision$ |
| 規範 | $CausalImportance\not\Rightarrow MoralImportance$ |

---

**系列：高階集合、欲求與 Leviathan / HSNRD 完整数學方法論**  
**第二部：HSNRD 完整数學方法論**  
**篇次：10 / 10**  
**狀態：全系列完成**
