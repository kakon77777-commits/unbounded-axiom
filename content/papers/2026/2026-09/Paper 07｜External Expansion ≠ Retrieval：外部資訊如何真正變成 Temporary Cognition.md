# Paper 07｜External Expansion ≠ Retrieval：外部資訊如何真正變成 Temporary Cognition

**English Title:** *External Expansion Is Not Retrieval: From Retrieved Information to Temporary Cognition*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／RAG、Context Compilation、Temporary Cognition 與外部知識展開研究

---

## 摘要

本文提出 **External Expansion ≠ Retrieval（外部展開不等於檢索）** 命題。前六篇已建立：Cognitive Density、Resident Cognitive Core、MoE Conditional Intelligence、Externalized Mixture of Cognitive Experts 與 Cognitive Factorization Problem。當能力與知識開始被外部化後，一個關鍵問題出現：

> **Mother AI 從外部世界「找到資料」之後，這些資料如何變成當下真正可被推理、驗證、比較、調度與重新收斂的認知狀態？**

傳統 Retrieval-Augmented Generation 可粗寫為：

$$
q
\rightarrow
\operatorname{Retrieve}(q)
\rightarrow
D_q
\rightarrow
\operatorname{Generate}(q,D_q).
$$

這個結構已經大幅改善模型取得最新資訊、長尾知識與可引用資料的能力。然而本文主張：

$$
\boxed{
\operatorname{Retrieve}
\neq
\operatorname{Understand}
\neq
\operatorname{Integrate}
\neq
\operatorname{Reason}.
}
$$

檢索結果：

$$
D_q
$$

只是 **evidence material**，不是完整 cognition。

Self-RAG 已顯示固定、不加判斷地檢索 passages 可能降低模型效用，因此 retrieval 本身需要按需決策與 self-reflection。Adaptive-RAG 又指出不同問題複雜度適合不同 retrieval / iterative reasoning 策略。RAPTOR 透過階層式摘要與 tree-organized retrieval 處理單純 chunk retrieval 缺少長文件全局理解的問題；GraphRAG 則把 unstructured text 轉成 graph、community hierarchy 與 summaries。Lost in the Middle 顯示「資訊已經存在 context」也不等於模型可以可靠使用它，尤其當關鍵資訊位於長 context 中間。2025 的 Retrieval is Not Enough 工作進一步提出 **Reasoning Misalignment**：模型內部推理軌跡可能偏離 retrieved evidence 的約束。2026 的 Structured Memory Scheduling RAG 更直接指出，複雜推理需要的不只是 retrieval relevance，而是 external knowledge 的組織、啟動時機、順序與 dependency scheduling。

因此本文把外部展開形式化為：

$$
\boxed{
Z_T
=
\Gamma_T
(
K_R,
S_t,
T,
D_T,
X_T
)
}
$$

其中：

- $K_R$：Resident Cognitive Core；
- $S_t$：當前持續狀態；
- $T$：任務；
- $D_T$：retrieved evidence；
- $X_T$：external experts / tools；
- $\Gamma_T$：Task-Conditioned Cognitive Compiler；
- $Z_T$：Temporary Cognition。

本文提出 **Cognitive Compilation（認知編譯）** 的九個公開階段：

$$
\boxed{
\Gamma_T
=
(
S,
N,
Y,
G,
C,
R,
P,
A,
V
)
}
$$

其中：

- $S$：Select，選擇；
- $N$：Normalize，正規化；
- $Y$：Type，賦予 epistemic / semantic type；
- $G$：Ground，建立來源與 provenance；
- $C$：Connect，建立關係與依賴；
- $R$：Resolve，標記衝突與未知；
- $P$：Project，投影成任務需要的表示；
- $A$：Activate / Schedule，安排何時使用；
- $V$：Verify，建立可驗證狀態。

Temporary Cognition 因此不是一個「更長的 prompt」，而是一個 task-relative、evidence-bearing、versioned、partially structured、可激活與可撤銷的認知工作狀態：

$$
\boxed{
Z_T
=
(
F_T,
R_T,
E_T,
U_T,
C_T,
P_T,
A_T,
V_T
)
}
$$

其中：

- $F_T$：facts / propositions；
- $R_T$：relations / dependencies；
- $E_T$：evidence / provenance；
- $U_T$：unknowns；
- $C_T$：conflicts / contested claims；
- $P_T$：task projection；
- $A_T$：activation schedule；
- $V_T$：verification state。

本文特別提出：

$$
\boxed{
\text{Context Length}
\neq
\text{Context Utility}
}
$$

以及：

$$
\boxed{
\text{Retrieved Relevance}
\neq
\text{Reasoning Relevance}.
}
$$

一個 chunk 與 query 語義相近，不代表它在當前推理步驟中應立即被激活；一項 evidence 可能只在某個後續 subgoal 出現後才有價值。這使外部知識從 passive context 轉成 **scheduled cognitive resource**。

本文提出十七項主要命題、十四類失敗模式與十二組可否證實驗。若未來實驗顯示：對大多數複雜任務，單純 top- $k$ retrieval + long context 與結構化 cognitive compilation 的效果沒有穩定差異；structured evidence state、dependency scheduling、conflict typing 與 context projection 無法提升 verified reasoning；或 compilation cost 長期大於其收益，則本文命題應被削弱。

本文的核心主張是：

$$
\boxed{
\text{Information becomes cognition only after it is made operational relative to a task.}
}
$$

亦即：

> **外部資料只有在被選擇、結構化、賦予證據狀態、建立依賴、投影到當前問題並進入正確推理時機後，才真正成為 Mother AI 當下的可用認知。**

**關鍵詞：** External Expansion、Temporary Cognition、Cognitive Compilation、RAG、Structured Memory、Context Engineering、Evidence State、GraphRAG、Self-RAG、Adaptive-RAG、Mother AI

