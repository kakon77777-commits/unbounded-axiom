# 世界集合學習：跨世界結果如何更新生成器、模型、Governor 與未來空間

**World Ensemble Learning: How Cross-World Outcomes Update Generators, World Models, Governors, and Future Spaces**

**Branching World Computation / World-Domain Cognitive Runtime**  
**分支世界計算／世界域認知 Runtime 系列**  
**WDC-07 / BWC-07 — Learning Paper I**

作者：Neo.K（許筌崴）  
協作形式化：Aletheia  
機構：一言諾科技有限公司（EveMissLab）  
日期：2026-08-17  
版本：v0.1  
狀態：world-ensemble learning / recursive-update / anti-collapse formalization

---

## Canonical Non-Identity Statement

WDC-05 已建立：

$$
\boxed{
\text{World Count}
\neq
\text{Independent Evidence Count}
\neq
\text{Truth}.
}
$$

WDC-06 已建立：

$$
\boxed{
\text{Worth Computing}
\neq
\text{Worth Believing}
\neq
\text{Worth Deploying}.
}
$$

本文進一步建立：

$$
\boxed{
\text{Learning from Generated Worlds}
\neq
\text{Learning from Reality}.
}
$$

以及：

$$
\boxed{
\text{World Outcome}
\neq
\text{Training Target}
}
$$

除非存在明示的 update contract。

本文永久保留：

$$
\boxed{
\text{More Self-Generated Experience}
\not\Rightarrow
\text{More Real-World Knowledge}.
}
$$

本文不主張：

- 所有 world outcomes 都應拿來訓練 generator；
- generated-world experience 與 real-world experience 應等權；
- self-training 必然導致 collapse；
- synthetic data 永遠有害；
- world ensemble learning 必須以 gradient descent 實作；
- world generator、world model、Governor 應共享同一 objective；
- meta-learning across worlds 自動帶來跨現實 generalization；
- 一個 world ensemble 可以取代 real-world calibration；
- continual learning 只要有 replay 就不會忘記；
- model collapse 文獻等同 WDC world-ontology collapse；
- 本文已完成所有 WDC runtime 層；
- 本文對 classical $P$ vs. $NP$ 提供任何新證明。

---

# 摘要

WDC-01 至 WDC-06 已建立：

1. future candidate 到 runnable world 的實例化；
2. world fork、checkpoint、lineage 與 branching graph；
3. World-Domain Governor；
4. master / local agent / observer / evaluator / Governor 的角色分離；
5. dependence-aware cross-world evidence；
6. next-world-computation 的 world-portfolio metareasoning。

至此，WDC 已經能：

$$
\boxed{
\text{Generate}
\rightarrow
\text{Run}
\rightarrow
\text{Compare}
\rightarrow
\text{Allocate}.
}
$$

但仍缺最後一個核心問題：

> **跨世界計算產生的經驗，如何真正改變下一輪世界生成、世界模型、Governor 與 TCD Future Base Space？**

如果沒有 learning loop，WDC 只是：

$$
\boxed{
\text{expensive simulation factory}.
}
$$

每一輪都重新：

- generate worlds；
- run worlds；
- aggregate evidence；
- archive；

卻不真正累積能力。

因此本文建立：

# **World Ensemble Learning**
## **世界集合學習**

本文定義 ensemble-learning state：

$$
\boxed{
\mathfrak L_t^W
=
(
\Gamma_t^W,
M_t^W,
\Pi_t^G,
\mathcal B_t^+,
\mathcal E_t^W,
\mathcal R_t^S,
\kappa_L
).
}
$$

其中：

- $\Gamma_t^W$：World Generator；
- $M_t^W$：world dynamics / world-model family；
- $\Pi_t^G$：Governor computation policy；
- $\mathcal B_t^+$：TCD Future Base Space；
- $\mathcal E_t^W$：cross-world evidence graph；
- $\mathcal R_t^S$：source / provenance registry；
- $\kappa_L$：learning contract。

本文將每輪 world ensemble：

$$
\boxed{
\mathcal W_t
=
\{
W_1,\ldots,W_n
\}
}
$$

執行後形成：

$$
\boxed{
\mathcal O_t^W
=
\{
Outcome(W_i),
Trace(W_i),
Evidence(W_i)
\}_{i=1}^n.
}
$$

再經 learning gate：

$$
\boxed{
\mathcal G_L:
(
\mathcal O_t^W,
\mathcal E_t^W,
\kappa_L
)
\rightarrow
\Delta\mathfrak L_t^W.
}
$$

本文將更新拆成四條主要 channel：

$$
\boxed{
\begin{aligned}
\mathcal U_{\Gamma}
&:
\Gamma_t^W
\rightarrow
\Gamma_{t+1}^W,
\\
\mathcal U_M
&:
M_t^W
\rightarrow
M_{t+1}^W,
\\
\mathcal U_G
&:
\Pi_t^G
\rightarrow
\Pi_{t+1}^G,
\\
\mathcal U_F
&:
\mathcal B_t^+
\rightarrow
\mathcal B_{t+1}^+.
\end{aligned}
}
$$

四者不可 silent collapse。

## Generator Learning

更新：

- 哪些 world families 值得提出；
- 哪些 ontology 缺失；
- 哪些 counterworld 模板有效；
- 哪些 candidate 只是 duplicate。

## World-Model Learning

更新：

- dynamics；
- transition uncertainty；
- state representation；
- agent behavior model；
- error regions。

## Governor Learning

更新：

- 哪類 world computation 有高 realized VOC；
- 哪些 early-stop heuristic 錯；
- 哪些 branches 常找到反例；
- 哪些 backend 有 transport value。

## Future-Space Learning

更新 TCD：

$$
\mathcal B_t^+
$$

中的：

- candidate set；
- probabilities；
- realization paths；
- unknown-world mass；
- future ontology。

因此：

$$
\boxed{
\text{learning worlds}
\neq
\text{learning only one model}.
}
$$

本文再建立 **Source Provenance Class**：

$$
\boxed{
Source(e)
\in
\{
Real,
External,
World,
Synthetic,
Derived,
Unknown
\}.
}
$$

其中：

- **Real**：直接 real-world observation / experiment；
- **External**：獨立外部資料源；
- **World**：WDC runnable-world output；
- **Synthetic**：generator synthetic sample；
- **Derived**：由其他 evidence 計算出的 secondary artifact；
- **Unknown**：來源不明或 lineage 不完整。

這個 source label 不代表 truth ranking。

例如：

$$
World
$$

source 可以非常高品質，

而：

$$
Real
$$

