# 從認知到神經元：人腦如何跨層測量智能計算

## From Cognition to Neurons: How Human Intelligence Is Measured Across Levels

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**英文系列：** *Physical Metrology of Intelligence: From Minimal Semantic Execution to Quality and Computational Spacetime*  
**系列編號：** EML-IPM  
**篇次：** Paper 03 / 10  
**文件編號：** EML-IPM-03  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開純理論論文／跨學科方法論  
**工程狀態：** 無 MVP；本文借鑑認知科學與神經科學的跨層量測方法，不將生物單位直接等同 AI 單位

---

## 摘要

若要建立智能的物理計量，最自然的歷史參照不是現有大型模型 benchmark，而是人類對自身大腦的研究。

然而，神經科學並沒有一個被普遍接受的：

$$
\boxed{
1\ \text{thought}
=
N\ \text{spikes}
}
$$

或：

$$
\boxed{
1\ \text{cognitive operation}
=
M\ \text{synaptic events}
}
$$

換算表。

相反地，認知科學與神經科學長期採用的是一套 **跨層代理量測（cross-level proxy measurement）**：

$$
\boxed{
\text{Behavior}
\rightarrow
\text{Latent Cognitive Process}
\rightarrow
\text{Neural Code}
\rightarrow
\text{Cellular Events}
\rightarrow
\text{Physical Implementation}.
}
$$

這條鏈中的每一層都使用不同單位：

- 行為層：accuracy、reaction time、choice、error、information throughput；
- 認知模型層：belief update、evidence accumulation、elementary cognitive operation、value of computation；
- 神經編碼層：spike count、spike timing、population pattern、mutual information、decoding accuracy；
- 細胞層：action potential、synaptic event、membrane integration、plasticity event；
- 物理實現層：ion flux、ATP、energy、heat、entropy production。

因此：

$$
\boxed{
\text{Cognitive Unit}
\neq
\text{Neural Event}
\neq
\text{Information Bit}
\neq
\text{Physical Operation}.
}
$$

本文主張，人腦研究真正值得 IPM 借用的不是某個固定「腦內 FLOP」，而是五個方法論原則：

1. **Level Separation**：不同描述層不可互相偷換；
2. **Latent Inference**：內部認知過程可由行為 proxy 與模型反推；
3. **Population over Atomism**：高階資訊通常由神經群體模式承載，而非單一神經元；
4. **Encoding–Decoding Duality**：需同時問「神經活動帶有什麼資訊」與「這些資訊能否支援行為」；
5. **Causal Perturbation**：相關性不足，必須透過干預、消融、刺激或其他擾動驗證功能貢獻。

本文首先借鑑 Marr 的三層分析：

$$
\boxed{
\text{Computational}
\rightarrow
\text{Algorithmic}
\rightarrow
\text{Implementational}.
}
$$

但 IPM 不直接照搬。Marr 的 implementational layer 對今天的智能物理計量過粗，因此本文擴張為：

$$
\boxed{
L_4:\text{Task Achievement}
}
$$

$$
\boxed{
L_3:\text{Semantic / Cognitive Operation}
}
$$

$$
\boxed{
L_2:\text{Algorithmic / Representational Realization}
}
$$

$$
\boxed{
L_1:\text{Neural / Computational Physical Events}
}
$$

$$
\boxed{
L_0:\text{Thermodynamic Realization}.
}
$$

第二，本文借鑑 resource-rational analysis。該傳統不只問「人是否理性」，而會定義 elementary mental operations，為操作分配時間與資源成本，再研究有限計算條件下哪些策略值得執行。這與 IPM 的：

$$
\mu_I
\rightarrow
Cost(\mu_I)
\rightarrow
Value(\mu_I)
$$

結構高度相容。

第三，本文借鑑 psychophysics 與 diffusion decision model。心理學常不把 reaction time 直接視為「認知量」，而是從 accuracy、mean RT、RT distribution 等可觀察資料推斷 latent evidence accumulation、decision boundary、bias 與 non-decision time。這告訴 IPM：

$$
\boxed{
\text{Internal Intelligent Operation}
}
$$

不必完全可直接觀測，

仍可以透過：

$$
\boxed{
\text{observable trace}
+
\text{constrained latent model}
}
$$

進行計量。

第四，本文處理 neural coding。神經科學會使用：

$$
\boxed{
\text{bits/spike}
}
$$

$$
\boxed{
\text{mutual information}
}
$$

$$
\boxed{
\text{population decoding accuracy}
}
$$

來描述神經活動與 stimulus／behavior 之間的資訊關係。但這些量只是 neural code 的特性，不是「智能本身」。

尤其：

$$
\boxed{
\text{bits/spike}
\neq
\text{cognitive bits}.
}
$$

第五，本文強調 population coding。單一 neuron 的活動常無法唯一決定其高階功能；資訊可能分散於神經群體的 joint activity 中。因此：

$$
\boxed{
\text{One Neuron}
\neq
\text{One Semantic Unit}.
}
$$

這直接支持 Paper 02 對 $\mu_I$ 的 realization-independence 原則。

