# PTE-07｜理論競賽與不可約殘差：AI 時代的假說市場

## Theory Tournaments and Irreducible Residues: Toward AI-Native Markets of Hypotheses

**系列：** 《假設你是對的》／Provisional Truth Engineering Series（PTE）  
**系列文件：** PTE-07 / 07  
**版本：** v0.1  
**日期：** 2026-09-09  
**作者：** Neo.K  
**研究協作：** AI-assisted theoretical development  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 公開方法論論文／AI-native theory tournament、研究資源分配與假說市場  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

Provisional Truth Engineering（PTE）前六篇建立了一條完整的 AI 時代理論壓測方法：

1. PTE-01 以暫時真值算子 $\mathsf{Assume}^{+}(T)$，要求先把理論推到最強可辯護、可檢驗版本；
2. PTE-02 定義 Theory-to-Engineering Latency，分析 AI 如何壓縮理解、形式化、實作與比較成本；
3. PTE-03 以 Matched Reconstruction Principle 區分「有用」與「不可約新原理」；
4. PTE-04 建立 Epistemic Salvage 與不可約殘差 $R_{\mathcal B,\mathcal E}(T)$ ；
5. PTE-05 將前述規則工程化為 AI-native Theory Stress Runtime；
6. PTE-06 引入 Irreducible Evidence Floor，指出 AI 不能把世界本身產生證據所需的時間與物理條件完全消除。

當這六個環節同時存在後，新的問題不再是：

> **AI 能不能幫忙測一套理論？**

而是：

> **當 AI 可以同時壓測成百上千套理論，而真正昂貴的外部實驗、世界存取、專家注意力與長期證據仍然稀缺時，研究資源應該優先給誰？**

本文提出 **Theory Tournament（理論競賽）** 與 **Hypothesis Market（假說市場）**。此處「市場」不是把真理商品化，也不是以人氣、資金或投票決定真假，而是將研究資源視為有限預算，讓理論在同一證據規則下競爭下一輪驗證資格。

設候選理論集合為：

$$
\boxed{
\mathcal T
=
\{T_1,T_2,\ldots,T_n\}.
}
$$

每個理論先接受：

$$
\mathsf{Assume}^{+},
$$

再經：

$$
\text{Formalization}
\rightarrow
\text{Operationalization}
\rightarrow
\text{Implementation}
\rightarrow
\text{Matched Reconstruction}
\rightarrow
\text{Adversarial Challenge}
\rightarrow
\text{Epistemic Salvage}.
$$

得到：

$$
\boxed{
R_i
=
R_{\mathcal B,\mathcal E}(T_i).
}
$$

理論競賽真正比較的，不是原始理論文字量、作者聲望、論文數量、敘事宏大度或 AI 共識，而是：

$$
\boxed{
\text{what survives after strongest known reconstruction}.
}
$$

本文提出 **Residual Research Priority（RRP）**：

$$
\boxed{
RRP(T_i)
=
f(
I_i,
U_i,
X_i,
G_i,
E_i,
C_i,
W_i
)
}
$$

其中：

- $I_i$：潛在影響；
- $U_i$：當前不確定性；
- $X_i$：可檢驗性；
- $G_i$：不可約／區分性殘差；
- $E_i$：預期 epistemic gain；
- $C_i$：下一輪驗證成本；
- $W_i$：world-access requirement。

因此下一輪研究資源不應優先分給「目前講得最大聲」的理論，而應優先分給：

$$
\boxed{
\frac{
\text{Expected Epistemic Gain}
}{
\text{Marginal Research Cost}
}
}
$$

較高，且其殘差能在公平測試中造成高資訊量區分的候選。

本文亦提出 **World Access Allocation（世界存取分配）**。當 PTE-06 所定義的 $E_{\min}(T,D)$ 成為主要瓶頸時，真正稀缺的研究資源可能不再是 token、文字或一般計算，而是：

- 實驗室時段；
- 人體研究；
- 長期 cohort；
- 硬體測試台；
- 現場部署；
- 高可信感測；
- 罕見事件；
- 合法資料存取；
- 專家與第三方 replication。

因此，AI 時代的科學制度可能逐步從：

$$
\boxed{
\text{Publication Competition}
}
$$

轉向：

$$
\boxed{
\text{Evidence Allocation Competition}.
}
$$

本文最後提出：成熟的 Hypothesis Market 不應直接產生「真理排行榜」，而應維護一個動態 **Epistemic Frontier**，其中每套理論都有：

```text
current residue
current strongest baseline
current evidence level
current uncertainty
next distinguishing experiment
world-access debt
reproducibility status
```

理論可以：

- 晉級；
- 降級；
- 暫停；
- 合併；
- 分叉；
- 被重建吸收；
- 等待世界；
- 因新證據重新開啟。

最終目標不是讓一個理論「贏得科學」，而是使整個研究系統持續把資源集中到：

$$
\boxed{
\text{尚未被解釋、但最值得被解釋的地方}.
}
$$

**關鍵詞：** Theory Tournament、Hypothesis Market、Irreducible Residue、Research Allocation、Epistemic Frontier、World Access、Expected Information Gain、AI-Native Science、Matched Reconstruction、Provisional Truth Engineering

---

# 0. 邊界聲明

本文不主張：

- 科學真理可以由市場價格決定；
- 最受歡迎的理論應獲得最多資源；
- AI 可以自動決定所有科研資金配置；
- 單一量化分數足以代表理論價值；
- 研究資源應只分配給短期可測理論；
- 高成本、低可測性理論一定不值得研究；
- theory tournament 可以取代同行評審；
- 競爭一定優於合作；
- 理論之間必須互斥；
- 一個理論落敗後不得重新進場；
- 不可約殘差等於新基本原理；
- 世界證據可以被完全市場化。

