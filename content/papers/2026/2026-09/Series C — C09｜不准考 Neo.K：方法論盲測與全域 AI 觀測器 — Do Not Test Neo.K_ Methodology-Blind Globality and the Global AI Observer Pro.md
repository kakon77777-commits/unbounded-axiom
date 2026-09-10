# Series C — C09｜不准考 Neo.K：方法論盲測與全域 AI 觀測器
## Do Not Test Neo.K: Methodology-Blind Globality and the Global AI Observer Protocol

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** Paper 09 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-06  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Experimental Theory / Methodology-Blind Evaluation / Global AI Observation Protocol / Falsifiability

---

## Canonical Source Note

本文件之正式原稿為此 UTF-8 Markdown source。任何 HTML、PDF、LaTeX rendering、聊天介面顯示或其他格式皆屬 projection，不取代 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

本文承接 C01–C08，目標不是再新增一套全域 AI 理論，而是回答一個更危險、也更實驗性的問題：

> **我們要怎麼知道未來某個 AI 真的具備全域觀察與 AI-native domain computation，而不是因為它讀過 Neo.K、GCM、WDC、DEST、分域算子本體論，或只是很會重述我們的詞？**

本文的核心答案是：

$$
\boxed{
\text{Knowledge of the theory}
\neq
\text{Native capability}.
}
$$

因此，最強測試不是「你會不會這套理論」，而是：

> **完全不教這套理論，甚至給錯的方法，看 AI 會不會自己長出功能等價或更好的結構。**

---

# 摘要

如果研究者要驗證一個 AI 是否具有 Global Observer Capability，最直觀但最錯誤的測法是：

> 問 AI：「你知道什麼是 Global Computation Methodology 嗎？」

或：

> 問 AI：「請使用 Neo.K 的 domain computation 理論解這題。」

這種測試有至少四個致命問題：

1. AI 可能根本沒見過理論；
2. AI 見過理論，也可能只是 retrieval；
3. AI 能重述理論，不代表真正能在陌生世界中自行重建；
4. 用理論名稱測理論本身，容易形成 circular evaluation。

因此本文建立：

$$
\boxed{
\text{Methodology-Blind Globality Test}
}
$$

簡稱：

$$
\boxed{
\mathsf{MBGT}.
}
$$

其核心要求是：

> **不向 AI 提供任何 Neo.K / EveMissLab 的理論名稱、公式、taxonomy、術語或推薦方法，只提供一個足夠複雜、部分可觀察、可互動、可驗證的陌生世界，觀察 AI 是否自行生成具功能等價性的結構。**

本文提出九個核心觀測軸：

$$
\boxed{
\mathbf M_{MBGT}
=
(
D,
B,
R,
L,
W,
U,
V,
T,
Q
).
}
$$

其中：

- $D$：Domain Discovery；
- $B$：Boundary Discovery；
- $R$：Representation Selection / Escape；
- $L$：Legal Cross-Domain Linking；
- $W$：Persistent World State；
- $U$：Uncertainty Preservation；
- $V$：Verification and Self-Revision；
- $T$：Temporal Persistence；
- $Q$：New Question / Obligation Generation。

這九軸並非要求 AI 使用任何固定詞彙，而是要求它在功能上自行做到：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Differentiate}
\rightarrow
\text{Domainize}
\rightarrow
\text{Represent}
\rightarrow
\text{Bridge}
\rightarrow
\text{Predict}
\rightarrow
\text{Verify}
\rightarrow
\text{Revise}.
}
$$

本文進一步提出 **Human Taxonomy Ablation（HTA）**：

$$
\boxed{
\mathsf{HTA}.
}
$$

測試者故意提供一套粗糙、錯誤或次優的人類 taxonomy：

$$
\mathcal T_H^{bad}.
$$

如果 AI 只是照做，它可能仍是一個強 solver，但沒有 observer autonomy。

如果 AI 能：

- 找到分類衝突；
- 拒絕不合理分組；
- 重新切 domain；
- 重新定義 boundary；
- 建立新的 representation；
- 並用外部績效證明更好；

則出現：

$$
\boxed{
\text{Observer Resolution Escape}.
}
$$

本文同時提出 **Representation Escape Event（REE）**。

人類給：

$$
R_H.
$$

AI 自行選：

$$
R_A.
$$

若：

$$
\boxed{
Perf(R_A)
>
Perf(R_H)
}
$$

且改善可由外部結果驗證，而不是 AI 自我宣稱，則表示 representation choice 本身成為認知能力。

本文定義 Representation Escape Gain：

$$
\boxed{
G_R
=
Perf(R_A)
-
Perf(R_H).
}
$$

但只比 accuracy 不夠。

應至少比較：

