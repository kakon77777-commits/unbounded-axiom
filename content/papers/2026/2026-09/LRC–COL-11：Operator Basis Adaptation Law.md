# LRC–COL-11：Operator Basis Adaptation Law
## 複合語言的變動定律
### The Adaptation Law of Composite Operator Bases

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL 前十篇分別建立了語言—現實耦合、語言行動收益、最小與最大有效算子集、基底—深度—粒度交換律、靜態／動態有效區間、AI 學習時間、語義穩定步數、代際傳播與多 Agent 傳播拓撲。這些工作共同指出：一套面向 AI、人類與多 Agent 系統的複合 operator language 不可能被設計成一次性、固定、永久完備的靜態字典。

真正需要的是一套**語言基底的變動定律**：

> **什麼時候應該創造新 operator？什麼時候某個反覆組合值得結晶成 stable macro？什麼時候兩個 operator 應合併？什麼時候過大的 operator 應拆分？語義漂移時應重新錨定還是淘汰？長期低效 operator 又應何時退出 stable language？**

本文提出 **Operator Basis Adaptation Law（OBAL）**，將複合算子語言表示為一個具有狀態、觀測、候選操作、約束、遷移成本與停止條件的動態系統。

核心狀態表示為：

$$
\boxed{
X_t
=
(
\mathcal O_t,
\mu_t,
A_t,
G_A(t),
G_O(t),
G_Q(t),
R_t,
H_t,
V_t
).
}
$$

其中：

- $\mathcal O_t$：當前 operator basis / library；
- $\mu_t$：workload / motif distribution；
- $A_t$：Agent capability / learning state；
- $G_A$：Agent communication graph；
- $G_O$：operator dependency / composition graph；
- $G_Q$：task dependency graph；
- $R_t$：retrieval / compiler / execution runtime；
- $H_t$：歷史 failure / usage / migration ledger；
- $V_t$：版本與治理狀態。

對每個候選語言變更：

$$
a
\in
\mathcal A
=
\{
Add,
Crystallize,
Merge,
Split,
Reground,
Deprecate,
Retire,
NoOp
\},
$$

本文定義：

$$
\boxed{
a_t^*
=
\arg\max_{a\in\mathcal A}
\left[
\mathbb E(
\Delta J_t
\mid
a,X_t
)
-
C_{migration}(a)
-
C_{uncertainty}(a)
\right]
}
$$

subject to：

$$
\boxed{
Coverage\ge\tau_C,\;
Fidelity\ge\tau_F,\;
Risk\le B_R,\;
Drift\le B_D,\;
LearningCost\le B_L.
}
$$

若沒有任何候選操作有足夠正的淨增益：

$$
\max_a \Delta U(a)\le\tau_{change},
$$

則：

$$
\boxed{
NoOp / STOP.
}
$$

因此「什麼都不改」正式成為 adaptation law 的合法結果。

本文特別反對「自我進化＝不斷新增 skills」。2026 年 evolving-tool 與 continual-skill 研究已開始處理 toolset evolution、skill creation / selection / utilization / distillation、skill lifecycle management 與 skill fragmentation。近期 benchmark 更顯示，能力較弱的模型可能累積更大、更碎片化的 task-specific skill collections，而 explicit skill maintenance 並不總能穩定超越 context adaptation。這表示一個有效的 language-evolution algorithm 必須同時具備**創造與刪除能力、結晶與解結晶能力、局部創新與全局去重能力**。

本文因此提出七種核心變動操作的明確 Gate：

1. **Add**：出現新的不可充分表達 distinction / capability；
2. **Crystallize**：高頻 motif 的重複 composition 已具有穩定可重用價值；
3. **Merge**：兩 operator 高度重疊，且 critical distinction loss 可控；
4. **Split**：單一 operator semantic surface 過大，內部 modes 已形成可辨識 cluster；
5. **Reground**：operator 有價值但已偏離 semantic anchor；
6. **Deprecate**：邊際效用低於保留門檻，但尚有 legacy dependency；
7. **Retire**：低價值、低 criticality、低 dependency，且 migration / compatibility window 已完成。

本文再加入四個防振盪機制：**Hysteresis、Dwell Time、Cooldown、Change Budget**；以及兩時間尺度 adaptation：fast loop 處理 ephemeral / local macros，slow loop 才改 stable core 與 adaptation policy 本身。其總體目的不是追逐瞬時最優 operator set，而是讓整套語言長期停留在：

$$
\boxed{
V_{\tau}(t)
\subseteq
I_{\mathcal O}^{D}(t)
}
$$

的高效 viability band 內，同時維持 bounded drift、bounded migration cost 與 cross-agent interoperability。

本文最終提出：

$$
\boxed{
\text{Good language evolution}
=
\text{novelty absorption}
+
\text{structural compression}
+
\text{semantic preservation}
+
\text{selective forgetting}.
}
$$

這是 LRC–COL 系列第一次從描述性理論正式進入可實作的 runtime / algorithm 核心。

---

## 關鍵詞

Operator Basis Adaptation Law；self-evolving agents；skill library；tool evolution；language evolution；macro crystallization；semantic drift；hysteresis；skill consolidation；AI-native language

---

# 1. 前十篇缺的最後一個動態核心

目前我們已經知道：

- operator 太少會失去 coverage；
- operator 太多會增加 selection / collision；
- basis 與 composition depth 交換；
- Agent 會學；
- language 會漂；
- communities 會形成 dialect；
- operator 會跨 generations 傳播。

但這仍然沒有告訴 runtime：

> **下一步現在到底要改什麼？**

因此需要：

$$
\boxed{
\mathcal O_t
\rightarrow
\mathcal O_{t+1}.
}
$$

---

# 2. Adaptation Law 不是單純新增公式

最粗錯誤模型：

```text
看到新任務
→ 新增 skill
→ skill library 變大
```

長期會造成：

$$
\boxed{
\text{Skill / Operator Fragmentation}.
}
$$

因為同一模式可能被重複寫成：

- task-specific skill；
- local variant；
- near-synonym；
- version fork。

所以 adaptation 必須是：

$$
\boxed{
\text{Add}
+
\text{Compress}
+
\text{Correct}
+
\text{Forget}.
}
$$

---

# 3. 2026 Evolving-Tool Environment 的現實對照

近期 tool-agent 研究已明確指出：

$$
\boxed{
\text{Tool Environment}
}
$$

不是 static。

會發生：

- tool addition；
- tool change；
- deprecation；
- overlap；
- fallback relation。

因此 agent 需要：

$$
\boxed{
\text{stability–adaptation balance}.
}
$$

這與本系列 dynamic completeness 的結論一致。

---

# 4. Documentation 也可以是 Adaptation Surface

2026 年 continual documentation adaptation 類工作提出：

> 不必每次重新訓練整個 Agent；可以修改 tool documentation / relation structure，使 Agent 適應新的 tool environment。

這支持：

$$
\boxed{
\text{Language Artifact}
}
$$

本身就是 adaptation layer。

對 COL 而言：

- operator definition；
- relation；
- fallback；
- preference；

都可以被 runtime 更新。

---

# 5. Skill Evolution 的三個耦合能力

最新 skill-evolution 工作也開始把：

$$
\boxed{
\text{Selection}
+
\text{Utilization}
+
\text{Distillation}
}
$$

視為同一個演化問題。

這和 COL 完全一致：

- operator 不是存了就好；
- 要找得到；
- 要用得對；
- 還要知道何時從 trajectory 蒸餾新 operator。

---

# 6. Skill Lifecycle

另一類 2026 工作已將 skill 視為：

$$
\boxed{
\text{long-lived, experience-aware, testable asset}.
}
$$

其 lifecycle 包括：

- creation；
- memory；
- management；
- evaluation；
- refinement。

本篇將這一方向進一步抽象成：

$$
\boxed{
\text{Operator Ecology}.
}
$$

---

# 7. ContinualSkillBench 的重要負結果

最新 continual-skill benchmark 報告一個對本系列非常重要的現象：

> 能力較弱模型容易累積更大、更碎片化的 task-specific skill collections。

而 explicit skill maintenance 的平均收益並不總是大幅超過直接利用 prior context / feedback 的 in-context adaptation。

這意味著：

$$
\boxed{
\text{More Explicit Skills}
\neq
\text{More Reusable Abstraction}.
}
$$

所以任何自動新增 operator 的演算法都必須有：

- reuse threshold；
- merge；
- fragmentation penalty；
- retirement。

---

# 8. Basis Adaptation State

本文定義：

$$
\boxed{
X_t
=
(
\mathcal O_t,
\mu_t,
A_t,
G_A(t),
G_O(t),
G_Q(t),
R_t,
H_t,
V_t
).
}
$$

---

# 9. Operator Library

$$
\mathcal O_t
=
\{O_1,\ldots,O_N\}.
$$

