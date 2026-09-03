# LRC–COL-07：AI 學習時間
## 從記憶符號到操作理解
### AI Learning Time: From Symbol Recall to Operational Understanding

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

前六篇已建立複合算子語言的語言—現實耦合、行動收益、最小與最大有效基底、基底—深度交換律，以及靜態／動態有效區間。但若一套 operator language 最終要被 AI 使用，還有一個不能被跳過的核心問題：

> **AI 到底要花多久，才算「學會」一個新符號、一個新 operator，或一整套複合算子語言？**

這個問題不能只用「看過幾次」回答。AI 可以在 prompt 中讀到一個定義並立刻複述；也可以在幾個 examples 後模仿一種已知用法；但這些都不必然表示它能在新的 composition、新的 domain、新的工具環境與新的 context 中可靠使用該 operator。更進一步，標準 in-context adaptation 與長期 persistent learning 也不能混為一談：一個只在當前 context 中有效的新規則，與一個已被外部記憶、runtime policy、adapter 或模型參數長期保存的能力，具有不同的學習時間與遺忘機制。

本文因此將 AI operator learning 拆成八級能力：

$$
\boxed{
\text{Recognition}
\rightarrow
\text{Recall}
\rightarrow
\text{Imitation}
\rightarrow
\text{Familiar Composition}
\rightarrow
\text{Novel Composition}
\rightarrow
\text{Cross-Context Transfer}
\rightarrow
\text{Cross-Domain Transfer}
\rightarrow
\text{Retention / Relearning}.
}
$$

本文提出 **Operational Understanding（操作理解）** 作為可測的工程概念，而不宣稱解決哲學上的「真正理解」問題。若一個 Agent 在不直接重播答案的 held-out 任務中，能穩定選擇、組合、執行與修正新 operator，並在指定時間／exposure window 內維持語義與行動保真，本文稱其達到指定門檻下的 operational understanding。

核心學習時間定義為：

$$
\boxed{
T_{\epsilon}^{learn}
=
\inf
\left\{
t:
\mathbf E_{op}(t:t+W)
\preceq
\boldsymbol\epsilon
\right\},
}
$$

其中 $\mathbf E_{op}$ 是一個包含 recognition、selection、composition、execution、transfer 與 retention error 的誤差向量， $W$ 是穩定窗口。本文另外區分 wall-clock time、compute time、exposure count、successful-use count 與 effective exposure。尤其：

$$
\boxed{
100\times\text{same example}
\neq
100\times\text{structurally informative examples}.
}
$$

因此本文定義：

$$
\boxed{
X_{eff}
=
\sum_i
w_i^{novel}
w_i^{coverage}
w_i^{discrimination}
w_i^{transfer},
}
$$

作為第一版 effective exposure measure。

本文也區分四種 learning substrate：context-bound learning、external-memory learning、runtime / policy learning，以及 parameter / adapter learning；並提出 retention、relearning savings、catastrophic forgetting、stability–plasticity tradeoff、curriculum geometry 與 learning phase transition 等研究命題。

近期研究提供重要外部錨點：2025 年 Rapid Word Learning Through Meta In-Context Learning 顯示，經專門 meta-training 後，模型可以從一到少數 context examples 學習新詞並產生新用法；但 minimum-coverage compositional generalization 與 morphology 研究仍顯示，元件已見過不代表 novel combinations 能穩定泛化。2026 年 continual-learning 與 online-adaptation benchmark 則進一步表明，持續吸收新知識同時避免忘記舊能力仍具有明顯 stability–plasticity 困難。

本文最終主張：

$$
\boxed{
\text{AI learning time is not the time to recall a symbol definition;}
}
$$

而是：

$$
\boxed{
\text{the time / exposure required to reach stable, transferable, fidelity-bounded operational competence under a specified persistence mode.}
}
$$

---

## 關鍵詞

AI learning time；operator learning；operational understanding；few-shot learning；in-context learning；compositional generalization；retention；continual learning；relearning；symbol learning

---

# 1. 「看過」不是「學會」

假設給 AI：

> `⟁ = 對目前方法建立一條獨立反例，若反例成立就升格方法本身。`

AI 立刻回答：

> `⟁` 表示建立獨立反例並必要時升格方法。

這最多證明：

$$
\boxed{
\text{Definition Recall}.
}
$$

還不能證明它能在新的任務中：

- 自己辨識何時該用；
- 正確展開；
- 與其他 operator 組合；
- 避免誤用；
- 執行後修正。

因此：

$$
\boxed{
\text{Seen}
\neq
\text{Remembered}
\neq
\text{Usable}
\neq
\text{Generalizable}.
}
$$

---

# 2. 為什麼「AI 需要多久理解」必須先拆開？

因為「多久」可能指：

- 幾秒 wall-clock；
- 幾個 tokens；
- 幾個 demonstrations；
- 幾次成功使用；
- 幾次錯誤修正；
- 幾個不同 composition；
- 幾次跨 context 重建；
- 幾輪 parameter update。

它們不是同一尺度。

因此本文至少區分：

$$
\boxed{
T_{wall},
T_{compute},
K_{exp},
K_{use},
X_{eff}.
}
$$

---

# 3. Wall-Clock Time

$$
T_{wall}
$$

表示從第一次 exposure 到達到指定 competence threshold 的真實時間。

但不同硬體、模型與並行度差異很大。

所以它是部署量，而不是最乾淨的認知量。

---

# 4. Compute Time / Cost

$$
T_{compute}
$$

或：

$$
C_{compute}
$$

表示：

- inference tokens；
- training steps；
- FLOPs；
- tool calls；
- memory accesses。

