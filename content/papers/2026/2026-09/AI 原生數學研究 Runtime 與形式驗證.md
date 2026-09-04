# MRSM Paper 03  
# AI 原生數學研究 Runtime 與形式驗證  
## AI-Native Mathematical Research Runtime and Formal Verification  
### Event-Sourced Research States, Autonomous Proof-Space Operations, and Kernel-Verified Mathematical Authority

**Series:** Mathematical Research Space Methodology（MRSM）  
**Paper:** 03  
**Version:** v0.1  
**Date:** 2026-08-28  
**Author:** Neo.K  
**Institution:** EveMissLab／一言諾科技有限公司

---

## 摘要

MRSM Paper 00 提出將數學研究過程本身物件化為可計算研究空間；Paper 01 建立 proof-space geometry、frontier、cut set、quotient、obstruction cover 與 relative exhaustion；Paper 02 則建立 Research Closure Calculus，使 route blocking、authority upgrade、scope transfer、proof debt、reopening 與 parent closure 成為 typed、certificate-carrying state transitions。

本系列最後一篇進一步回答：

> 如何將上述方法真正實作成可長期運作、可由 AI 操作、可由形式驗證器審核、可重播且不因自然語言推論而發生 epistemic collapse 的數學研究系統？

本文提出 **AI-Native Mathematical Research Runtime（AMRR）**。系統以事件溯源架構建立三層研究狀態：

\[
L_0
=
\text{Canonical Research Event Ledger},
\]

\[
L_1
=
\text{Native Mathematical Research State},
\]

\[
L_2
=
\text{Human / AI / Formal Views}.
\]

任何 canonical mathematical state 均由：

\[
\mathfrak M_t
=
\mathsf{Replay}
(
L_{\le t},
\Pi_t
)
\]

重建，其中 \(\Pi_t\) 是當前 validation、authority 與 admissibility policy。

在此架構中，AI 不直接擁有修改 mathematical truth 的權限，而僅能產生 proposals、candidates、routes、obstructions、formalization obligations 與 verification requests。所有高權限狀態轉換必須經過 certificate gate、scope gate、authority gate 與 parent propagation gate。Lean、Coq、SMT solver、symbolic engine 與外部 formal workbench 則被視為不同型別的 verification authority，而非與 AI 語言生成混為一體。

本文定義 AI-native research operators，包括：

\[
\mathsf{Observe},
\quad
\mathsf{RouteGenerate},
\quad
\mathsf{FrontierDetect},
\quad
\mathsf{ObstructionSearch},
\quad
\mathsf{QuotientPropose},
\]

\[
\mathsf{Formalize},
\quad
\mathsf{Verify},
\quad
\mathsf{Reopen},
\quad
\mathsf{ClosureAudit}.
\]

同時提出 Candidate Layer、Native State Gate、Formal Translation Certificate、Kernel Authority Protocol、cross-implementation replication、cross-kernel replication、deterministic replay、content-addressed evidence 與 fail-closed unknown handling。

本文主張，真正的 AI-native mathematics 不應被理解為：

\[
\text{LLM}
\to
\text{Proof Text},
\]

而更應被理解為：

\[
\boxed{
\text{Human}
+
\text{AI}
+
\text{Persistent Research Runtime}
+
\text{Formal Verification}
\leftrightarrow
\text{Dynamic Mathematical Research Space}.
}
\]

AI 在此不只是 theorem generator，而是大型 proof-space 的持續觀察者、管理者、路線生成器、證據協調者與研究狀態維護者。

**關鍵詞：** AI Mathematics、Mathematical Research Runtime、Event Sourcing、Proof Space、Formal Verification、Lean、Coq、Research Agent、Closure Audit、Mathematical Knowledge System

---

# 1. 導論：從 AI 寫證明到 AI 維護數學研究空間

目前大量 AI mathematics 研究集中於：

\[
\text{Problem}
\to
\text{Generated Proof}.
\]

這個方向具有重要價值。

但對大型、長期、跨數十年文獻與多種 representation 的未解問題而言，真正瓶頸未必只是：

> 下一行證明怎麼寫？

還包括：

- 現在有哪些 proof routes？
- 哪些 routes 已被合法阻斷？
- 哪些 no-go 只作用於局部 scope？
- 哪些 theorem 尚未獨立驗證？
- 哪些 bridge 尚有 proof debt？
- 哪些 old result 應因新 theorem reopening？
- 哪些 routes 實際屬於同一 quotient class？
- 哪些 formal proof 只證了 bounded child，而沒有證 parent claim？

因此大型研究問題需要的不只是 theorem prover。

它需要：

\[
\boxed{
\textbf{Mathematical Research Operating Runtime}.
}
\]

---

# 2. AI-Native Mathematics 的重新定義

本文提出：

\[
\boxed{
\text{AI-Native Mathematics}
\neq
\text{AI-generated mathematical prose}.
}
\]

真正 AI-native 的數學系統至少應使 AI 能持續操作：

\[
\mathfrak M_t,
\]

也就是完整 mathematical research state。

AI 所面對的基本單位不再只是 prompt。

而是：

\[
\boxed{
\text{Persistent Mathematical State}.
}
\]

---

# 3. 三層 Runtime Architecture

定義三層：

## Layer 0 — Canonical Event Ledger

\[
L_0.
\]

保存所有具有 canonical authority 的研究事件。

---

## Layer 1 — Native Mathematical State

\[
L_1.
\]

由 ledger replay 得到真正 machine-authoritative research state。

---

## Layer 2 — Views

\[
L_2.
\]

包括：

- human-readable paper；
- AI context；
- graph visualization；
- dashboard；
- formal prover input；
- summary；
- frontier report。

