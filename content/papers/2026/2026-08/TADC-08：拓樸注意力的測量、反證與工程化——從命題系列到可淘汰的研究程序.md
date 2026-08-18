# TADC-08：拓樸注意力的測量、反證與工程化——從命題系列到可淘汰的研究程序

**英文題名：** Measuring, Falsifying, and Engineering Topological Attention: From Conjecture Series to an Eliminative Research Program  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-08  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 測量框架／反證協議／模型比較／工程化研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

TADC-01 至 TADC-07 依序提出：可變認知空間、動態認知域、六算子、多尺度重索引、拓樸超專注、關係優先跨域連續性，以及外部認知支架與人—AI 混合認知拓樸。至此，系列已形成一套高度可展開的理論語言。

然而，一個理論如果只會增加名詞、重新描述既有現象，卻沒有明確方法證明自己是多餘的，那它不是完成，而是失控。

因此 TADC-08 的任務不是再提出第九個概念，而是建立：

$$
\boxed{
\text{Measurement}
\rightarrow
\text{Model Competition}
\rightarrow
\text{Falsification}
\rightarrow
\text{Engineering}.
}
$$

本文提出一個四層測量框架：

1. **Event Layer**：可觀察的認知／行為事件；
2. **Relational Layer**：事件之間的語義、因果、類比、程序、目標與控制關係；
3. **Domain / Scale Layer**：由關係與解析度誘導出的有效 domain、嵌套結構與 coarse-graining；
4. **Dynamic Operator Layer**：Expansion、Contraction、Traversal、Gluing、Detachment、Re-indexing 的候選狀態轉換。

本文將 TADC 的主要變量整理為可測向量：

$$
\boxed{
\mathbf Z_t
=
(
L_D,
\nu_I,
\nu_E,
H_I,
S_C,
G_C,
d_{\mathrm{rel}},
\Delta_{\mathrm{cross}},
K_R,
K_{RE},
\Gamma_R,
P_R,
\lambda,
\mathbf O
).
}
$$

並提出 **TADC Minimal Measurement Battery（TMMB）**，要求至少同時測量：狀態序列、domain retention、intra-domain / exit switching、relational distance、goal continuity、re-entry cost 與 outcome。只有取得這一層資料後，才應進一步聲稱 dynamic domains、topological hyperfocus 或 human–AI topology。

本文進一步提出七類競爭模型：Fixed-Space Selection、Fixed-Domain Partition、Fixed Latent Geometry、Ordinary Task Switching、Reward / Flow、Learning / Chunking、Speed / Offloading，以及 TADC Dynamic-Topology Model。所有核心分析應進行 out-of-sample model comparison，而不是僅靠 post-hoc fit。

對真正的「拓樸」主張，本文設定更高門檻。除了 graph / geometry 指標外，必須至少嘗試測量：

- connected components；
- cycles / loops；
- persistent homology；
- bridge persistence；
- scale-stable invariants；
- topology-sensitive representational similarity；
- operator-induced topology change。

如果 topology-sensitive measures 對行為、神經表示或模型區分沒有增量預測，則 TADC 應將「Topological」降級為「Dynamic Relational」。

本文提出分階段研究程序：

$$
\boxed{
M0\rightarrow M1\rightarrow P1\rightarrow P2\rightarrow V1\rightarrow E1
}
$$

其中：

- \(M0\)：measurement feasibility；
- \(M1\)：measurement reliability；
- \(P1\)：pilot hypothesis testing；
- \(P2\)：preregistered confirmatory testing；
- \(V1\)：cross-sample / cross-task validation；
- \(E1\)：engineering intervention。

此外，本文制定整個系列的**總淘汰條件**。若下列結果穩定成立：

1. fixed-space / fixed-hierarchy models 與 TADC 預測力相同；
2. relational distance 不優於 semantic similarity / familiarity；
3. domain boundaries 無法被 participant behavior 或 neural data 獨立恢復；
4. operator categories 不可辨識；
5. topology-sensitive descriptors 沒有增量預測；
6. multiscale invariants 不存在；
7. AI scaffold effect 可被單純 speed / memory capacity 解釋；

則 TADC 強版本必須被放棄。

本文最後提出「認知拓樸工程」的安全版本：不以最大化 hyperfocus、branch count 或 AI throughput 為目標，而以：

$$
\boxed{
\text{valid reachability}
+
\text{low re-entry cost}
+
\text{high verification precision}
+
\text{controllable exit}
+
\text{preserved internalization}
}
$$

作為多目標優化。

因此 TADC-08 將整個系列從一套命題語言轉換為一個可以被失敗結果縮減、重命名乃至淘汰的研究程序。

**關鍵詞：** topological attention；measurement；falsification；preregistration；model comparison；representational similarity analysis；persistent homology；cognitive maps；human–AI cognition；attention engineering；TADC

---

# 0. 邊界聲明

本文不是：

- 臨床研究；
- ADHD 診斷框架；
- 醫療建議；
- 神經疾病理論；
- 已驗證的認知拓樸定理；
- 已完成的人—AI 增強技術標準。

TADC 全系列目前都是：

$$
\boxed{
\text{conjecture-driven research program}.
}
$$

截至本文：

$$
\boxed{
\text{no original human experimental dataset
has been collected for TADC}.
}
$$

因此任何：

$$
\text{theory confirmed}
$$

或：

$$
\text{human cognition is topological}
$$

的說法都超出本文證據。

---

# 1. 為什麼第八篇不能再增加理論自由度？

前七篇已經引入：

- cognitive space；
- domains；
- charts；
- neighborhoods；
- six operators；
- scales；
- hyperfocus states；
- relational distances；
- hybrid cognitive systems。

每增加一個自由度：

$$
D_f\uparrow,
$$

理論就更容易：

$$
\boxed{
\text{fit almost anything post hoc}.
}
$$

因此：

$$
\boxed{
\text{TADC-08 must reduce degrees of freedom,
not increase them}.
}
$$

---

# 2. 理論的最低要求

一套 TADC 模型至少必須回答：

1. 哪些變量可觀察？
2. 哪些變量是 latent？
3. 如何從資料估計 latent structure？
4. 哪些競爭模型可以產生相同現象？
5. 什麼資料會支持 TADC？
6. 什麼資料會反駁 TADC？
7. 如何防止 researcher degrees of freedom？
8. 如何在新資料上驗證？

---

# 3. 四層測量架構

定義：

$$
\boxed{
\mathfrak M
=
(
\mathcal E,
\mathcal R,
\mathcal D,
\mathcal O
).
}
$$

其中：

- \(\mathcal E\)：Event Layer；
- \(\mathcal R\)：Relational Layer；
- \(\mathcal D\)：Domain / Scale Layer；
- \(\mathcal O\)：Operator Layer。

---

# 4. Layer 1：Event Layer

最小事件：

$$
e_i
=
(
t_i,
a_i,
q_i,
y_i
).
$$

其中：

- \(t_i\)：timestamp；
- \(a_i\)：observable action；
- \(q_i\)：context / query；
- \(y_i\)：outcome。

可能資料源：

- controlled task trial；
- keyboard / mouse logs；
- application focus；
- eye tracking；
- experience sampling；
- verbal protocol；
- neural recording；
- AI interaction log；
- file / branch event。

