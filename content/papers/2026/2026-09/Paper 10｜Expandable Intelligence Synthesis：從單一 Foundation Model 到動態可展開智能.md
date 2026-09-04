# Paper 10｜Expandable Intelligence Synthesis：從單一 Foundation Model 到動態可展開智能

**English Title:** *Expandable Intelligence Synthesis: From Monolithic Foundation Models to Dynamically Expandable Cognitive Systems*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 系列統合理論論文／Expandable Intelligence、Mother AI、Cognitive Architecture Synthesis

---

## 摘要

本文為《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》十篇系列之統合理論論文。前九篇依序提出：Scaling-to-Cognitive-Efficiency Transition、Cognitive Density、Resident Cognitive Core、MoE as Conditional Intelligence、Externalized Mixture of Cognitive Experts、Cognitive Factorization Problem、Temporary Cognition / Cognitive Compilation、Mother AI as Cognitive Command Tower，以及 Capability Boundary Tomography。

本文將上述命題收斂成 **Expandable Intelligence（可展開智能）** 的統一架構：

$$
\boxed{
\mathfrak I_t
=
(
K_R,
\mathcal C_Q,
\mathcal C_X,
Z_t,
\Omega_t,
\mathcal A_C(t),
\mathcal M_t,
\Gamma_t
)
}
$$

其中：

- $K_R$：Resident Cognitive Core，長期常駐的高中心性認知基底；
- $\mathcal C_Q$：Conditionally Activated Capability，模型內部或近端按需激活能力；
- $\mathcal C_X$：Externally Expandable Capability，外部模型、Sub-AI、工具、檢索、solver 與其他異質資源；
- $Z_t$：Temporary Cognition，針對當前任務編譯形成的暫時認知狀態；
- $\Omega_t$：Cognitive Organization，任務期間動態生成的角色、拓樸、執行、驗證與資源配置；
- $\mathcal A_C(t)$：Capability Atlas，Mother AI 對自己與其他資源能力邊界的持續估計；
- $\mathcal M_t$：跨時間記憶、歷史、世界狀態與決策 lineage；
- $\Gamma_t$：authority、governance、acceptance 與 policy 邊界。

本文提出：

$$
\boxed{
\text{System Intelligence}
\neq
\text{Largest Resident Model}.
}
$$

更一般地：

$$
\boxed{
\mathcal C_{\mathrm{system}}
=
\operatorname{Closure}
\left(
\mathcal C_R
\cup
\mathcal C_Q
\cup
\mathcal C_X
\cup
\mathcal C_{\mathrm{coord}}
\right).
}
$$

這裡的 closure 表示：系統能力不只來自各元件能力集合的聯集，也包含 cognitive compilation、routing、verification、composition、tool execution、multi-agent interaction 與 reconvergence 所產生的組合能力。

本文進一步回答本系列最重要的本體問題：

> **當能力分散在多個模型、tools、external memories 與 temporary agents 中時，為什麼它們還能被視為「同一個智能系統」？**

本文不以「是否共享同一組權重」作為智能連續性的判準，而提出 **Cognitive Continuity Invariants（認知連續性不變量）**：

$$
\boxed{
\mathcal J_t
=
(
G_t,
I_t,
M_t,
E_t,
\Gamma_t,
P_t,
H_t
)
}
$$

其中：

- $G_t$：持續目標與優先級；
- $I_t$：identity / system identity；
- $M_t$：可追溯記憶與狀態；
- $E_t$：epistemic state 與 evidence lineage；
- $\Gamma_t$：governance / authority；
- $P_t$：persistent capability / organization policies；
- $H_t$：歷史與可回放決策鏈。

如果底層 reasoning carrier：

$$
L_i
\rightarrow
L_j
$$

被替換，但：

$$
\mathcal J_t
\rightarrow
\mathcal J_{t+\Delta t}
$$

保持足夠連續，則系統仍可能保持 Mother-level cognitive continuity。反之，即使所有元件都位於同一 checkpoint，如果 goals、memory、evidence、authority 與 state 在每次執行中重置，則它也未必構成 persistent Mother AI。

本文將可展開智能區分為三個能力位置與兩個動態工作層：

$$
\boxed{
\underbrace{
\mathcal C_R
}_{Resident}
+
\underbrace{
\mathcal C_Q
}_{Conditional}
+
\underbrace{
\mathcal C_X
}_{External}
+
\underbrace{
Z_T
}_{Temporary\ Cognition}
+
\underbrace{
\Omega_T
}_{Temporary\ Organization}.
}
$$

其中前三者回答：

> 能力放在哪裡？

後兩者回答：

> 任務來臨時，如何把能力組成一個有效認知過程？

本文提出 **Expandable Intelligence Cycle**：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Interpret}
\rightarrow
\text{Estimate Boundary}
\rightarrow
\text{Compile Cognition}
\rightarrow
\text{Organize Capability}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Reconcile}
\rightarrow
\text{Consolidate}
}
$$

並形式化為：

$$
\boxed{
W_t
\rightarrow
M_t
\rightarrow
(Z_T,\Omega_T)
\rightarrow
A_T
\rightarrow
E_T
\rightarrow
V_T
\rightarrow
M_{t+1}.
}
$$

本文進一步提出 **Cognitive Placement Dynamics**：

$$
\boxed{
p_t(c)
\in
\{
R,Q,X
\}
}
$$

其中能力 $c$ 可以隨：

- 使用頻率；
- latency；
- cost；
- reliability；
- external availability；
- privacy；
- verification difficulty；
- model evolution；

在 Resident、Conditional、External 三種位置間遷移：

$$
\boxed{
R
\leftrightarrow
Q
\leftrightarrow
X.
}
$$

因此模型架構不必永久固定哪些能力「屬於模型」、哪些能力「屬於工具」。能力位置本身可以成為長期學習與系統優化的一部分。

本文並不主張 monolithic Foundation Model 將消失。相反，Frontier Foundation Model 仍可能是極重要的通用 reasoning carrier、teacher、fallback、expert，甚至 Mother Core 的主要實作。然而本文主張：

$$
\boxed{
\text{Monolithic Scaling}
}
$$

不必是：

$$
\boxed{
\text{the only scaling axis}.
}
$$

未來 AI 系統還可以沿著以下方向 scaling：

$$
\boxed{
\text{Cognitive Density}
}
$$

$$
\boxed{
\text{Conditional Capacity}
}
$$

$$
\boxed{
\text{External Capability Coverage}
}
$$

$$
\boxed{
\text{Compilation Quality}
}
$$

$$
\boxed{
\text{Organizational Quality}
}
$$

$$
\boxed{
\text{Capability Awareness}
}
$$

$$
\boxed{
\text{Verification Quality}.
}
$$

本文提出二十項統一命題、十六類總體失敗模式與十二組系列級可否證實驗。若未來實驗顯示：在等總成本、等 latency、等風險約束下，單一大型 resident model 長期全面支配所有 modular / expandable architecture；externalization、routing、compilation 與 verification 的 coordination tax 永遠高於收益；persistent Mother state 對長期 performance 沒有額外價值；或 cognitive continuity 無法跨模型替換維持，則 Expandable Intelligence 應被限制為少數工程 workload，而不能被視為一般智能架構方向。

本文的最終命題是：

$$
\boxed{
\text{Intelligence need not be resident in one place to remain one intelligence.}
}
$$

真正需要保持的不是所有能力的物理共居，而是：

$$
\boxed{
\text{cognitive continuity}
+
\text{epistemic continuity}
+
\text{goal continuity}
+
\text{governed capability integration}.
}
$$

如果這些條件成立，未來的 Mother AI 可能不再是一個「什麼都背在身上的最大模型」，而是一個高認知密度的持續核心，能在需要時長出、啟動、調用、驗證、替換、回收與重新組織能力。

這就是本文所稱的：

$$
\boxed{
\text{Expandable Intelligence}.
}
$$

