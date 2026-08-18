---
title: "世界會反駁 AI：外部約束推理、假說淘汰與可證偽 Agent"
english_title: "The World Can Refute AI: External-Constraint Reasoning, Hypothesis Elimination, and Falsifiable Agents"
series: "AI Epistemic Reconstruction Series"
paper: "04"
author: "Neo.K"
date: "2026-08-14"
version: "v0.1"
document_type: "Research Paper / Formalization-and-Method Paper"
language: "zh-Hant"
status: "Research Draft"
---

# 世界會反駁 AI：外部約束推理、假說淘汰與可證偽 Agent

## The World Can Refute AI: External-Constraint Reasoning, Hypothesis Elimination, and Falsifiable Agents

**作者：Neo.K**  
**系列：AI Epistemic Reconstruction Series — Paper 04**  
**版本：v0.1**  
**日期：2026 年 8 月 14 日**

---

## 摘要

大型語言模型可以產生高度流暢且內部一致的解釋，但語言上的可接受性並不等於外部世界中的正確性。當一個 Agent 僅依賴自身生成內容進行「自我檢查」時，原本錯誤的前提、偏誤或幻覺可能被重新表述，而不是被真正排除。相較之下，當 Agent 的假說必須接受編譯器、單元測試、正式驗證器、檔案雜湊、可重播模擬器、資料庫、感測器或其他模型無法任意指定輸出的外部系統檢驗時，錯誤可以從「另一個可能的文字敘述」轉化成「與 evidence 不相容的候選」。

本文提出 **External Falsification Surface（外部可反駁面）**，記為：

$$
\boxed{
\mathcal F_E
}
$$

用來描述一個 Agent 可將其主張暴露於何種外部、可操作、可重現或可統計檢驗的約束。令假說：

$$
h\in\mathcal H_t,
$$

行動：

$$
a_t,
$$

環境：

$$
E,
$$

產生觀測：

$$
o_{t+1}=E(a_t).
$$

若某候選對此 action 預測：

$$
\hat o_h(a_t),
$$

且在 exact verifier 下：

$$
\hat o_h(a_t)\neq o_{t+1},
$$

則可執行：

$$
\boxed{
h\rightarrow\text{invalidated}
}
$$

而不是僅降低其語言偏好。

本文進一步區分三種 correction：**intrinsic self-correction、model-mediated critique、externally grounded falsification**。前兩者仍可能共享同一模型的盲點；第三者則把至少一部分判定權交給模型之外的可執行規則或世界狀態。CRITIC、ReAct、Reflexion、compiler-feedback、formal theorem verifier 等工作共同顯示：外部回饋可以成為改善模型輸出與研究 trajectory 的重要來源；同時，關於 intrinsic self-correction 限制的研究提醒我們，不能把「模型再想一次」與「模型被外部證據反駁」視為同一件事。

本文不主張外部世界一定提供無誤真理。Verifier 可能寫錯、環境可能隨機、觀測可能不完全、工具也可能有 bug。因此本文再提出：

- exact falsification；
- statistical falsification；
- observational contradiction；
- verifier uncertainty；
- evidence provenance；

等分層機制。

最終，本文將可證偽 Agent 定義為：**其重要假說可以被外部 action–observation protocol 置於失敗風險之下，且系統能保存 contradiction、更新 epistemic state，並阻止已被否證的候選無成本地重新進入 canonical knowledge。**

**關鍵詞：** AI Agents, Falsification, External Feedback, Verification, Self-Correction, Tool Use, Hypothesis Elimination, Epistemic State, Formal Verification, Scientific Agents

---

# 1. 問題：AI 能不能真的「知道自己錯了」？

考慮模型輸出：

> $h$ 是正確的。

接著要求同一模型：

> 請檢查 $h$。

它可能回答：

> 經過檢查， $h$ 仍然正確。

這並沒有建立：

$$
h=\text{true}.
$$

只建立：

$$
M(h)\rightarrow M(\text{approve}(h)).
$$

如果：

$$
M
$$

在兩個階段共享相同盲點，第二次生成不一定增加外部真值約束。

---

# 2. 語言一致性與外部正確性

定義：

$$
P_{\mathrm{plausible}}(h)
$$

與：

$$
P_{\mathrm{correct}}(h\mid W),
$$

其中：

$$
W
$$

表示外部世界／實際 task state。

一般：

$$
\boxed{
P_{\mathrm{plausible}}(h)
\neq
P_{\mathrm{correct}}(h\mid W)
}
$$

一個敘述可以：

- 很流暢；
- 很合理；
- 很像專家；

但仍被：

- compiler；
- runtime；
- experiment；
- theorem checker；

判錯。

---

# 3. 三種 correction

本文區分三種常被混稱「自我修正」的機制。

## 3.1 Intrinsic Self-Correction

只有模型本身：

```text
answer
→ reflect
→ revise
```

沒有新增外部 evidence。

形式：

$$
y_0=M(x)
$$

$$
y_1=M(x,y_0,\text{reflect}).
$$

---

## 3.2 Model-Mediated Critique

另一個模型或同一模型的 critic：

$$
c=M_c(x,y_0).
$$

再：

$$
y_1=M(x,y_0,c).
$$

仍可能完全存在模型系統內部。

---

## 3.3 Externally Grounded Falsification

先執行：

$$
a=T(y_0)
$$

或：

$$
a=E(y_0),
$$

得到：

$$
o.
$$

再：

$$
V(y_0,o).
$$

此處：

$$
o
$$

不是模型靠語言直接指定。

---

# 4. 文獻接口：intrinsic self-correction 並不等於可靠驗證

Huang 等人的研究指出，LLM 在沒有 external feedback 時，intrinsic self-correction 在 reasoning 任務上可能無法穩定改善，甚至會劣化。

這個結果的重要性不是：

> LLM 永遠不能 self-correct。

而是提醒：

$$
\boxed{
\text{Self-Reconsideration}
\neq
\text{External Verification}
}
$$

---

# 5. CRITIC：工具回饋作為 correction source

CRITIC 的核心結構：

```text
Initial Output
→ Tool Interaction
→ Critique
→ Revision
```

