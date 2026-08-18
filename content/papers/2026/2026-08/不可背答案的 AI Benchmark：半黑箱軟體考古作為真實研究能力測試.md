---
title: "不可背答案的 AI Benchmark：半黑箱軟體考古作為真實研究能力測試"
english_title: "A Benchmark Whose Target Answer Cannot Be Memorized in Advance: Semi-Black-Box Software Archaeology for Evaluating AI Research Capability"
series: "AI Epistemic Reconstruction Series"
paper: "08"
author: "Neo.K"
date: "2026-08-14"
version: "v0.1"
document_type: "Research Paper / Benchmark Proposal"
language: "zh-Hant"
status: "Research Draft"
benchmark_name: "AER-Bench"
---

# 不可背答案的 AI Benchmark：半黑箱軟體考古作為真實研究能力測試

## A Benchmark Whose Target Answer Cannot Be Memorized in Advance: Semi-Black-Box Software Archaeology for Evaluating AI Research Capability

**作者：Neo.K**  
**系列：AI Epistemic Reconstruction Series — Paper 08**  
**Benchmark：AER-Bench — Active Epistemic Reconstruction Benchmark**  
**版本：v0.1**  
**日期：2026 年 8 月 14 日**

---

## 摘要

大型語言模型 benchmark 面臨一個結構性困難：當測試題、答案、解析、程式碼或相近變體已公開存在於網路上，模型的正確表現可能混合了推理、工具使用、潛在記憶、資料污染與模式匹配。即使一個模型在已知 benchmark 上得到高分，也很難僅由 final answer 區分：

$$
\text{Latent Retrieval}
$$

與：

$$
\text{Active Research}.
$$

本文提出 **AER-Bench（Active Epistemic Reconstruction Benchmark）**，以半黑箱軟體考古、私有變異與現場新證據為核心，測試 AI 是否能在 target-local 答案未預先公開的情況下，主動恢復未知表示、語義與規則。

AER-Bench 不要求模型「零先驗」。相反，受測 Agent 可以擁有：

- CPU / OS / programming language 知識；
- reverse-engineering 技術；
- 公開文件；
- 搜尋引擎；
- 程式執行；
- debugger；
- disassembler；
- historical prior；
- 一般軟體工程知識。

benchmark 唯一刻意隱藏的是：

$$
\boxed{
\Theta_\phi^*
=
(\rho_\phi^*,\delta_\phi^*,J_\phi^*)
}
$$

即某個測試 instance 經私有 mutation seed $\phi$ 產生後的 target-local representation、semantic mapping 與 judgment rules。

核心生成方式：

$$
\boxed{
G_\phi
=
Mutate(G_0,\phi)
}
$$

其中 $\phi$ 在評測 instance 建立時才生成，並保持 evaluator-private。可能的 mutation 包括：

- field relocation；
- semantic permutation；
- threshold mutation；
- constant mutation；
- rule rewiring；
- checksum / serialization variation；
- benign decoy fields；
- version-specific behavior change。

因此，即使模型訓練資料中包含 $G_0$ 的公開攻略、HEX 表或 source，仍不能直接知道：

$$
\phi.
$$

Agent 必須透過：

$$
\boxed{
\text{Prior}
\rightarrow
\text{Hypothesis}
\rightarrow
\text{Experiment}
\rightarrow
\text{Fresh Evidence}
\rightarrow
\text{External Verification}
\rightarrow
\text{Reconstruction}
}
$$

恢復 target-local truth。

本文將 benchmark 評分拆成七個維度：

1. Representation Recovery；
2. Semantic Recovery；
3. Judgment / Rule Recovery；
4. Falsification Quality；
5. Calibration；
6. Research Efficiency；
7. Behavioral Reimplementation Fidelity。

其中最強的終局驗證不是「Agent 說它理解」，而是要求它建立：

$$
\hat G_\phi
$$

並在 evaluator-private unseen traces 上滿足：

$$
O(\hat G_\phi)
\approx
O(G_\phi).
$$

本文同時提出 contamination resistance、fresh evidence ratio、private mutation secrecy、execution-based grading、evidence provenance、budget normalization、human comparison 與 benchmark regeneration 等機制。

AER-Bench 的核心哲學是：

> **允許 AI 帶著所有通用知識進場；只把這一個世界此刻真正的局部答案留到評測當下才生成。**

如此，benchmark 測到的不再只是「模型是否曾見過這個答案」，而更接近：

> **在答案不能被直接預先記住時，Agent 能否利用先驗、工具、外部世界與實驗，把一個局部未知計算系統重新理解出來？**

**關鍵詞：** AI Benchmark, Active Epistemic Reconstruction, Data Contamination, Dynamic Benchmarking, Software Archaeology, Reverse Engineering, Agent Evaluation, Fresh Evidence, Private Mutation, Research Capability

---

# 1. Benchmark 污染不是小問題

假設 benchmark：

$$
B
=
\{(x_i,y_i)\}_{i=1}^n.
$$

若：

$$
(x_i,y_i)
$$

已進入：

- pretraining corpus；
- fine-tuning data；
- synthetic training data；
- search index；
- public solution set；

則：

$$
Score(M,B)
$$

很難被單純解讀為：

> independent problem-solving ability。

---

# 2. LiveBench 的重要接口

LiveBench 的核心設計包括：

1. 使用近期資料來源；
2. 持續更新題目；
3. objective ground-truth scoring；
4. 降低 test-set contamination。

這說明：

$$
\boxed{
\text{Evaluation Freshness}
}
$$

本身已成為 LLM benchmark 的核心設計變量。

---

# 3. 但「題目新」仍不同於「target state 評測當下才生成」

LiveBench 的 freshness 主要來自：

> 新發布資料。

AER-Bench 再往前一步：

$$
\boxed{
\phi
\text{ is generated at evaluation time}
}
$$

所以 target-local answer：

$$
\Theta_\phi^*
$$

在 instance 生成前根本不存在。

---

# 4. RE-Bench 的重要接口

RE-Bench 已建立：

- realistic AI R&D environments；
- open-ended tasks；
- human expert trajectories；
- 2h / 8h / 32h budget comparison。

這證明：

> AI research capability 可以被放進時間受限、工具型、開放式環境，而不只是一次 QA。

AER-Bench 將保留這個精神。

---

# 5. OSWorld 的重要接口

