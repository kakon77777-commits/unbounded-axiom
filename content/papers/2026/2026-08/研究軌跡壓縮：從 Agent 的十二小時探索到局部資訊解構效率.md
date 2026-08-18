---
title: "研究軌跡壓縮：從 Agent 的十二小時探索到局部資訊解構效率"
english_title: "Research Trajectory Compression: From Twelve-Hour Agent Exploration to Local Information Deconstruction Efficiency"
series: "AI Epistemic Reconstruction Series"
paper: "06"
author: "Neo.K"
date: "2026-08-14"
version: "v0.1"
document_type: "Research Paper / Systems-and-Method Paper"
language: "zh-Hant"
status: "Research Draft"
---

# 研究軌跡壓縮：從 Agent 的十二小時探索到局部資訊解構效率

## Research Trajectory Compression: From Twelve-Hour Agent Exploration to Local Information Deconstruction Efficiency

**作者：Neo.K**  
**系列：AI Epistemic Reconstruction Series — Paper 06**  
**版本：v0.1**  
**日期：2026 年 8 月 14 日**

---

## 摘要

Paper 05 已處理長時 Agent 如何把大量原始 evidence 壓縮成小型、可追溯的 epistemic state；然而，**結果壓縮並不等於過程壓縮**。一個 Agent 即使能把十二小時研究濃縮成數 KB 的 handoff capsule，下一個相似問題仍可能再次花十二小時走過相同的低層 UI 操作、重複性 control experiment、hash、diff、reload 與 replication。

本文提出 **Research Trajectory Compression（RTC，研究軌跡壓縮）**，研究如何把一次昂貴探索 trajectory：

$$
\Pi
=
(a_1,o_1,a_2,o_2,\ldots,a_T,o_T)
$$

蒸餾成可在同類問題上重用的高階研究策略、程序、技能與「研究選項」（Research Options），使未來 Agent 不必從 primitive action level 重新探索。

核心轉換為：

$$
\boxed{
\text{Long Research Trajectories}
\rightarrow
\text{Reusable Research Options}
\rightarrow
\text{Shorter Future Search}
}
$$

本文借用 reinforcement learning 中 temporal abstraction / options 的思想，把一組具有明確啟動條件、內部 protocol、終止條件、驗證不變量與輸出 schema 的研究程序定義為：

$$
\boxed{
\Omega
=
(I,\pi,\beta,V,\Gamma)
}
$$

其中：

- $I$：initiation conditions；
- $\pi$：內部研究 policy / protocol；
- $\beta$：termination condition；
- $V$：verification contract；
- $\Gamma$：產生的 epistemic output schema。

例如一段原本由 Agent 手動執行數十至數百 primitive actions 的：

```text
load baseline
→ no-op
→ save
→ hash
→ byte diff
→ restart
→ reload
→ compare
```

可以蒸餾成一個：

```text
NoOpSaveEquivalenceTest
```

研究 option。

這不是把 trajectory 「摘要成文字」，而是把 trajectory **編譯成可再次執行的認識程序**。

本文進一步提出 **Local Information Deconstruction Efficiency（LIDE，局部資訊解構效率）**：

$$
\boxed{
\eta_D
=
\frac{
\Delta I_D
}{
C_{\mathrm{time}}
+
\lambda_K C_{\mathrm{token}}
+
\lambda_C C_{\mathrm{compute}}
+
\lambda_A C_{\mathrm{action}}
}
}
$$

其中 $\Delta I_D$ 表示在局部 domain $D$ 中對未知結構的有效不確定性降低量。真正的 RTC 目標不是使 Agent 動作更少而已，而是在維持 semantic fidelity、falsifiability 與 evidence quality 的前提下提高 $\eta_D$。

本文從 reinforcement learning 的 temporal abstraction / options、Voyager 的 executable skill library、ExpeL 的 experiential insights、Experiential Co-Learning 的 shortcut-oriented experiences、LRLL 的 skill abstraction，以及 2026 年 Trace2Skill 與 SKILL-KD 的 trajectory-to-skill distillation 出發，提出一個面向研究 Agent 的通用框架：

$$
\boxed{
\text{Experience}
\rightarrow
\text{Segmentation}
\rightarrow
\text{Contrast}
\rightarrow
\text{Skill Induction}
\rightarrow
\text{Cross-Task Validation}
\rightarrow
\text{Research Skill Library}
}
$$

本文也強調，軌跡壓縮存在明顯風險：單一成功 trajectory 可能包含偶然動作、版本依賴、無效步驟或不可泛化 shortcut。真正可重用的研究 option 必須從成功與失敗 evidence 中抽取必要條件、禁止條件、scope、termination、expected evidence 與 fallback，並在 holdout target 上驗證。

最終，本文提出一個更一般的命題：

> **高品質 Agent 不只會解未知問題；它還會把「自己是怎麼解的」重新編譯成下一次更高層級的行動空間。**

這使研究能力從單次解構升級成 **Meta-AER（Meta Active Epistemic Reconstruction）**：第一次探索目標系統，第二次學習如何更快探索同類系統。

**關鍵詞：** Research Trajectory Compression, Temporal Abstraction, Agent Skills, Experience Distillation, Local Information Deconstruction Efficiency, Meta-Learning, Long-Horizon Agents, Research Options, Skill Library, Active Epistemic Reconstruction

---

# 1. 問題：把結果壓成 5 KB，不代表下次只要 5 分鐘

Paper 05 已經建立：

$$
G
\rightarrow
R
\rightarrow
K
\rightarrow
A.
$$

其中：

- $R$：raw evidence；
- $K$：canonical epistemic state；
- $A$：active context。

這解決：

> Agent 如何不把十二小時所有歷史重新塞回 context？

但沒有回答：

> 下一個類似 target，是否還要重新操作十二小時？

---

# 2. Result Compression 與 Trajectory Compression

## Result Compression

$$
R_{0:T}
\rightarrow
K_T.
$$

壓縮：

> 已經知道什麼。

---

## Trajectory Compression

$$
\Pi_{0:T}
\rightarrow
\Omega.
$$

壓縮：

> **怎麼取得那些知識。**

---

# 3. 兩者完全不同

Agent 可以擁有完美 handoff：

```text
B1 verified
B2 incomplete
next = replicate B2
```

但如果它沒有學會：

```text
如何自動建立 baseline
如何 reset
如何做 save diff
如何排除 UI noise
```

仍會重複大量低層 labor。

---

# 4. Research Trajectory

定義一次研究 trajectory：

$$
\Pi
=
(s_0,a_0,o_1,v_1,s_1,\ldots,s_T).
$$

其中：

- $s_t$：epistemic / environment state；
- $a_t$：Agent action；
- $o_{t+1}$：observation；
- $v_{t+1}$：verdict / update。

---

# 5. Primitive Research Action

例如：

```text
click
type
wait
save
hash
read
diff
restart
```

如果全部由 LLM 每次逐步決策：