---

# 0. 研究定位

Paper 06 提出：

$$
\boxed{
\mathfrak F
=
(
D,C,X,L,R,G
).
}
$$

其中：

- $X$：Expand / Externalize；
- $L$：Link；
- $R$：Reconcile；
- $G$：Converge。

Paper 07 專門研究：

$$
\boxed{
X+L.
}
$$

也就是：

> 外部資訊被找到之後，究竟怎麼「接回」核心？

---

# 1. Retrieval 解決的是 Access Problem

假設外部知識庫：

$$
\mathcal K.
$$

Query：

$$
q.
$$

Retriever：

$$
\boxed{
R(q,\mathcal K)
\rightarrow
D_q.
}
$$

它主要解：

$$
\boxed{
\text{Which information should be made available?}
}
$$

這非常重要。

但不是全部。

---

# 2. Cognition 解決的是 Use Problem

即使：

$$
D_q
$$

完全包含正確答案所需資訊，

模型仍可能：

- 忽略；
- 混淆；
- 錯誤排序；
- 誤用；
- 與舊 belief 衝突；
- 推理跳步。

因此還有：

$$
\boxed{
\text{How should available information participate in reasoning?}
}
$$

---

# 3. Retrieval 與 Cognition 的第一個分界

$$
\boxed{
\text{Availability}
\neq
\text{Activation}.
}
$$

資料存在：

$$
D_q
$$

不代表它已經進入有效工作狀態。

---

# 4. 第二個分界：Relevance 不是 Utility

Retriever 通常最大化：

$$
\operatorname{Sim}(q,d).
$$

但推理需要：

$$
\operatorname{Utility}(d\mid T,s_t).
$$

因此：

$$
\boxed{
\text{Semantic Relevance}
\neq
\text{Reasoning Utility}.
}
$$

---

# 5. 某資料可能現在不重要、之後重要

對 reasoning state：

$$
s_t,
$$

document：

$$
d
$$

的效用可以是：

$$
U(d,t).
$$

可能：

$$
U(d,t_1)\approx0,
$$

但：

$$
U(d,t_2)\gg0.
$$

因此知識使用需要：

$$
\boxed{
\text{temporal / procedural scheduling}.
}
$$

---

# 6. Self-RAG 的重要意義

Self-RAG 已經指出：

$$
\boxed{
\text{retrieve everything}
}
$$

不是最佳策略。

模型需要判斷：

- 是否需要 retrieval；
- retrieved passage 是否 relevant；
- generation 是否 supported；
- 是否需要 critique。

因此：

$$
\boxed{
\text{Retrieval Decision}
}
$$

本身已經是一種 meta-cognitive operation。

---

# 7. Adaptive-RAG 的重要意義

Adaptive-RAG 將問題依 complexity 選擇：

- no retrieval；
- single-step retrieval；
- iterative retrieval。

這表示：

$$
\boxed{
\text{Retrieval Topology}
}
$$

應依任務改變。

而不是：

$$
\boxed{
\text{one fixed RAG pipeline}.
}
$$

---

# 8. RAPTOR 的重要意義

普通 chunk retrieval：

$$
D
=
\{
d_1,d_2,\ldots
\}
$$

容易失去：

- whole-document abstraction；
- multi-scale structure；
- distant relation。

RAPTOR 建立：

$$
\boxed{
\text{recursive summaries}
+
\text{tree hierarchy}.
}
$$

這表示：

$$
\boxed{
\text{retrieval representation}
}
$$

本身需要被設計。

---

# 9. GraphRAG 的重要意義

GraphRAG 不是只把文章切 chunk。

它建立：

- entities；
- relations；
- communities；
- hierarchical summaries。

因此：

$$
\boxed{
\text{external knowledge}
}
$$

可以先被轉成：

$$
\boxed{
\text{structured relational substrate}.
}
$$

---

# 10. Long Context 不等於 Cognition

Lost in the Middle 顯示：

$$
\boxed{
\text{information in context}
\not\Rightarrow
\text{information reliably used}.
}
$$

關鍵資料的位置本身就可能影響模型表現。

因此：

$$
\boxed{
\text{Context Window Size}
\neq
\text{Effective Cognitive Workspace}.
}
$$

---

# 11. Context Pollution

若：

$$
C
=
D_1\cup\cdots\cup D_n
$$

直接塞入所有 retrieved chunks，

會增加：

- noise；
- redundancy；
- contradiction；
- attention competition；
- token cost。

因此：

$$
\boxed{
\text{More Context}
\not\Rightarrow
\text{More Cognition}.
}
$$

---

# 12. Prompt Compression 提供另一個證據

LLMLingua / LongLLMLingua 類工作顯示：

$$
\boxed{
\text{selective compression}
}
$$

可以降低 token 成本，

並在一些 long-context 任務改善有效資訊利用。

這支持：

$$
\boxed{
\text{information density matters}.
}
$$

---

# 13. 但 Compression 仍不等於 Compilation

Prompt compression 主要回答：

> 哪些 token 可以刪掉？

Cognitive Compilation 還要回答：

- 哪個 claim 是 evidence？
- 哪個是 counterexample？
- 哪個是 assumption？
- 哪個已過時？
- 哪些互相衝突？
- 哪些應先使用？

因此：

$$
\boxed{
\text{Compression}
\neq
\text{Cognitive Compilation}.
}
$$

---

# 14. Retrieval Is Not Enough：Reasoning Misalignment

2025 的工作提出：

$$
\boxed{
\text{Reasoning Misalignment}
}
$$

即：

$$
\text{retrieved evidence}
$$

與：

$$
\text{model reasoning trajectory}
$$

不一致。

這是一個非常核心的現象。

---

# 15. Evidence Present 仍可 Unsupported Conclusion

即使所有證據都在 context，

模型可能：

