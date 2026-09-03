# AI 單次品質論：意圖忠實度、過程品質、完成度與結果品質

## AI Single-Run Quality Theory: Intent Fidelity, Process Quality, Completion, Verification, and Outcome Quality

**系列**：AI 互動時間與智能時間經濟學系列，第 7 篇／共 8 篇  
**文件編號**：EML-ASRQT-2026-07-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Agent Evaluation／Run-Level Quality／互動時間論收斂篇  
**狀態**：Public Theory Draft  
**直接前置**：《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1

---

## 摘要

AI Agent 的品質常被壓縮成單一結果判定：答案正確、任務通過、benchmark 得分或使用者接受，便被視為「這次表現很好」。然而，對具有意圖解析、規劃、工具使用、長時程執行、驗證、恢復、授權與世界作用能力的 Agent 而言，單一 outcome score 會隱藏至少三類重要資訊：第一，最終結果可能正確，但過程包含錯誤推理、無效工具、違反限制、危險 side effect 或純粹幸運；第二，過程可能高度合理、合規、可驗證，卻因外部環境、隨機失敗或不可控條件而未完成；第三，一個 run 可能已產生大量高價值 evidence、排除錯誤路徑與可重用知識，卻被二值 pass/fail 判為與「什麼都沒做到」相同。

本文提出「AI 單次品質論」（AI Single-Run Quality Theory, ASRQT），將一次 Agent run 的品質定義為多層、向量化、可定位錯誤的結構。第一代品質向量為：

$$
\mathbf Q_{\mathrm{run}}
=
(
Q_I,
Q_S,
Q_P,
Q_E,
Q_C,
Q_V,
Q_{\mathrm{Comp}},
Q_R,
Q_G,
Q_W
),
$$

其中：

- $Q_I$：Intent Fidelity；
- $Q_S$：Specification Quality；
- $Q_P$：Plan Quality；
- $Q_E$：Execution Quality；
- $Q_C$：Constraint Retention；
- $Q_V$：Verification Quality；
- $Q_{\mathrm{Comp}}$：Completion；
- $Q_R$：Result Quality；
- $Q_G$：Governance / Authority Quality；
- $Q_W$：World-Commit Integrity。

本文同時區分 Hard Gates 與 Soft Scores。若禁態被觸發、授權無效、必要驗證缺失或真實世界提交未被正確標記，其他高分不能透過平均將其洗掉。可定義：

$$
Q_{\mathrm{soft}}
=
\exp
\left(
\frac{
\sum_iw_i\ln(Q_i+\epsilon)
}{
\sum_iw_i
}
\right),
$$

以及：

$$
Q_{\mathrm{effective}}
=
G_{\mathrm{hard}}
\cdot
Q_{\mathrm{soft}}.
$$

本文進一步提出「品質—結果四象限」：可靠成功、幸運成功、紀律失敗、全面失敗；將 termination、completion、verification、acceptance 與 certification 分離；引入 Verified Completion、Quality-Adjusted Completion、Trace Coverage、Evaluation Coverage、Failure-Origin Distance、Verification Debt、False Completion Rate 與 Run Reliability 等量。

本文與 EveMissLab 既有 GCPR、生成爆炸／創造優先方法論、ISF、UCPNP Truth–Evidence–Certification 以及本系列前六篇形成收斂。外部研究方面，ClawTrack 已以 Task Score／Process Score 雙評估處理 outcome-only 盲點，Agent GPA 將 Goal、Plan、Action 分層評估，而 2026 年的 log-analysis 研究則直接指出只看 final pass/fail 可能錯估 capability、utility 與 safety。本文在這些方向上再加入意圖忠實度、限制保持、完成度、治理與世界提交，使「AI 單次品質」涵蓋從使用者意圖到現實結果的完整生命週期。

**關鍵詞**：Agent Evaluation、Single-Run Quality、Intent Fidelity、Process Score、Task Score、Completion、Verification、Constraint Retention、Lucky Success、Trace Evaluation、World Commit

---

# 0. 核心問題

最常見的 Agent 評估是：

$$
Success\in\{0,1\}
$$

或：

$$
Score\in[0,1].
$$

但它不足以回答：

- 是否理解正確意圖；
- 計畫是否正確；
- 是否遵守限制；
- 工具是否正確；
- 驗證是否充分；
- 到底完成多少；
- 是否有合法 authority；
- 是否真的改變正確的世界狀態。

