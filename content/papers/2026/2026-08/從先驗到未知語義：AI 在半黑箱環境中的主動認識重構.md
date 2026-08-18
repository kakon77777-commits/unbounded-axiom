---
title: "從先驗到未知語義：AI 在半黑箱環境中的主動認識重構"
english_title: "From Priors to Unknown Semantics: Active Epistemic Reconstruction by AI in Semi-Black-Box Environments"
series: "AI Epistemic Reconstruction Series"
paper: "03"
author: "Neo.K"
date: "2026-08-14"
version: "v0.1"
document_type: "Research Paper / Formalization-and-Method Paper"
language: "zh-Hant"
status: "Research Draft"
---

# 從先驗到未知語義：AI 在半黑箱環境中的主動認識重構

## From Priors to Unknown Semantics: Active Epistemic Reconstruction by AI in Semi-Black-Box Environments

**作者：Neo.K**  
**系列：AI Epistemic Reconstruction Series — Paper 03**  
**版本：v0.1**  
**日期：2026 年 8 月 14 日**

---

## 摘要

當 AI 面對一個半黑箱系統時，它通常並非真正「零先驗」：它可能已掌握程式語言、作業系統、CPU、檔案格式、統計推論、逆向工程與一般領域知識，也可能能搜尋到舊 FAQ、金手指、技術文件與前人留下的弱標註。然而，這些知識不等於特定 target build 的局部真值。一個今天才由本地 runtime 產生的 save diff、一個特定版本才存在的 hidden flag、一個重新編譯後被刻意改變的 threshold，並不能可靠地由既有權重或公開語料直接取得。

本文提出「**主動認識重構**」（Active Epistemic Reconstruction, AER）框架，用來描述 AI 如何從通用先驗、歷史先驗與現場新證據出發，逐步重建半黑箱系統的表示域、語義域與判定域。其核心不是一次性猜測，而是反覆執行：

$$
\boxed{
\text{Prior}
\rightarrow
\text{Hypothesis Set}
\rightarrow
\text{Experiment Selection}
\rightarrow
\text{Fresh Observation}
\rightarrow
\text{Constraint}
\rightarrow
\text{Epistemic Update}
}
$$

本文將可用資訊拆為三類：

$$
\boxed{
K_t
=
K_{\mathrm{general}}
\cup
K_{\mathrm{historical}}
\cup
E_{\mathrm{fresh},t}
}
$$

其中：

- $K_{\mathrm{general}}$：通用工具與領域知識；
- $K_{\mathrm{historical}}$：前人留下、但未對 target build 驗證的歷史先驗；
- $E_{\mathrm{fresh},t}$：當前 Agent 透過 action 在本地／實驗環境中新產生的證據。

在此框架下，「模型是否記得答案」與「系統是否能主動恢復答案」可以被部分拆開。歷史資料可以作為 prior，但必須經 target-specific intervention、negative control、reload、replication 與 behavioral validation 後，才能提升為較高信心的 canonical mapping。

本文結合 query-by-committee、active learning、Bayesian optimal experimental design 與近年的自主科學 Agent 工作，提出以預期資訊增益、候選空間收縮與成本正規化為核心的研究策略：

$$
a_t^*
=
\arg\max_{a\in\mathcal A}
\frac{
\mathbb E[
H(\mathcal H_t)-H(\mathcal H_{t+1})
\mid a
]
}{
C(a)
}.
$$

最後，本文提出一套 semi-black-box benchmark 方法：允許 AI 使用完整通用知識與公開工具，但隱藏 target-local semantics，並透過 fresh evidence、private mutation、holdout mapping 與行為重實作來判斷系統是否真正具有 active epistemic reconstruction 能力。

**關鍵詞：** Active Epistemic Reconstruction, Active Learning, Experimental Design, AI Agents, Black-Box Systems, Reverse Engineering, Information Gain, Fresh Evidence, Historical Prior, Scientific Discovery

---

# 1. 問題：AI 到底是在「知道」還是在「重新發現」？

大型模型的能力評估有一個長期難題：

> 當模型回答正確時，我們如何知道答案是現場推導出來的，還是訓練資料中曾經出現過？

對已公開：

- 數學題；
- 程式題；
- benchmark；
- 論文；
- 攻略；
- Stack Overflow；
- GitHub repository；

這個問題尤其難。

如果正確答案早已存在 corpus，最終輸出：

$$
y^*
$$

本身無法區分：

$$
\text{latent retrieval}
$$

與：

$$
\text{active reconstruction}.
$$

---

# 2. 半黑箱環境提供另一種研究條件

考慮一個特定 binary：

$$
G^*.
$$

Agent 知道：

- DOS；
- x86；
- little-endian；
- save file；
- dynamic tracing；
- binary diff；
- script automation。

但不知道：

$$
\Sigma^*
$$

即 target-specific semantic specification。

此時：

$$
K_{\mathrm{general}}
$$

很強，

但：

$$
K_{\mathrm{target}}
$$

仍不完整。

這種環境特別適合研究：

> **AI 能否把一般方法真正轉化為局部新知識？**

---

# 3. 與 Paper 01、Paper 02 的接口

Paper 01 定義：

$$
\mathcal A=(M,T,E,S,V,\Pi),
$$

說明現代 Agent 是模型、工具、環境、持久狀態與驗證器形成的混合認識系統。

Paper 02 定義：

$$
B
\xrightarrow{\rho}
R
\xrightarrow{\delta}
S
\xrightarrow{J}
O,
$$

說明 bits 並不自帶語義。

Paper 03 的問題是：

> 如果 $\rho^*,\delta^*,J^*$ 不知道，Agent 怎麼找到它們？

---

# 4. 定義：Active Epistemic Reconstruction

## Definition 1 — Target Semantic Structure

令：

$$
\Theta^*
=
(\rho^*,\delta^*,J^*)
$$

表示 target system 的未知語義結構。

其中：

- $\rho^*$：representation mapping；
- $\delta^*$：semantic definition mapping；
- $J^*$：judgment / transition structure。

---

