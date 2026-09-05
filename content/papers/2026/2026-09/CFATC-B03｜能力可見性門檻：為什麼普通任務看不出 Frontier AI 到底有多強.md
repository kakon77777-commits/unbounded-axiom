# CFATC-B03｜能力可見性門檻：為什麼普通任務看不出 Frontier AI 到底有多強
## Capability Visibility Threshold: Why Ordinary Tasks Fail to Reveal Frontier AI Capability

**系列：** Conditional Frontier Activation and Human–AI Tail Coupling（CFATC）  
**系列中文名：** 條件式前沿觸發與人機尾端耦合系列  
**篇次：** Paper 03 / 08  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** AI 能力可見性／Benchmark Methodology／Frontier Evaluation／人機耦合觀測論

---

## 摘要

CFATC-B01 已提出：

$$
\boxed{
C_{\mathrm{latent}}
\neq
C_{\mathrm{realized}}
}
$$

CFATC-B02 進一步提出 Conditional Frontier Activation：

$$
\boxed{
p_F(A\mid\Theta_F)
=
P(
C_{\mathrm{realized}}
\in
\mathcal C_{\mathrm{tail}}
\mid
A,\Theta_F
).
}
$$

然而，即使 AI 已具有某種 latent frontier capability，而且在適當耦合條件下確實可被觸發，仍然存在第三個問題：

> **觀察者是否看得見？**

本文提出：

$$
\boxed{
\text{Capability}
\neq
\text{Capability Visibility}.
}
$$

模型能力可以存在，但如果任務太簡單、評測已飽和、互動模式過窄、時間跨度太短、使用者能力不足、驗證器解析度不夠，則高階能力可能完全不出現在觀察面上。

本文將 **Capability Visibility（能力可見性）** 定義為：

$$
\boxed{
\chi(
A,
c,
T,
R,
O,
E
)
\in[0,1],
}
$$

其中：

- $A$：被測 AI 系統；
- $c$：欲觀察的能力；
- $T$：任務族；
- $R$：interaction / evaluation regime；
- $O$：observer / evaluator；
- $E$：environment，包括工具、時間、記憶、verifier 與資源。

當：

$$
\chi
<
\tau_{\mathrm{vis}},
$$

則即使：

$$
c(A)=1,
$$

觀察者也可能得到：

$$
\boxed{
\operatorname{Observed}_O(c)=0.
}
$$

本文將造成低可見性的來源拆成六類：

$$
\boxed{
\text{Task Ceiling}
+
\text{Regime Blindness}
+
\text{Temporal Truncation}
+
\text{Observer Limitation}
+
\text{Verification Resolution}
+
\text{Domain Mismatch}.
}
$$

第一，若任務難度遠低於兩個模型的能力：

$$
D(T)
\ll
C(A_1),
C(A_2),
$$

則兩者都接近滿分：

$$
P_{\mathrm{success}}(A_1)
\approx
P_{\mathrm{success}}(A_2)
\approx1.
$$

此時模型能力差距仍存在，但 benchmark discrimination：

$$
\boxed{
\Delta_{\mathrm{obs}}
\rightarrow0.
}
$$

第二，如果 benchmark 只測：

$$
Q\rightarrow A,
$$

它看不到：

$$
W\rightarrow Q,
$$

也看不到問題生成、frame switching、長期 state maintenance、方法重構、跨域 attention transfer 等更高階能力。

第三，短任務無法揭示需要多輪修復、跨 session memory、長期 wake condition 或 trajectory-level coherence 才能出現的能力。

第四，即使 AI 產生真正 frontier output，若 observer 無法判斷其價值、錯誤或新穎性，能力仍可能不可見。本文因此引入：

$$
\boxed{
C_O
}
$$

表示 observer competence。

第五，若 evaluator 只能判斷 final answer，卻無法檢查 proof、test、trajectory、state delta 或 external consequence，則高階能力與高階錯誤都會被壓縮成同一個表面分數。

第六，不同領域的 capability frontier 極不均勻。METR 的 2026 time-horizon work 明確指出不同 domain 的 time horizon 可以相差數個數量級，且其主要 task suite 集中於 software engineering、machine learning 與 cybersecurity。因此：

$$
\boxed{
\text{Visible in Domain }D_1
\not\Rightarrow
\text{Visible in Domain }D_2.
}
$$

本文提出 **Capability Visibility Threshold（CVT）**：