因此：

\[
\boxed{
L_2
\neq
L_1.
}
\]

---

# 4. 為什麼 View 不能當 Native State

自然語言 summary 一定會遺失資訊。

如果完整 native state 有：

\[
10^5
\]

個 edges，

一篇 paper 只能投影其中很小部分。

因此：

\[
\Pi(
\mathfrak M
)
=
V
\]

只是 projection。

不能反向假定：

\[
V
=
\mathfrak M.
\]

所以：

\[
\boxed{
\text{Context omission}
\neq
\text{Mathematical absence}.
}
\]

這對 LLM 尤其重要。

---

# 5. Event-Sourced Mathematical State

令 canonical event ledger：

\[
L=
(e_1,e_2,\ldots,e_n).
\]

則：

\[
\mathfrak M_n
=
\mathsf{Replay}
(
e_1,\ldots,e_n
).
\]

例如 events：

\[
\mathrm{REGISTER\_CLAIM},
\]

\[
\mathrm{REGISTER\_ROUTE},
\]

\[
\mathrm{REGISTER\_OBSTRUCTION},
\]

\[
\mathrm{BLOCK\_ROUTE},
\]

\[
\mathrm{REGISTER\_CERTIFICATE},
\]

\[
\mathrm{UPGRADE\_AUTHORITY},
\]

\[
\mathrm{REOPEN}.
\]

---

# 6. Replay as Research Integrity

runtime 的基本一致性要求：

\[
\boxed{
\mathsf{Replay}(L)
=
\mathfrak M_{\rm native}.
}
\]

如果：

\[
\mathsf{Replay}(L)
\neq
\mathfrak M_{\rm native},
\]

則問題不是「數學意見不同」。

而是：

\[
\boxed{
\mathsf{RuntimeIntegrityFailure}.
}
\]

---

# 7. Determinism

相同：

\[
L
\]

與相同：

\[
\Pi
\]

應得到：

\[
\boxed{
H(
\mathfrak M
)
=
\text{same hash}.
}
\]

因此 canonical state 不應包含：

- temporary path；
- wall-clock duration；
- local username；
- hostname；
- random output directory。

---

# 8. Evidence Identity

proof artifact應使用：

\[
\mathsf{ContentID}(E)
=
\mathrm{SHA256}(E).
\]

因此：

\[
\boxed{
\text{Evidence Location}
\neq
\text{Evidence Identity}.
}
\]

同一證明從：

```text id="rm0suk"
C:\proof\a.lean
```

移到：

```text id="gtar9y"
/home/user/proof/a.lean
```

不應改變 mathematical state。

---

# 9. Native Mathematical Object

一個 native object 可以表示為：

\[
X=
\langle
id,
type,
statement,
scope,
status,
authority,
assumptions,
debt,
certificates,
history
\rangle.
\]

這比單純：

```text id="ufgw2f"
theorem = true
```

具有更高資訊解析度。

---

# 10. Candidate Layer

所有自然語言、AI output、paper extraction 首先必須進：

\[
L_{\rm candidate}.
\]

例如：

```text id="hnzp3h"
Theorem 7 is proved.
```

不得直接轉：

\[
\mathrm{FORMAL\_PROOF}.
\]

而應轉：

\[
\mathsf{ProofClaimCandidate}.
\]

---

# 11. Candidate Firewall

因此：

\[
\boxed{
\text{Paper}
\to
\text{Candidate}
\to
\text{Audit}
\to
\text{Native State}.
}
\]

AI output 同樣：

\[
\boxed{
\text{AI Proposal}
\neq
\text{Native Mathematical Fact}.
}
\]

---

# 12. AI Operator Model

定義 AI research agent：

\[
\mathcal A_i.
\]

Agent 不直接寫 native state。

它只能提出：

\[
p
=
\mathsf{Proposal}
(
operator,
subjects,
evidence,
reason
).
\]

例如：

\[
\mathsf{Proposal}
(
\mathsf{BlockRoute},
R,
O
).
\]

---

# 13. Proposal Gate

proposal 經：

\[
\mathsf{ValidateProposal}.
\]

驗證：

- subject identity；
- scope；
- certificate；
- authority；
- dependencies；
- parent rules。

如果合法：

\[
\mathsf{Commit}.
\]

否則：

\[
\mathsf{Reject}
\]

或：

\[
\mathsf{Defer}.
\]

---

# 14. AI Creativity 與 Authority 分離

因此：

\[
\boxed{
\text{Generation Authority}
\neq
\text{Mathematical Authority}.
}
\]

AI 可以大量生成：

- route；
- conjecture；
- representation；
- analogy；
- possible bridge。

但 native state只接受通過 validation gate 的部分。

---

# 15. Observe Operator

定義：

\[
\mathsf{Observe}
(
\mathfrak M,
q
)
\]

讓 AI 讀取指定研究子圖。

這不是把全部 database塞進 context。

而是根據：

- target；
- frontier；
- dependency；
- scope；

產生 context projection。

---

# 16. Context as Query Result

因此 AI context應被理解為：

\[
C_t
=
Q(
\mathfrak M_t
).
\]

不是：

\[
C_t
=
\mathfrak M_t.
\]

這個區分能降低：

\[
\boxed{
\text{Context-local hallucinated closure}.
}
\]

---

# 17. RouteGenerate

定義：

\[
\mathsf{RouteGenerate}
(
Q,
\mathfrak M_t
)
\to
\{
R_1,\ldots,R_k
\}.
\]

產生的新 route一律為：

\[
\mathsf{RouteCandidate}.
\]

不具有 proof authority。

---

# 18. Route Novelty

AI route generator 不應只檢查文字相似度。

需要比較：