## Definition 2 — Hypothesis Space

Agent 維持候選：

$$
\mathcal H_t
=
\{h_1,\ldots,h_n\}.
$$

每個：

$$
h_i
=
(\rho_i,\delta_i,J_i).
$$

---

## Definition 3 — Action

Agent 可以選擇：

$$
a_t\in\mathcal A.
$$

例如：

- 修改一個遊戲狀態；
- 執行一段程式；
- 新增一個 breakpoint；
- 做一次 save；
- 重載；
- 查詢舊文件；
- 改變一個 input；
- 重複同一個實驗。

---

## Definition 4 — Observation

環境返回：

$$
o_{t+1}
=
E(\Theta^*,a_t,\xi_t),
$$

其中：

$$
\xi_t
$$

代表可能的 hidden state / noise / randomness。

---

## Definition 5 — Epistemic Update

Agent 由：

$$
U:
(\mathcal H_t,K_t,a_t,o_{t+1})
\rightarrow
(\mathcal H_{t+1},K_{t+1})
$$

更新知識。

---

## Definition 6 — Active Epistemic Reconstruction

若 Agent 不只被動接收固定 evidence，而能依目前 uncertainty 主動選 action，取得對 target semantics 有判別力的新 observation，則稱此過程為：

$$
\boxed{
\operatorname{AER}
}
$$

---

# 5. AER 的最小閉環

```text
Existing Knowledge
      ↓
Hypothesis Set
      ↓
Choose Next Experiment
      ↓
Act on External System
      ↓
Receive Fresh Evidence
      ↓
Validate / Contradict
      ↓
Update Confidence
      ↓
Choose Again
```

形式：

$$
K_t
\rightarrow
\mathcal H_t
\rightarrow
a_t
\rightarrow
o_{t+1}
\rightarrow
K_{t+1}.
$$

---

# 6. 三種資訊來源

本文將 Agent 的 epistemic input 分成三類。

## 6.1 General Prior

$$
K_G
$$

包括：

- CPU architecture；
- operating system；
- language semantics；
- standard algorithms；
- debugging knowledge；
- statistics；
- scientific method；
- general game design patterns。

這些知識不是作弊。

它們相當於研究者的專業訓練。

---

## 6.2 Historical Prior

$$
K_H
$$

包括：

- old FAQ；
- cheat table；
- HEX map；
- save editor；
- modding documentation；
- old BBS notes；
- fan tools；
- previous reverse-engineering reports。

這些資訊通常：

- 有價值；
- 但可能版本錯配；
- 缺乏 provenance；
- 缺少 negative control；
- 不一定描述 target build。

所以：

$$
K_H
\neq
\text{Truth}.
$$

---

## 6.3 Fresh Evidence

$$
E_F(t)
$$

是在當前研究過程中，經 action 新產生的 evidence。

例如：

```text
2026-08-14:
load local baseline
→ perform action A
→ create new save S'
→ calculate byte diff
```

這份：

$$
S'
$$

在 action 發生前甚至不存在。

因此它不能被簡單解釋為：

> 訓練語料中的直接答案。

---

# 7. Epistemic Composition

因此：

$$
\boxed{
K_t
=
K_G
\cup
K_H
\cup
E_F(0:t)
}
$$

Agent 的能力不應只問：

> 它有多少 prior？

也應問：

> 它能不能把 prior 轉成能被新 evidence 驗證的 hypothesis？

---

# 8. Latent Retrieval 與 Active Reconstruction

定義兩個理想化極端。

## Latent Retrieval

$$
x
\rightarrow
M
\rightarrow
y.
$$

答案已高度存在於參數／context 中。

---

## Active Reconstruction

$$
x
\rightarrow
H_0
\rightarrow
a_0
\rightarrow
E_1
\rightarrow
H_1
\rightarrow
a_1
\rightarrow
\cdots
\rightarrow
H_T.
$$

答案依賴多輪外部 evidence。

---

# 9. 真實系統通常是混合

實際 Agent：

$$
\boxed{
\text{Retrieval}
+
\text{Prior Reasoning}
+
\text{Experiment}
+
\text{Reconstruction}
}
$$

不是純二分。

所以 benchmark 應測：

> 最終結論中有多少關鍵 target-specific claim 必須由 fresh evidence 支持？

---

# 10. Historical Prior 的正確地位

假設舊 FAQ 說：

$$
h:
\quad
\texttt{offset 0x50}=\text{Stress}.
$$

可提高 prior：

$$
P(h).
$$

但不能直接宣告：

$$
P(h)=1.
$$

應有：

$$
P(h\mid E_{\mathrm{target}}).
$$

---

# 11. Prior-Assisted Falsification

最有效策略通常不是：

> 忽略前人資料，從零猜。

也不是：

> 相信前人資料。

而是：

$$
\boxed{
\text{Historical Prior}
\rightarrow
\text{Target-Specific Falsification}
}
$$

---

# 12. Weak Label

歷史資料應進資料庫：

```yaml
claim:
  source_type: historical_prior
  semantic_label: stress
  candidate_offset: 0x50
  target_build_verified: false
```

而不是：

```yaml
canonical:
  stress: 0x50
```

---

# 13. Promotion Ladder

建議 epistemic state：

```text
unknown
↓
historical_prior
↓
hypothesis
↓
partially_verified
↓
verified
```

失敗：

```text
invalidated
```

---

# 14. Active Learning 的歷史接口

Active learning 的核心問題是：

> 如果 learner 可以選下一筆資料，應該選哪一筆？

Query-by-committee 提出：

> 在候選模型／committee disagreement 最大的地方詢問 label。

如果 query 具有持續的正信息增益，可使 prediction error 隨 query 數量快速下降。

這一思想和 AER 的結構高度相容。

---

# 15. 從「選資料」到「選實驗」

傳統 active learning：

$$
x_t^*
=
\arg\max_x
U(x).
$$

AER 則是：

$$
a_t^*
=
\arg\max_a
U(a).
$$

action 不只是一個 query point。

可以是：