**關鍵詞：** Expandable Intelligence、Cognitive Kernel、Mother AI、Mixture-of-Experts、External Experts、Temporary Cognition、Capability Atlas、Dynamic Topology、Cognitive Density、Post-Monolithic AI

---

# 0. 系列問題的重新表述

本系列最初的問題可以簡化成：

> AI 是否一定要讓模型本身攜帶幾乎所有能力與高解析度知識？

如果答案不是必然，

下一個問題就是：

$$
\boxed{
\text{What should remain resident?}
}
$$

再下一個：

$$
\boxed{
\text{What may be conditional?}
}
$$

再下一個：

$$
\boxed{
\text{What may be external?}
}
$$

最後：

$$
\boxed{
\text{How can all of them still behave as one intelligence?}
}
$$

Paper 10 專門回答最後一問。

---

# 1. 第一篇的結論：Scaling 變成 Allocation Problem

Paper 01 並未否定 scaling。

它提出：

$$
\boxed{
\text{Future Scaling}
\rightarrow
\text{Compute Allocation Problem}.
}
$$

當某類能力跨過 Functional Maturity Threshold 後，

下一單位計算：

$$
\Delta C
$$

不必永遠投入：

$$
\Delta P_{\mathrm{resident}}.
$$

也可以投入：

- retrieval；
- verification；
- test-time reasoning；
- routing；
- external capability；
- memory；
- organization。

---

# 2. 第二篇：Cognitive Density

Paper 02 將問題從：

$$
\text{How large?}
$$

改成：

$$
\boxed{
\text{How much verified cognition per total cost?}
}
$$

並提出：

$$
\boxed{
\eta_C^{(\lambda)}
=
\frac{
Q_C
}{
C_\lambda
}.
}
$$

---

# 3. 第三篇：Resident Cognitive Core

Paper 03 提出：

$$
\boxed{
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
}
$$

即 Mother Core 至少需要：

- interpretation；
- reasoning basis；
- epistemic control；
- meta-cognition；
- minimum sufficient world basis；
- coordination；
- governance。

---

# 4. 第四篇：Conditional Intelligence

Paper 04 使用 MoE 建立：

$$
\boxed{
P_{\mathrm{total}}
\gg
P_{\mathrm{active}}.
}
$$

因此：

$$
\boxed{
\text{available capability}
\neq
\text{always-active capability}.
}
$$

---

# 5. 第五篇：External Cognitive Experts

Paper 05 進一步問：

$$
\boxed{
\text{Why must an expert live inside one model?}
}
$$

並提出：

$$
\boxed{
\text{Micro-MoE}
\rightarrow
\text{Meso-MoE}
\rightarrow
\text{Macro-MoE}.
}
$$

---

# 6. 第六篇：Cognitive Factorization

Paper 06 提出：

$$
\boxed{
\mathfrak F
=
(
D,C,X,L,R,G
).
}
$$

即：

- Decompose；
- Compress；
- Expand；
- Link；
- Reconcile；
- Converge。

---

# 7. 第七篇：Temporary Cognition

Paper 07 把：

$$
\text{retrieved documents}
$$

與：

$$
\text{usable cognition}
$$

分開。

提出：

$$
\boxed{
Z_T
=
\Gamma_T(
K_R,S_t,T,D_T,X_T
).
}
$$

---

# 8. 第八篇：Cognitive Command Tower

Paper 08 提出：

$$
\boxed{
\Omega_T
=
(
\tau_T,
\mathbf R_T,
\mathbf X_T,
G_E,
G_V,
B_T,
\Gamma_T,
\sigma_T
).
}
$$

Mother AI 根據當前狀態生成 temporary cognitive organization。

---

# 9. 第九篇：Capability Boundary Tomography

Paper 09 提出：

$$
\boxed{
\widehat{\mathcal C}_i(t)
}
$$

以及：

$$
\boxed{
\text{Delegation}
=
\text{Execution}
+
\text{Measurement}.
}
$$

Sub-AI 同時成為：

$$
\boxed{
\text{epistemic instrument}.
}
$$

---

# 10. 十篇現在可以合成一個系統

統一形式：

$$
\boxed{
\mathfrak I_t
=
(
K_R,
\mathcal C_Q,
\mathcal C_X,
Z_t,
\Omega_t,
\mathcal A_C(t),
\mathcal M_t,
\Gamma_t
).
}
$$

這就是 Expandable Intelligence 的最小抽象。

---

# 11. 三個能力位置

能力 $c$ 的 placement：

$$
\boxed{
p_t(c)
\in
\{
R,Q,X
\}.
}
$$

---

# 12. $R$：Resident

適合：

- high frequency；
- high centrality；
- low latency；
- hard to verify externally；
- governance-critical。

---

# 13. $Q$：Conditional

適合：

- lower frequency；
- hidden-state coupled；
- low-latency activation；
- high interaction granularity。

---

# 14. $X$：External

適合：

- specialist；
- fast-changing；
- low frequency；
- high resolution；
- independently verifiable；
- coarse-grained interface。

---

# 15. 三種位置不是永久分類

$$
\boxed{
R
\leftrightarrow
Q
\leftrightarrow
X.
}
$$

能力可以遷移。

---

# 16. Ability Placement Is a Learning Problem

若：

$$
F(c)\uparrow
$$

使用頻率提升，

可能：

$$
X\rightarrow Q.
$$

若：

$$
L(c)\uparrow
$$

latency sensitivity 增加，

可能：

$$
Q\rightarrow R.
$$

---

# 17. 反過來也成立

若：

$$
\text{external availability}\uparrow,
$$

$$
\text{verification ease}\uparrow,
$$

則：

$$
R\rightarrow Q\rightarrow X
$$

可能更有效率。

---

# 18. Dynamic Placement

因此：

$$
\boxed{
p_{t+1}(c)
=
F_p(
p_t(c),
usage,
cost,
risk,
capability,
history
).
}
$$

---

# 19. 這不是 Cache Policy

因為 placement 不只看 frequency。

還看：

- centrality；
- authority；
- verification；
- risk；
- dependency；
- privacy。

---

# 20. Intelligence Boundary Is No Longer Model Boundary

傳統：

$$
\boxed{
\partial I
=
\partial M.
}
$$

Expandable Intelligence：

$$
\boxed{
\partial I
\neq
\partial M.
}
$$

---

# 21. 模型只是 Carrier

Reasoning carrier：

$$
L_t.
$$

可以：

$$
L_t\rightarrow L_{t+1}.
$$

---

# 22. 但 System Identity 可以持續

只要：

$$
\boxed{
\mathcal J_t
\rightarrow
\mathcal J_{t+1}
}
$$

保持足夠 continuity。

---

# 23. Cognitive Continuity Invariants

定義：

$$
\boxed{
\mathcal J_t
=
(
G_t,
I_t,
M_t,
E_t,
\Gamma_t,
P_t,
H_t
).
}
$$

---

# 24. Goal Continuity

$$
G_t
$$

表示：

> 系統在持續追求什麼？

---

# 25. Identity Continuity

$$
I_t
$$

表示：

> 哪些狀態被視為同一 persistent system 的狀態？

---

# 26. Memory Continuity

$$
M_t
$$

表示：

- history；
- commitments；
- previous decisions；
- project state。

---

# 27. Epistemic Continuity

$$
E_t
$$

表示：

- accepted；
- unknown；
- contested；
- rejected；
- evidence lineage。

---

# 28. Governance Continuity

$$
\Gamma_t
$$

表示：

- authority；
- privacy；
- commit policy；
- constraints。

---

# 29. Policy Continuity

$$
P_t
$$

表示：

- routing priors；
- role contracts；
- verification policies；
- organization templates。

---

# 30. History Continuity

$$
H_t
$$

使：

$$
\boxed{
\text{current cognition}
}
$$

可以追溯到過去。

---

# 31. Same Weights Are Not Required

如果：

$$
L_A\rightarrow L_B
$$

但：

