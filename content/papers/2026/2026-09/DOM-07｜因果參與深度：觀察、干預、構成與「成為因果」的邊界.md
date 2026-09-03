# DOM-07｜因果參與深度：觀察、干預、構成與「成為因果」的邊界

## Causal Participation Depth: Observation, Intervention, Constitution, and the Limits of “Becoming Causality”

**系列：** Dynamic Operational Metaphysics（DOM）／動態可操作形而上學  
**篇次：** 07 / 08  
**文件編號：** EML-DOM-07-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-20  
**版本：** v0.1 Canonical Draft  
**文件性質：** 理論整合論文／因果參與／觀察—干預—嵌入—構成／因果認識論／具身與主體  
**證據狀態：** 本文主要建立形式化概念接口。interventionist causation、active causal discovery、scientific experimentation、embodied AI 與 causal modelling 僅作外部結構對照。本文不主張「越深參與就必然越理解」，也不主張任何存在能因「成為系統的一部分」而獲得對該系統的全知。

---

## 摘要

在因果研究中，外部觀察、主動干預、嵌入系統、成為系統構成部分，以及與系統在身份層級高度整合，常被直覺地排列成一條「越深入就越接近真正理解」的階梯。這種直覺有其吸引力：只看一個系統，與能改變它、進入它、承受它的因果規則，似乎確實是不同認識位置。

然而，如果直接寫成：

$$
\boxed{
\text{Participation Depth}
\uparrow
\Rightarrow
\text{Understanding}
\uparrow
}
$$

會過強。

本文提出 **Causal Participation Depth（因果參與深度）**，將觀察者與因果域的關係拆成一組可索引狀態，而不是把「參與」當成單一程度。

基本形式為：

$$
\boxed{
P_C
=
P_C(O,W,\alpha,t,c),
}
$$

其中：

- $O$：observer / agent；
- $W$：world / causal system；
- $\alpha$：participation type；
- $t$：time；
- $c$：condition。

第一版 participation ladder 為：

$$
\boxed{
P_0
\rightarrow
P_1
\rightarrow
P_2
\rightarrow
P_3
\rightarrow
P_4,
}
$$

其中：

- $P_0$：External Observation；
- $P_1$：Intervention；
- $P_2$：Embedded Participation；
- $P_3$：Constitutive Participation；
- $P_4$：Identity-Level Integration。

但本文明確指出：這不是價值排名，也不是 epistemic superiority 的單調階梯。

本文第一核心命題為：

$$
\boxed{
\text{Participation}
\not\Rightarrow
\text{Understanding}.
}
$$

第二核心命題為：

$$
\boxed{
\text{Understanding}
\not\Rightarrow
\text{Prediction}.
}
$$

第三核心命題為：

$$
\boxed{
\text{Prediction}
\not\Rightarrow
\text{Control}.
}
$$

第四核心命題為：

$$
\boxed{
\text{Control}
\not\Rightarrow
\text{Authority}.
}
$$

因此完整 Non-Collapse Chain 為：

$$
\boxed{
\text{Participation}
\not\Rightarrow
\text{Understanding}
\not\Rightarrow
\text{Prediction}
\not\Rightarrow
\text{Control}
\not\Rightarrow
\text{Authority}.
}
$$

本文保留一個較弱而可研究的候選猜想：

$$
\boxed{
P_C\uparrow
\rightsquigarrow
\text{possible expansion of epistemic access}.
}
$$

符號：

$$
\rightsquigarrow
$$

只表示可能的研究路徑，不是必然推出。

這種降格與現代因果研究相容。2025 年的 causal-discovery work 顯示，主動 intervention 可以提高 causal direction / structure identification；ICML 2025 的 Bayesian active learning 甚至在 embodied AI environment 中展示 sequential intervention 的效益。然而，2025 年科學哲學對 experiment / intervention 的分析同時指出，active intervention 並非取得高品質證據或揭露因果結構的唯一方法；自然實驗、觀察研究與其他 non-interventionist studies 在適當條件下也能具有重要 epistemic value。換句話說：

$$
\boxed{
\text{Intervention}
\neq
\text{Universal Epistemic Supremacy}.
}
$$

本文因此不把：

$$
P_1>P_0
$$

理解成所有任務中的「比較知道」。

本文進一步提出 **Participation Profile**：

$$
\boxed{
\mathbf P
=
\left\langle
P_O,
P_I,
P_E,
P_K,
P_{ID}
\right\rangle
}
$$

分別表示 observational、interventional、embedded、constitutive 與 identity-level participation。不同 systems 可以在不同軸上高低不一。

本文最重要的新修正則針對一句極端直覺：

> 「要真正理解因果，至少需要成為因果本身。」

DOM-07 將其改寫為：

$$
\boxed{
\text{to become part of a causal process}
\neq
\text{to become identical to the total causal domain}.
}
$$

更進一步：

$$
\boxed{
\text{Constitutive Participation}
\not\Rightarrow
\text{Complete Causal Self-Knowledge}.
}
$$

人體就是最直接的直覺反例：一個主體是其生物因果網路的一部分，甚至可被視為由其構成，但並不知道每一個細胞、分子、神經回路的即時因果狀態。DOM-03 已建立「包含不等於全知」，DOM-06 又建立「高度整合不等於完整知識」；因此「成為系統」若不拆 relation，仍會把構成、身份、觀察、控制與理解偷換成同一件事。

