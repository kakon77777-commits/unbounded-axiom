# CFATC-B04｜錯誤形態遷移：從低級錯誤到遺漏、邊界、形式化義務與高複雜度殘差
## Error Morphology Shift: From Surface Failures to Omissions, Boundary Errors, Formal Obligations, and High-Complexity Residuals

**系列：** Conditional Frontier Activation and Human–AI Tail Coupling（CFATC）  
**系列中文名：** 條件式前沿觸發與人機尾端耦合系列  
**篇次：** Paper 04 / 08  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** AI 錯誤型態／Frontier Reliability／Formal Verification／Long-Horizon Agent Failure

---

## 摘要

CFATC-B01 至 B03 已建立一條能力鏈：

$$
\boxed{
\text{Latent Capability}
\rightarrow
\text{Activated Capability}
\rightarrow
\text{Visible Capability}.
}
$$

本文處理下一個問題：

> **當 frontier AI 真的變強時，錯誤是否只是變少，還是其結構也會改變？**

直覺上，如果模型能力提高，應有：

$$
P(\mathrm{error})\downarrow.
$$

這通常是我們期待的方向。但僅觀察 error rate 會遺漏另一個可能更重要的現象：低階、容易看見、容易定位的錯誤下降後，剩餘錯誤可能更集中於需要更大上下文、更高抽象層、更長依賴鏈或更強驗證器才能發現的區域。

本文提出：

$$
\boxed{
\text{Error Reduction}
\neq
\text{Error Morphology Invariance}.
}
$$

並將 **Error Morphology Shift（錯誤形態遷移）** 定義為：

> 在控制任務、資源、互動與驗證條件後，AI 的錯誤分布在錯誤層級、局部性、可偵測性、修復成本、傳播範圍與時間位置上發生系統性變化。

本文首先整理一組由實際高難度數學、程式與架構協作觀察得到的 motivating taxonomy：

$$
E_1=\text{symbol / surface error}
$$

$$
E_2=\text{forgotten prior definition / local state loss}
$$

$$
E_3=\text{code does not run / direct execution failure}
$$

$$
E_4=\text{invalid proof leap / local logical gap}
$$

較高階殘差則可能轉為：

$$
E_5=\text{locally correct but missing conditions}
$$

$$
E_6=\text{definition / validity-boundary ambiguity}
$$

$$
E_7=\text{abstraction-layer mismatch}
$$

$$
E_8=\text{informal argument plausible, formalization misses an obligation}
$$

$$
E_9=\text{architecture globally plausible, but one branch is omitted under complexity}.
$$

本文不主張所有模型世代必然依序從 $E_1$ 單調遷移至 $E_9$，而提出較弱、可驗證的 **Morphology Shift Hypothesis（MSH）**：

$$
\boxed{
P(E=e\mid A_{t+1},T,R)
\neq
P(E=e\mid A_t,T,R)
}
$$

且在 frontier-normalized 任務中，error mass 可能由低層可見錯誤逐步移向高層結構殘差。

為避免把「任務變難」誤認成「模型錯誤型態變了」，本文區分三種來源：

$$
\boxed{
\text{Generation Shift}
\neq
\text{Task-Selection Shift}
\neq
\text{Detection Shift}.
}
$$

- **Generation Shift**：模型本身產生不同類型的錯誤；
- **Task-Selection Shift**：因模型變強，人類把它推去更難、更長、更開放的任務，因此暴露新錯誤；
- **Detection Shift**：新的 verifier、formalization、trajectory audit 使以前存在但看不見的錯誤被發現。

只有在 matched-task 或 frontier-normalized regime 中，才能較可靠研究第一種真正的 morphology change。

本文提出 **Error Morphology Vector**：

$$
\boxed{
\mathbf E
=
(
L,
S,
D,
R,
B,
P,
T,
V
)
}
$$

其中：

- $L$：Layer / abstraction depth；
- $S$：Spatial / structural locality；
- $D$：Detectability；
- $R$：Repairability；
- $B$：Blast radius；
- $P$：Propagation / persistence potential；
- $T$：Temporal position in trajectory；
- $V$：Verification dependence。

這使兩個同樣「錯一次」的系統可以具有完全不同風險。例如，一個 syntax error：

$$
E_{\mathrm{syntax}}
$$

通常 detectability 高、blast radius 小、repair cost 低；而一個被嵌入架構早期的錯誤抽象：

$$
E_{\mathrm{architecture}}
$$

可能局部每一步都看似合理，但經過數十個 downstream steps 後才形成失敗。

本文因此提出：

$$
\boxed{
\text{Error Count}
\neq
\text{Error Risk}.
}
$$