第六，本文提出 **跨層證據三角化（Cross-Level Triangulation）**：

$$
\boxed{
\mathcal X_L
=
(
E_B,
E_C,
E_N,
E_P
)
}
$$

其中：

- $E_B$：Behavioral Evidence；
- $E_C$：Cognitive-Model Evidence；
- $E_N$：Neural Evidence；
- $E_P$：Perturbational / Causal Evidence。

只有當多層證據收斂時，我們才逐步提高：

$$
Confidence(
\mu_I^{obs}
\approx
\mu_I^{int}
).
$$

本文最後提出對 AI 的直接借鑑：

$$
\boxed{
\text{Output Behavior}
\rightarrow
\text{Semantic-State Model}
\rightarrow
\text{Internal Computational Trace}
\rightarrow
\text{Physical Trace}.
}
$$

也就是，不要求現在立刻看穿 Transformer 的每一個 latent state；而是像神經科學一樣，逐步利用：

- behavioral task decomposition；
- structured trace；
- activation intervention；
- ablation；
- mechanistic probe；
- hardware telemetry；

把語意層與物理層對齊。

本文終端命題為：

$$
\boxed{
\textbf{
人腦研究真正教給智能物理計量學的，
不是「一個 spike 等於多少智能」，
而是：當高階認知無法被直接觀察時，
可以透過多層代理、模型反推、群體編碼與因果擾動，
逐步建立認知與物理事件之間的可檢驗映射。
}
}
$$

---

# 1. 第一個結論：沒有公認的「最小人類認知單位」

認知科學有：

- stimulus；
- response；
- choice；
- cognitive operation；
- memory item；
- belief；
- decision variable。

神經科學有：

- spike；
- burst；
- synaptic event；
- population pattern；
- oscillation；
- membrane potential。

資訊論有：

$$
bit.
$$

物理學有：

$$
Joule.
$$

但目前沒有可靠理由寫：

$$
\boxed{
1\ \text{cognitive operation}
=
k\ \text{spikes}
}
$$

作為普適常數。

---

# 2. 這不是研究失敗，而是跨層問題的本質

同一個 cognitive function 可以由：

- 不同腦區；
- 不同神經群體；
- 不同時間尺度；

共同實現。

而同一 neuron 也可能依語境參與不同功能。

所以：

$$
\boxed{
\text{Functional Unit}
\neq
\text{Anatomical Unit}.
}
$$

---

# 3. Marr：先分層再連接

Marr 的經典區分：

$$
\boxed{
\text{Computational}
\rightarrow
\text{Algorithmic}
\rightarrow
\text{Implementational}.
}
$$

可以粗略理解為：

- computational：系統解什麼問題？
- algorithmic：用什麼表示與程序解？
- implementational：由什麼物理基質實現？

---

# 4. 這個分層對 IPM 很重要

因為它阻止：

$$
\boxed{
\text{task performance}
}
$$

被直接等同：

$$
\boxed{
\text{physical event count}.
}
$$

也阻止：

$$
\boxed{
\text{physical similarity}
}
$$

被直接等同：

$$
\boxed{
\text{functional equivalence}.
}
$$

---

# 5. 但 Marr 三層對今天不夠細

對智能物理計量而言，implementational layer 太大。

裡面至少還有：

- neuron/network；
- ion channels；
- metabolism；
- heat；
- physical substrate。

因此 IPM 擴張成五層。

---

# 6. IPM 五層

$$
\boxed{
L_4=\text{Task Achievement}
}
$$

測：

- correctness；
- quality；
- decision success；
- behavioral utility。

---

# 7. $L_3$：Semantic / Cognitive Operation

$$
\boxed{
L_3=\mu_I\text{ layer}.
}
$$

測：

- belief update；
- relation construction；
- constraint resolution；
- strategy change；
- uncertainty restructuring。

---

# 8. $L_2$：Algorithmic / Representational Realization

處理：

- evidence accumulation；
- sampling；
- search；
- recurrent update；
- representation transformation。

---

# 9. $L_1$：Neural / Computational Physical Events

在人腦：

- spike；
- synaptic event；
- membrane dynamics；
- population pattern。

在 AI：

- tensor operation；
- memory access；
- routing；
- interconnect event。

---

# 10. $L_0$：Thermodynamic Realization

$$
\boxed{
L_0=
(
Energy,
Heat,
EntropyProduction
).
}
$$

Paper 04 才正式處理這一層。

---

# 11. 第一條借鑑：不要越級等同

所以：

$$
\boxed{
L_4\neq L_3\neq L_2\neq L_1\neq L_0.
}
$$

可以映射，但不應直接等同。

---

# 12. 行為層：人腦研究最容易看到什麼？

最容易觀測的通常不是 neural thought。

而是：

- 正確／錯誤；
- 反應時間；
- 選擇；
- 眼動；
- 動作；
- verbal report。

---

# 13. Reaction Time 不是認知操作本身

若：

$$
RT=500ms,
$$

不能說：

> 這個人做了 500 單位認知。

