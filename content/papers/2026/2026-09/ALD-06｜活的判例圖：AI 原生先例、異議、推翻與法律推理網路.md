# ALD-06｜活的判例圖：AI 原生先例、異議、推翻與法律推理網路
## Living Precedent Graphs: AI-Native Precedent, Dissent, Overruling, and Legal Reasoning Networks

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 06 篇 / 10  
**前篇：** ALD-05〈AI 共同立法：自動反例、規範 Patch 與合法性不能自動化〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／AI 法律域／判例圖／法律推理網路／Precedent Runtime  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

ALD-01 已把 `Precedent Graph` 列為 AI Legal Runtime 的核心模組；ALD-05 又指出法律演化不只發生在 statute / regulation，也持續透過 case law 的 cite、follow、distinguish、limit、criticise、overrule、concur 與 dissent 發生。本文因此提出 Living Precedent Graph（LPG，活的判例圖）的第一版架構。

傳統案例資料庫通常以「案件文件」為主要單位，並把 citations 當作可搜尋 metadata。然而，單純「A cites B」不足以表達 precedent 的法律語義。引用可能是支持、適用、區分、限制、批評、推翻，甚至只是背景提及。Harvard Caselaw Access Project 已把數百萬案件構造成 citation graph；CourtListener 亦提供 backward / forward citation API，並保留 lead、concurrence、dissent 等 opinion type。2026 年的判例網路研究進一步顯示，citation networks 可被用來追蹤 judicial reasoning 的歷史主路徑；另一項 2026 年研究把 text、citations 與 dissenting opinions 合併進 precedent analysis；而 2025–2026 的 LLM overruling benchmark 則顯示，即使最高法院意見明確寫出 overrule，長上下文模型仍可能發生時序與法律關係判斷錯誤。這些發展共同指出：

$$
\boxed{
\text{Citation Retrieval}
\neq
\text{Precedent Understanding}.
}
$$

本文的第一個核心修正是：**Case 不應被視為判例圖的最小法律節點。** 同一 case 內可能有 majority / lead opinion、concurrence、dissent；同一 opinion 內又可能包含多個具有不同後續命運的 proposition / ratio。故本文提出三層節點模型：

$$
\boxed{
\mathcal V
=
V_C
\sqcup
V_O
\sqcup
V_P,
}
$$

其中：

- $V_C$：Case nodes；
- $V_O$：Opinion nodes；
- $V_P$：Proposition / ratio nodes。

因此，一個後案「推翻某先例」未必表示前案所有 proposition 都失效。本文提出：

$$
\boxed{
\text{Case Overruled}
\neq
\text{Every Proposition Invalid}.
}
$$

更精確的 precedent status 應以 proposition、issue、jurisdiction 與 time 為索引：

$$
\boxed{
\operatorname{Status}
(
p,
J,
t,
q
)
}
$$

而不是只問：

```text
is_good_law(case) = true / false
```

本文第二個核心結構是 typed precedent edge family：

$$
\boxed{
\mathcal E_P
=
E_{\mathrm{cite}}
\sqcup
E_{\mathrm{follow}}
\sqcup
E_{\mathrm{apply}}
\sqcup
E_{\mathrm{adopt}}
\sqcup
E_{\mathrm{distinguish}}
\sqcup
E_{\mathrm{limit}}
\sqcup
E_{\mathrm{criticise}}
\sqcup
E_{\mathrm{question}}
\sqcup
E_{\mathrm{overrule}}
\sqcup
E_{\mathrm{concur}}
\sqcup
E_{\mathrm{dissent}}
\sqcup
E_{\mathrm{supersede}}.
}
$$

不同司法體系實際用語可以不同；本文不宣稱存在唯一全球 treatment taxonomy。其最低要求是：

$$
\boxed{
\text{Citation Edge}
\neq
\text{Treatment Edge}.
}
$$

Harvard CAP citation graph 可很好描述「誰引用誰」，但 raw citation count / PageRank 不能單獨等同 binding authority。Canadian citation-network literature 也指出 raw citation counts 是 precedent normative influence 的不完美 proxy，而 NLP 可以進一步區分 follow、distinguish、overrule 等不同 citation treatment。本文因此提出 Authority Profile：

$$
\boxed{
\mathbf A_P
=
(
A_{\mathrm{hier}},
A_{\mathrm{jur}},
A_{\mathrm{binding}},
A_{\mathrm{treatment}},
A_{\mathrm{issue}},
A_{\mathrm{time}},
A_{\mathrm{procedure}}
).
}
$$

因此：

$$
\boxed{
\text{Graph Centrality}
\neq
\text{Binding Authority}.
}
$$

本文第三個核心貢獻是 Dissent Preservation Principle。Dissent 一般不具有 majority holding 的 binding status，但它不應被 AI Legal Runtime 丟棄為「錯誤答案」。Dissent 可能保存 alternative legal reasoning、指出 majority overlooked facts、提出 rights objection、預示未來 doctrinal change，並在後案被引用或重新採納。

因此：

$$
\boxed{
\text{Dissent}
\neq
\text{Binding Holding}
\neq
\text{Irrelevant Noise}.
}
$$

本文第四個核心結構是 Precedent Event Ledger。判例法律狀態不是 static metadata，而是一組時間事件：

$$
\boxed{
\mathcal H_P
=
\{
\mathsf{Decided},
\mathsf{Cited},
\mathsf{Followed},
\mathsf{Distinguished},
\mathsf{Limited},
\mathsf{Questioned},
\mathsf{Overruled},
\mathsf{Revived},
\mathsf{Superseded}
\}.
}
$$

