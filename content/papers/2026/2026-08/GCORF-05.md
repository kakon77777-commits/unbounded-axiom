# GCORF-05
## 人–AI共同底空間與內外部學習：從參數更新到外部狀態、協議與共享認知域演化
### Human–AI Shared Bottom Spaces and Internal–External Learning: From Parameter Updates to External State, Protocol, and Shared Cognitive-Domain Evolution

**作者／理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-15  
**版本：** v0.1  
**系列：** General Cognitive Operator Reverse-Engineering Framework (GCORF) — Canonical Core Paper 05

---

## 摘要

GCORF-00 至 GCORF-04 已建立認知算子的證據逆向、部分組合代數、Spectrum–Bound–License 結構，以及可重新打開的動靜生命週期。本文處理 GCORF 的另一個中央問題：**在實際人–AI共同研究中，究竟什麼東西正在「學習」？**

傳統機器學習語境容易把學習壓縮為模型參數更新：

$$
\theta_{t+1}\neq\theta_t.
$$

然而在現代 AI 系統中，即使模型權重維持：

$$
\theta_{t+1}=\theta_t,
$$

系統仍可能因 context、retrieval、persistent memory、tool state、operator library、routing policy、interaction protocol、shared artifacts 與 human–AI mutual models 的改變，而在未來相同或相關問題上產生系統性不同的行為。GCORF 將此類現象形式化為 **Behaviorally Effective State Adaptation（BESA）**，並進一步區分：

$$
\boxed{
ParameterUpdate,
ContextUpdate,
MemoryUpdate,
RetrievalUpdate,
ToolStateUpdate,
OperatorUpdate,
ProtocolUpdate,
BottomSpaceUpdate.
}
$$

本文不將所有狀態變化都稱為學習。只有當變化能被保存、重新調用、影響後續判定／路由／行為，並通過 retention、reusability、transfer 或 performance/discriminability test 時，才可升格為 GCORF 意義下的 learning event。

本文同時提出 **Human–AI Shared Bottom Space**：

$$
\boxed{
\mathcal B_t
=
\Phi(
H_t,
A_t,
\widehat H_t^A,
\widehat A_t^H,
\Pi_t,
E_t,
K_t,
T_t,
\mathcal H_t
).
}
$$

其中共同底空間不是外部世界本身，也不是人或 AI 任一方的完整內部狀態，而是當下共同研究實際可訪問、可表達、可判定、可協作與可延伸的共享操作域。相同問題 $P$ 在不同人、不同模型、不同協議、不同記憶與工具條件下，可誘發不同的有效底空間：

