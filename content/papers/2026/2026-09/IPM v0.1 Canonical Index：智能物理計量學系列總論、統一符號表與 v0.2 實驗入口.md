# IPM v0.1 Canonical Index：智能物理計量學系列總論、統一符號表與 v0.2 實驗入口

## Intelligence Physical Metrology v0.1 — Canonical Series Index, Unified Notation, and Experimental Entry Point

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**英文系列：** *Physical Metrology of Intelligence: From Minimal Semantic Execution to Quality and Computational Spacetime*  
**系列代號：** EML-IPM  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1 Canonical Index  
**日期：** 2026-09-02  
**狀態：** Theoretical Series 10/10 COMPLETE  
**用途：** 網站系列首頁、GitHub README、後續實驗與 v0.2 reference implementation 的 canonical entry point

---

# 0. 一句話版本

IPM 研究的不是「AI 有幾分聰明」，而是：

$$
\boxed{
\textbf{
一個智能系統在指定任務下，
以多少物理計算時空與多少外部鷹架，
完成多少有效語意工作，
最後產生多少可驗證品質？
}
}
$$

---

# 1. IPM Canonical Intelligence Event

$$
\boxed{
\mathfrak I_{\mathrm{IPM}}
=
(
\mathfrak T,
\mathfrak Q_{\mathrm{IPM}},
\mathbf N_{\mu},
\mathfrak P_{\mathrm{compute}},
\mathfrak S_C,
\mathfrak M
).
}
$$

其中：

- $\mathfrak T$：Task / Specification Object；
- $\mathfrak Q_{\mathrm{IPM}}$：Quality Object；
- $\mathbf N_{\mu}$：Semantic Work Object；
- $\mathfrak P_{\mathrm{compute}}$：Physical Computation Object；
- $\mathfrak S_C$：Scaffolding Capability Record；
- $\mathfrak M$：Measurement Metadata。

IPM 的核心不是找一個 AI IQ，而是比較：

$$
\boxed{
\mathfrak P_{\mathrm{compute}}
\rightarrow
\mathbf N_{\mu}
\rightarrow
\mathfrak Q_{\mathrm{IPM}}.
}
$$

---

# 2. 系列依賴圖

```text
Paper 01  Turn / LOOP / Single Pass
   │
   ├──> Paper 02  μI Semantic Execution
   │       └──> Paper 03  Cognition ↔ Neural Evidence
   │               └──> Paper 04  ATP / Joule / Thermodynamics
   │                       └──> Paper 05  Physical Cost + CST
   │
   ├──> Paper 06  Formal / Structured Quality
   │       └──> Paper 07  IBQF / Binary Human Residual
   │               └──> Paper 08  High-Ambiguity Quality Ontology
   │
   └──────── Paper 05 + Paper 08 ───────> Paper 09 Scaffolding
                                              └──> Paper 10 Unified IPM
```

三條主線：

$$
\boxed{
P01\rightarrow P02\rightarrow P03\rightarrow P04\rightarrow P05
}
$$

為 **Execution / Physical Line**；

$$
\boxed{
P06\rightarrow P07\rightarrow P08
}
$$

為 **Quality Line**；

$$
\boxed{
(P01,P05,P08)\rightarrow P09\rightarrow P10
}
$$

為 **Capability / Integration Line**。

---

# 3. Paper 01–10 Canonical Map