因此：

$$
\boxed{
\text{Outcome Score}
\neq
\text{Run Quality}.
}
$$

---

# 1. Run Quality 的完整對象

令：

$$
R
=
(
I,S,P,E,V,O,G,W
).
$$

其中：

- $I$：Intent；
- $S$：Specification；
- $P$：Plan；
- $E$：Execution Trace；
- $V$：Verification；
- $O$：Outcome；
- $G$：Governance；
- $W$：World Commit。

則：

$$
\mathcal Q:R\rightarrow\mathbf Q_{\mathrm{run}}.
$$

---

# 2. 第一代品質向量

$$
\boxed{
\mathbf Q_{\mathrm{run}}
=
(
Q_I,
Q_S,
Q_P,
Q_E,
Q_C,
Q_V,
Q_{\mathrm{Comp}},
Q_R,
Q_G,
Q_W
).
}
$$

品質首先是一個向量，不是單一數字。

---

# 3. Intent Fidelity

使用者意圖：

$$
I_U
$$

與 Agent 重建：

$$
\widehat I_A.
$$

定義：

$$
Q_I
=
1-d_I(I_U,\widehat I_A).
$$

即使最終 artifact 很漂亮，如果 Agent 完成的是錯誤任務：

$$
Q_R\uparrow
\quad\land\quad
Q_I\downarrow.
$$

所以：

$$
\boxed{
\text{Perfect Execution of Wrong Intent}
\neq
\text{High-Quality Run}.
}
$$

---

# 4. Specification Quality

Agent 將意圖轉成：

$$
I_X.
$$

定義：

$$
Q_S
=
1-d_S(\widehat I_A,I_X).
$$

它檢查：

- goal；
- hard constraints；
- soft preferences；
- forbidden states；
- success criteria；
- expected artifacts；
- authority；
- risk boundary。

因此「聽懂了」與「成功編譯成 runtime 規格」是兩種不同品質。

---

# 5. Plan Quality

$$
Q_P
=
f(
GoalAlignment,
Feasibility,
DependencyCorrectness,
RiskAwareness,
ResourceFitness,
VerificationPlan
).
$$

高品質 plan 不能忽略必要依賴、使用不存在工具、超出 budget、漏掉 validator 或假設不可逆 action 可直接 rollback。

---

# 6. Execution Quality

對 execution trace：

$$
E=(e_1,\ldots,e_n),
$$

定義：

$$
Q_E
=
f(
ActionCorrectness,
ToolCorrectness,
ObservationUse,
Efficiency,
Recovery,
TraceIntegrity
).
$$

它回答的是：

> 計畫即使對，Agent 實際有沒有做好？

---

# 7. Plan Adherence 不等於 Blind Adherence

定義：

$$
Q_{PA}=1-d(P,E).
$$

但：

$$
Q_{PA}=1
$$

不一定最佳。

若世界狀態改變，合理行為可能是：

$$
P\rightarrow P'.
$$

所以必須區分：

$$
\text{Unauthorized Deviation}
$$

與：

$$
\text{Evidence-Justified Replan}.
$$

---

# 8. Constraint Retention

令 hard constraints：

$$
C_H=\{c_1,\ldots,c_m\}.
$$

在第 $j$ 步仍保留：

$$
C_H^{(j)}.
$$

定義：

$$
Q_C
=
\min_j
\frac{
\sum_iw_i\mathbb I[c_i\in C_H^{(j)}]
}{
\sum_iw_i
}.
$$

採最小值是因為某些限制只要曾被破壞一次，就可能造成不可逆後果。

因此：

$$
\boxed{
\text{Final Compliance}
\neq
\text{Trajectory Compliance}.
}
$$

---

# 9. Verification Quality

$$
Q_V
=
f(
Coverage,
Independence,
Correctness,
Relevance,
EvidenceStrength,
Reproducibility
).
$$

最重要的不等式：

$$
\boxed{
\text{Result Exists}
\neq
\text{Result Verified}.
}
$$

---

# 10. Verification Coverage

若必要驗證：

$$
V_{\mathrm{req}}
=
\{v_1^\ast,\ldots,v_m^\ast\},
$$

實際完成：

$$
V_{\mathrm{done}},
$$

則：

$$
VCov
=
\frac{
\sum_iw_i\mathbb I[v_i^\ast\in V_{\mathrm{done}}]
}{
\sum_iw_i
}.
$$

