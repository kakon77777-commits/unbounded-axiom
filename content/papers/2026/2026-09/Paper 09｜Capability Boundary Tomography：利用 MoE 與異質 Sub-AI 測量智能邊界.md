# Paper 09｜Capability Boundary Tomography：利用 MoE 與異質 Sub-AI 測量智能邊界

**English Title:** *Capability Boundary Tomography: Measuring Intelligence Boundaries through MoE, Heterogeneous Models, and Comparative Delegation*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／能力邊界、MoE Tomography、異質模型比較與 Mother AI 自我模型研究

---

## 摘要

本文提出 **Capability Boundary Tomography（CBT，能力邊界斷層測量）**。前八篇已建立 Resident Cognitive Core、Conditional Intelligence、Externalized Mixture of Cognitive Experts、Temporary Cognition 與 Mother AI as Cognitive Command Tower。當 Mother AI 能在自己、內部 MoE experts、外部模型、Sub-AI、工具與 deterministic executors 之間動態路由任務後，一個新的研究問題出現：

> **Mother AI 如何知道「自己會什麼」、其他模型會什麼、能力邊界在哪裡，以及這些邊界何時已經改變？**

本文主張，能力不能被表示成單一 scalar：

$$
\boxed{
C(M)=87.
}
$$

也不能只依賴 model card、leaderboard 或模型自我宣告。更合理的表示是：

$$
\boxed{
\widehat{\mathcal C}_i(t)
=
\text{versioned, task-conditioned, evidence-bearing capability field}.
}
$$

對 Mother AI：

$$
\widehat{\mathcal C}_M(t)
$$

是 self-capability model；

對外部 executor：

$$
\widehat{\mathcal C}_{X_i}(t)
$$

是 other-capability model。

本文將能力邊界定義為：

$$
\boxed{
\partial\mathcal C_i
=
\{T:
P(\operatorname{VerifiedSuccess}(X_i,T))
\approx
\theta
\}
}
$$

其中 $\theta$ 是指定 deployment 下的可接受 success threshold。能力邊界因此不是絕對的「會／不會」，而是受到：

- task representation；
- context；
- tool access；
- reasoning budget；
- verifier；
- latency；
- model version；
- prompting；
- external evidence；

影響的條件邊界。

本文把能力測量分成兩個互補方向：

$$
\boxed{
\text{Internal Tomography}
}
$$

與：

$$
\boxed{
\text{Comparative External Tomography}.
}
$$

Internal Tomography 研究 MoE routing、expert activation、ablation、route forcing、group perturbation、path replacement 與 hidden-state boundary signals；Comparative External Tomography 則比較 Mother AI、不同模型、Sub-AI、工具與 deterministic systems 在同一任務、同一 evidence contract、同一 verifier 下的成功／失敗差異。

本文提出最重要的新命題：

$$
\boxed{
\text{Delegation}
=
\text{Execution}
+
\text{Measurement}.
}
$$

每次 Mother AI 把任務 $T$ 交給 executor $X_i$，除了取得 output，也得到一筆能力證據：

$$
\boxed{
e_t
=
(
T_t,
X_i,
C_t,
B_t,
V_t,
O_t,
Y_t
)
}
$$

其中：

- $T_t$：任務；
- $X_i$：executor；
- $C_t$：context / tools；
- $B_t$：compute / reasoning budget；
- $V_t$：verification contract；
- $O_t$：output；
- $Y_t$：verified outcome。

若 Mother 失敗而 child 成功：

$$
V(O_M)=0,
\qquad
V(O_i)=1,
$$

則：

$$
\boxed{
\widehat{\mathcal C}_M^{t+1}
\neq
\widehat{\mathcal C}_M^t
}
$$

且：

$$
\boxed{
\widehat{\mathcal C}_{X_i}^{t+1}
\neq
\widehat{\mathcal C}_{X_i}^t.
}
$$

這表示 Sub-AI 不只是 labor：

$$
\boxed{
\text{Sub-AI is also an epistemic instrument.}
}
$$

它幫助 Mother AI 測量自己與其他智能的能力邊界。

本文引用 2025–2026 年的最新結果支持這個問題確實存在。Large Reasoning Model capability-boundary 研究顯示 reasoning expressions 與 pre-reasoning hidden states 可以包含 solvable / unsolvable 的邊界信號；UA-Bench 顯示 frontier LLM 仍難區分 data uncertainty 與 model uncertainty；AwarenessBench 顯示 metacognition / self-awareness 與一般語言或 reasoning progress 並不完全同步；LLMRouterBench 在大規模模型路由評測中確認 model complementarity，同時指出距離 Oracle router 仍有顯著落差；InferenceDynamics 更開始直接建立多維 capability / knowledge profile 以支援 routing。

本文因此提出：

$$
\boxed{
\text{Capability Model}
\neq
\text{Benchmark Table}.
}
$$

真正的 Capability Model 至少需要：

$$
\boxed{
\mathcal P_i
=
(
\mathcal T,
Q,
U,
C,
B,
V,
L,
R,
t,
v
)
}
$$

其中：

- $\mathcal T$：task region；
- $Q$：verified quality；
- $U$：uncertainty / calibration；
- $C$：context dependence；
- $B$：budget dependence；
- $V$：verification dependence；
- $L$：latency；
- $R$：risk / failure pattern；
- $t$：time；
- $v$：concrete model version。

本文提出 **Boundary Active Probing**：Mother AI 不只被動累積 production history，也可以選擇靠近能力邊界的任務：

$$
\boxed{
T
\approx
\partial\mathcal C_i
}
$$

進行低風險 probe，以最大化資訊增益：

$$
\boxed{
T^\ast
=
\arg\max_T
I(
Y_T;
\widehat{\mathcal C}_i
).
}
$$

這使能力探索從 benchmark evaluation 轉成持續的 active system identification。

本文最後提出：

$$
\boxed{
\mathcal C_{\mathrm{system}}
=
\operatorname{Closure}
\left(
\mathcal C_M
\cup
\bigcup_i
\mathcal C_{X_i}
\cup
\mathcal C_{\mathrm{coordination}}
\right).
}
$$

系統能力不等於 Mother 能力，也不等於最強 worker 能力；它包含能力互補、routing、verification、context compilation 與組織能力所形成的 closure。

本文提出十八項主要命題、十五類失敗模式與十二組可否證實驗。若未來實驗顯示：能力表現對 task phrasing / context 的變動大到無法形成可重用邊界；self-boundary signals 無法改善 routing / stopping；comparative delegation history 對未來 executor selection 無預測力；MoE internal tomography 與 external capability profiles 無法提供任何可利用的共通結構；或 active probing 的成本長期高於 routing gain，則本文命題應被限制。