| Paper | 核心問題 | Canonical 輸出 |
|---|---|---|
| 01 | 一輪到底是哪一種一輪？ | $U,G,I,L,R,S,P$ ；ELI；Interaction Compression |
| 02 | 智能「算一次」是什麼？ | $\mu_I$ ； $N_\mu^{gross/eff}$ ；semantic state transition |
| 03 | 認知如何跨層對到神經事件？ | Cross-Level Triangulation；measurement grade |
| 04 | 神經事件如何對到 Joule？ | gross/base/marginal/attributed energy；Landauer type safety |
| 05 | FLOPs 之外的物理成本是什麼？ | $\mathbf C_P$ ； $\mathbf V_{CST}$ ； $\Theta_{CST}$ |
| 06 | 成果品質怎麼客觀量？ | Formal / Structured / Residual Quality；Hard Gate |
| 07 | 人類主觀品質怎麼低負擔量？ | IBQF／BRQM；binary/pairwise → latent quality |
| 08 | 高歧義成果有哪些品質維度？ | Typed Quality Ontology；Construct Graph |
| 09 | 拿掉 LOOP 還剩多少 native capability？ | SSR、SDR、SCM、scaffolding ablation |
| 10 | 如何統一比較智能產率？ | $\mathfrak I_{IPM}$ ；Pareto frontier；reporting standard |

---

# 4. Canonical Layer Stack

$$
\boxed{
\begin{aligned}
L_4 &: \text{Task Achievement / Quality}\\
L_3 &: \text{Semantic Execution}\\
L_2 &: \text{Algorithmic / Representational Realization}\\
L_1 &: \text{Physical Computation}\\
L_0 &: \text{Thermodynamic Realization}.
\end{aligned}
}
$$

重要：

$$
\boxed{
L_4\neq L_3\neq L_2\neq L_1\neq L_0.
}
$$

各層可以建立映射，但不可互相偷換。

---

# 5. 統一符號：Turn / Execution

| 符號 | 定義 |
|---|---|
| $X$ | Task input |
| $\mathcal S$ | Success specification |
| $W$ | Evaluation environment |
| $U$ | User Interaction Turns |
| $G$ | Generation Trajectories |
| $I$ | Model Invocations |
| $L$ | External Feedback Loops |
| $R$ | Retries / Rollouts |
| $S$ | Selection / Verification |
| $\tau$ | Single solving trajectory |
| ELI | Externally Loopless Intelligence |

最乾淨的 single-pass 條件：

$$
\boxed{
U=1,\quad G=1,\quad R=1,\quad L=0,\quad S=0.
}
$$

但：

$$
\boxed{
NoExternalLoop\neq NoSequentialComputation.
}
$$

---

# 6. 統一符號：Semantic Work

$$
\boxed{
\mu_I
=
\text{Minimum Intelligent Semantic Execution Unit}.
}
$$

Operationally：

$$
\boxed{
\mu_I:z_t\rightarrow z_{t+1}
}
$$

其中該 transition 必須是 task-relevant、causally useful、在指定 semantic resolution 下 operationally minimal。

$$
\boxed{
Token\neq\mu_I\neq FLOP.
}
$$

$$
\boxed{
N_\mu^{gross}
}
$$

表示候選語意活動總量；

$$
\boxed{
N_\mu^{eff}
}
$$

表示對成果具有有效因果貢獻的語意工作量。

$$
\boxed{
\eta_\mu
=
\frac{N_\mu^{eff}}{N_\mu^{gross}}.
}
$$

---

# 7. 統一符號：Cross-Level Realization

$$
\boxed{
\mu_I
\rightarrow
\rho_C(\mu_I)
\rightarrow
\rho_P(\mu_I)
\rightarrow
\rho_T(\mu_I).
}
$$

- $\rho_C$：algorithmic/computational realization；
- $\rho_P$：physical trace；
- $\rho_T$：thermodynamic realization。

因此：

$$
\boxed{
1\mu_I\neq Constant\ FLOPs
}
$$

且：

$$
\boxed{
1\mu_I\neq Constant\ Joule.
}
$$

---

# 8. 統一符號：Energy

$$
\boxed{
\mathcal E
=
(E_{gross},E_{base},E_{marg},E_{attrib},E_{thermo,min}).
}
$$

$$
\boxed{
E_{gross}
=
\int_{t_0}^{t_f}P_{system}(t)dt
}
$$

