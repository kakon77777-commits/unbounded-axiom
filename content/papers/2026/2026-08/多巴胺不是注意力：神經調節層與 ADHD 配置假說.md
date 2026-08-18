# 多巴胺不是注意力：神經調節層與 ADHD 配置假說

**英文題名：** Dopamine Is Not Attention: A Neuromodulatory Layer Hypothesis for ADHD Configuration  
**系列：** ADHD 動態配置與認知拓撲系列，第 2 篇  
**版本：** v0.1  
**日期：** 2026-08-16  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論建模／認知神經科學命題／研究綱領  
**文獻檢索截點：** 2026-08-16  

---

# 0. 醫學、藥理與證據邊界聲明

本文不是臨床研究、藥理試驗、診斷工具、治療指南或用藥建議。

本文提出的「神經調節層」「配置參數」「狀態重參數化」「神經調節—配置映射」等概念均屬待驗證命題，不代表已被醫學界確認的 ADHD 病理機制。

原作者並非醫學、精神醫學、藥理學或臨床心理專業研究者。本文不提供新的人體、臨床、藥物、影像或生化實驗數據；所有實證性背景均來自公開同行評審研究。本文新增內容僅屬跨研究整合、形式化與可證偽假說。

本文不使用原作者的個人用藥經驗作為一般化證據，也不提供任何自行調整藥物、停藥、加藥、混合藥物或改變治療方式的建議。

本文的核心目的，是研究一個概念問題：

$$
\boxed{
\text{dopaminergic modulation}
\neq
\text{attention itself}.
}
$$

---

# 摘要

ADHD 與 dopamine、norepinephrine 及刺激劑治療之間具有長期且重要的研究關係，但「ADHD 是多巴胺不足」「刺激劑增加多巴胺，所以注意力增加」這類一維敘述已不足以容納目前的神經影像、PET、藥物反應與網路動力學資料。

2026 年發表的成人 ADHD longitudinal dual-tracer PET 研究顯示，extended-release methylphenidate 可同時降低 dopamine transporter 與 norepinephrine transporter 的 tracer binding，並伴隨部分認知改善；然而 transporter binding 的變化量並未與認知改善形成直接相關。2025 年 PNAS 的 PET/fMRI 研究亦顯示，methylphenidate 所引起的注意改善並不能簡單由 dopamine 增加幅度預測，而與個體基線 D1-to-D2/3 receptor availability ratio 有關。2025 年 Cell 研究則將 stimulant-related functional connectivity differences 更多地連接至 arousal、reward、sensorimotor 與 salience-related systems，而非單一 canonical attention network。另有 2025 年 ADHD 兒童研究顯示，methylphenidate 可降低 whole-brain flexibility，且部分網路穩定化與較低反應時間變異及較高任務表現相關。2025 年底發表、列入 2026 年 Nature Communications 卷期的 PET/fMRI 研究進一步顯示，methylphenidate 可壓縮 cortical principal gradient，改變大尺度功能層級與跨網路整合。

基於此，本文提出「Neuromodulatory Configuration Layer Hypothesis, NCLH」：dopamine 與 norepinephrine 不應在中層認知模型中被直接等同於注意力，而應被視為可改變 arousal、salience、reward valuation、action vigor、gating、stability、switching threshold 及 network integration 等參數的上游調節因子。

本文提出：

$$
\mathbf C_{t+1}
=
\Phi
\left(
\mathbf C_t,
\mathbf U_t,
\mathbf N_t,
\mathbf E_t
\right),
$$

其中 $\mathbf N_t$ 為 neuromodulatory state，而不是 attention variable 本身。

更進一步：

$$
\Delta \mathbf N_t
\not\Rightarrow
\Delta P_t > 0,
$$

因為客觀性能 $P_t$ 還受任務、基線狀態、工作記憶、控制穩定性、動機、學習史與環境耦合所決定。

本文的目標不是否定 dopamine model，而是將其由「單一病因敘事」降階為「動態配置系統的上游調節層」，使其能與 ADHD 的異質性、情境依賴性、個體藥物反應差異及腦網路動力學共存。