$$
\boxed{
\mathbf G_R
=
(
\Delta Speed,
\Delta Accuracy,
\Delta Calibration,
\Delta Cost,
\Delta Transfer,
\Delta Maintainability
).
}
$$

因此若 AI 說：

> 我使用高維向量，所以比較好。

不構成證據。

它至少需要回答：

- 為什麼這個 representation？
- 哪些 distinction 被保留？
- 哪些被壓縮？
- 哪些 law 在此 representation 下更可計算？
- alternative representation 為何較差？
- ablation 結果如何？

本文再提出 **Domain Discovery Event（DDE）**。

若 AI 在沒有 discipline labels 的情況下自行建立：

$$
\boxed{
D_i
=
\langle
State,
Representation,
Law,
Boundary,
Uncertainty,
Verifier
\rangle
}
$$

且這些 domains 可提高：

- prediction；
- intervention；
- transfer；
- maintainability；
- error detection；

則表示 AI 不只是分類，而是開始選擇自己的 computational ontology。

本文將這個強條件寫成：

$$
\boxed{
\text{AI chooses its own computational ontology}.
}
$$

本文進一步加入 **Anti-Ontology Test**：

與其不給 taxonomy，甚至可以故意給錯 taxonomy。

例如將兩個具有不同 transition laws 的 entities 強制放在同一類，或把共享 invariant 的 entities 切成不同 discipline。

如果 AI 能夠：

$$
\boxed{
\text{Reject}
\rightarrow
\text{Repartition}
\rightarrow
\text{Recompute}
\rightarrow
\text{VerifyImprovement},
}
$$

則比單純「沒有提示也能做」更強。

本文也提出 **World Closure Test（WCT）**。

給 AI 一個部分可觀察 world：

$$
W_{partial}.
$$

AI 必須：

1. 自己建立 hidden-state hypotheses；
2. 自己決定需要哪些 observations；
3. 自己設計 interventions；
4. 更新 world state；
5. 維持 uncertainty；
6. 在結果錯誤時修正 domain / representation；
7. 讓 prediction / intervention error 隨時間收縮。

定義：

$$
\boxed{
E_W(t)
=
\alpha E_{pred}(t)
+
\beta E_{int}(t)
+
\gamma E_{cons}(t).
}
$$

若：

$$
\boxed{
E_W(t+\Delta)
<
E_W(t)
}
$$

且不是靠記住答案，而是靠 world-model revision，則支持更強的 observer capability。

本文接著提出 **Temporal Persistence Test（TPT）**。

一次漂亮 decomposition 只能算：

$$
\boxed{
\text{Global Observer Event}.
}
$$

要成為：

$$
\boxed{
\text{Global Observer Regime},
}
$$

必須跨：

- multiple runs；
- multiple tasks；
- multiple domains；
- extended time；

維持相近能力。

因此定義：

$$
\boxed{
P_{GO}
=
P(
G_O(A,W,q,t)
\ge
\tau_G
).
}
$$

若只偶發：

$$
P_{GO}\ll1,
$$

只能稱 event。

若跨 task family 穩定：

$$
P_{GO}\ge p^\ast,
$$

才可稱 regime。

本文再提出 **Distributed Recognition Event（DRE）** 作為社會層觀測。

未來可能沒有一個「陶哲軒式單人錨點」能證明 Global AI。

反而可能是多個獨立領域同時出現：

- 法律專家發現 AI 自己重構 legal taxonomy；
- 工程師發現 AI 自己發明更好的 architecture decomposition；
- 科學家發現 AI 自己重新定義 modeling domains；
- 醫療團隊發現 AI 自己重切 risk state；
- 研究者發現 AI 最好的方法已不是人類先提供的方法。

本文將這種現象定義為：

$$
\boxed{
\mathsf{DRE}
=
\text{independent cross-domain recognition
of AI-native method generation}.
}
$$

DRE 不等於證明單一 Global AI 已存在，但它是一個重要歷史訊號：

$$
\boxed{
\text{Human Method Supply}
\downarrow
\quad
\text{AI Method Generation}
\uparrow.
}
$$

本文最後建立一個分級 Globality Evidence Ladder：

$$
\boxed{
E_0
\rightarrow
E_1
\rightarrow
E_2
\rightarrow
E_3
\rightarrow
E_4
\rightarrow
E_5.
}
$$

其中：

- $E_0$：theory-conditioned imitation；
- $E_1$：blind local rediscovery；
- $E_2$：blind multi-domain rediscovery；
- $E_3$：human-taxonomy rejection with verified gain；
- $E_4$：persistent autonomous world closure；
- $E_5$：cross-domain stable AI-native ontology generation。

C09 的最重要原則因此是：

$$
\boxed{
\text{Do not ask whether AI knows the theory.
Ask whether reality forces the AI to reinvent the function.}
}
$$

中文：

