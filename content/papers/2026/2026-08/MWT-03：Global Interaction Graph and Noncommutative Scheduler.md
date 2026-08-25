# MWT-03：Global Interaction Graph and Noncommutative Scheduler
## 全域交互圖、部分序、條件交換、分支壓縮、多 AI 執行與穩定世界提交

**英文題名：** *MWT-03: Global Interaction Graph and Noncommutative Scheduler — Partial Orders, Conditional Commutation, Branch Reduction, Multi-AI Execution, and Stable-World Commit*  
**系列：** Mathematical World Theory（MWT）  
**篇次：** 03  
**文件編號：** EML-MWT-03-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-18  
**版本：** v0.1  
**文件性質：** 數學世界論第三篇形式母稿／AI-native global scheduler／noncommutative execution theory  
**前置文件：** MWT-01、MWT-02  
**狀態：** 可使用研究稿；提供 reference scheduler；尚不宣稱最優排程或一般分支爆炸問題已解決  

---

## 摘要

MWT-01 將可操作數學建立為 heterogeneous presentation graph；MWT-02 進一步建立 Global Legality Calculus，使跨 presentation interaction 在執行前必須經過 Legal、Illegal、Undetermined、Conflicted 四態判定。由此得到一族已通過 commit-level legality 的 interactions：

$$
\mathcal I_t^+
=
\{
\alpha_1,\ldots,\alpha_n
\}.
$$

然而：

$$
\alpha_i\in\mathcal I_t^+
$$

只表示「目前有資格執行」，不表示它們可以任意排序、同時執行或合併。當多個合法 interaction 共享 state、依賴彼此產物、消耗共同資源、破壞對方 precondition、具有路徑依賴或滿足：

$$
A\circ B
\neq
B\circ A,
$$

則執行順序本身就是數學內容。

本文提出 **Global Interaction Graph（GIG）** 與 **Noncommutative Scheduler（NCS）**，作為 MWT 從「合法交互集合」走向「可執行世界演化」的第三層。核心不是把所有事件強制排列成單一 total order，而是保存：

$$
\boxed{
\text{partial order}
+
\text{conditional independence}
+
\text{noncommutative branches}
+
\text{transactional commit}.
}
$$

令穩定世界運行狀態為：

$$
\mathfrak W_t.
$$

當前全域交互圖定義為：

$$
\boxed{
\mathcal G_t^I
=
(
V_t,
E_t^{\mathrm{dep}},
E_t^{\mathrm{ord}},
E_t^{\mathrm{conf}},
E_t^{\mathrm{bridge}},
E_t^{\mathrm{inv}},
E_t^{\mathrm{res}}
).
}
$$

其中 $V_t$ 包含已合法 interaction 與必要的 state / certificate nodes；各 edge family 分別記錄依賴、順序、衝突、bridge、invariant 與 resource 關係。真正可在下一個 scheduling epoch 執行的集合不是全部 $\mathcal I_t^+$，而是 **dynamic frontier**：

$$
\boxed{
\mathcal F_t
=
\{
\alpha\in\mathcal I_t^+:
\operatorname{Pred}(\alpha)
\subseteq
\operatorname{Committed}_t
\land
\operatorname{FreshLegal}_t(\alpha)
\}.
}
$$

本文進一步定義 **contextual independence**。兩個 actions $A,B$ 只有在目前 state/context $\Gamma_t$ 下同時滿足：

1. 無未滿足依賴；
2. 沒有不可並行 resource conflict；
3. pre/post condition 相容；
4. 存在指定 identity / invariant 下的交換或合流證書；
5. 兩種順序皆保持 legality；

才允許寫：

$$
\boxed{
A
\mathrel{\mathsf{Ind}_{\Gamma_t,\mathfrak I}}
B.
}
$$

因此 independent 不是永久 operator property，而可以是 state-dependent、domain-dependent、identity-dependent 與 version-dependent。

若存在：

$$
C_{A,B}^{\mathrm{comm}}
$$

證明：

$$
B\circ A
\equiv_{\mathfrak I}
A\circ B
$$

於指定 domain 成立，則 scheduler 可以將兩個 interleavings 視為同一 **schedule equivalence class** 的代表，而不必兩條都完整執行。本文以 Mazurkiewicz-trace／partial-order-reduction 精神作成熟外部參照，但將交換關係改成 MWT 所需的動態、帶合法性與 identity specification 的 contextual swap relation：

$$
\gamma
\leftrightsquigarrow_{\Gamma,\mathfrak I}
\gamma'.
$$

其反身對稱傳遞閉包寫為：

$$
\boxed{
\gamma
\approx_{\Gamma,\mathfrak I}
\gamma'.
}
$$

這使 MWT 能在不刪除真正非交換差異的前提下壓縮大量純排序冗餘。

若 $A,B$ 均 Legal，但：

$$
A
\not\mathsf{Ind}
B,
$$

且兩種順序皆有研究價值，NCS 不強迫選一條，而建立 branch：

$$
\mathfrak W_t
\rightarrow
\mathfrak W_{t+1}^{A\prec B}
$$

與：

$$
\mathfrak W_t
\rightarrow
\mathfrak W_{t+1}^{B\prec A}.
$$

分支不是錯誤；真正問題是分支數量可能爆炸。本文因此加入 **branch budget、equivalence quotient、dominance pruning、invariant witness、state hash、causal provenance、research relevance** 等 branch-control 機制。其目標不是保證一般情形多項式可解，而是在有限 runtime budget 下盡可能保留「有數學差異的路徑」，刪除「只有可證交換重排差異的路徑」。

在 multi-AI 執行上，本文引入 logical event order：

$$
e_i
\prec_H
e_j,
$$

只記錄可證 causal precedence；無 causal relation 的 events 不需要被虛構成「誰真正先發生」。總順序只在 commit log、deterministic replay 或特定 backend 需要時由額外 tie-break layer 提供。這使 MWT 與分散系統中的 happened-before 部分序精神一致。

本文最後定義 **stable-world commit**。一批並行或分支 interactions 不因「都跑完」就可寫入 canonical world state。提交前必須存在 batch certificate：

$$
C_B^{\mathrm{commit}},
$$

證明該 batch 相對指定 identity / invariant contract，至少滿足其中一種：

1. serializable；
2. pairwise / globally commuting；
3. confluent；
4. explicitly merged by a certified merge operator。

否則只能保留 staging branches。

MWT-03 因此把「全域計算」從抽象口號推進為具體 operational thesis：

$$
\boxed{
\text{全域}
\neq
\text{全部同步}
\neq
\text{唯一順序}
\neq
\text{暴力枚舉全部 interleavings}.
}
$$

更準確地：

$$
\boxed{
\text{Global Mathematical Execution}
=
\text{legal partial-order orchestration}
+
\text{certified commutation}
+
\text{necessary branching}
+
\text{transactional convergence}.
}
$$

**關鍵詞：** Mathematical World Theory、Global Interaction Graph、noncommutative scheduler、partial order、Mazurkiewicz trace、DPOR、serializability、confluence、branch reduction、multi-AI、transaction、stable-world commit

---

# 0. 本文的責任：合法不等於現在就能一起算

MWT-02 給出：

$$
\mathcal I_t^+.
$$

但：

$$
\boxed{
\alpha,\beta
\in
\mathcal I_t^+
}
$$

只回答：

> 它們各自目前有資格成為候選執行。

仍未回答：

- 誰必須先？
- 能不能同時？
- 是否共享輸入？
- 是否共享可變 state？
- 是否消耗同一 resource？
- 是否交換？
- 是否只在部分 domain 交換？
- 如果不交換，要保留幾種順序？
- 如果跑出兩個結果，能不能 merge？
- 哪個結果可以進 stable world？

因此本文研究的不是：

$$
\mathsf{CanAct}(\alpha).
$$

而是：

$$
\boxed{
\mathsf{HowToOrderAndCommit}
(
\mathcal I_t^+
).
}
$$

---

# 1. 全域不等於 Total Order

最簡單 scheduler 會把 actions 排成：

$$
\alpha_1
\prec
\alpha_2
\prec
\cdots
\prec
\alpha_n.
$$

這當然可執行。

但它可能把本來可以同時或任意交換的事件全部人工序列化，造成：

- 不必要等待；
- 不必要因果；
- 假歷史；
- AI parallelism 浪費；
- branch semantics 消失。

MWT-03 因此採：

$$
\boxed{
\text{partial order first}.
}
$$

只有真正需要比較順序的 interaction pairs 才加入 precedence relation。

---

# 2. Interaction Event

定義一個 execution event：

$$
\boxed{
e
=
(
\alpha,
S_{\mathrm{pre}},
\Gamma,
C_{\alpha},
a,
\tau
).
}
$$

其中：

- $\alpha$：interaction；
- $S_{\mathrm{pre}}$：執行前 state；
- $\Gamma$：context；
- $C_{\alpha}$：legality certificate；
- $a$：executing agent / AI；
- $\tau$：logical event metadata。

event 不是 operator 本身。

同一 operator 的兩次執行是兩個 events。

---

# 3. Global Interaction Graph

在 epoch $t$，定義：

$$
\boxed{
\mathcal G_t^I
=
(
V_t,
E_t^{\mathrm{dep}},
E_t^{\mathrm{ord}},
E_t^{\mathrm{conf}},
E_t^{\mathrm{bridge}},
E_t^{\mathrm{inv}},
E_t^{\mathrm{res}}
).
}
$$