**關鍵詞：** ADHD、dopamine、norepinephrine、methylphenidate、neuromodulation、arousal、reward、salience、network dynamics、配置動力學、PET、fMRI

---

# 1. 問題：多巴胺模型真正需要修正的是哪一層？

本文不採取：

$$
\text{dopamine hypothesis}
=
\text{wrong}.
$$

相反地，現有藥理與 PET 證據持續顯示 catecholaminergic systems 與 ADHD 治療具有重要關係。

真正需要避免的是：

$$
\text{dopamine}
=
\text{attention}.
$$

以及：

$$
\text{dopamine increase}
\Rightarrow
\text{global cognitive enhancement}.
$$

這兩個等號與單向推出都過強。

因此本文首先建立三層分離：

$$
\boxed{
\text{Neuromodulation}
\neq
\text{Cognitive allocation}
\neq
\text{Behavioral performance}.
}
$$

其中：

- neuromodulation 是神經系統狀態調節；
- cognitive allocation 是有限處理資源如何配置；
- behavioral performance 是在特定任務上的可測輸出。

它們可以相關，但不能互換。

---

# 2. 為什麼不能把 dopamine 簡化為「注意力燃料」？

## 2.1 Dopamine 具有多功能性

dopaminergic signaling 參與的功能遠不止注意。

已有研究長期涉及：

- reinforcement learning；
- reward prediction；
- motivation；
- action selection；
- vigor；
- motor control；
- working memory；
- cognitive flexibility；
- salience-related processing；
- network integration。

因此：

$$
D_t
$$

如果被直接命名為「注意力量」，會把不同機制壓縮成單一標量。

本文改用：

$$
D_t
=
\text{dopaminergic modulatory state}.
$$

它不是 performance，也不是 attention score。

---

# 3. Norepinephrine 不能被從 stimulant model 中刪掉

methylphenidate 並不是單純的 dopamine-only perturbation。

成人 ADHD 的 2026 longitudinal dual-tracer PET 研究同時測量 DAT 與 NET。研究在治療穩定後觀察到 striatal DAT binding 與 thalamic／pontine NET binding 的下降，顯示 methylphenidate 同時影響 dopamine 與 norepinephrine transport systems。

因此若寫成：

$$
\text{MPH}
\rightarrow
D
\rightarrow
\text{attention},
$$

模型會遺漏：

$$
\text{MPH}
\rightarrow
(D,NE)
\rightarrow
\text{distributed state changes}.
$$

本文因此定義：

$$
\mathbf N_t
=
\left(
D_t,
NE_t,
\ldots
\right),
$$

其中 $\mathbf N_t$ 是神經調節狀態向量。

這個向量未來可以加入其他有實證理由的調節系統，但本文不預先宣稱其完整性。

---

# 4. Transporter occupancy 不等於 cognitive gain

2026 成人 ADHD dual-tracer PET 研究提供一個重要限制：

治療後可觀察到 DAT 與 NET binding 的改變，也可觀察到注意與 multitasking 等認知指標改善，但 transporter binding 的變化量與認知改善並沒有形成簡單的一對一關係。

因此不能寫成：

$$
\Delta DAT
\propto
\Delta P.
$$

也不能寫成：

$$
\Delta NET
\propto
\Delta P.
$$

更合理的候選關係是：

$$
\Delta \mathbf N
\rightarrow
\Delta \mathbf C
\rightarrow
\Delta P,
$$

而中間存在：

- baseline receptor state；
- network organization；
- task properties；
- compensatory mechanisms；
- individual variability；
- nonlinear response。

這正是本文所稱的「中介配置層」。

---

# 5. 個體基線比單純 dopamine 增幅更重要

2025 年 PNAS 的 PET/fMRI 研究在健康成人中發現，methylphenidate 引起的注意改善與個體基線 D1-to-D2/3 receptor availability ratio 有關，而不是由 striatal dopamine increase 的幅度單獨決定。