更合理的風險可概念化為：

$$
\boxed{
\mathcal R_E
=
\sum_e
P(e)
\cdot
I(e)
\cdot
L_{\mathrm{detect}}(e)
\cdot
P_{\mathrm{prop}}(e),
}
$$

其中 $I(e)$ 為影響、 $L_{\mathrm{detect}}$ 為偵測延遲、 $P_{\mathrm{prop}}$ 為錯誤傳播可能性。

本文進一步將 formal reasoning 視為觀察 morphology shift 的重要實驗場。既有 EveMissLab 的 Mathematical Problem Formalization 研究已指出：

$$
\boxed{
\text{Proof Formalization}
\neq
\text{Problem-Generation Formalization},
}
$$

以及：

$$
\boxed{
\text{logical correctness of a formal proof}
\neq
\text{fidelity of the formal target to the intended problem}.
}
$$

因此，當 theorem prover 越來越能產生 kernel-accepted proof，錯誤前沿可能上移到：

- theorem target 選錯；
- 量詞依賴錯；
- hidden assumption 被漏掉；
- formal statement drift；
- bridge lemma 缺失；
- architecture-level dependency omission。

FormalProofBench 2026 顯示 frontier foundation models 在 graduate-level Lean proof 上仍有巨大空間，最佳基礎模型約為 33.5% accuracy；TheoremBench 2026 則發現現有 prover 容易偏向先解簡單 subtheorems，且常以冗長 tactic trace 取代緊湊 proof plan。這些結果顯示，形式數學中的剩餘失敗已不能只由「會不會寫 Lean syntax」描述。

Long-horizon Agent 研究呈現類似現象。AgentRx 2026 針對失敗 trajectory 標註 critical failure step，LongRCA Bench 則顯示在上百步 Agent 軌跡中，即使知道最終失敗，要定位最早決定性 root-cause step 仍很困難；HORIZON 與 YC-Bench 等工作亦開始觀察 goal drift、state loss、over-parallelization、錯誤依賴與 compounding consequences。這表明：

$$
\boxed{
\text{Agent Reliability}
\neq
\text{Per-Step Correctness}.
}
$$

本文最後提出 **Error Morphology Evaluation Protocol（EMEP）**。對不同 AI 世代或 interaction regime，不只記錄 success rate，而同步記錄：

1. first-shot error type；
2. earliest decisive error；
3. detection latency；
4. repair rounds；
5. residual error after repair；
6. blast radius；
7. formal / empirical verification status；
8. whether error originated in representation, reasoning, tool use, state, architecture, or trajectory.

本文的核心主張不是「AI 越強，錯誤越陰險」這種不可證偽敘事，而是：

> **當低階錯誤被能力提升與工具化大量消除後，可靠性研究必須把注意力上移到更高抽象、更長依賴、更難驗證的 residual error frontier。**

**關鍵詞：** Error Morphology Shift、Residual Error Frontier、Formal Verification、Omission Error、Boundary Error、Architecture Error、Long-Horizon Agent、Trajectory Failure、Recursive Repair、Verification Debt

---

# 1. 問題：AI 變強以後，錯誤去哪裡了？

最簡單模型：

$$
C(A)\uparrow
\Rightarrow
P(E)\downarrow.
$$

這可以成立。

但它沒有回答：

$$
\boxed{
P(E=e_i)
}
$$

的分布如何改變。

---

# 2. 錯誤率與錯誤型態是兩個問題

定義：

$$
p_E(A,T)
=
P(
\text{error}
\mid
A,T
).
$$

再定義：

$$
\pi_E(e)
=
P(
E=e
\mid
\text{error occurred}
).
$$

模型可以：

$$
p_E\downarrow
$$

同時：

$$
\pi_E
$$

大幅改變。

---

# 3. Error Morphology Shift

本文定義：

$$
\boxed{
\mathcal M_E(A,T,R)
=
P(
E=e
\mid
A,T,R
).
}
$$

若：

$$
\mathcal M_E(A_1,T,R)
\neq
\mathcal M_E(A_2,T,R),
$$

則存在 error morphology difference。

---

# 4. 低階錯誤群

Motivating taxonomy：

$$
E_1=\text{symbol error}
$$

$$
E_2=\text{definition / local-state loss}
$$

$$
E_3=\text{execution failure}
$$

$$
E_4=\text{invalid local reasoning step}.
$$

---

# 5. 高階殘差群

$$
E_5=\text{missing condition}
$$

$$
E_6=\text{boundary ambiguity}
$$

$$
E_7=\text{abstraction mismatch}
$$

$$
E_8=\text{formal obligation omission}
$$

$$
E_9=\text{architecture branch omission}.
$$