本文最後建立 **Participation Certificate、Epistemic Access Gain、Intervention Burden、Embeddedness Cost、Constitutive Blind Spot、Participation Reversal** 與 **Causal Intimacy Without Omniscience**。其目的不是否定深度參與可能帶來新知識，而是建立一個能精確描述：

> 進入因果域究竟增加了什麼，又仍然不知道什麼？

的可操作框架。

---

## 關鍵詞

Causal Participation Depth；Intervention；Observation；Embedded Agency；Constitutive Participation；Causal Understanding；Causal Discovery；Active Learning；Embodied AI；Causal Intimacy；Participation–Knowledge Separation；因果參與；干預；因果理解；嵌入式主體

---

# 0. 研究定位與非主張

本文不主張：

1. intervention 永遠優於 observation；
2. embedded observer 永遠比 external observer 更理解系統；
3. constitutive participation 必然提升 causal knowledge；
4. identity-level integration 必然帶來 subjective unity；
5. 參與越深就一定越接近真理；
6. 具身化必然提升所有因果推理；
7. controllability 等於 understandability；
8. manipulability 等於 complete causation；
9. causation 已被 interventionism 唯一決定；
10. 所有因果只能透過 intervention 發現；
11. first-person experience 可直接取代第三人稱證據；
12. external science 無法理解 internal processes；
13. 成為 system 的一部分等於成為 system 本身；
14. 成為 system 本身等於知道 system 的全部 microstate；
15. causal participation 自動生成 normative authority。

本文真正主張：

$$
\boxed{
\text{participation type and epistemic value must be modeled separately}.
}
$$

---

# 1. 為什麼「參與因果」需要分層？

考慮五種情境：

1. 天文學家觀察遙遠星系；
2. 實驗者改變一個變量；
3. robot agent 在環境中行動並收到 feedback；
4. 某 agent 是 system dynamics 的內部構成元；
5. 多個 subselves 與 higher system 高度 identity-level integration。

都可以說：

> observer 與 causal system 有關係。

但 relation 明顯不同。

---

# 2. 基本定義

本文定義：

$$
\boxed{
P_C
=
P_C(O,W,\alpha,t,c).
}
$$

其中：

$$
\alpha
\in
\{
obs,
int,
embed,
constitute,
identity
\}.
$$

---

# 3. Participation Ladder

第一版：

$$
\boxed{
P_0
\rightarrow
P_1
\rightarrow
P_2
\rightarrow
P_3
\rightarrow
P_4.
}
$$

但箭頭只表示「更深的結構耦合可能」，不是：

$$
Knowledge(P_0)
<
Knowledge(P_1)
<
\cdots
<
Knowledge(P_4).
$$

---

# 4. $P_0$：External Observation

$$
\boxed{
P_0(O,W)
}
$$

表示：

> O 透過 observation channel 取得 W 的 information，但不主動操控 W 的 target variables，也不必成為 W 的內部 functional constituent。

---

# 5. External Observation 並不等於弱科學

很多領域：

- astronomy；
- geology；
- paleontology；
- epidemiology；
- ethology；

大量依賴 observational / natural-experimental evidence。

所以：

$$
\boxed{
P_0
\not\Rightarrow
\text{epistemically weak}.
}
$$

---

# 6. Observation Channel

定義：

$$
\boxed{
\Gamma^{obs}_{W\rightarrow O}.
}
$$

其資訊品質受：

- noise；
- bandwidth；
- calibration；
- model；
- selection effects；
- temporal resolution；

限制。

---

# 7. $P_1$：Intervention

$$
\boxed{
P_1(O,W)
}
$$

表示 O 能對某 variable / subsystem 執行：

$$
do(X=x)
$$

或其他合法 intervention。

---

# 8. Intervention 的認識價值

在 causal discovery 中，觀察資料可能無法區分某些 causal orientations，而 intervention 可以破除 observational equivalence。

因此：

$$
\boxed{
\text{intervention can increase causal identifiability}.
}
$$

2025 AAAI 的 intervention-design work 直接研究最小 intervention sets 以提高 causal structure identifiability；ICML 2025 的 Bayesian active learning 則用 sequential interventions 來辨識 causal direction。

---

# 9. Intervention 不是萬能

即使：

$$
P_1=1,
$$

也可能：

- intervention 不乾淨；
- manipulation 有 side effects；
- latent confounder 未處理；
- target variable representation 錯；
- measurement 失真；
- system nonstationary。

所以：

$$
\boxed{
\text{Intervention}
\not\Rightarrow
\text{Correct Causal Model}.
}
$$

---

# 10. Experiment ≠ Intervention by Definition

2025 科學哲學研究明確挑戰「experiment 必然等於 active intervention」的 received view，指出一些 observational、natural-experiment、simulation-based studies 也可構成 experiment proper，且 intervention 並不 ceteris paribus 保證 epistemically superior evidence。

DOM-07 因此固定：

$$
\boxed{
\text{Intervention}
\neq
\text{Universal Epistemic Supremacy}.
}
$$

---

# 11. $P_2$：Embedded Participation

$$
\boxed{
P_2(O,W)
}
$$

表示：

> O 的 sensing / action / learning loop 發生在 W 內部，且 O 的後續 state 依賴 W 的 causal feedback。

形式：

$$
x_O(t+1)
=
f_O
\left(
x_O(t),
y_W(t),
a_O(t)
\right).
$$

---

# 12. Embeddedness

定義：

$$
\boxed{
E(O,W)>0
}
$$