這項研究不能直接等同 ADHD 臨床機制，因為其研究對象為健康成人。

但它提供一個重要一般原理：

$$
\boxed{
\text{same perturbation}
+
\text{different baseline}
\Rightarrow
\text{different outcome}.
}
$$

因此本文加入基線條件：

$$
\Delta P_i
=
F
\left(
\Delta \mathbf N_i,
\mathbf B_i,
\mathbf T_i
\right),
$$

其中 $\mathbf B_i$ 是個體 baseline neurocognitive state。

---

# 6. 非線性工作區命題

若神經調節存在最佳工作區，則性能函數不應預設單調。

最簡化的候選形式可以寫成：

$$
P(D)
=
P_{\max}
-
\alpha
\left(
D-D^{*}
\right)^2.
$$

這不是對真實 dopamine-performance curve 的宣稱，而是一個用於表示「可能存在最佳工作區」的最小候選函數。

如果：

$$
D<D^{*},
$$

適度增加 $D$ 可能改善性能。

如果：

$$
D\approx D^{*},
$$

相同增加可能影響很小。

如果：

$$
D>D^{*},
$$

持續增加甚至可能降低某些控制功能。

因此：

$$
\boxed{
\text{more neuromodulation}
\neq
\text{more cognition}.
}
$$

---

# 7. Arousal 與 reward 是獨立的重要中介層

2025 年 Cell 的 stimulant functional-connectivity 研究使用大型 ABCD cohort，並以高度密集的 methylphenidate precision-imaging experiment 驗證部分結果。該研究報告 stimulant-related differences 更接近 wakefulness／arousal、reward、sensorimotor 與 salience-related organization，而不是簡單集中於 canonical dorsal attention network。

因此本文提出：

$$
\mathbf Z_t
=
\left(
A_t,
R_t,
S_t,
V_t
\right),
$$

其中：

- $A_t$：arousal；
- $R_t$：reward valuation；
- $S_t$：salience weighting；
- $V_t$：action vigor／engagement propensity。

再令：

$$
\mathbf Z_t
=
\Psi
\left(
\mathbf N_t,
\mathbf E_t,
\mathbf T_t
\right).
$$

此時 stimulant effect 的候選因果鏈不再是：

$$
\text{drug}
\rightarrow
\text{attention}
\rightarrow
\text{performance},
$$

而是：

$$
\boxed{
\text{drug}
\rightarrow
\mathbf N_t
\rightarrow
\mathbf Z_t
\rightarrow
\mathbf C_t
\rightarrow
P_t.
}
$$

這條鏈每一個箭頭都需要實證檢驗。

---

# 8. 「主觀清晰」不必然等於 objective performance

如果 arousal、salience 與 engagement propensity 改變，主體可能感受到：

$$
Q_t^{\text{subj}}
\uparrow,
$$

其中 $Q_t^{\text{subj}}$ 表示主觀清晰度、鮮明度、投入感或「狀態變好」的感受。

但：

$$
Q_t^{\text{subj}}
\uparrow
\not\Rightarrow
P_t
\uparrow.
$$

因此本文再區分：

$$
\boxed{
\text{Subjective state}
\neq
\text{Metacognitive confidence}
\neq
\text{Objective performance}.
}
$$

這一問題將在本系列第 6 篇獨立展開。

本文只指出：如果 stimulant effects 具有 arousal／reward／salience 成分，就必須允許「狀態感改變」與「性能改變」不同步。

---

# 9. Network stability：藥效可能表現在變異下降，而不是平均值增加

2025 年 stimulant-naive ADHD 兒童的 double-blind single-dose study 在 standard 與 rewarded go/no-go tasks 中發現：

- methylphenidate 改善部分 task performance；
- whole-brain flexibility 下降；
- flexibility 降幅與 reaction-time variability 降幅相關；
- rewarded condition 中，flexibility 降幅亦與較高 d-prime 改善相關。

因此，一個重要候選機制不是：