本文只研究：

> 當 AI 已能低成本完成大量前置理論壓測，而外部驗證與高品質人類判斷仍有限時，如何建立一個比聲望、文字量與初始敘事更公平的研究資源分配框架。

---

# 1. PTE 系列收斂到哪裡？

整個系列的核心鏈條現在可以寫成：

$$
\boxed{
T
\rightarrow
\mathsf{Assume}^{+}(T)
\rightarrow
F(T)
\rightarrow
O(T)
\rightarrow
I(T)
\rightarrow
B^{*}(T)
\rightarrow
E(T)
\rightarrow
R_{\mathcal B,\mathcal E}(T)
\rightarrow
\text{Next Evidence}.
}
$$

---

# 2. PTE-07 的問題不是「哪個理論是真的？」

而是：

> **在有限研究資源下，下一個最值得取得的證據是什麼？**

---

# 3. 從理論評價轉向研究配置

傳統問題：

$$
\boxed{
\text{Evaluate}(T).
}
$$

PTE-07 改為：

$$
\boxed{
\text{Allocate}(
\mathcal T,
\mathcal R
).
}
$$

其中：

$$
\mathcal R
$$

是有限研究資源。

---

# 4. 候選理論集合

設：

$$
\boxed{
\mathcal T
=
\{T_1,T_2,\ldots,T_n\}.
}
$$

每個理論可以：

- 互斥；
- 部分重疊；
- 互補；
- 處理不同尺度；
- 使用不同表示。

---

# 5. 不能直接比較原始文本

因為：

$$
|T_i|
$$

可能差異極大。

一套理論：

- 1000 頁；
- 100 個術語；

不天然優於：

- 10 頁；
- 3 個 invariant。

---

# 6. 先做 PTE Normalization

每個：

$$
T_i
$$

先產生：

```text
TheoryManifest
ClaimLedger
Strongest Interpretation
Operationalization
Implementation
Matched Baseline
Evidence Receipt
Residue Report
```

---

# 7. 只有經過 normalization 才進 tournament

否則：

> 一邊是完整工程系統，一邊只是文字概念。

沒有可比性。

---

# 8. Theory Tournament

本文定義：

$$
\boxed{
\mathfrak T
=
(
\mathcal T,
\mathcal B,
\mathcal E,
\mathcal R,
\Pi
)
}
$$

其中：

- $\mathcal T$：候選理論；
- $\mathcal B$：baseline family；
- $\mathcal E$：可用證據；
- $\mathcal R$：研究資源；
- $\Pi$：競賽規則。

---

# 9. Tournament 不直接判真假

它產生：

$$
\boxed{
\text{research priority ordering}.
}
$$

---

# 10. 理論真正的競爭對手首先不是其他理論

而是：

$$
\boxed{
\text{strongest known reconstruction}.
}
$$

---

# 11. 第一階：Internal Qualification

每套理論先問：

- claim 是否清楚？
- 是否可形式化？
- 是否有 observable？
- 是否有 falsifier？
- 是否能實作？
- 是否能建立 baseline？

---

# 12. Internal Qualification Failure

若：

$$
O(T_i)=\varnothing,
$$

且沒有合理 proxy，

則：

```text
NON_OPERATIONAL
```

---

# 13. 這不是永久淘汰

可能等待：

- 新測量；
- 新形式化；
- 新工具。

---

# 14. 第二階：Matched Reconstruction

計算：

$$
\Delta_i
=
M(S_{T_i})
-
M(B^{*}_i).
$$

---

# 15. 若 $\Delta_i=0$

標：

```text
RECONSTRUCTIBLE
```

但仍保存：

$$
V_C,V_F,V_E.
$$

---

# 16. 第三階：Adversarial Challenge

搜尋：

$$
D_{\Delta,i}.
$$

---

## 16.1 目標不是多跑測試

而是找：

$$
\boxed{
\text{maximum information difference}.
}
$$

---

# 17. 第四階：External Evidence

根據：

$$
E_{\min}(T_i,D)
$$

判定下一個 evidence tier。

---

# 18. 第五階：Residue Extraction

得到：

$$
\boxed{
R_i
=
R_{\mathcal B,\mathcal E}(T_i).
}
$$

---

# 19. Tournament 真正比較的是 Residue

而不是：

$$
T_i
$$

的原始宏大程度。

---

# 20. Residue Quality

一個 residue 可以很大，

但沒有價值。

---

## 20.1 例如

> 無法測量的模糊主張很多。

這只是：

$$
\text{large unknown},
$$

不是：

$$
\text{high-value residue}.
$$

---

# 21. 因此需要 Residual Research Priority

定義：

$$
\boxed{
RRP(T_i)
=
f(
I_i,
U_i,
X_i,
G_i,
E_i,
C_i,
W_i
).
}
$$

---

# 22. Impact

$$
I_i
$$

表示：

> 如果 residue 成立，會改變多少理論、工程或現實決策？

---

# 23. Uncertainty

$$
U_i
$$

表示：

> 當前 epistemic state 還有多少未決？

---

# 24. Testability

$$
X_i
$$

表示：

> 是否存在高區分力下一步測試？

---

# 25. Residual Distinctiveness

$$
G_i
$$

表示：

> residue 是否真的在 strongest baseline 之外？

---

