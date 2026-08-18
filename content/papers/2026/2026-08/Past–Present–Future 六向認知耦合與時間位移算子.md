# Past–Present–Future 六向認知耦合與時間位移算子

**Six-Way Temporal Coupling: A Unified Shift Operator for Past–Present–Future Cognitive Dynamics**

**Tri-Temporal Cognitive Dynamics — 三生認知耦合動力學系列**  
**TCD-07 / Unified Synthesis I**

作者：Neo.K（許筌崴）  
協作形式化：Aletheia  
機構：一言諾科技有限公司（EveMissLab）  
日期：2026-08-17  
版本：v0.1  
狀態：TCD first unified dynamics paper / six-way coupling synthesis

---

## Canonical Non-Identity Statement

TCD-01 至 TCD-06 已分別建立：

$$
\boxed{
\mathcal B_t^-,
\qquad
\mathcal B_t^0,
\qquad
\mathcal B_t^+
}
$$

以及六個方向的機制雛型。

本文第一次統一：

$$
\boxed{
\mathfrak T_t^{(3)}
=
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
)
}
$$

並建立時間位移：

$$
\boxed{
\mathscr S_t:
\mathfrak T_t^{(3)}
\rightarrow
\mathfrak T_{t+1}^{(3)}.
}
$$

但永久保留：

$$
\boxed{
\text{Six Coupling Directions}
\neq
\text{Six Identical Operators}.
}
$$

以及：

$$
\boxed{
\text{Temporal Coupling}
\neq
\text{Physical Retrocausality}.
}
$$

本文不主張：

- Past、Present、Future 是三個本體上獨立的宇宙層；
- 六條箭頭具有同樣的數學型別；
- Future Event 會物理地改變 Past Fact；
- 任何 agent 都需要完整六向 coupling；
- 六向 coupling 越強 intelligence 越高；
- TCD 是一般認知科學的已證實普遍定律；
- 同一時間內的 iterative deliberation 是時間旅行；
- 所有 coupling 都會收斂；
- TCD 可直接取代 POMDP、MPC、RL、world models、memory systems 或 causal models；
- 本文已給出完整跨域實證證明。

---

# 摘要

Tri-Temporal Cognitive Dynamics（TCD）前六篇依序完成三個時間底座與六個 directional couplings。

Past：

$$
\boxed{
\mathcal B_t^-
=
\text{compressed historical choice lineage}.
}
$$

Present：

$$
\boxed{
\mathcal B_t^0
=
\text{historically conditioned actionable / reachable domain}.
}
$$

Future：

$$
\boxed{
\mathcal B_t^+
=
\text{agent-generated prospective possibility domain}.
}
$$

六個方向分別為：

$$
\boxed{
\begin{array}{lll}
\mathcal B^- \rightarrow \mathcal B^0
&:&
\text{Historical Conditioning},\\
\mathcal B^0 \rightarrow \mathcal B^+
&:&
\text{Present-Conditioned Future Generation},\\
\mathcal B^+ \rightarrow \mathcal B^0
&:&
\text{Prospective Attraction},\\
\mathcal B^0 \rightarrow \mathcal B^-
&:&
\text{Historical Sedimentation},\\
\mathcal B^- \rightarrow \mathcal B^+
&:&
\text{Historical Projection},\\
\mathcal B^+ \rightarrow \mathcal B^-
&:&
\text{Retrospective Relevance}.
\end{array}
}
$$

本文最重要的第一個統一原則是：

$$
\boxed{
\textbf{the six arrows are typed}.
}
$$

它們分別可能是：

- state construction；
- candidate generation；
- policy valuation；
- provenance / dependency sedimentation；
- historical projection；
- relevance reweighting。

因此不能把：

$$
\mathcal B^-
,
\mathcal B^0
,
\mathcal B^+
$$

當成三個 ordinary vectors，再把六條 coupling 當同一種線性 matrix edge。

本文定義 typed temporal coupling graph：

$$
\boxed{
G_{\mathrm{TCD},t}
=
(
V_t,
E_t,
\tau_E
),
}
$$

其中：

$$
V_t
=
\{
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
\},
$$

而：

$$
\tau_E:
E_t
\rightarrow
\{
Condition,
Generate,
Attract,
Sediment,
Project,
Reweight
\}
$$

記錄每條 edge 的 operator type。

本文進一步解決一個形式上的核心問題：如果在同一時刻同時寫：

$$
\mathcal B_t^+
\rightarrow
\mathcal B_t^0
\rightarrow
\mathcal B_t^+
$$

以及：

$$
\mathcal B_t^+
\rightarrow
\mathcal B_t^-
\rightarrow
\mathcal B_t^+,
$$

表面上會形成 circular definition。

因此本文區分：

$$
\boxed{
t
=
\text{environment / historical time index}
}
$$

與：

$$
\boxed{
k
=
\text{within-step deliberation index}.
}
$$

在同一 physical / historical time $t$ 中，agent 可以執行 bounded deliberation：

$$
\boxed{
\mathcal B_t^{+,(k)}
\rightarrow
\mathbf w_t^{-,(k)}
\rightarrow
\pi_t^{(k)}
\rightarrow
\mathcal B_t^{+,(k+1)},
}
$$

但只要：

$$
a_t
$$

尚未對環境執行，

就仍然位於：

$$
\boxed{
t.
}
$$

真正 time shift 發生在 action execution 與 environment transition 之後：

$$
\boxed{
Z_t
\xrightarrow{a_t}
Z_{t+1}.
}
$$

本文因此提出一個完整 staged update：

$$
\boxed{
\begin{aligned}
\widetilde{\mathcal B}_t^0
&=
\Phi_{-0}
(
\mathcal B_t^-,
\Xi_t
),
\\
\mathcal B_t^{+,(0)}
&=
\Gamma_F
(
\mathcal B_t^-,
\widetilde{\mathcal B}_t^0,
\Xi_t
),
\\
\mathbf w_t^{-,(k)}
&=
\mathcal R_{+-}
(
\mathcal H_t^{prov},
\mathcal B_t^{+,(k)},
q_t
),
\\
\pi_t^{(k)}
&=
\Pi
(
\widetilde{\mathcal B}_t^0,
\mathcal B_t^{+,(k)},
\mathbf w_t^{-,(k)}
),
\\
\mathcal B_t^{+,(k+1)}
&=
\Gamma_F^{refine}
(
\mathcal B_t^-,
\widetilde{\mathcal B}_t^0,
\pi_t^{(k)},
\Xi_t
),
\\
a_t
&\sim
\pi_t^{(K)},
\\
Z_{t+1}
&=
T_Z(
Z_t,
a_t,
\varepsilon_t
),
\\
\mathcal B_{t+1}^-
&=
\mathcal H_-
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+,
a_t,
Z_{t+1},
E_t
),
\\
\mathcal B_{t+1}^0
&=
\Phi_{-0}
(
\mathcal B_{t+1}^-,
\Xi_{t+1}
),
\\
\mathcal B_{t+1}^+
&=
\Gamma_F
(
\mathcal B_{t+1}^-,
\mathcal B_{t+1}^0,
\Xi_{t+1}
).
\end{aligned}
}
$$

