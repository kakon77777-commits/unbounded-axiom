# 可靠自主勞動門檻：為什麼經濟相變不必等待 AGI

## The Reliable Autonomous Labor Threshold: Why Economic Discontinuity Does Not Require AGI

**系列**：閉環全域智能：從模型競賽到文明級智能系統，第 3 篇／共 8 篇＋1 篇總結  
**系列英文名**：Closed-Loop Global Intelligence: From Model Competition to Civilization-Scale Intelligent Systems  
**文件編號**：EML-CLGI-2026-03-v0.1  
**作者**：Neo.K with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-09-02  
**性質**：理論框架／Agentic Labor Economics／Temporal Economics／Autonomous Systems／AI Political Economy  
**狀態**：Public Theory Draft  
**直接前置**：EML-CLGI-2026-01《模型不是智能系統》；EML-CLGI-2026-02《超級智能的整合路徑》；《AI 時間槓桿的多重估值》；《Agentic Organization 的時間經濟學》

---

## 生成、邊界與可反駁性聲明

本文是一篇 AI 輔助生成的理論研究稿。

本文不主張當前所有 Agent 已經足以廣泛替代人類，也不主張工作市場會依照單一路徑快速自動化。本文討論的是一個較窄但重要的命題：

> 經濟體系發生重大 AI 勞動相變，不需要先等到模型被普遍承認為 AGI；只要某類 Agent 在足夠多任務域跨過「品質達標、低未檢出錯誤、可恢復、長期自主、低治理時間與成本優勢」的共同門檻，它就可能先成為一個具有經濟意義的自主智能勞動單元。

本文因此區分：

$$
\text{AGI Threshold}
\neq
\text{Economic Substitution Threshold}.
$$

同時區分：

$$
\text{Capability Demonstration}
\neq
\text{Reliable Production}.
$$

本文不把「能做一次」視為「可以長期部署」，也不把「可以替代某些任務」擴張為「可以替代整個職業」或「可以替代所有人類工作」。

---

# 摘要

AI 與勞動市場的討論經常以 AGI 作為主要分界：當 AI 達到人類通用智能時，才會大規模影響白領、專業工作與組織結構。本文提出另一種可能：經濟相變的真正門檻可能顯著早於 AGI，而且其核心不是模型是否在所有領域達到人類水平，而是 Agent 是否在特定任務集合中達到「可靠自主勞動門檻」。

本文將自主 Agent 的經濟可用性分解為六個核心條件：最低品質門檻、可靠性、未檢出錯誤率、恢復能力、自主曆時與人類治理密度。若一個 Agent 的平均品質已高於任務最低可接受品質，且錯誤能被驗證、回溯、重試與局部隔離，使真正能污染長期狀態的未檢出錯誤維持在可接受風險範圍；同時，Agent 可以在低人類介入下持續工作數小時、數日或更久，並以低於可比人類流程的成本產生可驗證成果，則它已具有「自主智能勞動單元」的經濟性質，即使它仍不是 AGI。

本文提出可靠自主勞動門檻：

$$
\Theta_{\mathrm{RAL}}
=
\left\{
Q_A \ge Q_{\min},
\;
U_A \le \epsilon,
\;
\Gamma_A \ge \Gamma_{\min},
\;
T_A^{\mathrm{aut}} \ge T_{\min},
\;
\rho_H \le \rho_H^{\max},
\;
C_A^{*} < C_H^{*}
\right\},
$$

其中 $Q_A$ 是品質， $U_A$ 是未檢出且不可恢復錯誤率， $\Gamma_A$ 是恢復能力， $T_A^{\mathrm{aut}}$ 是可維持自主工作的曆時， $\rho_H$ 是人類介入密度， $C_A^{*}$ 與 $C_H^{*}$ 分別為風險與驗證調整後的 Agent 與人類成本。

本文進一步指出，Agent 的經濟競爭對象通常不是最頂尖專家，而是大量「要求穩定中上品質、可驗收、可持續與可追蹤」的組織任務。當這類工作可以被自主 Agent 持續完成時，經濟效果來自四個槓桿：人類治理時間釋放、24/7 機器智能時間、可利用平行度，以及成果的歷史累積。這使「單次能力是否勝過頂尖人類」與「總經濟產出是否具有替代性」成為兩個不同問題。