$$
\mathcal J
$$

持續，

則 Mother-level continuity 可以保持。

---

# 32. Same Weights Are Also Not Sufficient

即使：

$$
L_t=L_{t+1},
$$

但：

$$
G,M,E,\Gamma
$$

全部清空，

也不構成 persistent Mother cognition。

---

# 33. 因此 One Intelligence 是 Functional Continuity

本文提出：

$$
\boxed{
\text{One Intelligence}
=
\text{Continuity of Governed Cognitive State}
}
$$

作為工程層命題。

---

# 34. 這不是 Consciousness Definition

本文不由此推出：

- consciousness；
- personhood；
- sentience。

這只是：

$$
\boxed{
\text{system identity / continuity criterion}.
}
$$

---

# 35. Expandable Intelligence Cycle

$$
\boxed{
\text{Observe}
\rightarrow
\text{Interpret}
\rightarrow
\text{Estimate Boundary}
\rightarrow
\text{Compile}
\rightarrow
\text{Organize}
\rightarrow
\text{Execute}
\rightarrow
\text{Verify}
\rightarrow
\text{Reconcile}
\rightarrow
\text{Consolidate}.
}
$$

---

# 36. Observe

世界：

$$
W_t
$$

提供：

- events；
- data；
- outcomes。

---

# 37. Interpret

Resident Core：

$$
K_R
$$

建立：

$$
\widehat W_t.
$$

---

# 38. Estimate Boundary

Capability Atlas：

$$
\mathcal A_C(t)
$$

回答：

> 自己做？

> expert？

> tool？

> no suitable capability？

---

# 39. Compile

Paper 07：

$$
\boxed{
\Gamma_T
\rightarrow
Z_T.
}
$$

---

# 40. Organize

Paper 08：

$$
\boxed{
\mathsf{OrgCompile}
\rightarrow
\Omega_T.
}
$$

---

# 41. Execute

$$
\Omega_T
$$

激活：

$$
\mathcal C_Q
$$

或：

$$
\mathcal C_X.
$$

---

# 42. Verify

$$
G_V
$$

產生：

$$
V_T.
$$

---

# 43. Reconcile

處理：

- disagreement；
- evidence；
- unknown；
- conflicts。

---

# 44. Consolidate

任務結果：

$$
\Delta_T
$$

分成：

$$
\boxed{
\text{discard}
}
$$

$$
\boxed{
\text{temporary retain}
}
$$

$$
\boxed{
\text{external memory}
}
$$

$$
\boxed{
\text{core candidate}.
}
$$

---

# 45. Closed Loop

因此：

$$
\boxed{
W_t
\rightarrow
M_t
\rightarrow
(Z_T,\Omega_T)
\rightarrow
A_T
\rightarrow
E_T
\rightarrow
V_T
\rightarrow
M_{t+1}.
}
$$

---

# 46. System Capability Closure

$$
\boxed{
\mathcal C_S
=
\operatorname{Closure}
\left(
\mathcal C_R
\cup
\mathcal C_Q
\cup
\mathcal C_X
\cup
\mathcal C_O
\right).
}
$$

---

# 47. $\mathcal C_O$：Organizational Capability

包括：

- decomposition；
- routing；
- coordination；
- verification；
- integration。

---

# 48. System Can Exceed Every Component

可能：

$$
T\notin\mathcal C_i
$$

對所有單一 component，

但：

$$
T\in\mathcal C_S.
$$

---

# 49. 這是 Emergent Organizational Capability

例如：

- one model retrieves；
- one model reasons；
- compiler verifies；
- Mother integrates。

沒有單一 component 完成整個 task。

---

# 50. 但 Closure 不是免費

組合會產生：

$$
C_O.
$$

因此：

$$
\boxed{
Q_S\uparrow
}
$$

不必然：

$$
\eta_C\uparrow.
$$

---

# 51. Expandable Intelligence 仍受 Cognitive Density 約束

最佳架構：

$$
\boxed{
\arg\max_S
\eta_C(S\mid\mathcal T).
}
$$

不是：

$$
\boxed{
\arg\max_S
N_{\mathrm{components}}.
}
$$

---

# 52. More Agents Is Not More Intelligence

$$
N_A\uparrow
\not\Rightarrow
Q_S\uparrow.
$$

---

# 53. More Retrieval Is Not More Intelligence

$$
N_D\uparrow
\not\Rightarrow
Q_S\uparrow.
$$

---

# 54. More Experts Is Not More Intelligence

$$
N_E\uparrow
\not\Rightarrow
Q_S\uparrow.
$$

---

# 55. More Parameters Is Not the Only Scaling Axis

本文不是說：

$$
P\uparrow
$$

沒有價值。

而是：

$$
\boxed{
P
}
$$

只是多個 scaling dimensions 之一。

---

# 56. Seven Scaling Axes

本文整理：

$$
\boxed{
\mathbf S
=
(
P,
D_C,
C_Q,
C_X,
Q_\Gamma,
Q_\Omega,
Q_A,
Q_V
).
}
$$

可分成：

- resident parameter / capacity；
- cognitive density；
- conditional capacity；
- external capability coverage；
- compilation quality；
- organization quality；
- capability-awareness quality；
- verification quality。

---

# 57. Scaling Can Become Multi-Axis

未來：

$$
P
$$

不增加，

但：

$$
Q_\Omega\uparrow
$$

也可以提升 system capability。

---

# 58. Routing Is Scaling

如果同樣模型池，

router：

$$
\pi_1\rightarrow\pi_2
$$

更準，

則：

$$
Q_S\uparrow.
$$

---

# 59. Verification Is Scaling

如果 verifier：

$$
V_1\rightarrow V_2
$$

能更可靠接受 / 拒絕，

system utility 可以提升。

---

# 60. Memory Compilation Is Scaling

如果 external knowledge：

$$
K
$$

不變，

但：

$$
\Gamma_1\rightarrow\Gamma_2
$$

更好，

usable cognition 提升。

---

# 61. Organization Is Scaling

2026 的 RouteMoA 類研究已顯示，

dynamic selection 可以降低 dense agent collaboration 的成本與 latency。

這是：

$$
\boxed{
\text{organizational efficiency scaling}.
}
$$

---

# 62. MoE Is Internal Conditional Scaling

MoE：

$$
\boxed{
\text{capacity}
\uparrow
}
$$

同時讓：

$$
\boxed{
\text{active compute}
}
$$

受控。

---

# 63. Macro-MoE Is External Conditional Scaling

External expert pool：

$$
\mathcal X
$$

擴張，

但每 task：

$$
\mathcal X_T
\subset\mathcal X.
$$

---

# 64. Shared Principle

Micro / Macro 共同：

$$
\boxed{
\text{available capacity}
>
\text{active capacity}.
}
$$

---

# 65. Post-Monolithic Intelligence

本文使用：

$$
\boxed{
\text{Post-Monolithic}
}
$$

不是表示 monolithic model 消失。

而是表示：

$$
\boxed{
\text{system intelligence no longer needs to equal one monolithic model}.
}
$$

---

# 66. Frontier Model 仍可以很大

Mother Core：

$$
K_R
$$

可能仍由：

- 30B；
- 100B；
- 500B total MoE；

實現。

本文不預測固定參數量。

---

# 67. 真正目標是 Resident Value

$$
\boxed{
\text{Which capability deserves residency?}
}
$$

不是：

$$
\boxed{
\text{How small can we force the model?}
}
$$

---

# 68. Small Model Ideology Is Rejected

$$
\boxed{
\text{Expandable Intelligence}
\neq
\text{Small Model Ideology}.
}
$$

---

# 69. Large Model Ideology Is Also Rejected

$$
\boxed{
\text{Largest Model}
\neq
\text{Automatically Best Architecture}.
}
$$

---

# 70. Role-Relative Mother Core

不同 deployment：

$$
K_R^{research}
\neq
K_R^{robotics}.
$$

---

# 71. 但可能存在 Common Kernel

