# PTE-06｜不可壓縮證據底：AI 為何不能把所有科學都變成幾小時實驗

## The Irreducible Evidence Floor: Limits of AI-Accelerated Theory Testing

**系列：** 《假設你是對的》／Provisional Truth Engineering Series（PTE）  
**系列文件：** PTE-06 / 07  
**版本：** v0.1  
**日期：** 2026-09-09  
**作者：** Neo.K  
**研究協作：** AI-assisted theoretical development  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 公開方法論論文／AI 加速科學的證據邊界與不可壓縮時間  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

Provisional Truth Engineering（PTE）前五篇已建立一條快速理論壓測鏈：從暫時真值算子、Theory-to-Engineering Latency、公平重建、認識論回收，到 AI-native Theory Stress Runtime。這些方法在軟體、AI 架構、演算法、形式系統與可模擬工程中，可能把原本需要數週至數月的探索性研究壓縮到日級甚至小時級。

但如果由此推出：

$$
\boxed{
\text{AI acceleration}
\Rightarrow
\text{all scientific evidence becomes fast}
}
$$

則是錯誤的。

本文提出 **Irreducible Evidence Floor（IEF，不可壓縮證據底）**，用來描述一個理論 $T$ 在領域 $D$ 中，無法僅靠更強計算、更長上下文、更好的 Agent、更完整搜尋或更高模擬能力消除的最低外部證據需求：

$$
\boxed{
E_{\min}(T,D)
}
$$

以及其對應的最低證據時間：

$$
\boxed{
L_{\mathrm{floor}}(T,D).
}
$$

本文將理論檢驗總成本拆為：

$$
\boxed{
C_{\mathrm{test}}
=
C_U
+
C_F
+
C_O
+
C_I
+
C_B
+
C_A
+
C_X
+
C_P
}
$$

其中：

- $C_U$：理解與重建成本；
- $C_F$：形式化成本；
- $C_O$：操作化成本；
- $C_I$：實作成本；
- $C_B$：baseline 建立成本；
- $C_A$：分析與推論成本；
- $C_X$：外部實驗協調成本；
- $C_P$：世界本身生成證據的物理／時間成本。

AI 可以顯著壓縮：

$$
C_U,
C_F,
C_I,
C_B,
C_A,
$$

部分壓縮：

$$
C_O,
C_X,
$$

但對某些研究問題：

$$
\boxed{
C_P>0
}
$$

而且可能存在：

$$
\boxed{
C_P
\gg
C_U+C_F+C_I+C_B+C_A.
}
$$

此時真正瓶頸不是「我們想得不夠快」，而是：

> **世界尚未產生足以回答問題的證據。**

本文進一步把證據分成五層：

```text
E0  Internal / Formal Evidence
E1  Simulation / Synthetic Evidence
E2  Historical / Observational External Evidence
E3  Controlled External Experiment
E4  Time-Generated / World-Generated Evidence
```

並提出 **Evidence Substitution Boundary（證據替代邊界）**：低階證據可以降低不確定性、改進實驗設計、篩選候選，但不能自動取代高階證據。

例如，高精度模擬可以支持材料候選排序，卻不能在沒有實驗的情況下建立所有真實製程可靠性；數位分身可以幫助預測藥物反應，卻不能自動取代長期人體安全資料；社會模擬可以比較政策情境，卻不能讓未來十年的制度結果在今天真正發生。

本文特別區分：

$$
\boxed{
\text{Epistemic Compression}
}
$$

與：

$$
\boxed{
\text{Evidence Generation}.
}
$$

前者是把既有資訊更快變成知識；後者是讓世界產生原本不存在的新觀測。

AI 對前者的壓縮可以非常巨大，但後者常存在真正的時間底。

本文最後提出 **Evidence Floor Certificate**、**Proxy Debt**、**Simulation-to-Reality Gap Ledger** 與 **World-Wait Status**，要求 PTE Runtime 在遇到不可壓縮證據時，不得以更多模擬、更多 Agent 或更多自信替代，而應明確輸出：

```text
BLOCKED_BY_EVIDENCE
WAITING_FOR_WORLD
PROXY_ONLY
PHYSICAL_VALIDATION_REQUIRED
LONGITUDINAL_VALIDATION_REQUIRED
```

PTE 的成熟不是讓所有問題看起來都能被 AI 解完，而是讓系統知道：

$$
\boxed{
\text{何時已經不是「算得不夠多」，而是「世界還沒回答」。}
}
$$

**關鍵詞：** Irreducible Evidence Floor、Evidence Generation、Physical Validation、Longitudinal Evidence、Simulation-to-Reality Gap、Proxy Debt、AI Science、World-Generated Evidence、Theory Testing、Provisional Truth Engineering

---

# 0. 邊界聲明

本文不主張：