# 26. Expected Epistemic Gain

$$
E_i
$$

表示：

> 下一個實驗預期能改變多少 epistemic state？

---

# 27. Cost

$$
C_i
$$

表示：

> 取得下一輪證據需要多少資源？

---

# 28. World Access

$$
W_i
$$

表示：

> 是否需要稀缺現實世界接口？

---

# 29. 最小優先函數

可先寫成：

$$
\boxed{
RRP_i
=
\frac{
I_i
\cdot
U_i
\cdot
X_i
\cdot
G_i
\cdot
E_i
}{
C_i
}
}
$$

但本文不建議把它當唯一分數。

---

# 30. 為什麼不建議單一 score？

因為：

- high-impact / high-cost；
- low-impact / low-cost；

可能無法用單一權重公平比較。

---

# 31. Pareto Frontier 更合理

定義：

$$
\boxed{
\mathcal F_T
=
\text{ParetoFrontier}
(
I,U,X,G,E,-C,-W
).
}
$$

---

# 32. Tournament 先保留 Pareto 候選

再做：

- 專家判定；
- 多目標選擇；
- portfolio allocation。

---

# 33. Portfolio 而不是 Winner-Take-All

科學資源不應：

$$
\boxed{
100\%
\rightarrow
T^{*}.
}
$$

---

# 34. 因為高不確定性需要分散

可建立：

$$
\boxed{
\mathbf a
=
(a_1,\ldots,a_n),
\quad
\sum_i a_i=1.
}
$$

其中：

$$
a_i
$$

是研究資源比例。

---

# 35. Research Portfolio

目標：

$$
\boxed{
\max_{\mathbf a}
\mathbb E[
\text{Epistemic Gain}
]
}
$$

subject to：

$$
\sum_i a_iC_i
\le
B.
$$

---

# 36. 這像 portfolio，但不是金融市場

因為 payoff 是：

$$
\boxed{
\text{knowledge gain}.
}
$$

不是金錢。

---

# 37. Hypothesis Market 的「市場」是什麼？

它表示：

> 多個假說競爭有限驗證資源。

---

# 38. 不表示

> 真理由價格決定。

---

# 39. Market Unit

真正交易的不是：

$$
T_i.
$$

而是：

$$
\boxed{
\text{next experiment slot}.
}
$$

---

# 40. 所以可以稱

# **Evidence Allocation Market**

---

# 41. 理論提出成本正在下降

AI 使：

$$
C_{\mathrm{proposal}}
\downarrow.
$$

---

# 42. 於是候選數量可能爆炸

$$
|\mathcal T|
\uparrow\uparrow.
$$

---

# 43. 驗證資源不會同步無限

$$
|\mathcal R|
<\infty.
$$

---

# 44. 因此產生新的 scarcity

$$
\boxed{
\text{Hypothesis Abundance}
+
\text{Evidence Scarcity}.
}
$$

---

# 45. 這可能成為 AI 科學時代的核心張力

不是：

> 沒有想法。

而是：

> 想法太多，世界接口太少。

---

# 46. World Access Allocation

PTE-06 已指出：

真正稀缺可能是：

- lab；
- cohort；
- telescope；
- accelerator；
- hardware；
- field deployment。

---

# 47. 定義 World Access Budget

$$
\boxed{
B_W.
}
$$

---

# 48. 每個 theory residue 需要

$$
w_i.
$$

---

# 49. 約束

$$
\sum_i a_iw_i
\le
B_W.
$$

---

# 50. World Ticket

本文稱一次昂貴 external validation 機會為：

# **World Ticket**

---

# 51. 理論要先通過便宜壓測

才更有資格拿：

$$
\boxed{
\text{World Ticket}.
}
$$

---

# 52. 這不是歧視 speculative theory

而是避免：

> 可被 Python 反例打掉的理論直接消耗十年 cohort。

---

# 53. Cheap-Before-Expensive Principle

$$
\boxed{
\text{Cheap falsification first;
expensive evidence later}.
}
$$

---

# 54. 但不能因此永遠不做昂貴研究

如果：

$$
R(T)
$$

只剩 physical test 才能區分，

則：

$$
\boxed{
\text{world access becomes the correct next step}.
}
$$

---

# 55. Evidence Escalation Ladder

```text
formal
synthetic
external observational
controlled experiment
longitudinal/world-generated
```

---

# 56. 每一階都問

> 下一階的 expected information gain 值不值得成本？

---

# 57. Expected Information Gain

設 epistemic state：

$$
S.
$$

實驗：

$$
e.
$$

定義：

$$
\boxed{
EIG(e)
=
\mathbb E[
d(
S_{\mathrm{after}},
S_{\mathrm{before}}
)
].
}
$$

---

# 58. Cost-Normalized EIG

$$
\boxed{
CEIG(e)
=
\frac{
EIG(e)
}{
C(e)
}.
}
$$

---

# 59. 若 world experiment 極昂貴

但能一次區分：

$$
T_1,T_2,T_3,T_4,
$$

可能仍然值得。

---

# 60. Multi-Theory Experiment

最好的實驗不一定只測一套理論。

---

## 60.1 定義

$$
e^{*}
$$

若可以同時改變多個：

$$
T_i
$$

的 epistemic state，

其價值更高。

---

# 61. Shared Distinguishing Experiment

$$
\boxed{
D(e)
=
\{T_i:e\text{ discriminates }T_i\}.
}
$$

---

# 62. 實驗設計目標

$$
\boxed{
\max_e
\frac{
\sum_{T_i\in D(e)}
EIG_i(e)
}{
C(e)
}.
}
$$

