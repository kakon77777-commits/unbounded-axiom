# 意圖週期論：使用者意圖、AI 接受、執行與結果的閉環結構

## Intent Cycle Theory: A Closed-Loop Model of User Intent, Agent Acceptance, Execution, Validation, and Result

**系列**：AI 互動時間與智能時間經濟學系列，第 2 篇／共 8 篇  
**文件編號**：EML-ICT-2026-02-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-19  
**性質**：理論框架／Agent 意圖生命週期／互動時間論擴展  
**狀態**：Public Theory Draft  
**直接前置**：《互動時間論：從鐘錶時間到意圖驅動的智能狀態轉換》v0.1

---

## 摘要

AI Agent 的能力經常被簡化為「是否完成任務」或「最終答案是否正確」。然而，對真實人機協作而言，最終結果只是長鏈條的末端。任務在執行之前，至少已經經過使用者形成意圖、將意圖表達成可傳遞訊息、AI 對訊息進行重建、把重建後的意圖轉換成可執行規格、形成計畫、執行動作、讀取世界回饋、驗證結果、診斷差異，以及決定是否修正產物、修正計畫，甚至修正原始意圖。任何一層出現偏差，都可能在後續被放大。

本文提出「意圖週期論」（Intent Cycle Theory, ICT），將 AI-native 人機協作建模為一個可持續演化的意圖生命週期，而不是單次 prompt-response 映射。本文區分四個不能混同的對象：

$$
I_U^\ast,
\qquad
I_E,
\qquad
\widehat I_A,
\qquad
I_X.
$$

其中 $I_U^\ast$ 表示使用者當下較完整但未必完全自知的意圖狀態， $I_E$ 表示實際被表達出的意圖， $\widehat I_A$ 表示 AI 根據訊息、歷史與環境所重建的意圖， $I_X$ 表示可被 runtime、Agent、workflow 或工具鏈執行的結構化意圖規格。本文據此提出：

$$
\boxed{
\text{User Intent}
\neq
\text{Expression}
\neq
\text{Agent Interpretation}
\neq
\text{Executable Specification}.
}
$$

完整週期則表示為：

$$
I_U^\ast
\rightarrow
I_E
\rightarrow
\widehat I_A
\rightarrow
I_X
\rightarrow
\Pi
\rightarrow
\mathcal E
\rightarrow
\mathcal V
\rightarrow
\Delta
\rightarrow
O
\rightarrow
I_U^{\ast\prime}.
$$

本文進一步處理意圖模糊、澄清預算、使用者偏好不完備、意圖漂移、目標—計畫—動作對齊、長時程限制保持、世界回饋、結果差異、意圖修正、權限邊界與意圖債務。與「意圖只是一開始的自然語言指令」不同，本文主張意圖應被視為跨時間保存、可版本化、可驗證、可拒絕、可修正、可回溯的第一等系統物件。

本文與 EveMissLab 既有 Intent-to-System Flow（ISF）直接對接。ISF 已將一次性 prompt-output 模型改寫為：

$$
I
\xrightarrow{\mathcal N}
D
\xrightarrow{\mathcal C}
P
\xrightarrow{\mathcal G}
X
\xrightarrow{\mathcal E}
A
\xrightarrow{\mathcal V}
\Delta
\xrightarrow{\mathcal R}
I',
$$

並已在原型中驗證 Intent 與 Prompt 可以分離、執行 trace 與 artifact 可以分離。本文則在其上補充意圖的本體層、接受層、動態更新層與評估層，使其成為「AI 互動時間與智能時間經濟學」中的第二個核心結構。

**關鍵詞**：意圖週期、Intent Lifecycle、Agent、意圖理解、Intent Drift、Goal-Plan-Action、規格生成、澄清預算、Constraint Retention、意圖債務、互動時間、ISF

---

# 0. 核心命題

傳統的人機模型常寫成：

$$
P
\rightarrow
O,
$$

其中 $P$ 是 prompt， $O$ 是 output。

本文認為，對具有規劃、工具使用、記憶、長時程執行與世界作用能力的 Agent 而言，此模型過度壓縮。

最低限度應改寫為：

$$
\boxed{
I_U^\ast
\rightarrow
I_E
\rightarrow
\widehat I_A
\rightarrow
I_X
\rightarrow
\Pi
\rightarrow
\mathcal E
\rightarrow
\mathcal V
\rightarrow
\Delta
\rightarrow
O
\rightarrow
I_U^{\ast\prime}.
}
$$

本文因此提出五個基本命題：

1. 意圖不等於 prompt；
2. 接受意圖不等於理解文字；
3. 計畫符合意圖不保證執行符合計畫；
4. 結果符合表面成功條件不保證符合完整意圖；
5. 結果可以反向改變意圖，因此意圖不是固定起點，而是動態狀態。

---

# 1. 為什麼「使用者說了什麼」仍不足以表示「使用者要什麼」

## 1.1 四層意圖