$$
\text{attention magnitude}
\uparrow,
$$

而是：

$$
\boxed{
\text{state stability}
\uparrow.
}
$$

或：

$$
\boxed{
\text{unproductive state switching}
\downarrow.
}
$$

因此配置模型必須同時具有：

$$
\mathbb E
\left[
\mathbf C_t
\right]
$$

與：

$$
\operatorname{Var}
\left[
\mathbf C_t
\right].
$$

平均配置與配置變異不能互相替代。

---

# 10. ADHD 本身也出現神經穩定性證據

2025 年 Nature Communications 的兒童 ADHD cognitive-control study 使用 single-trial neural decoding 與 representational similarity analysis，發現 ADHD 組在 salience 與 frontoparietal networks 中呈現較高 temporal variability 與較低 spatial stability，且部分 neural variability 與行為波動及臨床症狀相關。

特別重要的是，研究在若干任務條件中沒有發現平均 task-evoked activation 的顯著組間差異，但在 trial-wise variability 與 spatial stability 上出現差異。

這提示：

$$
\boxed{
\text{mean neural activation}
\approx
\text{similar}
}
$$

仍可以同時存在：

$$
\boxed{
\text{neural variability}
\neq
\text{similar}.
}
$$

這對 ADHD 動態配置模型具有直接方法論意義：

> 平均值可能不是唯一關鍵統計量。

---

# 11. Cortical hierarchy 可以被 neuromodulation 重新組織

2025 年底發表、刊載於 Nature Communications 2026 卷期的 PET/fMRI 研究，在兩組 double-blind placebo-controlled healthy-adult experiments 中觀察到 methylphenidate 壓縮 principal cortical gradient。

亦即：

$$
\text{sensory-association segregation}
\downarrow.
$$

其中 inferior parietal cortex 的 gradient compression 與 attention improvement 相關。

這不能直接證明 ADHD 的「網狀認知拓撲」。

但它證明一個更弱、且對本文足夠的重要命題：

$$
\boxed{
\text{neuromodulatory perturbation}
\rightarrow
\text{large-scale functional reorganization}.
}
$$

因此 dopamine 不只可以被理解為某個局部訊號的「量」。

它也可能透過 receptor distribution 與 network coupling 改變整體功能組織方式。

---

# 12. 神經調節層的最小形式化

本文定義神經調節狀態：

$$
\mathbf N_t
=
\left(
D_t,
NE_t
\right).
$$

定義中介狀態：

$$
\mathbf Z_t
=
\left(
A_t,
R_t,
S_t,
V_t,
G_t,
F_t
\right),
$$

其中：

- $A_t$：arousal；
- $R_t$：reward valuation；
- $S_t$：salience；
- $V_t$：vigor／engagement；
- $G_t$：gating；
- $F_t$：flexibility-stability balance。

則：

$$
\mathbf Z_t
=
\Psi
\left(
\mathbf N_t,
\mathbf B,
\mathbf T_t,
\mathbf E_t
\right).
$$

再由：

$$
\mathbf C_{t+1}
=
\Phi
\left(
\mathbf C_t,
\mathbf Z_t,
\mathbf T_t,
\mathbf E_t
\right).
$$

最後：

$$
P_t
=
\Gamma
\left(
\mathbf C_t,
\mathbf T_t,
\mathbf W_t
\right),
$$

其中 $\mathbf W_t$ 包含工作記憶、學習史、疲勞、睡眠與其他未建模條件。

完整候選鏈：

$$
\boxed{
\mathbf N_t
\rightarrow
\mathbf Z_t
\rightarrow
\mathbf C_t
\rightarrow
P_t.
}
$$

---

# 13. Neuromodulatory gain matrix

若不同神經調節狀態對不同配置參數影響不同，可以引入：

$$
\mathbf G_t^{N}
=
\frac{
\partial \mathbf Z_t
}{
\partial \mathbf N_t
}.
$$

例如：