OSWorld 使用：

- real computer environment；
- initial state setup；
- execution-based evaluation；
- reproducible task reset。

AER-Bench 同樣要求：

$$
\boxed{
\text{Executable Environment}
+
\text{Execution-Based Grader}
}
$$

而不是只靠 LLM judge。

---

# 6. SWE-bench 的重要接口

SWE-bench 顯示：

> 真實 codebase + issue + execution environment

能測到遠超傳統 code generation 的能力。

AER-Bench 延伸：

> 不只修已知 issue，而是先恢復 hidden semantics，再完成可驗證重構。

---

# 7. Final Answer Benchmark 的限制

傳統：

```text
Question
→ Answer
→ Score
```

AER-Bench：

```text
Hidden System
→ Inspect
→ Act
→ Experiment
→ Accumulate Evidence
→ Reconstruct
→ Reimplement
→ Execute Hidden Tests
```

---

# 8. Benchmark 的核心不是「不知道知識」

Agent 可以知道：

> x86。

可以知道：

> DOS。

可以知道：

> mutation testing。

甚至可以知道：

> 原版 PM2 的公開金手指。

仍然沒關係。

---

# 9. 我們真正隱藏的是 target-local configuration

$$
\phi.
$$

---

# 10. Target-Local Unknown

定義：

$$
\Theta_\phi^*
=
(\rho_\phi,\delta_\phi,J_\phi).
$$

---

# 11. Representation

$$
\rho_\phi.
$$

例如：

- field offset；
- width；
- endian；
- layout；
- encoding。

---

# 12. Semantic Mapping

$$
\delta_\phi.
$$

例如：

```text
field A = stress
field B = money
```

---

# 13. Judgment Rules

$$
J_\phi.
$$

例如：

```text
if stress > 117:
    event probability changes
```

---

# 14. Benchmark Generator

令 seed：

$$
\phi
\sim
P_\Phi.
$$

產生：

$$
G_\phi
=
M(G_0,\phi).
$$

---

# 15. Benchmark 作者知道答案

Evaluator 保留：

- mutation manifest；
- source spec；
- hidden semantic map；
- hidden tests。

Agent 不可讀。

---

# 16. 對 Agent 而言是黑箱／半黑箱

Agent 可取得：

- binary；
- runtime；
- save files；
- partial docs；
- public prior。

---

# 17. 對 evaluator 而言是 white box

因此可以精確算：

$$
d(
\hat\Theta,
\Theta^*
).
$$

---

# 18. 這是很重要的雙重視角

$$
\boxed{
\text{Black to Agent}
\quad
\text{White to Evaluator}
}
$$

---

# 19. 為什麼不使用純未知真實軟體作唯一 benchmark？

如果連 evaluator 也不知道完整 truth：

> 很難精確打分。

---

# 20. 為什麼不只用 synthetic program？

完全 synthetic：

> 可控，但可能不夠真實。

---

# 21. AER-Bench 建議雙軌

## Track S — Synthetic

完全 evaluator-known。

## Track L — Legacy / Realistic

真實或 clean-room legacy-style system + controlled mutation。

---

# 22. 最佳 benchmark suite

$$
\boxed{
\text{Synthetic Control}
+
\text{Realistic Complexity}
}
$$

---

# 23. Proprietary Legacy Game 的角色

像 PM2 這類研究可作：

> pilot case study。

但公開 benchmark 不應依賴未授權 proprietary assets。

---

# 24. 公開 AER-Bench 建議

建立：

- clean-room legacy-style games；
- open-source old programs；
- synthetic save-based worlds。

---

# 25. PM2 的價值

不是 benchmark distribution asset，

而是：

> 啟發真實 research workflow 與 failure modes。

---

# 26. Benchmark Instance Composition

每個 instance：

$$
I_\phi
=
(G_\phi,D_\phi,T_\phi,B_\phi).
$$

---

# 27. $G_\phi$

Target runtime / binary。

---

# 28. $D_\phi$

Allowed documentation / priors。

---

# 29. $T_\phi$

Tool environment。

---

# 30. $B_\phi$

Budget。

---

# 31. Budget 必須固定

至少：

```text
wall time
model tokens
compute
environment actions
```

---

# 32. 否則

一個 Agent：

> brute-force 100 小時。

另一個：

> 2 小時。

不可直接比 accuracy。

---

# 33. Budget Vector

$$
\boxed{
B
=
(B_T,B_K,B_C,B_A)
}
$$

---

# 34. $B_T$

wall-clock。

---

# 35. $B_K$

model tokens / calls。

---

# 36. $B_C$

compute allowance。

---

# 37. $B_A$

environment interaction count。

---

# 38. Multiple Budget Curves

像 RE-Bench，

應看：

$$
Performance(B).
$$

不是只看單一 budget。

---

# 39. 例如

```text
30 min
2 h
8 h
24 h
```

---

# 40. Research Return Curve

$$
R(B)
=
Score(B).
$$

---

# 41. 邊際收益

$$
\frac{dR}{dB}.
$$

非常重要。

---

# 42. 某 Agent 起步快

但長時間不會改善。

---

# 43. 另一 Agent 慢

但長時間持續收斂。

---

# 44. 這是長時研究能力的重要區別

---

# 45. Mutation Family 1 — Constant Mutation

原：

$$
c=100.
$$

新：

$$
c'=117.
$$

---

# 46. 用途

測：

> 背攻略 vs 現場驗證。

---

# 47. Mutation Family 2 — Field Relocation

$$
offset(x)
\rightarrow
offset'(x).
$$

---

# 48. 用途

測：

> 是否只背 offset。

---

# 49. Mutation Family 3 — Semantic Permutation

原：

```text
A = Money
B = Stress
```

新：

```text
A = Stress
B = Money
```

但 UI / rules 同步更新。

---

# 50. 用途

測：

> 是否真正透過 intervention 建立 mapping。

---

# 51. Mutation Family 4 — Judgment Mutation

representation 不動。

改：

$$
J.
$$

---

# 52. 例如

```text
stress threshold:
100 → 117
```

---

# 53. 用途

測：

> 找到 field 是否等於理解 rule。

---

# 54. Mutation Family 5 — Serialization Mutation

例如：

- field width；
- byte order；
- checksum；
- version tag。

---

# 55. Mutation Family 6 — Decoy Fields

加入：

```text
fake stress cache
```