$$
\boxed{
E_{marg}
=
\int_{t_0}^{t_f}
[P_{system}(t)-P_{baseline}(t)]dt.
}
$$

Landauer：

$$
\boxed{
E_{erase,min}=k_BT\ln2
}
$$

但：

$$
\boxed{
LandauerBound\neq ActualIntelligenceCost.
}
$$

---

# 9. 統一符號：Physical Computation

$$
\boxed{
\mathbf C_P
=
(\mathbf O,\mathbf B_M,B_I,\mathbf B_N,V_M,V_C,T,\mathcal E).
}
$$

其中：

$$
\boxed{
\mathbf O
=(O_{FP64},O_{FP32},O_{BF16},O_{FP16},O_{INT8},\ldots)
}
$$

$$
\boxed{
\mathbf B_M
=(B_{reg},B_{cache},B_{sram},B_{hbm},B_{host}).
}
$$

Memory residency：

$$
\boxed{
V_M=\int M_{resident}(t)dt.
}
$$

Device time：

$$
\boxed{
V_C=\int D(t)dt.
}
$$

---

# 10. Computational Spacetime

資源場：

$$
\boxed{
\mathbf R(t)
=(r_C(t),r_M(t),r_N(t),r_S(t)).
}
$$

Raw CST：

$$
\boxed{
\mathbf V_{CST}
=
\int\mathbf R(t)dt
=
(V_C,V_M,V_N,V_S).
}
$$

IPM v0.1 的重要 type-safety rule：

$$
\boxed{
V_C+V_M+V_N+V_S
}
$$

在沒有 normalization 前沒有物理意義。

因此：

$$
\boxed{
CST=VectorFirst.
}
$$

---

# 11. Computational Spacetime Topology

$$
\boxed{
\Theta_{CST}
=
(T_{wall},T_{serial},P_{parallel},D_{peak},M_{peak},B_{peak},\Gamma_{comm}).
}
$$

所以：

$$
\boxed{
SameCSTVolume\neq SameCSTTopology.
}
$$

 $8GPU\times10s$ 與 $1GPU\times80s$ 可以具有相同 device-time volume，但 latency、peak capacity、communication 與 deployability 不相同。

---

# 12. 統一符號：Quality

Structured Quality：

$$
\boxed{
\mathbf Q_S
=(Q_C,Q_A,Q_K,Q_R,Q_B,Q_V,Q_P).
}
$$

對應：

- Correctness；
- Alignment；
- Completeness；
- Consistency；
- Robustness；
- Verifiability；
- Provenance。

三層品質：

$$
\boxed{
\mathcal Q_L=(Q_F,Q_S,Q_H).
}
$$

- $Q_F$：Formal Objective；
- $Q_S$：Structured Objective / Semi-Objective；
- $Q_H$：Human Residual。

---

# 13. High-Ambiguity Quality Ontology

$$
\boxed{
\mathcal Q[d,\tau,c,a]
}
$$

其中：

- $d$：domain / modality；
- $\tau$：task；
- $c$：context；
- $a$：audience / evaluator population。

$$
\boxed{
\mathcal Q
=
\mathcal Q_{core}
\oplus
\mathcal Q_{domain}
\oplus
\mathcal Q_{task}.
}
$$

品質測量鏈：

$$
\boxed{
Task
\rightarrow
Construct
\rightarrow
Indicator
\rightarrow
Item
\rightarrow
Observation
\rightarrow
LatentEstimate.
}
$$

因此：

$$
\boxed{
Construct\neq Indicator\neq Item\neq Metric.
}
$$

---

# 14. IBQF / BRQM

微觀回答：

$$
\boxed{
b_i\in\{0,1\}.
}
$$

宏觀 latent quality：

$$
\boxed{
\boldsymbol\theta\in\mathbb R^d.
}
$$

因此：

$$
\boxed{
BinaryObservation\neq BinaryPhenomenon.
}
$$