本文最後主張，AI 勞動相變可能不是一個單一瞬間，而是任務級門檻在不同職業中逐步被跨越。首先被重構的可能不是最需要極端原創性的工作，而是具備明確驗收標準、可分解、可重試、資訊可外部取得、錯誤可驗證、成果可累積的工作。當大量任務先被抽離，職業本身才進一步被重組。因此未來勞動研究應從「AI 能不能取代這個職業」轉向「這個職業中有多少任務已跨過可靠自主勞動門檻」。

**關鍵詞**：自主 Agent、AI 勞動、可靠自主勞動門檻、AGI、時間經濟學、未檢出錯誤、恢復能力、人類治理時間、數位勞動、經濟相變

---

# 0. 問題的提出：為什麼所有人都在等 AGI？

AI 對勞動市場的流行敘事常被寫成：

$$
\text{Current AI}
\longrightarrow
\text{AGI}
\longrightarrow
\text{Mass Automation}.
$$

這條時間線暗示：

> 在 AGI 之前，AI 主要是工具；到了 AGI 之後，才會出現真正自主的機器勞動。

但這個推論混合了兩種不同門檻：

$$
\Theta_{\mathrm{cog}}
=
\text{general cognitive threshold},
$$

以及：

$$
\Theta_{\mathrm{econ}}
=
\text{economic production threshold}.
$$

一個系統可能尚未跨過：

$$
\Theta_{\mathrm{cog}},
$$

卻已經在某類任務跨過：

$$
\Theta_{\mathrm{econ}}.
$$

原因很簡單。

公司購買勞動的目的，不是購買一個「哲學上完整的人類等價智能」。

公司真正需要的是：

$$
\text{acceptable output}
+
\text{reliability}
+
\text{timeliness}
+
\text{accountability}
+
\text{cost efficiency}.
$$

因此，AGI 不是所有經濟任務的必要條件。

---

# 1. 經濟替代的比較對象不是天才，而是任務要求

假設某一任務的最低可接受品質為：

$$
Q_{\min}.
$$

頂尖人類專家的品質可能為：

$$
Q_{\mathrm{elite}}
=
0.98.
$$

某 Agent 只有：

$$
Q_A
=
0.82.
$$

如果：

$$
Q_{\min}
=
0.75,
$$

則：

$$
Q_A
<
Q_{\mathrm{elite}}
$$

與：

$$
Q_A
\ge
Q_{\min}
$$

可以同時成立。

這表示：

> Agent 不需要擊敗最強人類，才能成為可用生產單元。

大量經濟活動的真實要求並不是：

$$
\max Q.
$$

而是：

$$
Q
\ge
Q_{\min}
$$

之後，再比較：

$$
\text{cost},
\quad
\text{speed},
\quad
\text{availability},
\quad
\text{reliability}.
$$

因此：

$$
\boxed{
\text{Economic usefulness is thresholded, not purely ranked.}
}
$$

---

# 2. 從「能做」到「能可靠地做」

AI demo 常證明：

$$
P(
\text{successful completion}
)
>
0.
$$

但生產系統真正需要的是：

$$
P(
\text{reliable completion}
)
\ge
r_{\min}.
$$

兩者差異很大。

一個 Agent 偶爾能：

- 寫出完整軟體；
- 做出高品質分析；
- 解決數學問題；
- 完成市場研究；

並不代表它適合直接進入長期組織流程。

因此需要區分：

$$
\text{Capability}
$$

與：

$$
\text{Production Reliability}.
$$

真正的勞動替代不是：

$$
\text{AI can do task } T.
$$

而是：

$$
\boxed{
\text{AI can repeatedly complete } T
\text{ under bounded risk and bounded supervision.}
}
$$

---

# 3. 可靠自主勞動門檻

本文正式提出：

$$
\boxed{
\Theta_{\mathrm{RAL}}
=
\text{Reliable Autonomous Labor Threshold}.
}
$$

對任務集合 $\mathcal T$，若 Agent 滿足：

$$
Q_A
\ge
Q_{\min},
$$

$$
U_A
\le
\epsilon,
$$

$$
\Gamma_A
\ge
\Gamma_{\min},
$$

$$
T_A^{\mathrm{aut}}
\ge
T_{\min},
$$

$$
\rho_H
\le
\rho_H^{\max},
$$

以及：

$$
C_A^{*}
<
C_H^{*},
$$

則可說該 Agent 在任務域 $\mathcal T$ 跨過可靠自主勞動門檻。

其中：

- $Q_A$：品質；
- $U_A$：未檢出且不可恢復錯誤率；
- $\Gamma_A$：錯誤恢復能力；
- $T_A^{\mathrm{aut}}$：可持續自主曆時；
- $\rho_H$：人類介入密度；
- $C_A^{*}$：風險、驗證與算力調整後 Agent 成本；
- $C_H^{*}$：可比人類流程的完整成本。