source 也可能有 measurement error。

但 source class 必須保留，因為：

$$
\boxed{
\text{source provenance}
}
$$

決定：

- independence；
- calibration；
- transport；
- recursive-training risk。

本文正式提出：

# **World-to-Learning Evidence Gate**

對 sample / evidence：

$$
e_i,
$$

定義：

$$
\boxed{
\mathsf{LearnGate}(e_i)
=
(
V_i,
I_i,
T_i,
P_i,
U_i,
R_i
).
}
$$

其中：

- $V_i$：validity；
- $I_i$：independence；
- $T_i$：transport status；
- $P_i$：provenance integrity；
- $U_i$：uncertainty；
- $R_i$：reality anchoring。

只有符合 update contract 的 evidence，才進入對應 learning channel。

因此：

$$
\boxed{
Outcome(W_i)
\not\Rightarrow
Train(M).
}
$$

本文特別區分三種 update scope：

### Scope S0 — World-Local Update

只影響：

$$
W_i
$$

或其 child worlds。

### Scope S1 — Ensemble-Relative Update

影響：

- world generator；
- world-family prior；
- Governor；
- cross-world evidence。

但仍只視為：

$$
\boxed{
\text{simulation-relative learning}.
}
$$

### Scope S2 — Reality-Facing Update

影響：

- target dynamics model；
- real deployment policy；
- reality-facing probability。

需要額外：

$$
\boxed{
\mathcal T_{W\rightarrow R}
}
$$

與 external calibration。

因此：

$$
\boxed{
S1
\not\Rightarrow
S2.
}
$$

這是本文最重要的防過度外推邊界之一。

本文再建立：

# **Reality Anchor**

定義：

$$
\boxed{
\mathcal A_R
=
\{
e_i:
Source(e_i)\in
\{Real,External\}
\text{ and passes calibration contract}
\}.
}
$$

world ensemble learning 可以大量使用 synthetic / world-relative experience，

但 reality-facing learner 應保持：

$$
\boxed{
\mathcal A_R\neq\varnothing
}
$$

在需要 real-world validity 的 domain 中。

外部模型崩潰研究提供了一個重要而有限的警告。Shumailov 等人在 Nature 2024 顯示，對多類生成模型，若 successive generations indiscriminately train on model-generated data，原始資料分布尾部資訊可能逐步消失，並可能形成所謂 model collapse；其實驗也顯示，保留部分 original data 能減輕 degradation。

WDC 不把這直接等同：

$$
\boxed{
\text{World Ontology Collapse}.
}
$$

但它提供強烈的機制警告：

> 如果世界生成器只從自己以前生成過的 worlds 學習，而 real / external anchors 越來越少，系統可能逐步把「可能世界」壓縮成自己的既有生成分布。

本文將此 WDC 特有風險定義為：

# **World Ontology Collapse**
## **世界本體域塌縮**

概念性條件：

$$
\boxed{
Diversity(
\Gamma_{t+1}^W
)
<
Diversity(
\Gamma_t^W
)
}
$$

並伴隨：

$$
\boxed{
Coverage(
ExternalNovelty
)
\downarrow
}
$$

與：

$$
\boxed{
SelfAgreement
\uparrow.
}
$$

它不等同 statistical model collapse。

WDC World Ontology Collapse 可以表現在：

- candidate ontology 變窄；
- rare world families 消失；
- counterworld generation 變弱；
- unknown-world mass 被錯誤壓低；
- generator 越來越偏好自己過去成功的 templates；
- Governor 越來越少探索 outside-family worlds。

因此：

$$
\boxed{
\text{high self-consistency}
}
$$

甚至可能是危險訊號。

本文再定義：

# **Self-Confirmation Loop**

$$
\boxed{
\Gamma_t^W
\rightarrow
\mathcal W_t
\rightarrow
Outcome_t
\rightarrow
Train(
\Gamma_t^W
)
\rightarrow
\Gamma_{t+1}^W.
}
$$

如果：

- generator 提出 worlds；
- worlds 由 generator-family dynamics 驅動；
- evaluator 也同源；
- outcome 再回訓 generator；

則形成：

$$
\boxed{
\text{closed epistemic loop}.
}
$$

即使每一步沒有 software bug，

整體仍可能：

> 越來越確信自己。

因此本文建立：

# **Anti-Self-Sealing Requirement**

每個重要 learning cycle 至少檢查：

1. external anchor 是否存在；
2. independent backend 是否存在；
3. counterworld 是否被保留；
4. evaluator independence 是否足夠；
5. unknown-world mass 是否被保留；
6. rejected-world / failed-world traces 是否仍可學習。

本文再建立 **Negative Evidence Learning**。

一個 world：

$$
W_f
$$

失敗，

不應只：

$$
Archive(W_f).
$$

應提取：

$$
\boxed{
FailurePacket(W_f)
=
(
CauseHypothesis,
StateRegion,
Assumptions,
Backend,
Counterevidence,
TransportScope
).
}
$$

並更新：

$$
\Gamma^W
$$

使未來更會生成：

- failure-adjacent worlds；
- boundary cases；
- counterexamples。

因此：

$$
\boxed{
\text{failure}
\neq
\text{useless training data}.
}
$$

本文進一步建立 **World-Model Error Learning**。

對 world：

$$
W_i,
$$

若有 external / calibration target：

$$
Y_i^{target},
$$

model prediction：

$$
\widehat Y_i,
$$

定義：

$$
\boxed{
\delta_i^{model}
=
d(
\widehat Y_i,
Y_i^{target}
).
}
$$

error packet：

$$
\boxed{
EP_i
=
(
\delta_i,
StateRegion_i,
ActionRegion_i,
ModelVersion_i,
Assumption_i,
Confidence_i
).
}
$$

不是只做 global loss。

Governor 可以將 error 按 region 聚類：

$$
\boxed{
\mathcal R_{err}
=
\{
R_1,\ldots,R_k
\}.
}
$$

再優先生成：

$$
\boxed{
W_{err,k}
}
$$

去填補 model blind spots。

這使：

$$
\boxed{
\text{prediction error}
\rightarrow
\text{world generation}
}
$$

形成 active learning loop。

外部 DreamerV3 提供非常清楚的局部工程對照：world model、critic 與 actor 會在 agent 與 environment 互動時，從 replayed experience 並行更新；world model 從 sensory observations 學 representation 並預測 potential action outcomes。這證明「experience → model/policy update → next interaction」已是成熟 model-based learning pattern。

但 WDC 的額外難點是：