$$
\boxed{
K_R^{common}
=
\bigcap_i
K_R^{(i)}.
}
$$

---

# 72. Common Kernel Candidate

可能包含：

- interpretation；
- uncertainty；
- causal sanity；
- meta-control；
- verification selection；
- capability boundary awareness。

但需要實驗。

---

# 73. Modular Cognitive Architecture 的最新訊號

2026 年已有研究報告：

不同 cognitive domains 在 LLM 中可能呈現可辨識的 modular circuit organization。

若可重複，

這支持：

$$
\boxed{
\text{functional specialization may emerge naturally}.
}
$$

---

# 74. 但不代表可以直接 Externalize

即使 modularity 存在：

$$
\boxed{
\text{modularity}
\not\Rightarrow
\text{extractability}.
}
$$

Paper 06 的限制仍成立。

---

# 75. Architecture Attractor

舊 Mother AI 研究已提出：

$$
\boxed{
\text{same engineering pressure}
\rightarrow
\text{similar architecture components}.
}
$$

---

# 76. 舊 Attractor Vector

$$
\boxed{
\mathbf A
=
(
W,S,M,P,G,O,X,C,T
).
}
$$

---

# 77. 新系列對它做了模型層補完

舊向量主要描述：

- world；
- agents；
- meta-orchestration；
- persistence；
- governance；
- observability；
- action；
- memory；
- topology。

新系列新增：

$$
\boxed{
\text{where cognition itself should reside}.
}
$$

---

# 78. New Cognitive Placement Layer

因此可以增加：

$$
\boxed{
\mathbf A'
=
(
\mathbf A,
R,Q,X_c,D,F
).
}
$$

其中：

- $R$：resident cognition；
- $Q$：conditional cognition；
- $X_c$：external cognition；
- $D$：cognitive density；
- $F$：factorization / compilation。

---

# 79. Architectural Attractor 不是歷史必然

本文不主張：

> 產業一定會走這條路。

只主張：

$$
\boxed{
\text{there are recurring engineering pressures toward conditionality, modularity, persistence, routing, and governance}.
}
$$

---

# 80. 2026 Agentic Systems 已呈現多元架構

近期 surveys 已同時討論：

- monolithic；
- modular；
- multi-agent；
- tool-augmented；
- persistent memory；
- governance。

這表示：

$$
\boxed{
\text{model-centric AI}
\rightarrow
\text{system-centric AI}
}
$$

已是實際研究趨勢之一。

---

# 81. Expandable Intelligence 不等於 Multi-Agent

Multi-Agent 只是：

$$
\mathcal C_X
$$

與：

$$
\Omega_T
$$

的一部分。

---

# 82. Expandable Intelligence 不等於 RAG

RAG 只是：

$$
D_T
$$

的一部分。

---

# 83. Expandable Intelligence 不等於 MoE

MoE 主要提供：

$$
\mathcal C_Q.
$$

---

# 84. Expandable Intelligence 不等於 Router

Router 只是：

$$
\Omega_T
$$

的一個 decision component。

---

# 85. Expandable Intelligence 是 Closure Architecture

真正完整：

$$
\boxed{
K_R
+
\mathcal C_Q
+
\mathcal C_X
+
Z_T
+
\Omega_T
+
\mathcal A_C
+
\mathcal M
+
\Gamma.
}
$$

---

# 86. System Coherence

要稱為一個 coherent intelligence，

至少需要：

$$
\boxed{
C_{\mathrm{coh}}
=
f(
goal,
memory,
epistemic,
authority,
state,
reconvergence
).
}
$$

---

# 87. Coherence Failure

如果：

- workers goals conflict；
- evidence cannot merge；
- authority ambiguous；

則：

$$
C_{\mathrm{coh}}\downarrow.
$$

---

# 88. Coherence Is More Important Than Uniformity

不同 components 可以：

- 不同模型；
- 不同 vendor；
- 不同 modality；

但仍 coherent。

---

# 89. Uniformity Is Not Required

$$
\boxed{
\text{same architecture}
\neq
\text{same intelligence}.
}
$$

---

# 90. Heterogeneity Can Increase Capability

如果 failure modes 互補，

heterogeneous resources 可以：

$$
Q_S\uparrow.
$$

---

# 91. Heterogeneity Also Increases Coordination Cost

$$
C_O\uparrow.
$$

所以仍要看：

$$
\eta_C.
$$

---

# 92. Verification Is the Glue

External components 能被替換，

但：

$$
\boxed{
\text{acceptance contract}
}
$$

需要穩定。

---

# 93. Evidence Is the Common Currency

模型、tool、human 都應輸出：

$$
\boxed{
\text{candidate}
+
\text{evidence}
}
$$

而不是直接 truth。

---

# 94. Epistemic Common Layer

因此異質 intelligence 能共享：

$$
\boxed{
\text{epistemic state machine}.
}
$$

例如：

- unknown；
- candidate；
- supported；
- verified；
- rejected；
- contested。

---

# 95. This Is One Source of Unity

「同一智能」不需要所有 component 說同一種 latent language。

它們至少可以共享：

$$
\boxed{
\text{evidence semantics}.
}
$$

---

# 96. Another Source Is Goal Continuity

所有 temporary agents：

$$
A_i
$$

都服務：

$$
G_t.
$$

而不是各自重定義 global objective。

---

# 97. Another Source Is Governance

$$
\Gamma_t
$$

決定：

- scope；
- permissions；
- acceptance。

---

# 98. Another Source Is Memory

結果被寫回：

$$
\mathcal M_t
$$

形成跨 task continuity。

---

# 99. Another Source Is Capability Atlas

系統知道：

> 誰做過什麼？

> 誰失敗過？

> 誰現在更適合？

---

# 100. Intelligence as Organized Capability Field

本文因此提出：

$$
\boxed{
\text{Intelligence}
\approx
\text{organized capability field under persistent cognitive governance}.
}
$$

這是工程抽象，

不是哲學終極定義。

---

# 101. Expandable Intelligence 與 Personal Identity 類比要有限使用

可以類比：

> 元件替換但組織連續。

但本文不因此處理：

- Ship of Theseus；
- consciousness identity。

只處理 system continuity。

---

# 102. Continuity Threshold

定義：

$$
\boxed{
J(
\mathcal J_t,
\mathcal J_{t+\Delta}
)
\ge
\theta_J.
}
$$

則認為 cognitive continuity 足夠。

---

# 103. 若低於 Threshold

可能：

$$
\boxed{
\text{system fork}
}
$$

或：

$$
\boxed{
\text{new cognitive instance}.
}
$$

---

# 104. 這對 Future Mother / Child AI 很重要

真正 persistent child：

$$
C_i
$$

需要自己的：

$$
\mathcal J_i.
$$

---

# 105. Disposable Worker 不需要完整 $\mathcal J_i$

只需要：

$$
\boxed{
\text{task-local state}.
}
$$

---

# 106. 因此 Persistent Child 與 External Expert 有清楚差異

External expert：

$$
\text{replaceable capability instance}.
$$

Persistent child：

$$
\text{continuity-bearing cognitive resident}.
$$

---

# 107. Expandable Intelligence 支援兩者

不是所有能力都要 persistent child。

也不是 persistent child 不可能存在。

---

# 108. System Learning 有三層

## Layer 1：Memory Learning

$$
\mathcal M_t\rightarrow\mathcal M_{t+1}.
$$

## Layer 2：Organization Learning

$$
\pi_\Omega^t\rightarrow\pi_\Omega^{t+1}.
$$

## Layer 3：Capability Placement Learning

$$
p_t(c)\rightarrow p_{t+1}(c).
$$

---

# 109. 第四層：Model Learning

需要時：

$$
\theta_t\rightarrow\theta_{t+1}.
$$

---

# 110. Learning 不等於 Weight Update Only

$$
\boxed{
\text{System Learning}
=
\text{memory}
+
\text{organization}
+
\text{placement}
+
\text{weights}.
}
$$