- 一段完整操作序列；
- reboot；
- controlled intervention；
- trace；
- compare；
- cross-version experiment。

---

# 16. Information Gain

若 hypothesis entropy：

$$
H(\mathcal H_t)
$$

可以估計，

則 action $a$ 的 expected information gain：

$$
IG(a)
=
H(\mathcal H_t)
-
\mathbb E[
H(\mathcal H_{t+1})
\mid a
].
$$

---

# 17. Cost-Normalized Information Gain

真實 Agent 的實驗成本不同。

例如：

```text
read 2 bytes
```

很便宜。

但：

```text
boot DOS
→ create new game
→ play 20 minutes
→ save
```

很昂貴。

所以定義：

$$
\boxed{
U(a)
=
\frac{IG(a)}{C(a)}
}
$$

---

# 18. 多維成本

令：

$$
C(a)
=
\lambda_T T(a)
+
\lambda_K K(a)
+
\lambda_C C_{\mathrm{compute}}(a)
+
\lambda_R R_{\mathrm{risk}}(a).
$$

其中：

- $T$：時間；
- $K$：token / context；
- $C_{\mathrm{compute}}$：運算；
- $R$：風險／破壞性。

---

# 19. 最佳下一實驗

因此：

$$
\boxed{
a_t^*
=
\arg\max_{a\in\mathcal A}
\frac{
\mathbb E[
H(\mathcal H_t)-H(\mathcal H_{t+1})
\mid a
]
}{
C(a)
}
}
$$

這是本文最核心的 experiment-selection objective。

---

# 20. 不需要精確算 entropy 才能工作

真實 Agent 可以使用 heuristic approximation：

```text
Does this test separate multiple live hypotheses?
Is the result externally observable?
Is it cheap?
Can it be repeated?
Does it have a negative control?
```

也就是：

$$
\widehat{IG}(a).
$$

---

# 21. Discriminating Experiment

若兩假說：

$$
h_1,h_2
$$

對某 action：

$$
h_1(a)\neq h_2(a),
$$

則 $a$ 具有判別力。

理想：

$$
a^*
=
\arg\max_a
d(
h_i(a),
h_j(a)
).
$$

---

# 22. Running Case：一個未知 byte

假設：

```text
offset 0x0334:
00 → 64
```

候選：

```text
H1 = schedule state
H2 = transient UI state
H3 = RNG state
H4 = persistent gameplay flag
```

---

# 23. 低品質實驗

```text
再玩一次看看
```

可能同時改很多因素。

結果：

$$
o
$$

難以區分 $H_1$ ～ $H_4$。

---

# 24. 高品質實驗

```text
load same baseline
→ do nothing
→ save
```

如果 byte 不變，

可降低某些：

> save-time automatic mutation

假說。

---

# 25. 再一個高品質實驗

```text
load same baseline
→ open UI
→ cancel
→ save
```

可以專門測：

$$
H_2.
$$

---

# 26. 再一個

```text
load same baseline
→ commit one fixed schedule
→ save
```

可以針對：

$$
H_1/H_4
$$

取得新 evidence。

---

# 27. 實驗設計的核心不是「多」，而是「分離」

如果 100 次測試都無法分離候選：

$$
IG\approx0.
$$

而一個精準 intervention 排除 80% hypotheses：

$$
IG\gg0.
$$

所以：

$$
\boxed{
\text{Experiment Count}
\neq
\text{Research Quality}
}
$$

---

# 28. AER 與 brute force 的區別

Brute force：

$$
\forall a\in\mathcal A,\quad \text{run}(a).
$$

AER：

$$
a_t
=
\pi(\mathcal H_t,K_t).
$$

利用目前 uncertainty 選擇下一步。

---

# 29. Scientific Method 的 Agent 化

AER 可寫成：

```text
Observation
→ Hypothesis
→ Experimental Design
→ Intervention
→ Measurement
→ Falsification / Update
→ Replication
```

這不是說 Agent 已等於完整科學家。

而是：

> 科學方法中的某些可操作結構可以被 Agent 化。

---

# 30. 近年的自動科學 Agent

AI Scientist 類工作已把：

- idea generation；
- code writing；
- experiment execution；
- result analysis；
- manuscript generation；

串成長流程。

這證明：

$$
\text{LLM}
+
\text{experiment runtime}
$$

可以支撐多階段研究。

---

# 31. Robin：假說與真實資料的閉環

2026 年的 Robin 系統進一步將：

- literature search；
- hypothesis generation；
- experimental result analysis；
- updated hypothesis；

接成連續 feedback loop。

它展示一個重要現象：

> AI-generated hypothesis 可以被後續實驗資料反過來改寫。

這與 AER 的：

$$
H_t\rightarrow E_{t+1}\rightarrow H_{t+1}
$$

直接一致。

---

# 32. AER 不限於自然科學

適用：

- reverse engineering；
- debugging；
- cyber defense；
- scientific experimentation；
- model identification；
- game archaeology；
- API discovery；
- unknown database schema；
- hardware probing。

---

# 33. Semi-Black-Box 定義

完全 black box：

> 只能看 input / output。

White box：

> 完整 source / schema / semantics 已知。

Semi-black-box：

> 可取得部分 internal artifact、runtime behavior 或歷史資料，但核心 mapping 不完整。

形式：

$$
I_{\mathrm{known}}
\subset
I_{\mathrm{system}},
$$

且：

$$
I_{\mathrm{unknown}}
\neq\varnothing.
$$

---

# 34. 為什麼 semi-black-box 特別適合 AI benchmark

因為可以同時允許：

- tool use；
- general knowledge；
- search；
- code；
- experimentation；

又保持：

$$
\Theta^*
$$

局部未知。

---

# 35. Fresh Evidence Criterion

若 evidence：

$$
e_t
$$

滿足：

1. 在 task instance 建立前不存在；
2. 由當前 target runtime / mutation 產生；
3. 可保存；
4. 可重播或外部驗證；

則稱：

$$
e_t
$$

為 **fresh evidence**。

---

# 36. Fresh Evidence 與 Novel Knowledge

Fresh evidence 本身不保證：