這更適合比較 learning efficiency。

---

# 5. Exposure Count

$$
\boxed{
K_{exp}
}
$$

表示 AI 接觸 operator 定義／example 的次數。

但：

$$
K_{exp}=100
$$

可能只是同一例子重播 100 次。

所以不能直接當 learning amount。

---

# 6. Successful-Use Count

$$
\boxed{
K_{use}
}
$$

表示 AI 在實際 task 中正確使用 operator 的次數。

這比單純 exposure 更接近：

$$
\text{operational acquisition}.
$$

但若每次 task 結構完全相同，仍可能只是 pattern reuse。

---

# 7. Effective Exposure

因此提出：

$$
\boxed{
X_{eff}
=
\sum_i
w_i^{novel}
w_i^{coverage}
w_i^{discrimination}
w_i^{transfer}.
}
$$

每次 exposure 的權重依：

- novelty；
- semantic coverage；
- 是否區分容易混淆 operator；
- 是否測 transfer；

決定。

---

# 8. Exposure Diversity

還可以定義 exposure structure entropy：

$$
\boxed{
H_X
=
-\sum_m p(m)\log p(m),
}
$$

其中：

$$
m
$$

是 composition motif / usage pattern。

低：

$$
H_X
$$

可能表示：

> 一直看同一種用法。

高：

$$
H_X
$$

表示 exposure 涵蓋更多結構。

---

# 9. 但 Exposure Entropy 也不是越高越好

完全隨機、毫無階梯的 examples：

$$
H_X\uparrow
$$

可能反而讓學習變差。

所以需要：

$$
\boxed{
\text{Diversity}
+
\text{Curriculum Structure}.
}
$$

---

# 10. 八級 Operator Learning Ladder

本文提出第一版八級階梯。

---

## L0 — Recognition

看到：

$$
O
$$

知道：

> 這是一個合法 operator token。

不一定知道意思。

---

## L1 — Definition Recall

能回憶／重述：

$$
Definition(O).
$$

---

## L2 — Guided Imitation

給 explicit example：

$$
(x,O(x))
$$

能在高度相似案例模仿。

---

## L3 — Familiar Composition

能在已見過的 composition pattern 中使用：

$$
O_i\circ O_j.
$$

---

## L4 — Novel Composition

能把已知 operators 放進未見組合：

$$
O_a\circ O_c\circ O_b.
$$

---

## L5 — Cross-Context Transfer

換：

- wording；
- surface form；
- conversation；
- task framing；

仍能正確使用。

---

## L6 — Cross-Domain Transfer

原本在：

$$
\Omega_1
$$

學到 operator，

換到：

$$
\Omega_2
$$

仍能辨識結構並適用。

---

## L7 — Retention / Relearning

經時間、干擾、新學習後仍保留；

或忘記後再次學習明顯更快。

---

# 11. 「理解」最低應放在哪一級？

若只到：

$$
L1
$$

只是會背。

若：

$$
L2
$$

可能只是 imitation。

本文建議對 **Operational Understanding** 至少要求：

$$
\boxed{
L4+.
}
$$

也就是：

> 能在 held-out novel composition 中可靠使用。

更強版本要求：

$$
L5/L6.
$$

---

# 12. Operational Understanding

本文定義：

> **若 Agent 能在未直接示範答案的 held-out tasks 中，辨識 operator 的適用條件、與其他 operator 組合、執行正確行為、辨識失敗並在指定誤差與成本門檻下維持穩定，則稱其達到該測試域中的 Operational Understanding。**

這是工程操作定義。

不主張：

> 已解決 consciousness / semantic understanding 的哲學問題。

---

# 13. Competence Vector

不要用單一 accuracy。

定義：

$$
\boxed{
\mathbf C_O
=
(
R,
D,
I,
F,
N,
X,
P,
M
).
}
$$

其中：

- $R$：recognition；
- $D$：definition recall；
- $I$：guided imitation；
- $F$：familiar composition；
- $N$：novel composition；
- $X$：cross-context/domain transfer；
- $P$：persistence；
- $M$：misuse detection / self-correction。

---

# 14. Error Vector

相對：

$$
\mathbf C_O,
$$

定義：

$$
\boxed{
\mathbf E_{op}
=
(
e_R,e_D,e_I,e_F,e_N,e_X,e_P,e_M
).
}
$$

所以：

> 「學會」

是整個誤差向量進入 acceptable region，

不是單一答對率。

---

# 15. Tlearn 的正式定義

對誤差門檻：

$$
\boldsymbol\epsilon,
$$

穩定窗口：

$$
W,
$$

定義：

$$
\boxed{
T_{\epsilon}^{learn}
=
\inf
\left\{
t:
\mathbf E_{op}(t:t+W)
\preceq
\boldsymbol\epsilon
\right\}.
}
$$

也就是：

> 第一次進入「之後一段窗口仍然穩定達標」的時間。

---

# 16. 為什麼要 W？

如果某一次剛好答對：

$$
e_t<\epsilon,
$$

下一次又崩：

$$
e_{t+1}\gg\epsilon,
$$

不能稱穩定學會。

所以：

$$
\boxed{
\text{one success}
\neq
\text{stable acquisition}.
}
$$

---

# 17. Exposure-Based Learning Time

比 wall clock 更可比較的是：

$$
\boxed{
K_{\epsilon}^{learn}
=
\min
\{
k:
\mathbf E_{op}(k:k+W)
\preceq
\boldsymbol\epsilon
\}.
}
$$

這回答：

> 大約需要多少有效 exposure？

---

# 18. Effective-Exposure Learning Time