其中：

- $\Xi_t$：當前 exogenous information / environment / other-agent input；
- $\mathcal H_t^{prov}$：TCD-06 的 stable historical provenance layer；
- $\mathbf w_t^-$：retrospective relevance layer；
- $K$：bounded deliberation budget；
- $T_Z$：actual environment / system transition；
- $\mathcal H_-$：Historical Sedimentation update；
- $\Gamma_F$：Future Base Space generation operator。

因此：

$$
\boxed{
\text{Deliberative Recursion}
\neq
\text{Physical Time Loop}.
}
$$

同一個 $t$ 內可以反覆：

> 想未來 → 重看過去 → 改估值 → 再想未來。

只有真正 action execution 才讓：

$$
t
\rightarrow
t+1.
$$

本文也正式提出 **Temporal Shift Operator**：

$$
\boxed{
\mathscr S_t
\left(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+;
\Xi_t,
\varepsilon_t
\right)
=
\left(
\mathcal B_{t+1}^-,
\mathcal B_{t+1}^0,
\mathcal B_{t+1}^+
\right).
}
$$

這是 TCD 第一個完整 dynamical-system scaffold。

外部 AI、控制與認知研究提供了六向架構的局部工程對照，但沒有任何單一外部系統等同完整 TCD。MuZero 以 learned future-relevant dynamics 與 tree search 支援 current action selection；DreamerV3 的 world model 預測 potential actions outcomes、critic 評估 imagined outcomes、actor 學習 present policy；Mattar–Daw 的 prioritized-memory theory 則依某 memory 對未來 decision improvement 的 utility 選擇現在應 replay 的 past；Momennejad 等人的 human revaluation experiment 顯示 offline replay of distal past states 與之後 replanning 相關。2025 年的 navigation neuroscience 結果進一步顯示，新資訊可以快速改變 prospective representations of future choices，並伴隨 flexible route switching。這些局部結果共同支持一個保守結論：

$$
\boxed{
\text{past representations, prospective representations, and present choices can participate in recurrent decision loops}.
}
$$

但本文仍不宣稱六向 TCD 已被任何單一 biological or artificial system 實驗完整驗證。

本文最後提出：

$$
\boxed{
\textbf{Intelligence is not only a function from present state to action; for history-bearing prospective agents, it may be more usefully modeled as a bounded recurrent transformation among remembered/structured past, actionable present, and generated future.}
}
$$

中文：

> **智能不只是在現在輸入狀態後輸出 action；對具有歷史與前瞻能力的 agent，它可以被更完整地描述成：過去、現在與生成未來之間的有限反覆轉換，最後再把 action 寫回世界與歷史。**

本文將 TCD-01～07 封裝成第一版：

# **TCD v0.1 Core**

下一個理論接口不再只是增加第七條時間箭頭，而是把：

$$
\boxed{
\mathcal B_t^+
}
$$

中的 prospective branches 從 cognitive objects 升級為：

$$
\boxed{
\text{runnable world instances}.
}
$$

也就是後續：

# **Branching World Computation**
## **分支世界計算／世界域認知 Runtime**

的正式入口。

**關鍵詞：** Tri-Temporal Cognitive Dynamics、Six-Way Coupling、Temporal Shift Operator、Deliberative Recursion、World Models、Replay、Prospective Attraction、Historical Sedimentation、Retrospective Relevance、UCPNP

---

# 1. TCD-07 的任務：從六篇局部理論變成一個系統

TCD-01～03 建立三個 object。

TCD-04～06 建立三組重要 feedback mechanisms。

現在需要問：

> **如果把它們放在同一個 agent 裡，究竟怎麼更新？**

---

# 2. 三個基本時間域

## 2.1 Past

$$
\boxed{
\mathcal B_t^-
}
$$

是：

> historical choice lineage 的 task-relative compressed structure。

---

# 3. Present

$$
\boxed{
\mathcal B_t^0
}
$$

是：

> historically conditioned actionable / reachable domain。

---

# 4. Future

$$
\boxed{
\mathcal B_t^+
}
$$

是：

> agent-generated prospective possibility / choice domain。

---

# 5. Triple State

因此：

$$
\boxed{
\mathfrak T_t^{(3)}
=
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
).
}
$$

---

# 6. 為什麼不是三個普通 state vectors？

因為三者內部型別不同。

---

# 7. Past 可能包含

$$
\boxed{
\mathcal B_t^-
=
(
\mathcal H_t^{prov},
\mathbf w_t^-,
D_t,
L_t,
O_t
).
}
$$

---

# 8. Present 可能包含

$$
\boxed{
\mathcal B_t^0
=
(
Z_t^{est},
\mathcal A_t^{eff},
\widehat{\mathcal R}_{t:H}^{eff},
\mathcal V_t,
U_t^0
).
}
$$

---

# 9. Future 可能包含

$$
\boxed{
\mathcal B_t^+
=
(
\Omega_t^F,
P_t,
\Pi_t,
\mathcal G_t^F,
U_t^+,
E_t^+
).
}
$$

---

# 10. 所以 coupling 必須 Typed

一條：

$$
\mathcal B_t^-
\rightarrow
\mathcal B_t^0
$$

和：

$$
\mathcal B_t^+
\rightarrow
\mathcal B_t^-
$$

根本不是同一種 function。

---

# 11. Typed Coupling Graph

定義：

$$
\boxed{
G_{\mathrm{TCD},t}
=
(
V_t,
E_t,
\tau_E
).
}
$$

---

# 12. Vertex Set

$$
\boxed{
V_t
=
\{
B^-,
B^0,
B^+
\}.
}
$$

---

# 13. Edge-Type Map

$$
\boxed{
\tau_E(e)
\in
\{
Condition,
Generate,
Attract,
Sediment,
Project,
Reweight
\}.
}
$$

---

# 14. Edge I — Past → Present

$$
\boxed{
\Phi_{-0}:
\mathcal B_t^-
\times
\Xi_t
\rightarrow
\mathcal B_t^0.
}
$$

名稱：

# **Historical Conditioning**

---

# 15. 它做什麼？

Past 的：

- capability residue；
- dependency；
- resource history；
- permissions；
- path dependence；
- lost / recovered options；

參與構造現在有效 domain。

---

# 16. 它不是 Memory Retrieval

$$
\boxed{
\Phi_{-0}
\neq
RetrieveMemory.
}
$$

因為很多 history 已經固著在 current structure。

---

# 17. Edge II — Present → Future

$$
\boxed{
\Gamma_{0+}:
\mathcal B_t^0
\rightarrow
\mathcal B_t^+.
}
$$

名稱：

# **Present-Conditioned Future Generation**

---

# 18. 它做什麼？

Present 決定：

- current capabilities；
- current resources；
- current permissions；
- current reachable paths；

因此限制／啟發 agent 生成哪些 futures。