---

# 4. 真正重要的不是錯誤率，而是未檢出污染率

AI 不可能要求：

$$
P(
\text{any error}
)
=
0.
$$

人類也做不到。

更重要的是：

$$
P(
\text{error}
\rightarrow
\text{undetected persistent contamination}
).
$$

令：

$$
e
=
P(
\text{local error}
),
$$

$$
d
=
P(
\text{error detected}
\mid
\text{error}
),
$$

$$
g
=
P(
\text{successful recovery}
\mid
\text{error detected}
).
$$

則簡化的持續污染風險可以表示為：

$$
U
\approx
e
\left[
(1-d)
+
d(1-g)
\right].
$$

因此，就算：

$$
e
$$

沒有降到極低，只要：

$$
d
\uparrow,
$$

以及：

$$
g
\uparrow,
$$

真正的：

$$
U
$$

仍可大幅下降。

這是 Agent 工程的一個根本轉向：

$$
\boxed{
\text{Reliable autonomy does not require perfect cognition.}
}
$$

它要求的是：

$$
\boxed{
\text{fallible cognition}
+
\text{strong error containment}.
}
$$

---

# 5. Checkpoint、Retry 與 Rollback 改變了長週期概率

若一個任務有：

$$
n
$$

個串行步驟，每一步成功率為：

$$
p,
$$

並且任何一步錯誤都永久失敗，則：

$$
P_{\mathrm{success}}
=
p^n.
$$

這使長週期工作快速變得不可靠。

例如：

$$
p
=
0.99,
$$

$$
n
=
100,
$$

則：

$$
P_{\mathrm{success}}
\approx
0.366.
$$

但若每一步都有：

$$
\text{checkpoint},
$$

$$
\text{verification},
$$

$$
\text{retry},
$$

$$
\text{rollback},
$$

則失敗不再必然沿整條鏈傳播。

更合理的長期風險變成：

$$
P(
\text{error survives all gates}
).
$$

因此：

$$
\boxed{
\text{Long-horizon reliability}
\neq
p^n
}
$$

只要架構允許局部錯誤被吸收。

這也是為什麼可靠 Agent 的核心不只是更好的模型，而是：

$$
\text{Model}
+
\text{Verification Architecture}.
$$

---

# 6. 人類治理時間是自主勞動的真正瓶頸之一

如果 Agent 每做一步都需要：

> 「是否繼續？」

那它仍然只是高能力工具。

令：

$$
N_H
=
\text{human interventions},
$$

$$
N_T
=
\text{effective task transitions}.
$$

則人類介入密度：

$$
\rho_H
=
\frac{
N_H
}{
N_T
}.
$$

如果：

$$
\rho_H
\approx
1,
$$

代表幾乎每一步都需要人。

如果：

$$
\rho_H
\ll
1,
$$

代表人類主要只處理：

- 高風險決策；
- 模糊目標；
- 例外；
- 最終驗收；
- 不可逆提交。

因此：

$$
\boxed{
\text{Autonomy}
\approx
\text{reduction of unnecessary human control coupling}.
}
$$

這直接接到時間經濟學。

因為真正被釋放的是：

$$
T_H^{\mathrm{gov}},
$$

即有限的人類治理時間。

---

# 7. 自主曆時比單輪能力更接近經濟可用性

一個模型可以非常聰明，但只能穩定工作：

$$
10 \text{ minutes}.
$$

另一個 Agent 單輪能力稍低，但可以穩定維持：

$$
8 \text{ hours},
$$

$$
24 \text{ hours},
$$

甚至：

$$
7 \text{ days}.
$$

兩者的經濟意義不同。

因此定義：

$$
T_A^{\mathrm{aut}}
=
\text{maximum reliable autonomous horizon}.
$$

當：

$$
T_A^{\mathrm{aut}}
\uparrow,
$$

AI 能接手的任務型態會發生質變。

因為很多工作不是單次 reasoning，而是：

$$
\text{observe}
\rightarrow
\text{act}
\rightarrow
\text{wait}
\rightarrow
\text{observe again}
\rightarrow
\text{update}.
$$

例如：

- 長期軟體維護；
- 市場監控；
- 資料庫更新；
- 文獻追蹤；
- 錯誤修復；
- 持續測試；
- 客戶案件跟進；
- 系統營運。

這些工作要求的是：

$$
\boxed{
\text{continuity}
}
$$