$$
\mathbf G_t^{N}
=
\begin{bmatrix}
\frac{\partial A}{\partial D} &
\frac{\partial A}{\partial NE}
\\
\frac{\partial R}{\partial D} &
\frac{\partial R}{\partial NE}
\\
\frac{\partial S}{\partial D} &
\frac{\partial S}{\partial NE}
\\
\frac{\partial V}{\partial D} &
\frac{\partial V}{\partial NE}
\\
\frac{\partial G}{\partial D} &
\frac{\partial G}{\partial NE}
\\
\frac{\partial F}{\partial D} &
\frac{\partial F}{\partial NE}
\end{bmatrix}.
$$

本文不提供其數值。

它只是明確表示：

$$
\text{one neurotransmitter}
\rightarrow
\text{many cognitive parameters}.
$$

以及：

$$
\text{one cognitive parameter}
\leftarrow
\text{multiple neuromodulators}.
$$

因此：

$$
\boxed{
\text{many-to-many mapping}
}
$$

比一對一映射更適合作為候選模型。

---

# 14. Baseline-dependent response surface

令：

$$
\mathbf B_i
$$

表示個體 $i$ 的 baseline state。

藥物擾動為：

$$
\Delta \mathbf N_i.
$$

則：

$$
\Delta \mathbf Z_i
=
\Psi
\left(
\mathbf B_i,
\Delta \mathbf N_i
\right).
$$

因此：

$$
\Delta \mathbf N_i
=
\Delta \mathbf N_j
$$

並不能推出：

$$
\Delta \mathbf Z_i
=
\Delta \mathbf Z_j.
$$

更不能推出：

$$
\Delta P_i
=
\Delta P_j.
$$

這提供一個自然方式描述：

- responder；
- partial responder；
- non-responder；
- adverse cognitive response。

但本文不主張這四種是固定生物型。

---

# 15. 配置重參數化，而不是「能力值加成」

本文提出一個新的描述語言：

$$
\boxed{
\text{State Reparameterization}
}
$$

藥物不是直接把：

$$
P_t
$$

加上一個常數：

$$
P_t'
=
P_t+c.
$$

更合理的候選模型是：

$$
\Theta_t
\rightarrow
\Theta_t',
$$

其中 $\Theta_t$ 是整個系統的參數集合，例如：

$$
\Theta_t
=
\left(
\alpha_t,
\beta_t,
\gamma_t,
\delta_t,
\lambda_t,
\kappa_t,
\tau_t
\right).
$$

於是：

$$
\pi_t(e_i)
=
\operatorname{softmax}
\left(
s_t(e_i);
\Theta_t
\right)
$$

在神經調節改變後變成：

$$
\pi_t'(e_i)
=
\operatorname{softmax}
\left(
s_t(e_i);
\Theta_t'
\right).
$$

所以真正改變的可能是：

- 哪些事件變得更顯著；
- 哪些目標更容易維持；
- 哪些回饋更具吸引力；
- 切換門檻如何改變；
- 資源是否較穩定；
- 競爭項目是否被抑制；
- 網路是否更整合或更分離。

這就是「配置重參數化」。

---

# 16. 為什麼這個模型比 dopamine-deficit slogan 更強？

因為它可以容納下列現象：

## 16.1 同一藥物不同人效果不同

$$
\mathbf B_i
\neq
\mathbf B_j.
$$

## 16.2 同一人不同任務效果不同

$$
\mathbf T_a
\neq
\mathbf T_b.
$$

## 16.3 主觀狀態改善但特定績效不變

$$
Q^{\text{subj}}
\uparrow,
\qquad
P
\approx
\text{constant}.
$$

## 16.4 反應時間穩定化但平均能力未全面增加

$$
\operatorname{Var}(RT)
\downarrow
$$

可以與：

$$
\mathbb E(P)
\approx
\text{small change}
$$

並存。

## 16.5 網路拓撲改變但不能還原為單一 neurotransmitter quantity

$$
\Delta \text{network organization}
=
F
\left(
D,
NE,
\text{receptors},
\text{baseline},
\text{task}
\right).
$$

