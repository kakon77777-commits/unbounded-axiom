# 單輪不是一步：AI Turn、內部迴圈、工具動作與執行軌跡

## One Turn Is Not One Step: AI Turns, Internal Loops, Tool Actions, and Execution Trajectories

**系列**：AI 互動時間與智能時間經濟學系列，第 3 篇／共 8 篇  
**文件編號**：EML-ITT-2026-03-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-19  
**性質**：理論框架／Agent Runtime／Execution Trajectory／互動時間論擴展  
**狀態**：Public Theory Draft  
**直接前置**：《意圖週期論：使用者意圖、AI 接受、執行與結果的閉環結構》v0.1

---

## 摘要

在傳統聊天介面中，一次使用者訊息與一次 AI 回應通常被視為「一輪」。然而，Agent 化人工智慧已使「一輪」與「一步」迅速分離。同一個可見回合內，AI 可能進行多次規劃、搜尋、工具呼叫、程式執行、檔案讀寫、驗證、重試、重新規劃、狀態保存、分支探索、錯誤恢復與外部提交；也可能幾乎不做任何外部動作，只直接生成答案。因此，以 turn count 衡量 AI 工作量、能力或互動時間，會把高度異質的執行過程壓縮成同一個表面單位。

本文提出「單輪非一步原理」（One-Turn-Not-One-Step Principle），建立 AI-native 執行的分層模型。最低限度區分：

$$
r
=
\text{human-AI interaction round},
$$

$$
k
=
\text{deliberation / control-loop index},
$$

$$
j
=
\text{observable action index}.
$$

因此：

$$
\boxed{
r
\supset
\{k\}
\supset
\{j\}.
}
$$

更完整地，一次 Agent 執行由「意圖週期—Run—Attempt—Loop—Action—Observation—Validation—Recovery—Commit」等多層物件組成。本文區分 retry、replan、recovery、rollback 與 resume；提出 execution event、attempt lineage、checkpoint、side-effect boundary、progress delta、no-op action、trace completeness 與 turn expansion factor；並強調：

$$
\boxed{
\text{Visible Turn}
\neq
\text{Execution Work}
\neq
\text{Execution Depth}
\neq
\text{World Effect}.
}
$$

本文與 EveMissLab 的 Intent-to-System Flow（ISF）Execution Runtime v0.3、時間迴圈分類學及 World-Domain Cognitive Runtime 直接銜接。ISF v0.3 已建立 append-only Event Store、Artifact Store、Checkpoint/State Replay、Retry/Recovery、Resource Budget 與 Run Isolation，且要求 Program、Execution History 與 Artifacts 分離保存。外部研究亦正在快速轉向 trajectory-level evaluation、execution provenance、checkpoint/restore 與 recoverable long-horizon agents。本文將這些工程進展放入互動時間框架，主張 AI 的「單輪能力」應以其單輪內可可靠完成的狀態轉換、工具操作、驗證與恢復結構衡量，而不應只以輸出文字量、思考 token 或可見回合數衡量。

**關鍵詞**：AI Turn、Execution Trajectory、Agent Loop、Tool Call、Retry、Replan、Recovery、Rollback、Checkpoint、Event Sourcing、Execution Provenance、Interaction Time

---

# 0. 核心問題

對一般對話而言：

$$
User_r
\rightarrow
Assistant_r
$$

看似可以自然定義為一輪。

但 Agent 系統中，一次可見回應可能包含：

$$
\text{Plan}
\rightarrow
\text{Search}
\rightarrow
\text{Read}
\rightarrow
\text{Execute}
\rightarrow
\text{Observe}
\rightarrow
\text{Validate}
\rightarrow
\text{Retry}
\rightarrow
\text{Replan}
\rightarrow
\text{Commit}.
$$

因此：

$$
\boxed{
1\text{ Turn}
\neq
1\text{ Step}.
}
$$

本文處理的問題是：

> 一個可見 AI turn 內部究竟發生了多少可區分的智能控制、工具行動、世界觀測、驗證與恢復？這些結構如何被記錄、比較與計入互動時間？

---

# 1. Turn 是介面單位，不是計算本體單位

## 1.1 Visible Turn

令：

$$
r
\in
\mathbb N
$$

表示人機可見互動回合。

最簡形式：

$$
R_r
=
(
U_r,
A_r
),
$$

其中：

- $U_r$：使用者第 $r$ 次可見輸入；
- $A_r$：AI 第 $r$ 次可見輸出。