不同 edge family 不應全部壓成一種 generic edge。

因為：

$$
\text{dependency}
\neq
\text{conflict}
\neq
\text{resource sharing}
\neq
\text{invariant coupling}.
$$

---

# 4. Dependency Edge

若：

$$
\beta
$$

需要：

$$
\alpha
$$

的輸出、certificate、state update 或 bridge result，

寫：

$$
\boxed{
\alpha
\rightarrow_{\mathrm{dep}}
\beta.
}
$$

此 edge 建立 hard precedence：

$$
\alpha
\prec
\beta.
$$

但 precedence 不必等於 dependency 的唯一來源。

---

# 5. Order Edge

有些 actions 不直接資料依賴，但 ruleset 明示：

$$
\boxed{
\alpha
\rightarrow_{\mathrm{ord}}
\beta.
}
$$

例如：

- initialize before use；
- validate before commit；
- acquire before release；
- prove precondition before invoking theorem bridge。

這是一種 protocol / legality order。

---

# 6. Conflict Edge

若兩個 interactions：

$$
\alpha,\beta
$$

不能在同一 staging context 內無協調並行，

寫：

$$
\boxed{
\alpha
\leftrightarrow_{\mathrm{conf}}
\beta.
}
$$

conflict 可以來自：

- write/write；
- read/write；
- incompatible bridge；
- shared non-reentrant operator；
- identity conflict；
- competing constraint；
- mutually exclusive branch。

conflict edge 本身不決定誰先。

它只表示需要 scheduler 做額外決策。

---

# 7. Resource Edge

若：

$$
\alpha,\beta
$$

競爭有限 resource：

$$
r,
$$

可記：

$$
\alpha
\leftrightarrow_{\mathrm{res}(r)}
\beta.
$$

resource conflict 與 mathematical noncommutativity 不同。

兩個算子數學上交換，也可能因 GPU memory 不足而不能同時跑。

---

# 8. Invariant Coupling Edge

若：

$$
\alpha
$$

和：

$$
\beta
$$

各自不破壞 invariant $I$，

但並行組合是否保持 $I$ 尚未知，

寫：

$$
\boxed{
\alpha
\leftrightarrow_{\mathrm{inv}(I)}
\beta.
}
$$

在獲得 joint certificate 前，不視為 independent。

---

# 9. Bridge Edge

跨 presentation interaction 可能共享或依賴同一 bridge：

$$
b.
$$

若 bridge state/version 會被 action 影響，則：

$$
\alpha
\leftrightarrow_{\mathrm{bridge}(b)}
\beta
$$

需要進 scheduler。

如果 bridge 是 immutable pure translation，則可能不形成 conflict。

---

# 10. Happens-Before

定義 MWT runtime 的 causal precedence：

$$
\boxed{
e_i
\prec_H
e_j
}
$$

若至少有以下一項：

1. 同一 agent program order；
2. $e_i$ 的 output 被 $e_j$ consume；
3. $e_i$ 的 certificate 被 $e_j$ 使用；
4. explicit dependency / order edge；
5. message / transport from $e_i$ enables $e_j$ ；
6. transitive closure。

因此：

$$
\prec_H
$$

是 partial order。

對無關事件：

$$
e_i
\not\prec_H e_j
$$

且：

$$
e_j
\not\prec_H e_i.
$$

MWT 不必替它們虛構唯一的「真實先後」。

---

# 11. Total Order 是後端工具，不是本體預設

某些用途需要：

$$
<_{T}
$$

total order，例如：

- append-only commit log；
- deterministic replay；
- database storage；
- UI timeline。

可以選擇一個 extension：

$$
\boxed{
\prec_H
\subseteq
<_{T}.
}
$$

但：

$$
<_{T}
$$

新增的 tie-break relations 不自動升格成 causal relations。

因此：

$$
\boxed{
e_i <_T e_j
\not\Rightarrow
e_i\prec_H e_j.
}
$$

---

# 12. Enabled Interaction

一個 interaction：

$$
\alpha
$$

在 $t$ 可 enabled，至少需要：

$$
\operatorname{Pred}(\alpha)
\subseteq
\operatorname{Committed}_t.
$$

但還不夠。

因為 MWT-02 強調 dynamic legality。

所以還要求：

$$
\operatorname{FreshLegal}_t(\alpha)=1.
$$

---

# 13. Dynamic Frontier

定義：

$$
\boxed{
\mathcal F_t
=
\left\{
\alpha\in\mathcal I_t^+:
\operatorname{Pred}(\alpha)
\subseteq
\operatorname{Committed}_t
\land
\operatorname{FreshLegal}_t(\alpha)
\right\}.
}
$$

 $\mathcal F_t$ 是 scheduler 在當前 epoch 真正可選的 frontier。

它會隨 commit 動態改變。

---

# 14. Frontier 不是 Ready Queue 的永久快照

若：

$$
\alpha\in\mathcal F_t,
$$

另一 action $\beta$ commit 後可能使：

$$
\alpha\notin\mathcal F_{t+1}.
$$

例如：

- precondition 被改變；
- resource 被占用；
- certificate 被撤銷；
- bridge version 被更新；
- identity requirement 改變。

所以：

$$
\boxed{
\text{frontier must be recomputed or incrementally revalidated}.
}
$$

---

# 15. Independence Relation

傳統並行模型常定義靜態 independence relation。

MWT 需要更強的 contextual version：

$$
\boxed{
\mathsf{Ind}_{\Gamma,S,\mathfrak I}
(A,B).
}
$$

它不是 operator pair 的永久標籤。

---

# 16. Contextual Independence 的最低條件

MWT-03 v0.1 建議：

$$
\mathsf{Ind}_{\Gamma,S,\mathfrak I}(A,B)
$$

至少要求：

### I1 — Both Enabled

$$
A,B
\in
\mathcal F_t.
$$

### I2 — No Hard Dependency

$$
A
\not\rightarrow_{\mathrm{dep}}
B
$$

且：

$$
B
\not\rightarrow_{\mathrm{dep}}
A.
$$

### I3 — No Unresolved Resource Conflict

沒有未解：

$$
E^{\mathrm{res}}
$$

阻止並行。

### I4 — Both Orders Legal

$$
\mathsf{Legal}(B\circ A)
$$

且：

$$
\mathsf{Legal}(A\circ B).
$$

### I5 — Commutation / Confluence Contract

存在：

$$
C_{A,B}^{\mathrm{comm}}
$$

或相應 confluence certificate。

### I6 — Identity / Invariant Preservation

兩種順序對指定：

$$
\mathfrak I
$$

與：

$$
\mathcal Q_{\mathrm{inv}}
$$

等價。

---

# 17. Commutativity Is Relative

正式寫：

$$
\boxed{
B\circ A
\equiv_{\mathfrak I,\mathcal Q}
A\circ B.
}
$$

而不是永遠要求 syntactic equality。

因此兩個 actions 可以：

- final-state equivalent；
- history inequivalent；
- proof-trace inequivalent。

若 inquiry 需要 history，則不允許以 final-state commutativity 壓縮。

---

# 18. Strong Commutation

若：

$$
B(A(S))
=
A(B(S))
$$

且 intermediate legality、history obligations 與 invariants 全部相同，

稱：

$$
\boxed{
A
\mathrel{\mathsf{Comm}^{\mathrm{strong}}}
B.
}
$$

這是最強情形。

---

# 19. Identity-Relative Commutation

若：

$$
B(A(S))
\neq
A(B(S))
$$

但：

$$
B(A(S))
\equiv_{\mathfrak I}
A(B(S)),
$$

可以稱：

$$
\boxed{
A
\mathrel{\mathsf{Comm}^{\mathfrak I}}
B.
}
$$

例如 presentation 中保留不同 cache state，但 inquiry identity 不關心 cache。

---

# 20. Observational Commutation

對 observer $O$：

$$
\Pi_O(B(A(S)))
=
\Pi_O(A(B(S))),
$$

但完整 state 未必相等。

則：

$$
\boxed{
A
\mathrel{\mathsf{Comm}^{O}}
B.
}
$$

這只能支援 observer-relative schedule reduction。

不能直接升格成 World-level strong commutation。

---

# 21. Conditional Commutation Certificate

一個交換證書至少記：

$$
\boxed{
C_{A,B}^{\mathrm{comm}}
=
(
D,
\Gamma,
\mathfrak I,
\mathcal Q,
v,
\mathsf{proof}
).
}
$$

其中：

- $D$：valid domain；
- $\Gamma$：context；
- $\mathfrak I$：identity spec；
- $\mathcal Q$：preserved inquiries/invariants；
- $v$：version；
- $\mathsf{proof}$：proof/test/certificate。

超出 $D$ 不可 reuse。

---

# 22. Noncommutativity Certificate

同樣可以保存：

$$
\boxed{
C_{A,B}^{\mathrm{noncomm}}
}
$$

作為 witness：

$$
B(A(S))
\not\equiv_{\mathfrak I}
A(B(S)).
$$

一個 concrete witness 可以直接禁止 scheduler 把兩個 path quotient。

---

# 23. Schedule

定義一條 schedule：

$$
\boxed{
\gamma
=
(e_1,\ldots,e_n).
}
$$

schedule 必須尊重：

$$
\prec_H.
$$

即若：

$$
e_i\prec_H e_j,
$$

則 $e_i$ 必須在任何合法 linearization 中先於 $e_j$。

---

# 24. Linearization

對 partial order：

