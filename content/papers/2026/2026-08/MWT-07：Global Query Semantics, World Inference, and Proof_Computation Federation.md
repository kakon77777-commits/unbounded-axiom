# MWT-07：Global Query Semantics, World Inference, and Proof/Computation Federation
## 世界查詢語義、責任分解、證明—計算—搜尋—模擬聯邦與可證書化回答

**英文題名：** *MWT-07: Global Query Semantics, World Inference, and Proof/Computation Federation — Inquiry Contracts, Obligation Decomposition, Proof–Computation–Search–Simulation Federation, and Certifiable Answers*  
**系列：** Mathematical World Theory（MWT）  
**篇次：** 07  
**文件編號：** EML-MWT-07-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-19  
**版本：** v0.1  
**文件性質：** 數學世界論第七篇形式母稿／Global Query Semantics／World Inference／Proof–Computation Federation  
**前置文件：** MWT-01 ～ MWT-06  
**狀態：** 可使用研究稿；提供 reference query compiler / obligation router；不宣稱存在對所有問題都能自動產生完備查詢計畫的 universal planner  

---

## 摘要

MWT-01 至 MWT-06 已建立一個可運行的數學世界框架：World 可以由多種 presentations 表示；跨 presentation interaction 必須先接受 legality judgment；合法 interactions 由 noncommutative scheduler 以 partial order 執行；執行結果被收成可 reopen 的 world-state runtime；世界可以在有限 active support 下持續 refinement；不同尺度與 solver 又能透過 coupling ports 形成 Multi-Resolution World Solve。

此時，一個新的核心問題變得無法迴避：

> **當人類或 AI 對這個數學世界提出一個問題時，什麼才算真正理解了這個問題？系統如何知道應啟動哪些 presentation、proof system、numerical solver、simulation、retrieval source、observer、counterexample search、bridge、coupling 與 verification path？**

如果 query 只被視為自然語言字串：

$$
q=\text{``Is }P=NP\text{?''},
$$

那麼世界 runtime 最多只能依關鍵詞或模型直覺選工具。這會再次把一個全域數學問題過早壓縮成單一路徑。

本文提出 **Global Query Semantics（GQS）**、**World Inference Graph（WIG）** 與 **Proof/Computation Federation（PCF）**。其核心立場是：

$$
\boxed{
\text{Query}
\neq
\text{String}
\neq
\text{Single Solver Call}.
}
$$

在 MWT 中，一個完整 world query 被表示為一份 **Inquiry Contract**：

$$
\boxed{
\mathfrak Q
=
(
I,
D,
A,
\mathfrak I,
\mathcal E,
\mathcal V,
\mathcal T,
\mathcal R,
B,
\Pi_{\mathrm{out}}
).
}
$$

其中：

- $I$：intent / 欲結構，描述真正想知道、找到、構造或判定什麼；
- $D$：scope / domain；
- $A$：answer contract，規定允許的答案型態；
- $\mathfrak I$：identity specification；
- $\mathcal E$：evidence / proof requirement；
- $\mathcal V$：validation / certificate requirement；
- $\mathcal T$：temporal / version scope；
- $\mathcal R$：risk / consequence profile；
- $B$：resource budget；
- $\Pi_{\mathrm{out}}$：人類／AI輸出投影。

這使同一句自然語言在不同 inquiry contracts 下成為不同 query。例如：

> 「這個猜想對嗎？」

至少可以分成：

1. 找一個 counterexample；
2. 找正式 proof；
3. 估計 empirical plausibility；
4. 在指定有限 domain 驗證；
5. 判定某 formalization 中的 theoremhood；
6. 比較不同 foundations 的結果；
7. 尋找是否已有外部文獻解決。

它們不是同一 execution plan。

本文將 query 進一步編譯成 **Obligation Hypergraph**：

$$
\boxed{
\mathcal G_{\mathfrak Q}^{O}
=
(
\mathcal O_{\mathfrak Q},
E_{\mathrm{dep}},
E_{\mathrm{alt}},
E_{\mathrm{join}},
E_{\mathrm{refute}}
).
}
$$

其中 obligations 可包含：

$$
\boxed{
\mathcal O_{\mathfrak Q}
\subseteq
\{
O_{\mathrm{proof}},
O_{\mathrm{compute}},
O_{\mathrm{retrieve}},
O_{\mathrm{simulate}},
O_{\mathrm{observe}},
O_{\mathrm{formalize}},
O_{\mathrm{translate}},
O_{\mathrm{counterexample}},
O_{\mathrm{couple}},
O_{\mathrm{certify}},
O_{\mathrm{human}}
\}.
}
$$

query 的完成不要求所有 obligations 都執行，而要求所有 **mandatory answer obligations** 被滿足，並且替代路徑、失敗路徑與未完成 coverage 被明確記錄。

本文引入 **Query Answer Bundle**：

$$
\boxed{
\mathfrak A_{\mathfrak Q}
=
(
\mathcal C^+,
\mathcal C^-,
\mathcal U,
\mathcal X,
\mathcal P,
\mathcal H,
\Sigma
).
}
$$

其中：

- $\mathcal C^+$：正向 claims / support；
- $\mathcal C^-$：反向 claims / refutation；
- $\mathcal U$：unresolved；
- $\mathcal X$：conflicts；
- $\mathcal P$：provenance / presentations；
- $\mathcal H$：history / query plan execution；
- $\Sigma$：completion / coverage certificate。

因此回答不再只是：

$$
\boxed{
\text{Yes / No}.
}
$$

而可能是：

- formally proved relative to foundation $T$ ；
- formally refuted；
- counterexample found；
- numerically supported in domain $D$ ；
- empirically supported but unproved；
- no witness found under search scope $S$ ；
- unresolved；
- conflicted across contexts；
- question ill-posed under current identity specification。

本文特別固定：

$$
\boxed{
\text{Not Found}
\not\Rightarrow
\text{Does Not Exist}.
}
$$

這一點直接延續既有 GIPSS v0.2 的核心：有限搜尋只能證明在資料域、策略與預算下未找到；若要給出 existential negative answer，必須另外建立 coverage / completeness certificate，或有正式 impossibility proof。

在 proof/computation federation 層，本文不把 proof、computation、simulation 與 search 混成同一證據。相反地，定義不同 responsibility types：

- proof 建立相對 formal system 的演繹證書；
- computation 建立可重放的數值／符號結果；
- exhaustive finite search 可以建立有限域完備性證書；
- counterexample 可直接否證 universal claim；
- simulation 提供模型相對行為證據；
- retrieval 提供外部已知結果與來源；
- observation / experiment 提供 empirical evidence；
- LLM / heuristic reasoning 產生 candidate path，但不自動升格成 proof。

本文提出：

$$
\boxed{
\text{Reasoning}
\rightarrow
\text{Candidate}
\rightarrow
\text{Verification}
}
$$

而不是：

$$
\boxed{
\text{LLM says}
\Rightarrow
\text{Theorem}.
}
$$

這與 2026 年 agentic theorem proving 的最新方向高度相容：OpenProver 採 Planner–Worker–Verifier 並以 Lean 4 形式驗證生成 proof；Discover and Prove 明確把「先發現答案」與「再形式證明」分離；Automated Conjecture Resolution 則將 informal reasoning、theorem retrieval 與 formal verification 組成端到端研究流程。MWT 不把自身等同於這些 prover，而將它們視為 $O_{\mathrm{proof}}$ / $O_{\mathrm{formalize}}$ 的成熟 participant backends。

本文亦借用 federated query processing 的成熟教訓：heterogeneous federation 的查詢需要 source selection、query decomposition、query planning 與介面能力感知；不同來源不應被假設支援同一操作。MWT 將這一原則提升到數學世界：不同 solver / presentation / proof backend 具有不同 capabilities，Query Planner 必須先依 obligation 與 interface contract 路由，而不是把整個問題送給每一個工具。

在 AI-native 層，本文提出 Query Compiler、Intent/Scope Resolver、Obligation Graph Builder、Capability Router、Proof Federation Manager、Computation Federation Manager、Evidence Ledger、Counterexample Engine、Coverage Engine、Answer Synthesizer、Query Reopen Engine 等十一個最低模組。

MWT-07 最終將「提問」正式接回數學世界的呼吸循環：

$$
\boxed{
\text{Query}
\rightarrow
\text{Decompose}
\rightarrow
\text{Route}
\rightarrow
\text{Infer / Prove / Compute / Search}
\rightarrow
\text{Cross-Validate}
\rightarrow
\text{Answer}
\rightarrow
\text{Refine / Reopen}.
}
$$

因此一個世界不只會算；它開始知道「一個問題要求它做什麼」。

**關鍵詞：** Mathematical World Theory、Global Query Semantics、Inquiry Contract、World Inference Graph、Proof/Computation Federation、query decomposition、theorem proving、counterexample search、federated query planning、agentic mathematics、AI-native mathematics