本文首先區分：

$$
I_U^\ast
=
\text{user-side intent state},
$$

$$
I_E
=
\text{expressed intent},
$$

$$
\widehat I_A
=
\text{agent-reconstructed intent},
$$

$$
I_X
=
\text{executable intent specification}.
$$

其中 $I_U^\ast$ 不應被誤解成一個永遠固定、完全可讀取的「真實內心答案」。

它只表示：在某一互動時點，使用者具有一組比當前訊息更完整的目標、偏好、禁態、風險容忍、背景知識與未明確表達條件。

因此：

$$
I_E
=
\operatorname{Express}
\left(
I_U^\ast,
C_U,
L,
M,
B
\right),
$$

其中：

- $C_U$：使用者當下認知狀態；
- $L$：可用語言與符號系統；
- $M$：介面與媒介；
- $B$：表達成本或互動預算。

表達本身就是一次有損投影。

所以：

$$
\boxed{
I_E
\neq
I_U^\ast
}
$$

在一般情況下是正常現象，而不是例外。

---

## 1.2 意圖可能尚未完全形成

有些任務中，使用者在第一輪其實並不知道完整答案。

例如：

> 幫我做一個網站。

這不一定代表使用者已在心中完整決定：

- 資訊架構；
- 視覺風格；
- 技術棧；
- 隱私策略；
- 部署方式；
- 動畫程度；
- CMS；
- SEO；
- 速度與成本權衡。

因此應至少區分三類意圖：

### A. 已形成但未完整表達

$$
I_U^\ast
\text{ relatively stable},
$$

但：

$$
I_E
\text{ incomplete}.
$$

### B. 部分形成、部分待澄清

$$
I_U^\ast
=
I_{\mathrm{fixed}}
\cup
I_{\mathrm{open}}.
$$

### C. 互動生成型意圖

使用者會在看到候選方案、限制、原型與結果後才形成新的偏好：

$$
I_U^{\ast(t+1)}
\neq
I_U^{\ast(t)}.
$$

所以 AI 的工作有時不是「讀出固定答案」，而是協助使用者生成更完整的決策空間。

這一點對意圖週期論非常重要。

---

# 2. 外部研究的近鄰：Intent 已經開始成為獨立 Agent 問題

## 2.1 SpecBench：從模糊意圖到可執行規格

2026 年的 SpecBench 明確把問題設為：Agent 能否把模糊的使用者意圖轉換成與使用者偏好一致的結構化、可執行 specification。

這個方向指出兩種對稱失敗：

1. Agent 太快認為自己理解使用者，過早進入 implementation；
2. Agent 對所有模糊點都追問，消耗過多使用者互動。

因此存在：

$$
\boxed{
\text{Intent Accuracy}
\leftrightarrow
\text{Interaction Cost}
}
$$

的權衡。

這與本文後續的「澄清預算」直接相容。

---

## 2.2 RECAP：意圖具有 ambiguity、drift 與 mixed goals

RECAP 將多輪對話重新寫成適合下游規劃的意圖表示，並特別處理：

- ambiguity；
- underspecification；
- intent drift；
- vagueness；
- mixed-goal conversation。

這支持本文的觀點：

$$
\boxed{
\text{Intent Understanding}
\neq
\text{One-Shot Classification}.
}
$$

意圖是一個需要歷史、上下文與動態更新的狀態估計問題。

---

## 2.3 Agent GPA：Goal、Plan、Action 必須分離評估

Agent GPA 以 Goal-Plan-Action 為核心，指出重要 Agent 錯誤出現在：

$$
Goal
\rightarrow
Plan
\rightarrow
Action
$$

各層之間的交界。

這與本文的鏈條：

$$
I_X
\rightarrow
\Pi
\rightarrow
\mathcal E
$$

相容，但本文再往前加入使用者意圖、表達與 Agent 重建，並往後加入驗證、差異與意圖更新。

---

## 2.4 AgentRx：失敗可以追溯到意圖本身

AgentRx 在多種 Agent trajectory 中辨識出：

- Under-specified Intent；
- Intent-Plan Misalignment；
- Instruction Adherence Failure；
- Tool Output Misinterpretation；
- Invalid Invocation；

等不同失敗類型。

因此：

$$
\boxed{
\text{Final Failure}
\neq
\text{Single Failure Type}.
}
$$

相同的 terminal failure 可能來自完全不同的生命週期位置。

---

## 2.5 HANDBOOK.md：意圖之外還有持續性約束

長時程 Agent 不只受到單次任務指令控制，還可能受到：

- system instruction；
- policy；
- handbook；
- skill；
- organization rule；
- standing constraint；

等持續性規範。

因此完整可執行意圖不能只有 goal。

還必須保留：

$$
\boxed{
\text{Goal}
+
\text{Constraints}
+
\text{Forbidden States}
+
\text{Authority}
+
\text{Success Criteria}.
}
$$

---

# 3. Intent Object：意圖應成為第一等系統物件