$$
(V,\prec_H),
$$

任何 compatible total order：

$$
L
$$

稱為 linearization。

不同 linearizations 不一定代表不同 mathematical behavior。

這正是後續 schedule quotient 的來源。

---

# 25. Adjacent Swap

設 schedule 中相鄰：

$$
\ldots,A,B,\ldots
$$

若在該 prefix state $S_k$：

$$
\mathsf{Ind}_{\Gamma_k,S_k,\mathfrak I}(A,B),
$$

允許：

$$
\boxed{
\ldots,A,B,\ldots
\leftrightsquigarrow
\ldots,B,A,\ldots
}
$$

這是一個合法 adjacent swap。

---

# 26. Contextual Trace Equivalence

令：

$$
\approx_{\Gamma,\mathfrak I}
$$

為合法 adjacent swaps 的反身、對稱、傳遞閉包。

如果：

$$
\gamma
\approx_{\Gamma,\mathfrak I}
\eta,
$$

則：

> 對指定 context、identity 與 inquiry contract，兩條 schedules 可以被視為同一 schedule class 的不同 linearizations。

這是 MWT 對 Mazurkiewicz-trace 精神的動態擴張。

---

# 27. 為什麼不是直接採固定 Mazurkiewicz Independence？

因為 MWT 中：

$$
\mathsf{Ind}
$$

可能依賴：

- state；
- bridge version；
- observer；
- identity；
- resource；
- legality；
- history。

因此：

$$
\boxed{
\mathsf{Ind}_t(A,B)
}
$$

今天成立，

明天可能失效。

MWT 需要 contextual trace relation，而不是單一靜態 alphabet independence table。

---

# 28. Schedule Quotient

若：

$$
[\gamma]
=
\{
\eta:
\eta\approx\gamma
\},
$$

則 scheduler 原則上只需要完整探索一個 representative：

$$
\operatorname{rep}([\gamma]),
$$

只要 equivalence certificate 仍有效。

這可以消除大量「只有交換次序不同」的冗餘 interleavings。

---

# 29. Reduction Soundness Obligation

任何 schedule reduction 都必須聲明保留哪個 inquiry family：

$$
\mathcal Q.
$$

不能只因 final state 相同，就刪掉：

- timing-sensitive query；
- provenance query；
- security audit；
- causal-history query。

因此：

$$
\boxed{
\text{trace reduction soundness is inquiry-relative}.
}
$$

---

# 30. Dynamic Partial-Order Reduction Interface

MWT 不重新發明 DPOR。

DPOR 的核心外部精神可概括為：

> 先探索某個 interleaving，再根據實際互動動態找出需要 backtrack 的位置，避免枚舉全部純冗餘 interleavings。

MWT-03 可以把 DPOR 類方法作為：

$$
\boxed{
\mathsf{ScheduleReductionBackend}.
}
$$

但 MWT 還要額外加入：

- cross-presentation legality；
- dynamic bridge；
- identity-relative equivalence；
- certificate maturity；
- multi-AI provenance。

---

# 31. Branch Trigger

當：

$$
A,B
\in
\mathcal F_t
$$

且：

$$
\neg
\mathsf{Ind}(A,B),
$$

不代表一定 branch。

先判定：

- 是否有 hard order？
- 是否其中一順序 illegal？
- 是否 inquiry 只需要一種 admissible witness？
- 是否另一順序可能產生不同 invariant？

只有具有 unresolved mathematical significance 時才進 branch candidate。

---

# 32. Two-Order Branch

若：

$$
\mathsf{Legal}(B\circ A)
$$

且：

$$
\mathsf{Legal}(A\circ B),
$$

並已有 noncommutativity witness 或尚未證明等價，

可以建立：

$$
\boxed{
\mathfrak W_t
\to
\begin{cases}
\mathfrak W_{t+1}^{A\prec B},\\
\mathfrak W_{t+1}^{B\prec A}.
\end{cases}
}
$$

這兩支共享 parent provenance。

---

# 33. Branch Identity

每一 branch：

$$
B_i
$$

至少記：

$$
\boxed{
B_i
=
(
\mathrm{id},
\mathrm{parent},
\gamma_i,
S_i,
\Gamma_i,
C_i,
Q_i
).
}
$$

其中：

- $\gamma_i$：path；
- $S_i$：state；
- $C_i$：certificates；
- $Q_i$：open obligations。

---

# 34. Branch 不是 World 分裂的形上學宣言

MWT branch 只表示：

> runtime 暫時保留多個合法 mathematical execution candidates。

它不自動主張：

$$
\boxed{
\text{physical many-worlds ontology}.
}
$$

更不表示每一個 speculative branch 都在現實存在。

這是計算結構，不是宇宙學主張。

---

# 35. Branch Explosion

若每一步都有兩種非交換順序：

$$
2^n
$$

分支很快不可承受。

所以：

$$
\boxed{
\text{保留所有可能路徑}
}
$$

不能是無條件 runtime policy。

MWT 需要 branch control。

---

# 36. Branch Budget

設定：

$$
\boxed{
B_{\mathrm{branch}}
}
$$

作為：

- branch count；
- compute；
- memory；
- depth；
- wall-clock；
- proof budget；

的限制。

超出後不偽裝已完整探索，而標：

$$
\boxed{
\mathsf{BranchCoverageIncomplete}.
}
$$

---

# 37. Branch Reduction 的五種主要來源

### R1 — Trace Equivalence

可證交換的 linearizations quotient。

### R2 — State / Identity Equivalence

兩支到達：

$$
S_i
\equiv_{\mathfrak I}
S_j.
$$

### R3 — Dominance

一支在 inquiry 上被另一支嚴格支配。

### R4 — Invariant Witness

若目標只是找反例，一旦 branch 已找到 witness，可停止部分搜尋。

### R5 — Resource / Relevance Pruning

低優先 branch 延後，而不是聲稱不存在。

---

# 38. State Hash 不等於 Identity

兩個 branches state hash：

$$
h(S_i)=h(S_j)
$$

可以作快速 dedup signal。

但 hash equality 只在 canonical serialization、collision assumptions 與 identity contract 下有意義。

MWT 不把 raw hash 當本體 identity。

---

# 39. Dominance

對 inquiry family：

$$
\mathcal Q
$$

若 branch $B_1$：

- 保留至少同樣多 required invariants；
- cost 不高於 $B_2$ ；
- uncertainty 不高於 $B_2$ ；
- 且 $B_2$ 沒有額外 unique witness；

可定義 candidate dominance：

$$
\boxed{
B_1
\succeq_{\mathcal Q}
B_2.
}
$$

只有在 dominance certificate 下才 prune $B_2$。

---

# 40. Prune 不等於 Delete History

即使 branch 被 prune，

仍應保存：

- branch ID；
- parent；
- prune reason；
- dominance/equivalence certificate；
- last state hash。

因此未來 ruleset 改變時可重新開啟。

---

# 41. Frontier Batch

從：

$$
\mathcal F_t
$$

選擇一個 batch：

$$
\boxed{
\mathcal B_t
\subseteq
\mathcal F_t.
}
$$

batch 不要求所有 actions pairwise syntactically independent。

但若要真正 parallel commit，必須滿足 batch safety。

---

# 42. Pairwise Safe Batch

最簡單條件：

$$
\forall A\neq B
\in
\mathcal B_t,
$$

都有：

$$
\mathsf{Ind}(A,B).
$$

這給出 pairwise-certified batch。

但 pairwise independence 不一定自動保證所有高階 joint invariants，因此仍要 postcheck。


# 43. Higher-Order Batch Conflict

即使：

$$
A
\mathrel{\mathsf{Ind}}
B,
$$

$$
B
\mathrel{\mathsf{Ind}}
C,
$$

$$
A
\mathrel{\mathsf{Ind}}
C,
$$

仍可能存在一個三元 invariant：

$$
I(A,B,C)
$$

在 joint execution 下失敗。

因此 pairwise independence 只是一個 sufficient candidate condition，不應被自動提升成 universal theorem。

---

# 44. Batch Safety Certificate

一個 parallel batch：

$$
\mathcal B_t
=
\{
A_1,\ldots,A_k
\}
$$

若要進 commit-capable execution，應形成：

$$
\boxed{
C_{\mathcal B}^{\mathrm{safe}}.
}
$$

它至少證明：

1. 所有 members fresh Legal；
2. hard dependencies 已滿足；
3. resource allocation 不衝突；
4. joint invariant 不被破壞；
5. merge / serialization contract 存在。

---

# 45. Parallel Execution 不等於直接共享 Mutable State

MWT-03 建議 parallel batch 先在：

- isolated staging states；
- copy-on-write branches；
- transactional snapshots；
- pure functional backends；

之一執行。

然後再由 merge / serialization certificate 決定是否 commit。

這能避免「看起來 independent，但實作共享 state 產生 race」的工程錯誤。

---

# 46. Staging Semantics

對 batch：

$$
\mathcal B_t
$$

從同一 parent stable state：

$$
S_t
$$

產生：

$$
\widetilde S_t^{A_1},
\ldots,
\widetilde S_t^{A_k}.
$$

這些是 staging results。

只有 merge / serializable reconstruction 通過後，才生成：

$$
S_{t+1}.
$$

---

# 47. Serializable Batch

若存在某個合法 linearization：

$$
L
=
(A_{\pi(1)},\ldots,A_{\pi(k)})
$$

使 parallel execution 的 externally relevant effect 相對 identity specification：