---

# 63. 這是 AI 很適合做的

因為 AI 可以搜尋大量：

$$
e.
$$

---

# 64. Theory Tournament 不一定是 pairwise

不是：

$$
T_1\text{ vs }T_2.
$$

而可能：

$$
\boxed{
\text{one experiment}
\rightarrow
\text{many theories updated}.
}
$$

---

# 65. 理論之間也可以合併

若：

$$
R(T_1)
$$

與：

$$
R(T_2)
$$

互補，

可建立：

$$
T_{1\oplus2}.
$$

---

# 66. Merge 不能偷渡勝利

新理論：

$$
T_{1\oplus2}
$$

要重新跑 PTE。

---

# 67. 理論分叉

若同一理論：

$$
T
$$

殘差有兩個不同方向，

可以：

$$
T\rightarrow
T_a,T_b.
$$

---

# 68. Fork 也是市場行為

不同 fork 競爭：

$$
\text{next evidence}.
$$

---

# 69. 理論被 baseline 吸收

若：

$$
R(T_i)\rightarrow\varnothing,
$$

它可能進入：

```text
RECONSTRUCTED / ARCHIVED
```

---

# 70. 不是消失

其：

- historical value；
- engineering value；
- coordinate value；

仍可保存。

---

# 71. Archive 不是垃圾桶

Archived theory 可以被：

$$
\text{new evidence}
$$

重新開啟。

---

# 72. Reopen Condition

若：

$$
\mathcal E_{new}
$$

造成：

$$
R_{\mathcal B,\mathcal E_{new}}(T)
\neq
\varnothing,
$$

則：

```text
ARCHIVED -> REOPENED
```

---

# 73. Epistemic Frontier

本文定義：

$$
\boxed{
\mathcal F_E(t)
}
$$

為時刻 $t$ 所有仍具有高研究價值 residue 的集合。

---

# 74. Frontier 不是所有未解問題

而是：

> 已經接受目前可行 cheapest strong challenge 後，仍留下的高價值未解部分。

---

# 75. Frontier Node

每個 node：

```text
theory_id
residue_id
current_baseline
current_evidence
current_status
next_distinguishing_test
expected_information_gain
cost
world_access
```

---

# 76. Frontier 是動態圖

$$
\boxed{
\mathcal F_E(t+1)
\neq
\mathcal F_E(t).
}
$$

---

# 77. 新 baseline 會移動 frontier

---

# 78. 新 evidence 會移動 frontier

---

# 79. 新 measurement technology 也會移動 frontier

---

# 80. 因此科學前沿不是固定論文清單

而是：

$$
\boxed{
\text{dynamic unresolved residue graph}.
}
$$

---

# 81. 這與傳統 citation ranking 不同

Citation 高：

$$
\not\Rightarrow
$$

residue 高。

---

# 82. 論文新：

$$
\not\Rightarrow
$$

testability 高。

---

# 83. 作者有名：

$$
\not\Rightarrow
$$

baseline-resistant。

---

# 84. AI consensus 高：

$$
\not\Rightarrow
$$

external evidence 強。

---

# 85. Tournament 應盲化作者身份嗎？

某些階段可以。

---

## 85.1 Claim / baseline stage

可隱去：

- 作者；
- 機構；
- citation count。

降低 prestige bias。

---

# 86. 但 source provenance 不能消失

Evaluator 不看身份，

audit layer 仍保留：

$$
\text{source identity}.
$$

---

# 87. Blind Theory Qualification

可以讓第一階只看：

```text
claims
definitions
evidence
operationalization
```

---

# 88. 這是一個可測制度

比較：

```text
named review
blind review
```

是否改變 resource allocation。

---

# 89. Theory Tournament 的公平性

至少需要：

$$
\boxed{
\text{same protocol class}
}
$$

而不是所有理論使用同一個 benchmark。

---

# 90. 不同領域不能硬用同一 metric

物理：

$$
\neq
$$

軟體：

$$
\neq
$$

政治理論。

---

# 91. 所以是 protocol fairness

不是 metric uniformity。

---

# 92. Protocol Fairness

每套理論都必須：

- source freeze；
- strongest interpretation；
- falsifier；
- matched reconstruction；
- evidence-level honesty；
- reproducibility。

---

# 93. 但 metric 可領域化

---

# 94. Tournament Layering

可以分：

```text
Formal League
Software League
Simulation League
Experimental League
Longitudinal League
```

---

# 95. 跨 league 不直接比 score

只比：

$$
\text{resource allocation arguments}.
$$

---

# 96. Hypothesis Market 的價格可以是什麼？

若要使用「價格」概念，

可定義：

$$
\boxed{
P_E(T)
=
\text{marginal evidence cost}.
}
$$

---

# 97. 不是「真理價格」

而是：

> 再降低一單位不確定性要花多少？

---

# 98. Epistemic Price

$$
\boxed{
P_K
=
\frac{
\Delta C
}{
-\Delta U
}.
}
$$

---

# 99. 高價理論

可能很重要，

只是 evidence 非常貴。

---

# 100. 低價理論

可能只需：

$$
100
$$

行程式就能打掉。

---

# 101. 先買便宜資訊

這是一種：

$$
\boxed{
\text{Value of Information}
}
$$

策略。

---

# 102. Research Option Value

PTE-02 已指出舊理論保存具有期權價值。

在市場模型中：

$$
\boxed{
O_R(T)
}
$$

代表：

> 未來工具變強後重新測試它的可能收益。