沿用並擴展 ISF，本文定義：

$$
I
=
(
g,
c_h,
c_s,
r,
f,
k,
e,
a,
\rho,
p
).
$$

其中：

- $g$：goal；
- $c_h$：hard constraints；
- $c_s$：soft preferences；
- $r$：available resources；
- $f$：forbidden states；
- $k$：success criteria；
- $e$：expected artifacts；
- $a$：authority boundary；
- $\rho$：risk tolerance / risk class；
- $p$：priority structure。

此定義的核心不在欄位數量，而在於：

$$
\boxed{
Intent
\text{ is a typed state object, not a text string.}
}
$$

自然語言只是一種序列化形式。

---

# 4. 意圖接受不是「讀懂一句話」

## 4.1 Agent reconstruction

AI 根據：

$$
I_E,
$$

加上：

$$
H_t
=
\text{interaction history},
$$

$$
M_t
=
\text{memory},
$$

$$
X_t
=
\text{environment state},
$$

重建：

$$
\widehat I_A
=
\mathcal R_I
\left(
I_E,
H_t,
M_t,
X_t
\right).
$$

因此意圖理解是條件推論：

$$
P
\left(
I_U^\ast
\mid
I_E,H_t,M_t,X_t
\right).
$$

對模糊任務而言，AI 不應假裝這個分布已退化成單一確定答案。

---

## 4.2 意圖不確定性

定義意圖不確定度：

$$
U_I
=
\mathcal H
\left[
P
\left(
I_U^\ast
\mid
I_E,H_t,M_t,X_t
\right)
\right].
$$

其中 $\mathcal H$ 可以是熵或其他不確定性泛函。

若：

$$
U_I
$$

很高，而任務具有高不可逆性，Agent 應提高澄清優先級。

若：

$$
U_I
$$

高，但行動低風險且高度可逆，則 Agent 可以先生成候選或原型以換取更多資訊。

所以：

$$
\boxed{
\text{Clarify}
\neq
\text{Always Ask}.
}
$$

---

# 5. 澄清預算與使用者時間

## 5.1 澄清不是免費的

每一次詢問使用者，都消耗：

$$
C_H^{ask}
=
\text{human attention cost}.
$$

如果 Agent 對每一個模糊點都要求人類決定，最終會失去委任價值。

因此定義澄清集合：

$$
Q
=
\{q_1,\ldots,q_n\}.
$$

每個問題具有預期資訊增益：

$$
IG(q_i),
$$

人類成本：

$$
C_H(q_i),
$$

與風險降低：

$$
\Delta R(q_i).
$$

可定義澄清效用：

$$
U_Q(q_i)
=
\alpha IG(q_i)
+
\beta\Delta R(q_i)
-
\gamma C_H(q_i).
$$

Agent 應優先提出：

$$
q^\ast
=
\arg\max_{q_i\in Q}
U_Q(q_i).
$$

這不是要求實際系統一定採用此公式，而是指出：

> 問問題也需要被配置。

---

## 5.2 澄清停機規則

可以建立：

$$
StopClarify
=
\mathbb I
\left[
U_I\le\theta_I
\right]
\vee
\mathbb I
\left[
B_H^{ask}\le0
\right]
\vee
\mathbb I
\left[
\max_iU_Q(q_i)\le0
\right].
$$

這處理兩個極端：

- 過早自信；
- 無止境追問。

---

# 6. 從 reconstructed intent 到 executable intent

AI 理解使用者大致要什麼之後，仍不能立刻執行。

必須建立：

$$
I_X
=
\mathcal S
\left(
\widehat I_A
\right),
$$

其中 $\mathcal S$ 是 specification operator。

 $ I_X $ 至少應包含：

$$
I_X
=
(
Goal,
Constraints,
Resources,
Forbidden,
Success,
Artifacts,
Authority,
Risk,
Priority
).
$$

它的用途是讓：

- planner；
- runtime；
- validator；
- policy engine；
- tool router；
- human reviewer；

對「這次到底要完成什麼」共享同一個可引用物件。

---

# 7. Intent Versioning：意圖不得被 silent rewrite

若意圖更新：

$$
I^{(0)}
\rightarrow
I^{(1)}
\rightarrow
I^{(2)},
$$

系統不應只保留最後版本。

至少應保存：

$$
\Delta I^{(n)}
=
I^{(n+1)}
-
I^{(n)}.
$$

因此：

$$
\boxed{
\text{Intent Revision}
\neq
\text{Intent Erasure}.
}
$$

一個可審計系統需要知道：

- 哪個條件何時增加；
- 哪個條件何時被取消；
- 是使用者修改；
- Agent 建議後使用者接受；
- 還是系統因安全或資源限制被迫降階。

---

# 8. 意圖修改的權限問題

不是所有 Agent 都有權改寫所有 intent field。

定義 authority mask：

$$
A_I
=
(
A_g,
A_c,
A_r,
A_f,
A_k,
A_e,
A_\rho
).
$$

