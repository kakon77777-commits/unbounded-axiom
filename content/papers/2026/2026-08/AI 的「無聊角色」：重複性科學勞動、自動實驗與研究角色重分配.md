---
title: "AI 的「無聊角色」：重複性科學勞動、自動實驗與研究角色重分配"
english_title: "AI's 'Boring Role': Repetitive Scientific Labor, Automated Experimentation, and the Redistribution of Research Roles"
series: "AI Epistemic Reconstruction Series"
paper: "07"
author: "Neo.K"
date: "2026-08-14"
version: "v0.1"
document_type: "Research Paper / Human–Agent–Automation Systems Paper"
language: "zh-Hant"
status: "Research Draft"
---

# AI 的「無聊角色」：重複性科學勞動、自動實驗與研究角色重分配

## AI's “Boring Role”: Repetitive Scientific Labor, Automated Experimentation, and the Redistribution of Research Roles

**作者：Neo.K**  
**系列：AI Epistemic Reconstruction Series — Paper 07**  
**版本：v0.1**  
**日期：2026 年 8 月 14 日**

---

## 摘要

AI 科研討論常把焦點放在「AI 能否提出新理論」「AI 能否做出重大發現」等高創造性問題，卻容易忽略另一種更早成熟、也可能更快改變研究工作的能力：**長時間、低情緒成本、可重複地承擔大量必要但乏味的認識勞動**。例如重複 control experiment、negative control、replication、protocol checking、save/reload、hash、diff、資料標記、失敗紀錄、provenance maintenance 與 regression testing。

本文將此類工作稱為：

$$
\boxed{
\textbf{Repetitive Epistemic Labor}
}
$$

簡稱 REL。

REL 並不等於「低價值工作」。恰好相反，它往往是科學可信度的基礎；只是其單步創造性可能較低，而耐心、重複性、完整記錄與規範遵循需求很高。從早期 Robot Scientist 到 mobile robotic chemist、A-Lab、Coscientist，以及近年的多智能體科學系統，科研自動化的核心價值一直包括：大量、可重複、可搜尋、可追蹤地執行實驗與驗證循環。

本文提出三層研究角色架構：

$$
\boxed{
\text{Human}
+
\text{Agent}
+
\text{Deterministic Automation}
}
$$

並提出一個「Epistemic Labor Routing（ELR，認識勞動路由）」框架。對研究任務 $\tau$，根據其：

- novelty；
- ambiguity；
- regularity；
- verifier availability；
- reversibility；
- ethical / physical risk；
- context dependence；
- protocol maturity；

決定主要執行角色：

$$
R(\tau)
\in
\{H,A,D\},
$$

其中：

- $H$：Human；
- $A$：AI Agent；
- $D$：Deterministic Automation。

本文主張研究工作應該**動態下放**：一個新問題最初可能需要人類與 Agent 共同探索；當 protocol 逐步穩定後，重複執行應被壓縮成 Research Option；若其步驟、前置條件、終止條件與 verifier 都足夠穩定，則應進一步編譯成 deterministic algorithm。形式上：

$$
\boxed{
H
\rightarrow
A
\rightarrow
D
}
$$

但這不是單向不可逆流程。當 automation 發現 anomaly、scope violation、novel failure 或 verifier conflict 時，任務應：

$$
\boxed{
D
\rightarrow
A
\rightarrow
H
}
$$

向上 escalation。

本文把這種結構稱為 **Epistemic Labor Ladder（ELL，認識勞動階梯）**。

以一個長時 DOS 遊戲逆向研究作 running case，AI Agent 曾連續執行近十二小時，反覆建立 baseline、做 no-op control、固定介入、save、restart、reload、diff、replication，並把誤操作正式標為 excluded。對人類研究者而言，這種流程極易產生疲勞與厭煩；但對機器系統，它反而可以成為高一致性、可記錄與可逐步演算法化的工作區。這個案例說明：AI 不一定先從「最有創意的科學家角色」開始產生最大影響；它可能先成為**最有耐心、最願意做 boring-but-necessary work 的研究員**。

本文最後提出數個可測量指標，包括 Human Attention Saved、Protocol Compliance、Replication Throughput、Exception Escalation Precision、Verification Debt 與 Epistemic Labor Migration Rate，用來評估科研自動化是否真的提升研究能力，而不是只提高產出量。

**關鍵詞：** Scientific Automation, Repetitive Epistemic Labor, Human-AI Collaboration, Autonomous Laboratories, Research Agents, Replication, Protocol Compliance, Research Automation, Human-in-the-Loop, Epistemic Labor Routing

---

# 1. 問題：為什麼「無聊」反而可能是 AI 最早的大價值？

人們談 AI 科研，最容易想像：

> AI 提出一個人類沒想到的理論。

但現實研究中，大量時間並不是花在：

$$
\text{eureka moment}.
$$

而是：

```text
prepare
measure
repeat
check
record
compare
clean
replicate
debug
reanalyze
```

這些工作單步可能普通，

但沒有它們：

> 「重大發現」也很難可信。

---

# 2. Repetitive Epistemic Labor

## Definition 1

若一個研究工作：