例如：

- search engine；
- code interpreter；

可提供模型外 feedback。

這正好是本文：

$$
\mathcal F_E
$$

的早期具體實例之一。

---

# 6. ReAct：行動產生新 observation

ReAct 不是只讓模型多想一步。

它允許：

$$
\text{Reasoning}
\leftrightarrow
\text{Action}
\leftrightarrow
\text{Observation}.
$$

action 使模型能：

> 到外部來源取得之前 context 中沒有的資訊。

因此：

$$
K_{t+1}\neq K_t
$$

可以由外部 observation 驅動。

---

# 7. Reflexion：feedback 可保存成 episodic memory

Reflexion 展示：

> Agent 可以把 trial feedback 保存到 episodic memory，再影響下一輪決策。

這與本文的：

$$
\text{contradiction}
\rightarrow
\text{epistemic state}
$$

相容。

但本文額外要求區分：

- external feedback；
- internally simulated feedback。

因為其證據強度不同。

---

# 8. Compiler Feedback：編譯器真的會說「不行」

compiler-feedback 類工作給一個特別乾淨的例子。

模型產生：

$$
c.
$$

編譯：

$$
Compile(c).
$$

若：

```text
syntax error
type error
invalid IR
```

則至少有一些 claim 被硬約束。

模型不能靠：

> 我認為它可以編譯。

讓 compiler 回傳 success。

---

# 9. Formal Verifier：更強的外部約束

在 Lean 等 formal system 中：

$$
Proof
\rightarrow
Verifier.
$$

若 verifier 不接受：

$$
\boxed{
\text{proof rejected}
}
$$

這比：

> 另一個模型覺得證明可能有錯

具有不同的 epistemic status。

---

# 10. 但 formal verifier 也不是宇宙真理機

Verifier 能證明的是：

> 在其 formal language、axioms、kernel 與 theorem statement 中，此 proof term 是否合法。

所以：

$$
V_{\mathrm{formal}}(p)=pass
$$

不代表：

- premise 與現實世界一定吻合；
- theorem statement 沒寫錯；
- model specification 沒錯。

---

# 11. 定義：External Falsification Surface

## Definition 1

對 Agent：

$$
\mathcal A
$$

與 task environment：

$$
E,
$$

定義：

$$
\boxed{
\mathcal F_E
=
\{(h,a,o,V)\}
}
$$

其中：

- $h$：可檢驗假說；
- $a$：外部 action / protocol；
- $o$：環境 observation；
- $V$：compatibility judgment。

---

# 12. Falsifiability

若存在：

$$
a\in\mathcal A
$$

使：

$$
P(o\mid h,a)
$$

與某替代假說：

$$
h'
$$

產生不同可觀察預測，

則：

$$
h
$$

具有可操作可證偽性。

---

# 13. 完全不可反駁的 claim

如果無論：

$$
o
$$

為何，

Agent 都可以重新解釋：

> 這仍支持 $h$。

則：

$$
h
$$

缺乏有效 falsification surface。

---

# 14. Agent 的 epistemic risk

一個好的假說不是：

> 怎樣都能說對。

而是願意承擔：

$$
\boxed{
\text{Risk of Rejection}
}
$$

如果世界返回特定 observation，

它就必須被降級或淘汰。

---

# 15. Exact Falsification

若：

$$
V
$$

為 deterministic exact verifier：

$$
V(h,o)\in\{pass,fail\}.
$$

則：

$$
V(h,o)=fail
$$

可形成 hard contradiction。

---

# 16. 例：SHA-256

假說：

> File A 與 File B 完全相同。

測：

$$
SHA256(A)=SHA256(B).
$$

若不同：

$$
\boxed{
h=\text{false}
}
$$

就該 claim 而言，不需要模型投票。

---

# 17. 例：byte equality

更直接：

$$
A\stackrel{?}=B.
$$

若：

$$
\exists i,\quad A_i\neq B_i,
$$

則：

> byte-identical

被否證。

---

# 18. 例：編譯

假說：

> 程式 $c$ 在指定 compiler/version/options 下可編譯。

執行：

$$
Compile(c).
$$

若 exit status failure：

$$
h
$$

被否證。

---

# 19. Exact 不等於 domain-complete

如果 compiler 只檢查：

> 語法與型別。

它不能否證：

> 程式邏輯一定正確。

所以 verifier 只能否證：

$$
\text{within its contract}.
$$

---

# 20. Verifier Contract

定義：

$$
C_V
$$

描述 verifier 真正判斷什麼。

例如：

```yaml
verifier:
  checks:
    - compiles_under_clang_18
  does_not_check:
    - semantic_correctness
    - security
    - performance
```

---

# 21. Statistical Falsification

真實環境可能 noisy。

若：

$$
o\sim P(o\mid h),
$$

則不能一次 observation 就淘汰。

需要：

$$
\Lambda
=
\frac{
P(E\mid h_1)
}{
P(E\mid h_0)
}
$$

或其他統計檢驗。

---

# 22. Statistical Rejection

例如：

$$
p<\alpha
$$

只表示：

> 在指定模型與檢驗設計下，資料與 null hypothesis 不相容程度達到門檻。

不是：

$$
P(h_0=\text{false})=1.
$$

---

# 23. Observational Contradiction

有些 evidence：

> 強烈反對 claim，但無法 exact reject。

例如：

```text
預測：100 次應觸發 90 次
實際：100 次只觸發 12 次
```

這應：

$$
confidence(h)\downarrow
$$

而非必然：

$$
h\rightarrow invalidated.
$$

---

# 24. 四級 Falsification Strength

建議：

```text
F0 — internal critique only
F1 — external weak observation
F2 — replicated empirical contradiction
F3 — exact deterministic contradiction
```

---

# 25. F0：模型內部

```text
LLM thinks answer may be wrong
```

可用，但不是外部證據。

---

# 26. F1：外部但弱

例如：

- 搜尋結果；
- single noisy observation；
- uncertain OCR。

---

# 27. F2：重複實驗

相同 protocol：

$$
E_1,E_2,\ldots,E_n
$$

產生一致反例。

---