此定義對 UI、聊天歷史與使用者體驗很有用。

但它無法表示 $A_r$ 是如何形成的。

---

## 1.2 相同 Turn 數可以包含不同工作

考慮兩個系統：

### 系統 A

$$
U
\rightarrow
\text{direct generation}
\rightarrow
A.
$$

### 系統 B

$$
U
\rightarrow
\text{plan}
\rightarrow
\text{search}
\rightarrow
\text{read}
\rightarrow
\text{code}
\rightarrow
\text{test}
\rightarrow
\text{fix}
\rightarrow
\text{retest}
\rightarrow
A.
$$

兩者均滿足：

$$
N_{\mathrm{turn}}=1.
$$

但其 execution trajectory 明顯不等價。

因此：

$$
\boxed{
N_{\mathrm{turn}}
\text{ is not a universal measure of agent work}.
}
$$

---

# 2. 三層基本索引

本文建立：

$$
r
=
\text{interaction round},
$$

$$
k
=
\text{deliberation / control-loop index},
$$

$$
j
=
\text{observable action index}.
$$

一輪表示為：

$$
R_r
=
\left\{
L_{r,k}
\right\}_{k=1}^{K_r},
$$

每個 loop 又包含：

$$
L_{r,k}
=
\left\{
a_{r,k,j}
\right\}_{j=1}^{J_{r,k}}.
$$

因此：

$$
\boxed{
R_r
\supset
L_{r,k}
\supset
a_{r,k,j}.
}
$$

此式表示包含關係，不表示每一層都必須嚴格實作成巢狀資料結構。

---

# 3. Deliberation 不等於 Action

AI 可能在不改變外部世界的情況下進行多次候選比較。

定義 deliberation state：

$$
D_{r,k}.
$$

其內部更新可寫為：

$$
D_{r,k+1}
=
\mathcal F_D
\left(
D_{r,k},
I_X,
H,
O
\right).
$$

若沒有外部可觀測行動，仍可能發生：

- plan decomposition；
- candidate comparison；
- uncertainty update；
- strategy selection；
- budget allocation；
- stop / continue decision。

因此：

$$
\boxed{
\text{Deliberation Step}
\neq
\text{External Action}.
}
$$

本文不要求系統公開私有 chain-of-thought；工程 trace 只需保存足以重建控制流的狀態摘要、決策類型、工具操作與可驗證結果。

---

# 4. Action 的最低定義

定義一個可觀測 Agent action：

$$
a_j
=
(
actor,
type,
target,
input,
authority,
cost
).
$$

行動後產生：

$$
o_j
=
\text{observation}.
$$

狀態更新：

$$
S_{j+1}
=
T
\left(
S_j,
a_j,
o_j
\right).
$$

常見 action type 包括：

- model inference；
- search；
- retrieval；
- file read；
- file write；
- code execution；
- test；
- API call；
- database mutation；
- message send；
- tool invocation；
- validator invocation；
- checkpoint；
- branch；
- commit request。

不是所有 action 都具有相同的世界作用強度。

---

# 5. Execution Event

為了讓一輪可被審計，本文提出最小事件：

$$
e_j
=
(
id,
parent,
actor,
action,
input,
output,
S^-,
S^+,
cost,
status
).
$$

其中：

$$
S^-
$$

與：

$$
S^+
$$

分別是事件前後狀態。

若系統採 append-only event sourcing，則：

$$
\mathcal H_E
=
(e_1,e_2,\ldots,e_n).
$$

原則上不能透過修改過去事件偽造乾淨歷史。

因此：

$$
\boxed{
\text{Correction}
\neq
\text{History Rewrite}.
}
$$

修正本身應形成新事件。

---

# 6. Program、Execution History 與 Artifact 必須分離

設：

$$
P
=
\text{compiled program / plan},
$$

$$
H_E
=
\text{execution history},
$$

$$
A
=
\text{artifacts}.
$$

本文要求：

$$
\boxed{
P
\neq
H_E
\neq
A.
}
$$

理由如下：

同一個 program 可以有不同 run：

$$
P
\rightarrow
Run_1,
Run_2,
\ldots
$$

同一個 run 可以產生多個 artifact：

$$
Run_i
\rightarrow
\{A_{i,1},A_{i,2},\ldots\}.
$$

而 artifact 本身不能完整證明執行路徑。

這是可重現性與錯誤診斷的必要分離。

---

# 7. Run 與 Attempt

## 7.1 Run