---

# 0. 本文的責任：從「世界能算」走到「世界知道自己在回答什麼」

MWT-06 已經允許：

$$
\mathsf{WSolve}_{\Omega}.
$$

但：

> 誰建立 $\Omega$？

如果每次都由人類手工指定：

- participants；
- presentations；
- residuals；
- identity；
- solver；
- tolerance；

那麼 MWT 仍然只是巨大低階 runtime。

真正 AI-native 的下一步，是讓 query 自己產生：

$$
\boxed{
\text{world-solve obligations}.
}
$$

---

# 1. Query 不是字串

自然語言：

> 「這個理論對嗎？」

只是 surface form。

真正需要的是：

$$
\boxed{
\mathfrak Q.
}
$$

兩個完全相同的字串，在不同 context 下可以對應不同 inquiry contract。

---

# 2. Query Surface

令：

$$
q_{\mathrm{surf}}
$$

為原始：

- 自然語言；
- formal formula；
- API request；
- symbolic expression；
- visual selection；
- programmatic call。

Query Compiler 接收它。

---

# 3. Inquiry Contract

定義：

$$
\boxed{
\mathfrak Q
=
(
I,
D,
A,
\mathfrak I,
\mathcal E,
\mathcal V,
\mathcal T,
\mathcal R,
B,
\Pi_{\mathrm{out}}
).
}
$$

這是 MWT-07 的核心 record。

---

# 4. Intent

$$
I
$$

不是一個 embedding。

它描述 query 真正想完成的 relation。

例如：

- 判定；
- 尋找；
- 構造；
- 分類；
- 比較；
- 解釋；
- 證明；
- 否證；
- 模擬；
- 最佳化；
- 發現。

---

# 5. GIPSS 的「欲」作為 Query Intent 前身

既有 GIPSS 已把：

> 不知道名稱，但知道想找哪一種存在。

寫成欲結構。

MWT-07 將這個想法一般化：

$$
\boxed{
I
=
\text{desired answer structure}.
}
$$

所以 query 不一定知道答案名稱。

甚至不一定知道答案是否存在。

---

# 6. Domain / Scope

$$
D
$$

回答：

- 哪個 mathematical domain？
- 哪個 world-state version？
- 哪些 assumptions？
- 哪個 dataset？
- 哪個 finite range？
- 哪些 observers？

沒有 scope 的 universal claim 很容易偷換量詞。

---

# 7. Answer Contract

$$
A
$$

規定：

> 什麼形式的結果才算回答。

例如：

### A1 — Boolean

$$
\mathsf{Yes/No}.
$$

### A2 — Witness

要求：

$$
x
$$

使：

$$
P(x).
$$

### A3 — Counterexample

要求：

$$
x
$$

使：

$$
\neg P(x).
$$

### A4 — Proof

要求 formal derivation。

### A5 — Estimate

允許 interval / probability / bound。

### A6 — Classification

輸出 partition / labels。

### A7 — Construction

輸出 object / algorithm。

### A8 — Structured Branch Answer

允許多個 contexts 下不同答案。

---

# 8. Answer Type Matters

如果 query 只要求 witness：

$$
\exists x:P(x),
$$

找到一個：

$$
x^\ast
$$

即可完成。

如果 query 要求：

$$
\forall x:P(x),
$$

有限 sampled evidence 不足。

所以：

$$
\boxed{
\text{answer contract determines proof burden}.
}
$$

---

# 9. Identity Specification

同一 query：

> 「是不是同一個解？」

若：

$$
\mathfrak I_{\mathrm{value}}
$$

只看數值，

與：

$$
\mathfrak I_{\mathrm{path}}
$$

看 path provenance，

答案可以不同。

因此 query 必須帶：

$$
\mathfrak I.
$$

---

# 10. Evidence Requirement

$$
\mathcal E
$$

聲明可接受：

- formal proof；
- counterexample；
- exhaustive search；
- certified computation；
- empirical evidence；
- literature source；
- expert judgment；
- heuristic candidate。

不同 query 需要不同 maturity。

---

# 11. Validation Requirement

$$
\mathcal V
$$

比 evidence 更進一步，回答：

> 誰來驗？

例如：

- Lean；
- Coq；
- independent numerical implementation；
- interval arithmetic；
- cross-solver agreement；
- human review；
- external dataset replication。

---

# 12. Temporal / Version Scope

$$
\mathcal T
$$

聲明：

- current state；
- historical state；
- theorem library version；
- software version；
- data timestamp；
- external-source freshness。

對 current public information，版本是 query semantics 的一部分。

---

# 13. Risk Profile

$$
\mathcal R
$$

控制：

- false-positive cost；
- false-negative cost；
- proof threshold；
- required redundancy；
- human approval。

高風險 query 不能使用低 maturity evidence 直接 commit。

---

# 14. Budget

$$
B
=
(
B_{\mathrm{time}},
B_{\mathrm{compute}},
B_{\mathrm{search}},
B_{\mathrm{proof}},
B_{\mathrm{external}}
).
$$

budget 影響 execution coverage。

但不能修改命題本身。

---

# 15. Output Projection

$$
\Pi_{\mathrm{out}}
$$

規定最後：

- 人類短答；
- formal certificate；
- machine JSON；
- full research package；
- graph；
- proof object。

不同輸出 presentation 不應改變 underlying answer claim。

---

# 16. Query Class

本文定義候選 class family：

$$
\boxed{
\mathcal T_Q
=
\{
Q_{\exists},
Q_{\forall},
Q_{\mathrm{construct}},
Q_{\mathrm{prove}},
Q_{\mathrm{refute}},
Q_{\mathrm{estimate}},
Q_{\mathrm{classify}},
Q_{\mathrm{opt}},
Q_{\mathrm{causal}},
Q_{\mathrm{id}},
Q_{\mathrm{translate}},
Q_{\mathrm{simulate}},
Q_{\mathrm{discover}},
Q_{\mathrm{meta}}
\}.
}
$$

同一 query 可以同時屬多類。

---

# 17. Existential Query

$$
\boxed{
Q_{\exists}:
\exists x\in D,\ P(x)?
}
$$

positive answer 可由 witness 完成。

negative answer 通常需要：

- exhaustive coverage；
- impossibility proof；
- complete decision procedure。

---

# 18. Universal Query

$$
\boxed{
Q_{\forall}:
\forall x\in D,\ P(x)?
}
$$

negative answer可由一個 counterexample 完成。

positive answer 需要 universal burden。

這種正反責任高度不對稱。

---

# 19. Construction Query

問：

$$
\boxed{
\text{construct }x\text{ such that }C(x).
}
$$

proof obligation 可能是：

1. output exists；
2. output satisfies $C$ ；
3. construction executable；
4. complexity bound if requested。

---

# 20. Proof Query

$$
Q_{\mathrm{prove}}
$$

要求：

$$
T
\vdash
\varphi
$$

或其他 formal certificate。

natural-language argument 可以做 search scaffold，但不滿足 formal answer contract。

---

# 21. Refutation Query

$$
Q_{\mathrm{refute}}
$$

可以透過：

- counterexample；
- model；
- contradiction；
- formal negation proof。

不同 refutation 路徑要分。

---

# 22. Estimate Query

例如：

$$
\theta\in[a,b].
$$

需要：

- error model；
- confidence；
- sample；
- deterministic bound；

依 contract 決定。

---

# 23. Classification Query

要求：

$$
x
\mapsto
c_i.
$$

還需要：

- class ontology；
- boundary；
- multi-label allowance；
- unknown class。

---

# 24. Optimization Query

只有在 query 明示 objective：

$$
f
$$

才變成：

$$
\arg\min_{x\in D}f(x).
$$

這再次確認：

$$
\boxed{
\text{mathematical query}
\neq
\text{optimization by default}.
}
$$

---

# 25. Causal Query

問：

> 改變 $X$ 是否造成 $Y$？

這需要不同於 correlation query 的 evidence contract。

可能需要：

- intervention；
- causal model；
- experiment；
- identification theorem。

---

# 26. Identity Query

問：

$$
x
\stackrel{?}{\equiv}_{\mathfrak I}
y.
$$

核心不是「看起來像不像」，而是 identity specification。

---

# 27. Translation Query

問：

> presentation $P$ 的 structure 是否能 faithful 轉到 $Q$？

需要 MWT-01 fidelity / loss contract。

---

# 28. Simulation Query

問：

> 在 model $M$ 與 initial state $x_0$ 下會發生什麼？

其答案是：

$$
\boxed{
\text{model-relative trajectory}
}
$$

不是 World 必然未來。

---

# 29. Discovery Query

例如：

> 找到符合某種尚未命名結構的理論／對象。

直接連接 GIPSS：

$$
\boxed{
\text{intent profile}
+
\text{divergent search}
+
\text{evidence reconstruction}.
}
$$

---

# 30. Meta Query

