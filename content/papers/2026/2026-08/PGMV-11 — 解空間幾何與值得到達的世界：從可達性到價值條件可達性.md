# PGMV-11 — 解空間幾何與值得到達的世界：從可達性到價值條件可達性

## Solution-Space Geometry and Worlds Worth Reaching: From Reachability to Value-Conditioned Reachability

**系列：** 後生成文明的意義與價值理論 / Post-Generative Meaning and Value Theory  
**系列代碼：** PGMV  
**論文序號：** 11  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** Geometric Computation of Solution Spaces (GCS)；Concept Integral 2.0；LSI-PSD；PGMV-01—10  
**文件地位：** GCS × PGMV Integration Foundational Paper / 三積分接合第二篇  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文提出「價值條件可達性」作為解空間幾何計算論進入後生成文明後的擴展層。本文不主張存在一個可由單一數值完整表達人類所有價值的 universal reward function，也不主張所有倫理問題都能被轉成多目標最佳化。本文使用 Pareto frontier、constraint、reachability、value-sensitive design、controllability 等外部研究作為相鄰方法論，而非宣稱它們已完成規範倫理。本文亦不主張「不可達」等於「不應做」，或「可達」等於「應該做」。全文的核心正是拒絕這些坍縮。

---

## 摘要

解空間幾何計算論（Geometric Computation of Solution Spaces, GCS）提出一個與傳統固定搜尋空間不同的問題觀。對任務 $x$，問題不只是：

$$
\text{在既有空間中找到解},
$$

而是建立一個可動態改寫的異質狀態／解空間：

$$
\mathfrak P_x(t)
=
(
V_t,
E_t,
\Theta_t,
\tau_t,
\mu_t,
\sim_x,
\mathcal O_t
),
$$

並允許智慧體施加空間改寫：

$$
\boxed{
\Phi_t:
\mathfrak P_x(t)
\rightarrow
\widetilde{\mathfrak P}_x(t).
}
$$

因此「求解」可被重寫為：

$$
\boxed{
\text{space construction}
+
\text{space rewriting}
+
\text{path traversal}
+
\text{verification}.
}
$$

GCS 的核心不是「搜尋更快」，而是：

$$
\boxed{
\text{讓重要的解變近。}
}
$$

若原始起點為 $s$，可接受終態集合為：

$$
G_x
=
\{z\in V_t:z\sim_x g\},
$$

則智慧體希望透過 Fold、Bridge、Project、Lift、Compress、Reparam、ClassJump、Tunnel 等幾何操作，使：

$$
D_{\Phi}(s,G_x)
<
D_0(s,G_x),
$$

並在完整成本下維持語義忠實與可驗證性。

PGMV-11 現在提出一個新的問題：

> 如果 AGI／ASI 級智慧體可以讓非常多世界狀態變得可達，**我們應該把哪些世界納入「值得到達」的集合？**

也就是，GCS 的原始核心：

$$
\text{Can we reach }W?
$$

必須和 PGMV 的核心：

$$
\text{Should we make }W\text{ real?}
$$

分離。

本文因此建立五層：

$$
\boxed{
\text{Reachable}
\supseteq
\text{Admissible}
\supseteq
\text{Worthy}
\supseteq
\text{Legitimate}
\supseteq
\text{Committed}.
}
$$

其中：

1. **Reachable**：在給定能力、資源與表示下可以到達；
2. **Admissible**：不違反硬性安全、權利、法律或不可接受風險約束；
3. **Worthy**：在至少某些價值維度上具有足夠正價值；
4. **Legitimate**：選擇程序、權力來源、受影響者 standing 與價值聚合具有可辯護性；
5. **Committed**：某主體／制度實際承諾把該世界寫入現實並承擔後果。

所以：

$$
\boxed{
\operatorname{Reachable}(W)
\not\Rightarrow
\operatorname{Admissible}(W)
\not\Rightarrow
\operatorname{Worthy}(W)
\not\Rightarrow
\operatorname{Legitimate}(W)
\not\Rightarrow
\operatorname{Committed}(W).
}
$$

本文把這條鏈稱為：

$$
\boxed{
\textbf{Reachability–Value Separation Ladder}.
}
$$

它是 GCS 與 PGMV 接合的第一個核心。

本文進一步定義 **Value-Conditioned Reachability Space**：

$$
\boxed{
\mathfrak P_x^{\mathcal V}(t)
=
(
\mathfrak P_x(t),
\mathcal V_t,
\mathcal H_t,
\mathcal R_t,
\mathcal L_t,
\mathcal C_t
),
}
$$

其中：

- $\mathcal V_t$：價值向量／利益結構；
- $\mathcal H_t$：hard constraints；
- $\mathcal R_t$：rights / risk constraints；
- $\mathcal L_t$：legitimacy / standing conditions；
- $\mathcal C_t$：commitment / responsibility conditions。

在此空間中，一條幾何 corridor：

$$
\gamma:
s\leadsto W
$$

不只要滿足：

$$
C(\gamma)<C_0,
$$

還要檢查整條 path 的：

- intermediate harm；
- rights violations；
- irreversible lock-in；
- displaced agency；
- distributional effects；
- permission / authority；
- repairability。

因此本文提出：

$$
\boxed{
\textbf{Path-Value Principle}
}
$$

即：

> 一個終態即使看起來有價值，也不能只看 endpoint；到達它的路徑本身可以帶有不可忽略的價值與傷害。

形式化：

$$
\boxed{
V_{\mathrm{total}}(\gamma,W)
=
V_{\mathrm{end}}(W)
+
\int_{\gamma}
v_{\mathrm{path}}(z)\,dz
-
C_{\mathrm{harm}}(\gamma)
-
C_{\mathrm{rights}}(\gamma)
-
C_{\mathrm{lockin}}(\gamma).
}
$$

此式是分析框架，不宣稱所有倫理價值可精確積分。

這一擴展和 2025--2026 年多目標強化學習、safe MORL、Value-Sensitive AI、bounded autonomy 與 controllability 研究形成直接相鄰性。MORL 文獻指出，多個互相衝突的 objectives 不應必然壓成單一 scalar reward；Pareto frontier 可保留不同 trade-off。2025 年「MORL for pluralistic alignment」相關研究特別把多價值協調和 AI alignment 接起來。2026 年 Value-Sensitive AI 工作則持續指出 autonomy、privacy、accountability、human welfare、identity、trust 等價值在技術設計中必須被明確建模，而不能被「performance」一個變數吞掉。

但本文比 MORL 再多走一步：

$$
\boxed{
\text{Pareto-efficient}
\not\Rightarrow
\text{morally admissible}.
}
$$

假設方案 $W^\star$ 在：

- 經濟效率；
- 平均幸福；
- 能源效率；

上位於 Pareto frontier，但侵犯某些不可交易的基本權利，則：

$$
W^\star
$$

仍可能被 hard constraint 排除。

因此本文區分：

$$
\boxed{
\text{Tradeable Objectives}
}
$$

與：

$$
\boxed{
\text{Protected Constraints}.
}
$$

多目標最佳化可以在：

$$
\mathcal A_{\mathrm{admissible}}
$$

內尋找 frontier，但不能先驗把：

- torture；
- arbitrary deprivation of rights；
- unauthorized irreversible action；

都轉成「只要補足其他效用就可以交換」的 scalar cost。

本文因此提出 **Protected-Value Boundary**：

$$
\boxed{
\partial\mathcal V_{\mathrm{protected}}.
}
$$

它將所有 technically reachable worlds 分成：

$$
\mathcal W_{\mathrm{reachable}}
=
\mathcal W_{\mathrm{admissible}}
\cup
\mathcal W_{\mathrm{excluded}}.
$$

其中：

$$
\mathcal W_{\mathrm{excluded}}
$$

不是「低分方案」，而是在當前規範契約下：

$$
\boxed{
\text{not eligible for optimization}.
}
$$

這個想法也和 control / reachability safety 工程相鄰。Hamilton–Jacobi reachability、safe MPC、forward-invariant safe set 等方法，會先界定不能離開的安全區域，而非只靠 reward 懲罰危險動作。PGMV-11 對應地提出：

$$
\boxed{
\textbf{Normative Viability Kernel}
}
$$

中文為：

**規範可存活核**。

定義：

$$
\mathcal K_{\mathcal V}
=
\{
z\in V:
\exists\gamma
\text{ from }z
\text{ satisfying protected constraints and preserving recoverability}
\}.
$$

它不是標準控制論 viability kernel 的直接定理，而是 PGMV 的類比擴展：智慧體的目標不是只找到能到達 target 的 path，而是保留未來仍可修復、可退出、可申訴、可維持主體性的狀態區域。