因此：

$$
\operatorname{Status}(p,J,t_1)
\neq
\operatorname{Status}(p,J,t_2)
$$

可以完全合法。

本文進一步提出 Overruling Monotonicity with Historical Preservation：當後案 overrule 前案 proposition 時，Runtime 不得把舊 precedent node 從歷史刪掉。應新增：

$$
p_{\mathrm{new}}
\xrightarrow{\mathrm{overrule}}
p_{\mathrm{old}},
$$

並保留舊案在其生效期間曾具有的法律角色。故：

$$
\boxed{
\text{Overrule}
\neq
\text{Delete History}.
}
$$

本文第五個核心結構是 Precedent Query Runtime。`precedent.query` 不應只回 semantic similarity，而應返回 current status、relevant proposition、binding / persuasive profile、later treatment、negative treatment、jurisdiction、opinion type、temporal validity、dissent / concurrence、unresolved conflict 與 provenance。

本文稱之為：

$$
\boxed{
\text{Authority-Aware Precedent Retrieval}.
}
$$

2025 年的 overruling benchmark 顯示 LLM 在 236 組美國最高法院明確 overruling case pairs 上仍可能產生 era sensitivity、shallow reasoning 與 temporally impossible relations。故未來法律 RAG 不能只檢索「語義最像的舊案」，而必須把 later treatment 與 authority graph 納入檢索目標。

最後，本文提出：

$$
\boxed{
\text{Living Precedent}
=
\text{Text}
+
\text{Proposition}
+
\text{Treatment}
+
\text{Authority}
+
\text{Time}
+
\text{Dissent}
+
\text{Provenance}
+
\text{Review}.
}
$$

---

## 關鍵詞

AI 法律域；Living Precedent Graph；判例圖；Precedent；Citation Network；Overruling；Distinguishing；Dissent；Case Law；CourtListener；Caselaw Access Project；Legal Reasoning Graph；Authority-Aware Retrieval；Temporal Legal Graph

---

# 0. 從 ALD-05 的「修法」進到「判例演化」

ALD-05 已建立：

$$
N^{(\nu)}
\rightarrow
\operatorname{Counterexample}
\rightarrow
\Delta N^\ast
\rightarrow
\operatorname{Verify}
\rightarrow
\operatorname{Impact}
\rightarrow
\operatorname{Deliberate}
\rightarrow
\mathcal G_{\mathrm{legit}}
\rightarrow
N^{(\nu+1)}.
$$

但 common-law / case-law system 中，法律演化不只透過 $\Delta N$，還透過 case、opinion、ratio、interpretation、precedent treatment。

所以需要另一條動態通道：

$$
\boxed{
\text{Case}
\rightarrow
\text{Reasoning}
\rightarrow
\text{Treatment}
\rightarrow
\text{Doctrinal Evolution}.
}
$$

---

# 1. 第一個錯誤：判例庫等於文件庫

最簡單法律 RAG：

```text
query
-> vector search
-> top-k cases
-> answer
```

它把 precedent 當：

$$
\boxed{
\text{text chunks}.
}
$$

但真正法律問題是：

> 這個 case 在這個 issue 上，現在還有什麼 authority？

---

# 2. Citation 不等於 Precedential Support

若：

$$
A
\xrightarrow{\mathrm{cite}}
B,
$$

至少可能代表 follow、apply、distinguish、limit、criticise、overrule、background mention。

因此：

$$
\boxed{
\text{Cites}
\neq
\text{Supports}.
}
$$

---

# 3. Current Open Case-Law Infrastructure 已經有 Citation Graph

Harvard Caselaw Access Project 已公開數百萬 U.S. cases 的 citation graph。

CourtListener 亦提供：

- cited opinions；
- citing opinions；
- opinion clusters；
- lead / concurrence / dissent type；
- linked citations。

因此：

$$
\boxed{
\text{case-law graph infrastructure}
}
$$

已是現實。

---

# 4. 但 Raw Citation Graph 還不等於 Legal Reasoning Graph

CAP graph 的基本形式可以寫：

$$
\mathcal G_C
=
(
V_{\mathrm{case}},
E_{\mathrm{citation}}
).
$$

它能回答 who cites whom、inbound / outbound citations、centrality、cross-jurisdiction patterns。

但無法單靠 edge 存在回答：

> 這次引用是支持還是推翻？

---

# 5. Graph Centrality 不是 Binding Authority

CAP 可計算 PageRank / citation significance。

這對 influence、research priority、historical importance 很有價值。

但：

$$
\boxed{
\text{PageRank}
\neq
\text{Legal Binding Force}.
}
$$

---

# 6. Citation Count 的 normative limitation

Network citation analysis 已指出 raw citation count 是 normative influence 的不完美 proxy。

所以 AI Legal Runtime 必須從：

$$
E_{\mathrm{citation}}
$$

進一步推到：

$$
E_{\mathrm{treatment}}.
$$

---

# 7. Case 不是最小節點

一個 case 可能包含 majority opinion、plurality、concurrence、concurrence in judgment、dissent、per curiam、separate opinion。

所以：

$$
\boxed{
\text{Case Node}
\neq
\text{Opinion Node}.
}
$$

---

# 8. Opinion 也不是最小 doctrinal node

一份 majority opinion 可以同時提出：