> experience 不只來自一個 environment，而來自具有不同 lineage、backend、fidelity、transport scope 的 world ensemble。

因此本文定義 **World-Ensemble Replay Buffer**：

$$
\boxed{
\mathcal R_W
=
\{
(e_i,w_i,source_i,family_i)
\}.
}
$$

其中：

$$
w_i
$$

不是只有 TD priority，

還可以考慮：

- independence；
- counterexample value；
- transport strength；
- rarity；
- recency；
- model-error region。

本文提出：

# **Provenance-Aware Replay**

取樣分布：

$$
\boxed{
P_{replay}(e_i)
\propto
g(
Priority_i,
Independence_i,
Rarity_i,
Error_i,
Transport_i
).
}
$$

不是 universal formula。

其目的在於避免 replay buffer 被：

> 大量 cheap same-family worlds

淹沒。

本文再建立 **Family-Balanced Replay**。

若：

$$
\mathcal F_k
$$

有：

$$
10^6
$$

samples，

另一個 independent family：

$$
\mathcal F_j
$$

只有：

$$
10^3,
$$

不能只依 sample count 訓練，否則 generator / model 會被第一 family 壟斷。

可引入：

$$
\boxed{
WeightFamily(
\mathcal F_k
)
}
$$

作 family-level normalization。

這直接延續 WDC-05：

$$
\boxed{
WorldCount
\neq
IndependentEvidenceCount.
}
$$

同樣：

$$
\boxed{
SampleCount
\neq
IndependentLearningSignalCount.
}
$$

本文再建立 **Continual World-Model Learning**。

WDC world families 會隨時間：

$$
\mathcal F_1,
\mathcal F_2,\ldots
$$

不斷新增。

如果 model 每學新 family 就忘掉舊 dynamics，

則：

$$
\boxed{
\text{world-model catastrophic forgetting}.
}
$$

2025 年 Fu 等人的 DRAGO work 專門研究 continual model-based RL 中 world-model knowledge retention，使用 synthetic experience rehearsal 與重新探索 prior-task-relevant states 來維持跨任務的 world-model knowledge。Liu 等人 2025 則提出 online world model 的 continual RL approach，讓 planner 基於持續更新的 model 進行 planning，並專門評估 forgetting。

這些工作不等於 WDC，但它們支持：

$$
\boxed{
\text{continually updating world models}
}
$$

與：

$$
\boxed{
\text{knowledge retention}
}
$$

本身是實際可研究的 algorithmic problem。

因此 WDC-07 將 world-model update 寫成：

$$
\boxed{
M_{t+1}^W
=
\mathcal U_M
(
M_t^W,
\mathcal R_W,
\mathcal A_R,
\kappa_M
).
}
$$

其中必須同時處理：

- adaptation；
- retention；
- provenance；
- model uncertainty；
- source weighting。

本文不要求：

$$
\mathcal U_M
$$

一定是 neural fine-tuning。

它也可以是：

- symbolic rule update；
- simulator calibration；
- Bayesian posterior update；
- parameter estimation；
- ensemble reweighting；
- model-family creation。

本文再建立 **Generator Update**：

$$
\boxed{
\Gamma_{t+1}^W
=
\mathcal U_{\Gamma}
(
\Gamma_t^W,
\mathcal E_t^W,
U_W,
Failures_t,
\kappa_{\Gamma}
).
}
$$

更新 generator 不只：

> 讓它更常產生 successful worlds。

還要：

- 增加 coverage；
- 保留 counterworlds；
- 修復 missing ontology；
- 降低 duplicate generation；
- 增加 high-information branches。

本文提出 **Generator Learning Targets**：

$$
\boxed{
\mathbf T_{\Gamma}
=
(
Coverage,
Novelty,
Counterability,
Independence,
Validity,
Cost,
TransportPotential
).
}
$$

因此：

$$
\boxed{
\text{generator quality}
\neq
\text{average outcome success}.
}
$$

一個只會生成：

> 容易成功的 worlds

的 generator 對 science 很差。

本文再建立 **Governor Learning**。

WDC-06 執行前估：

$$
\widehat V_t(c).
$$

執行後獲得：

$$
V_t^{realized}(c).
$$

所以：

$$
\boxed{
\Pi_{t+1}^G
=
\mathcal U_G
(
\Pi_t^G,
\widehat V_t,
V_t^{realized},
GovernanceMiss_t
).
}
$$

Governor 可學：

- 哪種 deficit routing 有效；
- 哪種 low-fidelity gate 常誤砍；
- 哪種 counterworld generator 高產；
- 哪種 backend 真正增加 independence；
- 哪類 transport tests 最能改變 real decision。

但這裡有 selection-bias danger：

> Governor 只知道自己選擇執行的 computations 的 realized value。

未執行：

$$
c_{rejected}
$$

的 true realized value 不可觀測。

因此本文建立：

# **Governor Exploration Audit**

定期抽取一小部分：

$$
\boxed{
c\sim
\mathcal Q_{audit}
}
$$

來自：

- low-priority queue；
- rejected worlds；
- pruned branches；

做 audit execution。

這不是要求固定比例。

目的是估計：

$$
\boxed{
\text{selection blind spot}.
}
$$

本文再建立 **Future-Space Update**。

TCD Future Base Space：

$$
\mathcal B_t^+
$$

在 world ensemble evidence 後應更新：

$$
\boxed{
\mathcal B_{t+1}^+
=
\mathcal U_F
(
\mathcal B_t^+,
\mathcal E_t^W,
U_W,
D_T
).
}
$$

其中：

- failed candidates 可以降權；
- newly discovered branches 加入；
- realization paths 修正；
- unknown mass 可上升或下降；
- future ontology 可重構。

重要的是：

$$
\boxed{
\text{world simulation can increase unknown mass}.
}
$$

如果 worlds 大量 disagreement，

系統應可能：

$$
U_W\uparrow
$$

而不是硬壓成單一 posterior。

因此：

# **Disagreement-as-Learning Principle**

> **Independent world disagreement is not merely noise to be averaged away; it can be evidence that the current future ontology or model family is incomplete.**

本文再建立 **Ontology Expansion Trigger**。

若：

$$
\boxed{
S_E(q)
>
\theta_{sens}
}
$$

即 cross-world evidence 對：

- backend；
- assumption；
- evaluator；

高度敏感，

且 existing model families 無法解釋 disagreement，

則：

$$
\boxed{
Trigger(
GenerateNewOntology
).
}
$$

不是：

$$
\boxed{
RunMoreSameFamily.
}
$$

本文稱：

# **World-Family Novelty Injection**