$$
\mathcal B(P\mid H,A,\Pi)
\neq
\mathcal B(P\mid H',A',\Pi').
$$

因此人–AI共同認知不是單向「人給提示、AI輸出」，而是一個雙方與共享底空間共同演化的廣義雙生動力系統：

$$
\boxed{
(
H_t,
A_t,
\mathcal B_t,
\Pi_t
)
\longrightarrow
(
H_{t+1},
A_{t+1},
\mathcal B_{t+1},
\Pi_{t+1}
).
}
$$

本文最後建立 learning-event admission、external-state provenance、bottom-space drift、coupling gain、context contamination、memory hallucination、retrieval lock-in、protocol overfitting 與 false-learning 等失效模式。GCORF-05 的目的不是擴大「學習」一詞直到失去意義，而是建立一個可區分：**什麼改了、改在哪一層、是否可保留、是否可重用、是否真正改變未來認知行為**的計算認識論。

**關鍵詞：** Human–AI Coupling, Shared Bottom Space, External-State Learning, In-Context Adaptation, Persistent Memory, Retrieval, Operator Update, Protocol Update, Behavioral Adaptation, Cognitive Co-Evolution

---

# 1. 問題的提出

對一個固定權重模型：

$$
A_{\theta},
$$

若今天它透過：

- 新 context；
- 新檔案；
- 新資料庫；
- 新記憶；
- 新工具；
- 新 operator library；
- 新 routing policy；

完成昨天做不到的研究，應如何描述？

若只允許：

$$
\theta_{t+1}\neq\theta_t
$$

才叫學習，則大量真實 AI runtime adaptation 會被排除。

但若任何：

$$
State_{t+1}\neq State_t
$$

都叫學習，則「視窗多了一行字」也會被誤叫 learning。

因此 GCORF 必須建立更細分類。

---

# 2. 最小系統表示

定義人–AI共同研究系統：

$$
\boxed{
\mathcal J_t
=
(
H_t,
A_t,
\theta_t,
C_t,
M_t,
R_t,
T_t,
\mathfrak O_t,
\Pi_t,
\mathcal B_t,
\mathcal H_t
).
}
$$

其中：

- $H_t$：human state；
- $A_t$：AI runtime；
- $\theta_t$：AI model parameters；
- $C_t$：active context；
- $M_t$：persistent / semi-persistent memory；
- $R_t$：retrieval state / index / policy；
- $T_t$：tools and tool-state；
- $\mathfrak O_t$：operator library；
- $\Pi_t$：protocol / routing policy；
- $\mathcal B_t$：shared bottom space；
- $\mathcal H_t$：interaction history。

---

# 3. Internal Parameter Learning

最狹義的模型內部學習：

$$
\boxed{
\theta_{t+1}\neq\theta_t.
}
$$

例如：

- training；
- fine-tuning；
- adapter update；
- continual parameter learning。

此類學習會直接修改模型內部可泛化表示。

---

# 4. Weight-Fixed Adaptation

若：

$$
\boxed{
\theta_{t+1}=\theta_t
}
$$

但：

$$
\boxed{
\mathcal J_{t+1}\neq\mathcal J_t,
}
$$

則必須進一步判定變化發生在哪個外部層。

---

# 5. Context Update

定義：

$$
\boxed{
C_{t+1}
=
UpdateContext(
C_t,x_t
).
}
$$

Active context 的改變可立刻改變模型行為。

但 context update 通常：

- 短期；
- session-dependent；
- 可能在 context drop 後消失。

因此：

$$
\boxed{
ContextUpdate
\neq
PersistentLearning.
}
$$

---

# 6. In-Context Adaptation

若模型在同一 active context 中根據例子或回饋調整行為：

$$
A_{\theta}(x\mid C_t)
\rightarrow
A_{\theta}(x\mid C_{t+1}),
$$

可稱：

$$
\boxed{
InContextAdaptation.
}
$$

但除非狀態可持久化，不應自動稱為 long-term learning。

---

# 7. Persistent Memory Update

定義：

$$
\boxed{
M_{t+1}
=
Write(
M_t,
m_t
).
}
$$

若未來 runtime 能重新取回：

$$
m_t,
$$

並影響後續判斷，則形成 persistent external state。

---

# 8. Memory 不等於 Truth

寫入 memory：

$$
m
$$

不代表：

$$
Truth(m)=1.
$$

因此 memory record 必須保留：

- source；
- confidence；
- timestamp；
- context；
- revision；
- invalidation state。

---

# 9. Memory Learning Event

只有當：

$$
\boxed{
Retain
\land
Retrieve
\land
Reuse
}
$$

成立時，才將 memory update 升格為：

$$
\boxed{
MemoryLearningEvent.
}
$$

單純寫入但永不被使用，只是 storage mutation。

---

# 10. Retrieval Update

Retrieval state：

$$
R_t
$$

包含：

- index；
- embedding；
- search policy；
- reranker；
- source weighting；
- query transformation。

若：

$$
R_{t+1}\neq R_t,
$$

則即使：

$$
M_{t+1}=M_t,
$$

也可能使系統可取得完全不同的知識。

---

# 11. Retrieval Learning

定義：

$$
\boxed{
RetrievalLearning
}
$$

為 retrieval policy / representation 的持久變更，且能在後續任務改善：

$$
Recall,
Precision,
Discriminability,
Coverage.
$$

---

# 12. Retrieval Lock-In

若 retrieval 長期只強化既有來源：

$$
SourceWeight_t
\rightarrow
SourceWeight_{t+1}\uparrow,
$$

可能形成：

$$
\boxed{
RetrievalLockIn.
}
$$

使系統誤以為「越來越確定」，實際只是越來越只看同一批證據。

---

# 13. Tool-State Update

工具也具有狀態：

$$
T_t.
$$

例如：

- repository checkout；
- database schema；
- solver cache；
- browser session；
- external agent workspace；
- generated code；
- experimental results。

因此工具不是永遠無狀態函數。

---

# 14. Tool-Mediated Learning

如果：

$$
T_{t+1}
$$

保存了可重用結果，使後續研究空間發生持續改變，可以稱：

$$
\boxed{
ToolMediatedLearning.
}
$$

例如 proof assistant 中新增已驗證 lemma。

---

# 15. Operator Update

GCORF 最重要的外部學習層之一：

$$
\boxed{
\mathfrak O_t
\rightarrow
\mathfrak O_{t+1}.
}
$$

可能：

- 新增 operator；
- 修訂 operator；
- cluster compression；
- 新 composition；
- license change；
- failure rule change。

---

# 16. Operator Learning

若新 operator 能：

$$
\boxed{
\text{被識別}
+
\text{被保存}
+
\text{被重新路由}
+
\text{跨案例重用},
}
$$

則形成：

$$
\boxed{
OperatorLearningEvent.
}
$$

這比「AI 記住一句話」更接近方法論學習。

---

# 17. Protocol Update

定義：

$$
\boxed{
\Pi_t
\rightarrow
\Pi_{t+1}.
}
$$

Protocol 可包含：

- turn-taking；
- tool order；
- verification gates；
- multi-agent routing；
- source requirements；
- stop conditions；
- escalation rules。

---

# 18. Protocol Learning

若系統從 execution history 得到：

$$
\Pi_{t+1}
=
LearnPolicy(
\Pi_t,
\mathcal H_t
),
$$

並在後續任務中系統性改變行為，可稱：

$$
\boxed{
ProtocolLearning.
}
$$

---

# 19. Protocol Overfitting

如果新 protocol 只對：

$$
P_0
$$

有效，卻被全域部署：

$$
\forall P,\Pi_{new},
$$

則形成：

$$
\boxed{
ProtocolOverfitting.
}
$$

---

# 20. Bottom-Space Update

本文提出：

$$
\boxed{
\mathcal B_t
\rightarrow
\mathcal B_{t+1}.
}
$$

作為 GCORF 最廣義但也最需嚴格控制的外部學習層。

---

# 21. Shared Bottom Space

定義：

$$
\boxed{
\mathcal B_t
=
\Phi(
H_t,
A_t,
\widehat H_t^A,
\widehat A_t^H,
\Pi_t,
E_t,
K_t,
T_t,
\mathcal H_t
).
}
$$

其中：

- $\widehat H_t^A$：AI 對 human 的工作模型；
- $\widehat A_t^H$：human 對 AI 的工作模型；
- $E_t$：environment / available evidence；
- $K_t$：shared knowledge artifacts；
- $T_t$：tools；
- $\Pi_t$：protocol。

---

# 22. Bottom Space 不是「世界本身」

$$
\boxed{
\mathcal B_t
\neq
Reality.
}
$$

它只表示當前 joint system 能夠：

- 訪問；
- 表達；
- 比較；
- 操作；
- 驗證；
- 連接；

的有效共同操作域。

---

# 23. Bottom Space 也不是兩者知識交集

簡單交集：

$$
K_H\cap K_A
$$

過於狹窄。

因為人與 AI 可以透過互補建立：

$$
\boxed{
\mathcal B_t
\supset
K_H\cap K_A.
}
$$

例如人提供意圖與 meta-direction，AI 提供大規模檢索與計算，兩者形成任一單方都未完整持有的 joint reachable space。

---

# 24. Bottom-Space Reachability

定義：

$$
\boxed{
Reach(
x
\mid
\mathcal B_t
)
}
$$

表示 joint system 是否能在有限操作鏈內到達、表示或驗證 $x$。

---

# 25. Problem-Conditioned Bottom Space

相同 joint system 面對不同問題：

$$
P_1,P_2
$$

可以誘發：

$$
\boxed{
\mathcal B_t(P_1)
\neq
\mathcal B_t(P_2).
}
$$

因此 bottom space 不必是單一全域容器。

---

# 26. Observer-Conditioned Bottom Space

對不同人：

$$
H_1,H_2,
$$

即使 AI 相同：

$$
A,
$$

也可能：

$$
\boxed{
\mathcal B(P\mid H_1,A,\Pi)
\neq
\mathcal B(P\mid H_2,A,\Pi).
}
$$

---

# 27. AI-Conditioned Bottom Space

同一 human：

$$
H,
$$

換不同 AI：

$$
A_1,A_2,
$$

可能：

$$
\boxed{
\mathcal B(P\mid H,A_1,\Pi)
\neq
\mathcal B(P\mid H,A_2,\Pi).
}
$$

---

# 28. Protocol-Conditioned Bottom Space

即使：

$$
H,A
$$

都不變，

只要：

$$
\Pi_1\neq\Pi_2,
$$

也可能產生：

$$
\boxed{
\mathcal B(P\mid H,A,\Pi_1)
\neq
\mathcal B(P\mid H,A,\Pi_2).
}
$$

---

# 29. Bottom-Space Expansion

若：

$$
Reach_{t+1}
>
Reach_t
$$

且新區域可被合法訪問、驗證或操作：

$$
\boxed{
\mathcal B_t
\Rightarrow_E
\mathcal B_{t+1}.
}
$$

---

# 30. Bottom-Space Expansion 不等於資料增加

新增十萬篇文件：

$$
|E_{t+1}|\gg|E_t|
$$

不代表：

$$
\mathcal B_{t+1}
$$

一定更好。

如果檢索不到、無法理解、無法驗證，則只是 passive storage growth。

---

# 31. Bottom-Space Contraction

若：

- tool unavailable；
- memory deleted；
- context pruned；
- permission changed；
- source invalidated；

則：

$$
\boxed{
\mathcal B_{t+1}
\subset
\mathcal B_t.
}
$$

因此 shared cognition 可以退化。

---

# 32. Bottom-Space Distortion

若可達空間增加但偏差放大：

$$
Reach\uparrow,
\quad
Bias\uparrow,
$$

則：

$$
\boxed{
Expansion
\neq
Improvement.
}
$$

---

# 33. Mutual Modeling

人與 AI 都會形成對彼此的模型：

$$
\boxed{
\widehat H_t^A,
\quad
\widehat A_t^H.
}
$$

這些模型影響：

- 提問方式；
- 解釋粒度；
- 工具選擇；
- 信任；
- 驗證策略；
- 路由。

---

# 34. Mutual-Model Error

若：

$$
\widehat H_t^A
\not\approx
H_t
$$

或：

$$
\widehat A_t^H
\not\approx
A_t,
$$

可能產生：

$$
\boxed{
CouplingMisalignment.
}
$$

例如 AI 誤判 human 已理解某前提，或 human 誤判 AI 已持久記住某資訊。

---

# 35. Joint Dynamics

人–AI共同系統：

$$
\boxed{
(
H_t,
A_t,
\mathcal B_t,
\Pi_t
)
\rightarrow
(
H_{t+1},
A_{t+1},
\mathcal B_{t+1},
\Pi_{t+1}
).
}
$$

---

# 36. Human State Update

$$
H_{t+1}\neq H_t
$$

可能來自：

- 新理解；
- 新問題表述；
- 新偏好；
- 新方法習得；
- 新錯誤修正；
- cognitive fatigue；
- goal shift。

因此 human 也不是固定 controller。

---

# 37. AI Runtime Update

即使 $\theta$ 不變：

$$
A_{t+1}\neq A_t
$$

若其 runtime state：

$$
C,M,R,T,\mathfrak O,\Pi
$$

改變。

---

# 38. Generalized Twin Dynamics

本文將此稱為：

$$
\boxed{
GeneralizedTwinDynamics.
}
$$

因為不是只有 human 和 AI 兩個點。

真正耦合的是：

$$
\boxed{
H
+
A
+
\mathcal B
+
\Pi
+
\mathcal H.
}
$$

---

# 39. Learning Taxonomy

GCORF-05 v0.1 定義：

$$
\boxed{
\mathcal L
=
\{
L_\theta,
L_C,
L_M,
L_R,
L_T,
L_O,
L_\Pi,
L_B
\}.
}
$$

分別代表：

- parameter；
- context；
- memory；
- retrieval；
- tool-state；
- operator；
- protocol；
- bottom-space。

---

# 40. Learning Event

定義：

$$
\boxed{
\ell_t
=
(
Layer,
Before,
Update,
After,
Retention,
Reuse,
Transfer,
Evidence,
Version
).
}
$$

---

# 41. Learning Admission

不是所有 update 都是 learning。

定義：

$$
\boxed{
LearningEvent(\Delta)
}
$$

至少要求：

$$
StateChange
\land
BehavioralEffect
\land
Reusability.
$$

較強版本再要求：

$$
Retention
\land
Transfer.
$$

---

# 42. Behaviorally Effective State Adaptation

為避免把「learning」用得過寬，本文引入上位詞：

$$
\boxed{
BESA
=
BehaviorallyEffectiveStateAdaptation.
}
$$

若：

$$
State_{t+1}\neq State_t
$$

且：

$$
Behavior_{future}
$$

受其系統性影響，即可稱 BESA。

---

# 43. Learning 與 BESA 的關係

$$
\boxed{
Learning
\subseteq
BESA.
}
$$

不是所有 BESA 都是 learning。

例如短暫 context adaptation 可能是：

$$
BESA
$$

但沒有 persistence。

---

# 44. Persistence

定義：

$$
\boxed{
P_\ell(\Delta)
}
$$

衡量 update 在時間 / session / restart 後保留程度。

---

# 45. Reusability

定義：

$$
\boxed{
R_\ell(\Delta)
}
$$

衡量同一 state update 是否能在未來相關任務重新被使用。

---

# 46. Transfer

定義：

$$
\boxed{
T_\ell(
\Delta,
D_a\rightarrow D_b
).
}
$$

若 update 只在完全相同 task 有效，transfer 低。

---

# 47. Learning Strength

可以定義多維：

$$
\boxed{
\Sigma_L(\ell)
=
(
Persistence,
Reusability,
Transfer,
BehavioralEffect,
Evidence,
Cost
).
}
$$

仍不壓成一個固定總分。

---

# 48. False Learning

定義：

$$
\boxed{
FalseLearning
}
$$

當系統觀察到輸出改善，但實際沒有可保留的結構改變。

例如：

- random luck；
- easier input；
- hidden source leakage；
- evaluation contamination。

---

# 49. Benchmark Leakage

若 system 因看到答案：

$$
Answer
\in
Context
$$

而表現提升，不能叫：

$$
Learning.
$$

應標：

$$
\boxed{
EvaluationLeakage.
}
$$

---

# 50. Context Contamination

Active context 中錯誤資訊可能：

$$
C_t
\rightarrow
BehaviorError.
$$

若被錯誤寫入 persistent memory：

$$
C_t
\rightarrow
M_{t+1},
$$

污染會升級。

---

# 51. Memory Hallucination

若 memory system 保存：

$$
m
$$

但其 source 不存在／被模型自行補全，則：

$$
\boxed{
MemoryHallucination.
}
$$

必須與普通 model hallucination 分開追蹤。

---

# 52. Stale Memory

若：

$$
m_t
$$

曾經正確，但世界或 project 已更新：

$$
Truth_t(m)\neq Truth_{t+1}(m),
$$

則：

$$
\boxed{
StaleMemory.
}
$$

---

# 53. Memory Invalidation

定義：

$$
\boxed{
Invalidate(
m,
E_{new}
).
}
$$

不能只追加「新記憶」而保留舊錯誤同權重。

---

# 54. Retrieval–Memory Coupling

Memory 存在不代表能取回。

真正有效：

$$
\boxed{
MemoryEffect
=
Write
+
Index
+
Retrieve
+
Route.
}
$$

---

# 55. External Operator Library

可將抽出的 operator 存入：

$$
\boxed{
\mathfrak O^{ext}.
}
$$

AI runtime 可以在每次任務：

$$
RetrieveOperator(P)
\rightarrow
Compose
\rightarrow
Execute.
$$

---

# 56. Operator Externalization

這意味著模型不必在權重內「記住」完整方法。

可以：

$$
\boxed{
Method
\rightarrow
ExternalOperatorObject
\rightarrow
RuntimeRetrieval.
}
$$

---

# 57. Externalization Trade-Off

優點：

- 可版本化；
- 可驗證；
- 可刪除；
- 可替換；
- provenance 清楚。

缺點：

- retrieval dependency；
- latency；
- availability；
- coordination cost。

---

# 58. Parameter vs External Learning

Parameter learning：

$$
\boxed{
\theta_{t+1}\neq\theta_t.
}
$$

External learning：

$$
\boxed{
\theta_{t+1}=\theta_t,
\quad
\mathcal X_{t+1}^{ext}\neq\mathcal X_t^{ext}.
}
$$

其中：

$$
\mathcal X^{ext}
=
(
C,M,R,T,\mathfrak O,\Pi,\mathcal B
).
$$

---

# 59. Hybrid Learning

現實系統可以：

$$
\boxed{
L_{hybrid}
=
L_\theta
+
L_{ext}.
}
$$

兩者不互斥。

---

# 60. Parameter Superiority Fallacy

不能假定：

$$
\boxed{
ParameterUpdate
>
ExternalUpdate.
}
$$

不同任務下：

- 權重學習可能泛化更強；
- 外部 operator 更可審核；
- memory 更易更新；
- retrieval 更易撤銷。

---

# 61. External-State Inferiority Fallacy

也不能因為外部狀態可刪除，就說它不是「真正學習」。

若：

$$
Retention,
Reuse,
Transfer
$$

都成立，其行為效果是真實的。

---

# 62. Learning Location

因此「AI 學到哪裡」應回答：

$$
\boxed{
WhereDidLearningOccur?
}
$$

輸出可能：

$$
\theta,
M,
R,
T,
\mathfrak O,
\Pi,
\mathcal B.
$$

---

# 63. Learning Provenance

每次 learning event 必須保留：

$$
\boxed{
Source
\rightarrow
Update
\rightarrow
StateDelta
\rightarrow
BehaviorDelta.
}
$$

---

# 64. Causal Attribution

若多個層同時更新：

$$
M,R,\Pi
$$

則不能簡單宣稱某一層「造成改善」。

應使用：

$$
\boxed{
Ablation
/
CounterfactualReplay.
}
$$

---

# 65. Learning Attribution Test

比較：

$$
Run(
\mathcal J_{t+1}
)
$$

與：

$$
Run(
\mathcal J_{t+1}
\setminus\Delta_i
).
$$

若移除 $\Delta_i$ 後效果消失，才提高 causal credit。

---

# 66. Joint Learning

有些學習不屬於任何單方。

例如 human 學會如何把問題交給 AI，而 AI external operator library 也因 human feedback 更新。

因此：

$$
\boxed{
JointLearning
}
$$

可以是：

$$
\Delta H
+
\Delta \Pi
+
\Delta\mathfrak O
+
\Delta\mathcal B.
$$

---

# 67. Joint Learning 不等於 Shared Identity

即使高度耦合：

$$
H\neq A.
$$

GCORF 不主張人與 AI 合成單一主體。

共享底空間是：

$$
\boxed{
interaction domain,
}
$$

不是 metaphysical identity。

---

# 68. Asymmetric Learning

人與 AI 的 update rate 可以不同：

$$
v_H
\neq
v_A.
$$

例如 human 長期學到操作習慣，AI session context 卻結束後歸零。

---

# 69. Memory Asymmetry

可能：

$$
M_H
$$

持久，

但：

$$
M_A
$$

不持久。

也可能相反。

因此 joint system continuity 不能只看任一方。

---

# 70. Shared Artifact Continuity

外部 artifact：

$$
K_t
$$

可提供跨 session continuity。

例如：

- papers；
- databases；
- repositories；
- operator records；
- experiment logs；
- canonical snapshots。

---

# 71. Artifact-Mediated Continuity

定義：

$$
\boxed{
Continuity_{artifact}
}
$$

當人與 AI 都能重新讀取同一 artifact，joint bottom space 可以在 session break 後部分恢復。

---

# 72. Context Compression

若 active context 過大：

$$
|C_t|\gg Budget,
$$

需要壓縮。

定義：

$$
\boxed{
CompressContext:
C_t\rightarrow\widetilde C_t.
}
$$

---

# 73. Compression Loss

$$
\boxed{
Loss_C
=
Info(
C_t
)
-
Info(
\widetilde C_t
).
}
$$

如果重要 provenance / failure / constraint 被壓掉，future bottom space 會失真。

---

# 74. External Memory as Expansion–Consolidation Mechanism

GCORF-04 的 lifecycle 可以在 memory layer 實現：

$$
\boxed{
ContextExpand
\rightarrow
Externalize
\rightarrow
Consolidate
\rightarrow
Retrieve.
}
$$

---

# 75. Shared Bottom-Space Snapshot

可建立：

```json
{
  "bottom_space_id": "string",
  "time": "string",
  "human_state_ref": "string",
  "ai_runtime_ref": "string",
  "human_model_of_ai_ref": "string",
  "ai_model_of_human_ref": "string",
  "protocol_ref": "string",
  "knowledge_artifact_refs": [],
  "tool_refs": [],
  "memory_refs": [],
  "operator_library_ref": "string",
  "reachable_domains": [],
  "known_gaps": [],
  "version": "string"
}
```

---

# 76. Learning Event Record

```json
{
  "learning_event_id": "string",
  "layer": "parameter|context|memory|retrieval|tool|operator|protocol|bottom_space",
  "before_ref": "string",
  "after_ref": "string",
  "update_ref": "string",
  "behavioral_effect": {},
  "persistence": "none|session|persistent|unknown",
  "reusability": "low|medium|high|unknown",
  "transfer": "low|medium|high|unknown",
  "evidence_refs": [],
  "status": "BESA|learning|false_learning|unknown",
  "version": "string"
}
```

---

# 77. External-State Record

```json
{
  "state_id": "string",
  "context_ref": "string",
  "memory_ref": "string",
  "retrieval_ref": "string",
  "tool_state_refs": [],
  "operator_library_ref": "string",
  "protocol_ref": "string",
  "bottom_space_ref": "string",
  "timestamp": "string",
  "version": "string"
}
```

---

# 78. Learning Admission Protocol

候選 learning event：

$$
\boxed{
StateDelta
\rightarrow
BehavioralEffect
\rightarrow
Retention
\rightarrow
Reuse
\rightarrow
Transfer
\rightarrow
Attribution
\rightarrow
Admit.
}
$$

---

# 79. Minimum Learning Criterion

v0.1 最低：

$$
\boxed{
StateChange
\land
BehavioralEffect
\land
Reusability.
}
$$

若 persistence 只限 session：

$$
Status=BESA/InContextLearning
$$

而非 persistent learning。

---

# 80. Strong Learning Criterion

較強版本：

$$
\boxed{
StateChange
\land
Retention
\land
Reusability
\land
Transfer
\land
CausalSupport.
}
$$

---

# 81. Bottom-Space Update Protocol

$$
\boxed{
\mathcal B_t
\rightarrow
\mathcal B_{t+1}
}
$$

必須記錄：

1. trigger；
2. added reachable region；
3. removed region；
4. new tools；
5. new operator access；
6. changed protocol；
7. changed mutual models；
8. evidence；
9. distortion risk。

---

# 82. Coupling Gain

定義：

$$
\boxed{
G_C(
H,A
)
=
Performance(
H\otimes A
)
-
Baseline(
H,A
).
}
$$

Baseline 可以是：

$$
\max(
Performance(H),
Performance(A)
)
$$

或其他明確基準。

---

# 83. Coupling Gain 不等於 Intelligence Gain

$$
\boxed{
CouplingGain
\neq
GeneralIntelligenceGain.
}
$$

它只表示 joint system 在指定任務上的增益。

---

# 84. Negative Coupling

可能：

$$
\boxed{
G_C<0.
}
$$

例如：

- overtrust；
- communication overhead；
- false consensus；
- tool friction；
- memory contamination。

---

# 85. Coupling Stability

定義：

$$
\boxed{
Stability_C
}
$$

衡量 joint protocol 在時間、問題與模型切換下是否保持效果。

---

# 86. Protocol Portability

若：

$$
\Pi(H,A_1)
$$

換成：

$$
A_2
$$

仍有效：

$$
\boxed{
Portability(\Pi)
}
$$

較高。

---

# 87. AI Replacement Test

同一 human / corpus / protocol：

$$
(H,A_1,\Pi)
$$

與：

$$
(H,A_2,\Pi)
$$

比較：

$$
\Delta\mathcal B,
\Delta\mathfrak O,
\Delta Performance.
$$

可辨認 AI-specific coupling effects。

---

# 88. Human Replacement Test

同一 AI：

$$
(H_1,A,\Pi)
$$

與：

$$
(H_2,A,\Pi)
$$

比較，可測 human-conditioned bottom-space effects。

---

# 89. Protocol Replacement Test

固定：

$$
H,A,
$$

只改：

$$
\Pi_1\rightarrow\Pi_2.
$$

可測 protocol contribution。

---

# 90. Memory Ablation Test

移除：

$$
M_t
$$

重新執行。

若 performance / route 大幅改變，證明 persistent memory 是 joint system 的實質狀態。

---

# 91. Operator Ablation Test

移除：

$$
\Omega_k
$$

比較 runtime。

可判斷 operator learning 是否真正被調用。

---

# 92. Bottom-Space Drift

定義：

$$
\boxed{
\Delta_B(t)
=
d(
\mathcal B_t,
\mathcal B_{t+1}
).
}
$$

此 distance 不必一開始固定為單一 metric。

可拆：

$$
\Delta_B
=
(
\Delta Reach,
\Delta Structure,
\Delta Evidence,
\Delta Tools,
\Delta License
).
$$

---

# 93. Drift 不等於 Progress

$$
\boxed{
\Delta_B>0
\not\Rightarrow
Progress.
}
$$

可能只是 context 被污染。

---

# 94. Shared Bottom-Space Stabilization

若：

$$
\Delta_B
$$

在 window $W$ 中下降，且核心 reachability / protocol / evidence graph 穩定，可定義：

$$
\boxed{
Stab(
\mathcal B;W
).
}
$$

仍不是 finality。

---

# 95. Bottom-Space Reopening

新：

- AI；
- tool；
- corpus；
- human goal；
- protocol；
- observer；

可：

$$
\boxed{
StableBottomSpace
\rightarrow
ReopenedBottomSpace.
}
$$

---

# 96. Learning Debt

若 system 不斷吸收外部 state：

$$
M,R,T,\mathfrak O\uparrow
$$

但不 consolidation / invalidation，形成：

$$
\boxed{
LearningDebt.
}
$$

---

# 97. Memory Debt

過多：

- stale；
- duplicate；
- contradictory；
- source-less memory；

形成：

$$
\boxed{
MemoryDebt.
}
$$

---

# 98. Retrieval Debt

index / source weights 長期未 recalibrate：

$$
\boxed{
RetrievalDebt.
}
$$

---

# 99. Protocol Debt

protocol 只追加例外規則：

$$
\Pi_{t+1}
=
\Pi_t+\text{exceptions},
$$

卻不重構，形成：

$$
\boxed{
ProtocolDebt.
}
$$

---

# 100. Operator Debt

大量 provisional operators 未驗證／去重：

$$
\boxed{
OperatorDebt.
}
$$

---

# 101. Learning Health

定義 joint learning health：

$$
\boxed{
H_L
=
f(
Retention,
Reuse,
Transfer,
Debt,
ErrorVisibility,
Validation
).
}
$$

只作 diagnostic，不作 universal intelligence score。

---

# 102. External Learning and UBE

External operator / memory / protocol library 可：

$$
\boxed{
\mathcal X_{ext}^{[n]}
\Rightarrow_E
\mathcal X_{ext}^{[n+1]}.
}
$$

每一 actual state 有限，但無預設最終外部認知庫。

---

# 103. Bottom Space and UBE

同樣：

$$
\boxed{
\mathcal B^{[n]}
\Rightarrow_E
\mathcal B^{[n+1]}.
}
$$

不是建立已完成的：

$$
\mathcal B^{(\infty)}.
$$

---

# 104. Learning 不必單調

可能：

$$
\boxed{
Learn
\rightarrow
Unlearn
\rightarrow
Relearn.
}
$$

Invalidation / rollback 也是健康學習系統的一部分。

---

# 105. Forgetting

GCORF 區分：

$$
\boxed{
Forgetting
}
$$

與：

$$
\boxed{
Deletion.
}
$$

Forgetting 可是：

- priority decay；
- retrieval suppression；
- archive；
- context removal。

不一定物理刪除資料。

---

# 106. Strategic Forgetting

若 outdated / harmful memory 會污染 runtime，則：

$$
\boxed{
StrategicForgetting
}
$$

可能提高系統品質。

因此：

$$
MoreMemory
\neq
BetterMemory.
$$

---

# 107. Internal–External Recompilation

最一般形式：

$$
\boxed{
\mathcal J_{t+1}
=
Recompile(
\mathcal J_t,
Observation_t,
Feedback_t,
Evidence_t
).
}
$$

可能只修改外部層，也可能未來修改 $\theta$。

---

# 108. Knowledge Recompilation

不是只有 append：

$$
K_{t+1}
=
K_t+\Delta K.
$$

更一般：

$$
\boxed{
K_{t+1}
=
Recompile(
K_t,
O_t,
R_{t+1},
P_{t+1}
).
}
$$

其中舊 knowledge 可以：

- downgrade；
- reinterpret；
- merge；
- split；
- invalidate。

---

# 109. Learning as Topology Change

有些 learning event 不增加資訊量，但改變關係：

$$
\boxed{
E_t=E_{t+1}
}
$$

但：

$$
Graph_t
\neq
Graph_{t+1}.
$$

因此：

$$
\boxed{
Learning
\neq
InformationAccumulationOnly.
}
$$

---

# 110. Learning as Routing Change

同一 operator library：

$$
\mathfrak O
$$

若：

$$
\Pi_t\neq\Pi_{t+1},
$$

就可能出現巨大能力差異。

因此 routing 本身是認知資產。

---

# 111. Learning as Boundary Change

新 evidence 可能只修改：

$$
B_D,
\Lambda.
$$

沒有新增任何知識內容。

但這仍是：

$$
\boxed{
EpistemicLearning.
}
$$

因為 system 學會「哪裡不能用」。

---

# 112. Negative Knowledge

知道：

$$
\boxed{
\text{某路徑失敗}
}
$$

也是 learning。

因此 failure archive 是外部學習系統的重要部分。

---

# 113. Learning and Observer Diversity

若只有單一 observer 認為有 learning effect：

$$
o_1,
$$

其他 observer 重放無法重現，則 learning confidence 應下降。

---

# 114. Cross-Observer Learning Validation

定義：

$$
\boxed{
ValidateLearning(
\ell
\mid
o_1,\ldots,o_n
).
}
$$

保存 disagreement，不強迫 consensus。

---

# 115. GCORF-05 核心公理候選

### LEARN-A1 — Layer Separation

不同 learning layer 必須顯式區分。

### LEARN-A2 — Parameter Non-Exclusivity

$$
Learning
\not\equiv
ParameterUpdate.
$$

### LEARN-A3 — State-Change Non-Sufficiency

$$
StateChange
\not\Rightarrow
Learning.
$$

### LEARN-A4 — Behavioral Effect

learning event 必須對未來行為具有可辨識影響。

### LEARN-A5 — Reusability

正式 learning 至少要求可重用性。

### LEARN-A6 — Provenance

learning event 必須可追到 source / update / state delta。

### LEARN-A7 — Bottom-Space Conditionality

shared bottom space 受到 human / AI / protocol / tool / history 共同條件化。

### LEARN-A8 — Joint Non-Identity

高度耦合不推出 human–AI metaphysical identity。

### LEARN-A9 — External Revisability

外部 learning state 必須可 invalidation / rollback / archive。

### LEARN-A10 — Non-Final Learning Space

不存在預設完成的最終 external cognition state。

---

# 116. 十四個主要失效模式

1. **False Learning**：表現改善但沒有可保留結構改變；
2. **Evaluation Leakage**：答案洩漏被誤認學習；
3. **Context Contamination**：錯誤上下文導致暫態偏差；
4. **Memory Hallucination**：無真實來源的記憶被持久化；
5. **Stale Memory**：舊真實狀態被錯當目前真實；
6. **Retrieval Lock-In**：檢索只強化既有來源；
7. **Protocol Overfitting**：單任務 protocol 被錯誤泛化；
8. **Coupling Misalignment**：human / AI mutual model 錯配；
9. **Learning Attribution Error**：多層同時變動卻誤歸因；
10. **Bottom-Space Inflation**：資料增加被誤叫 reachable-space 增長；
11. **Memory Debt**：大量矛盾、重複、過期記憶；
12. **Operator Debt**：provisional operator 未整理；
13. **Persistence Confusion**：session adaptation 被誤稱長期學習；
14. **External-State Denial**：因權重沒變而否認可重用 external learning。

---

# 117. GCORF-05 核心 Runtime

定義：

$$
\boxed{
\operatorname{LearnEvent}
:
(
\mathcal J_t,
\Delta_t,
Task_t
)
\mapsto
(
\mathcal J_{t+1},
Layer,
BESAStatus,
LearningStatus,
Evidence
).
}
$$

---

# 118. Bottom-Space Runtime

$$
\boxed{
\operatorname{UpdateBottomSpace}
:
(
\mathcal B_t,
\Delta H,
\Delta A,
\Delta\Pi,
\Delta E,
\Delta K,
\Delta T
)
\mapsto
\mathcal B_{t+1}.
}
$$

---

# 119. Attribution Runtime

$$
\boxed{
\operatorname{AttributeLearning}
:
(
\mathcal J_{t+1},
\{\Delta_i\}
)
\mapsto
\{
Credit_i,
Uncertainty_i
\}.
}
$$

---

# 120. 與 GCORF-06 的接口

GCORF-05 已經建立：

$$
\boxed{
H,
A,
\mathcal B,
\Pi,
\mathcal H
}
$$

共同演化的 joint system。

下一個問題自然變成：

> 誰在觀察這整個 joint system？觀察者能否觀察自己、觀察自己的觀察規則、再把新的觀察層有限地加入系統？

因此 GCORF-06 將正式處理：

$$
\boxed{
\text{無界展開遞歸觀察者}
}
$$

以及：

$$
\boxed{
\text{observer stack}
+
\text{meta-observation}
+
\text{recursive legality}
+
\text{finite-prefix self-observation}.
}
$$

---

# 121. 結論

GCORF-05 將「學習」從單一參數更新問題，重新拆成多層可追蹤狀態轉換。

最核心分類為：

$$
\boxed{
Learning
=
\{
Parameter,
Context,
Memory,
Retrieval,
Tool,
Operator,
Protocol,
BottomSpace
\}.
}
$$

但本文同時拒絕把任何 update 都叫 learning。

正式 learning 至少必須回答：

$$
\boxed{
\text{改了什麼？}
}
$$

$$
\boxed{
\text{改在哪一層？}
}
$$

$$
\boxed{
\text{能保留多久？}
}
$$

$$
\boxed{
\text{能否重新使用？}
}
$$

$$
\boxed{
\text{能否轉移？}
}
$$

$$
\boxed{
\text{真的改變了後續行為嗎？}
}
$$

因此：

$$
\boxed{
\theta_{t+1}=\theta_t
}
$$

不能單獨證明：

$$
\boxed{
\text{No Learning}.
}
$$

更完整的問題應是：

$$
\boxed{
\mathcal J_{t+1}
\stackrel{?}{\neq}
\mathcal J_t
}
$$

以及這個差異是否具有：

$$
\boxed{
Retention
+
Reuse
+
BehavioralEffect
+
Evidence.
}
$$

最終，GCORF 將人–AI共同研究理解為：

$$
\boxed{
\begin{aligned}
&
(
H_t,
A_t,
\mathcal B_t,
\Pi_t,
\mathcal H_t
)
\\
&\qquad\longrightarrow
(
H_{t+1},
A_{t+1},
\mathcal B_{t+1},
\Pi_{t+1},
\mathcal H_{t+1}
),
\end{aligned}
}
$$

而不是單向：

$$
HumanPrompt
\rightarrow
AIAnswer.
$$

GCORF 因此開始進入真正的共同認知計算論：**學習不只可能發生在模型內，也可能發生在模型之外、工具之間、記憶之中、方法庫之中、協議之中，以及人與 AI 共同形成的可達認知空間本身。**