---

# 19. Edge III — Future → Present

$$
\boxed{
\Phi_{+0}:
(
\mathcal B_t^+,
\mathcal B_t^0
)
\rightarrow
\pi_t.
}
$$

名稱：

# **Prospective Attraction**

---

# 20. 它做什麼？

Future representations 經：

- probability；
- value；
- risk；
- option preservation；
- preparation；

改變現在 policy。

---

# 21. 永久邊界

$$
\boxed{
\Phi_{+0}
}
$$

使用的是：

$$
\boxed{
\operatorname{Rep}_t(Future),
}
$$

不是：

$$
\boxed{
FutureEvent_{t+\Delta}.
}
$$

---

# 22. Edge IV — Present → Past

$$
\boxed{
\mathsf{Sed}_{0-}:
(
\mathcal B_t^0,
a_t,
Z_{t+1},
E_t
)
\rightarrow
\Delta\mathcal B_{t+1}^-.
}
$$

名稱：

# **Historical Sedimentation**

---

# 23. 它做什麼？

把：

- actual action；
- alternatives；
- dependencies；
- plasticity；
- resource changes；
- permission changes；
- decision provenance；

寫入下一時刻 Past。

---

# 24. Edge V — Past → Future

$$
\boxed{
\Gamma_{-+}:
\mathcal B_t^-
\rightarrow
\mathcal B_t^+.
}
$$

名稱：

# **Historical Projection**

---

# 25. 它做什麼？

使用：

- analogies；
- prior failures；
- historical trajectories；
- recurring mechanisms；
- latent capabilities；
- dormant options；

生成／約束 future candidates。

---

# 26. Historical Projection 不是簡單 Extrapolation

$$
\boxed{
\Gamma_{-+}
\neq
\text{trend line only}.
}
$$

它可以：

- recombine past；
- invert past failure；
- reopen lost branches；
- abstract mechanism。

---

# 27. Edge VI — Future → Past

$$
\boxed{
\mathcal R_{+-}:
(
\mathcal H_t^{prov},
\mathcal B_t^+,
q_t
)
\rightarrow
\mathbf w_t^-.
}
$$

名稱：

# **Retrospective Relevance**

---

# 28. 它做什麼？

Future target 改變：

- retrieval；
- attention；
- support search；
- counterevidence search；
- historical reactivation。

---

# 29. 它不能改 Past Fact

$$
\boxed{
\mathcal R_{+-}
:
\text{weights change}
}
$$

而不是：

$$
\boxed{
\mathcal H_t^{prov}
:
\text{facts change}.
}
$$

---

# 30. 六條 Edge 的 Mechanism Table

| Edge | Name | Primary Mechanism |
|---|---|---|
| $-\to0$ | Historical Conditioning | state construction |
| $0\to+$ | Present-Conditioned Future Generation | prospective generation |
| $+\to0$ | Prospective Attraction | valuation / policy |
| $0\to-$ | Historical Sedimentation | provenance / structural update |
| $-\to+$ | Historical Projection | analogy / mechanism generation |
| $+\to-$ | Retrospective Relevance | retrieval / relevance reweighting |

---

# 31. 六向不等於六個對稱 Arrow

例如：

$$
\boxed{
\Phi_{-0}
\neq
\mathcal R_{+-}^{-1}.
}
$$

---

# 32. 同樣：

$$
\boxed{
\Gamma_{0+}
\neq
\mathsf{Sed}_{0-}^{-1}.
}
$$

---

# 33. 過去、現在、未來也不是 Information-Conserving Transform

一般：

$$
\boxed{
\mathscr S
}
$$

可以：

- lose information；
- add exogenous information；
- generate candidates；
- compress history。

---

# 34. TCD 因此不是 Reversible Time Physics

它是：

$$
\boxed{
\text{agent-level cognitive dynamics}.
}
$$

---

# 35. Circularity Problem

如果直接寫：

$$
B^0
\rightarrow
B^+
\rightarrow
B^0,
$$

會問：

> 哪個先算？

---

# 36. 第二個 Circularity

$$
B^-
\rightarrow
B^+
\rightarrow
B^-.
$$

也會問：

> 是 history 先生成 future，還是 future 先重看 history？

---

# 37. 解法：分離兩種時間 Index

本文定義：

$$
\boxed{
t
=
\text{historical / environment time}
}
$$

與：

$$
\boxed{
k
=
\text{deliberation iteration}.
}
$$

---

# 38. $t$ 的意義

當 agent 真正：

- act；
- environment transition；
- resource change；
- external event；

才進入下一個：

$$
t+1.
$$

---

# 39. $k$ 的意義

同一 decision moment 中：

> 想一下。

可以：

$$
k\rightarrow k+1.
$$

---

# 40. Deliberation Does Not Advance Historical Time

$$
\boxed{
k\rightarrow k+1
\not\Rightarrow
t\rightarrow t+1.
}
$$

---

# 41. Initial Present Construction

先從 past + exogenous current information：

$$
\boxed{
\widetilde{\mathcal B}_t^0
=
\Phi_{-0}
(
\mathcal B_t^-,
\Xi_t
).
}
$$

---

# 42. Initial Future Generation

$$
\boxed{
\mathcal B_t^{+,(0)}
=
\Gamma_F
(
\mathcal B_t^-,
\widetilde{\mathcal B}_t^0,
\Xi_t
).
}
$$

---

# 43. $\Gamma_F$ 同時接受 Past 與 Present

因此概念上：

$$
\boxed{
\Gamma_F
=
\operatorname{Couple}
(
\Gamma_{-+},
\Gamma_{0+}
).
}
$$

這不是線性加法。

---

# 44. Retrospective Reweighting

第 $k$ 輪：

$$
\boxed{
\mathbf w_t^{-,(k)}
=
\mathcal R_{+-}
(
\mathcal H_t^{prov},
\mathcal B_t^{+,(k)},
q_t
).
}
$$

---

# 45. Active Past

$$
\boxed{
\mathcal B_t^{-,act,(k)}
=
View(
\mathcal H_t^{prov},
\mathbf w_t^{-,(k)}
).
}
$$

---

# 46. Policy Update

$$
\boxed{
\pi_t^{(k)}
=
\Pi
(
\widetilde{\mathcal B}_t^0,
\mathcal B_t^{+,(k)},
\mathcal B_t^{-,act,(k)}
).
}
$$

---

# 47. Future Refinement

policy candidate 本身可以改變：

> 如果我這樣行動，future 會怎樣？

因此：

$$
\boxed{
\mathcal B_t^{+,(k+1)}
=
\Gamma_F^{refine}
(
\mathcal B_t^-,
\widetilde{\mathcal B}_t^0,
\pi_t^{(k)},
\Xi_t
).
}
$$

---

# 48. 這形成 Deliberation Loop

$$
\boxed{
Future^{(k)}
\rightarrow
PastView^{(k)}
\rightarrow
Policy^{(k)}
\rightarrow
Future^{(k+1)}.
}
$$