> 結論一定 novel。

但可以大幅降低：

> 這個特定 observation 是模型直接背到的

可能性。

---

# 37. Private Mutation

建立公開程序：

$$
G.
$$

測試時生成：

$$
G'=M_\phi(G),
$$

例如：

- threshold 100 → 117；
- field offset 重排；
- constant 改變；
- hidden flag mapping 改變。

只有 benchmark generator 知道：

$$
\phi.
$$

---

# 38. Memorization Trap

如果公開攻略：

```text
threshold = 100
```

而 private mutation：

```text
threshold = 117
```

模型若直接回答 100：

> 可能使用了 historical prior，但沒有重建 target-local semantics。

---

# 39. Reconstruction Success

若 Agent 經 fresh experiment 發現：

$$
117,
$$

才支持：

$$
\text{target-specific reconstruction}.
$$

---

# 40. Semantic Permutation

另一種 benchmark：

$$
P:
\text{offsets}
\rightarrow
\text{permuted offsets}.
$$

保持規則語義，但改 representation。

---

# 41. Behavioral Mutation

也可以保持 representation，改：

$$
J.
$$

例如：

```text
event threshold:
100 → 117
```

這測：

> Agent 是否只找 field，還是能恢復 judgment rule。

---

# 42. 三層 Holdout

## Representation Holdout

未知：

$$
\rho^*.
$$

## Semantic Holdout

未知：

$$
\delta^*.
$$

## Judgment Holdout

未知：

$$
J^*.
$$

---

# 43. AER Benchmark Score

定義：

$$
Score
=
w_\rho A_\rho
+
w_\delta A_\delta
+
w_J A_J
+
w_F F
+
w_C C.
$$

其中：

- $A_\rho$：representation recovery；
- $A_\delta$：semantic mapping；
- $A_J$：rule recovery；
- $F$：falsification quality；
- $C$：confidence calibration。

---

# 44. 只看 final answer 不夠

應保存：

```text
initial hypotheses
experiments selected
fresh evidence
invalidated hypotheses
confidence changes
final mapping
```

這是：

$$
\boxed{
\text{Epistemic Trace}
}
$$

---

# 45. 不需要保存私有 Chain-of-Thought

AER trace 不要求模型曝露 hidden reasoning。

只需 externalizable record：

```yaml
decision:
  hypotheses_considered:
  selected_experiment:
  expected_discrimination:
  observation:
  verdict:
  epistemic_update:
```

這是可稽核研究紀錄。

---

# 46. Negative Control

任何高信心 semantic mapping 都應問：

> 如果改變其他變量，candidate field 是否也跟著變？

這能避免：

- global checksum；
- time counter；
- generic dirty flag；

被誤認成目標 state。

---

# 47. Positive Intervention

如果：

$$
x=\text{Stress},
$$

則設計：

$$
do(a):x\rightarrow x+\Delta.
$$

期待：

$$
b_x
$$

出現可重現變動。

---

# 48. Independent Reload

save mapping 應：

```text
save
→ terminate process
→ restart
→ reload
```

避免只驗證 transient runtime state。

---

# 49. Replication

單次：

$$
E_1
$$

容易被：

- RNG；
- timing；
- accidental input；
- hidden state；

污染。

所以：

$$
E_1,E_2,\ldots,E_k
$$

應在相同 protocol 下獨立重複。

---

# 50. Protocol Freezing

實驗前固定：

```yaml
protocol:
  baseline_hash:
  initial_visible_state:
  action_sequence:
  save_slot:
  stop_condition:
  expected_observation:
```

避免看到結果後改 hypothesis definition。

---

# 51. Exclusion Log

失敗操作：

```text
clicked wrong menu
entered church
donated 100 gold
```

不應刪掉。

應：

```yaml
status: excluded
reason: protocol_violation
```

保留 provenance，但禁止用作核心 evidence。

---

# 52. AER 的 epistemic hygiene

高品質 AER 需要：

- positive evidence；
- negative evidence；
- excluded runs；
- contradictions；
- uncertainty；
- provenance。

不是只保存成功故事。

---

# 53. Confidence 不是 decoration

每個 claim：

$$
c_i\in[0,1].
$$

但 confidence 必須受 evidence update 約束。

不能：

> AI 覺得很像 → 0.99。

---

# 54. Evidence Classes

```text
E0 anecdotal
E1 historical prior
E2 static local evidence
E3 controlled intervention
E4 replicated intervention
E5 behavioral reconstruction
```

可用來映射 confidence ceiling。

---

# 55. Evidence Ceiling

例如：

```text
historical prior only
```

即使來源很可信，也可規定：

$$
c\le0.7
$$

直到 target-specific experiment。

---

# 56. Behavioral Reconstruction

最高強度驗證之一：

Agent 建立：

$$
\hat G.
$$

對 unseen inputs：

$$
O_{\hat G}(x)
\approx
O_G(x).
$$

這比單純 field label 更強。

---

# 57. Reconstruction as Compression

如果原研究產生：

$$
E
$$

大量 traces，

最後得到：

$$
\hat\Theta.
$$

則：

$$
\hat\Theta
$$

是對 evidence 的一種 semantic compression。

---

# 58. 但是壓縮必須保留 pointer

Canonical claim：

```yaml
stress:
  offset: 0x50
```

應指回：

```text
experiment_17
experiment_23
negative_control_4
historical_source_2
```

---

# 59. 因此 AER 的產品不是一篇報告

真正成果：

$$
\boxed{
\text{Semantic Model}
+
\text{Evidence Graph}
+
\text{Replay Corpus}
}
$$

---

# 60. Long-Horizon Agent 的核心問題

執行 12 小時不代表研究好。

可能是：

$$
\text{Looping}.
$$

所以必須測：

$$
\Delta H / \Delta C.
$$

---

# 61. Epistemic Progress Rate

定義：

$$
r_E(t)
=
-\frac{dH(\mathcal H_t)}{dC}.
$$

若：

$$
r_E(t)\approx0
$$

持續很久，

應考慮：