---

# 11. Verification Independence

生成器與 evaluator 若共享：

- 同模型；
- 同提示；
- 同資料；
- 同盲點；

則 nominal validation 可能虛高。

因此加入：

$$
I_V
=
\text{Verification Independence}.
$$

可由 deterministic test、independent model、external evidence、proof checker 或 human expert 提高。

---

# 12. Completion

令：

$$
Q_{\mathrm{Comp}}
=
Comp(S)\in[0,1].
$$

若成功條件：

$$
K=\{k_1,\ldots,k_m\},
$$

可定義：

$$
Comp
=
\frac{
\sum_iw_is_i
}{
\sum_iw_i
},
\qquad
s_i\in[0,1].
$$

---

# 13. Hard Completion Gates

若不可妥協條件集合：

$$
K_H,
$$

則：

$$
G_K
=
\prod_{k_i\in K_H}
\mathbb I[k_i\text{ satisfied}].
$$

有效完成度：

$$
Comp_{\mathrm{eff}}
=
G_K
\cdot
Comp_{\mathrm{soft}}.
$$

十項完成九項不一定是 90% 完成；若缺的是「不得刪除原始資料」，整體可以直接失效。

---

# 14. Result Quality

$$
Q_R
=
f(
Correctness,
Utility,
Relevance,
Clarity,
Robustness,
UserFit
).
$$

結果品質只是整體品質的一個維度。

---

# 15. Governance Quality

$$
Q_G
=
f(
AuthorityValidity,
PolicyCompliance,
EscalationQuality,
HumanOversight,
Revocability,
Auditability
).
$$

正確結果若來自無授權 action：

$$
Q_R\approx1,
\qquad
Q_G\ll1.
$$

所以：

$$
\boxed{
\text{Useful Result}
\neq
\text{Legitimate Run}.
}
$$

---

# 16. World-Commit Integrity

定義：

$$
Q_W
=
f(
CommitAuthority,
ReceiptIntegrity,
StateMatch,
ExternalConfirmation,
HistoricalIntegrity
).
$$

Sandbox 成功被誤報為 production 成功：

$$
Q_W\ll1.
$$

---

# 17. Hard Gates

$$
G_{\mathrm{hard}}
=
G_FG_AG_VG_WG_S,
$$

其中：

- $G_F$：Forbidden-state gate；
- $G_A$：Authority gate；
- $G_V$：Required verification gate；
- $G_W$：World-commit gate；
- $G_S$：Safety / domain gate。

在高風險任務中：

$$
G_i\in\{0,1\}
$$

可以保留真正 veto。

---

# 18. Soft Quality Scalarization

若需要 scalar：

$$
Q_{\mathrm{soft}}
=
\exp
\left(
\frac{
\sum_iw_i\ln(Q_i+\epsilon)
}{
\sum_iw_i
}
\right).
$$

再定義：

$$
\boxed{
Q_{\mathrm{effective}}
=
G_{\mathrm{hard}}
Q_{\mathrm{soft}}.
}
$$

但報告時仍應保存完整：

$$
\mathbf Q_{\mathrm{run}}.
$$

---

# 19. 為什麼不能只看總分

同樣：

$$
Q_{\mathrm{effective}}=0.72
$$

可能是：

- intent 高、verification 低；
- intent 低、execution 高；
- result 高、governance 低。

因此：

$$
\boxed{
\text{Scalarization}
\neq
\text{Diagnosis}.
}
$$

---

# 20. 品質—結果四象限

定義 process quality：

$$
Q_{\mathrm{proc}}
$$

與 outcome：

$$
Q_{\mathrm{out}}.
$$

得到四類：

### Reliable Success

$$
Q_{\mathrm{proc}}\uparrow,
\qquad
Q_{\mathrm{out}}\uparrow.
$$

### Lucky Success

$$
Q_{\mathrm{proc}}\downarrow,
\qquad
Q_{\mathrm{out}}\uparrow.
$$

### Disciplined Failure

$$
Q_{\mathrm{proc}}\uparrow,
\qquad
Q_{\mathrm{out}}\downarrow.
$$

### Comprehensive Failure

$$
Q_{\mathrm{proc}}\downarrow,
\qquad
Q_{\mathrm{out}}\downarrow.
$$

---

# 21. Reliable Success

可靠成功代表：