若 O 的可持續 operation 依賴 W 內部 feedback。

robot、animal、economic agent、software agent 都可在不同意義上是 embedded。

---

# 13. Embedded Observer 可能取得外部觀察不到的 channel

例如：

- proprioception；
- local contact；
- action consequence；
- endogenous reward；
- first-person control signal。

所以：

$$
\boxed{
P_2
\rightsquigarrow
\text{new epistemic channels}.
}
$$

但不是必然提升總理解。

---

# 14. Embedded Blindness

embedded agent 也可能因 local perspective 看不到 global structure。

因此：

$$
\boxed{
\text{embeddedness}
\not\Rightarrow
\text{global visibility}.
}
$$

---

# 15. Local Causal Privilege / Global Causal Blindness

可以同時：

$$
Access_{\mathrm{local}}\uparrow
$$

而：

$$
Access_{\mathrm{global}}\downarrow.
$$

這是 Participation Tradeoff。

---

# 16. $P_3$：Constitutive Participation

$$
\boxed{
P_3(O,W)
}
$$

表示：

> O 不只是位於 W 內，而是 W dynamics 的 constitutive subsystem。

例如：

$$
x_W
=
(x_O,x_R).
$$

O 的 state transition 直接構成 W 的一部分。

---

# 17. Constitutive Participation ≠ Identity

如果：

$$
O
\subset_{\mathrm{constitutive}}
W,
$$

不能推出：

$$
O=W.
$$

沿用 DOM-03：

$$
\boxed{
\text{Part-of}
\not\Rightarrow
\text{Whole Identity}.
}
$$

---

# 18. Constitutive Participation ≠ Self-Knowledge

即使 O 是 W 的一部分：

$$
P_3=1,
$$

也可能：

$$
K_O(W)\ll1.
$$

所以：

$$
\boxed{
\text{being constitutive}
\not\Rightarrow
\text{knowing the whole}.
}
$$

---

# 19. 人體反例

人類：

$$
H
$$

是人體 dynamics 的 constitutive high-level process。

但 ordinary conscious access 不包含：

- every cell state；
- every synaptic event；
- immune microstate；
- endocrine microstate。

因此：

$$
\boxed{
\text{constitutive intimacy}
\neq
\text{microstate omniscience}.
}
$$

---

# 20. $P_4$：Identity-Level Integration

$$
\boxed{
P_4(O,W)
}
$$

表示：

> O 與 W 在指定 identity criterion / higher-self structure 下高度整合。

例如：

- shared control；
- shared memory；
- shared narrative；
- shared external identity；
- highly integrated higher self。

---

# 21. $P_4$ 仍不推出 Numerical Identity

沿用 DOM-05：

$$
\boxed{
I_{\mathrm{control}},
I_{\mathrm{memory}},
I_{\mathrm{narrative}}
\approx1
\not\Rightarrow
I_{\mathrm{subjective}}=1.
}
$$

---

# 22. Identity-Level Integration ≠ Complete Knowledge

沿用 DOM-06：

$$
\boxed{
\text{High Integration}
\not\Rightarrow
\text{Complete Knowledge}.
}
$$

所以：

$$
P_4
$$

不是 omniscience level。

---

# 23. Participation Profile

本文定義：

$$
\boxed{
\mathbf P
=
\left\langle
P_O,
P_I,
P_E,
P_K,
P_{ID}
\right\rangle.
}
$$

其中：

- $P_O$：observational；
- $P_I$：interventional；
- $P_E$：embedded；
- $P_K$：constitutive；
- $P_{ID}$：identity-level integration。

---

# 24. Participation Profile 不是單一 scalar

某 agent 可能：

$$
P_O\gg0,
$$

$$
P_I=0,
$$

$$
P_E=0.
$$

例如 telescope observer。

另一些：

$$
P_E\gg0,
$$

但：

$$
P_O^{global}\ll1.
$$

例如 local embodied agent。

---

# 25. Epistemic Access Profile

定義：

$$
\boxed{
\mathbf E_A
=
\left\langle
E_{\mathrm{state}},
E_{\mathrm{counterfactual}},
E_{\mathrm{mechanism}},
E_{\mathrm{local}},
E_{\mathrm{global}},
E_{\mathrm{first-person}},
E_{\mathrm{historical}}
\right\rangle.
}
$$

Participation 與 Epistemic Access 應分開。

---

# 26. Participation–Access Map

定義候選：

$$
\boxed{
\Psi_P:
\mathbf P
\rightarrow
\mathbf E_A.
}
$$

但：

$$
\Psi_P
$$

不是 universal monotonic function。

---

# 27. External Observer 的優勢

 $P_0$ 有時更適合：

- global comparison；
- long baseline；
- low perturbation；
- independent replication；
- cross-system observation。

---

# 28. Intervening Observer 的優勢

 $P_1$ 有時更適合：

- direction identification；
- counterfactual testing；
- mechanism isolation；
- causal discrimination。

---

# 29. Embedded Observer 的優勢

 $P_2$ 有時更適合：

- local sensorimotor contingencies；
- real-time feedback；
- context-sensitive causal coupling；
- affordance discovery。

---

# 30. Constitutive Participant 的優勢

 $P_3$ 可能取得：

- endogenous signals；
- internal constraints；
- control conflict；
- internal latency；
- component-specific causal history。

但仍可能缺 global overview。

---

# 31. Identity-Level Integration 的可能優勢

 $P_4$ 可能增加：