而不只是高峰智力。

---

# 8. 24/7 不是單純延長工作時間

人類工作時間受到：

$$
T_H
\le
24 \text{ h/day}
$$

的硬限制。

實際有效專注工作時間更低。

Agent 則可以在算力與成本允許下：

$$
T_A
\rightarrow
24/7.
$$

但真正重要的不只是：

$$
T_A > T_H.
$$

而是：

$$
\text{same world time}
+
\text{parallel intelligent processes}.
$$

若存在：

$$
N_A
$$

個 Agent，可以同時處理具有可平行性的任務，則：

$$
W_A
\approx
Q_A
\cdot
R_A
\cdot
T_A
\cdot
\Pi_I.
$$

其中：

$$
\Pi_I
$$

是可利用平行度。

因此機器智能時間的真正槓桿是：

$$
\boxed{
\text{Persistence}
\times
\text{Parallelism}.
}
$$

---

# 9. Agent 數量本身不是勞動力

必須避免：

$$
N_A
\uparrow
\Rightarrow
W_A
\uparrow
$$

的簡單推論。

若任務不可平行，或者多 Agent 產生：

- 重複工作；
- 狀態衝突；
- 互相引用錯誤；
- 協調成本；
- 過度通訊；

則：

$$
\Omega_{\mathrm{coord}}
\uparrow.
$$

因此有效 Agent 勞動量應表示為：

$$
L_A^{\mathrm{eff}}
=
N_A
\cdot
Q_A
\cdot
R_A
\cdot
\Pi_A
-
\Omega_{\mathrm{coord}}.
$$

這再次說明：

$$
\boxed{
\text{Agent Count}
\neq
\text{Effective Labor}.
}
$$

---

# 10. 成本必須包含驗證、算力與風險

比較 AI 與人類成本時，不能只寫：

$$
C_A
=
\text{token cost}.
$$

完整 Agent 成本至少應包括：

$$
C_A^{*}
=
C_{\mathrm{model}}
+
C_{\mathrm{compute}}
+
C_{\mathrm{tool}}
+
C_{\mathrm{verification}}
+
C_{\mathrm{governance}}
+
C_{\mathrm{failure}}
+
C_{\mathrm{security}}.
$$

同樣，人類成本也不應只用薪水：

$$
C_H^{*}
=
C_{\mathrm{salary}}
+
C_{\mathrm{benefit}}
+
C_{\mathrm{management}}
+
C_{\mathrm{coordination}}
+
C_{\mathrm{training}}
+
C_{\mathrm{turnover}}
+
C_{\mathrm{error}}.
$$

只有比較：

$$
C_A^{*}
$$

與：

$$
C_H^{*},
$$

才有經濟意義。

因此：

$$
\boxed{
\text{cheap inference}
\neq
\text{cheap autonomous labor}.
}
$$

但反過來：

$$
\boxed{
\text{expensive inference}
\neq
\text{uneconomic autonomous labor}.
}
$$

如果 Agent 替代的是高成本、長曆時、需多人協作的工作，即使 token 很貴，也可能仍然具有正價值。

---

# 11. 任務級替代先於職業級替代

職業通常不是一個任務，而是：

$$
J
=
\{
T_1,
T_2,
\ldots,
T_n
\}.
$$

例如一名軟體工程師可能同時負責：

- 需求理解；
- 架構；
- coding；
- review；
- debugging；
- 溝通；
- 部署；
- 維護；
- 事故判斷。

Agent 可能先跨過：

$$
\Theta_{\mathrm{RAL}}
$$

於：

$$
T_3,
T_4,T_5,
$$

但尚未跨過：

$$
T_1,T_2,T_6.
$$

因此：

$$
\boxed{
\text{Task Substitution}
\rightarrow
\text{Job Recomposition}
\rightarrow
\text{Possible Job Substitution}.
}
$$

而不是：

$$
\text{AI suddenly replaces profession}.
$$

這使勞動市場相變更可能呈現漸進、非同步與不均勻擴張。

---

# 12. 哪些任務最容易先跨過門檻

可靠自主勞動門檻較容易在以下任務成立：

1. 驗收標準清楚；
2. 可以分解；
3. 可以重試；
4. 失敗成本可控；
5. 資訊主要可數位取得；
6. 工具介面明確；
7. 結果可自動測試；
8. 狀態可以外部化；
9. 任務重複度高；
10. 可由規則或 verifier 判斷結果。

可將任務適配度粗略表示為：

