# TADC-PP-01：關係距離 × 外部領域距離交叉實驗——Pilot Protocol

**英文題名：** TADC Pilot Protocol 01: Relational Distance × External Domain Distance Crossover  
**系列階段：** TADC Phase II — Pilot Protocol  
**文件編號：** TADC-PP-01  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** Exploratory Pilot Protocol／刺激校準／量測可行性研究  
**上游依賴：** TADC-MD-01  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

TADC-MD-01 將「關係距離」選為整個 TADC 量測鏈的第一個地基，因為 dynamic domain、cross-domain continuity、topological hyperfocus 與部分 human–AI topology 命題都依賴：

$$
d_{\mathrm{rel}}(x,y\mid G)
$$

能被穩定估計，且能提供超越外部分類距離與一般語義相似度的預測資訊。

本文制定第一個可直接執行的 Pilot Protocol：

$$
\boxed{
\text{Relational Distance}
\times
\text{External Domain Distance Crossover}
}
$$

實驗採 2×2 設計：

| | Relation Near | Relation Far |
|---|---:|---:|
| Same External Domain | SN | SF |
| Cross External Domain | CN | CF |

最具 TADC 區辨力的候選對比為：

$$
\boxed{
K_{CN}<K_{SF},
}
$$

其中 \(K\) 是由 target response time、accuracy 與 target baseline difficulty 所估計的 transition cost。

此預測表示：

> 一個「跨外部領域但關係結構接近」的轉換，可能比「仍在同一外部領域但關係結構遙遠」的轉換更低成本。

如果此關係完全不存在，且 relational-distance model 對 held-out data 沒有超越 external-domain + semantic-similarity model 的預測增量，則 Relation-First Cognition Conjecture（RFCC）不應直接進入 confirmatory study。

本 Pilot 分兩階段：

### Stage A — Independent Stimulus Calibration

使用與主實驗不同的參與者，校準：

- external domain classification；
- structural / relational similarity；
- surface semantic similarity；
- familiarity；
- target-only accuracy；
- target-only response time。

### Stage B — Transition Pilot

另一批參與者執行 source → target microproblem transitions。每個 target 在單一 participant 中只出現一次，但透過四份 counterbalanced lists，使同一 target 在跨 participants 的資料中分別出現在 SN、SF、CN、CF 四條件。

本文刻意將主要依變量稱為：

$$
\boxed{
\text{transition cost}
}
$$

而不是直接宣稱等同經典 stimulus–response task-switch cost。2026 年研究已顯示 switch-cost logic 可以擴展到更複雜的 goal / decision tasks，而 hierarchical-control 研究亦顯示不同抽象層級的 reconfiguration 具有不同 RT 與 neural costs；但本 Pilot 仍需先證明自己的量測效度。

本研究的成功標準不是 \(p<.05\)。Pilot 主要判斷：

1. 刺激是否能把 relation 與 external domain 正交化；
2. \(d_{\mathrm{rel}}\) 是否具基本 reliability；
3. 2×2 transition task 是否有足夠準確率與 RT 變異；
4. relational model 是否在 held-out prediction 中提供非負／正向增量；
5. \(K_{CN}-K_{SF}\) 的方向與不確定度；
6. 哪些 design parameters 應在 confirmatory preregistration 前凍結。

**關鍵詞：** relational distance；cross-domain cognition；analogical structure；transition cost；task switching；pilot study；model comparison；TADC

---

# 0. 研究邊界

本文件是：

$$
\boxed{
\text{exploratory pilot protocol}.
}
$$

不是：

- preregistered confirmatory protocol；
- 臨床 ADHD 研究；
- TADC 理論驗證完成；
- 因果神經機制研究。

Pilot 的目的不是證明 RFCC，而是估計：

$$
\boxed{
\text{whether RFCC is measurable enough
to deserve a confirmatory test}.
}
$$

---

# 1. 直接攻擊的命題

TADC-06 的 Relation-First Cognition Conjecture（RFCC）最低版本：

$$
\boxed{
d_{\mathrm{rel}}
\text{ adds predictive value beyond }
d_{\mathrm{ext}}
\text{ and ordinary semantic similarity}.
}
$$

本文只攻擊這一版。

不直接驗：

- Topological Hyperfocus；
- Dynamic Cognitive Atlas；
- Six-Operator algebra；
- Human–AI topology。

---

# 2. 為什麼先測 RFCC？

如果：

$$
d_{\mathrm{rel}}
$$

本身測不穩，

則：

$$
D_t
=
D(
\mathcal R_t,
\kappa_t,
G_t
)
$$

也缺少可操作地基。

因此：

$$
\boxed{
\text{RFCC measurement failure}
}
$$