---

# 6. 這不是嚴格階梯

不能假設：

$$
E_1<E_2<\cdots<E_9
$$

在所有 domain 都成立。

它們只是具有不同 abstraction / dependency depth 的候選類別。

---

# 7. Error Layer

本文定義：

$$
L(E)\in\{0,1,\ldots,k\}.
$$

例如：

- $L_0$：surface；
- $L_1$：local semantic；
- $L_2$：local logic；
- $L_3$：condition / boundary；
- $L_4$：formal obligation；
- $L_5$：architecture；
- $L_6$：trajectory / world state；
- $L_7$：meta-framing。

---

# 8. Surface Error

例如：

- typo；
- syntax；
- malformed call；
- wrong variable name。

通常：

$$
D_{\mathrm{detect}}\uparrow.
$$

---

# 9. Local Semantic Error

例如使用錯一個定義、混淆局部符號。

---

# 10. Local Logical Error

例如：

$$
A\rightarrow B
$$

被錯推為：

$$
B\rightarrow A.
$$

---

# 11. Missing-Condition Error

局部推理都對，但漏掉：

$$
H^\ast.
$$

結果：

$$
\boxed{
\text{locally valid}
+
\text{globally underconditioned}.
}
$$

---

# 12. Boundary Error

方法在：

$$
U
$$

內有效，

但 AI 外推到：

$$
x\notin U.
$$

---

# 13. Abstraction-Layer Mismatch

例如使用：

- implementation argument

回答：

- architecture question；

或用：

- empirical correlation

支撐：

- formal implication。

---

# 14. Formal Obligation Omission

非形式論證看起來成立，

但 formalization 展開後出現：

$$
O_1,O_2,\ldots,O_n
$$

其中某個 obligation 未被滿足。

---

# 15. Architecture Branch Omission

整體 design 很合理，

但在：

$$
G=(V,E)
$$

中漏掉一條必要 branch：

$$
e^\ast\notin E_{\mathrm{implemented}}.
$$

---

# 16. Trajectory Error

不是某一步明顯錯，

而是：

$$
a_1,a_2,\ldots,a_n
$$

組合後逐步偏離。

---

# 17. Meta-Framing Error

問題本身被表示錯：

$$
Q
\rightarrow
Q'.
$$

之後每一步都可以非常高品質，

但答案屬於錯的問題。

---

# 18. 三種「錯誤變高階」的來源

本文要求區分：

$$
\boxed{
\text{Generation Shift}
}
$$

$$
\boxed{
\text{Task-Selection Shift}
}
$$

$$
\boxed{
\text{Detection Shift}.
}
$$

---

# 19. Generation Shift

固定：

$$
T,R,V
$$

後，

模型 $A_2$ 的：

$$
P(E=e_i)
$$

與 $A_1$ 系統性不同。

這才最接近真正 model error morphology shift。

---

# 20. Task-Selection Shift

模型變強後，人類開始交付：

$$
D(T)\uparrow.
$$

新錯誤可能只是新任務區域的錯誤。

---

# 21. Selection Effect

如果舊模型根本到不了 architecture stage，

它不會犯 architecture omission。

它可能更早就在 syntax stage 失敗。

因此：

$$
\boxed{
\text{later failure}
\neq
\text{worse capability}.
}
$$

---

# 22. Detection Shift

加入：

- formal verifier；
- static analyzer；
- trajectory audit；

後，原本看不見的高階錯誤變得可見。

---

# 23. 更好的驗證器可能讓錯誤「看起來變多」

若：

$$
V_2>V_1,
$$

則：

$$
N_{\mathrm{detected}}(V_2)
>
N_{\mathrm{detected}}(V_1)
$$

完全可能。

---

# 24. 因此 Error Detection Rate 與 Error Generation Rate 必須分開

$$
\boxed{
p_{\mathrm{gen}}
\neq
p_{\mathrm{detect}}.
}
$$

---

# 25. Frontier-Normalized Comparison

為降低 task-selection confound，可定義 relative difficulty：

$$
\boxed{
\delta(T,A)
=
\frac{
D(T)
}{
C_{\mathrm{baseline}}(A)
}.
}
$$

---

# 26. 比較相近 $\delta$

若：

$$
\delta(T_1,A_1)
\approx
\delta(T_2,A_2),
$$

再比較 morphology，較合理。

---

# 27. Matched-Task Comparison

另一種方式是直接固定同一：

$$
T.
$$

但當強模型接近 ceiling 時，error sample 太少。

---

# 28. 因此需要兩種研究設計

1. Same-task morphology；
2. Frontier-normalized morphology。

兩者回答不同問題。

---