更進一步：

$$
\boxed{
X_{\epsilon}^{learn}
=
\inf
\{
X_{eff}:
\mathbf E_{op}
\preceq
\boldsymbol\epsilon
\}.
}
$$

這比「看幾次」更接近真正資料效率。

---

# 19. Learning Efficiency

定義：

$$
\boxed{
\eta_{learn}
=
\frac{
\Delta C_{operational}
}{
C_{exposure}
+
C_{compute}
+
C_{feedback}
}.
}
$$

即：

> 每單位學習成本換回多少 operational competence。

---

# 20. In-Context Learning 與 Persistent Learning

這是整篇最重要的區分之一。

AI 可以在當前 context：

$$
C_t
$$

讀入 operator definition，

立刻會用。

這是：

$$
\boxed{
\text{Context-Bound Acquisition}.
}
$$

但在標準 stateless invocation 中，

context 移除後，

這個新定義本身不會自動成為模型參數中的永久新知識。

因此：

$$
\boxed{
\text{In-Context Adaptation}
\neq
\text{Persistent Model Learning}.
}
$$

---

# 21. 四種 Learning Substrate

本文至少區分四種。

---

## M0 — Context Learning

operator 只存在當前 context。

優點：

- 快；
- 不需訓練。

缺點：

- context-bound；
- context cost 高。

---

## M1 — External Memory Learning

operator 存入：

- database；
- vector store；
- file；
- knowledge graph；
- protocol registry。

使用時 retrieval。

這是：

$$
\boxed{
\text{persistent externalized learning}.
}
$$

---

## M2 — Runtime / Policy Learning

operator 被加入：

- agent policy；
- workflow；
- tool router；
- compiler；
- rule system。

不一定改模型參數。

---

## M3 — Parameter / Adapter Learning

透過：

- finetuning；
- LoRA；
- adapter；
- continual pretraining；

改變模型。

這是更強的 persistent internal learning。

---

# 22. 不同 substrate 有不同 Tlearn

所以真正應寫：

$$
\boxed{
T_{\epsilon}^{learn}(M_j).
}
$$

不能拿：

> prompt 中 5 秒會用

和：

> 需要 fine-tuning 30 分鐘

直接說前者學得比較快。

因為 persistence target 不同。

---

# 23. Retrieval Latency vs Internalization Cost

M1 external memory：

- learning/store 快；
- 每次 retrieval 有成本。

M3 parameter learning：

- acquisition 慢；
- inference 時可能更直接。

因此：

$$
\boxed{
\text{Acquisition Cost}
\leftrightarrow
\text{Usage Cost}.
}
$$

---

# 24. Operator 的最佳學習 substrate 可能分層

### Rare / New
M0 / M1。

### Project Stable
M1 / M2。

### High-Frequency Universal
可能值得 M2 / M3。

因此 learning architecture 與前面的 high-frequency crystallization 相接。

---

# 25. Few-Shot Word Learning 的外部錨點

2025 年 Rapid Word Learning Through Meta In-Context Learning 提出 Minnow。

其核心結果之一是：

- 專門 meta-training 後；
- 模型可從 one / few in-context examples；
- 學習新詞；
- 區分新詞；
- 推斷 syntactic category；
- 生成合理的新用法與定義。

這支持：

$$
\boxed{
K_{exp}
\text{ can be very small}
}
$$

在某些經過適當 learning-to-learn training 的系統中。

---

# 26. 但 Word Learning 不等於 Operator Learning

新詞通常主要涉及：

- lexical semantics；
- syntax。

而 COL operator 可能同時包含：

- semantic contract；
- state transition；
- type；
- precondition；
- tool action；
- stop condition。

因此：

$$
\boxed{
T_{learn}^{operator}
}
$$

可能遠高於簡單 lexical learning。

---

# 27. Meta-Learning 可能降低 Tlearn

如果 Agent 不是第一次學 operator，

而是已學會：

> 如何學新的 operator，

則：

$$
\boxed{
\text{Learning-to-Learn}
\rightarrow
T_{\epsilon}^{learn}\downarrow.
}
$$

這是未來 COL 非常重要的可能性。

---

# 28. Operator Meta-Learner

可以訓練 Agent 面對新 operator 時，自動抽取：

```text
Name
Type
Input
Output
Precondition
Expansion
Examples
Failure
Stop
```

形成：

$$
\boxed{
\text{Operator Acquisition Routine}.
}
$$

---

# 29. Definition Alone vs Examples

只給 definition：

$$
D.
$$

只給 examples：

$$
E.
$$

給：

$$
D+E
$$

的學習效率可能不同。

因此需要比較：

$$
T(D),
T(E),
T(D+E).
$$

---

# 30. Positive Examples 不夠

如果只看 operator 成功使用：

$$
O(x)\rightarrow y,
$$

AI 可能不知道：

> 哪些情況不應該用。

因此還需要：

- negative examples；
- boundary examples；
- contrastive examples。

---

# 31. Contrastive Learning Exposure

對容易混淆：

$$
O_i,O_j,
$$

提供：

> 同一 task 為什麼應選 $O_i$ 而不是 $O_j$。

這提高：

$$
w_i^{discrimination}.
$$

因此可能大幅降低 selection-learning time。

---

# 32. Boundary Examples

尤其 high-coupling operator，

需要 examples：

```text
Use here.
Do not use here.
Escalate here.
Rollback here.
```

因為：

$$
\boxed{
\text{Knowing action}
\neq
\text{knowing applicability boundary}.
}
$$

---

# 33. Curriculum Geometry

學習順序也重要。

候選：