- shared state；
- shared memory；
- cross-part coordination；
- higher-level narrative access。

但不能推出所有 local microstates 都升到 higher self awareness。

---

# 32. Causal Intimacy

本文定義：

$$
\boxed{
C_I(O,W)
}
$$

為 observer 與 W 的 causal intimacy profile。

它綜合：

- feedback reciprocity；
- state coupling；
- intervention access；
- dependence；
- constitutive role；
- identity integration。

---

# 33. Causal Intimacy ≠ Causal Understanding

所以：

$$
\boxed{
C_I\uparrow
\not\Rightarrow
U_C\uparrow
}
$$

其中：

$$
U_C
$$

表示 causal understanding。

---

# 34. Causal Understanding

本文暫定：

$$
\boxed{
U_C
=
\left\langle
U_{\mathrm{predict}},
U_{\mathrm{counterfactual}},
U_{\mathrm{mechanism}},
U_{\mathrm{intervention}},
U_{\mathrm{scope}},
U_{\mathrm{failure}}
\right\rangle.
}
$$

即理解至少包括：

- prediction；
- counterfactuals；
- mechanism；
- intervention consequences；
- scope；
- failure conditions。

---

# 35. Understanding ≠ Prediction

一個 black-box predictor 可以：

$$
Predict\approx1
$$

但：

$$
MechanismUnderstanding\ll1.
$$

所以：

$$
\boxed{
\text{Prediction}
\not\Rightarrow
\text{Mechanistic Understanding}.
}
$$

---

# 36. Understanding ≠ Control

知道：

$$
X\to Y
$$

不表示有 actuator / permission 改 X。

所以：

$$
\boxed{
U_C
\not\Rightarrow
Control.
}
$$

---

# 37. Control ≠ Understanding

反過來也成立。

某 system 可以有：

```text
reset()
```

卻不知道 internal mechanism。

所以：

$$
\boxed{
Control
\not\Rightarrow
Understanding.
}
$$

---

# 38. Control ≠ Authority

沿用 DOM-04：

$$
\boxed{
CanControl(O,W)
\not\Rightarrow
MayControl(O,W).
}
$$

---

# 39. Full Non-Collapse Chain

因此：

$$
\boxed{
\text{Participation}
\not\Rightarrow
\text{Understanding}
\not\Rightarrow
\text{Prediction}
\not\Rightarrow
\text{Control}
\not\Rightarrow
\text{Authority}.
}
$$

這不是說每一箭頭永遠沒有 correlation。

只是禁止無條件 logical collapse。

---

# 40. Active Causal Discovery

2025 causal-discovery research 越來越重視 active experiment design：

$$
\text{observe}
\rightarrow
\text{choose intervention}
\rightarrow
\text{observe response}
\rightarrow
\text{update model}.
$$

這種 loop 正是：

$$
P_0\leftrightarrow P_1
$$

動態組合。

---

# 41. Bayesian Active Intervention

ICML 2025 的 work 將 causal direction identification 轉成 sequential hypothesis testing，選 intervention values 以增強 Bayes-factor evidence，並在 embodied AI environment 測試。

DOM 的啟示：

$$
\boxed{
\text{participation can be actively optimized for information gain}.
}
$$

---

# 42. Minimal Intervention Design

AAAI 2025 work 研究最小 intervention set 以確保 causal structure identifiability。

這說明：

> 不一定要「全面介入」才更了解。

有時 minimal targeted intervention 更有效。

---

# 43. Participation Efficiency

本文定義候選：

$$
\boxed{
\eta_P
=
\frac{
\Delta E_A
}{
Cost_P
}.
}
$$

即：

> 每單位 participation cost 帶來多少 epistemic gain。

---

# 44. Intervention Burden

定義：

$$
\boxed{
B_I
}
$$

包含：

- disturbance；
- cost；
- risk；
- ethics；
- irreversibility；
- confounding introduced by intervention。

---

# 45. Deep Participation Can Distort the System

observer 進得越深，可能：

$$
\text{observer effect}\uparrow.
$$

所以：

$$
\boxed{
\text{deeper participation}
\not\Rightarrow
\text{less distortion}.
}
$$

---

# 46. Participation–Perturbation Tradeoff

定義：

$$
\boxed{
\mathcal T_{PP}
=
(\Delta E_A,\Delta W).
}
$$

其中：

- $\Delta E_A$：知識增益；
- $\Delta W$：對 system 的改動。

有些 science 需要：

$$
\Delta W\approx0.
$$

有些因果 identification 需要：

$$
\Delta W>0.
$$

---

# 47. Observation Can Outperform Intervention Under Constraints

如果 intervention：

- unethical；
- impossible；
- too destructive；
- changes the phenomenon；

那麼：

$$
P_0
$$

可能是更好的 epistemic strategy。

---

# 48. Natural Experiments

natural experiment 讓：

$$
W
$$

自身產生可比較 variation，

observer 不直接操控 target。

這說明：

$$
\boxed{
\text{causal evidence}
\not\Rightarrow
\text{direct intervention by investigator}.
}
$$

---

# 49. Simulation Participation

simulation：

$$
\widehat W
$$

可允許：

$$
P_1^{sim}
$$

但：

$$
\boxed{
\text{intervention in model}
\neq
\text{intervention in world}.
}
$$

---

# 50. Model Causal Intimacy ≠ World Causal Intimacy

AI 可以深度操控：

$$
\widehat W
$$