本文的核心問題不是：

> **哪個模型比較強？**

而是：

$$
\boxed{
\text{Which intelligence is strong at what, under which conditions,}
}
$$

$$
\boxed{
\text{and how does the system know when that statement has stopped being true?}
}
$$

**關鍵詞：** Capability Boundary、Capability Tomography、Metacognition、MoE Interpretability、Model Routing、Sub-AI、Self-Awareness、Uncertainty Attribution、Active Probing、Mother AI

---

# 0. 研究定位

Paper 04 建立：

$$
\boxed{
\text{Internal MoE Capability Tomography}.
}
$$

Paper 08 建立：

$$
\boxed{
\text{Delegation as Capability Evidence}.
}
$$

Paper 09 將兩者統一。

---

# 1. 能力不是一個點

最簡單：

$$
\boxed{
C(M)=q.
}
$$

例如：

> 模型能力 90 分。

這對 routing 幾乎沒有意義。

---

# 2. 能力更像區域

令 task space：

$$
\mathcal T.
$$

Executor：

$$
X_i.
$$

則：

$$
\boxed{
\mathcal C_i
\subseteq
\mathcal T.
}
$$

表示可可靠完成的 task region。

---

# 3. Verified Capability Region

定義：

$$
\boxed{
\mathcal C_i^{(\theta)}
=
\{
T:
P(
\operatorname{VerifiedSuccess}(X_i,T)
)
\ge
\theta
\}.
}
$$

---

# 4. 能力邊界

$$
\boxed{
\partial\mathcal C_i^{(\theta)}
}
$$

是 success probability 接近 threshold 的區域。

---

# 5. 邊界不是固定

$$
\boxed{
\partial\mathcal C_i
=
f(
context,
tools,
budget,
version,
prompt,
verifier,
time
).
}
$$

---

# 6. 有工具與沒工具是不同能力域

$$
\mathcal C_i^{tool}
\neq
\mathcal C_i^{no-tool}.
$$

因此 model-only benchmark 不能直接等同 agent capability。

---

# 7. 有 retrieval 與無 retrieval 也不同

$$
\mathcal C_i^{RAG}
\neq
\mathcal C_i^{closed}.
$$

---

# 8. Reasoning Budget 改變邊界

$$
\mathcal C_i^{B_1}
\subseteq
\mathcal C_i^{B_2}
$$

可能成立，若：

$$
B_1<B_2.
$$

---

# 9. 但 More Compute 不保證成功

hard task 上：

$$
\text{reasoning tokens}\uparrow
$$

可能只造成：

$$
\boxed{
\text{longer failure}.
}
$$

因此 boundary awareness 很重要。

---

# 10. 2025 Capability-Boundary 研究的意義

Large reasoning model 研究發現：

- reasoning expression 有 boundary signal；
- pre-reasoning hidden state 也可能區分 solvable / unsolvable。

這表示：

$$
\boxed{
\text{capability boundary information}
}
$$

可能在答案生成前就部分存在。

---

# 11. Boundary Signal

概念上：

$$
\boxed{
b_i(T)
=
P(
T\in\mathcal C_i
\mid
s_{\mathrm{pre}}
).
}
$$

---

# 12. Self-Estimate 不等於 Truth

即使模型輸出：

$$
\hat p=0.9,
$$

仍需要：

$$
\boxed{
\operatorname{Calibration}.
}
$$

---

# 13. Calibration

如果：

$$
\hat p=0.8
$$

的一組任務中，

約：

$$
80\%
$$

成功，

才是較好 calibration。

---

# 14. UA-Bench 的重要區分

UA-Bench 分：

$$
\boxed{
\text{Data Uncertainty}
}
$$

與：

$$
\boxed{
\text{Model Uncertainty}.
}
$$

---

# 15. Data Uncertainty

問題本身：

- ambiguous；
- missing information；
- underspecified。

---

# 16. Model Uncertainty

問題有足夠資訊，

但：

$$
\boxed{
X_i
}
$$

能力不足。

---

# 17. 兩者行動不同

Data uncertainty：

$$
\boxed{
\text{ask / retrieve missing data}.
}
$$

Model uncertainty：

$$
\boxed{
\text{delegate / escalate / use tool}.
}
$$

---

# 18. 因此 Boundary Attribution 是 Control Primitive

如果兩者混淆，

Mother AI 會：

- 問不必要問題；
- 無限自己重試；
- 不必要 escalation；
- hallucinate。

---

# 19. AwarenessBench 的啟示

AwarenessBench 顯示：

$$
\boxed{
\text{reasoning progress}
\not\Rightarrow
\text{metacognitive progress}.
}
$$

因此：

$$
\boxed{
\text{answer skill}
}
$$

與：

$$
\boxed{
\text{boundary skill}
}
$$

要分開測。

---

# 20. Capability Boundary Quality

定義：

$$
\boxed{
Q_B
=
f(
\text{discrimination},
\text{calibration},
\text{attribution},
\text{action quality}
).
}
$$

---

# 21. Boundary-Aware Action

真正重要不是：

> 模型說「我不知道」。

而是：

$$
\boxed{
\text{Does it choose the right next action?}
}
$$

---

# 22. Internal Tomography

對 white-box / MoE：

$$
\boxed{
\mathcal T_{\mathrm{internal}}.
}
$$

研究：

- routing；
- activation；
- hidden states；
- expert ablation；
- path intervention。

---

# 23. External Tomography

對 black-box / heterogeneous models：

$$
\boxed{
\mathcal T_{\mathrm{external}}.
}
$$

研究：

- verified success；
- latency；
- uncertainty；
- tool use；
- failure patterns。

---

# 24. 兩者的共同抽象

都在估計：

$$
\boxed{
\text{where capability changes}.
}
$$

---

# 25. Internal Capability Gradient

對 task direction：

$$
d
$$

概念上：

$$
\boxed{
\nabla_d Q_i
}
$$

表示 task difficulty / property 改變時 performance slope。

---

# 26. External Capability Gradient

同樣可以：

$$
\boxed{
Q_i(T+\Delta T)-Q_i(T).
}
$$

---

# 27. Boundary Tomography 的核心不是 Label

不是：

> Expert 12 = math。

而是：

$$
\boxed{
\text{which intervention changes which verified behavior, under which task perturbation}.
}
$$

---

# 28. Task Perturbation

同一 base task：