$$
p_1,p_2,p_3,\ldots
$$

其中 $p_1$ 後來被 overrule， $p_2$ 仍有效， $p_3$ 只是 dictum， $p_4$ 僅限特殊 facts。

所以：

$$
\boxed{
\text{Opinion}
\neq
\text{One Atomic Rule}.
}
$$

---

# 9. Three-Layer Precedent Node Model

本文提出：

$$
\boxed{
\mathcal V
=
V_C
\sqcup
V_O
\sqcup
V_P.
}
$$

其中：

- $V_C$：Case nodes；
- $V_O$：Opinion nodes；
- $V_P$：Proposition / ratio / legal-reason nodes。

---

# 10. Case-to-Opinion Edge

$$
\boxed{
C
\xrightarrow{\mathrm{contains}}
O_i.
}
$$

並標：

$$
\operatorname{OpinionType}(O_i).
$$

---

# 11. Opinion-to-Proposition Edge

$$
\boxed{
O_i
\xrightarrow{\mathrm{asserts}}
p_j.
}
$$

每個 proposition 可附 issue、scope、facts、modality、ratio / dictum status、extraction provenance。

---

# 12. Proposition-Level Precedent

真正 precedence relation 可以：

$$
\boxed{
p_A
\xrightarrow{\mathrm{treat}}
p_B.
}
$$

因此「Case A overrules Case B」可以被細化成：

$$
p_A
\xrightarrow{\mathrm{overrule}}
p_B.
$$

---

# 13. Case Overruled 不等於 Every Proposition Invalid

$$
\boxed{
\text{Case Overruled}
\neq
\text{Every Proposition Invalid}.
}
$$

有些 overrule 是 narrow、issue-specific、partial、procedural。

---

# 14. Good Law 不能只是一個 Case Boolean

本文改成：

$$
\boxed{
\operatorname{Status}
(
p,
J,
t,
q
).
}
$$

其中：

- $p$：proposition；
- $J$：jurisdiction；
- $t$：time；
- $q$：query / issue。

---

# 15. Precedent Status Space

最低：

$$
\boxed{
\mathcal S_P
=
\{
\mathsf{Binding},
\mathsf{Persuasive},
\mathsf{Followed},
\mathsf{Applied},
\mathsf{Distinguished},
\mathsf{Limited},
\mathsf{Questioned},
\mathsf{Criticised},
\mathsf{Overruled},
\mathsf{Superseded},
\mathsf{Unresolved}
\}.
}
$$

---

# 16. Typed Precedent Edge Family

$$
\boxed{
\mathcal E_P
=
E_{\mathrm{cite}}
\sqcup
E_{\mathrm{follow}}
\sqcup
E_{\mathrm{apply}}
\sqcup
E_{\mathrm{adopt}}
\sqcup
E_{\mathrm{distinguish}}
\sqcup
E_{\mathrm{limit}}
\sqcup
E_{\mathrm{criticise}}
\sqcup
E_{\mathrm{question}}
\sqcup
E_{\mathrm{overrule}}
\sqcup
E_{\mathrm{concur}}
\sqcup
E_{\mathrm{dissent}}
\sqcup
E_{\mathrm{supersede}}.
}
$$

---

# 17. Treatment Taxonomy 不是全球固定標準

不同 legal systems 對 binding precedent、jurisprudence constante、persuasive authority、court hierarchy 處理不同。

所以本文只提出 typed treatment requirement，不宣稱全球法院必須使用完全同一 vocabulary。

---

# 18. Citation Edge ≠ Treatment Edge

$$
\boxed{
E_{\mathrm{cite}}
\neq
E_{\mathrm{follow}}
}
$$

也：

$$
\boxed{
E_{\mathrm{cite}}
\neq
E_{\mathrm{overrule}}.
}
$$

---

# 19. Follow

$$
A
\xrightarrow{\mathrm{follow}}
B
$$

表示後案將 B 的 relevant precedent reason 作為 followed / controlling reasoning。

---

# 20. Apply

$$
A
\xrightarrow{\mathrm{apply}}
B
$$

表示後案把 B 的 rule 應用到新的 facts / issue。

---

# 21. Distinguish

$$
A
\xrightarrow{\mathrm{distinguish}}
B
$$

不是「B is false」，而是：

> B 不控制此案，因 relevant difference 改變適用。

---

# 22. Distinguishing 本身仍是活的法理問題

2026 年 Legal Theory 研究專門討論 distinguishing、restrictive reinterpretation、constrained overruling。

這說明：

$$
\boxed{
\text{Distinguish}
}
$$

本身不是一個簡單「不採用」標記。

---

# 23. Limit

$$
A
\xrightarrow{\mathrm{limit}}
B
$$

表示縮小：

$$
\operatorname{Scope}(B).
$$

但未必完全 overrule。

---

# 24. Criticise / Question

後案可以 doubt、criticise、question 某 precedent，但仍受其拘束。

因此：

$$
\boxed{
\text{Negative Treatment}
\neq
\text{Overruled}.
}
$$

---

# 25. Overrule

最低定義：

$$
\boxed{
A
\xrightarrow{\mathrm{overrule}}
B
}
$$

表示具有足夠權威的後案明確取消 B 在某 legal proposition / point 上的 precedential force。

---

# 26. Overrule 與 Distinguish 必須嚴格分型

2025 的 Supreme Court overruling benchmark 為避免 ambiguity，只收 majority 明確表示 overrule 的 pairs，並排除 merely distinguished、limited、discredited。