---

# 103. 因此低 priority 不等於刪除

可以：

```text
PAUSED
```

---

# 104. Pause Condition

當：

- evidence floor 太高；
- tool 不成熟；
- EIG 太低；
- 無 distinguishing test。

---

# 105. Resume Condition

當：

- new dataset；
- new model；
- new instrument；
- new formal result；
- lower evidence cost。

---

# 106. 市場需要 memory

沒有版本與歷史：

$$
\text{same dead theory}
$$

會反覆重新消耗資源。

---

# 107. Theory Registry

```text
theory_id
versions
claims
past tests
baselines
counterexamples
residue_history
world_wait
archive_reason
```

---

# 108. Duplicate Theory Detection

AI 可以找：

$$
T_i
\approx
T_j.
$$

---

# 109. 這可以防止重新包裝已知理論反覆進場

---

# 110. Novelty Check

新理論先問：

> 它和既有 theory equivalence class 有多遠？

---

# 111. Reconstruction Equivalence Registry

可以保存：

$$
[T_i]_{\mathcal O}.
$$

---

# 112. 若只是新命名

直接標：

```text
KNOWN_RECONSTRUCTION_CANDIDATE
```

---

# 113. 但仍允許證明自己不同

不是封殺。

---

# 114. Tournament Anti-Gaming

AI 時代理論可能為了 score：

- 特化 benchmark；
- 躲避 falsifier；
- 縮小 scope；
- 增加模糊度。

---

# 115. Scope Gaming

如果理論每次失敗都縮 scope，

最後可能：

$$
D\rightarrow\epsilon.
$$

---

# 116. Scope Penalty

需要記錄：

$$
\boxed{
S_R
=
\frac{
|D_{\mathrm{current}}|
}{
|D_{\mathrm{original}}|
}.
}
$$

---

# 117. 不是禁止縮 scope

而是讓大家看見：

> 宏大性已經縮小多少。

---

# 118. Claim Inflation Penalty

反之，

若小結果被重新擴成全域，

也要轉紅。

---

# 119. Publication Gaming

若系統以：

$$
N_{\mathrm{papers}}
$$

為 reward，

AI 會拆文章。

---

# 120. 所以 tournament 不應獎勵 paper count

---

# 121. 應獎勵

$$
\boxed{
\text{validated epistemic transition}.
}
$$

---

# 122. Epistemic Transition Unit

例如：

```text
UNRESOLVED -> FALSIFIED
UNRESOLVED -> SUPPORTED
UNRESOLVED -> RECONSTRUCTIBLE
PROXY_ONLY -> EXPERIMENTALLY_SUPPORTED
RESIDUAL -> FORMALLY_SEPARATED
```

---

# 123. 每個 transition 都需 receipt

---

# 124. Research Reward

可定義：

$$
\boxed{
R_{\mathrm{science}}
=
\sum_j
w_j
\Delta S_j
}
$$

其中：

$$
\Delta S_j
$$

是有證據的 epistemic transition。

---

# 125. Negative Result 也有 reward

如果一個昂貴理論被公平否證：

$$
\boxed{
\text{knowledge gained}.
}
$$

---

# 126. 所以 market 不應只獎勵「成功」

---

# 127. Falsification Bounty

可以對：

$$
C_i
$$

設定：

> 找到有效 distinguishing counterexample。

---

# 128. 但反例必須過 validity gate

避免垃圾攻擊。

---

# 129. Reconstruction Bounty

也可以獎勵：

> 用更簡單 conventional system 重建 claimed novelty。

---

# 130. 這會促進 epistemic compression

---

# 131. Replication Bounty

對高 impact result：

> 第三方 fresh replay。

---

# 132. 世界實驗 Bounty

對：

$$
WAITING\_FOR\_WORLD
$$

的高 RRP claim，

提供 physical test 資源。

---

# 133. 這比只有論文 citation 更接近證據需求

---

# 134. AI 自動研究的治理問題

誰決定：

$$
I_i
$$

也就是 impact？

---

# 135. 不應由單一模型決定

可以有：

- scientific impact；
- engineering impact；
- social impact；
- safety impact；
- curiosity value。

---

# 136. 多權重 profile

$$
\boxed{
\mathbf I_i
=
(
I_s,
I_e,
I_{soc},
I_{safe},
I_c
).
}
$$

---

# 137. 不同資助者可使用不同 profile

但：

$$
\text{evidence state}
$$

應共用。

---

# 138. 價值偏好可以不同

證據帳本不能跟著變。

---

# 139. 這是一個重要制度分離

$$
\boxed{
\text{Value Allocation}
\neq
\text{Evidence Status}.
}
$$

---

# 140. 一個社會可以不資助某理論

不等於：

$$
T=\text{False}.
$$

---

# 141. 一個社會大量資助某理論

也不等於：

$$
T=\text{True}.
$$

---

# 142. Hypothesis Market 必須保留這條邊界

---

# 143. AI 評審的風險

如果大量 theory 都由相同 foundation model 評估，

可能產生：

$$
\boxed{
\text{epistemic monoculture}.
}
$$

---

# 144. Monoculture Risk

模型共同偏好：

- 某種形式化；
- 某種文風；
- 某種主流理論；

可能系統性低估異質理論。

---

# 145. 因此需要 evaluator diversity

包括：

- 不同模型；
- 不同方法；
- 人類專家；
- formal solver；
- external experiment。

---

# 146. Diversity 也不能只看模型名稱

如果底層訓練資料高度相似，

仍可能相關。

---