$$
|\Pi|
$$

會非常長。

---

# 6. Temporally Extended Research Action

如果一段穩定流程：

```text
baseline
→ intervention
→ save
→ diff
→ reload
→ verify
```

被抽象成一個高階 action：

$$
\omega,
$$

則 planner 不再需要逐步規劃所有 primitive actions。

---

# 7. Reinforcement Learning 的歷史接口

Temporal abstraction 的核心思想：

> 不只在 primitive action level 上規劃，而是在 temporally extended actions 上規劃。

Options framework 將 option 描述為：

- initiation set；
- internal policy；
- termination condition。

這提供 RTC 非常自然的理論類比。

---

# 8. Research Option

本文定義：

$$
\boxed{
\Omega
=
(I,\pi,\beta,V,\Gamma)
}
$$

---

# 9. $I$ — Initiation Conditions

何時可以啟動。

例如：

```text
baseline save exists
target version known
save format writable
runtime can restart
```

---

# 10. $\pi$ — Internal Policy

內部 protocol：

```text
load baseline
perform no-op
save target
hash both
byte diff
restart
reload target
```

---

# 11. $\beta$ — Termination

例如：

```text
exact equality established
OR
difference observed
OR
protocol violation
```

---

# 12. $V$ — Verification Contract

定義：

> 哪些結果能推出什麼。

例如：

```text
byte-identical = verified only if
protocol admissible AND
full-byte diff empty
```

---

# 13. $\Gamma$ — Epistemic Output

Option 不只返回：

```text
success
```

而返回：

```yaml
result:
  status:
  evidence:
  contradiction:
  confidence_delta:
  provenance:
```

---

# 14. Research Option 與普通 automation 的差別

普通 macro：

> 幫我把步驟按完。

Research Option：

> **把步驟按完，並產生具有特定認識意義的可驗證結果。**

---

# 15. Example — NoOpSaveEquivalenceTest

```yaml
research_option:
  id: NoOpSaveEquivalenceTest

  initiation:
    - baseline_save_available
    - target_runtime_bootable

  protocol:
    - load_baseline
    - perform_no_gameplay_action
    - save_to_new_slot
    - compute_hash
    - full_byte_diff
    - restart_runtime
    - reload_new_save

  outputs:
    - byte_identity
    - reload_validity
    - visible_state_consistency

  failure_modes:
    - accidental_action
    - wrong_slot
    - hidden_rng
```

---

# 16. 原 trajectory 可以很長

手動執行：

$$
\Pi_{\mathrm{manual}}
=
(a_1,\ldots,a_{150}).
$$

---

# 17. 壓縮後

高階 planner：

$$
\Pi_{\mathrm{high}}
=
(\omega_1).
$$

但 option 內部仍然可以執行 150 steps。

---

# 18. 所以 RTC 不一定降低機器實際 primitive operations

它首先降低：

$$
\boxed{
\text{High-Level Decision Load}
}
$$

---

# 19. 再進一步 algorithmization

如果 option 內步驟可 deterministic automation，

則實際：

- token；
- latency；
- error；

也能下降。

---

# 20. Temporal Abstraction 與 Computational Automation

兩階段：

$$
\text{Macro Abstraction}
\rightarrow
\text{Deterministic Implementation}.
$$

---

# 21. Voyager 的接口

Voyager 在 Minecraft 中建立：

> executable skill library。

長序列行為不必每次重新生成，

而可以：

- 儲存；
- retrieve；
- compose。

這與研究技能庫：

$$
\mathcal L_{\Omega}
$$

高度相似。

---

# 22. 但 Research Skill 比 Minecraft Skill 多一個要求

不只：

> 達成 environment goal。

還必須：

> 產生可稽核 evidence 與 epistemic output。

---

# 23. ExpeL 的接口

ExpeL 從 training tasks 的 agent experiences 中：

> 抽取自然語言 insights 與 past experiences，

在後續 task 中重用。

這支援一個核心命題：

$$
\boxed{
\text{Experience}
\rightarrow
\text{Non-Parametric Improvement}
}
$$

---

# 24. 不需要 fine-tune 才能學會研究捷徑

RTC 可以把：

$$
\Omega
$$

放在 external skill library。

模型參數：

$$
\theta
$$

不必改變。

---

# 25. Experiential Co-Learning

該工作特別提出：

> shortcut-oriented experiences。

這與本文的：

> 從歷史 trajectory 抽取能縮短未來 task 的研究捷徑

直接對位。

---

# 26. Shortcut 不等於偷懶

如果：

```text
舊方法 100 步
新方法 20 步
```

但：

- evidence 同等；
- verifier 同等；
- scope 同等；

則是效率提升。

---

# 27. 無效 Shortcut

如果新方法：

> 跳過 replication。

雖然更快，

但：

$$
FalsificationStrength\downarrow.
$$

這不是有效 RTC。

---

# 28. Lossless Research Compression

理想：

$$
C(\Pi)\downarrow
$$

同時：

$$
Q_E(\Pi)\approx constant.
$$

---

# 29. Quality-Constrained Compression

定義：

$$
\min_{\Omega}
C(\Omega)
$$

subject to：

$$
Q_{\mathrm{evidence}}(\Omega)\ge\tau_E
$$

$$
Q_{\mathrm{falsification}}(\Omega)\ge\tau_F
$$

$$
Q_{\mathrm{reproducibility}}(\Omega)\ge\tau_R.
$$

---

# 30. RTC 不是單純 action pruning

它包含：

- procedural abstraction；
- protocol extraction；
- automation；
- experiment prioritization；
- skill reuse；
- transfer。

---

# 31. 一個 trajectory 裡通常很多步其實沒有 information gain

例如：

```text
wait 2 sec
click menu
move cursor
```

這些是 execution necessities，

不是 epistemic decisions。

---

# 32. Decision / Execution Separation

把 trajectory 分：

$$
\Pi
=
\Pi_D
\cup
\Pi_X.
$$

其中：

- $\Pi_D$：decision points；
- $\Pi_X$：execution steps。

---

# 33. RTC 第一目標

讓：

$$
|\Pi_D|\downarrow.
$$

---

# 34. RTC 第二目標

把穩定：

$$
\Pi_X
$$

交給 deterministic automation。

---

# 35. Research Decision Point

真正需要模型判斷：

```text
Which hypothesis matters?
Which experiment discriminates?
Is result admissible?
Does contradiction require reframing?
```

---

# 36. 不需要模型每次判斷

```text
How to compute SHA-256?
```

---

# 37. LLM 不應做人肉 hash function

這是 Paper 01 的混合系統分工在 RTC 的直接延伸。

---

# 38. Research Skill Extraction

給 trajectories：

$$
\{\Pi_1,\ldots,\Pi_n\}.
$$

抽取：

$$
\{\Omega_1,\ldots,\Omega_m\}.
$$

---

# 39. 單一 trajectory 不夠

成功 trajectory 可能包含：