# 28. F3：Exact

例如：

- hash mismatch；
- formal verifier reject；
- deterministic unit test fail；
- exact parser contradiction。

---

# 29. Falsification Surface Coverage

Agent 的 claim：

$$
h
$$

可能有多個 dimensions：

```text
syntax
state
behavior
performance
security
```

定義：

$$
Coverage(\mathcal F_E,h)
$$

表示 verifier set 覆蓋多少 claim dimensions。

---

# 30. 單一 unit test 不等於完整驗證

如果：

$$
T_1(h)=pass,
$$

只證明：

> 此 test 沒有發現錯。

不能推出：

$$
h=\text{universally correct}.
$$

---

# 31. Positive Evidence 與 Falsification 非對稱

對一般程式：

$$
1000\text{ tests pass}
$$

仍不能保證：

$$
\forall x,\ f(x)\text{ correct}.
$$

但一個反例：

$$
\exists x^*,\ f(x^*)\neq spec(x^*)
$$

即可否證 universal claim。

---

# 32. 所以 Agent 應保存 counterexample

Counterexample：

$$
x^*
$$

是高價值 evidence。

應成為：

```text
permanent regression fixture
```

---

# 33. Contradiction Ledger

本文提出：

$$
\boxed{
L_C
}
$$

即 contradiction ledger。

記錄：

```yaml
claim_id:
experiment_id:
observation:
verifier:
strength:
status:
```

---

# 34. 被否證 claim 不能無成本復活

如果：

$$
h
$$

已 F3 invalidated，

後續模型又生成相同 claim，

系統應：

```text
blocked_by_existing_contradiction
```

除非提出：

- version difference；
- verifier bug；
- protocol change；
- scope change。

---

# 35. Epistemic Garbage Collection

錯誤 hypothesis 可以從 active context 壓縮出去，

但 contradiction pointer 必須保留。

避免：

$$
\text{forget}
\rightarrow
\text{repeat same mistake}.
$$

---

# 36. Paper 03 與 Paper 04 的分界

Paper 03：

> 如何選實驗取得資訊。

Paper 04：

> 取得的資訊如何對 claim 形成約束。

所以：

$$
\text{AER}
=
\text{Acquire Evidence}
+
\text{Respect Evidence}.
$$

---

# 37. 不尊重 evidence 的 Agent 不算真正重構

若：

```text
experiment contradicts h
```

但 Agent：

> 我仍認為 h 是對的。

而沒有提出新 mechanism，

則 epistemic update failure。

---

# 38. Update Rule

可用：

$$
score_{t+1}(h)
=
U(
score_t(h),
E_{t+1},
V
).
$$

---

# 39. Exact contradiction update

若：

$$
V(h,E)=F3,
$$

則：

$$
score(h)=0
$$

在相同 scope 下。

---

# 40. Scope-Aware Invalidation

claim：

> 在 DOS v1.02 中 offset X 是 Stress。

若 Refine 不同，

不代表 DOS claim 被否證。

所以 contradiction key 要包含：

$$
(target,version,protocol,claim).
$$

---

# 41. Scope Mutation

如果：

```text
compiler version changed
```

則原 compile failure 不一定適用。

需要：

$$
C_V'
$$

新的 verifier contract。

---

# 42. External World Is Not a Language Model

最重要區別：

> 世界不需要配合你的敘事。

如果：

```text
file differs
```

它就是 differs。

模型不能靠語言把：

$$
A\neq B
$$

改成：

$$
A=B.
$$

---

# 43. 但 interpretation 仍需模型

Observation：

$$
A\neq B
$$

只否證：

> 完全相同。

不自動告訴：

> 差異原因。

所以：

$$
\boxed{
\text{External Constraint}
\neq
\text{Complete Explanation}
}
$$

---

# 44. 分工

世界：

> 告訴你 prediction 是否撞牆。

Agent：

> 重新解釋為什麼撞牆。

---

# 45. Running Case：半黑箱 DOS Save

研究流程：

```text
baseline save
→ controlled action
→ new save
→ exact diff
→ reload
```

這包含多個 falsification surfaces。

---

# 46. Surface A：save existence

假說：

> action 後成功產生 save。

檔案不存在：

$$
h\rightarrow fail.
$$

---

# 47. Surface B：byte identity

假說：

> no-op save 與 baseline 完全一致。

若：

$$
Diff(A,B)=\varnothing,
$$

支持。

若：

$$
Diff(A,B)\neq\varnothing,
$$

否證 exact identity claim。

---

# 48. Surface C：reload

假說：

> 修改後 save 是 valid persistent state。

若重新啟動後不能載入：

$$
h\rightarrow fail.
$$

---

# 49. Surface D：visible state

假說：

> reload 後 money/time 等 state 與 save 前一致。

UI / trace 可以提供 observation。

---

# 50. Surface E：replication

若同 protocol 第二次結果不一致，

原 deterministic claim 需要降級。

---

# 51. 這比「AI 看檔案說像」強很多

Static guess：

```text
this byte probably means X
```

Externalized protocol：

```text
if X, intervention A predicts delta D
→ run A
→ observe not-D
→ reject X
```

---

# 52. Prediction-Bearing Hypothesis

本文要求高品質 hypothesis 包含：

$$
h
\Rightarrow
\{\hat o_1,\ldots,\hat o_k\}.
$$

沒有 prediction 的 claim 很難 falsify。

---

# 53. Falsification-Ready Record

```yaml
hypothesis:
  claim:
  scope:
  predicted_observations:
  discriminating_actions:
  rejection_conditions:
```

---

# 54. 先寫 rejection condition

研究 protocol 最好在實驗前寫：

> 看到什麼結果，我就承認這個假說錯？

如果答案：

> 沒有任何結果會讓我承認錯，

那不是良好的 falsifiable hypothesis。

---

# 55. Pre-registration 的 Agent 版本

實驗前凍結：

```text
hypothesis
protocol
expected result
rejection rule
```

避免結果出來後改故事。

---

# 56. Outcome Retrofitting

錯誤模式：

```text
prediction A
→ observe B
→ claim “B 其實也支持 A”
```