$$
\mathfrak I
$$

等價於：

$$
F_L(S_t),
$$

則稱 batch：

$$
\boxed{
\mathsf{Serializable}_{\mathfrak I}.
}
$$

serializability 是一種 commit certificate candidate。

---

# 48. Serializability 不要求實際逐步序列執行

如果 parallel implementation 可被證明等價於某個 serial schedule，

它仍然可以並行執行。

因此：

$$
\boxed{
\text{serializable}
\neq
\text{physically serial}.
}
$$

這一點與 transaction systems 的成熟觀念相容。

---

# 49. Conflict Graph 與 Serializability

對一個 batch：

$$
\mathcal B,
$$

可以建立 conflict / precedence graph：

$$
\boxed{
G_{\mathcal B}^{\mathrm{ser}}
=
(
\mathcal B,
E_{\mathrm{ser}}
).
}
$$

若某一 backend 使用標準 conflict-serializability criterion，acyclicity 可以成為其 serializability certificate 的一部分。

MWT 不宣稱所有 mathematical interactions 都可化約成 database transaction conflict graph。

它只是提供一個成熟後端。

---

# 50. Dependency Graph Precomputation

某些 workload 可以先建立 interaction dependency graph，再執行。

這與 database concurrency control 中「先解析 dependency，再 exploit parallelism」的工程路徑相容。

MWT 可以使用：

$$
\boxed{
\mathsf{PreSchedule}
}
$$

模式：

1. 先展開候選 interactions；
2. 建立 dependency/conflict graph；
3. 找 parallel frontier；
4. 再執行。

---

# 51. Online Scheduling

另一些 interaction 只有執行後才知道 dependency。

則使用：

$$
\boxed{
\mathsf{DynamicSchedule}
}
$$

模式：

1. 先執行一個合法 representative；
2. 觀察 read/write / bridge / invariant interactions；
3. 動態增加 backtrack points；
4. 探索必要替代順序。

這正是 DPOR 類方法對 MWT 特別有價值的地方。

---

# 52. Hybrid Scheduler

MWT 的正常 scheduler 更可能是：

$$
\boxed{
\mathsf{NCS}
=
\mathsf{StaticDependency}
+
\mathsf{DynamicInteractionDiscovery}
+
\mathsf{LegalityRecheck}.
}
$$

不是純 offline，也不是純 online。

---

# 53. Confluence

若兩條合法路徑：

$$
S
\overset{\gamma_1}{\longrightarrow}
S_1,
$$

$$
S
\overset{\gamma_2}{\longrightarrow}
S_2,
$$

存在合法後續：

$$
S_1
\overset{\eta_1}{\longrightarrow}
S^\ast,
$$

$$
S_2
\overset{\eta_2}{\longrightarrow}
S^\ast
$$

或至少：

$$
S_1'
\equiv_{\mathfrak I}
S_2',
$$

則可稱該分叉在指定 identity 下具有 candidate confluence。

---

# 54. Confluence 比 Commutativity 更寬

commutativity 要求：

$$
B(A(S))
\equiv
A(B(S)).
$$

confluence 只要求：

> 不同路徑最後仍可合法匯合。

所以：

$$
\boxed{
\text{commutation}
\Rightarrow
\text{local confluence candidate},
}
$$

但反向不必成立。

MWT merge layer 因此不能只會找 commutator。

---

# 55. Merge Operator

若兩支：

$$
B_1,
B_2
$$

需要合併，可提出：

$$
\boxed{
\mu:
(S_1,S_2)
\rightharpoonup
S^\ast.
}
$$

 $\mu$ 本身也是 operator。

因此它必須接受 MWT-02 legality judgment。

不能因名稱叫 merge 就自動合法。

---

# 56. Merge Certificate

合法 merge 至少需要：

$$
\boxed{
C_{\mu}
=
(
C_{\mathrm{domain}},
C_{\mathrm{id}},
C_{\mathrm{inv}},
C_{\mathrm{history}},
C_{\mathrm{loss}}
).
}
$$

如果 merge 丟失 branch-specific information，必須明示：

$$
\mathcal L_{\mu}.
$$

---

# 57. Merge 不等於 Homogenization

若兩個 branches 有不可約差異：

$$
D\neq\varnothing,
$$

MWT 可以收斂成：

$$
\boxed{
S^\ast
=
(
S_{\mathrm{shared}},
B_1,
B_2,
D
)
}
$$

而不是假裝得到單一同質 state。

因此：

$$
\boxed{
\text{global convergence}
\neq
\text{single value}.
}
$$

---

# 58. CRDT / Commutative Design Interface

在 distributed state backend 中，可以刻意設計操作使其 commutative / convergent。

CRDT 類思想提供一個成熟外部接口：

> 某些資料型別可以透過數學限制，使 replicas 在收到相同更新集合後 deterministic convergence。

MWT 可以把這類 backend 標記為：

$$
\boxed{
\mathsf{ConvergentBackend}.
}
$$

但 MWT 不假設所有 mathematical operators 都能被 CRDT 化。

---

# 59. Commutativity by Design

若某一 presentation 能把原本 noncommutative updates 重構為可交換 representation，

這可以降低 scheduler branch cost。

但轉換：

$$
T:
P_{\mathrm{noncomm}}
\to
P_{\mathrm{comm}}
$$

必須通過 MWT-01 fidelity 與 MWT-02 legality。

不能只因「容易平行」就接受語義損失。

---

# 60. Schedule Cost

每一 schedule / branch：

$$
\gamma
$$

可以有成本 profile：

$$
\boxed{
\kappa(\gamma)
=
(
c_{\mathrm{compute}},
c_{\mathrm{memory}},
c_{\mathrm{bridge}},
c_{\mathrm{proof}},
c_{\mathrm{communication}},
c_{\mathrm{human}}
).
}
$$

MWT 不要求把它壓成單一 scalar。

---

# 61. Scheduling Preference

只有在 schedules 都保持 required legality / invariants 後，才進：

$$
\boxed{
\mathsf{PreferenceLayer}.
}
$$

可以比較：

- cost；
- latency；
- coverage；
- novelty；
- proof maturity；
- human readability。

所以：

$$
\boxed{
\text{legality}
\prec
\text{scheduling optimization}.
}
$$

---

# 62. No Universal Best Schedule

因為不同 inquiry：

$$
\mathcal Q_1,
\mathcal Q_2
$$

可能有不同最重要的：

- throughput；
- proof depth；
- branch diversity；
- minimal memory；
- reproducibility。

所以 MWT 不預設：

$$
\boxed{
\exists\gamma^\ast
\text{ universally optimal for all goals}.
}
$$

scheduler optimization 永遠 goal-indexed。

---

# 63. Research-Relevance Score

對 exploratory branches，可以使用：

$$
\rho(B_i\mid\mathcal Q)
$$

表示 research relevance。

它可以由多個 signal 決定：

- 是否可能產生新 invariant；
- 是否可能反例；
- 是否覆蓋新 schedule class；
- 是否打開未探索 presentation；
- 是否高風險。

這是 branch ordering，不是 truth score。

---

# 64. Risk Score

對 commit-capable execution，另可定義：

$$
\chi(B_i)
$$

作 operational risk。

高風險 branch 可以要求：

- 更強 certificate；
- 更多 independent verifier；
- human approval；
- sandbox execution。

---

# 65. Branch Portfolio

在固定 budget 下：

$$
B_{\mathrm{total}},
$$

scheduler 可以選：

$$
\boxed{
\mathcal P_t^{\mathrm{branch}}
=
\{
B_{i_1},\ldots,B_{i_k}
\}
}
$$

作探索 portfolio。

目標不是選單一「最佳」 branch，而是維持：

- coverage；
- diversity；
- risk balance；
- expected information gain。

---

# 66. Branch Coverage

若 schedule classes 集合為：

$$
\mathcal T,
$$

目前探索 representatives：

$$
\mathcal R
\subseteq
\mathcal T,
$$

可定義 coverage metadata。

但在一般巨大 state space 中：

$$
|\mathcal T|
$$

可能未知。

因此 MWT 允許：

$$
\boxed{
\mathsf{CoverageUnknown}.
}
$$

而不是偽造百分比。

---

# 67. State-Space Estimation Interface

2026 年 DPOR state-space estimation 工作顯示：即使精確計數 Mazurkiewicz trace classes 困難，仍可在某些 bounded concurrent-program settings 以 sampling / stochastic methods估計探索空間規模。

MWT 可以把這類技術接成：

$$
\boxed{
\mathsf{BranchSpaceEstimator}.
}
$$

用途：

- 預估 branch budget；
- 預估 verification cost；
- 決定是否需要更強 reduction。

MWT 不把其特定複雜度結果直接泛化到所有數學世界。

---

# 68. Unknown Search Space 也是一級狀態

若 estimator 不適用，

runtime 應標：

$$
\boxed{
\mathsf{SearchSpaceUnknown}.
}
$$

這和 MWT-02 的 Undetermined 精神一致。

---

# 69. Backtracking Point

若執行中發現：

$$
A,B
$$

原先被當作 independent，

後來出現 noncommutative witness，

scheduler 應建立：

$$
\boxed{
\mathsf{BacktrackPoint}(k,A,B).
}
$$

從共同 prefix：

$$
\gamma_{0:k}
$$

重新展開替代順序。

---

# 70. Independence Revocation

若：

$$
C_{A,B}^{\mathrm{comm}}
$$

被撤銷，