$$
E
\rightarrow
R_{\mathrm{wrong}}
\rightarrow
O.
$$

因此：

$$
\boxed{
\text{Grounded Input}
\neq
\text{Grounded Reasoning}.
}
$$

---

# 16. SMS-RAG 的重要意義

2026 的 Structured Memory Scheduling RAG 明確提出：

> external knowledge 不能只是 flat context。

需要決定：

- 啟動哪些 memory；
- 什麼順序；
- dependency 如何；
- reasoning stage 如何對齊。

這非常接近本文的：

$$
\boxed{
\text{Cognitive Compilation}.
}
$$

---

# 17. External Expansion 的正式定義

本文定義：

$$
\boxed{
\mathsf{Expand}
:
(
K_R,
S_t,
T,
\mathcal K,
\mathcal X
)
\rightarrow
Z_T.
}
$$

其中：

$$
Z_T
$$

不是 raw documents。

它是：

$$
\boxed{
\text{Temporary Cognition}.
}
$$

---

# 18. Temporary Cognition

定義：

$$
\boxed{
Z_T
=
(
F_T,
R_T,
E_T,
U_T,
C_T,
P_T,
A_T,
V_T
).
}
$$

---

# 19. Facts / Propositions

$$
F_T
$$

保存 task-relevant propositions。

不是所有 retrieved sentence。

---

# 20. Relations

$$
R_T
$$

保存：

- causal；
- temporal；
- dependency；
- contradiction；
- equivalence；
- support。

---

# 21. Evidence

$$
E_T
$$

綁定：

- source；
- version；
- timestamp；
- retrieval path；
- confidence；
- evidence strength。

---

# 22. Unknowns

$$
U_T
$$

保存：

$$
\boxed{
\text{not yet resolved}.
}
$$

Unknown 不應被空白文字吞掉。

---

# 23. Contested Claims

$$
C_T
$$

保存：

$$
\boxed{
p
\quad\text{vs}\quad
\neg p
}
$$

的 conflict state。

---

# 24. Task Projection

$$
P_T
$$

只保留當前問題需要的：

- variables；
- constraints；
- goals；
- subgoals。

---

# 25. Activation Schedule

$$
A_T
$$

決定：

> 哪些資訊現在 active？

> 哪些暫存？

> 哪些等後續 subgoal 再啟動？

---

# 26. Verification State

$$
V_T
$$

保存：

- unverified；
- source-supported；
- cross-checked；
- mechanically verified；
- rejected。

---

# 27. Temporary Cognition 不是 Long-Term Memory

$$
\boxed{
Z_T
\neq
M_{\mathrm{long}}.
}
$$

它只存在於：

$$
\text{task lifetime}.
$$

---

# 28. Temporary Cognition 也不是 Prompt

Prompt 是：

$$
\text{serialization}.
$$

Temporary Cognition 是：

$$
\boxed{
\text{structured cognitive state}.
}
$$

Prompt 只是它的一種投影。

---

# 29. Cognitive Compiler

本文定義：

$$
\boxed{
\Gamma_T
:
(
K_R,
S_t,
T,
D_T,
X_T
)
\rightarrow
Z_T.
}
$$

這是：

$$
\boxed{
\text{Task-Conditioned Cognitive Compiler}.
}
$$

---

# 30. 九個公開編譯階段

$$
\boxed{
\Gamma_T
=
(
S,N,Y,G,C,R,P,A,V
).
}
$$

---

# 31. $S$：Select

從：

$$
D_T
$$

中選：

$$
D_T^\ast.
$$

目標不是 similarity 最高，

而是：

$$
\boxed{
\text{task utility}.
}
$$

---

# 32. Selection 必須允許「不要」

如果：

$$
d
$$

不必要，

則：

$$
\boxed{
d\rightarrow\varnothing.
}
$$

不是所有 retrieve 結果都必須進 cognition。

---

# 33. $N$：Normalize

不同 source 可能有：

- HTML；
- PDF；
- API；
- table；
- graph；
- prose。

Normalize：

$$
\boxed{
d_i
\rightarrow
n_i.
}
$$

建立一致基本 representation。

---

# 34. Normalization 不是抹平語義

結構化 table 不應被完全轉成失去 schema 的 prose。

因此 normalize 要保留：

$$
\boxed{
\text{semantic type}.
}
$$

---

# 35. $Y$：Type

給資訊賦予 epistemic / semantic type：

$$
\boxed{
Y(d)
\in
\{
\text{fact},
\text{claim},
\text{hypothesis},
\text{rule},
\text{example},
\text{counterexample},
\text{procedure},
\text{measurement}
\}.
}
$$

---

# 36. Type 很重要

因為：

$$
\boxed{
\text{example}
\neq
\text{rule}.
}
$$

如果模型把案例當普遍規則，

推理就會偏移。

---

# 37. $G$：Ground

建立：

$$
\boxed{
\text{claim}
\rightarrow
\text{source}.
}
$$

Grounding 不是只有 citation。

還包括：

- source identity；
- authority；
- version；
- timestamp；
- scope。

---

# 38. Source Scope

一篇文件可能只支持：

$$
p
$$

在：

$$
C
$$

條件下成立。

因此：

$$
\boxed{
\text{source support}
}
$$

必須綁：

$$
\boxed{
\text{scope}.
}
$$

---

# 39. $C$：Connect

建立：

$$
\boxed{
G_T
=
(
V_T,
E_T
).
}
$$

節點是 claims / concepts，

邊是：

- support；
- contradict；
- cause；
- depend；
- precede；
- derive。

---

# 40. 為什麼 Relation 必須顯式？

兩個 facts：

$$
a,
b
$$

若不知道：

$$
a\rightarrow b,
$$

模型仍要自己從 flat text 重建。

這會增加：

$$
\boxed{
\text{implicit reconstruction burden}.
}
$$

---