- assumptions；
- mechanism；
- representation；
- critical dependency；
- obstruction structure。

因此：

\[
\boxed{
\text{Novel Wording}
\neq
\text{Novel Proof Route}.
}
\]

---

# 19. QuotientPropose

AI 可以提出：

\[
R_i
\sim
R_j.
\]

但只是：

\[
\mathsf{QuotientProposal}.
\]

真正 quotient需要：

\[
C_{\sim}.
\]

因為錯誤 merge可能一次誤殺大量 proof space。

---

# 20. ObstructionSearch

operator：

\[
\mathsf{ObstructionSearch}
(
R,
\mathfrak M
)
\]

尋找：

- contradiction；
- impossibility theorem；
- invariant violation；
- compactness failure；
- representation inconsistency；
- known no-go。

結果為：

\[
\mathsf{ObstructionCandidate}.
\]

---

# 21. FrontierDetect

令：

\[
\mathcal F_t
=
\mathsf{FrontierDetect}
(
\mathfrak M_t
).
\]

frontier detection可考慮：

\[
\text{impact},
\quad
\text{dependency centrality},
\quad
\text{survivor coverage},
\quad
\text{proof debt},
\quad
\text{verification cost}.
\]

---

# 22. Research Priority Score

可以定義：

\[
\operatorname{Priority}(x)
=
\alpha I(x)
+
\beta C(x)
+
\gamma U(x)
-
\delta K(x),
\]

其中：

- \(I\)：closure impact；
- \(C\)：centrality；
- \(U\)：uncertainty reduction；
- \(K\)：estimated cost。

但：

\[
\boxed{
\text{Priority}
\neq
\text{Truth}.
}
\]

它只是研究排程資訊。

---

# 23. AI-Native Research Scheduling

傳統研究者通常根據直覺選下一步。

AI runtime可以使用：

\[
\mathsf{Schedule}
(
\mathcal F_t,
resources
).
\]

把 frontier拆給：

- symbolic agent；
- literature agent；
- formalization agent；
- counterexample agent；
- theorem-prover agent。

---

# 24. Multi-Agent Research

令 agents：

\[
\mathcal A_1,\ldots,\mathcal A_n.
\]

不同 agent可以有不同角色。

例如：

\[
\mathcal A_{\rm search},
\]

\[
\mathcal A_{\rm algebra},
\]

\[
\mathcal A_{\rm formal},
\]

\[
\mathcal A_{\rm audit},
\]

\[
\mathcal A_{\rm adversarial}.
\]

但所有 agent共享：

\[
\boxed{
\text{same canonical research state}.
}
\]

---

# 25. 為什麼共享 State 比共享 Conversation 更重要

multi-agent若只共享聊天紀錄，容易產生：

- inconsistent summaries；
- forgotten assumptions；
- duplicate routes；
- authority confusion。

如果共享：

\[
\mathfrak M,
\]

則 conversation只是一種 view。

因此：

\[
\boxed{
\text{Shared State}
>
\text{Shared Transcript}
}
\]

對長期數學研究尤其如此。

---

# 26. Independent Verification Layer

candidate theorem可依序通過：

\[
\mathsf{SourceAudit},
\]

\[
\mathsf{IndependentCheck},
\]

\[
\mathsf{CrossImplementationReplication},
\]

\[
\mathsf{FormalVerification}.
\]

形成 authority stack。

---

# 27. Independent Verification 不等於 Formal Proof

symbolic verifier：

\[
V_{\rm sym}
\]

可以證明 algebraic identity。

但：

\[
\boxed{
\mathsf{SymbolicallyVerified}
\neq
\mathsf{KernelFormalProof}.
}
\]

因此 authority tier必須分開。

---

# 28. Cross-Implementation Replication

若同一 mathematical asset由兩個獨立實作：

\[
V_1,
V_2
\]

得到相同 result，

則：

\[
\mathsf{CROSS\_IMPLEMENTATION\_REPLICATED}.
\]

要求：

\[
V_1
\]

不能只是呼叫：

\[
V_2.
\]

---

# 29. Formalization Layer

令 native theorem：

\[
T.
\]

formalization pipeline：

\[
T
\to
FIR(T)
\to
O(T),
\]

其中：

- \(FIR\)：formalization intermediate representation；
- \(O(T)\)：proof-assistant obligation。

---

# 30. Translation Is a Proof Obligation

最危險的錯誤之一是：

> Lean證明成功，但 Lean檔實際證了另一個命題。

因此必須：

\[
C_{\rm translation}.
\]

要求：

\[
\boxed{
\mathsf{KernelVerified}(O)
+
\mathsf{TranslationValid}(T,O)
}
\]

才能：

\[
\mathsf{FORMAL\_PROOF}(T).
\]

---

# 31. Formal Backend Layer

formal backends可以包括：

\[
\text{Lean},
\]

\[
\text{Coq},
\]

\[
\text{Isabelle},
\]

\[
\text{SMT},
\]

或其他 kernel / solver。

每個 backend都應有明確 adapter contract。

---

# 32. Checker Identity

任何 formal run應記：

\[
\mathsf{CheckerIdentity}
=
\langle
backend,
version,
binary\_hash
\rangle.
\]

不能只有：

```text id="lsqndo"
Lean passed
```

因為這無法回答：

> 哪個 Lean？

> 哪個 binary？

> 哪個 obligation？

---

# 33. Formal Outcome

一個 formal outcome 至少應記：

\[
\langle
status,
checker,
obligation\_hash,
axioms,
assumptions,
limitations
\rangle.
\]

formal status建議至少：

\[
\{
\mathrm{VERIFIED},
\mathrm{REFUTED},
\mathrm{UNKNOWN},
\mathrm{UNAVAILABLE}
\}.
\]