會迫使 TADC-02、TADC-05、TADC-06 的部分強命題一起縮減。

---

# 3. 現有鄰接研究

Analogical reasoning 已長期研究：

$$
\text{surface dissimilarity}
+
\text{relational similarity}.
$$

2022 年的 analogical mapping 研究直接追蹤人類如何建立兩個情境間共享 relational structure；2022 relation-learning computational theory 亦顯示 structured relational representations 可支援 cross-domain generalization。

2019 change-detection experiments 提供 relational re-representation 的行為證據，顯示 analogical alignment 可以伴隨 relation representation 的改變。

2025 task-space cognitive-map 研究顯示人腦會表示 task-relevant hidden states 與跨 task states 的抽象規則。

2026 hierarchical cognitive-control 研究則顯示 higher-level context 與 subordinate task-set switches 具有不同的 behavioral / neural reconfiguration。

這些研究支持本 Pilot 的可行性背景，但沒有直接回答：

$$
\boxed{
K_{CN}<K_{SF}\;?
}
$$

---

# 4. 主要設計：2×2 Crossing

兩因素：

## Factor A — External Domain

$$
D
\in
\{
\text{Same},
\text{Cross}
\}.
$$

## Factor B — Relational Structure

$$
R
\in
\{
\text{Near},
\text{Far}
\}.
$$

得到：

$$
\boxed{
SN,SF,CN,CF.
}
$$

---

# 5. 四個條件

## SN — Same Domain / Relation Near

相同表面領域、共享相同或高度相似的結構模板。

## SF — Same Domain / Relation Far

相同表面領域，但 underlying relational template 不同。

## CN — Cross Domain / Relation Near

表面領域不同，但 underlying relational template 相同或高度相似。

## CF — Cross Domain / Relation Far

表面領域不同，underlying relational template 也不同。

---

# 6. 最具區辨力對比

TADC 最重要的 Pilot contrast：

$$
\boxed{
\Delta_{RF}
=
K_{CN}-K_{SF}.
}
$$

RFCC 方向預測：

$$
\boxed{
\Delta_{RF}<0.
}
$$

---

# 7. 為什麼 CN vs SF 比 Near vs Far 主效應更重要？

如果只得到：

$$
K_{\mathrm{Near}}<K_{\mathrm{Far}},
$$

可能只是：

- semantic priming；
- familiarity；
- repeated strategy；
- generic similarity。

但是：

$$
K_{CN}<K_{SF}
$$

會更直接顯示：

> 外部領域改變本身不必比 relation structure 改變造成更大 transition cost。

仍然不是 RFCC 的最終證明，但區辨力更高。

---

# 8. 不稱為經典 switch cost

本文 primary variable 稱：

$$
\boxed{
K_{\mathrm{transition}}.
}
$$

理由：

本研究不是單純 parity/color task switching。

它測：

$$
\text{source microproblem}
\rightarrow
\text{target microproblem}.
$$

2026 年已有研究將 switch-cost 概念擴展到複雜 decision goals，因此此方向有方法論鄰接；但本研究先保持術語保守。

---

# 9. 刺激架構

建議建立四個 external surface domains：

1. **生命／生物系統**
2. **軟體／計算系統**
3. **市場／營運系統**
4. **物理／環境系統**

所有題目均：

- 自足；
- 不要求專業背景；
- 使用相同版面；
- 不使用 domain-specific 公式；
- 只需要短文本中提供的資訊。

---

# 10. 候選 relational templates

第一批建議八種：

1. Negative feedback；
2. Conservation / balance；
3. Bottleneck / limiting throughput；
4. Threshold cascade；
5. Diffusion / spread；
6. Hierarchy / nesting；
7. Optimization under constraint；
8. Recurrence / iterative dependence。

---

# 11. 為什麼使用 relation template？

這使 relation-near 不只依 participant 主觀感覺。

每個題目在 stimulus-generation 階段已有：

$$
R_{\mathrm{design}}
$$

ground-truth candidate。

但最後仍需 independent calibration：

$$
R_{\mathrm{rated}}.
$$

只有兩者一致才保留。

---

# 12. 一個例子：Negative Feedback

## 生命系統

某變量升高後會觸發調節機制，使其下降。

## 軟體系統

伺服器負載升高後系統增加資源，使負載回落。

這兩者：

$$
D_{\mathrm{ext}}
\neq
$$

但：

$$
R_{\mathrm{feedback}}
\approx.
$$

因此候選：

$$
CN.
$$

---

# 13. 一個 Same-Domain / Far 例子

仍在生命系統：

Source：

negative feedback。

Target：

hierarchical classification / nested organization。

則：

$$
D_{\mathrm{ext}}
=
\text{same},
$$

