# ADHD 動態配置統合理論：可證偽命題與未來研究綱領

**英文題名：** An Integrated Dynamic Configuration Theory of ADHD: Falsifiable Hypotheses and a Future Research Program  
**系列：** ADHD 動態配置與認知拓撲系列，第 10 篇／封頂篇  
**版本：** v1.0  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論整合／認知科學命題／研究綱領／系列封頂文件  
**文獻檢索截點：** 2026-08-17  

---

# 0. 醫學、診斷、藥理與證據邊界聲明

本文不是臨床研究、診斷工具、治療指南、藥理試驗、神經影像 biomarker 研究或醫療建議。

本文提出的「動態配置」「神經調節層」「配置熵」「認知拓撲」「臨床可見性」「連續配置空間」「情境匹配核」等概念均屬待驗證理論構件。除非本文明確指出某一背景結論來自既有研究，否則不能將本文新增數學形式視為已被神經科學、精神醫學或臨床心理學驗證的 ADHD 機制。

原作者並非醫學、精神醫學、藥理學、神經科學、遺傳學或臨床心理專業研究者。本文不提供新的臨床、人體、藥理、遺傳、神經影像、流行病學或心理實驗數據。本文所有實證性背景均依賴公開同行評審文獻與正式分類資料。

本文不使用原作者的個人 ADHD 診斷史、用藥經驗或其他個人經驗作為一般化實證證據。個人觀察最多可構成研究問題的來源，不構成群體層證明。

本文不得被用於：

- 自行診斷或排除 ADHD；
- 替他人判斷是否有 ADHD；
- 自行開始、停止、增加、減少或混合藥物；
- 以本文的 configuration score、entropy、graph metric 或 fit score 取代臨床評估；
- 以「局部優勢」否定功能損害或醫療需要；
- 以「連續光譜」主張所有人都有 ADHD；
- 以「biotype」主張目前已有可供個人臨床使用的腦影像分型。

本文最核心的證據規則是：

$$
\boxed{
\text{formal plausibility}
\neq
\text{empirical validation}
\neq
\text{clinical utility}.
}
$$

---

# 摘要

本系列以十篇論文重新檢視 ADHD 是否能被建模為一個多層、動態、情境依賴的配置系統，而不是僅以「注意力不足」作為完整機制敘述。

截至 2026 年，外部研究已提供數個彼此相容的重要背景。第一，ADHD symptoms、功能損害與遺傳 liability 具有明顯 dimensional evidence；2025 年大型 GWAS 支持 clinical ADHD 位於由 ADHD symptoms 索引的 continuous liability 高端。第二，ADHD 內部存在顯著 heterogeneity；2026 年 JAMA Psychiatry 的 normative morphometric-network study 在連續個體偏差上辨識出三個可外部驗證的 pediatric biotypes，顯示 dimensional variation 與 local clustering 可以同時存在。第三，刺激劑作用不能簡化為「增加一條注意力」；2025 年 Cell 研究將 stimulant-related connectivity effects 主要連結至 arousal、reward、salience 與 action-related systems，而 2026 年成人 ADHD dual-tracer PET 顯示 methylphenidate 同時影響 DAT 與 NET，但 transporter binding change 與 cognitive improvement 並非簡單一對一。第四，ADHD cognition 的平均值可能不足以描述動態差異；2025 年兒童研究發現 cognitive-control neural representations 的 temporal variability 與 spatial stability 差異，另有 methylphenidate 研究觀察到 whole-brain network flexibility 的穩定化。第五，adult ADHD literature 仍保留多項重大未解問題，包括 late-onset、emotional dysregulation、functional impairment、executive dysfunction、objective diagnostic measures 與長期 treatment effects。

基於上述背景，本篇將前九篇整合為「Integrated Dynamic Configuration Theory, IDCT-ADHD」。其最小核心不是：

$$
\text{ADHD}
=
\text{one mechanism},
$$

而是：

$$
\boxed{
\mathbf c_{i,t+1}
=
\Phi
\left(
\mathbf c_{i,t},
\mathbf q_{i,t},
\mathbf e_{i,t},
\mathbf s_{i,t}^{\mathrm{ext}},
\mathbf k_{i,t},
\mathbf u_{i,t};
\boldsymbol\theta_i
\right)
+
\boldsymbol\varepsilon_{i,t}.
}
$$

其中 $\mathbf c_{i,t}$ 是時間 $t$ 的動態認知配置， $\mathbf q$ 是任務／生活需求， $\mathbf e$ 是環境， $\mathbf s^{\mathrm{ext}}$ 是外部支架， $\mathbf k$ 是補償策略， $\mathbf u$ 是即時輸入， $\boldsymbol\theta_i$ 是較慢變個體參數。

客觀性能為：

$$
\mathbf p_{i,t}
=
F
\left(
\mathbf c_{i,t},
\mathbf q_{i,t},
\mathbf e_{i,t}
\right).
$$

主觀狀態：

$$
\chi_{i,t}
=
H
\left(
\mathbf c_{i,t},
\mathbf e_{i,t},
\mathbf x_{i,t}^{\mathrm{expectancy}}
\right).
$$

元認知估計：

$$
\widehat{\mathbf p}_{i,t}
=
M
\left(
\mathbf p_{i,t},
\chi_{i,t},
\mathbf f_{i,t}^{\mathrm{feedback}}
\right).
$$

功能損害：

$$
\mathbf i_{i,t}
=
J
\left(
\mathbf p_{i,t},
\mathbf q_{i,t},
\mathbf e_{i,t},
\mathbf s_{i,t}^{\mathrm{ext}},
\mathbf k_{i,t}
\right).
$$

臨床診斷則保留為獨立決策層：

$$
\boxed{
\mathfrak D_{i,t}
=
\Gamma
\left(
\mathbf y_{i,t},
\mathbf i_{i,t},
H_i^{\mathrm{dev}},
X_{i,t}^{\mathrm{diff}}
\right),
}
$$

其中 $\mathbf y$ 為可觀察表型， $H^{\mathrm{dev}}$ 為發展史， $X^{\mathrm{diff}}$ 為跨情境與鑑別診斷證據。

因此本理論的核心不是把 ADHD 診斷替換成數學模型，而是提出：

$$
\boxed{
\text{Configuration}
\neq
\text{Phenotype}
\neq
\text{Impairment}
\neq
\text{Diagnosis}.
}
$$

本篇建立三層證據帳本：（A）已有較強外部證據支持的背景；（B）有間接或局部支持、但仍需特定驗證的中層連結；（C）主要由本系列提出的新假說。配置熵、認知 graph topology、disengagement barrier、attention debt、reversal surface 等均被明確列入 C 層，不得與 continuous genetic liability、clinical heterogeneity 等 A 層證據等量齊觀。

本文提出十八項統一可證偽命題與六階段研究綱領。若高維動態模型不能在獨立樣本中超越 symptom score、executive-function model、單一 trait dimension 或現行 diagnosis 對功能損害、病程與 treatment-relevant outcomes 的預測，本理論應被簡化或放棄。

最終研究問題是：

$$
\boxed{
\text{Does a dynamic, multilevel, context-sensitive configuration model
predict what simpler ADHD models systematically miss?}
}
$$

**關鍵詞：** ADHD、dynamic configuration、neuromodulation、attention allocation、heterogeneity、continuous liability、biotype、metacognition、context dependence、person–environment fit、falsifiability

---

# 1. 本系列真正提出了什麼？

本系列不是提出：

> ADHD 的真正本質已被找到。

更弱、也更科學的命題是：

> 是否存在一個可操作的中層動態模型，可以把神經調節、注意配置、狀態穩定性、認知路徑、主觀狀態、發展支架、功能損害與情境性能放進同一個可證偽框架？

因此：

$$
\boxed{
\text{IDCT-ADHD}
=
\text{research framework},
}
$$

不是：