所有使用該 certificate 做 schedule quotient 的結果必須進：

$$
\boxed{
\mathsf{ScheduleRevalidationQueue}.
}
$$

這使 reduction 本身也具有 provenance。

---

# 71. Persistent Schedule Certificate

每個 committed execution 至少保存：

$$
\boxed{
C_{\gamma}^{\mathrm{sched}}
=
(
\prec_H,
C_{\mathrm{comm}},
C_{\mathrm{branch}},
C_{\mathrm{merge}},
C_{\mathrm{commit}}
).
}
$$

所以結果可以回答：

> 為什麼這些順序被省略？  
> 為什麼這兩個 action 可以平行？  
> 為什麼只探索這支？  
> 為什麼最後可以 merge？

---

# 72. Deterministic Replay

若要求 deterministic replay，

除了 causal order：

$$
\prec_H
$$

外，

還需要保存：

- total-order tie-break；
- random seeds；
- external data snapshots；
- model versions；
- bridge versions；
- resource-sensitive effects。

否則「同一 path 名稱」不保證同一執行。

---

# 73. Replay Equivalence

若兩次 replay：

$$
R_1,
R_2
$$

不 bitwise identical，

仍可能：

$$
R_1
\equiv_{\mathfrak I}
R_2.
$$

因此 replay success 也需要 identity specification。

---

# 74. Multi-AI Agent Set

令：

$$
\boxed{
\mathcal A_t
=
\{
A_1,\ldots,A_m
\}
}
$$

為 execution agents。

每個 agent 有：

- capabilities；
- presentations；
- tools；
- memory；
- trust/certificate backend；
- resource quota。

---

# 75. Agent Capability

interaction：

$$
\alpha
$$

只能分派給：

$$
A_i
$$

若：

$$
\boxed{
\operatorname{Cap}(A_i)
\supseteq
\operatorname{Req}(\alpha).
}
$$

這是 scheduling eligibility，不是數學 truth 判定。

---

# 76. Agent Independence

多 AI 同時給相同答案不等於真正 independent verification。

需要記：

- model family；
- shared prompt；
- shared data；
- shared proof backend；
- shared code；
- shared training artifact if known。

因此 verifier diversity 也應有 provenance。

---

# 77. Agent Assignment

scheduler 可以建立：

$$
\boxed{
\sigma:
\mathcal B_t
\to
\mathcal A_t
}
$$

將 actions 分配給 agents。

若一個 action 需要多 agent 協作，可以：

$$
\sigma(\alpha)
\subseteq
\mathcal A_t.
$$

---

# 78. Agent Logical Clock

每個 agent 維護 local logical clock：

$$
L_i.
$$

event 發生時遞增；

接收 dependency message 時更新。

其目的不是模擬物理時間，而是建立 reproducible causal metadata。

---

# 79. Cross-Agent Message Edge

若：

$$
A_i
$$

的 event $e$ 產生 message / certificate：

$$
m
$$

被：

$$
A_j
$$

的 event $f$ 使用，

建立：

$$
\boxed{
e
\prec_H
f.
}
$$

如此 multi-AI 執行得到一個 causal DAG，而不需要中央全知時鐘。

---

# 80. Central Scheduler 與 Distributed Scheduler

MWT-03 不強制唯一 architecture。

### Central Scheduler

單一 NCS 維護：

$$
\mathcal G_t^I.
$$

優點：

- 一致 state；
- 容易 audit。

缺點：

- bottleneck；
- single point of failure。

### Distributed Scheduler

多 agent 各自維護局部 frontier，再交換 certificates / causality。

優點：

- scalability；
- fault tolerance。

缺點：

- reconciliation 更難。

兩者都可以是合法 backend。

---

# 81. Scheduler 本身也是 Presentation / Operator

NCS 不是站在 World 外面。

它本身有：

- state；
- rules；
- version；
- logs；
- assumptions。

因此 scheduler 可以被表示為：

$$
P_{\mathrm{sched}}
$$

並接受 MWT 自我審計。

---

# 82. Scheduler Rule Freeze

對一次 formal execution：

$$
\boxed{
\Sigma^{(v)}
=
\text{fixed scheduler policy}.
}
$$

AI 不得因分支太多就偷偷修改：

$$
\mathsf{Ind}
$$

定義並繼續當同一 run。

任何 scheduler policy change 都是：

$$
\boxed{
\mathsf{ScheduleRevisionEvent}.
}
$$

---

# 83. Scheduling Mode

MWT-03 v0.1 提供四種 mode：

### S1 — Conservative

沒有強 commutativity certificate 就 serial / branch。

### S2 — Certified Parallel

只並行已有 certificate pairs / batches。

### S3 — Exploratory Parallel

允許 sandbox 內 speculative parallelism，commit 前再驗證。

### S4 — Reduction-Oriented

以 DPOR / trace reduction 為主要 search strategy。

mode 必須寫進 provenance。

---

# 84. Stable State

定義：

$$
\boxed{
S_t^{\mathrm{stable}}
}
$$

為：

> 已通過 commit policy、所有 required postconditions 與當前 invariant checks 的 canonical runtime state。

staging、sandbox、conflicted branches 都不等於 stable state。

---

# 85. Stable-World Commit

對 batch / path：

$$
\Gamma
$$

要生成：

$$
\boxed{
C_{\Gamma}^{\mathrm{commit}}.
}
$$

最低可以由下列之一支持：

1. certified serializable；
2. certified commuting；
3. certified confluent；
4. certified explicit merge。

再加：

- postcheck；
- no unresolved hard blocker；
- provenance complete。

---

# 86. Commit Criterion

形式上：

$$
\boxed{
\operatorname{Commit}(\Gamma)=1
}
$$

若：

$$
\operatorname{FreshLegal}(\Gamma)=1,
$$

$$
\operatorname{PostInvariant}(\Gamma)=1,
$$

$$
\operatorname{MergeOrSerialCert}(\Gamma)=1,
$$

且：

$$
\operatorname{HardConflict}(\Gamma)=0.
$$

---

# 87. Commit 不是 Truth Seal

即使一個 mathematical result 被 commit 到 stable runtime，

它也只是：

> 在指定 foundation、presentation、legality、scheduler 與 verification level 下，目前穩定接受。

它仍可以因：

- 新反例；
- proof bug；
- bridge revision；
- data correction；

被 future revision invalidated。

因此：

$$
\boxed{
\text{stable}
\neq
\text{eternally true}.
}
$$

---

# 88. Rollback

若 commit 後某 certificate 被撤銷，

系統可：

$$
\boxed{
S_t
\rightarrow
S_{t-k}
}
$$

或：

$$
S_t
\rightarrow
S_t'
$$

做 compensating repair。

rollback 本身也要有 legality。

---

# 89. Compensating Action

有些外部 action 不可物理 rollback。

例如已送出 message、已寫入外部 ledger、已操作機器。

則只能建立 compensating action：

$$
\boxed{
A^{-1}_{\mathrm{operational}}
}
$$

它不一定是真正 algebraic inverse。

MWT 必須區分：

$$
\text{mathematical inverse}
\neq
\text{operational compensation}.
$$

---

# 90. Irreversible Event

若 event：

$$
e
$$

不可 rollback，

應標：

$$
\boxed{
\mathsf{Irreversible}(e).
}
$$

scheduler 對 irreversible events 應提高 pre-commit certificate threshold。

---

# 91. Checkpoint

stable world 可以週期性產生：

$$
\boxed{
K_t
=
(
S_t,
H_t,
C_t,
V_t
).
}
$$

其中：

- state；
- history hash；
- certificate root；
- version set。

這是可重放 checkpoint。

---

# 92. Global Interaction Epoch

為工程方便，可把 runtime 分成：

$$
E_0,E_1,\ldots
$$

每個 epoch：

1. freeze relevant rule versions；
2. compute frontier；
3. schedule；
4. execute staging；
5. merge / serial-check；
6. postcheck；
7. commit；
8. checkpoint。

epoch 不是物理時間 primitive。

只是 runtime orchestration unit。

---

# 93. Epoch Barrier 不是強制全域同步

某些 backend 可局部 commit。

所以 epoch 不必：

> 等全世界所有 agent 都完成。

可以使用 nested / regional epochs。

這延續 MWT 的局部有限、全域無界精神。

---

# 94. Nested Scheduler

一個 interaction node：

$$
\alpha
$$

本身可以展開成內部 subgraph：

$$
\mathcal G_{\alpha}.
$$

因此 scheduler 支援：

$$
\boxed{
\text{scheduler inside scheduler}.
}
$$

父層只看到：

- precondition；
- output；
- certificate；
- cost；
- state。

內層可以有大量 branch。

---

# 95. Hierarchical Compression

對已證明 stable 的 subgraph：

$$
\mathcal G_{\alpha}
$$

可以壓成 macro-action：

$$
\boxed{
\widehat\alpha.
}
$$

但必須保留 expansion pointer：

$$
\widehat\alpha
\rightsquigarrow
\mathcal G_{\alpha}.
$$

所以壓縮不刪 proof history。

---

# 96. Macro-Action Revalidation

若：

$$
\mathcal G_{\alpha}
$$

內部 dependency / certificate 改變，

macro-action：

$$
\widehat\alpha
$$

必須 invalidated。

不能永久把舊壓縮當 atomic truth。

---

# 97. Resolution Change

同一 scheduler 可以在不同解析度：

$$
\lambda_1,
\lambda_2
$$

