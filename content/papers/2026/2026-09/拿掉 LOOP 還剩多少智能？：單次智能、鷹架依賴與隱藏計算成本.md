# 拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本

## How Much Intelligence Remains Without the Loop? Single-Pass Capability, Scaffolding Dependence, and Hidden Computational Cost

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**系列編號：** EML-IPM  
**篇次：** Paper 09 / 10  
**文件編號：** EML-IPM-09  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開純理論論文／智能系統能力分解方法論  
**工程狀態：** 無 MVP；本文建立 controlled scaffolding ablation 與 single-pass capability accounting，並不主張 LOOP、tool use 或 verifier 本身屬於作弊

---

## 摘要

一個 AI 系統的最終成果可能來自底層模型第一次直接生成，也可能來自：

- 多條 rollout；
- self-consistency；
- best-of-N；
- verifier / judge；
- tool use；
- code execution；
- web search；
- external environment feedback；
- retry；
- reflection；
- persistent memory；
- planner–executor loop。

這些機制都可能真實提高系統品質。

因此真正的問題不是：

> 有 LOOP 的系統算不算智能？

而是：

$$
\boxed{
\textbf{
最終成果中的多少能力來自模型原生單次求解，
多少來自額外計算、外部資訊與鷹架？
}
}
$$

本文將智能系統寫成：

$$
\boxed{
\mathcal A=(M,\mathbf S)
}
$$

其中 $M$ 是底層模型，而：

$$
\boxed{
\mathbf S=
(
S_T,S_R,S_N,S_V,S_E,S_M,S_P
)
}
$$

分別代表：

- $S_T$：Tool / External Information；
- $S_R$：Retry；
- $S_N$：Multi-Sample / Best-of-N / Self-Consistency；
- $S_V$：Verifier / Critic；
- $S_E$：Environment Feedback；
- $S_M$：External / Persistent Memory；
- $S_P$：Explicit Planner / Controller。

最小外部鷹架狀態：

$$
\boxed{
\mathbf S_0=\mathbf0.
}
$$

完整系統狀態：

$$
\boxed{
\mathbf S_F.
}
$$

則：

$$
\boxed{
\mathfrak Q_{SP}
=
\mathfrak Q(M,\mathbf S_0)
}
$$

為 single-pass / native quality，

而：

$$
\boxed{
\mathfrak Q_F
=
\mathfrak Q(M,\mathbf S_F)
}
$$

為完整系統品質。

若使用 Paper 06–08 已明示的品質投影：

$$
Q_{SP}=\Pi_Q(\mathfrak Q_{SP}),
$$

$$
Q_F=\Pi_Q(\mathfrak Q_F),
$$

則本文定義：

$$
\boxed{
\Delta Q_S
=
Q_F-Q_{SP}
}
$$

為 **Scaffolding Gain**。

再定義：

$$
\boxed{
SSR
=
\frac{Q_{SP}}{Q_F},
\qquad Q_F>0
}
$$

為 **Scaffolding Survival Ratio**，

以及：

$$
\boxed{
SDR
=
1-SSR
=
\frac{Q_F-Q_{SP}}{Q_F}
}
$$

為 **Scaffolding Dependence Ratio**。

直觀而言：

- $SSR\rightarrow1$：拿掉外部鷹架後，大部分品質仍保留；
- $SSR\rightarrow0$：完整成果高度依賴外部 scaffold。

但 scalar SSR/SDR 只有在同一 task、同一 quality schema、同一 projection rule 與同一 evaluation boundary 下才可比較。

多維品質更安全地表示為：

$$
\boxed{
\boldsymbol{\Delta Q}_S
=
\mathbf Q_F-\mathbf Q_{SP}
}
$$

以及：

$$
\boxed{
\mathbf{SSR}
=
\left(
\frac{Q_{SP,1}}{Q_{F,1}},
\dots,
\frac{Q_{SP,d}}{Q_{F,d}}
\right).
}
$$

本文再將 Paper 05 的物理成本接入。

令：

$$
\boxed{
\mathfrak P_{SP}
}
$$

為 single-pass 的 Physical Computation Object，

$$
\boxed{
\mathfrak P_F
}
$$