$$
\boxed{
\text{IDCT-ADHD}
=
\text{established medical theory}.
}
$$

---

# 2. 十篇系列的依賴結構

本系列依序建立：

## Paper 1

$$
\text{Attention Deficit}
\rightarrow
\text{Dynamic Configuration Conjecture}.
$$

## Paper 2

$$
\text{Neuromodulation}
\neq
\text{Attention}.
$$

## Paper 3

$$
\text{Salience}
\neq
\text{Activation}
\neq
\text{Allocation}
\neq
\text{Observation}
\neq
\text{Update}
\neq
\text{Action}.
$$

## Paper 4

$$
\text{Distractibility}
\not\perp
\text{Hyperfocus-like lock-in}.
$$

## Paper 5

$$
\text{Associative breadth}
\neq
\text{Path diversity}
\neq
\text{Coherence}
\neq
\text{Convergence}.
$$

## Paper 6

$$
\text{Subjective state}
\neq
\text{Metacognitive confidence}
\neq
\text{Objective performance}.
$$

## Paper 7

$$
\text{Configuration}
\neq
\text{Impairment}
\neq
\text{Visibility}
\neq
\text{Diagnosis}.
$$

## Paper 8

$$
\text{Continuous variation}
+
\text{Local clusters}
+
\text{Categorical clinical decisions}.
$$

## Paper 9

$$
\text{Functional effect}
=
F
\left(
\text{Configuration},
\text{Task},
\text{Environment}
\right).
$$

## Paper 10

將上述結構統一並建立：

$$
\boxed{
\text{measurement}
\rightarrow
\text{prediction}
\rightarrow
\text{falsification}
\rightarrow
\text{possible translation}.
}
$$

---

# 3. 統一符號：停止讓不同論文的符號互相碰撞

前九篇在局部模型中使用過若干重複符號。

封頂篇重新定義 canonical notation。

## 3.1 神經調節狀態

$$
\mathbf n_t
=
\text{neuromodulatory state}.
$$

候選包括：

$$
\mathbf n_t
=
(D_t,NE_t,\ldots).
$$

---

## 3.2 中介調節狀態

$$
\mathbf z_t
=
\left(
z_t^{\mathrm{arousal}},
z_t^{\mathrm{reward}},
z_t^{\mathrm{salience}},
z_t^{\mathrm{vigor}},
z_t^{\mathrm{gating}},
z_t^{\mathrm{stability}}
\right).
$$

---

## 3.3 配置分布

$$
\boldsymbol\pi_t
=
\left(
\pi_1(t),\ldots,\pi_n(t)
\right),
$$

其中：

$$
\sum_i\pi_i(t)=1.
$$

---

## 3.4 配置動態

$$
\mathbf x_t
=
\left(
\widehat{\mathcal H}_{\pi},
L_t,
T_t^{\mathrm{dwell}},
\nu_t^{\mathrm{switch}},
B_t^{\mathrm{exit}},
R_t^{\mathrm{goal}}
\right).
$$

---

## 3.5 認知關係圖

$$
\mathcal G_t
=
\left(
V_t,E_t,W_t
\right).
$$

---

## 3.6 表徵、更新與行動狀態

$$
\mathbf m_t
=
\left(
m_t^{\mathrm{obs}},
m_t^{\mathrm{update}},
m_t^{\mathrm{memory}},
m_t^{\mathrm{gate}}
\right).
$$

---

## 3.7 客觀性能

$$
\mathbf p_t
=
\left(
p_t^{\mathrm{accuracy}},
p_t^{\mathrm{RT}},
p_t^{\mathrm{RTV}},
p_t^{\mathrm{memory}},
p_t^{\mathrm{inhibition}},
p_t^{\mathrm{reasoning}},
p_t^{\mathrm{transfer}},
\ldots
\right).
$$

---

## 3.8 主觀狀態

$$
\chi_t
=
\text{subjective clarity／engagement state}.
$$

---

## 3.9 元認知估計

$$
\widehat{\mathbf p}_t
=
\text{estimated performance}.
$$

---

## 3.10 生命／任務需求

$$
\mathbf q_t
=
\text{task and life demands}.
$$

---

## 3.11 環境

$$
\mathbf e_t
=
\text{environmental state}.
$$

---

## 3.12 外部支架

$$
\mathbf s_t^{\mathrm{ext}}
=
\text{external scaffolding}.
$$

---

## 3.13 補償策略

$$
\mathbf k_t
=
\text{compensation}.
$$

---

## 3.14 功能損害

$$
\mathbf i_t
=
\text{functional impairment profile}.
$$

---

## 3.15 臨床可見性

$$
v_t
=
\text{clinical visibility}.
$$

---

## 3.16 臨床判定

$$
\mathfrak D_t
\in
\{0,1\}.
$$

此符號只是抽象表示「不符合／符合正式診斷決策」，不是臨床計算公式。

---

# 4. 全域配置狀態

定義個體 $i$ 在時間 $t$ 的全域 configuration：

$$
\boxed{
\mathbf c_{i,t}
=
\left(
\mathbf n_{i,t},
\mathbf z_{i,t},
\boldsymbol\pi_{i,t},
\mathbf x_{i,t},
\mathcal G_{i,t},
\mathbf m_{i,t}
\right).
}
$$

此表示故意沒有直接包含：

$$
\mathfrak D.
$$

因為診斷不是底層認知狀態本身。

---

# 5. 全域狀態更新

候選：

$$
\boxed{
\mathbf c_{i,t+1}
=
\Phi
\left(
\mathbf c_{i,t},
\mathbf q_{i,t},
\mathbf e_{i,t},
\mathbf s_{i,t}^{\mathrm{ext}},
\mathbf k_{i,t},
\mathbf u_{i,t};
\boldsymbol\theta_i
\right)
+
\boldsymbol\varepsilon_{i,t}.
}
$$

其中：

- $\mathbf u_{i,t}$：即時輸入；
- $\boldsymbol\theta_i$：較慢變的個體參數；
- $\boldsymbol\varepsilon_{i,t}$：未建模波動。

這是系列最重要的候選動力式。

---

# 6. 為什麼一定要保留時間？

若只測：

$$
\overline{\mathbf c}_i
=
\frac1T
\sum_t
\mathbf c_{i,t},
$$

可能遺失：

$$
\operatorname{Var}_t(\mathbf c),
$$

$$
P
\left(
\mathbf c_{t+1}
\mid
\mathbf c_t
\right),
$$

$$
T^{\mathrm{dwell}},
$$

$$
\text{transition asymmetry}.
$$

2025 年 cognitive-control neural-stability 研究與 network-flexibility stimulant study 都支持：

$$
\boxed{
\text{temporal organization itself can carry information}.
}
$$

但這仍不證明本文的具體配置變量正確。

---

# 7. 外部證據層 A：目前相對較強的背景事實

本文把以下內容列入：

$$
\boxed{
\text{Evidence Layer A}.
}
$$

其意義是：

> 有多項現代研究或大型研究支持相關背景，但仍不代表本文所有中介公式成立。

---

# 8. A1：ADHD 是臨床有效的神經發展診斷框架

截至 2026 年 ICD-11 最新 release，ADHD 仍位於 neurodevelopmental-disorder framework。

因此本系列不主張：

$$
\boxed{
\text{replace ADHD diagnosis}.
}
$$

---

# 9. A2：ADHD 具有顯著異質性

2025 World Psychiatry 成人 ADHD 綜述明確將 heterogeneity、functional impairment、executive dysfunction、late-onset、emotional dysregulation 等列為重要研究問題。

2026 JAMA Psychiatry 又以 data-driven methods 找到可重現 pediatric biotypes。

因此：

$$
\boxed{
\text{ADHD}
\neq
\text{one uniform cognitive state}.
}
$$

---

# 10. A3：Symptoms 與 Genetic Liability 具有連續性