- luck；
- redundant steps；
- hidden assumptions；
- accidental workaround。

---

# 40. Trace2Skill 的重要接口

Trace2Skill 主張：

> 不應只順序地從單一 trajectory 抽 fragile lessons；

而要：

- 分析多個 execution；
- 抽 trajectory-local lessons；
- hierarchical consolidation；
- 形成 conflict-free transferable skills。

這和 Research Option induction 非常相容。

---

# 41. Trajectory Pool

建立：

$$
\mathcal P
=
\{\Pi^+,\Pi^-,\Pi^{excluded}\}.
$$

---

# 42. 成功 trajectory

$$
\Pi^+.
$$

告訴：

> 什麼可能有效。

---

# 43. 失敗 trajectory

$$
\Pi^-.
$$

告訴：

> 哪些 protocol / assumptions 不可行。

---

# 44. Excluded trajectory

告訴：

> 哪些操作污染 evidence。

---

# 45. 所以 skill extraction 必須同時看三種

否則會把 accidental path 當 general skill。

---

# 46. Contrastive Skill Induction

比較：

$$
\Pi^+
$$

與：

$$
\Pi^-.
$$

找：

$$
\Delta_{\mathrm{action}}
$$

與：

$$
\Delta_{\mathrm{condition}}.
$$

---

# 47. SKILL-KD 的接口

2026 SKILL-KD：

> 比較 student failure 與 teacher trajectory，

把 actionable discrepancy 蒸餾成 skill patch，

再重新執行驗證。

這提供 RTC 很重要的一個機制：

$$
\boxed{
\text{Skill Distillation}
+
\text{Re-execution Validation}
}
$$

---

# 48. Skill 不能只靠語言看起來合理

研究 skill 必須：

> rerun。

---

# 49. Skill Validation

對新 target：

$$
G'.
$$

執行：

