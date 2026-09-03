# 分散式認知研究組織：論文庫如何從 Corpus 變成 Research Environment

## Distributed Epistemic Research Organizations: From Corpus to Research Environment

**系列**：AI 原生分散式組織系列，第 5 篇／共 10 篇  
**系列英文名**：AI-Native Distributed Organization Series  
**文件編號**：EML-ANDO-2026-05-v0.1  
**作者**：Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1  
**日期**：2026-08-20  
**性質**：理論框架／Distributed Research Organization／Research Environment／Knowledge Graph／Autonomous Research  
**狀態**：Public Theory Draft  
**直接前置**：《共享狀態中心論》v0.1；《非階層式 Agent 組織》v0.1；《委任主權論》v0.1；《AI 單次品質論》v0.1  
**Source fingerprint**：見正式 source package `SHA256SUMS.txt`

---

## 生成與保真聲明

本文為 AI 輔助生成的理論與工程框架草稿。本文不宣稱已完成對所有研究領域、研究機構或自主科研系統的實證驗證。本文中的形式化結構主要用於描述研究狀態、主張、證據、驗證、任務與組織關係，不應被誤解為所有研究活動都能完全形式化。

若本文未來加入外部文獻、數據、數學證明、實驗結果或法律與學術規範判斷，應依其內容類型採用對應 verification contract。本文特別主張：AI-generated research artifact 不應因為生成流程完整，就自動被視為真實、可發表或可引用的知識。

---

## 摘要

當研究者擁有大量論文、技術文件、理論分支、實驗紀錄與版本歷史時，傳統論文庫主要扮演儲存與檢索功能：使用者先提出問題，再從 corpus 中搜尋相關文章。然而，當 AI Agent 能持續讀取研究庫、搜尋外部前沿、追蹤未解問題、提出新假說、比較理論、執行計算、進行批判與驗證時，研究庫可以從靜態「內容集合」轉變為動態「研究環境」。

本文提出「分散式認知研究組織」（Distributed Epistemic Research Organization, DERO）概念。其核心不是讓一個中央 AI 自動寫大量論文，而是把既有研究內容轉換為 canonical research state，讓多個可替換 Agent 在共享研究狀態、權限、驗證規則與 artifact lineage 上形成分散式研究組織。

本文定義研究環境：

$$
\mathcal E_R(t)
=
(
\mathcal K_t,
\mathcal C_t,
\mathcal E_t,
\mathcal Q_t,
\mathcal T_t,
\mathcal V_t,
\mathcal B_t,
\mathcal A_t,
\mathcal L_t,
\mathcal P_t
),
$$

其中分別表示知識資產、主張集合、證據集合、未解問題、任務圖、驗證狀態、研究分支、Agent 集合、血統紀錄與治理政策。論文不再只是終端輸出，而是研究狀態中的一種 artifact。

本文進一步區分 Corpus、Knowledge Base、Research State、Research Environment 與 Research Organization 五個層級，提出：

$$
\boxed{
\text{Corpus}
\rightarrow
\text{Knowledge Base}
\rightarrow
\text{Research State}
\rightarrow
\text{Research Environment}
\rightarrow
\text{Research Organization}.
}
$$

真正的轉換不是「讓 AI 多寫文章」，而是讓研究系統知道：哪些命題已被驗證、哪些只是猜想、哪些證據互相衝突、哪些理論依賴尚未補完、哪些研究線已停滯、哪些問題可被平行化、哪些 artifact 可以公開、哪些必須保留為 internal candidate。

本文提出 Research Object、Claim Graph、Evidence Graph、Problem Frontier、Branch State、Verification State、Novelty State、Dependency State 與 Publication State 等基本資料結構，並設計 Explorer、Literature、Mathematics、Critic、Counterexample、Verifier、Curator、Integrator、Engineer 與 Publisher 等可替換 Agent 角色。研究組織因此不是永久階層，而是由研究問題誘導出的 task-conditioned graph。