2025 Nature Genetics GWAS：

$$
290,134
$$

次 symptom measures，

來自：

$$
70,953
$$

名獨立個體，

支持 clinical ADHD 位於 ADHD symptom continuous liability 高端。

因此：

$$
\boxed{
\text{continuous liability}
}
$$

具有相當外部支持。

---

# 11. A4：連續性不排除 Local Clustering

2026 pediatric biotype study 的方法本身先建立 normative dimensional deviations，再進行 clustering。

因此：

$$
\boxed{
\text{dimension}
+
\text{cluster}
}
$$

不是邏輯矛盾。

---

# 12. A5：Stimulant 作用不是單純「Attention Channel Gain」

2025 Cell study 在大型 ABCD data 與 highly sampled drug-imaging validation 中，將 stimulant-related functional connectivity effects 主要連結至：

- arousal；
- reward；
- salience；
- action-related systems；

而非 canonical attention networks 的簡單增強。

因此：

$$
\boxed{
\text{stimulant effect}
\neq
\text{one attention-network amplifier}.
}
$$

---

# 13. A6：DAT 與 NET 都與 Methylphenidate 有關

2026 issue 的成人 ADHD longitudinal dual-tracer PET 顯示 extended-release methylphenidate 同時改變：

$$
DAT
$$

與：

$$
NET
$$

binding。

但 transporter change 與 cognitive improvement 不是簡單一對一。

因此：

$$
\boxed{
\text{target engagement}
\neq
\text{cognitive outcome}.
}
$$

---

# 14. A7：ADHD Cognitive／Neural Variability 值得獨立研究

2025 Nature Communications 兒童研究顯示：

$$
\text{temporal variability}\uparrow
$$

與：

$$
\text{spatial stability}\downarrow
$$

可以出現在 cognitive-control neural representations。

另有 2025 methylphenidate study 觀察到 whole-brain flexibility 降低及部分 behavioral variability 改善。

因此：

$$
\boxed{
\text{mean state}
\neq
\text{dynamic stability}.
}
$$

---

# 15. A8：成人 ADHD 的晚診斷與晚起病不可直接等同

2025 adult ADHD review 與 2026 late-onset literature 仍將 adult-onset ADHD 視為未完全解決的 controversy。

因此：

$$
\boxed{
\text{adult diagnosis}
\neq
\text{adult onset}.
}
$$

---

# 16. 外部證據層 B：有局部或間接支持的中層連結

以下列為：

$$
\boxed{
\text{Evidence Layer B}.
}
$$

它們不是純想像，但證據仍不足以支持本系列最強版本。

---

# 17. B1：Allocation Capacity 與 Allocation Stability 可分離

2025 working-memory prioritization 研究顯示，具有 ADHD symptoms 的成人仍可以依價值有效 prioritise information。

因此：

$$
\boxed{
\text{ADHD}
\not\Rightarrow
\text{universal allocation incapacity}.
}
$$

真正差異可能在：

- maintenance；
- switching；
- interference；
- update；
- context coupling。

但這需要臨床與跨任務 replication。

---

# 18. B2：Hyperfocus 可被量化，但不是 ADHD 專屬核心

2024 AHQ-D validation 支持 dispositional hyperfocus 可以可靠測量。

但：

$$
\text{hyperfocus}
\neq
\text{ADHD-specific defining symptom}.
$$

因此本系列只把 hyperfocus 作為 candidate state。

---

# 19. B3：Metacognitive Calibration 可能具有 Domain-Specific Difference

2026 college-student study 比較：

$$
70
$$

名正式診斷 ADHD 學生與：

$$
70
$$

名 matched controls，

在 verbal 與 non-verbal tasks 觀察到 performance 與 confidence calibration 差異。

但：

$$
\boxed{
\text{ADHD}
\neq
\text{global metacognitive blindness}.
}
$$

其他認知域仍可保有相對完整 metacognition。

---

# 20. B4：Associative Breadth／Divergent Thinking 可能在部分 Profiles 不同

既有成人 ADHD semantic-activation 與 creativity literature 支持：

$$
\text{associative breadth}
$$

與：

$$
\text{divergent thinking}
$$

可能存在 profile-specific differences。

但 2026 strengths review 顯示整個 evidence base 高度異質。

因此：

$$
\boxed{
\text{networked cognition}
}
$$

仍是候選機制，不是既定 ADHD 特徵。

---

# 21. B5：Person–Environment Fit 對 Function 具有合理性

2024 employment systematic review 顯示工作環境、support、structure、autonomy 與 ADHD occupational experience 具有重要關係。

但多數 evidence 仍不足以證明：

$$
\text{specific trait}
\rightarrow
\text{objective performance reversal}.
$$

所以 performance reversal 仍需實驗。

---

# 22. 外部證據層 C：主要由本系列提出的新假說

以下全部列為：

$$
\boxed{
\text{Evidence Layer C}.
}
$$

除非未來實驗支持，不得稱為 ADHD 已知機制。

---

# 23. C1：Allocation Entropy

$$
\widehat{\mathcal H}_{\pi}
=
-\frac{
\sum_i\pi_i\log\pi_i
}{
\log n
}.
$$

目前只是候選描述變量。

它不是：

- EEG entropy；
- thermodynamic entropy；
- validated ADHD biomarker。

---

# 24. C2：Disengagement Barrier

$$
B^{\mathrm{exit}}
$$

表示從 dominant allocation state 退出的候選成本。

目前沒有成熟 ADHD standard measure。

---

# 25. C3：Attention Debt

$$
D_t^{\mathrm{attn}}
$$

表示長期未處理必要事件形成的累積負荷。

這是本系列新增機制。

---

# 26. C4：Cognitive Path Topology

$$
\mathcal G_t
=
(V_t,E_t,W_t)
$$

及：

$$
D_P,
\overline C_P,
X_P,
E_{\mathrm{conv}}
$$

都是本系列中層模型。

不能用 brain network topology 直接證明。

---

# 27. C5：Configuration Phase Transition

「相變」只表示：

$$
\text{nonlinear regime shift}.
$$

它不是對真實腦熱力學相變的宣稱。

---

# 28. C6：Reversal Surface

$$
\mathcal R_k
=
\left\{
(T,E):
\frac{\partial P}{\partial c_k}=0
\right\}.
$$

這是 performance-reversal research 的新候選工具。

---

# 29. C7：Global Fit Kernel

$$
K_{\mathrm{fit}}
=
K
\left(
\mathbf c,
\mathbf q,
\mathbf e
\right).
$$

尚未被 ADHD workplace research 直接驗證。

---

# 30. 統一 Neuromodulation Layer

第 2 篇的 canonical form：

$$
\mathbf z_t
=
\Psi
\left(
\mathbf n_t,
\mathbf b_i,
\mathbf q_t,
\mathbf e_t
\right).
$$

其中：

$$
\mathbf n_t
$$

不是注意力本身。

而：

$$
\mathbf z_t
$$

可能調節：

- arousal；
- reward；
- salience；
- vigor；
- gating；
- stability。

---

# 31. 統一 Allocation Layer

給定候選事件：

$$
\mathcal E_t
=
\{e_1,\ldots,e_n\},
$$

配置：

$$
\boldsymbol\pi_t
=
\Pi
\left(
\mathbf z_t,
\mathbf q_t,
\mathbf m_t,
\mathbf h_t
\right).
$$

其核心不是：

$$
\text{attention amount},
$$

而是：

$$
\boxed{
\text{who gets processing opportunity}.
}
$$

---

# 32. Processing Opportunity 命題

令：

$$
o_t(e)
$$

為有效處理。

則：

$$
P
\left(
o_t(e)=1
\mid
\pi_t(e)
\right)
$$

通常可以隨配置提高，但不必：

$$
=1.
$$

所以：

$$
\boxed{
\text{allocation}
\neq
\text{successful processing}.
}
$$

---