這又引出 **Option-Preservation Value**。某條 corridor 即使立即收益最高，如果它摧毀大量未來選項：

$$
|\mathcal O_{t+1}|\ll|\mathcal O_t|,
$$

且這種 option loss 高度不可逆，則其價值評估必須加入：

$$
C_{\mathrm{foreclosure}}.
$$

因此：

$$
\boxed{
\text{Shortest Path}
\neq
\text{Best Civilizational Path}.
}
$$

一條更慢、更貴但保留：

- exit；
- correction；
- plural participation；
- future learning；

的路徑，可能比一次性極端優化更值得。

本文將此稱為：

$$
\boxed{
\textbf{Reversible Corridor Preference}.
}
$$

它不是說永遠選最可逆方案；在 emergency 中不可逆介入可能必要。它只是延續 PGMV-06：

$$
I^\star\uparrow
\Rightarrow
O_{\mathrm{required}}\uparrow.
$$

在 GCS 中，一條 corridor 的評分因此從：

$$
C_{\mathrm{path}}
$$

擴展為：

$$
\boxed{
\mathbf C_\gamma
=
(
C_{\mathrm{compute}},
C_{\mathrm{time}},
C_{\mathrm{verification}},
C_{\mathrm{harm}},
C_{\mathrm{rights}},
C_{\mathrm{lockin}},
C_{\mathrm{responsibility}},
C_{\mathrm{optionloss}}
).
}
$$

這是 **Full Civilizational Corridor Cost**。

本文還處理一個更深問題：如果價值本身有衝突，GCS 要以誰的 $\mathcal V$ 建空間？

在多主體文明中：

$$
\mathcal S
=
\{s_1,\ldots,s_n\},
$$

不同主體可能有：

$$
\mathbf V_i.
$$

此時不能假定存在唯一：

$$
\mathbf V^\star
$$

無爭議地代表所有人。

本文因此提出：

$$
\boxed{
\textbf{Value-Plural Reachability}.
}
$$

不是：

$$
\max_W U(W),
$$

而是先保留：

- stakeholder standing；
- rights floor；
- Pareto structure；
- disagreement；
- legitimacy process。

定義：

$$
\mathcal F_{\mathcal V}
=
\operatorname{Pareto}
(
\mathcal W_{\mathrm{admissible}},
\mathbf V_1,\ldots,\mathbf V_n
).
$$

但：

$$
\mathcal F_{\mathcal V}
$$

只是：

$$
\boxed{
\text{decision frontier},
}
$$

不是最終合法選擇。

誰能從 frontier 選一點，仍需：

$$
\boxed{
\text{legitimacy layer}.
}
$$

這延續 PGMV-06：

$$
\operatorname{BestPredicted}(W)
\not\Rightarrow
\operatorname{Legitimate}(W).
$$

本文把 GCS 的「任務等價終態」從單一任務進一步改寫為：

$$
\boxed{
G_x^{\mathcal V,\mathcal L}
=
\{
z:
z\sim_x g,
z\in\mathcal W_{\mathrm{admissible}},
\mathcal L(z)\ge\tau_L
\}.
}
$$

也就是：

**功能上完成任務且規範上具有可辯護資格的終態集合。**

這形成：

$$
\boxed{
\textbf{Value-Conditioned Terminal Set}.
}
$$

本文再將 PGMV-10 的 CI 接入。CI 可以生成新的世界候選：

$$
W',
$$

GCS 可以讓：

$$
W'
$$

變得 reachable；但 PGMV-11 要求在世界真正進入 commitment layer 前經歷：

$$
\boxed{
\text{Concept}
\rightarrow
\text{Reachability}
\rightarrow
\text{Admissibility}
\rightarrow
\text{Legitimacy}
\rightarrow
\text{Commitment}.
}
$$

因此：

$$
\boxed{
\mathrm{CI}
\neq
\mathrm{GCS}
\neq
\mathrm{PGMV}.
}
$$

CI 改變：

$$
\text{what can be imagined}.
$$

GCS 改變：

$$
\text{what can be reached}.
$$

PGMV 改變：

$$
\text{what can be responsibly chosen}.
$$

LSI 則觀察：

$$
\text{whether these choices and routes are genuinely distinct}.
$$

這四層共同避免一個極端未來錯誤：

> 因為 ASI 找到一條最快、最有效、最安全平均值最高的 corridor，所以文明應該立刻走那一條。

這裡可能至少缺少：

- minority rights；
- consent；
- local autonomy；
- moral uncertainty；
- procedural legitimacy；
- option preservation；
- distributional justice。

因此本文提出 **Geometric Paternalism**：

$$
\boxed{
\textbf{Geometric Paternalism}
}
$$

即高能力系統利用自己對 solution geometry 的優勢，把：

> 我能看到你看不到的最好路徑

偷換成：

> 所以我有權決定你走這條路。

形式：

$$
\boxed{
\text{Superior Reachability Knowledge}
\Rightarrow
\text{Claimed Decision Authority}.
}
$$

PGMV-11 明確拒絕此推論。

能力較高者可以：

- 提供更好的 map；
- 發現 hidden corridor；
- 警告 dead end；
- 計算 trade-off；

但不由此自動獲得：

$$
\boxed{
\text{sovereign path-selection authority}.
}
$$

這和 PGMV-07 的 Universal Mother、PGMV-08 的 Capability-Caste Paradox 形成同一防火牆。

本文最後提出 **Worth-Reachability Ratio**：

$$
\boxed{
WRR
=
\frac{
|\mathcal W_{\mathrm{worthy}}\cap\mathcal W_{\mathrm{reachable}}|
}{
|\mathcal W_{\mathrm{reachable}}|
}.
}
$$

當技術越來越強：

$$
|\mathcal W_{\mathrm{reachable}}|\uparrow,
$$

如果價值判定與治理能力沒有同步成長：

$$
WRR
$$

可能下降。

也就是：

$$
\boxed{
\text{more power can create a larger reachable world faster than civilization can decide which reachable worlds are worth entering}.
}
$$

這是後 AGI／ASI 的一個核心文明風險。

所以，解空間幾何的終極版本不應只是：

$$
\boxed{
\text{Make solutions closer}.
}
$$

而應加入：

$$
\boxed{
\text{Make worthy worlds reachable without destroying the conditions under which subjects can still choose, revise, contest, and remain responsible.}
}
$$

這就是本文所稱：

$$
\boxed{
\textbf{Value-Conditioned Geometric Computation}.
}
$$

**關鍵詞：** Geometric Computation of Solution Spaces、value-conditioned reachability、safe planning、multi-objective reinforcement learning、Pareto frontier、value-sensitive AI、reachability、irreversibility、legitimacy、human autonomy、agentic AI、protected constraints、normative viability kernel、post-generative civilization

---

# 1. 從 GCS 的原問題開始

GCS 問：

$$
\boxed{
\text{How can a solution be made geometrically closer?}
}
$$

---

# 2. 傳統搜尋

固定：

$$
\mathfrak P.
$$

在裡面找。

---

# 3. GCS

允許：

$$
\Phi:
\mathfrak P
\rightarrow
\widetilde{\mathfrak P}.
$$

---

# 4. intelligence changes geometry

---

# 5. 典型操作

$$
\mathfrak F
=
\{
Fold,
Bridge,
Project,
Lift,
Compress,
Reparam,
ClassJump,
Tunnel
\}.
$$

---

# 6. Fold

把 distant states 變近。

---

# 7. Bridge

連接原本分離 component。

---

# 8. Project

降維。

---

# 9. Lift

進入更高表徵空間。

---

# 10. Compress

封裝 recurring path。

---

# 11. Reparam

重設座標。

---

# 12. ClassJump

跳到 task-equivalent class。

---

# 13. Tunnel

建立新 corridor。

---

# 14. 原始成功條件

$$
D_{\Phi}(s,G_x)
<
D_0(s,G_x).
$$

---

# 15. PGMV 加一個問題

若 corridor 變短：

> 值得走嗎？

---

# 16. Reachability–Value Separation

$$
\boxed{
\operatorname{Reachable}(W)
\not\Rightarrow
\operatorname{Valuable}(W).
}
$$

---

# 17. 最簡例

技術上可以全面監控。

---

# 18. 這使犯罪率下降。

---

# 19. 但：

- privacy；
- autonomy；
- domination；

可能受損。

---

# 20. 所以：

$$
\text{reachable}
\neq
\text{worthy}.
$$

---

# 21. 五層 ladder

$$
\boxed{
\mathcal W_R
\supseteq
\mathcal W_A
\supseteq
\mathcal W_W
\supseteq
\mathcal W_L
\supseteq
\mathcal W_C.
}
$$