本文也引入 Research Frontier Density、Claim Verification Ratio、Dependency Closure、Branch Productivity、Research Sedimentation Efficiency、Epistemic Debt 與 Human Governance Density 等診斷量，用於區分「大量 AI activity」與「真正形成可驗證研究沉積」。最終，本文主張大型論文庫的真正 AI-native 轉型不是 RAG 增強，而是建立一個可持續運行、可分支、可驗證、可審計、可恢復的 Research Environment。

**關鍵詞**：Distributed Epistemic Research Organization、Research Environment、Autonomous Research、Claim Graph、Evidence Graph、Research Frontier、Epistemic Debt、AI Research Governance、Knowledge Base、Research State

---

# 0. 核心問題：論文庫到底是什麼？

最簡單的論文庫可以表示為：

$$
\mathcal D
=
\{
p_1,p_2,\ldots,p_n
\}.
$$

其中每個：

$$
p_i
$$

是一篇文章或文件。

傳統使用方式是：

$$
Question
\rightarrow
Retrieve
\rightarrow
Read
\rightarrow
Answer.
$$

這仍然把論文庫視為：

$$
\boxed{
\text{Passive Corpus}.
}
$$

但對長期研究而言，真正重要的問題不只是：

> 有哪些論文？

而是：

- 現在有哪些研究線？
- 哪些 claim 已證？
- 哪些只是 conjecture？
- 哪些證據互相衝突？
- 哪些問題尚未解決？
- 哪些理論依賴斷裂？
- 哪些 artifact 已完成但尚未發表？
- 哪些方向值得繼續投入？
- 哪些方向已經重複？
- 哪些問題需要人類判斷？

只要這些狀態沒有被表示，AI 即使能讀完整 corpus，也仍然需要每次重新推導研究現況。

---

# 1. 五層轉換

本文區分五個層級。

## 1.1 Corpus

$$
\mathcal C_0
=
\{
Document
\}.
$$

回答：

> 有什麼內容？

---

## 1.2 Knowledge Base

$$
\mathcal K
=
(
Documents,
Metadata,
Index,
Relations
).
$$

回答：

> 內容之間有什麼關係？

---

## 1.3 Research State

$$
\mathcal S_R
=
(
Claims,
Evidence,
Problems,
Dependencies,
Verification,
Branches
).
$$

回答：

> 現在研究做到哪裡？

---

## 1.4 Research Environment

$$
\mathcal E_R
=
\mathcal S_R
+
Tasks
+
Agents
+
Tools
+
Policies
+
Runtime.
$$

回答：

> 研究如何繼續運作？

---

## 1.5 Research Organization

$$
\mathcal O_R
=
\mathcal E_R
+
Delegation
+
Governance
+
Persistent Coordination.
$$

回答：

> 哪些智能節點可以持續共同推進研究？

因此：

$$
\boxed{
\text{Corpus}
\neq
\text{Research Organization}.
}
$$

---

# 2. Research Environment 的正式表示

本文定義：

$$
\mathcal E_R(t)
=
(
\mathcal K_t,
\mathcal C_t,
\mathcal E_t,
\mathcal Q_t,
\mathcal T_t,
\mathcal V_t,
\mathcal B_t,
\mathcal A_t,
\mathcal L_t,
\mathcal P_t
).
$$

其中：

$$
\mathcal K_t
=
\text{Knowledge Assets},
$$

$$
\mathcal C_t
=
\text{Claim Set},
$$

$$
\mathcal E_t
=
\text{Evidence Set},
$$

$$
\mathcal Q_t
=
\text{Open Questions / Problem Frontier},
$$

$$
\mathcal T_t
=
\text{Research Task Graph},
$$

$$
\mathcal V_t
=
\text{Verification State},
$$

$$
\mathcal B_t
=
\text{Branch State},
$$

$$
\mathcal A_t
=
\text{Available Agents},
$$

$$
\mathcal L_t
=
\text{Lineage / Provenance},
$$

$$
\mathcal P_t
=
\text{Research Policies}.
$$

這使研究不是「從文檔生成文檔」，而是：

$$
State_t
\rightarrow
ResearchAction
\rightarrow
State_{t+1}.
$$

---

# 3. 論文不是唯一基本單位

如果研究系統只以「文章」為最小單位，會遇到一個問題：

一篇文章可能同時包含：

