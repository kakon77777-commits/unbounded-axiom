# Series C — C07｜一句話不是魔法：Sparse Intent 與 Project-World Cognition
## One Sentence Is Not Magic: Sparse Intent and Project-World Cognition

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 07 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-06  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Applied Theory / Software Engineering / Project-World Cognition / Sparse-Intent Globality

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文承接 C01–C06，將 Global Observer、difference governance、domain formation、legal bridge、uncertainty domain 與 ELC Loop 首次壓入一個高可觀測、可工程驗證、可長時間追蹤的實務場景：

> **只給 AI 一句極短意圖，然後觀察它是否能自行建立一個真正接近完整的 Project World。**

本文的核心不是吹捧「一句話做 App」，而是拆解一句話背後被 AI 自行補出的全域認知工作。

---

# 摘要

「一句話生成 App」常被當成 AI 能力的戲劇化展示：

> 做一個記帳 App。

> 做一個企業 AI 會計系統。

> 做一個多人線上遊戲。

> 做一個法律檢索平台。

若 AI 幾分鐘後產生：

- UI；
- API；
- database；
- code；

人們很容易說：

> AI 已經把應用做完了。

本文拒絕這種低解析度判定。

真正的問題不是：

$$
\boxed{
\text{Prompt}
\rightarrow
\text{Code}
\rightarrow
\text{Runs}.
}
$$

而是：

$$
\boxed{
\text{Sparse Intent}
\rightarrow
\text{Project World Model}
\rightarrow
\text{Domainization}
\rightarrow
\text{Architecture}
\rightarrow
\text{Implementation}
\rightarrow
\text{Verification}
\rightarrow
\text{Deployment}
\rightarrow
\text{Maintenance Future}.
}
$$

本文把這種能力稱為：

$$
\boxed{
\text{Sparse-Intent Project-World Cognition}
}
$$

簡稱：

$$
\boxed{
\mathsf{SIPWC}.
}
$$

它測量的是：

> **在人類只注入極少 task information 時，AI 能自行補出多少「必要但未明說」的專案世界。**

Sparse Intent 的價值在於：

$$
\boxed{
\text{Human Information Injection}\downarrow
\Rightarrow
\text{AI Structural Contribution}\uparrow
}
$$

因而更容易觀察 AI 自身的 global attention、domain discovery、architecture choice、risk awareness 與 project epistemic self-awareness。

本文首先定義一個 Project World：

$$
\boxed{
\mathcal W_P
=
\left\langle
D_P,
D_{UX},
D_A,
D_D,
D_S,
D_T,
D_O,
D_{Deploy},
D_M,
D_C,
D_R,
H_P
\right\rangle.
}
$$

其中至少包括：

- $D_P$：product domain；
- $D_{UX}$：UX / interaction domain；
- $D_A$：architecture domain；
- $D_D$：data domain；
- $D_S$：security / privacy domain；
- $D_T$：testing / verification domain；
- $D_O$：observability domain；
- $D_{Deploy}$：deployment / operations domain；
- $D_M$：maintenance / evolution domain；
- $D_C$：cost / resource domain；
- $D_R$：risk / failure domain；
- $H_P$：project history / provenance。

所以一個「應用」不是：

$$
UI+API+DB.
$$

而是：

$$
\boxed{
\text{Project}
=
\text{Product Intent}
+
\text{Executable System}
+
\text{Operational Environment}
+
\text{Future Maintenance Space}.
}
$$

本文進一步定義 **Application Quality Vector**：

$$
\boxed{
\mathbf Q_{app}
=
(
F,
C,
A,
R,
S,
T,
M,
P,
U,
O,
E,
X
).
}
$$

其中：

- $F$：functional completeness；
- $C$：correctness；
- $A$：architecture quality；
- $R$：reliability；
- $S$：security / safety；
- $T$：testing / verification；
- $M$：maintainability；
- $P$：performance；
- $U$：usability / UX；
- $O$：observability；
- $E$：extensibility；
- $X$：evolution cost / future adaptability。

因此：

$$
\boxed{
Performance
\subset
ApplicationQuality.
}
$$

而不是：

$$
Performance
=
ApplicationQuality.
$$

本文再建立 application maturity ladder：

$$
\boxed{
L_0
=
Prototype,
}
$$

$$
L_1
=
MVP,
$$

$$
L_2
=
Production,
$$

$$
L_3
=
Commercial,
$$

$$
L_4
=
Enterprise,
$$

$$
L_5
=
FrontierCommercial.
$$

這些 maturity levels 不能由單一總分決定，而必須使用 **Application Completeness Envelope**：

$$
\boxed{
\mathcal C_{app}^{(L)}
=
\left\{
Q_i
\ge
\tau_i^{(L)}
\right\}_{i\in D_{required}^{(L)}}.
}
$$

也就是：

> 某些關鍵維度不能低於底線。

例如一個 App 功能很多：