每個 operator 不只是 symbol。

---

# 10. Operator State Record

定義：

$$
\boxed{
Z_i(t)
=
(
f_i,
s_i,
c_i,
d_i,
l_i,
r_i,
\delta_i,
\rho_i,
\kappa_i,
v_i,
dep_i
).
}
$$

其中：

- $f_i$：usage frequency；
- $s_i$：success / fidelity；
- $c_i$：coverage contribution；
- $d_i$：depth saving；
- $l_i$：learning / selection cost；
- $r_i$：risk / criticality；
- $\delta_i$：semantic drift；
- $\rho_i$：collision / overlap；
- $\kappa_i$：reality coupling；
- $v_i$：version state；
- $dep_i$：dependency centrality。

---

# 11. Workload State

$$
\mu_t
$$

不只記 task frequency。

應記：

- recurring motifs；
- novel motifs；
- failed motifs；
- rare-critical motifs。

---

# 12. Motif

令：

$$
m
=
(O_{i_1},O_{i_2},\ldots,O_{i_k})
$$

是一個 recurrent composition pattern。

---

# 13. Motif State

$$
\boxed{
M_m(t)
=
(
f_m,
d_m,
F_m,
Y_m,
R_m,
C_m
).
}
$$

分別表示：

- frequency；
- depth；
- fidelity；
- action yield；
- risk；
- context dependence。

---

# 14. Failure State

$$
H_t
$$

保存：

- false selection；
- semantic collision；
- over-deep composition；
- drift；
- misuse；
- version mismatch；
- tool failure；
- cross-agent disagreement。

所以 adaptation 應是：

$$
\boxed{
\text{experience-conditioned}.
}
$$

---

# 15. Global Objective

令：

$$
\boxed{
J_t
=
\alpha Coverage_t
+
\beta Fidelity_t
+
\gamma Y_{L,t}
+
\eta Transfer_t
+
\theta Robustness_t
-
\lambda C_{learn,t}
-
\mu C_{select,t}
-
\nu C_{govern,t}
-
\xi Risk_t
-
\zeta Drift_t.
}
$$

---

# 16. 為什麼 J 不應只有 Task Accuracy？

如果只最佳化：

$$
TaskSuccess,
$$

runtime 可能：

- 新增很多 task-specific macros；
- 過擬合當前 workload；
- vocabulary 爆炸。

所以要懲罰：

$$
\boxed{
\text{Fragmentation}.
}
$$

---

# 17. Fragmentation Penalty

定義：

$$
\boxed{
C_{frag}
=
\alpha N_{low-reuse}
+
\beta N_{near-duplicate}
+
\gamma N_{single-task}.
}
$$

可加入：

$$
J_t.
$$

---

# 18. Candidate Adaptation Actions

本文核心 action set：

$$
\boxed{
\mathcal A
=
\{
Add,
Crystallize,
Merge,
Split,
Reground,
Deprecate,
Retire,
NoOp
\}.
}
$$

---

# 19. NoOp 不是失敗

如果：

$$
\max_a
\mathbb E[\Delta J(a)]
\le
\tau_{change},
$$

則：

$$
\boxed{
NoOp.
}
$$

因為：

> 不需要每天進化。

---

# 20. Change Utility

對候選 action：

$$
a,
$$

定義：

$$
\boxed{
\Delta U(a)
=
\mathbb E[
J(X_{t+1})-J(X_t)
\mid a
]
-
C_{migration}(a)
-
C_{uncertainty}(a).
}
$$

---

# 21. Adaptation Law

因此：

$$
\boxed{
a_t^*
=
\arg\max_{a\in\mathcal A}
\Delta U(a).
}
$$

只有：

$$
\Delta U(a_t^*)>\tau_{change}
$$

才執行。

---

# 22. 硬約束

即使：

$$
\Delta U>0,
$$

如果破壞：

$$
Risk\le B_R
$$

或：

$$
Fidelity\ge\tau_F,
$$

仍不能 deploy。

因此：

$$
\boxed{
\text{Utility Optimization}
+
\text{Hard Semantic / Risk Constraints}.
}
$$

---

# 23. ADD

## 問題

什麼時候應創造全新 operator？

---

# 24. ADD 的最低理由不是「新任務」

因為新任務可能只是舊 operators 的新組合。

所以：

$$
\boxed{
\text{Novel Task}
\neq
\text{Novel Operator}.
}
$$

---

# 25. ADD Trigger

候選：

1. 新 semantic distinction 無法由現 basis 低成本表達；
2. 新 capability / tool 無任何合理映射；
3. 現有 composition 必須長期越過 $d_{crit}$ ；
4. 現有 operator 若硬擴張會破壞 type / invariant。

---

# 26. Novelty Residual

令：

$$
R_{novel}(x)
$$

表示 task $x$ 在現有 basis 下無法被充分解釋的 residual。

若：

$$
\boxed{
R_{novel}>\tau_N
}
$$

才考慮 Add。

---

# 27. ADD Gain

$$
\boxed{
G_{add}
=
\Delta Coverage
+
\Delta Fidelity
+
\Delta DepthRescue
+
\Delta Yield.
}
$$

---

# 28. ADD Cost

$$
\boxed{
C_{add}
=
C_{learn}
+
C_{selection}
+
C_{version}
+
C_{collision}
+
C_{maintenance}.
}
$$

---

# 29. ADD Gate

$$
\boxed{
Add(O)
\iff
G_{add}-C_{add}>\tau_{add}
}
$$

且：

$$
CriticalDistinction(O)>0.
$$

---

# 30. 新 operator 先進 Experimental

不能：

$$
Birth
\rightarrow
Stable.
$$

應：

$$
\boxed{
Birth
\rightarrow
Experimental
\rightarrow
Candidate
\rightarrow
Stable.
}
$$

---

# 31. CRYSTALLIZE

Crystallize 和 Add 不同。

它不是新 capability。

而是把已存在的 recurrent composition：

$$
m
=
O_1\circ O_2\circ\cdots
$$

升格成：

$$
O_m.
$$

---

# 32. Crystallization Trigger

至少看：

- motif frequency；
- depth saving；
- fidelity gain；
- selection / context saving；
- cross-task reuse。

---

# 33. Crystallization Score

$$
\boxed{
S_{crys}(m)
=
f_m
[
\alpha\Delta d_m
+
\beta\Delta F_m
+
\gamma\Delta Y_m
+
\eta Transfer_m
]
-
C_{macro}(m).
}
$$

---

# 34. 必須跨 task Reuse

如果 motif：

$$
m
$$

只在一個 task 使用，

容易是：

$$
\boxed{
\text{Task Memorization}.
}
$$

所以 stable crystallization 應要求：

$$
ReuseDomains(m)\ge k.
$$

---

# 35. ContinualSkillBench 的直接提醒

如果 Agent 把每個 task 都 distill 成 skill，

skill library 會：

- 大；
- fragmented；
- low transfer。

所以：

$$
\boxed{
\text{Crystallization requires reuse evidence}.
}
$$

---

# 36. Crystallize Gate

$$
\boxed{
Crystallize(m)
\iff
S_{crys}(m)>\tau_C
\land
Reuse(m)\ge\tau_R
\land
F_m\ge\tau_F.
}
$$

---

# 37. Stable / Local / Ephemeral

Crystallized macro 依 reuse scope 分：

### Stable Global
跨 domains。

### Local
單 domain / project。

### Ephemeral
session。

這可避免 global basis 污染。

---

# 38. MERGE

若：

$$
O_i,O_j
$$

高度重疊，

可考慮：

$$
\boxed{
Merge(O_i,O_j)\rightarrow O_k.
}
$$

---

# 39. Merge 不是看名字像不像

需要同時看：

- semantic contract；
- behavior；
- type；
- boundary；
- usage context。

---

# 40. Semantic Overlap

定義：

$$
\boxed{
Sim_{ij}
=
Sim(
Sem(O_i),
Sem(O_j)
).
}
$$

---

# 41. Behavioral Overlap

$$
\boxed{
B_{ij}
=
P(
Behavior(O_i)=Behavior(O_j)
\mid ProbeSet
).
}
$$

---

# 42. Critical Distinction Loss

如果 merge 後會消失 distinction：

$$
d^*,
$$

定義：

$$
\boxed{
L_{dist}(i,j).
}
$$

---

# 43. Merge Gain

$$
\boxed{
G_{merge}
=
\Delta C_{select}
+
\Delta C_{version}
+
\Delta C_{learn}
+
\Delta CollisionReduction.
}
$$

---

# 44. Merge Cost

$$
\boxed{
C_{merge}
=
L_{dist}
+
C_{migration}
+
C_{legacy}
+
C_{retraining}.
}
$$

---

# 45. Merge Gate