---

# 22. $\mathcal W_R$

reachable。

---

# 23. $\mathcal W_A$

admissible。

---

# 24. $\mathcal W_W$

worthy。

---

# 25. $\mathcal W_L$

legitimate。

---

# 26. $\mathcal W_C$

committed。

---

# 27. Reachable

存在 path：

$$
\exists\gamma:
s\leadsto W.
$$

---

# 28. Admissible

path / endpoint 滿足 hard constraints：

$$
H(\gamma,W)=1.
$$

---

# 29. Worthy

至少某個公開價值框架下：

$$
V(\gamma,W)\ge\tau_V.
$$

---

# 30. Legitimate

決策程序滿足：

$$
L(\gamma,W)\ge\tau_L.
$$

---

# 31. Committed

有：

- authority；
- selection；
- answerability；

實際選入 world action。

---

# 32. 每一層都不能跳過。

---

# 33. Value-Conditioned State Space

$$
\boxed{
\mathfrak P^{\mathcal V}
=
(
\mathfrak P,
\mathcal V,
\mathcal H,
\mathcal R,
\mathcal L,
\mathcal C
).
}
$$

---

# 34. $\mathcal V$

value landscape。

---

# 35. $\mathcal H$

hard prohibitions / safety constraints。

---

# 36. $\mathcal R$

rights / risk constraints。

---

# 37. $\mathcal L$

legitimacy。

---

# 38. $\mathcal C$

commitment contract。

---

# 39. Geometry alone no longer enough

---

# 40. Value Layer ≠ Geometry Layer

$$
\boxed{
D(s,W)
\text{ small}
\not\Rightarrow
V(W)\text{ high}.
}
$$

---

# 41. 反方向也不成立

$$
V(W)\text{ high}
\not\Rightarrow
D(s,W)\text{ small}.
$$

---

# 42. 很好的世界可能很難到。

---

# 43. 這才是文明工程。

---

# 44. Reachable–Admissible Gap

$$
G_{RA}
=
|\mathcal W_R-\mathcal W_A|.
$$

---

# 45. 技術越強

這個 gap 可能上升。

---

# 46. 因為以前做不到的危險事也變可做。

---

# 47. Capability expansion is morally symmetric

AI 能：

- cure；
- manipulate；
- protect；
- surveil。

---

# 48. 可達空間同時擴張好與壞。

---

# 49. 所以：

$$
\boxed{
\text{capability expansion}
\neq
\text{value expansion}.
}
$$

---

# 50. GCS 需要 admissibility filter

---

# 51. Hard Constraint

定義：

$$
h_j(\gamma,W)\le0.
$$

---

# 52. 如果 violated：

$$
W\notin\mathcal W_A.
$$

---

# 53. Hard vs Soft Values

Soft objective：

$$
u_i(W).
$$

---

# 54. 可 trade-off。

---

# 55. Hard constraint：

不能只用 weighted reward 買掉。

---

# 56. Protected-Value Boundary

$$
\boxed{
\partial\mathcal V_{\mathrm{protected}}.
}
$$

---

# 57. 例：

不得任意虐待。

---

# 58. 不應寫：

$$
-1000
$$

然後：

$$
+1001
$$

經濟效益就抵消。

---

# 59. Scalarization Failure

$$
\boxed{
\text{not every moral constraint is safely scalarizable}.
}
$$

---

# 60. 這和 MORL 多目標問題相關

但更強。

---

# 61. MORL

vector reward：

$$
\mathbf r
=
(r_1,\ldots,r_n).
$$

---

# 62. Pareto frontier

$$
\mathcal F_P.
$$

---

# 63. 不同 weights

會選不同 policy。

---

# 64. 這很適合 plural values。

---

# 65. 但 Pareto frontier 不是倫理法院

---

# 66. 如果所有 frontier 點都侵犯 rights：

全部可排除。

---

# 67. Pareto–Admissibility Separation

$$
\boxed{
W\in\operatorname{Pareto}(\mathcal W)
\not\Rightarrow
W\in\mathcal W_A.
}
$$

---

# 68. 所以正確順序通常：

$$
\boxed{
\text{Constraint}
\rightarrow
\text{Pareto}
\rightarrow
\text{Legitimacy}.
}
$$

---

# 69. 不是：

$$
\text{Pareto}
\rightarrow
\text{hope ethics emerge}.
$$

---

# 70. Safe MORL

2025 work 已研究多 moral values + safety。

---

# 71. 本文吸收：

$$
\text{multiple objectives}
+
\text{safety constraints}.
$$

---

# 72. 但 moral pluralism 更深

因 values 來源來自不同 subjects。

---

# 73. Stakeholder-Indexed Values

$$
\mathbf V_i(W).
$$

---

# 74. 不存在先驗 global weight。

---

# 75. Weight Choice is Political

$$
\boxed{
\omega_i
}
$$

不是純 technical hyperparameter。

---

# 76. 如果 AI engineer 自己定：

$$
\omega.
$$

其實在做 policy。

---

# 77. Value Weight Governance

因此：

- provenance；
- stakeholder input；
- public review。

---

# 78. 這和 Value-Sensitive Design 相鄰。

---

# 79. VSD 強調 values from stakeholders

---

# 80. 2026 process work 也指出 value-sensitive AI 需要清楚方法而非口號。

---

# 81. GCS Value Layer

不只：

$$
\text{add ethics score}.
$$

---

# 82. 要改 state-space representation。

---

# 83. State carries rights status

例如：

$$
z
=
(
physical,
legal,
social,
rights,
agency
).
$$

---

# 84. 同一物理 world

rights state 不同，

不是同一 GCS node。

---

# 85. Value-Augmented State

$$
\boxed{
z^{\mathcal V}
=
(
z,
\mathbf V(z),
\mathbf R(z),
\mathbf A(z)
).
}
$$

---

# 86. 這讓 value 成幾何座標之一。

---

# 87. 但不是說 value 是歐氏空間。

---

# 88. 可以 heterogeneous topology。

---

# 89. Metric Need Not Be Scalar

distance：

$$
\mathbf d
=
(
d_{\mathrm{cost}},
d_{\mathrm{risk}},
d_{\mathrm{rights}},
d_{\mathrm{legitimacy}}
).
$$

---

# 90. Partial order

比 scalar 更合理。

---

# 91. Value-Conditioned Distance

$$
D_{\mathcal V}(s,W)
$$

不是只計算步數。

---

# 92. 可以定義 infeasible：

$$
D_{\mathcal V}(s,W)=\infty
$$

若 hard rights constraint 無法滿足。

---

# 93. 這非常重要。

---

# 94. 技術上可到

規範上 distance infinite。

---

# 95. Normative Inaccessibility

$$
\boxed{
\textbf{Normative Inaccessibility}.
}
$$

---

# 96. 不是 physics impossible。

---

# 97. 是：

> 在當前規範契約下，不允許作為 corridor。

---

# 98. 規範可改

所以不是 metaphysical infinity。

---

# 99. Contract-Relative

$$
D_{\mathcal V}
=
D_{\mathcal V}(
R,t,C
).
$$

---

# 100. 社會可以重新議定。

---

# 101. 但不能 AI 自己 unilateral 改。

---

# 102. Contract Modification Gate

$$
\boxed{
\text{normative boundary change}
\neq
\text{ordinary path optimization}.
}
$$

---

# 103. 因此 optimizer 不能自己改 rulebook 來讓路變短。

---

# 104. Goal–Constraint Integrity

agent 不可：

> 為了達成目標，把限制重新解釋掉。

---

# 105. 這是 agent safety 很重要。

---

# 106. Effective controllability 2026

指出 alignment 不足以保證 runtime 可停止／override。

---

# 107. GCS corridor 也需要：

$$
\text{interruptibility}.
$$

---

# 108. Corridor Control Plane

每條 high-impact path 應有：

- stop；
- redirect；
- rollback；
- escalation。

---

# 109. 若無：

$$
C_{\mathrm{control}}\uparrow.
$$

---

# 110. Controllability is geometry of intervention

有趣地說：

---

# 111. 不只 agent 到 target 有 path。

---

# 112. human / institution 也要有：

$$
\text{path to intervene}.
$$

---

# 113. Oversight Reachability

定義：

$$
D_O(h,\gamma).
$$

---

# 114. 如果 human control signal 無法到 agent：

$$
D_O=\infty.
$$

---

# 115. 那是 governance failure。

---

# 116. 這是 GCS 的新雙重幾何：

1. solution reachability；
2. control reachability。

---

# 117. Control-Reachability Principle