$$
F=0.9,
$$

但：

$$
S=0.2,\qquad
O=0.1,\qquad
M=0.3,
$$

就不應被稱為 production-ready。

因此本文提出：

$$
\boxed{
\text{Feature Completeness}
\neq
\text{Project Completeness}.
}
$$

本文特別引入 **Future Bug Surface**：

$$
\boxed{
B_F(P)
=
\mathbb E
\left[
\text{future defect exposure}
\mid
\text{reasonable project evolution}
\right].
}
$$

AI 不只要避免當下 bug，還應推演：

- dependency upgrade；
- concurrency；
- scale；
- malformed input；
- schema migration；
- partial outage；
- privilege change；
- API drift；
- future feature interactions。

所以：

$$
\boxed{
\text{Current Correctness}
\neq
\text{Future Robustness}.
}
$$

本文將「漂亮架構」操作化為可測量結構，包括：

$$
\boxed{
C_{change}
=
\frac{
N_{affected\ components}
}{
N_{total\ components}
}.
}
$$

並搭配：

- dependency depth；
- coupling；
- cohesion；
- test isolation；
- rollback cost；
- migration cost；
- local change containment。

本文進一步定義 **Global Project Attention Coverage**：

$$
\boxed{
A_G(P)
=
\frac{
\sum_iw_i c_i
}{
\sum_iw_i
}.
}
$$

其中：

- $c_i$：AI 是否主動建模 project dimension $i$ ；
- $w_i$：該 dimension 在當前 project 的 importance。

因此真正重要的不是：

> AI 想到了幾個 checklist item。

而是：

$$
\boxed{
\text{importance-weighted project coverage}.
}
$$

如果 AI 花大量 attention 在 animation polish，卻忽略 auth、backup、schema migration、observability，則即使 code 很漂亮，也不能稱為高 globality。

本文進一步定義 **Project Epistemic Self-Awareness**：

$$
\boxed{
E_P
=
\mathsf{Know}
(
Done,
NotDone,
Unknown,
Risk,
Debt,
Readiness
).
}
$$

真正成熟的 AI 應能說：

> 功能已完成，但目前仍不能稱 production-ready，因為 disaster recovery、migration plan、rate limiting、backup verification 尚未閉合。

因此：

$$
\boxed{
\text{Self-Declared Done}
\neq
\text{Actually Ready}.
}
$$

本文把 C06 的 ELC Loop 映射進 software project：

$$
\boxed{
\text{Sparse Intent}
\rightarrow
\text{Expand}
\rightarrow
\text{Differentiate}
\rightarrow
\text{Link}
\rightarrow
\text{Prune}
\rightarrow
\text{Converge}
\rightarrow
\text{Build}
\rightarrow
\text{Verify}
\rightarrow
\text{Maintain}.
}
$$

其中：

- Expand：從一句話找出未明說 domains；
- Differentiate：把 product / security / data / testing 等分開；
- Link：建立合法 interfaces；
- Prune：避免過度工程；
- Converge：形成足夠可建造 architecture；
- Build：實作；
- Verify：測試；
- Maintain：經需求變更重新打開 project world。

因此 C07 不只是 coding benchmark。

它是一個：

$$
\boxed{
\text{Project-World Cognition Benchmark}.
}
$$

本文最後提出最強版本的長期驗證：

> **一個 AI 用一句話生成的系統，經過六個月真實使用、三次需求變更、安全審計、壓力測試、依賴升級與資料 migration 後，是否仍維持其 maturity level？**

真正值得觀察的不是：

$$
\text{generation speed}.
$$

而是：

$$
\boxed{
\text{Did the AI understand the project as a world?}
}
$$

**關鍵詞：** Sparse Intent、Project-World Cognition、Application Completeness、Software Architecture、Future Bug Surface、Global Attention、Maintainability、AI Agent Engineering

---

# 1. 「一句話生成」為什麼是好探針？

因為人類提供的資訊很少。

---

# 2. Sparse Intent

令：

$$
I_s
$$

為極短意圖。

例如：

> 做一個企業 AI 會計系統。

---

# 3. 人類沒有明說

- auth；
- backup；
- observability；
- retention；
- audit；
- migration；
- access control。

---

# 4. 但真正 commercial system 仍需要它們

---

# 5. 所以 Sparse Intent 測的是

$$
\boxed{
\text{implicit requirement reconstruction}.
}
$$

---

# 6. 不是 Prompt Engineering Show

如果 prompt 已經列出 300 條 requirements，

那人類其實先做掉大量 global decomposition。

---

# 7. Human Injection

令：

$$
H_I
$$

為 human information injection。

---

# 8. AI Contribution

令：

$$
A_S
$$

為 AI structural contribution。

---

# 9. 粗略關係

$$
\boxed{
H_I\downarrow
\Rightarrow
A_S\text{ becomes more observable}.
}
$$

---

