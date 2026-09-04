---
title: "TCFT-02｜反事實視界：未發生世界、問題生成與認知覆蓋"
title_en: "The Counterfactual Horizon: Unrealized Worlds, Problem Generation, and Cognitive Coverage"
series: "Temporal Cognitive Frontier Theory (TCFT) / 時代認知前沿理論"
paper_no: "02"
version: "v0.1"
date: "2026-08-30"
author: "Neo.K"
affiliation: "EveMissLab / 一言諾科技有限公司"
document_type: "理論論文 / Counterfactual Horizon 篇"
language: "zh-Hant"
status: "正式系列初稿"
previous_paper: "TCFT-01｜未來底空間選擇：想像力、候選世界與問題先行"
next_paper: "TCFT-03｜反身性推理：當推理本身進入被推理世界"
---

# TCFT-02｜反事實視界：未發生世界、問題生成與認知覆蓋

## The Counterfactual Horizon: Unrealized Worlds, Problem Generation, and Cognitive Coverage

**系列：** Temporal Cognitive Frontier Theory, TCFT / 時代認知前沿理論  
**篇次：** 02  
**版本：** v0.1  
**日期：** 2026-08-30  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  

---

## 摘要

反事實推理通常被理解為對「如果事情不是這樣，而是那樣，結果會如何？」的推演。心理學、因果推理、決策科學與人工智能已長期研究 counterfactual thinking；結構因果模型則提供 intervention 與 counterfactual inference 的形式工具；近年的大型語言模型 benchmark 亦開始測試形式化、多跳與 forward counterfactual reasoning。然而，僅知道一個 agent 能否正確求解給定反事實，仍不足以描述其真正的反事實能力。

Temporal Cognitive Frontier Theory（TCFT）關心另一個更前置的問題：**哪些反事實會被生成？哪些不會？一個未被生成的反事實，是否可能足以翻轉決策、改寫歷史評價或暴露原有理論的失效？**

本文承接既有「反事實覆蓋度」概念，提出 **Counterfactual Horizon（反事實視界）**。對 agent $i$，在時間 $t$ 、知識條件 $\Gamma_t$ 與資源預算 $B$ 下，定義：

$$
\boxed{
\mathcal C_i(t;B,\Gamma)
=
G_i^{CF}
(
H_{\le t},
\mathfrak B_i(t),
B,
\Gamma
)
}
$$

其中 $H_{\le t}$ 為實際歷史， $\mathfrak B_i(t)$ 為 TCFT-01 的未來底空間，而 $G_i^{CF}$ 為反事實生成器。 $\mathcal C_i$ 不是所有 metaphysically possible worlds，而是該 agent 在當前 representation、knowledge、operators、policy 與 budget 下能合法生成、維持、比較與使用的反事實集合／生成區域。

本文區分五個容易被混為一談的量：

$$
\boxed{
\text{Counterfactual Correctness}
\neq
\text{Depth}
\neq
\text{Breadth}
\neq
\text{Coverage}
\neq
\text{Strategic Sufficiency}.
}
$$

一個 agent 可以在單一路徑上進行十階深度推理，但漏掉另一個一階分支；也可以生成大量分支，卻缺乏因果約束；甚至可以對既有候選反事實全部求解正確，卻仍沒有生成那個真正足以改變最適決策的反事實。

本文提出 **Counterfactual Blindspot** 與 **Reversal Witness**。若存在：

$$
c^*
\notin
\mathcal C_i(t)
$$

且在加入 $c^*$ 後，原決策：

$$
a_i^*
$$

不再保持最適：

$$
\arg\max_a U(a\mid \mathcal C_i)
\neq
\arg\max_a U(a\mid \mathcal C_i\cup\{c^*\}),
$$

則 $c^*$ 稱為一個反事實翻轉見證，表示原視界存在具有決策後果的盲點。

本文進一步提出 quality-adjusted counterfactual coverage。反事實能力不能以「生成越多越好」衡量，因為分支數在深度 $d$ 下可近似呈現：

$$
O(b^d),
$$

造成組合爆炸。成熟反事實系統必須同時處理 generation、constraint、pruning、diversity、counterexample search、relevance、termination 與 uncertainty reservation。因此：

$$
\boxed{
\text{High Counterfactual Capacity}
\neq
\text{Enumerate Everything}.
}
$$

真正重要的是在有限成本下，能否覆蓋足以改變推理、決策或理論結論的高價值反事實區域。

本文最後將反事實視界納入 TCFT 的時間正規化框架。若在 Frozen-Time 條件下，一個歷史人物、現代研究者、AI 或 human-AI system 能穩定生成同期 baseline 未能生成、且後續被證明具有高因果與決策價值的反事實，則可以形成 **Temporal Counterfactual Advancement** 候選。但此結果不證明特殊身份，也不證明全面優越性。

TCFT-02 的中心命題為：

$$
\boxed{
\text{The quality of reasoning depends not only on
how well an agent reasons within a counterfactual,
but on which counterfactuals become available to reason about.}
}
$$

**關鍵詞：** 反事實視界、反事實覆蓋度、反事實生成、反事實盲點、翻轉見證、可能世界、因果推理、決策魯棒性、AI、TCFT、Counterfactual Horizon

---

# Abstract

Counterfactual reasoning is commonly understood as reasoning about how events might have unfolded under alternative conditions. Psychology, causal inference, decision science, and artificial intelligence have long studied counterfactual thought, while structural causal models provide formal intervention-based tools for counterfactual inference. Recent large-language-model benchmarks further evaluate formal, multi-hop, and forward counterfactual reasoning. Yet the ability to correctly solve a supplied counterfactual does not fully characterize counterfactual intelligence.

Temporal Cognitive Frontier Theory (TCFT) asks a more prior question: **which counterfactuals are generated at all? Which remain ungenerated? Can an omitted counterfactual reverse a decision, alter an historical judgment, or expose the failure of a theory?**

Building on prior work on Counterfactual Coverage, this paper introduces the **Counterfactual Horizon**. For agent $i$ at time $t$, under knowledge context $\Gamma_t$ and resource budget $B$:

$$
\boxed{
\mathcal C_i(t;B,\Gamma)
=
G_i^{CF}
(
H_{\le t},
\mathfrak B_i(t),
B,
\Gamma
)
}
$$

where $H_{\le t}$ is actual history, $\mathfrak B_i(t)$ is the future base-space introduced in TCFT-01, and $G_i^{CF}$ is a counterfactual generator. $\mathcal C_i$ is not the set of all metaphysically possible worlds; it is the region of unrealized alternatives the agent can legally generate, represent, compare, and use under current cognitive and computational constraints.

We distinguish counterfactual correctness, depth, breadth, coverage, and strategic sufficiency. We introduce the notions of **Counterfactual Blindspot** and **Reversal Witness**: if an omitted counterfactual $c^*$ changes the optimal decision once introduced, then the previous horizon was strategically incomplete.

Because counterfactual branching can grow combinatorially, high counterfactual capacity cannot mean enumerating everything. A mature counterfactual system must allocate resources across generation, causal constraint, pruning, diversity, disconfirmation, relevance, termination, and uncertainty reservation. Counterfactual intelligence is therefore a problem of quality-adjusted coverage under bounded resources.

Finally, the paper defines **Temporal Counterfactual Advancement**: under a frozen-time audit, an agent may be temporally advanced if it reliably generates high-value counterfactuals that contemporaneous baselines fail to generate. This remains a performance claim, not an identity or status claim.

The central proposition is:

$$
\boxed{
\text{The quality of reasoning depends not only on
how well an agent reasons within a counterfactual,
but on which counterfactuals become available to reason about.}
}
$$

**Keywords:** counterfactual horizon; counterfactual coverage; counterfactual generation; blindspot; reversal witness; causal reasoning; decision robustness; AI; TCFT

---

# 1. 導論：反事實能力不是「會回答如果」

## 1.1 給定反事實與生成反事實

一個 benchmark 可以問：

> 如果事件 $A$ 沒有發生，而事件 $B$ 仍維持不變，結果 $Y$ 會如何？

agent 的任務是求：