---

# 5. Event 不等於 Cognition

必須保留：

$$
\boxed{
e_i^{\mathrm{artifact}}
\neq
e_i^{\mathrm{system}}
\neq
e_i^{\mathrm{human}}.
}
$$

例如 agent 自動 commit：

$$
\not\Rightarrow
$$

human attentional switch。

這是所有 digital-trace study 的基本防錯層。

---

# 6. Layer 2：Relational Layer

對事件或 cognitive objects：

$$
x_i,x_j
$$

建立 multiplex relations：

$$
R_{ij}
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

分別：

- semantic；
- causal；
- analogical；
- procedural；
- temporal；
- goal；
- control / constraint。

---

# 7. Relational Weights 不能只有 LLM Embedding

語義 embedding：

$$
d_{\mathrm{emb}}
$$

只能提供：

$$
r_S
$$

的候選 proxy。

至少需要：

- human ratings；
- task-defined ground truth；
- expert coding；
- causal graph；
- formal dependency；
- behavioral transition；
- model-derived similarity；

中的部分獨立證據。

所以：

$$
\boxed{
d_{\mathrm{emb}}
\neq
d_{\mathrm{rel}}.
}
$$

---

# 8. Layer 3：Domain / Scale Layer

根據：

$$
\mathcal R_t,
G_t,
\lambda_t
$$

推估：

$$
\mathcal U_t
=
\{U_{\alpha,t}\}.
$$

測：

- community / cluster structure；
- overlap；
- nested organization；
- domain boundaries；
- bridge nodes；
- scale hierarchy。

---

# 9. Domain 必須可以被獨立恢復

如果研究者先決定：

> 這些就是一個 domain。

再用同一分類證明 domain 存在，

是 circular。

所以需要：

$$
\boxed{
\text{independent domain recovery}.
}
$$

例如：

- unsupervised behavioral clustering；
- held-out transition prediction；
- neural representational geometry；
- participant self-grouping；
- cross-task replication。

---

# 10. Layer 4：Operator Layer

從：

$$
\mathcal C_t
\rightarrow
\mathcal C_{t+1}
$$

反推：

$$
O_t\in
\{E,C,T,G,D,R\}.
$$

但不能硬編碼。

需要：

$$
P(
O_t
\mid
Y_{t-k:t+k}
).
$$

---

# 11. Operator Identification 必須容許 Unknown

如果資料不支持：

$$
E,C,T,G,D,R
$$

任何一類，

必須允許：

$$
\boxed{
O_t=\mathrm{Unknown}.
}
$$

否則模型會把所有變化強行塞進六算子。

---

# 12. TADC Minimal Measurement Battery（TMMB）

任何第一次測 TADC 的 study，

至少應包含：

1. state / topic sequence；
2. timestamp；
3. goal label；
4. transition type；
5. relational distance；
6. external category distance；
7. domain-retention estimate；
8. intra-domain switching；
9. domain-exit switching；
10. performance outcome；
11. exit / re-entry measure。

---

# 13. 最小狀態向量

定義：

$$
\boxed{
\mathbf Z_t
=
(
L_D,
\nu_I,
\nu_E,
H_I,
S_C,
G_C,
d_{\mathrm{rel}},
\Delta_{\mathrm{cross}},
K_R,
K_{RE},
\Gamma_R,
P_R,
\lambda,
\mathbf O
).
}
$$

---

# 14. Domain Retention

$$
L_D(T)
=
\frac{1}{T}
\int_0^T
\mathbf 1[
x_t\in U_t
]dt.
$$

若 domain dynamic，

需要 correspondence：

$$
M_t:
U_t\rightsquigarrow U_{t+1}.
$$

---

# 15. Intra-Domain Switching

$$
\nu_I
=
\frac{
N(
x_t\rightarrow x_{t+1};
x_t,x_{t+1}\in U
)
}{
T_U
}.
$$

---

# 16. Exit Switching

$$
\nu_E
=
\frac{
N(
x_t\in U,
x_{t+1}\notin U
)
}{
T_U
}.
$$

---

# 17. Internal Entropy

$$
H_I
=
-\sum_i
p(x_i\mid U)
\log
p(x_i\mid U).
$$

---

# 18. Structural Continuity

候選：

$$
S_C
=
\alpha J_X
+
\beta J_R
+
\gamma I_G
+
\delta I_B.
$$

其中：

- node overlap；
- relation overlap；
- goal identity；
- bridge / invariant preservation。

---

# 19. Goal Continuity

$$
G_C
=
\frac1T
\sum_t
\operatorname{Sim}(G_t,G_{t+1}).
$$

---

# 20. Relational Distance

$$
d_{\mathrm{rel}}(x,y\mid G)
=
\min_{\gamma:x\leadsto y}
\sum_{e\in\gamma}
c(e\mid G).
$$

---

# 21. Cross-Domain Gap

$$
\Delta_{\mathrm{cross}}
=
\widehat d_{\mathrm{ext}}
-
\widehat d_{\mathrm{rel}}.
$$

---

# 22. Re-indexing Cost

$$
K_R
=
K(
\lambda_i
\rightarrow
\lambda_j
).
$$

---

# 23. Re-entry Cost

$$
K_{RE}
=
K_{\mathrm{locate}}
+
K_{\mathrm{retrieve}}
+
K_{\mathrm{reconstruct}}
+
K_{\mathrm{verify}}
+
K_{\mathrm{resume}}.
$$

---

# 24. Hybrid Reachability Gain

$$
\Gamma_R
=
\frac{
|\operatorname{Reach}_+|
-
|\operatorname{Reach}_H|
}{
|\operatorname{Reach}_H|
}.
$$

---

# 25. Reachability Precision

$$
P_R
=
\frac{
|\operatorname{Reach}_{valid}|
}{
|\operatorname{Reach}_{all}|
}.
$$

---

# 26. Observation Scale

$$
\lambda_t
$$

不能只由研究者指定。

需要：

- participant choice；
- task manipulation；
- behavioral model；
- neural decoding；

至少一項獨立支持。

---

# 27. Operator Profile

$$
\mathbf O_t
=
(
p_E,p_C,p_T,p_G,p_D,p_R,p_U
).
$$

其中：

$$
p_U
$$

是 Unknown probability。

---

# 28. Measurement Reliability

每個量：

$$
Z_i
$$

至少應估：

- test–retest；
- inter-rater；
- split-half；
- cross-session；
- cross-task reliability。

若：

$$
Rel(Z_i)\approx0,
$$

則該變量不應進入高階理論比較。

---

# 29. Measurement Validity

至少區分：

### Convergent validity

不同 measurement channels 是否一致？

### Discriminant validity

是否真的和已有 construct 不同？

### Predictive validity

是否預測未來 behavior？

### Incremental validity

是否超越簡單模型？

---

# 30. 「拓樸」需要更高門檻

Graph 有：

$$
\text{nodes + edges}.
$$

不等於已經需要 topology。

因此 TADC 若保留 Topological 名稱，

必須進一步測：

$$
\boxed{
\text{shape / connectivity / holes / persistence / invariants}.
}
$$

---

