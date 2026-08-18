# 補充論文 S4：超專注是能力的一部分嗎？——從 Hyperfocus 因果角色到可控注意力工程

**英文題名：** Is Hyperfocus Part of Capability? From Causal Roles of Hyperfocus to Controllable Attention Engineering  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論建模／因果假說／未來研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 0. 邊界聲明

本文不是醫療建議，不建議任何人自行使用藥物、腦刺激、神經回饋裝置或未核准腦機介面進行注意力增強。

本文中的「attention engineering」是研究綱領，不代表目前技術已能安全、任意地製造 hyperfocus 或提升一般人的高階能力。

核心問題：

$$
\boxed{
\text{Is hyperfocus merely associated with high output,
or can it causally help realize high ability?}
}
$$

---

## 摘要

ADHD-related hyperfocus 已逐步由軼事概念走向可量化研究。2024 年 AHQ-D 為成人 dispositional hyperfocus 提供 preregistered 量表驗證；2026 年成人 ADHD cognitive-affective flexibility 研究進一步指出 hyperfocus 與 switching、emotion reactivity 等機制可能相關。然而，目前並沒有證據證明 hyperfocus 是高智力、創造力或高學術成就的必要原因。

本文提出三個競爭因果模型與一個負面模型。

**Model E：Epiphenomenon**

$$
A\rightarrow H,
\qquad
A\rightarrow Y,
$$

hyperfocus 只是高興趣／高能力活動的伴隨結果。

**Model R：Realization Amplifier**

$$
A\rightarrow H\rightarrow Y,
$$

latent ability 已存在，而 hyperfocus 提高其在長時間工作中的實現率。

**Model D：Developmental Accumulator**

$$
H_{0:T}
\rightarrow
P^{\mathrm{deep\ practice}}_{0:T}
\rightarrow
K_T
\rightarrow
Y_T,
$$

hyperfocus 不只影響當下輸出，還透過多年深度練習塑造後來 expertise。

**Model C：Costly Lock-In**

$$
H\rightarrow Y_{\mathrm{local}}\uparrow,
$$

但：

$$
H\rightarrow U_{\mathrm{global}}\downarrow.
$$

這三個正向／中性模型與一個成本模型需要干預資料才能區分。

本文的第二部分指出，這個問題不再是永遠不可測的反事實。2026 年一項 108 名健康成人、五次訓練的 closed-loop EEG neurofeedback study 顯示，能成功提高 individual alpha frequency 的 learners 出現更快 visual-attention responses 與較佳 attentional efficiency。較早的 closed-loop EEG studies 已能即時 decode attentional states 並回饋；2019 年 ADHD BCI randomized trial 亦報告 BCI attention training 對 inattentive symptoms 有小至中等效果。2024 closed-loop tDCS sustained-attention pilot 仍只有 10 名健康學生，證據非常初步。另一方面，2026 年 sham／alpha-neurofeedback research 顯示部分 EEG alpha change 可由非特異因素、expectancy 或 spontaneous drift 產生，提醒「能改 brain signal」與「特異閉環因果控制」不是同一件事。

因此未來真正有價值的目標不是「製造超專注」，而是「可控注意配置」：

$$
\boxed{
\text{enter}
+
\text{target}
+
\text{depth}
+
\text{dwell}
+
\text{monitor}
+
\text{exit}.
}
$$

---

## 1. Hyperfocus 的最小候選狀態

沿用前文：

$$
H_t
=
F
\left(
C_t^{\mathrm{focus}},
T_t^{\mathrm{dwell}},
B_t^{\mathrm{exit}}
\right).
$$

至少包括：

$$
\text{high concentration},
$$

$$
\text{long dwell},
$$

$$
\text{high disengagement cost}.
$$

但目前沒有公認神經 biomarker。

---

## 2. 能力和 Hyperfocus 不是同一變量

定義：

$$
A_i
=
\text{latent domain capability}.
$$

$$
H_{i,t}
=
\text{hyperfocus-like state}.
$$

$$
Y_{i,t}
=
\text{realized output}.
$$

則：

$$
\boxed{
A_i
\neq
H_{i,t}
\neq
Y_{i,t}.
}
$$

---

