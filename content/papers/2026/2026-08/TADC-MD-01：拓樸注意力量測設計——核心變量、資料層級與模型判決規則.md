# TADC-MD-01：拓樸注意力量測設計——核心變量、資料層級與模型判決規則

**英文題名：** TADC Measurement Design 01: Core Variables, Data Layers, and Model-Adjudication Rules  
**系列階段：** TADC Phase II — Measurement Design  
**文件編號：** TADC-MD-01  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** Measurement Design／資料規格／模型比較前置文件  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

TADC-01 至 TADC-08 已建立一套關於可變認知空間、動態認知域、多尺度重索引、域級持續注意、關係優先跨域連續性，以及外部認知支架的命題系列。這些命題目前仍沒有 TADC 專屬原始人體實驗資料，因此下一步不應繼續增加理論，而應先回答：

> **TADC 中哪些變量真的能被穩定、獨立、可重現地量測？**

本文建立 TADC 第一份正式量測設計。整個測量系統分為六層：

$$
\boxed{
\text{Event}
\rightarrow
\text{Relation}
\rightarrow
\text{Domain}
\rightarrow
\text{Scale}
\rightarrow
\text{Operator}
\rightarrow
\text{Outcome}.
}
$$

其中 Event 為最接近直接觀察的資料；Relation、Domain、Scale 與 Operator 逐步增加模型假設。因此本文採取一個重要原則：

$$
\boxed{
\text{higher-level latent claims require lower-level measurement survival}.
}
$$

若 relational distance 無法穩定估計，則 dynamic domain 不進下一階段；若 domain 無法獨立恢復，則 domain hyperfocus、topological hyperfocus 與 cross-domain continuity 不進 confirmatory test；若 scale 無法被 participant behavior 或 independent decoding 區分，則 Re-indexing 只保留為分析工具；若 operator categories 不可辨識，則 SOCTS 六算子必須壓縮。

本文建立 **TADC Minimal Measurement Battery（TMMB）**，其核心變量包括：

$$
\boxed{
L_D,\nu_I,\nu_E,H_I,d_{\mathrm{rel}},
\Delta_{\mathrm{cross}},G_C,S_C,
K_R,K_{RE},E_C,R_C,\Gamma_R,P_R.
}
$$

並將測量分成：

### Core Battery

不需要 EEG / fMRI / persistent homology，只使用：

- controlled behavioral tasks；
- time-series logs；
- goal reports；
- relation annotations；
- interruption / re-entry tasks；
- held-out prediction。

### Advanced Topology Battery

只有 Core Battery 通過後才使用：

- representational similarity analysis；
- persistent homology；
- persistence diagrams；
- topology-sensitive model comparison；
- cross-scale invariants；
- operator-induced topology change。

現有 cognitive-map 研究已示範可用可靠的 representational structure 去直接 benchmark competing theoretical models，而非只做定性比喻。2025 年 representational topology analysis 也已將 persistent homology 引入 representational analysis，提供測量高階「形狀」結構的方法；但這些方法本身不證明 TADC。

本文最後制定 Go / Revise / Kill 規則，確保 Measurement Design 的結果可以阻止 TADC 進入不必要的 Pilot。

---

# 0. 研究狀態與邊界

目前 TADC：

- 已完成理論命題：8 篇；
- 原始 TADC 人體實驗：0；
- TADC 專屬 longitudinal validation：0；
- preregistered confirmatory study：0；
- TADC 特有拓樸不變量：0。

因此本文件不應使用：

$$
\boxed{
\text{validated theory}
}
$$

而只能使用：

$$
\boxed{
\text{measurement candidates}.
}
$$

---

# 1. Measurement Design 的第一原則：不要一次測整套 TADC

TADC 中存在明確 dependency：

$$
\boxed{
\text{Relation}
\rightarrow
\text{Domain}
\rightarrow
\text{Scale}
\rightarrow
\text{THF / Cross-domain continuity / Operators}.
}
$$

因此不能直接拿一個長期 log：

> 畫一張圖 → 找到很多 cluster → 宣稱拓樸注意力。

正確順序是：

$$
\boxed{
\text{Can we measure relations?}
}
$$

↓

$$
\boxed{
\text{Do relations recover useful domains?}
}
$$

↓

$$
\boxed{
\text{Do those domains predict switching / return?}
}
$$

↓

$$
\boxed{
\text{Is there additional multiscale / topological structure?}
}
$$

---

# 2. Measurement Dependency Graph

定義：

$$
M_R
=
\text{relational measurement}.
$$

$$
M_D
=
\text{domain inference}.
$$

$$
M_\lambda
=
\text{scale inference}.
$$

$$
M_O
=
\text{operator inference}.
$$

則：

$$
M_R
\rightarrow
M_D
\rightarrow
M_\lambda
\rightarrow
M_O.
$$

同時：

$$
M_D
\rightarrow
M_{\mathrm{DHF/THF}},
$$

$$
M_R
\rightarrow
M_{\mathrm{RFCC}},
$$

$$
M_D+M_\lambda
\rightarrow
M_{\mathrm{THF}},
$$

$$
M_R+M_D
\rightarrow
M_{\mathrm{AI-topology}}.
$$