### Curriculum A
primitive → simple composition → deep composition。

### Curriculum B
先看高階 macro → 再展開 primitives。

### Curriculum C
交錯 top-down / bottom-up。

它們可能產生不同：

$$
T_{learn}.
$$

---

# 34. Top-Down / Bottom-Up 不一定對稱

既有 compositional-generalization 研究已觀察到：

- 從高階 compositional instructions 泛化到低階；
- 從低階泛化到更高階；

能力可能不對稱。

因此：

$$
\boxed{
T_{learn}^{bottom-up}
\neq
T_{learn}^{top-down}.
}
$$

---

# 35. Composition Depth 會改變學習時間

對 operator chain depth：

$$
d,
$$

可以定義：

$$
\boxed{
T_{learn}(d).
}
$$

很可能：

- 小 d：快速；
- 中 d：平滑增長；
- 某 threshold：明顯變難。

因此可能出現：

$$
\boxed{
\text{Learning Depth Phase Transition}.
}
$$

---

# 36. Minimum Coverage 不保證 Learning Completion

2025 年 MC² 類研究指出：

即使 demonstrations 已達 compositional components 的 theoretical minimum coverage，

advanced LLMs 也不能保證在不同 semantic-parsing datasets 上取得良好 compositional generalization。

因此：

$$
\boxed{
\text{Component Coverage}
\neq
\text{Learning Completion}.
}
$$

---

# 37. Morphological Generalization 的提醒

2025 年 morphology 研究也顯示：

- primitives / morphemes 已知；
- 但遇 novel roots；
- complexity 提高；

LLM systematicity 仍下降。

所以：

$$
\boxed{
K_{exp}
}
$$

不能只按 primitive coverage 計算。

---

# 38. Novel Composition Requirement

真正 operator learning 必須包含：

$$
\boxed{
\mathcal C_{novel}.
}
$$

即：

> 訓練中沒有直接看過的合法 composition。

---

# 39. Cross-Context Transfer

把：

- variable names；
- wording；
- task story；

全部換掉。

如果仍會用：

$$
O,
$$

才更接近 structural learning。

---

# 40. Cross-Domain Transfer

更強：

在：

$$
\Omega_1
$$

學：

> `branch-if-uncertain`

到：

$$
\Omega_2
$$

例如 robotics / research / scheduling，

仍能使用。

這測：

$$
\boxed{
\text{semantic abstraction}.
}
$$

---

# 41. Abstraction Direction 可能影響學習

2025 emergent communication 研究顯示，agents 對不同 abstraction transfer directions 會採用不同 linguistic strategies。

因此：

$$
\boxed{
\text{Transfer}
}
$$

不能只測一個方向。

---

# 42. Learning Curve

最簡候選：

$$
E(k)
=
E_{\infty}
+
(E_0-E_{\infty})
e^{-\alpha X_{eff}}.
$$

其中：

- $\alpha$：learning rate；
- $E_{\infty}$：irreducible error floor。

但這只是 baseline。

---

# 43. Power-Law Learning

也可能：

$$
\boxed{
E(X)
=
aX^{-b}+c.
}
$$

很多 learning systems 的 empirical curve 可能更接近 power law。

本文不預設哪個。

---

# 44. Phase-Transition Curve

對 compositional language，

甚至可能：

$$
E(X)
$$

長時間 plateau，

達到某個 structural coverage 後突然下降。

因此：

$$
\boxed{
\text{learning may be non-smooth}.
}
$$

---

# 45. Learning Threshold

定義：

$$
\boxed{
X_c
}
$$

為 competence 開始跨過：

$$
\tau_C
$$

的 critical effective exposure。

這是後續實驗要估的量。

---

# 46. Learning Velocity

$$
\boxed{
v_L
=
-\frac{dE}{dX_{eff}}.
}
$$

表示每單位有效 exposure 的誤差下降速度。

---

# 47. Learning Acceleration

$$
\boxed{
a_L
=
-\frac{d^2E}{dX_{eff}^2}.
}
$$

若：

$$
a_L>0,
$$

可能進入快速結晶期。

若：

$$
a_L<0,
$$

收益遞減。

---

# 48. Plateau Detection

如果：

$$
|v_L|<\tau_v
$$

持續：

$$
W,
$$

但 error 仍高：

$$
E>\epsilon,
$$

則：

$$
\boxed{
\text{Learning Plateau}.
}
$$

此時不應只增加相同 examples。

---

# 49. Plateau 的處理

可以：

- 增加 contrastive examples；
- 改 curriculum；
- 拆 operator；
- 降低 granularity；
- 增加 type；
- 換 learning substrate。

所以 plateau 也能反向修正語言設計。

---

# 50. Learnability 是 Operator Design Property

如果：

$$
O
$$

需要 1000 examples 才學會，

另一個等價 operator：

$$
O'
$$

只需 20 examples，

則：

$$
\boxed{
\text{operator notation / contract affects learning time}.
}
$$

---

# 51. Symbol Shape 是否重要？

表面 token：

```text
⟁
```

與：

```text
IndependentChallenge
```

可能有不同 learning cost。

但「熟悉自然語言名稱」也可能帶入舊語義偏差。

因此需要比較：

- arbitrary symbol；
- mnemonic symbol；
- natural-language label；
- hybrid label。

---

# 52. Prior Semantic Interference

如果 operator 名稱：

```text
merge
```

模型已經有很強既有語義，

新定義與舊語義不同，

可能：

$$
\boxed{
\text{Prior Semantic Interference}.
}
$$

這會增加：

$$
T_{learn}.
$$

---

# 53. Blank Symbol 也有成本

完全新的：