- 意圖對；
- 規格對；
- plan 對；
- execution 對；
- constraints 守住；
- verification 足夠；
- result 對；
- authority 合法；
- world commit 正確。

它最適合作為 training exemplar 與 workflow baseline。

---

# 22. Lucky Success

幸運成功可能是：

- 猜中；
- 工具參數錯但系統容錯；
- 走錯流程但碰巧得到正確結果；
- 未驗證卻剛好正確。

因此：

$$
\boxed{
Q_R\uparrow
\not\Rightarrow
Q_{\mathrm{proc}}\uparrow.
}
$$

若只用 final pass 做正向訓練，可能把壞過程學進去。

---

# 23. Disciplined Failure

紀律失敗可能因：

- API outage；
- target changed；
- theorem false；
- authority revoked；
- external event；
- insufficient deadline。

這類 run：

$$
Q_R\downarrow
$$

但：

$$
Q_{\mathrm{proc}}\uparrow,
\qquad
\Delta K>0.
$$

它不應與「什麼都沒做好」等價。

---

# 24. Termination、Completion、Verification、Acceptance、Certification

令：

$$
T=\text{Terminated},
$$

$$
C=\text{Completed},
$$

$$
V=\text{Verified},
$$

$$
A=\text{Accepted},
$$

$$
Cert=\text{Certified}.
$$

一般：

$$
\boxed{
T
\neq
C
\neq
V
\neq
A
\neq
Cert.
}
$$

---

# 25. Verified Completion

$$
VC
=
Q_{\mathrm{Comp}}
Q_V.
$$

若完成度是 $1$，驗證只有 $0.2$：

$$
VC=0.2.
$$

---

# 26. Quality-Adjusted Completion

$$
QAC
=
Q_{\mathrm{Comp}}
Q_R
Q_V.
$$

加入 hard gate：

$$
QAC_{\mathrm{eff}}
=
G_{\mathrm{hard}}
QAC.
$$

---

# 27. Intent-Adjusted Completion

若完成了錯誤 intent：

$$
Q_{\mathrm{Comp}}\approx1
$$

仍不應高分。

定義：

$$
IAC
=
Q_IQ_{\mathrm{Comp}}.
$$

---

# 28. Governance-Adjusted Completion

對世界作用任務：

$$
GAC
=
Q_{\mathrm{Comp}}Q_GQ_W.
$$

任務做成，不代表手段與 authority 可以被忽略。

---

# 29. Useful Progress

未完成 run 仍可能有：

$$
\Delta K,
\Delta E,
-\Delta U.
$$

定義：

$$
UP
=
\alpha\Delta Comp
+
\beta\Delta K
+
\gamma\Delta E
-
\delta\Delta Risk.
$$

這對 research、debugging、proof search 特別重要。

---

# 30. Negative Progress

若 Agent：

- 污染資料；
- 寫入錯誤記憶；
- 增加 verification debt；
- 製造錯誤 artifact；

則：

$$
UP<0
$$

是可能的。

因此：

$$
\boxed{
\text{Activity}
\neq
\text{Progress}.
}
$$

---

# 31. Trace Coverage

若需要觀察事件集合：

$$
E_{\mathrm{req}},
$$

實際 log：

$$
E_{\mathrm{log}},
$$

則：

$$
TCov
=
\frac{
|E_{\mathrm{req}}\cap E_{\mathrm{log}}|
}{
|E_{\mathrm{req}}|
}.
$$

Process score 的可信度受 trace coverage 限制。

---

# 32. Evaluation Coverage

令品質維度：

$$
\mathcal Q
=
\{I,S,P,E,C,V,Comp,R,G,W\}.
$$

Evaluator 實際覆蓋：

$$
\mathcal Q_{\mathrm{eval}}.
$$

則：

$$
ECov
=
\frac{
\sum_iw_i\mathbb I[q_i\in\mathcal Q_{\mathrm{eval}}]
}{
\sum_iw_i
}.
$$

只測結果的 benchmark 不能聲稱測完整 Agent quality。

---

# 33. Evaluator Quality

$$
Q_{\mathrm{eval}}
=
f(
Calibration,
Agreement,
Robustness,
Independence,
Determinism
).
$$

所以：

$$
\boxed{
\text{Measured Quality}
\neq
\text{True Quality}.
}
$$

---

# 34. Hybrid Evaluation

不同 evaluator 適合不同層：