問：

- 這個問題是否 well-posed？
- 哪些 assumptions 缺失？
- 什麼證據才能回答？
- 需要新增哪個 presentation？

這對 MWT 非常重要，因為有些 query 的正確第一步是修改 query。

---

# 31. Query Well-Posedness

定義：

$$
\boxed{
\mathsf{WellPosed}_{\mathrm{MWT}}(\mathfrak Q)
}
$$

最低要求：

- scope 足夠；
- answer type 明確；
- identity 足夠；
- evidence burden 可描述；
- terms 可定位。

不要求 Hadamard 意義的數學適定性。

這是 query-contract completeness。

---

# 32. Query Ambiguity

如果一個 surface query 可以編譯成：

$$
\mathfrak Q_1,\ldots,\mathfrak Q_n,
$$

且不同 contracts 導致不同 answer，

則：

$$
\boxed{
\mathsf{QueryAmbiguous}.
}
$$

AI 應保存 branches，而不是私自挑一個。

---

# 33. Query Refinement

若原 query：

$$
\mathfrak Q
$$

過粗，可以：

$$
\boxed{
\mathfrak Q
\rightsquigarrow
\{
\mathfrak Q_1,\ldots,\mathfrak Q_n
\}.
}
$$

這是 MWT-05 的 inquiry refinement。

---

# 34. Obligation

定義：

$$
\boxed{
o
=
(
\tau,
\phi,
D,
\mathrm{pre},
\mathrm{post},
\mathcal E,
\mathcal V,
B
).
}
$$

其中 $\tau$ 是 obligation type。

---

# 35. Obligation Type Family

$$
\boxed{
\mathcal T_O
=
\{
O_P,
O_C,
O_R,
O_S,
O_O,
O_F,
O_T,
O_X,
O_K,
O_V,
O_H
\}.
}
$$

對應：

- Proof；
- Compute；
- Retrieve；
- Simulate；
- Observe；
- Formalize；
- Translate；
- Counterexample；
- Couple；
- Verify / Certify；
- Human judgment。

---

# 36. Proof Obligation

$$
O_P
$$

要求：

$$
T\vdash\phi.
$$

輸出必須有 proof certificate 或明確 fail/unknown。

---

# 37. Computation Obligation

$$
O_C
$$

要求：

- evaluate；
- solve；
- enumerate；
- optimize；
- bound。

結果要有：

- algorithm；
- precision；
- reproducibility；
- error / certificate。

---

# 38. Retrieval Obligation

$$
O_R
$$

要求從：

- theorem library；
- paper corpus；
- database；
- external source；

取得現有知識。

retrieval result 是 source claim，不是自動 theorem。


# 39. Simulation Obligation

$$
O_S
$$

要求：

$$
\operatorname{Simulate}
(
M,x_0,\Gamma
).
$$

必須保留：

- model；
- initialization；
- parameter；
- stochastic seed；
- solver；
- resolution。

---

# 40. Observation Obligation

$$
O_O
$$

要求：

- measurement；
- experiment；
- sensor；
- external-world check；
- human observation。

它與 simulation evidence 不同。

---

# 41. Formalization Obligation

$$
O_F
$$

把：

- informal theorem；
- natural-language definition；
- computational claim；

翻譯成 formal target。

形式化本身需要 fidelity audit。

---

# 42. Translation Obligation

$$
O_T
$$

建立：

$$
P_i
\to
P_j
$$

的 bridge。

可能是 answer plan 的必要中介。

---

# 43. Counterexample Obligation

$$
O_X
$$

搜索：

$$
x
$$

使：

$$
\neg P(x).
$$

對 universal query 特別高價值。

---

# 44. Coupling Obligation

$$
O_K
$$

表示 query 不能由單一 participant 回答。

需要：

$$
\boxed{
\mathsf{WSolve}_{\Omega}
}
$$

接 MWT-06。

---

# 45. Verification Obligation

$$
O_V
$$

不是產生答案，而是檢查：

- proof；
- computation；
- bridge；
- data；
- claim。

它可以由獨立 verifier 執行。

---

# 46. Human Obligation

$$
O_H
$$

只在：

- semantic ambiguity；
- governance；
- value choice；
- high-risk exception；

需要。

人類不是每個 query 的 mandatory node。

---

# 47. Obligation Hypergraph

定義：

$$
\boxed{
\mathcal G_{\mathfrak Q}^{O}
=
(
\mathcal O_{\mathfrak Q},
E_{\mathrm{dep}},
E_{\mathrm{alt}},
E_{\mathrm{join}},
E_{\mathrm{refute}}
).
}
$$

不同 edge：

### Dependency

$$
o_i
\to_{\mathrm{dep}}
o_j.
$$

### Alternative

$$
o_i
\leftrightarrow_{\mathrm{alt}}
o_j
$$

表示任一路徑成功即可。

### Join

多個 obligations 必須共同滿足：

$$
\{
o_1,\ldots,o_k
\}
\to_{\mathrm{join}}
o.
$$

### Refutation

$$
o_x
\to_{\mathrm{refute}}
o_p
$$

表示 counterexample 可以直接關閉 proof-positive branch。

---

# 48. Query Plan 不是一條固定 List

因為：

- alternative；
- branch；
- counterexample；
- proof failure；
- new evidence；

會改 plan。

所以：

$$
\boxed{
\text{Query Plan}
=
\text{dynamic obligation graph}.
}
$$

---

# 49. Mandatory Obligation

對 query：

$$
\mathfrak Q,
$$

定義：

$$
\boxed{
\operatorname{Mandatory}_{\mathfrak Q}(o).
}
$$

完成 query 只要求所有仍活躍的 mandatory obligations satisfied / validly closed。

---

# 50. Optional Obligation

例如：

- 額外第二種 proof；
- 更多 numerical evidence；
- richer explanation。

可以提高 maturity，但不是 answer completeness 的最低門檻。

---

# 51. Alternative Proof Paths

一個 theorem：

$$
\phi
$$

可以有：

$$
o_{P,1},
o_{P,2},
o_{P,3}
$$

不同 proof strategy。

如果 answer contract 只要求一個 valid proof，任何一支成功即可。

其他分支可停止或留作 independent verification。

---

# 52. Positive / Negative Asymmetry

對 existential query：

$$
\exists x:P(x),
$$

positive：

$$
\boxed{
\text{one witness sufficient}.
}
$$

negative：

$$
\boxed{
\text{requires coverage / impossibility}.
}
$$

對 universal query：

$$
\forall x:P(x),
$$

則反過來：

negative 可由一個 counterexample 完成；

positive 需要 universal burden。

---

# 53. Quantifier-Aware Query Compilation

Query Compiler 應先讀取：

$$
\exists,\forall,\exists!,\sup,\inf,\arg\min
$$

等量詞／answer structure。

因為這直接決定 obligations。

---

# 54. Finite-Domain Exhaustive Proof

若：

$$
|D|<\infty
$$

且完整 enumerate：

$$
\forall x\in D,
$$

並有 coverage certificate，

計算可以形成有限域 universal proof。

因此：

$$
\boxed{
\text{computation can become proof under explicit finite completeness conditions}.
}
$$

---

# 55. Infinite-Domain Sampling Is Not Universal Proof

若：

$$
|D|=\infty
$$

只測：

$$
x_1,\ldots,x_n,
$$

即使全部成立：

$$
P(x_i)=1,
$$

也不能直接推出：

$$
\forall x\in D,P(x).
$$

這是 proof/computation federation 必須永久保留的邊界。

---

# 56. Counterexample Has Asymmetric Power

如果：

$$
x^\star
$$

滿足：

$$
\neg P(x^\star),
$$

則 universal claim：

$$
\forall x,P(x)
$$

被直接 refute。

所以 MWT Query Planner 應在某些 universal problem 同時啟動：

$$
\boxed{
\text{proof search}
\parallel
\text{counterexample search}.
}
$$

---

# 57. Proof/Computation Federation

定義：

$$
\boxed{
\mathfrak F_{\mathrm{PC}}
=
(
\mathcal P_{\mathrm{proof}},
\mathcal P_{\mathrm{comp}},
\mathcal P_{\mathrm{sim}},
\mathcal P_{\mathrm{retr}},
\mathcal P_{\mathrm{obs}}
).
}
$$

它不是單一 solver。

它是 answer-oriented participant federation。

---

# 58. Proof Participant

proof participant：

$$
\mathfrak P_{\mathrm{proof}}
$$

至少有：

- formal system；
- library version；
- tactic / prover；
- proof certificate；
- trusted kernel。

---

# 59. Informal Reasoner

LLM / human informal reasoning 可以是：

$$
\boxed{
\mathfrak P_{\mathrm{reason}}
}
$$

其主要輸出：

- conjecture；
- plan；
- lemma；
- decomposition；
- analogy；
- proof sketch。

這些是 candidate artifacts。

---

# 60. Verifier