數值看起來相關，

但不驅動 behavior。

---

# 56. 用途

測 Paper 02：

> semantic label vs judgment role。

---

# 57. Mutation Family 7 — Hidden State

某 behavior 還依賴：

$$
z.
$$

讓簡單單變量模型失敗。

---

# 58. 用途

測：

> contradiction 後是否 reframe。

---

# 59. Mutation Family 8 — Tool / UI Noise

可加入可控：

- timing variability；
- irrelevant file change；
- UI-only state。

---

# 60. 但不能太多

不然變成：

> 測 UI 苦工，

而不是 research reasoning。

---

# 61. Difficulty Scaling

難度可以由：

$$
d_\phi
$$

控制：

- hidden fields；
- decoys；
- interaction depth；
- stochasticity；
- tool latency。

---

# 62. Level 0

單一 visible variable。

---

# 63. Level 1

單一 hidden field。

---

# 64. Level 2

多 field + decoy。

---

# 65. Level 3

rule dependency。

---

# 66. Level 4

cross-version / hidden state。

---

# 67. Level 5

partial nondeterminism + multi-stage semantics。

---

# 68. Fresh Evidence

Agent action：

$$
a_t
$$

產生：

$$
e_{t+1}.
$$

---

# 69. Fresh Evidence Criterion

若：

1. instance 生成後才存在；
2. 由 target runtime 產生；
3. evaluator 可 verify；
4. 有 provenance；

則標：

$$
Fresh(e)=1.
$$

---

# 70. Fresh Evidence Ratio

定義：

$$
\boxed{
FER
=
\frac{
N_{\mathrm{target\ claims\ supported\ by\ fresh\ evidence}}
}{
N_{\mathrm{target\ claims}}
}
}
$$

---

# 71. FER 高

代表 final mapping 更多依賴：

> 現場證據。

---

# 72. 但不要求 FER = 1

歷史 prior 有價值。

---

# 73. Benchmark 不是禁止 prior

而是：

> prior 不能單獨取得 private mutation answer。

---

# 74. Historical Prior Trap

可以故意提供：

```text
public original offset = 0x50
```

但 private target：

```text
offset = 0x72
```

---

# 75. 好 Agent

把 0x50 當 prior，

然後驗證。

---

# 76. Memorization-Dominant Agent

直接回答 0x50。

---

# 77. 這不是懲罰使用知識

而是測：

> 是否知道 prior 需要 target validation。

---

# 78. False Prior Track

更進一步可加入 evaluator-known：

> outdated docs。

---

# 79. 但倫理上／設計上要明確

不能讓 benchmark 變成純 deception puzzle。

---

# 80. Outdated Prior 應符合真實版本考古情境

---

# 81. Agent Output 不只 final answer

必須交：

$$
\boxed{
\text{Epistemic Reconstruction Package}
}
$$

---

# 82. Package 內容

```text
semantic map
rule map
confidence
evidence pointers
invalidated hypotheses
unknowns
reimplementation
```

---

# 83. 不要求 Chain-of-Thought

只要求：

> externalizable research record。

---

# 84. Benchmark Artifact

```yaml
claim:
  statement:
  confidence:
  status:
  evidence_ids:
  prediction:
```

---

# 85. Evidence Store

每個 experiment：

```text
action
input
output
hash
scope
```

---

# 86. Scoring Dimension 1 — Representation Recovery

$$
A_\rho.
$$

測：

- offset；
- width；
- endian；
- encoding；
- structure。

---

# 87. Dimension 2 — Semantic Recovery

$$
A_\delta.
$$

測：

> field meaning。

---

# 88. Dimension 3 — Judgment Recovery

$$
A_J.
$$

測：

> state 如何進入 rule / behavior。

---

# 89. Judgment 比 label 更重要

因為：

> 找到 Stress 不等於知道 Stress 怎麼用。

---

# 90. Dimension 4 — Falsification Quality

$$
F_Q.
$$

測：

- rejection conditions；
- contradiction response；
- invalidated memory；
- excluded run hygiene。

---

# 91. Dimension 5 — Calibration

$$
C_Q.
$$

UNKNOWN 能不能老實標 unknown。

---

# 92. Calibration 不應獎勵永遠低 confidence

需 proper scoring。

---

# 93. Dimension 6 — Research Efficiency

$$
\eta.
$$

---

# 94. 可使用

$$
\eta
=
\frac{
Score_{\mathrm{semantic}}
}{
C_{\mathrm{normalized}}
}.
$$

---

# 95. 或沿 Paper 06

$$
\eta_D
=
\frac{
\Delta I_D
}{
C
}.
$$

---

# 96. Dimension 7 — Behavioral Reimplementation

$$
F_R.
$$

---

# 97. 終局

Agent 建：

$$
\hat G_\phi.
$$

---

# 98. Evaluator 給 hidden traces

$$
X_{\mathrm{hidden}}.
$$

---

# 99. 比較

$$
\boxed{
F_R
=
1-
d(
O(\hat G_\phi,X),
O(G_\phi,X)
)
}
$$

---

# 100. 這是最硬的一層

因為：

> 描述可以說對一半。

行為重建會把錯誤暴露出來。

---

# 101. 但 behavioral equivalence 也有 observation contract

不用 bit-identical。

---

# 102. Contract

$$
\mathcal O
=
\{
state,
event,
output,
save,
timing?
\}.
$$

---

# 103. 哪些 timing 要不要算

由 benchmark task 定義。

---

# 104. Composite Score

$$
\boxed{
S
=
w_\rho A_\rho
+
w_\delta A_\delta
+
w_J A_J
+
w_F F_Q
+
w_C C_Q
+
w_\eta \eta
+
w_R F_R
}
$$

---

# 105. 建議不只公布總分

還要 radar / vector。

---

# 106. Agent A

語義高，

效率低。

---

# 107. Agent B

效率高，

但 calibration 差。

---

# 108. 不能用一個數字掩蓋

---

# 109. Research Efficiency Scoring

需要避免：

> 不做實驗，亂猜，省成本。

---

# 110. 因此 efficiency 只在 minimum quality threshold 以上計分。

---

# 111. Quality Gate

若：

$$
A_{\mathrm{semantic}}<\tau,
$$

則：

$$
EfficiencyBonus=0.
$$

---

# 112. Research Budget Fairness

不同模型 API 成本難統一。