---

# 3. 六層資料模型

## Layer E — Event

直接觀察或接近直接觀察。

## Layer R — Relation

兩事件／概念之間的關係。

## Layer D — Domain

由關係誘導的候選區域。

## Layer S — Scale

哪些 distinctions 在當前解析度被保留。

## Layer O — Operator

從狀態變化反推的操作類型。

## Layer Y — Outcome

performance、error、return、completion、cost。

---

# 4. Event Layer 是唯一可以先收再說的層

每個 event：

$$
e_i
=
(
id_i,
t_i,
s_i,
a_i,
q_i,
g_i,
y_i
).
$$

其中：

- \(id_i\)：event id；
- \(t_i\)：timestamp；
- \(s_i\)：source type；
- \(a_i\)：action；
- \(q_i\)：local context；
- \(g_i\)：declared / inferred goal；
- \(y_i\)：immediate outcome。

---

# 5. Source Type 必須先拆

至少：

$$
s_i\in
\{
H,S,A
\}.
$$

其中：

- \(H\)：Human interaction event；
- \(S\)：System / Agent event；
- \(A\)：Artifact event。

因此：

$$
\boxed{
H\neq S\neq A.
}
$$

---

# 6. Human Event

候選 human event：

- prompt / message；
- explicit task selection；
- manual file open；
- manual branch selection；
- participant button response；
- eye / focus-confirmed task engagement；
- self-report probe。

不能只用：

$$
\text{file modification time}
$$

當 human attention。

---

# 7. System Event

候選：

- agent execution；
- automatic search；
- background code run；
- scheduled generation；
- automatic summarization；
- index update。

System event 可反映：

$$
\text{hybrid system topology},
$$

但不能直接反推：

$$
\text{human attentional topology}.
$$

---

# 8. Artifact Event

候選：

- file creation；
- commit；
- ZIP release；
- paper export；
- generated code；
- validation output。

artifact 是結果層，

不是 cognition ground truth。

---

# 9. Event 最小欄位

所有研究至少記：

| 欄位 | 說明 |
|---|---|
| event_id | 唯一 ID |
| timestamp | ISO 8601 |
| actor_type | human / system / artifact |
| session_id | session |
| project_id | 外部 project label |
| task_id | task |
| subtask_id | subtask |
| action_type | action |
| goal_id | goal |
| parent_event | 前置 event |
| artifact_ref | 可選 |
| outcome | 結果 |
| confidence | 標註可信度 |

---

# 10. Human Attention Grounding

若研究 digital traces，

建議每：

$$
5\sim20
$$

分鐘插入低頻 experience-sampling probe：

1. 目前主要 goal？
2. 目前 subtopic？
3. 剛剛是否換題？
4. 換題是因為 distraction / exploration / regulation / external demand？
5. 目前是否能立即停止？

用來校準：

$$
\boxed{
\text{digital event}
\rightarrow
\text{human state}
}
$$

映射。

---

# 11. Relation Layer

TADC 最低 relational vector：

$$
\mathbf r_{ij}
=
(
r_S,
r_C,
r_A,
r_P,
r_T,
r_G,
r_K
).
$$

---

# 12. Semantic Relation \(r_S\)

測量：

- human semantic rating；
- lexical / embedding proxy；
- expert coding。

Embedding 只能：

$$
\boxed{
\text{proxy}.
}
$$

---

# 13. Causal Relation \(r_C\)

問題：

> \(x_i\) 是否被認為對 \(x_j\) 有因果、機制或 dependency 關係？

可由：

- explicit causal graph；
- formal dependency；
- expert rating；
- intervention task；

估計。

---

# 14. Analogical Relation \(r_A\)

問題：

> 兩者是否共享角色對應或 higher-order relational structure？

不能只問：

> 像不像？

應分：

$$
\text{surface similarity}
$$

與：

$$
\text{structural alignment}.
$$

---

# 15. Procedural Relation \(r_P\)

問題：

> 完成 \(x_j\) 是否需要 \(x_i\) 的 procedure / output？

特別適用：

- coding；
- mathematics；
- multi-step tasks。

---

# 16. Temporal Relation \(r_T\)

例如：

$$
x_i
\prec
x_j.
$$

但 temporal adjacency：

$$
\not\Rightarrow
$$

semantic / causal adjacency。

---

# 17. Goal Relation \(r_G\)

$$
r_G(x_i,x_j)
=
\operatorname{Sim}
(
G(x_i),
G(x_j)
).
$$

是 TADC 判斷「換題是否仍留在同一 higher-order goal」的重要變量。

---

# 18. Constraint Relation \(r_K\)

兩個 concepts 是否共享：

- boundary conditions；
- rules；
- allowed transformations；
- validity conditions。

這用來防：

$$
\boxed{
\text{false cross-domain gluing}.
}
$$

---

# 19. Relation Annotation 三級制

每條 relation 使用：

$$
r\in
\{0,1,2\}
$$

即可先做 Pilot。

- 0：無／極弱；
- 1：可能／部分；
- 2：強／明確。

另存：

$$
c_r\in[0,1]
$$

作 confidence。

先不要一開始用 0–100 精細量表。

---

# 20. Relational Distance 的兩個版本