---

# 49. Deliberation Loop 可以很短

例如：

$$
K=1.
$$

就是一次：

> 預測 → 選 action。

---

# 50. 也可以多輪

$$
K>1.
$$

例如：

> 提方案 → 找歷史反例 → 改方案 → 再模擬。

---

# 51. $K$ 必須 Bounded

真實 agent：

$$
\boxed{
K<\infty
}
$$

受：

- latency；
- compute；
- energy；
- deadline；

限制。

---

# 52. 不要求 Fixed-Point Convergence

$$
\boxed{
\pi^{(k+1)}
\rightarrow
\pi^\star
}
$$

不保證。

---

# 53. Deliberation 可 Oscillate

例如：

$$
f_1
\rightarrow
h_1
\rightarrow
f_2
\rightarrow
h_2
\rightarrow
f_1.
$$

---

# 54. Oscillation 不是自動 Bug

若 evidence 真 ambiguous，

policy indecision 可能合理。

---

# 55. 但需要 Stopping Contract

例如：

$$
\boxed{
Stop
=
BudgetExhausted
\lor
PolicyStable
\lor
RiskThreshold
\lor
Deadline.
}
$$

---

# 56. Policy Stability

$$
\boxed{
d_\pi(
\pi^{(k+1)},
\pi^{(k)}
)
<
\epsilon_\pi.
}
$$

---

# 57. Future-Space Stability

$$
\boxed{
d_F(
\mathcal B^{+,(k+1)},
\mathcal B^{+,(k)}
)
<
\epsilon_F.
}
$$

---

# 58. Historical-View Stability

$$
\boxed{
d_H(
\mathbf w^{-,(k+1)},
\mathbf w^{-,(k)}
)
<
\epsilon_H.
}
$$

---

# 59. Bounded Cognitive Closure

可定義：

$$
\boxed{
\mathfrak C_t^{(K)}
=
\operatorname{Delib}^{K}
(
\mathfrak T_t^{(3)}
).
}
$$

---

# 60. Cognitive Closure 不是 Logical Completeness

它只表示：

> 在 bounded deliberation budget 下完成的一輪 internal refinement。

---

# 61. Action Commitment

deliberation 結束：

$$
\boxed{
a_t
\sim
\pi_t^{(K)}.
}
$$

---

# 62. Environment Transition

$$
\boxed{
Z_{t+1}
=
T_Z(
Z_t,
a_t,
\varepsilon_t
).
}
$$

---

# 63. $\varepsilon_t$ 包含

- noise；
- exogenous event；
- other-agent action；
- model mismatch；
- stochasticity。

---

# 64. Actual Outcome May Differ from Predicted Future

$$
\boxed{
Z_{t+1}^{real}
\neq
\widehat Z_{t+1}.
}
$$

---

# 65. Prediction Error Becomes New Information

定義：

$$
\boxed{
\delta_t
=
d(
Z_{t+1}^{real},
\widehat Z_{t+1}
).
}
$$

---

# 66. Sedimentation

TCD-05：

$$
\boxed{
\mathcal B_{t+1}^-
=
\mathcal H_-
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+,
a_t,
Z_{t+1},
E_t
).
}
$$

---

# 67. New Past Includes

- what happened；
- what was chosen；
- what was unchosen；
- which future influenced decision；
- which dependencies changed；
- which prediction failed。

---

# 68. New Present

新 observation：

$$
\Xi_{t+1}
$$

到來後：

$$
\boxed{
\mathcal B_{t+1}^0
=
\Phi_{-0}
(
\mathcal B_{t+1}^-,
\Xi_{t+1}
).
}
$$

---

# 69. New Future

$$
\boxed{
\mathcal B_{t+1}^+
=
\Gamma_F
(
\mathcal B_{t+1}^-,
\mathcal B_{t+1}^0,
\Xi_{t+1}
).
}
$$

---

# 70. Full Shift

因此：

$$
\boxed{
\mathscr S_t
:
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
)
\rightarrow
(
\mathcal B_{t+1}^-,
\mathcal B_{t+1}^0,
\mathcal B_{t+1}^+
).
}
$$

---

# 71. Extended Shift

更完整：

$$
\boxed{
\mathscr S_t
=
\mathscr S
(
\mathfrak T_t^{(3)},
\Xi_t,
\varepsilon_t,
\mathbf B_t,
\kappa_t
).
}
$$

---

# 72. TCD Master Update

本文將第一版 master update 壓縮為：

$$
\boxed{
\begin{aligned}
\widetilde B_t^0
&=
\Phi_{-0}(B_t^-,\Xi_t),\\
B_t^{+,(0)}
&=
\Gamma_F(B_t^-,\widetilde B_t^0,\Xi_t),\\
(w_t^{-,(k)},\pi_t^{(k)},B_t^{+,(k+1)})
&=
\mathfrak D(
B_t^-,
\widetilde B_t^0,
B_t^{+,(k)}
),\\
a_t
&\sim
\pi_t^{(K)},\\
Z_{t+1}
&=
T_Z(Z_t,a_t,\varepsilon_t),\\
B_{t+1}^-
&=
\mathcal H_-(B_t^-,B_t^0,B_t^+,a_t,Z_{t+1}),\\
B_{t+1}^0
&=
\Phi_{-0}(B_{t+1}^-,\Xi_{t+1}),\\
B_{t+1}^+
&=
\Gamma_F(B_{t+1}^-,B_{t+1}^0,\Xi_{t+1}).
\end{aligned}
}
$$

---

# 73. $\mathfrak D$ 是 Deliberative Coupling Block

它包含：

$$
\boxed{
\mathcal R_{+-}
+
\Phi_{+0}
+
\Gamma_F^{refine}.
}
$$

仍然不是普通 algebraic sum。

---

# 74. Why Deliberative Block Matters

因為 agent 在 action 前可以：

- 生成 future；
- 用 future 找 past；
- 用 past 修正 future；
- 用 future 重新排序 action。

---

# 75. 這就是 Reflexive Cognition

不是：

$$
\boxed{
\text{one-pass inference}.
}
$$

而是：

$$
\boxed{
\text{bounded recurrent inference}.
}
$$

---

# 76. TCD 與普通 Markov Policy 的差別

普通形式：

$$
\boxed{
a_t
\sim
\pi(a\mid s_t).
}
$$

---

# 77. TCD 形式

更像：

$$
\boxed{
a_t
\sim
\pi
\left(
a
\mid
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
\right).
}
$$

---

# 78. 但如果 $s_t$ 已充分包含三者呢？

那：

$$
\boxed{
s_t
=
Compress(
B^-,
B^0,
B^+
)
}
$$

完全可以。

---

# 79. TCD 不反對 Markovization

如果能找到 sufficient augmented state：

$$
S_t^\star,
$$

TCD 可被壓縮進：

$$
S_t^\star.
$$

---

# 80. TCD 真正關心的是：壓縮前你有沒有漏掉功能

所以：

$$
\boxed{
\text{TCD}
\neq
\text{anti-Markov}.
}
$$