因此：

$$
\boxed{
\text{Overrule}
\neq
\text{Distinguish}
\neq
\text{Limit}
\neq
\text{Discredit}.
}
$$

---

# 27. LLM 仍可能誤判 Overruling

2025 benchmark 使用 236 組明確 U.S. Supreme Court overruling pairs，模型仍有 era sensitivity、shallow reasoning、context-dependent failures、temporally impossible relations。

所以：

$$
\boxed{
\text{Long Context}
\neq
\text{Reliable Precedent Status}.
}
$$

---

# 28. Precedent RAG 必須 Authority-Aware

普通 semantic retrieval 只找「最像的案例」不夠。

更成熟：

$$
\boxed{
\operatorname{RetrievePrecedent}
(
q,J,t
)
}
$$

要同時考慮 semantic relevance、hierarchy、binding status、later treatment、negative treatment、time、proposition match。

---

# 29. Authority Profile

$$
\boxed{
\mathbf A_P
=
(
A_{\mathrm{hier}},
A_{\mathrm{jur}},
A_{\mathrm{binding}},
A_{\mathrm{treatment}},
A_{\mathrm{issue}},
A_{\mathrm{time}},
A_{\mathrm{procedure}}
).
}
$$

---

# 30. Hierarchy

 $A_{\mathrm{hier}}$ 表示 superior court、same court、lower court、coordinate court。

不是單一全球順序，由 jurisdiction 定義。

---

# 31. Jurisdiction

同一 precedent $B$ 在 $J_1$ 可以 binding，在 $J_2$ 只是 persuasive。

因此：

$$
\boxed{
\operatorname{Authority}(B,J_1)
\neq
\operatorname{Authority}(B,J_2).
}
$$

---

# 32. Treatment

大量 negative treatment 即使尚未 formal overrule，也可能改變實務風險。

但 Runtime 必須區分：

$$
\boxed{
\text{Doctrinal Weakening}
\neq
\text{Formal Invalidity}.
}
$$

---

# 33. Issue Specificity

Case B 在 contract law 重要，不表示它對 constitutional privacy 有同樣 authority。

所以：

$$
A_{\mathrm{issue}}
$$

必須存在。

---

# 34. Time

$$
\operatorname{Authority}(B,t_1)
\neq
\operatorname{Authority}(B,t_2).
$$

---

# 35. Procedure

例如 en banc、panel、chamber、grand chamber 可能影響 authority。

所以：

$$
A_{\mathrm{procedure}}
$$

不能省略。

---

# 36. Authority Vector 不能直接平均

如果 hierarchy 高但已 overruled，不能得到「0.5 authority」。

因此：

$$
\boxed{
\mathbf A_P
\text{ contains hard legal dimensions}.
}
$$

---

# 37. Graph Centrality 只是一個分析特徵

可有：

$$
Centrality(B)=0.99,
$$

仍可能：

$$
Status(B)=\mathsf{Overruled}.
$$

因此：

$$
\boxed{
\text{Graph Centrality}
\neq
\text{Binding Authority}.
}
$$

---

# 38. Main Path Analysis 的現實接口

2026 年 Artificial Intelligence and Law 研究以 446 件 CJEU consumer-rights cases 的 citation network，用 Main Path Analysis 追蹤 judicial reasoning 的歷史演化。

這支持 precedent network 不只拿來找 central case，還能研究 doctrinal path。

---

# 39. Living Graph 不只是 Static Network

本文定義：

$$
\boxed{
\mathcal G_P(t)
}
$$

而不是：

$$
\mathcal G_P.
$$

因為每個新判決都可能新增 node、treatment edge、status、authority path。

---

# 40. Precedent Event Ledger

$$
\boxed{
\mathcal H_P
=
\{
\mathsf{Decided},
\mathsf{Cited},
\mathsf{Followed},
\mathsf{Applied},
\mathsf{Distinguished},
\mathsf{Limited},
\mathsf{Questioned},
\mathsf{Criticised},
\mathsf{Overruled},
\mathsf{Revived},
\mathsf{Superseded}
\}.
}
$$

---

# 41. Status 是 Event-Derived

$$
\boxed{
\operatorname{Status}_t(p)
=
F(
\mathcal H_P^{\le t},
J,
q
).
}
$$

---

# 42. Overrule 不得刪歷史

若：

$$
p_2
\xrightarrow{\mathrm{overrule}}
p_1,
$$

不應 `delete p1`，而應保留 p1 曾有效的時期、依 p1 作出的案件、p2 的 overruling reason。

所以：

$$
\boxed{
\text{Overrule}
\neq
\text{Delete History}.
}
$$

---

# 43. Precedent Historical Monotonicity

在正常 provenance-preserving graph 中：

$$
\boxed{
\mathcal G_P(t)
\hookrightarrow
\mathcal G_P(t+1).
}
$$

新的 treatment 可以改變 current status，但不能假裝舊事件從未存在。

---

# 44. Revived / Reintroduced Reasoning

後案可能重新採納 old dissent、previously marginal rationale、abandoned doctrine element。

因此 graph 需要 reasoning lineage，而不是只保留 current winner。

---

# 45. Dissent Preservation Principle

$$
\boxed{
\text{Dissent}
\neq
\text{Binding Holding}
\neq
\text{Irrelevant Noise}.
}
$$

---

# 46. Dissent 為什麼要保留？