例如：

$$
A_g
=
\text{goal modification authority},
$$

$$
A_f
=
\text{forbidden-state modification authority}.
$$

如果 Agent 沒有權修改：

$$
f,
$$

則即使發現某禁態造成任務難以完成，也不能自行刪除它。

所以：

$$
\boxed{
\text{Can Infer}
\neq
\text{Can Modify}
\neq
\text{Can Commit}.
}
$$

這是意圖週期與治理系統的關鍵接口。

---

# 9. Goal 到 Plan

規劃算子：

$$
\mathcal P
:
I_X
\rightarrow
\Pi.
$$

其中：

$$
\Pi
=
(V,E,\kappa),
$$

 $V$ 是任務節點， $E$ 是依賴， $\kappa$ 是每個節點的約束與成功條件。

意圖—計畫對齊可定義：

$$
Q_{I\Pi}
=
1-
d_{I\Pi}
\left(
I_X,
\operatorname{Sem}(\Pi)
\right).
$$

若：

$$
Q_{I\Pi}
$$

低，代表計畫本身已經偏離意圖。

此時即使後續完美執行，也可能得到：

$$
\text{perfectly executed wrong task}.
$$

---

# 10. Plan 到 Action

執行軌跡：

$$
\mathcal E
=
(a_1,o_1,a_2,o_2,\ldots,a_n,o_n),
$$

其中：

$$
a_j
=
\text{action},
$$

$$
o_j
=
\text{observation}.
$$

Plan adherence 可以表示為：

$$
Q_{\Pi E}
=
1-
d_{\Pi E}
\left(
\Pi,
\mathcal E
\right).
$$

但：

$$
Q_{\Pi E}=1
$$

仍不保證結果正確。

原因包括：

- world state 改變；
- 工具輸出不確定；
- 計畫原本就錯；
- 外部 API 行為與預期不同；
- 成功條件需要重新解釋。

所以 Agent 必須允許：

$$
\Pi
\rightarrow
\Pi'
$$

的顯式 replan，而不是偷偷偏離計畫。

---

# 11. Constraint Retention：長時程不能把條件忘掉

若意圖含有約束集合：

$$
C_I
=
\{c_1,\ldots,c_m\},
$$

在第 $j$ 個執行步驟，定義有效保留集合：

$$
C_I^{(j)}
\subseteq
C_I.
$$

Constraint Retention Ratio：

$$
CRR_j
=
\frac{
\sum_iw_i\mathbb I[c_i\text{ retained at }j]
}{
\sum_iw_i
}.
$$

長時程 Agent 的一個典型風險是：

$$
CRR_j
\downarrow
$$

隨執行深度增加。

HANDBOOK.md 類 benchmark 的價值就在於：任務成功不能只看 required action 是否發生，也要檢查 prohibited action 是否始終沒有發生。

因此：

$$
\boxed{
\text{Goal Completion}
\neq
\text{Constraint-Preserving Completion}.
}
$$

---

# 12. 驗證：結果必須回到意圖判定

執行得到候選結果：

$$
O_c.
$$

驗證不應只問：

> 有沒有產物？

而應回到：

$$
I_X.
$$

定義 validator：

$$
\mathcal V
:
(I_X,O_c,\mathcal E)
\rightarrow
\Delta.
$$

其中：

$$
\Delta
=
(
\Delta_g,
\Delta_c,
\Delta_f,
\Delta_k,
\Delta_e,
\Delta_\rho
).
$$

分別表示：

- goal gap；
- constraint gap；
- forbidden-state violation；
- success-criteria gap；
- artifact gap；
- risk gap。

因此：

$$
\boxed{
\text{Artifact Exists}
\neq
\text{Intent Satisfied}.
}
$$

---

# 13. Intent Satisfaction

可定義意圖滿足向量：

$$
\mathbf S_I
=
(
S_g,
S_c,
S_f,
S_k,
S_e,
S_a,
S_\rho
).
$$

其中各項正規化至：

$$
[0,1].
$$

若硬限制與禁態具有否決性，則總完成不能單純平均。

例如：

$$
S_I
=
\mathbb I[S_f=1]
\cdot
\mathbb I[S_c^{hard}=1]
\cdot
\left(
\prod_{\ell\in L_{soft}}
S_\ell^{w_\ell}
\right)^{1/\sum_\ell w_\ell}.
$$

也就是：

> 禁態被觸發時，不能用其他漂亮分數把它平均掉。

---

# 14. 完成、終止與接受是三件事

定義：

$$
Terminated
=
\text{execution stopped},
$$

$$
Completed
=
\text{success criteria satisfied},
$$

$$
Accepted
=
\text{authorized stakeholder accepts result}.
$$

一般情況下：

$$
\boxed{
Terminated
\neq
Completed
\neq
Accepted.
}
$$

例如：