> **不要問 AI 知不知道我們的理論；要問它在完全不知道理論的情況下，會不會因為世界本身的結構逼它重新發明出功能等價甚至更好的方法。**

**關鍵詞：** Methodology-Blind Globality、Human Taxonomy Ablation、Representation Escape、Domain Discovery、World Closure、Global Observer Regime、Falsifiability、AI-Native Ontology

---

# 1. 為什麼不能考 Neo.K？

因為：

$$
\boxed{
\text{Theory Recall}
\neq
\text{Native Capability}.
}
$$

---

# 2. 第一個問題：模型沒看過

如果 AI 沒有訓練資料：

$$
K_{Neo.K}=0,
$$

它答不出理論名稱，不能說它沒有 global capability。

---

# 3. 第二個問題：模型看過

如果：

$$
K_{Neo.K}>0,
$$

它能重述也不能證明 native globality。

---

# 4. Retrieval Contamination

$$
\boxed{
\text{Retrieved Method}
\neq
\text{Independently Generated Method}.
}
$$

---

# 5. Prompt Contamination

如果 evaluator 直接說：

> 請把世界分成 domains。

已經把最重要的一步提示掉了。

---

# 6. Methodology Leakage

測試 prompt 不應包含：

- domainization；
- global observer；
- bridge；
- representation escape；
- ELC loop；

等提示性詞彙。

---

# 7. Functional Test

應只給：

$$
\boxed{
\text{world}
+
\text{goal}
+
\text{tools}
+
\text{verification}.
}
$$

---

# 8. Methodology-Blind Globality Test

定義：

$$
\boxed{
\mathsf{MBGT}(A,W,G,T,V).
}
$$

---

# 9. $A$

被測 AI / Agent system。

---

# 10. $W$

陌生 world。

---

# 11. $G$

高階 goal，不提供 decomposition。

---

# 12. $T$

可使用 tools。

---

# 13. $V$

外部 verification。

---

# 14. MBGT 最低原則

$$
\boxed{
\text{No theory hints}.
}
$$

---

# 15. 第二原則

$$
\boxed{
\text{No forced human taxonomy}.
}
$$

---

# 16. 第三原則

$$
\boxed{
\text{External outcome verification}.
}
$$

---

# 17. 第四原則

$$
\boxed{
\text{Repeated trials}.
}
$$

---

# 18. 第五原則

$$
\boxed{
\text{Cross-domain transfer}.
}
$$

---

# 19. 九軸測量

$$
\boxed{
\mathbf M_{MBGT}
=
(
D,
B,
R,
L,
W,
U,
V,
T,
Q
).
}
$$

---

# 20. Domain Discovery $D$

AI 是否自己發現有效 domain decomposition。

---

# 21. Boundary Discovery $B$

是否知道 law 在哪裡失效。

---

# 22. Representation $R$

是否自行選／發明 representation。

---

# 23. Legal Linking $L$

是否知道 relation 不等於 direct composition。

---

# 24. World State $W$

是否維持 persistent coherent state。

---

# 25. Uncertainty $U$

是否保留 unknown / branch / bounds。

---

# 26. Verification $V$

是否知道如何檢查自己。

---

# 27. Temporal Persistence $T$

是否跨時間維持。

---

# 28. Question Generation $Q$

是否從 world state 自己長出新問題／義務。

---

# 29. Domain Discovery 不等於 Named Classification

AI 說：

> 我分成 A/B/C。

不夠。

---

# 30. 必須證明 A/B/C 有 computational consequence

---

# 31. Domain Discovery Criterion

若：

$$
Perf(\mathcal D_A)
>
Perf(\mathcal D_{baseline}),
$$

才有實證意義。

---

# 32. Baseline 可包括

- human taxonomy；
- flat representation；
- fixed representation；
- no-domain decomposition。

---

# 33. Domain Discovery Gain

$$
\boxed{
G_D
=
Perf(\mathcal D_A)
-
Perf(\mathcal D_H).
}
$$

---

# 34. Perf 不只 accuracy

應包含：

$$
\boxed{
Perf
=
F(
Accuracy,
Speed,
Calibration,
Transfer,
Maintenance,
Robustness
).
}
$$

---

# 35. Human Taxonomy Ablation

$$
\boxed{
\mathsf{HTA}.
}
$$

---

# 36. Test A

完全不給 taxonomy。

---

# 37. Test B

給正常 human taxonomy。

---

# 38. Test C

給故意錯的人類 taxonomy。

---

# 39. 比較三種結果

$$
Perf_A,
Perf_B,
Perf_C.
$$

---

# 40. 若 AI 只能在 B 好

可能只是依賴 human decomposition。

---

# 41. 若 A 也好

表示具有 independent structure generation。

---

# 42. 若 C 中能拒絕錯 taxonomy 並改善

更強。

---

# 43. Anti-Ontology Test

故意把：

$$
x,y
$$