$$
\chi_T
=
f(
V_T,
D_T,
R_T,
O_T,
S_T
),
$$

其中：

- $V_T$：verifiability；
- $D_T$：decomposability；
- $R_T$：recoverability；
- $O_T$：observability；
- $S_T$：state externalizability。

當：

$$
\chi_T
\uparrow,
$$

跨過：

$$
\Theta_{\mathrm{RAL}}
$$

所需模型能力通常下降。

---

# 13. 哪些任務較晚

以下類型通常更難完全自主化：

- 高度模糊的終極目標；
- 不可逆高風險決策；
- 缺乏可觀測結果；
- 無法形式驗證；
- 需要深度人際信任；
- 高度政治性協商；
- 現實世界感測不足；
- 極端新穎問題；
- 責任不能被輕易轉移的決策。

這些任務可能需要較高：

$$
Q_{\min},
$$

更低：

$$
\epsilon,
$$

以及更高：

$$
T_H^{\mathrm{gov}}.
$$

因此：

$$
\boxed{
\Theta_{\mathrm{RAL}}
\text{ is task-dependent}.
}
$$

不存在一個對全經濟一致的單一門檻。

---

# 14. 自主智能勞動單元

一旦某 Agent 對任務集合 $\mathcal T$ 穩定跨過：

$$
\Theta_{\mathrm{RAL}},
$$

本文將其稱為：

$$
\boxed{
\text{Autonomous Intelligent Labor Unit}
}
$$

即：

> 自主智能勞動單元。

它不需要具有：

- 人類式人格；
- 人類式意識；
- 人類等價全領域能力；
- AGI 身分。

其經濟定義只要求：

$$
\text{persistent delegated work}
\rightarrow
\text{verified useful output}.
$$

因此：

$$
\boxed{
\text{Economic agency}
\neq
\text{human equivalence}.
}
$$

---

# 15. 從工具到勞動單元的相變

傳統工具：

$$
H
\rightarrow
T
\rightarrow
O.
$$

人類必須持續操作工具。

自主 Agent：

$$
H
\rightarrow
G
\rightarrow
\{
A_1,A_2,\ldots,A_n
\}
\rightarrow
O.
$$

人類主要提供：

$$
\text{Intent}
+
\text{Constraints}
+
\text{High-Risk Governance}.
$$

Agent 負責：

$$
\text{execution loop}.
$$

因此：

$$
\boxed{
\text{Tool}
\rightarrow
\text{Delegated Worker}
}
$$

的真正相變，不是模型突然變成人，而是：

$$
\rho_H
\downarrow
$$

到足以使人類退出大部分 routine control loop。

---

# 16. 委任槓桿

沿用時間經濟學，可以定義：

$$
\Lambda_D
=
\frac{
V_{\mathrm{effective\ delegated\ work}}
}{
T_H^{\mathrm{gov}}+\epsilon
}.
$$

如果一個人一天花：

$$
2 \text{ hours}
$$

治理 Agent，卻得到相當於：

$$
20 \text{ hours}
$$

高品質可驗收工作，則：

$$
\Lambda_D
$$

已經大幅高於傳統一對一工具使用。

當：

$$
\Lambda_D
\uparrow,
$$

人類角色可能從：

$$
\text{operator}
$$

轉向：

$$
\text{governor},
$$

$$
\text{architect},
$$

$$
\text{intent setter},
$$

$$
\text{exception handler}.
$$

這是 AI 原生組織真正可能發生的人機分工改變。

---

# 17. 經濟相變不要求全面取代人類

若 Agent 只替代：

$$
30\%
$$

的任務，也可能使原本需要：

$$
100
$$

人的部門變成：

$$
70
$$

人。

若再透過：

$$
\Lambda_D
\uparrow,
$$

使剩餘員工可以同時治理更多 Agent，組織結構又會進一步改變。

因此經濟相變可以在：

$$
\text{partial task automation}
$$

階段先發生。

不需要：

$$
100\%
$$

的職業替代。

這使：

$$
\boxed{
\text{Economic discontinuity}
\text{ can precede }
\text{full labor substitution}.
}
$$

---

# 18. 低錯誤中上品質可能比偶發天才更有市場價值

對某些創造性任務，人們偏好：

$$
Q_{\mathrm{peak}}
$$

很高的系統。

但大量日常組織任務更在乎：

$$
Q_{\mathrm{floor}}.
$$

即：

> 最差情況有多差。

因此可以區分：

$$
Q_{\mathrm{peak}},
$$

以及：

$$
Q_{\mathrm{floor}}.
$$