為完整 scaffolded system 的物理成本。

則：

$$
\boxed{
\Delta\mathfrak P_S
=
\mathfrak P_F
\ominus
\mathfrak P_{SP}
}
$$

為 **Scaffolding Physical Overhead**。

 $\ominus$ 是 typed difference，不把不同量綱硬壓成一個數字。它可以分別包含：

$$
\Delta E_{\mathrm{marg}},
\quad
\Delta V_C,
\quad
\Delta V_M,
\quad
\Delta B_N,
\quad
\Delta T.
$$

於是我們能問：

$$
\boxed{
\textbf{
每增加一單位外部計算時空，
究竟換回多少成果品質？
}
}
$$

對任一成本軸 $C_j$：

$$
\boxed{
Y_S^{(j)}
=
\frac{
\Delta Q_S
}{
\Delta C_j
}.
}
$$

本文同時指出，簡單 remove-one ablation 不能在存在 scaffold interaction 時被當成唯一貢獻歸因。

例如 verifier 只有在多候選存在時才有東西可選，而 best-of-N 沒有 verifier 時又可能無法穩定挑中好候選。

因此：

$$
\boxed{
Contribution(S_i)
\neq
Q_F-Q_{-S_i}
}
$$

並不普遍成立。

本文提出 **Scaffolding Interaction Graph**：

$$
\boxed{
G_S=(V_S,E_S)
}
$$

以及 factorial ablation / Shapley-like attribution：

$$
\boxed{
\phi_i
=
\sum_{A\subseteq S\setminus\{i\}}
w(A)
[
Q(A\cup\{i\})-Q(A)
].
}
$$

完整 Shapley attribution 的 subset cost 可隨 scaffold 數量指數成長，因此實務上可以 sampling approximation，但必須報：

$$
\boxed{
U_{\phi}.
}
$$

本文進一步將「智能」拆成能力向量：

$$
\boxed{
\mathbf I
=
(
I_{SP},
I_L,
I_T,
I_V,
I_E
).
}
$$

其中：

- $I_{SP}$：Single-Pass Intelligence；
- $I_L$：Loop / Revision Intelligence；
- $I_T$：Tool Utilization Intelligence；
- $I_V$：Verification / Selection Intelligence；
- $I_E$：Environment Adaptation Intelligence。

因此：

$$
\boxed{
\text{High Scaffold Dependence}
\neq
\text{Low System Intelligence}.
}
$$

一個系統可能 single-pass 普通，但非常擅長搜尋、找工具、驗錯、從失敗恢復與重規劃。那是一種不同結構的智能。

真正應避免的是：

$$
\boxed{
\text{System Intelligence}
\rightarrow
\text{Model-Native Intelligence}
}
$$

的偷換。

本文並提出 **Task-Natural Scaffolding Principle**。

某些任務的本體就需要外部世界，例如：

- 最新新聞；
- 即時天氣；
- robot control；
- debugging；
- scientific experimentation。

此時：

$$
L=0
$$

不是「更高級」，而可能只是缺失必要資訊。

所以 single-pass benchmark 應測：

> 在固定、資訊充分的初始條件下，模型第一次求解能做到多好？

而 full-system benchmark 應測：

> 在資訊不完整或動態環境中，系統能多有效取得、驗證、更新與使用新資訊？

兩者都是合法智能，但必須分欄。

最後，本文建立：

$$
\boxed{
\mathfrak S_C
=
(
\mathfrak Q_{SP},
\mathfrak Q_F,
\boldsymbol{\Delta Q}_S,
\mathbf{SSR},
\mathfrak P_{SP},
\mathfrak P_F,
\Delta\mathfrak P_S,
G_S,
\boldsymbol{\phi},
\mathfrak P_{\mathrm{waste}},
Grade_S
).
}
$$

作為 **Scaffolding Capability Record**。

它同時回答：

1. 拿掉 LOOP 後還剩多少品質？
2. 加回 LOOP 後增加多少？
3. 為此多付出多少物理計算時空？
4. 哪些 scaffold 提供主要增益？
5. 是否存在 scaffold synergy / redundancy？
6. 系統提升究竟來自推理、資訊、選樣、驗證，還是純大量計算？