---

# 34. Missing Checker Firewall

如果 Lean不存在：

\[
\mathrm{UNAVAILABLE}.
\]

不能：

\[
\mathrm{VERIFIED}.
\]

因此：

\[
\boxed{
\text{Tool Missing}
\neq
\text{Proof Passed}.
}
\]

---

# 35. Incomplete Formal Proof

例如 Lean存在：

```lean id="i10aky"
sorry
```

則：

\[
\boxed{
\mathrm{UNKNOWN}
}
\]

而不是：

\[
\mathrm{VERIFIED}.
\]

---

# 36. Axiom Audit

formal proof的 authority與其 axiom依賴相關。

令 theorem：

\[
T.
\]

proof assistant可輸出：

\[
\operatorname{Axioms}(T).
\]

runtime應保存：

\[
A_T.
\]

若：

\[
A_T
\not\subseteq
A_{\rm allowed},
\]

則不能獲得預期 formal authority。

---

# 37. Cross-Kernel Replication

如果相同 theorem經：

\[
\mathsf{LeanVerified}
\]

與：

\[
\mathsf{CoqVerified},
\]

且 translation certificates互相對齊：

\[
T
\leftrightarrow
O_{\rm Lean},
\]

\[
T
\leftrightarrow
O_{\rm Coq},
\]

可以增加：

\[
\boxed{
\mathsf{CROSS\_KERNEL\_FORMAL\_REPLICATION}.
}
\]

---

# 38. Cross-Kernel 不代表 Absolute Truth

即使：

\[
\text{Lean}
+
\text{Coq}
\]

都驗證，

仍然只表示：

> bounded theorem在兩套 formalization/kernel中被驗證。

不能自動得到：

\[
\text{parent theorem}.
\]

因此：

\[
\boxed{
\mathsf{CrossKernel}
\neq
\mathsf{ParentClosure}.
}
\]

---

# 39. Formal Workbench as Adapter

外部 formal workbench可以扮演：

\[
\boxed{
\text{Research Runtime}
\leftrightarrow
\text{Formal Kernel}
}
\]

之間的 adapter。

它負責：

- prover invocation；
- provenance；
- binary identity；
- obligation identity；
- axiom audit；
- certificate recovery。

research runtime則保留 closure authority。

---

# 40. Separation of Responsibilities

因此合理分層是：

\[
\boxed{
\text{Research Runtime}
=
\text{Mathematical State Authority}
}
\]

\[
\boxed{
\text{Formal Workbench}
=
\text{Verification Execution Authority}
}
\]

\[
\boxed{
\text{Lean/Coq Kernel}
=
\text{Formal Proof Checking Authority}.
}
\]

---

# 41. Formal Workbench 不決定 Parent Closure

即使 formal workbench回傳：

\[
\mathrm{VERIFIED},
\]

它也不應知道：

> 此 theorem是否足以解決整個 research problem。

這是 research graph的責任。

因此：

\[
\boxed{
\text{Kernel Authority}
\neq
\text{Research Closure Authority}.
}
\]

---

# 42. Parent Propagation Runtime

當 child theorem更新後：

\[
C_i
\to
\mathrm{FORMAL\_PROOF},
\]

runtime重新計算 parent rules。

例如：

\[
P
\Leftarrow
C_1\land C_2.
\]

只有：

\[
C_1^+
\land
C_2^+
\]

且 scope/debt合法，

才能更新：

\[
P.
\]

---

# 43. Closure Reconstruction

每次重要 state mutation後，可以執行：

\[
\mathsf{RecomputeClosure}.
\]

流程：

\[
\text{State Update}
\to
\text{Dependency Propagation}
\to
\text{Obstruction Propagation}
\to
\text{Survivor Reconstruction}
\to
\text{Frontier Reconstruction}
\to
\text{Parent Closure Audit}.
\]

---

# 44. ClosureAudit

定義：

\[
\mathsf{ClosureAudit}(Q).
\]

檢查：

1. route inventory；
2. quotient completeness；
3. obstruction cover；
4. survivor region；
5. scope consistency；
6. proof debt；
7. certificate authority；
8. parent propagation rules。

---

# 45. Closure Audit 的輸出

不能只回：

```text id="oyho8o"
PASS
```

應回：

\[
\mathsf{ClosureReport}
=
\langle
status,
scope,
coverage,
debt,
survivors,
frontier,
authority
\rangle.
\]

---

# 46. Relative Closure in Runtime

如果所有 admissible routes已處理：

\[
\mathsf{RelativeClosure}.
\]

但報告必須附：

\[
\Xi=
(D,\Theta,\mathcal A,R,N,H).
\]

即：

\[
\boxed{
\text{Closure Without Context}
\text{ Is Invalid}.
}
\]

---

# 47. Reopening Runtime

新事件：

\[
e_{\rm new}
\]

可能使：

\[
\mathsf{Applicable}(O)
\]

失效。

runtime應自動檢查 dependent blocked routes。

若成立：

\[
R:
\mathrm{BLOCKED}
\to
\mathrm{REOPENED}.
\]

---

# 48. Reopening Is Not a Failure

在 dynamic research runtime中：

\[
\boxed{
\text{Reopening}
\neq
\text{System Error}.
}
\]

它是知識演進的正常狀態轉換。

真正錯誤是：

> 新證據出現後，舊 closure仍被無條件保留。

---

# 49. Historical Replay

可以重建任意時間：

\[
\mathfrak M_t.
\]

因此能回答：

> 為什麼當時我們認為這條 route blocked？

> 哪個 theorem後來使它 reopening？

這使研究歷史從 narrative轉成 machine-queryable provenance。