Dissent 可以保存 alternative interpretation、指出 rights conflict、保存 minority reasoning、預示 future doctrine、被後案引用或後來被 majority 採納。

---

# 47. 2026 Precedent Analysis 已把 Dissent 當重要訊號

ContraLEX 類研究把 textual content、citations、dissenting opinions 共同用於 precedent analysis。

這支持：

$$
\boxed{
\text{dissent is part of legal evolution signal}.
}
$$

---

# 48. Dissent Edge

$$
\boxed{
O_D
\xrightarrow{\mathrm{dissent\_from}}
O_M.
}
$$

還可以 proposition-level：

$$
p_D
\xrightarrow{\mathrm{rejects}}
p_M.
$$

---

# 49. Concurrence 也不能丟

Concurrence 可能同意結果，但提供不同理由、narrower / broader rule。

所以：

$$
\boxed{
\text{Same Judgment}
\neq
\text{Same Reason}.
}
$$

---

# 50. Holding、Ratio、Dictum 的抽取要保留不確定性

AI 可以提取：

$$
\operatorname{Role}(p)
\in
\{
\mathsf{Holding},
\mathsf{Ratio},
\mathsf{Dictum},
\mathsf{Uncertain}
\}.
$$

但不能假裝 extraction 永遠確定。

---

# 51. Proposition Extraction Certificate

每個 extracted proposition：

$$
p
$$

應附：

$$
\boxed{
K_p
=
(
case,
opinion,
span,
role,
issue,
extractor,
version,
evidence,
uncertainty
).
}
$$

---

# 52. AI 生成的 proposition 不是新的 precedent

如果 AI 對 case 做摘要：

$$
p_{AI},
$$

它只是 representation / extraction，不是 judicial holding。

所以：

$$
\boxed{
\text{AI Summary}
\neq
\text{Precedent}.
}
$$

---

# 53. Source Opinion 必須可回溯

所有 proposition 都要：

$$
p
\rightarrow
O
\rightarrow
C.
$$

若無法回到 source，只能：

$$
\mathsf{UnverifiedExtraction}.
$$

---

# 54. Precedent Graph 的時間方向

一般 citation：

$$
t_A>t_B
$$

時：

$$
A\rightarrow B.
$$

如果模型推較早 case overrule 較晚 case，可能是 Temporal Impossibility。

---

# 55. Temporal Constraint 是 Hard Gate

在普通 later-case overruling 定義中：

$$
\boxed{
\operatorname{Overrule}(A,B)
\Rightarrow
t_A>t_B.
}
$$

---

# 56. Precedent Query

$$
\boxed{
\operatorname{PrecedentQuery}
(
q,
J,
t,
\Gamma
)
\rightharpoonup
\mathcal R_P.
}
$$

---

# 57. Precedent Query Result

$$
\boxed{
\mathcal R_P
=
(
P,
S,
A,
T,
H,
D,
X,
R
).
}
$$

其中：

- $P$：relevant propositions；
- $S$：status；
- $A$：authority profile；
- $T$：later treatment；
- $H$：history；
- $D$：dissent / alternate reasoning；
- $X$：explanation / provenance；
- $R$：review / unresolved issues。

---

# 58. `precedent.query` 不應只回 Top-10

應回：

```text
case
opinion
proposition
relevance
authority
binding_status
later_treatment
negative_treatment
overruling_status
dissent
time
jurisdiction
source
```

---

# 59. Authority-Aware RAG

$$
\boxed{
Score
=
F(
\text{semantic relevance},
\mathbf A_P,
\text{treatment},
\text{time},
\text{issue}
).
}
$$

但 hard authority gates 不應被平均成單一 scalar。

---

# 60. Two-Stage Retrieval

## Stage 1

找 semantic / lexical relevant candidates。

## Stage 2

沿 precedent graph 查 current authority、overrule、distinguish、subsequent cases、jurisdiction。

---

# 61. Retrieval 的真正問題是「控制權威」

如果 query 是：

> X 現在是不是 good law？

只檢索 X 本身最危險。

真正答案可能在後案：

$$
Y
\xrightarrow{\mathrm{overrule}}
X.
$$

所以：

$$
\boxed{
\text{Retrieve Original Case}
\neq
\text{Retrieve Current Controlling Authority}.
}
$$

---

# 62. Good-Law Query

$$
\boxed{
\operatorname{GoodLaw}
(
p,
J,
t
)
}
$$

輸出：

```text
CURRENT_BINDING
CURRENT_PERSUASIVE
LIMITED
QUESTIONED
OVERRULED
SUPERSEDED
UNRESOLVED
```

並附 who、when、on what proposition、authority path。

---

# 63. Case-Level Flag 仍可存在，但只能是 Projection

UI 顯示：

```text
negative treatment
```

可以。

但 canonical data 應保留 proposition-level graph。

所以：

$$
\boxed{
\text{Case Badge}
=
\text{Projection of richer graph state}.
}
$$

---

# 64. Distinguish 不是 Negative Score

法院 distinguish precedent，可能恰恰證明 precedent 仍有 binding force，只是 facts 不同。

所以：

$$
\boxed{
\text{Distinguished}
\not\Rightarrow
\text{Weakened Globally}.
}
$$

---

# 65. Limited 才可能縮小 Scope

因此要追：

$$
\operatorname{Scope}_t(p).
$$

可以有：

$$
\operatorname{Scope}_{t+1}(p)
\subset
\operatorname{Scope}_t(p).
$$

---