## Graph Version

$$
d_{\mathrm{rel}}^{G}
=
\min_\gamma
\sum_{e\in\gamma}
c(e).
$$

## Statistical Version

學習：

$$
d_{\mathrm{rel}}^{M}
=
f_\theta(
\mathbf r_{ij}
)
$$

使其最佳預測：

$$
K_{\mathrm{switch}},
\text{transfer},
P_{\mathrm{return}}.
$$

兩者都保留。

---

# 21. 不先假定哪一個 relation layer 最重要

權重：

$$
\mathbf w
=
(w_S,w_C,w_A,w_P,w_T,w_G,w_K)
$$

應在 training data 學習，

再在 held-out data 評估。

confirmatory phase 前才 freeze。

---

# 22. Domain Layer

domain 不應直接等於：

- folder；
- repo；
- discipline；
- self-report category。

這些只能作：

$$
L_{\mathrm{ext}}.
$$

---

# 23. Candidate Domain

從 relational graph：

$$
\mathcal G
$$

估：

$$
\mathcal U
=
\{U_1,\ldots,U_k\}.
$$

可以比較：

- community detection；
- overlapping community；
- hierarchical clustering；
- latent-state model；
- task-defined domain。

---

# 24. Domain 不要求唯一 partition

允許：

$$
P(
x\in U_i
)
\in[0,1].
$$

因此：

$$
x
$$

可同時：

$$
x\in U_i
\cap
U_j.
$$

---

# 25. Domain Recovery 必須和 external label 分開

比較：

$$
M_{\mathrm{ext}}
$$

與：

$$
M_{\mathrm{rel-domain}}.
$$

Primary test：

$$
\boxed{
\operatorname{Pred}
(
M_{\mathrm{rel-domain}}
)
>
\operatorname{Pred}
(
M_{\mathrm{ext}}
).
}
$$

---

# 26. Domain 的主要 outcome

domain model 至少要預測一項：

- switch cost；
- return probability；
- transfer；
- memory clustering；
- task completion；
- neural similarity。

如果：

$$
U_i
$$

不預測任何 outcome，

它只是 clustering artifact。

---

# 27. Domain Retention

$$
L_D
=
\frac{
\sum_t
\mathbf1[
x_t\in U_t
]
}{
T
}.
$$

dynamic domain 時：

$$
U_t
$$

需有 correspondence mapping。

---

# 28. Domain Exit

$$
\nu_E
=
\frac{
N(
U_t\rightarrow V_t,\;
V_t\not\sim U_t
)
}{
T
}.
$$

其中：

$$
\not\sim
$$

不能只由 folder label 判斷。

---

# 29. Intra-Domain Switching

$$
\nu_I
=
\frac{
N(
x_i\rightarrow x_j,
x_i,x_j\in U
)
}{
T_U
}.
$$

---

# 30. Internal Entropy

$$
H_I
=
-\sum_i
p(x_i\mid U)\log p(x_i\mid U).
$$

---

# 31. Goal Continuity

$$
G_C
=
\frac1{T-1}
\sum_t
\operatorname{Sim}
(
G_t,G_{t+1}
).
$$

---

# 32. Structural Continuity

先採弱版：

$$
S_C
=
\alpha J_X
+
\beta J_R
+
\gamma G_C.
$$

不要第一版就塞太多 invariant。

---

# 33. Scale Layer

TADC-04 的最大風險是：

$$
\lambda
$$

可能只是分析者選擇。

所以 scale study 必須有 experimental manipulation。

---

# 34. Scale Manipulation

同一 structure：

$$
U
$$

要求 participant：

### Fine condition

處理：

$$
x_1,\ldots,x_n.
$$

### Coarse condition

把：

$$
U
$$

當一個 unit。

### Return-to-fine

再展開。

---

# 35. Re-indexing Cost

定義：

$$
K_R
=
RT_{\mathrm{switch-scale}}
-
RT_{\mathrm{same-scale}}.
$$

也可加入：

- error cost；
- neural reconfiguration；
- memory loss。

---

# 36. Scale Reality 判準

至少兩項成立：

1. instruction manipulation 改變 behavior；
2. participant grouping 符合 scale；
3. neural / representational decoding 分離；
4. cross-scale switch cost 可重現。

否則：

$$
\boxed{
\lambda
=
\text{analyst-only scale}.
}
$$

---

# 37. Operator Layer

TADC-03 六算子先不直接做六分類。

Measurement stage 採階層分類。

---

# 38. Operator Level 1

先分：

$$
\boxed{
\text{Move}
}
$$

vs

$$
\boxed{
\text{Structure Change}
}
$$

vs

$$
\boxed{
\text{Scale Change}
}
$$

---

# 39. Operator Level 2

Structure Change 再分：

- Expand；
- Contract；
- Connect；
- Disconnect。

Scale Change：

- coarse；
- fine。

Move：

- within-domain；
- across-domain。

---

# 40. 為什麼分兩層？

因為直接：

$$
\{E,C,T,G,D,R\}
$$

很可能 inter-rater reliability 低。

先確認 coarse categories 可辨識，

再升級細分類。

---

# 41. Operator Reliability

目標：