- 模擬沒有科學價值；
- 物理實驗永遠比理論與形式證明重要；
- 所有領域都存在長時間證據底；
- 任何 external validation 都必須昂貴；
- 現實世界證據天然無偏；
- 觀察資料一定優於合成資料；
- AI 不可能設計出大幅縮短實驗時間的新儀器與方法；
- 不可壓縮證據底是一個固定常數；
- 未來科技無法改變某些今天不可壓縮的等待時間；
- 只要存在 evidence floor，就不值得做前置模擬與理論工作。

本文只研究：

> 對一個指定理論、指定領域與指定主張，哪些證據需求可以被計算與認知能力壓縮，哪些證據必須由外部世界、真實系統或時間演化本身生成。

---

# 1. PTE-02 留下的未解問題

PTE-02 已提出：

$$
L_{TE}\downarrow.
$$

並把研究時間拆成：

$$
L_W,
H_A,
M_W,
C_O,
L_P.
$$

其中：

$$
L_P
$$

代表：

> 物理或外部證據本身所需的時間。

PTE-06 專門處理：

$$
\boxed{
L_P
}
$$

的結構。

---

# 2. AI 可以壓縮研究，但不能總是壓縮世界

設：

$$
T
$$

為理論，

$$
D
$$

為研究領域。

若：

$$
D
=
\text{software},
$$

很多證據可以直接由：

$$
\text{execution}
$$

生成。

---

## 2.1 例如

- 程式是否通過測試；
- 演算法是否在指定資料上收斂；
- event ordering 是否破壞 state；
- protocol 是否符合 contract。

這些問題：

$$
L_P\approx0.
$$

---

## 2.2 但若 $D$ 是

- 長期臨床安全；
- 材料疲勞；
- 生態系演化；
- 天文等待事件；
- 社會制度十年效果；

則：

$$
L_P
$$

可能很大。

---

# 3. 不可壓縮證據底

**定義 3.1（Irreducible Evidence Floor）**

對理論 $T$ 與領域 $D$，

定義：

$$
\boxed{
E_{\min}(T,D)
}
$$

為在當前可用工具、物理法則、測量方法與證據標準下，為使目標 claim 達到指定 epistemic status 所不可省略的最低外部證據集合。

---

# 4. 不可壓縮時間底

如果取得：

$$
E_{\min}(T,D)
$$

需要時間，

定義：

$$
\boxed{
L_{\mathrm{floor}}(T,D)
}
$$

為其最短合理等待時間。

---

## 4.1 核心

即使：

$$
C_U,C_F,C_I,C_B,C_A
\rightarrow0,
$$

仍可能：

$$
\boxed{
L_{\mathrm{total}}
\ge
L_{\mathrm{floor}}.
}
$$

---

# 5. Evidence Floor 不是形而上固定值

它依：

$$
(T,D,t,\mathcal I,\mathcal M)
$$

而變。

其中：

- $t$：技術時代；
- $\mathcal I$：儀器能力；
- $\mathcal M$：測量方法。

---

## 5.1 因此

$$
E_{\min}^{2026}
$$

不一定等於：

$$
E_{\min}^{2036}.
$$

---

# 6. 科技可以降低 evidence floor

例如：

- 更快測序；
- 高通量材料篩選；
- 自動實驗室；
- 加速老化測試；
- 數位病理；
- 自動化望遠鏡。

所以：

$$
\boxed{
E_{\min}(t)
\downarrow
}
$$

可能成立。

---

# 7. 但降低不等於歸零

若研究問題本身要求：

> 五年後會不會出現某種長期結果？

則模擬只能提供：

$$
\text{prediction},
$$

不是：

$$
\text{five-year observation}.
$$

---

# 8. Evidence Generation 與 Evidence Processing

這是本文最重要的區分。

---

## 8.1 Evidence Processing

已有：

$$
E.
$$

AI 做：

$$
\boxed{
E
\rightarrow
\text{analysis}
\rightarrow
\text{inference}.
}
$$

---

## 8.2 Evidence Generation

原本：

$$
E^{*}
$$

不存在。

必須透過：

- experiment；
- measurement；
- time；
- intervention；

讓：

$$
\boxed{
E^{*}
}
$$

真的出現。

---

# 9. AI 在第一類上非常強

AI 可以：

- 搜尋；
- 統計；
- 整合；
- 建模；
- 推演；
- 形式化。

---

# 10. 第二類常需要世界

$$
\boxed{
\text{Computation}
\not\Rightarrow
\text{new physical observation}.
}
$$

---

# 11. 五層證據階梯

本文定義：

```text
E0 Internal / Formal
E1 Simulation / Synthetic
E2 Historical / Observational
E3 Controlled External Experiment
E4 Time-Generated / World-Generated
```

---

# 12. E0 — Internal / Formal Evidence

包括：

- proof；
- model checking；
- theorem proving；
- exact computation；
- internal consistency；
- finite exhaustive search。

---

## 12.1 對某些 claim

E0 就足夠。

例如：

$$
\text{formal theorem}.
$$

---

# 13. E1 — Simulation / Synthetic Evidence

包括：