# 33. Observation–Update–Action 分離

本文統一為：

$$
m_t^{\mathrm{obs}},
$$

$$
m_t^{\mathrm{update}},
$$

$$
m_t^{\mathrm{gate}}.
$$

因此可以：

$$
m^{\mathrm{obs}}>0
$$

但：

$$
m^{\mathrm{update}}\approx0,
$$

也可以：

$$
m^{\mathrm{update}}>0
$$

但：

$$
m^{\mathrm{gate}}=0.
$$

所以：

$$
\boxed{
\text{noticed}
\neq
\text{updated}
\neq
\text{acted}.
}
$$

---

# 34. 統一 Allocation Dynamics

$$
\mathbf x_t
=
\left(
\widehat{\mathcal H}_{\pi},
L_t,
T_t^{\mathrm{dwell}},
\nu_t^{\mathrm{switch}},
B_t^{\mathrm{exit}},
R_t^{\mathrm{goal}}
\right).
$$

此層用來描述：

- distribution；
- dominance；
- dwell；
- switching；
- disengagement；
- goal-relative allocation。

---

# 35. Distractibility 的統一定義方向

分心不能單獨由 entropy 決定。

令：

$$
R_t^{\mathrm{goal}}
=
\sum_{e\in\mathcal G_t^{\mathrm{goal}}}
\pi_t(e).
$$

則 task-relative distraction：

$$
D_t^{\mathrm{task}}
=
1-R_t^{\mathrm{goal}}.
$$

因此：

$$
\widehat{\mathcal H}_{\pi}\downarrow
$$

仍可能：

$$
D_t^{\mathrm{task}}\uparrow
$$

如果資源集中在錯誤目標。

---

# 36. Hyperfocus-like State 的統一候選

候選至少需要：

$$
L_t\uparrow,
$$

$$
T_t^{\mathrm{dwell}}\uparrow,
$$

$$
B_t^{\mathrm{exit}}\uparrow.
$$

因此：

$$
\boxed{
\text{low entropy alone}
\neq
\text{hyperfocus}.
}
$$

---

# 37. 統一 Cognitive Topology Layer

$$
\mathcal G_t
=
(V_t,E_t,W_t).
$$

需要至少區分：

$$
\text{semantic},
$$

$$
\text{causal},
$$

$$
\text{temporal},
$$

$$
\text{analogical},
$$

$$
\text{goal}.
$$

多 association 不能直接叫推理。

---

# 38. Topology Quality

候選：

$$
\Theta_t^{\mathrm{topo}}
=
\left(
B_t^{\mathrm{assoc}},
R_t^{\mathrm{act}},
D_t^{P},
C_t^{P},
X_t^{P},
E_t^{\mathrm{conv}}
\right).
$$

有效多路徑 cognition 需要：

$$
\boxed{
\text{Expansion}
+
\text{Coherence}
+
\text{Cross-validation}
+
\text{Convergence}.
}
$$

---

# 39. 統一 Subjective–Metacognitive Layer

主觀狀態：

$$
\chi_t.
$$

元認知 performance estimate：

$$
\widehat{\mathbf p}_t.
$$

客觀 performance：

$$
\mathbf p_t.
$$

因此：

$$
\boxed{
\chi_t
\neq
\widehat{\mathbf p}_t
\neq
\mathbf p_t.
}
$$

---

# 40. Metacognitive Error

$$
\mathbf e_t^{\mathrm{meta}}
=
\widehat{\mathbf p}_t
-
\mathbf p_t.
$$

這個誤差可以：

- positive；
- negative；
- domain-specific；
- state-dependent。

所以：

$$
\boxed{
\text{ADHD}
\neq
\text{global overconfidence}.
}
$$

---

# 41. Metacognitive Feedback

$$
\mathbf p_t
\rightarrow
\widehat{\mathbf p}_t
\rightarrow
\mathbf a_{t+1}^{\mathrm{strategy}}
\rightarrow
\mathbf p_{t+1}.
$$

因此 metacognition 不只是 report，也可能參與下一步行動。

---

# 42. 統一 Life-History Layer

生命需求：

$$
\mathbf q_t.
$$

外部支架：

$$
\mathbf s_t^{\mathrm{ext}}.
$$

補償：

$$
\mathbf k_t.
$$

有效需求—支持差：

$$
\boxed{
\mathbf l_t
=
\mathbf q_t
-
\mathbf r_t
-
\mathbf s_t^{\mathrm{ext}}
-
\mathbf k_t^{\mathrm{net}},
}
$$

其中 $\mathbf r_t$ 表示可用功能資源。

---

# 43. Compensation Cost

$$
\mathbf k_t^{\mathrm{net}}
=
\mathbf k_t
-
\mathbf c_t^{K}.
$$

這避免：

$$
\text{successful output}
$$

被直接等同：

$$
\text{low burden}.
$$

---

# 44. Impairment Layer

$$
\mathbf i_t
=
J
\left(
\mathbf p_t,
\mathbf q_t,
\mathbf e_t,
\mathbf s_t^{\mathrm{ext}},
\mathbf k_t
\right).
$$

因此：

$$
\boxed{
\text{symptom}
\neq
\text{impairment}.
}
$$

---

# 45. Visibility Layer

$$
v_t
=
V
\left(
\mathbf y_t,
\mathbf i_t,
\Omega_o,
A_t^{\mathrm{care}}
\right).
$$

其中：

- $\Omega_o$：觀察者 sampling domain；
- $A^{\mathrm{care}}$：醫療可近性。

所以：

$$
\boxed{
\text{impairment}
\neq
\text{visibility}.
}
$$

---

# 46. Clinical Decision Layer

$$
\boxed{
\mathfrak D_t
=
\Gamma
\left(
\mathbf y_t,
\mathbf i_t,
H^{\mathrm{dev}},
X_t^{\mathrm{diff}}
\right).
}
$$

這一層故意不由：

$$
\mathbf c_t
$$

直接推出。

原因是正式 ADHD diagnosis 還必須處理：

- developmental history；
- cross-context evidence；
- differential diagnosis；
- functional significance。

---

# 47. Continuous Configuration Space

令：

$$
\mathbf c_{i,t}
\in
\Omega_C.
$$

群體：

$$
\rho(\mathbf c).
$$

clinical ADHD sample：

$$
\rho_D(\mathbf c).
$$

因此可以：

$$
\boxed{
\text{continuous density}
+
\text{local cluster structure}.
}
$$

---

# 48. Subthreshold 邊界

本文再次明確：

$$
\boxed{
\text{subthreshold traits}
\neq
\text{hidden clinical ADHD}.
}
$$

可以：

$$
\mathfrak D=0
$$

但：

$$
\mathbf y\neq0
$$

或：

$$
\mathbf i\neq0.
$$

這表示可能需要支持，不表示特定 diagnosis 必然成立。

---

# 49. 統一 Context-Fit Layer

任務需求：

$$
\mathbf q_T.
$$

環境：

$$
\mathbf e.
$$

configuration：

$$
\mathbf c.
$$

fit：

$$
K_{\mathrm{fit}}
=
K
\left(
\mathbf c,
\mathbf q_T,
\mathbf e
\right).
$$

performance：

$$
\mathbf p
=
F
\left(
K_{\mathrm{fit}},
\mathbf c,
\mathbf q_T,
\mathbf e
\right).
$$

---

# 50. Performance Reversal

對 configuration dimension：

$$
c_k,
$$

定義：

$$
\beta_k(T,E)
=
\frac{
\partial P
}{
\partial c_k
}.
$$

真正 reversal 需要：

$$
\beta_k(T_a,E_a)<0
$$

而：

$$
\beta_k(T_b,E_b)>0.
$$

這仍是 C 層候選命題，尚未被 ADHD literature 系統驗證。

---

# 51. 局部優勢與全域損害可同時成立

令：