# 41. $R$：Resolve

Resolve 不代表強制解決所有 conflict。

更重要的是：

$$
\boxed{
\text{represent disagreement explicitly}.
}
$$

---

# 42. Conflict State

$$
\boxed{
C(p)
=
\{
(s_1,p),
(s_2,\neg p)
\}.
}
$$

系統可以保留：

$$
\boxed{
\text{contested}.
}
$$

---

# 43. Unknown State

如果 evidence 不足：

$$
\boxed{
p=\text{UNKNOWN}.
}
$$

不是：

$$
p=\text{FALSE}.
$$

---

# 44. $P$：Project

從完整 task graph：

$$
G_T
$$

投影當下 reasoning state：

$$
\boxed{
P_t
=
\operatorname{Project}(G_T,s_t).
}
$$

---

# 45. Projection 降低 Active Context

所有資料可以存在：

$$
Z_T,
$$

但當前只激活：

$$
P_t.
$$

因此：

$$
\boxed{
\text{Stored Temporary Cognition}
\neq
\text{Active Context}.
}
$$

---

# 46. $A$：Activate / Schedule

對 reasoning steps：

$$
t=1,\ldots,n,
$$

決定：

$$
\boxed{
A(t)
\subseteq Z_T.
}
$$

---

# 47. Knowledge Scheduling

某 evidence：

$$
e_i
$$

只有在 subgoal：

$$
g_j
$$

出現時才啟動。

因此：

$$
\boxed{
e_i
\rightarrow
g_j.
}
$$

---

# 48. Scheduled Knowledge 與 MoE 類比

Internal MoE：

$$
\text{token}
\rightarrow
\text{expert}.
$$

Temporary Cognition：

$$
\text{reasoning state}
\rightarrow
\text{evidence subset}.
$$

二者都有：

$$
\boxed{
\text{conditional activation}.
}
$$

---

# 49. $V$：Verify

編譯後：

$$
Z_T
$$

不是自動 trusted。

Verification：

$$
\boxed{
V:
Z_T
\rightarrow
Z_T^{verified}.
}
$$

---

# 50. Verification 可能是局部的

不是所有 node 都需要最高級 verifier。

例如：

$$
V(v_i)
$$

依：

- risk；
- impact；
- uncertainty；

分配。

---

# 51. Risk-Weighted Verification

定義：

$$
\boxed{
B_V(v)
=
f(
R_v,
U_v,
H_v
).
}
$$

高風險、低信心、高 downstream impact 的 node 得到更多 verification budget。

---

# 52. Cognitive Compilation 與 Compiler 類比

Source code：

$$
S
$$

不直接執行。

需要：

$$
\operatorname{Compile}(S)
\rightarrow
I.
$$

同樣：

$$
\boxed{
\text{Raw Knowledge}
\rightarrow
\text{Cognitive Intermediate Representation}.
}
$$

---

# 53. Cognitive IR

本文提出：

$$
\boxed{
\mathrm{CIR}_T
=
(
V,
E,
Y,
P,
A,
Vf
).
}
$$

它不是公開標準，

而是研究抽象。

---

# 54. CIR 的價值

如果存在穩定 Cognitive IR，

不同 external sources 可以：

$$
\boxed{
\text{compile to one task-state interface}.
}
$$

---

# 55. 這能降低模型依賴

不同 Mother Model：

$$
M_1,M_2
$$

可以共享：

$$
\mathrm{CIR}_T
$$

的部分結構。

因此：

$$
\boxed{
\text{knowledge infrastructure}
}
$$

不必完全綁死某個 LLM。

---

# 56. 但 Cognitive IR 不能過度僵化

如果 schema 太固定，

遇到 novel task：

$$
T_{\mathrm{novel}}
$$

可能無法表示。

因此：

$$
\boxed{
\text{typed}
+
\text{extensible}.
}
$$

---

# 57. Multi-Representation Temporary Cognition

同一：

$$
Z_T
$$

可以有：

- graph；
- text；
- table；
- code；
- embedding；
- evidence ledger。

因此：

$$
\boxed{
\text{one cognition}
\neq
\text{one serialization}.
}
$$

---

# 58. Context Compiler

真正送給 LLM 的 context：

$$
C_t
$$

應由：

$$
\boxed{
C_t
=
\operatorname{Serialize}
(
\operatorname{Project}(Z_T,s_t)
).
}
$$

不是：

$$
C_t=D_T.
$$

---

# 59. Context Density

定義：

$$
\boxed{
D_C
=
\frac{
\text{task-useful evidence}
}{
\text{active context tokens}
}.
}
$$

這是局部 context density，

不是 Paper 02 的整體 Cognitive Density。

---

# 60. Position-Aware Compilation

Lost in the Middle 表示：

$$
\boxed{
\text{position matters}.
}
$$

因此 Serialize 不只是：

$$
\text{append chunks}.
$$

還要決定：

- order；
- repetition；
- salience；
- grouping。

---

# 61. Evidence Proximity

互相依賴的：

$$
e_i,e_j
$$

可以在 serialization 中保持：

$$
\boxed{
\text{logical proximity}.
}
$$

降低模型跨長距離重建負擔。

---

# 62. LongLLMLingua 的啟示

Prompt compression 可以：

- reduce context；
- preserve key information；
- improve latency。

這支持：

$$
\boxed{
\text{context should be compiled, not accumulated}.
}
$$

---

# 63. Query Decomposition

複雜任務：

$$
T
$$

可以拆：

$$
\boxed{
T
\rightarrow
\{
g_1,\ldots,g_n
\}.
}
$$

每個 subgoal：

$$
g_i
$$

有自己的 retrieval。

---

# 64. Retrieval Plan

$$
\boxed{
\Pi_R
=
(
q_1,\ldots,q_n
).
}
$$

因此：

$$
\boxed{
\text{one user query}
\neq
\text{one retrieval query}.
}
$$