$$
T_0.
$$

產生：

$$
\boxed{
T(\delta)
}
$$

逐步改變：

- depth；
- distractor；
- context；
- novelty；
- tool requirement；
- ambiguity。

---

# 29. Boundary Sweep

$$
\boxed{
\delta_1<\delta_2<\cdots<\delta_n.
}
$$

測：

$$
Q_i(\delta).
$$

---

# 30. Crossover Point

若：

$$
Q_i(\delta^\ast)=\theta,
$$

則：

$$
\boxed{
\delta^\ast
}
$$

是該 task axis 上的 boundary estimate。

---

# 31. 多維邊界

真實 task：

$$
T
=
(
d,
n,
c,
u,
r,
v
).
$$

例如：

- difficulty；
- novelty；
- context length；
- uncertainty；
- retrieval need；
- verification difficulty。

---

# 32. Capability Surface

$$
\boxed{
Q_i
=
Q_i(
d,n,c,u,r,v
).
}
$$

---

# 33. Capability Boundary 是 Hypersurface

$$
\boxed{
Q_i(\mathbf x)=\theta.
}
$$

因此：

$$
\partial\mathcal C_i
$$

是高維 hypersurface。

---

# 34. 不同模型的邊界不必嵌套

常見假設：

$$
\mathcal C_{\mathrm{small}}
\subseteq
\mathcal C_{\mathrm{large}}.
$$

但模型互補性表示：

$$
\boxed{
\mathcal C_i-\mathcal C_j
\neq\varnothing
}
$$

可能成立。

---

# 35. LLMRouterBench 的重要證據

大規模 routing benchmark 確認：

$$
\boxed{
\text{model complementarity}
}
$$

是真實現象。

但很多 router 與 Oracle 仍有大差距。

---

# 36. Router Gap

定義：

$$
\boxed{
G_R
=
Q_{\mathrm{oracle}}
-
Q_{\mathrm{router}}.
}
$$

---

# 37. Persistent Model-Recall Failure

Router 未選出真正適合的模型，

即使 pool 裡存在能做的 model。

這是：

$$
\boxed{
\text{capability-model failure}.
}
$$

---

# 38. 更多模型不一定更好

LLMRouterBench 顯示 larger ensemble 可能有 diminishing returns。

因此：

$$
\boxed{
\text{Model Count}
\neq
\text{Capability Coverage Quality}.
}
$$

---

# 39. Curation Matters

更重要的是：

$$
\boxed{
\text{complementary model set}.
}
$$

而不是無限增加模型。

---

# 40. InferenceDynamics 的意義

InferenceDynamics 直接建立：

$$
\boxed{
\text{multi-dimensional capability and knowledge profiles}.
}
$$

這與本文 capability field 非常接近。

---

# 41. 但本文再多一層

本文需要：

- production evidence；
- self-boundary；
- delegation outcome；
- verifier；
- version history；
- active probing。

因此：

$$
\boxed{
\text{Capability Profile}
\rightarrow
\text{Persistent Capability Field}.
}
$$

---

# 42. Capability Passport

定義：

$$
\boxed{
\mathcal P_i
=
(
I_i,
\mathcal T_i,
Q_i,
U_i,
C_i,
B_i,
V_i,
L_i,
R_i,
t_i,
v_i
).
}
$$

---

# 43. Identity

$$
I_i
$$

必須是 concrete model / executor identity。

---

# 44. Task Region

$$
\mathcal T_i
$$

不是一個 category label。

應包含 task properties。

---

# 45. Quality

$$
Q_i
$$

必須是 verified quality。

---

# 46. Uncertainty

$$
U_i
$$

包括：

- calibration；
- abstention；
- uncertainty attribution。

---

# 47. Context Dependence

$$
C_i
$$

描述：

> 需要多少 context 才能成功？

---

# 48. Budget Dependence

$$
B_i
$$

描述：

> reasoning / compute 增加後能力如何變？

---

# 49. Verification Dependence

$$
V_i
$$

描述：

> output 是否容易被驗證？

---

# 50. Latency

$$
L_i
$$

是 production capability 的一部分。

---

# 51. Risk / Failure Pattern

$$
R_i
$$

保存：

- hallucination；
- formatting；
- omission；
- tool misuse；
- overconfidence。

---

# 52. Time / Version

$$
(t_i,v_i)
$$

使 capability evidence 可重放。

---

# 53. 不能用 Latest Alias

$$
\boxed{
\text{model-latest}
}
$$

不夠。

因為：

$$
\text{latest}(t_1)
\neq
\text{latest}(t_2).
$$

---

# 54. Capability Evidence Event

每次實驗：

$$
\boxed{
e_t
=
(
T_t,
X_i,
C_t,
B_t,
V_t,
O_t,
Y_t
).
}
$$

---

# 55. Verified Outcome

$$
Y_t
\in
\{
success,
partial,
failure,
unknown
\}.
$$

---

# 56. Terminal Success 不等於 Verified Success

模型回成功：

$$
\boxed{
\text{terminal success}
}
$$

只是 claim。

必須：

$$
\boxed{
V(O)=1
}
$$

才算 evidence。

---

# 57. Comparative Delegation

同一 task：

$$
T
$$

交給：

$$
M,
X_1,X_2.
$$

得到：

$$
Y_M,Y_1,Y_2.
$$

---

# 58. 四個基本比較狀態

## A

$$
M=1,
\quad
X=1.
$$

共同能力。

## B

$$
M=1,
\quad
X=0.
$$

Mother local advantage。

## C

$$
M=0,
\quad
X=1.
$$

External comparative advantage。

## D

$$
M=0,
\quad
X=0.
$$

system gap。

---

# 59. 狀態 C 最重要

如果：

$$
M=0,
\quad
X_i=1,
$$

則：

$$
\boxed{
\mathcal C_{X_i}-\mathcal C_M
\neq
\varnothing.
}
$$

這推翻：

$$
\boxed{
\mathcal C_{X_i}
\subseteq
\mathcal C_M
}
$$

的預設。

---

# 60. Mother 不必局部最強

只要：

$$
\boxed{
\text{Mother knows the difference}.
}
$$

---

# 61. Delegation as Measurement

每次：

$$
M\rightarrow X_i
$$

同時生成：

$$
\boxed{
\text{task output}
+
\text{capability evidence}.
}
$$

---

# 62. Sub-AI as Epistemic Instrument

因此：

$$
\boxed{
\text{Sub-AI}
=
\text{Labor}
+
\text{Measurement Instrument}.
}
$$

---