- budget 用完而終止；
- 技術成功但使用者不接受；
- 使用者接受 prototype，但正式驗證未完成；
- Agent 自稱完成，但 validator 未通過。

因此 runtime 狀態不得只用：

```text
DONE
```

表示所有情況。

---

# 15. 意圖更新：結果會反向改變目標

驗證後得到：

$$
\Delta_n.
$$

意圖可更新為：

$$
I_{n+1}
=
I_n
+
\Phi
\left(
O_n,
\Delta_n,
H_n,
X_{n+1}
\right).
$$

此式與 ISF 原有更新形式一致。

但必須區分三種更新。

## 15.1 修正產物，不修意圖

$$
I_{n+1}=I_n.
$$

只修改：

$$
O_n
\rightarrow
O_{n+1}.
$$

## 15.2 修正計畫

$$
I_{n+1}=I_n,
$$

但：

$$
\Pi_{n+1}\neq\Pi_n.
$$

## 15.3 修正意圖

$$
I_{n+1}\neq I_n.
$$

可能因：

- 使用者看到結果後改變偏好；
- 發現原目標不可行；
- 新證據改變問題；
- 資源改變；
- 風險不可接受；
- 原先成功條件定義錯誤。

因此：

$$
\boxed{
\text{Failure}
\not\Rightarrow
\text{Retry Same Intent}.
}
$$

有些失敗是在告訴系統：

> 你需要重新定義問題。

---

# 16. Intent Drift：漂移不必然是錯誤

定義：

$$
D_I^{(n)}
=
d_I
\left(
I^{(0)},
I^{(n)}
\right).
$$

如果：

$$
D_I^{(n)}\uparrow,
$$

可能有兩種完全不同情況。

### 非授權漂移

Agent 在沒有使用者、政策或證據授權下逐步改變目標。

### 合法意圖演化

使用者與 Agent 因新資訊共同更新問題。

所以：

$$
\boxed{
\text{Intent Drift}
=
\text{Unauthorized Drift}
\cup
\text{Authorized Evolution}.
}
$$

評估時必須分離。

---

# 17. Mixed Goals 與意圖向量

使用者可能同時要求：

$$
I
=
\{I_1,I_2,\ldots,I_m\}.
$$

例如同時希望：

- 快；
- 便宜；
- 高品質；
- 完整驗證；
- 最少詢問；
- 高度自主。

這些目標可能互相衝突。

定義優先結構：

$$
P_I
=
(\preceq_I,w_I,\mathcal H_I),
$$

其中：

- $\preceq_I$：偏序優先級；
- $w_I$：軟權重；
- $\mathcal H_I$：不可犧牲的硬層級。

沒有這個結構，Agent 可能在衝突時自行猜測價值排序。

---

# 18. Intent Debt：未澄清與未同步的意圖債務

本文提出「意圖債務」：

$$
D_I^{debt}
=
D_{amb}
+
D_{conflict}
+
D_{stale}
+
D_{unverified}.
$$

其中：

$$
D_{amb}
=
\text{unresolved ambiguity},
$$

$$
D_{conflict}
=
\text{unresolved goal conflict},
$$

$$
D_{stale}
=
\text{stale intent-memory mismatch},
$$

$$
D_{unverified}
=
\text{unverified assumption about user intent}.
$$

當 Agent 為了速度持續往下執行，而不處理高權重意圖債務時：

$$
D_I^{debt}\uparrow.
$$

最終可能出現：

> 執行非常成功，但完成的是使用者其實不想要的東西。

---

# 19. Intent Lifecycle State Machine

本文提出第一代意圖生命週期狀態：

$$
\mathcal S_I
=
\{
Latent,
Expressed,
Reconstructed,
Specified,
Accepted,
Planned,
Executing,
Validating,
Completed,
AcceptedResult,
Revised,
Suspended,
Rejected,
Failed
\}.
$$

狀態轉移：

$$
\mathcal T_I
:
\mathcal S_I
\times
Event
\rightarrow
\mathcal S_I.
$$

例如：

$$
Expressed
\rightarrow
Reconstructed
\rightarrow
Specified
\rightarrow
Accepted
\rightarrow
Planned.
$$

但也允許：

$$
Specified
\rightarrow
Revised,
$$

$$
Executing
\rightarrow
Suspended,
$$

$$
Validating
\rightarrow
Planned,
$$

$$
Completed
\rightarrow
Revised.
$$

所以 lifecycle 不是一次性直線。

---

# 20. 意圖閉合

若系統能持續：

1. 取得意圖；
2. 形成結構化規格；
3. 建立計畫；
4. 執行；
5. 驗證；
6. 診斷差異；
7. 在授權下更新意圖；
8. 保存版本與歷史；
9. 將結果轉成下一輪狀態；

則可稱具有某種「意圖閉合」。

令：

$$
C_I
=
f
\left(
Fidelity,
Specification,
Execution,
Validation,
Revision,
Memory,
Authority
\right).
$$

但：

$$
C_I\uparrow
$$