$$
A_i(T,E)
=
P_i(T,E)-P_{\mathrm{ref}}(T,E).
$$

可以：

$$
A_i(T^*,E^*)>0
$$

同時：

$$
\|\mathbf i_i\|>0.
$$

所以：

$$
\boxed{
\text{local advantage}
\neq
\text{absence of disorder-related impairment}.
}
$$

---

# 52. 一條統一因果候選鏈

將所有層整合：

$$
\boxed{
\mathbf n_t
\rightarrow
\mathbf z_t
\rightarrow
\boldsymbol\pi_t
\rightarrow
\mathbf x_t
\rightarrow
\mathcal G_t
\rightarrow
\mathbf m_t
\rightarrow
\mathbf p_t
\rightarrow
\mathbf y_t.
}
$$

但同時存在：

$$
\boxed{
\mathbf q_t,
\mathbf e_t,
\mathbf s_t^{\mathrm{ext}},
\mathbf k_t
}
$$

對多層的調節。

---

# 53. 另一條主觀／元認知迴路

$$
\boxed{
\mathbf z_t
\rightarrow
\chi_t
\rightarrow
\widehat{\mathbf p}_t
\rightarrow
\mathbf a_{t+1}^{\mathrm{strategy}}
\rightarrow
\mathbf p_{t+1}.
}
$$

所以 subjectivity 不是附錄，而可能參與動態閉環。

---

# 54. 生命史／診斷鏈

$$
\boxed{
\mathbf p_t
+
\mathbf q_t
+
\mathbf e_t
+
\mathbf s_t^{\mathrm{ext}}
+
\mathbf k_t
\rightarrow
\mathbf i_t
\rightarrow
v_t
\rightarrow
\text{assessment}
\rightarrow
\mathfrak D_t.
}
$$

這條鏈解釋：

$$
\text{diagnosis timing}
$$

為何不能被當作：

$$
\text{biological onset time}.
$$

---

# 55. IDCT-ADHD 十八項統一可證偽命題

## U-H1：非單因子命題

不存在一個單一 scalar：

$$
a
$$

能穩定、完整解釋 ADHD-related symptom、impairment、task variation 與 treatment response。

如果單一 scalar model 在跨資料集持續勝過 IDCT，則本理論應簡化。

---

## U-H2：動態增量命題

加入：

$$
\operatorname{Var}_t(\mathbf c)
$$

與：

$$
P(\mathbf c_{t+1}\mid\mathbf c_t)
$$

應在部分 outcomes 提供超越平均值的預測力。

---

## U-H3：Allocation–Maintenance 分離命題

能初始 prioritise 不代表能長時間穩定維持配置。

---

## U-H4：Observation–Update–Action 分離命題

$$
\text{noticed}
\neq
\text{updated}
\neq
\text{acted}.
$$

若三者無法可靠操作化區分，SAD 部分應被簡化。

---

## U-H5：State-Multiplicity 命題

distractibility、mind wandering、adaptive focus 與 hyperfocus-like lock-in 不應被單一 attention amount 完整描述。

---

## U-H6：Neuromodulatory Mediation 命題

部分 pharmacological effects 透過：

$$
\mathbf z_t
$$

狀態中介，而不是直接：

$$
\text{drug}
\rightarrow
P.
$$

---

## U-H7：Subjective–Objective 分離命題

存在：

$$
\Delta\chi>0
$$

而：

$$
\Delta\mathbf p\approx0
$$

的可重現狀態。

---

## U-H8：Metacognitive Feedback 命題

$$
\widehat{\mathbf p}_t-\mathbf p_t
$$

能預測後續 strategy change。

---

## U-H9：Associative Breadth 非充分命題

$$
B^{\mathrm{assoc}}\uparrow
$$

只有在：

$$
C^P,
X^P,
E^{\mathrm{conv}}
$$

足夠時才可能提高有效推理。

---

## U-H10：Demand–Support 命題

$$
\mathbf q_t
-
\mathbf s_t^{\mathrm{ext}}
-
\mathbf k_t
$$

的變化應能解釋部分 within-person impairment change。

---

## U-H11：Visibility 非等同命題

功能損害與 clinical visibility 可在不同時間尺度變化。

---

## U-H12：Dimensional-plus-Cluster 命題

高維 ADHD-related space 同時容許 continuous variation 與 local clusters。

---

## U-H13：Subthreshold Non-Identity 命題

below-threshold traits 不等於 clinical ADHD。

---

## U-H14：Context-Fit 命題

$$
K_{\mathrm{fit}}
$$

對 objective task performance 應有增量預測力。

---

## U-H15：Performance-Reversal 命題

至少某些 configuration dimensions 在嚴格 matched tasks 中可能出現 effect-sign reversal。

---

## U-H16：Local–Global 分離命題

局部 performance advantage 不等於整體 impairment 消失。

---

## U-H17：Transdiagnostic Overlap 命題

部分 IDCT variables 應跨 ADHD、anxiety、sleep problems 等共享，因此不能被直接當 ADHD-specific biomarker。

---

## U-H18：Out-of-Sample Superiority 命題

整套模型只有在：

$$
P_{\mathrm{IDCT,out}}
>
P_{\mathrm{simpler,out}}
$$

時才值得保留。

這是最重要的一條。

---

# 56. 什麼叫「更簡單模型」？

至少應比較：

## M1：Binary Diagnosis Model

$$
P
=
F(\mathfrak D).
$$

## M2：Symptom Total Model

$$
P
=
F(S_{\mathrm{total}}).
$$

## M3：Executive Function Model

$$
P
=
F(EF).
$$

## M4：Single Dimensional Liability Model

$$
P
=
F(z_{\mathrm{ADHD}}).
$$

## M5：Static High-Dimensional Model

$$
P
=
F(\mathbf c).
$$

## M6：Dynamic Configuration Model

$$
P
=
F
\left(
\mathbf c_t,
\Delta\mathbf c_t,
T,
E
\right).
$$

只有：

$$
M6
$$

在外部驗證中有穩定增量，動態理論才有存在價值。

---

# 57. Complexity Penalty

模型越複雜，越容易 overfit。

因此 model selection 必須包括：

$$
\text{prediction gain}
-
\lambda
\text{complexity}.
$$

可以使用：

- held-out likelihood；
- cross-validation；
- information criteria；
- preregistered primary metric。

而不是：

> 模型看起來比較完整。

---

# 58. 研究綱領 Phase A：Construct Validation

第一階段完全不需要 neuroimaging。

先建立：

- allocation stability；
- disengagement；
- cognitive-path diversity；
- subjective clarity；
- compensation cost；
- context fit；

的可靠 measurement。

要求：

$$
\operatorname{Reliability}>0
$$

且跨 session 可重現。

如果 construct 本身測不穩，後面全部停止。

---

# 59. Phase B：Within-Person Dynamic Experiments

同一人跨不同：

- novelty；
- reward；
- structure；
- interruption；
- delay；
- task type；

重複測量。

核心：

$$
\boxed{
\text{within-person transition}
}
$$

而不是只做：

$$
\text{ADHD mean}
-
\text{control mean}.
$$

---

# 60. Phase C：Clinical Replication

Phase A、B 的 construct 必須在：

- clinically diagnosed ADHD；
- matched controls；
- relevant clinical comparison groups；

重現。

尤其需要：

- sleep disorders；
- anxiety；
- depression；
- autism；

作 differential comparison。

---

# 61. Phase D：Multimodal Mechanism

只有在行為 construct 成立後，再加入：

- EEG；
- fMRI；
- PET；
- pupillometry；
- actigraphy；
- digital phenotyping。

避免：

$$
\boxed{
\text{brain-first storytelling}.
}
$$

---

# 62. Phase E：Longitudinal Development

追蹤：

$$
\mathbf c_t,
\mathbf q_t,
\mathbf e_t,
\mathbf s_t^{\mathrm{ext}},
\mathbf k_t,
\mathbf i_t,
v_t.
$$