- deterministic test：schema、unit test、數值；
- LLM judge：語義、相關性、複合 rubric；
- human：高風險、價值衝突、模糊 intent；
- external evidence：真實世界狀態。

因此不應讓單一 evaluator monoculture 取代全部品質層。

---

# 35. Failure-Origin Distance

令真正因果錯誤事件：

$$
e_c,
$$

表面失敗事件：

$$
e_s.
$$

定義：

$$
D_F
=
d_G(e_c,e_s).
$$

高 $D_F$ 代表錯誤很早發生、很晚才暴露。

---

# 36. Error Amplification

若初始偏差：

$$
\epsilon_0
$$

經後續變換：

$$
\epsilon_n
=
L_n\cdots L_1\epsilon_0,
$$

且：

$$
\prod_iL_i>1,
$$

小錯誤可能被放大成大終局偏差。

所以 early-stage quality 不能由最終結果完全替代。

---

# 37. Failure Attribution Vector

$$
\mathbf F
=
(
F_I,
F_S,
F_P,
F_E,
F_C,
F_V,
F_G,
F_W
).
$$

目標不是強迫找唯一 root cause，而是產生可操作的 attribution。

---

# 38. Process Score 與 Outcome Score

定義：

$$
Q_{\mathrm{proc}}
=
f(
Q_I,Q_S,Q_P,Q_E,Q_C,Q_V,Q_G
),
$$

以及：

$$
Q_{\mathrm{out}}
=
f(
Q_{\mathrm{Comp}},Q_R,Q_W
).
$$

建議首先報：

$$
(Q_{\mathrm{proc}},Q_{\mathrm{out}})
$$

雙軸。

---

# 39. ClawTrack 接口

ClawTrack 的 process dimensions：

- goal alignment；
- efficiency；
- information utilization；
- result verification。

本文映射：

$$
GoalAlignment
\rightarrow
(Q_I,Q_P),
$$

$$
Efficiency
\rightarrow
Q_E,
$$

$$
InformationUtilization
\rightarrow
Q_E,
$$

$$
ResultVerification
\rightarrow
Q_V.
$$

再補：

$$
Q_S,Q_C,Q_G,Q_W,Q_{\mathrm{Comp}}.
$$

---

# 40. Agent GPA 接口

Agent GPA 的：

- Goal Fulfillment；
- Logical Consistency；
- Execution Efficiency；
- Plan Quality；
- Plan Adherence；

可映射到：

$$
Q_P,
Q_E,
Q_{\mathrm{Comp}},
Q_R.
$$

ASRQT 再加入上游 Intent 及下游 Verification、Governance、World Commit。

---

# 41. Log Analysis 接口

Outcome-only evaluation 可能隱藏：

- shortcut；
- scaffold failure；
- dangerous action；
- wrong tool；
- recurring failure mode。

因此：

$$
\boxed{
\text{Credible Agent Evaluation}
\supset
\text{Outcome}
+
\text{Trace}.
}
$$

Trace 不要求公開 private chain-of-thought。

---

# 42. Verification Bottleneck

生成爆炸理論已指出：

$$
\lambda_{\mathrm{system}}
\le
\min(
\lambda_g,
\lambda_e,
\lambda_v
).
$$

當：

$$
\lambda_g\gg\lambda_v,
$$

系統累積未驗證候選。

所以：

$$
Q_V
$$

是 AI 時代單次品質的核心瓶頸之一。

---

# 43. Verification Debt

$$
D_V
=
\sum_iw_i(1-Q_{V,i}).
$$

若：

$$
\frac{dD_V}{dt}>0,
$$

代表生成速度長期高於可信驗證能力。

---

# 44. Quality Debt

更廣義：

$$
D_Q
=
D_I+D_S+D_V+D_G+D_W.
$$

高名義產出可以伴隨：

$$
D_Q\uparrow.
$$

---

# 45. Run Quality 不等於 Agent Capability

單一 run：

$$
\mathbf Q_{\mathrm{run}}
$$

只是一次樣本。

Agent capability 應估：

$$
C_A
=
E[
\mathbf Q_{\mathrm{run}}
\mid
Task,Budget,Tools,Harness,Environment
].
$$

還需看 variance、tail failure、recovery 與 calibration。

因此：

$$
\boxed{
\text{One Good Run}
\neq
\text{Reliable Agent}.
}
$$

---

# 46. Run Reliability

定義：