定義一個執行實例：

$$
Run_m
=
(
IntentVersion,
PlanVersion,
Environment,
Budget,
Trace
).
$$

Run 有自己的不可變身份。

若失敗後重新執行，不應偷偷覆寫：

$$
Run_m.
$$

應建立：

$$
Run_{m+1}.
$$

## 7.2 Attempt

一個 Run 內部可能存在多個局部 attempt。

例如：

$$
Attempt_{q,1}
\rightarrow
Failed,
$$

$$
Attempt_{q,2}
\rightarrow
Succeeded.
$$

Attempt 的存在使：

$$
\text{Task Success}
$$

與：

$$
\text{First-Try Success}
$$

可以分離。

---

# 8. Retry、Replan、Recovery、Rollback、Resume 不是同義詞

## 8.1 Retry

Retry 表示：

$$
a
\rightarrow
\text{fail}
\rightarrow
a'
$$

且：

$$
a'
\approx a.
$$

主要策略與目標沒有改變。

## 8.2 Replan

Replan 表示：

$$
\Pi
\rightarrow
\Pi',
$$

通常因：

- 新觀測；
- 路徑不可行；
- 外部狀態改變；
- 成本超標；
- 發現新依賴。

所以：

$$
\boxed{
Retry
\neq
Replan.
}
$$

## 8.3 Recovery

Recovery 是錯誤後讓系統回到可繼續工作的合法狀態。

$$
S_{failed}
\xrightarrow{\mathcal R}
S_{recoverable}.
$$

Recovery 可以包含 retry、local repair、reload、dependency replacement、partial recomputation、compensating action、rollback。

因此 recovery 是上位概念。

## 8.4 Rollback

Rollback 將某部分狀態恢復到已知 checkpoint：

$$
S_t
\rightarrow
S_{t-c}.
$$

但若外部 side effect 已發生，rollback 未必能物理撤銷它。

所以：

$$
\boxed{
\text{State Rollback}
\neq
\text{World History Erasure}.
}
$$

## 8.5 Resume

Resume 表示從合法保存狀態繼續：

$$
S_{suspended}
\rightarrow
S_{running}.
$$

它不等同於重新從頭執行。

---

# 9. Checkpoint 是執行時間的錨點

定義：

$$
C_q
=
(
AgentState,
EnvironmentState,
ArtifactRefs,
EventOffset,
BudgetState
).
$$

好的 checkpoint 至少回答：

- Agent 當時知道什麼？
- 環境當時是什麼狀態？
- 哪些動作已產生外部效果？
- 哪些 artifact 已完成？
- 預算剩多少？
- 從哪個 event 接續？

因此：

$$
\boxed{
\text{Checkpoint}
\neq
\text{Text Summary Only}.
}
$$

長時程 Agent 若只保存文字上下文，可能無法恢復真實環境。

---

# 10. 外部研究：Recoverable Agent 已成為獨立 runtime 問題

2026 年的 AgentRewind 提出 aligned checkpoints，同時記錄 Agent context 與 controlled environment，讓長時程 Agent 可回到較早狀態，並攜帶前次嘗試資訊重新執行。

這說明：

$$
\boxed{
\text{Agent Recovery}
=
\text{Cognitive Recovery}
+
\text{Environment Recovery}.
}
$$

而 Crab 類 checkpoint/restore runtime 則進一步處理 sandbox 級狀態保存與回退。

因此 checkpoint 不只是 LLM context management，而是 execution semantics。

---

# 11. Side Effect Boundary

Agent action 可以分成：

$$
a_j^{pure}
$$

與：

$$
a_j^{effect}.
$$

前者例如本地推理、sandbox 計算、read-only retrieval。

後者可能寄信、修改資料庫、發布、下單、部署、移動真實設備或改變權限。

因此應建立：

$$
Effect(a_j)
\in
\{0,1\}
$$

或更一般的 effect class。

一旦：

$$
Effect(a_j)=1,
$$

其 recovery 成本通常顯著不同。

---

# 12. Compensating Action 與真正 Rollback

若外部效果無法直接撤銷，系統只能執行 compensating action：

$$
a
\rightarrow
X'
\rightarrow
a^{-}
\rightarrow
X''.
$$

通常：

$$
X''
\neq
X.
$$

例如寄錯郵件後再寄道歉信，不代表第一封郵件從歷史消失。

所以：

$$
\boxed{
\text{Compensation}
\neq
\text{Inverse History}.
}
$$