才能研究：

- late diagnosis；
- compensation collapse；
- developmental trajectories；
- context transition。

---

# 63. Phase F：Prediction and Translation

最後才測：

$$
P
\left(
\text{future impairment}
\mid
\mathbf c
\right),
$$

$$
P
\left(
\text{treatment response}
\mid
\mathbf c
\right).
$$

只有 out-of-sample predictive gain 足夠，才討論 precision support。

---

# 64. 不允許跳過的順序

本文提出：

$$
\boxed{
\text{Construct}
\rightarrow
\text{Reliability}
\rightarrow
\text{Replication}
\rightarrow
\text{Prediction}
\rightarrow
\text{Clinical utility}.
}
$$

不能：

$$
\text{nice equation}
\rightarrow
\text{clinical tool}.
$$

---

# 65. Measurement Principle 1：平均值與變異都要保存

至少測：

$$
\mathbb E[X],
$$

$$
\operatorname{Var}(X),
$$

$$
\operatorname{Autocorr}(X_t),
$$

$$
P(X_{t+1}\mid X_t).
$$

ADHD dynamic research 不應只報平均 performance。

---

# 66. Measurement Principle 2：主觀與客觀不能互換

同步測：

$$
\chi_t,
$$

$$
\widehat{\mathbf p}_t,
$$

$$
\mathbf p_t.
$$

主觀資料不是低級資料，但它測的是不同東西。

---

# 67. Measurement Principle 3：Task 必須明確參數化

不要只寫：

> attention task。

應寫：

$$
\mathbf q_T
=
\left(
\text{sustained demand},
\text{novelty},
\text{reward delay},
\text{switching},
\text{interruption},
\ldots
\right).
$$

否則 context dependence 無法重現。

---

# 68. Measurement Principle 4：Environment 必須被記錄

至少保留：

- noise；
- social presence；
- autonomy；
- structure；
- feedback；
- time pressure；
- support。

這些不能全部當 noise。

---

# 69. Measurement Principle 5：跨診斷對照

如果某變量：

$$
X
$$

在：

- ADHD；
- anxiety；
- sleep deprivation；

都相同改變，

則：

$$
X
$$

可能是 general dysregulation marker，而非 ADHD-specific marker。

這不是失敗，而是分類修正。

---

# 70. Measurement Principle 6：Clinical Diagnosis 不可由研究變量循環定義

若先用：

$$
X
$$

定義 ADHD subgroup，

再說：

$$
X
$$

證明 ADHD subgroup 不同，

即 circularity。

因此 clinical diagnosis 與 experimental constructs 必須保持可追溯分離。

---

# 71. Measurement Principle 7：多評分者與觀察域

保存：

$$
Y^{\mathrm{self}},
Y^{\mathrm{parent}},
Y^{\mathrm{teacher}},
Y^{\mathrm{partner}}.
$$

不要只求一個平均值就丟失 disagreement。

disagreement 本身可能包含 context information。

---

# 72. Measurement Principle 8：Treatment State 必須記錄

至少區分：

- stimulant-naïve；
- currently medicated；
- washout／not washout；
- treatment history；
- dose／formulation。

否則不同研究不應被直接比較。

---

# 73. 成人與兒童必須分開驗證

不能：

$$
\text{child ADHD mechanism}
\Rightarrow
\text{adult ADHD mechanism}
$$

自動成立。

需要：

$$
\boxed{
\text{developmental invariance test}.
}
$$

---

# 74. Cross-Cultural Validity

ADHD diagnosis、observer threshold、school demand 與 work structure 受文化與制度影響。

因此：

$$
\Phi_{\text{Taiwan}}
$$

不必：

$$
=
\Phi_{\text{US}}.
$$

研究需檢驗 measurement invariance。

---

# 75. Digital Phenotyping 的角色

2026 成人 ADHD digital-health review 顯示數位工具研究快速增加。

IDCT 可利用：

- task timing；
- switching；
- calendar behavior；
- phone interaction；
- EMA；

做高頻狀態測量。

但：

$$
\boxed{
\text{digital trace}
\neq
\text{diagnosis}.
}
$$

---

# 76. 生態瞬時評估

EMA 特別適合：

$$
\mathbf c_t
$$

與：

$$
\mathbf e_t
$$

的 repeated measurements。

例如每次記錄：

- current task；
- interest；
- stress；
- clarity；
- distraction；
- urge to switch；
- time awareness；
- competing obligations。

---

# 77. 模型必須保存零結果

如果某構念：

$$
X
$$

在 preregistered study：

$$
\Delta X\approx0,
$$

不能只把它移出故事。

需要保留：

$$
\text{null evidence}.
$$

本理論的演化應為：

$$
T_0
\rightarrow
\text{Test}
\rightarrow
T_1,
$$

而不是只累積正向發現。

---

# 78. Pre-registration Rule

所有關鍵 experiment 應提前固定：

- primary hypothesis；
- primary outcome；
- exclusion criteria；
- model comparison；
- stopping rule；
- multiplicity correction。

避免 model flexibility 讓任何結果都可以「解釋」。

---

# 79. Out-of-Sample Rule

任何新的 IDCT construct 要進入核心模型，至少要求：

$$
P_{\text{out}}
>
P_{\text{baseline,out}}.
$$

如果只在 training sample 漂亮：

$$
\boxed{
\text{discard or downgrade}.
}
$$

---

# 80. Falsification Level F0：Measurement Failure

如果：

$$
\operatorname{Reliability}(X)\approx0,
$$

直接淘汰 $X$。

不需要進入神經機制討論。

---

# 81. F1：Dissociation Failure

若：

$$
Q,
\widehat P,
P
$$

實際上高度不可分，

則 SMOSH 簡化。

若：

$$
Salience,
Activation,
Allocation
$$

不可區分，

則 SAD 簡化。

---

# 82. F2：Dynamic Failure

若：

$$
\operatorname{Var}_t(X)
$$

與 transition features 沒有增量價值，

則 dynamic component 應移除。

---

# 83. F3：Topology Failure

若 graph-derived：

$$
D_P,
C_P,X_P,E_{\mathrm{conv}}
$$

不優於普通 executive／divergent measures，

則 NCTH 淘汰。

---

# 84. F4：Context-Reversal Failure

若嚴格 matched-task crossover 中：

$$
\beta_k(T,E)
$$

從不換號，

performance-reversal hypothesis 應大幅削弱。

---

# 85. F5：Longitudinal Failure

若：

$$
\Delta q,
\Delta s^{\mathrm{ext}},
\Delta k
$$

無法預測 within-person impairment change，

DCVH 簡化。

---

# 86. F6：Clinical Increment Failure

如果整體 configuration model 在控制：

- diagnosis；
- symptom severity；
- executive function；
- IQ；
- comorbidity；

後：

$$
\Delta R^2\approx0,
$$

則 IDCT 不具有臨床研究增量價值。

---

# 87. 最強反證：簡單模型一直贏

如果跨多資料集：

$$
P(M_{\mathrm{simple,out}})
>
P(M_{\mathrm{IDCT,out}}),
$$

則最合理結論不是：

> 資料還不夠理解高深理論。

而是：

$$
\boxed{
\text{use the simpler model}.
}
$$

---

# 88. IDCT 成功的最低條件

本理論不需要所有模組都成立。

最低成功條件是：

1. 至少數個 dynamic constructs 可可靠測量；
2. 它們跨情境可重現；
3. 可預測 within-person performance changes；
4. 在 external data 有增量；
5. 能明確指出何時失效。

---

# 89. IDCT 的強成功條件

更強版本需要：

$$
\boxed{
\text{configuration}
\rightarrow
\text{future impairment}
}
$$

與：

$$
\boxed{
\text{configuration}
\rightarrow
\text{treatment-relevant outcome}
}
$$