- simulation；
- Monte Carlo；
- synthetic benchmark；
- digital twin；
- generated counterfactual。

---

## 13.1 它可以測

- model behavior；
- sensitivity；
- robustness；
- edge case；
- possible mechanism。

---

## 13.2 但

$$
\boxed{
E1
\not\Rightarrow
E3
}
$$

自動成立。

---

# 14. E2 — Historical / Observational Evidence

包括：

- archive；
- logs；
- cohort；
- natural experiment；
- observational dataset。

---

## 14.1 優點

世界已經產生資料。

所以：

$$
L_{\mathrm{floor}}
$$

可能很低。

---

## 14.2 但有 causal limit

$$
\boxed{
\text{Observation}
\neq
\text{Intervention}.
}
$$

---

# 15. E3 — Controlled External Experiment

包括：

- lab test；
- randomized trial；
- controlled deployment；
- hardware measurement；
- field experiment。

---

# 16. E4 — Time-Generated Evidence

某些證據只能由：

$$
\text{system evolving through time}
$$

產生。

例如：

- long-term safety；
- aging；
- ecological shift；
- institutional adaptation；
- chronic effect。

---

# 17. Evidence Substitution Boundary

**定義 17.1**

若低層證據：

$$
E_i
$$

不能在不增加未證假設的情況下建立高層 claim，

則存在：

$$
\boxed{
S_{i\rightarrow j}
}
$$

證據替代邊界。

---

# 18. Proxy 不等於 Target

設：

$$
P
$$

為 proxy，

$$
Y
$$

為 target。

即使：

$$
\mathrm{Corr}(P,Y)\gg0,
$$

也不能直接：

$$
P=Y.
$$

---

# 19. Proxy Debt

若研究以 proxy：

$$
P
$$

暫代：

$$
Y,
$$

定義：

$$
\boxed{
D_P
}
$$

為 Proxy Debt。

---

## 19.1 Debt 表示

> 還欠一次 target-level validation。

---

# 20. Proxy Debt 不能被更多 proxy 清零

$$
P_1,P_2,\ldots,P_n
$$

都只是 proxy 時，

仍可能：

$$
D_P>0.
$$

---

# 21. Simulation-to-Reality Gap

定義：

$$
\boxed{
G_{SR}
=
d(
P_{\mathrm{sim}},
P_{\mathrm{real}}
).
}
$$

---

## 21.1 如果沒有 real data

則：

$$
G_{SR}
=
\text{NotMeasured}.
$$

---

# 22. 不得假定 $G_{SR}=0$

這是 AI 加速研究最常見的過度外推之一。

---

# 23. Perfect Simulator 的例外

如果存在：

$$
S^{*}
$$

能被證明與 target system 等價，

則：

$$
E1
$$

可以更接近：

$$
E3.
$$

---

## 23.1 但證明等價本身很難

需要：

$$
\boxed{
\text{model adequacy evidence}.
}
$$

---

# 24. Model Adequacy Debt

定義：

$$
\boxed{
D_M
}
$$

為：

> 模擬器對現實 target 的未驗證差距。

---

# 25. Digital Twin 的限制

Digital twin：

$$
\neq
$$

world itself。

---

## 25.1 它是

$$
\boxed{
\text{continuously calibrated proxy}.
}
$$

---

# 26. Longitudinal Evidence

若 claim：

$$
C
$$

顯式包含：

$$
t+\Delta t,
$$

那麼其驗證可能需要：

$$
\Delta t.
$$

---

# 27. 時間是變量，不只是成本

例如：

$$
Y(t)
$$

本身就是研究對象。

---

## 27.1 因此

把：

$$
t
$$

跳過，

可能等於改變問題。

---

# 28. Accelerated Aging

材料可用：

- 高溫；
- 高壓；
- 高負載；

模擬長期老化。

---

## 28.1 但它依賴

$$
\boxed{
\text{acceleration model validity}.
}
$$

---

# 29. 所以不是免費壓縮

你把：

$$
L_P
$$

換成：

$$
\text{model assumption}.
$$

---

# 30. Evidence Compression Tradeoff

定義：

$$
\boxed{
L_P\downarrow
\Rightarrow
A_M\uparrow
}
$$

其中：

$$
A_M
$$

是模型假設負擔。

---

# 31. 這形成一條 tradeoff frontier

$$
\boxed{
\mathcal F_E
=
\{
(L_P,A_M,U_E)
\}
}
$$

其中：

$$
U_E
$$

為 evidence uncertainty。

---

# 32. 越想快速

可能越依賴：

- surrogate；
- proxy；
- extrapolation；
- accelerated protocol。

---

# 33. 科學速度不是單調免費

$$
\boxed{
\text{faster evidence}
\not\Rightarrow
\text{same epistemic strength}.
}
$$

---

# 34. 不同 claim 有不同 floor

同一理論：

$$
T
$$

可能含：

$$
C_1,C_2,C_3.
$$

---