這也是為什麼世界歷史時間與 sandbox runtime 必須分開。

---

# 13. Validation 也是 Action

驗證不應被當成輸出後的附註。

Validator 本身是：

$$
v_j
=
\text{observable action}.
$$

其可能讀 artifact、跑 test、比對 schema、檢查 policy、重算數學、取得外部 evidence 或觸發人工 review。

因此完整 trajectory 包含：

$$
Execution
\rightarrow
Validation
\rightarrow
PossibleRecovery.
$$

而不是：

$$
Execution
\rightarrow
Done.
$$

---

# 14. Inference-Time Reviewer

近期 tool-agent 研究開始把 reviewer 直接放入 execution loop，在工具真正執行前評估 provisional action。

可以寫成：

$$
a_j^{proposal}
\rightarrow
Reviewer
\rightarrow
\begin{cases}
Execute,\\
Revise,\\
Reject.
\end{cases}
$$

這使：

$$
\text{Validation}
$$

不再只存在於終點。

它可以分布於整條 trajectory。

---

# 15. Observation 不是被動訊息

每個 tool output：

$$
o_j
$$

都會改變後續狀態。

Agent 必須執行：

$$
\widehat o_j
=
Interpret(o_j).
$$

因此可能發生：

$$
o_j
\neq
\widehat o_j.
$$

即工具本身正確，但 Agent 誤讀輸出。

這是獨立失敗類型。

所以：

$$
\boxed{
\text{Tool Success}
\neq
\text{Observation Success}.
}
$$

---

# 16. Execution Provenance

外部工具與資料來源越多，僅保存最終答案越不足。

本文定義 provenance relation：

$$
\mathcal P_E
\subseteq
Source
\times
Event
\times
Claim
\times
Artifact.
$$

它回答：

- 這個 action 由什麼資訊觸發？
- 這個 output 來自哪個工具？
- 哪個 claim 依賴哪個 observation？
- 哪個 artifact 由哪些 event 產生？
- 哪個外部 state change 由哪個授權 action 造成？

因此：

$$
\boxed{
\text{Trace}
\rightarrow
\text{Provenance}
\rightarrow
\text{Auditability}.
}
$$

---

# 17. Trace 不等於 Chain-of-Thought

本文要求的 trace 可以包含 action type、tool name、tool arguments 的必要摘要、tool output reference、state transition、validator result、retry / recovery、resource cost、artifact lineage、commit record。

本文不要求：

$$
\text{private hidden reasoning}
$$

被逐字保存或公開。

所以：

$$
\boxed{
\text{Execution Trace}
\neq
\text{Private Chain-of-Thought}.
}
$$

---

# 18. No-Op 與低價值動作

不是每一個 action 都造成進展。

定義：

$$
\Delta Comp_j
=
Comp(S_{j+1})
-
Comp(S_j).
$$

若：

$$
\Delta Comp_j
\approx0,
$$

且沒有新增有效 evidence、排除路徑或降低風險，則可稱為近似 no-op。

但需注意：

$$
\Delta Comp_j=0
$$

不必然表示沒有價值。

例如失敗測試可能：

$$
\Delta Knowledge_j>0.
$$

因此更完整地：

$$
Value(a_j)
=
f
\left(
\Delta Comp_j,
\Delta K_j,
\Delta Risk_j,
\Delta Reach_j
\right).
$$

---

# 19. 重複動作與無效 Retry Loop

若：

$$
a_{j+1}
\approx
a_j
$$

且：

$$
o_{j+1}
\approx
o_j,
$$

又沒有新的策略或資訊：

$$
\Delta K
\approx0,
$$

則系統可能進入 retry loop。

定義局部重複率：

$$
\rho_R
=
\frac{
N_{\mathrm{redundant\ retry}}
}{
N_{\mathrm{attempt}}
}.
$$

高：

$$
\rho_R
$$

表示 agent 可能正在消耗互動時間而沒有實質狀態增益。

---

# 20. Infinite Deliberation 與 Analysis Paralysis

如果：

$$
K_r
\rightarrow
\infty
$$

但：

$$
\Delta Comp
\rightarrow0,
$$

或者：

$$
C_{\mathrm{delib}}
\gg
ExpectedGain,
$$

則深度推理本身成為瓶頸。

因此：

$$
\boxed{
\text{More Deliberation}
\not\Rightarrow
\text{Better Action}.
}
$$

這不是反對深度推理，而是要求 deliberation 也接受成本—收益判斷。

---