具有可重複 external prediction。

在此之前不應宣稱 precision psychiatry。

---

# 90. Clinical Translation Guardrail

任何未來 clinical tool 至少需要：

- prospective validation；
- external replication；
- calibration；
- fairness；
- harm analysis；
- clinical utility analysis；
- clinician oversight。

不能只報：

$$
AUC.
$$

---

# 91. Imaging Biomarker Guardrail

2026 biotype study 是重要研究進展。

但目前不能：

$$
\boxed{
\text{brain scan}
\rightarrow
\text{routine ADHD diagnosis}.
}
$$

研究 stratification 與 clinical biomarker 仍是不同階段。

---

# 92. Genetics Guardrail

2025 genetics 支持 continuous liability。

但：

$$
\boxed{
\text{polygenic score}
\neq
\text{individual ADHD diagnosis}.
}
$$

IDCT 不使用 genetics 作單人 diagnostic oracle。

---

# 93. Strengths Guardrail

2026 strengths scoping review 支持 strengths field 值得研究。

但：

$$
\boxed{
\text{ADHD strength}
\neq
\text{universal advantage}.
}
$$

每個 strength 都需要：

- objective measure；
- context；
- comparator；
- cost；
- generalization。

---

# 94. Masking Guardrail

ADHD camouflaging／masking 目前仍需要更成熟 construct validation。

所以：

$$
\boxed{
\text{late diagnosis}
\neq
\text{masking by default}.
}
$$

---

# 95. Transdiagnostic Guardrail

如果 IDCT 最後發現：

$$
\mathbf c
$$

中的很多變量同樣適用於 anxiety、autism、sleep disorder，

可能意味：

$$
\boxed{
\text{IDCT becomes a general cognitive-regulation framework}.
}
$$

這不必視為失敗。

但其 ADHD-specific claim 必須縮小。

---

# 96. 理論可能最後「離開 ADHD」

這是一個重要可能。

若：

$$
\Phi
$$

對不同 neurodevelopmental／psychiatric groups 都有效，

則最合理名稱可能從：

$$
\text{ADHD Dynamic Configuration Theory}
$$

變成：

$$
\text{General Dynamic Cognitive Configuration Theory}.
$$

科學模型不應被原始命名綁架。

---

# 97. 最小可實作研究原型

若只做第一個真正實驗，不需要十層全部上。

可以先測：

$$
\boxed{
\text{allocation stability}
\times
\text{task novelty}
\times
\text{reward timing}.
}
$$

每個人重複完成：

- low novelty／delayed reward；
- low novelty／immediate reward；
- high novelty／delayed reward；
- high novelty／immediate reward。

測：

$$
accuracy,
RT,
RTV,
switches,
confidence,
subjective clarity.
$$

這已經可以同時測 Paper 3、4、6、9 的一部分命題。

---

# 98. 第二個最小實驗：Sparse vs Scaffolded Completion

比較：

$$
I_{\mathrm{sparse}}
$$

與：

$$
I_{\mathrm{scaffolded}}.
$$

測：

$$
accuracy,
completion\ time,
path\ diversity,
false\ path,
confidence.
$$

若 graph measures 沒有可靠增量，Paper 5 可以直接降級。

---

# 99. 第三個最小實驗：Life-Transition EMA

追蹤進入：

- 大學；
- 新工作；
- 遠距工作；
- 親職；

前後。

測：

$$
q_t,
s_t^{\mathrm{ext}},
k_t,
i_t,
v_t.
$$

直接測 Paper 7，而不是依賴回憶。

---

# 100. 最後的研究順序

本文建議：

$$
\boxed{
\text{先行為}
\rightarrow
\text{再動態}
\rightarrow
\text{再跨診斷}
\rightarrow
\text{再神經}
\rightarrow
\text{再縱向}
\rightarrow
\text{最後臨床預測}.
}
$$

而不是從：

$$
\text{brain scan}
$$

直接跳到：

$$
\text{new ADHD subtype}.
$$

---

# 101. 本系列最需要避免的十五種錯誤

1. 把數學形式當證據；
2. 把 ADHD 當單一機制；
3. 把 dopamine 當 attention；
4. 把 subjective enhancement 當 performance enhancement；
5. 把 hyperfocus 當 ADHD 專屬核心；
6. 把 creativity 當 ADHD 超能力；
7. 把 brain network 當 cognitive graph；
8. 把 adult diagnosis 當 adult onset；
9. 把 compensation 當 absence of impairment；
10. 把 masking 當已成熟 ADHD construct；
11. 把 continuous traits 當 everyone-has-ADHD；
12. 把 subthreshold 當 hidden diagnosis；
13. 把 biotype 當新臨床 subtype；
14. 把 local advantage 當 global advantage；
15. 把 complex model 當 better model。

---

# 102. 十篇系列的最小共同命題

如果把所有內容壓到最小，只剩：

$$
\boxed{
\text{ADHD-related functioning is likely to be
heterogeneous, dynamic, multidimensional,
and context-sensitive}.
}
$$

這句本身與現代 literature 相容。

但本系列真正需要被驗證的是更強版本：

$$
\boxed{
\text{specific dynamic configuration variables
provide incremental predictive value}.
}
$$

---

# 103. 封頂總式

最終候選系統：

$$
\boxed{
\begin{aligned}
\mathbf c_{t+1}
&=
\Phi
\left(
\mathbf c_t,
\mathbf q_t,
\mathbf e_t,
\mathbf s_t^{\mathrm{ext}},
\mathbf k_t,
\mathbf u_t
\right)
+
\boldsymbol\varepsilon_t,
\\
\mathbf p_t
&=
F
\left(
\mathbf c_t,
\mathbf q_t,
\mathbf e_t
\right),
\\
\chi_t
&=
H
\left(
\mathbf c_t,
\mathbf e_t,
\mathbf x_t^{\mathrm{expectancy}}
\right),
\\
\widehat{\mathbf p}_t
&=
M
\left(
\mathbf p_t,
\chi_t,
\mathbf f_t^{\mathrm{feedback}}
\right),
\\
\mathbf i_t
&=
J
\left(
\mathbf p_t,
\mathbf q_t,
\mathbf e_t,
\mathbf s_t^{\mathrm{ext}},
\mathbf k_t
\right),
\\
v_t
&=
V
\left(
\mathbf y_t,
\mathbf i_t,
\Omega_o,
A_t^{\mathrm{care}}
\right),
\\
\mathfrak D_t
&=
\Gamma
\left(
\mathbf y_t,
\mathbf i_t,
H^{\mathrm{dev}},
X_t^{\mathrm{diff}}
\right).
\end{aligned}
}
$$

這不是 ADHD 的已證實方程。

它是整個系列的 research-program compression。

---

# 104. 這套模型如果是錯的，應該怎麼死？

它不應該透過不斷增加自由參數來逃避反證。

最清楚的死亡條件是：

$$
\boxed{
\text{simple models predict just as well or better}.
}
$$

其次是：

$$
\boxed{
\text{new constructs cannot be measured reliably}.
}
$$

再其次：

$$
\boxed{
\text{dynamic／contextual predictions fail to replicate}.
}
$$

如果這三件事發生，IDCT 應被歸檔，而不是繼續擴張。

---

# 105. 這套模型如果是真的，最先會看到什麼？

最先不會是：

> 發現 ADHD 新腦區。

而更可能是：

1. 同一人跨任務 performance variance 很有結構；
2. 配置穩定性比單次平均值更能預測錯誤；
3. subjective clarity 與 objective performance 可穩定脫鉤；
4. context fit 可預測 within-person performance change；
5. 某些 profile 在 matched tasks 出現可重現 sign reversal；
6. 這些變量在 external cohorts 有增量價值。

---

# 106. 系列的理論地位

本系列最合理的目前地位：

$$
\boxed{
\text{pre-empirical integrative computational framework}.
}
$$