# 147. Independence Receipt

記：

```text
evaluator
provider
model family
context isolation
data overlap known?
blind status
human reviewer
```

---

# 148. Theory Tournament 的 Twin

對重要 claim，

最好有：

$$
\boxed{
\text{independent governing reviewer}.
}
$$

---

# 149. 如果沒有

就標：

```text
TWIN = DEGRADED
```

---

# 150. 不應在同一上下文模擬兩個獨立審查者

---

# 151. Tournament State Machine

```text
SUBMITTED
NORMALIZED
QUALIFIED
RECONSTRUCTED
CHALLENGED
RESIDUAL
PAUSED
WORLD_QUEUE
FUNDED
TESTED
UPDATED
ARCHIVED
REOPENED
```

---

# 152. 晉級不是榮譽

只是：

> 獲得下一輪更昂貴 evidence 的資格。

---

# 153. Elimination 也不是羞辱

只是：

> current marginal information gain 太低。

---

# 154. Theory League Table 的危險

如果做單一排名：

$$
1,2,3,\ldots
$$

容易變成：

- prestige；
- marketing；
- false certainty。

---

# 155. 所以更適合 dashboard

顯示：

```text
residue
evidence
baseline closure
testability
cost
world wait
next experiment
```

---

# 156. 不顯示「真理分數」

---

# 157. Public Epistemic Dashboard

這可能是未來研究基礎設施。

---

# 158. 每個理論都有可點開 evidence lineage

不是只看 abstract。

---

# 159. AI 可以持續更新

當：

- 新 paper；
- 新 dataset；
- 新 replication；
- 新 counterexample；

出現。

---

# 160. 但更新需要 source authority

不能自動把網路評論當同級證據。

---

# 161. Evidence Authority Graph

$$
\boxed{
G_E
=
(V_E,E_E).
}
$$

---

# 162. 節點包括

- paper；
- code；
- dataset；
- experiment；
- replication；
- critique；
- correction。

---

# 163. 邊表示

- supports；
- contradicts；
- reconstructs；
- depends；
- supersedes。

---

# 164. Theory Frontier 其實是 knowledge graph frontier

---

# 165. AI 時代 publication 可能退居第二層

真正第一層：

$$
\boxed{
\text{machine-readable evidence objects}.
}
$$

---

# 166. Paper 仍然重要

因為提供：

- 敘事；
- 理論背景；
- 人類可讀解釋。

---

# 167. 但 machine-native science 需要更多

- claim ID；
- experiment ID；
- hashes；
- baselines；
- receipts；
- residue。

---

# 168. PTE Series 本身就是一個例子

它從：

$$
\text{方法直覺}
$$

逐步變成：

$$
\text{protocol}
\rightarrow
\text{metrics}
\rightarrow
\text{runtime}
\rightarrow
\text{evidence allocation}.
$$

---

# 169. 但本系列目前仍是方法論

尚未建立：

$$
\boxed{
\text{large-scale independent empirical validation}.
}
$$

---

# 170. 所以 PTE 自己也應接受 PTE

這是系列最重要的自反要求。

---

# 171. PTE Self-Application

將：

$$
T_{\mathrm{PTE}}
$$

放入：

$$
\mathsf{Assume}^{+}.
$$

---

# 172. 建 strongest baseline

例如：

- standard scientific method；
- preregistration；
- benchmark best practice；
- TEVV；
- adversarial evaluation；
- reproducible research pipelines。

---

# 173. 然後問

> PTE 到底有沒有新增不可約方法？

---

# 174. 完全可能結果是

$$
\boxed{
V_C,V_F,V_E>0,
\quad
V_U=\text{NotEstablished}.
}
$$

---

# 175. 如果如此

PTE 也必須接受。

---

# 176. 這才符合《假設你是對的》

不是只用來測別人的理論。

---

# 177. Self-Application Constraint

$$
\boxed{
\text{A theory-testing framework that exempts itself is incomplete}.
}
$$

---

# 178. PTE-07 的第一個未來實驗

選：

$$
N
$$

套公開理論，

跑完整：

$$
PTE\text{-}TSR.
$$

---

# 179. 建立 theory portfolio

測：

- resource allocation；
- residue stability；
- false-win reduction；
- evidence gain。

---

# 180. 與傳統 allocation 比

```text
citation-based
expert-only
random
PTE-RRP
```

---

# 181. 觀察哪一個 allocation

在固定 budget：

$$
B
$$

下得到更多：

$$
\text{validated epistemic transitions}.
$$

---

# 182. 核心實驗指標

$$
\boxed{
EGR
=
\frac{
\text{Epistemic Gain}
}{
\text{Research Cost}
}.
}
$$

---

# 183. World Ticket Efficiency

$$
\boxed{
WTE
=
\frac{
\text{validated transitions from world tests}
}{
\text{world tickets consumed}
}.
}
$$

---

# 184. Residue Resolution Rate

$$
\boxed{
RRR
=
\frac{
\text{resolved residue nodes}
}{
\text{tested residue nodes}
}.
}
$$

---

# 185. False Priority Rate

如果高 priority 理論經第一個 cheap test 就崩，

可能表示 allocation model 有問題。

---

# 186. But cheap falsification success 也不是浪費

因為：

$$
\boxed{
\text{cheaply killing expensive error}
}
$$

本身有高價值。

---

# 187. 所以要看 avoided cost

$$
\boxed{
C_{\mathrm{avoided}}.
}
$$

---

# 188. Counterfactual Research Savings

若 cheap PTE test 避免昂貴 experiment，