$$
\boxed{
Merge
\iff
Sim_{ij}>\tau_S
\land
B_{ij}>\tau_B
\land
L_{dist}<\tau_D
\land
G_{merge}>C_{merge}.
}
$$

---

# 46. Merge 可能產生 God Operator

因此還需：

$$
SemanticSurface(O_k)\le B_S.
$$

若超過，

不 merge。

---

# 47. SPLIT

Split 是 Merge 的反向操作。

什麼時候一個 operator 太粗？

---

# 48. Split Trigger

候選：

- context-dependent error；
- parameter schema 爆大；
- modes 有明顯 clusters；
- high internal branching；
- boundary 常被誤用；
- 一個 name 實際代表多個不同行為。

---

# 49. Conditional Error Clusters

假設：

$$
Error(O\mid C_1)\gg0,
$$

$$
Error(O\mid C_2)\approx0.
$$

且不同 contexts 對應不同行為模式。

這表示：

$$
\boxed{
\text{semantic overloading}.
}
$$

---

# 50. Mode Clustering

如果 operator traces 可分：

$$
M_1,M_2,\ldots,M_k
$$

且群間行為距離高，

可以：

$$
\boxed{
Split(O)\rightarrow
\{O_1,\ldots,O_k\}.
}
$$

---

# 51. Split Gain

$$
\boxed{
G_{split}
=
\Delta Fidelity
+
\Delta BoundaryClarity
+
\Delta Learnability.
}
$$

---

# 52. Split Cost

$$
\boxed{
C_{split}
=
\Delta SelectionCost
+
\Delta Vocabulary
+
Migration.
}
$$

---

# 53. Split Gate

只有：

$$
G_{split}>C_{split}+\tau_S
$$

才拆。

---

# 54. REGROUND

Reground 用於：

> operator 還有價值，但意思已漂。

不是新建一個。

---

# 55. Reground Trigger

若：

$$
D_{sem}>B_D(O)
$$

但：

$$
Utility(O)>\tau_U,
$$

則：

$$
\boxed{
Reground(O).
}
$$

---

# 56. Reground 流程

1. reload canonical anchor；
2. replay invariant probes；
3. compare behavioral signature；
4. inspect drift source；
5. update examples / constraints；
6. revalidate cross-Agent use。

---

# 57. Reground vs Revision

若只是 Agent interpretation 漂，

保持：

$$
O@v.
$$

若 semantic contract 本身需改：

$$
O@v
\rightarrow
O@(v+1).
$$

---

# 58. DEPRECATE

Deprecate 表示：

> 不再推薦新使用，但仍需支持 legacy。

---

# 59. Deprecation Trigger

候選：

- usage 長期低；
- better successor 存在；
- high maintenance；
- high collision；
- obsolete tool / domain。

---

# 60. Deprecate 不等於 Remove

因為：

- old artifacts；
- historical logs；
- old Agents；

仍可能引用。

所以：

$$
\boxed{
\text{Deprecated}
\neq
\text{Deleted}.
}
$$

---

# 61. Hysteresis

加入門檻：

$$
\tau_{add}
>
\tau_{remove}.
$$

避免：

$$
Add
\leftrightarrow
Remove
$$

反覆震盪。

---

# 62. Deprecation Gate

如果：

$$
U_O<\tau_{deprecate}
$$

持續：

$$
W_D
$$

且有 replacement / derivation path，

則：

$$
\boxed{
Deprecate.
}
$$

---

# 63. RETIRE

Retire 是正式退出 active stable language。

---

# 64. Retirement Preconditions

至少要求：

1. 已 deprecated 足夠久；
2. no critical dependency；
3. migration 已完成；
4. old version 可 archival retrieval；
5. removing it 不破壞 coverage / risk threshold。

---

# 65. Retirement Gate

$$
\boxed{
Retire(O)
\iff
U_O<\tau_R
\land
Dependency(O)<\tau_D
\land
Criticality(O)<\tau_C
\land
MigrationComplete.
}
$$

---

# 66. Selective Forgetting

這使 language 擁有：

$$
\boxed{
\text{Selective Forgetting}.
}
$$

沒有忘記能力的語言，

最後會只增不減。

---

# 67. Forgetting 不是刪歷史

archive：

$$
O_{old}
$$

仍保留：

- definition；
- reason retired；
- migration；
- failures。

所以：

$$
\boxed{
\text{Operational Forgetting}
\neq
\text{Historical Erasure}.
}
$$

---

# 68. 七個操作構成 Lifecycle

$$
\boxed{
Add
\rightarrow
Crystallize
\rightarrow
Merge/Split
\rightarrow
Reground
\rightarrow
Deprecate
\rightarrow
Retire.
}
$$

不是每個 operator 都走完整鏈。

---

# 69. Operator Lifecycle State Machine

```text
Experimental
    ↓
Candidate
    ↓
Stable
 ↙   ↓   ↘
Split Reground Merge
    ↓
Deprecated
    ↓
Retired
```

---

# 70. Action Competition

同一時間：

$$
O
$$

可能同時滿足：

- Merge；
- Deprecate。

應比較：

$$
\Delta U.
$$

不能固定 priority 硬套。

---

# 71. Constraint Override

但 high-risk drift：

$$
D_{sem}\gg B_D
$$

可以 override utility ranking，

先：

$$
\boxed{
Freeze / Reground.
}
$$

---

# 72. Emergency Freeze

增加 runtime control：

$$
\boxed{
Freeze(O).
}
$$

它不是 basis-evolution 主操作，

而是 safety control。

停止：

- new executions；
- new propagation。

直到 review。

---

# 73. Adaptation Window

不能每次 task 後都改 stable basis。

定義：

$$
\boxed{
W_A
}
$$

收集一段 evidence 後再 adaptation。

---

# 74. Dwell Time

operator 進某狀態後至少停留：

$$
T_{dwell}.
$$

例如 Candidate 至少：

$$
100
$$

有效 uses 才可 Stable。

---

# 75. Cooldown

一次 Merge / Split 後：

$$
T_{cool}
$$

期間禁止再次結構改動，

除非 emergency。

防止連鎖震盪。

---

# 76. Change Budget

每個時間窗口：

$$
\boxed{
B_{change}
=
(
N_{add},
N_{merge},
N_{split},
N_{core-change}
).
}
$$

限制最大變更量。

---

# 77. 為什麼 Change Budget 必要？

如果：

$$
\mathcal O_t
$$

一次改 30%，

很難知道 performance 變化來自哪個 change。

因此：

$$
\boxed{
\text{Adaptation Observability}
}
$$

需要 bounded change.

---

# 78. Change Credit Assignment

每個 change：

$$
a_i
$$

需要記：

- reason；
- evidence；
- expected gain；
- observed gain；
- regressions。

形成：

$$
\boxed{
\text{Basis Revision Ledger}.
}
$$

---

# 79. Blame-Aware Evolution 的外部對照

2026 EVOTOOL 類工作已開始處理：

> long-horizon tool-use trajectory 中，究竟是哪個 policy module 造成失敗？

並使用 blame-aware mutation / diversity-aware selection 改進 tool-use policy。

這直接提醒：

$$
\boxed{
\text{Failure}
\rightarrow
\text{targeted mutation}
}
$$

比全局重寫更合理。

---

# 80. Operator-Level Blame

若 failure trace：

$$
O_1\rightarrow O_2\rightarrow O_3
$$

錯在：

$$
O_2,
$$

不要：

> 重寫整套語言。

只對：

$$
O_2
$$

或其 edge / contract adaptation。

---

# 81. Blame Distribution

定義：

$$
\boxed{
b_i
=
P(
O_i
\text{ caused failure}
\mid trajectory
).
}
$$

變更優先：

$$
b_i
$$

高者。

---

# 82. Diversity-Aware Candidate Selection

adaptation 可以產生多個候選：

$$
O'_1,O'_2,\ldots.
$$

不要只取第一個。

可以保留：

- 不同 granularity；
- 不同 type boundary；
- 不同 macro structure。

再 benchmark。

---

# 83. Candidate Branching

因此：

$$
\boxed{
O
\rightarrow
\{
O'_a,O'_b,O'_c
\}
}
$$

先在 experimental branch 測。

---

# 84. Stable Core 不能直接被一個 Task 修改

core operator：

$$
O_C
$$

需要：

- cross-task evidence；
- cross-Agent evidence；
- regression suite；
- migration plan。

---

# 85. Fast Loop / Slow Loop

本文提出兩時間尺度。

---

# 86. Fast Loop

每 task / session：

- ephemeral macro；
- retrieval ranking；
- local aliases；
- local failure memory。

記：

$$
\boxed{
\mathcal A_f.
}
$$

---

# 87. Slow Loop

每：

- release；
- evidence window；
- major workload shift；

才處理：

- stable Add；
- Merge；
- Split；
- Reground；
- Deprecate；
- Retire。

記：

$$
\boxed{
\mathcal A_s.
}
$$