但：

$$
R_{\mathrm{source}}
\neq
R_{\mathrm{target}}.
$$

候選：

$$
SF.
$$

---

# 14. 避免直接提示 relation 名稱

題目正文不寫：

- feedback；
- bottleneck；
- diffusion；
- recursion。

否則 relation-near 可能退化成 lexical priming。

relation name 只存在 stimulus metadata。

---

# 15. Stage A — Independent Stimulus Calibration

Stage A 參與者不得進 Stage B。

避免：

$$
\boxed{
\text{same participants define and validate the metric}.
}
$$

---

# 16. Stage A 候選樣本

Pilot feasibility target：

$$
\boxed{
N_A=48
}
$$

完成校準。

這不是 confirmatory power target。

若招募成本需要降低，可分成多個 partial-rating forms。

---

# 17. Stage A 子任務

## A1 — Domain Classification

participant 將每個 microproblem 分到：

- 生命；
- 軟體；
- 市場／營運；
- 物理／環境；
- 無法判斷。

---

# 18. A1 Domain Gate

保留題目建議：

$$
P(
\text{modal domain label}
)
\geq
0.80.
$$

若低於：

$$
0.70,
$$

優先重寫。

中間區間：

$$
0.70\sim0.79
$$

列為候補。

這些門檻為 Pilot design rule，不是心理學通則。

---

# 19. A2 — Familiarity

7 點：

> 在讀題前，你對這類情境有多熟悉？

記：

$$
F_i.
$$

---

# 20. A3 — Surface Semantic Similarity

對 source-target pair：

7 點：

> 不考慮「背後運作原理」，只看主題、詞義與情境內容，兩者有多相似？

記：

$$
S^{surface}_{ij}.
$$

---

# 21. A4 — Structural / Relational Similarity

7 點：

> 忽略人物、領域與表面名詞，兩個情境「如何運作／如何解決問題」的結構有多相似？

記：

$$
S^{rel}_{ij}.
$$

---

# 22. A5 — Relation Confidence

另問：

> 你有多確定剛才的結構相似度判斷？

$$
C^{rel}_{ij}\in[1,7].
$$

---

# 23. A6 — Solo Target Performance

所有 target microproblems 需在**沒有 source predecessor**時獨立測：

- accuracy；
- RT。

得到：

$$
A_j^{solo},
$$

$$
RT_j^{solo}.
$$

---

# 24. Target Baseline

定義：

$$
B_j
=
\operatorname{median}
(
\log RT_j^{solo}
).
$$

Stage B 可估：

$$
\boxed{
K_{ij}
=
\log RT_{ij}^{target}
-
B_j.
}
$$

因此 target item difficulty 有獨立 baseline。

---

# 25. Relational Near / Far Calibration

候選 Near：

$$
\bar S^{rel}\geq5.5/7.
$$

候選 Far：

$$
\bar S^{rel}\leq2.5/7.
$$

中間：

$$
2.5<\bar S^{rel}<5.5
$$

不進第一版主 stimulus set。

仍屬 Pilot provisional thresholds。

---

# 26. Semantic Matching

核心目標：

Near / Far 的：

$$
S^{surface}
$$

不要和：

$$
S^{rel}
$$

完全共線。

刺激挑選時以 matching / optimization 使四條件的：

- surface similarity；
- length；
- readability；
- target solo RT；
- target solo accuracy；

盡量平衡。

---

# 27. 若 relation 和 semantic 無法拆開怎麼辦？

這本身就是 Measurement 結果。

如果：

$$
corr(
S^{rel},
S^{surface}
)
\rightarrow1,
$$

則目前刺激無法識別 RFCC。

決策：

$$
\boxed{
\text{REVISE stimulus construction}.
}
$$

不能硬進 Stage B。

---

# 28. Stage A Reliability

relational ratings 建議估：

- ICC；
- split-half；
- rater bootstrap。

Pilot Gate：

$$
ICC_{\mathrm{rel}}\geq0.60
$$

才進 Stage B 主分析。

目標值：

$$
\geq0.75
$$

較理想。

---

# 29. Stage A Target Gate

target 題目建議：

$$
0.70
\leq
Accuracy^{solo}
\leq
0.95.
$$

避免 floor / ceiling。

---

# 30. Stage B — Transition Pilot

另一批一般成人 participants。

不要求 ADHD。

---

# 31. Stage B 候選樣本

feasibility target：

$$
\boxed{
N_B=32
}
$$

completed participants。

理由：

- 足以檢查 task feasibility；
- 足以估 participant / item variance 的初步範圍；
- 足以測 list counterbalancing 是否工作。

不是 confirmatory power justification。

---

# 32. Stage B Trial Count