所以：

$$
\boxed{
ReactionTime
\neq
CognitiveWork.
}
$$

---

# 14. 但 RT 是有價值 proxy

因為在 controlled task 中：

$$
RT
$$

會隨：

- stimulus difficulty；
- decision threshold；
- attention；
- evidence quality；

系統性改變。

---

# 15. Accuracy 也不是全部

兩個人都：

$$
Accuracy=95\%.
$$

但：

$$
RT_A\ll RT_B.
$$

可能代表完全不同處理策略。

---

# 16. 所以心理學通常做多變量行為量測

$$
\boxed{
E_B=
(
Accuracy,
RT,
RTDistribution,
ErrorPattern,
Choice
).
}
$$

---

# 17. Diffusion Decision Model 是漂亮例子

在 two-choice task 中，observable behavior 可被模型拆成 latent components。

---

# 18. 典型 latent variables

例如：

$$
v=\text{drift rate}
$$

代表 evidence quality / accumulation rate。

---

# 19. Decision boundary

$$
a=\text{decision threshold}.
$$

反映 speed–accuracy trade-off。

---

# 20. Starting point

$$
z_0=\text{initial bias}.
$$

---

# 21. Non-decision time

$$
T_{er}
$$

包含 perception / motor 等非 decision accumulation 部分。

---

# 22. 關鍵不是 diffusion model 一定是真實神經機制

而是方法論：

$$
\boxed{
\text{observable behavior}
\rightarrow
\text{constrained latent cognitive model}.
}
$$

---

# 23. 這就是 IPM 可以借的東西

我們現在看不到：

$$
\mu_I^{int}
$$

不代表完全不能量。

可以先建立：

$$
\mu_I^{obs}.
$$

---

# 24. 第二條借鑑：Latent 不等於不可科學化

只要模型：

- 有明確 observable prediction；
- 有 competing model；
- 可被 falsify；
- 可接受 intervention；

就可以逐步提高可信度。

---

# 25. Resource Rationality：計算本身有成本

認知科學另一個直接相關方向是：

$$
\boxed{
\text{Resource-Rational Analysis}.
}
$$

---

# 26. 它問的不是「完美理性者會怎麼做」

而是：

> 在有限時間、有限記憶、有限計算下，什麼策略值得做？

---

# 27. 基本形式

定義一組：

$$
c_1,c_2,\ldots,c_n
$$

elementary mental operations。

---

# 28. 每個操作有成本

$$
Cost(c_i).
$$

可以來自：

- time；
- memory；
- opportunity cost；
- computation。

---

# 29. 執行操作有價值

因為：

$$
c_i
$$

可能改變 belief，

進而改善 decision。

---

# 30. 因此可寫成

$$
\boxed{
ValueOfComputation
=
ExpectedImprovement
-
Cost.
}
$$

---

# 31. 這與 IPM 幾乎同構

Paper 02：

$$
\mu_I
$$

就是我們的 elementary semantic operation candidate。

---

# 32. 但 IPM 再往下

Resource-rational cost 常是抽象 cost。

我們要進一步：

$$
\boxed{
Cost(\mu_I)
\rightarrow
PhysicalTrace
\rightarrow
Joule.
}
$$

---

# 33. 第三條借鑑：操作成本必須和成果效用一起看

不能只問：

> 花了多少計算？

還要問：

> 那次計算到底改善了多少結果？

所以：

$$
\boxed{
ComputationCount
\neq
IntelligenceValue.
}
$$

---

# 34. 從認知模型進入神經編碼

下一個問題：

> 認知操作到底由什麼 neural activity 承載？

神經科學不會直接回答：

> 這一顆 neuron 就是 belief update。

---

# 35. Neural Coding 的核心問題

更常問：

> 哪些 neural responses 與 stimulus / task variable / behavior 相關？

---

# 36. Encoding

$$
\boxed{
Stimulus
\rightarrow
NeuralResponse.
}
$$

研究：

> 給定世界狀態，神經系統如何反應？

---

# 37. Decoding

$$
\boxed{
NeuralResponse
\rightarrow
Estimate(Stimulus/Behavior).
}
$$

研究：

> 從神經活動能否重建外部變量？

---

# 38. Encoding 和 decoding 都重要

只有 encoding：

可能知道 neuron 對 stimulus 敏感，

但不知道 brain downstream 是否真的能利用。

---

# 39. 只有 decoding：

可能 decoder 很強，

但抓到的是相關資訊，不一定是腦真正使用的 code。

---

# 40. 所以：

$$
\boxed{
Decodable
\neq
UsedByBrain.
}
$$

這也是 AI mechanistic probe 必須注意的陷阱。

---

# 41. Information Theory 的角色

神經科學常用 mutual information：

$$
\boxed{
I(S;R)
=
H(S)-H(S\mid R).
}
$$

其中：

- $S$：stimulus / task variable；
- $R$：neural response。

---

# 42. 它問

神經反應 $R$ 對 $S$ 帶來多少 uncertainty reduction。

---

# 43. bits/spike