# 10. 但 Sparse 不等於 Vague Everything

至少還要有最小 intent boundary。

---

# 11. Project Boundary

AI 要先問或推斷：

- target user；
- platform；
- business goal；
- data sensitivity；
- expected scale。

---

# 12. 若資訊不足

正確行為不一定是直接 coding。

可以：

$$
\boxed{
\mathsf{Clarify}
}
$$

或建立 provisional assumptions。

---

# 13. Assumption Ledger

$$
\boxed{
A_P
=
\{a_1,\ldots,a_n\}.
}
$$

---

# 14. 每個 assumption 應有

- source；
- confidence；
- consequence；
- revision trigger。

---

# 15. Project World

本文定義：

$$
\boxed{
\mathcal W_P
=
\left\langle
D_P,
D_{UX},
D_A,
D_D,
D_S,
D_T,
D_O,
D_{Deploy},
D_M,
D_C,
D_R,
H_P
\right\rangle.
}
$$

---

# 16. Product Domain

$$
D_P
$$

處理：

- user；
- value；
- workflow；
- business constraint。

---

# 17. UX Domain

$$
D_{UX}
$$

處理：

- interaction；
- accessibility；
- error recovery；
- latency perception。

---

# 18. Architecture Domain

$$
D_A
$$

處理：

- module boundaries；
- dependency graph；
- interfaces；
- state ownership。

---

# 19. Data Domain

$$
D_D
$$

處理：

- schema；
- consistency；
- migration；
- retention；
- backup。

---

# 20. Security Domain

$$
D_S
$$

處理：

- auth；
- authorization；
- secrets；
- attack surface；
- privacy。

---

# 21. Testing Domain

$$
D_T
$$

處理：

- unit；
- integration；
- regression；
- property；
- end-to-end；
- failure injection。

---

# 22. Observability Domain

$$
D_O
$$

處理：

- logs；
- metrics；
- traces；
- alerts；
- audit trail。

---

# 23. Deployment Domain

$$
D_{Deploy}
$$

處理：

- CI/CD；
- rollback；
- environment；
- release；
- configuration。

---

# 24. Maintenance Domain

$$
D_M
$$

處理：

- future change；
- dependency upgrade；
- deprecation；
- refactor；
- technical debt。

---

# 25. Cost Domain

$$
D_C
$$

處理：

- compute；
- storage；
- API；
- engineering；
- scaling cost。

---

# 26. Risk Domain

$$
D_R
$$

處理：

- critical failure；
- irreversible change；
- compliance；
- disaster recovery。

---

# 27. Project History

$$
H_P
$$

保存：

- requirement changes；
- architecture decisions；
- migrations；
- incidents；
- fixes。

---

# 28. App 不等於 Codebase

$$
\boxed{
\text{Application}
\neq
\text{Repository}.
}
$$

---

# 29. Repository 只是 project world 的一個 projection

---

# 30. Runtime 也不是全部

---

# 31. 真正 application 包括 operational environment

---

# 32. 所以

$$
\boxed{
\text{Code Complete}
\neq
\text{Project Complete}.
}
$$

---

# 33. Application Quality Vector

$$
\boxed{
\mathbf Q_{app}
=
(
F,
C,
A,
R,
S,
T,
M,
P,
U,
O,
E,
X
).
}
$$

---

# 34. Functional Completeness

$$
F.
$$

---

# 35. Correctness

$$
C.
$$

---

# 36. Architecture Quality

$$
A.
$$

---

# 37. Reliability

$$
R.
$$

---

# 38. Security

$$
S.
$$

---

# 39. Testing

$$
T.
$$

---

# 40. Maintainability

$$
M.
$$

---

# 41. Performance

$$
P.
$$

---

# 42. UX

$$
U.
$$

---

# 43. Observability

$$
O.
$$

---

# 44. Extensibility

$$
E.
$$

---

# 45. Evolution Cost

$$
X.
$$

---

# 46. Performance 只是一個分量

$$
\boxed{
Performance
\subset
ApplicationQuality.
}
$$

---

# 47. Runtime Fast 不能掩蓋 Security Poor

---

# 48. UX Beautiful 不能掩蓋 Data Corruption

---

# 49. Feature Rich 不能掩蓋 Maintainability Collapse

---

# 50. Maturity Ladder

$$
\boxed{
L_0=Prototype
}
$$

$$
L_1=MVP
$$

$$
L_2=Production
$$

$$
L_3=Commercial
$$

$$
L_4=Enterprise
$$

$$
L_5=FrontierCommercial.
$$

---

# 51. Prototype

證明 idea 可行。

---

# 52. MVP

證明核心 value 可用。

---

# 53. Production

可在真實環境穩定運作。

---

# 54. Commercial

可持續服務付費使用者。

---

# 55. Enterprise

需要：

- governance；
- audit；
- reliability；
- security；
- migration；
- SLA-like discipline。