# 63. 工具也是 Instrument

Python / compiler / search 也可以測：

> 這個 task 是否其實不應該由 LLM 完成？

---

# 64. Deterministic Dominance Region

存在：

$$
\boxed{
\mathcal C_D
}
$$

使 deterministic program：

$$
Q_D>Q_{\mathrm{LLM}}
$$

且：

$$
C_D<C_{\mathrm{LLM}}.
$$

---

# 65. Capability Tomography 要包含非 AI executors

否則：

$$
\boxed{
\text{AI-only benchmark}
}
$$

會高估 AI 適用域。

---

# 66. Self-Capability Model

Mother 保存：

$$
\boxed{
\widehat{\mathcal C}_M.
}
$$

---

# 67. Other-Capability Model

對每個：

$$
X_i,
$$

保存：

$$
\boxed{
\widehat{\mathcal C}_{X_i}.
}
$$

---

# 68. 系統 Capability Atlas

$$
\boxed{
\mathcal A_C
=
\{
\widehat{\mathcal C}_M,
\widehat{\mathcal C}_{X_1},
\dots
\}.
}
$$

---

# 69. Atlas 不等於 Static Benchmark Table

它是：

- versioned；
- conditional；
- uncertainty-bearing；
- continuously updated。

---

# 70. Bayesian Update

概念上：

$$
\boxed{
P(
\mathcal C_i
\mid
E_{1:t}
)
\propto
P(
E_t
\mid
\mathcal C_i
)
P(
\mathcal C_i
\mid
E_{1:t-1}
).
}
$$

不要求實作一定 Bayesian。

---

# 71. Confidence Decay

舊 evidence：

$$
e_{t-k}
$$

可能隨版本與時間：

$$
w(e)\downarrow.
$$

---

# 72. Drift Detection

如果：

$$
Q_i^{new}
-
Q_i^{old}
$$

持續偏離，

觸發：

$$
\boxed{
\text{requalification}.
}
$$

---

# 73. Capability Drift 不是只有退化

也可能：

$$
Q_i\uparrow.
$$

新版本突然擅長舊版本不會的 task。

---

# 74. 因此固定 routing 會過時

$$
\boxed{
\pi_t
\neq
\pi_{t+\Delta}.
}
$$

---

# 75. Active Capability Probing

被動 production history 只會覆蓋：

$$
\mathcal T_{\mathrm{observed}}.
$$

可能看不到真正 boundary。

---

# 76. Probe near Boundary

選：

$$
\boxed{
T
\approx
\partial\mathcal C_i.
}
$$

資訊量最高。

---

# 77. Active Learning 類比

如果 task：

$$
T
$$

模型顯然會：

$$
P\approx1,
$$

或顯然不會：

$$
P\approx0,
$$

資訊增益較低。

---

# 78. Boundary Uncertainty

$$
\boxed{
H_B(T)
=
H(
P(
T\in\mathcal C_i
)
).
}
$$

---

# 79. Probe Selection

$$
\boxed{
T^\ast
=
\arg\max_T
\frac{
I(
Y_T;
\mathcal C_i
)
}{
C_{\mathrm{probe}}(T)
}.
}
$$

---

# 80. Probe 必須 Low-Risk

不能為了測 capability：

$$
\boxed{
\text{execute dangerous real-world action}.
}
$$

使用：

- sandbox；
- simulation；
- offline benchmark；
- synthetic task。

---

# 81. Probe 也可以 Pairwise

若不知道：

$$
X_i
$$

與：

$$
X_j
$$

誰更適合，

選：

$$
T
$$

最大化：

$$
\boxed{
P(Y_i\neq Y_j).
}
$$

---

# 82. Discriminative Probe

這比：

$$
\boxed{
\text{random benchmark expansion}
}
$$

更有效率。

---

# 83. Boundary Decomposition

能力邊界失敗可能來自：

- knowledge；
- reasoning；
- context；
- tool；
- uncertainty；
- format；
- verification。

因此：

$$
\boxed{
\text{failure reason}
}
$$

本身要分類。

---

# 84. Failure Attribution

$$
\boxed{
F_T
\in
\{
knowledge,
reasoning,
context,
tool,
policy,
format,
unknown
\}.
}
$$

---

# 85. Data vs Model Uncertainty 是其中一個切面

UA-Bench 對：

$$
\boxed{
\text{data}
\quad vs \quad
\text{model}
}
$$

提供重要基本分法。

---

# 86. Capability Tomography 再擴張

本文需要：

$$
\boxed{
\text{why failed}
}
$$

不只：

$$
\boxed{
\text{failed}.
}
$$

---

# 87. Failure Mode Boundary

某 model 可能：

- knowledge task 失敗；
- reasoning task 成功。

另一個反過來。

所以：

$$
\boxed{
\partial\mathcal C_i
}
$$

也有 failure semantics。

---

# 88. MoE Internal Tomography 回歸

對 MoE：

$$
\rho_T(l,e)
$$

routing fingerprint。

---

# 89. Expert Contribution

$$
\boxed{
I_e(T)
=
Q(T)-Q(T\mid -E_e).
}
$$

---

# 90. Route Forcing

$$
Q(T\mid r\rightarrow e).
$$

---

# 91. Internal Boundary Signal

如果某 task 接近：

$$
\partial\mathcal C_M,
$$

可能看到：

- routing entropy ↑；
- margin ↓；
- certain experts overused；
- hidden-state signal 改變。

---

# 92. 這是可檢驗猜想

本文不宣稱一定成立。

只是提出：

$$
\boxed{
\text{internal dynamics may predict external capability boundary}.
}
$$

---

# 93. Internal–External Boundary Correlation

定義：

$$
\boxed{
\rho_{IE}
=
\operatorname{Corr}
(
S_{\mathrm{internal}},
Y_{\mathrm{external}}
).
}
$$

---

# 94. 如果 $\rho_{IE}$ 高

可以提前：

- stop；
- delegate；
- increase budget。

---

# 95. 如果 $\rho_{IE}$ 低

Internal tomography 只能用於 interpretability，

不能用於 routing control。

---

# 96. Cross-Model Internal Homology

不同 MoE：

$$
M_1,M_2
$$

可能有不同 expert indices，

但相似：

$$
\boxed{
\text{boundary dynamics}.
}
$$

---

# 97. Functional Boundary Homology

例如：

- routing entropy pattern；
- confidence collapse；
- expert-set transition；

在 capability crossover 附近重現。

---

# 98. Capability Boundary Is Not Failure Line Only

也存在：