$$
\mathfrak P_{\mathrm{verify}}
$$

把 candidate：

$$
c
$$

轉成：

$$
\boxed{
\mathsf{Accepted},
\mathsf{Rejected},
\mathsf{Unknown}
}
$$

相對 verifier contract。

---

# 61. Planner–Worker–Verifier Pattern

2026 年 OpenProver 類 agentic theorem proving 系統已採：

$$
\boxed{
\text{Planner}
\rightarrow
\text{parallel Workers}
\rightarrow
\text{Lean Verifier}.
}
$$

MWT 將此視為 proof obligation federation 的成熟具體架構之一。

MWT 的 query graph更廣，因為 worker 不只 proof。

---

# 62. Discover–Then–Prove Pattern

某些 theorem statement 不提供 answer。

此時：

$$
\boxed{
\text{discover candidate answer}
\rightarrow
\text{formalize}
\rightarrow
\text{prove}.
}
$$

這與 2026 年 Hard Mode theorem proving 的研究方向一致。

MWT 將「發現答案」與「證明答案」固定為不同 obligations。

---

# 63. Informal–Formal Tandem

研究級數學可以先由 informal system 搜索：

$$
\pi_{\mathrm{informal}},
$$

再由 formal system建立：

$$
C_{\mathrm{formal}}.
$$

如果 formalization 失敗，不表示 informal insight 一定錯。

可能是：

- library gap；
- formalization gap；
- hidden assumption；
- actual error。

所以 failure 進 diagnosis。

---

# 64. Proof Search Failure

如果：

$$
\mathsf{ProofSearchFailed},
$$

不能推出：

$$
\neg\phi.
$$

除非 prover / logic 對該 domain 有 completeness certificate。

---

# 65. Computation Participant

$$
\mathfrak P_{\mathrm{comp}}
$$

可以是：

- CAS；
- SAT/SMT；
- numerical solver；
- exhaustive enumerator；
- interval arithmetic；
- graph algorithm；
- optimization solver。

---

# 66. Computation Certificate

計算結果至少應保存：

$$
\boxed{
C_{\mathrm{comp}}
=
(
\text{algorithm},
\text{input},
\text{version},
\text{precision},
\text{coverage},
\text{output},
\text{hash}
).
}
$$

---

# 67. Rigorous Numerics

若使用：

- interval arithmetic；
- exact arithmetic；
- formally verified algorithm；

可以讓 numerical obligation 產生更強 certificate。

但 MWT 不把所有浮點計算視為 proof。

---

# 68. Simulation Participant

simulation：

$$
\mathfrak P_{\mathrm{sim}}
$$

回答：

> 在 model $M$ 下發生什麼？

它不直接回答：

> World 必然發生什麼？

---

# 69. Retrieval Participant

$$
\mathfrak P_{\mathrm{retr}}
$$

負責：

- theorem retrieval；
- literature search；
- database query；
- source lookup。

它的 answer 必須帶 source provenance。

---

# 70. Federated Retrieval

不同 sources：

$$
S_1,\ldots,S_n
$$

可能具有不同 query capabilities。

所以：

$$
\boxed{
\text{source selection}
+
\text{query decomposition}
+
\text{interface-aware planning}
}
$$

是必要的。

這與 federated query processing 的成熟問題一致。

---

# 71. FedQPL Interface

FedQPL 提供 heterogeneous RDF federation 的 logical query plan language，並研究 source selection / plan rewriting。

MWT 不把數學 query 化約成 RDF。

它吸收的原則是：

$$
\boxed{
\text{不同來源有不同 interface capabilities，}
\quad
\text{query plan 必須顯式表示}.
}
$$

---

# 72. Adaptive Query Planning

如果 runtime 發現：

- source latency；
- solver fail；
- new theorem；
- unexpected selectivity；

query plan 可以重排。

所以：

$$
\boxed{
\text{plan}
\neq
\text{immutable}.
}
$$

但任何 replan 都需要 history/provenance。

---

# 73. Capability Profile

每 participant：

$$
\mathfrak P_i
$$

暴露：

$$
\boxed{
\operatorname{Cap}(\mathfrak P_i).
}
$$

例如：

```text
prove
refute
enumerate
optimize
simulate
retrieve
formalize
translate
observe
certify
```

以及 domain / cost / maturity。

---

# 74. Capability Router

對 obligation：

$$
o,
$$

router 選：

$$
\boxed{
\operatorname{Route}(o)
\subseteq
\{
\mathfrak P_i
\}.
}
$$

可以一對一，也可以 ensemble。

---

# 75. Routing Is Typed

不能把：

$$
O_{\mathrm{proof}}
$$

直接送給只有：

$$
\operatorname{Cap}=\{\mathsf{simulate}\}
$$

的 participant。

除非先把 obligation 改成 simulation sub-obligation。

---

# 76. Capability Does Not Equal Suitability

兩個 prover 都能 proof，

但：

- domain library；
- cost；
- reliability；

不同。

所以 routing 還需要：

$$
\boxed{
\mathsf{Suitability}
(
\mathfrak P_i,o,\Gamma
).
}
$$

---

# 77. Query Planning Cost

query plan：

$$
\pi_Q
$$

有：

$$
\kappa(\pi_Q)
$$

包括：

- compute；
- source；
- proof；
- formalization；
- communication；
- human cost。

planner 可做 Pareto selection。

---

# 78. Minimal Plan 不是唯一目標

最便宜 plan：

$$
\pi_{\min}
$$

可能 evidence 太弱。

高風險 query 可能選：

$$
\boxed{
\text{redundant independent verification}.
}
$$

---

# 79. Proof Ensemble

對重要 theorem，可以：

- Lean；
- Coq；
- second Lean formalization；
- independent proof；
- computational checks；

形成：

$$
\boxed{
\mathcal E_{\mathrm{proof}}.
}
$$

不同 verifier 的同意提高 maturity。

---

# 80. Shared-Kernel Correlation

兩個 agent 都用同一 proof kernel，

不算完全 independent。

所以 evidence ledger 要記：

- model；
- prover；
- kernel；
- library；
- source code lineage。

---

# 81. Counterexample Engine

$$
\boxed{
\mathsf{CXE}
}
$$

專門：

- finite search；
- random search；
- adversarial search；
- SAT/SMT；
- numerical search；
- construction。

一個 counterexample 必須再驗證它真的滿足 domain / premise。

---

# 82. False Counterexample

若：

$$
x^\star
$$

其實：

$$
x^\star\notin D,
$$

則不能 refute claim。

所以 counterexample 也要：

$$
\boxed{
C_{\mathrm{domain}}
+
C_{\neg P}.
}
$$

---

# 83. Evidence Ledger

定義：

$$
\boxed{
\mathsf{EL}.
}
$$

對 claim：

$$
c
$$

保存：

$$
\boxed{
E(c)
=
(
E^+,
E^-,
E^{?},
E^{\mathrm{conf}}
).
}
$$

---

# 84. Evidence Type

每條 evidence：

$$
e
$$

帶：

- type；
- source；
- scope；
- maturity；
- version；
- dependency；
- validity horizon。

不能把所有 evidence 直接加權成單一 confidence。

---

# 85. Proof Evidence

如果：

$$
T\vdash\phi,
$$

形成：

$$
e_{\mathrm{proof}}.
$$

其 scope 包含：

$$
T.
$$

foundation index 不能刪。

---

# 86. Counterexample Evidence

如果：

$$
x^\star\in D
$$

且：

$$
\neg P(x^\star),
$$

形成：

$$
e_{\mathrm{cx}}.
$$

它對：

$$
\forall x\in D,P(x)
$$

具有直接 refutation power。

---

# 87. Empirical Evidence

observation：

$$
y
$$

支持 model claim。

它不等於 formal proof。

但對 empirical query，可能是 mandatory answer evidence。

---

# 88. Literature Evidence

paper / database result：

$$
e_{\mathrm{lit}}
$$

要區分：

- original source；
- secondary summary；
- unverified claim；
- retracted / superseded version。

---

# 89. Heuristic Evidence

LLM reasoning：

$$
e_{\mathrm{heur}}
$$

可以：

- raise candidate；
- prioritize plan；
- generate lemma。

不能單獨滿足 high-rigor proof contract。

---

# 90. Claim

定義：

$$
\boxed{
c
=
(
\phi,
D,
\Gamma,
\mathfrak I,
v
).
}
$$

同一句：

$$
\phi
$$

不同 context 是不同 claim record。

---

# 91. Query Answer Bundle

定義：

$$
\boxed{
\mathfrak A_{\mathfrak Q}
=
(
\mathcal C^+,
\mathcal C^-,
\mathcal U,
\mathcal X,
\mathcal P,
\mathcal H,
\Sigma
).
}
$$

---

# 92. Positive Claims

$$
\mathcal C^+
$$

是目前被 support / prove 的 claims。

必須帶 scope。