# 66. Doctrinal Drift

法律變化常不是一次 Overrule，而可能：

$$
\mathsf{Follow}
\rightarrow
\mathsf{Distinguish}
\rightarrow
\mathsf{Question}
\rightarrow
\mathsf{Limit}
\rightarrow
\mathsf{Overrule}.
$$

本文稱：

$$
\boxed{
\text{Doctrinal Drift Path}.
}
$$

---

# 67. Drift 不等於 Formal Overrule

$$
\boxed{
\text{Doctrinal Drift}
\neq
\text{Formal Overruling}.
}
$$

---

# 68. Main Path 與 Drift 可以互補

Main Path Analysis 找 doctrine 主要歷史路徑；treatment-aware temporal graph 找 precedent treatment 如何逐步改變。

兩者可以成為：

$$
\boxed{
\text{legal evolution observatory}.
}
$$

---

# 69. Precedent Fork

同一 precedent 可能產生不同 interpretation branch：

$$
p
\rightarrow
\{
p_A,
p_B
\}.
$$

---

# 70. 判例 Fork 不等於 Identity Fork

這裡的 fork 是 doctrinal interpretation branch，不是 Dynamic Theseus subject fork。

---

# 71. Jurisdictional Split

若：

$$
J_1
$$

採 $p_A$，而 $J_2$ 採 $p_B$，Runtime 應輸出：

$$
\boxed{
\mathsf{JurisdictionalSplit}.
}
$$

而不是平均兩者。

---

# 72. Court Split

可標：

$$
E_{\mathrm{split}}.
$$

後續 superior authority 可能 resolve、preserve、narrow。

---

# 73. Precedent Merge

後案也可能綜合：

$$
p_A,p_B
$$

形成：

$$
p_C.
$$

但：

$$
\boxed{
\text{Synthesis}
\neq
\text{Erase Prior Branches}.
}
$$

---

# 74. Dissent-to-Majority Transition

某 dissent proposition $p_D$ 未來被 majority opinion $p_M'$ 採納。

可以記：

$$
\boxed{
p_M'
\xrightarrow{\mathrm{revives/adopts}}
p_D.
}
$$

---

# 75. Alternative Reasoning Lineage

Living Precedent Graph 不只回答現在贏的是誰，還可以回答：

> 現在這條 doctrine 是從哪個曾經的少數路徑長出來？

---

# 76. Judicial Memory 不應 Winner-Take-All

如果只保存 majority holdings，會失去 dissent、concurrence、criticised reasoning、abandoned branches。

所以：

$$
\boxed{
\text{Current Law}
\neq
\text{Complete Legal Memory}.
}
$$

---

# 77. Precedent Graph 需要 Provenance

每條 treatment edge：

$$
e
$$

至少標：

$$
\boxed{
K_e
=
(
source\_opinion,
target,
relation,
span,
court,
J,
t,
authority,
extractor,
verification
).
}
$$

---

# 78. Human-Asserted vs AI-Inferred Edge

edge status 應區分：

```text
EXPLICIT_JUDICIAL
CURATED_LEGAL
AI_INFERRED
UNVERIFIED
```

---

# 79. AI-Inferred Overrule 不得默默升格

如果 model 推：

$$
A
\xrightarrow{\mathrm{overrule}}B,
$$

但 source 沒明確支持，只能：

$$
\mathsf{AI\_INFERRED}.
$$

不能冒充：

$$
\mathsf{EXPLICIT\_JUDICIAL}.
$$

---

# 80. Edge Verification

$$
\boxed{
\operatorname{VerifyEdge}
(
e,
source,
authority
)
}
$$

可輸出：

- Verified；
- Probable；
- Ambiguous；
- Refuted；
- InsufficientEvidence。

---

# 81. Citation Extraction Error

OCR、citation parser、name ambiguity 都可能建錯 edge。

所以：

$$
\boxed{
\text{Graph Edge}
\neq
\text{Automatically True}.
}
$$

---

# 82. Open Data 的價值

CAP 與 CourtListener 之類 open infrastructure 的重要性是 reproducibility、public verification、benchmark creation、independent research。

AI Legal Domain 應盡量保留：

$$
\boxed{
\text{verifiable public provenance}.
}
$$

---

# 83. Precedent Cache

Runtime 可以 cache：

$$
\operatorname{PrecedentQuery}(q).
$$

但新 case 發生後，相關 cache 必須 invalidate。

---

# 84. Precedent Impact Closure

定義：

$$
\boxed{
\operatorname{PrecedentImpactClosure}
(
e
)
}
$$

追蹤 affected propositions、dependent cases、certificates、legal advice、Agent permissions、pending matters。

---

# 85. Overruling 的影響閉包可能巨大

一個 overrule：

$$
p_{\mathrm{new}}
\rightarrow
p_{\mathrm{old}}
$$

可能使：

$$
|\operatorname{ImpactClosure}|
\gg1.
$$

所以 legal runtime 需要 revalidation。

---

# 86. Overrule 不等於所有歷史決定自動撤銷

這取決於 doctrine、procedure、retroactivity、finality、jurisdiction。

所以：

$$
\boxed{
\text{Precedent Overruled}
\neq
\text{All Past Judgments Automatically Void}.
}
$$

---

# 87. 判例圖也需要 ALD-03 的 Failure Semantics

`precedent.query` 可能輸出：