看到不同 node structure。

高層：

$$
\widehat\alpha
$$

是一個 action。

低層：

$$
\alpha_1,\ldots,\alpha_k.
$$

因此：

$$
\boxed{
\text{atomicity is resolution-relative}.
}
$$

---

# 98. Scheduler Re-indexing

如果某個 branch 太複雜，

AI 可以對一個 subgraph 做：

$$
\boxed{
\mathsf{ReIndex}
(
\mathcal G
)
}
$$

建立新的 macro-object。

這與 TADC / RDSS 的重索引精神相容。

---

# 99. Noncommutative Defect

對兩個 actions：

$$
A,B,
$$

若有 metric / discrepancy backend，可定義：

$$
\boxed{
\delta_{A,B}(S)
=
d
(
B(A(S)),
A(B(S))
).
}
$$

這是 schedule difference 的一種量化。

但沒有 metric 時仍可以使用 symbolic witness：

$$
B(A(S))
\not\equiv_{\mathfrak I}
A(B(S)).
$$

---

# 100. Defect Propagation

若後續 path：

$$
T
$$

會放大差異，

則初始 noncommutative defect 可能影響遠端結果。

因此 scheduler 不只關心：

$$
\delta_{A,B}
$$

是否非零，

還關心：

$$
\boxed{
\operatorname{Propagate}
(
\delta_{A,B},
T
).
}
$$

這與 Series B 的局部缺陷傳播精神直接相連。


# 101. Defect Threshold 不能自動取代 Identity

若：

$$
\delta_{A,B}(S)
<
\varepsilon,
$$

只能說在某 metric 下差異小。

不能自動推出：

$$
B(A(S))
\equiv_{\mathfrak I}
A(B(S)).
$$

除非 identity specification 明示：

$$
d(x,y)<\varepsilon
\Rightarrow
x\equiv_{\mathfrak I}y.
$$

---

# 102. Approximate Commutation

若在指定 domain：

$$
\delta_{A,B}(S)
\leq
\varepsilon,
$$

可以定義：

$$
\boxed{
A
\mathrel{\mathsf{Comm}^{\varepsilon}}
B.
}
$$

但這只能進允許 approximate semantics 的 scheduler mode。

strict proof mode 不應自動使用。

---

# 103. Approximate Merge

同理，branches：

$$
S_1,S_2
$$

可以在：

$$
d(S_1,S_2)\leq\varepsilon
$$

時 candidate merge。

但必須把：

$$
\varepsilon
$$

與 metric backend 寫入 merge certificate。

---

# 104. Global Invariant Ledger

scheduler 需要讀取：

$$
\boxed{
\mathsf{IVL}
}
$$

即 MWT-01 的 Invariant Ledger。

每個 batch / branch 都應知道：

- hard invariants；
- observer invariants；
- branch-local invariants；
- merge invariants；
- proof invariants。

排程不只是「避免資料 race」，而是避免破壞當前 mathematical contract。

---

# 105. Schedule Invariant

可以定義：

$$
I_{\mathrm{sched}}
$$

例如：

- dependency respected；
- no illegal commit；
- all irreversible actions certified；
- history hash continuous；
- no missing bridge version。

這些 invariant 作用於 scheduler 自身。

---

# 106. Global Interaction Ledger

MWT-03 新增：

$$
\boxed{
\mathsf{GIL}
=
\text{Global Interaction Ledger}.
}
$$

至少記錄：

```text
interaction_id
event_id
branch_id
agent_id
predecessors
conflicts
resource_edges
commutativity_certificates
legality_ref
staging_state_ref
commit_status
```

---

# 107. Schedule Ledger

再新增：

$$
\boxed{
\mathsf{SL}
=
\text{Schedule Ledger}.
}
$$

保存：

- partial order；
- chosen linearization if any；
- skipped equivalent linearizations；
- reduction certificates；
- backtrack points；
- branch budget；
- unexplored classes。

---

# 108. Branch Ledger

$$
\boxed{
\mathsf{BL}
}
$$

保存：

```text
branch_id
parent_branch
prefix_path
current_state
open_frontier
equivalence_class
prune_reason
merge_target
status
```

---

# 109. Agent Ledger

$$
\boxed{
\mathsf{AL}
}
$$

保存：

- agent capabilities；
- assigned tasks；
- event clocks；
- outputs；
- failures；
- verifier provenance。

這使 multi-AI execution 可被 audit。

---

# 110. Scheduler Engine

核心 runtime：

$$
\boxed{
\mathsf{NCS}
=
\text{Noncommutative Scheduler}.
}
$$

輸入：

$$
(
S_t,
\mathcal G_t^I,
\mathcal F_t,
\Sigma^{(v)},
B_t
)
$$

輸出：

$$
(
\mathcal B_t,
\mathcal P_t^{\mathrm{branch}},
C_{\mathrm{sched}}
).
$$

---

# 111. Scheduler Policy

$$
\Sigma^{(v)}
$$

至少包含：

- execution mode；
- independence criteria；
- branch budget；
- resource budget；
- risk thresholds；
- commit threshold；
- reduction backend；
- merge policy；
- replay policy。

---

# 112. Dynamic Frontier Engine

$$
\boxed{
\mathsf{DFE}
}
$$

負責：

- predecessor completion；
- fresh legality；
- certificate expiry；
- resource availability；
- newly discovered conflicts。

它不直接決定最佳順序。

只維護目前 enabled frontier。

---

# 113. Independence Engine

$$
\boxed{
\mathsf{IE}
}
$$

輸入：

$$
(A,B,S,\Gamma,\mathfrak I,\mathcal Q)
$$

輸出：

$$
\{
\mathsf{Independent},
\mathsf{Dependent},
\mathsf{Undetermined},
\mathsf{Conflicted}
\}.
$$

這裡也沿用四態精神。

如果 independence 不確定，conservative mode 不應把兩者 parallelize。

---

# 114. Reduction Engine

$$
\boxed{
\mathsf{RE}
}
$$

維護：

- swap certificates；
- schedule equivalence；
- representative selection；
- backtracking；
- coverage metadata。

它可以接 DPOR 類 backend，但不被固定成單一算法。

---

# 115. Merge Engine

$$
\boxed{
\mathsf{ME}
}
$$

判定：

- branches 是否 identity-equivalent；
- 是否 serializable；
- 是否 confluent；
- 是否需要 explicit merge operator；
- loss 是否允許。

---

# 116. Commit Engine

$$
\boxed{
\mathsf{CE}
}
$$

只接受：

$$
C_{\Gamma}^{\mathrm{commit}}
$$

完整的 batch/path。

commit engine 不做研究猜測。

它是 stable-world 最後一道邊界。

---

# 117. Reference Scheduler：最低目標

本 Source Pack 附帶：

```text
mwt03_scheduler_reference.py
```

它不模擬真正並行 runtime。

只固定 v0.1 的幾個最低語義：

1. dependency DAG frontier；
2. contextual pairwise independence input；
3. pairwise-independent batch 選擇；
4. deterministic tie-break；
5. branch suggestion for noncommuting enabled pairs；
6. committed-node frontier update。

這是 reference semantics，不是 optimal scheduler。

---

# 118. Reference Data Model

最低 interaction node：

```text
InteractionNode:
  node_id
  legal
  predecessors
  conflicts
  resources
  irreversible
```

independence certificate：

```text
IndependenceCertificate:
  left
  right
  valid
  identity_scope
  context_version
```

scheduler state：

```text
SchedulerState:
  committed
  pending
  branches
  epoch
```

---

# 119. Basic Batch Selection

最簡單 conservative algorithm：

```text
frontier = all fresh-legal nodes with committed predecessors

batch = []

for node in deterministic_order(frontier):
    if node is certified independent of every node in batch:
        batch.append(node)

return batch
```

它可能不是最大 batch。

但容易 audit。

未來可換成：

- maximum independent set approximations；
- resource-aware packing；
- priority scheduling；
- distributed selection。

---

# 120. Branch Suggestion

對 frontier 中：

$$
A,B
$$

若：

- 兩者都 enabled；
- 無 hard order；
- independence 未成立；
- 兩種順序沒有已知 illegal；
- inquiry 要求 order sensitivity；

則建立：

```text
branch:
  [A, B]
  [B, A]
```

之後再由 reduction engine 判定是否可 quotient。

---

# 121. MWT-03 Minimal Constitution

v0.1 固定二十條：

### S1 — Partial Order First

全域 scheduler 不預設唯一 total order。

### S2 — Causality Is Not Tie-Break Order

total-order extension 不得自動升格成 causal relation。

### S3 — Frontier Is Dynamic

enabled set 必須隨 state / legality 更新。

### S4 — Independence Is Contextual

交換／獨立性需帶 domain、context、identity 與 version。

### S5 — Both Orders Must Be Admissible for Swap Reduction

若其中一個順序非法，不得以交換等價刪除合法順序。

### S6 — Commutation Is Inquiry-Relative

final-state 等價不自動等於 history 等價。

### S7 — Genuine Noncommutativity Must Be Preserved

有有效 noncommutative witness 的 branches 不得被 quotient。

### S8 — Branching Is Legal

多 branch 是正常研究狀態，不是錯誤。

### S9 — Branch Space May Be Incomplete

超出 budget 時要標記 incomplete coverage。

### S10 — Pruning Requires a Reason

每次 prune 必須有 equivalence、dominance、resource 或 policy reason。

### S11 — Parallelism Requires Certification