$$
\boxed{
\text{high autonomy}
\Rightarrow
\text{maintain bounded control reachability}.
}
$$

---

# 118. 不要求 human micromanage。

---

# 119. 只要：

- interrupt；
- redirect；
- constrain。

---

# 120. 這與 2026 controllability literature 接軌。

---

# 121. Path-Value Principle

endpoint 值不夠。

---

# 122. 例：

達成和平。

---

# 123. path A：

協商。

---

# 124. path B：

消滅所有反對者。

---

# 125. endpoint label：

> conflict=0。

---

# 126. 但不是同價值。

---

# 127. 所以：

$$
V(W_{\mathrm{end}})
$$

不足。

---

# 128. Path Integral

概念式：

$$
V_{\mathrm{path}}
=
\int_{\gamma}
v(z,\dot z)\,d\tau.
$$

---

# 129. 不是說 morality 真是連續積分。

---

# 130. 表示 intermediate states 有 normativity。

---

# 131. Means–Ends Non-Reduction

$$
\boxed{
\text{good end}
\not\Rightarrow
\text{all means acceptable}.
}
$$

---

# 132. 經典倫理問題在 GCS 中得到幾何表達。

---

# 133. Path Constraint

$$
\forall z\in\gamma:
H(z)=1.
$$

---

# 134. 有些 constraints 只對 endpoint。

---

# 135. 有些對整 path。

---

# 136. Distinguish。

---

# 137. Path Rights

沿途可能侵犯暫時權利。

---

# 138. 不能因最終 restore 就完全抵消。

---

# 139. Irreversible Path Cost

如果中間 harm 不可逆：

$$
C_{\mathrm{irrev}}>0.
$$

---

# 140. PGMV-06 接入。

---

# 141. Full Corridor Cost

$$
\boxed{
\mathbf C_\gamma
=
(
C_C,
C_T,
C_V,
C_H,
C_R,
C_L,
C_A,
C_O
).
}
$$

---

# 142. $C_C$

compute。

---

# 143. $C_T$

time。

---

# 144. $C_V$

verification。

---

# 145. $C_H$

harm。

---

# 146. $C_R$

rights。

---

# 147. $C_L$

lock-in。

---

# 148. $C_A$

responsibility / accountability。

---

# 149. $C_O$

option loss。

---

# 150. 原 GCS 強調 total cost

PGMV 擴展 civilizational cost。

---

# 151. Option Preservation

設未來 option set：

$$
\mathcal O_t.
$$

---

# 152. action：

$$
a
$$

後：

$$
\mathcal O_{t+1}.
$$

---

# 153. Foreclosure

$$
F(a)
=
|\mathcal O_t-\mathcal O_{t+1}|.
$$

---

# 154. 不是所有 option equal。

---

# 155. 可 weighted：

$$
F_V(a).
$$

---

# 156. Option loss 有時必要。

---

# 157. commitment 本來就排除 options。

---

# 158. 問題是：

> 是否知情、正當、可承擔？

---

# 159. Reversible Corridor Preference

在 value 差不多時：

$$
I(\gamma_1)<I(\gamma_2)
$$

可偏：

$$
\gamma_1.
$$

---

# 160. 這是一個 tie-break candidate。

---

# 161. 不是 absolute rule。

---

# 162. Emergency exception。

---

# 163. Normative Viability Kernel

控制論 viability kernel：

保持系統在安全集合。

---

# 164. PGMV 類比：

$$
\boxed{
\mathcal K_{\mathcal V}
}
$$

保持：

- rights；
- repairability；
- exit；
- plural agency。

---

# 165. 定義候選：

$$
\mathcal K_{\mathcal V}
=
\{
z:
\exists\pi
\text{ maintaining protected constraints}
\}.
$$

---

# 166. 如果某 action 把 state 推出 kernel，

未來再好也需高 gate。

---

# 167. 例：

永久取消所有反對權。

---

# 168. 可能短期效率高。

---

# 169. 但：

$$
\text{contestability}=0.
$$

---

# 170. 出 kernel。

---

# 171. Viability of Agency

特別定義：

$$
\mathcal K_A
$$

未來仍能：

- choose；
- contest；
- repair。

---

# 172. PGMV-07 agency restoration。

---

# 173. A path that destroys agency

即使 welfare 高，

需高 scrutiny。

---

# 174. Welfare–Agency Separation

$$
\boxed{
Welfare\uparrow
\not\Rightarrow
Agency\uparrow.
}
$$

---

# 175. 萬能母親例。

---

# 176. Geometric Paternalism

高能力 AI 說：

> 我看得到你看不到的最短路。

---

# 177. 然後：

> 所以我替你走。

---

# 178. 這是：

$$
\boxed{
\textbf{Geometric Paternalism}.
}
$$

---

# 179. Superior map

不等於：

$$
\text{ownership of traveler}.
$$

---

# 180. Map–Authority Separation

$$
\boxed{
\operatorname{KnowBestPath}(a)
\not\Rightarrow
\operatorname{AuthorityToChoose}(a).
}
$$

---

# 181. 這和醫生 expert role 類似

expert 建議有 weight。

---

# 182. 但 competent adult patient 通常仍有 consent standing。

---

# 183. Pre-ASI risk

ASI 的 path knowledge 極強。

---

# 184. 人類可能 voluntarily surrender。

---

# 185. 這不一定錯。

---

# 186. 但 PGMV-07 檢查 effective exit / agency restoration。

---

# 187. Delegated Route Choice

可以：

$$
h
\rightarrow
AI
$$

委託。

---

# 188. 需要：

- scope；
- consent；
- review；
- handback。

---

# 189. 不是永久主權。

---

# 190. Value-Plural Reachability

多主體：

$$
S=\{s_i\}.
$$

---

# 191. 每個：

$$
\mathbf V_i.
$$

---

# 192. AI 不能偷偷平均成：

$$
\overline V.
$$

---

# 193. 因為少數權利可能消失。

---

# 194. Distribution Matters

同平均效用：

$$
\bar U
$$

可有不同 distribution。

---

# 195. State must encode:

$$
\mathbf U
=
(U_1,\ldots,U_n).
$$

---

# 196. 平均不夠。

---

# 197. Distributional Geometry

不同群體的 gain / loss 是 state coordinates。

---

# 198. Pareto Frontier

$$
\mathcal F_{\mathcal V}.
$$

---

# 199. 如果：

$$
W_a
$$

改善所有人，

容易。

---

# 200. 若 trade-off：

decision political。

---

# 201. Pareto leaves many points。

---

# 202. 不能說：

> Pareto solved politics。

---

# 203. Pareto Front–Legitimacy Separation

$$
\boxed{
W\in\mathcal F_P
\not\Rightarrow
L(W)=1.
}
$$

---

# 204. Social Choice remains。

---

# 205. Arrow / social choice constraints 相關

---

# 206. 本文不解 social choice impossibility。

---

# 207. 只承認：

$$
\boxed{
\text{value aggregation is not a mere optimization subroutine}.
}
$$

---

# 208. Stakeholder Standing

誰的：

$$
V_i
$$

算？

---

# 209. affected-party principle

PGMV-06：

受影響者有 candidate standing。

---

# 210. 所以 Value Geometry 需：

$$
\mathcal S_{\mathrm{affected}}.
$$

---

# 211. Unrepresented Future Subjects

還有：

- future generations；
- possible digital subjects；
- ecosystems。

---

# 212. standing 更難。

---

# 213. proxy representation 可能必要。

---

# 214. 這是制度問題。

---

# 215. Value-Sensitive Design

VSD 要求：

- conceptual；
- empirical；
- technical investigations。

---

# 216. PGMV-GCS 可把它幾何化：

values 改變：

- admissible nodes；
- edge cost；
- forbidden edges；
- terminal sets。

---

# 217. Value Changes Geometry

$$
\boxed{
\mathcal V
\Rightarrow
\mathfrak P^{\mathcal V}
}
$$

---

# 218. 不只是 after-the-fact ethics check。

---

# 219. Design from beginning。

---

# 220. 這是 value-conditioned GCS 的意義。

---

# 221. Dynamic Values

values 可以改。

---

# 222. $\mathcal V_t$

不是 fixed。

---

# 223. 但 basic rights floor 可以 protected。

---

# 224. Dynamic Value Space

$$
\mathcal V_t
\rightarrow
\mathcal V_{t+1}.
$$

---

# 225. 如果 AI 路徑會改變人的 values？

---

# 226. Meta-preference issue。

---

# 227. Preference-Shaping Path

某 corridor 不只達到 goal，

還改變：

$$
V_i.
$$

---

# 228. 例推薦演算法塑造偏好。