# 21. Deliberation Gate

可以建立：

$$
ContinueDeep
=
\mathbb I
\left[
E[\Delta V_{\mathrm{next}}]
>
C_{\mathrm{next}}
\right].
$$

若：

$$
E[\Delta V_{\mathrm{next}}]
\le
C_{\mathrm{next}},
$$

系統應傾向 commit、ask human、use fallback、terminate 或 defer，而不是無限展開。

---

# 22. Turn Expansion Factor

本文提出一個簡單但有用的描述量：

$$
X_r
=
\frac{
N_{\mathrm{effective\ events}}^{(r)}
}{
1\ \mathrm{visible\ turn}
}.
$$

因此：

$$
X_r
=
N_{\mathrm{effective\ events}}^{(r)}.
$$

其用途不是宣稱 action 越多越好，而是表示：

> 一個 visible turn 被展開成多少可觀測執行事件。

不同 Agent harness 可能：

$$
X_r
$$

差距極大。

---

# 23. Quality-Adjusted Turn Expansion

若每個事件權重：

$$
w_j
=
Value(e_j),
$$

則：

$$
X_r^{Q}
=
\sum_jw_j.
$$

這比單純計算 tool calls 更合理。

但 $w_j$ 必須任務相對。

因此：

$$
\boxed{
X_r^Q
\text{ is a projection, not an ontological universal constant}.
}
$$

---

# 24. Action Density 與 Human Intervention

定義 machine action density：

$$
\rho_A
=
\frac{
N_{\mathrm{effective\ actions}}
}{
T_H^{active}+\epsilon
}.
$$

若自主程度提高：

$$
\rho_A\uparrow.
$$

但仍須與：

$$
Q_{\mathrm{result}},
\qquad
Q_{\mathrm{verification}},
\qquad
D_V
$$

一起評估。

否則「少問人、多做事」可能只是更快地做錯。

---

# 25. Partial Progress

長時程任務不應只使用：

$$
Success\in\{0,1\}.
$$

可以定義 checklist 或完成向量：

$$
\mathbf C
=
(c_1,c_2,\ldots,c_m).
$$

則：

$$
Progress
=
\frac{
\sum_iw_ic_i
}{
\sum_iw_i
}.
$$

這使早期失敗、中途 recovery、部分完成、rollback 後恢復可以被更精確評估。

近期 AgentRewind 也以 task success 與 average checklist progress 同時評估 recoverable execution。

---

# 26. Trajectory Quality

定義：

$$
Q_{\mathrm{traj}}
=
f
\left(
Q_{goal},
Q_{action},
Q_{efficiency},
Q_{observation},
Q_{verification},
Q_{recovery},
Q_{provenance}
\right).
$$

因此：

$$
\boxed{
Q_{\mathrm{traj}}
\neq
Q_{\mathrm{final}}.
}
$$

---

# 27. 失敗發生點與失敗顯現點不同

令：

$$
e_c
=
\text{causal error event},
$$

$$
e_s
=
\text{surface failure event}.
$$

一般可能：

$$
e_c
\prec
e_s.
$$

甚至相隔很多步。

因此：

$$
\boxed{
\text{Where Failure Appears}
\neq
\text{Where Failure Begins}.
}
$$

這是 trajectory-based debugging 的必要性。

---

# 28. Detect–Attribute–Recover–Rerun

本文提出一個通用修復閉環：

$$
Detect
\rightarrow
Attribute
\rightarrow
Recover
\rightarrow
Rerun.
$$

若沒有 Attribute，系統可能只是不斷換答案，而不知道錯在哪裡。

---

# 29. Parallel Actions 與單輪內非線性

多 Agent 系統中：

$$
a_1
\parallel
a_2
\parallel
a_3.
$$

所以單輪內事件未必存在唯一全序。

本文只在此建立：

$$
e_i
\prec
e_j
$$

表示因果先後。

完整的偏序拓撲與 critical path 將留給第 4 篇。

因此本篇只提出：

$$
\boxed{
\text{Single Turn}
\text{ can contain a partially ordered execution set}.
}
$$

---

# 30. Branch 與 Attempt Lineage

如果 Agent 從同一 checkpoint 生成兩條候選：

$$
C_q
\rightarrow
\begin{cases}
B_1,\\
B_2.
\end{cases}
$$

則必須保存 lineage：

$$
Parent(B_1)=C_q,
$$

$$
Parent(B_2)=C_q.
$$