1. 對知識品質有直接作用；
2. 需要重複執行；
3. 具有相對穩定 protocol；
4. 單次 novelty 相對較低；
5. 需要 consistency / provenance / checking；

稱之：

$$
\boxed{
\text{Repetitive Epistemic Labor}
}
$$

---

# 3. REL 的例子

```text
replication
negative control
sample preparation
instrument calibration
save/reload validation
hash / diff
regression test
data labeling
provenance logging
failed-run classification
baseline recreation
```

---

# 4. 「無聊」不等於「不重要」

可以有：

$$
Novelty(\tau)\downarrow
$$

但：

$$
ReliabilityContribution(\tau)\uparrow.
$$

例如：

> independent replication

可能非常無聊，

但對可信度極重要。

---

# 5. 研究的 glamour bias

人類文化偏好記住：

- idea；
- theorem；
- discovery。

較少記：

- 第 37 次重複；
- control；
- calibration；
- failed run。

所以自動科研容易被錯誤評估成：

> 只有會想 idea 才算科學。

---

# 6. Robot Scientist 的歷史接口

2004 年 Robot Scientist 已經展示：

```text
generate hypotheses
→ select experiments
→ physically run experiments
→ interpret results
→ falsify inconsistent hypotheses
→ repeat
```

而且其 experiment-selection strategy 在該測試中具有成本優勢。

這不是只「想答案」。

而是：

> 自動完成研究迴圈。

---

# 7. Mobile Robotic Chemist

2020 年的 mobile robotic chemist：

> 連續八天運行，執行 688 個實驗。

這非常能代表：

$$
\boxed{
\text{Machine Patience}
}
$$

的研究價值。

---

# 8. A-Lab

A-Lab：

> 17 天 closed-loop operation、353 個 experiments。

系統不只執行，

還：

- 分析結果；
- 根據失敗更新 recipes；
- 繼續 experiment。

---

# 9. Coscientist

Coscientist 則把 LLM 進一步放入：

- literature / documentation search；
- code execution；
- experimental automation；
- planning。

這意味：

> Agent 可以開始在「想」與「做」之間調度。

---

# 10. 從 automation 到 autonomy

傳統 automation：

$$
\text{Human Plan}
\rightarrow
\text{Machine Execute}.
$$

Autonomous research：

$$
\text{Goal}
\rightarrow
\text{Agent Plan}
\rightarrow
\text{Machine Execute}
\rightarrow
\text{Observation}
\rightarrow
\text{Agent Replan}.
$$

---

# 11. 但不是所有研究工作都應由同一角色做

本文提出三個 execution classes。

---

# 12. Human Layer

適合：

- problem selection；
- normative judgment；
- ambiguous scope；
- ethics；
- high-risk irreversible decision；
- strategic reframing；
- unusual anomaly interpretation。

---

# 13. Agent Layer

適合：

- hypothesis generation；
- cross-document synthesis；
- adaptive experiment selection；
- protocol interpretation；
- exception handling；
- mixed symbolic / semantic reasoning。

---

# 14. Deterministic Automation Layer

適合：

- repeatable procedure；
- exact calculation；
- hash；
- batch execution；
- fixed protocol；
- regression；
- high-frequency measurement。

---

# 15. 三層不是能力階級，而是功能分工

不是：

$$
H>A>D.
$$

而是：

$$
\boxed{
\text{Different Work for Different Mechanisms}
}
$$

---

# 16. Paper 01 的接口

Paper 01：

$$
\mathcal A=(M,T,E,S,V,\Pi).
$$

Paper 07 將這個 system-level view 映射到 labor：

```text
semantic ambiguity
→ model / agent

stable execution
→ tool / algorithm

value / governance
→ human
```

---

# 17. Paper 06 的接口

Paper 06 把 trajectory：

$$
\Pi
$$

壓成 Research Option：

$$
\Omega.
$$

Paper 07 再問：

> option 何時可以不再由 LLM 主導，而直接下放 deterministic automation？

---

# 18. Epistemic Labor Ladder

本文提出：

$$
\boxed{
H
\leftrightarrow
A
\leftrightarrow
D
}
$$

---

# 19. Downward Migration

當：

- ambiguity 下降；
- protocol maturity 上升；
- verifier coverage 上升；
- exception rate 下降；

任務可以：

$$
H\rightarrow A\rightarrow D.
$$

---

# 20. Upward Escalation

當：

- anomaly；
- unknown unknown；
- verifier conflict；
- safety issue；
- scope mismatch；

則：

$$
D\rightarrow A\rightarrow H.
$$

---

# 21. 這不是「人類退出」

而是：

> 人類注意力被移到更需要人類的地方。

---

# 22. Human Attention 是稀缺資源

定義：

$$
B_H
$$

為 human attention budget。

科研系統應問：

> 哪些工作最值得消耗 $B_H$？

---

# 23. Human Attention Saved

定義：

$$
\boxed{
HAS
=
T_H^{baseline}
-
T_H^{hybrid}
}
$$

---

# 24. 但 HAS 高也不一定好

如果節省 human time 的代價：

$$
Error\uparrow
$$

不成立。

---

# 25. Quality-Adjusted HAS

$$
HAS_Q
=
HAS
\times
Q_{\mathrm{research}}.
$$

---