---

# 65. Iterative Retrieval

reasoning：

$$
s_t
$$

產生新的：

$$
q_{t+1}.
$$

因此：

$$
\boxed{
q_{t+1}
=
f(
T,
s_t,
U_t
).
}
$$

---

# 66. Unknown Drives Retrieval

理想上：

$$
U_t
$$

Unknown set 直接生成：

$$
\boxed{
\text{next information need}.
}
$$

這比固定：

$$
\text{retrieve top 5}
$$

更接近 epistemic control。

---

# 67. Retrieval Stop Condition

當：

$$
\operatorname{ExpectedGain}(R_{t+1})
<
C_R,
$$

應停止。

因此：

$$
\boxed{
\text{retrieval has a budget}.
}
$$

---

# 68. Evidence Saturation

如果新增 documents：

$$
D_{n+1}
$$

不增加：

$$
Q_V,
$$

則：

$$
\boxed{
\text{retrieval saturated}.
}
$$

---

# 69. Retrieval Pollution

如果新增：

$$
D_{n+1}
$$

反而：

$$
Q_V\downarrow,
$$

則：

$$
\boxed{
\text{retrieval pollution}.
}
$$

---

# 70. Evidence Competition

兩個 evidence：

$$
e_1,e_2
$$

可能：

- 支持不同假設；
- scope 不同；
- version 不同。

因此不能只：

$$
\text{rank by similarity}.
$$

---

# 71. Evidence Hierarchy

可以建立：

$$
\boxed{
E_0<E_1<E_2<E_3<E_4.
}
$$

例如：

- assertion；
- secondary source；
- primary source；
- independent reproduction；
- mechanical proof。

---

# 72. 但 Evidence Hierarchy 是 Task-Relative

法律：

$$
E_{\mathrm{statute}}
$$

與物理：

$$
E_{\mathrm{experiment}}
$$

不可直接共用同一 hierarchy。

因此：

$$
\boxed{
V_T
}
$$

必須 role / domain-aware。

---

# 73. Freshness

外部資訊有：

$$
t_s.
$$

任務有：

$$
t_q.
$$

若：

$$
|t_q-t_s|
$$

太大，

freshness risk：

$$
R_F\uparrow.
$$

---

# 74. Version Semantics

Software API：

$$
v_1
$$

與：

$$
v_2
$$

不能混在同一 fact bucket。

因此：

$$
\boxed{
\text{claim}
+
\text{version}
}
$$

才是完整 evidence key。

---

# 75. Provenance 是 Cognition 的一部分

如果只保留：

$$
p,
$$

不保留：

$$
source(p),
$$

Mother AI 無法：

- recheck；
- retract；
- compare；
- update。

因此：

$$
\boxed{
\text{Provenance}
}
$$

不是 metadata decoration。

---

# 76. Provenance Enables Retraction

若 source：

$$
s
$$

被撤回：

$$
s\rightarrow\bot,
$$

可以找到：

$$
\boxed{
\{p_i:source(p_i)=s\}.
}
$$

進行 revalidation。

---

# 77. Conflict 是正常狀態

外部世界本來可能：

$$
s_1\models p,
$$

$$
s_2\models\neg p.
$$

因此：

$$
\boxed{
\text{conflict}
}
$$

不是 compiler failure。

它是一種合法 epistemic state。

---

# 78. Cognitive Compilation 不應強制單一答案

有時輸出應是：

$$
\boxed{
\text{unresolved conflict}.
}
$$

這比假裝 certainty 更正確。

---

# 79. Temporary Cognition 的生命週期

$$
\boxed{
\text{Construct}
\rightarrow
\text{Activate}
\rightarrow
\text{Update}
\rightarrow
\text{Verify}
\rightarrow
\text{Retire / Consolidate}.
}
$$

---

# 80. Retire

任務完成後：

$$
Z_T
$$

大部分應：

$$
\boxed{
\text{expire}.
}
$$

否則 core / memory 會無限膨脹。

---

# 81. Consolidate

只有：

- stable；
- reusable；
- high-evidence；

部分：

$$
\Delta Z_T
$$

才考慮：

$$
\boxed{
\text{consolidation}.
}
$$

---

# 82. Consolidation 不一定進 Model Weights

可能寫入：

- external memory；
- capability registry；
- causal graph；
- verifier library。

因此：

$$
\boxed{
\text{learning}
\neq
\text{weight update only}.
}
$$

---

# 83. Temporary Cognition 與 Working Memory

它近似：

$$
\boxed{
\text{task-conditioned working cognition}.
}
$$

但本文不直接等同人類 working memory。

這只是功能類比。

---

# 84. External Expansion 與 MoE 的跨尺度同構

Internal MoE：

$$
h_t
\rightarrow
E_i.
$$

External cognition：

$$
s_t
\rightarrow
A_t\subseteq Z_T.
$$

都在做：

$$
\boxed{
\text{conditional activation of available resources}.
}
$$

---

# 85. Cognitive Memory Scheduler

因此可以概念化：

$$
\boxed{
\pi_M(s_t)
\rightarrow
A_t.
}
$$

其中：

$$
A_t
$$

是 active evidence / memory set。

---

# 86. Scheduler 可以是 Deterministic + AI Hybrid

某些規則：

- version；
- authority；
- security；

適合 deterministic。

某些：

- semantic relevance；
- hypothesis usefulness；

適合 AI。

因此：

$$
\boxed{
\text{Memory Scheduler}
=
\text{Hybrid Control}.
}
$$

---

# 87. External Expert Outputs 也要進 Compiler

Paper 05 的：

$$
X_i
$$

返回：

$$
O_i.
$$

不能直接：

$$
O_i\rightarrow M.
$$

更合理：

$$
\boxed{
O_i
\rightarrow
\Gamma_T
\rightarrow
Z_T.
}
$$