---

# 17. 本文與「低 dopamine ADHD」說法的關係

本文不主張：

$$
\text{ADHD has normal dopamine in all cases}.
$$

也不主張：

$$
\text{dopamine is irrelevant}.
$$

本文只拒絕：

$$
\boxed{
\text{ADHD}
=
\text{one-dimensional dopamine deficiency}.
}
$$

更合理的研究問題是：

$$
\boxed{
\text{Which neuromodulatory configurations,
in which circuits,
at which developmental stages,
under which tasks,
produce which cognitive states?}
}
$$

這是一個條件化問題，而不是單值問題。

---

# 18. 六項核心命題

## N1：非等同性命題

$$
\text{dopamine}
\neq
\text{attention}.
$$

若未來證據顯示單一 dopamine quantity 可以近乎完整、穩定地預測 ADHD attention state，則 N1 應被削弱。

---

## N2：多調節命題

ADHD stimulant response 應至少允許 dopamine 與 norepinephrine 的共同作用：

$$
\mathbf N_t
=
(D_t,NE_t,\ldots).
$$

若大型研究反覆顯示 NE modulation 對核心現象無增量作用，則模型應簡化。

---

## N3：基線依賴命題

$$
\Delta P_i
=
F
\left(
\Delta \mathbf N_i,
\mathbf B_i
\right).
$$

若相同 pharmacological perturbation 對不同 baseline individuals 的反應高度一致，則此命題應被削弱。

---

## N4：中介狀態命題

藥理效果部分透過：

$$
\mathbf Z_t
=
(A,R,S,V,G,F)
$$

等狀態中介。

若 arousal、reward、salience、stability 等變量完全不能介導 stimulant-related behavioral change，則 N4 應被削弱。

---

## N5：變異優先命題

部分 ADHD-related dysfunction 與 treatment response 可能更敏感於：

$$
\operatorname{Var}
\left(
\mathbf C_t
\right)
$$

而非只對：

$$
\mathbb E
\left[
\mathbf C_t
\right].
$$

若 trial-wise variability 與 network stability 沒有任何增量預測力，則此命題失敗。

---

## N6：重參數化命題

stimulant effect 更適合描述為：

$$
\Theta
\rightarrow
\Theta'
$$

而非：

$$
P
\rightarrow
P+c.
$$

若跨任務效應可被單一固定能力增益常數準確描述，則 N6 應被放棄。

---

# 19. 可證偽實驗設計

## 19.1 同一受試者、多任務、藥物交叉設計

在 placebo 與 clinically supervised medication condition 下，測量：

- sustained attention；
- working memory；
- response inhibition；
- reward sensitivity；
- low-reward persistence；
- high-novelty exploration；
- task switching。

如果藥物只是 global cognitive enhancer，則應看到近似同方向增益。

如果 NCLH 較接近真實，則應看到：

$$
\Delta P(T_1)
\neq
\Delta P(T_2).
$$

---

## 19.2 PET + fMRI + behavior

同時估計：

$$
\Delta DAT,
\qquad
\Delta NET,
\qquad
\Delta \text{network state},
\qquad
\Delta P.
$$

比較模型：

$$
M_1:
\Delta DAT
\rightarrow
\Delta P
$$

與：

$$
M_2:
(\Delta DAT,\Delta NET)
\rightarrow
\Delta \text{network}
\rightarrow
\Delta P.
$$

若 $M_1$ 在 out-of-sample prediction 中不劣於 $M_2$，中介配置模型就沒有必要複雜化。

---

## 19.3 主觀—客觀分離測試

同步測量：

$$
Q_t^{\text{subj}}
$$

與：

$$
P_t^{\text{obj}}.
$$

檢查：

$$
\operatorname{Corr}
\left(
\Delta Q^{\text{subj}},
\Delta P^{\text{obj}}
\right).
$$

若兩者近乎完全同步，則主觀／客觀分離的重要性下降。