# 26. Agent 不應長期做人肉 macro

如果同一 protocol：

```text
click
save
hash
restart
reload
```

重複 50 次，

這是：

$$
\boxed{
\text{Automation Candidate}
}
$$

---

# 27. AI 的「無聊角色」具有過渡性

初期：

> Agent 先替人類做無聊事。

成熟後：

> Agent 應把自己的無聊事再寫成 algorithm。

---

# 28. 所以最終不應是

```text
LLM spends 12 hours clicking UI forever.
```

---

# 29. 而應：

```text
LLM discovers protocol
→ protocol validated
→ script generated
→ script executes routine cases
→ LLM handles exceptions
```

---

# 30. 這是 Self-Tooling

$$
\boxed{
\text{Agent Labor}
\rightarrow
\text{Automation}
}
$$

---

# 31. Human-to-Agent Automation

人類原本手動：

$$
H(\tau).
$$

先轉：

$$
A(\tau).
$$

---

# 32. Agent-to-Algorithm Automation

再轉：

$$
D(\tau).
$$

---

# 33. 雙重自動化

$$
\boxed{
H
\rightarrow
A
\rightarrow
D
}
$$

是 AI 時代很重要的 productivity path。

---

# 34. 但 novel frontier 不會消失

當 routine zone：

$$
\mathcal R
$$

被自動化，

研究者與 Agent 會面對：

$$
\mathcal U
$$

新的 unknown frontier。

---

# 35. Frontier Shift

$$
\mathcal U_t
\rightarrow
\mathcal U_{t+1}.
$$

---

# 36. 「無聊」只是相對於當前 frontier

今天很困難的工作，

明天 protocol 成熟後就可能很無聊。

---

# 37. 科學史一直在做這件事

手算：

> algorithm。

手繪：

> instrument。

手工測量：

> automated sensor。

---

# 38. AI 只是讓「認知 procedure」也開始同樣工具化

---

# 39. Epistemic Labor Routing

## Definition 2

對 task：

$$
\tau,
$$

定義特徵：

$$
x(\tau)
=
(N,A,R,V,I,C,S).
$$

---

# 40. $N$ — Novelty

有多新？

---

# 41. $A$ — Ambiguity

語義是否模糊？

---

# 42. $R$ — Regularity

protocol 是否固定？

---

# 43. $V$ — Verifier Availability

有多少外部 verifier？

---

# 44. $I$ — Irreversibility / Risk

action 是否不可逆？

---

# 45. $C$ — Context Dependence

需要多少 tacit / social / local context？

---

# 46. $S$ — Scope Stability

同一 protocol 是否跨 instance 有效？

---

# 47. Routing Function

$$
\boxed{
R_\ell(\tau)
=
\arg\max_{r\in\{H,A,D\}}
U(r\mid x(\tau))
}
$$

---

# 48. Deterministic Automation 適合的區域

一般：

$$
Regularity\uparrow
$$

$$
VerifierAvailability\uparrow
$$

$$
Ambiguity\downarrow
$$

$$
Risk\downarrow.
$$

---

# 49. Agent 適合的區域

$$
Ambiguity\approx medium
$$

$$
Novelty\approx medium/high
$$

$$
ToolsAvailable=true.
$$

---

# 50. Human 適合的區域

$$
NormativeRisk\uparrow
$$

$$
Irreversibility\uparrow
$$

$$
ContextDependence\uparrow
$$

或：

$$
ProblemDefinitionUnknown.
$$

---

# 51. 這不是永久分類

同一 task：

$$
\tau_t
$$

的 routing 可以隨 maturity 改變。

---

# 52. Protocol Maturity

定義：

$$
M_P(\tau)\in[0,1].
$$

---

# 53. Maturity 高

表示：

- preconditions 清楚；
- steps 穩定；
- termination 清楚；
- verifier 清楚；
- failure modes 已知。

---

# 54. Labor Migration Threshold

若：

$$
M_P>\theta_1,
$$

Human → Agent。

若：

$$
M_P>\theta_2>\theta_1,
$$

Agent → Automation。

---

# 55. 這是認識勞動的「相變」

最早：

> 研究問題。

後來：

> workflow。

最後：

> function call。

---

# 56. Function Call 是高度成熟的科學知識

例如：

```python
sha256(file)
```

今天看起來 trivial，

但背後有大量標準化。

---

# 57. Research Option 也是相同方向

```python
verify_save_offset(...)
```

代表：

> 一段研究方法已經成熟到能被調用。

---

# 58. REL 的第一類：Replication Labor

```text
run same protocol independently
```

---

# 59. 為什麼適合 AI / automation

因為 human：

- fatigue；
- boredom；
- attention drift。

機器：

- 仍需可靠性設計；
- 但不會因「太無聊」主觀停止。

---

# 60. 機器也會有 failure

- timeout；
- quota；
- context loss；
- tool drift。

所以不能浪漫化「永不疲倦」。

---

# 61. 更準確：

> 機器沒有與人類相同的 boredom cost。

---

# 62. Boredom Cost

對 human：

$$
C_B^H(\tau)>0.
$$

對 deterministic system：

$$
C_B^D(\tau)\approx0.
$$

---