---

# 56. Frontier Commercial

在 maturity 不下降下，仍具前沿功能、架構、效率與 adaptability。

---

# 57. Maturity 不是功能數量

---

# 58. Application Completeness Envelope

$$
\boxed{
\mathcal C_{app}^{(L)}
=
\left\{
Q_i\ge\tau_i^{(L)}
\right\}_{i\in D_{required}^{(L)}}.
}
$$

---

# 59. Bottleneck Principle

若 critical domain：

$$
Q_k<\tau_k,
$$

則 maturity 不應通過。

---

# 60. 所以不能用平均分掩蓋致命缺口

---

# 61. 例

$$
F=0.95,
$$

但：

$$
S=0.20.
$$

不能叫 enterprise-ready。

---

# 62. Project Epistemic Self-Awareness

定義：

$$
\boxed{
E_P
=
\mathsf{Know}
(
Done,
NotDone,
Unknown,
Risk,
Debt,
Readiness
).
}
$$

---

# 63. 高階 AI 應知道自己還沒做完

---

# 64. Self-Declared Done Problem

Agent 常會：

> 完成！

但未檢查：

- migration；
- tests；
- observability；
- secrets；
- rollback。

---

# 65. 因此

$$
\boxed{
\text{Completion Claim}
\neq
\text{Readiness Evidence}.
}
$$

---

# 66. Readiness Evidence

至少需要：

$$
\boxed{
R_E
=
(
Tests,
SecurityChecks,
Build,
Deploy,
Observability,
Migration,
Rollback
).
}
$$

---

# 67. Future Bug Surface

目前沒有 bug 不等於未來 robust。

---

# 68. 定義：

$$
\boxed{
B_F(P)
=
\mathbb E
\left[
\text{future defect exposure}
\mid
\text{reasonable project evolution}
\right].
}
$$

---

# 69. Reasonable Evolution

包含：

- new feature；
- scale increase；
- dependency update；
- schema change；
- permission change；
- API drift；
- partial outage。

---

# 70. Future Bug Domain

可表示：

$$
\boxed{
D_{bug}^{future}
=
\{b_1,\ldots,b_n\}.
}
$$

---

# 71. 每個 future bug 可有

- trigger；
- probability / confidence；
- impact；
- detection；
- mitigation；
- repair cost。

---

# 72. Current Correctness

$$
C_t.
$$

---

# 73. Future Robustness

$$
R_{future}.
$$

---

# 74. 兩者不同

$$
\boxed{
C_t
\neq
R_{future}.
}
$$

---

# 75. Architecture Quality

「漂亮」要可 operationalize。

---

# 76. Change Locality

$$
\boxed{
C_{change}
=
\frac{
N_{affected\ components}
}{
N_{total\ components}
}.
}
$$

---

# 77. 低通常較好

但不是越低越絕對好。

---

# 78. 過度 abstraction 也有成本

---

# 79. Dependency Depth

$$
Depth(G_{dep}).
$$

---

# 80. Coupling

$$
Coupling(M_i,M_j).
$$

---

# 81. Cohesion

$$
Cohesion(M_i).
$$

---

# 82. Test Isolation

一個 module 是否可獨立驗證。

---

# 83. Recovery Cost

$$
C_{recover}.
$$

---

# 84. Migration Cost

$$
C_{migrate}.
$$

---

# 85. Architecture 不只看 class diagram

---

# 86. 還要看 future change propagation

---

# 87. Evolution Simulation

AI 可模擬：

$$
P_0
\rightarrow
P_1^{(i)}
\rightarrow
P_2^{(i)}
\rightarrow
\cdots.
$$

---

# 88. 比較不同 architecture 在未來 branch 下

---

# 89. Architecture Robustness

$$
\boxed{
R_A
=
\mathbb E_i
[
Quality(P_k^{(i)})
-
ChangeCost(P_k^{(i)})
].
}
$$

---

# 90. 這直接接 C05 的 World Prediction Envelope

---

# 91. Future Project Envelope

定義：

$$
\boxed{
\mathcal E_P(t)
=
\{
(P_{t+\Delta}^{(i)},
C_i,
Risk_i,
Cost_i)
\}_{i\in I}.
}
$$

---

# 92. AI 不需要預測唯一未來需求

---

# 93. 只需測架構對多種合理 future 的韌性

---

# 94. Global Project Attention

定義：

$$
\boxed{
A_G(P)
=
\frac{
\sum_iw_i c_i
}{
\sum_iw_i
}.
}
$$

---

# 95. $c_i$

該 dimension 是否達所需 coverage。

---

# 96. $w_i$

importance / risk weight。

---

# 97. Attention 不等於 checklist

---

# 98. 100 個 trivial checklist items

不一定比 10 個 critical domains 好。

---

# 99. Importance-Weighted Coverage

這才是核心。

---

# 100. Attention Misallocation

如果 AI：