建議：

$$
64
$$

scored transition trials / participant。

即：

$$
16
$$

per condition：

- SN 16；
- SF 16；
- CN 16；
- CF 16。

另：

- practice 8；
- attention checks 少量；
- optional transfer probes 16。

---

# 33. 為什麼不一開始 200 trials？

microproblem 不像 parity task。

reading + reasoning 負荷較高。

Pilot 優先避免：

$$
\boxed{
\text{fatigue becomes the dominant transition effect}.
}
$$

---

# 34. Counterbalancing

建立：

$$
4
$$

份 lists：

$$
L_1,L_2,L_3,L_4.
$$

每個 target：

$$
T_j
$$

在每份 list 使用不同 predecessor type：

- SN；
- SF；
- CN；
- CF。

單一 participant：

$$
T_j
$$

只看一次。

跨 participants：

同一 target 可出現在四條件。

---

# 35. Counterbalancing 的重要性

這避免：

$$
\boxed{
\text{target difficulty}
}
$$

與：

$$
\boxed{
\text{condition}
}
$$

永久綁死。

分析仍加入：

$$
(1|target).
$$

---

# 36. Source Item

Source 也需：

- 自足；
- participant 作答；
- 有 accuracy；
- 不直接告訴 relation 名稱。

若 source 作答錯誤：

主分析保留 source-accuracy covariate；

sensitivity analysis 可只看 source-correct trials。

---

# 37. 一個 trial

## Step 1

fixation：

$$
500\text{ ms}.
$$

## Step 2

Source microproblem。

max：

$$
20\text{ s}.
$$

participant 作答。

## Step 3

blank / neutral transition：

$$
500\text{ ms}.
$$

## Step 4

Target microproblem。

max：

$$
20\text{ s}.
$$

participant 作答。

## Step 5

inter-trial interval：

$$
700\text{ ms}.
$$

---

# 38. Confidence Probe

不是每題都問。

隨機：

$$
25\%
$$

target trials 問：

> 對 target 答案有多確定？

避免 confidence response 本身擾亂所有 transition timing。

---

# 39. Optional Explicit Relation Probe

只在最後 block 後做，

不要 trial-by-trial 問：

> 兩題關係像不像？

否則 participant 會被訓練成主動找 analogy，

改變主實驗策略。

---

# 40. Instructions

主實驗不告知：

> 研究關係結構。

只說：

> 你會連續解兩個短問題，請盡可能正確、自然地作答。

這降低 demand characteristic。

---

# 41. Primary Outcome 1 — Target RT

使用：

$$
\log RT^{target}.
$$

主要只分析 correct-target trials。

另報 accuracy model。

---

# 42. Primary Outcome 2 — Baseline-adjusted Transition Cost

$$
\boxed{
K_{ij}
=
\log RT_{ij}^{target}
-
B_j.
}
$$

其中：

$$
B_j
$$

來自 Stage A target-only sample。

---

# 43. Secondary Outcome — Target Accuracy

binary：

$$
Y_{acc}\in\{0,1\}.
$$

使用 logistic mixed model。

---

# 44. Secondary Outcome — Transfer

對一部分 target 設計：

$$
\text{novel inference}
$$

只有真正抓到 structural relation 才容易答對。

不能只是重複 source 答案。

---

# 45. Primary Descriptive Contrast

$$
\boxed{
\Delta_{RF}
=
\bar K_{CN}
-
\bar K_{SF}.
}
$$

報：

- point estimate；
- bootstrap CI；
- participant-level distribution。

Pilot 不以：

$$
p<.05
$$

判決。

---

# 46. Factorial Effects

Relation effect：

$$
\Delta_R
=
K_{Far}-K_{Near}.
$$

Domain effect：

$$
\Delta_D
=
K_{Cross}-K_{Same}.
$$

Interaction：

$$
\Delta_{DR}.
$$

---

# 47. Mixed Model — Pilot Version

RT：

```text
log_target_rt ~
external_cross * relation_far
+ surface_similarity
+ familiarity
+ source_accuracy
+ trial_index
+ (1 | participant)
+ (1 | target)
```

若資料支援，再加入 participant random slopes。

---

# 48. Continuous Relational Model

比 binary Near/Far 更重要。

```text
log_target_rt ~
external_distance
+ surface_similarity
+ relational_distance
+ familiarity
+ source_accuracy
+ trial_index
+ random effects
```

binary 2×2 是 design。

continuous：

$$
d_{\mathrm{rel}}
$$

是理論 measurement。

---

# 49. Model M0

$$
M_0:
$$

- external distance；
- surface semantic similarity；
- familiarity；
- target baseline；
- source accuracy；
- trial index。

---