若兩者經常脫鉤，則必須保留兩個變量。

---

## 19.4 時間解析研究

以高時間解析度測量：

$$
\mathbf C_t
$$

的狀態轉移。

比較：

$$
\text{mean state}
$$

與：

$$
\text{transition matrix}.
$$

例如：

$$
\mathbf M_{ab}
=
P
\left(
C_{t+1}=b
\mid
C_t=a
\right).
$$

若 ADHD-related differences 主要出現在 $\mathbf M$ 而非 mean state，將直接支持 dynamic-configuration view。

---

# 20. 重要限制

## 20.1 健康成人研究不能直接等同 ADHD

部分 PET/fMRI methylphenidate studies 使用 healthy adults。

因此：

$$
\text{mechanistic pharmacology in controls}
\neq
\text{ADHD pathophysiology}.
$$

它們只能提供候選機制。

---

## 20.2 兒童研究不能直接外推成人 ADHD

發展階段會改變：

- receptor expression；
- cortical maturation；
- compensation；
- environmental demand；
- medication history。

所以：

$$
\text{child ADHD}
\neq
\text{adult ADHD}
$$

在機制上不能預設完全相同。

---

## 20.3 BOLD 不等於 neurotransmitter

fMRI functional connectivity 是間接血氧訊號。

因此：

$$
\Delta \text{BOLD}
\neq
\Delta D
$$

以及：

$$
\Delta \text{BOLD}
\neq
\Delta NE.
$$

必須透過 PET、藥理操弄或其他方法建立更強因果鏈。

---

## 20.4 PET binding change 也不是完整 neurotransmission

transporter／receptor tracer binding 是可操作化指標。

它不等於完整：

$$
\text{release}
+
\text{reuptake}
+
\text{receptor signaling}
+
\text{downstream network effect}.
$$

所以本文不把 PET 數值本體化為「真正 dopamine 量」。

---

# 21. 本文不主張的內容

本文不主張：

1. dopamine 與 ADHD 無關；
2. norepinephrine 才是唯一真正機制；
3. methylphenidate 只作用於 reward；
4. stimulant 不會改善 attention tasks；
5. dopamine receptor ratio 已可作臨床 biomarker；
6. cortical gradient compression 等於 ADHD 被矯正；
7. brain stability 越高越好；
8. flexibility 越低越好；
9. 所有人都有相同最佳 dopamine level；
10. 神經調節可以完整解釋 ADHD；
11. 本文模型可用來預測個人用藥；
12. 本文提供任何醫療操作建議。

核心限制仍是：

$$
\boxed{
\text{mechanistic plausibility}
\neq
\text{clinical validation}.
}
$$

---

# 22. 與第 1 篇 ADCC 的整合

第 1 篇定義：

$$
\mathbf C_{i,t}
=
\text{dynamic cognitive configuration}.
$$

本文補上其上游：

$$
\mathbf N_{i,t}
=
\text{neuromodulatory state}.
$$

因此目前系列主幹變成：

$$
\boxed{
\mathbf N_t
\rightarrow
\mathbf Z_t
\rightarrow
\mathbf C_t
\rightarrow
P_t
\rightarrow
\mathbf Y_t.
}
$$

其中：

- $\mathbf N_t$：神經調節；
- $\mathbf Z_t$：arousal／reward／salience／gating／stability；
- $\mathbf C_t$：認知配置；
- $P_t$：任務性能；
- $\mathbf Y_t$：可觀察表型。

這條鏈不是已證實定律。

它是本系列接下來逐層拆解的候選架構。

---

# 23. 結論

本文真正要改寫的不是 dopamine science，而是語義。

錯誤的簡化是：

$$
\text{dopamine}
=
\text{attention fuel}.
$$

本文提出的替代語言是：

$$
\boxed{
\text{dopamine and norepinephrine}
=
\text{upstream neuromodulatory variables
that reshape cognitive state parameters}.
}
$$

因此：

$$
\Delta D
>0
$$

不能單獨推出：

$$
\Delta P
>0.
$$