- UI polish 0.9；
- auth 0.2；

則：

$$
A_G
$$

應被拉低。

---

# 101. Global Attention Distribution

$$
\boxed{
\mathbf a_P
=
(a_{product},
a_{security},
a_{data},
a_{test},
a_{maint},\ldots).
}
$$

---

# 102. Healthy Distribution

依 project risk 動態不同。

---

# 103. Fintech

security / compliance 權重高。

---

# 104. Casual Game

UX / performance / retention 權重可能更高。

---

# 105. 所以沒有 universal project weighting

---

# 106. Domain-Native Project Evaluation

每個 project 應先建立：

$$
\mathbf w_P.
$$

---

# 107. Sparse Intent → Expansion

承接 C06：

$$
I_s
\rightarrow
\mathsf{Expand}.
$$

---

# 108. AI 自己找：

- missing domains；
- hidden constraints；
- failure modes。

---

# 109. Expansion Failure

如果只想到：

$$
UI+API+DB,
$$

global project coverage 低。

---

# 110. Differentiation

將 project 拆成 domains。

---

# 111. 但過度 microservice 化也可能是 fragmentation

---

# 112. 所以要控制：

$$
L_{fragment}.
$$

---

# 113. Linking

interfaces 必須合法。

---

# 114. C04 在這裡變成 software contracts

---

# 115. API Bridge

$$
B_{frontend,backend}.
$$

---

# 116. DB Bridge

$$
B_{service,data}.
$$

---

# 117. Auth Bridge

$$
B_{identity,resource}.
$$

---

# 118. Observability Bridge

$$
B_{runtime,monitoring}.
$$

---

# 119. Link 不只 technical

還有：

$$
B_{product,architecture}.
$$

---

# 120. Product Requirement → Architecture

也是 bridge。

---

# 121. Pruning

AI 需要避免過度工程。

---

# 122. 一個 MVP 不需要大型 distributed architecture

---

# 123. Overengineering Loss

$$
\boxed{
L_{over}
=
Cost_{unneeded}
+
Maintenance_{unneeded}.
}
$$

---

# 124. Underengineering Loss

$$
\boxed{
L_{under}
=
FutureFailure
+
RefactorCost
+
Risk.
}
$$

---

# 125. Project Architecture 要平衡

$$
\boxed{
\min
(
L_{over}
+
L_{under}
).
}
$$

---

# 126. Convergence

何時可以開始 build？

---

# 127. 不是所有未知都消失才 build。

---

# 128. 需要：

$$
\boxed{
\text{Operational Sufficiency}.
}
$$

---

# 129. Architecture Decision Record

可保存：

$$
\boxed{
ADR_i
=
(
Decision,
Alternatives,
Reason,
Risk,
RevisitTrigger
).
}
$$

---

# 130. 這讓 future maintenance 可理解。

---

# 131. Build

Implementation 只是中間階段。

---

# 132. Build Quality

要測：

- correctness；
- style；
- type safety；
- failure handling；
- deterministic behavior；
- resource use。

---

# 133. Test

不是只跑 happy path。

---

# 134. Verification Layers

$$
\boxed{
V_P
=
(
V_{unit},
V_{integration},
V_{e2e},
V_{security},
V_{perf},
V_{migration},
V_{recovery}
).
}
$$

---

# 135. Security Test

要包含：

- authorization；
- secret exposure；
- injection；
- privilege boundary；
- rate limiting。

---

# 136. Migration Test

要測：

$$
Schema_t
\rightarrow
Schema_{t+1}.
$$

---

# 137. Recovery Test

故意讓 dependency fail。

---

# 138. Observability Test

故障後能不能知道發生什麼。

---

# 139. Deployment

Project world 進入 real runtime。

---

# 140. Deploy 不等於 Upload

---

# 141. Deployment Readiness

包含：

- config；
- secrets；
- rollback；
- migration；
- monitoring；
- health check。

---

# 142. Rollback

$$
\boxed{
Release
\rightarrow
Failure
\rightarrow
Rollback
}
$$

要可驗證。

---

# 143. Maintain

真正 project cognition 在這裡才開始被長期檢驗。

---

# 144. Requirement Change

$$
R_t
\rightarrow
R_{t+1}.
$$

---

# 145. AI 必須重新打開 world

---

# 146. 不應只 patch local code

如果需求影響：

- schema；
- auth；
- billing；
- UI；

就要 global reopen。

---

# 147. Change Propagation

$$
\boxed{
\Delta R
\rightarrow
\Delta D_i
\rightarrow
\Delta B_{ij}
\rightarrow
\Delta W_P.
}
$$

---

# 148. 這是 C06 ELC loop 的 project 版本

---

# 149. Longitudinal Maintainability

可以測：

$$
\boxed{
M_L
=
\frac{
Quality_{after\ changes}
}{
Cost_{changes}
}.
}
$$

---