其價值：

$$
\boxed{
V_{\mathrm{save}}
=
C_{\mathrm{expensive}}
-
C_{\mathrm{cheap}}.
}
$$

---

# 189. Hypothesis Market 的總目標

不是最大化：

$$
N_{\mathrm{wins}}.
$$

---

# 190. 而是最大化：

$$
\boxed{
\text{credible knowledge gain per scarce research resource}.
}
$$

---

# 191. 這也改變「失敗」的意義

理論被快速公平打掉：

$$
\neq
$$

研究失敗。

---

# 192. 反而可能是高效率科學

---

# 193. 一個理論存活很久也不代表成功

可能只是：

$$
\text{never properly tested}.
$$

---

# 194. Claim Survival Time

定義：

$$
\tau_S
$$

但不能直接當品質。

---

# 195. 更重要的是

$$
\boxed{
\text{challenge intensity}.
}
$$

---

# 196. Challenge-Adjusted Survival

可定義：

$$
\boxed{
CAS
=
\frac{
\tau_S
}{
1+\text{weak challenge penalty}
}
}
$$

但仍只作探索性指標。

---

# 197. 理論市場的倫理

不能因為某理論：

$$
RRP
$$

低，

就阻止私人或好奇研究。

---

# 198. 它只影響公共稀缺資源的優先級

---

# 199. Open Research Lane

可以保留：

```text
open exploration
```

不需要 tournament qualification。

---

# 200. Scarce Resource Lane

需要：

```text
evidence allocation review
```

---

# 201. 兩者並存

避免：

$$
\text{optimization}
$$

扼殺：

$$
\text{serendipity}.
$$

---

# 202. Curiosity Reserve

公共 portfolio 可保留：

$$
\boxed{
\alpha B
}
$$

給：

- 高風險；
- 高奇異；
- 尚不可量化；

研究。

---

# 203. Exploitation / Exploration

資源分：

$$
B
=
B_{\mathrm{exploit}}
+
B_{\mathrm{explore}}.
$$

---

# 204. 這避免 Hypothesis Market 變得過度保守

---

# 205. AI 也應保留異常點

不是所有 low-probability 理論都立即刪除。

---

# 206. 但異常點進昂貴實驗前

仍應先走：

$$
\text{cheap falsification}.
$$

---

# 207. 理論市場與公開性

公開：

- source；
- benchmark；
- residue；
- receipt；

可以讓第三方 challenge。

---

# 208. 但 private theory 也可用同一 protocol

---

# 209. Confidential Tournament

只要：

- source boundary；
- audit；
- role separation；

存在。

---

# 210. PTE-07 最終制度架構

```text
Theory Registry
-> PTE Normalization
-> Cheap Stress Test
-> Matched Reconstruction
-> Residue Extraction
-> Frontier Registry
-> Evidence Allocation
-> World Test
-> Epistemic Update
-> Archive / Reopen
```

---

# 211. 最終狀態不是 Winner

而是：

```text
CURRENTLY_SUPPORTED
RECONSTRUCTIBLE
RESIDUAL
WAITING_FOR_WORLD
FALSIFIED
PAUSED
ARCHIVED
REOPENED
```

---

# 212. Theory Tournament 不是比誰活著

而是：

> 哪個 epistemic transition 最值得現在做？

---

# 213. PTE-07 核心公式

第一：

$$
\boxed{
\mathcal T
=
\{T_1,\ldots,T_n\}.
}
$$

第二：

$$
\boxed{
R_i
=
R_{\mathcal B,\mathcal E}(T_i).
}
$$

第三：

$$
\boxed{
RRP(T_i)
=
f(
I_i,U_i,X_i,G_i,E_i,C_i,W_i
).
}
$$

第四：

$$
\boxed{
e^{*}
=
\arg\max_e
\frac{
EIG(e)
}{
C(e)
}.
}
$$

第五：

$$
\boxed{
\text{Hypothesis Abundance}
+
\text{Evidence Scarcity}.
}
$$

---

# 214. 七篇系列的完整閉合

PTE-01：

$$
\boxed{
\text{先公平假設它為真}.
}
$$

---

PTE-02：

$$
\boxed{
\text{測量從理論到證據的時間}.
}
$$

---

PTE-03：

$$
\boxed{
\text{用 strongest matched reconstruction 防止假新穎}.
}
$$

---

PTE-04：

$$
\boxed{
\text{把失敗、可重建、可用與未知拆開回收}.
}
$$

---

PTE-05：

$$
\boxed{
\text{把懷疑編譯成 AI runtime}.
}
$$

---

PTE-06：

$$
\boxed{
\text{知道哪些證據必須等世界}.
}
$$

---

PTE-07：

$$
\boxed{
\text{把稀缺研究資源給最值得的下一個證據}.
}
$$

---

# 215. 整套方法的最短形式

$$
\boxed{
\text{Assume}
\rightarrow
\text{Build}
\rightarrow
\text{Match}
\rightarrow
\text{Break}
\rightarrow
\text{Salvage}
\rightarrow
\text{Wait}
\rightarrow
\text{Allocate}.
}
$$

---

# 216. 《假設你是對的》真正的意思

它不是：

> 我相信你。

而是：

> **我願意先暫停最便宜的反駁方式，替你的理論建立它最強、最公平、最可執行的版本。**

然後：

> **我也會替最強既有替代方案做同樣的事。**

最後讓：

- 程式；
- 反例；
- baseline；
- 外部資料；
- 世界本身；

決定下一個 epistemic state。

---