可以定義某些情況下：

$$
\boxed{
\frac{
I(S;R)
}{
N_{spike}
}.
}
$$

---

# 44. 但這不是「一個 spike = 幾 bits 的思想」

因為它依賴：

- stimulus ensemble；
- time bin；
- response definition；
- neuronal population；
- encoding assumptions。

---

# 45. 所以：

$$
\boxed{
bits/spike
\neq
cognitive\ bits.
}
$$

---

# 46. 一個 spike 也不是固定資訊量

不同 neuron、task、context：

$$
I_{spike}^{A}
\neq
I_{spike}^{B}.
$$

---

# 47. 這跟 $\mu_I$ 的物理成本一樣

同類語意事件：

$$
\mu_I
$$

在不同架構下也不會有固定 physical cost。

---

# 48. Population Coding

現代 neuroscience 很早就發現：

$$
\boxed{
\text{information is often population-distributed}.
}
$$

---

# 49. 所以：

$$
\boxed{
OneNeuron
\neq
OneVariable.
}
$$

---

# 50. 某個 stimulus value 可以由整個 population pattern 表示

$$
\mathbf r=
(r_1,r_2,\ldots,r_n).
$$

---

# 51. 這對 Paper 02 很重要

因為它支持：

$$
\boxed{
SemanticUnit
\neq
SpecificNeuron.
}
$$

---

# 52. realization 可以是 distributed

$$
\rho_N(\mu_I)
=
\{\text{population pattern over time}\}.
$$

---

# 53. 神經編碼還有時間尺度問題

資訊可能存在於：

- firing rate；
- spike count；
- precise spike timing；
- burst；
- population synchronization。

---

# 54. 所以 measurement resolution 會改變 code

若 time bin：

$$
\Delta t
$$

不同，

得到的：

$$
I(S;R)
$$

也可能不同。

---

# 55. 這與 Paper 02 的解析度相對性一致

$$
\boxed{
Minimality
=
Minimality(\delta,Task,Observer).
}
$$

神經科學也沒有一個永恆固定的唯一觀察尺度。

---

# 56. Single-Neuron 到 Population-Neuron 的轉變

早期研究常看：

$$
r_i(t)
$$

單一 neuron。

---

# 57. 大規模 recording 後

越來越常分析：

$$
\boxed{
\mathbf R(t)
=
(r_1(t),\ldots,r_n(t)).
}
$$

---

# 58. 這能捕捉 single-cell level 不明顯的 information

也能做 single-trial decoding。

---

# 59. 第四條借鑑：不要把可計量的最小硬體單位誤認成功能最小單位

神經元容易數。

spike 容易數。

但：

$$
\boxed{
EasyToCount
\neq
CorrectUnit.
}
$$

---

# 60. 這句對 AI 更重要

token 容易數。

FLOP 容易估。

但仍然不代表它們就是智能單位。

---

# 61. Behavioral Throughput：10 bits/s 的啟示

有研究以多種人類行為任務估計，人類可觀察行為資訊 throughput 約在：

$$
\boxed{
10\ bits/s
}
$$

量級。

---

# 62. 而 sensory input 的估計可高很多

約：

$$
10^9\ bits/s
$$

量級。

---

# 63. 這個差距很刺激

但不能解讀成：

> 大腦只做 10 bits/s 的總計算。

---

# 64. 更合理：

$$
\boxed{
\text{Behavioral Output Rate}
\neq
\text{Internal Neural Computation Rate}.
}
$$

---

# 65. 這正好對應 AI

一個模型最後只輸出：

$$
1000\ tokens
$$

不代表內部只做了 1000 個智能事件。

---

# 66. Output bottleneck 可以遠小於 internal dynamics

因此：

$$
\boxed{
OutputRate
\neq
ComputationRate.
}
$$

---

# 67. 10 bits/s 更適合當什麼？

它是一個：

$$
\boxed{
\text{behavioral effective throughput proxy}.
}
$$

不是 brain FLOPS。

---

# 68. 第五條借鑑：區分 throughput 與 work

throughput 問：

> 單位時間有多少可觀察資訊通過？

work 問：

> 系統內部做了多少有效狀態轉換？

兩者不是一樣。

---

# 69. Correlation 不等於 Causal Function

假設某 brain region 在做數學時亮起來。

不能立刻說：

> 這裡就是數學模組。

---

# 70. 因為 activity 可以是：

- upstream；
- downstream；
- correlated；
- compensatory；
- epiphenomenal。

---

# 71. 所以神經科學使用 perturbation

例如：

- lesion；
- TMS；
- electrical stimulation；
- optogenetics；
- pharmacological perturbation。

---

# 72. 基本思想

$$
\boxed{
do(N_i=\tilde N_i)
\rightarrow
\Delta Behavior?
}
$$

---

# 73. 若干預神經活動後功能系統性改變

則 causal evidence 增強。

---

# 74. 但 perturbation 也不是完美

TMS 等技術可能：

- 作用範圍廣；
- 有 side effect；
- state-dependent；
- network compensation。

所以：