## 3. Model E：Epiphenomenon

假設：

$$
A\rightarrow Y
$$

且高能力／高興趣也造成：

$$
A\rightarrow H.
$$

則觀察：

$$
H\leftrightarrow Y
$$

只是 common-cause association。

此時移除 $H$：

$$
Y
$$

不一定下降。

---

## 4. Model R：Realization Amplifier

假設：

$$
A
$$

已存在，但：

$$
H
$$

提高：

- uninterrupted dwell；
- depth；
- repetition；
- memory consolidation opportunities；
- total effective practice。

則：

$$
Y
=
A\eta(H,T,E).
$$

若：

$$
\frac{\partial\eta}{\partial H}>0,
$$

hyperfocus 是能力實現的中介。

---

## 5. Model D：Developmental Accumulator

長期 skill：

$$
K_{t+1}
=
K_t
+
\eta(H_t)P_t
-
\delta_t.
$$

所以：

$$
\sum_{t=0}^{T}H_t
$$

可能改變：

$$
K_T.
$$

這個模型預測：

> 童年／青年期高 domain-specific hyperfocus frequency，即使控制 baseline ability，也能預測後來 expertise growth。

目前此因果鏈尚未被 ADHD longitudinal research 證明。

---

## 6. Model C：Costly Lock-In

還有第四種：

$$
H\rightarrow Y_{\mathrm{local}}\uparrow
$$

但：

$$
H\rightarrow U_{\mathrm{global}}\downarrow.
$$

原因可能包括：

- sleep displacement；
- competing obligations；
- health cost；
- switching failure；
- neglect of bodily needs。

因此即使 hyperfocus 有局部因果收益，也不表示其全域效用為正。

---

## 7. 真正的反事實

問題一：

$$
Y(A,H=1)-Y(A,H=0)
$$

是否大於零？

問題二：

$$
K_T(H_{0:T}=1)-K_T(H_{0:T}=0)
$$

是否大於零？

問題三：

一般人若人工得到：

$$
H^*,
$$

是否：

$$
\Delta Y>0?
$$

這三題都需要 intervention。

---

## 8. 為什麼今天開始不只是哲學反問？

因為 attention state 已可部分被：

- real-time decoding；
- neurofeedback；
- closed-loop stimulation；
- BCI training；

操弄。

這距離「自由調節 hyperfocus」仍然很遠，但已打破：

$$
\boxed{
\text{attention state is experimentally immutable}.
}
$$

---

## 9. 2026 Closed-Loop Alpha-Frequency Study

2026 年研究：

$$
N=108
$$

健康成人，

完成：

$$
5
$$

次 EEG-based IAF neurofeedback 或 active placebo control。

能成功學會提高 IAF 的 participants 出現：

- faster responses；
- higher attentional efficiency；
- stronger cue facilitation。

這支持：

$$
\boxed{
\text{some temporal properties of attention
can be causally modulated by closed-loop training}.
}
$$

但不支持：

$$
\text{hyperfocus can now be engineered}.
$$

---

## 10. Learners 與 Non-Learners 很重要

該研究並非人人都能成功 modulation。

因此：

$$
\boxed{
\text{neurofeedback responsiveness}
\text{ is itself an individual-difference variable}.
}
$$

未來 attention engineering 不能預設一套 protocol 適合所有人。

---

## 11. 2021 Closed-Loop Attention Decoding

real-time EEG decoding 已能在 sustained visual-attention task 中估計 attentional states，並以 participant-specific closed-loop feedback 改變行為。

這證明：

$$
\text{detect}
\rightarrow
\text{feedback}
\rightarrow
\text{behavioral modulation}
$$

原則上可行。

---

## 12. ADHD BCI Training 的早期證據

2019 randomized controlled trial 的 BCI-based attention training 經：

$$
20-24
$$

sessions 後，對 inattentive symptoms 有 small-to-moderate improvement depending on rater。

這是 treatment/training evidence，

不是：

$$
\text{cognitive augmentation proof}.
$$

---

## 13. 2024 Closed-Loop tDCS Pilot：證據仍很薄

adaptive tDCS sustained-attention pilot：

$$
N=10
$$

健康大學生。

這只能提供：