---

# 50. Reproducible Research State

傳統 reproducibility通常要求：

> 重跑實驗得到相同結果。

MRSM進一步要求：

\[
\boxed{
\text{Rebuild research state from ledger}.
}
\]

也就是：

\[
\mathsf{Replay}
(
L_{\le t}
)
=
\mathfrak M_t.
\]

---

# 51. Research State Snapshot

可定期保存：

\[
S_t.
\]

但 snapshot只是 cache。

canonical source仍然是：

\[
L.
\]

因此：

\[
\boxed{
\text{Snapshot}
\neq
\text{Canonical History}.
}
\]

---

# 52. Runtime Schema Evolution

研究 runtime本身也會升版。

例如：

\[
S^{(v1)}
\to
S^{(v2)}.
\]

schema migration不能要求：

\[
H(S^{(v1)})
=
H(S^{(v2)}),
\]

因為 serializer可能增加新欄位。

正確要求是：

\[
\boxed{
\mathsf{Migrate}(S^{(v1)})
=
\mathsf{Replay}_{v2}(L).
}
\]

---

# 53. Historical Evidence

舊 release evidence應 frozen。

新 runtime不應每次重新製造舊歷史。

因此：

\[
\boxed{
\text{Historical Validation}
=
\text{Validate Frozen Evidence},
}
\]

而不是：

\[
\text{Re-run Entire Historical Research}.
\]

---

# 54. AI Memory

長期 AI research需要：

\[
\text{persistent memory}.
\]

但真正 canonical memory不應只是 embedding database。

應該區分：

\[
\boxed{
\text{Retrieval Memory}
}
\]

與：

\[
\boxed{
\text{Mathematical State}.
}
\]

embedding適合找資料；

它不應決定 theorem status。

---

# 55. Vector Similarity Firewall

如果：

\[
\operatorname{sim}(A,B)\approx1,
\]

不能得到：

\[
A=B.
\]

因此：

\[
\boxed{
\text{Vector Similarity}
\neq
\text{Mathematical Identity}.
}
\]

AI retrieval只能產生 candidate relation。

---

# 56. Language Model Firewall

LLM可根據語言推斷：

> 這似乎是 no-go theorem。

但 native state只能記：

\[
\mathsf{NoGoCandidate}.
\]

直到 audit完成。

因此：

\[
\boxed{
\text{Language Confidence}
\neq
\text{Mathematical Authority}.
}
\]

---

# 57. AI Hallucination as State-Safety Problem

如果 AI hallucinate一條 theorem，

只要它停留在 proposal layer：

\[
\mathsf{Candidate}.
\]

native state不受污染。

因此 hallucination不只是 model quality問題。

也可以透過：

\[
\boxed{
\text{Runtime Authority Separation}
}
\]

降低傷害。

---

# 58. Adversarial Agent

multi-agent system中可以專門設：

\[
\mathcal A_{\rm adversarial}.
\]

任務：

- 尋找 scope inflation；
- 找 hidden assumptions；
- 找 invalid quotient；
- 找 transfer mismatch；
- 找 parent leakage；
- 尋找 counterexample。

---

# 59. Consensus 不等於 Proof

即使：

\[
10
\]

個 AI agent都同意：

\[
P,
\]

也只能提高：

\[
\text{research confidence}.
\]

不能增加：

\[
\text{formal authority}.
\]

因此：

\[
\boxed{
\text{Agent Consensus}
\neq
\text{Mathematical Proof}.
}
\]

---

# 60. Autonomous Research Loop

一個完整 autonomous loop可以寫成：

\[
\boxed{
\mathsf{Observe}
\to
\mathsf{SelectFrontier}
\to
\mathsf{Generate}
\to
\mathsf{Test}
\to
\mathsf{Audit}
\to
\mathsf{Commit}
\to
\mathsf{Recompute}
}
\]

然後重複。

---

# 61. Loop Termination

AI loop不能因：

> 沒想到下一步

就宣告：

\[
\mathsf{ProblemClosed}.
\]

合理輸出應是：

\[
\mathsf{FrontierSearchExhausted}_{\rm current}.
\]

因此：

\[
\boxed{
\text{Agent Search Exhausted}
\neq
\text{Mathematical Space Exhausted}.
}
\]

---

# 62. Research Cycle Boundary

每一輪 autonomous research可定義：

\[
C_i.
\]

cycle完成只意味：

\[
\mathsf{CycleClosed}(C_i).
\]

問題本身：

\[
Q
\]

可以繼續：

\[
\mathrm{OPEN}.
\]

---

# 63. Resource-Aware Mathematics

AI research runtime還可考慮：

- compute；
- time；
- formalization cost；
- literature cost；
- expected information gain。

因此：

\[
\mathsf{Schedule}
\]

可以成為 computational research optimization問題。

---

# 64. Expected Closure Gain

可定義研究行動 \(a\) 的：

\[
\operatorname{ECG}(a)
=
\mathbb E[
\Delta
\operatorname{ClosureInformation}
].
\]

用於比較：

> 是先 formalize這個 theorem，

還是搜尋另一個 obstruction？

---

# 65. AI Research Economics

在大型 proof space中，全部 routes都深入到底是不合理的。

需要：

\[
\boxed{
\text{Search Budget Allocation}.
}
\]

因此 mathematical research runtime也涉及資源配置。

---

# 66. Human Role

AI-native不表示人類退出。

人類尤其適合：

- redefining problem；
- inventing representation；
- recognizing deep analogy；
- selecting valuable research direction；
- evaluating meaning；
- changing admissibility policy。

AI則適合：

- large-state maintenance；
- dependency tracking；
- literature integration；
- replay；
- exhaustive local checking；
- route bookkeeping。