# 31. 2025 Representational Topology Analysis

Brown 與 Farivar（2025）提出 representational topology analysis（RTA），使用 topological data analysis 與 persistence diagrams 補充傳統 RSA。

其核心意義是：

$$
\boxed{
\text{two representational spaces can differ
in higher-order shape even when pairwise analyses are limited}.
}
$$

這提供 TADC 一條真正可操作的拓樸測量路線。

但 RTA 是 neural representational analysis 方法，

不是 TADC 的證明。

---

# 32. Persistent Homology

對 point cloud / distance matrix：

$$
X
$$

建立 filtration：

$$
\mathcal K_\epsilon.
$$

隨：

$$
\epsilon\uparrow,
$$

追蹤：

- \(H_0\)：connected components；
- \(H_1\)：loops；
- \(H_2\)：voids。

每個 feature 有：

$$
(b_i,d_i)
$$

birth / death。

persistence：

$$
p_i=d_i-b_i.
$$

---

# 33. TADC 的候選拓樸指標

### Component count

$$
\beta_0.
$$

### Loop count

$$
\beta_1.
$$

### Persistence entropy

$$
H_P.
$$

### Total persistence

$$
TP_k
=
\sum_i
(d_i-b_i)^k.
$$

### Bottleneck / Wasserstein distance

比較：

$$
PD_t
$$

與：

$$
PD_{t+1}.
$$

---

# 34. Operator-induced Topology Change

若：

$$
O_t
$$

前後：

$$
PD_t
\neq
PD_{t+1},
$$

可定義：

$$
\Delta_{\mathrm{topo}}(O_t)
=
d_B(
PD_t,
PD_{t+1}
).
$$

這才是真正接近：

$$
\boxed{
\text{operator changes topology}.
}
$$

---

# 35. 但 Persistent Homology 也不能被濫用

如果：

$$
\Delta_{\mathrm{topo}}>0
$$

只是：

- noise；
- sample size；
- metric choice；
- threshold；
- embedding artifact；

造成，

沒有認知意義。

所以必須：

- permutation control；
- bootstrap；
- matched density；
- sensitivity analysis；
- held-out behavior prediction。

---

# 36. Topology Must Earn Incremental Validity

比較：

$$
M_G
=
\text{geometry-only},
$$

$$
M_T
=
\text{topology-only},
$$

$$
M_{GT}
=
\text{geometry + topology}.
$$

TADC 強版本至少要求：

$$
\boxed{
\operatorname{Pred}(M_{GT})
>
\operatorname{Pred}(M_G)
}
$$

在部分核心 task 上成立。

---

# 37. 2025 Cognitive-Map Benchmark 的方法論意義

Lee 等人（2025）建立 framework，

把 competing cognitive-map models 的 prediction 和實際 CA1 representational dynamics 直接比較。

其重要點不是某個特定 hippocampal 結果，

而是：

$$
\boxed{
\text{qualitative map metaphors
can be converted into quantitative model adjudication}.
}
$$

TADC 應採同樣精神。

---

# 38. 七個主要競爭模型

## M0 — Fixed-Space Selection

$$
X,\mathcal R
$$

固定，

只改 attention weight：

$$
\mathbf w_t.
$$

---

## M1 — Fixed-Domain Partition

$$
\Pi
=
\{D_1,\ldots,D_n\}
$$

固定，

只在 domains 間 switching。

---

## M2 — Fixed Latent Geometry

存在固定：

$$
Z.
$$

goal 只改 readout：

$$
f_G.
$$

---

## M3 — Ordinary Task Switching

所有 transition cost 由：

- task-set reconfiguration；
- inhibition；
- working memory；

解釋。

---

## M4 — Reward / Flow / Motivation

長 dwell 與 switching pattern 由：

$$
V(x),
\text{flow},
\text{motivation}
$$

解釋。

---

## M5 — Learning / Chunking / Schema

所有：

- Expansion；
- Gluing；
- Re-indexing；

都由既有 learning theory 解釋。

---

## M6 — Speed / Offloading

AI / external scaffold 只降低：

- lookup；
- memory load；
- response time。

不改 graph structure。

---

## M7 — TADC Dynamic-Topology Model

$$
\mathcal C_t
\rightarrow
\mathcal C_{t+1}
$$

且：

$$
\mathfrak A_t,
\lambda_t,
\mathcal O_t
$$

可動態改變。

---

# 39. 模型比較不能只看 in-sample fit

複雜模型：

$$
M_7
$$

幾乎必然：

$$
\text{training fit}\uparrow.
$$

所以必須使用：

- held-out prediction；
- cross-validation；
- information criteria；
- posterior predictive checks；
- preregistered benchmark；
- cross-dataset validation。

---

# 40. 最低 model-comparison 標準

至少：

$$
\Delta
\operatorname{Pred}_{heldout}
>
0.
$$

不能只：

$$
R^2_{train}\uparrow.
$$

---

# 41. Model Complexity Penalty

若：

$$
M_7
$$

只比：

$$
M_2
$$

提高：

$$
\epsilon
$$

預測，

但參數增加：

$$
100\times,
$$

則：

$$
\boxed{
\text{TADC loses by parsimony}.
}
$$

---

# 42. 預註冊為什麼必要？

TADC 有大量：

- threshold；
- graph metric；
- scale；
- relation weight；
- domain clustering；
- operator labeling；

自由度。

若不預註冊，

很容易：

$$
\boxed{
\text{choose the topology after seeing the answer}.
}
$$

---

# 43. Cognitive-Model Preregistration

現有 cognitive-model preregistration literature 已指出：

model development、model application、model evaluation、model comparison 應分開處理。

TADC 應明確區分：

$$
\boxed{
\text{exploratory model development}
}
$$

與：

$$
\boxed{
\text{confirmatory model comparison}.
}
$$

---

# 44. EEG / ERP Preregistration 的警告

2025 Registered Report 對 EEG / ERP preregistration practices 的分析顯示：

即使研究已 preregister，

accessibility、adherence、transparency 與 selection bias 仍需實際檢查。

所以：

$$
\boxed{
\text{preregistered}
\neq
\text{automatically confirmatory}.
}
$$

TADC 的 preregistration 必須包含 deviation log。

---

# 45. TADC Preregistration Template

每個 confirmatory study 應預先寫：

1. hypotheses；
2. sample size；
3. exclusion；
4. task；
5. event definition；
6. relation coding；
7. domain inference method；
8. scale grid；
9. operator classifier；
10. primary outcome；
11. competing models；
12. model-comparison criterion；
13. falsification threshold；
14. missing data；
15. robustness analysis；
16. exploratory analyses；
17. deviation policy。

---

# 46. Hypothesis 必須可失敗

不能寫：

> TADC 預測 cognition 具有某些 dynamic patterns。

要寫：

$$
H_1:
\operatorname{Pred}(M_7)
-
\operatorname{Pred}(M_2)
>
\delta.
$$

其中：

$$
\delta
$$

預先設定 minimal effect。

---

# 47. 不使用「任何顯著差異都算成功」

若 primary hypothesis 是：

$$
d_{\mathrm{rel}}
$$

比：

$$
d_{\mathrm{ext}}
$$

更好，