$$
\Omega(G').
$$

---

# 50. Transfer Test

如果：

$$
\Omega
$$

只在：

$$
G
$$

有效，

它可能只是 instance-specific macro。

---

# 51. Transferable Research Skill

要求：

$$
P(
\text{valid}
\mid
G'\sim\mathcal D
)
\ge\tau.
$$

---

# 52. Scope 是 skill 的一部分

```yaml
scope:
  DOS_save_based_game
  deterministic_file_save
  rebootable_runtime
```

---

# 53. 不能過度泛化

一個：

```text
GNX save diff procedure
```

不應被標成：

> 所有遊戲都適用。

---

# 54. Scope Fidelity

定義：

$$
SF(\Omega)
=
P(
\text{correct applicability judgment}
).
$$

---

# 55. 研究技能失敗的危險

若錯誤 skill 被高頻重用，

會把錯誤放大。

所以：

$$
\boxed{
\text{Reusable Error}
>
\text{One-Off Error}
}
$$

風險更高。

---

# 56. Skill Provenance

每個 skill 應保留：

```text
source trajectories
validation targets
failure cases
version
```

---

# 57. Skill Versioning

```text
NoOpSaveTest v1.0
NoOpSaveTest v1.1
```

---

# 58. Skill Patch

如果新 target 發現：

> Save 會自動更新 timestamp。

就修改 initiation / normalization。

---

# 59. Skill Drift

反覆 patch 可能讓 skill：

- 越來越長；
- scope 越來越混；
- contradictions 出現。

SKILL-KD 的 drift-aware consolidation 正好對應。

---

# 60. Research Skill Consolidation

定期：

```text
add
modify
split
deprecate
```

而不是永遠 append。

---

# 61. Skill Split

若：

```text
DOS
Refine
```

protocol 不同，

不要塞進同一條巨大 if/else。

可以：

$$
\Omega_{\mathrm{DOS}},
\Omega_{\mathrm{Refine}}.
$$

---

# 62. Hierarchical Skill Library

```text
ReverseEngineering/
├─ SaveAnalysis/
│  ├─ NoOpEquivalence
│  ├─ SingleVariableIntervention
│  └─ ReloadPersistence
├─ BinaryFormat/
├─ RuntimeTrace/
└─ HistoricalPriorValidation/
```

---

# 63. Skill Composition

高階：

```text
VerifyHistoricalOffset
```

可以 compose：

```text
BaselineFreeze
SingleVariableIntervention
ByteDiff
NegativeControl
IndependentReload
Replication
```

---

# 64. Temporal Abstraction 的真正價值

不是只少按幾次鍵。

而是 planner action space：

原：

$$
\mathcal A.
$$

加入 skills：

$$
\mathcal A'
=
\mathcal A
\cup
\Omega.
$$

---

# 65. 高階規劃

Agent 可以直接問：

> 我現在需要 VerifyHistoricalOffset。

而不是：

> 下一步先點哪裡？

---

# 66. Search Depth Reduction

primitive plan depth：

$$
d.
$$

skill-level：

$$
d'.
$$

理想：

$$
d'\ll d.
$$

---

# 67. Planning Compression Ratio

定義：

$$
\boxed{
PCR
=
\frac{
N_{\mathrm{primitive\ decision\ points}}
}{
N_{\mathrm{high\ level\ decisions}}
}
}
$$

---

# 68. 但 PCR 高不代表 skill 好

如果 high-level option 內部錯，

只是把錯誤藏起來。

---

# 69. Verification-Preserving PCR

定義：

$$
PCR_V
=
PCR
\cdot
Q_V.
$$

其中：

$$
Q_V
$$

代表 verification fidelity。

---

# 70. LIDE：局部資訊解構效率

本文提出：

$$
\boxed{
\eta_D
=
\frac{
\Delta I_D
}{
C_D
}
}
$$

---

# 71. $D$ — Local Domain

例如：

```text
PM2 DOS save semantics
```

而不是：

> 世界所有知識。

---

# 72. $\Delta I_D$

可以用：

- entropy reduction；
- verified claims；
- eliminated hypotheses；
- prediction error reduction；

近似。

---

# 73. 成本

$$
C_D
=
C_T
+
\lambda_K C_K
+
\lambda_C C_C
+
\lambda_A C_A.
$$

---

# 74. $C_T$

wall-clock time。

---

# 75. $C_K$

tokens / context。

---

# 76. $C_C$

CPU / GPU / I/O。

---

# 77. $C_A$

environment actions。

---

# 78. 為什麼要 local

同樣 1000 token，

在：

```text
save field mapping
```

可能很高資訊量。

在：

```text
全域整個遊戲
```

可能微不足道。

---

# 79. Local Information Deconstruction

指：

> 把局部未知結構逐步分解成可驗證表示、語義與規則。

---

# 80. LIDE 的目標

$$
\eta_D\uparrow.
$$

---

# 81. RTC 如何提高 $\eta_D$

三條路：

1. 少做低價值實驗；
2. 重用高價值 protocol；
3. 把執行步驟自動化。

---

# 82. Research Speedup

定義：

$$
S_R
=
\frac{
C_{\mathrm{baseline}}
}{
C_{\mathrm{RTC}}
}
$$

在相同 target quality 下。

---

# 83. Quality Constraint

比較 speedup 前必須要求：

$$
Q_{\mathrm{RTC}}
\ge
Q_{\mathrm{baseline}}-\epsilon.
$$

---

# 84. 不然「不做驗證」永遠最快

這是錯誤 benchmark。

---

# 85. Meta-AER

Paper 03 的 AER：

> 主動學 target。

Paper 06 的 Meta-AER：

> **主動學「怎麼學 target」。**

---

# 86. 定義

$$
\boxed{
\operatorname{MetaAER}
:
\{\Pi_i\}
\rightarrow
\pi_R^*
}
$$

其中：

$$
\pi_R^*
$$

是研究策略。

---

# 87. Research Policy

輸入：

$$
z_t
$$

表示目前 epistemic state。

輸出：

$$
a_t
$$

是下一研究 action / option。

---

# 88. 從單次解題到研究 policy

第一次：

```text
Agent discovers good sequence accidentally.
```

之後：

```text
Agent recognizes state pattern
→ invokes known research option
```

---

# 89. Pattern Recognition

例如：

```text
unknown save field
+
writable deterministic save
+
controllable visible stat
```

立即觸發：

```text
SingleVariableInterventionOption
```

---

# 90. 這就是局部研究自動化

---

# 91. Automatic Curriculum 的接口

Voyager 不只是 skill library，

還有 automatic curriculum：

> 根據當前能力選下一個值得探索的 task。

研究 Agent 同理：

> 根據目前 epistemic frontier 選下一個最有價值 subproblem。

---

# 92. Curriculum over Unknowns

```text
easy high-confidence offsets
→ time mapping
→ economy mapping
→ event conditions
→ RNG
```

---

# 93. Curriculum 也能被壓縮

過去哪種順序：

> 最能建立 downstream anchors？

可被學習。

---

# 94. Dependency-Aware Curriculum

如果：

$$
c_1\rightarrow c_2,
$$

先研究 $c_1$。

---

# 95. Research DAG

$$
G_R
=
(V_{\mathrm{subproblem}},E_{\mathrm{dependency}}).
$$

---

# 96. 最佳順序不是任意

應考慮：

- dependency；
- information gain；
- cost；
- reuse potential。

---

# 97. Option Utility

對 skill：

$$
\Omega_i,
$$

定義：

$$
U(\Omega_i)
=
\frac{
\mathbb E[\Delta I]
}{
\mathbb E[C]
}.
$$

---

# 98. High Utility Option

被頻繁保留。

---

# 99. Low Utility Option

若：

- expensive；
- fragile；
- low discrimination；

可以 deprecate。

---

# 100. Skill Library 也需要 GC

Paper 05 有 Evidence GC。

Paper 06 有：

$$
\boxed{
\text{Skill GC}
}
$$

---

# 101. Skill Obsolescence

如果新工具出現：

> 舊的手動 protocol 已無必要。

例如：

```text
manual screenshots
→ direct memory instrumentation
```

---

# 102. Skill Replacement

$$
\Omega_{\mathrm{old}}
\rightarrow
\Omega_{\mathrm{new}}.
$$

---

# 103. Skill Dominance

若：

$$
C(\Omega_2)<C(\Omega_1)
$$

且：

$$
Q(\Omega_2)\ge Q(\Omega_1),
$$

則 $\Omega_2$ dominates $\Omega_1$。

---

# 104. Pareto Frontier

技能可以依：

- cost；
- fidelity；
- generality；
- risk；

形成 Pareto front。

---

# 105. 不同情況用不同 option

Fast exploratory：

> cheap / lower confidence。

Publication-grade：

> expensive / high confidence。

---

# 106. Verification Profiles

```text
Exploratory
Standard
Strict
Publication
```

---

# 107. 同一 Research Option 可以 parameterized

```yaml
replications: 1 / 2 / 5
negative_controls: true
independent_reload: true
```

---

# 108. 動態嚴謹度

早期探索：

$$
Q_V\approx moderate.
$$

關鍵 claim：

$$
Q_V\rightarrow high.
$$

---

# 109. 這能避免「每個 byte 都做博士論文級驗證」

（笑）

---

# 110. Research Cost Allocation

把高成本 verification 留給：

> high-impact claims。

---

# 111. Claim Impact

$$
I_C(c)
=
N_{\mathrm{downstream\ dependencies}}
\times
Risk(c).
$$

---

# 112. High-impact claim

例如：

> save endian / checksum model。

錯了會污染大量 downstream。

---

# 113. Low-impact claim

某個不重要 UI offset。

---

# 114. Verification Budget

$$
B_V
$$

依 impact 分配。

---

# 115. RTC 與 Active Learning 的結合

Paper 03 選：

$$
a^*
=
\arg\max IG/C.
$$

Paper 06 增加：

> action 可以是高階 option。

---

# 116. Option-Level Experiment Selection

$$
\omega_t^*
=
\arg\max_{\omega\in\Omega}
\frac{
IG(\omega)
}{
C(\omega)
}.
$$

---

# 117. 搜尋空間從 primitive actions 提升到 protocol space

---

# 118. Hierarchical Planner

上層：

> 選研究 option。

下層：

> 執行 protocol。

---

# 119. Error Escalation

Option 遇到非預期狀態：

```text
expected menu missing
```

不應自己亂猜。

應：

$$
\boxed{
\text{Escalate to Agent}
}
$$

---

# 120. Skill Boundary

Skill 處理：

> known knowns。

Agent 處理：

> unknown unknowns。

---

# 121. Automation Trap

把不穩定研究過早寫死成 script，

可能：

> 把錯假說制度化。

---

# 122. Promotion Ladder for Research Skills

```text
trajectory-local hint
↓
candidate skill
↓
validated skill
↓
transfer-tested skill
↓
stable research option
```

---

# 123. 必須先驗證才自動化

---

# 124. Skill Evidence

```yaml
skill:
  source_trajectories:
  successful_runs:
  failed_runs:
  holdout_runs:
  known_limitations:
```

---

# 125. Trace2Skill 式整體分析

不要：

```text
run1 → add rule
run2 → add rule
run3 → add rule
```

一直局部 patch。

---

# 126. 而應定期：

```text
analyze broad trajectory pool
→ consolidate
→ remove conflicts
→ rewrite skill
```

---

# 127. Holistic Skill Compilation

$$
\mathcal C_{\mathrm{skill}}
:
\mathcal P
\rightarrow
\Omega.
$$

---

# 128. Declarative Skill vs Executable Skill

### Declarative

```text
When validating a save offset, use a negative control.
```

### Executable

```python
verify_save_offset(...)
```

---

# 129. 最好兩者都有

Declarative：

> 適合不同 tool environment。

Executable：

> 高效率、高一致性。

---

# 130. Dual Representation

$$
\Omega
=
(\Omega_{\mathrm{spec}},\Omega_{\mathrm{exec}}).
$$

---

# 131. Spec 是 canonical truth

Exec 可以重寫。

---

# 132. Tool Migration

DOSBox → DOSBox-X → 自建 emulator。

只要 spec 不變，

可以替換 executable implementation。

---

# 133. Research Option 與 Paper 02 的語義域

每個 option 必須標：

> 它在哪個 domain 有效。

---

# 134. Definition Domain of a Research Skill

例如：

$$
D_\Omega
=
\text{rebootable file-based legacy game}.
$$

---

# 135. Judgment Domain of a Research Skill

它能判定：

```text
save byte equality
```

不能判：

```text
entire gameplay correctness
```

---

# 136. 防止過度宣稱

skill 的 verifier contract 也要存在。

---

# 137. Running Case：PM2 的可能 RTC

以下是候選，不代表已測得實際 speedup。

---

# 138. Option A — Baseline Freeze

自動：

- copy；
- hash；
- manifest；
- mark immutable。

---

# 139. Option B — No-Op Save Equivalence

自動：

- load；
- no-op；
- save；
- hash；
- diff；
- reload。

---

# 140. Option C — Single-Variable Intervention

要求：

- target state；
- intervention；
- negative control。

---

# 141. Option D — Historical Prior Validation

輸入：

```text
old HEX claim
```

自動建立：

- candidate mapping；
- intervention；
- diff；
- replication。

---

# 142. Option E — Replication Scaffold

把：

```text
B1
```

自動轉成：

```text
B2 independent replication
```

---

# 143. Option F — Exclusion Detector

若：

- money unexpected；
- date unexpected；
- menu branch wrong；

標：

```text
EXCLUDED
```

並 reset。

---

# 144. 這一項可能非常省 Agent 時間

因為之前大量 labor：

> 發現自己操作走錯，再人工重來。

---

# 145. UI Automation Risk

但 legacy UI 可能：

- timing sensitive；
- OCR unreliable；
- emulator state different。

所以需：

> screenshot / state verifier。

---

# 146. UI Research Option 必須有 checkpoint

```text
expected screen
expected money
expected date
```

---

# 147. State-aware Macro

不是盲 macro：

```text
click x,y
```

而是：

```text
if screen_state == expected:
    act
else:
    escalate
```

---

# 148. 這是 robust option

---

# 149. 十二小時不是恥辱

第一次探索：

> 必須發現 failure modes。

這些 failure modes 正是未來 skill 的 training data。

---

# 150. First Run as Capital Expenditure

可以理解：

$$
C_{\mathrm{first}}
$$

是：

> 建立研究基礎設施成本。

---

# 151. 後續 marginal cost

理想：

$$
C_{n+1}<C_n.
$$

---

# 152. Learning Curve

若同 task family：

$$
C_n
=
C_\infty
+
(C_1-C_\infty)e^{-kn}
$$

只是概念模型。

---

# 153. 若沒有下降

表示 Agent：

> 沒把 experience 編譯成 reusable structure。

---

# 154. Trajectory Repetition Ratio

定義：

$$
RR_T
=
\frac{
N_{\mathrm{repeated\ primitive\ patterns}}
}{
N_{\mathrm{total\ primitive\ actions}}
}.
$$

---

# 155. 高 $RR_T$

表示：

> 有強烈 RTC 潛力。

---

# 156. Automation Candidate Detection

若 action subsequence：

$$
\sigma
$$

頻繁出現，

且 outcomes stable，

提議：

$$
\sigma\rightarrow\Omega.
$$

---

# 157. Frequency 不夠

還要：

- low variance；
- clear precondition；
- clear termination；
- high utility。

---

# 158. Skill Candidate Score

$$
S_\Omega
=
f(
Frequency,
Cost,
Stability,
InformationGain,
Transferability
).
$$

---

# 159. 低頻但昂貴 protocol 也可能值得 skill 化

例如：

> full release regression。

---

# 160. Process Mining 的接口

研究 trajectories 可以像 business process logs 一樣：

> 找 common patterns / bottlenecks。

本文不展開 process mining 文獻，

但工程上非常適合。

---

# 161. Bottleneck Detection

統計：

```text
time spent
token spent
failure count
retry count
```

找到：

$$
\arg\max C(step).
$$

---

# 162. 最大成本未必是最大價值

---

# 163. Local Optimization

先壓縮：

> 高成本低信息步驟。

---

# 164. Global Optimization

再重排研究順序。

---

# 165. Experiment Ordering

假設：

```text
A gives anchor for B
```

先跑 A 可以讓 B 快很多。

---

# 166. RTC 不只縮 macro

也能改：

$$
\text{research order}.
$$

---

# 167. Curriculum Compression

從歷史 tasks 學：

> 哪些 anchors 應先找。

---

# 168. Example

先找到：

```text
money
date
stress
```

可能成為後續：

> save state alignment anchors。

---

# 169. Anchor Value

定義：

$$
V_A(c)
=
\text{Expected downstream uncertainty reduction}.
$$

---

# 170. 高 anchor value claim

優先研究。

---

# 171. Knowledge Prerequisite Graph

$$
G_P.
$$

Meta-AER 可以學：

> 哪些節點先解。

---

# 172. Research Policy Distillation

歷史 trajectories：

$$
\Pi_i
$$

轉成：

$$
\pi_R.
$$

---

# 173. Policy 不一定是 neural network

可以是：

- declarative guide；
- decision tree；
- workflow；
- code；
- mixed.

---

# 174. Frozen Model 也能更強

如果外部：

$$
\pi_R
$$

變好，

即使：

$$
\theta
$$

不變，

Agent performance 可以上升。

---

# 175. 這再次支持 Paper 01

完整 Agent ability：

> 不等於單一 model weights。

---

# 176. Skill Transfer Across Models

Trace2Skill 報告的 trajectory-grounded skills 可跨 model scale / OOD transfer。

這對研究 runtime 非常重要：

> skill library 不應綁死單一 AI provider。

---

# 177. Model-Agnostic Research Skill

理想：

```text
input schema
output schema
tool contract
```

清楚。

---

# 178. 不同模型只負責高層推理

---

# 179. Agent Skill ABI

可以類比：

$$
\boxed{
\text{Research Skill ABI}
}
$$

---

# 180. Skill ABI 包含

```text
name
inputs
preconditions
outputs
failure codes
evidence schema
version
```

---

# 181. 這使 skill 可以被 GPT / Claude / local model 共用

只要 tool runtime 相容。

---

# 182. Skill Compiler

Declarative skill：

```yaml
verify_save_offset
```

編譯成：

- Python；
- emulator macros；
- shell；
- debugger scripts。

---

# 183. Cross-Environment Compilation

$$
\Omega_{\mathrm{spec}}
\rightarrow
\Omega_{\mathrm{exec}}^{(E)}.
$$

---

# 184. 這與 Game Rebirth 的 semantic runtime 很像

同一 semantic core：

> 多 backend。

---

# 185. Research Runtime 也應如此

---

# 186. Local Information Deconstruction Efficiency 的 benchmark

建立多個類似 black-box tasks：

$$
D_1,\ldots,D_n.
$$

---

# 187. Baseline Agent

每個從零。

---

# 188. RTC Agent

可用歷史 skill library。

---

# 189. 比較

- final accuracy；
- wall time；
- tokens；
- environment actions；
- evidence quality。

---

# 190. LIDE Ratio

$$
\boxed{
Gain_{\mathrm{LIDE}}
=
\frac{
\eta_D^{RTC}
}{
\eta_D^{base}
}
}
$$

---

# 191. 真正成功

要求：

$$
Gain_{\mathrm{LIDE}}>1
$$

且 final quality 不下降。

---

# 192. Generalization Test

不能只在同一 PM2 save 上測。

要：

- 不同 slot；
- 不同 version；
- different legacy game；
- synthetic mutation。

---

# 193. In-Domain Transfer

$$
D'\approx D.
$$

---

# 194. Cross-Domain Transfer

$$
D'\neq D.
$$

更難。

---

# 195. Skill Generality Spectrum

```text
instance
version
game
engine family
legacy software
generic black-box
```

---

# 196. 越 general 越可能失去效率

---

# 197. Specificity / Generality Tradeoff

$$
U(\Omega)
=
Transferability
\times
Efficiency.
$$

---

# 198. 最佳 skill library 需要多層

generic：

```text
single-variable intervention
```

specific：

```text
PM2 GNX reload validator
```

---

# 199. Hierarchical Retrieval

先找：

> specific skill。

沒有再找：

> generic skill。

---

# 200. Skill Conflict

兩 skill：

$$
\Omega_1,\Omega_2
$$

在同 scope 給不同 protocol。

---

# 201. Conflict Resolution

依：

- validation evidence；
- recency；
- version；
- success rate。

---

# 202. Skill Confidence

$$
c_\Omega.
$$

---

# 203. 低信心 skill

只能：

> suggest。

---

# 204. 高信心 skill

可以：

> auto-execute。

---

# 205. Automation Authority

隨 confidence 增加：

```text
recommend
→ supervised execute
→ auto execute
```

---

# 206. 這降低錯誤 skill 的破壞性

---

# 207. Research Skill Safety

如果 action：

- destructive；
- irreversible；
- expensive；

即使 skill verified，

仍需 policy gate。

---

# 208. RTC 不代表自主權無限制

---

# 209. Research Option Logging

每次 reuse：

```yaml
invocation:
  option:
  target:
  parameters:
  outcome:
  cost:
  evidence:
```

---

# 210. Skill 自己也持續學

$$
\Omega_t
\rightarrow
\Omega_{t+1}.
$$

---

# 211. Skill Performance Statistics

```text
success rate
median cost
median info gain
failure modes
```

---

# 212. Empirical Utility

$$
\hat U(\Omega)
=
\frac{
\sum \Delta I
}{
\sum C
}.
$$

---

# 213. Delete Dead Skills

如果多年不用且被更好 skill dominate，

archive。

---

# 214. Research Library 會變成第二層智能

第一層：

$$
M.
$$

第二層：

$$
\mathcal L_{\Omega}.
$$

---

# 215. Agent Capability

$$
\boxed{
Capability
=
Model
+
Tools
+
Memory
+
Research Skills
}
$$

---

# 216. 這使「同一模型」隨時間可以越來越會研究

即使 weights 不變。

---

# 217. Non-Parametric Learning

RTC 是一種：

$$
\boxed{
\text{Non-Parametric Research Learning}
}
$$

---

# 218. 與 finetuning 不衝突

未來也可以把成熟 skills：

> 再蒸餾進模型。

---

# 219. Skill-to-Weight Distillation

$$
\mathcal L_\Omega
\rightarrow
\theta'.
$$

但不是 RTC 必要條件。

---

# 220. 可證偽預測一

在同 task family 中，使用 validated research options 的 Agent 應以更少 high-level decisions 達到相同 final fidelity。

---

# 221. 可證偽預測二

將穩定 execution subsequences algorithmize 後，token cost 應下降。

---

# 222. 可證偽預測三

只從成功 trajectory 抽 skill，應比 success+failure contrastive distillation 更容易 overfit。

---

# 223. 可證偽預測四

跨多 trajectory consolidation 的 skill，應比單 trajectory summary 有更高 holdout transfer。

---

# 224. 可證偽預測五

Skill library 若不保存 scope，cross-version error rate 應上升。

---

# 225. 可證偽預測六

Skill invocation 有 state checkpoint / verifier 的 robust macro，應比 blind coordinate macro 有更低 protocol violation rate。

---

# 226. 可證偽預測七

加入 research option library 後：

$$
PCR
$$

應上升，

而：

$$
Q_E
$$

不下降。

---

# 227. 可證偽預測八

validated historical-prior-validation option 應降低逐 offset 從零 discovery cost。

---

# 228. 可證偽預測九

Meta-AER curriculum 應比固定 subproblem order 有更低 time-to-anchor。

---

# 229. 可證偽預測十

跨模型使用同一 research skill library 時，能力提升的一部分應保留，顯示 improvement 不完全綁在 model weights。

---

# 230. 限制一：12 小時案例尚未證明未來一定更快

本文目前提出：

> 可壓縮 opportunity。

還沒有以後續完整 PM2 session 實證：

$$
12h\rightarrow2h.
$$

---

# 231. 因此 speedup 是待測假說

不是既成事實。

---

# 232. 限制二：Task Distribution Shift

新遊戲可能：

- 不同 save；
- 不同 UI；
- anti-cheat；
- nondeterministic。

舊 skill 可能失效。

---

# 233. 限制三：Skill Discovery 本身有成本

蒸餾：

$$
C_{\mathrm{distill}}.
$$

若 skill 只用一次，

可能不划算。

---

# 234. Break-Even Reuse Count

若每次省：

$$
\Delta C,
$$

則需要：

$$
N^*
\ge
\frac{
C_{\mathrm{distill}}
}{
\Delta C
}.
$$

---

# 235. 限制四：Over-automation

Agent 過度依賴技能庫，

可能不再探索更好方法。

---

# 236. Exploration Reserve

保留一定：

$$
\epsilon
$$

機率探索 alternative protocol。

---

# 237. 限制五：Skill Lock-In

一個早期次優 skill 成為標準後，

後面所有 Agent 都跟著慢。

---

# 238. 定期 Benchmark Skill Library

---

# 239. 限制六：Hidden Assumptions

skill 可能默認：

- locale；
- timing；
- resolution；
- permissions。

---

# 240. Assumption Manifest

每 skill 必須顯式寫。

---

# 241. 限制七：Research Skill 可能洩漏 benchmark 答案

如果 skill 直接寫：

```text
offset = 0x50
```

那是 target answer，

不是 general skill。

---

# 242. Skill / Answer Separation

Skill 應：

> 教你怎麼驗證 offset。

不是：

> 告訴你 offset。

---

# 243. 這對 contamination-resistant benchmark 很重要

Paper 08 將展開。

---

# 244. 限制八：資訊增益難精確估

所以：

$$
\eta_D
$$

實際常需 proxy。

---

# 245. Proxy 可以是

- verified claim count；
- hypothesis reduction；
- unseen prediction accuracy。

---

# 246. 但不能只計 claim 數

一個重大 rule：

> 價值可能遠高於 100 個 UI offset。

---

# 247. Weighted Information Gain

$$
\Delta I_D
=
\sum_i
w_i\Delta q_i.
$$

---

# 248. $w_i$

可依：

- downstream dependency；
- uncertainty；
- impact；
- reuse。

---

# 249. LIDE 是工程指標，不是假裝有絕對信息單位

本文不主張：

> 已有唯一自然單位。

---

# 250. 它主要提供比較框架

同一 task family：

> Agent A vs B。

---

# 251. 核心命題一

## Proposition 1 — Result Compression Does Not Imply Trajectory Compression

存在：

$$
C_R(R)\ll R
$$

但下一 task 仍重走完整：

$$
\Pi.
$$

所以 Paper 05 的 semantic compression 不能自動導出 RTC。

---

# 252. 核心命題二

## Proposition 2 — Temporally Extended Research Options Can Reduce High-Level Planning Depth

若 primitive sequence：

$$
\sigma=(a_1,\ldots,a_k)
$$

可由一個 option：

$$
\omega
$$

可靠執行，

則 high-level planner 可用一個 decision 取代 $k$ 個 primitive decision points。

---

# 253. 核心命題三

## Proposition 3 — Verification Must Be Preserved Under Trajectory Compression

若：

$$
C(\Pi)
$$

移除必要 negative control / verifier，

則它不是等價 research trajectory compression。

---

# 254. 核心命題四

## Proposition 4 — Multi-Trajectory Skill Induction Can Reduce Single-Trajectory Overfitting

使用：

$$
\{\Pi_i^+,\Pi_j^-,\Pi_k^{ex}\}
$$

可比只使用單一：

$$
\Pi^+
$$

提供更多 failure conditions 與 applicability boundaries。

此命題需實證評估。

---

# 255. 核心命題五

## Proposition 5 — Research Skills Permit Non-Parametric Accumulation of Agent Capability

若：

$$
M
$$

固定，

但 skill library：

$$
\mathcal L_{\Omega,t}
$$

持續改善，

則系統 task performance 可以提高而無需修改 $\theta$。

---

# 256. 核心命題六

## Proposition 6 — Meta-AER Converts Target Learning into Learning How to Learn Targets

AER：

$$
\Theta^*
\leftarrow\text{experiments}.
$$

Meta-AER：

$$
\pi_R^*
\leftarrow\text{AER trajectories}.
$$

---

# 257. 核心命題七

## Proposition 7 — Local Information Deconstruction Efficiency Can Increase Even When Raw Compute Remains Constant

即使某些 primitive runtime costs 不變，

若：

- high-level decision count；
- token overhead；
- repeated mistakes；

下降，

則：

$$
\eta_D
$$

仍可提高。

---

# 258. 統一流程

```text
RAW RESEARCH TRAJECTORIES
        │
        ▼
SEGMENT
decision / execution / evidence
        │
        ▼
COMPARE
success / failure / excluded
        │
        ▼
INDUCE
candidate research skills
        │
        ▼
VALIDATE
holdout target / mutation
        │
        ▼
CONSOLIDATE
scope / precondition / verifier
        │
        ▼
RESEARCH OPTION LIBRARY
        │
        ▼
HIERARCHICAL PLANNER
        │
        ▼
SHORTER FUTURE RESEARCH
```

---

# 259. RTC 與 Paper 05 的統一

Paper 05：

$$
R\rightarrow K.
$$

Paper 06：

$$
\Pi\rightarrow\Omega.
$$

所以長時 Agent 的雙重壓縮：

$$
\boxed{
(R,\Pi)
\rightarrow
(K,\Omega)
}
$$

---

# 260. Knowledge + Procedure

$$
K
$$

回答：

> 我們知道什麼？

$$
\Omega
$$

回答：

> 我們下次怎麼知道得更快？

---

# 261. 這兩者共同形成真正可累積研究能力

---

# 262. Research Capital

可以定義：

$$
\boxed{
\mathcal C_R
=
(K,\Omega,I,R)
}
$$

包含：

- knowledge；
- research skills；
- index；
- raw evidence。

---

# 263. Agent 換掉也沒關係

如果：

$$
M_1\rightarrow M_2,
$$

Research Capital 仍可保留。

---

# 264. 所以研究組織的能力不等於單個模型

---

# 265. Research Organization as Persistent Runtime

這可能是未來：

> AI Lab Operating System

的核心。

---

# 266. 每一次昂貴研究都應留下兩種產物

### Product A — Knowledge

```text
what was learned
```

### Product B — Method

```text
how to learn this class faster next time
```

---

# 267. 只留下 A

就是傳統報告。

---

# 268. 留下 A+B

才開始形成：

$$
\boxed{
\text{Compounding Research Capability}
}
$$

---

# 269. Compounding

第一次：

$$
C_1.
$$

第二次：

$$
C_2<C_1.
$$

同時 knowledge base 擴張。

---

# 270. 理想極限

對已高度標準化 domain：

> 大部分 routine reverse engineering 變成 algorithm。

Agent 專注：

> 真正未知部分。

---

# 271. Unknown Frontier Shrinkage

工具／技能越成熟：

$$
\mathcal U_{\mathrm{routine}}\downarrow.
$$

留下：

$$
\mathcal U_{\mathrm{novel}}.
$$

---

# 272. 這就是「局部資訊解構能力」真正提升

不是 AI magically 更聰明。

而是：

> 同一局部 domain 中更多結構已被編譯成 reusable cognition。

---

# 273. Cognitive Infrastructure

Research Options 是：

$$
\boxed{
\text{Externalized Cognitive Infrastructure}
}
$$

---

# 274. 人類科學也一直這樣做

從：

- 手工算術；
- table；
- calculator；
- software；
- automated instrument。

---

# 275. AI 只是能更快把自己的 labor 再工具化

---

# 276. Self-Tooling Loop

$$
\boxed{
\text{Research}
\rightarrow
\text{Observe Repetition}
\rightarrow
\text{Build Tool}
\rightarrow
\text{Research Faster}
}
$$

---

# 277. 這是一個正向 feedback loop

---

# 278. 但也需要治理

錯工具會放大錯誤。

所以：

$$
\boxed{
\text{Skill Verification}
}
$$

是 Meta-AER 的核心。

---

# 279. 最終公式

研究效率：

$$
\boxed{
\eta_D
=
\frac{
\Delta I_D
}{
C_{\mathrm{time}}
+
\lambda_K C_{\mathrm{token}}
+
\lambda_C C_{\mathrm{compute}}
+
\lambda_A C_{\mathrm{action}}
}
}
$$

Research Option selection：

$$
\boxed{
\omega_t^*
=
\arg\max_{\omega}
\frac{
\mathbb E[\Delta I_D\mid\omega]
}{
C(\omega)
}
}
$$

Trajectory-to-skill：

$$
\boxed{
\mathcal C_{\mathrm{skill}}
:
\{\Pi_i\}
\rightarrow
\{\Omega_j\}
}
$$

Meta-AER：

$$
\boxed{
\operatorname{MetaAER}
:
\{\Pi_i,K_i\}
\rightarrow
\pi_R^*
}
$$

---

# 280. 最終結論

長時 Agent 研究不應只追求：

> 最後有沒有得到答案。

每一次昂貴 trajectory 都包含第二種資產：

> **如何更有效率地取得這類答案。**

如果這種程序知識沒有被抽取，下一個 Agent 會重新：

- 點相同 UI；
- 犯相同 protocol mistake；
- 重跑相同 low-information experiment；
- 再次消耗相同 token 與時間。

真正的研究能力累積要求：

$$
\boxed{
\text{Experience}
\rightarrow
\text{Research Skill}
}
$$

Paper 05 將十二小時的 evidence 壓成 epistemic state；Paper 06 則把十二小時的探索過程壓成可重用的 Research Options。

因此：

$$
\boxed{
\text{Long Trajectory}
\neq
\text{Permanent Cost}
}
$$

只要 trajectory 能被：

- 分段；
- 比較；
- 抽象；
- 驗證；
- 程序化；
- 重用，

第一次十二小時就可能成為之後整個 task family 的 **認知基礎設施投資**。

本文最終提出：

> **真正會成長的研究 Agent，不只把新知識寫進記憶，也把高成本研究過程重新編譯成下一次可直接調用的高階技能。**

這種能力即本文所稱：

$$
\boxed{
\textbf{Research Trajectory Compression}
}
$$

其最終衡量，不是「trajectory 被縮短多少字」，而是：

$$
\boxed{
\textbf{Local Information Deconstruction Efficiency}
}
$$

是否真正提升。

---

# 281. 後續

**Paper 07：AI 的「無聊角色」：重複性科學勞動、自動實驗與研究角色重分配**

將進一步處理：

> 當 Research Option 成熟後，哪些工作應由 LLM Agent 做、哪些應降級為 deterministic algorithm、哪些必須保留給人類？

也就是：

$$
\boxed{
\text{Human}
+
\text{Agent}
+
\text{Automation}
}
$$

三者在 AI 科研中的新分工。

---

# References

[1] Sutton, R. S., Singh, S. P., Precup, D., & Ravindran, B. **Improved Switching among Temporally Abstract Actions.** NeurIPS 1998.  
https://papers.nips.cc/paper/1607-improved-switching-among-temporally-abstract-actions

[2] Sutton, R. S., Precup, D., & Singh, S. **Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning.** Artificial Intelligence 112, 181–211 (1999).  
Historical options framework; referenced through primary research lineage.

[3] Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., & Anandkumar, A. **Voyager: An Open-Ended Embodied Agent with Large Language Models.** arXiv:2305.16291, 2023.  
https://arxiv.org/abs/2305.16291

[4] Zhao, A., Huang, D., Xu, Q., Lin, M., Liu, Y.-J., & Huang, G. **ExpeL: LLM Agents Are Experiential Learners.** arXiv:2308.10144, 2023.  
https://arxiv.org/abs/2308.10144

[5] Qian, C., et al. **Experiential Co-Learning of Software-Developing Agents.** arXiv:2312.17025, 2023.  
https://arxiv.org/abs/2312.17025

[6] Tziafas, G., & Kasaei, H. **Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models.** arXiv:2406.18746, 2024.  
https://arxiv.org/abs/2406.18746

[7] Li, Z., Poesia, G., & Solar-Lezama, A. **When Do Skills Help Reinforcement Learning? A Theoretical Analysis of Temporal Abstractions.** arXiv:2406.07897, 2024.  
https://arxiv.org/abs/2406.07897

[8] Ni, J., et al. **Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills.** arXiv:2603.25158, 2026.  
https://arxiv.org/abs/2603.25158

[9] Shi, Q., et al. **SKILL-KD: Contrastive Skill Distillation for LLM Agents.** arXiv:2607.28048, 2026.  
https://arxiv.org/abs/2607.28048

---

# Appendix A — Research Option Schema

```yaml
research_option:
  id:
  version:

  scope:
    task_family:
    target_types:
    excluded_targets: []

  initiation:
    required_state: []
    required_tools: []
    assumptions: []

  protocol:
    high_level_steps: []
    executable_backend:

  termination:
    success_conditions: []
    inconclusive_conditions: []
    failure_conditions: []
    escalation_conditions: []

  verifier:
    contract:
    evidence_required: []
    negative_controls: []
    replication_policy:

  epistemic_output:
    schema:
    status_values:
      - verified
      - partially_verified
      - invalidated
      - unknown
      - excluded

  provenance:
    source_trajectories: []
    successful_validation_runs: []
    failed_validation_runs: []
    holdout_targets: []

  metrics:
    median_time:
    median_tokens:
    median_actions:
    estimated_information_gain:
    transfer_success_rate:

  authority:
    mode:
      - recommend_only
      - supervised_execute
      - auto_execute
```

---

# Appendix B — RTC Pipeline

```text
1. Collect trajectories.
2. Label success / failure / excluded.
3. Segment decision vs execution steps.
4. Find repeated stable subsequences.
5. Identify epistemic purpose of each subsequence.
6. Contrast success and failure conditions.
7. Induce candidate research option.
8. Write scope + preconditions + verifier contract.
9. Implement declarative and/or executable form.
10. Re-run on original targets.
11. Validate on holdout variants.
12. Measure cost and information-gain proxies.
13. Promote / patch / split / deprecate.
14. Add to versioned research skill library.
```

---

# Appendix C — LIDE Measurement Skeleton

```yaml
lide_run:
  domain:
  target:

  before:
    hypothesis_entropy_proxy:
    verified_claims:
    unresolved_claims:

  cost:
    wall_time_seconds:
    model_tokens:
    compute_seconds:
    environment_actions:

  after:
    hypothesis_entropy_proxy:
    verified_claims:
    unresolved_claims:

  quality:
    evidence_strength:
    reproducibility:
    unseen_prediction_accuracy:

  derived:
    local_information_gain:
    lide_score:
```

---

# Appendix D — 一句話命題

> **第一次研究是在解問題；研究軌跡壓縮是在把「解這類問題的方法」也變成可重用的計算資產。**