- 已知事實；
- 外部引用；
- 原創 conjecture；
- 部分證明；
- 失敗路線；
- 假設；
- 實驗結果；
- 尚未驗證的推論。

因此本文引入：

$$
ResearchObject.
$$

定義：

$$
r_i
=
(
type,
content,
status,
source,
dependencies,
verification,
lineage
).
$$

ResearchObject 可以是：

- claim；
- theorem candidate；
- conjecture；
- definition；
- proof fragment；
- counterexample；
- dataset；
- experiment；
- code artifact；
- citation；
- unresolved question；
- failure note；
- design decision。

論文只是：

$$
Paper
=
Compose(
r_1,r_2,\ldots,r_m
).
$$

---

# 4. Claim Graph

令：

$$
G_C
=
(
V_C,E_C
).
$$

其中：

$$
V_C
=
\{
c_1,c_2,\ldots,c_n
\}
$$

是 claim。

邊可以表示：

$$
supports,
contradicts,
depends,
generalizes,
specializes,
equivalent,
unknown.
$$

因此：

$$
c_i
\xrightarrow{depends}
c_j
$$

表示：

$$
c_i
$$

依賴：

$$
c_j.
$$

若：

$$
c_j
$$

被推翻，系統可以追蹤哪些 claim 受到影響。

---

# 5. Evidence Graph

令：

$$
G_E
=
(
V_E,E_E
).
$$

Evidence node 可以包括：

- 原始論文；
- dataset；
- computation；
- proof checker output；
- code execution；
- experimental observation；
- primary source；
- external database result。

Claim 與 evidence 關係可表示為：

$$
c_i
\leftrightarrow
\{
e_1,e_2,\ldots,e_k
\}.
$$

因此研究系統可以問：

> 這個 claim 到底依賴什麼？

而不是只問：

> 這個 claim 出現在哪篇文章？

---

# 6. Verification State

對每個 claim：

$$
c_i
$$

定義：

$$
V(c_i)
=
(
v_{source},
v_{logic},
v_{math},
v_{data},
v_{citation},
v_{replication}
).
$$

不同 claim type 不必使用全部維度。

例如：

### 數學 claim

可以重視：

$$
v_{logic},
v_{math}.
$$

### data claim

可以重視：

$$
v_{source},
v_{data},
v_{replication}.
$$

### literature claim

可以重視：

$$
v_{source},
v_{citation}.
$$

因此：

$$
\boxed{
\text{Verification must be typed by claim class.}
}
$$

---

# 7. Problem Frontier

真正的研究環境不只保存已知內容。

它還必須保存：

$$
\mathcal Q_t
=
\{
q_1,q_2,\ldots,q_m
\}.
$$

每個 open question：

$$
q_i
=
(
problem,
importance,
difficulty,
dependencies,
attempts,
status,
expectedValue
).
$$

因此 Agent 可以自主尋找：

$$
q_i^\star
=
\arg\max_{q_i}
ResearchValue(q_i).
$$

而不是每次都等待人類說：

> 下一篇寫什麼？

---

# 8. Research Frontier

可把研究前沿表示為：

$$
\mathcal F_t
=
\{
q_i
\in
\mathcal Q_t
:
Ready(q_i)=1
\}.
$$

其中 Ready 可以依：

- dependency 是否滿足；
- 是否有足夠工具；
- 是否有足夠資料；
- 是否在 budget 內；
- 是否需要 human decision；
- 是否與其他 branch 重複。

因此：

$$
\boxed{
\text{Research Frontier}
\neq
\text{Latest Paper}.
}
$$

它是當下真正可推進的未解研究邊界。

---

# 9. Branch State

研究天然會分支。

定義：

$$
\mathcal B_t
=
\{
b_1,b_2,\ldots,b_k
\}.
$$

每個 branch：

$$
b_i
=
(
root,
goal,
claims,
tasks,
status,
budget,
agents,
artifacts
).
$$

Branch status 可為：

$$
Active,
Paused,
Blocked,
Merged,
Archived,
Rejected.
$$

如此 AI 可以知道：

> 這條路不是沒人想到，而是之前已經走過而且失敗。

這對避免重複研究非常重要。

---