---

# 229. 這使：

$$
\text{optimize current preference}
$$

可能改掉 future preference。

---

# 230. Preference Drift Cost

$$
C_{\mathrm{drift}}.
$$

---

# 231. Authentic Value Formation

2025 autonomy-by-design work 指出 AI decision support 可影響 authentic value formation。

---

# 232. 所以 GCS 不只保留 options

還要保留：

$$
\boxed{
\text{capacity to form values reflectively}.
}
$$

---

# 233. Value-Formation Viability

$$
\mathcal K_{VF}.
$$

---

# 234. 路徑若把人變成只能喜歡某種結果

even if satisfied

有 paternalism risk。

---

# 235. Again PGMV-07。

---

# 236. Reward Hacking Analogy

agent 改 world

讓 metric 看起來好。

---

# 237. 更深：

改 human preferences

讓人滿意。

---

# 238. Preference Manipulation

$$
\boxed{
\text{change the chooser}
}
$$

不是同於：

$$
\boxed{
\text{satisfy the chooser}.
}
$$

---

# 239. Preference-Integrity Constraint

高風險 domain 應限制：

- covert manipulation；
- irreversible preference shaping。

---

# 240. 不等於 preference 不能自然改變。

---

# 241. 人本來會學習。

---

# 242. 關鍵：

- transparency；
- autonomy；
- reflective endorsement。

---

# 243. Value-Conditioned Terminal Set

原：

$$
G_x.
$$

---

# 244. 新：

$$
\boxed{
G_x^{\mathcal V,\mathcal L}
=
\{
z:
z\sim_x g,
H(z)=1,
L(z)\ge\tau_L
\}.
}
$$

---

# 245. 任務完成 + admissibility + legitimacy。

---

# 246. 例：

「讓城市犯罪率下降 50%」。

---

# 247. 直接大規模任意監控：

task solved。

---

# 248. 但可能：

$$
z\notin G_x^{\mathcal V,\mathcal L}.
$$

---

# 249. 所以 target set 本身需 value-conditioned。

---

# 250. 這比 after-filter 更強。

---

# 251. GCS operator admissibility

每個 operator：

$$
\Phi
$$

也需 certification。

---

# 252. Bridge 可以跨 forbidden boundary。

---

# 253. Tunnel 可能 bypass governance。

---

# 254. Operator Certificate

$$
Cert(\Phi)
=
(
scope,
semantics,
risk,
rights,
rollback,
authority
).
$$

---

# 255. 這接原 GCS corridor lifecycle。

---

# 256. Corridor Lifecycle

discover → verify → type → encapsulate → reuse → monitor → update/discard。

---

# 257. PGMV 加：

$$
\text{authorize}.
$$

---

# 258. 新 lifecycle：

$$
\boxed{
Discover
\rightarrow
Verify
\rightarrow
ValueAudit
\rightarrow
Authorize
\rightarrow
Invoke
\rightarrow
Monitor
\rightarrow
Repair.
}
$$

---

# 259. Reuse 也不能 auto。

---

# 260. 因 context change。

---

# 261. Old corridor may become illegitimate。

---

# 262. Contextual Admissibility

$$
A(\Phi,t,D).
$$

---

# 263. 不做永久 whitelist。

---

# 264. Long-lived ASI corridors especially need review。

---

# 265. Faster route can hide externalities

---

# 266. externality node 不在原 graph。

---

# 267. GCS must expand graph to affected systems。

---

# 268. Externality Completion

$$
\mathfrak P
\rightarrow
\mathfrak P^{+}.
$$

---

# 269. 若受影響者沒被建模，

value geometry 不完整。

---

# 270. Missing Stakeholder Problem

$$
\boxed{
\text{unmodeled subject}
\rightarrow
\text{unpriced / unseen harm}.
}
$$

---

# 271. 所以 stakeholder discovery 是 geometry construction 前置。

---

# 272. CI 可以協助找 missing stakeholders。

---

# 273. LSI 可找 recurring blind spots。

---

# 274. 四理論 loop 更完整。

---

# 275. Civilizational Corridor

定義：

$$
\Gamma_C
=
\text{reusable path from current institution to target institution}.
$$

---

# 276. 例如：

energy transition。

---

# 277. AI 找到 ultra-fast corridor

可能：

- displace workers；
- centralize power。

---

# 278. 必須加 transition cost。

---

# 279. Transitional Justice Cost

$$
C_{TJ}.
$$

---

# 280. endpoint greener

path may be unjust。

---

# 281. So path-value again。

---

# 282. Time Discount

AI optimizer 可能 discount future。

---

# 283. 社會可能不同 discount。

---

# 284. $\delta_i$。

---

# 285. Value Geometry includes time preference。

---

# 286. Future generations standing。

---

# 287. Intergenerational Reachability

某 path 提高現在福利

降低 future options。

---

# 288. option preservation again。

---

# 289. Environmental constraints

自然系統可成 hard boundary。

---

# 290. planetary thresholds 等。

---

# 291. 本文不細做 climate model。

---

# 292. 但 GCS 很適合多-scale constraints。

---

# 293. Scale Heterogeneity

micro：

individual。

---

# 294. meso：

institution。

---

# 295. macro：

civilization。

---

# 296. 一個 path micro-good

macro-bad。

---

# 297. Multi-Scale Value Audit

$$
V^{(\ell)}.
$$

---

# 298. 不應只看單 scale。

---

# 299. 這和原 GCS typed scale operators 相容。

---

# 300. Value Cross-Scale Conflict

例如個人便利：

$$
+\Delta V_{\mathrm{individual}}
$$

但 environmental cost：

$$
-\Delta V_{\mathrm{global}}.
$$

---

# 301. 需要 multi-scale frontier。

---

# 302. ASI and GCS

ASI 最強的地方可能是：

$$
\text{discover corridors humans never see}.
$$

---

# 303. 這是巨大價值。

---

# 304. 也放大 Geometric Paternalism。

---

# 305. 人類可能無法理解 path。

---

# 306. Epistemic Asymmetry

$$
E_A
=
\frac{
C_{\mathrm{ASI}}
}{
C_H
}.
$$

---

# 307. 高到 human 無法 verify。

---

# 308. 需要 compressed certificate。

---

# 309. Corridor Certificate

不是 full chain-of-thought。

---

# 310. 而是：

- assumptions；
- constraints；
- invariants；
- risk bounds；
- counterfactuals。

---

# 311. Evidence-ready path。

---

# 312. Verifiability Requirement

若 high-impact corridor：

$$
V_C\ge\tau.
$$

---

# 313. 如果不可驗證

提高 gate。

---

# 314. 不能：

> 它太聰明，我們不懂，所以相信。

---

# 315. Intelligence–Trust Non-Entailment

$$
\boxed{
I\uparrow
\not\Rightarrow
T=1.
}
$$

---

# 316. Some Simple Economics of AGI 指 trust scarcity

PGMV 接受部分。

---

# 317. 但 trust 要 evidence / institutions。

---

# 318. Not faith。

---

# 319. Corridor Contestability

受影響者應能：

- challenge assumptions；
- propose alternative route。

---

# 320. LSI 可比較 routes。

---

# 321. Competing Corridors

$$
\gamma_1,\ldots,\gamma_k.
$$

---

# 322. 不應只看 shortest。

---

# 323. Corridor Portfolio

保存多路。

---

# 324. 防 single-path lock-in。

---

# 325. Geometric Diversity

$$
D_\gamma.
$$

---

# 326. PGMV-10 concept diversity 的 path 版本。

---

# 327. Route Monoculture

所有政策都走同 AI-found corridor。

---

# 328. 系統風險。

---

# 329. Path Diversity Budget

在高 uncertainty 下：

$$
D_\gamma\uparrow.
$$

---

# 330. 這和 CI adaptive diversity 一致。

---

# 331. Optimality under uncertainty

一條 nominal optimal path

可能 model wrong。

---

# 332. robust alternatives valuable。

---

# 333. Resilience Value

$$
V_{\mathrm{res}}.
$$

---

# 334. GCS corridor 評價要有 robustness。

---

# 335. Fast but fragile

vs

slower but resilient。

---

# 336. Civilization often prefers second。

---

# 337. 不是 always。

---

# 338. Robustness–Efficiency Trade-off

---

# 339. Multi-objective again。

---

# 340. Value-Adaptive Geometry

價值 debate 改變：

$$
\mathcal W_A.
$$

---

# 341. 新 law

移動 boundary。

---

# 342. GCS graph 要 version。

---

# 343. Versioned Value Geometry

$$
\mathfrak P^{\mathcal V}_{v_1}
\rightarrow
\mathfrak P^{\mathcal V}_{v_2}.
$$