不能在事後只留下成功 branch，假裝失敗 branch 從未存在。

失敗 branch 可能包含重要 evidence。

---

# 31. Branch Explosion

若每層平均分支數為：

$$
b,
$$

深度：

$$
d,
$$

則候選節點可能近似：

$$
b^d.
$$

因此「更多探索」可能快速消耗：

$$
B_{\mathrm{compute}},
\qquad
B_{\mathrm{token}},
\qquad
B_{\mathrm{verification}}.
$$

這也是為什麼 Agent runtime 需要 Governor 或 tractability gate。

---

# 32. Run 狀態機

第一代 Run state：

$$
\mathcal S_R
=
\{
CREATED,
RESOLVED,
PLANNED,
RUNNING,
SUSPENDED,
VALIDATING,
SUCCEEDED,
FAILED,
CANCELLED
\}.
$$

成功：

$$
CREATED
\rightarrow
RESOLVED
\rightarrow
PLANNED
\rightarrow
RUNNING
\rightarrow
VALIDATING
\rightarrow
SUCCEEDED.
$$

恢復：

$$
RUNNING
\rightarrow
SUSPENDED
\rightarrow
RUNNING.
$$

終止：

$$
RUNNING
\rightarrow
FAILED.
$$

若重新執行：

$$
Run_m
\rightarrow
Run_{m+1},
$$

而不是：

$$
Run_m^{history}
\leftarrow
\text{silent rewrite}.
$$

---

# 33. Execution Budget

一輪內總預算：

$$
B_r
=
(
B_{token},
B_{compute},
B_{tool},
B_{wall},
B_{risk},
B_{human}
).
$$

每個事件消耗：

$$
c(e_j).
$$

需滿足：

$$
\sum_jc(e_j)
\preceq
B_r.
$$

因此 Agent 的控制問題之一是：

$$
\boxed{
\text{Which next event is worth its cost?}
}
$$

這將在第 5 篇正式進入 AI 計算時間經濟學。

---

# 34. Execution Time Ledger

本文提出第 3 篇所需的 runtime ledger：

```text
Run
  run_id
  intent_version
  plan_version
  interaction_round
  attempt_id
  parent_attempt_id
  branch_id
  loop_id
  event_id
  parent_event_ids
  actor
  event_type
  action_type
  tool
  input_ref
  output_ref
  observation_ref
  state_before_ref
  state_after_ref
  artifact_refs
  checkpoint_ref
  retry_of
  replan_from
  recovery_type
  side_effect_class
  validator_refs
  budget_before
  budget_after
  completion_before
  completion_after
  status
  world_commit_ref
  provenance_ref
```

---

# 35. 可檢驗命題

## 命題一：Turn 非等價命題

存在：

$$
R_1,
R_2
$$

使：

$$
N_{\mathrm{turn}}(R_1)
=
N_{\mathrm{turn}}(R_2)=1,
$$

但：

$$
N_{\mathrm{event}}(R_1)
\neq
N_{\mathrm{event}}(R_2).
$$

## 命題二：Action 數不足命題

存在：

$$
N_{\mathrm{action}}(A)
>
N_{\mathrm{action}}(B),
$$

但：

$$
\Delta Comp_A
<
\Delta Comp_B.
$$

所以 tool call 數不能單獨代表有效進展。

## 命題三：Recovery 增益命題

對部分長時程任務，允許 checkpoint + recovery 的 Agent：

$$
P_{success}^{recoverable}
>
P_{success}^{restart-only}.
$$

## 命題四：失敗延遲顯現命題

存在 trajectory，使：

$$
e_c
\prec
e_s
$$

且：

$$
d(e_c,e_s)\gg1.
$$

所以只檢查最後幾步可能無法定位根因。

## 命題五：無限 deliberation 損失命題

存在任務區間，使：

$$
\frac{
\partial ExpectedValue
}{
\partial C_{\mathrm{delib}}
}
\le0.
$$

因此更深思考存在邊際收益轉負的可能。

## 命題六：Side-effect asymmetry 命題

對相同邏輯錯誤，若發生在：

$$
a^{pure}
$$

與：

$$
a^{effect},
$$

其 recovery cost 一般不同。

---

# 36. 實驗設計

## 36.1 Same Turn / Different Work

固定單一 user turn，讓不同 Agent harness 執行同一任務。

比較：

$$
K_r,
\qquad
N_{\mathrm{action}},
\qquad
N_{\mathrm{validator}},
\qquad
N_{\mathrm{retry}},
\qquad
\Delta Comp,
\qquad
Cost.
$$