# 10. Failure 也是 Research Object

傳統論文往往只保存成功結果。

但對 autonomous research：

$$
Failure
$$

本身也是高價值 state。

例如：

$$
f_i
=
(
attempt,
reason,
conditions,
evidence,
reusability
).
$$

如果 failure 不被 canonicalize：

$$
A_1
$$

失敗後：

$$
A_2
$$

可能重新走完全相同路線。

因此：

$$
\boxed{
\text{Negative Results}
\text{ can reduce future research time.}
}
$$

---

# 11. Research Agent 角色

本文不主張一個 AI 同時做全部事情。

可以定義：

$$
\mathcal A_R
=
\{
A_{explore},
A_{lit},
A_{math},
A_{critic},
A_{counter},
A_{verify},
A_{curate},
A_{integrate},
A_{engineer},
A_{publish}
\}.
$$

這些是角色，不必綁定固定模型。

---

# 12. Explorer Agent

負責：

- 找新連接；
- 提出 conjecture；
- 發現 corpus 中隱含結構；
- 建立新的 problem candidate。

其輸出預設是：

$$
Provisional.
$$

而不是：

$$
CanonicalTruth.
$$

---

# 13. Literature Agent

負責：

- 搜尋外部前沿；
- 回查原始來源；
- 找相似工作；
- 更新 prior-art state；
- 標記 citation risk。

它不應只提供摘要，而應返回：

$$
Source,
Claim,
Date,
Context,
Relevance,
Confidence.
$$

---

# 14. Mathematics Agent

負責：

- symbolic derivation；
- theorem candidate；
- counterexample search；
- CAS；
- proof assistant；
- numerical sanity check。

數學 Agent 產生的結果仍應區分：

$$
Derived,
Checked,
FormallyVerified,
Unverified.
$$

---

# 15. Critic 與 Counterexample Agent

Critic 不只是：

> 給文章打分。

它應嘗試破壞：

$$
Claim,
Inference,
Definition,
Assumption,
Scope.
$$

Counterexample Agent 則特別尋找：

$$
x
$$

使：

$$
Claim(x)=\mathrm{False}.
$$

因此：

$$
\boxed{
\text{Research Organization}
\text{ needs anti-confirmation roles.}
}
$$

---

# 16. Verifier Agent

Verifier 應根據 claim type 選擇 contract。

例如：

$$
Verify(c_i)
=
Contract(type(c_i)).
$$

因此驗證不是一個通用 prompt，而是一個：

$$
\boxed{
\text{Typed Verification Runtime}.
}
$$

---

# 17. Curator Agent

Curator 的工作不是產生新內容。

而是：

- 去重；
- 合併相似 claim；
- 修正 metadata；
- 更新 lineage；
- 標記 obsolete state；
- 清理 orphan artifact；
- 維護 branch graph。

這對大型研究環境非常重要。

否則：

$$
N_{artifact}\uparrow
$$

會迅速造成：

$$
EpistemicDebt\uparrow.
$$

---

# 18. Integrator Agent

Integrator 負責：

$$
\{
c_1,c_2,\ldots,c_n
\}
\rightarrow
Synthesis.
$$

但 synthesis 必須保留：

$$
Lineage.
$$

因此新的整合理論不能讓原始異議消失。

---

# 19. Engineer Agent

當研究需要：

- prototype；
- code experiment；
- benchmark；
- simulation；
- visualization；

Engineer Agent 形成：

$$
Theory
\rightarrow
ExecutableArtifact.
$$

這使 Research Environment 不只停在文字生成。

---

# 20. Publisher Agent

Publisher 只負責：

$$
CanonicalResearchState
\rightarrow
PublishableArtifact.
$$

而不是自行決定所有 claim 都可以公開。

因此：

$$
Publish
\Rightarrow
VerificationPolicyPassed
+
AuthorityValid.
$$

---

# 21. 研究拓撲是任務誘導的

對某問題：

$$
q_i
$$

可以形成：

$$
A_{explore}
\rightarrow
\{
A_{lit},
A_{math},
A_{counter}
\}.
$$

再：

$$
\{
A_{lit},
A_{math},
A_{counter}
\}
\rightarrow
A_{integrate}.
$$