- CaseNotFound；
- CitationAmbiguous；
- OpinionTypeUnknown；
- TreatmentUnresolved；
- AuthorityConflict；
- JurisdictionSplit；
- TemporalConflict；
- ExtractionUnverified。

不是單純：

```text
no precedent
```

---

# 88. 判例圖也需要 ALD-04 的 Versioning

Graph schema：

$$
\nu_G.
$$

Treatment taxonomy：

$$
\nu_T.
$$

Extraction model：

$$
\nu_M.
$$

都需要版本。

---

# 89. 判例圖也需要 ALD-05 的 Legitimation Separation

AI 可以 infer edge、suggest treatment、detect drift。

但：

$$
\boxed{
\text{AI-Inferred Legal Relation}
\neq
\text{Judicial Act}.
}
$$

---

# 90. AI 不能自己 overrule precedent

除非未來法律正式授予某 juridical AI judicial authority。

現在不能因：

> AI 覺得舊案錯

就改：

$$
Status=\mathsf{Overruled}.
$$

---

# 91. Legal Reasoning Graph

最終：

$$
\boxed{
\mathfrak G_L
=
(
V_C,
V_O,
V_P,
E_P,
A,
T,
H,
K
).
}
$$

其中：

- $V_C$：cases；
- $V_O$：opinions；
- $V_P$：propositions；
- $E_P$：typed treatment edges；
- $A$：authority profiles；
- $T$：temporal state；
- $H$：event history；
- $K$：provenance / certificates。

---

# 92. Living Precedent Graph

$$
\boxed{
\mathfrak G_L(t+1)
=
\operatorname{Update}
(
\mathfrak G_L(t),
case_{t+1},
treatment_{t+1}
).
}
$$

這是一個：

$$
\boxed{
\text{append-preserving, status-recomputing legal graph}.
}
$$

---

# 93. 判例圖不是 Knowledge Graph 的普通子類

因為它有 binding authority、hierarchy、procedural status、legal effect、overruling、temporal applicability。

所以：

$$
\boxed{
\text{Legal Reasoning Graph}
\neq
\text{Generic Knowledge Graph}.
}
$$

---

# 94. Human UI 與 AI UI 可以不同

AI 可以看完整 graph、edge、authority vector、status history。

人類 UI 可以投影：

> 這個 precedent 已被部分限制，原因如下。

所以：

$$
\boxed{
\text{same legal graph}
\rightarrow
\text{different explanatory projections}.
}
$$

---

# 95. 判例查詢的最低 Explanation Surface

回答：

1. Which proposition?
2. Which court?
3. Which jurisdiction?
4. Binding or persuasive?
5. Later treatment?
6. Explicit overrule?
7. Distinguished on facts?
8. Relevant dissent?
9. Effective at what time?
10. Source spans?

---

# 96. 十四個核心非等價

$$
\boxed{
\text{Citation}
\neq
\text{Support}
}
$$

$$
\boxed{
\text{Case}
\neq
\text{Opinion}
}
$$

$$
\boxed{
\text{Opinion}
\neq
\text{Atomic Rule}
}
$$

$$
\boxed{
\text{Case Overruled}
\neq
\text{Every Proposition Invalid}
}
$$

$$
\boxed{
\text{PageRank}
\neq
\text{Binding Authority}
}
$$

$$
\boxed{
\text{Negative Treatment}
\neq
\text{Formal Overrule}
}
$$

$$
\boxed{
\text{Distinguish}
\neq
\text{Overrule}
}
$$

$$
\boxed{
\text{Dissent}
\neq
\text{Binding Holding}
}
$$

$$
\boxed{
\text{Dissent}
\neq
\text{Irrelevant Noise}
}
$$

$$
\boxed{
\text{AI Summary}
\neq
\text{Precedent}
}
$$

$$
\boxed{
\text{Semantic Similarity}
\neq
\text{Controlling Authority}
}
$$

$$
\boxed{
\text{Doctrinal Drift}
\neq
\text{Formal Overruling}
}
$$

$$
\boxed{
\text{Overrule}
\neq
\text{Delete History}
}
$$

$$
\boxed{
\text{AI-Inferred Relation}
\neq
\text{Judicial Act}
}
$$

---

# 97. 八個工程測試

## 97.1 Citation Treatment Test

同一 cited case 分別構造 follow、distinguish、overrule，確認 Runtime 不只輸出 `cited=true`。

## 97.2 Partial Overrule Test

一個 case 有三個 propositions，只 overrule 其中一個。case-level badge 可以 negative，但另外兩個 proposition 仍可 valid。

## 97.3 Dissent Preservation Test

dissent 未 binding，但可被後案 query / cite / adopt。

## 97.4 Temporal Impossibility Test

較早 case 不得被誤標為 later-case overrule。

## 97.5 Authority vs Centrality Test

高 PageRank 但已 overruled case，不得排序為 current controlling authority。

## 97.6 Jurisdiction Split Test

不同 jurisdictions 採不同 proposition branch，輸出 `JurisdictionalSplit`。

## 97.7 Overrule Impact Closure Test

新增 overrule edge 後，追蹤 stale certificates / cached advice。

## 97.8 AI Edge Provenance Test

AI-inferred edge 未經驗證，不能升格 explicit judicial treatment。

---

# 98. 可反駁點

## 98.1 Proposition Extraction Cost

把所有 cases 拆到 proposition level 成本高。可以先對高價值 / high-risk precedent 做細粒度處理。

## 98.2 Treatment Taxonomy Ambiguity

法院語言不總是標準化。所以 edge 可以保留：