不是：

$$
\text{medical theory confirmed},
$$

也不是：

$$
\text{clinical diagnostic framework}.
$$

---

# 107. 系列封頂後的下一步不是再寫更多理論篇

若此系列要繼續，優先順序應從：

$$
\text{theory generation}
$$

切換為：

$$
\boxed{
\text{measurement design}
\rightarrow
\text{pilot protocol}
\rightarrow
\text{preregistered validation}.
}
$$

也就是停止繼續堆疊新名詞。

---

# 108. 結論

本系列從一個很簡單的懷疑開始：

$$
\text{ADHD}
\neq
\text{just too little attention}.
$$

十篇之後，這個懷疑被拆成一套更嚴格、也更容易被打假的研究架構。

目前的外部研究支持：

- ADHD 是高度異質的神經發展障礙；
- symptoms 與 genetic liability 具有明顯連續性；
- continuous variation 與 local biotypes 可以共存；
- stimulant mechanisms 涉及 dopamine、norepinephrine、arousal、reward 與 network dynamics，而非單一 attention gain；
- trial-to-trial neural stability 與 network flexibility 值得作為獨立變量；
- adult ADHD diagnosis、impairment、late onset、emotional dysregulation、objective measures 仍有大量重要未解問題。

但這些證據**尚未證明**：

- allocation entropy；
- attention debt；
- cognitive graph topology；
- disengagement barrier；
- reversal surface；
- global fit kernel；

是 ADHD 的真實機制。

這些都是本系列交給未來實驗的東西。

因此封頂篇不以：

> 我們已經解釋 ADHD。

作結。

而以：

$$
\boxed{
\text{Can these constructs survive measurement,
replication, prediction, and falsification?}
}
$$

作結。

如果不能：

$$
\boxed{
\text{discard them}.
}
$$

如果能：

$$
\boxed{
\text{keep only the parts that survive}.
}
$$

這才是本系列最終的科學立場。

---

# 參考文獻

1. World Health Organization. *Clinical descriptions and diagnostic requirements for ICD-11 mental, behavioural and neurodevelopmental disorders (CDDR).* WHO. Current ICD-11 framework accessed 2026-08-17.

2. World Health Organization. *ICD-11 2026 Release.* WHO, 16 February 2026.

3. Cortese, S., Bellgrove, M. A., Brikell, I., Franke, B., Goodman, D. W., Hartman, C. A., et al. Attention-deficit/hyperactivity disorder (ADHD) in adults: evidence base, uncertainties and controversies. *World Psychiatry*. 2025;24(3):347–371. DOI: 10.1002/wps.21374.

4. Pan, N., Long, Y., Qin, K., et al. Mapping ADHD Heterogeneity and Biotypes by Topological Deviations in Morphometric Similarity Networks. *JAMA Psychiatry*. 2026;83(5):478–490. DOI: 10.1001/jamapsychiatry.2026.0001.

5. van der Laan, C. M., Ip, H. F., Schipper, M., et al. Genome-wide association meta-analysis of childhood ADHD symptoms and diagnosis identifies new loci and potential effector genes. *Nature Genetics*. 2025;57:2427–2435. DOI: 10.1038/s41588-025-02295-y.

6. Kay, B. P., Wheelock, M. D., Siegel, J. S., et al. Stimulant medications affect arousal and reward, not attention networks. *Cell*. 2025. DOI: 10.1016/j.cell.2025.11.039.

7. Oya, M., Matsuoka, K., Kubota, M., et al. Effects of Extended-Release Methylphenidate on Dopamine and Norepinephrine Transporters in Adults With Attention-Deficit/Hyperactivity Disorder: A Longitudinal Dual-Tracer PET Study. *Psychiatry and Clinical Neurosciences*. 2026;80(1):48–54. DOI: 10.1111/pcn.13911.

8. Gao, Z., et al. Reduced temporal and spatial stability of neural activity patterns predict cognitive control deficits in children with ADHD. *Nature Communications*. 2025;16:2346. DOI: 10.1038/s41467-025-57685-x.

9. Nugiel, T., et al. Methylphenidate stabilizes dynamic brain network organization during tasks probing attention and reward processing in stimulant-naïve children with ADHD. *Translational Psychiatry*. 2025;15:488. DOI: 10.1038/s41398-025-03694-9.

10. Atkinson, A. L., Pinheiro Sanchez, B., Warburton, M., Allmark, H., & Allen, R. J. The Ability to Direct Attention in Working Memory Is Not Impaired in Adults With Symptoms of ADHD. *Journal of Attention Disorders*. 2025;29(9):684–705. DOI: 10.1177/10870547251330039.

11. Hupfeld, K. E., Osborne, J. B., Tran, Q. T., Hyatt, H. W., Abagis, T. R., et al. Validation of the dispositional adult hyperfocus questionnaire (AHQ-D). *Scientific Reports*. 2024;14:19460. DOI: 10.1038/s41598-024-70028-y.

12. Elsholz, L., et al. ADHD symptomatology and metacognitive monitoring insights for college student support. *Current Psychology*. 2026. DOI: 10.1007/s12144-026-09164-9.

13. Kang, S., Fu, Z., Li, Q., Yang, L., & Cao, Q. Adult-diagnosed and childhood-diagnosed attention deficit/hyperactivity disorder: cognitive and environmental contributions to symptom severity across different age of diagnosis. *Frontiers in Psychiatry*. 2026;17:1782999. DOI: 10.3389/fpsyt.2026.1782999.

14. Bayard, S., Madiouni, C., Radiguer, F., Roulin, M., & Henrard, S. Late-Onset ADHD symptoms in the general population: A scoping review of longitudinal trajectories in population-based cohorts. *The European Journal of Psychiatry*. 2026;40(1):100337. DOI: 10.1016/j.ejpsy.2025.100337.

15. Rafael, R. B., Jia, H., Rouel, M., Wootton, B. M., & Mitchison, D. Attention Deficit/Hyperactivity Disorder (ADHD)-Related Strengths in Adults: A Scoping Review. *Journal of Attention Disorders*. 2026. DOI: 10.1177/10870547261425737.

16. Arildskov, T. W., Thomsen, P. H., Sonuga-Barke, E. J. S., Lambek, R., Østergaard, S. D., & Virring, A. Is Attention-Deficit/Hyperactivity Disorder (ADHD) a Dimension or a Category? What Does the Relationship Between ADHD Traits and Psychosocial Quality of Life Tell Us? *Journal of Attention Disorders*. 2024;28(7):1035–1044. DOI: 10.1177/10870547231222228.

17. Faraone, S. V., et al. Attention-deficit/hyperactivity disorder. *Nature Reviews Disease Primers*. 2024;10:11. DOI: 10.1038/s41572-024-00495-0.

18. Schork, A. J., et al. Polygenic profiles define aspects of clinical heterogeneity in attention deficit hyperactivity disorder. *Nature Genetics*. 2024;56:234–244. DOI: 10.1038/s41588-023-01593-7.

---

# 文獻使用聲明

本文僅使用上述研究建立截至 2026-08-17 的外部實證邊界。

本文提出的 IDCT-ADHD、全域 configuration state $\mathbf c_t$ 、allocation entropy、disengagement barrier、attention debt、cognitive path topology、global fit kernel、reversal surface 與十八項統一命題，均為本系列理論構件，不應被誤認為上述研究作者的原始結論。

本篇也不把兒童、成人、healthy-control pharmacology、genetics、neuroimaging、self-report、clinical review 與 workplace research 視為可直接相加的單一證據池。不同研究只支持不同層級的局部背景。

---

# 系列封頂狀態

**系列狀態：** 10／10 完成  
**本篇狀態：** v1.0 封頂理論稿  
**新增原始臨床／人體數據：** 無  
**醫學用途：** 無  
**下一階段：** Measurement Design／Pilot Protocol／Preregistered Validation  