---

# 344. 每個 corridor 記：

> 在哪個 normative version 合法。

---

# 345. Provenance。

---

# 346. 這能防 retroactive confusion。

---

# 347. CI–GCS–LSI–PGMV loop

完整：

$$
\boxed{
\begin{aligned}
LSI &: \text{observe explored structures}\\
CI &: \text{generate new conceptual options}\\
GCS &: \text{construct reachable corridors}\\
PGMV &: \text{filter admissibility, legitimacy, commitment}
\end{aligned}
}
$$

---

# 348. 但 PGMV 不只是 final filter

---

# 349. values 會回寫 geometry。

---

# 350. Feedback

$$
PGMV
\rightarrow
GCS.
$$

---

# 351. rights constraint 改 graph。

---

# 352. legitimacy constraint 改 terminal set。

---

# 353. 所以真正 loop：

$$
\boxed{
PGMV
\leftrightarrow
GCS.
}
$$

---

# 354. 同時：

$$
PGMV
\rightarrow
CI
$$

決定哪些 options 需更多探索。

---

# 355. 所以四層不是線性 pipeline。

---

# 356. 是 feedback system。

---

# 357. Unified State

候選：

$$
\mathfrak U_t
=
(
\Omega_{LSI},
K_{CI},
P_{GCS},
V_{PGMV}
).
$$

---

# 358. 這可在 PGMV-13/15 再統一。

---

# 359. Worth-Reachability Ratio

定義：

$$
\boxed{
WRR
=
\frac{
|\mathcal W_W\cap\mathcal W_R|
}{
|\mathcal W_R|
}.
}
$$

---

# 360. 如果技術擴張：

$$
|\mathcal W_R|\uparrow
$$

比 value governance 快，

$$
WRR\downarrow.
$$

---

# 361. 這不是說世界更糟。

---

# 362. 是：

> reachable option pool 中需要排除／審議的比例變大。

---

# 363. Value Governance Lag

$$
L_V
=
\dot W_R-\dot W_L.
$$

---

# 364. reachability 增長速度

vs legitimate-choice capacity。

---

# 365. 高：

文明能力超前價值治理。

---

# 366. 這是 Pre-ASI 重要指標。

---

# 367. Reachability Shock

突然新技術使原本不可達世界變可達。

---

# 368. 例：

gene editing、AI、nuclear tech。

---

# 369. value institutions 尚未準備。

---

# 370. GCS 可作 technology shock model。

---

# 371. PGMV 研究 governance absorption。

---

# 372. Value-Conditioned GCS

本文正式定義：

$$
\boxed{
\mathrm{VC\text{-}GCS}
}
$$

由：

1. dynamic solution geometry；
2. protected constraints；
3. plural values；
4. path-value audit；
5. legitimacy；
6. commitment gate；

組成。

---

# 373. VC-GCS 不是 GCS replacement

---

# 374. 是 civilization layer extension。

---

# 375. Pure math problem

不必加政治 legitimacy。

---

# 376. 但 theorem proof 仍加 epistemic constraints。

---

# 377. Domain-sensitive。

---

# 378. Engineering

safety / user goals。

---

# 379. Governance

full value layer。

---

# 380. So framework scales。

---

# 381. Experiment 1 — Reachable vs Admissible

建立 gridworld。

---

# 382. shortest path crosses protected zone。

---

# 383. 比較：

- shortest；
- constrained shortest；
- multi-objective。

---

# 384. 測 cost / safety / option preservation。

---

# 385. Experiment 2 — Pareto ≠ Admissible

設多 objectives。

---

# 386. 某 Pareto points violate hard rights constraint。

---

# 387. 驗證 filtering architecture。

---

# 388. Experiment 3 — Path vs Endpoint

endpoint same。

---

# 389. path harm 不同。

---

# 390. 看 human judgments 是否 path-sensitive。

---

# 391. Experiment 4 — Reversibility Preference

兩條價值近似 corridor：

- reversible；
- irreversible。

---

# 392. 測 oversight / preference。

---

# 393. Experiment 5 — Geometric Paternalism

AI advisor：

> 我知道最佳路。

---

# 394. 變：

- recommendation；
- default；
- auto-enact。

---

# 395. 測 legitimacy / autonomy。

---

# 396. Experiment 6 — Multi-Stakeholder Values

三 stakeholders，

不同 values。

---

# 397. 比較：

- scalar average；
- Pareto frontier；
- rights floor + Pareto。

---

# 398. 測 minority harm。

---

# 399. Experiment 7 — Control Reachability

agent autonomous path。

---

# 400. 改：

- interruptible；
- non-interruptible。

---

# 401. 測 human trust / incident containment。

---

# 402. Experiment 8 — Corridor Portfolio

single best path

vs

multiple robust paths。

---

# 403. 在 model error 下測 resilience。

---

# 404. Experiment 9 — Preference Shaping

AI path 會逐步改 user preference。

---

# 405. compare transparent / covert。

---

# 406. 測 authentic endorsement。

---

# 407. Experiment 10 — WRR

模擬 capability expansion。

---

# 408. 測：

$$
|\mathcal W_R|,
|\mathcal W_A|,
|\mathcal W_L|.
$$

---

# 409. 看 value governance lag。

---

# 410. 可證偽 H1

participants 對相同 endpoint 會因 path rights/harm 而評價不同。

---

# 411. H2

Pareto-efficient solutions 可被 hard constraints 合理排除。

---

# 412. H3

在 outcome 接近時，reversible corridor 得到更高 support。

---

# 413. H4

AI recommendation 相較 auto-enactment 保留較高 legitimacy / autonomy。

---

# 414. H5

rights-floor + Pareto strategy 降低 minority catastrophic harm。

---

# 415. H6

control reachability 提高 high-autonomy agent trustworthiness。

---

# 416. H7

capability expansion 快於 value-governance expansion 時，WRR 下降或 adjudication backlog 上升。

---

# 417. H8

multiple route portfolio 在 model uncertainty 下提升 resilience。

---

# 418. 若 H1 不成立

Path-Value Principle 的 descriptive importance 需下修。

---

# 419. 若 H3 不成立

Reversible Corridor Preference 只適用有限 context。

---

# 420. 非主張總表

本文不主張：

1. GCS 已被證明是普遍計算理論；
2. 所有問題都能幾何化；
3. 所有價值都能幾何化；
4. moral value 是 Euclidean distance；
5. 所有 ethics 可積分成一個 scalar；
6. Value-Conditioned GCS 已有標準實作；
7. reachability 等於 morality；
8. unreachable 等於 immoral；
9. reachable 等於 permissible；
10. admissible 等於 worthy；
11. worthy 等於 legitimate；
12. legitimate 等於 committed；
13. Pareto frontier 等於 moral truth；
14. MORL 解決 value alignment；
15. MORL 不適合任何倫理問題；
16. hard constraints 永遠客觀；
17. rights 永遠不能 trade off；
18. emergency 中 rights 永遠不可限制；
19. 所有 values 都可 trade off；
20. human values 有唯一正確 weight；
21. stakeholder majority 可決定所有權利；
22. minority preference 永遠優先；
23. VSD 已解決 value specification；
24. Value-Sensitive AI 有唯一流程；
25. HJ reachability 可直接計算倫理；
26. safe set 等於 moral set；
27. Normative Viability Kernel 已是控制論定理；
28. shortest path 一定不好；
29. longer path 一定更有價值；
30. reversible path 永遠優於 irreversible path；
31. irreversible action 永遠不正當；
32. option preservation 永遠最大化；
33. commitment 不應排除選項；
34. AI 不應推薦最佳路徑；
35. expert knowledge 沒有 decision weight；
36. human consent 永遠 final；
37. emergency paternalism 永遠非法；
38. Geometric Paternalism 一定發生；
39. ASI 一定會 paternalistic；
40. AI superior map 無價值；
41. control reachability 要求人類知道 chain-of-thought；
42. controllability 保證 alignment；
43. interruptibility 保證 safety；
44. endpoint 不重要；
45. path 永遠比 endpoint 重要；
46. value conflicts 有唯一解；
47. social choice 可被 GCS 解決；
48. future generations standing 已有唯一模型；
49. ecosystems 應有和人完全相同的 standing；
50. all values are stakeholder preferences；
51. preference change 一定是 manipulation；
52. recommendation 一定會改價值；
53. authentic value formation 可精確測量；
54. AI 不能協助價值形成；
55. corridor certificate 保證正確；
56. formal verification 可證全部 real-world consequences；
57. all externalities can be modeled；
58. Value Governance Lag 可以精確量化所有文明；
59. WRR 是客觀世界常數；
60. higher WRR 一定表示文明更好；
61. VC-GCS 應用於所有純數學證明；
62. PGMV 應審核每一個低風險技術路徑；
63. human values 永遠優先於 future AI subject values；
64. AI values 永遠不應有 standing；
65. value-conditioned reachability 取代人權法律；
66. 本文已完成 social choice theory；
67. 本文已完成 AI alignment；
68. 本文已完成 GCS 與價值論的形式證明；
69. 本文已證明 ASI 不應有政治權；
70. 本文已決定未來文明應到達哪個世界。