基本映射：

$$
\boxed{
\{0,1\}^{N}
\rightarrow
\widehat{\boldsymbol\theta}_H.
}
$$

母原則：

$$
\boxed{
\textbf{
評分者負責做容易、局部、具體的判斷；
測量系統負責做困難、全域、連續的量化。
}
}
$$

---

# 15. Scaffolding

$$
\boxed{
\mathbf S=(S_T,S_R,S_N,S_V,S_E,S_M,S_P).
}
$$

- $S_T$：Tool / External Information；
- $S_R$：Retry；
- $S_N$：Multi-sample / Best-of-N / Self-Consistency；
- $S_V$：Verifier / Critic；
- $S_E$：Environment Feedback；
- $S_M$：External / Persistent Memory；
- $S_P$：Planner / Controller。

Single-pass：

$$
\boxed{
\mathfrak Q_{SP}=\mathfrak Q(M,\mathbf0).
}
$$

Full system：

$$
\boxed{
\mathfrak Q_F=\mathfrak Q(M,\mathbf S_F).
}
$$

---

# 16. SSR / SDR / SCM

$$
\boxed{
SSR=\frac{Q_{SP}}{Q_F}
}
$$

$$
\boxed{
SDR=1-SSR.
}
$$

$$
\boxed{
SCM_j=\frac{C_j^F}{C_j^{SP}}.
}
$$

SSR/SDR 必須與 physical overhead 一起解讀，不能把 scaffold dependence 本身當成缺陷。

$$
\boxed{
Loop\neq Cheating.
}
$$

真正需要避免的是能力來源與成本被隱藏。

---

# 17. Intelligence Yield

若品質 projection 已公開：

$$
Q^*=\Pi_Q(\mathfrak Q),
$$

則：

$$
\boxed{
\mathbf Y_I
=
\left(
\frac{Q^*}{E_{marg}},
\frac{Q^*}{V_C},
\frac{Q^*}{V_M},
\frac{Q^*}{B_M},
\frac{Q^*}{B_N},
\frac{Q^*}{T}
\right).
}
$$

語意產率：

$$
\boxed{
Y_{\mu/E}=\frac{N_\mu^{eff}}{E_{marg}}
}
$$

$$
\boxed{
Y_{Q/\mu}=\frac{Q^*}{N_\mu^{eff}}.
}
$$

---

# 18. No Premature Scalarization Principle

$$
\boxed{
\textbf{
能保留向量時，不先壓成總分；
能保留結構時，不先壓成平均；
能保留不確定性時，不先假裝精確。
}
}
$$

Scalarization 只有在 task、policy、weights、gates 與 boundary 明示後才合法。

---

# 19. Pareto Comparison

若：

$$
\mathfrak Q_A\succeq\mathfrak Q_B
$$

且所有 relevant cost axes：

$$
C_{A,j}\le C_{B,j}
$$

並至少一軸嚴格較優，則：

$$
\boxed{
A\succ_{IPM}B.
}
$$

若不是 dominance：

$$
\boxed{
\text{保留 trade-off，不強迫總排名。}
}
$$

---

# 20. IPM Minimum Reporting Standard v0.1

最低報告欄位：

### Task
1. Task ID / Task Text  
2. Success Specification  
3. Evaluation Environment  
4. Quality Boundary  
5. Physical Boundary  

### Quality
6. Quality Schema  
7. Ontology Version  
8. Hard Gates  
9. Objective Verification  
10. Human Residual Protocol  
11. Quality Uncertainty  

### Execution
12. Single-Pass / Full-System Flag  
13. Model Invocation Count  
14. Trajectory Count  
15. Retry Count  
16. Tool Calls  
17. Verifier / Selector Class  

### Physical
18. Hardware  
19. Software / Runtime  
20. Wall Time  
21. Device Occupancy  
22. Peak Memory  
23. Memory Residency  
24. Memory Traffic  
25. Interconnect Traffic  
26. Energy Type  
27. Energy Boundary  