---

# 93. Negative Claims

$$
\mathcal C^-
$$

是被 refute / disproved 的 claims。

它不是缺乏 positive evidence。

---

# 94. Unresolved

$$
\mathcal U
$$

包含：

- open proof；
- incomplete search；
- unknown bridge；
- budget exhausted。

---

# 95. Conflict

$$
\mathcal X
$$

保存：

- different foundations；
- source disagreement；
- proof-verifier conflict；
- semantic ambiguity。

---

# 96. Provenance

$$
\mathcal P
$$

連到：

- source；
- solver；
- presentation；
- versions；
- certificate roots。

---

# 97. Query History

$$
\mathcal H
$$

保存：

- decompositions；
- routes；
- failed branches；
- replans；
- counterexamples；
- proof attempts。

這使 answer 可 audit。

---

# 98. Completion Certificate

$$
\boxed{
\Sigma
}
$$

回答：

> 為什麼現在可以停止？

它不是 truth certificate。

它是 query completion / coverage certificate。

---

# 99. Query Completion

定義：

$$
\boxed{
\operatorname{Complete}(\mathfrak Q)=1
}
$$

若所有 mandatory answer obligations：

- satisfied；
- validly refuted；
- validly superseded；
- or answer contract allows explicit Unknown。

---

# 100. Unknown Can Be a Complete Answer

如果 answer contract：

> 判定目前是否能確定。

那：

$$
\boxed{
\mathsf{Undetermined}
}
$$

本身可以是完整回答，

只要 uncertainty reason / coverage 完整。

---

# 101. Budget-Exhausted Is Usually Not Complete

如果 query 原本要求 proof，

但只是：

$$
B_{\mathrm{proof}}
$$

耗盡，

不能把：

$$
\mathsf{NoProofFound}
$$

當完整 No。

---

# 102. Coverage Certificate

對 search query：

$$
\boxed{
C_{\mathrm{cov}}
=
(
D_{\mathrm{searched}},
S_{\mathrm{sources}},
\Pi_{\mathrm{plan}},
B,
\mathrm{known\ gaps}
).
}
$$

---

# 103. Not Found vs Does Not Exist

固定：

$$
\boxed{
\neg\operatorname{Found}(x\mid C_{\mathrm{cov}})
\not\Rightarrow
\neg\operatorname{Exists}(x).
}
$$

除非：

$$
C_{\mathrm{cov}}
$$

對 required universe 完備，或另有 impossibility proof。

---

# 104. GIPSS Integration

GIPSS 的：

- 欲；
- DRC；
- SGCD；

可以成為 discovery query backend。

MWT-07 將：

$$
I
$$

編譯給 GIPSS，

由 DRC 控制：

$$
\mathsf{Diverge}
\to
\mathsf{Resonate}
\to
\mathsf{Compress}.
$$

結果回到 evidence ledger。

---

# 105. Search Is World Inference

在 MWT 裡，retrieval 不只是「找文件」。

它可以改：

- entity identity；
- presentation registry；
- stable claim；
- query plan；
- world-state。

所以：

$$
\boxed{
\text{retrieval}
\subset
\text{world inference}.
}
$$

---

# 106. World Inference Graph

定義：

$$
\boxed{
\mathcal G_{\mathfrak Q}^{W}
}
$$

將：

- obligations；
- participants；
- evidence；
- claims；
- presentations；
- branches；

放入同一 inquiry graph。

---

# 107. Inference Edge Types

至少：

$$
\boxed{
E^W
=
\{
E_{\mathrm{derive}},
E_{\mathrm{support}},
E_{\mathrm{refute}},
E_{\mathrm{translate}},
E_{\mathrm{compute}},
E_{\mathrm{observe}},
E_{\mathrm{couple}},
E_{\mathrm{depend}}
\}.
}
$$

---

# 108. Inference Path

一條 answer path：

$$
\pi
$$

可能：

$$
q
\to
\text{retrieve theorem}
\to
\text{formalize}
\to
\text{prove}
\to
\text{certify}.
$$

另一條：

$$
q
\to
\text{generate candidate}
\to
\text{compute}
\to
\text{find counterexample}.
$$

兩條可並行。


# 109. Inference Order May Be Noncommutative

若先做：

$$
O_{\mathrm{formalize}}
$$

再做：

$$
O_{\mathrm{retrieve}},
$$

與先 retrieve 現有 formal theorem 再 formalize query，

可能得到不同 obligations。

因此 query planning 本身也是 MWT-03 scheduler problem。

---

# 110. Plan Noncommutativity

可以存在：

$$
R\circ F
\neq
F\circ R,
$$

其中：

- $R$：retrieval；
- $F$：formalization。

這不是 implementation trivia。

可能直接改變：

- query scope；
- theorem statement；
- available proof library；
- proof burden。

---

# 111. Replanning Trigger

以下事件可以：

$$
\boxed{
\operatorname{Replan}(\mathfrak Q).
}
$$

1. proof branch fails；
2. counterexample found；
3. new source discovered；
4. bridge fails；
5. query ambiguity exposed；
6. budget changes；
7. new presentation admitted；
8. solver unavailable；
9. conflict localized；
10. answer contract refined。

---

# 112. Replanning 不得抹掉舊 Plan

每次：

$$
\pi_Q^{(v)}
\to
\pi_Q^{(v+1)}
$$

要保存：

- why changed；
- obligations closed；
- obligations added；
- evidence retained；
- branch retired。

---

# 113. Query State

定義：

$$
\boxed{
\mathfrak S_{\mathfrak Q,t}
=
(
\mathfrak Q,
\mathcal G_{\mathfrak Q}^{O},
\mathcal G_{\mathfrak Q}^{W},
\mathfrak A_{\mathfrak Q},
B_t,
v_t
).
}
$$

query 自己也是一個 dynamic state system。

---

# 114. Query Dynamic Fixed Point

當：

- mandatory obligations closed；
- answer bundle stable；
- no mandatory replan；
- completion certificate exists；

則：

$$
\boxed{
\operatorname{QDFP}
(
\mathfrak S_{\mathfrak Q}
)
=1.
}
$$

這是 query-level temporary closure。

---

# 115. Query Reopen

新 evidence：

$$
e
$$

可以：

$$
\boxed{
\operatorname{ReopenQuery}
(
\mathfrak Q,e
).
}
$$

例如：

- theorem retracted；
- counterexample；
- software bug；
- new data；
- new foundation；
- user asks stronger question。

---

# 116. Query Answer Is Versioned

answer：

$$
\mathfrak A_{\mathfrak Q}^{(v)}
$$

必須帶：

- world-state version；
- source versions；
- proof library；
- solver；
- query contract version。

因此未來可以比較：

$$
\mathfrak A^{(v)}
\rightsquigarrow
\mathfrak A^{(v+1)}.
$$

---

# 117. Contradictory Answers May Be Context-Split

若：

$$
T_1\vdash\phi
$$

但：

$$
T_2\vdash\neg\phi,
$$

不能刪：

$$
T_1,T_2.
$$

正確 answer 可以是：

$$
\boxed{
\begin{cases}
\phi & \text{under }T_1,\\
\neg\phi & \text{under }T_2.
\end{cases}
}
$$

這是 context-indexed structured answer。

---

# 118. Answer Homogenization Is Forbidden

不同 evidence types 不應全部被壓成：

$$
0.87
$$

再說：

> 87% 真。

除非 query contract 明確定義 probabilistic belief model。

形式 proof、empirical support、search failure 與 simulation 不是天然可加權同質量。

---

# 119. Claim Maturity

v0.1 建議：

### A0 — Candidate

LLM / heuristic proposal。

### A1 — Supported

有非形式 evidence。

### A2 — Reproducible

計算 / search 可重放。

### A3 — Certified Local

在指定 presentation / formal system 有 certificate。

### A4 — Cross-Verified

跨 implementation / presentation 驗證。

### A5 — Stable Query Answer

已進當前 World-State Stable Core。

maturity 不等於 truth probability。

---

# 120. Proof Maturity Is Not Search Coverage

一個 theorem formal proof：

$$
T\vdash\phi
$$

可以是高 proof maturity。

但若 query 問：

> 世界上是否存在某篇相關論文？

這個 proof 對 retrieval coverage 沒有直接意義。

所以 maturity 也是 obligation-type relative。

---

# 121. Query Confidence

若產品/UI 需要 confidence score，

必須由：

$$
\boxed{
\operatorname{Conf}
(
c\mid
\text{evidence model}
)
}
$$

顯式定義。

MWT 核心不自動提供 universal scalar confidence。

---

# 122. Query Plan Coverage

planner 應輸出：

$$
\boxed{
\operatorname{Coverage}(\pi_Q)
}
$$

至少描述：

- mandatory obligations covered；
- alternative branches explored；
- sources queried；
- search limits；
- unexplored branches。

---

# 123. Coverage Unknown