一個 Agent 可能：

$$
Q_{\mathrm{peak}}
=
0.90,
$$

$$
Q_{\mathrm{floor}}
=
0.78.
$$

另一個模型：

$$
Q_{\mathrm{peak}}
=
0.99,
$$

但：

$$
Q_{\mathrm{floor}}
=
0.40.
$$

對長期生產而言，前者可能更有價值。

因此：

$$
\boxed{
\text{Production AI optimizes the quality floor, not only the quality ceiling.}
}
$$

這也是「降低幻覺」在 Agent 時代比單輪聊天時代更重要的原因。

---

# 19. 長期累積使 Agent 產生資本性質

如果 Agent 每次工作後都將結果丟棄：

$$
O_t
\rightarrow
\varnothing,
$$

其價值主要是當期服務。

如果輸出進入：

$$
S_{t+1},
$$

則工作可以成為：

- 資料庫；
- 程式資產；
- 知識圖譜；
- 流程；
- 模型訓練資料；
- 驗證器；
- 客戶歷史；
- 世界狀態。

因此：

$$
O_t
\rightarrow
K_{t+1}.
$$

這時 Agent 不只產生：

$$
\text{labor flow},
$$

還可能形成：

$$
\text{knowledge capital stock}.
$$

於是：

$$
\boxed{
\text{Autonomous Labor}
\rightarrow
\text{Cumulative Capital Formation}.
}
$$

這比單純「省幾個人力」更重要。

---

# 20. 與時間經濟學的統合

沿用：

$$
\rho_{\mathrm{intel}}
=
\frac{
W_I^{\mathrm{quality\ adjusted}}
}{
\Delta t_W
},
$$

以及：

$$
\rho_{\mathrm{commit}}
=
\frac{
V_{\mathrm{verified\ world\ commit}}
}{
\Delta t_W
}.
$$

若 Agent 的：

$$
\rho_{\mathrm{intel}}
$$

很高，但：

$$
\rho_{\mathrm{commit}}
$$

低，代表大量 token 沒有沉積成真正資產。

可靠自主勞動的目標是：

$$
\boxed{
\rho_{\mathrm{commit}}
\uparrow
}
$$

同時：

$$
T_H^{\mathrm{gov}}
\downarrow.
$$

因此一個更完整的委任效率可以表示為：

$$
\eta_{\mathrm{RAL}}
=
\frac{
V_{\mathrm{verified\ accumulated\ output}}
}{
T_H^{\mathrm{gov}}
+
C_A^{*}
+
\epsilon
}.
$$

這比單純：

$$
\text{tokens per second}
$$

更接近經濟價值。

---

# 21. 不是所有自主性都值得追求

Agent autonomy 不應被最大化為：

$$
A
\rightarrow
1.
$$

因為某些任務：

$$
Risk_T
$$

很高。

更合理的目標是：

$$
A_T^{*}
=
\arg\max_A
\left[
V(A)
-
Risk(A)
-
GovernanceCost(A)
\right].
$$

因此：

$$
\boxed{
\text{Optimal Autonomy}
\neq
\text{Maximum Autonomy}.
}
$$

低風險、高可驗證任務可以高度自主。

高風險、不可逆任務則需要：

$$
\text{human gate}.
$$

這使未來組織更可能形成「分層自主」而不是全面放權。

---

# 22. 可靠自主勞動與大量基本可替代人員

這裡必須精確處理一個容易引發誤解的命題。

本文不主張「某些人沒有價值」。

本文討論的是：

$$
\text{role substitutability}.
$$

一個人在某家公司中負責的任務，可能高度：

- 標準化；
- 可驗證；
- 可重複；
- 可數位取得；
- 可回滾。

這表示：

$$
\chi_T
$$

很高。

若 Agent 跨過：

$$
\Theta_{\mathrm{RAL}},
$$

則該角色中的部分任務具有較高自動化可能。

這是：

$$
\boxed{
\text{task architecture}
}
$$

的性質，不是：

$$
\boxed{
\text{human worth}
}
$$

的評價。

---

# 23. 為什麼高薪也不自動等於高不可替代性

市場薪資：

$$
W_H
$$

並不只反映：

$$
\text{frontier cognitive contribution}.
$$

它還可能包含：

- 稀缺證照；
- 組織階級；
- 網絡位置；
- 管理權；
- 地理；
- 品牌；
- 歷史制度；
- 議價能力。

因此：

$$
\boxed{
W_H
\not\propto
\text{AI-resistance}.
}
$$