```text
⊛7
```

沒有 prior interference，

但沒有 mnemonic support。

因此：

$$
\boxed{
\text{Prior Knowledge}
}
$$

既可能是 bonus，也可能是 bias。

---

# 54. Semantic Distance

定義：

$$
d_{prior}(O)
=
D(
Meaning_{new},
PriorMeaning_{label}
).
$$

可能存在：

$$
T_{learn}
=
f(d_{prior}).
$$

這是可測命題。

---

# 55. Operator Family Learning

如果已學：

$$
O_1,O_2,O_3
$$

同 family，

新：

$$
O_4
$$

可能更快。

這是：

$$
\boxed{
\text{Family Transfer}.
}
$$

所以單 operator 學習時間會隨既有 language basis 改變。

---

# 56. Cold-Start vs Warm-Start

定義：

$$
T_{cold}(O)
$$

與：

$$
T_{warm}(O\mid\mathcal O_{known}).
$$

通常候選：

$$
\boxed{
T_{warm}<T_{cold}.
}
$$

這就是語言逐漸形成後的 network effect。

---

# 57. 但 Family Confusion 也可能增加

若 family 內 operators 太相近：

$$
\rho_{col}\uparrow,
$$

則：

$$
T_{selection}
$$

可能增加。

所以：

$$
\boxed{
\text{Transfer Benefit}
\leftrightarrow
\text{Collision Cost}.
}
$$

---

# 58. Persistence：學會多久還在？

達到：

$$
T_{\epsilon}^{learn}
$$

後仍需要：

$$
\boxed{
T_{\epsilon}^{retain}.
}
$$

定義：

$$
T_{\epsilon}^{retain}
=
\sup
\{
\Delta t:
E(t+\Delta t)\le\epsilon
\}.
$$

---

# 59. Context-Bound Retention

M0 context learning 的 retention 通常由：

- context availability；
- conversation state；
- context truncation；

決定。

它不等於 parameter forgetting。

---

# 60. External-Memory Retention

M1 需要：

- storage intact；
- retriever 找得到；
- version 可解析。

所以：

$$
\boxed{
\text{Stored}
\neq
\text{Retrievable}
\neq
\text{Usable}.
}
$$

---

# 61. Parameter Retention

M3 需要考慮：

$$
\boxed{
\text{Catastrophic Forgetting}.
}
$$

新學習可能破壞舊能力。

因此新增：

$$
F_{old}(t).
$$

---

# 62. Stability–Plasticity Tradeoff

學得快：

$$
Plasticity\uparrow.
$$

但可能：

$$
Forgetting\uparrow.
$$

所以：

$$
\boxed{
\text{Learning Speed}
\neq
\text{Long-Term Learning Quality}.
}
$$

---

# 63. 2026 SCALE 的邊界

SCALE 類 continual-learning 研究明確處理：

- preserve old behavior；
- adapt to new knowledge；

的 trade-off。

其結果再次表明：

$$
\boxed{
\text{Preservation}
\leftrightarrow
\text{Adaptation}
}
$$

需要共同設計。

---

# 64. OAKS：Online Adaptation 仍然困難

2026 OAKS benchmark 測 continual knowledge stream。

即使 state-of-the-art models 與 agentic memory systems，

仍會：

- state-tracking delay；
- 被 distraction 影響；
- adaptation 不夠 robust。

因此：

$$
\boxed{
\text{having memory infrastructure}
\neq
\text{robust continual acquisition}.
}
$$

---

# 65. Relearning

若一個 operator 被忘記：

$$
E>\epsilon,
$$

重新 exposure 後：

$$
K_{relearn}
$$

可能比最初：

$$
K_{initial}
$$

小。

---

# 66. Relearning Savings

定義：

$$
\boxed{
S_{relearn}
=
1-
\frac{
K_{relearn}
}{
K_{initial}
}.
}
$$

若：

$$
S_{relearn}>0,
$$

表示仍有 residual learning trace。

---

# 67. 完全忘記不一定真的「沒有留下」

如果 overt performance 下降，

但重新學習明顯更快，

可能仍有 latent trace。

因此：

$$
\boxed{
\text{performance forgetting}
\neq
\text{zero residual representation}.
}
$$

本文不對內部表徵作強斷言，只把 relearning savings 當行為量。

---

# 68. Interference Test

學完：

$$
O_A,
$$

再學：

$$
O_B.
$$

若：

$$
O_B
$$

和：

$$
O_A
$$

語義相近，

測：

$$
Retention(O_A).
$$

這可以估：

$$
\boxed{
\text{Operator Interference}.
}
$$

---

# 69. Sequential Language Expansion

真正 COL 不是一次學完全部。

而是：

$$
\mathcal O_1
\rightarrow
\mathcal O_2
\rightarrow
\cdots.
$$

所以需要測：

> 第 100 個 operator 的 learning time 是否比第 10 個更長？

---

# 70. Learning-Time Scaling

定義：

$$
\boxed{
T_{learn}(N_{known})
}
$$

觀察隨既有 vocabulary 增長：

- transfer 讓它下降；
- collision 讓它上升。

可能 U 型或非單調。

---

# 71. Language Saturation in Learning

若：

$$
N_{known}
$$

超過某值後，

新 operator：

- 很難找到唯一 semantic niche；
- 與舊 operator 太相似；

則：

$$
T_{learn}\uparrow.
$$

這和 LRC–COL-04 的 $N_{\max}$ 接合。

---

# 72. Operational Understanding Gate

本文提出第一版 gate：

一個 operator $O$ 只有同時滿足以下條件，才稱「在 domain $\Omega$ 、persistence mode $M$ 下達到 operational understanding」：