# 29. Error Morphology Vector

本文提出：

$$
\boxed{
\mathbf E
=
(
L,
S,
D,
R,
B,
P,
T,
V
).
}
$$

---

# 30. Layer $L$

錯誤位於哪個抽象層。

---

# 31. Structural Locality $S$

錯誤影響：

- one token；
- one function；
- one lemma；
- one module；
- whole architecture。

---

# 32. Detectability $D$

有多容易被：

- parser；
- compiler；
- test；
- human；
- prover；

發現。

---

# 33. Repairability $R$

錯誤被定位後，需要多少修改才能恢復。

---

# 34. Blast Radius $B$

錯誤會破壞多少 downstream state。

---

# 35. Propagation $P$

錯誤能否被後續步驟吸收成「正常前提」。

---

# 36. Temporal Position $T$

錯誤發生在 trajectory：

- early；
- middle；
- late。

---

# 37. Verification Dependence $V$

是否只有特定 verifier 才能發現。

---

# 38. 一個 syntax error

可以概念化：

$$
\mathbf E_{\mathrm{syntax}}
=
(
0,
\text{local},
\text{high detect},
\text{easy repair},
\text{small blast},
\text{low propagation},
\text{early},
\text{compiler}
).
$$

---

# 39. 一個 architecture assumption error

可能：

$$
\mathbf E_{\mathrm{arch}}
=
(
5,
\text{global},
\text{low detect},
\text{hard repair},
\text{large blast},
\text{high propagation},
\text{early-origin/late-detection},
\text{multi-verifier}
).
$$

---

# 40. Error Count 不等於 Error Risk

因此：

$$
\boxed{
N_E
\neq
\mathcal R_E.
}
$$

---

# 41. Error Risk

概念上：

$$
\boxed{
\mathcal R_E
=
\sum_e
P(e)
I(e)
L_{\mathrm{detect}}(e)
P_{\mathrm{prop}}(e).
}
$$

---

# 42. 模型可以少犯錯，但剩餘錯誤更昂貴

例如：

$$
P(E)\downarrow,
$$

但：

$$
\mathbb E[
I(E)\mid E
]
\uparrow.
$$

兩者可同時成立。

---

# 43. 這不代表強模型風險必然更高

總風險仍可能：

$$
\mathcal R_E\downarrow.
$$

本文只要求不能只看 error count。

---

# 44. Formal Reasoning 是理想觀察場

因為形式系統能把：

$$
\text{hidden obligation}
$$

顯式化。

---

# 45. Proof Correctness 與 Target Fidelity

既有 MPF 研究已提出：

$$
\boxed{
\text{Proof Formalization}
\neq
\text{Problem-Generation Formalization}.
}
$$

---

# 46. Kernel Accepted 不保證問對問題

可以：

$$
K(\Pi,T_f)=\mathrm{PASS},
$$

但：

$$
T_f
\neq
T_{\mathrm{intended}}.
$$

---

# 47. 這是典型高階 error

形式 proof 無錯，

錯的是：

$$
\boxed{
\text{target selection}.
}
$$

---

# 48. Premature Closure

若 AI 太早把：

$$
C_{\mathrm{source}}
$$

凍結成：

$$
C^\ast_{\mathrm{freeze}},
$$

可能遺失 proof-relevant semantics。

---

# 49. Quantifier Error

例如：

$$
\forall x\exists W_x
$$

被誤升格為：

$$
\exists W\forall x.
$$

這類錯誤表面 syntax 完全合法。

---

# 50. Witness-Dependency Error

同樣：

$$
\forall N\exists A_N
\not\Rightarrow
\exists A\forall N.
$$

若依賴被壓掉，formal proof target 本身已變。

---

# 51. FormalProofBench 的訊號

2026 FormalProofBench 對 advanced undergraduate / graduate Lean proofs 測試 frontier models。

最佳基礎模型約：

$$
33.5\%.
$$

---

# 52. 這說明 frontier formal reasoning 仍遠未飽和

但更重要的是 failure analysis。

較弱模型可能直接：

- proof incomplete；
- invalid Lean；
- search failure。

---

# 53. 更強模型可能卡在更深 obligation

例如：

- wrong lemma search；
- over-search；
- proof plan inefficiency；
- hidden dependency。

---

# 54. TheoremBench 的訊號

TheoremBench 2026 建立 main theorem + supporting subtheorem 結構。

---

# 55. 它看到一個有趣現象

現有 provers：

$$
\boxed{
\text{biased toward easy subtheorems}.
}
$$

---

# 56. 也常產生冗長 tactic trace

而不是：

$$
\boxed{
\text{compact global proof plan}.
}
$$