卻對：

$$
W
$$

只有 observational access。

所以 participation 必須帶 world index。

---

# 51. Embodiment

具身化增加：

- local sensing；
- action consequences；
- feedback；
- vulnerability；
- temporal coupling。

因此可能：

$$
P_E\uparrow.
$$

---

# 52. Embodiment ≠ Universal Understanding Gain

body 同時帶來：

- sensor limits；
- local perspective；
- action constraints；
- finite energy；
- damage risk。

所以：

$$
\boxed{
\text{Embodiment}
\not\Rightarrow
\text{Omniscience}.
}
$$

---

# 53. Participation and Scale

同一 observer：

$$
O
$$

在 micro scale：

$$
P_C^{micro}
$$

可能低；

在 macro scale：

$$
P_C^{macro}
$$

可能高。

例如人對 social institution 高度參與，但對 molecular microdynamics 幾乎只間接參與。

---

# 54. Participation Is Scale-Indexed

因此：

$$
\boxed{
P_C(O,W\mid s).
}
$$

不能省略 scale。

---

# 55. Participation and Time

某 observer：

$$
P_0\to P_1\to P_2
$$

隨 technology 進展。

所以：

$$
\boxed{
P_{C,t_0}
\neq
P_{C,t_1}.
}
$$

---

# 56. Participation Event Types

定義：

$$
\mathcal E_P
=
\{
Observe,
Intervene,
Embed,
Constitute,
Integrate,
Detach,
Externalize,
Reclassify
\}.
$$

---

# 57. Detach

$$
P_3\rightarrow P_2
$$

或：

$$
P_2\rightarrow P_0.
$$

例如 sub-agent 被移出 system。

---

# 58. Externalize

原本 internal process：

$$
P_3
$$

被移到外部 monitoring layer。

participation depth 下降，但 global observation 可能上升。

---

# 59. Participation Reversal

因此：

$$
\boxed{
P_C\uparrow
}
$$

不是唯一文明進展方向。

有時把 observer 從 system 中抽離，反而改善 measurement / independence。

---

# 60. Constitutive Blind Spot

本文提出：

$$
\boxed{
CB(O,W)
}
$$

表示：

> 因 observer 本身就是 system 的構成部分，而難以取得 external contrast / global comparison 的盲點。

---

# 61. External Contrast Advantage

external observer 可能更容易比較：

$$
W_1,W_2,\ldots,W_n.
$$

所以：

$$
\boxed{
\text{externality can itself be an epistemic resource}.
}
$$

---

# 62. Internal Phenomenal Access

反方向，如果某 knowledge 只有 first-person access：

$$
E_{\mathrm{first-person}}>0,
$$

external observer 可能永遠只能取得 proxy。

但本文不從此推出：

> first-person report 不可被科學研究。

---

# 63. First-Person / Third-Person Complementarity

候選：

$$
\boxed{
E_{\mathrm{total}}
=
F
\left(
E_{\mathrm{first}},
E_{\mathrm{third}}
\right).
}
$$

某些 domains 可能需要兩者互補。

---

# 64. Participatory Knowledge

本文定義候選：

$$
\boxed{
K_P
}
$$

表示：

> 只有在參與特定 causal loop 時才能取得的 knowledge class。

例如：

- skill；
- sensorimotor contingency；
- interactive affordance；
- endogenous control constraint。

---

# 65. Participatory Knowledge ≠ All Knowledge

即使：

$$
K_P>0,
$$

仍不能：

$$
K_P=K_{\mathrm{total}}.
$$

---

# 66. Skill Knowledge

知道：

> 怎麼騎腳踏車

與知道所有 bicycle dynamics equations 不同。

這提醒：

$$
\boxed{
\text{knowing how}
\neq
\text{knowing all causes}.
}
$$

---

# 67. Causal Experience

本文允許：

$$
\boxed{
E_{\mathrm{causal-exp}}
}
$$

表示：

> observer 直接承受某 causal process 的 first-person / embedded consequence。

但：

$$
E_{\mathrm{causal-exp}}>0
$$

不證明 causal theory 正確。

---

# 68. Experience Is Evidence, Not Automatic Theory

因此：

$$
\boxed{
\text{experience}
\not\Rightarrow
\text{correct interpretation}.
}
$$

---

# 69. Becoming Causality — Strong Reading

強版本：

> O 要理解 W，必須成為 W 的因果本身。

如果寫：

$$
O=W,
$$

語義過強。

---

# 70. Becoming Causality — DOM Rewrite

改寫為五個分離 predicates：

$$
\boxed{
Observe(O,W),
}
$$

$$
\boxed{
Intervene(O,W),
}
$$

$$
\boxed{
Embed(O,W),
}
$$

$$
\boxed{
Constitute(O,W),
}
$$

$$
\boxed{
Same_{\alpha}(O,W).
}
$$

它們一般不等價。

---

# 71. Becoming Part ≠ Becoming Whole

$$
\boxed{
Constitute(O,W)=1
\not\Rightarrow
O=W.
}
$$

---

# 72. Becoming Whole ≠ Knowing Whole

即使某 theory 在 scale $s$ 認定：

$$
Same_{\alpha}(O,W)=1,
$$

仍不能：

$$
K_O(W)=1.
$$

因為 DOM-03 已證明 containment / constitution 不推出 epistemic transparency。

---

# 73. Causal Self-Knowledge Gap

本文定義：