# 50. Model M1

$$
M_1
=
M_0
+
d_{\mathrm{rel}}.
$$

RFCC Minimum Test：

$$
\boxed{
\operatorname{Pred}_{heldout}(M_1)
>
\operatorname{Pred}_{heldout}(M_0).
}
$$

---

# 51. Held-out Strategy

Pilot 建議做兩種：

### Participant-held-out

測個體 generalization。

### Target-held-out

測 item generalization。

若只有 trial-held-out 成功，

證據較弱。

---

# 52. Pilot Prediction Metric

可用：

- MAE / RMSE for log RT；
- log predictive density；
- Brier / log loss for accuracy。

主文件不先鎖唯一 metric。

Pilot 後 confirmatory 再 freeze。

---

# 53. RT 清理：Pilot 原則

硬排除：

- technical failure；
- no response；
- RT < 500 ms；
- RT > 20 s timeout。

另做 sensitivity：

- participant-wise robust outlier filtering；
- no additional filtering。

Pilot 目標是了解 RT distribution，再為 preregistration freeze。

---

# 54. Participant Data Quality

候選 exclusion：

- overall target accuracy < 0.65；
- missing / timeout > 0.20；
- failed instruction checks；
- duplicate / technical corruption。

不依：

$$
\Delta_{RF}
$$

方向排除 participant。

---

# 55. Reading Ability / Language

題目統一繁體中文。

participant 需：

- 成年；
- 能流暢閱讀繁體中文。

其他 demographic variables：

- age；
- education；
- self-rated domain familiarity。

Pilot 用作描述／探索 moderation。

---

# 56. 專業背景

若 participant 是：

- programmer；
- biologist；
- economist；
- engineer；

可能對特定 external domains 有熟悉度優勢。

因此記錄：

$$
E_D
$$

並在 analysis 探索。

Confirmatory 才決定 stratification / exclusion。

---

# 57. 倫理與同意

若此 Pilot 實際招募人體參與者並用於正式研究／發表，應依執行機構與所在地適用的人體研究倫理程序處理 informed consent、資料保護、退出權與必要的倫理審查。

本 protocol 本身不等於已取得研究倫理核准。

---

# 58. 個資最小化

資料不要收：

- 真名；
- 精確住址；
- 不必要醫療資訊。

使用：

$$
participant\_id.
$$

---

# 59. ADHD 不在 Pilot 1 招募條件

不要求 diagnosis。

也不把 ADHD traits 當 primary predictor。

原因：

$$
\boxed{
\text{first test the general measurement}.
}
$$

---

# 60. Stage B Feasibility Outcomes

## F1

completion rate。

## F2

median trial duration。

## F3

accuracy distribution。

## F4

RT distribution。

## F5

counterbalance integrity。

## F6

model convergence。

## F7

participant fatigue rating。

---

# 61. 刺激 Feasibility Gate

GO if：

- ≥ 70% candidate targets 通過 calibration；
- domain agreement ≥ .80 for final items；
- relation ICC ≥ .60；
- relation near / far 有明顯分離；
- surface similarity 可被合理 matching。

---

# 62. Task Feasibility Gate

GO if：

- overall accuracy 約 0.70–0.95；
- timeout < 15%；
- four conditions 均有足夠 valid trials；
- RT 不大量堆在 timeout；
- participants 能理解 instructions。

---

# 63. RFCC Pilot Gate

## GO to confirmatory design

需要同時：

1. relational measure reliable；
2. \(M_1\) held-out prediction 不差於 \(M_0\)，且呈可重現正增量；
3. \(\Delta_{RF}\) 方向大致為負，或 continuous \(d_{\mathrm{rel}}\) effect 清楚；
4. effect 不完全被 surface similarity / familiarity 吸收。

---

# 64. REVISE

若：

- relation rating reliable；
- task works；
- 但 \(\Delta_{RF}\) 接近 0；
- model gain 非穩定；

則：

$$
\boxed{
\text{REVISE stimulus / task,
not claim support}.
}
$$

---

# 65. KILL Current Operationalization

若：

- relation ratings 不可靠；
- relation / semantic 無法拆；
- \(M_1\) 在 target-held-out / participant-held-out 都不優於 \(M_0\)；
- CN / SF 完全沒有理論方向；
- task variance 主要由 domain expertise 決定；

則：

$$
\boxed{
\text{do not proceed to preregistered RFCC confirmation}.
}
$$

這是 kill 當前 operationalization / escalation route，不是一次 Pilot 就證明所有可能的 relation-first cognition 永遠為假。

---

# 66. Pilot 不做 Null-Hypothesis Victory Claim

若：

$$
\Delta_{RF}\approx0,
$$

Pilot 只說：