---

# 57. 這是一種 morphology signal

不是單純：

> 會 / 不會證明。

而是：

> proof search 如何組織。

---

# 58. Proof Existence 不等於 Proof Trust Architecture

既有 Proof Lattice 研究提出：

$$
\boxed{
\text{Proof Existence}
\neq
\text{Proof Trust Architecture}.
}
$$

---

# 59. 同一 proof 重跑十次不是十份獨立驗證

$$
10\times\text{same checker}
\neq
10\times\text{independent verification}.
$$

---

# 60. Verification Diversity

所以 error morphology 研究也需要：

- proof-path diversity；
- checker diversity；
- formalism diversity；
- assumption diversity；
- statement diversity。

---

# 61. Local Correctness 可能掩蓋 Shared Dependency Error

若多條 proof 都依賴：

$$
L^\ast,
$$

而：

$$
L^\ast
$$

錯，

表面 diversity 可能是假象。

---

# 62. 程式工程也有類似遷移

弱模型常犯：

- syntax；
- import；
- type；
- runtime。

---

# 63. 強模型可能更多剩餘錯誤在

- wrong architecture assumption；
- omitted migration path；
- race condition；
- hidden state；
- permissions；
- incomplete rollback；
- one unhandled branch。

---

# 64. Test Pass 不等於 Architecture Complete

$$
\boxed{
\text{local tests pass}
\not\Rightarrow
\text{global branch coverage}.
}
$$

---

# 65. Omission Error 是特殊高風險類

模型沒有說錯任何已輸出的句子。

它只是：

$$
\boxed{
\text{did not generate a necessary branch}.
}
$$

---

# 66. 為什麼 omission 難抓？

因為 verifier 需要知道：

> 應該存在什麼。

而不是只檢查：

> 已存在的東西是否正確。

---

# 67. Completeness Verifier

因此需要：

$$
V_{\mathrm{complete}}
$$

而不只是：

$$
V_{\mathrm{correct}}.
$$

---

# 68. Correctness 與 Completeness

$$
\boxed{
\text{Correctness}
\neq
\text{Completeness}.
}
$$

---

# 69. 長程 Agent 的錯誤更像 trajectory phenomenon

Agent 執行：

$$
s_0
\rightarrow
a_1
\rightarrow
s_1
\rightarrow
\cdots
\rightarrow
s_n.
$$

---

# 70. 最後失敗不代表最後一步錯

earliest decisive error：

$$
e_k
$$

可能早在：

$$
k\ll n
$$

時出現。

---

# 71. AgentRx 的方向

AgentRx 2026 將失敗 agent trajectory 標註 critical failure step 與 grounded failure category。

---

# 72. 這代表 failure analysis 正從 output-level 轉向 root-cause-level

$$
\boxed{
\text{Outcome Failure}
\rightarrow
\text{Trajectory Diagnosis}.
}
$$

---

# 73. LongRCA Bench

LongRCA Bench 2026 包含：

$$
1140
$$

條 failed trajectories，跨五個 domain。

---

# 74. Median trajectory 約 145 steps

這種長度下：

> 找最早決定性 root-cause step

本身已是困難任務。

---

# 75. Strongest baseline 仍難精確定位 root step

這直接說明：

$$
\boxed{
\text{Failure Attribution}
}
$$

是 long-horizon reliability 的獨立能力。

---

# 76. HORIZON 類工作

長程 task failure 會隨：

- dependency depth；
- horizon；
- state；
- planning；

改變。

---

# 77. YC-Bench 的錯誤也不是單一 step accuracy

其一年期 startup simulation 中可看到：

- over-parallelization；
- adversarial client miss；
- persistent-state use；

等結構差異。

---

# 78. Per-Step Correctness 不能推出 Trajectory Correctness

若每步：

$$
P(a_i\text{ correct})=p,
$$

不能只用：

$$
p^n
$$

完整描述長程失敗。

---

# 79. 因為錯誤會改變後續 state distribution

一個早期錯誤：

$$
e_k
$$

會改變：

$$
P(s_{k+1:n}).
$$

---

# 80. Error Becomes Premise

最危險情況之一：

$$
E_t
\rightarrow
\text{accepted state}
\rightarrow
E_{t+1}.
$$

---

# 81. Error Compounding

可寫：

$$
\boxed{
\epsilon_{t+1}
=
F(
\epsilon_t,
\Delta\epsilon_t,
R_t
).
}
$$

---

# 82. Repairability 變得比 First-Shot 更重要

若模型能自動：

- detect；
- localize；
- rollback；
- retry；

則 first-shot error 未必致命。

---

# 83. First-Shot Accuracy