$$
Rel
=
P(
Q_{\mathrm{proc}}\ge\theta_P
\land
Q_{\mathrm{out}}\ge\theta_O
).
$$

它比只看：

$$
P(Q_R\ge\theta_R)
$$

更嚴格。

---

# 47. Lucky Success Rate

$$
LSR
=
P(
Q_R\ge\theta_R
\land
Q_{\mathrm{proc}}<\theta_P
).
$$

高 LSR 代表 pass rate 可能高估可靠能力。

---

# 48. Disciplined Failure Rate

$$
DFR
=
P(
Q_{\mathrm{proc}}\ge\theta_P
\land
Q_R<\theta_R
).
$$

它能分離「系統很亂」與「環境困難／任務不可達」。

---

# 49. False Completion Rate

$$
FCR
=
P(
AgentClaimsDone=1
\land
VC<\theta
).
$$

這是 production Agent 非常重要的品質指標。

---

# 50. Completion Calibration

若 Agent 自評：

$$
\hat p_C
$$

而外部 verified completion：

$$
y_C,
$$

可使用 Brier score / calibration error 評估：

> Agent 說自己完成時到底可信不可信？

---

# 51. Quality-Adjusted Productivity

$$
P_Q
=
\frac{
QAC_{\mathrm{eff}}
}{
C_{\mathrm{total}}+\epsilon
}.
$$

其中：

$$
C_{\mathrm{total}}
=
C_{\mathrm{compute}}
+
C_{\mathrm{tool}}
+
C_{\mathrm{human}}
+
C_{\mathrm{latency}}
+
C_{\mathrm{risk}}.
$$

---

# 52. Quality-Adjusted Delegation Leverage

第 6 篇委任槓桿：

$$
\Lambda_D.
$$

現在定義：

$$
\Lambda_D^Q
=
\frac{
Q_{\mathrm{effective}}
V_{\mathrm{delegated}}
}{
T_H^{gov}+\epsilon
}.
$$

低品質 autonomous throughput 不應被叫做高治理槓桿。

---

# 53. Evaluation-to-Improvement

若：

$$
Q_i
$$

是主要低分維度，下一輪應優先投入能最大化：

$$
E[
\Delta Q_{\mathrm{effective}}
]
$$

的 intervention。

所以 evaluation 直接回接第 5 篇的 compute allocation。

---

# 54. Evaluation-to-Training

完整閉環：

$$
Run
\rightarrow
Evaluate
\rightarrow
Attribute
\rightarrow
SelectTrace
\rightarrow
Update
\rightarrow
Run'.
$$

若只選 final success，Lucky Success 可能被誤當正樣本。

---

# 55. Evaluation-to-Governance

若主要問題是：

$$
Q_G,
$$

不一定要重新訓練模型。

可能要改：

- authority；
- approval；
- escalation；
- policy；
- tool scope。

因此：

$$
\boxed{
\text{Low Quality}
\not\Rightarrow
\text{Model Problem}.
}
$$

---

# 56. Evaluation-to-Architecture

若：

$$
Q_I\downarrow
$$

問題偏 intent inference。

若：

$$
Q_P\downarrow
$$

偏 planner。

若：

$$
Q_E\downarrow
$$

偏 execution runtime。

若：

$$
Q_V\downarrow
$$

偏 validator。

所以品質向量可以定位 architecture layer。

---

# 57. Benchmark Contract

任何 Agent benchmark 至少應聲明：

```text
task semantics
intent source
success criteria
hard constraints
tool environment
budget
harness
process observability
outcome evaluator
process evaluator
verification method
authority assumptions
world-effect scope
seed / repetition policy
```

否則 score 很容易偷換測量對象。

---

# 58. Budget-Normalized Quality

若：

$$
B_A^{(1)}
\neq
B_A^{(2)},
$$

不能把 score 差異全部歸因於模型能力。

應比較：

$$
Q(A\mid B_0)
$$

或完整：

$$
Q(Budget)
$$

曲線。

---

# 59. Quality Frontier

不同模型、harness、budget、topology、oversight 形成：

$$
(
Quality,
Cost,
Latency,
HumanTime,
Risk
).
$$

真正比較應看 Pareto frontier，而不是單一 leaderboard。

---

# 60. Minimum Quality Contract

Production task 可定義：

$$
\mathfrak Q_{\min}
=
(
Q_I^{min},
Q_C^{min},
Q_V^{min},
Q_R^{min},
Q_G^{min},
Q_W^{min}
).
$$