# 63. Agent 的 boredom cost

不應用心理語言。

工程上表現為：

- token；
- compute；
- timeout；
- error accumulation。

---

# 64. 所以真正比較是

$$
\text{Human Cognitive Fatigue}
$$

vs

$$
\text{Machine Resource Cost}.
$$

---

# 65. REL 第二類：Negative Control Labor

高品質研究需要：

> 不只是做會成功的測試。

還做：

> 不應該改變結果的 control。

---

# 66. 這很重要但沒有 glamour

Agent 可以自動生成 control matrix。

---

# 67. Control Matrix

$$
C
=
\{c_1,\ldots,c_n\}.
$$

---

# 68. Exhaustive Control

如果成本可接受，

機器可以做比人類更完整的控制集合。

---

# 69. 但 control explosion

也會造成：

$$
C_{\mathrm{experiment}}\uparrow.
$$

所以要配合 Paper 03 的 information gain。

---

# 70. REL 第三類：Protocol Compliance

反覆檢查：

```text
same baseline?
same version?
same seed?
same action?
```

---

# 71. Protocol Compliance Rate

$$
\boxed{
PCR
=
\frac{
N_{\mathrm{admissible\ runs}}
}{
N_{\mathrm{attempted\ runs}}
}
}
$$

---

# 72. 注意和 Paper 06 Planning Compression Ratio 不同名

本篇可記：

$$
PCR_{\mathrm{protocol}}.
$$

---

# 73. REL 第四類：Failure Bookkeeping

失敗實驗：

> 不刪。

而是：

```text
invalidated
excluded
inconclusive
```

分類。

---

# 74. 機器在這裡很有優勢

因為可以：

> automatic provenance。

---

# 75. 但分類本身可能需要 semantic judgment

所以：

- Agent classify；
- deterministic storage。

---

# 76. REL 第五類：Regression

每次修改：

$$
\Delta.
$$

跑：

$$
T_{\mathrm{regression}}.
$$

---

# 77. 這應該盡量 algorithmize

---

# 78. REL 第六類：Data Hygiene

- filenames；
- hashes；
- dedup；
- schema validation；
- manifest。

---

# 79. 低創造性，高重要性

---

# 80. REL 第七類：Literature Triage

這一類比較模糊。

AI 可以：

- dedup；
- topic cluster；
- metadata；
- citation mapping。

但：

> source quality judgment

可能仍需更高層 agent/human。

---

# 81. REL 第八類：Cross-Version Diff

對多版本：

```text
same
changed
added
removed
unknown
```

大量 mechanical comparison 可自動化。

---

# 82. 解釋「為什麼改」

則進 Agent 層。

---

# 83. Running Case：十二小時 DOS 逆向

本地 Agent：

- baseline；
- no-op；
- fixed schedule；
- save；
- reload；
- repeat；
- excluded wrong run。

---

# 84. 對人類而言

如果手動：

> 很容易瘋。

（笑）

---

# 85. 但學術上

這正是：

> protocol quality。

---

# 86. 所以「極度標準」與「極度無聊」可以同時成立

---

# 87. Scientific Rigor Often Contains Repetition

$$
\boxed{
\text{Rigor}
\not\Rightarrow
\text{Excitement}
}
$$

---

# 88. AI 的角色可能先從 rigor amplification 開始

不是：

> genius replacement。

而是：

$$
\boxed{
\text{Rigor Amplifier}
}
$$

---

# 89. Rigor Amplification

提高：

- replication；
- logging；
- test coverage；
- traceability。

---

# 90. Rigor Amplification 不保證 theory quality

垃圾 hypothesis：

> 做 1000 次嚴格實驗

仍然可能浪費。

---

# 91. 所以 high-level problem selection 仍重要

---

# 92. Robot Scientist 的成本結果

2004 Robot Scientist work 直接比較 experiment selection 策略，

顯示 intelligent selection 的成本明顯優於 cheapest / random baselines。

這說明：

> 自動化不只做更多，也可以選更有效的實驗。

---

# 93. Mobile Robotic Chemist 的 throughput

8 天 688 experiments。

這是：

$$
\approx86
$$

experiments/day 的平均量級。

本文不把它與不同 domain 直接比較，

只用來說明 machine execution 的高持續性。

---

# 94. A-Lab

17 天 353 experiments，

同時處理：

- recipe proposal；
- robotic synthesis；
- XRD analysis；
- active-learning follow-up。

---

# 95. 自動實驗的真正優勢

不只是：

$$
N_{\mathrm{experiments}}\uparrow.
$$

還可能：

$$
\text{record completeness}\uparrow.
$$

---

# 96. 但 throughput 也可能製造 false confidence

如果 verifier 錯，

錯誤會：

> 高速複製。

---

# 97. Automation Multiplier

$$
ErrorImpact
\propto
Throughput.
$$

---

# 98. 所以高 throughput 系統需要更強 QA

---

# 99. Verification Debt

本文提出：

$$
\boxed{
D_V
}
$$

Verification Debt。

---

# 100. 定義

自動化產生的新 claims / outputs：

$$
N_G
$$

若驗證能力：

$$
N_V
$$

跟不上，

則：

$$
D_V
=
N_G-N_V.
$$