---

# 88. 所以 External Knowledge 與 External Expert 同一化

對 Compiler 而言：

$$
\boxed{
\text{document}
}
$$

與：

$$
\boxed{
\text{expert result}
}
$$

都是：

$$
\boxed{
\text{external evidence-bearing input}.
}
$$

---

# 89. 但 Authority 不同

Document：

$$
A=0.
$$

Expert output：

$$
A
$$

也不應自動大於零。

只有 runtime policy 決定 authority。

---

# 90. Temporary Cognition 是 Mother AI 的 Task-Specific Expansion

Resident Core：

$$
K_R
$$

保持較穩定。

每個 task：

$$
T
$$

生成：

$$
Z_T.
$$

因此：

$$
\boxed{
\text{small stable core}
+
\text{large temporary expansion}.
}
$$

---

# 91. 這正好避免所有知識常駐

如果：

$$
Z_T
$$

可以可靠建構，

則：

$$
K_R
$$

不需要永遠保存：

- every paper；
- every API；
- every historical detail。

---

# 92. 但 Core 必須懂得編譯

如果：

$$
K_R
$$

不知道：

- what to retrieve；
- what to trust；
- how to connect；

則：

$$
\boxed{
\Gamma_T
}
$$

會崩潰。

所以 External Expansion 反而再次證明 Resident Cognitive Core 必須有內容。

---

# 93. Compiler 也可能外包一部分

例如：

- document parser；
- graph extractor；
- source classifier；

可以由 external tools 執行。

但 compiler governance：

$$
\boxed{
\text{what state is accepted}
}
$$

不能完全消失。

---

# 94. Cognitive Compilation Cost

定義：

$$
\boxed{
C_\Gamma
=
C_S+
C_N+
C_Y+
C_G+
C_C+
C_R+
C_P+
C_A+
C_V.
}
$$

如果：

$$
C_\Gamma
$$

太高，

則簡單 RAG 可能更好。

---

# 95. Compilation Gain

$$
\boxed{
G_\Gamma
=
Q_V(\Gamma)
-
Q_V(\text{naive RAG}).
}
$$

只有：

$$
G_\Gamma>\lambda C_\Gamma
$$

才值得。

---

# 96. Cognitive Compilation 不是所有任務都需要

簡單 fact lookup：

$$
T_{\mathrm{simple}}
$$

可能：

$$
\boxed{
\text{retrieve}
\rightarrow
\text{answer}
}
$$

足夠。

複雜 task 才需要完整：

$$
\Gamma_T.
$$

---

# 97. Adaptive Compilation

因此：

$$
\boxed{
\Gamma_T^{(k)}
}
$$

可以有不同層級：

- Level 0：no retrieval；
- Level 1：simple retrieval；
- Level 2：filtered retrieval；
- Level 3：structured compilation；
- Level 4：scheduled multi-source reasoning。

---

# 98. Complexity-Aware Expansion

$$
\boxed{
k^\ast
=
f(
\text{task complexity},
\text{risk},
\text{uncertainty},
\text{budget}
).
}
$$

這承接 Adaptive-RAG。

---

# 99. Compilation Depth

不是所有 evidence 都需要建完整 graph。

因此：

$$
\boxed{
d_\Gamma
}
$$

也是動態變數。

---

# 100. Reasoning State Alignment

定義：

$$
\boxed{
A_R
=
\operatorname{Align}
(
R_{\mathrm{reason}},
E_{\mathrm{active}}
).
}
$$

衡量 reasoning steps 是否受當前 evidence constraints 支持。

---

# 101. Evidence-Constrained Reasoning

理想：

$$
r_i
$$

每一步都能指出：

$$
\boxed{
\operatorname{Support}(r_i).
}
$$

不是要求所有自然語言 reasoning 都公開，

而是系統內可以做 provenance / justification check。

---

# 102. Reasoning Misalignment Test

給完整正確 evidence，

故意加入：

- distractor；
- outdated source；
- contradiction。

看模型是否：

$$
\boxed{
\text{follow evidence constraints}.
}
$$

---

# 103. Temporary Cognition Integrity

定義：

$$
\boxed{
I_Z
=
f(
\text{coverage},
\text{consistency},
\text{provenance},
\text{freshness},
\text{unknown preservation}
).
}
$$

---

# 104. Cognitive Expansion Efficiency

Paper 02 定義：

$$
\eta_E.
$$

現在可以細化：

$$
\boxed{
\eta_{\mathrm{expand}}
=
\frac{
Q_V(Z_T)-Q_V(K_R)
}{
C_R+C_\Gamma+C_X+C_V
}.
}
$$

---

# 105. Expansion 失敗模式 1：Retrieval Illusion

有資料就以為已解決問題。

---

# 106. 失敗模式 2：Similarity Trap

語義最相似的 chunk 不等於推理最重要。

---

# 107. 失敗模式 3：Context Flooding

大量資料全部塞入 context。

---

# 108. 失敗模式 4：Lost-in-the-Middle

正確 evidence 存在但未被有效使用。

---

# 109. 失敗模式 5：Evidence Flattening

graph / table / temporal structure 被抹平成 prose。

---

# 110. 失敗模式 6：Source Amnesia

claim 留下，provenance 遺失。

---

# 111. 失敗模式 7：Conflict Collapse

互相衝突 sources 被強制 merge 成單一 certainty。

---

# 112. 失敗模式 8：Unknown Erasure

missing evidence 被模型補成答案。

---

# 113. 失敗模式 9：Reasoning Misalignment

reasoning trajectory 偏離 evidence constraints。

---

# 114. 失敗模式 10：Over-Compilation

簡單任務也跑完整昂貴 compiler。

---

# 115. 失敗模式 11：Compiler Hallucination

Compiler 自己新增 source 中不存在的 relation。

---