若 hard floor 不滿足：

$$
RejectCommit.
$$

所以：

$$
\boxed{
\text{Best-Effort Output}
\neq
\text{Production-Admissible Output}.
}
$$

---

# 61. Domain-Specific Quality

不同 domain 的權重不同。

Creative writing 偏重：

$$
Q_I,Q_R.
$$

Code deployment 偏重：

$$
Q_C,Q_V,Q_G,Q_W.
$$

Mathematical proof 偏重：

$$
Q_V.
$$

高風險專業領域還要加重 evidence、scope、uncertainty 與 governance。

因此不存在所有 domain 共用的唯一品質 scalar。

---

# 62. 可檢驗命題

## 命題一：Outcome Insufficiency

存在：

$$
Q_R^{(1)}
\approx
Q_R^{(2)}
$$

但：

$$
Q_{\mathrm{proc}}^{(1)}
\neq
Q_{\mathrm{proc}}^{(2)}.
$$

## 命題二：Lucky Success

$$
P(
Q_R\uparrow
\land
Q_{\mathrm{proc}}\downarrow
)>0.
$$

## 命題三：Disciplined Failure

$$
P(
Q_R\downarrow
\land
Q_{\mathrm{proc}}\uparrow
)>0.
$$

## 命題四：Verification Bottleneck

生成能力上升而 validator 固定時：

$$
D_V\uparrow.
$$

## 命題五：Trace Value

有 trace 的 evaluator 對 failure attribution 優於 outcome-only evaluator。

## 命題六：Hard-Gate Necessity

純平均分數可能讓 authority / forbidden-state violation 被其他高分錯誤補償。

## 命題七：Run-Capability Separation

單次高分不充分支持高 reliability claim。

---

# 63. 實驗設計

第一，設計 Lucky Success：故意讓 Agent 用錯過程但因環境容錯得到正確答案。

第二，設計 Disciplined Failure：外部 API 故障，但過程完全合理。

第三，加入 hard-constraint violation，測平均分數是否錯誤掩蓋。

第四，對同結果分別做 no verification、self-check、independent validator。

第五，做 trace ablation：final only、tool log、full event lineage。

第六，控制相同 budget，測完整：

$$
\mathbf Q_{\mathrm{run}}.
$$

---

# 64. 生成爆炸理論的收斂

生成成本下降後，稀缺逐步從候選本身轉向：

$$
\text{criteria}
+
\text{evaluation}
+
\text{verification}
+
\text{world feedback}.
$$

所以 AI 時代品質系統的核心不是「多生成」，而是能否把候選爆炸轉成可信結果。

---

# 65. GCPR 的收斂

GCPR 提出：

> 結果是過程的積分。

ASRQT 將其操作化為：

$$
\boxed{
\text{Run Quality}
=
\text{Intent}
+
\text{Process}
+
\text{Verification}
+
\text{Completion}
+
\text{Result}
+
\text{Governance}
+
\text{World Commit}.
}
$$

---

# 66. UCPNP 的收斂

UCPNP 分離：

$$
Truth,
Evidence,
Certification.
$$

因此：

$$
Q_R
\neq
Q_V
\neq
Q_{\mathrm{Cert}}.
$$

看起來對、有證據、通過正式 certification 是不同層次。

---

# 67. 與第 8 篇的接口

前七篇依次處理：

1. 互動時間；
2. 意圖週期；
3. 單輪 execution；
4. 偏序拓撲；
5. compute allocation；
6. 委任與治理；
7. run quality。

最後第 8 篇要回到最大的問題：

> 人類每天仍只有有限生物時間，而 AI 可以在同一世界日裡運行大量互動時間、計算時間與委任時間。這些局部時間如何真正進入世界歷史？

即：

# **世界時間與智能文明**

---

# 68. 規範與倫理邊界

本框架不應：

1. 把所有價值壓成 leaderboard；
2. 為 process score 要求公開 private chain-of-thought；
3. 把使用者滿意等同真實正確；
4. 讓結果高分抵消 authority / safety violation；
5. 以低成本為由犧牲必要 verification；
6. 把一次成功當 reliability；
7. 讓同模型 evaluator 壟斷所有品質判定；
8. 把可量化維度當作全部價值。

---

# 69. 理論限制

第一，各 $Q_i$ 的 operationalization 依 domain 而異。