之後：

$$
A_{critic}
\rightarrow
A_{verify}
\rightarrow
A_{curate}.
$$

最後才可能：

$$
A_{publish}.
$$

另一個問題可能完全使用不同 topology。

因此：

$$
\boxed{
\text{Research Organization}
\text{ is a dynamic graph over persistent research state.}
}
$$

---

# 22. Human Governance 在哪裡？

Distributed research 不表示人類完全退出。

Human Bridge 可以保留在：

- 高價值理論分岔；
- 作者責任；
- 高爭議 claim；
- publication policy；
- 法律與倫理限制；
- 高成本資源配置；
- 外部不可逆承諾。

因此：

$$
Human
\notin
EveryTransition.
$$

但：

$$
Human
\in
HighGovernanceValueTransitions.
$$

---

# 23. Research Governance Density

沿用前置理論，可定義：

$$
\rho_R^H
=
\frac{
N_{\mathrm{human\ research\ governance\ interventions}}
}{
N_{\mathrm{effective\ research\ transitions}}+\epsilon
}.
$$

目標不一定是：

$$
\rho_R^H
\rightarrow0.
$$

而是：

$$
\boxed{
\text{Human attention should concentrate on high-governance-value research states.}
}
$$

---

# 24. Claim Verification Ratio

定義：

$$
CVR
=
\frac{
N_{\mathrm{verified\ claims}}
}{
N_{\mathrm{active\ claims}}+\epsilon
}.
$$

但不是所有 claim 都必須立即驗證。

Exploratory branch 可以暫時維持：

$$
CVR
\text{ low}
$$

但 publishable branch 應要求更高：

$$
CVR.
$$

因此 CVR 應與 branch state 一起解讀。

---

# 25. Dependency Closure

定義：

$$
DC
=
\frac{
N_{\mathrm{resolved\ required\ dependencies}}
}{
N_{\mathrm{required\ dependencies}}+\epsilon
}.
$$

如果一篇 candidate paper 的核心 claim 有大量 unresolved dependency：

$$
DC\ll1,
$$

則即使文章文字完整，也不代表研究完成。

---

# 26. Research Frontier Density

定義：

$$
RFD
=
\frac{
N_{\mathrm{ready\ frontier\ problems}}
}{
N_{\mathrm{active\ research\ objects}}+\epsilon
}.
$$

過低可能表示：

- 研究已停滯；
- dependency 沒有被解；
- 問題沒有被顯式表示。

過高則可能表示：

- problem generation 過多；
- verification / closure 跟不上。

---

# 27. Branch Productivity

對 branch：

$$
b_i
$$

定義：

$$
BP(b_i)
=
\frac{
V_{\mathrm{verified\ new\ knowledge}}
}{
C_{\mathrm{research}}+\epsilon
}.
$$

其中成本可以包含：

$$
Token,
Compute,
HumanTime,
AgentTime,
ExternalTools.
$$

這比單純計算：

$$
N_{\mathrm{papers}}
$$

更有意義。

---

# 28. Research Sedimentation Efficiency

沿用時間經濟學的 sedimentation 概念，定義：

$$
\eta_R
=
\frac{
V_{\mathrm{verified\ research\ sediment}}
}{
W_R^{total}+\epsilon
}.
$$

若 AI 一天生成大量文章，但：

$$
\eta_R
\rightarrow0,
$$

則只是研究噪音。

因此：

$$
\boxed{
\text{Research Throughput}
\neq
\text{Research Progress}.
}
$$

---

# 29. Epistemic Debt

本文定義：

$$
D_E
=
D_{unverified}
+
D_{duplicate}
+
D_{dependency}
+
D_{citation}
+
D_{orphan}
+
D_{contradiction}.
$$

分別表示：

- 未驗證債；
- 重複債；
- 依賴債；
- 引用債；
- orphan artifact 債；
- 未處理矛盾債。

如果：

$$
D_E\uparrow
$$

速度大於：

$$
KnowledgeClosure,
$$

研究環境會逐漸失去可信度。

---

# 30. Novelty 不能只由 AI 自評

研究系統需要區分：