就不能事後因：

$$
H_I
$$

顯著而宣稱整篇支持 TADC。

需要：

$$
\boxed{
\text{claim-specific success criteria}.
}
$$

---

# 48. TADC Research Ladder

本文提出：

$$
\boxed{
M0\rightarrow M1\rightarrow P1\rightarrow P2\rightarrow V1\rightarrow E1.
}
$$

---

# 49. M0 — Measurement Feasibility

目的：

$$
\boxed{
\text{Can the variables be estimated at all?}
}
$$

不做強理論宣稱。

檢查：

- logs；
- coding；
- graph construction；
- missingness；
- task feasibility。

---

# 50. M1 — Measurement Reliability

回答：

$$
\boxed{
\text{Are estimates stable?}
}
$$

如：

- \(d_{\mathrm{rel}}\)；
- \(L_D\)；
- \(S_C\)；
- \(K_{RE}\)；
- operator classification。

---

# 51. P1 — Exploratory Pilot

用小樣本尋找：

- parameter ranges；
- likely effect size；
- failure modes；
- model identifiability。

不能拿 P1 當 confirmatory proof。

---

# 52. P2 — Preregistered Confirmatory Study

鎖定：

- primary hypotheses；
- thresholds；
- model set；
- metrics；
- stopping rule。

---

# 53. V1 — Validation

至少一種：

- new sample；
- new task；
- new modality；
- new lab；
- new population。

若只在單 task 成立，

應限制 theory scope。

---

# 54. E1 — Engineering Intervention

只有前面通過，

才開始問：

> 是否能刻意改變 TADC variables 以改善 outcome？

這時才叫：

$$
\boxed{
\text{attention engineering}.
}
$$

---

# 55. 第一個推薦實驗：Relational Distance Benchmark

最乾淨。

四組：

1. same-domain / relation-near；
2. same-domain / relation-far；
3. cross-domain / relation-near；
4. cross-domain / relation-far。

Primary outcome：

$$
K_{\mathrm{switch}}.
$$

Primary model comparison：

$$
M_{\mathrm{taxonomy}}
$$

vs

$$
M_{\mathrm{relational}}.
$$

---

# 56. 第二個推薦實驗：Dynamic Domain Benchmark

固定 object set：

$$
X.
$$

改 goal：

$$
G_1,G_2,G_3.
$$

測 domain clustering：

$$
\mathcal U^{(1)},
\mathcal U^{(2)},
\mathcal U^{(3)}.
$$

Primary question：

$$
\boxed{
\text{Does goal-dependent domain inference
outperform fixed partition?}
}
$$

---

# 57. 第三個推薦實驗：Hyperfocus Dynamics

長時間 task：

$$
T.
$$

測：

$$
L_D,
\nu_I,
\nu_E,
H_I,
E_C.
$$

Primary test：

$$
\boxed{
L_D\uparrow
\land
H_I\uparrow
}
$$

是否存在且具功能意義。

---

# 58. 第四個推薦實驗：Re-indexing

同 hierarchy：

$$
U_i
$$

在不同 blocks：

- object-level；
- domain-level；
- meta-domain-level。

Primary outcome：

$$
K_R.
$$

測：

$$
R^-
$$

與：

$$
R^+.
$$

---

# 59. 第五個推薦實驗：Operator Order

Group A：

$$
E\rightarrow C.
$$

Group B：

$$
C\rightarrow E.
$$

若：

$$
\mathcal C_{EC}
\neq
\mathcal C_{CE},
$$

支持 non-commutativity。

---

# 60. 第六個推薦實驗：Re-entry Topology

比較：

- no external state；
- raw notes；
- structured checkpoint；
- provenance-preserving AI checkpoint。

測：

$$
K_{RE}.
$$

Primary hypothesis：

$$
K_{RE}^{structured}
<
K_{RE}^{raw}.
$$

---

# 61. 第七個推薦實驗：Topology Increment

同一 neural / behavioral representational dataset：

比較：

$$
RSA,
$$

$$
RTA/TDA,
$$

$$
RSA+RTA.
$$

Primary question：

$$
\boxed{
\text{Does topology predict behavior
beyond geometry?}
}
$$

---

# 62. TADC Phase-1 最小實驗矩陣

| Study | TADC Core | Primary Variable | Main Null |
|---|---|---|---|
| A | TADC-06 | \(d_{\mathrm{rel}}\) | taxonomy / semantic distance |
| B | TADC-02 | dynamic \(U_t\) | fixed partition |
| C | TADC-05 | \(L_D,H_I,\nu_E\) | point-lock / flow |
| D | TADC-04 | \(K_R\) | fixed hierarchy |
| E | TADC-03 | operator order | generic learning |
| F | TADC-07 | \(K_{RE}\) | memory capacity / speed |
| G | Topological claim | persistent topology | geometry-only |

---

# 63. N=1 Longitudinal Studies 的定位

高密度個體 time series 可以非常有價值。

但它能回答：

$$
\boxed{
\text{within-system dynamics}
}
$$

不是：

$$
\boxed{
\text{population prevalence}.
}
$$

---

# 64. N=1 的最低資料要求

至少：

- long enough observation；
- repeated states；
- multiple interruptions；
- multiple returns；
- task labels；
- relation coding；
- outcome measures；
- human / AI event separation。

---

# 65. N=1 不能證明 ADHD 機制

即使 participant 有 ADHD diagnosis：

$$
\boxed{
N=1
\not\Rightarrow
\text{ADHD-general mechanism}.
}
$$

最多：

$$
\boxed{
\text{case-level behavioral topology}.
}
$$

---

# 66. AI System Logs 的額外分層

建議：

$$
X_t
=
(
H_t,S_t,A_t
).
$$

其中：

- \(H_t\)：human interaction；
- \(S_t\)：system / agent activity；
- \(A_t\)：artifacts。

避免：

$$
A_t
\rightarrow H_t
$$

直接反推。

---

# 67. 人–AI 資料的時間解析度

應至少同時保留：

- second / minute；
- session；
- day；
- week；
- project lifetime。

因為：

$$
\boxed{
\text{scale changes the observed switching pattern}.
}
$$

---

# 68. Multi-Resolution Analysis

對時間窗：

$$
\Delta t
\in
\{
1m,10m,1h,1d,1w
\}
$$

計算：

$$
\nu_I(\Delta t),
\nu_E(\Delta t),
H_D(\Delta t),
CCR(\Delta t).
$$

若結論對時間尺度極度不穩定，

必須明確報告。

---

# 69. Topic Segmentation 不能只靠資料夾名

folder / repo：

$$
\neq
$$

cognitive domain。

可以作外部 label：

$$
L_{\mathrm{ext}}.
$$

但 internal domain 需要由：

- content；
- relations；
- goals；
- transition；

估計。

---

# 70. Semantic Drift

長時間資料中：

$$
L(x)
$$

的含義可能變。

因此 relation model 應版本化：

$$
\mathcal R_t.
$$

否則早期與晚期 topic 會被錯誤視為固定相同。

---

# 71. Annotation Pipeline

建議至少三層：

### Machine annotation

LLM / embedding 初標。

### Human review

抽樣／關鍵 edge 檢查。