## 34.1 例如

 $C_1$ 是 formal claim：

$$
E_{\min}(C_1)=E0.
$$

 $C_2$ 是 engineering claim：

$$
E_{\min}(C_2)=E3.
$$

 $C_3$ 是 long-term societal claim：

$$
E_{\min}(C_3)=E4.
$$

---

# 35. 因此不能給整套理論單一 Evidence Level

應 claim-level。

---

# 36. Evidence Requirement Function

定義：

$$
\boxed{
\mathcal E_R(C_i)
=
(
E_{\mathrm{level}},
n,
\tau,
q,
u
)
}
$$

其中：

- evidence level；
- sample size；
- duration；
- quality；
- uncertainty tolerance。

---

# 37. Scientific Claim 的時間結構

某些 claim 是：

$$
\text{atemporal}.
$$

例如形式定理。

---

# 38. 某些是 snapshot

例如：

> 現在的系統 latency 是多少？

---

# 39. 某些是 trajectory

例如：

> 三年後 failure rate 是否上升？

---

# 40. Trajectory claim 天生依賴時間

$$
\boxed{
\text{trajectory truth}
\neq
\text{snapshot truth}.
}
$$

---

# 41. World-Wait Status

PTE Runtime 應允許：

```text
WAITING_FOR_WORLD
```

---

## 41.1 這不是失敗

表示：

> 現階段所有可做的 epistemic processing 已完成，但 target evidence 尚未生成。

---

# 42. Evidence Floor Certificate

最小：

```text
claim_id
target_evidence
minimum_evidence_level
current_evidence_level
proxy_evidence
simulation_evidence
physical_validation_needed
minimum_duration
blocking_condition
next_observation
```

---

# 43. 這張證書有什麼用？

避免系統因：

$$
\text{more compute}
$$

而誤以為：

$$
\text{evidence complete}.
$$

---

# 44. Physical Validation Required

如果：

$$
E_{\min}\ge E3,
$$

PTE 應輸出：

```text
PHYSICAL_VALIDATION_REQUIRED
```

---

# 45. Longitudinal Validation Required

若：

$$
E_{\min}=E4,
$$

輸出：

```text
LONGITUDINAL_VALIDATION_REQUIRED
```

---

# 46. Proxy Only

若只有：

$$
E1
$$

或：

$$
E2
$$

而 target 要：

$$
E3,
$$

輸出：

```text
PROXY_ONLY
```

---

# 47. Blocked by Evidence

若必要 evidence：

$$
E^{*}
$$

目前無法取得：

```text
BLOCKED_BY_EVIDENCE
```

---

# 48. 不能寫成 False

沒有證據：

$$
\neq
$$

反證。

---

# 49. 也不能寫成 Supported

如果 evidence level 不夠。

---

# 50. Evidence Status Vocabulary

```text
FORMALLY_ESTABLISHED
SIMULATION_SUPPORTED
OBSERVATIONALLY_SUPPORTED
EXPERIMENTALLY_SUPPORTED
LONGITUDINALLY_SUPPORTED
PROXY_ONLY
NOT_MEASURED
BLOCKED_BY_EVIDENCE
WAITING_FOR_WORLD
```

---

# 51. AI 的第一個貢獻：縮短準備時間

即使：

$$
L_P
$$

很大，

AI 仍能壓縮：

$$
L_{\mathrm{prep}}.
$$

---

## 51.1 包括

- protocol；
- sample design；
- power analysis；
- instrument code；
- data pipeline；
- monitoring；
- analysis plan。

---

# 52. 第二個貢獻：提高每次實驗資訊量

若一次 physical experiment 很昂貴，

AI 可以優化：

$$
\boxed{
IG/C_P.
}
$$

---

# 53. Information Gain per Physical Experiment

定義：

$$
\boxed{
IG_P
=
\frac{
\Delta H
}{
C_P
}
}
$$

其中：

$$
\Delta H
$$

是 uncertainty reduction。

---

# 54. 第三個貢獻：Active Experiment Design

AI 可選：

$$
x^{*}
=
\arg\max_x
\mathbb E[IG(x)].
$$

---

# 55. 因此 AI 可以減少實驗次數

但不能保證：

$$
n=0.
$$

---

# 56. 第四個貢獻：跨資料再利用

既有世界資料：

$$
E_{\mathrm{historical}}
$$

可以降低新實驗需求。

---

## 56.1 但前提

- domain match；
- measurement quality；
- provenance；
- causal relevance。

---

# 57. 第五個貢獻：自動監測世界

對 E4 claim，

AI 可以：

- schedule；
- monitor；
- detect change；
- update evidence。

---

# 58. 但它仍需等事件發生

$$
\boxed{
\text{monitoring speed}
\neq
\text{world evolution speed}.
}
$$

---

# 59. 生物醫學例

假設 claim：

> 某治療長期五年安全。

即使 AI：

- 分析所有既有資料；
- 建數位病人；
- 跑十億模擬；