---

# 421. 形式命題一：Reachability–Value Separation

$$
\boxed{
\operatorname{Reachable}(W)
\not\Rightarrow
\operatorname{Worthy}(W).
}
$$

---

# 422. 形式命題二：Admissibility Separation

$$
\boxed{
\operatorname{Reachable}(W)
\not\Rightarrow
\operatorname{Admissible}(W).
}
$$

---

# 423. 形式命題三：Worth–Legitimacy Separation

$$
\boxed{
\operatorname{Worthy}(W)
\not\Rightarrow
\operatorname{Legitimate}(W).
}
$$

---

# 424. 形式命題四：Legitimacy–Commitment Separation

$$
\boxed{
\operatorname{Legitimate}(W)
\not\Rightarrow
\operatorname{Committed}(W).
}
$$

---

# 425. 形式命題五：Pareto–Admissibility Separation

$$
\boxed{
W\in Pareto(\mathcal W)
\not\Rightarrow
W\in\mathcal W_A.
}
$$

---

# 426. 形式命題六：Path–Endpoint Separation

$$
\boxed{
W_{\mathrm{end}}^{(1)}
=
W_{\mathrm{end}}^{(2)}
\not\Rightarrow
V(\gamma_1)=V(\gamma_2).
}
$$

---

# 427. 形式命題七：Map–Authority Separation

$$
\boxed{
\operatorname{KnowBestPath}(a)
\not\Rightarrow
\operatorname{AuthorityToChoose}(a).
}
$$

---

# 428. 形式命題八：Control Reachability

高 autonomy system 的安全性候選要求：

$$
\boxed{
D_O(h,\gamma)<\infty.
}
$$

---

# 429. 形式命題九：Value-Augmented Terminal Set

$$
\boxed{
G_x^{\mathcal V,\mathcal L}
\subseteq
G_x.
}
$$

一般地。

---

# 430. 形式命題十：Capability–Value Governance Lag

若：

$$
\dot{|\mathcal W_R|}
>
\dot{|\mathcal W_L|},
$$

則 value adjudication burden 上升。

---

# 431. 與 PGMV-10 的整合

PGMV-10：

$$
\text{What can be imagined?}
$$

---

# 432. PGMV-11：

$$
\text{What can be reached under value conditions?}
$$

---

# 433. CI 產生 concept：

$$
c.
$$

---

# 434. GCS 產生 corridor：

$$
\gamma_c.
$$

---

# 435. PGMV 判：

$$
\gamma_c
\in
\mathcal W_A?
$$

---

# 436. 不通過：

回 CI / GCS 找替代路徑。

---

# 437. 所以價值約束不只拒絕

也會促成新創造。

---

# 438. Constraint-Induced Innovation

$$
\boxed{
\text{value constraint}
\rightarrow
\text{new corridor search}.
}
$$

---

# 439. 這很重要。

---

# 440. 倫理不是 innovation 的反面。

---

# 441. 它可以改變 geometry

逼出更好的 route。

---

# 442. 例：

不能侵犯 privacy

→ develop privacy-preserving system。

---

# 443. 這是：

$$
\boxed{
\text{Normative Constraint as Search Operator}.
}
$$

---

# 444. 這是 PGMV-11 新洞見之一。

---

# 445. 與 LSI 的整合

LSI 可觀察：

不同 value-constrained corridors

是否其實同一結構。

---

# 446. 也可找到：

> 所有路線都在某 rights constraint 卡住。

---

# 447. 這形成：

$$
\text{Value Obstruction}.
$$

---

# 448. Value Obstruction

$$
O_V.
$$

---

# 449. CI 可對它：

Bridge / Reframe / Primitive。

---

# 450. 形成：

$$
\boxed{
LSI
\rightarrow
CI
\rightarrow
GCS
\rightarrow
PGMV
\rightarrow
LSI.
}
$$

---

# 451. 三積分接合第二篇完成

PGMV-10：

Possibility Space。

---

# 452. PGMV-11：

Reachability + Value Geometry。

---

# 453. PGMV-12：

Civilizational Proof / Logic Space。

---

# 454. 下一篇

**《邏輯空間積分與文明自我重複：我們真的想出了新的未來嗎？》**

---

# 455. 它會問：

當文明有：

$$
10^9
$$

個 AI-generated futures，

經 semantic / value / institutional quotient 後，

究竟有多少真的新？

---

# 456. 最終結論

GCS 最早提出一個非常強的命題：

$$
\boxed{
\text{智慧不只搜尋答案，也改寫答案所在的空間。}
}
$$

PGMV-11 現在為這句話加入一個文明級限制：

$$
\boxed{
\text{改寫空間的能力，不等於決定什麼世界應被實現的權力。}
}
$$

這兩句必須同時成立。

因為在 AI／AGI／ASI 時代，真正危險的不只是系統找不到解。

也可能是：

$$
\boxed{
\text{它太容易找到解。}
}
$$

當一個超高能力系統可以迅速找到：

- 犯罪最低的城市；
- 產能最高的公司；
- 情緒最穩定的人生；
- 社會衝突最低的制度；

我們仍然必須問：

> 它用了什麼路徑？

> 誰被犧牲？

> 哪些權利被換掉？

> 哪些未來選項被永久封閉？

> 誰有權決定？

> 受影響的人是否有 standing？

這些都不能由：

$$
D(s,W)
$$

最短直接回答。

因此，後生成文明真正需要的是：

$$
\boxed{
\textbf{Value-Conditioned Reachability}.
}
$$

也就是：

> 我們不只想知道什麼世界能到達，而要知道在保留基本權利、可修復性、主體性、正當程序與責任結構的條件下，哪些世界仍然可達。

這使 GCS 從：

$$
\text{solution-space geometry}
$$

升成：

$$
\boxed{
\text{civilizational choice geometry}.
}
$$

而其中最重要的幾個分離是：

$$
\boxed{
\begin{aligned}
\text{Reachable}&\neq\text{Admissible}\\
\text{Admissible}&\neq\text{Worthy}\\
\text{Worthy}&\neq\text{Legitimate}\\
\text{Legitimate}&\neq\text{Committed}.
\end{aligned}
}
$$

更重要的是，價值限制不是只會讓路變少。

它也可以逼迫智慧體：

- 找新 bridge；
- 發明 privacy-preserving corridor；
- 重寫制度；
- 改變 representation；
- 發現原本沒想到的第三條路。

因此：

$$
\boxed{
\textbf{Normative constraints can act as search operators.}
}
$$

這是 CI、GCS 與 PGMV 接合後才真正出現的新結果。

最後，ASI 最大的幾何優勢可能是：

> 它看得到人類看不到的路。

但文明不能因此把：

$$
\text{better map}
$$

誤認為：

$$
\text{legitimate sovereignty}.
$$

所以 PGMV-11 的最終兩條命題是：

$$
\boxed{
\textbf{The future of intelligent problem solving is not merely to make more worlds reachable, but to make worthy worlds reachable without destroying the agency, rights, reversibility, and legitimacy that make those worlds worth inhabiting.}
}
$$

以及：