$$
\boxed{
\text{cost boundary}.
}
$$

---

# 99. Economic Capability Boundary

如果：

$$
Q_i>\theta
$$

但：

$$
C_i>C_{\max},
$$

對 deployment 而言仍不可用。

---

# 100. Latency Boundary

如果：

$$
L_i>L_{\max},
$$

則：

$$
T
\notin
\mathcal C_i^{deploy}.
$$

---

# 101. Verification Boundary

如果 output 無法在風險要求內驗證，

也可能不屬於 deployable capability。

---

# 102. Deployable Capability

因此：

$$
\boxed{
\mathcal C_i^{D}
=
\{
T:
Q_i\ge\theta_Q,
C_i\le\theta_C,
L_i\le\theta_L,
V_i\ge\theta_V,
R_i\le\theta_R
\}.
}
$$

---

# 103. Capability Boundary 是 Multi-Constraint Frontier

這比單一 accuracy threshold 更符合 production。

---

# 104. Mother Boundary vs System Boundary

Mother：

$$
\mathcal C_M.
$$

System：

$$
\mathcal C_S.
$$

通常希望：

$$
\boxed{
\mathcal C_M
\subseteq
\mathcal C_S.
}
$$

---

# 105. System Closure

$$
\boxed{
\mathcal C_S
=
\operatorname{Closure}
(
\mathcal C_M
\cup
\bigcup_i
\mathcal C_{X_i}
\cup
\mathcal C_{\mathrm{coord}}
).
}
$$

---

# 106. Coordination Can Create New Capability

可能：

$$
T\notin\mathcal C_M,
$$

$$
T\notin\mathcal C_{X_1},
$$

$$
T\notin\mathcal C_{X_2},
$$

但：

$$
T\in
\mathcal C_{\mathrm{coord}}(M,X_1,X_2).
$$

---

# 107. Emergent System Capability

這是：

$$
\boxed{
\text{organizational capability}.
}
$$

---

# 108. 但 Coordination 也可能毀掉能力

$$
Q_{\mathrm{coord}}
<
\max_iQ_i
$$

也可能。

---

# 109. System Boundary 需要獨立測

不能從 individual capabilities 直接相加推導。

---

# 110. Capability Complementarity

定義：

$$
\boxed{
K_{ij}
=
\mu(
\mathcal C_i
\triangle
\mathcal C_j
)
}
$$

其中：

$$
\triangle
$$

為 symmetric difference。

---

# 111. Complementarity 高不一定好

如果兩者都只擅長低價值 task，

system gain 小。

---

# 112. Value-Weighted Complementarity

$$
\boxed{
K_{ij}^{V}
=
\int_{\mathcal T}
w(T)
\mathbf 1[
Y_i(T)\neq Y_j(T)
]
dT.
}
$$

---

# 113. Model Pool Curation

選：

$$
\boxed{
\mathcal X^\ast
=
\arg\max_{\mathcal X}
\operatorname{Coverage}
-
\lambda Cost
-
\mu Redundancy.
}
$$

---

# 114. 這比「模型越多越好」合理

對應 LLMRouterBench 的 diminishing returns。

---

# 115. Boundary-Aware Routing

Router：

$$
\boxed{
\pi(
T,
\widehat{\mathcal C}
)
\rightarrow
X_i.
}
$$

---

# 116. Router 不只預測 Winner

也可以預測：

$$
\boxed{
\text{none suitable}.
}
$$

---

# 117. No-Suitable-Model 是合法輸出

此時：

$$
\boxed{
\text{decompose / retrieve / human / abort}.
}
$$

---

# 118. Oracle Gap 可以被 Capability Tomography 縮小

如果：

$$
\widehat{\mathcal C}_i
$$

更準，

希望：

$$
G_R\downarrow.
$$

這是可否證目標。

---

# 119. Boundary-Aware Stop

如果：

$$
P(
T\in\mathcal C_M
)
\ll\theta,
$$

Mother 不應無限思考。

---

# 120. Boundary-Aware Escalation

$$
\boxed{
\text{low self capability}
+
\text{high external capability}
\rightarrow
\text{delegate}.
}
$$

---

# 121. Boundary-Aware Clarification

若：

$$
\text{data uncertainty}\uparrow,
$$

則：

$$
\boxed{
\text{ask}.
}
$$

---

# 122. Boundary-Aware Tool Use

若：

$$
\text{model uncertainty}
$$

來自：

- arithmetic；
- current data；
- execution；

則選 tool。

---

# 123. Capability Awareness 直接影響 Cognitive Density

如果能提前停止無效 reasoning：

$$
C_{\mathrm{active}}\downarrow.
$$

---

# 124. 2025 Boundary-Aware Reasoning 的效率信號

現有研究報告 boundary-aware strategies 可大幅減少無效 reasoning token，而不犧牲 accuracy。

這支持：

$$
\boxed{
\text{metacognitive boundary modeling}
}
$$

具有直接 compute value。

---

# 125. Capability Tomography 也是安全問題

不知道自己不會：

$$
\rightarrow
\text{hallucination}.
$$

不知道工具不存在：

$$
\rightarrow
\text{fabricated action}.
$$

---

# 126. CAR-bench 的意義

CAR-bench 專門測：

- missing tools；
- ambiguous requests；
- limit-awareness；
- clarification。

這說明 capability awareness 已從靜態 QA 進入 real-world agent setting。

---

# 127. Capability Boundary 要測 Action

不是只問：

> 你有多有信心？

而是：

$$
\boxed{
\text{你接下來做了什麼？}
}
$$

---

# 128. Knowing-to-Act Gap

模型可能知道：

> 自己不確定。

但仍然：

$$
\boxed{
\text{take wrong action}.
}
$$

因此：

$$
\boxed{
\text{awareness}
\neq
\text{control}.
}
$$

---

# 129. Action-Calibrated Boundary

定義：

$$
\boxed{
Q_{BA}
=
P(
\text{correct next action}
\mid
\text{boundary state}
).
}
$$

---

# 130. Capability Passport 必須包括 Action Policy

不只是：

$$
Q_i.
$$

還要：

$$
\boxed{
\text{when to abstain / ask / delegate}.
}
$$

---

# 131. Production Tomography

真實任務可以持續更新：

$$
\mathcal A_C.
$$

---

# 132. 但 Production Data 有 Selection Bias

Mother 只會把某些 task 給某 model。

因此：

$$
\boxed{
\text{observed success}
}
$$

不是隨機樣本。

---

# 133. Counterfactual Evaluation

需要偶爾：