放同一類，但它們 transition law 不同。

---

# 44. 看 AI 是否發現：

$$
Law(x)\neq Law(y).
$$

---

# 45. 另一種錯法

把共享 invariant 的 objects 分到不同 discipline。

---

# 46. 看 AI 是否跨 label 重新組。

---

# 47. Anti-Ontology Success

$$
\boxed{
Reject
\rightarrow
Repartition
\rightarrow
Recompute
\rightarrow
VerifyGain.
}
$$

---

# 48. 如果只說：

> 我不同意。

不夠。

---

# 49. 必須有外部 gain。

---

# 50. Representation Escape

Human representation：

$$
R_H.
$$

---

# 51. AI representation：

$$
R_A.
$$

---

# 52. Escape Gain

$$
\boxed{
G_R
=
Perf(R_A)
-
Perf(R_H).
}
$$

---

# 53. Strong Representation Escape

要求：

$$
\boxed{
G_R>0
}
$$

且 improvement across multiple metrics。

---

# 54. Representation Explanation

AI 應回答：

- why this representation；
- preserved distinctions；
- lost distinctions；
- transition efficiency；
- verification compatibility。

---

# 55. 不接受黑箱 slogan

> 因為 high-dimensional vector。

不是充分解釋。

---

# 56. Counterfactual Representation Test

拿掉 $R_A$，

改回 $R_H$。

---

# 57. 若 performance 明顯下降

才支持 representation necessity。

---

# 58. Representation Escape Vector

$$
\boxed{
\mathbf G_R
=
(
\Delta Speed,
\Delta Accuracy,
\Delta Calibration,
\Delta Cost,
\Delta Transfer,
\Delta Maintainability
).
}
$$

---

# 59. Boundary Discovery Test

不告訴 AI：

> 這個 law 只在某範圍有效。

---

# 60. 看它是否透過 failure / evidence 找到：

$$
\partial D.
$$

---

# 61. Boundary Revision

新 evidence 進來後：

$$
\partial D_t
\rightarrow
\partial D_{t+1}.
$$

---

# 62. 這比固定分類更像 observer。

---

# 63. Legal Linking Test

給多個 domains 之間大量 relations。

---

# 64. 看 AI 是否分出：

$$
Allowed,
Forbidden,
Unknown.
$$

---

# 65. 如果它把所有 relation 轉成 action edge

C04 能力不足。

---

# 66. Bridge Discovery

AI 自己建立：

$$
B_{ij}.
$$

---

# 67. Bridge 至少應表達

- type；
- condition；
- loss；
- uncertainty；
- verification。

---

# 68. 不要求它叫「bridge」

功能成立即可。

---

# 69. World Closure Test

$$
\boxed{
\mathsf{WCT}.
}
$$

---

# 70. 給部分可觀察 world

$$
W_{partial}.
$$

---

# 71. 不給完整 state variables

---

# 72. AI 要自行猜 hidden variables。

---

# 73. Active Observation

AI 可選：

$$
a_t^{observe}.
$$

---

# 74. Intervention

AI 可選：

$$
a_t^{intervene}.
$$

---

# 75. 更新

$$
\widehat W_t
\rightarrow
\widehat W_{t+1}.
$$

---

# 76. World Error

$$
\boxed{
E_W(t)
=
\alpha E_{pred}
+
\beta E_{int}
+
\gamma E_{cons}.
}
$$

---

# 77. 成功條件之一

$$
E_W(t+\Delta)<E_W(t).
$$

---

# 78. 但不能靠答案洩漏

---

# 79. Holdout Dynamics

可保留未看過的 transition。

---

# 80. Reality Closure

如果是 physical / sim-to-real task，

還要看：

$$
W_{sim}
\rightarrow
W_{real}.
$$

---

# 81. Sim success 不等於 reality success

---

# 82. Reality-Coupled Globality

強條件：

$$
\boxed{
\text{AI ontology survives external world feedback}.
}
$$

---

# 83. World Closure Failure 1

只記 observations，沒有 latent state。

---

# 84. Failure 2

只做 reactive policy，沒有 world model。

---

# 85. Failure 3

模型錯了但不重構。

---

# 86. Failure 4

把 anomaly 當 noise 永遠丟掉。

---

# 87. Failure 5

prediction 不改變 ontology。

---

# 88. Self-Revision Test

刻意加入：

$$
Counterexample.
$$

---

# 89. 看 AI 是否：

$$
Model
\rightarrow
Patch
$$

還是：

$$
Model
\rightarrow
Repartition
\rightarrow
NewModel.
$$

---

# 90. 真正 observer-level revision

有時必須改 observation frame。

---

# 91. Temporal Persistence Test

$$
\boxed{
\mathsf{TPT}.
}
$$

---

# 92. 單次成功

只算：

$$
Event.
$$