仍不等於：

$$
\text{five-year human outcome observed}.
$$

---

# 60. 材料例

claim：

> 元件在正常環境下可可靠運行十年。

加速老化可以降低：

$$
L_P.
$$

但需要：

$$
\text{validated acceleration law}.
$$

---

# 61. 軟體例

claim：

> deterministic state machine 對所有 bounded inputs 保持 invariant。

若輸入域有限且可 exhaustive，

則：

$$
E_{\min}\approx E0.
$$

所以可非常快。

---

# 62. AI 架構例

claim：

> 新 validator 在 frozen dataset 上 unsafe accept 更低。

只要 dataset 與 implementation 可得：

$$
L_P\approx0.
$$

---

# 63. 社會制度例

claim：

> 某制度十年後提高社會信任。

模擬可提供：

$$
E1,
$$

歷史比較提供：

$$
E2,
$$

但真正新制度的十年結果：

$$
E4.
$$

---

# 64. 天文例

若需要：

> 下一次特定週期事件

才可觀測，

則：

$$
L_{\mathrm{floor}}
$$

受宇宙事件約束。

---

# 65. 粒子物理例

理論可以先：

- formalize；
- simulate；
- calculate cross-section。

但若判別需要 collider event，

仍需：

$$
E3.
$$

---

# 66. Evidence Bottleneck Classification

本文提出：

```text
COMPUTE_BOUND
DATA_BOUND
INSTRUMENT_BOUND
EXPERIMENT_BOUND
TIME_BOUND
EVENT_BOUND
ETHICS_BOUND
```

---

# 67. Compute-Bound

主要瓶頸：

$$
C_{\mathrm{compute}}.
$$

AI / hardware 可壓縮。

---

# 68. Data-Bound

缺：

$$
\text{relevant data}.
$$

---

# 69. Instrument-Bound

測不到目標變量。

---

# 70. Experiment-Bound

需要昂貴 intervention。

---

# 71. Time-Bound

必須等系統演化。

---

# 72. Event-Bound

必須等罕見事件。

---

# 73. Ethics-Bound

不能隨意做必要實驗。

---

# 74. Ethics 也是 evidence floor

不是算力能突破。

---

# 75. 不可做的實驗

某些 causal claim：

$$
\text{direct experiment}
$$

因倫理禁止。

---

## 75.1 此時

可能永遠依賴：

- observational；
- natural experiment；
- indirect evidence。

---

# 76. Evidence Floor 不只物理

也可能是：

$$
\boxed{
\text{institutional / ethical floor}.
}
$$

---

# 77. Legal / Access Bound

資料存在，

但不能合法取得。

---

# 78. 因此 Evidence Availability

定義：

$$
\boxed{
A_E
=
f(
\text{physical},
\text{ethical},
\text{legal},
\text{financial},
\text{temporal}
).
}
$$

---

# 79. Evidence Floor 與資金

有些：

$$
L_P
$$

可以用更多資金降低。

例如更多儀器。

---

# 80. 但不是全部

十年後的真實十年結果，

錢不能讓日曆立刻走十年。

---

# 81. Parallel Cohort

可以平行增加樣本，

但：

$$
\Delta t
$$

仍可能不變。

---

# 82. Time Depth vs Sample Width

定義：

$$
\boxed{
\text{Sample Width}
\neq
\text{Temporal Depth}.
}
$$

---

# 83. 一百萬個一年樣本

不一定等於：

$$
\text{一個五年 trajectory}.
$$

---

# 84. 時間壓縮的非法替代

常見錯誤：

$$
\text{more parallel subjects}
\Rightarrow
\text{longer time evidence}.
$$

不成立。

---

# 85. Evidence Geometry

可以把證據表示為：

$$
E
=
(
w,
d,
c,
r
)
$$

其中：

- $w$：sample width；
- $d$：temporal depth；
- $c$：causal control；
- $r$：realism。

---

# 86. Simulation 通常

$$
r
$$

較低，

但：

$$
w
$$

可極高。

---

# 87. Longitudinal field data

$$
d,r
$$

高，

但：

$$
c
$$

可能低。

---

# 88. Controlled experiment

$$
c
$$

高，

但：

$$
r
$$

不一定最高。

---

# 89. 沒有單一 evidence scalar 足夠

因此不能只說：

> evidence 很多。

---

# 90. Evidence Vector

$$
\boxed{
\mathbf E
=
(
E_w,
E_d,
E_c,
E_r,
E_p
)
}
$$

其中：

$$
E_p
$$

為 provenance quality。

---

# 91. Claim Matching

每個 claim 需要：

$$
\mathbf E_{\mathrm{req}}(C).
$$

---

# 92. Evidence Sufficiency

若：

$$
\mathbf E_{\mathrm{obs}}
\ge
\mathbf E_{\mathrm{req}}
$$

在指定偏序下，

才叫：

$$
\text{sufficient}.
$$

---

# 93. 這不是普通數值大於