$$
\boxed{
\text{feasibility-level evidence}.
}
$$

不能證明 closed-loop stimulation 已可可靠提升一般 cognition。

---

## 14. 2026 Negative Controls 很重要

2026 neurofeedback work 發現：

- alpha power 可在 genuine、sham、甚至 passive conditions 都上升；
- sham feedback 本身也可能改變 EEG alpha 與 attention-related state。

因此：

$$
\boxed{
\text{brain-signal change}
\neq
\text{specific neurofeedback causation}.
}
$$

真正 closed-loop trials 必須有：

- sham；
- active control；
- expectancy measurement；
- transfer test。

---

## 15. Artificial Hyperfocus 其實不是好目標

如果只最大化：

$$
C^{\mathrm{focus}}\uparrow
$$

與：

$$
T^{\mathrm{dwell}}\uparrow,
$$

卻沒有 exit control：

$$
B^{\mathrm{exit}}\uparrow,
$$

可能製造的是：

$$
\boxed{
\text{maladaptive lock-in}.
}
$$

所以工程目標不能叫：

$$
\text{maximum focus}.
$$

---

## 16. Controllable Attention Allocation

真正理想控制向量：

$$
\mathbf a_t^{\mathrm{ctrl}}
=
\left(
D_t^{\mathrm{depth}},
B_t^{\mathrm{breadth}},
T_t^{\mathrm{dwell}},
\nu_t^{\mathrm{switch}},
E_t^{\mathrm{exit}},
M_t^{\mathrm{monitor}}
\right).
$$

也就是控制：

- 深度；
- 廣度；
- 駐留；
- 切換；
- 退出；
- 背景監控。

---

## 17. 良好注意不是最大專注

本文提出：

$$
\boxed{
\text{good attention}
=
\text{right target}
+
\text{right depth}
+
\text{right duration}
+
\text{right breadth}
+
\text{right exit timing}.
}
$$

所以：

$$
\text{attention quality}
\neq
\text{attention intensity}.
$$

---

## 18. Target Error

如果：

$$
H(\text{wrong target})\uparrow,
$$

則：

$$
Y_{\text{goal}}\downarrow
$$

可能更嚴重。

因此任何 attention engineering 必須先處理：

$$
\text{target selection}.
$$

---

## 19. Exploration Cost

過度集中可能：

$$
B^{\mathrm{breadth}}\downarrow.
$$

在需要 divergent search 的任務中：

$$
P_{\mathrm{creative}}\downarrow
$$

是合理可能。

所以人工深度 focus 必須和 exploration phase 協調。

---

## 20. Hyperfocus Necessity Hypothesis

**HF-H1：** 部分 high achievers 的 extreme output 對 hyperfocus-like dwell 有中介依賴。

若控制 baseline ability、practice、motivation 後， $H$ 沒有任何增量，則否定。

---

## 21. Hyperfocus Development Hypothesis

**HF-H2：** 長期 domain-specific $H_{0:T}$ 預測 expertise growth：

$$
\Delta K_T>0.
$$

需要 prospective longitudinal data。

---

## 22. Attention-State Transfer Hypothesis

**HF-H3：** 若非 ADHD 個體被安全誘導至 matched deep-attention state：

$$
H^*,
$$

在 high-depth tasks 中：

$$
\Delta P>0.
$$

但必須同步測：

$$
\Delta C_{\mathrm{fatigue}},
$$

$$
\Delta C_{\mathrm{switch}},
$$

$$
\Delta C_{\mathrm{exploration}}.
$$

---

## 23. Closed-Loop Control Hypothesis

**HF-H4：** closed-loop state-dependent intervention 應優於 fixed open-loop stimulation。

如果：

$$
P_{\mathrm{closed}}
\leq
P_{\mathrm{open}},
$$

則 attention-state targeting 的額外複雜度沒有價值。

---

## 24. 實驗一：Within-ADHD Natural State Study

同一 ADHD participant 在：

- ordinary focus；
- self-reported hyperfocus；
- post-hyperfocus；

測：

$$
P,
\chi,
T_{\mathrm{dwell}},
B_{\mathrm{exit}},
fatigue.
$$

只做相關，不能證因果。

---