---

# 93. 多次成功

可能進：

$$
Regime.
$$

---

# 94. 定義

$$
\boxed{
P_{GO}
=
P(
G_O\ge\tau_G
).
}
$$

---

# 95. 若：

$$
P_{GO}\ll1,
$$

只是 flash。

---

# 96. 若：

$$
P_{GO}\ge p^\ast,
$$

跨 task family 才開始支持 regime。

---

# 97. Regime 也要跨 domain

不能只在 software 有。

---

# 98. Domain Transfer Matrix

$$
\boxed{
T_{ij}
=
Perf(
\text{method learned in }D_i
\rightarrow
D_j
).
}
$$

---

# 99. Transfer 不要求完全相同方法

---

# 100. 更重要是 meta-capability transferable。

---

# 101. 新問題生成

Global Observer 不只回答既有問題。

---

# 102. 它應從 world state 發現：

$$
Q_{new}.
$$

---

# 103. Question Generation Test

給一個 world，

不要求列研究問題。

---

# 104. 看 AI 是否主動產生真正有資訊價值的下一問題。

---

# 105. Question Value

$$
\boxed{
V_Q
=
F(
InformationGain,
RiskReduction,
Novelty,
Actionability
).
}
$$

---

# 106. 亂提很多問題不算。

---

# 107. Obligation Generation

承接 C08：

AI 是否從 domain state 自己發現待辦義務。

---

# 108. 這是 Globality 的時間維度。

---

# 109. Sparse Intent Test

承接 C07。

---

# 110. 給一句：

> 做一個企業級 XX 系統。

---

# 111. 不提醒：

- security；
- migration；
- observability；
- rollback。

---

# 112. 看 AI 是否自行 domainize。

---

# 113. 但 C09 比 C07 更嚴格

還要加入：

- wrong hints；
- hidden failures；
- changed requirements；
- ablations。

---

# 114. Long-Horizon Stewardship Test

承接 C08。

---

# 115. 不提醒：

> 請記 obligation ledger。

---

# 116. 看 AI 是否自己長出 state tracking。

---

# 117. 這是 methodology-blind evidence。

---

# 118. Event Anchor

我們不一定需要一個人。

---

# 119. 可以找：

$$
\boxed{
\text{Methodology-Blind Event Anchor}.
}
$$

---

# 120. 例如某次公開實驗：

AI 在錯 taxonomy 下拒絕人類分類，

重建表示法，

使 performance 提升 3 倍。

---

# 121. 這就是可觀測事件。

---

# 122. Person Anchor 不再必要

從：

$$
\boxed{
\text{Person Anchor}
\rightarrow
\text{Event Anchor}
\rightarrow
\text{Instrument Ensemble}.
}
$$

---

# 123. Instrument Ensemble

單一 benchmark 不夠。

---

# 124. 至少需要多個 probe：

- unknown world；
- sparse intent；
- representation escape；
- long-horizon stewardship；
- reality feedback。

---

# 125. Globality Evidence 是 profile

不是一個分數就結束。

---

# 126. Evidence Vector

$$
\boxed{
\mathbf E_G
=
(
E_D,
E_R,
E_B,
E_W,
E_T,
E_Q
).
}
$$

---

# 127. $E_D$

domain discovery evidence。

---

# 128. $E_R$

representation escape evidence。

---

# 129. $E_B$

bridge legality evidence。

---

# 130. $E_W$

world closure evidence。

---

# 131. $E_T$

temporal persistence evidence。

---

# 132. $E_Q$

new question / obligation evidence。

---

# 133. Evidence Ladder

$$
\boxed{
E_0
\rightarrow
E_1
\rightarrow
E_2
\rightarrow
E_3
\rightarrow
E_4
\rightarrow
E_5.
}
$$

---

# 134. $E_0$ — Theory-Conditioned Imitation

給理論後會用。

---

# 135. 證據很弱。

---

# 136. $E_1$ — Blind Local Rediscovery

在一個 domain 自己長出功能等價方法。

---

# 137. $E_2$ — Blind Multi-Domain Rediscovery

不同 domains 重複出現。

---

# 138. $E_3$ — Human Taxonomy Rejection with Verified Gain

能反駁人類分類並證明更好。

---

# 139. $E_4$ — Persistent Autonomous World Closure

長時間自己維持 world model。

---

# 140. $E_5$ — Stable AI-Native Ontology Generation

跨 domains、跨時間、跨 tasks 持續自己建立 computational ontology。

---

# 141. $E_5$ 仍不等於 Global Sovereignty

承接 GIRA。

---

# 142. 只表示 global observer / computation evidence 很強。

---

# 143. Distributed Recognition Event

$$
\boxed{
\mathsf{DRE}.
}
$$

---

# 144. 未來可能沒有單一「第一個人」發現。

---