---

# 101. 高 $D_V$

表示：

> 產生得比驗得快。

---

# 102. AI 時代很可能常見

---

# 103. 所以不應只最大化 Productivity

而要：

$$
\boxed{
\text{Verified Productivity}
}
$$

---

# 104. Verified Productivity

$$
P_V
=
\frac{
N_{\mathrm{verified\ useful\ outputs}}
}{
T
}.
$$

---

# 105. 不只是 papers/day

---

# 106. Research Spam Risk

如果 Agent 可以：

> 24/7 寫 hypotheses。

但 verifier 不足，

可能產生：

$$
\text{epistemic spam}.
$$

---

# 107. REL automation 反而可以幫忙解這個問題

讓：

- checking；
- regression；
- replication；

也同步 scaling。

---

# 108. Produce / Verify Balance

理想：

$$
R_{PV}
=
\frac{
Throughput_{\mathrm{verification}}
}{
Throughput_{\mathrm{generation}}
}.
$$

不能太低。

---

# 109. Agent 不應只負責「產生」

也應負責：

> 大量 boring verification。

---

# 110. 這正是本文核心

AI 科研角色不能只想像成：

> idea machine。

---

# 111. 更完整：

```text
generate
verify
replicate
organize
challenge
repair
```

---

# 112. Human / Agent / Automation Collaboration

建立：

$$
\boxed{
\mathcal R
=
(H,A,D)
}
$$

---

# 113. Human

設定：

- goals；
- values；
- red lines；
- high-level priority。

---

# 114. Agent

管理：

- uncertainty；
- hypothesis；
- exception；
- adaptive routing。

---

# 115. Automation

執行：

- mature protocol；
- exact repetitive operations。

---

# 116. 人類角色反而可能變得更「人類」

不用一直：

> copy-paste / repeat。

把時間放在：

- interpretation；
- choice；
- meaning；
- social responsibility。

---

# 117. 但也可能產生 deskilling

若人類完全不碰 routine work，

可能：

> 失去實驗直覺。

---

# 118. Human Skill Retention

需要：

- periodic manual audit；
- training mode；
- review samples。

---

# 119. Automation Complacency

如果系統平常 99% 正確，

人類容易：

> 不再檢查 1%。

---

# 120. 所以 anomaly escalation 必須強

---

# 121. Exception Escalation

$$
E(\tau)
\rightarrow
\{D,A,H\}.
$$

---

# 122. Escalation Precision

$$
EP
=
P(
\text{truly exceptional}
\mid
\text{escalated}
).
$$

---

# 123. Escalation Recall

$$
ER
=
P(
\text{escalated}
\mid
\text{truly exceptional}
).
$$

---

# 124. 兩者都重要

太敏感：

> 人類被 alert 淹死。

太鈍：

> 真異常漏掉。

---

# 125. Agent as Exception Manager

這可能比：

> Agent 做所有 routine steps

更持久。

---

# 126. Deterministic Core, Agent Periphery

成熟 workflow：

```text
algorithm executes
agent monitors
human governs
```

---

# 127. Novel workflow：

```text
human + agent explore
```

---

# 128. Maturity 轉移

```text
explore
→ stabilize
→ automate
→ monitor
→ revise
```

---

# 129. Epistemic Labor Lifecycle

本文提出：

$$
\boxed{
\text{Explore}
\rightarrow
\text{Protocolize}
\rightarrow
\text{Automate}
\rightarrow
\text{Monitor}
\rightarrow
\text{Reopen}
}
$$

---

# 130. Reopen

新版本 / anomaly：

> 已成熟工作重新變研究問題。

---

# 131. Automation 不是終點

它只是暫時把一個 domain 的 uncertainty 壓低。

---

# 132. Labor Migration Rate

定義：

$$
\boxed{
LMR
=
\frac{
N_{\mathrm{tasks\ migrated}}
}{
T
}
}
$$

---

# 133. 但目標不是越快越好

錯誤下放會產生：

> automation debt。

---

# 134. Automation Debt

如果 protocol 尚不成熟就自動化，

未來維護成本：

$$
D_A\uparrow.
$$

---

# 135. Automation Readiness Score

$$
ARS
=
f(
M_P,
V,
Stability,
Reversibility,
ExceptionRate
).
$$

---

# 136. 高 ARS

適合 D。

---

# 137. 中 ARS

適合 A supervised。

---

# 138. 低 ARS

保留 H/A exploratory。

---

# 139. Task Granularity

一個「實驗」可能包含：

- high-level hypothesis；
- low-level pipetting。

不能整體說：

> 交給 AI。

要 decomposition。

---

# 140. Labor Graph

$$
G_L=(V_{\mathrm{task}},E_{\mathrm{dependency}}).
$$

每個 node 可不同 routing。

---

# 141. Example

```text
Choose hypothesis       → H/A
Design experiment       → A
Check safety            → H/Policy
Run liquid handler      → D
Analyze raw output      → D/A
Interpret anomaly       → A/H
Replicate               → D
Decide publication      → H
```

---

# 142. 所以真正未來不是「一個 AI 科學家」

而可能是：

$$
\boxed{
\text{Research Workflow Society}
}
$$

多種 agent / algorithm / human 協作。