$$
\boxed{
Perturbation
\neq
PerfectLocalization.
}
$$

---

# 75. 這個謹慎態度對 AI 很重要

activation ablation 之後輸出變差，

也不表示：

> 那個 activation 就是完整概念本體。

---

# 76. 我們只能說

$$
\boxed{
\text{it has causal relevance under this intervention}.
}
$$

---

# 77. Causal Chain

因此一個認知神經推斷至少要考慮：

$$
\boxed{
Intervention
\rightarrow
NeuralChange
\rightarrow
CognitiveChange
\rightarrow
BehaviorChange.
}
$$

---

# 78. 中間每一步都有 confound

所以不能跳階。

---

# 79. 第六條借鑑：Cross-Level Triangulation

本文提出：

$$
\boxed{
\mathcal X_L
=
(
E_B,
E_C,
E_N,
E_P
).
}
$$

---

# 80. $E_B$：Behavioral Evidence

例如：

- accuracy；
- RT；
- choice；
- error profile。

---

# 81. $E_C$：Cognitive-Model Evidence

例如：

- drift model；
- memory model；
- resource-rational model；
- task decomposition。

---

# 82. $E_N$：Neural Evidence

例如：

- spike train；
- population representation；
- EEG/MEG/fMRI；
- neural decoding。

---

# 83. $E_P$：Perturbational Evidence

例如：

- lesion；
- stimulation；
- causal manipulation。

---

# 84. 證據越收斂

越可以提高：

$$
\boxed{
Confidence(
CognitiveFunction
\leftrightarrow
NeuralMechanism
).
}
$$

---

# 85. 這比只看 correlation 更可靠

也比只看 abstract cognitive model 更可靠。

---

# 86. Cross-Level Consistency

若：

$$
Model_C
$$

預測某 condition 會增加 evidence accumulation time，

行為 RT 真的改變，

神經 population dynamics 也以一致方向改變，

干預該 dynamics 又破壞 behavior，

那就是強跨層證據。

---

# 87. 這種結構對 $\mu_I$ 非常重要

未來我們要建立：

$$
\boxed{
\mu_I^{obs}
}
$$

不能只靠 verbal interpretation。

---

# 88. 應至少使用

$$
\boxed{
\mu_I^{obs}
=
F(
Behavior,
StructuredTrace,
InternalProbe,
Intervention
).
}
$$

---

# 89. 人腦研究也告訴我們：代理量不是恥辱

只要誠實標記：

$$
\boxed{
Proxy
\neq
Ontology.
}
$$

---

# 90. reaction time 是 proxy

但不是 thought。

---

# 91. spike count 是 proxy

但不是 cognition。

---

# 92. mutual information 是 relation measure

但不是 meaning 本身。

---

# 93. decoding accuracy 是 accessibility measure

但不保證 causal use。

---

# 94. 這種 type discipline 是我們最需要借的

AI benchmark 最大問題之一恰恰是：

$$
\boxed{
Proxy
\rightarrow
Ontology
}
$$

偷換得太快。

---

# 95. 人腦跨層量測的第一種失敗：Reverse Inference

看到 region A active，

就說：

> subject 正在做 function X。

---

# 96. 這通常不夠

因為 region A 可能參與很多功能。

---

# 97. AI 也有同樣錯誤

看到 head H 對某詞敏感，

不能直接說：

> H 就是語法 head。

---

# 98. 所以：

$$
\boxed{
Selectivity
\neq
Exclusivity.
}
$$

---

# 99. 第二種失敗：One-to-One Localization

高階 cognition 常不是一個位置。

---

# 100. 而是：

$$
\boxed{
\text{distributed dynamics}.
}
$$

---

# 101. 所以 IPM 不應追求：

> 找到「推理 neuron」。

---

# 102. 而應追求：

$$
\boxed{
\text{semantic transition}
\leftrightarrow
\text{distributed realization trace}.
}
$$

---

# 103. 第三種失敗：把 information 當 meaning

若：

$$
I(S;R)=2\ bits,
$$

只表示 $R$ 對 $S$ 含有資訊。

---

# 104. 不表示：

> 這兩 bits 就是 2 units of understanding。

所以：

$$
\boxed{
Information
\neq
Understanding.
}
$$

---

# 105. 第四種失敗：忽略觀測尺度

神經 code 在：

$$
1ms
$$

與：

$$
100ms
$$

時間窗可能完全不同。

---

# 106. AI 也是一樣

你可以按：

- token；
- layer；
- block；
- trajectory；
- task；

切分。

得到完全不同 operation count。

---

# 107. 因此解析度必須明示

$$
\boxed{
Measurement
=
Measurement(\delta).
}
$$

---

# 108. 第五種失敗：把平均表現當單次認知

很多 neuroscience 結果來自：

$$
trial-average.
$$

---

# 109. 但人腦每次決策其實是 single trial

所以 population decoding 後來越來越重視：

$$
\boxed{
\text{single-trial activity}.
}
$$

---

# 110. 這與 IPM 的 Single-Pass 問題高度相似