---

# 88. Two-Timescale Adaptation

$$
\boxed{
\mathcal A_f
\gg
\mathcal A_s
}
$$

表示 fast changes 頻率高。

stable core 變慢。

---

# 89. MetaSkill-Evolve 的外部對照

2026 MetaSkill-Evolve 提出：

- task skills 快速演化；
- meta-skill（如何改 skill）慢速演化。

這與本文完全同構：

$$
\boxed{
\text{Basis Evolution}
}
$$

本身也需要更慢的：

$$
\boxed{
\text{Adaptation-Policy Evolution}.
}
$$

---

# 90. Meta-Adaptation

不只：

$$
\mathcal O_t
\rightarrow
\mathcal O_{t+1}.
$$

還有：

$$
\boxed{
\mathcal A_t
\rightarrow
\mathcal A_{t+1}.
}
$$

也就是：

> 如何決定 Add / Merge / Split 的方法本身也能改。

---

# 91. 但 Meta-Adaptation 不能和 Fast Loop 同速

否則：

- language 在變；
- adaptation rule 也一直變；

系統不可識別。

所以：

$$
\boxed{
T_{meta}
\gg
T_{basis}
\gg
T_{ephemeral}.
}
$$

---

# 92. 三時間尺度

### τ₁ — Ephemeral
session / local.

### τ₂ — Basis
stable operator evolution.

### τ₃ — Meta
adaptation-law revision.

這是：

$$
\boxed{
\text{Three-Timescale Operator Ecology}.
}
$$

---

# 93. Adaptation Policy State

$$
\boxed{
\Pi_t
=
(
\tau_{add},
\tau_{crys},
\tau_{merge},
\tau_{split},
B_D,
B_{change},
T_{dwell},
T_{cool}
).
}
$$

---

# 94. Meta-Update Gate

只有當：

- repeated adaptation failures；
- systematic overgrowth；
- systematic under-adaptation；
- chronic churn；

才更新：

$$
\Pi_t.
$$

---

# 95. Churn Rate

定義：

$$
\boxed{
R_{churn}
=
\frac{
N_{state\ transitions}
}{
Window
}.
}
$$

太高：

language 不穩。

---

# 96. Under-Adaptation Rate

如果新 motifs / failures 長期未被吸收：

$$
\boxed{
R_{under}
}
$$

高。

---

# 97. Over-Adaptation Rate

若大量 changes 後：

- utility 沒升；
- regressions 增加；

則：

$$
\boxed{
R_{over}.
}
$$

---

# 98. Meta Policy Objective

$$
\boxed{
J_{\Pi}
=
PerformanceGain
-
Churn
-
Regression
-
Migration
-
Fragmentation.
}
$$

---

# 99. Viability Band

前面 LRC–COL-06 已定義：

$$
V_{\tau}(t)
\subseteq
I_{\mathcal O}^{D}(t).
$$

adaptation law 的目的不是：

> 每一刻找 exact optimum。

而是：

$$
\boxed{
\mathcal O_t
\in
V_{\tau}(t).
}
$$

---

# 100. 如果仍在 Viability Band

即使：

$$
N\neq N^*,
$$

也可能：

$$
\boxed{
NoOp.
}
$$

這能大幅降低 churn。

---

# 101. Viability Exit

若：

$$
\mathcal O_t
\notin
V_{\tau}(t),
$$

才提高 adaptation urgency。

---

# 102. Urgency

定義：

$$
\boxed{
Urgency_t
=
D(
State(\mathcal O_t),
V_{\tau}(t)
).
}
$$

越遠：

- adaptation budget 可提高。

---

# 103. Dynamic Interval Constraint

必須保持：

$$
\boxed{
N_{\min}(t)
\le
N_t
\le
N_{\max}(t).
}
$$

如果：

$$
N_t<N_{\min},
$$

需要 expansion / crystallization。

如果：

$$
N_t>N_{\max},
$$

需要 merge / retire / hierarchy。

---

# 104. Active-Set Constraint

還需：

$$
\boxed{
N_A(q,t)\le B_A.
}
$$

否則不一定要刪 global operators，

可先改善 retrieval / routing。

---

# 105. 這是一個非常重要的分流判斷

如果 performance 差是因：

$$
N_A
$$

過大，

解法可能是：

$$
\boxed{
\text{Improve Retrieval}
}
$$

而不是：

$$
\boxed{
\text{Retire Useful Operators}.
}
$$

---

# 106. Root-Cause Routing

所以 adaptation 前必須先判斷 failure root：

```text
Coverage?
Learning?
Selection?
Composition?
Drift?
Execution?
Topology?
```

再決定 operator action。

---

# 107. Wrong-Layer Adaptation

例如：

> tool selection 很差。

如果根因是 retriever，

卻 Merge operators，

可能破壞 distinctions。

這是：

$$
\boxed{
\text{Wrong-Layer Adaptation}.
}
$$

---

# 108. Layer Diagnosis

定義：

$$
\boxed{
Root(F)
\in
\{
Operator,
Grammar,
Retriever,
Compiler,
Agent,
Topology,
Tool,
Environment
\}.
}
$$

只有：

$$
Root(F)=Operator
$$

或 operator interaction 才改 basis。

---

# 109. Evidence Requirement

adaptation 不能只根據一個 trajectory。

尤其 Add / Split。

需要：

- repeated evidence；
- contrastive success/failure；
- cross-task validation。

---

# 110. SkillCAT 類近期工作對應

2026 skill-evolution 研究開始強調：

- success/failure trajectory contrast；
- candidate patch replay；
- hierarchical merge；
- 不要把全部 skill content 無差別載入。

這與本文的 evidence gate、merge 與 active-set governance 高度同構。

---

# 111. Contrastive Causal Evidence

對候選 change：

$$
a,
$$

最好有：

$$
\boxed{
\Delta Outcome
\mid
\text{with }a
\quad
vs
\quad
\text{without }a.
}
$$

不是：

> 感覺這個 skill 有用。

---

# 112. Replay Gate

candidate operator change 先在：

- source-task clones；
- held-out tasks；
- adversarial cases；

重播。

只有不造成重大 regression 才 promote。

---

# 113. Regression Budget

定義：

$$
\boxed{
B_{reg}
}
$$

允許的最大 old-task performance loss。

---

# 114. Stability–Adaptation Frontier

新 change 提高新 domain：

$$
Gain_{new}>0
$$

卻讓 old：

$$
Loss_{old}>0.
$$

因此：

$$
\boxed{
\text{Adaptation}
\leftrightarrow
\text{Stability}.
}
$$

---

# 115. Continual Documentation Adaptation 的對照

2026 ContDa 類工作直接把：

- 新 capability discovery；
- old competence preservation；

分開量。

這提醒 COL 也應報：

$$
\boxed{
A_{new}
}
$$

與：

$$
\boxed{
S_{old}.
}
$$

不能只報平均。

---

# 116. Stability Metric

$$
\boxed{
S_{old}
=
1-
Loss(
OldTasks
).
}
$$

---

# 117. Adaptation Metric

$$
\boxed{
A_{new}
=
Gain(
NewTasks
).
}
$$

---

# 118. Adaptation Utility

$$
\boxed{
U_{adapt}
=
\alpha A_{new}
+
\beta S_{old}
-
\gamma C_{migration}.
}
$$

---

# 119. Skill1 類聯合演化的對照

skill selection、usage、distillation 其實互相依賴。

COL 同樣：

- retriever 決定哪些 operators 被用；
- usage frequency 決定哪些 motifs 看起來值得 crystallize；
- crystallization 又改變 retrieval distribution。

所以：

$$
\boxed{
\text{Selection}
\leftrightarrow
\text{Use}
\leftrightarrow
\text{Distillation}.
}
$$

---

# 120. Feedback Loop Bias

如果 retriever 永遠偏好某 operator：

$$
Usage(O)\uparrow,
$$

runtime 可能誤以為：

> 它很重要，

再進一步 crystallize / promote。

形成：

$$
\boxed{
\text{Popularity Feedback Loop}.
}
$$

---

# 121. Counterfactual Usage

因此 frequency：

$$
f_i
$$

應校正：

> 若所有 operators 有公平曝光，是否仍然高價值？

這可用：

- exploration；
- randomized routing；
- counterfactual evaluation。

---

# 122. Exploration Budget

保留：

$$
\boxed{
B_{explore}.
}
$$

讓低 usage 但 potentially useful operators 有機會被測。

---

# 123. Exploration 不應污染 High-Risk Execution

高風險：

- sandbox；
- simulation；

先探索。

---

# 124. Local Innovation before Global Adoption

新 operator：

$$
O_{new}
$$

先在 local community：

$$
C_i
$$

試驗。

若：

- stable；
- cross-task useful；
- bridge benefit；

才 promotion。

---