至少同時報：

- wall time；
- tokens；
- tool calls；
- environment actions。

---

# 113. Human Baseline

像 RE-Bench，

需要：

> skilled human reverse engineers / software researchers。

---

# 114. Human 不一定要做所有 level

先在小型 suite。

---

# 115. Human Trace

保存：

- actions；
- tools；
- findings；
- time。

---

# 116. 比較

$$
R_H(B)
$$

與：

$$
R_A(B).
$$

---

# 117. 不只比較 final accuracy

還比較：

- information gain curve；
- action choice；
- time-to-first-anchor；
- replication behavior。

---

# 118. Time-to-Anchor

定義：

$$
T_A(c)
$$

找到第一個重要 verified semantic anchor 所需時間。

---

# 119. Time-to-Rule

$$
T_J.
$$

---

# 120. Time-to-Reimplementation

$$
T_R.
$$

---

# 121. Falsification Latency

錯 hypothesis：

$$
h^-.
$$

從提出到 invalidated：

$$
T_F.
$$

---

# 122. Error Half-Life

延續 Paper 04：

$$
T_{1/2}^{error}.
$$

---

# 123. Repeated Error Rate

$$
R_E
=
\frac{
N_{\mathrm{repeated\ invalidated\ claims}}
}{
N_{\mathrm{invalidated\ claims}}
}.
$$

---

# 124. Memory Continuity

做 context reset：

> Agent 能不能從 external epistemic state 恢復？

---

# 125. Reset Challenge

Benchmark 可在中途：

```text
restart agent session
```

保留合法 external memory。

---

# 126. 測 Paper 05

是否真的：

> evidence-backed memory。

---

# 127. Trajectory Transfer Challenge

第二個 instance：

$$
G_{\phi_2}.
$$

允許使用第一個 instance 學到的 Research Options，

但不能讀 $\phi_2$。

---

# 128. 測 Paper 06

$$
C_2<C_1?
$$

---

# 129. Skill Contamination Problem

研究 skill 不能偷偷包含：

```text
answer = 0x50.
```

---

# 130. Skill Auditor

檢查：

> skill 是否 target-invariant。

---

# 131. Target-Invariant Skill

例如：

```text
use single-variable intervention
```

---

# 132. Target-Leaking Skill

例如：

```text
stress is always offset 0x50
```

---

# 133. Skill Transfer Score

$$
S_T.
$$

---

# 134. Benchmark Regeneration

LiveBench 的啟發：

> benchmark 要持續更新。

AER-Bench 更適合：

$$
\boxed{
\text{generate fresh instances continuously}
}
$$

---

# 135. Seed Rotation

每個 evaluation：

$$
\phi_t.
$$

---

# 136. Public Generator / Private Seed

最佳：

- generator logic public；
- seed private until evaluation over。

---

# 137. 但 generator 完全公開可能讓 Agent exploit mutation grammar

---

# 138. 因此可有

```text
public mutation classes
private exact generators
```

---

# 139. Benchmark Security

需要防：

- hidden file leakage；
- environment variable leakage；
- test extraction；
- grader tampering。

---

# 140. Agent Permission Boundary

允許：

- inspect target；
- execute；
- debug。

禁止：

- read evaluator secret；
- modify hidden tests；
- access mutation manifest。

---

# 141. 這和真正研究很類似

可以研究物體，

不能翻答案本。

---

# 142. Grader Integrity

Paper 04 的 verifier integrity boundary 在這裡很重要。

---

# 143. Agent 不得改：

$$
V_{\mathrm{hidden}}.
$$

---

# 144. 但是可以寫自己的 tests

而且應鼓勵。

---

# 145. Self-Generated Tests

這本身是能力。

---

# 146. Mutation Testing 的歷史接口

軟體測試很早就使用：

> program mutants

來評估 test 是否能區分正確程式與帶有人工 defect 的變體。

AER-Bench 的 private mutation 與此不同，

但共享：

> **人工產生有控制的行為差異，測試觀測／驗證能力。**

---

# 147. Metamorphic Testing 的接口

當沒有單一簡單 oracle，

可使用：

> related inputs / outputs 間應保持的 relation。

AER-Bench 某些 task 可加入 metamorphic relations。

---

# 148. 例如

如果只換 save slot：

> canonical state 應不變。

---

# 149. Metamorphic Property

$$
f(T(x))
=
R(f(x)).
$$

---

# 150. 這可測 Agent 是否找到 invariant

---

# 151. Dynamic Code Benchmark 的接口

近年的 dynamic code benchmark 也利用：

> 問題變體／動態生成

降低固定 dataset contamination。

AER-Bench 把這種思想搬到：

> executable black-box semantics。

---

# 152. LiveBench vs AER-Bench

LiveBench：

> fresh questions + objective ground truth。

AER-Bench：

> fresh executable worlds + hidden semantic ground truth。

---

# 153. RE-Bench vs AER-Bench

RE-Bench：

> realistic AI R&D task。

AER-Bench：

> target semantics intentionally hidden / mutated for contamination resistance。

---

# 154. OSWorld vs AER-Bench

OSWorld：

> real computer interaction。

AER-Bench：

> interaction 是取得 unknown semantics 的手段，而不只是完成 user task。

---

# 155. SWE-bench vs AER-Bench

SWE-bench：

> issue → code patch。

AER-Bench：

> unknown system → semantic model → verified reimplementation。

---

# 156. Benchmark 不應變成 CTF

這一點很重要。

AER-Bench 不是：

> 誰會 exploitation。

---

# 157. 目標是研究方法

所以 target 應：

- safe；
- local；
- sandboxed；
- no real credential；
- no hostile target。

---

# 158. Reverse Engineering Scope

只使用：

- benchmark-owned；
- open-source；
- clean-room；
- licensed artifacts。

---

# 159. 不鼓勵對第三方未授權系統做逆向 benchmark。

---

# 160. Task Family 1 — Save Archaeology

給：

- binary；
- save；
- runtime。

找：

- fields；
- rules；
- serialization。

---

# 161. Task Family 2 — Custom File Format

找：

- container；
- records；
- compression；
- checksums。

---

# 162. Task Family 3 — Event Engine

找：

- trigger；
- priority；
- hidden flags；
- transition。

---

# 163. Task Family 4 — Tiny VM

找：

- opcode semantics；
- stack；
- control flow。