平均 100 次 rollout 很強，

不能代表：

$$
Pass@1
$$

很強。

---

# 111. 第七條借鑑：單次事件與平均性能必須分開

$$
\boxed{
EnsemblePerformance
\neq
SingleEpisodePerformance.
}
$$

---

# 112. 人腦研究與 AI 的對照表

| 人腦研究層 | 常用量 | IPM 對應 | 不可偷換 |
|---|---|---|---|
| Behavior | Accuracy / RT | $Q,T$ | RT ≠ intelligence work |
| Cognitive model | latent operation | $\mu_I^{obs}$ | model ≠ internal truth |
| Neural coding | spike / population code | internal trace | spike ≠ semantic unit |
| Information theory | bits/spike, MI | semantic information proxy | bit ≠ meaning |
| Perturbation | TMS / lesion | ablation / activation intervention | perturbation ≠ perfect localization |
| Physical layer | ion / metabolism | hardware telemetry | physical event ≠ cognition |

---

# 113. 所以 IPM 應該如何借？

不是做「人工腦類比」。

---

# 114. 第一個可借原則：Level Separation

$$
\boxed{
Task
\neq
SemanticOperation
\neq
Algorithm
\neq
PhysicalEvent.
}
$$

---

# 115. 第二個：Latent Inference

$$
\boxed{
Observable
+
Model
\rightarrow
LatentEstimate.
}
$$

---

# 116. 第三個：Population Realization

$$
\boxed{
SemanticFunction
\leftrightarrow
DistributedPattern
}
$$

通常比 one-node mapping 合理。

---

# 117. 第四個：Encoding–Decoding Duality

不只問：

> 內部有哪些資訊？

還要問：

> 這些資訊是否能被 downstream 利用？

---

# 118. 第五個：Causal Perturbation

$$
\boxed{
Correlation
\rightarrow
Intervention
\rightarrow
CausalConfidence.
}
$$

---

# 119. 第六個：Multi-Scale Measurement

不同：

$$
\delta
$$

下都要重新聲明單位。

---

# 120. 第七個：Single-Trial Discipline

不要只報平均。

---

# 121. 對 AI 的五層量測架構

現在可建立：

$$
\boxed{
A_4=\text{Task Output}
}
$$

---

# 122. $A_3$：Semantic Reconstruction

$$
\boxed{
A_3=\mu_I^{obs}
}
$$

由：

- proof step；
- structured reasoning；
- behavior change；

重建。

---

# 123. $A_2$：Internal Computational Mechanism

例如：

- activation trajectory；
- routing；
- memory retrieval；
- attention pattern。

---

# 124. $A_1$：Hardware Execution

$$
\boxed{
(
Ops,
Memory,
Interconnect,
DeviceTime
).
}
$$

---

# 125. $A_0$：Thermodynamic Trace

$$
\boxed{
(
Energy,
Heat,
Entropy
).
}
$$

---

# 126. AI Cross-Level Triangulation

可以定義：

$$
\boxed{
\mathcal X_{AI}
=
(
E_O,
E_S,
E_I,
E_A,
E_H
)
}
$$

---

# 127. $E_O$：Output Evidence

結果品質。

---

# 128. $E_S$：Semantic Evidence

可重建求解狀態改變。

---

# 129. $E_I$：Internal Trace Evidence

latent / activation / routing。

---

# 130. $E_A$：Ablation / Intervention Evidence

移除或修改內部結構後的影響。

---

# 131. $E_H$：Hardware Evidence

真實設備 telemetry。

---

# 132. 對某個 $\mu_I$ 的可信度

概念上：

$$
\boxed{
Conf(\mu_I)
=
F(
E_O,E_S,E_I,E_A,E_H
).
}
$$

---

# 133. 這比只從 Chain-of-Thought 數步驟好很多

因為 visible reasoning：

$$
\boxed{
\text{may not equal internal reasoning}.
}
$$

---

# 134. 同樣比只看 activation 好

因為：

$$
Activation
$$

沒有 task semantics。

---

# 135. 最終要兩邊收斂

$$
\boxed{
SemanticEvidence
\leftrightarrow
PhysicalEvidence.
}
$$

---

# 136. 這就是 Physical Metrology 真正的跨層橋

不是找一個神奇單位。

而是建立：

$$
\boxed{
\text{equivalence constraints}
}
$$

讓兩層越來越對得上。

---

# 137. Measurement Confidence 應該是連續的

我們不應只有：

> 找到了／沒找到 $\mu_I$。

---

# 138. 而是：

$$
\boxed{
Conf(\mu_I)\in[0,1]
}
$$

或至少分級。

---

# 139. IPM Measurement Grade

本文提出：

### Grade D — Behavioral

只有輸入輸出 proxy。

---

# 140. Grade C — Structured Semantic

已有可靠 task decomposition / semantic trace。

---

# 141. Grade B — Internal Correlation

已有 internal representation 對應。

---

# 142. Grade A — Causal Internal

已有 intervention / ablation 支持。

---

# 143. Grade A+ — Physical-Semantic Alignment