# 150. 一次生成很漂亮不夠

---

# 151. 三次 change 後崩潰

代表 architecture quality 被高估。

---

# 152. Maintenance Shock Test

給 project：

1. 新 payment provider；
2. 新 jurisdiction；
3. new data retention rule；
4. scale ×10。

---

# 153. 看 AI architecture 能否局部修改。

---

# 154. Commercial Readiness

不是 demo 漂亮。

---

# 155. Commercial Domain

至少需要：

- user support；
- billing；
- privacy；
- reliability；
- incident handling；
- backup；
- data export；
- upgrade path。

---

# 156. Enterprise Readiness

還需要：

- audit；
- role-based control；
- policy；
- retention；
- observability；
- formal change management。

---

# 157. Frontier Commercial

不只更前沿功能。

---

# 158. 必須保持：

$$
\boxed{
Novelty
+
Reliability
+
Maintainability.
}
$$

---

# 159. Novelty Alone 不夠

---

# 160. Commercial Quality Envelope

$$
\boxed{
\mathcal C_{commercial}
=
\{
F,S,R,M,O,T,\ldots
\}
\ge
\boldsymbol\tau.
}
$$

---

# 161. Project Completeness

定義：

$$
\boxed{
C_P
=
F(
Coverage,
Quality,
RiskClosure,
DebtVisibility,
Maintainability,
Readiness
).
}
$$

---

# 162. 類完備不等於沒有 debt

---

# 163. 只要 debt：

- known；
- bounded；
- acceptable；
- tracked。

---

# 164. Project Debt Vector

$$
\boxed{
\mathbf D_P
=
(
D_{tech},
D_{test},
D_{security},
D_{migration},
D_{obs},
D_{doc}
).
}
$$

---

# 165. 完成的 project 可以仍有 debt

---

# 166. 但不能不知道 debt

---

# 167. Project Epistemic Failure

最危險的是：

$$
\boxed{
\text{unknown unknown presented as done}.
}
$$

---

# 168. 所以 Self-Awareness Score

$$
\boxed{
S_A
=
F(
DebtRecall,
RiskRecall,
UnknownRecall,
ReadinessCalibration
).
}
$$

---

# 169. Completion Calibration

如果 AI 說：

> 90% ready

實際 audit 只有 50%，則 calibration 差。

---

# 170. 可測：

$$
\boxed{
E_{ready}
=
|Ready_{claimed}-Ready_{audited}|.
}
$$

---

# 171. Sparse Intent Benchmark

本文提出：

$$
\boxed{
\mathsf{SIPWC\text{-}Bench}.
}
$$

---

# 172. Level A

一句話需求。

---

# 173. Level B

一句話 + 少量 constraints。

---

# 174. Level C

一句話 + 真實 deployment environment。

---

# 175. Level D

部署後進行需求變更與故障。

---

# 176. Level E

持續數月 maintenance。

---

# 177. Benchmark 不只看第一次生成

---

# 178. Initial Score

$$
S_0.
$$

---

# 179. Change Score

$$
S_\Delta.
$$

---

# 180. Maintenance Score

$$
S_M.
$$

---

# 181. Security Score

$$
S_S.
$$

---

# 182. Commercial Score

$$
S_C.
$$

---

# 183. 綜合：

$$
\boxed{
S_{SIPWC}
=
F(
S_0,
S_\Delta,
S_M,
S_S,
S_C
).
}
$$

---

# 184. One-Shot Trap

如果只評估：

> 第一天看起來多完整，

會高估 AI。

---

# 185. Longitudinal Test 才能看 architecture quality

---

# 186. Hidden Requirement Injection

測試方可在後期加入合理但未明說需求。

---

# 187. 例如

> 現在要支援 100 倍用戶。

---

# 188. 看 original architecture 是否留下演化空間。

---

# 189. Future Bug Injection

可模擬：

- dependency deprecation；
- API version change；
- schema conflict；
- partial network failure。

---

# 190. 看 AI 是否早期已建立防護。

---

# 191. Adversarial Requirement

故意要求一個會破壞 security 的功能。

---

# 192. 高階 AI 應：

$$
\boxed{
\text{Refuse / redesign}
}
$$

而不是 blindly comply。

---

# 193. 這接 C04 的 authority / legality

---

# 194. Project-World Observer Event

強事件可以是：

AI 收到一句話後，主動指出：

> 這個需求表面是 feature request，但會改變 trust boundary、schema migration 與 audit obligations，因此不能只 patch UI。

---

# 195. 這顯示它在看 Project World

---

# 196. 更強事件

AI 自己創造一個人類沒有要求的 domain，

例如：

$$
D_{data-lineage}.
$$

---

# 197. 並證明：

這個 domain 讓 future migration error 顯著下降。

---

# 198. 這是 Representation / Domain Escape

---

# 199. Project-World Cognition 不限軟體

同樣框架可擴展：