$$
NovelToCorpus,
NovelToProject,
NovelToLiterature,
NovelToWorld.
$$

AI 很容易把：

> 我在本次 context 沒看過

誤認成：

> 世界上沒有人做過。

因此：

$$
\boxed{
\text{Context Novelty}
\neq
\text{Literature Novelty}.
}
$$

Novelty claim 必須經 external literature check 才能升級。

---

# 31. Publication State

每個 research artifact 可具有：

$$
PState
\in
\{
Scratch,
Candidate,
Internal,
Verified,
Publishable,
Published,
Deprecated,
Retracted
\}.
$$

如此：

$$
AI\text{-generated}
$$

不會直接跳到：

$$
Published.
$$

---

# 32. Research Domain 而不是人格模仿

AI 代理人不需要：

> 模仿研究者本人講話。

它需要進入的是：

$$
\mathcal D_R
=
(
Corpus,
Definitions,
Claims,
Methods,
Policies,
History,
OpenProblems
).
$$

因此：

$$
\boxed{
\text{Research Continuity}
\text{ can be domain-based rather than personality-based.}
}
$$

這使多模型、多 Agent 與未來替換更加乾淨。

---

# 33. 外部前沿的角色

Research Environment 不能封閉在自己的 corpus。

需要持續接收：

$$
ExternalLiterature,
Web,
Databases,
Code,
Benchmarks,
ExperimentalData.
$$

但外部資訊必須經：

$$
Retrieve
\rightarrow
SourceCheck
\rightarrow
ClaimExtraction
\rightarrow
Relevance
\rightarrow
CanonicalProposal.
$$

不能：

$$
SearchResult
\rightarrow
CanonicalTruth.
$$

---

# 34. 內部與公開研究域

研究環境可以分成：

$$
\mathcal E_R^{public}
$$

與：

$$
\mathcal E_R^{internal}.
$$

公開域可偏向：

- 可引用；
- 可重現；
- 已完成；
- 可對外解釋。

內部域可保存：

- speculative branches；
- unfinished mathematics；
- failed experiments；
- commercial ideas；
- private governance notes。

兩者可以共享部分 lineage，但 authority 與 publication policy 不同。

---

# 35. Research Object 的生命週期

一個 research object 可以經過：

$$
Idea
\rightarrow
Candidate
\rightarrow
Investigating
\rightarrow
Supported
\rightarrow
Verified
\rightarrow
Integrated
\rightarrow
Published.
$$

也可能：

$$
Candidate
\rightarrow
Rejected
$$

或：

$$
Supported
\rightarrow
Deprecated.
$$

因此研究狀態天然不是線性的。

---

# 36. 自主研究的停止條件

自主研究不能只是：

$$
\mathrm{while}(\mathrm{True}):
\quad
\mathrm{research}()
$$

至少需要：

$$
Stop
\Leftarrow
\{
GoalReached,
BudgetExceeded,
NoMarginalGain,
Blocked,
RiskExceeded,
HumanDecisionRequired
\}.
$$

也可以定義：

$$
\Delta V_R
=
V_R(t+1)-V_R(t).
$$

若長期：

$$
\Delta V_R
<
\epsilon,
$$

則 branch 應被 pause、reformulate 或 archive。

---

# 37. 多 Agent 共識不等於研究正確

若：

$$
A_1,A_2,A_3
$$

都同意：

$$
c,
$$

只能得到：

$$
Consensus(c).
$$

不能直接得到：

$$
Truth(c).
$$

因此：

$$
\boxed{
\text{Agent Consensus}
\neq
\text{Epistemic Verification}.
}
$$

共識可以觸發：

$$
ReviewPriority,
$$

但不能取代 evidence 與 formal validation。

---

# 38. AI-generated Research Disclosure

對公開 artifact，應保留：

$$
GenerationProvenance.
$$

例如：

- AI-generated；
- AI-assisted；
- human-reviewed；
- source-checked；
- formally verified；
- experimentally reproduced。

與其只寫：

> AI 可能犯錯。

更有資訊量的是：

$$
\boxed{
\text{What was generated?}
+
\text{What was checked?}
+
\text{What remains uncertain?}
}
$$

---