語意單位、內部機制與硬體 telemetry 可對齊。

---

# 144. 這種分級比假裝每次都知道模型內部發生什麼誠實

---

# 145. 對 Paper 02 的第一次修正

Paper 02 寫：

$$
\mu_I^{obs}
\approx
\mu_I^{int}.
$$

現在應補上：

$$
\boxed{
ApproximationStrength
=
F(
CrossLevelEvidence
).
}
$$

---

# 146. 即：

$$
\boxed{
Conf(
\mu_I^{obs}
\approx
\mu_I^{int}
)
\uparrow
}
$$

當：

- behavioral；
- semantic；
- internal；
- causal；
- physical；

證據收斂。

---

# 147. 這是我們從 neuroscience 真正借到的東西

不是神經元數字。

而是：

$$
\boxed{
\text{triangulated epistemology}.
}
$$

---

# 148. 一個重要限制：生物腦不是數位電腦的慢版

不能因為：

$$
Neuron
\sim
Unit
$$

就把：

$$
Neuron
\leftrightarrow
ArtificialNeuron
$$

當等號。

---

# 149. 生物 neuron 有：

- dendritic computation；
- stochasticity；
- nonlinear membrane dynamics；
- neuromodulation；
- plasticity。

---

# 150. 人工 neuron 通常只是抽象 mathematical operation

所以：

$$
\boxed{
BiologicalNeuron
\neq
ANNNeuron.
}
$$

---

# 151. 同樣 spike 也不是 token

$$
\boxed{
Spike
\neq
Token.
}
$$

---

# 152. 因此 Paper 03 的任務是借方法，不借本體

這一點必須固定。

---

# 153. 八個借用原則

本文總結成：

$$
\boxed{
\mathcal B_N=
(
B_L,B_P,B_M,B_D,B_C,B_S,B_T,B_G
)
}
$$

---

# 154. $B_L$ — Level Separation

跨層不可偷換。

---

# 155. $B_P$ — Proxy Discipline

代理量必須標記為 proxy。

---

# 156. $B_M$ — Model-Mediated Inference

latent cognition 可透過模型估計。

---

# 157. $B_D$ — Distributed Realization

高階功能可由分散群體實現。

---

# 158. $B_C$ — Causal Perturbation

相關必須盡量補上因果證據。

---

# 159. $B_S$ — Scale Declaration

任何 operation count 都要聲明解析度。

---

# 160. $B_T$ — Trial Separation

single episode 與 ensemble statistics 分離。

---

# 161. $B_G$ — Grounding Downward

最終必須能往物理層追。

---

# 162. 十二個 Canonical Invariants

**Invariant 1**

$$
\boxed{
CognitiveUnit
\neq
NeuralEvent.
}
$$

**Invariant 2**

$$
\boxed{
NeuralEvent
\neq
InformationBit.
}
$$

**Invariant 3**

$$
\boxed{
FunctionalUnit
\neq
AnatomicalUnit.
}
$$

**Invariant 4**

$$
\boxed{
ReactionTime
\neq
CognitiveWork.
}
$$

**Invariant 5**

$$
\boxed{
bits/spike
\neq
cognitive\ bits.
}
$$

**Invariant 6**

$$
\boxed{
OneNeuron
\neq
OneSemanticUnit.
}
$$

**Invariant 7**

$$
\boxed{
Decodable
\neq
CausallyUsed.
}
$$

**Invariant 8**

$$
\boxed{
Correlation
\neq
CausalFunction.
}
$$

**Invariant 9**

$$
\boxed{
Proxy
\neq
Ontology.
}
$$

**Invariant 10**

$$
\boxed{
OutputRate
\neq
InternalComputationRate.
}
$$

**Invariant 11**

$$
\boxed{
EnsemblePerformance
\neq
SingleEpisodePerformance.
}
$$

**Invariant 12**

$$
\boxed{
BiologicalNeuron
\neq
ANNNeuron.
}
$$

---

# 163. 對 IPM 統一事件向量的擴張

Paper 02：

$$
\mathfrak E'=
(
Q,
\mathbf N_{\mu},
U,G,I,L,R,S,T,E,V_{CST}
).
$$

---

# 164. 現在加入 measurement confidence

$$
\boxed{
\mathfrak E''=
(
Q,
\mathbf N_{\mu},
Conf_{\mu},
Grade_{\mu},
U,G,I,L,R,S,T,E,V_{CST}
).
}
$$

---

# 165. 因為同一個 $N_\mu$

若只是 Grade D behavioral reconstruction，

與 Grade A+ physical-semantic alignment，

可信度不是同一級。

---

# 166. 這避免虛假精確

例如：

> 模型執行了 12,431 次 $\mu_I$。

如果只有 behavior proxy，

這種精確度就是假的。

---

# 167. 更誠實應該說

$$
\widehat N_{\mu}
\pm
\text{uncertainty}
$$

並附：

$$
Grade_{\mu}.
$$

---

# 168. 結論：神經科學沒有給我們智能原子，但給了更重要的東西