> 此 operationalization 沒有提供值得進 confirmatory 的訊號。

不說：

> RFCC 已被宇宙級證偽。

---

# 67. Stage A → Stage B Freeze

Stage A 完成後，Stage B 開始前 freeze：

- final item set；
- condition assignment；
- baseline RT；
- relation ratings；
- semantic ratings；
- four counterbalanced lists。

不能看 Stage B 結果後換 item membership。

---

# 68. Stage B → Confirmatory Freeze

Pilot 後才決定：

- confirmatory sample size；
- exact exclusion；
- primary RT preprocessing；
- relational-distance formula；
- primary CV metric；
- minimal effect \(\delta\)。

---

# 69. Confirmatory Sample Planning

不直接從：

$$
p_{\mathrm{pilot}}
$$

決定 sample。

使用 Pilot 的：

- participant variance；
- item variance；
- residual variance；
- plausible effect range；

做 simulation-based precision / power planning。

---

# 70. Confirmatory Target

最終 preregistered study 應至少能區分：

$$
\Delta_{RF}=0
$$

與一個事先認為值得理論保留的：

$$
\delta_{\min}.
$$

\(\delta_{\min}\) 由 Pilot 決定，不在本 Protocol 任意指定。

---

# 71. Stimulus Generation 不應由單一 AI 直接當 ground truth

AI 可以生成 candidate microproblems。

但：

$$
\boxed{
\text{AI-generated relation label}
\neq
\text{validated relation label}.
}
$$

必須經 Stage A independent human calibration。

---

# 72. AI 可做什麼？

可以：

- 生成 paraphrase；
- 平衡長度；
- 建候選 relation templates；
- 找 lexical leakage；
- 產生 alternate sources。

但 final stimulus selection 由 calibration 決定。

---

# 73. Lexical Leakage Check

對 Near pairs 檢查是否共享：

- 相同關鍵動詞；
- relation 名稱；
- 明顯同義詞；
- 數字模式。

若 Near 只靠 lexical cue，

RFCC 會退化成：

$$
\text{surface priming}.
$$

---

# 74. Surface-Matched Pairing

理想：

$$
S^{surface}_{CN}
\approx
S^{surface}_{SF}.
$$

同時：

$$
S^{rel}_{CN}
>
S^{rel}_{SF}.
$$

這是最重要的刺激工程目標之一。

---

# 75. Reading Length

對 source / target：

- character count；
- sentence count；
- number of alternatives；

盡量匹配。

分析保留 text length covariate 作 sensitivity。

---

# 76. Target Answer Position

四選一答案位置：

$$
1,2,3,4
$$

平衡。

避免 condition 和 motor response 綁定。

---

# 77. Relation Template × Domain Matrix

每個 relational template 至少應有：

$$
\geq4
$$

external-domain realizations。

這使 CN transition 不依賴單一 domain pair。

---

# 78. Domain Pair Balance

Cross transitions：

- Life ↔ Software；
- Life ↔ Market；
- Life ↔ Physical；
- Software ↔ Market；
- Software ↔ Physical；
- Market ↔ Physical；

盡量平衡。

---

# 79. Source-Target Direction

若：

$$
A\rightarrow B
$$

與：

$$
B\rightarrow A
$$

可能不同，

Stage B 應平衡方向。

relation 本身不預設對稱。

---

# 80. Directed Relations

某些：

$$
r_C,r_P
$$

具有方向。

所以 relation metadata 應保存：

$$
R_{A\rightarrow B}
$$

與：

$$
R_{B\rightarrow A}.
$$

---

# 81. Relation Near 不是「同答案」

source / target 不能只是答案一樣。

應共享：

$$
\boxed{
\text{inference structure},
}
$$

而非：

$$
\boxed{
\text{response identity}.
}
$$

---

# 82. Pilot Transfer Probe

對 16 題加一個 post-target probe：

> 下列哪一個變化最可能讓這個系統失去原本的穩定／限制／傳播特性？

用來測 structural transfer。

不放在 primary RT trial 之前。

---

# 83. Demand Characteristic Check

實驗結束問：

> 你覺得這個實驗主要在研究什麼？

若大量 participant 精確猜到：

> 跨領域的結構相似性，

需在報告中註明。

---

# 84. Debriefing

結束後告知：

- 研究比較表面領域與 underlying relation；
- relation ratings 來自獨立 calibration；
- 沒有 clinical diagnosis。

---

# 85. Data Files

Stage A：

- `stimuli.csv`
- `calibration_domain.csv`
- `calibration_pair_ratings.csv`
- `solo_target_baseline.csv`

Stage B：

- `participants.csv`
- `trials.csv`
- `transfer_probes.csv`
- `counterbalance_lists.csv`