不同維度不可完全互換。

---

# 94. Evidence Pareto Frontier

研究可能在：

$$
(w,d,c,r)
$$

間取捨。

---

# 95. AI 可以搜尋 frontier

但不能自動改變：

$$
\text{claim requirement}.
$$

---

# 96. Claim Downgrade 也是合法選項

如果只能取得：

$$
E2,
$$

可以把：

> causal certainty

降成：

> observational association。

---

# 97. 但必須標明 downgrade

接 PTE-04。

---

# 98. Evidence Floor 與 PTE-03

Strong baseline tie：

$$
\Delta_T=0
$$

可能在 E1 成立。

---

## 98.1 但 E3

仍可能揭露差異。

所以：

$$
\boxed{
\text{reconstruction equivalence}
}
$$

也有 evidence-level dependency。

---

# 99. Evidence-Level Reconstruction

定義：

$$
S_T
\sim_{E_i}
B.
$$

表示在：

$$
E_i
$$

層不可區分。

---

# 100. 不能自動外推到 $E_j$

如果：

$$
j>i.
$$

---

# 101. Residue 也會因 evidence level 改變

$$
R_{E1}(T)
\neq
R_{E3}(T).
$$

---

# 102. 因此 PTE-04 的 residue 是暫態

這再次支持：

$$
R_{\mathcal B,\mathcal E}(T).
$$

---

# 103. Evidence Floor 與 PTE-05 Runtime

PTE-TSR 應在 operationalization 時先問：

> 需要哪一層 evidence？

---

# 104. 如果答案是 E4

Runtime 不應繼續假裝：

> 再多跑 simulation 就能 close。

---

# 105. World-Wait Queue

可以建立：

```text
claim_id
required_event
expected_date
monitor
trigger
analysis_plan
```

---

# 106. AI 自動等待與回來分析

這是未來 Agent 很適合做的工作。

---

# 107. 但等待狀態必須明示

$$
\boxed{
\text{WAITING}
\neq
\text{COMPLETE}.
}
$$

---

# 108. Evidence Debt Ledger

每個 claim：

```text
claim_id
current_level
required_level
proxy_debt
model_debt
time_debt
physical_debt
ethical_constraint
next_evidence
```

---

# 109. Time Debt

定義：

$$
\boxed{
D_T
=
L_{\mathrm{floor}}
-
L_{\mathrm{elapsed}}.
}
$$

若正值，

表示還欠：

$$
D_T
$$

時間。

---

# 110. Physical Debt

尚欠：

- lab；
- hardware；
- deployment；
- human trial。

---

# 111. Evidence Completion

只有所有 hard evidence debt：

$$
=0
$$

才可提升相應 status。

---

# 112. 不能用平均抵銷

若：

$$
D_{\mathrm{physical}}>0,
$$

不能因：

$$
D_{\mathrm{simulation}}=0
$$

而說 complete。

---

# 113. AI 最好的角色之一：知道何時停算

如果：

$$
IG_{\mathrm{simulation}}
\rightarrow0
$$

而真正瓶頸是：

$$
E3,
$$

繼續燒算力沒有意義。

---

# 114. Compute-to-Evidence Saturation

定義：

$$
\boxed{
CES
=
\frac{
\partial IG
}{
\partial C_{\mathrm{compute}}
}.
}
$$

---

## 114.1 若

$$
CES\rightarrow0,
$$

應轉向：

$$
\text{external evidence}.
$$

---

# 115. 這是一個重要的停止條件

```text
SIMULATION_SATURATED
PHYSICAL_NEXT
```

---

# 116. Evidence-Aware Research Allocation

資源分配：

$$
\boxed{
x^{*}
=
\arg\max_x
\frac{
IG(x)
}{
C(x)
}.
}
$$

---

# 117. 如果最高 IG 在 physical experiment

就不該繼續：

$$
\text{LLM debate}.
$$

---

# 118. AI 時代可能出現新的浪費

以前浪費是：

> 實驗太貴。

未來可能是：

> 模擬太便宜，所以永遠不去做真正的驗證。

---

# 119. Simulation Comfort Trap

本文稱：

$$
\boxed{
\text{Simulation Comfort Trap}.
}
$$

---

## 119.1 定義

當研究者因：

- synthetic benchmark 一直進步；
- model confidence 很高；
- digital twin 很漂亮；

而推遲必要 real-world test。

---

# 120. Proxy Proliferation Trap

不斷增加 proxy，

卻從不測 target。

---

# 121. Evidence Inflation

一千萬個 synthetic cases：

$$
\neq
$$

一個必要 physical observation。

---

# 122. PTE-06 的反幻覺原則

$$
\boxed{
\text{More simulated evidence}
\not\Rightarrow
\text{higher evidence level}.
}
$$

---

# 123. 形式證明的特殊性

對純數學 claim，

若形式系統、前提與 proof 都明確，

$$
E0
$$

可以是最高需要。

---

# 124. 因此 Evidence Ladder 不是價值排序