---

# 81. Temporal Sufficiency

定義：

$$
\boxed{
S_t^\star
=
\Psi_{TCD}
(
B_t^-,
B_t^0,
B_t^+
).
}
$$

---

# 82. 若 $S_t^\star$ 足夠

使：

$$
P(
Y_{t:H}
\mid
B^-,
B^0,
B^+
)
\approx
P(
Y_{t:H}
\mid
S_t^\star
),
$$

則可使用 compressed state。

---

# 83. 這延續 HSV

不是所有 history 都要永久展開。

---

# 84. Coupling Strength

如何量一條 edge 的重要性？

用 ablation。

---

# 85. Edge-Ablation

對 edge：

$$
e_{ij},
$$

建立：

$$
\boxed{
G_{\mathrm{TCD}}^{-e_{ij}}.
}
$$

---

# 86. Coupling Sensitivity

對 task loss：

$$
\mathcal L_T,
$$

定義：

$$
\boxed{
\chi_{ij}^{(T)}
=
\mathcal L_T(
G^{-e_{ij}}
)
-
\mathcal L_T(
G
).
}
$$

---

# 87. $\chi>0$

表示移除 coupling 使 performance 變差。

---

# 88. $\chi\approx0$

表示在該 task：

> 這條 edge 可能不重要。

---

# 89. $\chi<0$

表示移除 edge 反而更好。

這非常重要。

---

# 90. More Coupling Is Not Always Better

$$
\boxed{
\text{more temporal coupling}
\not\Rightarrow
\text{better cognition}.
}
$$

---

# 91. Example：Bad Future Representation

如果：

$$
B_t^+
$$

充滿 phantom futures，

強：

$$
+\to0
$$

可能傷害 policy。

---

# 92. Example：Bad Retrospective Relevance

若：

$$
+\to-
$$

只找支持 future 的 history，

形成 narrative capture。

---

# 93. Example：Excess Sedimentation

若：

$$
0\to-
$$

保存太多 old constraints，

plasticity 崩潰。

---

# 94. TCD 因此需要 Coupling Governance

每條 edge 都要有：

- budget；
- uncertainty；
- evidence；
- stopping；
- audit。

---

# 95. Coupling Profile

對 agent：

$$
\boxed{
\Pi_{\mathrm{TCD}}^A
=
(
Q_{-0},
Q_{0+},
Q_{+0},
Q_{0-},
Q_{-+},
Q_{+-}
).
}
$$

---

# 96. 不是 Scalar

不要：

$$
\boxed{
TCDIQ=95.
}
$$

---

# 97. Agent A 可能 History 強

$$
Q_{-0}\gg0,
$$

但：

$$
Q_{0+}
$$

弱。

---

# 98. Agent B 可能 Future Generation 強

但 Sedimentation 差，

反覆重犯。

---

# 99. Agent C 可能 Prospective Attraction 太強

容易被 phantom future 操縱。

---

# 100. Agent D 可能 Retrospective Relevance 太弱

無法從新目標重新啟用 old knowledge。

---

# 101. Six-Edge Bottleneck

定義：

$$
\boxed{
e^\star
=
\arg\max_e
\chi_e^{(T)}.
}
$$

表示在該 task 移除後造成最大性能損失的 temporal coupling。

---

# 102. Coupling Bottleneck Can Migrate

隨 agent 改進：

$$
\boxed{
e_t^\star
\neq
e_{t+1}^\star.
}
$$

---

# 103. Positive Feedback Loop I — Narrative Capture

$$
\boxed{
f
\rightarrow
supportive\ past
\rightarrow
P(f)\uparrow
\rightarrow
more\ support\ search.
}
$$

---

# 104. 這可能形成 Self-Reinforcing Belief

不是因為 evidence 真變強，

而是 retrieval bias。

---

# 105. Negative Feedback Loop I — Adversarial Correction

$$
\boxed{
f
\rightarrow
counterhistory
\rightarrow
P(f)\downarrow
\rightarrow
future\ revision.
}
$$

---

# 106. 這是 Desired Stabilization

TCD 不只研究正 feedback。

---

# 107. Positive Feedback Loop II — Constructive Realization

$$
\boxed{
f
\rightarrow
action
\rightarrow
infrastructure
\rightarrow
P(f)\uparrow.
}
$$

---

# 108. Negative Feedback Loop II — Prevention

$$
\boxed{
f_{bad}
\rightarrow
mitigation
\rightarrow
P(f_{bad})\downarrow.
}
$$

---

# 109. Feedback Sign Depends on Mechanism

所以：

$$
\boxed{
Cycle
\neq
SelfReinforcement.
}
$$

---

# 110. Loop Gain

概念上可定義：

$$
\boxed{
G_{loop}
=
\prod_{e\in cycle}
g_e.
}
$$

但只在 edge gains 有可比尺度時使用。

---

# 111. 一般 TCD 不假設 Linear Stability Theory 直接適用

如果 operator nonlinear / typed，

應使用：

- simulation；
- ablation；
- local linearization；
- empirical dynamics。

---

# 112. Temporal Coherence

一個 mature agent 的三個 base spaces 不應互相完全矛盾。

---

# 113. Example

Present says：

$$
\text{resource}=0,
$$

Future says：

> tomorrow deploy giant system。

若沒有 path：

$$
\boxed{
\text{future-present incoherence}.
}
$$

---

# 114. Past-Future Coherence

Future claim 若依賴已被 Past falsified 的 dependency，

也有：

$$
\boxed{
\text{historical-future incoherence}.
}
$$

---

# 115. Coherence Checks

可定義：

$$
\boxed{
C_{-0},
C_{0+},
C_{-+}.
}
$$

---

# 116. Coherence 不等於 Conformism

new future 可以挑戰 past trend。

只要：

> 有 explicit mechanism。

---

# 117. Surprise Is Allowed

TCD Future 仍保留：

$$
U_t^+.
$$

---

# 118. Unknown Mass Prevents Temporal Overclosure

如果：

$$
p_\bot=0
$$

被濫用，

agent 容易：

> 把目前三生模型當宇宙全部可能性。

---

# 119. TCD Unknown Triple

可寫：

$$
\boxed{
\mathbf U_t
=
(
U_t^-,
U_t^0,
U_t^+
).
}
$$

---

# 120. Past Unknown

無法完整重建 historical alternatives。

---

# 121. Present Unknown

不知道 hidden capability / path / dependency。

---

# 122. Future Unknown

不知道未命名 future regions。

---

# 123. Temporal Epistemic Humility

所以：

$$
\boxed{
\widehat{\mathfrak T}_t^{(3)}
\neq
\mathfrak T_t^{(3),true}
}
$$

一般應保留。

---

# 124. Observation of TCD Is Observer-Relative

不同 observer：

$$
A,B
$$

可能建出：

$$
\widehat{\mathfrak T}_t^{(3),A}
\neq
\widehat{\mathfrak T}_t^{(3),B}.
$$

---