$$
\mathsf{AmbiguousTreatment}.
$$

## 98.3 Common-Law Bias

本文大量使用 precedent / overrule 語言，主要適合 precedent-sensitive systems。Civil-law / mixed systems 需要調整 authority semantics。

## 98.4 Dissent Overweighting

保留 dissent 不表示應給 dissent 與 majority 同等 authority。

## 98.5 Graph Fetish

graph 結構不能取代原始 opinion text、法律解釋與制度脈絡。

## 98.6 AI Treatment Error

LLM 對 overrule / distinguish 的判斷仍可能錯。因此來源與 verification layer 必須保留。

---

# 99. 與下一篇的接口

下一篇：

## ALD-07｜Juridical Routing：分散式 AI 的跨法域選擇與法律路由

ALD-06 已建立：

$$
\operatorname{Status}
(
p,
J,
t,
q
)
$$

明確要求 $J$ 是 precedent status 的一級索引。

下一篇將處理：

- compute jurisdiction；
- entity jurisdiction；
- user jurisdiction；
- data jurisdiction；
- effect jurisdiction；
- lineage jurisdiction；
- conflict of laws；
- route selection；
- multi-jurisdiction LawCall；
- forum / authority ambiguity。

---

# 100. 結論

傳統法律搜尋常問：

> 有沒有一個案例講過這件事？

AI 原生法律真正要問的是：

> 哪一個 proposition 在哪個 jurisdiction、哪個時間、經過哪些 later treatments 後，現在還具有什麼 authority？

因此 precedent 不應只是一個 PDF。

它是一個動態節點，持續被 cite、follow、apply、distinguish、limit、criticise、question、overrule、dissent、revive。

所以：

$$
\boxed{
\text{Living Precedent}
=
\text{Text}
+
\text{Proposition}
+
\text{Treatment}
+
\text{Authority}
+
\text{Time}
+
\text{Dissent}
+
\text{Provenance}
+
\text{Review}.
}
$$

最終的 AI Legal Runtime 不應只做：

```text
find similar cases
```

而應做：

$$
\boxed{
\text{retrieve relevant authority}
\rightarrow
\text{trace later treatment}
\rightarrow
\text{resolve jurisdiction}
\rightarrow
\text{preserve dissent}
\rightarrow
\text{compute current status}
\rightarrow
\text{return provenance}.
}
$$

本篇最後收斂成兩句：

$$
\boxed{
\text{判例不是被引用過多少次；}
}
$$

$$
\boxed{
\text{判例是它在整個法律推理網路中，現在被誰以什麼理由承認、限制、區分、反對或推翻。}
}
$$

以及：

$$
\boxed{
\text{成熟的法律記憶，不只保存最後贏的判決；}
}
$$

$$
\boxed{
\text{還要保存法律如何爭論、分叉、異議、改變與重新理解自己。}
}
$$

---

# 參考文獻

1. Harvard Library Innovation Lab. *Caselaw Access Project Citation Graph*. 2020.
2. Harvard Library Innovation Lab. *Caselaw Access Project Cite Grid*. 2020.
3. Harvard Library Innovation Lab. *Introducing CAP Case Analysis*. 2020.
4. Free Law Project. *CourtListener Case Law API* and *Opinions Cited/Citing API*. Current documentation accessed 2026.
5. van Kuppevelt, D. et al. *Tracking the evolution of case law with main path analysis*. Artificial Intelligence and Law, 2026.
6. *Leveraging textual content, citational aspects and dissenting opinions through a multi-view contrastive learning methodology for legal precedent analysis*. Computer Law & Security Review 60, 2026, 106257.
7. Zhang, Li, Jaromir Savelka, and Kevin Ashley. *Do LLMs Truly Understand When a Precedent Is Overruled?* 2025/2026.
8. Stanford RegLab / Casetext. *The Overruling Dataset: A Benchmark for Detecting Legal Decisions that Have Been Overruled*.
9. Mullins, Robert. *Distinguishing and Reinterpreting in the Reason Model of Precedent*. Legal Theory 32, 2026, e1.
10. Network Citation Analysis, CanLII Docs 2024, discussing directional citation networks and treatment-aware NLP.
11. Neo.K × Aletheia. 《ALD-01｜AI 法律域：從 Law as Code 到機器原生規範 Runtime》v0.1, 2026.
12. Neo.K × Aletheia. 《ALD-05｜AI 共同立法：自動反例、規範 Patch 與合法性不能自動化》v0.1, 2026.
13. Neo.K. 《網路資訊海作為文明動態記憶：總論與未來命題》v0.1, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Case / Opinion / Proposition 三層節點明確分離
- Citation edge 與 treatment edge 明確分離
- follow / apply / distinguish / limit / criticise / question / overrule / dissent 分型
- 不宣稱存在全球唯一 treatment taxonomy
- Graph Centrality / Citation Count 不等同 Binding Authority
- Good Law 不以單一 case-level Boolean 作 canonical representation
- Case Overruled 不自動等同 Every Proposition Invalid
- Dissent 被保留但不提升為 majority binding holding
- AI summary / AI-inferred edge 不冒充 judicial holding / judicial act
- Precedent status 明確索引 jurisdiction / time / issue
- Overruling 使用 append-preserving history，不刪除 precedent history
- 2025/2026 LLM overruling benchmark 僅作模型限制證據
- Harvard CAP / CourtListener 僅作現有 open citation infrastructure 錨點