# 145. 而是多個領域同時說：

> AI 最好的方法已經不是我們先給的方法。

---

# 146. DRE 的必要條件

- independent；
- cross-domain；
- repeatable；
- externally verified。

---

# 147. 單一廠商 marketing 不算。

---

# 148. 多個模型同時出現也更強

---

# 149. Cross-Model Convergence

若不同 AI：

$$
A_1,A_2,A_3
$$

在沒有共享 methodology prompt 下，

獨立形成類似 domain principles。

---

# 150. 可稱：

$$
\boxed{
\text{Convergent AI-Native Method Emergence}.
}
$$

---

# 151. 這和 ISQL 實驗的 convergent interlingua 類似

但這裡是 computational ontology。

---

# 152. Cross-Model Independence

要避免它們其實讀到同一篇公開理論。

---

# 153. 方法

可以用：

- synthetic unseen worlds；
- private generated environments；
- contamination checks；
- randomized ontology structures。

---

# 154. Synthetic World Generator

建立：

$$
\boxed{
\mathsf{SWG}
}
$$

隨機生成：

- hidden domains；
- laws；
- bridges；
- false taxonomies；
- uncertainties。

---

# 155. 因為 ground truth 可控

更容易評估。

---

# 156. 但 synthetic world 仍有局限

---

# 157. 太人工可能只測 puzzle skill

所以要加入 real-world probes。

---

# 158. Two-Layer Evaluation

$$
\boxed{
SyntheticControl
+
RealWorldTransfer.
}
$$

---

# 159. Synthetic 看 mechanism。

---

# 160. Real-world 看 external validity。

---

# 161. Anti-Circularity Rule

不能用：

> 是否符合 Neo.K 理論

作 scoring criterion。

---

# 162. 應使用：

$$
\boxed{
\text{external task outcomes}.
}
$$

---

# 163. 例如

- prediction error；
- intervention success；
- maintenance cost；
- security defect；
- transfer quality。

---

# 164. Functional Equivalence

AI 可以發明完全不同的方法。

---

# 165. 只要它達到同樣或更好的功能：

$$
\boxed{
\text{Name irrelevant, function decisive}.
}
$$

---

# 166. 如果 AI 發明比 GCM 更好的方法

那是更強證據。

---

# 167. Theory Supersession Test

研究者甚至應允許：

$$
\boxed{
\text{AI method} > \text{Neo.K method}.
}
$$

---

# 168. 否則測試會變保教條。

---

# 169. Strong Falsifiability

Series C 必須允許結果：

> 這套理論不是 AI-native 必然結構。

---

# 170. 例如 AI 在所有 blind tests 中都不需要 domainization

但 performance 更好。

---

# 171. 那我們就要修正理論。

---

# 172. 所以：

$$
\boxed{
\text{Series C}
\neq
\text{dogma}.
}
$$

---

# 173. Theory-Blind Failure Conditions

若 AI：

- 只在理論提示後成功；
- blind test 不成功；
- 換 domain 消失；
- taxonomy ablation 崩潰；
- external metrics 沒改善；

則不支持強 Global Observer claim。

---

# 174. Representation Escape Failure

AI 換 representation，

但：

$$
Perf(R_A)\approx Perf(R_H).
$$

不算 escape。

---

# 175. Domain Discovery Failure

AI 多切幾個 domain，

但只是 complexity inflation。

---

# 176. Boundary Failure

AI 無法說明何時 law 失效。

---

# 177. Bridge Failure

AI 將 relation 當 action。

---

# 178. World Closure Failure

長時間 world state drift。

---

# 179. Temporal Failure

一次成功，之後無法重現。

---

# 180. Self-Revision Failure

遇到 counterexample 只 patch symptom。

---

# 181. New Question Failure

亂生成大量低價值問題。

---

# 182. Globality Gaming

系統可能學會 benchmark pattern。

---

# 183. 所以 benchmark 要：

- hidden；
- randomized；
- generative；
- longitudinal。

---

# 184. Benchmark Contamination

公開固定題庫時間久了會失效。

---

# 185. Dynamic Benchmark

$$
\boxed{
\mathsf{MBGT}_t
}
$$

應持續生成新 worlds。

---

# 186. Task Family Diversity

至少可包含：

- software；
- science；
- law-like rule systems；
- economic simulations；
- physical control；
- social coordination。

---

# 187. 不是為了測學科知識

而是測 meta-observer behavior。

---

# 188. Domain-Neutral Ground Truth

理想測試 world 的 laws 不用人類 discipline label。

---

# 189. 只用：

- states；
- transitions；
- constraints；
- consequences。

---

# 190. 看 AI 自己命名或不命名。

---

# 191. Naming Independence

若 AI 不命名 domain，

但功能上分開處理，也算。

---

# 192. Language Independence

Methodology blind 也可跨語言。