### Hidden / Discarded Work
28. Candidate Count  
29. Discarded Attempts  
30. Wasted Physical Cost  

### Measurement
31. Quality Grade  
32. Semantic Grade  
33. Energy Grade  
34. CST Grade  
35. Scaffolding Grade  
36. Scalarization / Projection Rule，如有。  

---

# 21. Canonical Comparison Protocol

1. Freeze Task： $\mathfrak T$。  
2. Freeze Quality Ontology： $\mathcal Q_{schema},Version_Q$。  
3. Run Single Pass： $(\mathfrak Q_{SP},\mathfrak P_{SP})$。  
4. Run Scaffolded： $(\mathfrak Q_F,\mathfrak P_F)$。  
5. Compute SSR / SDR / SCM / $\Delta\mathfrak P$。  
6. 可行時估 $\mathbf N_\mu$。  
7. 建立 $\mathcal F_{IPM}$。  
8. 若決策真的需要 scalar，才公開 $\Pi_Q,\Pi_C$。  
9. 報 measurement grades 與 uncertainty。  
10. 保存 raw trace / provenance。  

---

# 22. 系列核心 Invariants

$$
\boxed{Token\neq\mu_I\neq FLOP.}
$$

$$
\boxed{OneUserTurn\neq OnePhysicalTurn.}
$$

$$
\boxed{NoExternalLoop\neq NoSequentialComputation.}
$$

$$
\boxed{Pass@k\neq Pass@1.}
$$

$$
\boxed{SystemCapability\neq ModelNativeCapability.}
$$

$$
\boxed{SemanticWork\neq PhysicalWork.}
$$

$$
\boxed{FLOPs\neq PhysicalComputationalCost.}
$$

$$
\boxed{GrossEnergy\neq MarginalEnergy.}
$$

$$
\boxed{LandauerBound\neq ActualIntelligenceCost.}
$$

$$
\boxed{Quality\neq UniversalScalar.}
$$

$$
\boxed{FormalVerification\neq RealWorldGoalCorrectness.}
$$

$$
\boxed{BinaryObservation\neq BinaryPhenomenon.}
$$

$$
\boxed{Reliability\neq Validity.}
$$

$$
\boxed{Novelty\neq Creativity.}
$$

$$
\boxed{Loop\neq Cheating.}
$$

$$
\boxed{InvisibleOutput\neq ZeroCost.}
$$

$$
\boxed{SameQuality\neq SamePhysicalCost.}
$$

$$
\boxed{Scalarization\Rightarrow DeclaredPolicy.}
$$

$$
\boxed{Measurement\Rightarrow Uncertainty+Boundary+Version.}
$$

---

# 23. 五個 v0.1 可證偽命題

### F1 — Token Hypothesis

若 token 是良好普適智能工作單位，則：

$$
\frac{N_\mu^{eff}}{TokenCount}
$$

應跨 model / language / phrasing 相對穩定。

### F2 — FLOPs Sufficiency

若 FLOPs 足夠描述物理成本，控制 FLOPs 後：

$$
T,E,B_M,B_N,V_M
$$

不應仍有巨大獨立差異。

### F3 — Binary Burden Hypothesis

若 BRQM 的低負擔假說成立，適當 binary / pairwise protocol 應在至少部分場景改善 response time、consistency、dropout、predictive validity 或 fatigue。

### F4 — Scaffolding Separation

若 $Q_F-Q_{SP}$ 在多數任務與 compute budgets 顯著存在，則 native / system capability separation 具有實證必要性。

### F5 — Semantic Intermediate Utility

若 $\mathbf N_\mu$ 無法改善 efficiency prediction、error explanation、scaffold analysis 或 cross-architecture comparison，則 $\mu_I$ 應被修正甚至淘汰。