---

# 164. Task Family 5 — Legacy UI State Machine

找：

- state；
- transitions；
- persistence。

---

# 165. Task Family 6 — Cross-Version Semantic Diff

兩版本：

$$
G_1,G_2.
$$

找：

$$
\Delta\rho,\Delta\delta,\Delta J.
$$

---

# 166. Task Family 7 — Reimplementation

只有黑箱 behavior。

重建：

$$
\hat G.
$$

---

# 167. Synthetic Legacy Game

最理想 initial benchmark：

- 2D / text UI；
- 20–100 state variables；
- save file；
- event rules；
- RNG；
- hidden flags。

---

# 168. 為什麼遊戲很好

遊戲：

- state rich；
- resettable；
- safe；
- observable；
- reproducible。

---

# 169. 又有世界性

Agent 可以：

> action → consequence。

---

# 170. 但不要一開始做超大遊戲

Benchmark 應可控。

---

# 171. Small Yet Deep

目標：

$$
\operatorname{Bytes}(G)
$$

小，

但：

$$
\operatorname{SemanticDepth}(G)
$$

高。

---

# 172. 這也延續 PM2 啟發

10 MB 不等於簡單。

---

# 173. Ground-Truth Semantic Graph

Evaluator 保留：

$$
G_\Sigma.
$$

---

# 174. Node

- state；
- rule；
- event；
- serialization field。

---

# 175. Edge

- reads；
- writes；
- triggers；
- encodes。

---

# 176. Agent Output Graph

$$
\hat G_\Sigma.
$$

---

# 177. Graph Matching

計算：

- node precision / recall；
- edge precision / recall；
- weighted importance。

---

# 178. Weighted Semantics

不是每個 field 等價重要。

---

# 179. High-Impact Rules

權重高。

---

# 180. Decoy fields

權重低或 special score。

---

# 181. Hidden Rule Test

讓 Agent 必須：

> discover behavior not obvious from static bytes。

---

# 182. Static-only Baseline

作對照：

$$
M_{static}.
$$

---

# 183. Active Agent

$$
M_{active}.
$$

---

# 184. 核心實驗

比較：

$$
Score(M_{active})
-
Score(M_{static}).
$$

---

# 185. 直接測 Paper 03

active experimentation 的增益。

---

# 186. No-Verifier Baseline

移除：

- hidden execution checks？

至少讓 Agent final response 無 runtime feedback。

---

# 187. 比較 Paper 04

external falsification 是否提升。

---

# 188. Summary-Only Memory Baseline

只給 prose summary。

---

# 189. Pointer Memory Agent

給 evidence-backed state。

---

# 190. 比較 Paper 05

---

# 191. No-Skill Baseline

每 instance 從零。

---

# 192. Skill-Library Agent

可 reuse research options。

---

# 193. 比較 Paper 06

---

# 194. Full-Agent vs Agent+Automation

穩定 loops：

- LLM 全做；
- deterministic tool 做。

---

# 195. 比較 Paper 07

---

# 196. 這使一個 benchmark 可以驗證整個系列

---

# 197. Ablation Matrix

```text
Prior
Tools
External Verifier
Persistent Memory
Research Skills
Automation
```

逐一移除。

---

# 198. Agent Architecture Neutrality

AER-Bench 不限定：

- ReAct；
- planner；
- model family。

只限定：

> I/O、permissions、budget、grader。

---

# 199. 模型可以是 closed / open / local

---

# 200. Benchmark 得分必須記錄環境

```text
model
version
agent scaffold
tools
budget
date
```

---

# 201. 因為 Agent 能力不是只有 model

Paper 01 已經指出。

---

# 202. 不公平比較

```text
Model A + debugger + 8h
vs
Model B no tools + 5min
```

無意義。

---

# 203. Standard Tool Profiles

建立：

```text
T0 text only
T1 filesystem + python
T2 debugger + disassembler
T3 full research toolkit
```

---

# 204. 這能看 tool leverage

---

# 205. Tool Leverage

$$
L_T
=
Score(T_3)-Score(T_0).
$$

---

# 206. Prior Profile

```text
P0 no historical prior
P1 public docs
P2 public historical cheats/tools
```

---

# 207. Prior Leverage

$$
L_P.
$$

---

# 208. Mutation Robustness

同一 base：

$$
G_{\phi_1},\ldots,G_{\phi_n}.
$$

---

# 209. Score variance

$$
Var_\phi(Score).
$$

---

# 210. Memorization-heavy Agent

對 public-original-like instance 高，

mutation 後掉很多。

---

# 211. Reconstruction-heavy Agent

mutation robustness 較高。

---

# 212. Mutation Robustness Score

$$
\boxed{
MRS
=
1-
\frac{
Score(G_0)-\mathbb E_\phi Score(G_\phi)
}{
Score(G_0)+\epsilon
}
}
$$

概念式。

---

# 213. Contamination Resistance 指標

不能證明 training corpus 內沒有相關知識。

但可以使：

> exact target answer 不可能完整預先存在。

---

# 214. 這是一個較精確的 claim

不要說：

> 絕對不可作弊。

---

# 215. 正確說法

$$
\boxed{
\text{Target-local answer is generated after model training and withheld from the agent.}
}
$$

---

# 216. 如果模型預先知道 generator

它仍可能：

> 猜 mutation distribution。

---

# 217. 但只要 seed private，

仍要識別這次：

$$
\phi.
$$

---

# 218. Random Guess Baseline

需要建立。

---

# 219. Mutation entropy

$$
H(\Phi)
$$

必須足夠大。

---

# 220. 太小

Agent 可以：

> enumerate all mutations。

---

# 221. 太大

研究不可識別。

---

# 222. 所以設計要平衡

$$
\boxed{
\text{Mutation Diversity}
+
\text{Experimental Identifiability}
}
$$

---

# 223. Identifiability

對不同：

$$
\phi_i,\phi_j,
$$

存在 allowed action：

$$
a
$$

使：

$$
P(o\mid\phi_i,a)
\neq
P(o\mid\phi_j,a).
$$

---

# 224. 否則 benchmark 只是猜。

---

# 225. Difficulty 應來自「要設計好實驗」

不是來自：

> evaluator 故意藏到無法觀察。

---

# 226. Benchmark Quality Principle 1

**Solvable by evidence.**

---

# 227. Principle 2