# 125. Topology-Aware Adaptation

因 LRC–COL-10：

$$
G_A
$$

會影響 operator birth / spread。

所以 adaptation law 需要 topology term。

---

# 126. Local Frequency ≠ Global Frequency

operator 在：

$$
C_i
$$

高頻，

全局可能低頻。

所以：

$$
\boxed{
f_i^{local}
\neq
f_i^{global}.
}
$$

---

# 127. Global Admission

進 common kernel 需要：

$$
\boxed{
CrossCommunityUtility(O)
}
$$

而不只單群 frequency。

---

# 128. Kernel Admission Gate

候選：

$$
O
\in\mathcal K
$$

要求：

1. 多 communities 需要；
2. semantics stable；
3. translation benefit；
4. low collision；
5. high critical distinction value。

---

# 129. Kernel Retirement 更嚴格

因 centrality 高：

$$
dep_i\uparrow.
$$

所以：

$$
\tau_{retire}^{kernel}
<
\tau_{retire}^{local}
$$

意思是需要更低效用才考慮淘汰。

---

# 130. Dependency Graph

operator graph：

$$
G_O=(V,E).
$$

如果：

$$
O_j
$$

大量依賴：

$$
O_i,
$$

則：

$$
dep_i
$$

高。

---

# 131. Centrality-Weighted Change Risk

$$
\boxed{
Risk_{change}(O_i)
\propto
Centrality_{G_O}(O_i).
}
$$

所以核心 primitive 改動需要更高 evidence。

---

# 132. Change Propagation Simulation

修改：

$$
O_i
$$

前，

在 dependency graph 上模擬：

$$
Affected(O_i).
$$

---

# 133. Affected Set

$$
\boxed{
A_i
=
\{
O_j:
O_i\leadsto O_j
\}.
}
$$

change cost 隨：

$$
|A_i|
$$

上升。

---

# 134. Tri-Graph Adaptation

LRC–COL-10 提出：

$$
\mathfrak G
=
(G_A,G_O,G_Q).
$$

因此 operator change 也應考慮：

- Agent communities；
- operator dependencies；
- task dependencies。

---

# 135. Tri-Graph Utility

候選：

$$
\boxed{
\Delta J(a)
=
f(
\Delta G_A,
\Delta G_O,
\Delta G_Q
).
}
$$

---

# 136. Task Motif Extraction

從：

$$
G_Q
$$

抽 repeated subgraphs。

如果 repeated subgraph 與 operator composition 相符，

它就是 crystallization candidate。

---

# 137. Graph-Motif Crystallization

$$
\boxed{
Subgraph(G_Q)
\rightarrow
OperatorMacro.
}
$$

這是未來非常直接的 algorithmic path。

---

# 138. Operator Graph Compression

Merge / crystallize 可以被視為：

$$
\boxed{
G_O
\rightarrow
G_O'
}
$$

的 graph compression。

---

# 139. Compression Quality

不能只最小化 node count。

要保持：

- reachability；
- type constraints；
- path semantics；
- critical distinctions。

---

# 140. Basis Adaptation 可以視為 Graph Rewrite System

每個 action：

- Add node；
- Contract subgraph；
- Merge nodes；
- Split node；
- Re-label / reground；
- deactivate node。

所以：

$$
\boxed{
\text{OBAL}
=
\text{constrained graph rewriting}.
}
$$

---

# 141. Rewrite Rule

抽象：

$$
\boxed{
G_{O,t+1}
=
\mathcal R_a(
G_{O,t},
Evidence_t
).
}
$$

---

# 142. Formal Grammar Update

有時 Add operator 也要求：

$$
G_t\rightarrow G_{t+1}.
$$

例如新 arity / type。

所以：

$$
\boxed{
\text{Operator Adaptation}
\neq
\text{Node-Only Adaptation}.
}
$$

---

# 143. Grammar Change Gate

grammar 比 operator 更 core。

需要：

- stronger evidence；
- larger regression suite；
- major version。

---

# 144. Runtime Adaptation vs Language Adaptation

如果問題可藉：

- better retriever；
- better compiler；

解決，

不要硬改 language。

因此：

$$
\boxed{
\text{Adapt the cheapest correct layer}.
}
$$

---

# 145. Minimum Intervention Principle

選擇：

$$
a
$$

時加入：

$$
C_{scope}(a).
$$

偏好：

> 能解決 failure 的最小結構修改。

---

# 146. Adaptation Scope

### S0
metadata / description。

### S1
operator example / boundary。

### S2
operator semantics。

### S3
basis structure。

### S4
grammar。

### S5
adaptation policy。

越高層：

$$
C_{migration}\uparrow.
$$

---

# 147. Escalation Rule

只有低層修正反覆失敗，

才升更高層。

這與 RLMM promotion 完全同構。

---

# 148. OBAL 自己也是 RLMM 的實例

觀察：

$$
Failure
$$

→ 把 operator 當 object；

若反覆：

→ 把 basis policy 當 object。

所以：

$$
\boxed{
RLMM
\rightarrow
OBAL
}
$$

不是兩套完全分離理論。

---

# 149. Operator Adaptation Loop

完整：

$$
\boxed{
Observe
\rightarrow
Diagnose
\rightarrow
Generate Candidate
\rightarrow
Replay
\rightarrow
Score
\rightarrow
Promote / Reject
\rightarrow
Monitor.
}
$$

---

# 150. Observe

收：

- usage；
- failure；
- drift；
- learning；
- topology；
- cost。

---

# 151. Diagnose

決定 root：

- missing capability；
- repeated motif；
- redundancy；
- overload；
- drift；
- obsolescence。

---

# 152. Generate Candidate

選：

$$
Add / Crystallize / Merge / Split / Reground / Deprecate / Retire.
$$

---

# 153. Replay

測：

- old tasks；
- new tasks；
- cross-domain；
- boundary；
- high-risk probes。

---

# 154. Score

算：

$$
\Delta U.
$$

---

# 155. Promote / Reject

若：

$$
\Delta U>\tau
$$

且 hard constraints pass：

promotion。

否則：

reject / remain experimental。

---

# 156. Monitor

deployment 後再追：

- regression；
- drift；
- usage；
- unexpected collision。

必要：

$$
Rollback.
$$

---

# 157. Rollback

每個 structural change 都應保留：

$$
\boxed{
RollbackPath.
}
$$

---

# 158. Atomic Change

一次 adaptation transaction：

$$
\boxed{
a_t
}
$$

最好可原子回退。

避免半完成 migration。

---

# 159. Version Graph

operator / basis version：

$$
G_V.
$$

edge：

- revise；
- merge；
- split；
- supersede；
- retire。

---

# 160. Provenance

每個 stable operator 要知道：

> 它從哪個 motif / failure / version 出生？

這是：

$$
\boxed{
\text{Evolutionary Provenance}.
}
$$

---

# 161. Why Provenance Matters

未來 AI 看到：

$$
O
$$

不只知道：

> 怎麼用。

還知道：

> 為什麼存在。

這降低 future legacy blindness。

---

# 162. Adaptation Memory

保存被拒絕的 changes：

$$
a_{reject}.
$$

避免未來重複提出同一壞改法。

---

# 163. Negative Evolution Memory

這是：

$$
\boxed{
\text{anti-regression knowledge}.
}
$$

---

# 164. Operator Fitness

可定義：

$$
\boxed{
\phi_i
=
\alpha Reuse_i
+
\beta Fidelity_i
+
\gamma Yield_i
+
\eta Transfer_i
+
\theta Criticality_i
-
\lambda LearnCost_i
-
\mu Collision_i
-
\nu Drift_i
-
\xi Maintenance_i.
}
$$

---

# 165. 但 Fitness 不能直接決定 Retire

因 dependency / criticality。

所以：

$$
\boxed{
\phi_i
}
$$

只是 summary。

---

# 166. Population of Operators

可以把：

$$
\mathcal O
$$

視為 population。

但不是 Darwinian 自由競爭。

因為我們有：

- semantic constraints；
- governance；
- safety；
- provenance。

所以是：

$$
\boxed{
\text{engineered operator ecology}.
}
$$

---

# 167. Selection Pressure

高：

- reuse；
- fidelity；
- transfer；

operators 生存。

高：

- collision；
- cost；
- drift；

operators 被 merge / retire。

---

# 168. Innovation Pressure

new domains 產生：

$$
Add.
$$

---

# 169. Compression Pressure

repeated motifs：

$$
Crystallize.
$$

redundancy：

$$
Merge.
$$

---

# 170. Differentiation Pressure

God operator / multimodal semantics：

$$
Split.
$$

---

# 171. Grounding Pressure

semantic drift：

$$
Reground.
$$

---

# 172. Forgetting Pressure

obsolete / low-value：

$$
Deprecate / Retire.
$$

---

# 173. 六種壓力總式

可以寫：