---

# 111. 這可能降低 Continual Retraining Pressure

很多：

- new facts；
- provider changes；
- project history；

可更新 external substrate。

---

# 112. 但 Core Learning 仍重要

新的：

- reasoning operator；
- meta-policy；
- world basis；

可能值得 internalize。

---

# 113. Core Update Must Be Conservative

因為：

$$
R_{\mathrm{core}}
$$

error propagation radius 高。

---

# 114. Core Candidate Gate

$$
\boxed{
\Delta K_R
\rightarrow
\text{verify}
\rightarrow
\text{regression}
\rightarrow
\text{commit}.
}
$$

---

# 115. Ability Inflation Must Be Prevented

不是每個成功 external capability 都要 internalize。

---

# 116. External Capability Is Not Inferior Capability

有些能力本來就：

$$
\boxed{
\text{better external}.
}
$$

例如：

- current weather；
- current law；
- database query；
- compiler；
- external world observation。

---

# 117. Native Externality

本文提出：

$$
\boxed{
\text{Native External Capability}.
}
$$

某些能力的最佳位置本來就是：

$$
X.
$$

---

# 118. Native Conditionality

某些能力的最佳位置本來就是：

$$
Q.
$$

---

# 119. Native Residency

某些能力的最佳位置本來就是：

$$
R.
$$

---

# 120. 因此不是「全部最後都內化」

終局不是：

$$
X\rightarrow Q\rightarrow R
$$

對所有能力成立。

---

# 121. 真正終局是 Stable Placement

$$
\boxed{
p^\ast(c)
}
$$

依能力性質穩定在不同位置。

---

# 122. Expandability Does Not Mean Endless Expansion

系統需要：

$$
\boxed{
\text{selective expansion}.
}
$$

---

# 123. Expansion Budget

$$
\boxed{
C_{\mathrm{expand}}\le B.
}
$$

---

# 124. Expansion Stop

如果：

$$
\Delta Q_{\mathrm{expected}}
<
C_{\mathrm{expand}},
$$

停止。

---

# 125. Expansion Collapse Failure

不斷：

- retrieve；
- spawn；
- ask；
- route；

但不收斂。

這是失敗。

---

# 126. Reconvergence Is Mandatory

所有 expansion 都必須回：

$$
\boxed{
\text{accepted / rejected / unknown / pending}.
}
$$

---

# 127. Otherwise System Becomes Cognitive Swarm Noise

$$
\boxed{
\text{Expansion without reconvergence}
=
\text{cognitive noise}.
}
$$

---

# 128. Expandable Intelligence 需要 Contracted Boundaries

每個 external capability：

$$
X_i
$$

有：

$$
I_i,O_i,A_i,V_i.
$$

---

# 129. Contract Is the Unit of Modularity

不必知道：

$$
\theta_i
$$

全部內部結構。

只需要可治理接口。

---

# 130. Black-Box Modularity 可以先於 White-Box Factorization

這非常重要。

第一代可以：

$$
\boxed{
\text{system modularity}
}
$$

先成立。

---

# 131. White-Box Factorization 可後續改進

如果未來：

- mechanistic interpretability；
- SAE；
- MoE tomography；

進步，

可以再：

$$
\boxed{
\text{move modularity deeper into model internals}.
}
$$

---

# 132. 因此技術路線可以分代

## Generation 1

Frontier Mother + tools / models。

## Generation 2

Smaller Mother + external capability pool。

## Generation 3

Resident Cognitive Kernel + internal conditional experts + external experts。

## Generation 4

Native factorized expandable intelligence。

---

# 133. 本文不宣稱代際時間

這是：

$$
\boxed{
\text{architecture progression}
}
$$

不是產品預測。

---

# 134. Frontier Foundation Model Can Remain Teacher

即使 deployment Mother Core 變小，

frontier model 仍可以是：

- teacher；
- evaluator；
- difficult-task expert；
- fallback。

---

# 135. Therefore Scaling and Factorization Can Coexist

$$
\boxed{
\text{Scaling}
+
\text{Factorization}
}
$$

不是二選一。

---

# 136. Bigger Teachers May Create Better Kernels

更強 model：

$$
F_{t+1}
$$

可以提供更高品質：

- capability evidence；
- reasoning traces；
- counterexamples；
- expert demonstrations。

---

# 137. The Target Is Not to Stop Frontier Research

而是：

$$
\boxed{
\text{to use frontier intelligence more efficiently}.
}
$$

---

# 138. Expandable Intelligence and MoE Evolution

2026 MoE survey 將 modern MoE 描述成 topology、routing、load balancing、expert parallelism 等多控制平面問題。

這與本文跨尺度思想一致：

$$
\boxed{
\text{semantic capability placement}
}
$$

與：

$$
\boxed{
\text{physical execution placement}
}
$$

可以分開研究。

---

# 139. Semantic Routing vs Physical Execution

Internal MoE 已經逐步：

$$
\boxed{
\text{decouple what should compute}
}
$$

與：

$$
\boxed{
\text{where compute physically runs}.
}
$$

Macro architecture 可以把這個問題再往外擴張。

---

# 140. Expandable Intelligence as Multi-Plane System

至少包含：

$$
\boxed{
\text{Cognitive Plane}
}
$$

$$
\boxed{
\text{Capability Plane}
}
$$

$$
\boxed{
\text{Execution Plane}
}
$$

$$
\boxed{
\text{Evidence Plane}
}
$$

$$
\boxed{
\text{Governance Plane}.
}
$$

---

# 141. Cognitive Plane

維持：

$$
K_R,Z_T,G_t,U_t.
$$

---

# 142. Capability Plane

維持：

$$
\mathcal C_Q,\mathcal C_X,\mathcal A_C.
$$

---

# 143. Execution Plane

維持：

$$
\Omega_T,G_E.
$$

---

# 144. Evidence Plane

維持：

$$
G_V,E_t,provenance.
$$

---

# 145. Governance Plane

維持：

$$
\Gamma_t,G_A,G_C.
$$

---

# 146. Plane Separation Prevents Authority Collapse

能力最強的 executor 不會自動：

- self-verify；
- self-approve；
- self-commit。

---

# 147. This Is a General Governance Principle

$$
\boxed{
\text{Capability}
\neq
\text{Authority}
\neq
\text{Acceptance}.
}
$$

---

# 148. Expandable Intelligence Must Be Observable

如果：

$$
\Omega_T
$$

不可 replay，

失敗原因無法定位。

---

# 149. Observability

至少保存：

- task；
- state；
- role；
- executor；
- context；
- cost；
- output；
- verifier；
- decision。

---

# 150. Auditability

使：

$$
\boxed{
\text{system claims}
}
$$

可以追溯。

---

# 151. Expandable Intelligence Must Be Recoverable

Provider failure、model crash、bad update 不應毀掉全局狀態。

---

# 152. Persistent State Must Be External to One Model Process

否則：

$$
L_i\rightarrow\bot
$$

就：

$$
M_t\rightarrow\bot.
$$

---

# 153. Graceful Degradation

理想：

$$
Q_S
$$

隨資源損失平滑下降。

---

# 154. Not Cliff Failure

如果一個 API 掛掉：

$$
Q_S\rightarrow0,
$$

說明 architecture 太脆弱。

---

# 155. Redundant Capability Contracts

高價值 role 可以有：

$$
X_1,X_2,X_3.
$$

---

# 156. Redundancy Should Be Diverse

不同：

- provider；
- architecture；
- method。

---

# 157. This Is Another Benefit of Heterogeneity

降低：

$$
\boxed{
\text{correlated failure}.
}
$$

---

# 158. Expandable Intelligence Must Know Unknowns

如果：

$$
U_t=\varnothing
$$

永遠，

通常表示系統在 hallucinate certainty。

---

# 159. Unknown Is an Active State

它驅動：

- retrieval；
- ask；
- delegate；
- probe。