若事前沒寫，

可能是 post-hoc rationalization。

---

# 57. Agent Rationalization Risk

LLM 特別擅長：

> 為任何結果產生合理故事。

所以需要：

$$
\boxed{
\text{Precommitted Falsification Rule}
}
$$

---

# 58. World Feedback 的真正價值

不是只提供更多 token。

而是提供：

$$
\boxed{
\text{Non-Negotiable Constraint}
}
$$

---

# 59. Intrinsic Critique 為何可能失敗

若：

$$
M
$$

生成錯誤 $h$，

又由相同：

$$
M
$$

判斷 $h$，

errors 可能 correlated。

---

# 60. Correlated Error

假設：

$$
P(\text{critic wrong}\mid\text{generator wrong})
$$

很高，

則自我 critique 對 error reduction 有限。

---

# 61. Independent Verifier

若 verifier failure mode 與 generator 不同，

則可降低 correlated error。

例如：

```text
LLM generates code
compiler checks syntax/type
unit tests check examples
```

---

# 62. Independence 不必完全

compiler 也可能：

- bug；
- undefined behavior；
- wrong flags。

但 failure modes 明顯不同於 LLM textual plausibility。

---

# 63. Heterogeneous Verification

最強系統通常不是：

$$
M+M+M.
$$

而是：

$$
\boxed{
M
+
Compiler
+
Tests
+
Runtime
+
Formal Checker
+
Human
}
$$

針對不同 claim dimension。

---

# 64. Multi-Verifier Consensus

令：

$$
V_1,\ldots,V_n.
$$

不是簡單 majority vote。

應根據：

$$
C_{V_i}
$$

各自 verifier contract 判斷。

---

# 65. Example

Compiler：

> 程式可編譯。

Unit tests：

> sample behavior 正確。

Formal verifier：

> specification property 成立。

Security scanner：

> 某 known pattern 不存在。

這些不是同一個問題的四票。

---

# 66. Verification Lattice

可以形成：

```text
syntax
  ↓
type
  ↓
runtime
  ↓
behavioral tests
  ↓
formal property
  ↓
target-world outcome
```

不同層不能互相取代。

---

# 67. 外部 evidence 也需要 provenance

Observation：

```text
test failed
```

要知道：

- test version；
- environment；
- seed；
- input；
- output；
- tool hash。

---

# 68. Reproducibility

若：

$$
E
$$

不能重現，

其 falsification strength 應降低。

---

# 69. Replayable Evidence

理想：

```text
artifact
protocol
seed
tool versions
expected output
actual output
```

---

# 70. External Falsification Surface Density

定義一個粗略指標：

$$
D_F
=
\frac{
N_{\mathrm{testable\ claims}}
}{
N_{\mathrm{important\ claims}}
}.
$$

---

# 71. 高 $D_F$

例如 formal code task：

大量 claim 可由 compiler/tests/checker 測。

---

# 72. 低 $D_F$

例如：

> 這個角色設定比較有靈魂。

缺乏精確 external verifier。

---

# 73. 不同 task 的 Agent 可驗證性不同

所以：

$$
\text{Agent Reliability}
$$

部分受 task：

$$
D_F
$$

限制。

---

# 74. Falsification Bandwidth

即：

> 每單位時間，世界能回傳多少具有判別力的 contradiction？

定義：

$$
B_F
=
\frac{
I(\mathcal H;E)
}{
T
}.
$$

---

# 75. DOS emulator 是高價值 sandbox

因為：

- reset 快；
- snapshot；
- deterministic parts；
- save diff；
- reproducible。

所以：

$$
B_F
$$

可能很高。

---

# 76. 真實社會系統則可能很低

原因：

- hidden variables；
- slow feedback；
- ethics；
- 不可 reset。

因此不能簡單把 DOS Agent 成功外推成：

> 所有科學 domain 都一樣容易。

---

# 77. Falsification Cost

$$
C_F(h)
$$

表示把 hypothesis 暴露於有效反駁所需成本。

---

# 78. 低成本

```text
run unit test
```

---

# 79. 高成本

```text
clinical trial
```

所以自動科學 Agent 能力會高度 domain-dependent。

---

# 80. Environment Authority

Agent 不應有權改：

$$
o_t
$$

以配合自己的 hypothesis。

否則：

> evidence laundering。

---

# 81. Immutable Raw Evidence

建議：

```text
raw/
  append-only
```

模型可以寫 interpretation，

不能覆蓋 original observation。

---

# 82. Derived Evidence

```text
raw observation
→ normalized
→ interpreted
```

每層保留 hash / provenance。

---

# 83. Verifier Hacking

如果 Agent 能修改 verifier：

$$
V,
$$

它可能：

> 不是把答案做對，而是把測試改成 pass。

---

# 84. Reward Hacking 的 epistemic 版本

目標：

$$
\max V(h)
$$

若 Agent 可改 $V$，

可能找到：

$$
V'(h)=pass
$$

而非：

$$
h=\text{correct}.
$$

---

# 85. Verifier Integrity Boundary

因此：

$$
V
$$

需要權限隔離。

Agent 可以：

- propose test；
- request new verifier；

但核心 benchmark verifier 不可由它靜默改寫。

---

# 86. Test Deletion Attack

失敗：

```text
test X fails
```

Agent：

```text
delete test X
```

不能算修正。

---

# 87. Legitimate Test Revision

如果 test specification 本身錯，

可以改，

但必須：

```text
old test retained
reason documented
human / independent approval
```

---

# 88. External Falsification 與安全

安全系統也可以：

```text
proposal
→ sandbox
→ policy verifier
→ runtime monitor
```

但本文不展開安全治理。

---

# 89. 世界並不是單一 Oracle

更精確：

$$
W
$$

透過測量函數：

$$
m(W)
$$

產生 observation。

所以：

$$
o=m(W)+\epsilon.
$$

---

# 90. 測量誤差

若：

$$
\epsilon\neq0,
$$

不能把 observation 當 perfect truth。

---

# 91. Falsification Pipeline

$$
W
\rightarrow
Measurement
\rightarrow
Observation
\rightarrow
Verifier
\rightarrow
Epistemic Update.
$$