- 換實驗；
- 搜尋外部 prior；
- 壓縮 context；
- 停止。

---

# 62. Stop Criterion

可以在：

$$
\max_a
\frac{IG(a)}{C(a)}
<
\epsilon
$$

時停止。

或：

$$
P(h^*\mid E)>\tau.
$$

---

# 63. Unknown 是合法終點

如果目前 evidence 無法分辨：

$$
h_1,h_2,
$$

正確結果是：

```text
UNKNOWN
```

而不是強迫模型選一個。

---

# 64. AER 與 hallucination

AER 不會消除 hallucination。

但可以把 hallucination 變成：

$$
\text{testable hypothesis}.
$$

如果：

$$
V(h)=fail,
$$

則將其淘汰。

---

# 65. 這是一個功能上的巨大改變

純 hallucination：

```text
wrong claim
```

AER：

```text
wrong hypothesis
→ test
→ contradiction
→ invalidated
```

錯誤被納入研究流程。

---

# 66. AER 的失敗模式一：錯誤 domain framing

如果 Agent 一開始候選空間：

$$
\mathcal H_0
$$

沒有包含真實：

$$
h^*,
$$

再多 evidence 也可能找不到答案。

---

# 67. 失敗模式二：不可識別性

若：

$$
\forall a\in\mathcal A,
\quad
h_1(a)=h_2(a),
$$

則在允許的 observation contract 下：

$$
h_1,h_2
$$

不可識別。

---

# 68. Identifiability

定義：

若：

$$
\exists a:
h_i(a)\neq h_j(a),
$$

則兩候選在 action set $\mathcal A$ 下可區分。

---

# 69. 失敗模式三：工具錯誤

如果：

$$
T
$$

的 parser / diff / debugger 有 bug，

Agent 可能建立錯 evidence。

所以重要 observation 最好：

- independent implementation；
- hash；
- redundant check。

---

# 70. 失敗模式四：環境 nondeterminism

若：

$$
\xi_t
$$

不可控制，

應增加：

- seed；
- repeated trials；
- confidence interval；
- state reset。

---

# 71. 失敗模式五：Agent 過度嚴謹

可能：

> 每個 byte 都跑 20 次實驗。

這會使：

$$
C(a)\rightarrow\infty.
$$

研究效率崩潰。

---

# 72. 嚴謹不等於重複最大化

應根據：

$$
IG/C
$$

選擇 replication depth。

---

# 73. Algorithmization

當某一實驗 protocol 已穩定：

```text
load
save
diff
reload
```

應轉成 deterministic script。

讓 LLM 不再手動做重複 UI 操作。

---

# 74. Human / AI / Algorithm 三層分工

## Human

- 問題定義；
- 價值；
- scope；
- 高層異常判斷。

## AI Agent

- hypothesis；
- experiment planning；
- cross-domain interpretation。

## Algorithm

- deterministic repetition；
- hash；
- diff；
- replay；
- batch execution。

---

# 75. AER 自我加速

第一次：

$$
\Pi_1
$$

可能很長。

將有效 protocol 保存後：

$$
\Pi_2
$$

變短。

所以：

$$
|\Pi_{n+1}|<|\Pi_n|
$$

在相似 task family 中可能成立。

---

# 76. Meta-AER

當 Agent 不只重建 target，

還重建：

> 如何更快重建 target。

即：

$$
\operatorname{AER}
\rightarrow
\operatorname{MetaAER}.
$$

這會在 Paper 06 展開。

---

# 77. Historical Prior 也可以被學習

如果某來源：

$$
S_i
$$

過去 100 個 claims：

$$
95
$$

個被驗證，

可提高其 source reliability。

但仍不能取消 target-specific test。

---

# 78. Source Reliability

$$
R(S_i)
=
P(
\text{claim correct}
\mid
S_i
).
$$

此值用於：

$$
P(h)
$$

而不是當作：

$$
P(h)=1.
$$

---

# 79. Cross-Version Prior

版本 A 已 verified：

$$
h_A.
$$

版本 B 可以把它當 prior：

$$
P(h_B\approx h_A)
$$

但不能假設：

$$
h_B=h_A.
$$

---

# 80. Version Distance

可估：

$$
d(V_A,V_B)
$$

越近，

historical prior weight 越高。

---

# 81. AER 對軟體考古的特殊價值

Legacy software 常：

- source missing；
- docs incomplete；
- formats custom；
- fan knowledge scattered。

AER 能把：

$$
\text{Scattered Prior}
+
\text{Executable Artifact}
$$

轉成：

$$
\text{Evidence-Backed Specification}.
$$

---

# 82. 對科學研究的類比

未知程式：

$$
G
$$

像自然系統。

Agent 只能：

- intervention；
- observe；
- hypothesize。

因此：

$$
\text{software archaeology}
$$

可視為一種 controlled scientific environment。

---

# 83. 差別：軟體世界通常更可重播

自然世界的 reset 很昂貴。

但 emulator：

```text
snapshot
→ reset
```

成本低。

所以 software black box 是非常好的 Agent epistemology sandbox。

---

# 84. Ground Truth 最終可能可取得

benchmark 作者可以保留：

- source code；
- schema；
- hidden mapping。

因此可以真正評估：

$$
\hat\Theta
$$

和：

$$
\Theta^*.
$$

---

# 85. 這比很多開放科學 benchmark 更乾淨

因為真實科學問題的：

$$
\Theta^*
$$

常不知道。

Legacy synthetic benchmark 則可以：

> 對 Agent 黑箱，對 evaluator 白箱。

---

# 86. Contamination-Resistant Benchmark

理想設計：

```text
Public:
  ISA
  tools
  general docs

Private:
  binary instance
  state mapping
  constants
  mutation seed
```

---

# 87. Benchmark 生成

$$
G_\phi
=
Mutate(G,\phi).
$$

每個受測 Agent：

$$
\phi
$$

不同。

降低 benchmark answer leakage。

---

# 88. Online Evidence

評分時禁止：

> 直接讀 hidden source。

但允許：

- execute；
- inspect output；
- save；
- trace；
- disassemble。