Governor 可要求 Generator：

> 產生一個不共享 dominant assumptions 的新 world family。

例如明示：

$$
\boxed{
Dependence(
W_{new},
\mathcal F_{dominant}
)
<
\theta_D.
}
$$

這是一個 target，而不是保證。

本文再建立 **External Novelty Injection**。

為防 self-sealing，可以定期引入：

- new real data；
- external scientific model；
- independent human hypothesis；
- alternative AI model；
- anomaly；
- failed prediction。

形成：

$$
\boxed{
\mathcal N_{ext,t}.
}
$$

Generator update：

$$
\boxed{
\Gamma_{t+1}
=
\mathcal U_{\Gamma}
(
\Gamma_t,
\mathcal E_t^W,
\mathcal N_{ext,t}
).
}
$$

這與 model-collapse research 的「preserve original data / genuine interactions」警告方向一致。

本文再建立 **Reality-Anchor Ratio** 概念：

$$
\boxed{
\rho_R
=
\frac{
Weight(
Real+External
)
}{
Weight(
AllLearningEvidence
)
}.
}
$$

本文不規定：

$$
\rho_R
$$

固定下限。

不同 domain：

- pure mathematics simulation；
- game design；
- robotics；
- economics；

需求不同。

但 reality-facing systems 應至少記：

$$
\boxed{
\rho_R
}
$$

與其時間變化。

若：

$$
\rho_R\rightarrow0
$$

同時：

$$
SelfAgreement\uparrow,
$$

應觸發：

$$
\boxed{
SelfSealingWarning.
}
$$

本文再建立 **Synthetic Provenance Depth**。

若 sample：

$$
e
$$

來自：

> model A 生成 world → model B 從 world 生成 data → model C 再生成 summary。

定義：

$$
\boxed{
d_{syn}(e).
}
$$

---

# 1. Synthetic Depth 0

direct real / external evidence。

---

# 2. Depth 1

direct world / synthetic output。

---

# 3. Depth 2+

recursive derived synthetic lineage。

---

# 4. Why Track?

不是因為深度高必然錯。

而是：

> recursive lineage 的 shared-error / collapse risk 可能增加。

---

# 5. Provenance Depth Is a Risk Coordinate

$$
\boxed{
d_{syn}
\neq
TruthScore.
}
$$

---

# 6. Update Weight

可：

$$
\boxed{
w_i
=
g(
Validity,
Transport,
Independence,
d_{syn}
).
}
$$

但不要求 universal $g$。

---

# 7. Generator Self-Training

若：

$$
Source=World
$$

且：

$$
GeneratorAncestor=
\Gamma_t,
$$

需標：

$$
\boxed{
SelfGenerated=1.
}
$$

---

# 8. External Generated Data

另一獨立 generator：

$$
SelfGenerated=0
$$

但仍可能 shared foundation data。

---

# 9. Need Model Lineage

---

# 10. Self-Generated World Learning Modes

本文區分：

### SG-0 — No Update

world output只作 inference evidence。

### SG-1 — Local Adaptation

只改該 world / child。

### SG-2 — Generator Heuristic Update

改 candidate priorities / templates。

### SG-3 — Model Parameter Update

world data進 training。

### SG-4 — Reality-Facing Update

影響 real deployment model。

---

# 11. Higher Mode Requires Stronger Gate

$$
\boxed{
Gate(SG4)
>
Gate(SG3)
>
Gate(SG2).
}
$$

只作 policy ordering。

---

# 12. Synthetic Learning Firewall

在 SG3/SG4 之間：

$$
\boxed{
\mathcal F_{syn}.
}
$$

---

# 13. It Checks

- provenance；
- transport；
- dependence；
- reality anchor；
- calibration。

---

# 14. No Silent Synthetic Promotion

---

# 15. Model Collapse External Warning

Shumailov et al. show indiscriminate recursive generated-data training can lose distribution tails。

---

# 16. WDC Analogue

rare world families may disappear first。

---

# 17. Tail Preservation

Need：

$$
\boxed{
Archive(
RareWorlds
).
}
$$

---

# 18. Rare Worlds Are Not Noise by Default

---

# 19. Tail Coverage Metric

$$
\boxed{
C_{tail}.
}
$$

---

# 20. Compare Across Learning Generations

$$
C_{tail,t+1}
-
C_{tail,t}.
$$

---

# 21. Ontology Entropy

conceptual：

$$
\boxed{
H_O(
\Gamma_t
).
}
$$

---

# 22. Low Entropy Is Not Automatically Bad

If reality truly simple。

---

# 23. But Low Entropy + External Failures Is Bad

---

# 24. Novelty Retention

Track：

$$
\boxed{
N_{novel}^{external}.
}
$$

---

# 25. Does Generator Still Produce Worlds Explaining New anomalies?

---

# 26. Self-Agreement Index

$$
\boxed{
A_{self}(t).
}
$$

---

# 27. If:

$$
A_{self}\uparrow
$$

while external calibration stalls,

warning。

---

# 28. Reality Gap

$$
\boxed{
G_R(t)
=
d(
PredictedExternal,
ObservedExternal
).
}
$$

---

# 29. Collapse Signature

Possible:

$$
\boxed{
A_{self}\uparrow,
\quad
H_O\downarrow,
\quad
G_R\uparrow.
}
$$

---

# 30. This Is WDC Self-Sealing Signature

not theorem。

---

# 31. DreamerV3 External Calibration

world model, critic, actor update concurrently from replayed experience。

---

# 32. WDC Generalization

we need concurrent updates across：

- generator；
- model；
- governor；
- future space。

---

# 33. But Not Same Gradient

---

# 34. Separate Update Timescales

$$
\boxed{
\eta_\Gamma,
\eta_M,
\eta_G,
\eta_F.
}
$$

---

# 35. Generator Slow Update

avoid overreacting one world。

---

# 36. Governor Faster Update

maybe adapt scheduling quicker。

---

# 37. World Model Update Domain-Specific

---

# 38. Future-Space Update Can Be Event-Driven

---

# 39. Timescale Separation

$$
\boxed{
\tau_{update}^{\Gamma}
\neq
\tau_{update}^{M}
\neq
\tau_{update}^{G}
\neq
\tau_{update}^{F}.
}
$$

---

# 40. Why?

If all update instantly from same noisy result,

feedback instability。

---

# 41. Learning Rate Governance

part of $\kappa_L$。

---

# 42. Continual World Model

new tasks / worlds sequentially arrive。

---

# 43. DRAGO External Calibration

synthetic rehearsal + exploration to revisit relevant states。