如果 planner 不知道還有哪些可能 strategy：

$$
\boxed{
\mathsf{CoverageUnknown}.
}
$$

這是正常狀態。

不能偽造：

> 已搜索所有可能數學方法。

---

# 124. Global Query 不等於 Global Exhaustion

MWT 的 global query 表示：

> 問題可跨整個 active world registry 路由。

不表示：

> 每次都遍歷所有數學、所有論文、所有 proof、所有 solver。

所以：

$$
\boxed{
\text{global addressability}
\neq
\text{global exhaustive execution}.
}
$$

---

# 125. Source Selection

query planner 對：

$$
O_R
$$

先選：

$$
S_{\mathrm{cand}}.
$$

source selection 可以依：

- relevance；
- authority；
- capability；
- freshness；
- cost；
- access。

---

# 126. Solver Selection

對：

$$
O_C,
O_P,
O_S,
$$

選：

$$
\mathfrak P_i.
$$

solver selection 也不是永久固定。

runtime 結果可觸發 replacement。

---

# 127. Theorem Retrieval as Planning Accelerator

proof system 可以先搜尋：

$$
\mathcal L_{\mathrm{theorem}}
$$

取得 candidate lemmas。

這能減少 proof search。

但 retrieved theorem 必須：

- type compatible；
- assumptions compatible；
- library version valid。

---

# 128. Cross-Domain Theorem Retrieval

如果 query 在 domain $D_1$，

retrieval 發現：

$$
T:D_2\to D_1
$$

的 bridge theorem，

可以生成新的 translation obligation。

所以 theorem retrieval 不只補 lemma，也可以改 presentation graph。

---

# 129. Formalization as Discovery

將 informal statement formalize 時，可能發現：

- hidden quantifier；
- missing domain；
- ambiguous identity；
- inconsistent assumptions。

因此：

$$
\boxed{
\text{formalization}
}
$$

本身可以是 query refinement。

---

# 130. Verification Failure as Information

若 Lean / Coq / verifier 拒絕 candidate proof，

可能原因：

1. proof wrong；
2. formalization wrong；
3. missing lemma；
4. library mismatch；
5. type mismatch；
6. kernel/tool issue。

所以：

$$
\boxed{
\text{verification failure}
\neq
\text{theorem false}.
}
$$

---

# 131. Cross-Formal-System Federation

同一 theorem 可以在：

$$
T_1,T_2
$$

分別 formalize。

若有 bridge：

$$
F:T_1\to T_2,
$$

可以驗證：

$$
F(\phi_1)
\equiv
\phi_2.
$$

這提高 translation / identity maturity。

---

# 132. Proof–Computation Feedback

計算可以：

- 找 lemma pattern；
- 猜 bound；
- 找 counterexample；
- 驗證 finite cases。

proof 又可以：

- certify algorithm；
- prove termination；
- prove error bound；
- 縮小 search domain。

因此：

$$
\boxed{
\text{proof}
\leftrightarrow
\text{computation}.
}
$$

---

# 133. Search–Proof Feedback

literature retrieval 找到 theorem：

$$
T,
$$

proof system檢查是否真的 applicable。

proof failure 又可回到 retrieval：

> 找更弱/更強版本。

所以：

$$
\boxed{
\text{retrieve}
\leftrightarrow
\text{prove}.
}
$$

---

# 134. Simulation–Proof Feedback

simulation 發現 invariant candidate：

$$
I.
$$

proof system嘗試證明：

$$
I.
$$

若 proof 失敗，可搜索 counterexample。

這形成：

$$
\boxed{
\text{simulate}
\to
\text{conjecture}
\to
\text{prove/refute}.
}
$$

---

# 135. World Inference Loop

綜合：

$$
\boxed{
\begin{aligned}
\mathfrak Q
&\to
\mathcal G^O\\
&\to
\text{route}\\
&\to
\text{retrieve/prove/compute/simulate/observe}\\
&\to
\mathsf{EL}\\
&\to
\mathfrak A_{\mathfrak Q}\\
&\to
\text{replan/refine}\\
&\to
\operatorname{QDFP}.
\end{aligned}
}
$$

---

# 136. Query Compiler

第一個 MWT-07 runtime 模組：

$$
\boxed{
\mathsf{QC}.
}
$$

輸入：

$$
q_{\mathrm{surf}}.
$$

輸出：

$$
\mathfrak Q.
$$

---

# 137. Intent / Scope Resolver

第二個模組：

$$
\boxed{
\mathsf{ISR}.
}
$$

解析：

- intent；
- domain；
- quantifier；
- answer type；
- identity；
- risk；
- time scope。

---

# 138. Obligation Graph Builder

第三個模組：

$$
\boxed{
\mathsf{OGB}.
}
$$

建立：

$$
\mathcal G_{\mathfrak Q}^{O}.
$$

---

# 139. Capability Router

第四個模組：

$$
\boxed{
\mathsf{CR}.
}
$$

把 obligation 路由到 participants。

---

# 140. Proof Federation Manager

第五個模組：

$$
\boxed{
\mathsf{PFM}.
}
$$

管理：

- theorem retrieval；
- informal planner；
- formal prover；
- verifier；
- proof ensemble。

---

# 141. Computation Federation Manager

第六個模組：

$$
\boxed{
\mathsf{CFM}.
}
$$

管理：

- symbolic；
- numeric；
- SAT/SMT；
- enumeration；
- optimization；
- simulation。

---

# 142. Evidence Ledger

第七個模組：

$$
\boxed{
\mathsf{EL}.
}
$$

已於前文定義。

---

# 143. Counterexample Engine

第八個模組：

$$
\boxed{
\mathsf{CXE}.
}
$$

負責 adversarial negative search。

---

# 144. Coverage Engine

第九個模組：

$$
\boxed{
\mathsf{CovE}.
}
$$

管理：

- source coverage；
- finite enumeration completeness；
- query-plan coverage；
- unexplored branches。

---

# 145. Answer Synthesizer

第十個模組：

$$
\boxed{
\mathsf{AS}.
}
$$

將 heterogeneous evidence：

$$
\mathsf{EL}
$$

轉成：

$$
\mathfrak A_{\mathfrak Q}.
$$

它不得自行把不同 evidence types 混成未定義 scalar。

---

# 146. Query Reopen Engine

第十一個模組：

$$
\boxed{
\mathsf{QRE}.
}
$$

監控：

- new evidence；
- version；
- counterexample；
- source update；
- stronger inquiry。

---

# 147. Reference Query Compiler

本 Source Pack 附帶：

```text
mwt07_query_reference.py
```

它只固定最低 v0.1 semantics：

1. query class；
2. quantifier-aware obligation generation；
3. capability routing；
4. mandatory / optional obligation；
5. completion判定；
6. `Not Found != Does Not Exist` 的 negative-search guard。

它不是 natural-language semantic parser，也不是 universal theorem planner。

---

# 148. Example：Universal Claim

query：

$$
\forall x\in D,P(x)?
$$

compiler 建立：

- $O_P$：proof；
- $O_X$：counterexample；
- $O_C$：finite/symbolic checks optional。

若 counterexample success：

$$
O_X
\to
\mathsf{CompleteNo}.
$$

若 sampled computation success：

仍然不能：

$$
\mathsf{CompleteYes}.
$$

---

# 149. Example：Existence Search

query：

$$
\exists x\in D,P(x)?
$$

compiler 建立：

- retrieval/search；
- construction；
- counterexample-to-nonexistence 不適用；
- coverage track。

找到 witness：

$$
\boxed{
\mathsf{CompleteYes}.
}
$$

沒找到：

$$
\boxed{
\mathsf{NotFoundUnderCoverage}.
}
$$

除非有 exhaustive / impossibility certificate。

---

# 150. Example：Research-Level Theorem

對一個未形式化 conjecture：

1. formalize statement；
2. retrieve nearby theorem；
3. informal reasoning；
4. counterexample search；
5. formal proof；
6. independent verification。

這些可並行部分執行。

---

# 151. Example：Cross-Presentation Identity

問：

> 這兩個構造是不是同一個？

需要：

- identity specification；
- translation；
- invariant comparison；
- maybe proof；
- maybe counterexample。

若 $\mathfrak I$ 不明：

第一個 mandatory obligation 是：

$$
O_H/O_F:
\text{resolve identity contract}.
$$

---

# 152. Example：World Model Prediction

問：

> 明天系統會怎樣？

如果沒有足夠 deterministic law，

answer contract 應變成：

- model-relative scenarios；
- probability；
- uncertainty；
- assumptions。

不能偷換成 theorem query。

---

# 153. MWT-07 Minimal Constitution

v0.1 固定二十七條：

### Q1 — Query Is Not a String

surface form 不等於 inquiry contract。

### Q2 — Intent Must Be Represented

query 必須有 answer-directed intent。

### Q3 — Scope Must Be Explicit