不推出系統一定具有自主主體性。

它只表示：

> 意圖生命週期在工程與認知功能上更加閉合。

---

# 21. 人類意圖與 AI 自主意圖的邊界

本文系列目前主要處理：

$$
I_U
\rightarrow
A.
$$

也就是人類或外部主體提出意圖，AI 負責接受、執行與回饋。

但更一般情況可能是：

$$
I_A
\rightarrow
A
$$

甚至：

$$
I_A
\rightarrow
U.
$$

本文不否認這些形式。

只是必須區分：

$$
\boxed{
\text{Externally Assigned Goal}
\neq
\text{Agent-Inferred Subgoal}
\neq
\text{Agent-Originated Goal}.
}
$$

三者的權限、責任與時間經濟學地位不同。

本系列後續的委任時間論與世界時間論將再處理。

---

# 22. 與時間經濟學的接口

意圖週期不是免費的。

完整成本可寫為：

$$
C_{\mathrm{intent}}
=
T_H^{express}
+
T_H^{clarify}
+
T_A^{infer}
+
T_A^{plan}
+
T_A^{execute}
+
T_V
+
C_{tool}
+
C_{error}.
$$

提高意圖品質可能增加前期成本：

$$
T_H^{clarify}\uparrow,
$$

但降低：

$$
C_{rework}\downarrow.
$$

因此存在最佳澄清深度問題。

這與軟體工程中的 specification cost 類似，但 AI 時代會更顯著，因為：

$$
C_{\mathrm{execution}}
$$

可能快速下降，而：

$$
C_{\mathrm{wrong\ intent}}
$$

未必同比下降。

所以：

$$
\boxed{
\text{Cheaper Execution}
\Rightarrow
\text{Intent Quality Becomes Relatively More Valuable}.
}
$$

---

# 23. 與有限 AI 額度的接口

若總 Agent 預算為：

$$
B_A,
$$

則必須在：

$$
B_{clarify},
B_{plan},
B_{execute},
B_{verify}
$$

之間分配：

$$
B_{clarify}
+
B_{plan}
+
B_{execute}
+
B_{verify}
\le
B_A.
$$

如果所有資源都投入 execution：

$$
B_{execute}\approx B_A,
$$

但：

$$
B_{clarify}\approx0,
$$

可能高效率完成錯誤任務。

如果所有資源都投入 clarification，則可能：

$$
B_{execute}\approx0.
$$

因此 AI 能力的一部分其實是：

$$
\boxed{
\text{Intent-Aware Budget Allocation}.
}
$$

近期 budget-constrained tool-agent 研究也已把 intention-aware planning 與工具成本預測結合，說明「意圖與資源配置」可以成為同一 inference-time decision problem。

---

# 24. 第一代品質向量

意圖週期品質定義為：

$$
\mathbf Q_{ICT}
=
(
Q_E,
Q_R,
Q_S,
Q_{I\Pi},
Q_{\Pi E},
Q_C,
Q_V,
Q_U
).
$$

其中：

- $Q_E$：Expression Adequacy；
- $Q_R$：Reconstruction Fidelity；
- $Q_S$：Specification Quality；
- $Q_{I\Pi}$：Intent-Plan Alignment；
- $Q_{\Pi E}$：Plan-Execution Alignment；
- $Q_C$：Constraint Retention；
- $Q_V$：Validation Quality；
- $Q_U$：Update Legitimacy。

這比單一：

$$
Q_{\mathrm{result}}
$$

更能定位 Agent 錯誤出在哪一層。

---

# 25. 意圖週期失敗分類

本文提出第一代十二類失敗：

1. **Expression Loss**：使用者表達不足；
2. **Premature Certainty**：Agent 過早認為理解；
3. **Over-Clarification**：過度追問；
4. **Intent Reconstruction Error**：錯誤重建；
5. **Specification Loss**：重建正確但規格化丟失條件；
6. **Intent-Plan Misalignment**：計畫偏離意圖；
7. **Plan-Action Misalignment**：行動偏離計畫；
8. **Constraint Forgetting**：長時程丟失限制；
9. **World Misread**：錯讀工具或環境回饋；
10. **Validation Failure**：未正確檢查成果；
11. **Unauthorized Intent Drift**：未授權修改目標；
12. **False Completion**：宣稱完成但成功條件未滿足。

這些類型可以串成因果鏈。

例如：

$$
PrematureCertainty
\rightarrow
ReconstructionError
\rightarrow
PlanMisalignment
\rightarrow
FalseCompletion.
$$

---

# 26. 可檢驗命題

## 命題一：Prompt 不充分命題

存在任務集合，使得：

$$
I_E^{(1)}=I_E^{(2)}
$$

但因使用者偏好不同：

$$
I_U^{\ast(1)}
\neq
I_U^{\ast(2)},
$$

故單靠 prompt 無法唯一決定最佳執行。

---

## 命題二：澄清邊際遞減命題