---

# 67. Human-AI Division

可概括為：

\[
\boxed{
\text{Human}
=
\text{High-Level Mathematical Reframing}
}
\]

\[
\boxed{
\text{AI}
=
\text{Large-Scale Research-State Operations}.
}
\]

實際系統中兩者可以重疊。

---

# 68. Research Runtime 不取代論文

paper仍然重要。

但 paper變成：

\[
\Pi_{\rm human}(
\mathfrak M
).
\]

也就是 human-readable projection。

canonical research state則可以比 paper更完整。

---

# 69. Future Mathematical Publication

未來一個 theorem release可能同時包含：

\[
\boxed{
\text{Paper}
+
\text{Research Graph}
+
\text{Ledger}
+
\text{Certificates}
+
\text{Formal Proof}
+
\text{Replay Manifest}.
}
\]

這比單一 PDF具有更高可驗證性。

---

# 70. Living Mathematical Publication

研究空間會持續演進。

因此 publication可以是：

\[
\mathfrak M_{t_1},
\mathfrak M_{t_2},
\ldots
\]

的一系列 signed/frozen releases。

這形成：

\[
\boxed{
\text{Versioned Mathematics}.
}
\]

---

# 71. Versioned Mathematics 不代表 Truth Is Relative

versioned指的是：

\[
\text{our encoded knowledge state}
\]

會改變。

不是：

\[
\text{mathematical truth itself}
\]

隨版本改變。

因此：

\[
\boxed{
\text{Epistemic State Evolves}
\neq
\text{Truth Becomes Relative}.
}
\]

---

# 72. Reference Runtime Architecture

一個最小 MRSM runtime可分：

```text id="gyr6px"
Corpus Layer
    ↓
Candidate Layer
    ↓
Review Layer
    ↓
Native Mathematical State
    ↓
Independent Verification Layer
    ↓
Formalization Layer
    ↓
Formal Backend Layer
    ↓
Kernel Verification
    ↓
Authority Import Gate
    ↓
Closure Reconstruction
```

---

# 73. Corpus Layer

負責：

- paper；
- books；
- formal repositories；
- experiments；
- computational results。

只提供 source artifacts。

不具有 native authority。

---

# 74. Review Layer

負責：

- statement extraction；
- source fidelity；
- scope；
- assumptions；
- nonclaims；
- candidate classification。

---

# 75. Native Layer

負責：

- stable identity；
- typed graph；
- statuses；
- authority；
- debts；
- certificates；
- history。

---

# 76. Verification Layer

可以包含：

\[
\text{symbolic},
\]

\[
\text{exact arithmetic},
\]

\[
\text{independent implementation},
\]

\[
\text{numerical enclosure},
\]

\[
\text{external theorem audit}.
\]

---

# 77. Formal Layer

負責：

\[
\text{FIR}
\to
\text{formal obligation}
\to
\text{kernel}.
\]

它是 high-authority validation layer。

但不是 research graph本身。

---

# 78. Closure Layer

負責：

- route coverage；
- obstruction cover；
- survivor set；
- frontier；
- relative closure；
- parent propagation。

---

# 79. Minimal Runtime Invariants

一個 MRSM runtime至少應保證：

1. Candidate ≠ Native State；
2. Status ≠ Authority；
3. Scope不能無證擴張；
4. Debt不能無證消失；
5. Runtime success ≠ theorem proof；
6. Formal proof只對 exact obligation有效；
7. Child authority不自動傳 parent；
8. replay必須 deterministic；
9. evidence identity應 content-addressed；
10. unknown時 fail closed。

---

# 80. Conformance Testing

runtime可以有 conformance suite。

例如：

\[
\mathsf{C01}:
\text{BLOCKED cannot imply CLOSED}^{-},
\]

\[
\mathsf{C02}:
\text{AUDIT cannot auto-upgrade to PROOF},
\]

\[
\mathsf{C03}:
\text{FORMAL\_PROOF requires kernel evidence},
\]

\[
\mathsf{C04}:
\text{scope mismatch rejects promotion}.
\]

---

# 81. Fault Injection

還應故意測：

- corrupted certificate；
- missing theorem；
- wrong scope；
- fake checker；
- modified obligation；
- empty axiom audit；
- replay mismatch；
- stale external theorem。

因為：

\[
\boxed{
\text{A verifier that only saw passing input has not been tested enough}.
}
\]

---

# 82. Mathematical Runtime Security

這類系統不只是軟體安全。

還有：

\[
\boxed{
\textbf{Epistemic Security}.
}
\]

它要防止：

- proof laundering；
- authority inflation；
- scope laundering；
- hidden assumptions；
- false equivalence；
- stale certificate reuse。

---

# 83. Proof Laundering

若 source-internal claim：

\[
\mathrm{AUDIT}
\]

經過多層格式轉換後，被錯誤標成：

\[
\mathrm{PROOF},
\]

稱：

\[
\boxed{
\mathsf{ProofLaundering}.
}
\]

runtime應保存完整 lineage避免此事。

---

# 84. Formalization Laundering

若：

\[
P
\]

被錯翻成容易證明的：

\[
P',
\]

而 kernel成功後回寫成：

\[
P
\text{ proved},
\]

則是：

\[
\boxed{
\mathsf{FormalizationLaundering}.
}
\]

Translation Certificate就是為了阻止這件事。

---

# 85. Stale Authority

若 external theorem被修正，

依賴它的 assets應重新 audit。

因此 runtime需要：

\[
\mathsf{DependencyInvalidation}.
\]

這使 mathematical knowledge具有 dependency-aware maintenance能力。

---

# 86. AI-Native Reaudit

AI可以定期：