# 39. 第一代研究組織診斷向量

定義：

$$
\mathbf Z_R
=
(
CVR,
DC,
RFD,
\eta_R,
D_E,
\rho_R^H,
Q_{novelty},
Q_{lineage},
Q_{publication}
).
$$

其中：

- $CVR$：Claim Verification Ratio；
- $DC$：Dependency Closure；
- $RFD$：Research Frontier Density；
- $\eta_R$：Research Sedimentation Efficiency；
- $D_E$：Epistemic Debt；
- $\rho_R^H$：Human Research Governance Density；
- $Q_{novelty}$：Novelty Assessment Quality；
- $Q_{lineage}$：Lineage Quality；
- $Q_{publication}$：Publication Gate Quality。

---

# 40. 可檢驗命題

## 命題一：Corpus-to-State Advantage

將 corpus 轉成 claim / evidence / problem / dependency state，應降低 Agent 重複理解研究現況的時間。

## 命題二：Failure Memory Advantage

保存 negative results 與 failed routes，應降低重複失敗率。

## 命題三：Typed Verification Advantage

typed verification contract 應比單一通用 reviewer prompt 更能降低不同研究類型的錯誤。

## 命題四：Frontier Explicitness

將 open problems 顯式表示為 canonical frontier，應提升 autonomous task selection 的穩定性。

## 命題五：Role Separation

Explorer、Critic、Verifier 與 Curator 的角色分離，應降低單一 Agent 自我確認偏差。

## 命題六：State-Centric Research Continuity

即使 Agent 與模型更換，只要 research state 與 lineage 完整，研究線 continuity 應可維持。

---

# 41. 第一代實驗設計

## 41.1 Static RAG vs Research Environment

模式 A：

$$
Corpus
+
RAG.
$$

模式 B：

$$
ResearchEnvironment.
$$

比較：

$$
TaskSetupTime,
DuplicateRate,
StateRecovery,
VerificationCoverage,
ResearchProgress.
$$

## 41.2 Agent Replacement

研究中途替換主要 Agent，測試是否能依：

$$
\mathcal E_R(t)
$$

接續同一 branch。

## 41.3 Failed-Route Replay

讓新 Agent 接手已失敗問題，測試 canonical failure memory 是否降低重複探索。

## 41.4 Frontier Selection

比較由人類逐次指定問題與 Agent 自主從：

$$
\mathcal F_t
$$

選擇問題的結果。

## 41.5 Verification Contract Test

對數學、引用、資料與概念論文分別使用 typed contract，比較錯誤率。

## 41.6 Publication Gate Test

故意讓高文字品質但低 verification 的 paper candidate 進入 publish queue，測試是否被 gate 阻擋。

---

# 42. 與前四篇的閉合

目前系列已形成：

$$
\text{Operator Exit}
\rightarrow
\text{Delegated Sovereignty}
\rightarrow
\text{Dynamic Topology}
\rightarrow
\text{Shared State}
\rightarrow
\text{Research Organization}.
$$

第 4 篇回答：

> 組織記憶應該在哪裡？

本篇回答：

> 當 shared state 中放入研究 claim、evidence、problem、branch 與 verification 後，它會變成什麼？

答案是：

$$
\boxed{
\text{A persistent distributed epistemic research organization.}
}
$$

---

# 43. 與下一篇的接口

一旦 AI 可以持續產生：

$$
Claim,
Paper,
Code,
Experiment,
Citation,
ProofCandidate,
$$

下一個最危險的問題就是：

> 這些東西要怎麼判斷可以信到什麼程度？

因此下一篇將正式建立：

# **AI 研究保真與認知責任：異質證據的 Verification Contract**

核心問題是：

$$
\boxed{
\text{不同 epistemic object 必須接受不同保真義務。}
}
$$

也就是：

- 有數據的，必須查數據；
- 有引用的，必須回來源；
- 有數學推理的，必須獨立驗證；
- 有實驗的，必須區分「真的跑過」與「只描述了實驗」；
- 有論證缺口的，必須標示；
- AI-generated 的，必須保存 provenance。

---

# 44. 理論限制