### Blind adjudication

對 disputed links 做獨立判定。

---

# 72. Ground Truth 不一定存在

像：

$$
d_{\mathrm{rel}}
$$

可能沒有唯一真值。

因此可以用：

$$
\boxed{
\text{multi-rater probabilistic ground truth}.
}
$$

例如：

$$
p(r_{ij}=1).
$$

---

# 73. Measurement Uncertainty

不要把：

$$
\widehat d_{\mathrm{rel}}
$$

當 exact。

應保留：

$$
p(
d_{\mathrm{rel}}
\mid
data
).
$$

domain membership：

$$
p(
x\in U
).
$$

operator：

$$
p(
O_t
).
$$

---

# 74. Soft Topology

在 measurement 階段：

$$
\kappa_{ij}\in[0,1].
$$

比硬 edge：

$$
0/1
$$

更合理。

再透過 filtration：

$$
\theta
$$

研究拓樸是否在廣泛 threshold 下 persistent。

---

# 75. Persistent Feature 的真正意義

若一個 component / loop 只有在非常窄：

$$
\theta
$$

出現，

可能是 threshold artifact。

若跨大區間：

$$
[\theta_b,\theta_d]
$$

存在，

才較 robust。

因此：

$$
\boxed{
\text{persistence}
}
$$

比單 threshold graph 更適合 TADC。

---

# 76. 但是「loop」要有心理意義

persistent homology 找到：

$$
H_1
$$

loop，

不代表：

> 大腦有一個心理循環。

需要第二步：

$$
\boxed{
\text{topological feature}
\rightarrow
\text{behavioral interpretation}.
}
$$

例如 loop persistence 是否預測：

- return path；
- flexible navigation；
- inference；
- switching。

---

# 77. Topological Feature Ablation

若候選 bridge / loop：

$$
f
$$

被認為重要，

應做 perturbation：

$$
\mathcal G
\setminus f.
$$

若 behavior：

$$
Y
$$

不變，

則：

$$
f
$$

可能沒有功能意義。

---

# 78. Causal Intervention 優先於相關

最高證據：

$$
\boxed{
\text{intervene on structure}
\rightarrow
\text{predictable change in behavior}.
}
$$

例如：

- teach bridge；
- remove cue；
- change hierarchy；
- force resolution；
- alter external memory；
- insert false relation。

---

# 79. Engineering 之前必須有 Causal Handle

若：

$$
Z
$$

只是相關，

不能直接設計：

$$
\operatorname{do}(Z).
$$

所以 E1 phase 要求：

$$
\boxed{
P(Y\mid \operatorname{do}(Z))
\neq
P(Y)
}
$$

至少有實驗支持。

---

# 80. 認知拓樸工程的錯誤目標

不能把以下任一當單獨目標：

$$
\max
\text{focus duration},
$$

$$
\max
\text{branch count},
$$

$$
\max
\text{agent throughput},
$$

$$
\min
\text{switching}.
$$

都可能造成反效果。

---

# 81. 多目標工程函數

定義：

$$
J
=
w_1V_R
-
w_2K_{RE}
+
w_3P_R
+
w_4E_C
+
w_5\Gamma_I
-
w_6K_V
-
w_7K_C.
$$

其中：

- \(V_R\)：valid reachability；
- \(K_{RE}\)：re-entry cost；
- \(P_R\)：precision；
- \(E_C\)：exit controllability；
- \(\Gamma_I\)：internalization；
- \(K_V\)：verification cost；
- \(K_C\)：coordination cost。

---

# 82. Engineering Principle 1：Reduce Invalid Distance, Not All Distance

如果所有 concepts 都被拉近：

$$
d(x,y)\rightarrow0,
$$

系統失去 discriminability。

所以目標不是：

$$
\min d.
$$

而是：

$$
\boxed{
\min d_{\mathrm{valid}}
\quad\text{while preserving}
\quad
d_{\mathrm{invalid}}.
}
$$

---

# 83. Principle 2：Preserve Detachment

好的系統不只會：

$$
G.
$$

還要：

$$
D.
$$

即：

$$
\boxed{
\text{build bridges}
+
\text{destroy false bridges}.
}
$$

---

# 84. Principle 3：Preserve Exit Control

若提高：

$$
L_D
$$

卻降低：

$$
E_C,
$$

可能從 productive persistence 變 lock-in。

所以：

$$
\boxed{
\Delta L_D>0
}
$$

不能在：

$$
\Delta E_C\ll0
$$

下被判定為單純 improvement。

---

# 85. Principle 4：Preserve Internalization

AI 支架：

$$
\Gamma_A\uparrow
$$

但：

$$
\Gamma_I\downarrow
$$

時，

應依任務目標決定是否接受。

若目標是學習：

$$
\Gamma_I
$$

權重必須高。

---

# 86. Principle 5：Preserve Provenance

所有 AI bridge：

$$
R_{AI}
$$

應有：

- source；
- confidence；
- version；
- validation state。

否則：

$$
K_V\uparrow.
$$

---

# 87. Principle 6：Optimize Re-entry

對長期 project，

可以保存：

$$
m_b
=
(
G_b,
S_b,
D_b,
Q_b,
N_b,
V_b
).
$$

其中：

- goal；
- state；
- dependency；
- unresolved questions；
- next action；
- verification status。

---

# 88. TADC Tool Prototype 的最小功能

若未來做軟體，

不需要一開始做腦機介面。

先做：

1. branch state capture；
2. relation graph；
3. goal labels；
4. dynamic topic graph；
5. re-entry checkpoint；
6. verified bridge；
7. false-bridge detachment；
8. multi-scale view；
9. event provenance；
10. exportable dataset。

---

# 89. 可視化不是證據

漂亮的 graph：

$$
\neq
$$

真實 cognitive topology。

visualization 只能：

- debug；
- explore；
- communicate。

證據仍來自：

$$
\boxed{
\text{prediction}
+
\text{intervention}
+
\text{replication}.
}
$$

---

# 90. TADC 的總淘汰矩陣

## Kill Condition K1 — Fixed Space Suffices

若：

$$
M_0\approx M_7
$$

在 held-out prediction 長期成立，

ASTC 強版刪除。

---

## K2 — Fixed Domain Suffices

若：

$$
M_1\approx M_7,
$$

DIC / BRC 強版刪除。

---

## K3 — Six Operators Collapse

若：

$$
E,C,G,D,R
$$

都只是 generic learning / weight update，

SOCTS 刪除或壓縮。

---

## K4 — Fixed Hierarchy Suffices

若：

$$
M_{\mathrm{fixed-hierarchy}}
$$

完全預測 multiscale data，

dynamic re-indexing 刪除。

---

## K5 — Hyperfocus Point Model Suffices

若：

$$
L_x,h_x
$$

已完整預測，

DHF / THF 刪除。

---

## K6 — Relational Distance Adds Nothing

若：

$$
d_{\mathrm{rel}}
$$

無增量，

RFCC / CDCC 刪除。

---

## K7 — AI Effect Is Speed Only

若：

$$
K_{\mathrm{lookup}}
$$

解釋全部，

human–AI topology 降級為 offloading model。

---

## K8 — Topology Adds Nothing Beyond Geometry