$$
P_0
=
P(
\text{correct on first attempt}
).
$$

---

# 84. Eventual Correctness

$$
\boxed{
P_n
=
P(
\text{verified correct within }n\text{ repairs}
).
}
$$

---

# 85. Repair Gain

$$
\boxed{
G_R(n)
=
P_n-P_0.
}
$$

---

# 86. Repair Contraction

對 residual error：

$$
\epsilon_k,
$$

定義：

$$
\boxed{
\kappa_k
=
\frac{
\|\epsilon_{k+1}\|
}{
\|\epsilon_k\|
}.
}
$$

---

# 87. 若 $\kappa_k<1$

錯誤收斂。

---

# 88. 若 $\kappa_k\approx1$

repair 沒有效果。

---

# 89. 若 $\kappa_k>1$

修復反而擴散錯誤。

---

# 90. Error Migration Through Repair

有時修掉：

$$
E_3
$$

後，

剩下：

$$
E_6.
$$

這不是 repair 失敗，而是 deeper residual 被暴露。

---

# 91. Residual Error Frontier

本文定義：

$$
\boxed{
\mathcal F_E(A,R)
}
$$

表示在能力 $A$ 與 repair regime $R$ 下，仍然穩定存活的 error classes。

---

# 92. AI 越強，Residual Frontier 可能往上移

假說：

$$
\boxed{
\mathbb E[
L(E)
\mid
E\in\mathcal F_E
]
\uparrow.
}
$$

---

# 93. 但這是待驗證假說

它可能在某些 domain 不成立。

例如 stronger model 也可能突然消除某類 high-level error。

---

# 94. Error Morphology 可能非單調

模型世代：

$$
A_1\rightarrow A_2\rightarrow A_3
$$

可出現：

$$
E_5\downarrow,
\quad
E_7\uparrow,
\quad
E_8\downarrow.
$$

沒有必要形成單一直線。

---

# 95. Morphology Tensor

更合理：

$$
\boxed{
\mathbb M_E
=
[
P(E=e_i\mid A_j,T_k,R_l,V_m)
].
}
$$

---

# 96. 這是一個條件分布

不是模型永久 personality。

---

# 97. Error Detection Latency

定義：

$$
\boxed{
L_D(e)
=
t_{\mathrm{detected}}
-
t_{\mathrm{introduced}}.
}
$$

---

# 98. 高階錯誤常具有高 detection latency

因為它可能直到：

- integration；
- formalization；
- deployment；
- late proof obligation；

才暴露。

---

# 99. Early-Origin / Late-Detection

這是高 blast-radius error 的典型模式：

$$
t_{\mathrm{origin}}\ll t_{\mathrm{detect}}.
$$

---

# 100. Root-Cause Distance

定義：

$$
\boxed{
D_R
=
n_{\mathrm{failure}}
-
n_{\mathrm{root}}.
}
$$

---

# 101. $D_R$ 越大，debug 越難

尤其 multi-agent handoff 中，責任角色甚至可能已變。

---

# 102. Error Ownership

在 multi-agent system 中：

$$
E
$$

可能由：

- planner；
- worker；
- verifier；
- memory；
- tool；

產生。

---

# 103. Responsible Role

因此 failure taxonomy 應包含：

$$
\boxed{
\operatorname{Role}(E).
}
$$

---

# 104. Error Morphology Evaluation Protocol（EMEP）

本文提出標準流程。

---

# 105. EMEP Step 1：固定評測語境

記錄：

$$
A,T,R,V,B.
$$

---

# 106. Step 2：記錄 First Failure

分類：

$$
E_{\mathrm{first}}.
$$

---

# 107. Step 3：定位 Earliest Decisive Error

不是只記最後 crash。

---

# 108. Step 4：執行 Repair Loop

直到：

- verified success；
- budget exhausted；
- residual stable。

---

# 109. Step 5：記錄 Residual Error

$$
E_{\mathrm{res}}.
$$

---

# 110. Step 6：量 Detectability / Blast / Repair Cost

建立：

$$
\mathbf E.
$$

---

# 111. Step 7：做 Verifier Ablation

比較：

$$
V_0,V_1,\ldots,V_n.
$$

分離 detection shift。

---

# 112. Step 8：做 Task Matching

比較 same-task 與 frontier-normalized regime。

---

# 113. Error Morphology Matrix

輸出：

$$
\boxed{
M_{ij}
=
P(
E=e_i
\mid
A_j
).
}
$$

加上 task / verifier 維度。

---

# 114. Error Migration Distance

若有 error-layer 座標：

$$
L(e),
$$

可定義：