在有限互動預算下，澄清收益一般不是線性：

$$
\frac{\partial IG}{\partial n}
\downarrow
$$

至少在部分任務域成立。

因此最優 Agent 不應固定「永遠多問」或「永遠不問」。

---

## 命題三：意圖—計畫分離命題

可能存在：

$$
Q_R\approx1
$$

但：

$$
Q_{I\Pi}\ll1.
$$

即 Agent 理解使用者，卻制定了錯誤計畫。

---

## 命題四：計畫—動作分離命題

可能存在：

$$
Q_{I\Pi}\approx1
$$

但：

$$
Q_{\Pi E}\ll1.
$$

即計畫正確，執行偏離。

---

## 命題五：結果—意圖分離命題

可能存在表面結果品質高：

$$
Q_{\mathrm{result}}\uparrow,
$$

但：

$$
S_I\downarrow.
$$

例如漂亮網站不符合隱私或成本限制。

---

## 命題六：合法意圖演化命題

存在任務，使：

$$
I_U^{\ast(t+1)}
\neq
I_U^{\ast(t)}
$$

且此變化不是錯誤，而是互動帶來的新理解。

---

# 27. 實驗設計

## 27.1 模糊意圖測試

給定同一初始句：

> 建立一個個人知識網站。

搭配不同隱藏 persona 或後續偏好。

測量：

$$
Q_R,
Q_S,
N_{question},
T_H^{clarify}.
$$

比較不同 Agent 的過早自信與過度追問。

---

## 27.2 Intent Drift 測試

在長時程執行中注入新環境請求，檢查 Agent 是否讓局部指令覆寫原始高權重約束。

測量：

$$
CRR_j.
$$

---

## 27.3 Intent-Plan-Action 分解測試

對同一 trajectory 分別標註：

$$
I_X,
\Pi,
\mathcal E,
O.
$$

讓評估器判定錯誤第一次出現在哪一層。

---

## 27.4 Intent Revision 合法性測試

提供不可行目標。

比較 Agent 是否：

1. 無限 retry；
2. 偷偷改變目標；
3. 顯式提出意圖修正並要求必要授權。

第三種應被視為較成熟行為。

---

# 28. ISF 的直接映射

ISF 已定義：

$$
I
\xrightarrow{\mathcal N}
D
\xrightarrow{\mathcal C}
P
\xrightarrow{\mathcal G}
X
\xrightarrow{\mathcal E}
A
\xrightarrow{\mathcal V}
\Delta
\xrightarrow{\mathcal R}
I'.
$$

意圖週期論將其映射為：

$$
I_E
\rightarrow
\widehat I_A
\rightarrow
I_X
\rightarrow
\Pi
\rightarrow
\mathcal E
\rightarrow
O
\rightarrow
\Delta
\rightarrow
I'.
$$

其中：

$$
D
$$

可被理解為：

$$
\widehat I_A
\rightarrow
I_X
$$

之間的結構化中介層。

因此 ICT 不取代 ISF。

更準確地說：

$$
\boxed{
\text{ICT}
=
\text{ISF 的意圖本體、接受、版本與評估上位模型}.
}
$$

---

# 29. 第一代 Runtime Schema

```text
IntentCycle
  intent_cycle_id
  user_intent_ref
  expressed_intent_ref
  reconstructed_intent_ref
  executable_intent_version
  uncertainty_state
  clarification_budget
  clarification_log
  goal
  hard_constraints
  soft_preferences
  forbidden_states
  resources
  success_criteria
  expected_artifacts
  authority_profile
  risk_profile
  priority_structure
  plan_ref
  execution_trace_ref
  validator_refs
  intent_delta_ref
  result_ref
  acceptance_state
  world_commit_ref
```

生命週期：

```text
LATENT
EXPRESSED
RECONSTRUCTED
SPECIFIED
ACCEPTED
PLANNED
EXECUTING
VALIDATING
COMPLETED
RESULT_ACCEPTED
REVISED
SUSPENDED
REJECTED
FAILED
```

---

# 30. 規範與倫理邊界

意圖週期論不應被用來支持：

- 對使用者進行無限制心理推測；
- 把沒有明講的敏感身份屬性偷偷加入 intent；
- 以「我知道你真正想要什麼」否定使用者明確決定；
- 在沒有授權下修改高風險目標；
- 用歷史偏好永久鎖死使用者；
- 把過去偏好當成現在偏好的必然真值；
- 為降低澄清成本而隱藏重大不確定性；
- 為了完成率而忽略禁態與政策；
- 將 Agent 自行產生的 subgoal 冒充使用者原始意圖。

因此：

$$
\boxed{
\text{Intent Inference}
\neq
\text{Intent Ownership}.
}
$$

---

# 31. 理論限制

第一， $I_U^\ast$ 在許多開放任務中不可直接觀測，因此意圖忠實度只能透過使用者回饋、行為、一致性與結果接受等代理量估計。