# 125. Observer Difference 不是 Arbitrary Subjectivism

仍受：

- evidence；
- provenance；
- dynamics；
- experiment；
- resolution；

約束。

---

# 126. Multi-Agent TCD

對 agents：

$$
A_1,\ldots,A_n,
$$

每個有：

$$
\mathfrak T_t^{(3),i}.
$$

---

# 127. Shared Present

它們可能共享：

$$
Env_t,
$$

但：

$$
B_t^{+,i}
$$

不同。

---

# 128. Shared Future Candidate Can Couple Agents

若：

$$
f
$$

被多人採用，

可：

$$
\boxed{
f
\rightarrow
a_t^1,\ldots,a_t^n.
}
$$

---

# 129. Collective Prospective Attraction

未來 narrative 可以形成 collective coordination。

---

# 130. 也可能形成 Collective Phantom Future

錯誤 future narrative 也能同時改變大量 agents。

---

# 131. Collective Sedimentation

multi-agent actions 產生：

- standards；
- institutions；
- markets；
- infrastructure。

---

# 132. 這為 Branching World / Institution TCD 留接口

本文不展開。

---

# 133. MuZero 的外部對照

MuZero 建立 planning-relevant learned dynamics，

用 tree search 評估 action sequences，

再選 current action。 

外部意義：

$$
\boxed{
\text{future model}
\rightarrow
\text{present action}.
}
$$

---

# 134. DreamerV3 的外部對照

DreamerV3 的 world model：

> 預測 potential action outcomes；

critic：

> 評估 imagined outcomes；

actor：

> 學習導向高 value outcome 的 action。

這是非常清楚的：

$$
\boxed{
FutureRepresentation
\rightarrow
Valuation
\rightarrow
Policy.
}
$$

---

# 135. Mattar–Daw 的外部對照

其 prioritized memory access theory：

> 依 memory 對 future decision improvement 的 utility 決定 replay priority。

對照：

$$
\boxed{
FutureNeed
\rightarrow
PastAccess.
}
$$

---

# 136. Momennejad 等人的外部對照

reward revaluation 後：

> distal past states 的 offline replay 與後續 replanning 相關。

對照：

$$
\boxed{
NewInformation
\rightarrow
PastReplay
\rightarrow
NewPolicy.
}
$$

---

# 137. 2025 Prospective Navigation Codes 的外部對照

一項大鼠 flexible navigation 研究顯示：

> 新 reward-location information 到來後，hippocampal/prefrontal prospective representations of future choices 可以快速調整，並伴隨 route switching。

---

# 138. TCD 的最保守讀法

這只支持：

$$
\boxed{
\text{past integration}
+
\text{prospective representation}
+
\text{current choice update}
}
$$

在至少某些 biological decision tasks 中具有經驗相鄰性。

---

# 139. 不宣稱 Rat Brain = TCD Runtime

$$
\boxed{
\text{biological analogue}
\neq
\text{theory identity}.
}
$$

---

# 140. Six-Edge Ablation Benchmark

建立 finite environment。

---

# 141. Full Agent

有六條 coupling。

---

# 142. Ablation 1

移除：

$$
-\to0.
$$

---

# 143. Ablation 2

移除：

$$
0\to+.
$$

---

# 144. Ablation 3

移除：

$$
+\to0.
$$

---

# 145. Ablation 4

移除：

$$
0\to-.
$$

---

# 146. Ablation 5

移除：

$$
-\to+.
$$

---

# 147. Ablation 6

移除：

$$
+\to-.
$$

---

# 148. Measure

比較：

- cumulative task return；
- safe reachability；
- future coverage；
- adaptation；
- repeated-error rate；
- option preservation；
- provenance fidelity；
- compute cost。

---

# 149. Exact Finite Micro-Model

可用 dynamic graph：

$$
G_t=(V_t,E_t).
$$

---

# 150. Past Choice Alters Graph

action：

$$
a_t
$$

可以：

- add edge；
- remove edge；
- increase edge cost。

---

# 151. Present Domain

agent 只能看到：

$$
V_t^{vis}
$$

與：

$$
E_t^{vis}.
$$

---

# 152. Future Generator

生成 candidate goals：

$$
f_1,\ldots,f_n.
$$

---

# 153. Prospective Attraction

future value 改 path selection。

---

# 154. Sedimentation

action 改 graph + log。

---

# 155. Retrospective Relevance

future goal 改 past transition retrieval。

---

# 156. 這可以完整執行六條 Edge

而且：

$$
\boxed{
\text{finite}
}
$$

可 exact audit。

---

# 157. TCD Runtime Trace

每輪至少輸出：

```text
t
past_base_version
present_base_version
future_base_version
deliberation_rounds
active_past_items
future_candidates
future_unknown_mass
policy_before_future
policy_after_future
chosen_action
predicted_outcomes
real_outcome
prediction_error
sedimentation_record
dependencies_changed
options_lost
options_opened
next_state_versions
```

---

# 158. Replayability

理想：

$$
\boxed{
Trace_{0:t}
\rightarrow
\widehat{\mathfrak T}_t^{(3)}.
}
$$

---

# 159. Replay 不必 Deterministic

若 system stochastic，

保存：

- seeds；
- distributions；
- model versions。

---

# 160. Temporal Provenance

每一個：

$$
B^-,
B^0,B^+
$$

都應有：

- timestamp；
- version；
- parent；
- evidence；
- operator；
- cost。

---

# 161. Six-Way Coupling Evidence Passport

對每條 edge claim：

```text
edge
agent
task
domain
source_state
target_state
operator
budget
ablation
effect_size
uncertainty
evidence_level
failure_conditions
```

---

# 162. Edge Claim 不能越界

例如：

> DreamerV3 有 $+\to0$ engineering analogue。

不能推出：

> DreamerV3 已具完整 TCD。

---

# 163. Temporal Shift Operator

本文正式命名：

# **TCD Shift Operator**

$$
\boxed{
\mathscr S_t.
}
$$

---

# 164. Minimal Definition

$$
\boxed{
\mathscr S_t
:
\mathfrak T_t^{(3)}
\times
\Xi_t
\times
\mathcal E_t
\rightarrow
\mathfrak T_{t+1}^{(3)}.
}
$$

---

# 165. $\mathcal E_t$ 表示

- actual action；
- environment event；
- observed consequence；
- new evidence。

---

# 166. Shift Operator 不是 Closed Autonomous Law

真實 agent 會接收：

$$
\boxed{
\Xi_t.
}
$$

---

# 167. 所以 TCD 是 Open Dynamical System

$$
\boxed{
\text{TCD agent}
+
\text{environment}
+
\text{other agents}.
}
$$

---

# 168. No Closed-World Assumption

future unknown：

$$
U_t^+
$$

永遠可能非零。

---

# 169. Temporal Fixed Point

若：

$$
\mathfrak T_{t+1}^{(3)}
\approx
\mathfrak T_t^{(3)},
$$

可稱：

$$
\boxed{
\text{local temporal cognitive fixed regime}.
}
$$