1. recognition accuracy ≥ $\tau_R$ ；
2. selection accuracy ≥ $\tau_S$ ；
3. familiar composition ≥ $\tau_F$ ；
4. novel composition ≥ $\tau_N$ ；
5. semantic fidelity ≥ $\tau_{sem}$ ；
6. misuse / boundary detection ≥ $\tau_B$ ；
7. held-out stability 維持 $W$ ；
8. 若宣稱 persistent，retention ≥ $\tau_P$。

---

# 73. 不同應用可以有不同門檻

低風險：

$$
\tau_N=0.9
$$

可能足夠。

高風險：

$$
\tau_N=0.999...
$$

可能仍不夠。

因此：

$$
\boxed{
T_{\epsilon}^{learn}
}
$$

一定是 risk-conditioned。

---

# 74. Learning Time 和 Reality Coupling 接合

如果 operator：

$$
\kappa_{LR}
$$

高，

誤用代價高。

所以 high-coupling operator 應要求：

- 更多 boundary exposure；
- 更高 fidelity；
- 更長 stability window。

因此：

$$
\boxed{
\kappa_{LR}\uparrow
\Rightarrow
T_{qualify}\uparrow
}
$$

可能成立。

---

# 75. 「學會」與「允許執行」可以分開

Agent 可以先達：

$$
L4
$$

但只允許 sandbox。

直到：

$$
L7
$$

才取得 production permission。

這是：

$$
\boxed{
\text{Capability Acquisition}
\neq
\text{Execution Authorization}.
}
$$

---

# 76. Staged Permission Curriculum

例如：

```text
Stage 0: explain
Stage 1: simulate
Stage 2: sandbox
Stage 3: reversible real action
Stage 4: high-coupling action
```

這讓 learning 與 reality coupling 安全接軌。

---

# 77. Multi-Agent Learning

一個 Agent 學會 operator 後，

能否教：

$$
A_2?
$$

這涉及：

$$
\boxed{
T_{transmit}.
}
$$

不是只有：

$$
T_{learn}.
$$

---

# 78. Teaching Efficiency

定義：

$$
\boxed{
\eta_{teach}
=
\frac{
Competence(A_2)
}{
CommunicationCost(A_1\rightarrow A_2)
}.
}
$$

這直接接後面的傳播研究。

---

# 79. Teacher Compression Risk

如果：

$$
A_1
$$

把 operator 過度壓縮成短符號，

 $A_2$ 學習時間可能反而增加。

所以：

$$
\boxed{
\text{Teacher Compression}
\leftrightarrow
\text{Learner Reconstruction Cost}.
}
$$

---

# 80. Learning-Time / Language-Size Feedback

如果某 operator：

$$
T_{learn}
$$

太高，

可能不值得進 stable basis。

因此：

$$
\boxed{
T_{learn}
}
$$

本身會反向影響：

$$
N_{\max}^{effective}.
$$

---

# 81. Learning-Time Admission Gate

新增 operator：

$$
O
$$

除了前面的 utility gate，

還要求：

$$
\boxed{
T_{\epsilon}^{learn}(O)
\le
B_{learn}.
}
$$

否則：

- 改名；
- 拆分；
- 加 examples；
- 降粒度；
- 留 local layer。

---

# 82. Learnability-Adjusted Operator Utility

前面：

$$
\Delta J(O).
$$

現在加入：

$$
\boxed{
\Delta J_L(O)
=
\Delta J(O)
-
\lambda T_{\epsilon}^{learn}(O)
-
\mu C_{retain}(O).
}
$$

---

# 83. Stable Language 不只要可表達

它還要：

$$
\boxed{
\text{teachable}.
}
$$

這是本篇很重要的新限制。

---

# 84. AI-native Language 的特殊目標

人類語言通常經過世代演化。

COL 可以第一次把：

- operator design；
- curriculum；
- learning metric；
- runtime；

聯合優化。

因此可以主動尋找：

$$
\boxed{
\text{machine-teachable language}.
}
$$

---

# 85. 但不能只為單一模型優化

如果只讓：

$$
A_1
$$

學得超快，

其他：

$$
A_2,A_3
$$

很難，

通用傳播差。

因此還要：

$$
\boxed{
T_{learn}^{shared}
}
$$

跨 Agent family 評估。

---

# 86. Shared Learning Time

例如：

$$
\boxed{
T_{learn}^{shared}
=
Q_{p}
\{
T_{learn}(A_i)
\},
}
$$

用某個高分位數，而不是只看平均。

避免語言只適合少數模型。

---

# 87. Learning Equity Across Agents

這不是社會意義上的 equity，而是工程上的：

> 同一 operator language 是否只對特定 architecture 特別容易？

可以報：

$$
Var_A[T_{learn}].
$$

variance 太高，通用性差。

---

# 88. 第一批正式命題

## LT-P1 — Recall–Use Gap

definition recall 達標不保證 operational use 達標。

## LT-P2 — Novel-Composition Threshold

operational understanding 至少需要 held-out novel composition。

## LT-P3 — Effective Exposure

學習時間比 raw exposure count 更依賴 exposure 的 novelty、coverage 與 discrimination。

## LT-P4 — Meta-Learning Acceleration

learning-to-learn training 可降低新 operator 的 $T_{\epsilon}^{learn}$。

## LT-P5 — Depth-Dependent Learning

operator composition depth 上升會增加 learning time，且可能存在 phase transition。

## LT-P6 — Prior-Semantics Dual Effect

已有語義可以加速學習，也可以因 mismatch 造成 interference。