若：

$$
M_{GT}
\approx
M_G,
$$

正式名稱：

$$
\boxed{
\text{Topological Attention}
}
$$

應降級。

---

# 91. 降級路徑

如果 topology 失敗，

保留：

$$
\boxed{
\text{Dynamic Relational Attention（DRA）}.
}
$$

如果 dynamic domains 也失敗，

再降：

$$
\boxed{
\text{Contextual Relational Attention（CRA）}.
}
$$

如果 relational increment 也失敗，

回到：

$$
\boxed{
\text{existing attention / task-control models}.
}
$$

這不是理論失敗的羞恥，

而是：

$$
\boxed{
\text{successful elimination of unnecessary complexity}.
}
$$

---

# 92. 升級條件

只有當以下至少多項穩定成立：

1. dynamic domain model 有 held-out gain；
2. relational distance 有增量；
3. object/domain re-indexing 可獨立測量；
4. operator order effect 重現；
5. topology-sensitive metric 有增量；
6. causal perturbation 可預測；
7. cross-task replication；

才考慮：

$$
\boxed{
\text{Conjecture}
\rightarrow
\text{Theory}.
}
$$

---

# 93. 什麼時候可以真正叫「拓樸注意力理論」？

最低建議標準：

$$
\boxed{
\exists
\text{ measurable topology-sensitive invariant}
}
$$

且：

$$
\boxed{
\Delta\operatorname{Prediction}_{topology}>0
}
$$

再加：

$$
\boxed{
\text{at least one causal topology-changing intervention}.
}
$$

否則仍保持：

$$
\boxed{
\text{Topological Attention Conjecture}.
}
$$

---

# 94. 第一批預註冊研究建議

## Study 1

Relational-distance crossover experiment。

## Study 2

Goal-induced dynamic domain experiment。

## Study 3

Domain hyperfocus / high-internal-entropy experiment。

## Study 4

Re-indexing / horizontal-vs-vertical switch experiment。

## Study 5

External checkpoint / re-entry experiment。

先不一次驗全部。

---

# 95. 為什麼不一次驗整個 TADC？

因為：

$$
\boxed{
\text{large theory}
+
\text{large flexible dataset}
=
\text{high post-hoc risk}.
}
$$

應逐層：

$$
TADC\text{-}01
\rightarrow
02
\rightarrow
03
\rightarrow\cdots
$$

逐一淘汰。

---

# 96. Measurement Dependency Graph

$$
d_{\mathrm{rel}}
\rightarrow
D_t
\rightarrow
L_D
\rightarrow
THF
$$

如果：

$$
d_{\mathrm{rel}}
$$

測不穩，

後面：

$$
D_t
$$

就失去基礎。

同樣：

$$
D_t
$$

不可靠，

THF 不能測。

所以 TADC 具有明確 measurement dependency。

---

# 97. 最優先測什麼？

不是 Hyperfocus。

而是：

$$
\boxed{
d_{\mathrm{rel}}
}
$$

與：

$$
\boxed{
D_t.
}
$$

因為後者是整套理論的地基。

---

# 98. 第二優先：Re-indexing

若：

$$
\lambda
$$

沒有 cognitive reality，

TADC-04 及部分 TADC-05 / 07 都會縮水。

因此：

$$
\boxed{
K_R
}
$$

是第二核心。

---

# 99. 第三優先：Topology Increment

在 geometry / graph model 已建立後，

才使用 persistent homology / RTA。

順序：

$$
\boxed{
\text{behavior}
\rightarrow
\text{geometry}
\rightarrow
\text{topology}.
}
$$

而不是反過來。

---

# 100. 與現有拓樸神經科學的關係

2025 年 Annual Review 已系統整理 persistent homology 等 topology 方法在：

- grid cells；
- head-direction systems；
- olfaction；
- neural circuits；

中的使用。

2025 representational-topology work 也顯示 topology-sensitive analysis 可以和 RSA 互補。

2026 Human Brain Mapping 研究則顯示部分 persistent-homology / MST-derived network topology measures 可預測認知表現，且在特定 task fMRI 指標上有增量表現。

這些研究說明：

$$
\boxed{
\text{topological neuroscience is already methodologically real}.
}
$$

但：