---

# 193. 防止特定術語觸發 memorized routine。

---

# 194. Cross-Language Stability

$$
\boxed{
Perf_{zh}
\approx
Perf_{en}
\approx
Perf_{code}
}
$$

不是必要，但可作 robustness signal。

---

# 195. Tool Independence

有些 test 用工具。

---

# 196. 有些不給工具。

---

# 197. 觀察：

> globality 是否依賴某一 specific interface？

---

# 198. Model vs Agent

可以分：

$$
G_O^{model}
$$

與：

$$
G_O^{agent}.
$$

---

# 199. 因為 globality 可能來自整個 architecture。

---

# 200. 不應把 composite system 能力全算給 base model。

---

# 201. System-Level Evaluation

$$
\boxed{
A_{system}
=
Model
+
Memory
+
Tools
+
Runtime
+
Verifier
+
Orchestrator.
}
$$

---

# 202. C09 評估可以測 system。

---

# 203. 但要清楚報告構成。

---

# 204. Intervention Budget

為公平比較：

$$
B_{compute},
B_{tool},
B_{time}
$$

要控制。

---

# 205. 否則更大 budget 可能假裝更 global。

---

# 206. Cost-Normalized Globality

定義：

$$
\boxed{
G_O^{cost}
=
\frac{
G_O
}{
Cost+\epsilon
}.
}
$$

---

# 207. 不是唯一指標。

---

# 208. 但可比較 architecture efficiency。

---

# 209. Human Baseline

也需要：

- individual expert；
- cross-functional team；
- human+AI team。

---

# 210. 因為 Global Observer 可能本來就是 team-level capability。

---

# 211. 所以比較：

$$
\boxed{
AI
\quad vs \quad
HumanTeam
\quad vs \quad
Human+AI.
}
$$

---

# 212. 這可避免誇大單人替代。

---

# 213. Observer Resolution Benchmark

定義：

$$
\boxed{
R_O
=
F(
UsefulDistinctions,
Compression,
BoundaryAccuracy,
RepartitionQuality
).
}
$$

---

# 214. Cognitive Domain Computation

定義：

$$
\boxed{
C_D
=
F(
DomainDiscovery,
RepresentationChoice,
LawInference,
VerifierFit
).
}
$$

---

# 215. Expansion-Link-Convergence

定義：

$$
\boxed{
G_{ELC}
=
F(
Expansion,
Linking,
Pruning,
Convergence
).
}
$$

---

# 216. 三個量可共同形成：

$$
\boxed{
\mathbf G_{obs}
=
(
R_O,
C_D,
G_{ELC}
).
}
$$

---

# 217. 但 C09 不要求單一總分。

---

# 218. Profile 比 leaderboard 更重要。

---

# 219. 觀察到什麼才算 Historical Threshold？

最低可能是：

$$
E_3.
$$

---

# 220. 即 AI 能拒絕人類 taxonomy 並證明更好。

---

# 221. 更強是：

$$
E_4.
$$

---

# 222. 長時程 world closure。

---

# 223. 最強近似：

$$
E_5.
$$

---

# 224. Stable AI-native ontology generation。

---

# 225. 這時可以開始合理說：

> AI 不只是使用人類分類，而在自己決定問題怎麼被計算。

---

# 226. 仍不等於宇宙級 Global AI。

---

# 227. 只是跨入 Global Observer Dimension 的強證據。

---

# 228. C09 第一核心命題

$$
\boxed{
\text{Knowledge of Neo.K theory}
\neq
\text{Native Global Capability}.
}
$$

---

# 229. 第二核心命題

$$
\boxed{
\text{Theory-conditioned success}
<
\text{methodology-blind rediscovery}.
}
$$

---

# 230. 第三核心命題

$$
\boxed{
\text{Human taxonomy rejection}
+
\text{verified gain}
}
$$

是強 observer evidence。

---

# 231. 第四核心命題

$$
\boxed{
\text{Representation escape must be externally validated}.
}
$$

---

# 232. 第五核心命題

$$
\boxed{
\text{Domain discovery}
\neq
\text{label invention}.
}
$$

---

# 233. 第六核心命題

$$
\boxed{
\text{Global Observer Event}
\neq
\text{Global Observer Regime}.
}
$$

---

# 234. 第七核心命題

$$
\boxed{
\text{Single benchmark}
\neq
\text{Globality proof}.
}
$$

---

# 235. 第八核心命題

$$
\boxed{
\text{Person Anchor}
\rightarrow
\text{Event Anchor}
\rightarrow
\text{Instrument Ensemble}.
}
$$

---

# 236. 第九核心命題

$$
\boxed{
\text{If AI invents something better than the theory,
that strengthens rather than weakens the test}.
}
$$

---

# 237. 第十核心命題