$$
\boxed{
G_{CSK}(O,W)
=
\text{causally constitutive information not accessible to }O.
}
$$

即：

> 你是它的一部分，但你不知道這部分如何完整運作。

---

# 74. Whole-Level Self-Knowledge Is Compressed

Higher-level self 可能只維護：

$$
\Pi(X_{micro})
=
X_{macro}.
$$

所以：

$$
\boxed{
\text{self-knowledge}
}
$$

本身可能是 coarse-grained。

---

# 75. Full Microstate Access Is Not Required for Functional Selfhood

因此：

$$
\boxed{
Subject(O)=1
\not\Rightarrow
K_O(X_{micro})=1.
}
$$

至少在 DOM formal role framework 中不需要這個推出。

---

# 76. Participation and Unknown Profile

沿用 DOM-02：

$$
P_C\uparrow
$$

可以讓：

$$
U_O,U_R
$$

下降，

卻讓：

$$
U_T,U_{\Omega}
$$

仍然保持。

甚至新的 participation 可能暴露新的 Unknown Type。

---

# 77. Participation Can Expand Unknown Frontier

所以：

$$
\boxed{
P_C\uparrow
\land
|\partial K|\uparrow
}
$$

也可能。

例如你進入新 environment 後，第一次發現原來有新的 causal variables。

---

# 78. Participation Discovery Gain

定義候選：

$$
\boxed{
G_{PD}
}
$$

表示：

> 參與所暴露的新 variable / relation / question types。

---

# 79. AI Scientific Agents

2025 AI-for-science work 越來越研究：

- automated hypothesis generation；
- experiment design；
- intervention targeting；
- embodied environment testing；
- persistent scientific memory。

這使 AI 從：

$$
P_0^{data}
$$

逐步進入：

$$
P_1^{experiment}
$$

與：

$$
P_2^{embodied}.
$$

---

# 80. LLM-Guided Intervention Targeting

2025 LeGIT work 探索用 LLM world knowledge 輔助 causal intervention target selection。

DOM 的關鍵不是「LLM 更懂因果」。

而是：

$$
\boxed{
\text{AI can participate in choosing where causal participation should increase}.
}
$$

---

# 81. Meta-Participation

本文提出候選：

$$
\boxed{
P_M
}
$$

表示：

> agent 不只參與 experiment，也選擇 participation mode / intervention target。

---

# 82. Participation Policy

定義：

$$
\boxed{
\Pi_P
:
State
\rightarrow
ParticipationAction.
}
$$

例如：

- observe more；
- intervene；
- embed；
- simulate；
- defer；
- detach。

---

# 83. Participation as Resource Allocation

深度參與有成本。

所以：

$$
\boxed{
\text{more participation}
}
$$

是 research policy decision，不是 automatically better state。

---

# 84. Participation Budget

定義：

$$
\boxed{
B_P
=
(B_{time},B_{compute},B_{risk},B_{energy},B_{ethics},B_{authority}).
}
$$

---

# 85. Ethical Intervention Boundary

即使：

$$
ExpectedInfoGain\gg0,
$$

如果：

$$
Risk\gg0
$$

或：

$$
Authority=0,
$$

仍不應執行 intervention。

所以：

$$
\boxed{
\text{epistemic value}
\not\Rightarrow
\text{permission}.
}
$$

---

# 86. Participation Certificate

本文提出：

```yaml
causal_participation_certificate:
  observer: "O"
  system: "W"
  time: "..."
  scale: "..."
  condition: "..."
  profile:
    observation: "..."
    intervention: "..."
    embeddedness: "..."
    constitutive_role: "..."
    identity_integration: "..."
  channels:
    observational: []
    action: []
    endogenous: []
    first_person: []
  epistemic_access:
    state: "..."
    counterfactual: "..."
    mechanism: "..."
    local: "..."
    global: "..."
  costs:
    perturbation: "..."
    risk: "..."
    irreversibility: "..."
  authority:
    intervention_allowed: "yes|no|conditional"
  unknowns:
    - "..."
```

---

# 87. Participation Is Not a Rank Certificate

即使：

$$
P_4
$$

也不能在 certificate 上寫：

```text
epistemic_rank: supreme
```

因為 participation level 與 evidence quality 不是同一軸。

---

# 88. Causal Intimacy Without Omniscience

本文將這一結構命名為：

$$
\boxed{
\text{Causal Intimacy Without Omniscience}.
}
$$

即：

> 一個存在可以非常深地參與、構成甚至 identity-integrate 某系統，仍保留大量內部未知。

---

# 89. Formal Proposition 1：Participation–Understanding Separation

$$
\boxed{
P_C(O,W)>0
\not\Rightarrow
U_C(O,W)=1.
}
$$

---

# 90. Proposition 2：Constitution–Identity Separation

$$
\boxed{
Constitute(O,W)=1
\not\Rightarrow
O=W.
}
$$

---

# 91. Proposition 3：Constitution–Knowledge Separation

$$
\boxed{
Constitute(O,W)=1
\not\Rightarrow
K_O(W)=1.
}
$$

---

# 92. Proposition 4：Intervention–Truth Separation

$$
\boxed{
Intervene(O,W)=1
\not\Rightarrow
CausalModel_O(W)=\mathrm{True}.
}
$$

---

# 93. Proposition 5：Observation–Weakness Separation

$$
\boxed{
P_0
\not\Rightarrow
\text{inferior evidence}.
}
$$

在適當 task / design 下 observational evidence 可具有高 epistemic value。