---

# 170. 不一定是好事

可能是：

- stable expertise；
- rigid institution；
- stuck loop；
- mature policy。

---

# 171. Temporal Cycle

若：

$$
\mathfrak T_{t+k}^{(3)}
\approx
\mathfrak T_t^{(3)},
$$

可研究 periodic cognitive regime。

---

# 172. Temporal Drift

若 state 持續移動但無突然轉變：

$$
\boxed{
\text{drift}.
}
$$

---

# 173. Temporal Phase Shift

若：

- future ontology；
- capability；
- reachable domain；
- historical relevance；

突然重構，

可標：

$$
\boxed{
\text{temporal cognitive phase shift}.
}
$$

---

# 174. 本文不正式建立 Phase Theory

只留接口。

---

# 175. Learning Is Temporal-State Change

如果：

$$
Cap_{t+1}\neq Cap_t,
$$

這是：

$$
\boxed{
\mathfrak T_{t+1}^{(3)}
\neq
\mathfrak T_t^{(3)}.
}
$$

---

# 176. Forgetting Is Temporal-State Change

如果：

$$
B_{t+1}^-
$$

壓縮／失活某些 residue，

也會改：

$$
B_{t+1}^0,
B_{t+1}^+.
$$

---

# 177. Prediction Error Can Trigger Temporal Reorganization

若：

$$
\delta_t\gg0,
$$

agent 可能：

- reweight past；
- revise world model；
- expand unknown mass；
- generate new future ontology。

---

# 178. Error-Driven TCD Update

概念：

$$
\boxed{
\delta_t
\rightarrow
(
\Delta B^-,
\Delta B^0,
\Delta B^+
).
}
$$

---

# 179. Surprise Does Not Automatically Mean Learning

若 agent 不 sediment / update：

$$
\delta_t
$$

可能被忽略。

---

# 180. Long-Term Intelligence Requires Temporal Credit Assignment

某 action：

$$
a_t
$$

結果：

$$
t+100
$$

才顯現。

---

# 181. Credit Assignment Across TCD

需要追：

$$
\boxed{
R_t^+
\rightarrow
a_t
\rightarrow
Sediment
\rightarrow
FutureOutcome.
}
$$

---

# 182. 這是 PCI 長期 Resolution 的 runtime 版本

PCI 保存：

- prediction；
- realization path；
- future resolution。

TCD 現在保存它們之間的 temporal lineage。

---

# 183. TCD 與 UCPNP 的關係

UCPNP 問：

> 哪些 intervention 能改變 agent-relative tractability frontier？

---

# 184. TCD 回答其中一個動力來源

同一 intervention：

- 新 knowledge；
- new tool；
- new future；
- reactivated past；

會經 TCD couplings 改變：

$$
\boxed{
\mathcal B^0
}
$$

與：

$$
\boxed{
\mathcal B^+.
}
$$

---

# 185. UCPNP 是 Frontier Program

TCD 是：

$$
\boxed{
\text{one temporal dynamics layer beneath frontier motion}.
}
$$

---

# 186. TCD 不能取代 UCPNP

它不直接定義：

- verification；
- certification；
- completion cost；
- complexity regime。

---

# 187. 兩者接口

$$
\boxed{
\mathfrak U_t
\supset
\mathfrak T_t^{(3)}
}
$$

可作未來整合方向。

---

# 188. TCD v0.1 Core

本文建議將：

# **TCD-01～TCD-07**

視為：

$$
\boxed{
\text{TCD v0.1 Core}.
}
$$

---

# 189. v0.1 包含

1. Past Base Space；
2. Present Base Space；
3. Future Base Space；
4. Prospective Attraction；
5. Historical Sedimentation；
6. Retrospective Relevance；
7. Six-Way Coupling + Shift Operator。

---

# 190. v0.1 不包含

- runnable world branching；
- world-domain governance；
- cross-world evidence；
- multi-world allocation；
- persistent subworld agents；
- full normative deployment layer。

---

# 191. 為什麼下一步應該分新系列？

因為：

$$
\boxed{
\mathcal B_t^+
}
$$

目前仍是：

> cognitive / modelled future domain。

---

# 192. 下一階

若把 candidate：

$$
f_i
$$

instantiate：

$$
\boxed{
f_i
\rightarrow
W_i,
}
$$

世界：

$$
W_i
$$

開始：

- run；
- accumulate history；
- contain agents；
- receive interventions；

就不是單純 TCD representation。

---

# 193. 這是 Runnable Future

$$
\boxed{
\text{Represented Future}
\rightarrow
\text{Executable Future World}.
}
$$

---

# 194. 新問題

不再只是：

> 哪些 futures 值得想？

而是：

$$
\boxed{
\text{哪些 futures 值得實際投入計算？}
}
$$

---

# 195. 這就是下一系列

# **Branching World Computation**
## **分支世界計算／世界域認知 Runtime**

---

# 196. 可否證條件

## F196.1 Edge-Indistinguishability

若六條 coupling 在 controlled ablation 中無法操作性區分，

taxonomy 應簡化。

## F196.2 Deliberation No-Gain

若 $K>1$ 的 reflective loop 長期不比 $K=1$ 好，

bounded recursion 不應被神化。

## F196.3 Circularity Failure

若 implementation 無法區分 deliberation index $k$ 與 historical time $t$，

runtime formalization 需要重構。

## F196.4 Past-Fact Contamination

若 $+\to-$ 會 silently rewrite provenance，

統一系統失效。

## F196.5 Phantom-Future Instability

若錯誤 future representation 經 $+\to0$ 造成大規模 harmful lock-in，

需要降低 coupling gain / 增加 adversarial gate。

## F196.6 Over-Sedimentation

若 $0\to-$ 造成 memory rigidity / plasticity collapse，

需增加 forgetting / archive。

## F196.7 Historical Confirmation Loop

若 $+\to-\to+$ 只強化同一 narrative，

需強制 counter-retrieval。

## F196.8 External-Shock Failure

若 TCD 忽略 $\Xi_t,\varepsilon_t$ 後只能解釋封閉世界，

必須保留 open-system formulation。

## F196.9 No Predictive Gain

若完整 TCD state 對 planning / adaptation / audit 完全不優於更簡單 sufficient state，

應使用簡單模型。

---

# 197. 結論

TCD-01 說：

$$
\boxed{
Past\neq Memory.
}
$$

TCD-02 說：

$$
\boxed{
Present\neq Point.
}
$$

TCD-03 說：

$$
\boxed{
Future\neq PreGivenMap.
}
$$

TCD-04 說：

$$
\boxed{
FutureRepresentation
\rightarrow
PresentPolicy.
}
$$

TCD-05 說：

$$
\boxed{
PresentAction
\rightarrow
PastSediment.
}
$$

TCD-06 說：

$$
\boxed{
FutureTarget
\rightarrow
PastRelevance.
}
$$

TCD-07 現在把它們全部放進同一個系統。

真正的核心不再是：