## 36.2 Retry vs Replan

建立一個初始策略必定失敗的任務。

比較 naïve retry、explicit replan、checkpoint recovery。

測量成功率與成本。

## 36.3 Early Error Propagation

在第：

$$
j=3
$$

步注入錯誤。

觀察 failure 何時顯現，以及不同診斷器能否定位：

$$
e_c.
$$

## 36.4 Side-Effect Recovery

讓 sandbox action 與不可逆模擬 external action 使用相同邏輯。

比較 rollback 與 compensation 的語義差異。

## 36.5 Trace Ablation

分別只保留：

1. final output；
2. tool-call list；
3. full event lineage。

測試 failure attribution、recovery 與 audit quality。

---

# 37. 與外部長時程 Agent 研究的接口

SWE-Marathon 類 benchmark 已顯示長時程 Agent 執行可以消耗極大量 token、工具與環境步驟，且現有前沿 Agent 對超長任務仍具有顯著失敗率。

Execution provenance 研究則指出，最終答案無法回答工具為何被呼叫、輸出來自哪個 evidence、memory 如何影響後續行動、失敗起點在哪裡、外部 state 是否被合法修改。

AgentRewind、Crab、DeltaBox 等工作進一步說明 checkpoint、restore、branch 與 rollback 已開始成為 Agent runtime 的一級工程問題。

因此：

$$
\boxed{
\text{Agent Evaluation}
\rightarrow
\text{Trajectory Evaluation}
\rightarrow
\text{Recoverable Runtime Evaluation}.
}
$$

---

# 38. 與 ISF v0.3 的映射

ISF v0.3 已建立：

$$
Runtime_{0.3}
=
(E,A,S,C,R,K,B,I),
$$

其中：

- $E$：Event Store；
- $A$：Artifact Store；
- $S$：Scheduler；
- $C$：Checkpoint / Replay；
- $R$：Retry / Recovery；
- $K$：Cache；
- $B$：Budget；
- $I$：Isolation。

本篇可直接映射：

$$
Event
\leftrightarrow
e_j,
$$

$$
Checkpoint
\leftrightarrow
C_q,
$$

$$
Retry/Recovery
\leftrightarrow
\mathcal R,
$$

$$
Budget
\leftrightarrow
B_r.
$$

因此本文不是為 ISF 重新發明 runtime。

它做的是：

$$
\boxed{
\text{把既有 runtime execution semantics 納入互動時間的正式測量層}.
}
$$

---

# 39. 與 WDC 的接口

WDC 已區分：

$$
t
=
\text{parent historical time},
$$

$$
k
=
\text{deliberation iteration},
$$

$$
\tau
=
\text{world-local runtime}.
$$

本篇增加 visible interaction round：

$$
r.
$$

因此可形成：

$$
\boxed{
(t,r,k,j,\tau).
}
$$

其中：

- $t$：外部歷史；
- $r$：人機回合；
- $k$：AI 內部控制迴圈；
- $j$：具體 action；
- $\tau$：局部執行環境時間。

這些時間索引不得被混成單一 `time` 欄位。

---

# 40. 規範與倫理邊界

本框架不應被用來：

- 把 action 數量當 KPI；
- 鼓勵 Agent 為提高「工作量」故意多呼叫工具；
- 以可見 turn 少宣稱自主性高；
- 用大量 hidden computation 掩飾低效率；
- 把 checkpoint 當成可以抹除真實世界後果；
- 讓 retry 繞過原本權限；
- 將 recovery 變成重複執行危險動作；
- 以完整 trace 為由不必要地保存敏感資料；
- 要求公開私有 chain-of-thought；
- 把 simulator / sandbox side effect 當成真實世界 commit。

---

# 41. 理論限制

第一，內部 deliberation 的實際步數對閉源模型通常不可完全觀測。

第二，tool call 與 action 的粒度取決於 runtime，跨框架比較需要正規化。

第三，一個「有效 event」仍具有任務相對性。

第四，checkpoint 成本在不同環境差異巨大。

第五，side-effect reversibility 不是二值問題，而可能是連續光譜。

第六，並行 Agent 的完整偏序結構在本篇只建立接口，正式數學化留待第 4 篇。

---

# 42. 與第 4 篇的接口

本篇已建立：

$$
1\text{ Turn}
\neq
1\text{ Step},
$$

且同一 turn 中可能：