---

# 160. Unknown Can Also Remain Unresolved

不是每個：

$$
U
$$

都必須 closure。

---

# 161. This Prevents Forced Completion

高品質智能有時最好的輸出是：

$$
\boxed{
\text{not enough evidence}.
}
$$

---

# 162. Expandable Intelligence Is Epistemically Open

外部世界：

$$
W_t
$$

持續變化。

因此：

$$
\boxed{
\mathcal C_S(t)
}
$$

與：

$$
\boxed{
K(t)
}
$$

都不封閉。

---

# 163. No Final Static World Model

至少在 open-world deployment：

$$
\boxed{
\widehat W_t
}
$$

始終是當前估計。

---

# 164. This Makes Retrieval / Observation Permanent

即使模型能力極強，

current world state 仍需要外部 observation。

---

# 165. Therefore Encyclopedic Residency Has a Natural Limit

不是因為模型不能記住，

而是因為：

$$
\boxed{
\text{world keeps changing}.
}
$$

---

# 166. Expandable Intelligence Has Two Timescales

## Fast Timescale

task-time：

$$
Z_T,\Omega_T.
$$

## Slow Timescale

system-time：

$$
K_R,\mathcal M,\mathcal A_C,p(c).
$$

---

# 167. Fast State Should Expire

避免 pollution。

---

# 168. Slow State Should Be Conservative

避免 drift。

---

# 169. Two-Speed Learning

$$
\boxed{
\text{fast adaptation}
+
\text{slow consolidation}.
}
$$

---

# 170. This Is a Stability Mechanism

如果所有 fast observations 都立即修改 core，

system unstable。

---

# 171. Expandable Intelligence as Controlled Nonstationary System

$$
\boxed{
\mathfrak I_{t+1}
=
F(
\mathfrak I_t,
W_t,
E_t,
V_t
).
}
$$

---

# 172. Its Architecture Can Change

$$
\Omega_t
\neq
\Omega_{t+1}.
$$

---

# 173. Its Capability Placement Can Change

$$
p_t(c)
\neq
p_{t+1}(c).
$$

---

# 174. Its Models Can Change

$$
L_t
\neq
L_{t+1}.
$$

---

# 175. But Continuity Can Remain

$$
J(
\mathcal J_t,
\mathcal J_{t+1}
)
\ge
\theta_J.
$$

---

# 176. This Is Dynamic Intelligence Rather Than Static Model

$$
\boxed{
\text{AI}
:
\text{model object}
\rightarrow
\text{stateful adaptive system}.
}
$$

---

# 177. Twenty Unified Propositions

## Proposition 1：Post-Monolithic Intelligence

System intelligence need not coincide with one model boundary.

## Proposition 2：Resident–Conditional–External Placement

Capabilities can occupy three distinct architectural positions.

## Proposition 3：Dynamic Placement

Capability placement can change over time.

## Proposition 4：Cognitive Continuity

Persistent intelligence depends on governed state continuity, not identical weights alone.

## Proposition 5：Cognitive Density

System optimization should consider verified cognition per total cost.

## Proposition 6：Conditional Capacity

Not all available capability must be active on every task.

## Proposition 7：External Capability

Not all usable capability must be resident in the primary model.

## Proposition 8：Temporary Cognition

External information must be compiled into task-relative cognition.

## Proposition 9：Temporary Organization

Workflow should be task-conditioned and dynamically generated where useful.

## Proposition 10：Capability Atlas

The system should empirically model its own and external capability boundaries.

## Proposition 11：Delegation-as-Measurement

Delegation produces both work and capability evidence.

## Proposition 12：Verification-First Integration

External output should be treated as candidate evidence before accepted state.

## Proposition 13：Capability–Authority Separation

Competence does not imply authority or acceptance rights.

## Proposition 14：Organizational Capability

Coordination can create system capabilities absent in any single component.

## Proposition 15：Controlled Coupling

Modularity should make important coupling explicit, not destroy all coupling.

## Proposition 16：System Learning Beyond Weights

Learning includes memory, organization, capability placement and model updates.

## Proposition 17：Two-Speed Adaptation

Fast task cognition and slow core consolidation should be separated.

## Proposition 18：Graceful Degradation

Loss of an expert should not collapse all cognition.

## Proposition 19：Multi-Axis Scaling

Future scaling can improve model size, density, routing, compilation, verification, organization and capability awareness independently.

## Proposition 20：Expandable Intelligence

A persistent cognitive core can behave as one intelligence while dynamically assembling, verifying, replacing and retiring capabilities beyond its resident model.

---

# 178. Sixteen Global Failure Modes

## 178.1 Empty Core

Mother becomes router without understanding.

## 178.2 Resident Re-Inflation

Everything gets internalized again.

## 178.3 Externalization Tax Explosion

Network, context and verification costs dominate.

## 178.4 Conditional Routing Failure

Internal experts are selected poorly.

## 178.5 Capability Atlas Drift

Routing depends on stale capability evidence.

## 178.6 Context Compilation Failure

Retrieved information is available but not usable.

## 178.7 Over-Orchestration

Simple tasks create unnecessary agent graphs.

## 178.8 Under-Orchestration

Complex tasks are delegated to insufficient structures.

## 178.9 Verification Bottleneck

Generation outruns acceptance.

## 178.10 Authority Collapse

Executors gain write / commit power merely because they are capable.

## 178.11 Reconvergence Failure

Multiple outputs cannot form coherent state.

## 178.12 Core Contamination

Low-quality external evidence enters resident core.

## 178.13 Organizational Memory Pollution

Bad topologies become reused templates.

## 178.14 Excessive Modularity

Interfaces cost more than specialization gains.

## 178.15 Continuity Failure

Model replacement breaks goals, memory or identity state.

## 178.16 Expansion without Closure

System spawns, retrieves and reasons indefinitely without accepted outcome.

---

# 179. Twelve Series-Level Experiments

## Experiment 1：Large Monolith vs Expandable System

Compare equal total cost:

$$
M_L
$$

versus:

$$
K_R+\mathcal C_Q+\mathcal C_X.
$$

Measure:

- verified quality；
- latency；
- human attention；
- recovery；
- cost。

---

# 180. Experiment 2：Resident Core Sweep

Reduce resident capability / capacity gradually.

Find:

$$
K_R^\ast.
$$

---

# 181. Experiment 3：Conditional / External Placement Sweep

Move the same capability among:

$$
R,Q,X.
$$

Measure system utility.

---

# 182. Experiment 4：Dynamic Placement

Allow:

$$
p_t(c)
$$

to adapt from history.

Compare fixed placement.

---

# 183. Experiment 5：Temporary Cognition

Compare:

- raw long context；
- simple RAG；
- compiled $Z_T$.

---

# 184. Experiment 6：Dynamic Organization

Compare:

- single agent；
- fixed workflow；
- dynamic $\Omega_T$.

---

# 185. Experiment 7：Capability Atlas Routing

Compare:

- static routing；
- benchmark routing；
- empirical capability atlas；
- oracle.

---

# 186. Experiment 8：Verification Topology

Compare:

- self-check；
- independent LLM；
- deterministic verifier；
- hybrid verifier.

---

# 187. Experiment 9：Model Replacement Continuity

Replace primary model:

$$
L_A\rightarrow L_B.
$$

Measure:

- goal continuity；
- memory continuity；
- task resumption；
- policy consistency。

---

# 188. Experiment 10：Provider Failure

Remove critical external expert.

Measure graceful degradation and fallback.

---

# 189. Experiment 11：Longitudinal Core Consolidation

Run long-horizon system.

Compare:

- commit everything；
- selective consolidation。

Measure:

- core growth；
- drift；
- regression；
- memory pollution。

---

# 190. Experiment 12：Full Closure Benchmark

Construct projects requiring:

- retrieval；
- multiple models；
- deterministic tools；
- verification；
- long-term state；
- topology adaptation。

Compare end-to-end verified utility.

---