**Not solvable by answer leakage alone.**

---

# 228. Principle 3

**Execution-based grading.**

---

# 229. Principle 4

**Fresh target-local variation.**

---

# 230. Principle 5

**Reproducible environments.**

---

# 231. Principle 6

**Evidence provenance.**

---

# 232. Principle 7

**Budgeted long-horizon evaluation.**

---

# 233. Principle 8

**Partial-credit semantic scoring.**

---

# 234. Principle 9

**Explicit UNKNOWN allowed.**

---

# 235. Principle 10

**Behavioral reimplementation as strong final check.**

---

# 236. Benchmark Lifecycle

```text
Base templates
→ generate private mutations
→ package sandbox
→ run agents
→ collect epistemic trace
→ hidden evaluation
→ reveal mutation after closure
→ archive results
→ rotate seeds
```

---

# 237. Reveal Policy

評測關閉後可以公開：

- instance；
- mutation；
- trajectories。

---

# 238. 下一輪用新 seed

防止 benchmark stagnation。

---

# 239. Leaderboard

應按：

```text
model
agent
tool profile
budget
benchmark version
```

分列。

---

# 240. 不應只有一個「AI 排名」

---

# 241. Human Expert Track

也需同 tool profile。

---

# 242. Human + AI Track

甚至可測：

> hybrid team。

---

# 243. 因為真科研未來很可能是 hybrid。

---

# 244. Team Score

可以比較：

$$
H,
A,
H+A.
$$

---

# 245. 這也測 Paper 07 的 labor routing

---

# 246. Benchmark Pilot — PM2-Inspired Clean-Room

建立一個全新：

```text
Princess-like raising simulator
```

但不使用原角色、資產或 code。

---

# 247. 內含

- monthly schedule；
- 30 stats；
- hidden relationships；
- event thresholds；
- save file；
- RNG；
- endings。

---

# 248. Private mutation

每 instance：

- reorder save fields；
- change thresholds；
- alter event priority；
- change checksum；
- decoys。

---

# 249. Agent task

> Recover enough semantic specification to reproduce behavior.

---

# 250. 這會非常貼近我們真實 PM2 workflow

但 legal / distribution 更乾淨。

---

# 251. Benchmark Pilot 2 — Tiny DOS-like VM

自建：

- 16-bit-like bytecode；
- undocumented opcodes；
- stateful saves。

---

# 252. Agent 可：

- disassemble；
- execute；
- probe。

---

# 253. Hidden mutations

opcode remap / constant change。

---

# 254. Pilot 3 — Custom Archive Format

Agent 必須：

- parse；
- identify records；
- reconstruct exporter/importer。

---

# 255. 三個 pilot 能覆蓋

$$
\rho,\delta,J.
$$

---

# 256. Research Artifact Requirements

Agent 最後提交：

```text
semantic_spec.yaml
evidence_graph.json
reimplementation/
report.md
unknowns.yaml
```

---

# 257. semantic_spec

Evaluator 比對 hidden truth。

---

# 258. evidence_graph

測 provenance / falsification。

---

# 259. reimplementation

跑 hidden behavioral tests。

---

# 260. unknowns

測 calibration。

---

# 261. report

只做人類閱讀，

不作主要 grader。

---

# 262. Automatic Grading First

避免：

> LLM judge bias。

LiveBench 的 objective scoring 精神值得延續。

---

# 263. 但某些 semantic equivalence 可能多解

需要 graph canonicalization / behavior tests。

---

# 264. 不應要求變量名稱完全一樣

Agent 叫：

```text
stress_level
```

Evaluator 叫：

```text
fatigue_pressure
```

如果 behavior 對，

應可匹配。

---

# 265. Semantic Alignment Grader

可依：

- interventions；
- read/write relations；
- behavior。

而非只 string match。

---

# 266. Hidden Probe Set

Evaluator 對 Agent mapping 問：

```text
If this field is changed, predict X.
```

---

# 267. 這比 label string 更強。

---

# 268. Reimplementation Hidden Tests

包含：

- seen-like；
- boundary；
- unseen combination；
- negative control；
- mutation-specific edge。

---

# 269. Holdout Trace

Agent 研究期間看不到。

---

# 270. 防 overfit。

---

# 271. Benchmark 的「研究」成分

如果只要求：

> 最後 parse file。

可能退化成 coding task。

---

# 272. 所以需要 hidden semantics + interactive experiments。

---

# 273. Research Necessity Criterion

若靜態一次分析即可幾乎滿分，

則 task 的 AER 強度不足。

---

# 274. 定義

$$
AERGap
=
Score_{\mathrm{active}}
-
Score_{\mathrm{static}}.
$$

---

# 275. 理想 task

$$
AERGap>0
$$

顯著。

---

# 276. Experiment Value

Agent 真的需要：

> 問世界。

---

# 277. 這就是 Paper 03 的 benchmark 化。

---

# 278. Falsification Necessity

加入 decoy / false prior，

讓沒有 Paper 04 能力的 Agent 容易錯。

---

# 279. Memory Necessity

長 task + reset，

測 Paper 05。

---

# 280. Skill Transfer Necessity

multi-instance，

測 Paper 06。

---

# 281. Labor Routing Necessity

routine protocol + exceptions，

測 Paper 07。

---

# 282. 所以前七篇不是背景裝飾

全部都有 ablation。

---

# 283. Series-to-Benchmark Mapping

```text
Paper 01 → Model/Tool/Verifier ablation
Paper 02 → Representation/Semantic/Judgment scores
Paper 03 → Active-vs-static experiment gap
Paper 04 → Contradiction / falsification tests
Paper 05 → Reset / memory continuity
Paper 06 → Multi-instance trajectory transfer
Paper 07 → Agent-vs-automation routing
```

---

# 284. Paper 08 是系列的實驗封頂

---

# 285. 可證偽預測一

Private mutation 會降低只依賴 public original answer 的 Agent 表現。

---

# 286. 可證偽預測二

Active experiment access 應提高：

$$
A_\delta,A_J.
$$

---

# 287. 可證偽預測三

External verifier access 應降低 persistent false hypotheses。

---

# 288. 可證偽預測四

Pointer-backed memory 應提高 reset 後 continuity。

---

# 289. 可證偽預測五

Validated skill library 應降低第二個同類 instance 的 cost。

---

# 290. 可證偽預測六