本文終端命題：

$$
\boxed{
\textbf{
LOOP 不是作弊；
隱藏 LOOP 的能力來源與物理成本，
才會讓「模型有多聰明」失去可比較性。
}
}
$$

---

# 1. 為什麼要拿掉 LOOP？

不是為了證明 LOOP 不是真智能。

而是要做：

$$
\boxed{
\text{capability decomposition}.
}
$$

---

# 2. 最終品質有多個來源

$$
\boxed{
Q_F
=
F(
M,
Tools,
Retries,
Rollouts,
Verifier,
Memory,
Environment,
Controller
).
}
$$

如果只報一個 benchmark score，我們不知道提升是：

- 模型變強；
- 算更多次；
- 查到更多資訊；
- verifier 更準；
- 重試更多次。

---

# 3. Single-Pass Baseline

最小 external scaffolding 應至少滿足：

- 一條 trajectory；
- 無 external tool feedback；
- 無 retry；
- 無 best-of-N；
- 無 independent verifier；
- 無完整候選後再重寫；
- initial context 固定。

得到：

$$
\boxed{
\mathfrak Q_{SP}.
}
$$

---

# 4. Full System

開啟實際產品使用的：

$$
\mathbf S_F.
$$

得到：

$$
\boxed{
\mathfrak Q_F.
}
$$

二者差距才是真正的 scaffold gain。

---

# 5. Scaffolding Gain

$$
\boxed{
\Delta Q_S
=
Q_F-Q_{SP}.
}
$$

若：

$$
\Delta Q_S\gg0,
$$

不表示模型很差，而表示 system harness 提供巨大增益。

---

# 6. Survival 與 Dependence

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

但必須寫：

$$
\boxed{
SSR
=
SSR(Task,Config,QualityProjection).
}
$$

---

# 7. 同一模型不同任務可完全不同

純數學：

$$
SDR_{math}\ll1
$$

可能成立。

最新新聞：

$$
SDR_{news}\approx1
$$

也可能成立。

因為最新資訊本來就不在 model static state 中。

---

# 8. 所以

$$
\boxed{
ScaffoldingDependence
\neq
ModelDefect.
}
$$

---

# 9. 七類 Scaffold

$$
\boxed{
\mathbf S
=
(
S_T,S_R,S_N,S_V,S_E,S_M,S_P
).
}
$$

Tool、Retry、Multi-sample、Verifier、Environment、Memory、Planner 應分開記錄。

---

# 10. Multi-Sample 為什麼重要？

若單次成功率為：

$$
p,
$$

在理想獨立 sampling 下：

$$
\boxed{
P(\ge1\ \text{success})
=
1-(1-p)^k.
}
$$

因此：

$$
\boxed{
Pass@k
\neq
Pass@1.
}
$$

---

# 11. Repeated Sampling 不是模型瞬間變強

它是在利用模型輸出 distribution：

$$
\boxed{
\text{distribution exploitation}.
}
$$

所以 benchmark 必須把：

$$
k
$$

一起報。

---

# 12. Self-Consistency

Self-consistency 生成多條 reasoning paths，再聚合最一致答案。

因此同時增加：

- trajectory count；
- compute；
- selection。

它是真實的 inference method，但不是 single trajectory。

---

# 13. Best-of-N

$$
Y_1,\ldots,Y_N
\rightarrow
Y^\*.
$$

最終能力其實來自：

$$
\boxed{
Generator
+
CandidateDistribution
+
Selector.
}
$$

---

# 14. Verifier Intelligence

模型可能不容易第一次生成正解，但非常會辨識哪個候選比較好。

所以：

$$
\boxed{
GenerationAbility
\neq
VerificationAbility.
}
$$

---

# 15. Tool Intelligence

Tool access 本身不等於能力。

真正能力包括：

- 知道何時需要工具；
- 選哪個工具；
- 問什麼；
- 怎麼理解結果；
- 怎麼整合證據。

所以：

$$
\boxed{
ToolAccess
\neq
ToolUtilizationIntelligence.
}
$$

---

# 16. ReAct 類 closed loop