如果我們原本希望從人腦研究找到：

> 一個神經 spike 到底等於多少智能？

答案令人失望：

$$
\boxed{
\text{沒有這個普適換算。}
}
$$

但這其實是更好的結果。

因為神經科學已經告訴我們，真正的智能計量不應建立在一對一神話上。

人類研究自己的方式更接近：

$$
\boxed{
\text{Behavior}
\rightarrow
\text{Latent Model}
\rightarrow
\text{Neural Population}
\rightarrow
\text{Causal Perturbation}
\rightarrow
\text{Physical Mechanism}.
}
$$

每一層都允許不同單位。

每一層都可以提供證據。

而真正強的理論，是讓這些證據彼此約束。

所以：

$$
\boxed{
\textbf{
跨層映射不是一次完成的等號，
而是一個逐步增加可信度的證據網路。
}
}
$$

這直接修正了我們對 $\mu_I$ 的態度。

 $\mu_I$ 不需要一開始就被直接「看見」。

我們可以先得到：

$$
\mu_I^{obs},
$$

再透過：

- behavior；
- structured reasoning；
- internal probes；
- intervention；
- hardware telemetry；

逐步提高：

$$
Conf(
\mu_I^{obs}
\approx
\mu_I^{int}
).
$$

因此，IPM 不需要等到 mechanistic interpretability 完全成熟才開始。

它可以像認知神經科學一樣：

$$
\boxed{
\text{measure partially}
\rightarrow
\text{model explicitly}
\rightarrow
\text{intervene causally}
\rightarrow
\text{ground physically}.
}
$$

這才是本文真正從人腦研究借來的方法。

而下一步，自然就是繼續往下。

我們現在已經知道：

- cognition 不能直接等於 spike；
- spike 可以承載 information；
- population coding 比單神經元更重要；
- causal perturbation 可以提高功能定位可信度。

但還沒有回答：

> 這些神經事件最後到底花多少能量？

也就是：

$$
\boxed{
\textbf{
怎麼從 spike、synapse、membrane dynamics，
一路算到 ATP、Joule、heat 與 thermodynamic bound？
}
}
$$

這就是 Paper 04。

---

## 文獻基礎

[1] Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*.  
[2] Griffiths, T. L., Lieder, F., & Goodman, N. D. (2015). Rational use of cognitive resources: Levels of analysis between the computational and the algorithmic. *Topics in Cognitive Science*, 7(2), 217–229. DOI: 10.1111/tops.12142.  
[3] Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences*, 43, e1. DOI: 10.1017/S0140525X1900061X.  
[4] Ratcliff, R., & McKoon, G. (2008). The diffusion decision model: Theory and data for two-choice decision tasks. *Neural Computation*, 20(4), 873–922. DOI: 10.1162/neco.2008.12-06-420.  
[5] Love, B. C. (2015). The algorithmic level is the bridge between computation and brain. *Topics in Cognitive Science*, 7(2), 230–242. DOI: 10.1111/tops.12131.  
[6] Borst, A., & Theunissen, F. E. (1999). Information theory and neural coding. *Nature Neuroscience*, 2, 947–957. DOI: 10.1038/14731.  
[7] Quian Quiroga, R., & Panzeri, S. (2009). Extracting information from neuronal populations: Information theory and decoding approaches. *Nature Reviews Neuroscience*, 10, 173–185.  
[8] Pouget, A., Dayan, P., & Zemel, R. (2000). Information processing with population codes. *Nature Reviews Neuroscience*, 1, 125–132.  
[9] Timme, N. M., & Lapish, C. (2018). A tutorial for information theory in neuroscience. *eNeuro*, 5(3). DOI: 10.1523/ENEURO.0052-18.2018.  
[10] Zheng, J., & Meister, M. (2025). The unbearable slowness of being: Why do we live at 10 bits/s? *Neuron*. DOI: 10.1016/j.neuron.2024.11.008.  
[11] Bergmann, T. O., & Hartwigsen, G. (2021). Inferring causality from noninvasive brain stimulation in cognitive neuroscience. *Journal of Cognitive Neuroscience*, 33(2), 195–225. DOI: 10.1162/jocn_a_01591.  
[12] Bradley, C. et al. (2022). State-dependent effects of neural stimulation on brain function and cognition. *Nature Reviews Neuroscience*, 23, 459–475.

---

## 系列路徑

1. **Paper 01｜一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義**  
2. **Paper 02｜智能到底算了一次什麼？：最小智能語意執行單位的候選理論**  
3. **Paper 03｜從認知到神經元：人腦如何跨層測量智能計算**  
4. **Paper 04｜從神經元到焦耳：智能計算的能量、熱力學與物理下界**  
5. **Paper 05｜計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積**  
6. **Paper 06｜成果品質到底怎麼量？：從形式化正確性到結構化智能品質**  
7. **Paper 07｜不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估**  
8. **Paper 08｜自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間**  
9. **Paper 09｜拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本**  
10. **Paper 10｜一個答案值多少物理世界？：智能產率的統一計量框架**