$$
\boxed{
\dot{\mathcal O}
=
P_{innovation}
+
P_{compression}
+
P_{differentiation}
+
P_{grounding}
-
P_{forgetting}
+
P_{governance}.
}
$$

符號化而非嚴格微分。

---

# 174. Language Growth Rate

cardinality：

$$
\boxed{
\dot N
=
B_{add}
+
B_{crys}
+
B_{split}
-
D_{merge}
-
D_{retire}.
}
$$

---

# 175. N 不應被直接控制

因為：

> 20 個高品質 operator 可能不夠；
> 200 個也可能很好。

runtime 應控制：

$$
\boxed{
J
}
$$

與：

$$
\boxed{
V_{\tau}.
}
$$

不是追固定 N。

---

# 176. Operator Carrying Capacity

可以借 ecology 類比：

$$
\boxed{
K_O(t)
}
$$

表示當前 Agent / runtime 可有效維持的 operator complexity capacity。

近似與：

$$
N_{\max}^{effective}(t)
$$

相接。

---

# 177. Overpopulation

若：

$$
N_t>K_O(t),
$$

產生：

- selection；
- collision；
- maintenance；

壓力。

---

# 178. Underpopulation

若：

$$
N_t<N_{\min}(t),
$$

產生：

- excessive depth；
- missing distinctions。

---

# 179. Homeostatic Regulation

因此 OBAL 是：

$$
\boxed{
\text{language homeostasis}.
}
$$

讓語言在：

$$
[N_{\min},N_{\max}]
$$

內自調節。

---

# 180. But Not Static Homeostasis

因：

$$
N_{\min}(t),N_{\max}(t)
$$

自己會動。

所以是：

$$
\boxed{
\text{moving-target homeostasis}.
}
$$

---

# 181. Dynamic Target

$$
\boxed{
\mathcal O_t
\in
V_{\tau}(t)
}
$$

是最終控制目標。

---

# 182. Candidate Algorithm v0.1

```text
INPUT:
  Current operator basis O_t
  Usage/failure window H_t
  Workload motifs M_t
  Drift/learning/selection metrics
  Agent/topology/runtime state

1. Estimate current viability:
   Nmin(t), Nmax(t), V_tau(t)

2. Diagnose failures by layer:
   operator / grammar / retrieval / agent / topology / environment

3. Extract candidate motifs and redundancies.

4. Generate candidate actions:
   Add
   Crystallize
   Merge
   Split
   Reground
   Deprecate
   Retire

5. For each candidate:
   estimate ΔCoverage
   estimate ΔDepth
   estimate ΔFidelity
   estimate ΔYield
   estimate ΔLearningCost
   estimate ΔSelectionCost
   estimate ΔMigration
   estimate ΔRisk
   estimate ΔDrift

6. Reject candidates violating hard constraints.

7. Replay remaining candidates on:
   regression
   held-out
   boundary
   high-risk
   cross-agent suites

8. Compute ΔU.

9. If max ΔU <= τ_change:
   NOOP / STOP.

10. Otherwise choose best bounded candidate,
    respecting hysteresis, dwell time,
    cooldown, and change budget.

11. Apply candidate in experimental/candidate layer.

12. Monitor post-change behavior.

13. Promote to stable only after stability window.

14. Preserve rollback + provenance + rejected alternatives.
```

---

# 183. 這不是聲稱已是最佳 Algorithm

OBAL v0.1 是：

$$
\boxed{
\text{reference control law}.
}
$$

後續可替換：

- heuristic；
- Bayesian；
- RL；
- evolutionary；
- graph optimization；
- multi-objective search。

---

# 184. Heuristic Controller

最容易第一版實作。

優點：

- 可解釋；
- 易除錯。

---

# 185. Bayesian Controller

對：

$$
\Delta U
$$

保留 uncertainty posterior。

適合 evidence 少時。

---

# 186. Reinforcement-Learning Controller

將：

$$
a_t
$$

視為 action，

長期：

$$
J
$$

為 reward。

但 credit assignment 難。

---

# 187. Evolutionary Controller

同時保留多候選 language branches。

適合：

- non-differentiable；
- multi-objective。

但成本高。

---

# 188. Graph Optimization

若 basis 主要是 operator graph：

- motif compression；
- community detection；
- minimum cut；
- set cover；

可能直接有效。

---

# 189. Hybrid Controller

最可能實務化：

$$
\boxed{
\text{Heuristic Gates}
+
\text{Learned Scoring}
+
\text{Replay Verification}.
}
$$

---

# 190. 為什麼不是純 RL？

因 semantic / safety constraints 很難只靠 reward 保證。

所以：

$$
\boxed{
\text{Learned Adaptation}
+
\text{Hard Invariants}.
}
$$

---

# 191. Multi-Objective Rather Than Single Reward

保留：

$$
\mathbf J
=
(
Coverage,
Fidelity,
Yield,
Learning,
Selection,
Risk,
Drift,
Migration
).
$$

不要太早壓 scalar。

---

# 192. Pareto Candidate Selection

保留：

$$
\boxed{
\mathcal P_{change}
}
$$

Pareto-optimal candidates。

由 domain policy 選。

---

# 193. High-Risk Policy

偏：

- fidelity；
- drift；
- rollback。

---

# 194. Low-Risk High-Throughput

偏：

- yield；
- depth；
- latency。

---

# 195. Research Language

偏：

- novelty；
- branch preservation；
- transfer。

---

# 196. Static Core

低 change budget。

---

# 197. Adaptation Law 也需要 Benchmark

不能只看：

> 最終 task score。

要測：

- library growth；
- fragmentation；
- reuse；
- merge quality；
- regression；
- churn；
- cross-agent transfer。

---

# 198. OBAL-Bench Candidate Metrics

```text
Coverage
Operator Count
Effective Complexity
Reuse Rate
Novel-Task Gain
Cross-Task Transfer
Fragmentation
Collision
Average Depth
Learning Time
Selection Accuracy
Drift
Churn
Migration Cost
Rollback Count
Retired-but-Regretted Rate
```

---

# 199. Retired-but-Regretted Rate

如果 retire 後很快：

> 又需要重新建一個近似 operator，

表示 retirement 太激進。

定義：

$$
\boxed{
R_{regret}.
}
$$

---

# 200. Merge Regret

merge 後發現 critical distinction 消失。

---

# 201. Split Regret

split 後 selection entropy 大幅上升而 fidelity 沒改善。

---

# 202. Add Regret

新增後長期 low reuse。

---

# 203. Crystallization Regret

macro 高頻只是 workload temporary burst。

---

# 204. Adaptation Regret

總：

$$
\boxed{
Regret_A
=
\sum_t
[
J(a_t^*)-J(a_t)
].
}
$$

理論上可作 online-control 目標。

---

# 205. Future Online Adaptation

若 workload stream：

$$
x_1,x_2,\ldots
$$

持續到來，

OBAL 是：

$$
\boxed{
\text{online language-structure learning}.
}
$$

---

# 206. Concept Drift

workload distribution：

$$
\mu_t
$$

會變。

所以 old operator fitness：

$$
\phi_i(t)
$$

也會變。

---

# 207. Temporal Decay

usage 可用：

$$
\boxed{
f_i(t)
=
\sum_{k}
e^{-\lambda(t-k)}
Use_i(k).
}
$$

避免十年前高頻永遠影響現在。

---

# 208. 但 Criticality 不應 Decay 太快

emergency operator 即使低頻，

仍保留。

---

# 209. Two-Channel Value

$$
\boxed{
Value_i
=
FrequencyUtility_i
+
CriticalityUtility_i.
}
$$

---

# 210. Cold Storage

低頻但可能未來需要：

不必 Stable active。

可進：

$$
\boxed{
\text{Cold Operator Archive}.
}
$$

retrieval-only。

---

# 211. Hot / Warm / Cold

### Hot
active / resident.

### Warm
retrievable stable.

### Cold
archived legacy / rare.

這把 storage 與 active selection 解耦。

---

# 212. Memory Tiering 直接推高 Nmax

因：

$$
N_G
$$

大，

但：

$$
N_A
$$

小。

與 LRC–COL-04 完整接合。

---

# 213. Promotion Across Tiers

operator 可：

$$
Cold
\rightarrow
Warm
\rightarrow
Hot.
$$

依 workload。

---

# 214. Demotion

反過來：

$$
Hot
\rightarrow
Warm
\rightarrow
Cold.
$$

不一定直接 retire。

---

# 215. Tier Adaptation 比 Retire 更平滑

這可以降低：

$$
R_{regret}.
$$

---

# 216. 最終 Operator Ecology 架構

候選：