\[
\mathsf{Reaudit}
(
\mathfrak M
).
\]

搜尋：

- stale references；
- superseded theorem；
- broken external links；
- changed formal dependencies；
- stronger new results。

---

# 87. Continuous Mathematical Integration

可以借用 software engineering的 CI概念。

每次 state update後跑：

\[
\boxed{
\text{Mathematical CI}.
}
\]

包括：

- replay；
- conformance；
- dependency audit；
- certificate verification；
- formal checks；
- closure recomputation。

---

# 88. Continuous Formal Verification

如果 theorem formal artifact更新：

\[
O_t
\to
O_{t+1},
\]

formal backend重新檢查。

因此：

\[
\boxed{
\text{Formal Proof}
\text{ 可以成為持續可重驗 artifact}.
}
\]

---

# 89. AI-Native Mathematics 與傳統 ATP

Automated Theorem Proving主要探索：

\[
\text{proof state}
\to
\text{proof state}.
\]

MRSM runtime探索：

\[
\boxed{
\text{research-space state}
\to
\text{research-space state}.
}
\]

它在更高一層。

---

# 90. Meta-Proof Search

AI不只搜尋：

\[
\pi:
\Gamma\vdash P.
\]

還搜尋：

- 哪個 representation；
- 哪個 decomposition；
- 哪個 theorem family；
- 哪個 obstruction；
- 哪種 verifier；
- 哪條 formalization route。

因此是：

\[
\boxed{
\text{Search Over Proof-Search Architectures}.
}
\]

---

# 91. Research-Space Compression

隨研究進展：

\[
\mathcal S_0
\supset
\mathcal S_1
\supset
\cdots
\]

survivor space縮小。

這本身是一種可量化研究進展。

---

# 92. Progress Without Final Proof

即使：

\[
Q=\mathrm{OPEN},
\]

仍可以有：

\[
|\mathcal S_{t+1}|
\ll
|\mathcal S_t|.
\]

因此系統能辨識：

\[
\boxed{
\text{Structured Progress Without Final Closure}.
}
\]

---

# 93. Negative Knowledge as Asset

傳統研究中失敗 route常散落於文獻。

MRSM將它保存為：

\[
\boxed{
\text{Certified Negative Knowledge}.
}
\]

例如：

- impossible region；
- failed representation；
- scope-limited no-go；
- invalid transfer；
- dead quotient class。

---

# 94. Preventing Repeated Failure

AI runtime因此能回答：

> 這個 route過去是否已被證明失敗？

> 在什麼 scope？

> 失敗原因是否仍成立？

避免每一代 researcher重新走同樣死路。

---

# 95. Reopening Dead Ends

同時也不把歷史失敗永久封死。

如果前提變化：

\[
\mathsf{Reopen}.
\]

因此：

\[
\boxed{
\text{Remember Failure}
+
\text{Allow Legitimate Reopening}.
}
\]

---

# 96. Mathematical Research as Persistent Computation

從 runtime角度：

\[
\mathfrak M_t
\]

是一個持續演化 computation。

新 paper、新 theorem、新 formal proof都只是 input events。

因此可以寫：

\[
\boxed{
\mathfrak M_{t+1}
=
F(
\mathfrak M_t,
e_{t+1}
).
}
\]

---

# 97. Research Runtime as Cognitive Carrier

這引出一個更大的觀點。

過去 proof-space主要存在於：