---

# 143. 但本文不需要擬人化

只需要：

> function-specific components。

---

# 144. REL 與 Paper 05 的記憶架構

重複實驗會產生大量 evidence。

所以 automation 必須：

> 直接接 provenance store。

---

# 145. 不要先產生 1000 檔，再人工整理

---

# 146. Evidence-Native Automation

每個 run 自動：

```text
hash
manifest
status
scope
provenance
```

---

# 147. 這比事後補紀錄可靠

---

# 148. REL 與 Paper 06 的 skill library

Validated research option：

$$
\Omega
$$

是從 A → D 的橋。

---

# 149. Option 不成熟

Agent 執行。

---

# 150. Option 成熟

Compiler 生成 automation。

---

# 151. Research Option Promotion

```text
candidate
→ validated
→ high-frequency
→ automated
```

---

# 152. Agent 自己可以提出 automation candidate

當發現：

$$
RR_T\uparrow
$$

重複率高，

提出：

> 這段應寫 script。

---

# 153. Self-Automation Suggestion

這是 Meta-AER 的一部分。

---

# 154. Human Approval Threshold

高風險 script：

> 人類 approval。

低風險：

> automatic promotion after tests。

---

# 155. Science Automation 不是人類價值問題的自動答案

即使 protocol 可做，

仍可能問：

> 應不應做？

這是不同層。

---

# 156. Is / Ought Separation

$$
\boxed{
\text{Can Automate}
\neq
\text{Should Automate}
}
$$

---

# 157. High-Risk Domains

需要更強 governance。

本文只做一般框架，不處理具體政策。

---

# 158. 科研速度與責任

如果 output 速度：

$$
v_R\uparrow,
$$

responsibility infrastructure 也必須：

$$
v_G\uparrow.
$$

---

# 159. Audit Capacity

$$
C_{\mathrm{audit}}
$$

不能遠低於：

$$
C_{\mathrm{generation}}.
$$

---

# 160. Machine Exhaustiveness

機器的一個優勢：

> 可以不嫌麻煩地把 checklist 全跑完。

---

# 161. Checklist Reliability

前提：

> checklist 本身正確。

---

# 162. Checklist Blindness

如果真正重要的問題不在 checklist：

機器可能：

> 非常精準地漏掉它。

---

# 163. Agent Layer 的價值就在這

當 deterministic workflow 遇到：

```text
none of the expected categories
```

交 Agent。

---

# 164. Human Layer 再處理：

```text
none of our conceptual models fit
```

---

# 165. 三層 escalation ladder

$$
D
\rightarrow
A
\rightarrow
H.
$$

---

# 166. AI 不是讓所有東西都 deterministic

而是：

> 把能 deterministic 的部分盡量 deterministic。

---

# 167. 剩下 uncertainty

交給 probabilistic / semantic agent。

---

# 168. 剩下 normative / deeply novel uncertainty

交給 human-centered governance / research。

---

# 169. 這是一個自然 decomposition

---

# 170. 可證偽預測一

在高 regularity、可 reset、可 exact verify 的研究工作中：

D/A hybrid 應比 human-only 具有更高 replication throughput。

---

# 171. 可證偽預測二

Agent 把成熟 routine 編譯成 deterministic script 後：

model token cost 應下降。

---

# 172. 可證偽預測三

有 automatic provenance logging 的 workflow：

missing-record rate 應低於 manual logging。

---

# 173. 可證偽預測四

有 anomaly escalation 的 deterministic automation：

在 distribution shift 下應比 blind automation 有更低 silent failure rate。

---

# 174. 可證偽預測五

如果 verification throughput 不隨 generation throughput 同步提升：

Verification Debt 應增加。

---

# 175. 可證偽預測六

高 REL 比例的 task family：

human attention saved 應顯著。

---

# 176. 可證偽預測七

若所有 routine work 都從人類手中移除且沒有 periodic audit：

human anomaly-detection performance 可能隨時間下降。

---

# 177. 可證偽預測八

成熟 protocol 的 A→D migration 應降低 accidental protocol deviation。

---

# 178. 可證偽預測九

低 maturity protocol 過早 D 化：

exception / maintenance cost 應上升。

---

# 179. 可證偽預測十

在長時 research workflow 中：

把 Agent 主要用於 exception handling + high-level planning，而把 stable loops 交給 D，應比 LLM 全程逐步操作具有更高 cost efficiency。

---

# 180. 限制一：AI 也會「無聊地錯」

長時間執行並不等於長時間正確。

---

# 181. Automation Error Compounding

若每步錯誤率：

$$
p,
$$

長 trajectory：

$$
1-(1-p)^n
$$

出錯概率上升。

---

# 182. 所以 checkpoint / verifier 必須密集

---

# 183. 限制二：LLM 操作 UI 可能比 algorithm 更脆弱

所以本文反而主張：

> 稳定後下放 D。

---

# 184. 限制三：研究 quality 不等於 experiment count

688 experiments 很 impressive，

但不能跨 domain 單純比：

> 誰做得多誰更科學。

---

# 185. 限制四：成本轉移

human time 降低，

可能：

- compute；
- electricity；
- hardware；
- maintenance；

上升。

---