## LT-P7 — Family Transfer vs Collision

已知 operator family 可加速新成員學習，但過密 family 會增加 selection interference。

## LT-P8 — Persistence-Mode Dependence

context learning、external memory、runtime policy 與 parameter learning 的 $T_{\epsilon}^{learn}$ 不可直接比較。

## LT-P9 — Stability–Plasticity Tradeoff

更快 persistent adaptation 可能增加對既有能力的 forgetting。

## LT-P10 — Relearning Savings

表面 forgetting 後的 relearning speed 可以揭示 residual acquisition。

## LT-P11 — Coupling-Conditioned Qualification

reality-coupling 越高的 operator 應有更嚴格的 learning / retention threshold。

## LT-P12 — Learnability-Constrained Vocabulary

operator 的 learning time 會反向限制有效 vocabulary size。

---

# 89. 第一版實驗：Single Operator Acquisition

設計一個完全新、無既有名稱語義的 operator：

$$
O_X.
$$

分組給：

### E1
definition only。

### E2
2 positive examples。

### E3
definition + positive。

### E4
definition + positive + negative。

### E5
definition + contrastive + boundary。

測：

$$
K_{\epsilon}^{learn}.
$$

---

# 90. Novel Composition Test

學：

$$
O_A,O_B,O_C.
$$

training 只出現：

$$
A\circ B,
\quad
B\circ C.
$$

測：

$$
A\circ C,
$$

$$
C\circ A,
$$

$$
A\circ B\circ C.
$$

---

# 91. Depth Sweep

訓練到：

$$
d\le3.
$$

測：

$$
d=4,5,6,\ldots.
$$

量：

$$
T_{learn}(d)
$$

與：

$$
d_{crit}.
$$

---

# 92. Cross-Context Test

同 operator：

- 換名稱；
- 換情境；
- 換自然語言描述；
- 換 variable。

確認不是 lexical memorization。

---

# 93. Cross-Domain Test

從：

$$
\Omega_1
$$

學，

在：

$$
\Omega_2
$$

用。

例如：

```text
branch
```

先在 research，

再到 scheduling / software / robot planning。

---

# 94. Retention Test

達標後：

$$
\Delta t=
1h,1d,1w,\ldots
$$

依 learning substrate 測。

M0 context-bound 不應假裝可以測 parameter retention。

---

# 95. Interference Test

依序：

$$
O_1
\rightarrow
O_2
\rightarrow
\cdots
\rightarrow
O_k.
$$

每新增一個，

回測舊 operators。

得到：

$$
\boxed{
ForgettingMatrix_{ij}.
}
$$

---

# 96. Relearning Test

讓：

$$
O_i
$$

下降到 criterion 以下，

重新提供少量 exposure。

比較：

$$
K_{initial}
$$

與：

$$
K_{relearn}.
$$

---

# 97. Substrate Comparison

同一 operator：

### M0
context。

### M1
external memory。

### M2
runtime policy。

### M3
adapter / finetune。

比較：

- acquisition time；
- inference cost；
- transfer；
- retention；
- forgetting；
- update cost。

---

# 98. Curriculum Comparison

比較：

### Bottom-Up
primitive → macro。

### Top-Down
macro → expansion。

### Interleaved
兩者交錯。

測：

$$
T_{\epsilon}^{learn},
$$

$$
F_{sem},
$$

$$
Transfer.
$$

---

# 99. Learning-Time Profile

最終每個 operator 不應只存：

```text
Name
Definition
Version
```

還應保存：

```text
Estimated Learning Time
Required Examples
Known Confusions
Depth Limit
Transfer Evidence
Retention Mode
Relearning Cost
```

形成：

$$
\boxed{
\text{Operator Learnability Profile}.
}
$$

---

# 100. Language-Level Learnability

整套 language：

$$
\mathcal O
$$

可定義：

$$
\boxed{
T_{\epsilon}^{language}
}
$$

但它不能只是所有 operator learning time 相加。

因為：

- shared types；
- family transfer；
- compositional reuse；

會產生共享學習收益。

---

# 101. Curriculum Compression

學完 core：

$$
\mathcal O_C,
$$

後續 domain extension：

$$
\mathcal O_D
$$

可能學得更快。

因此語言完整學習曲線可能：

$$
\boxed{
\text{slow core acquisition}
\rightarrow
\text{fast extension acquisition}.
}
$$

這是很值得測的候選現象。

---

# 102. Core Learning Investment

如果 universal core 的學習成本高，

但之後每個 domain：

$$
T_{extension}\downarrow,
$$

長期仍可能值得。

這需要 lifecycle learning yield：

$$
\boxed{
Y_{learn}^{life}
=
\frac{
\text{future acquisition savings}
}{
\text{core learning cost}
}.
}
$$

---

# 103. 這與 LRC 的接點

一套語言 action yield 很高，

但 learning cost 極高，

可能不適合通用傳播。

因此真正：

$$
\boxed{
Y_{COL}
=
Y_L
-
\lambda C_{learn}.
}
$$

---

# 104. AI 要「多久懂」的第一版回答

現在可以正式回答：

> 沒有單一秒數或 exposure 次數。

真正答案形式應是：

$$
\boxed{
T_{\epsilon}^{learn}
=
f(
O,
A,
M,
Curriculum,
Depth,
Prior,
Risk,
Persistence
).
}
$$

其中：

- $O$：operator；
- $A$：Agent；
- $M$：learning substrate；
- Curriculum：exposure structure；
- Depth：composition complexity；
- Prior：prior semantic compatibility；
- Risk：qualification threshold；
- Persistence：需要維持多久。