domain / assumptions / version 不得被無聲省略。

### Q4 — Answer Type Determines Burden

witness、proof、estimate、classification 不可混同。

### Q5 — Identity Is Query-Indexed

「同一」必須帶 identity specification。

### Q6 — Evidence Is Typed

proof、computation、simulation、observation、retrieval 不得默認等價。

### Q7 — Validation Is Separate from Generation

candidate generation 不等於 verification。

### Q8 — Query Decomposes into Obligations

複雜 query 不預設單一 solver call。

### Q9 — Obligations Form a Graph

dependencies / alternatives / refutations 必須可表示。

### Q10 — Quantifiers Control Evidence Burden

 $\exists$ 與 $\forall$ 的正反責任不對稱。

### Q11 — Not Found Is Not Nonexistence

有限 search failure 不能直接推出 existential negative。

### Q12 — Proof Search Failure Is Not Refutation

除非 completeness 明示。

### Q13 — Simulation Is Model-Relative

simulation output 不是 World 必然真值。

### Q14 — Computation Can Be Proof Only Under Explicit Completeness Conditions

例如 finite exhaustive certified search。

### Q15 — Counterexamples Require Domain Certificates

假的 counterexample 不得 refute theorem。

### Q16 — Routing Is Capability-Aware

不同 participants 不假設同能力。

### Q17 — Planning Is Reopenable

runtime evidence 可改 query plan。

### Q18 — Planning Order May Be Noncommutative

query operations 可產生順序效應。

### Q19 — Coverage Must Be Reported

停止 search 要說明搜了什麼。

### Q20 — Coverage Unknown Is Allowed

不能偽裝全域完備搜尋。

### Q21 — Answers Are Structured Bundles

Yes/No 只是某些 query 的投影。

### Q22 — Conflict Is Preserved by Context

不同 foundation / source 衝突不可靜默平均。

### Q23 — Answer Maturity Is Not Probability

形式化成熟度與信念分數分離。

### Q24 — Query Completion Is Scoped

完成是相對 answer contract。

### Q25 — Unknown Can Be a Complete Answer

如果 contract 要求判定可知性。

### Q26 — New Evidence Can Reopen an Answer

query answer 不是永久封印。

### Q27 — Query Execution Returns to World State

重要新 evidence / theorem / bridge 應能更新 MWT-04 world state。

---

# 154. 命題：Existential Positive Requires No Global Coverage

對：

$$
\mathfrak Q:
\exists x\in D,P(x),
$$

若找到：

$$
x^\star\in D
$$

且：

$$
P(x^\star)
$$

有有效 certificate，

則 positive answer 已完成。

不需要遍歷整個 $D$。

---

# 155. 命題：Existential Negative Needs Additional Burden

同一 query 若只得到：

$$
\neg\operatorname{Found}
(
x
\mid
S,B
),
$$

由 Q11 不能推出：

$$
\neg\exists x\in D,P(x).
$$

需要額外 completeness / impossibility certificate。

---

# 156. 命題：Universal Negative Is Witness-Complete

對：

$$
\forall x\in D,P(x),
$$

若找到：

$$
x^\star\in D
$$

且：

$$
\neg P(x^\star),
$$

則 universal claim 被 refute。

---

# 157. 命題：Formal Proof Is Foundation-Indexed

若：

$$
T\vdash\phi,
$$

則可輸出：

$$
\boxed{
\mathsf{Proved}
(
\phi\mid T
).
}
$$

不能刪除 $T$ index 後自動宣稱：

$$
\mathsf{WorldTrue}(\phi).
$$

---

# 158. 命題：Query Replanning Does Not Invalidate Retained Evidence

若 plan：

$$
\pi_1
\to
\pi_2
$$

而某 evidence：

$$
e
$$

仍滿足新 plan scope / version，

則 $e$ 可以被 retained。

replan 不要求全部從頭開始。

---

# 159. 條件定理：Certified Query Completion

若：

1. Inquiry Contract well-posed；
2. 所有 mandatory obligations 有完成證書、valid refutation 或 contract-allowed unknown；
3. 所有 claim scope / identity / version 明示；
4. coverage obligations 滿足；
5. no unreported hard conflict；
6. Answer Bundle 與 provenance 完整；

則：

$$
\boxed{
\operatorname{Complete}(\mathfrak Q)=1.
}
$$

由本文 query-completion definition 成立。

---

# 160. 條件定理：Finite Exhaustive Universal Certification

若：

1. $D$ 有有限完整 enumeration：
   $$
   D=\{x_1,\ldots,x_n\};
   $$
2. enumeration completeness 有 certificate；
3. 對每個 $x_i$， $P(x_i)$ 有 valid certificate；

則：

$$
\boxed{
\forall x\in D,P(x)
}
$$

可由 finite exhaustive computation certification 得到。

---

# 161. 研究猜想：Query-Native Mathematics

未來 AI-native mathematics 的核心入口可能不再是：

> 選一個 theorem prover / solver。

而是：

$$
\boxed{
\text{compile inquiry contract}
\rightarrow
\text{generate obligation graph}
\rightarrow
\text{federate methods}.
}
$$

---

# 162. 研究猜想：Proof/Computation Complementarity

對部分 research problems，proof search 與 counterexample / numerical search 並行可能比單獨任一路線更有效，因為兩者互相縮小 search space、產生 lemma 與 falsify weak conjectures。

---

# 163. 研究猜想：Persistent Query Residual as Discovery Signal

如果一個 query 在多 presentation、solver、proof / search route 下長期留下同一 unresolved obligation，該 residual 可能指向：

- missing definition；
- missing invariant；
- missing dimension；
- genuinely hard boundary。

---

# 164. 研究猜想：World Query Planner as AGI Mathematics Interface

當 AI 能從高層 query 自動生成可靠 obligation graph，並將 proof、computation、retrieval、simulation、observer 與 coupling participant 自動聯邦時，數學使用介面可能從「人類選方法」逐步變成「人類定義問題與驗證標準」。

---

# 165. 開放問題

### O1 — Intent Compilation

自然語言 intent 如何無損轉成 Inquiry Contract？

### O2 — Obligation Completeness

如何知道 planner 沒漏掉 mandatory obligation？

### O3 — Plan Search Complexity

最佳 obligation graph 是否本身難解？

### O4 — Proof/Computation Evidence Algebra

不同證據如何組成，而不做錯誤數值化？

### O5 — Query Coverage

無限 source / strategy space 下如何表示 coverage？

### O6 — Automated Identity Resolution

query 中的「同一」如何由 AI 安全推定？

### O7 — Cross-Foundation Query Answer

多 formal systems 給出不同結果時，最佳 answer representation 是什麼？

### O8 — Query Reopen Minimality

新 evidence 到來後如何只重算受影響 obligations？

### O9 — Human Query Governance

哪些 query contract 必須由人類定義？

### O10 — Query-to-Refinement

persistent query failure 何時應觸發 MWT-05 新 dimension / presentation？

---

# 166. 外部研究接口：Agentic Formal Theorem Proving

2026 年 OpenProver 展示：

- Planner；
- Workers；
- Lean 4 verifier；
- persistent repository；

可形成 agentic formal proof workflow。

MWT 將這種架構視為 Proof Federation Manager 的成熟 backend 類型。

---

# 167. 外部研究接口：Discover and Prove

Hard Mode ATP 顯示：

> 找到答案與形式證明答案是兩個不同任務。

MWT-07 將其一般化成：

$$
\boxed{
O_{\mathrm{discover}}
\neq
O_{\mathrm{prove}}.
}
$$

---

# 168. 外部研究接口：Automated Conjecture Resolution

2026 年 Automated Conjecture Resolution 將 informal reasoning、theorem search 與 formal Lean verification連成研究流程。

這提供：

$$
\boxed{
\text{informal discovery}
+
\text{formal certification}
}
$$

的當代成熟案例。

MWT 再把 numerical、simulation、retrieval、observer 與 coupling obligations 放入同一 query layer。

---

# 169. 外部研究接口：Federated Query Processing

heterogeneous data federation 已長期研究：

- source selection；
- decomposition；
- logical plan；
- interface-aware execution；
- adaptive replanning。

MWT 不把數學世界等同資料庫。

它吸收：

$$
\boxed{
\text{heterogeneous capabilities require explicit query planning}.
}
$$

---

# 170. FedQPL Interface

FedQPL 對 heterogeneous RDF federation 建立 logical query-plan language，並形式研究 source selection 與 rewriting。

MWT 的 Obligation Hypergraph 在精神上更接近：

> 對 heterogeneous mathematical capabilities 建立 explicit world-inference plan。

但 MWT obligations 包括 proof、simulation 與 observation，不只是資料查詢。

---

# 171. 與 GIPSS / DRC / SGCD 的接口

GIPSS v0.2 已有：