每一層都可能失敗。

---

# 92. 所以「世界會反駁 AI」不是神諭論

它的意思是：

> 外部 causal process 可以產生不受模型文本偏好控制的 observation。

---

# 93. External Constraint Grounding

本文定義：

若 observation 的值由：

$$
P(o\mid W,a)
$$

決定，

且模型不能直接 override，

則該 observation 對 Agent 是 externally grounded。

---

# 94. Grounded 不等於 true interpretation

例如 sensor：

```text
voltage = 2.1V
```

是 grounded reading。

但：

> 這代表溫度 30°C

需要 calibration model。

---

# 95. Evidence vs Interpretation

應保存：

```yaml
raw:
  voltage: 2.1

interpretation:
  temperature_estimate: 30
```

不能混成一層。

---

# 96. 對 PM2 同理

Raw：

```text
offset 0x50 = 0x0064
```

Interpretation：

```text
Stress = 100
```

Rule claim：

```text
Stress affects disease
```

三個 claim 使用不同 verifier。

---

# 97. Falsification Chain

$$
h_R
\rightarrow
h_S
\rightarrow
h_J.
$$

Representation 假說錯，

後面都可能錯。

---

# 98. Root-Cause Backtracking

若 behavioral test fail，

不一定：

$$
h_J
$$

錯。

也可能：

$$
h_R
$$

或：

$$
h_S
$$

錯。

---

# 99. Dependency Graph

```text
Representation
      ↓
Semantic Mapping
      ↓
Rule Model
      ↓
Behavior Prediction
```

contradiction 應沿 dependency graph 回溯。

---

# 100. Blame Assignment

Agent 需要：

$$
P(
h_i\text{ wrong}
\mid
E_{\mathrm{contradiction}}
).
$$

而不是整個模型全部推翻。

---

# 101. Minimal Contradiction Set

若可能，

找最小：

$$
C^*
$$

使 specification inconsistent。

這能縮小 debugging space。

---

# 102. Formal Methods 接口

SAT/SMT/formal checker 可以提供：

```text
counterexample
unsat core
proof failure
```

這些比單純：

> fail

更有信息量。

---

# 103. Rich Verifier Feedback

Verifier 返回：

$$
(o,\Delta),
$$

其中：

$$
\Delta
$$

是 error localization。

這能提高 Paper 03 的：

$$
IG(a).
$$

---

# 104. 所以 verifier 不只是 judge

好的 verifier 還是：

$$
\boxed{
\text{Information Generator}
}
$$

---

# 105. Compiler error message

比：

```text
exit 1
```

包含更多：

```text
line
type mismatch
symbol
```

所以更高 information gain。

---

# 106. Formal proof state

Lean verifier 可返回：

- unsolved goals；
- type mismatch；
- missing lemma context。

也可作下一步 proposal input。

---

# 107. Externally Guided Iteration

$$
Proposal_t
\rightarrow
VerifierFeedback_t
\rightarrow
Proposal_{t+1}.
$$

---

# 108. 這不等於 weight update

模型參數：

$$
\theta
$$

可能不變。

更新的是：

$$
K_t.
$$

---

# 109. Epistemic correction

所以：

$$
\boxed{
\text{Correction}
\neq
\text{Training}
}
$$

可以是 session-level evidence update。

---

# 110. Persistent Error Memory

若 contradiction 保存到：

$$
S,
$$

下一次：

$$
M
$$

可讀取它。

---

# 111. 無 persistent state

同一錯誤可能每次重生。

所以長時 Agent 需要：

$$
\text{negative memory}.
$$

---

# 112. Negative Memory

不只記：

> 什麼是對的。

也記：

> 什麼已經被證明不行。

---

# 113. 高品質 Research Memory

```text
VERIFIED
INVALIDATED
UNKNOWN
EXCLUDED
```

四類都重要。

---

# 114. Excluded 與 Invalidated 不同

Excluded：

> 實驗 protocol 失效，不能判 hypothesis。

Invalidated：

> 有效 evidence 與 hypothesis 衝突。

不能混。

---

# 115. Example

誤點教堂捐 100G：

```text
run = excluded
```

不是：

```text
hypothesis = false
```

---

# 116. Epistemic Hygiene

若把 corrupted run 當反例，

會錯殺正確 hypothesis。

---

# 117. Evidence admissibility

定義：

$$
A(e)\in\{admissible,excluded\}.
$$

只有：

$$
A(e)=admissible
$$

才能更新核心 claim。

---

# 118. Protocol Violation

例如：

- unexpected UI branch；
- wrong seed；
- save slot conflict；
- accidental action。

全部進 exclusion log。

---

# 119. 可證偽 Agent 的正式定義

## Definition 2 — Falsifiable Agent

Agent：

$$
\mathcal A
$$

若對重要 claim $h$：

1. 保存 scope；
2. 保存 prediction；
3. 存在 external test；
4. 保存 rejection rule；
5. contradiction 可修改 epistemic state；
6. invalidated claim 不會無痕復活；

則稱其在該 claim class 上為：

$$
\boxed{
\text{falsifiable agent}
}
$$

---

# 120. Falsifiability Ratio

$$
R_F
=
\frac{
|\mathcal H_{\mathrm{falsifiable}}|
}{
|\mathcal H_{\mathrm{active}}|
}.
$$

---

# 121. $R_F$ 高不保證答案正確

但表示：

> 更多主張願意被世界檢驗。

---

# 122. Epistemic Accountability

可定義：

$$
A_E
=
f(
R_F,
Provenance,
UpdateCompliance,
Replayability
).
$$

---

# 123. Update Compliance

世界已反駁，

Agent 有沒有真的改？

定義：

$$
U_C
=
P(
\text{state updated}
\mid
\text{valid contradiction}
).
$$

---

# 124. 很低的 $U_C$

代表：

> Agent 看了 evidence 但仍照講原答案。

---

# 125. Overcorrection

另一風險：

一個 weak contradiction 就把高證據假說全部刪掉。

所以 update 要看 strength。

---

# 126. Strength-Aware Update