# 217. 這是一種認識論上的對稱性

理論不因陌生而被提前打死。

也不因宏大而獲得豁免。

---

# 218. Strong Theory Deserves Strong Test

$$
\boxed{
\text{Claim Strength}\uparrow
\Rightarrow
\text{Challenge Strength}\uparrow.
}
$$

---

# 219. 這也是系列最核心的倫理

不是對人客氣。

而是對：

$$
\boxed{
\text{evidence}
}
$$

公平。

---

# 220. AI 時代真正可能改變的科學秩序

過去：

$$
\text{theory generation}
\ll
\text{verification capacity}.
$$

---

# 221. 未來可能：

$$
\text{theory generation}
\gg
\text{world validation capacity}.
$$

---

# 222. 所以瓶頸從思想稀缺轉向證據稀缺

---

# 223. 這需要新的科學基礎設施

不只是更大的模型。

而是：

- theory registry；
- evidence graph；
- reusable baselines；
- automated labs；
- replication infrastructure；
- longitudinal data systems；
- world-access governance。

---

# 224. AI 會把很多理論推到「世界門口」

但世界門口只能一次進有限數量。

---

# 225. 所以新的研究能力不是只會想

而是：

$$
\boxed{
\text{知道什麼值得下一次真的去問世界}.
}
$$

---

# 226. PTE Self-Test

本系列最後必須對自己留下：

```text
PTE-specific superiority = NotEstablished
large-scale external validation = NotMeasured
independent replication = NotEstablished
methodological usefulness = Proposed
engineering runtime feasibility = Testable
```

---

# 227. 這不是弱化 PTE

反而是：

> PTE 必須遵守 PTE。

---

# 228. 如果未來 strong conventional research methodology

能完全重建 PTE：

$$
\Delta_{\mathrm{PTE}}=0,
$$

那麼：

$$
\boxed{
\text{PTE can still remain a useful coordinate system}.
}
$$

---

# 229. 如果 PTE 在實驗中真的降低

- false theory wins；
- weak baseline bias；
- unreproducible conclusions；

則：

$$
V_E(\mathrm{PTE})>0
$$

得到更強支持。

---

# 230. 如果進一步出現 baseline-resistant gain

才開始研究：

$$
V_U(\mathrm{PTE}).
$$

---

# 231. 這就是自反閉合

$$
\boxed{
\text{The framework is not exempt from the framework}.
}
$$

---

# 232. 最終結論

AI 時代可能第一次讓一件長期昂貴的事情變得日常化：

> **不是更快提出理論，而是更快給理論一個公平的機會。**

當：

$$
L_{TE}
\downarrow,
$$

我們不需要在：

> 「聽起來荒謬。」

和：

> 「聽起來革命性。」

之間太早選邊。

可以先：

$$
\mathsf{Assume}^{+}(T).
$$

然後把它做出來。

再建立：

$$
B^{*}(T).
$$

讓兩邊接受相同壓力。

如果理論的宏大性被吸收，

保存：

$$
V_C,V_F,V_E.
$$

如果仍有：

$$
R_{\mathcal B,\mathcal E}(T),
$$

就把研究集中到 residue。

如果下一步需要世界，

承認：

$$
\text{WAITING FOR WORLD}.
$$

當很多理論同時走到這一步，

真正的科學問題就變成：

> **哪一個下一步證據，最值得我們現在付出世界成本？**

因此，《假設你是對的》系列最終不是一套「替奇怪理論辯護」的方法。

它是一套：

$$
\boxed{
\text{讓理論更快從敘事進入證據競爭}
}
$$

的方法。

更短地說：

$$
\boxed{
\text{不要先問誰講得像真的。}
}
$$

而是：

$$
\boxed{
\text{先假設它是真的，做到最強，再看世界還剩下什麼不同。}
}
$$

若最後沒有差異，

我們得到一個乾淨的重建結果。

若留下工程價值，

我們把工程價值留下。

若留下不可約殘差，

我們把下一張 World Ticket 給它。

若世界還沒回答，

我們就等待。

這就是 PTE 的完整閉合：

$$
\boxed{
\text{Assume}
\rightarrow
\text{Execute}
\rightarrow
\text{Challenge}
\rightarrow
\text{Reconstruct}
\rightarrow
\text{Salvage}
\rightarrow
\text{Allocate}
\rightarrow
\text{Reopen}.
}
$$

---

# 233. 系列最終狀態

**PTE-01 — Assume the Theory Is True**  
建立暫時真值工程母協議。

**PTE-02 — Theory-to-Engineering Latency**  
建立 AI 時代理論驗證的時間經濟。

**PTE-03 — Matched Reconstruction Principle**  
建立有用性、優越性、獨特性與不可約性的分界。

**PTE-04 — Epistemic Salvage**  
建立多維價值、降級與不可約殘差。

**PTE-05 — AI-Native Theory Stress Runtime**  
建立可執行理論壓測、role separation 與 fresh replay。

**PTE-06 — Irreducible Evidence Floor**  
建立 AI 無法任意消除的外部證據與世界時間底。

**PTE-07 — Theory Tournaments and Hypothesis Markets**  
建立多理論研究資源配置、Epistemic Frontier 與 World Ticket 機制。

---

# 234. 最後一句

$$
\boxed{
\text{A good theory should survive more than admiration.}
}
$$

而一個好的科學系統，也應該做到：

$$
\boxed{
\text{讓值得活下來的結構留下，
讓不值得的宣稱更快消失，
讓真正未知的地方獲得下一次證據。}
}
$$