$$
Y_{A\leftarrow a'}.
$$

這測量的是：

$$
\boxed{
\text{Counterfactual Inference Given a Query}.
}
$$

但現實決策者首先還要做另一件事：

> 哪一個「如果」值得被問？

這是：

$$
\boxed{
\text{Counterfactual Generation}.
}
$$

兩者不相同。

---

## 1.2 一個沒有被問出的「如果」

假設所有分析者都比較：

$$
c_1,c_2,c_3.
$$

並一致認為：

$$
a^*
$$

最佳。

但存在：

$$
c_4
$$

使：

$$
a^*
$$

在 $c_4$ 下產生災難。

如果沒有人生成：

$$
c_4,
$$

則：

$$
\text{perfect reasoning over }
\{c_1,c_2,c_3\}
$$

仍然可能導致錯誤決策。

因此：

$$
\boxed{
\text{Inference Quality}
\neq
\text{Counterfactual Support Quality}.
}
$$

---

# 2. 反事實的工作單位

本文不把任何幻想都稱作 counterfactual。

一個最小反事實候選可表示為：

$$
\boxed{
c
=
(
H,
\Delta,
P,
M,
Y,
E
).
}
$$

其中：

- $H$：actual/history anchor；
- $\Delta$：被修改的 antecedent / intervention；
- $P$：保持不變或需要重新推定的 preservation assumptions；
- $M$：transition / causal model；
- $Y$：推演結果；
- $E$：evidence / justification / provenance。

這不是唯一可能 schema，而是讓反事實可審計的最低工作形式。

---

# 3. Pearl-style Counterfactual 與 TCFT

在結構因果模型脈絡中，一種標準 counterfactual procedure 可概念性表示為：

$$
\boxed{
\text{Abduction}
\rightarrow
\text{Action / Intervention}
\rightarrow
\text{Prediction}.
}
$$

也就是：

1. 根據觀察推定背景狀態；
2. 修改指定變量或結構；
3. 在修改後模型中推演結果。

TCFT 接受這類形式工具的重要性。

但 TCFT-02 研究的是更上一層：

$$
\boxed{
\text{Who selected the intervention?
Who generated the alternative?
Who decided what to preserve?
}
$$

這些本身就是認知能力的一部分。

---

# 4. 反事實視界

承接既有反事實覆蓋度，定義：

$$
\boxed{
\mathcal C_i(t;B,\Gamma)
=
G_i^{CF}
(
H_{\le t},
\mathfrak B_i(t),
B,
\Gamma
).
}
$$

其中：

- $i$：agent / cognitive system；
- $t$：時間；
- $H_{\le t}$：截至當下的實際歷史；
- $\mathfrak B_i(t)$：TCFT-01 Future Base-Space；
- $B$：認知／計算 budget；
- $\Gamma$：知識、工具、representation、制度與 context；
- $G_i^{CF}$：counterfactual generator。

---

# 5. 反事實視界不是所有 possible worlds

必須保留：

$$
\boxed{
\mathcal C_i(t)
\neq
\Omega_{\mathrm{possible}}.
}
$$

也不假定：

$$
\bigcup_i
\mathcal C_i(t)
=
\Omega_{\mathrm{possible}}.
$$

一個 collective horizon 仍然可以漏掉：

$$
c^*.
$$

因此：

$$
\boxed{
\text{Collective Counterfactual Horizon}
\neq
\text{Counterfactual Exhaustiveness}.
}
$$

---

# 6. Counterfactual Correctness

對一個已給定反事實：

$$
c,
$$

agent 可以產生預測：

$$
\hat Y_i(c).
$$

若：

$$
\hat Y_i(c)
$$

與 causal model / ground truth / later evidence 相符，

表示：

$$
\boxed{
\text{Counterfactual Correctness}.
}
$$

但這只回答：

> 給你這個反事實，你算得對不對？

它不回答：

> 你會不會自己想到這個反事實？

---

# 7. Counterfactual Depth

定義一條反事實推演的有效步數／依賴深度：

$$
d(c).
$$

例如：

$$
A
\rightarrow
B
\rightarrow
C
\rightarrow
D
$$

修改：

$$
A'
$$

並一路推到：

$$
D'
$$

需要較高 depth。

近期 benchmark 已能生成不同 hop 數與 reasoning complexity 的 counterfactual tasks。

但：

$$
\boxed{
\text{Depth}
\neq
\text{Coverage}.
}
$$

---

# 8. Counterfactual Breadth

若 agent 一次生成：

$$
N
$$

個不同 alternatives，

可以有：

$$
Breadth_i=N.
$$

但單純的數量也不等於 coverage。

因為：

$$
c_1,c_2,\ldots,c_{1000}
$$

可能只是同一類微小變體。

---

# 9. Counterfactual Diversity

因此需要考慮：

$$
\boxed{
Diversity(
\mathcal C_i
).
}
$$

它可以來自：

- 不同 intervention variables；
- 不同 causal pathways；
- 不同 timescales；
- 不同 agents；
- 不同 institutions；
- 不同 representations；
- 不同 ontology assumptions。

這比 raw count 更有意義。

---

# 10. Counterfactual Coverage

若存在一個 reference relevant counterfactual set：

$$
\mathcal C_{rel},
$$

可概念性寫：

$$
\boxed{
Coverage_i
=
\frac{
|\mathcal C_i\cap\mathcal C_{rel}|
}{
|\mathcal C_{rel}|
}.
}
$$

但這個定義只能用在：

$$
\mathcal C_{rel}
$$

可合理建立的 benchmark。

現實中：

$$
\mathcal C_{rel}
$$

通常本身未知。

因此 TCFT 不宣稱可以直接測出「所有反事實覆蓋率」。

---

# 11. Relevant Counterfactual

不是所有 logical alternative 都值得算。

本文暫定：

$$
\boxed{
c\in\mathcal C_{rel}
}
$$

若 $c$ 至少具有某種：

- causal plausibility；
- decision relevance；
- explanatory relevance；
- falsification value；
- robustness value；
- policy relevance；
- theoretical discrimination。

---

# 12. Quality-Adjusted Counterfactual Coverage

因此：

$$
\boxed{
QCC_i
=
f(
Correctness,
Diversity,
Relevance,
CausalCoherence,
Discrimination,
Novelty,
Coverage,
Cost
).
}
$$

更保守的實作是保存向量：

$$
\vec QCC_i
$$

而不是硬壓一個總分。

---

# 13. Counterfactual Blindspot

定義：

$$
\boxed{
c^*
\in
\mathcal C_{rel}
\setminus
\mathcal C_i.
}
$$

如果 $c^*$ 具有高相關性，

則稱：

$$
\boxed{
\text{Counterfactual Blindspot}.
}
$$

它表示：

> 這個 alternative 對結論可能重要，但 agent 根本沒有把它生成出來。

---

# 14. Reversal Witness

更強的盲點是：

$$
\boxed{
c^*
\notin
\mathcal C_i
}
$$

且：

$$
\arg\max_a
U(a\mid\mathcal C_i)
\neq
\arg\max_a
U(a\mid\mathcal C_i\cup\{c^*\}).
$$

則：

$$
\boxed{
c^*
=
\text{Reversal Witness}.
}
$$

也就是：

> 只要把這一個漏掉的反事實加入，原本的最適決策就翻轉。

---

# 15. 反事實覆蓋度的真正危險

因此：

$$
\boxed{
\text{Observed Optimality}
\not\Rightarrow
\text{Counterfactual Robust Optimality}.
}
$$

一個政策、方法或 agent 在所有被測 alternatives 中最好，

不能推出：

$$
\boxed{
\text{不存在未生成的更好 alternative}.
}
$$

這是既有反事實覆蓋度命題在 TCFT 中的核心用途。

---

# 16. Counterfactual Robustness

如果某決策：

$$
a^*
$$

在廣泛高價值反事實中都保持優勢，

可以定義：

$$
\boxed{
Robust(a^*;\mathcal C)
}
$$

比單一路徑：

$$
U(a^*\mid H)
$$

更有資訊。

---

# 17. Robustness Margin

例如：

$$
\boxed{
RM(a)
=
\inf_{c\in\mathcal C_{rel}}
[
U(a,c)
-
U(a_c^*,c)
]
}
$$

只是其中一種候選形式。

若：

$$
RM(a)
$$

接近零，

代表只需要小幅反事實變化就可能翻轉。

---

# 18. Depth 與 Breadth 的正交性

存在兩個 agents：

$$
A,
B.
$$

可能：

$$
Depth_A\gg Depth_B
$$

但：

$$
Breadth_A\ll Breadth_B.
$$

A 很會把一條線算到底。

B 很會生成不同線。

因此：

$$
\boxed{
\text{Counterfactual Depth}
\perp
\text{Counterfactual Breadth}
}
$$

至少在理論上應先視為不同軸。

---

# 19. Breadth 與 Coverage 也不同

若 B 生成 1000 個 variations，

但真正 relevant counterfactual 是：

$$
c^*,
$$

而 B 沒生成，

則：

$$
Breadth_B=1000
$$

仍可能：

$$
StrategicCoverage_B
$$

很低。

---

# 20. Coverage 與 Exhaustiveness 也不同

TCFT 不要求：

$$
Coverage_i=1
$$

才算優秀。

在開放世界：

$$
Coverage=1
$$

通常不可證。

更合理的是：

$$
\boxed{
\text{bounded, quality-adjusted, decision-relevant coverage}.
}
$$

---

# 21. Counterfactual Branching Explosion

若每一節點平均可生成：

$$
b
$$

個 alternatives，

深度：

$$
d,
$$

完整 tree 大小約：

$$
\boxed{
O(b^d).
}
$$

因此：

$$
\boxed{
\text{Enumerate Everything}
}
$$

不是可行的普遍策略。

---

# 22. 反事實能力必須包含 Pruning

成熟 generator 需要：

$$
\boxed{
Generate
\rightarrow
Constrain
\rightarrow
Score
\rightarrow
Prune
\rightarrow
Expand
\rightarrow
Re-evaluate.
}
$$

所以：

$$
\boxed{
\text{Counterfactual Intelligence}
\neq
\text{Counterfactual Proliferation}.
}
$$

---

# 23. Pruning 也可能造成 Blindspot

若 pruning policy：

$$
\pi_{prune}
$$

過度依賴：

- probability；
- familiarity；
- current value；
- cultural prior；
- language similarity；

可能把真正低機率但高後果的：

$$
c^*
$$

提前刪除。

所以：

$$
\boxed{
\text{Efficient Pruning}
\neq
\text{Safe Pruning}.
}
$$

---

# 24. Unknown Counterfactual Reserve

承接 TCFT-01 的 Unknown Reserve，

反事實系統也需要保留：

$$
\boxed{
\mathcal U_i^{CF}(t)
}
$$

表示：

> 目前生成的反事實集合不是完整世界集合。

它可以是 flag、budget reservation、adversarial search trigger 或 periodic re-expansion policy。

---

# 25. Counterfactual Surprise

如果後續事件揭示：

$$
c^*
\notin\mathcal C_i,
$$

可以定義：

$$
\boxed{
\text{Counterfactual Surprise Event}.
}
$$

其重點不是：

> 我猜錯了。

而是：

> 我甚至沒有建立這條 alternative。

---

# 26. Counterfactual Horizon Expansion

新 evidence：

$$
E_{t+1}
$$

可以使：

$$
\boxed{
\mathcal C_i(t+1)
=
Expand(
\mathcal C_i(t),
E_{t+1}
).
}
$$

也可能迫使 generator 本身修改：

$$
\boxed{
G_i^{CF}(t+1)
\neq
G_i^{CF}(t).
}
$$

---

# 27. Meta-Counterfactual Generation

第一階 generator：

$$
G_i^{CF}
$$

生成：

$$
c.
$$

更高階問題是：

> 還有什麼生成方式是我沒有使用的？

可以寫：

$$
\boxed{
G_i^{meta}:
G_i^{CF}
\rightarrow
\{G_{i,1}^{CF},G_{i,2}^{CF},\ldots\}.
}
$$

這不是要求無限 meta recursion。

而是承認 generator 本身也可能有盲點。

---

# 28. Problem Generation 與 Counterfactual Generation

問題：

$$
q
$$

決定：

$$
\mathcal C(q).
$$

如果只問：

> 如果政策 A 改成 B 會怎樣？

可能永遠不會生成：

> 如果整個政策目標本身錯了呢？

因此：

$$
\boxed{
\text{Problem Frame}
\rightarrow
\text{Counterfactual Horizon}.
}
$$

---

# 29. Frame-Locked Counterfactuals

如果所有 alternatives 都保持：

$$
F
$$

不變，

可以寫：

$$
\mathcal C_i^F.
$$

即使：

$$
|\mathcal C_i^F|
$$

很大，

仍可能漏掉：

$$
c^*
$$

因為：

$$
c^*
$$

要求修改 frame 本身。

本文稱：

$$
\boxed{
\text{Frame-Locked Counterfactual Coverage}.
}
$$

---

# 30. Frame-Breaking Counterfactual

若：

$$
c^*
$$

改變：

- objective；
- ontology；
- agent set；
- temporal scale；
- causal graph；
- representation；

則可稱：

$$
\boxed{
\text{Frame-Breaking Counterfactual}.
}
$$

這類反事實可能對時代超前尤其重要。

---

# 31. 表示系統限制 Counterfactual Horizon

若 representation：

$$
R
$$

無法表示某種關係，

則：

$$
c^*
$$

可能無法生成。

因此：

$$
\boxed{
\mathcal R_i
\rightarrow
\mathcal C_i.
}
$$

這與 TCFT-01 的 Representation-Induced Base-Space Blindness 相連。

---

# 32. Counterfactual Representation Blindness

定義：

$$
\boxed{
c^*
\in
\mathcal C_{possible}
$$

但：

$$
c^*
\notin
\mathcal C_i
$$

主要因：

$$
\mathcal R_i
$$

缺乏表示能力。

這是：

$$
\boxed{
\text{Counterfactual Representation Blindness}.
}
$$

---

# 33. 反事實與因果圖

一個 agent 的 causal graph：

$$
G_i
$$

會限制可生成 intervention。

若某條 edge：

$$
X\rightarrow Y
$$

根本不在模型裡，

agent 不會自然生成：

$$
do(X=x')
$$

對 $Y$ 的重要後果。

所以：

$$
\boxed{
\text{Causal Model Blindness}
\rightarrow
\text{Counterfactual Blindness}.
}
$$

---

# 34. 反過來，Counterfactual 可發現 Causal Gap

若反覆出現：

$$
PredictionError(c)
$$

可能提示：

$$
G_i
$$

缺少結構。

因此：

$$
\boxed{
\text{Counterfactual Failure}
\rightarrow
\text{Causal Model Revision}.
}
$$

---

# 35. Retrospective Counterfactual

典型：

> 如果過去沒有發生 $X$，結果會怎樣？

寫成：

$$
\boxed{
CF^{-}
}
$$

它主要改寫已發生歷史。

---

# 36. Prospective / Forward Counterfactual

另一類：

> 如果接下來採取 $a$，世界可能如何展開？

寫成：

$$
\boxed{
CF^{+}.
}
$$

2025 年已有工作把 forward counterfactual generation 做成金融市場 benchmark。

因此 TCFT 不宣稱 forward counterfactual 本身是新概念。

---

# 37. TCFT 的新增問題

TCFT 問：

$$
\boxed{
\text{How does an agent construct the set of forward counterfactuals
before evaluating them?}
}
$$

也就是：

$$
CF^{+}_{generation}
$$

而不只：

$$
CF^{+}_{inference}.
$$

---

# 38. Counterfactual Horizon 與 Future Base-Space

TCFT-01：

$$
\mathfrak B_i(t)
$$

是一個更一般未來底空間。

TCFT-02：

$$
\mathcal C_i(t)
$$

是其中由：

- alteration；
- intervention；
- causal simulation；
- alternative history；

生成的重要區域。

因此概念上：

$$
\boxed{
\mathcal C_i(t)
\hookrightarrow
\mathfrak B_i(t)
}
$$

但不強制把所有未來候選都寫成標準 counterfactual。

---

# 39. 反事實視界的時代差異

對兩個年代：

$$
t_0<t_1,
$$

通常：

$$
\mathcal C_{baseline}(t_0)
\neq
\mathcal C_{baseline}(t_1).
$$

因為新：

- causal knowledge；
- technology；
- language；
- simulation tools；
- data；
- AI；

會改變可生成 alternatives。

---

# 40. Temporal Counterfactual Advancement

定義候選：

$$
\boxed{
TCA_i^{CF}(t)
=
f(
\mathcal C_i(t),
\mathcal C_{B_t}(t),
QCC_i,
\Delta T,
Integrity
).
}
$$

重點是：

$$
\mathcal C_i(t)
\setminus
\mathcal C_{B_t}(t).
$$

是否包含高價值、受約束而同期 baseline 難以生成的 alternatives。

---

# 41. Collective Baseline

建立：

$$
\boxed{
\mathcal C_{B_t}^{collective}
=
\bigcup_{j=1}^{m}
\mathcal C_{B_j}(t).
}
$$

但必須 quality-filter，

避免：

$$
m\rightarrow\infty
$$

後 union 覆蓋所有亂想。

---

# 42. Quality-Filtered Baseline Horizon

定義：

$$
\boxed{
\mathcal C_{B_t}^{+}
=
\bigcup_j
\{
c\in\mathcal C_{B_j}:
Q(c)\ge\theta
\}.
}
$$

候選主體的新穎部分：

$$
\boxed{
\Delta\mathcal C_i^{+}
=
\mathcal C_i^{+}
\setminus
\mathcal C_{B_t}^{+}.
}
$$

---

# 43. Counterfactual Lead Time

若某高價值 alternative：

$$
c^*
$$

由 agent $i$ 在：

$$
t_i
$$

生成，

而 baseline 首次穩定生成在：

$$
t_B,
$$

則：

$$
\boxed{
\Delta T_i^{CF}(c^*)
=
t_B-t_i.
}
$$

但：

$$
\boxed{
\Delta T>0
}
$$

不代表它一定正確或有用。

---

# 44. Ex Ante Counterfactual Quality

在：

$$
t_i
$$

當下只能使用：

$$
K_{\le t_i}.
$$

評估：

$$
\boxed{
Q_{pre}(c).
}
$$

至少考慮：

- causal coherence；
- constraint satisfaction；
- relevance；
- discriminability；
- explicit assumptions。

---

# 45. Ex Post Counterfactual Value

後來可以額外評估：

$$
\boxed{
Q_{post}(c;t_i,t_k).
}
$$

例如：

- 是否後來成為真實政策問題；
- 是否揭示真實 failure mode；
- 是否導致新理論；
- 是否改善 decision robustness；
- 是否被實驗支持。

兩者不能混帳。

---

# 46. 歷史人物中的反事實超前

對歷史人物真正值得問的不是：

> 他是不是什麼都預見了？

而是：

> 他是否生成了同期少見、後來具有高因果或工程價值的 alternatives？

例如：

$$
\text{「如果不沿既有設計路徑，而改變基本機制？」}
$$

這類 frame-breaking counterfactual 可能比事件預言更有價值。

---

# 47. 「未來人」中的反事實測試

若某人聲稱來自未來，

除了查：

$$
PredictionHit,
$$

還可測：

$$
\boxed{
\text{Counterfactual Signature}.
}
$$

例如：

- 是否能描述「如果某技術沒有出現」的替代路徑；
- 是否理解不同政策造成的 downstream consequences；
- 是否能區分多條世界線；
- 是否提出當代 baseline 難以生成的 failure modes；
- 是否具有非線性與制度反應模型。

---

# 48. 但高 CF 不證明未來身份

即使：

$$
TCA_i^{CF}\gg0,
$$

仍然只表示：

$$
\boxed{
\text{unusual counterfactual performance}.
}
$$

不推出：

$$
\boxed{
\text{time-travel identity}.
}
$$

---

# 49. AI 時代的反事實爆炸

LLM 可以快速生成：

$$
c_1,\ldots,c_{10^4}.
$$

這使：

$$
GenerationCost\downarrow.
$$

但：

$$
EvaluationCost\uparrow.
$$

所以：

$$
\boxed{
\text{AI Counterfactual Capability}
\neq
\text{Generate More Text}.
}
$$

---

# 50. AI 需要 Counterfactual Search Policy

可以寫：

$$
\boxed{
\pi^{CF}
:
State
\rightarrow
\{
Generate,
Expand,
Prune,
Verify,
Stop
\}.
}
$$

這開始接近真正 AI-native counterfactual search。

---

# 51. Branch Value

對反事實：

$$
c,
$$

定義候選價值：

$$
\boxed{
V_{branch}(c)
=
ExpectedDecisionImpact
+
FalsificationValue
+
NoveltyValue
+
RiskValue
-
ComputeCost.
}
$$

不一定所有項目都需純量化。

---

# 52. Search 優先度

可以：

$$
\boxed{
Priority(c)
=
f(
V_{branch},
Uncertainty,
Novelty,
CoverageGap
).
}
$$

使 AI 不只是 breadth-first 或 random expansion。

---

# 53. Adversarial Counterfactual Search

如果 agent 只生成支持自己結論的 alternatives，

會形成：

$$
\text{confirmation-biased horizon}.
$$

因此需要：

$$
\boxed{
G_i^{disconfirm}
}
$$

專門生成：

> 什麼情況會讓我的結論失敗？

---

# 54. Falsification Counterfactual

定義：

$$
\boxed{
c_f
:
Conclusion
\rightarrow
Failure.
}
$$

如果 agent 無法生成任何：

$$
c_f,
$$

不代表理論無敵。

可能只代表 generator 太弱。

---

# 55. Counterfactual Closure Trap

另一個危險是：

$$
\mathcal C_i
$$

完全由自己的模型：

$$
M_i
$$

生成。

再用：

$$
M_i
$$

評估所有反事實。

形成：

$$
M_i
\rightarrow
\mathcal C_i
\rightarrow
Evaluation_{M_i}
\rightarrow
M_i.
$$

這是一種：

$$
\boxed{
\text{Counterfactual Closure Trap}.
}
$$

---

# 56. 外部異質生成器

因此成熟系統應加入：

$$
\boxed{
\mathcal C^{external}
}
$$

來源包括：

- other humans；
- other AIs；
- domain experts；
- adversarial agents；
- historical analogies；
- simulation；
- random perturbation；
- real-world anomalies。

---

# 57. Distributed Counterfactual Generation

集體可以：

$$
\boxed{
\mathcal C_{dist}
=
\bigcup_i
\mathcal C_i.
}
$$

再由高容量系統整合：

$$
\boxed{
\text{Distributed Generation}
+
\text{Central/Distributed Integration}
+
\text{Plural Validation}.
}
$$

這延續既有 Counterfactual Coverage 的治理方向。

---

# 58. 但集體也可能 Shared Blindspot

如果所有 agents 共享：

$$
R,
M,
D,
Culture,
TrainingData,
$$

則：

$$
\boxed{
\bigcup_i\mathcal C_i
}
$$

仍可能共同漏掉：

$$
c^*.
$$

所以多 agent 不自動等於多元 counterfactual horizon。

---

# 59. Diversity of Generators

比 agent 數更重要的可能是：

$$
\boxed{
Diversity(
G_1^{CF},
\ldots,
G_n^{CF}
).
}
$$

不同 generator：

- 改不同變量；
- 用不同 representation；
- 允許不同 ontology；
- 採不同 causal assumptions。

---

# 60. Counterfactual Coverage 與認知成本

總 budget：

$$
B.
$$

反事實展開成本：

$$
C_{CF}.
$$

若：

$$
C_{CF}>B,
$$

必須停止。

所以完整能力一定包含：

$$
\boxed{
\text{Counterfactual Stopping}.
}
$$

---

# 61. 邊際停止條件

對第 $k$ 個新增分支：

$$
c_k,
$$

邊際價值：

$$
\Delta V_k.
$$

邊際成本：

$$
\Delta C_k.
$$

若：

$$
\boxed{
\Delta V_k
\le
\Delta C_k
+
\Delta O_k
}
$$

其中：

$$
\Delta O_k
$$

為機會成本，

則應考慮停止或切換搜尋區域。

這將在 TCFT-04 完整處理。

---

# 62. Counterfactual Sufficiency

對特定決策：

$$
D,
$$

若新增合理 counterfactual 在高概率下不再改變決策，

可以定義一種 task-relative：

$$
\boxed{
\epsilon\text{-Counterfactual Sufficiency}.
}
$$

它不是全域完備。

只是：

> 在目前 task / budget / evidence 下，繼續擴展的預期決策收益很小。

---

# 63. Sufficiency 不是 Truth

即使：

$$
\epsilon\text{-Sufficient},
$$

仍可能存在：

$$
c^*
$$

尚未被想到。

所以：

$$
\boxed{
\text{Operational Sufficiency}
\neq
\text{Counterfactual Completeness}.
}
$$

---

# 64. 反事實視界與策略

高階策略不要求：

$$
|\mathcal C|\rightarrow\infty.
$$

反而要求：

$$
\boxed{
\text{Generate the alternatives most capable of changing the decision}.
}
$$

因此反事實 search 本身就是策略。

---

# 65. Counterfactual Sensitivity Map

對 decision：

$$
a^*,
$$

不同 perturbations：

$$
\Delta_1,\Delta_2,\ldots
$$

可以建立：

$$
\boxed{
S^{CF}(a^*)
}
$$

表示：

> 哪些變化最容易使結論翻轉？

這可能比枚舉完整世界更有效。

---

# 66. Counterfactual Gradient 類比

若系統連續可微，

可以用 sensitivity / derivative 類工具。

但一般 TCFT 問題可能：

- discrete；
- symbolic；
- relational；
- structural；
- ontology-changing。

所以本文只借用：

$$
\boxed{
\text{direction of decision sensitivity}
}
$$

作類比，不宣稱所有反事實都存在微分。

---

# 67. 反事實與動態不動點

若某結論：

$$
x_t
$$

在大量合理反事實更新後仍保留某種高階不變：

$$
I(x_{t+1})\approx I(x_t),
$$

可視為一種：

$$
\boxed{
\text{counterfactually robust dynamic invariant}.
}
$$

這與既有動態不動點思想可以形成未來接口，但本文不把兩者直接等同。

---

# 68. Counterfactual Horizon 的版本性

$$
\mathcal C_i(t)
$$

不是永久人格屬性。

它會隨：

- knowledge；
- tools；
- AI；
- memory；
- representation；
- training；
- context；

改變。

因此：

$$
\boxed{
\mathcal C_i(t)
\neq
\mathcal C_i(t+1).
}
$$

---

# 69. 能力可能被工具放大

某人：

$$
i
$$

單獨：

$$
\mathcal C_i.
$$

配 AI：

$$
\mathcal C_{i+AI}.
$$

通常：

$$
\mathcal C_{i+AI}
\neq
\mathcal C_i
\cup
\mathcal C_{AI}.
$$

因為互動會產生新分支。

---

# 70. Coupled Counterfactual Generator

定義：

$$
\boxed{
G_{H+AI}^{CF}
=
f(
H,
AI,
Protocol,
Search,
Memory,
Iteration,
Tools
).
}
$$

這才是 AI 時代較合理的研究單位。

---

# 71. Frozen-Time Counterfactual Audit

對時間：

$$
t_0,
$$

建立：

$$
K_{\le t_0}.
$$

candidate-blind baseline agents 生成：

$$
\mathcal C_{B_t}.
$$

候選主體文本／行為 recovery：

$$
\mathcal C_i.
$$

比較：

$$
\boxed{
\Delta\mathcal C_i
=
\mathcal C_i
\setminus
\mathcal C_{B_t}.
}
$$

---

# 72. 不能只看後來「成真的」反事實

反事實本來就是：

$$
\text{unrealized alternatives}.
$$

所以它的價值不要求：

$$
c
$$

真的發生。

重要的是：

- 是否合理；
- 是否能區分理論；
- 是否改善決策；
- 是否揭露風險；
- 是否提供 causal insight。

因此：

$$
\boxed{
\text{Counterfactual Value}
\neq
\text{Later Realization}.
}
$$

---

# 73. 歷史驗證的替代方式

對沒有實現的反事實，

可透過：

- simulation；
- natural experiment；
- causal model；
- comparative history；
- policy evaluation；
- mechanism evidence；
- robustness analysis；

取得不同程度支持。

---

# 74. Counterfactual Provenance

每個高價值反事實應保存：

$$
\boxed{
Prov(c)
=
(
Author,
Time,
Inputs,
Generator,
Assumptions,
Model,
Revisions
).
}
$$

否則後來很容易把：

$$
c
$$

錯誤歸因給某個人。

---

# 75. Independent Generation

如果多個互不共享答案的 agents：

$$
A_1,\ldots,A_n
$$

獨立生成同一：

$$
c^*,
$$

可以提高：

$$
\text{structural salience}.
$$

但也不證明：

$$
c^*
$$

為真。

---

# 76. Convergent Counterfactual Generation

可以研究：

$$
\boxed{
P(
c^*
\text{ independently generated}
\mid
K_{\le t}
).
}
$$

若極低但反覆出現，

可能顯示某種 deeper structural constraint。

這可成為未來 benchmark。

---

# 77. 反事實與異常人物審查

對所謂異常人物，

TCFT 不問：

> 他能不能講很多奇怪世界？

而問：

$$
\boxed{
\text{Does the agent generate high-value alternatives
that contemporaneous baselines systematically miss?}
}
$$

這更接近真正的 cognitive anomaly。

---

# 78. 多維 Counterfactual Frontier

可以保存：

$$
\boxed{
\vec C_i^{CF}
=
(
Correctness,
Depth,
Breadth,
Diversity,
Novelty,
Disconfirmation,
ReversalDetection,
Efficiency
).
}
$$

而不是單一：

$$
CFScore.
$$

---

# 79. Counterfactual Pareto Frontier

在時間 $t$：

$$
\boxed{
\mathcal F_t^{CF}
}
$$

可由多維向量形成 Pareto frontier。

因此可以存在：

- depth frontier；
- breadth frontier；
- efficiency frontier；
- reversal-detection frontier；

而沒有唯一 champion。

---

# 80. 可反證命題

## H1：Generation 與 Inference 可分離

如果給定反事實求解能力完全預測自主生成高價值反事實的能力，則 TCFT-02 不需要把兩者分成獨立軸。

---

## H2：Reversal Witness Detection 具有額外決策價值

若加入 reversal-oriented counterfactual search 不能改善決策 robustness，則其強版本應降級。

---

## H3：Quality-Adjusted Coverage 優於 Raw Breadth

若 raw count / semantic diversity 已能完全預測反事實效用，則 QCC 不需更複雜結構。

---

## H4：Generator Diversity 能降低 Shared Blindspot

若異質 generators 的 union 不比同質 generators 在 held-out counterfactuals 上有更高 coverage，則 distributed generation 的強主張受削弱。

---

## H5：Frame-Breaking Counterfactual 可被實證識別

若所有 frame-breaking alternatives 最終都可等價還原為 frame-preserving variable perturbations，則該分類不需獨立保留。

---

# 81. 實驗一：Given-CF vs Generated-CF

先測：

$$
\text{GivenCF Accuracy}.
$$

再給相同 base scenario，要求自主生成：

$$
\mathcal C_i.
$$

比較：

$$
\boxed{
\text{Inference Score}
\quad vs \quad
\text{Generation Quality}.
}
$$

檢驗兩者相關性。

---

# 82. 實驗二：Hidden Reversal Witness

設計決策題：

$$
D.
$$

存在：

$$
c^*
$$

會翻轉最佳決策。

但不主動提示。

測量：

$$
\boxed{
P(
c^*\in\mathcal C_i
).
}
$$

這比給定 $c^*$ 後求答案更能測 coverage。

---

# 83. 實驗三：Generator Diversity Ablation

比較：

- same-model multi-sample；
- heterogeneous LLMs；
- human experts；
- human-AI；
- adversarial generator。

測量 held-out reversal witness recall。

---

# 84. 實驗四：Budgeted Counterfactual Search

固定：

$$
B.
$$

比較：

- breadth-first；
- depth-first；
- random；
- value-guided；
- adversarial；
- novelty-guided；

誰在有限 budget 下找到更多高價值：

$$
c^*.
$$

---

# 85. 實驗五：Historical Counterfactual Reconstruction

選歷史決策節點：

$$
H_t.
$$

凍結當時資料。

讓不同 agents 生成：

$$
\mathcal C.
$$

再和：

- 後來學術反事實；
- 歷史比較研究；
- subsequent failure modes；

做對照。

---

# 86. 實驗六：Problem-Frame Ablation

固定 evidence。

Group A 只能在既有 frame 變動 parameters。

Group B 可以修改：

- objective；
- ontology；
- actor set；
- time scale。

比較是否更容易找到 reversal witness。

---

# 87. 與 TCFT-03 的接口

TCFT-02 仍然允許：

$$
c
$$

被當成外部 alternative。

下一篇加入：

$$
\boxed{
\text{reasoner's own belief, prediction, or action}
}
$$

作為世界中的 endogenous variable。

因此：

$$
\boxed{
\mathcal C_i
\rightarrow
\mathcal C_i^{reflexive}.
}
$$

---

# 88. 反身性反事實

最小例子：

$$
\boxed{
\text{If I believe/publish prediction }p,
\text{ how does the world change?}
}
$$

也就是：

$$
W_{t+1}
=
F(
W_t,
Prediction_t,
AgentResponse_t
).
$$

這將是 Paper 03 的核心。

---

# 89. 與 TCFT-04 的接口

Counterfactual Horizon 不可能無限展開。

所以 Paper 04 將處理：

$$
\boxed{
\text{Reasoning Allocation}
}
$$

包括：

- 何時深入；
- 何時擴張；
- 何時切換；
- 何時停止；
- 何時把資源轉向其他 agent / domain。

---

# 90. 與 TCFT-05 的接口

若聲稱：

> 某人在 1950 年能想到別人想不到的反事實。

必須用：

$$
\boxed{
K_{\le1950}
}
$$

做 Frozen-Time audit。

不能讓 2026 的因果知識偷渡回去。

---

# 91. 侷限

第一，反事實視界未必能被顯式枚舉；它可能是 implicit generative capacity。

第二， $\mathcal C_{rel}$ 在真實問題中通常未知，因此「覆蓋率」需要 benchmark-specific operationalization。

第三，反事實 causal validity 可能依賴有爭議的模型。

第四，counterfactual diversity metrics 可能被表面語言差異欺騙。

第五，frame-breaking 與 frame-preserving 的邊界可能 observer-relative。

第六，高 breadth 容易被 AI 大量生成灌水。

第七，reversal witness 的 utility function 本身可能有爭議。

第八，歷史 counterfactual 很難得到 ground truth。

第九，未生成反事實永遠存在 epistemic possibility，因此 TCFT 不宣稱 complete coverage。

第十，強反事實能力不是人格、道德或政治權威證明。

---

# 92. 結論

反事實推理最容易被簡化為：

$$
\boxed{
\text{Given }c,
\text{ infer }Y.
}
$$

但 TCFT-02 把問題往前移：

$$
\boxed{
\text{Where did }c\text{ come from?}
}
$$

真正的反事實能力至少有：

$$
\boxed{
\text{Correctness},
\text{Depth},
\text{Breadth},
\text{Coverage},
\text{Strategic Sufficiency}.
}
$$

而它們不能互相取代。

一個 agent 可以：

- 算得很深但想得很窄；
- 想得很廣但沒有因果約束；
- 對每個給定反事實都答對，卻漏掉最重要的 alternative；
- 生成很多 alternatives，卻沒有一個能改變決策。

所以：

$$
\boxed{
\text{Counterfactual Intelligence}
\neq
\text{Counterfactual Quantity}.
}
$$

更成熟的目標是：

$$
\boxed{
\text{bounded, quality-adjusted, decision-relevant counterfactual coverage}.
}
$$

而最重要的 failure 之一是：

$$
\boxed{
c^*
\notin
\mathcal C_i
}
$$

且：

$$
c^*
$$

其實是一個：

$$
\boxed{
\text{Reversal Witness}.
}
$$

也就是：

> 你不是把這個世界算錯了。

而是你從來沒有想到這個世界。

這就是反事實視界真正值得研究的原因。

在 TCFT 中，時代超前也因此獲得另一種定義：

$$
\boxed{
\text{某個存在比同期基準更早生成了
後來被證明具有高因果、決策或理論價值的未發生世界。}
}
$$

這仍然不是預言身份，不是英雄排名，也不保證那些 alternatives 全部正確。

它只是意味著：

$$
\boxed{
\text{the agent's counterfactual horizon extended farther
into a valuable region of unrealized possibility.}
}
$$

而下一篇將加入真正困難的那一層：

$$
\boxed{
\text{如果推理本身會改變世界，
那麼反事實生成器是否也必須把自己放進反事實？}
}
$$

這就是 TCFT-03 的反身性推理。

---

# References

1. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press.
2. Pearl, J., & Mackenzie, D. (2018). *The Book of Why*. Basic Books.
3. Byrne, R. M. J. (2016). Counterfactual Thought. *Annual Review of Psychology*, 67, 135–157. DOI: 10.1146/annurev-psych-122414-033249.
4. Roese, N. J., & Epstude, K. (2017). The Functional Theory of Counterfactual Thinking: New Evidence, New Challenges, New Insights. *Advances in Experimental Social Psychology*, 56, 1–79. DOI: 10.1016/bs.aesp.2017.02.001.
5. Gerstenberg, T. (2024). Counterfactual simulation in causal cognition. *Trends in Cognitive Sciences*, 28(10), 924–936. DOI: 10.1016/j.tics.2024.04.012.
6. Chen, Y., Singh, V. K., Ma, J., & Tang, R. (2025). CounterBench: A Benchmark for Counterfactuals Reasoning in Large Language Models. arXiv:2502.11008.
7. Roewer-Després, F., Feng, J., Zhu, Z., & Rudzicz, F. (2025). ACCORD: Closing the Commonsense Measurability Gap. *NAACL 2025*, 3799–3829. DOI: 10.18653/v1/2025.naacl-long.193.
8. Ong, K., Mao, R., Varshney, D., Liang, P. P., Cambria, E., & Mengaldo, G. (2025). Deriving Strategic Market Insights with Large Language Models: A Benchmark for Forward Counterfactual Generation. *EMNLP 2025*, 11411–11434. DOI: 10.18653/v1/2025.emnlp-main.575.
9. Phillips, J., Morris, A., & Cushman, F. (2019). How We Know What Not To Think. *Trends in Cognitive Sciences*, 23(12), 1026–1040.
10. Neo.K. (2026). *反事實覆蓋度：哲人王必須吞下多少個沒有發生的世界？* EveMissLab.
11. Neo.K. (2026). *TCFT-00｜超前認知不是預言：時代認知前沿的問題設定*. EveMissLab.
12. Neo.K. (2026). *TCFT-01｜未來底空間選擇：想像力、候選世界與問題先行*. EveMissLab.
13. Neo.K. (2026). *Cognitive Operator-Domain Theory (CODT) Series 01–10*. EveMissLab.

---

# Canonical Note

本文件正式原始碼使用 UTF-8。

數學原始碼只使用 canonical delimiters：

- inline math：` $...$ `
- display math：`$$...$$`

不進行 unicode_escape 類 round-trip；不把 LaTeX 轉為 Unicode 數學字元後再作 canonical source；不以聊天 rendering view 作為正式原稿。