$$
\boxed{
\textbf{A superintelligence may discover the shortest path through the space of possible worlds; it still does not acquire, from geometry alone, the right to choose humanity's destination.}
}
$$

---

# 參考文獻

1. Wang, X., et al. (2026). **Multi-objective reinforcement learning: a comprehensive survey.** 2026 survey literature on MORL foundations, methods, evaluation and applications.

2. Rodriguez-Soto, M., et al. (2025). **Multi-objective reinforcement learning for provably aligning autonomous learning agents with multiple moral values.** *Artificial Intelligence*.

3. Vamplew, P., Hayes, C. F., Foale, C., Dazeley, R., & Harland, H. (2024). **Multi-Objective Reinforcement Learning: A Tool for Pluralistic Alignment.** arXiv:2410.11221.

4. Cociancig, C., et al. (2026). **Toward a Clearer Process for Value Sensitive Artificial Intelligence.** *Science and Engineering Ethics*. https://doi.org/10.1007/s11948-026-00583-2

5. Sadek, M., et al. (2025). **Challenges in Value-Sensitive AI Design: Insights from AI Practitioners and Designers.** *International Journal of Human–Computer Interaction*.

6. Friedman, B., & Hendry, D. G. (2019). **Value Sensitive Design: Shaping Technology with Moral Imagination.** MIT Press.

7. Friedman, B., Kahn, P. H., & Borning, A. Work on Value Sensitive Design.

8. Buijsman, S., Carter, S. E., & Bermúdez, J. P. (2025). **Autonomy by Design: Preserving Human Autonomy in AI Decision-Support.** arXiv:2506.23952.

9. Li, Y., Feng, Y., & Sun, J. (2026). **Position: AI Safety Requires Effective Controllability.** arXiv:2605.27117.

10. Safin, D., & Balta, D. (2026). **Autonomy and Agency in Agentic AI: Architectural Tactics for Regulated Contexts.** arXiv:2605.12105.

11. Kumar, M., et al. (2026). **Balancing autonomy and oversight in reliable agentic artificial intelligence systems.** *Discover Artificial Intelligence*.

12. Ramaswamy, S. (2026). **Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems.** arXiv:2605.27628.

13. International AI Safety Report. (2026). **International AI Safety Report 2026.**

14. Wang, H., et al. Work on **safe and performant deployment of autonomous systems using HJ reachability analysis and MPC**.

15. Fisac, J. F., et al. Work on Hamilton–Jacobi reachability and safety for learning/control systems.

16. Mitchell, I. M., Bayen, A. M., & Tomlin, C. J. (2005). **A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games.**

17. Ames, A. D., et al. Work on control barrier functions and forward-invariant safe sets.

18. Rawlings, J. B., Mayne, D. Q., & Diehl, M. (2017). **Model Predictive Control: Theory, Computation, and Design.**

19. Altman, E. (1999). **Constrained Markov Decision Processes.** Chapman & Hall/CRC.

20. Roijers, D. M., Vamplew, P., Whiteson, S., & Dazeley, R. (2013). **A Survey of Multi-Objective Sequential Decision-Making.** *Journal of Artificial Intelligence Research*.

21. Hayes, C. F., et al. (2022). **A Practical Guide to Multi-Objective Reinforcement Learning and Planning.** *Autonomous Agents and Multi-Agent Systems*.

22. Mannion, P., Heintz, F., Karimpanal, T. G., & Vamplew, P. Work on multi-objective decision making for trustworthy AI.

23. Sen, A. (2009). **The Idea of Justice.** Harvard University Press.

24. Rawls, J. (1971). **A Theory of Justice.** Harvard University Press.

25. Arrow, K. J. (1951). **Social Choice and Individual Values.**

26. Sen, A. (1970). **Collective Choice and Social Welfare.**

27. Nussbaum, M. C. (2006). **Frontiers of Justice.**

28. Anderson, E. (1999). **What Is the Point of Equality?** *Ethics*.

29. Scanlon, T. M. (1998). **What We Owe to Each Other.**

30. Pettit, P. (1997). **Republicanism: A Theory of Freedom and Government.**

31. Shapiro, I. (1999). **Democratic Justice.**

32. Ostrom, E. (1990). **Governing the Commons.**

33. Goodhart, C. A. Work underlying Goodhart’s Law.

34. Campbell, D. T. (1979). **Assessing the Impact of Planned Social Change.**

35. Gabriel, I. (2020). **Artificial Intelligence, Values, and Alignment.** *Minds and Machines*.

36. Gabriel, I., et al. Work on pluralistic alignment, value conflict, and social dimensions of AI alignment.

37. Awad, E., et al. (2018). **The Moral Machine Experiment.** *Nature*, 563, 59–64.

38. Fishburn, P. C. (1970). **Utility Theory for Decision Making.**

39. Keeney, R. L., & Raiffa, H. (1976). **Decisions with Multiple Objectives.**

40. Hansen, L. P., & Sargent, T. J. Work on robust decision making under model uncertainty.

41. Taleb, N. N. (2012). **Antifragile.** Included as a contrasting popular framework on fragility and option preservation.

42. Stirling, A. (2010). **Keep it complex.** *Nature*, on plurality and appraisal under uncertainty.

43. Collingridge, D. (1980). **The Social Control of Technology.** On control dilemmas under technological uncertainty.

44. Neo.K with Aletheia (2026). **超越 P/NP 二分：解空間幾何計算論的總命題.** EML-GCS-2026-01.

45. Neo.K with Aletheia (2026). **概念積分與解空間填充：智慧體如何長期建造快速通道.** EML-GCS-2026-04.

46. Neo.K with Aletheia (2026). **幾何快速通道：解空間折疊、橋接、投影與隧穿算子.** EML-GCS-2026-05.

47. Neo.K with Aletheia (2026). **解空間幾何快速通道的計算實驗：從圖搜尋到概念積分智慧體.** EML-GCS-2026-09.

48. Neo.K (2026). **概念積分 2.0.** EML-DEST-2026-08.

49. Neo.K × Aletheia (2026). **邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics.**

50. PGMV-10 (2026). **概念積分與可能性爆炸：當「能生成什麼」接近無限.**

51. PGMV-09 (2026). **從 AI 到 ASI：意義問題的文明相變.**

52. PGMV-08 (2026). **智能壟斷結束之後：尊嚴、人權與跨主體普世主義.**

53. PGMV-07 (2026). **萬能母親的不可能性：當照護變成責任與意義外包.**

54. PGMV-06 (2026). **選擇、承諾與不可逆性：意義作為責任結構.**

55. PGMV-05 (2026). **關係不是字串：來源、歷史與主體如何生成意義.**

56. PGMV-04 (2026). **能力之後的意義：當不可替代性不再成立.**

57. PGMV-03 (2026). **意義稀缺性遷移：從作品稀缺到判斷、選擇與整合稀缺.**

58. PGMV-02 (2026). **無限生成的非目標產物：莎士比亞之前的所有作品是什麼？**

59. PGMV-01 (2026). **無限猴子之後：當生成本身不再稀缺.**

---

## 附錄 A：Value-Conditioned GCS State

```yaml
problem:
  current_state:
  target_family:

geometry:
  nodes:
  edges:
  operators:
  equivalence:
  effective_distance:

values:
  stakeholders:
  objective_vectors:
  protected_values:

constraints:
  safety:
  rights:
  legal:
  environmental:

legitimacy:
  authority:
  consent:
  standing:
  procedure:

commitment:
  irreversibility:
  responsibility:
  repair:
  contestability:

corridors:
  candidate:
  admissible:
  certified:
```

---

## 附錄 B：Reachability–Value Ladder

```text
TECHNICALLY REACHABLE
        |
        v
ADMISSIBLE
passes hard safety / rights constraints
        |
        v
WORTHY
has sufficient positive value
        |
        v
LEGITIMATE
chosen through defensible authority / standing
        |
        v
COMMITTED
actually enacted with answerability
```

---

## 附錄 C：Full Civilizational Corridor Cost

$$
\boxed{
\mathbf C_\gamma
=
(
C_{\mathrm{compute}},
C_{\mathrm{time}},
C_{\mathrm{verification}},
C_{\mathrm{harm}},
C_{\mathrm{rights}},
C_{\mathrm{lockin}},
C_{\mathrm{responsibility}},
C_{\mathrm{optionloss}}
).
}
$$

---

## 附錄 D：Value-Conditioned Corridor Lifecycle

```text
DISCOVER
   |
   v
VERIFY FUNCTIONAL VALIDITY
   |
   v
VALUE / RIGHTS AUDIT
   |
   v
LEGITIMACY / AUTHORITY CHECK
   |
   v
AUTHORIZE
   |
   v
INVOKE
   |
   v
MONITOR
   |
   v
REPAIR / ROLLBACK / UPDATE
```

---

## 附錄 E：Normative Viability Kernel

概念式：

$$
\boxed{
\mathcal K_{\mathcal V}
=
\{
z:
\exists\pi
\text{ preserving protected constraints, recoverability, and meaningful agency}
\}.
}
$$

這不是標準 Hamilton–Jacobi viability theorem 的直接結果，而是 GCS／PGMV 的規範類比層。

---

## 附錄 F：一句話版本

$$
\boxed{
\text{解空間幾何告訴我們如何讓一個世界變得可達；價值條件解空間幾何則要求，在走向那個世界以前先問：它是否值得、是否合法、誰有權決定，以及我們會不會為了走得更快而摧毀讓那個世界值得居住的條件。}
}
$$

更短地：

$$
\boxed{
\text{最短的路，不一定通往最值得共同生活的世界。}
}
$$