$$
\boxed{
\Delta L
=
\mathbb E[
L(E)\mid A_2
]
-
\mathbb E[
L(E)\mid A_1
].
}
$$

---

# 115. 但 $\Delta L>0$ 不自動表示更危險

仍要看：

$$
\mathcal R_E.
$$

---

# 116. Error Severity–Detectability Tradeoff

高階模型理想情況：

$$
P(E)\downarrow
$$

且：

$$
D_{\mathrm{detect}}\uparrow.
$$

這是雙重進步。

---

# 117. 危險情況

若：

$$
P(E)\downarrow
$$

但：

$$
D_{\mathrm{detect}}\downarrow
$$

且：

$$
B(E)\uparrow,
$$

則剩餘錯誤更難治理。

---

# 118. Verification Architecture 因此必須跟模型能力一起升級

$$
\boxed{
C_A\uparrow
\Rightarrow
C_V\uparrow
}
$$

是工程目標，不是自然必然。

---

# 119. Verifier Lag

若：

$$
C_A>C_V,
$$

可能形成：

$$
\boxed{
\text{Verification Lag}.
}
$$

---

# 120. 這與 B03 Visibility 問題直接相連

若 verifier 看不到 error：

$$
\chi_E\downarrow.
$$

---

# 121. Error Visibility Threshold

本文可定義：

$$
\boxed{
\chi_E(
e,
V,O
)
}
$$

表示錯誤被識別的概率。

---

# 122. Model Capability 變強也可能降低錯誤可見性

因為輸出更流暢、更局部一致。

所以：

$$
\boxed{
\text{Plausibility}
\uparrow
\not\Rightarrow
\text{Correctness}
\uparrow
}
$$

對個別 residual output 仍成立。

---

# 123. 但整體 correctness 仍可同時提高

本文不是說 stronger models 更會 hallucinate。

而是：

> 剩下的 hallucination / omission 可能更難由表面 fluency 發現。

---

# 124. Human Coupler 的角色也會變

舊模型時，人類常修：

- syntax；
- direct facts；
- obvious mistakes。

---

# 125. 新模型時，人類可能更多修

- definition；
- scope；
- boundary；
- proof obligation；
- architecture completeness；
- experiment interpretation。

---

# 126. 這就是 Coupling Skill Migration

定義：

$$
\boxed{
H_{\mathrm{repair}}(t)
}
$$

所需技能也可能向 higher meta-level 移動。

---

# 127. B05 的前置

若所需 repair / activation skill 越高階，

能有效耦合的使用者比例可能改變。

這會在 B05 處理。

---

# 128. B06 的前置

B06 將把：

- problem construction；
- method；
- verification；
- repair；

正式放進 coupling state space。

---

# 129. B07 的現實觀測價值

高能力專家與 AI 的 frontier work 可觀察：

> 錯誤究竟已從 basic mistakes 移去哪裡。

---

# 130. B08 的長期問題

若 AI 能自己：

- detect omissions；
- identify boundary mismatch；
- formalize obligations；
- audit architecture；

則人類 repair role 可能下降。

---

# 131. 可證偽命題一

若 error morphology 不隨模型能力改變，

則 matched-task regime 下：

$$
\mathcal M_E(A_1)
\approx
\mathcal M_E(A_2).
$$

---

# 132. 可證偽命題二

若 observed shift 主要來自 task selection，

則同一任務比較中：

$$
\Delta L\approx0,
$$

而 frontier-normalized comparison 才有差。

---

# 133. 可證偽命題三

若 observed shift 主要來自 better verification，

則固定 model / task、只提升 verifier：

$$
N_{\mathrm{high-level\ detected}}
\uparrow.
$$

---

# 134. 可證偽命題四

若 stronger model repairability 提升，

則：

$$
G_R(n)\uparrow
$$

且：

$$
\kappa\downarrow.
$$

---

# 135. 可證偽命題五

若 omission 成為重要 residual class，

則 completeness-oriented verifier 的 marginal detection gain 應高於 syntax-oriented verifier。

---

# 136. 可觀測預測

本文提出九個預測：

1. frontier models 的 syntax / direct execution error rate 將持續低於舊世代。
2. residual failures 會更多集中於 condition omission、boundary mismatch、formal obligations、architecture completeness 與 long-horizon state errors。
3. first-shot correctness 的邊際價值會逐步讓位給 eventual verified correctness 與 repair contraction。
4. formal verification 會把部分自然語言中不可見的 proof obligations 顯影。
5. software Agent evaluation 會增加 completeness、branch coverage、rollback、state consistency 與 trajectory root-cause metrics。
6. long-horizon Agent failure taxonomy 會從 final-outcome labels 走向 earliest decisive root cause。
7. stronger models 的 remaining errors 將需要更專業 verifier 才能可靠辨識。
8. human–AI coupling 中人類修正工作會從低階 syntax correction 向 definition、boundary、architecture、verification 移動。
9. 當 AI self-verification 與 meta-repair 成熟後，這些高階 residual classes 也會再次縮小，形成新的 error frontier。