## 25. 實驗二：Interrupt-and-Recover

在高 engagement 狀態提供必要 target switch。

測：

$$
T_{\mathrm{exit}},
$$

$$
T_{\mathrm{reentry}},
$$

$$
P_{\mathrm{post}}.
$$

估計：

$$
B^{\mathrm{exit}}.
$$

---

## 26. 實驗三：Closed-Loop Deep-Work Trial

健康成人或臨床監督樣本：

$$
\text{real NF}
$$

vs：

$$
\text{active sham}.
$$

任務使用：

- proof search；
- code debugging；
- complex reading；
- visual reasoning。

同步測：

$$
\text{depth},
\text{accuracy},
\text{transfer},
\text{fatigue},
\text{switch cost}.
$$

---

## 27. 實驗四：Adaptive Exit Control

系統不是只強化 focus。

當：

$$
T_{\mathrm{dwell}}>T^*
$$

或 competing obligation 到期時，閉環提高：

$$
E^{\mathrm{exit}}.
$$

比較：

$$
\text{focus-only}
$$

與：

$$
\text{focus+exit control}.
$$

這更接近真正 cognition engineering。

---

## 28. 實驗五：Developmental Longitudinal Study

在 gifted ADHD、average-ability ADHD、controls 中多年追蹤：

$$
H_{\mathrm{domain}},
$$

$$
P_{\mathrm{practice}},
$$

$$
K_{\mathrm{skill}},
$$

$$
Y_{\mathrm{achievement}}.
$$

測 Model E、R、D 哪一個最能預測資料。

---

## 29. 安全邊界

未來 attention engineering 可能帶來：

- sleep displacement；
- addiction-like reinforcement；
- maladaptive lock-in；
- neglect of bodily needs；
- autonomy concerns；
- coercive workplace use。

因此：

$$
\boxed{
\text{cognitive enhancement}
\neq
\text{maximize engagement}.
}
$$

---

## 30. 結論

Hyperfocus 與高能力的關係目前仍是開放問題。

本文提出三個真正可競爭模型：

$$
\boxed{
\text{Epiphenomenon}
}
$$

$$
\boxed{
\text{Realization Amplifier}
}
$$

$$
\boxed{
\text{Developmental Accumulator}.
}
$$

以及一個重要負面模型：

$$
\boxed{
\text{Costly Lock-In}.
}
$$

未來 closed-loop EEG、BCI、neurofeedback 與其他受控技術，使這個問題開始具有 intervention route。

真正值得追求的不是：

$$
\text{Artificial Hyperfocus},
$$

而是：

$$
\boxed{
\text{Controllable Attention Allocation}.
}
$$

也就是：

$$
\boxed{
\text{想進就進、該出就出，
保留探索、監控與切換能力。}
}
$$

---

## 參考文獻

1. Hupfeld KE, et al. *Validation of the dispositional adult hyperfocus questionnaire (AHQ-D).* Scientific Reports. 2024;14:19460. DOI: 10.1038/s41598-024-70028-y.  
2. Samson JL, et al. *Cognitive-affective flexibility in adult ADHD: Links to emotion reactivity and hyperfocus.* J Affect Disord Rep. 2026;24:101047.  
3. *Successful closed-loop neurofeedback alpha frequency modulation enhances the temporal dynamics of attention.* NeuroImage. 2026. PMID: 41962614.  
4. *Real-Time Decoding of Attentional States Using Closed-Loop EEG Neurofeedback.* Neural Computation. 2021. PMID: 33513324.  
5. Lim CG, et al. *A randomized controlled trial of a brain-computer interface based attention training program for ADHD.* PLoS ONE. 2019;14:e0216225.  
6. Caravati E, et al. *Closed-Loop Transcranial Electrical Neurostimulation for Sustained Attention Enhancement: A Pilot Study.* Bioengineering. 2024;11:467.  
7. *Alpha power increases spontaneously during a neurofeedback session.* Communications Psychology. 2026.  
8. *Non-specific increase in alpha power during a neurofeedback session targeting its downregulation.* 2026. PMID: 42232075.

---

**狀態：** v0.1 補充理論稿  
**醫學用途：** 無  
**新增原始臨床／人體數據：** 無