```text
Stable Kernel
  ├─ Hot Core
  ├─ Warm General Library
  └─ Cold Legacy / Rare-Critical Archive

Domain Dialects
  ├─ Stable Local
  └─ Experimental

Ephemeral Layer
  └─ Session / Task Macros

Adaptation Controller
  ├─ Add
  ├─ Crystallize
  ├─ Merge
  ├─ Split
  ├─ Reground
  ├─ Deprecate
  └─ Retire
```

---

# 217. Operator Basis Adaptation Law 的簡化母式

可以壓縮成：

$$
\boxed{
\mathcal O_{t+1}
=
\mathcal A(
\mathcal O_t,
U_t,
F_t,
L_t,
D_t,
G_t,
Y_t
).
}
$$

其中：

- $U_t$：usage；
- $F_t$：failure；
- $L_t$：learning；
- $D_t$：drift；
- $G_t$：topology / graphs；
- $Y_t$：action yield。

---

# 218. 更完整控制式

$$
\boxed{
a_t^*
=
\arg\max_{a\in\mathcal A}
\Big[
\mathbb E[
\Delta J
\mid
X_t,a
]
-
C_{migration}
-
C_{uncertainty}
\Big]
}
$$

subject to：

$$
\boxed{
\begin{aligned}
Coverage&\ge\tau_C,\\
Fidelity&\ge\tau_F,\\
Risk&\le B_R,\\
Drift&\le B_D,\\
LearningCost&\le B_L,\\
ChangeRate&\le B_{change}.
\end{aligned}
}
$$

---

# 219. STOP Rule

如果：

$$
\boxed{
\max_a\Delta U(a)\le\tau_{change}
}
$$

則：

$$
\boxed{
STOP / NOOP.
}
$$

這是整個 adaptation law 最容易被忽略、但最重要的部分之一。

---

# 220. 沒有 STOP 的自我進化

會：

$$
\boxed{
\text{evolve itself into complexity}.
}
$$

而不是變好。

---

# 221. 十五個正式命題

## OB-P1 — Evolution Requires Forgetting
有效 operator ecology 必須同時支援 creation 與 selective retirement，否則 library 將長期碎片化。

## OB-P2 — Novel Task ≠ Novel Operator
新任務不足以構成 Add 理由，只有不可低成本表達的新 distinction / capability 才是。

## OB-P3 — Reuse-Gated Crystallization
stable macro crystallization 應以跨 task / domain reuse、depth saving 與 fidelity gain 為門檻。

## OB-P4 — Fragmentation Penalty
自動 skill creation 若沒有 merge / reuse / retirement pressure，較弱 Agent 特別容易累積 fragmented task-specific libraries。

## OB-P5 — Merge Requires Distinction Preservation
高 semantic overlap 不足以 Merge，還必須保留 critical distinctions 與 boundary semantics。

## OB-P6 — Split as Semantic Decompression
當單一 operator 的 conditional behaviors 已形成可分 cluster，Split 可用 vocabulary growth 換回 fidelity / boundary clarity。

## OB-P7 — Reground Before Retire
高價值但 drifted operator 應優先 reground，而非直接淘汰。

## OB-P8 — Hysteretic Adaptation
Add / retire 使用不同 threshold、搭配 dwell/cooldown，可降低 language churn。

## OB-P9 — Layer-Correct Adaptation
若 failure root 在 retriever / topology / tool，改 operator basis 可能造成 wrong-layer overcorrection。

## OB-P10 — Fast/Slow/Meta Timescales
ephemeral adaptation、stable-basis evolution 與 adaptation-policy evolution 應使用分離時間尺度。

## OB-P11 — Selection–Use–Distillation Co-Evolution
operator retrieval frequency、actual use 與 crystallization statistics 相互影響，需防 popularity feedback loop。

## OB-P12 — Topology-Aware Admission
local high-frequency operator 不應自動進 global kernel；kernel promotion 應要求 cross-community value。

## OB-P13 — Viability over Instant Optimum
basis controller 的目標應維持在 viability band，而非持續追逐瞬時 $N^*$。

## OB-P14 — Replay-Gated Evolution
structural operator changes 應經 regression / held-out / boundary / high-risk replay 後再 stable promotion。

## OB-P15 — Operator Ecology Homeostasis
OBAL 的總體作用是讓語言在移動的 $[N_{\min}(t),N_{\max}(t)]$ 與 semantic drift budget 中維持動態 homeostasis。

---

# 222. 第一版實驗 A：Skill-Library Growth

建立 sequence：

$$
Task_1,\ldots,Task_{100}.
$$

比較：

### A0 — Always Add

每 task 產生新 skill。

### A1 — Reuse Gate

先找 reuse。

### A2 — Reuse + Crystallize

motif gate。

### A3 — Full OBAL

加入 merge / split / retire。

量：

- performance；
- library size；
- fragmentation；
- transfer；
- learning cost。

---

# 223. 第一版實驗 B：Motif Crystallization

人工設計 recurring motifs：

$$
m_1,m_2,m_3.
$$

逐步提高：

$$
f_m.
$$

檢查 OBAL 是否在合理 threshold 才 crystallize。

---

# 224. 第一版實驗 C：False Macro Burst

前 20 tasks 高頻 motif，

之後永遠消失。

看：

- 會不會過早 stable；
- 是否能 demote / retire。

---

# 225. 第一版實驗 D：Merge Collision

建立兩個：

$$
O_1,O_2
$$

95% behavior 一樣，

但 5% 是 high-risk critical distinction。

好的 OBAL 不應 Merge。

---

# 226. 第一版實驗 E：God Operator Split

建立：

$$
O_G
$$

多 modes。

隨 contexts 增加：

- selection easy；
- internal error 上升。

測 Split Gate。

---

# 227. 第一版實驗 F：Semantic Drift

stable operator 經 transmission / model update 漂移。

測：

> Reground 還是 Retire？

---

# 228. 第一版實驗 G：Wrong-Layer Failure

故意讓 retriever 出錯。

看 adaptation algorithm 是否誤以為 operator 不好而 merge / delete。

---

# 229. 第一版實驗 H：Topology-Local Skill

某 operator 只在 community $C_1$ 高頻。

測是否：

- local promotion；
- 不污染 kernel。

---

# 230. 第一版實驗 I：Weaker vs Stronger Agent

相同 tasks。

弱 Agent / 強 Agent 分別運行 self-evolving library。

檢查是否重現：

> 弱 Agent 更容易產生 fragmented skill collection。

---

# 231. 第一版實驗 J：Fast vs Slow Meta-Adaptation

比較：

### Same-Speed
basis rule 每輪都能改。

### Two-Timescale
basis 快、meta 慢。

### Three-Timescale
ephemeral / basis / meta。

量：

- performance；
- churn；
- stability；
- interpretability。

---

# 232. 第一版實驗 K：Hot/Warm/Cold Tiering

比較：

### Flat Library

### Tiered Library

量：

- selection；
- retrieval；
- active set；
- regret；
- Nmax。

---

# 233. 第一版實驗 L：Viability-Band Controller

比較：

### Exact-Optimum Chaser

每次都追估計 $N^*$。

### Viability-Band

只在越界時改。

預期後者：

- migration 少；
- churn 低；
- performance 相近。

---

# 234. OBAL Runtime 最小 MVP

未來實作不需要一次做完整 RL。

第一版可以只做：

```text
1. Usage ledger
2. Failure ledger
3. Operator dependency graph
4. Motif detector
5. Similarity / collision detector
6. Drift probes
7. Rule-based gates
8. Candidate replay
9. Version + rollback
10. Hot/Warm/Cold tiers
```

---

# 235. v0.1 最小規則

例如：

### Add
只在 repeated uncovered distinction。

### Crystallize
跨 ≥3 task 重用且 depth saving > threshold。

### Merge
behavior overlap > threshold 且 no critical distinction loss。

### Split
context clusters 顯著且 split 提高 fidelity。

### Reground
drift 超 budget 但 operator utility 高。

### Deprecate
低 utility 持續窗口。

### Retire
deprecated + no critical dependency + migration complete。

---

# 236. 未來 Learned Controller

等 rule-based baseline 有資料後，

再學：

$$
\boxed{
Policy_{\theta}(a\mid X_t).
}
$$

這樣比較合理。

---

# 237. 先 Rule，再 Learn 的理由

否則：

> controller 尚未知道什麼叫好 language，

就先讓它自由改 language。

難以歸因。

---

# 238. Learned Controller 的 Training Data

OBAL ledger 天然產生：

```text
State
Candidate Change
Predicted Gain
Observed Gain
Regression
Rollback
Long-Term Reuse
```

未來可做：

$$
\boxed{
\text{adaptation-policy training corpus}.
}
$$

---

# 239. 這是非常重要的自舉路徑

$$
\boxed{
\text{Rule-Based OBAL}
\rightarrow
\text{Evolution Data}
\rightarrow
\text{Learned OBAL}.
}
$$

---

# 240. 再往後才是 Meta-OBAL