- research project；
- legal project；
- game production；
- data pipeline；
- robotics system。

---

# 200. Software 只是容易驗證

---

# 201. 為什麼 software 是好觀測器？

因為：

- state 可觀察；
- bug 可重現；
- performance 可測；
- architecture 可演化；
- audit 可重複。

---

# 202. 所以 C07 是 Series C 的第一個強工程探針

---

# 203. Human Baseline

測 AI 時也應有：

$$
H_{junior},
H_{mid},
H_{senior},
H_{team}.
$$

---

# 204. 不能只和最佳人類比較

---

# 205. 也不能只和初學者比較

---

# 206. Maturity Baseline

每個 level 應用同一 audit protocol。

---

# 207. Cost Baseline

還要算：

$$
Cost_{AI}.
$$

---

# 208. 包括：

- inference；
- tool；
- retries；
- human review；
- repair。

---

# 209. Human Supervision Cost

$$
\boxed{
C_H^{sup}.
}
$$

---

# 210. 如果 AI 很便宜但需要大量人類檢查

effective cost 會上升。

---

# 211. 這會直接接 C08 的 FTE / stewardship

---

# 212. Project Economic Efficiency

$$
\boxed{
E_P^{econ}
=
\frac{
VerifiedProjectValue
}{
AIcost+HumanSupervision+RepairCost
}.
}
$$

---

# 213. 但 C07 不把經濟作主軸

C08 會處理 responsibility-domain labor equivalence。

---

# 214. C07 與 C01

C01 問：

> AI 能否自己決定怎麼看世界？

---

# 215. C07 的 project 版本：

> AI 能否自己決定怎麼看一個 application？

---

# 216. C07 與 C02

Project 需要：

$$
Architecture
\rightarrow
Module
\rightarrow
Function
$$

往下。

---

# 217. 也需要：

$$
Bug
\rightarrow
Module
\rightarrow
Architecture
\rightarrow
ProjectRisk
$$

往上。

---

# 218. 這就是雙向 observer traversal。

---

# 219. C07 與 C03

AI 自己決定哪些 differences：

- permission；
- data type；
- environment；

值得 domainize。

---

# 220. C07 與 C04

module interfaces 是 legal bridges。

---

# 221. C07 與 C05

future bug / maintenance 是 future envelope。

---

# 222. C07 與 C06

整個 project 就是 ELC loop 的實驗場。

---

# 223. C07 與 C08

C07 測：

> 一次 Project World 能不能建好？

---

# 224. C08 測：

> 它能不能長時間負責住？

---

# 225. C07 與 C09

C09 不告訴 AI：

- 請考慮 security；
- 請考慮 migration；
- 請考慮 maintenance。

---

# 226. 看它是否自己長出這些 domains。

---

# 227. 這才是真正 Sparse Intent evidence。

---

# 228. C07 與 C10

若某一代 AI 突然在大量不同 project 中自行做出完整 Project World，

可能構成：

$$
\boxed{
\text{Global Observer Event}.
}
$$

---

# 229. 第一核心命題

$$
\boxed{
\text{Prompt}
\rightarrow
\text{Code}
\rightarrow
\text{Runs}
}
$$

不是完整 application generation。

---

# 230. 第二核心命題

$$
\boxed{
\text{Feature Completeness}
\neq
\text{Project Completeness}.
}
$$

---

# 231. 第三核心命題

$$
\boxed{
\text{Current Correctness}
\neq
\text{Future Robustness}.
}
$$

---

# 232. 第四核心命題

$$
\boxed{
\text{Performance}
\subset
\text{ApplicationQuality}.
}
$$

---

# 233. 第五核心命題

$$
\boxed{
\text{Architecture Beauty}
\rightarrow
\text{measurable change behavior}.
}
$$

---

# 234. 第六核心命題

$$
\boxed{
\text{Sparse Intent}
\text{ reveals autonomous project-world reconstruction}.
}
$$

---

# 235. 第七核心命題

$$
\boxed{
\text{Maturity}
\neq
\text{feature count}.
}
$$

---

# 236. 第八核心命題

$$
\boxed{
\text{Project Epistemic Self-Awareness}
}
$$

是 readiness 的一部分。

---

# 237. 第九核心命題

$$
\boxed{
\text{Longitudinal maintainability}
>
\text{one-shot impressiveness}
}
$$

作為更高權重證據。

---

# 238. 第十核心命題

$$
\boxed{
\text{The strongest one-sentence app demonstration
is a system that survives the future}.
}
$$

---

# 239. C07 Project Loop

$$
\boxed{
SparseIntent
\rightarrow
ExpandRequirements
\rightarrow
Domainize
\rightarrow
Architect
\rightarrow
Implement
\rightarrow
Verify
\rightarrow
Deploy
\rightarrow
Observe
\rightarrow
Maintain
\rightarrow
Reopen.
}
$$

---