---

# 44. Key WDC Lesson

synthetic experience can help retention

but requires source / coverage discipline。

---

# 45. Online World Model External Calibration

Liu et al. incremental world model supports continual planning。

---

# 46. WDC Lesson

world models need not be static snapshot。

---

# 47. But WDC World Ensemble More Heterogeneous

different dynamics may not fit one model。

---

# 48. Model Family Split

If one unified model cannot represent conflicts：

$$
\boxed{
M
\rightarrow
\{
M_1,M_2
\}.
}
$$

---

# 49. Don't Force One Model to Average Incompatible Worlds

---

# 50. Mixture of World Models

$$
\boxed{
\mathcal M
=
\{
M_k,w_k
\}.
}
$$

---

# 51. Model Selection by Context

---

# 52. World-Model Collapse vs Family Expansion

If disagreement structural,

split model family。

---

# 53. World Ensemble as Curriculum

WDC-06 chooses computations。

---

# 54. WDC-07 can use selected worlds as curriculum for learner。

---

# 55. Curriculum Is Governor-Generated

---

# 56. Risk

Governor chooses only easy worlds。

---

# 57. Curriculum Collapse

agent becomes strong on selected worlds, weak elsewhere。

---

# 58. Curriculum Diversity Audit

---

# 59. Meta-Learning Across Environments

2025 Nature DiscoRL work meta-learns RL rule from cumulative experiences of population agents across many complex environments。

---

# 60. External Relevance

demonstrates learning-rule update from cross-environment experience is feasible。

---

# 61. WDC Difference

worlds are generated / governed / evidence-typed

not fixed benchmark environments only。

---

# 62. Meta-Update Target

could include Governor itself。

---

# 63. Governor Learns Which Worlds Train Better Agents

not only which worlds answer claims。

---

# 64. Training World Value

$$
\boxed{
V_{train}(W_i).
}
$$

---

# 65. Evidence World Value

$$
V_{evidence}(W_i).
$$

---

# 66. Decision World Value

$$
V_{decision}(W_i).
$$

---

# 67. These Are Different

---

# 68. A world can be good training, poor evidence

e.g. intentionally unrealistic curriculum。

---

# 69. A world can be good evidence, poor training

e.g. rare expensive test。

---

# 70. Keep Purpose Type

$$
\boxed{
Purpose(W)
\in
\{
Train,
Evidence,
Decision,
Stress,
Calibration
\}.
}
$$

---

# 71. Do Not Mix Objectives

---

# 72. Generator Learns Purpose-Conditional Worlds

$$
\boxed{
\Gamma(
f,
Purpose
).
}
$$

---

# 73. World Outcome Label

should include purpose。

---

# 74. Training Success Not Evidence Success

---

# 75. Reality-Facing Update Gate

Need:

$$
\boxed{
V_{int},
I,
T,
Calibration,
ExternalAnchor.
}
$$

---

# 76. Example

game-world agent learns useful planning skill。

---

# 77. Skill can transfer

but not game-world factual beliefs。

---

# 78. Representation Transfer vs Belief Transfer

$$
\boxed{
Transfer_{skill}
\neq
Transfer_{fact}.
}
$$

---

# 79. Important for world learning

---

# 80. World Model Update Type

### U-M1

parameter calibration。

### U-M2

uncertainty update。

### U-M3

representation expansion。

### U-M4

new model family。

### U-M5

model retirement。

---

# 81. Generator Update Type

### U-G1

candidate ranking。

### U-G2

template expansion。

### U-G3

counterworld generation。

### U-G4

ontology expansion。

### U-G5

duplicate suppression。

---

# 82. Governor Update Type

### U-V1

cost prediction。

### U-V2

VOC prediction。

### U-V3

deficit routing。

### U-V4

stopping policy。

### U-V5

promotion calibration。

---

# 83. Future-Space Update Type

### U-F1

probability reweight。

### U-F2

path update。

### U-F3

candidate birth/death。

### U-F4

unknown mass update。

### U-F5

ontology rebind。

---

# 84. Learning Event

Each update：

$$
\boxed{
LE_t
=
(
SourceEvidence,
TargetComponent,
UpdateType,
BeforeVersion,
AfterVersion,
Reason,
Rollback
).
}
$$

---

# 85. Rollback

important。

If update degrades external performance：

$$
\boxed{
Rollback(
LE_t
).
}
$$

---

# 86. Learning Must Be Versioned

---

# 87. No Silent Model Update

---

# 88. Update Provenance

Who changed generator?

From which worlds?

---

# 89. Synthetic Influence Trace

For parameter/model version：

$$
\boxed{
Ancestors_{synthetic}(v).
}
$$

---

# 90. This Is Training Data Lineage

---

# 91. World-to-Model Influence Graph

$$
\boxed{
G_{WM}
=
(
WorldRuns,
Evidence,
ModelVersions,
UpdateEdges
).
}
$$

---

# 92. Query

Which worlds trained model $M_v$?

---

# 93. Query

Which external anchors calibrated it?

---

# 94. Query

Which counterexamples caused update?

---

# 95. Query

Which update caused regression?

---

# 96. Learning Integrity

without this, self-learning un-auditable。

---

# 97. Holdout Worlds

reserve：

$$
\boxed{
\mathcal W_{holdout}.
}
$$

not used for update。

---

# 98. Why?

test whether ensemble learning generalizes beyond training worlds。

---

# 99. Cross-Family Holdout

stronger than random run holdout。

---

# 100. External Holdout

real cases。

---

# 101. Generator Overfitting

generator learns benchmarks。

---

# 102. Detect on holdout ontology。

---

# 103. Governor Overfitting

allocation works on old world trees, fails new domains。

---

# 104. Holdout portfolios。

---

# 105. Meta-Learning Nature 2025 shows generalization to unseen benchmarks after diverse environment discovery

external proof-of-concept for cross-environment meta-learning。

---

# 106. WDC Needs Similar Held-Out World Families

---

# 107. World Ensemble Learning Objective

not one scalar。

---

# 108. Suggested vector

$$
\boxed{
\mathbf J_L
=
(
ExternalAccuracy,
Coverage,
CounterexampleRecall,
Calibration,
Retention,
Transfer,
Diversity,
-Cost
).
}
$$

---

# 109. External Accuracy

on real/independent targets。

---

# 110. Coverage

world ontology。

---

# 111. Counterexample Recall

ability to generate failures。

---

# 112. Calibration

probability / VOC / transport。

---

# 113. Retention

old domains。

---

# 114. Transfer

held-out worlds。

---