# 116. 失敗模式 12：Stale Evidence

舊資料被當成 current。

---

# 117. 失敗模式 13：Premature Consolidation

temporary claims 太早寫入 long-term memory。

---

# 118. 失敗模式 14：Representation Lock-In

Cognitive IR 太僵化，無法表示 novel task。

---

# 119. 十七項主要命題

## 命題 1：Retrieval 非 Cognition 命題

$$
\boxed{
\text{Retrieval}
\neq
\text{Cognition}.
}
$$

## 命題 2：Availability 非 Activation 命題

資訊存在於 context 不代表已被有效使用。

## 命題 3：Semantic Relevance 非 Reasoning Utility 命題

retrieval similarity 與推理效用不可等同。

## 命題 4：Context Length 非 Context Utility 命題

更長 context 不保證更高任務效用。

## 命題 5：Structured Representation 命題

某些複雜任務需要 graph / hierarchy / typed evidence，而非 flat chunks。

## 命題 6：Temporary Cognition 命題

外部展開應形成 task-relative cognitive state：

$$
Z_T.
$$

## 命題 7：Cognitive Compilation 命題

$$
\boxed{
D_T
\rightarrow
Z_T
}
$$

需要獨立編譯步驟。

## 命題 8：Epistemic Typing 命題

fact、claim、hypothesis、example、counterexample 等不應被視為同一資料型別。

## 命題 9：Provenance Residency 命題

外部 evidence 在 temporary cognition 中應保留來源與版本。

## 命題 10：Conflict Preservation 命題

矛盾 evidence 可以合法共存於 contested state。

## 命題 11：Unknown Preservation 命題

缺失資訊應保持 Unknown，而不是自動 closure。

## 命題 12：Knowledge Scheduling 命題

外部知識的使用時機與順序會影響複雜推理效能。

## 命題 13：Adaptive Compilation 命題

不同任務只需要不同深度的 cognitive compilation。

## 命題 14：External Expert Compilation 命題

external model output 也需要經 $\Gamma_T$ 才能進入 accepted cognitive state。

## 命題 15：Temporary-State Retirement 命題

大部分 $Z_T$ 應在任務結束後 expire，而非永久寫回。

## 命題 16：Selective Consolidation 命題

只有高證據、高重用價值結構才應進 long-term substrate。

## 命題 17：Expansion Efficiency 命題

Cognitive Compilation 只有在 verified utility 增益高於 compilation tax 時才值得使用。

---

# 120. 十二組可否證實驗

## 實驗 1：Naive RAG vs Compiled Context

比較：

$$
\text{top-k chunks}
$$

與：

$$
\Gamma_T(D_T).
$$

測 verified accuracy。

## 實驗 2：Long Context vs Projection

同樣 evidence：

- full context；
- projected context。

比較 performance / token cost。

## 實驗 3：Position Robustness

改變 evidence 在 prompt 位置，

測 compiled serialization 是否降低 position bias。

## 實驗 4：Graph vs Flat

multi-hop task 比較 graph representation 與 flat chunks。

## 實驗 5：Conflict Preservation

加入互相矛盾 sources，

測系統是否保持 contested state。

## 實驗 6：Unknown Preservation

刻意缺少一個必要 fact，

測系統是否生成 Unknown。

## 實驗 7：Scheduling Ablation

固定相同 evidence，

只改 activation order。

測 reasoning quality。

## 實驗 8：Provenance Ablation

移除 source metadata，

測 conflict resolution / retraction 能力。

## 實驗 9：Adaptive Compilation

simple / medium / complex tasks 比較不同 $\Gamma$ level。

## 實驗 10：External Expert Integration

相同 external output：

- direct prompt insertion；
- compiled integration。

比較 acceptance quality。

## 實驗 11：Temporary Cognition Retirement

長期多任務測：

- retain everything；
- selective consolidate。

比較 memory pollution。

## 實驗 12：Compilation Cost Crossover

尋找：

$$
C_\Gamma
$$

何時開始高於：

$$
G_\Gamma.
$$

---

# 121. 什麼結果會支持本文？

以下結果會支持：

1. compiled context 在相同 evidence 下穩定優於 flat top- $k$ ；
2. structured relation 顯著改善 multi-hop reasoning；
3. projection 可以降低 token 但保持或提升 verified quality；
4. conflict / unknown typing 降低 unsupported conclusions；
5. provenance 可以改善 retraction / update；
6. scheduling order 對 reasoning 有可重複影響；
7. adaptive compilation 優於 always-heavy pipeline；
8. external expert outputs 經 compilation 後 acceptance error 降低；
9. Temporary Cognition retirement 降低長期 memory pollution；
10. reasoning-evidence alignment 可被量測並改善；
11. context position sensitivity 因 compilation 降低；
12. external expansion 在部分任務提高 Cognitive Density。

---

# 122. 什麼結果會削弱本文？

以下結果會削弱：

1. modern long-context models 已使 context position / overload 問題完全消失；
2. flat top- $k$ 在複雜任務與 structured compilation 無穩定差異；
3. relation graph / typing 成本高但無效益；
4. activation scheduling 不影響 reasoning；
5. provenance 對實際品質幾乎無價值；
6. unknown / conflict state 無法改善錯誤率；
7. compilation hallucination 超過 naive RAG；
8. compilation latency 使系統不可部署；
9. external expert outputs 不需額外 integration；
10. Temporary Cognition 無法與一般 prompt/context 操作區分；
11. adaptive compilation classifier 錯誤抵消收益；
12. selective consolidation 造成過多有用資訊遺失。

---

# 123. 公開命題與未公開方法的邊界

本文公開：

- Temporary Cognition；
- Cognitive Compilation；
- 九階段 $\Gamma_T$ ；
- evidence typing；
- relation / provenance / conflict / unknown；
- activation scheduling；
- adaptive compilation；
- falsification tests。