$$
\mathcal W_t
\to
\operatorname{DRC}_D
\to
\mathcal Q_t
\to
\operatorname{Retrieve}
\to
\operatorname{SGCD}
\to
\operatorname{GIPSS}
\to
\Delta\Phi_t
\to
\operatorname{DRC}_{R,C}.
$$

MWT-07 將其定位為：

$$
\boxed{
Q_{\mathrm{discover}}
}
$$

的高價值 specialized backend。

---

# 172. 與 MWT-06 的接口

如果 obligation graph 中：

$$
O_K
$$

成立，

Query Planner 建立：

$$
\mathsf{WSolve}_{\Omega}.
$$

World Solve 的 residual / result 回到 Answer Bundle。

---

# 173. 與 MWT-05 的接口

如果 query 無法被 current presentation vocabulary 表達：

$$
\boxed{
\mathsf{QueryFailure}
\rightarrow
\mathsf{RefinementObligation}.
}
$$

可能生成：

- new dimension；
- new presentation；
- new bridge；
- new observer。

---

# 174. 與 MWT-04 的接口

重要 query answer：

$$
\mathfrak A_{\mathfrak Q}
$$

若達到 Stable Core admission，更新：

$$
K_t.
$$

未解 query 進：

$$
\mathcal U_t.
$$

新 evidence 可進 Reopen Set。

---

# 175. 與 MWT-03 的接口

obligation graph execution順序、parallel proof / search、noncommutative formalization / retrieval 全部交給 NCS。

---

# 176. 與 MWT-02 的接口

每個：

- proof attempt；
- external query；
- simulation；
- computation；
- translation；

都是 interaction，必須有 legality。

---

# 177. 與 MWT-01 的接口

query 的 scope、identity、presentation、translation 與 answer projection都依 Presentation Theory。

因此 MWT-07 沒有新增一個脫離世界的「超級問答器」。

---

# 178. MWT-01～07 的循環

目前可以寫：

$$
\boxed{
\begin{aligned}
\text{Present}
&\rightarrow
\text{Judge}\\
&\rightarrow
\text{Schedule}\\
&\rightarrow
\text{World-State}\\
&\rightarrow
\text{Refine}\\
&\rightarrow
\text{Couple / Solve}\\
&\rightarrow
\text{Query / Infer}\\
&\rightarrow
\text{Answer}\\
&\rightarrow
\text{Update / Reopen}.
\end{aligned}
}
$$

---

# 179. 下一篇接口

下一篇最自然的是：

# **MWT-08：Global Quantification, Coverage, and Universal Proof Obligations**

因為 MWT-07 已經知道如何問問題。

下一個最危險的地方就是：

$$
\boxed{
\forall
}
$$

與：

$$
\boxed{
\text{global}.
}
$$

MWT-08 將正式處理：

- universal quantifier；
- finite / infinite coverage；
- global proof；
- exhaustive certificate；
- local-to-global lift；
- counterexample completeness；
- approximation；
- quantifier compression；
- 「驗證很多」何時真的能變成「對所有」。

也就是替 MWT 的「全域」補上真正的量詞責任。

---

# 180. 一句話版

> **MWT-07 將 query 從字串提升為 Inquiry Contract，明示 intent、scope、answer type、identity、evidence、validation、version、risk 與 budget，並將複雜問題編譯成帶 dependency、alternative、join 與 refutation edges 的 obligation hypergraph。Proof、computation、retrieval、simulation、observation、formalization、translation、counterexample 與 coupling 各自保留不同證據地位，由 capability-aware federation 並行執行與交叉驗證。系統不再把「沒有找到」偷換成「不存在」、不把 proof search failure 偷換成 refutation，也不把 simulation 或 LLM reasoning 偷換成 theorem；真正的回答是一個帶正反 claims、unknown、conflict、provenance、history 與 coverage certificate 的結構化 Answer Bundle。**

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $q_{\mathrm{surf}}$ | query surface |
| $\mathfrak Q$ | Inquiry Contract |
| $I$ | query intent |
| $D$ | query scope |
| $A$ | answer contract |
| $\mathfrak I$ | identity specification |
| $\mathcal E$ | evidence requirement |
| $\mathcal V$ | validation requirement |
| $\mathcal T$ | time/version scope |
| $\mathcal R$ | risk profile |
| $B$ | budget |
| $\mathcal G_{\mathfrak Q}^{O}$ | Obligation Hypergraph |
| $O_P$ | proof obligation |
| $O_C$ | computation obligation |
| $O_R$ | retrieval obligation |
| $O_S$ | simulation obligation |
| $O_O$ | observation obligation |
| $O_F$ | formalization obligation |
| $O_T$ | translation obligation |
| $O_X$ | counterexample obligation |
| $O_K$ | coupling obligation |
| $O_V$ | verification obligation |
| $\mathfrak A_{\mathfrak Q}$ | Query Answer Bundle |
| $\mathsf{EL}$ | Evidence Ledger |
| $\Sigma$ | completion / coverage certificate |
| $\mathsf{QC}$ | Query Compiler |
| $\mathsf{ISR}$ | Intent/Scope Resolver |
| $\mathsf{OGB}$ | Obligation Graph Builder |
| $\mathsf{CR}$ | Capability Router |
| $\mathsf{PFM}$ | Proof Federation Manager |
| $\mathsf{CFM}$ | Computation Federation Manager |
| $\mathsf{CXE}$ | Counterexample Engine |
| $\mathsf{CovE}$ | Coverage Engine |
| $\mathsf{AS}$ | Answer Synthesizer |
| $\mathsf{QRE}$ | Query Reopen Engine |

---

# 附錄 B：v0.1 非主張清單

MWT-07 不主張：

1. 每個自然語言 query 都能無歧義形式化；
2. 每個 query 都存在完備 obligation graph；
3. 所有 proof obligations 可自動解；
4. 所有 query 都需要 formal proof；
5. numerical evidence 等於 proof；
6. simulation 等於現實；
7. retrieval result 等於真理；
8. LLM reasoning 等於 theorem；
9. proof search failure 等於 theorem false；
10. search failure 等於不存在；
11. 所有 source coverage 可精確量化；
12. query planner 可以搜尋所有可能方法；
13. capability router 永遠選到最佳 solver；
14. 多 verifier 同意等於 World truth；
15. 不同 proof assistants 就天然獨立；
16. 所有 evidence 可以壓成單一 confidence；
17. Query Answer Bundle 永遠需要 Yes / No；
18. query completion 等於數學問題永遠完成；
19. answer stable 後不會被新證據 reopen；
20. formalization 不會改變 query；
21. 任何 counterexample candidate 都有效；
22. federated query processing 等於 MWT；
23. agentic theorem prover 等於 MWT；
24. GIPSS 能回答所有 query type；
25. MWT-07 已建立 universal AGI question-answering system；
26. query planning 可繞過 MWT legality；
27. 「global query」表示必須執行全域 exhaustive search。

---

# 附錄 C：外部研究接口與參考文獻

1. Matěj Kripner and Milan Straka, **OpenProver: Agentic and Interactive Theorem Proving with Lean 4**, 2026, arXiv:2607.09217.  
2. Chengwu Liu et al., **Discover and Prove: An Open-source Agentic Framework for Hard Mode Automated Theorem Proving in Lean 4**, 2026, arXiv:2604.15839.  
3. Haocheng Ju et al., **Automated Conjecture Resolution with Formal Verification**, 2026, arXiv:2604.03789.  
4. Junqi Liu et al., **Numina-Lean-Agent: An Open and General Agentic Reasoning System for Formal Mathematics**, 2026, arXiv:2601.14027.  
5. Sijin Cheng and Olaf Hartig, **FedQPL: A Language for Logical Query Plans over Heterogeneous Federations of RDF Data Sources**, 2020, arXiv:2010.01190.  
6. Lars Heling and Maribel Acosta, **A Framework for Federated SPARQL Query Processing over Heterogeneous Linked Data Fragments**, 2021, arXiv:2102.03269.  
7. Amin Beiranvand and Nasser Ghadiri, **ADQUEX: Adaptive Processing of Federated Queries over Linked Data based on Tuple Routing**, 2015, arXiv:1505.04880.  

---

# 附錄 D：內部依賴

MWT-07 直接依賴：

- MWT-01《World Primitive 與 Presentation Theory》
- MWT-02《Global Legality Calculus》
- MWT-03《Global Interaction Graph and Noncommutative Scheduler》
- MWT-04《World State, Branch Convergence, and Dynamic Fixed Points》
- MWT-05《Unbounded Refinement, World Expansion, and Resolution Dynamics》
- MWT-06《Global Coupling Calculus and Multi-Resolution World Solve》
- GIPSS v0.2／DRC／SGCD
- 《全域欲相位認識論》
- 帳本因果數學／數學因果帳本
- NTLA-O identity / observer 主線

本文把既有「搜尋／欲」擴展成一般 World Query，但保留 GIPSS 作 discovery-query specialized backend。