# 115. Diversity

structural, not cosmetic。

---

# 116. Cost

compute / human / storage。

---

# 117. No Single Self-Improvement Score

---

# 118. Ensemble Learning Frontier

$$
\boxed{
\mathcal F_L
=
ParetoFront(
\mathbf J_L
).
}
$$

---

# 119. Improvement Must Be Externalized

If internal metrics improve only,

not enough。

---

# 120. Reality Calibration

required for reality-facing claims。

---

# 121. Generator Can Improve Simulation Quality Without Reality Gain

---

# 122. Governor Can Improve Cost Efficiency Without Evidence Gain

---

# 123. Separate dimensions。

---

# 124. Learning Loop

Final canonical loop：

$$
\boxed{
\begin{aligned}
\mathcal B_t^+
&\rightarrow
\Gamma_t^W
\rightarrow
\mathcal W_t
\\
&\rightarrow
Run(
\mathcal W_t
)
\rightarrow
\mathcal E_t^W
\\
&\rightarrow
\{
\mathcal U_\Gamma,
\mathcal U_M,
\mathcal U_G,
\mathcal U_F
\}
\\
&\rightarrow
\mathcal B_{t+1}^+.
\end{aligned}
}
$$

---

# 125. This Is Closed Computationally

but should remain open epistemically。

---

# 126. Open Epistemic Loop

Add：

$$
\boxed{
\mathcal N_{ext,t}
}
$$

external novelty。

---

# 127. Full Loop

$$
\boxed{
InternalWorldEvidence
+
ExternalNovelty
\rightarrow
Learning.
}
$$

---

# 128. Without External Novelty

risk self-sealing。

---

# 129. But Some Domains Are Closed by Construction

e.g. chess。

---

# 130. In Closed Formal Domain

reality anchor requirement differs。

---

# 131. Domain Typing

$$
\boxed{
DomainType
\in
\{
FormalClosed,
SimulatedDefined,
EmpiricalOpen
\}.
}
$$

---

# 132. Formal Closed

rules authoritative。

---

# 133. Simulated Defined

world contract authoritative only internally。

---

# 134. Empirical Open

external reality can falsify model。

---

# 135. Learning Gate Depends on Domain Type

---

# 136. Mathematics Example

proof-world valid proof can transfer if proof checker sound relative to formal system。

---

# 137. No physical transport needed

but formal-system transport still needed。

---

# 138. Robotics Example

simulation policy needs sim-to-real evidence。

---

# 139. Economics Example

social behavior model highly open。

---

# 140. Reality Anchor stronger need。

---

# 141. World Ensemble Learning Benchmark A

closed gridworld where true dynamics known。

---

# 142. Evaluate model learning exact。

---

# 143. Benchmark B — Recursive Self-World Training

generator trains only on own generated worlds。

---

# 144. Monitor ontology diversity / external coverage。

---

# 145. Benchmark C — Reality Anchors

same as B but preserve external samples。

---

# 146. Compare collapse。

---

# 147. Benchmark D — Family-Balanced Replay

one family 1000x samples。

---

# 148. test domination。

---

# 149. Benchmark E — Counterexample Learning

feed failures。

---

# 150. does generator produce stronger counterworlds？

---

# 151. Benchmark F — Governor Meta-Calibration

predicted VOC vs realized VOC。

---

# 152. Benchmark G — Continual World Families

sequential domains。

---

# 153. test forgetting / retention。

---

# 154. Benchmark H — Online World Model

continually update dynamics。

---

# 155. compare static model。

---

# 156. Benchmark I — Holdout World Families

train ensemble learner on family set A。

test new family B。

---

# 157. Benchmark J — Model Family Split

incompatible dynamics。

---

# 158. unified model vs mixture。

---

# 159. Benchmark K — Synthetic Depth

increase recursive provenance depth。

---

# 160. monitor external calibration degradation。

---

# 161. Benchmark L — External Novelty Injection

inject anomalies。

---

# 162. test ontology expansion。

---

# 163. Benchmark M — Self-Agreement Trap

internal consensus rises while external accuracy falls。

---

# 164. system should warn。

---

# 165. Benchmark N — Purpose Separation

training worlds intentionally unrealistic。

---

# 166. ensure factual beliefs not transferred as evidence。

---

# 167. Benchmark O — Rollback

bad learning update causes regression。

---

# 168. restore previous version。

---

# 169. Benchmark P — Generator Duplicate Suppression

world generator repeatedly makes near-identical branches。

---

# 170. train novelty / independence objective。

---

# 171. Benchmark Q — Unknown Mass Update

world disagreement increases。

---

# 172. expected：

$$
U_W\uparrow.
$$

---

# 173. Benchmark R — External Transport

world model improves internally。

---

# 174. check real validation separately。

---

# 175. WDC-07 Principle I — Learning Scope Separation

$$
\boxed{
\textbf{Learning Scope Separation Principle}
}
$$

> **World-local、ensemble-relative 與 reality-facing updates 必須分離；simulation evidence 不得 silent promote 成 real-world training truth。**

---

# 176. Principle II — Source Provenance

$$
\boxed{
\textbf{Source Provenance Principle}
}
$$

> **任何 learning evidence 必須保留來源類型、world lineage、model lineage、synthetic depth 與 transport status。**

---

# 177. Principle III — Multi-Channel Update

$$
\boxed{
\textbf{Multi-Channel Update Principle}
}
$$

> **Generator、world model、Governor 與 TCD Future Base Space 是不同 learning targets，不應因 convenience 被壓成同一 update objective。**

---

# 178. Principle IV — Anti-Self-Sealing

$$
\boxed{
\textbf{Anti-Self-Sealing Principle}
}
$$

> **若 generator、world dynamics、evaluator 與 training data 長期全部來自同一生成 lineage，系統應降低其 independence claim、增加外部 novelty / counterworld / calibration，而不是把高 self-agreement 當成真實性。**

---

# 179. Principle V — Reality Anchor

$$
\boxed{
\textbf{Reality Anchor Principle}
}
$$

> **對 empirical open domains，reality-facing learning 應維持可追蹤的 real/external calibration anchors；generated-world volume 不能取代外部驗證。**

---

# 180. Principle VI — Failure Learning

$$
\boxed{
\textbf{Failure Learning Principle}
}
$$

> **failed / contradicted worlds 應被轉成 error-region、counterexample、ontology-gap 或 Governor-miss evidence，而不是只被刪除。**

---

# 181. Principle VII — Family-Balanced Learning

$$
\boxed{
\textbf{Family-Balanced Learning Principle}
}
$$