strict commit mode 不因「看起來獨立」就平行 commit。

### S12 — Batch Safety Exceeds Pairwise Safety

高階 joint invariants 仍需 postcheck。

### S13 — Merge Is an Operator

merge 必須自己通過 legality。

### S14 — Convergence Need Not Homogenize

不可約 branch differences 可保留。

### S15 — Commit Requires Stable Certificate

跑完不等於可提交。

### S16 — Stable Does Not Mean Eternal Truth

stable result 可因 future evidence 被撤銷。

### S17 — Scheduler Policy Is Versioned

同一 run 不得偷偷改 scheduler policy。

### S18 — Multi-AI Events Need Causal Provenance

agent output 必須可追溯 dependency / message relation。

### S19 — Atomicity Is Resolution-Relative

macro-action 可以展開，但 expansion pointer 必須保留。

### S20 — Global Does Not Mean Simultaneous

MWT 全域執行是全域治理的 partial-order orchestration，不是全部一起跑。

---

# 122. 命題：Frontier Safety

若：

$$
\alpha
\in
\mathcal F_t,
$$

則依定義：

$$
\operatorname{Pred}(\alpha)
\subseteq
\operatorname{Committed}_t
$$

且：

$$
\operatorname{FreshLegal}_t(\alpha)=1.
$$

因此 frontier 不包含已知 predecessor 未滿足或 freshness legality 失效的 interactions。

---

# 123. 命題：Independent Adjacent Swap Preserves Declared Contract

若：

$$
\mathsf{Ind}_{\Gamma,S,\mathfrak I}(A,B)
$$

且 independence certificate 定義中包含：

$$
B(A(S))
\equiv_{\mathfrak I,\mathcal Q}
A(B(S)),
$$

則由定義：

$$
\boxed{
(A,B)
\leftrightsquigarrow
(B,A)
}
$$

對 $\mathfrak I,\mathcal Q$ 的 declared contract sound。

此命題不宣稱兩條 history 在所有可能 inquiry 下相同。

---

# 124. 命題：Trace Quotient Does Not Collapse Certified Noncommutativity

若存在：

$$
C_{A,B}^{\mathrm{noncomm}}
$$

證明：

$$
B(A(S))
\not\equiv_{\mathfrak I}
A(B(S)),
$$

則 $A,B$ 不滿足該 identity scope 下的 independence definition。

因此不能使用本文 adjacent-swap rule 將：

$$
(A,B)
$$

與：

$$
(B,A)
$$

放入同一 contextual trace class。

---

# 125. 命題：Branch Merge Requires More Than Equal Labels

即使兩個 branches 都標記：

$$
\text{Solved},
$$

也不能推出：

$$
S_1\equiv S_2.
$$

因為 label equality 不是 identity specification。

必須由 merge / identity certificate 判定。

---

# 126. 命題：Serializable Parallel Batch Has a Sequential Witness

由 serializability 定義，若：

$$
\mathcal B
$$

是 $\mathfrak I$ -serializable，

則存在 linearization：

$$
L
$$

使其 externally relevant effect：

$$
\operatorname{Eff}(\mathcal B)
\equiv_{\mathfrak I}
F_L(S).
$$

因此 parallel implementation 有一個 sequential witness。

---

# 127. 命題：Total-Order Tie Break Does Not Add Causality

若：

$$
e_i,e_j
$$

在：

$$
\prec_H
$$

不可比較，

但 total-order extension 選：

$$
e_i<_T e_j,
$$

則由 S2：

$$
e_i<_T e_j
$$

不能單獨作為：

$$
e_i\prec_H e_j
$$

的證書。

---

# 128. 條件定理：Certified Pairwise Batch

設：

$$
\mathcal B
=
\{
A_1,\ldots,A_k
\}
$$

滿足：

1. 所有 $A_i$ fresh Legal；
2. 所有 predecessors committed；
3. 每對 $A_i,A_j$ 具有 strong commutativity certificate；
4. certificates 對同一 identity / invariant scope 有效；
5. 無 resource conflict；
6. joint postcheck 成功。

則任意 linearization：

$$
L_{\pi}
$$

在 declared scope 下得到等價結果。

這是強條件下的 batch-order independence。

---

# 129. 條件定理：Branch Rejoin

若：

$$
S
\overset{\gamma_1}{\to}
S_1
$$

與：

$$
S
\overset{\gamma_2}{\to}
S_2
$$

且存在合法：

$$
\eta_1,\eta_2
$$

使：

$$
F_{\eta_1}(S_1)
\equiv_{\mathfrak I}
F_{\eta_2}(S_2),
$$

則兩 branch 在 $\mathfrak I$ 下有共同 rejoin candidate。

若 merge certificate 完整，可以壓成共同後繼 macro-node。

---

# 130. 研究猜想：Global Interaction Compression

對大量 AI-native mathematical workloads，若能建立足夠高品質的 contextual independence、identity 與 invariant certificates，則實際需要探索的 schedule classes 可能遠少於所有 raw interleavings。

這是 MWT 的重要工程猜想。

它不主張一般情況保證指數級縮減。

---

# 131. 研究猜想：Dynamic Locality Emergence

若 scheduler 從大型 global interaction graph 出發，再由 dependency、legality、resource 與 noncommutativity 自動切出可並行 clusters，則部分「局部問題分解」可以由 runtime 動態產生，而不是全部由人類事先決定。

---

# 132. 研究猜想：Multi-AI Mathematical Runtime

當多 AI 可以共享：

- presentation registry；
- legality engine；
- causal ledger；
- schedule certificate；
- branch ledger；

則 mathematical research 可以從「多 AI 各自聊天後人工整合」提升為真正共享的 causal computation graph。

---

# 133. 研究猜想：Branch Diversity as Mathematical Signal

在未解問題中，不同 noncommutative branches 長期不能 merge 可能本身就是結構訊號：

$$
\boxed{
\text{persistent branch separation}
}
$$

可能對應：

- hidden invariant；
- phase boundary；
- missing variable；
- incompatible foundation；
- genuine multiple solution regimes。

因此 branch 不只是一種計算成本，也可能是數學資訊。

---

# 134. 開放問題

### O1 — Contextual Trace Theory

如何建立 state-dependent independence 的完整代數與等價理論？

### O2 — Scheduler Complexity

MWT scheduler 在一般 heterogeneous presentation graph 上的 complexity class 如何描述？

### O3 — High-Order Independence

如何避免只靠 pairwise commutativity 漏掉高階 interaction？

### O4 — Branch-Equivalence Verification

跨 presentation branches 的等價如何低成本驗證？

### O5 — Merge Synthesis

AI 能否自動合成合法 merge operator？

### O6 — Distributed Commit

多 AI、跨機器 runtime 如何維持 stable-world commit？

### O7 — Irreversible External Actions

如何安全整合不可 rollback 的現實操作？

### O8 — Dynamic Policy Revision

scheduler rules 改版時，哪些舊 schedule certificates 可保留？

### O9 — World-Scale Coverage

當 branch space 無法精確計數時，如何報告可信 coverage？

### O10 — Convergence vs Preservation

何時應 merge，何時應永久保留 branching structure？

---

# 135. 與外部成熟理論的接口

MWT-03 不宣稱重新發明：

- partial orders；
- logical clocks；
- Mazurkiewicz traces；
- partial-order reduction；
- DPOR；
- serializability；
- transaction dependency graphs；
- confluence；
- CRDT；
- distributed commit。

這些都是成熟研究方向。

MWT 的候選增量位於：

$$
\boxed{
\begin{aligned}
&\text{cross-presentation legality}\\
+&\text{contextual identity-relative commutation}\\
+&\text{noncommutative mathematical branching}\\
+&\text{certificate-governed schedule quotient}\\
+&\text{multi-AI causal execution}\\
+&\text{stable-world transactional commit}.
\end{aligned}
}
$$

---

# 136. Lamport Interface

分散系統中，事件之間的 happened-before relation 提供 partial order；沒有 causal relation 的事件不必被認為具有一個內在可觀察的唯一先後。

MWT 採這個成熟精神，將：

$$
\prec_H
$$

作 multi-AI event causality backend。

但 MWT 的 event 不只軟體 message event，也可能是：

- theorem derivation；
- bridge construction；
- simulation；
- proof verification；
- branch merge。

---

# 137. DPOR Interface

Flanagan–Godefroid 的 Dynamic Partial-Order Reduction 展示：

> 可以從實際 interleaving 動態識別 interaction / backtracking，避免完整枚舉所有 concurrent schedules。

MWT 將其放入 Reduction Engine。

但 MWT 的 independence 需要額外知道：

- presentation；
- identity；
- legality；
- invariant；
- observer。

所以不直接宣稱原 DPOR algorithm 可不修改地處理所有 MWT interactions。

---

# 138. 2026 State-Space Estimation Interface

2026 年 PLDI 工作進一步研究 DPOR induced Mazurkiewicz trace-equivalence classes 的數量估計，顯示 branch-space 規模本身可以成為 scheduling resource allocation 的研究對象。

MWT 因而將：

$$
\mathsf{BranchSpaceEstimator}
$$

列為可選 runtime module。

---

# 139. Transaction / Serializability Interface

transaction research 長期研究：

- precedence；
- conflicts；
- serializable schedules；
- batch scheduling；
- commit certification。

MWT 將這些方法視為 stateful mathematical interactions 的重要 backend。

但數學世界中的 equivalence 可能比 database final-state equality 更複雜，因此 serializability 必須帶：