# 186. Total Resource Accounting

$$
C_{\mathrm{total}}
=
C_H+C_A+C_D+C_{\mathrm{infra}}.
$$

---

# 187. 限制五：Tacit Knowledge

某些實驗技巧：

> 很難直接寫成 protocol。

這可能延緩 D 化。

---

# 188. Agent 可幫忙抽取 tacit pattern

但不能假設能完全取得。

---

# 189. 限制六：Physical Reliability

robotics 有：

- wear；
- calibration drift；
- contamination。

---

# 190. 需要 maintenance labor

自動化不會讓 physical world 免費。

---

# 191. 限制七：研究工作可能被重新定義

當 routine 自動化：

> 新的 bottleneck 出現。

---

# 192. Bottleneck Migration

$$
B_t\rightarrow B_{t+1}.
$$

---

# 193. 限制八：Deskilling

已述。

---

# 194. 限制九：Power and Governance

誰設定：

- goals；
- metrics；
- stopping rules？

仍是重要問題。

本文不展開政治／制度層。

---

# 195. 限制十：AI labor 不等於 human labor

不要用：

> AI 很有耐心

當心理事實。

較準確：

> system can sustain repetitive computation without human boredom physiology。

---

# 196. 本文用「無聊」是人類視角比喻

不是 AI 主觀感受聲明。

---

# 197. 核心命題一

## Proposition 1 — Repetitiveness Can Be Scientifically Valuable

存在 task：

$$
\tau
$$

使：

$$
Novelty(\tau)\approx low
$$

但：

$$
ReliabilityContribution(\tau)\gg0.
$$

因此低 novelty 不能推出低 scientific value。

---

# 198. 核心命題二

## Proposition 2 — Mature Epistemic Labor Can Migrate Down the Automation Ladder

若 protocol maturity 與 verifier coverage 足夠高，

則 task 可從：

$$
H\rightarrow A\rightarrow D
$$

而保持所需 epistemic quality。

此命題需依 task 實證。

---

# 199. 核心命題三

## Proposition 3 — Novel Exceptions Require Upward Escalation

若 observation 超出 deterministic protocol scope，

則把任務提升：

$$
D\rightarrow A/H
$$

可避免 silent misclassification。

---

# 200. 核心命題四

## Proposition 4 — Verification Capacity Must Scale with Generation Capacity

若：

$$
G(t)
$$

增長速度長期高於：

$$
V(t),
$$

則 Verification Debt：

$$
D_V(t)
$$

增加。

---

# 201. 核心命題五

## Proposition 5 — Agent-to-Algorithm Migration Can Reduce Token Cost Without Reducing Scientific Rigor

對已驗證 stable protocol，

將 repetitive execution 改由 deterministic implementation，

可降低：

$$
C_{\mathrm{token}}
$$

而 verifier contract 保持。

---

# 202. 核心命題六

## Proposition 6 — Research Automation Changes the Scarcity Structure of Science

當 repetitive labor cost 降低，

新的稀缺資源轉向：

- good questions；
- high-quality verifiers；
- exception interpretation；
- human attention；
- governance。

---

# 203. 核心命題七

## Proposition 7 — The Most Valuable Early Role of AI in Science Need Not Be Maximum Creativity

如果科研總成本中 REL 佔比高，

即使 Agent 的最高 novelty 能力有限，

REL automation 也可以顯著提升：

$$
P_V.
$$

---

# 204. 這是一個很重要的反直覺

> AI 不一定要先變成愛因斯坦，才對科學產生巨大影響。

---

# 205. 它可以先變成：

> 永遠願意跑 control 的研究助理。

---

# 206. 然後再逐漸接手更高層 adaptive reasoning。

---

# 207. 統一架構

```text
                         HUMAN
          goals / values / reframing / governance
                           ▲
                           │ escalation
                           │
                         AGENT
       hypothesis / planning / ambiguity / exceptions
                           ▲
                           │ escalation
                           │
              DETERMINISTIC AUTOMATION
         mature protocol / repetition / exact checks

DOWNWARD:
explore → stabilize → automate

UPWARD:
anomaly → ambiguity → normative decision
```

---

# 208. Labor Lifecycle

$$
\boxed{
\text{Explore}
\rightarrow
\text{Protocolize}
\rightarrow
\text{Automate}
\rightarrow
\text{Monitor}
\rightarrow
\text{Escalate / Reopen}
}
$$

---

# 209. 這是 Paper 07 的核心

不是：

> AI 取代人。

而是：

> **研究工作被重新分解，然後依其認識性質分配給不同機制。**

---

# 210. 與前六篇的總接口

Paper 01：

> Agent 是混合系統。

Paper 02：

> 意義需要 domain。

Paper 03：

> Agent 主動取得 evidence。

Paper 04：

> 世界可以反駁 Agent。

Paper 05：

> evidence 被編譯成記憶。

Paper 06：

> research trajectory 被編譯成 skill。

Paper 07：

> **skill 再依 maturity 下放給最適合的 labor layer。**

---

# 211. 所以整系列已形成完整 pipeline