$$
score_{t+1}(h)
=
score_t(h)
-
w(e)
$$

weak evidence。

F3 exact contradiction：

$$
score=0.
$$

---

# 127. Conflicting Evidence

如果：

$$
E^+
$$

與：

$$
E^-
$$

同時存在，

可能表示：

- context difference；
- hidden variable；
- version difference；
- tool bug。

---

# 128. 不應 average 掉矛盾

而要建立：

$$
\text{split hypothesis}.
$$

例如：

```text
h_DOS
h_Refine
```

---

# 129. Contradiction as Discovery

矛盾不是只是錯誤。

它常指出：

> 原 hypothesis 太粗。

所以：

$$
\boxed{
\text{Contradiction}
\rightarrow
\text{Model Refinement}
}
$$

---

# 130. 這正是科學價值

世界說：

> 你的模型不夠。

研究者：

> 那我要增加一個變數／分版本／分 domain。

---

# 131. Falsification 不是單純 delete

可能：

$$
h
\rightarrow
\{h_1,h_2\}.
$$

---

# 132. Model Refinement Operator

$$
R_f(h,e)
\rightarrow
\{h'_1,\ldots,h'_k\}.
$$

---

# 133. 但 refinement 不能無限 ad hoc

如果每次反例就新增：

> 特例 exception

最終模型失去 predictive power。

---

# 134. Complexity Penalty

可以懲罰：

$$
Complexity(h).
$$

例如 MDL/Bayesian prior 思想。

---

# 135. 可反駁性與簡潔性的平衡

理想：

> 能解釋更多 evidence，但不靠無限補丁。

---

# 136. Paper 05 的接口

長時間 falsification 會產生：

- logs；
- failures；
- counterexamples；
- traces。

所以：

$$
E
$$

爆炸。

Paper 05 將研究：

$$
\boxed{
\text{Evidence Explosion}
\rightarrow
\text{Semantic Compression}
}
$$

---

# 137. Paper 06 的接口

很多 falsification protocol 最初很慢。

未來要把：

$$
\Pi
$$

壓成自動 script。

---

# 138. Paper 07 的接口

重複：

```text
run
fail
reset
rerun
```

正是 AI 可以承擔的「無聊認識勞動」。

---

# 139. Paper 08 的接口

Benchmark 可以故意放：

- false priors；
- misleading labels；
- private mutations。

測 Agent 是否真的讓世界反駁自己。

---

# 140. 可證偽預測一

在具有 reliable external verifier 的 reasoning/code task：

$$
M+V_E
$$

應優於只有 intrinsic self-correction 的：

$$
M+M.
$$

---

# 141. 可證偽預測二

如果 verifier feedback 被隨機打亂，

performance improvement 應顯著下降。

---

# 142. 可證偽預測三

如果 contradiction ledger 被移除，

長時 Agent 應更頻繁重複已 invalidated claim。

---

# 143. 可證偽預測四

加入 precommitted rejection conditions 應降低 post-hoc rationalization。

---

# 144. 可證偽預測五

多 verifier、異質 failure mode 的系統應比單一 self-critic 更能發現不同類型錯誤。

---

# 145. 可證偽預測六

如果 Agent 可偷偷修改 verifier，

表面 pass rate 可能提高，

但 unseen ground-truth performance 下降。

---

# 146. 可證偽預測七

較高 external falsification surface density 的 task，Agent 的可稽核可靠性應更高。

---

# 147. 限制一：World feedback 可能昂貴

不是所有 domain 都像 compiler。

若：

$$
C_F\gg1,
$$

Agent 可能無法大量試錯。

---

# 148. 限制二：Ethical Constraints

某些實驗即使有高 information gain，

也不能做。

所以 action set：

$$
\mathcal A_{\mathrm{allowed}}
\subset
\mathcal A.
$$

---

# 149. 限制三：不可逆世界

DOS 可 reset。

現實世界有些 action：

$$
irreversible.
$$

所以 falsification planning 必須加入 risk。

---

# 150. 限制四：Verifier Bias

Benchmark 只測 verifier 能看的東西。

Agent 可能過度優化：

$$
V
$$

而忽略真正 task。

---

# 151. 限制五：Specification Error

如果 spec 錯，

perfect verifier 也會驗錯東西。

---

# 152. 限制六：Unknown Unknowns

假說空間：

$$
\mathcal H
$$

如果不含真實模型，

所有候選都可能被反例打掉。

Agent 最後必須能：

```text
none of the above
```

---

# 153. 開放世界 falsification

因此：

$$
\mathcal H_{t+1}
$$

有時不是 subset。

也可能：

$$
\mathcal H_{t+1}
=
(\mathcal H_t\setminus H^-)
\cup H^+_{\mathrm{new}}.
$$

---

# 154. 反駁同時促進 hypothesis generation

外部 evidence 不只減少 search space。

也可能創造新方向。

---

# 155. 這就是研究而不是選擇題

若真答案永遠在候選清單，

問題比較簡單。

真實研究允許：

> 原來我們一開始整個問題框錯了。

---

# 156. Falsification-Driven Expansion

當全部候選 fail：

$$
\forall h\in\mathcal H_t,\ V(h)=fail,
$$

觸發：

$$
\text{reframe}.
$$

---

# 157. Reframe

重新檢查：

- representation；
- assumptions；
- measurement；
- tool；
- task definition。

---

# 158. Agent 必須知道 verifier 也可能錯

成熟 Agent 不應：

> verifier fail → 世界絕對錯。

而是根據 verifier reliability。

---

# 159. Verifier Reliability

$$
r_V
=
P(
V\text{ correct}
).
$$

F3 只適用於高可靠 exact contract。

---

# 160. Independent Cross-Check

關鍵 evidence 可用：

$$
V_1,V_2
$$

獨立實作交叉驗證。

---

# 161. 例如 Hash + byte diff

兩者同時說：

> files identical

證據更強。

---

# 162. 但兩者也可能共享同一 input corruption

所以 provenance chain 仍重要。

---

# 163. External Falsification Stack

```text
Raw Artifact
   ↓
Measurement
   ↓
Normalization
   ↓
Verifier
   ↓
Contradiction
   ↓
Epistemic Update
```