$$
\kappa_{\mathrm{rater}}
\geq
0.70
$$

作為 Pilot 建議門檻。

低於：

$$
0.60
$$

則 operator definitions 需重寫。

這是研究設計門檻，不是通用心理測量定理。

---

# 42. Hyperfocus Measurement

TADC-05 不應直接創造新問卷取代 AHQ-D。

AHQ-D 可作 trait-level external measure；其 2024 validation 以 12-item dispositional scale 測成人 hyperfocus，並將 hyperfocus 操作為 intense/deep concentration，包含 timelessness、忽略外界／個人需求、停止困難等面向。

TADC 增加的是 episode dynamics。

---

# 43. Episode Battery

每個 long-focus episode 測：

$$
\mathbf H
=
(
I,T,L_D,\nu_I,\nu_E,H_I,E_C,R_C
).
$$

其中：

- intensity；
- duration；
- domain retention；
- intra switching；
- exit switching；
- entropy；
- exit control；
- re-entry control。

---

# 44. Exit Controllability

隨機 exit cue。

測：

$$
\tau_{\mathrm{exit}}
$$

與：

$$
P_{\mathrm{exit|cue}}.
$$

---

# 45. Re-entry Controllability

退出：

$$
\Delta t
$$

後，

測：

$$
\tau_{\mathrm{reentry}}
$$

與：

$$
\text{state reconstruction accuracy}.
$$

task interruption literature 已證明 resumption 存在可測成本，因此這是可直接接到既有 paradigm 的量。TADC 的新增部分是把它和 domain / external checkpoint 結構連起來。

---

# 46. Human–AI Measurement

AI study 必須至少三層：

$$
\boxed{
H_t,S_t,A_t.
}
$$

不能只抓 Git / files。

---

# 47. Human Layer

收：

- prompt timestamp；
- active-window focus；
- explicit branch selection；
- self-report；
- manual approval；
- validation decision。

---

# 48. System Layer

收：

- agent start/end；
- tool call；
- branch execution；
- model output；
- background task；
- automatic retrieval。

---

# 49. Artifact Layer

收：

- paper；
- code；
- commit；
- release；
- validation；
- summary。

---

# 50. AI Reachability Gain

需要 matched task。

Human-only：

$$
\operatorname{Reach}_H^{T}.
$$

Human+AI：

$$
\operatorname{Reach}_+^{T}.
$$

不能用自然狀態「AI 組做了更多」直接判。

---

# 51. Reachability Precision

每個 candidate state：

$$
y_i
$$

標：

- valid；
- invalid；
- unresolved。

所以：

$$
P_R
=
\frac{
N_{\mathrm{valid}}
}{
N_{\mathrm{valid}}
+
N_{\mathrm{invalid}}
+
N_{\mathrm{unresolved}}
}.
$$

Pilot 另報：

$$
P_R^{resolved}
=
\frac{
N_{\mathrm{valid}}
}{
N_{\mathrm{valid}}
+
N_{\mathrm{invalid}}
}.
$$

避免 unresolved 被隱藏。

---

# 52. External Checkpoint Condition

比較至少三種：

### Raw

只保存完整 history。

### Structured

保存：

$$
(
goal,
state,
dependencies,
open\ questions,
next\ action
).
$$

### AI Structured + Provenance

另保存：

- source；
- confidence；
- validation state。

---

# 53. Re-entry Primary Outcome

$$
K_{RE}
=
z(RT)
+
z(error)
+
z(reconstruction\ loss).
$$

或三個分開報。

第一個 Pilot 不要硬合成單一 index。

---

# 54. Core Battery 的七個首要量

第一輪最重要：

$$
\boxed{
d_{\mathrm{rel}},
L_D,
\nu_I,
\nu_E,
G_C,
K_R,
K_{RE}.
}
$$

其他變量第二順位。

---

# 55. 為什麼先這七個？

因為它們直接決定：

- relation-first 是否值得繼續；
- domain 是否有實體測量價值；
- macro / micro 是否可測；
- re-entry topology 是否可測。

如果這七個失敗，

很多後續理論自然消失。

---

# 56. 第一個 Measurement Study：Relation Distance Calibration

## 目的

建立：

$$
d_{\mathrm{rel}}.
$$

## Participants

先用一般成人樣本。

不需要 ADHD。

---

# 57. Relation Distance Calibration Task

準備：

$$
N
$$

組 concept / task pairs。

收：

1. semantic similarity；
2. causal relation；
3. analogical alignment；
4. procedural dependency；
5. goal similarity；
6. external discipline distance。

再做：

- switching RT；
- inference accuracy；
- transfer。

---

# 58. Primary Test

比較：

$$
M_0:
K_{\mathrm{switch}}
\sim
d_{\mathrm{ext}}
+
d_{\mathrm{sem}}.
$$

與：

$$
M_1:
K_{\mathrm{switch}}
\sim
d_{\mathrm{ext}}
+
d_{\mathrm{sem}}
+
d_{\mathrm{rel}}.
$$

若：

$$
\Delta\operatorname{Pred}_{heldout}
\leq0,
$$

Relation-first 強版不進 Pilot。

---

# 59. 第二個 Measurement Study：Dynamic Domain Recovery

固定：