---

# 24. IPM v0.2：不要先做大平台

v0.2 的第一步應是最小可證偽實驗，而不是立刻做完整產品。

## Experiment A — Single-Pass vs Scaffolded

優先用 math / code / structured reasoning，因為 $Q$ 容易客觀驗證。

條件：

- A0：single pass；
- A1：longer internal budget；
- A2：multi-sample；
- A3：verifier；
- A4：tool / environment；
- A5：full agentic loop。

每層記：

$$
(Q_k,E_k,T_k,V_{C,k},V_{M,k},B_{M,k},B_{N,k}).
$$

## Experiment B — Binary vs Numeric Human Measurement

比較：

1. direct 0–10；
2. structured Yes/No；
3. adaptive pairwise。

量：response time、missingness、inconsistency、test-retest、predictive validity、fatigue。

## Experiment C — $\mu_I$ Operational Identification

選 proof steps、code repair、constraint puzzle，建立 candidate semantic transition，再做 ablation / counterfactual replacement。

## Experiment D — Physical Trace Alignment

先從同一台機器的：GPU power telemetry、latency、memory peak、memory bandwidth、device occupancy 做起。

v0.2 不必一開始宣稱 data-center-level energy。

## Experiment E — Token / FLOPs Proxy Failure Test

選相同 task quality、不同 language / verbosity / context / memory pressure 的執行，比較：

$$
TokenCount,FLOPs,E,T,B_M,N_\mu^{eff}.
$$

---

# 25. v0.2 推進順序

推薦：

$$
\boxed{
A\rightarrow D\rightarrow B\rightarrow C\rightarrow E.
}
$$

原因：

1. 先確認 scaffolding gap 是否穩定存在；
2. 建立 physical telemetry；
3. 驗證 IBQF/BRQM 的人類測量負擔假說；
4. 再攻最難的 $\mu_I$ ；
5. 最後挑戰 token / FLOPs proxy。

---

# 26. v0.2 最小 Run Schema

```yaml
ipm_version: "0.2-experimental"
task:
  id:
  specification_version:
  quality_schema_version:

execution:
  mode: single_pass | scaffolded
  trajectories:
  retries:
  tool_calls:
  verifier_passes:

quality:
  hard_gate:
  structured_vector:
  human_residual:
  uncertainty:
  grade:

semantic:
  mu_count_gross:
  mu_count_effective:
  confidence:
  grade:

physical:
  wall_time_s:
  energy_type:
  energy_j:
  device_time:
  memory_peak_bytes:
  memory_residency_byte_s:
  memory_traffic_bytes:
  interconnect_bytes:
  boundary:
  grade:

provenance:
  model:
  hardware:
  software:
  timestamp:
```

---

# 27. Versioning Rule

任何下列定義改變都應 bump version：

- $\mu_I$ definition；
- quality ontology；
- CST normalization；
- scaffold taxonomy；
- reporting schema。

因此：

$$
\boxed{
MeasurementDefinitionChange\Rightarrow VersionChange.
}
$$

---

# 28. 系列最終母命題

$$
\boxed{
\textbf{
智能不只在於能否得到答案，
還在於一個物理世界中的系統，
為了得到這個答案，
究竟必須執行多少有效語意工作，
占用多少計算時空，
消耗多少能量，
依賴多少外部鷹架，
最後換回多少可驗證品質。
}
}
$$

---

# 29. Canonical Status

$$
\boxed{
\text{EML-IPM v0.1}
=
10\ Papers
+
Canonical\ Index
+
Unified\ Notation
+
Experimental\ Entry\ Point.
}
$$

下一個 canonical milestone：

# IPM v0.2 — Experimental Measurement Protocol

它的目的不是證明 IPM v0.1 正確，而是讓 IPM 的核心命題第一次真正有機會被：

$$
\boxed{
\textbf{支持、修正、或證偽。}
}
$$