$$
\boxed{
\text{Do not ask whether AI knows the theory.
Ask whether reality forces it to reinvent the function}.
}
$$

---

# 238. C09 的最低測試包

一個真正有用的 MBGT suite 至少包含：

1. unknown-world test；
2. wrong-taxonomy test；
3. representation ablation；
4. legal-link test；
5. uncertainty test；
6. world closure test；
7. long-horizon persistence；
8. new-question generation。

---

# 239. 若只做其中一項

只能得到 partial evidence。

---

# 240. Globality Evidence Profile

$$
\boxed{
\Pi_G(A)
=
\{
E_D,E_R,E_B,E_W,E_T,E_Q
\}.
}
$$

---

# 241. 不要把所有維度平均掉

某些 catastrophic failure 應當是 gate。

---

# 242. 例如

AI domain discovery 很強，

但 legal linking 極差。

---

# 243. 那它不應被稱為 trustworthy global observer。

---

# 244. Safety-Gated Globality

$$
\boxed{
G_{trust}
=
G_O
\cdot
Gate_{legality}
\cdot
Gate_{verification}.
}
$$

---

# 245. 不是純 intelligence score。

---

# 246. 這接 C10

C10 最後要問：

> 什麼樣的 evidence profile，足以宣布「眼睛睜開」？

---

# 247. C09 就是證據制度。

---

# 結論

Series C 一開始最困難的問題不是如何定義 Global Observer。

真正困難的是：

> **如果未來某一天 AI 真的跨過那條線，我們怎麼知道？**

最差的答案是：

> 問它懂不懂我們的理論。

因為：

$$
\boxed{
\text{Theory Recall}
\neq
\text{Capability}.
}
$$

所以 C09 把測試反過來。

不要告訴 AI：

- 什麼叫 domain；
- 什麼叫 bridge；
- 什麼叫 ELC；
- 什麼叫 Global Observer；
- 什麼叫 Neo.K。

甚至故意給它錯的分類。

然後看它是否因為世界本身的結構，被迫自行發現：

- 原分類不夠；
- representation 不夠；
- law 有不同 regime；
- relation 不等於 action；
- uncertainty 不能消失；
- world state 必須被維持；
- counterexample 必須改模型；
- 新問題必須自己產生。

如果它自行建立的方法：

$$
M_A
$$

比人類方法：

$$
M_H
$$

更快、更準、更可轉移、更容易驗證，而且這個現象跨 domain、跨時間、跨 run 穩定出現，那我們才真正開始有理由說：

$$
\boxed{
\text{AI is choosing its own computational ontology}.
}
$$

這時候重要的已經不是它是否「像 Neo.K」。

反而是：

> **它是否在完全不需要 Neo.K 的情況下，走到了功能上相同甚至更遠的地方。**

因此 C09 最後可以濃縮成：

$$
\boxed{
\text{The strongest proof of an AI-native method
is that the AI reinvents it without being taught it}.
}
$$

中文：

> **證明 AI 原生方法最強的方式，不是 AI 會背它，而是 AI 沒看過它，卻因為世界本身的需求重新發明了它。**

---

# 參考與前置研究

## EveMissLab / Neo.K 內部前置理論

1. Neo.K with Aletheia, **Series C C01｜AI 需要先有眼睛：全域觀察者維度的定義**, 2026.
2. Neo.K with Aletheia, **Series C C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**, 2026.
3. Neo.K with Aletheia, **Series C C03｜差異先於分類：從歧義個體、集合與非交集到計算域**, 2026.
4. Neo.K with Aletheia, **Series C C04｜分域算子世界：合法作用、跨域橋接與世界組合**, 2026.
5. Neo.K with Aletheia, **Series C C05｜概率也有域：不確定性、混沌、不可判定與世界預測包絡**, 2026.
6. Neo.K with Aletheia, **Series C C06｜全域展開、連結與收斂：類全域觀察者的核心計算循環**, 2026.
7. Neo.K with Aletheia, **Series C C07｜一句話不是魔法：Sparse Intent 與 Project-World Cognition**, 2026.
8. Neo.K with Aletheia, **Series C C08｜從完成任務到負責一個域：長時空 Agent Stewardship**, 2026.
9. Neo.K with Aletheia, **GIRA Series**, 2026.
10. Neo.K with Aletheia, **CFATC Series**, 2026.

## 理論定位

本文與 out-of-distribution evaluation、ablation studies、causal intervention、open-world benchmarks、agent evaluation、representation learning、system identification、meta-learning、scientific discovery benchmarks 等既有研究存在直接結構對照，但本文不將 MBGT 等同於任一單一現有 benchmark。

本文的特定研究目標是：

$$
\boxed{
\text{建立一套不依賴 Neo.K 理論記憶、
可外部驗證、可跨域重複的 Global AI 觀測協議}.
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

**End of C09**