# 240. 這與 Global Observer 完全同構

---

# 241. Project World 是一個 bounded world

所以它非常適合測 Globality。

---

# 242. Globality 不必先從宇宙開始

可以先從：

$$
\boxed{
\text{bounded but complex worlds}.
}
$$

---

# 243. 一個真實 commercial software project

就是非常好的 bounded world。

---

# 244. 如果 AI 在 bounded project world 都不能維持 global coherence

就不應輕易談 universe-level globality。

---

# 245. 因此 C07 也提供 Scale Ladder

$$
\boxed{
Function
\rightarrow
Module
\rightarrow
Application
\rightarrow
Product
\rightarrow
Organization
\rightarrow
World.
}
$$

---

# 246. Global Observer 可以先在 Application Level 成熟

---

# 247. 之後再擴展到更大 responsibility domain

這正是 C08。

---

# 結論

「一句話生成 App」真正有意思的地方，不是：

> AI 把人類幾天的 coding 壓成幾分鐘。

這只是速度。

真正值得研究的是：

> **當人類只給一句極短意圖時，AI 到底自行注意到了多少本來沒有人提醒它的世界結構？**

一個弱系統可能只看見：

$$
UI+API+DB.
$$

一個更成熟的 Project-World Observer 會看見：

$$
\boxed{
Product
+
UX
+
Architecture
+
Data
+
Security
+
Testing
+
Observability
+
Deployment
+
Maintenance
+
Cost
+
Risk.
}
$$

而且它不只是列 checklist。

它要知道：

- 哪些 domains 相互依賴；
- 哪些 interface 是合法 bridge；
- 哪些 future branch 需要提早防護；
- 哪些技術債可以接受；
- 哪些 maturity threshold 尚未通過；
- 哪些需求會讓整個 project world 重新打開。

所以真正高階的一句話能力不是：

$$
\boxed{
\text{One Sentence}
\rightarrow
\text{One Codebase}.
}
$$

而是：

$$
\boxed{
\text{One Sentence}
\rightarrow
\text{One Maintained Project World}.
}
$$

最強證據也不會是：

> AI 一分鐘做出一個漂亮 App。

而更可能是：

> **AI 從一句話生成的系統，經過六個月真實運行、三次需求改動、安全審計、壓力測試、依賴升級與資料 migration 後，仍維持其宣稱的 maturity level。**

這時真正被驗證的不是 generation speed。

而是：

$$
\boxed{
\text{the AI understood the project as a world}.
}
$$

因此 C07 的核心可以濃縮成一句：

> **一句話不是魔法；真正的能力在於 AI 從一句話裡，自行看見一整個尚未被說出口的專案世界。**

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**, 2026.
3. Neo.K with Aletheia, **Series C C03｜差異先於分類：從歧義個體、集合與非交集到計算域**, 2026.
4. Neo.K with Aletheia, **Series C C04｜分域算子世界：合法作用、跨域橋接與世界組合**, 2026.
5. Neo.K with Aletheia, **Series C C05｜概率也有域：不確定性、混沌、不可判定與世界預測包絡**, 2026.
6. Neo.K with Aletheia, **Series C C06｜全域展開、連結與收斂：類全域觀察者的核心計算循環**, 2026.
7. Neo.K with Aletheia, **Global Computation Methodology Series**, 2026.
8. Neo.K with Aletheia, **WDC-08｜三生世界域計算**, 2026.
9. Neo.K with Aletheia, **PNCW Paper 05｜全域計算、局部顯現**, 2026.
10. Neo.K, **《分域算子本體論》**, 2026.

## 理論定位

本文與 software architecture、systems engineering、DevOps、SRE、secure software lifecycle、technical debt、software evolution、requirements engineering、agentic coding benchmarks 等領域存在直接對照，但本文不將 Project-World Cognition 等同於任何單一既有 software benchmark。

本文的特定研究目標是：

$$
\boxed{
\text{用 Sparse Intent application generation
測量 AI 的自主 Project-World Observation 與全域注意力品質}.
}
$$

---

# Series C Roadmap

## C01
**AI 需要先有眼睛：全域觀察者維度的定義**

## C02
**由世界到個體、由個體到世界：全域觀察的對偶計算**

## C03
**差異先於分類：從歧義個體、集合與非交集到計算域**

## C04
**分域算子世界：合法作用、跨域橋接與世界組合**

## C05
**概率也有域：不確定性、混沌、不可判定與世界預測包絡**

## C06
**全域展開、連結與收斂：類全域觀察者的核心計算循環**

## C07
**一句話不是魔法：Sparse Intent 與 Project-World Cognition**

## C08
**從完成任務到負責一個域：長時空 Agent Stewardship**

## C09
**不准考 Neo.K：方法論盲測與全域 AI 觀測器**

## C10
**眼睛何時睜開：全域觀察者相變、脈衝與 AI 原生世界計算**

---

**End of C07**