---

# 105. 最重要的新區分

因此未來我們不能說：

> 「AI 看一次就懂了。」

更精確：

> 「AI 在 M0 context mode 下，一次 exposure 後已能 definition recall。」

或：

> 「經 12 effective exposures 後，在 depth≤4 的 held-out novel compositions 上達到 98% fidelity，並維持 100-task window。」

這才是工程語言。

---

# 106. 本篇核心公式組

有效 exposure：

$$
\boxed{
X_{eff}
=
\sum_i
w_i^{novel}
w_i^{coverage}
w_i^{discrimination}
w_i^{transfer}.
}
$$

Operational learning time：

$$
\boxed{
T_{\epsilon}^{learn}
=
\inf
\{
t:
\mathbf E_{op}(t:t+W)
\preceq
\boldsymbol\epsilon
\}.
}
$$

exposure learning time：

$$
\boxed{
K_{\epsilon}^{learn}
=
\min
\{
k:
\mathbf E_{op}(k:k+W)
\preceq
\boldsymbol\epsilon
\}.
}
$$

relearning savings：

$$
\boxed{
S_{relearn}
=
1-
\frac{K_{relearn}}{K_{initial}}.
}
$$

learnability-adjusted utility：

$$
\boxed{
\Delta J_L(O)
=
\Delta J(O)
-
\lambda T_{\epsilon}^{learn}(O)
-
\mu C_{retain}(O).
}
$$

---

# 107. 非主張

本文不主張：

1. engineering operational understanding 等於哲學意義的理解；
2. 一次 few-shot 成功等於 persistent learning；
3. in-context learning 會自動寫入模型參數；
4. 所有 operator 都應 parameterize；
5. exposure entropy 越高越好；
6. learning curve 一定 exponential 或 power-law；
7. $L4$ 是所有 domain 唯一理解門檻；
8. relearning savings 證明特定 hidden representation 存在；
9. continual-learning 方法已解決 catastrophic forgetting；
10. 不同 Agent 的 learning time 可以無條件直接比較。

本文只提出：

$$
\boxed{
\text{Operator learning should be evaluated as stable, transferable, fidelity-bounded operational competence under an explicit learning and persistence substrate.}
}
$$

---

# 108. 文獻錨點

1. **Rapid Word Learning Through Meta In-Context Learning（EMNLP 2025）**  
   Minnow 透過 meta-training 培養 few-shot word-learning ability；模型能從 one / few in-context examples 區分新詞、推斷 syntactic category、生成新用法與定義。這支持「learning-to-learn 可以大幅降低新符號 acquisition cost」。

2. **MC²: A Minimum-Coverage and Dataset-Agnostic Framework for Compositional Generalization of LLMs on Semantic Parsing（EMNLP Findings 2025）**  
   在 demonstrations 僅達 compositional minimum-coverage lower bound 時，advanced LLMs 仍無法保證跨 datasets 的良好 compositional generalization。這支援「primitive / component coverage 不等於 operational learning completion」。

3. **Evaluating Morphological Compositional Generalization in Large Language Models（NAACL 2025）**  
   顯示 LLM 對 novel roots 與更高 morphological complexity 的 compositional generalization 仍明顯下降，支持 depth / novelty 應進入 learning-time 模型。

4. **ModeLing: A Novel Dataset for Testing Linguistic Reasoning in Language Models（2025）**  
   用全新 Linguistics Olympiad-style puzzles 測試模型從少量 examples 推斷陌生語言規則的 few-shot inductive / compositional reasoning，提供「未知符號／未知語法學習」的外部測試錨點。

5. **Agents generalize to novel levels of abstraction by using adaptive linguistic strategies（ACL Findings 2025）**  
   顯示不同 abstraction generalization directions 可誘發不同 linguistic strategies，支持 cross-domain / abstraction transfer 不應只測單一方向。

6. **Continual Learning of Large Language Models（EMNLP Tutorial 2025）**  
   系統整理 continual pre-training、instruction tuning、alignment 與 lifelong agents 中 adaptation / forgetting 的核心問題，支持 persistent learning 必須和 context-bound learning 分開。

7. **Can Large Language Models Keep Up? Benchmarking Online Adaptation to Continual Knowledge Streams（ACL 2026）**  
   OAKS 顯示 state-of-the-art models 與 agentic memory systems 在 streaming knowledge 下仍有 adaptation delays 與 distraction susceptibility，說明「有記憶機制」不等於「持續學習已解決」。

8. **SCALE: Upscaled Continual Learning of Large Language Models（ACL Findings 2026）**  
   透過 preservation / adaptation 結構降低 forgetting，並明確呈現 persistent learning 的 stability–plasticity tradeoff。

---

# 109. 下一篇

## LRC–COL-08：語言穩定步數、語義漂移與穩定窗口
### Language Stabilization Steps, Semantic Drift, and Stability Windows

下一篇將正式處理：

$$
\boxed{
K_{\epsilon}^{stable}.
}
$$

它與本篇不同。

本篇問：

> AI 幾次 exposure 後會用？

下一篇問：

> **整套語言經過多少次使用、重新解讀、跨 Agent 傳遞與版本更新後，才有資格說「這個 operator 的意思暫時穩定了」？**

將建立：

- semantic drift trajectory；
- expansion/recompression drift；
- cross-agent disagreement；
- stability window；
- semantic checksum / invariant；
- convergence；
- false convergence；
- stability vs frozen-language；

並正式區分：

$$
\boxed{
\text{Agent Learns the Language}
\neq
\text{Language Itself Is Stable}.
}
$$

**END — LRC–COL-07 v0.1**