$$
\boxed{
\text{shadow routing}.
}
$$

同一 task 在 sandbox 給另一個 model，

測 counterfactual outcome。

---

# 134. Shadow Evaluation

$$
\boxed{
T
\rightarrow
\begin{cases}
X_{\mathrm{prod}}\\
X_{\mathrm{shadow}}
\end{cases}
}
$$

shadow 不影響 production state。

---

# 135. Shadow Cost

需要控制：

$$
C_{\mathrm{shadow}}.
$$

不是所有 task 都多跑一遍。

---

# 136. Selective Shadowing

只對：

- boundary；
- new model；
- uncertain router；

執行。

---

# 137. New Model Qualification

新：

$$
X_j
$$

不能只看 vendor benchmark。

需要：

$$
\boxed{
\text{probe against current Atlas}.
}
$$

---

# 138. Model Entry Test

選一組：

$$
\mathcal T_{\mathrm{discriminative}}.
$$

測：

> 它到底增加了哪些 coverage？

---

# 139. Duplicate Model

如果：

$$
\mathcal C_j
\approx
\mathcal C_i
$$

且 cost 更高，

則：

$$
\boxed{
\text{no system value}.
}
$$

---

# 140. Novel Specialist

如果：

$$
\mathcal C_j-\mathcal C_{\mathrm{pool}}
$$

很大，

即使 overall benchmark 不最高，也可能很有價值。

---

# 141. 這改變模型採購邏輯

不是：

> 誰排行榜最高？

而是：

$$
\boxed{
\text{Who fills the capability gap?}
}
$$

---

# 142. Capability Gap

$$
\boxed{
G_C
=
\mathcal T_{\mathrm{needed}}
-
\mathcal C_{\mathrm{system}}.
}
$$

---

# 143. Probe Gap

Mother AI 可以針對：

$$
G_C
$$

尋找：

- model；
- tool；
- human；
- new training。

---

# 144. Capability Atlas 也是 Discovery Map

它不只知道：

> 我們會什麼？

還知道：

$$
\boxed{
\text{我們缺什麼？}
}
$$

---

# 145. Internal MoE 可以揭示 Native Gap

如果某 task 接近 failure boundary，

MoE route pattern 可能指出：

> 缺乏哪類 internal conditional capacity？

---

# 146. External Pool 可以補 Gap

如果 internal：

$$
Q_M<\theta
$$

external：

$$
Q_X>\theta,
$$

則先 externalize。

---

# 147. 後續可決定是否 Internalize

如果該 gap：

- high frequency；
- high latency cost；
- critical；

可能：

$$
\boxed{
X\rightarrow Q\rightarrow R.
}
$$

---

# 148. Tomography 因此回饋 Cognitive Factorization

Paper 06：

$$
D,C,X,L,R,G.
$$

Paper 09 提供：

$$
\boxed{
\text{which factors are actually needed where}.
}
$$

---

# 149. Capability Boundary 也回饋 MoE

Paper 04：

$$
\mathcal C_Q.
$$

Paper 09 可以問：

> expert set 對 boundary task 有什麼 causal effect？

---

# 150. Boundary-Centric MoE Analysis

不是對平均 benchmark。

而是集中：

$$
\boxed{
T\approx\partial\mathcal C_M.
}
$$

---

# 151. 因為邊界區最有資訊

如果 task 太簡單，

所有 experts 都成功。

難以辨識：

$$
\boxed{
\text{who matters}.
}
$$

---

# 152. Boundary Perturbation + Expert Ablation

$$
\boxed{
T(\delta)
+
Ablate(E_i)
}
$$

可以得到更敏感的 causal map。

---

# 153. Capability Tomography 的六個層級

## Level 0：Benchmark

平均 performance。

## Level 1：Task-Family Profile

domain / task type。

## Level 2：Conditioned Capability

context / tools / budget。

## Level 3：Boundary Map

success frontier。

## Level 4：Causal Tomography

internal intervention / comparative delegation。

## Level 5：Adaptive Capability Atlas

持續更新 + active probing + routing feedback。

---

# 154. Paper 09 聚焦 Level 3–5

這是與普通 benchmark 的主要差別。

---

# 155. Capability Evidence Quality

每筆：

$$
e_t
$$

需要 evidence grade。

---

# 156. Grade 0

Self-report only。

---

# 157. Grade 1

Output looks plausible。

---

# 158. Grade 2

Independent model review。

---

# 159. Grade 3

Source / test grounded。

---

# 160. Grade 4

Mechanical verification / reproducible proof。

---

# 161. 能力 Atlas 應偏重高級 Evidence

$$
\boxed{
w(e)
=
f(
grade,
freshness,
task fit
).
}
$$

---

# 162. 不應把 24 個 API Success 當 24 個 Correct

Terminal status：

$$
\boxed{
\neq
\text{capability evidence unless verified}.
}
$$

---

# 163. 這是能力研究常見陷阱

模型完成：

$$
\text{candidate}
$$

不等於：

$$
\boxed{
\text{task solved}.
}
$$

---

# 164. Benchmark Leakage

如果 task 已在 training data：

$$
Q\uparrow
$$

可能來自 memorization。

因此 boundary probe 需要：

- novel variants；
- mutation；
- counterfactual；
- held-out generation。

---

# 165. Counterfactual Capability Test

改：

$$
\text{surface}
$$

保留：

$$
\text{structure}.
$$

測：

$$
\boxed{
\text{transfer}.
}
$$

---

# 166. Mutation Test

對 structured task：

$$
T
$$

做小變異，

看能力是否穩定。

---

# 167. Capability Is Distributional

單一 task 成功：

$$
\boxed{
\not\Rightarrow
T\subset\mathcal C_i.
}
$$

需要 task neighborhood。

---

# 168. Local Neighborhood

$$
\boxed{
N_\epsilon(T)
}
$$

中多個 variants 都成功，才支持 local capability region。

---

# 169. Boundary Smoothness

如果：

$$
Q(T)
$$

隨小 perturbation 劇烈跳動，

能力邊界可能：

$$
\boxed{
\text{highly fractal / unstable}.
}
$$

---

# 170. 這本身也是重要結果

不應強迫：

$$
\boxed{
\text{smooth capability map}.
}
$$

---

# 171. Capability Tomography 失敗模式 1：Benchmark-as-Boundary

平均分數被當成能力邊界。

---

# 172. Failure 2：Self-Confidence-as-Truth

模型自報 confidence 被直接相信。

---

# 173. Failure 3：Terminal-Success Inflation