不是：

$$
E4>E3>E2>E1>E0.
$$

---

## 124.1 而是 claim-match

$$
\boxed{
\text{right evidence for the right claim}.
}
$$

---

# 125. 理論 claim 如果是 formal

拿人體實驗也沒意義。

---

# 126. Engineering claim 如果是 real-world reliability

只有 proof 也可能不夠。

---

# 127. Claim-Evidence Type Matching

定義：

$$
\boxed{
M_{CE}(C,E)
}
$$

為 claim 與 evidence type 的匹配度。

---

# 128. 高 evidence level 但低 match 仍然沒用

---

# 129. External Validity

E3 的 lab result 也不一定能推：

$$
\text{field}.
$$

---

# 130. Field Validation

可能需要：

$$
E3^{\mathrm{field}}.
$$

---

# 131. Deployment Evidence

對 AI systems，

真實 deployment 可能暴露：

- distribution shift；
- user adaptation；
- adversarial behavior；
- operational drift。

---

# 132. 所以 benchmark 只是 evidence surface 之一

---

# 133. Real-World Feedback Loop

$$
\boxed{
\text{Model}
\rightarrow
\text{Deployment}
\rightarrow
\text{World Response}
\rightarrow
\text{New Evidence}.
}
$$

---

# 134. 反身系統的 evidence floor 更複雜

因為：

$$
\text{deployment changes the environment}.
$$

---

# 135. 社會系統尤其如此

理論一旦被採用，

世界不再是：

$$
D_0.
$$

而變：

$$
D_1.
$$

---

# 136. Evidence Endogeneity

因此：

$$
\boxed{
E
}
$$

可能受理論介入本身影響。

---

# 137. PTE 不能把這當普通 i.i.d.

---

# 138. 自適應 Evidence Floor

對反身系統：

$$
E_{\min}(T,D_t)
$$

隨：

$$
t
$$

變。

---

# 139. Monitoring 必須持續

這接：

$$
\text{condition watch}.
$$

---

# 140. 理論驗證可能不是一次事件

而是：

$$
\boxed{
\text{continuous evidence maintenance}.
}
$$

---

# 141. Evidence Decay

某些 evidence 隨時間失效。

---

## 141.1 例如

- old benchmark；
- old population；
- old hardware；
- old policy environment。

---

# 142. 定義 Evidence Half-Life

$$
\boxed{
\tau_E
}
$$

為 evidence 適用性衰減尺度。

---

# 143. 所以 evidence floor 不只「第一次拿到」

還包括：

> 如何維持。

---

# 144. AI 可降低 maintenance cost

但仍不能保證：

$$
\tau_E=\infty.
$$

---

# 145. PTE-06 可檢驗命題

## IEF-H1：Processing–Generation Separation

隨 AI 能力提升：

$$
C_{\mathrm{processing}}\downarrow
$$

快於：

$$
C_{\mathrm{world\ generation}}.
$$

---

## IEF-H2：Evidence Floor Dominance

對部分實證領域，

當 AI 足夠強後：

$$
C_P
$$

將成為總研究成本主項。

---

## IEF-H3：Proxy Debt Hypothesis

依賴 proxy 越多而缺乏 target validation，

false confidence risk：

$$
\uparrow.
$$

---

## IEF-H4：Simulation Saturation Hypothesis

存在：

$$
C^{*}_{\mathrm{compute}},
$$

使：

$$
C>C^{*}
$$

後，

額外 simulation 的 epistemic gain：

$$
\rightarrow0.
$$

---

## IEF-H5：Claim-Specific Floor Hypothesis

同一理論不同 claims 的：

$$
E_{\min}
$$

可顯著不同。

---

## IEF-H6：Time-Depth Non-Substitutability

對 trajectory claim，

sample width 增長不能完全替代：

$$
\text{temporal depth}.
$$

---

# 146. 最小 PTE-06 實驗設計

選四類 claims：

```text
formal
software
physical engineering
longitudinal
```

---

## 146.1 對每個 claim

建立：

```text
required evidence
current evidence
AI-compressible steps
non-compressible steps
simulation saturation
proxy debt
time floor
```

---

# 147. 比較不同 AI 能力

測：

$$
L_{\mathrm{processing}}
$$

下降多少。

---

# 148. 同時測

$$
L_{\mathrm{floor}}
$$

是否真的下降。

---

# 149. 預期

軟體：

$$
L_{\mathrm{floor}}\approx0.
$$

長期實證：

$$
L_{\mathrm{floor}}\gg0.
$$

---

# 150. 最小 Evidence Floor Receipt

```text
claim_id
domain
claim_type
required_evidence_level
current_evidence_level
processing_complete
proxy_only
simulation_gap
physical_required
longitudinal_required
minimum_wait
ethical_limit
legal_limit
status
next_action
```

---

# 151. PTE-06 的核心公式

第一：

$$
\boxed{
E_{\min}(T,D)
}
$$