某些高薪工作的實際日常任務仍可能具有高：

$$
\chi_T.
$$

反之，某些薪資較低工作可能包含：

- 現場感知；
- 身體互動；
- 高社會信任；
- 非結構化環境；
- 責任承擔；

而更難自主化。

因此 AI 勞動衝擊不應簡化為：

$$
\text{low salary first}.
$$

---

# 24. 新的人類比較優勢

當既有知識查詢、普通分析、程式生成與資料整理逐漸被 Agent 吸收後，人類比較優勢可能移向：

$$
\text{Novel Problem Formation},
$$

$$
\text{Cross-Domain Abstraction},
$$

$$
\text{Normative Judgment},
$$

$$
\text{Institution Design},
$$

$$
\text{High-Stakes Responsibility},
$$

$$
\text{Embodied and Social Context}.
$$

因此：

$$
\boxed{
\text{AI substitutability}
\neq
\text{human obsolescence}.
}
$$

更可能出現的是：

$$
\text{routine cognition}
\downarrow
$$

在人類工作中的比重下降，而：

$$
\text{governance}
+
\text{novelty}
+
\text{responsibility}
$$

的比重提高。

---

# 25. 經濟相變的早期指標

如果要判斷可靠自主勞動是否真正到來，應觀察：

1. 平均自主曆時：
   $$
   T_A^{\mathrm{aut}}.
   $$

2. 人類介入密度：
   $$
   \rho_H.
   $$

3. 未檢出且不可恢復錯誤率：
   $$
   U_A.
   $$

4. 驗證後世界提交密度：
   $$
   \rho_{\mathrm{commit}}.
   $$

5. 風險調整後成本：
   $$
   C_A^{*}.
   $$

6. 任務跨域覆蓋：
   $$
   |\mathcal T_{\mathrm{RAL}}|.
   $$

若：

$$
T_A^{\mathrm{aut}}
\uparrow,
$$

$$
\rho_H
\downarrow,
$$

$$
U_A
\downarrow,
$$

$$
\rho_{\mathrm{commit}}
\uparrow,
$$

且：

$$
|\mathcal T_{\mathrm{RAL}}|
\uparrow,
$$

那麼 AI 勞動相變可能已經在發生，即使沒有人正式宣布 AGI。

---

# 26. 經濟 AGI 是一個容易誤導的名詞

有人可能將這種狀態稱為：

$$
\text{Economic AGI}.
$$

但本文不優先採用此名稱。

原因是：

> 一個系統可以在大量經濟任務中高度可替代，卻仍不具有人類式通用認知。

因此更精確的概念是：

$$
\boxed{
\text{Reliable Autonomous Labor}
}
$$

而不是透過修改 AGI 定義，把任何重大經濟影響都叫 AGI。

這能保持：

$$
\text{cognitive taxonomy}
$$

與：

$$
\text{economic taxonomy}
$$

的分離。

---

# 27. 從個體 Agent 到自主勞動網路

一旦多個 Agent 都跨過：

$$
\Theta_{\mathrm{RAL}},
$$

組織可以形成：

$$
\mathcal L_A
=
\{
A_1,
A_2,
\ldots,
A_n
\}.
$$

不同 Agent 負責：

- 搜尋；
- coding；
- verification；
- 資料管理；
- 文書；
- 監控；
- 部署；
- 研究。

這時 AI 組織的能力變成：

$$
W_{\mathcal L_A}
=
\sum_i
W_{A_i}
+
\Sigma_{\mathrm{synergy}}
-
\Omega_{\mathrm{coord}}.
$$

只要：

$$
\Sigma_{\mathrm{synergy}}
>
\Omega_{\mathrm{coord}},
$$

多 Agent 勞動網路就可能形成正協同。

這就是 Paper 02 所討論的：

$$
\text{Organizational Superhuman Capability}
$$

在經濟層最早可能出現的實體基礎之一。

---

# 28. 經濟相變的真正順序

本文提出一個可能的漸進序列：

$$
\text{Assistant}
$$

$$
\downarrow
$$

$$
\text{Tool-Using Agent}
$$

$$
\downarrow
$$

$$
\text{Reliable Task Agent}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Autonomous Intelligent Labor Unit}
}
$$

$$
\downarrow
$$

$$
\text{Multi-Agent Labor Network}
$$

$$
\downarrow
$$

$$
\text{Agentic Organization}.
$$

注意：

$$
\text{AGI}
$$

不一定必須位於：

$$
\text{Reliable Task Agent}
$$

與：