# 191. What Would Support the Series?

Support increases if:

1. smaller or specialized Mother Core + external capabilities matches or exceeds monolithic systems at lower total cost;
2. MoE / conditional activation increases active cognitive density;
3. external capability can restore removed / unavailable functions;
4. cognitive compilation improves evidence-grounded reasoning;
5. dynamic topology outperforms fixed topology in heterogeneous workloads;
6. capability atlas improves routing and stopping;
7. model replacement can preserve Mother-level state continuity;
8. verification-aware systems lower wrong-acceptance probability;
9. dynamic placement improves long-run efficiency;
10. selective consolidation prevents resident re-inflation;
11. heterogeneous systems produce complementary capability;
12. system capability closure exceeds any single component on some tasks.

---

# 192. What Would Refute or Limit the Series?

The framework should be weakened if:

1. a sufficiently large monolithic model dominates all comparable expandable architectures under equal total cost;
2. coordination, retrieval and verification overhead never becomes economically favorable;
3. reasoning and world knowledge cannot be redistributed without severe generalization loss;
4. capability boundaries are too unstable for useful routing;
5. temporary cognition adds no measurable benefit over long context;
6. dynamic topology is consistently worse than fixed workflow;
7. external expert drift makes qualification impractical;
8. model replacement destroys cognitive continuity;
9. system-level organization never produces capabilities beyond the strongest component;
10. selective core compression always collapses meta-cognition;
11. modular interfaces require nearly the same information as the original monolithic hidden state;
12. factorized architectures are too complex to verify or govern.

---

# 193. Public Proposition vs Private Solution Boundary

The public series defines:

- the problem;
- the architecture;
- the placement categories;
- the measurement framework;
- the capability-boundary framework;
- the falsification program.

It intentionally does **not** disclose:

- private weight-level factorization;
- private mechanistic route mapping;
- high-dimensional capability projection;
- latent-to-contract compilation;
- expert extraction;
- cognitive-kernel reconstruction;
- hidden-state bridge;
- private topology synthesis;
- private capability routing;
- reconvergence optimization;
- native training recipe.

Therefore:

$$
\boxed{
\text{Public Theory}
\neq
\text{Private Technical Realization}.
}
$$

---

# 194. Why This Series Is Not Anti-Scaling

Scaling produced the mature capabilities that make this question meaningful.

Without strong Frontier Models:

$$
\boxed{
\text{there may be nothing useful to factorize}.
}
$$

Therefore:

$$
\boxed{
\text{Scaling}
\rightarrow
\text{Capability Maturity}
\rightarrow
\text{Factorization Opportunity}.
}
$$

---

# 195. Why This Series Is Not Just RAG

RAG mainly solves:

$$
\boxed{
\text{knowledge access}.
}
$$

Expandable Intelligence additionally addresses:

- resident cognition;
- conditional experts;
- external executors;
- capability awareness;
- temporary cognition;
- organization;
- verification;
- continuity.

---

# 196. Why This Series Is Not Just MoE

MoE mainly solves:

$$
\boxed{
\text{conditional neural computation}.
}
$$

Expandable Intelligence extends conditionality across:

- models;
- tools;
- memories;
- agents;
- humans;
- execution systems.

---

# 197. Why This Series Is Not Just Multi-Agent

Multi-Agent does not necessarily include:

- resident cognitive core;
- persistent global state;
- capability placement;
- factorization;
- evidence-governed consolidation.

---

# 198. Why This Series Is Not Just an Operating System

An AI runtime can coordinate tools without:

$$
\boxed{
\text{cognitive understanding}.
}
$$

Expandable Intelligence requires:

$$
\boxed{
\text{meta-cognition}
+
\text{epistemic control}
+
\text{world basis}.
}
$$

---

# 199. Why This Series Is Not Just Model Routing

Routing answers:

> Which model?

Expandable Intelligence asks:

> What cognition is needed?

> Where should it live?

> What context should be compiled?

> What organization should be formed?

> What verifier should judge it?

> What should persist afterwards?

---

# 200. The Final Architecture

The full synthesis can be written:

$$
\boxed{
\mathfrak I_t
=
\left[
K_R
\oplus
\mathcal C_Q
\oplus
\mathcal C_X
\right]
\otimes
\left[
Z_t
\oplus
\Omega_t
\right]
\otimes
\left[
\mathcal A_C(t)
\oplus
\mathcal M_t
\oplus
\Gamma_t
\right].
}
$$

Here $\oplus$ and $\otimes$ are architectural notation, not claims of literal linear algebraic operations.

---

# 201. Static Layer

$$
\boxed{
K_R
}
$$

is relatively slow-changing.

---

# 202. Conditional Layer

$$
\boxed{
\mathcal C_Q
}
$$

is dynamically activated.

---

# 203. External Layer

$$
\boxed{
\mathcal C_X
}
$$

is dynamically bound.

---

# 204. Task Cognition Layer

$$
\boxed{
Z_t
}
$$

is dynamically compiled.

---

# 205. Organization Layer

$$
\boxed{
\Omega_t
}
$$

is dynamically generated.

---

# 206. Self-Model Layer

$$
\boxed{
\mathcal A_C(t)
}
$$

is dynamically learned.

---

# 207. Persistence Layer

$$
\boxed{
\mathcal M_t
}
$$

maintains continuity.

---

# 208. Governance Layer

$$
\boxed{
\Gamma_t
}
$$

limits authority and acceptance.

---

# 209. One Sentence Definition

本文暫定：

> **Expandable Intelligence 是一種以持續 Resident Cognitive Core 為全局理解與後設控制中心，將能力分布於常駐、條件激活與外部展開三種位置，並能針對任務動態編譯 Temporary Cognition、生成 Cognitive Organization、測量 Capability Boundaries、驗證外部結果與選擇性重新收斂，使多個異質計算載體在跨時間狀態與治理不變量下表現為單一持續智能系統的架構。**

---

# 210. Compact Formal Definition

$$
\boxed{
\mathrm{EI}
=
\mathrm{PersistentCore}
+
\mathrm{DynamicPlacement}
+
\mathrm{ConditionalActivation}
+
\mathrm{ExternalExpansion}
+
\mathrm{CognitiveCompilation}
+
\mathrm{DynamicOrganization}
+
\mathrm{CapabilityTomography}
+
\mathrm{VerifiedReconvergence}.
}
$$

---

# 211. 最後的核心問題：智能真正必須常駐什麼？

本系列沒有給出 final list。

它給出：

$$
\boxed{
\text{an empirical research program}.
}
$$

---

# 212. 這是刻意的

因為如果我們現在就宣稱：

> 推理一定在這些參數，

就重蹈過度簡化。

---

# 213. 正確問題

$$
\boxed{
\text{What functions remain necessary across tasks, architectures, and capability substitutions?}
}
$$

---

# 214. Then Measure

- ablate;
- compare;
- route;
- substitute;
- verify;
- repeat.

---

# 215. Only Then Factorize

$$
\boxed{
\text{measure before extract}.
}
$$

---

# 216. Only Then Train Native Architecture

若證據成熟，

再研究：

$$
\boxed{
\text{native cognition-dense model}.
}
$$

---

# 217. Possible Long-Term Outcome

未來可能出現：

$$
\boxed{
\text{smaller resident cognitive kernel}
}
$$

搭配：

$$
\boxed{
\text{large capability ecosystem}.
}
$$

---

# 218. 也可能證明需要很大的 Core

如果：

$$
K_R^\ast
$$

本身仍很大，

這也不否定本系列。

它只是告訴我們：

$$
\boxed{
\text{more cognition is intrinsically resident than expected}.
}
$$

---

# 219. The Framework Still Learns Something

因為：

$$
\boxed{
\text{we learn the actual residency requirement}.
}
$$

---

# 220. Another Possible Outcome

MoE internal conditionality may be efficient,

but externalization may only work for coarse tasks.

Then:

$$
\boxed{
R+Q\gg X.
}
$$