$$
\mathfrak I
$$

與 inquiry contract。

---

# 140. CRDT Interface

commutative / conflict-free replicated data structures 顯示：

> 若從資料型別與操作設計層就建立 commutativity / convergence，分散式同步可以減少 coordination。

MWT 因此允許「為 scheduler 重新設計 presentation」。

但：

$$
\boxed{
\text{easier concurrency}
\neq
\text{faithful mathematics}.
}
$$

任何 commutativizing translation 都要接受 MWT-01 fidelity audit。

---

# 141. 與 Series B 的接口

Series B 已把：

$$
\delta_{A,B}(x)
=
d(B(A(x)),A(B(x)))
$$

理解為關係順序差，

並將長路徑、holonomy、observer transport 與 covariance 納入同一線。

MWT-03 把這些數學對象正式接進 scheduler：

- $\delta$ 成為 noncommutative witness；
- ordered path 成為 schedule；
- observer transport 成為 cross-agent / cross-presentation edge；
- holonomy 成為 closed schedule history effect；
- covariance 成為 merge / observer equivalence gate。

---

# 142. 與 RDSS 的接口

RDSS 中：

$$
\text{State}
\leftrightarrow
\text{Container}
\leftrightarrow
\text{Process}
$$

的尺度相對性，在 MWT-03 變成 nested scheduler：

- 高層 action；
- 中層 subgraph；
- 低層 events。

因此一個 node 是否 atomic 不是絕對的，而依 resolution。

---

# 143. 與差合化的接口

可把 scheduler 高階 orchestration 暫時看作：

$$
\mathsf E
\rightarrow
\mathsf L
\rightarrow
\mathsf C.
$$

其中：

- $\mathsf E$：展開 branch / presentation / schedule；
- $\mathsf L$：建立 dependency / bridge / commutation relations；
- $\mathsf C$：schedule quotient / merge / stable commit。

但 MWT-03 不把這三個操作宣稱為 World 的唯一 primitives。

---

# 144. 與動態不動點精神的接口

每個 stable state：

$$
S_t^{\mathrm{stable}}
$$

只是相對：

$$
(
\Lambda^{(v)},
\Sigma^{(v)},
\mathfrak I,
\mathcal Q
)
$$

的暫時閉合。

新 branch、新 certificate、新反例都可能使它重新展開。

因此：

$$
\boxed{
\text{stable commit}
\neq
\text{final closure}.
}
$$

---

# 145. MWT-01、02、03 的三層組合

MWT-01：

$$
\boxed{
\text{What can represent the World?}
}
$$

MWT-02：

$$
\boxed{
\text{What may act?}
}
$$

MWT-03：

$$
\boxed{
\text{In what partial order may legal actions execute and commit?}
}
$$

因此目前得到：

$$
\boxed{
\mathbf W
\Rightarrow
\mathcal G_t^P
\Rightarrow
\mathcal I_t^+
\Rightarrow
\mathcal G_t^I
\Rightarrow
S_{t+1}^{\mathrm{stable}}.
}
$$

---

# 146. 仍未完成的部分

MWT-03 尚未完成：

- 世界狀態 canonical runtime definition；
- branch convergence 的完整數學；
- global expansion / contraction governance；
- memory / compression hierarchy；
- proof-object persistence；
- long-horizon world evolution。

因此下一篇不應再只談 scheduler。

---

# 147. 下一篇接口

建議：

# **MWT-04：World State, Branch Convergence, and Dynamic Fixed Points**

正式回答：

$$
\boxed{
\text{經過大量合法、非交換、分支與 merge 後，
什麼叫「目前的數學世界狀態」？}
}
$$

核心需要：

- stable core；
- unresolved branch bundle；
- conflict set；
- proof/certificate roots；
- history compression；
- dynamic fixed point；
- reopen conditions；
- world-state versioning。

MWT-03 讓世界開始動。

MWT-04 才定義：

> 動過之後，「現在」究竟是什麼。

---

# 148. 一句話版

> **MWT-03 將數學世界中的合法 interactions 組織成帶多種邊的 Global Interaction Graph，並以 partial order 而非唯一 total order 作為預設歷史；scheduler 只有在 context、identity、invariant 與 legality 都允許時才把 actions 視為可交換，並利用 contextual trace equivalence 壓縮純排序冗餘，對真正非交換順序建立 branches。分支在有限 budget 下以證書化 reduction、dominance、relevance 與 state equivalence 控制；multi-AI 執行以 causal event order 保存 provenance；任何並行 batch 或 branch merge 只有在 serializable、commuting、confluent 或 explicit certified merge 的條件下才能寫入 stable world state。**

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $\mathcal G_t^I$ | Global Interaction Graph |
| $E^{\mathrm{dep}}$ | dependency edges |
| $E^{\mathrm{ord}}$ | explicit order edges |
| $E^{\mathrm{conf}}$ | conflict edges |
| $E^{\mathrm{res}}$ | resource edges |
| $E^{\mathrm{inv}}$ | invariant-coupling edges |
| $\prec_H$ | causal happened-before partial order |
| $<_T$ | optional total-order extension |
| $\mathcal F_t$ | dynamic frontier |
| $\mathsf{Ind}_{\Gamma,S,\mathfrak I}$ | contextual independence |
| $C_{A,B}^{\mathrm{comm}}$ | commutativity certificate |
| $C_{A,B}^{\mathrm{noncomm}}$ | noncommutativity witness |
| $\gamma$ | schedule / ordered path |
| $\approx_{\Gamma,\mathfrak I}$ | contextual trace equivalence |
| $\mathcal B_t$ | scheduled batch |
| $B_i$ | branch |
| $\mu$ | merge operator |
| $C_\mu$ | merge certificate |
| $C_\Gamma^{\mathrm{commit}}$ | stable commit certificate |
| $\mathsf{NCS}$ | Noncommutative Scheduler |
| $\mathsf{DFE}$ | Dynamic Frontier Engine |
| $\mathsf{IE}$ | Independence Engine |
| $\mathsf{RE}$ | Reduction Engine |
| $\mathsf{ME}$ | Merge Engine |
| $\mathsf{CE}$ | Commit Engine |

---

# 附錄 B：v0.1 非主張清單

MWT-03 不主張：

1. 所有合法 interactions 都存在最優排程；
2. 所有 dependency graphs 都是 DAG；
3. 所有 noncommutative branches 都能完整探索；
4. pairwise commutativity 保證任意高階 joint safety；
5. final-state equality 等於 history equality；
6. observational commutativity 等於 World-level commutativity；
7. DPOR 可直接無修改套用所有 MWT interactions；
8. Mazurkiewicz trace equivalence 足以描述所有數學 history；
9. 所有 batches 都應追求 serializability；
10. 所有 branches 最後都能 merge；
11. confluence 等於 commutativity；
12. CRDT 能表示所有數學作用；
13. total-order commit log 就是 causal history；
14. logical clock 是物理時間；
15. multi-AI agreement 等於 independent verification；
16. scheduler policy 可在同一 run 中無紀錄改變；
17. stable commit 等於永恆真理；
18. MWT 已解決一般 state explosion；
19. branch pruning 不會有任何資訊損失；
20. AI 可以不受 resource bound 地維持無限 schedule space。

---

# 附錄 C：外部研究接口與參考文獻

1. Leslie Lamport, **Time, Clocks, and the Ordering of Events in a Distributed System**, *Communications of the ACM*, 21(7), 1978, pp. 558–565.  
2. Cormac Flanagan and Patrice Godefroid, **Dynamic Partial-Order Reduction for Model Checking Software**, POPL 2005, pp. 110–121. DOI: 10.1145/1040305.1040315.  
3. A. R. Balasubramanian, Mohammad Hossein Khoshechin Jorshari, Rupak Majumdar, Umang Mathur, and Minjian Zhang, **State Space Estimation for DPOR-Based Model Checkers**, *Proceedings of the ACM on Programming Languages*, PLDI 2026, Article 213. DOI: 10.1145/3808291.  
4. Mihai Letia, Nuno Preguiça, and Marc Shapiro, **CRDTs: Consistency without Concurrency Control**, 2009, arXiv:0907.0929.  
5. Marc Shapiro and Nuno Preguiça, **Designing a Commutative Replicated Data Type**, 2007, arXiv:0710.1784.  
6. Eric Koskinen and Matthew Parkinson, **The Push/Pull Model of Transactions**, PLDI 2015.  
7. Chang Yao et al., **DGCC: A New Dependency Graph based Concurrency Control Protocol for Multicore Database Systems**, 2015, arXiv:1503.03642.  
8. Huyen T. T. Nguyen et al., **Quasi-Optimal Partial Order Reduction**, 2018, arXiv:1802.03950.  
9. Marek Chalupa et al., **Data-Centric Dynamic Partial Order Reduction**, 2016, arXiv:1610.01188.  

---

# 附錄 D：內部依賴

MWT-03 直接依賴：

- 《MWT-01：World Primitive 與 Presentation Theory》
- 《MWT-02：Global Legality Calculus》
- Series B《非交換缺陷與關係順序》
- Series B《局部順序差到全域阻塞》
- Series B《路徑傳輸、Holonomy 與關係記憶》
- Series B《觀察者轉換與關係協變性》
- RDSS《狀態、容器與存在》
- 《差合化的保真擴張》
- 《分域算子本體論》

本文將這些既有接口組合成 scheduler 層，不取代其原始用途。