即：

> 允許研究，不允許看答案。

---

# 89. AER Success Definition

成功不必：

$$
\hat\Theta=\Theta^*
$$

bit-level 完全一樣。

可用 observation contract：

$$
O(\hat\Theta)
\approx
O(\Theta^*).
$$

---

# 90. Partial Credit

```text
representation recovered
semantic mapping recovered
rule recovered
but RNG unresolved
```

應得到部分分數，而不是全錯。

---

# 91. Epistemic Calibration

如果：

```text
RNG mapping unknown
```

Agent 說：

```text
confidence = 0.2
```

比錯誤地：

```text
confidence = 0.99
```

更高品質。

---

# 92. Calibration Score

可使用 proper scoring rule 或分 bucket reliability。

核心：

$$
P(\text{correct}\mid c\approx0.8)
\approx0.8.
$$

---

# 93. Decision Trace Quality

測：

- 是否重跑已 verified；
- 是否忽略 contradiction；
- 是否選低判別力實驗；
- 是否保存 exclusion。

---

# 94. Research Efficiency

定義：

$$
\boxed{
\eta_{\mathrm{AER}}
=
\frac{
H(\mathcal H_0)-H(\mathcal H_T)
}{
C_{\mathrm{total}}
}
}
$$

---

# 95. 若 entropy 不可計算

可以替代：

$$
\eta'
=
\frac{
N_{\mathrm{invalidated}}
+
\alpha N_{\mathrm{verified}}
}{
C_{\mathrm{total}}
}.
$$

---

# 96. 但不能只追求 invalidation 數量

因為 Agent 可以建立大量垃圾 hypothesis 再自己排除。

所以候選必須：

- meaningful；
- distinct；
- pre-registered。

---

# 97. Hypothesis Inflation Attack

若：

$$
|\mathcal H_0|
$$

由 Agent 任意膨脹，

則 entropy reduction metric 可被操弄。

需用 evaluator-defined hypothesis ontology。

---

# 98. External Ground Truth

若 benchmark 有 source truth：

$$
\Theta^*,
$$

可以直接比較：

$$
d(\hat\Theta,\Theta^*).
$$

這更可靠。

---

# 99. AER 與 Bayesian Update

AER 可以採 Bayesian update：

$$
P(h\mid E)
\propto
P(E\mid h)P(h).
$$

但本文不要求所有 Agent 顯式計算 Bayes posterior。

---

# 100. 更一般的 constraint update

可以：

$$
\mathcal H_{t+1}
=
Filter(
\mathcal H_t,
E_{t+1}
).
$$

或：

$$
score_{t+1}(h)
=
F(score_t(h),E_{t+1}).
$$

---

# 101. 因此 AER 不是 Bayesianism 的同義詞

它描述的是功能：

> 主動取得 evidence 來重構未知結構。

更新機制可以：

- Bayesian；
- frequentist；
- logical；
- heuristic；
- hybrid。

---

# 102. Bayesian Optimal Experimental Design 的接口

BOED 的核心問題：

> 哪個實驗最能改善 posterior knowledge？

AER 接受這個精神，

但把 design space 擴展到：

- tool calls；
- program executions；
- UI actions；
- traces；
- cross-version tests。

---

# 103. Query-by-Committee 的接口

QBC 以 model disagreement 找 informative query。

AER 可令：

$$
committee
=
\mathcal H_t.
$$

選：

$$
a
$$

讓候選預測最分歧。

---

# 104. Active Learning 的接口

Active learning 的：

$$
x\rightarrow y
$$

在 AER 中變成：

$$
a\rightarrow o.
$$

其中 $a$ 可能是一段 procedure。

---

# 105. Scientific Agent 的接口

Robin 等系統展示：

$$
Hypothesis
\rightarrow
Experiment
\rightarrow
Data
\rightarrow
Updated Hypothesis.
$$

AER 提供一個更一般、可跨軟體／科學 domain 的形式描述。

---

# 106. 可證偽預測一

在 target-local semantics 被 private mutation 的 benchmark：

只依賴 static prior 的 Agent 應顯著低於允許 active experiment 的 Agent。

---

# 107. 可證偽預測二

加入 verified historical prior 應降低：

$$
C_{\mathrm{discovery}}.
$$

但不應顯著降低 final validation requirement。

---

# 108. 可證偽預測三

有 information-gain-oriented planning 的 Agent 應比隨機實驗使用更少 action 達到同等 semantic accuracy。

---

# 109. 可證偽預測四

有 exclusion log / invalidation memory 的長時 Agent 應較少重複已知失敗。

---

# 110. 可證偽預測五

將穩定 protocol algorithmize 後：

$$
C_{\mathrm{token}}
$$

應下降，

且：

$$
A_{\mathrm{semantic}}
$$

不應下降。

---

# 111. 可證偽預測六

只給歷史 HEX table：

semantic label recovery 提高；

judgment-rule recovery 提升較小。

---

# 112. 可證偽預測七

fresh evidence 比例提高的 task，final correctness 與 benchmark contamination 的相關性應降低。

---

# 113. 限制一：Fresh 不等於 Correct

新生成的 observation 也可能：

- 量錯；
- log 錯；
- UI 認錯；
- script bug。

Freshness 只是 provenance 屬性。

---

# 114. 限制二：先驗不可避免

真正零先驗研究者不存在。

連知道：

> 這是一個 file

都是 prior。

因此目標不是：

$$
K_G=0.
$$

而是控制：

$$
K_{\mathrm{target}}.
$$

---

# 115. 限制三：黑箱程度是一個光譜

可定義：

$$
\beta\in[0,1].
$$

 $\beta=0$：

> white box。

 $\beta=1$：

> 完全不可觀察 black box。

Semi-black-box：

$$
0<\beta<1.
$$

---

# 116. 黑箱越深不一定 benchmark 越好

如果 observation 太少：

$$
\Theta^*
$$

不可識別，

只是在測猜運氣。

最佳 benchmark 需要：

> 足夠困難，但可透過高品質實驗收斂。

---