$$
\text{Autonomous Intelligent Labor Unit}
$$

之間。

這正是本文的中心命題。

---

# 29. 結論：文明不需要等到 AGI 才會遇到自主機器勞動力

本文的核心結論可以寫成：

$$
\boxed{
\text{AGI is sufficient for broad autonomous labor, but not necessary for many economically valuable forms of autonomous labor.}
}
$$

真正的經濟門檻是：

$$
\Theta_{\mathrm{RAL}},
$$

而不是：

$$
\Theta_{\mathrm{AGI}}.
$$

當 Agent 在愈來愈多任務域滿足：

$$
Q_A
\ge
Q_{\min},
$$

$$
U_A
\le
\epsilon,
$$

$$
\Gamma_A
\ge
\Gamma_{\min},
$$

$$
T_A^{\mathrm{aut}}
\ge
T_{\min},
$$

$$
\rho_H
\le
\rho_H^{\max},
$$

以及：

$$
C_A^{*}
<
C_H^{*},
$$

它就開始從：

$$
\text{AI Tool}
$$

轉化為：

$$
\boxed{
\text{Autonomous Intelligent Labor Unit}.
}
$$

它未必是 AGI。

它未必能做頂尖科學。

它未必具有普遍價值判斷。

它甚至可能只在某些領域保持中上品質。

但如果它：

- 長期不睡；
- 能查資料；
- 能用工具；
- 能維持狀態；
- 能驗證；
- 能回滾；
- 能重試；
- 能持續累積；

那麼它已經足以改變組織。

因此，AI 勞動市場真正值得追蹤的問題，不再只是：

> 「哪一年 AGI 到來？」

而是：

> **「哪一些任務正在跨過可靠自主勞動門檻？」**

當這個集合：

$$
\mathcal T_{\mathrm{RAL}}
$$

持續擴張時，經濟相變可能早已開始。

---

## 核心命題摘要

### 命題一：AGI 門檻與經濟替代門檻不同

$$
\boxed{
\Theta_{\mathrm{AGI}}
\neq
\Theta_{\mathrm{RAL}}.
}
$$

### 命題二：經濟可用性是門檻問題，而非只看最高品質

$$
\boxed{
Q_A
\ge
Q_{\min}
}
$$

即可進入某些生產流程，不要求：

$$
Q_A
=
Q_{\mathrm{elite}}.
$$

### 命題三：真正重要的是未檢出且不可恢復錯誤

$$
\boxed{
U_A
=
P(
\text{undetected unrecoverable error}
).
}
$$

### 命題四：可靠自主性依賴錯誤吸收而非完美認知

$$
\boxed{
\text{Fallible Cognition}
+
\text{Error Containment}
\rightarrow
\text{Reliable Autonomy}.
}
$$

### 命題五：人類治理密度是自主勞動的重要指標

$$
\boxed{
\rho_H
=
\frac{
N_H
}{
N_T
}.
}
$$

### 命題六：任務級替代先於職業級替代

$$
\boxed{
\text{Task Substitution}
\rightarrow
\text{Job Recomposition}.
}
$$

### 命題七：24/7 與平行性使中上品質 Agent 形成總量優勢

$$
\boxed{
W_A
=
Q_A
\cdot
R_A
\cdot
T_A
\cdot
\Pi_I.
}
$$

### 命題八：自主勞動可以形成知識資本

$$
\boxed{
\text{Autonomous Labor}
\rightarrow
\text{Cumulative Capital Formation}.
}
$$

### 命題九：經濟相變可以先於 AGI

$$
\boxed{
\text{Economic Discontinuity}
\not\Rightarrow
\text{AGI First}.
}
$$

---

## 系列接口

Paper 01 將模型與智能系統分離。

Paper 02 提出系統級超人類組織能力可能先於模型級 ASI。

Paper 03 則把這個中間層落到經濟結構：

$$
\boxed{
\text{Non-AGI Agent}
+
\text{Reliability}
+
\text{Persistence}
+
\text{Verification}
\rightarrow
\text{Autonomous Intelligent Labor}.
}
$$

下一篇將研究這種自主勞動最容易被低估的一個長期性質：

**Paper 04：《累積比聰明更重要：從一次回答到持續世界沉積》**

核心問題是：

> 如果一個 Agent 每一輪只比普通專業人員稍好或相近，但它可以持續工作數月、數年，並把每次輸出都沉積成下一輪可重用的資料、工具、驗證器與世界狀態，那麼「歷史累積」是否會成為比單輪智力更重要的智能資本？