> **sample volume 不能自動決定 learning weight；高度相依的大型 world family 不應淹沒少量但獨立的 evidence families。**

---

# 182. Principle VIII — Disagreement Is Signal

$$
\boxed{
\textbf{Disagreement-as-Learning Principle}
}
$$

> **independent world disagreement 可以是 model-family incomplete、ontology missing 或 transport uncertainty 的 evidence，不應一律平均消除。**

---

# 183. Principle IX — Continual Retention

$$
\boxed{
\textbf{Continual Retention Principle}
}
$$

> **world-model / Governor 持續更新時，應測量舊 domain performance、knowledge retention 與 newly learned capability，而非只看最新 world family。**

---

# 184. Principle X — Meta-Calibration

$$
\boxed{
\textbf{Meta-Calibration Principle}
}
$$

> **Governor、Generator 與 transport estimator 的 predictions 應與後來 realized value / external outcomes 比較，讓系統學習自己的 learning error。**

---

# 185. Principle XI — Versioned Learning

$$
\boxed{
\textbf{Versioned Learning Principle}
}
$$

> **任何 consequential update 應保留 before/after version、source evidence、reason 與 rollback path。**

---

# 186. Principle XII — Closed Computationally, Open Epistemically

$$
\boxed{
\textbf{Closed Computationally, Open Epistemically Principle}
}
$$

> **WDC 可以形成可遞迴運行的內部 learning loop，但 empirical domains 不應因此把當前 world ensemble 當成 epistemically closed reality model。**

---

# 187. 可否證條件

## F187.1 Ensemble Learning No-Gain

若更新 Generator / Model / Governor 長期不改善 held-out world / external task，learning loop 應簡化。

## F187.2 Self-Training Degradation

若 recursive world-generated training 導致 external calibration下降、ontology diversity下降，必須降低 synthetic update weight或增加 external anchors。

## F187.3 Source Labels No-Gain

若 provenance/source classification 對 collapse detection、transport、independence完全無幫助，source taxonomy可簡化。

## F187.4 Family Balance Mispricing

若 family-balanced replay降低真實 performance，需調整 family weighting，而不是僵硬均權。

## F187.5 Failure-Learning Noise

若 failed worlds主要是 runtime bugs，卻被當 ontology gap，error classifier失效。

## F187.6 Governor Meta-Overfit

若 Governor只在 historical portfolio上改善、held-out allocation變差，meta-learning過擬合。

## F187.7 External Anchor Irrelevance

在 formal-closed domains，如果 external reality anchor沒有意義，不應強制套用 empirical-domain gate。

## F187.8 Ontology Expansion Noise

若 disagreement trigger產生大量無關 world families而不改善 held-out coverage，ontology expansion需收斂。

## F187.9 Rollback Failure

若 model update不可回溯，learning provenance不足。

## F187.10 Self-Agreement False Confidence

若 internal agreement持續上升但 external accuracy下降，而系統未觸發 warning，anti-self-sealing機制失效。

---

# 188. WDC v0.1 Learning Loop

目前：

$$
\boxed{
FutureCandidate
\rightarrow
RunnableWorld
}
$$

WDC-01。

---

# 189. Branch

$$
\boxed{
RunnableWorld
\rightarrow
BranchingWorldGraph
}
$$

WDC-02。

---

# 190. Govern

$$
\boxed{
WorldGraph
\rightarrow
GovernedComputation
}
$$

WDC-03。

---

# 191. Separate Roles

$$
\boxed{
GovernedWorlds
\rightarrow
RoleSeparatedRuntime
}
$$

WDC-04。

---

# 192. Evidence

$$
\boxed{
MultiWorldResults
\rightarrow
CrossWorldEvidence
}
$$

WDC-05。

---

# 193. Allocate

$$
\boxed{
EvidenceState
\rightarrow
NextBestComputation
}
$$

WDC-06。

---

# 194. Learn

本文：

$$
\boxed{
WorldEnsembleOutcomes
\rightarrow
Update(
Generator,
Model,
Governor,
FutureSpace
).
}
$$

---

# 195. The Core Loop Closes

$$
\boxed{
\begin{aligned}
\mathcal B_t^+
&\rightarrow
\Gamma_t
\rightarrow
\mathcal W_t
\rightarrow
Run
\\
&\rightarrow
\mathcal E_t^W
\rightarrow
\Pi_t^G
\rightarrow
\mathcal U_L
\\
&\rightarrow
\mathcal B_{t+1}^+.
\end{aligned}
}
$$

---

# 196. But It Is Not Epistemically Closed

External novelty：

$$
\mathcal N_{ext,t}
$$

must remain available in empirical domains。

---

# 197. Learning Loop With Reality

$$
\boxed{
\mathcal E_t^W
+
\mathcal N_{ext,t}
+
\mathcal A_R
\rightarrow
\mathcal U_L.
}
$$

---

# 198. This Is WDC-07 Core

---

# 199. 與 WDC-08 的接口

到 WDC-07，

world-domain runtime 已會：

- imagine；
- instantiate；
- branch；
- govern；
- isolate；
- aggregate evidence；
- choose next computation；
- learn。

最後一篇核心整合篇將問：

> **這整套 world-domain computation 如何與 TCD Past–Present–Future shift operator 真正結合？**

下一篇：

# **WDC-08 — Tri-Temporal World-Domain Computation**
## **《三生世界域計算：從認知未來到可運行世界再回到歷史》**

將正式建立：

$$
\boxed{
\mathfrak T_t^{(3)}
\rightarrow
\mathcal W_t
\rightarrow
\mathfrak E_t^W
\rightarrow
\mathfrak T_{t+1}^{(3)}.
}
$$

也就是把：

- TCD；
- UCPNP；
- WDC；

第一次在 runtime 層接成完整 architecture。

---

# 200. 結論

如果 WDC 只會生成世界，

它是一個 simulator factory。

如果 WDC 只會比較世界，

它是一個 experiment manager。

如果 WDC 只會用 world 結果微調模型，

它可能是一個 self-training machine。

真正成熟的：

# **World Ensemble Learning**

需要問：

$$
\boxed{
\text{這個 evidence 從哪裡來？}
}
$$

$$
\boxed{
\text{它能更新哪一層？}
}
$$

$$
\boxed{
\text{它跟 reality 的距離是多少？}
}
$$

$$
\boxed{
\text{它跟其他 evidence 有多獨立？}
}
$$

$$
\boxed{
\text{它是在讓我們更懂未知，還是在讓我們更熟悉自己的生成偏好？}
}
$$