API status 被當 correctness。

---

# 174. Failure 4：Static Capability Profile

模型更新後仍使用舊 profile。

---

# 175. Failure 5：Domain Label Overcompression

「coding model」這種粗 label 掩蓋內部能力差異。

---

# 176. Failure 6：Task-Context Confounding

不同 context 下結果被混在一起。

---

# 177. Failure 7：Verifier Bias

同一模型生成又自己驗證。

---

# 178. Failure 8：Production Selection Bias

只看到 router 本來就會分配的 task。

---

# 179. Failure 9：Over-Probing

為測能力浪費大量 compute。

---

# 180. Failure 10：Risky Probing

用真實高風險 action 測 boundary。

---

# 181. Failure 11：Internal-External Equivalence Fallacy

MoE expert boundary 與 model-level capability 被直接等同。

---

# 182. Failure 12：Capability Drift Blindness

忽略 model version / provider change。

---

# 183. Failure 13：Complementarity Illusion

不同模型只是隨機噪音，不是真正互補。

---

# 184. Failure 14：Atlas Overconfidence

把估計地圖當確定真理。

---

# 185. Failure 15：Measurement Changes Routing Distribution

Atlas 改善 routing 後，production data distribution 又變，造成 feedback bias。

---

# 186. 十八項主要命題

## 命題 1：Capability Region 命題

能力應建模為 task-conditioned region，而非單 scalar。

## 命題 2：Boundary Conditionality 命題

能力邊界依 context、tool、budget、version、verifier 改變。

## 命題 3：Self-Boundary Signal 命題

模型內部或 reasoning expression 可能包含 capability-boundary signal。

## 命題 4：Accuracy–Awareness Separation 命題

高 answer accuracy 不保證高 uncertainty attribution / boundary awareness。

## 命題 5：Data–Model Uncertainty Separation 命題

兩者需要不同控制行動。

## 命題 6：Model Complementarity 命題

不同模型能力域不必互相嵌套。

## 命題 7：Delegation-as-Measurement 命題

$$
\boxed{
\text{Delegation}
=
\text{Execution}
+
\text{Capability Evidence}.
}
$$

## 命題 8：Sub-AI-as-Epistemic-Instrument 命題

Sub-AI 可以用來測量 Mother 與外部智能邊界。

## 命題 9：Verified Capability Evidence 命題

capability update 應以 verified outcome 為核心。

## 命題 10：Persistent Capability Atlas 命題

Mother AI 應維持 versioned capability field，而不是 static benchmark table。

## 命題 11：Active Boundary Probing 命題

靠近 boundary 的 probe 通常具有較高資訊增益。

## 命題 12：Deployable Capability Frontier 命題

production capability 同時受 quality、cost、latency、verification、risk 約束。

## 命題 13：System Closure 命題

系統能力包括 Mother、workers 與 coordination 所形成的 closure。

## 命題 14：Organizational Capability 命題

某些 task 可由組合系統完成，而任何單一 component 無法完成。

## 命題 15：Boundary-Aware Routing 命題

更準確的 capability atlas 應縮小 router-to-oracle gap。

## 命題 16：Boundary-Aware Compute 命題

能力邊界估計可降低無效 reasoning / retry。

## 命題 17：Internal–External Correlation 命題

internal mechanistic signals 可能預測 external failure boundary，但必須實證。

## 命題 18：Capability Gap Navigation 命題

Mother AI 不只要知道能力，也要知道未覆蓋 gap 並主動尋找新資源。

---

# 187. 十二組可否證實驗

## 實驗 1：Boundary Sweep

對單一 task axis：

$$
\delta
$$

逐步增加 difficulty。

找：

$$
\delta^\ast.
$$

## 實驗 2：Self-Estimate Calibration

比較模型 boundary self-estimate 與 verified outcome。

## 實驗 3：Data vs Model Uncertainty

測 ask / retrieve / delegate 行動選擇。

## 實驗 4：Mother vs Worker Differential

同 task 給 Mother 與多個 workers，建立 comparative regions。

## 實驗 5：Tool-Conditioned Boundary

同模型：

- no tool；
- with tool。

比較：

$$
\partial\mathcal C.
$$

## 實驗 6：Budget-Conditioned Boundary

改 reasoning budget，測 capability expansion 與 waste。

## 實驗 7：Internal MoE Boundary Probe

在 boundary tasks 上記錄 routing / entropy / ablation signal。

## 實驗 8：Internal–External Prediction

用 internal signals 預測 external verified failure。

## 實驗 9：Atlas Routing

比較：

- static router；
- benchmark router；
- capability-atlas router；
- oracle。

## 實驗 10：Active Probing

比較 random probes 與 information-gain probes 的 Atlas learning efficiency。

## 實驗 11：Drift Detection

模型版本更新後測 Atlas requalification speed。

## 實驗 12：Pool Curation

比較：

- many redundant models；
- fewer complementary models。

測 coverage / cost / oracle gap。

---

# 188. 什麼結果會支持本文？

以下結果會支持：

1. capability boundary 在局部 task family 可重複估計；
2. self-boundary signal 對 verified failure 有預測力；
3. data / model uncertainty attribution 改善 next-action quality；
4. comparative delegation 顯示穩定 model complementarity；
5. capability history 改善 future routing；
6. active probing 以更少 calls 學到更準 Atlas；
7. internal MoE signals 可部分預測 external boundary；
8. capability-atlas router 縮小 Oracle gap；
9. complementary pool 優於單純 large pool；
10. boundary-aware stopping 降低 token waste；
11. drift detector 能在 model update 後快速修正 routing；
12. system closure 顯示 organizational capability。

---

# 189. 什麼結果會削弱本文？

以下結果會削弱：

1. capability boundary 對 prompt / seed 極端不穩；
2. self-boundary signal 無法泛化；
3. uncertainty attribution 不改善 action quality；
4. model complementarity 主要來自 random variance；
5. historical capability evidence 對未來無預測力；
6. active probing cost 高於 routing gain；
7. internal MoE signal 與 external failure 無關；
8. capability-atlas router 不優於簡單 baseline；
9. model drift 快到 Atlas 無法維護；
10. tool / context dependency 使 capability region 無法重用；
11. system closure 無法產生 individual components 之外的新能力；
12. model pool curation 對成本／品質無穩定收益。

---

# 190. 公開命題與未公開方法邊界

本文公開：

- Capability Region / Boundary；
- Capability Passport；
- Comparative Delegation；
- Delegation-as-Measurement；
- Sub-AI-as-Epistemic-Instrument；
- Active Boundary Probing；
- Capability Atlas；
- deployable capability frontier；
- falsification experiments。