$$
\boxed{
D_{\mathrm{task}}
\geq
D_{\mathrm{vis}}(
A_1,A_2,c,R,O
)
}
$$

只有當任務進入足夠有區辨力的區間，能力差異才較可能穩定可見。

但如果任務過難：

$$
D_{\mathrm{task}}
\gg
C(A_1),C(A_2),
$$

兩者又會共同失敗：

$$
P_{\mathrm{success}}
\approx0.
$$

所以真正理想的 frontier evaluation 並不是「越難越好」，而是存在一個 **Diagnostic Visibility Band（診斷可見帶）**：

$$
\boxed{
D_{\mathrm{low}}
<
D(T)
<
D_{\mathrm{high}}.
}
$$

在這個區域中，模型仍具有非零成功率，但能力差距尚未被 ceiling 或 floor 壓扁。

本文將此寫成：

$$
\boxed{
\mathcal B_{\mathrm{vis}}
=
\{
T:
\epsilon
<
P_A(\mathrm{success}\mid T)
<
1-\epsilon
\}.
}
$$

對多模型比較，則要求 task family 對模型排序與失敗形態具有足夠 discrimination。

2026 年 Stanford AI Index 已直接指出，frontier capability 正在超越 benchmark 設計速度：Humanity’s Last Exam 一年內 frontier model 成績提升約 30 個百分點，而原本預期可維持多年挑戰性的評測在數月內即可能快速失去區辨力。METR 亦指出其 time-horizon benchmark 對現代 frontier models 正接近飽和，測量誤差與分析假設敏感度因此上升，且 16 小時以上的 time horizon 目前無法可靠估計。這些現象共同支持：

$$
\boxed{
\text{Benchmark Half-Life}
}
$$

正在成為 frontier AI evaluation 的實際問題。

本文定義 benchmark diagnostic half-life：

$$
\boxed{
T_{1/2}^{B}
=
\inf
\{
\Delta t:
\operatorname{Disc}(B,t+\Delta t)
\leq
\tfrac12
\operatorname{Disc}(B,t)
\}.
}
$$

其中 $\operatorname{Disc}$ 表示 benchmark 對 frontier models 的區辨能力。

本文也提出一個更強命題：

$$
\boxed{
\text{As frontier AI improves, capability visibility may migrate upward in task meta-level}.
}
$$

也就是，以前足以區分模型的能力可能是：

- syntax；
- factual QA；
- short coding；
- direct reasoning；

未來則逐步上移到：

- long-horizon coherence；
- problem formulation；
- representation change；
- verification；
- recursive repair；
- frame generation；
- autonomous frontier discovery。

因此一般使用者可能真實感受到：

> 「模型看起來都差不多。」

但這個觀察只能推出：