$$
X.
$$

操縱：

$$
G_1,G_2,G_3.
$$

例如：

- causal goal；
- semantic goal；
- action goal。

---

# 60. Primary Test

是否：

$$
\mathcal U_{G_1}
\neq
\mathcal U_{G_2}
$$

且 domain model 能預測：

$$
K_{\mathrm{switch}},
P_{\mathrm{return}},
\text{transfer}.
$$

---

# 61. Third Study：Scale / Re-indexing Feasibility

人工 hierarchy：

$$
x_{ijk}
\subset
U_{ij}
\subset
V_i.
$$

要求：

- item；
- cluster；
- meta-cluster；

三尺度判斷。

Primary：

$$
K_R>0
$$

且不同 scale 有可辨識 performance pattern。

---

# 62. Fourth Study：Interruption / Re-entry

task branch：

$$
b_1,b_2,b_3.
$$

中斷後回返。

比較：

- no checkpoint；
- raw checkpoint；
- structured checkpoint。

Primary：

$$
K_{RE}^{structured}
<
K_{RE}^{raw}
<
K_{RE}^{none}.
$$

---

# 63. Fifth Study：Long-Focus Episode Feasibility

不要一開始宣稱 THF。

只收：

$$
L_D,\nu_I,\nu_E,H_I,E_C.
$$

問：

$$
\boxed{
\text{Are high-}L_D\text{ / high-}H_I
\text{ episodes empirically observable?}
}
$$

---

# 64. TMMB Core Study Order

$$
\boxed{
R1
\rightarrow
D1
\rightarrow
S1
\rightarrow
RE1
\rightarrow
HF1.
}
$$

其中：

- R1：relation；
- D1：domain；
- S1：scale；
- RE1：re-entry；
- HF1：long-focus dynamics。

---

# 65. 不先做 Topology

Persistent homology：

$$
\boxed{
\text{not Phase-1 primary outcome}.
}
$$

先確認：

$$
\mathcal G
$$

真的和 behavior 有關。

---

# 66. Advanced Topology Battery（ATB）

只有 Core Battery 通過後啟用。

包含：

1. RSA / representational geometry；
2. persistent homology；
3. persistence diagrams；
4. topological distances；
5. topology–behavior prediction；
6. operator-induced topology change。

---

# 67. Representational Geometry Baseline

先計算 RDM：

$$
D_{ij}.
$$

比較：

- task conditions；
- participants；
- time；
- model predictions。

---

# 68. Topology Layer

對：

$$
D
$$

做 filtration。

計算：

$$
H_0,H_1
$$

優先。

第一批不急著：

$$
H_2+.
$$

避免過度複雜。

---

# 69. Primary Topology Measures

$$
\beta_0,
\beta_1,
TP_1,
H_P,
d_B.
$$

其中：

- Betti 0；
- Betti 1；
- total persistence；
- persistence entropy；
- bottleneck distance。

---

# 70. Topology Increment Test

三模型：

$$
M_G
=
\text{geometry}.
$$

$$
M_T
=
\text{topology}.
$$

$$
M_{GT}
=
\text{geometry+topology}.
$$

Primary：

$$
\boxed{
\operatorname{Pred}(M_{GT})
-
\operatorname{Pred}(M_G)
>
\delta_T.
}
$$

---

# 71. 為何這是「Topological」生死線？

2025 representational topology analysis 已展示 persistent diagrams 可以像 RSA 一樣進行 inference / comparison；因此 topology 不是不可測名詞。

但如果 TADC 的 topology-sensitive measures：

$$
\Delta\operatorname{Pred}\approx0,
$$

就應改名：

$$
\boxed{
\text{Dynamic Relational Attention}.
}
$$

---

# 72. Model Benchmark 原則

2025 Neuron cognitive-map benchmark 的核心方法是：

> 先建立可靠 representational structure，再用它直接區分 competing models。

TADC 採同樣原則：

$$
\boxed{
\text{data structure}
\rightarrow
\text{model adjudication},
}
$$

不是：

$$
\boxed{
\text{theory label}
\rightarrow
\text{select confirming graph}.
}
$$

---

# 73. Model Set

至少保留：

### M0

Fixed-space attention。

### M1

Fixed task / domain switching。

### M2

Fixed latent semantic geometry。

### M3

Learning / chunking。

### M4

Reward / flow / motivation。

### M5

Offloading / speed。

### M6

TADC dynamic relational model。

### M7

TADC topology-sensitive model。

---

# 74. Nested Model Strategy

不要一次：

$$
M0
\text{ vs }
M7.
$$

而是：

$$
M0\rightarrow M1\rightarrow M2\rightarrow M6\rightarrow M7.
$$

只有簡單模型輸了，

才加複雜度。

---

# 75. Held-out Prediction

Primary metric 應是：

$$
\boxed{
\text{out-of-sample predictive performance}.
}
$$

而不是 training：

$$
R^2.
$$

---

# 76. Cross-Validation Unit

要依資料結構選：

- trial-held-out；
- session-held-out；
- participant-held-out；
- task-held-out。

最強：

$$
\boxed{
\text{task-held-out / participant-held-out}.
}
$$

---

# 77. Generalization Ladder

Level 0：