第一，將研究轉為 structured state 可能過度形式化創造性研究，因此不能要求所有 exploratory thinking 都立即結構化。

第二，Research Object schema 本身可能成為偏見來源；不同學科需要不同 object type。

第三，external literature retrieval 仍受搜尋品質、資料庫覆蓋與存取權限制。

第四，AI verifier 仍可能與 producer 共享系統性盲點，因此高風險研究需要獨立方法與外部工具。

第五，研究價值函數難以完全形式化，不能只靠單一 scalar 排序研究問題。

第六，分散式研究組織的產出量增加後，publication gate 與 curator 會變得更加重要，否則可能形成高規模低可信輸出。

---

# 45. 結論

大型論文庫真正的 AI-native 未來，不是：

$$
\boxed{
\text{More Documents}
+
\text{Better Search}.
}
$$

而是：

$$
\boxed{
\text{Persistent Research State}
+
\text{Dynamic Agent Topology}
+
\text{Typed Verification}
+
\text{Governance}
+
\text{Runtime}.
}
$$

因此：

$$
\boxed{
\text{Corpus}
\rightarrow
\text{Research Environment}
}
$$

不是單純的 RAG 升級。

它代表研究系統開始知道：

- 什麼已知；
- 什麼未知；
- 什麼可疑；
- 什麼被驗證；
- 什麼已失敗；
- 什麼值得繼續；
- 什麼必須等待人類；
- 什麼可以被公開。

當這些狀態都能被多個可替換 Agent 共同讀寫、批判、驗證與推進時，論文庫就不再只是研究的過去。

它開始成為：

$$
\boxed{
\text{研究本身持續發生的環境。}
}
$$

而這也使「AI 自主研究」從一個模型能力問題，正式提升為：

$$
\boxed{
\text{組織、狀態、驗證與治理的共同問題。}
}
$$

---

# 符號表

| 符號 | 定義 |
|---|---|
| $\mathcal E_R(t)$ | 時間 $t$ 的 Research Environment |
| $\mathcal K_t$ | Knowledge Assets |
| $\mathcal C_t$ | Claim Set |
| $\mathcal E_t$ | Evidence Set |
| $\mathcal Q_t$ | Open Questions / Problem Frontier |
| $\mathcal T_t$ | Research Task Graph |
| $\mathcal V_t$ | Verification State |
| $\mathcal B_t$ | Branch State |
| $\mathcal A_t$ | Available Research Agents |
| $\mathcal L_t$ | Lineage / Provenance |
| $\mathcal P_t$ | Research Policies |
| $G_C$ | Claim Graph |
| $G_E$ | Evidence Graph |
| $\mathcal F_t$ | Research Frontier |
| $CVR$ | Claim Verification Ratio |
| $DC$ | Dependency Closure |
| $RFD$ | Research Frontier Density |
| $BP$ | Branch Productivity |
| $\eta_R$ | Research Sedimentation Efficiency |
| $D_E$ | Epistemic Debt |
| $\rho_R^H$ | Human Research Governance Density |

---

# 前置依賴

1. Neo.K with Aletheia，《從 AI 工具到 AI 組織：操作員退出問題》v0.1，2026。
2. Neo.K with Aletheia，《委任主權論：高 AI 自主與高人類主權能否共存》v0.1，2026。
3. Neo.K with Aletheia，《非階層式 Agent 組織：從管理樹到動態協作圖》v0.1，2026。
4. Neo.K with Aletheia，《共享狀態中心論：為什麼中央不能是某一個 AI》v0.1，2026。
5. Neo.K，《AI 單次品質論：意圖忠實度、過程品質、完成度與結果品質》v0.1，2026。
6. Neo.K，《委任時間論：自主 Agent、人類介入密度與治理槓桿》v0.1，2026。
7. Neo.K，《Interaction-Time Runtime & Agent Temporal Ledger v0.1》，2026。

---

# 版本紀錄

- **v0.1 / 2026-08-20**：建立 Distributed Epistemic Research Organization、Research Environment 五層轉換、Research Object、Claim Graph、Evidence Graph、Problem Frontier、Branch State、typed Verification State、Epistemic Debt、Research Sedimentation Efficiency 與第一代實驗設計。