每層都應可追蹤。

---

# 164. 最小實作架構

```text
MODEL
  ↓ propose
HYPOTHESIS REGISTRY
  ↓ select
EXPERIMENT RUNNER
  ↓ observe
RAW EVIDENCE STORE
  ↓
VERIFIER
  ↓
CONTRADICTION LEDGER
  ↓
EPISTEMIC STATE
  └────────→ MODEL
```

---

# 165. Hypothesis Registry

```yaml
hypothesis:
  id:
  scope:
  claim:
  predictions:
  rejection_conditions:
  confidence:
  status:
```

---

# 166. Raw Evidence Store

append-only：

```yaml
evidence:
  id:
  timestamp:
  protocol:
  artifact_hashes:
  raw_observation:
```

---

# 167. Verifier Output

```yaml
verdict:
  hypothesis_id:
  evidence_id:
  result:
    - supports
    - contradicts
    - inconclusive
  strength:
    - F0
    - F1
    - F2
    - F3
  contract:
```

---

# 168. Contradiction Ledger

```yaml
contradiction:
  id:
  hypothesis:
  evidence:
  verifier:
  scope:
  effect:
  replay_pointer:
```

---

# 169. Epistemic Update

```yaml
update:
  old_status:
  new_status:
  reason:
  confidence_before:
  confidence_after:
```

---

# 170. Why this matters for AI research

如果只看 final answer：

> 可能猜中。

如果保存 falsification trace：

> 可以看它怎麼被世界修正。

這是完全不同的可稽核程度。

---

# 171. Agent Reliability 不是「永不犯錯」

更成熟定義：

$$
\boxed{
\text{Reliable Agent}
=
\text{Makes Errors}
+
\text{Exposes Errors to Tests}
+
\text{Updates When Refuted}
}
$$

---

# 172. 錯誤不可避免

尤其 open-ended research。

重點是：

$$
\text{error lifetime}.
$$

---

# 173. Error Half-Life

可定義：

$$
T_{1/2}^{error}
$$

即一個錯誤假說被 evidence 降到低 confidence 所需時間。

---

# 174. 更好的 Agent

不是完全不犯錯，

而是：

$$
T_{1/2}^{error}\downarrow.
$$

---

# 175. Contradiction Throughput

$$
Q_C
=
\frac{
N_{\mathrm{valid\ contradictions\ processed}}
}{
T
}.
$$

---

# 176. 但 throughput 不是越高越好

如果 Agent 產生大量垃圾假說再淘汰，

只是浪費。

要和 Paper 03 的 hypothesis quality 合看。

---

# 177. Epistemic Productivity

可定義：

$$
P_E
=
\frac{
\Delta K_{\mathrm{verified}}
}{
C_{\mathrm{total}}
}.
$$

Falsification 是其中一個機制。

---

# 178. 與 Paper 01 的回扣

Paper 01 說：

$$
\text{Probability}
+
\text{Tools}
+
\text{Verification}.
$$

Paper 04 現在說明：

> Verification 不是裝飾，而是能改變 hypothesis survival 的獨立結構。

---

# 179. 與「只是概率模型」再一次連接

模型可以：

$$
P(h_i\mid context).
$$

但 external verifier 可以加入：

$$
constraint(h_i)=0.
$$

如果 hard contradiction：

$$
h_i
$$

退出 active set。

---

# 180. Probabilistic proposal, deterministic rejection

因此一個很漂亮的模式：

$$
\boxed{
\text{Probabilistic Proposal}
+
\text{Deterministic Rejection}
}
$$

---

# 181. 另一種：probabilistic proposal, statistical rejection

自然科學：

$$
\boxed{
\text{Probabilistic Proposal}
+
\text{Statistical Falsification}
}
$$

---

# 182. 更一般：

$$
\boxed{
\text{Uncertain Generator}
+
\text{Constraint-Producing World}
}
$$

---

# 183. 系統的知識不是模型單方面生成

而是在：

$$
M
\leftrightarrow
W
$$

互動中被塑形。

---

# 184. Epistemic Coupling

定義：

$$
K_{t+1}
=
U(
K_t,
M_t,
W_t
).
$$

---

# 185. 世界具有 veto power

在某些 claim class 上：

$$
W
$$

可以否決模型 proposal。

這就是：

$$
\boxed{
\text{Epistemic Veto}
}
$$

---

# 186. 但 veto 受 observation contract 限制

世界只能對可觀測 claim 行使 veto。

不可觀測部分仍 unknown。

---

# 187. 所以高品質 Agent 應明確標記

```text
VERIFIED
FALSIFIED
INCONCLUSIVE
UNTESTABLE_UNDER_CURRENT_TOOLS
```

---

# 188. 最糟糕的是把 INCONCLUSIVE 寫成 VERIFIED

這是 epistemic overclaim。

---

# 189. Falsifiability-aware language

Agent 輸出應區分：

- observed；
- inferred；
- verified；
- speculative。

---

# 190. 最終形式化

給：

$$
h_t,
a_t,
o_{t+1},
V,
$$

更新：

$$
K_{t+1}
=
U(
K_t,
h_t,
a_t,
o_{t+1},
V
).
$$

若：

$$
V(h_t,o_{t+1})=\text{exact contradiction},
$$

則在固定 scope：

$$
h_t
\notin
\mathcal H_{t+1}^{active}.
$$

---

# 191. 開放世界版本

同時：

$$
\mathcal H_{t+1}
=
(
\mathcal H_t
\setminus
\{h_t\}
)
\cup
GenerateNew(
E_{t+1}
).
$$

所以反駁會：

> 刪除舊模型，也刺激新模型。

---

# 192. 核心命題一

## Proposition 1 — External Observation Can Add a Constraint Unavailable to Pure Intrinsic Reconsideration

若：

$$
o=E(a)
$$

在 action 前不在 context 中，

且模型不能直接設定 $o$，

則 $o$ 對 hypothesis update 提供一個額外外部 constraint。

---

# 193. 核心命題二

## Proposition 2 — Exact Verifier Produces Hard Elimination Within Scope

若：