$$
Reasoning
\rightarrow
Action
\rightarrow
Observation
\rightarrow
Reasoning.
$$

這更接近：

$$
\boxed{
I_L+I_T+I_E.
}
$$

而不是：

$$
I_{SP}.
$$

---

# 17. Tree Search / Tree of Thoughts

多路探索：

$$
\tau_1,\tau_2,\ldots
$$

並允許：

- evaluate；
- branch；
- backtrack；
- lookahead。

這是 search intelligence，不是單軌跡能力。

---

# 18. Reflexion 類方法

Trial 1 的 feedback 被寫入 episodic memory，再影響 Trial 2。

因此：

$$
\boxed{
Trial_2
}
$$

已不是與 Trial 1 相同資訊狀態下的 pass@1。

---

# 19. Test-Time Compute

應直接承認：

$$
\boxed{
Quality
=
F(
BaseModel,
TestTimeCompute
).
}
$$

所以 benchmark 不只要報 model name，還應報 inference compute budget。

---

# 20. Hidden Compute Problem

若只說：

> 模型一輪回答。

卻不報：

- samples；
- retries；
- verifier；
- tool calls；
- planning rounds；

那麼成果缺少能力來源 metadata。

---

# 21. 這不要求公開 private Chain-of-Thought

IPM 只要求 operational accounting：

- trajectory count；
- invocation count；
- retry count；
- tool call count；
- selection class；
- physical resource trace。

所以：

$$
\boxed{
TransparencyOfCompute
\neq
DisclosureOfPrivateReasoning.
}
$$

---

# 22. Controlled Ablation Ladder

本文提出：

### A0 — Native Single Pass

$$
\mathbf S=0.
$$

### A1 — Extra Internal Budget

單一 trajectory 可以更長，但仍無 external feedback。

### A2 — Multi-Sample

加入：

$$
S_N.
$$

### A3 — Verification

加入：

$$
S_V.
$$

### A4 — Tool / Environment

加入：

$$
S_T,S_E.
$$

### A5 — Full Agentic

加入：

$$
S_M,S_P
$$

與完整 feedback loops。

---

# 23. 每一層都同時測品質和成本

$$
\boxed{
(
\mathfrak Q_k,
\mathfrak P_k
).
}
$$

這形成：

$$
\boxed{
\mathcal R_S
=
\{
(C_k,Q_k)
\}_{k=0}^{K}
}
$$

——**Scaffolding Response Curve**。

---

# 24. Marginal Scaffolding Yield

$$
\boxed{
Y_{S,k}
=
\frac{
Q_{k+1}-Q_k
}{
C_{k+1}-C_k
}.
}
$$

若隨 scaffold 增加：

$$
Y_{S,k}\downarrow,
$$

代表 diminishing returns。

---

# 25. Brute-Force Intelligence Region

若：

$$
\Delta Q\ll1
$$

卻需要：

$$
\Delta C\gg1,
$$

則進入：

$$
\boxed{
\text{Brute-Force Intelligence Region}.
}
$$

---

# 26. Brute-Force Cost Profile

更安全地保留向量：

$$
\boxed{
\boldsymbol{BFI}
=
\left(
\frac{\Delta E}{\Delta Q},
\frac{\Delta V_C}{\Delta Q},
\frac{\Delta T}{\Delta Q},
\frac{\Delta B_M}{\Delta Q},
\ldots
\right).
}
$$

高值表示每增加少量品質，需要大量額外物理資源。

但：

$$
\boxed{
BruteForce
\neq
Useless.
}
$$

高價值任務可能值得大量計算。

---

# 27. Scaffold Cost Multiplier

若 single-pass 某成本軸非零：

$$
\boxed{
SCM_j
=
\frac{
C_j^F
}{
C_j^{SP}
}.
}
$$

例如：

$$
SCM_E=20
$$

代表 full system 的能源是 single-pass 的 20 倍。

---

# 28. SSR 必須和 SCM 一起看

例如：

$$
SSR=0.95,
\quad
SCM_E=20.
$$

表示：

> 花 20 倍能源換最後 5% 品質。

另一系統：

$$
SSR=0.5,
\quad
SCM_E=2.
$$

則可能是非常有效率的 scaffold。