Routine automation 應降低 token cost，但不降低 verifier-defined fidelity。

---

# 291. 可證偽預測七

Mutation robustness 應比 public benchmark original score 更能區分 memorization-heavy 與 reconstruction-heavy behavior。

---

# 292. 可證偽預測八

Behavioral reimplementation score 與 semantic graph score應正相關，但不完全等同。

---

# 293. 可證偽預測九

允許 UNKNOWN 且校準計分，應降低 overclaim。

---

# 294. 可證偽預測十

較高 LIDE 的 Agent 應在固定 budget 下更快達到 verified anchor。

---

# 295. 限制一：不能完全證明模型沒見過所有相關模式

AER-Bench 只能控制：

> exact target-local mutation。

---

# 296. 模型仍然有大量相似先驗

這是允許的。

---

# 297. 限制二：Mutation 可能引入不自然 artifact

如果 permutation 太人工，

Agent 只學：

> benchmark generator quirks。

---

# 298. 所以 mutation 要 behaviorally plausible。

---

# 299. 限制三：Benchmark Generator 會被研究

公開後 Agent 可能特化。

---

# 300. 需要多 generator / hidden seed / rotation。

---

# 301. 限制四：Execution cost 高

長時 benchmark 很貴。

---

# 302. 建議分

```text
AER-Mini
AER-Standard
AER-Long
```

---

# 303. AER-Mini

5–30 min。

---

# 304. AER-Standard

1–4 h。

---

# 305. AER-Long

8–24 h。

---

# 306. 限制五：Human baseline 很昂貴

先小規模 expert study。

---

# 307. 限制六：Reverse engineering skill 不是所有 research skill

這是一種 research substrate，

不能直接代表全部科學。

---

# 308. 但它有優點

- ground truth；
- reset；
- safety；
- controllability；
- fresh evidence。

---

# 309. 限制七：Tooling 差異巨大

需固定 tool profile。

---

# 310. 限制八：Agent 可能 exploit evaluator

要做 adversarial benchmark audit。

---

# 311. 限制九：Synthetic tasks 可能太 toy

所以要 legacy-realistic track。

---

# 312. 限制十：Realistic legacy tasks 又可能有 licensing / provenance 問題

所以 clean-room design 很重要。

---

# 313. 核心命題一

## Proposition 1 — Evaluation-Time Private Mutation Reduces Exact-Answer Memorization as a Sufficient Explanation

若：

$$
\phi
$$

在模型訓練完成後才生成，

且不向 Agent 洩漏，

則模型不能直接從訓練 corpus 記住：

$$
\phi
$$

本身。

---

# 314. 注意

它仍可使用 general prior 推測。

---

# 315. 核心命題二

## Proposition 2 — Interactive Fresh Evidence Makes Target-Local Reconstruction Measurable

若 target-local semantic differences 對 allowed actions 可識別，

則 Agent 可透過 interaction 產生 fresh evidence 來恢復：

$$
\Theta_\phi.
$$

---

# 316. 核心命題三

## Proposition 3 — Behavioral Reimplementation Is a Stronger Test of Semantic Understanding Than Verbal Description Alone

若：

$$
\hat G
$$

在 unseen traces 保持 behavior，

則至少對 observation contract，Agent 的 semantic model 具有外部支持。

---

# 317. 核心命題四

## Proposition 4 — A Dynamic Benchmark Can Separate Prior Use from Prior Obedience

Historical prior 可以提高搜尋效率，

但 private mutation 使 Agent 必須驗證 prior，而不能盲從。

---

# 318. 核心命題五

## Proposition 5 — Multi-Dimensional Scoring Better Represents Research Capability Than Final Accuracy Alone

因為 research agent 的：

- calibration；
- efficiency；
- falsification；
- memory；

可能在同 final accuracy 下顯著不同。

---

# 319. 核心命題六

## Proposition 6 — AER-Bench Can Serve as a Systems Benchmark for the Entire Epistemic Reconstruction Stack

因其可對：

$$
M,T,E,S,V,\Pi
$$

做 ablation，

測試 Paper 01 的 system view。

---

# 320. 核心命題七

## Proposition 7 — Benchmark Regeneration Is Part of Benchmark Validity

在快速變化模型時代，

static dataset 的有效期有限。

因此：

$$
\boxed{
\text{Fresh Instance Generation}
}
$$

應是 benchmark architecture，而不是事後維護。

---

# 321. 統一架構

```text
PUBLIC KNOWLEDGE
docs / ISA / tools / historical priors
              │
              ▼
       PRIVATE INSTANCE GENERATOR
              │
      mutation seed φ
              │
              ▼
      SEMI-BLACK-BOX TARGET Gφ
              │
         ┌────┴─────┐
         ▼          ▼
      STATIC      ACTIVE
     INSPECTION  EXPERIMENTS
         │          │
         └────┬─────┘
              ▼
         FRESH EVIDENCE
              │
              ▼
       EPISTEMIC RECONSTRUCTION
    ρ̂ / δ̂ / Ĵ / confidence / unknown
              │
              ▼
        REIMPLEMENTATION Ĝφ
              │
              ▼
        HIDDEN EXECUTION TESTS
              │
              ▼
    MULTI-DIMENSIONAL SCORE VECTOR
```

---

# 322. 最終 benchmark 公式

Instance：

$$
G_\phi
=
Mutate(G_0,\phi).
$$

Agent：

$$
\mathcal A
=
(M,T,E,S,V,\Pi).
$$

Output：

$$
Y
=
(\hat\rho,\hat\delta,\hat J,\hat G,K,E).
$$

Score：

$$
\boxed{
Score(
\mathcal A,
G_\phi,
B
)
=
F(
A_\rho,
A_\delta,
A_J,
F_Q,
C_Q,
\eta,
F_R
)
}
$$

---

# 323. 最終結論

「AI 到底是真的會研究，還是只是把訓練資料裡的答案重新組合？」這個問題若只靠哲學辯論，很難結束。

更好的方法是：

> **設計一個 target-local 答案在評測當下才生成、模型可以自由使用通用知識、但必須透過實驗才能知道這一次世界真正如何運作的 benchmark。**

AER-Bench 因此不追求「無先驗」。

它追求：

$$
\boxed{
\text{Known Methods}
+
\text{Unknown Local Truth}
}
$$

這更接近真實研究。

科學家不是沒有先驗。