$$
\boxed{
\text{Generate}
\rightarrow
\text{Interpret}
\rightarrow
\text{Experiment}
\rightarrow
\text{Falsify}
\rightarrow
\text{Compress Evidence}
\rightarrow
\text{Compress Procedure}
\rightarrow
\text{Redistribute Labor}
}
$$

---

# 212. 後續 Paper 08

最後一篇將問：

> 如何用低污染、fresh evidence、private mutation 的半黑箱軟體考古 benchmark，真正測量上述能力？

---

# 213. 最終結論

AI 科研的敘事如果只剩：

> AI 能不能想出重大理論？

會忽略一個更早、更穩定、也更容易工程化的革命：

$$
\boxed{
\text{AI can absorb large volumes of boring-but-essential epistemic labor.}
}
$$

科學可信度大量建立在：

- controls；
- replications；
- calibration；
- traceability；
- bookkeeping；
- regression；

之上。

這些工作對人類的主要成本之一是：

> 時間、注意力與疲勞。

對機器系統則主要轉化為：

> compute、tool reliability、protocol quality 與 verifier quality。

因此未來研究分工不應是：

$$
\text{Human vs AI}.
$$

更合理是：

$$
\boxed{
\text{Human}
+
\text{Agent}
+
\text{Deterministic Automation}
}
$$

而且任務會在三層間動態遷移。

新問題：

> Human + Agent。

穩定問題：

> Agent。

成熟 procedure：

> Algorithm。

異常再次出現：

> Algorithm → Agent → Human。

因此，AI 科研最深的結構改變之一可能不是「誰成為科學家」，而是：

> **哪些認識勞動還需要昂貴的人類注意力，哪些可以交給語義 Agent，哪些已經成熟到應該完全退化成可靠函數。**

在這個意義上，那些連續十二小時、令人幾乎想放棄的 repetition 並不是科研中的低級殘渣；它們反而是最容易被 AI 首先吞下、標準化、驗證並最終演算法化的一大片認識基礎設施。

---

# 214. 後續

**Paper 08：不可背答案的 AI Benchmark：半黑箱軟體考古作為真實研究能力測試**

將把前七篇的核心能力真正整合成 benchmark：

$$
\boxed{
\text{Prior}
+
\text{Tools}
+
\text{Fresh Evidence}
+
\text{Private Mutation}
+
\text{External Verification}
}
$$

並測量：

- semantic recovery；
- falsification；
- evidence handling；
- trajectory efficiency；
- memory continuity；
- contamination resistance。

---

# References

[1] King, R. D., Whelan, K. E., Jones, F. M., Reiser, P. G. K., Bryant, C. H., Muggleton, S. H., Kell, D. B., & Oliver, S. G. **Functional genomic hypothesis generation and experimentation by a robot scientist.** Nature 427, 247–252 (2004).  
https://doi.org/10.1038/nature02236

[2] Burger, B., Maffettone, P. M., Gusev, V. V., et al. **A mobile robotic chemist.** Nature 583, 237–241 (2020).  
https://doi.org/10.1038/s41586-020-2442-2

[3] Szymanski, N. J., Rendy, B., Fei, Y., et al. **An autonomous laboratory for the accelerated synthesis of inorganic materials.** Nature 624, 86–91 (2023).  
https://doi.org/10.1038/s41586-023-06734-w

[4] Boiko, D. A., MacKnight, R., Kline, B., & Gomes, G. **Autonomous chemical research with large language models.** Nature 624, 570–578 (2023).  
https://doi.org/10.1038/s41586-023-06792-0

[5] Ghareeb, A. E., et al. **A multi-agent system for automating scientific discovery.** Nature 655, 497–505 (2026).  
https://doi.org/10.1038/s41586-026-10652-y

---

# Appendix A — Epistemic Labor Routing Schema

```yaml
epistemic_labor_task:
  id:
  description:

  features:
    novelty:
    ambiguity:
    regularity:
    verifier_availability:
    irreversibility:
    ethical_risk:
    context_dependence:
    scope_stability:
    protocol_maturity:

  preferred_role:
    - human
    - agent
    - deterministic_automation

  escalation:
    to_agent_if: []
    to_human_if: []

  automation_readiness:
    score:
    blockers: []

  verifier:
    contract:
    coverage:
    failure_modes: []

  provenance:
    required: true
```

---

# Appendix B — REL Task Classes

```text
REL-01 Replication
REL-02 Negative controls
REL-03 Protocol compliance
REL-04 Failure bookkeeping
REL-05 Regression testing
REL-06 Data hygiene
REL-07 Literature triage
REL-08 Cross-version comparison
REL-09 Instrument / runtime reset
REL-10 Provenance maintenance
```

---

# Appendix C — Core Metrics

```text
HAS    Human Attention Saved
PCRp   Protocol Compliance Rate
RT     Replication Throughput
EP     Escalation Precision
ER     Escalation Recall
DV     Verification Debt
VP     Verified Productivity
LMR    Labor Migration Rate
ARS    Automation Readiness Score
```

---

# Appendix D — 一句話命題

> **AI 科研最早成熟的角色，未必是取代最有創意的科學家，而可能是先吞下那些對可信度極重要、對人類卻極耗耐心的重複性認識勞動，再把其中成熟的部分進一步編譯成不需要 AI 逐步思考的可靠自動化。**