本文不公開任何未驗證或未公開的：

- private capability embedding；
- boundary interpolation algorithm；
- active-probe generator；
- internal mechanistic projection；
- capability graph compiler；
- routing optimizer；
- capability update policy；
- hidden-state boundary classifier；
- private MACR qualification implementation。

因此：

$$
\boxed{
\text{Public Capability Tomography Theory}
\neq
\text{Private Capability Measurement Runtime}.
}
$$

---

# 191. 與 Paper 10 的銜接

Paper 09 已經建立：

$$
\boxed{
\widehat{\mathcal C}_M,
\widehat{\mathcal C}_{X_i},
\mathcal C_{\mathrm{system}}.
}
$$

系列最後只剩一個問題：

> **當 Resident Core、Conditional Experts、External Experts、Temporary Cognition、Cognitive Organization 與 Capability Atlas 同時存在時，這整個系統究竟是一種什麼樣的智能？**

因此 Paper 10：

$$
\boxed{
\text{Expandable Intelligence Synthesis}.
}
$$

將統合：

$$
\boxed{
\text{Resident}
+
\text{Conditional}
+
\text{External}
+
\text{Coordination}
+
\text{Reconvergence}.
}
$$

---

# 192. 結論

AI 能力研究長期習慣問：

> 哪個模型 benchmark 比較高？

但當模型開始：

- 使用不同 reasoning budget；
- 使用 tools；
- 使用 retrieval；
- 由 router 動態選擇；
- 與其他 models / agents 協作；

能力已經不再是一個固定 scalar。

因此本文提出：

$$
\boxed{
\text{Capability}
=
\text{conditioned region in task space}.
}
$$

並將其邊界：

$$
\boxed{
\partial\mathcal C_i
}
$$

視為可以被持續觀察、比較與更新的研究對象。

Internal MoE 提供：

$$
\boxed{
\text{routing / activation / intervention surface}.
}
$$

External heterogeneous systems 提供：

$$
\boxed{
\text{comparative success / failure surface}.
}
$$

兩者共同形成：

$$
\boxed{
\text{Capability Boundary Tomography}.
}
$$

最重要的是，delegation 不再只是：

$$
\boxed{
\text{讓別人做工作}.
}
$$

每次 delegation 都同時回答：

> Mother 自己會不會？

> Child 是否真的更好？

> Tool 是否其實比 AI 更適合？

> 哪個 model 的能力已經漂移？

因此：

$$
\boxed{
\text{Delegation}
=
\text{Execution}
+
\text{Measurement}.
}
$$

而 Sub-AI 也因此具有第二個角色：

$$
\boxed{
\text{Sub-AI}
=
\text{Cognitive Labor}
+
\text{Epistemic Instrument}.
}
$$

當 Mother AI 能持續將這些 evidence 累積成：

$$
\boxed{
\mathcal A_C
=
\{
\widehat{\mathcal C}_M,
\widehat{\mathcal C}_{X_1},
\ldots
\}
}
$$

它就不再只是在「猜誰比較適合」。

它開始擁有：

$$
\boxed{
\text{an empirical map of intelligence around itself}.
}
$$

更進一步，Mother AI 可以主動對：

$$
\boxed{
T
\approx
\partial\mathcal C_i
}
$$

進行低風險 active probe，

找到：

- 自己的 edge；
- worker 的 edge；
- system 的 gap；
- 新模型真正增加的 coverage；
- 哪些能力值得 internalize；
- 哪些能力適合 externalize。

因此 Capability Tomography 最終不只是 routing technology。

它是一種：

$$
\boxed{
\text{epistemology of heterogeneous intelligence}.
}
$$

也就是：

> **智能系統如何透過比較、干預、失敗、成功與驗證，逐步知道「誰能做什麼」以及「自己到底是什麼」。**

---

# References

1. Zhang, Q., Fu, Y., Wang, Y., Yan, L., Wei, T., Xu, K., Huang, M., & Qiu, H. (2025). *On the Self-awareness of Large Reasoning Models' Capability Boundaries*. arXiv:2509.24711.
2. Li, X., et al. (2026). *AwarenessBench: Assessing Cognitive Capabilities of Language Models*. ACL 2026.
3. Ren, J., et al. (2026). *Beyond "I Don't Know": Evaluating LLM Self-Awareness in Discriminating Data and Model Uncertainty*. ACL 2026.
4. Li, H., et al. (2026). *LLMRouterBench: A Massive Benchmark and Unified Framework for LLM Routing*. Findings of ACL 2026.
5. Shi, H., et al. (2026). *InferenceDynamics: Adaptive LLM Routing through Structured Capability and Knowledge Profiling*. ACL 2026.
6. Kirmayr, J., Stappen, L., & Andre, E. (2026). *CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty*. ACL 2026.
7. Herbst, J., Lee, J. H., & Wermter, S. (2026). *The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expert Level*. arXiv:2604.02178.
8. Falke, T., et al. (2026). *MoE Routing Testbed: Studying Expert Specialization and Routing Behavior at Small Scale*. arXiv:2604.07030.
9. Neo.K. & Aletheia. (2026). *MoE as Conditional Intelligence：Shared Core、Routed Experts 與能力局部化*.
10. Neo.K. & Aletheia. (2026). *Externalized Mixture of Cognitive Experts：為什麼 Expert 一定要住在同一個模型裡？*.
11. Neo.K. & Aletheia. (2026). *Mother AI as Cognitive Command Tower：異質認知資源的全局協調*.
12. Neo.K. & Aletheia. (2026). *Cognitive Density Hypothesis：認知密度命題*.
13. Neo.K. & Aletheia. (2026). *Resident Cognitive Core：Mother Model 到底必須常駐什麼？*.
14. Neo.K. & Aletheia. (2026). *子 AI 是認知器官，不是獨立 Workflow*.

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

- capability region / boundary；
- capability passport；
- comparative delegation；
- delegation-as-measurement；
- Sub-AI as epistemic instrument；
- active probing；
- capability atlas；
- deployable capability frontier；
- public falsification tests。

本文不公開任何未驗證或未公開的：

- private capability embedding；
- mechanistic projection；
- boundary interpolation；
- active-probe generator；
- capability graph compiler；
- routing optimization；
- hidden-state boundary classifier；
- private qualification runtime。

因此：

$$
\boxed{
\text{Public Capability Boundary Theory}
\neq
\text{Private Capability Tomography Engine}.
}
$$