$$
\boxed{
\text{models are similar inside the user's visibility band}.
}
$$

不能推出：

$$
\boxed{
\text{models have equal latent or frontier capability}.
}
$$

本文最後提出 **Visibility-Aware Frontier Evaluation（VAFE）**，要求 frontier 評測同時掃描：

$$
\boxed{
\text{Task Difficulty}
\times
\text{Time Horizon}
\times
\text{Interaction Regime}
\times
\text{Observer Competence}
\times
\text{Verification Depth}.
}
$$

CFATC 的研究因此形成第三條鏈：

$$
\boxed{
\text{Latent Capability}
\rightarrow
\text{Activated Capability}
\rightarrow
\text{Visible Capability}
\rightarrow
\text{Recognized Capability}.
}
$$

能力「看不見」不是證明能力不存在，而是要求我們先檢查：

> **是不是觀察器本身已經落後於被觀察系統？**

**關鍵詞：** Capability Visibility Threshold、Benchmark Saturation、Frontier Evaluation、Ceiling Effect、Floor Effect、Observer Competence、Long-Horizon Evaluation、Diagnostic Band、Benchmark Half-Life、Human–AI Coupling

---

# 1. 問題：模型明明變強，為什麼很多人感覺「差不多」？

假設：

$$
C(A_2)
>
C(A_1).
$$

但普通使用者的任務集合：

$$
\mathcal T_U
$$

全部滿足：

$$
D(T)
\ll
C(A_1).
$$

那麼：

$$
P(A_1\text{ succeeds})
\approx
P(A_2\text{ succeeds})
\approx1.
$$

使用者自然會得到：

$$
\boxed{
A_1
\approx
A_2
}
$$

的經驗。

---

# 2. 這個經驗不一定錯

對：

$$
\mathcal T_U
$$

而言，它可能完全正確。

問題只出在把：

$$
A_1\approx A_2
\mid
\mathcal T_U
$$

外推成：

$$
A_1\approx A_2
\quad
\forall T.
$$

---

# 3. Capability Visibility

本文定義：

$$
\boxed{
\chi(
A,
c,
T,
R,
O,
E
)
}
$$

表示能力 $c$ 在特定 task、regime、observer 與 environment 下被可靠觀察的程度。

---

# 4. Visibility 不是 Capability

因此：

$$
\boxed{
C(A)
\neq
\chi(A).
}
$$

高能力可以低可見。

低能力也可能因 demo 設計而高可見。

---

# 5. Demo Visibility

一個精心挑選的 demo 可以：

$$
\chi_{\mathrm{demo}}\gg0
$$

即使：

$$
R_{\mathrm{robust}}
\ll1.
$$

所以：

$$
\boxed{
\text{Demonstrability}
\neq
\text{Robust Capability}.
}
$$

---

# 6. 第一個可見性障礙：Ceiling Effect

若任務太簡單：

$$
D(T)
<
D_{\mathrm{low}},
$$

則：

$$
P_{\mathrm{success}}
\rightarrow1.
$$

模型差異被壓縮。

---

# 7. 第二個障礙：Floor Effect

若任務太難：

$$
D(T)
>
D_{\mathrm{high}},
$$

則：

$$
P_{\mathrm{success}}
\rightarrow0.
$$

所有模型都失敗。

---

# 8. 因此越難不一定越好

真正 evaluation 需要找：

$$
\boxed{
\text{Diagnostic Visibility Band}.
}
$$

---

# 9. Visibility Band

定義：

$$
\boxed{
\mathcal B_{\mathrm{vis}}(A)
=
\{
T:
\epsilon
<
P(
\mathrm{success}\mid A,T
)
<
1-\epsilon
\}.
}
$$

---

# 10. 多模型比較的可見帶

對：

$$
A_1,A_2,\ldots,A_n,
$$

理想 task family 應讓模型成功率：

- 不全部為 1；
- 不全部為 0；
- 有穩定排序或可解釋 failure difference。

---

# 11. Visibility Threshold

對能力 $c$，定義：

$$
\boxed{
D_{\mathrm{vis}}(c)
}
$$

為 task difficulty 進入可辨識該能力區域的最低門檻。

---

# 12. Task Difficulty 不是單一尺度

更完整：

$$
\mathbf D(T)
=
(
D_{\mathrm{depth}},
D_{\mathrm{horizon}},
D_{\mathrm{ambiguity}},
D_{\mathrm{tools}},
D_{\mathrm{verification}},
D_{\mathrm{open}}
).
$$

---

# 13. Reasoning Depth

有些能力只有在多步推理中可見。

---

# 14. Time Horizon

有些能力需要：

$$
t\gg1
$$

才出現，例如：

- persistence；
- recovery；
- delayed planning；
- long-run consistency。

---

# 15. Ambiguity

有些 frontier 能力表現在：

> 問題本身不完整時，AI 是否先重構問題。

---

# 16. Tool Demand

有些能力只有在：

$$
\text{model}
+
\text{tools}
$$

的 regime 下可見。

---

# 17. Verification Demand

如果任務不要求證明、測試或 external evidence，很多高階 verifier / repair 能力不會被觸發。

---

# 18. Open-World Demand

如果所有問題與評分都預先定義：

$$
Q\rightarrow A,
$$

就看不到：

$$
W\rightarrow Q.
$$

---

# 19. Regime Blindness

同一 AI 在：

- chat；
- agent；
- tool-using；
- persistent runtime；

中是不同 system regime。

所以：

$$
\boxed{
\chi(A,c,T,R_1)
\neq
\chi(A,c,T,R_2).
}
$$

---

# 20. Chat Benchmark 可能看不到 Agent Capability

如果 benchmark 每題：

- reset context；
- 禁工具；
- 無記憶；
- 無多輪 repair；

則：

$$
\boxed{
\text{Agentic Capability}
}
$$

被結構性消除。

---

# 21. Agent Benchmark 也可能看不到 Metacognition

如果 task 已經明確：

- goal；
- method；
- tool；
- verifier；

則 AI 不需要：

$$
\boxed{
\text{select its own cognitive strategy}.
}
$$

---

# 22. Meta-Level Visibility

因此越高階能力，越需要：

$$
\boxed{
\text{less pre-specified task structure}.
}
$$

---

# 23. LHCF 的 Solver 問題

既有 LHCF 已提出：

$$
S_1=\text{Problem Solver},
$$

$$
S_2=\text{Theory Builder},
$$

$$
S_3=\text{Problem Generator},
$$

$$
S_4=\text{Frame Generator},
$$

$$
S_5=\text{Frontier Regenerator}.
$$

---

# 24. Solver Benchmark 只能穩定觀察 $S_1$

如果 benchmark 給定：

$$
Q,
\mathcal R,
G,
$$

則高階：

$$
S_3,S_4,S_5
$$

可能根本沒有被要求。

---

# 25. 所以沒有出現，不代表沒有

$$
\boxed{
\text{Not Invoked}
\neq
\text{Not Possessed}.
}
$$

---

# 26. 第三個障礙：Temporal Truncation

如果評測只有：

$$
5\text{ minutes},
$$

就無法觀察需要：

$$
5\text{ hours}
$$

才出現的 failure / recovery pattern。

---

# 27. Long-Horizon Capability

有些 AI 在短任務很穩，

但長任務出現：

- drift；
- state loss；
- goal substitution；
- compounding error。

---

# 28. 反過來也可能存在

模型短任務不突出，

但長任務：

- better recovery；
- better planning；
- better self-check；

差異放大。

---

# 29. 因此時間本身是觀察器

$$
\boxed{
\chi
=
\chi(\Delta t).
}
$$

---

# 30. METR Time Horizon

METR 將 task difficulty 映射到：

> human expert completion time。

這提供一個可解釋的 long-horizon capability axis。

---

# 31. 但 Time Horizon 不是自治工作時間

METR 自己明確指出：

$$
\boxed{
\text{Time Horizon}
\neq
\text{time AI can work independently}.
}
$$

它是基於人類完成時間標定的 task difficulty measure。

---

# 32. Domain Limitation

METR 目前主要 task suite 來自：

- software engineering；
- ML；
- cybersecurity。

因此：

$$
\boxed{
H_T(D_1)
\neq
H_T(D_2).
}
$$

---

# 33. 不同領域可差數個數量級

這進一步說明：

$$
\boxed{
\text{One capability metric}
\neq
\text{universal visibility metric}.
}
$$

---

# 34. 第四個障礙：Observer Limitation

即使 AI 產生正確 frontier result，

observer 也可能看不懂。

---

# 35. Observer Competence

定義：

$$
\boxed{
C_O(c,T)
}
$$

表示 observer 對能力 $c$ 與任務 $T$ 的評判能力。

---

# 36. 如果 Observer Competence 太低

可能：

$$
C_O
<
C_{\mathrm{output}}.
$$

此時：

- 正確結果被當錯；
- 錯誤結果被當對；
- 新方法被當成胡說。

---

# 37. Recognition Bottleneck

所以：

$$
\boxed{
\text{Capability Visibility}
\leq
\text{Evaluator Resolution}.
}
$$

---

# 38. Human Expert Evaluation

frontier 數學、科學、程式與法律問題 often require domain experts。

一般 crowd label：

$$
L_{\mathrm{crowd}}
$$

可能沒有足夠解析度。

---

# 39. AI-as-Judge 也有同樣問題

如果 evaluator model：

$$
J
$$

比 candidate：

$$
A
$$

弱，

則：

$$
\boxed{
\text{Judge Capability Ceiling}.
}
$$

---

# 40. Stronger Judge 仍不保證正確

因為：

- shared blind spot；
- same training distribution；
- style preference；
- reward hacking；

仍可能存在。

---

# 41. 第五個障礙：Verification Resolution

只評 final answer：

$$
y.
$$

會丟失：

- proof；
- process；
- repair；
- test；
- uncertainty。

---

# 42. Outcome-Only Eval

可寫：

$$
E_{\mathrm{out}}(y).
$$

---

# 43. Trajectory Eval

更高階：

$$
\boxed{
E_{\mathrm{traj}}
(
s_0,a_1,s_1,\ldots,a_n,s_n
).
}
$$

---

# 44. 為什麼 trajectory 重要？

同樣 final success：

$$
y=1
$$

可能來自：

- robust method；
- luck；
- reward hack；
- hidden leakage。

---

# 45. OpenAI 2026 Long-Horizon Case

OpenAI 公開描述，在有限內部長程模型部署中觀察到 pre-deployment eval 未捕捉的新 failure modes，之後加入 trajectory-level monitoring。

這支持：

$$
\boxed{
\text{Deployment Trajectory}
\neq
\text{Static Eval Snapshot}.
}
$$

---

# 46. 第六個障礙：Domain Mismatch

若能力是：

$$
c_{\mathrm{math}},
$$

用 coding benchmark 測不到。

這很明顯，但 frontier evaluation 仍常犯更細的版本。

---

# 47. Subdomain Mismatch

例如：

$$
\text{coding}
$$

內還有：

- greenfield；
- legacy reconstruction；
- debugging；
- architecture；
- formal verification。

能力不均勻。

---

# 48. Jagged Frontier

因此：

$$
\boxed{
C(A,D)
}
$$

是一個崎嶇曲面。

不是平滑 IQ 軸。

---

# 49. Capability Visibility Surface

本文提出：

$$
\boxed{
\mathcal V_A
=
\chi(
\mathbf D,
R,
O,
E
).
}
$$

---

# 50. Visibility Ridge

存在一些 task region：

$$
\boxed{
\text{Visibility Ridge}
}
$$

最能放大模型差異。

---

# 51. Visibility Desert

也存在：

$$
\boxed{
\text{Visibility Desert}
}
$$

其中模型能力不同但觀察表現接近。

---

# 52. Ceiling Desert

第一種：

$$
P\approx1.
$$

---

# 53. Floor Desert

第二種：

$$
P\approx0.
$$

---

# 54. Regime Desert

第三種：

> benchmark 根本沒有給能力發生的條件。

---

# 55. Observer Desert

第四種：

> 沒有足夠 evaluator 能辨識結果。

---

# 56. Benchmark Saturation

令 benchmark：

$$
B.
$$

若 frontier models：

$$
S(A_i,B)
\rightarrow
S_{\max},
$$

則：

$$
\boxed{
\operatorname{Disc}(B)\rightarrow0.
}
$$

---

# 57. Diagnostic Discrimination

定義：

$$
\boxed{
\operatorname{Disc}(B,t)
=
\operatorname{Var}_{A\in F_t}
[
S(A,B)
]
}
$$

作為最簡概念量。

---

# 58. 這個定義不是唯一方法

實務上還可以使用：

- rank stability；
- information gain；
- item response theory；
- pairwise separation。

本文只需要一個抽象。

---

# 59. Benchmark Half-Life

定義：

$$
\boxed{
T_{1/2}^{B}
=
\inf
\{
\Delta t:
\operatorname{Disc}(B,t+\Delta t)
\leq
\tfrac12
\operatorname{Disc}(B,t)
\}.
}
$$

---

# 60. 2026 AI Index 的現實訊號

Stanford AI Index 2026 指出：

> frontier capability 正跑得比 benchmark 設計更快。

Humanity’s Last Exam 一年內 frontier score 提升約 30 percentage points。

---

# 61. Benchmark 原本預計很難

但：

$$
\boxed{
\text{designed-to-last-years}
\rightarrow
\text{months-scale saturation}
}
$$

正在出現。

---

# 62. 這不是 benchmark 沒價值

而是：

$$
\boxed{
\text{benchmark is a moving measurement instrument}.
}
$$

---

# 63. METR 也觀察到 Saturation

METR 2026 明確指出其 time-horizon suite 正接近 saturation，導致：

- error bars widening；
- point estimate sensitivity；
- longer task shortage。

---

# 64. 16 小時以上目前難以可靠測量

METR 公開頁明示：

$$
\boxed{
H_{50}>16\text{h}
}
$$

的測量目前不可靠。

---

# 65. 這是 Instrument Ceiling

不是：

$$
\boxed{
\text{AI incapable above 16h}.
}
$$

而是：

$$
\boxed{
\text{instrument cannot resolve reliably above 16h}.
}
$$

---

# 66. Measurement Ceiling 與 Capability Ceiling 必須分開

$$
\boxed{
C_{\mathrm{instrument}}
\neq
C_{\mathrm{system}}.
}
$$

---

# 67. Frontier Model 會逃出 Benchmark Window

當：

$$
C_A(t)
\uparrow
$$

固定 benchmark：

$$
B
$$

最終會落到 ceiling region。

---

# 68. 因此評測必須動態更新

$$
B_t
\rightarrow
B_{t+1}.
$$

---

# 69. 但 benchmark 更新也有成本

建立 frontier-quality task 需要：

- expert time；
- verification；
- contamination control；
- baselining。

---

# 70. Evaluation Lag

定義：

$$
\boxed{
\tau_E
=
T_{\mathrm{new\ diagnostic}}
-
T_{\mathrm{capability\ shift}}.
}
$$

---

# 71. 當 $\tau_E>0$

存在一段：

> capability 已進步，但公開測量仍看不清。

---

# 72. 一般使用者的 Evaluation Lag 更大

一般人不會每天更新自己的 task suite。

所以：

$$
\tau_U
\gg
\tau_E
$$

可能成立。

---

# 73. User Visibility Band

每位使用者其實都有：

$$
\boxed{
\mathcal B_{\mathrm{user}}(u).
}
$$

---

# 74. 如果兩模型都超出使用者需求

則：

$$
A_1\approx A_2
$$

對使用者而言是真實效用等價。

---

# 75. 但 Product Utility 等價不等於 Frontier Capability 等價

$$
\boxed{
U_u(A_1)
\approx
U_u(A_2)
\not\Rightarrow
C_{\mathrm{tail}}(A_1)
=
C_{\mathrm{tail}}(A_2).
}
$$

---

# 76. 這能解釋很多模型爭論

兩個人可能都沒說謊：

- 一人說「新版強很多」；
- 一人說「完全沒差」。

因為其：

$$
\mathcal B_{\mathrm{user}}
$$

不同。

---

# 77. Coupling Visibility

B02 已提出 CFA。

如果使用者從不提供：

- method；
- verifier；
- long horizon；
- repair；

則：

$$
p_F
$$

很低。

---

# 78. 因此能力尾端可能對大多數使用者是不可見的

即：

$$
\boxed{
\mathcal C_{\mathrm{tail}}
\cap
\mathcal B_{\mathrm{user}}
=
\varnothing.
}
$$

---

# 79. Capability Activation 與 Visibility 是兩道不同門

即使：

$$
\operatorname{Activate}=1,
$$

也可能：

$$
\operatorname{Visible}=0
$$

因為 evaluator 看不懂。

---

# 80. 所以完整鏈是

$$
\boxed{
\text{Latent}
\rightarrow
\text{Activated}
\rightarrow
\text{Visible}
\rightarrow
\text{Recognized}.
}
$$

---

# 81. Observed Capability

本文定義：

$$
\boxed{
C_{\mathrm{obs}}
=
\Pi_O(
C_{\mathrm{realized}},
R,
E
).
}
$$

其中 $\Pi_O$ 是 observer projection。

---

# 82. Projection 可以丟失能力差異

如果：

$$
\ker\Pi_O
\neq0,
$$

部分能力落入 observer blind spot。

---

# 83. 這直接接回 GIRA-A02

Representation / observer dependence：

$$
\boxed{
\text{observer-relative representation}
\neq
\text{arbitrary truth}.
}
$$

---

# 84. 高階能力可見性可能需要高階 Observer

例如 theorem proof：

$$
C_O^{\mathrm{math}}
$$

不足時，

一般人無法區分：

- valid theorem；
- plausible nonsense。

---

# 85. Expert Observer 仍有限

真正 frontier 可能：

$$
C_{\mathrm{output}}
>
C_O^{\max}.
$$

此時需要：

- formal verifier；
- experiment；
- collective review。

---

# 86. Verification as Visibility Amplifier

因此：

$$
\boxed{
V
\uparrow
\Rightarrow
\chi
\uparrow
}
$$

在許多 frontier tasks 可能成立。

---

# 87. Formal Proof 是極端案例

如果 theorem 被 Lean 驗證：

$$
V_{\mathrm{formal}}=1,
$$

observer 不必自己重做完整 proof 才知道：

> 至少形式系統接受。

---

# 88. 但 Formal Verification 也不等於所有語義正確

仍需檢查：

- theorem statement；
- assumptions；
- formalization fidelity。

---

# 89. Skill-Formation Visibility

AI 不只影響輸出，也影響人類能力。

這種效應在一次 task benchmark 幾乎不可見。

---

# 90. Longitudinal Human–AI Eval

需要：

$$
H_t
\rightarrow
H_{t+n}.
$$

測：

- learning；
- hollowing；
- calibration；
- coupling growth。

---

# 91. Relation-State Visibility

共享歷史：

$$
\mathcal R_{HA}
$$

的價值也需要多次互動才能可見。

---

# 92. 一次性 Benchmark 看不到 Relational Capital

所以：

$$
\boxed{
\text{Session Reset}
}
$$

會刻意刪除某些真實能力維度。

---

# 93. 這有時是好事

如果我們只想測：

$$
C_{\mathrm{base}},
$$

reset 很合理。

---

# 94. 但不能把 Base Capability Benchmark 當完整系統能力

$$
\boxed{
\text{Base Model Eval}
\neq
\text{Coupled System Eval}.
}
$$

---

# 95. Visibility-Aware Frontier Evaluation（VAFE）

本文提出：

$$
\boxed{
\mathrm{VAFE}
=
(
\mathcal T,
\mathcal H,
\mathcal R,
\mathcal O,
\mathcal V
).
}
$$

---

# 96. $\mathcal T$：Task Difficulty Sweep

從：

$$
D_{\mathrm{low}}
\rightarrow
D_{\mathrm{high}}.
$$

---

# 97. $\mathcal H$：Time-Horizon Sweep

從：

- minutes；
- hours；
- days；
- persistent multi-session。

---

# 98. $\mathcal R$：Interaction-Regime Sweep

比較：

- first-shot；
- expert coupled；
- tool-enabled；
- verifier-enabled；
- autonomous agent。

---

# 99. $\mathcal O$：Observer Sweep

比較：

- automatic scorer；
- general human；
- expert human；
- stronger AI judge；
- formal verifier。

---

# 100. $\mathcal V$：Verification Depth

從：

- final answer；
- output evidence；
- process trace；
- formal / empirical certification。

---

# 101. Visibility Tensor

最終可得到：

$$
\boxed{
\mathbb V_A
=
[
\chi_{d,h,r,o,v}
].
}
$$

---

# 102. 這比單一 benchmark 更接近能力形狀

模型可能在：

$$
(d_1,h_1,r_1)
$$

不可見，

但在：

$$
(d_2,h_2,r_2)
$$

非常清楚。

---

# 103. Visibility Robustness

定義：

$$
\boxed{
R_{\mathrm{vis}}
=
P(
\chi>\tau_{\mathrm{vis}}
\mid
T\sim\mathcal T_F
).
}
$$

---

# 104. Tail Visibility Ratio

定義：

$$
\boxed{
\rho_{\mathrm{tail-vis}}
=
\frac{
\mu(
\mathcal C_{\mathrm{tail}}
\cap
\mathcal C_{\mathrm{visible}}
)
}{
\mu(
\mathcal C_{\mathrm{tail}}
)
}.
}
$$

---

# 105. 如果 $\rho_{\mathrm{tail-vis}}\ll1$

表示：

> 模型大部分尾端能力尚未被現有觀察制度穩定顯影。

---

# 106. 這不是神秘能力論

必須有：

- repeatable task；
- verified output；
- ablation；
- empirical evidence。

否則不能宣稱 invisible tail。

---

# 107. Invisible ≠ Unfalsifiable

本文堅持：

$$
\boxed{
\text{Invisible Capability Claim}
\text{ must generate a testable visibility intervention}.
}
$$

---

# 108. 例如

如果我們聲稱：

> 加 verifier 能顯示 latent math capability。

就必須測：

$$
\chi(V=1)
>
\chi(V=0).
$$

---

# 109. Visibility Intervention

定義：

$$
\boxed{
\Delta\chi_i
=
\chi(\Theta+i)
-
\chi(\Theta).
}
$$

---

# 110. 如果任何 intervention 都無效

那「能力只是看不見」的說法應被削弱。

---

# 111. 可證偽命題一

若模型差距只存在 marketing claim，而非 tail capability：

$$
\mathcal B_{\mathrm{vis}}
$$

擴大後仍不應出現穩定 separation。

---

# 112. 可證偽命題二

若 ceiling effect 是主因，把 task difficulty 上調到 diagnostic band 後：

$$
\operatorname{Disc}
\uparrow.
$$

---

# 113. 可證偽命題三

若 long-horizon capability 真實存在：

$$
\chi(\Delta t_{\mathrm{long}})
>
\chi(\Delta t_{\mathrm{short}})
$$

對相關能力應成立。

---

# 114. 可證偽命題四

若 expert coupling 只是 placebo：

$$
\chi(H_{\mathrm{expert}})
-
\chi(H_{\mathrm{ordinary}})
$$

在控制 prompt information 後不應穩定為正。

---

# 115. 可觀測預測

本文提出九個預測：

1. frontier model 的一般日常使用體感差異會隨 ordinary-task saturation 而縮小。
2. 真正模型差異會向更難、更長、更開放、更需驗證的任務遷移。
3. benchmark half-life 會持續縮短，迫使 frontier evaluation 更頻繁更新。
4. public benchmark score 將越來越需要搭配 task-distribution 與 saturation disclosure。
5. long-horizon evaluation 會增加 trajectory-level scoring，而不是只看 final output。
6. domain expert evaluators、formal verifiers 與 empirical tools 會變得更重要。
7. 一部分「新版模型沒差」其實是 user visibility-band saturation，而非 capability stagnation。
8. coupling-aware evaluation 會發現相同模型在 expert interaction regimes 中呈現更大的 tail visibility。
9. 當 AI self-activation 提升後，tail visibility 將逐步從 rare expert coupling 移入一般 agent runtime。

---

# 116. 與既有 EveMissLab 研究的關係

## 116.1 CFATC-B01

B01 建立：

$$
C_{\mathrm{latent}}
\neq
C_{\mathrm{realized}}.
$$

B03 再加入：

$$
\boxed{
C_{\mathrm{realized}}
\neq
C_{\mathrm{observed}}.
}
$$

## 116.2 CFATC-B02

B02 建立 CFA：

$$
\Theta_F
\rightarrow
C_{\mathrm{tail}}.
$$

B03 研究：

> tail 被觸發後，何時能被 observer 看見？

## 116.3 LHCF-07

LHCF 已提出 Problem Solver → Theory Builder → Problem Generator → Frame Generator → Frontier Regenerator。

B03 將其解讀為：

> 不同 meta-level 需要不同 evaluation regime 才可見。

## 116.4 GIRA-A06

GIRA-A06 已區分：

$$
T_E,
T_O,
T_C,
T_R.
$$

B03 提供 $T_O$ 之前的一個微觀條件：

$$
\boxed{
\text{capability must enter the observer's visibility band}.
}
$$

---

# 117. 外部研究支點

1. Stanford Institute for Human-Centered Artificial Intelligence, **The 2026 AI Index Report — Technical Performance**, 2026.
2. METR, **Task-Completion Time Horizons of Frontier AI Models**, updated May 8, 2026.
3. Kwa, T., **Clarifying Limitations of Time Horizon**, METR Research Note, January 22, 2026.
4. METR, **Frontier Risk Report (February to March 2026)**, May 19, 2026.
5. OpenAI, **Safety and Alignment in an Era of Long-Horizon Models**, July 20, 2026.
6. Neo.K with Aletheia, **CFATC-B01**, 2026.
7. Neo.K with Aletheia, **CFATC-B02**, 2026.
8. Neo.K, **從解題者到前沿生成者：最後人類認知對手的能力結構**, LHCF-07, 2026.

---

# 118. 結論

本文的核心命題是：

$$
\boxed{
\text{Capability}
\neq
\text{Capability Visibility}.
}
$$

一個 frontier model 可以真實變強，但普通任務仍讓：

$$
P_{\mathrm{success}}
\approx1.
$$

此時差異被 ceiling effect 吃掉。

反之，如果任務遠超所有模型能力：

$$
P_{\mathrm{success}}
\approx0,
$$

差異又被 floor effect 吃掉。

所以真正的 frontier evaluation 要找到：

$$
\boxed{
\mathcal B_{\mathrm{vis}}
}
$$

——能讓能力差異具有最大診斷價值的可見帶。

更完整地：

$$
\boxed{
\chi
=
\chi(
\text{Task},
\text{Horizon},
\text{Regime},
\text{Observer},
\text{Verification},
\text{Domain}
).
}
$$

因此我們不能從：

> 「我日常用起來沒差」

直接推出：

> 「模型 frontier capability 沒差」。

也不能從：

> 「某個 benchmark 已經滿分」

推出：

> 「能力已經測完」。

更精確的結論是：

$$
\boxed{
\text{The measurement instrument may have saturated before the capability did}.
}
$$

CFATC 至此形成三層：

$$
\boxed{
\text{Latent Capability}
\rightarrow
\text{Activated Capability}
\rightarrow
\text{Visible Capability}.
}
$$

下一篇 CFATC-B04 將處理第四個現象：

$$
\boxed{
\text{Error Morphology Shift}.
}
$$

也就是：

> **當 frontier AI 越來越強，為什麼錯誤不只是變少，而會從低級錯誤遷移到遺漏、邊界、形式化義務、架構分支與高複雜度殘差？**

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