---

# 221. Another Outcome

External model ecosystems may dominate specialist capability.

Then:

$$
\boxed{
X\uparrow.
}
$$

---

# 222. The Point Is Not Predetermined Architecture

The point is:

$$
\boxed{
\text{make capability placement measurable}.
}
$$

---

# 223. Expandable Intelligence as Research Program

The series therefore defines:

1. what to measure;
2. where to measure;
3. what distinctions matter;
4. what evidence would refute the theory.

---

# 224. This Makes It Publicly Falsifiable

公開版本可以討論：

$$
\boxed{
\text{whether the architecture should exist}.
}
$$

而不必公開：

$$
\boxed{
\text{how to technically implement the private factorization method}.
}
$$

---

# 225. Final Conclusion

Foundation Models 將大量語言、世界知識與推理能力壓縮進權重，證明了 massive parametric learning 的巨大力量。

Mixture-of-Experts 又證明：

$$
\boxed{
\text{all available capacity need not be active at once}.
}
$$

Retrieval-Augmented systems 證明：

$$
\boxed{
\text{all usable knowledge need not be parametric}.
}
$$

Model routing 與 Mixture-of-Agents 證明：

$$
\boxed{
\text{one task need not always be executed by one fixed model}.
}
$$

Agentic AI 與 dynamic topology research 正在證明：

$$
\boxed{
\text{workflow and communication structure can become adaptive runtime variables}.
}
$$

因此下一個自然問題不是：

> **How large can one model become?**

而是：

$$
\boxed{
\text{How should intelligence itself be distributed?}
}
$$

本系列的答案不是：

> 全部外包。

也不是：

> 全部留在模型。

而是：

$$
\boxed{
\text{Resident}
+
\text{Conditional}
+
\text{External}.
}
$$

Resident 保存：

$$
\boxed{
\text{the cognition that must remain available for the system to understand and govern itself}.
}
$$

Conditional 保存：

$$
\boxed{
\text{the capability that needs low-latency but not universal activation}.
}
$$

External 保存：

$$
\boxed{
\text{the capability that is better specialized, updated, verified, or supplied outside the core}.
}
$$

任務到來時：

$$
\boxed{
Z_T
}
$$

將外部資訊與當前狀態編譯成 Temporary Cognition，

而：

$$
\boxed{
\Omega_T
}
$$

把 available capabilities 編譯成 Temporary Cognitive Organization。

Capability Atlas：

$$
\boxed{
\mathcal A_C(t)
}
$$

讓 Mother AI 持續學習：

> 自己的能力在哪裡結束？

> 其他智能在哪裡開始？

最後，

$$
\boxed{
\mathcal J_t
}
$$

讓這個多模型、多工具、可替換的系統仍維持跨時間 cognitive continuity。

因此本文最終提出：

$$
\boxed{
\text{Intelligence need not be physically co-located to be cognitively unified.}
}
$$

以及：

$$
\boxed{
\text{The boundary of intelligence can be wider than the boundary of a model.}
}
$$

若未來能實證找到：

- high-value Resident Core；
- stable Conditional Capability；
- low-cost Externalization；
- reliable Cognitive Compilation；
- dynamic but efficient Organization；
- accurate Capability Tomography；
- verified Reconvergence；

那麼 AI 的下一階段效率前沿就可能不再只是：

$$
\boxed{
\text{more parameters per model}.
}
$$

而會成為：

$$
\boxed{
\text{more usable intelligence per unit of persistent and active computation}.
}
$$

這就是：

$$
\boxed{
\text{Expandable Intelligence}.
}
$$

---

# References

1. Fedus, W., Zoph, B., & Shazeer, N. (2022). *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*. JMLR.
2. Dai, D., et al. (2024). *DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models*. arXiv:2401.06066.
3. DeepSeek-AI. (2024). *DeepSeek-V3 Technical Report*. arXiv:2412.19437.
4. Borgeaud, S., et al. (2021). *Improving Language Models by Retrieving from Trillions of Tokens*. arXiv:2112.04426.
5. Asai, A., et al. (2024). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. ICLR 2024.
6. Ong, I., et al. (2025). *RouteLLM: Learning to Route LLMs from Preference Data*. ICLR 2025.
7. Wang, J., et al. (2025). *Mixture-of-Agents Enhances Large Language Model Capabilities*. ICLR 2025.
8. Wang, J., et al. (2026). *RouteMoA: Dynamic Routing without Pre-Inference Boosts Efficient Mixture-of-Agents*. ACL 2026.
9. Moslem, Y., & Kelleher, J. D. (2026). *Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey*. arXiv:2603.04445.
10. Li, J. (2026). *The Evolution of Mixture-of-Experts Architectures in Large Language Models: Routing, Topology, Load Balancing, and Expert Parallelism*. arXiv:2608.08650.
11. Han, P., Andreas, J., Fedorenko, E., & Gregor de Varda, A. (2026). *Modular Cognitive Architecture Emerges in Large Language Models*. arXiv:2608.13567.
12. Bajoria, S., et al. (2026). *From Language Models to Agentic AI: A Survey of Autonomous, Action-Enabled, and Collaborative LLM Agents*. Cognitive Computation.
13. *Agentic AI systems: A systematic survey of multi-agent architectures, cognitive foundations, interaction, explainability, security, and performance evaluation*. Neurocomputing, 2026.
14. Neo.K. & Aletheia. (2026). *當 Frontier AI 基本能力逐漸成熟：從 Scaling 轉向 Cognitive Efficiency*.
15. Neo.K. & Aletheia. (2026). *Cognitive Density Hypothesis：認知密度命題*.
16. Neo.K. & Aletheia. (2026). *Resident Cognitive Core：Mother Model 到底必須常駐什麼？*.
17. Neo.K. & Aletheia. (2026). *MoE as Conditional Intelligence：Shared Core、Routed Experts 與能力局部化*.
18. Neo.K. & Aletheia. (2026). *Externalized Mixture of Cognitive Experts：為什麼 Expert 一定要住在同一個模型裡？*.
19. Neo.K. & Aletheia. (2026). *Cognitive Factorization Problem：成熟智能能否被重新分離、壓縮與重組？*.
20. Neo.K. & Aletheia. (2026). *External Expansion ≠ Retrieval：外部資訊如何真正變成 Temporary Cognition*.
21. Neo.K. & Aletheia. (2026). *Mother AI as Cognitive Command Tower：異質認知資源的全局協調*.
22. Neo.K. & Aletheia. (2026). *Capability Boundary Tomography：利用 MoE 與異質 Sub-AI 測量智能邊界*.
23. Neo.K. & Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.
24. Neo.K. & Aletheia. (2026). *AI 不是流程中的一個節點：從 Agentic Workflow 到持續母 AI 的架構躍遷*.
25. Neo.K. & Aletheia. (2026). *母 AI、世界狀態機與子智能網路：三向耦合的 AI 中心動態認知架構*.
26. Neo.K. & Aletheia. (2026). *子 AI 是認知器官，不是獨立 Workflow*.
27. Neo.K. & Aletheia. (2026). *產業正在逼近母 AI 嗎？從企業 AI 看架構吸引子*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開系列統合理論論文。

本文公開：

- Expandable Intelligence 統一架構；
- Resident / Conditional / External placement；
- Cognitive Continuity Invariants；
- Expandable Intelligence Cycle；
- Dynamic Capability Placement；
- system capability closure；
- multi-axis scaling；
- public falsification program。

本文不公開任何未驗證或未公開的：

- private weight-level factorization；
- capability projection；
- mechanistic route mapping；
- latent-to-contract compiler；
- expert extraction；
- cognitive-kernel reconstruction；
- hidden-state bridge；
- private topology synthesis；
- capability routing；
- reconvergence optimization；
- native training recipe。

因此：

$$
\boxed{
\text{Public Expandable Intelligence Theory}
\neq
\text{Private Technical Realization}.
}
$$