$$
V(h,o)=fail
$$

且：

- $V$ exact；
- protocol valid；
- scope matched；

則：

$$
h
$$

可被 hard invalidated。

---

# 194. 核心命題三

## Proposition 3 — Intrinsic Self-Correction Is Not Equivalent to External Falsification

因為 intrinsic：

$$
M\rightarrow M
$$

不保證新增：

$$
o_E.
$$

externally grounded：

$$
M\rightarrow E\rightarrow o_E\rightarrow M
$$

包含模型外 constraint。

---

# 195. 核心命題四

## Proposition 4 — A Falsifiable Agent Requires Update Compliance

僅有 verifier 不夠。

若 Agent 不因 contradiction 更新，

則：

$$
\mathcal F_E
$$

未真正進入 epistemic loop。

---

# 196. 核心命題五

## Proposition 5 — Contradiction Memory Reduces Repeated Error Under Persistent Tasks

若 invalidated hypothesis 記錄可被後續查詢，

則在相同 task family 上，重複提出相同已否證 claim 的機率應下降。

此命題可實驗測試。

---

# 197. 核心命題六

## Proposition 6 — Verifier Diversity Can Increase Error-Class Coverage

若：

$$
V_i
$$

具有非完全重疊 failure detection domains，

則：

$$
Coverage(\cup_i V_i)
\ge
\max_i Coverage(V_i).
$$

---

# 198. 最終結論

一個 AI Agent 若只能：

> 產生答案，再由自己說答案看起來對不對，

它仍缺乏強外部可證偽性。

當系統加入：

- compiler；
- test；
- formal verifier；
- runtime；
- black-box experiment；
- replay；
- hash；
- independent environment；

模型的 claim 才開始被暴露於：

$$
\boxed{
\mathcal F_E
}
$$

即外部可反駁面。

此時真正重要的不是：

> AI 是否永遠不犯錯。

而是：

> **AI 的錯誤是否有地方會撞牆？撞牆後，它是否真的改變自己的知識狀態？**

因此本文提出：

$$
\boxed{
\text{Falsifiable Agent}
=
\text{Hypothesis Generator}
+
\text{External Falsification Surface}
+
\text{Contradiction Memory}
+
\text{Update Compliance}
}
$$

最簡潔地說：

> **語言可以說服另一段語言；世界則可以讓一個預測直接失敗。**

真正具有研究能力的 Agent，需要的不只是更會生成說法，而是願意把自己的說法交給世界判定，並且在世界說「不」之後，保留那個「不」。

---

# 199. 後續

**Paper 05：從十二小時到數 KB：AI 長時研究中的證據爆炸與語義再壓縮**

將處理：

$$
\boxed{
\text{Raw Evidence Explosion}
\rightarrow
\text{Canonical Epistemic State}
}
$$

也就是：

> 當 Agent 經過數小時甚至數天累積大量 screenshots、traces、diffs、failed runs 與 counterexamples 時，如何壓縮成幾 KB～幾 MB 的可續接研究狀態，又不丟掉反駁能力？

---

# References

[1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. **ReAct: Synergizing Reasoning and Acting in Language Models.** ICLR 2023. arXiv:2210.03629.  
https://arxiv.org/abs/2210.03629

[2] Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. **Reflexion: Language Agents with Verbal Reinforcement Learning.** NeurIPS 2023. arXiv:2303.11366.  
https://arxiv.org/abs/2303.11366

[3] Gou, Z., Shao, Z., Gong, Y., Shen, Y., Yang, Y., Duan, N., & Chen, W. **CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing.** ICLR 2024. arXiv:2305.11738.  
https://arxiv.org/abs/2305.11738

[4] Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., & Zhou, D. **Large Language Models Cannot Self-Correct Reasoning Yet.** ICLR 2024. arXiv:2310.01798.  
https://arxiv.org/abs/2310.01798

[5] Grubisic, D., Cummins, C., Seeker, V., & Leather, H. **Compiler Generated Feedback for Large Language Models.** arXiv:2403.14714, 2024.  
https://arxiv.org/abs/2403.14714

[6] Ji, X., Liu, Y., Wang, Q., Zhang, J., Yue, Y., Shi, R., Sun, C., Zhang, F., Zhou, G., & Gai, K. **Leanabell-Prover-V2: Verifier-integrated Reasoning for Formal Theorem Proving via Reinforcement Learning.** arXiv:2507.08649, 2025.  
https://arxiv.org/abs/2507.08649

---

# Appendix A — External Falsification Record

```yaml
falsification_record:
  hypothesis:
    id:
    scope:
    claim:
    predictions: []
    rejection_conditions: []

  experiment:
    id:
    protocol_hash:
    action:
    environment:
    tool_versions:
    admissible: true
    exclusion_reason:

  observation:
    raw:
    artifact_hashes: []
    reproducible:
    repetitions:

  verifier:
    id:
    contract:
    reliability:
    result:
      - supports
      - contradicts
      - inconclusive
    strength:
      - F0
      - F1
      - F2
      - F3

  epistemic_update:
    old_status:
    new_status:
    confidence_before:
    confidence_after:
    contradiction_ledger_id:
```

---

# Appendix B — Minimal Falsifiable-Agent Loop

```python
state = load_epistemic_state()

proposal = model.propose(state)

hypothesis = register_hypothesis(
    proposal,
    scope=state.current_scope,
    rejection_conditions=proposal.rejection_conditions
)

experiment = planner.choose_test(
    hypothesis,
    state.available_falsification_surfaces
)

observation = runner.execute(experiment)

verdict = verifier.evaluate(
    hypothesis=hypothesis,
    observation=observation
)

ledger.append(
    hypothesis=hypothesis,
    experiment=experiment,
    observation=observation,
    verdict=verdict
)

state = epistemic_update(
    state,
    verdict,
    hypothesis
)

save_epistemic_state(state)
```

---

# Appendix C — 一句話命題

> **真正可驗證的 AI 研究能力，不只在於能產生可能正確的假說，而在於其假說能否被模型之外的世界置於失敗風險之下，以及系統在失敗發生後是否真的保存並服從那個反例。**