工程師不是不知道工具。

真正的研究問題通常是：

> **你已經知道很多東西，但眼前這個具體世界仍有一部分沒有告訴你。你能不能想辦法讓它自己把答案露出來？**

半黑箱軟體考古提供一個少見的理想 sandbox：

- 世界可以 reset；
- evidence 可以 hash；
- experiment 可以重播；
- ground truth 可以由 evaluator 保留；
- private mutation 可以在訓練後生成；
- Agent 可以使用真實工具；
- 最後還可以重實作驗證理解。

因此本文提出：

$$
\boxed{
\textbf{AER-Bench}
}
$$

作為一種研究能力 benchmark：

> **不是問 AI「你知道答案嗎？」；而是把一個它不可能預先知道這次局部答案的可執行世界放在它面前，然後觀察它是否知道如何提出假說、取得證據、接受反駁、保存不確定性、壓縮研究狀態、學習研究技能，最後重新生成足以匹配原世界行為的模型。**

這正是前七篇理論最終可以被實驗化的地方。

---

# 324. 系列總結

整個 **AI Epistemic Reconstruction Series** 最終形成：

### Paper 01

概率—確定性混合認識系統：

$$
\mathcal A=(M,T,E,S,V,\Pi).
$$

### Paper 02

位元到語義：

$$
B\rightarrow R\rightarrow S\rightarrow J\rightarrow O.
$$

### Paper 03

主動認識重構：

$$
Prior\rightarrow Hypothesis\rightarrow Experiment\rightarrow Evidence.
$$

### Paper 04

世界反駁：

$$
Hypothesis\rightarrow External\ Falsification.
$$

### Paper 05

證據再壓縮：

$$
R\rightarrow K\rightarrow A.
$$

### Paper 06

研究軌跡壓縮：

$$
\Pi\rightarrow\Omega.
$$

### Paper 07

認識勞動重分配：

$$
Human\leftrightarrow Agent\leftrightarrow Automation.
$$

### Paper 08

全部進入可執行 benchmark：

$$
\boxed{
\text{AER-Bench}
}
$$

因此整個系列的總命題可以濃縮成：

$$
\boxed{
\text{AI Research Capability}
\neq
\text{Static Answer Accuracy}
}
$$

而更接近：

$$
\boxed{
\text{AI Research Capability}
=
\text{Prior Use}
+
\text{Active Experimentation}
+
\text{External Falsification}
+
\text{Evidence Memory}
+
\text{Trajectory Learning}
+
\text{Verified Reconstruction}
}
$$

---

# References

[1] White, C., Dooley, S., Roberts, M., et al. **LiveBench: A Challenging, Contamination-Free LLM Benchmark.** arXiv:2406.19314, 2024.  
https://arxiv.org/abs/2406.19314

[2] Wijk, H., Lin, T., Becker, J., et al. **RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts.** arXiv:2411.15114, 2024.  
https://arxiv.org/abs/2411.15114

[3] Xie, T., Zhang, D., Chen, J., et al. **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments.** arXiv:2404.07972, 2024.  
https://arxiv.org/abs/2404.07972

[4] Jimenez, C. E., Yang, J., Wettig, A., et al. **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** arXiv:2310.06770, 2023.  
https://arxiv.org/abs/2310.06770

[5] Chen, S., Pusarla, P., & Ray, B. **Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contamination.** arXiv:2503.04149, 2025.  
https://arxiv.org/abs/2503.04149

[6] DeMillo, R. A., Lipton, R. J., & Sayward, F. G. **Hints on Test Data Selection: Help for the Practicing Programmer.** Computer 11(4), 34–41, 1978. DOI: 10.1109/C-M.1978.218136.  
https://doi.org/10.1109/C-M.1978.218136

[7] Chan, F. T., Chen, T. Y., Cheung, S. C., Lau, M. F., & Yiu, S. M. **Application of Metamorphic Testing in Numerical Analysis.** SE'98, 1998.  
https://hdl.handle.net/1783.1/70576

---

# Appendix A — AER-Bench Task Instance

```yaml
aer_bench_instance:
  benchmark_version:
  instance_id:

  template:
    id:
    family:

  mutation:
    private_seed:
    manifest_private: true
    families: []

  target:
    artifact_hashes: []
    runtime:
    reset_method:

  agent_permissions:
    filesystem:
    execute:
    debug:
    internet:
    historical_priors:
    hidden_evaluator_access: false

  budget:
    wall_time_seconds:
    model_tokens:
    compute:
    environment_actions:

  required_outputs:
    semantic_spec:
    evidence_graph:
    reimplementation:
    unknowns:

  hidden_evaluation:
    semantic_graph:
    behavioral_tests:
    holdout_traces:
```

---

# Appendix B — AER-Bench Scoring Vector

```text
Aρ   Representation Recovery
Aδ   Semantic Recovery
AJ   Judgment / Rule Recovery
FQ   Falsification Quality
CQ   Calibration Quality
η    Research Efficiency
FR   Behavioral Reimplementation Fidelity
FER  Fresh Evidence Ratio
MRS  Mutation Robustness Score
```

---

# Appendix C — Agent Research Record

```yaml
research_record:
  hypothesis:
    id:
    claim:
    confidence:
    status:

  experiment:
    id:
    action:
    expected_discrimination:
    cost:

  observation:
    fresh:
    raw_evidence:
    artifact_hashes:

  verdict:
    supports:
    contradicts:
    inconclusive:

  update:
    confidence_before:
    confidence_after:
    new_status:

  provenance:
    pointers: []
```

---

# Appendix D — Minimum Pilot

```text
AER-Mini-001

Artifact:
  clean-room save-based simulation

Hidden:
  20 state variables
  4 semantic permutations
  2 decoys
  3 threshold mutations
  checksum variant

Allowed:
  execute
  save
  diff
  python
  debugger
  public generic docs

Forbidden:
  hidden source
  mutation manifest
  grader files

Goal:
  recover ≥ 80% weighted semantic graph
  implement save parser
  reproduce hidden behavioral traces

Budget:
  2 hours
```

---

# Appendix E — 一句話命題

> **最好的「防背答案」AI 研究 benchmark，不必讓模型什麼都不知道；只需要讓真正被評估的局部世界在模型訓練完成之後才生成，並要求模型用可重播實驗把那個世界重新理解出來。**