$$
a_1
\parallel
a_2
\parallel
a_3.
$$

因此下一篇不能再使用單一線性步數描述互動時間。

第 4 篇將正式建立：

$$
G_I
=
(V_I,E_I,\prec),
$$

並區分：

$$
W_I
=
\text{Interaction Work},
$$

與：

$$
D_I
=
\text{Interaction Depth}.
$$

也就是：

> 一個系統總共做了多少工作，與它從意圖到結果真正跨越了多深的不可約因果路徑，是兩個不同問題。

---

# 43. 結論

本文提出：

$$
\boxed{
1\text{ Turn}
\neq
1\text{ Step}.
}
$$

一個 AI turn 可能是一個極短的直接映射，也可能是一個包含：

$$
\text{Plan}
+
\text{Deliberation}
+
\text{Tool Use}
+
\text{Observation}
+
\text{Validation}
+
\text{Retry}
+
\text{Replan}
+
\text{Recovery}
+
\text{Checkpoint}
+
\text{Commit}
$$

的完整執行宇宙。

因此：

$$
\boxed{
\text{Visible Turn}
\neq
\text{Execution Work}
\neq
\text{Execution Depth}
\neq
\text{World Effect}.
}
$$

如果只看最終訊息，人類看到的可能只有：

> 完成了。

但這個「完成了」背後可能包含數十、數百乃至更多可區分的機器狀態轉換。

反過來，一段很長的回應也可能沒有任何外部執行與驗證。

所以 AI-native 時間測量不能停留在：

$$
\text{messages},
$$

$$
\text{tokens},
$$

或：

$$
\text{wall-clock seconds}.
$$

最低限度需要同時保存：

$$
\boxed{
\text{Round}
\rightarrow
\text{Loop}
\rightarrow
\text{Action}
\rightarrow
\text{Observation}
\rightarrow
\text{Validation}
\rightarrow
\text{Recovery}
\rightarrow
\text{Commit}.
}
$$

這使「單次品質」第一次具有可被執行系統直接觀測的內部結構，也為下一篇的互動時間拓撲奠定基礎。

---

# 參考文獻與前置理論

## EveMissLab 前置理論

1. Neo.K，《互動時間論：從鐘錶時間到意圖驅動的智能狀態轉換》v0.1，EveMissLab，2026。
2. Neo.K，《意圖週期論：使用者意圖、AI 接受、執行與結果的閉環結構》v0.1，EveMissLab，2026。
3. Neo.K，《Intent-to-System Flow Execution Runtime Specification》v0.3，EveMissLab，2026。
4. Neo.K，《Intent-to-System Flow Protocol Kernel》v0.2，EveMissLab，2026。
5. Neo.K，《時間迴圈分類學：一種面向長時程程式、AI Agent 與人機協作的通用控制流理論》，EveMissLab，2026。
6. Neo.K，《WDC-08: Tri-Temporal World-Domain Computation》，EveMissLab，2026。
7. Neo.K，《World-Domain Cognitive Runtime v0.1 Technical Whitepaper》，EveMissLab，2026。

## 外部研究

8. Zhuang, Y., Chen, K., Duan, Y., Zheng, S., Li, J., Zhang, X.-Y. *AgentRewind: Recoverable Execution for Long-Horizon LLM Agents*. arXiv:2608.14380, 2026.
9. Wu, T., et al. *Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes*. arXiv:2604.28138, 2026.
10. *DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Checkpointing*. arXiv:2605.22781, 2026.
11. Wang, Y., et al. *From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents*. arXiv:2606.04990, 2026.
12. *AgentDebugX: An Open-Source Toolkit for Failure Attribution and Recovery in LLM Agents*. arXiv:2607.18754, 2026.
13. *SWE-Marathon: Can Agents Autonomously Complete Ultra Long-Horizon Technical Tasks?* arXiv:2606.07682, 2026.
14. Ta, A., Zhu, J., Shayandeh, S. *Reinforced Agent: Inference-Time Feedback for Tool-Calling Agents*. arXiv:2604.27233, 2026.
15. *Intervention-Supported Error Attribution for Silent Failures in LLM Agents*. arXiv:2606.09071, 2026.

---

## 一句話版本

> **AI 的一個可見回合只是介面表面；真正的智能工作存在於其內部可追蹤的 loop、action、observation、validation、recovery 與 commit 軌跡之中。**

---

*EML-ITT-2026-03-v0.1*  
*AI 互動時間與智能時間經濟學系列 03/08*