Analysis：

- `analysis_config.json`
- `pilot_report.md`

---

# 86. Stimuli CSV 最小欄位

```text
stimulus_id
domain
relation_template
variant_id
text
question
option_1
option_2
option_3
option_4
correct_option
char_count
version
```

---

# 87. Pair CSV 最小欄位

```text
pair_id
source_id
target_id
designed_domain_relation
designed_relational_relation
external_condition
relational_condition
surface_similarity_mean
relational_similarity_mean
relational_confidence_mean
pair_status
```

---

# 88. Stage B Trial Log

```text
participant_id
list_id
trial_index
source_id
target_id
condition
source_rt
source_correct
target_rt
target_correct
confidence
timeout
technical_error
```

---

# 89. Analysis Config

至少記：

- protocol version；
- stimulus version；
- relation ontology version；
- exclusion version；
- model formulas；
- CV split seed；
- software version。

---

# 90. Reproducibility

Pilot report 應能由：

$$
\boxed{
\text{raw derived data + config + analysis code}
}
$$

重建。

不要手動複製數字進報告。

---

# 91. Pilot Report 必須有的表

1. Stage A calibration table；
2. relation vs semantic correlation；
3. final stimulus balance；
4. condition accuracy；
5. condition RT；
6. CN–SF contrast；
7. M0 vs M1 held-out prediction；
8. participant / item variance；
9. exclusion summary；
10. GO / REVISE / KILL decision。

---

# 92. Pilot Report 必須有的圖

1. relational vs semantic scatter；
2. four-condition RT distribution；
3. participant-level \(\Delta_{RF}\)；
4. target-item \(\Delta_{RF}\)；
5. held-out prediction comparison。

---

# 93. 不在 Pilot 報的結論

不要寫：

> TADC 被證明。

不要寫：

> 人類認知以關係為第一原理。

不要寫：

> 學科領域只是幻覺。

Pilot 最多寫：

$$
\boxed{
\text{the RFCC operationalization
did / did not survive feasibility testing}.
}
$$

---

# 94. Pilot 的第一個真正價值

即使結果失敗，

也能回答：

- relation / semantic 是否可分；
- external domain 是否能正交操縱；
- transition RT 是否適合此問題；
- 哪些 relation templates 太明顯／太難；
- expertise confound 多大。

這些都是有效結果。

---

# 95. Success State A

最理想：

$$
\Delta_{RF}<0,
$$

M1 held-out gain positive，

且：

$$
corr(
S^{rel},
S^{surface}
)
$$

不高。

則：

$$
\boxed{
\text{GO to preregistered RFCC confirmation design}.
}
$$

---

# 96. Success State B

若：

$$
\Delta_{RF}\approx0
$$

但 continuous：

$$
d_{\mathrm{rel}}
$$

穩定預測 target transition cost，

可能：

binary Near/Far threshold 太粗。

決策：

$$
\boxed{
\text{REVISE 2×2 categorization,
retain continuous RFCC route}.
}
$$

---

# 97. Failure State A

relation ratings 本身：

$$
ICC<0.60.
$$

決策：

$$
\boxed{
\text{do not interpret Stage B as RFCC test}.
}
$$

---

# 98. Failure State B

Near / Far 與 semantic similarity 幾乎完全共線。

決策：

$$
\boxed{
\text{stimulus construction failed}.
}
$$

不是 RFCC 理論直接失敗。

---

# 99. Failure State C

calibration 很乾淨，

但：

$$
M_1\leq M_0
$$

跨 participant-held-out 與 target-held-out 都穩定。

且：

$$
\Delta_{RF}\geq0.
$$

這才是對當前 RFCC operationalization 的真正負面結果。

---

# 100. 下一步條件

只有 GO 時進：

$$
\boxed{
\text{TADC-PR-01 Confirmatory Preregistration}.
}
$$

REVISE 時：

$$
\boxed{
\text{TADC-PP-01 v0.2}.
}
$$

KILL 時：

停止 RFCC confirmatory escalation，

回 TADC-MD-01 重新評估：

$$
d_{\mathrm{rel}}.
$$

---

# 101. 結論

TADC-PP-01 將 TADC 第一個最基礎的理論分歧變成一個可執行實驗：

$$
\boxed{
\text{Does relational distance predict transition cost
beyond external-domain and semantic distance?}
}
$$

設計的核心不是只比較：

$$
\text{Same}
$$

與：

$$
\text{Cross}.
$$

而是強迫：

$$
\boxed{
\text{external domain}
}
$$

與：

$$
\boxed{
\text{relational structure}
}
$$

交叉。

最有區辨力的候選結果：