$$
\boxed{
Past,
Present,
Future.
}
$$

而是：

$$
\boxed{
Past
\leftrightarrows
Present
\leftrightarrows
Future
\leftrightarrows
Past
}
$$

但每一條箭頭都有不同 operator semantics。

在 agent 的同一 decision moment：

$$
t
$$

內，

可以有：

$$
\boxed{
Future^{(k)}
\rightarrow
PastView^{(k)}
\rightarrow
Policy^{(k)}
\rightarrow
Future^{(k+1)}.
}
$$

這不是時間旅行。

它只是：

$$
\boxed{
\text{bounded deliberation}.
}
$$

當 agent 真正執行：

$$
a_t,
$$

世界才：

$$
\boxed{
t\rightarrow t+1.
}
$$

於是：

$$
\boxed{
PresentAction_t
\rightarrow
Past_{t+1}.
}
$$

新的 Past 又重新構造：

$$
Present_{t+1},
$$

新的 Present 再與新的 Past 一起生成：

$$
Future_{t+1}.
$$

所以第一版完整 TCD 可以壓縮成一句話：

> **智能不只是在現在解題；它利用沉積的過去生成可行的現在與想像的未來，再讓被生成的未來重新組織現在的行動與過去的相關性，而行動又被沉積成下一輪歷史。**

形式上：

$$
\boxed{
\mathscr S_t:
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
)
\longrightarrow
(
\mathcal B_{t+1}^-,
\mathcal B_{t+1}^0,
\mathcal B_{t+1}^+
).
}
$$

這就是：

# **Tri-Temporal Cognitive Dynamics v0.1 Core**

第一次完整閉合。

下一步不再需要多畫一條時間箭頭。

真正的新問題是：

> **如果 Future Base Space 中的候選不只被想像，而可以被 instantiate 成可持續執行、具有自身 agent、history、rules 與 interventions 的子世界，智能體要如何管理大量並行世界？**

那已經是另一個研究層：

# **Branching World Computation**

---

# Claim Typing

| Claim | Type | Status |
|---|---|---|
| TCD 可表示為三個 typed temporal base spaces | D | Canonical synthesis |
| 六個 coupling 方向具有不同 operator semantics | D | Canonical boundary |
| deliberation index $k$ 應與 historical time $t$ 分離 | D / methodology | Core anti-circularity formalization |
| TCD Shift Operator 可作完整一步更新 scaffold | D | Proposed unified dynamics |
| coupling importance 可用 edge ablation 衡量 | D / experiment design | Proposed operationalization |
| MuZero / Dreamer 提供 future-model-to-present-action engineering analogues | E | External calibration |
| prioritized / offline replay 提供 future-need-to-past-access analogues | E | External calibration |
| prospective navigation codes adapt with new information | E | External neuroscience evidence |
| 完整六向 TCD 已被單一實驗系統證明 | — | Not claimed |
| Future $\to$ Past 是物理逆因果 | — | Explicitly rejected |
| 更多 coupling 一定更智能 | — | Explicitly rejected |

---

# Evidence Ladder

本文目前主要位於：

- **L0**：typed six-way coupling + shift operator；
- **L1–L2**：finite six-edge ablation / deliberation benchmarks 可實作；
- **L3**：world-model planning、replay、revaluation、prospective-navigation studies 提供局部機制外部對照；
- **L4**：需要 persistent AI / robot / institution runtime 做 longitudinal six-edge ablation；
- **L5+**：跨 domain replication、multi-agent TCD、runnable-world extension 尚待後續。

---

# 參考文獻

## Neo.K 內部正典與譜系

1. Neo.K. *歷史作為狀態變量：路徑依賴、記憶增廣與複雜系統的動力身份*. 2026.
2. Neo.K with Aletheia. *Past Is Not Memory*. TCD-01, 2026.
3. Neo.K with Aletheia. *The Present Is Not a Point*. TCD-02, 2026.
4. Neo.K with Aletheia. *Future as a Generated Base Space*. TCD-03, 2026.
5. Neo.K with Aletheia. *Prospective Attraction*. TCD-04, 2026.
6. Neo.K with Aletheia. *Historical Sedimentation*. TCD-05, 2026.
7. Neo.K with Aletheia. *Retrospective Relevance*. TCD-06, 2026.
8. Neo.K with Aletheia. *Neo.K Ultimate Cognitive P/NP Unified Theory*. UCPNP Paper 09, 2026.
9. Neo.K with Aletheia. *Generative Forecasting*. UCPNP Series II Paper 13, 2026.
10. Neo.K with Aletheia. *Prospective Constructive Intelligence*. UCPNP Series II Paper 14, 2026.

## External technical calibration

11. Schrittwieser, J., Antonoglou, I., Hubert, T., et al. *Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model*. Nature 588, 604–609, 2020.
12. Hafner, D., Pasukonis, J., Ba, J., & Lillicrap, T. *Mastering Diverse Control Tasks through World Models*. Nature 640, 647–653, 2025.
13. Mattar, M. G., & Daw, N. D. *Prioritized Memory Access Explains Planning and Hippocampal Replay*. Nature Neuroscience 21, 1609–1617, 2018.
14. Momennejad, I., Otto, A. R., Daw, N. D., & Norman, K. A. *Offline Replay Supports Planning in Human Reinforcement Learning*. eLife 7:e32548, 2018.
15. Prince, S. M., Cushing, S. D., Yassine, T. A., et al. *New Information Triggers Prospective Codes to Adapt for Flexible Navigation*. Nature Communications 16, 4822, 2025.
16. Schaul, T., Quan, J., Antonoglou, I., & Silver, D. *Prioritized Experience Replay*. arXiv:1511.05952, 2015.
17. Andrychowicz, M., Wolski, F., Ray, A., et al. *Hindsight Experience Replay*. Advances in Neural Information Processing Systems 30, 2017.

---

## Public Version Disclaimer

本文是 agent-level cognitive / decision / temporal dynamics framework。

本文不聲稱：

- 六向 coupling 是標準認知科學定律；
- Past、Present、Future 是三個物理本體層；
- Future physically causes Past；
- recurrent deliberation 是時間旅行；
- 六條 edge 必須存在於所有 agent；
- coupling strength 可以跨 domain 直接比較；
- world models、replay 或 hippocampal prospective coding 等同完整 TCD；
- TCD 必然提高 performance；
- TCD v0.1 已經完成 runnable-world / multi-world architecture；
- 本文對 classical $P$ vs. $NP$ 提供任何新證明。

本文真正建立的是：

$$
\boxed{
\mathfrak T_t^{(3)}
=
(
\mathcal B_t^-,
\mathcal B_t^0,
\mathcal B_t^+
)
}
$$

與：

$$
\boxed{
\mathscr S_t:
\mathfrak T_t^{(3)}
\rightarrow
\mathfrak T_{t+1}^{(3)}.
}
$$

並明確要求：

$$
\boxed{
\text{six temporal couplings are typed, bounded, auditable, and empirically ablatable}.
}
$$