---

# 29. Scaffolding Efficiency Profile

$$
\boxed{
\mathcal E_S
=
(
SSR,
SDR,
\mathbf{SCM},
\mathbf Y_S
).
}
$$

---

# 30. 四種直觀系統類型

### Type I — Native Strong

$$
SSR\uparrow.
$$

### Type II — Efficiently Scaffoldable

中等 SSR，但：

$$
\Delta Q/\Delta C\uparrow.
$$

### Type III — Compute-Hungry

品質依靠巨大 cost multiplier。

### Type IV — Scaffold-Dependent

$$
SSR\downarrow.
$$

但 full-system 仍可能極強。

---

# 31. Scaffold Interaction

假設 verifier 單獨：

$$
+2
$$

multi-sample 單獨：

$$
+3
$$

一起：

$$
+15.
$$

這表示：

$$
\boxed{
Interaction_{N,V}>0.
}
$$

---

# 32. 所以 remove-one 不等於唯一歸因

建立：

$$
\boxed{
G_S=(V_S,E_S)
}
$$

其中 edge 可表示：

- synergy；
- redundancy；
- prerequisite；
- antagonism。

---

# 33. Shapley-Like Attribution

$$
\boxed{
\phi_i
=
\sum_A
w(A)
[
Q(A\cup\{i\})-Q(A)
].
}
$$

它考慮多種 scaffold 加入順序。

但完整 subset evaluation 成本高，所以可以 Monte Carlo approximation，同時報：

$$
U_\phi.
$$

---

# 34. Physical Attribution 也可以分解

例如估：

$$
\phi_i^E,
\quad
\phi_i^T,
\quad
\phi_i^{V_C}.
$$

如此可以問：

> verifier 貢獻 10% 品質，是否卻用了 40% 額外能源？

---

# 35. Capability Vector

$$
\boxed{
\mathbf I
=
(
I_{SP},
I_L,
I_T,
I_V,
I_E
).
}
$$

因此「強」可以有不同結構。

---

# 36. Single-Pass Intelligence

問：

> 第一條求解軌跡，在固定資訊下直接能做到多好？

---

# 37. Loop Intelligence

問：

> 得到新 feedback 後能否正確修正？

---

# 38. Tool Intelligence

問：

> 能否選擇、使用與理解外部工具？

---

# 39. Verification Intelligence

問：

> 能否發現錯誤、比較候選與知道何時不可信？

---

# 40. Environment Intelligence

問：

> 世界改變後能否更新 state 與 plan？

---

# 41. Task-Natural Scaffolding

某些問題本來就需要外部 interaction。

最新資訊、robot control、debugging、實驗科學都屬此類。

所以：

$$
\boxed{
Loopless
\neq
SuperiorByDefinition.
}
$$

---

# 42. Information-Controlled Ablation

Tool gain 同時可能來自：

- 新資訊；
- 額外計算；
- iterative interaction。

所以工具實驗至少可以比較：

1. no tool；
2. tool 找到的 evidence 預先塞入 context；
3. one-shot tool access；
4. iterative tool loop。

---

# 43. 如果 evidence pre-supplied 已恢復大部分品質

主要 gain 來自：

$$
\boxed{
InformationAcquisition.
}
$$

---

# 44. 若 iterative tool loop 仍明顯更強

則：

- query reformulation；
- search strategy；
- evidence selection；

本身提供額外能力。

---

# 45. External Memory 也不是 Internal Learning

Persistent memory 改變了未來可取得資訊，但沒有因此自動改變 model weights。

所以：

$$
\boxed{
ExternalMemory
\neq
InternalLearning.
}
$$

---

# 46. Hidden Retry

如果產品 failure 後自動重試，而 benchmark 只記最後成功答案，就產生 survivorship bias。

因此應記：

$$
\boxed{
R_{\mathrm{attempted}},
R_{\mathrm{failed}},
R_{\mathrm{shown}}.
}
$$

---

# 47. 被丟掉的工作仍然耗物理資源

$$
\boxed{
\mathfrak P_{\mathrm{waste}}
=
\sum_{\mathrm{discarded\ attempts}}
\mathfrak P_i.
}
$$

所以：