---

# 137. 與既有 EveMissLab 研究的關係

## 137.1 CFATC-B01 至 B03

B01：

$$
C_{\mathrm{latent}}
\neq
C_{\mathrm{realized}}.
$$

B02：

$$
\text{coupling}
\rightarrow
\text{frontier activation}.
$$

B03：

$$
C_{\mathrm{realized}}
\neq
C_{\mathrm{visible}}.
$$

B04 增加：

$$
\boxed{
\text{higher capability}
\neq
\text{same residual error distribution}.
}
$$

## 137.2 Mathematical Problem Formalization

既有 MPF 研究提出：

$$
\text{Proof Formalization}
\neq
\text{Problem-Generation Formalization}
$$

以及 target fidelity / premature closure 問題。

B04 將其視為典型高階 error morphology。

## 137.3 Multi-Proof / Proof Lattice

既有研究提出：

$$
\text{Proof Existence}
\neq
\text{Proof Trust Architecture}.
$$

B04 將 verifier diversity、shared dependency 與 statement fidelity 納入 error detectability。

## 137.4 LHCF Cognitive Resistance

LHCF 已指出：

$$
\text{local comprehension}
\not\Rightarrow
\text{global theory reconstruction}.
$$

B04 將局部—全域差距轉成錯誤分布問題。

## 137.5 APR / Differential Reobservation

APR 的差分重觀察思想提供另一個 repair 接口：

> 不必每次重算全部狀態，而應針對變化與殘差重新觀察。

B04 的 residual-error monitoring 與此相容。

---

# 138. 外部研究支點

1. Ravi, N. et al., **FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?**, ICLR 2026.
2. Pham, Q. V. et al., **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics**, 2026.
3. Barke, S. et al., **AgentRx: Diagnosing AI Agent Failures from Execution Trajectories**, Microsoft Research, 2026.
4. Zhang, Y. et al., **LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures**, 2026.
5. Wang, X. J. et al., **The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break (HORIZON)**, 2026.
6. He, M. et al., **YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution**, 2026.
7. OpenAI, **Safety and Alignment in an Era of Long-Horizon Models**, 2026.

這些外部研究不直接提出本文的 Error Morphology Shift 理論；它們分別提供 formal-proof residual、proof-structure bias、trajectory diagnosis、root-cause localization 與 long-horizon failure decomposition 的實證支點。

---

# 139. 結論

本文提出：

$$
\boxed{
\text{Error Morphology Shift}
}
$$

作為 frontier AI reliability 的核心研究問題之一。

真正需要測的不是只有：

$$
P(\mathrm{error}).
$$

還包括：

$$
\boxed{
P(
E=e
\mid
A,T,R,V
).
}
$$

因為 AI 變強後，最常見的情況可能不是：

> 錯誤全部消失。

而是：

> **低階錯誤先被消除，剩下的錯誤往更長依賴、更高抽象、更難驗證的 residual frontier 集中。**

但這個命題只有在排除：

$$
\boxed{
\text{Task-Selection Shift}
}
$$

與：

$$
\boxed{
\text{Detection Shift}
}
$$

後，才有資格被稱為真正 model morphology shift。

所以本文的最終方法論是：

$$
\boxed{
\text{Same Task}
+
\text{Frontier-Normalized Task}
+
\text{Verifier Ablation}
+
\text{Trajectory Root Cause}
+
\text{Repair Analysis}.
}
$$

而 reliability 的目標也應從：

$$
\boxed{
\text{Never Make a Mistake}
}
$$

轉成更現實的：

$$
\boxed{
\text{Make Fewer Errors}
+
\text{Detect Earlier}
+
\text{Repair Reliably}
+
\text{Prevent Propagation}
+
\text{Expose Residual Boundaries}.
}
$$

CFATC 至此形成：

$$
\boxed{
\text{Latent}
\rightarrow
\text{Activated}
\rightarrow
\text{Visible}
\rightarrow
\text{Residual Error Morphology}.
}
$$

下一篇 CFATC-B05 將正式處理本系列最具爭議性的猜想之一：

$$
\boxed{
\text{Tail-Domain Contraction Hypothesis}.
}
$$

也就是：

> **AI 越強，雖然能使用 AI 的人越多，但真正能反覆把它推入最高能力尾端的人類比例，是否反而可能下降？**

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