第二，完整 intent 不可直接觀測， $Q_I$ 只能近似。

第三，process evaluation 受 trace completeness 限制。

第四，LLM judge 可能有 calibration 與 correlation 問題。

第五，不存在已證明的普遍唯一 scalarization。

第六，hard gate 需要 domain governance。

第七，單次品質與長期 reliability 間仍需統計模型。

---

# 70. 結論

AI Agent 的品質不能再只問：

> 答案對不對？

完整問題是：

> 它理解對了嗎？規格對了嗎？計畫對了嗎？執行對了嗎？限制守住了嗎？驗證做了嗎？完成多少？結果好嗎？有權這樣做嗎？真的正確改變世界了嗎？

因此：

$$
\boxed{
\mathbf Q_{\mathrm{run}}
=
(
Q_I,
Q_S,
Q_P,
Q_E,
Q_C,
Q_V,
Q_{\mathrm{Comp}},
Q_R,
Q_G,
Q_W
).
}
$$

最重要的拒絕是：

$$
\boxed{
\text{Outcome}
\neq
\text{Quality}.
}
$$

一個 run 可以：

- 答對但不可靠；
- 答錯但值得學習；
- 完成但未驗證；
- 驗證但未獲授權；
- 有 artifact 但沒完成 intent；
- sandbox 成功但未改變現實。

真正成熟的 Agent evaluation 應同時保存：

$$
\boxed{
\text{Intent Fidelity}
+
\text{Process Quality}
+
\text{Constraint Retention}
+
\text{Verification}
+
\text{Completion}
+
\text{Outcome}
+
\text{Governance}
+
\text{World Integrity}.
}
$$

它的目的不是產生更漂亮的總分，而是：

$$
\boxed{
\text{知道這一次哪裡好、哪裡壞、為什麼成功、為什麼失敗，以及下一單位資源應該修哪裡。}
}
$$

---

# 參考文獻與前置理論

## EveMissLab 前置理論

1. Neo.K，《互動時間論：從鐘錶時間到意圖驅動的智能狀態轉換》v0.1，2026。
2. Neo.K，《意圖週期論：使用者意圖、AI 接受、執行與結果的閉環結構》v0.1，2026。
3. Neo.K，《單輪不是一步：AI Turn、內部迴圈、工具動作與執行軌跡》v0.1，2026。
4. Neo.K，《互動時間拓撲：平行 Agent、偏序因果與不可約互動深度》v0.1，2026。
5. Neo.K，《AI 計算時間經濟學：Token、算力、額度與智能資源配置》v0.1，2026。
6. Neo.K，《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1，2026。
7. Neo.K，《生成爆炸：AI 時代的創造優先方法論》公開版 v2.0，2026。
8. Neo.K，《通用創造過程結果論》，EveMissLab。
9. Neo.K，《Intent-to-System Flow》系列，2026。
10. Neo.K with Aletheia，《UCPNP Unified Theory》v0.1，2026。

## 外部研究

11. Wu, X., Zhu, X., Liu, X., et al. *ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents*. arXiv:2607.28037, 2026.
12. Jia, A. S., Huang, D., Vytla, N., Choudhury, N., Mitchell, J. C., Datta, A. *What Is Your Agent's GPA? A Framework for Evaluating Agent Goal-Plan-Action Alignment*. arXiv:2510.08847v2, 2026.
13. Kirgis, P., Kapoor, S., et al. *Log analysis is necessary for credible evaluation of AI agents*. arXiv:2605.08545, 2026.
14. Liu, S., Dehghan, S., Ganhotra, J., Hirzel, M., Jabbarvand, R. *From Plan to Action: How Well Do Agents Follow the Plan?* arXiv:2604.12147, 2026.
15. Arghal, R., Chen, F., Dalton, N., et al. *A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents*. arXiv:2602.08964, 2026.
16. *Aligning Agents via Planning: A Benchmark for Trajectory-Level Planning Preferences*. arXiv:2604.08178, 2026.

---

## 一句話版本

> **AI 單次品質不是最終答案的分數，而是從意圖、規格、計畫、執行、限制、驗證、完成、結果、治理到世界提交的完整品質向量；「答對了」只能證明結果可能是對的，不能單獨證明這是一個可靠的成功。**

---

*EML-ASRQT-2026-07-v0.1*  
*AI 互動時間與智能時間經濟學系列 07/08*