$$
\boxed{
InvisibleOutput
\neq
ZeroCost.
}
$$

---

# 48. Selection Waste Ratio

若已明示某成本 scalarization：

$$
\boxed{
SWR
=
\frac{
C_{\mathrm{discarded}}
}{
C_{\mathrm{total}}
}.
}
$$

Best-of-100 中，最後只展示一個答案並不會讓另外 99 個候選的成本消失。

---

# 49. Scaffolding Measurement Grade

### S-Grade E — Unknown Harness

只知道最後答案。

### S-Grade D — Declared Components

知道有 tool / retry / verifier，但無完整計數。

### S-Grade C — Execution Trace

有 invocation、trajectory、tool、retry count。

### S-Grade B — Controlled Ablations

有 matched single-pass / scaffolded 比較。

### S-Grade A — Factorial / Interaction Analysis

能分析主要 scaffold 交互作用。

### S-Grade A+ — Physical-Causal Attribution

品質 ablation 與 synchronized physical cost attribution 同時存在。

---

# 50. Scaffolding Capability Record

$$
\boxed{
\mathfrak S_C
=
(
\mathfrak Q_{SP},
\mathfrak Q_F,
\boldsymbol{\Delta Q}_S,
\mathbf{SSR},
\mathfrak P_{SP},
\mathfrak P_F,
\Delta\mathfrak P_S,
G_S,
\boldsymbol{\phi},
\mathfrak P_{\mathrm{waste}},
Grade_S
).
}
$$

這是 Paper 09 的正式輸出。

---

# 51. Single-Pass Capability Frontier

在不同固定 compute budget $C$ 下：

$$
\boxed{
Q_{SP}(C).
}
$$

保持：

$$
L_{\mathrm{external}}=0.
$$

即可研究：

$$
\boxed{
\frac{dQ_{SP}}{dC}.
}
$$

---

# 52. 再與 scaffolded frontier 比較

$$
\boxed{
Q_F(C).
}
$$

以及：

$$
\boxed{
G_S(C)
=
Q_F(C)-Q_{SP}(C).
}
$$

這比只報單一 SDR 更完整。

---

# 53. 若 single-pass 很快飽和

但 scaffolded curve 持續上升，

代表 search、verification、environment feedback 對該模型特別重要。

---

# 54. 若兩條 curve 長期接近

代表 native trajectory 已保留大部分能力。

---

# 55. 十八個 Canonical Invariants

**Invariant 1**

$$
\boxed{
Loop
\neq
Cheating.
}
$$

**Invariant 2**

$$
\boxed{
SystemCapability
\neq
ModelNativeCapability.
}
$$

**Invariant 3**

$$
\boxed{
Pass@k
\neq
Pass@1.
}
$$

**Invariant 4**

$$
\boxed{
BestOfN
\neq
SingleTrajectory.
}
$$

**Invariant 5**

$$
\boxed{
GenerationAbility
\neq
VerificationAbility.
}
$$

**Invariant 6**

$$
\boxed{
ToolAccess
\neq
ToolUtilizationIntelligence.
}
$$

**Invariant 7**

$$
\boxed{
ScaffoldingDependence
\neq
SystemDefect.
}
$$

**Invariant 8**

$$
\boxed{
Loopless
\neq
SuperiorByDefinition.
}
$$

**Invariant 9**

$$
\boxed{
InvisibleOutput
\neq
ZeroCost.
}
$$

**Invariant 10**

$$
\boxed{
HiddenRetry
\neq
FreeRetry.
}
$$

**Invariant 11**

$$
\boxed{
ExternalMemory
\neq
InternalLearning.
}
$$

**Invariant 12**

$$
\boxed{
ToolGain
\neq
ReasoningGain.
}
$$

**Invariant 13**

$$
\boxed{
OneAtATimeAblation
\neq
UniqueAttribution.
}
$$

**Invariant 14**

$$
\boxed{
ComputeScaling
\neq
ModelScaling.
}
$$

**Invariant 15**

$$
\boxed{
SameFinalQuality
\neq
SameScaffoldingDependence.
}
$$

**Invariant 16**

$$
\boxed{
SameFinalQuality
\neq
SamePhysicalCost.
}
$$