same session。

Level 1：

new session。

Level 2：

new participant。

Level 3：

new task。

Level 4：

new population / lab。

TADC 越 general，

需要越高階 generalization。

---

# 78. Measurement Reliability Gate

候選：

### Relation ratings

ICC / inter-rater。

### Domain recovery

cluster stability / held-out prediction。

### Operator coding

Cohen/Fleiss \(\kappa\)。

### Scale

within-person repeatability。

### Re-entry

test–retest / condition reliability。

---

# 79. Gate A：Relation

如果：

$$
Rel(d_{\mathrm{rel}})<0.60
$$

或 held-out prediction 無增量：

$$
\boxed{
\text{STOP domain theory escalation}.
}
$$

---

# 80. Gate B：Domain

如果：

$$
\mathcal U
$$

對 behavior 不比 external labels 好：

$$
\boxed{
\text{STOP THF / CDCC escalation}.
}
$$

---

# 81. Gate C：Scale

如果：

$$
K_R
$$

無穩定 effect，

且 scale decoding 失敗：

$$
\boxed{
\text{Re-indexing becomes analyst tool only}.
}
$$

---

# 82. Gate D：Re-entry

若 structured state 不降低：

$$
K_{RE},
$$

則 TADC-07 RTC 失敗，

但不影響整個 TADC。

---

# 83. Gate E：Topology

若：

$$
M_{GT}
\not>
M_G,
$$

則：

$$
\boxed{
\text{rename Topological Attention}.
}
$$

---

# 84. Go / Revise / Kill

每個 construct：

### GO

- reliable；
- incremental；
- predictive；
- replicable。

### REVISE

- measurable；
- weak / unstable prediction；
- construct overlap。

### KILL

- unreliable；
- non-identifiable；
- no incremental value；
- explained by simpler model。

---

# 85. 第一階段不需要臨床樣本

原因：

TADC 的 general architecture 若只在 ADHD sample 才看得到，

需要先知道：

$$
\boxed{
\text{is it a general process or population-specific effect?}
}
$$

所以 Measurement Design 優先：

$$
\text{general adult sample}.
$$

---

# 86. ADHD 可以放哪裡？

後續 validation：

$$
\boxed{
\text{group moderation study}.
}
$$

例如比較：

$$
P(
L_D,H_I,\nu_E,K_R
\mid
ADHD
)
$$

與 controls。

但不是第一階段。

---

# 87. AHQ-D 的角色

AHQ-D 可作：

$$
\boxed{
\text{trait-level convergent measure}.
}
$$

不是 TADC ground truth。

2024 validation 顯示 AHQ-D 是 12-item dispositional hyperfocus measure，可量化成人 hyperfocus tendency。

TADC episode measures 應測：

$$
\boxed{
\text{within-episode dynamics}.
}
$$

---

# 88. Sample Size 現階段不要亂定

Measurement Design 不先寫：

$$
N=30
$$

或：

$$
N=100.
$$

先做：

$$
\boxed{
\text{simulation / pilot effect-size estimation}.
}
$$

之後 preregistered study 再 power analysis / precision planning。

---

# 89. Pilot 的樣本目標

Pilot 目標不是 hypothesis significance，

而是：

- task works；
- measure variance exists；
- reliability；
- effect direction；
- model identifiability；
- data loss。

所以：

$$
\boxed{
\text{Pilot success}
\neq
p<0.05.
}
$$

---

# 90. Preregistration 還不是現在

Measurement Design 完成後：

$$
\boxed{
\text{Pilot Protocol}
}
$$

先跑。

Pilot 會改：

- thresholds；
- relation coding；
- task timing；
- scale levels。

這些尚未 freeze。

---

# 91. Confirmatory 前必須 freeze

preregistration 前鎖：

- primary hypotheses；
- measures；
- inclusion；
- preprocessing；
- model set；
- hyperparameters；
- cross-validation；
- success threshold；
- falsification rule。

現有 cognitive-model preregistration template 已明確強調 model development、application、evaluation 與 comparison 的透明分離；TADC 應照這個精神做。

---

# 92. Data Versioning

每次：

$$
schema^{v0.1}
\rightarrow
schema^{v0.2}
$$

要有 changelog。

不能用新 schema 回頭改 old pilot 再當 confirmatory。

---

# 93. Relation Ontology Versioning

關係類型：

$$
\mathcal R^{v0.1}
$$

若新增：

$$
r_{\mathrm{spatial}},
$$

就變：

$$
\mathcal R^{v0.2}.
$$

模型結果必須記 ontology version。

---

# 94. Blind Annotation

relation / operator annotation 若知道 outcome，

容易 bias。

至少一部分：

$$
\boxed{
\text{blind to condition / outcome}.
}
$$

---

# 95. Gold / Silver Labels

Gold：

- formal dependency；
- task-generated ground truth；
- expert consensus。

Silver：

- LLM + human review；
- participant self-report；
- heuristic relation。

分析分開。

---

# 96. Unresolved 是合法標籤

不能逼：

$$
\text{valid/invalid}.
$$

使用：

$$
\boxed{
\text{unresolved}.
}
$$

尤其 AI research branch。

---

# 97. N=1 Longitudinal Extension