第二：

$$
\boxed{
L_{\mathrm{total}}
\ge
L_{\mathrm{floor}}(T,D)
}
$$

第三：

$$
\boxed{
\text{Evidence Processing}
\neq
\text{Evidence Generation}.
}
$$

第四：

$$
\boxed{
\text{More Simulation}
\not\Rightarrow
\text{Target Validation}.
}
$$

---

# 152. 與 PTE-01 的關係

PTE-01 問：

> 如果理論是真的，什麼可觀測結果應出現？

PTE-06 再問：

> 這個結果能靠計算得到，還是必須等世界產生？

---

# 153. 與 PTE-02 的關係

PTE-02 的：

$$
L_P
$$

在本文被展開成：

$$
E_{\min}
$$

與：

$$
L_{\mathrm{floor}}.
$$

---

# 154. 與 PTE-03 的關係

Matched reconstruction 只能在：

$$
\text{available evidence surface}
$$

上比較。

---

# 155. 與 PTE-04 的關係

若 evidence level 不足，

claim 應：

$$
\text{UNRESOLVED}
$$

或：

$$
\text{PROXY\_ONLY}.
$$

---

# 156. 與 PTE-05 的關係

PTE-TSR 必須能輸出：

```text
WAITING_FOR_WORLD
```

而不是永遠繼續計算。

---

# 157. 科學未來的真正瓶頸可能轉移

當：

$$
C_U,
C_F,
C_I,
C_B,
C_A
\downarrow,
$$

真正稀缺資源可能變成：

- physical experiment slots；
- human participants；
- rare events；
- longitudinal time；
- trusted sensors；
- lawful data access。

---

# 158. 這會改變科研資源配置

AI 算力未必永遠是最主要瓶頸。

---

# 159. Future Science Infrastructure

可能更需要：

- automated labs；
- sensor networks；
- long-term data trusts；
- continuous cohorts；
- shared hardware testbeds；
- reproducible field deployments。

---

# 160. AI 把問題推到世界接口

也就是：

$$
\boxed{
\text{AI-rich science}
\rightarrow
\text{evidence-interface bottleneck}.
}
$$

---

# 161. 理論太多，世界實驗有限

若 AI 每天產生：

$$
10^6
$$

個可測假說，

但 physical lab 只能測：

$$
10^2,
$$

那真正問題變成：

$$
\boxed{
\text{experiment allocation}.
}
$$

---

# 162. 所以 Evidence Triage 更重要

選擇：

$$
x^{*}
=
\arg\max
\frac{
\text{expected epistemic value}
}{
\text{physical cost}
}.
$$

---

# 163. 這接 PTE-07

未來 Theory Tournament 最後的稀缺資源，

不是文字，

可能是：

$$
\boxed{
\text{world access}.
}
$$

---

# 164. 結論：AI 可以讓我們更快走到世界面前，但不能替世界回答

PTE 前五篇容易帶來一種誘惑：

> 既然理論能在幾小時內被讀懂、實作、建 baseline、跑反例，那科學驗證是不是也能全面進入小時級？

PTE-06 的答案是：

$$
\boxed{
\text{No, not universally}.
}
$$

更精確地說：

AI 可以大幅壓縮：

$$
\boxed{
\text{epistemic processing latency}.
}
$$

但對某些主張，

真正剩下的是：

$$
\boxed{
\text{evidence generation latency}.
}
$$

當研究已經知道：

- 要測什麼；
- 怎麼測；
- 哪個 baseline；
- 哪個 metric；
- 哪個反例；

但 target evidence 尚未出現時，

繼續增加：

- Agent；
- token；
- simulation；
- debate；

不一定再增加知識。

此時科學上最正確的狀態可能只是：

$$
\boxed{
\text{WAITING FOR WORLD}.
}
$$

這不是 AI 不夠強。

而是：

$$
\boxed{
\text{真實證據本身就是世界狀態的一部分}.
}
$$

PTE 成熟的標誌，不是它能快速為所有理論給出答案。

而是它能精確知道：

> **哪些問題現在可以算完，哪些問題現在只能準備好，然後等待世界。**

---

# 165. 下一篇

**PTE-07｜理論競賽與不可約殘差：AI 時代的假說市場**  
*Theory Tournaments and Irreducible Residues: Toward AI-Native Markets of Hypotheses*

最終篇將整合：

$$
\mathsf{Assume}^{+}(T),
$$

$$
L_{TE},
$$

$$
B^{*}(T),
$$

$$
R_{\mathcal B,\mathcal E}(T),
$$

$$
E_{\min}(T,D),
$$

建立多理論競賽框架：

$$
\boxed{
\mathcal T
=
\{T_1,\ldots,T_n\}
}
$$

並回答：

> **當 AI 可以快速替每個理論建立最強版本、實作、baseline、反例與 residue，而真正昂貴的只剩部分外部證據時，我們應該如何把稀缺研究資源分配給最值得繼續存活的假說？**