---

# 94. Proposition 6：Embeddedness–Globality Separation

$$
\boxed{
Embedded(O,W)=1
\not\Rightarrow
GlobalAccess_O(W)=1.
}
$$

---

# 95. Proposition 7：Control–Authority Separation

$$
\boxed{
Control(O,W)>0
\not\Rightarrow
Authority(O,W)>0.
}
$$

---

# 96. Proposition 8：Identity Integration–Omniscience Separation

$$
\boxed{
P_{ID}\gg0
\not\Rightarrow
K_O(W)=1.
}
$$

---

# 97. 候選猜想一：Participation Can Expand Epistemic Access

$$
\boxed{
P_C\uparrow
\rightsquigarrow
\Delta E_A>0.
}
$$

但依 task / channel / perturbation 而定。

---

# 98. 候選猜想二：Optimal Causal Inquiry Uses Mixed Participation

很多 complex science 可能最適合：

$$
\boxed{
P_0+P_1+P_2
}
$$

混合，而不是單一路徑。

---

# 99. 候選猜想三：Constitutive Blind Spots Increase with Self-Embedding

某些高度 embedded agents：

$$
P_3\uparrow
$$

可能增加：

$$
CB(O,W).
$$

---

# 100. 候選猜想四：Participation Can Reveal Unknown Types

$$
P_C\uparrow
\rightsquigarrow
U_T^{new}>0.
$$

即深度參與可能讓我們發現以前根本不知道的 variable / causal relation。

---

# 101. 候選猜想五：Embodied Agents Learn Causal Affordances Faster in Some Domains

具身 action–feedback loop 可能加速：

$$
E_{\mathrm{affordance}}.
$$

但不是 universal theorem。

---

# 102. 候選猜想六：First/Third-Person Combination Can Dominate Either Alone

對某些 self / embodied systems：

$$
\boxed{
F(E_{\mathrm{first}},E_{\mathrm{third}})
>
E_{\mathrm{first}}
}
$$

且：

$$
F(E_{\mathrm{first}},E_{\mathrm{third}})
>
E_{\mathrm{third}}.
$$

待實驗。

---

# 103. 候選猜想七：Participation Policy Is an AI Scientific Capability

能選：

$$
\Pi_P
$$

可能是 future autonomous science agents 的核心能力之一。

---

# 104. 候選猜想八：Deep Integration Needs Deliberate Ignorance Boundaries

即使：

$$
P_4
$$

很高，

higher self 仍可能需要 selective telemetry / local privacy。

這直接接 DOM-06。

---

# 105. 實驗一：Observation vs Intervention

對同一 causal graph：

- observation-only；
- random intervention；
- optimized intervention。

比較：

- structure recovery；
- cost；
- perturbation；
- false confidence。

---

# 106. 實驗二：Embedded vs External Agent

同一 environment：

A. external log observer；  
B. embodied acting agent。

比較：

- local causal learning；
- global model；
- blind spots；
- adaptation。

---

# 107. 實驗三：Constitutive Blind Spot

讓 agent 成為 system module。

控制：

- local sensor access；
- global dashboard access。

測：

$$
CB(O,W).
$$

---

# 108. 實驗四：Identity-Level Integration

多 Agent system 逐步提高：

- shared memory；
- shared control；
- shared narrative。

測：

- whole-level knowledge；
- local unknowns；
- microstate visibility。

驗證：

$$
P_{ID}\uparrow
\not\Rightarrow
U\rightarrow0.
$$

---

# 109. 實驗五：Minimal Intervention

比較全面 intervention 與 targeted minimal intervention 的：

$$
\eta_P.
$$

---

# 110. 實驗六：Participation Reversal

讓 embedded agent 暫時 externalize，觀察 global comparison 是否改善。

---

# 111. 實驗七：Unknown-Type Discovery

讓 agent 進入具有未標記 causal variables 的 environment，測 participation 是否幫助發現 new question types。

---

# 112. 外部研究邊界

2025 AAAI 的 causal-discovery-by-interventions work 將 intervention target design 形式化為 optimization problem，以最小 intervention sets 提高 causal structure identifiability。DOM-07 將此視為「intervention 可增加特定因果可辨識性」的工程證據，而非 interventionism 的終極形上學證明。

ICML 2025 的 Bayesian active learning for causal discovery 進一步以 sequential interventions 強化 causal direction hypothesis testing，並在 embodied AI environment 中驗證方法可行性。這支持「參與模式可以被主動設計」與「action–feedback loop 可成為 causal learning interface」。

但 2025 年的 *Intervention and experiment* 對「experiment 必然等於 active intervention」提出系統性反駁，並指出 non-interventionist studies 在適當條件下同樣可提供強證據；這是本文拒絕 $P_1$ 無條件高於 $P_0$ 的主要哲學依據。

AI-for-science 研究也愈來愈將 experiment design、causal discovery、formal reasoning 與 persistent scientific memory連成閉環；這支持 DOM-07 將 participation policy 視為 future scientific-agent architecture 的一個可工程化部件。

---

# 113. 與 DOM-08 的接口

DOM-01 建立：

$$
\mathbf M_t.
$$

DOM-02 建立：

$$
\mathbf U.
$$

DOM-03 建立：

$$
\mathfrak C.
$$

DOM-04 建立：

$$
\mathfrak T.
$$

DOM-05 建立：

$$
\mathbf I.
$$

DOM-06 建立：