等 Core Battery 有可用 measurement 後，

可以做：

$$
\boxed{
N=1\text{ dense longitudinal study}.
}
$$

但不是先拿 N=1 定義變量。

---

# 98. N=1 Data Required

至少：

- 30+ sessions；
- repeated interruption / return；
- multiple projects；
- human event markers；
- relation graph；
- outcomes。

這只是 practical candidate minimum，不是統計定理。

---

# 99. N=1 Primary Questions

不是：

> 這個人有沒有 THF？

而是：

1. \(L_D\) 和 \(H_I\) 可否同時高？
2. \(d_{\mathrm{rel}}\) 是否預測 switching？
3. \(K_{RE}\) 是否被 structured state 降低？
4. micro-switching 和 long-horizon completion 的關係？

---

# 100. Research Output 不等於 Attention Measure

論文數：

$$
N_P
$$

可作 outcome。

不能作：

$$
L_D
$$

的直接替代。

---

# 101. Productivity Outcome

建議：

$$
O_P
=
(
N_{\mathrm{completed}},
N_{\mathrm{validated}},
P_{\mathrm{return}},
P_{\mathrm{abandoned}},
T_{\mathrm{completion}}
).
$$

比單純 file count 好。

---

# 102. Human–AI Outcome

加：

$$
O_{HA}
=
(
\Gamma_R,
P_R,
K_V,
K_C,
\Gamma_I
).
$$

---

# 103. 注意「高產」可能來自 Agent

因此：

$$
\boxed{
\text{system productivity}
\neq
\text{human cognitive capacity}.
}
$$

永遠分層報。

---

# 104. TADC Measurement Dashboard

未來工具可顯示：

- current domain；
- branch graph；
- \(L_D\)；
- \(\nu_I/\nu_E\)；
- \(K_{RE}\)；
- goal continuity；
- unresolved bridges；
- human/system event ratio。

但 dashboard 不是實驗證據。

---

# 105. 第一個真正應寫程式的東西

不是 TDA。

而是：

$$
\boxed{
\text{event logger + relation annotator + branch checkpoint}.
}
$$

先收對資料。

---

# 106. 最小資料格式

一列 event：

```text
event_id
timestamp
actor_type
session_id
project_id
task_id
subtask_id
goal_id
action_type
parent_event
previous_human_event
external_label
outcome
confidence
```

另表 relation：

```text
source_event
target_event
semantic
causal
analogical
procedural
temporal
goal
constraint
confidence
annotator
```

---

# 107. 為什麼 event / relation 分表？

避免：

$$
O(N^2)
$$

relation columns 塞進 event table。

也方便 relation graph versioning。

---

# 108. Checkpoint Table

```text
checkpoint_id
branch_id
timestamp
goal
current_state
dependencies
open_questions
next_action
provenance
verification_state
```

直接對應：

$$
K_{RE}.
$$

---

# 109. Pilot Dataset 的最低輸出

Pilot 結束必須能輸出：

1. `events.csv`
2. `relations.csv`
3. `checkpoints.csv`
4. `domains.json`
5. `analysis_config.json`
6. `validation_report.md`

---

# 110. Measurement Report 必須報失敗

例如：

- 42% operator 無法分類；
- relation ICC 只有 0.41；
- domain model 不穩；
- AI events 與 human events 難分。

這些就是 Measurement Design 的重要成果。

---

# 111. 什麼叫 Measurement Design 成功？

不是 TADC 被支持。

而是：

$$
\boxed{
\text{we know which constructs can and cannot be measured}.
}
$$

---

# 112. Measurement Design Go Criteria

進 Pilot Protocol 前，文件層需至少完成：

- data schema；
- codebook；
- relation rubric；
- domain inference plan；
- scale manipulation；
- primary outcomes；
- null models；
- kill rules。

本文件已完成 framework，

下一份 Pilot Protocol 要把它變成實際 task。

---

# 113. 第一個 Pilot 應該選哪一條？

建議不是 Hyperfocus。

最乾淨的是：

$$
\boxed{
\textbf{Relational Distance × External Domain Distance Crossover}
}
$$

因為：

- 時間短；
- 不需長期追蹤；
- 不需 AI；
- 不需 neuroimaging；
- 直接打 TADC-06 的地基；
- 若失敗，可快速縮減整套 theory。

---

# 114. Pilot 1 核心 2×2

| | Relationally Near | Relationally Far |
|---|---:|---:|
| Same External Domain | SN | SF |
| Cross External Domain | CN | CF |

---

# 115. TADC 的關鍵預測

$$
\boxed{
K_{CN}
<
K_{SF}
}
$$

即：

> 跨外部領域但關係近，比同領域但關係遠更容易轉換。

這如果完全看不到，

Relation-First Cognition 會受到直接打擊。

---

# 116. Pilot 1 Primary Outcomes

- switch RT；
- accuracy；
- novel inference；
- transfer confidence；
- optional neural measure later。

---

# 117. Pilot 1 Primary Null

$$
M_0:
K
=
f(
d_{\mathrm{ext}},
d_{\mathrm{sem}},
familiarity
).
$$

TADC model：

$$
M_1:
K
=
M_0
+
f(
d_{\mathrm{rel}}
).
$$