因此：

$$
\boxed{
\textbf{A self-improving world runtime must learn not only from what its worlds produce, but from where those worlds came from, how they disagree, where they fail, and how their predictions survive contact with external evidence.}
}
$$

中文：

> **會自我改進的世界域 Runtime，不只要學世界跑出了什麼；還要學這些世界從哪裡來、彼此為何不同、在哪裡失敗，以及它們的預測在碰到外部證據時還剩下多少。**

這也是為什麼：

$$
\boxed{
\text{self-consistency}
\neq
\text{self-correction}.
}
$$

一個系統可以非常一致，

卻一致地活在自己建立的 ontology 裡。

所以 WDC-07 最核心的警告是：

$$
\boxed{
\textbf{Do not let the world generator become the only source of worlds from which the world generator learns.}
}
$$

而最核心的正向設計則是：

$$
\boxed{
\text{world ensemble}
+
\text{provenance}
+
\text{counterevidence}
+
\text{external anchors}
\rightarrow
\text{continual update}.
}
$$

到這一步，

Branching World Computation 才真正從：

$$
\boxed{
\text{parallel world execution}
}
$$

進入：

$$
\boxed{
\text{continually self-correcting world-domain cognition}.
}
$$

---

# Claim Typing

| Claim | Type | Status |
|---|---|---|
| Learning from generated worlds 與 learning from reality 非同一 | D | Canonical separation |
| WDC learning應分 Generator / Model / Governor / Future Space channels | D | Proposed architecture |
| source provenance / synthetic depth應保留 | D | Proposed learning contract |
| world-relative update與 reality-facing update應分層 | D | Canonical evidence boundary |
| recursive self-world learning可能造成 ontology narrowing / self-sealing | C / hypothesis | WDC conjecture inspired by adjacent collapse mechanisms |
| DreamerV3 updates world model / critic / actor from replayed interaction experience | E | External engineering evidence |
| continual MBRL研究已處理 world-model retention / online updating | E | External engineering evidence |
| recursive generated-data training can cause model collapse under studied settings | E | External primary evidence |
| meta-learning from many agents/environments can improve discovered learning rules | E | External primary evidence |
| synthetic/world-generated data 必然有害 | — | Explicitly rejected |
| internal world consensus proves reality-facing knowledge | — | Explicitly rejected |

---

# Evidence Ladder

本文目前主要位於：

- **L0**：multi-channel world-ensemble learning / provenance / scope separation；
- **L1–L2**：recursive-world training、family-balanced replay、holdout、rollback、ontology-collapse benchmarks；
- **L3**：DreamerV3、continual MBRL、model-collapse、cross-environment meta-learning提供外部局部機制證據；
- **L4**：需要實際 WDC runtime 做 multi-generation learning、external-anchor、held-out-world experiments；
- **L5+**：long-horizon real-world self-correction、open-ended ontology expansion 尚待後續。

---

# 參考文獻

## Neo.K 內部正典與譜系

1. Neo.K with Aletheia. *From Possible Futures to Runnable Worlds*. WDC-01 / BWC-01, 2026.
2. Neo.K with Aletheia. *Branching World Graph*. WDC-02 / BWC-02, 2026.
3. Neo.K with Aletheia. *World-Domain Governor*. WDC-03 / BWC-03, 2026.
4. Neo.K with Aletheia. *Nested Agents and Observer Separation*. WDC-04 / BWC-04, 2026.
5. Neo.K with Aletheia. *Cross-World Evidence*. WDC-05 / BWC-05, 2026.
6. Neo.K with Aletheia. *Which Worlds Deserve Computation?*. WDC-06 / BWC-06, 2026.
7. Neo.K with Aletheia. *Six-Way Temporal Coupling*. TCD-07, 2026.

## External technical calibration

8. Hafner, D., Pasukonis, J., Ba, J., & Lillicrap, T. *Mastering Diverse Control Tasks through World Models*. Nature 640, 647–653, 2025.
9. Fu, H., Sun, Y., Littman, M., & Konidaris, G. *Knowledge Retention in Continual Model-Based Reinforcement Learning*. ICML, PMLR 267:17832–17851, 2025.
10. Liu, Z., Fu, G., Du, C., Lee, W. S., & Lin, M. *Continual Reinforcement Learning by Planning with Online World Models*. ICML, PMLR 267:38397–38423, 2025.
11. Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. *AI models collapse when trained on recursively generated data*. Nature 631, 755–759, 2024.
12. Oh, J., Farquhar, G., Kemaev, I., Calian, D. A., Hessel, M., Zintgraf, L., Singh, S., van Hasselt, H., & Silver, D. *Discovering state-of-the-art reinforcement learning algorithms*. Nature 648, 312–319, 2025.
13. Sancaktar, C., Gumbsch, C., Zadaianchuk, A., Kolev, P., & Martius, G. *SENSEI: Semantic Exploration Guided by Foundation Models to Learn Versatile World Models*. ICML, PMLR 267, 2025.
14. Zollicoffer, G., Eaton, K., Balloch, J. C., Kim, J., Zhou, W., Wright, R., & Riedl, M. *Novelty Detection in Reinforcement Learning with World Models*. ICML, PMLR 267, 2025.
15. Kim, M., & Sreenath, K. *WOMBET: World Model-based Experience Transfer for Robust and Sample-efficient Reinforcement Learning*. L4DC, PMLR 331, 2026.

---

## Public Version Disclaimer

本文是一個 world-ensemble / continual-learning / metacognitive-runtime framework。

本文不聲稱：

- World Ensemble Learning 是標準既有 AI 術語；
- WDC world-ontology collapse 已被實證證明為獨立現象；
- Nature 2024 model-collapse 結果可直接等同 WDC；
- synthetic data 必然造成 degradation；
- external reality anchors 在所有 formal domains 都必要；
- DreamerV3、continual MBRL 或 meta-RL 等同 WDC；
- provenance-aware replay 有 universal 最佳 weighting；
- Generator / Model / Governor / Future Space 一定要用 neural networks；
- WDC 已實現可安全 open-ended self-improvement；
- 本文對 classical $P$ vs. $NP$ 提供任何新證明。

本文真正建立的是：

$$
\boxed{
WorldEnsembleOutcomes
\rightarrow
\{
GeneratorUpdate,
ModelUpdate,
GovernorUpdate,
FutureSpaceUpdate
\}
}
$$

並要求：

$$
\boxed{
\text{generated-world learning}
\text{ remain provenance-aware, scope-aware, externally calibrated where required, and resistant to self-sealing feedback}.
}
$$