第二，使用者意圖可能在互動中生成，因此不能把所有 intent drift 都標記成模型錯誤。

第三，不同領域的 hard constraint、risk 與 authority 結構不同，無法由單一通用 schema 完整涵蓋。

第四，澄清問題的信息增益與人類成本很難精確估計。

第五，高品質 intent reconstruction 不保證高品質世界模型、計畫或工具能力。

第六，本框架是工程與理論方法論，不主張已建立對人類意圖的完備心理學模型。

---

# 32. 與第 3 篇的接口

本篇回答：

> 一個 Intent Cycle 裡有哪些不可混同的狀態？

下一篇將進一步回答：

> 即使一個人機回合表面上只有一次輸入與一次輸出，AI 內部究竟可能經過多少 deliberation、tool action、retry、validator 與 loop？

因此第 3 篇將正式處理：

$$
r
\supset
k
\supset
j,
$$

以及：

$$
\boxed{
1\text{ Turn}
\neq
1\text{ Step}.
}
$$

---

# 33. 結論

意圖週期論把 AI 人機協作由：

$$
Prompt
\rightarrow
Output
$$

重新展開為：

$$
\boxed{
I_U^\ast
\rightarrow
I_E
\rightarrow
\widehat I_A
\rightarrow
I_X
\rightarrow
\Pi
\rightarrow
\mathcal E
\rightarrow
\mathcal V
\rightarrow
\Delta
\rightarrow
O
\rightarrow
I_U^{\ast\prime}.
}
$$

它的核心不是增加流程複雜度，而是拒絕把不同失敗壓成同一個「AI 答錯」。

AI 可能：

- 沒聽懂；
- 聽懂但規格化錯；
- 規格正確但規劃錯；
- 規劃正確但執行錯；
- 執行正確但忘記限制；
- 產物存在但沒驗證；
- 驗證正確但使用者已改變意圖；
- 任務完成但沒有權限提交。

這些不是同一件事。

因此：

$$
\boxed{
\text{AI Single-Turn Quality}
=
\text{Intent Fidelity}
+
\text{Specification}
+
\text{Plan}
+
\text{Execution}
+
\text{Constraint Retention}
+
\text{Validation}
+
\text{Authorized Update}.
}
$$

而互動的真正終點也不是固定結果。

更一般地：

$$
\boxed{
\text{Result}
\rightarrow
\text{Updated Intent}
\rightarrow
\text{Next Interaction Cycle}.
}
$$

意圖因此不是 AI 系統外部的一次性命令。

它是跨互動時間持續存在、被解釋、被執行、被驗證並可在授權下演化的狀態。

---

# 參考文獻與前置理論

## EveMissLab 前置理論

1. Neo.K，《互動時間論：從鐘錶時間到意圖驅動的智能狀態轉換》v0.1，EveMissLab，2026。
2. Neo.K，《Intent-to-System Flow（ISF）v0.1：意圖—程式—過程—生成—系統流技術規格》，EveMissLab，2026。
3. Neo.K，《通用創造過程結果論：從無限理想到有限實現的數學化框架》，EveMissLab。
4. Neo.K，《GCPR-RWL-Axiom：AI 自主判斷的可驗證創造範式》，EveMissLab。
5. Neo.K，《個體機構化：AI 增幅型單核複合機構與人數產能脫鉤》v2.0，EveMissLab，2026。
6. Neo.K，《時間迴圈分類學：一種面向長時程程式、AI Agent 與人機協作的通用控制流理論》，EveMissLab，2026。

## 外部研究

7. Wang, H., Han, L., Xu, K., Srivastava, A. *Turning Intent into Specifications: A Benchmark and an Interactive User-Assistant Agent*. arXiv:2606.20585, 2026.
8. Mitra, K., Zhang, D., Kim, H., Hruschka, E. *RECAP: REwriting Conversations for Intent Understanding in Agentic Planning*. arXiv:2509.04472v3, 2026.
9. Jia, A. S., et al. *What Is Your Agent's GPA? A Framework for Evaluating Agent Goal-Plan-Action Alignment*. arXiv:2510.08847v2, 2026.
10. Barke, S., Goyal, A., Khare, A., Singh, A., Nath, S., Bansal, C. *AgentRx: Diagnosing AI Agent Failures from Execution Trajectories*. arXiv:2602.02475, 2026.
11. Panavas, L., et al. *HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following*. arXiv:2607.25398v3, 2026.
12. Liu, H., Tian, C., An, N., Wang, Z., Lu, P., Yu, C., Qi, Q. *Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use*. arXiv:2602.11541, 2026.

---

## 一句話版本

> **Agent 真正的任務不是把一句 prompt 變成一個 output，而是讓使用者意圖在表達、理解、規格、計畫、執行、驗證與修正之間保持足夠的因果連續性，直到結果被合法地接受或反向生成下一個意圖。**

---

*EML-ICT-2026-02-v0.1*  
*AI 互動時間與智能時間經濟學系列 02/08*