$$
\boxed{
K_{CN}<K_{SF}.
}
$$

即：

> **跨領域但關係近，可能比同領域但關係遠更低成本。**

然而本 Pilot 不以單一 contrast 決定理論。

真正的最低要求是：

$$
\boxed{
M_1
=
M_0+d_{\mathrm{rel}}
}
$$

在 held-out participants / targets 上比：

$$
M_0
$$

提供可重現的預測增量。

Stage A 獨立校準則確保：

$$
d_{\mathrm{rel}}
$$

不是在看到 Stage B 結果後才被任意定義。

因此本 Protocol 的科學價值正是：

$$
\boxed{
\text{separate definition,
measurement,
and validation}.
}
$$

如果 Pilot 失敗，

TADC 得到第一個真正有價值的負面結果。

如果 Pilot 存活，

下一步也不是宣告理論成立，

而是把 Pilot 的 variance、item behavior 與 measurement error 用來建立：

$$
\boxed{
\text{TADC-PR-01 preregistered confirmatory study}.
}
$$

這才是 TADC 從命題系列走向實證研究的第一個真正入口。

---

# 參考文獻

1. Enisman M, Cordova A, Kleiman T. **It was the best of times, it was the worst of times: Evidence for switch cost beyond stimulus-response tasks.** *Journal of Experimental Psychology: Learning, Memory, and Cognition*. 2026. doi:10.1037/xlm0001643. PMID: 42406489.  
2. Mendl J, Bratzke D, Dreisbach G. **Task switching promotes switch readiness: Evidence from forced and voluntary task switching.** *Cognition*. 2026;271:106458. doi:10.1016/j.cognition.2026.106458. PMID: 41643504.  
3. Leach SC, Chen X, Hwang K. **Hierarchical Reconfiguration of Neurocognitive Task Set Representations Mediates Cognitive Flexibility.** *Journal of Neuroscience*. 2026. doi:10.1523/JNEUROSCI.0113-26.2026. PMID: 42276789.  
4. Tan L, Qiu Y, Qiu L, et al. **The medial and lateral orbitofrontal cortex jointly represent the cognitive map of task space.** *Communications Biology*. 2025;8:163. doi:10.1038/s42003-025-07588-w. PMID: 39900714.  
5. Kroczek B, Ciechanowska I, Chuderski A. **Uncovering the course of analogical mapping using eye tracking.** *Cognition*. 2022;225:105140. doi:10.1016/j.cognition.2022.105140. PMID: 35483161.  
6. Doumas LAA, Puebla G, Martin AE, Hummel JE. **A theory of relation learning and cross-domain generalization.** *Psychological Review*. 2022;129(5):999–1041. doi:10.1037/rev0000346. PMID: 35113620.  
7. Silliman DC, Kurtz KJ. **Evidence of analogical re-representation from a change detection task.** *Cognition*. 2019;190:128–136. doi:10.1016/j.cognition.2019.04.031. PMID: 31075695.  
8. Bosnjak M, Fiebach CJ, Mellor D, et al. **A template for preregistration of quantitative research in psychology: Report of the joint psychological societies preregistration task force.** *American Psychologist*. 2022;77(4):602–615. doi:10.1037/amp0000879. PMID: 34807636.  
9. Wilson RC, Takahashi YK, Schoenbaum G, Niv Y. **Orbitofrontal cortex as a cognitive map of task space.** *Neuron*. 2014;81(2):267–279. doi:10.1016/j.neuron.2013.11.005. PMID: 24462094.  
10. Schuck NW, Cai MB, Wilson RC, Niv Y. **Human Orbitofrontal Cortex Represents a Cognitive Map of State Space.** *Neuron*. 2016;91(6):1402–1412. PMID: 27657452.  

---

## 附錄 A：四條件記號

| Code | External Domain | Relation |
|---|---|---|
| SN | Same | Near |
| SF | Same | Far |
| CN | Cross | Near |
| CF | Cross | Far |

---

## 附錄 B：Pilot 決策

### GO

Measurement reliable + held-out relational increment + theoretically compatible direction.

### REVISE

Measurement works, predictive signal ambiguous or stimulus confounding remains.

### KILL CURRENT OPERATIONALIZATION

Relation measurement unreliable or cleanly calibrated relational model provides no held-out increment.

---

**狀態：** TADC-PP-01 v0.1  
**階段：** Exploratory Pilot Protocol  
**實際人體資料：** 尚未收集  
**Pilot sample targets：** Stage A \(N_A=48\)，Stage B \(N_B=32\)，僅作 feasibility targets，不是 confirmatory power justification  
**下一步：** 刺激集 v0.1 → Stage A Calibration → Stage B Pilot → GO / REVISE / KILL