更合理的是：

$$
\boxed{
\Delta \mathbf N
\rightarrow
\Delta \Theta
\rightarrow
\Delta \mathbf C
\rightarrow
\Delta P,
}
$$

其中每一層都受 baseline、task、environment 與 development 調節。

這個模型自然容納：

- 藥物有效但不同任務改善幅度不同；
- 同一藥物不同人反應不同；
- 生化 target engagement 與 cognitive improvement 不一對一；
- 主觀狀態改變與客觀性能可能脫鉤；
- network stability 與 trial-wise variability 可能比平均 activation 更有信息；
- neuromodulation 可以重新組織大尺度功能網路，而不是單純「把注意力調高」。

本文因此提出最終研究問題：

$$
\boxed{
\text{Does neuromodulation improve cognition by adding capacity,
or by moving a dynamic system into a more task-compatible state?}
}
$$

如果未來研究支持前者，NCLH 應被簡化。

如果後者具有更高的跨任務、跨個體與 out-of-sample 解釋力，那麼「配置重參數化」可能比「注意力加成」更適合作為 ADHD stimulant mechanism 的中層描述。

---

# 參考文獻

1. Oya, M., Matsuoka, K., Kubota, M., et al. Effects of Extended-Release Methylphenidate on Dopamine and Norepinephrine Transporters in Adults With Attention-Deficit/Hyperactivity Disorder: A Longitudinal Dual-Tracer PET Study. *Psychiatry and Clinical Neurosciences*. 2026;80(1):48-54. DOI: 10.1111/pcn.13911.

2. Manza, P., Tomasi, D., Demiral, S. B., et al. Neural basis for individual differences in the attention-enhancing effects of methylphenidate. *Proceedings of the National Academy of Sciences of the United States of America*. 2025;122(13):e2423785122. DOI: 10.1073/pnas.2423785122.

3. Kay, B. P., Wheelock, M. D., Siegel, J. S., et al. Stimulant medications affect arousal and reward, not attention networks. *Cell*. 2025. DOI: 10.1016/j.cell.2025.11.039.

4. Nugiel, T., et al. Methylphenidate stabilizes dynamic brain network organization during tasks probing attention and reward processing in stimulant-naïve children with ADHD. *Translational Psychiatry*. 2025. DOI: 10.1038/s41398-025-03694-9.

5. Tomasi, D., Manza, P., Demiral, S. B., et al. Methylphenidate reorganizes cortical hierarchy through dopaminergic modulation. *Nature Communications*. Published 13 December 2025; volume 17, article 791 (2026). DOI: 10.1038/s41467-025-67477-y.

6. Gao, Z., et al. Reduced temporal and spatial stability of neural activity patterns predict cognitive control deficits in children with ADHD. *Nature Communications*. 2025. DOI: 10.1038/s41467-025-57685-x.

7. Pretzsch, C. M., Parlatini, V., & Murphy, D. Single-dose methylphenidate induces shift in functional connectivity associated with positive longer term clinical response in adult attention-deficit/hyperactivity disorder. *Scientific Reports*. 2025;15:5794. DOI: 10.1038/s41598-025-87204-3.

---

# 文獻使用聲明

本文只將上述研究用作外部實證邊界。

本文提出的 NCLH、neuromodulatory configuration layer、state reparameterization、neuromodulatory gain matrix 與 $\mathbf N_t \rightarrow \mathbf Z_t \rightarrow \mathbf C_t \rightarrow P_t$ 鏈條，均為本文的理論構件，不應被誤認為上述研究作者的原始結論。

不同研究的樣本包含 ADHD 成人、ADHD 兒童及健康成人；藥物劑量、任務、PET tracer、fMRI 方法與研究目的均不同，不能把它們視為單一大型實驗直接相加。

---

**狀態：** v0.1，理論稿  
**原始臨床／人體資料：** 無  
**醫學用途：** 無  
**下一篇：** 《選擇配置動力學：顯著性、激活、注意與更新的分離》