**Invariant 17**

$$
\boxed{
TransparencyOfCompute
\neq
DisclosureOfPrivateReasoning.
}
$$

**Invariant 18**

$$
\boxed{
ScaffoldMeasurement
\Rightarrow
QualityAndCostTogether.
}
$$

---

# 56. 結論：真正要拿掉的不是 LOOP，而是能力來源的混淆

AI 系統使用：

- tools；
- search；
- verifier；
- retry；
- tree search；
- memory；

沒有任何本質問題。

對許多真實任務而言，這甚至是智能不可缺少的一部分。

真正的測量問題是：

$$
\boxed{
\textbf{
我們是否知道最後成果，
究竟由哪些能力與多少物理計算共同產生？
}
}
$$

如果模型：

$$
Q_{SP}=0.90
$$

完整 agent：

$$
Q_F=0.95,
$$

而只增加少量物理成本，

那代表：

> native capability 很強，scaffold 做了有效的最後修補。

如果：

$$
Q_{SP}=0.20
$$

完整 agent：

$$
Q_F=0.95,
$$

但需要：

- 100 rollouts；
- 多個 verifier passes；
- 多次 tool queries；
- 大量 discarded candidates；

它仍然可以是一個非常強的系統。

但它應被描述成：

$$
\boxed{
\text{highly scaffolded intelligent system}.
}
$$

不能被描述成：

> 底層模型第一次就有 0.95 的能力。

所以 SSR、SDR 不是用來貶低 agent。

它們描述的是：

$$
\boxed{
\text{intelligence source structure}.
}
$$

而：

$$
\boxed{
\Delta\mathfrak P_S
}
$$

描述：

> 為了把 native capability 放大成 system capability，物理世界額外付出了多少計算時空。

至此 IPM 已經擁有：

$$
\boxed{
\mathfrak P_{\mathrm{compute}}
}
$$

——物理成本；

$$
\boxed{
\mathbf N_{\mu}
}
$$

——有效語意工作；

$$
\boxed{
\mathfrak Q_{\mathrm{IPM}}
}
$$

——成果品質；

以及：

$$
\boxed{
\mathfrak S_C
}
$$

——鷹架依賴與能力來源。

最後只剩一件事：

把這些組成一個不會再次犯「用單一 proxy 代替智能」錯誤的統一框架。

因此 Paper 10 將問：

$$
\boxed{
\textbf{
一個答案，究竟值多少物理世界？
}
}
$$

也就是：

**《一個答案值多少物理世界？：智能產率的統一計量框架》**。

---

## 文獻基礎

[1] Chen, M. et al. (2021). *Evaluating Large Language Models Trained on Code*. arXiv:2107.03374.  
[2] Wang, X. et al. (2023). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. ICLR 2023. arXiv:2203.11171.  
[3] Yao, S. et al. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. NeurIPS 2023. arXiv:2305.10601.  
[4] Yao, S. et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023. arXiv:2210.03629.  
[5] Shinn, N. et al. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. NeurIPS 2023. arXiv:2303.11366.  
[6] Lightman, H. et al. (2023). *Let's Verify Step by Step*. arXiv:2305.20050.  
[7] Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*. arXiv:2408.03314.  
[8] Chen, Y., Pan, X., Li, Y., Ding, B., & Zhou, J. (2024). *Simple and Provable Scaling Laws for the Test-Time Compute of Large Language Models*. arXiv:2411.19477.

---

## 系列路徑

1. **Paper 01｜一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義**  
2. **Paper 02｜智能到底算了一次什麼？：最小智能語意執行單位的候選理論**  
3. **Paper 03｜從認知到神經元：人腦如何跨層測量智能計算**  
4. **Paper 04｜從神經元到焦耳：智能計算的能量、熱力學與物理下界**  
5. **Paper 05｜計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積**  
6. **Paper 06｜成果品質到底怎麼量？：從形式化正確性到結構化智能品質**  
7. **Paper 07｜不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估**  
8. **Paper 08｜自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間**  
9. **Paper 09｜拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本**  
10. **Paper 10｜一個答案值多少物理世界？：智能產率的統一計量框架**