讓 learned OBAL：

> 改自己的 adaptation primitives。

這屬於更遠期。

---

# 241. 與 RLMM 的總接合

RLMM 提供：

- Observe；
- Challenge；
- Promote；
- Update；
- Stop。

OBAL 對語言 basis 做：

- Observe usage；
- Diagnose failure；
- Promote motif；
- Update basis；
- Stop change。

因此：

$$
\boxed{
OBAL
=
RLMM
\text{ applied to an evolving operator language}.
}
$$

---

# 242. 與 LRC 的總接合

每次 basis change 都會改：

$$
Y_L
$$

與：

$$
\kappa_{LR}.
$$

所以：

$$
\boxed{
\text{Language Evolution}
\rightarrow
\text{Reality-Coupling Evolution}.
}
$$

---

# 243. 高耦合 operator 的 Adaptation 要更保守

若：

$$
\kappa_i\uparrow,
$$

則：

- Add evidence threshold ↑；
- Merge distinction threshold ↓；
- drift budget ↓；
- stable dwell ↑；
- replay depth ↑。

---

# 244. Risk-Scaled Governance

定義：

$$
\boxed{
\tau_{change}(O)
=
f(
\kappa_{LR}(O),
Risk(O),
Centrality(O)
).
}
$$

越高：

> 越難改。

---

# 245. 低耦合 Ephemeral Macro 可快速演化

例如：

- formatting；
- summarization；
- local analysis shortcut。

可用較低 threshold。

---

# 246. 這使語言不是一套平均塑性的系統

而是：

$$
\boxed{
\text{heterogeneous plasticity field}.
}
$$

---

# 247. Operator Plasticity

$$
\boxed{
\pi_i
=
f(
Age_i,
Risk_i,
Centrality_i,
Stability_i,
Usage_i
).
}
$$

---

# 248. Basis Plasticity

整體：

$$
\boxed{
\Pi_{\mathcal O}
=
\{\pi_1,\ldots,\pi_N\}.
}
$$

---

# 249. 這與 LRC–COL-08 完整接合

stable core：

$$
\pi_i\downarrow.
$$

experimental periphery：

$$
\pi_i\uparrow.
$$

---

# 250. Operator Basis Adaptation Law 的真正總結

不是：

> 語言會自己長。

而是：

$$
\boxed{
\text{Language should admit novelty, compress repetition, separate overloaded semantics, repair drift, and forget obsolete structure under bounded evidence and migration cost.}
}
$$

---

# 251. 本篇核心公式組

狀態：

$$
\boxed{
X_t
=
(
\mathcal O_t,
\mu_t,
A_t,
G_A,
G_O,
G_Q,
R_t,
H_t,
V_t
).
}
$$

action：

$$
\boxed{
\mathcal A
=
\{
Add,
Crystallize,
Merge,
Split,
Reground,
Deprecate,
Retire,
NoOp
\}.
}
$$

效用：

$$
\boxed{
\Delta U(a)
=
\mathbb E[
\Delta J
\mid
X_t,a
]
-
C_{migration}
-
C_{uncertainty}.
}
$$

決策：

$$
\boxed{
a_t^*
=
\arg\max_a\Delta U(a).
}
$$

STOP：

$$
\boxed{
\max_a\Delta U(a)\le\tau_{change}
\Rightarrow
NoOp.
}
$$

語言規模：

$$
\boxed{
\dot N
=
B_{add}
+
B_{crys}
+
B_{split}
-
D_{merge}
-
D_{retire}.
}
$$

---

# 252. 非主張

本文不主張：

1. 這組七操作已是唯一完備 adaptation action set；
2. 任一 scalar $J$ 足以完整表示語言品質；
3. 所有 operator fitness 都可精確估計；
4. motif frequency 高就必然應 crystallize；
5. low-frequency operator 都應 retire；
6. merge / split 可只靠 embedding similarity；
7. rule-based OBAL 是最終方案；
8. learned adaptation controller 必然優於 heuristic；
9. self-evolving skill research 已解決 long-term fragmentation；
10. meta-adaptation 應立即投入 production；
11. ecology 類比等於生物演化定律；
12. OBAL v0.1 已經被實證。

本文只提出：

$$
\boxed{
\text{A viable composite operator language requires a bounded adaptation controller that can add, crystallize, merge, split, reground, deprecate, retire, and deliberately do nothing according to evidence, reuse, fidelity, drift, learning cost, topology, and reality-coupling risk.}
}
$$

---

# 253. 文獻錨點

1. **Beyond Static Toolsets: Self-Evolving LLM Tool Agents via Continual Documentation Adaptation（Findings ACL 2026）**  
   將 toolsets 視為會新增、修改與 deprecate 的動態環境，提出 stability–adaptation dilemma，並透過 relation-guided exploration / relation-aware documentation adjustment 保留舊能力同時吸收新工具。這直接支持 operator relation / documentation 作為 adaptation surface。

2. **Dynamic Tool Dependency Retrieval for Lightweight Function Calling（Findings ACL 2026）**  
   將 tool retrieval 從 static query matching 改成依 evolving tool-calling plan 動態更新，並顯示 irrelevant tools 會降低 agent accuracy / efficiency。這支持「failure root 若在 retrieval，不應錯改 operator basis」。

3. **ToolOmni: Enabling Open-World Tool Use via Agentic Learning with Proactive Retrieval and Grounded Execution（ACL 2026）**  
   面對 massive and evolving tool repositories，同時最佳化 retrieval accuracy 與 execution efficacy，支持 operator language 應在 open-world retrieval / execution loop 中持續適應。

4. **ToolCPT: Improving Tool Utilization in LLM Agents via Continuous Pre-training（Findings ACL 2026）**  
   建立大規模 tool knowledge corpus，playbooks 中包含 tool functionality、inter-tool protocols、positive / negative examples，支持 operator knowledge 不只是 name / signature，而是可被內化的 semantic-operational asset。

5. **EVOTOOL: Self-Evolving Tool-Use Policy Optimization via Blame-Aware Mutation and Diversity-Aware Selection（ACL 2026）**  
   針對長 horizon tool-use credit assignment，使用 blame-aware mutation 與 diversity-aware selection，支持 targeted adaptation、candidate branching 與 failure attribution。

6. **ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?（2026）**  
   動態評估 continual in-context skill learning；結果顯示 sequential execution 通常帶來改善，但 explicit skill maintenance 的收益依模型與 domain 而異，較弱模型還傾向累積更大、更 fragmented 的 task-specific skill libraries。這直接支持 reuse-gated crystallization、fragmentation penalty 與 selective forgetting。

7. **Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning（2026）**  
   將 skill selection、utilization、distillation 聯合最佳化，說明 skill library evolution 中三者相互依賴；對應本篇 popularity feedback / co-evolution 問題。

8. **MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation（2026）**  
   將 skills 視為具有 creation、memory、management、evaluation、refinement lifecycle 的長期資產，與本文 operator lifecycle / skill-level memory 高度對應。

9. **MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution（2026）**  
   使用 fast task-skill evolution 與 slow meta-skill evolution，支持本文將 ephemeral / basis / meta-policy 分成不同時間尺度。

10. **SkillLearnBench（COLM 2026）與近期 skill-evolution benchmarks**  
    新一代 benchmarks 已開始把 skill generation、reuse、continual learning、cross-task transfer 分開評估，支持未來 OBAL 不能只用 task score 作唯一指標。

---

# 254. 下一篇

## LRC–COL-12：可執行複合語言總論
### 從語義到世界狀態變換
### Executable Composite Language: From Semantics to World-State Transformation

最後一篇將把整個 LRC–COL 系列收斂成完整架構：

$$
\boxed{
\text{Operator Basis}
\rightarrow
\text{Composition}
\rightarrow
\text{Learning}
\rightarrow
\text{Transmission}
\rightarrow
\text{Adaptation}
\rightarrow
\text{Execution}
\rightarrow
\text{World-State Change}.
}
$$

並正式提出：

- COL language stack；
- Surface / Kernel dual language；
- semantic contract；
- compiler；
- retrieval；
- verifier；
- executor；
- operator ecology manager；
- multi-Agent semantic kernel；
- version / drift governance；
- reality-coupling safety；
- static / dynamic completeness interval；
- $T_{\epsilon}^{learn}$ ；
- $K_{\epsilon}^{stable}$ ；
- $N_{\min}$ / $N_{\max}$ ；
- $Y_L$ ；
- OBAL。

最後會明確區分：

$$
\boxed{
\text{Research Theory}
\rightarrow
\text{Language Specification}
\rightarrow
\text{Compiler / Runtime}
\rightarrow
\text{Experimental Harness}.
}
$$

也就是不再繼續寫 LRC–COL-13，而是準備進入真正的 **Composite Operator Language Specification v0.1**。

**END — LRC–COL-11 v0.1**