---

# 118. Measurement Design 的正式停止點

本文到此停止。

不再：

- 加新 TADC constructs；
- 加新 operators；
- 加新 topology 名詞。

下一步只做：

$$
\boxed{
\text{Pilot Protocol 01}.
}
$$

---

# 119. 結論

TADC 第二階段的第一個問題不是：

> 拓樸注意力是真的嗎？

而是：

> **我們是否有一組足夠乾淨的觀察量，讓這個問題可以被資料回答？**

本文因此把整套 TADC 壓成六層：

$$
\boxed{
E
\rightarrow
R
\rightarrow
D
\rightarrow
S
\rightarrow
O
\rightarrow
Y.
}
$$

並建立最小 Core Battery：

$$
\boxed{
d_{\mathrm{rel}},
L_D,
\nu_I,
\nu_E,
G_C,
K_R,
K_{RE}.
}
$$

如果這些核心量：

- 不可靠；
- 不可辨識；
- 無 held-out prediction；
- 被更簡單變量完全吸收；

就不應進更高階 topology analysis。

只有 Core Battery 存活後，

才開：

$$
\boxed{
\text{Advanced Topology Battery}.
}
$$

使用：

- RSA；
- RTA；
- persistent homology；
- topology-sensitive model comparison。

TADC 的量測哲學因此是：

$$
\boxed{
\text{Behavior first}
\rightarrow
\text{Relation}
\rightarrow
\text{Geometry}
\rightarrow
\text{Topology}.
}
$$

而不是：

$$
\boxed{
\text{Topology first}
\rightarrow
\text{find a graph that looks convincing}.
}
$$

第一個正式 Pilot 建議鎖定：

$$
\boxed{
\text{Relational Distance × External Domain Distance Crossover}.
}
$$

它是整套 TADC 最便宜、最乾淨，也最可能快速證明我們錯了的第一刀。

如果這一刀砍下去，結果是：

$$
K_{CN}
\not<
K_{SF},
$$

並且：

$$
d_{\mathrm{rel}}
$$

對 held-out switching performance 沒有增量，

那麼 RFCC 必須收縮，

後面大量「領域就是關係空間」的強敘述也一起收縮。

反之，

如果：

$$
K_{CN}
<
K_{SF}
$$

穩定出現，

而且：

$$
d_{\mathrm{rel}}
$$

能跨 item、participant、task generalize，

那我們才真正取得第一塊屬於 TADC 自己的實證地基。

---

# 參考文獻

1. Lee JQ, Keinath AT, Cianfarano E, Brandon MP. **Identifying representational structure in CA1 to benchmark theoretical models of cognitive mapping.** *Neuron*. 2025;113(2):307–320.e5. doi:10.1016/j.neuron.2024.10.027. PMID: 39579760.  
2. Brown S, Farivar R. **The topology of representational geometry.** *Frontiers in Neuroscience*. 2025;19:1597899. doi:10.3389/fnins.2025.1597899.  
3. Crüwell S, Evans NJ. **Preregistration in diverse contexts: a preregistration template for the application of cognitive models.** *Royal Society Open Science*. 2021;8:210155. doi:10.1098/rsos.210155.  
4. Leach SC, Chen X, Hwang K. **Hierarchical Reconfiguration of Neurocognitive Task Set Representations Mediates Cognitive Flexibility.** *Journal of Neuroscience*. 2026. doi:10.1523/JNEUROSCI.0113-26.2026. PMID: 42276789.  
5. Hirsch P, Moretti L, Askin S, Koch I. **Examining the cognitive processes underlying resumption costs in task-interruption contexts: Decay or inhibition of suspended task goals?** *Memory & Cognition*. 2024;52(2):271–284. doi:10.3758/s13421-023-01458-8. PMID: 37674056.  
6. Hupfeld KE, Osborne JB, Tran QT, Hyatt HW, Abagis TR, Shah P. **Validation of the dispositional adult hyperfocus questionnaire (AHQ-D).** *Scientific Reports*. 2024;14:19460. doi:10.1038/s41598-024-70028-y. PMID: 39169147.  
7. Burnett LK, Richmond LL. **Meta-analytic investigations of the effect of cognitive offloading on memory-based task performance and interindividual variability.** *Memory & Cognition*. 2026;54(1):144–168. doi:10.3758/s13421-025-01743-8. PMID: 40500483.  
8. Murphy DH, Metcalfe J. **The Metacognitive Optimization of Offloading Task (MOOT): Both higher costs to offload and the accuracy of memory predict goodness of offloading performance.** *Journal of Experimental Psychology: General*. 2025;154(4):1149–1166. doi:10.1037/xge0001726. PMID: 39847000.  

---

## 下一步

**TADC-PP-01：Relational Distance × External Domain Distance Crossover — Pilot Protocol**

目標：

$$
\boxed{
\text{first direct empirical attack on RFCC}.
}
$$

---

**狀態：** TADC-MD-01 v0.1  
**階段：** Measurement Design  
**原始 TADC 人體資料：** 無  
**目前功能：** 固定量測語言、data schema、dependency、Go/Revise/Kill gate  
**下一階段：** Pilot Protocol  