$$
\mathbf H.
$$

DOM-07 現在建立：

$$
\boxed{
\mathbf P_C.
}
$$

因此最後一篇 DOM-08 終於可以回答：

> 一個過去主要只能被哲學思考的問題，究竟在什麼條件下進入 observation、intervention、realization、participation 與 engineering？

DOM-07 將 participation 補上後，DOM 已經擁有完整 operationalization axes。

---

# 114. 結論

「要理解因果，必須先成為因果本身」是一個非常強、也非常容易被誤讀的命題。

DOM-07 不直接保留這個強版本。

因為：

$$
\boxed{
\text{being part of a causal process}
\neq
\text{being identical to the entire causal domain}.
}
$$

而且：

$$
\boxed{
\text{being identical under one criterion}
\neq
\text{knowing every causal state}.
}
$$

真正可保留的較弱版本是：

$$
\boxed{
\text{deeper causal participation may expose epistemic channels unavailable to purely external observation}.
}
$$

這些 channel 可能包括：

- action consequence；
- endogenous constraint；
- local affordance；
- internal feedback；
- first-person / embedded signal；
- constitutive conflict。

但同時，external observation 也可能具有 internal agent 沒有的：

- global comparison；
- low-perturbation measurement；
- independent replication；
- cross-system perspective。

因此更成熟的因果認識論不是：

$$
\boxed{
\text{inside is always better than outside}.
}
$$

也不是：

$$
\boxed{
\text{outside science is always superior to lived participation}.
}
$$

而是：

$$
\boxed{
\text{different participation relations expose different causal projections}.
}
$$

因此：

$$
P_0,P_1,P_2,P_3,P_4
$$

不是一條「誰更接近真理」的神聖階梯。

它們是一組：

$$
\boxed{
\text{causal access positions}.
}
$$

最重要的護欄仍然是：

$$
\boxed{
\text{Participation}
\not\Rightarrow
\text{Understanding}
\not\Rightarrow
\text{Prediction}
\not\Rightarrow
\text{Control}
\not\Rightarrow
\text{Authority}.
}
$$

而最值得保留的新猜想則是：

$$
\boxed{
P_C\uparrow
\rightsquigarrow
\text{possible expansion of epistemic access}.
}
$$

這也精確回答了「體驗過、參與過、曾經是過，是否能讓理解更深」的問題：

> **可能，而且值得研究；但不應被預設為全知捷徑。**

一個存在可以和因果非常親密。

可以承受它。

可以改變它。

可以構成它。

甚至在某個尺度被視為與它高度同一。

但仍然不知道它的全部。

這就是：

$$
\boxed{
\text{Causal Intimacy Without Omniscience}.
}
$$

**END OF DOM-07 — v0.1**

---

# 內部理論譜系

本篇主要繼承與統合：

1. 《超越觀察者悖論》。
2. 《分域算子本體論：從萬物皆算子到合法作用》。
3. 《多域知識判定論》。
4. 《移動邊界論》。
5. 《無限階 Self–World 遞迴論》。
6. 《多尺度同一性與忒修斯主體》。
7. 《DOM-03｜型別化包含》。
8. 《DOM-04｜型別化超越》。
9. 《DOM-05｜多尺度同一與非同一》。
10. 《DOM-06｜保異質條件合一》。
11. CCAW-03、CCAW-05、CCAW-06、CCAW-07。

---

# 外部參考文獻

1. Elrefaey, A., & Pan, R. (2025). *Causal Discovery by Interventions via Integer Programming*. Proceedings of the AAAI Conference on Artificial Intelligence, 39(16), 16480–16487. DOI: 10.1609/aaai.v39i16.33810.
2. Wang, Y., Liu, M., Sun, X., Wang, W., & Wang, Y. (2025). *Bayesian Active Learning for Bivariate Causal Discovery*. Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, 63734–63754.
3. *Intervention and experiment*. (2025). Philosophy of Science / open-access article, PMCID: PMC11906572.
4. Kummerfeld, E., & Andrews, B. (2024). *Beyond Integrative Experiment Design: Systematic Experimentation Guided by Causal Discovery AI*. Behavioral and Brain Sciences. DOI: 10.1017/S0140525X23002273.
5. Reddy, C. K., & Shojaee, P. (2025). *Towards Scientific Discovery with Generative AI: Progress, Opportunities, and Challenges*. AAAI 2025, 39(27), 28601–28609.
6. Woodward, J. (2003). *Making Things Happen: A Theory of Causal Explanation*. Oxford University Press.
7. Pearl, J. (2000/2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
8. Hacking, I. (1983). *Representing and Intervening*. Cambridge University Press.

---

# 作者聲明

本文提出的 Causal Participation Depth、Participation Profile、Epistemic Access Profile、Causal Intimacy、Constitutive Blind Spot、Participation Efficiency、Participation–Perturbation Tradeoff、Participation Policy、Causal Self-Knowledge Gap 與 Causal Intimacy Without Omniscience 均為理論建模接口。本文不主張 intervention、embodiment、embeddedness、constitution 或 identity-level integration 必然提升因果理解；不主張 current AI 已具有第一人稱 causal experience；也不把 interventionist causation 當作唯一終極因果本體論。本文最重要的限制是：參與深度與認識價值是兩個不同變量，任何「成為因果」的說法都必須拆成 observation、intervention、embeddedness、constitution、identity 與 knowledge 等獨立 relation。

**END OF DOM-07 — v0.1**