\[
\text{researchers' brains}
+
\text{papers}.
\]

其可維護規模受限於：

\[
\text{human cognition}.
\]

persistent runtime提供另一種 carrier。

---

# 98. Carrier Expansion

人類不必把全部：

\[
10^5
\]

個 states保持在工作記憶。

可以由 runtime持有。

人類只讀取當前：

\[
\Pi_{\rm relevant}(
\mathfrak M
).
\]

因此：

\[
\boxed{
\text{Cognitive Capacity}
\text{ can be externally extended}.
}
\]

---

# 99. AI as Global Research-Space Attention

AI可以持續查詢整個 research state。

其真正優勢可能不是單步推理速度。

而是：

\[
\boxed{
\textbf{Global Attention over Persistent Mathematical State}.
}
\]

這在人類研究中極難長期維持。

---

# 100. 從數學助手到研究空間管理者

因此未來 AI mathematician的角色可以從：

> 幫我證這個 lemma。

升成：

> 維護這個問題的完整 proof landscape。

它持續：

- 收新文獻；
- 更新 graph；
- 驗證 claims；
- 找 frontier；
- 發現 route；
- 重新 formalize；
- 管理 proof debt；
- 做 closure audit。

---

# 101. 人類第一次可能擁有完整 Research-Space Carrier

這或許是 AI mathematics真正深遠的改變之一。

不是：

\[
\boxed{
\text{AI 終於可以像人一樣寫證明。}
}
\]

而是：

\[
\boxed{
\textbf{數學第一次可能擁有足以長期承載整個研究空間的計算載體。}
}
\]

---

# 102. 系列總結：四層 MRSM

整個 MRSM 系列形成四層。

---

## Paper 00 — Ontology / Methodology

回答：

\[
\boxed{
\text{為什麼要把研究過程物件化？}
}
\]

---

## Paper 01 — Geometry / Topology

回答：

\[
\boxed{
\text{證明空間長什麼樣？}
}
\]

---

## Paper 02 — Calculus / Authority

回答：

\[
\boxed{
\text{證明空間裡允許發生什麼？}
}
\]

---

## Paper 03 — Runtime / AI / Formal Verification

回答：

\[
\boxed{
\text{如何讓整個系統真正執行？}
}
\]

---

# 103. MRSM 的整體鏈

四篇合起來：

\[
\boxed{
\text{Research Process}
\to
\text{Research Object}
\to
\text{Proof Space}
\to
\text{Closure Calculus}
\to
\text{Executable Runtime}.
}
\]

---

# 104. 一個完整的 AI-Native Mathematical Pipeline

可以壓縮成：

\[
\boxed{
\begin{aligned}
\text{Corpus}
&\to
\text{Candidate}\\
&\to
\text{Typed Research Graph}\\
&\to
\text{Audit}\\
&\to
\text{Independent Verification}\\
&\to
\text{Formalization}\\
&\to
\text{Kernel Verification}\\
&\to
\text{Authority Import}\\
&\to
\text{Frontier Reconstruction}\\
&\to
\text{Closure Audit}.
\end{aligned}
}
\]

---

# 105. MRSM 不聲稱什麼

MRSM 不聲稱：

\[
\boxed{
\text{把研究畫成圖就能解決未解問題。}
}
\]

也不聲稱：

\[
\boxed{
\text{AI + database 就能取代新數學。}
}
\]

它解決的是另一層問題：

\[
\boxed{
\text{如何更精確地表示、維護、搜尋與驗證大型數學研究空間。}
}
\]

---

# 106. 方法的終極限制

即使 runtime完美，

仍可能存在：

\[
R^\ast
\notin
\Omega^{\rm obs}.
\]

也就是：

> 真正關鍵的新想法根本尚未被任何人或 AI 發現。

因此：

\[
\boxed{
\text{Perfect Research-State Management}
\neq
\text{Guaranteed Mathematical Discovery}.
}
\]

---

# 107. 但 Representational Improvement 仍然重要

因為即使無法保證 discovery，

降低：

- 重複研究；
- scope confusion；
- false closure；
- hidden debt；
- authority inflation；

本身就可以大幅提升大型研究問題的可處理性。

---

# 108. 從認知問題到系統問題

過去大量研究狀態依賴：

\[
\text{researcher's memory}.
\]

MRSM試圖將它轉化為：

\[
\boxed{
\text{explicit system state}.
}
\]

因此部分原本屬於「研究者是否記得」的問題，

變成：

\[
\text{runtime invariant}.
\]

---

# 109. 數學研究的軟體化，但不是把數學變成軟體

MRSM借用：

- event sourcing；
- versioning；
- typed state；
- CI；
- dependency tracking。

但這不表示數學真理由軟體定義。

恰好相反。

這些工程機制只是為了更嚴格地保存：

\[
\boxed{
\text{我們對數學知道什麼，以及為什麼相信它。}
}
\]

---

# 110. 結論

本文完成 Mathematical Research Space Methodology 系列的 runtime層。

核心架構為：

\[
\boxed{
L_0
=
\text{Canonical Event Ledger},
}
\]

\[
\boxed{
L_1
=
\text{Native Mathematical Research State},
}
\]

\[
\boxed{
L_2
=
\text{Human / AI / Formal Views}.
}
\]

其中 AI不是 canonical truth writer。

AI是：

\[
\boxed{
\text{Research-Space Operator}.
}
\]

它可以：

\[
\mathsf{Observe},
\]

\[
\mathsf{Generate},
\]

\[
\mathsf{Search},
\]

\[
\mathsf{Formalize},
\]

\[
\mathsf{Audit},
\]

但 high-authority mutation必須通過：

\[
\boxed{
\text{Candidate Gate}
+
\text{Certificate Gate}
+
\text{Scope Gate}
+
\text{Authority Gate}
+
\text{Parent Propagation Gate}.
}
\]

形式驗證器則提供：

\[
\boxed{
\text{bounded high-authority mathematical verification}.
}
\]

而 research runtime負責：

\[
\boxed{
\text{全域研究狀態與 closure semantics}.
}
\]

兩者不可坍縮。

因此最終的 AI-native mathematical system不是：

\[
\boxed{
\text{LLM}
\to
\text{answer}.
}
\]

而是：

\[
\boxed{
\text{Human}
+
\text{AI Agents}
+
\text{Persistent Research Runtime}
+
\text{Formal Kernels}
\leftrightarrow
\text{Dynamic Mathematical Research Space}.
}
\]

從這個角度看，AI 對數學最深遠的影響或許不只是自動生成證明。

真正重要的轉變可能是：

\[
\boxed{
\textbf{數學研究第一次開始具有一個比單一人類工作記憶更大的持久認知載體。}
}
\]

在此之前，一個大型 proof landscape 必須分散存在於：

- 數百名研究者；
- 數千篇論文；
- 不同 notation；
- 個人筆記；
- 未公開失敗路線；
- 社群默契。

而在 AI-native runtime 中，它可以逐漸成為：

\[
\boxed{
\textbf{一個可查詢、可重播、可驗證、可更新、可重新閉包的正式研究空間。}
}
\]

因此 MRSM 的最終主張並不是：

> 數學研究應該被 AI 自動化。

而是：

\[
\boxed{
\textbf{數學研究本身應該擁有一個與其複雜度相匹配的正式認知載體。}
}
\]

AI、圖資料庫、形式驗證器、symbolic engine 與長期記憶系統共同出現後，這個載體第一次具有實際工程可行性。

數學因此可能從：

\[
\boxed{
\text{以論文為主要載體的研究文明}
}
\]

逐步進入：

\[
\boxed{
\textbf{以動態研究空間為主要狀態、以論文與形式證明為不同投影的研究文明。}
}
\]

這也構成 Mathematical Research Space Methodology 的完整閉環：

\[
\boxed{
\text{研究}
\to
\text{空間}
\to
\text{演算}
\to
\text{Runtime}
\to
\text{新的研究}.
}
\]