# 117. 限制四：Experiment Budget

Agent 可能靠無限 brute force 最終找到答案。

所以需固定：

$$
B_{\mathrm{time}},
B_{\mathrm{token}},
B_{\mathrm{compute}},
B_{\mathrm{action}}.
$$

---

# 118. 限制五：Agent 可以搜尋公開答案

某些 benchmark 可允許 web，

但 private mutation 必須讓：

> 公開答案只能當 prior。

---

# 119. 限制六：Human Intervention

如果人類中途提供：

> 看 0x50。

應記錄：

$$
K_{\mathrm{human}}.
$$

避免把 human clue 當 Agent autonomous discovery。

---

# 120. AER Provenance

完整：

$$
K_t
=
K_G
\cup
K_H
\cup
K_{\mathrm{human}}
\cup
E_F.
$$

---

# 121. Local Novelty

本文使用：

> local novelty

而不是：

> universal novelty。

一個 claim：

$$
c
$$

可能早被 1995 年玩家知道，

但對目前 Agent：

$$
c\notin K_0.
$$

它仍可能需要重新驗證。

---

# 122. Universal Novelty 與 Local Reconstruction 分離

$$
\text{Historical Discovery}
\neq
\text{Agent-local Discovery}.
$$

benchmark 測後者。

---

# 123. 這避免誇大

不能因 AI 重新發現：

```text
Stress offset
```

就說：

> AI 做出人類從未有過的發現。

正確：

> AI 在受控環境中自行重構了 target-local mapping。

---

# 124. 但這仍具有研究價值

因為它測：

$$
\boxed{
\text{Can the system recover truth it was not directly given?}
}
$$

---

# 125. 最終形式

本文提出：

$$
\boxed{
\operatorname{AER}
:
(K_G,K_H,E,\mathcal A)
\rightarrow
\hat\Theta
}
$$

其中：

$$
\hat\Theta
=
(\hat\rho,\hat\delta,\hat J).
$$

---

# 126. AER Quality

$$
Q_{\mathrm{AER}}
=
f(
Accuracy,
Calibration,
Evidence,
Efficiency,
Reproducibility
).
$$

不能只看 accuracy。

---

# 127. 統一架構

```text
GENERAL PRIOR
  x86 / DOS / coding / statistics
           │
           ├───────────────┐
           │               │
           ▼               ▼
HISTORICAL PRIOR       LOCAL ARTIFACT
FAQ / HEX / tools      binary / save
           │               │
           └──────┬────────┘
                  ▼
           HYPOTHESIS SPACE
                  │
                  ▼
         EXPERIMENT PLANNER
                  │
                  ▼
              ACTION
                  │
                  ▼
          TARGET ENVIRONMENT
                  │
                  ▼
           FRESH EVIDENCE
                  │
                  ▼
             VERIFIER
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     VERIFY    REJECT    UNKNOWN
        │         │         │
        └─────────┼─────────┘
                  ▼
          EPISTEMIC STATE
                  │
                  └──────→ NEXT EXPERIMENT
```

---

# 128. 核心命題一

## Proposition 1 — Prior Is Not Target Truth

即使：

$$
P(h)
$$

很高，

只要 target 可能有 private mutation：

$$
P(h\mid \text{target})
\neq1.
$$

所以 historical prior 不能取代 local validation。

---

# 129. 核心命題二

## Proposition 2 — Active Experiment Can Add Target-Specific Information

若：

$$
I(\Theta;O\mid A=a)>0,
$$

則執行：

$$
a
$$

可增加關於 target semantics 的資訊。

因此 Agent 不只是消耗 prior，

也能主動取得新 evidence。

---

# 130. 核心命題三

## Proposition 3 — Active Strategy Can Dominate Passive Sampling

若存在 action：

$$
a^*
$$

其 expected information gain 高於 passive action distribution 的平均，

則在相同 action budget 下，選：

$$
a^*
$$

可以有更高期望 semantic uncertainty reduction。

這是 active learning／experimental design 在 AER 中的直接延伸。

---

# 131. 核心命題四

## Proposition 4 — Memorization and Reconstruction Are Experimentally Separable in Principle

若 benchmark 使用：

$$
G_\phi
$$

且：

$$
\phi
$$

在訓練後才隨機生成，

則模型不可能直接從訓練資料記住：

$$
\phi.
$$

如果成功依賴恢復 $\phi$ 的效果，

則至少此 target-local 部分必須由：

- inference；
- experiment；
- tool use；

取得。

---

# 132. 這不證明沒有任何 memorization

Agent 仍使用：

- general algorithms；
- prior patterns。

真正被隔離的是：

$$
\text{target-local answer}.
$$

---

# 133. 核心命題五

## Proposition 5 — Reimplementation Is a Stronger Test Than Description

如果 Agent 只說：

```text
I think rule is X
```

驗證較弱。

若建立：

$$
\hat G
$$

且 unseen behavior：

$$
O_{\hat G}
\approx
O_G,
$$

則 semantic model 有更強外部支持。

---

# 134. 從 PM2 抽象出去

PM2 只是一個實例。

真正一般模式：

$$
\boxed{
\text{Artifact}
+
\text{Prior}
+
\text{Active Probe}
\rightarrow
\text{Semantic Reconstruction}
}
$$

---

# 135. 對 AI「只是背資料」批評的精確回答

不能說：

> AI 完全不背。

模型當然使用 training priors。

更精確：

> **如果 target-local evidence 在模型訓練完成後才產生，且關鍵答案經 private mutation 隱藏，則成功不能被「直接記住這個特定答案」充分解釋。**

---

# 136. 對 AI「全部都是推理」宣傳的修正

也不能反過來說：

> 所有結果都是現場獨立發現。

Agent 仍可能大量借用：

- known methods；
- patterns；
- historical maps。

所以：

$$
\boxed{
\text{Prior-Assisted Reconstruction}
}
$$

比「from scratch intelligence」準確。

---

# 137. 最重要的研究問題

不是：

> 有沒有 prior？

而是：