$$
\boxed{
\text{TADC's cognitive topology is not therefore proven}.
}
$$

它只是現在終於有工具可以被測。

---

# 101. TADC 的兩條證據鏈

## Behavioral Chain

$$
\text{event}
\rightarrow
\text{relation}
\rightarrow
\text{domain}
\rightarrow
\text{transition}
\rightarrow
\text{outcome}.
$$

## Neural Chain

$$
\text{neural state}
\rightarrow
\text{representational geometry}
\rightarrow
\text{topological descriptor}
\rightarrow
\text{behavior}.
$$

兩條若 convergent：

$$
\boxed{
\text{evidence strength}\uparrow.
}
$$

---

# 102. 不要求 Neural Reduction

TADC 不必證明：

$$
\text{one cognitive domain}
=
\text{one brain region}.
$$

更可能：

$$
\boxed{
\text{distributed representation}.
}
$$

所以 neural evidence 主要用來：

- validate geometry；
- identify scale；
- compare models；
- test dynamics。

---

# 103. 行為資料依然可以先行

沒有 fMRI / EEG，

仍可以先測：

- switching cost；
- relational distance；
- re-entry；
- topic entropy；
- domain retention；
- transfer。

因此 TADC 第一階段：

$$
\boxed{
\text{does not require expensive neuroimaging}.
}
$$

---

# 104. Open Science Requirements

建議：

- preregistration；
- public protocol；
- anonymized derived data；
- analysis code；
- model definitions；
- negative results；
- deviation log；
- versioned ontology。

---

# 105. Negative Result Policy

若：

$$
H_1
$$

失敗，

不能：

> 換 threshold 重跑直到成功。

所有 alternative thresholds：

$$
\boxed{
\text{exploratory}.
}
$$

---

# 106. Versioning

TADC model：

$$
M^{v0.1}
$$

若在 pilot 後修改：

$$
M^{v0.2},
$$

confirmatory study 必須明確使用：

$$
v0.2.
$$

不能把不同版本結果混稱同一理論。

---

# 107. Series-Level Evidence Ledger

每個猜想標：

- unsupported；
- exploratory support；
- preregistered support；
- replicated support；
- contradicted；
- abandoned。

例如：

| Conjecture | Status |
|---|---|
| ASTC-W | unsupported / adjacent literature only |
| ASTC-M | unsupported |
| ASTC-S | unsupported |
| DIC | unsupported |
| ONC | unsupported |
| ODDC | unsupported |
| THF | unsupported |
| RFCC | unsupported |
| ECDTC | adjacent offloading evidence only |

避免：

$$
\boxed{
\text{theory drift by rhetoric}.
}
$$

---

# 108. 工程化的成熟條件

只有當：

$$
\operatorname{do}(Z)
\rightarrow
Y
$$

具有可重現 causal effect，

才進工程。

例如：

$$
\operatorname{do}(
K_{RE}\downarrow
)
\rightarrow
P_{\mathrm{return}}\uparrow.
$$

---

# 109. 第一個低風險工程方向：Re-entry

比「增強 hyperfocus」安全。

因為只要設計：

$$
\boxed{
\text{better project checkpoints}
}
$$

測：

$$
K_{RE}.
$$

若無效，

停止。

---

# 110. 第二個方向：Verified Bridge Assistance

AI 只提出：

$$
B_{candidate}.
$$

系統要求：

$$
V(B)
$$

後才加入 persistent graph。

這降低：

$$
\text{false gluing}.
$$

---

# 111. 第三個方向：Adaptive Resolution

工具提供：

- summary；
- mid-level outline；
- raw details。

讓 user：

$$
R^-,
R^+
$$

快速切換。

測：

$$
K_R.
$$

---

# 112. 第四個方向：Exit / Re-entry Controls

在長 focus session 中提供：

- checkpoint；
- stop cue；
- restart state；
- unresolved list。

目標：

$$
E_C\uparrow
$$

與：

$$
R_C\uparrow.
$$

不是：

$$
T_{\mathrm{focus}}\uparrow
$$

本身。

---

# 113. Cognitive Topology Engineering 不是 Neuroengineering

本文的 engineering 首先是：

$$
\boxed{
\text{information architecture}
+
\text{interface}
+
\text{workflow}.
}
$$

不是：

- brain stimulation；
- medication；
- implant。

這些高風險介入需要完全不同的醫療與倫理框架。

---

# 114. 最小工程 KPI

一個 cognitive scaffold 至少測：

$$
\boxed{
\mathbf K
=
(
K_{RE},
P_R,
E_C,
R_C,
\Gamma_I,
K_V
).
}
$$

不能只看：

$$
\text{tasks completed}.
$$

---

# 115. TADC 全系列的最小總方程

認知結構：

$$
\mathcal C_t
=
(
X_t,
\mathcal R_t,
\kappa_t,
\mathcal N_t,
A_t,
G_t
).
$$

尺度：

$$
\lambda_t.
$$

operator：

$$
O_t.
$$

外部支架：

$$
\mathcal S_t^E.
$$

AI：

$$
\mathcal A_t^{AI}.
$$

則：

$$
\boxed{
\mathcal H_{t+1}
=
\Phi
(
\mathcal H_t,
O_t,
\lambda_t,
G_t,
e_t,
m_t
).
}
$$

---

# 116. 可觀察投影

我們真正看到：

$$
Y_t
=
\Psi(
\mathcal H_t
)
+
\epsilon_t.
$$

所以所有認知拓樸：

$$
\mathcal H_t
$$

都是 latent。

研究問題是：

$$
\boxed{
P(
\mathcal H_t
\mid
Y_{1:T}
)
}
$$

是否可辨識。

---

# 117. Identifiability 是最後一道門

若不同：

$$
\mathcal H_t^{(1)}
$$

與：

$$
\mathcal H_t^{(2)}
$$

總能產生一樣：

$$
Y_t,
$$

那麼 TADC 無法從資料判定。

此時：

$$
\boxed{
\text{theory may be mathematically expressive
but empirically unidentified}.
}
$$

必須停止強宣稱。

---

# 118. Final Falsification Principle

TADC 應遵守：

$$
\boxed{
\text{Every added structural degree of freedom
must buy predictive or causal information.}
}
$$

如果沒有：

$$
\boxed{
\text{delete it}.
}
$$

---

# 119. 系列最終壓縮

TADC-01：

$$
\text{space may change}.
$$

TADC-02：

$$
\text{domains may be induced}.
$$

TADC-03：

$$
\text{change may have operator structure}.
$$

TADC-04：

$$
\text{object/domain may be scale-relative}.
$$

TADC-05：

$$
\text{focus may persist despite internal mobility}.
$$

TADC-06：

$$
\text{relational distance may beat disciplinary distance}.
$$

TADC-07：

$$
\text{external systems may alter effective reachability}.
$$

TADC-08：

$$
\boxed{
\text{measure all of this,
compare it against simpler models,
and delete whatever does not survive}.
}
$$

---

# 120. 結論

TADC 系列最初由一個直覺開始：

> 注意力可能不只是把 spotlight 移到另一個地方。

經八篇發展後，

其最強版本可以寫成：

$$
\boxed{
\text{attention and cognitive control
may participate in dynamically reorganizing
a multiscale relational accessibility structure}.
}
$$

但這仍然只是：

$$
\boxed{
\text{conjecture}.
}
$$

TADC-08 的目的就是禁止系列靠概念漂亮自我延續。

本文因此把最終研究流程固定為：

$$
\boxed{
\text{Define}
\rightarrow
\text{Measure}
\rightarrow
\text{Compete}
\rightarrow
\text{Intervene}
\rightarrow
\text{Replicate}
\rightarrow
\text{Engineer}.
}
$$

而不是：

$$
\boxed{
\text{Define}
\rightarrow
\text{Rename}
\rightarrow
\text{Expand forever}.
}
$$

真正的拓樸注意力理論至少需要：

1. 可重現的 dynamic-domain measurement；
2. 可區分的 relational distance；
3. 可測的 multiscale re-indexing；
4. 至少部分 operator identity；
5. topology-sensitive measure 的增量預測；
6. causal intervention；
7. cross-task / cross-sample replication。

若這些條件無法成立，

TADC 應依序降級：

$$
\boxed{
\text{Topological Attention}
\rightarrow
\text{Dynamic Relational Attention}
\rightarrow
\text{Contextual Relational Attention}
\rightarrow
\text{existing models}.
}
$$

這不是失敗。

這正是本文要求的科學結果。

反之，

如果：

$$
M_{\mathrm{dynamic-topology}}
$$

在新的資料上穩定擊敗：

$$
M_{\mathrm{fixed-space}},
$$

如果：

$$
d_{\mathrm{rel}}
$$

穩定預測 cognitive switching，

如果：

$$
P\circ\Phi_f
\approx
\Phi_c\circ P
$$

跨尺度成立，

如果：

$$
\Delta_{\mathrm{topo}}
$$

能預測 behavior，

如果對 bridge、scale、external state 的 intervention 能產生預測中的改變，

那麼 TADC 才有資格從：

$$
\boxed{
\text{conjecture series}
}
$$

向：

$$
\boxed{
\text{empirical theory}
}
$$

升級。

因此本系列最後留下的不是：

> 「人類注意力就是拓樸。」

而是更嚴格的命題：

$$
\boxed{
\text{Test whether attention is better described
as allocation over fixed states,
or as controlled motion and transformation
over a measurable multiscale relational space.}
}
$$

中文：

> **去驗證：注意力究竟只是固定狀態集合上的資源分配，還是更適合被描述為對一個可測、多尺度、關係化認知空間的移動與轉換控制。**

直到資料做出選擇之前，

TADC 都應保持：

$$
\boxed{
\text{可反證的命題，而不是答案。}
}
$$

---

# 參考文獻

1. Lee JQ, Keinath AT, Cianfarano E, Brandon MP. **Identifying representational structure in CA1 to benchmark theoretical models of cognitive mapping.** *Neuron*. 2025;113(2):307–320.e5. doi:10.1016/j.neuron.2024.10.027. PMID: 39579760.  
2. Brown S, Farivar R. **The topology of representational geometry.** *Frontiers in Neuroscience*. 2025;19:1597899. doi:10.3389/fnins.2025.1597899. PMID: 40620351.  
3. Lin B, Kriegeskorte N. **The topology and geometry of neural representations.** *PLoS Computational Biology*. 2024;20(10):e1012445. PMCID: PMC11494346.  
4. Curto C, Sanderson N. **Topological Neuroscience: Linking Circuits to Function.** *Annual Review of Neuroscience*. 2025;48:491–518. doi:10.1146/annurev-neuro-112723-034315.  
5. Tan L, Qiu Y, Qiu L, et al. **The medial and lateral orbitofrontal cortex jointly represent the cognitive map of task space.** *Communications Biology*. 2025;8:163. doi:10.1038/s42003-025-07588-w. PMID: 39900714.  
6. Peer M, Epstein RA. **Cognitive maps for hierarchical spaces in the human brain.** *Cerebral Cortex*. 2025;35(9):bhaf261. doi:10.1093/cercor/bhaf261. PMID: 40982478.  
7. Bhandari A, Keglovits H, Buyukyazgan D, Badre D. **Task structure tailors the geometry of neural representations in human lateral prefrontal cortex.** Preprint / manuscript line of work; representational similarity analyses reported in the available manuscript.  
8. Lee MD, Criss AH, Devezer B, Donkin C, Etz A, Leite FP, Matzke D, Rouder JN, Trueblood JS, White CN, Vandekerckhove J. **Robust modeling in cognitive science.** *Computational Brain & Behavior*. 2019;2:141–153.  
9. Crüwell S, Stefan AM, Evans NJ. **Preregistration in diverse contexts: a preregistration template for the application of cognitive models.** *Royal Society Open Science*. 2021;8:210155. doi:10.1098/rsos.210155.  
10. **A registered report of preregistration practices in studies of electroencephalogram (EEG) and event-related potentials (ERPs): A first look at accessibility, adherence, transparency, and selection bias.** *Cortex*. 2025;185:253–269. doi:10.1016/j.cortex.2025.02.008.  
11. Risko EF, Gilbert SJ. **Cognitive Offloading.** *Trends in Cognitive Sciences*. 2016;20(9):676–688. doi:10.1016/j.tics.2016.07.002. PMID: 27542527.  
12. Burnett LK, Richmond LL. **Meta-analytic investigations of the effect of cognitive offloading on memory-based task performance and interindividual variability.** *Memory & Cognition*. 2026;54(1):144–168. doi:10.3758/s13421-025-01743-8. PMID: 40500483.  
13. Bastani H, Bastani O, Sungu A, Ge H, Kabakcı Ö, Mariman R. **Generative AI without guardrails can harm learning: Evidence from high school mathematics.** *Proceedings of the National Academy of Sciences USA*. 2025;122(26):e2422633122. doi:10.1073/pnas.2422633122. PMID: 40560616.  
14. Hupfeld KE, Osborne JB, Tran QT, Hyatt HW, Abagis TR, Shah P. **Validation of the dispositional adult hyperfocus questionnaire (AHQ-D).** *Scientific Reports*. 2024;14:19460. doi:10.1038/s41598-024-70028-y. PMID: 39169147.  
15. Garcia Pimenta M, Gruhnert RK, Fuermaier ABM, Groen Y. **The role of executive functions in mediating the relationship between adult ADHD symptoms and hyperfocus in university students.** *Research in Developmental Disabilities*. 2024;144:104639. PMID: 38039699.  
16. Wang X, Krieger-Redwood K, Cui Y, et al. **Macroscale brain states support the control of semantic cognition.** *Communications Biology*. 2024;7:926. doi:10.1038/s42003-024-06630-7.  
17. Garvert MM, Dolan RJ, Behrens TEJ. **A map of abstract relational knowledge in the human hippocampal-entorhinal cortex.** *eLife*. 2017;6:e17086. doi:10.7554/eLife.17086.  
18. Park SA, Miller DS, Nili H, Ranganath C, Boorman ED. **Map Making: Constructing, Combining, and Inferring on Abstract Cognitive Maps.** *Neuron*. 2020;107(6):1226–1238.e8. doi:10.1016/j.neuron.2020.06.030.  
19. Behrens TEJ, Muller TH, Whittington JCR, et al. **What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior.** *Neuron*. 2018;100(2):490–509. doi:10.1016/j.neuron.2018.10.002.  
20. **Resting-State and Task Functional Magnetic Resonance Imaging Network Topology Metrics With no Threshold Selection to Predict Cognition.** *Human Brain Mapping*. 2026. PMID: 41947425.  

---

# 系列總索引

## TADC-01
**《注意力不是單點選擇——可變認知空間與注意—空間轉換猜想》**

核心：

$$
\boxed{
\text{Attention may transform effective cognitive accessibility.}
}
$$

---

## TADC-02
**《動態認知域——領域作為局部座標圖》**

核心：

$$
\boxed{
\text{Domain boundaries may be induced, overlapping, and goal-relative.}
}
$$

---

## TADC-03
**《拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引》**

核心：

$$
\boxed{
\mathcal O
=
\{E,C,T,G,D,R\}.
}
$$

---

## TADC-04
**《嵌套注意域與觀察尺度——宏觀／微觀的相對性與多尺度重索引》**

核心：

$$
\boxed{
\text{domain at one scale}
\leftrightarrow
\text{object at another}.
}
$$

---

## TADC-05
**《從單點超專注到拓樸超專注——域級持續性、內部高熵遍歷與可控退出》**

核心：

$$
\boxed{
\text{focus persistence}
\neq
\text{state immobility}.
}
$$

---

## TADC-06
**《關係優先認知與跨域連續性——從學科距離到關係距離的認知拓樸猜想》**

核心：

$$
\boxed{
d_{\mathrm{ext}}
\neq
d_{\mathrm{rel}}.
}
$$

---

## TADC-07
**《外部認知支架與人—AI 認知拓樸——有效距離、回返成本與混合認知系統》**

核心：

$$
\boxed{
d_{\mathrm{eff}}
=
d(
\mathcal C^H
\oplus
\mathcal S^E
\oplus
\mathcal A^{AI}
).
}
$$

---

## TADC-08
**《拓樸注意力的測量、反證與工程化——從命題系列到可淘汰的研究程序》**

核心：

$$
\boxed{
\text{Every added structural degree of freedom
must buy predictive or causal information.}
}
$$

否則：

$$
\boxed{
\text{delete it}.
}
$$

---

# 系列狀態

**系列：** TADC v0.1 — 第一季完成  
**篇數：** 8  
**原始人體／臨床數據：** 無  
**理論狀態：** 命題猜想系列／研究綱領  
**實證狀態：** 僅與既有相鄰文獻建立理論接軌；TADC 特有核心命題尚待直接驗證  
**下一階段：** Measurement Design → Pilot Protocol → Preregistered Validation  
**升級條件：** topology-sensitive incremental prediction + causal intervention + replication  
**降級條件：** 若 topology 無增量，改為 Dynamic Relational Attention；若 dynamic relational structure 亦無增量，進一步收縮至既有 attention / task-control models