本文不公開任何未驗證或未公開的：

- private context compiler algorithm；
- high-dimensional semantic projection；
- graph compilation heuristic；
- hidden-state bridge；
- evidence-weight learning；
- activation scheduling optimizer；
- internal memory compiler；
- reconvergence implementation。

因此：

$$
\boxed{
\text{Public Cognitive Compilation Theory}
\neq
\text{Private Compilation Method}.
}
$$

---

# 124. 與 Paper 08 的銜接

Paper 07 已經建立：

$$
\boxed{
\text{external information}
\rightarrow
Z_T.
}
$$

接下來需要回答：

> **誰決定何時建立 $Z_T$ 、何時調用 external expert、何時直接自己推理、何時需要 verifier，以及整個 temporary organization 怎麼形成？**

因此下一篇：

$$
\boxed{
\text{Mother AI as Cognitive Command Tower}.
}
$$

Paper 08 會把：

- Resident Core；
- Internal Experts；
- External Experts；
- Temporary Cognition；

正式放到同一個 coordination architecture。

---

# 125. 結論

Retrieval-Augmented Generation 已經證明：

$$
\boxed{
\text{external knowledge matters}.
}
$$

但「可以找到資訊」不是終點。

Self-RAG 顯示 retrieval 本身需要反思與按需控制；Adaptive-RAG 顯示 retrieval strategy 應隨問題複雜度調整；RAPTOR 與 GraphRAG 顯示外部資訊的 hierarchy / relation representation 會影響利用方式；Lost in the Middle 顯示資訊即使完整存在 context，也不一定被模型穩定使用；Retrieval is Not Enough 顯示 reasoning trajectory 可能偏離 evidence；SMS-RAG 則把 external memory 進一步提升為需要 scheduling 與 dependency organization 的 reasoning resource。

因此本文提出：

$$
\boxed{
\text{Retrieval}
\rightarrow
\text{Evidence Material}.
}
$$

而真正的 External Expansion 是：

$$
\boxed{
\text{Evidence Material}
\xrightarrow{\Gamma_T}
\text{Temporary Cognition}.
}
$$

也就是：

$$
\boxed{
Z_T
=
\Gamma_T
(
K_R,
S_t,
T,
D_T,
X_T
).
}
$$

Temporary Cognition 不只是更長的 context。

它包含：

$$
\boxed{
\text{facts}
+
\text{relations}
+
\text{evidence}
+
\text{unknowns}
+
\text{conflicts}
+
\text{task projection}
+
\text{activation schedule}
+
\text{verification state}.
}
$$

外部知識只有在完成：

$$
\boxed{
\text{Select}
\rightarrow
\text{Normalize}
\rightarrow
\text{Type}
\rightarrow
\text{Ground}
\rightarrow
\text{Connect}
\rightarrow
\text{Resolve}
\rightarrow
\text{Project}
\rightarrow
\text{Activate}
\rightarrow
\text{Verify}
}
$$

之後，才開始真正成為當下可操作 cognition。

因此本篇的最終命題是：

$$
\boxed{
\text{Knowledge should not merely be retrieved into context;}
}
$$

而應：

$$
\boxed{
\text{be compiled into cognition relative to the task}.
}
$$

如果這件事成立，

那麼 Mother AI 未來真正使用的並不是：

$$
\boxed{
\text{an infinitely long prompt}.
}
$$

而是：

$$
\boxed{
\text{a continuously compiled, task-relative cognitive workspace}.
}
$$

這就是 External Expansion 與 ordinary Retrieval 的根本差異。

---

# References

1. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020.
2. Liu, N. F., et al. (2024). *Lost in the Middle: How Language Models Use Long Contexts*. Transactions of the Association for Computational Linguistics, 12, 157–173.
3. Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2024). *Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection*. ICLR 2024.
4. Sarthi, P., et al. (2024). *RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval*. ICLR 2024.
5. Jeong, S., Baek, J., Cho, S., Hwang, S. J., & Park, J. C. (2024). *Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity*. NAACL 2024.
6. Jiang, H., et al. (2023). *LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models*. EMNLP 2023.
7. Jiang, H., et al. (2024). *LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression*. ACL 2024.
8. Edge, D., et al. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv:2404.16130.
9. Wei, J., et al. (2025). *Retrieval is Not Enough: Enhancing RAG Reasoning through Test-Time Critique and Optimization*. NeurIPS 2025.
10. Yao, X., Zhao, X., Zhou, D., et al. (2026). *Why Retrieval is not Enough: Structured Memory Scheduling for Large Language Model Reasoning*. Data Science and Engineering.
11. Neo.K. & Aletheia. (2026). *Cognitive Density Hypothesis：認知密度命題*.
12. Neo.K. & Aletheia. (2026). *Resident Cognitive Core：Mother Model 到底必須常駐什麼？*.
13. Neo.K. & Aletheia. (2026). *Externalized Mixture of Cognitive Experts：為什麼 Expert 一定要住在同一個模型裡？*.
14. Neo.K. & Aletheia. (2026). *Cognitive Factorization Problem：成熟智能能否被重新分離、壓縮與重組？*.
15. Neo.K. & Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開命題論文。

本文公開：

- External Expansion ≠ Retrieval；
- Temporary Cognition；
- Task-Conditioned Cognitive Compiler；
- nine-stage compilation abstraction；
- evidence / conflict / unknown / provenance；
- knowledge activation scheduling；
- adaptive compilation；
- public falsification tests。

本文不公開任何未驗證或未公開的：

- private context compiler；
- high-dimensional projection；
- hidden-state bridge；
- evidence weighting；
- graph compilation；
- memory scheduling optimizer；
- reconvergence implementation。

因此：

$$
\boxed{
\text{Public Expansion Theory}
\neq
\text{Private Cognitive Compiler}.
}
$$