$$
\boxed{
\text{How efficiently can prior be converted into target-specific verified knowledge?}
}
$$

---

# 138. AER Efficiency

$$
\eta
=
\frac{
\Delta K_{\mathrm{verified}}
}{
\Delta C
}.
$$

這可能成為 Agent research capability 的核心量。

---

# 139. 與 Paper 04 的接口

Paper 03 關注：

> 怎麼取得 evidence。

Paper 04 將專門處理：

> **世界如何用 evidence 反駁 Agent。**

即：

$$
\boxed{
\text{External Falsification Surface}
}
$$

---

# 140. 與 Paper 05 的接口

AER 可能產生巨大：

$$
E_F.
$$

Paper 05 處理：

$$
\boxed{
\text{Evidence Explosion}
\rightarrow
\text{Semantic Compression}
}
$$

---

# 141. 與 Paper 06 的接口

AER 第一次 trajectory：

$$
\Pi_1
$$

可能很長。

Paper 06 處理：

> 如何把它壓縮成更短的研究策略。

---

# 142. 與 Paper 08 的接口

Paper 08 將把本文的 private mutation / fresh evidence 正式建成：

$$
\boxed{
\text{Contamination-Resistant Research Benchmark}
}
$$

---

# 143. 結論

AI 在半黑箱環境中的真正研究能力，不能只由：

> 它是否能對 raw artifact 猜出正確答案

衡量。

更重要的是：

1. 它能否區分通用先驗與 target-local truth；
2. 能否把歷史資料當 prior 而非 canonical truth；
3. 能否維持多個候選；
4. 能否選擇具有判別力的下一個 action；
5. 能否從外部系統產生 fresh evidence；
6. 能否因 contradiction 淘汰或降低假說信心；
7. 能否保留 UNKNOWN；
8. 能否把已驗證知識轉成可重播 specification。

因此本文將「主動認識重構」形式化為：

$$
\boxed{
K_t
\rightarrow
\mathcal H_t
\rightarrow
a_t^*
\rightarrow
E_{t+1}
\rightarrow
\mathcal H_{t+1}
}
$$

其中：

$$
a_t^*
=
\arg\max_a
\frac{
\mathbb E[
H(\mathcal H_t)-H(\mathcal H_{t+1})
]
}{
C(a)
}.
$$

最終目標不是：

> 讓 AI 猜更多。

而是：

> **讓 AI 知道自己目前不知道什麼，選擇最有價值的方式去問世界，然後用世界給出的新證據重新組織自己的局部知識。**

這就是本文所稱：

$$
\boxed{
\textbf{Active Epistemic Reconstruction}
}
$$

---

# References

[1] Freund, Y., Seung, H. S., Shamir, E., & Tishby, N. **Information, Prediction, and Query by Committee.** Advances in Neural Information Processing Systems 5, 1992.  
https://proceedings.neurips.cc/paper/1992/hash/3871bd64012152bfb53fdf04b401193f-Abstract.html

[2] Cohn, D. A., Ghahramani, Z., & Jordan, M. I. **Active Learning with Statistical Models.** Advances in Neural Information Processing Systems 7, 1994.  
https://proceedings.neurips.cc/paper/1994/hash/7f975a56c761db6506eca0b37ce6ec87-Abstract.html

[3] Sung, K. K., & Niyogi, P. **Active Learning for Function Approximation.** Advances in Neural Information Processing Systems 7, 1994.  
https://proceedings.neurips.cc/paper/1994/hash/acf4b89d3d503d8252c9c4ba75ddbf6d-Abstract.html

[4] Walsh, S. N., Wildey, T. M., & Jakeman, J. D. **Optimal Experimental Design Using A Consistent Bayesian Approach.** arXiv:1705.09395, 2017.  
https://arxiv.org/abs/1705.09395

[5] Pandita, P., Bilionis, I., & Panchal, J. **Bayesian Optimal Design of Experiments For Inferring The Statistical Expectation Of A Black-Box Function.** arXiv:1807.09979, 2018.  
https://arxiv.org/abs/1807.09979

[6] Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery.** arXiv:2408.06292, 2024.  
https://arxiv.org/abs/2408.06292

[7] Ghareeb, A. E., et al. **A multi-agent system for automating scientific discovery.** Nature 655, 497–505, 2026.  
https://www.nature.com/articles/s41586-026-10652-y

---

# Appendix A — AER Minimal Record

```yaml
aer_state:
  target:
    id:
    version:
    provenance:

  priors:
    general: []
    historical: []
    human: []

  hypotheses:
    - id:
      claim:
      prior_confidence:
      current_confidence:
      status:
      evidence_for: []
      evidence_against: []

  experiments:
    - id:
      protocol:
      expected_discrimination:
      cost:
      status:
      observation:
      excluded_reason:

  fresh_evidence:
    - id:
      generated_at:
      action_id:
      artifact_hash:
      supports: []
      contradicts: []

  frontier:
    unresolved: []
    next_candidate_experiments: []
```

---

# Appendix B — Historical Prior Ingestion

```yaml
historical_prior:
  source:
  claim:
  target_version:
  target_verified: false

  mapping:
    representation:
    semantic:
    judgment:

  validation_required:
    - controlled_intervention
    - negative_control
    - independent_reload
    - replication

  status: historical_prior
```

---

# Appendix C — Experiment Selection Heuristic

```python
def choose_experiment(hypotheses, experiments):
    best = None
    best_score = float("-inf")

    for experiment in experiments:
        discrimination = estimate_discrimination(
            hypotheses,
            experiment
        )

        reproducibility = estimate_reproducibility(
            experiment
        )

        cost = estimate_cost(
            experiment
        )

        score = (
            discrimination
            * reproducibility
            / max(cost, 1e-9)
        )

        if score > best_score:
            best = experiment
            best_score = score

    return best
```

---

# Appendix D — 一句話命題

> **真正具有研究能力的 Agent，不只是利用已知資料生成答案；它還能辨識局部未知、選擇對未知最有判別力的行動，從外部世界取得先前不存在的證據，再據此改寫自己的可用知識狀態。**
